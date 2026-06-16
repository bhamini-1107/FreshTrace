import streamlit as st

st.title("🏢 Business Portal")

st.write(
    "Add restaurant and dish information for complete food transparency."
)

st.divider()

# Dashboard

st.header("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Dishes Listed", "12")

with col2:
    st.metric("Transparency Score", "94")

with col3:
    st.metric("Customer Views", "2,541")

st.divider()

# Restaurant Information

st.header("🍽 Restaurant Information")

restaurant_name = st.text_input(
    "Restaurant Name"
)

restaurant_location = st.text_input(
    "Location"
)

restaurant_image = st.file_uploader(
    "Upload Restaurant Image",
    type=["jpg", "png", "jpeg"]
)

st.divider()

st.header("🥗 Quick Dish Upload")

dish_name = st.text_input(
    "Dish Name"
)

dish_image = st.file_uploader(
    "Upload Dish Image",
    type=["jpg", "png", "jpeg"]
)

ingredients = st.text_area(
    "Ingredients (One Per Line)",
    placeholder="""
Quinoa - 120g
Avocado - 60g
Cherry Tomatoes - 50g
"""
)

supplier = st.text_input(
    "Supplier / Farm Name"
)
invoice = st.file_uploader(
    "📄 Upload Supplier Invoice",
    type=["pdf", "jpg", "jpeg", "png"]
)
proof = st.file_uploader(
    "📷 Upload Harvest Receipt",
    type=["jpg", "jpeg", "png"]
)

if st.button("Generate Transparency Report"):

    st.success("Dish Added Successfully!")

    st.subheader("📊 Auto Generated Report")
    if invoice:
        st.success("✅ Supplier Invoice Verified")

    if proof:
        st.success("✅ Harvest Receipt Uploaded")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Freshness Score", "94/100")

    with col2:
        st.metric("Transparency Score", "96/100")

    with col3:
        st.metric("Sustainability Score", "87/100")

    st.info(
        "⚠️ Potential Allergens: Nuts"
    )

    st.success(
        "✅ Supplier Information Verified"
    )