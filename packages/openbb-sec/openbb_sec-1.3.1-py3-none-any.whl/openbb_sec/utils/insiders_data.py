"""SEC Insiders Data Utility"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional

from openbb_core.provider.utils.helpers import amake_request
from openbb_sec.utils.definitions import SEC_HEADERS


def convert_quarter_to_date(quarter: str) -> str:
    """Converts the quarter to the last of the quarter."""
    year, q = quarter.split(" ")
    if q == "Q1":
        month_date = "03-31"
    elif q == "Q2":
        month_date = "06-30"
    elif q == "Q3":
        month_date = "09-30"
    else:
        month_date = "12-31"
    return f"{year}-{month_date}"


async def get_insider_data_urls() -> Dict:
    """Get the list of URLS to download the insider datasets from the SEC website.
    Data begins in 2006 and is updated quarterly.
    """
    data = await amake_request("https://www.sec.gov/data.json", headers=SEC_HEADERS)
    insiders_data = [
        d["distribution"]
        for d in data["dataset"]  # type: ignore
        if d["title"] == "Insider Transactions Data Sets"
    ][0]
    data_urls = {d["title"]: d["downloadURL"] for d in insiders_data}
    dates = [(" ").join(d.split(" ")[:2]) for d in data_urls]
    dates = [convert_quarter_to_date(d) for d in dates]
    urls = dict(zip(dates, data_urls.values()))

    return urls


def get_filing_candidates(
    symbol: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> List[Dict]:
    """Get the list of filing candidates based on the symbol and date range."""

    if start_date is None:
        start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    SEARCH_URL = f"https://efts.sec.gov/LATEST/search-index?dateRange=custom&category=custom&startdt={start_date}&enddt={end_date}&3%252C4%252C5"
    SEARCH_URL = SEARCH_URL + "&entityName=" + symbol if symbol else SEARCH_URL

    filing_candidates: List[Dict] = []
    data = amake_request(SEARCH_URL, headers=SEC_HEADERS)
    return data
