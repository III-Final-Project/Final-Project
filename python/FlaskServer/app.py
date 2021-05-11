from flask import Flask, request, Response
from repository.db import initialize_db
from repository.models import User
from face import faceService
import os
import json
import base64
import numpy as np
from flask_cors import CORS

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
            return Response(users, status=200, mimetype='application/json')
        elif request.method == 'POST':
            body = request.get_json()
            user = User(**body).save()
            return_object = {'returnCode': '200', 'details': []}
            return_object['details'].append(body)
            result = json.dumps(return_object)
            return Response(result, status=200)
        # 給定userid即可以更新想更新的資料
        elif request.method == 'PUT':
            body = request.get_json()
            user_id = body['user_id']
            User.objects.get(user_id=user_id).update(**body)
            return_object = {'returnCode': '200', 'message': 'updated successful'}
            result = json.dumps(return_object)
            return Response(result, status=200)
        elif request.method == 'DELETE':
            body = request.get_json()
            user_id = body['user_id']
            User.objects.get(user_id=user_id).delete()
            return_object = {'returnCode': '200', 'message': 'deleted successful'}
            result = json.dumps(return_object)
            return Response(result, status=200)
    except Exception as e:
        return Response(json.dumps(e), status=500)


@app.route('/face', methods=['POST'])
def face_id():
    try:
        if request.method == 'POST':
            picture = request.values['picture'].split(',')[1]
            # using face service
            face = faceService.FaceId()
            face.frame = picture
            user_name = face.face_detect()
            return_object = {'returnCode': '200', 'username': user_name}
            result = json.dumps(return_object)
            return Response(result, status=200)
    except Exception as e:
        return Response(json.dumps(e), status=500)


app.run(port=5000)
