#!/usr/bin/python3
# 户型图 正式库
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker

from SQLStatusListOEM import StatusList
from SQLHouseListOEM import HouseList
import time
# default
engine = create_engine('mysql+pymysql://root:Qwer1234@localhost:3306/lianjia?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)
# CREATE TABLE `fa_building_apartment` (
#   `building_apartment_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
#   `image` varchar(256) NOT NULL COMMENT '户型图片链接',
#   `area` varchar(255) DEFAULT NULL COMMENT '面积',
#   `price` varchar(255) NOT NULL COMMENT '估价',
#   `building_id` int(11) NOT NULL COMMENT '楼盘id',
#   `createtime` datetime NOT NULL COMMENT '创建时间',
#   `orientation` varchar(64) NOT NULL COMMENT '朝向',
#   `sale` int(11) NOT NULL COMMENT '售卖状态:10=待售,20=在售,30=售罄',
#   `layout` varchar(255) DEFAULT NULL COMMENT '户型',
#   `housetype` varchar(255) DEFAULT NULL COMMENT '居室',
#   PRIMARY KEY (`building_apartment_id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COMMENT='楼盘户型表';
class apartmentBean(Base):
    __tablename__='fa_building_apartment'
    building_apartment_id = Column(Integer,primary_key=True)
    image = Column(String(255))  #户型图片链接',
    area = Column(String(255))  #面积',
    price = Column(String(255))  #估价',
    building_id = Column(Integer)  #楼盘id',
    createtime = Column(String(255))  #创建时间',
    orientation = Column(String(255))  #朝向',
    sale = Column(Integer)  #售卖状态:10=待售,20=在售,30=售罄',
    layout = Column(String(255))  #户型',
    housetype = Column(String(255))  #居室',


class apartment(object):

    def __init__(self):
        self.session = Session()

    def add_one(self,new_obj):
        # print("id{}".format(id))
        # 详情list
        # timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(timeStr)

        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def test_search(self):
        result = self.session.query(HouseListBean)
        return result
        # print(type(result))
        # for instance in result:
        #     print(instance.SonUrl, instance.name)

def main():
    slist = StatusList()
    result = slist.test_search()
    houseListObj = HouseList()
    aObj = apartment()
    for sitem in result:
        hlBeanAll = houseListObj.selectBySonUrl(sitem.SonUrl)
        # 如果存在此条房屋信息的多个户型
        if len(hlBeanAll):
            for hlBean in hlBeanAll:
                aBean = apartmentBean()
                aBean.image = hlBean.picture
                aBean.area = hlBean.area[3:]
                aBean.building_id = sitem.id
                aBean.createtime = sitem.putTime
                if hlBean.status == "在售":
                    aBean.sale = 20
                elif hlBean.status == "售罄":
                    aBean.sale = 30
                elif hlBean.status == "待售":
                    aBean.sale = 10
                else:
                    aBean.sale = 0   #未知
                aBean.layout = hlBean.layout
                aBean.price = "暂无数据"
                aBean.orientation = "暂无数据"
                aBean.housetype = hlBean.housetype[3:]
                aObj.add_one(aBean)






if __name__ == '__main__':
    main()