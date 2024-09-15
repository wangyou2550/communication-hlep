import numpy as np
from scipy.integrate import quad
from fractions import Fraction

# 定义一个函数将小数转换为分数
def decimal_to_fraction(decimal_number):
    # 使用 Fraction 将小数转换为分数
    fraction = Fraction(decimal_number).limit_denominator()
    return fraction

# 示例
# decimal_number = 0.0462962962962963
# result = decimal_to_fraction(decimal_number)
#
# print(f"The fraction representation of {decimal_number} is: {result}")

# 定义概率密度函数 f(x)
def f(x):
    return (-x+4) / 16 if 0 <= x <= 4 else 0

# 定义第一个积分的被积函数
def integrand1(x):
    return (x-1) ** 2 * f(x)

# 定义第二个积分的被积函数
def integrand2(x):
    return (x-3) ** 2 * f(x)

# 定义第三个积分的被积函数
def integrand3(x):
    return (2.5 - x) ** 2 * f(x)

def integrand4(x):
    return (x**2)

# 计算各个积分
I1, _ = quad(integrand1, 0, 2)
I2, _ = quad(integrand2, 2, 4)

print(decimal_to_fraction(I1))
print(decimal_to_fraction(I2))
# 计算总和
result = (I1 + I2 )*2

print(f"Total result: {decimal_to_fraction(result)}")