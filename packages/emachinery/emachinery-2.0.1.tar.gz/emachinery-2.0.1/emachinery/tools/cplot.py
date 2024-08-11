import os
import re
import yaml
import pandas as pd
from pylab import np, plt, mpl

def load_yaml():
    with open(os.path.dirname(__file__)+'/../user_plot_config.yaml', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config

def main(motor_type):
    user_plot_config = load_yaml()
    base_path = os.path.dirname(__file__)+"/../acmsimcv5"

    # 风格
    # further customize: https://stackoverflow.com/questions/35223312/matplotlib-overriding-ggplot-default-style-properties and https://matplotlib.org/2.0.2/users/customizing.html
    mpl.style.use('ggplot')
    # plt.style.use("dark_background")
    # mpl.style.use('grayscale')
    # mpl.style.use('classic')

    # 字体
    for key, value in user_plot_config['config']['mpl'].items():
        mpl.rcParams[key] = value
    for key, value in user_plot_config['config']['plt'].items():
        plt.rcParams[key] = value

    # 实用函数
    import subprocess

    def subprocess_cmd(command_string, bool_run_parallel=False):
        process = subprocess.Popen(
            command_string, stdout=subprocess.PIPE, shell=True)
        if not bool_run_parallel:
            streamdata = proc_stdout = process.communicate()[0].strip()
            print(proc_stdout)
        return process

    def cyclic_generator(list_of_things):
        N, i = len(list_of_things), 0
        while True:
            yield list_of_things[i]
            i += 1
            if i > (N-1):
                i = 0

    # 画图风格
    cjh_linestyles = [
        '-', '--', (0, (3, 1, 1, 1)), ':', '-.',
        '-', '--', (0, (3, 1, 1, 1)), ':', '-.',
        '-', '--', (0, (3, 1, 1, 1)), ':', '-.',
    ]
    cjh_linestyle = cyclic_generator(cjh_linestyles)
    # 颜色设置叁/叁
    cjh_colors = user_plot_config['config']['cjh_colors']
    cjh_color = cyclic_generator(cjh_colors)
    # 注意，不可以做 list(self.cjh_color)，因为这是一个无止境循环的发生器，会卡住的。。。

    # 读取数据
    if not os.path.exists(base_path+'/dat'):
        os.makedirs(base_path+'/dat')
    data_file_name = base_path+'/dat/'+str(motor_type)+'.dat'
    if not os.path.exists(data_file_name):
        print(
            f"Data file {data_file_name} does not exist. Please run main first!")
        return []
    with open(data_file_name, 'r') as f:
        if not f.read():
            print(
                f"Data file {data_file_name} is empty. Please run main first!")
            return []
    df_profiles = pd.read_csv(data_file_name, na_values=['1.#QNAN', '-1#INF00', '-1#IND00'])
    no_samples = df_profiles.shape[0]
    no_traces = df_profiles.shape[1]

    DOWN_SAMPLE = 1
    CL_TS = 1e-4
    time = np.arange(1, no_samples+1) * DOWN_SAMPLE * CL_TS

    trace_counter = 0
    fig, axs = plt.subplots(len(user_plot_config['cplot']['subplot']), 1, figsize=(
        user_plot_config['cplot']['width'], user_plot_config['cplot']['height']*len(user_plot_config['cplot']['subplot'])), facecolor='#3d444c')

    for subplot_config in user_plot_config['cplot']['subplot']:

        ax = axs[user_plot_config['cplot']['subplot'].index(subplot_config)]

        for subplot_signal_index in range(len(subplot_config['y'])):
            trace_counter += 1
            if subplot_config['y'][subplot_signal_index]['y_data'] not in df_profiles.keys():
                print(f"Warning: cannot find signal {subplot_config['y'][subplot_signal_index]['y_data']} in the signal library, check your DATA_LABELS.")
            else:
                signal = df_profiles[ subplot_config['y'][subplot_signal_index]['y_data'] ]
                ax.plot(time, signal,
                        linestyle=cjh_linestyles[subplot_signal_index],
                        color=cjh_colors[subplot_signal_index], lw=1.5,
                        label=subplot_config['y'][subplot_signal_index]['y_label'],
                        alpha=0.5, zorder=100-trace_counter)  # 如果是减去trace_counter，那么就是后来的画在下面
        ax.set_ylabel(subplot_config['y_title'])
        ax.set_title(subplot_config['title'])
        ax.legend(loc='lower right').set_zorder(202)
    return [fig]

if __name__ == "__main__":
    main('TEST_PHIL_LAB_PID_CODES-0-0-0-0')
    plt.show()
