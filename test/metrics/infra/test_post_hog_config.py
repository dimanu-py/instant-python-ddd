import pytest
from expects import be_false, be_true, equal, expect

from instant_python.metrics.infra.post_hog_config import PostHogConfig


@pytest.mark.unit
class TestPostHogConfig:
    def test_should_have_metrics_enabled_by_default(self) -> None:
        config = PostHogConfig()

        expect(config.is_metrics_disabled()).to(be_false)

    def test_should_disable_metrics_when_env_var_is_false(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("IPY_METRICS_ENABLE", "false")
        config = PostHogConfig()

        expect(config.is_metrics_disabled()).to(be_true)

    def test_should_disable_metrics_when_env_var_is_0(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("IPY_METRICS_ENABLE", "0")
        config = PostHogConfig()

        expect(config.is_metrics_disabled()).to(be_true)

    def test_should_enable_metrics_when_env_var_is_true(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("IPY_METRICS_ENABLE", "true")
        config = PostHogConfig()

        expect(config.is_metrics_disabled()).to(be_false)

    def test_should_enable_metrics_when_env_var_is_1(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("IPY_METRICS_ENABLE", "1")
        config = PostHogConfig()

        expect(config.is_metrics_disabled()).to(be_false)

    def test_should_read_post_hog_api_key_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("POST_HOG_API_KEY", "test_api_key")
        config = PostHogConfig()

        expect(config.api_key).to(equal("test_api_key"))

    def test_should_read_post_hog_host_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("POST_HOG_HOST", "https://example.com")
        config = PostHogConfig()

        expect(config.host).to(equal("https://example.com"))
