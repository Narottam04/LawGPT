import torch
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

print(DEVICE,  torch.cuda.is_available() )

loader = PyPDFDirectoryLoader("pdfs")
docs = loader.load()
print("length of docs is", len(docs))

embeddings = HuggingFaceInstructEmbeddings(
    model_name="hkunlp/instructor-large", model_kwargs={"device": DEVICE}
)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
texts = text_splitter.split_documents(docs)
print("length of texts is", len(texts))


db = Chroma.from_documents(texts, embeddings, persist_directory="db")



