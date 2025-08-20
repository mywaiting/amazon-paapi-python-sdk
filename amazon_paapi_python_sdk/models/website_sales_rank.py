import dataclasses
import typing

@dataclasses.dataclass
class WebsiteSalesRank:
    context_free_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'ContextFreeName'})
    display_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayName'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})
    sales_rank: typing.Optional[int] = dataclasses.field(metadata={'key': 'SalesRank'})