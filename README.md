# AI Virtual Attendance System

## Overview

AI Virtual Attendance System is a Full Stack AI-powered web application that automates attendance using real-time face recognition. Students can register their facial data, which is converted into facial encodings for identification through a webcam. The system automatically records attendance with timestamps while preventing duplicate entries, providing an efficient and reliable alternative to manual attendance management.

## Features

- Student Registration
- Real-Time Face Recognition
- Automatic Attendance Marking
- Duplicate Attendance Prevention
- Face Encoding Generation
- Student Search & Delete
- Download Attendance Records
- Responsive Dark-Themed UI

## Tech Stack

**Frontend:** HTML, CSS, JavaScript  
**Backend:** Python, FastAPI, Uvicorn  
**AI / Computer Vision:** OpenCV, face_recognition, dlib  
**Data Handling:** pandas, openpyxl

## Installation & Run

```bash
git clone <repository-url>
cd webattendence/backend
pip install fastapi uvicorn opencv-python face-recognition pandas openpyxl
python -m uvicorn main:app --reload --port 8001
```

Open your browser and visit:

```text
http://127.0.0.1:8001
```

## Future Improvements

- User Authentication
- Database Integration
- Cloud Deployment
- Analytics Dashboard
- Enhanced Mobile Responsiveness


