import pandas as pd
from datetime import datetime, timedelta
import os
from openpyxl import load_workbook

def mark_attendance(name, roll):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    file = os.path.join(BASE_DIR, "attendance.xlsx")

    now = datetime.now()

    roll = str(roll)

    if not os.path.exists(file):

        df = pd.DataFrame(columns=["Name","Roll","Timestamp"])
        df.loc[len(df)] = [name, roll, now]
        df.to_excel(file, index=False)

    else:

        df = pd.read_excel(file)

        df["Roll"] = df["Roll"].astype(str)
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])

        student = df[df["Roll"] == roll]

        if not student.empty:

            last_time = student.iloc[-1]["Timestamp"]

            if now - last_time < timedelta(minutes=50):

                print("Attendance already marked")
                return False

        df.loc[len(df)] = [name, roll, now]
        df.to_excel(file, index=False)

    # Format Excel

    wb = load_workbook(file)
    ws = wb.active

    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 30

    wb.save(file)

    print("Attendance Marked")

    return True