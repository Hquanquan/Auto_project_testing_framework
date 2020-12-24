#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 10:29
# @File : main_test.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import os

import pytest

from pylib.UIlib.pageObjects.loginPage import LoginPage
from pylib.UIlib.pageObjects.demoPage import Demopage
from utils.tools import read_yaml


def run():
    for one in os.listdir('report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'report/tmp/{one}')

    pytest.main(['testcase/UI测试用例', '-s', '--alluredir=report/tmp'])
    os.system('allure serve report/tmp')

if __name__ == '__main__':

    pytest.main(["-s", "-k test_paymentCollectionApproval.py "])
    # run()







