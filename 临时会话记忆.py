from langchain_community.chat_models.openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
import os


model=ChatOpenAI(
    model="deepseek-v4-pro",
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)           
#prompt = PromptTemplate.from_template(
#    "你需要根据会话历史回应用户问题。对话历史：{chat_history},用户提问：{input},请回答。")
str_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages([
     ("system","你需要根据会话历史回应用户问题。对话历史"),
     MessagesPlaceholder("chat_history"),
     ("human","请回答如下问题{input}")

]

)
def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt

base_chain = prompt | print_prompt | model | str_parser
story = {}
def get_history(id):
    if id not in story:  # 如果没有历史，则创建一个
        story[id] = InMemoryChatMessageHistory()
    
    return story[id]



new_chain = RunnableWithMessageHistory(
    base_chain,   # 基础链
    get_history,  # 获取历史
    input_messages_key="input",   # 输入消息的键
    history_messages_key="chat_history"   # 历史消息的键
        
)
# 添加langchain配置 为当前配置 id
session_config = {
    "configurable":{
        "session_id":"user_001"
    }
}
res = new_chain.invoke({"input": "小明有两个猫"},session_config) # pyright: ignore[reportArgumentType]
print("第一次执行",res)
res = new_chain.invoke({"input": "小刚有一只狗"},session_config) # pyright: ignore[reportArgumentType]
print("第二次执行",res)
res = new_chain.invoke({"input": "请问总共有多少个宠物"},session_config) # pyright: ignore[reportArgumentType]
print("第三次执行",res)


