#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 15:09
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统已有客户
import time

import allure
import pytest

from pylib.UIlib.pageObjects.waitingCustomers import WaittingCustomersPage
from utils.tools import read_yaml

@pytest.fixture(scope="session")
@allure.suite("step:【初始化创建客户】")
def init_customers(user_login):
    """
    初始化创建客户
    :param user_login:
    :return:
    """
    commonPage = user_login[1]
    waittingCustomers = WaittingCustomersPage()
    # 点击进入待跟客户
    commonPage.click_customerManagement()
    commonPage.click_waittingCustomers()
    # 切换到对应的待跟客户iframe,进行创建客户
    commonPage.switch_to_waittingCustomers_iframe()
    waittingCustomers.createCustomers()
    # 创建完毕，自动关闭弹窗，等待3秒，防止弹窗未关闭就进行操作导致失败
    time.sleep(3)
    customersInfo = read_yaml("configs/createCustomers.yaml")

    # 刷新页面，重新进入待跟客户iframe
    commonPage.refresh()
    commonPage.switch_to_waittingCustomers_iframe()
    # 查找刚创建的客户
    #    获取刚才创建的客户信息
    customersInfo = read_yaml("configs/createCustomers.yaml")

    # name = customersInfo["customersInfo"]["name"]
    # # 根据公司名称查找客户
    # waittingCustomers.find_customers(name)
    # # 获取查找结果的列表信息
    # customersInfo = waittingCustomers.get_tables_costomersInfo()

    # 待跟客户页面刷新,退出iframe
    waittingCustomers.refresh()
    # 点击首页
    commonPage.click_homePagePreview()

    yield commonPage, waittingCustomers, customersInfo



