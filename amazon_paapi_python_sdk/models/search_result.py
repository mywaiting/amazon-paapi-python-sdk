import dataclasses
import typing

from .item import Item
from .search_refinements import SearchRefinements

@dataclasses.dataclass
class SearchResult:
    total_result_count: typing.Optional[int] = dataclasses.field(metadata={'key': 'TotalResultCount'})
    search_url: typing.Optional[str] = dataclasses.field(metadata={'key': 'SearchURL'})
    items: typing.Optional[list[Item]] = dataclasses.field(metadata={'key': 'Items'})
    search_refinements: typing.Optional[SearchRefinements] = dataclasses.field(metadata={'key': 'SearchRefinements'})