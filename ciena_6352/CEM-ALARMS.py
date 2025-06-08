# SNMP MIB module (CEM-ALARMS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-ALARMS.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

cnAlarmsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 11)
)
if mibBuilder.loadTexts:
    cnAlarmsModule.setRevisions(
        ("2002-02-20 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CnAlarmSeverityType(TextualConvention, Integer32):
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
        *(("cnCritical", 1),
          ("cnMajor", 2),
          ("cnMinor", 3),
          ("cnInformational", 4))
    )



class CnAlarmTableAudibilityConfigType(TextualConvention, Integer32):
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
        *(("cnAlarmAudible", 1),
          ("cnAlarmSilent", 2),
          ("cnAlarmAudibleNotApplicable", 3))
    )



class CnAlarmTableBufferConfigType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnLinearAlarmTable", 1),
          ("cnCircularAlarmTable", 2))
    )



class CnTableControlType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnClearTableCommand", 1),
          ("cnAcknowledgeAllAlarms", 2))
    )



class CnAlarmCodeType(TextualConvention, Integer32):
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
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              1014,
              1015,
              1016,
              1017,
              1018,
              1019,
              1020,
              1021,
              1022,
              1023,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1038,
              1039,
              1040,
              1041,
              2000,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              2011,
              2012,
              2013,
              2014,
              2015,
              2016,
              2017,
              2018,
              2019,
              2020,
              2021,
              2022,
              2023,
              2024,
              2025,
              2026,
              2027,
              2028,
              2029,
              2030,
              2031,
              2032,
              2033,
              2034,
              2035,
              2036,
              2037,
              2038,
              2039,
              2040,
              2041,
              2042,
              2043,
              3000,
              3001,
              3002,
              3003,
              3004,
              4000,
              4001,
              4002,
              4003,
              4004,
              4005,
              4006,
              4007,
              4008,
              4009,
              4010,
              4011,
              4012,
              4013,
              4014,
              4015,
              4016,
              4017,
              4018,
              4019,
              4020,
              4021,
              4022,
              4023,
              4024,
              4025,
              5000,
              5001,
              5002,
              5003,
              5004,
              5005,
              5006,
              5007,
              5008,
              5009,
              5010,
              5011,
              5012,
              5013,
              5014,
              5015,
              5016,
              6000,
              6001,
              6002,
              6003,
              6004,
              6005,
              6006,
              6007,
              6008,
              6009,
              6010,
              6011,
              6012,
              6013,
              6014,
              6015,
              6016,
              6017,
              6018,
              6019,
              6020,
              6021,
              6036,
              6037,
              6038,
              6039,
              6040,
              6041,
              6042,
              6043)
        )
    )
    namedValues = NamedValues(
        *(("cnAlarmDatabaseCorruption", 1),
          ("cnAlarmDatabaseReset", 2),
          ("cnAlarmNoActiveBankSet", 3),
          ("cnAlarmBootFromInactiveBank", 4),
          ("cnAlarmNoValidSoftwareLoad", 5),
          ("cnUnknownSoftwareLoadBank1", 6),
          ("cnUnknownSoftwareLoadBank2", 7),
          ("cnSoftwareUpgradeInProgress", 8),
          ("cnCardValidationFailure", 9),
          ("cnAlarmConfigInstallMismatch", 10),
          ("cnAlarmCardAppearance", 11),
          ("cnAlarmCardDisappearance", 12),
          ("cnAlarmSyncSourceTimingChanged", 13),
          ("cnAlarmPrimaryAndSecondarySyncSourceFailure", 14),
          ("cnAlarmPrimarySyncSourceTimingFailure", 15),
          ("cnAlarmSecondarySyncSourceTimingFailure", 16),
          ("cnAlarmForcedSyncSourceReference", 17),
          ("cnAlarmNoAvailableSystemTimingSource", 18),
          ("cnSystemTimingSourceFailure", 19),
          ("cnSyncSysTimingStateChange", 20),
          ("cnStratum3HoldOverTimeExceeded", 21),
          ("cnSyncStatusByteChanged", 22),
          ("cnAlarmProtectionSwitchPerformed", 23),
          ("cnAlarmProtectionSwitchFailed", 24),
          ("cnNoRedundancy", 25),
          ("cnAlarmCriticalAlarmBufferFull", 26),
          ("cnAlarmMajorAlarmBufferFull", 27),
          ("cnAlarmMinorAlarmBufferFull", 28),
          ("cnAlarmInformationalAlarmBufferFull", 29),
          ("cnAlarmDiagnosticFailure", 30),
          ("cnSoftwareUpgradeComplete", 31),
          ("cnProtGroupConfigMismatch", 32),
          ("cnForcedProtectionSwitch", 33),
          ("cnAlarmCutoffActivated", 34),
          ("cnUnknownAlarmCode", 35),
          ("cnAlarmTestCardLinkSanity", 36),
          ("cnAlarmSonetApsSwitchPerformed", 37),
          ("cnProtectionGroupDown", 38),
          ("cnAutoProtectionSwitch", 39),
          ("cnAlarmOverrideRevertiveSwitch", 40),
          ("cnAlarmSystemBoot", 41),
          ("cnAlarmProtectionGroupUp", 42),
          ("cnAlarmProtGrpSwMismatch", 43),
          ("cnAlarmProtGrpBackupCardHasLowerSwVersion", 44),
          ("cnAlarmProtGrpLocked", 45),
          ("cnAlarmDatabaseConversionFailure", 46),
          ("cnAlarmConfigFileTransferFailure", 47),
          ("cnAlarmFuncCodeMismatch", 48),
          ("cnAlarmATMPolicyMismatch", 49),
          ("cnAlarmATMGlobalTDMismatch", 50),
          ("cnBreakerFail", 1000),
          ("cnFanFailure", 1001),
          ("cnTalkBatteryFail", 1002),
          ("cnAlarmInput1", 1003),
          ("cnAlarmInput2", 1004),
          ("cnAlarmInput3", 1005),
          ("cnAlarmInput4", 1006),
          ("cnAlarmInput5", 1007),
          ("cnAlarmInput6", 1008),
          ("cnAlarmInput7", 1009),
          ("cnAlarmInput8", 1010),
          ("cnAlarmInput9", 1011),
          ("cnAlarmInput10", 1012),
          ("cnAlarmInput11", 1013),
          ("cnAlarmInput12", 1014),
          ("cnAlarmInput13", 1015),
          ("cnAlarmInput14", 1016),
          ("cnAlarmInput15", 1017),
          ("cnAlarmInput16", 1018),
          ("cnAlarmInput17", 1019),
          ("cnAlarmInput18", 1020),
          ("cnAlarmInput19", 1021),
          ("cnAlarmInput20", 1022),
          ("cnAlarmInput21", 1023),
          ("cnAlarmInput22", 1024),
          ("cnAlarmInput23", 1025),
          ("cnAlarmInput24", 1026),
          ("cnAlarmFanTrayDisAppearance", 1027),
          ("cnAlarmAuxShelfDisappearance", 1028),
          ("cnAlarmATCDisappearance", 1029),
          ("cnAlarmLEDTest", 1030),
          ("cnAlarmTBFDisappearance", 1031),
          ("cnAlarmTBFPairDisabled", 1032),
          ("cnAlarmTestCardDisappearance", 1033),
          ("cnAlarmHighTemperature", 1034),
          ("cnAlarmOnuPowerFailure", 1035),
          ("cnAlarmOnuInsufficientPower", 1036),
          ("cnAlarmOnuRingerFailure", 1037),
          ("cnAlarmOnuDoorAjar", 1038),
          ("cnAlarmOnuHighTemperature", 1039),
          ("cnAlarmOnuScanPoint", 1040),
          ("cnAlarmOnuRf", 1041),
          ("cnDS1LineLOS", 2000),
          ("cnDS1PathLOF", 2001),
          ("cnDS1PathAIS", 2002),
          ("cnDS1PathRAI", 2003),
          ("cnDS3LineLOS", 2004),
          ("cnDS3PathLOF", 2005),
          ("cnDS3PathAIS", 2006),
          ("cnDS3PathRAI", 2007),
          ("cnSONETLOS", 2008),
          ("cnSONETSectionLOF", 2009),
          ("cnSONETLineAIS", 2010),
          ("cnSONETPathAIS", 2011),
          ("cnSONETPathLOP", 2012),
          ("cnSONETPathUNEQ", 2013),
          ("cnSONETPathTIM", 2014),
          ("cnSONETPathPLM", 2015),
          ("cnSONETLineRDI", 2016),
          ("cnSONETPathRDI", 2017),
          ("cnSONETAPSModeMismatch", 2018),
          ("cnSONETAPSChannelMismatch", 2019),
          ("cnSONETAPSProtSwitchByteFail", 2020),
          ("cnSONETAPSFarEndProtLineFail", 2021),
          ("cnSONETBitErrRateSignalFail", 2022),
          ("cnSONETBitErrRateSignalDegrade", 2023),
          ("cnAlarmSONETAPSActiveChanSignalFail", 2024),
          ("cnAlarmSONETAPSGroupNotRedundant", 2025),
          ("cnDS1LineSES", 2026),
          ("cnAlarmDs3FeacSaEqptFail", 2027),
          ("cnAlarmDs3FeacLosHberAlarm", 2028),
          ("cnAlarmDs3FeacOOF", 2029),
          ("cnAlarmDs3FeacAIS", 2030),
          ("cnAlarmDs3FeacCommEqptFail", 2031),
          ("cnAlarmDs3PlcpLOFalarmCode", 2032),
          ("cnAlarmDs3PlcpYellowalarmCode", 2033),
          ("cnAlarmDs3RcvRaiFailureAlarmCode", 2034),
          ("cnAlarmDs3UnavailSignalStateAlarmCode", 2035),
          ("cnAlarmDs3NetEquipOOSAlarmCode", 2036),
          ("cnAlarmDs3OofAlarmCode", 2037),
          ("cnAlarmDs3IdleAlarmCode", 2038),
          ("cnAlarmE1LineLOS", 2039),
          ("cnAlarmE1PathLOF", 2040),
          ("cnAlarmE1PathAIS", 2041),
          ("cnAlarmE1PathRAI", 2042),
          ("cnAlarmE1LineSES", 2043),
          ("cnLossOfCellDelineation", 3000),
          ("cnAlarmDSLLineDown", 3001),
          ("cnAlarmDSLLineUp", 3002),
          ("cnAlarmATMF5AIS", 3003),
          ("cnAlarmDSLPowerConservation", 3004),
          ("cn15MinTCACVS", 4000),
          ("cn15MinTCACVL", 4001),
          ("cn15MinTCACVLFE", 4002),
          ("cn15MinTCACVP", 4003),
          ("cn15MinTCACVPFE", 4004),
          ("cn15MinTCAESS", 4005),
          ("cn15MinTCAESL", 4006),
          ("cn15MinTCAESLFE", 4007),
          ("cn15MinTCAESP", 4008),
          ("cn15MinTCAESPFE", 4009),
          ("cn15MinTCASESS", 4010),
          ("cn15MinTCASESL", 4011),
          ("cn15MinTCASESLFE", 4012),
          ("cn15MinTCASESP", 4013),
          ("cn15MinTCASESPFE", 4014),
          ("cn15MinTCAUASS", 4015),
          ("cn15MinTCAUASL", 4016),
          ("cn15MinTCAUASLFE", 4017),
          ("cn15MinTCAUASP", 4018),
          ("cn15MinTCAUASPFE", 4019),
          ("cn15MinTCAHEC", 4020),
          ("cn15MinTCABO", 4021),
          ("cn15MinTCABU", 4022),
          ("cn15MinTCACSS", 4023),
          ("cn15MinTCASAS", 4024),
          ("cn15MinTCAUAS", 4025),
          ("cn24HrTCACVLBPV", 5000),
          ("cn24HrTCACVPCRC", 5001),
          ("cn24HrTCACVPFE", 5002),
          ("cn24HrTCACCS", 5003),
          ("cn24HrTCASAS", 5004),
          ("cn24HrTCAUAS", 5005),
          ("cn24HrTCAESP", 5006),
          ("cn24HrTCAESL", 5007),
          ("cn24HrTCASESP", 5008),
          ("cn24HrTCASESL", 5009),
          ("cn24HrTCAUASP", 5010),
          ("cn24HrTCAUASL", 5011),
          ("cn24HrTCAHEC", 5012),
          ("cn24HrTCABO", 5013),
          ("cn24HrTCABU", 5014),
          ("cn24HrTCAcn1000OAIS", 5015),
          ("cn24HrTCAOcn1000RDI", 5016),
          ("cnVceSignallingLinkDownMin", 6000),
          ("cnVceLgSigLinkDownCri", 6001),
          ("cnVceSignallingLinkDownCri", 6002),
          ("cnVceCallRejRdtLineUnavailMin", 6003),
          ("cnVceCallRejRdtLineUnavailMaj", 6004),
          ("cnVceCallRejRdtLineUnavailCri", 6005),
          ("cnVceLgOutCallRejLineUnSubMin", 6006),
          ("cnVceLgOutCallRejLineUnSubMaj", 6007),
          ("cnVceLgOutCallRejLineUnSubCri", 6008),
          ("cnVceLgInCallRejLineUnSubMin", 6009),
          ("cnVceLgInCallRejLineUnSubMaj", 6010),
          ("cnVceLgInCallRejLineUnSubCri", 6011),
          ("cnVceLgRefCallRejLineUnSubMin", 6012),
          ("cnVceLgRefCallRejLineUnSubMaj", 6013),
          ("cnVceLgRefCallRejLineUnSubCri", 6014),
          ("cnVceLgRefCallRejIdtLineUnavailMin", 6015),
          ("cnVceLgRefCallRejIdtLineUnavailMaj", 6016),
          ("cnVceLgRefCallRejIdtLineUnavailCri", 6017),
          ("cnVceLgRefCallRejUnkownCrvMin", 6018),
          ("cnVceLgRefCallRejUnkownCrvMaj", 6019),
          ("cnVceLgRefCallRejUnkownCrvCri", 6020),
          ("cnVceMgSignallingLinkDownCri", 6021),
          ("cnGR303EOCProtectionSwitchToSecondary", 6036),
          ("cnGR303TMCProtectionSwitchToSecondary", 6037),
          ("cnGR303EOCClear", 6038),
          ("cnGR303EOCMinor", 6039),
          ("cnGR303EOCCri", 6040),
          ("cnGR303TMCClear", 6041),
          ("cnGR303TMCMinor", 6042),
          ("cnGR303TMCCri", 6043))
    )



class CnAlarmNotificationEnablingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnAlarmNotificationsEnabled", 1),
          ("cnAlarmNotificationsDisabled", 2))
    )



class CnAlarmMiscEnvironRelayStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnAlarmRelayOpen", 1),
          ("cnAlarmRelayClosed", 2))
    )



class CnAlarmMiscEnvironRelayFunctionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnAlarmMiscellaneous", 1),
          ("cnAlarmACPowerFail", 2))
    )



class CnAlarmIndexRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class CnAlarmUserAcknowledgementStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("userAcknowledged", 1),
          ("userUnacknowledged", 2))
    )



class CnAlarmResolutionStatusType(TextualConvention, Integer32):
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
        *(("cnAlarmUnresolved", 1),
          ("cnAlarmResolved", 2),
          ("cnAlarmResolutionNotApplicable", 3))
    )



class CnAlarmNotificationSequence(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )



# MIB Managed Objects in the order of their OIDs

_CnAlarmClassAudibleCutoff_Type = Integer32
_CnAlarmClassAudibleCutoff_Object = MibScalar
cnAlarmClassAudibleCutoff = _CnAlarmClassAudibleCutoff_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 1),
    _CnAlarmClassAudibleCutoff_Type()
)
cnAlarmClassAudibleCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmClassAudibleCutoff.setStatus("current")
_CnAlarmClassConfigAndControlTable_Object = MibTable
cnAlarmClassConfigAndControlTable = _CnAlarmClassConfigAndControlTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 3)
)
if mibBuilder.loadTexts:
    cnAlarmClassConfigAndControlTable.setStatus("current")
_CnAlarmClassConfigAndControlEntry_Object = MibTableRow
cnAlarmClassConfigAndControlEntry = _CnAlarmClassConfigAndControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 3, 1)
)
cnAlarmClassConfigAndControlEntry.setIndexNames(
    (0, "CEM-ALARMS", "cnAlarmSeverity"),
)
if mibBuilder.loadTexts:
    cnAlarmClassConfigAndControlEntry.setStatus("current")
_CnAlarmSeverity_Type = CnAlarmSeverityType
_CnAlarmSeverity_Object = MibTableColumn
cnAlarmSeverity = _CnAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 3, 1, 1),
    _CnAlarmSeverity_Type()
)
cnAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAlarmSeverity.setStatus("current")
_CnAlarmAudible_Type = CnAlarmTableAudibilityConfigType
_CnAlarmAudible_Object = MibTableColumn
cnAlarmAudible = _CnAlarmAudible_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 3, 1, 2),
    _CnAlarmAudible_Type()
)
cnAlarmAudible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmAudible.setStatus("current")
_CnAlarmBufferType_Type = CnAlarmTableBufferConfigType
_CnAlarmBufferType_Object = MibTableColumn
cnAlarmBufferType = _CnAlarmBufferType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 3, 1, 5),
    _CnAlarmBufferType_Type()
)
cnAlarmBufferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmBufferType.setStatus("current")
_CnAlarmTableControl_Type = CnTableControlType
_CnAlarmTableControl_Object = MibTableColumn
cnAlarmTableControl = _CnAlarmTableControl_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 3, 1, 7),
    _CnAlarmTableControl_Type()
)
cnAlarmTableControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmTableControl.setStatus("current")
_CnUserDefinedAlarmConfigTable_Object = MibTable
cnUserDefinedAlarmConfigTable = _CnUserDefinedAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 4)
)
if mibBuilder.loadTexts:
    cnUserDefinedAlarmConfigTable.setStatus("current")
_CnUserDefinedAlarmConfigEntry_Object = MibTableRow
cnUserDefinedAlarmConfigEntry = _CnUserDefinedAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 4, 1)
)
cnUserDefinedAlarmConfigEntry.setIndexNames(
    (0, "CEM-ALARMS", "cnAlarmUserDefinedAlarmNumber"),
)
if mibBuilder.loadTexts:
    cnUserDefinedAlarmConfigEntry.setStatus("current")
_CnAlarmUserDefinedAlarmNumber_Type = CnAlarmCodeType
_CnAlarmUserDefinedAlarmNumber_Object = MibTableColumn
cnAlarmUserDefinedAlarmNumber = _CnAlarmUserDefinedAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 4, 1, 1),
    _CnAlarmUserDefinedAlarmNumber_Type()
)
cnAlarmUserDefinedAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAlarmUserDefinedAlarmNumber.setStatus("current")
_CnAlarmUserDefinedAlarmSeverity_Type = CnAlarmSeverityType
_CnAlarmUserDefinedAlarmSeverity_Object = MibTableColumn
cnAlarmUserDefinedAlarmSeverity = _CnAlarmUserDefinedAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 4, 1, 2),
    _CnAlarmUserDefinedAlarmSeverity_Type()
)
cnAlarmUserDefinedAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmUserDefinedAlarmSeverity.setStatus("current")
_CnAlarmUserDefinedAlarmNotification_Type = CnAlarmNotificationEnablingType
_CnAlarmUserDefinedAlarmNotification_Object = MibTableColumn
cnAlarmUserDefinedAlarmNotification = _CnAlarmUserDefinedAlarmNotification_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 4, 1, 3),
    _CnAlarmUserDefinedAlarmNotification_Type()
)
cnAlarmUserDefinedAlarmNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmUserDefinedAlarmNotification.setStatus("current")


class _CnAlarmUserDefinedAlarmText_Type(OctetString):
    """Custom type cnAlarmUserDefinedAlarmText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CnAlarmUserDefinedAlarmText_Type.__name__ = "OctetString"
_CnAlarmUserDefinedAlarmText_Object = MibTableColumn
cnAlarmUserDefinedAlarmText = _CnAlarmUserDefinedAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 4, 1, 4),
    _CnAlarmUserDefinedAlarmText_Type()
)
cnAlarmUserDefinedAlarmText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmUserDefinedAlarmText.setStatus("current")
_CnAlarmMiscEnvironConfigTable_Object = MibTable
cnAlarmMiscEnvironConfigTable = _CnAlarmMiscEnvironConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 6)
)
if mibBuilder.loadTexts:
    cnAlarmMiscEnvironConfigTable.setStatus("current")
_CnAlarmMiscEnvironConfigEntry_Object = MibTableRow
cnAlarmMiscEnvironConfigEntry = _CnAlarmMiscEnvironConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 6, 1)
)
cnAlarmMiscEnvironConfigEntry.setIndexNames(
    (0, "CEM-ALARMS", "cnAlarmMiscEnvironRelayNumber"),
)
if mibBuilder.loadTexts:
    cnAlarmMiscEnvironConfigEntry.setStatus("current")


class _CnAlarmMiscEnvironRelayNumber_Type(Integer32):
    """Custom type cnAlarmMiscEnvironRelayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CnAlarmMiscEnvironRelayNumber_Type.__name__ = "Integer32"
_CnAlarmMiscEnvironRelayNumber_Object = MibTableColumn
cnAlarmMiscEnvironRelayNumber = _CnAlarmMiscEnvironRelayNumber_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 6, 1, 1),
    _CnAlarmMiscEnvironRelayNumber_Type()
)
cnAlarmMiscEnvironRelayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAlarmMiscEnvironRelayNumber.setStatus("current")
_CnAlarmMiscEnvironAlarmCode_Type = CnAlarmCodeType
_CnAlarmMiscEnvironAlarmCode_Object = MibTableColumn
cnAlarmMiscEnvironAlarmCode = _CnAlarmMiscEnvironAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 6, 1, 2),
    _CnAlarmMiscEnvironAlarmCode_Type()
)
cnAlarmMiscEnvironAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAlarmMiscEnvironAlarmCode.setStatus("current")
_CnAlarmMiscEnvironNormalRelayState_Type = CnAlarmMiscEnvironRelayStateType
_CnAlarmMiscEnvironNormalRelayState_Object = MibTableColumn
cnAlarmMiscEnvironNormalRelayState = _CnAlarmMiscEnvironNormalRelayState_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 6, 1, 3),
    _CnAlarmMiscEnvironNormalRelayState_Type()
)
cnAlarmMiscEnvironNormalRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmMiscEnvironNormalRelayState.setStatus("current")
_CnAlarmMiscEnvironRelayFunction_Type = CnAlarmMiscEnvironRelayFunctionType
_CnAlarmMiscEnvironRelayFunction_Object = MibTableColumn
cnAlarmMiscEnvironRelayFunction = _CnAlarmMiscEnvironRelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 6, 1, 4),
    _CnAlarmMiscEnvironRelayFunction_Type()
)
cnAlarmMiscEnvironRelayFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmMiscEnvironRelayFunction.setStatus("current")
_CnAlarmActiveTable_Object = MibTable
cnAlarmActiveTable = _CnAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7)
)
if mibBuilder.loadTexts:
    cnAlarmActiveTable.setStatus("current")
_CnAlarmActiveEntry_Object = MibTableRow
cnAlarmActiveEntry = _CnAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1)
)
cnAlarmActiveEntry.setIndexNames(
    (0, "CEM-ALARMS", "cnAlarmSeverity"),
    (0, "CEM-ALARMS", "cnActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    cnAlarmActiveEntry.setStatus("current")
_CnActiveAlarmIndex_Type = CnAlarmIndexRange
_CnActiveAlarmIndex_Object = MibTableColumn
cnActiveAlarmIndex = _CnActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 1),
    _CnActiveAlarmIndex_Type()
)
cnActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmIndex.setStatus("current")
_CnActiveAlarmCode_Type = CnAlarmCodeType
_CnActiveAlarmCode_Object = MibTableColumn
cnActiveAlarmCode = _CnActiveAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 2),
    _CnActiveAlarmCode_Type()
)
cnActiveAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmCode.setStatus("current")
_CnActiveAlarmTimeStamp_Type = TimeStamp
_CnActiveAlarmTimeStamp_Object = MibTableColumn
cnActiveAlarmTimeStamp = _CnActiveAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 3),
    _CnActiveAlarmTimeStamp_Type()
)
cnActiveAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmTimeStamp.setStatus("current")


class _CnActiveAlarmText_Type(OctetString):
    """Custom type cnActiveAlarmText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CnActiveAlarmText_Type.__name__ = "OctetString"
_CnActiveAlarmText_Object = MibTableColumn
cnActiveAlarmText = _CnActiveAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 4),
    _CnActiveAlarmText_Type()
)
cnActiveAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmText.setStatus("current")


class _CnActiveAlarmShelfIdentifier_Type(Integer32):
    """Custom type cnActiveAlarmShelfIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CnActiveAlarmShelfIdentifier_Type.__name__ = "Integer32"
_CnActiveAlarmShelfIdentifier_Object = MibTableColumn
cnActiveAlarmShelfIdentifier = _CnActiveAlarmShelfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 5),
    _CnActiveAlarmShelfIdentifier_Type()
)
cnActiveAlarmShelfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmShelfIdentifier.setStatus("current")


class _CnActiveAlarmSlotIdentifier_Type(Integer32):
    """Custom type cnActiveAlarmSlotIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CnActiveAlarmSlotIdentifier_Type.__name__ = "Integer32"
_CnActiveAlarmSlotIdentifier_Object = MibTableColumn
cnActiveAlarmSlotIdentifier = _CnActiveAlarmSlotIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 6),
    _CnActiveAlarmSlotIdentifier_Type()
)
cnActiveAlarmSlotIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmSlotIdentifier.setStatus("current")


class _CnActiveAlarmPortIdentifier_Type(Integer32):
    """Custom type cnActiveAlarmPortIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CnActiveAlarmPortIdentifier_Type.__name__ = "Integer32"
_CnActiveAlarmPortIdentifier_Object = MibTableColumn
cnActiveAlarmPortIdentifier = _CnActiveAlarmPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 7),
    _CnActiveAlarmPortIdentifier_Type()
)
cnActiveAlarmPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmPortIdentifier.setStatus("current")
_CnActiveAlarmUserAckStatus_Type = CnAlarmUserAcknowledgementStatusType
_CnActiveAlarmUserAckStatus_Object = MibTableColumn
cnActiveAlarmUserAckStatus = _CnActiveAlarmUserAckStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 8),
    _CnActiveAlarmUserAckStatus_Type()
)
cnActiveAlarmUserAckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnActiveAlarmUserAckStatus.setStatus("current")
_CnActiveAlarmResolutionStatus_Type = CnAlarmResolutionStatusType
_CnActiveAlarmResolutionStatus_Object = MibTableColumn
cnActiveAlarmResolutionStatus = _CnActiveAlarmResolutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 9),
    _CnActiveAlarmResolutionStatus_Type()
)
cnActiveAlarmResolutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmResolutionStatus.setStatus("current")
_CnActiveAlarmEntryRowStatus_Type = RowStatus
_CnActiveAlarmEntryRowStatus_Object = MibTableColumn
cnActiveAlarmEntryRowStatus = _CnActiveAlarmEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 10),
    _CnActiveAlarmEntryRowStatus_Type()
)
cnActiveAlarmEntryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnActiveAlarmEntryRowStatus.setStatus("current")
_CnActiveAlarmIfType_Type = Integer32
_CnActiveAlarmIfType_Object = MibTableColumn
cnActiveAlarmIfType = _CnActiveAlarmIfType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 12),
    _CnActiveAlarmIfType_Type()
)
cnActiveAlarmIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmIfType.setStatus("current")
_CnActiveAlarmEntPhysicalType_Type = Integer32
_CnActiveAlarmEntPhysicalType_Object = MibTableColumn
cnActiveAlarmEntPhysicalType = _CnActiveAlarmEntPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 13),
    _CnActiveAlarmEntPhysicalType_Type()
)
cnActiveAlarmEntPhysicalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmEntPhysicalType.setStatus("current")
_CnActiveAlarmVPI_Type = Integer32
_CnActiveAlarmVPI_Object = MibTableColumn
cnActiveAlarmVPI = _CnActiveAlarmVPI_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 15),
    _CnActiveAlarmVPI_Type()
)
cnActiveAlarmVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmVPI.setStatus("current")
_CnActiveAlarmVCI_Type = Integer32
_CnActiveAlarmVCI_Object = MibTableColumn
cnActiveAlarmVCI = _CnActiveAlarmVCI_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 7, 1, 16),
    _CnActiveAlarmVCI_Type()
)
cnActiveAlarmVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnActiveAlarmVCI.setStatus("current")
_CnAlarmNotificationsControl_ObjectIdentity = ObjectIdentity
cnAlarmNotificationsControl = _CnAlarmNotificationsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 11, 11)
)
_CnAlarmNotificationsIpAddress_Type = IpAddress
_CnAlarmNotificationsIpAddress_Object = MibScalar
cnAlarmNotificationsIpAddress = _CnAlarmNotificationsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 11, 1),
    _CnAlarmNotificationsIpAddress_Type()
)
cnAlarmNotificationsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmNotificationsIpAddress.setStatus("deprecated")


class _CnAlarmNotificationsPort_Type(Integer32):
    """Custom type cnAlarmNotificationsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnAlarmNotificationsPort_Type.__name__ = "Integer32"
_CnAlarmNotificationsPort_Object = MibScalar
cnAlarmNotificationsPort = _CnAlarmNotificationsPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 11, 2),
    _CnAlarmNotificationsPort_Type()
)
cnAlarmNotificationsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAlarmNotificationsPort.setStatus("deprecated")
_CnCriticalAlarmNotifications_Type = CnAlarmNotificationEnablingType
_CnCriticalAlarmNotifications_Object = MibScalar
cnCriticalAlarmNotifications = _CnCriticalAlarmNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 11, 3),
    _CnCriticalAlarmNotifications_Type()
)
cnCriticalAlarmNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnCriticalAlarmNotifications.setStatus("current")
_CnMajorAlarmNotifications_Type = CnAlarmNotificationEnablingType
_CnMajorAlarmNotifications_Object = MibScalar
cnMajorAlarmNotifications = _CnMajorAlarmNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 11, 4),
    _CnMajorAlarmNotifications_Type()
)
cnMajorAlarmNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMajorAlarmNotifications.setStatus("current")
_CnMinorAlarmNotifications_Type = CnAlarmNotificationEnablingType
_CnMinorAlarmNotifications_Object = MibScalar
cnMinorAlarmNotifications = _CnMinorAlarmNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 11, 5),
    _CnMinorAlarmNotifications_Type()
)
cnMinorAlarmNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnMinorAlarmNotifications.setStatus("current")
_CnInformationalAlarmNotifications_Type = CnAlarmNotificationEnablingType
_CnInformationalAlarmNotifications_Object = MibScalar
cnInformationalAlarmNotifications = _CnInformationalAlarmNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 11, 6),
    _CnInformationalAlarmNotifications_Type()
)
cnInformationalAlarmNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnInformationalAlarmNotifications.setStatus("current")
_CnAlarmNotificationSequence_Type = CnAlarmNotificationSequence
_CnAlarmNotificationSequence_Object = MibScalar
cnAlarmNotificationSequence = _CnAlarmNotificationSequence_Object(
    (1, 3, 6, 1, 4, 1, 6352, 11, 11, 7),
    _CnAlarmNotificationSequence_Type()
)
cnAlarmNotificationSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnAlarmNotificationSequence.setStatus("current")
_CnAlarmsNotifications_ObjectIdentity = ObjectIdentity
cnAlarmsNotifications = _CnAlarmsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 11, 22)
)
_CnAlarmsConformance_ObjectIdentity = ObjectIdentity
cnAlarmsConformance = _CnAlarmsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 11, 23)
)

# Managed Objects groups

cnAlarmsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 11, 23, 1)
)
cnAlarmsObjectsGroup.setObjects(
      *(("CEM-ALARMS", "cnAlarmClassAudibleCutoff"),
        ("CEM-ALARMS", "cnAlarmSeverity"),
        ("CEM-ALARMS", "cnAlarmAudible"),
        ("CEM-ALARMS", "cnAlarmBufferType"),
        ("CEM-ALARMS", "cnAlarmTableControl"),
        ("CEM-ALARMS", "cnAlarmUserDefinedAlarmNumber"),
        ("CEM-ALARMS", "cnAlarmUserDefinedAlarmSeverity"),
        ("CEM-ALARMS", "cnAlarmUserDefinedAlarmText"),
        ("CEM-ALARMS", "cnAlarmMiscEnvironRelayNumber"),
        ("CEM-ALARMS", "cnAlarmMiscEnvironAlarmCode"),
        ("CEM-ALARMS", "cnAlarmMiscEnvironNormalRelayState"),
        ("CEM-ALARMS", "cnActiveAlarmIndex"),
        ("CEM-ALARMS", "cnActiveAlarmCode"),
        ("CEM-ALARMS", "cnActiveAlarmTimeStamp"),
        ("CEM-ALARMS", "cnActiveAlarmText"),
        ("CEM-ALARMS", "cnActiveAlarmShelfIdentifier"),
        ("CEM-ALARMS", "cnActiveAlarmSlotIdentifier"),
        ("CEM-ALARMS", "cnActiveAlarmPortIdentifier"),
        ("CEM-ALARMS", "cnActiveAlarmUserAckStatus"),
        ("CEM-ALARMS", "cnActiveAlarmResolutionStatus"),
        ("CEM-ALARMS", "cnActiveAlarmEntryRowStatus"),
        ("CEM-ALARMS", "cnCriticalAlarmNotifications"),
        ("CEM-ALARMS", "cnMajorAlarmNotifications"),
        ("CEM-ALARMS", "cnMinorAlarmNotifications"),
        ("CEM-ALARMS", "cnInformationalAlarmNotifications"),
        ("CEM-ALARMS", "cnAlarmNotificationSequence"),
        ("CEM-ALARMS", "cnAlarmUserDefinedAlarmNotification"))
)
if mibBuilder.loadTexts:
    cnAlarmsObjectsGroup.setStatus("current")


# Notification objects

cnAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 11, 22, 1)
)
cnAlarmNotification.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CEM-ALARMS", "cnAlarmNotificationSequence"),
        ("CEM-ALARMS", "cnAlarmSeverity"),
        ("CEM-ALARMS", "cnActiveAlarmIndex"),
        ("CEM-ALARMS", "cnActiveAlarmCode"),
        ("CEM-ALARMS", "cnActiveAlarmTimeStamp"),
        ("CEM-ALARMS", "cnActiveAlarmText"),
        ("CEM-ALARMS", "cnActiveAlarmShelfIdentifier"),
        ("CEM-ALARMS", "cnActiveAlarmSlotIdentifier"),
        ("CEM-ALARMS", "cnActiveAlarmPortIdentifier"),
        ("CEM-ALARMS", "cnActiveAlarmUserAckStatus"),
        ("CEM-ALARMS", "cnActiveAlarmResolutionStatus"),
        ("CEM-ALARMS", "cnActiveAlarmVCI"),
        ("CEM-ALARMS", "cnActiveAlarmVPI"),
        ("CEM-ALARMS", "cnActiveAlarmEntPhysicalType"),
        ("CEM-ALARMS", "cnActiveAlarmIfType"))
)
if mibBuilder.loadTexts:
    cnAlarmNotification.setStatus(
        "current"
    )


# Notifications groups

cnAlarmsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 11, 23, 2)
)
cnAlarmsNotificationsGroup.setObjects(
    ("CEM-ALARMS", "cnAlarmNotification")
)
if mibBuilder.loadTexts:
    cnAlarmsNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cnAlarmsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 11, 23, 3)
)
cnAlarmsCompliance.setObjects(
      *(("CEM-ALARMS", "cnAlarmsObjectsGroup"),
        ("CEM-ALARMS", "cnAlarmsNotificationsGroup"))
)
if mibBuilder.loadTexts:
    cnAlarmsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-ALARMS",
    **{"CnAlarmSeverityType": CnAlarmSeverityType,
       "CnAlarmTableAudibilityConfigType": CnAlarmTableAudibilityConfigType,
       "CnAlarmTableBufferConfigType": CnAlarmTableBufferConfigType,
       "CnTableControlType": CnTableControlType,
       "CnAlarmCodeType": CnAlarmCodeType,
       "CnAlarmNotificationEnablingType": CnAlarmNotificationEnablingType,
       "CnAlarmMiscEnvironRelayStateType": CnAlarmMiscEnvironRelayStateType,
       "CnAlarmMiscEnvironRelayFunctionType": CnAlarmMiscEnvironRelayFunctionType,
       "CnAlarmIndexRange": CnAlarmIndexRange,
       "CnAlarmUserAcknowledgementStatusType": CnAlarmUserAcknowledgementStatusType,
       "CnAlarmResolutionStatusType": CnAlarmResolutionStatusType,
       "CnAlarmNotificationSequence": CnAlarmNotificationSequence,
       "cnAlarmsModule": cnAlarmsModule,
       "cnAlarmClassAudibleCutoff": cnAlarmClassAudibleCutoff,
       "cnAlarmClassConfigAndControlTable": cnAlarmClassConfigAndControlTable,
       "cnAlarmClassConfigAndControlEntry": cnAlarmClassConfigAndControlEntry,
       "cnAlarmSeverity": cnAlarmSeverity,
       "cnAlarmAudible": cnAlarmAudible,
       "cnAlarmBufferType": cnAlarmBufferType,
       "cnAlarmTableControl": cnAlarmTableControl,
       "cnUserDefinedAlarmConfigTable": cnUserDefinedAlarmConfigTable,
       "cnUserDefinedAlarmConfigEntry": cnUserDefinedAlarmConfigEntry,
       "cnAlarmUserDefinedAlarmNumber": cnAlarmUserDefinedAlarmNumber,
       "cnAlarmUserDefinedAlarmSeverity": cnAlarmUserDefinedAlarmSeverity,
       "cnAlarmUserDefinedAlarmNotification": cnAlarmUserDefinedAlarmNotification,
       "cnAlarmUserDefinedAlarmText": cnAlarmUserDefinedAlarmText,
       "cnAlarmMiscEnvironConfigTable": cnAlarmMiscEnvironConfigTable,
       "cnAlarmMiscEnvironConfigEntry": cnAlarmMiscEnvironConfigEntry,
       "cnAlarmMiscEnvironRelayNumber": cnAlarmMiscEnvironRelayNumber,
       "cnAlarmMiscEnvironAlarmCode": cnAlarmMiscEnvironAlarmCode,
       "cnAlarmMiscEnvironNormalRelayState": cnAlarmMiscEnvironNormalRelayState,
       "cnAlarmMiscEnvironRelayFunction": cnAlarmMiscEnvironRelayFunction,
       "cnAlarmActiveTable": cnAlarmActiveTable,
       "cnAlarmActiveEntry": cnAlarmActiveEntry,
       "cnActiveAlarmIndex": cnActiveAlarmIndex,
       "cnActiveAlarmCode": cnActiveAlarmCode,
       "cnActiveAlarmTimeStamp": cnActiveAlarmTimeStamp,
       "cnActiveAlarmText": cnActiveAlarmText,
       "cnActiveAlarmShelfIdentifier": cnActiveAlarmShelfIdentifier,
       "cnActiveAlarmSlotIdentifier": cnActiveAlarmSlotIdentifier,
       "cnActiveAlarmPortIdentifier": cnActiveAlarmPortIdentifier,
       "cnActiveAlarmUserAckStatus": cnActiveAlarmUserAckStatus,
       "cnActiveAlarmResolutionStatus": cnActiveAlarmResolutionStatus,
       "cnActiveAlarmEntryRowStatus": cnActiveAlarmEntryRowStatus,
       "cnActiveAlarmIfType": cnActiveAlarmIfType,
       "cnActiveAlarmEntPhysicalType": cnActiveAlarmEntPhysicalType,
       "cnActiveAlarmVPI": cnActiveAlarmVPI,
       "cnActiveAlarmVCI": cnActiveAlarmVCI,
       "cnAlarmNotificationsControl": cnAlarmNotificationsControl,
       "cnAlarmNotificationsIpAddress": cnAlarmNotificationsIpAddress,
       "cnAlarmNotificationsPort": cnAlarmNotificationsPort,
       "cnCriticalAlarmNotifications": cnCriticalAlarmNotifications,
       "cnMajorAlarmNotifications": cnMajorAlarmNotifications,
       "cnMinorAlarmNotifications": cnMinorAlarmNotifications,
       "cnInformationalAlarmNotifications": cnInformationalAlarmNotifications,
       "cnAlarmNotificationSequence": cnAlarmNotificationSequence,
       "cnAlarmsNotifications": cnAlarmsNotifications,
       "cnAlarmNotification": cnAlarmNotification,
       "cnAlarmsConformance": cnAlarmsConformance,
       "cnAlarmsObjectsGroup": cnAlarmsObjectsGroup,
       "cnAlarmsNotificationsGroup": cnAlarmsNotificationsGroup,
       "cnAlarmsCompliance": cnAlarmsCompliance}
)
