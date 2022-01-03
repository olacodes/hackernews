import datetime
from datetime import timezone

from rest_framework import serializers

from news.models.news import News

dt = datetime.datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = (
            "dead",
            "deleted",
            "parent",
            "poll",
            "part",
            "descendants",
            "kids",
            "news_id",
            "is_hknews",
            "time",
        )
