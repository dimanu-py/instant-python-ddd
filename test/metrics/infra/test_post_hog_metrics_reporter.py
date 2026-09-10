import json
import tempfile
from pathlib import Path

import pytest
import vcr
from vcr.request import Request

from instant_python.metrics.infra.post_hog_config import PostHogConfig
from instant_python.metrics.infra.post_hog_metrics_reporter import PostHogMetricsReporter
from instant_python.metrics.infra.user_identity_manager import UserIdentityManager
from test.metrics.domain.error_metrics_event_mother import ErrorMetricsEventMother
from test.metrics.domain.usage_metrics_event_mother import UsageMetricsEventMother


def filter_api_key(request) -> Request:
    """Filter api_key from request body before recording"""
    if request.body:
        body = json.loads(request.body.decode("utf-8"))
        body["api_key"] = "****"
        request.body = json.dumps(body).encode("utf-8")
    return request


posthog_vcr = vcr.VCR(
    cassette_library_dir=str(Path(__file__).parent / "cassettes"),
    record_mode="once",
    filter_headers=["Authorization"],
    before_record_request=filter_api_key,
)


@pytest.mark.integration
class TestPostHogMetricsReporter:
    @posthog_vcr.use_cassette("success_posthog_reporter.yml")
    def test_should_send_metrics_to_posthog(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config = PostHogConfig()
            user_identity_manager = UserIdentityManager(config_dir=Path(temp_dir))
            reporter = PostHogMetricsReporter(config=config, user_identity_manager=user_identity_manager)
            metrics = UsageMetricsEventMother.any()

            reporter.send_success(metrics)

    @posthog_vcr.use_cassette("error_posthog_reporter.yml")
    def test_should_send_error_metrics_to_posthog(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config = PostHogConfig()
            user_identity_manager = UserIdentityManager(config_dir=Path(temp_dir))
            reporter = PostHogMetricsReporter(config=config, user_identity_manager=user_identity_manager)
            metrics = ErrorMetricsEventMother.any()

            reporter.send_error(ValueError(), metrics)
