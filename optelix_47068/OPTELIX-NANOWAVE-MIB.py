# SNMP MIB module (OPTELIX-NANOWAVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/optelix_47068/OPTELIX-NANOWAVE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:48:38 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

optelix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47068)
)
if mibBuilder.loadTexts:
    optelix.setRevisions(
        ("2016-01-20 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Subsection_ObjectIdentity = ObjectIdentity
subsection = _Subsection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1)
)
_Nanowave_ObjectIdentity = ObjectIdentity
nanowave = _Nanowave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1)
)
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 1)
)


class _AllAlarms_Type(Integer32):
    """Custom type allAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AllAlarms_Type.__name__ = "Integer32"
_AllAlarms_Object = MibScalar
allAlarms = _AllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 1, 1),
    _AllAlarms_Type()
)
allAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allAlarms.setStatus("current")


class _NanowaveLowRSSIAlarm_Type(Integer32):
    """Custom type nanowaveLowRSSIAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NanowaveLowRSSIAlarm_Type.__name__ = "Integer32"
_NanowaveLowRSSIAlarm_Object = MibScalar
nanowaveLowRSSIAlarm = _NanowaveLowRSSIAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 1, 2),
    _NanowaveLowRSSIAlarm_Type()
)
nanowaveLowRSSIAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowaveLowRSSIAlarm.setStatus("current")


class _NanowaveLowAPDVoltageAlarm_Type(Integer32):
    """Custom type nanowaveLowAPDVoltageAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NanowaveLowAPDVoltageAlarm_Type.__name__ = "Integer32"
_NanowaveLowAPDVoltageAlarm_Object = MibScalar
nanowaveLowAPDVoltageAlarm = _NanowaveLowAPDVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 1, 3),
    _NanowaveLowAPDVoltageAlarm_Type()
)
nanowaveLowAPDVoltageAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowaveLowAPDVoltageAlarm.setStatus("current")


class _NanowaveLow12VVoltageAlarm_Type(Integer32):
    """Custom type nanowaveLow12VVoltageAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NanowaveLow12VVoltageAlarm_Type.__name__ = "Integer32"
_NanowaveLow12VVoltageAlarm_Object = MibScalar
nanowaveLow12VVoltageAlarm = _NanowaveLow12VVoltageAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 1, 4),
    _NanowaveLow12VVoltageAlarm_Type()
)
nanowaveLow12VVoltageAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowaveLow12VVoltageAlarm.setStatus("current")


class _NanowaveLowLaserPowerAlarm_Type(Integer32):
    """Custom type nanowaveLowLaserPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NanowaveLowLaserPowerAlarm_Type.__name__ = "Integer32"
_NanowaveLowLaserPowerAlarm_Object = MibScalar
nanowaveLowLaserPowerAlarm = _NanowaveLowLaserPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 1, 5),
    _NanowaveLowLaserPowerAlarm_Type()
)
nanowaveLowLaserPowerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowaveLowLaserPowerAlarm.setStatus("current")
_Parameters_ObjectIdentity = ObjectIdentity
parameters = _Parameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2)
)


class _NanowaveRSSI_Type(Integer32):
    """Custom type nanowaveRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NanowaveRSSI_Type.__name__ = "Integer32"
_NanowaveRSSI_Object = MibScalar
nanowaveRSSI = _NanowaveRSSI_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 1),
    _NanowaveRSSI_Type()
)
nanowaveRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowaveRSSI.setStatus("current")


class _NanowavePAV1_Type(Integer32):
    """Custom type nanowavePAV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NanowavePAV1_Type.__name__ = "Integer32"
_NanowavePAV1_Object = MibScalar
nanowavePAV1 = _NanowavePAV1_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 2),
    _NanowavePAV1_Type()
)
nanowavePAV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowavePAV1.setStatus("current")


class _NanowavePAV2_Type(Integer32):
    """Custom type nanowavePAV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NanowavePAV2_Type.__name__ = "Integer32"
_NanowavePAV2_Object = MibScalar
nanowavePAV2 = _NanowavePAV2_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 3),
    _NanowavePAV2_Type()
)
nanowavePAV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowavePAV2.setStatus("current")


class _NanowavePAV3_Type(Integer32):
    """Custom type nanowavePAV3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NanowavePAV3_Type.__name__ = "Integer32"
_NanowavePAV3_Object = MibScalar
nanowavePAV3 = _NanowavePAV3_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 4),
    _NanowavePAV3_Type()
)
nanowavePAV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowavePAV3.setStatus("current")


class _NanowavePAV4_Type(Integer32):
    """Custom type nanowavePAV4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NanowavePAV4_Type.__name__ = "Integer32"
_NanowavePAV4_Object = MibScalar
nanowavePAV4 = _NanowavePAV4_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 5),
    _NanowavePAV4_Type()
)
nanowavePAV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowavePAV4.setStatus("current")


class _NanowaveAPDVoltage_Type(Integer32):
    """Custom type nanowaveAPDVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(140, 200),
    )


_NanowaveAPDVoltage_Type.__name__ = "Integer32"
_NanowaveAPDVoltage_Object = MibScalar
nanowaveAPDVoltage = _NanowaveAPDVoltage_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 6),
    _NanowaveAPDVoltage_Type()
)
nanowaveAPDVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowaveAPDVoltage.setStatus("current")


class _NanowaveAPDTemperature_Type(Integer32):
    """Custom type nanowaveAPDTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 14),
    )


_NanowaveAPDTemperature_Type.__name__ = "Integer32"
_NanowaveAPDTemperature_Object = MibScalar
nanowaveAPDTemperature = _NanowaveAPDTemperature_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 7),
    _NanowaveAPDTemperature_Type()
)
nanowaveAPDTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowaveAPDTemperature.setStatus("current")


class _NanowaveSoftwareVersion_Type(Integer32):
    """Custom type nanowaveSoftwareVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NanowaveSoftwareVersion_Type.__name__ = "Integer32"
_NanowaveSoftwareVersion_Object = MibScalar
nanowaveSoftwareVersion = _NanowaveSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 8),
    _NanowaveSoftwareVersion_Type()
)
nanowaveSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nanowaveSoftwareVersion.setStatus("current")
_Logs_ObjectIdentity = ObjectIdentity
logs = _Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 3)
)


class _NanowaveHours_Type(Integer32):
    """Custom type nanowaveHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400000000),
    )


_NanowaveHours_Type.__name__ = "Integer32"
_NanowaveHours_Object = MibScalar
nanowaveHours = _NanowaveHours_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 3, 1),
    _NanowaveHours_Type()
)
nanowaveHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nanowaveHours.setStatus("current")
_Commands_ObjectIdentity = ObjectIdentity
commands = _Commands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 4)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 5)
)


class _NanowaveLaser1Status_Type(Integer32):
    """Custom type nanowaveLaser1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NanowaveLaser1Status_Type.__name__ = "Integer32"
_NanowaveLaser1Status_Object = MibScalar
nanowaveLaser1Status = _NanowaveLaser1Status_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 5, 1),
    _NanowaveLaser1Status_Type()
)
nanowaveLaser1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nanowaveLaser1Status.setStatus("current")


class _NanowaveLaser2Status_Type(Integer32):
    """Custom type nanowaveLaser2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NanowaveLaser2Status_Type.__name__ = "Integer32"
_NanowaveLaser2Status_Object = MibScalar
nanowaveLaser2Status = _NanowaveLaser2Status_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 5, 2),
    _NanowaveLaser2Status_Type()
)
nanowaveLaser2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nanowaveLaser2Status.setStatus("current")


class _NanowaveLaser3Status_Type(Integer32):
    """Custom type nanowaveLaser3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NanowaveLaser3Status_Type.__name__ = "Integer32"
_NanowaveLaser3Status_Object = MibScalar
nanowaveLaser3Status = _NanowaveLaser3Status_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 5, 3),
    _NanowaveLaser3Status_Type()
)
nanowaveLaser3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nanowaveLaser3Status.setStatus("current")


class _NanowaveLaser4Status_Type(Integer32):
    """Custom type nanowaveLaser4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NanowaveLaser4Status_Type.__name__ = "Integer32"
_NanowaveLaser4Status_Object = MibScalar
nanowaveLaser4Status = _NanowaveLaser4Status_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 5, 4),
    _NanowaveLaser4Status_Type()
)
nanowaveLaser4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nanowaveLaser4Status.setStatus("current")
_TrapSettings_ObjectIdentity = ObjectIdentity
trapSettings = _TrapSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6)
)


class _SnmpTrapOnAlarms_Type(Integer32):
    """Custom type snmpTrapOnAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SnmpTrapOnAlarms_Type.__name__ = "Integer32"
_SnmpTrapOnAlarms_Object = MibScalar
snmpTrapOnAlarms = _SnmpTrapOnAlarms_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 1),
    _SnmpTrapOnAlarms_Type()
)
snmpTrapOnAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapOnAlarms.setStatus("current")


class _SnmpTrapOnParams_Type(Integer32):
    """Custom type snmpTrapOnParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SnmpTrapOnParams_Type.__name__ = "Integer32"
_SnmpTrapOnParams_Object = MibScalar
snmpTrapOnParams = _SnmpTrapOnParams_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 2),
    _SnmpTrapOnParams_Type()
)
snmpTrapOnParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapOnParams.setStatus("current")


class _SnmpTrapOnLogs_Type(Integer32):
    """Custom type snmpTrapOnLogs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SnmpTrapOnLogs_Type.__name__ = "Integer32"
_SnmpTrapOnLogs_Object = MibScalar
snmpTrapOnLogs = _SnmpTrapOnLogs_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 3),
    _SnmpTrapOnLogs_Type()
)
snmpTrapOnLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapOnLogs.setStatus("current")


class _SnmpTrapOnStatus_Type(Integer32):
    """Custom type snmpTrapOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SnmpTrapOnStatus_Type.__name__ = "Integer32"
_SnmpTrapOnStatus_Object = MibScalar
snmpTrapOnStatus = _SnmpTrapOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 4),
    _SnmpTrapOnStatus_Type()
)
snmpTrapOnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapOnStatus.setStatus("current")


class _SnmpAlarmInterval_Type(Integer32):
    """Custom type snmpAlarmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SnmpAlarmInterval_Type.__name__ = "Integer32"
_SnmpAlarmInterval_Object = MibScalar
snmpAlarmInterval = _SnmpAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 5),
    _SnmpAlarmInterval_Type()
)
snmpAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAlarmInterval.setStatus("current")


class _SnmpParamInterval_Type(Integer32):
    """Custom type snmpParamInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SnmpParamInterval_Type.__name__ = "Integer32"
_SnmpParamInterval_Object = MibScalar
snmpParamInterval = _SnmpParamInterval_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 6),
    _SnmpParamInterval_Type()
)
snmpParamInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpParamInterval.setStatus("current")


class _SnmpLogInterval_Type(Integer32):
    """Custom type snmpLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SnmpLogInterval_Type.__name__ = "Integer32"
_SnmpLogInterval_Object = MibScalar
snmpLogInterval = _SnmpLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 7),
    _SnmpLogInterval_Type()
)
snmpLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpLogInterval.setStatus("current")


class _SnmpStatusInterval_Type(Integer32):
    """Custom type snmpStatusInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SnmpStatusInterval_Type.__name__ = "Integer32"
_SnmpStatusInterval_Object = MibScalar
snmpStatusInterval = _SnmpStatusInterval_Object(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 8),
    _SnmpStatusInterval_Type()
)
snmpStatusInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpStatusInterval.setStatus("current")
_ObjectGroups_ObjectIdentity = ObjectIdentity
objectGroups = _ObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 7)
)
_NotificationGroups_ObjectIdentity = ObjectIdentity
notificationGroups = _NotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 8)
)

# Managed Objects groups

allObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 7, 1)
)
allObjectGroup.setObjects(
      *(("OPTELIX-NANOWAVE-MIB", "allAlarms"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLowRSSIAlarm"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLowAPDVoltageAlarm"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLow12VVoltageAlarm"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLowLaserPowerAlarm"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveRSSI"),
        ("OPTELIX-NANOWAVE-MIB", "nanowavePAV1"),
        ("OPTELIX-NANOWAVE-MIB", "nanowavePAV2"),
        ("OPTELIX-NANOWAVE-MIB", "nanowavePAV3"),
        ("OPTELIX-NANOWAVE-MIB", "nanowavePAV4"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveAPDVoltage"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveAPDTemperature"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveSoftwareVersion"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveHours"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLaser1Status"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLaser2Status"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLaser3Status"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLaser4Status"),
        ("OPTELIX-NANOWAVE-MIB", "snmpTrapOnAlarms"),
        ("OPTELIX-NANOWAVE-MIB", "snmpTrapOnParams"),
        ("OPTELIX-NANOWAVE-MIB", "snmpTrapOnLogs"),
        ("OPTELIX-NANOWAVE-MIB", "snmpTrapOnStatus"),
        ("OPTELIX-NANOWAVE-MIB", "snmpAlarmInterval"),
        ("OPTELIX-NANOWAVE-MIB", "snmpParamInterval"),
        ("OPTELIX-NANOWAVE-MIB", "snmpLogInterval"),
        ("OPTELIX-NANOWAVE-MIB", "snmpStatusInterval"))
)
if mibBuilder.loadTexts:
    allObjectGroup.setStatus("current")


# Notification objects

alarmsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 1, 100)
)
alarmsNotification.setObjects(
      *(("OPTELIX-NANOWAVE-MIB", "allAlarms"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLowRSSIAlarm"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLowAPDVoltageAlarm"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLow12VVoltageAlarm"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLowLaserPowerAlarm"))
)
if mibBuilder.loadTexts:
    alarmsNotification.setStatus(
        "current"
    )

parametersNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 2, 100)
)
parametersNotification.setObjects(
      *(("OPTELIX-NANOWAVE-MIB", "nanowaveRSSI"),
        ("OPTELIX-NANOWAVE-MIB", "nanowavePAV1"),
        ("OPTELIX-NANOWAVE-MIB", "nanowavePAV2"),
        ("OPTELIX-NANOWAVE-MIB", "nanowavePAV3"),
        ("OPTELIX-NANOWAVE-MIB", "nanowavePAV4"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveAPDVoltage"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveAPDTemperature"))
)
if mibBuilder.loadTexts:
    parametersNotification.setStatus(
        "current"
    )

logsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 3, 100)
)
logsNotification.setObjects(
    ("OPTELIX-NANOWAVE-MIB", "nanowaveHours")
)
if mibBuilder.loadTexts:
    logsNotification.setStatus(
        "current"
    )

statusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 5, 100)
)
statusNotification.setObjects(
      *(("OPTELIX-NANOWAVE-MIB", "nanowaveLaser1Status"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLaser2Status"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLaser3Status"),
        ("OPTELIX-NANOWAVE-MIB", "nanowaveLaser4Status"))
)
if mibBuilder.loadTexts:
    statusNotification.setStatus(
        "current"
    )

settingsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 6, 100)
)
settingsNotification.setObjects(
    ("OPTELIX-NANOWAVE-MIB", "snmpTrapOnAlarms")
)
if mibBuilder.loadTexts:
    settingsNotification.setStatus(
        "current"
    )


# Notifications groups

allNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47068, 1, 1, 1, 8, 1)
)
allNotificationGroup.setObjects(
      *(("OPTELIX-NANOWAVE-MIB", "alarmsNotification"),
        ("OPTELIX-NANOWAVE-MIB", "parametersNotification"),
        ("OPTELIX-NANOWAVE-MIB", "logsNotification"),
        ("OPTELIX-NANOWAVE-MIB", "statusNotification"),
        ("OPTELIX-NANOWAVE-MIB", "settingsNotification"))
)
if mibBuilder.loadTexts:
    allNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTELIX-NANOWAVE-MIB",
    **{"optelix": optelix,
       "subsection": subsection,
       "products": products,
       "nanowave": nanowave,
       "alarms": alarms,
       "allAlarms": allAlarms,
       "nanowaveLowRSSIAlarm": nanowaveLowRSSIAlarm,
       "nanowaveLowAPDVoltageAlarm": nanowaveLowAPDVoltageAlarm,
       "nanowaveLow12VVoltageAlarm": nanowaveLow12VVoltageAlarm,
       "nanowaveLowLaserPowerAlarm": nanowaveLowLaserPowerAlarm,
       "alarmsNotification": alarmsNotification,
       "parameters": parameters,
       "nanowaveRSSI": nanowaveRSSI,
       "nanowavePAV1": nanowavePAV1,
       "nanowavePAV2": nanowavePAV2,
       "nanowavePAV3": nanowavePAV3,
       "nanowavePAV4": nanowavePAV4,
       "nanowaveAPDVoltage": nanowaveAPDVoltage,
       "nanowaveAPDTemperature": nanowaveAPDTemperature,
       "nanowaveSoftwareVersion": nanowaveSoftwareVersion,
       "parametersNotification": parametersNotification,
       "logs": logs,
       "nanowaveHours": nanowaveHours,
       "logsNotification": logsNotification,
       "commands": commands,
       "status": status,
       "nanowaveLaser1Status": nanowaveLaser1Status,
       "nanowaveLaser2Status": nanowaveLaser2Status,
       "nanowaveLaser3Status": nanowaveLaser3Status,
       "nanowaveLaser4Status": nanowaveLaser4Status,
       "statusNotification": statusNotification,
       "trapSettings": trapSettings,
       "snmpTrapOnAlarms": snmpTrapOnAlarms,
       "snmpTrapOnParams": snmpTrapOnParams,
       "snmpTrapOnLogs": snmpTrapOnLogs,
       "snmpTrapOnStatus": snmpTrapOnStatus,
       "snmpAlarmInterval": snmpAlarmInterval,
       "snmpParamInterval": snmpParamInterval,
       "snmpLogInterval": snmpLogInterval,
       "snmpStatusInterval": snmpStatusInterval,
       "settingsNotification": settingsNotification,
       "objectGroups": objectGroups,
       "allObjectGroup": allObjectGroup,
       "notificationGroups": notificationGroups,
       "allNotificationGroup": allNotificationGroup}
)
