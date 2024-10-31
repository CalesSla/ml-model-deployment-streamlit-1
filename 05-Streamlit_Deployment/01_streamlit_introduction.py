import streamlit as st
import time
from PIL import Image

st.title("Machine Learning Model Deployment at the Server!!!")

st.header("Introduction: This is heading")

st.subheader("This is subheader")

st.text("This is text")

input_text = st.text_input("Type something", "type here...")
st.text(input_text)

input_text = st.text_area("Enter here", "this is large text area")

st.markdown("This text is __really important__.")
st.markdown("# This is heading")
st.markdown(
    """
    1. First item
    2. Second item
    3. Third item
    4. Fourth item
 """
)

button = st.button("Click me")
if button:
    st.text("Button is clicked")
    st.info("I am clicked! Snap me fast!")
    st.toast("I dissappear")
    st.warning("This is a warning")
    st.error("This is an error")

flag = st.checkbox("Select me")
st.text(flag)


selection = st.radio("Choose your model", ["NLP", "Image", "Audio"])
st.write(selection)

selection = st.selectbox("Choose your model", ["NLP", "Image", "Audio"])
st.write(selection)

selection = st.multiselect("Choose your model", ["NLP", "Image", "Audio"])
st.write(selection)

with st.spinner("Downloading... Please wait!"):
    st.write("download your model here")

st.slider("Set threshold", 0, 100, step=1)

