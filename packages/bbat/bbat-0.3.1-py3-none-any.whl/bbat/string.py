import json
import re
from urllib.parse import parse_qs, urlparse


def parse_mysql_url(
    url="mysql://username:password@localhost:3306/database_name?param1=value1&param2=value2",
):
    '''mysql url转dict'''
    parser = urlparse(url)
    query_string = parser.query
    query_params = parse_qs(query_string)

    db_dict = {
        "scheme": parser.scheme,
        "host": parser.hostname,
        "port": parser.port,
        "user": parser.username,
        "password": parser.password,
        "database": parser.path[1:],  # 去除路径中的斜杠
        "query_params": query_params,
    }
    return db_dict

def to_snake_case(name: str) -> str:
    """驼峰命名转蛇形命名"""
    to_snake_pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return to_snake_pattern.sub('_', name).lower()

def to_camel_case(name: str, is_upper=True) -> str:
    """蛇形命名转驼峰命名
        is_upper: 为True则首字母大写, 否则首字母小写
    """
    if not name:
        return name
    res = ''.join(word.title() for word in name.split('_'))
    if not is_upper:
        res = f'{res[0].lower()}{res[1:]}'
    return res

def remove_punctuation(sentence: str, punctuation="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"):
    """去掉特殊字符"""
    dic = str.maketrans("", "", punctuation)
    return sentence.translate(dic)


def cutout(pattern, string):
    """
    匹配并抠出
    cutout(r'\(.*?\)', string)
    """
    string = string.replace(" ", "")
    match = re.findall(pattern, string)
    if len(match) > 0:
        for i in match:
            string = string.replace(i, "")
        return string, match[0]
    return string, None


def symbol_split(string):
    '''识别括号中的内容'''
    ls = list()
    buff = ""
    enclosed = []
    symbol = ["(", ")", "[", "]", "{", "}"]
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


# 判断是否中文
def is_chinese(char):
    """判断是否是中文"""
    if "\u4e00" <= char <= "\u9fff":
        return True
    else:
        return False


def chinese_to_pinyin(text="北京"):
    '''转拼音'''
    from xpinyin import Pinyin

    p = Pinyin()
    return p.get_pinyin(text).replace("-", "")
