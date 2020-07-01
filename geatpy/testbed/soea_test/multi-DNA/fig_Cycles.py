import matplotlib.pyplot as plt

# from pylab import *                                 #支持中文
# mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['10', '50', '100', '200', '500', '1000']
x = range(len(names))
y = [100, 500, 1000, 2000, 5000, 10000]
y1 = [3039, 3043, 3048, 3058, 3088, 3138]
y2 = [1965.531, 1995.531833, 2033.031167, 2108.031167, 2333.031167, 2708.031]
y3 = [95.11033333, 408.9955, 700.9056667, 1129.78, 1977.664, 2475.930667]
# plt.plot(x, y, 'ro-')
# plt.plot(x, y1, 'bo-')
# pl.xlim(-1, 11)  # 限定横轴的范围
# pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y, marker='.', label='Local')
plt.plot(x, y1, marker='2', label='Cloud')
plt.plot(x, y2, marker='v', label='MEC')
plt.plot(x, y3, marker='^', color='blue', mec='b', mfc='b', label='GA algo')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0.05)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("CPU Cycles u(x10^3)")  # X轴标签
plt.ylabel("System Cost")  # Y轴标签
# plt.title("A simple plot")  # 标题

plt.show()
