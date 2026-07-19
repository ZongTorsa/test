
from vector_store import VectorStore
from langchain_community.embeddings import DashScopeEmbeddings
import config_data as config
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory,RunnableLambda
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from file_histor import get_history


class Ragservice(object):
    def __init__(self):
        self.vector_service = VectorStore(
            embedding=DashScopeEmbeddings(model=config.embedding_model))
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", config.system_template),
                ("system", "这是用户的对话历史记录如下"),
                MessagesPlaceholder("chat_history"),
                ("human", config.human_template)
            ]
        )
        self.chat_model = ChatTongyi(model=config.chat_model, streaming=True)  # pyright: ignore[reportCallIssue]
        self.chain = self.__get_chain()

    def __get_chain(self):
        retriever = self.vector_service.get_retriever()
        def format_document(docs:list[Document]):
            if not docs:
                return "无参考资料"
            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段：{doc.page_content}\n文档元数据:{doc.metadata}\n\n"
            return formatted_str
        
        def format_for_retriever(value):
            return value["question"]
        def format_for_promptTemplate(value):
            new_value = {}
            new_value["question"] = value["question"]["question"]
            new_value["context"] = value["context"]
            new_value["chat_history"] = value["question"]["chat_history"]

            return new_value

        chain =(
            {
                "question":RunnablePassthrough(), 
                "context":RunnableLambda(format_for_retriever) | retriever | format_document
            }  | RunnableLambda(format_for_promptTemplate) | self.prompt_template | self.chat_model | StrOutputParser()
        )
        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="question",
            history_messages_key="chat_history"
        )
        
        return conversation_chain
    

if __name__ == "__main__":
    session_config = {
        "configurable":{
            "session_id":"user_001"
        }
    } 
    res = Ragservice().chain.invoke({"question":"你能做什么"},session_config)
    print(res)