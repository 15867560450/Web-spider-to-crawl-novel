# -*- coding: utf-8 -*-
# Created on 2022/08/26
# Author: mystereal

import requests
from bs4 import BeautifulSoup
import lxml
import re
import os


def crawler_req(url):
    r = requests.get(url)
    if r.status_code != 200:
        print(url + "爬取失败")
        return None
    r.encoding = r.apparent_encoding
    return r


def crawler(view_url):  # 获取搜索页面的json格式
    base_url = "https://trxs.cc"
    book_list = []
    try:
        r = crawler_req(view_url)
        if r is None:
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
    except:
        print(view_url + "爬取失败")
        return None


def crawler_content(content_url):
    base_url = "https://trxs.cc"
    url_list = []
    try:
        r = crawler_req(content_url)
        if r is None:
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
    except:
        print(content_url + "爬取失败")
        return None


def crawler_page(page_url):
    try:
        r = crawler_req(page_url)
        if r is None:
            return None
        soup = BeautifulSoup(r.text, 'lxml')
        data = soup.select('.read_chapterDetail')
        page = {
            'title': soup.h1.text,
            'text': data[0].text
        }
        return page
    except:
        print(page_url + "爬取失败")
        return None


if __name__ == '__main__':
    content = crawler_content('https://trxs.cc/tongren/7216.html')
    title = content['title']
    for page_url in content['url']:
        page = crawler_page(page_url=page_url)
        if page is None:
            continue
        with open(title + ".txt", "a+", encoding='utf-8') as fp:
            fp.write(page['title'])
            fp.write(page['text'] + '\n')
    print("爬取成功!")
