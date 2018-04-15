import json
from pprint import pprint
import aiohttp
import random
import urllib.parse

async def pixiv(bot, msg):
	url = 'https://public-api.secure.pixiv.net/v1/ranking/all?image_sizes=px_128x128%2Cpx_480mw%2Clarge&include_stats=true&page=1&profile_image_sizes=px_170x170%2Cpx_50x50&mode=daily&include_sanity_level=true&per_page=50'
	headers = {"Host": "public-api.secure.pixiv.net", "Authorization": "Bearer WHDWCGnwWA2C8PRfQSdXJxjXp0G6ULRaRkkd6t5B6h8", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Accept-Language": "zh-cn", "Connection": "keep-alive", "Proxy-ConnectAion": "keep-alive", "User-Agent": "PixivIOSApp/5.6.0", "Referer": "http://spapi.pixiv.net/"}

	async with aiohttp.ClientSession(headers = headers) as session:
		async with session.get(url = url) as resp:
			jResp = json.loads(await resp.text())
			num = random.randint(0,49)
			photo_url = jResp['response'][0]['works'][num]['work']['image_urls']['large']
			pixiv_url = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id={}'.format(urllib.parse.urlsplit(photo_url).path.split('/')[-1].replace('_p0.jpg', '').replace('_p0.png', ''))
			await bot.sendPhoto(msg['chat']['id'], photo_url, caption = pixiv_url)
