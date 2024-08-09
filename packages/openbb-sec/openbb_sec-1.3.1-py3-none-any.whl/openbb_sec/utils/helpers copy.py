"""SEC Helpers module"""

# flake8: noqa

import concurrent.futures
from datetime import (
    datetime,
    timedelta,
)
from typing import Dict, List, Optional, Union

import pandas as pd
import requests
import requests_cache
import xmltodict
from bs4 import BeautifulSoup
from openbb_core.provider.utils.helpers import amake_request
from aiohttp_client_cache import SQLiteBackend
from aiohttp_client_cache.session import CachedSession
from openbb_sec.models.company_filings import (
    SecCompanyFilingsFetcher,
    SecCompanyFilingsQueryParams,
)
from openbb_sec.utils.definitions import HEADERS, QUARTERS, SEC_HEADERS, TAXONOMIES
from pydantic import BaseModel, ConfigDict


async def sec_callback(response, _):
    """Response callback for SEC requests."""
    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        return await response.json()
    if "text/html" in content_type:
        return await response.text(encoding="latin1")
    return await response.text()


async def search_investment_company_series(keyword: str = "", use_cache: bool = True):
    """Search for an investment company series by keyword or symbol.

    Info: https://www.sec.gov/about/opendatasetsshtmlinvestment_company
    """
    # pylint: disable=import-outside-toplevel
    from io import StringIO
    from pandas import read_csv
    from openbb_core.app.utils import get_user_cache_directory

    url = (
        "https://www.sec.gov/files/investment/data/other/investment-company-series-and-class-information"
        + "/investment_company_series_class.csv"
    )

    response: Union[dict, List[dict]] = {}
    if use_cache is True:
        cache_dir = f"{get_user_cache_directory()}/http/sec_investment_company_series"
        async with CachedSession(
            cache=SQLiteBackend(cache_dir, expire_after=3600 * 24 * 30)
        ) as session:
            try:
                response = await amake_request(url, headers=SEC_HEADERS, session=session, response_callback=sec_callback)  # type: ignore
            finally:
                await session.close()
    else:
        response = await amake_request(url, headers=SEC_HEADERS, response_callback=sec_callback)  # type: ignore

    df = read_csv(StringIO(response))  # type: ignore
    df = df[
        [
            "class_ticker_symbol",
            "CIK",
            "entity_name",
            "class_name",
            "class_id",
            "series_name",
            "series_id",
        ]
    ].replace({"[NULL]": None})
    df.series_name = df.series_name.str.replace("amp;", "")
    results = (
        df[
            df.entity_name.str.contains(keyword, case=False)
            | df.class_name.str.contains(keyword, case=False)
            | df.series_name.str.contains(keyword, case=False)
            | df.class_ticker_symbol.str.contains(keyword, case=False)
        ]
        if keyword
        else df
    )

    return results


def get_all_companies(use_cache: bool = True) -> pd.DataFrame:
    """Gets all company names, tickers, and CIK numbers registered with the SEC.
    Companies are sorted by market cap.

    Returns
    -------
    pd.DataFrame: Pandas DataFrame with columns for Symbol, Company Name, and CIK Number.

    Example
    -------
    >>> tickers = get_all_companies()
    """

    url = "https://www.sec.gov/files/company_tickers.json"

    r = (
        sec_session_companies.get(url, headers=SEC_HEADERS, timeout=5)
        if use_cache is True
        else requests.get(url, headers=SEC_HEADERS, timeout=5)
    )
    df = pd.DataFrame(r.json()).transpose()
    cols = ["cik", "symbol", "name"]
    df.columns = cols
    return df.astype(str)


def get_all_ciks(use_cache: bool = True) -> pd.DataFrame:
    """Gets a list of entity names and their CIK number."""

    HEADERS = {
        "User-Agent": "my real company name definitelynot@fakecompany.com",
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.sec.gov",
    }
    url = "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt"
    r = (
        sec_session_companies.get(url, headers=HEADERS, timeout=5)
        if use_cache is True
        else requests.get(url, headers=HEADERS, timeout=5)
    )
    data = r.text
    lines = data.split("\n")
    data_list = []
    delimiter = ":"
    for line in lines:
        row = line.split(delimiter)
        data_list.append(row)
    df = pd.DataFrame(data_list)
    df = df.iloc[:, 0:2]
    cols = ["Institution", "CIK Number"]
    df.columns = cols
    df = df.dropna()

    return df


def get_mf_and_etf_map(use_cache: bool = True) -> pd.DataFrame:
    """Returns the CIK number of a ticker symbol for querying the SEC API."""

    symbols = pd.DataFrame()

    url = "https://www.sec.gov/files/company_tickers_mf.json"
    r = (
        sec_session_companies.get(url, headers=SEC_HEADERS, timeout=5)
        if use_cache is True
        else requests.get(url, headers=SEC_HEADERS, timeout=5)
    )
    if r.status_code == 200:
        symbols = pd.DataFrame(data=r.json()["data"], columns=r.json()["fields"])

    return symbols


def search_institutions(keyword: str, use_cache: bool = True) -> pd.DataFrame:
    """Search for an institution by name.  It is case-insensitive."""
    institutions = get_all_ciks(use_cache=use_cache)
    hp = institutions["Institution"].str.contains(keyword, case=False)
    return institutions[hp].astype(str)


def symbol_map(symbol: str, use_cache: bool = True) -> str:
    """Returns the CIK number of a ticker symbol for querying the SEC API."""

    symbol = symbol.upper().replace(".", "-")
    symbols = get_all_companies(use_cache=use_cache)

    if symbol not in symbols["symbol"].to_list():
        symbols = get_mf_and_etf_map().astype(str)
        if symbol not in symbols["symbol"].to_list():
            return ""

    cik = symbols[symbols["symbol"] == symbol]["cik"].iloc[0]
    cik_: str = ""
    temp = 10 - len(cik)
    for i in range(temp):
        cik_ = cik_ + "0"

    return str(cik_ + cik)


def catching_diff_url_formats(ftd_urls: list) -> list:
    """Catches if URL for SEC data is one of the few URLS that are not in the
    standard format. Catches are for either specific date ranges that have a different
    format or singular URLs that have a different format.

    Parameters
    ----------
    ftd_urls : list
        list of urls of sec data

    Returns
    -------
    list
        list of ftd urls
    """
    feb_mar_apr_catch = ["202002", "202003", "202004"]
    for i, ftd_url in enumerate(ftd_urls):
        # URLs with dates prior to the first half of June 2017 have different formats
        if int(ftd_url[58:64]) < 201706 or "201706a" in ftd_url:
            ftd_urls[i] = ftd_url.replace(
                "fails-deliver-data",
                "frequently-requested-foia-document-fails-deliver-data",
            )
        # URLs between february, march, and april of 2020 have different formats
        elif any(x in ftd_urls[i] for x in feb_mar_apr_catch):
            ftd_urls[i] = ftd_url.replace(
                "data/fails-deliver-data", "node/add/data_distribution"
            )
        # First half of october 2019 has a different format
        elif (
            ftd_url
            == "https://www.sec.gov/files/data/fails-deliver-data/cnsfails201910a.zip"
        ):
            ftd_urls[i] = (
                "https://www.sec.gov/files/data/fails-deliver-data/cnsfails201910a_0.zip"
            )

    return ftd_urls


def download_files(urls: List[str]) -> List[Dict]:
    results = []

    def get_one(url):
        r = sec_session_facts.get(url, timeout=5, headers=HEADERS)
        if r.status_code == 200:
            results.extend([r])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_one, urls)

    return results


class CompanyFacts(BaseModel):
    """
    Extracts the data from the CompanyFacts object.

    DataFrame(aapl.extract_fact("EarningsPerShareDiluted", parse_units=True)).drop_duplicates(subset="filed", keep="last").sort_values(by="filed").query("`fy`==2015")

    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

    def extract_fact(self, fact: str, parse_units: bool = True) -> Dict:
        """Extracts the data from the CompanyFacts object."""

        response = {}
        keys = list(self.model_extra.keys())

        if "facts_us_gaap" in keys and fact in self.facts_us_gaap:
            response = self.all_data["facts"]["us-gaap"][fact]
            units = list(response["units"].keys())

        if "facts_dei" in keys and fact in self.facts_dei:
            response = self.all_data["facts"]["dei"][fact]
            units = list(response["units"].keys())

        if parse_units is True:
            return (
                {unit: response["units"][unit] for unit in units}
                if len(units) > 1
                else response["units"][units[0]]
            )
        return response


def get_company_facts(ticker: str, use_cache: bool = True) -> CompanyFacts:
    """Get company facts from SEC API. Data will be cached for thirty days if use_cache is True."""

    HEADERS = {
        "User-Agent": "my real company name definitelynot@fakecompany.com",
        "Accept-Encoding": "gzip, deflate",
    }

    cik = symbol_map(ticker)

    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

    r = (
        requests.get(url, headers=HEADERS, timeout=5)
        if use_cache is False
        else sec_session_facts.get(url, headers=HEADERS, timeout=5)
    )

    data = r.json() if r.status_code == 200 else {}
    taxonomies = list(data["facts"].keys())
    results = CompanyFacts()
    results.__setattr__("all_data", data)
    results.__setattr__("name", data["entityName"])
    results.__setattr__("cik", data["cik"])
    for taxonomy in taxonomies:
        results.__setattr__(
            f"facts_{taxonomy}".replace("-", "_"), list(data["facts"][taxonomy].keys())
        )

    return CompanyFacts.model_validate(results)


def get_series_id(symbol: Optional[str] = None, cik: Optional[str] = None):
    """
    This function maps the fund to the series and class IDs for validating the correct filing.
    For an exact match, use a symbol.
    """
    symbol = symbol if symbol else ""
    cik = cik if cik else ""

    results = pd.DataFrame()
    if not symbol and not cik:
        raise ValueError("Either symbol or cik must be provided.")

    target = symbol if symbol else cik
    choice = "cik" if not symbol else "symbol"
    funds = get_mf_and_etf_map(use_cache=True).astype(str)

    results = funds[
        funds["cik"].str.contains(target, case=False)
        | funds["seriesId"].str.contains(target, case=False)
        | funds["classId"].str.contains(target, case=False)
        | funds["symbol"].str.contains(target, case=False)
    ]

    if len(results) > 0:
        results = results[results[choice if not symbol else choice] == target]

        return results


def get_nport_candidates(
    symbol: Optional[str] = None,
    cik: Optional[Union[str, int]] = None,
    filing_date: Optional[str] = None,
    limit: int = 10000,
):
    """Retrieves N-Port filing candidates for a company."""

    fetcher = SecCompanyFilingsFetcher()
    query = SecCompanyFilingsQueryParams()
    if symbol:
        query.symbol = symbol
    if cik:
        query.cik = cik
    query.type = "NPORT-P"
    query.limit = limit
    results = pd.DataFrame()
    filings = pd.DataFrame(fetcher.extract_data(query, credentials={}))

    if len(filings) == 0:
        return pd.DataFrame()
    dates = filings["reportDate"].to_list()
    base_url = f"https://www.sec.gov/Archives/edgar/data/{query.cik}/"
    filings.loc[:, "xml"] = (
        base_url + filings["accessionNumber"] + "/primary_doc.xml"
    ).str.replace("-", "")
    if not filing_date:
        return filings
    if filing_date is not None:
        new_date: str = ""
        date = filing_date
        # Gets the nearest valid date to the requested one.
        __dates = pd.Series(pd.to_datetime(dates))
        __date = pd.to_datetime(date)
        __nearest = pd.DataFrame(__dates - __date)
        __nearest_date = abs(__nearest[0].astype("int64")).idxmin()
        new_date = __dates[__nearest_date].strftime("%Y-%m-%d")

        date = new_date if new_date else date

        results = filings[filings["reportDate"].astype(str).str.contains(date)]

    return results


def parse_nport(
    url: Optional[str] = None,
    data: Optional[requests.Response] = None,
):
    """
    This function parses the primary_doc.xml file for N-Port filings.
    It accepts either a url or a Requests Response object.
    """

    if not url and not data:
        raise ValueError("Either url or Requests Response Object must be provided.")

    HEADERS = {
        "User-Agent": "my real company name definitelynot@fakecompany.com",
        "Accept-Encoding": "gzip, deflate",
    }

    r = data if data else sec_session_facts.get(url, headers=HEADERS, timeout=5)
    if r.status_code != 200:
        raise RuntimeError(f"Request failed with status code {r.status_code}")
    response = xmltodict.parse(r.content)
    if (
        "edgarSubmission" in response
        and "formData" in response["edgarSubmission"]
        and response["edgarSubmission"]["headerData"]["submissionType"] == "NPORT-P"
        and "invstOrSecs" in response["edgarSubmission"]["formData"]
        and "invstOrSec" in response["edgarSubmission"]["formData"]["invstOrSecs"]
    ):
        df = pd.DataFrame.from_records(
            response["edgarSubmission"]["formData"]["invstOrSecs"]["invstOrSec"]
        )

        for i in df.index:
            if "isin" in df.iloc[i]["identifiers"]:
                isin = df.iloc[i]["identifiers"]["isin"]["@value"]
                df.loc[i, "isin"] = isin if isin else None

        results = {}
        if not df.empty:
            results.update(
                {
                    "series_info": response["edgarSubmission"]["headerData"],
                    "gen_info": response["edgarSubmission"]["formData"]["genInfo"],
                    "fund_info": response["edgarSubmission"]["formData"]["fundInfo"],
                    "form_data": df.sort_values(by="pctVal", ascending=False).to_dict(
                        "records"
                    ),
                }
            )

        return results


def validate_series_id(
    symbol: Optional[str] = None,
    cik: Optional[str] = None,
    filing_date: Optional[str] = None,
    limit: int = 10000,
):
    """
    Retrives the N-Port filing and checks the series ID to validate
    the correct filing is returned when the CIK has multiple funds associated with it.
    """

    symbol = symbol if symbol else None
    cik = cik if cik else None
    filing_date = filing_date if filing_date else None

    id = ""
    series_id = pd.DataFrame()
    candidates = get_nport_candidates(symbol, cik, filing_date, limit)
    if candidates is None or len(candidates) == 0:
        return id, candidates

    series_id = get_series_id(symbol, cik)
    if series_id is not None and not series_id.empty and len(series_id) == 1:
        id = series_id["seriesId"].iloc[0]

    return id, candidates


def get_nport_filing(
    symbol: Optional[str] = None,
    cik: Optional[str] = None,
    filing_date: Optional[str] = None,
    url: Optional[str] = None,
    limit: int = 10000,
):
    symbol = symbol.upper() if symbol else None
    cik = str(cik) if cik else None
    filing_date = filing_date if filing_date else None
    id, candidates = validate_series_id(symbol, cik, filing_date, limit)
    if len(candidates) == 0:
        return {}
    urls = candidates["xml"].to_list()

    invalid_form = 0

    data = {}
    _temp = {}
    temp = []
    if url is not None:
        urls = [url]
    if cik is not None and not id:
        data = parse_nport(url=urls[0])
        return {
            "Warning": "CIK numbers are not unique to each fund, results may not be the anticipated filing.",
            "unvalidated": data,
        }
    if symbol or cik and id:
        for url in urls:
            data = {}
            data = parse_nport(url=url) if not url else parse_nport(url=url)
            if id and data is not None:
                if (
                    data["series_info"]["filerInfo"]["seriesClassInfo"]["seriesId"]
                    == id
                ):
                    return data
                if (
                    data["series_info"]["filerInfo"]["seriesClassInfo"]["seriesId"]
                    != id
                ):
                    name = data["gen_info"]["seriesName"]
                    series = data["gen_info"]["seriesId"]
                    print(name, series)
                    temp.extend([{"name": name, "series": series}])
                    invalid_form += 1
                    print(invalid_form)

    return (
        data
        if data
        and data["series_info"]["filerInfo"]["seriesClassInfo"]["seriesId"] == id
        else {
            "Error": "No matching record found or CIK number is not unique.",
            "unvalidated_results": data,
        }
    )


def get_frame(
    year: int,
    quarter: Optional[QUARTERS] = None,
    taxonomy: TAXONOMIES = "us-gaap",
    units: str = "USD",
    fact: str = "Revenues",
    instantaneous: bool = False,
    use_cache: bool = True,
) -> Dict:
    """
    The xbrl/frames API aggregates one fact for each reporting entity
    that is last filed that most closely fits the calendrical period requested.

    This API supports for annual, quarterly and instantaneous data:

    https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json

    Where the units of measure specified in the XBRL contains a numerator and a denominator,
    these are separated by “-per-” such as “USD-per-shares”. Note that the default unit in XBRL is “pure”.

    CY####Q# for quarterly data (duration 91 days +/- 30 days).
    Because company financial calendars can start and end on any month or day and even change in length from quarter to
    quarter according to the day of the week, the frame data is assembled by the dates that best align with a calendar
    quarter or year. Data users should be mindful different reporting start and end dates for facts contained in a frame.

    Example facts:
    Revenues
    ProvisionForLoanLeaseAndOtherLosses
    Assets
    AssetsCurrent
    AssetsNoncurrent
    NoncurrentAssets
    GrossProfit
    CostOfRevenue
    CostsAndExpenses
    ResearchAndDevelopmentInProcess
    ResearchAndDevelopmentExpense
    DividendsCash
    PreferredStockDividendsAndOtherAdjustments
    DistributedEarnings
    AccountsPayableCurrent
    OperatingExpenses
    OperatingCostsAndExpenses
    OperatingIncomeLoss
    OtherOperatingIncome
    NoninterestIncome
    InterestExpense
    InterestAndDebtExpense
    IncomeTaxExpenseBenefit
    NetIncomeLoss
    NetIncomeLossAvailableToCommonStockholdersBasic
    ProfitLoss

    Facts where units are, "shares":
    WeightedAverageNumberOfSharesOutstandingBasic
    WeightedAverageNumberOfDilutedSharesOutstanding
    """

    if fact in [
        "WeightedAverageNumberOfDilutedSharesOutstanding",
        "WeightedAverageNumberOfSharesOutstandingBasic",
    ]:
        units = "shares"

    url = f"https://data.sec.gov/api/xbrl/frames/{taxonomy}/{fact}/{units}/CY{year}"

    if quarter is not None:
        url = url + f"Q{quarter}"

    if instantaneous is True:
        url = url + "I"
    url = url + ".json"
    r = (
        requests.get(url, headers=HEADERS, timeout=5)
        if use_cache is False
        else sec_session_frames.get(url, headers=HEADERS, timeout=5)
    )

    if r.status_code != 200:
        raise RuntimeError(f"Request failed with status code {r.status_code}")

    response = r.json()

    data = sorted(response["data"], key=lambda x: x["val"], reverse=True)
    metadata = {
        "frame": response["ccp"],
        "tag": response["tag"],
        "label": response["label"],
        "description": response["description"],
        "taxonomy": response["taxonomy"],
        "unit": response["uom"],
        "count": response["pts"],
    }

    results = {"metadata": metadata, "data": data}

    return results


def get_schema_filelist(year: Optional[int] = None) -> Dict:
    """Navigate the file path structure to get the standard XML and XSD schema files by year and type."""
    results = {}
    if year is None:
        year = datetime.now().year

    url = f"https://xbrl.fasb.org/us-gaap/{year}/USGAAP{year}FileList.xml"

    r = sec_session_frames.get(url, headers=HEADERS, timeout=5)

    if r.status_code != 200:
        raise RuntimeError(f"Request failed with status code {r.status_code}")

    results = xmltodict.parse(r.content)

    return results


def cik_map(cik: int) -> str:
    """
    Converts a CIK number to a ticker symbol.  Enter CIK as an integer with no leading zeros.

    Function is not meant for funds.

    Parameters
    ----------
    cik : int
        The CIK number to convert to a ticker symbol.

    Returns
    -------
    str: The ticker symbol associated with the CIK number.
    """
    _cik = str(cik)
    symbol = ""
    companies = get_all_companies().astype(str)
    if _cik in companies["cik"].to_list():
        symbol = companies[companies["cik"] == _cik]["symbol"].iloc[0]
    else:
        return f"Error: CIK, {cik}, does not have a unique ticker."

    return symbol


def parse_files(files, symbol):
    invalid_form = 0
    id = ""
    series_id = get_series_id(symbol)
    if len(series_id) == 1:
        id = series_id["seriesId"].iloc[0]
    data = {}
    _temp = {}
    temp = []

    for file in files:
        data = {}
        data = parse_nport(data=file)
        if id and data is not None:
            if data["series_info"]["filerInfo"]["seriesClassInfo"]["seriesId"] == id:
                return data
            if data["series_info"]["filerInfo"]["seriesClassInfo"]["seriesId"] != id:
                name = data["gen_info"]["seriesName"]
                series = data["gen_info"]["seriesId"]
                print(name, series)
                temp.extend([{"name": name, "series": series}])
                invalid_form += 1
                print(invalid_form)
                return temp


def get_ftd_urls() -> Dict:
    """Get Fails-to-Deliver Data URLs."""

    results = {}
    position = None
    key = "title"
    value = "Fails-to-Deliver Data"

    r = requests.get("https://www.sec.gov/data.json", timeout=5)
    if r.status_code != 200:
        raise RuntimeError(f"Request failed with status code {str(r.status_code)}")
    data = r.json()["dataset"]

    for index, d in enumerate(data):
        if key in d and d[key] == value:
            position = index
            break
    if position is not None:
        fails = data[13]["distribution"]
        key = "downloadURL"
        urls = list(map(lambda d: d[key], filter(lambda d: key in d, fails)))
        dates = [d[-11:-4] for d in urls]
        ftd_urls = pd.Series(index=dates, data=urls)
        ftd_urls.index = ftd_urls.index.str.replace("_", "")
        results = ftd_urls.to_dict()

    return results


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


def list_xbrl_company_facts(
    ticker: str,
    include_query: Optional[str] = None,
    exclude_query: Optional[str] = None,
    use_cache: bool = True,
) -> list:
    """Get company facts from SEC API."""

    data = download_company_facts(ticker, use_cache=use_cache)
    taxonomies = list(data["facts"].keys())
    facts = []
    for taxonomy in taxonomies:
        facts.extend([taxonomy + "_" + d for d in list(data["facts"][taxonomy].keys())])

    if include_query is not None:
        facts = [d for d in facts if include_query in d]

    if exclude_query is not None:
        facts = [d for d in facts if exclude_query not in d]

    return facts


from io import StringIO


def get_companies_by_sic(sic: Union[str, int] = 3674):
    """Get companies by SIC code."""
    df = pd.DataFrame()
    start = 0
    BASE_URL = (
        "https://www.sec.gov/cgi-bin/browse-edgar?company=&match=starts-with"
        + f"&filenum=&State=&Country=&SIC={sic}&myowner=include&action=getcompany"
        + f"&count=100&start={start}"
    )
    url = f"{BASE_URL}{start}"

    with requests.session() as session:
        response = session.get(url, headers=HEADERS, timeout=5)
        data = response.content.decode()
        df = pd.read_html(StringIO(data))[0]
        count = len(df)
        while count == 100:
            start += 100
            url = f"{BASE_URL}{start}"
            response = session.get(url, headers=HEADERS, timeout=5)
            data = response.content.decode()
            temp = pd.read_html(StringIO(data))[0]
            df = pd.concat([df, temp])
            count = len(temp)

        session.close()

    return df


def get_current_filings(form_type: str = "8-K"):
    """Get current filings."""
    start = 0
    BASE_URL = (
        f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type={form_type}"
        "&company=&dateb=&owner=include&count=100&output=atom&start="
    )
    url = f"{BASE_URL}{start}"
    results = []

    def parse_entries(item: Dict) -> Dict:
        """Parse entries and return as a dictionary."""
        result = {}
        date = item.get("updated", "")
        if date:
            result["date"] = date
        title = item.get("title", "")
        result["title"] = title
        cik: Union[str, None] = ""
        try:
            cik = str(title.split("(")[1].split(")")[0])
        except IndexError:
            cik = None
        if cik:
            result["cik"] = cik
        form = item.get("category", {}).get("@term", "")
        if form:
            result["form"] = form
        url = item.get("link", {}).get("@href", "")
        result["filing_url"] = url
        result["complete_submission_url"] = url.replace("-index.htm", ".txt")
        return result

    with requests.session() as session:
        response = requests.get(url, headers=SEC_HEADERS, timeout=5)
        text = response.text
        parsed = xmltodict.parse(text)
        count = 0
        entries = parsed["feed"].get("entry", [])
        count = len(entries)
        if entries:
            results.extend([parse_entries(item) for item in entries])
        while count == 100:
            start += 100
            url = f"{BASE_URL}{start}"
            response = session.get(url, headers=SEC_HEADERS, timeout=5)
            if response.status_code != 200:
                break
            text = response.text
            parsed = xmltodict.parse(text)
            entries = parsed["feed"].get("entry", [])
            if entries:
                results.extend([parse_entries(item) for item in entries])
            count = len(entries)

        session.close()

    return results


async def complete_submission_callback(response, _):
    """Use callback function for processing the response object."""
    if response.status == 200:
        return await response.text()
    raise RuntimeError(f"Request failed with status code {response.status}")


async def get_complete_submission(url: str):
    """Get the Complete Submission TXT file string from the SEC API."""
    return await amake_request(
        url, headers=HEADERS, response_callback=complete_submission_callback
    )


def parse_header(filing_str: str) -> Dict:
    """Parse the header of a Complete Submission TXT file string."""
    soup = BeautifulSoup(filing_str, "lxml-xml")
    data = soup.find_all("ACCEPTANCE-DATETIME")[0].text
    lines = data.split("\n")
    parsed_header: Dict = {}
    for line in lines:
        parts = line.split(":")
        if len(parts) == 2:
            key = parts[0].strip().replace(" ", "_").lower()
            value = parts[1].strip()
            if value and value != "''":
                parsed_header[key] = value
    return parsed_header


def get_submission_type(filing_str: str):
    """Get the submission type of a Complete Submission TXT file string."""
    header = parse_header(filing_str)
    form_type = header.get("conformed_submission_type", "")
    if not form_type:
        raise ValueError(
            "Failed to get the form type from the header."
            + " Check the response from `parse_header`."
        )
    return form_type


def get_period_ending(filing_str: str):
    """Get the report date from a Complete Submission TXT file string."""
    header = parse_header(filing_str)
    period_ending = header.get("conformed_period_of_report", "")
    if not period_ending:
        raise ValueError(
            "Failed to get the conformed period of report from the header."
            + " Check the response from `parse_header`."
        )
    return period_ending
