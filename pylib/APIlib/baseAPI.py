#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 11:14
# @File : baseAPI.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : api基类，实现基本的CRUD增删改查功能，用于被业务api类继承
from json import JSONDecodeError

import requests

from configs.api_env import HOST, password, userName
from pylib.APIlib.user import User
from utils.tools import read_yaml


class BaseAPI:
    """
    api基类，实现基本的CRUD增删改查功能，用于被业务api类继承
    """

    def __init__(self, cookies):
        """
        初始化，
        :param cookies: 鉴权信息
        """
        # cookies信息必须在登录接口里获取
        self.cookies = cookies
        # cookies 里包含spaceid
        self.space_id = self.cookies["X-Space-Id"]
        # 测试接口的URL地址，
        self.host = HOST
        # 接口数据模板的文件相对路径
        path = "configs/api_conf.yaml"
        api_template = read_yaml(path)
        # 获取当前类的类名，便于根据类名读取yaml文件里的模板数据
        current_className = self.__class__.__name__
        # 根据当前类名获取yaml文件接口数据模板
        self.conf = api_template[current_className]
        self.path = self.conf["path"]

    def add(self, **kwargs):
        """
        添加
        :param kwargs:
        :return:
        """
        # 读取配置文件模板中：add 的内容
        data = self.conf["add"]
        kwargs["space"] = self.space_id
        data.update(kwargs)
        payload = data
        url = self.host + self.path
        resp = requests.post(url, json=payload, cookies=self.cookies)
        return resp.json()["value"][0]

    def edit(self, _id, **kwargs):
        """
        编辑修改
        :param _id:
        :param kwargs:
        :return:
        """
        # 读取配置文件模板中：edit 的内容
        data = self.conf["edit"]
        # 更新data的数据，把kwargs的内容更新到data
        data.update(kwargs)
        # 把当前对象的space_id复制到data["space"],主要避免space_id不一致
        data["space"] = self.space_id
        # 把修改请求参数放到$set中
        payload = {"$set": data}
        url = self.host + self.path + "/" + _id
        resp = requests.put(url, json=payload, cookies=self.cookies)
        try:
            res = resp.json()
            return res
        except JSONDecodeError:
            return {}

    def list_all(self):
        """
        获取所有数据
        :return:
        """
        url = self.host + self.path
        resp = requests.get(url, cookies=self.cookies)
        return resp.json()["value"]

    def delete(self, _id):
        """
        根据id单个数据
        :param _id:
        :return:
        """
        url = self.host + self.path + "/" + _id
        resp = requests.delete(url, cookies=self.cookies)
        return resp.json()

    def delete_all(self):
        """
        获取所有数据，变量删除数据
        :return:
        """
        items = self.list_all()
        for item in items:
            self.delete(item['_id'])


if __name__ == '__main__':
    cookies = User(userName, password).login()
    base = BaseAPI(cookies)
    print(base.conf["path"])


