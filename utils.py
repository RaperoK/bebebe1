from datetime import datetime
import pytz

def get_date():
    return datetime.utcnow().replace(tzinfo=pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d')

def get_time(iso8601):
    date_time = datetime.strptime(iso8601, "%Y-%m-%dT%H:%M:%S%z")
    return date_time.time().strftime("%H:%M")

def percent(list):
    result = []
    for item in list:
        result.append(round(item / sum(list) * 100))
    return result