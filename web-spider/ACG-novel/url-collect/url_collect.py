import requests
from bs4 import BeautifulSoup
import lxml
import os
import re

def web_spider(url):
    base_url="https://trxs.cc"
    r=requests.get(url)
    if r.status_code != 200:
        print("ERROR:网络服务器未连接，请稍后再试！")
        return 0
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"lxml")
    data=soup.select(".book_info")[0]
    print(data.h1.text)
    
    
if __name__ == "__main__":
    web_spider("https://trxs.cc/tongren/6994.html")