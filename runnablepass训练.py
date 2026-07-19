
from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document



model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题，参考资料为：{context}"),
        ("human", "用户提问:{question}")
    ]
)
vector_store = InMemoryVectorStore(embedding = DashScopeEmbeddings(model="text-embedding-v4"))

vector_store.add_texts(
    ["减肥就是要少吃多练","在减脂期问吃东西很重要,清淡少油控制卡路里摄入并运动起来","跑步是很好的运动哦"]
)

input_text = "怎么减肥?"

retriever = vector_store.as_retriever(search_kwargs={"k": 2})


def format_func(docs:list[Document]):
    if not docs:
        return "无参考资料"
    
    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
    formatted_str += "]"

    return formatted_str

    


chain = (
    {"question":RunnablePassthrough(),"context":retriever | format_func } | prompt | model | StrOutputParser()
)

res = chain.invoke(input_text)
print(res)