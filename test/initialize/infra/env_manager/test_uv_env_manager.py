from typing import ClassVar

import pytest
from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, raise_error

from instant_python.initialize.infra.env_manager.system_console import CommandExecutionError, SystemConsole
from instant_python.initialize.infra.env_manager.uv_env_manager import UvEnvManager
from test.initialize.infra.env_manager.mother.command_execution_result_mother import CommandExecutionResultMother
from test.shared.domain.mothers.dependency_config_mother import DependencyConfigMother


@pytest.mark.unit
class TestUvEnvManager:
    _UV_EXECUTABLE = "~/.local/bin/uv"
    _SUCCESSFUL_COMMAND_RESULT = CommandExecutionResultMother.success()
    _FAILED_COMMAND_RESULT = CommandExecutionResultMother.failure()
    _A_PYTHON_VERSION = "3.12"
    _A_DEPENDENCY = DependencyConfigMother.with_parameter(name="requests", version="latest")
    _NO_DEPENDENCIES: ClassVar[list] = []

    def setup_method(self) -> None:
        self._console = Mimic(Mock, SystemConsole)
        self._uv_env_manager = UvEnvManager(console=self._console)

    def test_should_setup_environment_without_installing_uv_when_is_already_installed(self) -> None:
        self._should_check_that_uv_is_installed()
        self._should_install_python_version()
        self._should_create_virtual_environment()

        self._uv_env_manager.setup(python_version=self._A_PYTHON_VERSION, dependencies=self._NO_DEPENDENCIES)

        expect(self._console).to(have_been_satisfied)

    def test_should_setup_environment_installing_uv_when_is_not_installed(self) -> None:
        self._should_check_that_uv_is_not_installed()
        self._should_install_uv()
        self._should_install_python_version()
        self._should_create_virtual_environment()

        self._uv_env_manager.setup(python_version=self._A_PYTHON_VERSION, dependencies=self._NO_DEPENDENCIES)

        expect(self._console).to(have_been_satisfied)

    def test_should_setup_environment_installing_specified_dependencies(self) -> None:
        self._should_check_that_uv_is_installed()
        self._should_install_python_version()
        self._should_create_virtual_environment()
        self._should_install_dependencies()

        self._uv_env_manager.setup(python_version=self._A_PYTHON_VERSION, dependencies=[self._A_DEPENDENCY])

        expect(self._console).to(have_been_satisfied)

    def test_should_raise_error_when_a_command_execution_fails(self) -> None:
        self._should_check_that_uv_is_installed()
        self._should_fail_installing_python()

        expect(lambda: self._uv_env_manager.setup(python_version=self._A_PYTHON_VERSION, dependencies=[])).to(
            raise_error(CommandExecutionError)
        )

    def _should_check_that_uv_is_installed(self) -> None:
        expect_call(self._console).execute(f"{self._UV_EXECUTABLE} --version").returns(self._SUCCESSFUL_COMMAND_RESULT)

    def _should_check_that_uv_is_not_installed(self) -> None:
        expect_call(self._console).execute(f"{self._UV_EXECUTABLE} --version").returns(self._FAILED_COMMAND_RESULT)

    def _should_install_python_version(self) -> None:
        expect_call(self._console).execute_or_raise(
            f"{self._UV_EXECUTABLE} python install {self._A_PYTHON_VERSION}"
        ).returns(self._SUCCESSFUL_COMMAND_RESULT)

    def _should_create_virtual_environment(self) -> None:
        expect_call(self._console).execute_or_raise(f"{self._UV_EXECUTABLE} sync --all-groups").returns(
            self._SUCCESSFUL_COMMAND_RESULT
        )

    def _should_install_uv(self) -> None:
        expect_call(self._console).execute_or_raise("curl -LsSf https://astral.sh/uv/install.sh | sh").returns(
            self._SUCCESSFUL_COMMAND_RESULT
        )

    def _should_install_dependencies(self) -> None:
        expect_call(self._console).execute_or_raise(f"{self._UV_EXECUTABLE} add requests").returns(
            self._SUCCESSFUL_COMMAND_RESULT
        )

    def _should_fail_installing_python(self) -> None:
        expect_call(self._console).execute_or_raise(
            f"{self._UV_EXECUTABLE} python install {self._A_PYTHON_VERSION}"
        ).raises(
            CommandExecutionError(
                exit_code=self._FAILED_COMMAND_RESULT.exit_code, stderr_output=self._FAILED_COMMAND_RESULT.stderr
            )
        )
