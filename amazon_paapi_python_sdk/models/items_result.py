import dataclasses
import typing

from .item import Item

@dataclasses.dataclass
class ItemsResult:
    items: typing.Optional[list[Item]] = dataclasses.field(metadata={'key': 'Items'})