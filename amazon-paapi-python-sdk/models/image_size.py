import dataclasses
import typing

@dataclasses.dataclass
class ImageSize:
    url: typing.Optional[str] = dataclasses.field(metadata={'key': 'URL'})
    height: typing.Optional[int] = dataclasses.field(metadata={'key': 'Heighet'})
    width: typing.Optional[int] = dataclasses.field(metadata={'key': 'Width'})