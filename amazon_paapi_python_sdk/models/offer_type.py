import dataclasses
import typing

@dataclasses.dataclass
class OfferType:
    SUBSCRIBE_AND_SAVE = "SUBSCRIBE_AND_SAVE"
    LIGHTNING_DEAL = "LIGHTNING_DEAL"