from dataclasses import dataclass
import json
import os
import time


def get_env(key, default=""):
    val = os.getenv(key)
    return val if val else default


class Config:
    dict = {}

    def __init__(self, path="config.yaml"):
        if not os.path.exists(path):
            raise Exception("config file not exists")

        suffix = path.split('.')[-1]
        if suffix in ['yaml', 'yml']:
            self.load_yaml(path)
        if suffix in ['json', 'jsonl']:
            self.load_json(path)

    def __call__(self, key):
        return self.get_env(key)

    def load_yaml(self, file):
        import yaml

        with open(file, 'r', encoding='utf-8') as conf_file:
            self.dict = yaml.safe_load(conf_file)

    def load_json(self, file):
        import json

        with open(file, 'r', encoding='utf-8') as conf_file:
            self.dict = json.load(conf_file)

    def set(self, key, value):
        '''set config'''
        keys = key.split(".")
        config_value = self.dict
        for k in keys:
            config_value = config_value[k]
        config_value = value

    def merge(self, config):
        '''merge config'''
        self.dict.update(config)
        return self.dict

    def get(self, key):
        '''key - 配置key，支持级联：app.name
        config['app']['name'] else None
        '''
        keys = key.split(".")
        config_value = self.dict
        for k in keys:
            config_value = config_value.get(k)
        return config_value

    def get_env(self, key):
        """key - 配置key，支持级联：app.name
        app.name 先取 APP_NAME 环境变量，再取config['app']['name']
        """
        keys = key.split(".")
        env_key = "_".join([i.upper() for i in keys])
        config_value = get_env(env_key)
        if not config_value:
            return self.get(key)
        return config_value


@dataclass
class DBConfig:
    """数据库配置操作工具"""

    table = 'system_config'
    db = None

    async def get(self, type_: str, name: str = None):
        """根据类型和名称获取配置字典"""
        where = f"type='{type_}'"
        if name:
            where = f"name='{name}'"
        configs = await self.db.fetch_all(f"select * {self.table} WHERE {where}")
        return {i.name: i.value for i in configs}

    async def get_val(self, type_: str, name: str, default: str = None):
        """根据类型和名称获取配置值"""
        config = await DBConfig.get(type_, name)
        if name not in config:
            return default
        return config.get(name)

    async def get_map(self, type_: str, name: str):
        """根据类型和名称获取配置值(Json字符串转dict)"""
        value = await DBConfig.get_val(type_, name)
        if value is None:
            return None
        if not value:
            return {}
        return json.loads(value)

    async def set(self, type_: str, name: str, val: str):
        """设置配置的值"""
        config = await self.db.fetch_one(f"select * {self.table} WHERE type='{type_}' and name='{name}' limit 1")
        if config:
            await self.db.execute(
                f"update {self.table} set value='{val}', update_time={int(time.time())} WHERE id={config['id']}"
            )
        else:
            await self.db.execute(
                f"insert into {self.table} (type,name,value,create_time,update_time) values('{type_}', '{name}', '{val}', {int(time.time())}, {int(time.time())})"
            )
