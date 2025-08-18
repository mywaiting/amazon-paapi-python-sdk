import dataclasses
import typing

from .single_string_valued_attribute import SingleStringValuedAttribute

@dataclasses.dataclass
class Classifications:
    binding: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Binding'})
    product_group: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'ProductGroup'})