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
    def uploadFile(self):
        """
        上传附件 ，
        默认上传 E:\image.jpg
        :return:
        """
        self.uploadFile_to_input(self.PC_uploadFile_input)

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

        # 回款期数选择3期
        self.click(self.PC_repaymentPeriod_input)
        self.click(self.PC_repaymentPeriod_number)

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

    @allure.step("step: 编辑回款计划")
    def edit_paymentPlan(self):
        """编辑回款计划"""
        # 回款比例 60
        self.send_keys(self.PC_rp_repaymentProportion_0, 60)
        # 回款金额 60000
        self.send_keys(self.PC_rp_repaymentMoney_0, 60000)
        # 回款备注
        self.send_keys(self.PC_rp_remark_0, "回款备注：xxx")

        # 回款比例 20
        self.send_keys(self.PC_rp_repaymentProportion_1, 20)
        # 回款金额 20000
        self.send_keys(self.PC_rp_repaymentMoney_1, 20000)
        # 回款备注
        self.send_keys(self.PC_rp_remark_1, "回款备注：xxx")

        # 回款比例 20
        self.send_keys(self.PC_rp_repaymentProportion_2, 20)
        # 回款金额 20000
        self.send_keys(self.PC_rp_repaymentMoney_2, 20000)
        # 回款备注
        self.send_keys(self.PC_rp_remark_2, "回款备注：xxx")


    # 资质配置
    @allure.step("step: 资质配置")
    def edit_qualificationConfiguration(self):
        """
        资质配置，只填写我司提供人数和客户提供人数，其他暂时不填
        :return:
        """
        # 循环遍历填写提供人数
        quaX_needNum_inputs_eles = self.find_elements(self.PC_quaX_needNum_inputs)
        quaX_provideNum_inputs_eles = self.find_elements(self.PC_quaX_provideNum_inputs)
        # 遍历输入我司提供人数：2
        self.forEach_send_keys(quaX_needNum_inputs_eles, "2")
        # 遍历输入客户提供人数：2
        self.forEach_send_keys(quaX_provideNum_inputs_eles, "2")

    # 安证配置
    @allure.step("step: 安证配置")
    def edit_cerConfiguration(self):
        """
        安证配置,新增一行建造师
        :return:
        """
        # 点击添加一行
        self.click(self.PC_cerAddBtn)

        #  第二行第一列的人才类型选择器
        self.click(self.PC_cer_personnelType_select)
        #  下拉选择框：建造师
        self.click(self.PC_cer_personnelType_builder)
        #  第二行社保提供方
        self.click(self.PC_cer_buySafeProvider_select)
        #  下拉选择框：客户
        self.click(self.PC_cer_buySafeProvider)

        # 我方提供数
        self.send_keys(self.PC_cer_oneProvideNum_1, "2")
        # 客户提供数
        self.send_keys(self.PC_cer_needNum_1, "2")

    @allure.step("step: 点击【保存信息】")
    def click_saveBtn(self):
        """
        点击完善合同页的保存信息按钮
        :return:
        """
        self.click(self.PC_save_btn)
