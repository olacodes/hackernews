from django.contrib.postgres.fields import ArrayField
from django.core.validators import URLValidator
from django.db import models

from .news import News


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment_api_id = models.BigIntegerField(null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=200)
    by = models.CharField(max_length=255)
    time = models.BigIntegerField(null=True)
    text = models.TextField(null=True)
    parent = models.BigIntegerField(null=True)
    kids = ArrayField(base_field=models.BigIntegerField(null=True), default=list)
    url = models.TextField(validators=[URLValidator()], null=True)
    score = models.IntegerField(null=True)

    def __str__(self):
        return self.news.title
