# -*-coding:utf-8-*-
# """MyProblem.py"""
import numpy as np
import geatpy as ea


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):
        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        # #初始化maxormins（目标最小最大化标记列表，1：最小化；-1：最大化）
        maxormins = [1]
        Dim = 12  # 初始化Dim（决策变量维数）
        # #初始化决策变量的类型，元素为0表示变量是连续的；1为离散的
        varTypes = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        lb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 决策变量下界
        ub = [10, 10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界
        ubin = [1] * Dim  # 决策变量上边界
        # #调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
        self.places = np.array([[0.1707, 0.2293],
                                [0.2293, 0.761],
                                [0.2439, 0.1463],
                                [0.4, 0.4439],
                                [0.5171, 0.9414],
                                [0.6195, 0.2634],
                                [0.6683, 0.2536],
                                [0.6878, 0.5219],
                                [0.8488, 0.3609],
                                [0.8732, 0.6536]])*10

    def aimFunc(self, pop):  # 目标函数
        X = pop.Phen  # 得到决策变量矩阵
        # x1 = X[:, [0]]
        # x2 = X[:, [1]]
        # x3 = X[:, [2]]
        # x4 = X[:, [3]]
        # x5 = X[:, [4]]
        # x6 = X[:, [5]]
        # x7 = X[:, [6]]
        # x8 = X[:, [7]]
        # x9 = X[:, [8]]
        # x10 = X[:, [9]]
        # x11 = X[:, [10]]

        C = 200
        D = 20
        F_localCPU = 1
        F_cloudCPU = 50
        F_MECCPU = 5
        e_localCPU = 1
        e_cloudCPU = 0
        e_MECCPU = 0.5
        R_cellular = 1
        R_wifi = 5
        e_cloudcellular = 18.6
        e_MECwifi = 12.6

        d = []  # 存储所有种群个体对应的总路程
        for i in range(X.shape[0]):
            distance = np.sqrt(np.square(self.places[:, 0] - X[i][0]) + np.square(self.places[:, 1] - X[i][1]))  # 计算路程
            d.append(distance)
        pl = 30 + 30 * np.log10(np.array([d]))  # 损失
        b = 2000000 / 8 * np.log2(1 + 10 ** (-pl / 10))  # 网络速度
        # t = 0 + 2 / b / 80  # 时间

        # t1 = np.sum(t.T, axis=0)

        infor = np.zeros((X.shape[0], X.shape[1] - 2))
        for i in range(X.shape[0]):
            for j in range(X.shape[1] - 2):
                if (X[i][j + 2] == 0):
                    T_local = C / F_localCPU
                    E_local = C * e_localCPU
                    infor[i][j] = 0.5 * E_local + 0.5 * T_local#200
                    # infor[i][j] = 0 * E_local + 1 * T_local  # 200
                elif (X[i][j+2] == 1):
                    T_cloud = C / F_cloudCPU + D / R_cellular# 2+10
                    E_cloud = D * e_cloudcellular# 186
                    infor[i][j] = 0.5 * E_cloud + 0.5 * T_cloud#206
                    # infor[i][j] = 0 * E_cloud + 1 * T_cloud  # 206
                else:
                    T_MEC = C / F_MECCPU + D / b[0][i][j]#20+2
                    E_MEC = C * e_MECCPU + D * e_MECwifi#50+126
                    infor[i][j] = 0.5 * E_MEC + 0.5 * T_MEC#198
                    # infor[i][j] = 0 * E_MEC + 1 * T_MEC  # 198


        Objv = np.sum(infor, axis=1)
        Objv = np.reshape(Objv, (X.shape[0], 1))


        pop.ObjV = Objv

        # pop.ObjV = np.sin(2 * x1) - np.cos(x2) + 2 * x3 ** 2 - 3 * x4 + (x5 - 3) ** 2 + 7 * x6 + 8 * x7 + 9 * x8 + 10 * x9  # 计算目标函数值，赋值给pop种群对象的ObjV属性
