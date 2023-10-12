import torch
from langchain import HuggingFacePipeline, PromptTemplate
from langchain.chains import RetrievalQA
from transformers import AutoTokenizer, TextStreamer, pipeline, AutoModelForCausalLM
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceInstructEmbeddings
import streamlit as st 

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

print(DEVICE, torch.cuda.is_available())
print(torch.version.cuda)

model_name_or_path = "TheBloke/Llama-2-13B-chat-GPTQ"
model_basename = "model"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path,
    device_map="auto",
    trust_remote_code=False,
    revision="main",
)

print("model is", model)

DEFAULT_SYSTEM_PROMPT = """
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased, concise and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
""".strip()

print(DEFAULT_SYSTEM_PROMPT)

def generate_prompt(prompt: str, system_prompt: str = DEFAULT_SYSTEM_PROMPT) -> str:
    return f"""
[INST] <>
{system_prompt}
<>

{prompt} [/INST]
""".strip()

streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

@st.cache_resource
def llm_pipeline():
    text_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=1024,
        temperature=0,
        top_p=0.95,
        repetition_penalty=1.15,
        streamer=streamer,
    )
    llm = HuggingFacePipeline(pipeline=text_pipeline, model_kwargs={"temperature": 0})
    return llm

SYSTEM_PROMPT = "Use the following pieces of context to answer the question in a concise manner at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer."

template = generate_prompt(
    """
{context}

Question: {question}
""",
    system_prompt=SYSTEM_PROMPT,
)

prompt = PromptTemplate(template=template, input_variables=["context", "question"])

def qa_llm(query):
    llm = llm_pipeline()
    embeddings = HuggingFaceInstructEmbeddings(
        model_name="hkunlp/instructor-large", model_kwargs={"device": DEVICE}
    )
    db = Chroma(persist_directory="db", embedding_function=embeddings)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )
    answer, metadata = qa_chain.ask(query)  # Use the .ask method to get an answer
    return answer

def main():
    st.title("LAWGPT📄")
    with st.expander("About the App"):
        st.markdown(
            """
            This is a Generative AI powered Question and Answering app that responds to questions about the Indian Constitution.
            """
        )
    question = st.text_area("Enter your Question")
    if st.button("Ask"):
        st.info("Your Question: " + question)
        st.info("Your Answer")
        answer = qa_llm(question) 
        st.write(answer)

main()

if __name__ == '__main__':
    main()
