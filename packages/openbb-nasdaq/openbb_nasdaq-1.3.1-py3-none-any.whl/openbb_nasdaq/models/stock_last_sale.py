import concurrent.futures
from typing import Dict, List

import pandas as pd
import requests
from random_user_agent.user_agent import UserAgent


def get_random_agent() -> str:
    user_agent_rotator = UserAgent(limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent


def get_realtime_trades(symbol: str) -> List[Dict]:
    TRADE_TIMES = [
        "09:30",
        "10:00",
        "10:30",
        "11:00",
        "11:30",
        "12:00",
        "12:30",
        "13:00",
        "13:30",
        "14:00",
        "14:30",
        "15:00",
        "15:30",
    ]

    def generate_urls(symbol: str, TRADE_TIME: str) -> str:
        return f"https://api.nasdaq.com/api/quote/{symbol}/realtime-trades?&limit=50000&fromTime={TRADE_TIME}"

    urls: List[str] = []
    for TRADE_TIME in iter(TRADE_TIMES):
        urls.append(generate_urls(symbol, TRADE_TIME))

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
        "Host": "api.nasdaq.com",
        "User-Agent": get_random_agent(),
    }
    results = []

    def get_one(url: str) -> None:
        result = []
        r = requests.get(url, headers=headers, timeout=10)
        r_json = r.json()
        last_updated = (
            r_json["data"]["message"][-1]
            if "last updated" in r_json["data"]["message"][-1]
            else r_json["data"]["message"][0]
        ).replace("Data last updated ", "")
        # last_updated =  parse(last_updated, tzinfos={"ET": "UTC-4"}).strftime("%Y-%m-%d %H:%M:%S%z")
        if "data" in r_json and "rows" in r_json["data"]:
            result = r_json["data"]["rows"]
            for d in result:
                d["last_updated"] = last_updated

        results.extend(result)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_one, urls)

    output = []
    try:
        data = pd.DataFrame.from_records(results)
        data["nlsTime"] = pd.DatetimeIndex(data["nlsTime"])
        data["nlsTime"] = data["nlsTime"].dt.strftime("%H:%M:%S")
        data["nlsPrice"] = (
            data["nlsPrice"].astype(str).str.replace("$ ", "").astype(float)
        )
        data["nlsShareVolume"] = (
            data["nlsShareVolume"].str.replace(",", "").astype("int64")
        )
        output = (
            data.set_index("nlsTime")
            .sort_index()
            .reset_index()
            .to_dict(orient="records")
        )
        return output
    except KeyError:
        return output
