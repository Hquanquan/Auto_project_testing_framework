#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 14:47
# @File : basePage1.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 使用OP模式，读取yaml文件的方式获取页面元素

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pylib.UIlib.common.webDriver import Driver
from utils.tools import read_yaml


class BasePage:

    def __init__(self, conf_path = "../../../configs/web_ele_conf.yaml"):
        """
        conf_path="configs/web_ele_conf.yaml"
        初始化，获取driver,读取配置文件的数据
        :param conf_path:
        """
        self.driver = Driver().get_driver()
        self.__init_eles(conf_path)

    def __init_eles(self, conf_path):
        """
        动态读取配置文件的页面元素，把继承树上的页面元素都赋值到当前页面类中作为属性
        :param conf_path:
        :return:
        """
        # 使用当前页面继承的所有页面类作为元素配置项，去掉basepage和object
        class_names = [m.__name__ for m in self.__class__.mro()][:-2]

        for class_name in class_names:
            eles = read_yaml(conf_path)[class_name]
            # eles的key作为属性名称，value作为属性值
            for key in eles:
                # self.__setattr__(属性名称key, 属性值eles[key]),动态生成对象属性
                self.__setattr__(key, eles[key])


    def input_text(self, locator, text):
        self.click(locator)  # 点一下再输入
        self.driver.find_element(*locator).send_keys(text)

    def click(self, locator):
        ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator[0], locator[1])))
        ele.click()










