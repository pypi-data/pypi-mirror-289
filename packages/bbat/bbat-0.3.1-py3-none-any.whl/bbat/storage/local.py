import os
import aiofiles
from fastapi import UploadFile

SIZE = 2048


class LocalStorage:
    path = './uploads'

    async def upload(self, file_in: UploadFile, key: str):
        directory = self.path
        paths = key.split('/')
        save_name = paths[-1]
        _date = paths[-2]
        folder = '/'.join(paths[:-2])
        save_path = os.path.join(directory, folder, _date).replace('\\', '/')
        file_name = os.path.join(save_path, save_name).replace('\\', '/')

        if not os.path.exists(save_path):
            os.makedirs(save_path)
        try:
            async with aiofiles.open(file_name, 'wb') as file_out:
                content = await file_in.read(SIZE)
                while content:
                    await file_out.write(content)
                    content = await file_in.read(SIZE)
        except Exception as e:
            raise Exception('上传文件失败:%s' % e)
