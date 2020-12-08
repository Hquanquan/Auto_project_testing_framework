#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 22:59
# @File : commonPage.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
from pylib.UIlib.pageObjects.basePage1 import BasePage


class CommonPage(BasePage):


    def logout(self):
        """
        退出当前账号
        :return:
        """
        self.click(self.logout_btn)
        self.click(self.logout_confirm)
        return self

    # ================左侧菜单栏=============================

    def click_homePagePreview(self):
        """
        点击首页预览
        :return:
        """
        if self.isdispaly(self.homePagePreview):
            self.click(self.homePagePreview)
        return self

    def click_customerManagement(self):
        """
        点击客户管理
        :return:
        """
        if self.isdispaly(self.customerManagement):
            self.click(self.customerManagement)
        return self

    def click_waittingCustomers(self):
        """
        点击待跟客户
        :return:
        """
        if self.isdispaly(self.waittingCustomers):
            self.click(self.waittingCustomers)
        return self

    def click_qualificationManagement(self):
        """
        点击资质办理
        :return:
        """
        if self.isdispaly(self.qualificationManagement):
            self.click(self.qualificationManagement)
        return self

    def click_publicResource(self):
        """
        点击资质办理
        :return:
        """
        if self.isdispaly(self.publicResource):
            self.click(self.publicResource)
        return self

    def click_financialManagement(self):
        """
        点击财务管理
        :return:
        """
        if self.isdispaly(self.financialManagement):
            self.click(self.financialManagement)
        return self

    def click_CustomerServiceManagement(self):
        """
        点击客服管理
        :return:
        """
        if self.isdispaly(self.CustomerServiceManagement):
            self.click(self.CustomerServiceManagement)
        return self

    def click_dataStatistics(self):
        """
        点击数据统计
        :return:
        """
        if self.isdispaly(self.dataStatistics):
            self.click(self.dataStatistics)
        return self

    def click_OA_collaboration(self):
        """
        点击OA协同
        :return:
        """
        if self.isdispaly(self.OA_collaboration):
            self.click(self.OA_collaboration)
        return self

    def click_SystemSettings(self):
        """
        点击系统设置
        :return:
        """
        if self.isdispaly(self.SystemSettings):
            self.click(self.SystemSettings)
        return self

    def switch_to_waittingCustomers_iframe(self):
        """
        切换到客户管理-待跟客户iframe
        :return:
        """
        myiframe_object = self.find_element(self.waittingCustomers_iframe)
        self.driver.switch_to.frame(myiframe_object)






