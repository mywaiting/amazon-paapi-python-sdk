import dataclasses
import typing


@dataclasses.dataclass
class CountryCodes:
    """ISO 3166 country codes, Alpha-2 codes
    """
    AUSTRALIA = "AU"
    BELGIUM = "BE"
    BRAZIL = "BR"
    CANADA = "CA"
    EGYPT = "EG"
    FRANCE = "FR"
    GERMANY = "DE"
    INDIA = "IN"
    IRELAND = "IE"
    ITALY = "IT"
    JAPAN = "JP"
    MEXICO = "MX"
    NETHERLANDS = "NL"
    POLAND = "PL"
    SINGAPORE = "SG"
    SAUDI_ARABIA = "SA"
    SPAIN = "ES"
    SWEDEN = "SE"
    TURKEY = "TR"
    UNITED_ARAB_EMIRATES = "AE"
    UNITED_KINGDOM = "UK"
    UNITED_STATES = "US"