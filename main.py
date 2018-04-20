#!/usr/bin/python3

__author__  = 'sakiiily'
import asyncio
from aiohttp import web
import telepot
import telepot.aio
import re
import random
from telepot.aio.loop import OrderedWebhook
from pprint import pprint
from plugins.whois import whois
from plugins.bmi import bmi
from plugins.decided import decided
from plugins.kuaidi import kuaidi
from plugins.pixiv import pixiv
from plugins.cur import cur
from plugins.wikipedia_summary import wikipedia_summary
from plugins.miaow import miaow
#from plugins.datab import datab
from config import TOKEN, URL, PORT


async def feeder(request):
    data = await request.text()
    webhook.feed(data)
    return web.Response(body = 'OK'.encode('UTF-8'))

async def init(app, bot): # Copy/Pasting code from telepot examples
    app.router.add_route('GET', '/webhook', feeder)
    app.router.add_route('POST', '/webhook', feeder)

    await bot.setWebhook(URL)

async def handler(msg):
    pprint(telepot.flance(msg,long=True)) #logging info.
    try:
        if msg['text'].startswith('/bmi'):
            await bmi(bot, msg)
        elif msg['text'].startswith('/whois'):
            await whois(bot, msg)
        elif msg['text'].startswith('/kuaidi'):
            await kuaidi(bot, msg)
        elif msg['text'].startswith('/pixiv'):
            await pixiv(bot, msg)
        elif msg['text'].startswith('/cur'):
            await cur(bot, msg)
        elif msg['text'].startswith('/wikipedia_summary'):
            await wikipedia(bot, msg)
        elif msg['text'].startswith('/start'):
            await bot.sendMessage(msg['chat']['id'], "Hi, I'm haoYe-ng bot")
        elif msg['text'].startswith('/decided'):
            await decided(bot, msg)
        else:
            pass
        if re.search(r'[qpbd]+[wau]+[qpbd]', msg['text']) != None:
            await miaow(bot, msg)
        if random.randint(0,10) in [1,2]:
            await bot.sendMessage(msg['chat']['id'], msg['text'])
    except KeyError as e:
        pprint(e)

loop = asyncio.get_event_loop() # Get eventloop

app = web.Application(loop=loop)
bot = telepot.aio.Bot(TOKEN, loop=loop)
webhook = OrderedWebhook(bot, {'chat': handler}) # Create Webhook here.

loop.run_until_complete(init(app, bot))

loop.create_task(webhook.run_forever())

web.run_app(app, port=PORT)
