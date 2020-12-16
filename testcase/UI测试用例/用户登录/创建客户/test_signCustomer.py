#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 14:53
# @File : test_signCustomer.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统有客户，没有签约客户
import allure
import pytest

from pylib.UIlib.pageObjects.commonPage import CommonPage
from pylib.UIlib.pageObjects.customersDetailPage import CustomersDetailPage
from pylib.UIlib.pageObjects.signedCustomersPage import SignedCustomersPage
from pylib.UIlib.pageObjects.waitingCustomersPage import WaittingCustomersPage


@allure.epic("UI模块-CRM系统")
@allure.feature("客户管理")
class Test_SignCustomers:

    @pytest.fixture()
    def before_test_signedCustomer(self, init_customers):
        """
        签约客户前的环境设置
        :param init_customers: 创建客户，提供客户进行签约
        :return:
        """
        self.commonPage = init_customers[0]
        self.waittingCustomersPage = init_customers[1]
        self.costomersInfo = init_customers[2]
        self.customersDetailPage = CustomersDetailPage()
        self.signedCustomersPage = SignedCustomersPage()
        # 点击客户管理
        self.commonPage.click_customerManagement()
        # 点击待跟客户
        self.commonPage.click_waittingCustomers()
        # 切换到对应的待跟客户iframe
        self.commonPage.switch_to_waittingCustomers_iframe()
        # 根据公司名称查找客户
        name = self.costomersInfo["customersInfo"]["name"]
        self.waittingCustomersPage.find_customers(name)
        # 点击待跟客户列表的详情按钮，进入客户详情页
        self.waittingCustomersPage.click_detail_btn()
        # time.sleep(3)
        # 切换到客户详情页的ifram
        self.waittingCustomersPage.switch_to_customers_datail_iframe()
        yield
        # 回到默认的iframe
        self.signedCustomersPage.switch_to_default_content()
        # 关闭签约客户tab页
        self.commonPage.close_SignedCustomersPage_tab()

    @allure.story("客户管理-待跟客户")
    @allure.title("签约客户")
    # @pytest.mark.skip("暂不执行")
    def test_signedCustomer(self, before_test_signedCustomer):
        """
        当前系统没有签约客户，进行签约客户操作。预期结果在签约客户列表查找到该客户
        :param before_test_signedCustomer:
        :return:
        """
        # 点击客户详情页里的签约客户按钮
        self.customersDetailPage.click_sign_CustomersBtn()
        # 回到主页iframe
        self.customersDetailPage.switch_to_default_content()
        # 关闭待跟客户tab页
        self.commonPage.close_WaittingCustomersPage_tab()
        # 点击客户管理
        self.commonPage.click_customerManagement()
        # 点击签约客户列表页
        self.commonPage.click_signedCustomersPage()
        # 切换到签约客户iframe
        self.commonPage.switch_to_signedCustomersPage_iframe()
        # 查找签约客户
        self.signedCustomersPage.find_signedCustomers(self.costomersInfo["customersInfo"]["name"])
        # 获取签约客户列表里单行数据里的公司名称
        name = self.signedCustomersPage.get_tables_signedCostomersInfo()
        # 断言 签约客户名称一致
        assert name == self.costomersInfo["customersInfo"]["name"]


