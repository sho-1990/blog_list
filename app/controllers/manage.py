# -*- coding:utf-8 -*-

from bottle import get, post, route, request, template, error
from app.models.soup import create_matome_list, analyze_urls
from app.models import get_urls

@route('/', method='GET')
def soup():

    matome_list = []
    matome_list = create_matome_list(analyze_urls(get_urls.get_url_list()))

    return template('1', i = matome_list)

