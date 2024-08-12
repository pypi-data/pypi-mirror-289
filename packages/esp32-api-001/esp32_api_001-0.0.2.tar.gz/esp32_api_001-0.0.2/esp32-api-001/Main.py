import random
from umqtt.simple import MQTTClient
from machine import UART, Pin
import time
import network
import json
import ntptime
from .DataChangeUtil import DataChangeUtil
from .ReturnDataSubstring import ReturnDataSubstring
from .FactoryUtil import FactoryUtil


class Main:
    sensor_flag = 1
    time_string = ''
    BAUDRATE_COPY = 115200

    @staticmethod
    def wifi_connect(ssid, password):
        # 创建并激活 WIFI 连接对象
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

        # 断开之前的连接并扫描可用 WiFi
        wlan.disconnect()
        print('扫描周围信号源：', wlan.scan())

        # 尝试连接 WiFi 并显示进度
        print("正在连接 WiFi 中", end="")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print(".", end="")
            time.sleep(0.5)
        print("")  # 添加换行，使得后续输出更清晰

        # 连接成功后，打印网络信息
        ifconfig_info = wlan.ifconfig()
        print(f"IP: {ifconfig_info[0]}")
        print(f"Netmask: {ifconfig_info[1]}")
        print(f"Gateway: {ifconfig_info[2]}")
        print(f"DNS: {ifconfig_info[3]}")

    @staticmethod
    def set_time():
        global time_string
        # 设置 NTP 服务器地址
        ntptime.host = "pool.ntp.org"
        # 同步时间
        ntptime.settime()
        # 获取当前时间
        current_time = time.localtime()
        # 将时间格式化为字符串
        time_string = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
            current_time[0], current_time[1], current_time[2],
            current_time[3], current_time[4], current_time[5])

    @staticmethod
    def emqx_connect(MQTT_BROKER, MQTT_PORT, KEEPALIVE_TIME, MQTT_USER, MQTT_PASSWORD,
                     CLIENT_ID, MQTT_TOPIC, REPLY_TOPIC,
                     ID, BAUDRATE, TX, RX, BIT,
                     PARITY, STOP):
        # Initialize variables locally instead of using globals
        arrayData = []
        global BAUDRATE_COPY
        BAUDRATE_COPY = BAUDRATE
        has_printed = False
        last_heartbeat = 0
        client = None

        def reconnect():
            nonlocal client
            while client is None:
                try:
                    client = MQTTClient(client_id=CLIENT_ID, server=MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER,
                                        password=MQTT_PASSWORD, keepalive=KEEPALIVE_TIME)
                    client.connect()
                    print("Connected to MQTT broker")
                except OSError as ex:
                    print(f"Connection failed with error {ex}. Retrying...")
                    time.sleep(5)  # Wait before retrying

        reconnect()
        # Subscribe to topic and set up UART as before...
        client.set_callback(Test.mqtt_subscribe_callback)
        client.subscribe(MQTT_TOPIC)

        # Initialize UART
        global uart
        uart = UART(ID, baudrate=BAUDRATE, tx=Pin(TX), rx=Pin(RX), bits=BIT, parity=PARITY, stop=STOP)

        while True:
            try:
                # Check for new MQTT messages and process UART data as before...
                client.check_msg()
                # Additional check for client status before ping and publish
                if client and time.ticks_diff(time.ticks_ms(), last_heartbeat) > KEEPALIVE_TIME * 1000:
                    client.ping()
                    last_heartbeat = time.ticks_ms()
                    print("Heartbeat sent.")
                # ... rest of the UART and MQTT processing logic ...
                if uart.any():
                    # Read available bytes
                    response = uart.read()
                    if response is not None:
                        arrayData.append(response)
                        # print("Received from STC8H-->", response)
                        has_printed = False
                elif arrayData and not has_printed:
                    # 合并所有的字节序列
                    merged_data = b''.join(arrayData)
                    # 使用列表推导式将每个字节转换为大写的两位十六进制数，然后使用join()方法连接这些字符串
                    hex_string = ' '.join(['{:02X}'.format(byte) for byte in merged_data])  # AA 01 02 03 04 05 06
                    rm_space = DataChangeUtil.clean_string(hex_string)
                    print(f"{time_string} Received from STC8H--------> {hex_string}")
                    # 判断是四系列数据还是七系列数据
                    data = ''
                    if hex_string[:2] == 'AA':
                        data = ReturnDataSubstring.substring_data_4(rm_space, sensor_flag)
                    elif hex_string[:2] == '3A':
                        data = ReturnDataSubstring.substring_data_7(rm_space, sensor_flag)
                    print(f"{time_string} Received from STC8H--------> {data}")
                    # 将消息推送到EMQX上,格式为JSON
                    sensor_data = {
                        "data": data
                    }
                    json_data = json.dumps(sensor_data).encode('utf-8')
                    client.publish(REPLY_TOPIC, json_data)
                    # 清空arrayData以准备接收下一批数据
                    arrayData.clear()
                    has_printed = True

            except Exception as e:
                print("Error occurred:", e)
                if client:
                    try:
                        client.disconnect()
                    except Exception as dis_e:
                        print("Error disconnecting:", dis_e)
                client = None
                # break
                # time.sleep(1)  # 暂停一秒
                reconnect()  # Attempt to reconnect instead of just sleeping

    @staticmethod
    def mqtt_subscribe_callback(topic, msg):
        global sensor_flag
        global BAUDRATE_COPY
        # 1.读取传感器类型  2.读取气体浓度  3.零点标定  4.温度等等
        string_data = msg.decode('utf-8')
        sensor_flag = int(string_data)
        code = FactoryUtil.by_type_get_return(sensor_flag, BAUDRATE_COPY)
        formatted_hex = ' '.join(f'{byte:02x}' for byte in code)
        uart.write(code)

        print("发送的指令：", sensor_flag)
        print(f"{time_string} Sent to STC8H--------> {formatted_hex.upper()}")


# 使用案例
# from esp32-api-001.Main import Main
# import random
#
# MQTT_BROKER = '47.102.120.144'
# MQTT_PORT = 1883
# CLIENT_ID = 'esp32-client-{id}'.format(id=random.getrandbits(8))
# MQTT_TOPIC = b'emqx/esp32/send'
# REPLY_TOPIC = b'emqx/stc8h/receive'
# MQTT_USER = 'admin'
# MQTT_PASSWORD = 'Semea-0407'
#
# KEEPALIVE_TIME = 30  # 设置keepalive时间为30秒
#
# # WIFI连接
# SSID = 'SemeaTech'
# PASSWORD = 'Smt-0407'
#
# # UART configuration
# ID = 2
# BAUDRATE = 115200
# TX = 17
# RX = 16
# BIT = 8
# PARITY = None
# STOP = 1
#
# Main.wifi_connect(SSID, PASSWORD)
# Main.set_time()
# Main.emqx_connect(MQTT_BROKER, MQTT_PORT, KEEPALIVE_TIME, MQTT_USER, MQTT_PASSWORD,
#                   CLIENT_ID, MQTT_TOPIC, REPLY_TOPIC,
#                   ID, BAUDRATE, TX, RX, BIT, PARITY,
#                   STOP)
