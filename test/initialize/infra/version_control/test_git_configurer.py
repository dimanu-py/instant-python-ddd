import pytest
from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, raise_error

from instant_python.initialize.infra.env_manager.system_console import CommandExecutionError, SystemConsole
from instant_python.initialize.infra.version_control.git_configurer import GitConfigurer
from test.initialize.infra.env_manager.mother.command_execution_result_mother import CommandExecutionResultMother
from test.shared.domain.mothers.git_config_mother import GitConfigMother


@pytest.mark.unit
class TestGitConfigurer:
    _SUCCESSFUL_COMMAND_RESULT = CommandExecutionResultMother.success()
    _FAILED_COMMAND_RESULT = CommandExecutionResultMother.failure()
    _A_USERNAME = "test_user"
    _A_EMAIL = "test_user@gmail.com"

    def setup_method(self) -> None:
        self._console = Mimic(Mock, SystemConsole)
        self._git_configurer = GitConfigurer(console=self._console)

    def test_should_configure_git_repository_successfully(self) -> None:
        self._should_create_repository()
        self._should_set_user_information()
        self._should_make_first_commit()

        self._git_configurer.setup(
            GitConfigMother.with_parameters(
                username=self._A_USERNAME,
                email=self._A_EMAIL,
            )
        )

        expect(self._console).to(have_been_satisfied)

    def test_should_raise_error_when_repository_initialization_fails(self) -> None:
        self._should_fail_to_create_repository()

        expect(lambda: self._git_configurer.setup(GitConfigMother.initialize())).to(raise_error(CommandExecutionError))

    def _should_create_repository(self) -> None:
        expect_call(self._console).execute_or_raise("git init").returns(self._SUCCESSFUL_COMMAND_RESULT)

    def _should_set_user_information(self) -> None:
        expect_call(self._console).execute(f"git config user.name {self._A_USERNAME}").returns(
            self._SUCCESSFUL_COMMAND_RESULT
        )
        expect_call(self._console).execute(f"git config user.email {self._A_EMAIL}").returns(
            self._SUCCESSFUL_COMMAND_RESULT
        )

    def _should_make_first_commit(self) -> None:
        expect_call(self._console).execute("git add .").returns(self._SUCCESSFUL_COMMAND_RESULT)
        expect_call(self._console).execute('git commit -m "🎉 chore: initial commit"').returns(
            self._SUCCESSFUL_COMMAND_RESULT
        )

    def _should_fail_to_create_repository(self) -> None:
        expect_call(self._console).execute_or_raise("git init").raises(
            CommandExecutionError(
                exit_code=self._FAILED_COMMAND_RESULT.exit_code,
                stderr_output=self._FAILED_COMMAND_RESULT.stderr,
            )
        )
