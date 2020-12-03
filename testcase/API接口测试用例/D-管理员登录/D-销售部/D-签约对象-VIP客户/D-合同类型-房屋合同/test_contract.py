#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:16
# @File : test_contract.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统没有合同
import allure
import pytest

from utils.convertData import ConvertData
from utils.tools import dynamic_report

@allure.epic("API模块")
@allure.feature("合同-ContractsAPI")
class TestContractsAPI:

    @pytest.fixture()
    def after_tc003001(self, empty_contract):
        self.contract_api = empty_contract
        yield
        self.contract_api.delete(self.new_contract["_id"])

    @dynamic_report('name', 'name')
    @allure.story("合同-ContractsAPI-添加合同")
    @allure.title("添加合同测试用例")
    @pytest.mark.parametrize("name,amount", ConvertData.get_param())
    def test_tc003001(self, name, amount, after_tc003001, init_organiz, init_accounts, init_contractTypes):
        """
        当前系统没有合同，添加合同。预期结果是添加的合同存在于所有的合同列表中
        添加合同需要的参数：
            name string 合同名称
            othercompany string 签约对象ID
            contract_type string 合同类型ID
            company_id sting  分部ID
            create_date string 创建日期： 2020-07-07T07:31:06.754Z
            amount int 合同金额
        :param after_tc003001:
        :param name: 参数化传入的name
        :param amount: 参数化传入的amount
        :param after_tc003001: 环境初始化
        :param init_organiz: 提供部门对象信息
        :param init_accounts: 提供签约对象信息
        :param init_contractTypes: 提供合同分类对象信息
        :return:
        """
        self.new_contract = self.contract_api.add(name=name,
                                                  amount=amount,
                                                  othercompany=init_accounts[1]["_id"],
                                                  contract_type=init_contractTypes[1]["_id"],
                                                  company_id=init_organiz[1]["_id"])
        # 列出所有合同
        contracts = self.contract_api.list_all()
        # 断言 新添加的合同在所有合同里
        assert self.new_contract in contracts

    @allure.story("合同-ContractsAPI-修改合同")
    @allure.title("修改合同测试用例")
    def test_tc003052(self, empty_contract):
        """
        当前系统没有合同，通过不存在的合同id去修改合同
        :param empty_contract:
        :return:
        """
        self.contract_api = empty_contract
        res = self.contract_api.edit("asfdasdf", name="租房合同")
        assert res["error"]["code"] == 500

    @pytest.fixture()
    def before_tc003091(self, empty_contract, init_accounts, init_contractTypes, init_organiz):
        self.contract_api = empty_contract
        self.new_contract = self.contract_api.add(name="租房合同",
                                                  amount=50000,
                                                  othercompany=init_accounts[1]["_id"],
                                                  contract_type=init_contractTypes[1]["_id"],
                                                  company_id=init_organiz[1]["_id"])

    @allure.story("合同-ContractsAPI-删除合同")
    @allure.title("删除合同测试用例")
    def test_tc003091(self, before_tc003091):
        """
        当前系统没有合同，通过已存在的合同id去删除合同
        :param before_tc003091:
        :return:
        """
        self.contract_api.delete(self.new_contract["_id"])
        contracts = self.contract_api.list_all()
        assert contracts == []


