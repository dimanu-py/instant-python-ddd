from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostHogConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_prefix="POST_HOG_")
    api_key: str = Field(default="phc_mcDDYHvnYAon8FJ3sl33Jy22j1k3Ul5jTv8wgeG5TzP")
    host: str = Field(default="https://eu.i.posthog.com")
    metrics_enabled: bool = Field(
        default=True,
        alias="IPY_METRICS_ENABLE",
    )

    def is_metrics_disabled(self) -> bool:
        return not self.metrics_enabled
