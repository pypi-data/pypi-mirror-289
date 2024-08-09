#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
colors = plt.cm.tab20.colors


def wind_error_image(data, group_one, group_two, x_label, y_label, title, image_name, types=None):
    plt.close()
    plt.figure(figsize=(12, 6))

    if types:
        use_data = data[data['types'] == types]
    else:
        use_data = data

    if use_data.empty:
        plt.bar([], [])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
        return

    grouped = use_data.groupby([group_one, group_two])['count'].agg('sum').unstack().fillna(0)
    error_types = grouped.columns

    bottom = np.zeros(len(grouped))
    for i, error_type in enumerate(error_types):
        color = colors[i % len(colors)]
        plt.bar(grouped.index, grouped[error_type], bottom=bottom, label=error_type, color=color)
        bottom += grouped[error_type].values

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(title='故障类型', loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=len(error_types))
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    plt.close()

class SCADAError:
    def __init__(self, data, wind_field, start_time_field, end_time_field, error_type_field, function):
        """
        分析SCADA系统故障数据

        Args:
            data: 故障数据
            wind_field: 风机字段
            start_time_field: 故障开始时间字段
            end_time_field: 故障结束时间字段
            error_type_field: 故障类型字段
            function: 故障分析方法:故障次数,停机时间
        """

        self.data = data
        self.wind_field = wind_field
        self.start_time_field = start_time_field
        self.end_time_field = end_time_field
        self.error_type_field = error_type_field
        self.function = function
        self.result = {}
        self.result_dict = {}
        self.init_data()

    def init_data(self):
        self.data[self.start_time_field] = pd.to_datetime(self.data[self.start_time_field], errors='coerce')
        self.data[self.end_time_field] = pd.to_datetime(self.data[self.end_time_field], errors='coerce')

    def error_time(self, data, start_time, end_time, error_status):
        data = data[data[error_status].str.contains('故障')]
        df = data.sort_values(by=[start_time])

        def is_overlapping(start1, end1, start2, end2):
            tolerance = pd.Timedelta(minutes=30)
            return end1 + tolerance >= start2

        def merge_intervals(intervals):
            if not intervals:
                return []
            sorted_intervals = sorted(intervals, key=lambda x: x[0])
            merged = [sorted_intervals[0]]
            for current in sorted_intervals[1:]:
                previous = merged[-1]
                if is_overlapping(previous[0], previous[1], current[0], current[1]):
                    merged[-1] = (previous[0], max(previous[1], current[1]), previous[2])
                else:
                    merged.append(current)
            return merged

        intervals = list(
            zip(df[start_time], df[end_time], df[error_status]))
        merged_intervals = merge_intervals(intervals)
        fault_analysis = {
            'Total Faults': len(merged_intervals),
            'Fault Details': [{'Start': start, 'End': end, 'Fault Code': code, 'Duration': end - start} for
                              start, end, code
                              in merged_intervals],
            'Total Duration': sum((end - start).total_seconds() for start, end, code in merged_intervals)
        }
        return fault_analysis

    def down_time(self, data, error_status, start_time, end_time):
        data = data[data[error_status].str.contains('故障')]
        df = data.sort_values(by=[start_time])

        def is_overlapping(start1, end1, start2, end2):
            return max(start1, start2) <= min(end1, end2)

        def merge_intervals(intervals):
            if not intervals:
                return []

            sorted_intervals = sorted(intervals, key=lambda x: x[0])

            merged = [sorted_intervals[0]]
            for current in sorted_intervals:
                previous = merged[-1]
                if is_overlapping(previous[0], previous[1], current[0], current[1]):
                    merged[-1] = (previous[0], max(previous[1], current[1]), previous[2])
                else:
                    merged.append(current)

            return merged

        intervals = list(
            zip(df[start_time], df[end_time], df[error_status]))
        merged_intervals = merge_intervals(intervals)
        fault_analysis = {
            'Total Faults': len(merged_intervals),
            'Fault Details': [{'Start': start, 'End': end, 'Fault Code': code, 'Duration': end - start} for
                              start, end, code in merged_intervals]
        }
        return fault_analysis['Total Faults']

    def error_analysis(self):
        try:
            datas = self.data.groupby(self.wind_field)
            rows = []
            fault_analysis = {}
            for index, data in datas:
                data = data.reset_index(drop=True)
                use_result = self.error_time(data, self.start_time_field,
                                        self.end_time_field,
                                        self.error_type_field)
                fault_analysis[index] = {
                    'Total Faults': use_result['Total Faults'],
                    'Fault Details': use_result['Fault Details']
                }
                for detail in use_result['Fault Details']:
                    rows.append({
                        'Unit': index,
                        'Start': detail['Start'],
                        'End': detail['End'],
                        'Fault Code': detail['Fault Code'],
                        'Duration': detail['Duration']
                    })
                if self.function == '故障次数':
                    key = str(index) + ' 故障次数'
                    self.result[key] = use_result['Total Faults']
                    print(key + str(self.result[key]))
                else:
                    key = str(index) + ' 停机时间'
                    self.result[key] = str(use_result['Total Duration']) + ' (秒)'
                    print(key + str(self.result[key]))
            result_df = pd.DataFrame(rows)
            result_df.to_csv(('fault_analysis_results.csv'), index=False)
            return fault_analysis
        except Exception as e:
            print(e)
            return False

    def error_statistical(self,_type="故障"):
        """
        分析SCADA系统故障类型
        Args:
            _type:故障、警告
        """
        self.error_type = _type
        result = self.error_analysis()
        for product, info in result.items():
            res = self.type_statistics(info, _type)
            if product +'_'+ _type not in self.result_dict:
                self.result_dict[product +'_'+ _type] = res
            else:
                for key in self.result_dict[product + _type].keys():
                    self.result_dict[product +'_'+ _type][key] = [a + b for a, b in zip(self.result_dict[product +'_'+ _type][key], res[key])]
        self.pie_image(self.result_dict)

    def pie_image(self, data):
        data_list = []
        for product, faults in data.items():
            for category, values in faults.items():
                count, duration = values
                unit, types = product.split('_')
                data_list.append([unit, category, count, duration, types])
        data = pd.DataFrame(data_list, columns=['unit', 'error_type', 'count', 'duration', 'types'])
        wind_error_image(data, 'unit', 'error_type', '风机', '故障次数', '各风机故障类型统计（全部）', '各风机故障类型统计（全部）')
        wind_error_image(data, 'unit', 'error_type', '风机', '故障次数', '各风机故障类型统计（故障）', '各风机故障类型统计（故障）',types='故障')
        wind_error_image(data, 'unit', 'error_type', '风机', '故障次数', '各风机故障类型统计（报警）', '各风机故障类型统计（报警）',types='报警')
        wind_error_image(data, 'error_type', 'types', '故障类型', '故障次数', '故障类型分类统计', '故障类型分类统计')
        wind_error_image(data, 'unit', 'types', '风机', '故障次数', '各风机故障类型分类统计', '各风机故障类型分类统计')
        types = data['error_type'].unique()
        for tp in types:
            plt.figure(figsize=(12, 6))
            use_data = data[data['error_type'] == tp]
            wind_error_image(use_data, 'unit', 'types', '风机', '故障次数', f'各风机{tp}统计', f'各风机{tp}统计')

    def type_statistics(self, info, _type="故障"):
        example = {
            '变流器故障': [0, 0],
            '变桨故障': [0, 0],
            '偏航故障': [0, 0],
            '主控故障': [0, 0],
            '发电机故障': [0, 0],
            '润滑故障': [0, 0],
            '水冷故障': [0, 0],
            '其他故障': [0, 0],
        }
        for fault in info['Fault Details']:
            fault['Fault Code'] = int(re.findall(r'\d+', fault['Fault Code'])[0])
            print(
                f" - Start: {fault['Start']}, End: {fault['End']}, Fault Code: {fault['Fault Code']}, Duration: {fault['Duration']}")
            if _type == "故障":
                if fault['Fault Code'] in range(17, 30 + 1) or fault['Fault Code'] in range(401, 512 + 1) or fault[
                    'Fault Code'] == 660 or fault['Fault Code'] in range(794, 937 + 1):
                    example['变流器故障'][0] += 1
                    example['变流器故障'][1] += fault['Duration'].total_seconds()
                elif fault['Fault Code'] in range(304, 383 + 1) or fault['Fault Code'] in range(387, 399 + 1) or fault[
                    'Fault Code'] in range(514, 519 + 1) or fault['Fault Code'] in range(
                    601, 615 + 1) or fault['Fault Code'] in range(661, 663 + 1) or fault['Fault Code'] in range(701,
                                                                                                                793 + 1):
                    example['变桨故障'][0] += 1
                    example['变桨故障'][1] += fault['Duration'].total_seconds()
                elif fault['Fault Code'] == 210 or fault['Fault Code'] in range(223, 233 + 1) or fault[
                    'Fault Code'] in range(260, 261 + 1) or fault['Fault Code'] in range(290, 292 + 1):
                    example['偏航故障'][0] += 1
                    example['偏航故障'][1] += fault['Duration'].total_seconds()
                elif fault['Fault Code'] == 1 or fault['Fault Code'] == 7 or fault['Fault Code'] in range(9, 14 + 1) or \
                        fault['Fault Code'] in range(30, 47 + 1) or fault['Fault Code'] in range(
                    211, 222 + 1) or fault['Fault Code'] in range(234, 239 + 1) or fault['Fault Code'] in range(293,
                                                                                                                297 + 1):
                    example['主控故障'][0] += 1
                    example['主控故障'][1] += fault['Duration'].total_seconds()
                elif fault['Fault Code'] in range(240, 255 + 1) or fault['Fault Code'] in range(262, 271 + 1):
                    example['发电机故障'][0] += 1
                    example['发电机故障'][1] += fault['Duration'].total_seconds()
                elif fault['Fault Code'] in range(275, 279 + 1) or fault['Fault Code'] in range(384, 386 + 1):
                    example['润滑故障'][0] += 1
                    example['润滑故障'][1] += fault['Duration'].total_seconds()
                elif fault['Fault Code'] in range(100, 111 + 1) or fault['Fault Code'] in range(150, 161 + 1):
                    example['水冷故障'][0] += 1
                    example['水冷故障'][1] += fault['Duration'].total_seconds()
                elif fault['Fault Code'] == 5 or fault['Fault Code'] == 112 or fault['Fault Code'] in range(130,
                                                                                                            131 + 1) or \
                        fault['Fault Code'] == 204 or fault['Fault Code'] in range(256, 258 + 1) or fault[
                    'Fault Code'] in range(
                    272, 274 + 1) or fault['Fault Code'] in range(280, 289 + 1):
                    example['其他故障'][0] += 1
                    example['其他故障'][1] += fault['Duration'].total_seconds()
                else:
                    print("未收录故障？？？")
            else:
                if fault['Fault Code'] in range(240, 255 + 1) or fault['Fault Code'] in range(262, 271 + 1):
                    example['发电机故障'][0] += 1
                    example['发电机故障'][1] += fault['Duration'].total_seconds()
                elif fault['Fault Code'] in range(275, 279 + 1) or fault['Fault Code'] in range(384, 386 + 1):
                    example['润滑故障'][0] += 1
                    example['润滑故障'][1] += fault['Duration'].total_seconds()
        print(example)
        return example