"""SEC Equity Profile Model."""

from typing import Any, Dict, List, Optional

from aiohttp_client_cache import SQLiteBackend
from aiohttp_client_cache.session import CachedSession
from openbb_core.app.utils import get_user_cache_directory
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.equity_profile import (
    EquityProfileData,
    EquityProfileQueryParams,
)
from openbb_core.provider.utils.helpers import amake_request
from openbb_


def download_company_facts(ticker: str, use_cache: bool = True) -> Dict:
    """Download the facts file from the SEC API."""

    HEADERS = {
        "User-Agent": "my real company name definitelynot@fakecompany.com",
        "Accept-Encoding": "gzip, deflate",
    }

    cik = symbol_map(ticker, use_cache=use_cache)

    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

    r = (
        requests.get(url, headers=HEADERS, timeout=5)
        if use_cache is False
        else sec_session_facts.get(url, headers=HEADERS, timeout=5)
    )

    if r.status_code == 200:
        return r.json()
    raise RuntimeError(f"Request failed with status code {str(r.status_code)}")
