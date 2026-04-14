# Utility CSS-Container File




# This Handles Making the Streamlit Button for Calculator Toggle Invisible
st.markdown("""

# CSS to overlay button over your menu item
.stButton > button#calc_btn {
    position: absolute;
    top: 8px; /* adjust to match taskbar */
    left: 800px; /* adjust to match Calculator menu location */
    width: 80px; /* width of menu item */
    height: 20px; /* height of menu item */
    background: transparent !important;
    border: none !important;
    color: transparent !important;
    z-index: 20; /* above menu but below other overlays if needed */
    cursor: pointer;
}

""", unsafe_allow_html=True)