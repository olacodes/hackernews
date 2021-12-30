import asyncio

import aiohttp
import requests


async def fetch_hkn_item_async(news_list):
    actions, hk_news = [], []

    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        for news_id in news_list:
            url = f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json"
            actions.append(asyncio.ensure_future(get_data_async(session, url)))

        hk_news_res = await asyncio.gather(*actions)
        for data in hk_news_res:
            hk_news.append(data)
    return hk_news


async def get_data_async(session, url):
    async with session.get(url) as res:
        data = await res.json()
        return data


def get_data_sync(url):
    try:
        return requests.get(url).json()
    except Exception as err:
        print("An error occurred", err)
        return False
