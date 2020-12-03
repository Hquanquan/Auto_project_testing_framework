#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 11:23
# @File : tools.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 通用工具
import datetime
from functools import wraps

import allure
import yaml


def read_yaml(filePath):
    """
    读取yaml文件数据，并字典格式返回
    :param filePath:
    :return:
    """
    # 打开filePath路径的文件
    with open(filePath, encoding="utf-8") as f:
        # 读取yaml文件内容，赋值到content
        content = f.read()
        # 把content转化为字典格式
        data_json = yaml.safe_load(content)
        return data_json

def get_dataTime(time_formate="%Y-%m-%d-%H%M%S"):
    """
    获取当前时间，转换为指定的字符串格式返回
    :param time_formate: 格式
    :return:
    """
    dt = datetime.datetime.now()
    current_time = dt.strftime(time_formate)
    return current_time

# 自定义的装饰器
def dynamic_report(target, target_tile=None):
    def decorate(fun):
        @wraps(fun)  # 保留测试方法原来的信息
        def warpper(*args, **kwargs):
            res = fun(*args, **kwargs)
            desc = kwargs[target]  # 从用例参数列表获取要表示的字段
            allure.dynamic.description('用例描述---%s' % desc)
            if target_tile:  # 如果指定了目标标题就从参数列表的数据自定义报告标题
                title = kwargs[target_tile]
                allure.dynamic.title(title)
            return res
        return warpper
    return decorate



if __name__ == '__main__':
    data = read_yaml(r"../configs/api_conf.yaml")
    print(get_dataTime())

