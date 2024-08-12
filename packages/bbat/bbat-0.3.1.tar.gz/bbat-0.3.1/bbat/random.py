import random
import uuid
import string

ALL_RANDOM_STR: str = string.ascii_letters + string.digits


def random_int(length: int) -> int:
    """
    返回指定长度的随机整数
    :param length:
    :return:
    """
    return random.randint(0, 10 ** length)


def random_string(length: int) -> str:
    """返回随机字符串"""
    return ''.join(random.choices(ALL_RANDOM_STR, k=length))