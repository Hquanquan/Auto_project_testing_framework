#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 16:12
# @File : demoPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
from pylib.UIlib.pageObjects.basePage2 import BasePage


class Demopage(BasePage):
    username = ["id", "username1"]
    password = ["id", "password"]
    login_btn = ["css selector", ".loginItem .layui-form-item button"]

    def find_ele(self):
        ele = self.find_element1(self.username)







