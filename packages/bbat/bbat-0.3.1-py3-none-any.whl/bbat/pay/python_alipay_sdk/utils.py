"""
    alipay/utils.py
    ~~~~~~~~~~
"""


class AliPayConfig:
    def __init__(self, timeout=15):
        self.timeout = timeout


def float2dot(str):
    """
    把数字或字符串10.00 转换成保留后两位（字符串）输出
    """
    try:
        return '%.2f' % round(float(str),2)
    except:
        return str