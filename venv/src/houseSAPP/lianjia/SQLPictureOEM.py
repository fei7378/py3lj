#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import sessionmaker
import time
import re

# default
engine = create_engine('mysql+pymysql://root:Qwer1234@localhost:3306/lianjia?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class PictureBean(Base):
    __tablename__ = 'lianjia_images'
    id = Column(Integer, primary_key=True)
    SonUrl = Column(String(255))
    name = Column(String(255))
    designImages = Column(String)
    realImages = Column(String)
    sampleImages = Column(String)
    locationImages = Column(String)
    matchImages = Column(String)
    sceneImages = Column(String)
    licenseImages = Column(String)
    # ImageBackup = Column(String)
    putTime = Column(String(255))


class Picture(object):

    def __init__(self):
        self.session = Session()

    def add_one(self, new_obj):
        # print("id{}".format(id))
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        new_obj.putTime = timeStr
        # print(new_obj.designImages)
        # print(timeStr)
        #
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    # 判断信息是否存在
    def selectBySonUrl(self, SonUrl):
        # print("查询url: {}".format(SonUrl))
        result = self.session.query(PictureBean).filter(PictureBean.SonUrl==SonUrl).all()
        return len(result)
        # print(len(result))
    def getBySonUrl(self, SonUrl):
        # print("查询url: {}".format(SonUrl))
        result = self.session.query(PictureBean).filter(PictureBean.SonUrl == SonUrl).all()
        return result
        # for instance in result:
        #     print(instance.SonUrl, instance.name)

if __name__ == '__main__':
    obj = Picture()
    status = obj.selectBySonUrl("cxdsabjgs")
    print(status)
    if not status:
        print("不存在")
    else:
        print("存在")