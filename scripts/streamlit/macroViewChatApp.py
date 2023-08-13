import streamlit as st
import random
import time

st.title("MacroView Care Center Chat App")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = "Macroview Care Centre (MC2) was founded by Ms Emily Low and her husband in 2003. The couple raised four children of their own with great care and saw them growing up to be healthy, happy and unique individuals. Ms Low, who actively engages in professional counseling and social work in Singapore, pursued the idea of bringing her expertise back to her homeland. Combining concepts of education and counseling, the couple focuses on children’s lifelong learning developments. They personally customised and led various programmes to develop children’s vast learning abilities. "
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
