import dataclasses
import typing

from .browse_node import BrowseNode

@dataclasses.dataclass
class BrowseNodesResult:
    browse_nodes: typing.Optional[list[BrowseNode]] = dataclasses.field(metadata={'key': 'BrowseNodes'})