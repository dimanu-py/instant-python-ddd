import pytest
from doublex import ANY_ARG, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.metrics.application.usage_metrics_sender import UsageMetricsSender
from instant_python.metrics.domain.metrics_reporter import MetricsReporter
from test.metrics.domain.config_snapshot_mother import ConfigSnapshotMother


@pytest.mark.unit
class TestUsageMetricsSender:
    def test_should_send_usage_metrics_event(self) -> None:
        reporter = Mock(MetricsReporter)
        usage_metrics_sender = UsageMetricsSender(reporter=reporter)

        expect_call(reporter).send_success(ANY_ARG)

        usage_metrics_sender.execute_on_success(command_name="init", config_snapshot=ConfigSnapshotMother.any())

        expect(reporter).to(have_been_satisfied)

    def test_should_send_error_metrics_event(self) -> None:
        reporter = Mock(MetricsReporter)
        usage_metrics_sender = UsageMetricsSender(reporter=reporter)
        error = ValueError("Test error")

        expect_call(reporter).send_error(error, ANY_ARG)

        usage_metrics_sender.execute_on_failure(command_name="init", error=error)

        expect(reporter).to(have_been_satisfied)
