import dataclasses
import typing

from .browse_nodes_result import BrowseNodesResult
from .error_data import ErrorData

@dataclasses.dataclass
class GetBrowseNodesResponse:
    browse_nodes_result: typing.Optional[BrowseNodesResult] = dataclasses.field(metadata={'key': 'BrowseNodesResult'})
    errors: typing.Optional[list[ErrorData]] = dataclasses.field(metadata={'key': 'Errors'})