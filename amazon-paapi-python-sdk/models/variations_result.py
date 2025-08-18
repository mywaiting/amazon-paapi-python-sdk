import dataclasses
import typing

from .item import Item
from .variation_summary import VariationSummary

@dataclasses.dataclass
class VariationsResult:
    items: typing.Optional[list[Item]] = dataclasses.field(metadata={'key': 'Items'})
    variation_summary: typing.Optional[VariationSummary] = dataclasses.field(metadata={'key': 'VariationSummary'})