from time import time
from datetime import datetime, UTC, timedelta
# from warnings import deprecated


def rni():
    """ms since epoch. js equiv"""
    return int(time() * 1000)


def rn(tz=UTC):
    """Aware datetime defaulting to UTC"""
    return datetime.now(tz)


def age(dt: datetime):
    return datetime.now(dt.tzinfo) - dt


def stale(dt: datetime | None, max_age: timedelta):
    if not dt:
        return True
    return age(dt) > max_age
