# SNMP MIB module (SCTE-HMS-HE-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-COMMON-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:48 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(HeTenthCentigrade,
 heCommon) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "HeTenthCentigrade",
    "heCommon")

(scteHmsTree,) = mibBuilder.importSymbols(
    "SCTE-ROOT",
    "scteHmsTree")

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

heCommonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    heCommonMib.setRevisions(
        ("2009-11-17 14:00",
         "2009-02-13 15:14",
         "2008-01-22 10:30",
         "2005-05-26 17:30",
         "2003-02-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HeCommonTrapPrefix_ObjectIdentity = ObjectIdentity
heCommonTrapPrefix = _HeCommonTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0)
)
_HeCommonObjects_ObjectIdentity = ObjectIdentity
heCommonObjects = _HeCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1)
)
_HeCommonParams_ObjectIdentity = ObjectIdentity
heCommonParams = _HeCommonParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 1)
)
_HeCommonTable_Object = MibTable
heCommonTable = _HeCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    heCommonTable.setStatus("current")
_HeCommonEntry_Object = MibTableRow
heCommonEntry = _HeCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 1, 1, 1)
)
heCommonEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    heCommonEntry.setStatus("current")
_HeCommonTime_Type = DateAndTime
_HeCommonTime_Object = MibTableColumn
heCommonTime = _HeCommonTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 1, 1, 1, 1),
    _HeCommonTime_Type()
)
heCommonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heCommonTime.setStatus("current")
_HeCommonTemperature_Type = HeTenthCentigrade
_HeCommonTemperature_Object = MibTableColumn
heCommonTemperature = _HeCommonTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 1, 1, 1, 2),
    _HeCommonTemperature_Type()
)
heCommonTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonTemperature.setStatus("current")


class _HeCommonSoftwareReset_Type(Integer32):
    """Custom type heCommonSoftwareReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HeCommonSoftwareReset_Type.__name__ = "Integer32"
_HeCommonSoftwareReset_Object = MibTableColumn
heCommonSoftwareReset = _HeCommonSoftwareReset_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 1, 1, 1, 3),
    _HeCommonSoftwareReset_Type()
)
heCommonSoftwareReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heCommonSoftwareReset.setStatus("current")


class _HeCommonAlarmDetectionControl_Type(Integer32):
    """Custom type heCommonAlarmDetectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("detectionDisabled", 1),
          ("detectionEnabled", 2),
          ("detectionEnabledAndRegenerate", 3))
    )


_HeCommonAlarmDetectionControl_Type.__name__ = "Integer32"
_HeCommonAlarmDetectionControl_Object = MibTableColumn
heCommonAlarmDetectionControl = _HeCommonAlarmDetectionControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 1, 1, 1, 4),
    _HeCommonAlarmDetectionControl_Type()
)
heCommonAlarmDetectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heCommonAlarmDetectionControl.setStatus("current")
_HeCommonLog_ObjectIdentity = ObjectIdentity
heCommonLog = _HeCommonLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2)
)


class _HeCommonLogNumberOfEntries_Type(Integer32):
    """Custom type heCommonLogNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HeCommonLogNumberOfEntries_Type.__name__ = "Integer32"
_HeCommonLogNumberOfEntries_Object = MibScalar
heCommonLogNumberOfEntries = _HeCommonLogNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 1),
    _HeCommonLogNumberOfEntries_Type()
)
heCommonLogNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogNumberOfEntries.setStatus("current")


class _HeCommonLogLastIndex_Type(Integer32):
    """Custom type heCommonLogLastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HeCommonLogLastIndex_Type.__name__ = "Integer32"
_HeCommonLogLastIndex_Object = MibScalar
heCommonLogLastIndex = _HeCommonLogLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 2),
    _HeCommonLogLastIndex_Type()
)
heCommonLogLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogLastIndex.setStatus("current")
_HeCommonLogTable_Object = MibTable
heCommonLogTable = _HeCommonLogTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    heCommonLogTable.setStatus("current")
_HeCommonLogEntry_Object = MibTableRow
heCommonLogEntry = _HeCommonLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1)
)
heCommonLogEntry.setIndexNames(
    (0, "SCTE-HMS-HE-COMMON-MIB", "heCommonLogIndex"),
)
if mibBuilder.loadTexts:
    heCommonLogEntry.setStatus("current")


class _HeCommonLogIndex_Type(Integer32):
    """Custom type heCommonLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HeCommonLogIndex_Type.__name__ = "Integer32"
_HeCommonLogIndex_Object = MibTableColumn
heCommonLogIndex = _HeCommonLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 1),
    _HeCommonLogIndex_Type()
)
heCommonLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    heCommonLogIndex.setStatus("current")
_HeCommonLogOID_Type = ObjectIdentifier
_HeCommonLogOID_Object = MibTableColumn
heCommonLogOID = _HeCommonLogOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 2),
    _HeCommonLogOID_Type()
)
heCommonLogOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogOID.setStatus("current")


class _HeCommonLogValue_Type(Integer32):
    """Custom type heCommonLogValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_HeCommonLogValue_Type.__name__ = "Integer32"
_HeCommonLogValue_Object = MibTableColumn
heCommonLogValue = _HeCommonLogValue_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 3),
    _HeCommonLogValue_Type()
)
heCommonLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogValue.setStatus("current")


class _HeCommonLogState_Type(Integer32):
    """Custom type heCommonLogState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("heCommonNominal", 1),
          ("heCommonHIHI", 2),
          ("heCommonHI", 3),
          ("heCommonLO", 4),
          ("heCommonLOLO", 5),
          ("heCommonDiscreteMajor", 6),
          ("heCommonDiscreteMinor", 7),
          ("heCommonInformational", 8))
    )


_HeCommonLogState_Type.__name__ = "Integer32"
_HeCommonLogState_Object = MibTableColumn
heCommonLogState = _HeCommonLogState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 4),
    _HeCommonLogState_Type()
)
heCommonLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogState.setStatus("current")
_HeCommonLogTime_Type = DateAndTime
_HeCommonLogTime_Object = MibTableColumn
heCommonLogTime = _HeCommonLogTime_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 5),
    _HeCommonLogTime_Type()
)
heCommonLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogTime.setStatus("current")
_HeCommonLogText_Type = DisplayString
_HeCommonLogText_Object = MibTableColumn
heCommonLogText = _HeCommonLogText_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 6),
    _HeCommonLogText_Type()
)
heCommonLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogText.setStatus("current")
_HeCommonLogModuleIdOID_Type = ObjectIdentifier
_HeCommonLogModuleIdOID_Object = MibTableColumn
heCommonLogModuleIdOID = _HeCommonLogModuleIdOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 7),
    _HeCommonLogModuleIdOID_Type()
)
heCommonLogModuleIdOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogModuleIdOID.setStatus("current")
_HeCommonLogCardType_Type = DisplayString
_HeCommonLogCardType_Object = MibTableColumn
heCommonLogCardType = _HeCommonLogCardType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 8),
    _HeCommonLogCardType_Type()
)
heCommonLogCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogCardType.setStatus("current")
_HeCommonLogAlias_Type = DisplayString
_HeCommonLogAlias_Object = MibTableColumn
heCommonLogAlias = _HeCommonLogAlias_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 1, 2, 3, 1, 9),
    _HeCommonLogAlias_Type()
)
heCommonLogAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heCommonLogAlias.setStatus("current")
_HeCommonTraps_ObjectIdentity = ObjectIdentity
heCommonTraps = _HeCommonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 2)
)
_HeCommonConformance_ObjectIdentity = ObjectIdentity
heCommonConformance = _HeCommonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 3)
)
_HeCommonCompliances_ObjectIdentity = ObjectIdentity
heCommonCompliances = _HeCommonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 3, 1)
)
_HeCommonGroups_ObjectIdentity = ObjectIdentity
heCommonGroups = _HeCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 3, 2)
)

# Managed Objects groups

heCommonParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 3, 2, 1)
)
heCommonParamsGroup.setObjects(
      *(("SCTE-HMS-HE-COMMON-MIB", "heCommonTime"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonTemperature"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonSoftwareReset"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonAlarmDetectionControl"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogModuleIdOID"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogCardType"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogAlias"))
)
if mibBuilder.loadTexts:
    heCommonParamsGroup.setStatus("current")

heCommonLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 3, 2, 2)
)
heCommonLogGroup.setObjects(
      *(("SCTE-HMS-HE-COMMON-MIB", "heCommonLogNumberOfEntries"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogLastIndex"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogOID"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogValue"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogState"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogTime"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogText"))
)
if mibBuilder.loadTexts:
    heCommonLogGroup.setStatus("current")


# Notification objects

heCommonAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0, 5)
)
heCommonAlarmEvent.setObjects(
      *(("SCTE-HMS-HE-COMMON-MIB", "heCommonLogOID"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogValue"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogState"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogTime"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogModuleIdOID"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogCardType"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonLogAlias"))
)
if mibBuilder.loadTexts:
    heCommonAlarmEvent.setStatus(
        "current"
    )


# Notifications groups

heCommonNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 3, 2, 3)
)
heCommonNotificationsGroup.setObjects(
    ("SCTE-HMS-HE-COMMON-MIB", "heCommonAlarmEvent")
)
if mibBuilder.loadTexts:
    heCommonNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

heCommonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1, 1, 3, 1, 1)
)
heCommonCompliance.setObjects(
      *(("SCTE-HMS-HE-COMMON-MIB", "heCommonLogGroup"),
        ("SCTE-HMS-HE-COMMON-MIB", "heCommonNotificationsGroup"),
        ("ENTITY-MIB", "entityPhysicalGroup"),
        ("ENTITY-MIB", "entityPhysical2Group"),
        ("ENTITY-MIB", "entityGeneralGroup"),
        ("ENTITY-MIB", "entityNotificationsGroup"),
        ("SNMP-TARGET-MIB", "snmpTargetBasicGroup"),
        ("SNMP-NOTIFICATION-MIB", "snmpNotifyGroup"),
        ("SNMPv2-MIB", "systemGroup"),
        ("SCTE-HMS-PROPERTY-MIB", "analogAlarmsGroup"),
        ("SCTE-HMS-PROPERTY-MIB", "discreteAlarmsGroup"),
        ("SCTE-HMS-PROPERTY-MIB", "currentAlarmsGroup"))
)
if mibBuilder.loadTexts:
    heCommonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-COMMON-MIB",
    **{"heCommonTrapPrefix": heCommonTrapPrefix,
       "heCommonAlarmEvent": heCommonAlarmEvent,
       "heCommonMib": heCommonMib,
       "heCommonObjects": heCommonObjects,
       "heCommonParams": heCommonParams,
       "heCommonTable": heCommonTable,
       "heCommonEntry": heCommonEntry,
       "heCommonTime": heCommonTime,
       "heCommonTemperature": heCommonTemperature,
       "heCommonSoftwareReset": heCommonSoftwareReset,
       "heCommonAlarmDetectionControl": heCommonAlarmDetectionControl,
       "heCommonLog": heCommonLog,
       "heCommonLogNumberOfEntries": heCommonLogNumberOfEntries,
       "heCommonLogLastIndex": heCommonLogLastIndex,
       "heCommonLogTable": heCommonLogTable,
       "heCommonLogEntry": heCommonLogEntry,
       "heCommonLogIndex": heCommonLogIndex,
       "heCommonLogOID": heCommonLogOID,
       "heCommonLogValue": heCommonLogValue,
       "heCommonLogState": heCommonLogState,
       "heCommonLogTime": heCommonLogTime,
       "heCommonLogText": heCommonLogText,
       "heCommonLogModuleIdOID": heCommonLogModuleIdOID,
       "heCommonLogCardType": heCommonLogCardType,
       "heCommonLogAlias": heCommonLogAlias,
       "heCommonTraps": heCommonTraps,
       "heCommonConformance": heCommonConformance,
       "heCommonCompliances": heCommonCompliances,
       "heCommonCompliance": heCommonCompliance,
       "heCommonGroups": heCommonGroups,
       "heCommonParamsGroup": heCommonParamsGroup,
       "heCommonLogGroup": heCommonLogGroup,
       "heCommonNotificationsGroup": heCommonNotificationsGroup}
)
