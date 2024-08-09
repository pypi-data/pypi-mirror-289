"""Charting Extension Query Params."""

from typing import List, Optional, Union

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field


def _get_type_name(t):
    """Get the type name of a type hint."""
    if hasattr(t, "__origin__"):
        return f"{t.__origin__.__name__}[{', '.join([_get_type_name(arg) for arg in t.__args__])}]"
    else:
        return t.__name__


class ChartQueryParams(QueryParams):
    """Chart Query Parmams Base Model."""

    def __init__(self, **data):
        super().__init__(**data)
        self.__doc__ = self.__repr__()

    def __repr__(self):
        fields = self.__class__.model_fields
        repr_str = (
            "\n"
            + self.__class__.__name__
            + "\n\n"
            + "    Parameters\n"
            + "    ----------\n"
            + "\n".join(
                [
                    f"\n    {k} ({_get_type_name(v.annotation)}):\n        {v.description}".replace(
                        ". ", ".\n        "
                    )
                    for k, v in fields.items()
                ]
            )
        )
        return repr_str

    data: Optional[Union[Data, List[Data]]] = Field(
        default=None,
        description="Filtered versions of the data contained in the original `self.results`."
        + " Columns should be the same as the original data."
        + " Example use is to reduce the number of columns, or the length of data, to plot.",
    )


class FredSeriesChartQueryParams(ChartQueryParams):
    """FRED Series Chart Query Params."""

    title: Optional[str] = Field(
        default=None,
        description="Title of the chart.",
    )
    y1title: Optional[str] = Field(
        default=None,
        description="Right Y-axis title.",
    )
    y2title: Optional[str] = Field(
        default=None,
        description="Left Y-axis title.",
    )
    xtitle: Optional[str] = Field(
        default=None,
        description="X-axis title.",
    )
    dropnan: bool = Field(
        default=True,
        description="If True, rows containing NaN will be dropped.",
    )
    normalize: bool = Field(
        default=False,
        description="If True, the data will be normalized and placed on the same axis.",
    )
    allow_unsafe: bool = Field(
        default=False,
        description="If True, the method will attempt to pass all supplied data to the chart constructor."
        + " This can result in unexpected behavior.",
    )


class TechnicalConesChartQueryParams(ChartQueryParams):
    """Technical Cones Chart Query Params."""

    title: Optional[str] = Field(
        default=None,
        description="Title of the chart.",
    )
    symbol: Optional[str] = Field(
        default=None,
        description="Symbol represented by the data. Used to label the chart.",
    )
