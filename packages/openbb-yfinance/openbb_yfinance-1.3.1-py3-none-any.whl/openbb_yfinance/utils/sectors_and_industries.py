"""YFinance Sector & Industry Helpers."""

from typing import Dict, List

from yfinance.data import YfData

# https://query1.finance.yahoo.com/v1/finance/sectors/consumer-cyclical?formatted=true&withReturns=true&lang=en-US&region=US&crumb=4RNeMJ56Ymi

# ca_data = yfdata.get_raw_json("https://query1.finance.yahoo.com/v1/finance/sectors/consumer-cyclical?formatted=true&withReturns=true&lang=en-CA&region=CA")

# Historical prices represent market cap in millions.


earnings_cal_url = "https://finance.yahoo.com/calendar/earnings?day=2024-06-28"

econ_cal_url = "https://query1.finance.yahoo.com/ws/screeners/v1/finance/calendar-events?countPerDay=25&economicEventsHighImportanceOnly=true&economicEventsRegionFilter=&endDate=1719309600000&modules=economicEvents&startDate=1719223200000&lang=en-US&region=US"

_QUOTE_SUMMARY_URL_ = "https://query2.finance.yahoo.com/v10/finance/quoteSummary"

# FUTURES_CHAIN_SUMMARY = yfdata.get_raw_json("https://query2.finance.yahoo.com/v10/finance/quoteSummary/ES%3DF", params={"modules": "futuresChain"})


async def get_futures_quotes(symbols):
    # pylint: disable=import-outside-toplevel
    import os  # noqa
    from contextlib import (
        contextmanager,
        redirect_stderr,
        redirect_stdout,
        suppress,
    )  # noqa
    from aiohttp import ClientError  # noqa
    from openbb_yfinance.models.equity_quote import YFinanceEquityQuoteFetcher  # noqa
    from pandas import DataFrame  # noqa

    @contextmanager
    def suppress_all_output():
        with open(os.devnull, "w") as devnull, redirect_stdout(
            devnull
        ), redirect_stderr(devnull):
            yield

    with suppress_all_output(), suppress(ClientError):
        fetcher = YFinanceEquityQuoteFetcher()
        data = await fetcher.fetch_data(
            params={"symbol": ",".join(symbols)}, credentials={}
        )

    df = DataFrame([d.model_dump() for d in data])
    prices = df[["symbol", "bid", "ask", "prev_close"]].copy()
    prices.loc[:, "price"] = round((prices.ask + prices.bid) / 2, 2)
    prices.price = prices.price.fillna(prices.prev_close)
    return prices.set_index("symbol")["price"].to_dict()


def get_futures_symbols(symbol: str):
    """Get the list of futures symbols from the continuation symbol."""
    _symbol = symbol.upper() + "%3DF"
    URL = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{_symbol}"
    params = {"modules": "futuresChain"}
    response: Dict = YfData(session=None).get_raw_json(url=URL, params=params)
    futures_symbols: List = []
    if "quoteSummary" in response:
        result = response["quoteSummary"].get("result", [])
        if not result:
            raise ValueError(f"No futures chain found for, {symbol}")
        futures = result[0].get("futuresChain", {})
        if futures:
            futures_symbols = futures.get("futures", [])
    return futures_symbols


SECTOR_SYMBOLS = {
    "energy": "^YH309",
    "basic_materials": "^YH101",
    "industrials": "^YH310",
    "consumer_defensive": "^YH205",
    "consumer_cyclical": "^YH102",
    "financials_services": "^YH103",
    "healthcare": "^YH206",
    "technology": "^YH311",
    "communication_services": "^YH308",
    "utilities": "^YH207",
    "real_estate": "^YH104",
}

# https://query1.finance.yahoo.com/v1/finance/industries/silver?formatted=true&sectorKey=basic-materials&withReturns=true&lang=en-US&region=US&crumb=4RNeMJ56Ymi
# https://finance.yahoo.com/screener/predefined/sec-ind_ind-largest-equities_internet-retail/?offset=0&count=100
# https://query1.finance.yahoo.com/v1/finance/sectors/technology?formatted=false&withReturns=true&lang=en-CA&region=CA&crumb=4RNeMJ56Ymi

INDUSTRY_SYMBOLS = {
    "energy": {
        "oil_and_gas_integrated": "^YH30910030",
        "oil_and_gas_exploration_and_production": "^YH30910020",  # E&P
        "oil_and_gas_midstream": "^YH30910040",
        "oil_and_gas_refining_and_marketing": "^YH30910050",
        "oil_and_gas_equipment_and_services": "^YH30910060",
        "uranium": "^YH30920020",
        "oil_and_gas_drilling": "^YH30910010",
        "thermal_coal": "YH30920010",
    },
    "basic_materials": {
        "specialty_chemicals": "^YH10130020",
        "gold": "^YH10150040",
        "copper": "^YH10150020",
        "building_materials": "^YH10120010",
        "steel": "^YH10160020",
        "agricultural_inputs": "^YH10110010",
        "chemicals": "^YH10130010",
        "other_industrials_metal_and_mining": "^YH10150030",
        "lumber_and_wood_production": "^YH10140010",
        "aluminum": "^YH10150010",
        "other_precious_metals_and_mining": "^YH10150060",
        "coking_coal": "^YH10160010",
        "paper_and_paper_products": "^YH10140020",
        "silver": "^YH10150050",
    },
    "industrials": {
        "aerospace_and_defense": "^YH31010010",
        "specialty_industrial_machinery": "^YH31070020",
        "railroads": "^YH31080030",
        "farm_and_heavy_construction_machinery": "^YH31050010",
        "building_products_and_equipment": "^YH31040030",
        "specialty_business_services": "^YH31020010",
        "integrated_freight_and_logistics": "^YH31080060",
        "waste_management": "^YH31090010",
        "conglomerates": "^YH31030010",
        "industrial_distribution": "^YH31060010",
        "engineering_and_construction": "^YH31040010",
        "staffing_and_employment_services": "^YH31020050",
        "rental_leasing_and_services": "^YH31020030",
        "electrical_equipment_and_parts": "^YH31070060",
        "consulting_services": "^YH31020020",
        "trucking": "^YH31080050",
        "airlines": "^YH31080020",
        "tools_and_accessories": "^YH31070050",
        "security_and_protection_services": "^YH31020040",
        "pollution_and_treatment_controls": "^YH31070040",
        "marine_shipping": "^YH31080040",
        "metal_fabrication": "^YH31070030",
        "infrastructure_operations": "^YH31040020",
        "airports_and_air_services": "^YH31080010",
        "business_equipment_and_supplies": "^YH31070010",
    },
    "consumer_defensive": {
        "discount_stores": "^YH20550010",
        "beverages_non_alcoholic": "^YH20520010",
        "household_and_personal_products": "^YH20525030",
        "packaged_foods": "^YH20525040",
        "tobacco": "^YH20560010",
        "confectioners": "^YH20525010",
        "farm_products": "^YH20525020",
        "beverages_wineries_and_distilleries": "^YH20510020",
        "food_distribution": "^YH20550020",
        "grocery_stores": "^YH20550030",
        "education_and_training_services": "^YH20540010",
        "beverages_brewers": "^YH20510010",
    },
    "consumer_cyclical": {
        "internet_retail": "^YH10280050",
        "auto_manufacturers": "YH10200020",
        "restaurants": "^YH10270010",
        "home_improvement_retail": "^YH10280030",
        "travel_services": "^YH10290050",
        "specialty_retail": "^YH10280060",
        "apparel_retail": "^YH10280010",
        "residential_construction": "^YH10230010",
        "footwear_and_accessories": "^YH10240030",
        "auto_parts": "^YH10200030",
        "packaging_and_containers": "^YH10250010",
        "lodging": "^YH10290030",
        "auto_and_truck_dealerships": "^YH10200010",
        "resorts_and_casinos": "^YH10290040",
        "gambling": "^YH10290010",
        "leisure": "^YH10290020",
        "apparel_manufacturing": "^YH10240020",
        "personal_services": "^YH10260010",
        "furnishings_fixtures_and_appliances": "^YH10220010",
        "recreational_vehicles": "^YH10200040",
        "luxury_goods": "^YH10280040",
        "department_stores": "^YH10280020",
        "textile_manufacturing": "^YH10240010",
    },
    "financial_services": {
        "banks_diversified": "^YH10320010",
        "credit_services": "^YH10360010",
        "asset_management": "^YH10310010",
        "insurance_diversified": "^YH10340060",
        "banks_regional": "^YH10320020",
        "capital_markets": "^YH10330010",
        "financial_data_and_stock_exchanges": "^YH10330020",
        "insurance_property_and_casualty": "^YH10340020",
        "insurance_brokers": "^YH10340050",
        "insurance_life": "^YH10340010",
        "insurance_specialty": "^YH10340040",
        "mortgage_finance": "^YH10320030",
        "insurance_reinsurance": "^YH10340030",
        "shell_companies": "^YH10350010",
        "financial_conglomerates": "^YH10350020",
    },
    "healthcare": {
        "drug_manufacturers_general": "^YH20620010",
        "healthcare_plans": "^YH20630010",
        "medical_devices": "^YH20650010",
        "diagnostic_and_research": "^YH20660010",
        "biotechnology": "^YH20610010",
        "medical_instruments_and_supplies": "^YH20650020",
        "medical_care_facilities": "^YH20645010",
        "drug_manufacturers_specialty_and_generic": "^YH20620020",
        "medical_distribution": "^YH20670010",
        "health_information_services": "^YH20645030",
        "pharmaceutical_retailers": "^YH20645020",
    },
    "technology": {
        "software_infrastructure": "^YH31110030",
        "semiconductors": "^YH31130020",
        "consumer_electronics": "^YH31120030",
        "software_application": "^YH31110020",
        "it_services": "^YH31110010",
        "semiconductor_equipment_and_materials": "^YH31130010",
        "computer_hardware": "^YH31120020",
        "communication_equipment": "^YH31120010",
        "electronic_components": "^YH31120040",
        "scientific_and_technical_instruments": "^YH31120060",
        "solar": "^YH31130030",
        "electronics_and_computer_distribution": "^YH31120050",
    },
    "communication_services": {
        "internet_content_and_information": "^YH30830010",
        "telecom_services": "^YH30810010",
        "entertainment": "^YH30820040",
        "electronic_gaming_and_multimedia": "^YH30830020",
        "advertising_agencies": "^YH30820010",
        "broadcasting": "^YH30820030",
        "publishing": "^YH30820020",
    },
    "utilities": {
        "regulated_electric": "^YH20720020",
        "renewable": "^YH20710020",
        "diversified": "^YH20720040",
        "regulated_gas": "^YH20720030",
        "independent_power_producers": "^YH20710010",
        "regulated_water": "^YH20720010",
    },
    "real_estate": {
        "reit_specialty": "^YH10420080",
        "reit_industrial": "^YH10420030",
        "reit_residential": "^YH10420050",
        "reit_retail": "^YH10420060",
        "reit_healthcare_facilities": "^YH10420010",
        "real_estate_services": "^YH10410020",
        "reit_office": "^YH10420040",
        "reit_diversified": "^YH10420090",
        "reit_mortgage": "^YH10420070",
        "reit_hotel_and_motel": "^YH10420020",
        "real_estate_diversified": "^YH10410030",
        "real_estate_development": "^YH10410010",
    },
}

# with yf.Ticker
# {k: v for k,v  in ticker.basic_info.items()}

# ticker.get_info()
# {'exchange': 'YHD',
# 'quoteType': 'NONE',
# 'symbol': '^YH101',
# 'underlyingSymbol': '^YH101',
# 'shortName': 'Basic Materials (Sector)',
# 'firstTradeDateEpochUtc': 1515594600,
# 'timeZoneFullName': 'America/New_York',
# 'timeZoneShortName': 'EDT',
# 'uuid': '9fe72762-6c2d-39dc-aeca-a3b2d1950883',
# 'messageBoardId': 'finmb_INDEXYH101',
# 'gmtOffSetMilliseconds': -14400000,
# 'maxAge': 86400,
# 'trailingPegRatio': None}
