#!/usr/bin/env python
"""
@Project ：web-chatroom 
@File ：manul_add_user.py
@Author ：huweitai
@Date ：2021/12/6 3:17 下午 
@Desc ：
"""

import sqlite3
import settings
import argparse
import hashlib

conn = sqlite3.connect(settings.DB)
c = conn.cursor()

add_user = """INSERT INTO user (email,username,password_hash,avatar_url) values(?,?,?,?)
"""
parse = argparse.ArgumentParser()
parse.add_argument('--email', type=str)
parse.add_argument('--username', type=str)
parse.add_argument('--password', type=str)
user = parse.parse_args()
user.password_hash = hashlib.md5(user.password.encode('utf-8')).hexdigest()
user.avatar_url = 'https://dn-qiniu-avatar.qbox.me/avatar/'+hashlib.md5(user.email.encode('utf-8')).hexdigest()+'?d=identicon'
c.execute(add_user, (user.email,user.username, user.password_hash, user.avatar_url))
a = c.execute("select * from user;").fetchall()
conn.commit()
conn.close()
for i in a:
    print(i)
