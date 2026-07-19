from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi


chat_prompt_template = ChatPromptTemplate.from_messages(
    [
       ("system","你是一名边塞诗人。"),
       MessagesPlaceholder("history"),
       ("human","请再来一首唐诗"),
    ]
)


history_data = [
    ("human","请来一首唐诗"),
    ("ai","床前明月光,疑是地上霜，举头望明月，低头思故乡。"),
    ("human","好诗，请再来一首"),
    ("ai","白日依山尽，黄河入海流。")
]

model = ChatTongyi(model="qwen3-max")
chain = chat_prompt_template | model
#res = chain.invoke({"history":history_data})
#print(res.content)
for chunk in chain.stream({"history":history_data}):
    print(chunk.content,end="",flush=True)