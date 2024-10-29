from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from  langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool

from langchain_core.prompts import PromptTemplate
from langchain import hub
from langchain.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
res=llm.invoke("how are you!")
print(res.content)