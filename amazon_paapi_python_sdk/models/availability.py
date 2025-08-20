import dataclasses
import typing

@dataclasses.dataclass
class Availability:
    AVAILABLE = "Available"
    INCLUDEOUTOFSTOCK = "IncludeOutOfStock"