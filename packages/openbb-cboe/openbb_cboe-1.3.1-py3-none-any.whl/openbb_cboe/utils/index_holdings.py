"""Cboe Index Holdings Utilities."""

INDEX_HOLDINGS_URLS = {
    "SPRF": "https://cdn.cboe.com/resources/indices/documents/sprf_strikes.xlsx",
}


MARKET_STATISTICS_URLS = {
    "us_options_market_share": "https://www.cboe.com/us/options/market_share/market/csv/?bias=Volume&auctions=y&oddLots=y",
    "us_options_market_share_30d": "https://www.cboe.com/us/options/market_share/market/csv/history/?bias=Volume&auctions=y&oddLots=y",
}

# %s is the year. Each year is daily data, and begins in 2007.
HISTORICAL_MAKRET_VOLUME = "https://www.cboe.com/us/equities/market_statistics/historical_market_volume/market_history_%s.csv-dl"

# Short interest reports for Cboe-listed equities. %s is the year and YYYYMMDD, respectively.
SHORT_INTEREST_REPORTS = "https://www.cboe.com/us/equities/market_statistics/short_interest/%s/Bats_Listed_Short_Interest-finra-%s.csv-dl"


IV_INDICES = {
    "global_developed_markets_iv": "VXMXEA",
    "global_emerging_markets_iv": "VXMXEF",
}

MSCI_WORLD_OPTIONS = (
    {  # https://www.cboe.com/tradable_products/msci/msci_index_options/
        "MSCI World Net Total Return USD Index": "MXWLD",
        "MSCI ACWI Net Total Return USD Index": "MXACW",
        "MSCI EAFE Price Return USD Index": "MXEA",
        "MSCI Emerging Markets Price Return USD Index": "MXEF",
        "MSCI USA Gross Total Return USD Index": "MXUSA",
    }
)

# 1 IBHY contract = +2500 high yield bonds
# 1 IBIG contract = +1100 investment grade
# https://marketdata.theocc.com/flex-reports?reportType=PR&optionType=E&reportDate=20240521
