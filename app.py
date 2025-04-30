import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from utils import preprocess_image, predict

import json
with open('class_names.json') as f:
    class_names = json.load(f)

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            padding: 2rem;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #2e7d32;
            color: white;
        }
        .stFileUploader>div>div {
            border: 2px dashed #2e7d32;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='color: #2e7d32;'>🌿 Plant Disease Classifier</h1>", unsafe_allow_html=True)
st.markdown("Upload a plant leaf image and get an instant prediction of its health condition.")
# st.title("🌿 Plant Disease Classifier")

uploaded_file = st.file_uploader("Upload a plant leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1])  # Two equal-width columns
    
    with col1:
        st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)

    with st.spinner("🔍 Analyzing..."):
        img_array = preprocess_image(image)
        model = tf.keras.models.load_model("plant_disease_model.keras")
        prediction, confidence = predict(model, img_array, class_names)

    with col2:
        st.success(f"✅ Prediction:\n\n**{class_names[prediction]}**")
        st.info(f"📊 Confidence: **{confidence * 100:.2f}%**")

