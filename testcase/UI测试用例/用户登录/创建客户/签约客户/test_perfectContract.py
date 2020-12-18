#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 14:43
# @File : test_perfectContract.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 完善合同
import time

import allure
import pytest

from pylib.UIlib.pageObjects.perfectContractPage import PerfectContractPage


@allure.epic("UI模块-CRM系统")
@allure.feature("客户管理")
class TestContract:

    @pytest.fixture()
    def before_test_perfectContract(self, init_signedCustomers):
        # 创建客户并签约客户
        self.commonPage = init_signedCustomers[0]
        self.signedCustomersPage = init_signedCustomers[1]
        self.customersDetailPage = init_signedCustomers[2]
        self.costomersInfo = init_signedCustomers[3]
        self.perfectContractPage = PerfectContractPage()
        # 点击客户管理
        self.commonPage.click_customerManagement()
        # 点击签约客户
        self.commonPage.click_signedCustomersPage()
        # 切换到签约客户页iframe
        self.commonPage.switch_to_signedCustomersPage_iframe()
        time.sleep(2)
        # 查找签约客户
        self.signedCustomersPage.find_signedCustomers(self.costomersInfo["customersInfo"]["name"])
        # 进入客户详情页
        self.signedCustomersPage.enter_customerDetail()
        # 【内部操作：签约客户列表页切换到客户详情iframe】
        self.signedCustomersPage.switch_to_CustomersDetailPage_iframe()
        # 点击完善合同按钮，进入完善合同页面
        self.customersDetailPage.click_perfectContractBtn()
        # 【内部操作：签约客户列表页切换到客户详情iframe】
        self.customersDetailPage.switch_to_perfectContractPage_iframe()
        yield
        self.customersDetailPage.switch_to_default_content()
        self.commonPage.close_SignedCustomersPage_tab()

    @allure.story("客户管理-签约客户")
    @allure.title("完善合同")
    def test_perfectContract(self, before_test_perfectContract):
        # 编辑基本信息
        self.perfectContractPage.edit_basicInformation()
        # 编辑费用明细
        self.perfectContractPage.edit_costDetail()
        # 编辑回款计划
        self.perfectContractPage.edit_paymentPlan()
        # 编辑资质配置
        self.perfectContractPage.edit_qualificationConfiguration()
        # 编辑安证配置
        self.perfectContractPage.edit_cerConfiguration()
        # 点击保存信息按钮
        self.perfectContractPage.click_saveBtn()
        time.sleep(1)
        # =========== 切换iframe 否则无法获取元素===============
        # 回到默认的iframe
        self.perfectContractPage.switch_to_default_content()
        # 切换iframe到签约客户列表页iframe
        self.commonPage.switch_to_signedCustomersPage_iframe()
        # 切换iframe到客户详情页
        self.signedCustomersPage.switch_to_CustomersDetailPage_iframe()
        # 断言
        assert self.customersDetailPage.get_contractStatus() == "等待首款回款"




