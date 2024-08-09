from openbb_core.provider.utils.helpers import amake_request
from openbb_nasdaq.utils.helpers import IPO_HEADERS

symbol = "PLTR"

DRILL_DOWN_URL = f"https://api.nasdaq.com/api/quote/{symbol.lower()}/option-chain?assetclass=stocks&recordID={symbol.upper()}--240202c00014500"


INDEX_CHAINS = f"https://api.nasdaq.com/api/quote/{symbol.upper()}/option-chain?assetclass=index&limit=15000&fromdate=all&todate=undefined&excode=oprac&callput=callput&money=all&type=all"


async def get_chains_data(symbol: str):
    """Get the options chains data."""

    asset_classes = ["stocks", "etf", "index"]
    chains_data = {}
    for asset_class in asset_classes:
        CHAINS_URL = (
            f"https://api.nasdaq.com/api/quote/{symbol.upper()}/"
            f"option-chain?assetclass={asset_class}&limit=15000&fromdate=all&todate=undefined"
            "&excode=oprac&callput=callput&money=all&type=all"
        )
        print(CHAINS_URL)
        chains_data = await amake_request(CHAINS_URL, timeout=20, headers=IPO_HEADERS)
        if chains_data.get("data"):
            break

    if not chains_data:
        raise RuntimeError(
            f"Error with the Nasdaq request, no data was returned for {symbol}."
        )
    return chains_data
