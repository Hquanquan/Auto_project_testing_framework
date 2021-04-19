#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 9:21
# @File : test_accounts.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统已有签约对象
import allure
import pytest

@allure.epic("API模块")
@allure.feature("签约对象-AccountsAPI")
class TestAccountsAPI:
    @pytest.fixture()
    def after_tc001002(self, init_accounts):
        self.accounts_api = init_accounts[0]
        yield
        self.accounts_api.delete(self.new_account["_id"])

    @allure.story("签约对象-AccountsAPI-添加签约对象")
    @allure.title("添加签约对象测试用例")
    def test_tc001002(self, after_tc001002, init_organiz):
        """
        当前已有签约对象，创建一个新的签约对象
        :param after_tc001002: 环境初始化，为系统创建一个默认存在的签约对象，清除测试后的数据
        :param init_organiz: 提供已存在的部门对象信息
        :return:
        """
        self.new_account = self.accounts_api.add(name="SVIP客户", company_ids=[init_organiz[1]["_id"]])
        accounts = self.accounts_api.list_all()
        assert self.new_account in accounts

    @pytest.fixture()
    def before_tc001051(self, init_accounts, init_organiz):
        self.accounts_api = init_accounts[0]
        self.new_account = self.accounts_api.add(name="普通客户", company_ids=[init_organiz[1]["_id"]])
        yield
        self.accounts_api.delete(self.new_account["_id"])

    @allure.story("签约对象-AccountsAPI-修改签约对象")
    @allure.title("修改签约对象测试用例")
    def test_tc001051(self, before_tc001051):
        """
        当前系统已有签约对象，修改一个已存在的签约对象的名称.预期结果显示修改后的名称
        :param before_tc001051: 初始化环境，创建一个新的签约对象用于修改
        :return:
        """
        self.accounts_api.edit(self.new_account["_id"], name="土豪客户")
        accounts = self.accounts_api.list_all()
        for account in accounts:
            if account["_id"] == self.new_account["_id"]:
                assert account["name"] == "土豪客户"
                break

    @allure.story("签约对象-AccountsAPI-删除签约对象")
    @allure.title("删除签约对象测试用例")
    def test_tc001092(self, init_accounts):
        """
        当前系统已存在签约对象，通过不存在的签约对象id去删除签约对象
        :param init_accounts:
        :return:
        """
        self.accounts_api = init_accounts[0]
        accounts1 = self.accounts_api.list_all()
        self.accounts_api.delete("afsdfasda")
        accounts2 = self.accounts_api.list_all()
        assert accounts1 == accounts2
