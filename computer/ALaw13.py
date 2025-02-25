import numpy as np
import math

def floor_to_binary_string(number):
    # 向下取整
    floored_number = math.floor(number)
    # 转为二进制字符串（去掉前缀 '0b'）
    binary_string = bin(floored_number)[2:]
    return binary_string

def encode(A, value):
    for i in range(1,7):
        if A/(2**i)<value<=(A/(2**(i-1))):
            segment=8-i
            print(f"i={i}")
            c2=bin(segment)[2:]
            print(f"段内码={c2}")
            left=A/(2**i)
            print(f"left={left}")
            v1=value-A/(2**i)
            print(f"v1={v1}")
            v2=v1/(A/(2**(i+4)))
            print(f"v2={v2}")
            v3=floor_to_binary_string(v2)
            print(f"段落码={v3}")

def decode(A,v1,v2):
    print(A/(2**(8-v1)))
    a=A/(2**(8-v1))+(A/(2**(8-v1)))*((v2+0.5)/16)
    print(f"量化值={a}")

encode(50,23.1)
decode(500,4,13)


