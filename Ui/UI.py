import streamlit as st
import cv2
import PIL
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av
from pathlib import Path
from PIL import Image

# ---------- Page Config ----------
st.set_page_config(page_title="ASLT", layout="wide" , initial_sidebar_state="expanded" , page_icon="/Users/fayadh/Downloads/ASLT Icon.png")

# ---------- Custom Style ----------
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .title {
            font-size: 58px;
            font-weight: bold;
            text-align: center;
            background: -webkit-linear-gradient(45deg, #004474, #ff5733, #28a745);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .section {
            font-size: 26px;
            font-weight: bold;
            color: #34495e;
            margin-top: 30px;
        }
        .small-text {
            font-size: 18px;
            color: #7f8c8d;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Navigation Menu ----------
with st.sidebar:
    st.title("🔍 Navigation")
    menu_options = ["title", "Demos & Projects", "Gallery", "Live Stream", "Features", "Contact Us", "About The Project", "Team Members"]
    selected_option = st.radio("Go to:", menu_options)

# Scroll to the selected section
if selected_option == "titleœœ§":
    st.experimental_set_query_params(section="title")
elif selected_option == "Demos & Projects":
    st.experimental_set_query_params(section="Demos")
elif selected_option == "Gallery":
    st.experimental_set_query_params(section="gallery")
elif selected_option == "Live Stream":
    st.experimental_set_query_params(section="live_stream")
elif selected_option == "Features":
    st.experimental_set_query_params(section="features")
elif selected_option == "Contact Us":
    st.experimental_set_query_params(section="contact")
# elif selected_option == "About The Project":
#     st.experimental_set_query_params(section="about")
# elif selected_option == "Team Members":
#     st.experimental_set_query_params(section="team")

# ---------- Header ----------
st.markdown("<div class='title'>Welcome to ASLT Project</div>", unsafe_allow_html=True)
st.markdown("---")
st.subheader("🧠 Arabic Sign Language Translator")
st.write("An AI-powered web platform to bridge communication through Arabic sign language interpretation.")

#-------------------------------------------------Section 1----------------------------------------------------

# ---------- Projects / Demos ----------
st.markdown("<div class = 'Demos'> ### 🚀 Demos & Projects")

demo_col1, demo_col2, demo_col3 = st.columns(3)

with demo_col1:
    st.image("https://placehold.co/400x300", caption="Live Sign Translation")
    st.write("Translate Arabic sign language in real-time using webcam.")

with demo_col2:
    st.image("https://placehold.co/400x300", caption="Dataset Annotator")
    st.write("Tool for labeling and managing Arabic sign datasets.")

with demo_col3:
    st.image("https://placehold.co/400x300", caption="Model Comparison")
    st.write("Compare accuracy of different ML models on gesture data.")

st.markdown("---") #--------------------------------------Section 2--------------------------------------------

# ---------- Gallery ----------
st.markdown("### 🖼️ Gallery")

gallery_col1, gallery_col2 = st.columns(2)

with gallery_col1:
    st.image("https://placehold.co/600x400", caption="Training session snapshot")

with gallery_col2:
    st.image("https://placehold.co/600x400", caption="User testing with ASL gestures")

st.markdown("---") #--------------------------------------Section 3--------------------------------------------

st.title("🎥 Live Webcam Stream with Streamlit")

# Define the video frame transformer
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Convert and return the frame (unchanged here, but you can process it!)
        img = frame.to_ndarray(format="bgr240")
        bigger = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
        return img

# Start the stream
webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

# st.title("📷 OpenCV Webcam Frame Capture")

# Initialize session state for camera
if "camera_on" not in st.session_state:
    st.session_state.camera_on = False

st.title("🎥 ASLT Camera Control")
st.title("📷 Try the Project from your Webcam")

# Initialize session state
if "camera_on" not in st.session_state:
    st.session_state.camera_on = False

# Two side-by-side buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("📷 Turn Camera ON"):
        st.session_state.camera_on = True

with col2:
    if st.button("🛑 Turn Camera OFF"):
        st.session_state.camera_on = False

# Show camera input if ON
if st.session_state.camera_on:
    st.success("Camera is ON. Capture your sign below:")
    img_file_buffer = st.camera_input("Capture Sign")

    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        st.image(image, caption="Captured Image", use_column_width=True)
else:
    st.warning("Camera is OFF. Click the ON button to activate it.")


# ---------- Footer ----------
st.markdown("© 2025 ASLT — Made with ❤️ using Streamlit")




# st.markdown("---")

# # OpenCV video capture
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     st.error("Unable to access camera")
# else:
#     ret, frame = cap.read()
#     cap.release()

#     if ret:
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

st.markdown("---")

# ---------- Features Section ----------
st.markdown("### 🛠️ Features")


#         st.image(frame, caption="Captured from Camera", channels="RGB")
#     else:
#         st.error("Failed to capture image")


# ---------- Contact ----------
st.markdown("### 📬 Contact Us")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        st.success("Thanks! Your message has been sent. We'll get back to you soon.")

st.markdown("---")

# ---------- About Section ----------
st.markdown("### 🧑‍💻 About The Project")
st.write("""
The **ASLT (Arabic Sign Language Translator)** is a machine learning-based project that uses computer vision to recognize and translate Arabic sign language into readable text.
This tool aims to help individuals with hearing impairments to communicate more easily and effectively in the digital world.
""")
st.markdown("---")
features = [
    "✅ Real-time sign recognition",
    "✅ Multi-letter and word detection",
    "✅ User-friendly interface",
    "✅ Works with webcam or uploaded images",
    "✅ Arabic language support",
]

for feature in features:
    st.write(feature)


# ---------- Team Section ----------
st.markdown("### 👨‍👩‍👧‍👦 Team Members")

team_col1, team_col2, team_col3 = st.columns(3)

with team_col1:
    st.image("https://placehold.co/400x300", caption="Alice - ML Developer")
    st.caption("Specialized in model training and dataset handling.")

with team_col2:
    st.image("https://placehold.co/400x300", caption="Bob - Frontend Engineer")
    st.caption("Built the Streamlit interface and UX design.")

with team_col3:
    st.image("https://placehold.co/400x300", caption="Charlie - Research Lead")
    st.caption("Focused on sign language linguistics and accuracy.")

st.markdown("---")


