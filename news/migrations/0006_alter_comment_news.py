# Generated by Django 3.2.10 on 2022-01-03 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.news'),
        ),
    ]
