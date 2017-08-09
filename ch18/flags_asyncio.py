import os
import time
import sys

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VH ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'

import asyncio
import aiohttp

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp: fp.write(img)

@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    img = yield from resp.read()
    return img

@asyncio.coroutine
def download_one(cc):
    img = yield from get_flag(cc)
    show(cc)
    save_flag(img, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do) # wait是一个协程，会返回一个Task
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)
