from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st


llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

st.title("🤖 AskBuddy - AI QNA Bot")
st.markdown("My QnA ChatBot using LangChain and Google Gemini API.")
#using title we can set title of the app and using description we can write the provided message. 

if "messages" not in st.session_state:
    st.session_state.messages = []
#here we are checking if the messages are not in the session state then we are creating a list of messages in the session state. session state means space till app is running without refreshing the page.


for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)
#this loop is used to display the messages in the chat interface. It iterates through the messages stored in the session state and displays them using the appropriate role (user or AI) and content.loop will execute only if when following if condition will run.


query=st.chat_input("Ask me anything...")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    st.session_state.messages.append({"role": "ai", "content": res.text})
    st.chat_message("ai").markdown(res.text)
#this bblock of code is used to handle user input and generate AI responses. When the user submits a query, it is added to the session state messages, displayed in the chat interface, and then passed to the language model (llm) for processing. The AI's response is also added to the session state messages and displayed in the chat interface.
