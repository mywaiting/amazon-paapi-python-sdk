import dataclasses
import typing

from .refinement import Refinement

@dataclasses.dataclass
class SearchRefinements:
    browse_node: typing.Optional[Refinement] = dataclasses.field(metadata={'key': 'BrowseNode'})
    other_refinements: typing.Optional[list[Refinement]] = dataclasses.field(metadata={'key': 'OtherRefinements'})
    search_index: typing.Optional[Refinement] = dataclasses.field(metadata={'key': 'SearchIndex'})