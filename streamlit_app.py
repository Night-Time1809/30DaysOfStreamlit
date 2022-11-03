import streamlit as st

st.title("Customizing the theme of Streamlit apps")

st.write("Contents of the `.streamlit/config.toml` file of this app")

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")