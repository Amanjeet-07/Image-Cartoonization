import streamlit as st
from PIL import Image

st.title('IMAGE CARTOONIZER')
st.text("UPLOAD AN IMAGE")

uploaded_file=st.file_uploader("Choose an Image:",type="jpg")
if uploaded_file is not None:
  img=Image.open(uploaded_file)
  st.image(img,caption="Uploaded Image")

  if st.button("PREDICT"):
    img = img.save("/content/test_code/test_images/new.jpg")
    !python /content/test_code/cartoonize.py
    res = Image.open("/content/test_code/cartoonized_images/new.jpg")
    st.text("RESULT")
    st.image(img,caption="Cartoonized Image")