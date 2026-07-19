
from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

result = vector_store.similarity_search(input_text,2)
reference = "["
for doc in result:
    reference += doc.page_content
reference += "]"
def print_prompt(prompt):
    print(prompt.to_string(),)
    print("="*20)
    return prompt
chain = prompt | print_prompt | model | StrOutputParser()

res = chain.invoke({"question": input_text, "context": reference})
print(res)