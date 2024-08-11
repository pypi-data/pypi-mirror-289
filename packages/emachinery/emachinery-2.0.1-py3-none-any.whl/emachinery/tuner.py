# -*- coding: utf-8 -*-
from pylab import np, plt, mpl
import control

def getBodePlot(CLBW_Hz, currentKp, currentKi, speedKi, speedKp, L, KT, npp, Js, bool_render=False, st=None):

    # Transfer functions
    Gi_closed = control.tf([1], [L/currentKp, 1]) # current loop zero-pole cancelled already
    dc_motor_motion = control.tf([KT*npp/Js], [1, 0])
    speedRegulator = control.tf([speedKp, speedKp*speedKi], [1, 0])
    Gw_open = dc_motor_motion * Gi_closed * speedRegulator

    # C2C
    if bool_render: fig = plt.figure(101)
    c2c_tf = Gi_closed
    mag, phase, omega = control.bode_plot(c2c_tf, 2*np.pi*np.logspace(0,4,500), dB=1, Hz=1, deg=1, lw='0.5', label=f'{CLBW_Hz:g=} Hz', plot=bool_render)
    CLBW_Hz_BodePlot = omega[(np.abs(mag-0.707)).argmin()]/2/np.pi
    C2C_designedMagPhaseOmega = mag, phase, omega

    # C2V
    if bool_render: fig = plt.figure(102)
    c2v_tf = dc_motor_motion * Gi_closed
    mag, phase, omega = control.bode_plot(c2v_tf, 2*np.pi*np.logspace(0,4,500), dB=1, Hz=1, deg=1, lw='0.5', label=f'{CLBW_Hz:g=} Hz', plot=bool_render)
    openVL_cutoff_frequency_Hz = omega[(np.abs(mag-1.0)).argmin()]/2/np.pi
    C2V_designedMagPhaseOmega = mag, phase, omega

    # V2V
    if bool_render: fig = plt.figure(103)
    Gw_closed = Gw_open / (1+Gw_open)
    mag, phase, omega = control.bode_plot(Gw_closed, 2*np.pi*np.logspace(0,4,500), dB=1, Hz=1, deg=1, lw='0.5', label=f'Velocity', plot=bool_render)
    VLBW_Hz = omega[(np.abs(mag-0.707)).argmin()]/2/np.pi
    V2V_designedMagPhaseOmega = mag, phase, omega
    # plt.close(fig)

    # print(f'{CLBW_Hz_BodePlot=}; {CLBW_Hz=}; {openVL_cutoff_frequency_Hz=}; {VLBW_Hz=}')
    output = {
        'CLBW_Hz_BodePlot': CLBW_Hz_BodePlot,
        'openVL_cutoff_frequency_Hz': openVL_cutoff_frequency_Hz,
        'VLBW_Hz': VLBW_Hz,
    }
    return  (mag, phase, omega), VLBW_Hz, output

def InstaSPIN_series_PI_tuner(
    delta,
    CLBW_Hz,
    Ld,Lq,R,Js,npp,KE,
    bool_render=False):
    speedKFB = 0
    KT = 1.5*npp*KE
    d_currentKp = CLBW_Hz * 2 * np.pi * Ld
    d_currentKi = R / Ld
    q_currentKp = CLBW_Hz * 2 * np.pi * Lq
    q_currentKi = R / Lq
    speedKi = 2*np.pi * CLBW_Hz / delta**2 # THIS IS INTEGRAL GAIN

    # 这里不需要npp
    # 这里不需要npp
    # 这里不需要npp
    speedKp = delta * speedKi / KT * Js 
    (mag, phase, omega), VLBW_Hz, output = getBodePlot(CLBW_Hz, q_currentKp, q_currentKi, speedKi, speedKp, Lq, KT, npp, Js, bool_render=bool_render)
    input = {
        'delta': delta,
        'CLBW_Hz': CLBW_Hz,
        'Ld': Ld,
        'Lq': Lq,
        'R': R,
        'Js': Js,
        'npp': npp,
        'KE': KE,
    }
    return VLBW_Hz, d_currentKp, d_currentKi, q_currentKp, q_currentKi, speedKp, speedKi, speedKFB, (mag, phase, omega), input, output


def WC_tuner(
zeta, omega_n, 
max_CLBW_PER_min_CLBW,
Ld,Lq,R,Js,npp,KE):
    # motor parameters
    KT = 1.5 * npp * KE # torque constant
    K0 = KT / Js # motor constant

    # 要在这TM更新带宽啊
    # 要在这TM更新带宽啊
    # 要在这TM更新带宽啊
    max_CLBW = zeta * omega_n * 4
    min_CLBW = zeta * omega_n * 2
    
    if max_CLBW_PER_min_CLBW > 1:
        raise ValueError('max_CLBW_PER_min_CLBW > 1 change change it !?')
    else:
        # 通过一个小于1的比例系数来选取电流环带宽
        FOC_CLBW = max_CLBW_PER_min_CLBW * max_CLBW + (1-max_CLBW_PER_min_CLBW) * min_CLBW
    
    # current loop
    d_currentKp = FOC_CLBW * Ld
    d_currentKi = R / Ld

    q_currentKp = FOC_CLBW * Lq
    q_currentKi = R / Lq
    
    # speed loop
    speedKp  = omega_n**2 / (FOC_CLBW * K0)
    speedKFB = (2*zeta*omega_n*FOC_CLBW - 4*zeta**2*omega_n**2) / (FOC_CLBW*K0) 
    speedKi = (FOC_CLBW - np.sqrt(FOC_CLBW**2 - 4*FOC_CLBW*K0*speedKFB)) * 0.5
    # if FOC_CLBW - 4 * K0 * speedKFB:
    #     raise ValueError('can not do zero-pole cancellation')
    # else:
    #     raise ValueError('can do a zero-pole cancellation')

    # 这里(mag, phase, omega), input, output先不要！！！
    return d_currentKp, d_currentKi, q_currentKp, q_currentKi, speedKp, speedKi, speedKFB


if __name__ == '__main__':
    InstaSPIN_series_PI_tuner(5, 100, 5e-3, 1.1, 0.006, 4, 0.09, bool_render=True)
    plt.show()

