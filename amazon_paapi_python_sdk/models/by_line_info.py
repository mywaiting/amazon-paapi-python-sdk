import dataclasses
import typing

from .single_string_valued_attribute import SingleStringValuedAttribute
from .contributor import Contributor

@dataclasses.dataclass
class ByLineInfo:
    brand: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Brand'})
    contributors: typing.Optional[list[Contributor]] = dataclasses.field(metadata={'key': 'Contributors'})
    manufacturer: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'Manufacturer'})