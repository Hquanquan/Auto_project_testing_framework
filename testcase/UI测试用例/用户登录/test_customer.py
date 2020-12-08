#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 23:09
# @File : test_customer.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import time

import allure
import pytest

from pylib.UIlib.pageObjects.waitingCustomers import WaittingCustomers
from utils.tools import read_yaml

@allure.epic("UI模块-CRM系统")
@allure.feature("客户管理")
class TestCustomer:

    @pytest.fixture()
    def after_test_CreateCus(self, user_login):
        self.commonpage = user_login[1]
        self.waittingCustomers = WaittingCustomers()
        yield
        self.waittingCustomers.refresh()
        self.commonpage.click_homePagePreview()

    # @pytest.mark.skip("暂不执行")
    @allure.story("客户管理-待跟客户")
    @allure.title("创建客户")
    def test_CreateCus(self, after_test_CreateCus):
        """
        创建客户，预期结果，通过公司名称可查找到客户
        :param after_test_CreateCus:
        :return:
        """
        # 点击进入待跟客户
        self.commonpage.click_customerManagement()
        self.commonpage.click_waittingCustomers()
        # 切换到对应的待跟客户iframe,进行创建客户
        self.commonpage.switch_to_waittingCustomers_iframe()
        self.waittingCustomers.createCustomers()
        # 创建完毕，自动关闭弹窗，等待3秒，防止弹窗未关闭就进行操作导致失败
        time.sleep(3)
        # 刷新页面，重新进入待跟客户iframe
        self.commonpage.refresh()
        self.commonpage.switch_to_waittingCustomers_iframe()
        # 查找刚创建的客户
        #    获取刚才创建的客户信息
        customersInfo = read_yaml("configs/createCustomers.yaml")
        name = customersInfo["customersInfo"]["name"]
        # 根据公司名称查找客户
        self.waittingCustomers.find_customers(name)
        # 获取查找结果的列表信息
        messages = self.waittingCustomers.get_tables_costomersInfo()
        assert name == messages["name"]
