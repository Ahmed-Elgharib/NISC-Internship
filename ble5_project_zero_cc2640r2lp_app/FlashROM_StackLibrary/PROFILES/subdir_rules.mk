################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL = cmd.exe

# Each subdirectory must supply rules for building sources it contributes
PROFILES/devinfoservice.obj: ../PROFILES/devinfoservice.c $(GEN_OPTS) | $(GEN_FILES) $(GEN_MISC_FILES)
	@echo 'Building file: "$<"'
	@echo 'Invoking: Arm Compiler'
	"C:/ti/ccs1200/ccs/tools/compiler/ti-cgt-arm_20.2.6.LTS/bin/armcl" --cmd_file="E:/ti/ble5_project_zero_cc2640r2lp_app/TOOLS/defines/ble5_project_zero_cc2640r2lp_app_FlashROM_StackLibrary.opt" --cmd_file="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/config/build_components.opt" --cmd_file="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/config/factory_config.opt" --cmd_file="E:/ti/ble5_project_zero_cc2640r2lp_stack_library/TOOLS/build_config.opt"  -mv7M4 --code_state=16 -me -O2 --opt_for_speed=0 --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Application" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Startup" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/PROFILES" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Include" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/examples/rtos/CC2640R2_LAUNCHXL/ble5stack/project_zero/src/extra" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/controller/cc26xx/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/rom" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/common/cc26xx" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/icall/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/target" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/target/_common" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/target/_common/cc26xx" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/heapmgr" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/icall/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/osal/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/services/src/saddr" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/services/src/sdata" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/devices/cc26x0r2" --include_path="C:/ti/ccs1200/ccs/tools/compiler/ti-cgt-arm_20.2.6.LTS/include" --define=DeviceFamily_CC26X0R2 --define=uartlog_FILE="\"devinfoservice.c\"" --define=UARTLOG_ENABLE -g --c99 --gcc --diag_warning=225 --diag_wrap=off --display_error_number --gen_func_subsections=on --abi=eabi --preproc_with_compile --preproc_dependency="PROFILES/devinfoservice.d_raw" --obj_directory="PROFILES" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: "$<"'
	@echo ' '

PROFILES/gatt_uuid.obj: ../PROFILES/gatt_uuid.c $(GEN_OPTS) | $(GEN_FILES) $(GEN_MISC_FILES)
	@echo 'Building file: "$<"'
	@echo 'Invoking: Arm Compiler'
	"C:/ti/ccs1200/ccs/tools/compiler/ti-cgt-arm_20.2.6.LTS/bin/armcl" --cmd_file="E:/ti/ble5_project_zero_cc2640r2lp_app/TOOLS/defines/ble5_project_zero_cc2640r2lp_app_FlashROM_StackLibrary.opt" --cmd_file="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/config/build_components.opt" --cmd_file="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/config/factory_config.opt" --cmd_file="E:/ti/ble5_project_zero_cc2640r2lp_stack_library/TOOLS/build_config.opt"  -mv7M4 --code_state=16 -me -O2 --opt_for_speed=0 --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Application" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Startup" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/PROFILES" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Include" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/examples/rtos/CC2640R2_LAUNCHXL/ble5stack/project_zero/src/extra" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/controller/cc26xx/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/rom" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/common/cc26xx" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/icall/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/target" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/target/_common" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/target/_common/cc26xx" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/heapmgr" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/icall/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/osal/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/services/src/saddr" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/services/src/sdata" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/devices/cc26x0r2" --include_path="C:/ti/ccs1200/ccs/tools/compiler/ti-cgt-arm_20.2.6.LTS/include" --define=DeviceFamily_CC26X0R2 --define=uartlog_FILE="\"gatt_uuid.c\"" --define=UARTLOG_ENABLE -g --c99 --gcc --diag_warning=225 --diag_wrap=off --display_error_number --gen_func_subsections=on --abi=eabi --preproc_with_compile --preproc_dependency="PROFILES/gatt_uuid.d_raw" --obj_directory="PROFILES" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: "$<"'
	@echo ' '

PROFILES/gattservapp_util.obj: ../PROFILES/gattservapp_util.c $(GEN_OPTS) | $(GEN_FILES) $(GEN_MISC_FILES)
	@echo 'Building file: "$<"'
	@echo 'Invoking: Arm Compiler'
	"C:/ti/ccs1200/ccs/tools/compiler/ti-cgt-arm_20.2.6.LTS/bin/armcl" --cmd_file="E:/ti/ble5_project_zero_cc2640r2lp_app/TOOLS/defines/ble5_project_zero_cc2640r2lp_app_FlashROM_StackLibrary.opt" --cmd_file="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/config/build_components.opt" --cmd_file="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/config/factory_config.opt" --cmd_file="E:/ti/ble5_project_zero_cc2640r2lp_stack_library/TOOLS/build_config.opt"  -mv7M4 --code_state=16 -me -O2 --opt_for_speed=0 --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Application" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Startup" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/PROFILES" --include_path="E:/ti/ble5_project_zero_cc2640r2lp_app/Include" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/examples/rtos/CC2640R2_LAUNCHXL/ble5stack/project_zero/src/extra" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/controller/cc26xx/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/rom" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/common/cc26xx" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/icall/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/target" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/target/_common" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/target/_common/cc26xx" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/hal/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/heapmgr" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/icall/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/osal/src/inc" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/services/src/saddr" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/ble5stack/services/src/sdata" --include_path="C:/ti/simplelink_cc2640r2_sdk_5_30_00_03/source/ti/devices/cc26x0r2" --include_path="C:/ti/ccs1200/ccs/tools/compiler/ti-cgt-arm_20.2.6.LTS/include" --define=DeviceFamily_CC26X0R2 --define=uartlog_FILE="\"gattservapp_util.c\"" --define=UARTLOG_ENABLE -g --c99 --gcc --diag_warning=225 --diag_wrap=off --display_error_number --gen_func_subsections=on --abi=eabi --preproc_with_compile --preproc_dependency="PROFILES/gattservapp_util.d_raw" --obj_directory="PROFILES" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: "$<"'
	@echo ' '


