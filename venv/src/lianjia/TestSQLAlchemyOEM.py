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
    __tablename__='lianjia_main'
    id = Column(Integer,primary_key=True)
    SonUrl = Column(String(255))
    name = Column(String(255))
    state = Column(String(255))
    address = Column(String(255))
    unitPrice = Column(String(255))
    unit = Column(String(255))
    label = Column(String(255))
    projectAddress = Column(String(255))
    sellAddress = Column(String(255))
    Developers = Column(String(255))
    property = Column(String(255))
    opentime = Column(String(255))
    propertyType = Column(String(255))
    handInHouse = Column(String(255))
    volume = Column(String(255))
    proRight = Column(String(255))
    green = Column(String(255))
    houseNum = Column(String(255))
    propertyMoney = Column(String(255))
    carPlace = Column(String(255))
    heating = Column(String(255))
    water = Column(String(255))
    electric = Column(String(255))
    buildTypw = Column(String(255))
    aversive_Facility = Column(String(255))
    land = Column(String(255))
    area = Column(String(255))
    putTime = Column(String(255))

class OrmTest(object):

    def __init__(self):
        self.session = Session()

    def add_one(self,list):
        print("id{}".format(id))
        # [1, '银诚龙悦中心', '商业类/在售', '龙泉驿/十陵/成洛大道5333号', '7000', '元/平(均价)', '低单价/新盘首开/小户型/环线房', 'yclyzxbjwxb',
        #  ['项目地址：', '成洛大道5333号', '售楼处地址：', '成洛大道5333号（接待时间9:00-18:00）', '开发商：', '成都银诚投资管理有限公司', '物业公司：', '成都千禾物业服务有限公司',
        #   '最新开盘：', '2019.05.04', '物业类型：', '商业类', '交房时间：', '2022年06月30日', '容积率：', '6.40', '产权年限：', '40年', '绿化率：', '10%',
        #   '规划户数：', '暂无', '物业费用：', '2.6元/m²/月', '车位情况：', '地下车位数2918', '供暖方式：', '自采暖', '供水方式：', '民水', '供电方式：', '商电',
        #   '建筑类型：', '塔楼', '嫌恶设施：', '暂无', '占地面积：', '89,333㎡', '建筑面积：', '750,000㎡', '查看更多']]
        # 详情list
        sonlist=list[8]
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(timeStr)
        new_obj = News(
            name=list[1],
            state=list[2],
            address=list[3],
            unitPrice=list[4],
            unit=list[5],
            label=list[6],
            SonUrl=list[7],

            projectAddress=sonlist[1],
            sellAddress=sonlist[3],
            Developers=sonlist[5],
            property=sonlist[7],
            opentime=sonlist[9],
            propertyType=sonlist[11],
            handInHouse=sonlist[13],
            volume=sonlist[15],
            proRight=sonlist[17],
            green=sonlist[19],
            houseNum=sonlist[21],
            propertyMoney=sonlist[23],
            carPlace=sonlist[25],
            heating=sonlist[27],
            water=sonlist[29],
            electric=sonlist[31],
            buildTypw=sonlist[33],
            aversive_Facility=sonlist[35],
            land=sonlist[37],
            area=sonlist[39],
            putTime=str(timeStr)
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj


def main():
    obj = OrmTest()
    rest = obj.add_one(555)
    print(rest.id)

if __name__ == '__main__':
    main()



