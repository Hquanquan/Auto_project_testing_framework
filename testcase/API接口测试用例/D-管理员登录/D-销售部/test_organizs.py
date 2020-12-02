#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 16:40
# @File : test_organizs.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统已有部门
import allure
import pytest

@allure.epic("API模块")
@allure.feature("部门-OrganizaAPI")
class TestOrganizAPI:

    @pytest.fixture()
    def after_tc000002(self, init_organiz):
        self.org_api = init_organiz[0]
        yield
        self.org_api.delete(self.new_organiz["_id"])

    @allure.story("部门-OrganizaAPI-添加部门")
    @allure.title("添加部门测试用例")
    def test_tc000002(self, after_tc000002):
        """
        当前系统已有部门，创建一个新的部门
        :param after_tc000002:
        :return:
        """
        self.new_organiz = self.org_api.add(name="测试部")
        orgs = self.org_api.list_all()
        assert self.new_organiz in orgs

    @pytest.fixture()
    def before_tc000051(self, init_organiz):
        self.org_api = init_organiz[0]
        self.new_organiz = self.org_api.add(name="测试部")
        yield
        self.org_api.delete(self.new_organiz["_id"])

    @allure.story("部门-OrganizaAPI-修改部门")
    @allure.title("修改部门测试用例")
    def test_tc000051(self, before_tc000051):
        """
        当前系统已有部门，修改其中一个部门的名称
        :param before_tc000051:
        :return:
        """
        self.org_api.edit(self.new_organiz["_id"], name="产品背锅部")
        orgs = self.org_api.list_all()
        for org in orgs:
            if org["_id"] == self.new_organiz["_id"]:
                assert org["name"] == "产品背锅部"
                break

    @allure.story("部门-OrganizaAPI-修改部门")
    @allure.title("修改部门测试用例")
    def test_tc000052(self, init_organiz):
        """
        当前已有部门，通过一个不存在的部门id来修改部门名称
        :param init_organiz:
        :return:
        """
        self.org_api = init_organiz[0]
        res = self.org_api.edit(_id="asdfasdfdds", name="产品背锅部")
        assert res["error"]["code"] == 500

    @allure.story("部门-OrganizaAPI-删除部门")
    @allure.title("删除部门测试用例")
    def test_tc000092(self, init_organiz):
        self.org_api = init_organiz[0]
        orgs1 = self.org_api.list_all()
        self.org_api.delete("sdfasdfasdf")
        orgs2 = self.org_api.list_all()
        assert orgs1 == orgs2
