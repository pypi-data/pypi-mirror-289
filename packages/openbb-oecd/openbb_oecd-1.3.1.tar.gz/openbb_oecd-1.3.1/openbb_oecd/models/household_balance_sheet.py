"""OECD Household Balance Sheet Model.

"https://data-explorer.oecd.org/vis?lc=en&df[ds]=DisseminateFinalDMZ&df[id]=DSD_NASEC20%40DF_T7HH_Q&df[ag]=OECD.SDD.NAD&pd=%2C&dq=Q....S1M...A..F63%2BF52..USD......&ly[rw]=INSTR_ASSET&ly[cl]=TIME_PERIOD&ly[rs]=REF_AREA&to[TIME_PERIOD]=false&vw=tb"
"""

COUNTRIES = {
    "australia": "AUS",
    "austria": "AUT",
    "belgium": "BEL",
    "canada": "CAN",
    "chile": "CHL",
    "colombia": "COL",
    "croatia": "HRV",
    "czechia": "CZE",
    "denmark": "DNK",
    "estonia": "EST",
    "finland": "FIN",
    "france": "FRA",
    "germany": "DEU",
    "greece": "GRC",
    "hungary": "HUN",
    "iceland": "ISL",
    "ireland": "IRL",
    "italy": "ITA",
    "japan": "JPN",
    "korea": "KOR",
    "luxembourg": "LUX",
    "mexico": "MEX",
    "netherlands": "NLD",
    "new zealand": "NZL",
    "norway": "NOR",
    "poland": "POL",
    "portugal": "PRT",
    "slovak republic": "SVK",
    "spain": "ESP",
    "sweden": "SWE",
    "switzerland": "CHE",
    "turkey": "TUR",
    "united kingdom": "GBR",
    "united states": "USA",
}

period_dict = {
    "quarter": "Q",
    "annual": "A",
}
period = "quarter"
start_date = "2023-Q4"
country = ""
accounting_entry_dict = {
    "all": "",
    "assets": "A",
    "liabilities": "L",
}
accounting_entry = "all"

assets_dict = {
    "all_assets": "",
}
debt_maturity_dict = {
    "all": "",
    "short_term": "S",
    "long_term": "L",
}
debt_maturity = "all"
liabilities_dict = {
    "all_loans": "F4",
    "consumer_credit": "F4A",
    "revolving_credit": "F4A1",
    "non_revolving_credit": "F4A2",
    "house_purchase_loans": "F4B",
    "other_loans": "F4C",
}
liabilities = "all"
url = (
    "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NASEC20@DF_T7HH_Q,/"
    + f"{period_dict.get(period, 'Q')}..{country}..S1M"
    + f".....{liabilities_dict.get(liabilities, '')}.{accounting_entry_dict.get(accounting_entry, '')}"
    + f".{debt_maturity_dict.get(debt_maturity, '')}."
    + "USD......?"
    + f"startPeriod={start_date}"
    + "&dimensionAtObservation=AllDimensions"
)
