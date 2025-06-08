# SNMP MIB module (DeltaIPMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_2254/DeltaIPMI-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:49:11 2025
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Delta_ObjectIdentity = ObjectIdentity
delta = _Delta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2)
)
_Ipmiv1_ObjectIdentity = ObjectIdentity
ipmiv1 = _Ipmiv1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100)
)
_DipmiInfo_ObjectIdentity = ObjectIdentity
dipmiInfo = _DipmiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1)
)
_DipmiDeviceNum_Type = Integer32
_DipmiDeviceNum_Object = MibScalar
dipmiDeviceNum = _DipmiDeviceNum_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 1),
    _DipmiDeviceNum_Type()
)
dipmiDeviceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiDeviceNum.setStatus("mandatory")
_DipmiTemplateNum_Type = Integer32
_DipmiTemplateNum_Object = MibScalar
dipmiTemplateNum = _DipmiTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 2),
    _DipmiTemplateNum_Type()
)
dipmiTemplateNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiTemplateNum.setStatus("mandatory")
_DipmiDeviceInfoTable_Object = MibTable
dipmiDeviceInfoTable = _DipmiDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3)
)
if mibBuilder.loadTexts:
    dipmiDeviceInfoTable.setStatus("mandatory")
_DipmiDeviceInfoTableEntry_Object = MibTableRow
dipmiDeviceInfoTableEntry = _DipmiDeviceInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1)
)
dipmiDeviceInfoTableEntry.setIndexNames(
    (0, "DeltaIPMI-MIB", "dipmiDeviceInfoID"),
)
if mibBuilder.loadTexts:
    dipmiDeviceInfoTableEntry.setStatus("mandatory")


class _DipmiDeviceInfoID_Type(Integer32):
    """Custom type dipmiDeviceInfoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 420),
    )


_DipmiDeviceInfoID_Type.__name__ = "Integer32"
_DipmiDeviceInfoID_Object = MibTableColumn
dipmiDeviceInfoID = _DipmiDeviceInfoID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 1),
    _DipmiDeviceInfoID_Type()
)
dipmiDeviceInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiDeviceInfoID.setStatus("mandatory")


class _DipmiDeviceName_Type(DisplayString):
    """Custom type dipmiDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DipmiDeviceName_Type.__name__ = "DisplayString"
_DipmiDeviceName_Object = MibTableColumn
dipmiDeviceName = _DipmiDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 2),
    _DipmiDeviceName_Type()
)
dipmiDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiDeviceName.setStatus("mandatory")


class _DipmiState_Type(Integer32):
    """Custom type dipmiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("poweroff", 2),
          ("poweron", 3))
    )


_DipmiState_Type.__name__ = "Integer32"
_DipmiState_Object = MibTableColumn
dipmiState = _DipmiState_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 3),
    _DipmiState_Type()
)
dipmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiState.setStatus("mandatory")


class _DipmiFirmwareRev_Type(DisplayString):
    """Custom type dipmiFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DipmiFirmwareRev_Type.__name__ = "DisplayString"
_DipmiFirmwareRev_Object = MibTableColumn
dipmiFirmwareRev = _DipmiFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 4),
    _DipmiFirmwareRev_Type()
)
dipmiFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiFirmwareRev.setStatus("mandatory")
_DipmiManufacturerName_Type = DisplayString
_DipmiManufacturerName_Object = MibTableColumn
dipmiManufacturerName = _DipmiManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 5),
    _DipmiManufacturerName_Type()
)
dipmiManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiManufacturerName.setStatus("mandatory")
_DipmiIPAddress_Type = IpAddress
_DipmiIPAddress_Object = MibTableColumn
dipmiIPAddress = _DipmiIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 6),
    _DipmiIPAddress_Type()
)
dipmiIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiIPAddress.setStatus("mandatory")


class _DipmiPowerControl_Type(Integer32):
    """Custom type dipmiPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("powerdown", 1),
          ("powerup", 2),
          ("powercycle", 3),
          ("hardreset", 4),
          ("softshutdown", 5))
    )


_DipmiPowerControl_Type.__name__ = "Integer32"
_DipmiPowerControl_Object = MibTableColumn
dipmiPowerControl = _DipmiPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 7),
    _DipmiPowerControl_Type()
)
dipmiPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dipmiPowerControl.setStatus("mandatory")
_DipmiModelName_Type = DisplayString
_DipmiModelName_Object = MibTableColumn
dipmiModelName = _DipmiModelName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 8),
    _DipmiModelName_Type()
)
dipmiModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiModelName.setStatus("mandatory")
_DipmiSN_Type = DisplayString
_DipmiSN_Object = MibTableColumn
dipmiSN = _DipmiSN_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 3, 1, 9),
    _DipmiSN_Type()
)
dipmiSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiSN.setStatus("mandatory")
_DipmiScanInfoTableSize_Type = Integer32
_DipmiScanInfoTableSize_Object = MibScalar
dipmiScanInfoTableSize = _DipmiScanInfoTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 4),
    _DipmiScanInfoTableSize_Type()
)
dipmiScanInfoTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoTableSize.setStatus("mandatory")
_DipmiScanInfoTable_Object = MibTable
dipmiScanInfoTable = _DipmiScanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5)
)
if mibBuilder.loadTexts:
    dipmiScanInfoTable.setStatus("mandatory")
_DipmiScanInfoTableEntry_Object = MibTableRow
dipmiScanInfoTableEntry = _DipmiScanInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1)
)
dipmiScanInfoTableEntry.setIndexNames(
    (0, "DeltaIPMI-MIB", "dipmiScanInfoDeviceID"),
    (0, "DeltaIPMI-MIB", "dipmiScanInfoID"),
)
if mibBuilder.loadTexts:
    dipmiScanInfoTableEntry.setStatus("mandatory")


class _DipmiScanInfoDeviceID_Type(Integer32):
    """Custom type dipmiScanInfoDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 420),
    )


_DipmiScanInfoDeviceID_Type.__name__ = "Integer32"
_DipmiScanInfoDeviceID_Object = MibTableColumn
dipmiScanInfoDeviceID = _DipmiScanInfoDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 1),
    _DipmiScanInfoDeviceID_Type()
)
dipmiScanInfoDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoDeviceID.setStatus("mandatory")


class _DipmiScanInfoID_Type(Integer32):
    """Custom type dipmiScanInfoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DipmiScanInfoID_Type.__name__ = "Integer32"
_DipmiScanInfoID_Object = MibTableColumn
dipmiScanInfoID = _DipmiScanInfoID_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 2),
    _DipmiScanInfoID_Type()
)
dipmiScanInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoID.setStatus("mandatory")


class _DipmiScanInfoSensorName_Type(DisplayString):
    """Custom type dipmiScanInfoSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DipmiScanInfoSensorName_Type.__name__ = "DisplayString"
_DipmiScanInfoSensorName_Object = MibTableColumn
dipmiScanInfoSensorName = _DipmiScanInfoSensorName_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 3),
    _DipmiScanInfoSensorName_Type()
)
dipmiScanInfoSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoSensorName.setStatus("mandatory")
_DipmiScanInfoSensorReading_Type = Integer32
_DipmiScanInfoSensorReading_Object = MibTableColumn
dipmiScanInfoSensorReading = _DipmiScanInfoSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 4),
    _DipmiScanInfoSensorReading_Type()
)
dipmiScanInfoSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoSensorReading.setStatus("mandatory")


class _DipmiScanInfoSensorType_Type(DisplayString):
    """Custom type dipmiScanInfoSensorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DipmiScanInfoSensorType_Type.__name__ = "DisplayString"
_DipmiScanInfoSensorType_Object = MibTableColumn
dipmiScanInfoSensorType = _DipmiScanInfoSensorType_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 5),
    _DipmiScanInfoSensorType_Type()
)
dipmiScanInfoSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoSensorType.setStatus("mandatory")


class _DipmiScanInfoSensorUnit_Type(DisplayString):
    """Custom type dipmiScanInfoSensorUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DipmiScanInfoSensorUnit_Type.__name__ = "DisplayString"
_DipmiScanInfoSensorUnit_Object = MibTableColumn
dipmiScanInfoSensorUnit = _DipmiScanInfoSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 6),
    _DipmiScanInfoSensorUnit_Type()
)
dipmiScanInfoSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoSensorUnit.setStatus("mandatory")
_DipmiScanInfoUNR_Type = Integer32
_DipmiScanInfoUNR_Object = MibTableColumn
dipmiScanInfoUNR = _DipmiScanInfoUNR_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 7),
    _DipmiScanInfoUNR_Type()
)
dipmiScanInfoUNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoUNR.setStatus("mandatory")
_DipmiScanInfoUC_Type = Integer32
_DipmiScanInfoUC_Object = MibTableColumn
dipmiScanInfoUC = _DipmiScanInfoUC_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 8),
    _DipmiScanInfoUC_Type()
)
dipmiScanInfoUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoUC.setStatus("mandatory")
_DipmiScanInfoUNC_Type = Integer32
_DipmiScanInfoUNC_Object = MibTableColumn
dipmiScanInfoUNC = _DipmiScanInfoUNC_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 9),
    _DipmiScanInfoUNC_Type()
)
dipmiScanInfoUNC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoUNC.setStatus("mandatory")
_DipmiScanInfoLNC_Type = Integer32
_DipmiScanInfoLNC_Object = MibTableColumn
dipmiScanInfoLNC = _DipmiScanInfoLNC_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 10),
    _DipmiScanInfoLNC_Type()
)
dipmiScanInfoLNC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoLNC.setStatus("mandatory")
_DipmiScanInfoLC_Type = Integer32
_DipmiScanInfoLC_Object = MibTableColumn
dipmiScanInfoLC = _DipmiScanInfoLC_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 11),
    _DipmiScanInfoLC_Type()
)
dipmiScanInfoLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoLC.setStatus("mandatory")
_DipmiScanInfoLNR_Type = Integer32
_DipmiScanInfoLNR_Object = MibTableColumn
dipmiScanInfoLNR = _DipmiScanInfoLNR_Object(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 1, 5, 1, 12),
    _DipmiScanInfoLNR_Type()
)
dipmiScanInfoLNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dipmiScanInfoLNR.setStatus("mandatory")
_DipmiTraps_ObjectIdentity = ObjectIdentity
dipmiTraps = _DipmiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20)
)

# Managed Objects groups


# Notification objects

dipmiCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20, 0, 1)
)
dipmiCommunicationLost.setObjects(
    ("DeltaIPMI-MIB", "dipmiDeviceName")
)
if mibBuilder.loadTexts:
    dipmiCommunicationLost.setStatus(
        ""
    )

dipmiCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20, 0, 2)
)
dipmiCommunicationEstablished.setObjects(
    ("DeltaIPMI-MIB", "dipmiDeviceName")
)
if mibBuilder.loadTexts:
    dipmiCommunicationEstablished.setStatus(
        ""
    )

dipmiSensorNonCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20, 0, 3)
)
dipmiSensorNonCritical.setObjects(
      *(("DeltaIPMI-MIB", "dipmiDeviceName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorReading"))
)
if mibBuilder.loadTexts:
    dipmiSensorNonCritical.setStatus(
        ""
    )

dipmiSensorNonCriticalRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20, 0, 4)
)
dipmiSensorNonCriticalRecover.setObjects(
      *(("DeltaIPMI-MIB", "dipmiDeviceName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorReading"))
)
if mibBuilder.loadTexts:
    dipmiSensorNonCriticalRecover.setStatus(
        ""
    )

dipmiSensorCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20, 0, 5)
)
dipmiSensorCritical.setObjects(
      *(("DeltaIPMI-MIB", "dipmiDeviceName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorReading"))
)
if mibBuilder.loadTexts:
    dipmiSensorCritical.setStatus(
        ""
    )

dipmiSensorCriticalRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20, 0, 6)
)
dipmiSensorCriticalRecover.setObjects(
      *(("DeltaIPMI-MIB", "dipmiDeviceName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorReading"))
)
if mibBuilder.loadTexts:
    dipmiSensorCriticalRecover.setStatus(
        ""
    )

dipmiSensorNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20, 0, 7)
)
dipmiSensorNonRecoverable.setObjects(
      *(("DeltaIPMI-MIB", "dipmiDeviceName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorReading"))
)
if mibBuilder.loadTexts:
    dipmiSensorNonRecoverable.setStatus(
        ""
    )

dipmiSensorNonRecoverableRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2254, 2, 100, 20, 0, 8)
)
dipmiSensorNonRecoverableRecover.setObjects(
      *(("DeltaIPMI-MIB", "dipmiDeviceName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorName"),
        ("DeltaIPMI-MIB", "dipmiScanInfoSensorReading"))
)
if mibBuilder.loadTexts:
    dipmiSensorNonRecoverableRecover.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DeltaIPMI-MIB",
    **{"delta": delta,
       "ups": ups,
       "ipmiv1": ipmiv1,
       "dipmiInfo": dipmiInfo,
       "dipmiDeviceNum": dipmiDeviceNum,
       "dipmiTemplateNum": dipmiTemplateNum,
       "dipmiDeviceInfoTable": dipmiDeviceInfoTable,
       "dipmiDeviceInfoTableEntry": dipmiDeviceInfoTableEntry,
       "dipmiDeviceInfoID": dipmiDeviceInfoID,
       "dipmiDeviceName": dipmiDeviceName,
       "dipmiState": dipmiState,
       "dipmiFirmwareRev": dipmiFirmwareRev,
       "dipmiManufacturerName": dipmiManufacturerName,
       "dipmiIPAddress": dipmiIPAddress,
       "dipmiPowerControl": dipmiPowerControl,
       "dipmiModelName": dipmiModelName,
       "dipmiSN": dipmiSN,
       "dipmiScanInfoTableSize": dipmiScanInfoTableSize,
       "dipmiScanInfoTable": dipmiScanInfoTable,
       "dipmiScanInfoTableEntry": dipmiScanInfoTableEntry,
       "dipmiScanInfoDeviceID": dipmiScanInfoDeviceID,
       "dipmiScanInfoID": dipmiScanInfoID,
       "dipmiScanInfoSensorName": dipmiScanInfoSensorName,
       "dipmiScanInfoSensorReading": dipmiScanInfoSensorReading,
       "dipmiScanInfoSensorType": dipmiScanInfoSensorType,
       "dipmiScanInfoSensorUnit": dipmiScanInfoSensorUnit,
       "dipmiScanInfoUNR": dipmiScanInfoUNR,
       "dipmiScanInfoUC": dipmiScanInfoUC,
       "dipmiScanInfoUNC": dipmiScanInfoUNC,
       "dipmiScanInfoLNC": dipmiScanInfoLNC,
       "dipmiScanInfoLC": dipmiScanInfoLC,
       "dipmiScanInfoLNR": dipmiScanInfoLNR,
       "dipmiTraps": dipmiTraps,
       "dipmiCommunicationLost": dipmiCommunicationLost,
       "dipmiCommunicationEstablished": dipmiCommunicationEstablished,
       "dipmiSensorNonCritical": dipmiSensorNonCritical,
       "dipmiSensorNonCriticalRecover": dipmiSensorNonCriticalRecover,
       "dipmiSensorCritical": dipmiSensorCritical,
       "dipmiSensorCriticalRecover": dipmiSensorCriticalRecover,
       "dipmiSensorNonRecoverable": dipmiSensorNonRecoverable,
       "dipmiSensorNonRecoverableRecover": dipmiSensorNonRecoverableRecover}
)
