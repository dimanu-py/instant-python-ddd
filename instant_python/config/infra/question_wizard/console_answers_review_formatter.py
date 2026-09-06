from typing import ClassVar

from instant_python.config.domain.answers_review_formatter import AnswersReviewFormatter


class ConsoleAnswersReviewFormatter(AnswersReviewFormatter):
    _TITLE = "Review Configuration"
    _SECTION_TITLES: ClassVar[dict[str, str]] = {
        "general": "General",
        "template": "Template",
        "git": "Git",
        "dependencies": "Dependencies",
    }

    def print_answers(self, answers: dict) -> None:
        summary = [self._TITLE]
        for section_key, section_content in answers.items():
            section_title = self._SECTION_TITLES[section_key]
            summary.append(section_title)
            if not section_content:
                summary.append("  None")
                continue
            if isinstance(section_content, list):
                for dependency in section_content:
                    env_content = "(prod)"
                    if dependency["is_dev"] is True:
                        env_content = f"(dev, group: {dependency['group']})" if dependency["group"] != "" else "(dev)"
                    summary.append(f"  {dependency['name']}=={dependency['version']} {env_content}")
                continue
            for field_title, field_content in section_content.items():
                if isinstance(field_content, list):
                    field_content = "None" if not field_content else ", ".join(field_content)
                summary.append(f"  {field_title.title().replace('_', ' ')}: {field_content}")
        print("\n".join(summary))
