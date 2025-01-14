from src.contexts.platform.shared.domain.exceptions.invalid_negative_value_error import (
	InvalidNegativeValueError,
)
from src.contexts.platform.shared.domain.value_objects.value_object import ValueObject


class IntValueObject(ValueObject[int]):
	def _validate(self, value: int) -> None:
		if value < 0:
			raise InvalidNegativeValueError(value)
