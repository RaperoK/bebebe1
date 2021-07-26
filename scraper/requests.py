import requests
import json

from filters import live_only, prematch_only, min_vol, max_vol, min_percent, max_percent, min_odd, max_odd
from utils import get_date


def matches_url(filters):
    base_url = "https://betwatch.fr/getMoney?choice=&"
    return base_url + "&".join([
            f"date={get_date()}",
            f"live_only={filters.live_only}",
            f"prematch_only={filters.prematch_only}",
            "not_countries=",
            "not_leagues=",
            "settings_order=score",
            "country=",
            "league=",
            f"min_vol={filters.min_vol}",
            f"max_vol={filters.max_vol}",
            f"min_vol={filters.min_vol}",
            f"max_vol={filters.max_vol}",
            f"min_percent={filters.min_percent}",
            f"max_percent={filters.max_percent}",
            f"min_odd={filters.min_odd}",
            f"max_odd={filters.max_odd}",
            "filtering=true",
            "utc=5"]).replace("False", "false").replace("True", "true")

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