import dataclasses
import typing

from .single_string_valued_attribute import SingleStringValuedAttribute

@dataclasses.dataclass
class ManufactureInfo:
    item_part_number: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'ItemPartNumber'})
    model: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Model'})
    warranty: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Warranty'})