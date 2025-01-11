import streamlit as st
import google.generativeai as genai

# Configure your Gemini API key
GOOGLE_API_KEY = st.secrets['gemini']['api_key']
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input, chat_history):
    """
    Sends the user's input along with the chat history to the Gemini model
    and returns the generated response.
    """
    try:
        # Combine chat history for contextual input
        full_input = "\n".join(chat_history + [f"User: {user_input}"])
        response = model.generate_content(full_input)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, something went wrong. Please try again later."

# Streamlit UI setup
st.set_page_config(page_title="BablooGPT", page_icon="💬")
st.markdown("<h1 style='text-align: center;'>🤖 Welcome to BablooGPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Your AI assistant is here to help you! 🚀</p>", unsafe_allow_html=True)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Stores conversation history

# Main content area
st.markdown("## ✍️ Enter your query below:")

# Form for user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("", placeholder="Ask me anything...", key='user_input')
    submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        with st.spinner("🤔 Thinking..."):
            # Get response from the model with chat history
            response = getResponseFromModel(user_input, st.session_state.chat_history)
            
            # Update chat history
            st.session_state.chat_history.append(f"User: {user_input}")
            st.session_state.chat_history.append(f"AI: {response}")
        
        # Display conversation
        for i, message in enumerate(st.session_state.chat_history):
            if "User" in message:
                st.markdown(f"**{message}**")
            else:
                st.markdown(f"_{message}_")

# Option to clear chat history
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.success("Chat history cleared!")
