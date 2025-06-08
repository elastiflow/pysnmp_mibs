# SNMP MIB module (SNMPv2-M2M-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SNMPv2-M2M-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:06:23 2025
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

(contextIdentity,) = mibBuilder.importSymbols(
    "SNMPv2-PARTY-MIB",
    "contextIdentity")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 InstancePointer,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "InstancePointer",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

snmpM2M = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpM2MObjects_ObjectIdentity = ObjectIdentity
snmpM2MObjects = _SnmpM2MObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 2, 1)
)
_SnmpAlarm_ObjectIdentity = ObjectIdentity
snmpAlarm = _SnmpAlarm_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 2, 1, 1)
)


class _SnmpAlarmNextIndex_Type(Integer32):
    """Custom type snmpAlarmNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpAlarmNextIndex_Type.__name__ = "Integer32"
_SnmpAlarmNextIndex_Object = MibScalar
snmpAlarmNextIndex = _SnmpAlarmNextIndex_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 1),
    _SnmpAlarmNextIndex_Type()
)
snmpAlarmNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAlarmNextIndex.setStatus("current")
_SnmpAlarmTable_Object = MibTable
snmpAlarmTable = _SnmpAlarmTable_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    snmpAlarmTable.setStatus("current")
_SnmpAlarmEntry_Object = MibTableRow
snmpAlarmEntry = _SnmpAlarmEntry_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1)
)
snmpAlarmEntry.setIndexNames(
    (0, "SNMPv2-PARTY-MIB", "contextIdentity"),
    (0, "SNMPv2-M2M-MIB", "snmpAlarmIndex"),
)
if mibBuilder.loadTexts:
    snmpAlarmEntry.setStatus("current")


class _SnmpAlarmIndex_Type(Integer32):
    """Custom type snmpAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpAlarmIndex_Type.__name__ = "Integer32"
_SnmpAlarmIndex_Object = MibTableColumn
snmpAlarmIndex = _SnmpAlarmIndex_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 1),
    _SnmpAlarmIndex_Type()
)
snmpAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpAlarmIndex.setStatus("current")
_SnmpAlarmVariable_Type = InstancePointer
_SnmpAlarmVariable_Object = MibTableColumn
snmpAlarmVariable = _SnmpAlarmVariable_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 2),
    _SnmpAlarmVariable_Type()
)
snmpAlarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmVariable.setStatus("current")
_SnmpAlarmInterval_Type = Integer32
_SnmpAlarmInterval_Object = MibTableColumn
snmpAlarmInterval = _SnmpAlarmInterval_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 3),
    _SnmpAlarmInterval_Type()
)
snmpAlarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    snmpAlarmInterval.setUnits("seconds")


class _SnmpAlarmSampleType_Type(Integer32):
    """Custom type snmpAlarmSampleType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_SnmpAlarmSampleType_Type.__name__ = "Integer32"
_SnmpAlarmSampleType_Object = MibTableColumn
snmpAlarmSampleType = _SnmpAlarmSampleType_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 4),
    _SnmpAlarmSampleType_Type()
)
snmpAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmSampleType.setStatus("current")
_SnmpAlarmValue_Type = Integer32
_SnmpAlarmValue_Object = MibTableColumn
snmpAlarmValue = _SnmpAlarmValue_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 5),
    _SnmpAlarmValue_Type()
)
snmpAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAlarmValue.setStatus("current")


class _SnmpAlarmStartupAlarm_Type(Integer32):
    """Custom type snmpAlarmStartupAlarm based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("risingAlarm", 1),
          ("fallingAlarm", 2),
          ("risingOrFallingAlarm", 3))
    )


_SnmpAlarmStartupAlarm_Type.__name__ = "Integer32"
_SnmpAlarmStartupAlarm_Object = MibTableColumn
snmpAlarmStartupAlarm = _SnmpAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 6),
    _SnmpAlarmStartupAlarm_Type()
)
snmpAlarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmStartupAlarm.setStatus("current")
_SnmpAlarmRisingThreshold_Type = Integer32
_SnmpAlarmRisingThreshold_Object = MibTableColumn
snmpAlarmRisingThreshold = _SnmpAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 7),
    _SnmpAlarmRisingThreshold_Type()
)
snmpAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmRisingThreshold.setStatus("current")
_SnmpAlarmFallingThreshold_Type = Integer32
_SnmpAlarmFallingThreshold_Object = MibTableColumn
snmpAlarmFallingThreshold = _SnmpAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 8),
    _SnmpAlarmFallingThreshold_Type()
)
snmpAlarmFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmFallingThreshold.setStatus("current")


class _SnmpAlarmRisingEventIndex_Type(Integer32):
    """Custom type snmpAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpAlarmRisingEventIndex_Type.__name__ = "Integer32"
_SnmpAlarmRisingEventIndex_Object = MibTableColumn
snmpAlarmRisingEventIndex = _SnmpAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 9),
    _SnmpAlarmRisingEventIndex_Type()
)
snmpAlarmRisingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmRisingEventIndex.setStatus("current")


class _SnmpAlarmFallingEventIndex_Type(Integer32):
    """Custom type snmpAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpAlarmFallingEventIndex_Type.__name__ = "Integer32"
_SnmpAlarmFallingEventIndex_Object = MibTableColumn
snmpAlarmFallingEventIndex = _SnmpAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 10),
    _SnmpAlarmFallingEventIndex_Type()
)
snmpAlarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmFallingEventIndex.setStatus("current")


class _SnmpAlarmUnavailableEventIndex_Type(Integer32):
    """Custom type snmpAlarmUnavailableEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpAlarmUnavailableEventIndex_Type.__name__ = "Integer32"
_SnmpAlarmUnavailableEventIndex_Object = MibTableColumn
snmpAlarmUnavailableEventIndex = _SnmpAlarmUnavailableEventIndex_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 11),
    _SnmpAlarmUnavailableEventIndex_Type()
)
snmpAlarmUnavailableEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmUnavailableEventIndex.setStatus("current")
_SnmpAlarmStatus_Type = RowStatus
_SnmpAlarmStatus_Object = MibTableColumn
snmpAlarmStatus = _SnmpAlarmStatus_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 2, 1, 12),
    _SnmpAlarmStatus_Type()
)
snmpAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpAlarmStatus.setStatus("current")
_SnmpAlarmNotifications_ObjectIdentity = ObjectIdentity
snmpAlarmNotifications = _SnmpAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 3)
)
_SnmpEvent_ObjectIdentity = ObjectIdentity
snmpEvent = _SnmpEvent_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 2, 1, 2)
)


class _SnmpEventNextIndex_Type(Integer32):
    """Custom type snmpEventNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpEventNextIndex_Type.__name__ = "Integer32"
_SnmpEventNextIndex_Object = MibScalar
snmpEventNextIndex = _SnmpEventNextIndex_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 1),
    _SnmpEventNextIndex_Type()
)
snmpEventNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEventNextIndex.setStatus("current")
_SnmpEventTable_Object = MibTable
snmpEventTable = _SnmpEventTable_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    snmpEventTable.setStatus("current")
_SnmpEventEntry_Object = MibTableRow
snmpEventEntry = _SnmpEventEntry_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 2, 1)
)
snmpEventEntry.setIndexNames(
    (0, "SNMPv2-M2M-MIB", "snmpEventIndex"),
)
if mibBuilder.loadTexts:
    snmpEventEntry.setStatus("current")


class _SnmpEventIndex_Type(Integer32):
    """Custom type snmpEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpEventIndex_Type.__name__ = "Integer32"
_SnmpEventIndex_Object = MibTableColumn
snmpEventIndex = _SnmpEventIndex_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 2, 1, 1),
    _SnmpEventIndex_Type()
)
snmpEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpEventIndex.setStatus("current")
_SnmpEventID_Type = ObjectIdentifier
_SnmpEventID_Object = MibTableColumn
snmpEventID = _SnmpEventID_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 2, 1, 2),
    _SnmpEventID_Type()
)
snmpEventID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpEventID.setStatus("current")


class _SnmpEventDescription_Type(DisplayString):
    """Custom type snmpEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SnmpEventDescription_Type.__name__ = "DisplayString"
_SnmpEventDescription_Object = MibTableColumn
snmpEventDescription = _SnmpEventDescription_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 2, 1, 3),
    _SnmpEventDescription_Type()
)
snmpEventDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpEventDescription.setStatus("current")
_SnmpEventEvents_Type = Counter32
_SnmpEventEvents_Object = MibTableColumn
snmpEventEvents = _SnmpEventEvents_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 2, 1, 4),
    _SnmpEventEvents_Type()
)
snmpEventEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEventEvents.setStatus("current")


class _SnmpEventLastTimeSent_Type(TimeStamp):
    """Custom type snmpEventLastTimeSent based on TimeStamp"""
    defaultValue = 0


_SnmpEventLastTimeSent_Type.__name__ = "TimeStamp"
_SnmpEventLastTimeSent_Object = MibTableColumn
snmpEventLastTimeSent = _SnmpEventLastTimeSent_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 2, 1, 5),
    _SnmpEventLastTimeSent_Type()
)
snmpEventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEventLastTimeSent.setStatus("current")
_SnmpEventStatus_Type = RowStatus
_SnmpEventStatus_Object = MibTableColumn
snmpEventStatus = _SnmpEventStatus_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 2, 1, 6),
    _SnmpEventStatus_Type()
)
snmpEventStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpEventStatus.setStatus("current")
_SnmpEventNotifyMinInterval_Type = Integer32
_SnmpEventNotifyMinInterval_Object = MibScalar
snmpEventNotifyMinInterval = _SnmpEventNotifyMinInterval_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 3),
    _SnmpEventNotifyMinInterval_Type()
)
snmpEventNotifyMinInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEventNotifyMinInterval.setStatus("current")
if mibBuilder.loadTexts:
    snmpEventNotifyMinInterval.setUnits("seconds")
_SnmpEventNotifyMaxRetransmissions_Type = Integer32
_SnmpEventNotifyMaxRetransmissions_Object = MibScalar
snmpEventNotifyMaxRetransmissions = _SnmpEventNotifyMaxRetransmissions_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 4),
    _SnmpEventNotifyMaxRetransmissions_Type()
)
snmpEventNotifyMaxRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEventNotifyMaxRetransmissions.setStatus("current")
_SnmpEventNotifyTable_Object = MibTable
snmpEventNotifyTable = _SnmpEventNotifyTable_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    snmpEventNotifyTable.setStatus("current")
_SnmpEventNotifyEntry_Object = MibTableRow
snmpEventNotifyEntry = _SnmpEventNotifyEntry_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 5, 1)
)
snmpEventNotifyEntry.setIndexNames(
    (0, "SNMPv2-M2M-MIB", "snmpEventIndex"),
    (0, "SNMPv2-PARTY-MIB", "contextIdentity"),
)
if mibBuilder.loadTexts:
    snmpEventNotifyEntry.setStatus("current")


class _SnmpEventNotifyIntervalRequested_Type(Integer32):
    """Custom type snmpEventNotifyIntervalRequested based on Integer32"""
    defaultValue = 30


_SnmpEventNotifyIntervalRequested_Type.__name__ = "Integer32"
_SnmpEventNotifyIntervalRequested_Object = MibTableColumn
snmpEventNotifyIntervalRequested = _SnmpEventNotifyIntervalRequested_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 5, 1, 1),
    _SnmpEventNotifyIntervalRequested_Type()
)
snmpEventNotifyIntervalRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpEventNotifyIntervalRequested.setStatus("current")
if mibBuilder.loadTexts:
    snmpEventNotifyIntervalRequested.setUnits("seconds")


class _SnmpEventNotifyRetransmissionsRequested_Type(Integer32):
    """Custom type snmpEventNotifyRetransmissionsRequested based on Integer32"""
    defaultValue = 5


_SnmpEventNotifyRetransmissionsRequested_Type.__name__ = "Integer32"
_SnmpEventNotifyRetransmissionsRequested_Object = MibTableColumn
snmpEventNotifyRetransmissionsRequested = _SnmpEventNotifyRetransmissionsRequested_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 5, 1, 2),
    _SnmpEventNotifyRetransmissionsRequested_Type()
)
snmpEventNotifyRetransmissionsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpEventNotifyRetransmissionsRequested.setStatus("current")


class _SnmpEventNotifyLifetime_Type(Integer32):
    """Custom type snmpEventNotifyLifetime based on Integer32"""
    defaultValue = 86400


_SnmpEventNotifyLifetime_Type.__name__ = "Integer32"
_SnmpEventNotifyLifetime_Object = MibTableColumn
snmpEventNotifyLifetime = _SnmpEventNotifyLifetime_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 5, 1, 3),
    _SnmpEventNotifyLifetime_Type()
)
snmpEventNotifyLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpEventNotifyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    snmpEventNotifyLifetime.setUnits("seconds")
_SnmpEventNotifyStatus_Type = RowStatus
_SnmpEventNotifyStatus_Object = MibTableColumn
snmpEventNotifyStatus = _SnmpEventNotifyStatus_Object(
    (1, 3, 6, 1, 6, 3, 2, 1, 2, 5, 1, 4),
    _SnmpEventNotifyStatus_Type()
)
snmpEventNotifyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpEventNotifyStatus.setStatus("current")
_SnmpM2MConformance_ObjectIdentity = ObjectIdentity
snmpM2MConformance = _SnmpM2MConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 2, 2)
)
_SnmpM2MCompliances_ObjectIdentity = ObjectIdentity
snmpM2MCompliances = _SnmpM2MCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 2, 2, 1)
)
_SnmpM2MGroups_ObjectIdentity = ObjectIdentity
snmpM2MGroups = _SnmpM2MGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 2, 2, 2)
)

# Managed Objects groups

snmpAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 2, 2, 2, 1)
)
snmpAlarmGroup.setObjects(
      *(("SNMPv2-M2M-MIB", "snmpAlarmNextIndex"),
        ("SNMPv2-M2M-MIB", "snmpAlarmVariable"),
        ("SNMPv2-M2M-MIB", "snmpAlarmInterval"),
        ("SNMPv2-M2M-MIB", "snmpAlarmSampleType"),
        ("SNMPv2-M2M-MIB", "snmpAlarmValue"),
        ("SNMPv2-M2M-MIB", "snmpAlarmStartupAlarm"),
        ("SNMPv2-M2M-MIB", "snmpAlarmRisingThreshold"),
        ("SNMPv2-M2M-MIB", "snmpAlarmFallingThreshold"),
        ("SNMPv2-M2M-MIB", "snmpAlarmRisingEventIndex"),
        ("SNMPv2-M2M-MIB", "snmpAlarmFallingEventIndex"),
        ("SNMPv2-M2M-MIB", "snmpAlarmUnavailableEventIndex"),
        ("SNMPv2-M2M-MIB", "snmpAlarmStatus"))
)
if mibBuilder.loadTexts:
    snmpAlarmGroup.setStatus("current")

snmpEventGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 2, 2, 2, 2)
)
snmpEventGroup.setObjects(
      *(("SNMPv2-M2M-MIB", "snmpEventNextIndex"),
        ("SNMPv2-M2M-MIB", "snmpEventID"),
        ("SNMPv2-M2M-MIB", "snmpEventDescription"),
        ("SNMPv2-M2M-MIB", "snmpEventEvents"),
        ("SNMPv2-M2M-MIB", "snmpEventLastTimeSent"),
        ("SNMPv2-M2M-MIB", "snmpEventStatus"),
        ("SNMPv2-M2M-MIB", "snmpEventNotifyMinInterval"),
        ("SNMPv2-M2M-MIB", "snmpEventNotifyMaxRetransmissions"),
        ("SNMPv2-M2M-MIB", "snmpEventNotifyIntervalRequested"),
        ("SNMPv2-M2M-MIB", "snmpEventNotifyRetransmissionsRequested"),
        ("SNMPv2-M2M-MIB", "snmpEventNotifyLifetime"),
        ("SNMPv2-M2M-MIB", "snmpEventNotifyStatus"))
)
if mibBuilder.loadTexts:
    snmpEventGroup.setStatus("current")


# Notification objects

snmpRisingAlarm = NotificationType(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 3, 1)
)
snmpRisingAlarm.setObjects(
      *(("SNMPv2-M2M-MIB", "snmpAlarmVariable"),
        ("SNMPv2-M2M-MIB", "snmpAlarmSampleType"),
        ("SNMPv2-M2M-MIB", "snmpAlarmValue"),
        ("SNMPv2-M2M-MIB", "snmpAlarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    snmpRisingAlarm.setStatus(
        "current"
    )

snmpFallingAlarm = NotificationType(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 3, 2)
)
snmpFallingAlarm.setObjects(
      *(("SNMPv2-M2M-MIB", "snmpAlarmVariable"),
        ("SNMPv2-M2M-MIB", "snmpAlarmSampleType"),
        ("SNMPv2-M2M-MIB", "snmpAlarmValue"),
        ("SNMPv2-M2M-MIB", "snmpAlarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    snmpFallingAlarm.setStatus(
        "current"
    )

snmpObjectUnavailableAlarm = NotificationType(
    (1, 3, 6, 1, 6, 3, 2, 1, 1, 3, 3)
)
snmpObjectUnavailableAlarm.setObjects(
    ("SNMPv2-M2M-MIB", "snmpAlarmVariable")
)
if mibBuilder.loadTexts:
    snmpObjectUnavailableAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

snmpM2MCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 2, 2, 1, 1)
)
snmpM2MCompliance.setObjects(
      *(("SNMPv2-M2M-MIB", "snmpAlarmGroup"),
        ("SNMPv2-M2M-MIB", "snmpEventGroup"))
)
if mibBuilder.loadTexts:
    snmpM2MCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMPv2-M2M-MIB",
    **{"snmpM2M": snmpM2M,
       "snmpM2MObjects": snmpM2MObjects,
       "snmpAlarm": snmpAlarm,
       "snmpAlarmNextIndex": snmpAlarmNextIndex,
       "snmpAlarmTable": snmpAlarmTable,
       "snmpAlarmEntry": snmpAlarmEntry,
       "snmpAlarmIndex": snmpAlarmIndex,
       "snmpAlarmVariable": snmpAlarmVariable,
       "snmpAlarmInterval": snmpAlarmInterval,
       "snmpAlarmSampleType": snmpAlarmSampleType,
       "snmpAlarmValue": snmpAlarmValue,
       "snmpAlarmStartupAlarm": snmpAlarmStartupAlarm,
       "snmpAlarmRisingThreshold": snmpAlarmRisingThreshold,
       "snmpAlarmFallingThreshold": snmpAlarmFallingThreshold,
       "snmpAlarmRisingEventIndex": snmpAlarmRisingEventIndex,
       "snmpAlarmFallingEventIndex": snmpAlarmFallingEventIndex,
       "snmpAlarmUnavailableEventIndex": snmpAlarmUnavailableEventIndex,
       "snmpAlarmStatus": snmpAlarmStatus,
       "snmpAlarmNotifications": snmpAlarmNotifications,
       "snmpRisingAlarm": snmpRisingAlarm,
       "snmpFallingAlarm": snmpFallingAlarm,
       "snmpObjectUnavailableAlarm": snmpObjectUnavailableAlarm,
       "snmpEvent": snmpEvent,
       "snmpEventNextIndex": snmpEventNextIndex,
       "snmpEventTable": snmpEventTable,
       "snmpEventEntry": snmpEventEntry,
       "snmpEventIndex": snmpEventIndex,
       "snmpEventID": snmpEventID,
       "snmpEventDescription": snmpEventDescription,
       "snmpEventEvents": snmpEventEvents,
       "snmpEventLastTimeSent": snmpEventLastTimeSent,
       "snmpEventStatus": snmpEventStatus,
       "snmpEventNotifyMinInterval": snmpEventNotifyMinInterval,
       "snmpEventNotifyMaxRetransmissions": snmpEventNotifyMaxRetransmissions,
       "snmpEventNotifyTable": snmpEventNotifyTable,
       "snmpEventNotifyEntry": snmpEventNotifyEntry,
       "snmpEventNotifyIntervalRequested": snmpEventNotifyIntervalRequested,
       "snmpEventNotifyRetransmissionsRequested": snmpEventNotifyRetransmissionsRequested,
       "snmpEventNotifyLifetime": snmpEventNotifyLifetime,
       "snmpEventNotifyStatus": snmpEventNotifyStatus,
       "snmpM2MConformance": snmpM2MConformance,
       "snmpM2MCompliances": snmpM2MCompliances,
       "snmpM2MCompliance": snmpM2MCompliance,
       "snmpM2MGroups": snmpM2MGroups,
       "snmpAlarmGroup": snmpAlarmGroup,
       "snmpEventGroup": snmpEventGroup}
)
