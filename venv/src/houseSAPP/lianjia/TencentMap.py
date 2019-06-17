import requests

import hashlib

import json

from SQLAlchemyOEM import OrmTest

SK = "yB29tAH17ZQVvqVhI0RcWpti8OZbdMoU"
key = "2ORBZ-4Z2CD-TUN44-P4ICJ-IKHYJ-PVF6Z"



def md5(str):
    # 创建md5对象
    m = hashlib.md5()

    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()

    print('MD5加密前为 ：' + str)
    print('MD5加密后为 ：' + str_md5)
    return str_md5

def main():
    global SK,key

    ormTest = OrmTest()
    resultMain = ormTest.selectAll()
    for rmain in resultMain:
        print(rmain.projectAddress)


        address = "成都市"+rmain.projectAddress.strip()

        str = "/ws/geocoder/v1/?address="+address+"&key="+key+SK
        print(str)
        strMd5 = md5(str)
        print(strMd5)

        r = requests.get(url='https://apis.map.qq.com/ws/geocoder/v1/',params={"address":address,"key":key,"sig":strMd5})


        try:
            rjson = json.loads(r.text)
            result = rjson['result']
            localtion = result['location']
            longitude = localtion['lng']
            latitude = localtion['lat']

            # print(localtion)
            print(longitude)
            print(latitude)
            ormTest.update_one(rmain.id,longitude,latitude)
        except:
            print("返回值异常: "+r.text)

if __name__ == '__main__':
    main()