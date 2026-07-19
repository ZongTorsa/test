
import json								# 导入json模块，用于将数据序列化为JSON格式写入文件
from pymysql import Connection			# 导入pymysql的Connection类，用于连接MySQL数据库
with open('D:/2011年2月销售数据.txt','w',encoding='utf-8') as fw:	# 以写入模式打开文件，用于存储查询结果；'w'表示覆盖写入
    conn = Connection(					# 创建MySQL数据库连接对象
    host='localhost',					# 数据库主机地址，localhost表示连接本机数据库
    port=3306,							# MySQL服务的端口号，默认为3306
    user='root',						# 数据库登录用户名
    password='qq13530705321',			# 数据库登录密码
    )
    cursor = conn.cursor()				# 创建游标对象，通过游标执行SQL语句
    cursor.execute('use test')			# 切换到名为test的数据库
    result = cursor.execute("select * from py_sql where datedata >= '2011-02-01' and datedata <'2011-03-01'")	# 查询2011年2月的所有销售记录
    data1 = cursor.fetchall()			# fetchall()获取查询返回的所有行，返回元组列表
    data_dict = {}						# 初始化空字典（当前未使用）
    data_list = []						# 初始化空列表，用于存放转换后的字典格式数据
    for x in data1:						# 遍历查询结果的每一行
        data_list.append({				# 将每行数据转为字典后追加到列表
            "date": str(x[0]),			# 第0列：日期，转为字符串
            "other_id": x[1],			# 第1列：订单ID
            "money": x[2],				# 第2列：销售额
            "province": x[3]			# 第3列：省份
        })
    for x in data_list:					# 遍历转换后的字典列表
        json.dump(x, fw, ensure_ascii=False)	# json.dump()将字典写入文件；ensure_ascii=False保留中文不转义
        fw.write('\n')					# 每条记录后写入换行符，使文件每行一条JSON

     