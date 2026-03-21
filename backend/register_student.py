import os
import cv2
import subprocess

def register_student(name, roll):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(BASE_DIR, "dataset")

    # Create folder name
    folder_name = f"{roll}_{name}"
    student_path = os.path.join(dataset_path, folder_name)

    # 🔥 CHECK IF ALREADY REGISTERED
    if os.path.exists(student_path):
        print("⚠ Already Registered")
        return "already"

    # Create dataset folder
    os.makedirs(student_path, exist_ok=True)

    cap = cv2.VideoCapture(0)

    count = 0
    print("Capturing images...")

    while count < 20:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Register Face", frame)

        img_path = os.path.join(student_path, f"{count}.jpg")
        cv2.imwrite(img_path, frame)

        count += 1

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Images captured:", count)

    # 🔥 UPDATE ENCODINGS
    print("Updating encodings...")
    subprocess.run(["python", "encode_faces.py"])

    return "registered"