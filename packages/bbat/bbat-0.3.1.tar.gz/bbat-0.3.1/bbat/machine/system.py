#!/bin/python
#coding: utf-8
# +-------------------------------------------------------------------
# | django-vue-lyadmin
# +-------------------------------------------------------------------
# | Author: lybbn
# +-------------------------------------------------------------------
# | QQ: 1042594286
# +-------------------------------------------------------------------

# ------------------------------
# 系统命令封装
# ------------------------------

import sys,os,platform
from django.core.cache import cache

BASE_DIR = './'

plat = platform.system().lower()
if plat == 'windows':
    from . import windows as myos
else:
    from . import linux as myos


class system:

    isWindows = False

    def __init__(self):
        self.isWindows = self.isWindows()

    def isWindows(self):
        plat = platform.system().lower()
        if plat == 'windows':
            return True
        return False

    def getSystemAllInfo(self,isCache=False):
        """
        获取系统所有信息
        """
        data = {}
        data['mem'] = self.getMemInfo()
        data['load_average'] = self.getLoadAverage()
        data['network'] = self.getNetWork()
        data['cpu'] = self.getCpuInfo(1)
        data['disk'] = self.getDiskInfo()
        data['time'] = self.getBootTime()
        data['system'] = self.getSystemVersion()
        data['is_windows'] = self.isWindows
        return data

    def getMemInfo(self):
        memInfo =  myos.getMemInfo()
        return memInfo

    def getLoadAverage(self):
        data = myos.getLoadAverage()
        return data

    def getNetWork(self):
        data = myos.getNetWork()
        return data

    def getCpuInfo(self,interval=1):
        data = myos.getCpuInfo(interval)
        return data

    def getBootTime(self):
        data = myos.getBootTime()
        return data

    def getDiskInfo(self):
        data = myos.getDiskInfo()
        return data

    def getSystemVersion(self):
        data = myos.getSystemVersion()
        return data