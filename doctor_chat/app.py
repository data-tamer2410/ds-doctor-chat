# This file contains the main code for the streamlit app.
import streamlit as st
from functionality import (
    load_model_and_tokenizer,
    processing_user_input,
    generate_response,
    ai_message_generator
)


def main():
    # Set page config
    st.set_page_config(page_title="Doctor Chat", page_icon="🩺️", layout="centered")

    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    if 'context' not in st.session_state:
        st.session_state['context'] = []
    if 'send_in_progress' not in st.session_state:
        st.session_state['send_in_progress'] = False
    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = ""

    # Set title
    _, title_col, _ = st.columns([14, 24, 14])
    title_col.markdown(
        """
        <h1 style='color: grey;'>Doctor Chat <a href="https://github.com/data-tamer2410/ds-doctor-chat">
        <img src="https://img.icons8.com/m_rounded/512/FFFFFF/github.png" width="50" height="50"></a></h1>
        """,
        unsafe_allow_html=True
    )

    # Load model and tokenizer
    model, tokenizer = load_model_and_tokenizer()

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Display user input field
    user_input = st.chat_input("Enter message...")

    # Process user input
    if st.session_state.user_input:
        user_input = st.session_state.user_input
        st.session_state.user_input = ""
    if st.session_state.send_in_progress and user_input:
        st.session_state.send_in_progress = False
        st.session_state.user_input = user_input
        st.rerun()
    if user_input and user_input.strip():
        try:
            st.session_state.send_in_progress = True
            user_input = user_input.strip()
            with st.chat_message("user"):
                st.write(user_input)
            with st.spinner("AI is typing..."):
                input_ids = processing_user_input(user_input, st.session_state.context, tokenizer)
                response = generate_response(input_ids, model, tokenizer)
            with st.chat_message("ai"):
                st.write_stream(ai_message_generator(response))
            st.session_state.send_in_progress = False
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "ai", "content": response, })
            st.session_state.context.append({"token": "[|Human|]", "content": user_input})
            st.session_state.context.append({"token": "[|AI|]", "content": response})
        except Exception as e:
            st.error(str(e))


if __name__ == '__main__':
    main()
