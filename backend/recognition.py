import face_recognition
import pickle
import cv2
import os

from attendence import mark_attendance
from register_student import register_student


def start_recognition():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    encodings_path = os.path.join(BASE_DIR, "encodings", "encodings.pickle")

    print("Loading encodings...")
    data = pickle.load(open(encodings_path, "rb"))
    print("Encodings loaded successfully")

    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    processed_rolls = set()
    message = ""

    while True:

        ret, frame = video.read()
        if not ret:
            break

        # Resize frame (optional performance improvement)
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)

        for (top, right, bottom, left), face_encoding in zip(faces, encodings):

            # Adjust back to original frame size
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2

            name = "Unknown"
            roll = ""

            if len(data["encodings"]) > 0:

                # 🔥 NEW: Distance-based matching
                distances = face_recognition.face_distance(data["encodings"], face_encoding)

                min_distance = min(distances)
                idx = distances.tolist().index(min_distance)

                # 🔥 STRICT THRESHOLD
                if min_distance < 0.45:

                    name = data["names"][idx]
                    roll = str(data["rolls"][idx])

                    if roll not in processed_rolls:

                        marked = mark_attendance(name, roll)

                        if marked:
                            message = "Attendance Marked"
                        else:
                            message = "Already Marked"

                        processed_rolls.add(roll)

                    color = (0, 255, 0)

                else:
                    name = "Unknown / Press N to Register"
                    color = (0, 0, 255)

            else:
                name = "No Data Found"
                color = (0, 0, 255)

            # Draw box
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

            # Put name text
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Show message
        cv2.putText(frame, message, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        cv2.imshow("AI Attendance System", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break

        # 🔥 Press N to register
        if key == ord("n"):

            video.release()
            cv2.destroyAllWindows()

            print("\nRegister New Student")

            name = input("Enter student name: ")
            roll = input("Enter roll number: ")

            register_student(name, roll)

            break

    video.release()
    cv2.destroyAllWindows()