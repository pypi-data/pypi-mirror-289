#include "ACMSim.h"


// 定义特定的测试指令，如快速反转等
void cmd_fast_speed_reversal(REAL timebase, REAL instant, REAL interval, REAL rpm_cmd){
    if(timebase > instant+2*interval){
        ACM.rpm_cmd = 1*1500 + rpm_cmd;
    }else if(timebase > instant+interval){
        ACM.rpm_cmd = 1*1500 + -rpm_cmd;
    }else if(timebase > instant){
        ACM.rpm_cmd = 1*1500 + rpm_cmd;
    }else{
        ACM.rpm_cmd = 20; // default initial command
    }
}

REAL short_stopping_at_zero_speed(){
    static REAL set_rpm_speed_command=0.0;

    #define RPM1 100
    #define BIAS 0
    if((*CTRL).timebase<1){ // note 1 sec is not enough for stator flux to reach steady state.
        set_rpm_speed_command = 0;
    }else if((*CTRL).timebase<5){
        set_rpm_speed_command = RPM1;
    }else if((*CTRL).timebase<10){
        set_rpm_speed_command += CL_TS * -50;
        if(set_rpm_speed_command < 0){
            set_rpm_speed_command = 0.0;
        }
    }else if((*CTRL).timebase<15){
        set_rpm_speed_command += CL_TS * -50;
        if(set_rpm_speed_command<-RPM1){
            set_rpm_speed_command = -RPM1;
        }
    }else if((*CTRL).timebase<20){
        set_rpm_speed_command += CL_TS * +50;
        if(set_rpm_speed_command > 0){
            set_rpm_speed_command = 0.0;
        }
    }else if((*CTRL).timebase<25){
        set_rpm_speed_command += CL_TS * +50;
        if(set_rpm_speed_command>RPM1){
            set_rpm_speed_command = RPM1;
        }
    }

    return set_rpm_speed_command;
    #undef RPM1
    #undef BIAS
}

REAL slow_speed_reversal(REAL slope){ // slope = 20 rpm/s, 50 rpm/s
    static REAL set_rpm_speed_command=0.0;

    #define RPM1 100
    #define BIAS 0
    if((*CTRL).timebase<0.5){ // note 1 sec is not enough for stator flux to reach steady state.
        set_rpm_speed_command = 0;
    }else if((*CTRL).timebase<1){
        set_rpm_speed_command = -50;
    }else if((*CTRL).timebase<4){
        set_rpm_speed_command = RPM1+50;
    }else if((*CTRL).timebase<15){
        set_rpm_speed_command += CL_TS * -slope;
        if(set_rpm_speed_command<-RPM1){
            set_rpm_speed_command = -RPM1;
        }
    }else if((*CTRL).timebase<25){
        set_rpm_speed_command += CL_TS * +slope;
        if(set_rpm_speed_command>RPM1){
            set_rpm_speed_command = RPM1;
        }
    }

    if((*CTRL).timebase>25 && (*CTRL).timebase<35){
        set_rpm_speed_command = RPM1*2;
    }

    return set_rpm_speed_command;
    #undef RPM1
    #undef BIAS
}

REAL low_speed_operation(){
    REAL set_rpm_speed_command;

    #define RPM1 200
    #define BIAS 50
    if((*CTRL).timebase<1){ // note 1 sec is not enough for stator flux to reach steady state.
        set_rpm_speed_command = RPM1;
    }else if((*CTRL).timebase<3){
        set_rpm_speed_command = RPM1 + BIAS;
    }else if((*CTRL).timebase<6+BIAS){
        set_rpm_speed_command = -RPM1;
    }else if((*CTRL).timebase<9+BIAS){
        set_rpm_speed_command = 10;
    }else if((*CTRL).timebase<12+BIAS){
        set_rpm_speed_command = RPM1*sin(20*2*M_PI*(*CTRL).timebase);
    }

    return set_rpm_speed_command;
    #undef RPM1
    #undef BIAS
}

REAL high_speed_operation(){
    REAL set_rpm_speed_command;

    #define RPM1 1500
    #define BIAS 0
    if((*CTRL).timebase<1){ // note 1 sec is not enough for stator flux to reach steady state.
        set_rpm_speed_command = 0;
    }else if((*CTRL).timebase<4){
        set_rpm_speed_command = RPM1;
    }else if((*CTRL).timebase<6+BIAS){
        set_rpm_speed_command = -RPM1;
    }else if((*CTRL).timebase<9+BIAS){
        set_rpm_speed_command = 10;
    }else if((*CTRL).timebase<12+BIAS){
        set_rpm_speed_command = RPM1*sin(2*2*M_PI*(*CTRL).timebase);
    }

    return set_rpm_speed_command;
    #undef RPM1
    #undef BIAS
}

// declared in pid_regulator.h
extern struct SweepFreq sf;
void commands(REAL *p_set_rpm_speed_command, REAL *p_set_iq_cmd, REAL *p_set_id_cmd,
                    int *p_set_current_loop, int *p_flag_overwrite_theta_d, REAL *p_Overwrite_Current_Frequency){
    #define set_rpm_speed_command (*p_set_rpm_speed_command)
    #define set_iq_cmd (*p_set_iq_cmd)
    #define set_id_cmd (*p_set_id_cmd)
    #define set_current_loop (*p_set_current_loop) // 0: Dual Loop 1: Speed Loop
    #define flag_overwrite_theta_d (*p_flag_overwrite_theta_d)
    #define Overwrite_Current_Frequency (*p_Overwrite_Current_Frequency)

    // 测试
    // set_rpm_speed_command = 50;
    // set_current_loop = 1;
    // set_iq_cmd = 1;
    // set_rpm_speed_command = 200;
    // return;

    // if (set_current_loop == 1){
    //     set_iq_cmd = 4; // unit: Ameper
    //     set_id_cmd = 0;
    // }

    // 调节励磁
    #if CONTROL_STRATEGY == NULL_D_AXIS_CURRENT_CONTROL
        set_id_cmd = 0.0;
    #else
        set_id_cmd = 0.0;
    #endif

    // 位置环 in rad
    #if EXCITATION_TYPE == 0
        REAL position_command = 10*M_PI;
        if((*CTRL).timebase>5){
            position_command = -10*M_PI;
        }
        REAL position_error = position_command - ACM.theta_d_accum;
        REAL position_KP = 8;
        REAL rad_speed_command = position_KP*position_error;
        set_rpm_speed_command = rad_speed_command*ELEC_RAD_PER_SEC_2_RPM;
    #endif

    // 扫频建模
    #if EXCITATION_TYPE == 2
        REAL amp_current_command;
        sf.time += CL_TS;
        if(sf.time > sf.current_freq_end_time){
            // next frequency
            sf.current_freq += sf.freq_step_size;
            // next end time
            sf.last_current_freq_end_time = sf.current_freq_end_time;
            sf.current_freq_end_time += 1.0/sf.current_freq; // 1.0 Duration for each frequency
        }
        if(sf.current_freq > SWEEP_FREQ_MAX_FREQ){
            set_rpm_speed_command = 0.0;
            amp_current_command = 0.0;
        }else{
            // # closed-cloop sweep
            set_rpm_speed_command   = SWEEP_FREQ_VELOCITY_AMPL * sin(2*M_PI*sf.current_freq*(sf.time - sf.last_current_freq_end_time));

            // open-loop sweep
            amp_current_command = SWEEP_FREQ_CURRENT_AMPL * sin(2*M_PI*sf.current_freq*(sf.time - sf.last_current_freq_end_time));
        }
        set_iq_cmd = amp_current_command;   
    #endif

    // 转速运动模式 in rpm
    #if EXCITATION_TYPE == 1
        /* Preset */
        // set_rpm_speed_command = low_speed_operation();
        // set_rpm_speed_command = high_speed_operation();
        //set_rpm_speed_command = slow_speed_reversal(50); // 20
        
        // set_rpm_speed_command = short_stopping_at_zero_speed();

        /* Custom */
        if((*CTRL).timebase < 0.5)
        {
            set_rpm_speed_command = 50;
        }
        else if((*CTRL).timebase < 1)
        { 
            set_rpm_speed_command = 200;
        }
        else if((*CTRL).timebase < 2)
        { 
            set_rpm_speed_command = 200;
        }
    #endif
}



double load_model(){
    static double Tload = 0.0;

    // Tload = 0.0001 * ACM.rpm + 0.002 * cos(3*ACM.x[3]); // this load causes zero speed oscillation in controller 
    // Tload = 0.005*sign(ACM.rpm);
    // Tload = LOAD_TORQUE*sign(ACM.rpm) + 0*sin(2*M_PI*1*ACM.timebase);

    static int load_state = 0;

    static double dc_part = LOAD_TORQUE;
    static double viscous_part = 0.0; // 这个变量去到Config文件里面了

    if(FALSE){
        if((*CTRL).timebase>40.0)
        {
            dc_part = LOAD_TORQUE*2;
        }
        else if((*CTRL).timebase>35.0)
        {
            dc_part = 0.2*LOAD_TORQUE;
        }
        else if((*CTRL).timebase>30.0)
        {
            dc_part = 0.6*LOAD_TORQUE;
        }
        else if((*CTRL).timebase>25.0)
        {
            dc_part = LOAD_TORQUE;
        }
        else if((*CTRL).timebase>12.0)
        {
            dc_part = LOAD_TORQUE*2;
        }
        else if((*CTRL).timebase>3)
        {
            dc_part = LOAD_TORQUE;
        }
        else if((*CTRL).timebase>1)
        {
            dc_part = 0;
            // if(fabs(ACM.rpm)>10 && load_state==0)
            // {
            //     load_state = 1;
            //     dc_part = LOAD_TORQUE;
            //     // dc_part = LOAD_TORQUE*sign(ACM.rpm);
            //     // dc_part = - LOAD_TORQUE*sign(ACM.rpm);
            // }
            // else if(fabs(ACM.rpm)<-10 && load_state==1)
            // {
            //     load_state = 0;
            //     // TODO this is not reached?!
            //     dc_part = 99999* LOAD_TORQUE*sign(ACM.rpm);
            // }
        }        
    }

    viscous_part = VISCOUS_COEFF*ACM.rpm*RPM_2_ELEC_RAD_PER_SEC;
    Tload = dc_part + viscous_part;

    // Tload = -sign(ACM.rpm) * Tload;

    #if ENABLE_COMMISSIONING
        Tload = 0.0;
    #endif

    // Tload = 2;

    // printf("%g, %g, %g\n", Tload, LOAD_TORQUE*sign(ACM.rpm), VISCOUS_COEFF*ACM.rpm*RPM_2_ELEC_RAD_PER_SEC);

    // Tload = 0.0;
        // EPA-2019-0568.R1
        // double friction;
        // if(fabs(ACM.rpm*RPM_2_ELEC_RAD_PER_SEC)<0.08){
        //     if(ACM.rpm>0){
        //         friction = 0.0125 / 0.08 * ACM.rpm*RPM_2_ELEC_RAD_PER_SEC; // <- using elec rad/s is wrong
        //     }else{
        //         friction = - 0.0125 / 0.08 * ACM.rpm*RPM_2_ELEC_RAD_PER_SEC;
        //     }
        // }else{
        //     if(ACM.rpm>0){
        //         friction = 0.0025 + 0.0025 * ACM.rpm*RPM_2_ELEC_RAD_PER_SEC;
        //     }else{
        //         friction = - 0.0025 - 0.0025 * ACM.rpm*RPM_2_ELEC_RAD_PER_SEC;
        //     }
        // }
        // ACM.Tload += friction;

        // 齿轮箱背隙建模(在背隙形程内，负载为零，否则突然加载)
    return Tload;
}
