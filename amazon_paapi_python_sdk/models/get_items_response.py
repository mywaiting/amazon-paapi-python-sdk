import dataclasses
import typing

from .error_data import ErrorData
from .items_result import ItemsResult

@dataclasses.dataclass
class GetItemsResponse:
    errors: typing.Optional[list[ErrorData]] = dataclasses.field(metadata={'key': 'Errors'})
    items_result: typing.Optional[ItemsResult] = dataclasses.field(metadata={'key': 'ItemsResult'})