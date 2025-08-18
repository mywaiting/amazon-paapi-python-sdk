import dataclasses
import typing

@dataclasses.dataclass
class Condition:
    ANY = "Any"
    COLLECTIBLE = "Collectible"
    NEW = "New"
    REFURBISHED = "Refurbished"
    USED = "Used"