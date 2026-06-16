import streamlit as st

st.title("🥗 Quinoa Power Bowl")

st.image(
    "https://images.unsplash.com/photo-1546069901-ba9599a7e63c",
    width="stretch"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Calories", "420")

with col2:
    st.metric("Protein", "22g")

with col3:
    st.metric("Freshness", "94/100")
    st.divider()

st.subheader("🟢 Freshness Analysis")

st.success("Excellent Freshness • 94/100")

st.write("""
This dish received a high freshness score because:

✅ Quinoa harvested 3 days ago

✅ Avocado harvested 1 day ago

✅ Cherry Tomatoes harvested 2 days ago

✅ Ingredients sourced from verified farms

✅ Low transportation distance

✅ No expired ingredients detected
""")
st.divider()

st.subheader("🔍 Transparency Score")

st.progress(96)

st.success("Transparency Rating: 96/100")

st.write("""
This score is calculated based on:

✅ Ingredient Source Available

✅ Harvest Dates Available

✅ Supplier Information Verified

✅ Nutrition Information Provided

✅ Allergen Information Available

✅ Freshness Information Available
""")

with col4:
    st.metric("Price", "₹299")
if "cart" not in st.session_state:
    st.session_state.cart = []

if st.button("🛒 Add to Cart"):

    st.session_state.cart.append(
        {
            "dish": "Quinoa Power Bowl",
            "price": 299
        }
    )

    st.success("Added to Cart!")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info("🌾 Harvest Date: 12 June 2026")

with col2:
    st.info("🚜 Source Farm: Organic Valley Farm")
col1, col2 = st.columns(2)

with col1:
    st.success("📍 Source Location: Ladakh")

with col2:
    st.warning("⚠️ Allergens: Nuts")
st.divider()

st.subheader("⚠️ Allergens")

st.warning("Contains Nuts")

st.divider()

st.subheader("🌱 Ingredient Transparency")

st.divider()

ingredients = [
    ["Quinoa", "120g", "Organic Valley Farm", "Ladakh", "12 June 2026"],
    ["Avocado", "60g", "Green Farms", "Bangalore", "14 June 2026"],
    ["Cherry Tomatoes", "50g", "Fresh Earth Farms", "Tamil Nadu", "13 June 2026"]
]

for ingredient in ingredients:

    with st.expander(f"🌿 {ingredient[0]}"):

        st.markdown(f"**Quantity:** {ingredient[1]}")

        st.markdown(f"**🚜 Farm:** {ingredient[2]}")

        st.markdown(f"**📍 Source Location:** {ingredient[3]}")

        st.markdown(f"**🌾 Harvest Date:** {ingredient[4]}")

        st.progress(95)

        st.caption("Verified Supplier Information")

st.divider()

st.subheader("📍 Ingredient Origins")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🌾 Quinoa")
    st.write("Ladakh")

with col2:
    st.success("🥑 Avocado")
    st.write("Bangalore")

with col3:
    st.success("🍅 Cherry Tomatoes")
    st.write("Tamil Nadu")

st.subheader("♻️ Sustainability")

st.success("87/100")

st.write(
    "This dish uses mostly locally sourced ingredients and has a low transportation footprint."
)

st.divider()

st.subheader("🚚 Food Journey")

st.markdown("""
🌱 Harvested

⬇️

🚛 Transported

⬇️

🍳 Prepared

⬇️

🍽️ Served Fresh
""")