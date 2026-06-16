import streamlit as st

st.set_page_config(layout="wide")

st.title("🍽️ FreshTrace")

st.markdown(
    """
    ### Discover Transparent Restaurants
    View ingredient sourcing, harvest locations, freshness scores, and nutritional information before ordering.
    """
)

search = st.text_input(
    "🔍 Search Restaurants or Dishes"
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "pages/restaurant1.jpg",
        width="stretch"
    )
    st.subheader("Green Kitchen")
    st.write("⭐ 4.8")
    st.write("🟢 Transparency Score: 96")
    st.write("📍 Bangalore")

with col2:
    st.image(
        "https://images.unsplash.com/photo-1552566626-52f8b828add9",
        width="stretch"
    )
    st.subheader("Fresh Bowl")
    st.write("⭐ 4.7")
    st.write("🟢 Transparency Score: 92")
    st.write("📍 Mumbai")

with col3:
    st.image(
        "https://images.unsplash.com/photo-1559339352-11d035aa65de",
        width="stretch"
    )
    st.subheader("Urban Harvest")
    st.write("⭐ 4.9")
    st.write("🟢 Transparency Score: 98")
    st.write("📍 Hyderabad")

    st.divider()

st.header("🏆 Top Transparent Restaurants")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🥇 Urban Harvest")
    st.write("Transparency Score: 98")

with col2:
    st.success("🥈 Green Kitchen")
    st.write("Transparency Score: 96")

with col3:
    st.success("🥉 Fresh Bowl")
    st.write("Transparency Score: 92")

    st.divider()

st.header("🔥 Trending Dishes")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("🥗 Quinoa Power Bowl")
    st.write("⭐ 4.9")

with col2:
    st.write("🥑 Avocado Salad")
    st.write("⭐ 4.8")

with col3:
    st.write("🍅 Mediterranean Bowl")
    st.write("⭐ 4.7")