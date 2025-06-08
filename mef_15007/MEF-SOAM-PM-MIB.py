# SNMP MIB module (MEF-SOAM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mef_15007/MEF-SOAM-PM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:23:56 2025
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

(Dot1afCfmIndexIntegerNextFree,
 Dot1agCfmMepId,
 Dot1agCfmMepIdOrZero,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1afCfmIndexIntegerNextFree",
    "Dot1agCfmMepId",
    "Dot1agCfmMepIdOrZero",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(MefSoamTcAvailabilityType,
 MefSoamTcDataPatternType,
 MefSoamTcDelayMeasurementBinType,
 MefSoamTcMeasurementPeriodType,
 MefSoamTcOperationTimeType,
 MefSoamTcSessionType,
 MefSoamTcStatusType,
 MefSoamTcTestPatternType) = mibBuilder.importSymbols(
    "MEF-SOAM-TC-MIB",
    "MefSoamTcAvailabilityType",
    "MefSoamTcDataPatternType",
    "MefSoamTcDelayMeasurementBinType",
    "MefSoamTcMeasurementPeriodType",
    "MefSoamTcOperationTimeType",
    "MefSoamTcSessionType",
    "MefSoamTcStatusType",
    "MefSoamTcTestPatternType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

mefSoamPmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3)
)
if mibBuilder.loadTexts:
    mefSoamPmMib.setRevisions(
        ("2015-03-30 12:00",
         "2012-01-13 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MefSoamPmNotifications_ObjectIdentity = ObjectIdentity
mefSoamPmNotifications = _MefSoamPmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0)
)
_MefSoamPmMibObjects_ObjectIdentity = ObjectIdentity
mefSoamPmMibObjects = _MefSoamPmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1)
)
_MefSoamPmMep_ObjectIdentity = ObjectIdentity
mefSoamPmMep = _MefSoamPmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1)
)
_MefSoamPmMepTable_Object = MibTable
mefSoamPmMepTable = _MefSoamPmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamPmMepTable.setStatus("current")
_MefSoamPmMepEntry_Object = MibTableRow
mefSoamPmMepEntry = _MefSoamPmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mefSoamPmMepEntry.setStatus("current")
_MefSoamPmMepOperNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_MefSoamPmMepOperNextIndex_Object = MibTableColumn
mefSoamPmMepOperNextIndex = _MefSoamPmMepOperNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1, 1),
    _MefSoamPmMepOperNextIndex_Type()
)
mefSoamPmMepOperNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamPmMepOperNextIndex.setStatus("current")


class _MefSoamPmMepLmSingleEndedResponder_Type(TruthValue):
    """Custom type mefSoamPmMepLmSingleEndedResponder based on TruthValue"""
    defaultValue = 1


_MefSoamPmMepLmSingleEndedResponder_Type.__name__ = "TruthValue"
_MefSoamPmMepLmSingleEndedResponder_Object = MibTableColumn
mefSoamPmMepLmSingleEndedResponder = _MefSoamPmMepLmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1, 2),
    _MefSoamPmMepLmSingleEndedResponder_Type()
)
mefSoamPmMepLmSingleEndedResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmMepLmSingleEndedResponder.setStatus("current")


class _MefSoamPmMepSlmSingleEndedResponder_Type(TruthValue):
    """Custom type mefSoamPmMepSlmSingleEndedResponder based on TruthValue"""
    defaultValue = 1


_MefSoamPmMepSlmSingleEndedResponder_Type.__name__ = "TruthValue"
_MefSoamPmMepSlmSingleEndedResponder_Object = MibTableColumn
mefSoamPmMepSlmSingleEndedResponder = _MefSoamPmMepSlmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1, 3),
    _MefSoamPmMepSlmSingleEndedResponder_Type()
)
mefSoamPmMepSlmSingleEndedResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmMepSlmSingleEndedResponder.setStatus("current")


class _MefSoamPmMepDmSingleEndedResponder_Type(TruthValue):
    """Custom type mefSoamPmMepDmSingleEndedResponder based on TruthValue"""
    defaultValue = 1


_MefSoamPmMepDmSingleEndedResponder_Type.__name__ = "TruthValue"
_MefSoamPmMepDmSingleEndedResponder_Object = MibTableColumn
mefSoamPmMepDmSingleEndedResponder = _MefSoamPmMepDmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 1, 1, 1, 4),
    _MefSoamPmMepDmSingleEndedResponder_Type()
)
mefSoamPmMepDmSingleEndedResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmMepDmSingleEndedResponder.setStatus("current")
_MefSoamPmLmObjects_ObjectIdentity = ObjectIdentity
mefSoamPmLmObjects = _MefSoamPmLmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2)
)
_MefSoamLmCfgTable_Object = MibTable
mefSoamLmCfgTable = _MefSoamLmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mefSoamLmCfgTable.setStatus("current")
_MefSoamLmCfgEntry_Object = MibTableRow
mefSoamLmCfgEntry = _MefSoamLmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1)
)
mefSoamLmCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmCfgEntry.setStatus("current")


class _MefSoamLmCfgIndex_Type(Unsigned32):
    """Custom type mefSoamLmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamLmCfgIndex_Type.__name__ = "Unsigned32"
_MefSoamLmCfgIndex_Object = MibTableColumn
mefSoamLmCfgIndex = _MefSoamLmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 1),
    _MefSoamLmCfgIndex_Type()
)
mefSoamLmCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmCfgIndex.setStatus("current")


class _MefSoamLmCfgType_Type(Integer32):
    """Custom type mefSoamLmCfgType based on Integer32"""
    defaultValue = 2

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
        *(("lmLmm", 1),
          ("lmSlm", 2),
          ("lmCcm", 3),
          ("lm1SlTx", 4),
          ("lm1SlRx", 5))
    )


_MefSoamLmCfgType_Type.__name__ = "Integer32"
_MefSoamLmCfgType_Object = MibTableColumn
mefSoamLmCfgType = _MefSoamLmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 2),
    _MefSoamLmCfgType_Type()
)
mefSoamLmCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgType.setStatus("current")


class _MefSoamLmCfgVersion_Type(Unsigned32):
    """Custom type mefSoamLmCfgVersion based on Unsigned32"""
    defaultValue = 0


_MefSoamLmCfgVersion_Type.__name__ = "Unsigned32"
_MefSoamLmCfgVersion_Object = MibTableColumn
mefSoamLmCfgVersion = _MefSoamLmCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 3),
    _MefSoamLmCfgVersion_Type()
)
mefSoamLmCfgVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgVersion.setStatus("current")


class _MefSoamLmCfgEnabled_Type(TruthValue):
    """Custom type mefSoamLmCfgEnabled based on TruthValue"""
    defaultValue = 1


_MefSoamLmCfgEnabled_Type.__name__ = "TruthValue"
_MefSoamLmCfgEnabled_Object = MibTableColumn
mefSoamLmCfgEnabled = _MefSoamLmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 4),
    _MefSoamLmCfgEnabled_Type()
)
mefSoamLmCfgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgEnabled.setStatus("current")


class _MefSoamLmCfgMeasurementEnable_Type(Bits):
    """Custom type mefSoamLmCfgMeasurementEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bForwardTransmitedFrames", 0),
          ("bForwardReceivedFrames", 1),
          ("bForwardMinFlr", 2),
          ("bForwardMaxFlr", 3),
          ("bForwardAvgFlr", 4),
          ("bBackwardTransmitedFrames", 5),
          ("bBackwardReceivedFrames", 6),
          ("bBackwardMinFlr", 7),
          ("bBackwardMaxFlr", 8),
          ("bBackwardAvgFlr", 9),
          ("bSoamPdusSent", 10),
          ("bSoamPdusReceived", 11),
          ("bAvailForwardHighLoss", 12),
          ("bAvailForwardConsecutiveHighLoss", 13),
          ("bAvailForwardAvailable", 14),
          ("bAvailForwardUnavailable", 15),
          ("bAvailForwardMinFlr", 16),
          ("bAvailForwardMaxFlr", 17),
          ("bAvailForwardAvgFlr", 18),
          ("bAvailBackwardHighLoss", 19),
          ("bAvailBackwardConsecutiveHighLoss", 20),
          ("bAvailBackwardAvailable", 21),
          ("bAvailBackwardUnavailable", 22),
          ("bAvailBackwardMinFlr", 23),
          ("bAvailBackwardMaxFlr", 24),
          ("bAvailBackwardAvgFlr", 25),
          ("bMeasuredStatsForwardMeasuredFlr", 26),
          ("bMeasuredStatsBackwardMeasuredFlr", 27),
          ("bMeasuredStatsAvailForwardStatus", 28),
          ("bMeasuredStatsAvailBackwardStatus", 29))
    )

_MefSoamLmCfgMeasurementEnable_Type.__name__ = "Bits"
_MefSoamLmCfgMeasurementEnable_Object = MibTableColumn
mefSoamLmCfgMeasurementEnable = _MefSoamLmCfgMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 5),
    _MefSoamLmCfgMeasurementEnable_Type()
)
mefSoamLmCfgMeasurementEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgMeasurementEnable.setStatus("current")


class _MefSoamLmCfgMessagePeriod_Type(MefSoamTcMeasurementPeriodType):
    """Custom type mefSoamLmCfgMessagePeriod based on MefSoamTcMeasurementPeriodType"""
    defaultValue = 100


_MefSoamLmCfgMessagePeriod_Type.__name__ = "MefSoamTcMeasurementPeriodType"
_MefSoamLmCfgMessagePeriod_Object = MibTableColumn
mefSoamLmCfgMessagePeriod = _MefSoamLmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 6),
    _MefSoamLmCfgMessagePeriod_Type()
)
mefSoamLmCfgMessagePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgMessagePeriod.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgMessagePeriod.setUnits("ms")
_MefSoamLmCfgPriority_Type = IEEE8021PriorityValue
_MefSoamLmCfgPriority_Object = MibTableColumn
mefSoamLmCfgPriority = _MefSoamLmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 7),
    _MefSoamLmCfgPriority_Type()
)
mefSoamLmCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgPriority.setStatus("current")


class _MefSoamLmCfgFrameSize_Type(Unsigned32):
    """Custom type mefSoamLmCfgFrameSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_MefSoamLmCfgFrameSize_Type.__name__ = "Unsigned32"
_MefSoamLmCfgFrameSize_Object = MibTableColumn
mefSoamLmCfgFrameSize = _MefSoamLmCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 8),
    _MefSoamLmCfgFrameSize_Type()
)
mefSoamLmCfgFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgFrameSize.setUnits("bytes")


class _MefSoamLmCfgDataPattern_Type(MefSoamTcDataPatternType):
    """Custom type mefSoamLmCfgDataPattern based on MefSoamTcDataPatternType"""
    defaultValue = 1


_MefSoamLmCfgDataPattern_Type.__name__ = "MefSoamTcDataPatternType"
_MefSoamLmCfgDataPattern_Object = MibTableColumn
mefSoamLmCfgDataPattern = _MefSoamLmCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 9),
    _MefSoamLmCfgDataPattern_Type()
)
mefSoamLmCfgDataPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDataPattern.setStatus("current")


class _MefSoamLmCfgTestTlvIncluded_Type(TruthValue):
    """Custom type mefSoamLmCfgTestTlvIncluded based on TruthValue"""
    defaultValue = 2


_MefSoamLmCfgTestTlvIncluded_Type.__name__ = "TruthValue"
_MefSoamLmCfgTestTlvIncluded_Object = MibTableColumn
mefSoamLmCfgTestTlvIncluded = _MefSoamLmCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 10),
    _MefSoamLmCfgTestTlvIncluded_Type()
)
mefSoamLmCfgTestTlvIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgTestTlvIncluded.setStatus("current")


class _MefSoamLmCfgTestTlvPattern_Type(MefSoamTcTestPatternType):
    """Custom type mefSoamLmCfgTestTlvPattern based on MefSoamTcTestPatternType"""
    defaultValue = 1


_MefSoamLmCfgTestTlvPattern_Type.__name__ = "MefSoamTcTestPatternType"
_MefSoamLmCfgTestTlvPattern_Object = MibTableColumn
mefSoamLmCfgTestTlvPattern = _MefSoamLmCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 11),
    _MefSoamLmCfgTestTlvPattern_Type()
)
mefSoamLmCfgTestTlvPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgTestTlvPattern.setStatus("current")


class _MefSoamLmCfgMeasurementInterval_Type(Unsigned32):
    """Custom type mefSoamLmCfgMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 525600),
    )


_MefSoamLmCfgMeasurementInterval_Type.__name__ = "Unsigned32"
_MefSoamLmCfgMeasurementInterval_Object = MibTableColumn
mefSoamLmCfgMeasurementInterval = _MefSoamLmCfgMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 12),
    _MefSoamLmCfgMeasurementInterval_Type()
)
mefSoamLmCfgMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgMeasurementInterval.setUnits("minutes")


class _MefSoamLmCfgNumIntervalsStored_Type(Unsigned32):
    """Custom type mefSoamLmCfgNumIntervalsStored based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1000),
    )


_MefSoamLmCfgNumIntervalsStored_Type.__name__ = "Unsigned32"
_MefSoamLmCfgNumIntervalsStored_Object = MibTableColumn
mefSoamLmCfgNumIntervalsStored = _MefSoamLmCfgNumIntervalsStored_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 13),
    _MefSoamLmCfgNumIntervalsStored_Type()
)
mefSoamLmCfgNumIntervalsStored.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgNumIntervalsStored.setStatus("current")
_MefSoamLmCfgDestMacAddress_Type = MacAddress
_MefSoamLmCfgDestMacAddress_Object = MibTableColumn
mefSoamLmCfgDestMacAddress = _MefSoamLmCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 14),
    _MefSoamLmCfgDestMacAddress_Type()
)
mefSoamLmCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDestMacAddress.setStatus("current")


class _MefSoamLmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type mefSoamLmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_MefSoamLmCfgDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_MefSoamLmCfgDestMepId_Object = MibTableColumn
mefSoamLmCfgDestMepId = _MefSoamLmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 15),
    _MefSoamLmCfgDestMepId_Type()
)
mefSoamLmCfgDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDestMepId.setStatus("current")


class _MefSoamLmCfgDestIsMepId_Type(TruthValue):
    """Custom type mefSoamLmCfgDestIsMepId based on TruthValue"""
    defaultValue = 1


_MefSoamLmCfgDestIsMepId_Type.__name__ = "TruthValue"
_MefSoamLmCfgDestIsMepId_Object = MibTableColumn
mefSoamLmCfgDestIsMepId = _MefSoamLmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 16),
    _MefSoamLmCfgDestIsMepId_Type()
)
mefSoamLmCfgDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDestIsMepId.setStatus("current")


class _MefSoamLmCfgStartTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamLmCfgStartTimeType based on MefSoamTcOperationTimeType"""
    defaultValue = 2


_MefSoamLmCfgStartTimeType_Type.__name__ = "MefSoamTcOperationTimeType"
_MefSoamLmCfgStartTimeType_Object = MibTableColumn
mefSoamLmCfgStartTimeType = _MefSoamLmCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 17),
    _MefSoamLmCfgStartTimeType_Type()
)
mefSoamLmCfgStartTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgStartTimeType.setStatus("current")


class _MefSoamLmCfgFixedStartDateAndTime_Type(DateAndTime):
    """Custom type mefSoamLmCfgFixedStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamLmCfgFixedStartDateAndTime_Type.__name__ = "DateAndTime"
_MefSoamLmCfgFixedStartDateAndTime_Object = MibTableColumn
mefSoamLmCfgFixedStartDateAndTime = _MefSoamLmCfgFixedStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 18),
    _MefSoamLmCfgFixedStartDateAndTime_Type()
)
mefSoamLmCfgFixedStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgFixedStartDateAndTime.setStatus("current")


class _MefSoamLmCfgRelativeStartTime_Type(TimeInterval):
    """Custom type mefSoamLmCfgRelativeStartTime based on TimeInterval"""
    defaultValue = 0


_MefSoamLmCfgRelativeStartTime_Type.__name__ = "TimeInterval"
_MefSoamLmCfgRelativeStartTime_Object = MibTableColumn
mefSoamLmCfgRelativeStartTime = _MefSoamLmCfgRelativeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 19),
    _MefSoamLmCfgRelativeStartTime_Type()
)
mefSoamLmCfgRelativeStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgRelativeStartTime.setStatus("current")


class _MefSoamLmCfgStopTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamLmCfgStopTimeType based on MefSoamTcOperationTimeType"""
    defaultValue = 1


_MefSoamLmCfgStopTimeType_Type.__name__ = "MefSoamTcOperationTimeType"
_MefSoamLmCfgStopTimeType_Object = MibTableColumn
mefSoamLmCfgStopTimeType = _MefSoamLmCfgStopTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 20),
    _MefSoamLmCfgStopTimeType_Type()
)
mefSoamLmCfgStopTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgStopTimeType.setStatus("current")


class _MefSoamLmCfgFixedStopDateAndTime_Type(DateAndTime):
    """Custom type mefSoamLmCfgFixedStopDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamLmCfgFixedStopDateAndTime_Type.__name__ = "DateAndTime"
_MefSoamLmCfgFixedStopDateAndTime_Object = MibTableColumn
mefSoamLmCfgFixedStopDateAndTime = _MefSoamLmCfgFixedStopDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 21),
    _MefSoamLmCfgFixedStopDateAndTime_Type()
)
mefSoamLmCfgFixedStopDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgFixedStopDateAndTime.setStatus("current")


class _MefSoamLmCfgRelativeStopTime_Type(TimeInterval):
    """Custom type mefSoamLmCfgRelativeStopTime based on TimeInterval"""
    defaultValue = 0


_MefSoamLmCfgRelativeStopTime_Type.__name__ = "TimeInterval"
_MefSoamLmCfgRelativeStopTime_Object = MibTableColumn
mefSoamLmCfgRelativeStopTime = _MefSoamLmCfgRelativeStopTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 22),
    _MefSoamLmCfgRelativeStopTime_Type()
)
mefSoamLmCfgRelativeStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgRelativeStopTime.setStatus("current")


class _MefSoamLmCfgRepetitionTime_Type(Unsigned32):
    """Custom type mefSoamLmCfgRepetitionTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_MefSoamLmCfgRepetitionTime_Type.__name__ = "Unsigned32"
_MefSoamLmCfgRepetitionTime_Object = MibTableColumn
mefSoamLmCfgRepetitionTime = _MefSoamLmCfgRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 23),
    _MefSoamLmCfgRepetitionTime_Type()
)
mefSoamLmCfgRepetitionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgRepetitionTime.setUnits("seconds")


class _MefSoamLmCfgAlignMeasurementIntervals_Type(TruthValue):
    """Custom type mefSoamLmCfgAlignMeasurementIntervals based on TruthValue"""
    defaultValue = 1


_MefSoamLmCfgAlignMeasurementIntervals_Type.__name__ = "TruthValue"
_MefSoamLmCfgAlignMeasurementIntervals_Object = MibTableColumn
mefSoamLmCfgAlignMeasurementIntervals = _MefSoamLmCfgAlignMeasurementIntervals_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 24),
    _MefSoamLmCfgAlignMeasurementIntervals_Type()
)
mefSoamLmCfgAlignMeasurementIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAlignMeasurementIntervals.setStatus("current")


class _MefSoamLmCfgAlignMeasurementOffset_Type(Unsigned32):
    """Custom type mefSoamLmCfgAlignMeasurementOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_MefSoamLmCfgAlignMeasurementOffset_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAlignMeasurementOffset_Object = MibTableColumn
mefSoamLmCfgAlignMeasurementOffset = _MefSoamLmCfgAlignMeasurementOffset_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 25),
    _MefSoamLmCfgAlignMeasurementOffset_Type()
)
mefSoamLmCfgAlignMeasurementOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAlignMeasurementOffset.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgAlignMeasurementOffset.setUnits("minutes")


class _MefSoamLmCfgAvailabilityMeasurementInterval_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 525600),
    )


_MefSoamLmCfgAvailabilityMeasurementInterval_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityMeasurementInterval_Object = MibTableColumn
mefSoamLmCfgAvailabilityMeasurementInterval = _MefSoamLmCfgAvailabilityMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 26),
    _MefSoamLmCfgAvailabilityMeasurementInterval_Type()
)
mefSoamLmCfgAvailabilityMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityMeasurementInterval.setUnits("minutes")


class _MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Object = MibTableColumn
mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus = _MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 27),
    _MefSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type()
)
mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus.setStatus("current")


class _MefSoamLmCfgAvailabilityFlrThreshold_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityFlrThreshold based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCfgAvailabilityFlrThreshold_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityFlrThreshold_Object = MibTableColumn
mefSoamLmCfgAvailabilityFlrThreshold = _MefSoamLmCfgAvailabilityFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 28),
    _MefSoamLmCfgAvailabilityFlrThreshold_Type()
)
mefSoamLmCfgAvailabilityFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityFlrThreshold.setUnits("milli-percent")


class _MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityNumConsecutiveIntervals based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Object = MibTableColumn
mefSoamLmCfgAvailabilityNumConsecutiveIntervals = _MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 29),
    _MefSoamLmCfgAvailabilityNumConsecutiveIntervals_Type()
)
mefSoamLmCfgAvailabilityNumConsecutiveIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityNumConsecutiveIntervals.setStatus("current")


class _MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type(Unsigned32):
    """Custom type mefSoamLmCfgAvailabilityNumConsecutiveHighFlr based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Object = MibTableColumn
mefSoamLmCfgAvailabilityNumConsecutiveHighFlr = _MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 30),
    _MefSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type()
)
mefSoamLmCfgAvailabilityNumConsecutiveHighFlr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgAvailabilityNumConsecutiveHighFlr.setStatus("current")


class _MefSoamLmCfgSessionType_Type(MefSoamTcSessionType):
    """Custom type mefSoamLmCfgSessionType based on MefSoamTcSessionType"""
    defaultValue = 1


_MefSoamLmCfgSessionType_Type.__name__ = "MefSoamTcSessionType"
_MefSoamLmCfgSessionType_Object = MibTableColumn
mefSoamLmCfgSessionType = _MefSoamLmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 31),
    _MefSoamLmCfgSessionType_Type()
)
mefSoamLmCfgSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgSessionType.setStatus("current")
_MefSoamLmCfgSessionStatus_Type = MefSoamTcStatusType
_MefSoamLmCfgSessionStatus_Object = MibTableColumn
mefSoamLmCfgSessionStatus = _MefSoamLmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 32),
    _MefSoamLmCfgSessionStatus_Type()
)
mefSoamLmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCfgSessionStatus.setStatus("current")


class _MefSoamLmCfgHistoryClear_Type(TruthValue):
    """Custom type mefSoamLmCfgHistoryClear based on TruthValue"""
    defaultValue = 2


_MefSoamLmCfgHistoryClear_Type.__name__ = "TruthValue"
_MefSoamLmCfgHistoryClear_Object = MibTableColumn
mefSoamLmCfgHistoryClear = _MefSoamLmCfgHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 33),
    _MefSoamLmCfgHistoryClear_Type()
)
mefSoamLmCfgHistoryClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgHistoryClear.setStatus("current")
_MefSoamLmCfgRowStatus_Type = RowStatus
_MefSoamLmCfgRowStatus_Object = MibTableColumn
mefSoamLmCfgRowStatus = _MefSoamLmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 34),
    _MefSoamLmCfgRowStatus_Type()
)
mefSoamLmCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgRowStatus.setStatus("current")


class _MefSoamLmCfgCosType_Type(Integer32):
    """Custom type mefSoamLmCfgCosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("pcp", 2),
          ("dei", 3))
    )


_MefSoamLmCfgCosType_Type.__name__ = "Integer32"
_MefSoamLmCfgCosType_Object = MibTableColumn
mefSoamLmCfgCosType = _MefSoamLmCfgCosType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 35),
    _MefSoamLmCfgCosType_Type()
)
mefSoamLmCfgCosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgCosType.setStatus("current")
_MefSoamLmCfgSourceMacAddress_Type = MacAddress
_MefSoamLmCfgSourceMacAddress_Object = MibTableColumn
mefSoamLmCfgSourceMacAddress = _MefSoamLmCfgSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 36),
    _MefSoamLmCfgSourceMacAddress_Type()
)
mefSoamLmCfgSourceMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgSourceMacAddress.setStatus("current")
_MefSoamLmCfgTcaNextIndex_Type = Unsigned32
_MefSoamLmCfgTcaNextIndex_Object = MibTableColumn
mefSoamLmCfgTcaNextIndex = _MefSoamLmCfgTcaNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 37),
    _MefSoamLmCfgTcaNextIndex_Type()
)
mefSoamLmCfgTcaNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCfgTcaNextIndex.setStatus("current")


class _MefSoamLmCfgDei_Type(Integer32):
    """Custom type mefSoamLmCfgDei based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noDei", 0),
          ("setDei", 1))
    )


_MefSoamLmCfgDei_Type.__name__ = "Integer32"
_MefSoamLmCfgDei_Object = MibTableColumn
mefSoamLmCfgDei = _MefSoamLmCfgDei_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 38),
    _MefSoamLmCfgDei_Type()
)
mefSoamLmCfgDei.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmCfgDei.setStatus("current")


class _MefSoamLmTestId_Type(Unsigned32):
    """Custom type mefSoamLmTestId based on Unsigned32"""
    defaultValue = 0


_MefSoamLmTestId_Type.__name__ = "Unsigned32"
_MefSoamLmTestId_Object = MibTableColumn
mefSoamLmTestId = _MefSoamLmTestId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 1, 1, 39),
    _MefSoamLmTestId_Type()
)
mefSoamLmTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmTestId.setStatus("current")
_MefSoamLmMeasuredStatsTable_Object = MibTable
mefSoamLmMeasuredStatsTable = _MefSoamLmMeasuredStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsTable.setStatus("current")
_MefSoamLmMeasuredStatsEntry_Object = MibTableRow
mefSoamLmMeasuredStatsEntry = _MefSoamLmMeasuredStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1)
)
mefSoamLmMeasuredStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsEntry.setStatus("current")


class _MefSoamLmMeasuredStatsForwardFlr_Type(Unsigned32):
    """Custom type mefSoamLmMeasuredStatsForwardFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmMeasuredStatsForwardFlr_Type.__name__ = "Unsigned32"
_MefSoamLmMeasuredStatsForwardFlr_Object = MibTableColumn
mefSoamLmMeasuredStatsForwardFlr = _MefSoamLmMeasuredStatsForwardFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 1),
    _MefSoamLmMeasuredStatsForwardFlr_Type()
)
mefSoamLmMeasuredStatsForwardFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsForwardFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsForwardFlr.setUnits("milli-percent")


class _MefSoamLmMeasuredStatsBackwardFlr_Type(Unsigned32):
    """Custom type mefSoamLmMeasuredStatsBackwardFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmMeasuredStatsBackwardFlr_Type.__name__ = "Unsigned32"
_MefSoamLmMeasuredStatsBackwardFlr_Object = MibTableColumn
mefSoamLmMeasuredStatsBackwardFlr = _MefSoamLmMeasuredStatsBackwardFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 2),
    _MefSoamLmMeasuredStatsBackwardFlr_Type()
)
mefSoamLmMeasuredStatsBackwardFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsBackwardFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsBackwardFlr.setUnits("milli-percent")
_MefSoamLmMeasuredStatsAvailForwardStatus_Type = MefSoamTcAvailabilityType
_MefSoamLmMeasuredStatsAvailForwardStatus_Object = MibTableColumn
mefSoamLmMeasuredStatsAvailForwardStatus = _MefSoamLmMeasuredStatsAvailForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 3),
    _MefSoamLmMeasuredStatsAvailForwardStatus_Type()
)
mefSoamLmMeasuredStatsAvailForwardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsAvailForwardStatus.setStatus("current")
_MefSoamLmMeasuredStatsAvailBackwardStatus_Type = MefSoamTcAvailabilityType
_MefSoamLmMeasuredStatsAvailBackwardStatus_Object = MibTableColumn
mefSoamLmMeasuredStatsAvailBackwardStatus = _MefSoamLmMeasuredStatsAvailBackwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 4),
    _MefSoamLmMeasuredStatsAvailBackwardStatus_Type()
)
mefSoamLmMeasuredStatsAvailBackwardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsAvailBackwardStatus.setStatus("current")
_MefSoamLmMeasuredStatsAvailForwardLastTransitionTime_Type = DateAndTime
_MefSoamLmMeasuredStatsAvailForwardLastTransitionTime_Object = MibTableColumn
mefSoamLmMeasuredStatsAvailForwardLastTransitionTime = _MefSoamLmMeasuredStatsAvailForwardLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 5),
    _MefSoamLmMeasuredStatsAvailForwardLastTransitionTime_Type()
)
mefSoamLmMeasuredStatsAvailForwardLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsAvailForwardLastTransitionTime.setStatus("current")
_MefSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Type = DateAndTime
_MefSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Object = MibTableColumn
mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime = _MefSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 2, 1, 6),
    _MefSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Type()
)
mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime.setStatus("current")
_MefSoamLmCurrentAvailStatsTable_Object = MibTable
mefSoamLmCurrentAvailStatsTable = _MefSoamLmCurrentAvailStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsTable.setStatus("current")
_MefSoamLmCurrentAvailStatsEntry_Object = MibTableRow
mefSoamLmCurrentAvailStatsEntry = _MefSoamLmCurrentAvailStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1)
)
mefSoamLmCurrentAvailStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsEntry.setStatus("current")
_MefSoamLmCurrentAvailStatsIndex_Type = Unsigned32
_MefSoamLmCurrentAvailStatsIndex_Object = MibTableColumn
mefSoamLmCurrentAvailStatsIndex = _MefSoamLmCurrentAvailStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 1),
    _MefSoamLmCurrentAvailStatsIndex_Type()
)
mefSoamLmCurrentAvailStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsIndex.setStatus("current")
_MefSoamLmCurrentAvailStatsStartTime_Type = DateAndTime
_MefSoamLmCurrentAvailStatsStartTime_Object = MibTableColumn
mefSoamLmCurrentAvailStatsStartTime = _MefSoamLmCurrentAvailStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 2),
    _MefSoamLmCurrentAvailStatsStartTime_Type()
)
mefSoamLmCurrentAvailStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsStartTime.setStatus("current")
_MefSoamLmCurrentAvailStatsElapsedTime_Type = TimeInterval
_MefSoamLmCurrentAvailStatsElapsedTime_Object = MibTableColumn
mefSoamLmCurrentAvailStatsElapsedTime = _MefSoamLmCurrentAvailStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 3),
    _MefSoamLmCurrentAvailStatsElapsedTime_Type()
)
mefSoamLmCurrentAvailStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsElapsedTime.setStatus("current")
_MefSoamLmCurrentAvailStatsSuspect_Type = TruthValue
_MefSoamLmCurrentAvailStatsSuspect_Object = MibTableColumn
mefSoamLmCurrentAvailStatsSuspect = _MefSoamLmCurrentAvailStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 4),
    _MefSoamLmCurrentAvailStatsSuspect_Type()
)
mefSoamLmCurrentAvailStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsSuspect.setStatus("current")
_MefSoamLmCurrentAvailStatsForwardHighLoss_Type = Unsigned32
_MefSoamLmCurrentAvailStatsForwardHighLoss_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardHighLoss = _MefSoamLmCurrentAvailStatsForwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 5),
    _MefSoamLmCurrentAvailStatsForwardHighLoss_Type()
)
mefSoamLmCurrentAvailStatsForwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardHighLoss.setStatus("current")
_MefSoamLmCurrentAvailStatsBackwardHighLoss_Type = Unsigned32
_MefSoamLmCurrentAvailStatsBackwardHighLoss_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardHighLoss = _MefSoamLmCurrentAvailStatsBackwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 6),
    _MefSoamLmCurrentAvailStatsBackwardHighLoss_Type()
)
mefSoamLmCurrentAvailStatsBackwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardHighLoss.setStatus("current")
_MefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Type = Unsigned32
_MefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss = _MefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 7),
    _MefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Type()
)
mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss.setStatus("current")
_MefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Type = Unsigned32
_MefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss = _MefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 8),
    _MefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Type()
)
mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss.setStatus("current")
_MefSoamLmCurrentAvailStatsForwardAvailable_Type = Gauge32
_MefSoamLmCurrentAvailStatsForwardAvailable_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardAvailable = _MefSoamLmCurrentAvailStatsForwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 9),
    _MefSoamLmCurrentAvailStatsForwardAvailable_Type()
)
mefSoamLmCurrentAvailStatsForwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardAvailable.setStatus("current")
_MefSoamLmCurrentAvailStatsBackwardAvailable_Type = Gauge32
_MefSoamLmCurrentAvailStatsBackwardAvailable_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardAvailable = _MefSoamLmCurrentAvailStatsBackwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 10),
    _MefSoamLmCurrentAvailStatsBackwardAvailable_Type()
)
mefSoamLmCurrentAvailStatsBackwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardAvailable.setStatus("current")
_MefSoamLmCurrentAvailStatsForwardUnavailable_Type = Gauge32
_MefSoamLmCurrentAvailStatsForwardUnavailable_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardUnavailable = _MefSoamLmCurrentAvailStatsForwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 11),
    _MefSoamLmCurrentAvailStatsForwardUnavailable_Type()
)
mefSoamLmCurrentAvailStatsForwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardUnavailable.setStatus("current")
_MefSoamLmCurrentAvailStatsBackwardUnavailable_Type = Gauge32
_MefSoamLmCurrentAvailStatsBackwardUnavailable_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardUnavailable = _MefSoamLmCurrentAvailStatsBackwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 12),
    _MefSoamLmCurrentAvailStatsBackwardUnavailable_Type()
)
mefSoamLmCurrentAvailStatsBackwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardUnavailable.setStatus("current")


class _MefSoamLmCurrentAvailStatsForwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsForwardMinFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardMinFlr = _MefSoamLmCurrentAvailStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 13),
    _MefSoamLmCurrentAvailStatsForwardMinFlr_Type()
)
mefSoamLmCurrentAvailStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardMinFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsForwardMaxFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardMaxFlr = _MefSoamLmCurrentAvailStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 14),
    _MefSoamLmCurrentAvailStatsForwardMaxFlr_Type()
)
mefSoamLmCurrentAvailStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsForwardAvgFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsForwardAvgFlr = _MefSoamLmCurrentAvailStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 15),
    _MefSoamLmCurrentAvailStatsForwardAvgFlr_Type()
)
mefSoamLmCurrentAvailStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsForwardAvgFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsBackwardMinFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardMinFlr = _MefSoamLmCurrentAvailStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 16),
    _MefSoamLmCurrentAvailStatsBackwardMinFlr_Type()
)
mefSoamLmCurrentAvailStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardMinFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsBackwardMaxFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardMaxFlr = _MefSoamLmCurrentAvailStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 17),
    _MefSoamLmCurrentAvailStatsBackwardMaxFlr_Type()
)
mefSoamLmCurrentAvailStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmCurrentAvailStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentAvailStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentAvailStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentAvailStatsBackwardAvgFlr_Object = MibTableColumn
mefSoamLmCurrentAvailStatsBackwardAvgFlr = _MefSoamLmCurrentAvailStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 3, 1, 18),
    _MefSoamLmCurrentAvailStatsBackwardAvgFlr_Type()
)
mefSoamLmCurrentAvailStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsBackwardAvgFlr.setUnits("milli-percent")
_MefSoamLmCurrentStatsTable_Object = MibTable
mefSoamLmCurrentStatsTable = _MefSoamLmCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsTable.setStatus("current")
_MefSoamLmCurrentStatsEntry_Object = MibTableRow
mefSoamLmCurrentStatsEntry = _MefSoamLmCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1)
)
mefSoamLmCurrentStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsEntry.setStatus("current")
_MefSoamLmCurrentStatsIndex_Type = Unsigned32
_MefSoamLmCurrentStatsIndex_Object = MibTableColumn
mefSoamLmCurrentStatsIndex = _MefSoamLmCurrentStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 1),
    _MefSoamLmCurrentStatsIndex_Type()
)
mefSoamLmCurrentStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsIndex.setStatus("current")
_MefSoamLmCurrentStatsStartTime_Type = DateAndTime
_MefSoamLmCurrentStatsStartTime_Object = MibTableColumn
mefSoamLmCurrentStatsStartTime = _MefSoamLmCurrentStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 2),
    _MefSoamLmCurrentStatsStartTime_Type()
)
mefSoamLmCurrentStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsStartTime.setStatus("current")
_MefSoamLmCurrentStatsElapsedTime_Type = TimeInterval
_MefSoamLmCurrentStatsElapsedTime_Object = MibTableColumn
mefSoamLmCurrentStatsElapsedTime = _MefSoamLmCurrentStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 3),
    _MefSoamLmCurrentStatsElapsedTime_Type()
)
mefSoamLmCurrentStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsElapsedTime.setStatus("current")
_MefSoamLmCurrentStatsSuspect_Type = TruthValue
_MefSoamLmCurrentStatsSuspect_Object = MibTableColumn
mefSoamLmCurrentStatsSuspect = _MefSoamLmCurrentStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 4),
    _MefSoamLmCurrentStatsSuspect_Type()
)
mefSoamLmCurrentStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsSuspect.setStatus("current")
_MefSoamLmCurrentStatsForwardTransmittedFrames_Type = Gauge32
_MefSoamLmCurrentStatsForwardTransmittedFrames_Object = MibTableColumn
mefSoamLmCurrentStatsForwardTransmittedFrames = _MefSoamLmCurrentStatsForwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 5),
    _MefSoamLmCurrentStatsForwardTransmittedFrames_Type()
)
mefSoamLmCurrentStatsForwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardTransmittedFrames.setStatus("current")
_MefSoamLmCurrentStatsForwardReceivedFrames_Type = Gauge32
_MefSoamLmCurrentStatsForwardReceivedFrames_Object = MibTableColumn
mefSoamLmCurrentStatsForwardReceivedFrames = _MefSoamLmCurrentStatsForwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 6),
    _MefSoamLmCurrentStatsForwardReceivedFrames_Type()
)
mefSoamLmCurrentStatsForwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardReceivedFrames.setStatus("current")


class _MefSoamLmCurrentStatsForwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsForwardMinFlr_Object = MibTableColumn
mefSoamLmCurrentStatsForwardMinFlr = _MefSoamLmCurrentStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 7),
    _MefSoamLmCurrentStatsForwardMinFlr_Type()
)
mefSoamLmCurrentStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardMinFlr.setUnits("milli-percent")


class _MefSoamLmCurrentStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsForwardMaxFlr_Object = MibTableColumn
mefSoamLmCurrentStatsForwardMaxFlr = _MefSoamLmCurrentStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 8),
    _MefSoamLmCurrentStatsForwardMaxFlr_Type()
)
mefSoamLmCurrentStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmCurrentStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsForwardAvgFlr_Object = MibTableColumn
mefSoamLmCurrentStatsForwardAvgFlr = _MefSoamLmCurrentStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 9),
    _MefSoamLmCurrentStatsForwardAvgFlr_Type()
)
mefSoamLmCurrentStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsForwardAvgFlr.setUnits("milli-percent")
_MefSoamLmCurrentStatsBackwardTransmittedFrames_Type = Gauge32
_MefSoamLmCurrentStatsBackwardTransmittedFrames_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardTransmittedFrames = _MefSoamLmCurrentStatsBackwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 10),
    _MefSoamLmCurrentStatsBackwardTransmittedFrames_Type()
)
mefSoamLmCurrentStatsBackwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardTransmittedFrames.setStatus("current")
_MefSoamLmCurrentStatsBackwardReceivedFrames_Type = Gauge32
_MefSoamLmCurrentStatsBackwardReceivedFrames_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardReceivedFrames = _MefSoamLmCurrentStatsBackwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 11),
    _MefSoamLmCurrentStatsBackwardReceivedFrames_Type()
)
mefSoamLmCurrentStatsBackwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardReceivedFrames.setStatus("current")


class _MefSoamLmCurrentStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsBackwardMinFlr_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardMinFlr = _MefSoamLmCurrentStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 12),
    _MefSoamLmCurrentStatsBackwardMinFlr_Type()
)
mefSoamLmCurrentStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardMinFlr.setUnits("milli-percent")


class _MefSoamLmCurrentStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsBackwardMaxFlr_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardMaxFlr = _MefSoamLmCurrentStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 13),
    _MefSoamLmCurrentStatsBackwardMaxFlr_Type()
)
mefSoamLmCurrentStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmCurrentStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmCurrentStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmCurrentStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmCurrentStatsBackwardAvgFlr_Object = MibTableColumn
mefSoamLmCurrentStatsBackwardAvgFlr = _MefSoamLmCurrentStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 14),
    _MefSoamLmCurrentStatsBackwardAvgFlr_Type()
)
mefSoamLmCurrentStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsBackwardAvgFlr.setUnits("milli-percent")
_MefSoamLmCurrentStatsSoamPdusSent_Type = Gauge32
_MefSoamLmCurrentStatsSoamPdusSent_Object = MibTableColumn
mefSoamLmCurrentStatsSoamPdusSent = _MefSoamLmCurrentStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 15),
    _MefSoamLmCurrentStatsSoamPdusSent_Type()
)
mefSoamLmCurrentStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsSoamPdusSent.setStatus("current")
_MefSoamLmCurrentStatsSoamPdusReceived_Type = Gauge32
_MefSoamLmCurrentStatsSoamPdusReceived_Object = MibTableColumn
mefSoamLmCurrentStatsSoamPdusReceived = _MefSoamLmCurrentStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 4, 1, 16),
    _MefSoamLmCurrentStatsSoamPdusReceived_Type()
)
mefSoamLmCurrentStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsSoamPdusReceived.setStatus("current")
_MefSoamLmHistoryAvailStatsTable_Object = MibTable
mefSoamLmHistoryAvailStatsTable = _MefSoamLmHistoryAvailStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsTable.setStatus("current")
_MefSoamLmHistoryAvailStatsEntry_Object = MibTableRow
mefSoamLmHistoryAvailStatsEntry = _MefSoamLmHistoryAvailStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1)
)
mefSoamLmHistoryAvailStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsEntry.setStatus("current")
_MefSoamLmHistoryAvailStatsIndex_Type = Unsigned32
_MefSoamLmHistoryAvailStatsIndex_Object = MibTableColumn
mefSoamLmHistoryAvailStatsIndex = _MefSoamLmHistoryAvailStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 1),
    _MefSoamLmHistoryAvailStatsIndex_Type()
)
mefSoamLmHistoryAvailStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsIndex.setStatus("current")
_MefSoamLmHistoryAvailStatsEndTime_Type = DateAndTime
_MefSoamLmHistoryAvailStatsEndTime_Object = MibTableColumn
mefSoamLmHistoryAvailStatsEndTime = _MefSoamLmHistoryAvailStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 2),
    _MefSoamLmHistoryAvailStatsEndTime_Type()
)
mefSoamLmHistoryAvailStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsEndTime.setStatus("current")
_MefSoamLmHistoryAvailStatsElapsedTime_Type = TimeInterval
_MefSoamLmHistoryAvailStatsElapsedTime_Object = MibTableColumn
mefSoamLmHistoryAvailStatsElapsedTime = _MefSoamLmHistoryAvailStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 3),
    _MefSoamLmHistoryAvailStatsElapsedTime_Type()
)
mefSoamLmHistoryAvailStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsElapsedTime.setStatus("current")
_MefSoamLmHistoryAvailStatsSuspect_Type = TruthValue
_MefSoamLmHistoryAvailStatsSuspect_Object = MibTableColumn
mefSoamLmHistoryAvailStatsSuspect = _MefSoamLmHistoryAvailStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 4),
    _MefSoamLmHistoryAvailStatsSuspect_Type()
)
mefSoamLmHistoryAvailStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsSuspect.setStatus("current")
_MefSoamLmHistoryAvailStatsForwardHighLoss_Type = Unsigned32
_MefSoamLmHistoryAvailStatsForwardHighLoss_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardHighLoss = _MefSoamLmHistoryAvailStatsForwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 5),
    _MefSoamLmHistoryAvailStatsForwardHighLoss_Type()
)
mefSoamLmHistoryAvailStatsForwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardHighLoss.setStatus("current")
_MefSoamLmHistoryAvailStatsBackwardHighLoss_Type = Unsigned32
_MefSoamLmHistoryAvailStatsBackwardHighLoss_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardHighLoss = _MefSoamLmHistoryAvailStatsBackwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 6),
    _MefSoamLmHistoryAvailStatsBackwardHighLoss_Type()
)
mefSoamLmHistoryAvailStatsBackwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardHighLoss.setStatus("current")
_MefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Type = Unsigned32
_MefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss = _MefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 7),
    _MefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Type()
)
mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss.setStatus("current")
_MefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Type = Unsigned32
_MefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss = _MefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 8),
    _MefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Type()
)
mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss.setStatus("current")
_MefSoamLmHistoryAvailStatsForwardAvailable_Type = Gauge32
_MefSoamLmHistoryAvailStatsForwardAvailable_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardAvailable = _MefSoamLmHistoryAvailStatsForwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 9),
    _MefSoamLmHistoryAvailStatsForwardAvailable_Type()
)
mefSoamLmHistoryAvailStatsForwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardAvailable.setStatus("current")
_MefSoamLmHistoryAvailStatsBackwardAvailable_Type = Gauge32
_MefSoamLmHistoryAvailStatsBackwardAvailable_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardAvailable = _MefSoamLmHistoryAvailStatsBackwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 10),
    _MefSoamLmHistoryAvailStatsBackwardAvailable_Type()
)
mefSoamLmHistoryAvailStatsBackwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardAvailable.setStatus("current")
_MefSoamLmHistoryAvailStatsForwardUnavailable_Type = Gauge32
_MefSoamLmHistoryAvailStatsForwardUnavailable_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardUnavailable = _MefSoamLmHistoryAvailStatsForwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 11),
    _MefSoamLmHistoryAvailStatsForwardUnavailable_Type()
)
mefSoamLmHistoryAvailStatsForwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardUnavailable.setStatus("current")
_MefSoamLmHistoryAvailStatsBackwardUnavailable_Type = Gauge32
_MefSoamLmHistoryAvailStatsBackwardUnavailable_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardUnavailable = _MefSoamLmHistoryAvailStatsBackwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 12),
    _MefSoamLmHistoryAvailStatsBackwardUnavailable_Type()
)
mefSoamLmHistoryAvailStatsBackwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardUnavailable.setStatus("current")


class _MefSoamLmHistoryAvailStatsForwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsForwardMinFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardMinFlr = _MefSoamLmHistoryAvailStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 13),
    _MefSoamLmHistoryAvailStatsForwardMinFlr_Type()
)
mefSoamLmHistoryAvailStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardMinFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsForwardMaxFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardMaxFlr = _MefSoamLmHistoryAvailStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 14),
    _MefSoamLmHistoryAvailStatsForwardMaxFlr_Type()
)
mefSoamLmHistoryAvailStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsForwardAvgFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsForwardAvgFlr = _MefSoamLmHistoryAvailStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 15),
    _MefSoamLmHistoryAvailStatsForwardAvgFlr_Type()
)
mefSoamLmHistoryAvailStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsForwardAvgFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsBackwardMinFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardMinFlr = _MefSoamLmHistoryAvailStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 16),
    _MefSoamLmHistoryAvailStatsBackwardMinFlr_Type()
)
mefSoamLmHistoryAvailStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardMinFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsBackwardMaxFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardMaxFlr = _MefSoamLmHistoryAvailStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 17),
    _MefSoamLmHistoryAvailStatsBackwardMaxFlr_Type()
)
mefSoamLmHistoryAvailStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmHistoryAvailStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryAvailStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryAvailStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryAvailStatsBackwardAvgFlr_Object = MibTableColumn
mefSoamLmHistoryAvailStatsBackwardAvgFlr = _MefSoamLmHistoryAvailStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 5, 1, 18),
    _MefSoamLmHistoryAvailStatsBackwardAvgFlr_Type()
)
mefSoamLmHistoryAvailStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsBackwardAvgFlr.setUnits("milli-percent")
_MefSoamLmHistoryStatsTable_Object = MibTable
mefSoamLmHistoryStatsTable = _MefSoamLmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsTable.setStatus("current")
_MefSoamLmHistoryStatsEntry_Object = MibTableRow
mefSoamLmHistoryStatsEntry = _MefSoamLmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1)
)
mefSoamLmHistoryStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsEntry.setStatus("current")
_MefSoamLmHistoryStatsIndex_Type = Unsigned32
_MefSoamLmHistoryStatsIndex_Object = MibTableColumn
mefSoamLmHistoryStatsIndex = _MefSoamLmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 1),
    _MefSoamLmHistoryStatsIndex_Type()
)
mefSoamLmHistoryStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsIndex.setStatus("current")
_MefSoamLmHistoryStatsEndTime_Type = DateAndTime
_MefSoamLmHistoryStatsEndTime_Object = MibTableColumn
mefSoamLmHistoryStatsEndTime = _MefSoamLmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 2),
    _MefSoamLmHistoryStatsEndTime_Type()
)
mefSoamLmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsEndTime.setStatus("current")
_MefSoamLmHistoryStatsElapsedTime_Type = TimeInterval
_MefSoamLmHistoryStatsElapsedTime_Object = MibTableColumn
mefSoamLmHistoryStatsElapsedTime = _MefSoamLmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 3),
    _MefSoamLmHistoryStatsElapsedTime_Type()
)
mefSoamLmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsElapsedTime.setStatus("current")
_MefSoamLmHistoryStatsSuspect_Type = TruthValue
_MefSoamLmHistoryStatsSuspect_Object = MibTableColumn
mefSoamLmHistoryStatsSuspect = _MefSoamLmHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 4),
    _MefSoamLmHistoryStatsSuspect_Type()
)
mefSoamLmHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsSuspect.setStatus("current")
_MefSoamLmHistoryStatsForwardTransmittedFrames_Type = Gauge32
_MefSoamLmHistoryStatsForwardTransmittedFrames_Object = MibTableColumn
mefSoamLmHistoryStatsForwardTransmittedFrames = _MefSoamLmHistoryStatsForwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 5),
    _MefSoamLmHistoryStatsForwardTransmittedFrames_Type()
)
mefSoamLmHistoryStatsForwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardTransmittedFrames.setStatus("current")
_MefSoamLmHistoryStatsForwardReceivedFrames_Type = Gauge32
_MefSoamLmHistoryStatsForwardReceivedFrames_Object = MibTableColumn
mefSoamLmHistoryStatsForwardReceivedFrames = _MefSoamLmHistoryStatsForwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 6),
    _MefSoamLmHistoryStatsForwardReceivedFrames_Type()
)
mefSoamLmHistoryStatsForwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardReceivedFrames.setStatus("current")


class _MefSoamLmHistoryStatsForwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsForwardMinFlr_Object = MibTableColumn
mefSoamLmHistoryStatsForwardMinFlr = _MefSoamLmHistoryStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 7),
    _MefSoamLmHistoryStatsForwardMinFlr_Type()
)
mefSoamLmHistoryStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardMinFlr.setUnits("milli-percent")


class _MefSoamLmHistoryStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsForwardMaxFlr_Object = MibTableColumn
mefSoamLmHistoryStatsForwardMaxFlr = _MefSoamLmHistoryStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 8),
    _MefSoamLmHistoryStatsForwardMaxFlr_Type()
)
mefSoamLmHistoryStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmHistoryStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsForwardAvgFlr_Object = MibTableColumn
mefSoamLmHistoryStatsForwardAvgFlr = _MefSoamLmHistoryStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 9),
    _MefSoamLmHistoryStatsForwardAvgFlr_Type()
)
mefSoamLmHistoryStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsForwardAvgFlr.setUnits("milli-percent")
_MefSoamLmHistoryStatsBackwardTransmittedFrames_Type = Gauge32
_MefSoamLmHistoryStatsBackwardTransmittedFrames_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardTransmittedFrames = _MefSoamLmHistoryStatsBackwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 10),
    _MefSoamLmHistoryStatsBackwardTransmittedFrames_Type()
)
mefSoamLmHistoryStatsBackwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardTransmittedFrames.setStatus("current")
_MefSoamLmHistoryStatsBackwardReceivedFrames_Type = Gauge32
_MefSoamLmHistoryStatsBackwardReceivedFrames_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardReceivedFrames = _MefSoamLmHistoryStatsBackwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 11),
    _MefSoamLmHistoryStatsBackwardReceivedFrames_Type()
)
mefSoamLmHistoryStatsBackwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardReceivedFrames.setStatus("current")


class _MefSoamLmHistoryStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsBackwardMinFlr_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardMinFlr = _MefSoamLmHistoryStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 12),
    _MefSoamLmHistoryStatsBackwardMinFlr_Type()
)
mefSoamLmHistoryStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardMinFlr.setUnits("milli-percent")


class _MefSoamLmHistoryStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsBackwardMaxFlr_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardMaxFlr = _MefSoamLmHistoryStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 13),
    _MefSoamLmHistoryStatsBackwardMaxFlr_Type()
)
mefSoamLmHistoryStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardMaxFlr.setUnits("milli-percent")


class _MefSoamLmHistoryStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type mefSoamLmHistoryStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MefSoamLmHistoryStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_MefSoamLmHistoryStatsBackwardAvgFlr_Object = MibTableColumn
mefSoamLmHistoryStatsBackwardAvgFlr = _MefSoamLmHistoryStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 14),
    _MefSoamLmHistoryStatsBackwardAvgFlr_Type()
)
mefSoamLmHistoryStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsBackwardAvgFlr.setUnits("milli-percent")
_MefSoamLmHistoryStatsSoamPdusSent_Type = Gauge32
_MefSoamLmHistoryStatsSoamPdusSent_Object = MibTableColumn
mefSoamLmHistoryStatsSoamPdusSent = _MefSoamLmHistoryStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 15),
    _MefSoamLmHistoryStatsSoamPdusSent_Type()
)
mefSoamLmHistoryStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsSoamPdusSent.setStatus("current")
_MefSoamLmHistoryStatsSoamPdusReceived_Type = Gauge32
_MefSoamLmHistoryStatsSoamPdusReceived_Object = MibTableColumn
mefSoamLmHistoryStatsSoamPdusReceived = _MefSoamLmHistoryStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 6, 1, 16),
    _MefSoamLmHistoryStatsSoamPdusReceived_Type()
)
mefSoamLmHistoryStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsSoamPdusReceived.setStatus("current")
_MefSoamLmTcaCfgTable_Object = MibTable
mefSoamLmTcaCfgTable = _MefSoamLmTcaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8)
)
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgTable.setStatus("current")
_MefSoamLmTcaCfgEntry_Object = MibTableRow
mefSoamLmTcaCfgEntry = _MefSoamLmTcaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1)
)
mefSoamLmTcaCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmTcaCfgType"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamLmTcaCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgEntry.setStatus("current")


class _MefSoamLmTcaCfgIndex_Type(Unsigned32):
    """Custom type mefSoamLmTcaCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamLmTcaCfgIndex_Type.__name__ = "Unsigned32"
_MefSoamLmTcaCfgIndex_Object = MibTableColumn
mefSoamLmTcaCfgIndex = _MefSoamLmTcaCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1, 1),
    _MefSoamLmTcaCfgIndex_Type()
)
mefSoamLmTcaCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgIndex.setStatus("current")


class _MefSoamLmTcaCfgType_Type(Integer32):
    """Custom type mefSoamLmTcaCfgType based on Integer32"""
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
        *(("undefined", 0),
          ("hliForward", 1),
          ("chliForward", 2),
          ("hliBackward", 3),
          ("chliBackward", 4))
    )


_MefSoamLmTcaCfgType_Type.__name__ = "Integer32"
_MefSoamLmTcaCfgType_Object = MibTableColumn
mefSoamLmTcaCfgType = _MefSoamLmTcaCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1, 2),
    _MefSoamLmTcaCfgType_Type()
)
mefSoamLmTcaCfgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgType.setStatus("current")


class _MefSoamLmTcaCfgEnable_Type(TruthValue):
    """Custom type mefSoamLmTcaCfgEnable based on TruthValue"""
    defaultValue = 1


_MefSoamLmTcaCfgEnable_Type.__name__ = "TruthValue"
_MefSoamLmTcaCfgEnable_Object = MibTableColumn
mefSoamLmTcaCfgEnable = _MefSoamLmTcaCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1, 3),
    _MefSoamLmTcaCfgEnable_Type()
)
mefSoamLmTcaCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgEnable.setStatus("current")


class _MefSoamLmTcaCfgAlarmType_Type(Integer32):
    """Custom type mefSoamLmTcaCfgAlarmType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateless", 1),
          ("stateful", 2))
    )


_MefSoamLmTcaCfgAlarmType_Type.__name__ = "Integer32"
_MefSoamLmTcaCfgAlarmType_Object = MibTableColumn
mefSoamLmTcaCfgAlarmType = _MefSoamLmTcaCfgAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1, 4),
    _MefSoamLmTcaCfgAlarmType_Type()
)
mefSoamLmTcaCfgAlarmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgAlarmType.setStatus("current")


class _MefSoamLmTcaCfgThresholdValue_Type(Integer32):
    """Custom type mefSoamLmTcaCfgThresholdValue based on Integer32"""
    defaultValue = 1


_MefSoamLmTcaCfgThresholdValue_Type.__name__ = "Integer32"
_MefSoamLmTcaCfgThresholdValue_Object = MibTableColumn
mefSoamLmTcaCfgThresholdValue = _MefSoamLmTcaCfgThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1, 5),
    _MefSoamLmTcaCfgThresholdValue_Type()
)
mefSoamLmTcaCfgThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgThresholdValue.setStatus("current")


class _MefSoamLmTcaCfgClearValue_Type(Integer32):
    """Custom type mefSoamLmTcaCfgClearValue based on Integer32"""
    defaultValue = 1


_MefSoamLmTcaCfgClearValue_Type.__name__ = "Integer32"
_MefSoamLmTcaCfgClearValue_Object = MibTableColumn
mefSoamLmTcaCfgClearValue = _MefSoamLmTcaCfgClearValue_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1, 6),
    _MefSoamLmTcaCfgClearValue_Type()
)
mefSoamLmTcaCfgClearValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgClearValue.setStatus("current")


class _MefSoamLmTcaCfgAlarmCurrentState_Type(Integer32):
    """Custom type mefSoamLmTcaCfgAlarmCurrentState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_MefSoamLmTcaCfgAlarmCurrentState_Type.__name__ = "Integer32"
_MefSoamLmTcaCfgAlarmCurrentState_Object = MibTableColumn
mefSoamLmTcaCfgAlarmCurrentState = _MefSoamLmTcaCfgAlarmCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1, 7),
    _MefSoamLmTcaCfgAlarmCurrentState_Type()
)
mefSoamLmTcaCfgAlarmCurrentState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgAlarmCurrentState.setStatus("current")
_MefSoamLmTcaCfgRowStatus_Type = RowStatus
_MefSoamLmTcaCfgRowStatus_Object = MibTableColumn
mefSoamLmTcaCfgRowStatus = _MefSoamLmTcaCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 2, 8, 1, 8),
    _MefSoamLmTcaCfgRowStatus_Type()
)
mefSoamLmTcaCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamLmTcaCfgRowStatus.setStatus("current")
_MefSoamPmDmObjects_ObjectIdentity = ObjectIdentity
mefSoamPmDmObjects = _MefSoamPmDmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3)
)
_MefSoamDmCfgTable_Object = MibTable
mefSoamDmCfgTable = _MefSoamDmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mefSoamDmCfgTable.setStatus("current")
_MefSoamDmCfgEntry_Object = MibTableRow
mefSoamDmCfgEntry = _MefSoamDmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1)
)
mefSoamDmCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmCfgEntry.setStatus("current")


class _MefSoamDmCfgIndex_Type(Unsigned32):
    """Custom type mefSoamDmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamDmCfgIndex_Type.__name__ = "Unsigned32"
_MefSoamDmCfgIndex_Object = MibTableColumn
mefSoamDmCfgIndex = _MefSoamDmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 1),
    _MefSoamDmCfgIndex_Type()
)
mefSoamDmCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmCfgIndex.setStatus("current")


class _MefSoamDmCfgType_Type(Integer32):
    """Custom type mefSoamDmCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dmDmm", 1),
          ("dm1DmTx", 2),
          ("dm1DmRx", 3))
    )


_MefSoamDmCfgType_Type.__name__ = "Integer32"
_MefSoamDmCfgType_Object = MibTableColumn
mefSoamDmCfgType = _MefSoamDmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 2),
    _MefSoamDmCfgType_Type()
)
mefSoamDmCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgType.setStatus("current")


class _MefSoamDmCfgVersion_Type(Unsigned32):
    """Custom type mefSoamDmCfgVersion based on Unsigned32"""
    defaultValue = 0


_MefSoamDmCfgVersion_Type.__name__ = "Unsigned32"
_MefSoamDmCfgVersion_Object = MibTableColumn
mefSoamDmCfgVersion = _MefSoamDmCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 3),
    _MefSoamDmCfgVersion_Type()
)
mefSoamDmCfgVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgVersion.setStatus("current")


class _MefSoamDmCfgEnabled_Type(TruthValue):
    """Custom type mefSoamDmCfgEnabled based on TruthValue"""
    defaultValue = 1


_MefSoamDmCfgEnabled_Type.__name__ = "TruthValue"
_MefSoamDmCfgEnabled_Object = MibTableColumn
mefSoamDmCfgEnabled = _MefSoamDmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 4),
    _MefSoamDmCfgEnabled_Type()
)
mefSoamDmCfgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgEnabled.setStatus("current")


class _MefSoamDmCfgMeasurementEnable_Type(Bits):
    """Custom type mefSoamDmCfgMeasurementEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bSoamPdusSent", 0),
          ("bSoamPdusReceived", 1),
          ("bFrameDelayTwoWayBins", 2),
          ("bFrameDelayTwoWayMin", 3),
          ("bFrameDelayTwoWayMax", 4),
          ("bFrameDelayTwoWayAvg", 5),
          ("bFrameDelayForwardBins", 6),
          ("bFrameDelayForwardMin", 7),
          ("bFrameDelayForwardMax", 8),
          ("bFrameDelayForwardAvg", 9),
          ("bFrameDelayBackwardBins", 10),
          ("bFrameDelayBackwardMin", 11),
          ("bFrameDelayBackwardMax", 12),
          ("bFrameDelayBackwardAvg", 13),
          ("bIfdvForwardBins", 14),
          ("bIfdvForwardMax", 16),
          ("bIfdvForwardAvg", 17),
          ("bIfdvBackwardBins", 18),
          ("bIfdvBackwardMax", 20),
          ("bIfdvBackwardAvg", 21),
          ("bIfdvTwoWayBins", 22),
          ("bIfdvTwoWayMax", 24),
          ("bIfdvTwoWayAvg", 25),
          ("bFrameDelayRangeForwardBins", 26),
          ("bFrameDelayRangeForwardMax", 27),
          ("bFrameDelayRangeForwardAvg", 28),
          ("bFrameDelayRangeBackwardBins", 29),
          ("bFrameDelayRangeBackwardMax", 30),
          ("bFrameDelayRangeBackwardAvg", 31),
          ("bFrameDelayRangeTwoWayBins", 32),
          ("bFrameDelayRangeTwoWayMax", 33),
          ("bFrameDelayRangeTwoWayAvg", 34),
          ("bMeasuredStatsFrameDelayTwoWay", 35),
          ("bMeasuredStatsFrameDelayForward", 36),
          ("bMeasuredStatsFrameDelayBackward", 37),
          ("bMeasuredStatsIfdvTwoWay", 38),
          ("bMeasuredStatsIfdvForward", 39),
          ("bMeasuredStatsIfdvBackward", 40))
    )

_MefSoamDmCfgMeasurementEnable_Type.__name__ = "Bits"
_MefSoamDmCfgMeasurementEnable_Object = MibTableColumn
mefSoamDmCfgMeasurementEnable = _MefSoamDmCfgMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 5),
    _MefSoamDmCfgMeasurementEnable_Type()
)
mefSoamDmCfgMeasurementEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasurementEnable.setStatus("current")


class _MefSoamDmCfgMessagePeriod_Type(MefSoamTcMeasurementPeriodType):
    """Custom type mefSoamDmCfgMessagePeriod based on MefSoamTcMeasurementPeriodType"""
    defaultValue = 1000


_MefSoamDmCfgMessagePeriod_Type.__name__ = "MefSoamTcMeasurementPeriodType"
_MefSoamDmCfgMessagePeriod_Object = MibTableColumn
mefSoamDmCfgMessagePeriod = _MefSoamDmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 6),
    _MefSoamDmCfgMessagePeriod_Type()
)
mefSoamDmCfgMessagePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgMessagePeriod.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgMessagePeriod.setUnits("ms")
_MefSoamDmCfgPriority_Type = IEEE8021PriorityValue
_MefSoamDmCfgPriority_Object = MibTableColumn
mefSoamDmCfgPriority = _MefSoamDmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 7),
    _MefSoamDmCfgPriority_Type()
)
mefSoamDmCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgPriority.setStatus("current")


class _MefSoamDmCfgFrameSize_Type(Unsigned32):
    """Custom type mefSoamDmCfgFrameSize based on Unsigned32"""
    defaultValue = 64


_MefSoamDmCfgFrameSize_Type.__name__ = "Unsigned32"
_MefSoamDmCfgFrameSize_Object = MibTableColumn
mefSoamDmCfgFrameSize = _MefSoamDmCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 8),
    _MefSoamDmCfgFrameSize_Type()
)
mefSoamDmCfgFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgFrameSize.setStatus("current")


class _MefSoamDmCfgDataPattern_Type(MefSoamTcDataPatternType):
    """Custom type mefSoamDmCfgDataPattern based on MefSoamTcDataPatternType"""
    defaultValue = 1


_MefSoamDmCfgDataPattern_Type.__name__ = "MefSoamTcDataPatternType"
_MefSoamDmCfgDataPattern_Object = MibTableColumn
mefSoamDmCfgDataPattern = _MefSoamDmCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 9),
    _MefSoamDmCfgDataPattern_Type()
)
mefSoamDmCfgDataPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDataPattern.setStatus("current")


class _MefSoamDmCfgTestTlvIncluded_Type(TruthValue):
    """Custom type mefSoamDmCfgTestTlvIncluded based on TruthValue"""
    defaultValue = 2


_MefSoamDmCfgTestTlvIncluded_Type.__name__ = "TruthValue"
_MefSoamDmCfgTestTlvIncluded_Object = MibTableColumn
mefSoamDmCfgTestTlvIncluded = _MefSoamDmCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 10),
    _MefSoamDmCfgTestTlvIncluded_Type()
)
mefSoamDmCfgTestTlvIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgTestTlvIncluded.setStatus("current")


class _MefSoamDmCfgTestTlvPattern_Type(MefSoamTcTestPatternType):
    """Custom type mefSoamDmCfgTestTlvPattern based on MefSoamTcTestPatternType"""
    defaultValue = 1


_MefSoamDmCfgTestTlvPattern_Type.__name__ = "MefSoamTcTestPatternType"
_MefSoamDmCfgTestTlvPattern_Object = MibTableColumn
mefSoamDmCfgTestTlvPattern = _MefSoamDmCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 11),
    _MefSoamDmCfgTestTlvPattern_Type()
)
mefSoamDmCfgTestTlvPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgTestTlvPattern.setStatus("current")


class _MefSoamDmCfgMeasurementInterval_Type(Unsigned32):
    """Custom type mefSoamDmCfgMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_MefSoamDmCfgMeasurementInterval_Type.__name__ = "Unsigned32"
_MefSoamDmCfgMeasurementInterval_Object = MibTableColumn
mefSoamDmCfgMeasurementInterval = _MefSoamDmCfgMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 12),
    _MefSoamDmCfgMeasurementInterval_Type()
)
mefSoamDmCfgMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasurementInterval.setUnits("minutes")


class _MefSoamDmCfgNumIntervalsStored_Type(Unsigned32):
    """Custom type mefSoamDmCfgNumIntervalsStored based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1000),
    )


_MefSoamDmCfgNumIntervalsStored_Type.__name__ = "Unsigned32"
_MefSoamDmCfgNumIntervalsStored_Object = MibTableColumn
mefSoamDmCfgNumIntervalsStored = _MefSoamDmCfgNumIntervalsStored_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 13),
    _MefSoamDmCfgNumIntervalsStored_Type()
)
mefSoamDmCfgNumIntervalsStored.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgNumIntervalsStored.setStatus("current")
_MefSoamDmCfgDestMacAddress_Type = MacAddress
_MefSoamDmCfgDestMacAddress_Object = MibTableColumn
mefSoamDmCfgDestMacAddress = _MefSoamDmCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 14),
    _MefSoamDmCfgDestMacAddress_Type()
)
mefSoamDmCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDestMacAddress.setStatus("current")


class _MefSoamDmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type mefSoamDmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_MefSoamDmCfgDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_MefSoamDmCfgDestMepId_Object = MibTableColumn
mefSoamDmCfgDestMepId = _MefSoamDmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 15),
    _MefSoamDmCfgDestMepId_Type()
)
mefSoamDmCfgDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDestMepId.setStatus("current")


class _MefSoamDmCfgDestIsMepId_Type(TruthValue):
    """Custom type mefSoamDmCfgDestIsMepId based on TruthValue"""
    defaultValue = 1


_MefSoamDmCfgDestIsMepId_Type.__name__ = "TruthValue"
_MefSoamDmCfgDestIsMepId_Object = MibTableColumn
mefSoamDmCfgDestIsMepId = _MefSoamDmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 16),
    _MefSoamDmCfgDestIsMepId_Type()
)
mefSoamDmCfgDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDestIsMepId.setStatus("current")
_MefSoamDmCfgSourceMacAddress_Type = MacAddress
_MefSoamDmCfgSourceMacAddress_Object = MibTableColumn
mefSoamDmCfgSourceMacAddress = _MefSoamDmCfgSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 17),
    _MefSoamDmCfgSourceMacAddress_Type()
)
mefSoamDmCfgSourceMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgSourceMacAddress.setStatus("current")


class _MefSoamDmCfgStartTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamDmCfgStartTimeType based on MefSoamTcOperationTimeType"""
    defaultValue = 2


_MefSoamDmCfgStartTimeType_Type.__name__ = "MefSoamTcOperationTimeType"
_MefSoamDmCfgStartTimeType_Object = MibTableColumn
mefSoamDmCfgStartTimeType = _MefSoamDmCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 18),
    _MefSoamDmCfgStartTimeType_Type()
)
mefSoamDmCfgStartTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgStartTimeType.setStatus("current")


class _MefSoamDmCfgFixedStartDateAndTime_Type(DateAndTime):
    """Custom type mefSoamDmCfgFixedStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamDmCfgFixedStartDateAndTime_Type.__name__ = "DateAndTime"
_MefSoamDmCfgFixedStartDateAndTime_Object = MibTableColumn
mefSoamDmCfgFixedStartDateAndTime = _MefSoamDmCfgFixedStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 19),
    _MefSoamDmCfgFixedStartDateAndTime_Type()
)
mefSoamDmCfgFixedStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgFixedStartDateAndTime.setStatus("current")


class _MefSoamDmCfgRelativeStartTime_Type(TimeInterval):
    """Custom type mefSoamDmCfgRelativeStartTime based on TimeInterval"""
    defaultValue = 0


_MefSoamDmCfgRelativeStartTime_Type.__name__ = "TimeInterval"
_MefSoamDmCfgRelativeStartTime_Object = MibTableColumn
mefSoamDmCfgRelativeStartTime = _MefSoamDmCfgRelativeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 20),
    _MefSoamDmCfgRelativeStartTime_Type()
)
mefSoamDmCfgRelativeStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgRelativeStartTime.setStatus("current")


class _MefSoamDmCfgStopTimeType_Type(MefSoamTcOperationTimeType):
    """Custom type mefSoamDmCfgStopTimeType based on MefSoamTcOperationTimeType"""
    defaultValue = 1


_MefSoamDmCfgStopTimeType_Type.__name__ = "MefSoamTcOperationTimeType"
_MefSoamDmCfgStopTimeType_Object = MibTableColumn
mefSoamDmCfgStopTimeType = _MefSoamDmCfgStopTimeType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 21),
    _MefSoamDmCfgStopTimeType_Type()
)
mefSoamDmCfgStopTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgStopTimeType.setStatus("current")


class _MefSoamDmCfgFixedStopDateAndTime_Type(DateAndTime):
    """Custom type mefSoamDmCfgFixedStopDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MefSoamDmCfgFixedStopDateAndTime_Type.__name__ = "DateAndTime"
_MefSoamDmCfgFixedStopDateAndTime_Object = MibTableColumn
mefSoamDmCfgFixedStopDateAndTime = _MefSoamDmCfgFixedStopDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 22),
    _MefSoamDmCfgFixedStopDateAndTime_Type()
)
mefSoamDmCfgFixedStopDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgFixedStopDateAndTime.setStatus("current")


class _MefSoamDmCfgRelativeStopTime_Type(TimeInterval):
    """Custom type mefSoamDmCfgRelativeStopTime based on TimeInterval"""
    defaultValue = 0


_MefSoamDmCfgRelativeStopTime_Type.__name__ = "TimeInterval"
_MefSoamDmCfgRelativeStopTime_Object = MibTableColumn
mefSoamDmCfgRelativeStopTime = _MefSoamDmCfgRelativeStopTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 23),
    _MefSoamDmCfgRelativeStopTime_Type()
)
mefSoamDmCfgRelativeStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgRelativeStopTime.setStatus("current")


class _MefSoamDmCfgRepetitionTime_Type(Unsigned32):
    """Custom type mefSoamDmCfgRepetitionTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_MefSoamDmCfgRepetitionTime_Type.__name__ = "Unsigned32"
_MefSoamDmCfgRepetitionTime_Object = MibTableColumn
mefSoamDmCfgRepetitionTime = _MefSoamDmCfgRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 24),
    _MefSoamDmCfgRepetitionTime_Type()
)
mefSoamDmCfgRepetitionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgRepetitionTime.setUnits("seconds")


class _MefSoamDmCfgAlignMeasurementIntervals_Type(TruthValue):
    """Custom type mefSoamDmCfgAlignMeasurementIntervals based on TruthValue"""
    defaultValue = 1


_MefSoamDmCfgAlignMeasurementIntervals_Type.__name__ = "TruthValue"
_MefSoamDmCfgAlignMeasurementIntervals_Object = MibTableColumn
mefSoamDmCfgAlignMeasurementIntervals = _MefSoamDmCfgAlignMeasurementIntervals_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 25),
    _MefSoamDmCfgAlignMeasurementIntervals_Type()
)
mefSoamDmCfgAlignMeasurementIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgAlignMeasurementIntervals.setStatus("current")


class _MefSoamDmCfgAlignMeasurementOffset_Type(Unsigned32):
    """Custom type mefSoamDmCfgAlignMeasurementOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_MefSoamDmCfgAlignMeasurementOffset_Type.__name__ = "Unsigned32"
_MefSoamDmCfgAlignMeasurementOffset_Object = MibTableColumn
mefSoamDmCfgAlignMeasurementOffset = _MefSoamDmCfgAlignMeasurementOffset_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 26),
    _MefSoamDmCfgAlignMeasurementOffset_Type()
)
mefSoamDmCfgAlignMeasurementOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgAlignMeasurementOffset.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgAlignMeasurementOffset.setUnits("minutes")


class _MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type(Unsigned32):
    """Custom type mefSoamDmCfgNumMeasBinsPerFrameDelayInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type.__name__ = "Unsigned32"
_MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Object = MibTableColumn
mefSoamDmCfgNumMeasBinsPerFrameDelayInterval = _MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 27),
    _MefSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type()
)
mefSoamDmCfgNumMeasBinsPerFrameDelayInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgNumMeasBinsPerFrameDelayInterval.setStatus("current")


class _MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type(Unsigned32):
    """Custom type mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type.__name__ = "Unsigned32"
_MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Object = MibTableColumn
mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval = _MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 28),
    _MefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type()
)
mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval.setStatus("current")


class _MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Type(Unsigned32):
    """Custom type mefSoamDmCfgInterFrameDelayVariationSelectionOffset based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Type.__name__ = "Unsigned32"
_MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Object = MibTableColumn
mefSoamDmCfgInterFrameDelayVariationSelectionOffset = _MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 29),
    _MefSoamDmCfgInterFrameDelayVariationSelectionOffset_Type()
)
mefSoamDmCfgInterFrameDelayVariationSelectionOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgInterFrameDelayVariationSelectionOffset.setStatus("current")


class _MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type(Unsigned32):
    """Custom type mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type.__name__ = "Unsigned32"
_MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Object = MibTableColumn
mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval = _MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 30),
    _MefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type()
)
mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval.setStatus("current")


class _MefSoamDmCfgSessionType_Type(MefSoamTcSessionType):
    """Custom type mefSoamDmCfgSessionType based on MefSoamTcSessionType"""
    defaultValue = 1


_MefSoamDmCfgSessionType_Type.__name__ = "MefSoamTcSessionType"
_MefSoamDmCfgSessionType_Object = MibTableColumn
mefSoamDmCfgSessionType = _MefSoamDmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 31),
    _MefSoamDmCfgSessionType_Type()
)
mefSoamDmCfgSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgSessionType.setStatus("current")
_MefSoamDmCfgSessionStatus_Type = MefSoamTcStatusType
_MefSoamDmCfgSessionStatus_Object = MibTableColumn
mefSoamDmCfgSessionStatus = _MefSoamDmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 32),
    _MefSoamDmCfgSessionStatus_Type()
)
mefSoamDmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCfgSessionStatus.setStatus("current")


class _MefSoamDmCfgHistoryClear_Type(TruthValue):
    """Custom type mefSoamDmCfgHistoryClear based on TruthValue"""
    defaultValue = 2


_MefSoamDmCfgHistoryClear_Type.__name__ = "TruthValue"
_MefSoamDmCfgHistoryClear_Object = MibTableColumn
mefSoamDmCfgHistoryClear = _MefSoamDmCfgHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 33),
    _MefSoamDmCfgHistoryClear_Type()
)
mefSoamDmCfgHistoryClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgHistoryClear.setStatus("current")
_MefSoamDmCfgRowStatus_Type = RowStatus
_MefSoamDmCfgRowStatus_Object = MibTableColumn
mefSoamDmCfgRowStatus = _MefSoamDmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 34),
    _MefSoamDmCfgRowStatus_Type()
)
mefSoamDmCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgRowStatus.setStatus("current")


class _MefSoamDmCfgCosType_Type(Integer32):
    """Custom type mefSoamDmCfgCosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("pcp", 2),
          ("dei", 3))
    )


_MefSoamDmCfgCosType_Type.__name__ = "Integer32"
_MefSoamDmCfgCosType_Object = MibTableColumn
mefSoamDmCfgCosType = _MefSoamDmCfgCosType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 35),
    _MefSoamDmCfgCosType_Type()
)
mefSoamDmCfgCosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgCosType.setStatus("current")
_MefSoamDmCfgTcaNextIndex_Type = Unsigned32
_MefSoamDmCfgTcaNextIndex_Object = MibTableColumn
mefSoamDmCfgTcaNextIndex = _MefSoamDmCfgTcaNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 36),
    _MefSoamDmCfgTcaNextIndex_Type()
)
mefSoamDmCfgTcaNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCfgTcaNextIndex.setStatus("current")


class _MefSoamDmCfgDei_Type(Integer32):
    """Custom type mefSoamDmCfgDei based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noDei", 0),
          ("setDei", 1))
    )


_MefSoamDmCfgDei_Type.__name__ = "Integer32"
_MefSoamDmCfgDei_Object = MibTableColumn
mefSoamDmCfgDei = _MefSoamDmCfgDei_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 1, 1, 37),
    _MefSoamDmCfgDei_Type()
)
mefSoamDmCfgDei.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmCfgDei.setStatus("current")
_MefSoamDmCfgMeasBinTable_Object = MibTable
mefSoamDmCfgMeasBinTable = _MefSoamDmCfgMeasBinTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinTable.setStatus("current")
_MefSoamDmCfgMeasBinEntry_Object = MibTableRow
mefSoamDmCfgMeasBinEntry = _MefSoamDmCfgMeasBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2, 1)
)
mefSoamDmCfgMeasBinEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinType"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinEntry.setStatus("current")
_MefSoamDmCfgMeasBinType_Type = MefSoamTcDelayMeasurementBinType
_MefSoamDmCfgMeasBinType_Object = MibTableColumn
mefSoamDmCfgMeasBinType = _MefSoamDmCfgMeasBinType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2, 1, 1),
    _MefSoamDmCfgMeasBinType_Type()
)
mefSoamDmCfgMeasBinType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinType.setStatus("current")
_MefSoamDmCfgMeasBinNumber_Type = Unsigned32
_MefSoamDmCfgMeasBinNumber_Object = MibTableColumn
mefSoamDmCfgMeasBinNumber = _MefSoamDmCfgMeasBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2, 1, 2),
    _MefSoamDmCfgMeasBinNumber_Type()
)
mefSoamDmCfgMeasBinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinNumber.setStatus("current")
_MefSoamDmCfgMeasBinLowerBound_Type = Unsigned32
_MefSoamDmCfgMeasBinLowerBound_Object = MibTableColumn
mefSoamDmCfgMeasBinLowerBound = _MefSoamDmCfgMeasBinLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 2, 1, 3),
    _MefSoamDmCfgMeasBinLowerBound_Type()
)
mefSoamDmCfgMeasBinLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinLowerBound.setUnits("microseconds (us)")
_MefSoamDmCurrentStatsBinsTable_Object = MibTable
mefSoamDmCurrentStatsBinsTable = _MefSoamDmCurrentStatsBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsBinsTable.setStatus("current")
_MefSoamDmCurrentStatsBinsEntry_Object = MibTableRow
mefSoamDmCurrentStatsBinsEntry = _MefSoamDmCurrentStatsBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 5, 1)
)
mefSoamDmCurrentStatsBinsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinType"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsBinsEntry.setStatus("current")
_MefSoamDmCurrentStatsBinsCounter_Type = Gauge32
_MefSoamDmCurrentStatsBinsCounter_Object = MibTableColumn
mefSoamDmCurrentStatsBinsCounter = _MefSoamDmCurrentStatsBinsCounter_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 5, 1, 1),
    _MefSoamDmCurrentStatsBinsCounter_Type()
)
mefSoamDmCurrentStatsBinsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsBinsCounter.setStatus("current")
_MefSoamDmHistoryStatsBinsTable_Object = MibTable
mefSoamDmHistoryStatsBinsTable = _MefSoamDmHistoryStatsBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 7)
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsBinsTable.setStatus("current")
_MefSoamDmHistoryStatsBinsEntry_Object = MibTableRow
mefSoamDmHistoryStatsBinsEntry = _MefSoamDmHistoryStatsBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 7, 1)
)
mefSoamDmHistoryStatsBinsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinType"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsBinsEntry.setStatus("current")
_MefSoamDmHistoryStatsBinsCounter_Type = Gauge32
_MefSoamDmHistoryStatsBinsCounter_Object = MibTableColumn
mefSoamDmHistoryStatsBinsCounter = _MefSoamDmHistoryStatsBinsCounter_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 7, 1, 1),
    _MefSoamDmHistoryStatsBinsCounter_Type()
)
mefSoamDmHistoryStatsBinsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsBinsCounter.setStatus("current")
_MefSoamDmTcaCfgTable_Object = MibTable
mefSoamDmTcaCfgTable = _MefSoamDmTcaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9)
)
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgTable.setStatus("current")
_MefSoamDmTcaCfgEntry_Object = MibTableRow
mefSoamDmTcaCfgEntry = _MefSoamDmTcaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1)
)
mefSoamDmTcaCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgType"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgEntry.setStatus("current")


class _MefSoamDmTcaCfgIndex_Type(Unsigned32):
    """Custom type mefSoamDmTcaCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamDmTcaCfgIndex_Type.__name__ = "Unsigned32"
_MefSoamDmTcaCfgIndex_Object = MibTableColumn
mefSoamDmTcaCfgIndex = _MefSoamDmTcaCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 1),
    _MefSoamDmTcaCfgIndex_Type()
)
mefSoamDmTcaCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgIndex.setStatus("current")


class _MefSoamDmTcaCfgType_Type(Integer32):
    """Custom type mefSoamDmTcaCfgType based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("fdForwardBin", 1),
          ("fdForwardMax", 2),
          ("fdrForwardBin", 3),
          ("fdrForwardMax", 4),
          ("ifdvForwardBin", 5),
          ("ifdvForwardMax", 6),
          ("fdBackwardBin", 7),
          ("fdBackwardMax", 8),
          ("fdrBackwardBin", 9),
          ("fdrBackwardMax", 10),
          ("ifdvBackwardBin", 11),
          ("ifdvBackwardMax", 12),
          ("fdTwoWayBin", 13),
          ("fdTwoWayMax", 14),
          ("fdrTwoWayBin", 15),
          ("fdrTwoWayMax", 16),
          ("ifdvTwoWayBin", 17),
          ("ifdvTwoWayMax", 18))
    )


_MefSoamDmTcaCfgType_Type.__name__ = "Integer32"
_MefSoamDmTcaCfgType_Object = MibTableColumn
mefSoamDmTcaCfgType = _MefSoamDmTcaCfgType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 2),
    _MefSoamDmTcaCfgType_Type()
)
mefSoamDmTcaCfgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgType.setStatus("current")


class _MefSoamDmTcaCfgEnable_Type(TruthValue):
    """Custom type mefSoamDmTcaCfgEnable based on TruthValue"""
    defaultValue = 1


_MefSoamDmTcaCfgEnable_Type.__name__ = "TruthValue"
_MefSoamDmTcaCfgEnable_Object = MibTableColumn
mefSoamDmTcaCfgEnable = _MefSoamDmTcaCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 3),
    _MefSoamDmTcaCfgEnable_Type()
)
mefSoamDmTcaCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgEnable.setStatus("current")


class _MefSoamDmTcaCfgAlarmType_Type(Integer32):
    """Custom type mefSoamDmTcaCfgAlarmType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateless", 1),
          ("stateful", 2))
    )


_MefSoamDmTcaCfgAlarmType_Type.__name__ = "Integer32"
_MefSoamDmTcaCfgAlarmType_Object = MibTableColumn
mefSoamDmTcaCfgAlarmType = _MefSoamDmTcaCfgAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 4),
    _MefSoamDmTcaCfgAlarmType_Type()
)
mefSoamDmTcaCfgAlarmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgAlarmType.setStatus("current")


class _MefSoamDmTcaCfgBinNumber_Type(Unsigned32):
    """Custom type mefSoamDmTcaCfgBinNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MefSoamDmTcaCfgBinNumber_Type.__name__ = "Unsigned32"
_MefSoamDmTcaCfgBinNumber_Object = MibTableColumn
mefSoamDmTcaCfgBinNumber = _MefSoamDmTcaCfgBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 5),
    _MefSoamDmTcaCfgBinNumber_Type()
)
mefSoamDmTcaCfgBinNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgBinNumber.setStatus("current")


class _MefSoamDmTcaCfgThresholdValue_Type(Integer32):
    """Custom type mefSoamDmTcaCfgThresholdValue based on Integer32"""
    defaultValue = 1


_MefSoamDmTcaCfgThresholdValue_Type.__name__ = "Integer32"
_MefSoamDmTcaCfgThresholdValue_Object = MibTableColumn
mefSoamDmTcaCfgThresholdValue = _MefSoamDmTcaCfgThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 6),
    _MefSoamDmTcaCfgThresholdValue_Type()
)
mefSoamDmTcaCfgThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgThresholdValue.setStatus("current")


class _MefSoamDmTcaCfgClearValue_Type(Integer32):
    """Custom type mefSoamDmTcaCfgClearValue based on Integer32"""
    defaultValue = 1


_MefSoamDmTcaCfgClearValue_Type.__name__ = "Integer32"
_MefSoamDmTcaCfgClearValue_Object = MibTableColumn
mefSoamDmTcaCfgClearValue = _MefSoamDmTcaCfgClearValue_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 7),
    _MefSoamDmTcaCfgClearValue_Type()
)
mefSoamDmTcaCfgClearValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgClearValue.setStatus("current")


class _MefSoamDmTcaCfgAlarmCurrentState_Type(Integer32):
    """Custom type mefSoamDmTcaCfgAlarmCurrentState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_MefSoamDmTcaCfgAlarmCurrentState_Type.__name__ = "Integer32"
_MefSoamDmTcaCfgAlarmCurrentState_Object = MibTableColumn
mefSoamDmTcaCfgAlarmCurrentState = _MefSoamDmTcaCfgAlarmCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 8),
    _MefSoamDmTcaCfgAlarmCurrentState_Type()
)
mefSoamDmTcaCfgAlarmCurrentState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgAlarmCurrentState.setStatus("current")
_MefSoamDmTcaCfgRowStatus_Type = RowStatus
_MefSoamDmTcaCfgRowStatus_Object = MibTableColumn
mefSoamDmTcaCfgRowStatus = _MefSoamDmTcaCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 9, 1, 9),
    _MefSoamDmTcaCfgRowStatus_Type()
)
mefSoamDmTcaCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mefSoamDmTcaCfgRowStatus.setStatus("current")
_MefSoamDmMeasuredStatsXTable_Object = MibTable
mefSoamDmMeasuredStatsXTable = _MefSoamDmMeasuredStatsXTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 10)
)
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXTable.setStatus("current")
_MefSoamDmMeasuredStatsXEntry_Object = MibTableRow
mefSoamDmMeasuredStatsXEntry = _MefSoamDmMeasuredStatsXEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 10, 1)
)
mefSoamDmMeasuredStatsXEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXEntry.setStatus("current")
_MefSoamDmMeasuredStatsXFrameDelayTwoWay_Type = Integer32
_MefSoamDmMeasuredStatsXFrameDelayTwoWay_Object = MibTableColumn
mefSoamDmMeasuredStatsXFrameDelayTwoWay = _MefSoamDmMeasuredStatsXFrameDelayTwoWay_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 10, 1, 1),
    _MefSoamDmMeasuredStatsXFrameDelayTwoWay_Type()
)
mefSoamDmMeasuredStatsXFrameDelayTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXFrameDelayTwoWay.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXFrameDelayTwoWay.setUnits("microseconds")
_MefSoamDmMeasuredStatsXFrameDelayForward_Type = Integer32
_MefSoamDmMeasuredStatsXFrameDelayForward_Object = MibTableColumn
mefSoamDmMeasuredStatsXFrameDelayForward = _MefSoamDmMeasuredStatsXFrameDelayForward_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 10, 1, 2),
    _MefSoamDmMeasuredStatsXFrameDelayForward_Type()
)
mefSoamDmMeasuredStatsXFrameDelayForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXFrameDelayForward.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXFrameDelayForward.setUnits("microseconds")
_MefSoamDmMeasuredStatsXFrameDelayBackward_Type = Integer32
_MefSoamDmMeasuredStatsXFrameDelayBackward_Object = MibTableColumn
mefSoamDmMeasuredStatsXFrameDelayBackward = _MefSoamDmMeasuredStatsXFrameDelayBackward_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 10, 1, 3),
    _MefSoamDmMeasuredStatsXFrameDelayBackward_Type()
)
mefSoamDmMeasuredStatsXFrameDelayBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXFrameDelayBackward.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXFrameDelayBackward.setUnits("microseconds")
_MefSoamDmMeasuredStatsXIfdvTwoWay_Type = Integer32
_MefSoamDmMeasuredStatsXIfdvTwoWay_Object = MibTableColumn
mefSoamDmMeasuredStatsXIfdvTwoWay = _MefSoamDmMeasuredStatsXIfdvTwoWay_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 10, 1, 4),
    _MefSoamDmMeasuredStatsXIfdvTwoWay_Type()
)
mefSoamDmMeasuredStatsXIfdvTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXIfdvTwoWay.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXIfdvTwoWay.setUnits("microseconds")
_MefSoamDmMeasuredStatsXIfdvForward_Type = Integer32
_MefSoamDmMeasuredStatsXIfdvForward_Object = MibTableColumn
mefSoamDmMeasuredStatsXIfdvForward = _MefSoamDmMeasuredStatsXIfdvForward_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 10, 1, 5),
    _MefSoamDmMeasuredStatsXIfdvForward_Type()
)
mefSoamDmMeasuredStatsXIfdvForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXIfdvForward.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXIfdvForward.setUnits("microseconds")
_MefSoamDmMeasuredStatsXIfdvBackward_Type = Integer32
_MefSoamDmMeasuredStatsXIfdvBackward_Object = MibTableColumn
mefSoamDmMeasuredStatsXIfdvBackward = _MefSoamDmMeasuredStatsXIfdvBackward_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 10, 1, 6),
    _MefSoamDmMeasuredStatsXIfdvBackward_Type()
)
mefSoamDmMeasuredStatsXIfdvBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXIfdvBackward.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsXIfdvBackward.setUnits("microseconds")
_MefSoamDmCurrentStatsXTable_Object = MibTable
mefSoamDmCurrentStatsXTable = _MefSoamDmCurrentStatsXTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11)
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXTable.setStatus("current")
_MefSoamDmCurrentStatsXEntry_Object = MibTableRow
mefSoamDmCurrentStatsXEntry = _MefSoamDmCurrentStatsXEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1)
)
mefSoamDmCurrentStatsXEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXEntry.setStatus("current")
_MefSoamDmCurrentStatsXIndex_Type = Unsigned32
_MefSoamDmCurrentStatsXIndex_Object = MibTableColumn
mefSoamDmCurrentStatsXIndex = _MefSoamDmCurrentStatsXIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 1),
    _MefSoamDmCurrentStatsXIndex_Type()
)
mefSoamDmCurrentStatsXIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIndex.setStatus("current")
_MefSoamDmCurrentStatsXStartTime_Type = DateAndTime
_MefSoamDmCurrentStatsXStartTime_Object = MibTableColumn
mefSoamDmCurrentStatsXStartTime = _MefSoamDmCurrentStatsXStartTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 2),
    _MefSoamDmCurrentStatsXStartTime_Type()
)
mefSoamDmCurrentStatsXStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXStartTime.setStatus("current")
_MefSoamDmCurrentStatsXElapsedTime_Type = TimeInterval
_MefSoamDmCurrentStatsXElapsedTime_Object = MibTableColumn
mefSoamDmCurrentStatsXElapsedTime = _MefSoamDmCurrentStatsXElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 3),
    _MefSoamDmCurrentStatsXElapsedTime_Type()
)
mefSoamDmCurrentStatsXElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXElapsedTime.setStatus("current")
_MefSoamDmCurrentStatsXSuspect_Type = TruthValue
_MefSoamDmCurrentStatsXSuspect_Object = MibTableColumn
mefSoamDmCurrentStatsXSuspect = _MefSoamDmCurrentStatsXSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 4),
    _MefSoamDmCurrentStatsXSuspect_Type()
)
mefSoamDmCurrentStatsXSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXSuspect.setStatus("current")
_MefSoamDmCurrentStatsXFrameDelayTwoWayMin_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayTwoWayMin_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayTwoWayMin = _MefSoamDmCurrentStatsXFrameDelayTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 5),
    _MefSoamDmCurrentStatsXFrameDelayTwoWayMin_Type()
)
mefSoamDmCurrentStatsXFrameDelayTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayTwoWayMin.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayTwoWayMax_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayTwoWayMax_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayTwoWayMax = _MefSoamDmCurrentStatsXFrameDelayTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 6),
    _MefSoamDmCurrentStatsXFrameDelayTwoWayMax_Type()
)
mefSoamDmCurrentStatsXFrameDelayTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayTwoWayMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayTwoWayAvg_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayTwoWayAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayTwoWayAvg = _MefSoamDmCurrentStatsXFrameDelayTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 7),
    _MefSoamDmCurrentStatsXFrameDelayTwoWayAvg_Type()
)
mefSoamDmCurrentStatsXFrameDelayTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayTwoWayAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayForwardMin_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayForwardMin_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayForwardMin = _MefSoamDmCurrentStatsXFrameDelayForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 8),
    _MefSoamDmCurrentStatsXFrameDelayForwardMin_Type()
)
mefSoamDmCurrentStatsXFrameDelayForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayForwardMin.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayForwardMax_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayForwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayForwardMax = _MefSoamDmCurrentStatsXFrameDelayForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 9),
    _MefSoamDmCurrentStatsXFrameDelayForwardMax_Type()
)
mefSoamDmCurrentStatsXFrameDelayForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayForwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayForwardAvg_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayForwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayForwardAvg = _MefSoamDmCurrentStatsXFrameDelayForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 10),
    _MefSoamDmCurrentStatsXFrameDelayForwardAvg_Type()
)
mefSoamDmCurrentStatsXFrameDelayForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayForwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayBackwardMin_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayBackwardMin_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayBackwardMin = _MefSoamDmCurrentStatsXFrameDelayBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 11),
    _MefSoamDmCurrentStatsXFrameDelayBackwardMin_Type()
)
mefSoamDmCurrentStatsXFrameDelayBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayBackwardMin.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayBackwardMax_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayBackwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayBackwardMax = _MefSoamDmCurrentStatsXFrameDelayBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 12),
    _MefSoamDmCurrentStatsXFrameDelayBackwardMax_Type()
)
mefSoamDmCurrentStatsXFrameDelayBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayBackwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayBackwardAvg_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayBackwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayBackwardAvg = _MefSoamDmCurrentStatsXFrameDelayBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 13),
    _MefSoamDmCurrentStatsXFrameDelayBackwardAvg_Type()
)
mefSoamDmCurrentStatsXFrameDelayBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayBackwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXIfdvForwardMax_Type = Integer32
_MefSoamDmCurrentStatsXIfdvForwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsXIfdvForwardMax = _MefSoamDmCurrentStatsXIfdvForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 15),
    _MefSoamDmCurrentStatsXIfdvForwardMax_Type()
)
mefSoamDmCurrentStatsXIfdvForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvForwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXIfdvForwardAvg_Type = Integer32
_MefSoamDmCurrentStatsXIfdvForwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXIfdvForwardAvg = _MefSoamDmCurrentStatsXIfdvForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 16),
    _MefSoamDmCurrentStatsXIfdvForwardAvg_Type()
)
mefSoamDmCurrentStatsXIfdvForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvForwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXIfdvBackwardMax_Type = Integer32
_MefSoamDmCurrentStatsXIfdvBackwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsXIfdvBackwardMax = _MefSoamDmCurrentStatsXIfdvBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 18),
    _MefSoamDmCurrentStatsXIfdvBackwardMax_Type()
)
mefSoamDmCurrentStatsXIfdvBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvBackwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXIfdvBackwardAvg_Type = Integer32
_MefSoamDmCurrentStatsXIfdvBackwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXIfdvBackwardAvg = _MefSoamDmCurrentStatsXIfdvBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 19),
    _MefSoamDmCurrentStatsXIfdvBackwardAvg_Type()
)
mefSoamDmCurrentStatsXIfdvBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvBackwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXIfdvTwoWayMax_Type = Integer32
_MefSoamDmCurrentStatsXIfdvTwoWayMax_Object = MibTableColumn
mefSoamDmCurrentStatsXIfdvTwoWayMax = _MefSoamDmCurrentStatsXIfdvTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 21),
    _MefSoamDmCurrentStatsXIfdvTwoWayMax_Type()
)
mefSoamDmCurrentStatsXIfdvTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvTwoWayMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXIfdvTwoWayAvg_Type = Integer32
_MefSoamDmCurrentStatsXIfdvTwoWayAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXIfdvTwoWayAvg = _MefSoamDmCurrentStatsXIfdvTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 22),
    _MefSoamDmCurrentStatsXIfdvTwoWayAvg_Type()
)
mefSoamDmCurrentStatsXIfdvTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXIfdvTwoWayAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayRangeForwardMax_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayRangeForwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayRangeForwardMax = _MefSoamDmCurrentStatsXFrameDelayRangeForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 23),
    _MefSoamDmCurrentStatsXFrameDelayRangeForwardMax_Type()
)
mefSoamDmCurrentStatsXFrameDelayRangeForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeForwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayRangeForwardAvg_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayRangeForwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayRangeForwardAvg = _MefSoamDmCurrentStatsXFrameDelayRangeForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 24),
    _MefSoamDmCurrentStatsXFrameDelayRangeForwardAvg_Type()
)
mefSoamDmCurrentStatsXFrameDelayRangeForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeForwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayRangeBackwardMax_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayRangeBackwardMax_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayRangeBackwardMax = _MefSoamDmCurrentStatsXFrameDelayRangeBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 25),
    _MefSoamDmCurrentStatsXFrameDelayRangeBackwardMax_Type()
)
mefSoamDmCurrentStatsXFrameDelayRangeBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeBackwardMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg = _MefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 26),
    _MefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg_Type()
)
mefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax = _MefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 27),
    _MefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax_Type()
)
mefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax.setUnits("microseconds")
_MefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg_Type = Integer32
_MefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg_Object = MibTableColumn
mefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg = _MefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 28),
    _MefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg_Type()
)
mefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg.setUnits("microseconds")
_MefSoamDmCurrentStatsXSoamPdusSent_Type = Gauge32
_MefSoamDmCurrentStatsXSoamPdusSent_Object = MibTableColumn
mefSoamDmCurrentStatsXSoamPdusSent = _MefSoamDmCurrentStatsXSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 29),
    _MefSoamDmCurrentStatsXSoamPdusSent_Type()
)
mefSoamDmCurrentStatsXSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXSoamPdusSent.setStatus("current")
_MefSoamDmCurrentStatsXSoamPdusReceived_Type = Gauge32
_MefSoamDmCurrentStatsXSoamPdusReceived_Object = MibTableColumn
mefSoamDmCurrentStatsXSoamPdusReceived = _MefSoamDmCurrentStatsXSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 11, 1, 30),
    _MefSoamDmCurrentStatsXSoamPdusReceived_Type()
)
mefSoamDmCurrentStatsXSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsXSoamPdusReceived.setStatus("current")
_MefSoamDmHistoryStatsXTable_Object = MibTable
mefSoamDmHistoryStatsXTable = _MefSoamDmHistoryStatsXTable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13)
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXTable.setStatus("current")
_MefSoamDmHistoryStatsXEntry_Object = MibTableRow
mefSoamDmHistoryStatsXEntry = _MefSoamDmHistoryStatsXEntry_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1)
)
mefSoamDmHistoryStatsXEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmCfgIndex"),
    (0, "MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXIndex"),
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXEntry.setStatus("current")
_MefSoamDmHistoryStatsXIndex_Type = Unsigned32
_MefSoamDmHistoryStatsXIndex_Object = MibTableColumn
mefSoamDmHistoryStatsXIndex = _MefSoamDmHistoryStatsXIndex_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 1),
    _MefSoamDmHistoryStatsXIndex_Type()
)
mefSoamDmHistoryStatsXIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIndex.setStatus("current")
_MefSoamDmHistoryStatsXEndTime_Type = DateAndTime
_MefSoamDmHistoryStatsXEndTime_Object = MibTableColumn
mefSoamDmHistoryStatsXEndTime = _MefSoamDmHistoryStatsXEndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 2),
    _MefSoamDmHistoryStatsXEndTime_Type()
)
mefSoamDmHistoryStatsXEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXEndTime.setStatus("current")
_MefSoamDmHistoryStatsXElapsedTime_Type = TimeInterval
_MefSoamDmHistoryStatsXElapsedTime_Object = MibTableColumn
mefSoamDmHistoryStatsXElapsedTime = _MefSoamDmHistoryStatsXElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 3),
    _MefSoamDmHistoryStatsXElapsedTime_Type()
)
mefSoamDmHistoryStatsXElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXElapsedTime.setStatus("current")
_MefSoamDmHistoryStatsXSuspect_Type = TruthValue
_MefSoamDmHistoryStatsXSuspect_Object = MibTableColumn
mefSoamDmHistoryStatsXSuspect = _MefSoamDmHistoryStatsXSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 4),
    _MefSoamDmHistoryStatsXSuspect_Type()
)
mefSoamDmHistoryStatsXSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXSuspect.setStatus("current")
_MefSoamDmHistoryStatsXFrameDelayTwoWayMin_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayTwoWayMin_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayTwoWayMin = _MefSoamDmHistoryStatsXFrameDelayTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 5),
    _MefSoamDmHistoryStatsXFrameDelayTwoWayMin_Type()
)
mefSoamDmHistoryStatsXFrameDelayTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayTwoWayMin.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayTwoWayMax_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayTwoWayMax_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayTwoWayMax = _MefSoamDmHistoryStatsXFrameDelayTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 6),
    _MefSoamDmHistoryStatsXFrameDelayTwoWayMax_Type()
)
mefSoamDmHistoryStatsXFrameDelayTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayTwoWayMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayTwoWayAvg_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayTwoWayAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayTwoWayAvg = _MefSoamDmHistoryStatsXFrameDelayTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 7),
    _MefSoamDmHistoryStatsXFrameDelayTwoWayAvg_Type()
)
mefSoamDmHistoryStatsXFrameDelayTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayTwoWayAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayForwardMin_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayForwardMin_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayForwardMin = _MefSoamDmHistoryStatsXFrameDelayForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 8),
    _MefSoamDmHistoryStatsXFrameDelayForwardMin_Type()
)
mefSoamDmHistoryStatsXFrameDelayForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayForwardMin.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayForwardMax_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayForwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayForwardMax = _MefSoamDmHistoryStatsXFrameDelayForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 9),
    _MefSoamDmHistoryStatsXFrameDelayForwardMax_Type()
)
mefSoamDmHistoryStatsXFrameDelayForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayForwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayForwardAvg_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayForwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayForwardAvg = _MefSoamDmHistoryStatsXFrameDelayForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 10),
    _MefSoamDmHistoryStatsXFrameDelayForwardAvg_Type()
)
mefSoamDmHistoryStatsXFrameDelayForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayForwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayBackwardMin_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayBackwardMin_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayBackwardMin = _MefSoamDmHistoryStatsXFrameDelayBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 11),
    _MefSoamDmHistoryStatsXFrameDelayBackwardMin_Type()
)
mefSoamDmHistoryStatsXFrameDelayBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayBackwardMin.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayBackwardMax_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayBackwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayBackwardMax = _MefSoamDmHistoryStatsXFrameDelayBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 12),
    _MefSoamDmHistoryStatsXFrameDelayBackwardMax_Type()
)
mefSoamDmHistoryStatsXFrameDelayBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayBackwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayBackwardAvg_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayBackwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayBackwardAvg = _MefSoamDmHistoryStatsXFrameDelayBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 13),
    _MefSoamDmHistoryStatsXFrameDelayBackwardAvg_Type()
)
mefSoamDmHistoryStatsXFrameDelayBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayBackwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXIfdvForwardMax_Type = Integer32
_MefSoamDmHistoryStatsXIfdvForwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsXIfdvForwardMax = _MefSoamDmHistoryStatsXIfdvForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 15),
    _MefSoamDmHistoryStatsXIfdvForwardMax_Type()
)
mefSoamDmHistoryStatsXIfdvForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvForwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXIfdvForwardAvg_Type = Integer32
_MefSoamDmHistoryStatsXIfdvForwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXIfdvForwardAvg = _MefSoamDmHistoryStatsXIfdvForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 16),
    _MefSoamDmHistoryStatsXIfdvForwardAvg_Type()
)
mefSoamDmHistoryStatsXIfdvForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvForwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXIfdvBackwardMax_Type = Integer32
_MefSoamDmHistoryStatsXIfdvBackwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsXIfdvBackwardMax = _MefSoamDmHistoryStatsXIfdvBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 18),
    _MefSoamDmHistoryStatsXIfdvBackwardMax_Type()
)
mefSoamDmHistoryStatsXIfdvBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvBackwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXIfdvBackwardAvg_Type = Integer32
_MefSoamDmHistoryStatsXIfdvBackwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXIfdvBackwardAvg = _MefSoamDmHistoryStatsXIfdvBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 19),
    _MefSoamDmHistoryStatsXIfdvBackwardAvg_Type()
)
mefSoamDmHistoryStatsXIfdvBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvBackwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXIfdvTwoWayMax_Type = Integer32
_MefSoamDmHistoryStatsXIfdvTwoWayMax_Object = MibTableColumn
mefSoamDmHistoryStatsXIfdvTwoWayMax = _MefSoamDmHistoryStatsXIfdvTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 21),
    _MefSoamDmHistoryStatsXIfdvTwoWayMax_Type()
)
mefSoamDmHistoryStatsXIfdvTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvTwoWayMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXIfdvTwoWayAvg_Type = Integer32
_MefSoamDmHistoryStatsXIfdvTwoWayAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXIfdvTwoWayAvg = _MefSoamDmHistoryStatsXIfdvTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 22),
    _MefSoamDmHistoryStatsXIfdvTwoWayAvg_Type()
)
mefSoamDmHistoryStatsXIfdvTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXIfdvTwoWayAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayRangeForwardMax_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayRangeForwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayRangeForwardMax = _MefSoamDmHistoryStatsXFrameDelayRangeForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 23),
    _MefSoamDmHistoryStatsXFrameDelayRangeForwardMax_Type()
)
mefSoamDmHistoryStatsXFrameDelayRangeForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeForwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayRangeForwardAvg_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayRangeForwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayRangeForwardAvg = _MefSoamDmHistoryStatsXFrameDelayRangeForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 24),
    _MefSoamDmHistoryStatsXFrameDelayRangeForwardAvg_Type()
)
mefSoamDmHistoryStatsXFrameDelayRangeForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeForwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayRangeBackwardMax_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayRangeBackwardMax_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayRangeBackwardMax = _MefSoamDmHistoryStatsXFrameDelayRangeBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 25),
    _MefSoamDmHistoryStatsXFrameDelayRangeBackwardMax_Type()
)
mefSoamDmHistoryStatsXFrameDelayRangeBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeBackwardMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg = _MefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 26),
    _MefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg_Type()
)
mefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax = _MefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 27),
    _MefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax_Type()
)
mefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax.setUnits("microseconds")
_MefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg_Type = Integer32
_MefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg_Object = MibTableColumn
mefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg = _MefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 28),
    _MefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg_Type()
)
mefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg.setUnits("microseconds")
_MefSoamDmHistoryStatsXSoamPdusSent_Type = Gauge32
_MefSoamDmHistoryStatsXSoamPdusSent_Object = MibTableColumn
mefSoamDmHistoryStatsXSoamPdusSent = _MefSoamDmHistoryStatsXSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 29),
    _MefSoamDmHistoryStatsXSoamPdusSent_Type()
)
mefSoamDmHistoryStatsXSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXSoamPdusSent.setStatus("current")
_MefSoamDmHistoryStatsXSoamPdusReceived_Type = Gauge32
_MefSoamDmHistoryStatsXSoamPdusReceived_Object = MibTableColumn
mefSoamDmHistoryStatsXSoamPdusReceived = _MefSoamDmHistoryStatsXSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 3, 13, 1, 30),
    _MefSoamDmHistoryStatsXSoamPdusReceived_Type()
)
mefSoamDmHistoryStatsXSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsXSoamPdusReceived.setStatus("current")
_MefSoamPmNotificationCfg_ObjectIdentity = ObjectIdentity
mefSoamPmNotificationCfg = _MefSoamPmNotificationCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 4)
)


class _MefSoamPmNotificationCfgAlarmInterval_Type(Unsigned32):
    """Custom type mefSoamPmNotificationCfgAlarmInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MefSoamPmNotificationCfgAlarmInterval_Type.__name__ = "Unsigned32"
_MefSoamPmNotificationCfgAlarmInterval_Object = MibScalar
mefSoamPmNotificationCfgAlarmInterval = _MefSoamPmNotificationCfgAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 4, 1),
    _MefSoamPmNotificationCfgAlarmInterval_Type()
)
mefSoamPmNotificationCfgAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmNotificationCfgAlarmInterval.setStatus("current")
if mibBuilder.loadTexts:
    mefSoamPmNotificationCfgAlarmInterval.setUnits("Seconds")


class _MefSoamPmNotificationCfgAlarmEnable_Type(Bits):
    """Custom type mefSoamPmNotificationCfgAlarmEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bAvailabilityChangeAlarm", 0),
          ("bLmSessionStartStopAlarm", 1),
          ("bDmSessionStartStopAlarm", 2))
    )

_MefSoamPmNotificationCfgAlarmEnable_Type.__name__ = "Bits"
_MefSoamPmNotificationCfgAlarmEnable_Object = MibScalar
mefSoamPmNotificationCfgAlarmEnable = _MefSoamPmNotificationCfgAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 4, 2),
    _MefSoamPmNotificationCfgAlarmEnable_Type()
)
mefSoamPmNotificationCfgAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mefSoamPmNotificationCfgAlarmEnable.setStatus("current")
_MefSoamPmNotificationObj_ObjectIdentity = ObjectIdentity
mefSoamPmNotificationObj = _MefSoamPmNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5)
)
_MefSoamPmNotificationObjDateAndTime_Type = DateAndTime
_MefSoamPmNotificationObjDateAndTime_Object = MibScalar
mefSoamPmNotificationObjDateAndTime = _MefSoamPmNotificationObjDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 1),
    _MefSoamPmNotificationObjDateAndTime_Type()
)
mefSoamPmNotificationObjDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjDateAndTime.setStatus("current")
_MefSoamPmNotificationObjThresholdId_Type = ObjectIdentifier
_MefSoamPmNotificationObjThresholdId_Object = MibScalar
mefSoamPmNotificationObjThresholdId = _MefSoamPmNotificationObjThresholdId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 2),
    _MefSoamPmNotificationObjThresholdId_Type()
)
mefSoamPmNotificationObjThresholdId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjThresholdId.setStatus("current")
_MefSoamPmNotificationObjThresholdConfig_Type = Unsigned32
_MefSoamPmNotificationObjThresholdConfig_Object = MibScalar
mefSoamPmNotificationObjThresholdConfig = _MefSoamPmNotificationObjThresholdConfig_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 3),
    _MefSoamPmNotificationObjThresholdConfig_Type()
)
mefSoamPmNotificationObjThresholdConfig.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjThresholdConfig.setStatus("current")
_MefSoamPmNotificationObjThresholdValue_Type = Unsigned32
_MefSoamPmNotificationObjThresholdValue_Object = MibScalar
mefSoamPmNotificationObjThresholdValue = _MefSoamPmNotificationObjThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 4),
    _MefSoamPmNotificationObjThresholdValue_Type()
)
mefSoamPmNotificationObjThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjThresholdValue.setStatus("current")
_MefSoamPmNotificationObjSuspect_Type = TruthValue
_MefSoamPmNotificationObjSuspect_Object = MibScalar
mefSoamPmNotificationObjSuspect = _MefSoamPmNotificationObjSuspect_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 5),
    _MefSoamPmNotificationObjSuspect_Type()
)
mefSoamPmNotificationObjSuspect.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjSuspect.setStatus("current")


class _MefSoamPmNotificationObjCrossingType_Type(Integer32):
    """Custom type mefSoamPmNotificationObjCrossingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateless", 1),
          ("statefulSet", 2),
          ("statefulClear", 3))
    )


_MefSoamPmNotificationObjCrossingType_Type.__name__ = "Integer32"
_MefSoamPmNotificationObjCrossingType_Object = MibScalar
mefSoamPmNotificationObjCrossingType = _MefSoamPmNotificationObjCrossingType_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 6),
    _MefSoamPmNotificationObjCrossingType_Type()
)
mefSoamPmNotificationObjCrossingType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjCrossingType.setStatus("current")
_MefSoamPmNotificationObjDestinationMep_Type = MacAddress
_MefSoamPmNotificationObjDestinationMep_Object = MibScalar
mefSoamPmNotificationObjDestinationMep = _MefSoamPmNotificationObjDestinationMep_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 7),
    _MefSoamPmNotificationObjDestinationMep_Type()
)
mefSoamPmNotificationObjDestinationMep.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjDestinationMep.setStatus("current")
_MefSoamPmNotificationObjPriority_Type = IEEE8021PriorityValue
_MefSoamPmNotificationObjPriority_Object = MibScalar
mefSoamPmNotificationObjPriority = _MefSoamPmNotificationObjPriority_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 8),
    _MefSoamPmNotificationObjPriority_Type()
)
mefSoamPmNotificationObjPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjPriority.setStatus("current")
_MefSoamPmNotificationObjDestinationMepId_Type = Dot1agCfmMepId
_MefSoamPmNotificationObjDestinationMepId_Object = MibScalar
mefSoamPmNotificationObjDestinationMepId = _MefSoamPmNotificationObjDestinationMepId_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 9),
    _MefSoamPmNotificationObjDestinationMepId_Type()
)
mefSoamPmNotificationObjDestinationMepId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjDestinationMepId.setStatus("current")
_MefSoamPmNotificationObjMeasurementInterval_Type = DateAndTime
_MefSoamPmNotificationObjMeasurementInterval_Object = MibScalar
mefSoamPmNotificationObjMeasurementInterval = _MefSoamPmNotificationObjMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 10),
    _MefSoamPmNotificationObjMeasurementInterval_Type()
)
mefSoamPmNotificationObjMeasurementInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjMeasurementInterval.setStatus("current")


class _MefSoamPmNotificationObjSeverity_Type(Integer32):
    """Custom type mefSoamPmNotificationObjSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("info", 2))
    )


_MefSoamPmNotificationObjSeverity_Type.__name__ = "Integer32"
_MefSoamPmNotificationObjSeverity_Object = MibScalar
mefSoamPmNotificationObjSeverity = _MefSoamPmNotificationObjSeverity_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 11),
    _MefSoamPmNotificationObjSeverity_Type()
)
mefSoamPmNotificationObjSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjSeverity.setStatus("current")
_MefSoamPmNotificationObjAvailabilityStatus_Type = Unsigned32
_MefSoamPmNotificationObjAvailabilityStatus_Object = MibScalar
mefSoamPmNotificationObjAvailabilityStatus = _MefSoamPmNotificationObjAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 1, 5, 12),
    _MefSoamPmNotificationObjAvailabilityStatus_Type()
)
mefSoamPmNotificationObjAvailabilityStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjAvailabilityStatus.setStatus("current")
_MefSoamPmMibConformance_ObjectIdentity = ObjectIdentity
mefSoamPmMibConformance = _MefSoamPmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2)
)
_MefSoamPmMibCompliances_ObjectIdentity = ObjectIdentity
mefSoamPmMibCompliances = _MefSoamPmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 1)
)
_MefSoamPmMibGroups_ObjectIdentity = ObjectIdentity
mefSoamPmMibGroups = _MefSoamPmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("MEF-SOAM-PM-MIB",
     "mefSoamPmMepEntry")
)
mefSoamPmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

mefSoamPmMepMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 1)
)
mefSoamPmMepMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmMepOperNextIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmMepSlmSingleEndedResponder"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmMepDmSingleEndedResponder"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmMepLmSingleEndedResponder"))
)
if mibBuilder.loadTexts:
    mefSoamPmMepMandatoryGroup.setStatus("current")

mefSoamLmCfgMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 3)
)
mefSoamLmCfgMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCfgType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgEnabled"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgMeasurementEnable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgMessagePeriod"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgPriority"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgFrameSize"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgMeasurementInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgNumIntervalsStored"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDestMacAddress"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDestMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDestIsMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgStartTimeType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgFixedStartDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgRelativeStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgStopTimeType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgFixedStopDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgRelativeStopTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgRepetitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityMeasurementInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityNumConsecutiveHighFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityFlrThreshold"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAvailabilityNumConsecutiveIntervals"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgSessionType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgRowStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgCosType"))
)
if mibBuilder.loadTexts:
    mefSoamLmCfgMandatoryGroup.setStatus("current")

mefSoamLmCfgOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 4)
)
mefSoamLmCfgOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCfgVersion"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDataPattern"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgTestTlvIncluded"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgTestTlvPattern"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAlignMeasurementIntervals"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgAlignMeasurementOffset"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgSourceMacAddress"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgSessionStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgHistoryClear"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgTcaNextIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgDei"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmTestId"))
)
if mibBuilder.loadTexts:
    mefSoamLmCfgOptionalGroup.setStatus("current")

mefSoamLmMeasuredStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 5)
)
mefSoamLmMeasuredStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailForwardLastTransitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailForwardStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailBackwardStatus"))
)
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsMandatoryGroup.setStatus("current")

mefSoamLmMeasuredStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 6)
)
mefSoamLmMeasuredStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsForwardFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsBackwardFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmMeasuredStatsOptionalGroup.setStatus("current")

mefSoamLmCurrentAvailStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 7)
)
mefSoamLmCurrentAvailStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardUnavailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardUnavailable"))
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsMandatoryGroup.setStatus("current")

mefSoamLmCurrentAvailStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 8)
)
mefSoamLmCurrentAvailStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardAvgFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardAvgFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentAvailStatsOptionalGroup.setStatus("current")

mefSoamLmCurrentStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 9)
)
mefSoamLmCurrentStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardTransmittedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardReceivedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardTransmittedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardReceivedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsSoamPdusSent"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsSoamPdusReceived"))
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsMandatoryGroup.setStatus("current")

mefSoamLmCurrentStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 10)
)
mefSoamLmCurrentStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsForwardAvgFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsBackwardAvgFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmCurrentStatsOptionalGroup.setStatus("current")

mefSoamLmHistoryAvailStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 11)
)
mefSoamLmHistoryAvailStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsEndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardUnavailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardUnavailable"))
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsMandatoryGroup.setStatus("current")

mefSoamLmHistoryAvailStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 12)
)
mefSoamLmHistoryAvailStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsForwardAvgFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsBackwardAvgFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryAvailStatsOptionalGroup.setStatus("current")

mefSoamLmHistoryStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 13)
)
mefSoamLmHistoryStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsEndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardTransmittedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardReceivedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardTransmittedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardReceivedFrames"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsSoamPdusSent"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsSoamPdusReceived"))
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsMandatoryGroup.setStatus("current")

mefSoamLmHistoryStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 14)
)
mefSoamLmHistoryStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsForwardAvgFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardMinFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardMaxFlr"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsBackwardAvgFlr"))
)
if mibBuilder.loadTexts:
    mefSoamLmHistoryStatsOptionalGroup.setStatus("current")

mefSoamDmCfgMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 15)
)
mefSoamDmCfgMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCfgType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgEnabled"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasurementEnable"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMessagePeriod"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgPriority"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgFrameSize"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasurementInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgNumIntervalsStored"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDestMacAddress"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDestMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDestIsMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgStartTimeType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgFixedStartDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgRelativeStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgStopTimeType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgFixedStopDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgRelativeStopTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgRepetitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgAlignMeasurementIntervals"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgNumMeasBinsPerFrameDelayInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgSessionType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgRowStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgCosType"))
)
if mibBuilder.loadTexts:
    mefSoamDmCfgMandatoryGroup.setStatus("current")

mefSoamDmCfgOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 16)
)
mefSoamDmCfgOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCfgVersion"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDataPattern"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgTestTlvIncluded"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgTestTlvPattern"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgSourceMacAddress"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgAlignMeasurementOffset"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgInterFrameDelayVariationSelectionOffset"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgSessionStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgHistoryClear"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgTcaNextIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgDei"))
)
if mibBuilder.loadTexts:
    mefSoamDmCfgOptionalGroup.setStatus("current")

mefSoamDmCfgMeasBinMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 17)
)
mefSoamDmCfgMeasBinMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinLowerBound"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsXFrameDelayForward"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsXFrameDelayBackward"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsXIfdvTwoWay"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsXIfdvForward"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsXIfdvBackward"))
)
if mibBuilder.loadTexts:
    mefSoamDmCfgMeasBinMandatoryGroup.setStatus("current")

mefSoamDmMeasuredStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 18)
)
mefSoamDmMeasuredStatsOptionalGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsXFrameDelayTwoWay")
)
if mibBuilder.loadTexts:
    mefSoamDmMeasuredStatsOptionalGroup.setStatus("current")

mefSoamDmCurrentStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 19)
)
mefSoamDmCurrentStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXIndex"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXStartTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayTwoWayMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayTwoWayAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayForwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayBackwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXIfdvForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXIfdvForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXIfdvBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXIfdvBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayRangeForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayRangeForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayRangeBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXSoamPdusSent"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXSoamPdusReceived"))
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsMandatoryGroup.setStatus("current")

mefSoamDmCurrentStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 20)
)
mefSoamDmCurrentStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXIfdvTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXIfdvTwoWayAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg"))
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsOptionalGroup.setStatus("current")

mefSoamDmCurrentStatsBinsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 21)
)
mefSoamDmCurrentStatsBinsMandatoryGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsBinsCounter")
)
if mibBuilder.loadTexts:
    mefSoamDmCurrentStatsBinsMandatoryGroup.setStatus("current")

mefSoamDmHistoryStatsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 22)
)
mefSoamDmHistoryStatsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXEndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXElapsedTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayTwoWayMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayTwoWayAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayForwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayBackwardMin"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXIfdvForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXIfdvForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXIfdvBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXIfdvBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayRangeForwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayRangeForwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayRangeBackwardMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXSoamPdusSent"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXSoamPdusReceived"))
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsMandatoryGroup.setStatus("current")

mefSoamDmHistoryStatsOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 23)
)
mefSoamDmHistoryStatsOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXIfdvTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXIfdvTwoWayAvg"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg"))
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsOptionalGroup.setStatus("current")

mefSoamDmHistoryStatsBinsMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 24)
)
mefSoamDmHistoryStatsBinsMandatoryGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsBinsCounter")
)
if mibBuilder.loadTexts:
    mefSoamDmHistoryStatsBinsMandatoryGroup.setStatus("current")

mefSoamPmNotificationCfgMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 31)
)
mefSoamPmNotificationCfgMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationCfgAlarmInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationCfgAlarmEnable"))
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationCfgMandatoryGroup.setStatus("current")

mefSoamPmNotificationObjMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 32)
)
mefSoamPmNotificationObjMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjPriority"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjMeasurementInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjAvailabilityStatus"))
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjMandatoryGroup.setStatus("current")

mefSoamPmNotificationObjOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 33)
)
mefSoamPmNotificationObjOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdConfig"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdId"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdValue"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjCrossingType"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjSeverity"))
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationObjOptionalGroup.setStatus("current")

mefSoamLmTcaOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 34)
)
mefSoamLmTcaOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmTcaCfgEnable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmTcaCfgAlarmType"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmTcaCfgThresholdValue"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmTcaCfgClearValue"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmTcaCfgAlarmCurrentState"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmTcaCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefSoamLmTcaOptionalGroup.setStatus("current")

mefSoamDmTcaOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 35)
)
mefSoamDmTcaOptionalGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgEnable"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgAlarmType"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgBinNumber"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgThresholdValue"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgClearValue"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgAlarmCurrentState"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmTcaCfgRowStatus"))
)
if mibBuilder.loadTexts:
    mefSoamDmTcaOptionalGroup.setStatus("current")


# Notification objects

mefSoamAvailabilityChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0, 1)
)
mefSoamAvailabilityChangeAlarm.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailForwardStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailBackwardStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailForwardLastTransitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsForwardUnavailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardAvailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsBackwardUnavailable"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjPriority"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMepId"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjAvailabilityStatus"))
)
if mibBuilder.loadTexts:
    mefSoamAvailabilityChangeAlarm.setStatus(
        "current"
    )

mefSoamLmSessionStartStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0, 2)
)
mefSoamLmSessionStartStopAlarm.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamLmCfgSessionStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    mefSoamLmSessionStartStopAlarm.setStatus(
        "current"
    )

mefSoamDmSessionStartStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0, 3)
)
mefSoamDmSessionStartStopAlarm.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamDmCfgSessionStatus"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    mefSoamDmSessionStartStopAlarm.setStatus(
        "current"
    )

mefSoamPmThresholdCrossingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 0, 4)
)
mefSoamPmThresholdCrossingAlarm.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjCrossingType"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdId"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdConfig"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjThresholdValue"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjSuspect"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDateAndTime"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjDestinationMep"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjMeasurementInterval"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjSeverity"))
)
if mibBuilder.loadTexts:
    mefSoamPmThresholdCrossingAlarm.setStatus(
        "current"
    )


# Notifications groups

mefSoamPmNotificationsMandatoryGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 29)
)
mefSoamPmNotificationsMandatoryGroup.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamAvailabilityChangeAlarm"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmSessionStartStopAlarm"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmSessionStartStopAlarm"))
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationsMandatoryGroup.setStatus(
        "current"
    )

mefSoamPmNotificationsOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 2, 30)
)
mefSoamPmNotificationsOptionalGroup.setObjects(
    ("MEF-SOAM-PM-MIB", "mefSoamPmThresholdCrossingAlarm")
)
if mibBuilder.loadTexts:
    mefSoamPmNotificationsOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mefSoamPmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 15007, 1, 3, 2, 1, 1)
)
mefSoamPmMibCompliance.setObjects(
      *(("MEF-SOAM-PM-MIB", "mefSoamPmMepMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgMeasBinMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsBinsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsBinsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationsMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationCfgMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjMandatoryGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCfgOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmMeasuredStatsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentAvailStatsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmCurrentStatsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryAvailStatsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmHistoryStatsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCfgOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmMeasuredStatsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmCurrentStatsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmHistoryStatsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationsOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamPmNotificationObjOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamLmTcaOptionalGroup"),
        ("MEF-SOAM-PM-MIB", "mefSoamDmTcaOptionalGroup"))
)
if mibBuilder.loadTexts:
    mefSoamPmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEF-SOAM-PM-MIB",
    **{"mefSoamPmMib": mefSoamPmMib,
       "mefSoamPmNotifications": mefSoamPmNotifications,
       "mefSoamAvailabilityChangeAlarm": mefSoamAvailabilityChangeAlarm,
       "mefSoamLmSessionStartStopAlarm": mefSoamLmSessionStartStopAlarm,
       "mefSoamDmSessionStartStopAlarm": mefSoamDmSessionStartStopAlarm,
       "mefSoamPmThresholdCrossingAlarm": mefSoamPmThresholdCrossingAlarm,
       "mefSoamPmMibObjects": mefSoamPmMibObjects,
       "mefSoamPmMep": mefSoamPmMep,
       "mefSoamPmMepTable": mefSoamPmMepTable,
       "mefSoamPmMepEntry": mefSoamPmMepEntry,
       "mefSoamPmMepOperNextIndex": mefSoamPmMepOperNextIndex,
       "mefSoamPmMepLmSingleEndedResponder": mefSoamPmMepLmSingleEndedResponder,
       "mefSoamPmMepSlmSingleEndedResponder": mefSoamPmMepSlmSingleEndedResponder,
       "mefSoamPmMepDmSingleEndedResponder": mefSoamPmMepDmSingleEndedResponder,
       "mefSoamPmLmObjects": mefSoamPmLmObjects,
       "mefSoamLmCfgTable": mefSoamLmCfgTable,
       "mefSoamLmCfgEntry": mefSoamLmCfgEntry,
       "mefSoamLmCfgIndex": mefSoamLmCfgIndex,
       "mefSoamLmCfgType": mefSoamLmCfgType,
       "mefSoamLmCfgVersion": mefSoamLmCfgVersion,
       "mefSoamLmCfgEnabled": mefSoamLmCfgEnabled,
       "mefSoamLmCfgMeasurementEnable": mefSoamLmCfgMeasurementEnable,
       "mefSoamLmCfgMessagePeriod": mefSoamLmCfgMessagePeriod,
       "mefSoamLmCfgPriority": mefSoamLmCfgPriority,
       "mefSoamLmCfgFrameSize": mefSoamLmCfgFrameSize,
       "mefSoamLmCfgDataPattern": mefSoamLmCfgDataPattern,
       "mefSoamLmCfgTestTlvIncluded": mefSoamLmCfgTestTlvIncluded,
       "mefSoamLmCfgTestTlvPattern": mefSoamLmCfgTestTlvPattern,
       "mefSoamLmCfgMeasurementInterval": mefSoamLmCfgMeasurementInterval,
       "mefSoamLmCfgNumIntervalsStored": mefSoamLmCfgNumIntervalsStored,
       "mefSoamLmCfgDestMacAddress": mefSoamLmCfgDestMacAddress,
       "mefSoamLmCfgDestMepId": mefSoamLmCfgDestMepId,
       "mefSoamLmCfgDestIsMepId": mefSoamLmCfgDestIsMepId,
       "mefSoamLmCfgStartTimeType": mefSoamLmCfgStartTimeType,
       "mefSoamLmCfgFixedStartDateAndTime": mefSoamLmCfgFixedStartDateAndTime,
       "mefSoamLmCfgRelativeStartTime": mefSoamLmCfgRelativeStartTime,
       "mefSoamLmCfgStopTimeType": mefSoamLmCfgStopTimeType,
       "mefSoamLmCfgFixedStopDateAndTime": mefSoamLmCfgFixedStopDateAndTime,
       "mefSoamLmCfgRelativeStopTime": mefSoamLmCfgRelativeStopTime,
       "mefSoamLmCfgRepetitionTime": mefSoamLmCfgRepetitionTime,
       "mefSoamLmCfgAlignMeasurementIntervals": mefSoamLmCfgAlignMeasurementIntervals,
       "mefSoamLmCfgAlignMeasurementOffset": mefSoamLmCfgAlignMeasurementOffset,
       "mefSoamLmCfgAvailabilityMeasurementInterval": mefSoamLmCfgAvailabilityMeasurementInterval,
       "mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus": mefSoamLmCfgAvailabilityNumConsecutiveMeasPdus,
       "mefSoamLmCfgAvailabilityFlrThreshold": mefSoamLmCfgAvailabilityFlrThreshold,
       "mefSoamLmCfgAvailabilityNumConsecutiveIntervals": mefSoamLmCfgAvailabilityNumConsecutiveIntervals,
       "mefSoamLmCfgAvailabilityNumConsecutiveHighFlr": mefSoamLmCfgAvailabilityNumConsecutiveHighFlr,
       "mefSoamLmCfgSessionType": mefSoamLmCfgSessionType,
       "mefSoamLmCfgSessionStatus": mefSoamLmCfgSessionStatus,
       "mefSoamLmCfgHistoryClear": mefSoamLmCfgHistoryClear,
       "mefSoamLmCfgRowStatus": mefSoamLmCfgRowStatus,
       "mefSoamLmCfgCosType": mefSoamLmCfgCosType,
       "mefSoamLmCfgSourceMacAddress": mefSoamLmCfgSourceMacAddress,
       "mefSoamLmCfgTcaNextIndex": mefSoamLmCfgTcaNextIndex,
       "mefSoamLmCfgDei": mefSoamLmCfgDei,
       "mefSoamLmTestId": mefSoamLmTestId,
       "mefSoamLmMeasuredStatsTable": mefSoamLmMeasuredStatsTable,
       "mefSoamLmMeasuredStatsEntry": mefSoamLmMeasuredStatsEntry,
       "mefSoamLmMeasuredStatsForwardFlr": mefSoamLmMeasuredStatsForwardFlr,
       "mefSoamLmMeasuredStatsBackwardFlr": mefSoamLmMeasuredStatsBackwardFlr,
       "mefSoamLmMeasuredStatsAvailForwardStatus": mefSoamLmMeasuredStatsAvailForwardStatus,
       "mefSoamLmMeasuredStatsAvailBackwardStatus": mefSoamLmMeasuredStatsAvailBackwardStatus,
       "mefSoamLmMeasuredStatsAvailForwardLastTransitionTime": mefSoamLmMeasuredStatsAvailForwardLastTransitionTime,
       "mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime": mefSoamLmMeasuredStatsAvailBackwardLastTransitionTime,
       "mefSoamLmCurrentAvailStatsTable": mefSoamLmCurrentAvailStatsTable,
       "mefSoamLmCurrentAvailStatsEntry": mefSoamLmCurrentAvailStatsEntry,
       "mefSoamLmCurrentAvailStatsIndex": mefSoamLmCurrentAvailStatsIndex,
       "mefSoamLmCurrentAvailStatsStartTime": mefSoamLmCurrentAvailStatsStartTime,
       "mefSoamLmCurrentAvailStatsElapsedTime": mefSoamLmCurrentAvailStatsElapsedTime,
       "mefSoamLmCurrentAvailStatsSuspect": mefSoamLmCurrentAvailStatsSuspect,
       "mefSoamLmCurrentAvailStatsForwardHighLoss": mefSoamLmCurrentAvailStatsForwardHighLoss,
       "mefSoamLmCurrentAvailStatsBackwardHighLoss": mefSoamLmCurrentAvailStatsBackwardHighLoss,
       "mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss": mefSoamLmCurrentAvailStatsForwardConsecutiveHighLoss,
       "mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss": mefSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss,
       "mefSoamLmCurrentAvailStatsForwardAvailable": mefSoamLmCurrentAvailStatsForwardAvailable,
       "mefSoamLmCurrentAvailStatsBackwardAvailable": mefSoamLmCurrentAvailStatsBackwardAvailable,
       "mefSoamLmCurrentAvailStatsForwardUnavailable": mefSoamLmCurrentAvailStatsForwardUnavailable,
       "mefSoamLmCurrentAvailStatsBackwardUnavailable": mefSoamLmCurrentAvailStatsBackwardUnavailable,
       "mefSoamLmCurrentAvailStatsForwardMinFlr": mefSoamLmCurrentAvailStatsForwardMinFlr,
       "mefSoamLmCurrentAvailStatsForwardMaxFlr": mefSoamLmCurrentAvailStatsForwardMaxFlr,
       "mefSoamLmCurrentAvailStatsForwardAvgFlr": mefSoamLmCurrentAvailStatsForwardAvgFlr,
       "mefSoamLmCurrentAvailStatsBackwardMinFlr": mefSoamLmCurrentAvailStatsBackwardMinFlr,
       "mefSoamLmCurrentAvailStatsBackwardMaxFlr": mefSoamLmCurrentAvailStatsBackwardMaxFlr,
       "mefSoamLmCurrentAvailStatsBackwardAvgFlr": mefSoamLmCurrentAvailStatsBackwardAvgFlr,
       "mefSoamLmCurrentStatsTable": mefSoamLmCurrentStatsTable,
       "mefSoamLmCurrentStatsEntry": mefSoamLmCurrentStatsEntry,
       "mefSoamLmCurrentStatsIndex": mefSoamLmCurrentStatsIndex,
       "mefSoamLmCurrentStatsStartTime": mefSoamLmCurrentStatsStartTime,
       "mefSoamLmCurrentStatsElapsedTime": mefSoamLmCurrentStatsElapsedTime,
       "mefSoamLmCurrentStatsSuspect": mefSoamLmCurrentStatsSuspect,
       "mefSoamLmCurrentStatsForwardTransmittedFrames": mefSoamLmCurrentStatsForwardTransmittedFrames,
       "mefSoamLmCurrentStatsForwardReceivedFrames": mefSoamLmCurrentStatsForwardReceivedFrames,
       "mefSoamLmCurrentStatsForwardMinFlr": mefSoamLmCurrentStatsForwardMinFlr,
       "mefSoamLmCurrentStatsForwardMaxFlr": mefSoamLmCurrentStatsForwardMaxFlr,
       "mefSoamLmCurrentStatsForwardAvgFlr": mefSoamLmCurrentStatsForwardAvgFlr,
       "mefSoamLmCurrentStatsBackwardTransmittedFrames": mefSoamLmCurrentStatsBackwardTransmittedFrames,
       "mefSoamLmCurrentStatsBackwardReceivedFrames": mefSoamLmCurrentStatsBackwardReceivedFrames,
       "mefSoamLmCurrentStatsBackwardMinFlr": mefSoamLmCurrentStatsBackwardMinFlr,
       "mefSoamLmCurrentStatsBackwardMaxFlr": mefSoamLmCurrentStatsBackwardMaxFlr,
       "mefSoamLmCurrentStatsBackwardAvgFlr": mefSoamLmCurrentStatsBackwardAvgFlr,
       "mefSoamLmCurrentStatsSoamPdusSent": mefSoamLmCurrentStatsSoamPdusSent,
       "mefSoamLmCurrentStatsSoamPdusReceived": mefSoamLmCurrentStatsSoamPdusReceived,
       "mefSoamLmHistoryAvailStatsTable": mefSoamLmHistoryAvailStatsTable,
       "mefSoamLmHistoryAvailStatsEntry": mefSoamLmHistoryAvailStatsEntry,
       "mefSoamLmHistoryAvailStatsIndex": mefSoamLmHistoryAvailStatsIndex,
       "mefSoamLmHistoryAvailStatsEndTime": mefSoamLmHistoryAvailStatsEndTime,
       "mefSoamLmHistoryAvailStatsElapsedTime": mefSoamLmHistoryAvailStatsElapsedTime,
       "mefSoamLmHistoryAvailStatsSuspect": mefSoamLmHistoryAvailStatsSuspect,
       "mefSoamLmHistoryAvailStatsForwardHighLoss": mefSoamLmHistoryAvailStatsForwardHighLoss,
       "mefSoamLmHistoryAvailStatsBackwardHighLoss": mefSoamLmHistoryAvailStatsBackwardHighLoss,
       "mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss": mefSoamLmHistoryAvailStatsForwardConsecutiveHighLoss,
       "mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss": mefSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss,
       "mefSoamLmHistoryAvailStatsForwardAvailable": mefSoamLmHistoryAvailStatsForwardAvailable,
       "mefSoamLmHistoryAvailStatsBackwardAvailable": mefSoamLmHistoryAvailStatsBackwardAvailable,
       "mefSoamLmHistoryAvailStatsForwardUnavailable": mefSoamLmHistoryAvailStatsForwardUnavailable,
       "mefSoamLmHistoryAvailStatsBackwardUnavailable": mefSoamLmHistoryAvailStatsBackwardUnavailable,
       "mefSoamLmHistoryAvailStatsForwardMinFlr": mefSoamLmHistoryAvailStatsForwardMinFlr,
       "mefSoamLmHistoryAvailStatsForwardMaxFlr": mefSoamLmHistoryAvailStatsForwardMaxFlr,
       "mefSoamLmHistoryAvailStatsForwardAvgFlr": mefSoamLmHistoryAvailStatsForwardAvgFlr,
       "mefSoamLmHistoryAvailStatsBackwardMinFlr": mefSoamLmHistoryAvailStatsBackwardMinFlr,
       "mefSoamLmHistoryAvailStatsBackwardMaxFlr": mefSoamLmHistoryAvailStatsBackwardMaxFlr,
       "mefSoamLmHistoryAvailStatsBackwardAvgFlr": mefSoamLmHistoryAvailStatsBackwardAvgFlr,
       "mefSoamLmHistoryStatsTable": mefSoamLmHistoryStatsTable,
       "mefSoamLmHistoryStatsEntry": mefSoamLmHistoryStatsEntry,
       "mefSoamLmHistoryStatsIndex": mefSoamLmHistoryStatsIndex,
       "mefSoamLmHistoryStatsEndTime": mefSoamLmHistoryStatsEndTime,
       "mefSoamLmHistoryStatsElapsedTime": mefSoamLmHistoryStatsElapsedTime,
       "mefSoamLmHistoryStatsSuspect": mefSoamLmHistoryStatsSuspect,
       "mefSoamLmHistoryStatsForwardTransmittedFrames": mefSoamLmHistoryStatsForwardTransmittedFrames,
       "mefSoamLmHistoryStatsForwardReceivedFrames": mefSoamLmHistoryStatsForwardReceivedFrames,
       "mefSoamLmHistoryStatsForwardMinFlr": mefSoamLmHistoryStatsForwardMinFlr,
       "mefSoamLmHistoryStatsForwardMaxFlr": mefSoamLmHistoryStatsForwardMaxFlr,
       "mefSoamLmHistoryStatsForwardAvgFlr": mefSoamLmHistoryStatsForwardAvgFlr,
       "mefSoamLmHistoryStatsBackwardTransmittedFrames": mefSoamLmHistoryStatsBackwardTransmittedFrames,
       "mefSoamLmHistoryStatsBackwardReceivedFrames": mefSoamLmHistoryStatsBackwardReceivedFrames,
       "mefSoamLmHistoryStatsBackwardMinFlr": mefSoamLmHistoryStatsBackwardMinFlr,
       "mefSoamLmHistoryStatsBackwardMaxFlr": mefSoamLmHistoryStatsBackwardMaxFlr,
       "mefSoamLmHistoryStatsBackwardAvgFlr": mefSoamLmHistoryStatsBackwardAvgFlr,
       "mefSoamLmHistoryStatsSoamPdusSent": mefSoamLmHistoryStatsSoamPdusSent,
       "mefSoamLmHistoryStatsSoamPdusReceived": mefSoamLmHistoryStatsSoamPdusReceived,
       "mefSoamLmTcaCfgTable": mefSoamLmTcaCfgTable,
       "mefSoamLmTcaCfgEntry": mefSoamLmTcaCfgEntry,
       "mefSoamLmTcaCfgIndex": mefSoamLmTcaCfgIndex,
       "mefSoamLmTcaCfgType": mefSoamLmTcaCfgType,
       "mefSoamLmTcaCfgEnable": mefSoamLmTcaCfgEnable,
       "mefSoamLmTcaCfgAlarmType": mefSoamLmTcaCfgAlarmType,
       "mefSoamLmTcaCfgThresholdValue": mefSoamLmTcaCfgThresholdValue,
       "mefSoamLmTcaCfgClearValue": mefSoamLmTcaCfgClearValue,
       "mefSoamLmTcaCfgAlarmCurrentState": mefSoamLmTcaCfgAlarmCurrentState,
       "mefSoamLmTcaCfgRowStatus": mefSoamLmTcaCfgRowStatus,
       "mefSoamPmDmObjects": mefSoamPmDmObjects,
       "mefSoamDmCfgTable": mefSoamDmCfgTable,
       "mefSoamDmCfgEntry": mefSoamDmCfgEntry,
       "mefSoamDmCfgIndex": mefSoamDmCfgIndex,
       "mefSoamDmCfgType": mefSoamDmCfgType,
       "mefSoamDmCfgVersion": mefSoamDmCfgVersion,
       "mefSoamDmCfgEnabled": mefSoamDmCfgEnabled,
       "mefSoamDmCfgMeasurementEnable": mefSoamDmCfgMeasurementEnable,
       "mefSoamDmCfgMessagePeriod": mefSoamDmCfgMessagePeriod,
       "mefSoamDmCfgPriority": mefSoamDmCfgPriority,
       "mefSoamDmCfgFrameSize": mefSoamDmCfgFrameSize,
       "mefSoamDmCfgDataPattern": mefSoamDmCfgDataPattern,
       "mefSoamDmCfgTestTlvIncluded": mefSoamDmCfgTestTlvIncluded,
       "mefSoamDmCfgTestTlvPattern": mefSoamDmCfgTestTlvPattern,
       "mefSoamDmCfgMeasurementInterval": mefSoamDmCfgMeasurementInterval,
       "mefSoamDmCfgNumIntervalsStored": mefSoamDmCfgNumIntervalsStored,
       "mefSoamDmCfgDestMacAddress": mefSoamDmCfgDestMacAddress,
       "mefSoamDmCfgDestMepId": mefSoamDmCfgDestMepId,
       "mefSoamDmCfgDestIsMepId": mefSoamDmCfgDestIsMepId,
       "mefSoamDmCfgSourceMacAddress": mefSoamDmCfgSourceMacAddress,
       "mefSoamDmCfgStartTimeType": mefSoamDmCfgStartTimeType,
       "mefSoamDmCfgFixedStartDateAndTime": mefSoamDmCfgFixedStartDateAndTime,
       "mefSoamDmCfgRelativeStartTime": mefSoamDmCfgRelativeStartTime,
       "mefSoamDmCfgStopTimeType": mefSoamDmCfgStopTimeType,
       "mefSoamDmCfgFixedStopDateAndTime": mefSoamDmCfgFixedStopDateAndTime,
       "mefSoamDmCfgRelativeStopTime": mefSoamDmCfgRelativeStopTime,
       "mefSoamDmCfgRepetitionTime": mefSoamDmCfgRepetitionTime,
       "mefSoamDmCfgAlignMeasurementIntervals": mefSoamDmCfgAlignMeasurementIntervals,
       "mefSoamDmCfgAlignMeasurementOffset": mefSoamDmCfgAlignMeasurementOffset,
       "mefSoamDmCfgNumMeasBinsPerFrameDelayInterval": mefSoamDmCfgNumMeasBinsPerFrameDelayInterval,
       "mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval": mefSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval,
       "mefSoamDmCfgInterFrameDelayVariationSelectionOffset": mefSoamDmCfgInterFrameDelayVariationSelectionOffset,
       "mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval": mefSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval,
       "mefSoamDmCfgSessionType": mefSoamDmCfgSessionType,
       "mefSoamDmCfgSessionStatus": mefSoamDmCfgSessionStatus,
       "mefSoamDmCfgHistoryClear": mefSoamDmCfgHistoryClear,
       "mefSoamDmCfgRowStatus": mefSoamDmCfgRowStatus,
       "mefSoamDmCfgCosType": mefSoamDmCfgCosType,
       "mefSoamDmCfgTcaNextIndex": mefSoamDmCfgTcaNextIndex,
       "mefSoamDmCfgDei": mefSoamDmCfgDei,
       "mefSoamDmCfgMeasBinTable": mefSoamDmCfgMeasBinTable,
       "mefSoamDmCfgMeasBinEntry": mefSoamDmCfgMeasBinEntry,
       "mefSoamDmCfgMeasBinType": mefSoamDmCfgMeasBinType,
       "mefSoamDmCfgMeasBinNumber": mefSoamDmCfgMeasBinNumber,
       "mefSoamDmCfgMeasBinLowerBound": mefSoamDmCfgMeasBinLowerBound,
       "mefSoamDmCurrentStatsBinsTable": mefSoamDmCurrentStatsBinsTable,
       "mefSoamDmCurrentStatsBinsEntry": mefSoamDmCurrentStatsBinsEntry,
       "mefSoamDmCurrentStatsBinsCounter": mefSoamDmCurrentStatsBinsCounter,
       "mefSoamDmHistoryStatsBinsTable": mefSoamDmHistoryStatsBinsTable,
       "mefSoamDmHistoryStatsBinsEntry": mefSoamDmHistoryStatsBinsEntry,
       "mefSoamDmHistoryStatsBinsCounter": mefSoamDmHistoryStatsBinsCounter,
       "mefSoamDmTcaCfgTable": mefSoamDmTcaCfgTable,
       "mefSoamDmTcaCfgEntry": mefSoamDmTcaCfgEntry,
       "mefSoamDmTcaCfgIndex": mefSoamDmTcaCfgIndex,
       "mefSoamDmTcaCfgType": mefSoamDmTcaCfgType,
       "mefSoamDmTcaCfgEnable": mefSoamDmTcaCfgEnable,
       "mefSoamDmTcaCfgAlarmType": mefSoamDmTcaCfgAlarmType,
       "mefSoamDmTcaCfgBinNumber": mefSoamDmTcaCfgBinNumber,
       "mefSoamDmTcaCfgThresholdValue": mefSoamDmTcaCfgThresholdValue,
       "mefSoamDmTcaCfgClearValue": mefSoamDmTcaCfgClearValue,
       "mefSoamDmTcaCfgAlarmCurrentState": mefSoamDmTcaCfgAlarmCurrentState,
       "mefSoamDmTcaCfgRowStatus": mefSoamDmTcaCfgRowStatus,
       "mefSoamDmMeasuredStatsXTable": mefSoamDmMeasuredStatsXTable,
       "mefSoamDmMeasuredStatsXEntry": mefSoamDmMeasuredStatsXEntry,
       "mefSoamDmMeasuredStatsXFrameDelayTwoWay": mefSoamDmMeasuredStatsXFrameDelayTwoWay,
       "mefSoamDmMeasuredStatsXFrameDelayForward": mefSoamDmMeasuredStatsXFrameDelayForward,
       "mefSoamDmMeasuredStatsXFrameDelayBackward": mefSoamDmMeasuredStatsXFrameDelayBackward,
       "mefSoamDmMeasuredStatsXIfdvTwoWay": mefSoamDmMeasuredStatsXIfdvTwoWay,
       "mefSoamDmMeasuredStatsXIfdvForward": mefSoamDmMeasuredStatsXIfdvForward,
       "mefSoamDmMeasuredStatsXIfdvBackward": mefSoamDmMeasuredStatsXIfdvBackward,
       "mefSoamDmCurrentStatsXTable": mefSoamDmCurrentStatsXTable,
       "mefSoamDmCurrentStatsXEntry": mefSoamDmCurrentStatsXEntry,
       "mefSoamDmCurrentStatsXIndex": mefSoamDmCurrentStatsXIndex,
       "mefSoamDmCurrentStatsXStartTime": mefSoamDmCurrentStatsXStartTime,
       "mefSoamDmCurrentStatsXElapsedTime": mefSoamDmCurrentStatsXElapsedTime,
       "mefSoamDmCurrentStatsXSuspect": mefSoamDmCurrentStatsXSuspect,
       "mefSoamDmCurrentStatsXFrameDelayTwoWayMin": mefSoamDmCurrentStatsXFrameDelayTwoWayMin,
       "mefSoamDmCurrentStatsXFrameDelayTwoWayMax": mefSoamDmCurrentStatsXFrameDelayTwoWayMax,
       "mefSoamDmCurrentStatsXFrameDelayTwoWayAvg": mefSoamDmCurrentStatsXFrameDelayTwoWayAvg,
       "mefSoamDmCurrentStatsXFrameDelayForwardMin": mefSoamDmCurrentStatsXFrameDelayForwardMin,
       "mefSoamDmCurrentStatsXFrameDelayForwardMax": mefSoamDmCurrentStatsXFrameDelayForwardMax,
       "mefSoamDmCurrentStatsXFrameDelayForwardAvg": mefSoamDmCurrentStatsXFrameDelayForwardAvg,
       "mefSoamDmCurrentStatsXFrameDelayBackwardMin": mefSoamDmCurrentStatsXFrameDelayBackwardMin,
       "mefSoamDmCurrentStatsXFrameDelayBackwardMax": mefSoamDmCurrentStatsXFrameDelayBackwardMax,
       "mefSoamDmCurrentStatsXFrameDelayBackwardAvg": mefSoamDmCurrentStatsXFrameDelayBackwardAvg,
       "mefSoamDmCurrentStatsXIfdvForwardMax": mefSoamDmCurrentStatsXIfdvForwardMax,
       "mefSoamDmCurrentStatsXIfdvForwardAvg": mefSoamDmCurrentStatsXIfdvForwardAvg,
       "mefSoamDmCurrentStatsXIfdvBackwardMax": mefSoamDmCurrentStatsXIfdvBackwardMax,
       "mefSoamDmCurrentStatsXIfdvBackwardAvg": mefSoamDmCurrentStatsXIfdvBackwardAvg,
       "mefSoamDmCurrentStatsXIfdvTwoWayMax": mefSoamDmCurrentStatsXIfdvTwoWayMax,
       "mefSoamDmCurrentStatsXIfdvTwoWayAvg": mefSoamDmCurrentStatsXIfdvTwoWayAvg,
       "mefSoamDmCurrentStatsXFrameDelayRangeForwardMax": mefSoamDmCurrentStatsXFrameDelayRangeForwardMax,
       "mefSoamDmCurrentStatsXFrameDelayRangeForwardAvg": mefSoamDmCurrentStatsXFrameDelayRangeForwardAvg,
       "mefSoamDmCurrentStatsXFrameDelayRangeBackwardMax": mefSoamDmCurrentStatsXFrameDelayRangeBackwardMax,
       "mefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg": mefSoamDmCurrentStatsXFrameDelayRangeBackwardAvg,
       "mefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax": mefSoamDmCurrentStatsXFrameDelayRangeTwoWayMax,
       "mefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg": mefSoamDmCurrentStatsXFrameDelayRangeTwoWayAvg,
       "mefSoamDmCurrentStatsXSoamPdusSent": mefSoamDmCurrentStatsXSoamPdusSent,
       "mefSoamDmCurrentStatsXSoamPdusReceived": mefSoamDmCurrentStatsXSoamPdusReceived,
       "mefSoamDmHistoryStatsXTable": mefSoamDmHistoryStatsXTable,
       "mefSoamDmHistoryStatsXEntry": mefSoamDmHistoryStatsXEntry,
       "mefSoamDmHistoryStatsXIndex": mefSoamDmHistoryStatsXIndex,
       "mefSoamDmHistoryStatsXEndTime": mefSoamDmHistoryStatsXEndTime,
       "mefSoamDmHistoryStatsXElapsedTime": mefSoamDmHistoryStatsXElapsedTime,
       "mefSoamDmHistoryStatsXSuspect": mefSoamDmHistoryStatsXSuspect,
       "mefSoamDmHistoryStatsXFrameDelayTwoWayMin": mefSoamDmHistoryStatsXFrameDelayTwoWayMin,
       "mefSoamDmHistoryStatsXFrameDelayTwoWayMax": mefSoamDmHistoryStatsXFrameDelayTwoWayMax,
       "mefSoamDmHistoryStatsXFrameDelayTwoWayAvg": mefSoamDmHistoryStatsXFrameDelayTwoWayAvg,
       "mefSoamDmHistoryStatsXFrameDelayForwardMin": mefSoamDmHistoryStatsXFrameDelayForwardMin,
       "mefSoamDmHistoryStatsXFrameDelayForwardMax": mefSoamDmHistoryStatsXFrameDelayForwardMax,
       "mefSoamDmHistoryStatsXFrameDelayForwardAvg": mefSoamDmHistoryStatsXFrameDelayForwardAvg,
       "mefSoamDmHistoryStatsXFrameDelayBackwardMin": mefSoamDmHistoryStatsXFrameDelayBackwardMin,
       "mefSoamDmHistoryStatsXFrameDelayBackwardMax": mefSoamDmHistoryStatsXFrameDelayBackwardMax,
       "mefSoamDmHistoryStatsXFrameDelayBackwardAvg": mefSoamDmHistoryStatsXFrameDelayBackwardAvg,
       "mefSoamDmHistoryStatsXIfdvForwardMax": mefSoamDmHistoryStatsXIfdvForwardMax,
       "mefSoamDmHistoryStatsXIfdvForwardAvg": mefSoamDmHistoryStatsXIfdvForwardAvg,
       "mefSoamDmHistoryStatsXIfdvBackwardMax": mefSoamDmHistoryStatsXIfdvBackwardMax,
       "mefSoamDmHistoryStatsXIfdvBackwardAvg": mefSoamDmHistoryStatsXIfdvBackwardAvg,
       "mefSoamDmHistoryStatsXIfdvTwoWayMax": mefSoamDmHistoryStatsXIfdvTwoWayMax,
       "mefSoamDmHistoryStatsXIfdvTwoWayAvg": mefSoamDmHistoryStatsXIfdvTwoWayAvg,
       "mefSoamDmHistoryStatsXFrameDelayRangeForwardMax": mefSoamDmHistoryStatsXFrameDelayRangeForwardMax,
       "mefSoamDmHistoryStatsXFrameDelayRangeForwardAvg": mefSoamDmHistoryStatsXFrameDelayRangeForwardAvg,
       "mefSoamDmHistoryStatsXFrameDelayRangeBackwardMax": mefSoamDmHistoryStatsXFrameDelayRangeBackwardMax,
       "mefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg": mefSoamDmHistoryStatsXFrameDelayRangeBackwardAvg,
       "mefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax": mefSoamDmHistoryStatsXFrameDelayRangeTwoWayMax,
       "mefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg": mefSoamDmHistoryStatsXFrameDelayRangeTwoWayAvg,
       "mefSoamDmHistoryStatsXSoamPdusSent": mefSoamDmHistoryStatsXSoamPdusSent,
       "mefSoamDmHistoryStatsXSoamPdusReceived": mefSoamDmHistoryStatsXSoamPdusReceived,
       "mefSoamPmNotificationCfg": mefSoamPmNotificationCfg,
       "mefSoamPmNotificationCfgAlarmInterval": mefSoamPmNotificationCfgAlarmInterval,
       "mefSoamPmNotificationCfgAlarmEnable": mefSoamPmNotificationCfgAlarmEnable,
       "mefSoamPmNotificationObj": mefSoamPmNotificationObj,
       "mefSoamPmNotificationObjDateAndTime": mefSoamPmNotificationObjDateAndTime,
       "mefSoamPmNotificationObjThresholdId": mefSoamPmNotificationObjThresholdId,
       "mefSoamPmNotificationObjThresholdConfig": mefSoamPmNotificationObjThresholdConfig,
       "mefSoamPmNotificationObjThresholdValue": mefSoamPmNotificationObjThresholdValue,
       "mefSoamPmNotificationObjSuspect": mefSoamPmNotificationObjSuspect,
       "mefSoamPmNotificationObjCrossingType": mefSoamPmNotificationObjCrossingType,
       "mefSoamPmNotificationObjDestinationMep": mefSoamPmNotificationObjDestinationMep,
       "mefSoamPmNotificationObjPriority": mefSoamPmNotificationObjPriority,
       "mefSoamPmNotificationObjDestinationMepId": mefSoamPmNotificationObjDestinationMepId,
       "mefSoamPmNotificationObjMeasurementInterval": mefSoamPmNotificationObjMeasurementInterval,
       "mefSoamPmNotificationObjSeverity": mefSoamPmNotificationObjSeverity,
       "mefSoamPmNotificationObjAvailabilityStatus": mefSoamPmNotificationObjAvailabilityStatus,
       "mefSoamPmMibConformance": mefSoamPmMibConformance,
       "mefSoamPmMibCompliances": mefSoamPmMibCompliances,
       "mefSoamPmMibCompliance": mefSoamPmMibCompliance,
       "mefSoamPmMibGroups": mefSoamPmMibGroups,
       "mefSoamPmMepMandatoryGroup": mefSoamPmMepMandatoryGroup,
       "mefSoamLmCfgMandatoryGroup": mefSoamLmCfgMandatoryGroup,
       "mefSoamLmCfgOptionalGroup": mefSoamLmCfgOptionalGroup,
       "mefSoamLmMeasuredStatsMandatoryGroup": mefSoamLmMeasuredStatsMandatoryGroup,
       "mefSoamLmMeasuredStatsOptionalGroup": mefSoamLmMeasuredStatsOptionalGroup,
       "mefSoamLmCurrentAvailStatsMandatoryGroup": mefSoamLmCurrentAvailStatsMandatoryGroup,
       "mefSoamLmCurrentAvailStatsOptionalGroup": mefSoamLmCurrentAvailStatsOptionalGroup,
       "mefSoamLmCurrentStatsMandatoryGroup": mefSoamLmCurrentStatsMandatoryGroup,
       "mefSoamLmCurrentStatsOptionalGroup": mefSoamLmCurrentStatsOptionalGroup,
       "mefSoamLmHistoryAvailStatsMandatoryGroup": mefSoamLmHistoryAvailStatsMandatoryGroup,
       "mefSoamLmHistoryAvailStatsOptionalGroup": mefSoamLmHistoryAvailStatsOptionalGroup,
       "mefSoamLmHistoryStatsMandatoryGroup": mefSoamLmHistoryStatsMandatoryGroup,
       "mefSoamLmHistoryStatsOptionalGroup": mefSoamLmHistoryStatsOptionalGroup,
       "mefSoamDmCfgMandatoryGroup": mefSoamDmCfgMandatoryGroup,
       "mefSoamDmCfgOptionalGroup": mefSoamDmCfgOptionalGroup,
       "mefSoamDmCfgMeasBinMandatoryGroup": mefSoamDmCfgMeasBinMandatoryGroup,
       "mefSoamDmMeasuredStatsOptionalGroup": mefSoamDmMeasuredStatsOptionalGroup,
       "mefSoamDmCurrentStatsMandatoryGroup": mefSoamDmCurrentStatsMandatoryGroup,
       "mefSoamDmCurrentStatsOptionalGroup": mefSoamDmCurrentStatsOptionalGroup,
       "mefSoamDmCurrentStatsBinsMandatoryGroup": mefSoamDmCurrentStatsBinsMandatoryGroup,
       "mefSoamDmHistoryStatsMandatoryGroup": mefSoamDmHistoryStatsMandatoryGroup,
       "mefSoamDmHistoryStatsOptionalGroup": mefSoamDmHistoryStatsOptionalGroup,
       "mefSoamDmHistoryStatsBinsMandatoryGroup": mefSoamDmHistoryStatsBinsMandatoryGroup,
       "mefSoamPmNotificationsMandatoryGroup": mefSoamPmNotificationsMandatoryGroup,
       "mefSoamPmNotificationsOptionalGroup": mefSoamPmNotificationsOptionalGroup,
       "mefSoamPmNotificationCfgMandatoryGroup": mefSoamPmNotificationCfgMandatoryGroup,
       "mefSoamPmNotificationObjMandatoryGroup": mefSoamPmNotificationObjMandatoryGroup,
       "mefSoamPmNotificationObjOptionalGroup": mefSoamPmNotificationObjOptionalGroup,
       "mefSoamLmTcaOptionalGroup": mefSoamLmTcaOptionalGroup,
       "mefSoamDmTcaOptionalGroup": mefSoamDmTcaOptionalGroup}
)
