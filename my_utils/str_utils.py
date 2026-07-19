# 将字符串反转
def str_reverse(str):
    str = str[::-1]  # 使用切片步长 -1 实现反转
    return str


# 截取字符串中指定范围的子串
def substr(s, x, y):
    str = s[x:y]     # 从索引 x 截取到索引 y（不包含 y）
    return str

print(substr('abcdefg', 0, 5))
