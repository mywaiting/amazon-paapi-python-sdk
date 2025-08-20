import dataclasses
import typing

from .price import Price
from .variation_dimension import VariationDimension

@dataclasses.dataclass
class VariationSummary:
    page_count: typing.Optional[int] = dataclasses.field(metadata={'key': 'PageCount'})
    price: typing.Optional[Price] = dataclasses.field(metadata={'key': 'Price'})
    variation_count: typing.Optional[int] = dataclasses.field(metadata={'key': 'VariationCount'})
    variation_dimensions: typing.Optional[list[VariationDimension]] = dataclasses.field(metadata={'key': 'VariationDimensions'})