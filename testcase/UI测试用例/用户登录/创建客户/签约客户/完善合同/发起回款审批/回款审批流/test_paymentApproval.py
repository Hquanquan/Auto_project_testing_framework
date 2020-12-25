#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 10:30
# @File : test_paymentApproval.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 回款审批流
import time

import pytest

from pylib.UIlib.pageObjects.loginPage import LoginPage
from pylib.UIlib.pageObjects.paymentApprovalPage import PaymentApprovalPage


class TestPaymentApproval:

    @pytest.fixture()
    def after_test_paymentApproval(self, init_paymentCollectionApproval):
        self.commonPage = init_paymentCollectionApproval[0]
        self.signedCustomersPage = init_paymentCollectionApproval[1]
        self.customersDetailPage = init_paymentCollectionApproval[2]
        self.costomersInfo = init_paymentCollectionApproval[3]
        yield
        self.customersDetailPage.refresh()
        # 关闭回款审批tab页
        self.commonPage.close_SignedCustomersPage_tab()



    def test_paymentApproval(self, after_test_paymentApproval):
        """
        回款审批流：
        分公司负责人审批:admin => 区域负责人审批:admin =>
        营销总经理审批:admin => 总经理审批:朱炜杰 => 财务审批 :吴小玉
        :param after_test_paymentApproval:
        :return:
        """
        # 获取回款审批的客户公司名称
        self.costomersName = self.costomersInfo["customersInfo"]["name"]
        # ============== 此时页面在签约客户-客户详情页 ===========
        # 刷新页面，回到签约客户列表页
        self.customersDetailPage.refresh()
        time.sleep(2)
        # 退出当前账号
        self.commonPage.logout()

        # ======================== 分公司负责人审批 =========================
        # 登录审批人账号
        LoginPage().login("18819443338", "18819443338")
        # 点击客户管理
        self.commonPage.click_customerManagement()
        # 点击签约客户
        self.commonPage.click_signedCustomersPage()
        # 切换到签约客户iframe
        self.commonPage.switch_to_signedCustomersPage_iframe()
        # 按公司名称查找签约客户
        self.signedCustomersPage.find_signedCustomers(self.costomersName)
        # 查找到客户后，点击【详情】进入客户详情
        self.signedCustomersPage.enter_customerDetail()
        # 切换到客户详情页iframe
        self.signedCustomersPage.switch_to_CustomersDetailPage_iframe()
        # 点击客户详情页的【回款审批】按钮
        self.customersDetailPage.click_paymentApproval_btn()
        # 切换到回款审批弹窗iframe
        self.customersDetailPage.switch_to_CDP_returnOperate_iframe()
        # 选择区域负责人审批：admin
        self.customersDetailPage.select_CDP_Approver(number=2)
        # 回款审批信息
        self.customersDetailPage.send_CDP_recRemark1("分公司负责人审批通过，下一步区域负责人审批")
        # 点击回款审批弹窗的确定按钮
        self.customersDetailPage.click_CDP_comfirm_btn1()
        # 此时页面回到签约客户列表里的客户详情页
        time.sleep(2)
        # ==================== 区域负责人审批 =================================
        self.customersDetailPage.switch_to_default_content()
        self.commonPage.switch_to_signedCustomersPage_iframe()
        self.signedCustomersPage.switch_to_CustomersDetailPage_iframe()

        # 点击客户详情页的【回款审批】按钮
        self.customersDetailPage.click_paymentApproval_btn()
        # 切换到回款审批弹窗iframe
        self.customersDetailPage.switch_to_CDP_returnOperate_iframe()
        # 选择营销总经理审批：admin
        self.customersDetailPage.select_CDP_Approver(number=3)
        # 回款审批信息
        self.customersDetailPage.send_CDP_recRemark1("区域负责人审批通过，下一步营销总经理审批")
        # 点击回款审批弹窗的确定按钮
        self.customersDetailPage.click_CDP_comfirm_btn1()
        time.sleep(2)
        # ==================== 营销总经理审批 =================================
        self.customersDetailPage.switch_to_default_content()
        self.commonPage.switch_to_signedCustomersPage_iframe()
        self.signedCustomersPage.switch_to_CustomersDetailPage_iframe()
        # 点击客户详情页的【回款审批】按钮
        self.customersDetailPage.click_paymentApproval_btn()
        # 切换到回款审批弹窗iframe
        self.customersDetailPage.switch_to_CDP_returnOperate_iframe()
        # 选择总经理审批：陆文彬
        self.customersDetailPage.select_CDP_managingDirectorApprover()
        # 回款审批信息
        self.customersDetailPage.send_CDP_recRemark1("营销总经理审批审批通过，下一步总经理审批 ")
        # 点击回款审批弹窗的确定按钮
        self.customersDetailPage.click_CDP_comfirm_btn1()
        # ============== 此时页面在签约客户-客户详情页 ===========
        # 刷新页面，回到签约客户列表页
        self.customersDetailPage.refresh()
        time.sleep(2)
        # 退出当前账号
        self.commonPage.logout()

        # ==================== 总经理审批 =================================
        # 登录审批人账号:陆文彬 13602477326
        LoginPage().login("13602477326", "13602477326")
        # 点击客户管理
        self.commonPage.click_customerManagement()
        # 点击签约客户
        self.commonPage.click_signedCustomersPage()
        # 切换到签约客户iframe
        self.commonPage.switch_to_signedCustomersPage_iframe()
        # 切换到待我审批tab
        self.signedCustomersPage.switch_to_SiCus_Wait_for_me_approval_tab()
        # 按公司名称查找签约客户
        self.signedCustomersPage.find_signedCustomers(self.costomersName)
        # 查找到客户后，点击【详情】进入客户详情
        self.signedCustomersPage.enter_customerDetail()
        # 切换到客户详情页iframe
        self.signedCustomersPage.switch_to_CustomersDetailPage_iframe()
        # 点击客户详情页的【回款审批】按钮
        self.customersDetailPage.click_paymentApproval_btn()
        # 切换到回款审批弹窗iframe
        self.customersDetailPage.switch_to_CDP_returnOperate_iframe()
        # 选择财务审批节点：吴小玉
        self.customersDetailPage.select_CDP_financeApprover()
        # 回款审批信息
        self.customersDetailPage.send_CDP_recRemark1("总经理审批审批通过，下一步财务审批 ")
        # 点击回款审批弹窗的确定按钮
        self.customersDetailPage.click_CDP_comfirm_btn1()
        # ============== 此时页面在签约客户-客户详情页 ===========
        # 刷新页面，回到签约客户列表页
        self.customersDetailPage.refresh()
        time.sleep(2)
        # 退出当前账号
        self.commonPage.logout()
        # ==================== 财务审批 =================================
        # 登录审批人账号:吴小玉 18613083885
        LoginPage().login("18613083885", "18613083885")
        # 点击财务管理
        self.commonPage.click_financialManagement()
        # 点击回款审批
        self.commonPage.click_paymentApproval()
        # 切换到财务管理-回款审批iframe
        self.commonPage.switch_to_financeManagement_paymentApproval_iframe()
        # 创建回款审批页的对象
        self.paymentApprovalPage = PaymentApprovalPage()
        # 查找回款审批页里的客户
        self.paymentApprovalPage.find_customers(self.costomersName)
        # 点击找到的客户列表里的【详情】按钮
        self.paymentApprovalPage.click_detail_btn()
        # 切换到客户详情页的iframe
        self.paymentApprovalPage.switch_to_PAG_customers_detail_iframe()
        # 点击客户详情页里的【回款审批】按钮
        self.customersDetailPage.click_paymentApproval_btn()
        # 切换到回款审批弹窗的iframe
        self.customersDetailPage.switch_to_CDP_returnOperate_iframe()
        # 输入立项时间
        self.customersDetailPage.send_CDP_proAppTime()
        # 输入审批信息
        self.customersDetailPage.send_CDP_recRemark1("财务审批通过！")
        # 选择通过
        self.customersDetailPage.select_CDP_pass()
        # 点击确定
        self.customersDetailPage.click_CDP_comfirm_btn1()
        time.sleep(2)

        # =========== 切换iframe 否则无法获取元素===============
        # 刷新页面
        self.customersDetailPage.refresh()
        # 切换iframe回到财务管理-回款审批列表页iframe
        self.commonPage.switch_to_financeManagement_paymentApproval_iframe()
        # 切换到已审批tab
        self.paymentApprovalPage.switch_to_PAG_approved_tab()
        # 查找回款审批页里的客户
        self.paymentApprovalPage.find_customers(self.costomersName)
        # 点击找到的客户列表里的【详情】按钮
        self.paymentApprovalPage.click_detail_btn()
        # 切换到客户详情页的iframe
        self.paymentApprovalPage.switch_to_PAG_customers_detail_iframe()
        # 断言
        assert self.customersDetailPage.get_contractStatus() == "等待人才下单"



