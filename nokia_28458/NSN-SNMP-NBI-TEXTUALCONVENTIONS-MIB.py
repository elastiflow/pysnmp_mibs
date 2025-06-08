# SNMP MIB module (NSN-SNMP-NBI-TEXTUALCONVENTIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_28458/NSN-SNMP-NBI-TEXTUALCONVENTIONS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:24:52 2025
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

(nbiNetActSnmp,) = mibBuilder.importSymbols(
    "NSN-SNMP-NBI-REGISTRATION-MIB",
    "nbiNetActSnmp")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(LongUtf8String,
 Utf8String) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "LongUtf8String",
    "Utf8String")


# MODULE-IDENTITY

nbiTextualConventionsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28458, 1, 26, 1)
)
if mibBuilder.loadTexts:
    nbiTextualConventionsMIB.setRevisions(
        ("2011-01-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NbiActiveInterfaceVersion(SnmpAdminString):
    status = "current"


class NbiChangedPeriodType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmSummary", 1),
          ("heartbeat", 2))
    )



class NbiEmsSynchronizationState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sync", 1),
          ("partialSync", 2),
          ("noSync", 3))
    )



class NbiDateAndTime(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class NbiEventTime(DateAndTime):
    status = "current"


class NbiEventTypeFilter(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("filterAll", 0),
          ("noEventTypeFilter", 1),
          ("filterCommunicationsAlarm", 2),
          ("filterQualityOfServiceAlarm", 3),
          ("filterProcessingErrorAlarm", 4),
          ("filterEquipmentAlarm", 5),
          ("filterEnvironmentalAlarm", 6),
          ("filterIntegrityViolationAlarm", 7),
          ("filterOperationalViolationAlarm", 8),
          ("filterPhysicalViolationAlarm", 9),
          ("filterSecurityServiceOrMechanismViolationAlarm", 10),
          ("filterTimeDomainViolationAlarm", 11),
          ("filterCreateNotification", 12),
          ("filterDeleteNotification", 13),
          ("filterAVCNotification", 14),
          ("filterStateChangeNotification", 15),
          ("filterAlarmSyncNotification", 16),
          ("filterSyncEMSDataNotification", 17),
          ("filterSyncNEDataNotification", 18),
          ("filterAlarmSummaryNotification", 19),
          ("filterHeartbeatNotification", 20),
          ("filterEndOfSequenceNotification", 21),
          ("filterChangedPeriodNotification", 22),
          ("filterStartUpNotification", 23),
          ("filterShutDownNotification", 24))
    )


class NbiFailureReason(SnmpAdminString):
    status = "current"


class NbiIpAddress(TextualConvention, OctetString):
    status = "current"


class NbiNmsName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class NbiNotSyncNEs(TextualConvention, OctetString):
    status = "current"


class NbiNoOfResponseTraps(TextualConvention, Integer32):
    status = "current"


class NbiObjectInstance(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 399),
    )



class NbiObjectInstanceFilter(TextualConvention, OctetString):
    status = "current"


class NbiPortNumber(TextualConvention, OctetString):
    status = "current"


class NbiProcessingStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("partialSuccess", 2),
          ("failure", 3))
    )



class NbiRetransmitTrapIds(SnmpAdminString):
    status = "current"


class NbiRetransmitTrapType(TextualConvention, Integer32):
    status = "current"
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
        *(("alarms", 1),
          ("topologyEvents", 2),
          ("alarmsAndTopologyEvents", 3),
          ("allEvents", 4))
    )



class NbiSequenceId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NbiSeverityFilter(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("filterAllAlarms", 0),
          ("noSeverityFilter", 1),
          ("filterCriticalAlarms", 2),
          ("filterMajorAlarms", 3),
          ("filterMinorAlarms", 4),
          ("filterWarnings", 5),
          ("filterClearedAlarms", 6),
          ("filterIndeterminateAlarms", 7))
    )


class NbiSimpleIdentifier(TextualConvention, Unsigned32):
    status = "current"


class NbiSupervisionPeriod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )



class NbiUserLabel(SnmpAdminString):
    status = "current"


class NbiAckState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 1),
          ("unAcknowledged", 2))
    )



class NbiAckTime(NbiDateAndTime):
    status = "current"


class NbiAckUser(SnmpAdminString):
    status = "current"


class NbiAdditionalText(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



class NbiAlarmHandling(TruthValue):
    status = "current"


class NbiAlarmId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class NbiAlarmIdList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class NbiAlarmTime(DateAndTime):
    status = "current"


class NbiAlarmType(TextualConvention, Integer32):
    status = "current"
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
        *(("communicationsAlarm", 1),
          ("qualityOfServiceAlarm", 2),
          ("processingErrorAlarm", 3),
          ("equipmentAlarm", 4),
          ("environmentalAlarm", 5))
    )



class NbiClearTime(NbiDateAndTime):
    status = "current"


class NbiClearUser(SnmpAdminString):
    status = "current"


class NbiCommentText(TextualConvention, OctetString):
    status = "current"


class NbiCommentTime(NbiDateAndTime):
    status = "current"


class NbiCommentUser(SnmpAdminString):
    status = "current"


class NbiGetAlarms(SnmpAdminString):
    status = "current"


class NbiGetAlarmsByStartingTime(DateAndTime):
    status = "current"


class NbiNumberOfAlarms(TextualConvention, Integer32):
    status = "current"


class NbiPerceivedSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("clear", 5),
          ("indeterminate", 6))
    )



class NbiProbableCause(TextualConvention, Integer32):
    status = "current"


class NbiProposedRepairAction(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )



class NbiRelatedNEs(SnmpAdminString):
    status = "current"


class NbiSpecificProblem(SnmpAdminString):
    status = "current"


class NbiAdditionalInfo(LongUtf8String):
    status = "current"


class NbiAdministrativeState(TextualConvention, Integer32):
    status = "current"
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
        *(("locked", 1),
          ("unlocked", 2),
          ("shuttingDown", 3),
          ("unknown", 4))
    )



class NbiChangedAttributeSet(LongUtf8String):
    status = "current"


class NbiChangedStateSet(LongUtf8String):
    status = "current"


class NbiCommunicationState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



class NbiGetTopologyData(SnmpAdminString):
    status = "current"


class NbiLocation(SnmpAdminString):
    status = "current"


class NbiOperationalState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", 3))
    )



class NbiProductType(SnmpAdminString):
    status = "current"


class NbiVendor(SnmpAdminString):
    status = "current"


class NbiEMSorNEVersion(SnmpAdminString):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSN-SNMP-NBI-TEXTUALCONVENTIONS-MIB",
    **{"NbiActiveInterfaceVersion": NbiActiveInterfaceVersion,
       "NbiChangedPeriodType": NbiChangedPeriodType,
       "NbiEmsSynchronizationState": NbiEmsSynchronizationState,
       "NbiDateAndTime": NbiDateAndTime,
       "NbiEventTime": NbiEventTime,
       "NbiEventTypeFilter": NbiEventTypeFilter,
       "NbiFailureReason": NbiFailureReason,
       "NbiIpAddress": NbiIpAddress,
       "NbiNmsName": NbiNmsName,
       "NbiNotSyncNEs": NbiNotSyncNEs,
       "NbiNoOfResponseTraps": NbiNoOfResponseTraps,
       "NbiObjectInstance": NbiObjectInstance,
       "NbiObjectInstanceFilter": NbiObjectInstanceFilter,
       "NbiPortNumber": NbiPortNumber,
       "NbiProcessingStatus": NbiProcessingStatus,
       "NbiRetransmitTrapIds": NbiRetransmitTrapIds,
       "NbiRetransmitTrapType": NbiRetransmitTrapType,
       "NbiSequenceId": NbiSequenceId,
       "NbiSeverityFilter": NbiSeverityFilter,
       "NbiSimpleIdentifier": NbiSimpleIdentifier,
       "NbiSupervisionPeriod": NbiSupervisionPeriod,
       "NbiUserLabel": NbiUserLabel,
       "NbiAckState": NbiAckState,
       "NbiAckTime": NbiAckTime,
       "NbiAckUser": NbiAckUser,
       "NbiAdditionalText": NbiAdditionalText,
       "NbiAlarmHandling": NbiAlarmHandling,
       "NbiAlarmId": NbiAlarmId,
       "NbiAlarmIdList": NbiAlarmIdList,
       "NbiAlarmTime": NbiAlarmTime,
       "NbiAlarmType": NbiAlarmType,
       "NbiClearTime": NbiClearTime,
       "NbiClearUser": NbiClearUser,
       "NbiCommentText": NbiCommentText,
       "NbiCommentTime": NbiCommentTime,
       "NbiCommentUser": NbiCommentUser,
       "NbiGetAlarms": NbiGetAlarms,
       "NbiGetAlarmsByStartingTime": NbiGetAlarmsByStartingTime,
       "NbiNumberOfAlarms": NbiNumberOfAlarms,
       "NbiPerceivedSeverity": NbiPerceivedSeverity,
       "NbiProbableCause": NbiProbableCause,
       "NbiProposedRepairAction": NbiProposedRepairAction,
       "NbiRelatedNEs": NbiRelatedNEs,
       "NbiSpecificProblem": NbiSpecificProblem,
       "NbiAdditionalInfo": NbiAdditionalInfo,
       "NbiAdministrativeState": NbiAdministrativeState,
       "NbiChangedAttributeSet": NbiChangedAttributeSet,
       "NbiChangedStateSet": NbiChangedStateSet,
       "NbiCommunicationState": NbiCommunicationState,
       "NbiGetTopologyData": NbiGetTopologyData,
       "NbiLocation": NbiLocation,
       "NbiOperationalState": NbiOperationalState,
       "NbiProductType": NbiProductType,
       "NbiVendor": NbiVendor,
       "NbiEMSorNEVersion": NbiEMSorNEVersion,
       "nbiTextualConventionsMIB": nbiTextualConventionsMIB}
)
