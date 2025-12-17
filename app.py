import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from collections import Counter

# Import the disease info we created
from disease_info import disease_dic
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Plant Doctor - AI Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS FOR UI POLISH ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        background-color: #2e8b57;
        color: white;
    }
    .report-box {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD MODEL (Cached for speed) ---
@st.cache_resource
def load_model():
    # 1. Rebuild the model structure
    base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    base_model.trainable = False

    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(38, activation='softmax') 
    ])
    
    # 2. Load the weights (Update the filename here!)
    model.load_weights('plant_weights.weights.h5')
    
    return model

model = load_model()

# --- PREDICTION LOGIC ---
def predict_image(image_file):
    img = Image.open(image_file)
    img = img.resize((224, 224))
    img_array = np.array(img)
    
    # Check if image has 4 channels (RGBA) and convert to RGB
    if img_array.shape[-1] == 4:
        img_array = img_array[..., :3]
        
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0 # Normalize
    
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    
    # We need the list of classes exactly as they were during training
    # (These must match the keys in disease_dic)
    class_names = list(disease_dic.keys())
    
    return class_names[class_index], np.max(predictions)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=100)
    st.title("🌿 Plant Doctor")
    st.info("This AI tool helps farmers identify plant diseases by analyzing leaf photos.")
    st.write("---")
    st.write("### ⚙️ How it works")
    st.write("1. Upload 1-3 photos of the same plant.")
    st.write("2. The AI analyzes each photo.")
    st.write("3. It 'votes' to find the most likely disease.")
    st.write("4. You get a treatment plan.")

# --- MAIN PAGE ---
st.title("📸 Plant Disease Detection")
st.write("Upload clear photos of the affected plant leaves.")

uploaded_files = st.file_uploader("Choose leaf images...", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])

if uploaded_files:
    # 1. SHOW IMAGES
    st.write("### 🔎 Preview")
    cols = st.columns(len(uploaded_files))
    for i, file in enumerate(uploaded_files):
        cols[i].image(file, use_container_width=True, caption=f"Image {i+1}")

    # 2. ANALYZE BUTTON
    if st.button("Analyze Plant Health"):
        votes = []
        progress_bar = st.progress(0)
        
        for i, file in enumerate(uploaded_files):
            # Run prediction
            predicted_class, confidence = predict_image(file)
            votes.append(predicted_class)
            
            # Update progress
            progress_bar.progress((i + 1) / len(uploaded_files))
        
        # 3. VOTING LOGIC
        final_decision = Counter(votes).most_common(1)[0][0]
        
        # Get info from database
        info = disease_dic.get(final_decision, {
            'name': 'Unknown Disease', 
            'treatment': 'Consult an expert.'
        })
        
        # 4. DISPLAY RESULTS
        st.write("---")
        st.success("Analysis Complete!")
        
        # Create two columns for the result
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Display a big dynamic icon based on health
            if "healthy" in final_decision.lower():
                st.markdown("<h1 style='text-align: center; font-size: 100px;'>✅</h1>", unsafe_allow_html=True)
            else:
                st.markdown("<h1 style='text-align: center; font-size: 100px;'>⚠️</h1>", unsafe_allow_html=True)
                
        with col2:
            st.markdown(f"## Diagnosis: **{info['name']}**")
            st.markdown(f"**Confidence:** {confidence*100:.1f}%")
            
            with st.expander("🚑 View Treatment Plan", expanded=True):
                st.write(info['treatment'])
                
        # Warning disclaimer
        st.warning("⚠️ Note: This tool is an AI assistant. Always consult an agricultural expert before applying chemical treatments.")