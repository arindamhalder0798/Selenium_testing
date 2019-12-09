# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class DmozPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("dmoz.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.conn.execute(""" create table if not exists external_links(
                        id INTEGER PRIMARY KEY,
                        name text NOT NULL,
                        link text NOT NULL
                          )""")
    
    def process_item(self, item, spider):

        for i in range(10):
            print(item['name'] [i], item['link'] [i])
            self.store_db(item, i)
        self.conn.close()
        return item

    def store_db(self, item, pos):
        self.conn.execute("""INSERT INTO `external_links`
                          ('name', 'link') 
                           VALUES (?,?);""", (item['name'] [pos], item['link'] [pos]))
        self.conn.commit()