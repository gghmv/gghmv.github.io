# -*- coding: UTF-8 -*-

import pymysql
import traceback
import json

conn = pymysql.connect(host='127.0.0.1', port=3306, user='movie', passwd='Movie000', db='movie', charset='utf8')

def select_movie(id):
    cursor = conn.cursor()
    cursor.execute("select uuid,movie from movie where id = %s",(id))
    return cursor.fetchone()

def select_urls(uuid):
    cursor = conn.cursor()
    cursor.execute("select uuid,url from urls where uuid = %s",(uuid))
    return cursor.fetchall()

def write_data(uuid,data):
    f = open("data/"+uuid+'.json', 'wb')
    try:
        f.write(json.dumps(data, encoding='utf-8', ensure_ascii=False))
    finally:
        if f:
            f.close()

def init_index_json(movie):
    mo = {}
    mo['uuid'] = movie[0].encode('utf-8')
    mo['movie'] = movie[1].encode('utf-8')
    return mo

def main():
    index = []
    for i in range(30000):
        movie = select_movie(i)
        if movie:
            index.append(init_index_json(movie))
            urls = select_urls(movie[0])
            s = []
            for url in urls:
                s.append(url[1].encode('utf-8'))
            write_data(movie[0], s)
    write_data('index', index)

if __name__ == '__main__':
    main()