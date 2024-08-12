from dataclasses import dataclass
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


@dataclass
class AliyunSms:
    engine = 'aliyun'
    app_key: str
    secret_key: str

    def get_status(self):
        """
        发送状态：[0=发送中, 1=发送成功, 2=发送失败]
        :return:
        """
        return self.status

    def send(self, mobile, config, template_id, template_params=None):
        """
        发送短信
        :param mobile:
        :param config:
        :param template_id:
        :param template_params:
        :return:
        """
        request = CommonRequest(domain="dysmsapi.aliyuncs.com", version="2017-05-25", action_name="SendSms")
        request.set_method("POST")
        request.set_protocol_type("https")
        request.add_query_param("PhoneNumbers", mobile)
        request.add_query_param("SignName", config.get("sign"))
        request.add_query_param("TemplateCode", template_id)
        request.add_query_param("TemplateParam", template_params)
        client = AcsClient(self.app_key, self.secret_key)
        response = client.do_action_with_exception(request)
        try:
            resp_data = json.loads(response)
            if resp_data.get("Code") != "OK" or resp_data.get("Message") != "OK":
                self.status = 2
                return resp_data.get("Message")
            self.status = 1
            return response
        except Exception as e:
            raise Exception(e)
