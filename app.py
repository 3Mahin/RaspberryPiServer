import streamlit as st
import matplotlib.pyplot as plt    
import numpy as np
import random
import base64



# Sidebar
with st.sidebar:
    st.title("Navigation")
    side_page = st.radio("Go to", ["Home", "Upload", "About"])

# Main Content
if side_page == "Home":
    st.subheader(" Graph !!!")

    # Example: Simple sine wave
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="Sample Graph")
    ax.legend()
    st.pyplot(fig)
    
    st.subheader(" Device Information: ")

    on = st.toggle("Status")
    if on:
        st.success("✅ Activated!")
    else:
        st.warning("⚠️ Deactivated")

    # Example values
    curr_power = 69
    power_gen = 420
    
    
    

    # ✅ Put custom HTML inside a container with limited width
    with st.container():
        st.markdown(f"""
        <div style="padding:10px; border-radius:10px; background:#f9f9f9; margin:10px 0;">
            <h4>⚡ Current Power</h4>
            <p style="font-size:20px; color:#2196F3;"><b>{curr_power} V</b></p>
        </div>
        <div style="padding:10px; border-radius:10px; background:#f9f9f9; margin:10px 0;">
            <h4>🔋 Power Generated</h4>
            <p style="font-size:20px; color:#FF9800;"><b>{power_gen} Wh</b></p>
        </div>
        """, unsafe_allow_html=True)

    # Refresh button
    if st.button("🔄 Refresh", type="primary"):
        new_power = random.randint(50, 100)
        new_gen = random.randint(300, 600)
        st.success(f"Refreshed! Curr Pow: {new_power} V, Pow Gen: {new_gen} Wh")


elif side_page == "Upload":
    st.title("📂 Upload Files")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "jpg", "png"])
    if uploaded_file:
        st.success(f"Uploaded file: {uploaded_file.name}")
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
            st.text_area("File Content", content, height=200)

def get_base64_of_bin_file(file_path):
    """
    Reads a file in binary mode and returns its Base64 encoded string.
    """
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_path = "background.jpg"
image_base64 = get_base64_of_bin_file(image_path)

# ✅ Set background image using CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

