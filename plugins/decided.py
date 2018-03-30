import random

async def decided(bot, msg):
    lst = msg['text'].split()
    lst = lst[1:]
    text = ''
    if len(list(set(lst))) == 1:
        text = '不' + lst[0]
    else:
        text = lst[random.randint(0, len(lst) - 1)]
    await bot.sendMessage(msg['chat']['id'], text)


