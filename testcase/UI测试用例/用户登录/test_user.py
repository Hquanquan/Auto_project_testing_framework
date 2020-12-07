#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 23:09
# @File : test_user.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import time

import pytest

from pylib.UIlib.pageObjects.waitingCustomers import WaittingCustomers


class TestUser:

    @pytest.mark.skip("暂不执行")
    def test_user(self, user_login):
        self.commonpage = user_login[1]
        time.sleep(2)
        self.commonpage.click_customerManagement()
        time.sleep(2)
        self.commonpage.click_qualificationManagement()
        time.sleep(2)
        self.commonpage.click_publicResource()
        time.sleep(2)
        self.commonpage.click_financialManagement()
        time.sleep(2)
        self.commonpage.click_CustomerServiceManagement()
        time.sleep(2)
        self.commonpage.click_dataStatistics()
        time.sleep(2)
        self.commonpage.click_OA_collaboration()
        time.sleep(2)
        self.commonpage.click_SystemSettings()
        time.sleep(2)
        self.commonpage.click_homePagePreview()

        assert self.commonpage.get_url_title() == "CRM管理系统"

    # @pytest.mark.skip("暂不执行")
    def test_CreateCus(self, user_login):
        self.commonpage = user_login[1]
        self.waittingCustomers = WaittingCustomers()
        self.commonpage.click_customerManagement()
        self.commonpage.click_waittingCustomers()
        self.commonpage.switch_to_myiframe()
        self.waittingCustomers.createCustomers()


