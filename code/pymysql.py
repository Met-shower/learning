import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='account',charset='utf8')

cursor = conn.cursor()

