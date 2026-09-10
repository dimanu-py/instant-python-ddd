import pytest
from expects import equal, expect, raise_error

from instant_python.shared.domain.general_config import (
    InvalidDependencyManagerValue,
    InvalidLicenseValue,
    InvalidPythonVersionValue,
    InvalidSlugValue,
)
from test.shared.domain.mothers.general_config_mother import (
    GeneralConfigMother,
)


@pytest.mark.unit
class TestGeneralConfig:
    def test_should_allow_to_create_general_config_with_valid_parameters(
        self,
    ) -> None:
        GeneralConfigMother.any()

    @pytest.mark.parametrize(
        "field, value, expected_error",
        [
            pytest.param("license", "BSD", InvalidLicenseValue, id="invalid_license"),
            pytest.param(
                "python_version",
                "3.9",
                InvalidPythonVersionValue,
                id="invalid_python_version",
            ),
            pytest.param(
                "dependency_manager",
                "pip",
                InvalidDependencyManagerValue,
                id="invalid_dependency_manager",
            ),
        ],
    )
    def test_should_raise_error_for_unsupported_config_parameters(self, field, value, expected_error) -> None:
        expect(lambda: GeneralConfigMother.with_parameter(**{field: value})).to(raise_error(expected_error))

    @pytest.mark.parametrize(
        "raw_slug, expected_slug",
        [
            pytest.param("My Cool Project", "my-cool-project", id="spaces_and_uppercase"),
            pytest.param("my_project", "my-project", id="underscores"),
            pytest.param("my.project", "my-project", id="dots"),
            pytest.param("My@Project#1", "my-project-1", id="invalid_characters"),
            pytest.param("--my-project--", "my-project", id="surrounding_invalid_characters"),
        ],
    )
    def test_should_normalize_slug_into_valid_distribution_name(self, raw_slug, expected_slug) -> None:
        config = GeneralConfigMother.with_parameter(slug=raw_slug)

        expect(config.slug).to(equal(expected_slug))

    def test_should_raise_error_when_slug_has_no_valid_characters(self) -> None:
        expect(lambda: GeneralConfigMother.with_parameter(slug="!!!")).to(raise_error(InvalidSlugValue))

    def test_should_set_uv_as_default_dependency_manager_when_not_provided(self) -> None:
        config = GeneralConfigMother.default_dependency_manager()

        expect(config.dependency_manager).to(equal("uv"))

    def test_should_set_uv_as_dependency_manager_when_pdm_is_provided(self) -> None:
        config = GeneralConfigMother.with_parameter(dependency_manager="pdm")

        expect(config.dependency_manager).to(equal("uv"))
