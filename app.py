import streamlit as st
import joblib

# Load the trained model
model = joblib.load('models/classifier.pkl')

st.set_page_config(page_title="Retail Issue Classifier", page_icon="🛍️")

st.title("🛍️ Retail Issue Classifier")
st.markdown("Enter a customer issue below, and we'll classify it to the right team.")

# Input field
user_input = st.text_area("✏️ Type or paste the customer issue here:", height=150)

# Predict on button click
if st.button("🔍 Classify Issue"):
    if user_input.strip() == "":
        st.warning("Please enter an issue first.")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"📬 Send this issue to: **{prediction}**")