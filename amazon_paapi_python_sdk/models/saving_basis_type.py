import dataclasses
import typing

@dataclasses.dataclass
class SavingBasisType:
    LIST_PRICE = "LIST_PRICE"
    LOWEST_PRICE = "LOWEST_PRICE"
    LOWEST_PRICE_STRIKETHROUGH = "LOWEST_PRICE_STRIKETHROUGH"
    WAS_PRICE = "WAS_PRICE"