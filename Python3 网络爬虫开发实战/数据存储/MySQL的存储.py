import pymysql

# 创建数据库
# db = pymysql.connect(host='localhost', user='root', password='199541466', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
# db.close()

# 创建表
import pymysql

db = pymysql.connect(host='localhost', user='root', password='199541466', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))'
cursor.execute(sql)
db.close()

# 插入数据
import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost',user='root',password='199541466',port=3306,db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s,%s,%s)'
try:
    cursor.execute(sql,(id, user, age))
    db.commit()
except:
    db.rollback()
db.close()

# 通用插入法
data  = {
    'id':'20120002',
    'name':'Emily',
    'age':21
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
db = pymysql.connect(host='localhost',user='root',password='199541466',port=3306,db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()

# 更新数据
db = pymysql.connect(host='localhost',user='root',password='199541466',port=3306,db='spiders')
cursor = db.cursor()
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql,(25,'Bob'))
    db.commit()
except:
    db.rollback()
db.close()

# 考虑重复问题
data = {
    'id':'20120001',
    'name':'Bob',
    'age':21
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) values ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([' {key} = %s'.format(key=key) for key in data] )
sql += update

db = pymysql.connect(host='localhost',user='root',password='199541466',port=3306,db='spiders')
cursor = db.cursor()
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()

# 删除数据

table = 'students'
condition = 'age<20'


sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
db = pymysql.connect(host='localhost',user='root',password='199541466',port=3306,db='spiders')
cursor = db.cursor()
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

# 查询数据
sql = 'SELECT * FROM students WHERE age >= 20'
db = pymysql.connect(host='localhost',user='root',password='199541466',port=3306,db='spiders')
cursor = db.cursor()
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

# 逐条获取
sql = 'SELECT * FROM students WHERE age >= 20'
db = pymysql.connect(host='localhost',user='root',password='199541466',port=3306,db='spiders')
cursor = db.cursor()
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('row:',row)
        row = cursor.fetchone()
except:
    print('Error')