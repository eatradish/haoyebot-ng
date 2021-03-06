# Fork on https://github.com/zhangyubaka/Fezabot-NG

from pprint import pprint
import json
import aiohttp


async def autocomCode(postid: str) -> str:
    url = 'https://www.kuaidi100.com/autonumber/autoComNum'
    # Set header for POST request.
    headers = {
        'Pragma': 'no-cache',
        'Origin': 'https://www.kuaidi100.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.kuaidi100.com/',
        'Content-Length': '0',
        'DNT': '1',
    }
    # The parameters for request.
    params = (('resultv2', '1'), ('text', postid))

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url=url, params=params) as resp:
            # A dirty hack for JSON serialize. Bypass 'Type mismatch'.
            jResp = json.loads(await resp.text())
            return jResp['auto'][0]['comCode']


async def query(ptype: str, postid: str) -> str:
    url = 'https://www.kuaidi100.com/query'
    headers = {
        'Pragma': 'no-cache',
        'DNT': '1',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.kuaidi100.com/',
    }
    # Set parameters
    params = (
        ('type', ptype),
        ('postid', postid),
    )

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=url, params=params) as resp:
            # Another dirty hack as usual.
            jResp = json.loads(await resp.text())
            lst = []
            for i in jResp['data']:
                lst.append('%s %s' % (i['time'], i['context']))
            s = "\n".join(lst)
            return s


async def kuaidi(bot, msg):
    postid = msg['text'].split()[-1]
    await bot.sendMessage(msg['chat']['id'], await query(await autocomCode(postid), postid))
