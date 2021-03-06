# Generated by Django 3.2.10 on 2022-01-01 13:46

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_story_id_news_news_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment_api_id', models.BigIntegerField(null=True)),
                ('type', models.CharField(max_length=200)),
                ('by', models.CharField(max_length=255)),
                ('time', models.BigIntegerField(null=True)),
                ('text', models.TextField(null=True)),
                ('parent', models.BigIntegerField()),
                ('kids', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(null=True), default=list, size=None)),
                ('url', models.TextField(null=True, validators=[django.core.validators.URLValidator()])),
                ('score', models.IntegerField(null=True)),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.news')),
            ],
        ),
    ]
