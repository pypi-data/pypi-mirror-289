
# SCADA故障数据DEMO
import pandas as pd

from ErrorAnalysis.error import SCADAError

# SCADA故障分析具体用法
from GeneratorPerformanceAnalysis.generator_performance_analysis import GeneratorPerformance
from PowerGenerationStatistics.power_generation_statistics import PowerGenerationStatistics
from Report.report import Report
from Utility.save_data_tool import SaveData, get_data
from Utility.utility import Utility
from YawAnalysis.YawAnalysis import YawAnalysis


def ErrorDemo():
    data = pd.read_csv('./SampleData/SampleErrorScada.csv')
    scada_error = SCADAError(data, 'event_unit','event_start_time','event_end_time','event_type','故障次数')
    scada_error.error_analysis()
    scada_error = SCADAError(data, 'event_unit','event_start_time','event_end_time','event_type','停机时间')
    scada_error.error_analysis()
    scada_error.error_statistical('故障')

# SCADA数据发电量统计分析具体用法
def PowerDemo():
    data = pd.read_csv('./SampleData/SampleScada.csv')
    power = PowerGenerationStatistics(data, 'wt_id','tal_ac_pw_gen', 'time', 'daily')
    power.power_analysis()
    power = PowerGenerationStatistics(data, 'wt_id', 'tal_ac_pw_gen', 'time', 'monthly')
    power.power_analysis()
    power = PowerGenerationStatistics(data, 'wt_id', 'tal_ac_pw_gen', 'time', 'all')
    power.power_analysis()

# SCADA数据发电性能分析具体用法
def GeneratorPerformanceDemo():
    data = pd.read_csv('./SampleData/SampleScada.csv')
    generator_performance = GeneratorPerformance(data, 'wind_speed','active_power','风速','功率','风速-功率曲线')
    generator_performance.Plot()
    generator_performance = GeneratorPerformance(data, 'generator_torque', 'wheel_rpm', '转矩', '转速', '转矩-转速曲线')
    generator_performance.Plot()
    generator_performance = GeneratorPerformance(data, 'wheel_rpm', 'blade1_angle', '转速', '桨距角', '转速-桨距角曲线')
    generator_performance.Plot()
    generator_performance = GeneratorPerformance(data, 'wind_speed', 'blade1_angle', '风速', '桨距角', '风速-桨距角曲线')
    generator_performance.Plot()
    generator_performance = GeneratorPerformance(data, 'wind_speed', 'wheel_rpm', '风速', '转速', '风速-转速曲线')
    generator_performance.Plot()
    generator_performance = GeneratorPerformance(data, 'wind_speed', 'wind_speed', '风速', '风速', '风速曲线')
    generator_performance.Plot()

# SCADA秒级数据，偏航分析
def YawAnalysisDemo():
    yaw_analysis = YawAnalysis('./SampleData/SecondData',trubine_field = '风机ID',hydraulic_pressure = '液压制动压力',angle_of_wind = '风向绝对值',
                               fan_status = '风机当前状态值',yaw_require = '偏航要求值',yaw_times = '总偏航次数',build_pressure_speed = None, angle = None)
    yaw_analysis.analysis()
    result = yaw_analysis.get_result()
    print(result)

def ReportDemo():
    report = Report('./SampleData/封面.docx')
    world = report.create_new_document()
    small_title_table_content = []
    analysis_type = {
        '发电机性能分析': ['风速-功率曲线', '转矩-转速曲线', '转速-桨距角曲线', '风速-转速曲线', '风速-桨距角曲线', '平均风速', '年平均风速', '理论电量', '实际电量']}
    functionality = "机组总体分析"
    feature_branch = "发电机性能分析"
    big_title = 1
    report.insert_title(world, str(big_title) + "、 " + "机组发电性能分析")
    small_title = 1
    flag = 0
    data = pd.DataFrame()
    _content = None
    table_flag = False
    utility = Utility()
    if '数据开始时间' not in data.columns and '数据结束时间' not in data.columns:
        data['数据开始时间'] = None
        data['数据结束时间'] = None
    for i in analysis_type['发电机性能分析']:
        save_type = SaveData(functionality, feature_branch, i)
        save_type = get_data(save_type, get_data_type="all", file_path='./SampleData/data.json')
        if not save_type:
            continue
        if i == '平均风速' or i == '年平均风速' or i == '理论电量' or i == '实际电量':
            flag += 1
            if flag == 1:
                report.insert_lettle_title_word(world,
                                                 str(big_title) + '.' + str(small_title) + "、 各风机风速和电量分析结果")
                small_title_table_content.append(str(big_title) + '.' + str(small_title) + "、 各风机风速和电量分析结果")
        else:
            report.insert_lettle_title_word(world,
                                             str(big_title) + '.' + str(small_title) + "、 各风机" + i + "分析结果")
            small_title_table_content.append(str(big_title) + '.' + str(small_title) + "、 各风机" + i + "分析结果")
        small_title += 1
        name = []
        path = []
        report_content = ''
        for id, content in save_type.items():
            if content['type'] == 'image':
                name.append(id)
                path.append(utility.resource_path(content['data'][0]).replace('\\', '/').replace('./', ''))
                report_content = report_content + content['content']
            elif content['type'] == 'table':
                table_flag = True
                if id not in data.index:
                    data.loc[id] = 0
                if i == '理论电量':
                    data.loc[id, i] = str(int(float(content['data'])))
                else:
                    data.loc[id, i] = str(content['data'])
                data.loc[id, '数据开始时间'] = content['start_time']
                data.loc[id, '数据结束时间'] = content['end_time']
                _content = content['content']
        if name:
            report.insert_image_table(world, path, name)
            report.insert_paragraph(world, report_content)
    if table_flag:
        target_columns = ['数据开始时间', '数据结束时间']
        moved_columns = [data.pop(col) for col in target_columns]
        for col in moved_columns:
            data[col.name] = col
        data.index.name = '风机'
        data_reset = data.reset_index()
        columns_list = data_reset.columns.tolist()
        columns_list = report.change_colums_value('平均风速', '平均风速(m/s)', columns_list)
        columns_list = report.change_colums_value('年平均风速', '年平均风速(m/s)', columns_list)
        columns_list = report.change_colums_value('理论电量', '理论电量(kw·h)', columns_list)
        columns_list = report.change_colums_value('实际电量', '实际电量(kw·h)', columns_list)
        values_list = data_reset.values.tolist()
        final_list = [columns_list] + [[str(val) for val in row] for row in values_list]
        final_list = utility.process_data(final_list)
        report.insert_table_word(world, final_list)
    print("机组发电性能分析报告生成成功")
    report.save(world, '报告.docx')
    # self.table_content[str(self.big_title) + "、 " + "机组发电性能分析"] = small_title_table_content
    # self.big_title += 1

if __name__ == '__main__':
    ErrorDemo()
    # PowerDemo()
    # GeneratorPerformanceDemo()
    # YawAnalysisDemo()
    # ReportDemo()