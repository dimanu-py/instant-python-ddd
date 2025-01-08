invalid_negative_value_error_template = """
class InvalidNegativeValueError(Exception):
    def __init__(self, value: int) -> None:
        message = f"Invalid negative value: {value}"
        super().__init__(message)
""".strip()