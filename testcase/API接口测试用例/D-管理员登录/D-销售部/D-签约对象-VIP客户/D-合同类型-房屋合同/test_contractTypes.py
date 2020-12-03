#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 16:30
# @File : test_contractTypes.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统已有合同类型
import allure
import pytest

from utils.tools import get_dataTime

@allure.epic("API模块")
@allure.feature("合同分类-ContractTypesAPI")
class TestContractTypesAPI:

    @pytest.fixture()
    def after_tc002002(self, init_contractTypes):
        self.contractTypes_api = init_contractTypes[0]
        yield
        self.contractTypes_api.delete(self.new_contractType["_id"])

    @allure.story("合同分类-ContractTypesAPI-添加合同分类")
    @allure.title("添加合同分类测试用例")
    def test_tc002002(self, after_tc002002):
        """
        当前系统已有合同类型，创建一个不同的合同类型
        :param after_tc002002:
        :return:
        """
        self.new_contractType = self.contractTypes_api.add(name="土地合同", code=get_dataTime())
        contractTypes = self.contractTypes_api.list_all()
        assert self.new_contractType in contractTypes

    @pytest.fixture()
    def before_tc002051(self, init_contractTypes):
        self.contractTypes_api = init_contractTypes[0]
        self.new_contractType = self.contractTypes_api.add(name="销售合同", code=get_dataTime())
        yield
        self.contractTypes_api.delete(self.new_contractType["_id"])

    @allure.story("合同分类-ContractTypesAPI-修改合同分类")
    @allure.title("修改合同分类测试用例")
    def test_tc002051(self, before_tc002051):
        self.contractTypes_api.edit(self.new_contractType["_id"], name="车辆合同")
        contractTypes = self.contractTypes_api.list_all()
        for contractType in contractTypes:
            if contractType["_id"] == self.new_contractType["_id"]:
                assert contractType["name"] == "车辆合同"
                break

    @allure.story("合同分类-ContractTypesAPI-删除合同分类")
    @allure.title("删除合同分类测试用例")
    def test_tc002092(self, init_contractTypes):
        """
        当前系统已有合同类型，通过一个不存在的合同类型id去删除合同分类
        :param init_contractTypes:
        :return:
        """
        self.contractTypes_api = init_contractTypes[0]
        contractTypes1 = self.contractTypes_api.list_all()
        self.contractTypes_api.delete("agdfgdsffg")
        contractTypes2 = self.contractTypes_api.list_all()
        assert contractTypes1 == contractTypes2





