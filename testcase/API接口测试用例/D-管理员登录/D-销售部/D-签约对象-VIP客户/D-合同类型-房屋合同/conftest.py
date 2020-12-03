#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 15:42
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest

from pylib.APIlib.contractTypesAPI import ContractTypesAPI
from pylib.APIlib.contractsAPI import ContractsAPI
from utils.tools import get_dataTime

@pytest.fixture(scope="session")
def init_contractTypes(admin_login):
    """
    初始化创建合同类型-房屋合同
    :param admin_login:
    :return:
    """
    contractTypes_api = ContractTypesAPI(admin_login)
    contractTypes_api.delete_all()
    new_contractType = contractTypes_api.add(name="房屋合同", code=get_dataTime())
    yield contractTypes_api, new_contractType
    contractTypes_api.delete(new_contractType["_id"])

@pytest.fixture(scope="session")
def empty_contract(admin_login):
    """
    清除当前系统的中的合同
    :param admin_login:
    :return:
    """
    contract_api = ContractsAPI(admin_login)
    contract_api.delete_all()
    yield contract_api

