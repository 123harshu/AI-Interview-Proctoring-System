# 👁️ AI-Interview-Proctoring-System

An AI-based real-time eye contact and attention tracking system built using **Python**, **OpenCV**, and **MediaPipe**. The application monitors user attention by detecting head movements, face presence, and multiple faces, making it suitable for online interview proctoring and attention monitoring.

---

## 🚀 Features

- ✅ Real-time Face Detection
- ✅ Face Mesh Detection using MediaPipe
- ✅ Head Movement Tracking
  - Left
  - Right
  - Up
  - Down
  - Center
- ✅ Attention Monitoring
- ✅ Multiple Face Detection Warning
- ✅ Distraction Counter
- ✅ Live Webcam Monitoring
- ✅ Smooth Face Tracking for Stable Detection

---

## 🛠️ Tech Stack

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

---

## 📂 Project Structure

```
EyeContactAI1/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── utils/
│   ├── attention.py
│   └── gaze.py
└── assets/
    ├── screenshot.png
    └── demo.gif
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/123harshu/EyeContactAI1.git
cd EyeContactAI1
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 📸 Output

### Face Detection

> Detects the user's face using MediaPipe Face Mesh.

### Head Direction Tracking

Displays the current head direction:

- LEFT
- RIGHT
- UP
- DOWN
- CENTER

### Multiple Face Detection

Shows a warning if more than one face is detected.

### Attention Monitoring

Counts distractions whenever the user looks away from the screen.

---

## 🎯 Future Improvements

- Eye Gaze Estimation
- Face Not Detected Alert
- Drowsiness Detection
- Blink Detection
- Mobile Phone Detection
- Session Report Generation
- PDF Report
- Flask Web Interface
- YOLO-based Object Detection

---

## 📷 Demo <img width="803" height="556" alt="image" src="https://github.com/user-attachments/assets/187d1551-0330-4ddc-9547-85071554515d" />


> Add screenshots or GIFs inside the **assets/** folder.

Example:

```
assets/
    screenshot.png
    demo.gif
```

---

## 💡 Applications

- AI Interview Proctoring
- Online Examination Monitoring
- Attention Tracking
- Student Monitoring
- Human-Computer Interaction
- Computer Vision Projects

---

## 👩‍💻 Author

**Harshita Verma**

- GitHub: https://github.com/123harshu

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.
