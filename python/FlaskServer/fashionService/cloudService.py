class Cloud:
    # Constructor
    def __init__(self):
        # import 第三方套件的寫法
        self.base64 = __import__('base64')
        self.urllib = __import__('urllib')
        self.json = __import__('json')
        self.http = __import__('http')
        self.requests = __import__('requests')
        self.azure_face_Key = 'fa4c14d188ac4ada81b57efcfca0a574'
        self.photo = None
        self.faceId = ''
        self.faceId_list = []
        self.face_attributes = 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,' \
                               'accessories,blur,exposure,noise'

    def face_detect_by_byte(self):
        headers = {
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.azure_face_Key
        }
        params = self.urllib.parse.urlencode({
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': self.face_attributes
        })
        try:
            conn = self.http.client.HTTPSConnection('eastasia.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/detect?%s" % params, self.base64.b64decode(self.photo), headers)
            response = conn.getresponse()
            data = response.read()
            json_obj = self.json.loads(data.decode("UTF-8"))
            conn.close()
            return json_obj  # array
        except Exception as e:
            return "[Error]:{}".format(e)

    def google_fashion_detect(self):
        try:
            r = self.requests.post('http://localhost:4000/users/suitdetect', data={'image': self.photo})
            result = self.json.loads(r.text)
            return result['detail']  # array
        except Exception as e:
            return "[Error]:{}".format(e)

    def combination_service(self):
        result_from_google = self.google_fashion_detect()
        result_from_azure = self.face_detect_by_byte()
        fashion_data = self.json.dumps(result_from_azure + result_from_google)
        # print(fashion_data)
        return fashion_data
