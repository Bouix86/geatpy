# 用来主牌标准差之类的脚本
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 读取数据
names = ['10', '50', '100', '200', '500', '1000']
x = range(len(names))
y = [100, 500, 1000, 2000, 5000, 10000]
y1 = [3039, 3043, 3048, 3058, 3088, 3138]
y2 = [1965.531, 1995.531833, 2033.031167, 2108.031167, 2333.031167, 2708.031]
y3 = [95.11033333, 408.9955, 700.9056667, 1129.78, 1977.664, 2475.930667]
yerr = [0, 0, 0, 0, 0, 0]
yerr1 = [3408, 3408, 3408, 3408, 3408, 3408]
yerr2 = [2197, 2197, 2197, 2197, 2197, 2197]
yerr3 = [10.9, 147.9, 345.5, 728.1, 1733.3, 2381.5]

# 绘图部分 
# 标记样式常用的值有（./,/o/v/^/s/*/D/d/x/</>/h/H/1/2/3/4/_/|）https://www.jianshu.com/p/b992c1279c73，参考
plt.errorbar(x, y, yerr, fmt='k-o', lw=2, ecolor='k', elinewidth=1, ms=7, capsize=3)
plt.errorbar(x, y1, yerr1, fmt='k-x', lw=2, ecolor='r', elinewidth=1, ms=7,
             capsize=3)
plt.errorbar(x, y2, yerr2, fmt='k-d', lw=2, ecolor='c', elinewidth=1, ms=7,
             capsize=3)
plt.errorbar(x, y3, yerr3, fmt='k-s', lw=2, ecolor='b', mec='b', mfc='b', elinewidth=1, ms=7,
             capsize=3)

# 设置坐标轴标签文本
Songti = fm.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')  # 创建宋体
plt.xlabel('growth stage\n', fontsize=14)
plt.ylabel('Upper light interception', fontsize=14)
# 创建字体，设置图例 windows自带字体路径

plt.legend(fontsize=19, ncol=2)
plt.tight_layout()  # 防止保存时大小不合适
# plt.savefig(r'C:\Users\Administrator\Desktop\{}.jpg'.format('Upper light interception'), dpi=400)
plt.show()
