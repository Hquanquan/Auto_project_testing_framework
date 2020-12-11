#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 15:38
# @File : customersDetailPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 客户详情页
import allure

from pylib.UIlib.pageObjects.basePage1 import BasePage


class customersDetailPage(BasePage):

    @allure.step("step: 点击【签约客户】")
    def click_sign_CustomersBtn(self):
        """点击【签约客户】"""
        self.click(self.sign_Customers_btn)
        # 点击弹窗的确定按钮
        self.click(self.sign_Customers_confirm)







