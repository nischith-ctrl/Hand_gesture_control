import cv2
import mediapipe as mp
import pyautogui
import math
import time

cap = cv2.VideoCapture(1)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

# Control variables
last_click = 0
last_scroll = 0

scroll_up_count = 0
scroll_down_count = 0

CLICK_COOLDOWN = 1
SCROLL_COOLDOWN = 0.6

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        lm = hand.landmark

        # Key points
        thumb_tip = lm[4]
        index_tip = lm[8]
        index_pip = lm[6]

        middle_tip = lm[12]
        middle_pip = lm[10]

        # ---------------- CURSOR CONTROL ----------------
        cursor_x = screen_w * index_tip.x
        cursor_y = screen_h * index_tip.y

        pyautogui.moveTo(cursor_x, cursor_y, duration=0.05)

        # ---------------- CLICK GESTURE ----------------
        distance = math.hypot(
            (index_tip.x - thumb_tip.x) * w,
            (index_tip.y - thumb_tip.y) * h
        )

        if distance < 30:
            if time.time() - last_click > CLICK_COOLDOWN:
                pyautogui.click()
                last_click = time.time()
                cv2.putText(frame, "CLICK", (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # ---------------- FINGER STATES ----------------
        index_up = index_tip.y < index_pip.y
        middle_up = middle_tip.y < middle_pip.y

        # ---------------- SCROLL UP (stable trigger) ----------------
        if index_up and middle_up:
            scroll_up_count += 1
            scroll_down_count = 0
        else:
            scroll_up_count = 0

        if scroll_up_count >= 5:
            if time.time() - last_scroll > SCROLL_COOLDOWN:
                pyautogui.scroll(60)
                last_scroll = time.time()
                scroll_up_count = 0
                cv2.putText(frame, "SCROLL UP", (20, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # ---------------- SCROLL DOWN (stable trigger) ----------------
        if (not index_up) and (not middle_up):
            scroll_down_count += 1
            scroll_up_count = 0
        else:
            scroll_down_count = 0

        if scroll_down_count >= 5:
            if time.time() - last_scroll > SCROLL_COOLDOWN:
                pyautogui.scroll(-60)
                last_scroll = time.time()
                scroll_down_count = 0
                cv2.putText(frame, "SCROLL DOWN", (20, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("AI Hand Gesture Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows