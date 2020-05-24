# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import logging
class DcardspiderPipeline:
    def __init__(self):
        config = {
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'password':'charlie11438',
        'db':'dcard'
        }
        self.__connection = pymysql.connect(**config)

    def process_item(self, item, spider):
        try:
            with self.__connection.cursor() as cursor:
                check = 'select hyperLink from article where hyperLink="%s"'%item['hyperLink']
                cursor.execute(check)
                result = cursor.fetchone()
                logging.info("select result:"+str(result))
                if not result:
                    sql = 'insert into article values ("%s","%s","%s","%s","%s",%s,%s)' % (item['article'],item['hyperLink'],item['forum'],item['date'],item['writer'],item['response'],item['motion'])
                    cursor.execute(sql)
                else:
                    sql = 'update article set motion=%s,response=%s where hyperLink="%s"'%(item['motion'],item['response'],item['hyperLink'])
                    cursor.execute(sql)
            self.__connection.commit()
            logging.info('insert success')
        except Exception as e:
            logging.info(str(e))
            self.__connection.rollback()
        return item
