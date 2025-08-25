import streamlit as st
from streamlit_navigation_bar import st_navbar
import matplotlib.pyplot as plt    
import numpy as np
import random
st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "Library", "Tutorials", "Development", "Download"]
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(pages, styles=styles)
st.write(page)

with st.sidebar:
    st.write("Sidebar")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload", "About"])

if page == "Home":
    st.subheader("Graph !!!")
    st.set_page_config(page_title="Device Monitor", layout="centered")
    


    # Example: Simple sine wave
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="Sample Graph")
    ax.legend()

    st.pyplot(fig)
    
    

    on = st.toggle("Status")

    if on:
        st.write("Activated!")


        
        
    curr_power = 69   # Example value
    power_gen = 420   # Example value

    st.write(f"**Curr Pow:** {curr_power} V")
    st.write(f"**Pow Gen:** {power_gen} Wh")
    
    st.markdown(f"""
    <div class="info-card">
        <h4>⚡ Current Power</h4>
        <p style="font-size:20px; color:#2196F3;"><b>{curr_power} V</b></p>
    </div>

    <div class="info-card">
        <h4>🔋 Power Generated</h4>
        <p style="font-size:20px; color:#FF9800;"><b>{power_gen} Wh</b></p>
    </div>
    """, unsafe_allow_html=True)


    if st.button("🔄 Refresh", type="primary"):
        new_power = random.randint(50, 100)
        new_gen = random.randint(300, 600)
        st.success(f"Refreshed! Curr Pow: {new_power} V, Pow Gen: {new_gen} Wh")


    
elif page == "Upload":
    st.title("📂 Upload Files")
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "jpg", "png"])
    
    if uploaded_file:
        st.success(f"Uploaded file: {uploaded_file.name}")
        if uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
            st.text_area("File Content", content, height=200)

