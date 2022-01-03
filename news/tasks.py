import requests
from asgiref.sync import async_to_sync, sync_to_async
from celery import shared_task

from .fetch import fetch_hkn_item_async, get_data_sync
from .models.comment import Comment
from .models.news import News

BASE_API_URL = "https://hacker-news.firebaseio.com/v0"


def get_item(id):
    item = requests.get(f"{BASE_API_URL}/item/{id}.json")
    return item.json()


@shared_task
def get_create_news_comments(news_id):
    single_hknews = get_item(news_id)
    news = News.objects.get(news_id=str(news_id))
    news_comments = single_hknews.get("kids", [])

    for kid in news_comments:
        comment_response = get_item(kid)
        comment, _ = Comment.objects.get_or_create(comment_api_id=kid)
        comment.news = news
        comment.comment_api_id = comment_response.get("id", "")
        comment.type = comment_response.get("type", "")
        comment.by = comment_response.get("by", "")
        comment.time = comment_response.get("time", 0)
        comment.text = comment_response.get("text", "")
        comment.url = comment_response.get("url", "")
        comment.parent = comment_response.get("parent", -1)
        comment.score = comment_response.get("score", 0)

        comment.save()


@shared_task
def sync_db(data):
    for data in data:
        news, _ = News.objects.get_or_create(news_id=data["id"])
        news.news_id = data.get("id", "")
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
        news.is_hknews = True
        news.save()
        get_create_news_comments.delay(data["id"])


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
