from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import os
import threading
import pandas as pd

from recognition import start_recognition
from register_student import register_student

app = FastAPI()

# ================= BASE PATH =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ================= FRONTEND =================
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "frontend", "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "frontend", "static")), name="static")


# ================= HOME =================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ================= START ATTENDANCE =================
@app.get("/start-attendance")
def start_attendance():
    threading.Thread(target=start_recognition).start()
    return {"message": "Attendance Started"}


# ================= REGISTER STUDENT =================
@app.post("/register-student")
def register(name: str = Form(...), roll: str = Form(...)):
    threading.Thread(target=register_student, args=(name, roll)).start()
    return {"message": "Registration Started"}


# ================= DOWNLOAD ATTENDANCE =================
@app.get("/attendance-file")
def download_attendance():

    file_path = os.path.join(BASE_DIR, "attendance.xlsx")

    # Auto-create file if missing
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Name", "Roll", "Timestamp"])
        df.to_excel(file_path, index=False)

    return FileResponse(file_path, filename="attendance.xlsx")


# ================= REGISTERED STUDENTS (FROM DATASET) =================
@app.get("/student-data")
def student_data():

    dataset_path = os.path.join(BASE_DIR, "dataset")

    if not os.path.exists(dataset_path):
        return {"students": [], "total": 0}

    students = []

    for folder in os.listdir(dataset_path):

        if "_" in folder:
            roll, name = folder.split("_", 1)

            students.append({
                "Name": name,
                "Roll": roll
            })

    return {
        "students": students,
        "total": len(students)
    }