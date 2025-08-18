import dataclasses
import typing


@dataclasses.dataclass
class Targets:
    GETBROWSENODES = "com.amazon.paapi5.v1.ProductAdvertisingAPIv1.GetBrowseNodes"
    GETITEMS = "com.amazon.paapi5.v1.ProductAdvertisingAPIv1.GetItems"
    GETVARIATIONS = "com.amazon.paapi5.v1.ProductAdvertisingAPIv1.GetVariations"
    SEARCHITEMS = "com.amazon.paapi5.v1.ProductAdvertisingAPIv1.SearchItems"