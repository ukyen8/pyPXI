# This is a python package for controlling Keysight PXI-base instrument.
# This module integrates PXI library which is developed by Keysight to Python environment,
# so as you can develop PXI function for instrument under Python environment.


Prerequisite:

1. Please install Keysight IO Library, version newer than 2019

https://www.keysight.com/zh-TW/pd-1985909/io-libraries-suite?pm=DL&nid=-33330.977662&cc=TW&lc=cht

2. Please install Keysight PXI driver

https://www.keysight.com/main/software.jspx?ckey=3085523&lc=cht&cc=TW&nid=-32203.1280160&id=3085523


Usages:

from .pxi import *

VISESSION = KtM960x_InitWithOptions("PXI0::5-0.0::INSTR", True, True, "")  # Initialize PXI instrument
KtM960x_SetAttributeViInt32(VISESSION, "", KTM960X_ATTR_MEASUREMENT_ARM_COUNT, 21)  # set a number to an attribute
res = KtM960x_GetAttributeViInt32(VISESSION, "", KTM960X_ATTR_MEASUREMENT_ARM_COUNT)  # get value from attribute
print(res)  # output 21
KtM960x_close(VISESSION)  # close PXI session


Update:

Currently, I transform the following function, others will keep updating.

KtM960x_InitWithOptions
KtM960x_GetAttributeViString
KtM960x_SetAttributeViString
KtM960x_GetAttributeViInt32
KtM960x_SetAttributeViInt32
KtM960x_close
KtM960x_GetAttributeViReal64
KtM960x_SetAttributeViReal64
KtM960x_GetAttributeViBoolean
KtM960x_SetAttributeViBoolean
KtM960x_Initiate
KtM960x_TransientInitiate
KtM960x_SystemWaitForOperationComplete
KtM960x_MeasurementMeasure
KtM960x_reset
KtM960x_MeasurementFetchArrayData


