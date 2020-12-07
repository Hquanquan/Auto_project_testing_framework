#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 11:56
# @File : waitingCustomers.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 待跟客户列表页
import time

from configs.web_env import HOST
from pylib.UIlib.pageObjects.basePage1 import BasePage
from utils.tools import create_Str, get_phone_num


class WaittingCustomers(BasePage):
    """
    待跟客户列表页
    """

    def to_page(self):
        """访问此页面的网址"""
        self.url = HOST + self.path
        self.driver.get(self.url)

    def createCustomers(self):
        """
        创建客户
            1、点击创建客户按钮
            2、切换到弹窗
            3、填写创建客户的信息
            4、点击保存
            5、页面自动关闭弹窗
        :return:
        """
        # 点击创建客户按钮
        self.click(self.create_Cus_Btn)
        # 找到iframe对象
        iframe_obj = self.find_element(self.WaittingCustomers_iframe)
        # 切换到iframe
        self.driver.switch_to.frame(iframe_obj)
        # 输入公司名称
        self.send_keys(self.companyName_input, create_Str("公司名称"))
        # 输入随机生成的手机号码
        self.send_keys(self.phoneNumber_input, get_phone_num())


        return self



