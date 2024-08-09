#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import zipfile
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

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



class YawAnalysis:
    def __init__(self,directory_path, trubine_field,hydraulic_pressure = None,angle_of_wind=None,fan_status=None,
                 yaw_require=None,yaw_times=None,build_pressure_speed=None,angle=None):
        """
            初始化偏航分析实例。
            :param directory_path: 数据文件的目录路径
            :param trubine_field: 风力发电机的字段名
            :param hydraulic_pressure: 液压压力，默认为None
            :param angle_of_wind: 风向角度，默认为None
            :param fan_status: 风机当前状态值，默认为None
            :param yaw_require: 偏航要求值，默认为None
            :param yaw_times: 偏航次数，默认为None
            :param build_pressure_speed: 建压速度，默认为None
            :param angle: 偏航角度，默认为None

            通过多线程分析路径下文件的偏航数据
        """
        self.directory_path = directory_path
        self.hydraulic_pressure = hydraulic_pressure
        self.angle_of_wind = angle_of_wind
        self.fan_status = fan_status
        self.yaw_require = yaw_require
        self.yaw_times = yaw_times
        self.build_pressure_speed = build_pressure_speed
        self.angle = angle
        self.trubine_field = trubine_field
        self.use_field = []
        if self.hydraulic_pressure is not None:
            self.use_field.append(hydraulic_pressure)
        if self.angle_of_wind is not None:
            self.use_field.append(angle_of_wind)
        if self.fan_status is not None:
            self.use_field.append(fan_status)
        if self.yaw_require is not None:
            self.use_field.append(yaw_require)
        if self.yaw_times is not None:
            self.use_field.append(yaw_times)
        if self.build_pressure_speed is not None:
            self.use_field.append(build_pressure_speed)
        if self.angle is not None:
            self.use_field.append(angle)
        if self.trubine_field is not None:
            self.use_field.append(trubine_field)

        self.Yaw = Yaw()

    def process_csv_datas(self, data,file_path):
        for i, d in data:
            if self.hydraulic_pressure:
                self.Yaw.maximum_hydraulic_pressure_average_value(d[self.hydraulic_pressure],i)
                self.Yaw.maximum_hydraulic_pressure(d[self.hydraulic_pressure],i)
            if self.angle_of_wind:
                self.Yaw.total_angle_of_wind_direction_change(d[self.angle_of_wind],i)
            if self.fan_status and self.yaw_require:
                self.Yaw.total_number_yawing_in_power_generation_state(d,self.fan_status,self.yaw_require,i)
                self.Yaw.maximum_yawing_time_in_power_generation_state(d,self.fan_status,self.yaw_require,i)
                self.Yaw.total_yaw_time_hours(d,self.fan_status,self.yaw_require,i)
            if self.yaw_times:
                self.Yaw.total_yaw_times(d[self.yaw_times], i)
            if self.build_pressure_speed:
                self.Yaw.maximum_build_pressure_speed(d[self.build_pressure_speed],i)
            if self.fan_status and self.yaw_require and self.angle:
                self.Yaw.maximum_slippage_angle_in_power_generation_state(d, self.fan_status, self.yaw_require, self.angle,i)
                self.Yaw.maximum_slippage_angle_in_non_power_generation_state(d, self.fan_status, self.yaw_require, self.angle,i)
            if self.yaw_require and self.angle:
                self.Yaw.total_angle_of_slippage_when_not_yawing(d,self.yaw_require,self.angle, i)

    def process_csv_data(self,file, name):
        encodings = ['gbk', 'utf-8', 'latin1']
        for encoding in encodings:
            try:
                data = pd.read_csv(io.StringIO(file.decode(encoding)), usecols=self.use_field,index_col=False)
                data = data.dropna()
                data = data.groupby(self.trubine_field)
                self.process_csv_datas(data,name)
                return
            except UnicodeDecodeError as e:
                print(f"Error processing file {name} with {encoding}: {e}")
            except Exception as e:
                print(f"Unexpected error processing file {name}: {e}")
                return
        print(f"All encodings failed for file {name}. Consider checking file encoding.")

    def extract_and_process_zip(self,zip_path, executor):
        try:
            with zipfile.ZipFile(zip_path, 'r') as z:
                for entry in z.infolist():
                    filename = entry.filename.encode('cp437').decode('gbk')
                    print("Processing entry with name:", filename)
                    if entry.filename.endswith('.zip'):
                        inner_zip_path = os.path.join('/tmp', os.path.basename(entry.filename))
                        with z.open(entry) as inner_file:
                            with open(inner_zip_path, 'wb') as f:
                                f.write(inner_file.read())
                        executor.submit(self.extract_and_process_zip, inner_zip_path, executor)
                    elif entry.filename.endswith('.csv'):
                        with z.open(entry) as file:
                            file_content = file.read()
                            self.process_csv_data(file_content, file.name)
        except zipfile.BadZipFile:
            print(f"Cannot open ZIP file as it is either a bad zip file or corrupted: {zip_path}")
        except Exception as e:
            print(f"General Error handling ZIP file {zip_path}: {e}")

    # 偏航分析入口程序
    def analysis(self):
        with ThreadPoolExecutor(max_workers=32) as executor:
            futures = []
            for root, dirs, files in os.walk(self.directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path.endswith('.zip'):
                        futures.append(executor.submit(self.extract_and_process_zip, file_path, executor))
                    elif file_path.endswith('.csv'):
                        with open(file_path, 'rb') as f:
                            file_content = f.read()
                            self.process_csv_data(file_content, file_path)
            for future in as_completed(futures):
                print("Completed processing for a future.")

    def get_result(self):
        return self.Yaw.get_result()
