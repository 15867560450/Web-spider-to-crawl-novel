import requests
from bs4 import BeautifulSoup
import lxml
import os
import re


def crawler():
    base_url = "https://trxs.cc"
    r = requests.get(base_url)
    r.encoding = r.apparent_encoding
    if r.status_code != 200:
        return 0
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.select('.bk')
    for info in data:
        print(info.h3.text)
        print(base_url + info.a.attrs['href'])
        print(info.p.text)
        print()
        
    
    
if __name__ == "__main__":
    crawler()
