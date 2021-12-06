#!/usr/bin/env python
"""
@Project ：web-chatroom 
@File ：db_init.py
@Author ：huweitai
@Date ：2021/12/3 7:00 下午 
@Desc ：
"""
import sqlite3
import settings
import os

if os.path.exists(settings.DB):
    os.remove(settings.DB)
conn = sqlite3.connect(settings.DB)
c = conn.cursor()
create_user = """
create table user(id integer primary key autoincrement,
username text,
email text,
password_hash text,
avatar_url text
)
"""
c.execute(create_user)

create_message = """
create table message(id integer primary key autoincrement,
content text ,
create_time integer,
author_id integer ,
foreign key(author_id) references user(id)
)
"""

c.execute(create_message)
# c.release()
conn.close()
