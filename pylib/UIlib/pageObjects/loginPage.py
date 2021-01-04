#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 16:33
# @File : loginPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 登录页
import allure

from pylib.UIlib.pageObjects.basePage1 import BasePage


class LoginPage(BasePage):
    """
    登录页
    """
    # 方案一: 通过读取配置文件里的数据作为属性值,动态赋值

    # 方案二: 手动编辑赋值属性，硬编码
    # username = ["id", "username"]
    # password = ["id", "password"]
    # login_btn = ["css selector", ".loginItem .layui-form-item button"]

    # 方案三: 与方案二一样，只是传参不一样
    # username = "id=>username"
    # password = "id=>password"
    # login_btn = "css=>.loginItem .layui-form-item button"

    @allure.step("step:用户登录系统")
    def login(self, username, password):
        """
        用户登录系统
        :param username:
        :param password:
        :return:
        """
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        self.click(self.login_btn)
        return self



if __name__ == '__main__':

    loginPage = LoginPage()
    loginPage.login("18819443338", "18819443338")

