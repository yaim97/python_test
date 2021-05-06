# 导入包
import pymysql

# 链接数据库
db = pymysql.connect(
    host="localhost",
    user="root",
    password="xxxxxx",
    database="test",
)

# 定义游标
cursor=db.cursor()

# 创建表
sql_create_table="CREATE TABLE User(id int, name varchar(255))"
cursor.execute(sql_create_table)


# 插入数据--1
sql_insert="INSERT INTO User VALUES(0,'yaim')"
cursor.execute(sql_insert)
db.commit()
# 插入数据--2
id_insert=1
name_insert="yaimm"
sql_insert="INSERT INTO User(id,name) VALUES('%d','%s')" % (id_insert,name_insert)
cursor.execute(sql_insert)
db.commit()

# 查询数据
sql_select="SELECT * FROM User WHERE id > %d" % (0)
cursor.execute(sql_select)
result=cursor.fetchall() # 获取到查询的所有记录列表
print(result)

# 删除数据
sql_delete="DELETE FROM User WHERE id = %d" % (1)
cursor.execute(sql_delete)
db.commit()

# 更新数据
sql_update="UPDATE User SET name = 'fyl' WHERE id = %d" % (0)
cursor.execute(sql_update)
db.commit()

# 发生错误则回滚
db.rollback()

# 关闭游标
cursor.close()
# 关闭数据库
db.cursor()