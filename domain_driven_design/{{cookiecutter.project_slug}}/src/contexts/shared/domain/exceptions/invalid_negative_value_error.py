class InvalidNegativeValueError(Exception):
	def __init__(self, value: int) -> None:
		message = f"Invalid negative value: {value}"
		super().__init__(message)
