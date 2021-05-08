class FaceId:
    def __init__(self):
        self.face_recognition = __import__('face_recognition')
        self.cv2 = __import__('cv2')
        self.np = __import__('numpy')
        self.base64 = __import__('base64')
        self.os = __import__('os')
        self.frame = None
        self.image_file = 'static/image'

    def file_reader(self):
        return self.os.listdir(self.image_file)

    def face_detect(self):
        image_list = self.file_reader()
        known_face_encodings = []
        known_face_names = []

        for image in image_list:
            user_image = self.face_recognition.load_image_file(self.image_file + '/' + image)  # 讀成BGR三維格式，opencv的格式
            user_face_encoding = self.face_recognition.face_encodings(user_image)[0]  # 將圖片做normalize
            known_face_encodings.append(user_face_encoding)
            user_name = image.split('.')[0]
            known_face_names.append(user_name)

        process_this_frame = True

        while True:
            pict_byte = self.base64.b64decode(self.frame)
            img_array = self.np.frombuffer(pict_byte, dtype=self.np.uint8)
            cv2_img = self.cv2.imdecode(img_array, self.cv2.COLOR_BGR2RGB)

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = self.cv2.resize(cv2_img, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = self.face_recognition.face_locations(rgb_small_frame)
                face_encodings = self.face_recognition.face_encodings(rgb_small_frame, face_locations)

                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = self.face_recognition.compare_faces(known_face_encodings, face_encoding)
                    # # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                        return name
                    else:
                        return 'Unknown'
