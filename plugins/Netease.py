import os
import sys
import json
import time
import hashlib
import random
import base64
import binascii
import requests
from Crypto.Cipher import AES

header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'  # NOQA
        }
MODULUS = (
    "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7"
    "b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280"
    "104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932"
    "575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b"
    "3ece0462db0a22b8e7"
)
PUBKEY = "010001"
NONCE = b"0CoJUm6Qyw8W8jud"


# 歌曲加密算法, 基于https://github.com/yanunon/NeteaseCloudMusic
def encrypted_id(id):
    magic = bytearray("3go8&$8*3*3h0k(2)2", "u8")
    song_id = bytearray(id, "u8")
    magic_len = len(magic)
    for i, sid in enumerate(song_id):
        song_id[i] = sid ^ magic[i % magic_len]
    m = hashlib.md5(song_id)
    result = m.digest()
    result = base64.b64encode(result).replace(b"/", b"_").replace(b"+", b"-")
    return result.decode("utf-8")


# 登录加密算法, 基于https://github.com/stkevintan/nw_musicbox
def encrypted_request(text):
    # type: (str) -> dict
    data = json.dumps(text).encode("utf-8")
    secret = create_key(16)
    params = aes(aes(data, NONCE), secret)
    encseckey = rsa(secret, PUBKEY, MODULUS)
    return {"params": params, "encSecKey": encseckey}


def aes(text, key):
    pad = 16 - len(text) % 16
    text = text + bytearray([pad] * pad)
    encryptor = AES.new(key, 2, b"0102030405060708")
    ciphertext = encryptor.encrypt(text)
    return base64.b64encode(ciphertext)


def rsa(text, pubkey, modulus):
    text = text[::-1]
    rs = pow(int(binascii.hexlify(text), 16),
             int(pubkey, 16), int(modulus, 16))
    return format(rs, "x").zfill(256)


def create_key(size):
    return binascii.hexlify(os.urandom(size))[:16]


def songs_detail_new_api(music_ids, bit_rate=320000):
    action = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token='  # NOQA
    # self.session.cookies.load()
    #csrf = ''
    # for cookie in self.session.cookies:
    #    if cookie.name == '__csrf':
    #        csrf = cookie.value
    # if csrf == '':
    #    notify('You Need Login', 1)
    #action += csrf
    data = {'ids': music_ids, 'br': bit_rate, 'csrf_token': ""}
    r = requests.post(url=action, data=encrypted_request(data))
    result = json.loads(r.text)
    # connection = requests.post(action,
    #                           data = encrypted_request(data),
    #                           headers = header)
    #result = json.loads(connection.text)

    return result['data']


if __name__ == '__main__':
    r = songs_detail_new_api([sys.argv[1]])
    print(r)
