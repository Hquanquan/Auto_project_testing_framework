#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 15:26
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 发起回款审批
import time

import pytest


@pytest.fixture()
def init_paymentCollectionApproval(init_prefectContract):
    commonPage = init_prefectContract[0]
    signedCustomersPage = init_prefectContract[1]
    customersDetailPage = init_prefectContract[2]
    costomersInfo = init_prefectContract[3]
    # 点击【已收回款】按钮
    customersDetailPage.click_CDP_returnOperate_btn()
    # 切换到已收回款弹窗iframe
    customersDetailPage.switch_to_CDP_returnOperate_iframe()
    # 上传回款图片
    customersDetailPage.uploadFile_CDP_uploadFile()
    # 输入回款金额 60000
    customersDetailPage.send_CDP_recober_money(60000)
    # 输入回款时间 默认当前时间
    customersDetailPage.send_CDP_recTime()
    # 输入回款备注 默认 回款备注+当前时间
    customersDetailPage.send_CDP_recRemark()
    # 选择回款账户 默认选第一个
    customersDetailPage.select_paymentAccount()
    # 选择审批人 默认选择admin
    customersDetailPage.select_CDP_Approver()
    # 点击确定按钮
    customersDetailPage.click_comfirmBtn()
    time.sleep(2)
    # 此时页面在客户详情页，iframe
    yield commonPage, signedCustomersPage, customersDetailPage, costomersInfo
