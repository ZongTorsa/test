from os import name

import streamlit as st
st.set_page_config(
    page_title="黄宗澎的streamlit训练",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)


st.title("AI智能助手")
st.header("一级标题")
st.subheader("我的功能概览")
st.write("1. 智能代码编写与编辑")
st.write("我可以帮你编写、修改和重构各类代码。无论是创建新项目、添加功能模块，还是修复 bug、优化性能，我都能直接在文件中进行精准编辑。我支持 Python、JavaScript、TypeScript、HTML/CSS、Java、C++ 等数十种编程语言，并且能自动适配你项目中的框架和库（如 React、Vue、Flask、Streamlit 等），确保生成的代码风格一致、符合最佳实践。")
st.write("2. 项目搭建与环境管理")
st.write("我可以从零开始帮你搭建完整的项目结构，包括创建文件夹、配置文件、安装依赖等。同时，我能识别和管理你的 Python 虚拟环境（venv、conda 等），帮你安装或更新第三方包。比如刚才我就帮你配置了虚拟环境并安装了 streamlit，让项目快速进入可开发状态。")
st.write("3. 代码搜索、分析与调试")
st.write("我能快速搜索工作区内的文件内容、定位符号引用、分析代码结构，还能获取编译错误和 lint 警告，帮你排查问题。同时我可以读取终端输出、查看浏览器页面内容，辅助你调试前端页面或后端服务。无论是理解遗留代码还是排查运行时错误，我都能提供有效的帮助。")
st.write("4. 数据库查询与文档检索")
st.write("我支持连接数据库并执行 SQL 查询，帮你快速查看表结构、验证数据。此外，我可以搜索 GitHub 上的开源代码、抓取网页内容、查阅 VS Code API 文档，甚至调用 Pylance 等语言工具获取类型信息和重构建议，让你在编码过程中随时获得所需的参考信息。")
st.image("./photo videos/studentphoto.png",width=400)
st.logo("./photo videos/logo.png",size="large",)

students = {
    "姓名":["黄宗澎",'zys','wjx','gzh'],
    '年龄':[18,17,16,19],
    "学号":[10001,10002,1004,1003]

}
st.table(students)
name = st.text_input("请输入姓名")
st.write("你当前输入的姓名为",name)



gender = st.radio("请点击你想选择的信息",["男",'女','trans'],)
st.write(f"您的性别为{gender}")

