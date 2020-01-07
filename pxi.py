import ctypes
from .headers import *

PXI_PATH = "C:\Program Files\IVI Foundation\IVI\Bin\KtM960x_64.dll"

# Data type for PXI driver
Retrun = ctypes.c_long
ViRsrc = ctypes.c_char_p
ViBoolean = ctypes.c_bool
ViConstString = ctypes.c_char_p
ViSession = ctypes.c_uint32
ViAttr = ctypes.c_uint32
ViInt32 = ctypes.c_int
ViChar = ctypes.c_char


def KtM960x_InitWithOptions(ResourceName, IdQuery, Reset, OptionsString, Vi=None):
    """Opens the I/O session to the instrument. Driver methods and properties that access the instrument are only accessible after Initialize is called.
            Initialize optionally performs a Reset and queries the instrument to validate the instrument model. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Retrun, ViRsrc, ViBoolean, ViBoolean, ViConstString, ctypes.POINTER(ViSession))
    paramflags = (1, "ResourceName"), (1, "IdQuery"), (1, "Reset"), (1, "OptionsString"), (2, "Vi"),
    KtM960x_InitWithOptions = prototype(("KtM960x_InitWithOptions", lib), paramflags)
    ret = KtM960x_InitWithOptions(ResourceName.encode('utf-8'), IdQuery, Reset, OptionsString.encode('utf-8'))
    return ret


def KtM960x_GetAttributeViString(Vi, RepCapIdentifier, AttributeID, AttributeValueBufferSize, AttributeValue=None):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Retrun, ViSession, ViConstString, ViAttr, ViInt32,
                                   ctypes.POINTER(ViChar * AttributeValueBufferSize))
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (1, "AttributeValueBufferSize"), (
        2, "AttributeValue"),
    KtM960x_GetAttributeViString = prototype(("KtM960x_GetAttributeViString", lib), paramflags)
    ret = KtM960x_GetAttributeViString(Vi, RepCapIdentifier.encode('utf-8'), AttributeID, AttributeValueBufferSize)
    return ret[:].decode('utf-8').rstrip('\x00')


def KtM960x_SetAttributeViString(Vi, RepCapIdentifier, AttributeID, AttributeValue):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Retrun, ViSession, ViConstString, ViAttr, ViConstString)
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (1, "AttributeValueBufferSize"),
    KtM960x_SetAttributeViString = prototype(("KtM960x_SetAttributeViString", lib), paramflags)
    ret = KtM960x_SetAttributeViString(Vi, RepCapIdentifier.encode('utf-8'), AttributeID, AttributeValue.encode('utf-8'))
    return ret


def KtM960x_GetAttributeViInt32(Vi, RepCapIdentifier, AttributeID, AttributeValue=None):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Retrun, ViSession, ViConstString, ViAttr, ctypes.POINTER(ViInt32))
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (2, "AttributeValue"),
    KtM960x_GetAttributeViInt32 = prototype(("KtM960x_GetAttributeViInt32", lib), paramflags)
    ret = KtM960x_GetAttributeViInt32(Vi, RepCapIdentifier.encode('utf-8'), AttributeID)
    return ret


def KtM960x_SetAttributeViInt32(Vi, RepCapIdentifier, AttributeID, AttributeValue):
    """This routine is used to access low-level settings of the instrument. See the attributeID parameter for a link to all attributes of the instrument. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Retrun, ViSession, ViConstString, ViAttr, ViInt32)
    paramflags = (1, "Vi"), (1, "RepCapIdentifier"), (1, "AttributeID"), (1, "AttributeValue"),
    KtM960x_SetAttributeViInt32 = prototype(("KtM960x_SetAttributeViInt32", lib), paramflags)
    ret = KtM960x_SetAttributeViInt32(Vi, RepCapIdentifier.encode('utf-8'), AttributeID, AttributeValue)
    return ret


def KtM960x_close(Vi):
    """Closes the I/O session to the instrument. Driver methods and properties that access the instrument are not accessible after Close is called. """
    lib = ctypes.WinDLL(PXI_PATH)
    prototype = ctypes.WINFUNCTYPE(Retrun, ViSession)
    paramflags = (1, "Vi"),
    KtM960x_close = prototype(("KtM960x_close", lib), paramflags)
    ret = KtM960x_close(Vi)
    return ret
