import dataclasses
import typing

@dataclasses.dataclass
class DeliveryFlag:
    AMAZONGLOBAL = "AmazonGlobal"
    FREESHIPPING = "FreeShipping"
    FULFILLEDBYAMAZON = "FulfilledByAmazon"
    PRIME = "Prime"