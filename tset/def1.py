import json							# 导入json模块，用于解析JSON格式的数据
from test1 import recode				# 导入recode数据类，用于封装每条销售记录

class read_file():					# 文件读取基类，定义统一的读取接口
    def read_data(self):				# 读取数据的通用方法，子类应重写此方法
        pass						# 基类中不实现具体逻辑，由子类覆盖实现

class txt_read(read_file):			# 继承read_file，专门读取txt格式（逗号分隔）的销售数据
    def __init__(self,path):			# 构造函数，接收文件路径
        self.path = path				# 保存文件路径
    
    def read_data(self):				# 重写父类的read_data方法
        with open(self.path,'r',encoding='utf-8') as f:	# 以只读模式打开文件，指定utf-8编码
            record_list = []			# 初始化空列表，用于存放解析后的recode对象
            for line in f.readlines() :	# readlines()读取文件所有行，逐行处理
                line = line.strip()		# strip()去除行首尾的空白字符（如换行符、空格）
                data_line = line.split(",")	# split(",")按逗号将一行字符串拆分为列表，如 ["2011-01-01","A001","100","北京"]
                recode_1 = recode(data_line[0],data_line[1],int(data_line[2]),data_line[3])	# 创建recode对象；金额转为int类型
                record_list.append(recode_1)	# 将recode对象添加到结果列表
            return record_list			# 返回所有销售记录列表

class json_read(read_file):			# 继承read_file，专门读取JSON格式的销售数据
    def __init__(self,path):			# 构造函数，接收文件路径
        self.path = path				# 保存文件路径
    
    def read_data(self):				# 重写父类的read_data方法
        with open(self.path,'r',encoding='utf-8') as f:	# 以只读模式打开文件，指定utf-8编码
            record_list = []			# 初始化空列表
            for line in f.readlines() :	# 逐行读取文件
                data_dict = json.loads(line)	# json.loads()将一行JSON字符串解析为Python字典
                recode_1 = recode(data_dict['date'],data_dict['order_id'],int(data_dict['money']),data_dict['province'])	# 从字典中按key取值创建recode对象
                record_list.append(recode_1)	# 将recode对象添加到结果列表
        return record_list				# 返回所有销售记录列表

            