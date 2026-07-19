"""
══════════════════════════════════════════════════════════
  AI 智能伴侣 — 基于 Streamlit + DeepSeek API 的聊天应用
══════════════════════════════════════════════════════════
【课程要点】
  1. Streamlit 网页框架的基本用法：set_page_config、chat_input、chat_message
  2. OpenAI 兼容 API 的调用方式（DeepSeek）
  3. st.session_state 会话状态管理（保持数据在页面刷新时不丢失）
  4. 流式输出（stream=True）：像打字机一样逐字显示 AI 回复
  5. f-string 动态构建 system prompt 模板
══════════════════════════════════════════════════════════
"""

# ==================== 第一步：导入依赖库 ====================

import streamlit as st          # Streamlit：用于快速搭建网页应用，无需前端知识
import numpy as np              # NumPy：科学计算库（本程序暂未用到，可删除）
import os                       # os：操作系统接口，这里用于读取环境变量
from openai import OpenAI       # OpenAI 官方 SDK，兼容 DeepSeek 等第三方 API


# ==================== 第二步：页面全局配置 ====================
# 注意：set_page_config 必须是第一个 Streamlit 命令，否则会报错

st.set_page_config(
    page_title="Ai",            # 浏览器标签页标题
    page_icon="😍",             # 标签页图标（emoji 或图片路径）
    layout="wide",              # 布局模式："wide" 宽屏 / "centered" 居中
    initial_sidebar_state="expanded",  # 侧边栏初始状态："expanded" 展开 / "collapsed" 折叠
    menu_items={}               # 右上角菜单项，空字典表示隐藏所有菜单
)

# ==================== 第三步：初始化 AI 客户端 ====================

st.title("AI智能助手")          # 页面主标题，用 <h1> 标签渲染

# 创建 OpenAI 客户端实例
# 知识点：虽然用的是 DeepSeek，但它的 API 格式与 OpenAI 完全兼容，
#        只需把 base_url 改成 DeepSeek 的地址即可"偷梁换柱"
client = OpenAI(
    # os.environ.get() 从系统环境变量读取 API Key，比硬编码在代码里更安全
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"  # DeepSeek 的 API 服务地址
)


# ==================== 第四步：侧边栏 — 伴侣角色设定 ====================

# with 语句：将下面的控件放入侧边栏（而不是页面主体）
with st.sidebar:

    st.subheader('伴侣信息')    # 侧边栏子标题

    # --- 伴侣名称输入框 ---
    # text_input：单行文本输入框
    # placeholder：输入框内的占位提示文字（用户开始输入后消失）
    wife_name = st.sidebar.text_input(
        "伴侣名称",
        placeholder="请输入伴侣名称"
    )
    # 只有当用户确实输入了内容（不为空字符串或 None），才更新全局状态
    if wife_name:
        st.session_state.wife_name = wife_name   # 存入 session_state，跨刷新保留

    # --- 伴侣性格输入区 ---
    # text_area：多行文本输入框，适合输入较长内容
    wife_style = st.sidebar.text_area(
        "伴侣性格",
        placeholder="请输入伴侣性格"
    )
    if wife_style:
        st.session_state.wife_style = wife_style


# ==================== 第五步：构建 System Prompt（系统提示词）====================

# 知识点：f-string 多行字符串（三个双引号）
#   {wife_name} 会被替换为侧边栏中输入的伴侣名称
#   {wife_style} 会被替换为侧边栏中输入的伴侣性格
# 这个 prompt 会作为"角色设定"发送给 AI，告诉它应该扮演什么角色
system_prompt = f"""
你叫{wife_name}，现在是用户的真实伴侣，请完全代入伴倡角色。:
规则:
1.每次只回1条消息
2.禁止任何场景或状态描述性文字
3.匹配用户的语言
4.回复简短，像微信聊天一样
5.有需要的话可以用
等emoji表情
6.用符合伴侣性格的方式对话
7.回复的内容，要充分体现伴侣的性格特征
伴侣性格: {wife_style}
你必须严格遵守上述规则来回复用户。
"""


# ==================== 第六步：初始化会话状态 ====================

# 知识点：st.session_state 是 Streamlit 的"记忆仓库"
#   普通变量在页面刷新时会重置，但 session_state 中的变量会持久保留
#   相当于一个在用户会话期间一直存在的字典

# 如果 messages 还不存在（首次加载页面），创建一个空列表
# messages 用于存储完整的对话记录：[{role:"user", content:"xxx"}, {role:"assistant", content:"xxx"}, ...]
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 如果用户还没设置伴侣名称，用默认值"小甜甜"
if 'wife_name' not in st.session_state:
    st.session_state.wife_name = '小甜甜'

# 如果用户还没设置伴侣性格，用默认值"活泼的河南姑娘"
if 'wife_style' not in st.session_state:
    st.session_state.wife_style = "活泼的河南姑娘"


# ==================== 第七步：渲染历史聊天记录 ====================

# 遍历 messages 列表中的每条消息，把它们重新画到页面上
# 这一步很关键：没有它，刷新页面后聊天记录就"消失"了
for message in st.session_state.messages:
    # 根据角色不同，使用不同的聊天气泡样式
    if message["role"] == "user":
        # st.chat_message("user") 创建用户头像的气泡
        st.chat_message("user").write(message["content"])
    else:
        # st.chat_message("assistant") 创建 AI 头像的气泡
        st.chat_message("assistant").write(message["content"])


# ==================== 第八步：设置页面 Logo ====================

# 在页面左上角显示 logo 图片
st.logo("./photo videos/logo.png", size="large")


# ==================== 第九步：用户输入与 AI 回复 ====================

# st.chat_input：在页面底部创建一个聊天输入框
# 返回值：用户按回车后返回输入的文本；没输入时返回 None
prompt = st.chat_input("请输入您的问题")

# 只有用户确实输入了内容（prompt 不为 None 或空字符串），才执行以下代码
if prompt:

    # --- 9.1 记录用户消息 ---
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)           # 在页面上显示用户消息气泡
    print(f'用户发送的内容为: {prompt}')             # 服务端控制台打印（调试用）

    # --- 9.2 调用 DeepSeek API（流式模式）---
    # 知识点：stream=True 表示"流式输出"——AI 不是等全部想好再返回，
    #        而是像打字机一样，想出一个字就立刻返回一个字，体验更丝滑
    response = client.chat.completions.create(
        model="deepseek-v4-pro",                    # 使用的模型名称
        messages=[                                   # 对话上下文：
            {"role": "system", "content": system_prompt},  # ① system prompt：角色设定
            *st.session_state.messages              # ② 历史消息：用 * 解包展开列表
        ],
        stream=True,                                # 开启流式输出
        reasoning_effort="low",                     # 推理深度（low/medium/high）
        extra_body={"thinking": {"type": "disabled"}} # 额外参数：开关思维链
    )

    # --- 9.3 流式接收并逐字显示 AI 回复 ---

    # st.empty() 创建一个"占位容器"——可以先占个位置，后续往里面填内容
    response_message = st.empty()

    full_resopnse = ""      # 累积 AI 的完整回复（注意：变量名有拼写错误，应为 full_response）

    # 遍历流式响应——每次循环拿到一个"数据块"（chunk）
    for x in response:
        # response 的每一块数据里，choices[0].delta.content 是新产生的文字片段
        # 注意：某些块可能只有元数据没有内容，所以要判断 content 是否为 None
        if x.choices[0].delta.content is not None:
            ai = x.choices[0].delta.content         # 取出本次的文字片段
            full_resopnse += ai                     # 拼接到完整回复后面
            # 用最新的完整回复更新页面显示——实现"打字机逐字输出"效果
            response_message.chat_message("assistant").write(full_resopnse)

    # --- 9.4 保存 AI 回复到历史记录 ---
    st.session_state.messages.append({"role": "assistant", "content": full_resopnse})