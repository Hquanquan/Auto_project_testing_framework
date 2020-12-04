#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 14:47
# @File : basepage2.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 使用OP模式，硬编码手动为每个页面动态赋值元素属性

import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from logs.logger import Logger
from pylib.UIlib.common.webDriver import Driver
from utils.tools import get_dataTime

logger = Logger(logger="BasePage").getlog()
class BasePage:
    """
    BasePage 类，所有页面的基础类，所有的页面类都要继承该类
    """

    # 初始化 driver 对象
    def __init__(self):
        """
        初始化 driver 对象
        """
        # 获取浏览器驱动对象
        self.driver = Driver.get_driver()

    # 根据特定的表达式获取元素
    def find_element(self, selectors):
        """
        获得单个元素
        :param selectors: 定位元素的列表 ["id","username"]
        :return:
        """
        element = ''

        selector_by = selectors[0]  # 元素名称
        selector_value = selectors[1]  # 元素ID名称
        # 根据id定位
        if selector_by == "i" or selector_by == "id":
            try:
                element = self.driver.find_element_by_id(selector_value)  # id 定位
                logger.info("%s Had find the element \' %s \' successfully "
                            "by %s via value:%s" % (get_dataTime(), element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("%s NoSuchElementException:%s" % (get_dataTime(), e))
                self.get_windows_img()
        # 根据name定位
        elif selector_by == "n" or selector_by == "name":
            try:
                element = self.driver.find_element_by_name(selector_value)  # name 名称定位
                logger.info("%s Had find the element \' %s \' successfully "
                            "by %s via value:%s" % (get_dataTime(), element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("%s NoSuchElementException:%s" % (get_dataTime(), e))
                self.get_windows_img()
        # 根据className定位
        elif selector_by == "class_name" or selector_by == "class name":
            try:
                element = self.driver.find_element_by_class_name(selector_value)  # css 样式名称定位
                logger.info("%s Had find the element \' %s \' successfully "
                            "by %s via value:%s" % (get_dataTime(), element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("%s NoSuchElementException:%s" % (get_dataTime(), e))
                self.get_windows_img()
        # 根据link_text标签文本定位
        elif selector_by == "link_text" or selector_by == "link text":
            try:
                element = self.driver.find_element_by_link_text(selector_value)  # 文本超链接定位
                logger.info("%s Had find the element \' %s \' successfully "
                            "by %s via value:%s" % (get_dataTime(), element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("%s NoSuchElementException:%s" % (get_dataTime(), e))
                self.get_windows_img()
        # 根据partial_link_text模糊标签文本定位
        elif selector_by == "p" or selector_by == "partial link text":
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                logger.info("%s Had find the element \' %s \' successfully "
                            "by %s via value:%s" % (get_dataTime(), element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("%s NoSuchElementException:%s" % (get_dataTime(), e))
                self.get_windows_img()
        # 根据tag_name标签名定位
        elif selector_by == "tag_name" or selector_by == "tag name":
            try:
                element = self.driver.find_element_by_tag_name(selector_value)
                logger.info("%s Had find the element \' %s \' successfully "
                            "by %s via value:%s" % (get_dataTime(), element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("%s NoSuchElementException:%s" % (get_dataTime(), e))
                self.get_windows_img()
        # 根据xpath定位
        elif selector_by == "x" or selector_by == "xpath":
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("%s Had find the element \' %s \' successfully "
                            "by %s via value:%s" % (get_dataTime(), element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("%s NoSuchElementException:%s" % (get_dataTime(), e))
                self.get_windows_img()
        # 根据css定位
        elif selector_by == "css" or selector_by == "css selector":
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                logger.info("%s Had find the element \' %s \' successfully "
                            "by %s via value:%s" % (get_dataTime(), element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("%s NoSuchElementException:%s" % (get_dataTime(), e))
                self.get_windows_img()
        # 无效的表达式
        else:
            logger.error("%s Please enter a valid type of targeting elements." % get_dataTime())
            raise NameError("%s Please enter a valid type of targeting elements." % get_dataTime())

        return element

        # 截图

    # 保存截图
    def get_windows_img(self):
        file_path = os.path.abspath('..') + '\\screenshots\\'
        isExists = os.path.exists(file_path)
        print(f"截图位置：{file_path}")
        # 判断文件夹是否存在，如果不存在则创建。
        if not isExists:
            try:
                os.makedirs(file_path)
            except Exception as e:
                logger.error("%s Failed new bulid folder %s" % (get_dataTime(), e))
        # 获取时间作为字符串，用作保存图片的名称
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("%s Had take screenshot and save to folder : /screenshots" % get_dataTime())
        except NameError as e:
            logger.error("%s Failed to take screenshot! %s" % (get_dataTime(), e))
            self.get_windows_img()

    # quit browser and end testing 浏览器退出方法
    def quit_browser(self):
        """
        浏览器退出方法
        :return:
        """
        logger("%s quit the browser!" % get_dataTime())
        self.driver.quit()

    # forward browser 浏览器前进方法
    def forward_browser(self):
        """
        forward browser 浏览器前进方法
        :return:
        """
        self.driver.forward()
        logger.info("%s Click forward on current page." % get_dataTime())

    # back browser 浏览器后退方法
    def back_browser(self):
        """
        back browser 浏览器后退方法
        :return:
        """
        self.driver.back()
        logger.info("%s Click back to current page." % get_dataTime())

    #  关闭当前浏览器窗口
    def close_browser(self):
        """
        关闭当前浏览器窗口
        :return:
        """
        try:
            self.driver.close()
            logger.info("%s Close and quit the browser" % get_dataTime())
        except NameError as e:
            logger.error("% Failed to quit the browser with %s" % (get_dataTime(), e))

    # # Text input 文本框输入
    # def send_keys(self, selector_object, text):
    #     """
    #     为指定的元素selector输入指的值text
    #     :param selector_object: 元素对象
    #     :param text:
    #     :return:
    #     """
    #     selector_object.clear()  # 文本框清空
    #     try:
    #         selector_object.send_keys(text)  # 输入文本信息
    #         logger.info("Had type \' %s \' in inputBox" % text)
    #     except NameError as e:
    #         logger.error("Failed to type in input box with %s" % e)
    #         self.get_windows_img()
    #
    # # Text clear 文本框清空
    # def clear(self, selector_object):
    #     """
    #     清空指定的文本框selector
    #     :param selector_object:元素对象
    #     :return:
    #     """
    #     try:
    #         selector_object.clear()
    #         logger.info("Clear text in input box before type")
    #     except NameError as e:
    #         logger.error("Failed to type in input box with %s" % e)
    #         self.get_windows_img()
    #
    # # click 点击事件
    # def click(self, selector_object):
    #     """
    #     click 点击事件
    #     :param selector_object: 元素对象
    #     :return:
    #     """
    #     try:
    #         selector_object.click()
    #         logger.info("The emement was click")  # 并不是每个元素都存在 text 属性
    #     except NameError as e:
    #         logger.error("Failed to type in input box with %s" % e)
    #         self.get_windows_img()

    # Text input 文本框输入
    def send_keys(self, selector, text):
        el = self.find_element(selector)  # 获取元素位置信息
        el.clear()  # 文本框清空
        try:
            el.send_keys(text)  # 输入文本信息
            logger.info("%s Had type \' %s \' in inputBox" % (get_dataTime(), text))
        except NameError as e:
            logger.error("%s Failed to type in input box with %s" % (get_dataTime(), e))
            self.get_windows_img()

    # Text clear 文本框清空 selector:元素位置
    def clear(self, selector):
        el = self.find_element(selector)  # 获取元素位置信息
        try:
            el.clear()
            logger.info("%s Clear text in input box before type" % get_dataTime())
        except NameError as e:
            logger.error("%s Failed to type in input box with %s" % (get_dataTime(), e))
            self.get_windows_img()

    # Text click 点击事件 selector:元素位置
    def click(self, selector):
        el = self.find_element(selector)  # 获取元素位置信息
        try:
            el.click()
            logger.info("%s The emement was click" % get_dataTime())  # 并不是每个元素都存在 text 属性
        except NameError as e:
            logger.error("%s Failed to type in input box with %s" % (get_dataTime(), e))
            self.get_windows_img()

    # get_url_title 获取网页标题
    def get_url_title(self):
        """
        get_url_title 获取当前网页标题
        :return:
        """
        logger.info("%s Current page title is %s" % (get_dataTime(), self.driver.title))
        return self.driver.title

    # 鼠标悬停在元素上
    def move_to_element(self, selector):
        """
        鼠标悬停在元素上
        :param selector:
        :return:
        """
        el = self.find_element(selector)  # 获取元素位置信息
        try:
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info("%s The mouse move on %s" % (get_dataTime(), el.text))
        except NameError as e:
            logger.error("%s Failed to the mouse move on %s " % (get_dataTime(), e))
            self.driver.get_windows_img()

    # 获取当前窗口句柄
    def current_window_handle(self):
        """
        获取当前窗口句柄
        :return:
        """
        logger.info("%s Get the current window handle" % get_dataTime())
        return self.driver.current_window_handle

    # 获取所有窗口句柄
    def window_handles(self):
        """
        获取所有窗口句柄
        :return:
        """
        logger.info("%s Get all window handles" % get_dataTime())
        return self.driver.window_handles

    # 切换窗口
    def switch_to_window(self, window=""):
        """
        切换到指定的窗口，默认为当前窗口
        :param window:
        :return:
        """
        if window == "":
            self.driver.switch_to_window(self.current_window_handle())
        else:
            self.driver.switch_to_window(window)
        logger.info("%s Switch the window" % get_dataTime())

    # 切换到当前最新打开的窗口
    def switch_to_new_window(self):
        """
        切换到当前最新打开的窗口
        :return:
        """
        logger.info("%s Switch to the current latest window" % get_dataTime())
        self.driver.switch_to.window(self.window_handles()[-1])


    # 刷新当前页面
    def refresh(self):
        """
        刷新当前页面
        :return:
        """
        logger.info("%s The page has been refreshed" % get_dataTime())
        self.driver.refresh()

    # 切换到弹窗窗口
    def switch_to_alert(self):
        """
        切换到弹窗窗口
        :return:
        """
        logger.info("%s Switch to pop-up window" % get_dataTime())
        return self.driver.switch_to.alert()

    # 同步执行js脚本:execute_script为同步执行且执行时间较短。
    # WebDriver会等待同步执行的结果然后执行后续代码；
    def execute_script(self, js):
        """
        同步执行js脚本:execute_script为同步执行且执行时间较短。
        WebDriver会等待同步执行的结果然后执行后续代码；
        :param js: js脚本
        :return:
        """
        logger.info("%s Synchronous execution of JS script: %s" % (get_dataTime(), js))
        return self.driver.execute_script(js)

    # 异步执行js脚本:execute_async_script为异步执行且执行时间较长。
    # WebDriver不会等待异步执行的结果，而是直接执行后续的代码
    def execute_async_script(self, js):
        """
        异步执行js脚本:execute_async_script为异步执行且执行时间较长。
        WebDriver不会等待异步执行的结果，而是直接执行后续的代码
        :param js: js脚本
        :return:
        """
        logger.info("%s Execute JS script asynchronously: %s" % (get_dataTime(), js))
        return self.driver.execute_async_script(js)

    # 获取sessionid
    def get_sessionid(self):
        """
        获取sessionid
        :return:
        """
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫sessionId，得具体看目标系统把sessionid存到哪个变量中
        sessionid = self.driver.execute_script('return sessionStorage.getItem("sessionId");')
        # 另外sessionid一般都直接通过返回Set-Cookies头设置到Cookie中，所以也可以从Cookie读取
        # 获取浏览器所有Set-Cookie，返回对象是字典列表
        # cookies = self.driver.get_cookies()
        # 获取单项Cookie，是不是叫sessionId取决于系统存成什么变量，单项Cookie是字典
        # cookie = self.driver.get_cookie("sessionId")
        # cookie = cookie["value"]
        # print(f"{cookies}")
        return sessionid

    # 获取token
    def get_token(self):
        """
        获取token
        :return:
        """
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
        token = self.driver.execute_script('return sessionStorage.getItem("token");')
        return token

    # 判断当前元素是否可见display
    def isdispaly(self):
        """
        判断当前元素是否可见
        :return:
        """
        return self.driver.isdispaly()

    # 滑动滚动条，到达指定的元素
    def slidingScrollbar(self, target):
        """
        滑动滚动条，到达指定的元素
        :param target:
        :return:
        """
        js = "arguments[0].scrollIntoView();"
        logger.info("%s Slide the scroll bar to the specified element: %s" % (get_dataTime(), js))
        self.driver.execute_script(js, target)


if __name__ == '__main__':
    basepage = BasePage()















