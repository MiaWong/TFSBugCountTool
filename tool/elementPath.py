#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------
# @Description ：
# @File        : elementPath.py
# @Date        : 2020-06-18
# @Author      : MiaWang
# @copyright   : Winning HealthCare
# ------

# URL
TFS_URL = "http://tfs2018-web.winning.com.cn:8080/tfs/WN_HIS/%E5%8C%BB%E7%96%97%E8%B4%A8%E9%87%8F%E7%AE%A1%E7%90%86/_workItems/index"

# new query button
QUERIES_NEW_BUTTON = '//*[@id="mi_86_new"]/span[1]'
# 下拉列表的 new query
QUERIES_NEW_QUERY_BUTTON = '//*[@id="mi_640_new-query"]/span[2]'

bug_level_field = '严重级别'
Bug_Level = ['1 - 严重', '2 - 高', '3 - 中', '4 - 低']

# 运算符
operator_equal = '='
operator_more = '>'
operator_less = '<'
#operator_contain = '包含'
operator_contain = 'Contains Words'

# and or
AND_OR_AND = 'And'
AND_OR_OR = 'Or'

# 第一行输入条件
# Field
QUERY_FIELD_TEXT_INPUT_XPATH_1    = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[5]/div/div[1]/input'
FIELD_WORK_TYPE = '工作项类型'
# Operator
QUERY_OPERATOR_TEXT_INPUT_XPATH_1 = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[6]/div/div[1]/input'
# value
QUERY_VALUE_TEXT_INPUT_XPATH_1  = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[7]/div/div/div[1]/input'
VALUE_WORK_TYPE_BUG = 'Bug'

# 第二行输入条件
# And/Or
QUERY_AND_OR_TEXT_INPUT_XPATH_2 = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[3]/td[4]/div/div[1]/input'
# Field
QUERY_FIELD_TEXT_INPUT_XPATH_2    = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[5]/div/div[1]/input'
FIELD_TITLE = '标题'
# Operator
QUERY_OPERATOR_TEXT_INPUT_XPATH_2 = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[6]/div/div[1]/input'
# value
QUERY_VALUE_TEXT_INPUT_XPATH_2  = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[7]/div/div/div[1]/input'

# 添加一行新的查询条件
ADD_NEW_CLAUSE_XPATH = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[4]/td/div/span[2]'

# 第三行输入条件
QUERY_AND_OR_TEXT_INPUT_XPATH_3 = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[4]/td[4]/div/div[1]/input'
QUERY_FIELD_TEXT_INPUT_XPATH_3    = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[5]/div/div[1]/input'
QUERY_OPERATOR_TEXT_INPUT_XPATH_3 = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[6]/div/div[1]/input'
QUERY_VALUE_TEXT_INPUT_XPATH_3  = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[3]/fieldset/div/table/tbody/tr[2]/td[7]/div/div/div[1]/input'

# 运行查询条件按钮
RUN_QUERY_BUTTON_XPATH = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[3]/div[4]/div[2]/div/div[2]/div/div[1]/div[1]/ul/li[3]/span[1]'

# 结果列表
# 第一行
result_class = 'grid-row grid-row-normal'
