#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 13:57
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 签约客户
import pytest

from pylib.UIlib.pageObjects.customersDetailPage import CustomersDetailPage
from pylib.UIlib.pageObjects.signedCustomersPage import SignedCustomersPage

@pytest.fixture()
def init_signedCustomers(init_customers):
    commonPage = init_customers[0]
    waittingCustomersPage = init_customers[1]
    costomersInfo = init_customers[2]
    customersDetailPage = CustomersDetailPage()
    signedCustomersPage = SignedCustomersPage()

    # 点击客户管理
    commonPage.click_customerManagement()
    # 点击待跟客户
    commonPage.click_waittingCustomers()
    # 切换到对应的待跟客户iframe
    commonPage.switch_to_waittingCustomers_iframe()
    # 根据公司名称查找客户
    name = costomersInfo["customersInfo"]["name"]
    waittingCustomersPage.find_customers(name)
    # 点击待跟客户列表的详情按钮，进入客户详情页
    waittingCustomersPage.click_detail_btn()
    # time.sleep(3)
    # 切换到客户详情页的ifram
    waittingCustomersPage.switch_to_customers_datail_iframe()
    # 点击客户详情页里的签约客户按钮
    customersDetailPage.click_sign_CustomersBtn()
    # 回到主页iframe
    customersDetailPage.switch_to_default_content()
    # 关闭待跟客户tab页
    commonPage.close_WaittingCustomersPage_tab()
    yield commonPage, signedCustomersPage, customersDetailPage, costomersInfo




