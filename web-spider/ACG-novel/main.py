import requests
from bs4 import BeautifulSoup
import lxml
import os
import re

def crawler():
    url = "https://trxs.cc"
    r = requests.get(url)
    r.encoding = r.apparent_coding
    if r.status_code != 200:
        return 0
    soup = BeautifulSoup(r.text,'lxml')
    data = soup.select('.bk')
    print(data)
