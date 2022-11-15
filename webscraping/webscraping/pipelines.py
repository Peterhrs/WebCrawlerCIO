import sqlite3
from itemadapter import ItemAdapter


class WebscrapingPipeline:

    def process_item(self, item, spider):
        self.conn.execute(
            "insert into Links(link) values (:link)", 
            item
        )
        self.conn.commit()
        return item

    def create_table(self):
        result = self.conn.execute(
            "select name from sqlite_master where type = 'table' and name = 'Links'"
        )
        try:
            value = next(result)
        except StopIteration as ex:
            self.conn.execute(
                "create table Links(id integer primary key, link text)"
            )

    def open_spider(self, spider):
        self.conn = sqlite3.connect('bdCrawlerLinks')
        self.create_table()
    
    def close_spider(self, spider):
        self.conn.close()
        