import dataclasses
import typing

from .single_string_valued_attribute import SingleStringValuedAttribute
from .single_boolean_valued_attribute import SingleBooleanValuedAttribute
from .single_integer_valued_attribute import SingleIntegerValuedAttribute
from .dimension_based_attribute import DimensionBasedAttribute

@dataclasses.dataclass
class ProductInfo:
    color: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Color'})
    is_adult_product: typing.Optional[SingleBooleanValuedAttribute] = dataclasses.field(metadata={'key': 'IsAdultProduct'})
    item_dimensions: typing.Optional[DimensionBasedAttribute] = dataclasses.field(metadata={'key': 'ItemDimensions'})
    release_date: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'ReleaseDate'})
    size: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Size'})
    unit_count: typing.Optional[SingleIntegerValuedAttribute] = dataclasses.field(metadata={'key': 'UnitCount'})