import time
import cv2
import numpy as np
import streamlit as st
from keras.models import load_model
from streamlit_TTS import text_to_speech

import mediapipe as mp

# Constants
ACTIONS = ['السلام عليكم', 'صباح الخير', 'كيف الحال؟']
SEQUENCE_LENGTH = 60
PREDICT_EVERY_N_FRAMES = 5
CONFIDENCE_THRESHOLD = 0.7

# Mediapipe setup
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

# Session state initialization
if "camera_running" not in st.session_state:
    st.session_state["camera_running"] = False
if "sequence" not in st.session_state:
    st.session_state.sequence = []  # Use regular list
if "last_prediction" not in st.session_state:
    st.session_state.last_prediction = ""
if "frame_count" not in st.session_state:
    st.session_state.frame_count = 0

# Load model once
@st.cache_resource
def load_sign_model():
    return load_model("Pages/3_words_model_halved.keras")

model = load_sign_model()

# Streamlit UI Setup
st.title("🤟 Saudi Sign Language Classifier with TTS")
st.markdown("Detects Saudi Arabic signs in real-time using hand landmarks and speaks them aloud.")
st.markdown("---")

video_placeholder = st.empty()
prediction_placeholder = st.empty()

# Toggle Camera
st.session_state.camera_running = st.toggle("Start Camera", value=st.session_state.camera_running)

# Helper functions
def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33 * 3)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21 * 3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21 * 3)
    return np.concatenate([pose, lh, rh])

def draw_landmarks(image, results):
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

# Main loop
if st.session_state.camera_running:
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while st.session_state.camera_running:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to access webcam.")
                break

            # Preprocess and detect
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image_rgb)
            keypoints = extract_keypoints(results)
            st.session_state.sequence.append(keypoints)

            # Keep only the last SEQUENCE_LENGTH frames
            if len(st.session_state.sequence) > SEQUENCE_LENGTH:
                st.session_state.sequence = st.session_state.sequence[-SEQUENCE_LENGTH:]

            # Predict every N frames
            if len(st.session_state.sequence) == SEQUENCE_LENGTH and st.session_state.frame_count % PREDICT_EVERY_N_FRAMES == 0:
                sequence_array = np.array(st.session_state.sequence)
                input_data = np.expand_dims(sequence_array, axis=0)
                predictions = model.predict(input_data, verbose=0)[0]
                predicted_idx = np.argmax(predictions)
                predicted_label = ACTIONS[predicted_idx]
                confidence = predictions[predicted_idx]

                # Only speak if prediction changed and confident
                if confidence > CONFIDENCE_THRESHOLD and predicted_label != st.session_state.last_prediction:
                    st.session_state.last_prediction = predicted_label
                    text_to_speech(predicted_label, language="ar", key=f"{predicted_label}_{time.time()}")

                # Display prediction
                with prediction_placeholder.container():
                    st.markdown(f"### Prediction: **{predicted_label}** ({confidence:.2%})")

            # Draw landmarks & show image
            draw_landmarks(frame, results)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            with video_placeholder.container():
                st.image(frame, channels="RGB", width=400)

            st.session_state.frame_count += 1

    cap.release()
    st.session_state.camera_running = False
else:
    with prediction_placeholder.container():
        st.markdown("🛑 Camera is off. Use the toggle above to start.")
