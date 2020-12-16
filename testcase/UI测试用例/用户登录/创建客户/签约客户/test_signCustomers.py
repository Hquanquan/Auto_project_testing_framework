#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 14:08
# @File : test_signCustomers.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import allure
import pytest


@allure.epic("UI模块-CRM系统")
@allure.feature("客户管理")
class Test_SignCustomers:

    @pytest.fixture()
    def before_test_signedCustomers(self, init_signedCustomers):
        # 签约客户
        self.commonPage = init_signedCustomers[0]
        self.signedCustomersPage = init_signedCustomers[1]
        self.customersDetailPage = init_signedCustomers[2]
        self.costomersInfo = init_signedCustomers[3]


    @allure.story("客户管理-待跟客户")
    @allure.title("签约客户")
    @pytest.mark.skip("暂不执行")
    def test_signedCustomers(self, before_test_signedCustomers):
        print("============== test_signedCustomers ===================")
        pass




