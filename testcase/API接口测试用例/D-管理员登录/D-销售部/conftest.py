#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 16:34
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None

import pytest

from pylib.APIlib.accountsAPI import AccountsAPI
from pylib.APIlib.organizAPI import OrganizAPI

@pytest.fixture(scope="session")
def init_organiz(admin_login):
    """
    初始化-创建销售部
    结束后-清除测试数据，删除销售部
    :param admin_login: 提供cookies
    :return:
    """
    org_api = OrganizAPI(admin_login)
    # 删除所有部门
    org_api.delete_all()
    # 创建一个销售部
    sale_org = org_api.add(name="销售部")
    yield org_api, sale_org
    # 删除这个新建的销售部
    org_api.delete(sale_org["_id"])


@pytest.fixture(scope="session")
def empty_accounts(admin_login):
    """
    删除当前账号所有的签约对象，返回签约对象实例
    :param admin_login:
    :return:
    """
    accounts_api = AccountsAPI(admin_login)
    accounts_api.delete_all()
    yield accounts_api

