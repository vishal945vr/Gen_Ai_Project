import streamlit as st
# Stylish Title
st.markdown("""
    <h1 style='text-align: center;
               color: #00BFFF;
               font-family: Arial, sans-serif;
               font-weight: 600;
               margin-top: 10px;
               margin-bottom: 20px;'>
        🤖  Brain Box
    </h1>
""", unsafe_allow_html=True)
# header chat bot
st.markdown("""
    <p style='text-align: center;
              color: #00BFFF;
              font-size: 25px;
              font-family: "Segoe UI", sans-serif;
              margin-top: -10px;
              margin-bottom: 30px;'>
        🔍 This chatbot is designed for quick summaries and smart conversations only.
    </p>
""", unsafe_allow_html=True)

# import libarys
from  langchain_huggingface import ChatHuggingFace,HuggingFaceEmbeddings,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import  StrOutputParser
from dotenv import load_dotenv
load_dotenv()

#llm code
llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    temperature = st.number_input("Efficiency Improvement", min_value=0.1, max_value=2.0, step=0.2)
)
model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()
# background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://png.pngtree.com/background/20250109/original/pngtree-abstract-low-poly-style-of-artificial-intelligence-chatbot-robot-with-text-picture-image_15876749.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# propmt template
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic", "language"],
    template="""
You are a highly qualified researcher and science communicator.

Your task is to explain the following topic in a deeply insightful, logical, and scientifically accurate way:

Topic: {topic}

Instructions:
1. Write in the {language} language with clarity and fluency.
2. Start with a short overview in layman's terms.
3. Then explain the topic in depth using:
   - Scientific principles
   - Step-by-step reasoning
   - Real-world examples or case studies
4. Include research-backed facts and terminology where appropriate.
5. Use analogies or metaphors to make abstract ideas easier to understand.
6. Conclude with key takeaways or practical implications.

Make your explanation comprehensive, intelligent, and suitable for learners, researchers, and professionals.
"""
)
# make  train the  model and answer the any topies
chain=prompt|model|parser
language=st.selectbox("Preferred language:",["English","Hindi"])
user_input=st.text_area("🔍Enter Your Topice")
if st.button("Genrated ⇅") :
    result = chain.invoke({
        "topic": user_input,
        "language": language
    })
    st.success("Succefully Excuted")
    st.write("🤖 Response:")
    st.markdown(result)

   


