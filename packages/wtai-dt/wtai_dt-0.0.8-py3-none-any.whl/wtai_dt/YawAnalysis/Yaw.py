#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional, Dict
import pandas as pd

class Yaw:
    def __init__(self):
        self.result_dict: Dict[str, float] = {}

    def get_result(self) -> Dict[str, float]:
        return self.result_dict

    def maximum_hydraulic_pressure_average_value(
            self, data: Optional[pd.Series], id: Optional[str]
    ) -> None:
        """
            计算最大液压压力平均值
            参数:
            data (pd.Series): 液压压力数据
            id (str, optional): 当前计算风机ID

            计算一组数据中,最大液压压力的平均值
        """
        t = data.mean().item()
        t = round(t, 3)
        if f"{id} 最大液压压力平均值(Pa)" not in self.result_dict:
            self.result_dict[f"{id} 最大液压压力平均值(Pa)"] = t
        else:
            self.result_dict[f"{id} 最大液压压力平均值(Pa)"] = round((t + self.result_dict[
                f"{id} 最大液压压力平均值(Pa)"]) / 2.0, 3)

    def maximum_hydraulic_pressure(
            self, data: Optional[pd.Series], id: Optional[str]
    ) -> None:
        """
            计算最大液压压力
            参数:
            data (pd.Series): 液压压力数据
            id (str, optional): 当前计算风机ID

            计算风电机组最大液压压力
        """
        t = data.max().item()
        if f"{id} 最大液压压力(Pa)" not in self.result_dict:
            self.result_dict[f"{id} 最大液压压力(Pa)"] = t
        else:
            self.result_dict[f"{id} 最大液压压力(Pa)"] = t if t > self.result_dict[f"{id} 最大液压压力(Pa)"] else self.result_dict[
                f"{id} 最大液压压力(Pa)"]

    def total_angle_of_wind_direction_change(
            self, data: Optional[pd.Series] , id: Optional[str]
    ) -> None:
        """
            计算风机风向变化总角度
            参数:
            data (pd.Series): 风向角度数据
            id (str, optional): 计算风机ID
        """
        t = data.dropna().diff().abs().sum().item()
        if f"{id} 风向变化总角度(°)" not in self.result_dict:
            self.result_dict[f"{id} 风向变化总角度(°)"] = t
        else:
            self.result_dict[f"{id} 风向变化总角度(°)"] += t

    def total_number_yawing_in_power_generation_state(
            self, data: Optional[pd.DataFrame], field1: Optional[str], field2: Optional[str] , id: Optional[str] = None
    ) -> None:
        """
            发电状态下,偏航总次数

            参数:
            data (pd.DataFrame): 风机数据.
            field1 (str): 风机状态值.
            field2 (str): 偏航要求值.
            id (str, optional): 计算风机ID.

            计算风机状态值为6且偏航要求值置1或2的次数之和.
        """
        condition_field1 = (data[field1] == 6)
        field2_series = data[field2][condition_field1]
        is_zero = field2_series == 0
        shifted_is_zero = is_zero.shift(1).fillna(True)
        change_to_non_zero = field2_series.isin([1, 2]) & shifted_is_zero
        total_count = change_to_non_zero.sum()
        key = f"{id} 发电状态偏航总次数"
        self.result_dict[key] = self.result_dict.get(key, 0) + total_count

    def maximum_yawing_time_in_power_generation_state(
            self, data: Optional[pd.DataFrame], field1: Optional[str], field2: Optional[str] , id: Optional[str] = None
    ) -> None:
        """
            风机发电状态最大偏航时长
            参数:
            data (pd.DataFrame): 风机数据.
            field1 (str): 风机状态值.
            field2 (str): 偏航要求值.
            id (str, optional): 计算风机ID.

            风机状态值为6，偏航要求值为1或2，单次偏航最大时间.对于一组数据,单次偏航时间为风机状态值为6，偏航要求值为1或2连续的数据量
        """
        mask = (data[field1] == 6) & (
                (data[field2] == 1) | (data[field2] == 2))
        groups = (mask != mask.shift()).cumsum()
        durations = data[mask].groupby(groups).size()
        max_duration = durations.max() if not durations.empty else 0
        key = f"{id} 发电状态最大偏航时长(秒)"
        self.result_dict[key] = max(self.result_dict.get(key, 0), max_duration)
        mask = data[data[field1] == 6]
        if f"{id} 有效数据量" not in self.result_dict:
            self.result_dict[f"{id} 有效数据量"] = len(mask)
        else:
            self.result_dict[f"{id} 有效数据量"] += len(mask)

    def total_yaw_times(
            self, data: Optional[pd.Series] , id: Optional[str]
    ) -> None:
        """
            总偏航次数
            参数:
            data (pd.Series): 风机数据.
            id (str, optional): 计算风机ID.

            风机总偏航次数
        """
        t = round((data.iloc[-1] - data.iloc[0]).item(), 0)
        if f"{id} 总偏航次数" not in self.result_dict:
            self.result_dict[f"{id} 总偏航次数"] = t
        else:
            self.result_dict[f"{id} 总偏航次数"] += t

    # 总偏航时间
    def total_yaw_time_hours(
            self, data: Optional[pd.DataFrame], field1: Optional[str], field2: Optional[str] , id: Optional[str] = None
    ) -> None:
        """
            风机总偏航时间
            参数:
            data (pd.DataFrame): 风机数据.
            field1 (str): 风机状态值.
            field2 (str): 偏航要求值.
            id (str, optional): 计算风机ID.

            风机状态值为6，偏航要求值为1或2，单次偏航最大时间.对于一组数据,单次偏航时间为风机状态值为6，偏航要求值为1或2连续的数据量
        """
        filtered_data = data[(data[field1] == 6) & (
                (data[field2] == 1) | (data[field2] == 2))]
        sum_time = round(1.0 * len(filtered_data) / 3600, 3)
        if f"{id} 总偏航时间(小时)" not in self.result_dict:
            self.result_dict[f"{id} 总偏航时间(小时)"] = round(sum_time, 3)
        else:
            self.result_dict[f"{id} 总偏航时间(小时)"] += round(sum_time, 3)

    # 最大建压速度
    def maximum_build_pressure_speed(
            self, data: Optional[pd.Series] , id: Optional[str]
    ) -> None:
        """
            最大建压速度
            参数:
            data (pd.Series): 风机建压速度数据.
            id (str, optional): 计算风机ID.
        """
        t = data.max().item()
        if f"{id} 最大建压速度" not in self.result_dict:
            self.result_dict[f"{id} 最大建压速度"] = t
        else:
            self.result_dict[f"{id} 最大建压速度"] = t if t > self.result_dict[
                f"{id} 最大建压速度"] else self.result_dict[f"{id} 最大建压速度"]

    def maximum_slippage_angle_in_power_generation_state(
            self, data: Optional[pd.DataFrame], field1: Optional[str], field2: Optional[str], field3: Optional[str], id: Optional[str] = None
    ) -> None:
        """
            发电状态下滑移角度最大值
            参数:
            data (pd.DataFrame): 风机数据.
            field1 (str): 风机状态值.
            field2 (str): 偏航要求值.
            field3 (str): 偏航角度.
            id (str, optional): 计算风机ID.

            风机状态值为6，偏航要求值为0，偏航角度大于0.013*360的偏航角度最大值
        """
        data = data.dropna()
        filtered_data = data[
            (data[field1] == 6) &
            (data[field2] == 0)
        ]
        angle_field = field3
        filtered_data = filtered_data[filtered_data[angle_field].diff().abs() > 0.013]
        angle = filtered_data[angle_field].diff().abs() * 360
        if angle.empty:
            return
        else:
            t = round(angle.max().item(), 3)
            if f"{id} 发电状态下的滑移角度最大值(°)" not in self.result_dict:
                self.result_dict[f"{id} 发电状态下的滑移角度最大值(°)"] = t
            else:
                self.result_dict[f"{id} 发电状态下的滑移角度最大值(°)"] = t if t > self.result_dict[
                    f"{id} 发电状态下的滑移角度最大值(°)"] else self.result_dict[f"{id} 发电状态下的滑移角度最大值(°)"]

    def maximum_slippage_angle_in_non_power_generation_state(
            self, data: Optional[pd.DataFrame], field1: Optional[str], field2: Optional[str], field3: Optional[str], id: Optional[str] = None
    ) -> None:
        """
            非发电状态下的滑移角度最大值
            参数:
            data (pd.DataFrame): 风机数据.
            field1 (str): 风机状态值.
            field2 (str): 偏航要求值.
            field3 (str): 偏航角度.
            id (str, optional): 计算风机ID.

            风机状态值不为6，偏航要求值为0，偏航角度大于0.013*360的偏航角度最大值
        """
        data = data.dropna()
        filtered_data = data[
            (data[field1] != 6) &
            (data[field2] == 0)
            ]
        # 0.013
        angle_field = field3
        filtered_data = filtered_data[filtered_data[angle_field].diff().abs() > 0.013]
        angle = filtered_data[angle_field].diff().abs() * 360
        if angle.empty:
            return  # 如果 angle 为空，则返回 None 或其他适当的值
        else:
            t = int(angle.max().item())
            if f"{id} 非发电状态下的滑移角度最大值(°)" not in self.result_dict:
                self.result_dict[f"{id} 非发电状态下的滑移角度最大值(°)"] = t
            else:
                self.result_dict[f"{id} 非发电状态下的滑移角度最大值(°)"] = t if t > self.result_dict[
                    f"{id} 非发电状态下的滑移角度最大值(°)"] else self.result_dict[f"{id} 非发电状态下的滑移角度最大值(°)"]

    def total_angle_of_slippage_when_not_yawing(
            self, data: Optional[pd.DataFrame], field1: Optional[str], field2: Optional[str], id: Optional[str] = None
    ) -> None:
        """
            未偏航时滑移总角度
            参数:
            data (pd.DataFrame): 风机数据.
            field1 (str): 偏航要求值.
            field2 (str): 偏航角度.
            id (str, optional): 计算风机ID.

            偏航要求值为0，偏航角度大于0.013*360的偏航角度累加
        """
        filtered_data = data[(data[field1] == 0)]
        angle_field = field2
        filtered_data = filtered_data[filtered_data[angle_field].diff().abs() > 0.013]
        twisted_cable_change = filtered_data[field2].diff().abs().sum()
        total_sum = twisted_cable_change * 360
        total_sum = round(total_sum, 0)
        key = f"{id} 未偏航时滑移总角度(°)"
        self.result_dict[key] = self.result_dict.get(key, 0) + total_sum
