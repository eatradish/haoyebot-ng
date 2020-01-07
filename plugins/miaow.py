async def miaow(bot, msg):
    dic = {'q': 'p', 'p': 'q', 'd': 'b', 'b': 'd'}
    run = ['a', 'w', 'u']
    lst = list(msg['text'])
    for i in range(len(lst)):
        if dic.get(lst[i]):
            lst[i] = dic[lst[i]]
        lst = list(filter(lambda x: x in dic.keys() or x in run, lst))
        while lst[0] in run:
            lst = lst[1:]
        while lst[-1] in run:
            lst = lst[:-1]
    await bot.sendMessage(msg['chat']['id'], "".join(lst))
