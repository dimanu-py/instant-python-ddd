from typing import ClassVar

import pytest
from expects import equal, expect

from instant_python.config.infra.question_wizard.console_answers_review_formatter import ConsoleAnswersReviewFormatter


@pytest.mark.integration
class TestConsoleAnswerReviewFormatter:
    _GENERAL_ANSWERS: ClassVar[dict[str, str]] = {
        "slug": "example-project",
        "source_name": "src",
        "description": "Example project description",
        "version": "0.1.0",
        "author": "Jane Doe",
        "license": "MIT",
        "python_version": "3.13",
        "dependency_manager": "uv",
    }
    _TEMPLATE_WITHOUT_BUILT_IN_FEATURES: ClassVar[dict[str, str | list]] = {
        "name": "standard_project",
        "built_in_features": [],
    }
    _TEMPLATE_WITH_BUILT_IN_FEATURES: ClassVar[dict[str, str | list]] = {
        "name": "standard_project",
        "built_in_features": ["value_objects", "github_actions"],
    }
    _TEMPLATE_WITH_BOUNDED_CONTEXT: ClassVar[dict[str, str | bool | list]] = {
        "name": "domain_driven_design",
        "specify_bounded_context": True,
        "bounded_context": "backoffice",
        "aggregate_name": "user",
        "built_in_features": [],
    }
    _GIT_NOT_INITIALIZED: ClassVar[dict[str, bool]] = {
        "initialize": False,
    }
    _GIT_INITIALIZED: ClassVar[dict[str, bool | str]] = {
        "initialize": True,
        "username": "johndoe",
        "email": "johndoe@gmail.com",
    }
    _A_PRODUCTION_DEPENDENCY: ClassVar[dict[str, str | bool]] = {
        "name": "sindripy",
        "version": "latest",
        "is_dev": False,
        "group": "",
    }
    _A_DEV_DEPENDENCY_WITHOUT_GROUP: ClassVar[dict[str, str | bool]] = {
        "name": "sindripy",
        "version": "latest",
        "is_dev": True,
        "group": "",
    }
    _A_DEV_DEPENDENCY_WITH_GROUP: ClassVar[dict[str, str | bool]] = {
        "name": "sindripy",
        "version": "latest",
        "is_dev": True,
        "group": "test",
    }

    def setup_method(self) -> None:
        self._formatter = ConsoleAnswersReviewFormatter()

    def test_should_show_review_header(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._formatter.print_answers({})

        printed_summary = capsys.readouterr().out
        expect(printed_summary).to(equal("Review Configuration\n"))

    def test_should_show_general_summary(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._formatter.print_answers({"general": self._GENERAL_ANSWERS})

        printed_summary = capsys.readouterr().out
        expected_summary = (
            "Review Configuration\n"
            "General\n"
            "  Slug: example-project\n"
            "  Source Name: src\n"
            "  Description: Example project description\n"
            "  Version: 0.1.0\n"
            "  Author: Jane Doe\n"
            "  License: MIT\n"
            "  Python Version: 3.13\n"
            "  Dependency Manager: uv\n"
        )
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_template_summary_without_built_in_features(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._formatter.print_answers({"template": self._TEMPLATE_WITHOUT_BUILT_IN_FEATURES})

        printed_summary = capsys.readouterr().out
        expected_summary = "Review Configuration\nTemplate\n  Name: standard_project\n  Built In Features: None\n"
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_template_summary_with_built_in_features(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._formatter.print_answers({"template": self._TEMPLATE_WITH_BUILT_IN_FEATURES})

        printed_summary = capsys.readouterr().out
        expected_summary = (
            "Review Configuration\n"
            "Template\n"
            "  Name: standard_project\n"
            "  Built In Features: value_objects, github_actions\n"
        )
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_template_summary_with_bounded_context(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._formatter.print_answers({"template": self._TEMPLATE_WITH_BOUNDED_CONTEXT})

        printed_summary = capsys.readouterr().out
        expected_summary = (
            "Review Configuration\n"
            "Template\n"
            "  Name: domain_driven_design\n"
            "  Specify Bounded Context: True\n"
            "  Bounded Context: backoffice\n"
            "  Aggregate Name: user\n"
            "  Built In Features: None\n"
        )
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_git_summary_not_initialized(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._formatter.print_answers({"git": self._GIT_NOT_INITIALIZED})

        printed_summary = capsys.readouterr().out
        expected_summary = "Review Configuration\nGit\n  Initialize: False\n"
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_git_summary_initialized_with_username_and_email(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        self._formatter.print_answers({"git": self._GIT_INITIALIZED})

        printed_summary = capsys.readouterr().out
        expected_summary = (
            "Review Configuration\nGit\n  Initialize: True\n  Username: johndoe\n  Email: johndoe@gmail.com\n"
        )
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_empty_dependencies_summary(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._formatter.print_answers({"dependencies": []})

        printed_summary = capsys.readouterr().out
        expected_summary = "Review Configuration\nDependencies\n  None\n"
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_dependencies_summary_with_one_production_dependency(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        self._formatter.print_answers({"dependencies": [self._A_PRODUCTION_DEPENDENCY]})

        printed_summary = capsys.readouterr().out
        expected_summary = "Review Configuration\nDependencies\n  sindripy==latest (prod)\n"
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_dependencies_summary_with_several_production_dependencies(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        self._formatter.print_answers({"dependencies": [self._A_PRODUCTION_DEPENDENCY, self._A_PRODUCTION_DEPENDENCY]})

        printed_summary = capsys.readouterr().out
        expected_summary = "Review Configuration\nDependencies\n  sindripy==latest (prod)\n  sindripy==latest (prod)\n"
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_dependencies_summary_with_development_dependency_without_group(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        self._formatter.print_answers({"dependencies": [self._A_DEV_DEPENDENCY_WITHOUT_GROUP]})

        printed_summary = capsys.readouterr().out
        expected_summary = "Review Configuration\nDependencies\n  sindripy==latest (dev)\n"
        expect(printed_summary).to(equal(expected_summary))

    def test_should_show_dependencies_summary_with_development_dependency_with_group(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        self._formatter.print_answers({"dependencies": [self._A_DEV_DEPENDENCY_WITH_GROUP]})

        printed_summary = capsys.readouterr().out
        expected_summary = "Review Configuration\nDependencies\n  sindripy==latest (dev, group: test)\n"
        expect(printed_summary).to(equal(expected_summary))
