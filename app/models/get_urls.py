# -*- coding:utf-8 -*-

from sql import urls

def get_url_list():
    try:
        return urls.select_url_orderby_id()
    finally:
        urls.close()
