import dataclasses
import typing

@dataclasses.dataclass
class BrowseNodeAncestor:
    ancestor: typing.Optional['BrowseNodeAncestor'] = dataclasses.field(metadata={'key': 'Ancestor'})
    context_free_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'ContextFreeName'})
    display_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayName'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})