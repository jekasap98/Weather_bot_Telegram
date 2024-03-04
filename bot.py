#!/usr/bin/env python3

# import pdb
# pdb.set_trace()

import os
import logging
import sys
from os import getenv
import open_weather_api
from aiohttp import web
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ContentType, ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

TOKEN = os.environ.get('TOKEN_TELEGRAM')
weatherApiKey = os.environ.get('TOKEN_API_WEATH')

# Webserver settings
# bind localhost only to prevent any external access
WEB_SERVER_HOST = "0.0.0.0"
# Port for incoming request from reverse proxy. Should be any available port
WEB_SERVER_PORT = 8083 #Проверка джобы Версия 2 

# Path to webhook route, on which Telegram will send requests
WEBHOOK_PATH = "/webhook"
# Secret key to validate requests from Telegram (optional)
WEBHOOK_SECRET = "my-secret"
# Base URL for webhook will be used to generate webhook URL for Telegram,
# in this example it is used public DNS with HTTPS support
BASE_WEBHOOK_URL = "https://telegrambotwe.ddns.net"

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Здарова кожанный! Используй /weather для запроса погоды.")


@router.message(Command("weather")) # Добавил еще одну команду с вопросом 
async def weather(message: types.Message) -> None:
    await message.answer("В каком городе хочешь узнать погоду, кожанный?")
    

@router.message(F.content_type.in_({'text'}))
async def handle_text(message: types.Message) -> None:
    city = message.text.strip() # Берем текст (обрезаем лишнии пробелы (.strip()) из переданной объекта
    print(city) 
    answer_json = open_weather_api.getWeather(city, weatherApiKey)
    answer = f'Погода в городе {answer_json["city"]}, feels_like: {answer_json["feels_like"]}'
    await message.answer(answer)


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}")

def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    # Create aiohttp.web.Application instance
    app = web.Application()
    # Create an instance of request handler,
    # aiogram has few implementations for different cases of usage
    # In this example we use SimpleRequestHandler which is designed to handle simple cases
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
