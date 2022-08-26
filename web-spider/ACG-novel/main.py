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
            'content_url': base_url + info.a.attrs['href'],
            'summary': info.p.text
        }
        book_list.append(result)
    return book_list


def crawler_content(content_url):
    base_url = "https://trxs.cc"
    url_list = []
    r = requests.get(content_url)
    r.encoding = r.apparent_encoding
    if r.status_code != 200:
        return None
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.select('ul.clearfix')[0]
    demo = soup.find_all('li')
    for i in demo:
        url_list.append(base_url + i.a.attrs['href'])
    for i in range(4):
        url_list.pop(0)
    content = {
        'title': soup.h1.text,
        'image': base_url + soup.img.attrs['src'],
        'summary': soup.p.text,
        'url': url_list
    }
    return content


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
    content = crawler_content('https://trxs.cc/tongren/6994.html')
    for page_url in content['url']:
        page = crawler_page(page_url=page_url)
        with open("test.txt", "a+") as fp:
            fp.write(page['title'])
            fp.write(page['text'] + '\n')
    print("爬取成功!")
