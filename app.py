import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import screen_brightness_control as sbc
import ctypes

# ----------------------------
# Volume Setup
# ----------------------------

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)
volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))

# ----------------------------
# MediaPipe Setup
# ----------------------------

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

print("Gesture Control Running in Background...")
print("Press Ctrl + C in terminal to stop.")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for handLms, handedness in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):

            label = handedness.classification[0].label
            h, w, _ = img.shape

            x1 = int(handLms.landmark[4].x * w)
            y1 = int(handLms.landmark[4].y * h)
            x2 = int(handLms.landmark[8].x * w)
            y2 = int(handLms.landmark[8].y * h)

            distance = np.hypot(x2 - x1, y2 - y1)
            distance = np.clip(distance, 30, 200)

            percent = int(np.interp(distance, [30, 200], [0, 100]))

            if label == "Right":
                vol_scalar = np.interp(distance, [30, 200], [0.0, 1.0])
                volume.SetMasterVolumeLevelScalar(vol_scalar, None)

            elif label == "Left":
                sbc.set_brightness(percent)

cap.release()
cv2.destroyAllWindows()
