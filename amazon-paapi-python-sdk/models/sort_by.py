import dataclasses
import typing

@dataclasses.dataclass
class SortBy:
    AVGCUSTOMERREVIEWS = "AvgCustomerReviews"
    FEATURED = "Featured"
    NEWESTARRIVALS = "NewestArrivals"
    PRICE_HIGHTOLOW = "Price:HighToLow"
    PRICE_LOWTOHIGH = "Price:LowToHigh"
    RELEVANCE = "Relevance"