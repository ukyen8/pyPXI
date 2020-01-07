import pytest
from .pxi import *

VISESSION = None

@pytest.mark.order1
def test_KtM960x_InitWithOptions():
    global VISESSION
    VISESSION = KtM960x_InitWithOptions("PXI0::5-0.0::INSTR", True, True, "")
    assert VISESSION == 1


def test_KtM960x_GetAttributeViInt32_and_KtM960x_GetAttributeViInt32():
    res = KtM960x_SetAttributeViInt32(VISESSION, "", KTM960X_ATTR_MEASUREMENT_ARM_COUNT, 21)
    res = KtM960x_GetAttributeViInt32(VISESSION, "", KTM960X_ATTR_MEASUREMENT_ARM_COUNT)
    assert res == 21


def test_KtM960x_GetAttributeViString_and_KtM960x_SetAttributeViString():
    # ViString read-write attribute
    res = KtM960x_SetAttributeViString(VISESSION, "", KTM960X_ATTR_NONVOLATILE_ASSET_NUMBER, "Test")
    assert res == 0
    res = KtM960x_GetAttributeViString(VISESSION, "", KTM960X_ATTR_NONVOLATILE_ASSET_NUMBER, 10)
    assert res[:] == "Test"

    # ViString read-only attribute
    res = KtM960x_SetAttributeViString(VISESSION, "", KTM960X_ATTR_INSTRUMENT_FIRMWARE_REVISION, "Test")
    assert res == -1074135027 and PXI_ERROR_DICT[res] == "Attribute '%1' is read-only."


@pytest.mark.last
def test_KtM960x_close():
    res = KtM960x_close(VISESSION)
    assert res == 0

