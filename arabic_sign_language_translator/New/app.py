import cv2
import time

import numpy as np
import mediapipe as mp
import streamlit as st

from keras.models import load_model
from streamlit_TTS import text_to_speech

# Load trained model and actions
model = load_model('3_words_model_hands_only.keras')
actions = ['السلام عليكم', 'صباح الخير', 'كيف الحال؟']
threshold = 0.7

# Mediapipe setup
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def extract_keypoints(results):
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21 * 3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21 * 3)
    return np.concatenate([lh, rh])

def mediapipe_detection(image, model):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb.flags.writeable = False
    results = model.process(image_rgb)
    image_rgb.flags.writeable = True
    return cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR), results

def draw_landmarks(image, results):
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

def run_app():
    st.title("🤟 Arabic Sign Language Classifier with TTS")
    st.markdown("Detects Arabic signs in real-time and speaks them when the prediction changes.")

    run = st.checkbox('Start Webcam')
    prediction_display = st.empty()
    frame_display = st.empty()

    sequence = []
    last_prediction = ""

    if run:
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    st.warning("Failed to grab frame.")
                    break

                image, results = mediapipe_detection(frame, holistic)
                draw_landmarks(image, results)

                keypoints = extract_keypoints(results)
                sequence.append(keypoints)
                sequence = sequence[-60:]

                if len(sequence) == 60:
                    res = model.predict(np.expand_dims(sequence, axis=0), verbose=0)[0]
                    confidence = np.max(res)
                    predicted_action = actions[np.argmax(res)]

                    # If the prediction changes, update and speak it
                    if confidence > threshold and predicted_action != last_prediction:
                        last_prediction = predicted_action

                        # Generate speech for the prediction
                        text_to_speech(predicted_action, language='ar', key=f"{predicted_action}_{time.time()}")



                    prediction_display.markdown(f"### Prediction: **{predicted_action}** ({100*confidence:.2f}%)")

                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                frame_display.image(image, channels="RGB")

                if not run:
                    break

            cap.release()

if __name__ == '__main__':
    run_app()
