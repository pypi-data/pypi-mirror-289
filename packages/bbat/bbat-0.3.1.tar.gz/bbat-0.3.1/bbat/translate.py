import hashlib
import time
import uuid


class Translator:
    def __init__(self, key="705d93e03f2780e6", secret="KaVHXgpo15lgOHHJ5907bRY05eCj5X6N"):
        self.host = "https://openapi.youdao.com/api"
        self.key = key
        self.secret = secret

    def __call__(self, text):
        return self.translate(text)

    def encrypt(self, signStr):
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(signStr.encode("utf-8"))
        return hash_algorithm.hexdigest()

    def truncate(self, q):
        if q is None:
            return None
        size = len(q)
        return q if size <= 20 else q[0:10] + str(size) + q[size - 10 : size]

    def gen_signature(self, q, curtime, salt):
        signStr = self.key + self.truncate(q) + salt + curtime + self.secret
        sign = self.encrypt(signStr)
        return sign

    def translate(self, text="你好"):
        """有道翻译"""
        import requests

        curtime = str(int(time.time()))
        salt = str(uuid.uuid1())

        data = {}
        data["from"] = "auto"
        data["to"] = "auto"
        data["signType"] = "v3"
        data["curtime"] = curtime
        data["appKey"] = self.key
        data["q"] = text
        sign = self.gen_signature(text, curtime, salt)
        data["salt"] = salt
        data["sign"] = sign
        # data['vocabId'] = "您的用户词表ID"

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(self.host, data=data, headers=headers)
        # contentType = response.headers['Content-Type']
        resp = response.json()
        # print(resp)
        data = {
            "translation": resp.get("translation"),
            "basic": resp.get("basic"),
        }
        translation = data["translation"]
        if not translation:
            return ""
        if len(translation) > 0:
            return "".join(data["translation"])
        return translation
