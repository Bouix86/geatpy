import matplotlib.pyplot as plt

# from pylab import *                                 #支持中文
# mpl.rcParams['font.sans-serif'] = ['SimHei']

names = ['1', '5', '10', '20', '50', '100']
x = range(len(names))
y = [3100, 3100, 3100, 3100, 3100, 3100]
y1 = [129, 521, 1011, 1991, 4931, 9831]
y2 = [295.662, 548.311, 864.1228333, 1495.7465, 3390.615, 6548.73]
y3 = [123.8873333, 406.6555, 695.8115, 1110.789667, 1840.205, 2611.037167]
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
plt.xlabel("Data Size (x10^3)")  # X轴标签
plt.ylabel("System Cost")  # Y轴标签
# plt.title("A simple plot")  # 标题

plt.show()