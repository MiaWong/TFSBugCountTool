#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------
# @Description ：
# @File        : inputs.py
# @Date        : 2020-06-22
# @Author      : MiaWang
# @copyright   : Winning HealthCare
# ------
# bug统计开始时间与结束时间
# 开始时间会统计开始时间之前带有这个标题与模块的bug数不仅仅是当天，因为有可能环境搭建，或冒烟测试时就会提一部分的bug
TEST_START_DATE = '2020-05-22'
TEST_END_DATE = '2020-07-22'

# 建议在封版期间有一个公共文档登记封版期间模块的标题，这样统计bug的时候就可以直接拿来用，不用再查一遍
# 示例：护理管理V5.5.202007封版测试 - 【一键部署】 -
PRODUCTION_NAME = '医务管理系统201907版本封版测试'

MODULE_NAME_LIST = ['-考试培训', '-基础业务支持平台', '-基础业务支撑平台', '-医务管理']

