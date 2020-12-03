#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 17:21
# @File : test_account.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统没有签约对象
import allure
import pytest


@allure.epic("API模块")
@allure.feature("签约对象-AccountsAPI")
class TestAccountsAPI:

    @pytest.fixture()
    def before_tc001001(self, empty_accounts):
        self.accounts_api = empty_accounts
        yield
        self.accounts_api.delete(self.new_account["_id"])

    @allure.story("签约对象-AccountsAPI-添加签约对象")
    @allure.title("添加签约对象测试用例")
    def test_tc001001(self, before_tc001001, init_organiz):
        """
        当前系统没有签约对象，创建一个签约对象
        :param before_tc001001: 提供签约对象实例信息
        :param init_organiz: 提供部门信息
        :return:
        """
        self.new_account = self.accounts_api.add(name="VIP客户", company_ids=[init_organiz[1]["_id"]])
        accounts = self.accounts_api.list_all()
        assert self.new_account in accounts

    @allure.story("签约对象-AccountsAPI-修改签约对象")
    @allure.title("修改签约对象测试用例")
    def test_tc001052(self, empty_accounts):
        """
        当前系统没有签约对象，通过不存在的签约对象id修改签约对象名称
        :param empty_accounts: 初始化环境，清除当前账号下的签约对象
        :return:
        """
        self.accounts_api = empty_accounts
        res = self.accounts_api.edit("fasdfasdf", name="普通客户")
        assert res["error"]["code"] == 500

    @pytest.fixture()
    def before_tc001091(self, empty_accounts, init_organiz):
        self.accounts_api = empty_accounts
        self.new_account = self.accounts_api.add(name="VIP客户", company_ids=[init_organiz[1]["_id"]])
        yield

    @allure.story("签约对象-AccountsAPI-删除签约对象")
    @allure.title("删除签约对象测试用例")
    def test_tc001091(self, before_tc001091):
        """
        当前系统没有签约对象，通过一个已存在的签约对象id删除签约对象
        :param before_tc001091: 环境初始化，提供一个已存在的签约对象信息
        :return:
        """
        self.accounts_api.delete(self.new_account["_id"])
        accounts = self.accounts_api.list_all()
        assert accounts == []



















