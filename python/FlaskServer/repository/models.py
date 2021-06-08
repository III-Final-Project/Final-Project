from .db import db
import mongoengine_goodjson as gj


class Customer(gj.Document):
    # require=True means not null.
    # unique means only one.
    user_name = db.StringField(required=True)  # 前端傳來
    customer_sex = db.StringField(required=True)  # azure 產生
    customer_age = db.StringField(required=True)  # azure 產生
    customer_time = db.StringField(required=True)  # yolo產生
    customer_img_path = db.StringField(required=True)  # yolo產生
    customer_recommend_product = db.StringField(required=True)
    customer_recommend_color = db.StringField(required=True)  # 特徵抽取產生
    customer_recommend_img = db.StringField(required=True)  # 爬蟲後產生
