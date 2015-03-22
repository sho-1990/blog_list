# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request

#引数のurlを解析し、ブログ記事の見出し一覧を
#Aタグ形式で返す関数.
def a_list(url={}):

    res_tetsugaku = urllib.request.urlopen(url['tetsugaku'])
    res_ryorisoku= urllib.request.urlopen(url['oryorisokuho'])
    res_itsoku = urllib.request.urlopen(url['itsoku'])

    tetsugaku = res_tetsugaku.read()
    ryorisokuho = res_ryorisoku.read()
    itsoku = res_itsoku.read()

    soup_tetsdugaku = BeautifulSoup(tetsugaku)
    soup_ryorisokuho = BeautifulSoup(ryorisokuho)
    soup_itsoku = BeautifulSoup(itsoku)

    soup_list = [soup_tetsdugaku, soup_ryorisokuho, soup_itsoku]

    a_list = []

    for soup in soup_list:

        for i in soup.find_all('a'):

            if i.get('title') == '個別記事ページへ':
                a_list.append(i)

            if i.get('itemprop') == 'url':
                a_list.append(i)

    return a_list