import pymysql
db = pymysql.connect(host="localhost",port=3306,user="root",passwd="Qwer1234",db="account")
cursor = db.cursor() #创建游标对象

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()