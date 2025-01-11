import streamlit as st
import google.generativeai as genai

# Configure your Gemini API key
GOOGLE_API_KEY = st.secrets['gemini']['api_key']
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    """
    This function sends the user's input to the Gemini model and returns the generated response.
    """
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, something went wrong. Please try again later."

# Streamlit UI setup
st.set_page_config(page_title="Ahmad's Chatbot", page_icon="💬")
st.markdown("<h1 style='text-align: center;'>🤖 Welcome to Ahmad's Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Your AI assistant is here to help you! 🚀</p>", unsafe_allow_html=True)

# Sidebar setup
st.sidebar.image('Ahmad Ali.png', use_column_width=True)
st.sidebar.header("**Ahmad Ali Rafique**")
st.sidebar.write("AI & Machine Learning Expert")

st.sidebar.header("Contact Information", divider='rainbow')
st.sidebar.write("Feel free to reach out through the following")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/ahmad-ali-rafique/)")
st.sidebar.write("[GitHub](https://github.com/Ahmad-Ali-Rafique/)")
st.sidebar.write("[Email](mailto:arsbussiness786@gmail.com)")
st.sidebar.write("Developed by Ahmad Ali Rafique", unsafe_allow_html=True)

# Main content area
st.markdown("## ✍️ Enter your query below:")

# Form for user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("", placeholder="Ask me anything...", key='user_input')
    submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        with st.spinner("🤔 Thinking..."):
            output = getResponseFromModel(user_input)
        st.markdown("### 🤖 Chatbot's Response:")
        st.success(output)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developed by 🧑🏻Ahmad Ali Rafique🧑🏻</p>", unsafe_allow_html=True)
