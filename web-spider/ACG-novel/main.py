import requests
from bs4 import BeautifulSoup
import lxml
import re
import os


def crawler(view_url):  # 获取搜索页面的json格式
    base_url = "https://trxs.cc"
    book_list = []
    r = requests.get(view_url)
    r.encoding = r.apparent_encoding
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.select('.bk')
    for info in data:
        result = {
            'title': info.h3.text,
            'locate_url': base_url + info.a.attrs['href'],
            'summary': info.p.text
        }
        book_list.append(result)
    return book_list


def crawler_content(content_url):
    return None


def crawler_page(page_url):
    r = requests.get(page_url)
    r.encoding = r.apparent_encoding
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.select('.read_chapterDetail')
    page = {
        'title': soup.h1.text,
        'text': data[0].text
    }
    return page


if __name__ == '__main__':
    page = crawler_page('https://trxs.cc/tongren/6994/1.html')
    with open("test.txt", "w") as fp:
        fp.write(page['title'])
        fp.write(page['text'])
