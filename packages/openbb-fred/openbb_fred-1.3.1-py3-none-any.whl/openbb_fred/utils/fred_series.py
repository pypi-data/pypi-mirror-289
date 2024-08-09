"""FRED Series IDs"""

from datetime import date as dateType
from typing import Optional, Union

def get_bop_series(country: str) -> dict:
    """Get the series IDs for the B6 Balance of Payments Report."""

    return dict(
        # Current Account Balance in USD.
        balance_percent_of_gdp=f"{country}B6BLTT02STSAQ",
        balance_total=f"{country}B6BLTT01CXCUSAQ",
        balance_total_services=f"{country}B6BLSE01CXCUSAQ",
        balance_total_secondary_income=f"{country}B6BLSI01CXCUSAQ",
        balance_total_goods=f"{country}B6BLTD01CXCUSAQ",
        balance_total_primary_income=f"{country}B6BLPI01CXCUSAQ",
        # Current Account Credits in USD
        credits_services_percent_of_goods_and_services=f"{country}B6CRSE03STSAQ",
        credits_services_percent_of_current_account=f"{country}B6CRSE02STSAQ",
        credits_total_services=f"{country}B6CRSE01CXCUSAQ",
        credits_total_goods=f"{country}B6CRTD01CXCUSAQ",
        credits_total_primary_income=f"{country}B6CRPI01CXCUSAQ",
        credits_total_secondary_income=f"{country}B6CRSI01CXCUSAQ",
        credits_total=f"{country}B6CRTT01CXCUSAQ",
        # Current Account Debits in USD
        debits_services_percent_of_goods_and_services=f"{country}B6DBSE03STSAQ",
        debits_services_percent_of_current_account=f"{country}B6DBSE02STSAQ",
        debits_total_services=f"{country}B6DBSE01CXCUSAQ",
        debits_total_goods=f"{country}B6DBTD01CXCUSAQ",
        debits_total_primary_income=f"{country}B6DBPI01CXCUSAQ",
        debits_total=f"{country}B6DBTT01CXCUSAQ",
        debits_total_secondary_income=f"{country}B6DBSI01CXCUSAQ",
    )


CPI_SYMBOL = "CPALTT01%s%s657N"  # Consumer Price Index All Items - 2-Letter Country Code - A,Q,M. - 7 is growth previous period, 9 is growth same period one year ago.


PRICES_MEATS = [
    "bacon",
    "beef",
    "bologna",
    "chicken",
    "chops",
    "ham",
    "frankfurters",
    "picnic",
    "lamb",
    "roast",
    "steak",
    "tuna",
    "turkey",
]

PRICES_DAIRY = [
    "eggs",
    "cheese",
    "cream",
    "milk",
    "butter",
    "yogurt",
]

PRICES_CEREALS = [
    "bread",
    "cookies",
    "crackers",
    "cupcakes",
    "flour",
    "rice",
    "rolls",
    "spaghetti",
]

PRICES_PRODUCE = [
    "apples",
    "apple",
    "bananas",
    "beans",
    "broccoli",
    "cabbage",
    "carrots",
    "celery",
    "cherries",
    "corn",
    "cucumbers",
    "grapefruit",
    "grapes",
    "lemons",
    "lettuce",
    "mushrooms",
    "onions",
    "oranges",
    "peaches",
    "pears",
    "peppers",
    "potatoes",
    "radishes",
    "strawberries",
    "tomatoes",
]

PRICES_BEVERAGES = [
    "beer",
    "cola",
    "malt",
    "vodka",
    "orange juice",
    "soft_drinks",
    "wine",
    "whiskey",
]

PRICES_OTHER_FOODS = [
    "coffee",
    "candy",
    "jelly",
    "margarine",
    "peanut_butter",
    "potato_chips",
    "shortening",
    "sugar",
    "tea",
]

ALL_FOOD = (
    PRICES_MEATS
    + PRICES_DAIRY
    + PRICES_CEREALS
    + PRICES_PRODUCE
    + PRICES_BEVERAGES
    + PRICES_OTHER_FOODS
)

PRICES_FUEL = [
    "diesel",
    "electricity",
    "gasoline",
    "oil",
    "utility",
]

RETAIL_PRICES = ALL_FOOD + PRICES_FUEL


BAML_REGIONS = ["us", "eu", "ex_g10", "emea", "asia", "latin_america"]
BamlCategories = Literal["high_yield", "us", "emerging_markets"]
BamlRegions = Literal["us", "eu", "ex_g10", "emea", "asia", "latin_america"]
BAML_UNITS = ["yield", "oas", "total_return", "yield_to_worst"]

BAML_CATEGORIES = {
    "high_yield": {
        "us": {
            "total_return": "BAMLHYH0A0HYM2TRIV",
            "yield": "BAMLH0A0HYM2EY",
            "oas": "BAMLH0A0HYM2",
            "yield_to_worst": "BAMLH0A0HYM2SYTW",
        },
        "europe": {
            "total_return": "BAMLHE00EHYITRIV",
            "yield": "BAMLHE00EHYIEY",
            "oas": "BAMLHE00EHYIOAS",
            "yield_to_worst": "BAMLHE00EHYISYTW",
        },
        "emerging": {
            "total_return": "BAMLEMHBHYCRPITRIV",
            "yield": "BAMLEMHBHYCRPIEY",
            "oas": "BAMLEMHBHYCRPIOAS",
            "yield_to_worst": "BAMLEMHBHYCRPISYTW",
        },
    },
    "us": {
        "corporate": {
            "total_return": "BAMLCC0A0CMTRIV",
            "yield": "BAMLC0A0CMEY",
            "oas": "BAMLC0A0CM",
            "yield_to_worst": "BAMLC0A0CMSYTW",
        },
        "high_yield": {
            "total_return": "BAMLHYH0A0HYM2TRIV",
            "yield": "BAMLH0A0HYM2EY",
            "oas": "BAMLH0A0HYM2",
            "yield_to_worst": "BAMLH0A0HYM2SYTW",
        },
        "yield_curve": {
            "1y_3y": {
                "total_return": "BAMLCC1A013YTRIV",
                "yield": "BAMLC1A0C13YEY",
                "oas": "BAMLC1A0C13Y",
                "yield_to_worst": "BAMLC1A0C13YSYTW",
            },
            "3y_5y": {
                "total_return": "BAMLCC2A035YTRIV",
                "yield": "BAMLC2A0C35YEY",
                "oas": "BAMLC2A0C35Y",
                "yield_to_worst": "BAMLC2A0C35YSYTW",
            },
            "5y_7y": {
                "total_return": "BAMLCC3A057YTRIV",
                "yield": "BAMLC3A0C57YEY",
                "oas": "BAMLC3A0C57Y",
                "yield_to_worst": "BAMLC3A0C57YSYTW",
            },
            "7y_10y": {
                "total_return": "BAMLCC4A0710YTRIV",
                "yield": "BAMLC4A0C710YEY",
                "oas": "BAMLC4A0C710Y",
                "yield_to_worst": "BAMLC4A0C710YSYTW",
            },
            "10y_15y": {
                "total_return": "BAMLCC7A01015YTRIV",
                "yield": "BAMLC7A0C1015YEY",
                "oas": "BAMLC7A0C1015Y",
                "yield_to_worst": "BAMLC7A0C1015YSYTW",
            },
            "15y+": {
                "total_return": "BAMLCC8A015PYTRIV",
                "yield": "BAMLC8A0C15PYEY",
                "oas": "BAMLC8A0C15PY",
                "yield_to_worst": "BAMLC8A0C15PYSYTW",
            },
        },
        "aaa": {
            "total_return": "BAMLCC0A1AAATRIV",
            "yield": "BAMLC0A1CAAAEY",
            "oas": "BAMLC0A1CAAA",
            "yield_to_worst": "BAMLC0A1CAAASYTW",
        },
        "aa": {
            "total_return": "BAMLCC0A2AATRIV",
            "yield": "BAMLC0A2CAAEY",
            "oas": "BAMLC0A2CAA",
            "yield_to_worst": "BAMLC0A2CAASYTW",
        },
        "a": {
            "total_return": "BAMLCC0A3ATRIV",
            "yield": "BAMLC0A3CAEY",
            "oas": "BAMLC0A3CA",
            "yield_to_worst": "BAMLC0A3CASYTW",
        },
        "bbb": {
            "total_return": "BAMLCC0A4BBBTRIV",
            "yield": "BAMLC0A4CBBBEY",
            "oas": "BAMLC0A4CBBB",
            "yield_to_worst": "BAMLC0A4CBBBSYTW",
        },
        "bb": {
            "total_return": "BAMLHYH0A1BBTRIV",
            "yield": "BAMLH0A1HYBBEY",
            "oas": "BAMLH0A1HYBB",
            "yield_to_worst": "BAMLH0A1HYBBSYTW",
        },
        "b": {
            "total_return": "BAMLHYH0A2BTRIV",
            "yield": "BAMLH0A2HYBEY",
            "oas": "BAMLH0A2HYB",
            "yield_to_worst": "BAMLH0A2HYBSYTW",
        },
        "ccc": {
            "total_return": "BAMLHYH0A3CMTRIV",
            "yield": "BAMLH0A3HYCEY",
            "oas": "BAMLH0A3HYCC",
            "yield_to_worst": "BAMLH0A3HYCCSYTW",
        },
    },
    "emerging_markets": {
        "crossover": {
            "total_return": "BAMLEM5BCOCRPITRIV",
            "yield": "BAMLEM5BCOCRPIEY",
            "oas": "BAMLEM5BCOCRPIOAS",
            "yield_to_worst": "BAMLEM5BCOCRPISYTW",
        },
        "public_sector": {
            "total_return": "BAMLEMPUPUBSLCRPIUSTRIV",
            "yield": "BAMLEMPUPUBSLCRPIUSEY",
            "oas": "BAMLEMPUPUBSLCRPIUSOAS",
            "yield_to_worst": "BAMLEMPUPUBSLCRPIUSSYTW",
        },
        "private_sector": {
            "total_return": "BAMLEMFSFCRPITRIV",
            "yield": "BAMLEMFSFCRPIEY",
            "oas": "BAMLEMFSFCRPIOAS",
            "yield_to_worst": "BAMLEMFSFCRPISYTW",
        },
        "non_financial": {
            "total_return": "BAMLEMNFNFLCRPIUSTRIV",
            "yield": "BAMLEMNFNFLCRPIUSEY",
            "oas": "BAMLEMNFNFLCRPIUSOAS",
            "yield_to_worst": "BAMLEMNFNFLCRPIUSSYTW",
        },
        "high_grade": {
            "total_return": "BAMLEMIBHGCRPITRIV",
            "yield": "BAMLEMIBHGCRPIEY",
            "oas": "BAMLEMIBHGCRPIOAS",
            "yield_to_worst": "BAMLEMIBHGCRPISYTW",
        },
        "high_yield": {
            "total_return": "BAMLEMHBHYCRPITRIV",
            "yield": "BAMLEMHBHYCRPIEY",
            "oas": "BAMLEMHBHYCRPIOAS",
            "yield_to_worst": "BAMLEMHBHYCRPISYTW",
        },
        "liquid_emea": {
            "total_return": "BAMLEMELLCRPIEMEAUSTRIV",
            "yield": "BAMLEMELLCRPIEMEAUSEY",
            "oas": "BAMLEMELLCRPIEMEAUSOAS",
            "yield_to_worst": "BAMLEMELLCRPIEMEAUSSYTW",
        },
        "emea": {
            "total_return": "BAMLEMRECRPIEMEATRIV",
            "yield": "BAMLEMRECRPIEMEAEY",
            "oas": "BAMLEMRECRPIEMEAOAS",
            "yield_to_worst": "BAMLEMRECRPIEMEASYTW",
        },
        "liquid_asia": {
            "total_return": "BAMLEMALLCRPIASIAUSTRIV",
            "yield": "BAMLEMALLCRPIASIAUSEY",
            "oas": "BAMLEMALLCRPIASIAUSOAS",
            "yield_to_worst": "BAMLEMALLCRPIASIAUSSYTW",
        },
        "asia": {
            "total_return": "BAMLEMRACRPIASIATRIV",
            "yield": "BAMLEMRACRPIASIAEY",
            "oas": "BAMLEMRACRPIASIAOAS",
            "yield_to_worst": "BAMLEMRACRPIASIASYTW",
        },
        "liquid_latam": {
            "total_return": "BAMLEMLLLCRPILAUSTRIV",
            "yield": "BAMLEMLLLCRPILAUSEY",
            "oas": "BAMLEMLLLCRPILAUSOAS",
            "yield_to_worst": "BAMLEMLLLCRPILAUSSYTW",
        },
        "latam": {
            "total_return": "BAMLEMRLCRPILATRIV",
            "yield": "BAMLEMRLCRPILAEY",
            "oas": "BAMLEMRLCRPILAOAS",
            "yield_to_worst": "BAMLEMRLCRPILASYTW",
        },
        "liquid_aaa": {
            "total_return": "BAMLEM1RAAA2ALCRPIUSTRIV",
            "yield": "BAMLEM1RAAA2ALCRPIUSEY",
            "oas": "BAMLEM1RAAA2ALCRPIUSOAS",
            "yield_to_worst": "BAMLEM1RAAA2ALCRPIUSSYTW",
        },
        "liquid_bbb": {
            "total_return": "BAMLEM2RBBBLCRPIUSTRIV",
            "yield": "BAMLEM2RBBBLCRPIUSEY",
            "oas": "BAMLEM2RBBBLCRPIUSOAS",
            "yield_to_worst": "BAMLEM2RBBBLCRPIUSSYTW",
        },
        "aaa": {
            "total_return": "BAMLEM1BRRAAA2ACRPITRIV",
            "yield": "BAMLEM1BRRAAA2ACRPIEY",
            "oas": "BAMLEM1BRRAAA2ACRPIOAS",
            "yield_to_worst": "BAMLEM1BRRAAA2ACRPISYTW",
        },
        "bbb": {
            "total_return": "BAMLEM2BRRBBBCRPITRIV",
            "yield": "BAMLEM2BRRBBBCRPIEY",
            "oas": "BAMLEM2BRRBBBCRPIOAS",
            "yield_to_worst": "BAMLEM2BRRBBBCRPISYTW",
        },
        "bb": {
            "total_return": "BAMLEM3BRRBBCRPITRIV",
            "yield": "BAMLEM3BRRBBCRPIEY",
            "oas": "BAMLEM3BRRBBCRPIOAS",
            "yield_to_worst": "BAMLEM3BRRBBCRPISYTW",
        },
        "b": {
            "total_return": "BAMLEM4BRRBLCRPITRIV",
            "yield": "BAMLEM4BRRBLCRPIEY",
            "oas": "BAMLEM4BRRBLCRPIOAS",
            "yield_to_worst": "BAMLEM4BRRBLCRPISYTW",
        },
    },
}

FOREX_INTERVENTION = {
    "JPINTDUSDJPY": "Japanese Bank purchases of USD against JPY",
    "TRINTDEXR": "Turkish Central Bank Intervention in FX Market",
}

CONSUMER_LENDING_RATES = {  # Monthly
    "credit_cards_all_accounts": "TERMCBCCALLNS",
    "credit_cards_accounts_assessed_interest": "TERMCBCCINTNS",
    "new_auto_48month": "TERMCBAUTO48NS",
    "new_auto_60month": "RIFLPBCIANM60NM",
    "new_auto_72month": "RIFLPBCIANM72NM",
    "personal_loan_24month": "RIFLPBCIANM72NM",
}


FRB_G19 = (  # Consumer Credit Monthly Release
    "https://www.federalreserve.gov/datadownload/Output.aspx?rel=G19&series=be2df920f30707fd397c306408143a6c"
    + "&lastobs=1&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package"
)

CONSUMER_CREDIT_OUTSTANDING_SA = (
    "https://www.federalreserve.gov/datadownload/Output.aspx?rel=G19&series=696245eb361e0a8bc89b8e5b01cc971b"
    + "&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package"
)

TERMS_OF_CREDIT = (
    "https://www.federalreserve.gov/datadownload/Output.aspx?rel=G19&series=10264fd36110a9c4906bd99f1daccf29"
    + "&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package"
)

MAJOR_HOLDERS = (
    "https://www.federalreserve.gov/datadownload/Output.aspx?rel=G19&series=dea37e76c1a4d3eb237d24b2050f02c8"
    + "&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package"
)

REVOLVING_CREDIT = (
    "https://www.federalreserve.gov/datadownload/Output.aspx?rel=G19&series=168bdeb9b49de845a62b18770527f83b"
    + "&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package"
)

NONREVOLVING_CREDIT = (
    "https://www.federalreserve.gov/datadownload/Output.aspx?rel=G19&series=f744d5187fdad4336feea41a12530eaa"
    + "&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package"
)

CONSUMER_CREDIT_OUTSTANDING_FLOW = (
    "https://www.federalreserve.gov/datadownload/Output.aspx?rel=G19&series=df09a45a23c289622086512c543d634f"
    + "&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package"
)


measurement_dict = {
    "real": "R",
    "nominal": "N",
}
measurement = "real"
unit_dict = {
    "index": "628",
    "yoy": "771",
}
unit = "index"
coutry_dict = (
    {
        "euro_area": "XM",
        "developed_markets": "5R",
        "emerging_markets": "4T",
    },
)
country = "CA"  # 2-Letter Country Code
RESIDENTIAL_PROPERTY_PRICES = (
    f"Q{country}{measurement_dict[measurement]}{unit_dict[unit]}BIS"
)

bis = "https://data.bis.org/topics/RPP/BIS,WS_DPP,1.0/Q.US.0.2.1.3.0.0"


DISCOUNT_RATES = "INTDSR%sM193N" # Discount Rate - 2-Letter Country Code (IMF)

https://fred.stlouisfed.org/series/

# OECD

CENTRAL_BANK_RATE = "IRSTCB01%sM156N"
INTERBANK_RATE = "IRSTCI01%sM156N" # Interbank Rate - 2-Letter Country Code
PRIME_RATE = "IRSTPI01%sM156N" # Immediate Interest Rates - 2-Letter Country Code
SHORT_TERM_INTEREST_RATES = "IR3TIB01%sM156N" # Short Term Interest Rates - 2-Letter Country Code
LONG_TERM_INTEREST_RATES = "IRLTLT01%sM156N" # Long Term Interest Rates - 2-Letter Country Code

INTEREST_RATE_COUNTRIES = {
    "us": "US",
    "australia": "AU",
    "austria": "AT",
    "belgium": "BE",
    "brazil": "BR",
    "canada": "CA",
    "chech_republic": "CZ",
    "chile": "CL",
    "china": "CN",
    "denmark": "DK",
    "estonia": "EE",
    "euro_area": "EZ",
    "finland": "FI",
    "france": "FR",
    "germany": "DE",
    "greece": "GR",
    "hungary": "HU",
    "icealnd": "IS",
    "india": "IN",
    "indonesia": "ID",
    "ireland": "IE",
    "israel": "IL",
    "italy": "IT",
    "japan": "JP",
    "luxembourg": "LU",
    "mexico": "MX",
    "netehrlands": "NL",
    "new_zealand": "NZ",
    "norway": "NO",
    "poland": "PL",
    "portugal": "PT",
    "russia": "RU",
    "slovak_republic": "SK",
    "slovenia": "SI",
    "south_africa": "ZA",
    "south_korea": "KR",
    "spain": "ES",
    "sweden": "SE",
    "switzerland": "CH",
    "turkey": "TR",
    "united_kingdom": "GB",
}

chicago_survey_of_economic_conditions = { # Federal Reserve District 7: Chicago
    "manufacturing_activity": "CFSBCACTIVITYMFG",
    "non_manufacturing_activity": "CFSBCACTIVITYNMFG",
    "capital_spending_expectations": "CFSBCCAPXEXP",
    "hiring_expectations": "CFSBCHIRINGEXP",
    "one_year_outlook": "CFSBCOUTLOOK",
    "activity_index": "CFSBCACTIVITY",
    "current_hiring_index": "CFSBCHIRING",
    "labor_costs_index": "CFSBCLABORCOSTS",
    "non_labor_costs_index": "CFSBCNONLABORCOSTS"
}

TEXAS_MANUFACTURING_OUTLOOK = {
    "business_activity": {
        "diffusion_index": "BACTSAMFRBDAL",
        "percent_reporting_increase": "BACTISAMFRBDAL",
        "percent_reporting_decrease": "BACTDSAMFRBDAL",
        "percent_reporting_no_change": "BACTNSAMFRBDAL",
    },
    "future_business_activity": {
        "diffusion_index": "FBACTSAMFRBDAL",
        "percent_reporting_increase": "FBACTISAMFRBDAL",
        "percent_reporting_decrease": "FBACTDSAMFRBDAL",
        "percent_reporting_no_change": "FBACTNSAMFRBDAL",
    },
    "current_business_outlook": {
        "diffusion_index": "COLKSAMFRBDAL",
        "percent_reporting_increase": "COLKISAMFRBDAL",
        "percent_reporting_decrease": "COLKDSAMFRBDAL",
        "percent_reporting_no_change": "COLKNSAMFRBDAL",
    }
    "future_business_outlook": {
        "diffusion_index": "FCOLKSAMFRBDAL",
        "percent_reporting_increase": "FCOLKISAMFRBDAL",
        "percent_reporting_decrease": "FCOLKDSAMFRBDAL",
        "percent_reporting_no_change": "FCOLKNSAMFRBDAL",
    },
    "current_capex": {
        "diffusion_index": "CEXPSAMFRBDAL",
        "percent_reporting_increase": "CEXPISAMFRBDAL",
        "percent_reporting_decrease": "CEXPDSAMFRBDAL",
        "percent_reporting_no_change": "CEXPNSAMFRBDAL",
    },
    "future_capex": {
        "diffusion_index": "FCEXPSAMFRBDAL",
        "percent_reporting_increase": "FCEXPISAMFRBDAL",
        "percent_reporting_decrease": "FCEXPDSAMFRBDAL",
        "percent_reporting_no_change": "FCEXPNSAMFRBDAL",
    },
    "current_prices_paid": {
        "diffusion_index": "PRMSAMFRBDAL",
        "percent_reporting_increase": "PRMISAMFRBDAL",
        "percent_reporting_decrease": "PRMDSAMFRBDAL",
        "percent_reporting_no_change": "PRMNSAMFRBDAL",
    },
    "future_prices_paid": {
        "diffusion_index": "FPRMSAMFRBDAL",
        "percent_reporting_increase": "FPRMISAMFRBDAL",
        "percent_reporting_decrease": "FPRMDSAMFRBDAL",
        "percent_reporting_no_change": "FPRMNSAMFRBDAL",
    },
    "current_production": {
        "diffusion_index": "PRODSAMFRBDAL",
        "percent_reporting_increase": "PRODISAMFRBDAL",
        "percent_reporting_decrease": "PRODDSAMFRBDAL",
        "percent_reporting_no_change": "PRODNSAMFRBDAL",
    },
    "future_production": {
        "diffusion_index": "FPRODSAMFRBDAL",
        "percent_reporting_increase": "FPRODISAMFRBDAL",
        "percent_reporting_decrease": "FPRODDSAMFRBDAL",
        "percent_reporting_no_change": "FPRODNSAMFRBDAL",
    },
    "current_inventory": {
        "diffusion_index": "FGISAMFRBDAL",
        "percent_reporting_increase": "FGIISAMFRBDAL",
        "percent_reporting_decrease": "FGIDSAMFRBDAL",
        "percent_reporting_no_change": "FGINSAMFRBDAL",
    },
    "future_inventory": {
        "diffusion_index": "FFGISAMFRBDAL",
        "percent_reporting_increase": "FFGIISAMFRBDAL",
        "percent_reporting_decrease": "FFGIDSAMFRBDAL",
        "percent_reporting_no_change": "FFGINSAMFRBDAL",
    },
    "current_new_orders": {
        "diffusion_index": "VNWOSAMFRBDAL",
        "percent_reporting_increase": "VNWOISAMFRBDAL",
        "percent_reporting_decrease": "VNWODSAMFRBDAL",
        "percent_reporting_no_change": "VNWONSAMFRBDAL",
    },
    "future_new_orders": {
        "diffusion_index": "FVNWOSAMFRBDAL",
        "percent_reporting_increase": "FVNWOISAMFRBDAL",
        "percent_reporting_decrease": "FVNWODSAMFRBDAL",
        "percent_reporting_no_change": "FVNWONSAMFRBDAL",
    },
    "current_new_orders_growth": {
        "diffusion_index": "GROSAMFRBDAL",
        "percent_reporting_increase": "GROISAMFRBDAL",
        "percent_reporting_decrease": "GRODSAMFRBDAL",
        "percent_reporting_no_change": "GRONSAMFRBDAL",
    },
    "future_new_orders_growth": {
        "diffusion_index": "FGROSAMFRBDAL",
        "percent_reporting_increase": "FGROISAMFRBDAL",
        "percent_reporting_decrease": "FGRODSAMFRBDAL",
        "percent_reporting_no_change": "FGRONSAMFRBDAL",
    },
    "current_unfilled_orders": {
        "diffusion_index": "UFILSAMFRBDAL",
        "percent_reporting_increase": "UFILISAMFRBDAL",
        "percent_reporting_decrease": "UFILDSAMFRBDAL",
        "percent_reporting_no_change": "UFILNSAMFRBDAL",
    },
    "future_unfilled_orders": {
        "diffusion_index": "FUFILSAMFRBDAL",
        "percent_reporting_increase": "FUFILISAMFRBDAL",
        "percent_reporting_decrease": "FUFILDSAMFRBDAL",
        "percent_reporting_no_change": "FUFILNSAMFRBDAL",
    },
    "current_shipments": {
        "diffusion_index": "VSHPSAMFRBDAL",
        "percent_reporting_increase": "VSHPISAMFRBDAL",
        "percent_reporting_decrease": "VSHPDSAMFRBDAL",
        "percent_reporting_no_change": "VSHPNSAMFRBDAL",
    },
    "future_shipments": {
        "diffusion_index": "FVSHPSAMFRBDAL",
        "percent_reporting_increase": "FVSHPISAMFRBDAL",
        "percent_reporting_decrease": "FVSHPDSAMFRBDAL",
        "percent_reporting_no_change": "FVSHPNSAMFRBDAL",
    },
    "current_delivery_times": {
        "diffusion_index": "DTMSAMFRBDAL",
        "percent_reporting_increase": "DTMISAMFRBDAL",
        "percent_reporting_decrease": "DTMDSAMFRBDAL",
        "percent_reporting_no_change": "DTMNSAMFRBDAL",
    },
    "future_delivery_time": {
        "diffusion_index": "FDTMSAMFRBDAL",
        "percent_reporting_increase": "FDTMISAMFRBDAL",
        "percent_reporting_decrease": "FDTMDSAMFRBDAL",
        "percent_reporting_no_change": "FDTMNSAMFRBDAL",
    },
    "current_employment": {
        "diffusion_index": "NEMPSAMFRBDAL",
        "percent_reporting_increase": "NEMPISAMFRBDAL",
        "percent_reporting_decrease": "NEMPDSAMFRBDAL",
        "percent_reporting_no_change": "NEMPNSAMFRBDAL",
    },
    "future_employment": {
        "diffusion_index": "FNEMPSAMFRBDAL",
        "percent_reporting_increase": "FNEMPISAMFRBDAL",
        "percent_reporting_decrease": "FNEMPDSAMFRBDAL",
        "percent_reporting_no_change": "FNEMPNSAMFRBDAL",
    },
    "current_wages": {
        "diffusion_index": "WGSSAMFRBDAL",
        "percent_reporting_increase": "WGSISAMFRBDAL",
        "percent_reporting_decrease": "WGSDSAMFRBDAL",
        "percent_reporting_no_change": "WGSNSAMFRBDAL",
    },
    "future_wages": {
        "diffusion_index": "FWGSSAMFRBDAL",
        "percent_reporting_increase": "FWGSISAMFRBDAL",
        "percent_reporting_decrease": "FWGSDSAMFRBDAL",
        "percent_reporting_no_change": "FWGSNSAMFRBDAL",
    },
    "current_hours_worked": {
        "diffusion_index": "AVGWKSAMFRBDAL",
        "percent_reporting_increase": "AVGWKISAMFRBDAL",
        "percent_reporting_decrease": "AVGWKDSAMFRBDAL",
        "percent_reporting_no_change": "AVGWKNSAMFRBDAL",
    },
    "future_hours_worked": {
        "diffusion_index": "FAVGWKSAMFRBDAL",
        "percent_reporting_increase": "FAVGWKISAMFRBDAL",
        "percent_reporting_decrease": "FAVGWKDSAMFRBDAL",
        "percent_reporting_no_change": "FAVGWKNSAMFRBDAL",
    },
}

TEXAS_MANUFACTURING_OUTLOOK_TOPICS = [
    "business_activity",
    "business_outlook",
    "capex",
    "prices_paid",
    "production",
    "inventory",
    "new_orders",
    "new_orders_growth",
    "unfilled_orders",
    "shipments",
    "delivery_times",
    "employment",
    "wages",
    "hours_worked",
]

MORTGAGE_ID_TO_TITLE = {
    "OBMMIC30YF": "30-Year Fixed Rate Conforming",
    "OBMMIC30YFNA": "30-Year Fixed Rate Conforming Non-Adjusted",
    "OBMMIJUMBO30YF": "30-Year Fixed Rate Jumbo",
    "OBMMIFHA30YF": "30-Year Fixed Rate FHA",
    "OBMMIVA30YF": "30-Year Fixed Rate Veterans Affairs",
    "OBMMIUSDA30YF": "30-Year Fixed Rate USDA",
    "OBMMIC15YF": "15-Year Fixed Rate Conforming",
    "OBMMIC30YFLVLE80FGE740": "30-Year Fixed Rate Conforming LTV <= 80 FICO >= 740",
    "OBMMIC30YFLVLE80FB720A739": "30-Year Fixed Rate Conforming LTV <= 80 FICO 720-739",
    "OBMMIC30YFLVLE80FB700A719": "30-Year Fixed Rate Conforming LTV <= 80 FICO 700-719",
    "OBMMIC30YFLVLE80FB680A699": "30-Year Fixed Rate Conforming LTV <= 80 FICO 680-699",
    "OBMMIC30YFLVLE80FLT680": "30-Year Fixed Rate Conforming LTV <= 80 FICO < 680",
    "OBMMIC30YFLVGT80FGE740": "30-Year Fixed Rate Conforming LTV > 80 FICO >= 740",
    "OBMMIC30YFLVGT80FB720A739": "30-Year Fixed Rate Conforming LTV > 80 FICO 720-739",
    "OBMMIC30YFLVGT80FB700A719": "30-Year Fixed Rate Conforming LTV > 80 FICO 700-719",
    "OBMMIC30YFLVGT80FB680A699": "30-Year Fixed Rate Conforming LTV > 80 FICO 680-699",
    "OBMMIC30YFLVGT80FLT680": "30-Year Fixed Rate Conforming LTV > 80 FICO < 680",
}


MORTGAGE_GROUPS = {
    "primary": [
        "OBMMIC30YF",
        "OBMMIC30YFNA",
        "OBMMIJUMBO30YF",
        "OBMMIFHA30YF",
        "OBMMIVA30YF",
        "OBMMIUSDA30YF",
        "OBMMIC15YF",
    ],
    "ltv_lte_80": [
        "OBMMIC30YFLVLE80FGE740",
        "OBMMIC30YFLVLE80FB720A739",
        "OBMMIC30YFLVLE80FB700A719",
        "OBMMIC30YFLVLE80FB680A699",
        "OBMMIC30YFLVLE80FLT680",
    ],
    "ltv_gt_80": [
        "OBMMIC30YFLVGT80FGE740",
        "OBMMIC30YFLVGT80FB720A739",
        "OBMMIC30YFLVGT80FB700A719",
        "OBMMIC30YFLVGT80FB680A699",
        "OBMMIC30YFLVGT80FLT680",
    ],
}


MORTGAGE_CHOICES = {
    "primary": MORTGAGE_GROUPS["primary"],
    "ltv_lte_80": MORTGAGE_GROUPS["ltv_lte_80"],
    "ltv_gt_80": MORTGAGE_GROUPS["ltv_gt_80"],
    "conforming_30y": "OBMMIC30YF",
    "conforming_30y_na": "OBMMIC30YFNA",
    "jumbo_30y": "OBMMIJUMBO30YF",
    "fha_30y": "OBMMIFHA30YF",
    "va_30y": "OBMMIVA30YF",
    "usda_30y": "OBMMIUSDA30YF",
    "conforming_15y": "OBMMIC15YF",
    "ltv_lte80_fico_ge740": "OBMMIC30YFLVLE80FGE740",
    "ltv_lte80_fico_a720b739": "OBMMIC30YFLVLE80FB720A739",
    "ltv_lte80_fico_a700b719": "OBMMIC30YFLVLE80FB700A719",
    "ltv_lte80_fico_a680b699": "OBMMIC30YFLVLE80FB680A699",
    "ltv_lte80_fico_lt680": "OBMMIC30YFLVLE80FLT680",
    "ltv_gt80_fico_ge740": "OBMMIC30YFLVGT80FGE740",
    "ltv_gt80_fico_a720b739": "OBMMIC30YFLVGT80FB720A739",
    "ltv_gt80_fico_a700b719": "OBMMIC30YFLVGT80FB700A719",
    "ltv_gt80_fico_a680b699": "OBMMIC30YFLVGT80FB680A699",
    "ltv_gt80_fico_lt680": "OBMMIC30YFLVGT80FLT680",
}

MortgageChoices = Literal[
    "primary",
    "ltv_lte_80",
    "ltv_gt_80",
    "conforming_30y",
    "conforming_30y_na",
    "jumbo_30y",
    "fha_30y",
    "va_30y",
    "usda_30y",
    "conforming_15y",
    "ltv_lte80_fico_ge740",
    "ltv_lte80_fico_a720b739",
    "ltv_lte80_fico_a700b719",
    "ltv_lte80_fico_a680b699",
    "ltv_lte80_fico_lt680",
    "ltv_gt80_fico_ge740",
    "ltv_gt80_fico_a720b739",
    "ltv_gt80_fico_a700b719",
    "ltv_gt80_fico_a680b699",
    "ltv_gt80_fico_lt680",
]

async def get_tips_series():
    from pandas import to_datetime
    from openbb_core.app.command_runner import CommandRunner
    res = await CommandRunner().run(
        "/economy/fred_search",
        provider_choices={
            "provider": "fred",
        },
        standard_params={},
        extra_params={
            "release_id" : 72,
        }
    )
    df = res.to_df().query("not title.str.contains('DISCONTINUED')").set_index("series_id")
    df.loc[:,"due"] = df.title.apply(lambda x: x.split("Due ")[-1].strip()).apply(to_datetime)
    df = df[["due", "observation_start", "observation_end", "title"]]
    return df.sort_values(by="due").reset_index()  # type: ignore

async def get_tips(start_date: Optional[Union[str, dateType]] = None, end_date: Optional[Union[str, dateType]] = None):
    from openbb_core.app.command_runner import CommandRunner

    ids_df = await get_tips_series()
    ids = ids_df.series_id.to_list()
    due_map = ids_df.set_index('series_id')["due"].dt.date.to_dict()
    title_map = (
        ids_df.set_index('series_id')["title"]
        .str.replace("Treasury Inflation-Indexed", "TIPS")
        .str.replace("  ", " ").str.strip().to_dict()
    )

    res = await CommandRunner().run(
        "/economy/fred_series",
        provider_choices={
            "provider": "fred",
        },
        standard_params={
            "symbol" : ",".join(ids),
            "start_date": start_date,
            "end_date": end_date,
        },
        extra_params={}
    )
    df = res.to_df(index=None)
    meta = res.extra["results_metadata"]

    for k, v in title_map.items():
        if k in meta:
            meta[k]["title"] = v

    df = df.melt(
        id_vars="date",
        value_vars=[d for d in df.columns if d !="date"],
        var_name="symbol",
    ).dropna().sort_values(by="date")
    df = df.reset_index(drop=True)
    df["due"] = df.symbol.map(due_map)
    df["name"] = df.symbol.map(title_map)
    df["value"] = df["value"] / 100
    df = df[["date", "due", "symbol", "name", "value"]]
    df = df.sort_values(by=["date", "due"])  # type: ignore

    records = df.to_dict(orient="records")

    output = dict(  # pylint: disable=dict-method
        records=records,
        meta=meta,
    )

    return output
