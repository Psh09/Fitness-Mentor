# AI-BASED FITNESS MENTOR

This project was a 3rd year, semester 6 mini-project. It provides a personalized and accessible solution to modern fitness challenges by leveraging artificial intelligence to guide users and improve workout effectiveness. It addresses common issues like improper exercise form, which can lead to injury, and the lack of personalized guidance that can hinder progress.

---

### Key Features

* **Real-time Posture Correction:** The system uses computer vision to detect and correct a user's posture during exercises.
* **Repetition Counting:** It automatically monitors and counts the number of repetitions completed for each exercise.
* **Adaptive Workouts:** The AI can design comprehensive workout routines tailored to individual fitness levels and goals.
* **Comprehensive Exercise Library:** The system tracks progress for a variety of fundamental exercises, including biceps curls, shoulder presses, squats, push-ups, deadlifts, and lunges.

---

### Technologies Used

#### Software
* **Programming Language:** Python
* **Libraries:** OpenCV, TensorFlow/PyTorch
* **Pose Estimation Model:** MediaPipe

#### Hardware
* **Input:** Webcam
* **Processor:** Multi-core CPU
* **RAM:** Minimum 8GB

---

### System Architecture

The system is designed to automatically count exercise repetitions using a webcam. It begins by capturing a video feed, which is then processed frame-by-frame. These frames are analyzed by a Pose Detection Module that identifies key body landmarks. The system then uses a Joint Angle Calculation Module to determine the angles between relevant joints, which are used by a Repetition Counting Module to track and count repetitions. This system leverages computer vision and pose estimation techniques to provide accurate real-time feedback.

---

### Project Team

This project was a mini-project for the B.E in Computer Engineering at Pillai HOC College of Engineering and Technology.


* **Prajwal Shivputra Halle**
* Sarthak Santosh Hasbe
* Smitesh Sangmesh Gajakosh
* Prathmesh Santosh Chaudhari
