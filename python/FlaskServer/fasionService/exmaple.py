from cloudService import Cloud
import base64

picture = "static/image/test1.jpg"

with open(picture, 'rb')as f:
    img_b64 = base64.b64encode(f.read())
    img_b64 = img_b64.decode('UTF-8')
cloud = Cloud()
cloud.photo = img_b64
fashion_data = cloud.combination_service()
print(fashion_data)
