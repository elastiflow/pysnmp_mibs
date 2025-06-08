# SNMP MIB module (OPTX-ONLINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_5672/OPTX-ONLINE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:47:13 2025
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

(DisplayString,
 Integer32,
 ModuleIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "Integer32",
    "ModuleIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

onlineModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5672, 1)
)
if mibBuilder.loadTexts:
    onlineModule.setRevisions(
        ("1900-02-28 18:01",
         "1900-02-01 18:01",
         "1900-01-31 18:01",
         "1900-01-30 18:01",
         "1900-01-22 18:01",
         "1900-01-13 18:01",
         "1900-01-12 18:01",
         "1900-01-11 18:01",
         "1900-12-14 18:00",
         "1900-12-14 18:00",
         "1900-12-05 18:00",
         "1900-10-04 18:00",
         "1900-08-15 18:00",
         "1900-06-21 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OptxIfIndexType(TextualConvention, Unsigned32):
    status = "current"


class OptxAdministrativeStateValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )



class OptxLockedQualifierValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("management", 0),
          ("maintenance", 1),
          ("softwareDownload", 2))
    )



class OptxAlarmStatusValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("indeterminate", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5),
          ("notReported", 6))
    )



class OptxFaultType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("communicationsAlarm", 0),
          ("qualityOfServiceAlarm", 1),
          ("processingErrorAlarm", 2),
          ("equipmentAlarm", 3),
          ("environmentalAlarm", 4))
    )



class OptxAvailabilityStatusValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("inTest", 0),
          ("failed", 1),
          ("powerOff", 2),
          ("offLine", 3),
          ("offDuty", 4),
          ("dependency", 5),
          ("degraded", 6),
          ("notInstalled", 7),
          ("logFull", 8))
    )



class OptxOperationalStateValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class OptxProbableCauseValue(TextualConvention, Integer32):
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
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              99,
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
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              200,
              201,
              202,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              301,
              302,
              303,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("degradedSignal", 1),
          ("farEndReceiverFailure", 2),
          ("framingError", 3),
          ("lossOfFrame", 4),
          ("lossOfSignal", 5),
          ("excessiveBER", 6),
          ("lowInputPower", 7),
          ("lowOutputPower", 8),
          ("transmitFailure", 9),
          ("thresholdCrossed", 10),
          ("underlyingResourceUnavailable", 11),
          ("excessiveInputPower", 12),
          ("lossOfSignalLine", 13),
          ("lossOfSignalTrib", 14),
          ("unsupportedPayloadType", 15),
          ("signalSquelchedLine", 16),
          ("signalSquelchedTrib", 17),
          ("signalSquelched", 18),
          ("aIS", 19),
          ("aISLine", 20),
          ("aISTrib", 21),
          ("lossOfFrameLine", 22),
          ("lossOfFrameTrib", 23),
          ("sectionTraceMismatchLine", 24),
          ("sectionTraceMismatchTrib", 25),
          ("signalDegradeBER", 26),
          ("signalFailBER", 27),
          ("signalDegradeBERLine", 28),
          ("signalFailBERLine", 29),
          ("signalDegradeBERTrib", 30),
          ("signalFailBERTrib", 31),
          ("lossOfSignalPreamp", 32),
          ("lossOfSignalPostamp", 33),
          ("thresholdCrossedOPR", 34),
          ("thresholdCrossedOPT", 35),
          ("thresholdCrossedOPRLine", 36),
          ("thresholdCrossedOPTLine", 37),
          ("thresholdCrossedLBCLine", 38),
          ("thresholdCrossedOPRTrib", 39),
          ("thresholdCrossedOPTTrib", 40),
          ("thresholdCrossedLBCTrib", 41),
          ("freeRun", 42),
          ("fastStart", 43),
          ("holdover", 44),
          ("referenceOutOfRange", 45),
          ("referenceFailed", 46),
          ("inputSignalExceededAllowedCeilingRate", 47),
          ("excessiveDataRate", 48),
          ("lossOfSignalWPS", 49),
          ("loopback", 50),
          ("backplaneFailure", 51),
          ("powerProblem", 52),
          ("processorProblem", 53),
          ("protectionPathFailure", 54),
          ("receiverFailure", 55),
          ("receiverFailureLine", 56),
          ("receiverFailureTrib", 57),
          ("transmitterFailure", 58),
          ("transmitterFailureLine", 59),
          ("transmitterFailureTrib", 60),
          ("replaceableUnitMissing", 61),
          ("replaceableUnitTypeMismatch", 62),
          ("lossOfClock", 63),
          ("shelfInterconnectFailure", 64),
          ("communicationsFailure", 65),
          ("alarmCardFailure", 66),
          ("planeAcommunicationsFailure", 67),
          ("planeBcommunicationsFailure", 68),
          ("fPGAFailureLine", 69),
          ("fPGAFailureTrib", 70),
          ("fPGAPowerFailureLine", 71),
          ("fPGAPowerFailureTrib", 72),
          ("laserBiasCurrentFailure", 73),
          ("laserBiasCurrentFailureLine", 74),
          ("laserBiasCurrentFailureTrib", 75),
          ("laserWavelengthLockFailure", 76),
          ("laserWavelengthLockFailureLine", 77),
          ("laserWavelengthLockFailureTrib", 78),
          ("replaceableUnitProblem", 79),
          ("peerCommunicationsFailure", 80),
          ("programMemoryFailure", 81),
          ("opticalSwitchFailure", 82),
          ("ethernetSwitchFailure", 83),
          ("temperatureSensorFailure", 84),
          ("osc4080DeviceFailure", 85),
          ("programMemoryMissing", 86),
          ("ethernetLinkAFailure", 87),
          ("ethernetLinkBFailure", 88),
          ("excessiveInputPowerLine", 89),
          ("excessiveInputPowerTrib", 90),
          ("powerAcoCardFailure", 99),
          ("fuseFailure", 101),
          ("highTemperature", 102),
          ("lowTemperature", 103),
          ("coolingFanFailure", 104),
          ("powerEntryFailure", 105),
          ("userAlarm1", 106),
          ("userAlarm2", 107),
          ("userAlarm3", 108),
          ("userAlarm4", 109),
          ("userAlarm5", 110),
          ("userAlarm6", 111),
          ("userAlarm7", 112),
          ("userAlarm8", 113),
          ("userAlarm9", 114),
          ("userAlarm10", 115),
          ("userAlarm11", 116),
          ("userAlarm12", 117),
          ("coolingFanMultipleFailure", 118),
          ("lossOfClockLine", 119),
          ("lossOfClockTrib", 120),
          ("lossValuesOutOfRange", 121),
          ("storageCapacityProblem", 151),
          ("memoryMismatch", 152),
          ("corruptData", 153),
          ("outOfCPUCycles", 154),
          ("softwareDownloadUnavailable", 155),
          ("softwareEnvironmentProblem", 156),
          ("softwareDownloadFailure", 157),
          ("configurationError", 158),
          ("protectionSwitchFailed", 159),
          ("protectionUnitStateMismatch", 160),
          ("powerManagementProblem", 161),
          ("signalingFailure", 162),
          ("oSPRProtectionUnavailable", 163),
          ("wavelengthManagementUnavailable", 164),
          ("shelfTypeMismatch", 165),
          ("diagnosticsFailureEEPromTest", 166),
          ("diagnosticsFailureSpiBusTest", 167),
          ("diagnosticsFailureHDLCTests", 168),
          ("diagnosticsFailureEthernetCpm0", 169),
          ("diagnosticsFailureEthernetCpm1", 170),
          ("diagnosticsFailure48VbusA", 171),
          ("diagnosticsFailure48VbusB", 172),
          ("diagnosticsFailurehs32703110Device", 173),
          ("diagnosticsFailurehsParallelDevice", 174),
          ("diagnosticsFailurehsDioDevice", 175),
          ("diagnosticsFailureOscMRV", 176),
          ("diagnosticsFailureSigFpgaDev", 177),
          ("diagnosticsFailurePM5347Dev", 178),
          ("diagnosticsFailurehsEEPromDevice", 179),
          ("diagnosticsFailurehsSwitchDevice", 180),
          ("diagnosticsFailureEDFADevice", 181),
          ("diagnosticsFailureGrdmPhyDev", 182),
          ("diagnosticsFailureGrdmEpldDevice", 183),
          ("diagnosticsFailureLM81Device", 184),
          ("diagnosticsFailurehsLEDDevice", 185),
          ("diagnosticsFailurehs4080Device", 186),
          ("diagnosticsFailurehsI2cDevice", 187),
          ("diagnosticsFailurehsCommonLedDevice", 188),
          ("diagnosticsFailureADCLoopbackTest", 189),
          ("diagnosticsFailureGrdmYukonDevice", 190),
          ("diagnosticsFailurehsDACad8412Device", 191),
          ("diagnosticsFailurehsADClm12458Device", 192),
          ("berTestRunning", 193),
          ("berTestAborted", 194),
          ("tribOpticalPowerMonitoringNotSupported", 195),
          ("topologyDiscovering", 200),
          ("topologyMismatch", 201),
          ("nodeInRecoveryState", 202),
          ("thresholdNMCrossedCV", 240),
          ("thresholdNMCrossedES", 241),
          ("thresholdNMCrossedSES", 242),
          ("thresholdNMCrossedSEFS", 243),
          ("thresholdNMCrossedCVLine", 244),
          ("thresholdNMCrossedESLine", 245),
          ("thresholdNMCrossedSESLine", 246),
          ("thresholdNMCrossedSEFSLine", 247),
          ("thresholdNMCrossedCVTrib", 248),
          ("thresholdNMCrossedESTrib", 249),
          ("thresholdNMCrossedSESTrib", 250),
          ("thresholdNMCrossedSEFSTrib", 251),
          ("thresholdNMCrossedCVs", 252),
          ("thresholdNMCrossedCVsCh1", 253),
          ("thresholdNMCrossedCVsCh2", 254),
          ("thresholdNMCrossedFCS", 255),
          ("payloadMappingFailure", 256),
          ("thresholdNMCrossedCVL", 257),
          ("thresholdNMCrossedCVLLine", 258),
          ("thresholdNMCrossedCVLTrib", 259),
          ("thresholdNMCrossedESL", 260),
          ("thresholdNMCrossedESLLine", 261),
          ("thresholdNMCrossedESLTrib", 262),
          ("thresholdNMCrossedSESL", 263),
          ("thresholdNMCrossedSESLLine", 264),
          ("thresholdNMCrossedSESLTrib", 265),
          ("thresholdNMCrossedUASL", 266),
          ("thresholdNMCrossedUASLLine", 267),
          ("thresholdNMCrossedUASLTrib", 268),
          ("thresholdNMCrossedFCL", 269),
          ("thresholdNMCrossedFCLLine", 270),
          ("thresholdNMCrossedFCLTrib", 271),
          ("thresholdNMCrossedCVPath", 272),
          ("thresholdNMCrossedESPath", 273),
          ("thresholdNMCrossedSESPath", 274),
          ("thresholdNMCrossedUASPath", 275),
          ("thresholdNMCrossedFCPath", 276),
          ("thresholdNMCrossedTCBELine", 277),
          ("thresholdNMCrossedGbEDE", 278),
          ("thresholdNMCrossedGbELOCS", 279),
          ("thresholdNMCrossedTCBETrib", 280),
          ("thresholdNMCrossedCVsLine", 281),
          ("thresholdNMCrossedCVsTrib", 282),
          ("thresholdNMCrossedGbECRCIn", 283),
          ("thresholdNMCrossedGbECRCOut", 284),
          ("thresholdNMCrossedGbEFRAGSIn", 285),
          ("thresholdNMCrossedGbEFRAGSOut", 286),
          ("thresholdNMCrossedGbEJABBERIn", 287),
          ("thresholdNMCrossedGbEJABBEROut", 288),
          ("thresholdNMCrossedFEFCS", 289),
          ("lossOfPointer", 301),
          ("pathTraceMismatch", 302),
          ("pathAis", 303),
          ("unknown", 1000))
    )



class OptxSourceIndicatorValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resourceOperation", 0),
          ("managementOperation", 1),
          ("unknown", 2))
    )



class OptxStandbyStatusValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("providingService", 0),
          ("hotStandby", 1))
    )



class OptxUsageStateValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("active", 1),
          ("busy", 2))
    )



class OptxThresholdType(TextualConvention, Integer32):
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
        *(("lineLBC", 0),
          ("lineOPR", 1),
          ("tribLBC", 2),
          ("tribOPR", 3),
          ("otherOPT", 4),
          ("otherOPR", 5))
    )



class OptxRestartValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5,
              9,
              10,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("warmReStart", 0),
          ("level1ReStart", 1),
          ("hardwareReStart", 5),
          ("ringMapUpdateReStart", 9),
          ("nodeIdChangeReStart", 10),
          ("unknownReStart", 9999))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTX-ONLINE-MIB",
    **{"OptxIfIndexType": OptxIfIndexType,
       "OptxAdministrativeStateValue": OptxAdministrativeStateValue,
       "OptxLockedQualifierValue": OptxLockedQualifierValue,
       "OptxAlarmStatusValue": OptxAlarmStatusValue,
       "OptxFaultType": OptxFaultType,
       "OptxAvailabilityStatusValue": OptxAvailabilityStatusValue,
       "OptxOperationalStateValue": OptxOperationalStateValue,
       "OptxProbableCauseValue": OptxProbableCauseValue,
       "OptxSourceIndicatorValue": OptxSourceIndicatorValue,
       "OptxStandbyStatusValue": OptxStandbyStatusValue,
       "OptxUsageStateValue": OptxUsageStateValue,
       "OptxThresholdType": OptxThresholdType,
       "OptxRestartValue": OptxRestartValue,
       "onlineModule": onlineModule}
)
