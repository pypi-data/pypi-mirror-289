import streamlit as st
import os
import json
import builtins
import datetime
import collections
import pkg_resources
import base64
import copy
import yaml
import pandas as pd
import numpy as np
from pylab import np, plt, mpl, fft
import pickle
import tuner
import control
import psutil
import math
import tools.tutorials_ep61_remove_numba as acmsimpy
# from pprint import pprint as print
from rich import print


VAR_LIST = ['TIME_SLICE', 'NUMBER_OF_SLICES', 'VL_EXE_PER_CL_EXE',
            'CTRL.bool_apply_decoupling_voltages_to_current_regulation',
            'FOC_CL_KI_factor_when__bool_apply_decoupling_voltages_to_current_regulation__is_False',
            'CTRL.bool_zero_id_control',
            'CTRL.bool_apply_sweeping_frequency_excitation',
            'CTRL.bool_sweeping_frequency_for_speed_loop',
            'CTRL.CMD_SPEED_SINE_RPM', 'CTRL.CMD_CURRENT_SINE_AMPERE',
            'CTRL.bool_apply_WC_tunner_for_speed_loop',
            'zeta', 'omega_n', 'max_CLBW_PER_min_CLBW',
            'FOC_delta', 'FOC_CLBW_HZ', 'FOC_desired_VLBW_HZ',
            'DC_BUS_VOLTAGE', 'init_IN']
VAR_LIST_SWEEP = ['zeta', 'omega_n', 'max_CLBW_PER_min_CLBW',
                  'CL_SERIES_KP_Q', 'CL_SERIES_KI_Q', 'CL_SERIES_KP_D', 'CL_SERIES_KI_D',
                  'VL_FEEDBACK_KFB', 'VL_SERIES_KP', 'VL_SERIES_KI',
                  'init_Js', 'init_Ld', 'init_Lq']

def user_selected_mode():
    with st.sidebar:
        st.title('✨使用Python或C仿真:')
        user_selected_mode = st.selectbox('user_selected_mode', ['C', 'Python'], key='user_selected_mode', label_visibility='collapsed')
    return user_selected_mode

def get_user_history():
    history = {}
    fname_session_state = f'{os.path.dirname(__file__)}/../jsons/streamllit_user_session_data.json'
    if not os.path.exists(fname_session_state):
        with open(fname_session_state, 'w') as f:
            f.write('{\n}')
    with open(fname_session_state, 'r') as f:
        d = json.load(f)
        for k, v in d.items():
            history[k] = v
    return history

def init_motor_lib():
    # https://stackoverflow.com/questions/10844064/items-in-json-object-are-out-of-order-using-json-dumps/23820416
    filepath_to_machineSpecs = pkg_resources.resource_filename(
        __name__, f'../jsons/machine_specification-auto.json')
    with open(filepath_to_machineSpecs, 'r', encoding='utf-8') as f:
        d_motors = json.load(f, object_pairs_hook=collections.OrderedDict)
    return d_motors

def init_user_selected_motor(history):
    if "user_selected_motor" not in st.session_state:
        if "user_selected_motor" not in history:
            st.session_state.user_selected_motor = 'F130-16-KV20'
        else:
            st.session_state.user_selected_motor = history["user_selected_motor"]

def option_select_motor(history, user_plot_config):

    # init_user_selected_motor(history)

    d_motors = init_motor_lib()
    motor_name_list = list(d_motors.keys()) + ['my-yaml-custom-motor']

    with st.sidebar:
        st.header('🔌电机选择:')
        user_selected_motor = st.selectbox(
            '从下拉列表选择一台电机：',
            motor_name_list,
            key='user_selected_motor',
        )

        user_motor = dict()
        if user_selected_motor == 'my-yaml-custom-motor':
            # print('history')
            # print(history, end='\n\n')
            st.write(f"开发者模式：直接根据现有的 user_plot_config.yaml 文件中的电机数据进行仿真，源自：{history['user_selected_motor']}")
            user_motor['motor'] = d_motors[history['user_selected_motor']]['基本参数']
        else:
            history['user_selected_motor'] = user_selected_motor
            user_motor['motor'] = d_motors[user_selected_motor]['基本参数']

        # 电机参数名字翻译
        user_motor['motor_simulated'] = {# Motor data
            'init_npp' :      user_motor['motor']['极对数 [1]'],
            'init_IN'  :      user_motor['motor']['额定电流 [Arms]'],
            'init_R'   :      user_motor['motor']['定子电阻 [Ohm]'],
            'init_Ld'  : 1e-3*user_motor['motor']['定子D轴电感 [mH]'],
            'init_Lq'  : 1e-3*user_motor['motor']['定子Q轴电感 [mH]'],
            'init_KE'  :      user_motor['motor']['额定反电势系数 [Wb]'], # 对于感应电机来说这个是磁力产生的KE
            'init_KA'  :      user_motor['motor']['额定反电势系数 [Wb]'],
            'init_Rreq': 0.0 if np.isnan(user_motor['motor']['反伽马转子电阻 [Ohm]']) else user_motor['motor']['反伽马转子电阻 [Ohm]'],
            'init_Js'  : 1e-4*user_motor['motor']['转动惯量 [kg.cm^2]'],
            'DC_BUS_VOLTAGE': user_motor['motor']['母线电压 [Vdc]'],
        }

        # 保存到 或者 读取自 streamlit session
        if st.session_state.user_selected_motor in history and 'd_user_input_motor_dict' in history[st.session_state.user_selected_motor]:
            print('Loading history d_user...')
            st.session_state.d_user_input_motor_dict = history[st.session_state.user_selected_motor]['d_user_input_motor_dict']
        else:
            # 电机参数传递
            st.session_state.d_user_input_motor_dict = copy.deepcopy(user_motor['motor_simulated'])
            # 仿真参数传递
            st.session_state.d_user_input_motor_dict.update(user_plot_config['simulation'])

        VLBW_Hz, d_currentKp, d_currentKi, q_currentKp, q_currentKi, speedKp, speedKi, speedKFB, (mag, phase, omega), input, output = tuner.InstaSPIN_series_PI_tuner(
            user_plot_config['simulation']['FOC_delta'],
            user_plot_config['simulation']['FOC_CLBW_HZ'],
            user_motor['motor_simulated']['init_Ld'],
            user_motor['motor_simulated']['init_Lq'],
            user_motor['motor_simulated']['init_R'],
            user_motor['motor_simulated']['init_Js'],
            user_motor['motor_simulated']['init_npp'],
            user_motor['motor_simulated']['init_KE'], bool_render=False)
        user_motor['motor_simulated']['CL_SERIES_KP_Q'] = st.session_state.d_user_input_motor_dict['CL_SERIES_KP_Q'] = q_currentKp
        user_motor['motor_simulated']['CL_SERIES_KI_Q'] = st.session_state.d_user_input_motor_dict['CL_SERIES_KI_Q'] = q_currentKi
        user_motor['motor_simulated']['VL_SERIES_KP']   = st.session_state.d_user_input_motor_dict['VL_SERIES_KP'] = speedKp
        user_motor['motor_simulated']['VL_SERIES_KI']   = st.session_state.d_user_input_motor_dict['VL_SERIES_KI'] = speedKi
        # 吴波用
        user_motor['motor_simulated']['CL_SERIES_KP_D'] = st.session_state.d_user_input_motor_dict['CL_SERIES_KP_D'] = d_currentKp
        user_motor['motor_simulated']['CL_SERIES_KI_D'] = st.session_state.d_user_input_motor_dict['CL_SERIES_KI_D'] = d_currentKi

        # 保存到 streamlit session
        # st.session_state.user_motor = user_motor

        with open('user_motor.yaml', 'w', encoding='utf-8') as yamlfile:
            # print(user_motor)
            yaml.dump(user_motor, yamlfile, default_flow_style=False, sort_keys=False, allow_unicode=True)

        df_basic_para_xlsx   = pd.DataFrame.from_dict(user_motor['motor'], orient='index')
        df_basic_para_python = pd.DataFrame.from_dict(user_motor['motor_simulated'], orient='index')

        # 更新侧边栏表格
        with st.expander(user_selected_motor + ' 的电机参数如下'):
            st.data_editor(df_basic_para_xlsx, disabled=True, use_container_width=True)
            st.data_editor(df_basic_para_python, disabled=True, use_container_width=True)

    return st.session_state.d_user_input_motor_dict, d_motors, user_selected_motor, user_motor

def example_plot(gdd, global_machine_times, save=True):
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    plt.style.use('bmh')
    mpl.rc('font', family='Times New Roman', size=10.0)
    # mpl.rc('legend', fontsize=10)
    # mpl.rc('lines', linewidth=4, linestyle='-.')
    mpl.rcParams['lines.linewidth'] = 0.75
    mpl.rcParams['mathtext.fontset'] = 'stix'

    with open(os.path.dirname(__file__)+'/../user_plot_config.yaml', encoding='utf-8') as f:
        user_plot_config = yaml.load(f, Loader=yaml.FullLoader)

    fig, axes = plt.subplots(nrows=len(user_plot_config['pyplot']['subplot']),
                            ncols=1, dpi=300, facecolor='w',
                            figsize=(
                                user_plot_config['pyplot']['width'],
                                user_plot_config['pyplot']['height'] *
                                len(user_plot_config['pyplot']['subplot'])),
                            sharex=True
                            )

    for subplot_config in user_plot_config['pyplot']['subplot']:
        ax = axes[user_plot_config['pyplot']['subplot'].index(subplot_config)]
        for subplot_signal_index in range(len(subplot_config['y'])):
            signal = gdd[subplot_config['y'][subplot_signal_index]['y_data']]
            label = subplot_config['y'][subplot_signal_index]['y_label']
            ax.plot(global_machine_times, signal, label=label)
        ax.set_ylabel(subplot_config['y_title'])
        ax.legend(loc=1)
        ax.grid(True)
    ax.set_xlabel(user_plot_config['pyplot']['x_label'])
    
    # Save data
    if save:
        if not os.path.exists(os.path.dirname(__file__)+"/../data/python"):
            os.mkdir(os.path.dirname(__file__)+"/../data/python")
        with open(os.path.dirname(__file__)+"/../data/python/global_machine_times.pkl", 'wb') as f:
            pickle.dump(global_machine_times, f)
        with open(os.path.dirname(__file__)+"/../data/python/gdd.pkl", 'wb') as f:
            pickle.dump(gdd, f)
    
    return fig

def example_plot_table(gdd, global_machine_times, d, tab, fig):
    performance_index_data, controller_parameter_data = cal_performance_index(
        gdd, d, global_machine_times)

    # TODO:现在全部的tab中都会显示下面这个表格，we need to fix this bug
    with tab:
        df = pd.DataFrame(performance_index_data, index=['实际值', '理论值'])
        st.table(df)
        st.subheader('控制器PI参数为串联Series类型！')
        df = pd.DataFrame(controller_parameter_data, index=['取值'])
        st.table(df)

    # 保存图像到本地data中，并且以参数命名好
    if d['CTRL.bool_apply_sweeping_frequency_excitation'] == False:  # 不扫频才保存此时的响应曲线
        filename = f"{st.session_state.user_selected_motor}_{d['zeta']}_{d['omega_n']}_{d['max_CLBW_PER_min_CLBW']}_{d['VL_EXE_PER_CL_EXE']}.png"
        filepath = os.path.join(
            '..', 'emachinery', 'data', 'IPEMC2024-Slide', filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        fig.savefig(filepath, bbox_inches='tight')

def cal_performance_index(gdd, d, global_machine_times):

    zeta = d['zeta']
    omega_n = d['omega_n']
    max_CLBW_PER_min_CLBW = d['max_CLBW_PER_min_CLBW']
    VL_EXE_PER_CL_EXE = d['VL_EXE_PER_CL_EXE']

    FOC_CLBW = cal_CLBW(d)
    FOC_VLBW = cal_VLBW(d)

    speed_peak = max(gdd['CTRL.omega_r_mech'])
    speed_ref = max(gdd['CTRL.cmd_rpm'])

    iq_max = max(abs(gdd['CTRL.idq[1]']))
    uq_max = max(abs(gdd['ACM.udq[1]']))

    CL_SERIES_KP_Q = d['CL_SERIES_KP_Q']
    CL_SERIES_KI_Q = d['CL_SERIES_KI_Q']
    VL_SERIES_KP = d['VL_SERIES_KP']
    VL_SERIES_KI = d['VL_SERIES_KI']
    CL_SERIES_KP_D = d['CL_SERIES_KP_D']
    CL_SERIES_KI_D = d['CL_SERIES_KI_D']

    VL_FEEDBACK_KFB = d['VL_FEEDBACK_KFB']

    # 根据TPEL 2019 YY Chen的方法计算带宽上限 A Moderate Online Servo Controller Parameter Self-Tuning Method via Variable-Period Inertia Identification
    if True:
        Js = d['init_Js'] / 1000  # from kg cm^2 to kg m^2
        KE = d['init_KE']
        iqmax_virtual = d['init_IN']  # q轴最大电流真的取额定电流吗，TODO：我们应该推导出带宽和母线电压之间的关系
        FOC_VLBW_max = np.sqrt(2) * KE * iqmax_virtual / speed_ref / Js

        # TODO:把nominal_speed改成从d里面读取
        # nominal_speed = 760 * 2 * np.pi / 60 # rpm to rad/s
        nominal_speed = speed_peak * 2 * np.pi  # rpm to rad/s
        R = d['init_R']
        npp = d['init_npp']
        Lq = d['init_Lq']
        udc = d['DC_BUS_VOLTAGE']  # 母线电压
        FOC_CLBW_max = (np.sqrt(3) * udc - 3 * R * iqmax_virtual -
                        3 * npp * nominal_speed * KE) / 3 / Lq / iqmax_virtual

    # 根据b站老哥提供的电流环带宽理解求解电流环“推荐”最小值，就是说小于这个值的话，系统有超过一半的能量来建立磁场
    if True:
        FOC_CLBW_min = speed_ref * 2 * np.pi / 60 * npp

    # 计算上面响应曲线的性能指标
    if True:
        overshoot = (speed_peak - speed_ref) / speed_ref
        overshoot_real = np.exp(-np.pi * zeta / np.sqrt(1 - zeta**2))
        # 调节时间以2%为边界
        tolerance = 0.02
        upper_limit = speed_ref * (1 + tolerance)
        lower_limit = speed_ref * (1 - tolerance)
        # 找到系统响应的峰值时间
        peak_index = np.argmax(gdd['CTRL.omega_r_mech'])
        peak_time = global_machine_times[peak_index]
        settling_time = None
        # 找到系统响应经过峰值时间后，第一次进入到2%范围内的时间点
        for t, y in zip(global_machine_times, gdd['CTRL.omega_r_mech']):
            if t > peak_time and y > lower_limit and y < upper_limit:
                settling_time = t
                break
        settling_time_theoretical = 4/zeta/omega_n
        # 如果settling_time为None，转换为字符串'None'
        if settling_time is None:
            settling_time = 0

    # 创建一个字典，包含你想在表格中显示的数据
    performance_index_data = {
        'Overshoot': [f'{overshoot:.2%}', f'{overshoot_real:.2%}'],
        'Ts(s)': [f'{settling_time if settling_time is not None else settling_time:.4f}', f'{settling_time_theoretical:.4f}'],
        'Max_Iq(A)': [f'{iq_max:.2f}',    'N/A'],
        'Max_Uq(V)': [f'{uq_max:.2f}', 'N/A'],
        'CLBW(rad/s)': ['N/A', f'{FOC_CLBW:.2f}'],
        'VLBW': ['N/A', f'{FOC_VLBW:.2f}'],
        'Max_VLBW': ['N/A', f'{FOC_VLBW_max:.2f}'],
        'Max_CLBW': ['N/A', f'{FOC_CLBW_max:.2f}'],
        'Min_CLBW': ['N/A', f'{FOC_CLBW_min:.2f}'],
    }
    controller_parameter_data = {
        'CL_KP_Q': [f'{CL_SERIES_KP_Q:.2f}'],
        'CL_KI_Q': [f'{CL_SERIES_KI_Q:.2f}'],
        'VL_KP': [f'{VL_SERIES_KP:.2f}'],
        'VL_KI': [f'{VL_SERIES_KI:.2f}'],
        'CL_KP_D': [f'{CL_SERIES_KP_D:.2f}'],
        'CL_KI_D': [f'{CL_SERIES_KI_D:.2f}'],
        'VL_FEEDBACK_KFB': [f'{VL_FEEDBACK_KFB:.2f}'],
    }

    return performance_index_data, controller_parameter_data

def component_save_fig(fig, path):
    fig.savefig(path)
    st.toast(f'成功保存图片到{path}', icon='📊')
    return

def component_save_gdd_data(gdd, global_machine_times):
    with st.sidebar:
        st.button('保存Python仿真数据', on_click=component_save_gdd_data_toggle, args=[
                  gdd, global_machine_times], type="primary", help='点击后，保存数据到文件', use_container_width=True)

def component_save_gdd_data_toggle(data, global_machine_times, base_filename='result', ext='.pkl'):
    filename = f"./data/{base_filename}_{datetime.date.today()}"
    # 保存数据到文件
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    st.toast(f'成功保存仿真数据到{filename}', icon='🗃️')
    with open('./data/global_machine_times.pkl', 'wb') as file:
        pickle.dump(global_machine_times, file)
    st.toast(f'成功保存global_machine_times到./data/global_machine_times.pkl', icon='🗃️')
    return

def component_save_sweeping_data(d, gdd, global_machine_times):
    with st.sidebar:
        st.button('保存扫频数据', on_click=component_save_sweeping_data_toggle, args=[
                  d, gdd, global_machine_times], type="primary", help='点击后，保存数据到文件', use_container_width=True)
    return

def component_save_sweeping_data_toggle(d, gdd, global_machine_times):
    # save sweeping data to txt
    filename = './data/SweepingData.txt'
    with open(filename, 'w') as f:
        f.write('[Signal Name]\n')
        f.write(f"Sample Period: {d['CL_TS']} s\n")
        f.write(f'Sample Time: {max(global_machine_times):.6f} s\n')
        f.write('signal1  ID:0x23040000  Name:reference  Unit:rpm\n')
        f.write('signal2  ID:0x60690000  Name:feedback  Unit:rpm\n')
        f.write('\n')  # 空一格
        # {:<13s}、{:<13.6f}表示左对齐，占13个字符的宽度。<表示左对齐，13表示宽度，s表示字符串，f表示浮点数，.6表示小数点后的位数
        f.write('{:<13s}{:<13s}{:<13s}\n'.format(
            'Time(s)', 'signal1', 'signal2'))
        if d['CTRL.bool_sweeping_frequency_for_speed_loop'] == False:
            for time, signal1, signal2 in zip(global_machine_times, gdd['CTRL.cmd_idq[0]'], gdd['CTRL.idq[0]']):
                f.write('{:<13.6f}{:<13.6f}{:<13.6f}\n'.format(
                    time, signal1, signal2))
        else:
            for time, signal1, signal2 in zip(global_machine_times, gdd['CTRL.cmd_rpm'], gdd['CTRL.omega_r_mech']):
                f.write('{:<13.6f}{:<13.6f}{:<13.6f}\n'.format(
                    time, signal1, signal2))
    st.toast(f'成功保存global_machine_times到{filename}', icon='🗃️')
    return

def begin_simulation(d, acmsimpy):
    if 'simulation' in st.session_state and d == st.session_state.prev_d:
        simulation = st.session_state.simulation
        print('Simulation object is reused')
    else:
        simulation = acmsimpy.Simulation_Benchmark(d)
        st.session_state.prev_d = d
        st.session_state.simulation = simulation
    return simulation, simulation.gdd, simulation.global_machine_times

def example_fig_show(fig, tab, path):
    with tab:
        with st.container(border=True):
            st.info("运行下列命令可视化画图", icon="ℹ️")
            st.info("python main.py pyplot", icon="ℹ️")
            st.pyplot(fig)
            st.button(f'保存图片到{path}', on_click=component_save_fig, args=[
                      fig, path], type="primary", help='点击后，保存图片到文件', use_container_width=True)
    return

def edit_df_user_input_motor_dict():
    edit_df_user_input_motor_dict = st.edit_df_user_input_motor_dict.to_dict()[
        '0']
    for k, v in st.session_state.d_user_input_motor_dict.items():
        if k in edit_df_user_input_motor_dict:
            if type(v) == type(True):
                if edit_df_user_input_motor_dict[k] == 'True' or edit_df_user_input_motor_dict[k] == 'true':
                    st.session_state.d_user_input_motor_dict[k] = True
                elif edit_df_user_input_motor_dict[k] == 'False' or edit_df_user_input_motor_dict[k] == 'false':
                    st.session_state.d_user_input_motor_dict[k] = False
                continue
            st.session_state.d_user_input_motor_dict[k] = type(
                v)(edit_df_user_input_motor_dict[k])
    save_user_config_to_json()

def disabled_add_plot_config():
    if 'tuner_plot_para' not in st.session_state or len(st.session_state.tuner_plot_para) == 0:
        return False
    else:
        check_list = [['Ld', 'init_Ld'], ['Lq', 'init_Lq'], ['npp', 'init_npp'], ['KE', 'init_KE'],
                      ['Js', 'init_Js'], ['CLBW_Hz', 'FOC_CLBW_HZ'], [
                          'delta', 'FOC_delta'], ['R', 'init_R'], ['Js', 'init_Js'],
                      ['zeta', 'zeta'], ['omega_n', 'omega_n'], [
                          'max_CLBW_PER_min_CLBW', 'max_CLBW_PER_min_CLBW'],
                      ['CTRL.bool_apply_WC_tunner_for_speed_loop', 'CTRL.bool_apply_WC_tunner_for_speed_loop']]
        for para in st.session_state.tuner_plot_para:
            same_flag = True
            for item in check_list:
                if para[item[0]] != st.session_state.d_user_input_motor_dict[item[1]]:
                    same_flag = False
                    break
            if same_flag:
                return True
        return False

def show_para():
    # Session State exists for as long as the tab is open and connected to the Streamlit server. As soon as you close the tab, everything stored in Session State is lost.
    df_user_input_motor_dict = pd.DataFrame.from_dict(
        st.session_state.d_user_input_motor_dict, orient='index')
    with st.sidebar:
        with st.expander("可调参数：", expanded=True):
            try:
                options = st.multiselect(
                    'Parameter table',
                    df_user_input_motor_dict.index.tolist(),
                    VAR_LIST)
            except st.errors.StreamlitAPIException as e:
                print(e)
                print('清空你的\emy-c-2024\emachinery\jsons\streamllit_user_session_data.json文件再试一遍')
                raise e
            st.edit_df_user_input_motor_dict = st.data_editor(
                df_user_input_motor_dict.loc[options], use_container_width=True)
            st.button('Apply change', on_click=edit_df_user_input_motor_dict,
                      type="primary", help='点击后，修改参数生效', use_container_width=True)

            disabled = disabled_add_plot_config()
            st.button('Add controller config to plot', on_click=add_plot_config,
                      type="primary", disabled=disabled, use_container_width=True)
    # todo: 将用户的 VAR_LIST 保存为 session_data

######################################## Auto Save #########################################################

def save_user_config_to_json():
    # save user input filters as json file

    fname_session_state = f'{os.path.dirname(__file__)}/../jsons/streamllit_user_session_data.json'
    with open(fname_session_state, 'r') as f:
        user_data = json.load(f)

    user_data['user_selected_motor'] = st.session_state.user_selected_motor
    user_data[st.session_state.user_selected_motor] = {}
    user_data[st.session_state.user_selected_motor]['d_user_input_motor_dict'] = st.session_state.d_user_input_motor_dict

    with open(fname_session_state, 'w') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)
        # json.dump(dict(st.session_state), f, ensure_ascii=False, indent=4)
    # print('Session state is saved to ', fname_session_state)
    return

################################### Session State Console Log ##############################################

def toggle_show_session_state():
    st.session_state.show_session_state = not st.session_state.show_session_state

def init_session_state_console():
    if 'show_session_state' not in st.session_state:
        st.session_state.show_session_state = False
    with st.sidebar:
        st.markdown('---')
        if st.session_state.show_session_state:
            st.button('Hide session state', on_click=toggle_show_session_state,
                      type="secondary", use_container_width=True)
        else:
            st.button('Show session state', on_click=toggle_show_session_state,
                      type="secondary", use_container_width=True)
    if st.session_state.show_session_state:
        st.json(st.session_state)

################################### ep9 Plot Section ########################################################

def toggle_show_ep9_plot():
    st.session_state.show_ep9_plot = not st.session_state.show_ep9_plot

def save_ep9_config(config):
    path = f'{os.path.dirname(__file__)}/../sensorless/config/user_config.txt'
    with open(path, 'w') as f:
        f.write(config)

def read_ep9_config():
    path = f'{os.path.dirname(__file__)}/../sensorless/config/user_config.txt'
    with open(path, 'r') as f:
        lines = f.readlines()
    result = ''
    for line in lines:
        result += line
    return result

def init_ep9_plot(d, tab, nplot_main):
    with tab:
        st.subheader('ep9 plot')

    result = read_ep9_config()
    d_tmp = d.copy()
    d_tmp_change_list = ['CL_SERIES_KP',
                         'CL_SERIES_KI', 'VL_SERIES_KP', 'VL_SERIES_KI']
    for para in d_tmp_change_list:
        d_tmp[para] = None
    if 'show_ep9_plot' not in st.session_state:
        st.session_state.show_ep9_plot = False
    with st.sidebar:
        st.markdown('---')
        if st.session_state.show_ep9_plot:
            st.button('Hide ep9 plot', on_click=toggle_show_ep9_plot,
                      type="secondary", use_container_width=True)
        else:
            st.button('Show ep9 plot', on_click=toggle_show_ep9_plot,
                      type="secondary", use_container_width=True)
    if st.session_state.show_ep9_plot:
        with st.sidebar:
            st.warning(
                '请小心使用这个功能，可能会造成collect_data.py和user_config.txt文件出错!!!', icon="⚠️")
            config = st.text_area('Config text', result)
            st.button('Apply change', on_click=save_ep9_config,
                      args=[config], type="primary")
        with tab:
            st.pyplot(nplot_main(d_tmp))

######################################### Bode Plot Section #################################################

def Step_Response(tfs, ax, title):
    for idx, tf in enumerate(tfs):
        T, yout = control.step_response(tf, T=0.2)
        ax.plot(T, yout, label=idx)
    ax.set_ylabel('Amplitude [rad/s]', fontname="Times New Roman")
    ax.set_xlabel('Time [s]', fontname="Times New Roman")
    ax.set_title(title)
    if title == 'Step Response':
        ax.set_xlim(0.0, 0.2)
    ax.legend()
    plt.rcParams["font.family"] = "Times New Roman"

def Bode_Plot(tfs, ax1, ax2):
    omega_range = np.logspace(0, 6, 10000)
    for idx, tf in enumerate(tfs):
        mag, phase, omega = control.bode_plot(
            tf, dB=True, plot=False, omega=omega_range)
        ax1.semilogx(omega, 20*np.log10(mag), label=idx)
        ax2.semilogx(omega, phase*180./np.pi, label=idx)
    ax1.set_ylabel('Magnitude [dB]', fontname="Times New Roman")
    ax2.set_ylabel('Phase [°]', fontname="Times New Roman")
    ax1.set_xlabel('Frequency [rad/s]', fontname="Times New Roman")
    ax2.set_xlabel('Frequency [rad/s]', fontname="Times New Roman")
    ax1.set_title('Bode Plot', fontname="Times New Roman")

    # 设置横坐标范围
    ax1.set_xlim(1, 1e6)
    ax2.set_xlim(1, 1e6)

    ax1.legend()

def figure_generator():
    Speed_OpenLoop_tf_list = []
    Speed_CloseLoop_tf_list = []
    Load_Rejection_tf_list = []
    if 'tuner_plot_para' not in st.session_state:
        st.session_state.tuner_plot_para = []
    for para in st.session_state.tuner_plot_para:
        Ld, Lq, npp, KE, KT, Js, CLBW_Hz, delta, R, Js = \
            para['Ld'], para['Lq'], para['npp'], para['KE'], para['KT'], para['Js'], para['CLBW_Hz'], para['delta'], para['R'], para['Js']

        # for new tuner
        zeta, omega_n, max_CLBW_PER_min_CLBW = para['zeta'], para['omega_n'], para['max_CLBW_PER_min_CLBW']

        # for convenience
        K = KT/Js

        # para['CL_SERIES_KP_Q'] = q_currentKp
        # para['CL_SERIES_KI_Q'] = q_currentKi
        # para['VL_SERIES_KP'] = speedKp
        # para['VL_SERIES_KI'] = speedKi

        if para['CTRL.bool_apply_WC_tunner_for_speed_loop'] == False:
            _, d_q_currentKp, d_currentKi, q_currentKp, q_currentKi, speedKp, speedKi, speedKFB, _, _, _ = \
                tuner.InstaSPIN_series_PI_tuner(
                    delta, CLBW_Hz, Ld, Lq, R, Js, npp, KE, bool_render=True)

            Speed_Regulator_tf = control.tf(
                [speedKp, speedKp*speedKi], [1, 0])  # 速度环PI控制器, parallel form
            Current_CloseLoop_tf = control.tf(
                [1], [Lq/q_currentKp, 1])  # 电流环传函
            # 速度环的Dynamic，就是j个很简单的积分环节
            Motor_Motion = control.tf([KT/Js], [1, 0])

            Speed_OpenLoop_tf = Motor_Motion * \
                Current_CloseLoop_tf * Speed_Regulator_tf  # 速度环的开环传函
            Speed_CloseLoop_tf = control.feedback(
                Speed_OpenLoop_tf, 1, -1)  # 速度环的闭环传函

            # 这里的CLBW记得改成rad/s为单位的
            CLBW_rad_s = 2*np.pi*CLBW_Hz
            LR_Plant = control.tf([-1], [Js, 0])
            LR_Feedback_loop = KT * Current_CloseLoop_tf * Speed_Regulator_tf
            Load_Rejection_tf = control.feedback(
                LR_Plant, LR_Feedback_loop, 1)  # 这里取正反馈
            # Load_Rejection_tf = KT * Load_Rejection_tf
            Load_Rejection_tf_cal = control.tf([-1/Js, -1/Js*CLBW_rad_s, 0], [
                                               1, CLBW_rad_s, speedKp*K*CLBW_rad_s, speedKi*speedKp*K*CLBW_rad_s])  # 负载抗扰传函

        else:
            d_currentKp, d_currentKi, q_currentKp, q_currentKi, speedKp, speedKi, speedKFB = tuner.WC_tuner(
                zeta, omega_n, max_CLBW_PER_min_CLBW, Ld, Lq, R, Js, npp, KE)
            Current_CloseLoop_tf = control.tf(
                [1], [Lq/q_currentKp, 1])  # 电流环传函，first-order transfer
            Speed_Loop_Plant = control.feedback(
                Current_CloseLoop_tf, speedKFB, -1)

            Speed_Regulator_tf = control.tf(
                [speedKp, speedKp*speedKi], [1, 0])  # 速度环PI控制器, parallel form
            Speed_OpenLoop_tf = control.series(
                Speed_Regulator_tf, Speed_Loop_Plant)
            Speed_CloseLoop_tf = control.feedback(Speed_OpenLoop_tf, 1, -1)

            LR_Plant = control.tf([-1], [Js, 0])
            LR_Feedback_loop = KT * Current_CloseLoop_tf * \
                (Speed_Regulator_tf + speedKFB)
            Load_Rejection_tf = control.feedback(
                LR_Plant, LR_Feedback_loop, 1)  # 这里取正反馈
            # Load_Rejection_tf = control.tf([-1/Js, -1/Js*CLBW_rad_s, 0], [1, CLBW_rad_s, (speedKp + speedKFB)*K*CLBW_rad_s, speedKi*speedKp*K*CLBW_rad_s ]) # 负载抗扰传函

        Speed_OpenLoop_tf_list.append(Speed_OpenLoop_tf)
        Speed_CloseLoop_tf_list.append(Speed_CloseLoop_tf)
        Load_Rejection_tf_list.append(Load_Rejection_tf)

    fig1, axs1 = plt.subplots(2, 1, figsize=(8, 10))

    fig2, axs2 = plt.subplots(4, 1, figsize=(8, 14))
    plt.subplots_adjust(hspace=0.5)

    # Step_Response(Speed_CloseLoop_tf_list, axs1[0], 'Step Response')
    # Step_Response(Load_Rejection_tf_list, axs1[1], 'Load Rejection')

    # print(f'{Speed_OpenLoop_tf_list=}',f'{Load_Rejection_tf_list=}')
    Bode_Plot(Speed_OpenLoop_tf_list, axs2[0], axs2[1])
    Bode_Plot(Load_Rejection_tf_list, axs2[2], axs2[3])

    return fig1, fig2

def add_plot_config():
    result = {}
    result['Ld'] = st.session_state.d_user_input_motor_dict['init_Ld']  # 定子D电感
    result['Lq'] = st.session_state.d_user_input_motor_dict['init_Lq']  # 定子Q轴电感
    result['npp'] = st.session_state.d_user_input_motor_dict['init_npp']  # 极对数
    result['KE'] = st.session_state.d_user_input_motor_dict['init_KE']  # 反电势系数
    result['KT'] = 1.5*result['npp']*result['KE']  # 转矩系数
    result['Js'] = st.session_state.d_user_input_motor_dict['init_Js']  # 转动惯量
    result['CLBW_Hz'] = st.session_state.d_user_input_motor_dict['FOC_CLBW_HZ']  # 电流环带宽
    result['delta'] = st.session_state.d_user_input_motor_dict['FOC_delta']
    result['R'] = st.session_state.d_user_input_motor_dict['init_R']
    result['Js'] = st.session_state.d_user_input_motor_dict['init_Js']
    # for new tuner
    result['Bool_NewTuner_On'] = st.session_state.d_user_input_motor_dict['CTRL.bool_apply_WC_tunner_for_speed_loop']
    result['zeta'] = st.session_state.d_user_input_motor_dict['zeta']
    result['omega_n'] = st.session_state.d_user_input_motor_dict['omega_n']
    result['max_CLBW_PER_min_CLBW'] = st.session_state.d_user_input_motor_dict['max_CLBW_PER_min_CLBW']
    result['CTRL.bool_apply_WC_tunner_for_speed_loop'] = st.session_state.d_user_input_motor_dict['CTRL.bool_apply_WC_tunner_for_speed_loop']
    if 'tuner_plot_para' not in st.session_state:
        st.session_state.tuner_plot_para = []
    if result not in st.session_state.tuner_plot_para:
        st.session_state.tuner_plot_para.append(result)
    print(st.session_state.tuner_plot_para)

def toggle_bode_plot():
    st.session_state.bode_plot = not st.session_state.bode_plot

def init_bode_plot(tab):
    with tab:
        st.subheader('Bode plot')
    if 'bode_plot' not in st.session_state:
        st.session_state.bode_plot = False
    with st.sidebar:
        st.markdown('---')
        if st.session_state.bode_plot:
            st.button('Hide Bode plot', on_click=toggle_bode_plot,
                      type="secondary", use_container_width=True)
        else:
            st.button('Show Bode plot', on_click=toggle_bode_plot,
                      type="secondary", use_container_width=True)
    if st.session_state.bode_plot:
        add_plot_config()
        fig1, fig2 = figure_generator()
        with tab:
            # st.pyplot(fig1)
            st.pyplot(fig2)

################################### Variable Sweep ########################################################

def toggle_show_run_sweep():
    st.session_state.show_run_sweep = not st.session_state.show_run_sweep

def cal_CLBW(d):
    if d['CTRL.bool_apply_WC_tunner_for_speed_loop'] == True:
        max_CLBW_PER_min_CLBW = d['max_CLBW_PER_min_CLBW']
        max_CLBW = d['zeta'] * d['omega_n'] * 4
        min_CLBW = d['zeta'] * d['omega_n'] * 2

        if max_CLBW_PER_min_CLBW > 1:
            raise ValueError('max_CLBW_PER_min_CLBW > 1 change change it !?')
        else:
            # 通过一个小于1的比例系数来选取电流环带宽
            FOC_CLBW = max_CLBW_PER_min_CLBW * max_CLBW + \
                (1-max_CLBW_PER_min_CLBW) * min_CLBW
    else:
        # Kp/Lq is the current bandwidth
        FOC_CLBW = d['CL_SERIES_KP_Q'] / d['init_Lq']

    return FOC_CLBW

def cal_VLBW(d):
    if d['CTRL.bool_apply_WC_tunner_for_speed_loop'] == True:
        FOC_VLBW = d['omega_n'] * np.sqrt(1 - 2 * d['zeta'] **
                                          2 + np.sqrt(4 * d['zeta'] ** 4 - 4 * d['zeta'] ** 2 + 2))
    else:
        FOC_CLBW = d['CL_SERIES_KP_Q'] / d['init_Lq']
        Gain = d['FOC_delta'] + 2.16 * \
            np.exp(-1 * d['FOC_delta'] / 2.8) - 1.86  # 从CLBW计算VLBW的估计公式
        FOC_VLBW = FOC_CLBW / Gain
    return FOC_VLBW
    # sqrt(1 - 2x² + sqrt(4x⁴ - 4x² + 2))

def cal_real_CLBW(d):
    # 强制开启扫频
    d['CTRL.bool_apply_sweeping_frequency_excitation'] = True
    # 开启电流环扫频功能
    d['CTRL.bool_sweeping_frequency_for_speed_loop'] = False
    # 设置时间 s
    d['TIME_SLICE'] = 1.5
    # ATTETION:这里不需要给定zeta和omega_n了，
    # 因为传入进来的d里面已经有相应HitWall时候的控制器参数，该开始我还想在这修改，多次一举
    # 保证扫频中不存在Load
    d['user_system_input_code'] = "if ii < 1: CTRL.cmd_idq[0] = 0.0; CTRL.cmd_rpm = 200 \nelif ii<100: CTRL.cmd_rpm = -100"

    sim = acmsimpy.Simulation_Benchmark(d)
    gdd, global_machine_times = sim.gdd, sim.global_machine_times
    # 存入扫频数据
    component_save_sweeping_data(d, gdd, global_machine_times)
    # 扫频数据计算带宽
    max_freq = 2000  # Hz
    FOC_real_CLBW = Sweeping_data2Bandwidth(max_freq)
    return FOC_real_CLBW

def cal_real_VLBW(d):
    # 强制开启扫频
    d['CTRL.bool_apply_sweeping_frequency_excitation'] = True
    # 开启速度环扫频功能
    d['CTRL.bool_sweeping_frequency_for_speed_loop'] = True
    # 设置时间 s
    d['TIME_SLICE'] = 1.2
    sim = acmsimpy.Simulation_Benchmark(d)
    gdd, global_machine_times = sim.gdd, sim.global_machine_times
    # 存入扫频数据
    component_save_sweeping_data(d, gdd, global_machine_times)
    # 扫频数据计算带宽
    max_freq = 1000  # Hz
    FOC_real_VLBW = Sweeping_data2Bandwidth(max_freq)
    return FOC_real_VLBW

def Sweeping_data2Bandwidth(max_freq):
    # Target file name
    fname = 'data/SweepingData.txt'
    # Read name and meta data
    signal_names = []
    with open(fname, 'r', encoding='gb2312') as f:
        for _ in range(5):
            line = f.readline()
            print(line)
            if 'Unit' in line:
                signal_name = line[line.find('Name')+5: line.find('Unit')]
                signal_names.append(signal_name)

    # read data as Data Frame
    df = pd.read_csv(fname, skiprows=7, sep='\s+', encoding='gb2312',
                     names=['Time(s)', signal_names[0], signal_names[1]])

    # Unpack as Series
    time = df['Time(s)']
    x_ref = df[signal_names[0]]
    x_qep = df[signal_names[1]]  # + 100 # add dc offset for test

    # Basic DFT parameters
    # N = df.shape[0]
    Ts = df['Time(s)'][1] - df['Time(s)'][0]
    samplingFreq = 1/Ts
    EndTime = df['Time(s)'].iloc[-1]

    ## DFT ##
    list_qep_max_amplitude = []
    list_qep_max_frequency = []
    list_ref_max_amplitude = []
    list_ref_max_frequency = []

    index_single_tone_begin = 0
    index_single_tone_end = 0
    # max_freq = 5 # debug
    for freq in range(1, max_freq):  # datum point at 1 Hz is absent
        period = 1/freq
        index_single_tone_begin = index_single_tone_end
        index_single_tone_end = index_single_tone_begin + int(period/Ts)

        ST_time = time[index_single_tone_begin:index_single_tone_end]
        ST_x_ref = x_ref[index_single_tone_begin:index_single_tone_end]
        ST_x_qep = x_qep[index_single_tone_begin:index_single_tone_end]

        # x_ref_dft = fft(ST_x_ref)
        # x_qep_dft = fft(ST_x_qep)

        if len(ST_x_ref) > 0 and len(ST_x_qep) > 0:
            x_ref_dft = fft(ST_x_ref)
            x_qep_dft = fft(ST_x_qep)
        else:
            print(
                f"Skipping FFT for frequency {freq} due to insufficient data points.")
        # Do DFT (Raw)
        N = len(ST_time)

        # Convert raw DFT results into human-friendly forms
        resolution = samplingFreq/N  # [Hz]
        Neff = math.ceil(N/2)  # number of effective points
        # 其实理论上来说，这里是比较复杂的，当N为偶数的时候，奈奎斯特频率就是采样频率的二分之一？当N为奇数的时候，还会多出一个分量，这个分量和直流分量是一对，具体我忘了……可能有错
        # 原始复数dft结果（双边变单边，除了直流分量，其他分量全部要乘以2）
        x_ref_hat = np.append(x_ref_dft[0]/N, 2*x_ref_dft[1:Neff+1]/N)
        x_qep_hat = np.append(x_qep_dft[0]/N, 2*x_qep_dft[1:Neff+1]/N)

        # qep related data collection
        max_amplitude = max(abs(x_qep_hat))
        list_qep_max_amplitude.append(max_amplitude)
        max_index = np.argmax(abs(x_qep_hat))
        max_frequency = (max_index+0)*resolution
        list_qep_max_frequency.append(max_frequency)

        # ref related data collection
        max_amplitude = max(abs(x_ref_hat))
        list_ref_max_amplitude.append(max_amplitude)
        max_index = np.argmax(abs(x_ref_hat))
        max_frequency = (max_index+0)*resolution
        list_ref_max_frequency.append(max_frequency)

    # Bode
    if max_freq > 500:
        list_ref_max_frequency = list(range(2, max_freq))
        list_qep_max_frequency = list(range(2, max_freq))

    # TODO：修复bug，这里freq缺1Hz
    list_ref_max_frequency.insert(0, 1)
    list_qep_max_frequency.insert(0, 1)
    closed_loop_transfer_function = [
        qep/ref for ref, qep in zip(list_ref_max_amplitude, list_qep_max_amplitude)]
    dB_values = [20*np.log10(el) for el in closed_loop_transfer_function]
    # Find -3dB point
    for i, dB in enumerate(dB_values):
        if dB < -3:
            break
    freq_at_minus_3dB = list_qep_max_frequency[i]
    # Convert to rad/s
    freq_at_minus_3dB_rad_s = freq_at_minus_3dB * 2 * np.pi
    return freq_at_minus_3dB_rad_s

def plot_for_sweep(var, var_list, iq_list, uq_list, overshoot_list):
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    plt.style.use('bmh')
    mpl.rc('font', family='Times New Roman', size=10.0)
    mpl.rc('legend', fontsize=10)
    # mpl.rc('lines', linewidth=4, linestyle='-.')
    mpl.rcParams['lines.linewidth'] = 0.75
    mpl.rcParams['mathtext.fontset'] = 'stix'

    fig, axes = plt.subplots(nrows=2, ncols=1, dpi=600,
                             facecolor='w', figsize=(8, 4), sharex=True)

    ax = axes[0]
    ax.plot(var_list, iq_list, label=r'$i_{q_{max}}$')
    ax.plot(var_list, uq_list, label=r'$u_{q_{max}}$')
    # ) #, fontdict=font)
    ax.set_ylabel(
        r'$i_{q\rm max}\qquad u_{q\rm max}$ [A V]', multialignment='center')
    # ax.legend(loc=2, prop={'size': 6})
    ax.legend(loc=1, fontsize=6)

    ax = axes[1]
    ax.plot(var_list, overshoot_list, label=r'$\sigma$')
    # ax.plot(global_machine_times, gdd['ACM.iD'])
    ax.set_ylabel(r'overshoot(%)', multialignment='center')  # , fontdict=font)

    for ax in axes:
        ax.grid(True)
        ax.legend(loc=1)
        # for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        #     tick.label.set_font(font)
    axes[-1].set_xlabel(var)  # , fontdict=font)

    # 在 Streamlit 应用中显示图形
    st.pyplot(plt)

def 撞墙数据写入excel(df_Hit_Wall, Hit_Wall_filename_excel):
    # 检查Excel是否正在运行
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'EXCEL.EXE':
            # 如果Excel正在运行，关闭它，这样不会报错
            ps = psutil.Process(proc.info['pid'])
            ps.terminate()
    # 读取原有的Excel文件
    if os.path.exists(Hit_Wall_filename_excel):
        df_existing = pd.read_excel(Hit_Wall_filename_excel)
    else:
        df_existing = pd.DataFrame()
    # 将新的数据追加到DataFrame的末尾
    df_combined = pd.concat([df_existing, df_Hit_Wall])
    # 将整个DataFrame写回Excel文件，并且 writer变量会在无excel时，创建一个
    with pd.ExcelWriter(Hit_Wall_filename_excel, mode='w') as writer:
        df_combined.to_excel(writer, index=False)

def sweep_main(var, sweep_min, sweep_max, sweep_step, d, tab):
    # print(var, sweep_min, sweep_max, sweep_step)
    d_tmp = d.copy()
    with tab:
        overshoot_list = []
        iq_list = []
        uq_list = []
        var_list = []
        FOC_CLBW_list = []
        FOC_VLBW_list = []
        Hit_Wall_flag = False

        Sweep_Data_filename_excel = 'Sweep_Data.xlsx'
        Hit_Wall_filename_excel = 'Hit_Wall.xlsx'

        zeta = d_tmp['zeta']
        overshoot_theoretical = np.exp(-np.pi * zeta / np.sqrt(1 - zeta**2))

        while sweep_min <= sweep_max:
            d_tmp[var] = sweep_min
            sweep_min += sweep_step
            sim1 = acmsimpy.Simulation_Benchmark(d_tmp)
            gdd, global_machine_times = sim1.gdd, sim1.global_machine_times

            iq_max = max(abs(gdd['CTRL.idq[1]']))
            uq_max = max(abs(gdd['ACM.udq[1]']))

            var_now = sweep_min-sweep_step
            var_list.append(var_now)  # get the last value of var

            iq_list.append(iq_max)
            uq_list.append(uq_max)

            # calculate the CLBW and VLBW
            FOC_CLBW = cal_CLBW(d_tmp)
            FOC_CLBW_list.append(FOC_CLBW)
            FOC_VLBW = cal_VLBW(d_tmp)
            FOC_VLBW_list.append(FOC_VLBW)

            # calculate overshoot
            speed_peak = max(gdd['CTRL.omega_r_mech'])
            speed_ref = max(gdd['CTRL.cmd_rpm'])
            overshoot = (speed_peak - speed_ref) / speed_ref
            overshoot_list.append(overshoot)

            # 将第一次uq撞墙的结果放入到Hit Wall excel中
            if uq_max >= d_tmp['DC_BUS_VOLTAGE'] / 1.732 and Hit_Wall_flag == False:
                Hit_Wall_flag = True
                df_Hit_Wall = pd.DataFrame({
                    var: [var_now],  # 将标量值放入列表中
                    'speed_ref': [speed_ref],
                    'iq_max': [iq_max],
                    'uq_max': [uq_max],
                    'FOC_CLBW': [FOC_CLBW],
                    'FOC_VLBW': [FOC_VLBW],
                    'overshoot': [overshoot],
                    'overshoot_theoretical': [overshoot_theoretical],
                    'zeta_set': [zeta],
                })
                撞墙数据写入excel(df_Hit_Wall, Hit_Wall_filename_excel)

            st.markdown('---')
            st.warning(var + ' = ' + str(sweep_min-sweep_step) +
                       ' CLBW = {:.2f}rad/s'.format(FOC_CLBW) + ' VLBW = {:.2f}rad/s'.format(FOC_VLBW))
            fig = example_plot(gdd, global_machine_times)
            example_plot_table(gdd, global_machine_times, d, tab, fig)
            st.pyplot(fig)

        # 把扫描结果画出来
        st.markdown('---')
        plot_for_sweep(var, var_list, iq_list, uq_list, overshoot_list)

        # 创建一个 DataFrame，保存list中的数据
        df_Sweep_data = pd.DataFrame({
            var: var_list,  # 假设 var_list 是包含所有 var 值的列表
            'iq_max': iq_list,
            'uq_max': uq_list,
            'FOC_CLBW': FOC_CLBW_list,
            'FOC_VLBW': FOC_VLBW_list,
            'overshoot': overshoot_list,
            'overshoot_theoretical': overshoot_theoretical,
            'zeta_set': zeta,
        })
        df_Sweep_data.to_excel(Sweep_Data_filename_excel, index=False)

def sweep_main_find_HitWall(var, sweep_min, sweep_max, sweep_step, tab, d):
    # print(var, sweep_min, sweep_max, sweep_step)
    sweep_min_init = sweep_min
    sweep_max_init = sweep_max
    d_tmp = d.copy()
    TIME_SLICE = d_tmp['TIME_SLICE']  # 保存一份TIME_SLICE的初始值
    with tab:
        ref_speed_list = [30, 50, 70, 100, 130, 160, 200,
                          240, 280, 320, 360, 400, 450, 500]  # command RPM
        # ref_speed_list = [200, 240, 280] # command RPM
        # ref_speed_list = [200, 240, 280, 320] # command RPM
        for speed in ref_speed_list:
            # 修改电机的命令
            d_tmp[
                'user_system_input_code'] = f"if ii < 100: CTRL.cmd_idq[0] = 0.0; CTRL.cmd_rpm = {speed}"
            d_tmp['TIME_SLICE'] = TIME_SLICE  # 确保TIME_SLICE的初始值不变
            # 确保不在撞墙loop中不开启扫频功能
            d_tmp['CTRL.bool_sweeping_frequency_for_speed_loop'] = False

            Hit_Wall_flag = False
            # once for all the situation 循环就写在这！
            Hit_Wall_filename_excel = 'Hit_Wall_uq.xlsx'
            Hit_Wall_iq_filename_excel = 'Hit_Wall_iq.xlsx'  # 存储以iq_max为上限的数据

            zeta = d_tmp['zeta']
            overshoot_theoretical = np.exp(-np.pi *
                                           zeta / np.sqrt(1 - zeta**2))

            # 在break后，将sweep_min重新赋值为初始值
            sweep_min = sweep_min_init
            sweep_max = sweep_max_init

            while sweep_min <= sweep_max:
                d_tmp[var] = sweep_min
                sweep_min += sweep_step
                sim1 = acmsimpy.Simulation_Benchmark(d_tmp)
                gdd, global_machine_times = sim1.gdd, sim1.global_machine_times

                var_now = sweep_min-sweep_step

                # calculate iqmax and uqmax
                iq_max = max(abs(gdd['CTRL.idq[1]']))
                uq_max = max(abs(gdd['ACM.udq[1]']))

                # calculate the CLBW and VLBW
                FOC_CLBW = cal_CLBW(d_tmp)
                FOC_VLBW = cal_VLBW(d_tmp)

                # calculate overshoot
                speed_peak = max(gdd['CTRL.omega_r_mech'])
                speed_ref = max(gdd['CTRL.cmd_rpm'])
                overshoot = (speed_peak - speed_ref) / speed_ref

                # 将第一次uq撞墙的结果放入到Hit Wall excel中
                if uq_max >= d_tmp['DC_BUS_VOLTAGE'] / 1.732 and Hit_Wall_flag == False:
                    Hit_Wall_flag = True
                    FOC_real_CLBW = cal_real_CLBW(d_tmp)
                    FOC_real_VLBW = cal_real_VLBW(d_tmp)
                    df_Hit_Wall = pd.DataFrame({
                        var: [var_now],  # 将标量值放入列表中
                        'speed_ref': [speed_ref],
                        'iq_max': [iq_max],
                        'uq_max': [uq_max],
                        'FOC_CLBW': [FOC_CLBW],
                        'FOC_VLBW': [FOC_VLBW],
                        'FOC_real_CLBW': [FOC_real_CLBW],
                        'FOC_real_VLBW': [FOC_real_VLBW],
                        'overshoot': [overshoot],
                        'overshoot_theoretical': [overshoot_theoretical],
                        'zeta_set': [zeta],
                    })
                    撞墙数据写入excel(df_Hit_Wall, Hit_Wall_filename_excel)
                    break
                # 将第一次iq撞墙的结果放入到Hit Wall iq excel中
                # if iq_max >= d_tmp['init_IN'] and Hit_Wall_flag == False:
                #     Hit_Wall_flag = True
                #     df_Hit_Wall = pd.DataFrame({
                #         var: [var_now],  # 将标量值放入列表中
                #         'speed_ref': [speed_ref],
                #         'iq_max': [iq_max],
                #         'uq_max': [uq_max],
                #         'FOC_CLBW': [FOC_CLBW],
                #         'FOC_VLBW': [FOC_VLBW],
                #         'overshoot': [overshoot],
                #         'overshoot_theoretical': [overshoot_theoretical],
                #         'zeta_set': [zeta],
                #     })
                #     撞墙数据写入excel(df_Hit_Wall, Hit_Wall_iq_filename_excel)
                #     break

def show_sweep(tab, d):
    with tab:
        var = st.selectbox(
            "Sweep Variable",
            (VAR_LIST_SWEEP),
            index=None,
            placeholder="Select a variable to sweep",
        )
        sweep_min = st.number_input('Sweep min', value=100)
        sweep_max = st.number_input('Sweep max', value=4500)
        sweep_step = st.number_input('Sweep step', value=20)
        st.button('Start sweeping', on_click=sweep_main, args=[
                  var, sweep_min, sweep_max, sweep_step], type="primary", use_container_width=True)
        st.button('Find Hit Wall', on_click=sweep_main_find_HitWall, args=[
                  var, sweep_min, sweep_max, sweep_step, tab, d], type="primary", use_container_width=True)
        st.warning('修改ref_speed_list中的变量以修改要检测的转速', icon="⚠️")

def init_run_sweep(tab):
    with tab:
        st.subheader('Sweep')
    if 'show_run_sweep' not in st.session_state:
        st.session_state.show_run_sweep = False
    with st.sidebar:
        st.markdown('---')
        if st.session_state.show_run_sweep:
            st.button('Hide Sweep', on_click=toggle_show_run_sweep,
                      type="secondary", use_container_width=True)
        else:
            st.button('Show Sweep', on_click=toggle_show_run_sweep,
                      type="secondary", use_container_width=True)
    if st.session_state.show_run_sweep:
        show_sweep()

################################### show HitWall plot ########################################################

def init_HitWall_plot(tab):
    with tab:
        #  显示tab6的标题
        st.subheader('Hit Wall Plot (Bandwidth is the IDEAL value from TF)')

    if 'show_HitWall_plot' not in st.session_state:
        st.session_state.show_HitWall_plot = False
    with st.sidebar:
        st.markdown('---')
        if st.session_state.show_HitWall_plot:
            st.button('Hide Hit Wall plot', on_click=toggle_show_HitWall_plot,
                      type="secondary", use_container_width=True)
        else:
            st.button('Show Hit Wall plot', on_click=toggle_show_HitWall_plot,
                      type="secondary", use_container_width=True)
    if st.session_state.show_HitWall_plot:
        show_HitWall_plot(tab)

def toggle_show_HitWall_plot():
    st.session_state.show_HitWall_plot = not st.session_state.show_HitWall_plot

def show_HitWall_plot(tab):
    with tab:
        filename_uq_max = 'Hit_Wall_uq.xlsx'
        filename_iq_max = 'Hit_Wall_iq.xlsx'
        df_uq = pd.read_excel(filename_uq_max)
        df_iq = pd.read_excel(filename_iq_max)
        HitWall_plot_main(df_uq, df_iq)
        st.warning('现在HitWall图中的带宽为传函的理论值，不是实际值！', icon='⚠️')

def HitWall_plot_main(df_uq, df_iq):
    # https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
    plt.style.use('bmh')
    mpl.rc('font', family='Times New Roman', size=10.0)
    mpl.rc('legend', fontsize=10)
    # mpl.rc('lines', linewidth=4, linestyle='-.')
    mpl.rcParams['lines.linewidth'] = 0.75
    mpl.rcParams['mathtext.fontset'] = 'stix'

    # 对excel中的数据进行分组
    df1_uq = df_uq.loc[(df_uq['uq_max'] > 0) & (df_uq['uq_max'] < 21)]
    df2_uq = df_uq.loc[(df_uq['uq_max'] > 24) & (df_uq['uq_max'] < 30)]
    df3_uq = df_uq.loc[(df_uq['uq_max'] > 31) & (df_uq['uq_max'] < 40)]

    df1_iq = df_iq.loc[(df_iq['iq_max'] > 0) & (df_iq['iq_max'] < 8)]
    df2_iq = df_iq.loc[(df_iq['iq_max'] > 8.5) & (df_iq['iq_max'] < 12)]
    # 这里设置34A的最大电流，超过了其实没什么意义，因为好像电流太大电机直接发散了？
    df3_iq = df_iq.loc[(df_iq['iq_max'] > 12.5) & (df_iq['iq_max'] < 34)]

    fig, axes = plt.subplots(nrows=2, ncols=1, dpi=600,
                             facecolor='w', figsize=(8, 8), sharex=True)

    ax = axes[0]
    ax.plot(df1_uq['speed_ref'], df1_uq['FOC_VLBW'],
            label=r'$V_{DC \mathrm{max} }$=36V')
    ax.plot(df2_uq['speed_ref'], df2_uq['FOC_VLBW'],
            label=r'$V_{DC \mathrm{max} }$=48V')
    ax.plot(df3_uq['speed_ref'], df3_uq['FOC_VLBW'],
            label=r'$V_{DC \mathrm{max} }$=60V')
    # ) #, fontdict=font)
    ax.set_ylabel(r'Speed Loop Bandwidth [rad/s]', multialignment='center')

    # Set yticks
    ax.set_ylim([0, 4500])
    ax.set_yticks(np.arange(0, 4500, step=500))  # 设置y轴的刻度为500一格

    ax = axes[1]
    ax.plot(df1_iq['speed_ref'], df1_iq['FOC_VLBW'],
            label=r'$i_{q \mathrm{max}}$=7A')
    ax.plot(df2_iq['speed_ref'], df2_iq['FOC_VLBW'],
            label=r'$i_{q \mathrm{max}}$=10A')
    ax.plot(df3_iq['speed_ref'], df3_iq['FOC_VLBW'],
            label=r'$i_{q \mathrm{max}}$=13A')
    # ) #, fontdict=font)
    ax.set_ylabel(r'Speed Loop Bandwidth [rad/s]', multialignment='center')

    # Set yticks
    ax.set_ylim([0, 4500])
    ax.set_yticks(np.arange(0, 4500, step=500))  # 设置y轴的刻度为500一格

    for ax in axes:
        ax.grid(True)
        ax.legend(loc=1)
        # for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        #     tick.label.set_font(font)
    axes[-1].set_xlabel('Command Speed [RPM]')  # , fontdict=font)

    # 在 Streamlit 应用中显示图形
    st.pyplot(plt)
