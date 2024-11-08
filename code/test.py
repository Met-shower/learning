import pymysql

conn = pymysql.connect(host='localhost',user='root' ,passwd='123456',db='school',charset='utf8')

cursor=conn.cursor()




# 创建表格不需要 conn.commit()
# sql = 'CREATE TABLE TEST(id INT, name VARCHAR(20))'


# # 通过使用 cursor.execute() 来对数据库进行操控
# cursor.execute(sql)
# ret = cursor.execute("INSERT INTO TEST VALUES (1, 'alex'), (2, 'lxy')")
# ret 接收的值是影响的行数 ，此处返回值是 2


# 打开列表
RET = cursor.execute("select * from TEST")
# print(RET)



# # 使用 fetch 方法查找表格内容
# print(cursor.fetchone())
# print(cursor.fetchall())
# print(cursor.fetchmany(3))


# 对游标进行控制
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
# 相对位置上游标移动到上一个
cursor.scroll(-1,mode='relative')
# 绝对位置移动游标
cursor.scroll(1,mode='absolute')





conn.commit()