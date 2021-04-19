#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 16:02
# @File : test_organiz.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统没有部门
import allure
import pytest


@allure.epic("API模块")
@allure.feature("部门-OrganizaAPI")
class TestOrganizAPI:

    @pytest.fixture()
    def after_tc000001(self, empty_organiz):
        self.org_api = empty_organiz
        yield
        self.org_api.delete(self.new_organiz["_id"])

    @allure.story("部门-OrganizaAPI-添加部门")
    @allure.title("添加部门测试用例")
    def test_tc000001(self, after_tc000001):
        """
        当前系统没有部门，创建一个新的部门
        :param after_tc000001: 测试结束后清除测试数据
        :return:
        """
        # 创建一个部门
        self.new_organiz = self.org_api.add(name="测试部")
        # 列出当前系统所有的部门
        orgs = self.org_api.list_all()
        # 断言新创建的部门存在于所有部门中
        assert self.new_organiz in orgs

    @pytest.fixture()
    def before_tc000091(self, empty_organiz):
        """
        删除部门测试用例前的操作！！！！！！！
        :param empty_organiz:
        :return:
        """
        self.org_api = empty_organiz
        self.new_organiz = self.org_api.add(name="测试部")

    @allure.story("部门-OrganizaAPI-删除部门")
    @allure.title("删除部门测试用例")
    def test_tc000091(self, before_tc000091):
        """
        当前系统没有部门，通过已存在的部门id删除部门
        :param before_tc000091: 初始化-创建一个部门，提供一个已存在的部门id
        :return:
        """
        # 通过已存在的部门id删除部门
        self.org_api.delete(self.new_organiz["_id"])
        # 过滤掉总公司，获取返回的部门列表
        res = self.org_api.list_all()[1:]
        # 断言返回部门列表为空
        assert res == []
