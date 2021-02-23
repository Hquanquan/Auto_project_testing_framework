#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:42
# @File : conftest.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pytest
from pylib.APIlib.contractsAPI import ContractsAPI


@pytest.fixture(scope="session")
def init_contracts(admin_login, init_accounts, init_contractTypes, init_organiz):
    """
    初始化创建一个购房合同
    :param admin_login: 提供cookies信息
    :param init_accounts: 提供签约对象信息
    :param init_contractTypes: 提供合同分类信息
    :param init_organiz: 提供部门信息
    :return:
    """
    contracts_api = ContractsAPI(admin_login)
    new_contract = contracts_api.add(name="购房合同",
                                     amount=50000,
                                     othercompany=init_accounts[1]["_id"],
                                     contract_type=init_contractTypes[1]["_id"],
                                     company_id=init_organiz[1]["_id"])
    yield contracts_api, new_contract
    contracts_api.delete(new_contract["_id"])
