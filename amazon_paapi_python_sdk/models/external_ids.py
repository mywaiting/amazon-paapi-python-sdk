import dataclasses
import typing

from .multi_valued_attribute import MultiValuedAttribute

@dataclasses.dataclass
class ExternalIds:
    ea_ns: typing.Optional[MultiValuedAttribute] = dataclasses.field(metadata={'key': 'EANs'})
    isb_ns: typing.Optional[MultiValuedAttribute] = dataclasses.field(metadata={'key': 'ISBNs'})
    up_cs: typing.Optional[MultiValuedAttribute] = dataclasses.field(metadata={'key': 'UPCs'})