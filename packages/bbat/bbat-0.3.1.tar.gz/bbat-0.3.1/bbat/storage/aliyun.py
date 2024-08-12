from dataclasses import dataclass
import oss2


@dataclass
class AliyunStorage():
    engine = 'aliyun'
    access_key = ''
    secret_key = ''
    bucket_name = ''

    async def oss_client(self):
        """
        :param kwargs:
        :return:
        """

        endpoint = "https://oss-cn-hangzhou.aliyuncs.com"
        auth = oss2.Auth(self.access_key, self.secret_key)
        return oss2.Bucket(auth, endpoint, self.bucket_name)

    @classmethod
    async def upload_data(cls, target_path, data, **kwargs):
        """
        通过stream上传阿里云
        :param target_path:  目标路径，即文档参数key
        :param data:    stream
        :param kwargs:
        :return:
        """
        try:
            bucket = await cls.oss_client()
            resp = bucket.put_object(target_path, data)
            return resp.resp.response.url
        except oss2.exceptions.OssError as e:
            raise Exception('上传文件失败:%s' % e.message)