from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader('textload和文本分割器.txt',encoding='utf-8')

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
    separators=["\n\n", "\n", "?","!","。",".","？","！" ," ", ""]
)

split_docs = splitter.split_documents(docs)


