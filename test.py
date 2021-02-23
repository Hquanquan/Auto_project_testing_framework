#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 10:41
# @File : test.py.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import pprint

from configs.api_env import userName, password
from pylib.APIlib.baseAPI import BaseAPI
from pylib.APIlib.organizAPI import OrganizAPI
from pylib.APIlib.user import User
from utils.convertData import ConvertData

if __name__ == '__main__':
    mycookies = User(userName, password).login()
    org = OrganizAPI(mycookies)
    new_org = org.add(name="背锅部")
    orgs = org.list_all()
    for i in orgs:
        pprint.pprint(i)
        print("=" * 100)
    text = org.edit(new_org["_id"], name="产品背锅部")
    print(text)
    print("******** 操作后的列表 ***********")
    orgs = org.list_all()[1:]
    for i in orgs:
        pprint.pprint(i)
        print("=" * 100)
    org.delete_all()
