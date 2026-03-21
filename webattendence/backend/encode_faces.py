import face_recognition
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(BASE_DIR, "dataset")

known_encodings = []
names = []
rolls = []

for folder in os.listdir(dataset_path):

    path = os.path.join(dataset_path, folder)

    if os.path.isdir(path) and "_" in folder:

        roll, name = folder.split("_",1)

        for img_name in os.listdir(path):

            img_path = os.path.join(path, img_name)

            image = face_recognition.load_image_file(img_path)

            encodings = face_recognition.face_encodings(image)

            if len(encodings)>0:

                known_encodings.append(encodings[0])
                names.append(name)
                rolls.append(roll)

data = {
    "encodings": known_encodings,
    "names": names,
    "rolls": rolls
}

encodings_dir = os.path.join(BASE_DIR,"encodings")

os.makedirs(encodings_dir, exist_ok=True)

with open(os.path.join(encodings_dir,"encodings.pickle"),"wb") as f:
    pickle.dump(data,f)

print("Encodings created successfully")