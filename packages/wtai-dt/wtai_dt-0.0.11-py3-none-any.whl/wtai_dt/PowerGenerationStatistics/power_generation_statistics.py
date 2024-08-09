#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

colors = plt.cm.tab20.colors
def process_data(power_data):
    result_dict = {}
    for key, value in power_data.items():
        parts = key.split(' ')
        if len(parts) == 2:
            unit = parts[0]
            date = parts[1]
        else:
            unit = key
            date = None
        if unit not in result_dict:
            result_dict[unit] = {}
        if date:
            result_dict[unit][date] = value
        else:
            result_dict[unit]['全场发电量'] = value
    return result_dict

def classify_columns(col):
    try:
        datetime.strptime(col, '%Y-%m-%d')
        return 'daily'
    except ValueError:
        try:
            datetime.strptime(col, '%Y-%m')
            return 'monthly'
        except ValueError:
            return 'unknown'

def wind_power_daily(data):
    plt.figure(figsize=(14, 7))
    for column in data.columns:
        data[column] = data[column].astype(float).astype(int)
    bottom = np.zeros(len(data.columns))
    for i, wind in enumerate(data.index):
        color = colors[i % len(colors)]
        plt.bar(data.columns, data.loc[wind], color=color, label=wind, bottom=bottom)
        bottom += data.loc[wind].values
    plt.xlabel('日期')
    plt.ylabel('发电量 (万kWh)')
    plt.title('每天的发电量')
    plt.xticks(rotation=90)
    if len(data.columns) >= 20:
        ncols = len(data.columns) // 3
    elif len(data.columns) >= 10:
        ncols = len(data.columns) // 2
    else:
        ncols = len(data.columns)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=ncols)
    plt.tight_layout()
    plt.show()

def wind_power_monthly(data):
    plt.close()
    plt.figure(figsize=(14, 7))
    months = data.columns
    wind_machines = data.index
    bar_width = 0.15
    x = np.arange(len(wind_machines))
    for i, month in enumerate(months):
        plt.bar(x + i * bar_width, data[month].astype(float), width=bar_width, label=f'{month} 月')
    plt.ylabel('发电量 (万kWh)')
    plt.title(f'各风机月发电量')
    plt.xticks(x + bar_width * (len(months) - 1) / 2, wind_machines)
    plt.xticks(rotation=90)
    plt.legend(title='月份')
    plt.tight_layout()
    plt.show()
    plt.close()

class PowerGenerationStatistics:
    def __init__(self, data, wind_field, power_generation_field,time_field,function):
        """
            初始化发电量统计分析类

            Args:
                data: 发电量数据
                wind_field: 风机字段
                time_field: 时间字段
                power_generation_field: 发电量字段
                function: 发电量函数:daily,monthly,all
        """
        self.data = data
        self.wind_field = wind_field
        self.time_field = time_field
        self.power_generation_field = power_generation_field
        self.function = function
        self.result_dict = {}

    def init_data(self):
        self.data[self.time_field] = pd.to_datetime(self.data[self.time_field])

    def day_generate(self, data, field, time):
        # 计算日发电量
        data[time] = pd.to_datetime(data[time])
        data = data.sort_values(time)
        data = data.set_index(time)
        data['day'] = data[field].diff()
        day_energy = data['day'].resample('D').sum()
        day_energy = {str(k.date()): v for k, v in day_energy.items()}  # 将日期转换为字符串格式
        print(day_energy)
        return day_energy

    def month_generate(self, data, field, time):
        # 计算月发电量
        data[time] = pd.to_datetime(data[time])
        data = data.sort_values(time)
        data = data.set_index(time)
        data['month'] = data[field].diff()
        month_energy = data['month'].resample('M').sum()
        month_energy = {k.strftime('%Y-%m'): v for k, v in month_energy.items()}  # 将日期转换为年-月格式
        print(month_energy)
        return month_energy

    def total_generate(self, data, field, time):
        data[time] = pd.to_datetime(data[time])
        data = data.sort_values(time)
        data = data.set_index(time)
        data['total'] = data[field].diff()
        total_power = data['total'].sum()
        print(total_power)
        return {'全场发电量': total_power}

    def power_analysis(self):
        d = self.data.groupby(self.wind_field)
        field = self.power_generation_field
        time = self.time_field
        for group_name, group_data in d:
            if self.function == 'daily':
                result_dict = self.day_generate(group_data, field, time)
            elif self.function == 'monthly':
                result_dict = self.month_generate(group_data,field,time)
            elif self.function == 'all':
                result_dict = self.total_generate(group_data,field,time)
            else:
                print("请选择正确的发电量计算函数:daily,monthly,all")
                return
            temp_dict = {}
            for key, value in result_dict.items():
                result_key = "风机" + str(group_name) + " " + key
                temp_dict.setdefault(result_key, str(value))
                self.result_dict[result_key] = str(value)

    def plot_image(self):
        result = process_data(self.result_dict)
        data = pd.DataFrame(result).T
        data = data.fillna(0)
        try:
            data = data.drop(columns=['全场发电量'])
            data = data.drop(index=['全场发电量'])
        except Exception as e:
            return e
        classification = {col: classify_columns(col) for col in data.columns}
        monthly_df , daily_df = None, None
        try:
            monthly_df = data[[col for col, clas in classification.items() if clas == 'monthly']]
            daily_df = data[[col for col, clas in classification.items() if clas == 'daily']]
        except Exception as e:
            print(e)
        if monthly_df is not None:
            wind_power_monthly(monthly_df)
            print('各机组月发电量画图完成')
            print('各机组月发电量数据提取成功')
        else:
            print('无法提取各机组月发电量数据')

        if daily_df is not None:
            wind_power_daily(daily_df)
            print('每天的发电量画图完成')
            print('每天的发电量数据提取成功')
        else:
            print('无法提取每天的发电量数据')