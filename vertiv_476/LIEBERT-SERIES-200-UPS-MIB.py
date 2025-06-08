# SNMP MIB module (LIEBERT-SERIES-200-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_476/LIEBERT-SERIES-200-UPS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:21:43 2025
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

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

_Emerson_ObjectIdentity = ObjectIdentity
emerson = _Emerson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476)
)
_LiebertCorp_ObjectIdentity = ObjectIdentity
liebertCorp = _LiebertCorp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1)
)
_LiebertUps_ObjectIdentity = ObjectIdentity
liebertUps = _LiebertUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1)
)
_LuExtensions_ObjectIdentity = ObjectIdentity
luExtensions = _LuExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1)
)
_LuCore_ObjectIdentity = ObjectIdentity
luCore = _LuCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1)
)
_LcUpsIdent_ObjectIdentity = ObjectIdentity
lcUpsIdent = _LcUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1)
)


class _LcUpsIdentManufacturer_Type(DisplayString):
    """Custom type lcUpsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LcUpsIdentManufacturer_Type.__name__ = "DisplayString"
_LcUpsIdentManufacturer_Object = MibScalar
lcUpsIdentManufacturer = _LcUpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 1),
    _LcUpsIdentManufacturer_Type()
)
lcUpsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentManufacturer.setStatus("optional")


class _LcUpsIdentModel_Type(DisplayString):
    """Custom type lcUpsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LcUpsIdentModel_Type.__name__ = "DisplayString"
_LcUpsIdentModel_Object = MibScalar
lcUpsIdentModel = _LcUpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 2),
    _LcUpsIdentModel_Type()
)
lcUpsIdentModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsIdentModel.setStatus("optional")


class _LcUpsIdentSoftwareVersion_Type(DisplayString):
    """Custom type lcUpsIdentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LcUpsIdentSoftwareVersion_Type.__name__ = "DisplayString"
_LcUpsIdentSoftwareVersion_Object = MibScalar
lcUpsIdentSoftwareVersion = _LcUpsIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 3),
    _LcUpsIdentSoftwareVersion_Type()
)
lcUpsIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentSoftwareVersion.setStatus("optional")
_LcUpsIdentSpecific_Type = ObjectIdentifier
_LcUpsIdentSpecific_Object = MibScalar
lcUpsIdentSpecific = _LcUpsIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 4),
    _LcUpsIdentSpecific_Type()
)
lcUpsIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentSpecific.setStatus("optional")
_LcUpsBattery_ObjectIdentity = ObjectIdentity
lcUpsBattery = _LcUpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2)
)


class _LcUpsBatTimeRemaining_Type(Integer32):
    """Custom type lcUpsBatTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcUpsBatTimeRemaining_Type.__name__ = "Integer32"
_LcUpsBatTimeRemaining_Object = MibScalar
lcUpsBatTimeRemaining = _LcUpsBatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 1),
    _LcUpsBatTimeRemaining_Type()
)
lcUpsBatTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatTimeRemaining.setStatus("optional")


class _LcUpsBatVoltage_Type(Integer32):
    """Custom type lcUpsBatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsBatVoltage_Type.__name__ = "Integer32"
_LcUpsBatVoltage_Object = MibScalar
lcUpsBatVoltage = _LcUpsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 3),
    _LcUpsBatVoltage_Type()
)
lcUpsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatVoltage.setStatus("optional")


class _LcUpsBatCapacity_Type(Integer32):
    """Custom type lcUpsBatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LcUpsBatCapacity_Type.__name__ = "Integer32"
_LcUpsBatCapacity_Object = MibScalar
lcUpsBatCapacity = _LcUpsBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 6),
    _LcUpsBatCapacity_Type()
)
lcUpsBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatCapacity.setStatus("optional")
_LcUpsInput_ObjectIdentity = ObjectIdentity
lcUpsInput = _LcUpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3)
)


class _LcUpsInputFrequency_Type(Integer32):
    """Custom type lcUpsInputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsInputFrequency_Type.__name__ = "Integer32"
_LcUpsInputFrequency_Object = MibScalar
lcUpsInputFrequency = _LcUpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 1),
    _LcUpsInputFrequency_Type()
)
lcUpsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputFrequency.setStatus("optional")


class _LcUpsInputNumLines_Type(Integer32):
    """Custom type lcUpsInputNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsInputNumLines_Type.__name__ = "Integer32"
_LcUpsInputNumLines_Object = MibScalar
lcUpsInputNumLines = _LcUpsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 5),
    _LcUpsInputNumLines_Type()
)
lcUpsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputNumLines.setStatus("optional")
_LcUpsInputTable_Object = MibTable
lcUpsInputTable = _LcUpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    lcUpsInputTable.setStatus("optional")
_LcUpsInputEntry_Object = MibTableRow
lcUpsInputEntry = _LcUpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1)
)
lcUpsInputEntry.setIndexNames(
    (0, "LIEBERT-SERIES-200-UPS-MIB", "lcUpsInputLine"),
)
if mibBuilder.loadTexts:
    lcUpsInputEntry.setStatus("optional")


class _LcUpsInputLine_Type(Integer32):
    """Custom type lcUpsInputLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsInputLine_Type.__name__ = "Integer32"
_LcUpsInputLine_Object = MibTableColumn
lcUpsInputLine = _LcUpsInputLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 1),
    _LcUpsInputLine_Type()
)
lcUpsInputLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputLine.setStatus("optional")


class _LcUpsInputVoltage_Type(Integer32):
    """Custom type lcUpsInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsInputVoltage_Type.__name__ = "Integer32"
_LcUpsInputVoltage_Object = MibTableColumn
lcUpsInputVoltage = _LcUpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 2),
    _LcUpsInputVoltage_Type()
)
lcUpsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputVoltage.setStatus("optional")
_LcUpsOutput_ObjectIdentity = ObjectIdentity
lcUpsOutput = _LcUpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4)
)


class _LcUpsOutputFrequency_Type(Integer32):
    """Custom type lcUpsOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputFrequency_Type.__name__ = "Integer32"
_LcUpsOutputFrequency_Object = MibScalar
lcUpsOutputFrequency = _LcUpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 1),
    _LcUpsOutputFrequency_Type()
)
lcUpsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputFrequency.setStatus("optional")


class _LcUpsOutputLoad_Type(Integer32):
    """Custom type lcUpsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LcUpsOutputLoad_Type.__name__ = "Integer32"
_LcUpsOutputLoad_Object = MibScalar
lcUpsOutputLoad = _LcUpsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 2),
    _LcUpsOutputLoad_Type()
)
lcUpsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputLoad.setStatus("optional")


class _LcUpsOutputNumLines_Type(Integer32):
    """Custom type lcUpsOutputNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsOutputNumLines_Type.__name__ = "Integer32"
_LcUpsOutputNumLines_Object = MibScalar
lcUpsOutputNumLines = _LcUpsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 3),
    _LcUpsOutputNumLines_Type()
)
lcUpsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputNumLines.setStatus("optional")
_LcUpsOutputTable_Object = MibTable
lcUpsOutputTable = _LcUpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lcUpsOutputTable.setStatus("optional")
_LcUpsOutputEntry_Object = MibTableRow
lcUpsOutputEntry = _LcUpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1)
)
lcUpsOutputEntry.setIndexNames(
    (0, "LIEBERT-SERIES-200-UPS-MIB", "lcUpsOutputLine"),
)
if mibBuilder.loadTexts:
    lcUpsOutputEntry.setStatus("optional")


class _LcUpsOutputLine_Type(Integer32):
    """Custom type lcUpsOutputLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsOutputLine_Type.__name__ = "Integer32"
_LcUpsOutputLine_Object = MibTableColumn
lcUpsOutputLine = _LcUpsOutputLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 1),
    _LcUpsOutputLine_Type()
)
lcUpsOutputLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputLine.setStatus("optional")


class _LcUpsOutputVoltage_Type(Integer32):
    """Custom type lcUpsOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputVoltage_Type.__name__ = "Integer32"
_LcUpsOutputVoltage_Object = MibTableColumn
lcUpsOutputVoltage = _LcUpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 2),
    _LcUpsOutputVoltage_Type()
)
lcUpsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputVoltage.setStatus("optional")


class _LcUpsOutputCurrent_Type(Integer32):
    """Custom type lcUpsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputCurrent_Type.__name__ = "Integer32"
_LcUpsOutputCurrent_Object = MibTableColumn
lcUpsOutputCurrent = _LcUpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 3),
    _LcUpsOutputCurrent_Type()
)
lcUpsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputCurrent.setStatus("optional")


class _LcUpsOutputVA_Type(Integer32):
    """Custom type lcUpsOutputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsOutputVA_Type.__name__ = "Integer32"
_LcUpsOutputVA_Object = MibTableColumn
lcUpsOutputVA = _LcUpsOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 4),
    _LcUpsOutputVA_Type()
)
lcUpsOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputVA.setStatus("optional")


class _LcUpsOutputWatts_Type(Integer32):
    """Custom type lcUpsOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsOutputWatts_Type.__name__ = "Integer32"
_LcUpsOutputWatts_Object = MibScalar
lcUpsOutputWatts = _LcUpsOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 5),
    _LcUpsOutputWatts_Type()
)
lcUpsOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputWatts.setStatus("optional")
_LcUpsInverter_ObjectIdentity = ObjectIdentity
lcUpsInverter = _LcUpsInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5)
)


class _LcUpsInverterStatus_Type(Integer32):
    """Custom type lcUpsInverterStatus based on Integer32"""
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
          ("on", 2),
          ("off", 3))
    )


_LcUpsInverterStatus_Type.__name__ = "Integer32"
_LcUpsInverterStatus_Object = MibScalar
lcUpsInverterStatus = _LcUpsInverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5, 1),
    _LcUpsInverterStatus_Type()
)
lcUpsInverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInverterStatus.setStatus("optional")
_LcUpsAlarm_ObjectIdentity = ObjectIdentity
lcUpsAlarm = _LcUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6)
)
_LcUpsAlarms_Type = Gauge32
_LcUpsAlarms_Object = MibScalar
lcUpsAlarms = _LcUpsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 1),
    _LcUpsAlarms_Type()
)
lcUpsAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarms.setStatus("optional")
_LcUpsAlarmTable_Object = MibTable
lcUpsAlarmTable = _LcUpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    lcUpsAlarmTable.setStatus("optional")
_LcUpsAlarmEntry_Object = MibTableRow
lcUpsAlarmEntry = _LcUpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1)
)
lcUpsAlarmEntry.setIndexNames(
    (0, "LIEBERT-SERIES-200-UPS-MIB", "lcUpsAlarmId"),
)
if mibBuilder.loadTexts:
    lcUpsAlarmEntry.setStatus("optional")


class _LcUpsAlarmId_Type(Integer32):
    """Custom type lcUpsAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsAlarmId_Type.__name__ = "Integer32"
_LcUpsAlarmId_Object = MibTableColumn
lcUpsAlarmId = _LcUpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 1),
    _LcUpsAlarmId_Type()
)
lcUpsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmId.setStatus("optional")
_LcUpsAlarmDescr_Type = ObjectIdentifier
_LcUpsAlarmDescr_Object = MibTableColumn
lcUpsAlarmDescr = _LcUpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 2),
    _LcUpsAlarmDescr_Type()
)
lcUpsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmDescr.setStatus("optional")
_LcUpsAlarmTime_Type = TimeTicks
_LcUpsAlarmTime_Object = MibTableColumn
lcUpsAlarmTime = _LcUpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 3),
    _LcUpsAlarmTime_Type()
)
lcUpsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmTime.setStatus("optional")
_LcUpsAlarmConditions_ObjectIdentity = ObjectIdentity
lcUpsAlarmConditions = _LcUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3)
)
_LcUpsAlarmLowBatteryWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmLowBatteryWarning = _LcUpsAlarmLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 1)
)
_LcUpsAlarmUtilFailed_ObjectIdentity = ObjectIdentity
lcUpsAlarmUtilFailed = _LcUpsAlarmUtilFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 3)
)
_LcUpsAlarmOverTempWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmOverTempWarning = _LcUpsAlarmOverTempWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 4)
)
_LcUpsAlarmOutputOverloadWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputOverloadWarning = _LcUpsAlarmOutputOverloadWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 6)
)
_LcUpsAlarmInputOverVoltage_ObjectIdentity = ObjectIdentity
lcUpsAlarmInputOverVoltage = _LcUpsAlarmInputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 8)
)
_LcUpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
lcUpsAlarmBatteryBad = _LcUpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 9)
)
_LcUpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
lcUpsAlarmOnBattery = _LcUpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 10)
)
_LcUpsAlarmStopNoticeIssued_ObjectIdentity = ObjectIdentity
lcUpsAlarmStopNoticeIssued = _LcUpsAlarmStopNoticeIssued_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 11)
)
_LcUpsAlarmUpsOff_ObjectIdentity = ObjectIdentity
lcUpsAlarmUpsOff = _LcUpsAlarmUpsOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 12)
)
_LcUpsTest_ObjectIdentity = ObjectIdentity
lcUpsTest = _LcUpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7)
)


class _LcUpsTestBattery_Type(Integer32):
    """Custom type lcUpsTestBattery based on Integer32"""
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
          ("start", 2),
          ("abort", 3))
    )


_LcUpsTestBattery_Type.__name__ = "Integer32"
_LcUpsTestBattery_Object = MibScalar
lcUpsTestBattery = _LcUpsTestBattery_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 1),
    _LcUpsTestBattery_Type()
)
lcUpsTestBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsTestBattery.setStatus("optional")


class _LcUpsTestBatteryStatus_Type(Integer32):
    """Custom type lcUpsTestBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("sysFailure", 5),
          ("notSupported", 6),
          ("inhibited", 7))
    )


_LcUpsTestBatteryStatus_Type.__name__ = "Integer32"
_LcUpsTestBatteryStatus_Object = MibScalar
lcUpsTestBatteryStatus = _LcUpsTestBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 2),
    _LcUpsTestBatteryStatus_Type()
)
lcUpsTestBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsTestBatteryStatus.setStatus("optional")
_LcUpsControl_ObjectIdentity = ObjectIdentity
lcUpsControl = _LcUpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8)
)


class _LcUpsControlOutputOffDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOffDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOffDelay_Object = MibScalar
lcUpsControlOutputOffDelay = _LcUpsControlOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 1),
    _LcUpsControlOutputOffDelay_Type()
)
lcUpsControlOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOffDelay.setStatus("optional")


class _LcUpsControlOutputOnDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOnDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOnDelay_Object = MibScalar
lcUpsControlOutputOnDelay = _LcUpsControlOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 2),
    _LcUpsControlOutputOnDelay_Type()
)
lcUpsControlOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOnDelay.setStatus("optional")


class _LcUpsControlOutputOffTrapDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOffTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOffTrapDelay_Object = MibScalar
lcUpsControlOutputOffTrapDelay = _LcUpsControlOutputOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 3),
    _LcUpsControlOutputOffTrapDelay_Type()
)
lcUpsControlOutputOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOffTrapDelay.setStatus("optional")


class _LcUpsControlOutputOnTrapDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOnTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOnTrapDelay_Object = MibScalar
lcUpsControlOutputOnTrapDelay = _LcUpsControlOutputOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 4),
    _LcUpsControlOutputOnTrapDelay_Type()
)
lcUpsControlOutputOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOnTrapDelay.setStatus("optional")


class _LcUpsControlUnixShutdownDelay_Type(Integer32):
    """Custom type lcUpsControlUnixShutdownDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlUnixShutdownDelay_Type.__name__ = "Integer32"
_LcUpsControlUnixShutdownDelay_Object = MibScalar
lcUpsControlUnixShutdownDelay = _LcUpsControlUnixShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 5),
    _LcUpsControlUnixShutdownDelay_Type()
)
lcUpsControlUnixShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlUnixShutdownDelay.setStatus("optional")


class _LcUpsControlUnixShutdownTrapDelay_Type(Integer32):
    """Custom type lcUpsControlUnixShutdownTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlUnixShutdownTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlUnixShutdownTrapDelay_Object = MibScalar
lcUpsControlUnixShutdownTrapDelay = _LcUpsControlUnixShutdownTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 6),
    _LcUpsControlUnixShutdownTrapDelay_Type()
)
lcUpsControlUnixShutdownTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlUnixShutdownTrapDelay.setStatus("optional")


class _LcUpsControlCancelCommands_Type(Integer32):
    """Custom type lcUpsControlCancelCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("cancel", 2))
    )


_LcUpsControlCancelCommands_Type.__name__ = "Integer32"
_LcUpsControlCancelCommands_Object = MibScalar
lcUpsControlCancelCommands = _LcUpsControlCancelCommands_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 7),
    _LcUpsControlCancelCommands_Type()
)
lcUpsControlCancelCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlCancelCommands.setStatus("optional")


class _LcUpsControlRebootAgentDelay_Type(Integer32):
    """Custom type lcUpsControlRebootAgentDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlRebootAgentDelay_Type.__name__ = "Integer32"
_LcUpsControlRebootAgentDelay_Object = MibScalar
lcUpsControlRebootAgentDelay = _LcUpsControlRebootAgentDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 8),
    _LcUpsControlRebootAgentDelay_Type()
)
lcUpsControlRebootAgentDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlRebootAgentDelay.setStatus("optional")
_LcUpsNominal_ObjectIdentity = ObjectIdentity
lcUpsNominal = _LcUpsNominal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9)
)


class _LcUpsNominalOutputVoltage_Type(Integer32):
    """Custom type lcUpsNominalOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputVoltage_Type.__name__ = "Integer32"
_LcUpsNominalOutputVoltage_Object = MibScalar
lcUpsNominalOutputVoltage = _LcUpsNominalOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 1),
    _LcUpsNominalOutputVoltage_Type()
)
lcUpsNominalOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputVoltage.setStatus("optional")


class _LcUpsNominalInputVoltage_Type(Integer32):
    """Custom type lcUpsNominalInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalInputVoltage_Type.__name__ = "Integer32"
_LcUpsNominalInputVoltage_Object = MibScalar
lcUpsNominalInputVoltage = _LcUpsNominalInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 2),
    _LcUpsNominalInputVoltage_Type()
)
lcUpsNominalInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalInputVoltage.setStatus("optional")


class _LcUpsNominalOutputVA_Type(Integer32):
    """Custom type lcUpsNominalOutputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputVA_Type.__name__ = "Integer32"
_LcUpsNominalOutputVA_Object = MibScalar
lcUpsNominalOutputVA = _LcUpsNominalOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 3),
    _LcUpsNominalOutputVA_Type()
)
lcUpsNominalOutputVA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputVA.setStatus("optional")


class _LcUpsNominalOutputWatts_Type(Integer32):
    """Custom type lcUpsNominalOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputWatts_Type.__name__ = "Integer32"
_LcUpsNominalOutputWatts_Object = MibScalar
lcUpsNominalOutputWatts = _LcUpsNominalOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 4),
    _LcUpsNominalOutputWatts_Type()
)
lcUpsNominalOutputWatts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputWatts.setStatus("optional")


class _LcUpsNominalOutputFreq_Type(Integer32):
    """Custom type lcUpsNominalOutputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputFreq_Type.__name__ = "Integer32"
_LcUpsNominalOutputFreq_Object = MibScalar
lcUpsNominalOutputFreq = _LcUpsNominalOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 5),
    _LcUpsNominalOutputFreq_Type()
)
lcUpsNominalOutputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputFreq.setStatus("optional")


class _LcUpsNominalInputFreq_Type(Integer32):
    """Custom type lcUpsNominalInputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalInputFreq_Type.__name__ = "Integer32"
_LcUpsNominalInputFreq_Object = MibScalar
lcUpsNominalInputFreq = _LcUpsNominalInputFreq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 6),
    _LcUpsNominalInputFreq_Type()
)
lcUpsNominalInputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalInputFreq.setStatus("optional")
_LcUpsTraps_ObjectIdentity = ObjectIdentity
lcUpsTraps = _LcUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11)
)
_LuSeries200_ObjectIdentity = ObjectIdentity
luSeries200 = _LuSeries200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8)
)
_LuSeries200Input_ObjectIdentity = ObjectIdentity
luSeries200Input = _LuSeries200Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3)
)


class _LuSeries200InputMaxVoltsSinceLastPoll_Type(Integer32):
    """Custom type luSeries200InputMaxVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LuSeries200InputMaxVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LuSeries200InputMaxVoltsSinceLastPoll_Object = MibScalar
luSeries200InputMaxVoltsSinceLastPoll = _LuSeries200InputMaxVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3, 1),
    _LuSeries200InputMaxVoltsSinceLastPoll_Type()
)
luSeries200InputMaxVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200InputMaxVoltsSinceLastPoll.setStatus("optional")


class _LuSeries200InputMinVoltsSinceLastPoll_Type(Integer32):
    """Custom type luSeries200InputMinVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LuSeries200InputMinVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LuSeries200InputMinVoltsSinceLastPoll_Object = MibScalar
luSeries200InputMinVoltsSinceLastPoll = _LuSeries200InputMinVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3, 2),
    _LuSeries200InputMinVoltsSinceLastPoll_Type()
)
luSeries200InputMinVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200InputMinVoltsSinceLastPoll.setStatus("optional")
_LuSeries200Alarm_ObjectIdentity = ObjectIdentity
luSeries200Alarm = _LuSeries200Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6)
)
_LuSeries200AlarmConditions_ObjectIdentity = ObjectIdentity
luSeries200AlarmConditions = _LuSeries200AlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6, 1)
)
_LuSeries200AlarmInputFreqError_ObjectIdentity = ObjectIdentity
luSeries200AlarmInputFreqError = _LuSeries200AlarmInputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6, 1, 1)
)
_LuSeries200Config_ObjectIdentity = ObjectIdentity
luSeries200Config = _LuSeries200Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12)
)


class _LuSeries200ConfigBypassInstalled_Type(Integer32):
    """Custom type luSeries200ConfigBypassInstalled based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_LuSeries200ConfigBypassInstalled_Type.__name__ = "Integer32"
_LuSeries200ConfigBypassInstalled_Object = MibScalar
luSeries200ConfigBypassInstalled = _LuSeries200ConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12, 1),
    _LuSeries200ConfigBypassInstalled_Type()
)
luSeries200ConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200ConfigBypassInstalled.setStatus("optional")


class _LuSeries200ConfigFrequencyChangerModel_Type(Integer32):
    """Custom type luSeries200ConfigFrequencyChangerModel based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_LuSeries200ConfigFrequencyChangerModel_Type.__name__ = "Integer32"
_LuSeries200ConfigFrequencyChangerModel_Object = MibScalar
luSeries200ConfigFrequencyChangerModel = _LuSeries200ConfigFrequencyChangerModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12, 2),
    _LuSeries200ConfigFrequencyChangerModel_Type()
)
luSeries200ConfigFrequencyChangerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200ConfigFrequencyChangerModel.setStatus("optional")
_LuSeries200Bypass_ObjectIdentity = ObjectIdentity
luSeries200Bypass = _LuSeries200Bypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 13)
)


class _LuSeries200OnBypass_Type(Integer32):
    """Custom type luSeries200OnBypass based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_LuSeries200OnBypass_Type.__name__ = "Integer32"
_LuSeries200OnBypass_Object = MibScalar
luSeries200OnBypass = _LuSeries200OnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 13, 1),
    _LuSeries200OnBypass_Type()
)
luSeries200OnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200OnBypass.setStatus("optional")
_LuExperimental_ObjectIdentity = ObjectIdentity
luExperimental = _LuExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 2)
)
_LuPrivate_ObjectIdentity = ObjectIdentity
luPrivate = _LuPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 3)
)

# Managed Objects groups


# Notification objects

lcUpsOverloadWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 1)
)
lcUpsOverloadWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverloadWarningTrap.setStatus(
        ""
    )

lcUpsOnBatteryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 3)
)
lcUpsOnBatteryTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOnBatteryTrap.setStatus(
        ""
    )

lcUpsLowBatteryWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 4)
)
lcUpsLowBatteryWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLowBatteryWarningTrap.setStatus(
        ""
    )

lcUpsUtilPowerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 6)
)
lcUpsUtilPowerFailedTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUtilPowerFailedTrap.setStatus(
        ""
    )

lcUpsUtilPowerRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 7)
)
lcUpsUtilPowerRestoredTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUtilPowerRestoredTrap.setStatus(
        ""
    )

lcUpsInputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 8)
)
lcUpsInputOverVoltageTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInputOverVoltageTrap.setStatus(
        ""
    )

lcUpsOverTempWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 9)
)
lcUpsOverTempWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverTempWarningTrap.setStatus(
        ""
    )

lcUpsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 11)
)
lcUpsAlarmTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsAlarmTrap.setStatus(
        ""
    )

lcUpsOutputOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 12)
)
lcUpsOutputOffTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOffTrap.setStatus(
        ""
    )

lcUpsOutputOffWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 13)
)
lcUpsOutputOffWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOffWarningTrap.setStatus(
        ""
    )

lcUpsOutputOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 14)
)
lcUpsOutputOnTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOnTrap.setStatus(
        ""
    )

lcUpsOutputOnWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 15)
)
lcUpsOutputOnWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOnWarningTrap.setStatus(
        ""
    )

lcUpsUnixShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 16)
)
lcUpsUnixShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUnixShutdownTrap.setStatus(
        ""
    )

lcUpsUnixShutdownWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 17)
)
lcUpsUnixShutdownWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUnixShutdownWarningTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-SERIES-200-UPS-MIB",
    **{"emerson": emerson,
       "liebertCorp": liebertCorp,
       "liebertUps": liebertUps,
       "luExtensions": luExtensions,
       "luCore": luCore,
       "lcUpsIdent": lcUpsIdent,
       "lcUpsIdentManufacturer": lcUpsIdentManufacturer,
       "lcUpsIdentModel": lcUpsIdentModel,
       "lcUpsIdentSoftwareVersion": lcUpsIdentSoftwareVersion,
       "lcUpsIdentSpecific": lcUpsIdentSpecific,
       "lcUpsBattery": lcUpsBattery,
       "lcUpsBatTimeRemaining": lcUpsBatTimeRemaining,
       "lcUpsBatVoltage": lcUpsBatVoltage,
       "lcUpsBatCapacity": lcUpsBatCapacity,
       "lcUpsInput": lcUpsInput,
       "lcUpsInputFrequency": lcUpsInputFrequency,
       "lcUpsInputNumLines": lcUpsInputNumLines,
       "lcUpsInputTable": lcUpsInputTable,
       "lcUpsInputEntry": lcUpsInputEntry,
       "lcUpsInputLine": lcUpsInputLine,
       "lcUpsInputVoltage": lcUpsInputVoltage,
       "lcUpsOutput": lcUpsOutput,
       "lcUpsOutputFrequency": lcUpsOutputFrequency,
       "lcUpsOutputLoad": lcUpsOutputLoad,
       "lcUpsOutputNumLines": lcUpsOutputNumLines,
       "lcUpsOutputTable": lcUpsOutputTable,
       "lcUpsOutputEntry": lcUpsOutputEntry,
       "lcUpsOutputLine": lcUpsOutputLine,
       "lcUpsOutputVoltage": lcUpsOutputVoltage,
       "lcUpsOutputCurrent": lcUpsOutputCurrent,
       "lcUpsOutputVA": lcUpsOutputVA,
       "lcUpsOutputWatts": lcUpsOutputWatts,
       "lcUpsInverter": lcUpsInverter,
       "lcUpsInverterStatus": lcUpsInverterStatus,
       "lcUpsAlarm": lcUpsAlarm,
       "lcUpsAlarms": lcUpsAlarms,
       "lcUpsAlarmTable": lcUpsAlarmTable,
       "lcUpsAlarmEntry": lcUpsAlarmEntry,
       "lcUpsAlarmId": lcUpsAlarmId,
       "lcUpsAlarmDescr": lcUpsAlarmDescr,
       "lcUpsAlarmTime": lcUpsAlarmTime,
       "lcUpsAlarmConditions": lcUpsAlarmConditions,
       "lcUpsAlarmLowBatteryWarning": lcUpsAlarmLowBatteryWarning,
       "lcUpsAlarmUtilFailed": lcUpsAlarmUtilFailed,
       "lcUpsAlarmOverTempWarning": lcUpsAlarmOverTempWarning,
       "lcUpsAlarmOutputOverloadWarning": lcUpsAlarmOutputOverloadWarning,
       "lcUpsAlarmInputOverVoltage": lcUpsAlarmInputOverVoltage,
       "lcUpsAlarmBatteryBad": lcUpsAlarmBatteryBad,
       "lcUpsAlarmOnBattery": lcUpsAlarmOnBattery,
       "lcUpsAlarmStopNoticeIssued": lcUpsAlarmStopNoticeIssued,
       "lcUpsAlarmUpsOff": lcUpsAlarmUpsOff,
       "lcUpsTest": lcUpsTest,
       "lcUpsTestBattery": lcUpsTestBattery,
       "lcUpsTestBatteryStatus": lcUpsTestBatteryStatus,
       "lcUpsControl": lcUpsControl,
       "lcUpsControlOutputOffDelay": lcUpsControlOutputOffDelay,
       "lcUpsControlOutputOnDelay": lcUpsControlOutputOnDelay,
       "lcUpsControlOutputOffTrapDelay": lcUpsControlOutputOffTrapDelay,
       "lcUpsControlOutputOnTrapDelay": lcUpsControlOutputOnTrapDelay,
       "lcUpsControlUnixShutdownDelay": lcUpsControlUnixShutdownDelay,
       "lcUpsControlUnixShutdownTrapDelay": lcUpsControlUnixShutdownTrapDelay,
       "lcUpsControlCancelCommands": lcUpsControlCancelCommands,
       "lcUpsControlRebootAgentDelay": lcUpsControlRebootAgentDelay,
       "lcUpsNominal": lcUpsNominal,
       "lcUpsNominalOutputVoltage": lcUpsNominalOutputVoltage,
       "lcUpsNominalInputVoltage": lcUpsNominalInputVoltage,
       "lcUpsNominalOutputVA": lcUpsNominalOutputVA,
       "lcUpsNominalOutputWatts": lcUpsNominalOutputWatts,
       "lcUpsNominalOutputFreq": lcUpsNominalOutputFreq,
       "lcUpsNominalInputFreq": lcUpsNominalInputFreq,
       "lcUpsTraps": lcUpsTraps,
       "lcUpsOverloadWarningTrap": lcUpsOverloadWarningTrap,
       "lcUpsOnBatteryTrap": lcUpsOnBatteryTrap,
       "lcUpsLowBatteryWarningTrap": lcUpsLowBatteryWarningTrap,
       "lcUpsUtilPowerFailedTrap": lcUpsUtilPowerFailedTrap,
       "lcUpsUtilPowerRestoredTrap": lcUpsUtilPowerRestoredTrap,
       "lcUpsInputOverVoltageTrap": lcUpsInputOverVoltageTrap,
       "lcUpsOverTempWarningTrap": lcUpsOverTempWarningTrap,
       "lcUpsAlarmTrap": lcUpsAlarmTrap,
       "lcUpsOutputOffTrap": lcUpsOutputOffTrap,
       "lcUpsOutputOffWarningTrap": lcUpsOutputOffWarningTrap,
       "lcUpsOutputOnTrap": lcUpsOutputOnTrap,
       "lcUpsOutputOnWarningTrap": lcUpsOutputOnWarningTrap,
       "lcUpsUnixShutdownTrap": lcUpsUnixShutdownTrap,
       "lcUpsUnixShutdownWarningTrap": lcUpsUnixShutdownWarningTrap,
       "luSeries200": luSeries200,
       "luSeries200Input": luSeries200Input,
       "luSeries200InputMaxVoltsSinceLastPoll": luSeries200InputMaxVoltsSinceLastPoll,
       "luSeries200InputMinVoltsSinceLastPoll": luSeries200InputMinVoltsSinceLastPoll,
       "luSeries200Alarm": luSeries200Alarm,
       "luSeries200AlarmConditions": luSeries200AlarmConditions,
       "luSeries200AlarmInputFreqError": luSeries200AlarmInputFreqError,
       "luSeries200Config": luSeries200Config,
       "luSeries200ConfigBypassInstalled": luSeries200ConfigBypassInstalled,
       "luSeries200ConfigFrequencyChangerModel": luSeries200ConfigFrequencyChangerModel,
       "luSeries200Bypass": luSeries200Bypass,
       "luSeries200OnBypass": luSeries200OnBypass,
       "luExperimental": luExperimental,
       "luPrivate": luPrivate}
)
