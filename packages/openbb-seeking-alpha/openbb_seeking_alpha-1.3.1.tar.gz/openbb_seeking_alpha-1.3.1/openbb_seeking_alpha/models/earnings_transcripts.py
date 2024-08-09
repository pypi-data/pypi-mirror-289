"""Seeking Alpha Earnings Transcripts Model."""

# pylint: disable=unused-argument

from typing import Any, Dict, List, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.earnings_call_transcript import (
    EarningsCallTranscriptData,
    EarningsCallTranscriptQueryParams,
)


class SAEarningsCallTranscriptQueryParams(EarningsCallTranscriptQueryParams):
    """Seeking Alpha Earnings Call Transcript Query.

    Source: https://seekingalpha.com/earnings/earnings-calendar
    """


class SAEarningsCallTranscriptData(EarningsCallTranscriptData):
    """Seeking Alpha Earnings Call Transcript Data."""


class SAEarningsCallTranscriptFetcher(Fetcher):
    """Seeking Alpha Earnings Call Transcript Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> SAEarningsCallTranscriptQueryParams:
        """Transform the query parameters."""
        return SAEarningsCallTranscriptQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: SAEarningsCallTranscriptQueryParams,
        credentials: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract the data."""
        base_url = (
            "https://seekingalpha.com/api/v3/articles?filter[category]=earnings::earnings-call-transcripts"
            + "&filter[since]=0&filter[until]=0"
            + "&include=author,primaryTickers,secondaryTickers&isMounting=true&page[size]=1000&page[number]=0"
        )
