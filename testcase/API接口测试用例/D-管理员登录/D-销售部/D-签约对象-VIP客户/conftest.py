#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 9:04
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 当前系统已有签约对象
import pytest

from pylib.APIlib.accountsAPI import AccountsAPI
from pylib.APIlib.contractTypesAPI import ContractTypesAPI


@pytest.fixture(scope="session")
def init_accounts(admin_login, init_organiz):
    """
    创建签约对象
    创建签约对象需要的参数：
        "name": name, 签约对象名称
        "category": 1, 签约对象类别，企业：1，个人：2，其他：3
        "company_ids": ["QmBLZC5zKaEMu96QN"],关联部门ID
        "status": 1, 启用状态，未启用：1，已启用：2 ，停用：3
        "space": self.api.space, spaceid可以从cookies的X-Space-Id字段获取
    测试完成后需要删除测试产生的数据，所以调用删除delete()
    :param admin_login: 提供cookies
    :param init_organiz: 提供销售部对象信息
    :return:
    """
    # 1、创建一个销售部，并返回该销售部实例对象
    sale_org = init_organiz[1]
    # 2、实例化一个签约对象
    accounts_api = AccountsAPI(admin_login)
    # 3、删除所有的签约对象
    accounts_api.delete_all()
    # 4、新建一个新的签约对象-VIP客户
    vip_account = accounts_api.add(name="VIP客户", company_ids=[sale_org["_id"]])
    yield accounts_api, vip_account
    accounts_api.delete(vip_account["_id"])

@pytest.fixture(scope="package")
def empty_contractType(admin_login):
    """
    清除当前账号的合同分类
    :param admin_login:
    :return:
    """
    contractType_api = ContractTypesAPI(admin_login)
    contractType_api.delete_all()
    yield contractType_api




