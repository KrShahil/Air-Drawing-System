import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# =======================
# LOAD MEDIAPIPE MODEL
# =======================
base_options = python.BaseOptions(
    model_asset_path="models/hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

# =======================
# INITIALIZE CAMERA
# =======================
cap = cv2.VideoCapture(0)

# =======================
# DRAWING VARIABLES
# =======================
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

prev_x, prev_y = 0, 0
draw_color = (255, 0, 255)     # Purple (default)
brush_thickness = 6

min_brush = 2
max_brush = 20

# Finger tips: index, middle, ring, pinky
finger_tips = [8, 12, 16, 20]

# =======================
# MAIN LOOP
# =======================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    if result.hand_landmarks:
        hand = result.hand_landmarks[0]
        h, w, _ = frame.shape

        # -----------------------
        # FINGER STATE DETECTION
        # -----------------------
        fingers = []
        for tip in finger_tips:
            fingers.append(1 if hand[tip].y < hand[tip - 2].y else 0)

        # Index finger position
        x = int(hand[8].x * w)
        y = int(hand[8].y * h)

        # Hand width (for open palm)
        hand_width = abs(hand[20].x - hand[8].x)

        # -----------------------
        # CLEAR SCREEN (OPEN PALM)
        # -----------------------
        if hand_width > 0.35 and sum(fingers) >= 3:
            canvas = np.zeros((480, 640, 3), dtype=np.uint8)
            prev_x, prev_y = 0, 0

        # -----------------------
        # COLOR SELECTION MODE
        # -----------------------
        elif fingers == [1, 1, 0, 0]:      # Index + Middle
            draw_color = (255, 0, 0)       # Blue
            prev_x, prev_y = 0, 0

        elif fingers == [1, 1, 1, 0]:      # Index + Middle + Ring
            draw_color = (0, 0, 255)       # Red
            prev_x, prev_y = 0, 0

        # -----------------------
        # BRUSH SIZE CONTROL
        # -----------------------
        elif fingers == [1, 0, 0, 1]:      # Index + Pinky
            brush_thickness = min(brush_thickness + 1, max_brush)

        elif fingers == [1, 0, 1, 0]:      # Index + Ring
            brush_thickness = max(brush_thickness - 1, min_brush)

        # -----------------------
        # DRAWING MODE
        # -----------------------
        elif fingers == [1, 0, 0, 0]:      # Index only
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            cv2.line(
                canvas,
                (prev_x, prev_y),
                (x, y),
                draw_color,
                brush_thickness
            )
            prev_x, prev_y = x, y

        # Draw index finger pointer
        cv2.circle(frame, (x, y), 8, (0, 0, 255), -1)

    # =======================
    # MERGE CANVAS & FRAME
    # =======================
    frame = cv2.add(frame, canvas)

    # UI Info
    cv2.putText(frame, f"Brush: {brush_thickness}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Air Drawing System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# =======================
# CLEANUP
# =======================
cap.release()
cv2.destroyAllWindows()

