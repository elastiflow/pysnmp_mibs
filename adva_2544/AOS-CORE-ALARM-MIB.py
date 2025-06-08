# SNMP MIB module (AOS-CORE-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/AOS-CORE-ALARM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:56 2025
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

(aosCommon,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "aosCommon")

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

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

aosCoreAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    aosCoreAlarmMIB.setRevisions(
        ("2015-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ServiceEffect(TextualConvention, Integer32):
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
        *(("none", 0),
          ("nonServiceAffecting", 1),
          ("serviceAffecting", 2))
    )



class NotificationCode(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("notAlarmed", 5),
          ("notReported", 6),
          ("clear", 7))
    )



class Direction(TextualConvention, Integer32):
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
        *(("noDirection", 1),
          ("transmit", 2),
          ("receive", 3),
          ("biDirectional", 4))
    )



class Location(TextualConvention, Integer32):
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
        *(("nearEnd", 1),
          ("farEnd", 2),
          ("noLocation", 3))
    )



class ConditionType(TextualConvention, Integer32):
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
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              400,
              401,
              410,
              411,
              412,
              413,
              414,
              550,
              551,
              552,
              553,
              554,
              555,
              570,
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
              616,
              617,
              618,
              619,
              620,
              621,
              622,
              623,
              650,
              651,
              652,
              653,
              654,
              655,
              656,
              657,
              658,
              659,
              660,
              661,
              670,
              680,
              690,
              1000,
              1020,
              1021,
              1022,
              1500,
              1501,
              1502,
              1503)
        )
    )
    namedValues = NamedValues(
        *(("voltAnr", 1),
          ("removed", 2),
          ("fault", 3),
          ("mea", 4),
          ("incompatibleHardware", 5),
          ("meaApprove", 6),
          ("meaAccept", 7),
          ("meaCapability", 8),
          ("fwPackageMismatch", 9),
          ("fwReboot", 10),
          ("backplaneCommFail", 11),
          ("meaPhys", 12),
          ("meaDiffer", 13),
          ("psuRedundancyMismatch", 14),
          ("insufficientPower", 15),
          ("backplaneEepromCommFail", 16),
          ("powerFeedUndervoltage", 17),
          ("powerFeedAFail", 18),
          ("powerFeedBFail", 19),
          ("outPowerFail", 20),
          ("tcaOutCurrentHigh", 21),
          ("tcaPowerConsumptionHigh", 22),
          ("tcaTempHigh", 23),
          ("tcaTempLow", 24),
          ("lossOfSignal", 25),
          ("laserFail", 26),
          ("forceLaserOn", 27),
          ("forceTransmitShutdown", 28),
          ("lossOfClock", 29),
          ("lossOfOverhead", 30),
          ("lossOfPrbsPattern", 31),
          ("laserOnDelay", 32),
          ("autoPowerReduction", 33),
          ("supportingEqptFailure", 35),
          ("payloadMissingIndication", 36),
          ("lossOfSignalPayload", 37),
          ("tcaOptRcvPowerHigh", 38),
          ("tcaOptTrmtPowerHigh", 39),
          ("tcaOptLaserBiasCurrHigh", 40),
          ("laserTempHigh", 41),
          ("tcaOptRcvPowerLow", 42),
          ("tcaOptTrmtPowerLow", 43),
          ("laserTempLow", 44),
          ("alarmIndicatorSigDefect", 45),
          ("backwardDefectIndicator", 46),
          ("backwardDefectIndicatorPayload", 47),
          ("backwardDefectIndicatorOverhead", 48),
          ("clientSigFail", 49),
          ("degradedSig", 50),
          ("forwardDefectIndicatorPayload", 51),
          ("forwardDefectIndicatorOverhead", 52),
          ("incomingAlignError", 53),
          ("backwardIncomingAlignError", 54),
          ("lossOfFrame", 55),
          ("lossOfMultiframe", 56),
          ("lossOfFrameAndMultiframe", 57),
          ("lockedCondition", 58),
          ("lossOfTandemConn", 59),
          ("multiplexStructIdentifierMismatch", 60),
          ("openConnIndication", 61),
          ("payloadMismatch", 62),
          ("serverSigFail", 63),
          ("serverSigFailPayload", 64),
          ("serverSigFailOverhead", 65),
          ("trailSigFail", 66),
          ("trailSigFailPayload", 67),
          ("trailSigFailOverhead", 68),
          ("trailTraceIdentifierMismatch", 69),
          ("lossOfSignalOverhead", 70),
          ("pumpEndOfLife", 71),
          ("midstageLossHigh", 72),
          ("ampControlAbnormal", 73),
          ("autoPowerShutdown", 74),
          ("voaControlFail", 75),
          ("gainControlFail", 76),
          ("tiltControlFail", 77),
          ("optLimitHt", 78),
          ("optLimitHtEx", 79),
          ("oscLaserFail", 80),
          ("oscPower", 81),
          ("lossOfSigMidstage", 82),
          ("lossOfOpuMultiframeId", 83),
          ("tcaUnavailableSecondsHigh", 84),
          ("tcaErroredSecondHigh", 85),
          ("tcaSeverlyErroredSecondHigh", 86),
          ("tcaBackgroundBlockErrorsHigh", 87),
          ("tcaOscOptLaserBiasCurrHigh", 88),
          ("tcaOscLaserTempHigh", 89),
          ("tcaOscOptRcvPowerHigh", 90),
          ("tcaOscOptTrmtPowerHigh", 91),
          ("tcaSesPayloadHigh", 92),
          ("tcaSesOverheadHigh", 93),
          ("tcaUasPayloadHigh", 94),
          ("tcaUasOverheadHigh", 95),
          ("tcaOscLaserTempLow", 96),
          ("tcaOscOptRcvPowerLow", 97),
          ("tcaOscOptTrmtPowerLow", 98),
          ("lossOfModemSync", 99),
          ("lossOfCouplingAlignment", 100),
          ("autoCdcFail", 101),
          ("tcaDiffGroupDelayHigh", 102),
          ("tcaCdcHigh", 103),
          ("tcaCarrierFreqOffsetHigh", 104),
          ("tcaSnrLow", 105),
          ("tcaCdcLow", 106),
          ("tcaCarrierFreqOffsetLow", 107),
          ("lnkFail", 108),
          ("lnkCblFault", 109),
          ("lnkCblRmv", 110),
          ("lnkAutonegFail", 111),
          ("lnkNoRootCause", 112),
          ("fendDupModeUnknown", 113),
          ("jabThldExceed", 114),
          ("lossOfSync", 115),
          ("rxLocalFault", 116),
          ("txLocalFault", 117),
          ("lossOfBlockLock", 118),
          ("hiBer", 119),
          ("autoCdcInProgress", 120),
          ("lossOfBlockLockLane", 121),
          ("lossOfLaneAlgnMarkLane", 122),
          ("lnkDownDeact", 123),
          ("negBwExceed", 124),
          ("rxSsf", 125),
          ("txSsf", 126),
          ("outputOvercurrent", 127),
          ("tcaOutputPowerHigh", 128),
          ("lossOfAlignment", 129),
          ("ntpServerUnavailable", 130),
          ("tunedFrequencyMismatch", 131),
          ("temperatureHigh", 133),
          ("temperatureLow", 134),
          ("manifestMismatch", 135),
          ("manifestIncomplete", 136),
          ("laserBiasCurrentAbnormal", 137),
          ("lossOfTrafficAfterFirmwareActivation", 138),
          ("softwareVersionMismatch", 139),
          ("fanFault", 140),
          ("portConfigMismatch", 141),
          ("licenseServerDisconnect", 142),
          ("hwResourceUnavailableRecoverable", 143),
          ("licenseInvalid", 144),
          ("ssdWearoutLevelWarning", 145),
          ("licenseExpire", 146),
          ("databaseMismatch", 147),
          ("licenseMissing", 148),
          ("licenseOverdraft", 149),
          ("cryptoPasswordMissing", 150),
          ("vmResumeFailed", 151),
          ("keyExchangeAuthMissing", 152),
          ("keyLifetimeExpired", 153),
          ("tamperDetected", 154),
          ("selfTestFailed", 155),
          ("cryptoTemporaryLockout", 156),
          ("batteryLow", 157),
          ("selfTestInProgress", 158),
          ("vmCrashed", 159),
          ("keyExchangeDegrade", 160),
          ("internalEncryptionFailed", 161),
          ("keyExchangeInProgress", 162),
          ("keyExchangeChannelFail", 163),
          ("terminalLoopbackInProgress", 164),
          ("localOscBiarCurAbnormal", 165),
          ("licenseFileMissing", 166),
          ("licenseServerConfigMissing", 167),
          ("hardwareBusy", 168),
          ("fanFilterReplace", 169),
          ("rebootInProgress", 170),
          ("prbsDetectionInProgress", 171),
          ("tcaOutOfFrameSecondHigh", 172),
          ("msLineAis", 173),
          ("localOscTemperatureLow", 174),
          ("localOscTemperatureHigh", 175),
          ("facilityLoopbackInProgress", 176),
          ("prbsGenerationInProgress", 177),
          ("transmitSignalFail", 178),
          ("loopbackActive", 179),
          ("meaPhyChanged", 180),
          ("licenseBackupServerDisconnect", 181),
          ("callHomeServerUnreachable", 182),
          ("timinglicensemissing", 183),
          ("eomplslicensemissing", 184),
          ("fullcapacitylicensemissing", 185),
          ("elephantflowlicensemissing", 186),
          ("snmpdyinggasp", 187),
          ("snmpdyinggasphostresourcesbusy", 188),
          ("snmpdyinggasphostunreachable", 189),
          ("controlplanelicensemissing", 190),
          ("l3licensemissing", 191),
          ("coldrebootrequired", 192),
          ("efmRemoteDyingGasp", 227),
          ("efmFail", 228),
          ("efmRemoteCriticalEvent", 229),
          ("efmRemoteLinkDown", 230),
          ("efmRemoteLoopbackFail", 231),
          ("efmRemoteLoopbackRequest", 232),
          ("tcaQFactorLow", 233),
          ("tcaPolarizationDependentLHigh", 234),
          ("tcaStateOfPolarizationChangeRateHigh", 235),
          ("tcaOpticalSnrLow", 236),
          ("srvDiscarded", 300),
          ("bwExceedPortSpeed", 301),
          ("meaPortalAddress", 302),
          ("meaPortalPri", 303),
          ("meaThreePortal", 304),
          ("meaPortalSysNumber", 305),
          ("meaActorAdminKey", 306),
          ("meaPortDigest", 307),
          ("meaGatewayDigest", 308),
          ("ztpInProgress", 400),
          ("ztpFailed", 401),
          ("cryptoConfigMismatch", 410),
          ("keyExchangeConfigMismatch", 411),
          ("fingerprintAuthMissing", 412),
          ("cryptoConfigError", 413),
          ("keyExchangeAuthMismatch", 414),
          ("crossConnectCCM", 550),
          ("errorCCM", 551),
          ("someRemoteMEPCCM", 552),
          ("someMACstatus", 553),
          ("someRDI", 554),
          ("ethAIS", 555),
          ("remoteInitSAT", 570),
          ("erpFoPPM", 580),
          ("erpFoPTO", 581),
          ("erpBlockPort0RPL", 582),
          ("erpBlockPort0SF", 583),
          ("erpBlockPort0MS", 584),
          ("erpBlockPort0FS", 585),
          ("erpBlockPort0WTR", 586),
          ("erpBlockPort1RPL", 587),
          ("erpBlockPort1SF", 588),
          ("erpBlockPort1MS", 589),
          ("erpBlockPort1FS", 590),
          ("erpBlockPort1WTR", 591),
          ("avgHoldoverNotReady", 600),
          ("freerun", 601),
          ("fastAccquisition", 602),
          ("holdover", 603),
          ("lossOfLock", 604),
          ("allSyncRefFail", 605),
          ("syncRefLockOut", 606),
          ("syncRefFS", 607),
          ("syncRefMS", 608),
          ("syncRefWTR", 609),
          ("syncRefSW", 610),
          ("syncRefFail", 611),
          ("syncRefFreqOffset", 612),
          ("ais", 616),
          ("bitsLossOfFrame", 617),
          ("qlMismatch", 618),
          ("qlInvalid", 619),
          ("esmcFail", 620),
          ("linkdownMasterSlaveCfg", 621),
          ("autoNegoMasterSlaveCfg", 622),
          ("squelched", 623),
          ("ptpFreerun", 650),
          ("ptpTimeFreeRun", 651),
          ("ptpFreqHoldover", 652),
          ("ptpTimeHoldover", 653),
          ("ptpFreqNotTraceable", 654),
          ("ptpTimeNotTraceable", 655),
          ("ptpAnnounceTimeout", 656),
          ("ptpSyncTimeout", 657),
          ("ptpDelayrespTimeout", 658),
          ("ptpMultiplePeers", 659),
          ("ptpWrongDomain", 660),
          ("ptpNoTrafficFP", 661),
          ("bgpNbrLinkDown", 670),
          ("paAuthFail", 680),
          ("noMGroupRes", 690),
          ("eomplsDstUnresovled", 1000),
          ("trafficArpTableFull", 1020),
          ("noRouteResources", 1021),
          ("ipAddressConflict", 1022),
          ("ntpLossOfServer", 1500),
          ("remoteServerUnreachable", 1501),
          ("sysLogServerUnreachable", 1502),
          ("targetAddressUnreachable", 1503))
    )



class ConditionDescr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class ConditionEntityTranslation(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_AlarmObjects_ObjectIdentity = ObjectIdentity
alarmObjects = _AlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1)
)
_AosCoreAlarmTable_Object = MibTable
aosCoreAlarmTable = _AosCoreAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aosCoreAlarmTable.setStatus("current")
_AosCoreAlarmEntry_Object = MibTableRow
aosCoreAlarmEntry = _AosCoreAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1)
)
aosCoreAlarmEntry.setIndexNames(
    (0, "AOS-CORE-ALARM-MIB", "aosCoreAlarmIndex"),
)
if mibBuilder.loadTexts:
    aosCoreAlarmEntry.setStatus("current")
_AosCoreAlarmIndex_Type = Integer32
_AosCoreAlarmIndex_Object = MibTableColumn
aosCoreAlarmIndex = _AosCoreAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 1),
    _AosCoreAlarmIndex_Type()
)
aosCoreAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aosCoreAlarmIndex.setStatus("current")
_AosCoreAlarmConditionType_Type = ConditionType
_AosCoreAlarmConditionType_Object = MibTableColumn
aosCoreAlarmConditionType = _AosCoreAlarmConditionType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 2),
    _AosCoreAlarmConditionType_Type()
)
aosCoreAlarmConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmConditionType.setStatus("current")
_AosCoreAlarmEntityTranslation_Type = ConditionEntityTranslation
_AosCoreAlarmEntityTranslation_Object = MibTableColumn
aosCoreAlarmEntityTranslation = _AosCoreAlarmEntityTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 3),
    _AosCoreAlarmEntityTranslation_Type()
)
aosCoreAlarmEntityTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmEntityTranslation.setStatus("current")
_AosCoreAlarmEntity_Type = RowPointer
_AosCoreAlarmEntity_Object = MibTableColumn
aosCoreAlarmEntity = _AosCoreAlarmEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 4),
    _AosCoreAlarmEntity_Type()
)
aosCoreAlarmEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmEntity.setStatus("current")
_AosCoreAlarmCondDescr_Type = ConditionDescr
_AosCoreAlarmCondDescr_Object = MibTableColumn
aosCoreAlarmCondDescr = _AosCoreAlarmCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 5),
    _AosCoreAlarmCondDescr_Type()
)
aosCoreAlarmCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmCondDescr.setStatus("current")
_AosCoreAlarmTimestamp_Type = DisplayString
_AosCoreAlarmTimestamp_Object = MibTableColumn
aosCoreAlarmTimestamp = _AosCoreAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 6),
    _AosCoreAlarmTimestamp_Type()
)
aosCoreAlarmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmTimestamp.setStatus("current")
_AosCoreAlarmDirection_Type = Direction
_AosCoreAlarmDirection_Object = MibTableColumn
aosCoreAlarmDirection = _AosCoreAlarmDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 7),
    _AosCoreAlarmDirection_Type()
)
aosCoreAlarmDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmDirection.setStatus("current")
_AosCoreAlarmLocation_Type = Location
_AosCoreAlarmLocation_Object = MibTableColumn
aosCoreAlarmLocation = _AosCoreAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 8),
    _AosCoreAlarmLocation_Type()
)
aosCoreAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmLocation.setStatus("current")
_AosCoreAlarmSrvEff_Type = ServiceEffect
_AosCoreAlarmSrvEff_Object = MibTableColumn
aosCoreAlarmSrvEff = _AosCoreAlarmSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 9),
    _AosCoreAlarmSrvEff_Type()
)
aosCoreAlarmSrvEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmSrvEff.setStatus("current")
_AosCoreAlarmNotifCode_Type = NotificationCode
_AosCoreAlarmNotifCode_Object = MibTableColumn
aosCoreAlarmNotifCode = _AosCoreAlarmNotifCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 10),
    _AosCoreAlarmNotifCode_Type()
)
aosCoreAlarmNotifCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmNotifCode.setStatus("current")
_AosCoreAlarmNotifTimestamp_Type = DisplayString
_AosCoreAlarmNotifTimestamp_Object = MibTableColumn
aosCoreAlarmNotifTimestamp = _AosCoreAlarmNotifTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 11),
    _AosCoreAlarmNotifTimestamp_Type()
)
aosCoreAlarmNotifTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmNotifTimestamp.setStatus("current")


class _AosCoreAlarmAdditionalInfo_Type(DisplayString):
    """Custom type aosCoreAlarmAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AosCoreAlarmAdditionalInfo_Type.__name__ = "DisplayString"
_AosCoreAlarmAdditionalInfo_Object = MibTableColumn
aosCoreAlarmAdditionalInfo = _AosCoreAlarmAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 1, 1, 1, 12),
    _AosCoreAlarmAdditionalInfo_Type()
)
aosCoreAlarmAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosCoreAlarmAdditionalInfo.setStatus("current")
_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 2)
)
_AlarmNotificationsPrefix_ObjectIdentity = ObjectIdentity
alarmNotificationsPrefix = _AlarmNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 2, 0)
)
_AlarmConformance_ObjectIdentity = ObjectIdentity
alarmConformance = _AlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3)
)
_AosCoreAlarmCompliances_ObjectIdentity = ObjectIdentity
aosCoreAlarmCompliances = _AosCoreAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 1)
)
_AosCoreAlarmGroups_ObjectIdentity = ObjectIdentity
aosCoreAlarmGroups = _AosCoreAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 2)
)

# Managed Objects groups

aosCoreAlarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 2, 1)
)
aosCoreAlarmObjectGroup.setObjects(
      *(("AOS-CORE-ALARM-MIB", "aosCoreAlarmIndex"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmConditionType"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmEntityTranslation"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmEntity"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmCondDescr"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmTimestamp"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmDirection"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmLocation"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmSrvEff"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifCode"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifTimestamp"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    aosCoreAlarmObjectGroup.setStatus("current")


# Notification objects

aosCoreAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 2, 0, 1)
)
aosCoreAlarmTrap.setObjects(
      *(("AOS-CORE-ALARM-MIB", "aosCoreAlarmIndex"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmConditionType"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmEntityTranslation"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmEntity"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmCondDescr"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmTimestamp"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmDirection"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmLocation"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmSrvEff"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifCode"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifTimestamp"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmAdditionalInfo"))
)
if mibBuilder.loadTexts:
    aosCoreAlarmTrap.setStatus(
        "current"
    )


# Notifications groups

aosCoreAlarmNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 2, 2)
)
aosCoreAlarmNotifGroup.setObjects(
    ("AOS-CORE-ALARM-MIB", "aosCoreAlarmTrap")
)
if mibBuilder.loadTexts:
    aosCoreAlarmNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aosCoreAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 1, 3, 1, 1)
)
aosCoreAlarmCompliance.setObjects(
      *(("AOS-CORE-ALARM-MIB", "aosCoreAlarmObjectGroup"),
        ("AOS-CORE-ALARM-MIB", "aosCoreAlarmNotifGroup"))
)
if mibBuilder.loadTexts:
    aosCoreAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AOS-CORE-ALARM-MIB",
    **{"ServiceEffect": ServiceEffect,
       "NotificationCode": NotificationCode,
       "Direction": Direction,
       "Location": Location,
       "ConditionType": ConditionType,
       "ConditionDescr": ConditionDescr,
       "ConditionEntityTranslation": ConditionEntityTranslation,
       "aosCoreAlarmMIB": aosCoreAlarmMIB,
       "alarmObjects": alarmObjects,
       "aosCoreAlarmTable": aosCoreAlarmTable,
       "aosCoreAlarmEntry": aosCoreAlarmEntry,
       "aosCoreAlarmIndex": aosCoreAlarmIndex,
       "aosCoreAlarmConditionType": aosCoreAlarmConditionType,
       "aosCoreAlarmEntityTranslation": aosCoreAlarmEntityTranslation,
       "aosCoreAlarmEntity": aosCoreAlarmEntity,
       "aosCoreAlarmCondDescr": aosCoreAlarmCondDescr,
       "aosCoreAlarmTimestamp": aosCoreAlarmTimestamp,
       "aosCoreAlarmDirection": aosCoreAlarmDirection,
       "aosCoreAlarmLocation": aosCoreAlarmLocation,
       "aosCoreAlarmSrvEff": aosCoreAlarmSrvEff,
       "aosCoreAlarmNotifCode": aosCoreAlarmNotifCode,
       "aosCoreAlarmNotifTimestamp": aosCoreAlarmNotifTimestamp,
       "aosCoreAlarmAdditionalInfo": aosCoreAlarmAdditionalInfo,
       "alarmNotifications": alarmNotifications,
       "alarmNotificationsPrefix": alarmNotificationsPrefix,
       "aosCoreAlarmTrap": aosCoreAlarmTrap,
       "alarmConformance": alarmConformance,
       "aosCoreAlarmCompliances": aosCoreAlarmCompliances,
       "aosCoreAlarmCompliance": aosCoreAlarmCompliance,
       "aosCoreAlarmGroups": aosCoreAlarmGroups,
       "aosCoreAlarmObjectGroup": aosCoreAlarmObjectGroup,
       "aosCoreAlarmNotifGroup": aosCoreAlarmNotifGroup}
)
