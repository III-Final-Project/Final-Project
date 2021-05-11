class Azure:
    # Constructor
    def __init__(self):
        # import 第三方套件的寫法
        self.base64 = __import__('base64')
        self.urllib = __import__('urllib')
        self.json = __import__('json')
        self.http = __import__('http')
        self.azure_face_Key = '9f9b446a0ffc4cd8924683536b056d6d'
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
            conn = self.http.client.HTTPSConnection('southeastasia.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/detect?%s" % params, self.photo, headers)
            response = conn.getresponse()
            data = response.read()
            json_obj = self.json.loads(data.decode("UTF-8"))
            self.faceId = json_obj[0]['faceId']
            conn.close()
            return json_obj
        except Exception as e:
            return "[Errno {0}]".format(e)
