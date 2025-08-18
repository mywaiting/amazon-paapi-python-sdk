import dataclasses
import typing

@dataclasses.dataclass
class OfferLoyaltyPointsV2:
    points: typing.Optional[int] = dataclasses.field(metadata={'key': 'Points'})