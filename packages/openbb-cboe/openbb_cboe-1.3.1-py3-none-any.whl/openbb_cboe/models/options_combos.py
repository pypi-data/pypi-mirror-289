"""Cboe Options Combos Model."""

# pylint: disable=invalid-name, unused-argument

from datetime import (
    date as dateType,
    datetime,
)
from typing import Any, Dict, List, Literal, Optional

from openbb_cboe.utils.helpers import (
    TICKER_EXCEPTIONS,
    get_cboe_data,
    get_company_directory,
    get_index_directory,
)
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.options_combos import (
    OptionsCombosData,
    OptionsCombosQueryParams,
)
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import amake_request
from pandas import DataFrame, Series, to_datetime
from pydantic import Field


class CboeOptionsCombosQueryParams(OptionsCombosQueryParams):
    """CBOE Options Combos Query.

    Source: https://www.cboe.com/
    """

    expiration: Optional[dateType] = Field(
        default=None,
        description="Target expiration date for the option. "
        + "If not provided, the first expiration date is used."
        + " If provided, the nearest expiration date will be matched."
        + " Format: YYYY-MM-DD",
    )
    target_price: int = Field(description="Target price for the underlying.")
    strategy: Literal["all", "spread", "naked"] = Field(
        default="spread",
    )
    use_cache: bool = Field(
        default=True,
        description="When True, the company directories will be cached for"
        + "24 hours and are used to validate symbols."
        + " The results of the function are not cached. Set as False to bypass.",
    )


class CboeOptionsCombosData(OptionsCombosData):
    """CBOE Options Combos Data."""

    last_trade_timestamp: Optional[datetime] = Field(
        description="Last trade timestamp of the option.", default=None
    )
    dte: int = Field(description="Days to expiration for the option.")


class CboeOptionsCombosFetcher(
    Fetcher[
        CboeOptionsCombosQueryParams,
        List[CboeOptionsCombosData],
    ]
):
    """Transform the query, extract and transform the data from the CBOE endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> CboeOptionsCombosQueryParams:
        """Transform the query."""
        return CboeOptionsCombosQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: CboeOptionsCombosQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Cboe endpoint"""
        results = []
        symbol = query.symbol.split(",")[0]
        INDEXES = await get_index_directory(use_cache=query.use_cache)
        await get_company_directory(use_cache=query.use_cache)
        INDEXES = INDEXES.set_index("index_symbol")
        if symbol in TICKER_EXCEPTIONS or INDEXES.index.to_list():
            symbol = "^" + symbol
        expirations_url = f"https://www.cboe.com/education/tools/trade-optimizer/symbol-info/?symbol={symbol}"
        expirations_response = await get_cboe_data(
            expirations_url, use_cache=query.use_cache
        )
        expirations = expirations_response.get("expirations")  # type: ignore

        def get_nearest_expiration(expiration: str, expirations: List[str]) -> str:
            """Gets the nearest expiration date."""

            _expirations = to_datetime(Series(expirations))
            _expiration = to_datetime(expiration)
            _nearest = DataFrame(_expirations - _expiration)
            _nearest_exp = abs(_nearest[0].astype("int64")).idxmin()
            new_expiration = expirations[_nearest_exp]
            return new_expiration

        expiration = (
            expirations[1]
            if query.expiration is None
            else get_nearest_expiration(query.expiration, expirations)
        )

        optimizer_url = f"https://www.cboe.com/education/tools/trade-optimizer/trade-optimizer-data/?symbol=SPY&targetDate={expiration}&targetPrice={query.target_price}"
        optimizer_response = await amake_request(optimizer_url)
        if optimizer_response.get("success") is True and optimizer_response.get(
            "results"
        ):
            data = (
                DataFrame(optimizer_response.get("results"))
                .replace(0, None)
                .dropna(axis=1)
            )
            results = data.to_dict(orient="records")
        return results

    @staticmethod
    def transform_data(
        query: CboeOptionsCombosQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[CboeOptionsCombosData]:
        """Transform the data to the standard format"""

        if not data:
            raise EmptyDataError()

        return [CboeOptionsCombosData.model_validate(d) for d in data]
