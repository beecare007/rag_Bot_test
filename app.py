import streamlit as st
from backend import get_answer
import time
import sys

# Force wide mode to prevent search bar hiding
st.set_page_config(layout="wide")

# Immediate visible search bar
st.title("⚡ Instant Knowledge Assistant 🤖 (AI Tutor)")

# Debug header
st.sidebar.header("System Status")
st.sidebar.write(f"Python: {sys.version}")
st.sidebar.write("Ollama models loaded")

# Always-visible search with two fallbacks
search_container = st.container()
with search_container:
    col1, col2 = st.columns([3,1])
    with col1:
        query = st.text_input(
            "Ask anything about your documents...",
            key="main_search",
            placeholder="Type your question here",
            label_visibility="visible"
        )
    with col2:
        st.write("")  # Spacer
        if st.button("Search", key="search_btn"):
            pass  # Forces refresh

# Fallback search methods
if not query:
    query = st.chat_input("Or type here...")
    
# Processing
if query:
    start_time = time.time()
    
    with st.spinner("Analyzing documents..."):
        response = get_answer(query)
        load_time = time.time() - start_time
    
    # Display with timing info
    st.success(f"Response time: {load_time:.2f}s")
    st.markdown(f"""
    <div style='
        padding: 15px;
        border-radius: 5px;
        background: #f0f2f6;
        margin: 10px 0;
    '>
    {response}
    </div>
    """, unsafe_allow_html=True)

# Debug footer
st.sidebar.divider()
st.sidebar.write("Connection active")
