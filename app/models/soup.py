# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request

#ブログ記事の見出し一覧を
#Aタグ形式で返す関数.
def create_matome_list(analyzed_list=[]):

    matome_list = []
    for soup in analyzed_list:

        for i in soup.find_all('a'):

            if i.get('title') == '個別記事ページへ':
                matome_list.append(i)

            if i.get('itemprop') == 'url':
                matome_list.append(i)

    return matome_list

# urlの一覧を解析し、結果をlistで返す関数.
def analyze_urls(url_list=[]):
    return [BeautifulSoup(urllib.request.urlopen(i.url).read()) for i in url_list]