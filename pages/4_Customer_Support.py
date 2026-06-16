import streamlit as st

st.title("💬 Customer Support")

st.write(
    "Need help? Report incorrect information, food safety concerns, or contact our support team."
)

st.divider()

# FAQ

st.header("❓ Frequently Asked Questions")

with st.expander("What is FreshTrace?"):
    st.write(
        "FreshTrace helps customers see ingredient sourcing, harvest dates, freshness scores, and transparency information."
    )

with st.expander("How is the freshness score calculated?"):
    st.write(
        "Freshness scores are based on harvest dates, sourcing distance, and ingredient quality."
    )

with st.expander("Can restaurants edit sourcing information?"):
    st.write(
        "Restaurants can submit information, but verified supplier data is protected to maintain transparency."
    )

st.divider()

# Report Section

st.header("⚠️ Report an Issue")

restaurant = st.text_input("Restaurant Name")

dish = st.text_input("Dish Name")

issue_type = st.selectbox(
    "Issue Type",
    [
        "Incorrect Ingredient Information",
        "Incorrect Harvest Date",
        "Food Safety Concern",
        "Wrong Allergen Information",
        "Other"
    ]
)

description = st.text_area(
    "Describe the Issue"
)

evidence = st.file_uploader(
    "Upload Evidence (Optional)",
    type=["jpg", "png", "jpeg"]
)

if st.button("Submit Report"):

    st.success(
        "Your report has been submitted successfully."
    )

st.divider()

# Contact

st.header("📞 Contact Support")

st.write("Email: support@freshtrace.com")

st.write("Phone: +91 98765 43210")

st.divider()

# Complaint Tracker

st.header("📋 Complaint Status")

st.info(
    "Ticket #FT-2026-1034 | Status: Under Review"
)
st.divider()

st.header("🚨 Report Food Safety Issue")

restaurant_name = st.text_input(
    "Restaurant Name",
    key="food_safety_restaurant"
)

dish_name = st.text_input(
    "Dish Name",
    key="food_safety_dish"
)

issue = st.selectbox(
    "Issue Type",
    [
        "Possible Food Poisoning",
        "Expired Ingredients",
        "Incorrect Ingredient Information",
        "Wrong Allergen Information",
        "Poor Food Quality"
    ]
)

description = st.text_area(
    "Describe the Issue",
    key="food_safety_description"
)

evidence = st.file_uploader(
    "Upload Photo Evidence",
    type=["jpg", "jpeg", "png"],
    key="food_safety_upload"
)

if st.button("Submit Food Safety Report"):

    st.success(
        "🚨 Food Safety Report Submitted Successfully!"
    )

    st.info(
        "Reference ID: FS-2026-001"
    )