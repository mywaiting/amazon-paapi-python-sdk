import dataclasses
import typing

from .rating import Rating

@dataclasses.dataclass
class CustomerReviews:
    count: typing.Optional[int] = dataclasses.field(metadata={'key': 'Count'})
    star_rating: typing.Optional[Rating] = dataclasses.field(metadata={'key': 'StarRating'})