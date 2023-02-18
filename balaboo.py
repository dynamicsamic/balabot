import asyncio
import json
import logging
from typing import Any

logger = logging.getLogger(__name__)

from aiohttp import ClientSession

url = "https://yandex.ru/lab/api/yalm/text3"
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Origin": "https://yandex.ru",
    "Referer": "https://yandex.ru/",
}

rq_body = {"query": "Отдых в Ялте", "intro": 24, "filter": 1}

"""
текст - intro 0
песня - {query: "любимая заинька", intro: 37, filter: 1}
инструкция - {query: "как вытереть стакан", intro: 24, filter: 1}
рецепт - 25
народная мудрость - 11
короткие истории - 6
вики - 8
фильмы - 9
предсказания - 10
"""


def get_style(style: str = "текст"):
    styles = {
        "текст": 0,
        "песня": 37,
        "инструкция": 24,
        "рецепт": 25,
        "народная мудрость": 11,
        "короткие истории": 6,
        "вики": 8,
        "фильмы": 9,
        "предсказания": 10,
    }
    return styles.get(style, 0)


def build_req_body(query: str, style: str) -> dict[str, Any]:
    return {"query": query, "intro": get_style(style), "filter": 1}


async def fetch(session: ClientSession, url: str, query: str, style: str):
    req_body = build_req_body(query, style)
    async with session.post(url, json=req_body, headers=headers) as resp:
        res = await resp.json()
        logger.info(res)
        return res.get("text")
        # b = await resp.text()
        # print(json.loads(b.read().decode("utf8")))


if __name__ == "__main__":
    asyncio.run(fetch(url, "моя любимая Натали", "песня"))
