import dataclasses
import typing

@dataclasses.dataclass
class Contributor:
    locale: typing.Optional[str] = dataclasses.field(metadata={'key': 'Locale'})
    name: typing.Optional[str] = dataclasses.field(metadata={'key': 'Name'})
    role: typing.Optional[str] = dataclasses.field(metadata={'key': 'Role'})
    role_type: typing.Optional[str] = dataclasses.field(metadata={'key': 'RoleType'})