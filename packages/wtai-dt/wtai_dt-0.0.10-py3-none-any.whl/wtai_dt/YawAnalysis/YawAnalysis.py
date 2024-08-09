#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import zipfile
from asyncio import as_completed
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

import wtai_dt.YawAnalysis.Yaw


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
