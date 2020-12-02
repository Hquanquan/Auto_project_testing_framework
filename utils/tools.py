#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 11:23
# @File : tools.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 通用工具
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

if __name__ == '__main__':
    data = read_yaml(r"../configs/api_conf.yaml")
    print(data)

