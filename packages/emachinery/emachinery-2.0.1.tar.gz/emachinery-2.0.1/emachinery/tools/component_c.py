import streamlit as st
import os
import ACMParam
import cplot

################################### Save to C ########################################################

def init_save_to_c_and_run(d):
    path2acmsimc = f'{os.path.dirname(__file__)}/../acmsimcv5/c/ACMParam.h'
    path2xlsx = f'{os.path.dirname(__file__)}/../jsons/ACMParam.xlsx'
    acm = ACMParam.ACMParam(path2acmsimc, path2xlsx)
    acm.readDict(d)
    with st.sidebar:
        st.markdown('---')
        st.warning('请小心使用这个功能，可能会造成ACMParam.h文件出错!!!', icon="⚠️")
        st.button('Save to C and compile', on_click=acm.updateACMParamAndRun, type="secondary", use_container_width=True)
    #                                               运行编译C代码的函数在这里^

def init_show_c_simulation():
    st.info("运行下列命令可视化画图", icon="ℹ️")
    st.info("python main.py cplot "+st.session_state.user_selected_motor, icon="ℹ️")
    figs = cplot.main(st.session_state.user_selected_motor)
    
    for fig in figs:
        st.pyplot(fig)
