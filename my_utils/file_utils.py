# 读取文件内容并打印到控制台
def print_file_info(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as fr:
            print(f"文件内容：{fr.read()}")
    except Exception as e:
        print("文件打开失败")
        print(e)
        

# 向文件末尾追加内容
def append_to_file(file_name, date):
    try:
        with open(file_name, "a", encoding="utf-8") as fa:
            num = fa.write(date)  # 写入并返回写入的字符数
            fa.write("\n")  # 添加换行符
            print(f"已将{date}追加到文件{file_name}中。")
            print(f"追加了{num}个字符。")
    except Exception as e:
        print("文件追加失败")
        print(e)


