"""Nasdaq Corporate Actions News Model."""

# pylint: disable=unused-argument
from typing import Any, Dict, List, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.rss_news import (
    RssNewsData,
    RssNewsQueryParams,
)
from openbb_core.provider.utils.helpers import make_request


class NasdaqCorporateActionsNewsQueryParams(RssNewsQueryParams):
    """
    Nasdaq Corporate Actions News Query Params.

    source: https://nasdaqtrader.com
    """


class NasdaqCorporateActionsNewsData(RssNewsData):
    """Nasdaq Corporate Actions News Data."""

    __alias_dict__ = {
        "url": "link",
        "date": "pubDate",
    }


class NasdaqCorporateActionsNewsFetcher(
    Fetcher[NasdaqCorporateActionsNewsQueryParams, NasdaqCorporateActionsNewsData]
):
    """Nasdaq Corporate Actions News Fetcher."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> NasdaqCorporateActionsNewsQueryParams:
        """Transform the query params."""
        return NasdaqCorporateActionsNewsQueryParams(**params)

    @staticmethod
    def extract_data(
        query: NasdaqCorporateActionsNewsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract the raw data."""

        url = "https://nasdaqtrader.com/Rss.aspx?feed=archiveheadlines&categorylist=105"
        make_request(url)
