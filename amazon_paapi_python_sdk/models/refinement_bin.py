import dataclasses
import typing

@dataclasses.dataclass
class RefinementBin:
    display_name: typing.Optional[str] = dataclasses.field(metadata={'key': 'DisplayName'})
    id: typing.Optional[str] = dataclasses.field(metadata={'key': 'Id'})