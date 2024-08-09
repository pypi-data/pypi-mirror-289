"""Gold Reserves Standard Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class GoldReservesQueryParams(QueryParams):
    """Gold ReservesQuery."""

    start_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class GoldReservesData(Data):
    """Gold Reserves Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date"))
    troy_ounces: float = Field(
        description="Number of Troy Ounces on the date.",
        json_schema_extra={"x-unit_measurement": "troy_ounces"},
    )
