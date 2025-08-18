import dataclasses
import typing

from .refinement_bin import RefinementBin

@dataclasses.dataclass
class Refinement:
    bins: typing.Optional[list[RefinementBin]] = dataclasses.field(metadata={'key': 'Bins'})
    display_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayName'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})