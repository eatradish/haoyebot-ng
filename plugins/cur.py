import aiohttp

async def cur(bot, msg):
	lst = msg['text'].split()[1:]
	from_tkc = lst[0]
	to_tkc = lst[1]
	amount = lst[2]
	headers = {'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja;q=0.6,zh-TW;q=0.5,uz;q=0.4,vi;q=0.3', 'Connection': 'keep-alive', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, br', 'Referer': 'http://www.cngold.org/fx/huansuan.html'}
	async with aiohttp.ClientSession(headers = headers) as session:
            async with session.get("https://api.jijinhao.com/plus/convert.htm?from_tkc=" + from_tkc + '&to_tkc=' + to_tkc + '&amount=' + amount) as resp:
                result = await resp.text()
                result = result.replace("var result = ", "")
                result = result.replace("'", "")
                await bot.sendMessage(msg['chat']['id'], result)

