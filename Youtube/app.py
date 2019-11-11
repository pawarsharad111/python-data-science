import requests
from bs4 import BeautifulSoup
import json
import time
import  random

data=json.load(open("id_data.json"))

a=1

for i in data.keys():
    print(a)
    scrape_url="https://www.youtube.com"
    search_url = "/watch?v="
    search_hardcode = i
    sb_url = scrape_url + search_url + search_hardcode

    sb_get = requests.get(sb_url)
    soupeddata = BeautifulSoup(sb_get.content, "html.parser")

    title = soupeddata.find_all('h1', class_="watch-title-container")
    title = title[0].text
    title = title.rstrip()
    title = title.lstrip()
    data[i]['video_title'] = title

    cid = soupeddata.findAll('a', class_='yt-uix-sessionlink spf-link ')
    cid = cid[0]['href'].split('/')[-1]
    data[i]['channel_id'] = cid

    cid = soupeddata.findAll('a', class_='yt-uix-sessionlink spf-link ')
    cid = cid[0]['href'].split('/')[-1]
    data[i]['channel_id'] = cid

    if a % 10 == 0:
        n = random.randint(1, 20)
        time.sleep(n)
        print(f'sleep for {n}')

    a = a + 1

    print(f'Added {cid} and {title}')

