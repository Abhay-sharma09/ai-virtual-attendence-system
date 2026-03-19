import cv2
import os
import subprocess


def register_student(name, roll):

    print("Starting registration...")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    dataset_path = os.path.join(BASE_DIR, "dataset")

    folder = os.path.join(dataset_path, f"{roll}_{name}")

    if not os.path.exists(folder):
        os.makedirs(folder)

    cam = cv2.VideoCapture(0)

    count = 0

    while count < 20:

        ret, frame = cam.read()

        cv2.imshow("Register Student", frame)

        img_path = os.path.join(folder, f"img{count}.jpg")

        cv2.imwrite(img_path, frame)

        count += 1

        if cv2.waitKey(200) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

    encode_path = os.path.join(BASE_DIR, "backend", "encode_faces.py")

    subprocess.run(["py", "-3.10", encode_path])

    print("Student registered")