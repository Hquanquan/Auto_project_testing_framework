#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 15:38
# @File : customersDetailPage.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 客户详情页
import time

import allure

from pylib.UIlib.pageObjects.basePage1 import BasePage
from utils.tools import get_dataTime, create_Str


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

    # 获取合同状态（文案）
    def get_contractStatus(self):
        """
        获取详情页里的合同状态（文案）
        :return:
        """
        return self.get_element_text(self.contractStatus_span)

    @allure.step("step: 点击【已收回款】")
    def click_CDP_returnOperate_btn(self):
        """
        点击【已收回款】按钮
        :return:
        """
        self.click(self.CDP_returnOperate_btn)

    @allure.step("step:（内部操作）【客户详情页切换到回款审批弹窗的iframe】")
    def switch_to_CDP_returnOperate_iframe(self):
        """（内部操作）【客户详情页切换到回款审批弹窗的iframe】"""
        self.switch_to_iframe(self.CDP_returnOperate_iframe)

    # ============================= 已收回款弹窗内部操作 ========================
    @allure.step("step: 上传回款图片")
    def uploadFile_CDP_uploadFile(self):
        """
        已收回款弹窗：上传回款图片,默认上传 E:\image.jpg
        :return:
        """
        self.uploadFile_to_input(self.CDP_uploadFile_input)


    @allure.step("step: 输入回款金额")
    def send_CDP_recober_money(self, money):
        """
        已收回款弹窗：输入回款金额
        :param money: 回款金额
        :return:
        """
        self.send_keys(self.CDP_recober_money_0_input, money)

    @allure.step("step: 输入回款时间")
    def send_CDP_recTime(self, time=get_dataTime("%Y-%m-%d %H:%M:%S")):
        """
        已收回款弹窗：输入回款时间
        :param time:  默认当前时间
        :return:
        """
        self.send_keys(self.CDP_recTimeInp_input, time)

    @allure.step("step: 输入备注")
    def send_CDP_recRemark(self, text="回款备注"):
        """
        已收回款弹窗：回款备注
        :param text:  默认：回款备注+当前时间
        :return:
        """
        self.send_keys(self.CDP_recRemark_input, create_Str(text))

    @allure.step("step: 选择回款账户")
    def select_paymentAccount(self):
        """
        已收回款弹窗：选择回款账户
        :return:
        """
        self.click(self.CDP_account_input)
        self.click(self.CDP_account_options)

    @allure.step("step: 审批节点：admin")
    def select_CDP_Approver(self, approver="admin", number=1):
        """
        回款审批,分公司,区域，营销总经理审批节点都选择admin
        :param approver:
        :param number: number=1代表分公司，number=2代表区域，number=3代表营销总经理
        :return:
        """
        if number == 1:
            self.click(self.CDP_branchesApproval_node)
        elif number == 2:
            self.click(self.CDP_regionApproval_node)
        elif number == 3:
            self.click(self.CDP_marketingManagerApproval_node)

        self.click(self.CDP_treeSelect_input)
        self.send_keys(self.CDP_treeSelect_input, approver)
        self.click(self.CDP_Approver)

    @allure.step("step: 选择总经理审批节点：陆文彬")
    def select_CDP_managingDirectorApprover(self, approver="陆文彬"):
        """
        回款审批,选择总经理审批节点：陆文彬
        :param approver:
        :return:
        """
        # 选择总经理审批节点
        self.click(self.CDP_managingDirectorApproval_node)
        # 点击一下输入框
        self.click(self.CDP_treeSelect_input)
        # 输入框中输入：陆文彬
        self.send_keys(self.CDP_treeSelect_input, approver)
        # 点击选择陆文彬
        self.click(self.CDP_managingDirectorApprover)


    @allure.step("step: 选择财务审批节点：吴小玉")
    def select_CDP_financeApprover(self, approver="吴小玉"):
        """
        回款审批,选择财务审批节点：吴小玉
        :param approver:
        :return:
        """
        # 选择财务审批节点
        self.click(self.CDP_financeApproval_node)
        # 点击一下输入框
        self.click(self.CDP_treeSelect_input)
        # 输入框中输入：吴小玉
        self.send_keys(self.CDP_treeSelect_input, approver)
        # 点击选择吴小玉
        self.click(self.CDP_financeApprover)

    @allure.step("step: 点击【确定】")
    def click_comfirmBtn(self):
        """
        已收回款弹窗,点击确定按钮，进入回款审批流程
        :return:
        """
        self.click(self.CDP_comfirm_btn)

    # ======================回款审批操作===============================

    @allure.step("step: 点击【回款审批】")
    def click_paymentApproval_btn(self):
        """
        客户详情页，点击【回款审批】，弹出窗口
        :return:
        """
        self.click(self.paymentApproval_btn)

    @allure.step("step: 回款审批时填写审批信息")
    def send_CDP_recRemark1(self, text="审批通过"):
        """
        回款审批时填写审批信息
        :param text:
        :return:
        """
        self.send_keys(self.CDP_approvalRemark_textarea, create_Str(text))

    @allure.step("step: 点击回款审批弹窗的【确定】按钮")
    def click_CDP_comfirm_btn1(self):
        """
        点击回款审批弹窗的【确定】按钮
        :return:
        """
        self.click(self.CDP_comfirm_btn1)

    @allure.step("step: 输入【立项时间】")
    def send_CDP_proAppTime(self):
        """
        输入立项时间，默认选择当月
        :return:
        """
        self.click(self.CDP_proAppTime_input)
        self.send_keys(self.CDP_proAppTime_input, get_dataTime(time_formate="%Y-%m"))
    # 选择通过
    def select_CDP_pass(self):
        """
        选择通过
        :return:
        """
        self.click(self.CDP_pass)






