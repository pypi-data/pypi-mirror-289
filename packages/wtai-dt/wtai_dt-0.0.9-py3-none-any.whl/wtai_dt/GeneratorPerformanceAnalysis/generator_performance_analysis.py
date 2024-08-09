#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class GeneratorPerformance:
    def __init__(self, data, filed1, filed2, xlabel, ylable, function):
        """
            初始化发电性能分析绘图类,转矩-转速曲线,转速-桨距角曲线,风速-桨距角曲线,风速-转速曲线,风速-功率曲线

            Args:
                data: 绘图数据
                filed1: X轴字段
                filed2: Y轴字段
                xlabel: X轴label
                ylabel: Y轴label
                function: 绘制的具体曲线
        """

        self.data = data
        self.filed1 = filed1
        self.filed2 = filed2
        self.function = function
        self.labels= [xlabel,ylable]

    def Plot(self):
        self.ScatterPlot(self.data[self.filed1],self.data[self.filed2],self.function,self.labels)

    def ScatterPlot(self, x, y, title, labels, is_wind=False, wind_data=None):
        plt.close()
        plt.scatter(x, y, s=1, alpha=0.5)
        if is_wind:
            wind_data_float = {float(k): float(v) for k, v in wind_data.items()}
            plt.plot(list(wind_data_float.keys()), list(wind_data_float.values()))
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.title(title)
        if "转矩-转速曲线" in title:
            plt.xlim(xmin=0, xmax=1600)
        elif "转速-桨距角曲线" in title or "风速-桨距角曲线" in title:
            plt.xlim(xmin=0, xmax=25)
            plt.ylim(ymin=-5, ymax=30)
        elif "风速-转速曲线" in title:
            plt.xlim(xmin=0, xmax=25)
        else:
            plt.ylim(ymin=y.min(), ymax=float(y.max()) * 1.3)
        plt.show()
        plt.close()