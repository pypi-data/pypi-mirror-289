import pandas as pd
import os, platform, subprocess, yaml
import streamlit as st
import pkg_resources

PYTHON_SHEET_NAME = 'Python 仿真'
C_SHEET_NAME = 'C语言仿真'

TEMPLATE_CONTENT_FRONT = '''// This header file is automatically generated. Any modification to this file will get lost.\n#ifndef ACMParam_H\n#define ACMParam_H\n\n'''
TEMPLATE_CONTENT_END = '''\n#endif // ACMParam_H\n'''

class ACMParam:
    '''
    Usage:
    acm = ACMParam('path2acmsimc', 'path2xlsx')
    acm.readXlsx()
    acm.readDict({'电机参数1': 1, '电机参数2': 2})
    acm.updateACMParam()
    '''
    def __init__(self, path2acmsimc, path2xlsx):
        self.path2acmsimc = path2acmsimc
        self.path2xlsx = path2xlsx
        self.c_macros = [] # 宏的名字列表（参数的c名字）
        self.python_variables = []
        self.pvalue = {}
        self.template_content_front = TEMPLATE_CONTENT_FRONT
        self.template_content_main = ""
        self.template_content_end = TEMPLATE_CONTENT_END
        # 初始化宏列表清单
        self.readXlsx()

    def readXlsx(self):
        self.template_content_main = ""
        df = pd.read_excel(open(self.path2xlsx, 'rb'), sheet_name='Sheet1')
        for index, item in enumerate(df[C_SHEET_NAME]):
            if type(item) == float:
                print(f'[Warning] {C_SHEET_NAME} {index} {df[C_SHEET_NAME][index]} is empty.')
                continue
            # 初始化 c 语言的宏
            self.c_macros.append(item)
            self.python_variables.append(df[PYTHON_SHEET_NAME][index])

    def readDict(self, d):
        for index, item in enumerate(self.c_macros):
            if self.python_variables[index] in d:
                self.pvalue[item] = d[self.python_variables[index]]
            else:
                print(f'[Warning] {self.python_variables[index]} no value in dict.')

    def load_signal_library(self):
        with open(os.path.dirname(__file__)+'/signal_library.yaml', encoding='utf-8') as f:
            data_details = yaml.load(f, Loader=yaml.FullLoader)
        return data_details['signal_variables']

    def updateACMParamAndRun(self):
        filename = self.path2acmsimc  # 'ACMParam.h'
        print(f'Generate {filename} \n')
        self.template_content_main = ""

        # 实现确定有这些宏了，填入宏的值进去。
        # for index, item in enumerate(self.c_macros):
        #     print(index, item)
        #     if type(self.pvalue[item]) == bool:
        #         self.template_content_main += f'#define {item} {str(self.pvalue[item]).upper()}\n'
        #     elif type(self.pvalue[item]) == float:
        #         self.template_content_main += f'#define {item} ({self.pvalue[item]})\n'
        #     else:
        #         self.template_content_main += f'#define {item} {self.pvalue[item]}\n'

        # 直接把 d_user_input_motor_dict 转为宏
        def convert_json_to_macros(d):
            for index, (key, val) in enumerate(d.items()):
                if key.upper() == 'NAME':
                    continue
                key = key.replace('.', '_')
                # print(index, key)
                if val == True:
                    val = 'TRUE'
                elif val == False:
                    val = 'FALSE'
                self.template_content_main += f'#define {key.upper()} {val}\n'
        convert_json_to_macros(st.session_state.d_user_input_motor_dict)
        # st.write(st.session_state.user_selected_motor)

        # DATA_FORMAT
        data_details = self.load_signal_library()
        data_format_str = "\n\n\n#define DATA_FORMAT \""
        data_labels_str = "#define DATA_LABELS \""
        data_details_str = "#define DATA_DETAILS "
        for data_detail in data_details:
            data_format_str += "%g,"
            data_labels_str += str(data_detail)+","
            data_details_str += str(data_detail)+","
        data_format_str = data_format_str[:-1] + "\\n\"\n"
        data_labels_str = data_labels_str[:-1] + "\\n\"\n"
        data_details_str = data_details_str[:-1] + "\n\n\n"
        data_unite =  data_format_str + data_labels_str + data_details_str
        
        data_file_name = "#define DATA_FILE_NAME \"../dat/" + str(st.session_state.user_selected_motor) + ".dat\"\n"
        config_content = self.template_content_front + self.template_content_main + data_unite + data_file_name + self.template_content_end
        # print(config_content)
        with open(filename, 'w') as file:
            file.write(config_content)

        # 获取当前文件的目录
        current_dir = os.path.dirname(__file__)
        # 构造目标目录
        target_dir = os.path.join(current_dir, 'acmsimcv5', 'c')
        origin_dir = os.getcwd()
        # 检测操作系统类型
        system_type = platform.system()
        os.chdir(target_dir)
        try:
            if system_type == 'Windows':
                # path_to_gmake_exe = pkg_resources.resource_filename(__name__, './acmsimcv5/c/gmake.exe')
                # path_to_makefile = pkg_resources.resource_filename(__name__, './acmsimcv5/c/makefile')
                # path_to_main_exe = pkg_resources.resource_filename(__name__, './acmsimcv5/c/main.exe')
                # target_dir = target_dir.replace('/', '\\')
                # subprocess.run(path_to_gmake_exe + ' ' + path_to_makefile, shell=True, check=True)
                subprocess.run('gmake', shell=True, check=True)
                subprocess.run('main', shell=True, check=True)

            else:
                subprocess.run('make clean', shell=True, check=True)
                subprocess.run('make', shell=True, check=True)
                subprocess.run('./main', shell=True, check=True)
        except Exception as e:
            print(e)
        finally:
            os.chdir(origin_dir)

if __name__ == "__main__":
    d = {
        "CL_TS": 0.0001,
        "VL_EXE_PER_CL_EXE": 5,
        "MACHINE_SIMULATIONs_PER_SAMPLING_PERIOD": 1,
        "TIME_SLICE": 0.2,
        "NUMBER_OF_SLICES": 6,
        "init_npp": 2,
        "init_IN": 4.6,
        "init_R": 5.5,
        "init_Ld": 0.5800000000000001,
        "init_Lq": 0.022,
        "init_KE": 1.3593784874408605,
        "init_KA": 1.3593784874408605,
        "init_Rreq": 2.1,
        "init_Js": 0.063,
        "DC_BUS_VOLTAGE": 600,
        "user_system_input_code": "if ii < 1: (*CTRL).cmd_idq[0] = 0.0; (*CTRL).cmd_rpm = 50 \nelif ii <5: ACM.TLoad = 0.2 \nelif ii <100: (*CTRL).cmd_rpm = -50",
        "(*CTRL).bool_apply_speed_closed_loop_control": True,
        "(*CTRL).bool_apply_decoupling_voltages_to_current_regulation": False,
        "(*CTRL).bool_apply_sweeping_frequency_excitation": False,
        "(*CTRL).bool_overwrite_speed_commands": True,
        "(*CTRL).bool_zero_id_control": True,
        "FOC_delta": 15,
        "FOC_CLBW_HZ": 400,
        "FOC_desired_VLBW_HZ": 120,
        "FOC_CL_KI_factor_when__bool_apply_decoupling_voltages_to_current_regulation__is_False": 10,
        "CL_SERIES_KP": 55.29203070318036,
        "CL_SERIES_KI": 250.00000000000003,
        "VL_SERIES_KP": 1.2941884120310692,
        "VL_SERIES_KI": 11.170107212763709,
        "VL_LIMIT_OVERLOAD_FACTOR": 3.0,
        "disp.Kp": 0.0,
        "disp.Ki": 0.0,
        "disp.Kd": 0.0,
        "disp.tau": 0.0,
        "disp.OutLimit": 0.0,
        "disp.IntLimit": 0.0
    }

    path2acmsimc = f'{os.path.dirname(__file__)}/acmsimcv5/c/ACMParam.h'
    path2xlsx = f'{os.path.dirname(__file__)}/jsons/ACMParam.xlsx'
    acm = ACMParam(path2acmsimc, path2xlsx)

    # acm = ACMParam('./', './jsons/ACMParam.xlsx')
    acm.readDict(d)
    acm.updateACMParamAndRun()
    print(acm.template_content_front)
    print(acm.template_content_main)
    print(acm.template_content_end)
