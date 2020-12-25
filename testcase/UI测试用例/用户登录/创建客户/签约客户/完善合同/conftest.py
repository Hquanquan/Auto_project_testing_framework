#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 9:15
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 完善合同
import time

import pytest

from pylib.UIlib.pageObjects.perfectContractPage import PerfectContractPage

@pytest.fixture()
def init_prefectContract(init_signedCustomers):
    # 创建客户并签约客户
    commonPage = init_signedCustomers[0]
    signedCustomersPage = init_signedCustomers[1]
    customersDetailPage = init_signedCustomers[2]
    costomersInfo = init_signedCustomers[3]
    perfectContractPage = PerfectContractPage()
    # 点击客户管理
    commonPage.click_customerManagement()
    # 点击签约客户
    commonPage.click_signedCustomersPage()
    # 切换到签约客户页iframe
    commonPage.switch_to_signedCustomersPage_iframe()
    time.sleep(2)
    # 查找签约客户
    signedCustomersPage.find_signedCustomers(costomersInfo["customersInfo"]["name"])
    # 进入客户详情页
    signedCustomersPage.enter_customerDetail()
    # 【内部操作：签约客户列表页切换到客户详情iframe】
    signedCustomersPage.switch_to_CustomersDetailPage_iframe()
    # 点击完善合同按钮，进入完善合同页面
    customersDetailPage.click_perfectContractBtn()
    # 【内部操作：签约客户列表页切换到客户详情iframe】
    customersDetailPage.switch_to_perfectContractPage_iframe()
    # 编辑基本信息
    perfectContractPage.edit_basicInformation()
    # 编辑费用明细
    perfectContractPage.edit_costDetail()
    # 编辑回款计划
    perfectContractPage.edit_paymentPlan()
    # 编辑资质配置
    perfectContractPage.edit_qualificationConfiguration()
    # 编辑安证配置
    perfectContractPage.edit_cerConfiguration()
    # 点击保存信息按钮
    perfectContractPage.click_saveBtn()
    time.sleep(1)
    # =========== 切换iframe 否则无法获取元素===============
    # 回到默认的iframe
    perfectContractPage.switch_to_default_content()
    # 切换iframe到签约客户列表页iframe
    commonPage.switch_to_signedCustomersPage_iframe()
    # 切换iframe到客户详情页
    signedCustomersPage.switch_to_CustomersDetailPage_iframe()
    yield commonPage, signedCustomersPage, customersDetailPage, costomersInfo

