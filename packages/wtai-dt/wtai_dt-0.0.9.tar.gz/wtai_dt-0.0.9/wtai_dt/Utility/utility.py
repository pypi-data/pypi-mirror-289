#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class Utility:
    def __init__(self):
        pass

    def resource_path(self, relative_path):
        if getattr(sys, 'frozen', False) and 'save_data' in relative_path:
            base_path = os.path.dirname(sys.executable)
        elif hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def ScatterPlot(self, x, y, title, x_label, y_label, x_min=None,x_max=None,y_min=None,y_max=None, wind_data=None):
        plt.close()
        plt.scatter(x, y, s=1, alpha=0.5)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        if x_min:
            plt.xlim(xmin=x_min)
        if x_max:
            plt.xlim(xmax=x_max)
        if y_min:
            plt.ylim(ymin=y_min)
        if y_max:
            plt.ylim(ymax=y_max)
        plt.show()
        plt.close()

    def process_data(self, original_data):
        headers = original_data[0]
        try:
            avg_wind_speed_index = headers.index('年平均风速')
        except ValueError:
            return original_data

        new_data = [headers]
        for row in original_data[1:]:
            try:
                year_avg_speed_dict = ast.literal_eval(row[avg_wind_speed_index])
            except (ValueError, SyntaxError):
                continue

            if isinstance(year_avg_speed_dict, dict):
                for year, speed in year_avg_speed_dict.items():
                    new_row = row[:avg_wind_speed_index] + [f"{year}: {speed}"] + row[avg_wind_speed_index + 1:]
                    new_data.append(new_row)
            else:
                new_data.append(row)
        return new_data