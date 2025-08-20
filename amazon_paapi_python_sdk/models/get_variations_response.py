import dataclasses
import typing

from .error_data import ErrorData
from .variations_result import VariationsResult

@dataclasses.dataclass
class GetVariationsResponse:
    errors: typing.Optional[list[ErrorData]] = dataclasses.field(metadata={'key': 'Errors'})
    variations_result: typing.Optional[VariationsResult] = dataclasses.field(metadata={'key': 'VariationsResult'})