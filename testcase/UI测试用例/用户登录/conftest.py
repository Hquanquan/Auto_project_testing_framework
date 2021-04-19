#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 9:28
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 用户登录
import allure
import pytest

from configs.web_env import userName, password
from pylib.UIlib.pageObjects.loginPage import LoginPage
from pylib.UIlib.pageObjects.commonPage import CommonPage


@pytest.fixture(scope="session")
def user_login():
    """
    1、用户登录系统，进入首页预览
    2、测试完毕退出登录
    :return:
    """
    user = LoginPage()
    user.login(userName, password)
    commonPage = CommonPage()
    yield user, commonPage
    # commonPage.logout()
    # commonPage.quit_browser()


