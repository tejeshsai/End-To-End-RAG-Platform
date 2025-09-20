from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def get_retriever(collection_name: str, persist_directory: str):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return Chroma(
        collection_name=collection_name,
        persist_directory=persist_directory,
        embedding_function=embeddings
    ).as_retriever(search_kwargs={"k": 4})


def answer_pdf_query(query: str) -> str:
    retriever = get_retriever(
        collection_name="pdf_embeddings", persist_directory="chroma_db")

    system_prompt = "Answer the question based on the context.if you don't know please answer you don't know, \n\nContext:{context}"

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    llm = ChatOpenAI(model="gpt-4o-mini")
    qa_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, qa_chain)

    result = chain.invoke({"input": query})
    return result["answer"]
