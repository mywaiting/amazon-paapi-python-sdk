import dataclasses
import typing

from .image_size import ImageSize

@dataclasses.dataclass
class ImageType:
    small: typing.Optional[ImageSize] = dataclasses.field(metadata={'key': 'Small'})
    medium: typing.Optional[ImageSize] = dataclasses.field(metadata={'key': 'Medium'})
    large: typing.Optional[ImageSize] = dataclasses.field(metadata={'key': 'Large'})