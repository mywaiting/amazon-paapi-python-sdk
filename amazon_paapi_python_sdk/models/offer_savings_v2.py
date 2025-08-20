import dataclasses
import typing

from .money import Money

@dataclasses.dataclass
class OfferSavingsV2:
    money: typing.Optional[Money] = dataclasses.field(metadata={'key': 'Money'})
    percentage: typing.Optional[int] = dataclasses.field(metadata={'key': 'Percentage'})