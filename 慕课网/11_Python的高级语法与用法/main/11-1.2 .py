from enum import Enum


class VIP(Enum):  # 继承
    # 常量
    # 枚举的意义重在标签,不在数值
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# VIP.YELLOW  VIP.GREEN VIP.BLACK (用枚举的方式表示类型)
print(VIP.YELLOW)
