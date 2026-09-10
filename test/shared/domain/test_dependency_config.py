import pytest
from expects import be, be_false, be_none, be_true, expect, raise_error

from instant_python.shared.domain.dependency_config import NotDevDependencyIncludedInGroup
from test.shared.domain.mothers.dependency_config_mother import (
    DependencyConfigMother,
)


@pytest.mark.unit
class TestDependencyConfig:
    def test_should_allow_to_create_dev_dependency_config(self) -> None:
        dependency_config = DependencyConfigMother.with_parameter(is_dev=True)

        expect(dependency_config.is_dev).to(be_true)

    def test_should_allow_to_create_non_dev_dependency_config(self) -> None:
        dependency_config = DependencyConfigMother.any()

        expect(dependency_config.is_dev).to(be_false)

    def test_should_allow_to_create_dependency_config_with_group(self) -> None:
        dependency_config = DependencyConfigMother.with_parameter(is_dev=True, group="test")

        expect(dependency_config.group).to_not(be_none)

    def test_should_allow_to_create_dependency_config_without_group(
        self,
    ) -> None:
        dependency_config = DependencyConfigMother.any()

        expect(dependency_config.group).to(be(""))

    def test_should_not_allow_to_create_not_dev_dependency_inside_group(self) -> None:
        expect(lambda: DependencyConfigMother.with_parameter(group="test")).to(
            raise_error(NotDevDependencyIncludedInGroup)
        )
