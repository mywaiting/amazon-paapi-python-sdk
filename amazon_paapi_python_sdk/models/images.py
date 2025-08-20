import dataclasses
import typing

from .image_type import ImageType

@dataclasses.dataclass
class Images:
    primary: typing.Optional[ImageType] = dataclasses.field(metadata={'key': 'Primary'})
    variants: typing.Optional[list[ImageType]] = dataclasses.field(metadata={'key': 'Variants'})