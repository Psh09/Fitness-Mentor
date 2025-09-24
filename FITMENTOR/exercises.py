import cv2
import mediapipe as mp
import time
from tkinter import messagebox

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    import numpy as np
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - \
              np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180:
        angle = 360 - angle
    return angle

def run_exercise(exercise_name):
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Webcam not accessible. Please check your camera.")
            return

        counter = 0
        stage = None
        start_time = time.time()

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = pose.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                try:
                    landmarks = results.pose_landmarks.landmark

                    if exercise_name == "Squats":
                        hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                        knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                        ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                        angle = calculate_angle(hip, knee, ankle)

                        if angle < 90:
                            stage = "down"
                        if angle > 160 and stage == "down":
                            stage = "up"
                            counter += 1

                    elif exercise_name == "Biceps":
                        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                        elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                        wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                        angle = calculate_angle(shoulder, elbow, wrist)

                        if angle > 150:
                            stage = "down"
                        if angle < 30 and stage == "down":
                            stage = "up"
                            counter += 1

                    elif exercise_name == "Lunges":
                        hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                        knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                        ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                                 landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                        angle = calculate_angle(hip, knee, ankle)

                        if angle < 90:
                            stage = "down"
                        if angle > 160 and stage == "down":
                            stage = "up"
                            counter += 1

                    elif exercise_name == "Shoulders":
                        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                        elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                        wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                        angle = calculate_angle(shoulder, elbow, wrist)

                        if angle > 160:
                            stage = "down"
                        if angle < 60 and stage == "down":
                            stage = "up"
                            counter += 1

                    elif exercise_name == "Jumping Jacks":
                        left_hand = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
                        right_hand = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
                        left_foot = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
                        right_foot = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]

                        hands_up = left_hand.y < 0.4 and right_hand.y < 0.4
                        legs_apart = abs(left_foot.x - right_foot.x) > 0.4

                        if hands_up and legs_apart:
                            stage = "open"
                        if not hands_up and not legs_apart and stage == "open":
                            stage = "close"
                            counter += 1

                    cv2.putText(image, f'{exercise_name} Reps: {counter}', (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                except Exception as e:
                    print("Error processing frame:", e)

                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                cv2.imshow(exercise_name, image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Exercise Completed", f"You completed {counter} {exercise_name} reps!")

    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))
