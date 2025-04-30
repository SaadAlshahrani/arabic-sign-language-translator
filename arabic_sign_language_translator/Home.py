import streamlit as st
from streamlit_option_menu import option_menu
import time

st.set_page_config(
    page_title="ASLT",
    page_icon="🚀",
    layout="wide"
    )

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
    options=["ℹ️ About", "👥 Team Members"],
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
if selected == "ℹ️ About":
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
# elif selected == "💻 Projects":
#     st.title("💻 My Awesome Projects")
#     with st.spinner('Loading projects...'):
#         time.sleep(0)
#     st.success('Projects loaded! 🚀')
#     st.write("Here are some cool things I'm working on:")
#--------------------------------Contact----------------------------------
elif selected == "👥 Team Members":
    st.title("The People Behind the Project")
    st.markdown("---")
    st.title("Our Team:")
    st.header("Fayadh ")
    st.sidebar.markdown(
    "<h1 class = 'SideBar' style='color:orange; font-size:70px;'>ASLT</h1>",
    unsafe_allow_html=True
    )
    col1, col2 ,col3 , col4 = st.columns(4)
    #----------------------------------------Fayadh-----------------------------
    with col1:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://www.linkedin.com/in/fayadh3" target="_blank" style="margin-right: 10px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="mailto:fayadh3@gmail.com" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://github.com/fayadh3" target="_blank" style="margin-right: 10px;">
                    <img src="https://img.icons8.com/ios11/512/FFFFFF/github.png" alt="GitHub" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="https://lewagon-alumni.slack.com/team/U08DZL4LA2D" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Slack_icon_2019.svg" alt="Slack" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.header("Abdulmajeed ")
    col1, col2 ,col3 , col4 = st.columns(4)
    #----------------------------------------Abdulmajeed-----------------------------
    with col1:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://www.linkedin.com/in/abdulmajeed-alrashidi-0039492bb/" target="_blank" style="margin-right: 10px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="mailto:alrashabdulmajeed@gmail.com" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://github.com/Mjeed42" target="_blank" style="margin-right: 10px;">
                    <img src="https://img.icons8.com/ios11/512/FFFFFF/github.png" alt="GitHub" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="https://slack.com/your-workspace" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Slack_icon_2019.svg" alt="Slack" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.header("Bander ")
    col1, col2 ,col3 , col4 = st.columns(4)
    #----------------------------------------Bander-----------------------------
    with col1:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://www.linkedin.com/in/bandar-al-qahtani-415a00296/overlay/about-this-profile/" target="_blank" style="margin-right: 10px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="mailto:bandr.khald.q@gmail.com" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://github.com/Bandr505q" target="_blank" style="margin-right: 10px;">
                    <img src="https://img.icons8.com/ios11/512/FFFFFF/github.png" alt="GitHub" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="https://lewagon-alumni.slack.com/team/U08BSJAP2R5" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Slack_icon_2019.svg" alt="Slack" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.header("Saud")
    col1, col2 ,col3 , col4 = st.columns(4)
    #----------------------------------------Saud-------------------------------
    with col1:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="http://www.linkedin.com/in/saud-sahli-4a53142a1" target="_blank" style="margin-right: 10px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="mailto:SaudSahli2002@gmail.com" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://github.com/SaudSahli2002" target="_blank" style="margin-right: 10px;">
                    <img src="https://img.icons8.com/ios11/512/FFFFFF/github.png" alt="GitHub" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="https://lewagon-alumni.slack.com/team/U08DEV84QUU" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Slack_icon_2019.svg" alt="Slack" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.header("Saad")
    col1, col2 ,col3 , col4 = st.columns(4)
    #----------------------------------------Saad-------------------------------
    with col1:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://www.linkedin.com/in/saad-s-alshahrani/" target="_blank" style="margin-right: 10px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="mailto:saadalshahrani111@outlook.com" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div style="display: flex; align-items: flex-start; justify-content: flex-start;">
                <a href="https://github.com/SaadAlshahrani" target="_blank" style="margin-right: 10px;">
                    <img src="https://img.icons8.com/ios11/512/FFFFFF/github.png" alt="GitHub" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div style="display: flex; align-items: left; justify-content: left;">
                <a href="https://lewagon-alumni.slack.com/team/U08DJ8197JR" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Slack_icon_2019.svg" alt="Slack" style="width:50px;height:50px;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
