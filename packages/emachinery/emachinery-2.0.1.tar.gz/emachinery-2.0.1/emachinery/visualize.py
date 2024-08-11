from pylab import np, plt, mpl, fft
import os, json, builtins, datetime, collections, pkg_resources, base64, copy
from io import BytesIO
import streamlit as st
import pandas as pd
# import  tools.tutorials_ep6_maglev_motor as acmsimpy
import tools.tutorials_ep61_remove_numba as acmsimpy

from sensorless.nplot import main as nplot_main
import ACMParam
import pickle
from openpyxl import load_workbook
import os
import psutil
import math
import tools.config as config
import tools.component as cpt
import tools.user_script_main as usm
import tools.component_c as cptc

# Python main function
def st_main_python(d):
    st.title(f'⚙️Electric Machinery Simulation Visualization | Python')

    # Divide tabs
    Main_tab, Ep6_tab, Bode_tab, Sweep_tab, Hit_tab = st.tabs(
        ["Main", "Ep9", "Bode Plot", "Sweep", "Hit Wall Plot"])

    # Simulation
    simulation, gdd, global_machine_times = cpt.begin_simulation(d, acmsimpy)

    # Basic fig plot. You can save the fig after fig generation. eg:
    fig = cpt.example_plot(gdd, global_machine_times)
    cpt.example_plot_table(gdd, global_machine_times, d, Main_tab, fig)
    # plot in Main tab
    cpt.example_fig_show(fig, Main_tab, 'data/user_image_data/basic.png')

    # Save data
    cpt.component_save_gdd_data(gdd, global_machine_times)  # save gdd data
    cpt.component_save_sweeping_data(
        d, gdd, global_machine_times)  # save sweeping data

    cpt.show_para()
    cpt.init_ep9_plot(d, Ep6_tab, nplot_main)
    cpt.init_bode_plot(Bode_tab)
    cpt.init_run_sweep(Sweep_tab)
    cpt.init_HitWall_plot(Hit_tab)
    st.subheader('Session state console')
    cpt.init_session_state_console()
    cpt.save_user_config_to_json()
    print('Finished')

    # User custom functions
    usm.user_python_main(d)

# C main function
def st_main_c(d):
    st.title(f'⚙️Electric Machinery Simulation Visualization | C')

    # 显示侧边栏各种可调参数等
    cpt.show_para()

    # 编译C代码、运行可执行文件main.exe生成数据
    cptc.init_save_to_c_and_run(d)

    # 画图，仿真结果可视化
    st.subheader('C simulation for ' + d['name'])
    cptc.init_show_c_simulation()

    st.write('For interactive visualization, please execute the following python snippets:.............')

    # User custom functions
    usm.user_c_main(d)

import yaml

if __name__ == '__main__':
    st.set_page_config(layout="wide")

    print('\n'+'-*'*30)

    config.streamlit_gui_config()
    user_selected_mode = cpt.user_selected_mode()
    user_history = cpt.get_user_history()

    with open(os.path.dirname(__file__)+'/user_plot_config.yaml', encoding='utf-8') as f:
        user_plot_config = yaml.load(f, Loader=yaml.FullLoader)

    d_user_input_motor_dict, d_motors, user_selected_motor, user_motor = cpt.option_select_motor(user_history, user_plot_config)

    # d_user_input_motor_dict = usm.user_pre_process(d_user_input_motor_dict)

    if user_selected_mode == 'Python':
        st_main_python(d_user_input_motor_dict)
    elif user_selected_mode == 'C':
        st_main_c(d_user_input_motor_dict)
