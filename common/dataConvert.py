#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------
# @Description ：
# @File        : dataConvert.py
# @Date        : 2020-06-17
# @Author      : MiaWang
# @copyright   : Winning HealthCare
# ------


class DataConvert:
    @staticmethod
    def convert_to_str(data_to_convert):
        convert_result = data_to_convert
        type_of_data_to_convert = type(data_to_convert)
        if type_of_data_to_convert == float and data_to_convert % 1 == 0:
            convert_result = str(int(data_to_convert))
        elif type_of_data_to_convert == float or type_of_data_to_convert == int:
            convert_result = str(data_to_convert)
        elif type_of_data_to_convert == tuple:
            # 因为是给读取excel使用的，所以这里的tuple就只读第一个
            convert_result = data_to_convert[0]

        return convert_result

    @staticmethod
    def list_convert_to_str(data_to_convert):
        convert_result = data_to_convert
        type_of_data_to_convert = type(data_to_convert)
        if type_of_data_to_convert == tuple or type_of_data_to_convert == list:
            convert_result = ''
            # 输出示例："mgr_se_staff","mgr_qc_leader","fc_tech_leader"
            for index, data in enumerate(data_to_convert):
                if index == 0:
                    convert_result = '"{0}"'.format(DataConvert.convert_to_str(data))
                else:
                    convert_result = '{0}, "{1}"'.format(convert_result, DataConvert.convert_to_str(data))

        return convert_result

    @staticmethod
    def convert_to_int(data_to_convert):
        convert_result = ''
        type_of_data_to_convert = type(data_to_convert)
        if type_of_data_to_convert == float and data_to_convert % 1 == 0:
            convert_result = int(data_to_convert)
        return convert_result
