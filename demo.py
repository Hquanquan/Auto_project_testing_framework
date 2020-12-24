#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 17:35
# @File : demo.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import yaml
import random
from utils.tools import get_dataTime, read_yaml

ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"




def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


def get_phone_num():
    """
    要获取一个手机号，我们首先需要了解手机号码的组成规律，我们简单的认为存在以下规律：
    ①手机号码一共有11位
    ②第1位目前都是1
    ③第2位in[3、4、5、7、8] 取值
    ④第3位比较复杂一些，根据第2位的数字，对应运营商的生成规律
    ⑤后8位是随机生成的8个数字
    :return:
    """
    second_spot = random.choice([3, 4, 5, 7, 8])
    third_spot = {
        3: random.randint(0, 9),
        4: random.choice([5, 7, 9]),
        5: random.choice([i for i in range(10) if i != 4]),
        7: random.choice([i for i in range(10) if i not in [4, 9]]),
        8: random.randint(0, 9), }[second_spot]

    remain_spot = random.randint(9999999, 100000000)
    phone_num = "1{}{}{}".format(second_spot, third_spot, remain_spot)
    return phone_num


def create_Str(text):
    """
    生成以text开头，以当前时间结尾的字符串
    :param text:
    :return:
    """
    return text + get_dataTime(time_formate="%Y%m%d%H%M%S")


def write_yaml(args, path="configs/createCustomers.yaml"):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(args, f, allow_unicode=True)


if __name__ == '__main__':
    # 生成手机号
    costomers = {
        "name": create_Str("客户名称"),
        "phone": get_phone_num(),
    }
    args = {"costomers": costomers}
    write_yaml(args)

    a = read_yaml("configs/createCustomers.yaml")
    print(a)
