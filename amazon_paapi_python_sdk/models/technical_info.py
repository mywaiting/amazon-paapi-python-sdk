import dataclasses
import typing

from .single_string_valued_attribute import SingleStringValuedAttribute
from .multi_valued_attribute import MultiValuedAttribute

@dataclasses.dataclass
class TechnicalInfo:
    energy_efficiency_class: typing.Optional[SingleStringValuedAttribute] = dataclasses.field(metadata={'key': 'EnergyEfficiencyClass'})
    formats: typing.Optional[MultiValuedAttribute] = dataclasses.field(metadata={'key': 'Formats'})