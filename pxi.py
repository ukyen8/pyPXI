import ctypes
from .headers import *

PXI_PATH = "C:\Program Files\IVI Foundation\IVI\Bin\KtM960x_64.dll"

# Data type for PXI driver
Return = ctypes.c_long
ViRsrc = ctypes.c_char_p
ViBoolean = ctypes.c_bool
ViConstString = ctypes.c_char_p
ViSession = ctypes.c_uint32
ViAttr = ctypes.c_uint32
ViStatus = ctypes.c_int
ViInt16 = ctypes.c_int16
ViInt32 = ctypes.c_int
ViInt64 = ctypes.c_int64
ViChar = ctypes.c_char
ViReal64 = ctypes.c_double


def KtM960x_InitWithOptions(ResourceName, IdQuery, Reset, OptionsString, Vi=None):
    """Opens the I/O session to the instrument. Driver methods and properties that access the instrument are only accessible after Initialize is called.
            Initialize optionally performs a Reset and queries the instrument to validate the instrument model. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViRsrc, ViBoolean, ViBoolean, ViConstString, ctypes.POINTER(ViSession))
    paramflags = (1, "ResourceName"), (1, "IdQuery"), (1, "Reset"), (1, "OptionsString"), (2, "Vi"),
    KtM960x_InitWithOptions = prototype(("KtM960x_InitWithOptions", lib), paramflags)
    ret = KtM960x_InitWithOptions(ResourceName.encode('utf-8'), IdQuery, Reset, OptionsString.encode('utf-8'))
    return ret


def KtM960x_GetAttributeViString(Vi, RepCapIdentifier, AttributeID, AttributeValueBufferSize, AttributeValue=None):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViConstString, ViAttr, ViInt32,
                                   ctypes.POINTER(ViChar * AttributeValueBufferSize))
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (1, "AttributeValueBufferSize"), (
        2, "AttributeValue"),
    KtM960x_GetAttributeViString = prototype(("KtM960x_GetAttributeViString", lib), paramflags)
    ret = KtM960x_GetAttributeViString(Vi, RepCapIdentifier.encode('utf-8'), AttributeID, AttributeValueBufferSize)
    return ret[:].decode('utf-8').rstrip('\x00')


def KtM960x_SetAttributeViString(Vi, RepCapIdentifier, AttributeID, AttributeValue):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViConstString, ViAttr, ViConstString)
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (1, "AttributeValueBufferSize"),
    KtM960x_SetAttributeViString = prototype(("KtM960x_SetAttributeViString", lib), paramflags)
    ret = KtM960x_SetAttributeViString(Vi, RepCapIdentifier.encode('utf-8'), AttributeID, AttributeValue.encode('utf-8'))
    return ret


def KtM960x_GetAttributeViInt32(Vi, RepCapIdentifier, AttributeID, AttributeValue=None):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViConstString, ViAttr, ctypes.POINTER(ViInt32))
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (2, "AttributeValue"),
    KtM960x_GetAttributeViInt32 = prototype(("KtM960x_GetAttributeViInt32", lib), paramflags)
    ret = KtM960x_GetAttributeViInt32(Vi, RepCapIdentifier.encode('utf-8'), AttributeID)
    return ret


def KtM960x_SetAttributeViInt32(Vi, RepCapIdentifier, AttributeID, AttributeValue):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViConstString, ViAttr, ViInt32)
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (1, "AttributeValue"),
    KtM960x_SetAttributeViInt32 = prototype(("KtM960x_SetAttributeViInt32", lib), paramflags)
    ret = KtM960x_SetAttributeViInt32(Vi, RepCapIdentifier.encode('utf-8'), AttributeID, AttributeValue)
    return ret

def KtM960x_GetAttributeViReal64(Vi, RepCapIdentifier, AttributeID, AttributeValue=None):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViConstString, ViAttr, ctypes.POINTER(ViReal64))
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (2, "AttributeValue"),
    KtM960x_GetAttributeViInt32 = prototype(("KtM960x_GetAttributeViReal64", lib), paramflags)
    ret = KtM960x_GetAttributeViInt32(Vi, RepCapIdentifier.encode('utf-8'), AttributeID)
    return ret

def KtM960x_SetAttributeViReal64(Vi, RepCapIdentifier, AttributeID, AttributeValue):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViConstString, ViAttr, ViReal64)
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (1, "AttributeValue"),
    KtM960x_SetAttributeViInt32 = prototype(("KtM960x_SetAttributeViReal64", lib), paramflags)
    ret = KtM960x_SetAttributeViInt32(Vi, RepCapIdentifier.encode('utf-8'), AttributeID, AttributeValue)
    return ret

def KtM960x_GetAttributeViBoolean(Vi, RepCapIdentifier, AttributeID, AttributeValue=None):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViConstString, ViAttr, ctypes.POINTER(ViBoolean))
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (2, "AttributeValue"),
    KtM960x_GetAttributeViBoolean = prototype(("KtM960x_GetAttributeViBoolean", lib), paramflags)
    ret = KtM960x_GetAttributeViBoolean(Vi, RepCapIdentifier.encode('utf-8'), AttributeID)
    return ret

def KtM960x_SetAttributeViBoolean(Vi, RepCapIdentifier, AttributeID, AttributeValue):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViConstString, ViAttr, ViBoolean)
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (1, "AttributeValue"),
    KtM960x_SetAttributeViBoolean = prototype(("KtM960x_SetAttributeViBoolean", lib), paramflags)
    ret = KtM960x_SetAttributeViBoolean(Vi, RepCapIdentifier.encode('utf-8'), AttributeID, AttributeValue)
    return ret

def KtM960x_Initiate(Vi, ChNumBufferSize, ChNum):
    """Initiates the specified device action. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViInt32, ViInt32 * ChNumBufferSize)
    paramflags = (1, "Vi"), (1, "ChNumBufferSize"), (1, "ChNum"),
    KtM960x_Initiate = prototype(("KtM960x_Initiate", lib), paramflags)
    ret = KtM960x_Initiate(Vi, ChNumBufferSize, ChNum)
    return ret

def KtM960x_TransientInitiate(Vi, ChNumBufferSize, ChNum):
    """Initiates the specified device action. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViInt32, ViInt32 * ChNumBufferSize)
    paramflags = (1, "Vi"), (1, "ChNumBufferSize"), (1, "ChNum"),
    KtM960x_TransientInitiate = prototype(("KtM960x_TransientInitiate", lib), paramflags)
    ret = KtM960x_TransientInitiate(Vi, ChNumBufferSize, ChNum)
    return ret

def KtM960x_SystemWaitForOperationComplete(Vi, TimeoutMs, Val=None):
    """Wait for all pending operations. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViInt32, ctypes.POINTER(ViBoolean))
    paramflags = (1, "Vi"), (1, "TimeoutMs"), (2, "Val"),
    KtM960x_SystemWaitForOperationComplete = prototype(("KtM960x_SystemWaitForOperationComplete", lib), paramflags)
    ret = KtM960x_SystemWaitForOperationComplete(Vi, TimeoutMs)
    return ret

def KtM960x_MeasurementMeasure(Vi, MeasurementType, ChNumBufferSize, ChNum, ValBufferSize, Val=None, ValActualSize=None):
    """Performs one point measurement and returns the array data which contains the first data for the specified data type. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViInt32, ViInt32, ctypes.POINTER(ViInt32), ViInt32, ctypes.POINTER(ViReal64 * ValBufferSize), ctypes.POINTER(ViInt32))
    paramflags = (1, "Vi"), (1, "MeasurementType"), (1, "ChNumBufferSize"), (1, "ChNum"), (1, "ValBufferSize"), (2, "Val"), (2, "ValActualSize"),
    KtM960x_MeasurementMeasure = prototype(("KtM960x_MeasurementMeasure", lib), paramflags)
    ret = KtM960x_MeasurementMeasure(Vi, MeasurementType, ChNumBufferSize, (ViInt32 * ChNumBufferSize)(*ChNum), ValBufferSize)
    return ret

def KtM960x_reset(Vi):
    """Places the instrument in a known state and configures instrument options on which the IVI specific driver depends (for example, enabling/disabling headers). For an IEEE 488.2 instrument, Reset sends the command string *RST to the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession)
    paramflags = (1, "Vi"),
    KtM960x_close = prototype(("KtM960x_reset", lib), paramflags)
    ret = KtM960x_close(Vi)
    return ret

def KtM960x_close(Vi):
    """Closes the I/O session to the instrument. Driver methods and properties that access the instrument are not accessible after Close is called. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession)
    paramflags = (1, "Vi"),
    KtM960x_close = prototype(("KtM960x_close", lib), paramflags)
    ret = KtM960x_close(Vi)
    return ret

def KtM960x_MeasurementFetchArrayData(Vi, FetchType, ChNumBufferSize, ChNum, ValBufferSize, Val=None, ValActualSize=None):
    """Waits measurement complete and returns the array data which contains all data for the specified data type."""
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Return, ViSession, ViInt32, ViInt32, ViInt32 * ChNumBufferSize, ViInt32,
                                   ctypes.POINTER(ViReal64*ValBufferSize), ctypes.POINTER(ViInt32))
    paramflags = (1, "Vi"), (1, "FetchType"), (1, "ChNumBufferSize"), (1, "ChNum"), (1, "ValBufferSize"), \
                 (2, "Val"), (2, "ValActualSize"),
    KtM960x_MeasurementFetchArrayData = prototype(("KtM960x_MeasurementFetchArrayData", lib), paramflags)
    ret = KtM960x_MeasurementFetchArrayData(Vi, FetchType, ChNumBufferSize, (ViInt32 * ChNumBufferSize)(*ChNum), ValBufferSize)
    return ret
