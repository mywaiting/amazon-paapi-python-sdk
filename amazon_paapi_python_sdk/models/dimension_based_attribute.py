import dataclasses
import typing

from .unit_based_attribute import UnitBasedAttribute

@dataclasses.dataclass
class DimensionBasedAttribute:
    height: typing.Optional[UnitBasedAttribute] = dataclasses.field(metadata={'key': 'Height'})
    length: typing.Optional[UnitBasedAttribute] = dataclasses.field(metadata={'key': 'Length'})
    weight: typing.Optional[UnitBasedAttribute] = dataclasses.field(metadata={'key': 'Weight'})
    width: typing.Optional[UnitBasedAttribute] = dataclasses.field(metadata={'key': 'Width'})