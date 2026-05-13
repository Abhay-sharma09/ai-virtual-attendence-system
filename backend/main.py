from fastapi import FastAPI, Request, Form, Body
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import os
import pandas as pd
import shutil

from recognition import start_recognition
from register_student import register_student

app = FastAPI()



#  BASE PATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#  FRONTEND 
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "frontend", "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "frontend", "static")), name="static")


# HOME 
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# START ATTENDANCE 
@app.get("/start-attendance")
def start_attendance():
    start_recognition()
    return {"message": "Attendance Started"}


#  REGISTER STUDENT 
@app.post("/register-student")
def register(name: str = Form(...), roll: str = Form(...)):

    result = register_student(name, roll)

    if result == "already":
        return {"message": " Already Registered"}

    return {"message": " Registration Successful"}


# DOWNLOAD ATTENDANCE 
@app.get("/attendance-file")
def download_attendance():

    file_path = os.path.join(BASE_DIR, "attendance.xlsx")

    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Name", "Roll", "Timestamp"])
        df.to_excel(file_path, index=False)

    return FileResponse(file_path, filename="attendance.xlsx")


#  REGISTERED STUDENTS 
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

    students.sort(key=lambda x: x["Roll"])

    return {
        "students": students,
        "total": len(students)
    }


#  DELETE STUDENT
import subprocess
import stat

@app.post("/delete-student")
def delete_student(data: dict = Body(...)):

    roll = data.get("roll")
    name = data.get("name")

    folder_name = f"{roll}_{name}"
    dataset_path = os.path.join(BASE_DIR, "dataset", folder_name)

    print("Deleting:", dataset_path)

    def remove_readonly(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    if os.path.exists(dataset_path):

        try:
            shutil.rmtree(dataset_path, onerror=remove_readonly)

            #  RE-GENERATE ENCODINGS
            print("Updating encodings after delete...")
            subprocess.run(["python", "encode_faces.py"])

            return {"message": " Student Deleted & Encodings Updated"}

        except Exception as e:
            return {"message": f" Error: {str(e)}"}

    return {"message": " Student Not Found"}