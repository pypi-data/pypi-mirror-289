HK = "https://www.hkgb.gov.hk/en/others/documents/DailyClosings.xls"
HK_HISTORICAL_DAILY = "https://www.hkgb.gov.hk/en/others/documents/T090403.xls"


def duration_sorter(durations: list) -> list:
    """Sort durations labeled as month_5, year_5, etc."""

    def duration_to_months(duration):
        """Convert duration to months."""
        if duration == "long_term":
            return 360
        parts = duration.split("_")
        months = 0
        for i in range(0, len(parts), 2):
            number = int(parts[i + 1])
            if parts[i] == "year":
                number *= 12  # Convert years to months
            months += number
        return months

    return sorted(durations, key=duration_to_months)


JPN_OTC_BOND_PRICES = "https://market.jsda.or.jp/en/statistics/bonds/prices/otc/files/csvheaderotc_eigo.xlsx"

JPN_OTC_BOND_PRICES_FIELDS = [
    "date",
    "issue_type",
    "code",
    "issues",
    "due_date",
    "coupon_rate",
    "avg_compound_yield",
    "avg_price",
    "change_price",
    "interest_payment_,month",
    "interest_payment_day",
    "information",
    "information_2",
    "information_3",
    "a",
]


async def get_bond_reference_dates_by_year(year: int) -> list:
    """List of dates for reference statistical prices [yields] for OTC bond transactions/rating matrix."""
    from datetime import datetime  # noqa
    from io import StringIO
    from pandas import read_html, to_datetime
    from openbb_core.provider.utils.helpers import amake_requests

    if year < 2002:
        raise ValueError("Year must be => 2002.")

    urls = [
        f"https://market.jsda.or.jp/en/statistics/bonds/prices/otc/archive{year}.html"
    ]
    if year == datetime.today().year:
        urls.append(
            "https://market.jsda.or.jp/en/statistics/bonds/prices/otc/index.html"
        )

    dates = []

    async def response_callback(response, _):
        """Callback to process response."""
        string = await response.text()
        df = read_html(StringIO(string), header=1)[0]
        _dates = to_datetime(df.Date).dt.strftime("%Y-%m-%d").tolist()
        dates.extend(_dates)

    await amake_requests(urls, response_callback=response_callback)  # type: ignore

    return dates


def get_corporate_bond_prices_yen(date: str):
    """Get Japanese OTC bond prices."""
    from datetime import datetime  # noqa
    from io import StringIO
    from numpy import nan
    from pandas import read_csv, to_datetime
    from openbb_core.provider.utils.helpers import make_request

    _date = datetime.strptime(date, "%Y-%m-%d").strftime("%y%m%d")
    year = datetime.strptime(date, "%Y-%m-%d").year

    # url = f"https://market.jsda.or.jp/en/statistics/bonds/prices/otc/files/{year}/ES{_date}.csv"
    url = f"https://www.jsda.or.jp/en/statistics/bonds/bond_trade/files/ETORIHIKI{year}.csv"
    cols = [
        "Date",
        "Issue Type",
        "Code",
        "Issues",
        "Due Date",
        "Coupon Rate",
        "Average Compound Yield",
        "Average Price(Yen)",
        "Change (Yen)",
        "Interest Payment Months",
        "Interest Payment Day",
        "Information",
        "Information2",
        "Information3",
        "Average Simple Yield",
        "High Price",
        "High Simple Yield",
        "Low Price",
        "Low Simple Yield",
        "Check Flag",
        "Number of Reporting Members",
        "Highest Compound Yield",
        "Highest Price Change (Yen)",
        "Lowest Compound Yield",
        "Lowest Price Change (Yen)",
        "Median Compound Yield",
        "Median Simple Yield",
        "Median Price (Yen)",
        "Median Price Change (Yen)",
    ]
    columns = [
        "Release Date",
        "Trade Date",
        "Code",
        "Issues",
        "Due Date",
        "Coupon Rate",
        "Buy/Sell Indicator",
        "Face Value Traded Over 500 Million Yen",
        "Face Value Traded Under 500 Million Yen",
        "Traded Price",
        "Reference Statistical Price",
    ]
    response = make_request(url)
    df = read_csv(
        StringIO(response.text),
        names=columns,
        dtype={
            "Code": str,
            "Coupon Rate": float,
            "Traded Price": float,
            "Reference Statistical Price": float,
        },
    )

    for col in ["Release Date", "Trade Date", "Due Date"]:
        df[col] = to_datetime(df[col], format="%Y%m%d").dt.strftime("%Y-%m-%d")

    # issues_by_type = df.groupby("Issue Type")["Issues"].apply(lambda x: x.unique().tolist()).to_dict()

    # issuers = list(set([d.split(" ")[0] for d in df.Issues.unique().tolist() if not d.startswith("JGB") or not d.startswith("T-BILL")]))
    df["Face Value Traded Over 500 Million Yen"] = (
        df["Face Value Traded Over 500 Million Yen"]
        .str.replace("*", "Y")
        .replace({nan: "N"})
    )
    df["Face Value Traded Under 500 Million Yen"] = (
        df["Face Value Traded Under 500 Million Yen"]
        .str.replace("*", "Y")
        .replace({nan: "N"})
    )
    df = df.drop(columns=["Face Value Traded Under 500 Million Yen"])
    return df
