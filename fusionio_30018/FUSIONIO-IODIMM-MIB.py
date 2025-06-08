# SNMP MIB module (FUSIONIO-IODIMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/fusionio_30018/FUSIONIO-IODIMM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:03:32 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class SimpleTime(DisplayString):
    """Custom type SimpleTime based on DisplayString"""




class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fusionio_ObjectIdentity = ObjectIdentity
fusionio = _Fusionio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018)
)
_FusionIoDimm_ObjectIdentity = ObjectIdentity
fusionIoDimm = _FusionIoDimm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1)
)
_FusionIoDimmMib_ObjectIdentity = ObjectIdentity
fusionIoDimmMib = _FusionIoDimmMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1, 1)
)


class _FusionIoDimmMibRevMajor_Type(Integer32):
    """Custom type fusionIoDimmMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FusionIoDimmMibRevMajor_Type.__name__ = "Integer32"
_FusionIoDimmMibRevMajor_Object = MibScalar
fusionIoDimmMibRevMajor = _FusionIoDimmMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 1, 1),
    _FusionIoDimmMibRevMajor_Type()
)
fusionIoDimmMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmMibRevMajor.setStatus("mandatory")


class _FusionIoDimmMibRevMinor_Type(Integer32):
    """Custom type fusionIoDimmMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmMibRevMinor_Type.__name__ = "Integer32"
_FusionIoDimmMibRevMinor_Object = MibScalar
fusionIoDimmMibRevMinor = _FusionIoDimmMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 1, 2),
    _FusionIoDimmMibRevMinor_Type()
)
fusionIoDimmMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmMibRevMinor.setStatus("mandatory")


class _FusionIoDimmMIBCondition_Type(Integer32):
    """Custom type fusionIoDimmMIBCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_FusionIoDimmMIBCondition_Type.__name__ = "Integer32"
_FusionIoDimmMIBCondition_Object = MibScalar
fusionIoDimmMIBCondition = _FusionIoDimmMIBCondition_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 1, 3),
    _FusionIoDimmMIBCondition_Type()
)
fusionIoDimmMIBCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmMIBCondition.setStatus("mandatory")
_FusionIoDimmComponent_ObjectIdentity = ObjectIdentity
fusionIoDimmComponent = _FusionIoDimmComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2)
)
_FusionIoDimmInfo_ObjectIdentity = ObjectIdentity
fusionIoDimmInfo = _FusionIoDimmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1)
)
_FusionIoDimmInfoTable_Object = MibTable
fusionIoDimmInfoTable = _FusionIoDimmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fusionIoDimmInfoTable.setStatus("mandatory")
_FusionIoDimmInfoEntry_Object = MibTableRow
fusionIoDimmInfoEntry = _FusionIoDimmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1)
)
fusionIoDimmInfoEntry.setIndexNames(
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
)
if mibBuilder.loadTexts:
    fusionIoDimmInfoEntry.setStatus("mandatory")


class _FusionIoDimmInfoIndex_Type(Integer32):
    """Custom type fusionIoDimmInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FusionIoDimmInfoIndex_Type.__name__ = "Integer32"
_FusionIoDimmInfoIndex_Object = MibTableColumn
fusionIoDimmInfoIndex = _FusionIoDimmInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 1),
    _FusionIoDimmInfoIndex_Type()
)
fusionIoDimmInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoIndex.setStatus("mandatory")


class _FusionIoDimmInfoStatus_Type(Integer32):
    """Custom type fusionIoDimmInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_FusionIoDimmInfoStatus_Type.__name__ = "Integer32"
_FusionIoDimmInfoStatus_Object = MibTableColumn
fusionIoDimmInfoStatus = _FusionIoDimmInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 2),
    _FusionIoDimmInfoStatus_Type()
)
fusionIoDimmInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoStatus.setStatus("mandatory")


class _FusionIoDimmInfoName_Type(DisplayString):
    """Custom type fusionIoDimmInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoName_Type.__name__ = "DisplayString"
_FusionIoDimmInfoName_Object = MibTableColumn
fusionIoDimmInfoName = _FusionIoDimmInfoName_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 3),
    _FusionIoDimmInfoName_Type()
)
fusionIoDimmInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmInfoName.setStatus("mandatory")


class _FusionIoDimmInfoSerialNumber_Type(DisplayString):
    """Custom type fusionIoDimmInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoSerialNumber_Type.__name__ = "DisplayString"
_FusionIoDimmInfoSerialNumber_Object = MibTableColumn
fusionIoDimmInfoSerialNumber = _FusionIoDimmInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 4),
    _FusionIoDimmInfoSerialNumber_Type()
)
fusionIoDimmInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoSerialNumber.setStatus("mandatory")


class _FusionIoDimmInfoPartNumber_Type(DisplayString):
    """Custom type fusionIoDimmInfoPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoPartNumber_Type.__name__ = "DisplayString"
_FusionIoDimmInfoPartNumber_Object = MibTableColumn
fusionIoDimmInfoPartNumber = _FusionIoDimmInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 5),
    _FusionIoDimmInfoPartNumber_Type()
)
fusionIoDimmInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPartNumber.setStatus("mandatory")


class _FusionIoDimmInfoSubVendorPartNumber_Type(DisplayString):
    """Custom type fusionIoDimmInfoSubVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoSubVendorPartNumber_Type.__name__ = "DisplayString"
_FusionIoDimmInfoSubVendorPartNumber_Object = MibTableColumn
fusionIoDimmInfoSubVendorPartNumber = _FusionIoDimmInfoSubVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 6),
    _FusionIoDimmInfoSubVendorPartNumber_Type()
)
fusionIoDimmInfoSubVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoSubVendorPartNumber.setStatus("mandatory")


class _FusionIoDimmInfoSparePartNumber_Type(DisplayString):
    """Custom type fusionIoDimmInfoSparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoSparePartNumber_Type.__name__ = "DisplayString"
_FusionIoDimmInfoSparePartNumber_Object = MibTableColumn
fusionIoDimmInfoSparePartNumber = _FusionIoDimmInfoSparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 7),
    _FusionIoDimmInfoSparePartNumber_Type()
)
fusionIoDimmInfoSparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoSparePartNumber.setStatus("mandatory")


class _FusionIoDimmInfoAssemblyNumber_Type(DisplayString):
    """Custom type fusionIoDimmInfoAssemblyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoAssemblyNumber_Type.__name__ = "DisplayString"
_FusionIoDimmInfoAssemblyNumber_Object = MibTableColumn
fusionIoDimmInfoAssemblyNumber = _FusionIoDimmInfoAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 8),
    _FusionIoDimmInfoAssemblyNumber_Type()
)
fusionIoDimmInfoAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoAssemblyNumber.setStatus("mandatory")


class _FusionIoDimmInfoFirmwareVersion_Type(DisplayString):
    """Custom type fusionIoDimmInfoFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoFirmwareVersion_Type.__name__ = "DisplayString"
_FusionIoDimmInfoFirmwareVersion_Object = MibTableColumn
fusionIoDimmInfoFirmwareVersion = _FusionIoDimmInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 9),
    _FusionIoDimmInfoFirmwareVersion_Type()
)
fusionIoDimmInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoFirmwareVersion.setStatus("mandatory")


class _FusionIoDimmInfoDriverVersion_Type(DisplayString):
    """Custom type fusionIoDimmInfoDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoDriverVersion_Type.__name__ = "DisplayString"
_FusionIoDimmInfoDriverVersion_Object = MibTableColumn
fusionIoDimmInfoDriverVersion = _FusionIoDimmInfoDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 10),
    _FusionIoDimmInfoDriverVersion_Type()
)
fusionIoDimmInfoDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoDriverVersion.setStatus("mandatory")


class _FusionIoDimmInfoUID_Type(DisplayString):
    """Custom type fusionIoDimmInfoUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoUID_Type.__name__ = "DisplayString"
_FusionIoDimmInfoUID_Object = MibTableColumn
fusionIoDimmInfoUID = _FusionIoDimmInfoUID_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 11),
    _FusionIoDimmInfoUID_Type()
)
fusionIoDimmInfoUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoUID.setStatus("mandatory")


class _FusionIoDimmInfoState_Type(Integer32):
    """Custom type fusionIoDimmInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("detached", 1),
          ("attached", 2),
          ("minimal", 3),
          ("error", 4),
          ("detaching", 5),
          ("attaching", 6),
          ("scanning", 7),
          ("formatting", 8),
          ("updating", 9),
          ("attach", 10),
          ("detach", 11),
          ("format", 12),
          ("update", 13))
    )


_FusionIoDimmInfoState_Type.__name__ = "Integer32"
_FusionIoDimmInfoState_Object = MibTableColumn
fusionIoDimmInfoState = _FusionIoDimmInfoState_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 12),
    _FusionIoDimmInfoState_Type()
)
fusionIoDimmInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmInfoState.setStatus("mandatory")


class _FusionIoDimmInfoClientDeviceName_Type(DisplayString):
    """Custom type fusionIoDimmInfoClientDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_FusionIoDimmInfoClientDeviceName_Type.__name__ = "DisplayString"
_FusionIoDimmInfoClientDeviceName_Object = MibTableColumn
fusionIoDimmInfoClientDeviceName = _FusionIoDimmInfoClientDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 13),
    _FusionIoDimmInfoClientDeviceName_Type()
)
fusionIoDimmInfoClientDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoClientDeviceName.setStatus("mandatory")
_FusionIoDimmInfoBeacon_Type = Boolean
_FusionIoDimmInfoBeacon_Object = MibTableColumn
fusionIoDimmInfoBeacon = _FusionIoDimmInfoBeacon_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 14),
    _FusionIoDimmInfoBeacon_Type()
)
fusionIoDimmInfoBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmInfoBeacon.setStatus("mandatory")


class _FusionIoDimmInfoPCIAddress_Type(DisplayString):
    """Custom type fusionIoDimmInfoPCIAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_FusionIoDimmInfoPCIAddress_Type.__name__ = "DisplayString"
_FusionIoDimmInfoPCIAddress_Object = MibTableColumn
fusionIoDimmInfoPCIAddress = _FusionIoDimmInfoPCIAddress_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 15),
    _FusionIoDimmInfoPCIAddress_Type()
)
fusionIoDimmInfoPCIAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPCIAddress.setStatus("mandatory")


class _FusionIoDimmInfoPCIDeviceID_Type(DisplayString):
    """Custom type fusionIoDimmInfoPCIDeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_FusionIoDimmInfoPCIDeviceID_Type.__name__ = "DisplayString"
_FusionIoDimmInfoPCIDeviceID_Object = MibTableColumn
fusionIoDimmInfoPCIDeviceID = _FusionIoDimmInfoPCIDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 16),
    _FusionIoDimmInfoPCIDeviceID_Type()
)
fusionIoDimmInfoPCIDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPCIDeviceID.setStatus("mandatory")


class _FusionIoDimmInfoPCISubdeviceID_Type(DisplayString):
    """Custom type fusionIoDimmInfoPCISubdeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_FusionIoDimmInfoPCISubdeviceID_Type.__name__ = "DisplayString"
_FusionIoDimmInfoPCISubdeviceID_Object = MibTableColumn
fusionIoDimmInfoPCISubdeviceID = _FusionIoDimmInfoPCISubdeviceID_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 17),
    _FusionIoDimmInfoPCISubdeviceID_Type()
)
fusionIoDimmInfoPCISubdeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPCISubdeviceID.setStatus("mandatory")


class _FusionIoDimmInfoPCIVendorID_Type(DisplayString):
    """Custom type fusionIoDimmInfoPCIVendorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_FusionIoDimmInfoPCIVendorID_Type.__name__ = "DisplayString"
_FusionIoDimmInfoPCIVendorID_Object = MibTableColumn
fusionIoDimmInfoPCIVendorID = _FusionIoDimmInfoPCIVendorID_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 18),
    _FusionIoDimmInfoPCIVendorID_Type()
)
fusionIoDimmInfoPCIVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPCIVendorID.setStatus("mandatory")


class _FusionIoDimmInfoPCISubvendorID_Type(DisplayString):
    """Custom type fusionIoDimmInfoPCISubvendorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_FusionIoDimmInfoPCISubvendorID_Type.__name__ = "DisplayString"
_FusionIoDimmInfoPCISubvendorID_Object = MibTableColumn
fusionIoDimmInfoPCISubvendorID = _FusionIoDimmInfoPCISubvendorID_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 19),
    _FusionIoDimmInfoPCISubvendorID_Type()
)
fusionIoDimmInfoPCISubvendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPCISubvendorID.setStatus("mandatory")


class _FusionIoDimmInfoPCISlot_Type(Integer32):
    """Custom type fusionIoDimmInfoPCISlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FusionIoDimmInfoPCISlot_Type.__name__ = "Integer32"
_FusionIoDimmInfoPCISlot_Object = MibTableColumn
fusionIoDimmInfoPCISlot = _FusionIoDimmInfoPCISlot_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 20),
    _FusionIoDimmInfoPCISlot_Type()
)
fusionIoDimmInfoPCISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPCISlot.setStatus("mandatory")
_FusionIoDimmInfoWearoutIndicator_Type = Boolean
_FusionIoDimmInfoWearoutIndicator_Object = MibTableColumn
fusionIoDimmInfoWearoutIndicator = _FusionIoDimmInfoWearoutIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 21),
    _FusionIoDimmInfoWearoutIndicator_Type()
)
fusionIoDimmInfoWearoutIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoWearoutIndicator.setStatus("mandatory")
_FusionIoDimmInfoFlashbackIndicator_Type = Boolean
_FusionIoDimmInfoFlashbackIndicator_Object = MibTableColumn
fusionIoDimmInfoFlashbackIndicator = _FusionIoDimmInfoFlashbackIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 22),
    _FusionIoDimmInfoFlashbackIndicator_Type()
)
fusionIoDimmInfoFlashbackIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoFlashbackIndicator.setStatus("obsolete")


class _FusionIoDimmInfoWritableIndicator_Type(Integer32):
    """Custom type fusionIoDimmInfoWritableIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("writeReduced", 0),
          ("nonWritable", 1),
          ("normal", 2),
          ("unknown", 3))
    )


_FusionIoDimmInfoWritableIndicator_Type.__name__ = "Integer32"
_FusionIoDimmInfoWritableIndicator_Object = MibTableColumn
fusionIoDimmInfoWritableIndicator = _FusionIoDimmInfoWritableIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 23),
    _FusionIoDimmInfoWritableIndicator_Type()
)
fusionIoDimmInfoWritableIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoWritableIndicator.setStatus("mandatory")


class _FusionIoDimmInfoInternalTemp_Type(Integer32):
    """Custom type fusionIoDimmInfoInternalTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_FusionIoDimmInfoInternalTemp_Type.__name__ = "Integer32"
_FusionIoDimmInfoInternalTemp_Object = MibTableColumn
fusionIoDimmInfoInternalTemp = _FusionIoDimmInfoInternalTemp_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 24),
    _FusionIoDimmInfoInternalTemp_Type()
)
fusionIoDimmInfoInternalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoInternalTemp.setStatus("mandatory")


class _FusionIoDimmInfoHealthPercentage_Type(Integer32):
    """Custom type fusionIoDimmInfoHealthPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_FusionIoDimmInfoHealthPercentage_Type.__name__ = "Integer32"
_FusionIoDimmInfoHealthPercentage_Object = MibTableColumn
fusionIoDimmInfoHealthPercentage = _FusionIoDimmInfoHealthPercentage_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 25),
    _FusionIoDimmInfoHealthPercentage_Type()
)
fusionIoDimmInfoHealthPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoHealthPercentage.setStatus("mandatory")
_FusionIoDimmInfoShortTermWearoutDate_Type = SimpleTime
_FusionIoDimmInfoShortTermWearoutDate_Object = MibTableColumn
fusionIoDimmInfoShortTermWearoutDate = _FusionIoDimmInfoShortTermWearoutDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 26),
    _FusionIoDimmInfoShortTermWearoutDate_Type()
)
fusionIoDimmInfoShortTermWearoutDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoShortTermWearoutDate.setStatus("obsolete")
_FusionIoDimmInfoLongTermWearoutDate_Type = SimpleTime
_FusionIoDimmInfoLongTermWearoutDate_Object = MibTableColumn
fusionIoDimmInfoLongTermWearoutDate = _FusionIoDimmInfoLongTermWearoutDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 27),
    _FusionIoDimmInfoLongTermWearoutDate_Type()
)
fusionIoDimmInfoLongTermWearoutDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoLongTermWearoutDate.setStatus("obsolete")
_FusionIoDimmInfoShortTermNonWritableDate_Type = SimpleTime
_FusionIoDimmInfoShortTermNonWritableDate_Object = MibTableColumn
fusionIoDimmInfoShortTermNonWritableDate = _FusionIoDimmInfoShortTermNonWritableDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 28),
    _FusionIoDimmInfoShortTermNonWritableDate_Type()
)
fusionIoDimmInfoShortTermNonWritableDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoShortTermNonWritableDate.setStatus("obsolete")
_FusionIoDimmInfoLongTermNonWritableDate_Type = SimpleTime
_FusionIoDimmInfoLongTermNonWritableDate_Object = MibTableColumn
fusionIoDimmInfoLongTermNonWritableDate = _FusionIoDimmInfoLongTermNonWritableDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 29),
    _FusionIoDimmInfoLongTermNonWritableDate_Type()
)
fusionIoDimmInfoLongTermNonWritableDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoLongTermNonWritableDate.setStatus("obsolete")


class _FusionIoDimmInfoMinimalModeReason_Type(Integer32):
    """Custom type fusionIoDimmInfoMinimalModeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("firmwareOutOfDate", 1),
          ("lowPower", 2),
          ("dualPlaneFail", 3),
          ("forced", 4),
          ("internal", 5),
          ("cardLimitExceeded", 6),
          ("notInMinimalMode", 7),
          ("unsupportedOS", 8),
          ("insufficientMemory", 9),
          ("bootloaderMode", 10),
          ("missingMidprom", 11),
          ("unsupportedNand", 12),
          ("driverOutOfDate", 13),
          ("hardwareFailure", 14),
          ("channelInitFail", 15),
          ("fallbackFirmware", 16))
    )


_FusionIoDimmInfoMinimalModeReason_Type.__name__ = "Integer32"
_FusionIoDimmInfoMinimalModeReason_Object = MibTableColumn
fusionIoDimmInfoMinimalModeReason = _FusionIoDimmInfoMinimalModeReason_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 30),
    _FusionIoDimmInfoMinimalModeReason_Type()
)
fusionIoDimmInfoMinimalModeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMinimalModeReason.setStatus("mandatory")


class _FusionIoDimmInfoReducedWriteReason_Type(Integer32):
    """Custom type fusionIoDimmInfoReducedWriteReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("userRequested", 1),
          ("noMdBlocks", 2),
          ("noMemory", 3),
          ("dieFailure", 4),
          ("wearout", 5),
          ("adapterPower", 6),
          ("internal", 7),
          ("powerLimiting", 8),
          ("unavailable", 9),
          ("groomFails", 10))
    )


_FusionIoDimmInfoReducedWriteReason_Type.__name__ = "Integer32"
_FusionIoDimmInfoReducedWriteReason_Object = MibTableColumn
fusionIoDimmInfoReducedWriteReason = _FusionIoDimmInfoReducedWriteReason_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 31),
    _FusionIoDimmInfoReducedWriteReason_Type()
)
fusionIoDimmInfoReducedWriteReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoReducedWriteReason.setStatus("mandatory")


class _FusionIoDimmInfoMilliVolts_Type(Integer32):
    """Custom type fusionIoDimmInfoMilliVolts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoMilliVolts_Type.__name__ = "Integer32"
_FusionIoDimmInfoMilliVolts_Object = MibTableColumn
fusionIoDimmInfoMilliVolts = _FusionIoDimmInfoMilliVolts_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 32),
    _FusionIoDimmInfoMilliVolts_Type()
)
fusionIoDimmInfoMilliVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMilliVolts.setStatus("mandatory")


class _FusionIoDimmInfoMilliVoltsPeak_Type(Integer32):
    """Custom type fusionIoDimmInfoMilliVoltsPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoMilliVoltsPeak_Type.__name__ = "Integer32"
_FusionIoDimmInfoMilliVoltsPeak_Object = MibTableColumn
fusionIoDimmInfoMilliVoltsPeak = _FusionIoDimmInfoMilliVoltsPeak_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 33),
    _FusionIoDimmInfoMilliVoltsPeak_Type()
)
fusionIoDimmInfoMilliVoltsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMilliVoltsPeak.setStatus("mandatory")


class _FusionIoDimmInfoMilliVoltsMin_Type(Integer32):
    """Custom type fusionIoDimmInfoMilliVoltsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoMilliVoltsMin_Type.__name__ = "Integer32"
_FusionIoDimmInfoMilliVoltsMin_Object = MibTableColumn
fusionIoDimmInfoMilliVoltsMin = _FusionIoDimmInfoMilliVoltsMin_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 34),
    _FusionIoDimmInfoMilliVoltsMin_Type()
)
fusionIoDimmInfoMilliVoltsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMilliVoltsMin.setStatus("mandatory")


class _FusionIoDimmInfoMilliWatts_Type(Integer32):
    """Custom type fusionIoDimmInfoMilliWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoMilliWatts_Type.__name__ = "Integer32"
_FusionIoDimmInfoMilliWatts_Object = MibTableColumn
fusionIoDimmInfoMilliWatts = _FusionIoDimmInfoMilliWatts_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 35),
    _FusionIoDimmInfoMilliWatts_Type()
)
fusionIoDimmInfoMilliWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMilliWatts.setStatus("mandatory")


class _FusionIoDimmInfoMilliWattsPeak_Type(Integer32):
    """Custom type fusionIoDimmInfoMilliWattsPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoMilliWattsPeak_Type.__name__ = "Integer32"
_FusionIoDimmInfoMilliWattsPeak_Object = MibTableColumn
fusionIoDimmInfoMilliWattsPeak = _FusionIoDimmInfoMilliWattsPeak_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 36),
    _FusionIoDimmInfoMilliWattsPeak_Type()
)
fusionIoDimmInfoMilliWattsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMilliWattsPeak.setStatus("mandatory")


class _FusionIoDimmInfoMilliAmps_Type(Integer32):
    """Custom type fusionIoDimmInfoMilliAmps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoMilliAmps_Type.__name__ = "Integer32"
_FusionIoDimmInfoMilliAmps_Object = MibTableColumn
fusionIoDimmInfoMilliAmps = _FusionIoDimmInfoMilliAmps_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 37),
    _FusionIoDimmInfoMilliAmps_Type()
)
fusionIoDimmInfoMilliAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMilliAmps.setStatus("mandatory")


class _FusionIoDimmInfoMilliAmpsPeak_Type(Integer32):
    """Custom type fusionIoDimmInfoMilliAmpsPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoMilliAmpsPeak_Type.__name__ = "Integer32"
_FusionIoDimmInfoMilliAmpsPeak_Object = MibTableColumn
fusionIoDimmInfoMilliAmpsPeak = _FusionIoDimmInfoMilliAmpsPeak_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 38),
    _FusionIoDimmInfoMilliAmpsPeak_Type()
)
fusionIoDimmInfoMilliAmpsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMilliAmpsPeak.setStatus("mandatory")


class _FusionIoDimmInfoAdapterType_Type(Integer32):
    """Custom type fusionIoDimmInfoAdapterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("singleAdapter", 0),
          ("dualAdapter", 1),
          ("ioSanAdapter", 2),
          ("octalBaseAdapter", 3),
          ("octalMezzAdapter", 4),
          ("ioDimm", 5),
          ("ioMono", 6),
          ("ioXtreme", 7),
          ("hpMezz", 8),
          ("controller", 9),
          ("hpAdrenaline3", 10),
          ("fused", 11),
          ("nandModule", 12),
          ("dualControllerAdapter", 13),
          ("singleControllerAdapter", 14),
          ("ciscoMezz", 15))
    )


_FusionIoDimmInfoAdapterType_Type.__name__ = "Integer32"
_FusionIoDimmInfoAdapterType_Object = MibTableColumn
fusionIoDimmInfoAdapterType = _FusionIoDimmInfoAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 39),
    _FusionIoDimmInfoAdapterType_Type()
)
fusionIoDimmInfoAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoAdapterType.setStatus("mandatory")


class _FusionIoDimmInfoAdapterPort_Type(Integer32):
    """Custom type fusionIoDimmInfoAdapterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_FusionIoDimmInfoAdapterPort_Type.__name__ = "Integer32"
_FusionIoDimmInfoAdapterPort_Object = MibTableColumn
fusionIoDimmInfoAdapterPort = _FusionIoDimmInfoAdapterPort_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 40),
    _FusionIoDimmInfoAdapterPort_Type()
)
fusionIoDimmInfoAdapterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoAdapterPort.setStatus("mandatory")


class _FusionIoDimmInfoAdapterSerialNumber_Type(DisplayString):
    """Custom type fusionIoDimmInfoAdapterSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoAdapterSerialNumber_Type.__name__ = "DisplayString"
_FusionIoDimmInfoAdapterSerialNumber_Object = MibTableColumn
fusionIoDimmInfoAdapterSerialNumber = _FusionIoDimmInfoAdapterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 41),
    _FusionIoDimmInfoAdapterSerialNumber_Type()
)
fusionIoDimmInfoAdapterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoAdapterSerialNumber.setStatus("mandatory")
_FusionIoDimmInfoAdapterExtPowerPresent_Type = Boolean
_FusionIoDimmInfoAdapterExtPowerPresent_Object = MibTableColumn
fusionIoDimmInfoAdapterExtPowerPresent = _FusionIoDimmInfoAdapterExtPowerPresent_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 42),
    _FusionIoDimmInfoAdapterExtPowerPresent_Type()
)
fusionIoDimmInfoAdapterExtPowerPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoAdapterExtPowerPresent.setStatus("mandatory")
_FusionIoDimmInfoPowerlossProtectDisabled_Type = Boolean
_FusionIoDimmInfoPowerlossProtectDisabled_Object = MibTableColumn
fusionIoDimmInfoPowerlossProtectDisabled = _FusionIoDimmInfoPowerlossProtectDisabled_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 43),
    _FusionIoDimmInfoPowerlossProtectDisabled_Type()
)
fusionIoDimmInfoPowerlossProtectDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPowerlossProtectDisabled.setStatus("mandatory")
_FusionIoDimmInfoInternalTempHigh_Type = Boolean
_FusionIoDimmInfoInternalTempHigh_Object = MibTableColumn
fusionIoDimmInfoInternalTempHigh = _FusionIoDimmInfoInternalTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 44),
    _FusionIoDimmInfoInternalTempHigh_Type()
)
fusionIoDimmInfoInternalTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoInternalTempHigh.setStatus("mandatory")


class _FusionIoDimmInfoAmbientTemp_Type(Integer32):
    """Custom type fusionIoDimmInfoAmbientTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_FusionIoDimmInfoAmbientTemp_Type.__name__ = "Integer32"
_FusionIoDimmInfoAmbientTemp_Object = MibTableColumn
fusionIoDimmInfoAmbientTemp = _FusionIoDimmInfoAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 45),
    _FusionIoDimmInfoAmbientTemp_Type()
)
fusionIoDimmInfoAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoAmbientTemp.setStatus("obsolete")


class _FusionIoDimmInfoPCIBandwidthCompatibility_Type(Integer32):
    """Custom type fusionIoDimmInfoPCIBandwidthCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              2048,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("incompatible", 0),
          ("suboptimal", 16),
          ("optimal", 2048),
          ("unknown", 32768))
    )


_FusionIoDimmInfoPCIBandwidthCompatibility_Type.__name__ = "Integer32"
_FusionIoDimmInfoPCIBandwidthCompatibility_Object = MibTableColumn
fusionIoDimmInfoPCIBandwidthCompatibility = _FusionIoDimmInfoPCIBandwidthCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 46),
    _FusionIoDimmInfoPCIBandwidthCompatibility_Type()
)
fusionIoDimmInfoPCIBandwidthCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPCIBandwidthCompatibility.setStatus("mandatory")


class _FusionIoDimmInfoPCIPowerCompatibility_Type(Integer32):
    """Custom type fusionIoDimmInfoPCIPowerCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              2048,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("incompatible", 0),
          ("suboptimal", 16),
          ("optimal", 2048),
          ("unknown", 32768))
    )


_FusionIoDimmInfoPCIPowerCompatibility_Type.__name__ = "Integer32"
_FusionIoDimmInfoPCIPowerCompatibility_Object = MibTableColumn
fusionIoDimmInfoPCIPowerCompatibility = _FusionIoDimmInfoPCIPowerCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 47),
    _FusionIoDimmInfoPCIPowerCompatibility_Type()
)
fusionIoDimmInfoPCIPowerCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPCIPowerCompatibility.setStatus("mandatory")


class _FusionIoDimmInfoActualGoverningLevel_Type(Integer32):
    """Custom type fusionIoDimmInfoActualGoverningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("light", 1),
          ("moderate", 2),
          ("heavy", 3),
          ("unavailable", 4))
    )


_FusionIoDimmInfoActualGoverningLevel_Type.__name__ = "Integer32"
_FusionIoDimmInfoActualGoverningLevel_Object = MibTableColumn
fusionIoDimmInfoActualGoverningLevel = _FusionIoDimmInfoActualGoverningLevel_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 48),
    _FusionIoDimmInfoActualGoverningLevel_Type()
)
fusionIoDimmInfoActualGoverningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoActualGoverningLevel.setStatus("mandatory")


class _FusionIoDimmInfoLifespanGoverningLevel_Type(Integer32):
    """Custom type fusionIoDimmInfoLifespanGoverningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("light", 1),
          ("moderate", 2),
          ("heavy", 3),
          ("unavailable", 4))
    )


_FusionIoDimmInfoLifespanGoverningLevel_Type.__name__ = "Integer32"
_FusionIoDimmInfoLifespanGoverningLevel_Object = MibTableColumn
fusionIoDimmInfoLifespanGoverningLevel = _FusionIoDimmInfoLifespanGoverningLevel_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 49),
    _FusionIoDimmInfoLifespanGoverningLevel_Type()
)
fusionIoDimmInfoLifespanGoverningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoLifespanGoverningLevel.setStatus("obsolete")


class _FusionIoDimmInfoPowerGoverningLevel_Type(Integer32):
    """Custom type fusionIoDimmInfoPowerGoverningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("light", 1),
          ("moderate", 2),
          ("heavy", 3),
          ("unavailable", 4))
    )


_FusionIoDimmInfoPowerGoverningLevel_Type.__name__ = "Integer32"
_FusionIoDimmInfoPowerGoverningLevel_Object = MibTableColumn
fusionIoDimmInfoPowerGoverningLevel = _FusionIoDimmInfoPowerGoverningLevel_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 50),
    _FusionIoDimmInfoPowerGoverningLevel_Type()
)
fusionIoDimmInfoPowerGoverningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPowerGoverningLevel.setStatus("mandatory")


class _FusionIoDimmInfoThermalGoverningLevel_Type(Integer32):
    """Custom type fusionIoDimmInfoThermalGoverningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("light", 1),
          ("moderate", 2),
          ("heavy", 3),
          ("unavailable", 4))
    )


_FusionIoDimmInfoThermalGoverningLevel_Type.__name__ = "Integer32"
_FusionIoDimmInfoThermalGoverningLevel_Object = MibTableColumn
fusionIoDimmInfoThermalGoverningLevel = _FusionIoDimmInfoThermalGoverningLevel_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 51),
    _FusionIoDimmInfoThermalGoverningLevel_Type()
)
fusionIoDimmInfoThermalGoverningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoThermalGoverningLevel.setStatus("mandatory")
_FusionIoDimmInfoLifespanGoverningEnabled_Type = Boolean
_FusionIoDimmInfoLifespanGoverningEnabled_Object = MibTableColumn
fusionIoDimmInfoLifespanGoverningEnabled = _FusionIoDimmInfoLifespanGoverningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 52),
    _FusionIoDimmInfoLifespanGoverningEnabled_Type()
)
fusionIoDimmInfoLifespanGoverningEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoLifespanGoverningEnabled.setStatus("obsolete")


class _FusionIoDimmInfoLifespanGoverningTgtDate_Type(DisplayString):
    """Custom type fusionIoDimmInfoLifespanGoverningTgtDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmInfoLifespanGoverningTgtDate_Type.__name__ = "DisplayString"
_FusionIoDimmInfoLifespanGoverningTgtDate_Object = MibTableColumn
fusionIoDimmInfoLifespanGoverningTgtDate = _FusionIoDimmInfoLifespanGoverningTgtDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 53),
    _FusionIoDimmInfoLifespanGoverningTgtDate_Type()
)
fusionIoDimmInfoLifespanGoverningTgtDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoLifespanGoverningTgtDate.setStatus("obsolete")
_FusionIoDimmInfoInternalTempCritical_Type = Boolean
_FusionIoDimmInfoInternalTempCritical_Object = MibTableColumn
fusionIoDimmInfoInternalTempCritical = _FusionIoDimmInfoInternalTempCritical_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 54),
    _FusionIoDimmInfoInternalTempCritical_Type()
)
fusionIoDimmInfoInternalTempCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoInternalTempCritical.setStatus("mandatory")
_FusionIoDimmInfoInternalTempShutdown_Type = Boolean
_FusionIoDimmInfoInternalTempShutdown_Object = MibTableColumn
fusionIoDimmInfoInternalTempShutdown = _FusionIoDimmInfoInternalTempShutdown_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 55),
    _FusionIoDimmInfoInternalTempShutdown_Type()
)
fusionIoDimmInfoInternalTempShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoInternalTempShutdown.setStatus("mandatory")


class _FusionIoDimmInfoPcieErrorsIndicator_Type(Integer32):
    """Custom type fusionIoDimmInfoPcieErrorsIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("correctable", 1),
          ("uncorrectable", 2))
    )


_FusionIoDimmInfoPcieErrorsIndicator_Type.__name__ = "Integer32"
_FusionIoDimmInfoPcieErrorsIndicator_Object = MibTableColumn
fusionIoDimmInfoPcieErrorsIndicator = _FusionIoDimmInfoPcieErrorsIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 56),
    _FusionIoDimmInfoPcieErrorsIndicator_Type()
)
fusionIoDimmInfoPcieErrorsIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoPcieErrorsIndicator.setStatus("mandatory")
_FusionIoDimmInfoMissingLebMapIndicator_Type = Boolean
_FusionIoDimmInfoMissingLebMapIndicator_Object = MibTableColumn
fusionIoDimmInfoMissingLebMapIndicator = _FusionIoDimmInfoMissingLebMapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 57),
    _FusionIoDimmInfoMissingLebMapIndicator_Type()
)
fusionIoDimmInfoMissingLebMapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoMissingLebMapIndicator.setStatus("mandatory")
_FusionIoDimmInfoVccIntErrorIndicator_Type = Boolean
_FusionIoDimmInfoVccIntErrorIndicator_Object = MibTableColumn
fusionIoDimmInfoVccIntErrorIndicator = _FusionIoDimmInfoVccIntErrorIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 58),
    _FusionIoDimmInfoVccIntErrorIndicator_Type()
)
fusionIoDimmInfoVccIntErrorIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoVccIntErrorIndicator.setStatus("mandatory")
_FusionIoDimmInfoVccAuxErrorIndicator_Type = Boolean
_FusionIoDimmInfoVccAuxErrorIndicator_Object = MibTableColumn
fusionIoDimmInfoVccAuxErrorIndicator = _FusionIoDimmInfoVccAuxErrorIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 59),
    _FusionIoDimmInfoVccAuxErrorIndicator_Type()
)
fusionIoDimmInfoVccAuxErrorIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoVccAuxErrorIndicator.setStatus("mandatory")
_FusionIoDimmInfoOverPowerIndicator_Type = Boolean
_FusionIoDimmInfoOverPowerIndicator_Object = MibTableColumn
fusionIoDimmInfoOverPowerIndicator = _FusionIoDimmInfoOverPowerIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 60),
    _FusionIoDimmInfoOverPowerIndicator_Type()
)
fusionIoDimmInfoOverPowerIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoOverPowerIndicator.setStatus("mandatory")
_FusionIoDimmInfoUpgradeInProgressIndicator_Type = Boolean
_FusionIoDimmInfoUpgradeInProgressIndicator_Object = MibTableColumn
fusionIoDimmInfoUpgradeInProgressIndicator = _FusionIoDimmInfoUpgradeInProgressIndicator_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 61),
    _FusionIoDimmInfoUpgradeInProgressIndicator_Type()
)
fusionIoDimmInfoUpgradeInProgressIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoUpgradeInProgressIndicator.setStatus("mandatory")


class _FusionIoDimmInfoInternalTempHighThreshold_Type(Integer32):
    """Custom type fusionIoDimmInfoInternalTempHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoInternalTempHighThreshold_Type.__name__ = "Integer32"
_FusionIoDimmInfoInternalTempHighThreshold_Object = MibTableColumn
fusionIoDimmInfoInternalTempHighThreshold = _FusionIoDimmInfoInternalTempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 62),
    _FusionIoDimmInfoInternalTempHighThreshold_Type()
)
fusionIoDimmInfoInternalTempHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoInternalTempHighThreshold.setStatus("mandatory")


class _FusionIoDimmInfoInternalTempCriticalThreshold_Type(Integer32):
    """Custom type fusionIoDimmInfoInternalTempCriticalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoInternalTempCriticalThreshold_Type.__name__ = "Integer32"
_FusionIoDimmInfoInternalTempCriticalThreshold_Object = MibTableColumn
fusionIoDimmInfoInternalTempCriticalThreshold = _FusionIoDimmInfoInternalTempCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 63),
    _FusionIoDimmInfoInternalTempCriticalThreshold_Type()
)
fusionIoDimmInfoInternalTempCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoInternalTempCriticalThreshold.setStatus("mandatory")


class _FusionIoDimmInfoInternalTempShutdownThreshold_Type(Integer32):
    """Custom type fusionIoDimmInfoInternalTempShutdownThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoInternalTempShutdownThreshold_Type.__name__ = "Integer32"
_FusionIoDimmInfoInternalTempShutdownThreshold_Object = MibTableColumn
fusionIoDimmInfoInternalTempShutdownThreshold = _FusionIoDimmInfoInternalTempShutdownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 64),
    _FusionIoDimmInfoInternalTempShutdownThreshold_Type()
)
fusionIoDimmInfoInternalTempShutdownThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoInternalTempShutdownThreshold.setStatus("mandatory")


class _FusionIoDimmInfoVirtualControllerNumber_Type(Integer32):
    """Custom type fusionIoDimmInfoVirtualControllerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoVirtualControllerNumber_Type.__name__ = "Integer32"
_FusionIoDimmInfoVirtualControllerNumber_Object = MibTableColumn
fusionIoDimmInfoVirtualControllerNumber = _FusionIoDimmInfoVirtualControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 65),
    _FusionIoDimmInfoVirtualControllerNumber_Type()
)
fusionIoDimmInfoVirtualControllerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoVirtualControllerNumber.setStatus("mandatory")


class _FusionIoDimmInfoVirtualControllerCount_Type(Integer32):
    """Custom type fusionIoDimmInfoVirtualControllerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FusionIoDimmInfoVirtualControllerCount_Type.__name__ = "Integer32"
_FusionIoDimmInfoVirtualControllerCount_Object = MibTableColumn
fusionIoDimmInfoVirtualControllerCount = _FusionIoDimmInfoVirtualControllerCount_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 66),
    _FusionIoDimmInfoVirtualControllerCount_Type()
)
fusionIoDimmInfoVirtualControllerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoVirtualControllerCount.setStatus("mandatory")


class _FusionIoDimmInfoActiveMediaPercent_Type(Integer32):
    """Custom type fusionIoDimmInfoActiveMediaPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FusionIoDimmInfoActiveMediaPercent_Type.__name__ = "Integer32"
_FusionIoDimmInfoActiveMediaPercent_Object = MibTableColumn
fusionIoDimmInfoActiveMediaPercent = _FusionIoDimmInfoActiveMediaPercent_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 1, 1, 1, 67),
    _FusionIoDimmInfoActiveMediaPercent_Type()
)
fusionIoDimmInfoActiveMediaPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmInfoActiveMediaPercent.setStatus("mandatory")
_FusionIoDimmExtn_ObjectIdentity = ObjectIdentity
fusionIoDimmExtn = _FusionIoDimmExtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2)
)
_FusionIoDimmExtnTable_Object = MibTable
fusionIoDimmExtnTable = _FusionIoDimmExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fusionIoDimmExtnTable.setStatus("mandatory")
_FusionIoDimmExtnEntry_Object = MibTableRow
fusionIoDimmExtnEntry = _FusionIoDimmExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1)
)
fusionIoDimmExtnEntry.setIndexNames(
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmExtnIndex"),
)
if mibBuilder.loadTexts:
    fusionIoDimmExtnEntry.setStatus("mandatory")


class _FusionIoDimmExtnIndex_Type(Integer32):
    """Custom type fusionIoDimmExtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FusionIoDimmExtnIndex_Type.__name__ = "Integer32"
_FusionIoDimmExtnIndex_Object = MibTableColumn
fusionIoDimmExtnIndex = _FusionIoDimmExtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 1),
    _FusionIoDimmExtnIndex_Type()
)
fusionIoDimmExtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnIndex.setStatus("mandatory")
_FusionIoDimmExtnTotalPhysCapacityU_Type = Counter32
_FusionIoDimmExtnTotalPhysCapacityU_Object = MibTableColumn
fusionIoDimmExtnTotalPhysCapacityU = _FusionIoDimmExtnTotalPhysCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 2),
    _FusionIoDimmExtnTotalPhysCapacityU_Type()
)
fusionIoDimmExtnTotalPhysCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnTotalPhysCapacityU.setStatus("mandatory")
_FusionIoDimmExtnTotalPhysCapacityL_Type = Counter32
_FusionIoDimmExtnTotalPhysCapacityL_Object = MibTableColumn
fusionIoDimmExtnTotalPhysCapacityL = _FusionIoDimmExtnTotalPhysCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 3),
    _FusionIoDimmExtnTotalPhysCapacityL_Type()
)
fusionIoDimmExtnTotalPhysCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnTotalPhysCapacityL.setStatus("mandatory")
_FusionIoDimmExtnUsablePhysCapacityU_Type = Counter32
_FusionIoDimmExtnUsablePhysCapacityU_Object = MibTableColumn
fusionIoDimmExtnUsablePhysCapacityU = _FusionIoDimmExtnUsablePhysCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 4),
    _FusionIoDimmExtnUsablePhysCapacityU_Type()
)
fusionIoDimmExtnUsablePhysCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnUsablePhysCapacityU.setStatus("obsolete")
_FusionIoDimmExtnUsablePhysCapacityL_Type = Counter32
_FusionIoDimmExtnUsablePhysCapacityL_Object = MibTableColumn
fusionIoDimmExtnUsablePhysCapacityL = _FusionIoDimmExtnUsablePhysCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 5),
    _FusionIoDimmExtnUsablePhysCapacityL_Type()
)
fusionIoDimmExtnUsablePhysCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnUsablePhysCapacityL.setStatus("obsolete")
_FusionIoDimmExtnUsedPhysCapacityU_Type = Counter32
_FusionIoDimmExtnUsedPhysCapacityU_Object = MibTableColumn
fusionIoDimmExtnUsedPhysCapacityU = _FusionIoDimmExtnUsedPhysCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 6),
    _FusionIoDimmExtnUsedPhysCapacityU_Type()
)
fusionIoDimmExtnUsedPhysCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnUsedPhysCapacityU.setStatus("obsolete")
_FusionIoDimmExtnUsedPhysCapacityL_Type = Counter32
_FusionIoDimmExtnUsedPhysCapacityL_Object = MibTableColumn
fusionIoDimmExtnUsedPhysCapacityL = _FusionIoDimmExtnUsedPhysCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 7),
    _FusionIoDimmExtnUsedPhysCapacityL_Type()
)
fusionIoDimmExtnUsedPhysCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnUsedPhysCapacityL.setStatus("obsolete")
_FusionIoDimmExtnTotalLogCapacityU_Type = Counter32
_FusionIoDimmExtnTotalLogCapacityU_Object = MibTableColumn
fusionIoDimmExtnTotalLogCapacityU = _FusionIoDimmExtnTotalLogCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 8),
    _FusionIoDimmExtnTotalLogCapacityU_Type()
)
fusionIoDimmExtnTotalLogCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnTotalLogCapacityU.setStatus("mandatory")
_FusionIoDimmExtnTotalLogCapacityL_Type = Counter32
_FusionIoDimmExtnTotalLogCapacityL_Object = MibTableColumn
fusionIoDimmExtnTotalLogCapacityL = _FusionIoDimmExtnTotalLogCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 9),
    _FusionIoDimmExtnTotalLogCapacityL_Type()
)
fusionIoDimmExtnTotalLogCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnTotalLogCapacityL.setStatus("mandatory")
_FusionIoDimmExtnAvailLogCapacityU_Type = Counter32
_FusionIoDimmExtnAvailLogCapacityU_Object = MibTableColumn
fusionIoDimmExtnAvailLogCapacityU = _FusionIoDimmExtnAvailLogCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 10),
    _FusionIoDimmExtnAvailLogCapacityU_Type()
)
fusionIoDimmExtnAvailLogCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnAvailLogCapacityU.setStatus("obsolete")
_FusionIoDimmExtnAvailLogCapacityL_Type = Counter32
_FusionIoDimmExtnAvailLogCapacityL_Object = MibTableColumn
fusionIoDimmExtnAvailLogCapacityL = _FusionIoDimmExtnAvailLogCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 11),
    _FusionIoDimmExtnAvailLogCapacityL_Type()
)
fusionIoDimmExtnAvailLogCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnAvailLogCapacityL.setStatus("obsolete")
_FusionIoDimmExtnBytesReadU_Type = Counter32
_FusionIoDimmExtnBytesReadU_Object = MibTableColumn
fusionIoDimmExtnBytesReadU = _FusionIoDimmExtnBytesReadU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 12),
    _FusionIoDimmExtnBytesReadU_Type()
)
fusionIoDimmExtnBytesReadU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnBytesReadU.setStatus("mandatory")
_FusionIoDimmExtnBytesReadL_Type = Counter32
_FusionIoDimmExtnBytesReadL_Object = MibTableColumn
fusionIoDimmExtnBytesReadL = _FusionIoDimmExtnBytesReadL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 13),
    _FusionIoDimmExtnBytesReadL_Type()
)
fusionIoDimmExtnBytesReadL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnBytesReadL.setStatus("mandatory")
_FusionIoDimmExtnBytesWrittenU_Type = Counter32
_FusionIoDimmExtnBytesWrittenU_Object = MibTableColumn
fusionIoDimmExtnBytesWrittenU = _FusionIoDimmExtnBytesWrittenU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 14),
    _FusionIoDimmExtnBytesWrittenU_Type()
)
fusionIoDimmExtnBytesWrittenU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnBytesWrittenU.setStatus("mandatory")
_FusionIoDimmExtnBytesWrittenL_Type = Counter32
_FusionIoDimmExtnBytesWrittenL_Object = MibTableColumn
fusionIoDimmExtnBytesWrittenL = _FusionIoDimmExtnBytesWrittenL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 15),
    _FusionIoDimmExtnBytesWrittenL_Type()
)
fusionIoDimmExtnBytesWrittenL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnBytesWrittenL.setStatus("mandatory")
_FusionIoDimmExtnLogBytesWrittenU_Type = Counter32
_FusionIoDimmExtnLogBytesWrittenU_Object = MibTableColumn
fusionIoDimmExtnLogBytesWrittenU = _FusionIoDimmExtnLogBytesWrittenU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 16),
    _FusionIoDimmExtnLogBytesWrittenU_Type()
)
fusionIoDimmExtnLogBytesWrittenU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnLogBytesWrittenU.setStatus("obsolete")
_FusionIoDimmExtnLogBytesWrittenL_Type = Counter32
_FusionIoDimmExtnLogBytesWrittenL_Object = MibTableColumn
fusionIoDimmExtnLogBytesWrittenL = _FusionIoDimmExtnLogBytesWrittenL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 17),
    _FusionIoDimmExtnLogBytesWrittenL_Type()
)
fusionIoDimmExtnLogBytesWrittenL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnLogBytesWrittenL.setStatus("obsolete")
_FusionIoDimmExtnShortTermStartDate_Type = SimpleTime
_FusionIoDimmExtnShortTermStartDate_Object = MibTableColumn
fusionIoDimmExtnShortTermStartDate = _FusionIoDimmExtnShortTermStartDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 18),
    _FusionIoDimmExtnShortTermStartDate_Type()
)
fusionIoDimmExtnShortTermStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnShortTermStartDate.setStatus("obsolete")


class _FusionIoDimmExtnShortTermWindow_Type(Integer32):
    """Custom type fusionIoDimmExtnShortTermWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_FusionIoDimmExtnShortTermWindow_Type.__name__ = "Integer32"
_FusionIoDimmExtnShortTermWindow_Object = MibTableColumn
fusionIoDimmExtnShortTermWindow = _FusionIoDimmExtnShortTermWindow_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 19),
    _FusionIoDimmExtnShortTermWindow_Type()
)
fusionIoDimmExtnShortTermWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnShortTermWindow.setStatus("obsolete")
_FusionIoDimmExtnShortTermEndDate_Type = SimpleTime
_FusionIoDimmExtnShortTermEndDate_Object = MibTableColumn
fusionIoDimmExtnShortTermEndDate = _FusionIoDimmExtnShortTermEndDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 20),
    _FusionIoDimmExtnShortTermEndDate_Type()
)
fusionIoDimmExtnShortTermEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnShortTermEndDate.setStatus("obsolete")
_FusionIoDimmExtnShortTermEndDateFloat_Type = Integer32
_FusionIoDimmExtnShortTermEndDateFloat_Object = MibTableColumn
fusionIoDimmExtnShortTermEndDateFloat = _FusionIoDimmExtnShortTermEndDateFloat_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 21),
    _FusionIoDimmExtnShortTermEndDateFloat_Type()
)
fusionIoDimmExtnShortTermEndDateFloat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnShortTermEndDateFloat.setStatus("obsolete")
_FusionIoDimmExtnLongTermStartDate_Type = SimpleTime
_FusionIoDimmExtnLongTermStartDate_Object = MibTableColumn
fusionIoDimmExtnLongTermStartDate = _FusionIoDimmExtnLongTermStartDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 22),
    _FusionIoDimmExtnLongTermStartDate_Type()
)
fusionIoDimmExtnLongTermStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnLongTermStartDate.setStatus("obsolete")


class _FusionIoDimmExtnLongTermWindow_Type(Integer32):
    """Custom type fusionIoDimmExtnLongTermWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_FusionIoDimmExtnLongTermWindow_Type.__name__ = "Integer32"
_FusionIoDimmExtnLongTermWindow_Object = MibTableColumn
fusionIoDimmExtnLongTermWindow = _FusionIoDimmExtnLongTermWindow_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 23),
    _FusionIoDimmExtnLongTermWindow_Type()
)
fusionIoDimmExtnLongTermWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnLongTermWindow.setStatus("obsolete")
_FusionIoDimmExtnLongTermEndDate_Type = SimpleTime
_FusionIoDimmExtnLongTermEndDate_Object = MibTableColumn
fusionIoDimmExtnLongTermEndDate = _FusionIoDimmExtnLongTermEndDate_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 24),
    _FusionIoDimmExtnLongTermEndDate_Type()
)
fusionIoDimmExtnLongTermEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnLongTermEndDate.setStatus("obsolete")
_FusionIoDimmExtnLongTermEndDateFloat_Type = Integer32
_FusionIoDimmExtnLongTermEndDateFloat_Object = MibTableColumn
fusionIoDimmExtnLongTermEndDateFloat = _FusionIoDimmExtnLongTermEndDateFloat_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 25),
    _FusionIoDimmExtnLongTermEndDateFloat_Type()
)
fusionIoDimmExtnLongTermEndDateFloat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnLongTermEndDateFloat.setStatus("obsolete")
_FusionIoDimmExtnWriteRateAutoCalc_Type = Integer32
_FusionIoDimmExtnWriteRateAutoCalc_Object = MibTableColumn
fusionIoDimmExtnWriteRateAutoCalc = _FusionIoDimmExtnWriteRateAutoCalc_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 26),
    _FusionIoDimmExtnWriteRateAutoCalc_Type()
)
fusionIoDimmExtnWriteRateAutoCalc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnWriteRateAutoCalc.setStatus("obsolete")
_FusionIoDimmExtnShortTermAvgU_Type = Counter32
_FusionIoDimmExtnShortTermAvgU_Object = MibTableColumn
fusionIoDimmExtnShortTermAvgU = _FusionIoDimmExtnShortTermAvgU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 27),
    _FusionIoDimmExtnShortTermAvgU_Type()
)
fusionIoDimmExtnShortTermAvgU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnShortTermAvgU.setStatus("obsolete")
_FusionIoDimmExtnShortTermAvgL_Type = Counter32
_FusionIoDimmExtnShortTermAvgL_Object = MibTableColumn
fusionIoDimmExtnShortTermAvgL = _FusionIoDimmExtnShortTermAvgL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 28),
    _FusionIoDimmExtnShortTermAvgL_Type()
)
fusionIoDimmExtnShortTermAvgL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnShortTermAvgL.setStatus("obsolete")
_FusionIoDimmExtnLongTermAvgU_Type = Counter32
_FusionIoDimmExtnLongTermAvgU_Object = MibTableColumn
fusionIoDimmExtnLongTermAvgU = _FusionIoDimmExtnLongTermAvgU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 29),
    _FusionIoDimmExtnLongTermAvgU_Type()
)
fusionIoDimmExtnLongTermAvgU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnLongTermAvgU.setStatus("obsolete")
_FusionIoDimmExtnLongTermAvgL_Type = Counter32
_FusionIoDimmExtnLongTermAvgL_Object = MibTableColumn
fusionIoDimmExtnLongTermAvgL = _FusionIoDimmExtnLongTermAvgL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 30),
    _FusionIoDimmExtnLongTermAvgL_Type()
)
fusionIoDimmExtnLongTermAvgL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnLongTermAvgL.setStatus("obsolete")


class _FusionIoDimmExtnConfidenceInterval_Type(Integer32):
    """Custom type fusionIoDimmExtnConfidenceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FusionIoDimmExtnConfidenceInterval_Type.__name__ = "Integer32"
_FusionIoDimmExtnConfidenceInterval_Object = MibTableColumn
fusionIoDimmExtnConfidenceInterval = _FusionIoDimmExtnConfidenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 31),
    _FusionIoDimmExtnConfidenceInterval_Type()
)
fusionIoDimmExtnConfidenceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionIoDimmExtnConfidenceInterval.setStatus("obsolete")


class _FusionIoDimmExtnFormattedBlockSize_Type(Integer32):
    """Custom type fusionIoDimmExtnFormattedBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 4096),
    )


_FusionIoDimmExtnFormattedBlockSize_Type.__name__ = "Integer32"
_FusionIoDimmExtnFormattedBlockSize_Object = MibTableColumn
fusionIoDimmExtnFormattedBlockSize = _FusionIoDimmExtnFormattedBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 32),
    _FusionIoDimmExtnFormattedBlockSize_Type()
)
fusionIoDimmExtnFormattedBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnFormattedBlockSize.setStatus("mandatory")
_FusionIoDimmExtnCurrentRAMUsageU_Type = Counter32
_FusionIoDimmExtnCurrentRAMUsageU_Object = MibTableColumn
fusionIoDimmExtnCurrentRAMUsageU = _FusionIoDimmExtnCurrentRAMUsageU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 33),
    _FusionIoDimmExtnCurrentRAMUsageU_Type()
)
fusionIoDimmExtnCurrentRAMUsageU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnCurrentRAMUsageU.setStatus("mandatory")
_FusionIoDimmExtnCurrentRAMUsageL_Type = Counter32
_FusionIoDimmExtnCurrentRAMUsageL_Object = MibTableColumn
fusionIoDimmExtnCurrentRAMUsageL = _FusionIoDimmExtnCurrentRAMUsageL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 34),
    _FusionIoDimmExtnCurrentRAMUsageL_Type()
)
fusionIoDimmExtnCurrentRAMUsageL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnCurrentRAMUsageL.setStatus("mandatory")
_FusionIoDimmExtnPeakRAMUsageU_Type = Counter32
_FusionIoDimmExtnPeakRAMUsageU_Object = MibTableColumn
fusionIoDimmExtnPeakRAMUsageU = _FusionIoDimmExtnPeakRAMUsageU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 35),
    _FusionIoDimmExtnPeakRAMUsageU_Type()
)
fusionIoDimmExtnPeakRAMUsageU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnPeakRAMUsageU.setStatus("mandatory")
_FusionIoDimmExtnPeakRAMUsageL_Type = Counter32
_FusionIoDimmExtnPeakRAMUsageL_Object = MibTableColumn
fusionIoDimmExtnPeakRAMUsageL = _FusionIoDimmExtnPeakRAMUsageL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 2, 1, 1, 36),
    _FusionIoDimmExtnPeakRAMUsageL_Type()
)
fusionIoDimmExtnPeakRAMUsageL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmExtnPeakRAMUsageL.setStatus("mandatory")
_FusionIoDimmCapacity_ObjectIdentity = ObjectIdentity
fusionIoDimmCapacity = _FusionIoDimmCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 3)
)
_FusionIoDimmCapacityTable_Object = MibTable
fusionIoDimmCapacityTable = _FusionIoDimmCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fusionIoDimmCapacityTable.setStatus("optional")
_FusionIoDimmCapacityEntry_Object = MibTableRow
fusionIoDimmCapacityEntry = _FusionIoDimmCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 3, 1, 1)
)
fusionIoDimmCapacityEntry.setIndexNames(
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmCapacityInfoIndex"),
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmCapacityIndex"),
)
if mibBuilder.loadTexts:
    fusionIoDimmCapacityEntry.setStatus("optional")


class _FusionIoDimmCapacityInfoIndex_Type(Integer32):
    """Custom type fusionIoDimmCapacityInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FusionIoDimmCapacityInfoIndex_Type.__name__ = "Integer32"
_FusionIoDimmCapacityInfoIndex_Object = MibTableColumn
fusionIoDimmCapacityInfoIndex = _FusionIoDimmCapacityInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 3, 1, 1, 1),
    _FusionIoDimmCapacityInfoIndex_Type()
)
fusionIoDimmCapacityInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmCapacityInfoIndex.setStatus("optional")


class _FusionIoDimmCapacityIndex_Type(Integer32):
    """Custom type fusionIoDimmCapacityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FusionIoDimmCapacityIndex_Type.__name__ = "Integer32"
_FusionIoDimmCapacityIndex_Object = MibTableColumn
fusionIoDimmCapacityIndex = _FusionIoDimmCapacityIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 3, 1, 1, 2),
    _FusionIoDimmCapacityIndex_Type()
)
fusionIoDimmCapacityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmCapacityIndex.setStatus("optional")
_FusionIoDimmCapacityValueU_Type = Counter32
_FusionIoDimmCapacityValueU_Object = MibTableColumn
fusionIoDimmCapacityValueU = _FusionIoDimmCapacityValueU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 3, 1, 1, 3),
    _FusionIoDimmCapacityValueU_Type()
)
fusionIoDimmCapacityValueU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmCapacityValueU.setStatus("optional")
_FusionIoDimmCapacityValueL_Type = Counter32
_FusionIoDimmCapacityValueL_Object = MibTableColumn
fusionIoDimmCapacityValueL = _FusionIoDimmCapacityValueL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 3, 1, 1, 4),
    _FusionIoDimmCapacityValueL_Type()
)
fusionIoDimmCapacityValueL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmCapacityValueL.setStatus("optional")
_FusionIoDimmCapacityTimestamp_Type = SimpleTime
_FusionIoDimmCapacityTimestamp_Object = MibTableColumn
fusionIoDimmCapacityTimestamp = _FusionIoDimmCapacityTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 3, 1, 1, 5),
    _FusionIoDimmCapacityTimestamp_Type()
)
fusionIoDimmCapacityTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmCapacityTimestamp.setStatus("optional")
_FusionIoDimmWrite_ObjectIdentity = ObjectIdentity
fusionIoDimmWrite = _FusionIoDimmWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 4)
)
_FusionIoDimmWriteTable_Object = MibTable
fusionIoDimmWriteTable = _FusionIoDimmWriteTable_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fusionIoDimmWriteTable.setStatus("optional")
_FusionIoDimmWriteEntry_Object = MibTableRow
fusionIoDimmWriteEntry = _FusionIoDimmWriteEntry_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 4, 1, 1)
)
fusionIoDimmWriteEntry.setIndexNames(
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmWriteInfoIndex"),
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmWriteIndex"),
)
if mibBuilder.loadTexts:
    fusionIoDimmWriteEntry.setStatus("optional")


class _FusionIoDimmWriteInfoIndex_Type(Integer32):
    """Custom type fusionIoDimmWriteInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FusionIoDimmWriteInfoIndex_Type.__name__ = "Integer32"
_FusionIoDimmWriteInfoIndex_Object = MibTableColumn
fusionIoDimmWriteInfoIndex = _FusionIoDimmWriteInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 4, 1, 1, 1),
    _FusionIoDimmWriteInfoIndex_Type()
)
fusionIoDimmWriteInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmWriteInfoIndex.setStatus("optional")


class _FusionIoDimmWriteIndex_Type(Integer32):
    """Custom type fusionIoDimmWriteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FusionIoDimmWriteIndex_Type.__name__ = "Integer32"
_FusionIoDimmWriteIndex_Object = MibTableColumn
fusionIoDimmWriteIndex = _FusionIoDimmWriteIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 4, 1, 1, 2),
    _FusionIoDimmWriteIndex_Type()
)
fusionIoDimmWriteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmWriteIndex.setStatus("optional")
_FusionIoDimmWriteValueU_Type = Counter32
_FusionIoDimmWriteValueU_Object = MibTableColumn
fusionIoDimmWriteValueU = _FusionIoDimmWriteValueU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 4, 1, 1, 3),
    _FusionIoDimmWriteValueU_Type()
)
fusionIoDimmWriteValueU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmWriteValueU.setStatus("optional")
_FusionIoDimmWriteValueL_Type = Counter32
_FusionIoDimmWriteValueL_Object = MibTableColumn
fusionIoDimmWriteValueL = _FusionIoDimmWriteValueL_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 4, 1, 1, 4),
    _FusionIoDimmWriteValueL_Type()
)
fusionIoDimmWriteValueL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmWriteValueL.setStatus("optional")
_FusionIoDimmWriteTimestamp_Type = DisplayString
_FusionIoDimmWriteTimestamp_Object = MibTableColumn
fusionIoDimmWriteTimestamp = _FusionIoDimmWriteTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 4, 1, 1, 5),
    _FusionIoDimmWriteTimestamp_Type()
)
fusionIoDimmWriteTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmWriteTimestamp.setStatus("optional")
_FusionIoDimmTemp_ObjectIdentity = ObjectIdentity
fusionIoDimmTemp = _FusionIoDimmTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 5)
)
_FusionIoDimmTempTable_Object = MibTable
fusionIoDimmTempTable = _FusionIoDimmTempTable_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    fusionIoDimmTempTable.setStatus("optional")
_FusionIoDimmTempEntry_Object = MibTableRow
fusionIoDimmTempEntry = _FusionIoDimmTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 5, 1, 1)
)
fusionIoDimmTempEntry.setIndexNames(
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmTempInfoIndex"),
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmTempIndex"),
)
if mibBuilder.loadTexts:
    fusionIoDimmTempEntry.setStatus("optional")


class _FusionIoDimmTempInfoIndex_Type(Integer32):
    """Custom type fusionIoDimmTempInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FusionIoDimmTempInfoIndex_Type.__name__ = "Integer32"
_FusionIoDimmTempInfoIndex_Object = MibTableColumn
fusionIoDimmTempInfoIndex = _FusionIoDimmTempInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 5, 1, 1, 1),
    _FusionIoDimmTempInfoIndex_Type()
)
fusionIoDimmTempInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmTempInfoIndex.setStatus("optional")


class _FusionIoDimmTempIndex_Type(Integer32):
    """Custom type fusionIoDimmTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FusionIoDimmTempIndex_Type.__name__ = "Integer32"
_FusionIoDimmTempIndex_Object = MibTableColumn
fusionIoDimmTempIndex = _FusionIoDimmTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 5, 1, 1, 2),
    _FusionIoDimmTempIndex_Type()
)
fusionIoDimmTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmTempIndex.setStatus("optional")


class _FusionIoDimmTempValue_Type(Integer32):
    """Custom type fusionIoDimmTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_FusionIoDimmTempValue_Type.__name__ = "Integer32"
_FusionIoDimmTempValue_Object = MibTableColumn
fusionIoDimmTempValue = _FusionIoDimmTempValue_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 5, 1, 1, 3),
    _FusionIoDimmTempValue_Type()
)
fusionIoDimmTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmTempValue.setStatus("optional")
_FusionIoDimmTempTimestamp_Type = SimpleTime
_FusionIoDimmTempTimestamp_Object = MibTableColumn
fusionIoDimmTempTimestamp = _FusionIoDimmTempTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 5, 1, 1, 4),
    _FusionIoDimmTempTimestamp_Type()
)
fusionIoDimmTempTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmTempTimestamp.setStatus("optional")
_FusionIoDimmProc_ObjectIdentity = ObjectIdentity
fusionIoDimmProc = _FusionIoDimmProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 6)
)
_FusionIoDimmProcTable_Object = MibTable
fusionIoDimmProcTable = _FusionIoDimmProcTable_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    fusionIoDimmProcTable.setStatus("obsolete")
_FusionIoDimmProcEntry_Object = MibTableRow
fusionIoDimmProcEntry = _FusionIoDimmProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 6, 1, 1)
)
fusionIoDimmProcEntry.setIndexNames(
    (0, "FUSIONIO-IODIMM-MIB", "fusionIoDimmProcIndex"),
)
if mibBuilder.loadTexts:
    fusionIoDimmProcEntry.setStatus("obsolete")


class _FusionIoDimmProcIndex_Type(Integer32):
    """Custom type fusionIoDimmProcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_FusionIoDimmProcIndex_Type.__name__ = "Integer32"
_FusionIoDimmProcIndex_Object = MibTableColumn
fusionIoDimmProcIndex = _FusionIoDimmProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 6, 1, 1, 1),
    _FusionIoDimmProcIndex_Type()
)
fusionIoDimmProcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmProcIndex.setStatus("obsolete")


class _FusionIoDimmProcName_Type(DisplayString):
    """Custom type fusionIoDimmProcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FusionIoDimmProcName_Type.__name__ = "DisplayString"
_FusionIoDimmProcName_Object = MibTableColumn
fusionIoDimmProcName = _FusionIoDimmProcName_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 6, 1, 1, 2),
    _FusionIoDimmProcName_Type()
)
fusionIoDimmProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmProcName.setStatus("obsolete")


class _FusionIoDimmProcState_Type(DisplayString):
    """Custom type fusionIoDimmProcState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_FusionIoDimmProcState_Type.__name__ = "DisplayString"
_FusionIoDimmProcState_Object = MibTableColumn
fusionIoDimmProcState = _FusionIoDimmProcState_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 6, 1, 1, 3),
    _FusionIoDimmProcState_Type()
)
fusionIoDimmProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmProcState.setStatus("obsolete")
_FusionIoDimmProcRAM_Type = Counter32
_FusionIoDimmProcRAM_Object = MibTableColumn
fusionIoDimmProcRAM = _FusionIoDimmProcRAM_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 6, 1, 1, 4),
    _FusionIoDimmProcRAM_Type()
)
fusionIoDimmProcRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmProcRAM.setStatus("obsolete")


class _FusionIoDimmProcCPU_Type(Integer32):
    """Custom type fusionIoDimmProcCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FusionIoDimmProcCPU_Type.__name__ = "Integer32"
_FusionIoDimmProcCPU_Object = MibTableColumn
fusionIoDimmProcCPU = _FusionIoDimmProcCPU_Object(
    (1, 3, 6, 1, 4, 1, 30018, 1, 2, 6, 1, 1, 5),
    _FusionIoDimmProcCPU_Type()
)
fusionIoDimmProcCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmProcCPU.setStatus("obsolete")
_FusionIoDimmTrapFlags_Type = Integer32
_FusionIoDimmTrapFlags_Object = MibScalar
fusionIoDimmTrapFlags = _FusionIoDimmTrapFlags_Object(
    (1, 3, 6, 1, 4, 1, 30018, 25),
    _FusionIoDimmTrapFlags_Type()
)
fusionIoDimmTrapFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionIoDimmTrapFlags.setStatus("obsolete")

# Managed Objects groups


# Notification objects

fusionIoDimmWearoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1001)
)
fusionIoDimmWearoutTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoWearoutIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"))
)
if mibBuilder.loadTexts:
    fusionIoDimmWearoutTrap.setStatus(
        ""
    )

fusionIoDimmNonWritableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1002)
)
fusionIoDimmNonWritableTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoWritableIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmNonWritableTrap.setStatus(
        ""
    )

fusionIoDimmFlashbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1003)
)
fusionIoDimmFlashbackTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFlashbackIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmFlashbackTrap.setStatus(
        ""
    )

fusionIoDimmTempHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1004)
)
fusionIoDimmTempHighTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoInternalTemp"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmTempHighTrap.setStatus(
        ""
    )

fusionIoDimmTempOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1005)
)
fusionIoDimmTempOkTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoInternalTemp"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmTempOkTrap.setStatus(
        ""
    )

fusionIoDimmErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1006)
)
fusionIoDimmErrorTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoState"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmErrorTrap.setStatus(
        ""
    )

fusionIoDimmPowerlossProtectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1007)
)
fusionIoDimmPowerlossProtectTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPowerlossProtectDisabled"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmPowerlossProtectTrap.setStatus(
        ""
    )

fusionIoDimmCriticalTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1008)
)
fusionIoDimmCriticalTempTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoInternalTemp"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmCriticalTempTrap.setStatus(
        ""
    )

fusionIoDimmShutdownTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1009)
)
fusionIoDimmShutdownTempTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoInternalTemp"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmShutdownTempTrap.setStatus(
        ""
    )

fusionIoDimmPcieErrorsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1010)
)
fusionIoDimmPcieErrorsTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPcieErrorsIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmPcieErrorsTrap.setStatus(
        ""
    )

fusionIoDimmMissingLebMapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1011)
)
fusionIoDimmMissingLebMapTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoMissingLebMapIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmMissingLebMapTrap.setStatus(
        ""
    )

fusionIoDimmSlotBandwidthIncompatibleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1012)
)
fusionIoDimmSlotBandwidthIncompatibleTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCIBandwidthCompatibility"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmSlotBandwidthIncompatibleTrap.setStatus(
        ""
    )

fusionIoDimmSlotBandwidthSuboptimalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1013)
)
fusionIoDimmSlotBandwidthSuboptimalTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCIBandwidthCompatibility"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmSlotBandwidthSuboptimalTrap.setStatus(
        ""
    )

fusionIoDimmLowReservesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1014)
)
fusionIoDimmLowReservesTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoHealthPercentage"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmLowReservesTrap.setStatus(
        ""
    )

fusionIoDimmVccIntTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1015)
)
fusionIoDimmVccIntTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoVccIntErrorIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmVccIntTrap.setStatus(
        ""
    )

fusionIoDimmVccAuxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1016)
)
fusionIoDimmVccAuxTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoVccAuxErrorIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmVccAuxTrap.setStatus(
        ""
    )

fusionIoDimmMinimalModeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1017)
)
fusionIoDimmMinimalModeTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoMinimalModeReason"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmMinimalModeTrap.setStatus(
        ""
    )

fusionIoDimmOverPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1018)
)
fusionIoDimmOverPowerTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoOverPowerIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmOverPowerTrap.setStatus(
        ""
    )

fusionIoDimmUpgradeInProgressTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 30018, 0, 1019)
)
fusionIoDimmUpgradeInProgressTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmTrapFlags"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoUpgradeInProgressIndicator"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoIndex"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoName"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoFirmwareVersion"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPartNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoSerialNumber"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoPCISlot"),
        ("FUSIONIO-IODIMM-MIB", "fusionIoDimmInfoStatus"))
)
if mibBuilder.loadTexts:
    fusionIoDimmUpgradeInProgressTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FUSIONIO-IODIMM-MIB",
    **{"SimpleTime": SimpleTime,
       "Boolean": Boolean,
       "fusionio": fusionio,
       "fusionIoDimmWearoutTrap": fusionIoDimmWearoutTrap,
       "fusionIoDimmNonWritableTrap": fusionIoDimmNonWritableTrap,
       "fusionIoDimmFlashbackTrap": fusionIoDimmFlashbackTrap,
       "fusionIoDimmTempHighTrap": fusionIoDimmTempHighTrap,
       "fusionIoDimmTempOkTrap": fusionIoDimmTempOkTrap,
       "fusionIoDimmErrorTrap": fusionIoDimmErrorTrap,
       "fusionIoDimmPowerlossProtectTrap": fusionIoDimmPowerlossProtectTrap,
       "fusionIoDimmCriticalTempTrap": fusionIoDimmCriticalTempTrap,
       "fusionIoDimmShutdownTempTrap": fusionIoDimmShutdownTempTrap,
       "fusionIoDimmPcieErrorsTrap": fusionIoDimmPcieErrorsTrap,
       "fusionIoDimmMissingLebMapTrap": fusionIoDimmMissingLebMapTrap,
       "fusionIoDimmSlotBandwidthIncompatibleTrap": fusionIoDimmSlotBandwidthIncompatibleTrap,
       "fusionIoDimmSlotBandwidthSuboptimalTrap": fusionIoDimmSlotBandwidthSuboptimalTrap,
       "fusionIoDimmLowReservesTrap": fusionIoDimmLowReservesTrap,
       "fusionIoDimmVccIntTrap": fusionIoDimmVccIntTrap,
       "fusionIoDimmVccAuxTrap": fusionIoDimmVccAuxTrap,
       "fusionIoDimmMinimalModeTrap": fusionIoDimmMinimalModeTrap,
       "fusionIoDimmOverPowerTrap": fusionIoDimmOverPowerTrap,
       "fusionIoDimmUpgradeInProgressTrap": fusionIoDimmUpgradeInProgressTrap,
       "fusionIoDimm": fusionIoDimm,
       "fusionIoDimmMib": fusionIoDimmMib,
       "fusionIoDimmMibRevMajor": fusionIoDimmMibRevMajor,
       "fusionIoDimmMibRevMinor": fusionIoDimmMibRevMinor,
       "fusionIoDimmMIBCondition": fusionIoDimmMIBCondition,
       "fusionIoDimmComponent": fusionIoDimmComponent,
       "fusionIoDimmInfo": fusionIoDimmInfo,
       "fusionIoDimmInfoTable": fusionIoDimmInfoTable,
       "fusionIoDimmInfoEntry": fusionIoDimmInfoEntry,
       "fusionIoDimmInfoIndex": fusionIoDimmInfoIndex,
       "fusionIoDimmInfoStatus": fusionIoDimmInfoStatus,
       "fusionIoDimmInfoName": fusionIoDimmInfoName,
       "fusionIoDimmInfoSerialNumber": fusionIoDimmInfoSerialNumber,
       "fusionIoDimmInfoPartNumber": fusionIoDimmInfoPartNumber,
       "fusionIoDimmInfoSubVendorPartNumber": fusionIoDimmInfoSubVendorPartNumber,
       "fusionIoDimmInfoSparePartNumber": fusionIoDimmInfoSparePartNumber,
       "fusionIoDimmInfoAssemblyNumber": fusionIoDimmInfoAssemblyNumber,
       "fusionIoDimmInfoFirmwareVersion": fusionIoDimmInfoFirmwareVersion,
       "fusionIoDimmInfoDriverVersion": fusionIoDimmInfoDriverVersion,
       "fusionIoDimmInfoUID": fusionIoDimmInfoUID,
       "fusionIoDimmInfoState": fusionIoDimmInfoState,
       "fusionIoDimmInfoClientDeviceName": fusionIoDimmInfoClientDeviceName,
       "fusionIoDimmInfoBeacon": fusionIoDimmInfoBeacon,
       "fusionIoDimmInfoPCIAddress": fusionIoDimmInfoPCIAddress,
       "fusionIoDimmInfoPCIDeviceID": fusionIoDimmInfoPCIDeviceID,
       "fusionIoDimmInfoPCISubdeviceID": fusionIoDimmInfoPCISubdeviceID,
       "fusionIoDimmInfoPCIVendorID": fusionIoDimmInfoPCIVendorID,
       "fusionIoDimmInfoPCISubvendorID": fusionIoDimmInfoPCISubvendorID,
       "fusionIoDimmInfoPCISlot": fusionIoDimmInfoPCISlot,
       "fusionIoDimmInfoWearoutIndicator": fusionIoDimmInfoWearoutIndicator,
       "fusionIoDimmInfoFlashbackIndicator": fusionIoDimmInfoFlashbackIndicator,
       "fusionIoDimmInfoWritableIndicator": fusionIoDimmInfoWritableIndicator,
       "fusionIoDimmInfoInternalTemp": fusionIoDimmInfoInternalTemp,
       "fusionIoDimmInfoHealthPercentage": fusionIoDimmInfoHealthPercentage,
       "fusionIoDimmInfoShortTermWearoutDate": fusionIoDimmInfoShortTermWearoutDate,
       "fusionIoDimmInfoLongTermWearoutDate": fusionIoDimmInfoLongTermWearoutDate,
       "fusionIoDimmInfoShortTermNonWritableDate": fusionIoDimmInfoShortTermNonWritableDate,
       "fusionIoDimmInfoLongTermNonWritableDate": fusionIoDimmInfoLongTermNonWritableDate,
       "fusionIoDimmInfoMinimalModeReason": fusionIoDimmInfoMinimalModeReason,
       "fusionIoDimmInfoReducedWriteReason": fusionIoDimmInfoReducedWriteReason,
       "fusionIoDimmInfoMilliVolts": fusionIoDimmInfoMilliVolts,
       "fusionIoDimmInfoMilliVoltsPeak": fusionIoDimmInfoMilliVoltsPeak,
       "fusionIoDimmInfoMilliVoltsMin": fusionIoDimmInfoMilliVoltsMin,
       "fusionIoDimmInfoMilliWatts": fusionIoDimmInfoMilliWatts,
       "fusionIoDimmInfoMilliWattsPeak": fusionIoDimmInfoMilliWattsPeak,
       "fusionIoDimmInfoMilliAmps": fusionIoDimmInfoMilliAmps,
       "fusionIoDimmInfoMilliAmpsPeak": fusionIoDimmInfoMilliAmpsPeak,
       "fusionIoDimmInfoAdapterType": fusionIoDimmInfoAdapterType,
       "fusionIoDimmInfoAdapterPort": fusionIoDimmInfoAdapterPort,
       "fusionIoDimmInfoAdapterSerialNumber": fusionIoDimmInfoAdapterSerialNumber,
       "fusionIoDimmInfoAdapterExtPowerPresent": fusionIoDimmInfoAdapterExtPowerPresent,
       "fusionIoDimmInfoPowerlossProtectDisabled": fusionIoDimmInfoPowerlossProtectDisabled,
       "fusionIoDimmInfoInternalTempHigh": fusionIoDimmInfoInternalTempHigh,
       "fusionIoDimmInfoAmbientTemp": fusionIoDimmInfoAmbientTemp,
       "fusionIoDimmInfoPCIBandwidthCompatibility": fusionIoDimmInfoPCIBandwidthCompatibility,
       "fusionIoDimmInfoPCIPowerCompatibility": fusionIoDimmInfoPCIPowerCompatibility,
       "fusionIoDimmInfoActualGoverningLevel": fusionIoDimmInfoActualGoverningLevel,
       "fusionIoDimmInfoLifespanGoverningLevel": fusionIoDimmInfoLifespanGoverningLevel,
       "fusionIoDimmInfoPowerGoverningLevel": fusionIoDimmInfoPowerGoverningLevel,
       "fusionIoDimmInfoThermalGoverningLevel": fusionIoDimmInfoThermalGoverningLevel,
       "fusionIoDimmInfoLifespanGoverningEnabled": fusionIoDimmInfoLifespanGoverningEnabled,
       "fusionIoDimmInfoLifespanGoverningTgtDate": fusionIoDimmInfoLifespanGoverningTgtDate,
       "fusionIoDimmInfoInternalTempCritical": fusionIoDimmInfoInternalTempCritical,
       "fusionIoDimmInfoInternalTempShutdown": fusionIoDimmInfoInternalTempShutdown,
       "fusionIoDimmInfoPcieErrorsIndicator": fusionIoDimmInfoPcieErrorsIndicator,
       "fusionIoDimmInfoMissingLebMapIndicator": fusionIoDimmInfoMissingLebMapIndicator,
       "fusionIoDimmInfoVccIntErrorIndicator": fusionIoDimmInfoVccIntErrorIndicator,
       "fusionIoDimmInfoVccAuxErrorIndicator": fusionIoDimmInfoVccAuxErrorIndicator,
       "fusionIoDimmInfoOverPowerIndicator": fusionIoDimmInfoOverPowerIndicator,
       "fusionIoDimmInfoUpgradeInProgressIndicator": fusionIoDimmInfoUpgradeInProgressIndicator,
       "fusionIoDimmInfoInternalTempHighThreshold": fusionIoDimmInfoInternalTempHighThreshold,
       "fusionIoDimmInfoInternalTempCriticalThreshold": fusionIoDimmInfoInternalTempCriticalThreshold,
       "fusionIoDimmInfoInternalTempShutdownThreshold": fusionIoDimmInfoInternalTempShutdownThreshold,
       "fusionIoDimmInfoVirtualControllerNumber": fusionIoDimmInfoVirtualControllerNumber,
       "fusionIoDimmInfoVirtualControllerCount": fusionIoDimmInfoVirtualControllerCount,
       "fusionIoDimmInfoActiveMediaPercent": fusionIoDimmInfoActiveMediaPercent,
       "fusionIoDimmExtn": fusionIoDimmExtn,
       "fusionIoDimmExtnTable": fusionIoDimmExtnTable,
       "fusionIoDimmExtnEntry": fusionIoDimmExtnEntry,
       "fusionIoDimmExtnIndex": fusionIoDimmExtnIndex,
       "fusionIoDimmExtnTotalPhysCapacityU": fusionIoDimmExtnTotalPhysCapacityU,
       "fusionIoDimmExtnTotalPhysCapacityL": fusionIoDimmExtnTotalPhysCapacityL,
       "fusionIoDimmExtnUsablePhysCapacityU": fusionIoDimmExtnUsablePhysCapacityU,
       "fusionIoDimmExtnUsablePhysCapacityL": fusionIoDimmExtnUsablePhysCapacityL,
       "fusionIoDimmExtnUsedPhysCapacityU": fusionIoDimmExtnUsedPhysCapacityU,
       "fusionIoDimmExtnUsedPhysCapacityL": fusionIoDimmExtnUsedPhysCapacityL,
       "fusionIoDimmExtnTotalLogCapacityU": fusionIoDimmExtnTotalLogCapacityU,
       "fusionIoDimmExtnTotalLogCapacityL": fusionIoDimmExtnTotalLogCapacityL,
       "fusionIoDimmExtnAvailLogCapacityU": fusionIoDimmExtnAvailLogCapacityU,
       "fusionIoDimmExtnAvailLogCapacityL": fusionIoDimmExtnAvailLogCapacityL,
       "fusionIoDimmExtnBytesReadU": fusionIoDimmExtnBytesReadU,
       "fusionIoDimmExtnBytesReadL": fusionIoDimmExtnBytesReadL,
       "fusionIoDimmExtnBytesWrittenU": fusionIoDimmExtnBytesWrittenU,
       "fusionIoDimmExtnBytesWrittenL": fusionIoDimmExtnBytesWrittenL,
       "fusionIoDimmExtnLogBytesWrittenU": fusionIoDimmExtnLogBytesWrittenU,
       "fusionIoDimmExtnLogBytesWrittenL": fusionIoDimmExtnLogBytesWrittenL,
       "fusionIoDimmExtnShortTermStartDate": fusionIoDimmExtnShortTermStartDate,
       "fusionIoDimmExtnShortTermWindow": fusionIoDimmExtnShortTermWindow,
       "fusionIoDimmExtnShortTermEndDate": fusionIoDimmExtnShortTermEndDate,
       "fusionIoDimmExtnShortTermEndDateFloat": fusionIoDimmExtnShortTermEndDateFloat,
       "fusionIoDimmExtnLongTermStartDate": fusionIoDimmExtnLongTermStartDate,
       "fusionIoDimmExtnLongTermWindow": fusionIoDimmExtnLongTermWindow,
       "fusionIoDimmExtnLongTermEndDate": fusionIoDimmExtnLongTermEndDate,
       "fusionIoDimmExtnLongTermEndDateFloat": fusionIoDimmExtnLongTermEndDateFloat,
       "fusionIoDimmExtnWriteRateAutoCalc": fusionIoDimmExtnWriteRateAutoCalc,
       "fusionIoDimmExtnShortTermAvgU": fusionIoDimmExtnShortTermAvgU,
       "fusionIoDimmExtnShortTermAvgL": fusionIoDimmExtnShortTermAvgL,
       "fusionIoDimmExtnLongTermAvgU": fusionIoDimmExtnLongTermAvgU,
       "fusionIoDimmExtnLongTermAvgL": fusionIoDimmExtnLongTermAvgL,
       "fusionIoDimmExtnConfidenceInterval": fusionIoDimmExtnConfidenceInterval,
       "fusionIoDimmExtnFormattedBlockSize": fusionIoDimmExtnFormattedBlockSize,
       "fusionIoDimmExtnCurrentRAMUsageU": fusionIoDimmExtnCurrentRAMUsageU,
       "fusionIoDimmExtnCurrentRAMUsageL": fusionIoDimmExtnCurrentRAMUsageL,
       "fusionIoDimmExtnPeakRAMUsageU": fusionIoDimmExtnPeakRAMUsageU,
       "fusionIoDimmExtnPeakRAMUsageL": fusionIoDimmExtnPeakRAMUsageL,
       "fusionIoDimmCapacity": fusionIoDimmCapacity,
       "fusionIoDimmCapacityTable": fusionIoDimmCapacityTable,
       "fusionIoDimmCapacityEntry": fusionIoDimmCapacityEntry,
       "fusionIoDimmCapacityInfoIndex": fusionIoDimmCapacityInfoIndex,
       "fusionIoDimmCapacityIndex": fusionIoDimmCapacityIndex,
       "fusionIoDimmCapacityValueU": fusionIoDimmCapacityValueU,
       "fusionIoDimmCapacityValueL": fusionIoDimmCapacityValueL,
       "fusionIoDimmCapacityTimestamp": fusionIoDimmCapacityTimestamp,
       "fusionIoDimmWrite": fusionIoDimmWrite,
       "fusionIoDimmWriteTable": fusionIoDimmWriteTable,
       "fusionIoDimmWriteEntry": fusionIoDimmWriteEntry,
       "fusionIoDimmWriteInfoIndex": fusionIoDimmWriteInfoIndex,
       "fusionIoDimmWriteIndex": fusionIoDimmWriteIndex,
       "fusionIoDimmWriteValueU": fusionIoDimmWriteValueU,
       "fusionIoDimmWriteValueL": fusionIoDimmWriteValueL,
       "fusionIoDimmWriteTimestamp": fusionIoDimmWriteTimestamp,
       "fusionIoDimmTemp": fusionIoDimmTemp,
       "fusionIoDimmTempTable": fusionIoDimmTempTable,
       "fusionIoDimmTempEntry": fusionIoDimmTempEntry,
       "fusionIoDimmTempInfoIndex": fusionIoDimmTempInfoIndex,
       "fusionIoDimmTempIndex": fusionIoDimmTempIndex,
       "fusionIoDimmTempValue": fusionIoDimmTempValue,
       "fusionIoDimmTempTimestamp": fusionIoDimmTempTimestamp,
       "fusionIoDimmProc": fusionIoDimmProc,
       "fusionIoDimmProcTable": fusionIoDimmProcTable,
       "fusionIoDimmProcEntry": fusionIoDimmProcEntry,
       "fusionIoDimmProcIndex": fusionIoDimmProcIndex,
       "fusionIoDimmProcName": fusionIoDimmProcName,
       "fusionIoDimmProcState": fusionIoDimmProcState,
       "fusionIoDimmProcRAM": fusionIoDimmProcRAM,
       "fusionIoDimmProcCPU": fusionIoDimmProcCPU,
       "fusionIoDimmTrapFlags": fusionIoDimmTrapFlags}
)
