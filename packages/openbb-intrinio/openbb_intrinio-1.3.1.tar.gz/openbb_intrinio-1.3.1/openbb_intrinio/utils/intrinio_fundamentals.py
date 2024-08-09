import concurrent.futures
from datetime import timedelta
from typing import Dict, List, Literal, Optional

import pandas as pd
import requests
import requests_cache

intrinio_fundamentals_session = requests_cache.CachedSession(
    "OpenBB_Intrinio_Fundamentals",
    use_cache_dir=True,
    serializer="json",
    expire_after=timedelta(days=1),
)

PERIOD_FILTERS = Literal[
    "FY",
    "Q",
    "TTM",
    "YTD",
    "Q1",
    "Q1TTM",
    "Q2",
    "Q2TTM",
    "Q2YTD",
    "Q3",
    "Q3TTM",
    "Q3YTD",
    "Q4",
]
STATEMENT_FILTERS = Literal[
    "cash_flow_statement", "income_statement", "balance_sheet_statement", "calculations"
]

api_key = "OmU1ZThiNGNkMDU0NzdiMzRkNDk0YmI3ODM2Nzk0NzM1"


def get_all_fundamentals_ids(
    symbol: str,
    api_key: str,
    period: Optional[PERIOD_FILTERS] = None,
    statement: Optional[STATEMENT_FILTERS] = None,
    use_cache: bool = True,
) -> pd.DataFrame:
    """Gets all available fundamentals IDs for a given symbol from Intrinio."""
    filings = pd.DataFrame()
    all_filings_url = f"https://api-v2.intrinio.com/companies/{symbol}/fundamentals?page_size=10000&api_key={api_key}"
    response = (
        requests.get(all_filings_url, timeout=5)
        if use_cache is False
        else intrinio_fundamentals_session.get(all_filings_url, timeout=5)
    )
    if response.status_code != 200:
        return pd.DataFrame()

    all_filings = pd.DataFrame(response.json()["fundamentals"])

    _period = "" if period is None else period
    _statement = "" if statement is None else statement

    if len(all_filings) > 0:
        filings = all_filings[
            all_filings["fiscal_period"].str.contains(_period)
            & all_filings["statement_code"].str.contains(_statement)
        ]
        if period == "Q":
            filings = filings[
                ~filings["fiscal_period"].str.contains("TTM")
                & ~filings["fiscal_period"].str.contains("YTD")
            ]

    return filings


def generate_url(id, api_key, as_reported: bool = True):
    """Generates a URL for a given ID."""
    report_type = "reported" if as_reported is True else "standardized"
    fundamentals_url = f"https://api-v2.intrinio.com/fundamentals/{id}/{report_type}_financials?api_key={api_key}"
    return fundamentals_url


def get_fundamentals(
    symbol: str,
    api_key: str,
    period: Optional[PERIOD_FILTERS] = None,
    statement: Optional[STATEMENT_FILTERS] = None,
    as_reported: bool = True,
    use_cache: bool = True,
) -> List[Dict]:
    """Gets all fundamentals for a given symbol and statement from Intrinio."""

    report_type = "reported" if as_reported is True else "standardized"
    ids = []
    urls = []
    filing_ids = get_all_fundamentals_ids(symbol, api_key, period, statement, use_cache)
    results = []
    if len(filing_ids) > 0:
        ids = filing_ids["id"].to_list()

    for id in ids:
        url = generate_url(id, api_key, as_reported)
        urls.append(url)

    def get_one(url, use_cache):
        result = {}
        response = (
            requests.get(url, timeout=5)
            if use_cache is False
            else intrinio_fundamentals_session.get(url, timeout=5)
        )
        if (
            response.status_code == 200
            and f"{report_type}_financials" in response.json()
        ):
            data = response.json()[f"{report_type}_financials"]
            metadata = response.json()["fundamental"]
            result.update(
                {
                    "date": metadata["end_date"],
                    "fiscal_year": metadata["fiscal_year"],
                    "fiscal_period": metadata["fiscal_period"],
                    "statement": metadata["statement_code"],
                    "metadata": metadata,
                    "data": data,
                }
            )
        results.append(result)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_one, urls, [use_cache] * len(urls))

    return (
        sorted(results, key=lambda x: x["date"], reverse=True) if results != [] else []
    )


def get_fundamentals_tags(
    statement: Literal[
        "income_statement",
        "balance_sheet_statement",
        "cash_flow_statement",
        "calculations",
        "current",
        None,
    ] = "balance_sheet_statement",
    template: Literal[
        "industrial",
        "financial",
        None,
    ] = None,
):
    url = "https://api-v2.intrinio.com/data_tags?"

    if statement is not None:
        url = url + f"statement_code={statement}&"
    if template is not None:
        url = url + f"template={template}&"

    url = url + "page_size=10000&api_key=" + api_key
    r = requests.get(url)
    return r.json()
