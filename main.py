import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
from aiogram.types import (
    BotCommand,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
    MessageEntity,
)
from aiohttp import ClientSession

import settings
from balaboo import fetch

logging.basicConfig(level=logging.INFO)

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


@dp.message_handler(commands=["balabot"])
async def cmd_one(message: types.Message, command: filters.Command.CommandObj):
    url = settings.BALABOO["api_url"]
    async with ClientSession() as session:
        text = await fetch(session, url, **extract_args(message.get_args()))
    await message.reply(text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
