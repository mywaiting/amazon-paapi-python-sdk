import dataclasses
import typing

@dataclasses.dataclass
class OfferLoyaltyPoints:
    points: typing.Optional[int] = dataclasses.field(metadata={'key': 'Points'})