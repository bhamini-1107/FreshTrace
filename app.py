import streamlit as st

st.set_page_config(
    page_title="FreshTrace",
    page_icon="🍽️",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

h1{
    color:#2E7D32;
}

.stButton>button{
    background-color:#2E7D32;
    color:white;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

st.title("🍽️ FreshTrace")

st.subheader(
    "Know exactly where your food comes from."
)

st.write(
    "FreshTrace helps customers check ingredient sourcing, freshness, allergens and food quality."
)