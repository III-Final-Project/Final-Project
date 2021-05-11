class ResMsg:
    def __init__(self, status, obj):
        from flask import Response
        import json

        self.Response = Response
        self.json = json
        self.details = []
        self.obj = obj
        self.code = '200'
        self.status = status
        if status != 200:
            self.code = str(status)

    def return_message(self):
        try:
            if type(self.obj) == str:
                try:
                    self.obj = self.json.loads(self.obj, encoding='utf-8')
                    return_object = {'returnCode': self.code, 'details': self.obj}
                    return self.Response(return_object, status=self.status)
                except Exception as e:
                    return_object = {'returnCode': self.code, 'message': self.obj}
                    result = self.json.dumps(return_object)
                    return self.Response(result, status=self.status)
            elif type(self.obj) == list:
                return_object = {'returnCode': self.code, 'details': self.obj}
                result = self.json.dumps(return_object)
                return self.Response(result, status=self.status)
            elif type(self.obj) == dict:
                self.details.append(self.obj)
                return_object = {'returnCode': self.code, 'details': self.details}
                result = self.json.dumps(return_object)
                return self.Response(result, status=self.status)
        except Exception as e:
            return e
