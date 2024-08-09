import asyncio
from typing import Dict, List, Literal

from openbb_core.provider.utils.helpers import amake_request
from pandas import DataFrame

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Accept": "*/*",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Connection": "keep-alive",
}

symbol_data = "https://seekingalpha.com/api/v3/symbol_data?fields[]=peRatioFwd&fields[]=lastClosePriceEarningsRatio&slugs=SMCI"
historical_prices = "https://seekingalpha.com/api/v3/historical_prices?filter[ticker][slug]=smci,sp500&filter[for_date][]=2024-05-21&filter[for_date][]=2024-5-25&sort=as_of_date"
historical_ohlc = "https://static.seekingalpha.com/cdn/finance-api/lua_charts?period=MAX&ticker_id=7098"
historical_periods = ["1D", "1M", "6M", "YTD", "1Y", "5Y", "10Y", "MAX"]

earnings_transcripts = "https://seekingalpha.com/api/v3/articles?filter[category]=earnings::earnings-call-transcripts&filter[unread]=true&filter[since]=0&filter[until]=0&include=author,primaryTickers,secondaryTickers&isMounting=true&page[size]=40&page[number]=2"


def _generate_tickers_url(asset_type, page) -> str:
    """Generate URL for the request."""
    return f"https://seekingalpha.com/api/v3/screener_results?type={asset_type}&page={page}&per_page=500&total_count=true"


async def get_all_tickers(asset_type: Literal["stock", "etf"] = "etf") -> Dict:
    """Retrieve a map of tickers and Seeking Alpha IDs by asset type."""
    data: List[Dict] = []
    page_1 = _generate_tickers_url(asset_type, 1)
    r = await amake_request(method="POST", url=page_1, headers=HEADERS)
    n_count = r.get("meta", {}).get("count")
    data = r.get("data")
    n_pages = round(n_count / 500)
    if n_pages * 500 <= n_count:
        n_pages += 1
    pages = range(2, n_pages + 1)
    urls = [_generate_tickers_url(asset_type, page) for page in pages]

    async def get_page(url):
        """Get a page of data."""

        response = await amake_request(method="POST", url=url, headers=HEADERS)
        new_data = response.get("data", [])
        if new_data:
            data.extend(new_data)

    await asyncio.gather(*[get_page(url) for url in urls])

    results = [
        {
            "symbol": d["attributes"].get("slug", "").upper(),
            "name": d["attributes"].get("companyName"),
            "seeking_alpha_id": d.get("id"),
        }
        for d in data
    ]

    return results


def update_json_files(asset_type: Literal["stock", "etf"] = "etf") -> None:
    """Update the static JSON files with symbol ID maps."""
    import nest_asyncio  # pylint: disable=import-outside-toplevel

    nest_asyncio.apply()
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(get_all_tickers(asset_type))
    df = DataFrame(response)
    df.set_index("symbol")["seeking_alpha_id"].to_json(f"{asset_type}_id_map.json")


QUOTES_URL = "https://finance-api.seekingalpha.com/real_time_quotes?sa_ids=9026"
