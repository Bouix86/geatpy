import numpy as np

places = np.array([[0.4, 0.4439],
                   [0.2439, 0.1463],
                   [0.1707, 0.2293],
                   [0.2293, 0.761],
                   [0.5171, 0.9414],
                   [0.8732, 0.6536],
                   [0.6878, 0.5219],
                   [0.8488, 0.3609],
                   [0.6683, 0.2536]]) * 10

x = [[5.024], [4.903]]
distance = np.sqrt(np.square(places[:, 0] - x[0]) + np.square(places[:, 1] - x[1]))  # 计算路程
pl = 30 + 30 * np.log10(np.array(distance))  # 损失
b = 20 / 8 * np.log2(1 + 10 ** (-pl / 10))  # 网络速度
t = 0 + 2 / b / 8000
# t_sum = t.sum()

# 选择卸载
l = len(t)
for i in range(l - 1, -1, -1):
    if t[i] > 4.0:
        t = np.delete(t, i)
print(t.sum())
