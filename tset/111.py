
from calendar import c					# 导入calendar模块的c函数（当前未使用）
from re import X						# 导入re模块的X常量（当前未使用）

from pymysql import Connection, cursors	# 导入pymysql的Connection和cursors，用于连接MySQL数据库
from pyecharts.charts import Bar		# 从pyecharts导入Bar类，用于绘制柱状图
from pyecharts.options import *		# 导入pyecharts所有配置选项
from def1 import read_file, txt_read, json_read	# 从自定义模块导入文件读取类
from test1 import recode				# 从自定义模块导入recode数据类，表示一条销售记录


txt_read1 = txt_read('D:/2011年1月销售数据.txt')		# 创建txt_read对象，读取1月的txt格式销售数据
json_read1 = json_read('D:/2011年2月销售数据JSON.txt')	# 创建json_read对象，读取2月的JSON格式销售数据
jan_data = txt_read1.read_data()		# 调用read_data()方法，解析文件并返回recode对象列表
feb_data = json_read1.read_data()		# 调用read_data()方法，解析文件并返回recode对象列表
all_data = jan_data + feb_data			# 合并1月和2月的销售数据


conn = Connection(						# 创建MySQL数据库连接
    host='localhost',					# 数据库主机地址，localhost表示本机
    port=3306,							# MySQL默认端口号3306
    user='root',						# 数据库用户名
    password='qq13530705321',			# 数据库密码

)

cursor = conn.cursor()					# 创建游标对象，用于执行SQL语句
cursor.execute('use test')				# 切换到test数据库
for x in all_data:						# 遍历合并后的所有销售数据
    cursor.execute("insert into py_sql values(%s,%s,%s,%s)",	# 使用参数化查询插入数据，防止SQL注入；%s为占位符
                   (x.date, x.id, x.money, x.province)		# 传入占位符对应的参数元组：日期、ID、金额、省份
    )

conn.commit()							# 提交事务，将所有插入操作写入数据库

conn.close()							# 关闭数据库连接，释放资源