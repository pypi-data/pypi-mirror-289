// This header file is automatically generated. Any modification to this file will get lost.
#ifndef ACMParam_H
#define ACMParam_H

#define INIT_NPP 5
#define INIT_IN 16.8
#define INIT_R 0.044
#define INIT_LD 0.00019
#define INIT_LQ 0.00019
#define INIT_KE 0.01717
#define INIT_KA 0.01717
#define INIT_RREQ FALSE
#define INIT_JS 0.000755295972
#define DC_BUS_VOLTAGE 48
#define CL_TS 0.0001
#define VL_EXE_PER_CL_EXE 5
#define MACHINE_SIMULATIONS_PER_SAMPLING_PERIOD TRUE
#define TIME_SLICE 0.02
#define NUMBER_OF_SLICES 6
#define ZETA 0.5
#define OMEGA_N 2500
#define MAX_CLBW_PER_MIN_CLBW 0.5
#define CTRL_CMD_SPEED_SINE_RPM 50
#define CTRL_CMD_CURRENT_SINE_AMPERE TRUE
#define CTRL_BOOL_SWEEPING_FREQUENCY_FOR_SPEED_LOOP TRUE
#define CTRL_BOOL_APPLY_SWEEPING_FREQUENCY_EXCITATION FALSE
#define CTRL_BOOL_APPLY_WC_TUNNER_FOR_SPEED_LOOP TRUE
#define CTRL_BOOL_APPLY_SPEED_CLOSED_LOOP_CONTROL TRUE
#define CTRL_BOOL_APPLY_DECOUPLING_VOLTAGES_TO_CURRENT_REGULATION FALSE
#define CTRL_BOOL_OVERWRITE_SPEED_COMMANDS TRUE
#define CTRL_BOOL_ZERO_ID_CONTROL TRUE
#define FOC_DELTA 10
#define FOC_CLBW_HZ 800
#define FOC_DESIRED_VLBW_HZ 120
#define FOC_CL_KI_FACTOR_WHEN__BOOL_APPLY_DECOUPLING_VOLTAGES_TO_CURRENT_REGULATION__IS_FALSE 10
#define CL_SERIES_KP_Q 0.5969026041820606
#define CL_SERIES_KI_Q 231.578947368421
#define VL_SERIES_KP 1.8426187357182389
#define VL_SERIES_KI 31.415926535897928
#define CL_SERIES_KP_D 0.5969026041820606
#define CL_SERIES_KI_D 231.578947368421
#define VL_FEEDBACK_KFB None
#define VL_LIMIT_OVERLOAD_FACTOR 3.0
#define DISP_KP FALSE
#define DISP_KI FALSE
#define DISP_KD FALSE
#define DISP_TAU FALSE
#define DISP_OUTLIMIT FALSE
#define DISP_INTLIMIT FALSE



#define DATA_FORMAT "%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g,%g\n"
#define DATA_LABELS "ACM.theta_d_activeFlux/M_PI*180,ACM.x[3]/M_PI*180,ACM.ual,ACM.ube,ACM.rpm_cmd,(*CTRL).I->rpm,(*CTRL).O->udq_cmd[0],(*CTRL).O->udq_cmd[1],(*CTRL).I->idq_cmd[1],(*CTRL).I->idq[1],(*CTRL).I->idq_cmd[0],(*CTRL).I->idq[0],ACM.TLoad,ACM.Tem,ACM.rpm_cmd,(*CTRL).O->uab_cmd_to_inverter[0],(*CTRL).O->uab_cmd_to_inverter[1]\n"
#define DATA_DETAILS ACM.theta_d_activeFlux/M_PI*180,ACM.x[3]/M_PI*180,ACM.ual,ACM.ube,ACM.rpm_cmd,(*CTRL).I->rpm,(*CTRL).O->udq_cmd[0],(*CTRL).O->udq_cmd[1],(*CTRL).I->idq_cmd[1],(*CTRL).I->idq[1],(*CTRL).I->idq_cmd[0],(*CTRL).I->idq[0],ACM.TLoad,ACM.Tem,ACM.rpm_cmd,(*CTRL).O->uab_cmd_to_inverter[0],(*CTRL).O->uab_cmd_to_inverter[1]


#define DATA_FILE_NAME "../dat/MD1-08075AC30BB0L1.dat"

#endif // ACMParam_H
