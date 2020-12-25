#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 15:10
# @File : paymentApprovalPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 财务管理的回款审批页
import allure

from pylib.UIlib.pageObjects.basePage1 import BasePage


class PaymentApprovalPage(BasePage):

    @allure.step("step:财务管理-回款审批页里查找客户")
    def find_customers(self, keyword):
        """
        在财务管理-回款审批页里查找客户
        :param keyword:
        :return:
        """
        # 输入框中输入客户名称
        self.send_keys(self.PAG_customerNameOrCode_input, keyword)
        # 点击查询按钮
        self.click(self.PAG_search_btn)
        return self

    @allure.step("step:点击财务管理-回款审批列表里的【详情】按钮")
    def click_detail_btn(self):
        """
        点击财务管理-回款审批列表里的【详情】按钮，进入客户详情页
        :return:
        """
        self.click(self.PAG_table_detail_btn)
        # # 找到一组详情按钮，其中下标为1的是准确的
        # eles = self.find_elements(self.PAG_table_detail_btn)
        # eles[1].click()

    @allure.step("step:【内部操作：财务管理-回款审批页切换到客户详情iframe】")
    def switch_to_PAG_customers_detail_iframe(self):
        """
        切换到回款审批里的客户详情页
        :return:
        """
        self.switch_to_iframe(self.PAG_customers_detail_iframe)

    @allure.step("step:点击【已审批】tab")
    def switch_to_PAG_approved_tab(self):
        """
        切换到财务管理-回款审批的已审批tab
        :return:
        """
        self.click(self.PAG_approved_tab)




