# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/sho/bottle_sample/')
from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Urls(Base):

    __tablename__ = 'urls'

    id = Column(Integer, primary_key = True)
    url = Column(VARCHAR(length=255))
    site_name = Column(VARCHAR(length=255))
    regdate = Column(TIMESTAMP)

    def __init__(self, url, site_name):

        self.url = url
        self.site_name = site_name

    def __repr__(self):

        return "<Urls(url='%s', site_name='%s')>" % (self.url, self.site_name)

from sqlalchemy.orm import sessionmaker
from sql import connector
Session = sessionmaker(bind=connector.engine)
session = Session()

def select_url_orderby_id():
        url_list = []
        for i in session.query(Urls).order_by(Urls.id):
            url_list.append(i)
        return url_list

def close():
    session.close()