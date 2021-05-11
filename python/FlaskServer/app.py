from flask import Flask, request, Response
from repository.db import initialize_db
from repository.models import User
from face import faceService
from util.resMsg import ResMsg
from flask_cors import CORS
import json
import os
import flask

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
            basedir = os.path.abspath(os.path.dirname(__file__))
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
            face = faceService.FaceId()
            face.frame = picture
            user_name = face.face_detect()
            # user_info_from_db = json.loads(User.objects(user_name=user_name).to_json())[0]
            # print(user_info_from_db)
            returnDic = {'user_name': user_name}
            return ResMsg(200, returnDic).return_message()
    except Exception as e:
        return ResMsg(500, json.dumps(e)).return_message()


app.run(port=5000)
