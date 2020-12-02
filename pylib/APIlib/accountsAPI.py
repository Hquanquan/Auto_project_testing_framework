#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 13:39
# @File : accountsAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    :
import pprint

import requests

from configs.api_env import password, userName
from pylib.APIlib.baseAPI import BaseAPI
from pylib.APIlib.user import User


class AccountsAPI(BaseAPI):
    """
    签约对象API,继承自BaseAPI,BaseAPI已实现CRUD增删改查功能。
    若需要扩展可在该类进行扩展，重写，重载
    """
    # 重写父类的list_all方法
    def list_all(self, hasTarget=False, **kwargs):
        """
        默认获取所有数据
        :param hasTarget: 默认hasTarget=False表明没有指定获取的条件
        :param kwargs:
        :return:
        """
        url = self.host + self.path
        payload = {}
        if hasTarget:
            data = self.conf["list"]
            if data:
                # 若data有数据，才进行更新操作，data=None进行更新操作会报错
                data.update(kwargs)
            payload = data
        resp = requests.get(url, cookies=self.cookies, params=payload)
        return resp.json()["value"]

