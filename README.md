# AI Virtual Attendance System

## About The Project

AI Virtual Attendance System is a Full Stack + AI based web application that automates attendance marking using real-time face recognition technology.

The system captures student face data, generates facial encodings, performs live recognition through webcam, and automatically stores attendance records with timestamps.

The project combines Computer Vision, FastAPI backend development, and modern frontend UI design to create a smart and scalable attendance solution.

---

# Features

- Student Registration System
- Real-Time Face Recognition
- Automatic Attendance Marking
- Duplicate Attendance Prevention
- Face Encoding Generation
- Student Search Functionality
- Delete Student Feature
- Download Attendance File
- Dark Themed Responsive UI
- Excel Based Attendance Storage

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Python
- FastAPI
- Uvicorn

## AI / Computer Vision
- OpenCV
- face_recognition
- dlib

## Data Handling
- pandas
- openpyxl

---

# Installation

```bash
git clone <your-repository-link>
cd webattendence/backend
pip install fastapi uvicorn opencv-python face-recognition pandas openpyxl
```

---

# How To Run The Project

## Start Backend Server

```bash
python -m uvicorn main:app --reload --port 8001
```

Open in Browser:

```text
http://127.0.0.1:8001
```

---

# Future Improvements

- Add Authentication System
- Database Integration
- Cloud Deployment
- Analytics Dashboard
- Mobile Responsive Improvements


