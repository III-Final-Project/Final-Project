from resources.customer import CustomerApi_by_id, CustomerApi_by_username, CustomerApi_fashion_recommend
from resources.user import UserApi_by_faceDetect, UserApi_by_imgUpload, UserApi_by_userInfo


def initialize_routes(api):
    api.add_resource(CustomerApi_by_id, '/api/customer/<id>')
    api.add_resource(CustomerApi_by_username, '/api/customer/query/<user_name>')
    api.add_resource(CustomerApi_fashion_recommend, '/api/customer/fashion')
    api.add_resource(UserApi_by_userInfo, '/api/user')
    api.add_resource(UserApi_by_imgUpload, '/api/user/img_upload')
    api.add_resource(UserApi_by_faceDetect, '/api/user/face')

