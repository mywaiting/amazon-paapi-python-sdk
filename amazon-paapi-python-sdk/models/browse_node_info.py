import dataclasses
import typing

from .browse_node import BrowseNode
from .website_sales_rank import WebsiteSalesRank

@dataclasses.dataclass
class BrowseNodeInfo:
    browse_nodes: typing.Optional[list[BrowseNode]] = dataclasses.field(metadata={'key': 'BrowseNodes'})
    website_sales_rank: typing.Optional[WebsiteSalesRank] = dataclasses.field(metadata={'key': 'WebsiteSalesRank'})