# -*- coding=utf-8
from dataclasses import dataclass
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

@dataclass
class QCloudStorage(object):
    engine = 'qiniu'
    bucket = ''
    secret_id = ''
    secret_key = ''
    region = ''

    async def get_client(self):
        """
        :param kwargs:
        :return:
        """
        try:
            config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key)
            return CosS3Client(config)
        except Exception as e:
            raise Exception(str(e))

    async def upload_data(self, target_path, data, **kwargs):
        """
        通过stream上传到七牛
        :param target_path:  目标路径，即文档参数key
        :param data:    stream
        :param kwargs:
        :return:
        """
        client = await self.get_client()
        try:
            response = client.put_object(Bucket=self.bucket, Body=data, Key=target_path)
            if response['ETag']:
                return target_path
        except Exception as e:
            raise Exception(str(e))
        return ''
