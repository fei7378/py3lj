#!/usr/bin/python3
# 户型图
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
import time
# default
engine = create_engine('mysql+pymysql://root:Qwer1234@localhost:3306/lianjia?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)
# CREATE TABLE `lianjia_layout` (
#   `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
#   `SonUrl` varchar(255) DEFAULT NULL COMMENT '详细信息的project_name',
#   `name` varchar(255) DEFAULT NULL COMMENT '房屋名称',
#   `layout` varchar(255) DEFAULT NULL COMMENT '户型',
#   `picture` varchar(255) DEFAULT NULL COMMENT '图片',
#   `housetype` varchar(255) DEFAULT NULL COMMENT '居室',
#   `area` varchar(255) DEFAULT NULL COMMENT '面积',
#   `money` varchar(255) DEFAULT NULL COMMENT '均价',
#   `status` varchar(255) DEFAULT NULL COMMENT '状态',
#   `direction` varchar(255) DEFAULT NULL COMMENT '朝向,暂无',
#   `putTime` varchar(255) DEFAULT NULL COMMENT '写入时间',
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
class HouseListBean(Base):
    __tablename__='lianjia_layout'
    id = Column(Integer,primary_key=True)
    SonUrl = Column(String(255))
    name = Column(String(255))
    layout = Column(String(255))
    picture = Column(String(255))
    housetype = Column(String(255))
    area = Column(String(255))
    money = Column(String(255))
    status = Column(String(255))
    direction = Column(String(255))
    putTime = Column(String(255))


class HouseList(object):

    def __init__(self):
        self.session = Session()

    def add_one(self,list):
        # print("id{}".format(id))
        # 详情list
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(timeStr)

        new_obj = HouseListBean(

            SonUrl = list[6],
            name = list[7],
            layout = list[0],
            picture = list[1],
            housetype = list[2],
            area = list[3],
            money = list[4],
            status = list[5],
            direction = "",
            putTime = timeStr

        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def test_search(self):
        result = self.session.query(HouseListBean)
        return result
        # print(type(result))
        # for instance in result:
        #     print(instance.SonUrl, instance.name)


    def selectBySonUrl(self,SonUrl):
        result = self.session.query(HouseListBean).filter(HouseListBean.SonUrl == SonUrl).all()
        return result