#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 11:56
# @File : waitingCustomers.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 待跟客户列表页
import time

import allure

from configs.web_env import HOST
from pylib.UIlib.pageObjects.basePage1 import BasePage
from utils.tools import create_Str, get_phone_num, write_yaml


class WaittingCustomersPage(BasePage):
    """
    待跟客户列表页
    """
    # 创建客户
    @allure.step("step:【创建客户】")
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
        # 随机生成客户信息，便于保存到配置文件,后续验证创建客户成功时需要用到客户信息
        customersInfo = {
            "name": create_Str("公司名称"),
            "phone": get_phone_num(),
            "wx": create_Str("wx"),
            "QQ": get_phone_num(),
            "contactPerson": create_Str("联系人"),
            "email": get_phone_num() + "@test.com",
            "departmentPosition": "董事长助理",
            "qualification": "工程造价",
            "otherRemarks": create_Str("测试创建客户"),
        }
        # 把客户信息保存到配置文件configs/createCustomers.yaml
        write_yaml(args={"customersInfo": customersInfo})
        # 输入公司名称
        self.send_keys(self.companyName_input, customersInfo["name"])
        # 输入随机生成的手机号码
        self.send_keys(self.phoneNumber_input, customersInfo["phone"])
        # 输入随机生成的wx号
        self.send_keys(self.wx_number_input, customersInfo["wx"])
        # 输入随机生成的11位的QQ号
        self.send_keys(self.QQ_input, customersInfo["QQ"])
        # 输入随机生成的联系人
        self.send_keys(self.contactPerson_input, customersInfo["contactPerson"])
        # 输入随机生成的email
        self.send_keys(self.email_input, customersInfo["email"])
        # 输入部门职位
        self.send_keys(self.departmentPosition_input, customersInfo["departmentPosition"])
        # 输入咨询资质
        self.send_keys(self.qualification_input, customersInfo["qualification"])
        # 客户来源，来源渠道暂时不填
        # 选择所在地区：广东省-广州市
        self.click(self.location_input)
        time.sleep(0.5)
        self.click(self.province)
        time.sleep(0.5)
        self.click(self.guangzhouCity)
        # 详细地址暂时不填
        # 选择资质类型-施工
        self.click(self.qualificationTypeSelect)
        self.click(self.construction)
        # 填写其他备注
        self.send_keys(self.otherRemarks_textarea, customersInfo["otherRemarks"])
        # 点击信息保存
        self.click(self.saveInformationBtn)
        return self

    # 查找客户
    @allure.step("step:【查找客户】")
    def find_customers(self, keyword, input1=True):
        """
        根据客户名称，联系人，联系电话,QQ、微信、邮箱 查找客户
        :param input1: input1=True 默认使用客户名称，联系人，联系电话输入框查找客户
        :param keyword:
        :return:
        """
        # 输入框输入搜索关键字
        if input1:
            self.send_keys(self.keyword_input1, keyword)
        else:
            self.send_keys(self.keyword_input2, keyword)
        time.sleep(2)
        # 点击查询按钮
        self.click(self.search_btn)
        return self

    # 获取查找客户后的列表客户信息
    @allure.step("step:【获取查找客户后的列表客户信息】")
    def get_tables_costomersInfo(self):
        """
        获取待跟客户列表里单行数据里的公司名称，联系人，联系电话
        :return:
        """
        name = self.find_element(self.WaittingCustomers_table_name_locator).text
        phoneNum = self.find_element(self.WaittingCustomers_table_phone_locator).text
        contactPerson = self.find_element(self.WaittingCustomers_table_person_locator).text
        costomersInfo = {
            "name": name,
            "phone": phoneNum,
            "contactPerson": contactPerson,
        }
        return costomersInfo

    # 点击客户列表里的【详情】按钮
    @allure.step("step: 【进入客户详情页】")
    def click_detail_btn(self):
        """点击客户列表里的【详情】按钮,进入客户详情页"""
        # 找到一组详情按钮，其中下标为1的是准确的
        eles = self.find_elements(self.WaittingCustomers_table_detail_btn)
        eles[1].click()

    # 切换到客户详情iframe
    @allure.step("step: 【内部操作：切换到客户详情iframe】")
    def switch_to_customers_datail_iframe(self):
        """切换到客户详情iframe"""
        myiframe_object = self.find_element(self.customers_detail_iframe)
        self.driver.switch_to.frame(myiframe_object)






