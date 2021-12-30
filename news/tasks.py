from asgiref.sync import async_to_sync, sync_to_async
from celery import shared_task

from .fetch import fetch_hkn_item_async, get_data_sync
from .models.news import News


@shared_task
def sync_db(data):
    for data in data:
        news, _ = News.objects.get_or_create(story_id=data["id"])
        news.story_id = data.get("id", "")
        news.type = data.get("type", "")
        news.by = data.get("by", "")
        news.time = data.get("time", 0)
        news.url = data.get("url", "")
        news.score = data.get("score", 0)
        news.descendants = data.get("descendants", 0)
        news.parent = data.get("parent", -1)
        news.poll = data.get("poll", 0)
        news.kids = data.get("kids", [])
        news.text = data.get("text", "")
        news.part = data.get("part", [])
        news.title = data.get("title", "")
        news.save()


@sync_to_async
def sync_to_async_db():
    return list(News.objects.all())


async def sync_hknews():
    news_list = get_data_sync("https://hacker-news.firebaseio.com/v0/newstories.json")
    hk_news = await fetch_hkn_item_async(news_list)
    sync_db.delay(hk_news)
    return hk_news


@shared_task
def sync_hknews_sync():
    async_to_sync(sync_hknews)()
