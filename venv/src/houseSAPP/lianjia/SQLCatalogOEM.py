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
class CatalogBean(Base):
    __tablename__='lianjia_catalog'
    id = Column(Integer,primary_key=True)
    SonUrl = Column(String(255))
    name = Column(String(255))
    putTime = Column(String(255))

class OrmTest(object):

    def __init__(self):
        self.session = Session()

    def add_one(self,list):
        print("id{}".format(id))
        # 详情list
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(timeStr)
        new_obj = CatalogBean(
            name=list[1],
            SonUrl=list[2],
            putTime=str(timeStr)
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def test_search(self):
        result = self.session.query(CatalogBean)
        return result
        # print(type(result))
        # for instance in result:
        #     print(instance.SonUrl, instance.name)

if __name__ == '__main__':
    obj = OrmTest()
    obj.test_search()

