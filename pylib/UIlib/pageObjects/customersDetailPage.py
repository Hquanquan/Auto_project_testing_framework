#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 15:38
# @File : customersDetailPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 客户详情页
import allure

from pylib.UIlib.pageObjects.basePage1 import BasePage


class CustomersDetailPage(BasePage):
    """
    客户详情页
    """

    @allure.step("step: 点击【签约客户】")
    def click_sign_CustomersBtn(self):
        """点击【签约客户】"""
        self.click(self.sign_Customers_btn)
        # 点击弹窗的确定按钮
        self.click(self.sign_Customers_confirm)

    @allure.step("step: 点击【完善合同】")
    def click_perfectContractBtn(self):
        """点击【完善合同】按钮"""
        self.click(self.perfectOperate_btn)

    @allure.step("step:（内部操作）【客户详情页切换到完善合同页的iframe】")
    def switch_to_perfectContractPage_iframe(self):
        """【内部操作:客户详情页切换到完善合同页的iframe】 """
        self.switch_to_iframe(self.PerfectContractPage_iframe)





