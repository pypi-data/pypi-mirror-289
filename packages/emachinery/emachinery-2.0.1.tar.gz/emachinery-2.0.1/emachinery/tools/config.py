import streamlit as st
import os
import json
from pylab import np, plt, mpl, fft

def side_bar_config():
    # side bar appearance settings
    with st.sidebar:
        st.markdown(
            """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"]{
            min-width: 450px;
            max-width: 1450px;
        }
        """,
            unsafe_allow_html=True,
        )
    return

# def set_custom_plot_style():
#     # 风格
#     # further customize: https://stackoverflow.com/questions/35223312/matplotlib-overriding-ggplot-default-style-properties and https://matplotlib.org/2.0.2/users/customizing.html
#     mpl.style.use('ggplot')
#     plt.style.use("dark_background")
#     mpl.style.use('grayscale')
#     mpl.style.use('classic')

#     # 字体
#     mpl.rcParams['mathtext.fontset'] = 'stix'
#     mpl.rcParams['font.family'] = 'STIXGeneral'
#     # bold is 700, normal is 400, see https://matplotlib.org/2.0.2/users/customizing.html
#     plt.rcParams['font.weight'] = '900'
#     # 13 is too big, commenting out is too small
#     plt.rcParams['font.size'] = 12

#     # 颜色设置壹/叁
#     # https://matplotlib.org/2.0.2/users/customizing.html from https://stackoverflow.com/questions/35223312/matplotlib-overriding-ggplot-default-style-properties
#     plt.rcParams['axes.labelsize'] = 14   # 'medium' # 'large'是没用的！
#     hex_monokai = '#272822'
#     hex_wanderson = '#3d444c'
#     # also need to change facecolor in mplwidget.py to get a consistent look
#     plt.rcParams['axes.facecolor'] = hex_wanderson
#     plt.rcParams['axes.labelcolor'] = '#d5d1c7'  # tint grey
#     plt.rcParams['axes.axisbelow'] = 'False'   # 'line'
#     plt.rcParams['ytick.color'] = '#d5d1c7'  # 'white'
#     plt.rcParams['xtick.color'] = '#d5d1c7'  # 'white'
#     plt.rcParams['text.color'] = '#d5d1c7'  # 'white'
#     plt.rcParams['grid.color'] = '#d5d1c7'  # grid color
#     plt.rcParams['grid.linestyle'] = '--'      # solid
#     plt.rcParams['grid.linewidth'] = 0.3       # in points
#     plt.rcParams['grid.alpha'] = 0.8       # transparency, between 0.0 and 1.0

def streamlit_gui_config():
    side_bar_config()
