import numpy as np
import matplotlib.pyplot as plt

A = 1  # 幅值
T = 1  # 周期
fc = 4 / T  # 载波频率

t = np.linspace(0, 2 * T, 1000)  # 时间范围
y = np.zeros_like(t)  # 输出信号

for i in range(len(t)):
    if 0 <= t[i] < T:
        tau = np.linspace(0, T, 1000)
        integrand = 0.5 * np.cos((16 * np.pi * tau - 16 * np.pi * t[i]) / T) + 0.5 * np.cos((16 * np.pi * tau + 16 * np.pi * t[i]) / T)
        y[i] = A**2 * np.trapz(integrand, tau)

plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Output Signal y(t)')
plt.grid(True)
plt.show()