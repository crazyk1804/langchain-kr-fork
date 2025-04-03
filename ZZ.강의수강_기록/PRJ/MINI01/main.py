import streamlit as st
from langchain_core.messages.chat import ChatMessage

# 대화기록 저장 용도
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    
def add_message(role, message):
    st.session_state['messages'].append(
        ChatMessage(role=role, content=message)
    )
    
def print_messages():
    for cm in st.session_state['messages']:
        # role = message['role']
        # content = message['content']
        st.chat_message(cm.role).markdown(cm.content)

st.title("챗... GPT")

# 입력 메시지
user_input = st.chat_input("Say something")
if user_input:
    add_message('user', user_input)

print_messages()
