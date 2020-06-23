#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------
# @Description ：
# @File        : bugCountByDate.py
# @Date        : 2020-06-18
# @Author      : MiaWang
# @copyright   : Winning HealthCare
# ------
from seleniumbase import BaseCase
import datetime
from input.inputs import *


class BugCountByDate(BaseCase):

    def bug_count_by_Date(production, datetime):
        return  None


    @staticmethod
    def date_range():
        dates = []
        dt = datetime.datetime.strftime(TEST_START_DATE, "%Y-%m-%d")
        date = TEST_START_DATE[:]
        while date <= TEST_END_DATE:
            dates.append(date)
            dt = dt + datetime.timedelta(1)
            date = dt.strftime("%Y-%m-%d")
        return dates
