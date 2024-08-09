"""Field Style Utilities."""

# %%
import locale
from typing import Callable, Dict, List, Optional, Union

import pandas as pd
from pandas.io.formats.style import Styler

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

DECIMAL_COLS = [
    "implied_volatility",
    "delta",
    "gamma",
    "vega",
    "rho",
    "theta",
    "vanna",
    "vomma",
    "charm",
    "iv",
    "iv30",
]

PERCENT_COLS = [
    "change_percent",
    "yield",
    "weight",
    "margin",
    "rate",
    "percent",
    "ytm",
    "dividend_yield",
    "yield_to_maturity",
    "return",
    "percent_change",
    "interest_rate",
    "gross_margin",
    "profit_margin",
    "ytd",
    "mtd",
    "qtd",
    "wtd",
    "one_day",
    "one_week",
    "one_month",
    "one_year",
    "three_month",
    "six_month",
    "one_year",
    "three_year",
    "five_year",
    "ten_year",
    "max",
    "change_over_time",
    "operating_margin",
    "return_on_assets",
    "return_on_equity",
    "return_on_investment",
    "effective_tax_rate",
    "tax_rate",
    "tax_expense_rate",
    "mer",
    "ter",
    "management_fee",
    "performance_fee",
    "sec_yield",
    "distribution_yield",
    "gdp_qoq",
    "gdp_yoy",
    "pe_growth",
    "ps_growth",
    "pb_growth",
    "cpi_yoy",
    "cpi_qoq",
    "industrial_production_yoy",
    "industrial_production_qoq",
    "retail_sales_yoy",
    "retail_sales_qoq",
    "core_yoy",
    "core_qoq",
    "growth",
]

CURRENCY_COLS = [
    "bid",
    "ask",
    "last_price",
    "close",
    "open",
    "high",
    "low",
    "prev_close",
    "last_price",
    "theoretical_price",
    "strike",
    "close_bid",
    "close_ask",
    "bid_high",
    "ask_high",
    "bid_low",
    "ask_low",
    "open_bid",
    "open_ask",
    "price",
    "last_price",
    "mark",
    "total_value",
    "average_price",
    "avg_price",
    "ask_at_execution",
    "bid_at_execution",
    "underlying_price_at_execution",
    "vwap",
    "adj_close",
    "year_high",
    "year_low",
    "ma_50d",
    "ma_200d",
    "eps",
    "fifty_two_week_high",
    "fifty_two_week_low",
    "target_consensus",
    "target_median",
    "last",
    "theoretical",
    "per_share",
    "book_value",
    "market_cap",
    "enterprise_value",
    "dividends",
    "dividend",
    "premium",
    "cost",
    "cash_per_share",
    "book_value_per_share",
    "nav",
    "net_asset_value",
    "net_asset_value_per_share",
    "aum",
    "assets_under_management",
    "transaction_price",
]

INT_COLS = [
    "volume",
    "unadjusted_volume",
    "adjusted_volume",
    "bid_size",
    "ask_size",
    "open_interest",
    "dte",
    "oi",
    "close_size",
    "close_bid_size",
    "close_ask_size",
    "number_of_analysts",
    "population",
    "securities_owned",
    "securities_transacted",
]

RATIO_COLS = [
    "forward_pe",
    "beta",
    "days_of_sales_outstanding",
    "days_of_inventory_outstanding",
    "days_of_payables_outstanding",
    "operating_cycle",
    "cash_conversion_cycle",
    "multiple",
    "debt_equity",
    "interest_coverage",
    "govt_debt_gdp",
    "current_account_gdp",
]

FIELD_TYPES = {
    "currency": CURRENCY_COLS,
    "int": INT_COLS,
    "percent": PERCENT_COLS,
    "decimal": DECIMAL_COLS,
    "ratio": RATIO_COLS,
}


def format_currency(x):
    if pd.isnull(x):
        return ""
    elif abs(x) >= 1e12:
        return locale.currency(x / 1e12, grouping=True) + "T"
    elif abs(x) >= 1e9:
        return locale.currency(x / 1e9, grouping=True) + "B"
    elif abs(x) >= 1e6:
        return locale.currency(x / 1e6, grouping=True) + "M"
    elif abs(x) >= 1e3:
        return locale.currency(x / 1e3, grouping=True) + "K"
    else:
        return locale.currency(x, grouping=True)


def format_int(x):
    if pd.isnull(x):
        return ""
    if abs(x) >= 1_000_000_000_000:
        return f"{x / 1_000_000_000_000:.3f}T"
    if abs(x) >= 1_000_000_000:
        return f"{x / 1_000_000_000:.3f}B"
    elif abs(x) >= 1_000_000:
        return f"{x / 1_000_000:.3f}M"
    elif abs(x) >= 10_000:
        return f"{x / 1000:.1f}K"
    else:
        return f"{x:,.0f}"


FORMATTERS = {
    "decimal": lambda x: "" if pd.isnull(x) else f"{x:.5f}",
    "percent": lambda x: (
        "" if pd.isnull(x) else f"{x:.0%}" if x * 100 % 1 == 0 else f"{x:.2%}"
    ),
    "int": lambda x: format_int(x),
    "currency": lambda x: format_currency(x),
    "ratio": lambda x: "" if pd.isnull(x) else f"{x:.3f}",
}


def get_field_type(col: str):
    """Get field type."""
    for field_type, cols in FIELD_TYPES.items():
        if col.replace(" ", "_").lower() in cols:
            return field_type
        if "ratio" in col.lower() or "_to_" in col.lower():
            return "ratio"
        if any(i in col for i in PERCENT_COLS):
            return "percent"
    return None


def apply_styler(
    df: Union[pd.DataFrame, Styler],
    field_map: Optional[Dict[str, Callable]] = None,
    keep_style: Optional[List[str]] = None,
) -> Styler:
    """Return a Pandas Styler instance."""
    format_dict: Dict = {}
    if field_map is None:
        for col in df.columns.to_list():
            field_type = None
            if col == "change" and set(
                ["open", "high", "low", "close", "change"]
            ).issubset(df.columns):
                field_type = "currency"
            else:
                field_type = get_field_type(col)
            format_dict[col] = FORMATTERS[field_type] if field_type else None
    else:
        format_dict = field_map
    return (
        df.style.format(format_dict)
        if isinstance(df, pd.DataFrame)
        else df.format(format_dict)
    )


def format_df(df: pd.DataFrame, keep_style: Optional[List[str]] = None):
    """Return a copy of the DataFrame formatted for display."""
    data = df.copy()
    for col in data.columns.to_list():
        field_type = None
        if col == "change" and set(["open", "high", "low", "close", "change"]).issubset(
            data.columns
        ):
            field_type = "currency"
        else:
            field_type = get_field_type(col)
        if field_type is not None:
            data[col] = data[col].apply(FORMATTERS[field_type])
    return data
