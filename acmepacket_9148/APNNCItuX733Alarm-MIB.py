# SNMP MIB module (APNNCItuX733Alarm-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/APNNCItuX733Alarm-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:26 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apNNCItuX733AlarmModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6)
)
if mibBuilder.loadTexts:
    apNNCItuX733AlarmModule.setRevisions(
        ("2013-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Acmepacket_ObjectIdentity = ObjectIdentity
acmepacket = _Acmepacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148)
)
_AcmepacketMgmt_ObjectIdentity = ObjectIdentity
acmepacketMgmt = _AcmepacketMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3)
)
_ApEMSModule_ObjectIdentity = ObjectIdentity
apEMSModule = _ApEMSModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8)
)
_ApNNCItuX733AlarmMIBObjects_ObjectIdentity = ObjectIdentity
apNNCItuX733AlarmMIBObjects = _ApNNCItuX733AlarmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 1)
)
_ApNNCItuX733NotificationObjects_ObjectIdentity = ObjectIdentity
apNNCItuX733NotificationObjects = _ApNNCItuX733NotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2)
)
_ApNNCItuX733NotificationId_Type = Unsigned32
_ApNNCItuX733NotificationId_Object = MibScalar
apNNCItuX733NotificationId = _ApNNCItuX733NotificationId_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 1),
    _ApNNCItuX733NotificationId_Type()
)
apNNCItuX733NotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733NotificationId.setStatus("current")
_ApNNCItuX733ManagedObjectClass_Type = DisplayString
_ApNNCItuX733ManagedObjectClass_Object = MibScalar
apNNCItuX733ManagedObjectClass = _ApNNCItuX733ManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 2),
    _ApNNCItuX733ManagedObjectClass_Type()
)
apNNCItuX733ManagedObjectClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733ManagedObjectClass.setStatus("current")
_ApNNCItuX733ManagedObjectInstance_Type = DisplayString
_ApNNCItuX733ManagedObjectInstance_Object = MibScalar
apNNCItuX733ManagedObjectInstance = _ApNNCItuX733ManagedObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 3),
    _ApNNCItuX733ManagedObjectInstance_Type()
)
apNNCItuX733ManagedObjectInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733ManagedObjectInstance.setStatus("current")


class _ApNNCItuX733PerceivedSeverity_Type(Integer32):
    """Custom type apNNCItuX733PerceivedSeverity based on Integer32"""
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
        *(("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )


_ApNNCItuX733PerceivedSeverity_Type.__name__ = "Integer32"
_ApNNCItuX733PerceivedSeverity_Object = MibScalar
apNNCItuX733PerceivedSeverity = _ApNNCItuX733PerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 4),
    _ApNNCItuX733PerceivedSeverity_Type()
)
apNNCItuX733PerceivedSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733PerceivedSeverity.setStatus("current")


class _ApNNCItuX733EventTime_Type(DisplayString):
    """Custom type apNNCItuX733EventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApNNCItuX733EventTime_Type.__name__ = "DisplayString"
_ApNNCItuX733EventTime_Object = MibScalar
apNNCItuX733EventTime = _ApNNCItuX733EventTime_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 5),
    _ApNNCItuX733EventTime_Type()
)
apNNCItuX733EventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733EventTime.setStatus("current")


class _ApNNCItuX733EventType_Type(Integer32):
    """Custom type apNNCItuX733EventType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("communicationsAlarm", 2),
          ("qualityOfServiceAlarm", 3),
          ("processingErrorAlarm", 4),
          ("equipmentAlarm", 5),
          ("environmentalAlarm", 6),
          ("integrityViolation", 7),
          ("operationalViolation", 8),
          ("physicalViolation", 9),
          ("securityServiceOrMechanismViolation", 10),
          ("timeDomainViolation", 11))
    )


_ApNNCItuX733EventType_Type.__name__ = "Integer32"
_ApNNCItuX733EventType_Object = MibScalar
apNNCItuX733EventType = _ApNNCItuX733EventType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 6),
    _ApNNCItuX733EventType_Type()
)
apNNCItuX733EventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733EventType.setStatus("current")


class _ApNNCItuX733ProbableCause_Type(Integer32):
    """Custom type apNNCItuX733ProbableCause based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("adapterError", 2),
          ("applicationSubsystemFailure", 3),
          ("bandwidthReduced", 4),
          ("callEstablishmentError", 5),
          ("communicationsProtocolError", 6),
          ("communicationsSubsystemFailure", 7),
          ("configurationOrCustomizationError", 8),
          ("congestion", 9),
          ("corruptData", 10),
          ("cpuCyclesLimitExceeded", 11),
          ("dataSetOrModemError", 12),
          ("degradedSignal", 13),
          ("dteDceInterfaceError", 14),
          ("enclosureDoorOpen", 15),
          ("equipmentMalfunction", 16),
          ("excessiveVibration", 17),
          ("fileError", 18),
          ("fireDetected", 19),
          ("floodDetected", 20),
          ("framingError", 21),
          ("heatingVentCoolingSystemProblem", 22),
          ("humidityUnacceptable", 23),
          ("inputOutputDeviceError", 24),
          ("inputDeviceError", 25),
          ("lanError", 26),
          ("leakDetected", 27),
          ("localNodeTransmissionError", 28),
          ("lossOfFrame", 29),
          ("lossOfSignal", 30),
          ("materialSupplyExhausted", 31),
          ("multiplexerProblem", 32),
          ("outOfMemory", 33),
          ("ouputDeviceError", 34),
          ("performanceDegraded", 35),
          ("powerProblem", 36),
          ("pressureUnacceptable", 37),
          ("processorProblem", 38),
          ("pumpFailure", 39),
          ("queueSizeExceeded", 40),
          ("receiveFailure", 41),
          ("receiverFailure", 42),
          ("remoteNodeTransmissionError", 43),
          ("resourceAtOrNearingCapacity", 44),
          ("responseTimeExecessive", 45),
          ("retransmissionRateExcessive", 46),
          ("softwareError", 47),
          ("softwareProgramAbnormallyTerminated", 48),
          ("softwareProgramError", 49),
          ("storageCapacityProblem", 50),
          ("temperatureUnacceptable", 51),
          ("thresholdCrossed", 52),
          ("timingProblem", 53),
          ("toxicLeakDetected", 54),
          ("transmitFailure", 55),
          ("transmitterFailure", 56),
          ("underlyingResourceUnavailable", 57),
          ("versionMismatch", 58),
          ("authenticationFailure", 59),
          ("breachOfConfidentiality", 60),
          ("cableTamper", 61),
          ("delayedInformation", 62),
          ("denialOfService", 63),
          ("duplicateInformation", 64),
          ("informationMissing", 65),
          ("informationModificationDetected", 66),
          ("informationOutOfSequence", 67),
          ("intrusionDetection", 68),
          ("keyExpired", 69),
          ("nonRepudiationFailure", 70),
          ("outOfHoursActivity", 71),
          ("outOfService", 72),
          ("proceduralError", 73),
          ("unauthorizedAccessAttempt", 74),
          ("unexpectedInformation", 75))
    )


_ApNNCItuX733ProbableCause_Type.__name__ = "Integer32"
_ApNNCItuX733ProbableCause_Object = MibScalar
apNNCItuX733ProbableCause = _ApNNCItuX733ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 7),
    _ApNNCItuX733ProbableCause_Type()
)
apNNCItuX733ProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733ProbableCause.setStatus("current")


class _ApNNCItuX733AdditionalText_Type(OctetString):
    """Custom type apNNCItuX733AdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2048),
    )


_ApNNCItuX733AdditionalText_Type.__name__ = "OctetString"
_ApNNCItuX733AdditionalText_Object = MibScalar
apNNCItuX733AdditionalText = _ApNNCItuX733AdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 8),
    _ApNNCItuX733AdditionalText_Type()
)
apNNCItuX733AdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733AdditionalText.setStatus("current")


class _ApNNCItuX733ThresholdInformation_Type(DisplayString):
    """Custom type apNNCItuX733ThresholdInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApNNCItuX733ThresholdInformation_Type.__name__ = "DisplayString"
_ApNNCItuX733ThresholdInformation_Object = MibScalar
apNNCItuX733ThresholdInformation = _ApNNCItuX733ThresholdInformation_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 9),
    _ApNNCItuX733ThresholdInformation_Type()
)
apNNCItuX733ThresholdInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733ThresholdInformation.setStatus("current")


class _ApNNCItuX733SpecificProblem_Type(DisplayString):
    """Custom type apNNCItuX733SpecificProblem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ApNNCItuX733SpecificProblem_Type.__name__ = "DisplayString"
_ApNNCItuX733SpecificProblem_Object = MibScalar
apNNCItuX733SpecificProblem = _ApNNCItuX733SpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 10),
    _ApNNCItuX733SpecificProblem_Type()
)
apNNCItuX733SpecificProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733SpecificProblem.setStatus("current")
_ApNNCItuX733CorrelationNotificationIds_Type = DisplayString
_ApNNCItuX733CorrelationNotificationIds_Object = MibScalar
apNNCItuX733CorrelationNotificationIds = _ApNNCItuX733CorrelationNotificationIds_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 11),
    _ApNNCItuX733CorrelationNotificationIds_Type()
)
apNNCItuX733CorrelationNotificationIds.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733CorrelationNotificationIds.setStatus("current")
_ApNNCItuX733AdditionalInformation_Type = DisplayString
_ApNNCItuX733AdditionalInformation_Object = MibScalar
apNNCItuX733AdditionalInformation = _ApNNCItuX733AdditionalInformation_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 12),
    _ApNNCItuX733AdditionalInformation_Type()
)
apNNCItuX733AdditionalInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733AdditionalInformation.setStatus("current")
_ApNNCItuX733ProposedRepairAction_Type = DisplayString
_ApNNCItuX733ProposedRepairAction_Object = MibScalar
apNNCItuX733ProposedRepairAction = _ApNNCItuX733ProposedRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 2, 13),
    _ApNNCItuX733ProposedRepairAction_Type()
)
apNNCItuX733ProposedRepairAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apNNCItuX733ProposedRepairAction.setStatus("current")
_ApNNCItuX733Notifications_ObjectIdentity = ObjectIdentity
apNNCItuX733Notifications = _ApNNCItuX733Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 3)
)
_ApNNCItuX733NotificationsPrefix_ObjectIdentity = ObjectIdentity
apNNCItuX733NotificationsPrefix = _ApNNCItuX733NotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 3, 0)
)
_ApNNCItuX733ModuleConformance_ObjectIdentity = ObjectIdentity
apNNCItuX733ModuleConformance = _ApNNCItuX733ModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4)
)
_ApNNCItuX733Groups_ObjectIdentity = ObjectIdentity
apNNCItuX733Groups = _ApNNCItuX733Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 1)
)
_ApNNCItuX733NotificationsGroups_ObjectIdentity = ObjectIdentity
apNNCItuX733NotificationsGroups = _ApNNCItuX733NotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 2)
)
_ApNNCItuX733NotificationObjectsGroups_ObjectIdentity = ObjectIdentity
apNNCItuX733NotificationObjectsGroups = _ApNNCItuX733NotificationObjectsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 3)
)

# Managed Objects groups

apNNCItuX733NotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 3, 1)
)
apNNCItuX733NotificationObjectsGroup.setObjects(
      *(("APNNCItuX733Alarm-MIB", "apNNCItuX733NotificationId"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ManagedObjectClass"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ManagedObjectInstance"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733PerceivedSeverity"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733EventTime"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733EventType"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ProbableCause"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalText"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ThresholdInformation"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733SpecificProblem"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733CorrelationNotificationIds"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalInformation"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ProposedRepairAction"))
)
if mibBuilder.loadTexts:
    apNNCItuX733NotificationObjectsGroup.setStatus("current")


# Notification objects

apNNCItuX733Notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 3, 0, 1)
)
apNNCItuX733Notification.setObjects(
      *(("APNNCItuX733Alarm-MIB", "apNNCItuX733NotificationId"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ManagedObjectClass"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ManagedObjectInstance"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733PerceivedSeverity"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733EventTime"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733EventType"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ProbableCause"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalText"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ThresholdInformation"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733SpecificProblem"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733CorrelationNotificationIds"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733AdditionalInformation"),
        ("APNNCItuX733Alarm-MIB", "apNNCItuX733ProposedRepairAction"))
)
if mibBuilder.loadTexts:
    apNNCItuX733Notification.setStatus(
        "current"
    )


# Notifications groups

apNNCItuX733NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 8, 6, 4, 2, 1)
)
apNNCItuX733NotificationsGroup.setObjects(
    ("APNNCItuX733Alarm-MIB", "apNNCItuX733Notification")
)
if mibBuilder.loadTexts:
    apNNCItuX733NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APNNCItuX733Alarm-MIB",
    **{"acmepacket": acmepacket,
       "acmepacketMgmt": acmepacketMgmt,
       "apEMSModule": apEMSModule,
       "apNNCItuX733AlarmModule": apNNCItuX733AlarmModule,
       "apNNCItuX733AlarmMIBObjects": apNNCItuX733AlarmMIBObjects,
       "apNNCItuX733NotificationObjects": apNNCItuX733NotificationObjects,
       "apNNCItuX733NotificationId": apNNCItuX733NotificationId,
       "apNNCItuX733ManagedObjectClass": apNNCItuX733ManagedObjectClass,
       "apNNCItuX733ManagedObjectInstance": apNNCItuX733ManagedObjectInstance,
       "apNNCItuX733PerceivedSeverity": apNNCItuX733PerceivedSeverity,
       "apNNCItuX733EventTime": apNNCItuX733EventTime,
       "apNNCItuX733EventType": apNNCItuX733EventType,
       "apNNCItuX733ProbableCause": apNNCItuX733ProbableCause,
       "apNNCItuX733AdditionalText": apNNCItuX733AdditionalText,
       "apNNCItuX733ThresholdInformation": apNNCItuX733ThresholdInformation,
       "apNNCItuX733SpecificProblem": apNNCItuX733SpecificProblem,
       "apNNCItuX733CorrelationNotificationIds": apNNCItuX733CorrelationNotificationIds,
       "apNNCItuX733AdditionalInformation": apNNCItuX733AdditionalInformation,
       "apNNCItuX733ProposedRepairAction": apNNCItuX733ProposedRepairAction,
       "apNNCItuX733Notifications": apNNCItuX733Notifications,
       "apNNCItuX733NotificationsPrefix": apNNCItuX733NotificationsPrefix,
       "apNNCItuX733Notification": apNNCItuX733Notification,
       "apNNCItuX733ModuleConformance": apNNCItuX733ModuleConformance,
       "apNNCItuX733Groups": apNNCItuX733Groups,
       "apNNCItuX733NotificationsGroups": apNNCItuX733NotificationsGroups,
       "apNNCItuX733NotificationsGroup": apNNCItuX733NotificationsGroup,
       "apNNCItuX733NotificationObjectsGroups": apNNCItuX733NotificationObjectsGroups,
       "apNNCItuX733NotificationObjectsGroup": apNNCItuX733NotificationObjectsGroup}
)
