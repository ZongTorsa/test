import streamlit as st
from knowledge_base import knowledgeBaseService
import time

st.title("知识库上传系统")
text_loader = st.file_uploader(
    "上传知识库文件",
    type=["txt"],
    accept_multiple_files=False, # 是否允许上传多个文件
)

if "service" not in st.session_state:
    st.session_state["service"] = knowledgeBaseService()

if text_loader is not None:
    file_name = text_loader.name
    file_tyer = text_loader.type
    file_size = text_loader.size/1024

    st.subheader(f"文件名:{file_name}")
    st.write(f"格式:{file_tyer} | 大小:{file_size:.2f} KB")
    text = text_loader.read().decode("utf-8")

    with st.spinner("上传中..."):
        time.sleep(1)
        result = st.session_state["service"].upload_by_str(text,file_name)
        st.write(result)

