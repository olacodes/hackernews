import datetime
from datetime import timezone

from django.contrib.postgres.fields import ArrayField
from django.core.validators import URLValidator
from django.db import models

dt = datetime.datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    news_id = models.BigIntegerField(null=True)
    type = models.CharField(max_length=200)
    by = models.CharField(max_length=255)
    deleted = models.BooleanField(blank=True, null=True, default=False)
    time = models.BigIntegerField(null=True, default=utc_timestamp)
    text = models.TextField(null=True)
    dead = models.BooleanField(default=False)
    parent = models.BigIntegerField(null=True)
    poll = models.BigIntegerField(null=True)
    kids = ArrayField(base_field=models.BigIntegerField(null=True), default=list)
    url = models.TextField(validators=[URLValidator()], null=True)
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    part = ArrayField(
        base_field=models.BigIntegerField(blank=True, null=True), default=list
    )
    descendants = models.BigIntegerField(null=True)
    is_hknews = models.BooleanField(default=False)

    class Meta:
        ordering = ("-time",)
