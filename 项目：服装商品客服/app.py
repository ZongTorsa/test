import streamlit as st
import time
from Rag import Ragservice
import config_data as config



st.title("服装尺码推荐客服")
st.divider()
if "message" not in st.session_state:
    st.session_state["message"] = [{"role":"ai","content": "欢迎来到服装尺码推荐客服，请输入您需要了解的服装尺码推荐问题"}]
if "rag" not in st.session_state:
    st.session_state["rag"] = Ragservice()

for message in st.session_state.message:
    st.chat_message(message["role"]).write(message["content"])
prompt = st.chat_input("请输入您的问题")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role":"user","content": prompt})
    ai_res_list = []
    with st.spinner("正在处理..."):
        res = st.session_state["rag"].chain.stream({"question":prompt},config.session_config)
        def capture(generator,cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk
        st.chat_message("assistant").write_stream(capture(res,ai_res_list))
        st.session_state["message"].append({"role":"ai","content":"".join(ai_res_list)})

