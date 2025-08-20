import dataclasses
import typing

@dataclasses.dataclass
class GetBrowseNodesResource:
    BROWSENODES_ANCESTOR = "BrowseNodes.Ancestor"
    BROWSENODES_CHILDREN = "BrowseNodes.Children"