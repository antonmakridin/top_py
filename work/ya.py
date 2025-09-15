# from langchain_community.llms import YandexGPT
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# token = 'AQVNwEo4xD0mPA7lXzS4sCGLHp3K8uenS6I9eho5'
# folder = 'b1goak37d5prthkdfd7n'
# # Initialize YandexGPT (replace with your actual credentials or environment variables)
# # If using IAM token:
# # llm = YandexGPT(iam_token="YOUR_IAM_TOKEN", folder_id="YOUR_FOLDER_ID")
# # If using API key:
# llm = YandexGPT(api_key=token, folder_id=folder)

# # Define a prompt template
# template = "What is the capital of {country}?"
# prompt = PromptTemplate.from_template(template)

# # Create an LLMChain
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# # Invoke the chain with a country
# country = "France"
# response = llm_chain.invoke(country)

# print(f"Question: What is the capital of {country}?")
# print(f"Answer: {response['text']}")

from langchain_community.embeddings import YandexGPTEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import YandexGPT

token = 'AQVNwEo4xD0mPA7lXzS4sCGLHp3K8uenS6I9eho5'
folder = 'b1goak37d5prthkdfd7n'
# Initialize YandexGPTEmbeddings (replace with your actual credentials or environment variables)
# embeddings = YandexGPTEmbeddings(iam_token="YOUR_IAM_TOKEN", folder_id="YOUR_FOLDER_ID")
embeddings = YandexGPTEmbeddings(api_key=token, folder_id=folder)
llm = YandexGPT(api_key=token, folder_id=folder)
# Sample documents
docs = [
    "Красный цвет цвет имеет наибольшую длину волны в видимом спектре",
    "Серый лис единственный вид собак, который может лазить по деревьям",
    "Марианская впадина самая глубокая точка мирового океана",
]

# Create a vector store from the documents
vectorstore = FAISS.from_texts(docs, embedding=embeddings)

# Create a retriever
retriever = vectorstore.as_retriever()

# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Query the RAG system
query = "какой вид собак по деревьям ползает?"
rag_response = qa_chain.invoke(query)

print(f"\nВопрос: {query}")
print(f"Ответ: {rag_response['result']}")