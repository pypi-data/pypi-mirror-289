from datetime import datetime
from typing import Literal, Optional

import requests

api_key = "OmU1ZThiNGNkMDU0NzdiMzRkNDk0YmI3ODM2Nzk0NzM1"
date = "2023-11-06"
time = "15:00"
source = "delayed"


def get_options_movers(
    metric: Optional[Literal["volume", "change"]] = None,
    source: Literal["delayed", "realtime"] = "delayed",
    date: Optional[str] = datetime.now().strftime("%Y-%m-%d"),
    time: Optional[str] = "15:00",
    api_key: str = "",
):
    base_url = "https://api-v2.intrinio.com/options/interval/movers"
    if metric == "volume":
        base_url += "/volume"
    if metric == "change":
        base_url += "/change"
    url = (
        base_url
        + f"?source={source}&open_time={date}T{time}:00.000-04:00&api_key={api_key}"
    )

    data = []
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code} - {response.text}")
    if "intervals" in response.json():
        data = response.json()["intervals"]
        open_time = response.json()["open_time"]
        close_time = response.json()["close_time"]
        [d.update({"open_time": open_time, "close_time": close_time}) for d in data]

    return data


def get_unusual_activity(
    symbol: Optional[str] = None,
    source: Literal["delayed", "realtime"] = "delayed",
    api_key: str = "",
):
    data = []
    base_url = "https://api-v2.intrinio.com/options/unusual_activity"
    url = (
        base_url + f"/{symbol}?source={source}&api_key={api_key}"
        if symbol
        else base_url + f"?source={source}&api_key={api_key}"
    )
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        raise RuntimeError(f"Error: {response.status_code} - {response.text}")
    if "trades" in response.json() and len(response.json()["trades"]) > 0:
        data = response.json()["trades"]

    return data
