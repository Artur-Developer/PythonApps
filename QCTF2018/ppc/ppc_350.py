
import json
import requests
# Host: browser-mining.contest.qctf.ru
# User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
# Accept: */*
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Referer: https://browser-mining.contest.qctf.ru/
# Content-Type: text/plain;charset=UTF-8
# Origin: https://browser-mining.contest.qctf.ru


def fetch(prime):

    cookies = {
        'user' : '2|1:0|10:1519592794|4:user|16:dmlwLm1hcnR5eQ==|cb4af227226f69f89c00b95f8a610d7f6b15bd2d2f87f83d2b5db3670f98d06f',
        # 'user': '2|1:0|10:1519589619|4:user|12:b3Vyb2Jvcm9z|69074677d97348e4ea910923e31e447f22264fd119814c500bb5d6a549a59f0d',
    }

    headers = {
        'Origin': 'https://browser-mining.contest.qctf.ru',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:20.0) Gecko/20121202 Firefox/20.0',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Accept': '*/*',
        'Referer': 'https://browser-mining.contest.qctf.ru/',
        'Connection': 'keep-alive',
        'DNT': '1',

    }

    data = '{"result":' + str(prime) + '}'

    response = requests.post('https://browser-mining.contest.qctf.ru/task', headers=headers, cookies=cookies, data=data)
    return response.text


def find_next_prime(n):
    return find_prime_in_range(n, 2 * n)


def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None


def main():
    # with open('primes1.txt', 'r') as f:
    #     for line in f:
    #         numbers = [int(x.replace(' ', '')) for x in f]
    # print(numbers[0:10])
    prime = 0
    while True:
        html = fetch(prime)
        print(html)
        data = json.loads(html)
        prime = find_next_prime(data['task'])
        # print(dcode)=
        print(prime)


if __name__ == '__main__':
    main()
