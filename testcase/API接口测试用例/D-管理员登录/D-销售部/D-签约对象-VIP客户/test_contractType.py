#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 10:43
# @File : test_contractType.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统没有合同分类
import allure
import pytest

from utils.tools import get_dataTime

@allure.epic("API模块")
@allure.feature("合同分类-ContractTypesAPI")
class TestContractTypesAPI:

    @pytest.fixture()
    def after_tc002001(self, empty_contractType):
        self.contractTypes_api = empty_contractType
        yield
        self.contractTypes_api.delete(self.new_contractType["_id"])

    @allure.story("合同分类-ContractTypesAPI-添加合同分类")
    @allure.title("添加合同分类测试用例")
    def test_tc002001(self, after_tc002001):
        """
        当前系统没有合同分类，创建一个合同分类
        :param after_tc002001: 初始化环境，提供一个合同分类实例对象
        :return:
        """
        self.new_contractType = self.contractTypes_api.add(name="房产合同类型", code=get_dataTime())
        contractTypes = self.contractTypes_api.list_all()
        assert self.new_contractType in contractTypes

    @allure.story("合同分类-ContractTypesAPI-修改合同分类")
    @allure.title("修改合同分类测试用例")
    def test_tc002052(self, empty_contractType):
        """
        当前系统没有合同分类，通过不存在的合同分类id去修改合同分类
        :param empty_contractType:
        :return:
        """
        self.contractTypes_api = empty_contractType
        res = self.contractTypes_api.edit("fasdfasdf", name="销售合同")
        assert res["error"]["code"] == 500

    @pytest.fixture()
    def before_tc002091(self, empty_contractType):
        self.contractTypes_api = empty_contractType
        self.new_contractType = self.contractTypes_api.add(name="房产合同类型", code=get_dataTime())

    @allure.story("合同分类-ContractTypesAPI-删除合同分类")
    @allure.title("删除合同分类测试用例")
    def test_tc002091(self, before_tc002091):
        """
        当前系统没有合同分类，通过已存在的合同类型id删除合同分类，预期结果合同类型列表为空
        :param before_tc002091: 提供已存在的合同类型信息
        :return:
        """
        self.contractTypes_api.delete(self.new_contractType["_id"])
        contractTypes = self.contractTypes_api.list_all()
        assert contractTypes == []



