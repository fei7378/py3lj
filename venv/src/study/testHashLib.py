# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作

import hashlib

# 待加密信息
str = 'this is a md5 test.'

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

# 另一种写法：b‘’前缀代表的就是bytes
str_md5 = hashlib.md5(b'this is a md5 test.').hexdigest()
print('MD5加密后为 ：' + str_md5)


class hashMd5():


    def md5(self,str):
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
    hmd5 = hashMd5()
    hmd5.md5("12ewee")
    str = 'this is a md5 test.'
    hmd5.md5(str)

if __name__ == '__main__':
    main()