# SNMP MIB module (EXFO-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exfo_6718/EXFO-ALARM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:54:13 2025
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

(eventAddInformIdentifier,
 eventAddInformSignificance,
 eventAddInformValueInteger,
 eventAddInformValueString,
 eventAddInformValueType,
 eventAdditionalText,
 eventAttrIdAttributeId,
 eventAttrValueChangeDefAttributeId,
 eventAttrValueChangeDefAttributeValueType,
 eventAttrValueChangeDefNewAttributeValueInteger,
 eventAttrValueChangeDefNewAttributeValueString,
 eventAttrValueChangeDefOldAttributeValueInteger,
 eventAttrValueChangeDefOldAttributeValueString,
 eventCorrNotifNotificationIdentifier,
 eventCorrNotifSourceObjectInst,
 eventManagedObjectInstance,
 eventNotificationIdentifier,
 eventTime) = mibBuilder.importSymbols(
    "EXFO-EVENT-MIB",
    "eventAddInformIdentifier",
    "eventAddInformSignificance",
    "eventAddInformValueInteger",
    "eventAddInformValueString",
    "eventAddInformValueType",
    "eventAdditionalText",
    "eventAttrIdAttributeId",
    "eventAttrValueChangeDefAttributeId",
    "eventAttrValueChangeDefAttributeValueType",
    "eventAttrValueChangeDefNewAttributeValueInteger",
    "eventAttrValueChangeDefNewAttributeValueString",
    "eventAttrValueChangeDefOldAttributeValueInteger",
    "eventAttrValueChangeDefOldAttributeValueString",
    "eventCorrNotifNotificationIdentifier",
    "eventCorrNotifSourceObjectInst",
    "eventManagedObjectInstance",
    "eventNotificationIdentifier",
    "eventTime")

(exfoCommonMib,
 exfoModules) = mibBuilder.importSymbols(
    "EXFO-SMI-REG",
    "exfoCommonMib",
    "exfoModules")

(AdministrativeState,
 ExfoRealValue,
 ExfoSnmpType,
 OperationalState) = mibBuilder.importSymbols(
    "EXFO-TC",
    "AdministrativeState",
    "ExfoRealValue",
    "ExfoSnmpType",
    "OperationalState")

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

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

exfoAlarmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1, 5)
)
if mibBuilder.loadTexts:
    exfoAlarmMib.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmPerceivedSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("cleared", 5))
    )



class AlarmTrendIndication(TextualConvention, Integer32):
    status = "current"
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
        *(("lessSevere", 0),
          ("noChange", 1),
          ("moreSevere", 2),
          ("notSpecify", 3))
    )



class ProbableCause(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              29,
              46,
              51,
              1000,
              1001)
        )
    )
    namedValues = NamedValues(
        *(("degradedSignal", 12),
          ("lossOfSignal", 29),
          ("softwareError", 46),
          ("thresholdCrossed", 51),
          ("commonFiberFault", 1000),
          ("lossOfChannel", 1001))
    )



# MIB Managed Objects in the order of their OIDs

_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2)
)
if mibBuilder.loadTexts:
    alarm.setStatus("current")
_AlarmConf_ObjectIdentity = ObjectIdentity
alarmConf = _AlarmConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alarmConf.setStatus("current")
_AlarmGroups_ObjectIdentity = ObjectIdentity
alarmGroups = _AlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alarmGroups.setStatus("current")
_AlarmCompls_ObjectIdentity = ObjectIdentity
alarmCompls = _AlarmCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alarmCompls.setStatus("current")
_AlarmObjs_ObjectIdentity = ObjectIdentity
alarmObjs = _AlarmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2)
)
if mibBuilder.loadTexts:
    alarmObjs.setStatus("current")
_AlarmNumber_Type = Unsigned32
_AlarmNumber_Object = MibScalar
alarmNumber = _AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 1),
    _AlarmNumber_Type()
)
alarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNumber.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1)
)
alarmEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
_AlarmIndex_Type = Unsigned32
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmProbableCause_Type = ProbableCause
_AlarmProbableCause_Object = MibTableColumn
alarmProbableCause = _AlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 2),
    _AlarmProbableCause_Type()
)
alarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProbableCause.setStatus("current")
_AlarmPerceivedSeverity_Type = AlarmPerceivedSeverity
_AlarmPerceivedSeverity_Object = MibTableColumn
alarmPerceivedSeverity = _AlarmPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 3),
    _AlarmPerceivedSeverity_Type()
)
alarmPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPerceivedSeverity.setStatus("current")
_AlarmProposedRepairActions_Type = DisplayString
_AlarmProposedRepairActions_Object = MibTableColumn
alarmProposedRepairActions = _AlarmProposedRepairActions_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 4),
    _AlarmProposedRepairActions_Type()
)
alarmProposedRepairActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmProposedRepairActions.setStatus("current")
_AlarmAdditionalText_Type = DisplayString
_AlarmAdditionalText_Object = MibTableColumn
alarmAdditionalText = _AlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 5),
    _AlarmAdditionalText_Type()
)
alarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAdditionalText.setStatus("current")
_AlarmUpdateTime_Type = DateAndTime
_AlarmUpdateTime_Object = MibTableColumn
alarmUpdateTime = _AlarmUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 6),
    _AlarmUpdateTime_Type()
)
alarmUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUpdateTime.setStatus("current")
_AlarmAdministrativeState_Type = AdministrativeState
_AlarmAdministrativeState_Object = MibTableColumn
alarmAdministrativeState = _AlarmAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 7),
    _AlarmAdministrativeState_Type()
)
alarmAdministrativeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAdministrativeState.setStatus("current")
_AlarmOperationalState_Type = OperationalState
_AlarmOperationalState_Object = MibTableColumn
alarmOperationalState = _AlarmOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 8),
    _AlarmOperationalState_Type()
)
alarmOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmOperationalState.setStatus("current")
_AlarmBackedUpStatus_Type = TruthValue
_AlarmBackedUpStatus_Object = MibTableColumn
alarmBackedUpStatus = _AlarmBackedUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 9),
    _AlarmBackedUpStatus_Type()
)
alarmBackedUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBackedUpStatus.setStatus("current")
_AlarmBackUpObject_Type = VariablePointer
_AlarmBackUpObject_Object = MibTableColumn
alarmBackUpObject = _AlarmBackUpObject_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 10),
    _AlarmBackUpObject_Type()
)
alarmBackUpObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBackUpObject.setStatus("current")
_AlarmTrendIndication_Type = AlarmTrendIndication
_AlarmTrendIndication_Object = MibTableColumn
alarmTrendIndication = _AlarmTrendIndication_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 11),
    _AlarmTrendIndication_Type()
)
alarmTrendIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTrendIndication.setStatus("current")
_AlarmTriggeredThreshold_Type = AutonomousType
_AlarmTriggeredThreshold_Object = MibTableColumn
alarmTriggeredThreshold = _AlarmTriggeredThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 12),
    _AlarmTriggeredThreshold_Type()
)
alarmTriggeredThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTriggeredThreshold.setStatus("current")
_AlarmObservedValue_Type = ExfoRealValue
_AlarmObservedValue_Object = MibTableColumn
alarmObservedValue = _AlarmObservedValue_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 13),
    _AlarmObservedValue_Type()
)
alarmObservedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmObservedValue.setStatus("current")
_AlarmThresholdLevelChoice_Type = Integer32
_AlarmThresholdLevelChoice_Object = MibTableColumn
alarmThresholdLevelChoice = _AlarmThresholdLevelChoice_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 14),
    _AlarmThresholdLevelChoice_Type()
)
alarmThresholdLevelChoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmThresholdLevelChoice.setStatus("current")
_AlarmThresholdLevelHigh_Type = ExfoRealValue
_AlarmThresholdLevelHigh_Object = MibTableColumn
alarmThresholdLevelHigh = _AlarmThresholdLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 15),
    _AlarmThresholdLevelHigh_Type()
)
alarmThresholdLevelHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmThresholdLevelHigh.setStatus("current")
_AlarmThresholdLevelLow_Type = ExfoRealValue
_AlarmThresholdLevelLow_Object = MibTableColumn
alarmThresholdLevelLow = _AlarmThresholdLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 16),
    _AlarmThresholdLevelLow_Type()
)
alarmThresholdLevelLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmThresholdLevelLow.setStatus("current")
_AlarmId_Type = Unsigned32
_AlarmId_Object = MibTableColumn
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 2, 1, 17),
    _AlarmId_Type()
)
alarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")
_AlarmSpecificProblemsTable_Object = MibTable
alarmSpecificProblemsTable = _AlarmSpecificProblemsTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    alarmSpecificProblemsTable.setStatus("current")
_AlarmSpecificProblemsEntry_Object = MibTableRow
alarmSpecificProblemsEntry = _AlarmSpecificProblemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 3, 1)
)
alarmSpecificProblemsEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
    (0, "EXFO-ALARM-MIB", "alarmSpecificProblemsIndex"),
)
if mibBuilder.loadTexts:
    alarmSpecificProblemsEntry.setStatus("current")
_AlarmSpecificProblemsIndex_Type = Unsigned32
_AlarmSpecificProblemsIndex_Object = MibTableColumn
alarmSpecificProblemsIndex = _AlarmSpecificProblemsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 3, 1, 1),
    _AlarmSpecificProblemsIndex_Type()
)
alarmSpecificProblemsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmSpecificProblemsIndex.setStatus("current")
_AlarmSpecificProblemsIdentifier_Type = AutonomousType
_AlarmSpecificProblemsIdentifier_Object = MibTableColumn
alarmSpecificProblemsIdentifier = _AlarmSpecificProblemsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 3, 1, 2),
    _AlarmSpecificProblemsIdentifier_Type()
)
alarmSpecificProblemsIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSpecificProblemsIdentifier.setStatus("current")
_AlarmMonitoredAttributesTable_Object = MibTable
alarmMonitoredAttributesTable = _AlarmMonitoredAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    alarmMonitoredAttributesTable.setStatus("current")
_AlarmMonitoredAttributesEntry_Object = MibTableRow
alarmMonitoredAttributesEntry = _AlarmMonitoredAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 4, 1)
)
alarmMonitoredAttributesEntry.setIndexNames(
    (0, "EXFO-ALARM-MIB", "alarmIndex"),
    (0, "EXFO-ALARM-MIB", "alarmMonitoredAttributesIndex"),
)
if mibBuilder.loadTexts:
    alarmMonitoredAttributesEntry.setStatus("current")
_AlarmMonitoredAttributesIndex_Type = Unsigned32
_AlarmMonitoredAttributesIndex_Object = MibTableColumn
alarmMonitoredAttributesIndex = _AlarmMonitoredAttributesIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 4, 1, 1),
    _AlarmMonitoredAttributesIndex_Type()
)
alarmMonitoredAttributesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmMonitoredAttributesIndex.setStatus("current")
_AlarmMonitoredAttributesIdentifier_Type = AutonomousType
_AlarmMonitoredAttributesIdentifier_Object = MibTableColumn
alarmMonitoredAttributesIdentifier = _AlarmMonitoredAttributesIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 4, 1, 2),
    _AlarmMonitoredAttributesIdentifier_Type()
)
alarmMonitoredAttributesIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMonitoredAttributesIdentifier.setStatus("current")
_AlarmMonitoredAttributesValueType_Type = ExfoSnmpType
_AlarmMonitoredAttributesValueType_Object = MibTableColumn
alarmMonitoredAttributesValueType = _AlarmMonitoredAttributesValueType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 4, 1, 3),
    _AlarmMonitoredAttributesValueType_Type()
)
alarmMonitoredAttributesValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMonitoredAttributesValueType.setStatus("current")
_AlarmMonitoredAttributesValueInteger_Type = Integer32
_AlarmMonitoredAttributesValueInteger_Object = MibTableColumn
alarmMonitoredAttributesValueInteger = _AlarmMonitoredAttributesValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 4, 1, 4),
    _AlarmMonitoredAttributesValueInteger_Type()
)
alarmMonitoredAttributesValueInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMonitoredAttributesValueInteger.setStatus("current")


class _AlarmMonitoredAttributesValueString_Type(OctetString):
    """Custom type alarmMonitoredAttributesValueString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AlarmMonitoredAttributesValueString_Type.__name__ = "OctetString"
_AlarmMonitoredAttributesValueString_Object = MibTableColumn
alarmMonitoredAttributesValueString = _AlarmMonitoredAttributesValueString_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 2, 4, 1, 5),
    _AlarmMonitoredAttributesValueString_Type()
)
alarmMonitoredAttributesValueString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmMonitoredAttributesValueString.setStatus("current")
_AlarmEvents_ObjectIdentity = ObjectIdentity
alarmEvents = _AlarmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 3)
)
if mibBuilder.loadTexts:
    alarmEvents.setStatus("current")

# Managed Objects groups

alarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 1, 1, 1)
)
alarmGroup.setObjects(
      *(("EXFO-ALARM-MIB", "alarmNumber"),
        ("EXFO-ALARM-MIB", "alarmId"),
        ("EXFO-ALARM-MIB", "alarmProbableCause"),
        ("EXFO-ALARM-MIB", "alarmPerceivedSeverity"),
        ("EXFO-ALARM-MIB", "alarmProposedRepairActions"),
        ("EXFO-ALARM-MIB", "alarmAdditionalText"),
        ("EXFO-ALARM-MIB", "alarmUpdateTime"),
        ("EXFO-ALARM-MIB", "alarmAdministrativeState"),
        ("EXFO-ALARM-MIB", "alarmOperationalState"),
        ("EXFO-ALARM-MIB", "alarmBackedUpStatus"),
        ("EXFO-ALARM-MIB", "alarmBackUpObject"),
        ("EXFO-ALARM-MIB", "alarmTrendIndication"),
        ("EXFO-ALARM-MIB", "alarmTriggeredThreshold"),
        ("EXFO-ALARM-MIB", "alarmObservedValue"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelChoice"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelHigh"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelLow"),
        ("EXFO-ALARM-MIB", "alarmSpecificProblemsIdentifier"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesIdentifier"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueType"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueInteger"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueString"))
)
if mibBuilder.loadTexts:
    alarmGroup.setStatus("current")


# Notification objects

qualityOfServiceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 3, 1)
)
qualityOfServiceAlarm.setObjects(
      *(("EXFO-EVENT-MIB", "eventManagedObjectInstance"),
        ("EXFO-EVENT-MIB", "eventTime"),
        ("EXFO-ALARM-MIB", "alarmProbableCause"),
        ("EXFO-ALARM-MIB", "alarmSpecificProblemsIdentifier"),
        ("EXFO-ALARM-MIB", "alarmPerceivedSeverity"),
        ("EXFO-ALARM-MIB", "alarmBackedUpStatus"),
        ("EXFO-ALARM-MIB", "alarmBackUpObject"),
        ("EXFO-ALARM-MIB", "alarmTrendIndication"),
        ("EXFO-ALARM-MIB", "alarmTriggeredThreshold"),
        ("EXFO-ALARM-MIB", "alarmObservedValue"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelChoice"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelHigh"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelLow"),
        ("EXFO-EVENT-MIB", "eventNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventCorrNotifSourceObjectInst"),
        ("EXFO-EVENT-MIB", "eventCorrNotifNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventAttrIdAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefAttributeValueType"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefOldAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefOldAttributeValueString"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefNewAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefNewAttributeValueString"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesIdentifier"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueType"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueInteger"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueString"),
        ("EXFO-ALARM-MIB", "alarmProposedRepairActions"),
        ("EXFO-EVENT-MIB", "eventAdditionalText"),
        ("EXFO-EVENT-MIB", "eventAddInformIdentifier"),
        ("EXFO-EVENT-MIB", "eventAddInformSignificance"),
        ("EXFO-EVENT-MIB", "eventAddInformValueType"),
        ("EXFO-EVENT-MIB", "eventAddInformValueInteger"),
        ("EXFO-EVENT-MIB", "eventAddInformValueString"))
)
if mibBuilder.loadTexts:
    qualityOfServiceAlarm.setStatus(
        "current"
    )

processingErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 3, 2)
)
processingErrorAlarm.setObjects(
      *(("EXFO-EVENT-MIB", "eventManagedObjectInstance"),
        ("EXFO-EVENT-MIB", "eventTime"),
        ("EXFO-ALARM-MIB", "alarmProbableCause"),
        ("EXFO-ALARM-MIB", "alarmSpecificProblemsIdentifier"),
        ("EXFO-ALARM-MIB", "alarmPerceivedSeverity"),
        ("EXFO-ALARM-MIB", "alarmBackedUpStatus"),
        ("EXFO-ALARM-MIB", "alarmBackUpObject"),
        ("EXFO-ALARM-MIB", "alarmTrendIndication"),
        ("EXFO-ALARM-MIB", "alarmTriggeredThreshold"),
        ("EXFO-ALARM-MIB", "alarmObservedValue"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelChoice"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelHigh"),
        ("EXFO-ALARM-MIB", "alarmThresholdLevelLow"),
        ("EXFO-EVENT-MIB", "eventNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventCorrNotifSourceObjectInst"),
        ("EXFO-EVENT-MIB", "eventCorrNotifNotificationIdentifier"),
        ("EXFO-EVENT-MIB", "eventAttrIdAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefAttributeId"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefAttributeValueType"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefOldAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefOldAttributeValueString"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefNewAttributeValueInteger"),
        ("EXFO-EVENT-MIB", "eventAttrValueChangeDefNewAttributeValueString"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesIdentifier"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueType"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueInteger"),
        ("EXFO-ALARM-MIB", "alarmMonitoredAttributesValueString"),
        ("EXFO-ALARM-MIB", "alarmProposedRepairActions"),
        ("EXFO-EVENT-MIB", "eventAdditionalText"),
        ("EXFO-EVENT-MIB", "eventAddInformIdentifier"),
        ("EXFO-EVENT-MIB", "eventAddInformSignificance"),
        ("EXFO-EVENT-MIB", "eventAddInformValueType"),
        ("EXFO-EVENT-MIB", "eventAddInformValueInteger"),
        ("EXFO-EVENT-MIB", "eventAddInformValueString"))
)
if mibBuilder.loadTexts:
    processingErrorAlarm.setStatus(
        "current"
    )


# Notifications groups

alarmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 1, 1, 2)
)
alarmNotificationGroup.setObjects(
      *(("EXFO-ALARM-MIB", "qualityOfServiceAlarm"),
        ("EXFO-ALARM-MIB", "processingErrorAlarm"))
)
if mibBuilder.loadTexts:
    alarmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alarmAdvancedCompls = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6718, 2, 2, 1, 2, 1)
)
alarmAdvancedCompls.setObjects(
      *(("EXFO-ALARM-MIB", "alarmGroup"),
        ("EXFO-ALARM-MIB", "alarmNotificationGroup"))
)
if mibBuilder.loadTexts:
    alarmAdvancedCompls.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXFO-ALARM-MIB",
    **{"AlarmPerceivedSeverity": AlarmPerceivedSeverity,
       "AlarmTrendIndication": AlarmTrendIndication,
       "ProbableCause": ProbableCause,
       "exfoAlarmMib": exfoAlarmMib,
       "alarm": alarm,
       "alarmConf": alarmConf,
       "alarmGroups": alarmGroups,
       "alarmGroup": alarmGroup,
       "alarmNotificationGroup": alarmNotificationGroup,
       "alarmCompls": alarmCompls,
       "alarmAdvancedCompls": alarmAdvancedCompls,
       "alarmObjs": alarmObjs,
       "alarmNumber": alarmNumber,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmProbableCause": alarmProbableCause,
       "alarmPerceivedSeverity": alarmPerceivedSeverity,
       "alarmProposedRepairActions": alarmProposedRepairActions,
       "alarmAdditionalText": alarmAdditionalText,
       "alarmUpdateTime": alarmUpdateTime,
       "alarmAdministrativeState": alarmAdministrativeState,
       "alarmOperationalState": alarmOperationalState,
       "alarmBackedUpStatus": alarmBackedUpStatus,
       "alarmBackUpObject": alarmBackUpObject,
       "alarmTrendIndication": alarmTrendIndication,
       "alarmTriggeredThreshold": alarmTriggeredThreshold,
       "alarmObservedValue": alarmObservedValue,
       "alarmThresholdLevelChoice": alarmThresholdLevelChoice,
       "alarmThresholdLevelHigh": alarmThresholdLevelHigh,
       "alarmThresholdLevelLow": alarmThresholdLevelLow,
       "alarmId": alarmId,
       "alarmSpecificProblemsTable": alarmSpecificProblemsTable,
       "alarmSpecificProblemsEntry": alarmSpecificProblemsEntry,
       "alarmSpecificProblemsIndex": alarmSpecificProblemsIndex,
       "alarmSpecificProblemsIdentifier": alarmSpecificProblemsIdentifier,
       "alarmMonitoredAttributesTable": alarmMonitoredAttributesTable,
       "alarmMonitoredAttributesEntry": alarmMonitoredAttributesEntry,
       "alarmMonitoredAttributesIndex": alarmMonitoredAttributesIndex,
       "alarmMonitoredAttributesIdentifier": alarmMonitoredAttributesIdentifier,
       "alarmMonitoredAttributesValueType": alarmMonitoredAttributesValueType,
       "alarmMonitoredAttributesValueInteger": alarmMonitoredAttributesValueInteger,
       "alarmMonitoredAttributesValueString": alarmMonitoredAttributesValueString,
       "alarmEvents": alarmEvents,
       "qualityOfServiceAlarm": qualityOfServiceAlarm,
       "processingErrorAlarm": processingErrorAlarm}
)
