#include "ACMSim.h"

#define INCREMENTAL_PID TRUE
#if INCREMENTAL_PID
    // void PID_calc(st_pid_regulator *r){

    //     r->Err = r->Ref - r->Fbk;
    //     r->Out = r->OutPrev \
    //             + r->Kp * ( r->Err - r->ErrPrev ) + r->Ki * r->Err;

    //     if(r->Out > r->OutLimit)
    //         r->Out = r->OutLimit;
    //     else if(r->Out < -r->OutLimit)
    //         r->Out = -r->OutLimit;

    //     r->ErrPrev = r->Err; 
    //     r->OutPrev = r->Out;
    // }
    void PID_calc(st_pid_regulator *r){

        // 打印 r->Kp 的值
        // printf("Value of r->Kp: %f\n", r->Kp);
        // printf("Value of r->Ki: %f\n", r->Ki);
        // printf("Value of r->Ref: %f\n", r->Ref);

        r->Err = r->Ref - r->Fbk;

        r->Out = r->OutPrev + \
                r->Kp * ( r->Err - r->ErrPrev ) + \
                r->Ki * r->Err;

        r->ErrPrev = r->Err; 
        r->OutPrev = r->Out;

        r->KFB_Term = r->KFB * r->Fbk;
        r->Out -= r->KFB_Term;

        if(r->Out > r->OutLimit)
            r->Out = r->OutLimit;
        else if(r->Out < -r->OutLimit)
            r->Out = -r->OutLimit;
        // printf("KFB is %f\n", r->KFB);
    }
#else
    void PID_calc(st_pid_regulator *r){
        #define DYNAMIC_CLAPMING TRUE
        #define DYNAMIC_CLAPMING_WUBO FALSE

        // 误差
        r->Err = r->Ref - r->Fbk;

        // 比例
        r->P_Term = r->Err * r->Kp;

        // 积分
        r->I_Term += r->Err * r->Ki;
        r->OutNonSat = r->I_Term;

        // Inner Loop
        r->KFB_Term = r->KFB * r->Fbk;

        // 添加积分饱和特性
        #if DYNAMIC_CLAPMING
            #if DYNAMIC_CLAPMING_WUBO
                // dynamic clamping wubo
                if( r->I_Term > r->OutLimit - r->P_Term)
                    r->I_Term = r->OutLimit - r->P_Term;
                else if( r->I_Term < -r->OutLimit + r->P_Term)
                    r->I_Term =      -r->OutLimit + r->P_Term; // OutLimit is a positive constant
           #else
                // dynamic clamping
                if( r->I_Term > r->OutLimit - r->Out)
                    r->I_Term = r->OutLimit - r->Out;
                else if( r->I_Term < -r->OutLimit + r->Out)
                    r->I_Term =      -r->OutLimit + r->Out; // OutLimit is a positive constant
            #endif
        #else
            // static clamping
            if( r->I_Term > r->OutLimit)
                r->I_Term = r->OutLimit; 
            else if( r->I_Term < -r->OutLimit)
                r->I_Term = -r->OutLimit;
        #endif

        // 微分
        // r->D_Term = r->Kd * (r->Err - r->ErrPrev);

        // 输出
        r->Out = r->I_Term + r->P_Term - r->KFB_Term; // + r->D_Term
        r->OutNonSat += r->P_Term; // + r->D_Term
        // 输出限幅
        if(r->Out > r->OutLimit)
            r->Out = r->OutLimit;
        else if(r->Out < -r->OutLimit)
            r->Out = -r->OutLimit;

        // 当前步误差赋值为上一步误差
        r->ErrPrev = r->Err;
        // 记录饱和输出和未饱和输出的差
        r->SatDiff = r->Out - r->OutNonSat;
    }
#endif


void PIDController_Init(st_PIDController *pid) {

    /* Clear controller variables */
    pid->integrator = 0.0f;
    pid->prevError  = 0.0f;

    pid->differentiator  = 0.0f;
    pid->prevMeasurement = 0.0f;

    pid->out = 0.0f;
}

float PIDController_Update(st_PIDController *pid) {

    // * Error signal
    float error = pid->setpoint - pid->measurement;

    // * Proportional   
    float proportional = pid->Kp * error;

    // * Integral
    pid->integrator = pid->integrator + 0.5f * pid->Ki * pid->Ts * (error + pid->prevError);

    /* Anti-wind-up via integrator clamping */
    if (pid->integrator > pid->intLimit) {
        pid->integrator = pid->intLimit;
    } else if (pid->integrator < -pid->intLimit) {
        pid->integrator = -pid->intLimit;
    }

    // * Derivative (band-limited differentiator)       
    pid->differentiator = -(2.0f * pid->Kd * (pid->measurement - pid->prevMeasurement)   /* Note: derivative on measurement, therefore minus sign in front of equation! */
                        + (2.0f * pid->tau - pid->Ts) * pid->differentiator)
                        / (2.0f * pid->tau + pid->Ts);

    // * Compute output and apply limits
    pid->out = proportional + pid->integrator + pid->differentiator;
    if (pid->out > pid->outLimit) {
        pid->out = pid->outLimit;
    } else if (pid->out < -pid->outLimit) {
        pid->out = -pid->outLimit;
    }

    /* Store error and measurement for later use */
    pid->prevError       = error;
    pid->prevMeasurement = pid->measurement;

    /* Return controller output */
    return pid->out;
}


// 初始化函数
void ACMSIMC_PIDTuner(){

    pid1_iM.Kp  = CL_SERIES_KP_D;
    pid1_iT.Kp  = CL_SERIES_KP_Q;
    pid1_spd.Kp = VL_SERIES_KP;

    pid1_iM.Ki  = CL_SERIES_KI_D_CODE;
    pid1_iT.Ki  = CL_SERIES_KI_Q_CODE;
    pid1_spd.Ki = VL_SERIES_KI_CODE;

    pid1_spd.KFB = SPEED_KFB;

    pid1_iM.OutLimit  = CURRENT_LOOP_LIMIT_VOLTS;
    pid1_iT.OutLimit  = CURRENT_LOOP_LIMIT_VOLTS;
    pid1_spd.OutLimit = SPEED_LOOP_LIMIT_AMPERE;

    #if PC_SIMULATION
        printf("pid1_iM.Kp = %f\n", pid1_iM.Kp);
        printf("pid1_iT.Kp = %f\n", pid1_iT.Kp);
        printf("pid1_spd.Kp = %f\n", pid1_spd.Kp);

        printf("pid1_iM.Ki = %f\n", pid1_iM.Ki);
        printf("pid1_iT.Ki = %f\n", pid1_iT.Ki);
        printf("pid1_spd.Ki = %f\n", pid1_spd.Ki);
    #endif

    // pid2_ix.Kp = CURRENT_KP;
    // pid2_iy.Kp = CURRENT_KP;
    // pid2_ix.Ki = CURRENT_KI_CODE;
    // pid2_iy.Ki = CURRENT_KI_CODE;
    // pid2_ix.OutLimit = CURRENT_LOOP_LIMIT_VOLTS;
    // pid2_iy.OutLimit = CURRENT_LOOP_LIMIT_VOLTS;

    // PIDController_Init(&pid1_dispX);
    // PIDController_Init(&pid1_dispY);

        // #define DISPLACEMENT_KP 0
        // #define DISPLACEMENT_KI_CODE 0
        // #define DISPLACEMENT_LOOP_LIMIT_AMPERE 0

        // pid1_disX.Kp       = DISPLACEMENT_KP;
        // pid1_disY.Kp       = DISPLACEMENT_KP;
        // pid1_disX.Ki       = DISPLACEMENT_KI_CODE;
        // pid1_disY.Ki       = DISPLACEMENT_KI_CODE;
        // pid1_disX.OutLimit = DISPLACEMENT_LOOP_LIMIT_AMPERE;
        // pid1_disY.OutLimit = DISPLACEMENT_LOOP_LIMIT_AMPERE;

        // pid1_ia.Kp = CURRENT_KP;
        // pid1_ib.Kp = CURRENT_KP;
        // pid1_ic.Kp = CURRENT_KP;
        // pid1_ia.Ki = CURRENT_KI_CODE;
        // pid1_ib.Ki = CURRENT_KI_CODE;
        // pid1_ic.Ki = CURRENT_KI_CODE;
        // pid1_ia.OutLimit = CURRENT_LOOP_LIMIT_VOLTS;
        // pid1_ib.OutLimit = CURRENT_LOOP_LIMIT_VOLTS;
        // pid1_ic.OutLimit = CURRENT_LOOP_LIMIT_VOLTS;
}

struct SweepFreq sf={0.0, 1, SWEEP_FREQ_INIT_FREQ-1, 0.0, 0.0};
