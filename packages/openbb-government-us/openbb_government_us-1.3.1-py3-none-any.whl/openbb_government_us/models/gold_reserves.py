"""Government US Gold Reserve Model."""

# pylint: disable=unused-argument

from typing import Any, Dict, List, Optional

from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.gold_reserves import (
    GoldReservesData,
    GoldReservesQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field


class GovernmentUSGoldReservesQueryParams(GoldReservesQueryParams):
    """US Government Gold Reserves Query.

    Data is updated monthly, and is available beginning 2012.

    Source: https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/u-s-treasury-owned-gold
    """


class GovernmentUSGoldReservesData(GoldReservesData):
    """US Government Gold Reserves Data."""

    __alias_dict__ = {
        "date": "record_date",
        "troy_ounces": "fine_troy_ounce_qty",
        "book_value": "book_value_amt",
        "facility": "facility_desc",
        "location": "location_desc",
        "form": "form_desc",
        "line": "src_line_nbr",
        "fiscal_year": "record_fiscal_year",
        "fiscal_quarter": "record_fiscal_quarter",
        "calendar_quarter": "record_calendar_quarter",
    }
    form: str = Field(
        description="Form in which the gold reserve is held.",
    )
    facility: str = Field(
        description="Type of facility housing gold reserve.",
    )
    location: str = Field(
        description="Location of the gold reserve.",
    )
    book_value: float = Field(
        description="The book value is not the market value, but instead represents the total number"
        + " of troy ounces multiplied by a value established by law ($42.222), set in 1973.",
        json_schema_extra={"x-unit_measurement": "currency"},
    )
    line: int = Field(
        description="Indicates the row of the corresponding table where a data point can be found."
        + " This can assist in structuring the data in a similar format to the published report"
        + " and in understanding potential hierarchies within the table.",
    )
    fiscal_year: int = Field(
        description="The fiscal year associated with record_date."
        + " The federal government's fiscal year runs from Oct. 1 to Sept. 30.",
    )
    fiscal_quarter: int = Field(
        description="	The fiscal quarter associated with record_date."
        + " For the federal government these quarters are:"
        + "\n    Q1 - Oct. to Dec."
        + "\n    Q2 - Jan. to Mar."
        + "\n    Q3 - Apr.to Jun."
        + "\n    Q4 - Jul. to Sept.",
    )
    calendar_quarter: int = Field(
        description="The calendar quarter associated with record_date."
    )


class GovernmentUSGoldReservesFetcher(
    Fetcher[
        GovernmentUSGoldReservesQueryParams,
        List[GovernmentUSGoldReservesData],
    ]
):
    """US Government Gold Reserves Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> GovernmentUSGoldReservesQueryParams:
        """Transform query params."""
        return GovernmentUSGoldReservesQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: GovernmentUSGoldReservesQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract the raw data from Treasury Fiscal Data API."""
        # pylint: disable=import-outside-toplevel
        from openbb_core.provider.utils.helpers import amake_request

        start_date = query.start_date if query.start_date else ""
        end_date = query.end_date if query.end_date else ""
        dates = ""

        if start_date:
            dates = f"record_date:gte:{start_date}"
            if end_date:
                dates = f"{dates},lte:{end_date}"

        if not start_date and end_date:
            dates = f"record_date:lte:{end_date}"

        if dates:
            dates = f"filter={dates}&"

        data: List = []
        url = (
            "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/gold_reserve?"
            + f"{dates}page[size]=10000&format=json"
        )
        try:
            print(url)
            response = await amake_request(url)
            data = response.get("data", [{}])  # type: ignore
        except Exception as e:
            raise OpenBBError(f"{e}")

        if not data:
            raise EmptyDataError("The data was returned empty.")

        return data

    @staticmethod
    def transform_data(
        data: List[Dict],
        query: GovernmentUSGoldReservesQueryParams,
        **kwargs: Any,
    ) -> List[GovernmentUSGoldReservesData]:
        """Transform the raw data."""
        return [
            GovernmentUSGoldReservesData.model_validate(d)
            for d in data
            if d
            not in [
                "record_calendar_year",
                "record_calendar_month",
                "record_calendar_day",
            ]
        ]
