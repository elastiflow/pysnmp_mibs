# SNMP MIB module (NETSURE-MIB-004-A) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_6302/NETSURE-MIB-004-A.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:37:40 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

powerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("unknown", 1),
          ("normal", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6),
          ("unmanaged", 7),
          ("restricted", 8),
          ("testing", 9),
          ("disabled", 10))
    )



class StatusChange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Ees_ObjectIdentity = ObjectIdentity
ees = _Ees_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302)
)
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2)
)
_Ident_ObjectIdentity = ObjectIdentity
ident = _Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1)
)
_IdentManufacturer_Type = DisplayString
_IdentManufacturer_Object = MibScalar
identManufacturer = _IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 1),
    _IdentManufacturer_Type()
)
identManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identManufacturer.setStatus("current")
_IdentModel_Type = DisplayString
_IdentModel_Object = MibScalar
identModel = _IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 2),
    _IdentModel_Type()
)
identModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identModel.setStatus("current")
_IdentControllerFirmwareVersion_Type = DisplayString
_IdentControllerFirmwareVersion_Object = MibScalar
identControllerFirmwareVersion = _IdentControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 3),
    _IdentControllerFirmwareVersion_Type()
)
identControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identControllerFirmwareVersion.setStatus("current")
_IdentName_Type = DisplayString
_IdentName_Object = MibScalar
identName = _IdentName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 4),
    _IdentName_Type()
)
identName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identName.setStatus("current")
_IdentSNMPCfgVer_Type = DisplayString
_IdentSNMPCfgVer_Object = MibScalar
identSNMPCfgVer = _IdentSNMPCfgVer_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 1, 5),
    _IdentSNMPCfgVer_Type()
)
identSNMPCfgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identSNMPCfgVer.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2)
)
_SystemStatus_Type = Status
_SystemStatus_Object = MibScalar
systemStatus = _SystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 1),
    _SystemStatus_Type()
)
systemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatus.setStatus("current")
_SystemVoltage_Type = Integer32
_SystemVoltage_Object = MibScalar
systemVoltage = _SystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 2),
    _SystemVoltage_Type()
)
systemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVoltage.setStatus("current")
_SystemCurrent_Type = Integer32
_SystemCurrent_Object = MibScalar
systemCurrent = _SystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 3),
    _SystemCurrent_Type()
)
systemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCurrent.setStatus("current")
_SystemUsedCapacity_Type = Integer32
_SystemUsedCapacity_Object = MibScalar
systemUsedCapacity = _SystemUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 4),
    _SystemUsedCapacity_Type()
)
systemUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUsedCapacity.setStatus("current")
_PsBattery_ObjectIdentity = ObjectIdentity
psBattery = _PsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5)
)
_PsBatteryVoltage_Type = Integer32
_PsBatteryVoltage_Object = MibScalar
psBatteryVoltage = _PsBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 1),
    _PsBatteryVoltage_Type()
)
psBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryVoltage.setStatus("current")
_PsTotalBatteryCurrent_Type = Integer32
_PsTotalBatteryCurrent_Object = MibScalar
psTotalBatteryCurrent = _PsTotalBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 2),
    _PsTotalBatteryCurrent_Type()
)
psTotalBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTotalBatteryCurrent.setStatus("current")
_PsBatteryCapacity_Type = Integer32
_PsBatteryCapacity_Object = MibScalar
psBatteryCapacity = _PsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 3),
    _PsBatteryCapacity_Type()
)
psBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryCapacity.setStatus("current")
_PsBatteryNominalCapacity_Type = Integer32
_PsBatteryNominalCapacity_Object = MibScalar
psBatteryNominalCapacity = _PsBatteryNominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 4),
    _PsBatteryNominalCapacity_Type()
)
psBatteryNominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryNominalCapacity.setStatus("current")
_PsBatteryTable_Object = MibTable
psBatteryTable = _PsBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    psBatteryTable.setStatus("current")
_PsBatteryEntry_Object = MibTableRow
psBatteryEntry = _PsBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5, 1)
)
psBatteryEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psBatteryIndex"),
)
if mibBuilder.loadTexts:
    psBatteryEntry.setStatus("current")


class _PsBatteryIndex_Type(Integer32):
    """Custom type psBatteryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PsBatteryIndex_Type.__name__ = "Integer32"
_PsBatteryIndex_Object = MibTableColumn
psBatteryIndex = _PsBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5, 1, 1),
    _PsBatteryIndex_Type()
)
psBatteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryIndex.setStatus("current")
_PsBatteryCurrent_Type = Integer32
_PsBatteryCurrent_Object = MibTableColumn
psBatteryCurrent = _PsBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5, 1, 2),
    _PsBatteryCurrent_Type()
)
psBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryCurrent.setStatus("current")
_PsBatteryName_Type = DisplayString
_PsBatteryName_Object = MibTableColumn
psBatteryName = _PsBatteryName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 5, 5, 1, 3),
    _PsBatteryName_Type()
)
psBatteryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBatteryName.setStatus("current")
_PsInput_ObjectIdentity = ObjectIdentity
psInput = _PsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6)
)
_PsInputLineAVoltage_Type = Integer32
_PsInputLineAVoltage_Object = MibScalar
psInputLineAVoltage = _PsInputLineAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 1),
    _PsInputLineAVoltage_Type()
)
psInputLineAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineAVoltage.setStatus("current")
_PsInputLineBVoltage_Type = Integer32
_PsInputLineBVoltage_Object = MibScalar
psInputLineBVoltage = _PsInputLineBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 2),
    _PsInputLineBVoltage_Type()
)
psInputLineBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineBVoltage.setStatus("current")
_PsInputLineCVoltage_Type = Integer32
_PsInputLineCVoltage_Object = MibScalar
psInputLineCVoltage = _PsInputLineCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 6, 3),
    _PsInputLineCVoltage_Type()
)
psInputLineCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psInputLineCVoltage.setStatus("current")
_PsTemperature_ObjectIdentity = ObjectIdentity
psTemperature = _PsTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7)
)
_PsTemperature1_Type = Integer32
_PsTemperature1_Object = MibScalar
psTemperature1 = _PsTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 1),
    _PsTemperature1_Type()
)
psTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperature1.setStatus("current")
_PsTemperature2_Type = Integer32
_PsTemperature2_Object = MibScalar
psTemperature2 = _PsTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 2),
    _PsTemperature2_Type()
)
psTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperature2.setStatus("current")
_PsTemperatureTable_Object = MibTable
psTemperatureTable = _PsTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    psTemperatureTable.setStatus("current")
_PsTemperatureEntry_Object = MibTableRow
psTemperatureEntry = _PsTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1)
)
psTemperatureEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psTemperatureIndex"),
)
if mibBuilder.loadTexts:
    psTemperatureEntry.setStatus("current")


class _PsTemperatureIndex_Type(Integer32):
    """Custom type psTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 71),
    )


_PsTemperatureIndex_Type.__name__ = "Integer32"
_PsTemperatureIndex_Object = MibTableColumn
psTemperatureIndex = _PsTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 1),
    _PsTemperatureIndex_Type()
)
psTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureIndex.setStatus("current")
_PsTemperatureMeasurement_Type = Integer32
_PsTemperatureMeasurement_Object = MibTableColumn
psTemperatureMeasurement = _PsTemperatureMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 2),
    _PsTemperatureMeasurement_Type()
)
psTemperatureMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureMeasurement.setStatus("current")
_PsTemperatureName_Type = DisplayString
_PsTemperatureName_Object = MibTableColumn
psTemperatureName = _PsTemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 3),
    _PsTemperatureName_Type()
)
psTemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureName.setStatus("current")


class _PsTemperatureType_Type(Integer32):
    """Custom type psTemperatureType based on Integer32"""
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
          ("ambient", 1),
          ("battery", 2))
    )


_PsTemperatureType_Type.__name__ = "Integer32"
_PsTemperatureType_Object = MibTableColumn
psTemperatureType = _PsTemperatureType_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 4),
    _PsTemperatureType_Type()
)
psTemperatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureType.setStatus("current")


class _PsTemperatureAlarmStatus_Type(Integer32):
    """Custom type psTemperatureAlarmStatus based on Integer32"""
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
        *(("high", 0),
          ("low", 1),
          ("fail", 2),
          ("none", 3))
    )


_PsTemperatureAlarmStatus_Type.__name__ = "Integer32"
_PsTemperatureAlarmStatus_Object = MibTableColumn
psTemperatureAlarmStatus = _PsTemperatureAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 7, 3, 1, 5),
    _PsTemperatureAlarmStatus_Type()
)
psTemperatureAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTemperatureAlarmStatus.setStatus("current")


class _PsStatusCommunication_Type(Integer32):
    """Custom type psStatusCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("normal", 2),
          ("interrupt", 3))
    )


_PsStatusCommunication_Type.__name__ = "Integer32"
_PsStatusCommunication_Object = MibScalar
psStatusCommunication = _PsStatusCommunication_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 8),
    _PsStatusCommunication_Type()
)
psStatusCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStatusCommunication.setStatus("current")


class _PsStatusBatteryMode_Type(Integer32):
    """Custom type psStatusBatteryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("unknown", 1),
          ("floatCharging", 2),
          ("shortTest", 3),
          ("bcForTest", 4),
          ("manualTesting", 5),
          ("planTesting", 6),
          ("acFailTesting", 7),
          ("acFail", 8),
          ("manualBC", 9),
          ("autoBC", 10),
          ("cyclicBC", 11),
          ("masterBC", 12),
          ("masterBT", 13))
    )


_PsStatusBatteryMode_Type.__name__ = "Integer32"
_PsStatusBatteryMode_Object = MibScalar
psStatusBatteryMode = _PsStatusBatteryMode_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 9),
    _PsStatusBatteryMode_Type()
)
psStatusBatteryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psStatusBatteryMode.setStatus("current")
_PsSMNumber_ObjectIdentity = ObjectIdentity
psSMNumber = _PsSMNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10)
)
_PsSMACNumber_Type = Integer32
_PsSMACNumber_Object = MibScalar
psSMACNumber = _PsSMACNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 1),
    _PsSMACNumber_Type()
)
psSMACNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMACNumber.setStatus("current")
_PsSMBATNumber_Type = Integer32
_PsSMBATNumber_Object = MibScalar
psSMBATNumber = _PsSMBATNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 2),
    _PsSMBATNumber_Type()
)
psSMBATNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMBATNumber.setStatus("current")
_PsSMIONumber_Type = Integer32
_PsSMIONumber_Object = MibScalar
psSMIONumber = _PsSMIONumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 10, 3),
    _PsSMIONumber_Type()
)
psSMIONumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMIONumber.setStatus("current")
_PsRectifier_ObjectIdentity = ObjectIdentity
psRectifier = _PsRectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11)
)
_NumberOfInstalledRectifiers_Type = Integer32
_NumberOfInstalledRectifiers_Object = MibScalar
numberOfInstalledRectifiers = _NumberOfInstalledRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 1),
    _NumberOfInstalledRectifiers_Type()
)
numberOfInstalledRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfInstalledRectifiers.setStatus("current")
_NumberOfRectifiersCommunicating_Type = Integer32
_NumberOfRectifiersCommunicating_Object = MibScalar
numberOfRectifiersCommunicating = _NumberOfRectifiersCommunicating_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 2),
    _NumberOfRectifiersCommunicating_Type()
)
numberOfRectifiersCommunicating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfRectifiersCommunicating.setStatus("current")
_RectifiersUsedCapacity_Type = Integer32
_RectifiersUsedCapacity_Object = MibScalar
rectifiersUsedCapacity = _RectifiersUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 3),
    _RectifiersUsedCapacity_Type()
)
rectifiersUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersUsedCapacity.setStatus("current")
_PsRectifierTable_Object = MibTable
psRectifierTable = _PsRectifierTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    psRectifierTable.setStatus("current")
_PsRectifierEntry_Object = MibTableRow
psRectifierEntry = _PsRectifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1)
)
psRectifierEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psRectifierIndex"),
)
if mibBuilder.loadTexts:
    psRectifierEntry.setStatus("current")


class _PsRectifierIndex_Type(Integer32):
    """Custom type psRectifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_PsRectifierIndex_Type.__name__ = "Integer32"
_PsRectifierIndex_Object = MibTableColumn
psRectifierIndex = _PsRectifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 1),
    _PsRectifierIndex_Type()
)
psRectifierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierIndex.setStatus("current")
_PsRectifierProductNumber_Type = DisplayString
_PsRectifierProductNumber_Object = MibTableColumn
psRectifierProductNumber = _PsRectifierProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 2),
    _PsRectifierProductNumber_Type()
)
psRectifierProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierProductNumber.setStatus("current")
_PsRectifierHWVersion_Type = DisplayString
_PsRectifierHWVersion_Object = MibTableColumn
psRectifierHWVersion = _PsRectifierHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 3),
    _PsRectifierHWVersion_Type()
)
psRectifierHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierHWVersion.setStatus("current")
_PsRectifierSWVersion_Type = DisplayString
_PsRectifierSWVersion_Object = MibTableColumn
psRectifierSWVersion = _PsRectifierSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 4),
    _PsRectifierSWVersion_Type()
)
psRectifierSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierSWVersion.setStatus("current")
_PsRectifierSerialNumber_Type = DisplayString
_PsRectifierSerialNumber_Object = MibTableColumn
psRectifierSerialNumber = _PsRectifierSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 5),
    _PsRectifierSerialNumber_Type()
)
psRectifierSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierSerialNumber.setStatus("current")
_PsRectifierCurrent_Type = Integer32
_PsRectifierCurrent_Object = MibTableColumn
psRectifierCurrent = _PsRectifierCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 6),
    _PsRectifierCurrent_Type()
)
psRectifierCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierCurrent.setStatus("current")
_PsRectifierIdent_Type = DisplayString
_PsRectifierIdent_Object = MibTableColumn
psRectifierIdent = _PsRectifierIdent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 7),
    _PsRectifierIdent_Type()
)
psRectifierIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierIdent.setStatus("current")
_PsRectifierFail_Type = StatusChange
_PsRectifierFail_Object = MibTableColumn
psRectifierFail = _PsRectifierFail_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 11, 4, 1, 8),
    _PsRectifierFail_Type()
)
psRectifierFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psRectifierFail.setStatus("current")
_PsDistribution_ObjectIdentity = ObjectIdentity
psDistribution = _PsDistribution_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12)
)
_PsTotalLoadCurrent_Type = Integer32
_PsTotalLoadCurrent_Object = MibScalar
psTotalLoadCurrent = _PsTotalLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 1),
    _PsTotalLoadCurrent_Type()
)
psTotalLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTotalLoadCurrent.setStatus("current")
_PsDistributionLoadTable_Object = MibTable
psDistributionLoadTable = _PsDistributionLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    psDistributionLoadTable.setStatus("current")
_PsDistributionLoadEntry_Object = MibTableRow
psDistributionLoadEntry = _PsDistributionLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2, 1)
)
psDistributionLoadEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psDistributionLoadIndex"),
)
if mibBuilder.loadTexts:
    psDistributionLoadEntry.setStatus("current")


class _PsDistributionLoadIndex_Type(Integer32):
    """Custom type psDistributionLoadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268386303),
    )


_PsDistributionLoadIndex_Type.__name__ = "Integer32"
_PsDistributionLoadIndex_Object = MibTableColumn
psDistributionLoadIndex = _PsDistributionLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2, 1, 1),
    _PsDistributionLoadIndex_Type()
)
psDistributionLoadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psDistributionLoadIndex.setStatus("current")
_PsDistributionLoadCurrent_Type = Integer32
_PsDistributionLoadCurrent_Object = MibTableColumn
psDistributionLoadCurrent = _PsDistributionLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2, 1, 2),
    _PsDistributionLoadCurrent_Type()
)
psDistributionLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDistributionLoadCurrent.setStatus("current")
_PsDistributionLoadName_Type = DisplayString
_PsDistributionLoadName_Object = MibTableColumn
psDistributionLoadName = _PsDistributionLoadName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 2, 1, 3),
    _PsDistributionLoadName_Type()
)
psDistributionLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDistributionLoadName.setStatus("current")
_PsDistributionGeneralTable_Object = MibTable
psDistributionGeneralTable = _PsDistributionGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    psDistributionGeneralTable.setStatus("current")
_PsDistributionGeneralEntry_Object = MibTableRow
psDistributionGeneralEntry = _PsDistributionGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3, 1)
)
psDistributionGeneralEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psDistributionGeneralIndex"),
)
if mibBuilder.loadTexts:
    psDistributionGeneralEntry.setStatus("current")


class _PsDistributionGeneralIndex_Type(Integer32):
    """Custom type psDistributionGeneralIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268386303),
    )


_PsDistributionGeneralIndex_Type.__name__ = "Integer32"
_PsDistributionGeneralIndex_Object = MibTableColumn
psDistributionGeneralIndex = _PsDistributionGeneralIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3, 1, 1),
    _PsDistributionGeneralIndex_Type()
)
psDistributionGeneralIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psDistributionGeneralIndex.setStatus("current")
_PsDistributionGeneralCurrent_Type = Integer32
_PsDistributionGeneralCurrent_Object = MibTableColumn
psDistributionGeneralCurrent = _PsDistributionGeneralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3, 1, 2),
    _PsDistributionGeneralCurrent_Type()
)
psDistributionGeneralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDistributionGeneralCurrent.setStatus("current")
_PsDistributionGeneralName_Type = DisplayString
_PsDistributionGeneralName_Object = MibTableColumn
psDistributionGeneralName = _PsDistributionGeneralName_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 12, 3, 1, 3),
    _PsDistributionGeneralName_Type()
)
psDistributionGeneralName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDistributionGeneralName.setStatus("current")
_PsConverter_ObjectIdentity = ObjectIdentity
psConverter = _PsConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13)
)
_NumberOfInstalledConverters_Type = Integer32
_NumberOfInstalledConverters_Object = MibScalar
numberOfInstalledConverters = _NumberOfInstalledConverters_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 1),
    _NumberOfInstalledConverters_Type()
)
numberOfInstalledConverters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfInstalledConverters.setStatus("current")
_NumberOfConvertersCommunicating_Type = Integer32
_NumberOfConvertersCommunicating_Object = MibScalar
numberOfConvertersCommunicating = _NumberOfConvertersCommunicating_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 2),
    _NumberOfConvertersCommunicating_Type()
)
numberOfConvertersCommunicating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfConvertersCommunicating.setStatus("current")
_ConvertersUsedCapacity_Type = Integer32
_ConvertersUsedCapacity_Object = MibScalar
convertersUsedCapacity = _ConvertersUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 3),
    _ConvertersUsedCapacity_Type()
)
convertersUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convertersUsedCapacity.setStatus("current")
_PsConverterVoltage_Type = Integer32
_PsConverterVoltage_Object = MibScalar
psConverterVoltage = _PsConverterVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 4),
    _PsConverterVoltage_Type()
)
psConverterVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterVoltage.setStatus("current")
_PsTotalConverterCurrent_Type = Integer32
_PsTotalConverterCurrent_Object = MibScalar
psTotalConverterCurrent = _PsTotalConverterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 5),
    _PsTotalConverterCurrent_Type()
)
psTotalConverterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psTotalConverterCurrent.setStatus("current")
_PsConverterTable_Object = MibTable
psConverterTable = _PsConverterTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6)
)
if mibBuilder.loadTexts:
    psConverterTable.setStatus("current")
_PsConverterEntry_Object = MibTableRow
psConverterEntry = _PsConverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1)
)
psConverterEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psConverterIndex"),
)
if mibBuilder.loadTexts:
    psConverterEntry.setStatus("current")


class _PsConverterIndex_Type(Integer32):
    """Custom type psConverterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PsConverterIndex_Type.__name__ = "Integer32"
_PsConverterIndex_Object = MibTableColumn
psConverterIndex = _PsConverterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 1),
    _PsConverterIndex_Type()
)
psConverterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterIndex.setStatus("current")
_PsConverterProductNumber_Type = DisplayString
_PsConverterProductNumber_Object = MibTableColumn
psConverterProductNumber = _PsConverterProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 2),
    _PsConverterProductNumber_Type()
)
psConverterProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterProductNumber.setStatus("current")
_PsConverterHWVersion_Type = DisplayString
_PsConverterHWVersion_Object = MibTableColumn
psConverterHWVersion = _PsConverterHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 3),
    _PsConverterHWVersion_Type()
)
psConverterHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterHWVersion.setStatus("current")
_PsConverterSWVersion_Type = DisplayString
_PsConverterSWVersion_Object = MibTableColumn
psConverterSWVersion = _PsConverterSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 4),
    _PsConverterSWVersion_Type()
)
psConverterSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterSWVersion.setStatus("current")
_PsConverterSerialNumber_Type = DisplayString
_PsConverterSerialNumber_Object = MibTableColumn
psConverterSerialNumber = _PsConverterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 5),
    _PsConverterSerialNumber_Type()
)
psConverterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterSerialNumber.setStatus("current")
_PsConverterCurrent_Type = Integer32
_PsConverterCurrent_Object = MibTableColumn
psConverterCurrent = _PsConverterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 6),
    _PsConverterCurrent_Type()
)
psConverterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterCurrent.setStatus("current")
_PsConverterIdent_Type = DisplayString
_PsConverterIdent_Object = MibTableColumn
psConverterIdent = _PsConverterIdent_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 7),
    _PsConverterIdent_Type()
)
psConverterIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterIdent.setStatus("current")
_PsConverterFail_Type = StatusChange
_PsConverterFail_Object = MibTableColumn
psConverterFail = _PsConverterFail_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 13, 6, 1, 8),
    _PsConverterFail_Type()
)
psConverterFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psConverterFail.setStatus("current")
_PsControl_ObjectIdentity = ObjectIdentity
psControl = _PsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14)
)
_ControlBatteryTest_Type = Integer32
_ControlBatteryTest_Object = MibScalar
controlBatteryTest = _ControlBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 1),
    _ControlBatteryTest_Type()
)
controlBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlBatteryTest.setStatus("current")
_ControlRelay8_Type = Integer32
_ControlRelay8_Object = MibScalar
controlRelay8 = _ControlRelay8_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 2),
    _ControlRelay8_Type()
)
controlRelay8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRelay8.setStatus("current")
_ControlRelay7_Type = Integer32
_ControlRelay7_Object = MibScalar
controlRelay7 = _ControlRelay7_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 3),
    _ControlRelay7_Type()
)
controlRelay7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRelay7.setStatus("current")
_ControlRelay6_Type = Integer32
_ControlRelay6_Object = MibScalar
controlRelay6 = _ControlRelay6_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 4),
    _ControlRelay6_Type()
)
controlRelay6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRelay6.setStatus("current")
_ControlRelayTest_Type = Integer32
_ControlRelayTest_Object = MibScalar
controlRelayTest = _ControlRelayTest_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 14, 5),
    _ControlRelayTest_Type()
)
controlRelayTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlRelayTest.setStatus("current")
_PsEquipmentSignalTable_Object = MibTable
psEquipmentSignalTable = _PsEquipmentSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 15)
)
if mibBuilder.loadTexts:
    psEquipmentSignalTable.setStatus("current")
_EquipmentSignalTableEntry_Object = MibTableRow
equipmentSignalTableEntry = _EquipmentSignalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 15, 1)
)
equipmentSignalTableEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psEquipmentSignalTableEntryIndex"),
)
if mibBuilder.loadTexts:
    equipmentSignalTableEntry.setStatus("current")


class _PsEquipmentSignalTableEntryIndex_Type(Integer32):
    """Custom type psEquipmentSignalTableEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268386303),
    )


_PsEquipmentSignalTableEntryIndex_Type.__name__ = "Integer32"
_PsEquipmentSignalTableEntryIndex_Object = MibTableColumn
psEquipmentSignalTableEntryIndex = _PsEquipmentSignalTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 15, 1, 1),
    _PsEquipmentSignalTableEntryIndex_Type()
)
psEquipmentSignalTableEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEquipmentSignalTableEntryIndex.setStatus("current")
_PsEquipmentSignalValue_Type = Integer32
_PsEquipmentSignalValue_Object = MibTableColumn
psEquipmentSignalValue = _PsEquipmentSignalValue_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 15, 1, 2),
    _PsEquipmentSignalValue_Type()
)
psEquipmentSignalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEquipmentSignalValue.setStatus("current")
_PsSMDUHCurrent_ObjectIdentity = ObjectIdentity
psSMDUHCurrent = _PsSMDUHCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16)
)
_NumberOfInstalledSMDUH_Type = Integer32
_NumberOfInstalledSMDUH_Object = MibScalar
numberOfInstalledSMDUH = _NumberOfInstalledSMDUH_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 1),
    _NumberOfInstalledSMDUH_Type()
)
numberOfInstalledSMDUH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfInstalledSMDUH.setStatus("current")
_PsSMDUH1Voltage_Type = Integer32
_PsSMDUH1Voltage_Object = MibScalar
psSMDUH1Voltage = _PsSMDUH1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 2),
    _PsSMDUH1Voltage_Type()
)
psSMDUH1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUH1Voltage.setStatus("current")
_PsSMDUH2Voltage_Type = Integer32
_PsSMDUH2Voltage_Object = MibScalar
psSMDUH2Voltage = _PsSMDUH2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 3),
    _PsSMDUH2Voltage_Type()
)
psSMDUH2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUH2Voltage.setStatus("current")
_PsSMDUH3Voltage_Type = Integer32
_PsSMDUH3Voltage_Object = MibScalar
psSMDUH3Voltage = _PsSMDUH3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 4),
    _PsSMDUH3Voltage_Type()
)
psSMDUH3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUH3Voltage.setStatus("current")
_PsSMDUH4Voltage_Type = Integer32
_PsSMDUH4Voltage_Object = MibScalar
psSMDUH4Voltage = _PsSMDUH4Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 5),
    _PsSMDUH4Voltage_Type()
)
psSMDUH4Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUH4Voltage.setStatus("current")
_PsSMDUH5Voltage_Type = Integer32
_PsSMDUH5Voltage_Object = MibScalar
psSMDUH5Voltage = _PsSMDUH5Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 6),
    _PsSMDUH5Voltage_Type()
)
psSMDUH5Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUH5Voltage.setStatus("current")
_PsSMDUH6Voltage_Type = Integer32
_PsSMDUH6Voltage_Object = MibScalar
psSMDUH6Voltage = _PsSMDUH6Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 7),
    _PsSMDUH6Voltage_Type()
)
psSMDUH6Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUH6Voltage.setStatus("current")
_PsSMDUH7Voltage_Type = Integer32
_PsSMDUH7Voltage_Object = MibScalar
psSMDUH7Voltage = _PsSMDUH7Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 8),
    _PsSMDUH7Voltage_Type()
)
psSMDUH7Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUH7Voltage.setStatus("current")
_PsSMDUH8Voltage_Type = Integer32
_PsSMDUH8Voltage_Object = MibScalar
psSMDUH8Voltage = _PsSMDUH8Voltage_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 9),
    _PsSMDUH8Voltage_Type()
)
psSMDUH8Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUH8Voltage.setStatus("current")
_PsSMDUHCurrentTable_Object = MibTable
psSMDUHCurrentTable = _PsSMDUHCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10)
)
if mibBuilder.loadTexts:
    psSMDUHCurrentTable.setStatus("current")
_PsSMDUHCurrentEntry_Object = MibTableRow
psSMDUHCurrentEntry = _PsSMDUHCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1)
)
psSMDUHCurrentEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psSMDUHCurrentIndex"),
)
if mibBuilder.loadTexts:
    psSMDUHCurrentEntry.setStatus("current")


class _PsSMDUHCurrentIndex_Type(Integer32):
    """Custom type psSMDUHCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PsSMDUHCurrentIndex_Type.__name__ = "Integer32"
_PsSMDUHCurrentIndex_Object = MibTableColumn
psSMDUHCurrentIndex = _PsSMDUHCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 1),
    _PsSMDUHCurrentIndex_Type()
)
psSMDUHCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrentIndex.setStatus("current")
_PsSMDUHCurrent1_Type = Integer32
_PsSMDUHCurrent1_Object = MibTableColumn
psSMDUHCurrent1 = _PsSMDUHCurrent1_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 2),
    _PsSMDUHCurrent1_Type()
)
psSMDUHCurrent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent1.setStatus("current")
_PsSMDUHCurrent2_Type = Integer32
_PsSMDUHCurrent2_Object = MibTableColumn
psSMDUHCurrent2 = _PsSMDUHCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 3),
    _PsSMDUHCurrent2_Type()
)
psSMDUHCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent2.setStatus("current")
_PsSMDUHCurrent3_Type = Integer32
_PsSMDUHCurrent3_Object = MibTableColumn
psSMDUHCurrent3 = _PsSMDUHCurrent3_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 4),
    _PsSMDUHCurrent3_Type()
)
psSMDUHCurrent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent3.setStatus("current")
_PsSMDUHCurrent4_Type = Integer32
_PsSMDUHCurrent4_Object = MibTableColumn
psSMDUHCurrent4 = _PsSMDUHCurrent4_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 5),
    _PsSMDUHCurrent4_Type()
)
psSMDUHCurrent4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent4.setStatus("current")
_PsSMDUHCurrent5_Type = Integer32
_PsSMDUHCurrent5_Object = MibTableColumn
psSMDUHCurrent5 = _PsSMDUHCurrent5_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 6),
    _PsSMDUHCurrent5_Type()
)
psSMDUHCurrent5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent5.setStatus("current")
_PsSMDUHCurrent6_Type = Integer32
_PsSMDUHCurrent6_Object = MibTableColumn
psSMDUHCurrent6 = _PsSMDUHCurrent6_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 7),
    _PsSMDUHCurrent6_Type()
)
psSMDUHCurrent6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent6.setStatus("current")
_PsSMDUHCurrent7_Type = Integer32
_PsSMDUHCurrent7_Object = MibTableColumn
psSMDUHCurrent7 = _PsSMDUHCurrent7_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 8),
    _PsSMDUHCurrent7_Type()
)
psSMDUHCurrent7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent7.setStatus("current")
_PsSMDUHCurrent8_Type = Integer32
_PsSMDUHCurrent8_Object = MibTableColumn
psSMDUHCurrent8 = _PsSMDUHCurrent8_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 9),
    _PsSMDUHCurrent8_Type()
)
psSMDUHCurrent8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent8.setStatus("current")
_PsSMDUHCurrent9_Type = Integer32
_PsSMDUHCurrent9_Object = MibTableColumn
psSMDUHCurrent9 = _PsSMDUHCurrent9_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 10),
    _PsSMDUHCurrent9_Type()
)
psSMDUHCurrent9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent9.setStatus("current")
_PsSMDUHCurrent10_Type = Integer32
_PsSMDUHCurrent10_Object = MibTableColumn
psSMDUHCurrent10 = _PsSMDUHCurrent10_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 11),
    _PsSMDUHCurrent10_Type()
)
psSMDUHCurrent10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent10.setStatus("current")
_PsSMDUHCurrent11_Type = Integer32
_PsSMDUHCurrent11_Object = MibTableColumn
psSMDUHCurrent11 = _PsSMDUHCurrent11_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 12),
    _PsSMDUHCurrent11_Type()
)
psSMDUHCurrent11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent11.setStatus("current")
_PsSMDUHCurrent12_Type = Integer32
_PsSMDUHCurrent12_Object = MibTableColumn
psSMDUHCurrent12 = _PsSMDUHCurrent12_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 13),
    _PsSMDUHCurrent12_Type()
)
psSMDUHCurrent12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent12.setStatus("current")
_PsSMDUHCurrent13_Type = Integer32
_PsSMDUHCurrent13_Object = MibTableColumn
psSMDUHCurrent13 = _PsSMDUHCurrent13_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 14),
    _PsSMDUHCurrent13_Type()
)
psSMDUHCurrent13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent13.setStatus("current")
_PsSMDUHCurrent14_Type = Integer32
_PsSMDUHCurrent14_Object = MibTableColumn
psSMDUHCurrent14 = _PsSMDUHCurrent14_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 15),
    _PsSMDUHCurrent14_Type()
)
psSMDUHCurrent14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent14.setStatus("current")
_PsSMDUHCurrent15_Type = Integer32
_PsSMDUHCurrent15_Object = MibTableColumn
psSMDUHCurrent15 = _PsSMDUHCurrent15_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 16),
    _PsSMDUHCurrent15_Type()
)
psSMDUHCurrent15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent15.setStatus("current")
_PsSMDUHCurrent16_Type = Integer32
_PsSMDUHCurrent16_Object = MibTableColumn
psSMDUHCurrent16 = _PsSMDUHCurrent16_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 17),
    _PsSMDUHCurrent16_Type()
)
psSMDUHCurrent16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent16.setStatus("current")
_PsSMDUHCurrent17_Type = Integer32
_PsSMDUHCurrent17_Object = MibTableColumn
psSMDUHCurrent17 = _PsSMDUHCurrent17_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 18),
    _PsSMDUHCurrent17_Type()
)
psSMDUHCurrent17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent17.setStatus("current")
_PsSMDUHCurrent18_Type = Integer32
_PsSMDUHCurrent18_Object = MibTableColumn
psSMDUHCurrent18 = _PsSMDUHCurrent18_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 19),
    _PsSMDUHCurrent18_Type()
)
psSMDUHCurrent18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent18.setStatus("current")
_PsSMDUHCurrent19_Type = Integer32
_PsSMDUHCurrent19_Object = MibTableColumn
psSMDUHCurrent19 = _PsSMDUHCurrent19_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 20),
    _PsSMDUHCurrent19_Type()
)
psSMDUHCurrent19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent19.setStatus("current")
_PsSMDUHCurrent20_Type = Integer32
_PsSMDUHCurrent20_Object = MibTableColumn
psSMDUHCurrent20 = _PsSMDUHCurrent20_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 16, 10, 1, 21),
    _PsSMDUHCurrent20_Type()
)
psSMDUHCurrent20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHCurrent20.setStatus("current")
_PsSMDUHPower_ObjectIdentity = ObjectIdentity
psSMDUHPower = _PsSMDUHPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17)
)
_PsSMDUHPowerTable_Object = MibTable
psSMDUHPowerTable = _PsSMDUHPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    psSMDUHPowerTable.setStatus("current")
_PsSMDUHPowerEntry_Object = MibTableRow
psSMDUHPowerEntry = _PsSMDUHPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1)
)
psSMDUHPowerEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psSMDUHPowerIndex"),
)
if mibBuilder.loadTexts:
    psSMDUHPowerEntry.setStatus("current")


class _PsSMDUHPowerIndex_Type(Integer32):
    """Custom type psSMDUHPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PsSMDUHPowerIndex_Type.__name__ = "Integer32"
_PsSMDUHPowerIndex_Object = MibTableColumn
psSMDUHPowerIndex = _PsSMDUHPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 1),
    _PsSMDUHPowerIndex_Type()
)
psSMDUHPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPowerIndex.setStatus("current")
_PsSMDUHPower1_Type = Integer32
_PsSMDUHPower1_Object = MibTableColumn
psSMDUHPower1 = _PsSMDUHPower1_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 2),
    _PsSMDUHPower1_Type()
)
psSMDUHPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower1.setStatus("current")
_PsSMDUHPower2_Type = Integer32
_PsSMDUHPower2_Object = MibTableColumn
psSMDUHPower2 = _PsSMDUHPower2_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 3),
    _PsSMDUHPower2_Type()
)
psSMDUHPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower2.setStatus("current")
_PsSMDUHPower3_Type = Integer32
_PsSMDUHPower3_Object = MibTableColumn
psSMDUHPower3 = _PsSMDUHPower3_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 4),
    _PsSMDUHPower3_Type()
)
psSMDUHPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower3.setStatus("current")
_PsSMDUHPower4_Type = Integer32
_PsSMDUHPower4_Object = MibTableColumn
psSMDUHPower4 = _PsSMDUHPower4_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 5),
    _PsSMDUHPower4_Type()
)
psSMDUHPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower4.setStatus("current")
_PsSMDUHPower5_Type = Integer32
_PsSMDUHPower5_Object = MibTableColumn
psSMDUHPower5 = _PsSMDUHPower5_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 6),
    _PsSMDUHPower5_Type()
)
psSMDUHPower5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower5.setStatus("current")
_PsSMDUHPower6_Type = Integer32
_PsSMDUHPower6_Object = MibTableColumn
psSMDUHPower6 = _PsSMDUHPower6_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 7),
    _PsSMDUHPower6_Type()
)
psSMDUHPower6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower6.setStatus("current")
_PsSMDUHPower7_Type = Integer32
_PsSMDUHPower7_Object = MibTableColumn
psSMDUHPower7 = _PsSMDUHPower7_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 8),
    _PsSMDUHPower7_Type()
)
psSMDUHPower7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower7.setStatus("current")
_PsSMDUHPower8_Type = Integer32
_PsSMDUHPower8_Object = MibTableColumn
psSMDUHPower8 = _PsSMDUHPower8_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 9),
    _PsSMDUHPower8_Type()
)
psSMDUHPower8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower8.setStatus("current")
_PsSMDUHPower9_Type = Integer32
_PsSMDUHPower9_Object = MibTableColumn
psSMDUHPower9 = _PsSMDUHPower9_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 10),
    _PsSMDUHPower9_Type()
)
psSMDUHPower9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower9.setStatus("current")
_PsSMDUHPower10_Type = Integer32
_PsSMDUHPower10_Object = MibTableColumn
psSMDUHPower10 = _PsSMDUHPower10_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 11),
    _PsSMDUHPower10_Type()
)
psSMDUHPower10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower10.setStatus("current")
_PsSMDUHPower11_Type = Integer32
_PsSMDUHPower11_Object = MibTableColumn
psSMDUHPower11 = _PsSMDUHPower11_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 12),
    _PsSMDUHPower11_Type()
)
psSMDUHPower11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower11.setStatus("current")
_PsSMDUHPower12_Type = Integer32
_PsSMDUHPower12_Object = MibTableColumn
psSMDUHPower12 = _PsSMDUHPower12_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 13),
    _PsSMDUHPower12_Type()
)
psSMDUHPower12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower12.setStatus("current")
_PsSMDUHPower13_Type = Integer32
_PsSMDUHPower13_Object = MibTableColumn
psSMDUHPower13 = _PsSMDUHPower13_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 14),
    _PsSMDUHPower13_Type()
)
psSMDUHPower13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower13.setStatus("current")
_PsSMDUHPower14_Type = Integer32
_PsSMDUHPower14_Object = MibTableColumn
psSMDUHPower14 = _PsSMDUHPower14_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 15),
    _PsSMDUHPower14_Type()
)
psSMDUHPower14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower14.setStatus("current")
_PsSMDUHPower15_Type = Integer32
_PsSMDUHPower15_Object = MibTableColumn
psSMDUHPower15 = _PsSMDUHPower15_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 16),
    _PsSMDUHPower15_Type()
)
psSMDUHPower15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower15.setStatus("current")
_PsSMDUHPower16_Type = Integer32
_PsSMDUHPower16_Object = MibTableColumn
psSMDUHPower16 = _PsSMDUHPower16_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 17),
    _PsSMDUHPower16_Type()
)
psSMDUHPower16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower16.setStatus("current")
_PsSMDUHPower17_Type = Integer32
_PsSMDUHPower17_Object = MibTableColumn
psSMDUHPower17 = _PsSMDUHPower17_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 18),
    _PsSMDUHPower17_Type()
)
psSMDUHPower17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower17.setStatus("current")
_PsSMDUHPower18_Type = Integer32
_PsSMDUHPower18_Object = MibTableColumn
psSMDUHPower18 = _PsSMDUHPower18_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 19),
    _PsSMDUHPower18_Type()
)
psSMDUHPower18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower18.setStatus("current")
_PsSMDUHPower19_Type = Integer32
_PsSMDUHPower19_Object = MibTableColumn
psSMDUHPower19 = _PsSMDUHPower19_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 20),
    _PsSMDUHPower19_Type()
)
psSMDUHPower19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower19.setStatus("current")
_PsSMDUHPower20_Type = Integer32
_PsSMDUHPower20_Object = MibTableColumn
psSMDUHPower20 = _PsSMDUHPower20_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 17, 1, 1, 21),
    _PsSMDUHPower20_Type()
)
psSMDUHPower20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHPower20.setStatus("current")
_PsSMDUHEnergy_ObjectIdentity = ObjectIdentity
psSMDUHEnergy = _PsSMDUHEnergy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18)
)
_PsSMDUHEnergyTable_Object = MibTable
psSMDUHEnergyTable = _PsSMDUHEnergyTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    psSMDUHEnergyTable.setStatus("current")
_PsSMDUHEnergyEntry_Object = MibTableRow
psSMDUHEnergyEntry = _PsSMDUHEnergyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1)
)
psSMDUHEnergyEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "psSMDUHEnergyIndex"),
)
if mibBuilder.loadTexts:
    psSMDUHEnergyEntry.setStatus("current")


class _PsSMDUHEnergyIndex_Type(Integer32):
    """Custom type psSMDUHEnergyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PsSMDUHEnergyIndex_Type.__name__ = "Integer32"
_PsSMDUHEnergyIndex_Object = MibTableColumn
psSMDUHEnergyIndex = _PsSMDUHEnergyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 1),
    _PsSMDUHEnergyIndex_Type()
)
psSMDUHEnergyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHEnergyIndex.setStatus("current")
_PsSMDUHTotalEnergy1_Type = Integer32
_PsSMDUHTotalEnergy1_Object = MibTableColumn
psSMDUHTotalEnergy1 = _PsSMDUHTotalEnergy1_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 2),
    _PsSMDUHTotalEnergy1_Type()
)
psSMDUHTotalEnergy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy1.setStatus("current")
_PsSMDUHTotalEnergy2_Type = Integer32
_PsSMDUHTotalEnergy2_Object = MibTableColumn
psSMDUHTotalEnergy2 = _PsSMDUHTotalEnergy2_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 3),
    _PsSMDUHTotalEnergy2_Type()
)
psSMDUHTotalEnergy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy2.setStatus("current")
_PsSMDUHTotalEnergy3_Type = Integer32
_PsSMDUHTotalEnergy3_Object = MibTableColumn
psSMDUHTotalEnergy3 = _PsSMDUHTotalEnergy3_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 4),
    _PsSMDUHTotalEnergy3_Type()
)
psSMDUHTotalEnergy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy3.setStatus("current")
_PsSMDUHTotalEnergy4_Type = Integer32
_PsSMDUHTotalEnergy4_Object = MibTableColumn
psSMDUHTotalEnergy4 = _PsSMDUHTotalEnergy4_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 5),
    _PsSMDUHTotalEnergy4_Type()
)
psSMDUHTotalEnergy4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy4.setStatus("current")
_PsSMDUHTotalEnergy5_Type = Integer32
_PsSMDUHTotalEnergy5_Object = MibTableColumn
psSMDUHTotalEnergy5 = _PsSMDUHTotalEnergy5_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 6),
    _PsSMDUHTotalEnergy5_Type()
)
psSMDUHTotalEnergy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy5.setStatus("current")
_PsSMDUHTotalEnergy6_Type = Integer32
_PsSMDUHTotalEnergy6_Object = MibTableColumn
psSMDUHTotalEnergy6 = _PsSMDUHTotalEnergy6_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 7),
    _PsSMDUHTotalEnergy6_Type()
)
psSMDUHTotalEnergy6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy6.setStatus("current")
_PsSMDUHTotalEnergy7_Type = Integer32
_PsSMDUHTotalEnergy7_Object = MibTableColumn
psSMDUHTotalEnergy7 = _PsSMDUHTotalEnergy7_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 8),
    _PsSMDUHTotalEnergy7_Type()
)
psSMDUHTotalEnergy7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy7.setStatus("current")
_PsSMDUHTotalEnergy8_Type = Integer32
_PsSMDUHTotalEnergy8_Object = MibTableColumn
psSMDUHTotalEnergy8 = _PsSMDUHTotalEnergy8_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 9),
    _PsSMDUHTotalEnergy8_Type()
)
psSMDUHTotalEnergy8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy8.setStatus("current")
_PsSMDUHTotalEnergy9_Type = Integer32
_PsSMDUHTotalEnergy9_Object = MibTableColumn
psSMDUHTotalEnergy9 = _PsSMDUHTotalEnergy9_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 10),
    _PsSMDUHTotalEnergy9_Type()
)
psSMDUHTotalEnergy9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy9.setStatus("current")
_PsSMDUHTotalEnergy10_Type = Integer32
_PsSMDUHTotalEnergy10_Object = MibTableColumn
psSMDUHTotalEnergy10 = _PsSMDUHTotalEnergy10_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 11),
    _PsSMDUHTotalEnergy10_Type()
)
psSMDUHTotalEnergy10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy10.setStatus("current")
_PsSMDUHTotalEnergy11_Type = Integer32
_PsSMDUHTotalEnergy11_Object = MibTableColumn
psSMDUHTotalEnergy11 = _PsSMDUHTotalEnergy11_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 12),
    _PsSMDUHTotalEnergy11_Type()
)
psSMDUHTotalEnergy11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy11.setStatus("current")
_PsSMDUHTotalEnergy12_Type = Integer32
_PsSMDUHTotalEnergy12_Object = MibTableColumn
psSMDUHTotalEnergy12 = _PsSMDUHTotalEnergy12_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 13),
    _PsSMDUHTotalEnergy12_Type()
)
psSMDUHTotalEnergy12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy12.setStatus("current")
_PsSMDUHTotalEnergy13_Type = Integer32
_PsSMDUHTotalEnergy13_Object = MibTableColumn
psSMDUHTotalEnergy13 = _PsSMDUHTotalEnergy13_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 14),
    _PsSMDUHTotalEnergy13_Type()
)
psSMDUHTotalEnergy13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy13.setStatus("current")
_PsSMDUHTotalEnergy14_Type = Integer32
_PsSMDUHTotalEnergy14_Object = MibTableColumn
psSMDUHTotalEnergy14 = _PsSMDUHTotalEnergy14_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 15),
    _PsSMDUHTotalEnergy14_Type()
)
psSMDUHTotalEnergy14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy14.setStatus("current")
_PsSMDUHTotalEnergy15_Type = Integer32
_PsSMDUHTotalEnergy15_Object = MibTableColumn
psSMDUHTotalEnergy15 = _PsSMDUHTotalEnergy15_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 16),
    _PsSMDUHTotalEnergy15_Type()
)
psSMDUHTotalEnergy15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy15.setStatus("current")
_PsSMDUHTotalEnergy16_Type = Integer32
_PsSMDUHTotalEnergy16_Object = MibTableColumn
psSMDUHTotalEnergy16 = _PsSMDUHTotalEnergy16_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 17),
    _PsSMDUHTotalEnergy16_Type()
)
psSMDUHTotalEnergy16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy16.setStatus("current")
_PsSMDUHTotalEnergy17_Type = Integer32
_PsSMDUHTotalEnergy17_Object = MibTableColumn
psSMDUHTotalEnergy17 = _PsSMDUHTotalEnergy17_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 18),
    _PsSMDUHTotalEnergy17_Type()
)
psSMDUHTotalEnergy17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy17.setStatus("current")
_PsSMDUHTotalEnergy18_Type = Integer32
_PsSMDUHTotalEnergy18_Object = MibTableColumn
psSMDUHTotalEnergy18 = _PsSMDUHTotalEnergy18_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 19),
    _PsSMDUHTotalEnergy18_Type()
)
psSMDUHTotalEnergy18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy18.setStatus("current")
_PsSMDUHTotalEnergy19_Type = Integer32
_PsSMDUHTotalEnergy19_Object = MibTableColumn
psSMDUHTotalEnergy19 = _PsSMDUHTotalEnergy19_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 20),
    _PsSMDUHTotalEnergy19_Type()
)
psSMDUHTotalEnergy19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy19.setStatus("current")
_PsSMDUHTotalEnergy20_Type = Integer32
_PsSMDUHTotalEnergy20_Object = MibTableColumn
psSMDUHTotalEnergy20 = _PsSMDUHTotalEnergy20_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 2, 18, 1, 1, 21),
    _PsSMDUHTotalEnergy20_Type()
)
psSMDUHTotalEnergy20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSMDUHTotalEnergy20.setStatus("current")
_AlarmLastTrapNo_Type = Counter32
_AlarmLastTrapNo_Object = MibScalar
alarmLastTrapNo = _AlarmLastTrapNo_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 3),
    _AlarmLastTrapNo_Type()
)
alarmLastTrapNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLastTrapNo.setStatus("current")
_AlarmActiveAlarmTable_Object = MibTable
alarmActiveAlarmTable = _AlarmActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alarmActiveAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "NETSURE-MIB-004-A", "alarmIndex"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")
_AlarmIndex_Type = Counter32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmTime_Type = DateAndTime
_AlarmTime_Object = MibTableColumn
alarmTime = _AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 2),
    _AlarmTime_Type()
)
alarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTime.setStatus("current")
_AlarmStatusChange_Type = StatusChange
_AlarmStatusChange_Object = MibTableColumn
alarmStatusChange = _AlarmStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 3),
    _AlarmStatusChange_Type()
)
alarmStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusChange.setStatus("current")
_AlarmSeverity_Type = Status
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 4),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmDescription_Type = DisplayString
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 5),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_AlarmType_Type = Integer32
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 4, 1, 6),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_PowerEvents_ObjectIdentity = ObjectIdentity
powerEvents = _PowerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5)
)

# Managed Objects groups


# Notification objects

alarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5, 1)
)
alarmTrap.setObjects(
      *(("NETSURE-MIB-004-A", "alarmIndex"),
        ("NETSURE-MIB-004-A", "alarmTime"),
        ("NETSURE-MIB-004-A", "alarmStatusChange"),
        ("NETSURE-MIB-004-A", "alarmSeverity"),
        ("NETSURE-MIB-004-A", "alarmDescription"),
        ("NETSURE-MIB-004-A", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmTrap.setStatus(
        "current"
    )

alarmActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5, 2)
)
alarmActiveTrap.setObjects(
      *(("NETSURE-MIB-004-A", "alarmTime"),
        ("NETSURE-MIB-004-A", "alarmSeverity"),
        ("NETSURE-MIB-004-A", "alarmDescription"),
        ("NETSURE-MIB-004-A", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmActiveTrap.setStatus(
        "current"
    )

alarmCeaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6302, 2, 1, 5, 3)
)
alarmCeaseTrap.setObjects(
      *(("NETSURE-MIB-004-A", "alarmTime"),
        ("NETSURE-MIB-004-A", "alarmSeverity"),
        ("NETSURE-MIB-004-A", "alarmDescription"),
        ("NETSURE-MIB-004-A", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmCeaseTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSURE-MIB-004-A",
    **{"Status": Status,
       "StatusChange": StatusChange,
       "ees": ees,
       "global": _pysmi_global,
       "powerMIB": powerMIB,
       "ident": ident,
       "identManufacturer": identManufacturer,
       "identModel": identModel,
       "identControllerFirmwareVersion": identControllerFirmwareVersion,
       "identName": identName,
       "identSNMPCfgVer": identSNMPCfgVer,
       "system": system,
       "systemStatus": systemStatus,
       "systemVoltage": systemVoltage,
       "systemCurrent": systemCurrent,
       "systemUsedCapacity": systemUsedCapacity,
       "psBattery": psBattery,
       "psBatteryVoltage": psBatteryVoltage,
       "psTotalBatteryCurrent": psTotalBatteryCurrent,
       "psBatteryCapacity": psBatteryCapacity,
       "psBatteryNominalCapacity": psBatteryNominalCapacity,
       "psBatteryTable": psBatteryTable,
       "psBatteryEntry": psBatteryEntry,
       "psBatteryIndex": psBatteryIndex,
       "psBatteryCurrent": psBatteryCurrent,
       "psBatteryName": psBatteryName,
       "psInput": psInput,
       "psInputLineAVoltage": psInputLineAVoltage,
       "psInputLineBVoltage": psInputLineBVoltage,
       "psInputLineCVoltage": psInputLineCVoltage,
       "psTemperature": psTemperature,
       "psTemperature1": psTemperature1,
       "psTemperature2": psTemperature2,
       "psTemperatureTable": psTemperatureTable,
       "psTemperatureEntry": psTemperatureEntry,
       "psTemperatureIndex": psTemperatureIndex,
       "psTemperatureMeasurement": psTemperatureMeasurement,
       "psTemperatureName": psTemperatureName,
       "psTemperatureType": psTemperatureType,
       "psTemperatureAlarmStatus": psTemperatureAlarmStatus,
       "psStatusCommunication": psStatusCommunication,
       "psStatusBatteryMode": psStatusBatteryMode,
       "psSMNumber": psSMNumber,
       "psSMACNumber": psSMACNumber,
       "psSMBATNumber": psSMBATNumber,
       "psSMIONumber": psSMIONumber,
       "psRectifier": psRectifier,
       "numberOfInstalledRectifiers": numberOfInstalledRectifiers,
       "numberOfRectifiersCommunicating": numberOfRectifiersCommunicating,
       "rectifiersUsedCapacity": rectifiersUsedCapacity,
       "psRectifierTable": psRectifierTable,
       "psRectifierEntry": psRectifierEntry,
       "psRectifierIndex": psRectifierIndex,
       "psRectifierProductNumber": psRectifierProductNumber,
       "psRectifierHWVersion": psRectifierHWVersion,
       "psRectifierSWVersion": psRectifierSWVersion,
       "psRectifierSerialNumber": psRectifierSerialNumber,
       "psRectifierCurrent": psRectifierCurrent,
       "psRectifierIdent": psRectifierIdent,
       "psRectifierFail": psRectifierFail,
       "psDistribution": psDistribution,
       "psTotalLoadCurrent": psTotalLoadCurrent,
       "psDistributionLoadTable": psDistributionLoadTable,
       "psDistributionLoadEntry": psDistributionLoadEntry,
       "psDistributionLoadIndex": psDistributionLoadIndex,
       "psDistributionLoadCurrent": psDistributionLoadCurrent,
       "psDistributionLoadName": psDistributionLoadName,
       "psDistributionGeneralTable": psDistributionGeneralTable,
       "psDistributionGeneralEntry": psDistributionGeneralEntry,
       "psDistributionGeneralIndex": psDistributionGeneralIndex,
       "psDistributionGeneralCurrent": psDistributionGeneralCurrent,
       "psDistributionGeneralName": psDistributionGeneralName,
       "psConverter": psConverter,
       "numberOfInstalledConverters": numberOfInstalledConverters,
       "numberOfConvertersCommunicating": numberOfConvertersCommunicating,
       "convertersUsedCapacity": convertersUsedCapacity,
       "psConverterVoltage": psConverterVoltage,
       "psTotalConverterCurrent": psTotalConverterCurrent,
       "psConverterTable": psConverterTable,
       "psConverterEntry": psConverterEntry,
       "psConverterIndex": psConverterIndex,
       "psConverterProductNumber": psConverterProductNumber,
       "psConverterHWVersion": psConverterHWVersion,
       "psConverterSWVersion": psConverterSWVersion,
       "psConverterSerialNumber": psConverterSerialNumber,
       "psConverterCurrent": psConverterCurrent,
       "psConverterIdent": psConverterIdent,
       "psConverterFail": psConverterFail,
       "psControl": psControl,
       "controlBatteryTest": controlBatteryTest,
       "controlRelay8": controlRelay8,
       "controlRelay7": controlRelay7,
       "controlRelay6": controlRelay6,
       "controlRelayTest": controlRelayTest,
       "psEquipmentSignalTable": psEquipmentSignalTable,
       "equipmentSignalTableEntry": equipmentSignalTableEntry,
       "psEquipmentSignalTableEntryIndex": psEquipmentSignalTableEntryIndex,
       "psEquipmentSignalValue": psEquipmentSignalValue,
       "psSMDUHCurrent": psSMDUHCurrent,
       "numberOfInstalledSMDUH": numberOfInstalledSMDUH,
       "psSMDUH1Voltage": psSMDUH1Voltage,
       "psSMDUH2Voltage": psSMDUH2Voltage,
       "psSMDUH3Voltage": psSMDUH3Voltage,
       "psSMDUH4Voltage": psSMDUH4Voltage,
       "psSMDUH5Voltage": psSMDUH5Voltage,
       "psSMDUH6Voltage": psSMDUH6Voltage,
       "psSMDUH7Voltage": psSMDUH7Voltage,
       "psSMDUH8Voltage": psSMDUH8Voltage,
       "psSMDUHCurrentTable": psSMDUHCurrentTable,
       "psSMDUHCurrentEntry": psSMDUHCurrentEntry,
       "psSMDUHCurrentIndex": psSMDUHCurrentIndex,
       "psSMDUHCurrent1": psSMDUHCurrent1,
       "psSMDUHCurrent2": psSMDUHCurrent2,
       "psSMDUHCurrent3": psSMDUHCurrent3,
       "psSMDUHCurrent4": psSMDUHCurrent4,
       "psSMDUHCurrent5": psSMDUHCurrent5,
       "psSMDUHCurrent6": psSMDUHCurrent6,
       "psSMDUHCurrent7": psSMDUHCurrent7,
       "psSMDUHCurrent8": psSMDUHCurrent8,
       "psSMDUHCurrent9": psSMDUHCurrent9,
       "psSMDUHCurrent10": psSMDUHCurrent10,
       "psSMDUHCurrent11": psSMDUHCurrent11,
       "psSMDUHCurrent12": psSMDUHCurrent12,
       "psSMDUHCurrent13": psSMDUHCurrent13,
       "psSMDUHCurrent14": psSMDUHCurrent14,
       "psSMDUHCurrent15": psSMDUHCurrent15,
       "psSMDUHCurrent16": psSMDUHCurrent16,
       "psSMDUHCurrent17": psSMDUHCurrent17,
       "psSMDUHCurrent18": psSMDUHCurrent18,
       "psSMDUHCurrent19": psSMDUHCurrent19,
       "psSMDUHCurrent20": psSMDUHCurrent20,
       "psSMDUHPower": psSMDUHPower,
       "psSMDUHPowerTable": psSMDUHPowerTable,
       "psSMDUHPowerEntry": psSMDUHPowerEntry,
       "psSMDUHPowerIndex": psSMDUHPowerIndex,
       "psSMDUHPower1": psSMDUHPower1,
       "psSMDUHPower2": psSMDUHPower2,
       "psSMDUHPower3": psSMDUHPower3,
       "psSMDUHPower4": psSMDUHPower4,
       "psSMDUHPower5": psSMDUHPower5,
       "psSMDUHPower6": psSMDUHPower6,
       "psSMDUHPower7": psSMDUHPower7,
       "psSMDUHPower8": psSMDUHPower8,
       "psSMDUHPower9": psSMDUHPower9,
       "psSMDUHPower10": psSMDUHPower10,
       "psSMDUHPower11": psSMDUHPower11,
       "psSMDUHPower12": psSMDUHPower12,
       "psSMDUHPower13": psSMDUHPower13,
       "psSMDUHPower14": psSMDUHPower14,
       "psSMDUHPower15": psSMDUHPower15,
       "psSMDUHPower16": psSMDUHPower16,
       "psSMDUHPower17": psSMDUHPower17,
       "psSMDUHPower18": psSMDUHPower18,
       "psSMDUHPower19": psSMDUHPower19,
       "psSMDUHPower20": psSMDUHPower20,
       "psSMDUHEnergy": psSMDUHEnergy,
       "psSMDUHEnergyTable": psSMDUHEnergyTable,
       "psSMDUHEnergyEntry": psSMDUHEnergyEntry,
       "psSMDUHEnergyIndex": psSMDUHEnergyIndex,
       "psSMDUHTotalEnergy1": psSMDUHTotalEnergy1,
       "psSMDUHTotalEnergy2": psSMDUHTotalEnergy2,
       "psSMDUHTotalEnergy3": psSMDUHTotalEnergy3,
       "psSMDUHTotalEnergy4": psSMDUHTotalEnergy4,
       "psSMDUHTotalEnergy5": psSMDUHTotalEnergy5,
       "psSMDUHTotalEnergy6": psSMDUHTotalEnergy6,
       "psSMDUHTotalEnergy7": psSMDUHTotalEnergy7,
       "psSMDUHTotalEnergy8": psSMDUHTotalEnergy8,
       "psSMDUHTotalEnergy9": psSMDUHTotalEnergy9,
       "psSMDUHTotalEnergy10": psSMDUHTotalEnergy10,
       "psSMDUHTotalEnergy11": psSMDUHTotalEnergy11,
       "psSMDUHTotalEnergy12": psSMDUHTotalEnergy12,
       "psSMDUHTotalEnergy13": psSMDUHTotalEnergy13,
       "psSMDUHTotalEnergy14": psSMDUHTotalEnergy14,
       "psSMDUHTotalEnergy15": psSMDUHTotalEnergy15,
       "psSMDUHTotalEnergy16": psSMDUHTotalEnergy16,
       "psSMDUHTotalEnergy17": psSMDUHTotalEnergy17,
       "psSMDUHTotalEnergy18": psSMDUHTotalEnergy18,
       "psSMDUHTotalEnergy19": psSMDUHTotalEnergy19,
       "psSMDUHTotalEnergy20": psSMDUHTotalEnergy20,
       "alarmLastTrapNo": alarmLastTrapNo,
       "alarmActiveAlarmTable": alarmActiveAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "alarmIndex": alarmIndex,
       "alarmTime": alarmTime,
       "alarmStatusChange": alarmStatusChange,
       "alarmSeverity": alarmSeverity,
       "alarmDescription": alarmDescription,
       "alarmType": alarmType,
       "powerEvents": powerEvents,
       "alarmTrap": alarmTrap,
       "alarmActiveTrap": alarmActiveTrap,
       "alarmCeaseTrap": alarmCeaseTrap}
)
