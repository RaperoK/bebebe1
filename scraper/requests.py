import requests
import json

from requests.structures import CaseInsensitiveDict

from utils import get_date


def matches_url(live_only, prematch_only):
    base_url = "https://betwatch.fr/getMoney?choice=&"
    return base_url + "&".join([
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
            f"min_percent=0",
            f"max_percent=100",
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


def get_match(id):
    headers = CaseInsensitiveDict()
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers = headers
    response = requests.get(f"https://betwatch.fr/{id}", headers=headers)
    if response.ok:
        result = response.text
        if result:
            result_json = json.loads(result)
            return result_json
    return []