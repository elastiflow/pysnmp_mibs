# SNMP MIB module (CALIX-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-TC.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:36:06 2025
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



class BpId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class Clei(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11



class AlarmTransition(TextualConvention, Integer32):
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
        *(("falling", 1),
          ("raising", 2),
          ("unknown", 3))
    )



class AlarmSeverity(TextualConvention, Integer32):
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
        *(("minor", 1),
          ("major", 2),
          ("critical", 3),
          ("unknown", 4))
    )



class CondSeverity(TextualConvention, Integer32):
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
        *(("minor", 1),
          ("major", 2),
          ("critical", 3),
          ("notAlarmed", 4),
          ("notReported", 5),
          ("unknown", 6))
    )



class CondLocation(TextualConvention, Integer32):
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
        *(("nearEnd", 1),
          ("farEnd", 2),
          ("bothEnds", 3),
          ("notApplicable", 4))
    )



class CondState(TextualConvention, Integer32):
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
        *(("cleared", 1),
          ("standing", 2),
          ("transient", 3),
          ("notApplicable", 4))
    )



class CondType(TextualConvention, Integer32):
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
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
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
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
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
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
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
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              327,
              328,
              329,
              330,
              331,
              332,
              333,
              334,
              335,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              360,
              361,
              362,
              363,
              364,
              365,
              366,
              367,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              417,
              418,
              419,
              420,
              421,
              422,
              423,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              433,
              434,
              435,
              436,
              437,
              438,
              439,
              440,
              441,
              442,
              443,
              444,
              445,
              446,
              447,
              448,
              449,
              450,
              451,
              452,
              453,
              454,
              455,
              456,
              457,
              458,
              459,
              460,
              461,
              462,
              463,
              464,
              465,
              466,
              467,
              468,
              469,
              470,
              471,
              472,
              473,
              474,
              475,
              476,
              477,
              478,
              479,
              480,
              481,
              482,
              483,
              484,
              485,
              486,
              487,
              488,
              489,
              490,
              491,
              492,
              493,
              494,
              495,
              496,
              497,
              498,
              499,
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
              556,
              557,
              558,
              559,
              560,
              561,
              562,
              563,
              564,
              565,
              566,
              567,
              568,
              569,
              570,
              571,
              572,
              573,
              574,
              575,
              576,
              577,
              578,
              579,
              580,
              581,
              582,
              583,
              584,
              585,
              586,
              587,
              588,
              589,
              590,
              591,
              592,
              593,
              594,
              595,
              596,
              597,
              598,
              599,
              600,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              608)
        )
    )
    namedValues = NamedValues(
        *(("alarmCutoffImmediateMode", 1),
          ("alarmCutoffManualMode", 2),
          ("loopbackInActPosition", 3),
          ("airCompressorFail", 4),
          ("airConditioningFail", 5),
          ("airDryerFailure", 6),
          ("alarmIndicationSignal", 7),
          ("alarmIndicationSignalLine", 8),
          ("alarmIndicationSignalPath", 9),
          ("protectSwitchByteFail", 10),
          ("topologyChange", 11),
          ("protectSwitchChannelMatchFail", 12),
          ("protectSwitchModeMismatch", 13),
          ("batteryDischarge", 14),
          ("batteryFail", 15),
          ("blockError", 16),
          ("bipolarViolation", 17),
          ("compositeClockBipolarViolDensity", 18),
          ("coolFanFailure", 19),
          ("coldProcessorReset", 20),
          ("coldDatabaseReset", 21),
          ("centralPowerMajorEnvAlarm", 22),
          ("centralPowerMinorEnvAlarm", 23),
          ("cyclicRedundCheckError", 24),
          ("databaseTransferFail", 25),
          ("engineFail", 26),
          ("engineOperating", 27),
          ("embeddedOperChanDuplexFail", 28),
          ("equipmentFail", 29),
          ("explosiveGas", 30),
          ("excessiveZeroes", 31),
          ("failToReleaseFromProtection", 32),
          ("failToSwitchToProtection", 33),
          ("fanFail", 34),
          ("frameBitError", 35),
          ("farEndBlockError", 36),
          ("farEndProtectLineFail", 37),
          ("fireDetectFail", 38),
          ("fire", 39),
          ("flood", 40),
          ("forcedSwitchToWorking", 41),
          ("forcedSwitchToProtection", 42),
          ("fuseFail", 43),
          ("generatorFail", 44),
          ("heatFail", 45),
          ("highAirflow", 46),
          ("highHumidity", 47),
          ("highTemperature", 48),
          ("highWater", 49),
          ("improperRemoval", 50),
          ("inhibitAutomaticMessageToOs", 51),
          ("inhibitPerfMonitoringMsg", 52),
          ("inhibitSwitchToDuplex", 53),
          ("inhibitSwitchToProtection", 54),
          ("inhibitSwitchToWorking", 55),
          ("inhibitStandbyUpgrade", 56),
          ("intruderAtSite", 57),
          ("intrusionAtMgmtInterface", 58),
          ("lightFail", 59),
          ("lockoutOfProtection", 60),
          ("lockoutOfWorking", 61),
          ("lossOfFrame", 62),
          ("logBuffer90percentFull", 63),
          ("logBufferDatabaseChange90percentFull", 64),
          ("logBufferSecurity90percentFull", 65),
          ("logBufferAlarmOverflow", 66),
          ("logBufferDatabaseChangeOverflow", 67),
          ("logBufferSecurityOverflow", 68),
          ("lossOfPointer", 69),
          ("lossOfPointerPath", 70),
          ("lossOfSignal", 71),
          ("loopbackCrossConnect", 72),
          ("loopbackDs1Feac", 73),
          ("lpbkDs3Feac", 74),
          ("loopbackLine", 75),
          ("lowBatteryVoltage", 76),
          ("lowFuel", 77),
          ("lowHumidity", 78),
          ("lowCablePressure", 79),
          ("lowTemperature", 80),
          ("lowWater", 81),
          ("manualSyncSwitchToIntClock", 82),
          ("manualSyncSwitchToPriClock", 83),
          ("manualSyncSwitchToSecClock", 84),
          ("manualSwitchFacEquipmentToWorking", 85),
          ("manualSwitchFacEquipmentToProtection", 86),
          ("miscellaneous", 87),
          ("normal", 88),
          ("openDoor", 89),
          ("automaticProtectionSwitchOverridden", 90),
          ("payloadLabelMismatch", 91),
          ("commercialPowerFail", 92),
          ("protectionUnitNotAvailable", 93),
          ("protectionSwitch", 94),
          ("pumpFail", 95),
          ("powerMgmtCardShutDown", 96),
          ("powerFailRestart", 97),
          ("remoteAlarmIndication", 98),
          ("rectifierFail", 99),
          ("rectifierHighVoltage", 100),
          ("rectifierLowVoltage", 101),
          ("remoteErrorIndicationLine", 102),
          ("remoteErrorIndicationPath", 103),
          ("replaceableUnitMissing", 104),
          ("remoteFailIndication", 105),
          ("remoteFailIndicationLine", 106),
          ("remoteFailIndicationPath", 107),
          ("realTimeClockFail", 108),
          ("stateChangeManualMaint", 109),
          ("signalDegradeBitErrorRate", 110),
          ("signalFailBitErrorRate", 111),
          ("signalLabelMismatchFail", 112),
          ("smokeDetected", 113),
          ("sprinklerFail", 114),
          ("softwareDownloadInProgress", 115),
          ("syncSwitchToInternalClock", 116),
          ("syncSwitchToPrimaryClock", 117),
          ("syncSwitchToSecondaryClock", 118),
          ("lossOfTimingOnBothSyncLinks", 119),
          ("lossOfTimingOnPrimarySyncLink", 120),
          ("lossOfTimingOnSecondarySyncLink", 121),
          ("syncStatusChange", 122),
          ("sysBoot", 123),
          ("thresholdOfUidAttemptsExceeded", 124),
          ("traceIdentifierMessageDefect", 125),
          ("timeSlotMgmtChannelDuplexFail", 126),
          ("timeSlotMgmtChannelSimplexFail", 127),
          ("toxicGas", 128),
          ("testSessionActive", 129),
          ("unequipped", 130),
          ("ventilationFail", 131),
          ("warmRestart", 132),
          ("facSwitchedBackToWorking", 133),
          ("facSwitchedBackToProtection", 134),
          ("waitingToRestoreState", 135),
          ("lossOfPower", 136),
          ("mismatchOfEquipmentAndProvisioning", 137),
          ("lossOfCellDelineationPath", 138),
          ("lossOfConnectivity", 139),
          ("tresholdControlSlipsPath", 140),
          ("thresholCodeViolationPathCPbitParity", 141),
          ("thresholdCodeViolationFastLine", 142),
          ("thresholdCodeViolationInterleavedLine", 143),
          ("thresholdCodeViolationLine", 144),
          ("thresholdCodeViolationPath", 145),
          ("thresholdCodeViolationSection", 146),
          ("thresholdForwardErrorCorrectionFastLine", 147),
          ("thresholdForwardErrorCorrectionInterleavedLine", 148),
          ("thresholdForwardErrorSecondsLine", 149),
          ("thresholdErrorSecondsLine", 150),
          ("thresholdErrSecondsPathCPbitParity", 151),
          ("thresholdErrorSecondsPath", 152),
          ("thresholdErrorSecondsSection", 153),
          ("thresholdNormalizedLaserBiasurrent", 154),
          ("thresholdOpticalPowerReceivedLevel", 155),
          ("thresholdOpticalPowerTransmissionLevel", 156),
          ("thresholdSeverErrorFrameAisSeconds", 157),
          ("thresholdSeverErrorSecondsPathCPbitParity", 158),
          ("thresholdSeverErrFrameSecondsPath", 159),
          ("thresholdSeverErrorFrameSecondsSection", 160),
          ("thresholdSeverErrorSecondsLine", 161),
          ("thresholdSeverErrorSecondsPath", 162),
          ("thresholdSeverErrorSecondsSection", 163),
          ("thresholdUnavailableSecondsPathCPbitParity", 164),
          ("thresholdUnavailableSecondsLine", 165),
          ("thresholdUnavailableSecondsPath", 166),
          ("softwareIncompatibility", 167),
          ("inhibitTmcProtectionSwitch", 168),
          ("inhibitEocProtectionSwitch", 169),
          ("tdmPathFail", 170),
          ("lossOfCellDelineationFast", 171),
          ("lossOfCellDelineationInterleaved", 172),
          ("noCellDelineationFast", 173),
          ("noCellDelineationInterleaved", 174),
          ("alarmCutoffInDelayedMode", 175),
          ("thresholdAlarmIndicationSignalSeconds", 176),
          ("threshCodeViolationPathPbitParity", 177),
          ("thresholdErrorSecondsPathPbitParity", 178),
          ("thresholdSeverErrorSecondsPathPbitParity", 179),
          ("thresholdUnavailableSecondsPathPbitParity", 180),
          ("thresholdAlarmIndicationSecondsPathEgress", 181),
          ("thresholdCodeViolationPathPbitParity", 182),
          ("thresholdErrorSecondsPathPbitParityEgress", 183),
          ("thresholdSeverErrorSecondstPathPbitParityEgress", 184),
          ("thresholdUnavailSecondsPathPbitParityEgress", 185),
          ("thresholdSeverErrorAisSecondsPathEgress", 186),
          ("thresholdCodeViolationPathCPbitParity", 187),
          ("thresholdErrorSecondsPathCPbitParityEgress", 188),
          ("thresholdSeverErrorAisSecondsCPbitParityEgress", 189),
          ("thresholdUnavailableSecondPathCPbitParityEgress", 190),
          ("thresholdErrorSecondsPathCPbitParity", 191),
          ("alarmIndicationSignalMatrix", 192),
          ("lossOfFrameMatrix", 193),
          ("lossOfSignalMatrix", 194),
          ("remoteAlarmIndicationMatrix", 195),
          ("embeddedOperationChannelSimplexFail", 196),
          ("lossOfFramePlcp", 197),
          ("remoteFailureIndicationPlcp", 198),
          ("signalDegradeBitErrorRatePath", 199),
          ("signalFailBitErrorRatePath", 200),
          ("equipmentManualSwitchedBackToWorking", 201),
          ("equipmentManualSwitchedToProtection", 202),
          ("hardwareTypeUnknown", 203),
          ("automaticProtectionSwitchingByteBabble", 204),
          ("equipmentSwitchedBackToWorking", 205),
          ("equipmentSwitchedToProtection", 206),
          ("dataFault", 207),
          ("enhancedRemoteFailureIndicationServerPath", 208),
          ("enhancedRemoteFailureConnectivityPath", 209),
          ("enhancedRemoteFailureIndicationPayloadPath", 210),
          ("unused1", 211),
          ("payloadFailureIndication", 212),
          ("doNotRevert", 213),
          ("active", 214),
          ("standby", 215),
          ("lossOfCellDelineation", 216),
          ("remoteFailureIndication", 217),
          ("equipmentProtectionTypeMismatch", 218),
          ("farEndMismatchDetected", 219),
          ("provisioningFail", 220),
          ("auditMismatch", 221),
          ("databaseMismatch", 222),
          ("loopbackFacility", 223),
          ("loopbackPayload", 224),
          ("loopbackTerminal", 225),
          ("remoteDefectIndicationLine", 226),
          ("remoteDefectIndicationPath", 227),
          ("farEndFfpDomainMismatch", 228),
          ("farEndDomainMismatch", 229),
          ("disjointDomain", 230),
          ("linkOnDisjointDomain", 231),
          ("thresholdLossOfSignalSecondsLine", 232),
          ("thresholdFailCountLine", 233),
          ("thresholdProtectionSwitchCountLine", 234),
          ("thresholdProtectionSwitchDurationLine", 235),
          ("thresholdFailCountPath", 236),
          ("userLogin", 237),
          ("passwordExpired", 238),
          ("userLogout", 239),
          ("userForcedLogout", 240),
          ("userloginAttemptFailed", 241),
          ("userProvisionModified", 242),
          ("securityTemplateModified", 243),
          ("commandDeniedForSecurityReason", 244),
          ("changeAccessPrivilegeMgmtPort", 245),
          ("shelfCommunicationLost", 246),
          ("forcedSwitchToInternalTimingSource", 247),
          ("forcedSwitchToPrimaryTimingSource", 248),
          ("forcedSwitchToSecondaryTimingSource", 249),
          ("forcedSwitchDDS1ToSystemTimingSource", 250),
          ("forcedSwitchDDS1ToRAPTimingSource", 251),
          ("manualSwitchDDS1ToSystemTimingSource", 252),
          ("manualSwitchDDS1ToRAPTimingSource", 253),
          ("autoSwitchDDS1ToSystemTimingSource", 254),
          ("autoSwitchDDS1ToRAPTimingSource", 255),
          ("peerNoLongerReachable", 256),
          ("peerNack", 257),
          ("thresholdSeverErrorFrameAisSecondsCPbitParity", 258),
          ("thresholdSeverErrorFrameAisSecondsCPbitParityEgress", 259),
          ("duplicatedAdminMasterProvisioned", 260),
          ("logAlarmInit", 261),
          ("logDatabaseChangeInit", 262),
          ("alarmIndicationSignalPathMatrix", 263),
          ("lossOfPointerPathMatrix", 264),
          ("remoteFailureIndicationPathMatrix", 265),
          ("unequippedPathMatrix", 266),
          ("traceIdentifierMessagePathMatrix", 267),
          ("payloadLabelMismatchMatrix", 268),
          ("signalDegradeBitErrorRateMatrix", 269),
          ("signalFailBitErrorRateMatrix", 270),
          ("lossOfContinuity", 271),
          ("log9AlarmInit", 272),
          ("log9DatabaseChangeInit", 273),
          ("backupAndRestoreInProgress", 274),
          ("imaLossOfFrame", 275),
          ("imaLinkOutOfDelaySynch", 276),
          ("imaTxLinkMisconnected", 277),
          ("imaRxLinkMisconnected", 278),
          ("imaRemoteDefectIndication", 279),
          ("imaFarEndTxUnusable", 280),
          ("imaFarEndRxUnusable", 281),
          ("imaNearEndInvalidCfgForState", 282),
          ("imaFarEndClockMismatchNearClock", 283),
          ("imaNearEndInsufficientLinks", 284),
          ("imaFarEndInsufficientLinks", 285),
          ("imaFarEndInStartUpState", 286),
          ("imaFarEndInvalidCfgForState", 287),
          ("imaFarEndInBlockedState", 288),
          ("hdslLossOfSynchronization", 289),
          ("thresholdSeverErrorFrameSecondsPath", 290),
          ("systemSecurityModified", 291),
          ("dcInputAFail", 292),
          ("dcInputBFail", 293),
          ("remoteAlarm", 294),
          ("invalidBackplaneId", 295),
          ("incorrectSwVersionForLu", 296),
          ("administrativeAmpAbsent", 297),
          ("totalFailCountPathEgress", 298),
          ("totalFailCountCBitParityPathIngress", 299),
          ("totalFailCountCBitParityPathEgress", 300),
          ("ddsLoopRLOS", 301),
          ("ddsLoopSignalAbsent", 302),
          ("ddsLoopNotSynchronized", 303),
          ("ddsOcuLatchLoopback", 304),
          ("ddsOcuLbNonLatchLoopback", 305),
          ("ddsCsuLatchLoopback", 306),
          ("ddsCsuNonLatchLoopback", 307),
          ("ddsDs0DropLoopback", 308),
          ("ddsDs0LineLoopback", 309),
          ("enhancedRemoteFailureIndicationServer-Vt", 310),
          ("enhancedRemoteFailureIndicationConnectivity-Vt", 311),
          ("enhancedRemoteFailureIndicationPayload-Vt", 312),
          ("sonetLOP-Vt", 313),
          ("sonetAIS-Vt", 314),
          ("sonetRFI-Vt", 315),
          ("sonetPLM-Vt", 316),
          ("sonetUNEQ-Vt", 317),
          ("sonetCV-Vt", 318),
          ("sonetES-Vt", 319),
          ("sonetSES-Vt", 320),
          ("sonetUAS-Vt", 321),
          ("sonetFC-Vt", 322),
          ("linenitSyncMismatchOnRap-A", 323),
          ("linenitSyncMismatchOnRap-B", 324),
          ("isdnAlarmIndicationBit", 325),
          ("farEndLossOfSynchronizationWord", 326),
          ("imaIcpViolation", 327),
          ("imaSes", 328),
          ("imaUas", 329),
          ("imaTxUus", 330),
          ("imaRxUus", 331),
          ("imaTxFc", 332),
          ("imaRxFc", 333),
          ("imaTxStuff", 334),
          ("imaRxStuff", 335),
          ("imaOif", 336),
          ("imaGrpUas", 337),
          ("imaGrpFc", 338),
          ("xLanOpen-Ethernet", 339),
          ("unused2", 340),
          ("xLanMismatch-Ethernet", 341),
          ("xLanCollision-Ethernet", 342),
          ("lanSwitchLost-Ethernet", 343),
          ("ethernetEnabled", 344),
          ("ethernetDisabled", 345),
          ("ethernetDataFlowing", 346),
          ("linkCommunicationDown", 347),
          ("hardwareNotCompatibleWithSoftware", 348),
          ("fileSystemError", 349),
          ("switchInitiatedLoopbackGR8", 350),
          ("linkAlarmGR8", 351),
          ("dataLinkAlamrGR8", 352),
          ("exceedShelfPowerLimit", 353),
          ("internalARSenumerationAlarmGR8link", 354),
          ("timingError", 355),
          ("ampCopyInProgress", 356),
          ("ampCopyNoAdminMaster", 357),
          ("ampCopyAdminMasterOutOfRevosion", 358),
          ("ampCopyAdminMasterCannotBeReached", 359),
          ("ampCopyMultipleRequests", 360),
          ("ampCopyFileSystemFail", 361),
          ("ampCopyFileTransferFailed", 362),
          ("ampCopyAdminMasterLostCommunication", 363),
          ("ampCopyFailed", 364),
          ("hdslSNRmarginAlarm", 365),
          ("hdslLoopAttenuationAlarm", 366),
          ("hdslLossOfSynchronizationWord", 367),
          ("duplicateShelfId", 368),
          ("clockFailure", 369),
          ("lossOfSignalForPPL", 370),
          ("eventLogInitialization", 371),
          ("eventLogBuffer90PercentFull", 372),
          ("eventLogBufferOverflow", 373),
          ("tcaLogInitialization", 374),
          ("tcaLogBuffer90PercentFull", 375),
          ("tcaLogBufferOverflow", 376),
          ("hdslSnrMarginLoopAlarm2Customer", 377),
          ("hdslLoopAttenuationLoop2Customer", 378),
          ("hsldLoswLoop2Customer", 379),
          ("hdslTcaRetrainCountLoop1", 380),
          ("hdslTcaRetrainCountLoop2", 381),
          ("hdslTcaCodingViolationLoop1", 382),
          ("hdslTcaCodingViolationLoop2", 383),
          ("hdslTcaErroredSecondsLineLoop1", 384),
          ("hdslTcaErroredSecondsLineLoop2", 385),
          ("hsldSeverelyErroredSecondsLineLoop1", 386),
          ("hsldSeverelyErroredSecondsLineLoop2", 387),
          ("hdslTcaUnavaliableSecondsLineLoop1", 388),
          ("hdslTcaUnavaliableSecondsLineLoop2", 389),
          ("hdslLossOfSynchWordLoop1Network", 390),
          ("hdslLossOfSynchWordLoop2Network", 391),
          ("hdslSnrMarginLoop1Network", 392),
          ("hdslSnrMarginLoop2Network", 393),
          ("hdlsLoopAttenuationAlarmLoop1Network", 394),
          ("hdlsLoopAttenuationAlarmLoop2Network", 395),
          ("equiptmentCommunicationFailureRap", 396),
          ("ethernetXLanOpenFarEnd", 397),
          ("ethernetLSwitchHasNoVti", 398),
          ("ethernetLSwitchVtiHasNoCrs", 399),
          ("ethernetLSwitchVtiCrsErr", 400),
          ("ethernetLSwitchEluCrsErr", 401),
          ("hdslLossOfSynchWordLoop1NeFe", 402),
          ("hdslLossOfSynchWordLoop2NeFe", 403),
          ("hdslSnrMarginAlarmLoop1NeFe", 404),
          ("hdslSnrMarginAlarmLoop2NeFe", 405),
          ("hdslLoopAttenuationAlarmLoop1NeFe", 406),
          ("hdslLoopAttenuationAlarmLoop2NeFe", 407),
          ("inbandLoopbackFacility", 408),
          ("inbandLoopbackPayload", 409),
          ("inbandLoopbackTerminal", 410),
          ("ethPortMappedToLSwitch", 411),
          ("logicalSwitchPortFail", 412),
          ("equipmentDegraded", 413),
          ("threshholdPeruIngress", 414),
          ("threshholdPeruEgress", 415),
          ("thresholdBandwidthConstraintRx", 416),
          ("thresholdBandwidthConstraintTx", 417),
          ("bwcIdRxLimitExceeded", 418),
          ("bwcIdTxLimitExceeded", 419),
          ("videoVcMismatch", 420),
          ("ipAddrInUse", 421),
          ("channelControlCommLinkDown", 422),
          ("vodEqressCommLinkDown", 423),
          ("vodIngressCommLinkDown", 424),
          ("vodServerCommLinkDown", 425),
          ("vodFlowFailure", 426),
          ("connectionDbMismatch", 427),
          ("videoXConnectionMismatch", 428),
          ("videoParameterMismatch", 429),
          ("constraintFeMismatch", 430),
          ("pplMismatch", 431),
          ("videoAuditTimeout", 432),
          ("equipEventReport", 433),
          ("ontStartUpFailure", 434),
          ("ontPloamCellLoss", 435),
          ("ontCellPhaseError", 436),
          ("ontRemoreErrorInd", 437),
          ("ontLossOfAck", 438),
          ("ontDefectFailure", 439),
          ("ontMessageError", 440),
          ("ontReceiveAlarmInhibit", 441),
          ("ontLinkMismatch", 442),
          ("ontMissing", 443),
          ("ontBatteryMissing", 444),
          ("ontCesDs1PortOutOfFrame", 445),
          ("ontCesSDs1PortBackAIS", 446),
          ("ontCesDs1ReceiveError", 447),
          ("ontCesDs1PortInfo0", 448),
          ("ontBadPassword", 449),
          ("atmMonLoss", 450),
          ("trafficThreshold", 451),
          ("callProcLuDown", 452),
          ("oltBlocked", 453),
          ("ampOltDownLoadOntSwFail", 454),
          ("ontDownLoadFail", 455),
          ("oltProvNoAmp", 456),
          ("fttpTransmissionFail", 457),
          ("ontEquipError", 458),
          ("ontSelfTestFail", 459),
          ("noMediaGatewayControllerComm", 460),
          ("mediaGatewayController1Comm", 461),
          ("mediaGatewayController2Comm", 462),
          ("sfpHighTxBias", 463),
          ("sfpLowTxBias", 464),
          ("sfpHighTxPwr", 465),
          ("sfpLowTxPwr", 466),
          ("sfpHighRxPwr", 467),
          ("sfpLowRxPwr", 468),
          ("sfpTxFault", 469),
          ("sfpHighVcc", 470),
          ("sfpLowVcc", 471),
          ("noRadServ", 472),
          ("noRadAmp", 473),
          ("sshFail", 474),
          ("radServFail", 475),
          ("radAmpFail", 476),
          ("maxProvClose", 477),
          ("maxProvHere", 478),
          ("tmgDD1SwToInt", 479),
          ("tmgDD1SwToPri", 480),
          ("tmgDD1SwToSec", 481),
          ("tmgDD1SyncOos", 482),
          ("tmgDD1SyncPri", 483),
          ("tmgDD1SyncSec", 484),
          ("tmgDD1ManSwToInt", 485),
          ("tmgDD1ManSwToPri", 486),
          ("tmgDD1ManSwToSec", 487),
          ("tmgDD1FrcdSwToInt", 488),
          ("tmgDD1FrcdSwToPri", 489),
          ("tmgDD1FrcdSwToSec", 490),
          ("swDlInProg", 491),
          ("mgmtIpAddr", 492),
          ("shelfArrival", 493),
          ("vrpFreqMismatch", 494),
          ("vrpNotSupported", 495),
          ("draLeaseRscLow", 496),
          ("draNoLeaseRsc", 497),
          ("vidSubNoBw", 498),
          ("appProcErr", 499),
          ("tLosc", 500),
          ("crprDown", 501),
          ("trafficImpairment", 502),
          ("draAssgIPDup", 503),
          ("dhcpIntfAddr", 504),
          ("dhcpIPAssnStaticHost", 505),
          ("dhcpMacAssnStaticHost", 506),
          ("rstpRecvdStpFrame", 507),
          ("seltInPrg", 508),
          ("protnUnitDown", 509),
          ("sfpMissing", 510),
          ("sfpNotSupported", 511),
          ("invVpiVci", 512),
          ("guaranteedTrafficCellLoss", 513),
          ("tBIP8Ont", 514),
          ("tBesOnt", 515),
          ("tSesOnt", 516),
          ("tUasOnt", 517),
          ("tMissOnt", 518),
          ("tMesOnt", 519),
          ("tEthFcs", 520),
          ("tEthEcc", 521),
          ("tEthLcc", 522),
          ("tEthFtl", 523),
          ("tEthBor", 524),
          ("tEthBot", 525),
          ("tEthSqe", 526),
          ("tEthDtc", 527),
          ("tEthAec", 528),
          ("tEthImr", 529),
          ("linkMm", 530),
          ("laserEndOfLife", 531),
          ("pktSlotMm", 532),
          ("vicVcThresh", 533),
          ("sipInvCfg", 534),
          ("insuffLineBw", 535),
          ("pppoeInsufNpRsc", 536),
          ("dhcpInsufNpRsc", 537),
          ("lpdInsufNpRsc", 538),
          ("luSlotMm", 539),
          ("dupIpAddr", 540),
          ("vrBadStaticHost", 541),
          ("vbPortDosDisable", 542),
          ("dupVidVb", 543),
          ("vbBadStaticMac", 544),
          ("dupSipVcgAid", 545),
          ("memDown", 546),
          ("minRateFailUs", 547),
          ("minRateFailDs", 548),
          ("maxRateFailUs", 549),
          ("maxRateFailDs", 550),
          ("diffDlyFailUs", 551),
          ("diffDlyFailDs", 552),
          ("linkRateFailUs", 553),
          ("linkRateFailDs", 554),
          ("thresholdUasG", 555),
          ("thresholdFcG", 556),
          ("thresholdMdsrFsG", 557),
          ("thresholdMusrFsG", 558),
          ("codecThermalFail", 559),
          ("bwPoolMm", 560),
          ("vlanModeMm", 561),
          ("vidBwcLinkMm", 562),
          ("vidSrcBwMm", 563),
          ("vidSrcBwThresh", 564),
          ("vidChanDropped", 565),
          ("dhcpSvrIpExhaust", 566),
          ("epkampFailure", 567),
          ("tEcL", 568),
          ("erpsActingMaster", 569),
          ("erpsSecondMaster", 570),
          ("erpsIsolatedNode", 571),
          ("erpsRingDown", 572),
          ("rstpMultPrimary", 573),
          ("rstpMultSecondary", 574),
          ("rstpNoPrimary", 575),
          ("rstpNoSecondary", 576),
          ("ampMaxCapClose", 577),
          ("ampMaxCapHere", 578),
          ("erpsRingPortDown", 579),
          ("ftpNotProv", 580),
          ("ftpDown", 581),
          ("ftpRelMissing", 582),
          ("ftpRelBadFiles", 583),
          ("ftpNotReady", 584),
          ("unrecognizedSfp", 585),
          ("moduleFault", 586),
          ("badInventory", 587),
          ("lacpPortFault", 588),
          ("vidChanFrameLoss", 589),
          ("noVoiceProt", 590),
          ("eqptImgUnavail", 591),
          ("lagDown", 592),
          ("vlanIfInsufNpRsc", 593),
          ("maxNumVidChans", 594),
          ("ontUaPresent", 595),
          ("ontUaMissing", 596),
          ("ontUaLinked", 597),
          ("tMissPkt", 598),
          ("tJBufUr", 599),
          ("tPktLosR", 600),
          ("misX", 601),
          ("mfPkts", 602),
          ("insuffNwQos", 603),
          ("tMfPkts", 604),
          ("linkTcModeMismatch", 605),
          ("tftpFail", 606),
          ("vidBwPoolMn", 607),
          ("unknown", 608))
    )



class CsAB(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csa", 1),
          ("csb", 2))
    )



class DesiredState(TextualConvention, Integer32):
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
        *(("is", 1),
          ("admin", 2),
          ("maint", 3))
    )



class Dirn(TextualConvention, Integer32):
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
        *(("trmt", 1),
          ("rcv", 2),
          ("bth", 3),
          ("tdtc", 4),
          ("tdtn", 5),
          ("na", 6))
    )



class Gos(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )



class INum15Min(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class INum24Hr(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )



class LinkId(TextualConvention, Integer32):
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
        *(("tl1", 1),
          ("web", 2),
          ("snmp", 3),
          ("gr303", 4))
    )



class LogBuffer(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )



class MonPer(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("history", 2))
    )



class Pid(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 10),
    )



class Pst(TextualConvention, Integer32):
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
        *(("isNr", 1),
          ("oosMa", 2),
          ("oosAu", 3),
          ("oosAuma", 4))
    )



class RowType(TextualConvention, Integer32):
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("aco", 1),
          ("adsl", 2),
          ("com", 3),
          ("cont", 4),
          ("crv", 5),
          ("ds1", 6),
          ("env", 7),
          ("eqpt", 8),
          ("gr303", 9),
          ("line", 10),
          ("link", 11),
          ("log", 12),
          ("mem", 13),
          ("oc3", 14),
          ("oc12", 15),
          ("oc48", 16),
          ("oc192", 17),
          ("path", 18),
          ("phys", 19),
          ("section", 20),
          ("secu", 21),
          ("secuDflt", 22),
          ("shelf", 23),
          ("sts1", 24),
          ("sts3", 25),
          ("sts12", 26),
          ("sts48", 27),
          ("sts192", 28),
          ("sys", 29),
          ("t0", 30),
          ("t1", 31),
          ("t3", 32),
          ("tgrp", 33),
          ("tmg", 34),
          ("upgrd", 35),
          ("user", 36),
          ("vc", 37),
          ("vp", 38))
    )



class SrvEffect(TextualConvention, Integer32):
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
        *(("nonServiceAffecting", 1),
          ("serviceAffecting", 2),
          ("unknown", 3))
    )



class ObjState(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bitOos", 0),
          ("bitMa", 1),
          ("bitAu", 2),
          ("bitMt", 3),
          ("bitAins", 4),
          ("bitAda", 5),
          ("bitFaf", 6),
          ("bitFlt", 7),
          ("bitLpbk", 8),
          ("bitMea", 9),
          ("bitMonPm", 10),
          ("bitNbk", 11),
          ("bitPwr", 12),
          ("bitRdld", 13),
          ("bitSdee", 14),
          ("bitSgeo", 15),
          ("bitStbyc", 16),
          ("bitStbyh", 17),
          ("bitStbyi", 18),
          ("bitStbys", 19),
          ("bitSwtch", 20),
          ("bitTs", 21),
          ("bitUasSw", 22),
          ("bitUeq", 23),
          ("bitWrk", 24),
          ("bitPua", 25),
          ("bitPri", 26),
          ("bitIdle", 27),
          ("bitDgn", 28),
          ("bitCrs", 29),
          ("bitSffp", 30),
          ("bitIsNr", 31))
    )


class ObjClass(TextualConvention, Integer32):
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
              50)
        )
    )
    namedValues = NamedValues(
        *(("eqpt", 1),
          ("ifDs0Port", 2),
          ("ifDs1Port", 3),
          ("ifDs3Port", 4),
          ("ifAdslPort", 5),
          ("ifOc3Port", 6),
          ("ifOc12Port", 7),
          ("ifOc48Port", 8),
          ("ifSts1Fac", 9),
          ("ifSts3cFac", 10),
          ("ifSts12cFac", 11),
          ("ifSts48cFac", 12),
          ("envContact", 13),
          ("extControl", 14),
          ("aco", 15),
          ("igDs1", 16),
          ("igDataLink", 17),
          ("log", 18),
          ("tmg", 19),
          ("shelf", 20),
          ("node", 21),
          ("imaGroup", 22),
          ("imaLink", 23),
          ("ifEthPort", 24),
          ("ifPseudoPort", 25),
          ("security", 26),
          ("pathProtectionLabel", 27),
          ("logicalSwitchPort", 28),
          ("bwConstrPort", 29),
          ("bwConstrSts", 30),
          ("ont", 31),
          ("ifOntDs0Port", 32),
          ("ifOntDs1Port", 33),
          ("ifOntEthPort", 34),
          ("ifOntRfVideoPort", 35),
          ("ifOntAvoPort", 36),
          ("ifVDs1Port", 37),
          ("vcg", 38),
          ("ifHdslPort", 39),
          ("radius", 40),
          ("ifPonPort", 41),
          ("ifVr", 42),
          ("ifVb", 43),
          ("ifXdslGrp", 44),
          ("vidSrc", 45),
          ("lag", 46),
          ("erps", 47),
          ("shelfIdx", 48),
          ("ifAtmRscPort", 49),
          ("unknown", 50))
    )



class ObjectIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class AlarmCntIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CondCntIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class Tl1Aid(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 30),
    )



class ShelfId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 4101),
    )



class MonVal(TextualConvention, Integer32):
    status = "current"


class ThLev(TextualConvention, Integer32):
    status = "current"


class TmPer(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pm15Min", 1),
          ("pm24Hr", 2),
          ("na", 255))
    )



class Uid(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )



class DatalinkType(TextualConvention, Integer32):
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
        *(("tmc", 1),
          ("eoc", 2),
          ("lineDcc", 3),
          ("sectionDcc", 4),
          ("internal", 5))
    )



class DatalinkPair(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class Facility(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )



class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class OcWidth(TextualConvention, Integer32):
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
        *(("oc3", 1),
          ("oc12", 2),
          ("oc48", 3),
          ("oc192", 4))
    )



class StsWidth(TextualConvention, Integer32):
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
        *(("sts1", 1),
          ("sts3c", 2),
          ("sts12c", 3),
          ("sts48c", 4),
          ("sts192c", 5))
    )



class TraceLevel(TextualConvention, Integer32):
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
        *(("traceLevel1", 1),
          ("traceLevel2", 2),
          ("traceLevel3", 3),
          ("traceLevel4", 4),
          ("traceLevel5", 5),
          ("default", 6))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-TC",
    **{"BpId": BpId,
       "Clei": Clei,
       "AlarmTransition": AlarmTransition,
       "AlarmSeverity": AlarmSeverity,
       "CondSeverity": CondSeverity,
       "CondLocation": CondLocation,
       "CondState": CondState,
       "CondType": CondType,
       "CsAB": CsAB,
       "DesiredState": DesiredState,
       "Dirn": Dirn,
       "Gos": Gos,
       "INum15Min": INum15Min,
       "INum24Hr": INum24Hr,
       "LinkId": LinkId,
       "LogBuffer": LogBuffer,
       "MonPer": MonPer,
       "Pid": Pid,
       "Pst": Pst,
       "RowType": RowType,
       "SrvEffect": SrvEffect,
       "ObjState": ObjState,
       "ObjClass": ObjClass,
       "ObjectIndex": ObjectIndex,
       "AlarmCntIndex": AlarmCntIndex,
       "CondCntIndex": CondCntIndex,
       "Tl1Aid": Tl1Aid,
       "ShelfId": ShelfId,
       "MonVal": MonVal,
       "ThLev": ThLev,
       "TmPer": TmPer,
       "Uid": Uid,
       "DatalinkType": DatalinkType,
       "DatalinkPair": DatalinkPair,
       "Facility": Facility,
       "InterfaceIndex": InterfaceIndex,
       "OcWidth": OcWidth,
       "StsWidth": StsWidth,
       "TraceLevel": TraceLevel}
)
