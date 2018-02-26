from collections import Counter
import aiohttp
import asyncio
import async_timeout


url = 'https://make-some-noise.contest.qctf.ru/9xWkjKVCX91TzD933bMD'
# Host: browser-mining.contest.qctf.ru

# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0

# Accept: */*

# Accept-Language: en-US,en;q=0.5

# Accept-Encoding: gzip, deflate

# Referer: https://browser-mining.contest.qctf.ru/

# Content-Type: text/plain;charset=UTF-8

# Origin: https://browser-mining.contest.qctf.ru
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

flags = []

strings = ''
flag = []


async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def collect_flags():
    async with aiohttp.ClientSession() as session:
        for x in range(1000):
            html = await fetch(session, url)
            flags.append(html)
            print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(collect_flags())
    for i in range(25):
        for line in flags:
            strings += line[i]
        print(Counter(strings).most_common(10))
        flag += [word for word, cnt in Counter(strings).most_common(1)]
        strings = ''
    print(''.join(flag))

