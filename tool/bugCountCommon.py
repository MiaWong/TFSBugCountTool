#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------
# @Description ：
# @File        : bugCountCommon.py
# @Date        : 2020-06-22
# @Author      : MiaWang
# @copyright   : Winning HealthCare
# ------
from input.inputs import *
from selenium.webdriver.common.by import By
from tool.elementPath import *
from seleniumbase import BaseCase
import time


class BugCountCommon(BaseCase):
    def test_count_total_bug(self):
        self.get_bug_count_total()

    def get_bug_count_total(self):
        self.new_query()
        # 工作项类型= bug
        self.input_a_set_query(field_xpath=QUERY_FIELD_TEXT_INPUT_XPATH_1, field_value=FIELD_WORK_TYPE,
                               operator_xpath=QUERY_OPERATOR_TEXT_INPUT_XPATH_1, operator_value=operator_equal,
                               value_xpath=QUERY_VALUE_TEXT_INPUT_XPATH_1, value_value=VALUE_WORK_TYPE_BUG)
        # and 标题 包含 productiontitle
        self.input_a_set_query(field_xpath=QUERY_FIELD_TEXT_INPUT_XPATH_2, field_value=FIELD_TITLE,
                               operator_xpath=QUERY_OPERATOR_TEXT_INPUT_XPATH_2, operator_value=operator_contain,
                               value_xpath=QUERY_VALUE_TEXT_INPUT_XPATH_2, value_value=PRODUCTION_NAME,
                               and_or_xpath=QUERY_AND_OR_TEXT_INPUT_XPATH_2, and_or_value=AND_OR_AND)

        self.click(RUN_QUERY_BUTTON_XPATH, by=By.XPATH)

        time.sleep(10)
        while not self.find_element(result_class, by=By.CLASS_NAME):
            time.sleep(10)

        result_count = self.find_elements(result_class, by=By.CLASS_NAME)
        return result_count.size()

    def new_query(self):
        self.open(TFS_URL)
        time.sleep(10)
        self.click(QUERIES_NEW_BUTTON, by=By.XPATH)
        self.click(QUERIES_NEW_QUERY_BUTTON, by=By.XPATH)

    #
    def input_a_set_query(self, field_xpath, field_value, operator_xpath,
                          operator_value, value_xpath, value_value, and_or_xpath='', and_or_value=''):
        if and_or_value:
            self.input_text_xpath(and_or_xpath, and_or_value)
        self.input_text_xpath(field_xpath, field_value)
        self.input_text_xpath(operator_xpath, operator_value)
        self.input_text_xpath(value_xpath, value_value)

    def input_text_xpath(self, xpath, value):
        self.input(xpath, value, by=By.XPATH)
