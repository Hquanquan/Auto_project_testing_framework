#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 15:54
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import allure
import pytest

from configs.api_env import userName, password
from pylib.APIlib.organizAPI import OrganizAPI
from pylib.APIlib.user import User

@pytest.fixture(scope="session")
def admin_login():
    """
    登录，获取用户的cookies
    :return:
    """
    cookies = User(userName, password).login()
    return cookies


@pytest.fixture(scope="session")
def empty_organiz(admin_login):
    """
    清空当前账号的所有部门
    :param admin_login: 提供cookies
    :return:
    """
    org_api = OrganizAPI(admin_login)
    org_api.delete_all()
    yield org_api


