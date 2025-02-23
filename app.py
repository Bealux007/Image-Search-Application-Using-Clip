import streamlit as st
from PIL import Image
from models.search import ImageSearch
import os

# Set up the image search model
IMAGE_FOLDER = "data/images"
if not os.path.exists(IMAGE_FOLDER):
    st.error(f"Image folder '{IMAGE_FOLDER}' not found. Please check the path.")
    st.stop()

image_search = ImageSearch(image_folder=IMAGE_FOLDER)

# Streamlit UI
st.title("🔍 Image Search App")
st.write("Search for images using text descriptions or by uploading an image.")

# Select search method
search_method = st.radio("Choose a search method:", ["🔤 Text Description", "📸 Upload Image"])

# Text-based search
if search_method == "🔤 Text Description":
    text_query = st.text_input("Enter a description of the image:")
    if st.button("🔍 Search"):
        if text_query.strip():  # Ensure the input is not empty
            results = image_search.search_by_text(text_query)
            if results:
                st.write("### 🖼️ Top Matches:")
                for result in results:
                    st.image(result, use_container_width=True)
            else:
                st.warning("No matching images found. Try a different description!")
        else:
            st.warning("Please enter a valid text description.")

# Image-based search
elif search_method == "📸 Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("🔍 Search"):
            results = image_search.search_by_image(image)
            if results:
                st.write("### 🖼️ Top Matches:")
                for result in results:
                    st.image(result, use_container_width=True)
            else:
                st.warning("No matching images found. Try uploading a different image!")
