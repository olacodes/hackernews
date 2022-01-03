import datetime

from django import template

register = template.Library()


@register.filter("timestamp_to_time")
def convert_timestamp_to_time(timestamp):
    import time  # noqa: F403, F401

    return datetime.date.fromtimestamp(int(timestamp))
