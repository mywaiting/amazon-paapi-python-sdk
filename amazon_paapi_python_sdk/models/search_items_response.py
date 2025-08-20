import dataclasses
import typing

from .search_result import SearchResult
from .error_data import ErrorData

@dataclasses.dataclass
class SearchItemsResponse:
    search_result: typing.Optional[SearchResult] = dataclasses.field(metadata={'key': 'SearchResult'})
    errors: typing.Optional[list[ErrorData]] = dataclasses.field(metadata={'key': 'Errors'})