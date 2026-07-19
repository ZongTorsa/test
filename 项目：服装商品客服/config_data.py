
md5_path = "./项目：服装商品客服/md5.text"


# Chroma 配置
collection_name = "Rag"
persist_directory= "./项目：服装商品客服/chroma_db"



# 文本分割配置
chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n", "\n", ".","。","?","？","!","！"," ", ""]
max_split_char_number = 1000

# 相似度检索
k = 1 # 返回最相似的k个向量

#向量化模型
embedding_model = "text-embedding-v4"
chat_model = "qwen3-max"


#提示词模板
system_template = " 以我提供的己知参考资料为主,简洁和专业的回答用户问题。参考资料:{context}。"
human_template = "请回答用户提问:{question}"

session_config = {
        "configurable":{
            "session_id":"user_001"
        }
    } 