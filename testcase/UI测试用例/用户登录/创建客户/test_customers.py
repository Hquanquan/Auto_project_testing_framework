#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 14:52
# @File : test_customers.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 环境:自动构造创建已存在客户
import time

import allure
import pytest

from pylib.UIlib.pageObjects.customersDetailPage import customersDetailPage
from utils.tools import read_yaml


@allure.epic("UI模块-CRM系统")
@allure.feature("客户管理")
class TestCustomer:

    @pytest.fixture()
    def before_test_createCustomer(self, init_customers):
        self.commonPage = init_customers[0]
        self.waittingCustomers = init_customers[1]
        self.costomersInfo = init_customers[2]
        yield
        self.waittingCustomers.refresh()
        self.commonPage.click_homePagePreview()

    @allure.story("客户管理-待跟客户")
    @allure.title("创建客户")
    @pytest.mark.skip("暂不执行")
    def test_createCustomer(self, before_test_createCustomer):
        """
        当前账号已有客户，创建一个新的客户
        :return:
        """
        # 点击进入待跟客户
        self.commonPage.click_customerManagement()
        self.commonPage.click_waittingCustomers()
        # 切换到对应的待跟客户iframe,进行创建客户
        self.commonPage.switch_to_waittingCustomers_iframe()
        self.waittingCustomers.createCustomers()
        # 创建完毕，自动关闭弹窗，等待3秒，防止弹窗未关闭就进行操作导致失败
        time.sleep(3)

        # 刷新页面，重新进入待跟客户iframe
        self.commonPage.refresh()
        self.commonPage.switch_to_waittingCustomers_iframe()

        # # 查找刚创建的客户
        # #    获取刚才创建的客户信息
        # customersInfo = read_yaml("configs/createCustomers.yaml")
        name = self.customersInfo["customersInfo"]["name"]
        # 根据公司名称查找客户
        self.waittingCustomers.find_customers(name)
        # 获取查找结果的列表信息
        messages = self.waittingCustomers.get_tables_costomersInfo()
        assert name == messages["name"]


    @pytest.fixture()
    def before_test_contract_sign(self, init_customers):
        self.commonPage = init_customers[0]
        self.waittingCustomers = init_customers[1]
        self.costomersInfo = init_customers[2]
        self.customersDetailPage = customersDetailPage()
        # 点击进入待跟客户
        self.commonPage.click_customerManagement()
        self.commonPage.click_waittingCustomers()
        # 切换到对应的待跟客户iframe
        self.commonPage.switch_to_waittingCustomers_iframe()
        name = self.costomersInfo["customersInfo"]["name"]
        # 根据公司名称查找客户
        self.waittingCustomers.find_customers(name)
        time.sleep(2)
        # 点击客户列表的详情按钮，进入客户详情页
        self.waittingCustomers.click_detail_btn()

        time.sleep(3)
        # 切换到客户详情页的ifram

        self.waittingCustomers.switch_to_customers_datail_iframe()
        yield



    @allure.story("客户管理-待跟客户")
    @allure.title("签约客户")
    def test_contract_sign(self, before_test_contract_sign):
        """
        签约客户
        :param before_test_contract_sign:
        :return:
        """
        # 点击签约客户
        self.customersDetailPage.click_sign_CustomersBtn()
        # 回到主页iframe
        self.customersDetailPage.switch_to_default_content()
        self.commonPage.click_homePagePreview()
        self.commonPage.click_customerManagement()
        self.commonPage.c

        print("===============")














