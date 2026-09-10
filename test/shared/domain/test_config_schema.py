import pytest
from expects import be_none, expect, raise_error

from instant_python.shared.domain.config_schema import ConfigKeyNotPresent, ConfigSchema, EmptyConfigurationNotAllowed


@pytest.mark.unit
class TestConfigSchema:
    def test_should_raise_error_if_raw_config_is_empty(self) -> None:
        empty_raw_config = {}

        expect(lambda: ConfigSchema.from_primitives(empty_raw_config)).to(raise_error(EmptyConfigurationNotAllowed))

    def test_should_raise_error_if_some_section_is_missing(self) -> None:
        raw_config = {
            "general": {
                "slug": "python-project",
                "source_name": "src",
                "description": "Python Project Description",
                "version": "0.1.0",
                "author": "Diego Martinez",
                "license": "MIT",
                "python_version": "3.13",
                "dependency_manager": "uv",
            },
            "git": {"initialize": True, "username": "dimanu-py", "email": "dimanu.py@gmail.com"},
        }

        expect(lambda: ConfigSchema.from_primitives(raw_config)).to(raise_error(ConfigKeyNotPresent))

    def test_should_parse_valid_raw_config(self) -> None:
        raw_config = {
            "general": {
                "slug": "python-project",
                "source_name": "src",
                "description": "Python Project Description",
                "version": "0.1.0",
                "author": "Diego Martinez",
                "license": "MIT",
                "python_version": "3.13",
                "dependency_manager": "uv",
            },
            "dependencies": [
                {"name": "pytest", "version": "latest", "is_dev": True, "group": "test"},
                {"name": "fastapi", "version": "latest", "is_dev": False},
            ],
            "git": {"initialize": True, "username": "dimanu-py", "email": "dimanu.py@gmail.com"},
            "template": {"name": "domain_driven_design"},
        }

        config = ConfigSchema.from_primitives(raw_config)

        expect(config).to_not(be_none)

    def test_should_ignore_legacy_year_field_in_general_section(self) -> None:
        raw_config = {
            "general": {
                "slug": "python-project",
                "source_name": "src",
                "description": "Python Project Description",
                "version": "0.1.0",
                "author": "Diego Martinez",
                "license": "MIT",
                "python_version": "3.13",
                "dependency_manager": "uv",
                "year": 2025,
            },
            "dependencies": [],
            "git": {"initialize": False},
            "template": {"name": "domain_driven_design"},
        }

        config = ConfigSchema.from_primitives(raw_config)

        expect(config).to_not(be_none)
