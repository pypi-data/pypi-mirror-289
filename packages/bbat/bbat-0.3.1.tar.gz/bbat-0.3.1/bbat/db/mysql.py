from typing import Any
import pymysql
import aiomysql
from dataclasses import dataclass
from sqlalchemy import text
import re


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


def _escape_value(value):
    if str(value).find('"') != -1:
        return f"'{value}'"
    return f'"{value}"'


@dataclass
class AsyncMysql(metaclass=Singleton):
    host: str
    port: int
    database: str
    user: str
    password: str
    return_dict: bool = True
    charset: str = "utf8mb4"
    autocommit = True
    loop: Any = None
    minsize: int = 3
    maxsize: int = 5
    pool_recycle: int = 7 * 3600
    connect_timeout: int = 20
    read_timeout: int = 20
    write_timeout: int = 20
    _pool: Any = None

    async def init_pool(self):
        if not self._pool:
            self._pool = await aiomysql.create_pool(
                host=self.host,
                port=self.port,
                db=self.database,
                user=self.user,
                password=self.password,
                minsize=self.minsize,
                maxsize=self.maxsize,
                charset=self.charset,
                loop=self.loop,
                autocommit=self.autocommit,
                pool_recycle=self.pool_recycle,
                cursorclass=aiomysql.cursors.DictCursor if self.return_dict else aiomysql.cursors.Cursor,
            )

    def sqlalchemy_sql(self, query):
        regex = re.compile(":(?P<name>\w+)")
        compiled = query.compile()
        params = compiled.construct_params()
        sql = regex.sub("'{\g<name>}'", str(query)).format(**params)
        return sql
    
    def _build_query(self, query, values):
        if isinstance(query, str):
            query = text(query)
            query = query.bindparams(**values) if values is not None else query
        elif values:
            query = query.values(**values)
        else:
            query = self.sqlalchemy_sql(query)
        return str(query)

    async def execute(self, query, values=None):
        """Executes the given query, returning the lastrowid from the query."""
        query = self._build_query(query, values)
        await self.init_pool()
        async with self._pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(query)
                except Exception:
                    # https://github.com/aio-libs/aiomysql/issues/340
                    await conn.ping()
                    await cur.execute(query)
                return cur.lastrowid

    async def fetch_all(self, query, values=None, return_dict=True, with_fields=False):
        """Returns a row list for the given query and args."""
        cursorclass = aiomysql.cursors.DictCursor if return_dict else aiomysql.cursors.Cursor
        query = self._build_query(query, values)

        await self.init_pool()
        async with self._pool.acquire() as conn:
            async with conn.cursor(cursorclass) as cur:
                try:
                    await cur.execute(query)
                    ret = await cur.fetchall()
                except pymysql.err.InternalError:
                    await conn.ping()
                    await cur.execute(query)
                    ret = await cur.fetchall()
                if with_fields:
                    # (table, field)
                    fields = [(field.table_name, field.name) for field in cur._result.fields]
                    return fields, ret
                return ret

    async def fetch_one(self, query, values=None):
        """Returns the (singular) row returned by the given query."""
        query = self._build_query(query, values)

        if not self._pool:
            await self.init_pool()
        async with self._pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(query)
                    ret = await cur.fetchone()
                except pymysql.err.InternalError:
                    await conn.ping()
                    await cur.execute(query)
                    ret = await cur.fetchone()
                return ret

    async def update(self, table, data, where=None):
        set_list = [f'`{k}`="{v}"' for k, v in data.items() if v != None]
        sql = f"update {table} set {','.join(set_list)}"
        if where:
            sql += f"where {where}"
        return await self.execute(sql)

    async def add(self, table, data_list: list = []):
        if not isinstance(data_list, list):
            data_list = [data_list]
        for data in data_list:
            field = ",".join([f"`{key}`" for key in data.keys()])
            value = ",".join([f'{_escape_value(val)}' for val in data.values()])
            sql = f"insert into {table}({field}) values({value})"
            return await self.execute(sql)

    async def create_table(self, table):
        sql = f'''
        CREATE TABLE `{table}`( 
            `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
            `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4
        '''
        print(">>>", sql)
        res = await self.execute(sql)
        return res

    async def table_list(self, database):
        sql = f"SELECT table_name FROM information_schema.tables WHERE table_schema='{database}'"
        print(">>>", sql)
        tables = await self.fetch_all(sql)
        table_list = list(map(lambda x: x['table_name'], tables))
        return table_list

    async def table_detail(self, database, table):
        sql = f"""
        SELECT column_name ,data_type ,column_comment ,column_default
        FROM information_schema.columns
        WHERE table_name = '{table}'
        AND table_schema = '{database}'
        """
        print(">>>", sql)
        table_info = await self.fetch_all(sql)
        return table_info

    async def add_field(self, table, field, type):
        sql = f"ALTER TABLE {table} ADD {field} {type}"
        print(">>>", sql)
        res = await self.execute(sql)
        return res

    async def remove_field(self, table, field):
        sql = f"ALTER TABLE {table} DROP {field}"
        print(">>>", sql)
        res = await self.execute(sql)
        return res


@dataclass
class Mysql(metaclass=Singleton):

    host: str
    port: int
    database: str
    user: str
    password: str
    return_dict: bool = True
    charset: str = "utf8mb4"
    autocommit = True
    loop: Any = None
    minsize: int = 3
    maxsize: int = 5
    pool_recycle: int = 7 * 3600
    connect_timeout: int = 20
    read_timeout: int = 20
    write_timeout: int = 20
    _pool: Any = None

    def connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            passwd=self.password,
            charset=self.charset,
            autocommit=self.autocommit,
            cursorclass=pymysql.cursors.DictCursor if self.return_dict else pymysql.cursors.Cursor,
        )

    def sqlalchemy_sql(self, query):
        regex = re.compile(":(?P<name>\w+)")
        compiled = query.compile()
        params = compiled.construct_params()
        sql = regex.sub("'{\g<name>}'", str(query)).format(**params)
        return sql
    
    def _build_query(self, query, values):
        if isinstance(query, str):
            query = text(query)
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
        return cur.lastrowid

    def fetch_all(self, query, values=None, return_dict=True, with_fields=False):
        query = self._build_query(query, values)

        cursorclass = pymysql.cursors.DictCursor if return_dict else pymysql.cursors.Cursor
        cur = self.connect().cursor(cursor=cursorclass)
        cur.execute(query)
        data = cur.fetchall()
        if with_fields:
            # (table, field)
            fields = [(field.table_name, field.name) for field in cur._result.fields]
            return fields, data
        return data

    def fetch_one(self, query, values=None):
        query = self._build_query(query, values)
        cur = self.connect().cursor()
        cur.execute(query, values)
        ret = cur.fetchone()
        return ret

    def update(self, table, data, where=None):
        set_list = [f'`{k}`="{v}"' for k, v in data.items()]
        sql = f"update {table} set {','.join(set_list)}"
        if where:
            sql += f"where {where}"
        return self.execute(sql)

    def add(self, table, data_list: list = []):
        for data in data_list:
            field = ",".join([f"`{key}`" for key in data.keys()])
            value = ",".join([f'{_escape_value(val)}' for val in data.values()])
            sql = f"insert into {table}({field}) values({value})"
            return self.execute(sql)

    # high level interface
    # 创建表
    def create_table(self, table):
        sql = f'''
        CREATE TABLE `{table}`( 
            `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
            `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4
        '''
        print(">>>", sql)
        res = self.execute(sql)
        return res

    # 所有表
    def table_list(self, database):
        sql = f"SELECT table_name FROM information_schema.tables WHERE table_schema='{database}'"
        print(">>>", sql)
        tables = self.fetch_all(sql)
        table_list = list(map(lambda x: x['table_name'], tables))
        return table_list

    # 表结构
    def table_detail(self, database, table):
        sql = f"""
        SELECT  column_name name
            ,data_type type
            ,column_comment comment
            ,column_default value
        FROM information_schema.columns
        WHERE table_name = '{table}'
        AND table_schema = '{database}'
        """
        print(">>>", sql)
        table_info = self.fetch_all(sql)
        return table_info

    # 添加字段
    def add_field(self, table, field, type):
        sql = f"ALTER TABLE {table} ADD {field} {type}"
        print(">>>", sql)
        res = self.execute(sql)
        return res

    def remove_field(self, table, field):
        sql = f"ALTER TABLE {table} DROP {field}"
        print(">>>", sql)
        res = self.execute(sql)
        return res


