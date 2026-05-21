# Motion-Detector
A Python-based real-time motion detection system using OpenCV's MOG2 background subtraction algorithm. Works with both live webcam feed and pre-recorded video files.
---

## 📌 Features

* Real-time motion detection
* Webcam support
* Video file support
* Background subtraction using MOG2
* Noise reduction using Gaussian Blur
* Bounding boxes around moving objects
* Motion status display

---

## 🛠 Technologies Used

* Python
* OpenCV (`cv2`)
* NumPy

---

# 📂 Project Structure

```bash
Motion-Detector-main/
│
├── main.py
├── README.md
└── sample_video.mp4   # optional
```

---

# ▶️ How It Works

The program:

1. Captures video frames
2. Converts frames to grayscale
3. Applies Gaussian blur to remove noise
4. Uses background subtraction to detect movement
5. Finds contours of moving objects
6. Draws rectangles around detected motion
7. Displays motion status on screen

---

# 🚀 Installation

## Step 1: Install Python

Download Python from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## Step 2: Install Required Libraries

Open terminal or command prompt and run:

```bash
pip install opencv-python numpy
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🎥 Webcam Mode

Inside `main.py`:

```python
SOURCE = 0
```

`0` means default webcam.

---

# 📹 Video File Mode

```python
SOURCE = "sample_video.mp4"
```

Place your video file inside the project folder.

---

# 🧠 Main Motion Detection Logic

```python
fgmask = mog.apply(gray)
```

This line compares the current frame with the background and detects changes.

---

# 📦 Example Output

* Green rectangles around moving objects
* Text:

```text
MOTION DETECTED
```

or

```text
No Motion
```
---

https://github.com/user-attachments/assets/e07109b0-8fea-418a-9b1f-71ca034069c0
