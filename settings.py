from pathlib import Path

from decouple import config

BASE_DIR = Path(__name__).resolve().parent
BOT_TOKEN = config("BOT_TOKEN")

BALABOO_API_URL = 1

BALABOO = {
    "api_url": "https://yandex.ru/lab/api/yalm/text3",
    "headers": {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Origin": "https://yandex.ru",
        "Referer": "https://yandex.ru/",
    },
    "payload_keys": ("query", "intro", "filter"),
}
