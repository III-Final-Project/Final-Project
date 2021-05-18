import face_recognition
import cv2
import numpy as np
import base64
import os


class FaceService:
    def __init__(self):
        self.frame = None
        self.image_file = 'static/image'

    def file_reader(self):
        return os.listdir(self.image_file)

    def face_recognize(self):
        image_list = self.file_reader()
        known_face_encodings = []
        known_face_names = []
        for image in image_list:
            user_image = face_recognition.load_image_file(self.image_file + '/' + image)  # 讀成BGR三維格式，opencv的格式
            user_face_encoding = face_recognition.face_encodings(user_image)[0]  # 將圖片做normalize
            known_face_encodings.append(user_face_encoding)
            user_name = image.split('.')[0]
            known_face_names.append(user_name)

        process_this_frame = True

        while True:
            pict_byte = base64.b64decode(self.frame)
            img_array = np.frombuffer(pict_byte, dtype=np.uint8)
            cv2_img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(cv2_img, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                name = 'Unknown'
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    # # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                    face_locations = list(face_locations[0])
                    my_new_list = [i * 4 for i in face_locations]
                    return_obj = {'name': name, 'face_location': my_new_list}
                    return return_obj
