import streamlit as st
from PIL import Image
import numpy as np

def convert_to_grayscale(img):
    img_array = np.array(img)
    # Convert to grayscale (simple average method)
    gray_array = np.mean(img_array, axis=2, keepdims=True).astype(np.uint8)
    gray_img = Image.fromarray(gray_array.repeat(3, axis=2)) # Convert back to RGB for display
    return gray_img

st.title("Image to Grayscale Converter")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    if st.button("Convert to Grayscale"):
        grayscale_image = convert_to_grayscale(image)
        st.image(grayscale_image, caption="Grayscale Image", use_container_width=True)