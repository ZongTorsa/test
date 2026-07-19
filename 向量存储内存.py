from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = InMemoryVectorStore(
    embedding = DashScopeEmbeddings(),
)


loader = CSVLoader(
    file_path = "./data/info.csv",
    encoding = "utf-8",
    source_column="source",
)

documents = loader.load()


vector_store.add_documents(
    documents = documents,
    ids = ["id"+str(i) for i in range(1,len(documents)+1) ]

)


vector_store.delete(["id1","id2"])

result = vector_store.similarity_search(
    "Python是不是简单易学呀",3

)
print(result)
