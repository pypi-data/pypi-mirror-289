# esp32api/DataChangeUtil.py

import re


class DataChangeUtil:

    @staticmethod
    def hex_string_to_byte_array(s):
        s = DataChangeUtil.clean_string(s)
        if s:
            try:
                if len(s) % 2 != 0:
                    s += "0"
                result = bytearray()
                for i in range(0, len(s), 2):
                    hex_pair = s[i:i + 2]
                    result.append(int(hex_pair, 16))
                return result
            except ValueError as e:
                print(f"Error: {e}")
        return bytearray()

    @staticmethod
    def clean_string(s):
        return re.sub(r'[^0-9A-Fa-f]', '', s)

    @staticmethod
    def byte_array_to_hex_string(byte_array):
        return ''.join(f'{b:02X}' for b in byte_array)

    @staticmethod
    def hex_to_decimal(hex_str):
        # 使用int()函数将十六进制字符串转换为整数
        big_integer = int(hex_str, 16)

        # 使用float()函数将整数转换为浮点数
        # 并使用round()函数对浮点数进行四舍五入
        big_decimal = round(float(big_integer), 2)
        return big_decimal

    @staticmethod
    def decimal_to_hex(concentration):
        hex_string = f'{concentration:04X}'
        formatted_hex = ' '.join(hex_string[i:i + 2] for i in range(0, len(hex_string), 2))
        return formatted_hex.strip()
