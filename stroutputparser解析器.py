
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

model = ChatTongyi(model="qwen3-max")
str_parser = StrOutputParser()
json_parser = JsonOutputParser()
first_prompt = PromptTemplate.from_template(
    "我邻居姓{lastname},刚生了{gender}。请起个名字,要求必须以json格式给我答案。"
    "要求key是name,value是你起的名字,请严格遵守。"
)
second_prompt = PromptTemplate.from_template(
    "姓名{name},帮我分析这个名字的含义"
)

chain = first_prompt | model | json_parser | second_prompt | model | str_parser

#res = chain.stream({"lastname": "郑", "gender": "男孩"})
for chunk in chain.stream({"lastname": "黄", "gender": "女儿"}):
    print(chunk,end="",flush=True)