#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 16:33
# @File : loginPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
from pylib.UIlib.pageObjects.basepage2 import BasePage


class LoginPage(BasePage):
    #
    username = ["id", "username"]
    password = ["id", "password"]
    login_btn = ["css selector", ".loginItem .layui-form-item button"]

    # username = "id=>username"
    # password = "id=>password"
    # login_btn = "css=>.loginItem .layui-form-item button"

    def login(self, username, password):
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        self.click(self.login_btn)
        return self



if __name__ == '__main__':

    loginPage = LoginPage()
    loginPage.login("18819443338", "18819443338")

