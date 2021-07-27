import requests
import json

import const
from utils import get_date


def matches_url(goals, live_only, prematch_only, min_percent, max_percent):
    base_url = "https://betwatch.fr/getMoney?choice="
    return base_url + "&".join([
            f"{f'First%20Half%20Goals%20{goals}' if goals != const.FIRST_HALF['none'] else ''}",
            f"date={get_date()}",
            f"live_only={live_only}",
            f"prematch_only={prematch_only}",
            "not_countries=",
            "not_leagues=",
            "settings_order=score",
            "country=",
            "league=",
            f"min_vol=0",
            f"max_vol=103",
            f"min_percent={min_percent}",
            f"max_percent={max_percent}",
            f"min_odd=0",
            f"max_odd=349",
            "filtering=true",
            "utc=5"])

def scores_url(id_list):
    return f"https://betwatch.fr/live?live={','.join(id_list)}"


def get(url):
    response = requests.get(url)
    if response.ok:
        result = response.text
        if result:
            result_json = json.loads(result)
            return result_json
    return []
