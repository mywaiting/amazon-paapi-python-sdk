import dataclasses
import typing

from .browse_node_ancestor import BrowseNodeAncestor
from .browse_node_child import BrowseNodeChild

@dataclasses.dataclass
class BrowseNode:
    ancestor: typing.Optional[BrowseNodeAncestor] = dataclasses.field(metadata={'key': 'Ancestor'})
    children: typing.Optional[list[BrowseNodeChild]] = dataclasses.field(metadata={'key': 'Children'})
    context_free_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'ContextFreeName'})
    display_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayName'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})
    is_root: typing.Optional[bool] = dataclasses.field(metadata={'key': 'IsRoot'})
    sales_rank: typing.Optional[int] = dataclasses.field(metadata={'key': 'SalesRank'})