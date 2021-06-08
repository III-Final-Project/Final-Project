from flask import request
from flask_restful import Resource
from util.resMsg import ResMsg
from face.faceService import FaceService
import json
import requests
import flask
import os


# 取得customer相關資訊(前端使用）


class UserApi_by_userInfo(Resource):
    def post(self):
        try:
            user_name = request.get_json()['user_name']
            body = {
                "userName": "omg123",
                "userPassword": "?AREyouFrickingKiddingME?!",
                "user_name": user_name
            }
            r = requests.post('http://localhost:4000/users/login', body)
            token = json.loads(r.text)['token']
            headers = {'authorization': 'Bearer {}'.format(token)}
            q = requests.get(
                'http://localhost:4000/users/queryname/{}'.format(user_name), headers=headers)
            user_info = json.loads(q.text)
            user_info['detail'][0]['token'] = token
            return ResMsg(200, user_info['detail']).return_message()
        except Exception as e:
            return ResMsg(500, 'server error').return_message()


class UserApi_by_imgUpload(Resource):
    def post(self):
        try:
            user_img = flask.request.files['image']
            basedir = os.path.abspath(os.path.dirname('__file__'))
            path = basedir + '/static/image/user/{}'.format(user_img.filename)
            user_img.save(path)
            return ResMsg(200, 'upload successfully').return_message()
        except Exception as e:
            return ResMsg(500, json.dumps(e)).return_message()


class UserApi_by_faceDetect(Resource):
    def post(self):
        try:
            picture = request.values['picture'].split(',')[1]
            face = FaceService()
            face.frame = picture
            result = face.face_recognize()
            return ResMsg(200, result).return_message()
        except Exception as e:
            return ResMsg(500, json.dumps(e)).return_message()
