from flask import Flask, request, Response
from repository.db import initialize_db
from repository.models import User
from face.faceService import FaceService
from util.resMsg import ResMsg
from flask_cors import CORS
import json
import os
import flask
import face_recognition
import base64
import numpy as np
import cv2

app = Flask(__name__)
cors = CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/user-info'
}
initialize_db(app)


@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_info():
    try:
        if request.method == 'GET':
            users = User.objects().to_json()
            result = json.loads(users)
            return ResMsg(200, result).return_message()
        elif request.method == 'POST':
            body = request.get_json()
            User(**body).save()
            return ResMsg(200, 'Created Success').return_message()
        # 給定userid即可以更新想更新的資料
        elif request.method == 'PUT':
            body = request.get_json()
            user_id = body['user_id']
            User.objects.get(user_id=user_id).update(**body)
            return ResMsg(200, 'Updated Success').return_message()
        elif request.method == 'DELETE':
            body = request.get_json()
            user_id = body['user_id']
            User.objects.get(user_id=user_id).delete()
            return ResMsg(200, 'Deleted Success').return_message()
    except Exception:
        return ResMsg(500, 'Server Error').return_message()


@app.route('/img_upload', methods=['POST'])
def img_upload():
    try:
        if request.method == 'POST':
            user_img = flask.request.files['image']
            print(user_img)
            basedir = os.path.abspath(os.path.dirname('__file__'))
            path = basedir + '/static/image/{}'.format(user_img.filename)
            user_img.save(path)
            return ResMsg(200, 'upload successfully').return_message()
    except Exception as e:
        return ResMsg(500, json.dumps(e)).return_message()


@app.route('/face', methods=['POST'])
def face_id():
    try:
        if request.method == 'POST':
            picture = request.values['picture'].split(',')[1]
            # using face service
            face = FaceService()
            face.frame = picture
            result = face.face_recognize()
            return ResMsg(200, result).return_message()
    except Exception as e:
        return ResMsg(500, json.dumps(e)).return_message()


@app.route('/testing', methods=['POST'])
def testing():
    if request.method == 'POST':
        frame = request.values['picture'].split(',')[1]
        # Thread(target=testing, args=(frame,)).start()
    return 'ok'


def testing_me(frame):
    michael_image = face_recognition.load_image_file("static/image/michael.jpg")
    michael_face_encoding = face_recognition.face_encodings(michael_image)[0]
    known_face_encodings = [michael_face_encoding]
    known_face_names = ["Michael"]

    process_this_frame = True

    while True:
        pict_byte = base64.b64decode(frame)
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
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    face_locations = list(face_locations[0])
                    my_new_list = [i * 4 for i in face_locations]
                    return_obj = {'name': name, 'face_location': my_new_list}
                    return return_obj


# app.run(host='0.0.0.0', port=5000, threaded=False)
# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0', port=5000, threaded=False)
