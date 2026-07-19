

class recode:				# 定义数据类recode，用于封装一条销售记录
    def __init__(self,date,id,money,province):	# 构造函数，接收日期、订单ID、金额、省份四个参数
        self.date = date			# 销售日期
        self.id = id				# 订单ID
        self.money = money			# 销售金额
        self.province = province	# 所属省份
    
    def __str__(self):				# 定义对象的字符串表示，在使用print()时自动调用
        return f"{self.date},{self.id},{self.money},{self.province}"	# 返回用逗号分隔的格式，便于输出查看

    