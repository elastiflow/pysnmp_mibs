# SNMP MIB module (ZEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/sysmech_44602/ZEN-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:51:04 2025
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(sysmech,) = mibBuilder.importSymbols(
    "SYSMECH-MIB",
    "sysmech")


# MODULE-IDENTITY

zen = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44602, 1)
)
if mibBuilder.loadTexts:
    zen.setRevisions(
        ("2016-02-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZENAttributeType(TextualConvention, Integer32):
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
        *(("string", 1),
          ("number", 2),
          ("time", 3))
    )



class ZENSeverity(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("cleared", 5))
    )



class ZENProbableCause(TextualConvention, Integer32):
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
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              509,
              510,
              511,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              528,
              529,
              530,
              531,
              532,
              533,
              534,
              535,
              536,
              537,
              538,
              539,
              540,
              541,
              542,
              543,
              544,
              545,
              546,
              547,
              548,
              549,
              550,
              551,
              552,
              553,
              554,
              555,
              600,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              608,
              609,
              610,
              611,
              612,
              613,
              614,
              615,
              1024,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106,
              1107,
              1108,
              1109,
              1110,
              1111,
              1112,
              1113,
              1114,
              1115,
              1116,
              1117,
              1118,
              1119,
              1120,
              1121,
              1122,
              1123,
              1124,
              1125,
              1126,
              1127,
              1128,
              1129,
              1130,
              1131,
              1132,
              1133,
              1134,
              1135,
              1136,
              1137,
              1138,
              1139,
              1140,
              1141,
              1142,
              1143,
              1144,
              1145,
              1146,
              1147,
              1148,
              1149)
        )
    )
    namedValues = NamedValues(
        *(("aIS", 1),
          ("callSetUpFailure", 2),
          ("degradedSignal", 3),
          ("farEndReceiverFailure", 4),
          ("framingError", 5),
          ("lossOfFrame", 6),
          ("lossOfPointer", 7),
          ("lossOfSignal", 8),
          ("payloadTypeMismatch", 9),
          ("transmissionError", 10),
          ("remoteAlarmInterface", 11),
          ("excessiveBER", 12),
          ("pathTraceMismatch", 13),
          ("unavailable", 14),
          ("signalLabelMismatch", 15),
          ("lossOfMultiFrame", 16),
          ("receiveFailure", 17),
          ("transmitFailure", 18),
          ("modulationFailure", 19),
          ("demodulationFailure", 20),
          ("broadcastChannelFailure", 21),
          ("connectionEstablishmentError", 22),
          ("invalidMessageReceived", 23),
          ("localNodeTransmissionError", 24),
          ("remoteNodeTransmissionError", 25),
          ("routingFailure", 26),
          ("backplaneFailure", 51),
          ("dataSetProblem", 52),
          ("equipmentIdentifierDuplication", 53),
          ("externalIFDeviceProblem", 54),
          ("lineCardProblem", 55),
          ("multiplexerProblem", 56),
          ("nEIdentifierDuplication", 57),
          ("powerProblem", 58),
          ("processorProblem", 59),
          ("protectionPathFailure", 60),
          ("receiverFailure", 61),
          ("replaceableUnitMissing", 62),
          ("replaceableUnitTypeMismatch", 63),
          ("synchronizationSourceMismatch", 64),
          ("terminalProblem", 65),
          ("timingProblem", 66),
          ("transmitterFailure", 67),
          ("trunkCardProblem", 68),
          ("replaceableUnitProblem", 69),
          ("realTimeClockFailure", 70),
          ("antennaFailure", 71),
          ("batteryChargingFailure", 72),
          ("diskFailure", 73),
          ("frequencyHoppingFailure", 74),
          ("iODeviceError", 75),
          ("lossOfSynchronisation", 76),
          ("lossOfRedundancy", 77),
          ("powerSupplyFailure", 78),
          ("signalQualityEvaluationFailure", 79),
          ("tranceiverFailure", 80),
          ("protectionMechanismFailure", 81),
          ("protectingResourceFailure", 82),
          ("airCompressorFailure", 101),
          ("airConditioningFailure", 102),
          ("airDryerFailure", 103),
          ("batteryDischarging", 104),
          ("batteryFailure", 105),
          ("commercialPowerFailure", 106),
          ("coolingFanFailure", 107),
          ("engineFailure", 108),
          ("fireDetectorFailure", 109),
          ("fuseFailure", 110),
          ("generatorFailure", 111),
          ("lowBatteryThreshold", 112),
          ("pumpFailure", 113),
          ("rectifierFailure", 114),
          ("rectifierHighVoltage", 115),
          ("rectifierLowFVoltage", 116),
          ("ventilationsSystemFailure", 117),
          ("enclosureDoorOpen", 118),
          ("explosiveGas", 119),
          ("fire", 120),
          ("flood", 121),
          ("highHumidity", 122),
          ("highTemperature", 123),
          ("highWind", 124),
          ("iceBuildUp", 125),
          ("intrusionDetection", 126),
          ("lowFuel", 127),
          ("lowHumidity", 128),
          ("lowCablePressure", 129),
          ("lowTemperatue", 130),
          ("lowWater", 131),
          ("smoke", 132),
          ("toxicGas", 133),
          ("coolingSystemFailure", 134),
          ("externalEquipmentFailure", 135),
          ("externalPointFailure", 136),
          ("storageCapacityProblem", 151),
          ("memoryMismatch", 152),
          ("corruptData", 153),
          ("outOfCPUCycles", 154),
          ("sfwrEnvironmentProblem", 155),
          ("sfwrDownloadFailure", 156),
          ("lossOfRealTimel", 157),
          ("applicationSubsystemFailure", 158),
          ("configurationOrCustomisationError", 159),
          ("databaseInconsistency", 160),
          ("fileError", 161),
          ("outOfMemory", 162),
          ("softwareError", 163),
          ("timeoutExpired", 164),
          ("underlayingResourceUnavailable", 165),
          ("versionMismatch", 166),
          ("bandwidthReduced", 201),
          ("congestion", 202),
          ("excessiveErrorRate", 203),
          ("excessiveResponseTime", 204),
          ("excessiveRetransmissionRate", 205),
          ("reducedLoggingCapability", 206),
          ("systemResourcesOverload", 207),
          ("adapterError", 500),
          ("applicationSubsystemFailture", 501),
          ("bandwidthReducedX733", 502),
          ("callEstablishmentError", 503),
          ("communicationsProtocolError", 504),
          ("communicationsSubsystemFailure", 505),
          ("configurationOrCustomizationError", 506),
          ("congestionX733", 507),
          ("coruptData", 508),
          ("cpuCyclesLimitExceeded", 509),
          ("dataSetOrModemError", 510),
          ("degradedSignalX733", 511),
          ("dteDceInterfaceError", 512),
          ("enclosureDoorOpenX733", 513),
          ("equipmentMalfunction", 514),
          ("excessiveVibration", 515),
          ("fileErrorX733", 516),
          ("fireDetected", 517),
          ("framingErrorX733", 518),
          ("heatingVentCoolingSystemProblem", 519),
          ("humidityUnacceptable", 520),
          ("inputOutputDeviceError", 521),
          ("inputDeviceError", 522),
          ("lanError", 523),
          ("leakDetected", 524),
          ("localNodeTransmissionErrorX733", 525),
          ("lossOfFrameX733", 526),
          ("lossOfSignalX733", 527),
          ("materialSupplyExhausted", 528),
          ("multiplexerProblemX733", 529),
          ("outOfMemoryX733", 530),
          ("ouputDeviceError", 531),
          ("performanceDegraded", 532),
          ("powerProblems", 533),
          ("pressureUnacceptable", 534),
          ("processorProblems", 535),
          ("pumpFailureX733", 536),
          ("queueSizeExceeded", 537),
          ("receiveFailureX733", 538),
          ("receiverFailureX733", 539),
          ("remoteNodeTransmissionErrorX733", 540),
          ("resourceAtOrNearingCapacity", 541),
          ("responseTimeExecessive", 542),
          ("retransmissionRateExcessive", 543),
          ("softwareErrorX733", 544),
          ("softwareProgramAbnormallyTerminated", 545),
          ("softwareProgramError", 546),
          ("storageCapacityProblemX733", 547),
          ("temperatureUnacceptable", 548),
          ("thresholdCrossed", 549),
          ("timingProblemX733", 550),
          ("toxicLeakDetected", 551),
          ("transmitFailureX733", 552),
          ("transmiterFailure", 553),
          ("underlyingResourceUnavailable", 554),
          ("versionMismatchX733", 555),
          ("authenticationFailure", 600),
          ("breachOfConfidentiality", 601),
          ("cableTamper", 602),
          ("delayedInformation", 603),
          ("denialOfService", 604),
          ("duplicateInformation", 605),
          ("informationMissing", 606),
          ("informationModificationDetected", 607),
          ("informationOutOfSequence", 608),
          ("keyExpired", 609),
          ("nonRepudiationFailure", 610),
          ("outOfHoursActivity", 611),
          ("outOfService", 612),
          ("proceduralError", 613),
          ("unauthorizedAccessAttempt", 614),
          ("unexpectedInformation", 615),
          ("other", 1024),
          ("abisToTRXInterfaceFailure", 1101),
          ("clockSynchronisationProblem", 1102),
          ("combinerProblem", 1103),
          ("excessiveReceiverTemperature", 1104),
          ("excessiveTransmitterOutputPower", 1105),
          ("excessiveTransmitterTemperature", 1106),
          ("frequencyHoppingDegraded", 1107),
          ("frequencyRedefinitionFailed", 1108),
          ("lineInterfaceFailure", 1109),
          ("linkFailure", 1110),
          ("lostRedundancy", 1111),
          ("mainsBreakdownWithBatteryBackUp", 1112),
          ("mainsBreakdownWithoutBatteryBackUp", 1113),
          ("receiverAntennaFault", 1114),
          ("receiverMulticouplerFailure", 1115),
          ("reducedTransmitterOutputPower", 1116),
          ("signalQualityEvaluationFault", 1117),
          ("timeslotHardwareFailure", 1118),
          ("transceiverProblem", 1119),
          ("transcoderProblem", 1120),
          ("transcoderOrRateAdapterProblem", 1121),
          ("transmitterAntennaFailure", 1122),
          ("transmitterAntennaNotAdjusted", 1123),
          ("transmitterLowVoltageOrCurrent", 1124),
          ("transmitterOffFrequency", 1125),
          ("fileSystemCallUnsuccessful", 1126),
          ("inputParameterOutOfRange", 1127),
          ("invalidParameter", 1128),
          ("invalidPointer", 1129),
          ("messageNotExpected", 1130),
          ("messageNotInitialised", 1131),
          ("messageOutOfSequence", 1132),
          ("systemCallUnsuccessful", 1133),
          ("variableOutOfRange", 1134),
          ("watchDogTimerExpired", 1135),
          ("externalPowerSupplyFailure", 1136),
          ("externalTransmissionDeviceFailure", 1137),
          ("reducedAlarmReporting", 1138),
          ("reducedEventReporting", 1139),
          ("invalidMSUReceived", 1140),
          ("lAPDLinkProtocolFailure", 1141),
          ("localAlarmIndication", 1142),
          ("remoteAlarmIndication", 1143),
          ("sS7ProtocolFailure", 1144),
          ("dataSetOrModemProblem", 1145),
          ("antennaProblem", 1146),
          ("batteryBreakdown", 1147),
          ("diskProblem", 1148),
          ("transmissionFailure", 1149))
    )



class ZENEventType(TextualConvention, Integer32):
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



class ZENonId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )



# MIB Managed Objects in the order of their OIDs

_ZenTraps_ObjectIdentity = ObjectIdentity
zenTraps = _ZenTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44602, 1, 0)
)
_ZenTrapInfo_ObjectIdentity = ObjectIdentity
zenTrapInfo = _ZenTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1)
)
_ZenEventCreator_Type = DisplayString
_ZenEventCreator_Object = MibScalar
zenEventCreator = _ZenEventCreator_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 1),
    _ZenEventCreator_Type()
)
zenEventCreator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zenEventCreator.setStatus("current")
_ZenNotifId_Type = DisplayString
_ZenNotifId_Object = MibScalar
zenNotifId = _ZenNotifId_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 2),
    _ZenNotifId_Type()
)
zenNotifId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zenNotifId.setStatus("current")
_ZenManagedObjectId_Type = ZENonId
_ZenManagedObjectId_Object = MibScalar
zenManagedObjectId = _ZenManagedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 3),
    _ZenManagedObjectId_Type()
)
zenManagedObjectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zenManagedObjectId.setStatus("current")
_ZenAlarmType_Type = ZENEventType
_ZenAlarmType_Object = MibScalar
zenAlarmType = _ZenAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 4),
    _ZenAlarmType_Type()
)
zenAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zenAlarmType.setStatus("current")
_ZenProbableCause_Type = ZENProbableCause
_ZenProbableCause_Object = MibScalar
zenProbableCause = _ZenProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 5),
    _ZenProbableCause_Type()
)
zenProbableCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zenProbableCause.setStatus("current")
_ZenSeverity_Type = ZENSeverity
_ZenSeverity_Object = MibScalar
zenSeverity = _ZenSeverity_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 6),
    _ZenSeverity_Type()
)
zenSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zenSeverity.setStatus("current")
_ZenEventTime_Type = DateAndTime
_ZenEventTime_Object = MibScalar
zenEventTime = _ZenEventTime_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 7),
    _ZenEventTime_Type()
)
zenEventTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zenEventTime.setStatus("current")
_ZenAdditionalText_Type = DisplayString
_ZenAdditionalText_Object = MibScalar
zenAdditionalText = _ZenAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 8),
    _ZenAdditionalText_Type()
)
zenAdditionalText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zenAdditionalText.setStatus("current")
_ZenAttributeChangeTable_Object = MibTable
zenAttributeChangeTable = _ZenAttributeChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 9)
)
if mibBuilder.loadTexts:
    zenAttributeChangeTable.setStatus("current")
_ZenAttributeEntry_Object = MibTableRow
zenAttributeEntry = _ZenAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 9, 1)
)
zenAttributeEntry.setIndexNames(
    (0, "ZEN-MIB", "zenAttributeEntryIndex"),
)
if mibBuilder.loadTexts:
    zenAttributeEntry.setStatus("current")


class _ZenAttributeEntryIndex_Type(Integer32):
    """Custom type zenAttributeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZenAttributeEntryIndex_Type.__name__ = "Integer32"
_ZenAttributeEntryIndex_Object = MibTableColumn
zenAttributeEntryIndex = _ZenAttributeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 9, 1, 1),
    _ZenAttributeEntryIndex_Type()
)
zenAttributeEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zenAttributeEntryIndex.setStatus("current")
_Name_Type = DisplayString
_Name_Object = MibTableColumn
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 9, 1, 2),
    _Name_Type()
)
name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Value_Type = DisplayString
_Value_Object = MibTableColumn
value = _Value_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 9, 1, 3),
    _Value_Type()
)
value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    value.setStatus("current")
_OldValue_Type = DisplayString
_OldValue_Object = MibTableColumn
oldValue = _OldValue_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 9, 1, 4),
    _OldValue_Type()
)
oldValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldValue.setStatus("current")
_ZenStateChangeTable_Object = MibTable
zenStateChangeTable = _ZenStateChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 10)
)
if mibBuilder.loadTexts:
    zenStateChangeTable.setStatus("current")
_ZenStateEntry_Object = MibTableRow
zenStateEntry = _ZenStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 10, 1)
)
zenStateEntry.setIndexNames(
    (0, "ZEN-MIB", "zenStateEntryIndex"),
)
if mibBuilder.loadTexts:
    zenStateEntry.setStatus("current")


class _ZenStateEntryIndex_Type(Integer32):
    """Custom type zenStateEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZenStateEntryIndex_Type.__name__ = "Integer32"
_ZenStateEntryIndex_Object = MibTableColumn
zenStateEntryIndex = _ZenStateEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 10, 1, 1),
    _ZenStateEntryIndex_Type()
)
zenStateEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zenStateEntryIndex.setStatus("current")
_FaultState_Type = DisplayString
_FaultState_Object = MibTableColumn
faultState = _FaultState_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 10, 1, 2),
    _FaultState_Type()
)
faultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultState.setStatus("current")
_OldFaultState_Type = DisplayString
_OldFaultState_Object = MibTableColumn
oldFaultState = _OldFaultState_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 10, 1, 3),
    _OldFaultState_Type()
)
oldFaultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldFaultState.setStatus("current")
_OperationalState_Type = DisplayString
_OperationalState_Object = MibTableColumn
operationalState = _OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 10, 1, 4),
    _OperationalState_Type()
)
operationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operationalState.setStatus("current")
_OldOperationalState_Type = DisplayString
_OldOperationalState_Object = MibTableColumn
oldOperationalState = _OldOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 44602, 1, 1, 10, 1, 5),
    _OldOperationalState_Type()
)
oldOperationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldOperationalState.setStatus("current")

# Managed Objects groups


# Notification objects

zenAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44602, 1, 0, 1)
)
zenAlarm.setObjects(
      *(("ZEN-MIB", "zenEventCreator"),
        ("ZEN-MIB", "zenNotifId"),
        ("ZEN-MIB", "zenManagedObjectId"),
        ("ZEN-MIB", "zenAlarmType"),
        ("ZEN-MIB", "zenProbableCause"),
        ("ZEN-MIB", "zenSeverity"),
        ("ZEN-MIB", "zenEventTime"),
        ("ZEN-MIB", "zenAdditionalText"))
)
if mibBuilder.loadTexts:
    zenAlarm.setStatus(
        "current"
    )

zenAlarmAttributeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 44602, 1, 0, 2)
)
zenAlarmAttributeChange.setObjects(
      *(("ZEN-MIB", "zenEventCreator"),
        ("ZEN-MIB", "zenNotifId"),
        ("ZEN-MIB", "zenEventTime"),
        ("ZEN-MIB", "zenAttributeChangeTable"))
)
if mibBuilder.loadTexts:
    zenAlarmAttributeChange.setStatus(
        "current"
    )

zenAlarmStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 44602, 1, 0, 3)
)
zenAlarmStateChange.setObjects(
      *(("ZEN-MIB", "zenEventCreator"),
        ("ZEN-MIB", "zenNotifId"),
        ("ZEN-MIB", "zenEventTime"),
        ("ZEN-MIB", "zenState"))
)
if mibBuilder.loadTexts:
    zenAlarmStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZEN-MIB",
    **{"ZENAttributeType": ZENAttributeType,
       "ZENSeverity": ZENSeverity,
       "ZENProbableCause": ZENProbableCause,
       "ZENEventType": ZENEventType,
       "ZENonId": ZENonId,
       "zen": zen,
       "zenTraps": zenTraps,
       "zenAlarm": zenAlarm,
       "zenAlarmAttributeChange": zenAlarmAttributeChange,
       "zenAlarmStateChange": zenAlarmStateChange,
       "zenTrapInfo": zenTrapInfo,
       "zenEventCreator": zenEventCreator,
       "zenNotifId": zenNotifId,
       "zenManagedObjectId": zenManagedObjectId,
       "zenAlarmType": zenAlarmType,
       "zenProbableCause": zenProbableCause,
       "zenSeverity": zenSeverity,
       "zenEventTime": zenEventTime,
       "zenAdditionalText": zenAdditionalText,
       "zenAttributeChangeTable": zenAttributeChangeTable,
       "zenAttributeEntry": zenAttributeEntry,
       "zenAttributeEntryIndex": zenAttributeEntryIndex,
       "name": name,
       "value": value,
       "oldValue": oldValue,
       "zenStateChangeTable": zenStateChangeTable,
       "zenStateEntry": zenStateEntry,
       "zenStateEntryIndex": zenStateEntryIndex,
       "faultState": faultState,
       "oldFaultState": oldFaultState,
       "operationalState": operationalState,
       "oldOperationalState": oldOperationalState}
)
