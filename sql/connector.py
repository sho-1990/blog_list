# -*- coding:utf-8 -*-
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:root@localhost/blog_list", echo=True)