import os
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from shapely import length
import config_data as config
import hashlib
from datetime import datetime
def check_md5(md5_str):
    if not os.path.exists(config.md5_path):  # 如果不存在，则返回False
        open(config.md5_path, "w",encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path, "r",encoding="utf-8").readlines():
            line = line.strip()

            if line == md5_str:  # 如果存在，则返回True
                print("已处理过")
                return True # 已处理过
        return False   


def save_md5(md5_str):
    with open(config.md5_path, "a",encoding="utf-8") as f:
        f.write(md5_str + "\n")

def get_string_md5(str,encoding="utf-8"):   # 字符串转md5
    str_bytes = str.encode(encoding=encoding)  # 字符串转字节数组
    md5_object = hashlib.md5()    # 创建md5对象
    md5_object.update(str_bytes) # 更新md5对象 传入需要转换的字节数组
    md5_hex = md5_object.hexdigest()  # 获取md5值 16进制
    return md5_hex



    

class knowledgeBaseService(object):
    def __init__(self):#向量存储的实例
        os.makedirs(config.persist_directory, exist_ok=True)
        self.chroma = Chroma(
            collection_name= config.collection_name,  #数据库名称
            embedding_function = DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory #数据库文件夹位置
                             
        )  
        self.spliter = RecursiveCharacterTextSplitter(       # 文本分割器
            chunk_size = config.chunk_size,       # 分割后文本长度
            chunk_overlap = config.chunk_overlap, # 分割后文本重叠长度
            separators = config.separators,
            length_function = len

        )

    def upload_by_str(self,data,filename):  #将传入的字符串，进行向量化，存入向量数据库中、
        md5_hex = get_string_md5(data)
        if check_md5(md5_hex):  # 检查md5，如果已处理过，则返回
            return "已处理过"
        if len(data) > config.max_split_char_number:   # 如果字符串长度超过最大分割长度，则进行分割
            knowledge = self.spliter.split_text(data)  # 进行分割
        else:
            knowledge = [data] # 否则，不进行分割
        metadata = {"source": filename, # 元数据
                    "create_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # 元数据
                    "operator": "hhhZp" # 元数据
        }
        self.chroma.add_texts(knowledge, metadatas=[metadata for i in knowledge]) # 存入向量数据库中
        save_md5(md5_hex)
        return "上传成功"



        

if __name__ == "__main__":
    kb = knowledgeBaseService()
    kb.upload_by_str("测试123","testfile")
