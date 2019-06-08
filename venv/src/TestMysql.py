import pymysql

config = {
          'host':'localhost',
          'port':3306,
          'user':'root',
          'passwd':'Qwer1234',
          'db':'account',
          'charset':'utf8'
          }
# 打开数据库连接
conn = pymysql.connect(**config)
try:
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM a_user "

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    liall = []
    for row in results:
        # print(row)
        liall.append(list(row))
        # fname = row[0]
        # lname = row[1]
        # age = row[2]
        # sex = row[3]
        # income = row[4]
        # # 打印结果
        # print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
        #       (fname, lname, age, sex, income))
    print(liall)
    # 关闭游标
    cursor.close()

    # 关闭链接
    conn.close()
    print("查询成功")
except:
    print("查询失败")
    # 发生错误时回滚