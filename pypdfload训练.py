from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path=

)

i = 0
for doc in loader.lazy_load(): 
    print(doc)
    i += 1