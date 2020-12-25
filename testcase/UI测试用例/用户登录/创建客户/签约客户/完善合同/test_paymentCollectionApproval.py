#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 9:32
# @File : test_paymentCollectionApproval.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 回款审批流
import time

import pytest


class TestPaymentCollectionApproval:

    @pytest.fixture()
    def after_test_paymentCollectionApproval(self, init_prefectContract):
        self.commonPage = init_prefectContract[0]
        self.signedCustomersPage = init_prefectContract[1]
        self.customersDetailPage = init_prefectContract[2]
        self.costomersInfo = init_prefectContract[3]
        yield
        self.customersDetailPage.switch_to_default_content()
        self.commonPage.close_SignedCustomersPage_tab()

    def test_paymentCollectionApproval(self, after_test_paymentCollectionApproval):
        """
        发起回款审批，预期结果合同状态显示：等待回款审批
        :param after_test_paymentCollectionApproval:
        :return:
        """
        # 点击【已收回款】按钮
        self.customersDetailPage.click_CDP_returnOperate_btn()
        # 切换到已收回款弹窗iframe
        self.customersDetailPage.switch_to_CDP_returnOperate_iframe()

        # 上传回款图片
        self.customersDetailPage.uploadFile_CDP_uploadFile()
        # 输入回款金额
        self.customersDetailPage.send_CDP_recober_money(60000)
        # 输入回款时间
        self.customersDetailPage.send_CDP_recTime()
        # 输入回款备注
        self.customersDetailPage.send_CDP_recRemark()
        # 选择回款账户
        self.customersDetailPage.select_paymentAccount()
        # 分公司负责人审批节点选择审批人admin
        self.customersDetailPage.select_CDP_Approver()
        # 点击确定按钮
        self.customersDetailPage.click_comfirmBtn()
        time.sleep(2)
        # =========== 切换iframe 否则无法获取元素===============
        # 刷新页面，回到签约客户列表页
        self.customersDetailPage.refresh()
        # 切换iframe到签约客户列表页iframe
        self.commonPage.switch_to_signedCustomersPage_iframe()
        # 进入客户详情页
        self.signedCustomersPage.enter_customerDetail()
        # 切换iframe到客户详情页
        self.signedCustomersPage.switch_to_CustomersDetailPage_iframe()
        # 断言
        assert self.customersDetailPage.get_contractStatus() == "等待回款审批（分公司负责人-->admin）"














