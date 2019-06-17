#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import time
# default
engine = create_engine('mysql+pymysql://root:Qwer1234@localhost:3306/lianjia?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)
class News(Base):
    __tablename__='lianjia_catalog'
    id = Column(Integer,primary_key=True)
    SonUrl = Column(String(255))
    name = Column(String(255))
    putTime = Column(String(255))

class OrmTest(object):

    def __init__(self):
        self.session = Session()

    def test_search(self):
        items = []
        for instance in self.session.query(News):
            print(instance.SonUrl, instance.name)
            items.append(instance.name)
            items.append(instance.SonUrl)
        return items

if __name__ == '__main__':
    obj = OrmTest()
    items = obj.test_search()
    print(items)





