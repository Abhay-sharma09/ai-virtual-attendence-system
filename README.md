# AI Virtual Attendance System

## Overview

The AI Virtual Attendance System is a Ai+full-stack application that automates attendance marking using face recognition technology. It captures student facial data, generates encodings, performs real-time recognition through a webcam, and records attendance in a structured format.

This project combines computer vision, backend API development, and frontend UI design to create a practical and scalable attendance solution.

---

## Features

### 1. Student Registration

* Register students using name and roll number
* Capture multiple face images(20 images) using webcam
* Store images in a structured dataset directory
* Prevent duplicate registrations

### 2. Face Encoding System

* Convert face images into numerical encodings
* Store encodings using pickle format
* Automatically update encodings after registration or deletion

### 3. Real-Time Face Recognition

* Detect faces using webcam
* Match detected faces with stored encodings
* Display recognized and unrecognized faces
* Use distance-based matching with threshold control

### 4. Smart Attendance System

* Automatically mark attendance with timestamp
* Prevent duplicate entries within a defined time interval (50 min)
* Store attendance data in Excel format

### 5. Attendance Management

* Automatically create attendance file if not present
* Store name, roll number, and timestamp
* Download attendance file from UI in just 1 click

### 6. Student Dashboard

* View all registered students
* Display student name and roll number
* Sorted list for better readability

### 7. Search Functionality

* Real-time search by name or roll number
* Dynamic filtering without page reload

### 8. Delete Student

* Remove student from dataset
* Delete all associated images
* Automatically regenerate face encodings
* Handle file permission and path issues

### 9. UI Features

* Dark themed modern interface
* Glass-style components
* Consistent color system
* Styled tables and forms
* Responsive layout structure

### 10. System Stability

* Error handling for file operations
* Safe folder creation
* Backend API validation
* Robust data handling

---

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript (Fetch API, DOM manipulation)

### Backend

* FastAPI
* Uvicorn

### AI / Computer Vision

* OpenCV
* face_recognition
* dlib

### Data Handling

* pandas
* openpyxl

### Storage

* Excel file (attendance.xlsx)
* Dataset folder
* Encodings (pickle file)

---

## Python Libraries Used

* os
* shutil
* subprocess
* datetime
* pickle
* cv2 (OpenCV)
* face_recognition
* pandas
* openpyxl

---

## Project Structure

webattendence/
│
├── backend/
│   ├── main.py
│   ├── recognition.py
│   ├── register_student.py
│   ├── encode_faces.py
│   ├── attendence.py
│
├── frontend/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│       ├── style.css
│       └── script.js
│
├── dataset/
├── encodings/
├── attendance.xlsx

---

## Installation and Setup



1. Navigate to project directory:
   cd webattendence/backend

2. Install dependencies:
   pip install fastapi uvicorn opencv-python face-recognition pandas openpyxl

3. Run the server:
   python -m uvicorn main:app --reload --port 8001

4. Open browser:
   http://127.0.0.1:8001

---

## Usage

1. Register a student by entering name and roll number
2. Capture face images via webcam
3. Start attendance to detect and recognize faces
4. Attendance will be automatically recorded
5. View or search registered students
6. Delete students if needed
7. Download attendance file

---

## Key Highlights

* Full-stack implementation
* Real-time face recognition system
* Automated attendance tracking
* Duplicate prevention logic
* Clean and modern UI
* Modular backend architecture

---

## Future Improvements

* Add authentication system
* Integrate database (SQLite/MySQL)
* Deploy application online
* Add analytics dashboard
* Implement browser-based camera access
* Export reports in PDF format
* Improve mobile responsiveness

---


