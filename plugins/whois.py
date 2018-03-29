import os

async def whois(bot, msg):
    print('GET /whois')
    text = msg['text'].split()[-1]
    await bot.sendMessage(os.popen("whois " + text).read())
