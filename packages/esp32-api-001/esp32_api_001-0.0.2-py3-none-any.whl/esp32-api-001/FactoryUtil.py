# esp32-api-001/FactoryUtil.py

from .DataChangeUtil import DataChangeUtil
from .FlagCode import FlagCode


class FactoryUtil:
    @staticmethod
    def by_type_get_return(typeId, baudRate):
        message = ""
        if baudRate == 9600:
            if typeId == 1:
                message = FlagCode.F_SENSOR_TYPE1
            elif typeId == 2:
                message = FlagCode.F_SENSOR_NUM2
            elif typeId == 3:
                message = FlagCode.F_SENSOR_MODULE_ZERO3
            elif typeId == 4:
                message = FlagCode.F_SENSOR_MODULE_CALIBRATION4
            elif typeId == 5:
                message = FlagCode.F_SENSOR_UPDATE_ADDRESS5
            elif typeId == 6:
                message = FlagCode.F_SENSOR_UPDATE_CONCENTRATION6
            else:
                message = "功能还在开发中......"
        elif baudRate == 115200:
            if typeId == 1:
                message = FlagCode.S_SENSOR_TYPE1
            elif typeId == 2:
                message = FlagCode.S_SENSOR_NUM2
            elif typeId == 3:
                message = FlagCode.S_SENSOR_NUM3
            elif typeId == 4:
                message = FlagCode.S_SENSOR_TEMPERATURE4
            elif typeId == 5:
                message = FlagCode.S_SENSOR_HUMIDITY5
            elif typeId == 6:
                message = FlagCode.S_SENSOR_PARAMS6
            elif typeId == 7:
                message = FlagCode.S_SENSOR_CHECK7
            elif typeId == 8:
                message = FlagCode.S_SENSOR_ZERO_CALIBRATION8
            elif typeId == 9:
                message = FlagCode.S_SENSOR_SENSITIVITY_CALIBRATION9
            else:
                message = "功能还在开发中......"
        return DataChangeUtil.hex_string_to_byte_array(message)
