from repository.models import Customer
from flask import request,Response
from flask_restful import Resource
from util.resMsg import ResMsg
import json
import cv2
from fashionService.fashionRecommendService import *

# query data by user_name
class CustomerApi_by_username(Resource):
    def get(self, user_name):
        customers = Customer.objects.filter(user_name=user_name).to_json()
        result = json.loads(customers)
        if result is None or len(result) == 0:
            return ResMsg(404, 'Data not fund').return_message()
        else:
            return ResMsg(200, result).return_message()

# get,put,delete by id
class CustomerApi_by_id(Resource):
    def get(self, id):
        customer = Customer.objects.get(id=id).to_json()
        result = json.loads(customer)
        if result is None or len(result) == 0:
            return ResMsg(404, 'Data not fund').return_message()
        else:
            return ResMsg(200, result).return_message()

    def put(self, id):
        try:
            body = request.get_json()
            Customer.objects.get(id=id).update(**body)
            return ResMsg(200, 'Updated successfully').return_message()
        except Exception:
            return ResMsg(404, 'id not fund').return_message()

    def delete(self, id):
        try:
            Customer.objects.get(id=id).delete()
            return ResMsg(200, 'ok').return_message()
        except Exception:
            return ResMsg(404, 'id not fund').return_message()


class CustomerApi_fashion_recommend(Resource):
    def post(self):
        try:
            user_name = request.get_json()['user_name']
            model, names, colors = initNet()
            cap = cv2.VideoCapture(0)
            ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / \
                cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            WIDTH = 400
            HEIGHT = int(WIDTH / ratio)
            # 計算yolo判斷物件次數而截圖
            count = 0
            return Response(gen_Video(cap, WIDTH, HEIGHT, model, count, user_name),
                            mimetype='multipart/x-mixed-replace; boundary=frame')
        except Exception as e:
            return ResMsg(500, '{}'.format(e)).return_message()
