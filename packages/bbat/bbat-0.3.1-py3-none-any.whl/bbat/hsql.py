""" 把http请求转成sql """
# coding: utf-8
from pymysql.converters import escape_string
from urllib.parse import unquote
from pydantic import BaseModel, Field
from typing import List
import re
from typing import Union
from pydantic import BaseModel
import datetime
import json

class Config:
    where_key = "where"
    select_key = "select"
    page_key = "page"
    size_key = "size"
    group_key = "groupby"
    order_key = "order"
    
    defalut_pagesize = 15


def contains(symbol, string):
    '''
    是否包含symbol字符
    '''
    return symbol in string


def condition_match(string):
    '''
    拆分表达式
    name<>"john"   =>     ('name', '<>', '"john"')
    '''
    match = re.match(r"(.*)([\s<>=!]+)(.*)", string)
    if match and len(match.groups()) == 3:
        return match.groups()
    return None


def cutout(pattern, string):
    '''
    匹配并抠出
    '''
    string = string.replace(" ", "")
    match = re.findall(pattern, string)
    if len(match) > 0:
        for i in match:
            string = string.replace(i, "")
        return string, match[0]
    return string, None


def symbol_split(string):
    ls = list()
    buff = ""
    enclosed = []
    symbol = ['(', ')', '[', ']', '{', '}']
    for i, val in enumerate(string):
        if i == len(string) - 1:
            buff += val
            ls.append(buff)
            buff = ""
        if val in symbol:
            index = symbol.index(val)
            if len(enclosed) > 0 and index - enclosed[-1] == 1:
                enclosed.pop()
            else:
                enclosed.append(index)
        if val == "," and len(enclosed) == 0:
            ls.append(buff)
            buff = ""
            continue
        buff += val
    return ls




class Param(BaseModel):
    key: str = ''
    value: str = ''


class WhereParam(Param):
    operator: str = '='
    value: str = ''
    key: str = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.value.find(".") > 0:
            self.operator, self.value = self.value.split(".")
            if self.operator == "like":
                self.value = self.value.replace("*", "%")

            if not self.value.isdigit() and self.operator != "in":
                self.value = f"'{self.value}'"
            self.operator = self.get_operator(self.operator)

    def get_operator(self, op):
        OPERATOR_MAP = {
            "eq": "=",
            "ne": "!=",
            "gt": ">",
            "gte": ">=",
            "lt": "<",
            "lte": "<=",
            "in": "IN",
            "nin": "NOT IN",
            "any": "ANY",
            "some": "SOME",
            "all": "ALL",
            "notnull": "IS NOT NULL",
            "null": "IS NULL",
            "true": "IS TRUE",
            "nottrue": "IS NOT TRUE",
            "false": "IS FALSE",
            "notfalse": "IS NOT FALSE",
            "like": "LIKE",
            "ilike": "ILIKE",
            "nlike": "NOT LIKE",
            "nilike": "NOT ILIKE",
        }
        return OPERATOR_MAP[op]

    def sql(self, table=None):
        table = table + "." if table else ""
        return f'{table}{self.key} {self.operator} {self.value}'


class FieldParam(BaseModel):
    name: str
    alias: str = None
    conver: str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 类型转换，例如 data|json
        name, type_match = cutout(r'\|\w*', self.name)
        self.conver = type_match.replace("|", "") if type_match else None
        # alias
        tmp = self.name.split(":")
        if len(tmp) == 2:
            self.name = tmp[0]
            self.alias = tmp[1]

    def sql(self, table=None):
        table = table + "." if table else ""
        if self.alias:
            return f"{table}{self.name} AS {self.alias}"
        return table + self.name


class SelectParam(Param):
    fields: List[FieldParam] = []
    symbol: str = "SELECT"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = [FieldParam(name=i) for i in self.value.split(',')]

    def find_field(self, key):
        for field in self.fields:
            if field.name == key:
                return field
        return None

    def sql(self, table=None):
        text_list = [i.sql(table) for i in self.fields]
        return ",".join(text_list)


class PageParam(Param):
    value: int = Field(..., ge=1)


class SizeParam(Param):
    value: int = Field(default=Config.defalut_pagesize, ge=1)


class GroupByParam(Param):
    fields: List[str] = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = [field for field in self.value.split(",") if field]

    def sql(self, table=None):
        table = table + "." if table else ""
        group_fields = [f"{table}{i}" for i in self.fields]
        return ','.join(group_fields)


class OrderParam(Param):
    fields: List[str] = []
    symbol: str = "ORDER BY"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = [i for i in self.value.split(",") if i]

    def parse_symbol(self, string):
        return string.replace("-", "") + " DESC" if string.startswith("-") else string

    def sql(self, table=None):
        table = table + "." if table else ""
        format_list = [table + self.parse_symbol(sort) for sort in self.fields]
        return ",".join(format_list)


class Parameter(BaseModel):
    table_param: str = ''
    query_param: str = ''
    table: str = ''
    join_on: str = ''

    select: SelectParam = None
    wheres: List[WhereParam] = []
    groupby: GroupByParam = None
    order: OrderParam = None
    page: PageParam = None
    size: SizeParam = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query_param = unquote(self.query_param)
        # set defualt value
        if self.select is None:
            self.select = SelectParam(value="*")
        if self.page is None:
            self.page = PageParam(value=1)
        if self.size is None:
            self.size = SizeParam(value=Config.defalut_pagesize)

        self.parse_table_param()
        self.parse_query_params()

    def _split_table_condition(self, string):
        query_list = string.split(',')
        result_list = []
        for idx, item in enumerate(query_list):

            if '=' in item or len(result_list) == 0:  # 判断是否为键值对
                result_list.append(item)
            else:  # 处理没有值的情况，如 "select"x
                result_list[idx - 1] += ',' + item  # 将没有值的部分连接到上一个键值对
        return result_list

    def parse_table_param(self):
        self.table, match = cutout(pattern=r"\(.*\)", string=self.table_param)
        if not match:
            return
        # remove ()
        condition = re.sub(r"\(|\)|\s", "", match)

        # condi_list = condition.split(",")
        condi_list = self._split_table_condition(condition)
        # add where item
        for string in condi_list:
            matches = condition_match(string)
            # assert matches, f"The format is not supported: {string}"
            if not matches:
                continue
            key, operator, value = matches
            # check whether it is join_info
            if operator == '=' and contains(".", key) and contains(".", value):
                self.join_on = string
            else:
                self.parse_keyword(f'{key}={value}')
                # self.wheres.append(WhereParam(key=key, operator=operator, value=value))

    def parse_query_params(self):
        if not self.query_param:
            return
        for text in self.query_param.split("&"):
            self.parse_keyword(text)

    def parse_keyword(self, text: str = None):
        key, value = text.split("=")
        key = key.strip()
        value = value.strip().lower().replace(" ", '')
        # print(key, value)

        if key == Config.select_key:
            self.select = SelectParam(key=key, value=value)
        elif key == Config.page_key:
            self.page = PageParam(key=key, value=value)
        elif key == Config.size_key:
            self.size = SizeParam(key=key, value=value)
        elif key == Config.group_key:
            self.groupby = GroupByParam(key=key, value=value)
        elif key == Config.order_key:
            self.order = OrderParam(key=key, value=value)
        else:
            param = WhereParam(key=key, value=value)
            self.wheres.append(param)


class JoinSQLGenerator(BaseModel):
    """处理table连接类"""

    parameter1: Parameter
    parameter2: Parameter
    join_on: str = None
    table1: str = None
    table2: str = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table1 = self.parameter1.table
        self.table2 = self.parameter2.table
        self.join_on = self.parameter2.join_on if self.parameter2.join_on else self.parameter1.join_on
        if not self.join_on:
            self.join_on = f"{self.table1}.id = {self.table2}.{self.table1}_id"

    def _where_sql(self):
        sql = ""
        if len(self.parameter1.wheres + self.parameter2.wheres) > 0:
            sql += " WHERE "
            where_list = [where.sql(table=self.table1) for where in self.parameter1.wheres] + [
                where.sql(table=self.table2) for where in self.parameter2.wheres
            ]

            sql += " AND ".join(where_list)
        return sql

    def _groupby_sql(self):
        sql = ""
        if self.parameter1.groupby or self.parameter2.groupby:
            sql += "GROUP BY "
        sql += "" if self.parameter1.groupby is None else self.parameter1.groupby.sql(table=self.table1)
        sql += "" if self.parameter2.groupby is None else self.parameter2.groupby.sql(table=self.table2)
        return sql

    def _order_sql(self):
        sql = ""
        if self.parameter1.order or self.parameter2.order:
            sql += "ORDER BY "
        sql += "" if self.parameter1.order is None else self.parameter1.order.sql(table=self.table1)
        sql += "" if self.parameter2.order is None else self.parameter2.order.sql(table=self.table1)
        return sql

    def _limit_sql(self):
        size = self.parameter1.size.value
        offset = (int(self.parameter1.page.value) - 1) * int(size)
        return f"LIMIT {offset},{size}"

    def select(self):
        sql = """
        SELECT {select1},{select2}
        FROM {table1} JOIN {table2} ON {join_on}
        {where} {groupby} {order} {limit}
        """.format(
            select1=self.parameter1.select.sql(self.table1),
            select2=self.parameter2.select.sql(self.table2),
            table1=self.table1,
            table2=self.table2,
            join_on=self.join_on,
            where=self._where_sql(),
            groupby=self._groupby_sql(),
            order=self._order_sql(),
            limit=self._limit_sql(),
        )
        return re.sub(r" +", " ", sql)


class SQLGenerator(BaseModel):
    table: str
    url: str
    parameter: Parameter = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table = self.table
        self.parameter = Parameter(table_param=self.table, query_param=self.url)

    def _where_sql(self):
        sql = ""
        if len(self.parameter.wheres) > 0:
            sql += " WHERE "
            where_list = [where.sql() for where in self.parameter.wheres]
            sql += " AND ".join(where_list)
        return sql

    def _groupby_sql(self):
        sql = "" if self.parameter.groupby is None else " GROUP BY " + self.parameter.groupby.sql()
        return sql

    def _order_sql(self):
        sql = "" if self.parameter.order is None else " ORDER BY " + self.parameter.order.sql()
        return sql

    def _limit_sql(self):
        size = self.parameter.size.value
        offset = (int(self.parameter.page.value) - 1) * int(size)
        return f" LIMIT {offset},{size}"

    def data2sqlvalue(self, data):
        def convert_data(item):
            result = []
            for i in item.values():
                if i is None:
                    result.append(None)
                elif i is True:
                    result.append('1')
                elif i is False:
                    result.append('0')
                else:
                    result.append(str(i))
            return result
        
        if isinstance(data, dict):
            item = data
            keys = item.keys()
            length = len(item)
            values = tuple(convert_data(item))
        elif isinstance(data, list):
            item = data[0]
            keys = item.keys()
            length = len(item)
            values = [tuple(convert_data(item)) for item in data]
        elif data is None:
            return None, None, None
        else:
            # print(data)
            raise Exception("data type error: ")
        return length, keys, values

    def select(self, with_limit=True):
        select_sql = self.parameter.select.sql()
        table = self.table
        sql = "SELECT {select} FROM {table}".format(select=select_sql, table=table)

        sql += self._where_sql()
        sql += self._groupby_sql()
        sql += self._order_sql()
        if with_limit:
            sql += self._limit_sql()

        return sql

    def counting(self):
        sql = "SELECT COUNT(*) AS total FROM {table} {where} ".format(
            table=self.table, where=self._where_sql(), groupby=self._groupby_sql()
        )
        return sql

    def insert(self, data, replace=False):
        length, keys, insert_data = self.data2sqlvalue(data)
        if type(insert_data) is tuple:
            insert_data = [insert_data]
            
        data = ["(" + ",".join([f"'{escape_string(i)}'" if i is not None else "NULL" for i in d]) + ")" for d in insert_data]
        sql = "INSERT INTO %s (%s) VALUES %s" % (
            self.table,
            ", ".join([f"`{i}`" for i in keys]),
            ", ".join(data),
        )
        if replace:
            sql += " ON DUPLICATE KEY UPDATE " + ", ".join(["%s=VALUES(%s)" % (x, x) for x in keys])
        # sqlalcheme parse bug
        sql = sql.replace(":", "\:")
        return sql

    # 更新sql
    def update(self, data):
        length, keys, values = self.data2sqlvalue(data)
        set_ls = []
        for index, k in enumerate(keys):
            v = values[index]
            if v is None:
                continue
            v = str(v).replace("'", "'")
            string = f"`{k}`=\"{escape_string(v)}\""
            set_ls.append(string)

        sql = "UPDATE {table} SET {update} {where}".format(
            table=self.table,
            update=",".join(set_ls),
            where=self._where_sql(),
        )
        # sqlalcheme parse bug
        sql = sql.replace(":", "\:")
        return sql

    # 删除sql
    def delete(self):
        sql = "DELETE FROM {table} {where}".format(
            table=self.table,
            where=self._where_sql(),
        )
        sql = sql.replace(":", "\:")
        return sql



class DataAdapter(BaseModel):
    '''查询出来的数据后处理'''
    generator: SQLGenerator
    data: Union[dict, list]

    def tree_list(self): ...

    def format(self):
        # 没有field 定义，直接转
        if isinstance(self.data, dict):
            self.data = self._field_format(self.data)
        else:
            for item in self.data:
                self._field_format(item)
        return self.data

    def _field_format(self, item):
        for key, value in item.items():
            field = self.generator.parameter.select.find_field(key)
            if field is None or field.conver is None:
                continue
            item[key] = self._field(field.conver, value)
        return item

    def _field(self, conver, value):
        if isinstance(value, datetime.datetime) or isinstance(value, datetime.date):
            value = value.strftime('%Y-%m-%d %H:%M:%S')
        if conver == "int":
            value = int(value)
        elif conver == "str":
            value = str(value)
        elif conver == "json":
            value = json.loads(value)
        elif conver == "float":
            value = float(value)
        else:
            raise ValueError(f'{conver} is not support!')
        return value


class HSQLTest:

    def test_join(
        self,
        table1="user",
        table2="chat_msg(user.id=chat_msg.user_id)",
        query1="page=1&size=20&order=name&age=gt.13&status=1&id=gt.2",
    ):

        param1 = Parameter(table_param=table1, query_param=query1)
        param2 = Parameter(table_param=table2)

        generator = JoinSQLGenerator(parameter1=param1, parameter2=param2)
        # print(generator)
        sql = generator.select()
        # print(sql)

    def test_parse_from_urlquery(
        self, table="robot", query="status=1&is_system=1&is_official=0&size=20&page=1&name=like.*11*&category=like.**"
    ):
        generator = SQLGenerator(table=table, url=query)
        # print(generator.__dict__)
        sql1 = generator.select()
        # print(sql1)
        pass

    def test_parse_from_table(self, table="user(id=gt.2, status=1, age=gt.13)", query="page=1&size=20&order=name"):
        '''table查询条件'''
        generator = SQLGenerator(table=table, url=query)
        # print(generator)
        sql1 = generator.select()
        # print(sql1)

    def test_sql_generator(
        self,
    ):
        def build_sql(table, query: str):
            generator = SQLGenerator(table=table, url=query)
            # print(generator)
            # print(generator.select())
            # print(generator.insert(data={"name": "zhangsan", "age": 18}))
            # print(generator.update(data={"name": "lisi", "age": None}))
            # print(generator.delete())

        table = "user"
        query = "name=zhangsan&age=3&_page=1&_size=20&_order=name"
        build_sql(table, query)

    def test_query(
        self,
    ):

        def parse_query_params(table, query_params: str):
            params = Parameter(table_param=table, query_param=query_params)
            # print(params.__dict__)

        table = "user(user.id=car.user_id, age=gt.10)"
        query = "name=zhangsan&age=3&_page=1&_size=20&_order=name"
        query = ""
        parse_query_params(table, query)
