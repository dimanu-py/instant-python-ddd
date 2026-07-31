import questionary


class Questionary:
    def boolean_question(self, message: str, default: bool = False) -> bool:
        return questionary.confirm(message, default=default).ask()

    def free_text_question(self, message: str, default: str | None = None) -> str:
        return questionary.text(message, default=default if default else "").ask()

    def single_choice_question(self, message: str, options: list[str], default: str | None = None) -> str:
        return questionary.select(message, choices=options, default=default).ask()

    def multiselect_question(self, message: str, options: list[str]) -> list[str]:
        return questionary.checkbox(message, choices=options).ask()
