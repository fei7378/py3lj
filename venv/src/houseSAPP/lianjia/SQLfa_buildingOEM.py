#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
import time


from SQLStatusListOEM import StatusList
from SQLAlchemyOEM import OrmTest
from SQLPictureOEM import Picture
# default
engine = create_engine('mysql+pymysql://root:Qwer1234@localhost:3306/lianjia?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)
# `longitude` varchar(256) DEFAULT NULL COMMENT '经度',
#   `latitude` varchar(256) DEFAULT NULL COMMENT '纬度',
class buildingBean(Base):
    __tablename__='fa_building'
    building_id = Column(Integer,primary_key=True)
    name = Column(String(255))
    SonUrl = Column(String(255))  # 详细信息的project_name
    createtime = Column(String(255))  #创建时间
    status = Column(Enum('10','20','30','40','50'))
    renovation = Column(Enum('10','20','30'))
    build_type = Column(Enum('10','20','30','40','50'))
    sale = Column(Enum('10','20','30','40'))
    house_price = Column(String(255))
    address = Column(String(255))
    developer = Column(String(255))
    use_time = Column(String(255))
    green = Column(String(255))
    volume = Column(String(255))
    parking = Column(String(255))  # 车位信息
    addr_area = Column(String(255))  # 占地面积
    buld_area = Column(String(255))  # 建筑面积
    property = Column(String(255))  # 物业公司
    synopsis = Column(String(255))  # 楼盘简介
    is_user = Column(String(255))  # 是否用户上传:10=爬虫,20=用户上传
    real_images = Column(String)  # 实景图
    periphery_images = Column(String)  # 周边图
    template_images = Column(String)  # 样板图
    effect_images = Column(String)  # 效果图
    bird_images = Column(String)  # 现场图
    locationImages = Column(String)  # 区位
    matchImages = Column(String)  # 小区配套
    licenseImages = Column(String)  # 预售许可证
    longitude = Column(String)  # 经度
    latitude = Column(String)  # 纬度

class building(object):

    def __init__(self):
        self.session = Session()

    def add_one(self,new_obj):
        # print("id{}".format(id))
        # 详情list
        # timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(timeStr)
        #  `status` enum('10','20','30','40','50') NOT NULL COMMENT '楼盘状态:10=在售,20=代售,30=商办,40=不限购,50=即将预售',
        #   `renovation` enum('10','20','30') NOT NULL COMMENT '装修标签:10=清水房,20=简装,30=精装',
        #   `build_type` enum('10','20','30','40','50') NOT NULL COMMENT '楼盘类型:10=住宅,20=公寓,30=写字楼,40=商铺,50=别墅',
        #   `sale` enum('10','20','30','40') NOT NULL COMMENT '售卖:10=待售,20=即将预售,30=在售,40=已清盘',

        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def test_search(self):
        result = self.session.query(StatusListBean)
        return result
        # print(type(result))
        # for instance in result:
        #     print(instance.SonUrl, instance.name)



    def selectBySonUrl(self,SonUrl):
        result = self.session.query(buildingBean).filter(buildingBean.SonUrl == SonUrl).all()
        return result





def storeToStore():
    statusObj = StatusList()
    result = statusObj.test_search()
    mainOem = OrmTest()
    picture = Picture()
    build = building()
    for instance in result:

        mainItem = mainOem.selectBySonUrl(instance.SonUrl)
        print(instance.SonUrl)

        if len(mainItem):

            bBean = buildingBean()
            bBean.name = instance.name
            bBean.SonUrl = instance.SonUrl
            bBean.createtime = instance.putTime

            bBean.status = instance.status
            bBean.renovation = instance.renovation
            bBean.build_type = instance.build_type
            bBean.sale = instance.sale
            for mainBean in mainItem:
                bBean.house_price = mainBean.unitPrice + " "+mainBean.unit
                bBean.address = mainBean.address
                bBean.developer = mainBean.Developers
                bBean.use_time = mainBean.proRight
                bBean.green = mainBean.green
                bBean.volume = mainBean.volume
                bBean.parking = mainBean.carPlace
                bBean.addr_area = mainBean.land
                bBean.buld_area = mainBean.area
                bBean.property = mainBean.property
                bBean.synopsis = mainBean.label
                bBean.latitude = mainBean.latitude
                bBean.longitude = mainBean.longitude
                bBean.is_user = '10'

                pictureStatusItem = picture.getBySonUrl(instance.SonUrl)
                if len(pictureStatusItem):
                    for pictureStatus in pictureStatusItem:
                        bBean.real_images = pictureStatus.realImages
                        bBean.periphery_images = pictureStatus.locationImages
                        bBean.template_images = pictureStatus.sampleImages
                        bBean.effect_images = pictureStatus.designImages
                        bBean.bird_images = pictureStatus.sceneImages  # 现场图
                        bBean.locationImages = pictureStatus.locationImages  # 区位
                        bBean.matchImages = pictureStatus.matchImages  # 小区配套
                        bBean.licenseImages = pictureStatus.licenseImages  # 预售许可证

                build.add_one(bBean)

        # statusBean = StatusListBean()

        # print(instance.SonUrl, instance.name)



if __name__ == '__main__':
    # obj = OrmTest()
    # obj.test_search()
    storeToStore()
    # build_obj = building()
    # result = build_obj.selectBySonUrl("tyaabmk")
    # print(len(result))