import pytest
from .pxi import *

IS_ONLINE = True
VISESSION = None


@pytest.mark.order1
# @pytest.mark.skip
def test_KtM960x_InitWithOptions():
    global VISESSION
    if IS_ONLINE is True:
        VISESSION = KtM960x_InitWithOptions("PXI0::5-0.0::INSTR", True, True, "")
    if IS_ONLINE is False:
        VISESSION = KtM960x_InitWithOptions("PXI0::5-0.0::INSTR", True, True, "Simulate=VI_TRUE, DriverSetup= Model=M9601A")
    assert VISESSION == 1

@pytest.mark.order2
# @pytest.mark.skip
def test_KtM960x_reset():
    res = KtM960x_reset(VISESSION)
    assert res == 0

@pytest.mark.order3
def test_KtM960x_GetAttributeViInt32_and_KtM960x_SetAttributeViInt32():
    res = KtM960x_SetAttributeViInt32(VISESSION, "", KTM960X_ATTR_MEASUREMENT_ARM_COUNT, 21)
    res = KtM960x_GetAttributeViInt32(VISESSION, "", KTM960X_ATTR_MEASUREMENT_ARM_COUNT)
    assert res == 21

@pytest.mark.order4
def test_KtM960x_GetAttributeViString_and_KtM960x_SetAttributeViString():
    # ViString read-write attribute
    res = KtM960x_SetAttributeViString(VISESSION, "", KTM960X_ATTR_NONVOLATILE_ASSET_NUMBER, "Test")
    assert res == 0
    res = KtM960x_GetAttributeViString(VISESSION, "", KTM960X_ATTR_NONVOLATILE_ASSET_NUMBER, 10)
    assert res[:] == "Test"

    # ViString read-only attribute
    res = KtM960x_SetAttributeViString(VISESSION, "", KTM960X_ATTR_INSTRUMENT_FIRMWARE_REVISION, "Test")
    assert res == -1074135027 and PXI_ERROR_DICT[res] == "Attribute '%1' is read-only."

# @pytest.mark.skip(reason="in development")
@pytest.mark.order5
def test_KtM960x_GetAttributeViReal64_and_KtM960x_SetAttributeViReal64():
    # ViReal64 read-write attribute
    res = KtM960x_SetAttributeViReal64(VISESSION, "", KTM960X_ATTR_MEASUREMENT_ARM_DELAY, 3.1415)
    assert res == 0
    res = KtM960x_GetAttributeViReal64(VISESSION, "", KTM960X_ATTR_MEASUREMENT_ARM_DELAY, 10)
    assert res == 3.1415

    # ViReal64 read-only attribute
    res = KtM960x_SetAttributeViReal64(VISESSION, "", KTM960X_ATTR_SYSTEM_TIMER_COUNT, 3.1415)
    assert res == -1074135027 and PXI_ERROR_DICT[res] == "Attribute '%1' is read-only."

@pytest.mark.order6
def test_KtM960x_GetAttributeViBoolean_and_KtM960x_SetAttributeViBoolean():
    # ViReal64 read-write attribute
    res = KtM960x_SetAttributeViBoolean(VISESSION, "", KTM960X_ATTR_SYSTEM_SFP_AUTOREFRESH_ENABLED, True)
    assert res == 0
    res = KtM960x_GetAttributeViBoolean(VISESSION, "", KTM960X_ATTR_SYSTEM_SFP_AUTOREFRESH_ENABLED, 10)
    assert res

    # ViReal64 read-only attribute
    res = KtM960x_SetAttributeViBoolean(VISESSION, "", KTM960X_ATTR_SYSTEM_INTERLOCK_TRIPPED, True)
    assert res == -1074135027 and PXI_ERROR_DICT[res] == "Attribute '%1' is read-only."


@pytest.mark.skip
def test_KtM960x_Initiate():
    # Trigger KtM960x_Initiate test
    pyarr = [1]
    arr = (ctypes.c_int * len(pyarr))(*pyarr)       # provide int list
    res = KtM960x_Initiate(VISESSION, len(arr), arr)
    assert res == 0


@pytest.mark.order7
def test_KtM960x_SystemWaitForOperationComplete():
    # SystemWaitForOperationComplete for hardware wait_th
    res = KtM960x_SystemWaitForOperationComplete(VISESSION, 5000)
    assert res is True


@pytest.mark.order8
def test_KtM960x_MeasurementMeasure():
    data = [0]*1024
    pyarr = [1]
    res = KtM960x_MeasurementMeasure(VISESSION, KTM960X_VAL_MEASUREMENT_FETCH_TYPE_ALL, len(pyarr), pyarr, len(data))
    assert len(res[0]) == 1024


@pytest.mark.order9
def test_KtM960x_MeasurementFetchArrayData():
    data = [0] * 1024
    pyarr = [1]
    res = KtM960x_MeasurementFetchArrayData(VISESSION, KTM960X_VAL_MEASUREMENT_FETCH_TYPE_VOLTAGE, len(pyarr), pyarr, len(data))
    assert len(res[0]) == 1024

@pytest.mark.order8
def test_KtM960x_TransientInitiate():
    # Trigger KtM960x_TransientInitiate test
    pyarr = [1]
    arr = (ctypes.c_int * len(pyarr))(*pyarr)       # provide int list
    res = KtM960x_TransientInitiate(VISESSION, len(arr), arr)
    assert res == 0

@pytest.mark.last
def test_KtM960x_close():
    res = KtM960x_close(VISESSION)
    assert res == 0

