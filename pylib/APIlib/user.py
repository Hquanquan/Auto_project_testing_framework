#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 10:45
# @File : user.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 用户类
import requests

from configs.api_env import HOST, userName, password


class User:

    def __init__(self, userName, password):
        self.host = HOST
        self.userName = userName
        self.password = password

    def login(self, get_Cookies=True):
        """
        获取登录信息
        :param get_Cookies: 默认get_Cookies=True 获取cookies信息
        :return:
        """
        path = "/accounts/password/authenticate"
        payload = {
            "user": {"email": self.userName},
            "password": self.password,
            "code": "",
            "locale": "zhcn"
        }
        url = f"{self.host}{path}"
        resp = requests.post(url, json=payload)
        if get_Cookies:
            return resp.cookies
        return resp.json()



if __name__ == '__main__':
    user = User(userName, password)
    info = user.login(False)
    print(info)





