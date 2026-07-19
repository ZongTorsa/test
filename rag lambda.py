import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
model = ChatOpenAI(
    model="deepseek-v4-pro",
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
                   
)
str_parser = StrOutputParser()
json_parser = JsonOutputParser()
first_prompt = PromptTemplate.from_template(
    "我邻居姓{lastname},刚生了{gender}。请起个名字。只需要一个名字，不需要其他额外内容。"
)
second_prompt = PromptTemplate.from_template(
    "姓名{name},帮我分析这个名字的含义,以简洁突出特点的描述。"
)
my_funs = RunnableLambda(lambda x: {"name": x.content})
chain = first_prompt | model | my_funs | second_prompt | model | str_parser

#res = chain.invoke({"lastname": "郑", "gender": "女儿"})
#print(res)
for res in chain.stream({"lastname": "黄", "gender": "女儿"}): 
    print(res,end="",flush=True)
