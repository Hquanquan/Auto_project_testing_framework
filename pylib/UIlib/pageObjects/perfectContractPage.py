#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 9:23
# @File : perfectContractPage.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 完善合同页
import allure

from configs.web_env import uploadFilePath
from pylib.UIlib.pageObjects.basePage1 import BasePage
from utils.tools import get_dataTime


class PerfectContractPage(BasePage):
    """
    完善合同页
    """

    @allure.step("step: 选择办理地区：广东省/广州市")
    def select_area(self):
        """
        选择办理地区
        :return:
        """
        # 点击办理地区
        self.click(self.PC_handlingArea_input)
        # 搜索广东省
        self.send_keys(self.PC_kw1_input, "广东省")
        # 鼠标悬停到广东省
        self.move_to_element(self.PC_province)
        # 点击广州市
        self.click(self.PC_guangzhouCity)

    @allure.step("step:输入办理时效")
    def send_keys_handleDays(self, text):
        """输入办理时效"""
        self.send_keys(self.PC_handleDays_input, text)

    @allure.step("step:输入客户签约人")
    def send_keys_clientSigner(self, text="客户代表"):
        """输入客户签约人"""
        self.send_keys(self.PC_clientSigner_input, text)

    @allure.step("step:输入我方签约人：王裕")
    def send_keys_OurSigner(self, text="王裕"):
        """输入我方签约人"""
        # 1、点一下输入框
        self.click(self.PC_OurSigner_input)
        # 2、输入框输入王裕
        self.send_keys(self.PC_OurSigner_input, text)
        # 3、点击王裕，选择王裕
        self.click(self.PC_OurSigner)

    @allure.step("step:输入签约时间")
    def send_keys_signTime(self, timeStr=get_dataTime("%Y-%m-%d %H:%M:%S")):
        """
        输入签约时间
        :param timeStr: 默认选择当前时间
        :return:
        """
        # 选择签约时间 选择当前时间
        self.send_keys(self.PC_signTimeStrInp, timeStr)

    @allure.step("step:输入备注")
    def send_keys_remarks(self, text="测试完善合同：" + get_dataTime("%Y-%m-%d %H:%M:%S")):
        """
        输入备注
        :param text:
        :return:
        """
        self.send_keys(self.PC_remarks_textarea, text)

    @allure.step("step:上传附件")
    def uploadFile(self, path=uploadFilePath):
        """ 上传附件 """
        # 上传附件
        ele = self.find_element(self.PC_uploadFile_input)
        ele.send_keys(path)


    @allure.step("step: 编辑完善合同页的基本信息")
    def edit_basicInformation(self):
        """
        编辑完善合同页的基本信息
        :return:
        """
        # 选择办理地区
        self.select_area()
        # 输入办理时效
        self.send_keys_handleDays("120")
        # 输入客户签约人
        self.send_keys_clientSigner()
        # 选择我方签约人:王裕
        self.send_keys_OurSigner()
        # 选择签约时间 选择当前时间
        self.send_keys_signTime()
        # 填写备注
        self.send_keys_remarks()
        # 上传附件
        self.uploadFile()

    @allure.step("step: 编辑完善合同页的费用明细")
    def edit_costDetail(self):
        """
        编辑完善合同页的费用明细
        :return:
        """
        # 输入项目性质：
        self.send_keys(self.PC_projectNature_input, "新办")
        # 输入人才费（建造师）
        self.send_keys(self.PC_talConstructorMoney_input, 10000)
        # 输入人才费（工程师）
        self.send_keys(self.PC_talEngineerMoney_input, 10000)
        # 人才费（技工）
        self.send_keys(self.PC_talArtisanMoney_input, 10000)
        # 人才费合计
        self.send_keys(self.PC_talMoney_input, 10000)
        #  社保费用
        self.send_keys(self.PC_socialSecurityMoney_input, 10000)
        #  业务费
        self.send_keys(self.PC_teaMoney_input, 10000)
        #  工商注册费
        self.send_keys(self.PC_industryRegisterMoney_input, 10000)
        #  安证ABC+插班/包过
        self.send_keys(self.PC_cerPackage_input, 10000)
        #  税费
        self.send_keys(self.PC_tax_input, 10000)
        #  其他费用（需备注事项）
        self.send_keys(self.PC_rest_input, 10000)
        # 服务费
        self.send_keys(self.PC_serMoney_input, 10000)
        # 合同金额 注意：要与回款计划-回款金额对应
        self.send_keys(self.PC_money_input, 100000)
        # 是否有赔款条约 选择：否
        self.click(self.PC_isReparations_input)
        self.click(self.PC_false_option)

        pass

    @allure.step("step: 编辑回款计划")
    def edit_paymentPlan(self):
        """编辑回款计划"""
        # 回款比例 100
        self.send_keys(self.PC_rp_repaymentProportion_0, 100)
        # 回款金额 100000
        self.send_keys(self.PC_rp_repaymentMoney_0, 100000)
        # 回款备注
        self.send_keys(self.PC_rp_remark_0, "回款备注：xxx")



