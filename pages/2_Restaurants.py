import streamlit as st

st.title("🍽 Restaurants")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("pages/restaurant1.jpg", width="stretch")
    st.subheader("Green Kitchen")
    st.write("⭐ 4.8")
    st.write("🟢 Transparency Score: 96")
    st.write("📍 Bangalore")

with col2:
    st.image(
        "https://images.unsplash.com/photo-1559339352-11d035aa65de",
        width="stretch")
    st.subheader("Fresh Bowl")
    st.write("⭐ 4.7")
    st.write("🟢 Transparency Score: 92")
    st.write("📍 Mumbai")

with col3:
    st.image(
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
        width="stretch"
    )
    st.subheader("Urban Harvest")
    st.write("⭐ 4.9")
    st.write("🟢 Transparency Score: 98")
    st.write("📍 Hyderabad")
