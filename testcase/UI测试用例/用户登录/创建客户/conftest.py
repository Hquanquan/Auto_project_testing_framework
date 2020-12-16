#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 15:09
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 初始化创建客户，提供新创建的客户信息
import time

import pytest
from pylib.UIlib.pageObjects.waitingCustomersPage import WaittingCustomersPage
from utils.tools import read_yaml



@pytest.fixture()
def init_customers(user_login):
    """
    初始化，创建客户，提供客户进行签约
    :param user_login:
    :return:
    """
    commonPage = user_login[1]
    waittingCustomersPage = WaittingCustomersPage()
    # 点击客户管理
    commonPage.click_customerManagement()
    # 点击待跟客户
    commonPage.click_waittingCustomers()
    # 切换到对应的待跟客户iframe
    commonPage.switch_to_waittingCustomers_iframe()
    # 进行创建客户
    waittingCustomersPage.createCustomers()
    # 创建完毕，自动关闭弹窗，等待3秒，防止弹窗未关闭就进行操作导致失败
    time.sleep(3)
    # 查找刚创建的客户
    #    获取刚才创建的客户信息
    customersInfo = read_yaml("configs/createCustomers.yaml")
    # 关闭待跟客户tab,自动回到首页
    commonPage.close_WaittingCustomersPage_tab()
    # 返回需要的数据
    yield commonPage, waittingCustomersPage, customersInfo



@pytest.fixture(scope="session")
def create_customers(user_login):
    """
    初始化，创建客户，提供客户进行签约
    :param user_login:
    :return:
    """
    commonPage = user_login[1]
    waittingCustomersPage = WaittingCustomersPage()
    # 点击进入待跟客户
    commonPage.click_customerManagement()
    commonPage.click_waittingCustomers()
    # 切换到对应的待跟客户iframe
    commonPage.switch_to_waittingCustomers_iframe()
    # 进行创建客户
    waittingCustomersPage.createCustomers()
    # 创建完毕，自动关闭弹窗，等待3秒，防止弹窗未关闭就进行操作导致失败
    time.sleep(3)
    # 查找刚创建的客户
    #    获取刚才创建的客户信息
    customersInfo = read_yaml("configs/createCustomers.yaml")
    # 关闭待跟客户tab,自动回到首页
    commonPage.close_WaittingCustomersPage_tab()
    yield commonPage, waittingCustomersPage, customersInfo


