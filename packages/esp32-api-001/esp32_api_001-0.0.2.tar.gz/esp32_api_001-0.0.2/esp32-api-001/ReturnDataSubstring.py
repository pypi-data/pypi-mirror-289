# esp32-api-001/ReturnDataSubstring.py

from .DataChangeUtil import DataChangeUtil
from .FlagCode import FlagCode


class ReturnDataSubstring:

    @staticmethod
    def switch_type_4(choose_id):
        msg = ""
        choose_id = int(choose_id)
        if choose_id in {0, 1, 6, 12, 16, 18, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 40}:
            msg = "无"
        elif choose_id == 2:
            msg = "CO"
        elif choose_id == 3:
            msg = "O2"
        elif choose_id == 4:
            msg = "H2"
        elif choose_id == 5:
            msg = "CH4"
        elif choose_id == 7:
            msg = "CO2"
        elif choose_id == 8:
            msg = "O3"
        elif choose_id == 9:
            msg = "H2S"
        elif choose_id == 10:
            msg = "SO2"
        elif choose_id == 11:
            msg = "NH3"
        elif choose_id == 13:
            msg = "ETO"
        elif choose_id == 14:
            msg = "HCL"
        elif choose_id == 15:
            msg = "PH3"
        elif choose_id == 17:
            msg = "HCN"
        elif choose_id == 19:
            msg = "HF"
        elif choose_id == 21:
            msg = "NO"
        elif choose_id == 22:
            msg = "NO2"
        elif choose_id == 23:
            msg = "NOX"
        elif choose_id == 24:
            msg = "CLO2"
        elif choose_id == 31:
            msg = "THT"
        elif choose_id == 32:
            msg = "C2H2"
        elif choose_id == 33:
            msg = "C2H4"
        elif choose_id == 34:
            msg = "CH2O"
        elif choose_id == 39:
            msg = "C2H3CL"
        elif choose_id == 41:
            msg = "CH3SH"
        else:
            msg = "不在定义范围内，没有对应的气体类型"
        return "监测气体:" + msg

    @staticmethod
    def substring_data_4(old_data, type_id):
        type_ = ""
        new_data = ""
        if type_id == 1:
            new_data = old_data[6:8]
            type_ = ReturnDataSubstring.switch_type_4(DataChangeUtil.hex_to_decimal(new_data))
        elif type_id == 2:
            new_data = old_data[8:14]
            type_ = str(DataChangeUtil.hex_to_decimal(new_data)) + " ppm"
        elif type_id == 3:
            type_ = "模块校零失败"
            if DataChangeUtil.clean_string(FlagCode.F_SENSOR_MODULE_ZERO3_TRUE) == old_data:
                type_ = "模块校零成功"
        elif type_id == 4:
            type_ = "模块标定失败"
            if DataChangeUtil.clean_string(FlagCode.F_SENSOR_MODULE_CALIBRATION4_TRUE) == old_data[:12]:
                type_ = "模块标定成功"
        return type_

    @staticmethod
    def switch_type_7(choose_id):
        msg = ""
        choose_id = int(choose_id)
        if choose_id in {0, 1, 6, 16, 18, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38}:
            msg = "无"
        elif choose_id == 2:
            msg = "CO"
        elif choose_id == 3:
            msg = "O2"
        elif choose_id == 4:
            msg = "H2"
        elif choose_id == 5:
            msg = "CH4"
        elif choose_id == 7:
            msg = "CO2"
        elif choose_id == 8:
            msg = "O3"
        elif choose_id == 9:
            msg = "H2S"
        elif choose_id == 10:
            msg = "SO2"
        elif choose_id == 11:
            msg = "NH3"
        elif choose_id == 12:
            msg = "CL2"
        elif choose_id == 13:
            msg = "ETO"
        elif choose_id == 14:
            msg = "HCL"
        elif choose_id == 15:
            msg = "PH3"
        elif choose_id == 17:
            msg = "HCN"
        elif choose_id == 19:
            msg = "HF"
        elif choose_id == 21:
            msg = "NO"
        elif choose_id == 22:
            msg = "NO2"
        elif choose_id == 23:
            msg = "NOX"
        elif choose_id == 24:
            msg = "CLO2"
        elif choose_id == 31:
            msg = "THT"
        elif choose_id == 32:
            msg = "C2H2"
        elif choose_id == 33:
            msg = "C2H4"
        elif choose_id == 34:
            msg = "CH2O"
        elif choose_id == 39:
            msg = "CH3SH"
        elif choose_id == 40:
            msg = "C2H3CL"
        else:
            msg = "不在定义范围内，没有对应的气体类型"
        return "监测气体:" + msg

    @staticmethod
    def substring_data_7(old_data, type_id):
        type_ = ""
        new_data = ""
        if type_id == 1:
            new_data = old_data[6:8]
            type_ = ReturnDataSubstring.switch_type_7(DataChangeUtil.hex_to_decimal(new_data))
        elif type_id == 2:
            new_data = old_data[12:20]
            type_ = str(DataChangeUtil.hex_to_decimal(new_data)) + "μg/m³"
        elif type_id == 3:
            new_data = old_data[12:20]
            type_ = str(DataChangeUtil.hex_to_decimal(new_data)) + "ppb"
        elif type_id == 4:
            new_data = old_data[12:16]
            type_ = "监测温度为:" + str(DataChangeUtil.hex_to_decimal(new_data) / 100) + "°C"
        elif type_id == 5:
            new_data = old_data[12:16]
            type_ = "监测湿度为:" + str(DataChangeUtil.hex_to_decimal(new_data) / 100) + "%RH"
        elif type_id == 6:
            data1 = DataChangeUtil.hex_to_decimal(old_data[12:20])
            data2 = DataChangeUtil.hex_to_decimal(old_data[20:28])
            data3 = DataChangeUtil.hex_to_decimal(old_data[28:32])
            data4 = DataChangeUtil.hex_to_decimal(old_data[32:36])
            type_ = "浓度值:\t" + str(data1) + " μg/m³, " + \
                    "浓度值:\t " + str(data2) + "ppb, " + \
                    "温度值:\t " + str(data3) + "°C, " + \
                    "湿度值: \t" + str(data4) + "%RH"
        elif type_id == 8:
            new_data = old_data[12:16]
            type_ = "零点标定返回数值:" + str(DataChangeUtil.hex_to_decimal(new_data))
        elif type_id == 9:
            flag = "标定成功"
            substring = old_data[6:8]
            if substring == "01":
                flag = "标定中"
            elif substring == "02":
                flag = "标定失败"
            type_ = "标定结果:" + flag
        return type_
