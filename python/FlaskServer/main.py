from flask import Flask, request, Response
# from repository.db import initialize_db
# from repository.models import User
from face.faceService import FaceService
from cloud.cloudService import Cloud
from util.resMsg import ResMsg
from flask_cors import CORS
import json
import os
import requests
import flask

app = Flask(__name__)
cors = CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/user-info'
}


# initialize_db(app)


# @app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def user_info():
#     try:
#         if request.method == 'GET':
#             users = User.objects().to_json()
#             result = json.loads(users)
#             return ResMsg(200, result).return_message()
#         elif request.method == 'POST':
#             body = request.get_json()
#             User(**body).save()
#             return ResMsg(200, 'Created Success').return_message()
#         # 給定userid即可以更新想更新的資料
#         elif request.method == 'PUT':
#             body = request.get_json()
#             user_id = body['user_id']
#             User.objects.get(user_id=user_id).update(**body)
#             return ResMsg(200, 'Updated Success').return_message()
#         elif request.method == 'DELETE':
#             body = request.get_json()
#             user_id = body['user_id']
#             User.objects.get(user_id=user_id).delete()
#             return ResMsg(200, 'Deleted Success').return_message()
#     except Exception:
#         return ResMsg(500, 'Server Error').return_message()


@app.route('/img_upload', methods=['POST'])
def img_upload():
    try:
        if request.method == 'POST':
            user_img = flask.request.files['image']
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
            face = FaceService()
            face.frame = picture
            result = face.face_recognize()
            return ResMsg(200, result).return_message()
    except Exception as e:
        return ResMsg(500, json.dumps(e)).return_message()


@app.route('/cloud', methods=['POST'])
def cloud_service():
    try:
        if request.method == 'POST':
            img_b64 = request.values['picture'].split(',')[1]  # base64
            cloud = Cloud()
            cloud.photo = img_b64
            fashion_data = cloud.combination_service()
            return ResMsg(200, fashion_data).return_message()
    except Exception as e:
        print(e)
        return ResMsg(500, 'server error').return_message()


@app.route('/userinfo', methods=['POST'])
def query_userinfo():
    try:
        if request.method == 'POST':
            user_name = request.get_json()['user_name']
            body = {
                "userName": "omg123",
                "userPassword": "?AREyouFrickingKiddingME?!",
                "user_name": user_name
            }
            r = requests.post('http://localhost:4000/users/login', body)
            token = json.loads(r.text)['token']
            headers = {'authorization': 'Bearer {}'.format(token)}
            q = requests.get('http://localhost:4000/users/queryname/{}'.format(user_name), headers=headers)
            user_info = json.loads(q.text)
            user_info['detail'][0]['token'] = token
            print(user_info['detail'])
            return ResMsg(200, user_info['detail']).return_message()
    except Exception as e:
        print(e)
        return ResMsg(500, 'server error').return_message()


app.run(port=5000, debug=True)