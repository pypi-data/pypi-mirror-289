''' sqliteclient easy to use '''

import aiosqlite

import sqlite3
from dataclasses import dataclass
from typing import Any, List, Tuple
import re


@dataclass
class SQLite:
    db_path: str
    return_dict: bool = True
    _conn: sqlite3.Connection = None

    def connect(self):
        if self._conn is None:
            self._conn = sqlite3.connect(self.db_path)
            self._conn.row_factory = lambda cursor, row: (
                dict(zip([col[0] for col in cursor.description], row)) if self.return_dict else row
            )
        return self._conn

    def sqlalchemy_sql(self, query):
        regex = re.compile(":(?P<name>\w+)")
        compiled = query.compile()
        params = compiled.construct_params()
        sql = regex.sub("'{\g<name>}'", str(query)).format(**params)
        return sql

    def _build_query(self, query, values):
        if isinstance(query, str):
            query = sqlite3.sql(query)
            query = query.bindparams(**values) if values is not None else query
        elif values:
            query = query.values(**values)
        else:
            query = self.sqlalchemy_sql(query)
        return str(query)

    def execute(self, query, values=None):
        query = self._build_query(query, values)
        cur = self.connect().cursor()
        cur.execute(query)
        if query.strip().upper().startswith("INSERT"):
            return cur.lastrowid
        elif query.strip().upper().startswith("SELECT"):
            return cur.fetchall()
        self._conn.commit()

    def fetch_all(self, query, values=None, return_dict=True, with_fields=False):
        query = self._build_query(query, values)
        cur = self.connect().cursor()
        cur.execute(query)
        data = cur.fetchall()
        if with_fields:
            fields = [(field[0], field[1]) for field in cur.description]
            return fields, data
        return data

    def fetch_one(self, query, values=None):
        query = self._build_query(query, values)
        cur = self.connect().cursor()
        cur.execute(query)
        ret = cur.fetchone()
        return ret

    def update(self, table, data, where=None):
        set_list = [f'`{k}`="{v}"' for k, v in data.items()]
        sql = f"UPDATE {table} SET {','.join(set_list)}"
        if where:
            sql += f" WHERE {where}"
        return self.execute(sql)

    def add(self, table, data_list: List[dict] = []):
        for data in data_list:
            field = ",".join([f"`{key}`" for key in data.keys()])
            value = ",".join([f'{val}' for val in data.values()])
            sql = f"INSERT INTO {table}({field}) VALUES({value})"
            return self.execute(sql)

    def create_table(self, table):
        sql = f'''
        CREATE TABLE IF NOT EXISTS `{table}`( 
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        '''
        print(">>>", sql)
        res = self.execute(sql)
        return res

    def table_list(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        print(">>>", sql)
        tables = self.fetch_all(sql)
        table_list = [row['name'] for row in tables]
        return table_list

    def table_detail(self, table):
        sql = f"""
        PRAGMA table_info({table})
        """
        print(">>>", sql)
        table_info = self.fetch_all(sql)
        return table_info

    def add_field(self, table, field, type):
        sql = f"""
        ALTER TABLE `{table}` ADD COLUMN `{field}` {type}
        """
        res = self.execute(sql)
        return res

    def drop_field(self, table, field):
        sql = f"""
        PRAGMA writable_schema=ON;
        ALTER TABLE `{table}` DROP COLUMN `{field}`;
        PRAGMA writable_schema=OFF;
        """
        res = self.execute(sql)
        return res
    

class AsyncSqlite:

    def __init__(self, sanic, database="sqlite.db"):
        self.sanic = sanic
        self.database = database
        self.conn = None

    async def fetch_all(self):
        # self.conn = await aiosqlite.connect(self.database)
        self.conn = await aiosqlite.connect(self.database, loop=self.sanic.loop)

        def dict_factory(cursor, row):
            d = {}
            for index, col in enumerate(cursor.description):
                d[col[0]] = row[index]
            return d

        self.conn.row_factory = dict_factory
        return self.conn

    async def query(self, query, *args, **kwargs):
        if not self.conn:
            await self.connect()
        async with self.conn.execute(query, *args, **kwargs) as cursor:
            ret = await cursor.fetchall()
            return ret

    async def fetch_one(self, query, *args, **kwargs):
        if not self.conn:
            await self.connect()
        async with self.conn.execute(query, *args, **kwargs) as cursor:
            ret = await cursor.fetchone()
            return ret

    async def execute(self, query, *args, **kwargs):
        if not self.conn:
            await self.connect()
        res = await self.conn.execute(query, *args, **kwargs)
        await self.conn.commit()

        return res

    # high level interface
    # 创建表
    async def create_table(self, table):
        sql = f'''CREATE TABLE `{table}`( 
            `id` integer PRIMARY KEY autoincrement,
            `created_at` datetime DEFAULT CURRENT_TIMESTAMP
        ) '''
        print(">>>", sql)
        res = await self.execute(sql)
        return res

    # 所有表
    async def tables(self, database):
        sql = f"SELECT name FROM sqlite_master WHERE type='table'"
        print(">>>", sql)
        tables = await self.query(sql)
        table_list = list(map(lambda x: x['name'], tables))
        return table_list

    # 表结构
    async def table_fields(self, name):
        sql = f"PRAGMA table_info({name})"
        print(">>>", sql)
        table_info = await self.query(sql)
        return table_info

    # 添加字段
    async def add_field(self, table, field, type):
        sql = f"ALTER TABLE {table} ADD COLUMN {field} {type}"
        print(">>>", sql)
        await self.execute(sql)
        return

    async def drop_field(self, table, field):
        sql = f"ALTER TABLE {table} DROP COLUMN {field}"
        print(">>>", sql)
        await self.execute(sql)
        return
