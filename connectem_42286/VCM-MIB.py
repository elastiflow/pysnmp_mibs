# SNMP MIB module (VCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/connectem_42286/VCM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:57:02 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

vcmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42286)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vcm_ObjectIdentity = ObjectIdentity
vcm = _Vcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 1)
)
_ConfSection1_ObjectIdentity = ObjectIdentity
confSection1 = _ConfSection1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 1, 1)
)
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 2)
)
_CountersSection1_ObjectIdentity = ObjectIdentity
countersSection1 = _CountersSection1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 2, 1)
)
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3)
)
_VcmNtfCommonParams_ObjectIdentity = ObjectIdentity
vcmNtfCommonParams = _VcmNtfCommonParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1)
)
_VcmEventType_Type = Integer32
_VcmEventType_Object = MibScalar
vcmEventType = _VcmEventType_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 1),
    _VcmEventType_Type()
)
vcmEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcmEventType.setStatus("current")
_VcmNotificationObject_Type = OctetString
_VcmNotificationObject_Object = MibScalar
vcmNotificationObject = _VcmNotificationObject_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 2),
    _VcmNotificationObject_Type()
)
vcmNotificationObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcmNotificationObject.setStatus("current")
_VcmNotifyingObject_Type = OctetString
_VcmNotifyingObject_Object = MibScalar
vcmNotifyingObject = _VcmNotifyingObject_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 3),
    _VcmNotifyingObject_Type()
)
vcmNotifyingObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcmNotifyingObject.setStatus("current")
_VcmEventTime_Type = TimeTicks
_VcmEventTime_Object = MibScalar
vcmEventTime = _VcmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 4),
    _VcmEventTime_Type()
)
vcmEventTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcmEventTime.setStatus("current")
_VcmNotificationClassIdentifier_Type = OctetString
_VcmNotificationClassIdentifier_Object = MibScalar
vcmNotificationClassIdentifier = _VcmNotificationClassIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 5),
    _VcmNotificationClassIdentifier_Type()
)
vcmNotificationClassIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmNotificationClassIdentifier.setStatus("current")
_VcmNotificationIdentifier_Type = Unsigned32
_VcmNotificationIdentifier_Object = MibScalar
vcmNotificationIdentifier = _VcmNotificationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 6),
    _VcmNotificationIdentifier_Type()
)
vcmNotificationIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmNotificationIdentifier.setStatus("current")
_VcmCorrelatedNotifications_Type = OctetString
_VcmCorrelatedNotifications_Object = MibScalar
vcmCorrelatedNotifications = _VcmCorrelatedNotifications_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 7),
    _VcmCorrelatedNotifications_Type()
)
vcmCorrelatedNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmCorrelatedNotifications.setStatus("current")
_VcmAdditionalText_Type = OctetString
_VcmAdditionalText_Object = MibScalar
vcmAdditionalText = _VcmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 8),
    _VcmAdditionalText_Type()
)
vcmAdditionalText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcmAdditionalText.setStatus("current")
_VcmAdditionalInformation_Type = OctetString
_VcmAdditionalInformation_Object = MibScalar
vcmAdditionalInformation = _VcmAdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 1, 9),
    _VcmAdditionalInformation_Type()
)
vcmAdditionalInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmAdditionalInformation.setStatus("current")
_VcmNotificationType_ObjectIdentity = ObjectIdentity
vcmNotificationType = _VcmNotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2)
)
_VcmObjectCreateDelete_ObjectIdentity = ObjectIdentity
vcmObjectCreateDelete = _VcmObjectCreateDelete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 1)
)
_VcmSourceIndicatorForObjectCreateDelete_Type = Integer32
_VcmSourceIndicatorForObjectCreateDelete_Object = MibScalar
vcmSourceIndicatorForObjectCreateDelete = _VcmSourceIndicatorForObjectCreateDelete_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 1, 1),
    _VcmSourceIndicatorForObjectCreateDelete_Type()
)
vcmSourceIndicatorForObjectCreateDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmSourceIndicatorForObjectCreateDelete.setStatus("current")
_VcmAttributeList_Type = OctetString
_VcmAttributeList_Object = MibScalar
vcmAttributeList = _VcmAttributeList_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 1, 2),
    _VcmAttributeList_Type()
)
vcmAttributeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmAttributeList.setStatus("current")
_VcmAttributeChange_ObjectIdentity = ObjectIdentity
vcmAttributeChange = _VcmAttributeChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 2)
)
_VcmSourceIndicatorForAttributeChange_Type = Integer32
_VcmSourceIndicatorForAttributeChange_Object = MibScalar
vcmSourceIndicatorForAttributeChange = _VcmSourceIndicatorForAttributeChange_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 2, 1),
    _VcmSourceIndicatorForAttributeChange_Type()
)
vcmSourceIndicatorForAttributeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmSourceIndicatorForAttributeChange.setStatus("current")
_VcmChangedAttributeList_Type = OctetString
_VcmChangedAttributeList_Object = MibScalar
vcmChangedAttributeList = _VcmChangedAttributeList_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 2, 2),
    _VcmChangedAttributeList_Type()
)
vcmChangedAttributeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmChangedAttributeList.setStatus("current")
_VcmStateChange_ObjectIdentity = ObjectIdentity
vcmStateChange = _VcmStateChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 3)
)
_VcmSourceIndicatorForStateChange_Type = Integer32
_VcmSourceIndicatorForStateChange_Object = MibScalar
vcmSourceIndicatorForStateChange = _VcmSourceIndicatorForStateChange_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 3, 1),
    _VcmSourceIndicatorForStateChange_Type()
)
vcmSourceIndicatorForStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmSourceIndicatorForStateChange.setStatus("current")
_VcmChangedStateAttributeList_Type = OctetString
_VcmChangedStateAttributeList_Object = MibScalar
vcmChangedStateAttributeList = _VcmChangedStateAttributeList_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 3, 2),
    _VcmChangedStateAttributeList_Type()
)
vcmChangedStateAttributeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmChangedStateAttributeList.setStatus("current")
_VcmAlarm_ObjectIdentity = ObjectIdentity
vcmAlarm = _VcmAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 4)
)
_VcmAlarmProbableCause_Type = Integer32
_VcmAlarmProbableCause_Object = MibScalar
vcmAlarmProbableCause = _VcmAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 4, 1),
    _VcmAlarmProbableCause_Type()
)
vcmAlarmProbableCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcmAlarmProbableCause.setStatus("current")
_VcmSpecificProblems_Type = OctetString
_VcmSpecificProblems_Object = MibScalar
vcmSpecificProblems = _VcmSpecificProblems_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 4, 2),
    _VcmSpecificProblems_Type()
)
vcmSpecificProblems.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcmSpecificProblems.setStatus("current")
_VcmAlarmSeverity_Type = Integer32
_VcmAlarmSeverity_Object = MibScalar
vcmAlarmSeverity = _VcmAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 4, 3),
    _VcmAlarmSeverity_Type()
)
vcmAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcmAlarmSeverity.setStatus("current")
_VcmTrendIndication_Type = Integer32
_VcmTrendIndication_Object = MibScalar
vcmTrendIndication = _VcmTrendIndication_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 4, 4),
    _VcmTrendIndication_Type()
)
vcmTrendIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmTrendIndication.setStatus("current")
_VcmThresholdInformation_Type = OctetString
_VcmThresholdInformation_Object = MibScalar
vcmThresholdInformation = _VcmThresholdInformation_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 4, 5),
    _VcmThresholdInformation_Type()
)
vcmThresholdInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmThresholdInformation.setStatus("current")
_VcmMonitoredAttributes_Type = OctetString
_VcmMonitoredAttributes_Object = MibScalar
vcmMonitoredAttributes = _VcmMonitoredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 4, 6),
    _VcmMonitoredAttributes_Type()
)
vcmMonitoredAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmMonitoredAttributes.setStatus("current")
_VcmProposedRepairActions_Type = OctetString
_VcmProposedRepairActions_Object = MibScalar
vcmProposedRepairActions = _VcmProposedRepairActions_Object(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 2, 4, 7),
    _VcmProposedRepairActions_Type()
)
vcmProposedRepairActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcmProposedRepairActions.setStatus("current")

# Managed Objects groups


# Notification objects

vcmTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 42286, 1, 3, 3)
)
vcmTraps.setObjects(
      *(("VCM-MIB", "vcmEventType"),
        ("VCM-MIB", "vcmNotificationObject"),
        ("VCM-MIB", "vcmNotifyingObject"),
        ("VCM-MIB", "vcmEventTime"),
        ("VCM-MIB", "vcmAlarmProbableCause"),
        ("VCM-MIB", "vcmAdditionalText"),
        ("VCM-MIB", "vcmAlarmSeverity"),
        ("VCM-MIB", "vcmSpecificProblems"))
)
if mibBuilder.loadTexts:
    vcmTraps.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VCM-MIB",
    **{"vcmMIB": vcmMIB,
       "vcm": vcm,
       "configuration": configuration,
       "confSection1": confSection1,
       "performance": performance,
       "countersSection1": countersSection1,
       "fault": fault,
       "vcmNtfCommonParams": vcmNtfCommonParams,
       "vcmEventType": vcmEventType,
       "vcmNotificationObject": vcmNotificationObject,
       "vcmNotifyingObject": vcmNotifyingObject,
       "vcmEventTime": vcmEventTime,
       "vcmNotificationClassIdentifier": vcmNotificationClassIdentifier,
       "vcmNotificationIdentifier": vcmNotificationIdentifier,
       "vcmCorrelatedNotifications": vcmCorrelatedNotifications,
       "vcmAdditionalText": vcmAdditionalText,
       "vcmAdditionalInformation": vcmAdditionalInformation,
       "vcmNotificationType": vcmNotificationType,
       "vcmObjectCreateDelete": vcmObjectCreateDelete,
       "vcmSourceIndicatorForObjectCreateDelete": vcmSourceIndicatorForObjectCreateDelete,
       "vcmAttributeList": vcmAttributeList,
       "vcmAttributeChange": vcmAttributeChange,
       "vcmSourceIndicatorForAttributeChange": vcmSourceIndicatorForAttributeChange,
       "vcmChangedAttributeList": vcmChangedAttributeList,
       "vcmStateChange": vcmStateChange,
       "vcmSourceIndicatorForStateChange": vcmSourceIndicatorForStateChange,
       "vcmChangedStateAttributeList": vcmChangedStateAttributeList,
       "vcmAlarm": vcmAlarm,
       "vcmAlarmProbableCause": vcmAlarmProbableCause,
       "vcmSpecificProblems": vcmSpecificProblems,
       "vcmAlarmSeverity": vcmAlarmSeverity,
       "vcmTrendIndication": vcmTrendIndication,
       "vcmThresholdInformation": vcmThresholdInformation,
       "vcmMonitoredAttributes": vcmMonitoredAttributes,
       "vcmProposedRepairActions": vcmProposedRepairActions,
       "vcmTraps": vcmTraps}
)
