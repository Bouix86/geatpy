import numpy as np
import matplotlib.pyplot as plt

places = np.array([[0.1707, 0.2293],
                   [0.2293, 0.761],
                   [0.2439, 0.1463],
                   [0.4, 0.4439],
                   [0.5171, 0.9414],
                   [0.6195, 0.2634],
                   [0.6683, 0.2536],
                   [0.6878, 0.5219],
                   [0.8488, 0.3609],
                   [0.8732, 0.6536]]) * 10
C = 1000
D = 100
F_localCPU = 1
F_cloudCPU = 50
F_MECCPU = 5
e_localCPU = 1
e_cloudCPU = 0
e_MECCPU = 0.1
R_cellular = 1
R_wifi = 5
e_cloudcellular = 18.6
e_MECwifi = 12.6

d = np.zeros((10))  # 存储所有种群个体对应的总路程
for i in range(10):
    d[i] = np.sqrt(np.square(places[i, 0] - 5.086) + np.square(places[i, 1] - 4.783))  # 计算路程
pl = 30 + 30 * np.log10(np.array([d]))  # 损失
b = 200000 / 8 * np.log2(1 + 10 ** (-pl / 10))  # 网络速度

infor = np.zeros((10))
# for i in range(10):
T_MEC = C / F_MECCPU + D / b
E_MEC = C * e_MECCPU + D * e_MECwifi
infor = 0 * E_MEC + 1 * T_MEC
#     T_cloud = C / F_cloudCPU + D / R_cellular# 2+10
#     E_cloud = D * e_cloudcellular# 186
#     infor[i] = 0 * E_cloud + 1 * T_cloud#206
print(np.sum(infor))


# # -*- coding: utf-8 -*-
#
#
# plt.bar(1, 3100, label='Local')
# plt.bar(2, 3069, label='Cloud')
# plt.bar(3, 2190, label='MEC')
# plt.bar(4, 1131, color='b', label='EA')
#
# # plt.bar([2, 4, 6, 8, 10], [4, 6, 8, 13, 15], label='graph 2')
#
# # params
#
# # x: 条形图x轴
# # y：条形图的高度
# # width：条形图的宽度 默认是0.8
# # bottom：条形底部的y坐标值 默认是0
# # align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘
#
# plt.legend()
#
# plt.xlabel('Strategies')
# plt.ylabel('Average System Cost')
#
#
# plt.show()
