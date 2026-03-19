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

# ---- Base Path ----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- Frontend Paths ----
templates_path = os.path.join(BASE_DIR, "frontend", "templates")
static_path = os.path.join(BASE_DIR, "frontend", "static")

templates = Jinja2Templates(directory=templates_path)

app.mount("/static", StaticFiles(directory=static_path), name="static")


# ================= HOME =================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ================= START ATTENDANCE =================
@app.get("/start-attendance")
def start_attendance():

    thread = threading.Thread(target=start_recognition)
    thread.start()

    return {"message": "Attendance started"}


# ================= REGISTER STUDENT =================
@app.post("/register-student")
def register_student_api(name: str = Form(...), roll: str = Form(...)):

    thread = threading.Thread(target=register_student, args=(name, roll))
    thread.start()

    return {"message": "Registration started"}


# ================= VIEW ATTENDANCE =================
@app.get("/attendance-file")
def view_attendance():

    file_path = os.path.join(BASE_DIR, "attendance.xlsx")

    # ✅ AUTO CREATE FILE IF NOT EXISTS
    if not os.path.exists(file_path):

        print("Creating attendance file...")

        df = pd.DataFrame(columns=["Name", "Roll", "Timestamp"])
        df.to_excel(file_path, index=False)

    return FileResponse(
        path=file_path,
        filename="attendance.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )