from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.runnables import RunnableMap
import keys 

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# Facebook AI Similarity Search
db = FAISS.from_documents(docs, 
                          HuggingFaceEmbeddings(
                              model_name='sentence-transformers/all-MiniLM-L6-v2'))
print('Created FAISS index')

query = "Generative AI course fee"

retriever = db.as_retriever(search_type="similarity", 
                            search_kwargs={"k": 3})

model_name = "mistralai/Mistral-7B-Instruct-v0.3"
 

prompt_template = """
Answer the question using the given context:

{context}

Question: {question}
"""

prompt  = PromptTemplate.from_template(prompt_template)

llm = HuggingFaceEndpoint(
    model = model_name,
    task="text-generation",
    huggingfacehub_api_token=keys.HUGGINGFACEKEY,
    max_new_tokens = 256
)

chain = (
    RunnableMap({
        "context": lambda x: retriever.invoke(x["question"]),
        "question": lambda x: x["question"]
    })
    | prompt
    | llm
    | StrOutputParser()
)

query = "What is the fee for the AWS course?"
response = chain.invoke({"question": query})
print("Answer:", response)
