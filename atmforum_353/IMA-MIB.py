# SNMP MIB module (IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/IMA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:06:53 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

atmfImaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1)
)
if mibBuilder.loadTexts:
    atmfImaMib.setRevisions(
        ("2003-08-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliSeconds(TextualConvention, Integer32):
    status = "current"


class ImaGroupState(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 1),
          ("startUp", 2),
          ("startUpAck", 3),
          ("configAbortUnsupportedM", 4),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("insufficientLinks", 7),
          ("blocked", 8),
          ("operational", 9),
          ("configAbortUnsupportedImaVersion", 10))
    )



class ImaGroupFailureStatus(TextualConvention, Integer32):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("noFailure", 1),
          ("startUpNe", 2),
          ("startUpFe", 3),
          ("invalidMValueNe", 4),
          ("invalidMValueFe", 5),
          ("failedAssymetricNe", 6),
          ("failedAssymetricFe", 7),
          ("insufficientLinksNe", 8),
          ("insufficientLinksFe", 9),
          ("blockedNe", 10),
          ("blockedFe", 11),
          ("otherFailure", 12),
          ("invalidImaVersionNe", 13),
          ("invalidImaVersionFe", 14))
    )



class ImaAlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("declared", 2))
    )



class ImaAlarmType(TextualConvention, Integer32):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("imaAlarmLinkLif", 1),
          ("imaAlarmLinkLods", 2),
          ("imaAlarmLinkRfi", 3),
          ("imaAlarmLinkTxMisConnect", 4),
          ("imaAlarmLinkRxMisConnect", 5),
          ("imaAlarmLinkTxFault", 6),
          ("imaAlarmLinkRxFault", 7),
          ("imaAlarmLinkTxUnusableFe", 8),
          ("imaAlarmLinkRxUnusableFe", 9),
          ("imaAlarmGroupStartupFe", 10),
          ("imaAlarmGroupCfgAbort", 11),
          ("imaAlarmGroupCfgAbortFe", 12),
          ("imaAlarmGroupInsuffLinks", 13),
          ("imaAlarmGroupInsuffLinksFe", 14),
          ("imaAlarmGroupBlockedFe", 15),
          ("imaAlarmGroupTimingSynch", 16))
    )



class ImaGroupTxClkMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )



class ImaGroupSymmetry(TextualConvention, Integer32):
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
        *(("symmetricOperation", 1),
          ("asymmetricOperation", 2),
          ("asymmetricConfiguration", 3))
    )



class ImaFrameLength(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("m32", 32),
          ("m64", 64),
          ("m128", 128),
          ("m256", 256))
    )



class ImaLinkState(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notInGroup", 1),
          ("unusableNoGivenReason", 2),
          ("unusableFault", 3),
          ("unusableMisconnected", 4),
          ("unusableInhibited", 5),
          ("unusableFailed", 6),
          ("usable", 7),
          ("active", 8))
    )



class ImaLinkFailureStatus(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noFailure", 1),
          ("imaLinkFailure", 2),
          ("lifFailure", 3),
          ("lodsFailure", 4),
          ("misConnected", 5),
          ("blocked", 6),
          ("fault", 7),
          ("farEndTxLinkUnusable", 8),
          ("farEndRxLinkUnusable", 9))
    )



class ImaTestProcStatus(TextualConvention, Integer32):
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
          ("operating", 2),
          ("linkFail", 3))
    )



class ImaPerfCurrDayCount(TextualConvention, Gauge32):
    status = "current"


class ImaPerfTimeElapsed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )



class ImaPerf1DayIntervalCount(TextualConvention, Gauge32):
    status = "current"


class ImaPerfIntervalThreshold(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfIma_ObjectIdentity = ObjectIdentity
atmfIma = _AtmfIma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7)
)
_ImaMibObjects_ObjectIdentity = ObjectIdentity
imaMibObjects = _ImaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1)
)
_ImaGroupTable_Object = MibTable
imaGroupTable = _ImaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    imaGroupTable.setStatus("current")
_ImaGroupEntry_Object = MibTableRow
imaGroupEntry = _ImaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1)
)
imaGroupEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    imaGroupEntry.setStatus("current")


class _ImaGroupIndex_Type(Integer32):
    """Custom type imaGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ImaGroupIndex_Type.__name__ = "Integer32"
_ImaGroupIndex_Object = MibTableColumn
imaGroupIndex = _ImaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 1),
    _ImaGroupIndex_Type()
)
imaGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaGroupIndex.setStatus("current")
_ImaGroupRowStatus_Type = RowStatus
_ImaGroupRowStatus_Object = MibTableColumn
imaGroupRowStatus = _ImaGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 2),
    _ImaGroupRowStatus_Type()
)
imaGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupRowStatus.setStatus("current")
_ImaGroupIfIndex_Type = InterfaceIndex
_ImaGroupIfIndex_Object = MibTableColumn
imaGroupIfIndex = _ImaGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 3),
    _ImaGroupIfIndex_Type()
)
imaGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIfIndex.setStatus("current")
_ImaGroupNeState_Type = ImaGroupState
_ImaGroupNeState_Object = MibTableColumn
imaGroupNeState = _ImaGroupNeState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 4),
    _ImaGroupNeState_Type()
)
imaGroupNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNeState.setStatus("current")
_ImaGroupFeState_Type = ImaGroupState
_ImaGroupFeState_Object = MibTableColumn
imaGroupFeState = _ImaGroupFeState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 5),
    _ImaGroupFeState_Type()
)
imaGroupFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeState.setStatus("current")
_ImaGroupFailureStatus_Type = ImaGroupFailureStatus
_ImaGroupFailureStatus_Object = MibTableColumn
imaGroupFailureStatus = _ImaGroupFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 6),
    _ImaGroupFailureStatus_Type()
)
imaGroupFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFailureStatus.setStatus("current")


class _ImaGroupSymmetry_Type(ImaGroupSymmetry):
    """Custom type imaGroupSymmetry based on ImaGroupSymmetry"""
    defaultValue = 1


_ImaGroupSymmetry_Type.__name__ = "ImaGroupSymmetry"
_ImaGroupSymmetry_Object = MibTableColumn
imaGroupSymmetry = _ImaGroupSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 7),
    _ImaGroupSymmetry_Type()
)
imaGroupSymmetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupSymmetry.setStatus("current")


class _ImaGroupMinNumTxLinks_Type(Integer32):
    """Custom type imaGroupMinNumTxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ImaGroupMinNumTxLinks_Type.__name__ = "Integer32"
_ImaGroupMinNumTxLinks_Object = MibTableColumn
imaGroupMinNumTxLinks = _ImaGroupMinNumTxLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 8),
    _ImaGroupMinNumTxLinks_Type()
)
imaGroupMinNumTxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupMinNumTxLinks.setStatus("current")


class _ImaGroupMinNumRxLinks_Type(Integer32):
    """Custom type imaGroupMinNumRxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ImaGroupMinNumRxLinks_Type.__name__ = "Integer32"
_ImaGroupMinNumRxLinks_Object = MibTableColumn
imaGroupMinNumRxLinks = _ImaGroupMinNumRxLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 9),
    _ImaGroupMinNumRxLinks_Type()
)
imaGroupMinNumRxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupMinNumRxLinks.setStatus("current")


class _ImaGroupNeTxClkMode_Type(ImaGroupTxClkMode):
    """Custom type imaGroupNeTxClkMode based on ImaGroupTxClkMode"""
    defaultValue = 1


_ImaGroupNeTxClkMode_Type.__name__ = "ImaGroupTxClkMode"
_ImaGroupNeTxClkMode_Object = MibTableColumn
imaGroupNeTxClkMode = _ImaGroupNeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 10),
    _ImaGroupNeTxClkMode_Type()
)
imaGroupNeTxClkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupNeTxClkMode.setStatus("current")
_ImaGroupFeTxClkMode_Type = ImaGroupTxClkMode
_ImaGroupFeTxClkMode_Object = MibTableColumn
imaGroupFeTxClkMode = _ImaGroupFeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 11),
    _ImaGroupFeTxClkMode_Type()
)
imaGroupFeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeTxClkMode.setStatus("current")
_ImaGroupTxTimingRefLink_Type = InterfaceIndexOrZero
_ImaGroupTxTimingRefLink_Object = MibTableColumn
imaGroupTxTimingRefLink = _ImaGroupTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 12),
    _ImaGroupTxTimingRefLink_Type()
)
imaGroupTxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTxTimingRefLink.setStatus("current")
_ImaGroupRxTimingRefLink_Type = InterfaceIndexOrZero
_ImaGroupRxTimingRefLink_Object = MibTableColumn
imaGroupRxTimingRefLink = _ImaGroupRxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 13),
    _ImaGroupRxTimingRefLink_Type()
)
imaGroupRxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxTimingRefLink.setStatus("current")
_ImaGroupLastChange_Type = DateAndTime
_ImaGroupLastChange_Object = MibTableColumn
imaGroupLastChange = _ImaGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 14),
    _ImaGroupLastChange_Type()
)
imaGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupLastChange.setStatus("current")


class _ImaGroupTxImaId_Type(Integer32):
    """Custom type imaGroupTxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaGroupTxImaId_Type.__name__ = "Integer32"
_ImaGroupTxImaId_Object = MibTableColumn
imaGroupTxImaId = _ImaGroupTxImaId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 15),
    _ImaGroupTxImaId_Type()
)
imaGroupTxImaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTxImaId.setStatus("current")


class _ImaGroupRxImaId_Type(Integer32):
    """Custom type imaGroupRxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaGroupRxImaId_Type.__name__ = "Integer32"
_ImaGroupRxImaId_Object = MibTableColumn
imaGroupRxImaId = _ImaGroupRxImaId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 16),
    _ImaGroupRxImaId_Type()
)
imaGroupRxImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxImaId.setStatus("current")


class _ImaGroupTxFrameLength_Type(ImaFrameLength):
    """Custom type imaGroupTxFrameLength based on ImaFrameLength"""
    defaultValue = 128


_ImaGroupTxFrameLength_Type.__name__ = "ImaFrameLength"
_ImaGroupTxFrameLength_Object = MibTableColumn
imaGroupTxFrameLength = _ImaGroupTxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 17),
    _ImaGroupTxFrameLength_Type()
)
imaGroupTxFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTxFrameLength.setStatus("current")
_ImaGroupRxFrameLength_Type = ImaFrameLength
_ImaGroupRxFrameLength_Object = MibTableColumn
imaGroupRxFrameLength = _ImaGroupRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 18),
    _ImaGroupRxFrameLength_Type()
)
imaGroupRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxFrameLength.setStatus("current")


class _ImaGroupDiffDelayMax_Type(MilliSeconds):
    """Custom type imaGroupDiffDelayMax based on MilliSeconds"""
    defaultValue = 25


_ImaGroupDiffDelayMax_Type.__name__ = "MilliSeconds"
_ImaGroupDiffDelayMax_Object = MibTableColumn
imaGroupDiffDelayMax = _ImaGroupDiffDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 19),
    _ImaGroupDiffDelayMax_Type()
)
imaGroupDiffDelayMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupDiffDelayMax.setStatus("current")
_ImaGroupLeastDelayLink_Type = InterfaceIndexOrZero
_ImaGroupLeastDelayLink_Object = MibTableColumn
imaGroupLeastDelayLink = _ImaGroupLeastDelayLink_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 20),
    _ImaGroupLeastDelayLink_Type()
)
imaGroupLeastDelayLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupLeastDelayLink.setStatus("current")
_ImaGroupDiffDelayMaxObs_Type = MilliSeconds
_ImaGroupDiffDelayMaxObs_Object = MibTableColumn
imaGroupDiffDelayMaxObs = _ImaGroupDiffDelayMaxObs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 21),
    _ImaGroupDiffDelayMaxObs_Type()
)
imaGroupDiffDelayMaxObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupDiffDelayMaxObs.setStatus("current")


class _ImaGroupAlphaValue_Type(Integer32):
    """Custom type imaGroupAlphaValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ImaGroupAlphaValue_Type.__name__ = "Integer32"
_ImaGroupAlphaValue_Object = MibTableColumn
imaGroupAlphaValue = _ImaGroupAlphaValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 22),
    _ImaGroupAlphaValue_Type()
)
imaGroupAlphaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupAlphaValue.setStatus("current")


class _ImaGroupBetaValue_Type(Integer32):
    """Custom type imaGroupBetaValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ImaGroupBetaValue_Type.__name__ = "Integer32"
_ImaGroupBetaValue_Object = MibTableColumn
imaGroupBetaValue = _ImaGroupBetaValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 23),
    _ImaGroupBetaValue_Type()
)
imaGroupBetaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupBetaValue.setStatus("current")


class _ImaGroupGammaValue_Type(Integer32):
    """Custom type imaGroupGammaValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ImaGroupGammaValue_Type.__name__ = "Integer32"
_ImaGroupGammaValue_Object = MibTableColumn
imaGroupGammaValue = _ImaGroupGammaValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 24),
    _ImaGroupGammaValue_Type()
)
imaGroupGammaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupGammaValue.setStatus("current")
_ImaGroupRunningSecs_Type = Gauge32
_ImaGroupRunningSecs_Object = MibTableColumn
imaGroupRunningSecs = _ImaGroupRunningSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 25),
    _ImaGroupRunningSecs_Type()
)
imaGroupRunningSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRunningSecs.setStatus("current")
_ImaGroupUnavailSecs_Type = Counter32
_ImaGroupUnavailSecs_Object = MibTableColumn
imaGroupUnavailSecs = _ImaGroupUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 26),
    _ImaGroupUnavailSecs_Type()
)
imaGroupUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupUnavailSecs.setStatus("current")
_ImaGroupNeNumFailures_Type = Counter32
_ImaGroupNeNumFailures_Object = MibTableColumn
imaGroupNeNumFailures = _ImaGroupNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 27),
    _ImaGroupNeNumFailures_Type()
)
imaGroupNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNeNumFailures.setStatus("current")
_ImaGroupFeNumFailures_Type = Counter32
_ImaGroupFeNumFailures_Object = MibTableColumn
imaGroupFeNumFailures = _ImaGroupFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 28),
    _ImaGroupFeNumFailures_Type()
)
imaGroupFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeNumFailures.setStatus("current")
_ImaGroupTxAvailCellRate_Type = Gauge32
_ImaGroupTxAvailCellRate_Object = MibTableColumn
imaGroupTxAvailCellRate = _ImaGroupTxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 29),
    _ImaGroupTxAvailCellRate_Type()
)
imaGroupTxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTxAvailCellRate.setStatus("current")
_ImaGroupRxAvailCellRate_Type = Gauge32
_ImaGroupRxAvailCellRate_Object = MibTableColumn
imaGroupRxAvailCellRate = _ImaGroupRxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 30),
    _ImaGroupRxAvailCellRate_Type()
)
imaGroupRxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxAvailCellRate.setStatus("current")
_ImaGroupNumTxCfgLinks_Type = Gauge32
_ImaGroupNumTxCfgLinks_Object = MibTableColumn
imaGroupNumTxCfgLinks = _ImaGroupNumTxCfgLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 31),
    _ImaGroupNumTxCfgLinks_Type()
)
imaGroupNumTxCfgLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumTxCfgLinks.setStatus("current")
_ImaGroupNumRxCfgLinks_Type = Gauge32
_ImaGroupNumRxCfgLinks_Object = MibTableColumn
imaGroupNumRxCfgLinks = _ImaGroupNumRxCfgLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 32),
    _ImaGroupNumRxCfgLinks_Type()
)
imaGroupNumRxCfgLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumRxCfgLinks.setStatus("current")
_ImaGroupNumTxActLinks_Type = Gauge32
_ImaGroupNumTxActLinks_Object = MibTableColumn
imaGroupNumTxActLinks = _ImaGroupNumTxActLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 33),
    _ImaGroupNumTxActLinks_Type()
)
imaGroupNumTxActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumTxActLinks.setStatus("current")
_ImaGroupNumRxActLinks_Type = Gauge32
_ImaGroupNumRxActLinks_Object = MibTableColumn
imaGroupNumRxActLinks = _ImaGroupNumRxActLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 34),
    _ImaGroupNumRxActLinks_Type()
)
imaGroupNumRxActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumRxActLinks.setStatus("current")


class _ImaGroupTestLinkIfIndex_Type(InterfaceIndexOrZero):
    """Custom type imaGroupTestLinkIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_ImaGroupTestLinkIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_ImaGroupTestLinkIfIndex_Object = MibTableColumn
imaGroupTestLinkIfIndex = _ImaGroupTestLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 35),
    _ImaGroupTestLinkIfIndex_Type()
)
imaGroupTestLinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTestLinkIfIndex.setStatus("current")


class _ImaGroupTestPattern_Type(Integer32):
    """Custom type imaGroupTestPattern based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_ImaGroupTestPattern_Type.__name__ = "Integer32"
_ImaGroupTestPattern_Object = MibTableColumn
imaGroupTestPattern = _ImaGroupTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 36),
    _ImaGroupTestPattern_Type()
)
imaGroupTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTestPattern.setStatus("current")


class _ImaGroupTestProcStatus_Type(ImaTestProcStatus):
    """Custom type imaGroupTestProcStatus based on ImaTestProcStatus"""
    defaultValue = 1


_ImaGroupTestProcStatus_Type.__name__ = "ImaTestProcStatus"
_ImaGroupTestProcStatus_Object = MibTableColumn
imaGroupTestProcStatus = _ImaGroupTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 37),
    _ImaGroupTestProcStatus_Type()
)
imaGroupTestProcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTestProcStatus.setStatus("current")
_ImaGroupTimeElapsed_Type = ImaPerfTimeElapsed
_ImaGroupTimeElapsed_Object = MibTableColumn
imaGroupTimeElapsed = _ImaGroupTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 40),
    _ImaGroupTimeElapsed_Type()
)
imaGroupTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTimeElapsed.setStatus("current")


class _ImaGroupTxOamLabelValue_Type(Integer32):
    """Custom type imaGroupTxOamLabelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ImaGroupTxOamLabelValue_Type.__name__ = "Integer32"
_ImaGroupTxOamLabelValue_Object = MibTableColumn
imaGroupTxOamLabelValue = _ImaGroupTxOamLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 41),
    _ImaGroupTxOamLabelValue_Type()
)
imaGroupTxOamLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTxOamLabelValue.setStatus("current")


class _ImaGroupRxOamLabelValue_Type(Integer32):
    """Custom type imaGroupRxOamLabelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaGroupRxOamLabelValue_Type.__name__ = "Integer32"
_ImaGroupRxOamLabelValue_Object = MibTableColumn
imaGroupRxOamLabelValue = _ImaGroupRxOamLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 42),
    _ImaGroupRxOamLabelValue_Type()
)
imaGroupRxOamLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxOamLabelValue.setStatus("current")


class _ImaGroupConfAlarmProfile_Type(SnmpAdminString):
    """Custom type imaGroupConfAlarmProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ImaGroupConfAlarmProfile_Type.__name__ = "SnmpAdminString"
_ImaGroupConfAlarmProfile_Object = MibTableColumn
imaGroupConfAlarmProfile = _ImaGroupConfAlarmProfile_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 43),
    _ImaGroupConfAlarmProfile_Type()
)
imaGroupConfAlarmProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupConfAlarmProfile.setStatus("current")
_ImaGroupMappingTable_Object = MibTable
imaGroupMappingTable = _ImaGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    imaGroupMappingTable.setStatus("current")
_ImaGroupMappingEntry_Object = MibTableRow
imaGroupMappingEntry = _ImaGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 3, 1)
)
imaGroupMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    imaGroupMappingEntry.setStatus("current")
_ImaGroupMappingIndex_Type = Integer32
_ImaGroupMappingIndex_Object = MibTableColumn
imaGroupMappingIndex = _ImaGroupMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 3, 1, 1),
    _ImaGroupMappingIndex_Type()
)
imaGroupMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupMappingIndex.setStatus("current")
_ImaLinkTable_Object = MibTable
imaLinkTable = _ImaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    imaLinkTable.setStatus("current")
_ImaLinkEntry_Object = MibTableRow
imaLinkEntry = _ImaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1)
)
imaLinkEntry.setIndexNames(
    (0, "IMA-MIB", "imaLinkIfIndex"),
)
if mibBuilder.loadTexts:
    imaLinkEntry.setStatus("current")
_ImaLinkIfIndex_Type = InterfaceIndex
_ImaLinkIfIndex_Object = MibTableColumn
imaLinkIfIndex = _ImaLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 1),
    _ImaLinkIfIndex_Type()
)
imaLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaLinkIfIndex.setStatus("current")
_ImaLinkRowStatus_Type = RowStatus
_ImaLinkRowStatus_Object = MibTableColumn
imaLinkRowStatus = _ImaLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 2),
    _ImaLinkRowStatus_Type()
)
imaLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkRowStatus.setStatus("current")
_ImaLinkGroupIndex_Type = Integer32
_ImaLinkGroupIndex_Object = MibTableColumn
imaLinkGroupIndex = _ImaLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 3),
    _ImaLinkGroupIndex_Type()
)
imaLinkGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkGroupIndex.setStatus("current")
_ImaLinkNeTxState_Type = ImaLinkState
_ImaLinkNeTxState_Object = MibTableColumn
imaLinkNeTxState = _ImaLinkNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 4),
    _ImaLinkNeTxState_Type()
)
imaLinkNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxState.setStatus("current")
_ImaLinkNeRxState_Type = ImaLinkState
_ImaLinkNeRxState_Object = MibTableColumn
imaLinkNeRxState = _ImaLinkNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 5),
    _ImaLinkNeRxState_Type()
)
imaLinkNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxState.setStatus("current")
_ImaLinkFeTxState_Type = ImaLinkState
_ImaLinkFeTxState_Object = MibTableColumn
imaLinkFeTxState = _ImaLinkFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 6),
    _ImaLinkFeTxState_Type()
)
imaLinkFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxState.setStatus("current")
_ImaLinkFeRxState_Type = ImaLinkState
_ImaLinkFeRxState_Object = MibTableColumn
imaLinkFeRxState = _ImaLinkFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 7),
    _ImaLinkFeRxState_Type()
)
imaLinkFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxState.setStatus("current")
_ImaLinkNeRxFailureStatus_Type = ImaLinkFailureStatus
_ImaLinkNeRxFailureStatus_Object = MibTableColumn
imaLinkNeRxFailureStatus = _ImaLinkNeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 8),
    _ImaLinkNeRxFailureStatus_Type()
)
imaLinkNeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxFailureStatus.setStatus("current")
_ImaLinkFeRxFailureStatus_Type = ImaLinkFailureStatus
_ImaLinkFeRxFailureStatus_Object = MibTableColumn
imaLinkFeRxFailureStatus = _ImaLinkFeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 9),
    _ImaLinkFeRxFailureStatus_Type()
)
imaLinkFeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxFailureStatus.setStatus("current")


class _ImaLinkTxLid_Type(Integer32):
    """Custom type imaLinkTxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ImaLinkTxLid_Type.__name__ = "Integer32"
_ImaLinkTxLid_Object = MibTableColumn
imaLinkTxLid = _ImaLinkTxLid_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 10),
    _ImaLinkTxLid_Type()
)
imaLinkTxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTxLid.setStatus("current")


class _ImaLinkRxLid_Type(Integer32):
    """Custom type imaLinkRxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ImaLinkRxLid_Type.__name__ = "Integer32"
_ImaLinkRxLid_Object = MibTableColumn
imaLinkRxLid = _ImaLinkRxLid_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 11),
    _ImaLinkRxLid_Type()
)
imaLinkRxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxLid.setStatus("current")
_ImaLinkRelDelay_Type = MilliSeconds
_ImaLinkRelDelay_Object = MibTableColumn
imaLinkRelDelay = _ImaLinkRelDelay_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 12),
    _ImaLinkRelDelay_Type()
)
imaLinkRelDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRelDelay.setStatus("current")
_ImaLinkImaViolations_Type = Counter32
_ImaLinkImaViolations_Object = MibTableColumn
imaLinkImaViolations = _ImaLinkImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 13),
    _ImaLinkImaViolations_Type()
)
imaLinkImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkImaViolations.setStatus("current")
_ImaLinkOifAnomalies_Type = Counter32
_ImaLinkOifAnomalies_Object = MibTableColumn
imaLinkOifAnomalies = _ImaLinkOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 14),
    _ImaLinkOifAnomalies_Type()
)
imaLinkOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkOifAnomalies.setStatus("current")
_ImaLinkNeSevErroredSecs_Type = Counter32
_ImaLinkNeSevErroredSecs_Object = MibTableColumn
imaLinkNeSevErroredSecs = _ImaLinkNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 15),
    _ImaLinkNeSevErroredSecs_Type()
)
imaLinkNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeSevErroredSecs.setStatus("current")
_ImaLinkFeSevErroredSecs_Type = Counter32
_ImaLinkFeSevErroredSecs_Object = MibTableColumn
imaLinkFeSevErroredSecs = _ImaLinkFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 16),
    _ImaLinkFeSevErroredSecs_Type()
)
imaLinkFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeSevErroredSecs.setStatus("current")
_ImaLinkNeUnavailSecs_Type = Counter32
_ImaLinkNeUnavailSecs_Object = MibTableColumn
imaLinkNeUnavailSecs = _ImaLinkNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 17),
    _ImaLinkNeUnavailSecs_Type()
)
imaLinkNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeUnavailSecs.setStatus("current")
_ImaLinkFeUnavailSecs_Type = Counter32
_ImaLinkFeUnavailSecs_Object = MibTableColumn
imaLinkFeUnavailSecs = _ImaLinkFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 18),
    _ImaLinkFeUnavailSecs_Type()
)
imaLinkFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeUnavailSecs.setStatus("current")
_ImaLinkNeTxUnusableSecs_Type = Counter32
_ImaLinkNeTxUnusableSecs_Object = MibTableColumn
imaLinkNeTxUnusableSecs = _ImaLinkNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 19),
    _ImaLinkNeTxUnusableSecs_Type()
)
imaLinkNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxUnusableSecs.setStatus("current")
_ImaLinkNeRxUnusableSecs_Type = Counter32
_ImaLinkNeRxUnusableSecs_Object = MibTableColumn
imaLinkNeRxUnusableSecs = _ImaLinkNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 20),
    _ImaLinkNeRxUnusableSecs_Type()
)
imaLinkNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxUnusableSecs.setStatus("current")
_ImaLinkFeTxUnusableSecs_Type = Counter32
_ImaLinkFeTxUnusableSecs_Object = MibTableColumn
imaLinkFeTxUnusableSecs = _ImaLinkFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 21),
    _ImaLinkFeTxUnusableSecs_Type()
)
imaLinkFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxUnusableSecs.setStatus("current")
_ImaLinkFeRxUnusableSecs_Type = Counter32
_ImaLinkFeRxUnusableSecs_Object = MibTableColumn
imaLinkFeRxUnusableSecs = _ImaLinkFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 22),
    _ImaLinkFeRxUnusableSecs_Type()
)
imaLinkFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxUnusableSecs.setStatus("current")
_ImaLinkNeTxNumFailures_Type = Counter32
_ImaLinkNeTxNumFailures_Object = MibTableColumn
imaLinkNeTxNumFailures = _ImaLinkNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 23),
    _ImaLinkNeTxNumFailures_Type()
)
imaLinkNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxNumFailures.setStatus("current")
_ImaLinkNeRxNumFailures_Type = Counter32
_ImaLinkNeRxNumFailures_Object = MibTableColumn
imaLinkNeRxNumFailures = _ImaLinkNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 24),
    _ImaLinkNeRxNumFailures_Type()
)
imaLinkNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxNumFailures.setStatus("current")
_ImaLinkFeTxNumFailures_Type = Counter32
_ImaLinkFeTxNumFailures_Object = MibTableColumn
imaLinkFeTxNumFailures = _ImaLinkFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 25),
    _ImaLinkFeTxNumFailures_Type()
)
imaLinkFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxNumFailures.setStatus("current")
_ImaLinkFeRxNumFailures_Type = Counter32
_ImaLinkFeRxNumFailures_Object = MibTableColumn
imaLinkFeRxNumFailures = _ImaLinkFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 26),
    _ImaLinkFeRxNumFailures_Type()
)
imaLinkFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxNumFailures.setStatus("current")
_ImaLinkTxStuffs_Type = Counter32
_ImaLinkTxStuffs_Object = MibTableColumn
imaLinkTxStuffs = _ImaLinkTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 27),
    _ImaLinkTxStuffs_Type()
)
imaLinkTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTxStuffs.setStatus("current")
_ImaLinkRxStuffs_Type = Counter32
_ImaLinkRxStuffs_Object = MibTableColumn
imaLinkRxStuffs = _ImaLinkRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 28),
    _ImaLinkRxStuffs_Type()
)
imaLinkRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxStuffs.setStatus("current")


class _ImaLinkRxTestPattern_Type(Integer32):
    """Custom type imaLinkRxTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaLinkRxTestPattern_Type.__name__ = "Integer32"
_ImaLinkRxTestPattern_Object = MibTableColumn
imaLinkRxTestPattern = _ImaLinkRxTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 29),
    _ImaLinkRxTestPattern_Type()
)
imaLinkRxTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxTestPattern.setStatus("current")
_ImaLinkTestProcStatus_Type = ImaTestProcStatus
_ImaLinkTestProcStatus_Object = MibTableColumn
imaLinkTestProcStatus = _ImaLinkTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 30),
    _ImaLinkTestProcStatus_Type()
)
imaLinkTestProcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTestProcStatus.setStatus("current")
_ImaLinkTimeElapsed_Type = ImaPerfTimeElapsed
_ImaLinkTimeElapsed_Object = MibTableColumn
imaLinkTimeElapsed = _ImaLinkTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 33),
    _ImaLinkTimeElapsed_Type()
)
imaLinkTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTimeElapsed.setStatus("current")


class _ImaLinkConfAlarmProfile_Type(SnmpAdminString):
    """Custom type imaLinkConfAlarmProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ImaLinkConfAlarmProfile_Type.__name__ = "SnmpAdminString"
_ImaLinkConfAlarmProfile_Object = MibTableColumn
imaLinkConfAlarmProfile = _ImaLinkConfAlarmProfile_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 34),
    _ImaLinkConfAlarmProfile_Type()
)
imaLinkConfAlarmProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkConfAlarmProfile.setStatus("current")
_ImaAlarmStatus_Type = ImaAlarmStatus
_ImaAlarmStatus_Object = MibScalar
imaAlarmStatus = _ImaAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 5),
    _ImaAlarmStatus_Type()
)
imaAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    imaAlarmStatus.setStatus("current")
_ImaAlarmType_Type = ImaAlarmType
_ImaAlarmType_Object = MibScalar
imaAlarmType = _ImaAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 6),
    _ImaAlarmType_Type()
)
imaAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    imaAlarmType.setStatus("current")
_ImaGroupCurrentTable_Object = MibTable
imaGroupCurrentTable = _ImaGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7)
)
if mibBuilder.loadTexts:
    imaGroupCurrentTable.setStatus("current")
_ImaGroupCurrentEntry_Object = MibTableRow
imaGroupCurrentEntry = _ImaGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7, 1)
)
imaGroupCurrentEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    imaGroupCurrentEntry.setStatus("current")
_ImaGroupCurrentUnavailSecs_Type = PerfCurrentCount
_ImaGroupCurrentUnavailSecs_Object = MibTableColumn
imaGroupCurrentUnavailSecs = _ImaGroupCurrentUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7, 1, 1),
    _ImaGroupCurrentUnavailSecs_Type()
)
imaGroupCurrentUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrentUnavailSecs.setStatus("current")
_ImaGroupCurrentNeNumFailures_Type = PerfCurrentCount
_ImaGroupCurrentNeNumFailures_Object = MibTableColumn
imaGroupCurrentNeNumFailures = _ImaGroupCurrentNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7, 1, 2),
    _ImaGroupCurrentNeNumFailures_Type()
)
imaGroupCurrentNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrentNeNumFailures.setStatus("current")
_ImaGroupCurrentFeNumFailures_Type = PerfCurrentCount
_ImaGroupCurrentFeNumFailures_Object = MibTableColumn
imaGroupCurrentFeNumFailures = _ImaGroupCurrentFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7, 1, 3),
    _ImaGroupCurrentFeNumFailures_Type()
)
imaGroupCurrentFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrentFeNumFailures.setStatus("current")
_ImaGroupIntervalTable_Object = MibTable
imaGroupIntervalTable = _ImaGroupIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8)
)
if mibBuilder.loadTexts:
    imaGroupIntervalTable.setStatus("current")
_ImaGroupIntervalEntry_Object = MibTableRow
imaGroupIntervalEntry = _ImaGroupIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1)
)
imaGroupIntervalEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
    (0, "IMA-MIB", "imaGroupIntervalNumber"),
)
if mibBuilder.loadTexts:
    imaGroupIntervalEntry.setStatus("current")


class _ImaGroupIntervalNumber_Type(Integer32):
    """Custom type imaGroupIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ImaGroupIntervalNumber_Type.__name__ = "Integer32"
_ImaGroupIntervalNumber_Object = MibTableColumn
imaGroupIntervalNumber = _ImaGroupIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 1),
    _ImaGroupIntervalNumber_Type()
)
imaGroupIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaGroupIntervalNumber.setStatus("current")
_ImaGroupIntervalUnavailSecs_Type = PerfIntervalCount
_ImaGroupIntervalUnavailSecs_Object = MibTableColumn
imaGroupIntervalUnavailSecs = _ImaGroupIntervalUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 2),
    _ImaGroupIntervalUnavailSecs_Type()
)
imaGroupIntervalUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIntervalUnavailSecs.setStatus("current")
_ImaGroupIntervalNeNumFailures_Type = PerfIntervalCount
_ImaGroupIntervalNeNumFailures_Object = MibTableColumn
imaGroupIntervalNeNumFailures = _ImaGroupIntervalNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 3),
    _ImaGroupIntervalNeNumFailures_Type()
)
imaGroupIntervalNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIntervalNeNumFailures.setStatus("current")
_ImaGroupIntervalFeNumFailures_Type = PerfIntervalCount
_ImaGroupIntervalFeNumFailures_Object = MibTableColumn
imaGroupIntervalFeNumFailures = _ImaGroupIntervalFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 4),
    _ImaGroupIntervalFeNumFailures_Type()
)
imaGroupIntervalFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIntervalFeNumFailures.setStatus("current")
_ImaGroupIntervalMoniSecs_Type = ImaPerfTimeElapsed
_ImaGroupIntervalMoniSecs_Object = MibTableColumn
imaGroupIntervalMoniSecs = _ImaGroupIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 5),
    _ImaGroupIntervalMoniSecs_Type()
)
imaGroupIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIntervalMoniSecs.setStatus("current")
_ImaGroupCurrDayTable_Object = MibTable
imaGroupCurrDayTable = _ImaGroupCurrDayTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9)
)
if mibBuilder.loadTexts:
    imaGroupCurrDayTable.setStatus("current")
_ImaGroupCurrDayEntry_Object = MibTableRow
imaGroupCurrDayEntry = _ImaGroupCurrDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1)
)
imaGroupCurrDayEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    imaGroupCurrDayEntry.setStatus("current")
_ImaGroupCurrDayTimeElapsed_Type = ImaPerfTimeElapsed
_ImaGroupCurrDayTimeElapsed_Object = MibTableColumn
imaGroupCurrDayTimeElapsed = _ImaGroupCurrDayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1, 1),
    _ImaGroupCurrDayTimeElapsed_Type()
)
imaGroupCurrDayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrDayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    imaGroupCurrDayTimeElapsed.setUnits("seconds")
_ImaGroupCurrDayUnavailSecs_Type = ImaPerfCurrDayCount
_ImaGroupCurrDayUnavailSecs_Object = MibTableColumn
imaGroupCurrDayUnavailSecs = _ImaGroupCurrDayUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1, 2),
    _ImaGroupCurrDayUnavailSecs_Type()
)
imaGroupCurrDayUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrDayUnavailSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaGroupCurrDayUnavailSecs.setUnits("seconds")
_ImaGroupCurrDayNeNumFailures_Type = ImaPerfCurrDayCount
_ImaGroupCurrDayNeNumFailures_Object = MibTableColumn
imaGroupCurrDayNeNumFailures = _ImaGroupCurrDayNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1, 3),
    _ImaGroupCurrDayNeNumFailures_Type()
)
imaGroupCurrDayNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrDayNeNumFailures.setStatus("current")
_ImaGroupCurrDayFeNumFailures_Type = ImaPerfCurrDayCount
_ImaGroupCurrDayFeNumFailures_Object = MibTableColumn
imaGroupCurrDayFeNumFailures = _ImaGroupCurrDayFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1, 4),
    _ImaGroupCurrDayFeNumFailures_Type()
)
imaGroupCurrDayFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrDayFeNumFailures.setStatus("current")
_ImaGroup1DayIntervalTable_Object = MibTable
imaGroup1DayIntervalTable = _ImaGroup1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10)
)
if mibBuilder.loadTexts:
    imaGroup1DayIntervalTable.setStatus("current")
_ImaGroup1DayIntervalEntry_Object = MibTableRow
imaGroup1DayIntervalEntry = _ImaGroup1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1)
)
imaGroup1DayIntervalEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
    (0, "IMA-MIB", "imaGroup1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    imaGroup1DayIntervalEntry.setStatus("current")


class _ImaGroup1DayIntervalNumber_Type(Integer32):
    """Custom type imaGroup1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ImaGroup1DayIntervalNumber_Type.__name__ = "Integer32"
_ImaGroup1DayIntervalNumber_Object = MibTableColumn
imaGroup1DayIntervalNumber = _ImaGroup1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 1),
    _ImaGroup1DayIntervalNumber_Type()
)
imaGroup1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaGroup1DayIntervalNumber.setStatus("current")
_ImaGroup1DayIntervalMoniSecs_Type = ImaPerfTimeElapsed
_ImaGroup1DayIntervalMoniSecs_Object = MibTableColumn
imaGroup1DayIntervalMoniSecs = _ImaGroup1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 2),
    _ImaGroup1DayIntervalMoniSecs_Type()
)
imaGroup1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroup1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaGroup1DayIntervalMoniSecs.setUnits("seconds")
_ImaGroup1DayIntervalUnavailSecs_Type = ImaPerf1DayIntervalCount
_ImaGroup1DayIntervalUnavailSecs_Object = MibTableColumn
imaGroup1DayIntervalUnavailSecs = _ImaGroup1DayIntervalUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 3),
    _ImaGroup1DayIntervalUnavailSecs_Type()
)
imaGroup1DayIntervalUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroup1DayIntervalUnavailSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaGroup1DayIntervalUnavailSecs.setUnits("seconds")
_ImaGroup1DayIntervalNeNumFailures_Type = ImaPerf1DayIntervalCount
_ImaGroup1DayIntervalNeNumFailures_Object = MibTableColumn
imaGroup1DayIntervalNeNumFailures = _ImaGroup1DayIntervalNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 4),
    _ImaGroup1DayIntervalNeNumFailures_Type()
)
imaGroup1DayIntervalNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroup1DayIntervalNeNumFailures.setStatus("current")
_ImaGroup1DayIntervalFeNumFailures_Type = ImaPerf1DayIntervalCount
_ImaGroup1DayIntervalFeNumFailures_Object = MibTableColumn
imaGroup1DayIntervalFeNumFailures = _ImaGroup1DayIntervalFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 5),
    _ImaGroup1DayIntervalFeNumFailures_Type()
)
imaGroup1DayIntervalFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroup1DayIntervalFeNumFailures.setStatus("current")
_ImaGroupAlarmConfProfileTable_Object = MibTable
imaGroupAlarmConfProfileTable = _ImaGroupAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11)
)
if mibBuilder.loadTexts:
    imaGroupAlarmConfProfileTable.setStatus("current")
_ImaGroupAlarmConfProfileEntry_Object = MibTableRow
imaGroupAlarmConfProfileEntry = _ImaGroupAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1)
)
imaGroupAlarmConfProfileEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    imaGroupAlarmConfProfileEntry.setStatus("current")


class _ImaGroupAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type imaGroupAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ImaGroupAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_ImaGroupAlarmConfProfileName_Object = MibTableColumn
imaGroupAlarmConfProfileName = _ImaGroupAlarmConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 1),
    _ImaGroupAlarmConfProfileName_Type()
)
imaGroupAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaGroupAlarmConfProfileName.setStatus("current")


class _ImaGroupThreshUnavailSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaGroupThreshUnavailSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaGroupThreshUnavailSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaGroupThreshUnavailSecs_Object = MibTableColumn
imaGroupThreshUnavailSecs = _ImaGroupThreshUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 2),
    _ImaGroupThreshUnavailSecs_Type()
)
imaGroupThreshUnavailSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupThreshUnavailSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaGroupThreshUnavailSecs.setUnits("seconds")


class _ImaGroupThreshNeNumFailures_Type(Integer32):
    """Custom type imaGroupThreshNeNumFailures based on Integer32"""
    defaultValue = 0


_ImaGroupThreshNeNumFailures_Type.__name__ = "Integer32"
_ImaGroupThreshNeNumFailures_Object = MibTableColumn
imaGroupThreshNeNumFailures = _ImaGroupThreshNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 3),
    _ImaGroupThreshNeNumFailures_Type()
)
imaGroupThreshNeNumFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupThreshNeNumFailures.setStatus("current")


class _ImaGroupThreshFeNumFailures_Type(Integer32):
    """Custom type imaGroupThreshFeNumFailures based on Integer32"""
    defaultValue = 0


_ImaGroupThreshFeNumFailures_Type.__name__ = "Integer32"
_ImaGroupThreshFeNumFailures_Object = MibTableColumn
imaGroupThreshFeNumFailures = _ImaGroupThreshFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 4),
    _ImaGroupThreshFeNumFailures_Type()
)
imaGroupThreshFeNumFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupThreshFeNumFailures.setStatus("current")
_ImaGroupAlarmConfProfileRowStatus_Type = RowStatus
_ImaGroupAlarmConfProfileRowStatus_Object = MibTableColumn
imaGroupAlarmConfProfileRowStatus = _ImaGroupAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 5),
    _ImaGroupAlarmConfProfileRowStatus_Type()
)
imaGroupAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupAlarmConfProfileRowStatus.setStatus("current")
_ImaLinkCurrentTable_Object = MibTable
imaLinkCurrentTable = _ImaLinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12)
)
if mibBuilder.loadTexts:
    imaLinkCurrentTable.setStatus("current")
_ImaLinkCurrentEntry_Object = MibTableRow
imaLinkCurrentEntry = _ImaLinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1)
)
imaLinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    imaLinkCurrentEntry.setStatus("current")
_ImaLinkCurrentImaViolations_Type = PerfCurrentCount
_ImaLinkCurrentImaViolations_Object = MibTableColumn
imaLinkCurrentImaViolations = _ImaLinkCurrentImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 1),
    _ImaLinkCurrentImaViolations_Type()
)
imaLinkCurrentImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentImaViolations.setStatus("current")
_ImaLinkCurrentOifAnomalies_Type = PerfCurrentCount
_ImaLinkCurrentOifAnomalies_Object = MibTableColumn
imaLinkCurrentOifAnomalies = _ImaLinkCurrentOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 2),
    _ImaLinkCurrentOifAnomalies_Type()
)
imaLinkCurrentOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentOifAnomalies.setStatus("current")
_ImaLinkCurrentNeSevErroredSecs_Type = PerfCurrentCount
_ImaLinkCurrentNeSevErroredSecs_Object = MibTableColumn
imaLinkCurrentNeSevErroredSecs = _ImaLinkCurrentNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 3),
    _ImaLinkCurrentNeSevErroredSecs_Type()
)
imaLinkCurrentNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeSevErroredSecs.setStatus("current")
_ImaLinkCurrentFeSevErroredSecs_Type = PerfCurrentCount
_ImaLinkCurrentFeSevErroredSecs_Object = MibTableColumn
imaLinkCurrentFeSevErroredSecs = _ImaLinkCurrentFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 4),
    _ImaLinkCurrentFeSevErroredSecs_Type()
)
imaLinkCurrentFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeSevErroredSecs.setStatus("current")
_ImaLinkCurrentNeUnavailSecs_Type = PerfCurrentCount
_ImaLinkCurrentNeUnavailSecs_Object = MibTableColumn
imaLinkCurrentNeUnavailSecs = _ImaLinkCurrentNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 5),
    _ImaLinkCurrentNeUnavailSecs_Type()
)
imaLinkCurrentNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeUnavailSecs.setStatus("current")
_ImaLinkCurrentFeUnavailSecs_Type = PerfCurrentCount
_ImaLinkCurrentFeUnavailSecs_Object = MibTableColumn
imaLinkCurrentFeUnavailSecs = _ImaLinkCurrentFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 6),
    _ImaLinkCurrentFeUnavailSecs_Type()
)
imaLinkCurrentFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeUnavailSecs.setStatus("current")
_ImaLinkCurrentNeTxUnusableSecs_Type = PerfCurrentCount
_ImaLinkCurrentNeTxUnusableSecs_Object = MibTableColumn
imaLinkCurrentNeTxUnusableSecs = _ImaLinkCurrentNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 7),
    _ImaLinkCurrentNeTxUnusableSecs_Type()
)
imaLinkCurrentNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeTxUnusableSecs.setStatus("current")
_ImaLinkCurrentNeRxUnusableSecs_Type = PerfCurrentCount
_ImaLinkCurrentNeRxUnusableSecs_Object = MibTableColumn
imaLinkCurrentNeRxUnusableSecs = _ImaLinkCurrentNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 8),
    _ImaLinkCurrentNeRxUnusableSecs_Type()
)
imaLinkCurrentNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeRxUnusableSecs.setStatus("current")
_ImaLinkCurrentFeTxUnusableSecs_Type = PerfCurrentCount
_ImaLinkCurrentFeTxUnusableSecs_Object = MibTableColumn
imaLinkCurrentFeTxUnusableSecs = _ImaLinkCurrentFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 9),
    _ImaLinkCurrentFeTxUnusableSecs_Type()
)
imaLinkCurrentFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeTxUnusableSecs.setStatus("current")
_ImaLinkCurrentFeRxUnusableSecs_Type = PerfCurrentCount
_ImaLinkCurrentFeRxUnusableSecs_Object = MibTableColumn
imaLinkCurrentFeRxUnusableSecs = _ImaLinkCurrentFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 10),
    _ImaLinkCurrentFeRxUnusableSecs_Type()
)
imaLinkCurrentFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeRxUnusableSecs.setStatus("current")
_ImaLinkCurrentNeTxNumFailures_Type = PerfCurrentCount
_ImaLinkCurrentNeTxNumFailures_Object = MibTableColumn
imaLinkCurrentNeTxNumFailures = _ImaLinkCurrentNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 11),
    _ImaLinkCurrentNeTxNumFailures_Type()
)
imaLinkCurrentNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeTxNumFailures.setStatus("current")
_ImaLinkCurrentNeRxNumFailures_Type = PerfCurrentCount
_ImaLinkCurrentNeRxNumFailures_Object = MibTableColumn
imaLinkCurrentNeRxNumFailures = _ImaLinkCurrentNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 12),
    _ImaLinkCurrentNeRxNumFailures_Type()
)
imaLinkCurrentNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeRxNumFailures.setStatus("current")
_ImaLinkCurrentFeTxNumFailures_Type = PerfCurrentCount
_ImaLinkCurrentFeTxNumFailures_Object = MibTableColumn
imaLinkCurrentFeTxNumFailures = _ImaLinkCurrentFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 13),
    _ImaLinkCurrentFeTxNumFailures_Type()
)
imaLinkCurrentFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeTxNumFailures.setStatus("current")
_ImaLinkCurrentFeRxNumFailures_Type = PerfCurrentCount
_ImaLinkCurrentFeRxNumFailures_Object = MibTableColumn
imaLinkCurrentFeRxNumFailures = _ImaLinkCurrentFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 14),
    _ImaLinkCurrentFeRxNumFailures_Type()
)
imaLinkCurrentFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeRxNumFailures.setStatus("current")
_ImaLinkCurrentTxStuffs_Type = PerfCurrentCount
_ImaLinkCurrentTxStuffs_Object = MibTableColumn
imaLinkCurrentTxStuffs = _ImaLinkCurrentTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 15),
    _ImaLinkCurrentTxStuffs_Type()
)
imaLinkCurrentTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentTxStuffs.setStatus("current")
_ImaLinkCurrentRxStuffs_Type = PerfCurrentCount
_ImaLinkCurrentRxStuffs_Object = MibTableColumn
imaLinkCurrentRxStuffs = _ImaLinkCurrentRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 16),
    _ImaLinkCurrentRxStuffs_Type()
)
imaLinkCurrentRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentRxStuffs.setStatus("current")
_ImaLinkIntervalTable_Object = MibTable
imaLinkIntervalTable = _ImaLinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13)
)
if mibBuilder.loadTexts:
    imaLinkIntervalTable.setStatus("current")
_ImaLinkIntervalEntry_Object = MibTableRow
imaLinkIntervalEntry = _ImaLinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1)
)
imaLinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IMA-MIB", "imaLinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    imaLinkIntervalEntry.setStatus("current")


class _ImaLinkIntervalNumber_Type(Integer32):
    """Custom type imaLinkIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ImaLinkIntervalNumber_Type.__name__ = "Integer32"
_ImaLinkIntervalNumber_Object = MibTableColumn
imaLinkIntervalNumber = _ImaLinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 1),
    _ImaLinkIntervalNumber_Type()
)
imaLinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaLinkIntervalNumber.setStatus("current")
_ImaLinkIntervalImaViolations_Type = PerfIntervalCount
_ImaLinkIntervalImaViolations_Object = MibTableColumn
imaLinkIntervalImaViolations = _ImaLinkIntervalImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 2),
    _ImaLinkIntervalImaViolations_Type()
)
imaLinkIntervalImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalImaViolations.setStatus("current")
_ImaLinkIntervalOifAnomalies_Type = PerfIntervalCount
_ImaLinkIntervalOifAnomalies_Object = MibTableColumn
imaLinkIntervalOifAnomalies = _ImaLinkIntervalOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 3),
    _ImaLinkIntervalOifAnomalies_Type()
)
imaLinkIntervalOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalOifAnomalies.setStatus("current")
_ImaLinkIntervalNeSevErroredSecs_Type = PerfIntervalCount
_ImaLinkIntervalNeSevErroredSecs_Object = MibTableColumn
imaLinkIntervalNeSevErroredSecs = _ImaLinkIntervalNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 4),
    _ImaLinkIntervalNeSevErroredSecs_Type()
)
imaLinkIntervalNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeSevErroredSecs.setStatus("current")
_ImaLinkIntervalFeSevErroredSecs_Type = PerfIntervalCount
_ImaLinkIntervalFeSevErroredSecs_Object = MibTableColumn
imaLinkIntervalFeSevErroredSecs = _ImaLinkIntervalFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 5),
    _ImaLinkIntervalFeSevErroredSecs_Type()
)
imaLinkIntervalFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeSevErroredSecs.setStatus("current")
_ImaLinkIntervalNeUnavailSecs_Type = PerfIntervalCount
_ImaLinkIntervalNeUnavailSecs_Object = MibTableColumn
imaLinkIntervalNeUnavailSecs = _ImaLinkIntervalNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 6),
    _ImaLinkIntervalNeUnavailSecs_Type()
)
imaLinkIntervalNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeUnavailSecs.setStatus("current")
_ImaLinkIntervalFeUnavailSecs_Type = PerfIntervalCount
_ImaLinkIntervalFeUnavailSecs_Object = MibTableColumn
imaLinkIntervalFeUnavailSecs = _ImaLinkIntervalFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 7),
    _ImaLinkIntervalFeUnavailSecs_Type()
)
imaLinkIntervalFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeUnavailSecs.setStatus("current")
_ImaLinkIntervalNeTxUnusableSecs_Type = PerfIntervalCount
_ImaLinkIntervalNeTxUnusableSecs_Object = MibTableColumn
imaLinkIntervalNeTxUnusableSecs = _ImaLinkIntervalNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 8),
    _ImaLinkIntervalNeTxUnusableSecs_Type()
)
imaLinkIntervalNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeTxUnusableSecs.setStatus("current")
_ImaLinkIntervalNeRxUnusableSecs_Type = PerfIntervalCount
_ImaLinkIntervalNeRxUnusableSecs_Object = MibTableColumn
imaLinkIntervalNeRxUnusableSecs = _ImaLinkIntervalNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 9),
    _ImaLinkIntervalNeRxUnusableSecs_Type()
)
imaLinkIntervalNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeRxUnusableSecs.setStatus("current")
_ImaLinkIntervalFeTxUnusableSecs_Type = PerfIntervalCount
_ImaLinkIntervalFeTxUnusableSecs_Object = MibTableColumn
imaLinkIntervalFeTxUnusableSecs = _ImaLinkIntervalFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 10),
    _ImaLinkIntervalFeTxUnusableSecs_Type()
)
imaLinkIntervalFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeTxUnusableSecs.setStatus("current")
_ImaLinkIntervalFeRxUnusableSecs_Type = PerfIntervalCount
_ImaLinkIntervalFeRxUnusableSecs_Object = MibTableColumn
imaLinkIntervalFeRxUnusableSecs = _ImaLinkIntervalFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 11),
    _ImaLinkIntervalFeRxUnusableSecs_Type()
)
imaLinkIntervalFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeRxUnusableSecs.setStatus("current")
_ImaLinkIntervalNeTxNumFailures_Type = PerfIntervalCount
_ImaLinkIntervalNeTxNumFailures_Object = MibTableColumn
imaLinkIntervalNeTxNumFailures = _ImaLinkIntervalNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 12),
    _ImaLinkIntervalNeTxNumFailures_Type()
)
imaLinkIntervalNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeTxNumFailures.setStatus("current")
_ImaLinkIntervalNeRxNumFailures_Type = PerfIntervalCount
_ImaLinkIntervalNeRxNumFailures_Object = MibTableColumn
imaLinkIntervalNeRxNumFailures = _ImaLinkIntervalNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 13),
    _ImaLinkIntervalNeRxNumFailures_Type()
)
imaLinkIntervalNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeRxNumFailures.setStatus("current")
_ImaLinkIntervalFeTxNumFailures_Type = PerfIntervalCount
_ImaLinkIntervalFeTxNumFailures_Object = MibTableColumn
imaLinkIntervalFeTxNumFailures = _ImaLinkIntervalFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 14),
    _ImaLinkIntervalFeTxNumFailures_Type()
)
imaLinkIntervalFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeTxNumFailures.setStatus("current")
_ImaLinkIntervalFeRxNumFailures_Type = PerfIntervalCount
_ImaLinkIntervalFeRxNumFailures_Object = MibTableColumn
imaLinkIntervalFeRxNumFailures = _ImaLinkIntervalFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 15),
    _ImaLinkIntervalFeRxNumFailures_Type()
)
imaLinkIntervalFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeRxNumFailures.setStatus("current")
_ImaLinkIntervalTxStuffs_Type = PerfIntervalCount
_ImaLinkIntervalTxStuffs_Object = MibTableColumn
imaLinkIntervalTxStuffs = _ImaLinkIntervalTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 16),
    _ImaLinkIntervalTxStuffs_Type()
)
imaLinkIntervalTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalTxStuffs.setStatus("current")
_ImaLinkIntervalRxStuffs_Type = PerfIntervalCount
_ImaLinkIntervalRxStuffs_Object = MibTableColumn
imaLinkIntervalRxStuffs = _ImaLinkIntervalRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 17),
    _ImaLinkIntervalRxStuffs_Type()
)
imaLinkIntervalRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalRxStuffs.setStatus("current")
_ImaLinkIntervalMoniSecs_Type = ImaPerfTimeElapsed
_ImaLinkIntervalMoniSecs_Object = MibTableColumn
imaLinkIntervalMoniSecs = _ImaLinkIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 13, 1, 18),
    _ImaLinkIntervalMoniSecs_Type()
)
imaLinkIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalMoniSecs.setStatus("current")
_ImaLinkCurrDayTable_Object = MibTable
imaLinkCurrDayTable = _ImaLinkCurrDayTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14)
)
if mibBuilder.loadTexts:
    imaLinkCurrDayTable.setStatus("current")
_ImaLinkCurrDayEntry_Object = MibTableRow
imaLinkCurrDayEntry = _ImaLinkCurrDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1)
)
imaLinkCurrDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    imaLinkCurrDayEntry.setStatus("current")
_ImaLinkCurrDayTimeElapsed_Type = ImaPerfTimeElapsed
_ImaLinkCurrDayTimeElapsed_Object = MibTableColumn
imaLinkCurrDayTimeElapsed = _ImaLinkCurrDayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 1),
    _ImaLinkCurrDayTimeElapsed_Type()
)
imaLinkCurrDayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayTimeElapsed.setStatus("current")
_ImaLinkCurrDayImaViolations_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayImaViolations_Object = MibTableColumn
imaLinkCurrDayImaViolations = _ImaLinkCurrDayImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 2),
    _ImaLinkCurrDayImaViolations_Type()
)
imaLinkCurrDayImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayImaViolations.setStatus("current")
_ImaLinkCurrDayOifAnomalies_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayOifAnomalies_Object = MibTableColumn
imaLinkCurrDayOifAnomalies = _ImaLinkCurrDayOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 3),
    _ImaLinkCurrDayOifAnomalies_Type()
)
imaLinkCurrDayOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayOifAnomalies.setStatus("current")
_ImaLinkCurrDayNeSevErroredSecs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayNeSevErroredSecs_Object = MibTableColumn
imaLinkCurrDayNeSevErroredSecs = _ImaLinkCurrDayNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 4),
    _ImaLinkCurrDayNeSevErroredSecs_Type()
)
imaLinkCurrDayNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayNeSevErroredSecs.setStatus("current")
_ImaLinkCurrDayFeSevErroredSecs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayFeSevErroredSecs_Object = MibTableColumn
imaLinkCurrDayFeSevErroredSecs = _ImaLinkCurrDayFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 5),
    _ImaLinkCurrDayFeSevErroredSecs_Type()
)
imaLinkCurrDayFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayFeSevErroredSecs.setStatus("current")
_ImaLinkCurrDayNeUnavailSecs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayNeUnavailSecs_Object = MibTableColumn
imaLinkCurrDayNeUnavailSecs = _ImaLinkCurrDayNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 6),
    _ImaLinkCurrDayNeUnavailSecs_Type()
)
imaLinkCurrDayNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayNeUnavailSecs.setStatus("current")
_ImaLinkCurrDayFeUnavailSecs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayFeUnavailSecs_Object = MibTableColumn
imaLinkCurrDayFeUnavailSecs = _ImaLinkCurrDayFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 7),
    _ImaLinkCurrDayFeUnavailSecs_Type()
)
imaLinkCurrDayFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayFeUnavailSecs.setStatus("current")
_ImaLinkCurrDayNeTxUnusableSecs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayNeTxUnusableSecs_Object = MibTableColumn
imaLinkCurrDayNeTxUnusableSecs = _ImaLinkCurrDayNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 8),
    _ImaLinkCurrDayNeTxUnusableSecs_Type()
)
imaLinkCurrDayNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayNeTxUnusableSecs.setStatus("current")
_ImaLinkCurrDayNeRxUnusableSecs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayNeRxUnusableSecs_Object = MibTableColumn
imaLinkCurrDayNeRxUnusableSecs = _ImaLinkCurrDayNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 9),
    _ImaLinkCurrDayNeRxUnusableSecs_Type()
)
imaLinkCurrDayNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayNeRxUnusableSecs.setStatus("current")
_ImaLinkCurrDayFeTxUnusableSecs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayFeTxUnusableSecs_Object = MibTableColumn
imaLinkCurrDayFeTxUnusableSecs = _ImaLinkCurrDayFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 10),
    _ImaLinkCurrDayFeTxUnusableSecs_Type()
)
imaLinkCurrDayFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayFeTxUnusableSecs.setStatus("current")
_ImaLinkCurrDayFeRxUnusableSecs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayFeRxUnusableSecs_Object = MibTableColumn
imaLinkCurrDayFeRxUnusableSecs = _ImaLinkCurrDayFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 11),
    _ImaLinkCurrDayFeRxUnusableSecs_Type()
)
imaLinkCurrDayFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayFeRxUnusableSecs.setStatus("current")
_ImaLinkCurrDayNeTxNumFailures_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayNeTxNumFailures_Object = MibTableColumn
imaLinkCurrDayNeTxNumFailures = _ImaLinkCurrDayNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 12),
    _ImaLinkCurrDayNeTxNumFailures_Type()
)
imaLinkCurrDayNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayNeTxNumFailures.setStatus("current")
_ImaLinkCurrDayNeRxNumFailures_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayNeRxNumFailures_Object = MibTableColumn
imaLinkCurrDayNeRxNumFailures = _ImaLinkCurrDayNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 13),
    _ImaLinkCurrDayNeRxNumFailures_Type()
)
imaLinkCurrDayNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayNeRxNumFailures.setStatus("current")
_ImaLinkCurrDayFeTxNumFailures_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayFeTxNumFailures_Object = MibTableColumn
imaLinkCurrDayFeTxNumFailures = _ImaLinkCurrDayFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 14),
    _ImaLinkCurrDayFeTxNumFailures_Type()
)
imaLinkCurrDayFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayFeTxNumFailures.setStatus("current")
_ImaLinkCurrDayFeRxNumFailures_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayFeRxNumFailures_Object = MibTableColumn
imaLinkCurrDayFeRxNumFailures = _ImaLinkCurrDayFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 15),
    _ImaLinkCurrDayFeRxNumFailures_Type()
)
imaLinkCurrDayFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayFeRxNumFailures.setStatus("current")
_ImaLinkCurrDayTxStuffs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayTxStuffs_Object = MibTableColumn
imaLinkCurrDayTxStuffs = _ImaLinkCurrDayTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 16),
    _ImaLinkCurrDayTxStuffs_Type()
)
imaLinkCurrDayTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayTxStuffs.setStatus("current")
_ImaLinkCurrDayRxStuffs_Type = ImaPerfCurrDayCount
_ImaLinkCurrDayRxStuffs_Object = MibTableColumn
imaLinkCurrDayRxStuffs = _ImaLinkCurrDayRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 14, 1, 17),
    _ImaLinkCurrDayRxStuffs_Type()
)
imaLinkCurrDayRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrDayRxStuffs.setStatus("current")
_ImaLink1DayIntervalTable_Object = MibTable
imaLink1DayIntervalTable = _ImaLink1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15)
)
if mibBuilder.loadTexts:
    imaLink1DayIntervalTable.setStatus("current")
_ImaLink1DayIntervalEntry_Object = MibTableRow
imaLink1DayIntervalEntry = _ImaLink1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1)
)
imaLink1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IMA-MIB", "imaLink1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    imaLink1DayIntervalEntry.setStatus("current")


class _ImaLink1DayIntervalNumber_Type(Integer32):
    """Custom type imaLink1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ImaLink1DayIntervalNumber_Type.__name__ = "Integer32"
_ImaLink1DayIntervalNumber_Object = MibTableColumn
imaLink1DayIntervalNumber = _ImaLink1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 1),
    _ImaLink1DayIntervalNumber_Type()
)
imaLink1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaLink1DayIntervalNumber.setStatus("current")
_ImaLink1DayIntervalMoniSecs_Type = ImaPerfTimeElapsed
_ImaLink1DayIntervalMoniSecs_Object = MibTableColumn
imaLink1DayIntervalMoniSecs = _ImaLink1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 2),
    _ImaLink1DayIntervalMoniSecs_Type()
)
imaLink1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLink1DayIntervalMoniSecs.setUnits("seconds")
_ImaLink1DayIntervalImaViolations_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalImaViolations_Object = MibTableColumn
imaLink1DayIntervalImaViolations = _ImaLink1DayIntervalImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 3),
    _ImaLink1DayIntervalImaViolations_Type()
)
imaLink1DayIntervalImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalImaViolations.setStatus("current")
_ImaLink1DayIntervalOifAnomalies_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalOifAnomalies_Object = MibTableColumn
imaLink1DayIntervalOifAnomalies = _ImaLink1DayIntervalOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 5),
    _ImaLink1DayIntervalOifAnomalies_Type()
)
imaLink1DayIntervalOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalOifAnomalies.setStatus("current")
_ImaLink1DayIntervalNeSevErroredSecs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalNeSevErroredSecs_Object = MibTableColumn
imaLink1DayIntervalNeSevErroredSecs = _ImaLink1DayIntervalNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 6),
    _ImaLink1DayIntervalNeSevErroredSecs_Type()
)
imaLink1DayIntervalNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalNeSevErroredSecs.setStatus("current")
_ImaLink1DayIntervalFeSevErroredSecs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalFeSevErroredSecs_Object = MibTableColumn
imaLink1DayIntervalFeSevErroredSecs = _ImaLink1DayIntervalFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 7),
    _ImaLink1DayIntervalFeSevErroredSecs_Type()
)
imaLink1DayIntervalFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalFeSevErroredSecs.setStatus("current")
_ImaLink1DayIntervalNeUnavailSecs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalNeUnavailSecs_Object = MibTableColumn
imaLink1DayIntervalNeUnavailSecs = _ImaLink1DayIntervalNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 8),
    _ImaLink1DayIntervalNeUnavailSecs_Type()
)
imaLink1DayIntervalNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalNeUnavailSecs.setStatus("current")
_ImaLink1DayIntervalFeUnavailSecs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalFeUnavailSecs_Object = MibTableColumn
imaLink1DayIntervalFeUnavailSecs = _ImaLink1DayIntervalFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 9),
    _ImaLink1DayIntervalFeUnavailSecs_Type()
)
imaLink1DayIntervalFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalFeUnavailSecs.setStatus("current")
_ImaLink1DayIntervalNeTxUnusableSecs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalNeTxUnusableSecs_Object = MibTableColumn
imaLink1DayIntervalNeTxUnusableSecs = _ImaLink1DayIntervalNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 10),
    _ImaLink1DayIntervalNeTxUnusableSecs_Type()
)
imaLink1DayIntervalNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalNeTxUnusableSecs.setStatus("current")
_ImaLink1DayIntervalNeRxUnusableSecs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalNeRxUnusableSecs_Object = MibTableColumn
imaLink1DayIntervalNeRxUnusableSecs = _ImaLink1DayIntervalNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 11),
    _ImaLink1DayIntervalNeRxUnusableSecs_Type()
)
imaLink1DayIntervalNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalNeRxUnusableSecs.setStatus("current")
_ImaLink1DayIntervalFeTxUnusableSecs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalFeTxUnusableSecs_Object = MibTableColumn
imaLink1DayIntervalFeTxUnusableSecs = _ImaLink1DayIntervalFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 12),
    _ImaLink1DayIntervalFeTxUnusableSecs_Type()
)
imaLink1DayIntervalFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalFeTxUnusableSecs.setStatus("current")
_ImaLink1DayIntervalFeRxUnusableSecs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalFeRxUnusableSecs_Object = MibTableColumn
imaLink1DayIntervalFeRxUnusableSecs = _ImaLink1DayIntervalFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 13),
    _ImaLink1DayIntervalFeRxUnusableSecs_Type()
)
imaLink1DayIntervalFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalFeRxUnusableSecs.setStatus("current")
_ImaLink1DayIntervalNeTxNumFailures_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalNeTxNumFailures_Object = MibTableColumn
imaLink1DayIntervalNeTxNumFailures = _ImaLink1DayIntervalNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 14),
    _ImaLink1DayIntervalNeTxNumFailures_Type()
)
imaLink1DayIntervalNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalNeTxNumFailures.setStatus("current")
_ImaLink1DayIntervalNeRxNumFailures_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalNeRxNumFailures_Object = MibTableColumn
imaLink1DayIntervalNeRxNumFailures = _ImaLink1DayIntervalNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 15),
    _ImaLink1DayIntervalNeRxNumFailures_Type()
)
imaLink1DayIntervalNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalNeRxNumFailures.setStatus("current")
_ImaLink1DayIntervalFeTxNumFailures_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalFeTxNumFailures_Object = MibTableColumn
imaLink1DayIntervalFeTxNumFailures = _ImaLink1DayIntervalFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 16),
    _ImaLink1DayIntervalFeTxNumFailures_Type()
)
imaLink1DayIntervalFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalFeTxNumFailures.setStatus("current")
_ImaLink1DayIntervalFeRxNumFailures_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalFeRxNumFailures_Object = MibTableColumn
imaLink1DayIntervalFeRxNumFailures = _ImaLink1DayIntervalFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 17),
    _ImaLink1DayIntervalFeRxNumFailures_Type()
)
imaLink1DayIntervalFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalFeRxNumFailures.setStatus("current")
_ImaLink1DayIntervalTxStuffs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalTxStuffs_Object = MibTableColumn
imaLink1DayIntervalTxStuffs = _ImaLink1DayIntervalTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 18),
    _ImaLink1DayIntervalTxStuffs_Type()
)
imaLink1DayIntervalTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalTxStuffs.setStatus("current")
_ImaLink1DayIntervalRxStuffs_Type = ImaPerf1DayIntervalCount
_ImaLink1DayIntervalRxStuffs_Object = MibTableColumn
imaLink1DayIntervalRxStuffs = _ImaLink1DayIntervalRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 15, 1, 19),
    _ImaLink1DayIntervalRxStuffs_Type()
)
imaLink1DayIntervalRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLink1DayIntervalRxStuffs.setStatus("current")
_ImaLinkAlarmConfProfileTable_Object = MibTable
imaLinkAlarmConfProfileTable = _ImaLinkAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16)
)
if mibBuilder.loadTexts:
    imaLinkAlarmConfProfileTable.setStatus("current")
_ImaLinkAlarmConfProfileEntry_Object = MibTableRow
imaLinkAlarmConfProfileEntry = _ImaLinkAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1)
)
imaLinkAlarmConfProfileEntry.setIndexNames(
    (0, "IMA-MIB", "imaLinkAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    imaLinkAlarmConfProfileEntry.setStatus("current")


class _ImaLinkAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type imaLinkAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ImaLinkAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_ImaLinkAlarmConfProfileName_Object = MibTableColumn
imaLinkAlarmConfProfileName = _ImaLinkAlarmConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 1),
    _ImaLinkAlarmConfProfileName_Type()
)
imaLinkAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaLinkAlarmConfProfileName.setStatus("current")


class _ImaLinkThreshImaViolations_Type(Integer32):
    """Custom type imaLinkThreshImaViolations based on Integer32"""
    defaultValue = 0


_ImaLinkThreshImaViolations_Type.__name__ = "Integer32"
_ImaLinkThreshImaViolations_Object = MibTableColumn
imaLinkThreshImaViolations = _ImaLinkThreshImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 2),
    _ImaLinkThreshImaViolations_Type()
)
imaLinkThreshImaViolations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshImaViolations.setStatus("current")


class _ImaLinkThreshOifAnomalies_Type(Integer32):
    """Custom type imaLinkThreshOifAnomalies based on Integer32"""
    defaultValue = 0


_ImaLinkThreshOifAnomalies_Type.__name__ = "Integer32"
_ImaLinkThreshOifAnomalies_Object = MibTableColumn
imaLinkThreshOifAnomalies = _ImaLinkThreshOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 3),
    _ImaLinkThreshOifAnomalies_Type()
)
imaLinkThreshOifAnomalies.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshOifAnomalies.setStatus("current")


class _ImaLinkThreshNeSevErroredSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaLinkThreshNeSevErroredSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaLinkThreshNeSevErroredSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaLinkThreshNeSevErroredSecs_Object = MibTableColumn
imaLinkThreshNeSevErroredSecs = _ImaLinkThreshNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 4),
    _ImaLinkThreshNeSevErroredSecs_Type()
)
imaLinkThreshNeSevErroredSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshNeSevErroredSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLinkThreshNeSevErroredSecs.setUnits("seconds")


class _ImaLinkThreshFeSevErroredSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaLinkThreshFeSevErroredSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaLinkThreshFeSevErroredSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaLinkThreshFeSevErroredSecs_Object = MibTableColumn
imaLinkThreshFeSevErroredSecs = _ImaLinkThreshFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 5),
    _ImaLinkThreshFeSevErroredSecs_Type()
)
imaLinkThreshFeSevErroredSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshFeSevErroredSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLinkThreshFeSevErroredSecs.setUnits("seconds")


class _ImaLinkThreshNeUnavailSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaLinkThreshNeUnavailSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaLinkThreshNeUnavailSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaLinkThreshNeUnavailSecs_Object = MibTableColumn
imaLinkThreshNeUnavailSecs = _ImaLinkThreshNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 6),
    _ImaLinkThreshNeUnavailSecs_Type()
)
imaLinkThreshNeUnavailSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshNeUnavailSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLinkThreshNeUnavailSecs.setUnits("seconds")


class _ImaLinkThreshFeUnavailSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaLinkThreshFeUnavailSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaLinkThreshFeUnavailSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaLinkThreshFeUnavailSecs_Object = MibTableColumn
imaLinkThreshFeUnavailSecs = _ImaLinkThreshFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 7),
    _ImaLinkThreshFeUnavailSecs_Type()
)
imaLinkThreshFeUnavailSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshFeUnavailSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLinkThreshFeUnavailSecs.setUnits("seconds")


class _ImaLinkThreshNeTxUnusableSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaLinkThreshNeTxUnusableSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaLinkThreshNeTxUnusableSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaLinkThreshNeTxUnusableSecs_Object = MibTableColumn
imaLinkThreshNeTxUnusableSecs = _ImaLinkThreshNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 8),
    _ImaLinkThreshNeTxUnusableSecs_Type()
)
imaLinkThreshNeTxUnusableSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshNeTxUnusableSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLinkThreshNeTxUnusableSecs.setUnits("seconds")


class _ImaLinkThreshNeRxUnusableSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaLinkThreshNeRxUnusableSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaLinkThreshNeRxUnusableSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaLinkThreshNeRxUnusableSecs_Object = MibTableColumn
imaLinkThreshNeRxUnusableSecs = _ImaLinkThreshNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 9),
    _ImaLinkThreshNeRxUnusableSecs_Type()
)
imaLinkThreshNeRxUnusableSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshNeRxUnusableSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLinkThreshNeRxUnusableSecs.setUnits("seconds")


class _ImaLinkThreshFeTxUnusableSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaLinkThreshFeTxUnusableSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaLinkThreshFeTxUnusableSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaLinkThreshFeTxUnusableSecs_Object = MibTableColumn
imaLinkThreshFeTxUnusableSecs = _ImaLinkThreshFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 10),
    _ImaLinkThreshFeTxUnusableSecs_Type()
)
imaLinkThreshFeTxUnusableSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshFeTxUnusableSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLinkThreshFeTxUnusableSecs.setUnits("seconds")


class _ImaLinkThreshFeRxUnusableSecs_Type(ImaPerfIntervalThreshold):
    """Custom type imaLinkThreshFeRxUnusableSecs based on ImaPerfIntervalThreshold"""
    defaultValue = 0


_ImaLinkThreshFeRxUnusableSecs_Type.__name__ = "ImaPerfIntervalThreshold"
_ImaLinkThreshFeRxUnusableSecs_Object = MibTableColumn
imaLinkThreshFeRxUnusableSecs = _ImaLinkThreshFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 11),
    _ImaLinkThreshFeRxUnusableSecs_Type()
)
imaLinkThreshFeRxUnusableSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshFeRxUnusableSecs.setStatus("current")
if mibBuilder.loadTexts:
    imaLinkThreshFeRxUnusableSecs.setUnits("seconds")


class _ImaLinkThreshNeTxNumFailures_Type(Integer32):
    """Custom type imaLinkThreshNeTxNumFailures based on Integer32"""
    defaultValue = 0


_ImaLinkThreshNeTxNumFailures_Type.__name__ = "Integer32"
_ImaLinkThreshNeTxNumFailures_Object = MibTableColumn
imaLinkThreshNeTxNumFailures = _ImaLinkThreshNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 12),
    _ImaLinkThreshNeTxNumFailures_Type()
)
imaLinkThreshNeTxNumFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshNeTxNumFailures.setStatus("current")


class _ImaLinkThreshNeRxNumFailures_Type(Integer32):
    """Custom type imaLinkThreshNeRxNumFailures based on Integer32"""
    defaultValue = 0


_ImaLinkThreshNeRxNumFailures_Type.__name__ = "Integer32"
_ImaLinkThreshNeRxNumFailures_Object = MibTableColumn
imaLinkThreshNeRxNumFailures = _ImaLinkThreshNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 13),
    _ImaLinkThreshNeRxNumFailures_Type()
)
imaLinkThreshNeRxNumFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshNeRxNumFailures.setStatus("current")


class _ImaLinkThreshFeTxNumFailures_Type(Integer32):
    """Custom type imaLinkThreshFeTxNumFailures based on Integer32"""
    defaultValue = 0


_ImaLinkThreshFeTxNumFailures_Type.__name__ = "Integer32"
_ImaLinkThreshFeTxNumFailures_Object = MibTableColumn
imaLinkThreshFeTxNumFailures = _ImaLinkThreshFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 14),
    _ImaLinkThreshFeTxNumFailures_Type()
)
imaLinkThreshFeTxNumFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshFeTxNumFailures.setStatus("current")


class _ImaLinkThreshFeRxNumFailures_Type(Integer32):
    """Custom type imaLinkThreshFeRxNumFailures based on Integer32"""
    defaultValue = 0


_ImaLinkThreshFeRxNumFailures_Type.__name__ = "Integer32"
_ImaLinkThreshFeRxNumFailures_Object = MibTableColumn
imaLinkThreshFeRxNumFailures = _ImaLinkThreshFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 15),
    _ImaLinkThreshFeRxNumFailures_Type()
)
imaLinkThreshFeRxNumFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkThreshFeRxNumFailures.setStatus("current")
_ImaLinkAlarmConfProfileRowStatus_Type = RowStatus
_ImaLinkAlarmConfProfileRowStatus_Object = MibTableColumn
imaLinkAlarmConfProfileRowStatus = _ImaLinkAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 16, 1, 16),
    _ImaLinkAlarmConfProfileRowStatus_Type()
)
imaLinkAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkAlarmConfProfileRowStatus.setStatus("current")
_ImaMibTraps_ObjectIdentity = ObjectIdentity
imaMibTraps = _ImaMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2)
)
_ImaMibTrapPrefix_ObjectIdentity = ObjectIdentity
imaMibTrapPrefix = _ImaMibTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0)
)
_ImaMibConformance_ObjectIdentity = ObjectIdentity
imaMibConformance = _ImaMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3)
)
_ImaMibGroups_ObjectIdentity = ObjectIdentity
imaMibGroups = _ImaMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1)
)
_ImaMibCompliances_ObjectIdentity = ObjectIdentity
imaMibCompliances = _ImaMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 2)
)

# Managed Objects groups

imaGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 1)
)
imaGroupGroup.setObjects(
      *(("IMA-MIB", "imaGroupRowStatus"),
        ("IMA-MIB", "imaGroupIfIndex"),
        ("IMA-MIB", "imaGroupNeState"),
        ("IMA-MIB", "imaGroupFeState"),
        ("IMA-MIB", "imaGroupFailureStatus"),
        ("IMA-MIB", "imaGroupSymmetry"),
        ("IMA-MIB", "imaGroupMinNumTxLinks"),
        ("IMA-MIB", "imaGroupMinNumRxLinks"),
        ("IMA-MIB", "imaGroupNeTxClkMode"),
        ("IMA-MIB", "imaGroupFeTxClkMode"),
        ("IMA-MIB", "imaGroupTxTimingRefLink"),
        ("IMA-MIB", "imaGroupRxTimingRefLink"),
        ("IMA-MIB", "imaGroupLastChange"),
        ("IMA-MIB", "imaGroupTxImaId"),
        ("IMA-MIB", "imaGroupRxImaId"),
        ("IMA-MIB", "imaGroupTxFrameLength"),
        ("IMA-MIB", "imaGroupRxFrameLength"),
        ("IMA-MIB", "imaGroupDiffDelayMax"),
        ("IMA-MIB", "imaGroupLeastDelayLink"),
        ("IMA-MIB", "imaGroupDiffDelayMaxObs"),
        ("IMA-MIB", "imaGroupAlphaValue"),
        ("IMA-MIB", "imaGroupBetaValue"),
        ("IMA-MIB", "imaGroupGammaValue"),
        ("IMA-MIB", "imaGroupRunningSecs"),
        ("IMA-MIB", "imaGroupUnavailSecs"),
        ("IMA-MIB", "imaGroupNeNumFailures"),
        ("IMA-MIB", "imaGroupFeNumFailures"),
        ("IMA-MIB", "imaGroupTxAvailCellRate"),
        ("IMA-MIB", "imaGroupRxAvailCellRate"),
        ("IMA-MIB", "imaGroupNumTxCfgLinks"),
        ("IMA-MIB", "imaGroupNumRxCfgLinks"),
        ("IMA-MIB", "imaGroupNumTxActLinks"),
        ("IMA-MIB", "imaGroupNumRxActLinks"),
        ("IMA-MIB", "imaGroupTxOamLabelValue"),
        ("IMA-MIB", "imaGroupRxOamLabelValue"),
        ("IMA-MIB", "imaGroupConfAlarmProfile"))
)
if mibBuilder.loadTexts:
    imaGroupGroup.setStatus("current")

imaLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 2)
)
imaLinkGroup.setObjects(
      *(("IMA-MIB", "imaLinkRowStatus"),
        ("IMA-MIB", "imaLinkGroupIndex"),
        ("IMA-MIB", "imaLinkNeRxState"),
        ("IMA-MIB", "imaLinkNeTxState"),
        ("IMA-MIB", "imaLinkFeRxState"),
        ("IMA-MIB", "imaLinkFeTxState"),
        ("IMA-MIB", "imaLinkNeRxFailureStatus"),
        ("IMA-MIB", "imaLinkFeRxFailureStatus"),
        ("IMA-MIB", "imaLinkTxLid"),
        ("IMA-MIB", "imaLinkRxLid"),
        ("IMA-MIB", "imaLinkRelDelay"),
        ("IMA-MIB", "imaLinkImaViolations"),
        ("IMA-MIB", "imaLinkOifAnomalies"),
        ("IMA-MIB", "imaLinkFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkNeUnavailSecs"),
        ("IMA-MIB", "imaLinkFeUnavailSecs"),
        ("IMA-MIB", "imaLinkNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkNeTxNumFailures"),
        ("IMA-MIB", "imaLinkNeRxNumFailures"),
        ("IMA-MIB", "imaLinkFeTxNumFailures"),
        ("IMA-MIB", "imaLinkFeRxNumFailures"),
        ("IMA-MIB", "imaLinkTxStuffs"),
        ("IMA-MIB", "imaLinkRxStuffs"),
        ("IMA-MIB", "imaLinkConfAlarmProfile"))
)
if mibBuilder.loadTexts:
    imaLinkGroup.setStatus("current")

imaGroupMappingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 3)
)
imaGroupMappingTableGroup.setObjects(
    ("IMA-MIB", "imaGroupMappingIndex")
)
if mibBuilder.loadTexts:
    imaGroupMappingTableGroup.setStatus("current")

imaTestPatternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 4)
)
imaTestPatternGroup.setObjects(
      *(("IMA-MIB", "imaGroupTestLinkIfIndex"),
        ("IMA-MIB", "imaGroupTestPattern"),
        ("IMA-MIB", "imaGroupTestProcStatus"),
        ("IMA-MIB", "imaLinkRxTestPattern"),
        ("IMA-MIB", "imaLinkTestProcStatus"))
)
if mibBuilder.loadTexts:
    imaTestPatternGroup.setStatus("current")

imaAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 5)
)
imaAlarmGroup.setObjects(
      *(("IMA-MIB", "imaAlarmStatus"),
        ("IMA-MIB", "imaAlarmType"))
)
if mibBuilder.loadTexts:
    imaAlarmGroup.setStatus("current")

imaGroupIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 6)
)
imaGroupIntervalGroup.setObjects(
      *(("IMA-MIB", "imaGroupTimeElapsed"),
        ("IMA-MIB", "imaGroupCurrentUnavailSecs"),
        ("IMA-MIB", "imaGroupCurrentNeNumFailures"),
        ("IMA-MIB", "imaGroupCurrentFeNumFailures"),
        ("IMA-MIB", "imaGroupIntervalUnavailSecs"),
        ("IMA-MIB", "imaGroupIntervalNeNumFailures"),
        ("IMA-MIB", "imaGroupIntervalFeNumFailures"),
        ("IMA-MIB", "imaGroupIntervalMoniSecs"),
        ("IMA-MIB", "imaGroupCurrDayTimeElapsed"),
        ("IMA-MIB", "imaGroupCurrDayUnavailSecs"),
        ("IMA-MIB", "imaGroupCurrDayNeNumFailures"),
        ("IMA-MIB", "imaGroupCurrDayFeNumFailures"),
        ("IMA-MIB", "imaGroup1DayIntervalMoniSecs"),
        ("IMA-MIB", "imaGroup1DayIntervalUnavailSecs"),
        ("IMA-MIB", "imaGroup1DayIntervalNeNumFailures"),
        ("IMA-MIB", "imaGroup1DayIntervalFeNumFailures"))
)
if mibBuilder.loadTexts:
    imaGroupIntervalGroup.setStatus("current")

imaLinkIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 7)
)
imaLinkIntervalGroup.setObjects(
      *(("IMA-MIB", "imaLinkTimeElapsed"),
        ("IMA-MIB", "imaLinkCurrentImaViolations"),
        ("IMA-MIB", "imaLinkCurrentOifAnomalies"),
        ("IMA-MIB", "imaLinkCurrentNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkCurrentFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkCurrentNeUnavailSecs"),
        ("IMA-MIB", "imaLinkCurrentFeUnavailSecs"),
        ("IMA-MIB", "imaLinkCurrentNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentNeTxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentNeRxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentFeTxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentFeRxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentTxStuffs"),
        ("IMA-MIB", "imaLinkCurrentRxStuffs"),
        ("IMA-MIB", "imaLinkIntervalImaViolations"),
        ("IMA-MIB", "imaLinkIntervalOifAnomalies"),
        ("IMA-MIB", "imaLinkIntervalNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkIntervalFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkIntervalNeUnavailSecs"),
        ("IMA-MIB", "imaLinkIntervalFeUnavailSecs"),
        ("IMA-MIB", "imaLinkIntervalNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkIntervalNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkIntervalFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkIntervalFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkIntervalNeTxNumFailures"),
        ("IMA-MIB", "imaLinkIntervalNeRxNumFailures"),
        ("IMA-MIB", "imaLinkIntervalFeTxNumFailures"),
        ("IMA-MIB", "imaLinkIntervalFeRxNumFailures"),
        ("IMA-MIB", "imaLinkIntervalTxStuffs"),
        ("IMA-MIB", "imaLinkIntervalRxStuffs"),
        ("IMA-MIB", "imaLinkIntervalMoniSecs"),
        ("IMA-MIB", "imaLinkCurrDayTimeElapsed"),
        ("IMA-MIB", "imaLinkCurrDayImaViolations"),
        ("IMA-MIB", "imaLinkCurrDayOifAnomalies"),
        ("IMA-MIB", "imaLinkCurrDayNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkCurrDayFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkCurrDayNeUnavailSecs"),
        ("IMA-MIB", "imaLinkCurrDayFeUnavailSecs"),
        ("IMA-MIB", "imaLinkCurrDayNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrDayNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrDayFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrDayFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrDayNeTxNumFailures"),
        ("IMA-MIB", "imaLinkCurrDayNeRxNumFailures"),
        ("IMA-MIB", "imaLinkCurrDayFeTxNumFailures"),
        ("IMA-MIB", "imaLinkCurrDayFeRxNumFailures"),
        ("IMA-MIB", "imaLinkCurrDayTxStuffs"),
        ("IMA-MIB", "imaLinkCurrDayRxStuffs"),
        ("IMA-MIB", "imaLink1DayIntervalMoniSecs"),
        ("IMA-MIB", "imaLink1DayIntervalImaViolations"),
        ("IMA-MIB", "imaLink1DayIntervalOifAnomalies"),
        ("IMA-MIB", "imaLink1DayIntervalNeSevErroredSecs"),
        ("IMA-MIB", "imaLink1DayIntervalFeSevErroredSecs"),
        ("IMA-MIB", "imaLink1DayIntervalNeUnavailSecs"),
        ("IMA-MIB", "imaLink1DayIntervalFeUnavailSecs"),
        ("IMA-MIB", "imaLink1DayIntervalNeTxUnusableSecs"),
        ("IMA-MIB", "imaLink1DayIntervalNeRxUnusableSecs"),
        ("IMA-MIB", "imaLink1DayIntervalFeTxUnusableSecs"),
        ("IMA-MIB", "imaLink1DayIntervalFeRxUnusableSecs"),
        ("IMA-MIB", "imaLink1DayIntervalNeTxNumFailures"),
        ("IMA-MIB", "imaLink1DayIntervalNeRxNumFailures"),
        ("IMA-MIB", "imaLink1DayIntervalFeTxNumFailures"),
        ("IMA-MIB", "imaLink1DayIntervalFeRxNumFailures"),
        ("IMA-MIB", "imaLink1DayIntervalTxStuffs"),
        ("IMA-MIB", "imaLink1DayIntervalRxStuffs"))
)
if mibBuilder.loadTexts:
    imaLinkIntervalGroup.setStatus("current")

imaGroupAlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 8)
)
imaGroupAlarmConfGroup.setObjects(
      *(("IMA-MIB", "imaGroupThreshUnavailSecs"),
        ("IMA-MIB", "imaGroupThreshNeNumFailures"),
        ("IMA-MIB", "imaGroupThreshFeNumFailures"),
        ("IMA-MIB", "imaGroupAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    imaGroupAlarmConfGroup.setStatus("current")

imaLinkAlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 9)
)
imaLinkAlarmConfGroup.setObjects(
      *(("IMA-MIB", "imaLinkThreshImaViolations"),
        ("IMA-MIB", "imaLinkThreshOifAnomalies"),
        ("IMA-MIB", "imaLinkThreshNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkThreshFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkThreshNeUnavailSecs"),
        ("IMA-MIB", "imaLinkThreshFeUnavailSecs"),
        ("IMA-MIB", "imaLinkThreshNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkThreshNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkThreshFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkThreshFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkThreshNeTxNumFailures"),
        ("IMA-MIB", "imaLinkThreshNeRxNumFailures"),
        ("IMA-MIB", "imaLinkThreshFeTxNumFailures"),
        ("IMA-MIB", "imaLinkThreshFeRxNumFailures"),
        ("IMA-MIB", "imaLinkAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    imaLinkAlarmConfGroup.setStatus("current")


# Notification objects

imaFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 1)
)
imaFailureAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaAlarmStatus"),
        ("IMA-MIB", "imaAlarmType"))
)
if mibBuilder.loadTexts:
    imaFailureAlarm.setStatus(
        "current"
    )

imaGroupUnavailSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 2)
)
imaGroupUnavailSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaGroupThreshUnavailSecs"),
        ("IMA-MIB", "imaGroupCurrentUnavailSecs"))
)
if mibBuilder.loadTexts:
    imaGroupUnavailSecsCrossing.setStatus(
        "current"
    )

imaGroupNeNumFailuresCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 3)
)
imaGroupNeNumFailuresCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaGroupThreshNeNumFailures"),
        ("IMA-MIB", "imaGroupCurrentNeNumFailures"))
)
if mibBuilder.loadTexts:
    imaGroupNeNumFailuresCrossing.setStatus(
        "current"
    )

imaGroupFeNumFailuresCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 4)
)
imaGroupFeNumFailuresCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaGroupThreshFeNumFailures"),
        ("IMA-MIB", "imaGroupCurrentFeNumFailures"))
)
if mibBuilder.loadTexts:
    imaGroupFeNumFailuresCrossing.setStatus(
        "current"
    )

imaLinkImaViolationsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 5)
)
imaLinkImaViolationsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshImaViolations"),
        ("IMA-MIB", "imaLinkCurrentImaViolations"))
)
if mibBuilder.loadTexts:
    imaLinkImaViolationsCrossing.setStatus(
        "current"
    )

imaLinkOifAnomaliesCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 6)
)
imaLinkOifAnomaliesCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshOifAnomalies"),
        ("IMA-MIB", "imaLinkCurrentOifAnomalies"))
)
if mibBuilder.loadTexts:
    imaLinkOifAnomaliesCrossing.setStatus(
        "current"
    )

imaLinkNeSevErroredSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 7)
)
imaLinkNeSevErroredSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkCurrentNeSevErroredSecs"))
)
if mibBuilder.loadTexts:
    imaLinkNeSevErroredSecsCrossing.setStatus(
        "current"
    )

imaLinkFeSevErroredSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 8)
)
imaLinkFeSevErroredSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkCurrentFeSevErroredSecs"))
)
if mibBuilder.loadTexts:
    imaLinkFeSevErroredSecsCrossing.setStatus(
        "current"
    )

imaLinkNeUnavailSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 9)
)
imaLinkNeUnavailSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshNeUnavailSecs"),
        ("IMA-MIB", "imaLinkCurrentNeUnavailSecs"))
)
if mibBuilder.loadTexts:
    imaLinkNeUnavailSecsCrossing.setStatus(
        "current"
    )

imaLinkFeUnavailSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 10)
)
imaLinkFeUnavailSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshFeUnavailSecs"),
        ("IMA-MIB", "imaLinkCurrentFeUnavailSecs"))
)
if mibBuilder.loadTexts:
    imaLinkFeUnavailSecsCrossing.setStatus(
        "current"
    )

imaLinkNeTxUnusableSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 11)
)
imaLinkNeTxUnusableSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentNeTxUnusableSecs"))
)
if mibBuilder.loadTexts:
    imaLinkNeTxUnusableSecsCrossing.setStatus(
        "current"
    )

imaLinkNeRxUnusableSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 12)
)
imaLinkNeRxUnusableSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentNeRxUnusableSecs"))
)
if mibBuilder.loadTexts:
    imaLinkNeRxUnusableSecsCrossing.setStatus(
        "current"
    )

imaLinkFeTxUnusableSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 13)
)
imaLinkFeTxUnusableSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentFeTxUnusableSecs"))
)
if mibBuilder.loadTexts:
    imaLinkFeTxUnusableSecsCrossing.setStatus(
        "current"
    )

imaLinkFeRxUnusableSecsCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 14)
)
imaLinkFeRxUnusableSecsCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentFeRxUnusableSecs"))
)
if mibBuilder.loadTexts:
    imaLinkFeRxUnusableSecsCrossing.setStatus(
        "current"
    )

imaLinkNeTxNumFailuresCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 15)
)
imaLinkNeTxNumFailuresCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshNeTxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentNeTxNumFailures"))
)
if mibBuilder.loadTexts:
    imaLinkNeTxNumFailuresCrossing.setStatus(
        "current"
    )

imaLinkNeRxNumFailuresCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 16)
)
imaLinkNeRxNumFailuresCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshNeRxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentNeRxNumFailures"))
)
if mibBuilder.loadTexts:
    imaLinkNeRxNumFailuresCrossing.setStatus(
        "current"
    )

imaLinkFeTxNumFailuresCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 17)
)
imaLinkFeTxNumFailuresCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshFeTxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentFeTxNumFailures"))
)
if mibBuilder.loadTexts:
    imaLinkFeTxNumFailuresCrossing.setStatus(
        "current"
    )

imaLinkFeRxNumFailuresCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 18)
)
imaLinkFeRxNumFailuresCrossing.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaLinkThreshFeRxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentFeRxNumFailures"))
)
if mibBuilder.loadTexts:
    imaLinkFeRxNumFailuresCrossing.setStatus(
        "current"
    )


# Notifications groups

imaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 10)
)
imaNotificationsGroup.setObjects(
      *(("IMA-MIB", "imaFailureAlarm"),
        ("IMA-MIB", "imaGroupUnavailSecsCrossing"),
        ("IMA-MIB", "imaGroupNeNumFailuresCrossing"),
        ("IMA-MIB", "imaGroupFeNumFailuresCrossing"),
        ("IMA-MIB", "imaLinkImaViolationsCrossing"),
        ("IMA-MIB", "imaLinkOifAnomaliesCrossing"),
        ("IMA-MIB", "imaLinkNeSevErroredSecsCrossing"),
        ("IMA-MIB", "imaLinkFeSevErroredSecsCrossing"),
        ("IMA-MIB", "imaLinkNeUnavailSecsCrossing"),
        ("IMA-MIB", "imaLinkFeUnavailSecsCrossing"),
        ("IMA-MIB", "imaLinkNeTxUnusableSecsCrossing"),
        ("IMA-MIB", "imaLinkNeRxUnusableSecsCrossing"),
        ("IMA-MIB", "imaLinkFeTxUnusableSecsCrossing"),
        ("IMA-MIB", "imaLinkFeRxUnusableSecsCrossing"),
        ("IMA-MIB", "imaLinkNeTxNumFailuresCrossing"),
        ("IMA-MIB", "imaLinkNeRxNumFailuresCrossing"),
        ("IMA-MIB", "imaLinkFeTxNumFailuresCrossing"),
        ("IMA-MIB", "imaLinkFeRxNumFailuresCrossing"))
)
if mibBuilder.loadTexts:
    imaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

imaMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 2, 1)
)
imaMibCompliance.setObjects(
      *(("IMA-MIB", "imaGroupGroup"),
        ("IMA-MIB", "imaLinkGroup"),
        ("IMA-MIB", "imaGroupMappingTableGroup"),
        ("IMA-MIB", "imaAlarmGroup"),
        ("IMA-MIB", "imaGroupAlarmConfGroup"),
        ("IMA-MIB", "imaLinkAlarmConfGroup"),
        ("IMA-MIB", "imaNotificationsGroup"),
        ("IMA-MIB", "imaTestPatternGroup"),
        ("IMA-MIB", "imaGroupIntervalGroup"),
        ("IMA-MIB", "imaLinkIntervalGroup"))
)
if mibBuilder.loadTexts:
    imaMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IMA-MIB",
    **{"MilliSeconds": MilliSeconds,
       "ImaGroupState": ImaGroupState,
       "ImaGroupFailureStatus": ImaGroupFailureStatus,
       "ImaAlarmStatus": ImaAlarmStatus,
       "ImaAlarmType": ImaAlarmType,
       "ImaGroupTxClkMode": ImaGroupTxClkMode,
       "ImaGroupSymmetry": ImaGroupSymmetry,
       "ImaFrameLength": ImaFrameLength,
       "ImaLinkState": ImaLinkState,
       "ImaLinkFailureStatus": ImaLinkFailureStatus,
       "ImaTestProcStatus": ImaTestProcStatus,
       "ImaPerfCurrDayCount": ImaPerfCurrDayCount,
       "ImaPerfTimeElapsed": ImaPerfTimeElapsed,
       "ImaPerf1DayIntervalCount": ImaPerf1DayIntervalCount,
       "ImaPerfIntervalThreshold": ImaPerfIntervalThreshold,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfIma": atmfIma,
       "atmfImaMib": atmfImaMib,
       "imaMibObjects": imaMibObjects,
       "imaGroupTable": imaGroupTable,
       "imaGroupEntry": imaGroupEntry,
       "imaGroupIndex": imaGroupIndex,
       "imaGroupRowStatus": imaGroupRowStatus,
       "imaGroupIfIndex": imaGroupIfIndex,
       "imaGroupNeState": imaGroupNeState,
       "imaGroupFeState": imaGroupFeState,
       "imaGroupFailureStatus": imaGroupFailureStatus,
       "imaGroupSymmetry": imaGroupSymmetry,
       "imaGroupMinNumTxLinks": imaGroupMinNumTxLinks,
       "imaGroupMinNumRxLinks": imaGroupMinNumRxLinks,
       "imaGroupNeTxClkMode": imaGroupNeTxClkMode,
       "imaGroupFeTxClkMode": imaGroupFeTxClkMode,
       "imaGroupTxTimingRefLink": imaGroupTxTimingRefLink,
       "imaGroupRxTimingRefLink": imaGroupRxTimingRefLink,
       "imaGroupLastChange": imaGroupLastChange,
       "imaGroupTxImaId": imaGroupTxImaId,
       "imaGroupRxImaId": imaGroupRxImaId,
       "imaGroupTxFrameLength": imaGroupTxFrameLength,
       "imaGroupRxFrameLength": imaGroupRxFrameLength,
       "imaGroupDiffDelayMax": imaGroupDiffDelayMax,
       "imaGroupLeastDelayLink": imaGroupLeastDelayLink,
       "imaGroupDiffDelayMaxObs": imaGroupDiffDelayMaxObs,
       "imaGroupAlphaValue": imaGroupAlphaValue,
       "imaGroupBetaValue": imaGroupBetaValue,
       "imaGroupGammaValue": imaGroupGammaValue,
       "imaGroupRunningSecs": imaGroupRunningSecs,
       "imaGroupUnavailSecs": imaGroupUnavailSecs,
       "imaGroupNeNumFailures": imaGroupNeNumFailures,
       "imaGroupFeNumFailures": imaGroupFeNumFailures,
       "imaGroupTxAvailCellRate": imaGroupTxAvailCellRate,
       "imaGroupRxAvailCellRate": imaGroupRxAvailCellRate,
       "imaGroupNumTxCfgLinks": imaGroupNumTxCfgLinks,
       "imaGroupNumRxCfgLinks": imaGroupNumRxCfgLinks,
       "imaGroupNumTxActLinks": imaGroupNumTxActLinks,
       "imaGroupNumRxActLinks": imaGroupNumRxActLinks,
       "imaGroupTestLinkIfIndex": imaGroupTestLinkIfIndex,
       "imaGroupTestPattern": imaGroupTestPattern,
       "imaGroupTestProcStatus": imaGroupTestProcStatus,
       "imaGroupTimeElapsed": imaGroupTimeElapsed,
       "imaGroupTxOamLabelValue": imaGroupTxOamLabelValue,
       "imaGroupRxOamLabelValue": imaGroupRxOamLabelValue,
       "imaGroupConfAlarmProfile": imaGroupConfAlarmProfile,
       "imaGroupMappingTable": imaGroupMappingTable,
       "imaGroupMappingEntry": imaGroupMappingEntry,
       "imaGroupMappingIndex": imaGroupMappingIndex,
       "imaLinkTable": imaLinkTable,
       "imaLinkEntry": imaLinkEntry,
       "imaLinkIfIndex": imaLinkIfIndex,
       "imaLinkRowStatus": imaLinkRowStatus,
       "imaLinkGroupIndex": imaLinkGroupIndex,
       "imaLinkNeTxState": imaLinkNeTxState,
       "imaLinkNeRxState": imaLinkNeRxState,
       "imaLinkFeTxState": imaLinkFeTxState,
       "imaLinkFeRxState": imaLinkFeRxState,
       "imaLinkNeRxFailureStatus": imaLinkNeRxFailureStatus,
       "imaLinkFeRxFailureStatus": imaLinkFeRxFailureStatus,
       "imaLinkTxLid": imaLinkTxLid,
       "imaLinkRxLid": imaLinkRxLid,
       "imaLinkRelDelay": imaLinkRelDelay,
       "imaLinkImaViolations": imaLinkImaViolations,
       "imaLinkOifAnomalies": imaLinkOifAnomalies,
       "imaLinkNeSevErroredSecs": imaLinkNeSevErroredSecs,
       "imaLinkFeSevErroredSecs": imaLinkFeSevErroredSecs,
       "imaLinkNeUnavailSecs": imaLinkNeUnavailSecs,
       "imaLinkFeUnavailSecs": imaLinkFeUnavailSecs,
       "imaLinkNeTxUnusableSecs": imaLinkNeTxUnusableSecs,
       "imaLinkNeRxUnusableSecs": imaLinkNeRxUnusableSecs,
       "imaLinkFeTxUnusableSecs": imaLinkFeTxUnusableSecs,
       "imaLinkFeRxUnusableSecs": imaLinkFeRxUnusableSecs,
       "imaLinkNeTxNumFailures": imaLinkNeTxNumFailures,
       "imaLinkNeRxNumFailures": imaLinkNeRxNumFailures,
       "imaLinkFeTxNumFailures": imaLinkFeTxNumFailures,
       "imaLinkFeRxNumFailures": imaLinkFeRxNumFailures,
       "imaLinkTxStuffs": imaLinkTxStuffs,
       "imaLinkRxStuffs": imaLinkRxStuffs,
       "imaLinkRxTestPattern": imaLinkRxTestPattern,
       "imaLinkTestProcStatus": imaLinkTestProcStatus,
       "imaLinkTimeElapsed": imaLinkTimeElapsed,
       "imaLinkConfAlarmProfile": imaLinkConfAlarmProfile,
       "imaAlarmStatus": imaAlarmStatus,
       "imaAlarmType": imaAlarmType,
       "imaGroupCurrentTable": imaGroupCurrentTable,
       "imaGroupCurrentEntry": imaGroupCurrentEntry,
       "imaGroupCurrentUnavailSecs": imaGroupCurrentUnavailSecs,
       "imaGroupCurrentNeNumFailures": imaGroupCurrentNeNumFailures,
       "imaGroupCurrentFeNumFailures": imaGroupCurrentFeNumFailures,
       "imaGroupIntervalTable": imaGroupIntervalTable,
       "imaGroupIntervalEntry": imaGroupIntervalEntry,
       "imaGroupIntervalNumber": imaGroupIntervalNumber,
       "imaGroupIntervalUnavailSecs": imaGroupIntervalUnavailSecs,
       "imaGroupIntervalNeNumFailures": imaGroupIntervalNeNumFailures,
       "imaGroupIntervalFeNumFailures": imaGroupIntervalFeNumFailures,
       "imaGroupIntervalMoniSecs": imaGroupIntervalMoniSecs,
       "imaGroupCurrDayTable": imaGroupCurrDayTable,
       "imaGroupCurrDayEntry": imaGroupCurrDayEntry,
       "imaGroupCurrDayTimeElapsed": imaGroupCurrDayTimeElapsed,
       "imaGroupCurrDayUnavailSecs": imaGroupCurrDayUnavailSecs,
       "imaGroupCurrDayNeNumFailures": imaGroupCurrDayNeNumFailures,
       "imaGroupCurrDayFeNumFailures": imaGroupCurrDayFeNumFailures,
       "imaGroup1DayIntervalTable": imaGroup1DayIntervalTable,
       "imaGroup1DayIntervalEntry": imaGroup1DayIntervalEntry,
       "imaGroup1DayIntervalNumber": imaGroup1DayIntervalNumber,
       "imaGroup1DayIntervalMoniSecs": imaGroup1DayIntervalMoniSecs,
       "imaGroup1DayIntervalUnavailSecs": imaGroup1DayIntervalUnavailSecs,
       "imaGroup1DayIntervalNeNumFailures": imaGroup1DayIntervalNeNumFailures,
       "imaGroup1DayIntervalFeNumFailures": imaGroup1DayIntervalFeNumFailures,
       "imaGroupAlarmConfProfileTable": imaGroupAlarmConfProfileTable,
       "imaGroupAlarmConfProfileEntry": imaGroupAlarmConfProfileEntry,
       "imaGroupAlarmConfProfileName": imaGroupAlarmConfProfileName,
       "imaGroupThreshUnavailSecs": imaGroupThreshUnavailSecs,
       "imaGroupThreshNeNumFailures": imaGroupThreshNeNumFailures,
       "imaGroupThreshFeNumFailures": imaGroupThreshFeNumFailures,
       "imaGroupAlarmConfProfileRowStatus": imaGroupAlarmConfProfileRowStatus,
       "imaLinkCurrentTable": imaLinkCurrentTable,
       "imaLinkCurrentEntry": imaLinkCurrentEntry,
       "imaLinkCurrentImaViolations": imaLinkCurrentImaViolations,
       "imaLinkCurrentOifAnomalies": imaLinkCurrentOifAnomalies,
       "imaLinkCurrentNeSevErroredSecs": imaLinkCurrentNeSevErroredSecs,
       "imaLinkCurrentFeSevErroredSecs": imaLinkCurrentFeSevErroredSecs,
       "imaLinkCurrentNeUnavailSecs": imaLinkCurrentNeUnavailSecs,
       "imaLinkCurrentFeUnavailSecs": imaLinkCurrentFeUnavailSecs,
       "imaLinkCurrentNeTxUnusableSecs": imaLinkCurrentNeTxUnusableSecs,
       "imaLinkCurrentNeRxUnusableSecs": imaLinkCurrentNeRxUnusableSecs,
       "imaLinkCurrentFeTxUnusableSecs": imaLinkCurrentFeTxUnusableSecs,
       "imaLinkCurrentFeRxUnusableSecs": imaLinkCurrentFeRxUnusableSecs,
       "imaLinkCurrentNeTxNumFailures": imaLinkCurrentNeTxNumFailures,
       "imaLinkCurrentNeRxNumFailures": imaLinkCurrentNeRxNumFailures,
       "imaLinkCurrentFeTxNumFailures": imaLinkCurrentFeTxNumFailures,
       "imaLinkCurrentFeRxNumFailures": imaLinkCurrentFeRxNumFailures,
       "imaLinkCurrentTxStuffs": imaLinkCurrentTxStuffs,
       "imaLinkCurrentRxStuffs": imaLinkCurrentRxStuffs,
       "imaLinkIntervalTable": imaLinkIntervalTable,
       "imaLinkIntervalEntry": imaLinkIntervalEntry,
       "imaLinkIntervalNumber": imaLinkIntervalNumber,
       "imaLinkIntervalImaViolations": imaLinkIntervalImaViolations,
       "imaLinkIntervalOifAnomalies": imaLinkIntervalOifAnomalies,
       "imaLinkIntervalNeSevErroredSecs": imaLinkIntervalNeSevErroredSecs,
       "imaLinkIntervalFeSevErroredSecs": imaLinkIntervalFeSevErroredSecs,
       "imaLinkIntervalNeUnavailSecs": imaLinkIntervalNeUnavailSecs,
       "imaLinkIntervalFeUnavailSecs": imaLinkIntervalFeUnavailSecs,
       "imaLinkIntervalNeTxUnusableSecs": imaLinkIntervalNeTxUnusableSecs,
       "imaLinkIntervalNeRxUnusableSecs": imaLinkIntervalNeRxUnusableSecs,
       "imaLinkIntervalFeTxUnusableSecs": imaLinkIntervalFeTxUnusableSecs,
       "imaLinkIntervalFeRxUnusableSecs": imaLinkIntervalFeRxUnusableSecs,
       "imaLinkIntervalNeTxNumFailures": imaLinkIntervalNeTxNumFailures,
       "imaLinkIntervalNeRxNumFailures": imaLinkIntervalNeRxNumFailures,
       "imaLinkIntervalFeTxNumFailures": imaLinkIntervalFeTxNumFailures,
       "imaLinkIntervalFeRxNumFailures": imaLinkIntervalFeRxNumFailures,
       "imaLinkIntervalTxStuffs": imaLinkIntervalTxStuffs,
       "imaLinkIntervalRxStuffs": imaLinkIntervalRxStuffs,
       "imaLinkIntervalMoniSecs": imaLinkIntervalMoniSecs,
       "imaLinkCurrDayTable": imaLinkCurrDayTable,
       "imaLinkCurrDayEntry": imaLinkCurrDayEntry,
       "imaLinkCurrDayTimeElapsed": imaLinkCurrDayTimeElapsed,
       "imaLinkCurrDayImaViolations": imaLinkCurrDayImaViolations,
       "imaLinkCurrDayOifAnomalies": imaLinkCurrDayOifAnomalies,
       "imaLinkCurrDayNeSevErroredSecs": imaLinkCurrDayNeSevErroredSecs,
       "imaLinkCurrDayFeSevErroredSecs": imaLinkCurrDayFeSevErroredSecs,
       "imaLinkCurrDayNeUnavailSecs": imaLinkCurrDayNeUnavailSecs,
       "imaLinkCurrDayFeUnavailSecs": imaLinkCurrDayFeUnavailSecs,
       "imaLinkCurrDayNeTxUnusableSecs": imaLinkCurrDayNeTxUnusableSecs,
       "imaLinkCurrDayNeRxUnusableSecs": imaLinkCurrDayNeRxUnusableSecs,
       "imaLinkCurrDayFeTxUnusableSecs": imaLinkCurrDayFeTxUnusableSecs,
       "imaLinkCurrDayFeRxUnusableSecs": imaLinkCurrDayFeRxUnusableSecs,
       "imaLinkCurrDayNeTxNumFailures": imaLinkCurrDayNeTxNumFailures,
       "imaLinkCurrDayNeRxNumFailures": imaLinkCurrDayNeRxNumFailures,
       "imaLinkCurrDayFeTxNumFailures": imaLinkCurrDayFeTxNumFailures,
       "imaLinkCurrDayFeRxNumFailures": imaLinkCurrDayFeRxNumFailures,
       "imaLinkCurrDayTxStuffs": imaLinkCurrDayTxStuffs,
       "imaLinkCurrDayRxStuffs": imaLinkCurrDayRxStuffs,
       "imaLink1DayIntervalTable": imaLink1DayIntervalTable,
       "imaLink1DayIntervalEntry": imaLink1DayIntervalEntry,
       "imaLink1DayIntervalNumber": imaLink1DayIntervalNumber,
       "imaLink1DayIntervalMoniSecs": imaLink1DayIntervalMoniSecs,
       "imaLink1DayIntervalImaViolations": imaLink1DayIntervalImaViolations,
       "imaLink1DayIntervalOifAnomalies": imaLink1DayIntervalOifAnomalies,
       "imaLink1DayIntervalNeSevErroredSecs": imaLink1DayIntervalNeSevErroredSecs,
       "imaLink1DayIntervalFeSevErroredSecs": imaLink1DayIntervalFeSevErroredSecs,
       "imaLink1DayIntervalNeUnavailSecs": imaLink1DayIntervalNeUnavailSecs,
       "imaLink1DayIntervalFeUnavailSecs": imaLink1DayIntervalFeUnavailSecs,
       "imaLink1DayIntervalNeTxUnusableSecs": imaLink1DayIntervalNeTxUnusableSecs,
       "imaLink1DayIntervalNeRxUnusableSecs": imaLink1DayIntervalNeRxUnusableSecs,
       "imaLink1DayIntervalFeTxUnusableSecs": imaLink1DayIntervalFeTxUnusableSecs,
       "imaLink1DayIntervalFeRxUnusableSecs": imaLink1DayIntervalFeRxUnusableSecs,
       "imaLink1DayIntervalNeTxNumFailures": imaLink1DayIntervalNeTxNumFailures,
       "imaLink1DayIntervalNeRxNumFailures": imaLink1DayIntervalNeRxNumFailures,
       "imaLink1DayIntervalFeTxNumFailures": imaLink1DayIntervalFeTxNumFailures,
       "imaLink1DayIntervalFeRxNumFailures": imaLink1DayIntervalFeRxNumFailures,
       "imaLink1DayIntervalTxStuffs": imaLink1DayIntervalTxStuffs,
       "imaLink1DayIntervalRxStuffs": imaLink1DayIntervalRxStuffs,
       "imaLinkAlarmConfProfileTable": imaLinkAlarmConfProfileTable,
       "imaLinkAlarmConfProfileEntry": imaLinkAlarmConfProfileEntry,
       "imaLinkAlarmConfProfileName": imaLinkAlarmConfProfileName,
       "imaLinkThreshImaViolations": imaLinkThreshImaViolations,
       "imaLinkThreshOifAnomalies": imaLinkThreshOifAnomalies,
       "imaLinkThreshNeSevErroredSecs": imaLinkThreshNeSevErroredSecs,
       "imaLinkThreshFeSevErroredSecs": imaLinkThreshFeSevErroredSecs,
       "imaLinkThreshNeUnavailSecs": imaLinkThreshNeUnavailSecs,
       "imaLinkThreshFeUnavailSecs": imaLinkThreshFeUnavailSecs,
       "imaLinkThreshNeTxUnusableSecs": imaLinkThreshNeTxUnusableSecs,
       "imaLinkThreshNeRxUnusableSecs": imaLinkThreshNeRxUnusableSecs,
       "imaLinkThreshFeTxUnusableSecs": imaLinkThreshFeTxUnusableSecs,
       "imaLinkThreshFeRxUnusableSecs": imaLinkThreshFeRxUnusableSecs,
       "imaLinkThreshNeTxNumFailures": imaLinkThreshNeTxNumFailures,
       "imaLinkThreshNeRxNumFailures": imaLinkThreshNeRxNumFailures,
       "imaLinkThreshFeTxNumFailures": imaLinkThreshFeTxNumFailures,
       "imaLinkThreshFeRxNumFailures": imaLinkThreshFeRxNumFailures,
       "imaLinkAlarmConfProfileRowStatus": imaLinkAlarmConfProfileRowStatus,
       "imaMibTraps": imaMibTraps,
       "imaMibTrapPrefix": imaMibTrapPrefix,
       "imaFailureAlarm": imaFailureAlarm,
       "imaGroupUnavailSecsCrossing": imaGroupUnavailSecsCrossing,
       "imaGroupNeNumFailuresCrossing": imaGroupNeNumFailuresCrossing,
       "imaGroupFeNumFailuresCrossing": imaGroupFeNumFailuresCrossing,
       "imaLinkImaViolationsCrossing": imaLinkImaViolationsCrossing,
       "imaLinkOifAnomaliesCrossing": imaLinkOifAnomaliesCrossing,
       "imaLinkNeSevErroredSecsCrossing": imaLinkNeSevErroredSecsCrossing,
       "imaLinkFeSevErroredSecsCrossing": imaLinkFeSevErroredSecsCrossing,
       "imaLinkNeUnavailSecsCrossing": imaLinkNeUnavailSecsCrossing,
       "imaLinkFeUnavailSecsCrossing": imaLinkFeUnavailSecsCrossing,
       "imaLinkNeTxUnusableSecsCrossing": imaLinkNeTxUnusableSecsCrossing,
       "imaLinkNeRxUnusableSecsCrossing": imaLinkNeRxUnusableSecsCrossing,
       "imaLinkFeTxUnusableSecsCrossing": imaLinkFeTxUnusableSecsCrossing,
       "imaLinkFeRxUnusableSecsCrossing": imaLinkFeRxUnusableSecsCrossing,
       "imaLinkNeTxNumFailuresCrossing": imaLinkNeTxNumFailuresCrossing,
       "imaLinkNeRxNumFailuresCrossing": imaLinkNeRxNumFailuresCrossing,
       "imaLinkFeTxNumFailuresCrossing": imaLinkFeTxNumFailuresCrossing,
       "imaLinkFeRxNumFailuresCrossing": imaLinkFeRxNumFailuresCrossing,
       "imaMibConformance": imaMibConformance,
       "imaMibGroups": imaMibGroups,
       "imaGroupGroup": imaGroupGroup,
       "imaLinkGroup": imaLinkGroup,
       "imaGroupMappingTableGroup": imaGroupMappingTableGroup,
       "imaTestPatternGroup": imaTestPatternGroup,
       "imaAlarmGroup": imaAlarmGroup,
       "imaGroupIntervalGroup": imaGroupIntervalGroup,
       "imaLinkIntervalGroup": imaLinkIntervalGroup,
       "imaGroupAlarmConfGroup": imaGroupAlarmConfGroup,
       "imaLinkAlarmConfGroup": imaLinkAlarmConfGroup,
       "imaNotificationsGroup": imaNotificationsGroup,
       "imaMibCompliances": imaMibCompliances,
       "imaMibCompliance": imaMibCompliance}
)
