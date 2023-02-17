import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from aiogram.types.message import Message

import settings
from balaboo import fetch

logging.basicConfig(level=logging.DEBUG)

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher(bot)


def extract_args(query_string: str = "") -> dict[str, str]:
    default_style = "текст"
    default_query = "придумай что-нибудь"
    if not query_string:
        return {"style": default_style, "query": default_query}
    args = query_string.split()
    if len(args) == 1:
        return {"style": default_style, "query": args[0]}
    style, *query = args
    return {"style": style, "query": " ".join(query)}


# @dp.inline_handler()
# async def inline_echo(query: InlineQuery):
#    # query, = extract_args(query.query)
#    url = settings.BALABOO["api_url"]
#    text = await fetch(url, **extract_args(query.query))
#    content = InputTextMessageContent(text)
#    msg = InlineQueryResultArticle(
#        id=1, title="some title", input_message_content=content
#    )
#    #    await query.answer(results=[msg], cache_time=1)
#    await bot.answer_inline_query(query.id, results=[msg], cache_time=1)


@dp.message_handler()
async def foo(message: Message):
    print(message.entities)
    print(message.entities)
    await message.answer("hi")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
