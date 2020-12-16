#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 15:23
# @File : signedCustomersPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 签约客户列表页
import time

import allure

from pylib.UIlib.pageObjects.basePage1 import BasePage


class SignedCustomersPage(BasePage):
    """
    签约客户列表页
    """

    @allure.step("step:【查找签约客户】")
    def find_signedCustomers(self, keyword):
        """
        查找签约客户
        :param keyword: 搜索关键字
        :return:
        """
        self.send_keys(self.SiCus_keyword_input, keyword)
        # time.sleep(2)
        # 点击查询按钮
        self.click(self.SiCus_search_btn)
        return self

    # 获取查找客户后的列表客户信息
    @allure.step("step:【获取查找客户后的列表客户信息】")
    def get_tables_signedCostomersInfo(self):
        """
        获取签约客户列表里单行数据里的公司名称
        :return:
        """
        costomersName = self.find_element(self.SiCus_table_name_locator).text
        return costomersName

    @allure.step("step:【进入客户详情】")
    def enter_customerDetail(self):
        """
        进入客户详情
        :return:
        """
        self.click(self.SiCus_table_name_locator)

    @allure.step("step:【内部操作：签约客户列表页切换到客户详情iframe】")
    def switch_to_CustomersDetailPage_iframe(self):
        """【内部操作：签约客户列表页切换到客户详情iframe】"""
        self.switch_to_iframe(self.CustomersDetailPage_iframe)




