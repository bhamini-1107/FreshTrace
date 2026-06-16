import streamlit as st

st.title("🛒 Cart")

if "cart" not in st.session_state:
    st.session_state.cart = []

total = 0

for item in st.session_state.cart:

    st.write(
        f"{item['dish']} - ₹{item['price']}"
    )

    total += item["price"]

st.divider()

st.subheader(f"Total: ₹{total}")

if st.button("Checkout"):
    st.success("Order Placed Successfully!")