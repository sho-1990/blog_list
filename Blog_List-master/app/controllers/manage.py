# -*- coding:utf-8 -*-

from bottle import get, post, route, request, template
from app.models.soup import a_list

@route('/', method='GET')
def soup():

    url = {}
    url['tetsugaku'] = 'http://blog.livedoor.jp/nwknews/'
    url['oryorisokuho'] = 'http://oryouri.2chblog.jp/'
    url['itsoku'] = 'http://blog.livedoor.jp/itsoku/'

    return template('1', i = a_list(url))