import streamlit as st
from streamlit_option_menu import option_menu
import time

st.set_page_config(page_title="ASLT", page_icon="🚀", layout="wide")

# Custom CSS to make it look even better
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #FF4B4B;
    }
    .SideBar {
            font-size: 58px;
            font-weight: bold;
            text-align: center;
            background: -webkit-linear-gradient(45deg, #004474, #ff5733, #28a745);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
    """, unsafe_allow_html=True)

# Fancy horizontal menu
selected = option_menu(
    menu_title=None,
    options=["🏠 Home", "💻 Projects", "👥 Team Members"],
    # icons=["house", "code-slash", "envelope"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        # "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {
            "font-size": "20px",
            "text-align": "center",
            "color": "black",
            "margin": "0px",
            "--hover-color": "#b8b8b884",
            "transition": "all 0.3s ease"
        },
        "nav-link-selected": {"background-color": "#FF4B4B"},
    }
)

# Page content
#--------------------------------Home----------------------------------
if selected == "🏠 Home":
    st.title("🤖 Real-Time Arabic Sign Language Translator")
    st.markdown("---")

    st.markdown("""

    This project builds a **real-time Arabic Sign Language translator** that captures hand gestures using a camera and instantly translates them into **text or speech**.


    ### 🔥 How it Works:

    - 🎯 **YOLO**: Detects and localizes hands in each video frame with high speed and precision.
    - 🧠 **CNN**: Extracts detailed features from hand shapes and movements.
    - 🔄 **RNN (LSTM/GRU)**: Understands sequences of gestures over time for dynamic sign translation.
    - 🤖 **AI Pipeline**: Combines models to deliver fast, accurate, and natural translations.

    ---

    ### 🌟 Goal:
    > Bridge communication between deaf individuals and the wider community using cutting-edge AI.

    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.image("/Users/fayadh/Documents/Data Science & AI (SDA)/Le Wagon Project/yolov8-streamlit-detection-tracking-master/images/office_4.jpg", caption="Image 1", use_container_width=True)

    with col2:
        st.image("/Users/fayadh/Documents/Data Science & AI (SDA)/Le Wagon Project/yolov8-streamlit-detection-tracking-master/images/office_4_detected.jpg", caption="Image 2", use_container_width=True)


    # search_term = st.sidebar.text_input("Search", "")
    # if search_term:
    #     st.write(f"Searching for: {search_term}")

    # st.snow()
    # st.toast("Welcome to my fancy multi-page app! 🎉", icon="🎈")

    st.sidebar.markdown(
    "<h1 class = 'SideBar' style='color:orange; font-size:70px;'>ASLT</h1>",
    unsafe_allow_html=True
)

#--------------------------------Projects----------------------------------
elif selected == "💻 Projects":
    st.title("💻 My Awesome Projects")
    with st.spinner('Loading projects...'):
        time.sleep(0)
    st.success('Projects loaded! 🚀')
    st.write("Here are some cool things I'm working on:")
#--------------------------------Contact----------------------------------
elif selected == "👥 Team Members":
    st.title("The People Behind the Project")
    st.markdown("---")
    st.title("Our Team:")
    st.header("Fayadh ")
    st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    st.markdown("---")
    st.header("Abdulmajeed ")
    st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    st.markdown("---")
    st.header("Bander ")
    st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    st.markdown("---")
    st.header("Saad ")
    st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    st.markdown("---")
    st.header("Saud ")
    st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
