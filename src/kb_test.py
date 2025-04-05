from machine import I2C, Pin
import time

# I2C 配置
I2C_SDA = 6   # 根据你的连接修改
I2C_SCL = 7   # 根据你的连接修改
I2C_ADDR = 31
scp=Pin(18,Pin.IN,Pin.PULL_UP)
sdp=Pin(17,Pin.IN,Pin.PULL_UP)

# 创建 I2C 对象
i2c = I2C(1, scl=scp, sda=sdp, freq=10000)  # 10kHz 与 Arduino 代码匹配

# 寄存器地址
REG_ID_FIF = 0x01  # FIFO 读取寄存器（根据 Arduino 代码）
REG_ID_KEY = 0x02  # 键盘状态寄存器（CapsLock, NumLock 状态）
print(i2c.scan())

def get_key_event():

    data = i2c.readfrom_mem(I2C_ADDR, 0x09,2)
    print(data)


print("等待按键输入...")
while True:
    get_key_event()

    time.sleep(0.1)  # 避免轮询过快