# -*- coding:utf-8 -*-
from __future__ import absolute_import


class Singleton(type):
    """
    单例类元类
    """
    _instance = None

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance


class AbstractFactory(Singleton):
    """
    抽象工厂元类
    """

    def __init__(self, *args, **kwargs):
        super(AbstractFactory, self).__init__(*args, **kwargs)
        self.instances = {}
        self._initialed = False

    def register(self, name, subclass):
        """
        向基类注册
        """
        if name in self.instances:
            raise ValueError("subclass name: %s has been registered" % name)
        else:
            self.instances[name] = subclass

    def getInstance(self, name):
        """
        通过类的名字获得 子类 的实例(因为是singleton)
        """
        if not self._initialed:
            self.init()
            self._initialed = True
        if name not in self.instances:
            registered_name = ', '.join(list(self.instances.keys()))
            raise ValueError("name: %s has not been registered.\n Registered name is:\n%s" % (name, registered_name))
        else:
            return self.instances[name]()

    def remove(self, name, subclass):
        """
        动态删除某个子类
        """
        if name not in self.instances:
            raise ValueError("subclass name: %s has not been registered" % name)
        if self.instances[name] != subclass:
            raise ValueError("registered subclass and removed subclass not the same")
        else:
            del self.instances[name]

    def init(self):
        """
        初始化操作，把子类注册全部引入
        """
        raise NotImplementedError
