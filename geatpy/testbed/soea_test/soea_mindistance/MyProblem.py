# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea

"""
    一个单目标最小距离优化问题：
    有十座城市：A, B, C, D, E, F, G, H, I, J，坐标如下：
        X      Y
    [[0.4,  0.4439],
     [0.2439,0.1463],
     [0.1707,0.2293],
     [0.2293,0.761],
     [0.5171,0.9414],
     [0.8732,0.6536],
     [0.6878,0.5219],
     [0.8488,0.3609],
     [0.6683,0.2536],
     [0.6195,0.2634]]
    某旅行者从A城市出发，想逛遍所有城市，并且每座城市去且只去一次，最后要返回出发地，
而且需要从G地拿重要文件到D地，另外要从F地把公司的车开到E地，那么他应该如何设计行程方案，才能用
最短的路程来满足他的旅行需求？
    分析：在这个案例中，旅行者从A地出发，把其他城市走遍一次后回到A地，因此我们只需要考虑中间途
径的9个城市的访问顺序即可。这9个城市需要排列组合选出满足约束条件的最优的排列顺序作为最终的路线方案。
"""


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        maxormins = [1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 2  # 初始化Dim（决策变量维数）
        varTypes = [0] * Dim  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [0, 0]  # 决策变量下界
        ub = [10, 10]  # 决策变量上界
        lbin = [1, 1]  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1, 1]  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
        # 新增一个属性存储旅行地坐标
        self.places = np.array([[0.4, 0.4439],
                                [0.2439, 0.1463],
                                [0.1707, 0.2293],
                                [0.2293, 0.761],
                                [0.5171, 0.9414],
                                [0.8732, 0.6536],
                                [0.6878, 0.5219],
                                [0.8488, 0.3609],
                                [0.6683, 0.2536]]) * 10

    def aimFunc(self, pop):  # 目标函数
        x = pop.Phen  # 得到决策变量矩阵
        # 添加从0地出发且最后回到出发地
        # X = np.hstack([np.zeros((x.shape[0], 1)), x, np.zeros((x.shape[0], 1))]).astype(int)

        d = []  # 存储所有种群个体对应的总路程
        for i in range(x.shape[0]):
            distance = np.sqrt(np.square(self.places[:, 0] - x[i][0]) + np.square(self.places[:, 1] - x[i][1]))  # 计算路程
            d.append(distance)
        pl = 30 + 30 * np.log10(np.array([d])) #损失
        b = 20 / 8 * np.log2(1 + 10 ** (-pl / 10)) #网络速度
        t = 0 + 2 / b / 8                           #时间
        e = np.ones_like(t) * 2 + np.ones_like(t) #能量
        t1 = np.sum(t.T, axis=0)                  #某个情况的时间之和
        e1 = np.sum(e.T, axis=0)                  #某个情况的能量之和
        ObjV = t1 + e1                            #求得各种群成员的代价之和
        pop.ObjV = ObjV  # 把求得的目标函数值赋值给种群pop的ObjV
        # 找到违反约束条件的个体在种群中的索引，保存在向量exIdx中（如：若0、2、4号个体违反约束条件，则编程找出他们来）
        # exIdx1 = np.where(np.where(x == 3)[1] - np.where(x == 6)[1] < 0)[0]
        # exIdx2 = np.where(np.where(x == 4)[1] - np.where(x == 5)[1] < 0)[0]
        # exIdx = np.unique(np.hstack([exIdx1, exIdx2]))
        # pop.CV = np.zeros((pop.sizes, 1))
        # pop.CV[exIdx] = 1 # 把求得的违反约束程度矩阵赋值给种群pop的CV
