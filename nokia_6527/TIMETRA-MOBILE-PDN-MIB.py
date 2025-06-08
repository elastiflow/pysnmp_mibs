# SNMP MIB module (TIMETRA-MOBILE-PDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MOBILE-PDN-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:37 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxBsxAaGrpPartIndex,) = mibBuilder.importSymbols(
    "TIMETRA-BSX-NG-MIB",
    "TmnxBsxAaGrpPartIndex")

(TmnxSlotNumOrZero,
 tmnxCardSlotNum,
 tmnxChassisIndex) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxSlotNumOrZero",
    "tmnxCardSlotNum",
    "tmnxChassisIndex")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRObjs")

(tmnxMobGwId,) = mibBuilder.importSymbols(
    "TIMETRA-MOBILE-GATEWAY-MIB",
    "tmnxMobGwId")

(tmnxMobGtpPriGrpName,
 tmnxMobGtpPriServerIndex,
 tmnxMobProfChgUnitRatingGroup,
 tmnxMobProfChgUnitServIdentifier,
 tmnxMobProfDiaPeerListIndex,
 tmnxMobProfDiaPeerName,
 tmnxMobProfPolBaseName,
 tmnxMobProfRadGrpName,
 tmnxMobProfRadPeerIndex) = mibBuilder.importSymbols(
    "TIMETRA-MOBILE-PROFILE-MIB",
    "tmnxMobGtpPriGrpName",
    "tmnxMobGtpPriServerIndex",
    "tmnxMobProfChgUnitRatingGroup",
    "tmnxMobProfChgUnitServIdentifier",
    "tmnxMobProfDiaPeerListIndex",
    "tmnxMobProfDiaPeerName",
    "tmnxMobProfPolBaseName",
    "tmnxMobProfRadGrpName",
    "tmnxMobProfRadPeerIndex")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TmnxAdminState,
 TmnxBsxIsaAaGroupIndexOrZero,
 TmnxCdrDiagnosticAction,
 TmnxCdrType,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledOrInherit,
 TmnxMobAccessType,
 TmnxMobAddrScheme,
 TmnxMobApn,
 TmnxMobApnOrZero,
 TmnxMobArp,
 TmnxMobArpValueOrZero,
 TmnxMobAuthType,
 TmnxMobAuthUserName,
 TmnxMobBearerId,
 TmnxMobBearerType,
 TmnxMobChargingBearerType,
 TmnxMobChargingLevel,
 TmnxMobChargingProfile,
 TmnxMobChargingProfileOrInherit,
 TmnxMobDiaDetailPathMgmtState,
 TmnxMobDiaPathMgmtState,
 TmnxMobDiaPeerHost,
 TmnxMobDiaRetryCount,
 TmnxMobDiaTransTimer,
 TmnxMobDualStackPref,
 TmnxMobGwId,
 TmnxMobImei,
 TmnxMobImsi,
 TmnxMobImsiStr,
 TmnxMobIpCanType,
 TmnxMobMcc,
 TmnxMobMnc,
 TmnxMobMsisdn,
 TmnxMobNai,
 TmnxMobNode,
 TmnxMobPathMgmtState,
 TmnxMobPdnGyChrgTriggerType,
 TmnxMobPdnRefPointType,
 TmnxMobPdnSessionEvent,
 TmnxMobPdnSessionState,
 TmnxMobPdnType,
 TmnxMobPeerType,
 TmnxMobPgwSigProtocol,
 TmnxMobPresenceState,
 TmnxMobProfMbrRate,
 TmnxMobProfName,
 TmnxMobProfNameOrEmpty,
 TmnxMobQci,
 TmnxMobQciValueOrZero,
 TmnxMobRatingGrpState,
 TmnxMobRfAcctLevel,
 TmnxMobRtrAdvtInterval,
 TmnxMobRtrAdvtLifeTime,
 TmnxMobSdf,
 TmnxMobSdfFilter,
 TmnxMobSdfFilterDirection,
 TmnxMobSdfFilterNum,
 TmnxMobSdfFilterProtocol,
 TmnxMobSdfRuleName,
 TmnxMobServerState,
 TmnxMobStaticPolPrecedence,
 TmnxMobUeId,
 TmnxMobUeIdType,
 TmnxMobUeRat,
 TmnxMobUeState,
 TmnxMobUeStrPrefix,
 TmnxMobUeSubType,
 TmnxOperState,
 TmnxQosBytesHex,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TmnxAdminState",
    "TmnxBsxIsaAaGroupIndexOrZero",
    "TmnxCdrDiagnosticAction",
    "TmnxCdrType",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledOrInherit",
    "TmnxMobAccessType",
    "TmnxMobAddrScheme",
    "TmnxMobApn",
    "TmnxMobApnOrZero",
    "TmnxMobArp",
    "TmnxMobArpValueOrZero",
    "TmnxMobAuthType",
    "TmnxMobAuthUserName",
    "TmnxMobBearerId",
    "TmnxMobBearerType",
    "TmnxMobChargingBearerType",
    "TmnxMobChargingLevel",
    "TmnxMobChargingProfile",
    "TmnxMobChargingProfileOrInherit",
    "TmnxMobDiaDetailPathMgmtState",
    "TmnxMobDiaPathMgmtState",
    "TmnxMobDiaPeerHost",
    "TmnxMobDiaRetryCount",
    "TmnxMobDiaTransTimer",
    "TmnxMobDualStackPref",
    "TmnxMobGwId",
    "TmnxMobImei",
    "TmnxMobImsi",
    "TmnxMobImsiStr",
    "TmnxMobIpCanType",
    "TmnxMobMcc",
    "TmnxMobMnc",
    "TmnxMobMsisdn",
    "TmnxMobNai",
    "TmnxMobNode",
    "TmnxMobPathMgmtState",
    "TmnxMobPdnGyChrgTriggerType",
    "TmnxMobPdnRefPointType",
    "TmnxMobPdnSessionEvent",
    "TmnxMobPdnSessionState",
    "TmnxMobPdnType",
    "TmnxMobPeerType",
    "TmnxMobPgwSigProtocol",
    "TmnxMobPresenceState",
    "TmnxMobProfMbrRate",
    "TmnxMobProfName",
    "TmnxMobProfNameOrEmpty",
    "TmnxMobQci",
    "TmnxMobQciValueOrZero",
    "TmnxMobRatingGrpState",
    "TmnxMobRfAcctLevel",
    "TmnxMobRtrAdvtInterval",
    "TmnxMobRtrAdvtLifeTime",
    "TmnxMobSdf",
    "TmnxMobSdfFilter",
    "TmnxMobSdfFilterDirection",
    "TmnxMobSdfFilterNum",
    "TmnxMobSdfFilterProtocol",
    "TmnxMobSdfRuleName",
    "TmnxMobServerState",
    "TmnxMobStaticPolPrecedence",
    "TmnxMobUeId",
    "TmnxMobUeIdType",
    "TmnxMobUeRat",
    "TmnxMobUeState",
    "TmnxMobUeStrPrefix",
    "TmnxMobUeSubType",
    "TmnxOperState",
    "TmnxQosBytesHex",
    "TmnxVRtrID")

(vRtrID,
 vRtrIpPoolName) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIpPoolName")


# MODULE-IDENTITY

timetraMobPdnMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 71)
)
if mibBuilder.loadTexts:
    timetraMobPdnMIBModule.setRevisions(
        ("1909-12-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxMobPdnConformance_ObjectIdentity = ObjectIdentity
tmnxMobPdnConformance = _TmnxMobPdnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71)
)
_TmnxMobPdnCompliances_ObjectIdentity = ObjectIdentity
tmnxMobPdnCompliances = _TmnxMobPdnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 1)
)
_TmnxMobPdnGroups_ObjectIdentity = ObjectIdentity
tmnxMobPdnGroups = _TmnxMobPdnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2)
)
_TmnxMobPdn_ObjectIdentity = ObjectIdentity
tmnxMobPdn = _TmnxMobPdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71)
)
_TmnxMobPdnConfObjs_ObjectIdentity = ObjectIdentity
tmnxMobPdnConfObjs = _TmnxMobPdnConfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1)
)
_TmnxMobPdnTable_Object = MibTable
tmnxMobPdnTable = _TmnxMobPdnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnTable.setStatus("current")
_TmnxMobPdnEntry_Object = MibTableRow
tmnxMobPdnEntry = _TmnxMobPdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1)
)
tmnxMobPdnEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnEntry.setStatus("current")
_TmnxMobPdnLastChanged_Type = TimeStamp
_TmnxMobPdnLastChanged_Object = MibTableColumn
tmnxMobPdnLastChanged = _TmnxMobPdnLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 1),
    _TmnxMobPdnLastChanged_Type()
)
tmnxMobPdnLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnLastChanged.setStatus("current")


class _TmnxMobPdnAdminState_Type(TmnxAdminState):
    """Custom type tmnxMobPdnAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMobPdnAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMobPdnAdminState_Object = MibTableColumn
tmnxMobPdnAdminState = _TmnxMobPdnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 2),
    _TmnxMobPdnAdminState_Type()
)
tmnxMobPdnAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnAdminState.setStatus("current")
_TmnxMobPdnOperState_Type = TmnxOperState
_TmnxMobPdnOperState_Object = MibTableColumn
tmnxMobPdnOperState = _TmnxMobPdnOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 3),
    _TmnxMobPdnOperState_Type()
)
tmnxMobPdnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnOperState.setStatus("current")


class _TmnxMobPdnGracefulShutTimeout_Type(Unsigned32):
    """Custom type tmnxMobPdnGracefulShutTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_TmnxMobPdnGracefulShutTimeout_Type.__name__ = "Unsigned32"
_TmnxMobPdnGracefulShutTimeout_Object = MibTableColumn
tmnxMobPdnGracefulShutTimeout = _TmnxMobPdnGracefulShutTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 4),
    _TmnxMobPdnGracefulShutTimeout_Type()
)
tmnxMobPdnGracefulShutTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGracefulShutTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnGracefulShutTimeout.setUnits("minutes")


class _TmnxMobPdnMobNode_Type(TmnxMobNode):
    """Custom type tmnxMobPdnMobNode based on TmnxMobNode"""
    defaultHexValue = ""


_TmnxMobPdnMobNode_Type.__name__ = "TmnxMobNode"
_TmnxMobPdnMobNode_Object = MibTableColumn
tmnxMobPdnMobNode = _TmnxMobPdnMobNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 5),
    _TmnxMobPdnMobNode_Type()
)
tmnxMobPdnMobNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnMobNode.setStatus("current")


class _TmnxMobPdnPccDynamicState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnPccDynamicState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnPccDynamicState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnPccDynamicState_Object = MibTableColumn
tmnxMobPdnPccDynamicState = _TmnxMobPdnPccDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 6),
    _TmnxMobPdnPccDynamicState_Type()
)
tmnxMobPdnPccDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnPccDynamicState.setStatus("current")


class _TmnxMobPdnPccPrecedenceBoundary_Type(TmnxMobStaticPolPrecedence):
    """Custom type tmnxMobPdnPccPrecedenceBoundary based on TmnxMobStaticPolPrecedence"""
    defaultValue = 257


_TmnxMobPdnPccPrecedenceBoundary_Type.__name__ = "TmnxMobStaticPolPrecedence"
_TmnxMobPdnPccPrecedenceBoundary_Object = MibTableColumn
tmnxMobPdnPccPrecedenceBoundary = _TmnxMobPdnPccPrecedenceBoundary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 7),
    _TmnxMobPdnPccPrecedenceBoundary_Type()
)
tmnxMobPdnPccPrecedenceBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnPccPrecedenceBoundary.setStatus("current")


class _TmnxMobPdnUplinkQciPolName_Type(TmnxMobProfName):
    """Custom type tmnxMobPdnUplinkQciPolName based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobPdnUplinkQciPolName_Type.__name__ = "TmnxMobProfName"
_TmnxMobPdnUplinkQciPolName_Object = MibTableColumn
tmnxMobPdnUplinkQciPolName = _TmnxMobPdnUplinkQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 8),
    _TmnxMobPdnUplinkQciPolName_Type()
)
tmnxMobPdnUplinkQciPolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnUplinkQciPolName.setStatus("current")


class _TmnxMobPdnDownlinkQciPolName_Type(TmnxMobProfName):
    """Custom type tmnxMobPdnDownlinkQciPolName based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobPdnDownlinkQciPolName_Type.__name__ = "TmnxMobProfName"
_TmnxMobPdnDownlinkQciPolName_Object = MibTableColumn
tmnxMobPdnDownlinkQciPolName = _TmnxMobPdnDownlinkQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 9),
    _TmnxMobPdnDownlinkQciPolName_Type()
)
tmnxMobPdnDownlinkQciPolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnDownlinkQciPolName.setStatus("current")


class _TmnxMobPdnHomePlmnList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnHomePlmnList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnHomePlmnList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnHomePlmnList_Object = MibTableColumn
tmnxMobPdnHomePlmnList = _TmnxMobPdnHomePlmnList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 10),
    _TmnxMobPdnHomePlmnList_Type()
)
tmnxMobPdnHomePlmnList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnHomePlmnList.setStatus("current")


class _TmnxMobPdnVisitingPlmnList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnVisitingPlmnList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnVisitingPlmnList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnVisitingPlmnList_Object = MibTableColumn
tmnxMobPdnVisitingPlmnList = _TmnxMobPdnVisitingPlmnList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 11),
    _TmnxMobPdnVisitingPlmnList_Type()
)
tmnxMobPdnVisitingPlmnList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnVisitingPlmnList.setStatus("current")


class _TmnxMobPdnBearerGtpuUdpChecksum_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnBearerGtpuUdpChecksum based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnBearerGtpuUdpChecksum_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnBearerGtpuUdpChecksum_Object = MibTableColumn
tmnxMobPdnBearerGtpuUdpChecksum = _TmnxMobPdnBearerGtpuUdpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 12),
    _TmnxMobPdnBearerGtpuUdpChecksum_Type()
)
tmnxMobPdnBearerGtpuUdpChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnBearerGtpuUdpChecksum.setStatus("current")


class _TmnxMobPdnBearerGtpuSeqNumber_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnBearerGtpuSeqNumber based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnBearerGtpuSeqNumber_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnBearerGtpuSeqNumber_Object = MibTableColumn
tmnxMobPdnBearerGtpuSeqNumber = _TmnxMobPdnBearerGtpuSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 13),
    _TmnxMobPdnBearerGtpuSeqNumber_Type()
)
tmnxMobPdnBearerGtpuSeqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnBearerGtpuSeqNumber.setStatus("current")


class _TmnxMobPdnChargingProfHome_Type(TmnxMobChargingProfile):
    """Custom type tmnxMobPdnChargingProfHome based on TmnxMobChargingProfile"""
    defaultValue = 0


_TmnxMobPdnChargingProfHome_Type.__name__ = "TmnxMobChargingProfile"
_TmnxMobPdnChargingProfHome_Object = MibTableColumn
tmnxMobPdnChargingProfHome = _TmnxMobPdnChargingProfHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 15),
    _TmnxMobPdnChargingProfHome_Type()
)
tmnxMobPdnChargingProfHome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChargingProfHome.setStatus("current")


class _TmnxMobPdnChargingProfVisiting_Type(TmnxMobChargingProfile):
    """Custom type tmnxMobPdnChargingProfVisiting based on TmnxMobChargingProfile"""
    defaultValue = 0


_TmnxMobPdnChargingProfVisiting_Type.__name__ = "TmnxMobChargingProfile"
_TmnxMobPdnChargingProfVisiting_Object = MibTableColumn
tmnxMobPdnChargingProfVisiting = _TmnxMobPdnChargingProfVisiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 16),
    _TmnxMobPdnChargingProfVisiting_Type()
)
tmnxMobPdnChargingProfVisiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChargingProfVisiting.setStatus("current")


class _TmnxMobPdnChargingProfRoaming_Type(TmnxMobChargingProfile):
    """Custom type tmnxMobPdnChargingProfRoaming based on TmnxMobChargingProfile"""
    defaultValue = 0


_TmnxMobPdnChargingProfRoaming_Type.__name__ = "TmnxMobChargingProfile"
_TmnxMobPdnChargingProfRoaming_Object = MibTableColumn
tmnxMobPdnChargingProfRoaming = _TmnxMobPdnChargingProfRoaming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 17),
    _TmnxMobPdnChargingProfRoaming_Type()
)
tmnxMobPdnChargingProfRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChargingProfRoaming.setStatus("current")


class _TmnxMobPdnChrgCcIgnoreAny_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnChrgCcIgnoreAny based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnChrgCcIgnoreAny_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnChrgCcIgnoreAny_Object = MibTableColumn
tmnxMobPdnChrgCcIgnoreAny = _TmnxMobPdnChrgCcIgnoreAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 18),
    _TmnxMobPdnChrgCcIgnoreAny_Type()
)
tmnxMobPdnChrgCcIgnoreAny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChrgCcIgnoreAny.setStatus("current")


class _TmnxMobPdnChrgCcIgnoreHome_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnChrgCcIgnoreHome based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnChrgCcIgnoreHome_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnChrgCcIgnoreHome_Object = MibTableColumn
tmnxMobPdnChrgCcIgnoreHome = _TmnxMobPdnChrgCcIgnoreHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 19),
    _TmnxMobPdnChrgCcIgnoreHome_Type()
)
tmnxMobPdnChrgCcIgnoreHome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChrgCcIgnoreHome.setStatus("current")


class _TmnxMobPdnChrgCcIgnoreVisiting_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnChrgCcIgnoreVisiting based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnChrgCcIgnoreVisiting_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnChrgCcIgnoreVisiting_Object = MibTableColumn
tmnxMobPdnChrgCcIgnoreVisiting = _TmnxMobPdnChrgCcIgnoreVisiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 20),
    _TmnxMobPdnChrgCcIgnoreVisiting_Type()
)
tmnxMobPdnChrgCcIgnoreVisiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChrgCcIgnoreVisiting.setStatus("current")


class _TmnxMobPdnChrgCcIgnoreRoaming_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnChrgCcIgnoreRoaming based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnChrgCcIgnoreRoaming_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnChrgCcIgnoreRoaming_Object = MibTableColumn
tmnxMobPdnChrgCcIgnoreRoaming = _TmnxMobPdnChrgCcIgnoreRoaming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 21),
    _TmnxMobPdnChrgCcIgnoreRoaming_Type()
)
tmnxMobPdnChrgCcIgnoreRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChrgCcIgnoreRoaming.setStatus("current")


class _TmnxMobPdnUmtsQosPolName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnUmtsQosPolName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnUmtsQosPolName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnUmtsQosPolName_Object = MibTableColumn
tmnxMobPdnUmtsQosPolName = _TmnxMobPdnUmtsQosPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 22),
    _TmnxMobPdnUmtsQosPolName_Type()
)
tmnxMobPdnUmtsQosPolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnUmtsQosPolName.setStatus("current")


class _TmnxMobPdnChrgCcReject_Type(TruthValue):
    """Custom type tmnxMobPdnChrgCcReject based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnChrgCcReject_Type.__name__ = "TruthValue"
_TmnxMobPdnChrgCcReject_Object = MibTableColumn
tmnxMobPdnChrgCcReject = _TmnxMobPdnChrgCcReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 23),
    _TmnxMobPdnChrgCcReject_Type()
)
tmnxMobPdnChrgCcReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChrgCcReject.setStatus("current")


class _TmnxMobPdnChrgNodeId_Type(DisplayString):
    """Custom type tmnxMobPdnChrgNodeId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMobPdnChrgNodeId_Type.__name__ = "DisplayString"
_TmnxMobPdnChrgNodeId_Object = MibTableColumn
tmnxMobPdnChrgNodeId = _TmnxMobPdnChrgNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 24),
    _TmnxMobPdnChrgNodeId_Type()
)
tmnxMobPdnChrgNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChrgNodeId.setStatus("current")


class _TmnxMobPdnAaGroupIndex_Type(TmnxBsxIsaAaGroupIndexOrZero):
    """Custom type tmnxMobPdnAaGroupIndex based on TmnxBsxIsaAaGroupIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnAaGroupIndex_Type.__name__ = "TmnxBsxIsaAaGroupIndexOrZero"
_TmnxMobPdnAaGroupIndex_Object = MibTableColumn
tmnxMobPdnAaGroupIndex = _TmnxMobPdnAaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 25),
    _TmnxMobPdnAaGroupIndex_Type()
)
tmnxMobPdnAaGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnAaGroupIndex.setStatus("current")


class _TmnxMobPdnAaGrpPartIndex_Type(TmnxBsxAaGrpPartIndex):
    """Custom type tmnxMobPdnAaGrpPartIndex based on TmnxBsxAaGrpPartIndex"""
    defaultValue = 0


_TmnxMobPdnAaGrpPartIndex_Type.__name__ = "TmnxBsxAaGrpPartIndex"
_TmnxMobPdnAaGrpPartIndex_Object = MibTableColumn
tmnxMobPdnAaGrpPartIndex = _TmnxMobPdnAaGrpPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 26),
    _TmnxMobPdnAaGrpPartIndex_Type()
)
tmnxMobPdnAaGrpPartIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnAaGrpPartIndex.setStatus("current")


class _TmnxMobPdnCdrType_Type(TmnxCdrType):
    """Custom type tmnxMobPdnCdrType based on TmnxCdrType"""
    defaultValue = 1


_TmnxMobPdnCdrType_Type.__name__ = "TmnxCdrType"
_TmnxMobPdnCdrType_Object = MibTableColumn
tmnxMobPdnCdrType = _TmnxMobPdnCdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 27),
    _TmnxMobPdnCdrType_Type()
)
tmnxMobPdnCdrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnCdrType.setStatus("current")


class _TmnxMobPdnHttpRedirect_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnHttpRedirect based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnHttpRedirect_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnHttpRedirect_Object = MibTableColumn
tmnxMobPdnHttpRedirect = _TmnxMobPdnHttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 28),
    _TmnxMobPdnHttpRedirect_Type()
)
tmnxMobPdnHttpRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnHttpRedirect.setStatus("current")


class _TmnxMobPdnDefAppProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobPdnDefAppProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnDefAppProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobPdnDefAppProfile_Object = MibTableColumn
tmnxMobPdnDefAppProfile = _TmnxMobPdnDefAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 29),
    _TmnxMobPdnDefAppProfile_Type()
)
tmnxMobPdnDefAppProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnDefAppProfile.setStatus("current")


class _TmnxMobPdnChargingAvpDiag_Type(TmnxCdrDiagnosticAction):
    """Custom type tmnxMobPdnChargingAvpDiag based on TmnxCdrDiagnosticAction"""
    defaultValue = 1


_TmnxMobPdnChargingAvpDiag_Type.__name__ = "TmnxCdrDiagnosticAction"
_TmnxMobPdnChargingAvpDiag_Object = MibTableColumn
tmnxMobPdnChargingAvpDiag = _TmnxMobPdnChargingAvpDiag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 1, 1, 30),
    _TmnxMobPdnChargingAvpDiag_Type()
)
tmnxMobPdnChargingAvpDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnChargingAvpDiag.setStatus("current")
_TmnxMobPdnSigTable_Object = MibTable
tmnxMobPdnSigTable = _TmnxMobPdnSigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxMobPdnSigTable.setStatus("current")
_TmnxMobPdnSigEntry_Object = MibTableRow
tmnxMobPdnSigEntry = _TmnxMobPdnSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnSigEntry.setStatus("current")
_TmnxMobPdnSigLastChanged_Type = TimeStamp
_TmnxMobPdnSigLastChanged_Object = MibTableColumn
tmnxMobPdnSigLastChanged = _TmnxMobPdnSigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 1),
    _TmnxMobPdnSigLastChanged_Type()
)
tmnxMobPdnSigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnSigLastChanged.setStatus("current")


class _TmnxMobPdnSigGtpcProfile_Type(TmnxMobProfName):
    """Custom type tmnxMobPdnSigGtpcProfile based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobPdnSigGtpcProfile_Type.__name__ = "TmnxMobProfName"
_TmnxMobPdnSigGtpcProfile_Object = MibTableColumn
tmnxMobPdnSigGtpcProfile = _TmnxMobPdnSigGtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 2),
    _TmnxMobPdnSigGtpcProfile_Type()
)
tmnxMobPdnSigGtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigGtpcProfile.setStatus("current")


class _TmnxMobPdnSigGtpuProfile_Type(TmnxMobProfName):
    """Custom type tmnxMobPdnSigGtpuProfile based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobPdnSigGtpuProfile_Type.__name__ = "TmnxMobProfName"
_TmnxMobPdnSigGtpuProfile_Object = MibTableColumn
tmnxMobPdnSigGtpuProfile = _TmnxMobPdnSigGtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 3),
    _TmnxMobPdnSigGtpuProfile_Type()
)
tmnxMobPdnSigGtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigGtpuProfile.setStatus("current")


class _TmnxMobPdnSigPmipv6Profile_Type(TmnxMobProfName):
    """Custom type tmnxMobPdnSigPmipv6Profile based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobPdnSigPmipv6Profile_Type.__name__ = "TmnxMobProfName"
_TmnxMobPdnSigPmipv6Profile_Object = MibTableColumn
tmnxMobPdnSigPmipv6Profile = _TmnxMobPdnSigPmipv6Profile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 4),
    _TmnxMobPdnSigPmipv6Profile_Type()
)
tmnxMobPdnSigPmipv6Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigPmipv6Profile.setStatus("current")


class _TmnxMobPdnSigPmipv6RtrAdIntvl_Type(TmnxMobRtrAdvtInterval):
    """Custom type tmnxMobPdnSigPmipv6RtrAdIntvl based on TmnxMobRtrAdvtInterval"""
    defaultValue = 30


_TmnxMobPdnSigPmipv6RtrAdIntvl_Type.__name__ = "TmnxMobRtrAdvtInterval"
_TmnxMobPdnSigPmipv6RtrAdIntvl_Object = MibTableColumn
tmnxMobPdnSigPmipv6RtrAdIntvl = _TmnxMobPdnSigPmipv6RtrAdIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 5),
    _TmnxMobPdnSigPmipv6RtrAdIntvl_Type()
)
tmnxMobPdnSigPmipv6RtrAdIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigPmipv6RtrAdIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnSigPmipv6RtrAdIntvl.setUnits("minutes")


class _TmnxMobPdnSigPmipv6RtrAdLife_Type(TmnxMobRtrAdvtLifeTime):
    """Custom type tmnxMobPdnSigPmipv6RtrAdLife based on TmnxMobRtrAdvtLifeTime"""
    defaultValue = 12


_TmnxMobPdnSigPmipv6RtrAdLife_Type.__name__ = "TmnxMobRtrAdvtLifeTime"
_TmnxMobPdnSigPmipv6RtrAdLife_Object = MibTableColumn
tmnxMobPdnSigPmipv6RtrAdLife = _TmnxMobPdnSigPmipv6RtrAdLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 6),
    _TmnxMobPdnSigPmipv6RtrAdLife_Type()
)
tmnxMobPdnSigPmipv6RtrAdLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigPmipv6RtrAdLife.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnSigPmipv6RtrAdLife.setUnits("hours")


class _TmnxMobPdnSigPmipv6AddrScheme_Type(TmnxMobAddrScheme):
    """Custom type tmnxMobPdnSigPmipv6AddrScheme based on TmnxMobAddrScheme"""
    defaultValue = 2


_TmnxMobPdnSigPmipv6AddrScheme_Type.__name__ = "TmnxMobAddrScheme"
_TmnxMobPdnSigPmipv6AddrScheme_Object = MibTableColumn
tmnxMobPdnSigPmipv6AddrScheme = _TmnxMobPdnSigPmipv6AddrScheme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 7),
    _TmnxMobPdnSigPmipv6AddrScheme_Type()
)
tmnxMobPdnSigPmipv6AddrScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigPmipv6AddrScheme.setStatus("current")


class _TmnxMobPdnSigDiaProfile_Type(TmnxMobProfName):
    """Custom type tmnxMobPdnSigDiaProfile based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobPdnSigDiaProfile_Type.__name__ = "TmnxMobProfName"
_TmnxMobPdnSigDiaProfile_Object = MibTableColumn
tmnxMobPdnSigDiaProfile = _TmnxMobPdnSigDiaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 8),
    _TmnxMobPdnSigDiaProfile_Type()
)
tmnxMobPdnSigDiaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigDiaProfile.setStatus("current")


class _TmnxMobPdnSigDiaOriginRealm_Type(TmnxMobDiaPeerHost):
    """Custom type tmnxMobPdnSigDiaOriginRealm based on TmnxMobDiaPeerHost"""
    defaultHexValue = ""


_TmnxMobPdnSigDiaOriginRealm_Type.__name__ = "TmnxMobDiaPeerHost"
_TmnxMobPdnSigDiaOriginRealm_Object = MibTableColumn
tmnxMobPdnSigDiaOriginRealm = _TmnxMobPdnSigDiaOriginRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 9),
    _TmnxMobPdnSigDiaOriginRealm_Type()
)
tmnxMobPdnSigDiaOriginRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigDiaOriginRealm.setStatus("current")


class _TmnxMobPdnSigDiaOriginHost_Type(TmnxMobDiaPeerHost):
    """Custom type tmnxMobPdnSigDiaOriginHost based on TmnxMobDiaPeerHost"""
    defaultHexValue = ""


_TmnxMobPdnSigDiaOriginHost_Type.__name__ = "TmnxMobDiaPeerHost"
_TmnxMobPdnSigDiaOriginHost_Object = MibTableColumn
tmnxMobPdnSigDiaOriginHost = _TmnxMobPdnSigDiaOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 10),
    _TmnxMobPdnSigDiaOriginHost_Type()
)
tmnxMobPdnSigDiaOriginHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigDiaOriginHost.setStatus("current")


class _TmnxMobPdnSigDefaultIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnSigDefaultIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnSigDefaultIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnSigDefaultIfVRtrId_Object = MibTableColumn
tmnxMobPdnSigDefaultIfVRtrId = _TmnxMobPdnSigDefaultIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 11),
    _TmnxMobPdnSigDefaultIfVRtrId_Type()
)
tmnxMobPdnSigDefaultIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigDefaultIfVRtrId.setStatus("current")


class _TmnxMobPdnSigDefaultIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnSigDefaultIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnSigDefaultIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnSigDefaultIfIndex_Object = MibTableColumn
tmnxMobPdnSigDefaultIfIndex = _TmnxMobPdnSigDefaultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 12),
    _TmnxMobPdnSigDefaultIfIndex_Type()
)
tmnxMobPdnSigDefaultIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigDefaultIfIndex.setStatus("current")


class _TmnxMobPdnSigMIP6AgntInfType_Type(Integer32):
    """Custom type tmnxMobPdnSigMIP6AgntInfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddr", 1),
          ("fqdn", 2))
    )


_TmnxMobPdnSigMIP6AgntInfType_Type.__name__ = "Integer32"
_TmnxMobPdnSigMIP6AgntInfType_Object = MibTableColumn
tmnxMobPdnSigMIP6AgntInfType = _TmnxMobPdnSigMIP6AgntInfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 13),
    _TmnxMobPdnSigMIP6AgntInfType_Type()
)
tmnxMobPdnSigMIP6AgntInfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigMIP6AgntInfType.setStatus("current")


class _TmnxMobPdnSigMIP6AgntInfFqdnType_Type(InetAddressType):
    """Custom type tmnxMobPdnSigMIP6AgntInfFqdnType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnSigMIP6AgntInfFqdnType_Type.__name__ = "InetAddressType"
_TmnxMobPdnSigMIP6AgntInfFqdnType_Object = MibTableColumn
tmnxMobPdnSigMIP6AgntInfFqdnType = _TmnxMobPdnSigMIP6AgntInfFqdnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 14),
    _TmnxMobPdnSigMIP6AgntInfFqdnType_Type()
)
tmnxMobPdnSigMIP6AgntInfFqdnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigMIP6AgntInfFqdnType.setStatus("current")


class _TmnxMobPdnSigMIP6AgntInfFqdn_Type(InetAddress):
    """Custom type tmnxMobPdnSigMIP6AgntInfFqdn based on InetAddress"""
    defaultHexValue = ""


_TmnxMobPdnSigMIP6AgntInfFqdn_Type.__name__ = "InetAddress"
_TmnxMobPdnSigMIP6AgntInfFqdn_Object = MibTableColumn
tmnxMobPdnSigMIP6AgntInfFqdn = _TmnxMobPdnSigMIP6AgntInfFqdn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 15),
    _TmnxMobPdnSigMIP6AgntInfFqdn_Type()
)
tmnxMobPdnSigMIP6AgntInfFqdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigMIP6AgntInfFqdn.setStatus("current")


class _TmnxMobPdnSigMIP6AgntInfRealm_Type(TmnxMobDiaPeerHost):
    """Custom type tmnxMobPdnSigMIP6AgntInfRealm based on TmnxMobDiaPeerHost"""
    defaultHexValue = ""


_TmnxMobPdnSigMIP6AgntInfRealm_Type.__name__ = "TmnxMobDiaPeerHost"
_TmnxMobPdnSigMIP6AgntInfRealm_Object = MibTableColumn
tmnxMobPdnSigMIP6AgntInfRealm = _TmnxMobPdnSigMIP6AgntInfRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 2, 1, 16),
    _TmnxMobPdnSigMIP6AgntInfRealm_Type()
)
tmnxMobPdnSigMIP6AgntInfRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnSigMIP6AgntInfRealm.setStatus("current")
_TmnxMobPdnGxTable_Object = MibTable
tmnxMobPdnGxTable = _TmnxMobPdnGxTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGxTable.setStatus("current")
_TmnxMobPdnGxEntry_Object = MibTableRow
tmnxMobPdnGxEntry = _TmnxMobPdnGxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGxEntry.setStatus("current")
_TmnxMobPdnGxLastChanged_Type = TimeStamp
_TmnxMobPdnGxLastChanged_Object = MibTableColumn
tmnxMobPdnGxLastChanged = _TmnxMobPdnGxLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3, 1, 1),
    _TmnxMobPdnGxLastChanged_Type()
)
tmnxMobPdnGxLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxLastChanged.setStatus("current")


class _TmnxMobPdnGxDiaIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnGxDiaIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnGxDiaIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnGxDiaIfVRtrId_Object = MibTableColumn
tmnxMobPdnGxDiaIfVRtrId = _TmnxMobPdnGxDiaIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3, 1, 2),
    _TmnxMobPdnGxDiaIfVRtrId_Type()
)
tmnxMobPdnGxDiaIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGxDiaIfVRtrId.setStatus("current")


class _TmnxMobPdnGxDiaIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnGxDiaIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnGxDiaIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnGxDiaIfIndex_Object = MibTableColumn
tmnxMobPdnGxDiaIfIndex = _TmnxMobPdnGxDiaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3, 1, 3),
    _TmnxMobPdnGxDiaIfIndex_Type()
)
tmnxMobPdnGxDiaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGxDiaIfIndex.setStatus("current")


class _TmnxMobPdnGxDiaTransTimer_Type(TmnxMobDiaTransTimer):
    """Custom type tmnxMobPdnGxDiaTransTimer based on TmnxMobDiaTransTimer"""
    defaultValue = 5


_TmnxMobPdnGxDiaTransTimer_Type.__name__ = "TmnxMobDiaTransTimer"
_TmnxMobPdnGxDiaTransTimer_Object = MibTableColumn
tmnxMobPdnGxDiaTransTimer = _TmnxMobPdnGxDiaTransTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3, 1, 4),
    _TmnxMobPdnGxDiaTransTimer_Type()
)
tmnxMobPdnGxDiaTransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGxDiaTransTimer.setStatus("current")


class _TmnxMobPdnGxDiaRetryCount_Type(TmnxMobDiaRetryCount):
    """Custom type tmnxMobPdnGxDiaRetryCount based on TmnxMobDiaRetryCount"""
    defaultValue = 3


_TmnxMobPdnGxDiaRetryCount_Type.__name__ = "TmnxMobDiaRetryCount"
_TmnxMobPdnGxDiaRetryCount_Object = MibTableColumn
tmnxMobPdnGxDiaRetryCount = _TmnxMobPdnGxDiaRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3, 1, 5),
    _TmnxMobPdnGxDiaRetryCount_Type()
)
tmnxMobPdnGxDiaRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGxDiaRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnGxDiaRetryCount.setUnits("seconds")


class _TmnxMobPdnGxDefPriDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGxDefPriDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGxDefPriDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGxDefPriDiaPeer_Object = MibTableColumn
tmnxMobPdnGxDefPriDiaPeer = _TmnxMobPdnGxDefPriDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3, 1, 6),
    _TmnxMobPdnGxDefPriDiaPeer_Type()
)
tmnxMobPdnGxDefPriDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGxDefPriDiaPeer.setStatus("current")


class _TmnxMobPdnGxDefSecDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGxDefSecDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGxDefSecDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGxDefSecDiaPeer_Object = MibTableColumn
tmnxMobPdnGxDefSecDiaPeer = _TmnxMobPdnGxDefSecDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 3, 1, 7),
    _TmnxMobPdnGxDefSecDiaPeer_Type()
)
tmnxMobPdnGxDefSecDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGxDefSecDiaPeer.setStatus("current")
_TmnxMobPdnS5Table_Object = MibTable
tmnxMobPdnS5Table = _TmnxMobPdnS5Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS5Table.setStatus("current")
_TmnxMobPdnS5Entry_Object = MibTableRow
tmnxMobPdnS5Entry = _TmnxMobPdnS5Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS5Entry.setStatus("current")
_TmnxMobPdnS5LastChanged_Type = TimeStamp
_TmnxMobPdnS5LastChanged_Object = MibTableColumn
tmnxMobPdnS5LastChanged = _TmnxMobPdnS5LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 1),
    _TmnxMobPdnS5LastChanged_Type()
)
tmnxMobPdnS5LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS5LastChanged.setStatus("current")


class _TmnxMobPdnS5PeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnS5PeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnS5PeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnS5PeerList_Object = MibTableColumn
tmnxMobPdnS5PeerList = _TmnxMobPdnS5PeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 2),
    _TmnxMobPdnS5PeerList_Type()
)
tmnxMobPdnS5PeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS5PeerList.setStatus("current")


class _TmnxMobPdnS5GtpcIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnS5GtpcIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnS5GtpcIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnS5GtpcIfVRtrId_Object = MibTableColumn
tmnxMobPdnS5GtpcIfVRtrId = _TmnxMobPdnS5GtpcIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 3),
    _TmnxMobPdnS5GtpcIfVRtrId_Type()
)
tmnxMobPdnS5GtpcIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS5GtpcIfVRtrId.setStatus("current")


class _TmnxMobPdnS5GtpcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnS5GtpcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnS5GtpcIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnS5GtpcIfIndex_Object = MibTableColumn
tmnxMobPdnS5GtpcIfIndex = _TmnxMobPdnS5GtpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 4),
    _TmnxMobPdnS5GtpcIfIndex_Type()
)
tmnxMobPdnS5GtpcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS5GtpcIfIndex.setStatus("current")


class _TmnxMobPdnS5GtpuIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnS5GtpuIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnS5GtpuIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnS5GtpuIfVRtrId_Object = MibTableColumn
tmnxMobPdnS5GtpuIfVRtrId = _TmnxMobPdnS5GtpuIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 5),
    _TmnxMobPdnS5GtpuIfVRtrId_Type()
)
tmnxMobPdnS5GtpuIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS5GtpuIfVRtrId.setStatus("current")


class _TmnxMobPdnS5GtpuIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnS5GtpuIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnS5GtpuIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnS5GtpuIfIndex_Object = MibTableColumn
tmnxMobPdnS5GtpuIfIndex = _TmnxMobPdnS5GtpuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 6),
    _TmnxMobPdnS5GtpuIfIndex_Type()
)
tmnxMobPdnS5GtpuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS5GtpuIfIndex.setStatus("current")


class _TmnxMobPdnS5GtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnS5GtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnS5GtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnS5GtpcProfile_Object = MibTableColumn
tmnxMobPdnS5GtpcProfile = _TmnxMobPdnS5GtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 7),
    _TmnxMobPdnS5GtpcProfile_Type()
)
tmnxMobPdnS5GtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS5GtpcProfile.setStatus("current")


class _TmnxMobPdnS5GtpuProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnS5GtpuProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnS5GtpuProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnS5GtpuProfile_Object = MibTableColumn
tmnxMobPdnS5GtpuProfile = _TmnxMobPdnS5GtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 8),
    _TmnxMobPdnS5GtpuProfile_Type()
)
tmnxMobPdnS5GtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS5GtpuProfile.setStatus("current")


class _TmnxMobPdnS5DualStackPref_Type(TmnxMobDualStackPref):
    """Custom type tmnxMobPdnS5DualStackPref based on TmnxMobDualStackPref"""
    defaultValue = 3


_TmnxMobPdnS5DualStackPref_Type.__name__ = "TmnxMobDualStackPref"
_TmnxMobPdnS5DualStackPref_Object = MibTableColumn
tmnxMobPdnS5DualStackPref = _TmnxMobPdnS5DualStackPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 4, 1, 9),
    _TmnxMobPdnS5DualStackPref_Type()
)
tmnxMobPdnS5DualStackPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS5DualStackPref.setStatus("current")
_TmnxMobPdnS8Table_Object = MibTable
tmnxMobPdnS8Table = _TmnxMobPdnS8Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS8Table.setStatus("current")
_TmnxMobPdnS8Entry_Object = MibTableRow
tmnxMobPdnS8Entry = _TmnxMobPdnS8Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS8Entry.setStatus("current")
_TmnxMobPdnS8LastChanged_Type = TimeStamp
_TmnxMobPdnS8LastChanged_Object = MibTableColumn
tmnxMobPdnS8LastChanged = _TmnxMobPdnS8LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 1),
    _TmnxMobPdnS8LastChanged_Type()
)
tmnxMobPdnS8LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS8LastChanged.setStatus("current")


class _TmnxMobPdnS8PeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnS8PeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnS8PeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnS8PeerList_Object = MibTableColumn
tmnxMobPdnS8PeerList = _TmnxMobPdnS8PeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 2),
    _TmnxMobPdnS8PeerList_Type()
)
tmnxMobPdnS8PeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS8PeerList.setStatus("current")


class _TmnxMobPdnS8GtpcIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnS8GtpcIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnS8GtpcIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnS8GtpcIfVRtrId_Object = MibTableColumn
tmnxMobPdnS8GtpcIfVRtrId = _TmnxMobPdnS8GtpcIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 3),
    _TmnxMobPdnS8GtpcIfVRtrId_Type()
)
tmnxMobPdnS8GtpcIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS8GtpcIfVRtrId.setStatus("current")


class _TmnxMobPdnS8GtpcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnS8GtpcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnS8GtpcIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnS8GtpcIfIndex_Object = MibTableColumn
tmnxMobPdnS8GtpcIfIndex = _TmnxMobPdnS8GtpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 4),
    _TmnxMobPdnS8GtpcIfIndex_Type()
)
tmnxMobPdnS8GtpcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS8GtpcIfIndex.setStatus("current")


class _TmnxMobPdnS8GtpuIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnS8GtpuIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnS8GtpuIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnS8GtpuIfVRtrId_Object = MibTableColumn
tmnxMobPdnS8GtpuIfVRtrId = _TmnxMobPdnS8GtpuIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 5),
    _TmnxMobPdnS8GtpuIfVRtrId_Type()
)
tmnxMobPdnS8GtpuIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS8GtpuIfVRtrId.setStatus("current")


class _TmnxMobPdnS8GtpuIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnS8GtpuIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnS8GtpuIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnS8GtpuIfIndex_Object = MibTableColumn
tmnxMobPdnS8GtpuIfIndex = _TmnxMobPdnS8GtpuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 6),
    _TmnxMobPdnS8GtpuIfIndex_Type()
)
tmnxMobPdnS8GtpuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS8GtpuIfIndex.setStatus("current")


class _TmnxMobPdnS8GtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnS8GtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnS8GtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnS8GtpcProfile_Object = MibTableColumn
tmnxMobPdnS8GtpcProfile = _TmnxMobPdnS8GtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 7),
    _TmnxMobPdnS8GtpcProfile_Type()
)
tmnxMobPdnS8GtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS8GtpcProfile.setStatus("current")


class _TmnxMobPdnS8GtpuProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnS8GtpuProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnS8GtpuProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnS8GtpuProfile_Object = MibTableColumn
tmnxMobPdnS8GtpuProfile = _TmnxMobPdnS8GtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 8),
    _TmnxMobPdnS8GtpuProfile_Type()
)
tmnxMobPdnS8GtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS8GtpuProfile.setStatus("current")


class _TmnxMobPdnS8DualStackPref_Type(TmnxMobDualStackPref):
    """Custom type tmnxMobPdnS8DualStackPref based on TmnxMobDualStackPref"""
    defaultValue = 3


_TmnxMobPdnS8DualStackPref_Type.__name__ = "TmnxMobDualStackPref"
_TmnxMobPdnS8DualStackPref_Object = MibTableColumn
tmnxMobPdnS8DualStackPref = _TmnxMobPdnS8DualStackPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 5, 1, 9),
    _TmnxMobPdnS8DualStackPref_Type()
)
tmnxMobPdnS8DualStackPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS8DualStackPref.setStatus("current")
_TmnxMobPdnS2aTable_Object = MibTable
tmnxMobPdnS2aTable = _TmnxMobPdnS2aTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS2aTable.setStatus("current")
_TmnxMobPdnS2aEntry_Object = MibTableRow
tmnxMobPdnS2aEntry = _TmnxMobPdnS2aEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS2aEntry.setStatus("current")
_TmnxMobPdnS2aLastChanged_Type = TimeStamp
_TmnxMobPdnS2aLastChanged_Object = MibTableColumn
tmnxMobPdnS2aLastChanged = _TmnxMobPdnS2aLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 6, 1, 1),
    _TmnxMobPdnS2aLastChanged_Type()
)
tmnxMobPdnS2aLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aLastChanged.setStatus("current")


class _TmnxMobPdnS2aPeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnS2aPeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnS2aPeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnS2aPeerList_Object = MibTableColumn
tmnxMobPdnS2aPeerList = _TmnxMobPdnS2aPeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 6, 1, 2),
    _TmnxMobPdnS2aPeerList_Type()
)
tmnxMobPdnS2aPeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerList.setStatus("current")


class _TmnxMobPdnS2aIfPmipv6RtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnS2aIfPmipv6RtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnS2aIfPmipv6RtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnS2aIfPmipv6RtrId_Object = MibTableColumn
tmnxMobPdnS2aIfPmipv6RtrId = _TmnxMobPdnS2aIfPmipv6RtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 6, 1, 3),
    _TmnxMobPdnS2aIfPmipv6RtrId_Type()
)
tmnxMobPdnS2aIfPmipv6RtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aIfPmipv6RtrId.setStatus("current")


class _TmnxMobPdnS2aIfPmipv6Interface_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnS2aIfPmipv6Interface based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnS2aIfPmipv6Interface_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnS2aIfPmipv6Interface_Object = MibTableColumn
tmnxMobPdnS2aIfPmipv6Interface = _TmnxMobPdnS2aIfPmipv6Interface_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 6, 1, 4),
    _TmnxMobPdnS2aIfPmipv6Interface_Type()
)
tmnxMobPdnS2aIfPmipv6Interface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aIfPmipv6Interface.setStatus("current")


class _TmnxMobPdnS2aIfPmipv6Profile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnS2aIfPmipv6Profile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnS2aIfPmipv6Profile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnS2aIfPmipv6Profile_Object = MibTableColumn
tmnxMobPdnS2aIfPmipv6Profile = _TmnxMobPdnS2aIfPmipv6Profile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 6, 1, 5),
    _TmnxMobPdnS2aIfPmipv6Profile_Type()
)
tmnxMobPdnS2aIfPmipv6Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aIfPmipv6Profile.setStatus("current")
_TmnxMobPdnRfTable_Object = MibTable
tmnxMobPdnRfTable = _TmnxMobPdnRfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxMobPdnRfTable.setStatus("current")
_TmnxMobPdnRfEntry_Object = MibTableRow
tmnxMobPdnRfEntry = _TmnxMobPdnRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnRfEntry.setStatus("current")
_TmnxMobPdnRfLastChanged_Type = TimeStamp
_TmnxMobPdnRfLastChanged_Object = MibTableColumn
tmnxMobPdnRfLastChanged = _TmnxMobPdnRfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 1),
    _TmnxMobPdnRfLastChanged_Type()
)
tmnxMobPdnRfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRfLastChanged.setStatus("current")


class _TmnxMobPdnRfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnRfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnRfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnRfVRtrId_Object = MibTableColumn
tmnxMobPdnRfVRtrId = _TmnxMobPdnRfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 2),
    _TmnxMobPdnRfVRtrId_Type()
)
tmnxMobPdnRfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfVRtrId.setStatus("current")


class _TmnxMobPdnRfIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnRfIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnRfIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnRfIfIndex_Object = MibTableColumn
tmnxMobPdnRfIfIndex = _TmnxMobPdnRfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 3),
    _TmnxMobPdnRfIfIndex_Type()
)
tmnxMobPdnRfIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfIfIndex.setStatus("current")


class _TmnxMobPdnRfPriDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnRfPriDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnRfPriDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnRfPriDiaPeer_Object = MibTableColumn
tmnxMobPdnRfPriDiaPeer = _TmnxMobPdnRfPriDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 4),
    _TmnxMobPdnRfPriDiaPeer_Type()
)
tmnxMobPdnRfPriDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfPriDiaPeer.setStatus("current")


class _TmnxMobPdnRfSecDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnRfSecDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnRfSecDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnRfSecDiaPeer_Object = MibTableColumn
tmnxMobPdnRfSecDiaPeer = _TmnxMobPdnRfSecDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 5),
    _TmnxMobPdnRfSecDiaPeer_Type()
)
tmnxMobPdnRfSecDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfSecDiaPeer.setStatus("current")


class _TmnxMobPdnRfAcctIntmInterval_Type(Unsigned32):
    """Custom type tmnxMobPdnRfAcctIntmInterval based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_TmnxMobPdnRfAcctIntmInterval_Type.__name__ = "Unsigned32"
_TmnxMobPdnRfAcctIntmInterval_Object = MibTableColumn
tmnxMobPdnRfAcctIntmInterval = _TmnxMobPdnRfAcctIntmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 6),
    _TmnxMobPdnRfAcctIntmInterval_Type()
)
tmnxMobPdnRfAcctIntmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfAcctIntmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRfAcctIntmInterval.setUnits("seconds")


class _TmnxMobPdnRfApplTxTimer_Type(Unsigned32):
    """Custom type tmnxMobPdnRfApplTxTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TmnxMobPdnRfApplTxTimer_Type.__name__ = "Unsigned32"
_TmnxMobPdnRfApplTxTimer_Object = MibTableColumn
tmnxMobPdnRfApplTxTimer = _TmnxMobPdnRfApplTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 7),
    _TmnxMobPdnRfApplTxTimer_Type()
)
tmnxMobPdnRfApplTxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfApplTxTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRfApplTxTimer.setUnits("seconds")


class _TmnxMobPdnRfRetryCount_Type(TmnxMobDiaRetryCount):
    """Custom type tmnxMobPdnRfRetryCount based on TmnxMobDiaRetryCount"""
    defaultValue = 3


_TmnxMobPdnRfRetryCount_Type.__name__ = "TmnxMobDiaRetryCount"
_TmnxMobPdnRfRetryCount_Object = MibTableColumn
tmnxMobPdnRfRetryCount = _TmnxMobPdnRfRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 8),
    _TmnxMobPdnRfRetryCount_Type()
)
tmnxMobPdnRfRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRfRetryCount.setUnits("seconds")


class _TmnxMobPdnRfChargingGroupID_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnRfChargingGroupID based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnRfChargingGroupID_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnRfChargingGroupID_Object = MibTableColumn
tmnxMobPdnRfChargingGroupID = _TmnxMobPdnRfChargingGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 9),
    _TmnxMobPdnRfChargingGroupID_Type()
)
tmnxMobPdnRfChargingGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfChargingGroupID.setStatus("current")


class _TmnxMobPdnRfOperatorString_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobPdnRfOperatorString based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnRfOperatorString_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobPdnRfOperatorString_Object = MibTableColumn
tmnxMobPdnRfOperatorString = _TmnxMobPdnRfOperatorString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 10),
    _TmnxMobPdnRfOperatorString_Type()
)
tmnxMobPdnRfOperatorString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOperatorString.setStatus("current")


class _TmnxMobPdnRfAcctLevel_Type(TmnxMobRfAcctLevel):
    """Custom type tmnxMobPdnRfAcctLevel based on TmnxMobRfAcctLevel"""
    defaultValue = 2


_TmnxMobPdnRfAcctLevel_Type.__name__ = "TmnxMobRfAcctLevel"
_TmnxMobPdnRfAcctLevel_Object = MibTableColumn
tmnxMobPdnRfAcctLevel = _TmnxMobPdnRfAcctLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 11),
    _TmnxMobPdnRfAcctLevel_Type()
)
tmnxMobPdnRfAcctLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfAcctLevel.setStatus("current")


class _TmnxMobPdnRfNodeId_Type(DisplayString):
    """Custom type tmnxMobPdnRfNodeId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMobPdnRfNodeId_Type.__name__ = "DisplayString"
_TmnxMobPdnRfNodeId_Object = MibTableColumn
tmnxMobPdnRfNodeId = _TmnxMobPdnRfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 12),
    _TmnxMobPdnRfNodeId_Type()
)
tmnxMobPdnRfNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfNodeId.setStatus("current")


class _TmnxMobPdnRfOcFilePrivateInfo_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobPdnRfOcFilePrivateInfo based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnRfOcFilePrivateInfo_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobPdnRfOcFilePrivateInfo_Object = MibTableColumn
tmnxMobPdnRfOcFilePrivateInfo = _TmnxMobPdnRfOcFilePrivateInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 13),
    _TmnxMobPdnRfOcFilePrivateInfo_Type()
)
tmnxMobPdnRfOcFilePrivateInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFilePrivateInfo.setStatus("current")


class _TmnxMobPdnRfOcFileExtension_Type(DisplayString):
    """Custom type tmnxMobPdnRfOcFileExtension based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxMobPdnRfOcFileExtension_Type.__name__ = "DisplayString"
_TmnxMobPdnRfOcFileExtension_Object = MibTableColumn
tmnxMobPdnRfOcFileExtension = _TmnxMobPdnRfOcFileExtension_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 14),
    _TmnxMobPdnRfOcFileExtension_Type()
)
tmnxMobPdnRfOcFileExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFileExtension.setStatus("current")


class _TmnxMobPdnRfOcFileClosureSize_Type(Unsigned32):
    """Custom type tmnxMobPdnRfOcFileClosureSize based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxMobPdnRfOcFileClosureSize_Type.__name__ = "Unsigned32"
_TmnxMobPdnRfOcFileClosureSize_Object = MibTableColumn
tmnxMobPdnRfOcFileClosureSize = _TmnxMobPdnRfOcFileClosureSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 15),
    _TmnxMobPdnRfOcFileClosureSize_Type()
)
tmnxMobPdnRfOcFileClosureSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFileClosureSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFileClosureSize.setUnits("megabytes")


class _TmnxMobPdnRfOcFileClsLifeTime_Type(Unsigned32):
    """Custom type tmnxMobPdnRfOcFileClsLifeTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TmnxMobPdnRfOcFileClsLifeTime_Type.__name__ = "Unsigned32"
_TmnxMobPdnRfOcFileClsLifeTime_Object = MibTableColumn
tmnxMobPdnRfOcFileClsLifeTime = _TmnxMobPdnRfOcFileClsLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 16),
    _TmnxMobPdnRfOcFileClsLifeTime_Type()
)
tmnxMobPdnRfOcFileClsLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFileClsLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFileClsLifeTime.setUnits("hours")


class _TmnxMobPdnRfOcFileClsMaxAcrs_Type(Unsigned32):
    """Custom type tmnxMobPdnRfOcFileClsMaxAcrs based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_TmnxMobPdnRfOcFileClsMaxAcrs_Type.__name__ = "Unsigned32"
_TmnxMobPdnRfOcFileClsMaxAcrs_Object = MibTableColumn
tmnxMobPdnRfOcFileClsMaxAcrs = _TmnxMobPdnRfOcFileClsMaxAcrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 17),
    _TmnxMobPdnRfOcFileClsMaxAcrs_Type()
)
tmnxMobPdnRfOcFileClsMaxAcrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFileClsMaxAcrs.setStatus("current")


class _TmnxMobPdnRfOcFileObsoleteTime_Type(Unsigned32):
    """Custom type tmnxMobPdnRfOcFileObsoleteTime based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TmnxMobPdnRfOcFileObsoleteTime_Type.__name__ = "Unsigned32"
_TmnxMobPdnRfOcFileObsoleteTime_Object = MibTableColumn
tmnxMobPdnRfOcFileObsoleteTime = _TmnxMobPdnRfOcFileObsoleteTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 18),
    _TmnxMobPdnRfOcFileObsoleteTime_Type()
)
tmnxMobPdnRfOcFileObsoleteTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFileObsoleteTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcFileObsoleteTime.setUnits("days")


class _TmnxMobPdnRfOcPrimaryCf_Type(Integer32):
    """Custom type tmnxMobPdnRfOcPrimaryCf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cf1", 1),
          ("cf2", 2),
          ("none", 3))
    )


_TmnxMobPdnRfOcPrimaryCf_Type.__name__ = "Integer32"
_TmnxMobPdnRfOcPrimaryCf_Object = MibTableColumn
tmnxMobPdnRfOcPrimaryCf = _TmnxMobPdnRfOcPrimaryCf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 19),
    _TmnxMobPdnRfOcPrimaryCf_Type()
)
tmnxMobPdnRfOcPrimaryCf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcPrimaryCf.setStatus("current")


class _TmnxMobPdnRfOcCf1State_Type(TruthValue):
    """Custom type tmnxMobPdnRfOcCf1State based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnRfOcCf1State_Type.__name__ = "TruthValue"
_TmnxMobPdnRfOcCf1State_Object = MibTableColumn
tmnxMobPdnRfOcCf1State = _TmnxMobPdnRfOcCf1State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 20),
    _TmnxMobPdnRfOcCf1State_Type()
)
tmnxMobPdnRfOcCf1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcCf1State.setStatus("current")


class _TmnxMobPdnRfOcCf1Limit_Type(Unsigned32):
    """Custom type tmnxMobPdnRfOcCf1Limit based on Unsigned32"""
    defaultValue = 0


_TmnxMobPdnRfOcCf1Limit_Type.__name__ = "Unsigned32"
_TmnxMobPdnRfOcCf1Limit_Object = MibTableColumn
tmnxMobPdnRfOcCf1Limit = _TmnxMobPdnRfOcCf1Limit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 21),
    _TmnxMobPdnRfOcCf1Limit_Type()
)
tmnxMobPdnRfOcCf1Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcCf1Limit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcCf1Limit.setUnits("megabytes")


class _TmnxMobPdnRfOcCf2State_Type(TruthValue):
    """Custom type tmnxMobPdnRfOcCf2State based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnRfOcCf2State_Type.__name__ = "TruthValue"
_TmnxMobPdnRfOcCf2State_Object = MibTableColumn
tmnxMobPdnRfOcCf2State = _TmnxMobPdnRfOcCf2State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 22),
    _TmnxMobPdnRfOcCf2State_Type()
)
tmnxMobPdnRfOcCf2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcCf2State.setStatus("current")


class _TmnxMobPdnRfOcCf2Limit_Type(Unsigned32):
    """Custom type tmnxMobPdnRfOcCf2Limit based on Unsigned32"""
    defaultValue = 0


_TmnxMobPdnRfOcCf2Limit_Type.__name__ = "Unsigned32"
_TmnxMobPdnRfOcCf2Limit_Object = MibTableColumn
tmnxMobPdnRfOcCf2Limit = _TmnxMobPdnRfOcCf2Limit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 23),
    _TmnxMobPdnRfOcCf2Limit_Type()
)
tmnxMobPdnRfOcCf2Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcCf2Limit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRfOcCf2Limit.setUnits("megabytes")


class _TmnxMobPdnRfSuppVendorAvps_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnRfSuppVendorAvps based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnRfSuppVendorAvps_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnRfSuppVendorAvps_Object = MibTableColumn
tmnxMobPdnRfSuppVendorAvps = _TmnxMobPdnRfSuppVendorAvps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 7, 1, 24),
    _TmnxMobPdnRfSuppVendorAvps_Type()
)
tmnxMobPdnRfSuppVendorAvps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRfSuppVendorAvps.setStatus("current")
_TmnxMobPdnPccBasePolTable_Object = MibTable
tmnxMobPdnPccBasePolTable = _TmnxMobPdnPccBasePolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxMobPdnPccBasePolTable.setStatus("current")
_TmnxMobPdnPccBasePolEntry_Object = MibTableRow
tmnxMobPdnPccBasePolEntry = _TmnxMobPdnPccBasePolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 8, 1)
)
tmnxMobPdnPccBasePolEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPccIpCanType"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseName"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnPccBasePolEntry.setStatus("current")
_TmnxMobPdnPccIpCanType_Type = TmnxMobIpCanType
_TmnxMobPdnPccIpCanType_Object = MibTableColumn
tmnxMobPdnPccIpCanType = _TmnxMobPdnPccIpCanType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 8, 1, 1),
    _TmnxMobPdnPccIpCanType_Type()
)
tmnxMobPdnPccIpCanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnPccIpCanType.setStatus("current")
_TmnxMobPdnPccBasePolRowStatus_Type = RowStatus
_TmnxMobPdnPccBasePolRowStatus_Object = MibTableColumn
tmnxMobPdnPccBasePolRowStatus = _TmnxMobPdnPccBasePolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 8, 1, 2),
    _TmnxMobPdnPccBasePolRowStatus_Type()
)
tmnxMobPdnPccBasePolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnPccBasePolRowStatus.setStatus("current")
_TmnxMobPdnApnTable_Object = MibTable
tmnxMobPdnApnTable = _TmnxMobPdnApnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnTable.setStatus("current")
_TmnxMobPdnApnEntry_Object = MibTableRow
tmnxMobPdnApnEntry = _TmnxMobPdnApnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1)
)
tmnxMobPdnApnEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnName"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnEntry.setStatus("current")
_TmnxMobPdnApnName_Type = TmnxMobApn
_TmnxMobPdnApnName_Object = MibTableColumn
tmnxMobPdnApnName = _TmnxMobPdnApnName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 1),
    _TmnxMobPdnApnName_Type()
)
tmnxMobPdnApnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnApnName.setStatus("current")
_TmnxMobPdnApnRowStatus_Type = RowStatus
_TmnxMobPdnApnRowStatus_Object = MibTableColumn
tmnxMobPdnApnRowStatus = _TmnxMobPdnApnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 2),
    _TmnxMobPdnApnRowStatus_Type()
)
tmnxMobPdnApnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnRowStatus.setStatus("current")
_TmnxMobPdnApnLastChanged_Type = TimeStamp
_TmnxMobPdnApnLastChanged_Object = MibTableColumn
tmnxMobPdnApnLastChanged = _TmnxMobPdnApnLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 3),
    _TmnxMobPdnApnLastChanged_Type()
)
tmnxMobPdnApnLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnLastChanged.setStatus("current")


class _TmnxMobPdnApnDescription_Type(TItemDescription):
    """Custom type tmnxMobPdnApnDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobPdnApnDescription_Type.__name__ = "TItemDescription"
_TmnxMobPdnApnDescription_Object = MibTableColumn
tmnxMobPdnApnDescription = _TmnxMobPdnApnDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 4),
    _TmnxMobPdnApnDescription_Type()
)
tmnxMobPdnApnDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDescription.setStatus("current")


class _TmnxMobPdnApnAdminState_Type(TmnxAdminState):
    """Custom type tmnxMobPdnApnAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxMobPdnApnAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMobPdnApnAdminState_Object = MibTableColumn
tmnxMobPdnApnAdminState = _TmnxMobPdnApnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 5),
    _TmnxMobPdnApnAdminState_Type()
)
tmnxMobPdnApnAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAdminState.setStatus("current")
_TmnxMobPdnApnOperState_Type = TmnxOperState
_TmnxMobPdnApnOperState_Object = MibTableColumn
tmnxMobPdnApnOperState = _TmnxMobPdnApnOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 6),
    _TmnxMobPdnApnOperState_Type()
)
tmnxMobPdnApnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnOperState.setStatus("current")


class _TmnxMobPdnApnGracefulShutTimeout_Type(Unsigned32):
    """Custom type tmnxMobPdnApnGracefulShutTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_TmnxMobPdnApnGracefulShutTimeout_Type.__name__ = "Unsigned32"
_TmnxMobPdnApnGracefulShutTimeout_Object = MibTableColumn
tmnxMobPdnApnGracefulShutTimeout = _TmnxMobPdnApnGracefulShutTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 7),
    _TmnxMobPdnApnGracefulShutTimeout_Type()
)
tmnxMobPdnApnGracefulShutTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnGracefulShutTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnApnGracefulShutTimeout.setUnits("minutes")


class _TmnxMobPdnApnType_Type(Integer32):
    """Custom type tmnxMobPdnApnType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("real", 1),
          ("virtual", 2))
    )


_TmnxMobPdnApnType_Type.__name__ = "Integer32"
_TmnxMobPdnApnType_Object = MibTableColumn
tmnxMobPdnApnType = _TmnxMobPdnApnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 8),
    _TmnxMobPdnApnType_Type()
)
tmnxMobPdnApnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnType.setStatus("current")


class _TmnxMobPdnApnVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnApnVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnApnVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnApnVRtrId_Object = MibTableColumn
tmnxMobPdnApnVRtrId = _TmnxMobPdnApnVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 9),
    _TmnxMobPdnApnVRtrId_Type()
)
tmnxMobPdnApnVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnVRtrId.setStatus("current")


class _TmnxMobPdnApnVirtualApnName_Type(TmnxMobApnOrZero):
    """Custom type tmnxMobPdnApnVirtualApnName based on TmnxMobApnOrZero"""
    defaultHexValue = ""


_TmnxMobPdnApnVirtualApnName_Type.__name__ = "TmnxMobApnOrZero"
_TmnxMobPdnApnVirtualApnName_Object = MibTableColumn
tmnxMobPdnApnVirtualApnName = _TmnxMobPdnApnVirtualApnName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 10),
    _TmnxMobPdnApnVirtualApnName_Type()
)
tmnxMobPdnApnVirtualApnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnVirtualApnName.setStatus("current")


class _TmnxMobPdnApnPdnTypeIpv4_Type(TruthValue):
    """Custom type tmnxMobPdnApnPdnTypeIpv4 based on TruthValue"""
    defaultValue = 1


_TmnxMobPdnApnPdnTypeIpv4_Type.__name__ = "TruthValue"
_TmnxMobPdnApnPdnTypeIpv4_Object = MibTableColumn
tmnxMobPdnApnPdnTypeIpv4 = _TmnxMobPdnApnPdnTypeIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 11),
    _TmnxMobPdnApnPdnTypeIpv4_Type()
)
tmnxMobPdnApnPdnTypeIpv4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPdnTypeIpv4.setStatus("current")


class _TmnxMobPdnApnPdnTypeIpv6_Type(TruthValue):
    """Custom type tmnxMobPdnApnPdnTypeIpv6 based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnPdnTypeIpv6_Type.__name__ = "TruthValue"
_TmnxMobPdnApnPdnTypeIpv6_Object = MibTableColumn
tmnxMobPdnApnPdnTypeIpv6 = _TmnxMobPdnApnPdnTypeIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 12),
    _TmnxMobPdnApnPdnTypeIpv6_Type()
)
tmnxMobPdnApnPdnTypeIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPdnTypeIpv6.setStatus("current")


class _TmnxMobPdnApnPdnTypeIpv4v6_Type(TruthValue):
    """Custom type tmnxMobPdnApnPdnTypeIpv4v6 based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnPdnTypeIpv4v6_Type.__name__ = "TruthValue"
_TmnxMobPdnApnPdnTypeIpv4v6_Object = MibTableColumn
tmnxMobPdnApnPdnTypeIpv4v6 = _TmnxMobPdnApnPdnTypeIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 13),
    _TmnxMobPdnApnPdnTypeIpv4v6_Type()
)
tmnxMobPdnApnPdnTypeIpv4v6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPdnTypeIpv4v6.setStatus("current")


class _TmnxMobPdnApnPdnAllocType_Type(Integer32):
    """Custom type tmnxMobPdnApnPdnAllocType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("ranSignaling", 2))
    )


_TmnxMobPdnApnPdnAllocType_Type.__name__ = "Integer32"
_TmnxMobPdnApnPdnAllocType_Object = MibTableColumn
tmnxMobPdnApnPdnAllocType = _TmnxMobPdnApnPdnAllocType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 14),
    _TmnxMobPdnApnPdnAllocType_Type()
)
tmnxMobPdnApnPdnAllocType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPdnAllocType.setStatus("current")


class _TmnxMobPdnApnPdnRestrictionType_Type(Integer32):
    """Custom type tmnxMobPdnApnPdnRestrictionType based on Integer32"""
    defaultValue = 0

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
        *(("any", 0),
          ("public1", 1),
          ("public2", 2),
          ("private1", 3),
          ("private2", 4))
    )


_TmnxMobPdnApnPdnRestrictionType_Type.__name__ = "Integer32"
_TmnxMobPdnApnPdnRestrictionType_Object = MibTableColumn
tmnxMobPdnApnPdnRestrictionType = _TmnxMobPdnApnPdnRestrictionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 15),
    _TmnxMobPdnApnPdnRestrictionType_Type()
)
tmnxMobPdnApnPdnRestrictionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPdnRestrictionType.setStatus("current")


class _TmnxMobPdnApnAllowMultiplePdns_Type(TruthValue):
    """Custom type tmnxMobPdnApnAllowMultiplePdns based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnAllowMultiplePdns_Type.__name__ = "TruthValue"
_TmnxMobPdnApnAllowMultiplePdns_Object = MibTableColumn
tmnxMobPdnApnAllowMultiplePdns = _TmnxMobPdnApnAllowMultiplePdns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 16),
    _TmnxMobPdnApnAllowMultiplePdns_Type()
)
tmnxMobPdnApnAllowMultiplePdns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAllowMultiplePdns.setStatus("current")


class _TmnxMobPdnApnSelectSubscribed_Type(TruthValue):
    """Custom type tmnxMobPdnApnSelectSubscribed based on TruthValue"""
    defaultValue = 1


_TmnxMobPdnApnSelectSubscribed_Type.__name__ = "TruthValue"
_TmnxMobPdnApnSelectSubscribed_Object = MibTableColumn
tmnxMobPdnApnSelectSubscribed = _TmnxMobPdnApnSelectSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 17),
    _TmnxMobPdnApnSelectSubscribed_Type()
)
tmnxMobPdnApnSelectSubscribed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnSelectSubscribed.setStatus("current")


class _TmnxMobPdnApnSelectMsProvided_Type(TruthValue):
    """Custom type tmnxMobPdnApnSelectMsProvided based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnSelectMsProvided_Type.__name__ = "TruthValue"
_TmnxMobPdnApnSelectMsProvided_Object = MibTableColumn
tmnxMobPdnApnSelectMsProvided = _TmnxMobPdnApnSelectMsProvided_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 18),
    _TmnxMobPdnApnSelectMsProvided_Type()
)
tmnxMobPdnApnSelectMsProvided.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnSelectMsProvided.setStatus("current")


class _TmnxMobPdnApnSelectNwProvided_Type(TruthValue):
    """Custom type tmnxMobPdnApnSelectNwProvided based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnSelectNwProvided_Type.__name__ = "TruthValue"
_TmnxMobPdnApnSelectNwProvided_Object = MibTableColumn
tmnxMobPdnApnSelectNwProvided = _TmnxMobPdnApnSelectNwProvided_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 19),
    _TmnxMobPdnApnSelectNwProvided_Type()
)
tmnxMobPdnApnSelectNwProvided.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnSelectNwProvided.setStatus("current")


class _TmnxMobPdnApnIpAllocLocalPool_Type(TruthValue):
    """Custom type tmnxMobPdnApnIpAllocLocalPool based on TruthValue"""
    defaultValue = 1


_TmnxMobPdnApnIpAllocLocalPool_Type.__name__ = "TruthValue"
_TmnxMobPdnApnIpAllocLocalPool_Object = MibTableColumn
tmnxMobPdnApnIpAllocLocalPool = _TmnxMobPdnApnIpAllocLocalPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 20),
    _TmnxMobPdnApnIpAllocLocalPool_Type()
)
tmnxMobPdnApnIpAllocLocalPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpAllocLocalPool.setStatus("current")


class _TmnxMobPdnApnIpAllocHssStatic_Type(TruthValue):
    """Custom type tmnxMobPdnApnIpAllocHssStatic based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnIpAllocHssStatic_Type.__name__ = "TruthValue"
_TmnxMobPdnApnIpAllocHssStatic_Object = MibTableColumn
tmnxMobPdnApnIpAllocHssStatic = _TmnxMobPdnApnIpAllocHssStatic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 21),
    _TmnxMobPdnApnIpAllocHssStatic_Type()
)
tmnxMobPdnApnIpAllocHssStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpAllocHssStatic.setStatus("current")


class _TmnxMobPdnApnIpAllocAaa_Type(TruthValue):
    """Custom type tmnxMobPdnApnIpAllocAaa based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnIpAllocAaa_Type.__name__ = "TruthValue"
_TmnxMobPdnApnIpAllocAaa_Object = MibTableColumn
tmnxMobPdnApnIpAllocAaa = _TmnxMobPdnApnIpAllocAaa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 22),
    _TmnxMobPdnApnIpAllocAaa_Type()
)
tmnxMobPdnApnIpAllocAaa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpAllocAaa.setStatus("current")


class _TmnxMobPdnApnIpAllocDhcpProxy_Type(TruthValue):
    """Custom type tmnxMobPdnApnIpAllocDhcpProxy based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnIpAllocDhcpProxy_Type.__name__ = "TruthValue"
_TmnxMobPdnApnIpAllocDhcpProxy_Object = MibTableColumn
tmnxMobPdnApnIpAllocDhcpProxy = _TmnxMobPdnApnIpAllocDhcpProxy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 23),
    _TmnxMobPdnApnIpAllocDhcpProxy_Type()
)
tmnxMobPdnApnIpAllocDhcpProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpAllocDhcpProxy.setStatus("current")


class _TmnxMobPdnApnIpAllocDhcpRelay_Type(TruthValue):
    """Custom type tmnxMobPdnApnIpAllocDhcpRelay based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnIpAllocDhcpRelay_Type.__name__ = "TruthValue"
_TmnxMobPdnApnIpAllocDhcpRelay_Object = MibTableColumn
tmnxMobPdnApnIpAllocDhcpRelay = _TmnxMobPdnApnIpAllocDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 24),
    _TmnxMobPdnApnIpAllocDhcpRelay_Type()
)
tmnxMobPdnApnIpAllocDhcpRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpAllocDhcpRelay.setStatus("current")


class _TmnxMobPdnApnIpAllocDhcpServer_Type(TruthValue):
    """Custom type tmnxMobPdnApnIpAllocDhcpServer based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnIpAllocDhcpServer_Type.__name__ = "TruthValue"
_TmnxMobPdnApnIpAllocDhcpServer_Object = MibTableColumn
tmnxMobPdnApnIpAllocDhcpServer = _TmnxMobPdnApnIpAllocDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 25),
    _TmnxMobPdnApnIpAllocDhcpServer_Type()
)
tmnxMobPdnApnIpAllocDhcpServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpAllocDhcpServer.setStatus("current")


class _TmnxMobPdnApnPcrfDynamicPcc_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobPdnApnPcrfDynamicPcc based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 2


_TmnxMobPdnApnPcrfDynamicPcc_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobPdnApnPcrfDynamicPcc_Object = MibTableColumn
tmnxMobPdnApnPcrfDynamicPcc = _TmnxMobPdnApnPcrfDynamicPcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 26),
    _TmnxMobPdnApnPcrfDynamicPcc_Type()
)
tmnxMobPdnApnPcrfDynamicPcc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcrfDynamicPcc.setStatus("current")


class _TmnxMobPdnApnPcrfPriDiameterPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnPcrfPriDiameterPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnPcrfPriDiameterPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnPcrfPriDiameterPeer_Object = MibTableColumn
tmnxMobPdnApnPcrfPriDiameterPeer = _TmnxMobPdnApnPcrfPriDiameterPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 27),
    _TmnxMobPdnApnPcrfPriDiameterPeer_Type()
)
tmnxMobPdnApnPcrfPriDiameterPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcrfPriDiameterPeer.setStatus("current")


class _TmnxMobPdnApnPcrfSecDiameterPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnPcrfSecDiameterPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnPcrfSecDiameterPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnPcrfSecDiameterPeer_Object = MibTableColumn
tmnxMobPdnApnPcrfSecDiameterPeer = _TmnxMobPdnApnPcrfSecDiameterPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 28),
    _TmnxMobPdnApnPcrfSecDiameterPeer_Type()
)
tmnxMobPdnApnPcrfSecDiameterPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcrfSecDiameterPeer.setStatus("current")


class _TmnxMobPdnApnUplinkQciPolName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnUplinkQciPolName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnUplinkQciPolName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnUplinkQciPolName_Object = MibTableColumn
tmnxMobPdnApnUplinkQciPolName = _TmnxMobPdnApnUplinkQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 29),
    _TmnxMobPdnApnUplinkQciPolName_Type()
)
tmnxMobPdnApnUplinkQciPolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnUplinkQciPolName.setStatus("current")


class _TmnxMobPdnApnDownlinkQciPolName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnDownlinkQciPolName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnDownlinkQciPolName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnDownlinkQciPolName_Object = MibTableColumn
tmnxMobPdnApnDownlinkQciPolName = _TmnxMobPdnApnDownlinkQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 30),
    _TmnxMobPdnApnDownlinkQciPolName_Type()
)
tmnxMobPdnApnDownlinkQciPolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDownlinkQciPolName.setStatus("current")


class _TmnxMobPdnApnAggrRateUplink_Type(TmnxMobProfMbrRate):
    """Custom type tmnxMobPdnApnAggrRateUplink based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxMobPdnApnAggrRateUplink_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxMobPdnApnAggrRateUplink_Object = MibTableColumn
tmnxMobPdnApnAggrRateUplink = _TmnxMobPdnApnAggrRateUplink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 31),
    _TmnxMobPdnApnAggrRateUplink_Type()
)
tmnxMobPdnApnAggrRateUplink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAggrRateUplink.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAggrRateUplink.setUnits("kbps")


class _TmnxMobPdnApnAggrRateDownlink_Type(TmnxMobProfMbrRate):
    """Custom type tmnxMobPdnApnAggrRateDownlink based on TmnxMobProfMbrRate"""
    defaultValue = 0


_TmnxMobPdnApnAggrRateDownlink_Type.__name__ = "TmnxMobProfMbrRate"
_TmnxMobPdnApnAggrRateDownlink_Object = MibTableColumn
tmnxMobPdnApnAggrRateDownlink = _TmnxMobPdnApnAggrRateDownlink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 32),
    _TmnxMobPdnApnAggrRateDownlink_Type()
)
tmnxMobPdnApnAggrRateDownlink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAggrRateDownlink.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAggrRateDownlink.setUnits("kbps")


class _TmnxMobPdnApnIdleTimeout_Type(Unsigned32):
    """Custom type tmnxMobPdnApnIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 3600),
    )


_TmnxMobPdnApnIdleTimeout_Type.__name__ = "Unsigned32"
_TmnxMobPdnApnIdleTimeout_Object = MibTableColumn
tmnxMobPdnApnIdleTimeout = _TmnxMobPdnApnIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 33),
    _TmnxMobPdnApnIdleTimeout_Type()
)
tmnxMobPdnApnIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIdleTimeout.setUnits("seconds")


class _TmnxMobPdnApnSessionTimeout_Type(Unsigned32):
    """Custom type tmnxMobPdnApnSessionTimeout based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1800, 86400),
    )


_TmnxMobPdnApnSessionTimeout_Type.__name__ = "Unsigned32"
_TmnxMobPdnApnSessionTimeout_Object = MibTableColumn
tmnxMobPdnApnSessionTimeout = _TmnxMobPdnApnSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 34),
    _TmnxMobPdnApnSessionTimeout_Type()
)
tmnxMobPdnApnSessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnApnSessionTimeout.setUnits("seconds")


class _TmnxMobPdnApnRejectForeignSub_Type(TruthValue):
    """Custom type tmnxMobPdnApnRejectForeignSub based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnRejectForeignSub_Type.__name__ = "TruthValue"
_TmnxMobPdnApnRejectForeignSub_Object = MibTableColumn
tmnxMobPdnApnRejectForeignSub = _TmnxMobPdnApnRejectForeignSub_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 35),
    _TmnxMobPdnApnRejectForeignSub_Type()
)
tmnxMobPdnApnRejectForeignSub.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnRejectForeignSub.setStatus("current")


class _TmnxMobPdnApnBlockedPlmnList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnBlockedPlmnList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnBlockedPlmnList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnBlockedPlmnList_Object = MibTableColumn
tmnxMobPdnApnBlockedPlmnList = _TmnxMobPdnApnBlockedPlmnList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 36),
    _TmnxMobPdnApnBlockedPlmnList_Type()
)
tmnxMobPdnApnBlockedPlmnList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnBlockedPlmnList.setStatus("current")


class _TmnxMobPdnApnUliReporting_Type(TruthValue):
    """Custom type tmnxMobPdnApnUliReporting based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnUliReporting_Type.__name__ = "TruthValue"
_TmnxMobPdnApnUliReporting_Object = MibTableColumn
tmnxMobPdnApnUliReporting = _TmnxMobPdnApnUliReporting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 37),
    _TmnxMobPdnApnUliReporting_Type()
)
tmnxMobPdnApnUliReporting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnUliReporting.setStatus("current")


class _TmnxMobPdnApnUmtsQosPolName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnUmtsQosPolName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnUmtsQosPolName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnUmtsQosPolName_Object = MibTableColumn
tmnxMobPdnApnUmtsQosPolName = _TmnxMobPdnApnUmtsQosPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 38),
    _TmnxMobPdnApnUmtsQosPolName_Type()
)
tmnxMobPdnApnUmtsQosPolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnUmtsQosPolName.setStatus("current")


class _TmnxMobPdnApnPcrfDynPccFHSession_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnApnPcrfDynPccFHSession based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnApnPcrfDynPccFHSession_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnApnPcrfDynPccFHSession_Object = MibTableColumn
tmnxMobPdnApnPcrfDynPccFHSession = _TmnxMobPdnApnPcrfDynPccFHSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 9, 1, 39),
    _TmnxMobPdnApnPcrfDynPccFHSession_Type()
)
tmnxMobPdnApnPcrfDynPccFHSession.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcrfDynPccFHSession.setStatus("current")
_TmnxMobPdnApnExtTable_Object = MibTable
tmnxMobPdnApnExtTable = _TmnxMobPdnApnExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnExtTable.setStatus("current")
_TmnxMobPdnApnExtEntry_Object = MibTableRow
tmnxMobPdnApnExtEntry = _TmnxMobPdnApnExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnExtEntry.setStatus("current")
_TmnxMobPdnApnExtLastChanged_Type = TimeStamp
_TmnxMobPdnApnExtLastChanged_Object = MibTableColumn
tmnxMobPdnApnExtLastChanged = _TmnxMobPdnApnExtLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 1),
    _TmnxMobPdnApnExtLastChanged_Type()
)
tmnxMobPdnApnExtLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnExtLastChanged.setStatus("current")


class _TmnxMobPdnApnDnsServerV4AddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnDnsServerV4AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnDnsServerV4AddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnDnsServerV4AddrType_Object = MibTableColumn
tmnxMobPdnApnDnsServerV4AddrType = _TmnxMobPdnApnDnsServerV4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 2),
    _TmnxMobPdnApnDnsServerV4AddrType_Type()
)
tmnxMobPdnApnDnsServerV4AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDnsServerV4AddrType.setStatus("current")


class _TmnxMobPdnApnDnsServerV4Addr_Type(InetAddress):
    """Custom type tmnxMobPdnApnDnsServerV4Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnApnDnsServerV4Addr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnDnsServerV4Addr_Object = MibTableColumn
tmnxMobPdnApnDnsServerV4Addr = _TmnxMobPdnApnDnsServerV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 3),
    _TmnxMobPdnApnDnsServerV4Addr_Type()
)
tmnxMobPdnApnDnsServerV4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDnsServerV4Addr.setStatus("current")


class _TmnxMobPdnApnDnsServerV6AddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnDnsServerV6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnDnsServerV6AddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnDnsServerV6AddrType_Object = MibTableColumn
tmnxMobPdnApnDnsServerV6AddrType = _TmnxMobPdnApnDnsServerV6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 4),
    _TmnxMobPdnApnDnsServerV6AddrType_Type()
)
tmnxMobPdnApnDnsServerV6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDnsServerV6AddrType.setStatus("current")


class _TmnxMobPdnApnDnsServerV6Addr_Type(InetAddress):
    """Custom type tmnxMobPdnApnDnsServerV6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnApnDnsServerV6Addr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnDnsServerV6Addr_Object = MibTableColumn
tmnxMobPdnApnDnsServerV6Addr = _TmnxMobPdnApnDnsServerV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 5),
    _TmnxMobPdnApnDnsServerV6Addr_Type()
)
tmnxMobPdnApnDnsServerV6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDnsServerV6Addr.setStatus("current")


class _TmnxMobPdnApnDhcpRelayV4RouterId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnApnDhcpRelayV4RouterId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnApnDhcpRelayV4RouterId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnApnDhcpRelayV4RouterId_Object = MibTableColumn
tmnxMobPdnApnDhcpRelayV4RouterId = _TmnxMobPdnApnDhcpRelayV4RouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 6),
    _TmnxMobPdnApnDhcpRelayV4RouterId_Type()
)
tmnxMobPdnApnDhcpRelayV4RouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpRelayV4RouterId.setStatus("current")


class _TmnxMobPdnApnDhcpRlyV4GiAddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnDhcpRlyV4GiAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnDhcpRlyV4GiAddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnDhcpRlyV4GiAddrType_Object = MibTableColumn
tmnxMobPdnApnDhcpRlyV4GiAddrType = _TmnxMobPdnApnDhcpRlyV4GiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 7),
    _TmnxMobPdnApnDhcpRlyV4GiAddrType_Type()
)
tmnxMobPdnApnDhcpRlyV4GiAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpRlyV4GiAddrType.setStatus("current")


class _TmnxMobPdnApnDhcpRelayV4GiAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnDhcpRelayV4GiAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnApnDhcpRelayV4GiAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnDhcpRelayV4GiAddr_Object = MibTableColumn
tmnxMobPdnApnDhcpRelayV4GiAddr = _TmnxMobPdnApnDhcpRelayV4GiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 8),
    _TmnxMobPdnApnDhcpRelayV4GiAddr_Type()
)
tmnxMobPdnApnDhcpRelayV4GiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpRelayV4GiAddr.setStatus("current")


class _TmnxMobPdnApnDhcpRelayV6RouterId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnApnDhcpRelayV6RouterId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnApnDhcpRelayV6RouterId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnApnDhcpRelayV6RouterId_Object = MibTableColumn
tmnxMobPdnApnDhcpRelayV6RouterId = _TmnxMobPdnApnDhcpRelayV6RouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 9),
    _TmnxMobPdnApnDhcpRelayV6RouterId_Type()
)
tmnxMobPdnApnDhcpRelayV6RouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpRelayV6RouterId.setStatus("current")


class _TmnxMobPdnApnDhcpRlyV6GiAddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnDhcpRlyV6GiAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnDhcpRlyV6GiAddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnDhcpRlyV6GiAddrType_Object = MibTableColumn
tmnxMobPdnApnDhcpRlyV6GiAddrType = _TmnxMobPdnApnDhcpRlyV6GiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 10),
    _TmnxMobPdnApnDhcpRlyV6GiAddrType_Type()
)
tmnxMobPdnApnDhcpRlyV6GiAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpRlyV6GiAddrType.setStatus("current")


class _TmnxMobPdnApnDhcpRelayV6GiAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnDhcpRelayV6GiAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnApnDhcpRelayV6GiAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnDhcpRelayV6GiAddr_Object = MibTableColumn
tmnxMobPdnApnDhcpRelayV6GiAddr = _TmnxMobPdnApnDhcpRelayV6GiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 11),
    _TmnxMobPdnApnDhcpRelayV6GiAddr_Type()
)
tmnxMobPdnApnDhcpRelayV6GiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpRelayV6GiAddr.setStatus("current")


class _TmnxMobPdnApnDhcpProxyV4RouterId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnApnDhcpProxyV4RouterId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnApnDhcpProxyV4RouterId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnApnDhcpProxyV4RouterId_Object = MibTableColumn
tmnxMobPdnApnDhcpProxyV4RouterId = _TmnxMobPdnApnDhcpProxyV4RouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 12),
    _TmnxMobPdnApnDhcpProxyV4RouterId_Type()
)
tmnxMobPdnApnDhcpProxyV4RouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpProxyV4RouterId.setStatus("current")


class _TmnxMobPdnApnDhcpPxyV4GiAddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnDhcpPxyV4GiAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnDhcpPxyV4GiAddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnDhcpPxyV4GiAddrType_Object = MibTableColumn
tmnxMobPdnApnDhcpPxyV4GiAddrType = _TmnxMobPdnApnDhcpPxyV4GiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 13),
    _TmnxMobPdnApnDhcpPxyV4GiAddrType_Type()
)
tmnxMobPdnApnDhcpPxyV4GiAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpPxyV4GiAddrType.setStatus("current")


class _TmnxMobPdnApnDhcpProxyV4GiAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnDhcpProxyV4GiAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnApnDhcpProxyV4GiAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnDhcpProxyV4GiAddr_Object = MibTableColumn
tmnxMobPdnApnDhcpProxyV4GiAddr = _TmnxMobPdnApnDhcpProxyV4GiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 14),
    _TmnxMobPdnApnDhcpProxyV4GiAddr_Type()
)
tmnxMobPdnApnDhcpProxyV4GiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpProxyV4GiAddr.setStatus("current")


class _TmnxMobPdnApnDhcpProxyV6RouterId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnApnDhcpProxyV6RouterId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnApnDhcpProxyV6RouterId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnApnDhcpProxyV6RouterId_Object = MibTableColumn
tmnxMobPdnApnDhcpProxyV6RouterId = _TmnxMobPdnApnDhcpProxyV6RouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 15),
    _TmnxMobPdnApnDhcpProxyV6RouterId_Type()
)
tmnxMobPdnApnDhcpProxyV6RouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpProxyV6RouterId.setStatus("current")


class _TmnxMobPdnApnDhcpPxyV6GiAddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnDhcpPxyV6GiAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnDhcpPxyV6GiAddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnDhcpPxyV6GiAddrType_Object = MibTableColumn
tmnxMobPdnApnDhcpPxyV6GiAddrType = _TmnxMobPdnApnDhcpPxyV6GiAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 16),
    _TmnxMobPdnApnDhcpPxyV6GiAddrType_Type()
)
tmnxMobPdnApnDhcpPxyV6GiAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpPxyV6GiAddrType.setStatus("current")


class _TmnxMobPdnApnDhcpProxyV6GiAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnDhcpProxyV6GiAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnApnDhcpProxyV6GiAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnDhcpProxyV6GiAddr_Object = MibTableColumn
tmnxMobPdnApnDhcpProxyV6GiAddr = _TmnxMobPdnApnDhcpProxyV6GiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 17),
    _TmnxMobPdnApnDhcpProxyV6GiAddr_Type()
)
tmnxMobPdnApnDhcpProxyV6GiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDhcpProxyV6GiAddr.setStatus("current")


class _TmnxMobPdnApnPcoDnsV4PriAddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoDnsV4PriAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoDnsV4PriAddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoDnsV4PriAddrType_Object = MibTableColumn
tmnxMobPdnApnPcoDnsV4PriAddrType = _TmnxMobPdnApnPcoDnsV4PriAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 18),
    _TmnxMobPdnApnPcoDnsV4PriAddrType_Type()
)
tmnxMobPdnApnPcoDnsV4PriAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoDnsV4PriAddrType.setStatus("current")


class _TmnxMobPdnApnPcoDnsV4PriAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoDnsV4PriAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnApnPcoDnsV4PriAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoDnsV4PriAddr_Object = MibTableColumn
tmnxMobPdnApnPcoDnsV4PriAddr = _TmnxMobPdnApnPcoDnsV4PriAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 19),
    _TmnxMobPdnApnPcoDnsV4PriAddr_Type()
)
tmnxMobPdnApnPcoDnsV4PriAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoDnsV4PriAddr.setStatus("current")


class _TmnxMobPdnApnPcoDnsV4SecAddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoDnsV4SecAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoDnsV4SecAddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoDnsV4SecAddrType_Object = MibTableColumn
tmnxMobPdnApnPcoDnsV4SecAddrType = _TmnxMobPdnApnPcoDnsV4SecAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 20),
    _TmnxMobPdnApnPcoDnsV4SecAddrType_Type()
)
tmnxMobPdnApnPcoDnsV4SecAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoDnsV4SecAddrType.setStatus("current")


class _TmnxMobPdnApnPcoDnsV4SecAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoDnsV4SecAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnApnPcoDnsV4SecAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoDnsV4SecAddr_Object = MibTableColumn
tmnxMobPdnApnPcoDnsV4SecAddr = _TmnxMobPdnApnPcoDnsV4SecAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 21),
    _TmnxMobPdnApnPcoDnsV4SecAddr_Type()
)
tmnxMobPdnApnPcoDnsV4SecAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoDnsV4SecAddr.setStatus("current")


class _TmnxMobPdnApnPcoDnsV6PriAddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoDnsV6PriAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoDnsV6PriAddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoDnsV6PriAddrType_Object = MibTableColumn
tmnxMobPdnApnPcoDnsV6PriAddrType = _TmnxMobPdnApnPcoDnsV6PriAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 22),
    _TmnxMobPdnApnPcoDnsV6PriAddrType_Type()
)
tmnxMobPdnApnPcoDnsV6PriAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoDnsV6PriAddrType.setStatus("current")


class _TmnxMobPdnApnPcoDnsV6PriAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoDnsV6PriAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnApnPcoDnsV6PriAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoDnsV6PriAddr_Object = MibTableColumn
tmnxMobPdnApnPcoDnsV6PriAddr = _TmnxMobPdnApnPcoDnsV6PriAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 23),
    _TmnxMobPdnApnPcoDnsV6PriAddr_Type()
)
tmnxMobPdnApnPcoDnsV6PriAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoDnsV6PriAddr.setStatus("current")


class _TmnxMobPdnApnPcoDnsV6SecAddrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoDnsV6SecAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoDnsV6SecAddrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoDnsV6SecAddrType_Object = MibTableColumn
tmnxMobPdnApnPcoDnsV6SecAddrType = _TmnxMobPdnApnPcoDnsV6SecAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 24),
    _TmnxMobPdnApnPcoDnsV6SecAddrType_Type()
)
tmnxMobPdnApnPcoDnsV6SecAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoDnsV6SecAddrType.setStatus("current")


class _TmnxMobPdnApnPcoDnsV6SecAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoDnsV6SecAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnApnPcoDnsV6SecAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoDnsV6SecAddr_Object = MibTableColumn
tmnxMobPdnApnPcoDnsV6SecAddr = _TmnxMobPdnApnPcoDnsV6SecAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 25),
    _TmnxMobPdnApnPcoDnsV6SecAddr_Type()
)
tmnxMobPdnApnPcoDnsV6SecAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoDnsV6SecAddr.setStatus("current")


class _TmnxMobPdnApnPcoPcscfV4PriAdrTyp_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoPcscfV4PriAdrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoPcscfV4PriAdrTyp_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoPcscfV4PriAdrTyp_Object = MibTableColumn
tmnxMobPdnApnPcoPcscfV4PriAdrTyp = _TmnxMobPdnApnPcoPcscfV4PriAdrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 26),
    _TmnxMobPdnApnPcoPcscfV4PriAdrTyp_Type()
)
tmnxMobPdnApnPcoPcscfV4PriAdrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoPcscfV4PriAdrTyp.setStatus("current")


class _TmnxMobPdnApnPcoPcscfV4PriAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoPcscfV4PriAddr based on InetAddress"""
    defaultHexValue = ""


_TmnxMobPdnApnPcoPcscfV4PriAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoPcscfV4PriAddr_Object = MibTableColumn
tmnxMobPdnApnPcoPcscfV4PriAddr = _TmnxMobPdnApnPcoPcscfV4PriAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 27),
    _TmnxMobPdnApnPcoPcscfV4PriAddr_Type()
)
tmnxMobPdnApnPcoPcscfV4PriAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoPcscfV4PriAddr.setStatus("current")


class _TmnxMobPdnApnPcoPcscfV6PriAdrTyp_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoPcscfV6PriAdrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoPcscfV6PriAdrTyp_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoPcscfV6PriAdrTyp_Object = MibTableColumn
tmnxMobPdnApnPcoPcscfV6PriAdrTyp = _TmnxMobPdnApnPcoPcscfV6PriAdrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 28),
    _TmnxMobPdnApnPcoPcscfV6PriAdrTyp_Type()
)
tmnxMobPdnApnPcoPcscfV6PriAdrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoPcscfV6PriAdrTyp.setStatus("current")


class _TmnxMobPdnApnPcoPcscfV6PriAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoPcscfV6PriAddr based on InetAddress"""
    defaultHexValue = ""


_TmnxMobPdnApnPcoPcscfV6PriAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoPcscfV6PriAddr_Object = MibTableColumn
tmnxMobPdnApnPcoPcscfV6PriAddr = _TmnxMobPdnApnPcoPcscfV6PriAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 29),
    _TmnxMobPdnApnPcoPcscfV6PriAddr_Type()
)
tmnxMobPdnApnPcoPcscfV6PriAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoPcscfV6PriAddr.setStatus("current")


class _TmnxMobPdnApnPcoNbnsV4PriAdrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoNbnsV4PriAdrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoNbnsV4PriAdrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoNbnsV4PriAdrType_Object = MibTableColumn
tmnxMobPdnApnPcoNbnsV4PriAdrType = _TmnxMobPdnApnPcoNbnsV4PriAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 30),
    _TmnxMobPdnApnPcoNbnsV4PriAdrType_Type()
)
tmnxMobPdnApnPcoNbnsV4PriAdrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoNbnsV4PriAdrType.setStatus("current")


class _TmnxMobPdnApnPcoNbnsV4PriAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoNbnsV4PriAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnApnPcoNbnsV4PriAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoNbnsV4PriAddr_Object = MibTableColumn
tmnxMobPdnApnPcoNbnsV4PriAddr = _TmnxMobPdnApnPcoNbnsV4PriAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 31),
    _TmnxMobPdnApnPcoNbnsV4PriAddr_Type()
)
tmnxMobPdnApnPcoNbnsV4PriAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoNbnsV4PriAddr.setStatus("current")


class _TmnxMobPdnApnPcoNbnsV4SecAdrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoNbnsV4SecAdrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoNbnsV4SecAdrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoNbnsV4SecAdrType_Object = MibTableColumn
tmnxMobPdnApnPcoNbnsV4SecAdrType = _TmnxMobPdnApnPcoNbnsV4SecAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 32),
    _TmnxMobPdnApnPcoNbnsV4SecAdrType_Type()
)
tmnxMobPdnApnPcoNbnsV4SecAdrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoNbnsV4SecAdrType.setStatus("current")


class _TmnxMobPdnApnPcoNbnsV4SecAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoNbnsV4SecAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnApnPcoNbnsV4SecAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoNbnsV4SecAddr_Object = MibTableColumn
tmnxMobPdnApnPcoNbnsV4SecAddr = _TmnxMobPdnApnPcoNbnsV4SecAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 33),
    _TmnxMobPdnApnPcoNbnsV4SecAddr_Type()
)
tmnxMobPdnApnPcoNbnsV4SecAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoNbnsV4SecAddr.setStatus("current")


class _TmnxMobPdnApnPcoNbnsV6PriAdrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoNbnsV6PriAdrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoNbnsV6PriAdrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoNbnsV6PriAdrType_Object = MibTableColumn
tmnxMobPdnApnPcoNbnsV6PriAdrType = _TmnxMobPdnApnPcoNbnsV6PriAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 34),
    _TmnxMobPdnApnPcoNbnsV6PriAdrType_Type()
)
tmnxMobPdnApnPcoNbnsV6PriAdrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoNbnsV6PriAdrType.setStatus("current")


class _TmnxMobPdnApnPcoNbnsV6PriAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoNbnsV6PriAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnApnPcoNbnsV6PriAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoNbnsV6PriAddr_Object = MibTableColumn
tmnxMobPdnApnPcoNbnsV6PriAddr = _TmnxMobPdnApnPcoNbnsV6PriAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 35),
    _TmnxMobPdnApnPcoNbnsV6PriAddr_Type()
)
tmnxMobPdnApnPcoNbnsV6PriAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoNbnsV6PriAddr.setStatus("current")


class _TmnxMobPdnApnPcoNbnsV6SecAdrType_Type(InetAddressType):
    """Custom type tmnxMobPdnApnPcoNbnsV6SecAdrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnPcoNbnsV6SecAdrType_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnPcoNbnsV6SecAdrType_Object = MibTableColumn
tmnxMobPdnApnPcoNbnsV6SecAdrType = _TmnxMobPdnApnPcoNbnsV6SecAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 36),
    _TmnxMobPdnApnPcoNbnsV6SecAdrType_Type()
)
tmnxMobPdnApnPcoNbnsV6SecAdrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoNbnsV6SecAdrType.setStatus("current")


class _TmnxMobPdnApnPcoNbnsV6SecAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnPcoNbnsV6SecAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnApnPcoNbnsV6SecAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnPcoNbnsV6SecAddr_Object = MibTableColumn
tmnxMobPdnApnPcoNbnsV6SecAddr = _TmnxMobPdnApnPcoNbnsV6SecAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 10, 1, 37),
    _TmnxMobPdnApnPcoNbnsV6SecAddr_Type()
)
tmnxMobPdnApnPcoNbnsV6SecAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPcoNbnsV6SecAddr.setStatus("current")
_TmnxMobPdnApnExt2Table_Object = MibTable
tmnxMobPdnApnExt2Table = _TmnxMobPdnApnExt2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnExt2Table.setStatus("current")
_TmnxMobPdnApnExt2Entry_Object = MibTableRow
tmnxMobPdnApnExt2Entry = _TmnxMobPdnApnExt2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnExt2Entry.setStatus("current")
_TmnxMobPdnApnExt2LastChanged_Type = TimeStamp
_TmnxMobPdnApnExt2LastChanged_Object = MibTableColumn
tmnxMobPdnApnExt2LastChanged = _TmnxMobPdnApnExt2LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 1),
    _TmnxMobPdnApnExt2LastChanged_Type()
)
tmnxMobPdnApnExt2LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnExt2LastChanged.setStatus("current")


class _TmnxMobPdnApnChrgProfileHome_Type(TmnxMobChargingProfileOrInherit):
    """Custom type tmnxMobPdnApnChrgProfileHome based on TmnxMobChargingProfileOrInherit"""
    defaultValue = -1


_TmnxMobPdnApnChrgProfileHome_Type.__name__ = "TmnxMobChargingProfileOrInherit"
_TmnxMobPdnApnChrgProfileHome_Object = MibTableColumn
tmnxMobPdnApnChrgProfileHome = _TmnxMobPdnApnChrgProfileHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 2),
    _TmnxMobPdnApnChrgProfileHome_Type()
)
tmnxMobPdnApnChrgProfileHome.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChrgProfileHome.setStatus("current")


class _TmnxMobPdnApnChrgProfileVisiting_Type(TmnxMobChargingProfileOrInherit):
    """Custom type tmnxMobPdnApnChrgProfileVisiting based on TmnxMobChargingProfileOrInherit"""
    defaultValue = -1


_TmnxMobPdnApnChrgProfileVisiting_Type.__name__ = "TmnxMobChargingProfileOrInherit"
_TmnxMobPdnApnChrgProfileVisiting_Object = MibTableColumn
tmnxMobPdnApnChrgProfileVisiting = _TmnxMobPdnApnChrgProfileVisiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 3),
    _TmnxMobPdnApnChrgProfileVisiting_Type()
)
tmnxMobPdnApnChrgProfileVisiting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChrgProfileVisiting.setStatus("current")


class _TmnxMobPdnApnChrgProfileRoaming_Type(TmnxMobChargingProfileOrInherit):
    """Custom type tmnxMobPdnApnChrgProfileRoaming based on TmnxMobChargingProfileOrInherit"""
    defaultValue = -1


_TmnxMobPdnApnChrgProfileRoaming_Type.__name__ = "TmnxMobChargingProfileOrInherit"
_TmnxMobPdnApnChrgProfileRoaming_Object = MibTableColumn
tmnxMobPdnApnChrgProfileRoaming = _TmnxMobPdnApnChrgProfileRoaming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 4),
    _TmnxMobPdnApnChrgProfileRoaming_Type()
)
tmnxMobPdnApnChrgProfileRoaming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChrgProfileRoaming.setStatus("current")


class _TmnxMobPdnApnChrgCcIgnoreAny_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobPdnApnChrgCcIgnoreAny based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobPdnApnChrgCcIgnoreAny_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobPdnApnChrgCcIgnoreAny_Object = MibTableColumn
tmnxMobPdnApnChrgCcIgnoreAny = _TmnxMobPdnApnChrgCcIgnoreAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 5),
    _TmnxMobPdnApnChrgCcIgnoreAny_Type()
)
tmnxMobPdnApnChrgCcIgnoreAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChrgCcIgnoreAny.setStatus("current")


class _TmnxMobPdnApnChrgCcIgnoreHome_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobPdnApnChrgCcIgnoreHome based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobPdnApnChrgCcIgnoreHome_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobPdnApnChrgCcIgnoreHome_Object = MibTableColumn
tmnxMobPdnApnChrgCcIgnoreHome = _TmnxMobPdnApnChrgCcIgnoreHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 6),
    _TmnxMobPdnApnChrgCcIgnoreHome_Type()
)
tmnxMobPdnApnChrgCcIgnoreHome.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChrgCcIgnoreHome.setStatus("current")


class _TmnxMobPdnApnChrgCcIgnoreVisit_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobPdnApnChrgCcIgnoreVisit based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobPdnApnChrgCcIgnoreVisit_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobPdnApnChrgCcIgnoreVisit_Object = MibTableColumn
tmnxMobPdnApnChrgCcIgnoreVisit = _TmnxMobPdnApnChrgCcIgnoreVisit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 7),
    _TmnxMobPdnApnChrgCcIgnoreVisit_Type()
)
tmnxMobPdnApnChrgCcIgnoreVisit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChrgCcIgnoreVisit.setStatus("current")


class _TmnxMobPdnApnChrgCcIgnoreRoaming_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobPdnApnChrgCcIgnoreRoaming based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobPdnApnChrgCcIgnoreRoaming_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobPdnApnChrgCcIgnoreRoaming_Object = MibTableColumn
tmnxMobPdnApnChrgCcIgnoreRoaming = _TmnxMobPdnApnChrgCcIgnoreRoaming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 8),
    _TmnxMobPdnApnChrgCcIgnoreRoaming_Type()
)
tmnxMobPdnApnChrgCcIgnoreRoaming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChrgCcIgnoreRoaming.setStatus("current")


class _TmnxMobPdnApnCdfPriDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnCdfPriDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnCdfPriDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnCdfPriDiaPeer_Object = MibTableColumn
tmnxMobPdnApnCdfPriDiaPeer = _TmnxMobPdnApnCdfPriDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 9),
    _TmnxMobPdnApnCdfPriDiaPeer_Type()
)
tmnxMobPdnApnCdfPriDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnCdfPriDiaPeer.setStatus("current")


class _TmnxMobPdnApnCdfSecDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnCdfSecDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnCdfSecDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnCdfSecDiaPeer_Object = MibTableColumn
tmnxMobPdnApnCdfSecDiaPeer = _TmnxMobPdnApnCdfSecDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 10),
    _TmnxMobPdnApnCdfSecDiaPeer_Type()
)
tmnxMobPdnApnCdfSecDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnCdfSecDiaPeer.setStatus("current")


class _TmnxMobPdnApnPreAuthType_Type(TmnxMobAuthType):
    """Custom type tmnxMobPdnApnPreAuthType based on TmnxMobAuthType"""
    defaultValue = 1


_TmnxMobPdnApnPreAuthType_Type.__name__ = "TmnxMobAuthType"
_TmnxMobPdnApnPreAuthType_Object = MibTableColumn
tmnxMobPdnApnPreAuthType = _TmnxMobPdnApnPreAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 11),
    _TmnxMobPdnApnPreAuthType_Type()
)
tmnxMobPdnApnPreAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPreAuthType.setStatus("current")


class _TmnxMobPdnApnPreAuthUserName_Type(TmnxMobAuthUserName):
    """Custom type tmnxMobPdnApnPreAuthUserName based on TmnxMobAuthUserName"""
    defaultValue = 1


_TmnxMobPdnApnPreAuthUserName_Type.__name__ = "TmnxMobAuthUserName"
_TmnxMobPdnApnPreAuthUserName_Object = MibTableColumn
tmnxMobPdnApnPreAuthUserName = _TmnxMobPdnApnPreAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 12),
    _TmnxMobPdnApnPreAuthUserName_Type()
)
tmnxMobPdnApnPreAuthUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPreAuthUserName.setStatus("current")


class _TmnxMobPdnApnAuthType_Type(TmnxMobAuthType):
    """Custom type tmnxMobPdnApnAuthType based on TmnxMobAuthType"""
    defaultValue = 1


_TmnxMobPdnApnAuthType_Type.__name__ = "TmnxMobAuthType"
_TmnxMobPdnApnAuthType_Object = MibTableColumn
tmnxMobPdnApnAuthType = _TmnxMobPdnApnAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 13),
    _TmnxMobPdnApnAuthType_Type()
)
tmnxMobPdnApnAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthType.setStatus("current")


class _TmnxMobPdnApnAuthUserName_Type(Integer32):
    """Custom type tmnxMobPdnApnAuthUserName based on Integer32"""
    defaultValue = 1

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
        *(("imsi", 1),
          ("msisdn", 2),
          ("pco", 3),
          ("fixed", 4))
    )


_TmnxMobPdnApnAuthUserName_Type.__name__ = "Integer32"
_TmnxMobPdnApnAuthUserName_Object = MibTableColumn
tmnxMobPdnApnAuthUserName = _TmnxMobPdnApnAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 14),
    _TmnxMobPdnApnAuthUserName_Type()
)
tmnxMobPdnApnAuthUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthUserName.setStatus("current")


class _TmnxMobPdnApnAcctType_Type(TmnxMobAuthType):
    """Custom type tmnxMobPdnApnAcctType based on TmnxMobAuthType"""
    defaultValue = 1


_TmnxMobPdnApnAcctType_Type.__name__ = "TmnxMobAuthType"
_TmnxMobPdnApnAcctType_Object = MibTableColumn
tmnxMobPdnApnAcctType = _TmnxMobPdnApnAcctType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 15),
    _TmnxMobPdnApnAcctType_Type()
)
tmnxMobPdnApnAcctType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAcctType.setStatus("current")


class _TmnxMobPdnApnAcctUserName_Type(TmnxMobAuthUserName):
    """Custom type tmnxMobPdnApnAcctUserName based on TmnxMobAuthUserName"""
    defaultValue = 1


_TmnxMobPdnApnAcctUserName_Type.__name__ = "TmnxMobAuthUserName"
_TmnxMobPdnApnAcctUserName_Object = MibTableColumn
tmnxMobPdnApnAcctUserName = _TmnxMobPdnApnAcctUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 16),
    _TmnxMobPdnApnAcctUserName_Type()
)
tmnxMobPdnApnAcctUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAcctUserName.setStatus("current")


class _TmnxMobPdnApnAcctInterimReport_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobPdnApnAcctInterimReport based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 1


_TmnxMobPdnApnAcctInterimReport_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobPdnApnAcctInterimReport_Object = MibTableColumn
tmnxMobPdnApnAcctInterimReport = _TmnxMobPdnApnAcctInterimReport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 17),
    _TmnxMobPdnApnAcctInterimReport_Type()
)
tmnxMobPdnApnAcctInterimReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAcctInterimReport.setStatus("current")


class _TmnxMobPdnApnChrgCcReject_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobPdnApnChrgCcReject based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobPdnApnChrgCcReject_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobPdnApnChrgCcReject_Object = MibTableColumn
tmnxMobPdnApnChrgCcReject = _TmnxMobPdnApnChrgCcReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 18),
    _TmnxMobPdnApnChrgCcReject_Type()
)
tmnxMobPdnApnChrgCcReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChrgCcReject.setStatus("current")


class _TmnxMobPdnApnAuthServerGroup_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnAuthServerGroup based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnAuthServerGroup_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnAuthServerGroup_Object = MibTableColumn
tmnxMobPdnApnAuthServerGroup = _TmnxMobPdnApnAuthServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 19),
    _TmnxMobPdnApnAuthServerGroup_Type()
)
tmnxMobPdnApnAuthServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthServerGroup.setStatus("current")


class _TmnxMobPdnApnAuthAcctSupImsi_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnApnAuthAcctSupImsi based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnApnAuthAcctSupImsi_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnApnAuthAcctSupImsi_Object = MibTableColumn
tmnxMobPdnApnAuthAcctSupImsi = _TmnxMobPdnApnAuthAcctSupImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 20),
    _TmnxMobPdnApnAuthAcctSupImsi_Type()
)
tmnxMobPdnApnAuthAcctSupImsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthAcctSupImsi.setStatus("obsolete")


class _TmnxMobPdnApnAcctServerGroup_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnAcctServerGroup based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnAcctServerGroup_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnAcctServerGroup_Object = MibTableColumn
tmnxMobPdnApnAcctServerGroup = _TmnxMobPdnApnAcctServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 21),
    _TmnxMobPdnApnAcctServerGroup_Type()
)
tmnxMobPdnApnAcctServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAcctServerGroup.setStatus("current")


class _TmnxMobPdnApnWaitAccounting_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnApnWaitAccounting based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnApnWaitAccounting_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnApnWaitAccounting_Object = MibTableColumn
tmnxMobPdnApnWaitAccounting = _TmnxMobPdnApnWaitAccounting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 22),
    _TmnxMobPdnApnWaitAccounting_Type()
)
tmnxMobPdnApnWaitAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnWaitAccounting.setStatus("current")


class _TmnxMobPdnApnOcsPriDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnOcsPriDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnOcsPriDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnOcsPriDiaPeer_Object = MibTableColumn
tmnxMobPdnApnOcsPriDiaPeer = _TmnxMobPdnApnOcsPriDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 23),
    _TmnxMobPdnApnOcsPriDiaPeer_Type()
)
tmnxMobPdnApnOcsPriDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnOcsPriDiaPeer.setStatus("current")


class _TmnxMobPdnApnOcsSecDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnOcsSecDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnOcsSecDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnOcsSecDiaPeer_Object = MibTableColumn
tmnxMobPdnApnOcsSecDiaPeer = _TmnxMobPdnApnOcsSecDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 24),
    _TmnxMobPdnApnOcsSecDiaPeer_Type()
)
tmnxMobPdnApnOcsSecDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnOcsSecDiaPeer.setStatus("current")


class _TmnxMobPdnApnGyDccaProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnGyDccaProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnGyDccaProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnGyDccaProfile_Object = MibTableColumn
tmnxMobPdnApnGyDccaProfile = _TmnxMobPdnApnGyDccaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 25),
    _TmnxMobPdnApnGyDccaProfile_Type()
)
tmnxMobPdnApnGyDccaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnGyDccaProfile.setStatus("current")


class _TmnxMobPdnApnPreAuthServerGroup_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnPreAuthServerGroup based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnPreAuthServerGroup_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnPreAuthServerGroup_Object = MibTableColumn
tmnxMobPdnApnPreAuthServerGroup = _TmnxMobPdnApnPreAuthServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 26),
    _TmnxMobPdnApnPreAuthServerGroup_Type()
)
tmnxMobPdnApnPreAuthServerGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPreAuthServerGroup.setStatus("current")


class _TmnxMobPdnApnChangeRepAction_Type(Integer32):
    """Custom type tmnxMobPdnApnChangeRepAction based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("cgiSai", 1),
          ("rai", 2),
          ("cgiSaiRai", 3),
          ("tai", 4),
          ("egci", 5),
          ("taiEgci", 6))
    )


_TmnxMobPdnApnChangeRepAction_Type.__name__ = "Integer32"
_TmnxMobPdnApnChangeRepAction_Object = MibTableColumn
tmnxMobPdnApnChangeRepAction = _TmnxMobPdnApnChangeRepAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 27),
    _TmnxMobPdnApnChangeRepAction_Type()
)
tmnxMobPdnApnChangeRepAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnChangeRepAction.setStatus("current")


class _TmnxMobPdnApnSuppFramedRoute_Type(TruthValue):
    """Custom type tmnxMobPdnApnSuppFramedRoute based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApnSuppFramedRoute_Type.__name__ = "TruthValue"
_TmnxMobPdnApnSuppFramedRoute_Object = MibTableColumn
tmnxMobPdnApnSuppFramedRoute = _TmnxMobPdnApnSuppFramedRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 28),
    _TmnxMobPdnApnSuppFramedRoute_Type()
)
tmnxMobPdnApnSuppFramedRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnSuppFramedRoute.setStatus("current")


class _TmnxMobPdnApnPccQciValue_Type(TmnxMobQciValueOrZero):
    """Custom type tmnxMobPdnApnPccQciValue based on TmnxMobQciValueOrZero"""
    defaultValue = 0


_TmnxMobPdnApnPccQciValue_Type.__name__ = "TmnxMobQciValueOrZero"
_TmnxMobPdnApnPccQciValue_Object = MibTableColumn
tmnxMobPdnApnPccQciValue = _TmnxMobPdnApnPccQciValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 29),
    _TmnxMobPdnApnPccQciValue_Type()
)
tmnxMobPdnApnPccQciValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPccQciValue.setStatus("current")


class _TmnxMobPdnApnPccArpValue_Type(TmnxMobArpValueOrZero):
    """Custom type tmnxMobPdnApnPccArpValue based on TmnxMobArpValueOrZero"""
    defaultValue = 0


_TmnxMobPdnApnPccArpValue_Type.__name__ = "TmnxMobArpValueOrZero"
_TmnxMobPdnApnPccArpValue_Object = MibTableColumn
tmnxMobPdnApnPccArpValue = _TmnxMobPdnApnPccArpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 30),
    _TmnxMobPdnApnPccArpValue_Type()
)
tmnxMobPdnApnPccArpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPccArpValue.setStatus("current")


class _TmnxMobPdnApnAuthFixUserName_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobPdnApnAuthFixUserName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("default")


_TmnxMobPdnApnAuthFixUserName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobPdnApnAuthFixUserName_Object = MibTableColumn
tmnxMobPdnApnAuthFixUserName = _TmnxMobPdnApnAuthFixUserName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 31),
    _TmnxMobPdnApnAuthFixUserName_Type()
)
tmnxMobPdnApnAuthFixUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthFixUserName.setStatus("current")


class _TmnxMobPdnApnAuthFixPassword_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobPdnApnAuthFixPassword based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnAuthFixPassword_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobPdnApnAuthFixPassword_Object = MibTableColumn
tmnxMobPdnApnAuthFixPassword = _TmnxMobPdnApnAuthFixPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 11, 1, 32),
    _TmnxMobPdnApnAuthFixPassword_Type()
)
tmnxMobPdnApnAuthFixPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthFixPassword.setStatus("current")
_TmnxMobPdnApnIpPoolTable_Object = MibTable
tmnxMobPdnApnIpPoolTable = _TmnxMobPdnApnIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpPoolTable.setStatus("current")
_TmnxMobPdnApnIpPoolEntry_Object = MibTableRow
tmnxMobPdnApnIpPoolEntry = _TmnxMobPdnApnIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 12, 1)
)
tmnxMobPdnApnIpPoolEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIpPoolName"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpPoolEntry.setStatus("current")
_TmnxMobPdnApnIpPoolRowStatus_Type = RowStatus
_TmnxMobPdnApnIpPoolRowStatus_Object = MibTableColumn
tmnxMobPdnApnIpPoolRowStatus = _TmnxMobPdnApnIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 12, 1, 1),
    _TmnxMobPdnApnIpPoolRowStatus_Type()
)
tmnxMobPdnApnIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpPoolRowStatus.setStatus("current")
_TmnxMobPdnApnBasePolTable_Object = MibTable
tmnxMobPdnApnBasePolTable = _TmnxMobPdnApnBasePolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnBasePolTable.setStatus("current")
_TmnxMobPdnApnBasePolEntry_Object = MibTableRow
tmnxMobPdnApnBasePolEntry = _TmnxMobPdnApnBasePolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 13, 1)
)
tmnxMobPdnApnBasePolEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfPolBaseName"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnBasePolEntry.setStatus("current")
_TmnxMobPdnApnBasePolRowStatus_Type = RowStatus
_TmnxMobPdnApnBasePolRowStatus_Object = MibTableColumn
tmnxMobPdnApnBasePolRowStatus = _TmnxMobPdnApnBasePolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 13, 1, 1),
    _TmnxMobPdnApnBasePolRowStatus_Type()
)
tmnxMobPdnApnBasePolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnBasePolRowStatus.setStatus("current")
_TmnxMobPdnGaTable_Object = MibTable
tmnxMobPdnGaTable = _TmnxMobPdnGaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGaTable.setStatus("current")
_TmnxMobPdnGaEntry_Object = MibTableRow
tmnxMobPdnGaEntry = _TmnxMobPdnGaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 14, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGaEntry.setStatus("current")
_TmnxMobPdnGaLastChanged_Type = TimeStamp
_TmnxMobPdnGaLastChanged_Object = MibTableColumn
tmnxMobPdnGaLastChanged = _TmnxMobPdnGaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 14, 1, 1),
    _TmnxMobPdnGaLastChanged_Type()
)
tmnxMobPdnGaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaLastChanged.setStatus("current")


class _TmnxMobPdnGaIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnGaIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnGaIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnGaIfVRtrId_Object = MibTableColumn
tmnxMobPdnGaIfVRtrId = _TmnxMobPdnGaIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 14, 1, 2),
    _TmnxMobPdnGaIfVRtrId_Type()
)
tmnxMobPdnGaIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGaIfVRtrId.setStatus("current")


class _TmnxMobPdnGaIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnGaIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnGaIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnGaIfIndex_Object = MibTableColumn
tmnxMobPdnGaIfIndex = _TmnxMobPdnGaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 14, 1, 3),
    _TmnxMobPdnGaIfIndex_Type()
)
tmnxMobPdnGaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGaIfIndex.setStatus("current")


class _TmnxMobPdnGaGtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGaGtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGaGtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGaGtpcProfile_Object = MibTableColumn
tmnxMobPdnGaGtpcProfile = _TmnxMobPdnGaGtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 14, 1, 4),
    _TmnxMobPdnGaGtpcProfile_Type()
)
tmnxMobPdnGaGtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGaGtpcProfile.setStatus("current")


class _TmnxMobPdnGaGtpPrimeGrpName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGaGtpPrimeGrpName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGaGtpPrimeGrpName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGaGtpPrimeGrpName_Object = MibTableColumn
tmnxMobPdnGaGtpPrimeGrpName = _TmnxMobPdnGaGtpPrimeGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 14, 1, 5),
    _TmnxMobPdnGaGtpPrimeGrpName_Type()
)
tmnxMobPdnGaGtpPrimeGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGaGtpPrimeGrpName.setStatus("current")
_TmnxMobPdnGnTable_Object = MibTable
tmnxMobPdnGnTable = _TmnxMobPdnGnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGnTable.setStatus("current")
_TmnxMobPdnGnEntry_Object = MibTableRow
tmnxMobPdnGnEntry = _TmnxMobPdnGnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGnEntry.setStatus("current")
_TmnxMobPdnGnLastChanged_Type = TimeStamp
_TmnxMobPdnGnLastChanged_Object = MibTableColumn
tmnxMobPdnGnLastChanged = _TmnxMobPdnGnLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1, 1),
    _TmnxMobPdnGnLastChanged_Type()
)
tmnxMobPdnGnLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnLastChanged.setStatus("current")


class _TmnxMobPdnGnGtpcIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnGnGtpcIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnGnGtpcIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnGnGtpcIfVRtrId_Object = MibTableColumn
tmnxMobPdnGnGtpcIfVRtrId = _TmnxMobPdnGnGtpcIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1, 2),
    _TmnxMobPdnGnGtpcIfVRtrId_Type()
)
tmnxMobPdnGnGtpcIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGnGtpcIfVRtrId.setStatus("current")


class _TmnxMobPdnGnGtpcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnGnGtpcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnGnGtpcIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnGnGtpcIfIndex_Object = MibTableColumn
tmnxMobPdnGnGtpcIfIndex = _TmnxMobPdnGnGtpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1, 3),
    _TmnxMobPdnGnGtpcIfIndex_Type()
)
tmnxMobPdnGnGtpcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGnGtpcIfIndex.setStatus("current")


class _TmnxMobPdnGnGtpuIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnGnGtpuIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnGnGtpuIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnGnGtpuIfVRtrId_Object = MibTableColumn
tmnxMobPdnGnGtpuIfVRtrId = _TmnxMobPdnGnGtpuIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1, 4),
    _TmnxMobPdnGnGtpuIfVRtrId_Type()
)
tmnxMobPdnGnGtpuIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGnGtpuIfVRtrId.setStatus("current")


class _TmnxMobPdnGnGtpuIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnGnGtpuIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnGnGtpuIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnGnGtpuIfIndex_Object = MibTableColumn
tmnxMobPdnGnGtpuIfIndex = _TmnxMobPdnGnGtpuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1, 5),
    _TmnxMobPdnGnGtpuIfIndex_Type()
)
tmnxMobPdnGnGtpuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGnGtpuIfIndex.setStatus("current")


class _TmnxMobPdnGnGtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGnGtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGnGtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGnGtpcProfile_Object = MibTableColumn
tmnxMobPdnGnGtpcProfile = _TmnxMobPdnGnGtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1, 6),
    _TmnxMobPdnGnGtpcProfile_Type()
)
tmnxMobPdnGnGtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGnGtpcProfile.setStatus("current")


class _TmnxMobPdnGnGtpuProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGnGtpuProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGnGtpuProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGnGtpuProfile_Object = MibTableColumn
tmnxMobPdnGnGtpuProfile = _TmnxMobPdnGnGtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1, 7),
    _TmnxMobPdnGnGtpuProfile_Type()
)
tmnxMobPdnGnGtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGnGtpuProfile.setStatus("current")


class _TmnxMobPdnGnPeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGnPeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGnPeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGnPeerList_Object = MibTableColumn
tmnxMobPdnGnPeerList = _TmnxMobPdnGnPeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 15, 1, 8),
    _TmnxMobPdnGnPeerList_Type()
)
tmnxMobPdnGnPeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerList.setStatus("current")
_TmnxMobPdnApTable_Object = MibTable
tmnxMobPdnApTable = _TmnxMobPdnApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApTable.setStatus("current")
_TmnxMobPdnApEntry_Object = MibTableRow
tmnxMobPdnApEntry = _TmnxMobPdnApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 16, 1)
)
tmnxMobPdnApEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnApEntry.setStatus("current")


class _TmnxMobPdnApPolicyId_Type(Unsigned32):
    """Custom type tmnxMobPdnApPolicyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TmnxMobPdnApPolicyId_Type.__name__ = "Unsigned32"
_TmnxMobPdnApPolicyId_Object = MibTableColumn
tmnxMobPdnApPolicyId = _TmnxMobPdnApPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 16, 1, 1),
    _TmnxMobPdnApPolicyId_Type()
)
tmnxMobPdnApPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnApPolicyId.setStatus("current")
_TmnxMobPdnApRowStatus_Type = RowStatus
_TmnxMobPdnApRowStatus_Object = MibTableColumn
tmnxMobPdnApRowStatus = _TmnxMobPdnApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 16, 1, 2),
    _TmnxMobPdnApRowStatus_Type()
)
tmnxMobPdnApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApRowStatus.setStatus("current")
_TmnxMobPdnApLastChanged_Type = TimeStamp
_TmnxMobPdnApLastChanged_Object = MibTableColumn
tmnxMobPdnApLastChanged = _TmnxMobPdnApLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 16, 1, 3),
    _TmnxMobPdnApLastChanged_Type()
)
tmnxMobPdnApLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApLastChanged.setStatus("current")


class _TmnxMobPdnApCollectAcctStats_Type(TruthValue):
    """Custom type tmnxMobPdnApCollectAcctStats based on TruthValue"""
    defaultValue = 2


_TmnxMobPdnApCollectAcctStats_Type.__name__ = "TruthValue"
_TmnxMobPdnApCollectAcctStats_Object = MibTableColumn
tmnxMobPdnApCollectAcctStats = _TmnxMobPdnApCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 16, 1, 4),
    _TmnxMobPdnApCollectAcctStats_Type()
)
tmnxMobPdnApCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApCollectAcctStats.setStatus("current")
_TmnxMobPdnGnPeerTable_Object = MibTable
tmnxMobPdnGnPeerTable = _TmnxMobPdnGnPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerTable.setStatus("current")
_TmnxMobPdnGnPeerEntry_Object = MibTableRow
tmnxMobPdnGnPeerEntry = _TmnxMobPdnGnPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1)
)
tmnxMobPdnGnPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerEntry.setStatus("current")
_TmnxMobPdnGnPeerAddressType_Type = InetAddressType
_TmnxMobPdnGnPeerAddressType_Object = MibTableColumn
tmnxMobPdnGnPeerAddressType = _TmnxMobPdnGnPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1, 1),
    _TmnxMobPdnGnPeerAddressType_Type()
)
tmnxMobPdnGnPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerAddressType.setStatus("current")


class _TmnxMobPdnGnPeerAddress_Type(InetAddress):
    """Custom type tmnxMobPdnGnPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnGnPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnGnPeerAddress_Object = MibTableColumn
tmnxMobPdnGnPeerAddress = _TmnxMobPdnGnPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1, 2),
    _TmnxMobPdnGnPeerAddress_Type()
)
tmnxMobPdnGnPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerAddress.setStatus("current")
_TmnxMobPdnGnPeerPort_Type = InetPortNumber
_TmnxMobPdnGnPeerPort_Object = MibTableColumn
tmnxMobPdnGnPeerPort = _TmnxMobPdnGnPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1, 3),
    _TmnxMobPdnGnPeerPort_Type()
)
tmnxMobPdnGnPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerPort.setStatus("current")
_TmnxMobPdnGnPeerLastChanged_Type = TimeStamp
_TmnxMobPdnGnPeerLastChanged_Object = MibTableColumn
tmnxMobPdnGnPeerLastChanged = _TmnxMobPdnGnPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1, 4),
    _TmnxMobPdnGnPeerLastChanged_Type()
)
tmnxMobPdnGnPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerLastChanged.setStatus("current")
_TmnxMobPdnGnPeerCreateTime_Type = TimeStamp
_TmnxMobPdnGnPeerCreateTime_Object = MibTableColumn
tmnxMobPdnGnPeerCreateTime = _TmnxMobPdnGnPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1, 5),
    _TmnxMobPdnGnPeerCreateTime_Type()
)
tmnxMobPdnGnPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerCreateTime.setStatus("current")
_TmnxMobPdnGnPeerPathMgmtState_Type = TmnxMobPathMgmtState
_TmnxMobPdnGnPeerPathMgmtState_Object = MibTableColumn
tmnxMobPdnGnPeerPathMgmtState = _TmnxMobPdnGnPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1, 6),
    _TmnxMobPdnGnPeerPathMgmtState_Type()
)
tmnxMobPdnGnPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerPathMgmtState.setStatus("current")
_TmnxMobPdnGnPeerGatewayId_Type = TmnxMobGwId
_TmnxMobPdnGnPeerGatewayId_Object = MibTableColumn
tmnxMobPdnGnPeerGatewayId = _TmnxMobPdnGnPeerGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1, 7),
    _TmnxMobPdnGnPeerGatewayId_Type()
)
tmnxMobPdnGnPeerGatewayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerGatewayId.setStatus("current")
_TmnxMobPdnGnPeerType_Type = TmnxMobPeerType
_TmnxMobPdnGnPeerType_Object = MibTableColumn
tmnxMobPdnGnPeerType = _TmnxMobPdnGnPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 17, 1, 8),
    _TmnxMobPdnGnPeerType_Type()
)
tmnxMobPdnGnPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerType.setStatus("current")
_TmnxMobPdnRadiusTable_Object = MibTable
tmnxMobPdnRadiusTable = _TmnxMobPdnRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusTable.setStatus("current")
_TmnxMobPdnRadiusEntry_Object = MibTableRow
tmnxMobPdnRadiusEntry = _TmnxMobPdnRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 18, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusEntry.setStatus("current")
_TmnxMobPdnRadiusLastChanged_Type = TimeStamp
_TmnxMobPdnRadiusLastChanged_Object = MibTableColumn
tmnxMobPdnRadiusLastChanged = _TmnxMobPdnRadiusLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 18, 1, 1),
    _TmnxMobPdnRadiusLastChanged_Type()
)
tmnxMobPdnRadiusLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusLastChanged.setStatus("current")


class _TmnxMobPdnRadiusIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnRadiusIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnRadiusIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnRadiusIfVRtrId_Object = MibTableColumn
tmnxMobPdnRadiusIfVRtrId = _TmnxMobPdnRadiusIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 18, 1, 2),
    _TmnxMobPdnRadiusIfVRtrId_Type()
)
tmnxMobPdnRadiusIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusIfVRtrId.setStatus("current")


class _TmnxMobPdnRadiusIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnRadiusIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnRadiusIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnRadiusIfIndex_Object = MibTableColumn
tmnxMobPdnRadiusIfIndex = _TmnxMobPdnRadiusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 18, 1, 3),
    _TmnxMobPdnRadiusIfIndex_Type()
)
tmnxMobPdnRadiusIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusIfIndex.setStatus("current")


class _TmnxMobPdnRadiusDisconnect_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnRadiusDisconnect based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnRadiusDisconnect_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnRadiusDisconnect_Object = MibTableColumn
tmnxMobPdnRadiusDisconnect = _TmnxMobPdnRadiusDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 18, 1, 4),
    _TmnxMobPdnRadiusDisconnect_Type()
)
tmnxMobPdnRadiusDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusDisconnect.setStatus("current")
_TmnxMobPdnApnDaccGrpTable_Object = MibTable
tmnxMobPdnApnDaccGrpTable = _TmnxMobPdnApnDaccGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnDaccGrpTable.setStatus("current")
_TmnxMobPdnApnDaccGrpEntry_Object = MibTableRow
tmnxMobPdnApnDaccGrpEntry = _TmnxMobPdnApnDaccGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 19, 1)
)
tmnxMobPdnApnDaccGrpEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnName"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDaccGrpName"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnDaccGrpEntry.setStatus("current")
_TmnxMobPdnApnDaccGrpName_Type = TmnxMobProfName
_TmnxMobPdnApnDaccGrpName_Object = MibTableColumn
tmnxMobPdnApnDaccGrpName = _TmnxMobPdnApnDaccGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 19, 1, 1),
    _TmnxMobPdnApnDaccGrpName_Type()
)
tmnxMobPdnApnDaccGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDaccGrpName.setStatus("current")
_TmnxMobPdnApnDaccGrpRowStatus_Type = RowStatus
_TmnxMobPdnApnDaccGrpRowStatus_Object = MibTableColumn
tmnxMobPdnApnDaccGrpRowStatus = _TmnxMobPdnApnDaccGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 19, 1, 2),
    _TmnxMobPdnApnDaccGrpRowStatus_Type()
)
tmnxMobPdnApnDaccGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDaccGrpRowStatus.setStatus("current")
_TmnxMobPdnApnDaccGrpLastChngd_Type = TimeStamp
_TmnxMobPdnApnDaccGrpLastChngd_Object = MibTableColumn
tmnxMobPdnApnDaccGrpLastChngd = _TmnxMobPdnApnDaccGrpLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 19, 1, 3),
    _TmnxMobPdnApnDaccGrpLastChngd_Type()
)
tmnxMobPdnApnDaccGrpLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDaccGrpLastChngd.setStatus("current")
_TmnxMobPdnGyTable_Object = MibTable
tmnxMobPdnGyTable = _TmnxMobPdnGyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyTable.setStatus("current")
_TmnxMobPdnGyEntry_Object = MibTableRow
tmnxMobPdnGyEntry = _TmnxMobPdnGyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyEntry.setStatus("current")
_TmnxMobPdnGyLastChanged_Type = TimeStamp
_TmnxMobPdnGyLastChanged_Object = MibTableColumn
tmnxMobPdnGyLastChanged = _TmnxMobPdnGyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 1),
    _TmnxMobPdnGyLastChanged_Type()
)
tmnxMobPdnGyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyLastChanged.setStatus("current")


class _TmnxMobPdnGyVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnGyVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnGyVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnGyVRtrId_Object = MibTableColumn
tmnxMobPdnGyVRtrId = _TmnxMobPdnGyVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 2),
    _TmnxMobPdnGyVRtrId_Type()
)
tmnxMobPdnGyVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGyVRtrId.setStatus("current")


class _TmnxMobPdnGyIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnGyIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnGyIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnGyIfIndex_Object = MibTableColumn
tmnxMobPdnGyIfIndex = _TmnxMobPdnGyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 3),
    _TmnxMobPdnGyIfIndex_Type()
)
tmnxMobPdnGyIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGyIfIndex.setStatus("current")


class _TmnxMobPdnGyPriDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGyPriDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGyPriDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGyPriDiaPeer_Object = MibTableColumn
tmnxMobPdnGyPriDiaPeer = _TmnxMobPdnGyPriDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 4),
    _TmnxMobPdnGyPriDiaPeer_Type()
)
tmnxMobPdnGyPriDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPriDiaPeer.setStatus("current")


class _TmnxMobPdnGySecDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGySecDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGySecDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGySecDiaPeer_Object = MibTableColumn
tmnxMobPdnGySecDiaPeer = _TmnxMobPdnGySecDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 5),
    _TmnxMobPdnGySecDiaPeer_Type()
)
tmnxMobPdnGySecDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGySecDiaPeer.setStatus("current")


class _TmnxMobPdnGyDccaProf_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGyDccaProf based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGyDccaProf_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGyDccaProf_Object = MibTableColumn
tmnxMobPdnGyDccaProf = _TmnxMobPdnGyDccaProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 6),
    _TmnxMobPdnGyDccaProf_Type()
)
tmnxMobPdnGyDccaProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGyDccaProf.setStatus("current")


class _TmnxMobPdnGyDiaSession_Type(Integer32):
    """Custom type tmnxMobPdnGyDiaSession based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pdnLevel", 1),
          ("bearerLevel", 2))
    )


_TmnxMobPdnGyDiaSession_Type.__name__ = "Integer32"
_TmnxMobPdnGyDiaSession_Object = MibTableColumn
tmnxMobPdnGyDiaSession = _TmnxMobPdnGyDiaSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 7),
    _TmnxMobPdnGyDiaSession_Type()
)
tmnxMobPdnGyDiaSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGyDiaSession.setStatus("current")


class _TmnxMobPdnGyOcsSelIdType_Type(Integer32):
    """Custom type tmnxMobPdnGyOcsSelIdType based on Integer32"""
    defaultValue = 0

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
          ("imsi", 1),
          ("msisdn", 2))
    )


_TmnxMobPdnGyOcsSelIdType_Type.__name__ = "Integer32"
_TmnxMobPdnGyOcsSelIdType_Object = MibTableColumn
tmnxMobPdnGyOcsSelIdType = _TmnxMobPdnGyOcsSelIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 8),
    _TmnxMobPdnGyOcsSelIdType_Type()
)
tmnxMobPdnGyOcsSelIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsSelIdType.setStatus("current")


class _TmnxMobPdnGyOcsSelIdMappingStyle_Type(Integer32):
    """Custom type tmnxMobPdnGyOcsSelIdMappingStyle based on Integer32"""
    defaultValue = 0

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
          ("prefix", 1),
          ("fullId", 2))
    )


_TmnxMobPdnGyOcsSelIdMappingStyle_Type.__name__ = "Integer32"
_TmnxMobPdnGyOcsSelIdMappingStyle_Object = MibTableColumn
tmnxMobPdnGyOcsSelIdMappingStyle = _TmnxMobPdnGyOcsSelIdMappingStyle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 20, 1, 9),
    _TmnxMobPdnGyOcsSelIdMappingStyle_Type()
)
tmnxMobPdnGyOcsSelIdMappingStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsSelIdMappingStyle.setStatus("current")
_TmnxMobPdnRatingGrpTable_Object = MibTable
tmnxMobPdnRatingGrpTable = _TmnxMobPdnRatingGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 21)
)
if mibBuilder.loadTexts:
    tmnxMobPdnRatingGrpTable.setStatus("current")
_TmnxMobPdnRatingGrpEntry_Object = MibTableRow
tmnxMobPdnRatingGrpEntry = _TmnxMobPdnRatingGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 21, 1)
)
tmnxMobPdnRatingGrpEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyRatingGroupId"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnRatingGrpEntry.setStatus("current")


class _TmnxMobPdnGyRatingGroupId_Type(Unsigned32):
    """Custom type tmnxMobPdnGyRatingGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxMobPdnGyRatingGroupId_Type.__name__ = "Unsigned32"
_TmnxMobPdnGyRatingGroupId_Object = MibTableColumn
tmnxMobPdnGyRatingGroupId = _TmnxMobPdnGyRatingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 21, 1, 1),
    _TmnxMobPdnGyRatingGroupId_Type()
)
tmnxMobPdnGyRatingGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGyRatingGroupId.setStatus("current")
_TmnxMobPdnRatingGrpRowStatus_Type = RowStatus
_TmnxMobPdnRatingGrpRowStatus_Object = MibTableColumn
tmnxMobPdnRatingGrpRowStatus = _TmnxMobPdnRatingGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 21, 1, 2),
    _TmnxMobPdnRatingGrpRowStatus_Type()
)
tmnxMobPdnRatingGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnRatingGrpRowStatus.setStatus("current")
_TmnxMobPdnRatingGrpLastChanged_Type = TimeStamp
_TmnxMobPdnRatingGrpLastChanged_Object = MibTableColumn
tmnxMobPdnRatingGrpLastChanged = _TmnxMobPdnRatingGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 21, 1, 3),
    _TmnxMobPdnRatingGrpLastChanged_Type()
)
tmnxMobPdnRatingGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRatingGrpLastChanged.setStatus("current")


class _TmnxMobPdnRatingGrpActvtThresold_Type(Unsigned32):
    """Custom type tmnxMobPdnRatingGrpActvtThresold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_TmnxMobPdnRatingGrpActvtThresold_Type.__name__ = "Unsigned32"
_TmnxMobPdnRatingGrpActvtThresold_Object = MibTableColumn
tmnxMobPdnRatingGrpActvtThresold = _TmnxMobPdnRatingGrpActvtThresold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 21, 1, 4),
    _TmnxMobPdnRatingGrpActvtThresold_Type()
)
tmnxMobPdnRatingGrpActvtThresold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnRatingGrpActvtThresold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRatingGrpActvtThresold.setUnits("kbps")
_TmnxMobPdnGpTable_Object = MibTable
tmnxMobPdnGpTable = _TmnxMobPdnGpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGpTable.setStatus("current")
_TmnxMobPdnGpEntry_Object = MibTableRow
tmnxMobPdnGpEntry = _TmnxMobPdnGpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGpEntry.setStatus("current")
_TmnxMobPdnGpLastChanged_Type = TimeStamp
_TmnxMobPdnGpLastChanged_Object = MibTableColumn
tmnxMobPdnGpLastChanged = _TmnxMobPdnGpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1, 1),
    _TmnxMobPdnGpLastChanged_Type()
)
tmnxMobPdnGpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpLastChanged.setStatus("current")


class _TmnxMobPdnGpGtpcIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnGpGtpcIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnGpGtpcIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnGpGtpcIfVRtrId_Object = MibTableColumn
tmnxMobPdnGpGtpcIfVRtrId = _TmnxMobPdnGpGtpcIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1, 2),
    _TmnxMobPdnGpGtpcIfVRtrId_Type()
)
tmnxMobPdnGpGtpcIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGpGtpcIfVRtrId.setStatus("current")


class _TmnxMobPdnGpGtpcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnGpGtpcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnGpGtpcIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnGpGtpcIfIndex_Object = MibTableColumn
tmnxMobPdnGpGtpcIfIndex = _TmnxMobPdnGpGtpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1, 3),
    _TmnxMobPdnGpGtpcIfIndex_Type()
)
tmnxMobPdnGpGtpcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGpGtpcIfIndex.setStatus("current")


class _TmnxMobPdnGpGtpuIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnGpGtpuIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnGpGtpuIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnGpGtpuIfVRtrId_Object = MibTableColumn
tmnxMobPdnGpGtpuIfVRtrId = _TmnxMobPdnGpGtpuIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1, 4),
    _TmnxMobPdnGpGtpuIfVRtrId_Type()
)
tmnxMobPdnGpGtpuIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGpGtpuIfVRtrId.setStatus("current")


class _TmnxMobPdnGpGtpuIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobPdnGpGtpuIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnGpGtpuIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobPdnGpGtpuIfIndex_Object = MibTableColumn
tmnxMobPdnGpGtpuIfIndex = _TmnxMobPdnGpGtpuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1, 5),
    _TmnxMobPdnGpGtpuIfIndex_Type()
)
tmnxMobPdnGpGtpuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGpGtpuIfIndex.setStatus("current")


class _TmnxMobPdnGpGtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGpGtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGpGtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGpGtpcProfile_Object = MibTableColumn
tmnxMobPdnGpGtpcProfile = _TmnxMobPdnGpGtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1, 6),
    _TmnxMobPdnGpGtpcProfile_Type()
)
tmnxMobPdnGpGtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGpGtpcProfile.setStatus("current")


class _TmnxMobPdnGpGtpuProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGpGtpuProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGpGtpuProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGpGtpuProfile_Object = MibTableColumn
tmnxMobPdnGpGtpuProfile = _TmnxMobPdnGpGtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1, 7),
    _TmnxMobPdnGpGtpuProfile_Type()
)
tmnxMobPdnGpGtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGpGtpuProfile.setStatus("current")


class _TmnxMobPdnGpPeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGpPeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGpPeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGpPeerList_Object = MibTableColumn
tmnxMobPdnGpPeerList = _TmnxMobPdnGpPeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 22, 1, 8),
    _TmnxMobPdnGpPeerList_Type()
)
tmnxMobPdnGpPeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerList.setStatus("current")
_TmnxMobPdnGpPeerTable_Object = MibTable
tmnxMobPdnGpPeerTable = _TmnxMobPdnGpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerTable.setStatus("current")
_TmnxMobPdnGpPeerEntry_Object = MibTableRow
tmnxMobPdnGpPeerEntry = _TmnxMobPdnGpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1)
)
tmnxMobPdnGpPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerEntry.setStatus("current")
_TmnxMobPdnGpPeerAddressType_Type = InetAddressType
_TmnxMobPdnGpPeerAddressType_Object = MibTableColumn
tmnxMobPdnGpPeerAddressType = _TmnxMobPdnGpPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1, 1),
    _TmnxMobPdnGpPeerAddressType_Type()
)
tmnxMobPdnGpPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerAddressType.setStatus("current")


class _TmnxMobPdnGpPeerAddress_Type(InetAddress):
    """Custom type tmnxMobPdnGpPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnGpPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnGpPeerAddress_Object = MibTableColumn
tmnxMobPdnGpPeerAddress = _TmnxMobPdnGpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1, 2),
    _TmnxMobPdnGpPeerAddress_Type()
)
tmnxMobPdnGpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerAddress.setStatus("current")
_TmnxMobPdnGpPeerPort_Type = InetPortNumber
_TmnxMobPdnGpPeerPort_Object = MibTableColumn
tmnxMobPdnGpPeerPort = _TmnxMobPdnGpPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1, 3),
    _TmnxMobPdnGpPeerPort_Type()
)
tmnxMobPdnGpPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerPort.setStatus("current")
_TmnxMobPdnGpPeerLastChanged_Type = TimeStamp
_TmnxMobPdnGpPeerLastChanged_Object = MibTableColumn
tmnxMobPdnGpPeerLastChanged = _TmnxMobPdnGpPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1, 4),
    _TmnxMobPdnGpPeerLastChanged_Type()
)
tmnxMobPdnGpPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerLastChanged.setStatus("current")
_TmnxMobPdnGpPeerCreateTime_Type = TimeStamp
_TmnxMobPdnGpPeerCreateTime_Object = MibTableColumn
tmnxMobPdnGpPeerCreateTime = _TmnxMobPdnGpPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1, 5),
    _TmnxMobPdnGpPeerCreateTime_Type()
)
tmnxMobPdnGpPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerCreateTime.setStatus("current")
_TmnxMobPdnGpPeerPathMgmtState_Type = TmnxMobPathMgmtState
_TmnxMobPdnGpPeerPathMgmtState_Object = MibTableColumn
tmnxMobPdnGpPeerPathMgmtState = _TmnxMobPdnGpPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1, 6),
    _TmnxMobPdnGpPeerPathMgmtState_Type()
)
tmnxMobPdnGpPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerPathMgmtState.setStatus("current")
_TmnxMobPdnGpPeerGatewayId_Type = TmnxMobGwId
_TmnxMobPdnGpPeerGatewayId_Object = MibTableColumn
tmnxMobPdnGpPeerGatewayId = _TmnxMobPdnGpPeerGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1, 7),
    _TmnxMobPdnGpPeerGatewayId_Type()
)
tmnxMobPdnGpPeerGatewayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerGatewayId.setStatus("current")
_TmnxMobPdnGpPeerType_Type = TmnxMobPeerType
_TmnxMobPdnGpPeerType_Object = MibTableColumn
tmnxMobPdnGpPeerType = _TmnxMobPdnGpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 23, 1, 8),
    _TmnxMobPdnGpPeerType_Type()
)
tmnxMobPdnGpPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerType.setStatus("current")
_TmnxMobPdnApnExt3Table_Object = MibTable
tmnxMobPdnApnExt3Table = _TmnxMobPdnApnExt3Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnExt3Table.setStatus("current")
_TmnxMobPdnApnExt3Entry_Object = MibTableRow
tmnxMobPdnApnExt3Entry = _TmnxMobPdnApnExt3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnExt3Entry.setStatus("current")
_TmnxMobPdnApnExt3LastChanged_Type = TimeStamp
_TmnxMobPdnApnExt3LastChanged_Object = MibTableColumn
tmnxMobPdnApnExt3LastChanged = _TmnxMobPdnApnExt3LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 1),
    _TmnxMobPdnApnExt3LastChanged_Type()
)
tmnxMobPdnApnExt3LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnExt3LastChanged.setStatus("current")


class _TmnxMobPdnApnAuthPriDiamPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnAuthPriDiamPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnAuthPriDiamPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnAuthPriDiamPeer_Object = MibTableColumn
tmnxMobPdnApnAuthPriDiamPeer = _TmnxMobPdnApnAuthPriDiamPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 2),
    _TmnxMobPdnApnAuthPriDiamPeer_Type()
)
tmnxMobPdnApnAuthPriDiamPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthPriDiamPeer.setStatus("current")


class _TmnxMobPdnApnAuthSecDiamPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnAuthSecDiamPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnAuthSecDiamPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnAuthSecDiamPeer_Object = MibTableColumn
tmnxMobPdnApnAuthSecDiamPeer = _TmnxMobPdnApnAuthSecDiamPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 3),
    _TmnxMobPdnApnAuthSecDiamPeer_Type()
)
tmnxMobPdnApnAuthSecDiamPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthSecDiamPeer.setStatus("current")


class _TmnxMobPdnApnDefAppProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobPdnApnDefAppProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnDefAppProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobPdnApnDefAppProfile_Object = MibTableColumn
tmnxMobPdnApnDefAppProfile = _TmnxMobPdnApnDefAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 4),
    _TmnxMobPdnApnDefAppProfile_Type()
)
tmnxMobPdnApnDefAppProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDefAppProfile.setStatus("current")


class _TmnxMobPdnApnAuthSupImsi_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnApnAuthSupImsi based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnApnAuthSupImsi_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnApnAuthSupImsi_Object = MibTableColumn
tmnxMobPdnApnAuthSupImsi = _TmnxMobPdnApnAuthSupImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 5),
    _TmnxMobPdnApnAuthSupImsi_Type()
)
tmnxMobPdnApnAuthSupImsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAuthSupImsi.setStatus("current")


class _TmnxMobPdnApnAcctSupImsi_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnApnAcctSupImsi based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnApnAcctSupImsi_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnApnAcctSupImsi_Object = MibTableColumn
tmnxMobPdnApnAcctSupImsi = _TmnxMobPdnApnAcctSupImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 6),
    _TmnxMobPdnApnAcctSupImsi_Type()
)
tmnxMobPdnApnAcctSupImsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAcctSupImsi.setStatus("current")


class _TmnxMobPdnApnPreAuthSupImsi_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnApnPreAuthSupImsi based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnApnPreAuthSupImsi_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnApnPreAuthSupImsi_Object = MibTableColumn
tmnxMobPdnApnPreAuthSupImsi = _TmnxMobPdnApnPreAuthSupImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 7),
    _TmnxMobPdnApnPreAuthSupImsi_Type()
)
tmnxMobPdnApnPreAuthSupImsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnPreAuthSupImsi.setStatus("current")


class _TmnxMobPdnApnAaGroupIndex_Type(TmnxBsxIsaAaGroupIndexOrZero):
    """Custom type tmnxMobPdnApnAaGroupIndex based on TmnxBsxIsaAaGroupIndexOrZero"""
    defaultValue = 0


_TmnxMobPdnApnAaGroupIndex_Type.__name__ = "TmnxBsxIsaAaGroupIndexOrZero"
_TmnxMobPdnApnAaGroupIndex_Object = MibTableColumn
tmnxMobPdnApnAaGroupIndex = _TmnxMobPdnApnAaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 8),
    _TmnxMobPdnApnAaGroupIndex_Type()
)
tmnxMobPdnApnAaGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAaGroupIndex.setStatus("current")


class _TmnxMobPdnApnAaGrpPartIndex_Type(TmnxBsxAaGrpPartIndex):
    """Custom type tmnxMobPdnApnAaGrpPartIndex based on TmnxBsxAaGrpPartIndex"""
    defaultValue = 0


_TmnxMobPdnApnAaGrpPartIndex_Type.__name__ = "TmnxBsxAaGrpPartIndex"
_TmnxMobPdnApnAaGrpPartIndex_Object = MibTableColumn
tmnxMobPdnApnAaGrpPartIndex = _TmnxMobPdnApnAaGrpPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 9),
    _TmnxMobPdnApnAaGrpPartIndex_Type()
)
tmnxMobPdnApnAaGrpPartIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAaGrpPartIndex.setStatus("current")


class _TmnxMobPdnApnHttpRedirect_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnApnHttpRedirect based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnApnHttpRedirect_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnApnHttpRedirect_Object = MibTableColumn
tmnxMobPdnApnHttpRedirect = _TmnxMobPdnApnHttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 10),
    _TmnxMobPdnApnHttpRedirect_Type()
)
tmnxMobPdnApnHttpRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnHttpRedirect.setStatus("current")


class _TmnxMobPdnApnRedirTrafficPol_Type(Integer32):
    """Custom type tmnxMobPdnApnRedirTrafficPol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mobileToMobile", 1),
          ("mobileToAll", 2))
    )


_TmnxMobPdnApnRedirTrafficPol_Type.__name__ = "Integer32"
_TmnxMobPdnApnRedirTrafficPol_Object = MibTableColumn
tmnxMobPdnApnRedirTrafficPol = _TmnxMobPdnApnRedirTrafficPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 11),
    _TmnxMobPdnApnRedirTrafficPol_Type()
)
tmnxMobPdnApnRedirTrafficPol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnRedirTrafficPol.setStatus("current")


class _TmnxMobPdnApnRedirPolRouterInst_Type(TmnxVRtrID):
    """Custom type tmnxMobPdnApnRedirPolRouterInst based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobPdnApnRedirPolRouterInst_Type.__name__ = "TmnxVRtrID"
_TmnxMobPdnApnRedirPolRouterInst_Object = MibTableColumn
tmnxMobPdnApnRedirPolRouterInst = _TmnxMobPdnApnRedirPolRouterInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 12),
    _TmnxMobPdnApnRedirPolRouterInst_Type()
)
tmnxMobPdnApnRedirPolRouterInst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnRedirPolRouterInst.setStatus("current")


class _TmnxMobPdnApnRedirPolNHopAddrTyp_Type(InetAddressType):
    """Custom type tmnxMobPdnApnRedirPolNHopAddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxMobPdnApnRedirPolNHopAddrTyp_Type.__name__ = "InetAddressType"
_TmnxMobPdnApnRedirPolNHopAddrTyp_Object = MibTableColumn
tmnxMobPdnApnRedirPolNHopAddrTyp = _TmnxMobPdnApnRedirPolNHopAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 13),
    _TmnxMobPdnApnRedirPolNHopAddrTyp_Type()
)
tmnxMobPdnApnRedirPolNHopAddrTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnRedirPolNHopAddrTyp.setStatus("current")


class _TmnxMobPdnApnRedirPolNHopAddr_Type(InetAddress):
    """Custom type tmnxMobPdnApnRedirPolNHopAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnApnRedirPolNHopAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnApnRedirPolNHopAddr_Object = MibTableColumn
tmnxMobPdnApnRedirPolNHopAddr = _TmnxMobPdnApnRedirPolNHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 14),
    _TmnxMobPdnApnRedirPolNHopAddr_Type()
)
tmnxMobPdnApnRedirPolNHopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnRedirPolNHopAddr.setStatus("current")


class _TmnxMobPdnApnAllowEmergency_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobPdnApnAllowEmergency based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobPdnApnAllowEmergency_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobPdnApnAllowEmergency_Object = MibTableColumn
tmnxMobPdnApnAllowEmergency = _TmnxMobPdnApnAllowEmergency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 24, 1, 15),
    _TmnxMobPdnApnAllowEmergency_Type()
)
tmnxMobPdnApnAllowEmergency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnApnAllowEmergency.setStatus("current")
_TmnxMobPdnGyOcsTable_Object = MibTable
tmnxMobPdnGyOcsTable = _TmnxMobPdnGyOcsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsTable.setStatus("current")
_TmnxMobPdnGyOcsEntry_Object = MibTableRow
tmnxMobPdnGyOcsEntry = _TmnxMobPdnGyOcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1)
)
tmnxMobPdnGyOcsEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsUserRangeName"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsEntry.setStatus("current")
_TmnxMobPdnGyOcsUserRangeName_Type = TNamedItem
_TmnxMobPdnGyOcsUserRangeName_Object = MibTableColumn
tmnxMobPdnGyOcsUserRangeName = _TmnxMobPdnGyOcsUserRangeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1, 1),
    _TmnxMobPdnGyOcsUserRangeName_Type()
)
tmnxMobPdnGyOcsUserRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsUserRangeName.setStatus("current")
_TmnxMobPdnGyOcsRowStatus_Type = RowStatus
_TmnxMobPdnGyOcsRowStatus_Object = MibTableColumn
tmnxMobPdnGyOcsRowStatus = _TmnxMobPdnGyOcsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1, 2),
    _TmnxMobPdnGyOcsRowStatus_Type()
)
tmnxMobPdnGyOcsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsRowStatus.setStatus("current")
_TmnxMobPdnGyOcsLastChanged_Type = TimeStamp
_TmnxMobPdnGyOcsLastChanged_Object = MibTableColumn
tmnxMobPdnGyOcsLastChanged = _TmnxMobPdnGyOcsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1, 3),
    _TmnxMobPdnGyOcsLastChanged_Type()
)
tmnxMobPdnGyOcsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsLastChanged.setStatus("current")
_TmnxMobPdnGyOcsUeStartId_Type = TmnxMobUeStrPrefix
_TmnxMobPdnGyOcsUeStartId_Object = MibTableColumn
tmnxMobPdnGyOcsUeStartId = _TmnxMobPdnGyOcsUeStartId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1, 4),
    _TmnxMobPdnGyOcsUeStartId_Type()
)
tmnxMobPdnGyOcsUeStartId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsUeStartId.setStatus("current")
_TmnxMobPdnGyOcsUeEndId_Type = TmnxMobUeStrPrefix
_TmnxMobPdnGyOcsUeEndId_Object = MibTableColumn
tmnxMobPdnGyOcsUeEndId = _TmnxMobPdnGyOcsUeEndId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1, 5),
    _TmnxMobPdnGyOcsUeEndId_Type()
)
tmnxMobPdnGyOcsUeEndId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsUeEndId.setStatus("current")
_TmnxMobPdnGyOcsPriDiaPeer_Type = TmnxMobProfNameOrEmpty
_TmnxMobPdnGyOcsPriDiaPeer_Object = MibTableColumn
tmnxMobPdnGyOcsPriDiaPeer = _TmnxMobPdnGyOcsPriDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1, 6),
    _TmnxMobPdnGyOcsPriDiaPeer_Type()
)
tmnxMobPdnGyOcsPriDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsPriDiaPeer.setStatus("current")


class _TmnxMobPdnGyOcsSecDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobPdnGyOcsSecDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobPdnGyOcsSecDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobPdnGyOcsSecDiaPeer_Object = MibTableColumn
tmnxMobPdnGyOcsSecDiaPeer = _TmnxMobPdnGyOcsSecDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1, 7),
    _TmnxMobPdnGyOcsSecDiaPeer_Type()
)
tmnxMobPdnGyOcsSecDiaPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsSecDiaPeer.setStatus("current")
_TmnxMobPdnGyOcsDccaProf_Type = TmnxMobProfName
_TmnxMobPdnGyOcsDccaProf_Object = MibTableColumn
tmnxMobPdnGyOcsDccaProf = _TmnxMobPdnGyOcsDccaProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 25, 1, 8),
    _TmnxMobPdnGyOcsDccaProf_Type()
)
tmnxMobPdnGyOcsDccaProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsDccaProf.setStatus("current")
_TmnxMobPdnS6bTable_Object = MibTable
tmnxMobPdnS6bTable = _TmnxMobPdnS6bTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 26)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS6bTable.setStatus("current")
_TmnxMobPdnS6bEntry_Object = MibTableRow
tmnxMobPdnS6bEntry = _TmnxMobPdnS6bEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 26, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS6bEntry.setStatus("current")
_TmnxMobPdnS6bLastChanged_Type = TimeStamp
_TmnxMobPdnS6bLastChanged_Object = MibTableColumn
tmnxMobPdnS6bLastChanged = _TmnxMobPdnS6bLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 26, 1, 1),
    _TmnxMobPdnS6bLastChanged_Type()
)
tmnxMobPdnS6bLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bLastChanged.setStatus("current")


class _TmnxMobPdnS6bTransactionTimer_Type(Unsigned32):
    """Custom type tmnxMobPdnS6bTransactionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_TmnxMobPdnS6bTransactionTimer_Type.__name__ = "Unsigned32"
_TmnxMobPdnS6bTransactionTimer_Object = MibTableColumn
tmnxMobPdnS6bTransactionTimer = _TmnxMobPdnS6bTransactionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 26, 1, 2),
    _TmnxMobPdnS6bTransactionTimer_Type()
)
tmnxMobPdnS6bTransactionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bTransactionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bTransactionTimer.setUnits("seconds")


class _TmnxMobPdnS6bRetryCount_Type(Unsigned32):
    """Custom type tmnxMobPdnS6bRetryCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TmnxMobPdnS6bRetryCount_Type.__name__ = "Unsigned32"
_TmnxMobPdnS6bRetryCount_Object = MibTableColumn
tmnxMobPdnS6bRetryCount = _TmnxMobPdnS6bRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 1, 26, 1, 3),
    _TmnxMobPdnS6bRetryCount_Type()
)
tmnxMobPdnS6bRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bRetryCount.setStatus("current")
_TmnxMobPdnStatObjs_ObjectIdentity = ObjectIdentity
tmnxMobPdnStatObjs = _TmnxMobPdnStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2)
)
_TmnxMobPdnUeTable_Object = MibTable
tmnxMobPdnUeTable = _TmnxMobPdnUeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnUeTable.setStatus("current")
_TmnxMobPdnUeEntry_Object = MibTableRow
tmnxMobPdnUeEntry = _TmnxMobPdnUeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1)
)
tmnxMobPdnUeEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsi"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnUeEntry.setStatus("current")
_TmnxMobPdnUeImsi_Type = TmnxMobUeId
_TmnxMobPdnUeImsi_Object = MibTableColumn
tmnxMobPdnUeImsi = _TmnxMobPdnUeImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 1),
    _TmnxMobPdnUeImsi_Type()
)
tmnxMobPdnUeImsi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnUeImsi.setStatus("current")
_TmnxMobPdnUeRowStatus_Type = RowStatus
_TmnxMobPdnUeRowStatus_Object = MibTableColumn
tmnxMobPdnUeRowStatus = _TmnxMobPdnUeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 2),
    _TmnxMobPdnUeRowStatus_Type()
)
tmnxMobPdnUeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnUeRowStatus.setStatus("current")
_TmnxMobPdnUeMsIsdn_Type = TmnxMobMsisdn
_TmnxMobPdnUeMsIsdn_Object = MibTableColumn
tmnxMobPdnUeMsIsdn = _TmnxMobPdnUeMsIsdn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 3),
    _TmnxMobPdnUeMsIsdn_Type()
)
tmnxMobPdnUeMsIsdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeMsIsdn.setStatus("current")
_TmnxMobPdnUeImei_Type = TmnxMobImei
_TmnxMobPdnUeImei_Object = MibTableColumn
tmnxMobPdnUeImei = _TmnxMobPdnUeImei_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 4),
    _TmnxMobPdnUeImei_Type()
)
tmnxMobPdnUeImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeImei.setStatus("current")
_TmnxMobPdnUeNai_Type = TmnxMobNai
_TmnxMobPdnUeNai_Object = MibTableColumn
tmnxMobPdnUeNai = _TmnxMobPdnUeNai_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 5),
    _TmnxMobPdnUeNai_Type()
)
tmnxMobPdnUeNai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeNai.setStatus("current")
_TmnxMobPdnUeNwkMcc_Type = TmnxMobMcc
_TmnxMobPdnUeNwkMcc_Object = MibTableColumn
tmnxMobPdnUeNwkMcc = _TmnxMobPdnUeNwkMcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 6),
    _TmnxMobPdnUeNwkMcc_Type()
)
tmnxMobPdnUeNwkMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeNwkMcc.setStatus("current")
_TmnxMobPdnUeNwkMnc_Type = TmnxMobMnc
_TmnxMobPdnUeNwkMnc_Object = MibTableColumn
tmnxMobPdnUeNwkMnc = _TmnxMobPdnUeNwkMnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 7),
    _TmnxMobPdnUeNwkMnc_Type()
)
tmnxMobPdnUeNwkMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeNwkMnc.setStatus("current")
_TmnxMobPdnUeTrackingAreaId_Type = Unsigned32
_TmnxMobPdnUeTrackingAreaId_Object = MibTableColumn
tmnxMobPdnUeTrackingAreaId = _TmnxMobPdnUeTrackingAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 8),
    _TmnxMobPdnUeTrackingAreaId_Type()
)
tmnxMobPdnUeTrackingAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeTrackingAreaId.setStatus("current")
_TmnxMobPdnUeCellId_Type = Unsigned32
_TmnxMobPdnUeCellId_Object = MibTableColumn
tmnxMobPdnUeCellId = _TmnxMobPdnUeCellId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 9),
    _TmnxMobPdnUeCellId_Type()
)
tmnxMobPdnUeCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeCellId.setStatus("current")
_TmnxMobPdnUeState_Type = TmnxMobUeState
_TmnxMobPdnUeState_Object = MibTableColumn
tmnxMobPdnUeState = _TmnxMobPdnUeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 10),
    _TmnxMobPdnUeState_Type()
)
tmnxMobPdnUeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeState.setStatus("current")
_TmnxMobPdnUeRat_Type = TmnxMobUeRat
_TmnxMobPdnUeRat_Object = MibTableColumn
tmnxMobPdnUeRat = _TmnxMobPdnUeRat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 11),
    _TmnxMobPdnUeRat_Type()
)
tmnxMobPdnUeRat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeRat.setStatus("current")
_TmnxMobPdnUePdnContexts_Type = Unsigned32
_TmnxMobPdnUePdnContexts_Object = MibTableColumn
tmnxMobPdnUePdnContexts = _TmnxMobPdnUePdnContexts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 12),
    _TmnxMobPdnUePdnContexts_Type()
)
tmnxMobPdnUePdnContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUePdnContexts.setStatus("current")
_TmnxMobPdnUeBearerContexts_Type = Unsigned32
_TmnxMobPdnUeBearerContexts_Object = MibTableColumn
tmnxMobPdnUeBearerContexts = _TmnxMobPdnUeBearerContexts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 13),
    _TmnxMobPdnUeBearerContexts_Type()
)
tmnxMobPdnUeBearerContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeBearerContexts.setStatus("current")
_TmnxMobPdnUeRfPgwAddrType_Type = InetAddressType
_TmnxMobPdnUeRfPgwAddrType_Object = MibTableColumn
tmnxMobPdnUeRfPgwAddrType = _TmnxMobPdnUeRfPgwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 14),
    _TmnxMobPdnUeRfPgwAddrType_Type()
)
tmnxMobPdnUeRfPgwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeRfPgwAddrType.setStatus("current")


class _TmnxMobPdnUeRfPgwAddr_Type(InetAddress):
    """Custom type tmnxMobPdnUeRfPgwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnUeRfPgwAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnUeRfPgwAddr_Object = MibTableColumn
tmnxMobPdnUeRfPgwAddr = _TmnxMobPdnUeRfPgwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 15),
    _TmnxMobPdnUeRfPgwAddr_Type()
)
tmnxMobPdnUeRfPgwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeRfPgwAddr.setStatus("current")
_TmnxMobPdnUeCtxAccessType_Type = TmnxMobAccessType
_TmnxMobPdnUeCtxAccessType_Object = MibTableColumn
tmnxMobPdnUeCtxAccessType = _TmnxMobPdnUeCtxAccessType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 16),
    _TmnxMobPdnUeCtxAccessType_Type()
)
tmnxMobPdnUeCtxAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeCtxAccessType.setStatus("current")
_TmnxMobPdnUeSubType_Type = TmnxMobUeSubType
_TmnxMobPdnUeSubType_Object = MibTableColumn
tmnxMobPdnUeSubType = _TmnxMobPdnUeSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 17),
    _TmnxMobPdnUeSubType_Type()
)
tmnxMobPdnUeSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeSubType.setStatus("current")
_TmnxMobPdnKeyType_Type = TmnxMobUeIdType
_TmnxMobPdnKeyType_Object = MibTableColumn
tmnxMobPdnKeyType = _TmnxMobPdnKeyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 18),
    _TmnxMobPdnKeyType_Type()
)
tmnxMobPdnKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobPdnKeyType.setStatus("current")
_TmnxMobPdnUeImsiStr_Type = TmnxMobImsiStr
_TmnxMobPdnUeImsiStr_Object = MibTableColumn
tmnxMobPdnUeImsiStr = _TmnxMobPdnUeImsiStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 1, 1, 19),
    _TmnxMobPdnUeImsiStr_Type()
)
tmnxMobPdnUeImsiStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnUeImsiStr.setStatus("current")
_TmnxMobPdnPdnContextTable_Object = MibTable
tmnxMobPdnPdnContextTable = _TmnxMobPdnPdnContextTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxMobPdnPdnContextTable.setStatus("current")
_TmnxMobPdnPdnContextEntry_Object = MibTableRow
tmnxMobPdnPdnContextEntry = _TmnxMobPdnPdnContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1)
)
tmnxMobPdnPdnContextEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsi"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcApn"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPdnType"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnPdnContextEntry.setStatus("current")
_TmnxMobPdnPcApn_Type = TmnxMobApn
_TmnxMobPdnPcApn_Object = MibTableColumn
tmnxMobPdnPcApn = _TmnxMobPdnPcApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 1),
    _TmnxMobPdnPcApn_Type()
)
tmnxMobPdnPcApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnPcApn.setStatus("current")
_TmnxMobPdnPcPdnType_Type = TmnxMobPdnType
_TmnxMobPdnPcPdnType_Object = MibTableColumn
tmnxMobPdnPcPdnType = _TmnxMobPdnPcPdnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 2),
    _TmnxMobPdnPcPdnType_Type()
)
tmnxMobPdnPcPdnType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnPcPdnType.setStatus("current")
_TmnxMobPdnPcLinkedBearerId_Type = TmnxMobBearerId
_TmnxMobPdnPcLinkedBearerId_Object = MibTableColumn
tmnxMobPdnPcLinkedBearerId = _TmnxMobPdnPcLinkedBearerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 3),
    _TmnxMobPdnPcLinkedBearerId_Type()
)
tmnxMobPdnPcLinkedBearerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcLinkedBearerId.setStatus("current")
_TmnxMobPdnPcApnRestriction_Type = Unsigned32
_TmnxMobPdnPcApnRestriction_Object = MibTableColumn
tmnxMobPdnPcApnRestriction = _TmnxMobPdnPcApnRestriction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 4),
    _TmnxMobPdnPcApnRestriction_Type()
)
tmnxMobPdnPcApnRestriction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcApnRestriction.setStatus("current")
_TmnxMobPdnPcUlApnAmbr_Type = Unsigned32
_TmnxMobPdnPcUlApnAmbr_Object = MibTableColumn
tmnxMobPdnPcUlApnAmbr = _TmnxMobPdnPcUlApnAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 5),
    _TmnxMobPdnPcUlApnAmbr_Type()
)
tmnxMobPdnPcUlApnAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcUlApnAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnPcUlApnAmbr.setUnits("kbps")
_TmnxMobPdnPcDlApnAmbr_Type = Unsigned32
_TmnxMobPdnPcDlApnAmbr_Object = MibTableColumn
tmnxMobPdnPcDlApnAmbr = _TmnxMobPdnPcDlApnAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 6),
    _TmnxMobPdnPcDlApnAmbr_Type()
)
tmnxMobPdnPcDlApnAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcDlApnAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnPcDlApnAmbr.setUnits("kbps")
_TmnxMobPdnPcIpv4AddressType_Type = InetAddressType
_TmnxMobPdnPcIpv4AddressType_Object = MibTableColumn
tmnxMobPdnPcIpv4AddressType = _TmnxMobPdnPcIpv4AddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 7),
    _TmnxMobPdnPcIpv4AddressType_Type()
)
tmnxMobPdnPcIpv4AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIpv4AddressType.setStatus("current")


class _TmnxMobPdnPcIpv4Address_Type(InetAddress):
    """Custom type tmnxMobPdnPcIpv4Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnPcIpv4Address_Type.__name__ = "InetAddress"
_TmnxMobPdnPcIpv4Address_Object = MibTableColumn
tmnxMobPdnPcIpv4Address = _TmnxMobPdnPcIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 8),
    _TmnxMobPdnPcIpv4Address_Type()
)
tmnxMobPdnPcIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIpv4Address.setStatus("current")
_TmnxMobPdnPcIpv6AddressType_Type = InetAddressType
_TmnxMobPdnPcIpv6AddressType_Object = MibTableColumn
tmnxMobPdnPcIpv6AddressType = _TmnxMobPdnPcIpv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 9),
    _TmnxMobPdnPcIpv6AddressType_Type()
)
tmnxMobPdnPcIpv6AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIpv6AddressType.setStatus("current")


class _TmnxMobPdnPcIpv6Address_Type(InetAddress):
    """Custom type tmnxMobPdnPcIpv6Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnPcIpv6Address_Type.__name__ = "InetAddress"
_TmnxMobPdnPcIpv6Address_Object = MibTableColumn
tmnxMobPdnPcIpv6Address = _TmnxMobPdnPcIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 10),
    _TmnxMobPdnPcIpv6Address_Type()
)
tmnxMobPdnPcIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIpv6Address.setStatus("current")
_TmnxMobPdnPcBearerContexts_Type = Unsigned32
_TmnxMobPdnPcBearerContexts_Object = MibTableColumn
tmnxMobPdnPcBearerContexts = _TmnxMobPdnPcBearerContexts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 11),
    _TmnxMobPdnPcBearerContexts_Type()
)
tmnxMobPdnPcBearerContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcBearerContexts.setStatus("current")
_TmnxMobPdnPcSessionState_Type = TmnxMobPdnSessionState
_TmnxMobPdnPcSessionState_Object = MibTableColumn
tmnxMobPdnPcSessionState = _TmnxMobPdnPcSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 12),
    _TmnxMobPdnPcSessionState_Type()
)
tmnxMobPdnPcSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSessionState.setStatus("current")
_TmnxMobPdnPcLastEvent_Type = TmnxMobPdnSessionEvent
_TmnxMobPdnPcLastEvent_Object = MibTableColumn
tmnxMobPdnPcLastEvent = _TmnxMobPdnPcLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 13),
    _TmnxMobPdnPcLastEvent_Type()
)
tmnxMobPdnPcLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcLastEvent.setStatus("current")
_TmnxMobPdnPcSigProtocol_Type = TmnxMobPgwSigProtocol
_TmnxMobPdnPcSigProtocol_Object = MibTableColumn
tmnxMobPdnPcSigProtocol = _TmnxMobPdnPcSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 14),
    _TmnxMobPdnPcSigProtocol_Type()
)
tmnxMobPdnPcSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSigProtocol.setStatus("current")
_TmnxMobPdnPcTnlRemoteCtrlTeid_Type = Unsigned32
_TmnxMobPdnPcTnlRemoteCtrlTeid_Object = MibTableColumn
tmnxMobPdnPcTnlRemoteCtrlTeid = _TmnxMobPdnPcTnlRemoteCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 15),
    _TmnxMobPdnPcTnlRemoteCtrlTeid_Type()
)
tmnxMobPdnPcTnlRemoteCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlRemoteCtrlTeid.setStatus("current")
_TmnxMobPdnPcTnlRemoteCtrlAddrTyp_Type = InetAddressType
_TmnxMobPdnPcTnlRemoteCtrlAddrTyp_Object = MibTableColumn
tmnxMobPdnPcTnlRemoteCtrlAddrTyp = _TmnxMobPdnPcTnlRemoteCtrlAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 16),
    _TmnxMobPdnPcTnlRemoteCtrlAddrTyp_Type()
)
tmnxMobPdnPcTnlRemoteCtrlAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlRemoteCtrlAddrTyp.setStatus("current")


class _TmnxMobPdnPcTnlRemoteCtrlAddr_Type(InetAddress):
    """Custom type tmnxMobPdnPcTnlRemoteCtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnPcTnlRemoteCtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnPcTnlRemoteCtrlAddr_Object = MibTableColumn
tmnxMobPdnPcTnlRemoteCtrlAddr = _TmnxMobPdnPcTnlRemoteCtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 17),
    _TmnxMobPdnPcTnlRemoteCtrlAddr_Type()
)
tmnxMobPdnPcTnlRemoteCtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlRemoteCtrlAddr.setStatus("current")
_TmnxMobPdnPcTnlRemV6CtrlAddrTyp_Type = InetAddressType
_TmnxMobPdnPcTnlRemV6CtrlAddrTyp_Object = MibTableColumn
tmnxMobPdnPcTnlRemV6CtrlAddrTyp = _TmnxMobPdnPcTnlRemV6CtrlAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 18),
    _TmnxMobPdnPcTnlRemV6CtrlAddrTyp_Type()
)
tmnxMobPdnPcTnlRemV6CtrlAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlRemV6CtrlAddrTyp.setStatus("current")


class _TmnxMobPdnPcTnlRemV6CtrlAddr_Type(InetAddress):
    """Custom type tmnxMobPdnPcTnlRemV6CtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnPcTnlRemV6CtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnPcTnlRemV6CtrlAddr_Object = MibTableColumn
tmnxMobPdnPcTnlRemV6CtrlAddr = _TmnxMobPdnPcTnlRemV6CtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 19),
    _TmnxMobPdnPcTnlRemV6CtrlAddr_Type()
)
tmnxMobPdnPcTnlRemV6CtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlRemV6CtrlAddr.setStatus("current")
_TmnxMobPdnPcTnlLocalCtrlTeid_Type = Unsigned32
_TmnxMobPdnPcTnlLocalCtrlTeid_Object = MibTableColumn
tmnxMobPdnPcTnlLocalCtrlTeid = _TmnxMobPdnPcTnlLocalCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 20),
    _TmnxMobPdnPcTnlLocalCtrlTeid_Type()
)
tmnxMobPdnPcTnlLocalCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlLocalCtrlTeid.setStatus("current")
_TmnxMobPdnPcTnlLocalCtrlAddrType_Type = InetAddressType
_TmnxMobPdnPcTnlLocalCtrlAddrType_Object = MibTableColumn
tmnxMobPdnPcTnlLocalCtrlAddrType = _TmnxMobPdnPcTnlLocalCtrlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 21),
    _TmnxMobPdnPcTnlLocalCtrlAddrType_Type()
)
tmnxMobPdnPcTnlLocalCtrlAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlLocalCtrlAddrType.setStatus("current")


class _TmnxMobPdnPcTnlLocalCtrlAddr_Type(InetAddress):
    """Custom type tmnxMobPdnPcTnlLocalCtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobPdnPcTnlLocalCtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnPcTnlLocalCtrlAddr_Object = MibTableColumn
tmnxMobPdnPcTnlLocalCtrlAddr = _TmnxMobPdnPcTnlLocalCtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 22),
    _TmnxMobPdnPcTnlLocalCtrlAddr_Type()
)
tmnxMobPdnPcTnlLocalCtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlLocalCtrlAddr.setStatus("current")
_TmnxMobPdnPcTnlLocalV6CtrlAdrTyp_Type = InetAddressType
_TmnxMobPdnPcTnlLocalV6CtrlAdrTyp_Object = MibTableColumn
tmnxMobPdnPcTnlLocalV6CtrlAdrTyp = _TmnxMobPdnPcTnlLocalV6CtrlAdrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 23),
    _TmnxMobPdnPcTnlLocalV6CtrlAdrTyp_Type()
)
tmnxMobPdnPcTnlLocalV6CtrlAdrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlLocalV6CtrlAdrTyp.setStatus("current")


class _TmnxMobPdnPcTnlLocalV6CtrlAddr_Type(InetAddress):
    """Custom type tmnxMobPdnPcTnlLocalV6CtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnPcTnlLocalV6CtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnPcTnlLocalV6CtrlAddr_Object = MibTableColumn
tmnxMobPdnPcTnlLocalV6CtrlAddr = _TmnxMobPdnPcTnlLocalV6CtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 24),
    _TmnxMobPdnPcTnlLocalV6CtrlAddr_Type()
)
tmnxMobPdnPcTnlLocalV6CtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlLocalV6CtrlAddr.setStatus("current")
_TmnxMobPdnPcOfcBearerType_Type = TmnxMobChargingBearerType
_TmnxMobPdnPcOfcBearerType_Object = MibTableColumn
tmnxMobPdnPcOfcBearerType = _TmnxMobPdnPcOfcBearerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 25),
    _TmnxMobPdnPcOfcBearerType_Type()
)
tmnxMobPdnPcOfcBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcOfcBearerType.setStatus("current")
_TmnxMobPdnPcPcrfEventTriggers_Type = Unsigned32
_TmnxMobPdnPcPcrfEventTriggers_Object = MibTableColumn
tmnxMobPdnPcPcrfEventTriggers = _TmnxMobPdnPcPcrfEventTriggers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 26),
    _TmnxMobPdnPcPcrfEventTriggers_Type()
)
tmnxMobPdnPcPcrfEventTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcPcrfEventTriggers.setStatus("current")
_TmnxMobPdnPcGxPcrfAddressType_Type = InetAddressType
_TmnxMobPdnPcGxPcrfAddressType_Object = MibTableColumn
tmnxMobPdnPcGxPcrfAddressType = _TmnxMobPdnPcGxPcrfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 27),
    _TmnxMobPdnPcGxPcrfAddressType_Type()
)
tmnxMobPdnPcGxPcrfAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcGxPcrfAddressType.setStatus("current")


class _TmnxMobPdnPcGxPcrfAddress_Type(InetAddress):
    """Custom type tmnxMobPdnPcGxPcrfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnPcGxPcrfAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnPcGxPcrfAddress_Object = MibTableColumn
tmnxMobPdnPcGxPcrfAddress = _TmnxMobPdnPcGxPcrfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 28),
    _TmnxMobPdnPcGxPcrfAddress_Type()
)
tmnxMobPdnPcGxPcrfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcGxPcrfAddress.setStatus("current")
_TmnxMobPdnPcGxPgwAddressType_Type = InetAddressType
_TmnxMobPdnPcGxPgwAddressType_Object = MibTableColumn
tmnxMobPdnPcGxPgwAddressType = _TmnxMobPdnPcGxPgwAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 29),
    _TmnxMobPdnPcGxPgwAddressType_Type()
)
tmnxMobPdnPcGxPgwAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcGxPgwAddressType.setStatus("current")


class _TmnxMobPdnPcGxPgwAddress_Type(InetAddress):
    """Custom type tmnxMobPdnPcGxPgwAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnPcGxPgwAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnPcGxPgwAddress_Object = MibTableColumn
tmnxMobPdnPcGxPgwAddress = _TmnxMobPdnPcGxPgwAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 30),
    _TmnxMobPdnPcGxPgwAddress_Type()
)
tmnxMobPdnPcGxPgwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcGxPgwAddress.setStatus("current")
_TmnxMobPdnPcAccessType_Type = TmnxMobAccessType
_TmnxMobPdnPcAccessType_Object = MibTableColumn
tmnxMobPdnPcAccessType = _TmnxMobPdnPcAccessType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 31),
    _TmnxMobPdnPcAccessType_Type()
)
tmnxMobPdnPcAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAccessType.setStatus("current")


class _TmnxMobPdnPcSelectionMode_Type(Integer32):
    """Custom type tmnxMobPdnPcSelectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("subscribed", 0),
          ("sentByMs", 1),
          ("chosenByServNode", 2))
    )


_TmnxMobPdnPcSelectionMode_Type.__name__ = "Integer32"
_TmnxMobPdnPcSelectionMode_Object = MibTableColumn
tmnxMobPdnPcSelectionMode = _TmnxMobPdnPcSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 32),
    _TmnxMobPdnPcSelectionMode_Type()
)
tmnxMobPdnPcSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSelectionMode.setStatus("current")
_TmnxMobPdnPcTnlLocalDataAddrType_Type = InetAddressType
_TmnxMobPdnPcTnlLocalDataAddrType_Object = MibTableColumn
tmnxMobPdnPcTnlLocalDataAddrType = _TmnxMobPdnPcTnlLocalDataAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 33),
    _TmnxMobPdnPcTnlLocalDataAddrType_Type()
)
tmnxMobPdnPcTnlLocalDataAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlLocalDataAddrType.setStatus("current")


class _TmnxMobPdnPcTnlLocalDataAddr_Type(InetAddress):
    """Custom type tmnxMobPdnPcTnlLocalDataAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnPcTnlLocalDataAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnPcTnlLocalDataAddr_Object = MibTableColumn
tmnxMobPdnPcTnlLocalDataAddr = _TmnxMobPdnPcTnlLocalDataAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 34),
    _TmnxMobPdnPcTnlLocalDataAddr_Type()
)
tmnxMobPdnPcTnlLocalDataAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlLocalDataAddr.setStatus("current")
_TmnxMobPdnPcPGWGREkey_Type = Unsigned32
_TmnxMobPdnPcPGWGREkey_Object = MibTableColumn
tmnxMobPdnPcPGWGREkey = _TmnxMobPdnPcPGWGREkey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 35),
    _TmnxMobPdnPcPGWGREkey_Type()
)
tmnxMobPdnPcPGWGREkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcPGWGREkey.setStatus("current")
_TmnxMobPdnPcMAGGREkey_Type = Unsigned32
_TmnxMobPdnPcMAGGREkey_Object = MibTableColumn
tmnxMobPdnPcMAGGREkey = _TmnxMobPdnPcMAGGREkey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 36),
    _TmnxMobPdnPcMAGGREkey_Type()
)
tmnxMobPdnPcMAGGREkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcMAGGREkey.setStatus("current")
_TmnxMobPdnPcTnlRemoteDataAddrTyp_Type = InetAddressType
_TmnxMobPdnPcTnlRemoteDataAddrTyp_Object = MibTableColumn
tmnxMobPdnPcTnlRemoteDataAddrTyp = _TmnxMobPdnPcTnlRemoteDataAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 37),
    _TmnxMobPdnPcTnlRemoteDataAddrTyp_Type()
)
tmnxMobPdnPcTnlRemoteDataAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlRemoteDataAddrTyp.setStatus("current")


class _TmnxMobPdnPcTnlRemoteDataAddr_Type(InetAddress):
    """Custom type tmnxMobPdnPcTnlRemoteDataAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnPcTnlRemoteDataAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnPcTnlRemoteDataAddr_Object = MibTableColumn
tmnxMobPdnPcTnlRemoteDataAddr = _TmnxMobPdnPcTnlRemoteDataAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 38),
    _TmnxMobPdnPcTnlRemoteDataAddr_Type()
)
tmnxMobPdnPcTnlRemoteDataAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlRemoteDataAddr.setStatus("current")
_TmnxMobPdnPcRfSrvAddrType_Type = InetAddressType
_TmnxMobPdnPcRfSrvAddrType_Object = MibTableColumn
tmnxMobPdnPcRfSrvAddrType = _TmnxMobPdnPcRfSrvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 39),
    _TmnxMobPdnPcRfSrvAddrType_Type()
)
tmnxMobPdnPcRfSrvAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfSrvAddrType.setStatus("current")


class _TmnxMobPdnPcRfSrvAddr_Type(InetAddress):
    """Custom type tmnxMobPdnPcRfSrvAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnPcRfSrvAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnPcRfSrvAddr_Object = MibTableColumn
tmnxMobPdnPcRfSrvAddr = _TmnxMobPdnPcRfSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 40),
    _TmnxMobPdnPcRfSrvAddr_Type()
)
tmnxMobPdnPcRfSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfSrvAddr.setStatus("current")
_TmnxMobPdnPcRfServerState_Type = TmnxMobServerState
_TmnxMobPdnPcRfServerState_Object = MibTableColumn
tmnxMobPdnPcRfServerState = _TmnxMobPdnPcRfServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 41),
    _TmnxMobPdnPcRfServerState_Type()
)
tmnxMobPdnPcRfServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfServerState.setStatus("current")
_TmnxMobPdnPcRfChargingLevel_Type = TmnxMobChargingLevel
_TmnxMobPdnPcRfChargingLevel_Object = MibTableColumn
tmnxMobPdnPcRfChargingLevel = _TmnxMobPdnPcRfChargingLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 42),
    _TmnxMobPdnPcRfChargingLevel_Type()
)
tmnxMobPdnPcRfChargingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChargingLevel.setStatus("current")
_TmnxMobPdnPcRfChargingProfile_Type = TmnxMobChargingProfile
_TmnxMobPdnPcRfChargingProfile_Object = MibTableColumn
tmnxMobPdnPcRfChargingProfile = _TmnxMobPdnPcRfChargingProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 43),
    _TmnxMobPdnPcRfChargingProfile_Type()
)
tmnxMobPdnPcRfChargingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChargingProfile.setStatus("current")
_TmnxMobPdnPcRfInterimRecords_Type = Unsigned32
_TmnxMobPdnPcRfInterimRecords_Object = MibTableColumn
tmnxMobPdnPcRfInterimRecords = _TmnxMobPdnPcRfInterimRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 44),
    _TmnxMobPdnPcRfInterimRecords_Type()
)
tmnxMobPdnPcRfInterimRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfInterimRecords.setStatus("current")
_TmnxMobPdnPcRfTriggeredRecords_Type = Unsigned32
_TmnxMobPdnPcRfTriggeredRecords_Object = MibTableColumn
tmnxMobPdnPcRfTriggeredRecords = _TmnxMobPdnPcRfTriggeredRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 45),
    _TmnxMobPdnPcRfTriggeredRecords_Type()
)
tmnxMobPdnPcRfTriggeredRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfTriggeredRecords.setStatus("current")
_TmnxMobPdnPcTnlDLPackets_Type = Counter64
_TmnxMobPdnPcTnlDLPackets_Object = MibTableColumn
tmnxMobPdnPcTnlDLPackets = _TmnxMobPdnPcTnlDLPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 46),
    _TmnxMobPdnPcTnlDLPackets_Type()
)
tmnxMobPdnPcTnlDLPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlDLPackets.setStatus("current")
_TmnxMobPdnPcTnlDLBytes_Type = Counter64
_TmnxMobPdnPcTnlDLBytes_Object = MibTableColumn
tmnxMobPdnPcTnlDLBytes = _TmnxMobPdnPcTnlDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 47),
    _TmnxMobPdnPcTnlDLBytes_Type()
)
tmnxMobPdnPcTnlDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlDLBytes.setStatus("current")
_TmnxMobPdnPcSgiULPackets_Type = Counter64
_TmnxMobPdnPcSgiULPackets_Object = MibTableColumn
tmnxMobPdnPcSgiULPackets = _TmnxMobPdnPcSgiULPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 48),
    _TmnxMobPdnPcSgiULPackets_Type()
)
tmnxMobPdnPcSgiULPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSgiULPackets.setStatus("current")
_TmnxMobPdnPcSgiULBytes_Type = Counter64
_TmnxMobPdnPcSgiULBytes_Object = MibTableColumn
tmnxMobPdnPcSgiULBytes = _TmnxMobPdnPcSgiULBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 49),
    _TmnxMobPdnPcSgiULBytes_Type()
)
tmnxMobPdnPcSgiULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSgiULBytes.setStatus("current")
_TmnxMobPdnPcTnlDLPacketsLow_Type = Counter32
_TmnxMobPdnPcTnlDLPacketsLow_Object = MibTableColumn
tmnxMobPdnPcTnlDLPacketsLow = _TmnxMobPdnPcTnlDLPacketsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 50),
    _TmnxMobPdnPcTnlDLPacketsLow_Type()
)
tmnxMobPdnPcTnlDLPacketsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlDLPacketsLow.setStatus("current")
_TmnxMobPdnPcTnlDLPacketsHigh_Type = Counter32
_TmnxMobPdnPcTnlDLPacketsHigh_Object = MibTableColumn
tmnxMobPdnPcTnlDLPacketsHigh = _TmnxMobPdnPcTnlDLPacketsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 51),
    _TmnxMobPdnPcTnlDLPacketsHigh_Type()
)
tmnxMobPdnPcTnlDLPacketsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlDLPacketsHigh.setStatus("current")
_TmnxMobPdnPcTnlDLBytesLow_Type = Counter32
_TmnxMobPdnPcTnlDLBytesLow_Object = MibTableColumn
tmnxMobPdnPcTnlDLBytesLow = _TmnxMobPdnPcTnlDLBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 52),
    _TmnxMobPdnPcTnlDLBytesLow_Type()
)
tmnxMobPdnPcTnlDLBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlDLBytesLow.setStatus("current")
_TmnxMobPdnPcTnlDLBytesHigh_Type = Counter32
_TmnxMobPdnPcTnlDLBytesHigh_Object = MibTableColumn
tmnxMobPdnPcTnlDLBytesHigh = _TmnxMobPdnPcTnlDLBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 53),
    _TmnxMobPdnPcTnlDLBytesHigh_Type()
)
tmnxMobPdnPcTnlDLBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcTnlDLBytesHigh.setStatus("current")
_TmnxMobPdnPcSgiULPacketsLow_Type = Counter32
_TmnxMobPdnPcSgiULPacketsLow_Object = MibTableColumn
tmnxMobPdnPcSgiULPacketsLow = _TmnxMobPdnPcSgiULPacketsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 54),
    _TmnxMobPdnPcSgiULPacketsLow_Type()
)
tmnxMobPdnPcSgiULPacketsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSgiULPacketsLow.setStatus("current")
_TmnxMobPdnPcSgiULPacketsHigh_Type = Counter32
_TmnxMobPdnPcSgiULPacketsHigh_Object = MibTableColumn
tmnxMobPdnPcSgiULPacketsHigh = _TmnxMobPdnPcSgiULPacketsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 55),
    _TmnxMobPdnPcSgiULPacketsHigh_Type()
)
tmnxMobPdnPcSgiULPacketsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSgiULPacketsHigh.setStatus("current")
_TmnxMobPdnPcSgiULBytesLow_Type = Counter32
_TmnxMobPdnPcSgiULBytesLow_Object = MibTableColumn
tmnxMobPdnPcSgiULBytesLow = _TmnxMobPdnPcSgiULBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 56),
    _TmnxMobPdnPcSgiULBytesLow_Type()
)
tmnxMobPdnPcSgiULBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSgiULBytesLow.setStatus("current")
_TmnxMobPdnPcSgiULBytesHigh_Type = Counter32
_TmnxMobPdnPcSgiULBytesHigh_Object = MibTableColumn
tmnxMobPdnPcSgiULBytesHigh = _TmnxMobPdnPcSgiULBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 57),
    _TmnxMobPdnPcSgiULBytesHigh_Type()
)
tmnxMobPdnPcSgiULBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSgiULBytesHigh.setStatus("current")


class _TmnxMobPdnPcImsiAuthStatus_Type(Integer32):
    """Custom type tmnxMobPdnPcImsiAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("authenticated", 1),
          ("unauthenticated", 2))
    )


_TmnxMobPdnPcImsiAuthStatus_Type.__name__ = "Integer32"
_TmnxMobPdnPcImsiAuthStatus_Object = MibTableColumn
tmnxMobPdnPcImsiAuthStatus = _TmnxMobPdnPcImsiAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 58),
    _TmnxMobPdnPcImsiAuthStatus_Type()
)
tmnxMobPdnPcImsiAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcImsiAuthStatus.setStatus("current")
_TmnxMobPdnPcImeiStr_Type = TmnxMobImei
_TmnxMobPdnPcImeiStr_Object = MibTableColumn
tmnxMobPdnPcImeiStr = _TmnxMobPdnPcImeiStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 59),
    _TmnxMobPdnPcImeiStr_Type()
)
tmnxMobPdnPcImeiStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcImeiStr.setStatus("current")
_TmnxMobPdnPcImsiStr_Type = TmnxMobImsiStr
_TmnxMobPdnPcImsiStr_Object = MibTableColumn
tmnxMobPdnPcImsiStr = _TmnxMobPdnPcImsiStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 60),
    _TmnxMobPdnPcImsiStr_Type()
)
tmnxMobPdnPcImsiStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcImsiStr.setStatus("current")
_TmnxMobPdnPcSessConfigTime_Type = Counter32
_TmnxMobPdnPcSessConfigTime_Object = MibTableColumn
tmnxMobPdnPcSessConfigTime = _TmnxMobPdnPcSessConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 61),
    _TmnxMobPdnPcSessConfigTime_Type()
)
tmnxMobPdnPcSessConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSessConfigTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSessConfigTime.setUnits("seconds")
_TmnxMobPdnPcSessRemExpTime_Type = Counter32
_TmnxMobPdnPcSessRemExpTime_Object = MibTableColumn
tmnxMobPdnPcSessRemExpTime = _TmnxMobPdnPcSessRemExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 62),
    _TmnxMobPdnPcSessRemExpTime_Type()
)
tmnxMobPdnPcSessRemExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSessRemExpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSessRemExpTime.setUnits("seconds")


class _TmnxMobPdnPcSessTimeDerivedFrom_Type(Integer32):
    """Custom type tmnxMobPdnPcSessTimeDerivedFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("radius", 1))
    )


_TmnxMobPdnPcSessTimeDerivedFrom_Type.__name__ = "Integer32"
_TmnxMobPdnPcSessTimeDerivedFrom_Object = MibTableColumn
tmnxMobPdnPcSessTimeDerivedFrom = _TmnxMobPdnPcSessTimeDerivedFrom_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 63),
    _TmnxMobPdnPcSessTimeDerivedFrom_Type()
)
tmnxMobPdnPcSessTimeDerivedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcSessTimeDerivedFrom.setStatus("current")
_TmnxMobPdnPcIdleConfigTime_Type = Counter32
_TmnxMobPdnPcIdleConfigTime_Object = MibTableColumn
tmnxMobPdnPcIdleConfigTime = _TmnxMobPdnPcIdleConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 64),
    _TmnxMobPdnPcIdleConfigTime_Type()
)
tmnxMobPdnPcIdleConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIdleConfigTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIdleConfigTime.setUnits("seconds")
_TmnxMobPdnPcIdleRemExpTime_Type = Counter32
_TmnxMobPdnPcIdleRemExpTime_Object = MibTableColumn
tmnxMobPdnPcIdleRemExpTime = _TmnxMobPdnPcIdleRemExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 65),
    _TmnxMobPdnPcIdleRemExpTime_Type()
)
tmnxMobPdnPcIdleRemExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIdleRemExpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIdleRemExpTime.setUnits("seconds")


class _TmnxMobPdnPcIdleTimeDerivedFrom_Type(Integer32):
    """Custom type tmnxMobPdnPcIdleTimeDerivedFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("radius", 1))
    )


_TmnxMobPdnPcIdleTimeDerivedFrom_Type.__name__ = "Integer32"
_TmnxMobPdnPcIdleTimeDerivedFrom_Object = MibTableColumn
tmnxMobPdnPcIdleTimeDerivedFrom = _TmnxMobPdnPcIdleTimeDerivedFrom_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 66),
    _TmnxMobPdnPcIdleTimeDerivedFrom_Type()
)
tmnxMobPdnPcIdleTimeDerivedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcIdleTimeDerivedFrom.setStatus("current")
_TmnxMobPdnPcRefPointType_Type = TmnxMobPdnRefPointType
_TmnxMobPdnPcRefPointType_Object = MibTableColumn
tmnxMobPdnPcRefPointType = _TmnxMobPdnPcRefPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 2, 1, 67),
    _TmnxMobPdnPcRefPointType_Type()
)
tmnxMobPdnPcRefPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRefPointType.setStatus("current")
_TmnxMobPdnBearerContextTable_Object = MibTable
tmnxMobPdnBearerContextTable = _TmnxMobPdnBearerContextTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBearerContextTable.setStatus("current")
_TmnxMobPdnBearerContextEntry_Object = MibTableRow
tmnxMobPdnBearerContextEntry = _TmnxMobPdnBearerContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1)
)
tmnxMobPdnBearerContextEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsi"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcApn"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPdnType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcBearerId"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnBearerContextEntry.setStatus("current")
_TmnxMobPdnBcBearerId_Type = TmnxMobBearerId
_TmnxMobPdnBcBearerId_Object = MibTableColumn
tmnxMobPdnBcBearerId = _TmnxMobPdnBcBearerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 1),
    _TmnxMobPdnBcBearerId_Type()
)
tmnxMobPdnBcBearerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnBcBearerId.setStatus("current")
_TmnxMobPdnBcBearerType_Type = TmnxMobBearerType
_TmnxMobPdnBcBearerType_Object = MibTableColumn
tmnxMobPdnBcBearerType = _TmnxMobPdnBcBearerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 2),
    _TmnxMobPdnBcBearerType_Type()
)
tmnxMobPdnBcBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcBearerType.setStatus("current")
_TmnxMobPdnBcUpTime_Type = Unsigned32
_TmnxMobPdnBcUpTime_Object = MibTableColumn
tmnxMobPdnBcUpTime = _TmnxMobPdnBcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 3),
    _TmnxMobPdnBcUpTime_Type()
)
tmnxMobPdnBcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcUpTime.setUnits("seconds")
_TmnxMobPdnBcQci_Type = TmnxMobQci
_TmnxMobPdnBcQci_Object = MibTableColumn
tmnxMobPdnBcQci = _TmnxMobPdnBcQci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 4),
    _TmnxMobPdnBcQci_Type()
)
tmnxMobPdnBcQci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcQci.setStatus("current")
_TmnxMobPdnBcArp_Type = TmnxMobArp
_TmnxMobPdnBcArp_Object = MibTableColumn
tmnxMobPdnBcArp = _TmnxMobPdnBcArp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 5),
    _TmnxMobPdnBcArp_Type()
)
tmnxMobPdnBcArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcArp.setStatus("current")
_TmnxMobPdnBcSdfs_Type = TmnxMobSdf
_TmnxMobPdnBcSdfs_Object = MibTableColumn
tmnxMobPdnBcSdfs = _TmnxMobPdnBcSdfs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 6),
    _TmnxMobPdnBcSdfs_Type()
)
tmnxMobPdnBcSdfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfs.setStatus("current")
_TmnxMobPdnBcFilters_Type = TmnxMobSdfFilterNum
_TmnxMobPdnBcFilters_Object = MibTableColumn
tmnxMobPdnBcFilters = _TmnxMobPdnBcFilters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 7),
    _TmnxMobPdnBcFilters_Type()
)
tmnxMobPdnBcFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcFilters.setStatus("current")
_TmnxMobPdnBcTnlRemoteTeid_Type = Unsigned32
_TmnxMobPdnBcTnlRemoteTeid_Object = MibTableColumn
tmnxMobPdnBcTnlRemoteTeid = _TmnxMobPdnBcTnlRemoteTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 8),
    _TmnxMobPdnBcTnlRemoteTeid_Type()
)
tmnxMobPdnBcTnlRemoteTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlRemoteTeid.setStatus("current")
_TmnxMobPdnBcTnlRemoteDataAddrTyp_Type = InetAddressType
_TmnxMobPdnBcTnlRemoteDataAddrTyp_Object = MibTableColumn
tmnxMobPdnBcTnlRemoteDataAddrTyp = _TmnxMobPdnBcTnlRemoteDataAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 9),
    _TmnxMobPdnBcTnlRemoteDataAddrTyp_Type()
)
tmnxMobPdnBcTnlRemoteDataAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlRemoteDataAddrTyp.setStatus("current")


class _TmnxMobPdnBcTnlRemoteDataAddr_Type(InetAddress):
    """Custom type tmnxMobPdnBcTnlRemoteDataAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnBcTnlRemoteDataAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnBcTnlRemoteDataAddr_Object = MibTableColumn
tmnxMobPdnBcTnlRemoteDataAddr = _TmnxMobPdnBcTnlRemoteDataAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 10),
    _TmnxMobPdnBcTnlRemoteDataAddr_Type()
)
tmnxMobPdnBcTnlRemoteDataAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlRemoteDataAddr.setStatus("current")
_TmnxMobPdnBcTnlLocalTeid_Type = Unsigned32
_TmnxMobPdnBcTnlLocalTeid_Object = MibTableColumn
tmnxMobPdnBcTnlLocalTeid = _TmnxMobPdnBcTnlLocalTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 11),
    _TmnxMobPdnBcTnlLocalTeid_Type()
)
tmnxMobPdnBcTnlLocalTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlLocalTeid.setStatus("current")
_TmnxMobPdnBcTnlLocalDataAddrType_Type = InetAddressType
_TmnxMobPdnBcTnlLocalDataAddrType_Object = MibTableColumn
tmnxMobPdnBcTnlLocalDataAddrType = _TmnxMobPdnBcTnlLocalDataAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 12),
    _TmnxMobPdnBcTnlLocalDataAddrType_Type()
)
tmnxMobPdnBcTnlLocalDataAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlLocalDataAddrType.setStatus("current")


class _TmnxMobPdnBcTnlLocalDataAddr_Type(InetAddress):
    """Custom type tmnxMobPdnBcTnlLocalDataAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnBcTnlLocalDataAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnBcTnlLocalDataAddr_Object = MibTableColumn
tmnxMobPdnBcTnlLocalDataAddr = _TmnxMobPdnBcTnlLocalDataAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 13),
    _TmnxMobPdnBcTnlLocalDataAddr_Type()
)
tmnxMobPdnBcTnlLocalDataAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlLocalDataAddr.setStatus("current")
_TmnxMobPdnBcTnlDLPackets_Type = Counter64
_TmnxMobPdnBcTnlDLPackets_Object = MibTableColumn
tmnxMobPdnBcTnlDLPackets = _TmnxMobPdnBcTnlDLPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 14),
    _TmnxMobPdnBcTnlDLPackets_Type()
)
tmnxMobPdnBcTnlDLPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlDLPackets.setStatus("current")
_TmnxMobPdnBcTnlDLBytes_Type = Counter64
_TmnxMobPdnBcTnlDLBytes_Object = MibTableColumn
tmnxMobPdnBcTnlDLBytes = _TmnxMobPdnBcTnlDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 15),
    _TmnxMobPdnBcTnlDLBytes_Type()
)
tmnxMobPdnBcTnlDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlDLBytes.setStatus("current")
_TmnxMobPdnBcSgiULPackets_Type = Counter64
_TmnxMobPdnBcSgiULPackets_Object = MibTableColumn
tmnxMobPdnBcSgiULPackets = _TmnxMobPdnBcSgiULPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 16),
    _TmnxMobPdnBcSgiULPackets_Type()
)
tmnxMobPdnBcSgiULPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSgiULPackets.setStatus("current")
_TmnxMobPdnBcSgiULBytes_Type = Counter64
_TmnxMobPdnBcSgiULBytes_Object = MibTableColumn
tmnxMobPdnBcSgiULBytes = _TmnxMobPdnBcSgiULBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 17),
    _TmnxMobPdnBcSgiULBytes_Type()
)
tmnxMobPdnBcSgiULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSgiULBytes.setStatus("current")
_TmnxMobPdnBcTnlDLPacketsLow_Type = Counter32
_TmnxMobPdnBcTnlDLPacketsLow_Object = MibTableColumn
tmnxMobPdnBcTnlDLPacketsLow = _TmnxMobPdnBcTnlDLPacketsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 18),
    _TmnxMobPdnBcTnlDLPacketsLow_Type()
)
tmnxMobPdnBcTnlDLPacketsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlDLPacketsLow.setStatus("current")
_TmnxMobPdnBcTnlDLPacketsHigh_Type = Counter32
_TmnxMobPdnBcTnlDLPacketsHigh_Object = MibTableColumn
tmnxMobPdnBcTnlDLPacketsHigh = _TmnxMobPdnBcTnlDLPacketsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 19),
    _TmnxMobPdnBcTnlDLPacketsHigh_Type()
)
tmnxMobPdnBcTnlDLPacketsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlDLPacketsHigh.setStatus("current")
_TmnxMobPdnBcTnlDLBytesLow_Type = Counter32
_TmnxMobPdnBcTnlDLBytesLow_Object = MibTableColumn
tmnxMobPdnBcTnlDLBytesLow = _TmnxMobPdnBcTnlDLBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 20),
    _TmnxMobPdnBcTnlDLBytesLow_Type()
)
tmnxMobPdnBcTnlDLBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlDLBytesLow.setStatus("current")
_TmnxMobPdnBcTnlDLBytesHigh_Type = Counter32
_TmnxMobPdnBcTnlDLBytesHigh_Object = MibTableColumn
tmnxMobPdnBcTnlDLBytesHigh = _TmnxMobPdnBcTnlDLBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 21),
    _TmnxMobPdnBcTnlDLBytesHigh_Type()
)
tmnxMobPdnBcTnlDLBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcTnlDLBytesHigh.setStatus("current")
_TmnxMobPdnBcSgiULPacketsLow_Type = Counter32
_TmnxMobPdnBcSgiULPacketsLow_Object = MibTableColumn
tmnxMobPdnBcSgiULPacketsLow = _TmnxMobPdnBcSgiULPacketsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 22),
    _TmnxMobPdnBcSgiULPacketsLow_Type()
)
tmnxMobPdnBcSgiULPacketsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSgiULPacketsLow.setStatus("current")
_TmnxMobPdnBcSgiULPacketsHigh_Type = Counter32
_TmnxMobPdnBcSgiULPacketsHigh_Object = MibTableColumn
tmnxMobPdnBcSgiULPacketsHigh = _TmnxMobPdnBcSgiULPacketsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 23),
    _TmnxMobPdnBcSgiULPacketsHigh_Type()
)
tmnxMobPdnBcSgiULPacketsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSgiULPacketsHigh.setStatus("current")
_TmnxMobPdnBcSgiULBytesLow_Type = Counter32
_TmnxMobPdnBcSgiULBytesLow_Object = MibTableColumn
tmnxMobPdnBcSgiULBytesLow = _TmnxMobPdnBcSgiULBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 24),
    _TmnxMobPdnBcSgiULBytesLow_Type()
)
tmnxMobPdnBcSgiULBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSgiULBytesLow.setStatus("current")
_TmnxMobPdnBcSgiULBytesHigh_Type = Counter32
_TmnxMobPdnBcSgiULBytesHigh_Object = MibTableColumn
tmnxMobPdnBcSgiULBytesHigh = _TmnxMobPdnBcSgiULBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 25),
    _TmnxMobPdnBcSgiULBytesHigh_Type()
)
tmnxMobPdnBcSgiULBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSgiULBytesHigh.setStatus("current")
_TmnxMobPdnBcOfcServerAddrType_Type = InetAddressType
_TmnxMobPdnBcOfcServerAddrType_Object = MibTableColumn
tmnxMobPdnBcOfcServerAddrType = _TmnxMobPdnBcOfcServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 26),
    _TmnxMobPdnBcOfcServerAddrType_Type()
)
tmnxMobPdnBcOfcServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcOfcServerAddrType.setStatus("current")


class _TmnxMobPdnBcOfcServerAddr_Type(InetAddress):
    """Custom type tmnxMobPdnBcOfcServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnBcOfcServerAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnBcOfcServerAddr_Object = MibTableColumn
tmnxMobPdnBcOfcServerAddr = _TmnxMobPdnBcOfcServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 27),
    _TmnxMobPdnBcOfcServerAddr_Type()
)
tmnxMobPdnBcOfcServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcOfcServerAddr.setStatus("current")
_TmnxMobPdnBcOfcServerState_Type = TmnxMobServerState
_TmnxMobPdnBcOfcServerState_Object = MibTableColumn
tmnxMobPdnBcOfcServerState = _TmnxMobPdnBcOfcServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 28),
    _TmnxMobPdnBcOfcServerState_Type()
)
tmnxMobPdnBcOfcServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcOfcServerState.setStatus("current")
_TmnxMobPdnBcOfcChargingProfile_Type = TmnxMobChargingProfile
_TmnxMobPdnBcOfcChargingProfile_Object = MibTableColumn
tmnxMobPdnBcOfcChargingProfile = _TmnxMobPdnBcOfcChargingProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 29),
    _TmnxMobPdnBcOfcChargingProfile_Type()
)
tmnxMobPdnBcOfcChargingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcOfcChargingProfile.setStatus("current")
_TmnxMobPdnBcOfcTriggeredRecords_Type = Counter32
_TmnxMobPdnBcOfcTriggeredRecords_Object = MibTableColumn
tmnxMobPdnBcOfcTriggeredRecords = _TmnxMobPdnBcOfcTriggeredRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 30),
    _TmnxMobPdnBcOfcTriggeredRecords_Type()
)
tmnxMobPdnBcOfcTriggeredRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcOfcTriggeredRecords.setStatus("current")
_TmnxMobPdnBcOfcInterimRecords_Type = Counter32
_TmnxMobPdnBcOfcInterimRecords_Object = MibTableColumn
tmnxMobPdnBcOfcInterimRecords = _TmnxMobPdnBcOfcInterimRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 31),
    _TmnxMobPdnBcOfcInterimRecords_Type()
)
tmnxMobPdnBcOfcInterimRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcOfcInterimRecords.setStatus("current")
_TmnxMobPdnBcAccessType_Type = TmnxMobAccessType
_TmnxMobPdnBcAccessType_Object = MibTableColumn
tmnxMobPdnBcAccessType = _TmnxMobPdnBcAccessType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 32),
    _TmnxMobPdnBcAccessType_Type()
)
tmnxMobPdnBcAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAccessType.setStatus("current")
_TmnxMobPdnBcPGWGreKey_Type = Unsigned32
_TmnxMobPdnBcPGWGreKey_Object = MibTableColumn
tmnxMobPdnBcPGWGreKey = _TmnxMobPdnBcPGWGreKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 33),
    _TmnxMobPdnBcPGWGreKey_Type()
)
tmnxMobPdnBcPGWGreKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcPGWGreKey.setStatus("current")
_TmnxMobPdnBcMAGGreKey_Type = Unsigned32
_TmnxMobPdnBcMAGGreKey_Object = MibTableColumn
tmnxMobPdnBcMAGGreKey = _TmnxMobPdnBcMAGGreKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 34),
    _TmnxMobPdnBcMAGGreKey_Type()
)
tmnxMobPdnBcMAGGreKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcMAGGreKey.setStatus("current")
_TmnxMobPdnBcRefPointType_Type = TmnxMobPdnRefPointType
_TmnxMobPdnBcRefPointType_Object = MibTableColumn
tmnxMobPdnBcRefPointType = _TmnxMobPdnBcRefPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 35),
    _TmnxMobPdnBcRefPointType_Type()
)
tmnxMobPdnBcRefPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcRefPointType.setStatus("current")
_TmnxMobPdnBcChargingChar_Type = Unsigned32
_TmnxMobPdnBcChargingChar_Object = MibTableColumn
tmnxMobPdnBcChargingChar = _TmnxMobPdnBcChargingChar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 36),
    _TmnxMobPdnBcChargingChar_Type()
)
tmnxMobPdnBcChargingChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcChargingChar.setStatus("current")
_TmnxMobPdnBcQosBytes_Type = TmnxQosBytesHex
_TmnxMobPdnBcQosBytes_Object = MibTableColumn
tmnxMobPdnBcQosBytes = _TmnxMobPdnBcQosBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 3, 1, 37),
    _TmnxMobPdnBcQosBytes_Type()
)
tmnxMobPdnBcQosBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcQosBytes.setStatus("current")
_TmnxMobPdnBcSdfTable_Object = MibTable
tmnxMobPdnBcSdfTable = _TmnxMobPdnBcSdfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfTable.setStatus("current")
_TmnxMobPdnBcSdfEntry_Object = MibTableRow
tmnxMobPdnBcSdfEntry = _TmnxMobPdnBcSdfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1)
)
tmnxMobPdnBcSdfEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsi"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcApn"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPdnType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcBearerId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfPrecedence"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfEntry.setStatus("current")


class _TmnxMobPdnBcSdfPrecedence_Type(Unsigned32):
    """Custom type tmnxMobPdnBcSdfPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxMobPdnBcSdfPrecedence_Type.__name__ = "Unsigned32"
_TmnxMobPdnBcSdfPrecedence_Object = MibTableColumn
tmnxMobPdnBcSdfPrecedence = _TmnxMobPdnBcSdfPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1, 1),
    _TmnxMobPdnBcSdfPrecedence_Type()
)
tmnxMobPdnBcSdfPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfPrecedence.setStatus("current")
_TmnxMobPdnBcSdfPcrfPrecedence_Type = Unsigned32
_TmnxMobPdnBcSdfPcrfPrecedence_Object = MibTableColumn
tmnxMobPdnBcSdfPcrfPrecedence = _TmnxMobPdnBcSdfPcrfPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1, 2),
    _TmnxMobPdnBcSdfPcrfPrecedence_Type()
)
tmnxMobPdnBcSdfPcrfPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfPcrfPrecedence.setStatus("current")
_TmnxMobPdnBcSdfRuleName_Type = TmnxMobSdfRuleName
_TmnxMobPdnBcSdfRuleName_Object = MibTableColumn
tmnxMobPdnBcSdfRuleName = _TmnxMobPdnBcSdfRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1, 3),
    _TmnxMobPdnBcSdfRuleName_Type()
)
tmnxMobPdnBcSdfRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfRuleName.setStatus("current")
_TmnxMobPdnBcSdfPacketFilters_Type = Unsigned32
_TmnxMobPdnBcSdfPacketFilters_Object = MibTableColumn
tmnxMobPdnBcSdfPacketFilters = _TmnxMobPdnBcSdfPacketFilters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1, 4),
    _TmnxMobPdnBcSdfPacketFilters_Type()
)
tmnxMobPdnBcSdfPacketFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfPacketFilters.setStatus("current")
_TmnxMobPdnBcSdfQosUlMbr_Type = Unsigned32
_TmnxMobPdnBcSdfQosUlMbr_Object = MibTableColumn
tmnxMobPdnBcSdfQosUlMbr = _TmnxMobPdnBcSdfQosUlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1, 5),
    _TmnxMobPdnBcSdfQosUlMbr_Type()
)
tmnxMobPdnBcSdfQosUlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfQosUlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfQosUlMbr.setUnits("Kbps")
_TmnxMobPdnBcSdfQosDlMbr_Type = Unsigned32
_TmnxMobPdnBcSdfQosDlMbr_Object = MibTableColumn
tmnxMobPdnBcSdfQosDlMbr = _TmnxMobPdnBcSdfQosDlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1, 6),
    _TmnxMobPdnBcSdfQosDlMbr_Type()
)
tmnxMobPdnBcSdfQosDlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfQosDlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfQosDlMbr.setUnits("Kbps")
_TmnxMobPdnBcSdfQosUlGbr_Type = Unsigned32
_TmnxMobPdnBcSdfQosUlGbr_Object = MibTableColumn
tmnxMobPdnBcSdfQosUlGbr = _TmnxMobPdnBcSdfQosUlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1, 7),
    _TmnxMobPdnBcSdfQosUlGbr_Type()
)
tmnxMobPdnBcSdfQosUlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfQosUlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfQosUlGbr.setUnits("Kbps")
_TmnxMobPdnBcSdfQosDlGbr_Type = Unsigned32
_TmnxMobPdnBcSdfQosDlGbr_Object = MibTableColumn
tmnxMobPdnBcSdfQosDlGbr = _TmnxMobPdnBcSdfQosDlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 4, 1, 8),
    _TmnxMobPdnBcSdfQosDlGbr_Type()
)
tmnxMobPdnBcSdfQosDlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfQosDlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfQosDlGbr.setUnits("Kbps")
_TmnxMobPdnBcSdfFilterTable_Object = MibTable
tmnxMobPdnBcSdfFilterTable = _TmnxMobPdnBcSdfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterTable.setStatus("current")
_TmnxMobPdnBcSdfFilterEntry_Object = MibTableRow
tmnxMobPdnBcSdfFilterEntry = _TmnxMobPdnBcSdfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1)
)
tmnxMobPdnBcSdfFilterEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsi"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcApn"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPdnType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcBearerId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfPrecedence"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterDirection"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterId"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterEntry.setStatus("current")
_TmnxMobPdnBcSdfFilterDirection_Type = TmnxMobSdfFilterDirection
_TmnxMobPdnBcSdfFilterDirection_Object = MibTableColumn
tmnxMobPdnBcSdfFilterDirection = _TmnxMobPdnBcSdfFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 1),
    _TmnxMobPdnBcSdfFilterDirection_Type()
)
tmnxMobPdnBcSdfFilterDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterDirection.setStatus("current")
_TmnxMobPdnBcSdfFilterId_Type = TmnxMobSdfFilter
_TmnxMobPdnBcSdfFilterId_Object = MibTableColumn
tmnxMobPdnBcSdfFilterId = _TmnxMobPdnBcSdfFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 2),
    _TmnxMobPdnBcSdfFilterId_Type()
)
tmnxMobPdnBcSdfFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterId.setStatus("current")
_TmnxMobPdnBcSdfFilterProtocol_Type = TmnxMobSdfFilterProtocol
_TmnxMobPdnBcSdfFilterProtocol_Object = MibTableColumn
tmnxMobPdnBcSdfFilterProtocol = _TmnxMobPdnBcSdfFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 3),
    _TmnxMobPdnBcSdfFilterProtocol_Type()
)
tmnxMobPdnBcSdfFilterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterProtocol.setStatus("current")
_TmnxMobPdnBcSdfFilterSrcAdrType_Type = InetAddressType
_TmnxMobPdnBcSdfFilterSrcAdrType_Object = MibTableColumn
tmnxMobPdnBcSdfFilterSrcAdrType = _TmnxMobPdnBcSdfFilterSrcAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 4),
    _TmnxMobPdnBcSdfFilterSrcAdrType_Type()
)
tmnxMobPdnBcSdfFilterSrcAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterSrcAdrType.setStatus("current")


class _TmnxMobPdnBcSdfFilterSrcAddr_Type(InetAddress):
    """Custom type tmnxMobPdnBcSdfFilterSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnBcSdfFilterSrcAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnBcSdfFilterSrcAddr_Object = MibTableColumn
tmnxMobPdnBcSdfFilterSrcAddr = _TmnxMobPdnBcSdfFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 5),
    _TmnxMobPdnBcSdfFilterSrcAddr_Type()
)
tmnxMobPdnBcSdfFilterSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterSrcAddr.setStatus("current")
_TmnxMobPdnBcSdfFilterSrcPfxLen_Type = InetAddressPrefixLength
_TmnxMobPdnBcSdfFilterSrcPfxLen_Object = MibTableColumn
tmnxMobPdnBcSdfFilterSrcPfxLen = _TmnxMobPdnBcSdfFilterSrcPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 6),
    _TmnxMobPdnBcSdfFilterSrcPfxLen_Type()
)
tmnxMobPdnBcSdfFilterSrcPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterSrcPfxLen.setStatus("current")
_TmnxMobPdnBcSdfFilterDstAdrType_Type = InetAddressType
_TmnxMobPdnBcSdfFilterDstAdrType_Object = MibTableColumn
tmnxMobPdnBcSdfFilterDstAdrType = _TmnxMobPdnBcSdfFilterDstAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 7),
    _TmnxMobPdnBcSdfFilterDstAdrType_Type()
)
tmnxMobPdnBcSdfFilterDstAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterDstAdrType.setStatus("current")


class _TmnxMobPdnBcSdfFilterDestAddr_Type(InetAddress):
    """Custom type tmnxMobPdnBcSdfFilterDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnBcSdfFilterDestAddr_Type.__name__ = "InetAddress"
_TmnxMobPdnBcSdfFilterDestAddr_Object = MibTableColumn
tmnxMobPdnBcSdfFilterDestAddr = _TmnxMobPdnBcSdfFilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 8),
    _TmnxMobPdnBcSdfFilterDestAddr_Type()
)
tmnxMobPdnBcSdfFilterDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterDestAddr.setStatus("current")
_TmnxMobPdnBcSdfFilterDestPfxLen_Type = InetAddressPrefixLength
_TmnxMobPdnBcSdfFilterDestPfxLen_Object = MibTableColumn
tmnxMobPdnBcSdfFilterDestPfxLen = _TmnxMobPdnBcSdfFilterDestPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 9),
    _TmnxMobPdnBcSdfFilterDestPfxLen_Type()
)
tmnxMobPdnBcSdfFilterDestPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterDestPfxLen.setStatus("current")
_TmnxMobPdnBcSdfFilterSrcPorts_Type = Unsigned32
_TmnxMobPdnBcSdfFilterSrcPorts_Object = MibTableColumn
tmnxMobPdnBcSdfFilterSrcPorts = _TmnxMobPdnBcSdfFilterSrcPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 10),
    _TmnxMobPdnBcSdfFilterSrcPorts_Type()
)
tmnxMobPdnBcSdfFilterSrcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterSrcPorts.setStatus("current")
_TmnxMobPdnBcSdfFilterDestPorts_Type = Unsigned32
_TmnxMobPdnBcSdfFilterDestPorts_Object = MibTableColumn
tmnxMobPdnBcSdfFilterDestPorts = _TmnxMobPdnBcSdfFilterDestPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 11),
    _TmnxMobPdnBcSdfFilterDestPorts_Type()
)
tmnxMobPdnBcSdfFilterDestPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFilterDestPorts.setStatus("current")
_TmnxMobPdnBcSdfFirstSrcPortOper_Type = TTcpUdpPortOperator
_TmnxMobPdnBcSdfFirstSrcPortOper_Object = MibTableColumn
tmnxMobPdnBcSdfFirstSrcPortOper = _TmnxMobPdnBcSdfFirstSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 12),
    _TmnxMobPdnBcSdfFirstSrcPortOper_Type()
)
tmnxMobPdnBcSdfFirstSrcPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFirstSrcPortOper.setStatus("current")
_TmnxMobPdnBcSdfFirstSrcPortVal1_Type = TTcpUdpPort
_TmnxMobPdnBcSdfFirstSrcPortVal1_Object = MibTableColumn
tmnxMobPdnBcSdfFirstSrcPortVal1 = _TmnxMobPdnBcSdfFirstSrcPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 13),
    _TmnxMobPdnBcSdfFirstSrcPortVal1_Type()
)
tmnxMobPdnBcSdfFirstSrcPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFirstSrcPortVal1.setStatus("current")
_TmnxMobPdnBcSdfFirstSrcPortVal2_Type = TTcpUdpPort
_TmnxMobPdnBcSdfFirstSrcPortVal2_Object = MibTableColumn
tmnxMobPdnBcSdfFirstSrcPortVal2 = _TmnxMobPdnBcSdfFirstSrcPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 14),
    _TmnxMobPdnBcSdfFirstSrcPortVal2_Type()
)
tmnxMobPdnBcSdfFirstSrcPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFirstSrcPortVal2.setStatus("current")
_TmnxMobPdnBcSdfSecndSrcPortOper_Type = TTcpUdpPortOperator
_TmnxMobPdnBcSdfSecndSrcPortOper_Object = MibTableColumn
tmnxMobPdnBcSdfSecndSrcPortOper = _TmnxMobPdnBcSdfSecndSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 15),
    _TmnxMobPdnBcSdfSecndSrcPortOper_Type()
)
tmnxMobPdnBcSdfSecndSrcPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfSecndSrcPortOper.setStatus("current")
_TmnxMobPdnBcSdfSecndSrcPortVal1_Type = TTcpUdpPort
_TmnxMobPdnBcSdfSecndSrcPortVal1_Object = MibTableColumn
tmnxMobPdnBcSdfSecndSrcPortVal1 = _TmnxMobPdnBcSdfSecndSrcPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 16),
    _TmnxMobPdnBcSdfSecndSrcPortVal1_Type()
)
tmnxMobPdnBcSdfSecndSrcPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfSecndSrcPortVal1.setStatus("current")
_TmnxMobPdnBcSdfSecndSrcPortVal2_Type = TTcpUdpPort
_TmnxMobPdnBcSdfSecndSrcPortVal2_Object = MibTableColumn
tmnxMobPdnBcSdfSecndSrcPortVal2 = _TmnxMobPdnBcSdfSecndSrcPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 17),
    _TmnxMobPdnBcSdfSecndSrcPortVal2_Type()
)
tmnxMobPdnBcSdfSecndSrcPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfSecndSrcPortVal2.setStatus("current")
_TmnxMobPdnBcSdfFirstDstPortOper_Type = TTcpUdpPortOperator
_TmnxMobPdnBcSdfFirstDstPortOper_Object = MibTableColumn
tmnxMobPdnBcSdfFirstDstPortOper = _TmnxMobPdnBcSdfFirstDstPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 18),
    _TmnxMobPdnBcSdfFirstDstPortOper_Type()
)
tmnxMobPdnBcSdfFirstDstPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFirstDstPortOper.setStatus("current")
_TmnxMobPdnBcSdfFirstDstPortVal1_Type = TTcpUdpPort
_TmnxMobPdnBcSdfFirstDstPortVal1_Object = MibTableColumn
tmnxMobPdnBcSdfFirstDstPortVal1 = _TmnxMobPdnBcSdfFirstDstPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 19),
    _TmnxMobPdnBcSdfFirstDstPortVal1_Type()
)
tmnxMobPdnBcSdfFirstDstPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFirstDstPortVal1.setStatus("current")
_TmnxMobPdnBcSdfFirstDstPortVal2_Type = TTcpUdpPort
_TmnxMobPdnBcSdfFirstDstPortVal2_Object = MibTableColumn
tmnxMobPdnBcSdfFirstDstPortVal2 = _TmnxMobPdnBcSdfFirstDstPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 20),
    _TmnxMobPdnBcSdfFirstDstPortVal2_Type()
)
tmnxMobPdnBcSdfFirstDstPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfFirstDstPortVal2.setStatus("current")
_TmnxMobPdnBcSdfSecndDstPortOper_Type = TTcpUdpPortOperator
_TmnxMobPdnBcSdfSecndDstPortOper_Object = MibTableColumn
tmnxMobPdnBcSdfSecndDstPortOper = _TmnxMobPdnBcSdfSecndDstPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 21),
    _TmnxMobPdnBcSdfSecndDstPortOper_Type()
)
tmnxMobPdnBcSdfSecndDstPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfSecndDstPortOper.setStatus("current")
_TmnxMobPdnBcSdfSecndDstPortVal1_Type = TTcpUdpPort
_TmnxMobPdnBcSdfSecndDstPortVal1_Object = MibTableColumn
tmnxMobPdnBcSdfSecndDstPortVal1 = _TmnxMobPdnBcSdfSecndDstPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 22),
    _TmnxMobPdnBcSdfSecndDstPortVal1_Type()
)
tmnxMobPdnBcSdfSecndDstPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfSecndDstPortVal1.setStatus("current")
_TmnxMobPdnBcSdfSecndDstPortVal2_Type = TTcpUdpPort
_TmnxMobPdnBcSdfSecndDstPortVal2_Object = MibTableColumn
tmnxMobPdnBcSdfSecndDstPortVal2 = _TmnxMobPdnBcSdfSecndDstPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 5, 1, 23),
    _TmnxMobPdnBcSdfSecndDstPortVal2_Type()
)
tmnxMobPdnBcSdfSecndDstPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcSdfSecndDstPortVal2.setStatus("current")
_TmnxMobPdnStatTable_Object = MibTable
tmnxMobPdnStatTable = _TmnxMobPdnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxMobPdnStatTable.setStatus("current")
_TmnxMobPdnStatEntry_Object = MibTableRow
tmnxMobPdnStatEntry = _TmnxMobPdnStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1)
)
tmnxMobPdnStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnStatEntry.setStatus("current")
_TmnxMobPdnCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxMobPdnCardSlotNum_Object = MibTableColumn
tmnxMobPdnCardSlotNum = _TmnxMobPdnCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 1),
    _TmnxMobPdnCardSlotNum_Type()
)
tmnxMobPdnCardSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnCardSlotNum.setStatus("current")
_TmnxMobPdnStatRealApn_Type = Gauge32
_TmnxMobPdnStatRealApn_Object = MibTableColumn
tmnxMobPdnStatRealApn = _TmnxMobPdnStatRealApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 2),
    _TmnxMobPdnStatRealApn_Type()
)
tmnxMobPdnStatRealApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatRealApn.setStatus("current")
_TmnxMobPdnStatVirtualApn_Type = Gauge32
_TmnxMobPdnStatVirtualApn_Object = MibTableColumn
tmnxMobPdnStatVirtualApn = _TmnxMobPdnStatVirtualApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 3),
    _TmnxMobPdnStatVirtualApn_Type()
)
tmnxMobPdnStatVirtualApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatVirtualApn.setStatus("current")
_TmnxMobPdnStatBearers_Type = Gauge32
_TmnxMobPdnStatBearers_Object = MibTableColumn
tmnxMobPdnStatBearers = _TmnxMobPdnStatBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 4),
    _TmnxMobPdnStatBearers_Type()
)
tmnxMobPdnStatBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatBearers.setStatus("current")
_TmnxMobPdnStatDefaultBearers_Type = Gauge32
_TmnxMobPdnStatDefaultBearers_Object = MibTableColumn
tmnxMobPdnStatDefaultBearers = _TmnxMobPdnStatDefaultBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 5),
    _TmnxMobPdnStatDefaultBearers_Type()
)
tmnxMobPdnStatDefaultBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatDefaultBearers.setStatus("current")
_TmnxMobPdnStatDedicatedBearers_Type = Gauge32
_TmnxMobPdnStatDedicatedBearers_Object = MibTableColumn
tmnxMobPdnStatDedicatedBearers = _TmnxMobPdnStatDedicatedBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 6),
    _TmnxMobPdnStatDedicatedBearers_Type()
)
tmnxMobPdnStatDedicatedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatDedicatedBearers.setStatus("current")
_TmnxMobPdnStatIpv4Bearers_Type = Gauge32
_TmnxMobPdnStatIpv4Bearers_Object = MibTableColumn
tmnxMobPdnStatIpv4Bearers = _TmnxMobPdnStatIpv4Bearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 7),
    _TmnxMobPdnStatIpv4Bearers_Type()
)
tmnxMobPdnStatIpv4Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpv4Bearers.setStatus("current")
_TmnxMobPdnStatIpv6Bearers_Type = Gauge32
_TmnxMobPdnStatIpv6Bearers_Object = MibTableColumn
tmnxMobPdnStatIpv6Bearers = _TmnxMobPdnStatIpv6Bearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 8),
    _TmnxMobPdnStatIpv6Bearers_Type()
)
tmnxMobPdnStatIpv6Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpv6Bearers.setStatus("current")
_TmnxMobPdnStatIpv4v6Bearers_Type = Gauge32
_TmnxMobPdnStatIpv4v6Bearers_Object = MibTableColumn
tmnxMobPdnStatIpv4v6Bearers = _TmnxMobPdnStatIpv4v6Bearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 9),
    _TmnxMobPdnStatIpv4v6Bearers_Type()
)
tmnxMobPdnStatIpv4v6Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpv4v6Bearers.setStatus("current")
_TmnxMobPdnStatRoamers_Type = Gauge32
_TmnxMobPdnStatRoamers_Object = MibTableColumn
tmnxMobPdnStatRoamers = _TmnxMobPdnStatRoamers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 10),
    _TmnxMobPdnStatRoamers_Type()
)
tmnxMobPdnStatRoamers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatRoamers.setStatus("current")
_TmnxMobPdnStatIpv4Sdf_Type = Gauge32
_TmnxMobPdnStatIpv4Sdf_Object = MibTableColumn
tmnxMobPdnStatIpv4Sdf = _TmnxMobPdnStatIpv4Sdf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 11),
    _TmnxMobPdnStatIpv4Sdf_Type()
)
tmnxMobPdnStatIpv4Sdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpv4Sdf.setStatus("current")
_TmnxMobPdnStatIpv6Sdf_Type = Gauge32
_TmnxMobPdnStatIpv6Sdf_Object = MibTableColumn
tmnxMobPdnStatIpv6Sdf = _TmnxMobPdnStatIpv6Sdf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 12),
    _TmnxMobPdnStatIpv6Sdf_Type()
)
tmnxMobPdnStatIpv6Sdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpv6Sdf.setStatus("current")
_TmnxMobPdnStatVPRNs_Type = Gauge32
_TmnxMobPdnStatVPRNs_Object = MibTableColumn
tmnxMobPdnStatVPRNs = _TmnxMobPdnStatVPRNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 13),
    _TmnxMobPdnStatVPRNs_Type()
)
tmnxMobPdnStatVPRNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatVPRNs.setStatus("current")
_TmnxMobPdnStatPdnSessions_Type = Gauge32
_TmnxMobPdnStatPdnSessions_Object = MibTableColumn
tmnxMobPdnStatPdnSessions = _TmnxMobPdnStatPdnSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 14),
    _TmnxMobPdnStatPdnSessions_Type()
)
tmnxMobPdnStatPdnSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatPdnSessions.setStatus("current")
_TmnxMobPdnStatIpv4PdnSessions_Type = Gauge32
_TmnxMobPdnStatIpv4PdnSessions_Object = MibTableColumn
tmnxMobPdnStatIpv4PdnSessions = _TmnxMobPdnStatIpv4PdnSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 15),
    _TmnxMobPdnStatIpv4PdnSessions_Type()
)
tmnxMobPdnStatIpv4PdnSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpv4PdnSessions.setStatus("current")
_TmnxMobPdnStatIpv6PdnSessions_Type = Gauge32
_TmnxMobPdnStatIpv6PdnSessions_Object = MibTableColumn
tmnxMobPdnStatIpv6PdnSessions = _TmnxMobPdnStatIpv6PdnSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 16),
    _TmnxMobPdnStatIpv6PdnSessions_Type()
)
tmnxMobPdnStatIpv6PdnSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpv6PdnSessions.setStatus("current")
_TmnxMobPdnStatIpv4v6PdnSessions_Type = Gauge32
_TmnxMobPdnStatIpv4v6PdnSessions_Object = MibTableColumn
tmnxMobPdnStatIpv4v6PdnSessions = _TmnxMobPdnStatIpv4v6PdnSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 17),
    _TmnxMobPdnStatIpv4v6PdnSessions_Type()
)
tmnxMobPdnStatIpv4v6PdnSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpv4v6PdnSessions.setStatus("current")
_TmnxMobPdnStatIpLocalPools_Type = Gauge32
_TmnxMobPdnStatIpLocalPools_Object = MibTableColumn
tmnxMobPdnStatIpLocalPools = _TmnxMobPdnStatIpLocalPools_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 18),
    _TmnxMobPdnStatIpLocalPools_Type()
)
tmnxMobPdnStatIpLocalPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatIpLocalPools.setStatus("current")
_TmnxMobPdnStatGnSgsns_Type = Gauge32
_TmnxMobPdnStatGnSgsns_Object = MibTableColumn
tmnxMobPdnStatGnSgsns = _TmnxMobPdnStatGnSgsns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 19),
    _TmnxMobPdnStatGnSgsns_Type()
)
tmnxMobPdnStatGnSgsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatGnSgsns.setStatus("current")
_TmnxMobPdnStatHomers_Type = Gauge32
_TmnxMobPdnStatHomers_Object = MibTableColumn
tmnxMobPdnStatHomers = _TmnxMobPdnStatHomers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 20),
    _TmnxMobPdnStatHomers_Type()
)
tmnxMobPdnStatHomers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatHomers.setStatus("current")
_TmnxMobPdnStatVisitors_Type = Gauge32
_TmnxMobPdnStatVisitors_Object = MibTableColumn
tmnxMobPdnStatVisitors = _TmnxMobPdnStatVisitors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 21),
    _TmnxMobPdnStatVisitors_Type()
)
tmnxMobPdnStatVisitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatVisitors.setStatus("current")
_TmnxMobPdnStatHSSStaticIpv4Sess_Type = Gauge32
_TmnxMobPdnStatHSSStaticIpv4Sess_Object = MibTableColumn
tmnxMobPdnStatHSSStaticIpv4Sess = _TmnxMobPdnStatHSSStaticIpv4Sess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 22),
    _TmnxMobPdnStatHSSStaticIpv4Sess_Type()
)
tmnxMobPdnStatHSSStaticIpv4Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatHSSStaticIpv4Sess.setStatus("current")
_TmnxMobPdnStatHSSStaticIpv6Sess_Type = Gauge32
_TmnxMobPdnStatHSSStaticIpv6Sess_Object = MibTableColumn
tmnxMobPdnStatHSSStaticIpv6Sess = _TmnxMobPdnStatHSSStaticIpv6Sess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 23),
    _TmnxMobPdnStatHSSStaticIpv6Sess_Type()
)
tmnxMobPdnStatHSSStaticIpv6Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatHSSStaticIpv6Sess.setStatus("current")
_TmnxMobPdnStatHSSSttIpv4v6Sess_Type = Gauge32
_TmnxMobPdnStatHSSSttIpv4v6Sess_Object = MibTableColumn
tmnxMobPdnStatHSSSttIpv4v6Sess = _TmnxMobPdnStatHSSSttIpv4v6Sess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 24),
    _TmnxMobPdnStatHSSSttIpv4v6Sess_Type()
)
tmnxMobPdnStatHSSSttIpv4v6Sess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatHSSSttIpv4v6Sess.setStatus("current")
_TmnxMobPdnStateHRPDPDNSess_Type = Gauge32
_TmnxMobPdnStateHRPDPDNSess_Object = MibTableColumn
tmnxMobPdnStateHRPDPDNSess = _TmnxMobPdnStateHRPDPDNSess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 25),
    _TmnxMobPdnStateHRPDPDNSess_Type()
)
tmnxMobPdnStateHRPDPDNSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStateHRPDPDNSess.setStatus("current")
_TmnxMobPdnStatLTEPDNSess_Type = Gauge32
_TmnxMobPdnStatLTEPDNSess_Object = MibTableColumn
tmnxMobPdnStatLTEPDNSess = _TmnxMobPdnStatLTEPDNSess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 26),
    _TmnxMobPdnStatLTEPDNSess_Type()
)
tmnxMobPdnStatLTEPDNSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatLTEPDNSess.setStatus("current")
_TmnxMobPdnStat2G3GPDNSess_Type = Gauge32
_TmnxMobPdnStat2G3GPDNSess_Object = MibTableColumn
tmnxMobPdnStat2G3GPDNSess = _TmnxMobPdnStat2G3GPDNSess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 27),
    _TmnxMobPdnStat2G3GPDNSess_Type()
)
tmnxMobPdnStat2G3GPDNSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStat2G3GPDNSess.setStatus("current")
_TmnxMobPdnStatNumSuspendedPDN_Type = Gauge32
_TmnxMobPdnStatNumSuspendedPDN_Object = MibTableColumn
tmnxMobPdnStatNumSuspendedPDN = _TmnxMobPdnStatNumSuspendedPDN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 28),
    _TmnxMobPdnStatNumSuspendedPDN_Type()
)
tmnxMobPdnStatNumSuspendedPDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatNumSuspendedPDN.setStatus("current")
_TmnxMobPdnStatEmergencyPdnSess_Type = Gauge32
_TmnxMobPdnStatEmergencyPdnSess_Object = MibTableColumn
tmnxMobPdnStatEmergencyPdnSess = _TmnxMobPdnStatEmergencyPdnSess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 29),
    _TmnxMobPdnStatEmergencyPdnSess_Type()
)
tmnxMobPdnStatEmergencyPdnSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatEmergencyPdnSess.setStatus("current")
_TmnxMobPdnStatRfPeer_Type = Gauge32
_TmnxMobPdnStatRfPeer_Object = MibTableColumn
tmnxMobPdnStatRfPeer = _TmnxMobPdnStatRfPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 30),
    _TmnxMobPdnStatRfPeer_Type()
)
tmnxMobPdnStatRfPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatRfPeer.setStatus("current")
_TmnxMobPdnStatRfAcctStartBuf_Type = Gauge32
_TmnxMobPdnStatRfAcctStartBuf_Object = MibTableColumn
tmnxMobPdnStatRfAcctStartBuf = _TmnxMobPdnStatRfAcctStartBuf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 31),
    _TmnxMobPdnStatRfAcctStartBuf_Type()
)
tmnxMobPdnStatRfAcctStartBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatRfAcctStartBuf.setStatus("current")
_TmnxMobPdnStatRfAcctIntBuf_Type = Gauge32
_TmnxMobPdnStatRfAcctIntBuf_Object = MibTableColumn
tmnxMobPdnStatRfAcctIntBuf = _TmnxMobPdnStatRfAcctIntBuf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 32),
    _TmnxMobPdnStatRfAcctIntBuf_Type()
)
tmnxMobPdnStatRfAcctIntBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatRfAcctIntBuf.setStatus("current")
_TmnxMobPdnStatRfAcctStopBuf_Type = Gauge32
_TmnxMobPdnStatRfAcctStopBuf_Object = MibTableColumn
tmnxMobPdnStatRfAcctStopBuf = _TmnxMobPdnStatRfAcctStopBuf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 6, 1, 33),
    _TmnxMobPdnStatRfAcctStopBuf_Type()
)
tmnxMobPdnStatRfAcctStopBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnStatRfAcctStopBuf.setStatus("current")
_TmnxMobPdnProcTable_Object = MibTable
tmnxMobPdnProcTable = _TmnxMobPdnProcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxMobPdnProcTable.setStatus("current")
_TmnxMobPdnProcEntry_Object = MibTableRow
tmnxMobPdnProcEntry = _TmnxMobPdnProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnProcEntry.setStatus("current")
_TmnxMobPdnProcAttach_Type = Counter32
_TmnxMobPdnProcAttach_Object = MibTableColumn
tmnxMobPdnProcAttach = _TmnxMobPdnProcAttach_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 1),
    _TmnxMobPdnProcAttach_Type()
)
tmnxMobPdnProcAttach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcAttach.setStatus("current")
_TmnxMobPdnProcAttachFail_Type = Counter32
_TmnxMobPdnProcAttachFail_Object = MibTableColumn
tmnxMobPdnProcAttachFail = _TmnxMobPdnProcAttachFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 2),
    _TmnxMobPdnProcAttachFail_Type()
)
tmnxMobPdnProcAttachFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcAttachFail.setStatus("current")
_TmnxMobPdnProcDetach_Type = Counter32
_TmnxMobPdnProcDetach_Object = MibTableColumn
tmnxMobPdnProcDetach = _TmnxMobPdnProcDetach_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 3),
    _TmnxMobPdnProcDetach_Type()
)
tmnxMobPdnProcDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcDetach.setStatus("current")
_TmnxMobPdnProcDetachFail_Type = Counter32
_TmnxMobPdnProcDetachFail_Object = MibTableColumn
tmnxMobPdnProcDetachFail = _TmnxMobPdnProcDetachFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 4),
    _TmnxMobPdnProcDetachFail_Type()
)
tmnxMobPdnProcDetachFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcDetachFail.setStatus("current")
_TmnxMobPdnProcNwDedBrActv_Type = Counter32
_TmnxMobPdnProcNwDedBrActv_Object = MibTableColumn
tmnxMobPdnProcNwDedBrActv = _TmnxMobPdnProcNwDedBrActv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 5),
    _TmnxMobPdnProcNwDedBrActv_Type()
)
tmnxMobPdnProcNwDedBrActv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcNwDedBrActv.setStatus("current")
_TmnxMobPdnProcNwDedBrActvFail_Type = Counter32
_TmnxMobPdnProcNwDedBrActvFail_Object = MibTableColumn
tmnxMobPdnProcNwDedBrActvFail = _TmnxMobPdnProcNwDedBrActvFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 6),
    _TmnxMobPdnProcNwDedBrActvFail_Type()
)
tmnxMobPdnProcNwDedBrActvFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcNwDedBrActvFail.setStatus("current")
_TmnxMobPdnProcNwDedBrDeActv_Type = Counter32
_TmnxMobPdnProcNwDedBrDeActv_Object = MibTableColumn
tmnxMobPdnProcNwDedBrDeActv = _TmnxMobPdnProcNwDedBrDeActv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 7),
    _TmnxMobPdnProcNwDedBrDeActv_Type()
)
tmnxMobPdnProcNwDedBrDeActv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcNwDedBrDeActv.setStatus("current")
_TmnxMobPdnProcNwDedBrDeActvFail_Type = Counter32
_TmnxMobPdnProcNwDedBrDeActvFail_Object = MibTableColumn
tmnxMobPdnProcNwDedBrDeActvFail = _TmnxMobPdnProcNwDedBrDeActvFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 8),
    _TmnxMobPdnProcNwDedBrDeActvFail_Type()
)
tmnxMobPdnProcNwDedBrDeActvFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcNwDedBrDeActvFail.setStatus("current")
_TmnxMobPdnProcNwDedBrModify_Type = Counter32
_TmnxMobPdnProcNwDedBrModify_Object = MibTableColumn
tmnxMobPdnProcNwDedBrModify = _TmnxMobPdnProcNwDedBrModify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 9),
    _TmnxMobPdnProcNwDedBrModify_Type()
)
tmnxMobPdnProcNwDedBrModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcNwDedBrModify.setStatus("current")
_TmnxMobPdnProcNwDedBrModifyFail_Type = Counter32
_TmnxMobPdnProcNwDedBrModifyFail_Object = MibTableColumn
tmnxMobPdnProcNwDedBrModifyFail = _TmnxMobPdnProcNwDedBrModifyFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 10),
    _TmnxMobPdnProcNwDedBrModifyFail_Type()
)
tmnxMobPdnProcNwDedBrModifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcNwDedBrModifyFail.setStatus("current")
_TmnxMobPdnProcUeDedBrActv_Type = Counter32
_TmnxMobPdnProcUeDedBrActv_Object = MibTableColumn
tmnxMobPdnProcUeDedBrActv = _TmnxMobPdnProcUeDedBrActv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 11),
    _TmnxMobPdnProcUeDedBrActv_Type()
)
tmnxMobPdnProcUeDedBrActv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcUeDedBrActv.setStatus("current")
_TmnxMobPdnProcUeDedBrActvFail_Type = Counter32
_TmnxMobPdnProcUeDedBrActvFail_Object = MibTableColumn
tmnxMobPdnProcUeDedBrActvFail = _TmnxMobPdnProcUeDedBrActvFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 12),
    _TmnxMobPdnProcUeDedBrActvFail_Type()
)
tmnxMobPdnProcUeDedBrActvFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcUeDedBrActvFail.setStatus("current")
_TmnxMobPdnProcUeDedBrDeActv_Type = Counter32
_TmnxMobPdnProcUeDedBrDeActv_Object = MibTableColumn
tmnxMobPdnProcUeDedBrDeActv = _TmnxMobPdnProcUeDedBrDeActv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 13),
    _TmnxMobPdnProcUeDedBrDeActv_Type()
)
tmnxMobPdnProcUeDedBrDeActv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcUeDedBrDeActv.setStatus("current")
_TmnxMobPdnProcUeDedBrDeActvFail_Type = Counter32
_TmnxMobPdnProcUeDedBrDeActvFail_Object = MibTableColumn
tmnxMobPdnProcUeDedBrDeActvFail = _TmnxMobPdnProcUeDedBrDeActvFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 14),
    _TmnxMobPdnProcUeDedBrDeActvFail_Type()
)
tmnxMobPdnProcUeDedBrDeActvFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcUeDedBrDeActvFail.setStatus("current")
_TmnxMobPdnProcUeDedBrModify_Type = Counter32
_TmnxMobPdnProcUeDedBrModify_Object = MibTableColumn
tmnxMobPdnProcUeDedBrModify = _TmnxMobPdnProcUeDedBrModify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 15),
    _TmnxMobPdnProcUeDedBrModify_Type()
)
tmnxMobPdnProcUeDedBrModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcUeDedBrModify.setStatus("current")
_TmnxMobPdnProcUeDedBrModifyFail_Type = Counter32
_TmnxMobPdnProcUeDedBrModifyFail_Object = MibTableColumn
tmnxMobPdnProcUeDedBrModifyFail = _TmnxMobPdnProcUeDedBrModifyFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 16),
    _TmnxMobPdnProcUeDedBrModifyFail_Type()
)
tmnxMobPdnProcUeDedBrModifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcUeDedBrModifyFail.setStatus("current")
_TmnxMobPdnProcHssQosModify_Type = Counter32
_TmnxMobPdnProcHssQosModify_Object = MibTableColumn
tmnxMobPdnProcHssQosModify = _TmnxMobPdnProcHssQosModify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 17),
    _TmnxMobPdnProcHssQosModify_Type()
)
tmnxMobPdnProcHssQosModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcHssQosModify.setStatus("current")
_TmnxMobPdnProcHssQosModifyFail_Type = Counter32
_TmnxMobPdnProcHssQosModifyFail_Object = MibTableColumn
tmnxMobPdnProcHssQosModifyFail = _TmnxMobPdnProcHssQosModifyFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 18),
    _TmnxMobPdnProcHssQosModifyFail_Type()
)
tmnxMobPdnProcHssQosModifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcHssQosModifyFail.setStatus("current")
_TmnxMobPdnProcPcrfQosModify_Type = Counter32
_TmnxMobPdnProcPcrfQosModify_Object = MibTableColumn
tmnxMobPdnProcPcrfQosModify = _TmnxMobPdnProcPcrfQosModify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 19),
    _TmnxMobPdnProcPcrfQosModify_Type()
)
tmnxMobPdnProcPcrfQosModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcPcrfQosModify.setStatus("current")
_TmnxMobPdnProcPcrfQosModifyFail_Type = Counter32
_TmnxMobPdnProcPcrfQosModifyFail_Object = MibTableColumn
tmnxMobPdnProcPcrfQosModifyFail = _TmnxMobPdnProcPcrfQosModifyFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 20),
    _TmnxMobPdnProcPcrfQosModifyFail_Type()
)
tmnxMobPdnProcPcrfQosModifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcPcrfQosModifyFail.setStatus("current")
_TmnxMobPdnProcSgwReloc_Type = Counter32
_TmnxMobPdnProcSgwReloc_Object = MibTableColumn
tmnxMobPdnProcSgwReloc = _TmnxMobPdnProcSgwReloc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 21),
    _TmnxMobPdnProcSgwReloc_Type()
)
tmnxMobPdnProcSgwReloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcSgwReloc.setStatus("current")
_TmnxMobPdnProcSgwRelocFail_Type = Counter32
_TmnxMobPdnProcSgwRelocFail_Object = MibTableColumn
tmnxMobPdnProcSgwRelocFail = _TmnxMobPdnProcSgwRelocFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 22),
    _TmnxMobPdnProcSgwRelocFail_Type()
)
tmnxMobPdnProcSgwRelocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcSgwRelocFail.setStatus("current")
_TmnxMobPdnProcPgwPdnSessDel_Type = Counter32
_TmnxMobPdnProcPgwPdnSessDel_Object = MibTableColumn
tmnxMobPdnProcPgwPdnSessDel = _TmnxMobPdnProcPgwPdnSessDel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 23),
    _TmnxMobPdnProcPgwPdnSessDel_Type()
)
tmnxMobPdnProcPgwPdnSessDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcPgwPdnSessDel.setStatus("current")
_TmnxMobPdnProcPgwPdnSessDelFail_Type = Counter32
_TmnxMobPdnProcPgwPdnSessDelFail_Object = MibTableColumn
tmnxMobPdnProcPgwPdnSessDelFail = _TmnxMobPdnProcPgwPdnSessDelFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 24),
    _TmnxMobPdnProcPgwPdnSessDelFail_Type()
)
tmnxMobPdnProcPgwPdnSessDelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcPgwPdnSessDelFail.setStatus("current")
_TmnxMobPdnProcAttachPiggyBack_Type = Counter32
_TmnxMobPdnProcAttachPiggyBack_Object = MibTableColumn
tmnxMobPdnProcAttachPiggyBack = _TmnxMobPdnProcAttachPiggyBack_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 25),
    _TmnxMobPdnProcAttachPiggyBack_Type()
)
tmnxMobPdnProcAttachPiggyBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcAttachPiggyBack.setStatus("current")
_TmnxMobPdneHRPDAttachSuccess_Type = Counter32
_TmnxMobPdneHRPDAttachSuccess_Object = MibTableColumn
tmnxMobPdneHRPDAttachSuccess = _TmnxMobPdneHRPDAttachSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 26),
    _TmnxMobPdneHRPDAttachSuccess_Type()
)
tmnxMobPdneHRPDAttachSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdneHRPDAttachSuccess.setStatus("current")
_TmnxMobPdneHRPDAttachFailure_Type = Counter32
_TmnxMobPdneHRPDAttachFailure_Object = MibTableColumn
tmnxMobPdneHRPDAttachFailure = _TmnxMobPdneHRPDAttachFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 27),
    _TmnxMobPdneHRPDAttachFailure_Type()
)
tmnxMobPdneHRPDAttachFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdneHRPDAttachFailure.setStatus("current")
_TmnxMobPdneHRPDDetachSuccess_Type = Counter32
_TmnxMobPdneHRPDDetachSuccess_Object = MibTableColumn
tmnxMobPdneHRPDDetachSuccess = _TmnxMobPdneHRPDDetachSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 28),
    _TmnxMobPdneHRPDDetachSuccess_Type()
)
tmnxMobPdneHRPDDetachSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdneHRPDDetachSuccess.setStatus("current")
_TmnxMobPdneHRPDDetachFailure_Type = Counter32
_TmnxMobPdneHRPDDetachFailure_Object = MibTableColumn
tmnxMobPdneHRPDDetachFailure = _TmnxMobPdneHRPDDetachFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 29),
    _TmnxMobPdneHRPDDetachFailure_Type()
)
tmnxMobPdneHRPDDetachFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdneHRPDDetachFailure.setStatus("current")
_TmnxMobPdneHRPDToLTEHandOverSucc_Type = Counter32
_TmnxMobPdneHRPDToLTEHandOverSucc_Object = MibTableColumn
tmnxMobPdneHRPDToLTEHandOverSucc = _TmnxMobPdneHRPDToLTEHandOverSucc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 30),
    _TmnxMobPdneHRPDToLTEHandOverSucc_Type()
)
tmnxMobPdneHRPDToLTEHandOverSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdneHRPDToLTEHandOverSucc.setStatus("current")
_TmnxMobPdneHRPDToLTEHandOverFail_Type = Counter32
_TmnxMobPdneHRPDToLTEHandOverFail_Object = MibTableColumn
tmnxMobPdneHRPDToLTEHandOverFail = _TmnxMobPdneHRPDToLTEHandOverFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 31),
    _TmnxMobPdneHRPDToLTEHandOverFail_Type()
)
tmnxMobPdneHRPDToLTEHandOverFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdneHRPDToLTEHandOverFail.setStatus("current")
_TmnxMobPdnLTEToeHRPDHandOverSucc_Type = Counter32
_TmnxMobPdnLTEToeHRPDHandOverSucc_Object = MibTableColumn
tmnxMobPdnLTEToeHRPDHandOverSucc = _TmnxMobPdnLTEToeHRPDHandOverSucc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 32),
    _TmnxMobPdnLTEToeHRPDHandOverSucc_Type()
)
tmnxMobPdnLTEToeHRPDHandOverSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnLTEToeHRPDHandOverSucc.setStatus("current")
_TmnxMobPdnLTEToeHRPDHandOverFail_Type = Counter32
_TmnxMobPdnLTEToeHRPDHandOverFail_Object = MibTableColumn
tmnxMobPdnLTEToeHRPDHandOverFail = _TmnxMobPdnLTEToeHRPDHandOverFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 33),
    _TmnxMobPdnLTEToeHRPDHandOverFail_Type()
)
tmnxMobPdnLTEToeHRPDHandOverFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnLTEToeHRPDHandOverFail.setStatus("current")
_TmnxMobPdnInterHSGWHandOvrSucc_Type = Counter32
_TmnxMobPdnInterHSGWHandOvrSucc_Object = MibTableColumn
tmnxMobPdnInterHSGWHandOvrSucc = _TmnxMobPdnInterHSGWHandOvrSucc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 34),
    _TmnxMobPdnInterHSGWHandOvrSucc_Type()
)
tmnxMobPdnInterHSGWHandOvrSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnInterHSGWHandOvrSucc.setStatus("current")
_TmnxMobPdnInterHSGWHandOvrFail_Type = Counter32
_TmnxMobPdnInterHSGWHandOvrFail_Object = MibTableColumn
tmnxMobPdnInterHSGWHandOvrFail = _TmnxMobPdnInterHSGWHandOvrFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 35),
    _TmnxMobPdnInterHSGWHandOvrFail_Type()
)
tmnxMobPdnInterHSGWHandOvrFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnInterHSGWHandOvrFail.setStatus("current")
_TmnxMobPdnProcPDNSuspendNotice_Type = Counter32
_TmnxMobPdnProcPDNSuspendNotice_Object = MibTableColumn
tmnxMobPdnProcPDNSuspendNotice = _TmnxMobPdnProcPDNSuspendNotice_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 36),
    _TmnxMobPdnProcPDNSuspendNotice_Type()
)
tmnxMobPdnProcPDNSuspendNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcPDNSuspendNotice.setStatus("current")
_TmnxMobPdnProcPDNResumeNotice_Type = Counter32
_TmnxMobPdnProcPDNResumeNotice_Object = MibTableColumn
tmnxMobPdnProcPDNResumeNotice = _TmnxMobPdnProcPDNResumeNotice_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 37),
    _TmnxMobPdnProcPDNResumeNotice_Type()
)
tmnxMobPdnProcPDNResumeNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcPDNResumeNotice.setStatus("current")
_TmnxMobPdnProcPDNIRSRP_Type = Counter32
_TmnxMobPdnProcPDNIRSRP_Object = MibTableColumn
tmnxMobPdnProcPDNIRSRP = _TmnxMobPdnProcPDNIRSRP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 38),
    _TmnxMobPdnProcPDNIRSRP_Type()
)
tmnxMobPdnProcPDNIRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcPDNIRSRP.setStatus("current")
_TmnxMobPdnProcEmergncyAttachSuc_Type = Counter32
_TmnxMobPdnProcEmergncyAttachSuc_Object = MibTableColumn
tmnxMobPdnProcEmergncyAttachSuc = _TmnxMobPdnProcEmergncyAttachSuc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 39),
    _TmnxMobPdnProcEmergncyAttachSuc_Type()
)
tmnxMobPdnProcEmergncyAttachSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcEmergncyAttachSuc.setStatus("current")
_TmnxMobPdnProcMmeDedBrDeActiv_Type = Counter32
_TmnxMobPdnProcMmeDedBrDeActiv_Object = MibTableColumn
tmnxMobPdnProcMmeDedBrDeActiv = _TmnxMobPdnProcMmeDedBrDeActiv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 40),
    _TmnxMobPdnProcMmeDedBrDeActiv_Type()
)
tmnxMobPdnProcMmeDedBrDeActiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcMmeDedBrDeActiv.setStatus("current")
_TmnxMobPdnProcMmeDedBrDeAcFails_Type = Counter32
_TmnxMobPdnProcMmeDedBrDeAcFails_Object = MibTableColumn
tmnxMobPdnProcMmeDedBrDeAcFails = _TmnxMobPdnProcMmeDedBrDeAcFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 41),
    _TmnxMobPdnProcMmeDedBrDeAcFails_Type()
)
tmnxMobPdnProcMmeDedBrDeAcFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcMmeDedBrDeAcFails.setStatus("current")
_TmnxMobPdnProcSessDeactDueToSt_Type = Counter32
_TmnxMobPdnProcSessDeactDueToSt_Object = MibTableColumn
tmnxMobPdnProcSessDeactDueToSt = _TmnxMobPdnProcSessDeactDueToSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 42),
    _TmnxMobPdnProcSessDeactDueToSt_Type()
)
tmnxMobPdnProcSessDeactDueToSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcSessDeactDueToSt.setStatus("current")
_TmnxMobPdnProcSessDeactDueToIt_Type = Counter32
_TmnxMobPdnProcSessDeactDueToIt_Object = MibTableColumn
tmnxMobPdnProcSessDeactDueToIt = _TmnxMobPdnProcSessDeactDueToIt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 43),
    _TmnxMobPdnProcSessDeactDueToIt_Type()
)
tmnxMobPdnProcSessDeactDueToIt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnProcSessDeactDueToIt.setStatus("current")
_TmnxMobPdnInterRat3gToEutranSucc_Type = Counter32
_TmnxMobPdnInterRat3gToEutranSucc_Object = MibTableColumn
tmnxMobPdnInterRat3gToEutranSucc = _TmnxMobPdnInterRat3gToEutranSucc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 44),
    _TmnxMobPdnInterRat3gToEutranSucc_Type()
)
tmnxMobPdnInterRat3gToEutranSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnInterRat3gToEutranSucc.setStatus("current")
_TmnxMobPdnInterRat3gToEutranFail_Type = Counter32
_TmnxMobPdnInterRat3gToEutranFail_Object = MibTableColumn
tmnxMobPdnInterRat3gToEutranFail = _TmnxMobPdnInterRat3gToEutranFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 45),
    _TmnxMobPdnInterRat3gToEutranFail_Type()
)
tmnxMobPdnInterRat3gToEutranFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnInterRat3gToEutranFail.setStatus("current")
_TmnxMobPdnInterRatEutranTo3gSucc_Type = Counter32
_TmnxMobPdnInterRatEutranTo3gSucc_Object = MibTableColumn
tmnxMobPdnInterRatEutranTo3gSucc = _TmnxMobPdnInterRatEutranTo3gSucc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 46),
    _TmnxMobPdnInterRatEutranTo3gSucc_Type()
)
tmnxMobPdnInterRatEutranTo3gSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnInterRatEutranTo3gSucc.setStatus("current")
_TmnxMobPdnInterRatEutranTo3gFail_Type = Counter32
_TmnxMobPdnInterRatEutranTo3gFail_Object = MibTableColumn
tmnxMobPdnInterRatEutranTo3gFail = _TmnxMobPdnInterRatEutranTo3gFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 47),
    _TmnxMobPdnInterRatEutranTo3gFail_Type()
)
tmnxMobPdnInterRatEutranTo3gFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnInterRatEutranTo3gFail.setStatus("current")
_TmnxMobPdneHRPDSessDeactSessTO_Type = Counter32
_TmnxMobPdneHRPDSessDeactSessTO_Object = MibTableColumn
tmnxMobPdneHRPDSessDeactSessTO = _TmnxMobPdneHRPDSessDeactSessTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 48),
    _TmnxMobPdneHRPDSessDeactSessTO_Type()
)
tmnxMobPdneHRPDSessDeactSessTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdneHRPDSessDeactSessTO.setStatus("current")
_TmnxMobPdneHRPDSessDeactIdleTO_Type = Counter32
_TmnxMobPdneHRPDSessDeactIdleTO_Object = MibTableColumn
tmnxMobPdneHRPDSessDeactIdleTO = _TmnxMobPdneHRPDSessDeactIdleTO_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 7, 1, 49),
    _TmnxMobPdneHRPDSessDeactIdleTO_Type()
)
tmnxMobPdneHRPDSessDeactIdleTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdneHRPDSessDeactIdleTO.setStatus("current")
_TmnxMobPdnGxPeerTable_Object = MibTable
tmnxMobPdnGxPeerTable = _TmnxMobPdnGxPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerTable.setStatus("current")
_TmnxMobPdnGxPeerEntry_Object = MibTableRow
tmnxMobPdnGxPeerEntry = _TmnxMobPdnGxPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8, 1)
)
tmnxMobPdnGxPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerEntry.setStatus("current")
_TmnxMobPdnGxPeerAddressType_Type = InetAddressType
_TmnxMobPdnGxPeerAddressType_Object = MibTableColumn
tmnxMobPdnGxPeerAddressType = _TmnxMobPdnGxPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8, 1, 1),
    _TmnxMobPdnGxPeerAddressType_Type()
)
tmnxMobPdnGxPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerAddressType.setStatus("current")


class _TmnxMobPdnGxPeerAddress_Type(InetAddress):
    """Custom type tmnxMobPdnGxPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnGxPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnGxPeerAddress_Object = MibTableColumn
tmnxMobPdnGxPeerAddress = _TmnxMobPdnGxPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8, 1, 2),
    _TmnxMobPdnGxPeerAddress_Type()
)
tmnxMobPdnGxPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerAddress.setStatus("current")
_TmnxMobPdnGxPeerPort_Type = InetPortNumber
_TmnxMobPdnGxPeerPort_Object = MibTableColumn
tmnxMobPdnGxPeerPort = _TmnxMobPdnGxPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8, 1, 3),
    _TmnxMobPdnGxPeerPort_Type()
)
tmnxMobPdnGxPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerPort.setStatus("current")
_TmnxMobPdnGxPeerLastChanged_Type = TimeStamp
_TmnxMobPdnGxPeerLastChanged_Object = MibTableColumn
tmnxMobPdnGxPeerLastChanged = _TmnxMobPdnGxPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8, 1, 4),
    _TmnxMobPdnGxPeerLastChanged_Type()
)
tmnxMobPdnGxPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerLastChanged.setStatus("current")
_TmnxMobPdnGxPeerCreateTime_Type = TimeStamp
_TmnxMobPdnGxPeerCreateTime_Object = MibTableColumn
tmnxMobPdnGxPeerCreateTime = _TmnxMobPdnGxPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8, 1, 5),
    _TmnxMobPdnGxPeerCreateTime_Type()
)
tmnxMobPdnGxPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerCreateTime.setStatus("current")
_TmnxMobPdnGxPeerPathMgmtState_Type = TmnxMobDiaPathMgmtState
_TmnxMobPdnGxPeerPathMgmtState_Object = MibTableColumn
tmnxMobPdnGxPeerPathMgmtState = _TmnxMobPdnGxPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8, 1, 6),
    _TmnxMobPdnGxPeerPathMgmtState_Type()
)
tmnxMobPdnGxPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerPathMgmtState.setStatus("current")
_TmnxMobPdnGxPeerDetailState_Type = TmnxMobDiaDetailPathMgmtState
_TmnxMobPdnGxPeerDetailState_Object = MibTableColumn
tmnxMobPdnGxPeerDetailState = _TmnxMobPdnGxPeerDetailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 8, 1, 7),
    _TmnxMobPdnGxPeerDetailState_Type()
)
tmnxMobPdnGxPeerDetailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerDetailState.setStatus("current")
_TmnxMobPdnGxStatTable_Object = MibTable
tmnxMobPdnGxStatTable = _TmnxMobPdnGxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTable.setStatus("current")
_TmnxMobPdnGxStatEntry_Object = MibTableRow
tmnxMobPdnGxStatEntry = _TmnxMobPdnGxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1)
)
tmnxMobPdnGxStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatEntry.setStatus("current")
_TmnxMobPdnGxStatTxCer_Type = Counter32
_TmnxMobPdnGxStatTxCer_Object = MibTableColumn
tmnxMobPdnGxStatTxCer = _TmnxMobPdnGxStatTxCer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 1),
    _TmnxMobPdnGxStatTxCer_Type()
)
tmnxMobPdnGxStatTxCer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxCer.setStatus("current")
_TmnxMobPdnGxStatRxCea_Type = Counter32
_TmnxMobPdnGxStatRxCea_Object = MibTableColumn
tmnxMobPdnGxStatRxCea = _TmnxMobPdnGxStatRxCea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 2),
    _TmnxMobPdnGxStatRxCea_Type()
)
tmnxMobPdnGxStatRxCea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCea.setStatus("current")
_TmnxMobPdnGxStatRxDpr_Type = Counter32
_TmnxMobPdnGxStatRxDpr_Object = MibTableColumn
tmnxMobPdnGxStatRxDpr = _TmnxMobPdnGxStatRxDpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 3),
    _TmnxMobPdnGxStatRxDpr_Type()
)
tmnxMobPdnGxStatRxDpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxDpr.setStatus("current")
_TmnxMobPdnGxStatTxDpa_Type = Counter32
_TmnxMobPdnGxStatTxDpa_Object = MibTableColumn
tmnxMobPdnGxStatTxDpa = _TmnxMobPdnGxStatTxDpa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 4),
    _TmnxMobPdnGxStatTxDpa_Type()
)
tmnxMobPdnGxStatTxDpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxDpa.setStatus("current")
_TmnxMobPdnGxStatTxDwr_Type = Counter32
_TmnxMobPdnGxStatTxDwr_Object = MibTableColumn
tmnxMobPdnGxStatTxDwr = _TmnxMobPdnGxStatTxDwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 5),
    _TmnxMobPdnGxStatTxDwr_Type()
)
tmnxMobPdnGxStatTxDwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxDwr.setStatus("current")
_TmnxMobPdnGxStatRxDwa_Type = Counter32
_TmnxMobPdnGxStatRxDwa_Object = MibTableColumn
tmnxMobPdnGxStatRxDwa = _TmnxMobPdnGxStatRxDwa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 6),
    _TmnxMobPdnGxStatRxDwa_Type()
)
tmnxMobPdnGxStatRxDwa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxDwa.setStatus("current")
_TmnxMobPdnGxStatConnAttempts_Type = Counter32
_TmnxMobPdnGxStatConnAttempts_Object = MibTableColumn
tmnxMobPdnGxStatConnAttempts = _TmnxMobPdnGxStatConnAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 7),
    _TmnxMobPdnGxStatConnAttempts_Type()
)
tmnxMobPdnGxStatConnAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatConnAttempts.setStatus("current")
_TmnxMobPdnGxStatConnFailures_Type = Counter32
_TmnxMobPdnGxStatConnFailures_Object = MibTableColumn
tmnxMobPdnGxStatConnFailures = _TmnxMobPdnGxStatConnFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 8),
    _TmnxMobPdnGxStatConnFailures_Type()
)
tmnxMobPdnGxStatConnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatConnFailures.setStatus("current")
_TmnxMobPdnGxStatRxTransportDisc_Type = Counter32
_TmnxMobPdnGxStatRxTransportDisc_Object = MibTableColumn
tmnxMobPdnGxStatRxTransportDisc = _TmnxMobPdnGxStatRxTransportDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 9),
    _TmnxMobPdnGxStatRxTransportDisc_Type()
)
tmnxMobPdnGxStatRxTransportDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxTransportDisc.setStatus("current")
_TmnxMobPdnGxStatRxMsgUnexpectVer_Type = Counter32
_TmnxMobPdnGxStatRxMsgUnexpectVer_Object = MibTableColumn
tmnxMobPdnGxStatRxMsgUnexpectVer = _TmnxMobPdnGxStatRxMsgUnexpectVer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 10),
    _TmnxMobPdnGxStatRxMsgUnexpectVer_Type()
)
tmnxMobPdnGxStatRxMsgUnexpectVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxMsgUnexpectVer.setStatus("current")
_TmnxMobPdnGxStatRxMsgTooBig_Type = Counter32
_TmnxMobPdnGxStatRxMsgTooBig_Object = MibTableColumn
tmnxMobPdnGxStatRxMsgTooBig = _TmnxMobPdnGxStatRxMsgTooBig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 11),
    _TmnxMobPdnGxStatRxMsgTooBig_Type()
)
tmnxMobPdnGxStatRxMsgTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxMsgTooBig.setStatus("current")
_TmnxMobPdnGxStatRxMsgTooSmall_Type = Counter32
_TmnxMobPdnGxStatRxMsgTooSmall_Object = MibTableColumn
tmnxMobPdnGxStatRxMsgTooSmall = _TmnxMobPdnGxStatRxMsgTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 12),
    _TmnxMobPdnGxStatRxMsgTooSmall_Type()
)
tmnxMobPdnGxStatRxMsgTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxMsgTooSmall.setStatus("current")
_TmnxMobPdnGxStatRxInvalidCea_Type = Counter32
_TmnxMobPdnGxStatRxInvalidCea_Object = MibTableColumn
tmnxMobPdnGxStatRxInvalidCea = _TmnxMobPdnGxStatRxInvalidCea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 13),
    _TmnxMobPdnGxStatRxInvalidCea_Type()
)
tmnxMobPdnGxStatRxInvalidCea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxInvalidCea.setStatus("current")
_TmnxMobPdnGxStatRxMsgs_Type = Counter32
_TmnxMobPdnGxStatRxMsgs_Object = MibTableColumn
tmnxMobPdnGxStatRxMsgs = _TmnxMobPdnGxStatRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 14),
    _TmnxMobPdnGxStatRxMsgs_Type()
)
tmnxMobPdnGxStatRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxMsgs.setStatus("current")
_TmnxMobPdnGxStatTxMsgs_Type = Counter32
_TmnxMobPdnGxStatTxMsgs_Object = MibTableColumn
tmnxMobPdnGxStatTxMsgs = _TmnxMobPdnGxStatTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 15),
    _TmnxMobPdnGxStatTxMsgs_Type()
)
tmnxMobPdnGxStatTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxMsgs.setStatus("current")
_TmnxMobPdnGxStatTxRetransmitMsgs_Type = Counter32
_TmnxMobPdnGxStatTxRetransmitMsgs_Object = MibTableColumn
tmnxMobPdnGxStatTxRetransmitMsgs = _TmnxMobPdnGxStatTxRetransmitMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 16),
    _TmnxMobPdnGxStatTxRetransmitMsgs_Type()
)
tmnxMobPdnGxStatTxRetransmitMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxRetransmitMsgs.setStatus("current")
_TmnxMobPdnGxStatTxCcrInitial_Type = Counter32
_TmnxMobPdnGxStatTxCcrInitial_Object = MibTableColumn
tmnxMobPdnGxStatTxCcrInitial = _TmnxMobPdnGxStatTxCcrInitial_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 17),
    _TmnxMobPdnGxStatTxCcrInitial_Type()
)
tmnxMobPdnGxStatTxCcrInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxCcrInitial.setStatus("current")
_TmnxMobPdnGxStatRxCcaInitial_Type = Counter32
_TmnxMobPdnGxStatRxCcaInitial_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaInitial = _TmnxMobPdnGxStatRxCcaInitial_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 18),
    _TmnxMobPdnGxStatRxCcaInitial_Type()
)
tmnxMobPdnGxStatRxCcaInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaInitial.setStatus("current")
_TmnxMobPdnGxStatTxCcrUpdate_Type = Counter32
_TmnxMobPdnGxStatTxCcrUpdate_Object = MibTableColumn
tmnxMobPdnGxStatTxCcrUpdate = _TmnxMobPdnGxStatTxCcrUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 19),
    _TmnxMobPdnGxStatTxCcrUpdate_Type()
)
tmnxMobPdnGxStatTxCcrUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxCcrUpdate.setStatus("current")
_TmnxMobPdnGxStatRxCcaUpdate_Type = Counter32
_TmnxMobPdnGxStatRxCcaUpdate_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaUpdate = _TmnxMobPdnGxStatRxCcaUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 20),
    _TmnxMobPdnGxStatRxCcaUpdate_Type()
)
tmnxMobPdnGxStatRxCcaUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaUpdate.setStatus("current")
_TmnxMobPdnGxStatTxCcrTerminate_Type = Counter32
_TmnxMobPdnGxStatTxCcrTerminate_Object = MibTableColumn
tmnxMobPdnGxStatTxCcrTerminate = _TmnxMobPdnGxStatTxCcrTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 21),
    _TmnxMobPdnGxStatTxCcrTerminate_Type()
)
tmnxMobPdnGxStatTxCcrTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxCcrTerminate.setStatus("current")
_TmnxMobPdnGxStatRxCcaTerminate_Type = Counter32
_TmnxMobPdnGxStatRxCcaTerminate_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaTerminate = _TmnxMobPdnGxStatRxCcaTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 22),
    _TmnxMobPdnGxStatRxCcaTerminate_Type()
)
tmnxMobPdnGxStatRxCcaTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaTerminate.setStatus("current")
_TmnxMobPdnGxStatCcrInitFails_Type = Counter32
_TmnxMobPdnGxStatCcrInitFails_Object = MibTableColumn
tmnxMobPdnGxStatCcrInitFails = _TmnxMobPdnGxStatCcrInitFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 23),
    _TmnxMobPdnGxStatCcrInitFails_Type()
)
tmnxMobPdnGxStatCcrInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatCcrInitFails.setStatus("current")
_TmnxMobPdnGxStatCcrUpdateFails_Type = Counter32
_TmnxMobPdnGxStatCcrUpdateFails_Object = MibTableColumn
tmnxMobPdnGxStatCcrUpdateFails = _TmnxMobPdnGxStatCcrUpdateFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 24),
    _TmnxMobPdnGxStatCcrUpdateFails_Type()
)
tmnxMobPdnGxStatCcrUpdateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatCcrUpdateFails.setStatus("current")
_TmnxMobPdnGxStatCcrTermFails_Type = Counter32
_TmnxMobPdnGxStatCcrTermFails_Object = MibTableColumn
tmnxMobPdnGxStatCcrTermFails = _TmnxMobPdnGxStatCcrTermFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 25),
    _TmnxMobPdnGxStatCcrTermFails_Type()
)
tmnxMobPdnGxStatCcrTermFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatCcrTermFails.setStatus("current")
_TmnxMobPdnGxStatRxRar_Type = Counter32
_TmnxMobPdnGxStatRxRar_Object = MibTableColumn
tmnxMobPdnGxStatRxRar = _TmnxMobPdnGxStatRxRar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 26),
    _TmnxMobPdnGxStatRxRar_Type()
)
tmnxMobPdnGxStatRxRar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxRar.setStatus("current")
_TmnxMobPdnGxStatTxRaa_Type = Counter32
_TmnxMobPdnGxStatTxRaa_Object = MibTableColumn
tmnxMobPdnGxStatTxRaa = _TmnxMobPdnGxStatTxRaa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 27),
    _TmnxMobPdnGxStatTxRaa_Type()
)
tmnxMobPdnGxStatTxRaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxRaa.setStatus("current")
_TmnxMobPdnGxStatTxRaaNack_Type = Counter32
_TmnxMobPdnGxStatTxRaaNack_Object = MibTableColumn
tmnxMobPdnGxStatTxRaaNack = _TmnxMobPdnGxStatTxRaaNack_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 28),
    _TmnxMobPdnGxStatTxRaaNack_Type()
)
tmnxMobPdnGxStatTxRaaNack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxRaaNack.setStatus("current")
_TmnxMobPdnGxStatBberfs_Type = Counter32
_TmnxMobPdnGxStatBberfs_Object = MibTableColumn
tmnxMobPdnGxStatBberfs = _TmnxMobPdnGxStatBberfs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 29),
    _TmnxMobPdnGxStatBberfs_Type()
)
tmnxMobPdnGxStatBberfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatBberfs.setStatus("current")
_TmnxMobPdnGxStatRxMalformedPkts_Type = Counter32
_TmnxMobPdnGxStatRxMalformedPkts_Object = MibTableColumn
tmnxMobPdnGxStatRxMalformedPkts = _TmnxMobPdnGxStatRxMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 30),
    _TmnxMobPdnGxStatRxMalformedPkts_Type()
)
tmnxMobPdnGxStatRxMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxMalformedPkts.setStatus("current")
_TmnxMobPdnGxStatRxCcaIMalformPkt_Type = Counter32
_TmnxMobPdnGxStatRxCcaIMalformPkt_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaIMalformPkt = _TmnxMobPdnGxStatRxCcaIMalformPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 31),
    _TmnxMobPdnGxStatRxCcaIMalformPkt_Type()
)
tmnxMobPdnGxStatRxCcaIMalformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaIMalformPkt.setStatus("current")
_TmnxMobPdnGxStatRxCcaUMalformPkt_Type = Counter32
_TmnxMobPdnGxStatRxCcaUMalformPkt_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaUMalformPkt = _TmnxMobPdnGxStatRxCcaUMalformPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 32),
    _TmnxMobPdnGxStatRxCcaUMalformPkt_Type()
)
tmnxMobPdnGxStatRxCcaUMalformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaUMalformPkt.setStatus("current")
_TmnxMobPdnGxStatRxCcaTMalformPkt_Type = Counter32
_TmnxMobPdnGxStatRxCcaTMalformPkt_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaTMalformPkt = _TmnxMobPdnGxStatRxCcaTMalformPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 33),
    _TmnxMobPdnGxStatRxCcaTMalformPkt_Type()
)
tmnxMobPdnGxStatRxCcaTMalformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaTMalformPkt.setStatus("current")
_TmnxMobPdnGxStatRxRarMalformPkts_Type = Counter32
_TmnxMobPdnGxStatRxRarMalformPkts_Object = MibTableColumn
tmnxMobPdnGxStatRxRarMalformPkts = _TmnxMobPdnGxStatRxRarMalformPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 34),
    _TmnxMobPdnGxStatRxRarMalformPkts_Type()
)
tmnxMobPdnGxStatRxRarMalformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxRarMalformPkts.setStatus("current")
_TmnxMobPdnGxStatRxUnknownPkts_Type = Counter32
_TmnxMobPdnGxStatRxUnknownPkts_Object = MibTableColumn
tmnxMobPdnGxStatRxUnknownPkts = _TmnxMobPdnGxStatRxUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 35),
    _TmnxMobPdnGxStatRxUnknownPkts_Type()
)
tmnxMobPdnGxStatRxUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxUnknownPkts.setStatus("current")
_TmnxMobPdnGxStatRxCcaIUnknownPkt_Type = Counter32
_TmnxMobPdnGxStatRxCcaIUnknownPkt_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaIUnknownPkt = _TmnxMobPdnGxStatRxCcaIUnknownPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 36),
    _TmnxMobPdnGxStatRxCcaIUnknownPkt_Type()
)
tmnxMobPdnGxStatRxCcaIUnknownPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaIUnknownPkt.setStatus("current")
_TmnxMobPdnGxStatRxCcaUUnknownPkt_Type = Counter32
_TmnxMobPdnGxStatRxCcaUUnknownPkt_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaUUnknownPkt = _TmnxMobPdnGxStatRxCcaUUnknownPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 37),
    _TmnxMobPdnGxStatRxCcaUUnknownPkt_Type()
)
tmnxMobPdnGxStatRxCcaUUnknownPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaUUnknownPkt.setStatus("current")
_TmnxMobPdnGxStatRxCcaTUnknownPkt_Type = Counter32
_TmnxMobPdnGxStatRxCcaTUnknownPkt_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaTUnknownPkt = _TmnxMobPdnGxStatRxCcaTUnknownPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 38),
    _TmnxMobPdnGxStatRxCcaTUnknownPkt_Type()
)
tmnxMobPdnGxStatRxCcaTUnknownPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaTUnknownPkt.setStatus("current")
_TmnxMobPdnGxStatRxRarUnknownPkts_Type = Counter32
_TmnxMobPdnGxStatRxRarUnknownPkts_Object = MibTableColumn
tmnxMobPdnGxStatRxRarUnknownPkts = _TmnxMobPdnGxStatRxRarUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 39),
    _TmnxMobPdnGxStatRxRarUnknownPkts_Type()
)
tmnxMobPdnGxStatRxRarUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxRarUnknownPkts.setStatus("current")
_TmnxMobPdnGxStatRxMissingIePkts_Type = Counter32
_TmnxMobPdnGxStatRxMissingIePkts_Object = MibTableColumn
tmnxMobPdnGxStatRxMissingIePkts = _TmnxMobPdnGxStatRxMissingIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 40),
    _TmnxMobPdnGxStatRxMissingIePkts_Type()
)
tmnxMobPdnGxStatRxMissingIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxMissingIePkts.setStatus("current")
_TmnxMobPdnGxStatRxCcaIMissIePkts_Type = Counter32
_TmnxMobPdnGxStatRxCcaIMissIePkts_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaIMissIePkts = _TmnxMobPdnGxStatRxCcaIMissIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 41),
    _TmnxMobPdnGxStatRxCcaIMissIePkts_Type()
)
tmnxMobPdnGxStatRxCcaIMissIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaIMissIePkts.setStatus("current")
_TmnxMobPdnGxStatRxCcaUMissIePkts_Type = Counter32
_TmnxMobPdnGxStatRxCcaUMissIePkts_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaUMissIePkts = _TmnxMobPdnGxStatRxCcaUMissIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 42),
    _TmnxMobPdnGxStatRxCcaUMissIePkts_Type()
)
tmnxMobPdnGxStatRxCcaUMissIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaUMissIePkts.setStatus("current")
_TmnxMobPdnGxStatRxCcaTMissIePkts_Type = Counter32
_TmnxMobPdnGxStatRxCcaTMissIePkts_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaTMissIePkts = _TmnxMobPdnGxStatRxCcaTMissIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 43),
    _TmnxMobPdnGxStatRxCcaTMissIePkts_Type()
)
tmnxMobPdnGxStatRxCcaTMissIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaTMissIePkts.setStatus("current")
_TmnxMobPdnGxStatRxRarMissIePkts_Type = Counter32
_TmnxMobPdnGxStatRxRarMissIePkts_Object = MibTableColumn
tmnxMobPdnGxStatRxRarMissIePkts = _TmnxMobPdnGxStatRxRarMissIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 44),
    _TmnxMobPdnGxStatRxRarMissIePkts_Type()
)
tmnxMobPdnGxStatRxRarMissIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxRarMissIePkts.setStatus("current")
_TmnxMobPdnGxStatRxCcaIUnkSession_Type = Counter32
_TmnxMobPdnGxStatRxCcaIUnkSession_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaIUnkSession = _TmnxMobPdnGxStatRxCcaIUnkSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 45),
    _TmnxMobPdnGxStatRxCcaIUnkSession_Type()
)
tmnxMobPdnGxStatRxCcaIUnkSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaIUnkSession.setStatus("current")
_TmnxMobPdnGxStatRxCcaUUnkSession_Type = Counter32
_TmnxMobPdnGxStatRxCcaUUnkSession_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaUUnkSession = _TmnxMobPdnGxStatRxCcaUUnkSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 46),
    _TmnxMobPdnGxStatRxCcaUUnkSession_Type()
)
tmnxMobPdnGxStatRxCcaUUnkSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaUUnkSession.setStatus("current")
_TmnxMobPdnGxStatRxCcaTUnkSession_Type = Counter32
_TmnxMobPdnGxStatRxCcaTUnkSession_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaTUnkSession = _TmnxMobPdnGxStatRxCcaTUnkSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 47),
    _TmnxMobPdnGxStatRxCcaTUnkSession_Type()
)
tmnxMobPdnGxStatRxCcaTUnkSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaTUnkSession.setStatus("current")
_TmnxMobPdnGxStatRxRarUnkSession_Type = Counter32
_TmnxMobPdnGxStatRxRarUnkSession_Object = MibTableColumn
tmnxMobPdnGxStatRxRarUnkSession = _TmnxMobPdnGxStatRxRarUnkSession_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 48),
    _TmnxMobPdnGxStatRxRarUnkSession_Type()
)
tmnxMobPdnGxStatRxRarUnkSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxRarUnkSession.setStatus("current")
_TmnxMobPdnGxStatTxDpr_Type = Counter32
_TmnxMobPdnGxStatTxDpr_Object = MibTableColumn
tmnxMobPdnGxStatTxDpr = _TmnxMobPdnGxStatTxDpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 49),
    _TmnxMobPdnGxStatTxDpr_Type()
)
tmnxMobPdnGxStatTxDpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxDpr.setStatus("current")
_TmnxMobPdnGxStatRxDpa_Type = Counter32
_TmnxMobPdnGxStatRxDpa_Object = MibTableColumn
tmnxMobPdnGxStatRxDpa = _TmnxMobPdnGxStatRxDpa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 50),
    _TmnxMobPdnGxStatRxDpa_Type()
)
tmnxMobPdnGxStatRxDpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxDpa.setStatus("current")
_TmnxMobPdnGxStatRxDwr_Type = Counter32
_TmnxMobPdnGxStatRxDwr_Object = MibTableColumn
tmnxMobPdnGxStatRxDwr = _TmnxMobPdnGxStatRxDwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 51),
    _TmnxMobPdnGxStatRxDwr_Type()
)
tmnxMobPdnGxStatRxDwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxDwr.setStatus("current")
_TmnxMobPdnGxStatTxDwa_Type = Counter32
_TmnxMobPdnGxStatTxDwa_Object = MibTableColumn
tmnxMobPdnGxStatTxDwa = _TmnxMobPdnGxStatTxDwa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 52),
    _TmnxMobPdnGxStatTxDwa_Type()
)
tmnxMobPdnGxStatTxDwa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatTxDwa.setStatus("current")
_TmnxMobPdnGxStatRxCcaInitialFail_Type = Counter32
_TmnxMobPdnGxStatRxCcaInitialFail_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaInitialFail = _TmnxMobPdnGxStatRxCcaInitialFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 53),
    _TmnxMobPdnGxStatRxCcaInitialFail_Type()
)
tmnxMobPdnGxStatRxCcaInitialFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaInitialFail.setStatus("current")
_TmnxMobPdnGxStatRxCcaUpdateFail_Type = Counter32
_TmnxMobPdnGxStatRxCcaUpdateFail_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaUpdateFail = _TmnxMobPdnGxStatRxCcaUpdateFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 54),
    _TmnxMobPdnGxStatRxCcaUpdateFail_Type()
)
tmnxMobPdnGxStatRxCcaUpdateFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaUpdateFail.setStatus("current")
_TmnxMobPdnGxStatRxCcaTermFail_Type = Counter32
_TmnxMobPdnGxStatRxCcaTermFail_Object = MibTableColumn
tmnxMobPdnGxStatRxCcaTermFail = _TmnxMobPdnGxStatRxCcaTermFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 55),
    _TmnxMobPdnGxStatRxCcaTermFail_Type()
)
tmnxMobPdnGxStatRxCcaTermFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatRxCcaTermFail.setStatus("current")
_TmnxMobPdnGxStatReTxCcrInitial_Type = Counter32
_TmnxMobPdnGxStatReTxCcrInitial_Object = MibTableColumn
tmnxMobPdnGxStatReTxCcrInitial = _TmnxMobPdnGxStatReTxCcrInitial_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 56),
    _TmnxMobPdnGxStatReTxCcrInitial_Type()
)
tmnxMobPdnGxStatReTxCcrInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatReTxCcrInitial.setStatus("current")
_TmnxMobPdnGxStatReTxCcrUpdate_Type = Counter32
_TmnxMobPdnGxStatReTxCcrUpdate_Object = MibTableColumn
tmnxMobPdnGxStatReTxCcrUpdate = _TmnxMobPdnGxStatReTxCcrUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 57),
    _TmnxMobPdnGxStatReTxCcrUpdate_Type()
)
tmnxMobPdnGxStatReTxCcrUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatReTxCcrUpdate.setStatus("current")
_TmnxMobPdnGxStatReTxCcrTerm_Type = Counter32
_TmnxMobPdnGxStatReTxCcrTerm_Object = MibTableColumn
tmnxMobPdnGxStatReTxCcrTerm = _TmnxMobPdnGxStatReTxCcrTerm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 9, 1, 58),
    _TmnxMobPdnGxStatReTxCcrTerm_Type()
)
tmnxMobPdnGxStatReTxCcrTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxStatReTxCcrTerm.setStatus("current")
_TmnxMobPdnGnStatTable_Object = MibTable
tmnxMobPdnGnStatTable = _TmnxMobPdnGnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatTable.setStatus("current")
_TmnxMobPdnGnStatEntry_Object = MibTableRow
tmnxMobPdnGnStatEntry = _TmnxMobPdnGnStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1)
)
tmnxMobPdnGnStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatEntry.setStatus("current")
_TmnxMobPdnGnStatCreatePdpReq_Type = Counter32
_TmnxMobPdnGnStatCreatePdpReq_Object = MibTableColumn
tmnxMobPdnGnStatCreatePdpReq = _TmnxMobPdnGnStatCreatePdpReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 1),
    _TmnxMobPdnGnStatCreatePdpReq_Type()
)
tmnxMobPdnGnStatCreatePdpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatCreatePdpReq.setStatus("current")
_TmnxMobPdnGnStatCreatePdpRsp_Type = Counter32
_TmnxMobPdnGnStatCreatePdpRsp_Object = MibTableColumn
tmnxMobPdnGnStatCreatePdpRsp = _TmnxMobPdnGnStatCreatePdpRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 2),
    _TmnxMobPdnGnStatCreatePdpRsp_Type()
)
tmnxMobPdnGnStatCreatePdpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatCreatePdpRsp.setStatus("current")
_TmnxMobPdnGnStatDeletePdpReq_Type = Counter32
_TmnxMobPdnGnStatDeletePdpReq_Object = MibTableColumn
tmnxMobPdnGnStatDeletePdpReq = _TmnxMobPdnGnStatDeletePdpReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 3),
    _TmnxMobPdnGnStatDeletePdpReq_Type()
)
tmnxMobPdnGnStatDeletePdpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatDeletePdpReq.setStatus("current")
_TmnxMobPdnGnStatDeletePdpRsp_Type = Counter32
_TmnxMobPdnGnStatDeletePdpRsp_Object = MibTableColumn
tmnxMobPdnGnStatDeletePdpRsp = _TmnxMobPdnGnStatDeletePdpRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 4),
    _TmnxMobPdnGnStatDeletePdpRsp_Type()
)
tmnxMobPdnGnStatDeletePdpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatDeletePdpRsp.setStatus("current")
_TmnxMobPdnGnStatModifyPdpReq_Type = Counter32
_TmnxMobPdnGnStatModifyPdpReq_Object = MibTableColumn
tmnxMobPdnGnStatModifyPdpReq = _TmnxMobPdnGnStatModifyPdpReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 5),
    _TmnxMobPdnGnStatModifyPdpReq_Type()
)
tmnxMobPdnGnStatModifyPdpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatModifyPdpReq.setStatus("current")
_TmnxMobPdnGnStatModifyPdpRsp_Type = Counter32
_TmnxMobPdnGnStatModifyPdpRsp_Object = MibTableColumn
tmnxMobPdnGnStatModifyPdpRsp = _TmnxMobPdnGnStatModifyPdpRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 6),
    _TmnxMobPdnGnStatModifyPdpRsp_Type()
)
tmnxMobPdnGnStatModifyPdpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatModifyPdpRsp.setStatus("current")
_TmnxMobPdnGnStatRxEchoRequests_Type = Counter32
_TmnxMobPdnGnStatRxEchoRequests_Object = MibTableColumn
tmnxMobPdnGnStatRxEchoRequests = _TmnxMobPdnGnStatRxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 7),
    _TmnxMobPdnGnStatRxEchoRequests_Type()
)
tmnxMobPdnGnStatRxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatRxEchoRequests.setStatus("current")
_TmnxMobPdnGnStatTxEchoResponses_Type = Counter32
_TmnxMobPdnGnStatTxEchoResponses_Object = MibTableColumn
tmnxMobPdnGnStatTxEchoResponses = _TmnxMobPdnGnStatTxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 8),
    _TmnxMobPdnGnStatTxEchoResponses_Type()
)
tmnxMobPdnGnStatTxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatTxEchoResponses.setStatus("current")
_TmnxMobPdnGnStatTxEchoRequests_Type = Counter32
_TmnxMobPdnGnStatTxEchoRequests_Object = MibTableColumn
tmnxMobPdnGnStatTxEchoRequests = _TmnxMobPdnGnStatTxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 9),
    _TmnxMobPdnGnStatTxEchoRequests_Type()
)
tmnxMobPdnGnStatTxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatTxEchoRequests.setStatus("current")
_TmnxMobPdnGnStatRxEchoResponses_Type = Counter32
_TmnxMobPdnGnStatRxEchoResponses_Object = MibTableColumn
tmnxMobPdnGnStatRxEchoResponses = _TmnxMobPdnGnStatRxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 10),
    _TmnxMobPdnGnStatRxEchoResponses_Type()
)
tmnxMobPdnGnStatRxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatRxEchoResponses.setStatus("current")
_TmnxMobPdnGnStatRxErrorsIndCnt_Type = Counter32
_TmnxMobPdnGnStatRxErrorsIndCnt_Object = MibTableColumn
tmnxMobPdnGnStatRxErrorsIndCnt = _TmnxMobPdnGnStatRxErrorsIndCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 11),
    _TmnxMobPdnGnStatRxErrorsIndCnt_Type()
)
tmnxMobPdnGnStatRxErrorsIndCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatRxErrorsIndCnt.setStatus("current")
_TmnxMobPdnGnStatTxErrorsIndCnt_Type = Counter32
_TmnxMobPdnGnStatTxErrorsIndCnt_Object = MibTableColumn
tmnxMobPdnGnStatTxErrorsIndCnt = _TmnxMobPdnGnStatTxErrorsIndCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 12),
    _TmnxMobPdnGnStatTxErrorsIndCnt_Type()
)
tmnxMobPdnGnStatTxErrorsIndCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatTxErrorsIndCnt.setStatus("current")
_TmnxMobPdnGnStatRxMalformedPkts_Type = Counter32
_TmnxMobPdnGnStatRxMalformedPkts_Object = MibTableColumn
tmnxMobPdnGnStatRxMalformedPkts = _TmnxMobPdnGnStatRxMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 13),
    _TmnxMobPdnGnStatRxMalformedPkts_Type()
)
tmnxMobPdnGnStatRxMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatRxMalformedPkts.setStatus("current")
_TmnxMobPdnGnStatRxUnknownPkts_Type = Counter32
_TmnxMobPdnGnStatRxUnknownPkts_Object = MibTableColumn
tmnxMobPdnGnStatRxUnknownPkts = _TmnxMobPdnGnStatRxUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 14),
    _TmnxMobPdnGnStatRxUnknownPkts_Type()
)
tmnxMobPdnGnStatRxUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatRxUnknownPkts.setStatus("current")
_TmnxMobPdnGnStatRxMissingIePkts_Type = Counter32
_TmnxMobPdnGnStatRxMissingIePkts_Object = MibTableColumn
tmnxMobPdnGnStatRxMissingIePkts = _TmnxMobPdnGnStatRxMissingIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 15),
    _TmnxMobPdnGnStatRxMissingIePkts_Type()
)
tmnxMobPdnGnStatRxMissingIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatRxMissingIePkts.setStatus("current")
_TmnxMobPdnGnStatPeerRestarts_Type = Counter32
_TmnxMobPdnGnStatPeerRestarts_Object = MibTableColumn
tmnxMobPdnGnStatPeerRestarts = _TmnxMobPdnGnStatPeerRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 16),
    _TmnxMobPdnGnStatPeerRestarts_Type()
)
tmnxMobPdnGnStatPeerRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatPeerRestarts.setStatus("current")
_TmnxMobPdnGnStatPeerRestrtCount_Type = Counter32
_TmnxMobPdnGnStatPeerRestrtCount_Object = MibTableColumn
tmnxMobPdnGnStatPeerRestrtCount = _TmnxMobPdnGnStatPeerRestrtCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 17),
    _TmnxMobPdnGnStatPeerRestrtCount_Type()
)
tmnxMobPdnGnStatPeerRestrtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatPeerRestrtCount.setStatus("current")
_TmnxMobPdnGnStatPathMgmtFails_Type = Counter32
_TmnxMobPdnGnStatPathMgmtFails_Object = MibTableColumn
tmnxMobPdnGnStatPathMgmtFails = _TmnxMobPdnGnStatPathMgmtFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 10, 1, 18),
    _TmnxMobPdnGnStatPathMgmtFails_Type()
)
tmnxMobPdnGnStatPathMgmtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnStatPathMgmtFails.setStatus("current")
_TmnxMobPdnGaStatTable_Object = MibTable
tmnxMobPdnGaStatTable = _TmnxMobPdnGaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTable.setStatus("current")
_TmnxMobPdnGaStatEntry_Object = MibTableRow
tmnxMobPdnGaStatEntry = _TmnxMobPdnGaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1)
)
tmnxMobPdnGaStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatEntry.setStatus("current")
_TmnxMobPdnGaStatAddressType_Type = InetAddressType
_TmnxMobPdnGaStatAddressType_Object = MibTableColumn
tmnxMobPdnGaStatAddressType = _TmnxMobPdnGaStatAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 1),
    _TmnxMobPdnGaStatAddressType_Type()
)
tmnxMobPdnGaStatAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatAddressType.setStatus("current")


class _TmnxMobPdnGaStatAddress_Type(InetAddress):
    """Custom type tmnxMobPdnGaStatAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnGaStatAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnGaStatAddress_Object = MibTableColumn
tmnxMobPdnGaStatAddress = _TmnxMobPdnGaStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 2),
    _TmnxMobPdnGaStatAddress_Type()
)
tmnxMobPdnGaStatAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatAddress.setStatus("current")
_TmnxMobPdnGaStatPort_Type = InetPortNumber
_TmnxMobPdnGaStatPort_Object = MibTableColumn
tmnxMobPdnGaStatPort = _TmnxMobPdnGaStatPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 3),
    _TmnxMobPdnGaStatPort_Type()
)
tmnxMobPdnGaStatPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatPort.setStatus("current")
_TmnxMobPdnGaStatLastChanged_Type = TimeStamp
_TmnxMobPdnGaStatLastChanged_Object = MibTableColumn
tmnxMobPdnGaStatLastChanged = _TmnxMobPdnGaStatLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 4),
    _TmnxMobPdnGaStatLastChanged_Type()
)
tmnxMobPdnGaStatLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatLastChanged.setStatus("current")
_TmnxMobPdnGaStatCreateTime_Type = TimeStamp
_TmnxMobPdnGaStatCreateTime_Object = MibTableColumn
tmnxMobPdnGaStatCreateTime = _TmnxMobPdnGaStatCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 5),
    _TmnxMobPdnGaStatCreateTime_Type()
)
tmnxMobPdnGaStatCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatCreateTime.setStatus("current")
_TmnxMobPdnGaStatRxEchoRequests_Type = Counter32
_TmnxMobPdnGaStatRxEchoRequests_Object = MibTableColumn
tmnxMobPdnGaStatRxEchoRequests = _TmnxMobPdnGaStatRxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 6),
    _TmnxMobPdnGaStatRxEchoRequests_Type()
)
tmnxMobPdnGaStatRxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxEchoRequests.setStatus("current")
_TmnxMobPdnGaStatTxEchoResponses_Type = Counter32
_TmnxMobPdnGaStatTxEchoResponses_Object = MibTableColumn
tmnxMobPdnGaStatTxEchoResponses = _TmnxMobPdnGaStatTxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 7),
    _TmnxMobPdnGaStatTxEchoResponses_Type()
)
tmnxMobPdnGaStatTxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxEchoResponses.setStatus("current")
_TmnxMobPdnGaStatTxEchoRequests_Type = Counter32
_TmnxMobPdnGaStatTxEchoRequests_Object = MibTableColumn
tmnxMobPdnGaStatTxEchoRequests = _TmnxMobPdnGaStatTxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 8),
    _TmnxMobPdnGaStatTxEchoRequests_Type()
)
tmnxMobPdnGaStatTxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxEchoRequests.setStatus("current")
_TmnxMobPdnGaStatRxEchoResponses_Type = Counter32
_TmnxMobPdnGaStatRxEchoResponses_Object = MibTableColumn
tmnxMobPdnGaStatRxEchoResponses = _TmnxMobPdnGaStatRxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 9),
    _TmnxMobPdnGaStatRxEchoResponses_Type()
)
tmnxMobPdnGaStatRxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxEchoResponses.setStatus("current")
_TmnxMobPdnGaStatRxNodeAlRequests_Type = Counter32
_TmnxMobPdnGaStatRxNodeAlRequests_Object = MibTableColumn
tmnxMobPdnGaStatRxNodeAlRequests = _TmnxMobPdnGaStatRxNodeAlRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 10),
    _TmnxMobPdnGaStatRxNodeAlRequests_Type()
)
tmnxMobPdnGaStatRxNodeAlRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxNodeAlRequests.setStatus("current")
_TmnxMobPdnGaStatTxNodeAlResps_Type = Counter32
_TmnxMobPdnGaStatTxNodeAlResps_Object = MibTableColumn
tmnxMobPdnGaStatTxNodeAlResps = _TmnxMobPdnGaStatTxNodeAlResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 11),
    _TmnxMobPdnGaStatTxNodeAlResps_Type()
)
tmnxMobPdnGaStatTxNodeAlResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxNodeAlResps.setStatus("current")
_TmnxMobPdnGaStatTxDataRecReqs_Type = Counter32
_TmnxMobPdnGaStatTxDataRecReqs_Object = MibTableColumn
tmnxMobPdnGaStatTxDataRecReqs = _TmnxMobPdnGaStatTxDataRecReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 12),
    _TmnxMobPdnGaStatTxDataRecReqs_Type()
)
tmnxMobPdnGaStatTxDataRecReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxDataRecReqs.setStatus("current")
_TmnxMobPdnGaStatTxDataRecTferReq_Type = Counter32
_TmnxMobPdnGaStatTxDataRecTferReq_Object = MibTableColumn
tmnxMobPdnGaStatTxDataRecTferReq = _TmnxMobPdnGaStatTxDataRecTferReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 13),
    _TmnxMobPdnGaStatTxDataRecTferReq_Type()
)
tmnxMobPdnGaStatTxDataRecTferReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxDataRecTferReq.setStatus("current")
_TmnxMobPdnGaStatRetrDataRecReqs_Type = Counter32
_TmnxMobPdnGaStatRetrDataRecReqs_Object = MibTableColumn
tmnxMobPdnGaStatRetrDataRecReqs = _TmnxMobPdnGaStatRetrDataRecReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 14),
    _TmnxMobPdnGaStatRetrDataRecReqs_Type()
)
tmnxMobPdnGaStatRetrDataRecReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRetrDataRecReqs.setStatus("current")
_TmnxMobPdnGaStatRxDataRecReqs_Type = Counter32
_TmnxMobPdnGaStatRxDataRecReqs_Object = MibTableColumn
tmnxMobPdnGaStatRxDataRecReqs = _TmnxMobPdnGaStatRxDataRecReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 15),
    _TmnxMobPdnGaStatRxDataRecReqs_Type()
)
tmnxMobPdnGaStatRxDataRecReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxDataRecReqs.setStatus("current")
_TmnxMobPdnGaStatUnackDataRexReqs_Type = Counter32
_TmnxMobPdnGaStatUnackDataRexReqs_Object = MibTableColumn
tmnxMobPdnGaStatUnackDataRexReqs = _TmnxMobPdnGaStatUnackDataRexReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 16),
    _TmnxMobPdnGaStatUnackDataRexReqs_Type()
)
tmnxMobPdnGaStatUnackDataRexReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatUnackDataRexReqs.setStatus("current")
_TmnxMobPdnGaStatRxRedirectionReq_Type = Counter32
_TmnxMobPdnGaStatRxRedirectionReq_Object = MibTableColumn
tmnxMobPdnGaStatRxRedirectionReq = _TmnxMobPdnGaStatRxRedirectionReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 17),
    _TmnxMobPdnGaStatRxRedirectionReq_Type()
)
tmnxMobPdnGaStatRxRedirectionReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxRedirectionReq.setStatus("current")
_TmnxMobPdnGaStatTxRedrnResp_Type = Counter32
_TmnxMobPdnGaStatTxRedrnResp_Object = MibTableColumn
tmnxMobPdnGaStatTxRedrnResp = _TmnxMobPdnGaStatTxRedrnResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 18),
    _TmnxMobPdnGaStatTxRedrnResp_Type()
)
tmnxMobPdnGaStatTxRedrnResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxRedrnResp.setStatus("current")
_TmnxMobPdnGaStatRxInvalidMsgs_Type = Counter32
_TmnxMobPdnGaStatRxInvalidMsgs_Object = MibTableColumn
tmnxMobPdnGaStatRxInvalidMsgs = _TmnxMobPdnGaStatRxInvalidMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 19),
    _TmnxMobPdnGaStatRxInvalidMsgs_Type()
)
tmnxMobPdnGaStatRxInvalidMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxInvalidMsgs.setStatus("current")
_TmnxMobPdnGaStatRxVerNotSupp_Type = Counter32
_TmnxMobPdnGaStatRxVerNotSupp_Object = MibTableColumn
tmnxMobPdnGaStatRxVerNotSupp = _TmnxMobPdnGaStatRxVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 20),
    _TmnxMobPdnGaStatRxVerNotSupp_Type()
)
tmnxMobPdnGaStatRxVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxVerNotSupp.setStatus("current")
_TmnxMobPdnGaStatTxCdrTermination_Type = Counter32
_TmnxMobPdnGaStatTxCdrTermination_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrTermination = _TmnxMobPdnGaStatTxCdrTermination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 21),
    _TmnxMobPdnGaStatTxCdrTermination_Type()
)
tmnxMobPdnGaStatTxCdrTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrTermination.setStatus("current")
_TmnxMobPdnGaStatTxCdrMaxChngCond_Type = Counter32
_TmnxMobPdnGaStatTxCdrMaxChngCond_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrMaxChngCond = _TmnxMobPdnGaStatTxCdrMaxChngCond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 22),
    _TmnxMobPdnGaStatTxCdrMaxChngCond_Type()
)
tmnxMobPdnGaStatTxCdrMaxChngCond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrMaxChngCond.setStatus("current")
_TmnxMobPdnGaStatTxCdrMsTmzChng_Type = Counter32
_TmnxMobPdnGaStatTxCdrMsTmzChng_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrMsTmzChng = _TmnxMobPdnGaStatTxCdrMsTmzChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 23),
    _TmnxMobPdnGaStatTxCdrMsTmzChng_Type()
)
tmnxMobPdnGaStatTxCdrMsTmzChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrMsTmzChng.setStatus("current")
_TmnxMobPdnGaStatTxCdrRatChng_Type = Counter32
_TmnxMobPdnGaStatTxCdrRatChng_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrRatChng = _TmnxMobPdnGaStatTxCdrRatChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 24),
    _TmnxMobPdnGaStatTxCdrRatChng_Type()
)
tmnxMobPdnGaStatTxCdrRatChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrRatChng.setStatus("current")
_TmnxMobPdnGaStatTxCdrTimeLimit_Type = Counter32
_TmnxMobPdnGaStatTxCdrTimeLimit_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrTimeLimit = _TmnxMobPdnGaStatTxCdrTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 25),
    _TmnxMobPdnGaStatTxCdrTimeLimit_Type()
)
tmnxMobPdnGaStatTxCdrTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrTimeLimit.setStatus("current")
_TmnxMobPdnGaStatTxCdrVolLimit_Type = Counter32
_TmnxMobPdnGaStatTxCdrVolLimit_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrVolLimit = _TmnxMobPdnGaStatTxCdrVolLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 26),
    _TmnxMobPdnGaStatTxCdrVolLimit_Type()
)
tmnxMobPdnGaStatTxCdrVolLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrVolLimit.setStatus("current")
_TmnxMobPdnGaStatRxCdrReqAcc_Type = Counter32
_TmnxMobPdnGaStatRxCdrReqAcc_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrReqAcc = _TmnxMobPdnGaStatRxCdrReqAcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 27),
    _TmnxMobPdnGaStatRxCdrReqAcc_Type()
)
tmnxMobPdnGaStatRxCdrReqAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrReqAcc.setStatus("current")
_TmnxMobPdnGaStatRxCdrNoResAva_Type = Counter32
_TmnxMobPdnGaStatRxCdrNoResAva_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrNoResAva = _TmnxMobPdnGaStatRxCdrNoResAva_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 28),
    _TmnxMobPdnGaStatRxCdrNoResAva_Type()
)
tmnxMobPdnGaStatRxCdrNoResAva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrNoResAva.setStatus("current")
_TmnxMobPdnGaStatRxCdrReqNotFf_Type = Counter32
_TmnxMobPdnGaStatRxCdrReqNotFf_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrReqNotFf = _TmnxMobPdnGaStatRxCdrReqNotFf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 29),
    _TmnxMobPdnGaStatRxCdrReqNotFf_Type()
)
tmnxMobPdnGaStatRxCdrReqNotFf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrReqNotFf.setStatus("current")
_TmnxMobPdnGaStatRxCdrReqFfilled_Type = Counter32
_TmnxMobPdnGaStatRxCdrReqFfilled_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrReqFfilled = _TmnxMobPdnGaStatRxCdrReqFfilled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 30),
    _TmnxMobPdnGaStatRxCdrReqFfilled_Type()
)
tmnxMobPdnGaStatRxCdrReqFfilled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrReqFfilled.setStatus("current")
_TmnxMobPdnGaStatRxCdrDupReqFf_Type = Counter32
_TmnxMobPdnGaStatRxCdrDupReqFf_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrDupReqFf = _TmnxMobPdnGaStatRxCdrDupReqFf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 31),
    _TmnxMobPdnGaStatRxCdrDupReqFf_Type()
)
tmnxMobPdnGaStatRxCdrDupReqFf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrDupReqFf.setStatus("current")
_TmnxMobPdnGaStatRxCdrInvMsgFmat_Type = Counter32
_TmnxMobPdnGaStatRxCdrInvMsgFmat_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrInvMsgFmat = _TmnxMobPdnGaStatRxCdrInvMsgFmat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 32),
    _TmnxMobPdnGaStatRxCdrInvMsgFmat_Type()
)
tmnxMobPdnGaStatRxCdrInvMsgFmat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrInvMsgFmat.setStatus("current")
_TmnxMobPdnGaStatRxCdrVerNotSupp_Type = Counter32
_TmnxMobPdnGaStatRxCdrVerNotSupp_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrVerNotSupp = _TmnxMobPdnGaStatRxCdrVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 33),
    _TmnxMobPdnGaStatRxCdrVerNotSupp_Type()
)
tmnxMobPdnGaStatRxCdrVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrVerNotSupp.setStatus("current")
_TmnxMobPdnGaStatRxCdrSrvcNotSupp_Type = Counter32
_TmnxMobPdnGaStatRxCdrSrvcNotSupp_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrSrvcNotSupp = _TmnxMobPdnGaStatRxCdrSrvcNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 34),
    _TmnxMobPdnGaStatRxCdrSrvcNotSupp_Type()
)
tmnxMobPdnGaStatRxCdrSrvcNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrSrvcNotSupp.setStatus("current")
_TmnxMobPdnGaStatRxCdrMandIeInc_Type = Counter32
_TmnxMobPdnGaStatRxCdrMandIeInc_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrMandIeInc = _TmnxMobPdnGaStatRxCdrMandIeInc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 35),
    _TmnxMobPdnGaStatRxCdrMandIeInc_Type()
)
tmnxMobPdnGaStatRxCdrMandIeInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrMandIeInc.setStatus("current")
_TmnxMobPdnGaStatRxCdrMandIeMiss_Type = Counter32
_TmnxMobPdnGaStatRxCdrMandIeMiss_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrMandIeMiss = _TmnxMobPdnGaStatRxCdrMandIeMiss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 36),
    _TmnxMobPdnGaStatRxCdrMandIeMiss_Type()
)
tmnxMobPdnGaStatRxCdrMandIeMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrMandIeMiss.setStatus("current")
_TmnxMobPdnGaStatRxCdrOptIeInc_Type = Counter32
_TmnxMobPdnGaStatRxCdrOptIeInc_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrOptIeInc = _TmnxMobPdnGaStatRxCdrOptIeInc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 37),
    _TmnxMobPdnGaStatRxCdrOptIeInc_Type()
)
tmnxMobPdnGaStatRxCdrOptIeInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrOptIeInc.setStatus("current")
_TmnxMobPdnGaStatRxCdrSystemFail_Type = Counter32
_TmnxMobPdnGaStatRxCdrSystemFail_Object = MibTableColumn
tmnxMobPdnGaStatRxCdrSystemFail = _TmnxMobPdnGaStatRxCdrSystemFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 38),
    _TmnxMobPdnGaStatRxCdrSystemFail_Type()
)
tmnxMobPdnGaStatRxCdrSystemFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxCdrSystemFail.setStatus("current")
_TmnxMobPdnGaStatRtrEchoRequests_Type = Counter32
_TmnxMobPdnGaStatRtrEchoRequests_Object = MibTableColumn
tmnxMobPdnGaStatRtrEchoRequests = _TmnxMobPdnGaStatRtrEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 39),
    _TmnxMobPdnGaStatRtrEchoRequests_Type()
)
tmnxMobPdnGaStatRtrEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRtrEchoRequests.setStatus("current")
_TmnxMobPdnGaStatGtpPrimeFail_Type = Counter32
_TmnxMobPdnGaStatGtpPrimeFail_Object = MibTableColumn
tmnxMobPdnGaStatGtpPrimeFail = _TmnxMobPdnGaStatGtpPrimeFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 40),
    _TmnxMobPdnGaStatGtpPrimeFail_Type()
)
tmnxMobPdnGaStatGtpPrimeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatGtpPrimeFail.setStatus("current")


class _TmnxMobPdnGaStatOperState_Type(Integer32):
    """Custom type tmnxMobPdnGaStatOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("active", 3))
    )


_TmnxMobPdnGaStatOperState_Type.__name__ = "Integer32"
_TmnxMobPdnGaStatOperState_Object = MibTableColumn
tmnxMobPdnGaStatOperState = _TmnxMobPdnGaStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 41),
    _TmnxMobPdnGaStatOperState_Type()
)
tmnxMobPdnGaStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatOperState.setStatus("current")
_TmnxMobPdnGaStatUpTime_Type = TimeStamp
_TmnxMobPdnGaStatUpTime_Object = MibTableColumn
tmnxMobPdnGaStatUpTime = _TmnxMobPdnGaStatUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 42),
    _TmnxMobPdnGaStatUpTime_Type()
)
tmnxMobPdnGaStatUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatUpTime.setStatus("current")
_TmnxMobPdnGaStatTxNodeAlRequests_Type = Counter32
_TmnxMobPdnGaStatTxNodeAlRequests_Object = MibTableColumn
tmnxMobPdnGaStatTxNodeAlRequests = _TmnxMobPdnGaStatTxNodeAlRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 43),
    _TmnxMobPdnGaStatTxNodeAlRequests_Type()
)
tmnxMobPdnGaStatTxNodeAlRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxNodeAlRequests.setStatus("current")
_TmnxMobPdnGaStatRxNodeAlResps_Type = Counter32
_TmnxMobPdnGaStatRxNodeAlResps_Object = MibTableColumn
tmnxMobPdnGaStatRxNodeAlResps = _TmnxMobPdnGaStatRxNodeAlResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 44),
    _TmnxMobPdnGaStatRxNodeAlResps_Type()
)
tmnxMobPdnGaStatRxNodeAlResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatRxNodeAlResps.setStatus("current")
_TmnxMobPdnGaStatNodeAlReqRetried_Type = Counter32
_TmnxMobPdnGaStatNodeAlReqRetried_Object = MibTableColumn
tmnxMobPdnGaStatNodeAlReqRetried = _TmnxMobPdnGaStatNodeAlReqRetried_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 45),
    _TmnxMobPdnGaStatNodeAlReqRetried_Type()
)
tmnxMobPdnGaStatNodeAlReqRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatNodeAlReqRetried.setStatus("current")
_TmnxMobPdnGaStatCdrsTx_Type = Counter32
_TmnxMobPdnGaStatCdrsTx_Object = MibTableColumn
tmnxMobPdnGaStatCdrsTx = _TmnxMobPdnGaStatCdrsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 46),
    _TmnxMobPdnGaStatCdrsTx_Type()
)
tmnxMobPdnGaStatCdrsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatCdrsTx.setStatus("current")
_TmnxMobPdnGaStatCdrsRx_Type = Counter32
_TmnxMobPdnGaStatCdrsRx_Object = MibTableColumn
tmnxMobPdnGaStatCdrsRx = _TmnxMobPdnGaStatCdrsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 47),
    _TmnxMobPdnGaStatCdrsRx_Type()
)
tmnxMobPdnGaStatCdrsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatCdrsRx.setStatus("current")
_TmnxMobPdnGaStatTxCdrPlmnChange_Type = Counter32
_TmnxMobPdnGaStatTxCdrPlmnChange_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrPlmnChange = _TmnxMobPdnGaStatTxCdrPlmnChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 48),
    _TmnxMobPdnGaStatTxCdrPlmnChange_Type()
)
tmnxMobPdnGaStatTxCdrPlmnChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrPlmnChange.setStatus("current")
_TmnxMobPdnGaStatTxCdrSerNdChLmt_Type = Counter32
_TmnxMobPdnGaStatTxCdrSerNdChLmt_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrSerNdChLmt = _TmnxMobPdnGaStatTxCdrSerNdChLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 49),
    _TmnxMobPdnGaStatTxCdrSerNdChLmt_Type()
)
tmnxMobPdnGaStatTxCdrSerNdChLmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrSerNdChLmt.setStatus("current")
_TmnxMobPdnGaStatTxVerNotSupp_Type = Counter32
_TmnxMobPdnGaStatTxVerNotSupp_Object = MibTableColumn
tmnxMobPdnGaStatTxVerNotSupp = _TmnxMobPdnGaStatTxVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 50),
    _TmnxMobPdnGaStatTxVerNotSupp_Type()
)
tmnxMobPdnGaStatTxVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxVerNotSupp.setStatus("current")
_TmnxMobPdnGaStatTxCdrMgmtInterv_Type = Counter32
_TmnxMobPdnGaStatTxCdrMgmtInterv_Object = MibTableColumn
tmnxMobPdnGaStatTxCdrMgmtInterv = _TmnxMobPdnGaStatTxCdrMgmtInterv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 11, 1, 51),
    _TmnxMobPdnGaStatTxCdrMgmtInterv_Type()
)
tmnxMobPdnGaStatTxCdrMgmtInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaStatTxCdrMgmtInterv.setStatus("current")
_TmnxMobPdnGyPeerTable_Object = MibTable
tmnxMobPdnGyPeerTable = _TmnxMobPdnGyPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerTable.setStatus("current")
_TmnxMobPdnGyPeerEntry_Object = MibTableRow
tmnxMobPdnGyPeerEntry = _TmnxMobPdnGyPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12, 1)
)
tmnxMobPdnGyPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerEntry.setStatus("current")
_TmnxMobPdnGyPeerAddressType_Type = InetAddressType
_TmnxMobPdnGyPeerAddressType_Object = MibTableColumn
tmnxMobPdnGyPeerAddressType = _TmnxMobPdnGyPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12, 1, 1),
    _TmnxMobPdnGyPeerAddressType_Type()
)
tmnxMobPdnGyPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerAddressType.setStatus("current")


class _TmnxMobPdnGyPeerAddress_Type(InetAddress):
    """Custom type tmnxMobPdnGyPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnGyPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnGyPeerAddress_Object = MibTableColumn
tmnxMobPdnGyPeerAddress = _TmnxMobPdnGyPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12, 1, 2),
    _TmnxMobPdnGyPeerAddress_Type()
)
tmnxMobPdnGyPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerAddress.setStatus("current")
_TmnxMobPdnGyPeerPort_Type = InetPortNumber
_TmnxMobPdnGyPeerPort_Object = MibTableColumn
tmnxMobPdnGyPeerPort = _TmnxMobPdnGyPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12, 1, 3),
    _TmnxMobPdnGyPeerPort_Type()
)
tmnxMobPdnGyPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerPort.setStatus("current")
_TmnxMobPdnGyPeerLastChanged_Type = TimeStamp
_TmnxMobPdnGyPeerLastChanged_Object = MibTableColumn
tmnxMobPdnGyPeerLastChanged = _TmnxMobPdnGyPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12, 1, 4),
    _TmnxMobPdnGyPeerLastChanged_Type()
)
tmnxMobPdnGyPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerLastChanged.setStatus("current")
_TmnxMobPdnGyPeerCreateTime_Type = TimeStamp
_TmnxMobPdnGyPeerCreateTime_Object = MibTableColumn
tmnxMobPdnGyPeerCreateTime = _TmnxMobPdnGyPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12, 1, 5),
    _TmnxMobPdnGyPeerCreateTime_Type()
)
tmnxMobPdnGyPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerCreateTime.setStatus("current")
_TmnxMobPdnGyPeerPathMgmtState_Type = TmnxMobDiaPathMgmtState
_TmnxMobPdnGyPeerPathMgmtState_Object = MibTableColumn
tmnxMobPdnGyPeerPathMgmtState = _TmnxMobPdnGyPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12, 1, 6),
    _TmnxMobPdnGyPeerPathMgmtState_Type()
)
tmnxMobPdnGyPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerPathMgmtState.setStatus("current")
_TmnxMobPdnGyPeerDetailState_Type = TmnxMobDiaDetailPathMgmtState
_TmnxMobPdnGyPeerDetailState_Object = MibTableColumn
tmnxMobPdnGyPeerDetailState = _TmnxMobPdnGyPeerDetailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 12, 1, 7),
    _TmnxMobPdnGyPeerDetailState_Type()
)
tmnxMobPdnGyPeerDetailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerDetailState.setStatus("current")
_TmnxMobPdnGyStatTable_Object = MibTable
tmnxMobPdnGyStatTable = _TmnxMobPdnGyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatTable.setStatus("current")
_TmnxMobPdnGyStatEntry_Object = MibTableRow
tmnxMobPdnGyStatEntry = _TmnxMobPdnGyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1)
)
tmnxMobPdnGyStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatEntry.setStatus("current")
_TmnxMobPdnGyStatCcrGranted_Type = Counter32
_TmnxMobPdnGyStatCcrGranted_Object = MibTableColumn
tmnxMobPdnGyStatCcrGranted = _TmnxMobPdnGyStatCcrGranted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 1),
    _TmnxMobPdnGyStatCcrGranted_Type()
)
tmnxMobPdnGyStatCcrGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcrGranted.setStatus("current")
_TmnxMobPdnGyStatCcrDenied_Type = Counter32
_TmnxMobPdnGyStatCcrDenied_Object = MibTableColumn
tmnxMobPdnGyStatCcrDenied = _TmnxMobPdnGyStatCcrDenied_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 2),
    _TmnxMobPdnGyStatCcrDenied_Type()
)
tmnxMobPdnGyStatCcrDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcrDenied.setStatus("current")
_TmnxMobPdnGyStatCcrInitialMsgTx_Type = Counter32
_TmnxMobPdnGyStatCcrInitialMsgTx_Object = MibTableColumn
tmnxMobPdnGyStatCcrInitialMsgTx = _TmnxMobPdnGyStatCcrInitialMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 3),
    _TmnxMobPdnGyStatCcrInitialMsgTx_Type()
)
tmnxMobPdnGyStatCcrInitialMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcrInitialMsgTx.setStatus("current")
_TmnxMobPdnGyStatCcrUpdateMsgTx_Type = Counter32
_TmnxMobPdnGyStatCcrUpdateMsgTx_Object = MibTableColumn
tmnxMobPdnGyStatCcrUpdateMsgTx = _TmnxMobPdnGyStatCcrUpdateMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 4),
    _TmnxMobPdnGyStatCcrUpdateMsgTx_Type()
)
tmnxMobPdnGyStatCcrUpdateMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcrUpdateMsgTx.setStatus("current")
_TmnxMobPdnGyStatCcrTermMsgTx_Type = Counter32
_TmnxMobPdnGyStatCcrTermMsgTx_Object = MibTableColumn
tmnxMobPdnGyStatCcrTermMsgTx = _TmnxMobPdnGyStatCcrTermMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 5),
    _TmnxMobPdnGyStatCcrTermMsgTx_Type()
)
tmnxMobPdnGyStatCcrTermMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcrTermMsgTx.setStatus("current")
_TmnxMobPdnGyStatCcaInitialMsgRx_Type = Counter32
_TmnxMobPdnGyStatCcaInitialMsgRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaInitialMsgRx = _TmnxMobPdnGyStatCcaInitialMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 6),
    _TmnxMobPdnGyStatCcaInitialMsgRx_Type()
)
tmnxMobPdnGyStatCcaInitialMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaInitialMsgRx.setStatus("current")
_TmnxMobPdnGyStatCcaUpdateMsgRx_Type = Counter32
_TmnxMobPdnGyStatCcaUpdateMsgRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaUpdateMsgRx = _TmnxMobPdnGyStatCcaUpdateMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 7),
    _TmnxMobPdnGyStatCcaUpdateMsgRx_Type()
)
tmnxMobPdnGyStatCcaUpdateMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaUpdateMsgRx.setStatus("current")
_TmnxMobPdnGyStatCcaTermMsgRx_Type = Counter32
_TmnxMobPdnGyStatCcaTermMsgRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaTermMsgRx = _TmnxMobPdnGyStatCcaTermMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 8),
    _TmnxMobPdnGyStatCcaTermMsgRx_Type()
)
tmnxMobPdnGyStatCcaTermMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaTermMsgRx.setStatus("current")
_TmnxMobPdnGyStatCcrInitMsgFails_Type = Counter32
_TmnxMobPdnGyStatCcrInitMsgFails_Object = MibTableColumn
tmnxMobPdnGyStatCcrInitMsgFails = _TmnxMobPdnGyStatCcrInitMsgFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 9),
    _TmnxMobPdnGyStatCcrInitMsgFails_Type()
)
tmnxMobPdnGyStatCcrInitMsgFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcrInitMsgFails.setStatus("current")
_TmnxMobPdnGyStatCcrUpdMsgFails_Type = Counter32
_TmnxMobPdnGyStatCcrUpdMsgFails_Object = MibTableColumn
tmnxMobPdnGyStatCcrUpdMsgFails = _TmnxMobPdnGyStatCcrUpdMsgFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 10),
    _TmnxMobPdnGyStatCcrUpdMsgFails_Type()
)
tmnxMobPdnGyStatCcrUpdMsgFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcrUpdMsgFails.setStatus("current")
_TmnxMobPdnGyStatCcrTermMsgFails_Type = Counter32
_TmnxMobPdnGyStatCcrTermMsgFails_Object = MibTableColumn
tmnxMobPdnGyStatCcrTermMsgFails = _TmnxMobPdnGyStatCcrTermMsgFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 11),
    _TmnxMobPdnGyStatCcrTermMsgFails_Type()
)
tmnxMobPdnGyStatCcrTermMsgFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcrTermMsgFails.setStatus("current")
_TmnxMobPdnGyStatAsrMsgRx_Type = Counter32
_TmnxMobPdnGyStatAsrMsgRx_Object = MibTableColumn
tmnxMobPdnGyStatAsrMsgRx = _TmnxMobPdnGyStatAsrMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 12),
    _TmnxMobPdnGyStatAsrMsgRx_Type()
)
tmnxMobPdnGyStatAsrMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatAsrMsgRx.setStatus("current")
_TmnxMobPdnGyStatAsaMsgTx_Type = Counter32
_TmnxMobPdnGyStatAsaMsgTx_Object = MibTableColumn
tmnxMobPdnGyStatAsaMsgTx = _TmnxMobPdnGyStatAsaMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 13),
    _TmnxMobPdnGyStatAsaMsgTx_Type()
)
tmnxMobPdnGyStatAsaMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatAsaMsgTx.setStatus("current")
_TmnxMobPdnGyStatAsaNackMsgTx_Type = Counter32
_TmnxMobPdnGyStatAsaNackMsgTx_Object = MibTableColumn
tmnxMobPdnGyStatAsaNackMsgTx = _TmnxMobPdnGyStatAsaNackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 14),
    _TmnxMobPdnGyStatAsaNackMsgTx_Type()
)
tmnxMobPdnGyStatAsaNackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatAsaNackMsgTx.setStatus("current")
_TmnxMobPdnGyStatRarMsgRx_Type = Counter32
_TmnxMobPdnGyStatRarMsgRx_Object = MibTableColumn
tmnxMobPdnGyStatRarMsgRx = _TmnxMobPdnGyStatRarMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 15),
    _TmnxMobPdnGyStatRarMsgRx_Type()
)
tmnxMobPdnGyStatRarMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRarMsgRx.setStatus("current")
_TmnxMobPdnGyStatRaaMsgTx_Type = Counter32
_TmnxMobPdnGyStatRaaMsgTx_Object = MibTableColumn
tmnxMobPdnGyStatRaaMsgTx = _TmnxMobPdnGyStatRaaMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 16),
    _TmnxMobPdnGyStatRaaMsgTx_Type()
)
tmnxMobPdnGyStatRaaMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRaaMsgTx.setStatus("current")
_TmnxMobPdnGyStatRaaNackMsgTx_Type = Counter32
_TmnxMobPdnGyStatRaaNackMsgTx_Object = MibTableColumn
tmnxMobPdnGyStatRaaNackMsgTx = _TmnxMobPdnGyStatRaaNackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 17),
    _TmnxMobPdnGyStatRaaNackMsgTx_Type()
)
tmnxMobPdnGyStatRaaNackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRaaNackMsgTx.setStatus("current")
_TmnxMobPdnGyStatMalformedPktsRx_Type = Counter32
_TmnxMobPdnGyStatMalformedPktsRx_Object = MibTableColumn
tmnxMobPdnGyStatMalformedPktsRx = _TmnxMobPdnGyStatMalformedPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 18),
    _TmnxMobPdnGyStatMalformedPktsRx_Type()
)
tmnxMobPdnGyStatMalformedPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatMalformedPktsRx.setStatus("current")
_TmnxMobPdnGyStatCCAInitMalfPktRx_Type = Counter32
_TmnxMobPdnGyStatCCAInitMalfPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCCAInitMalfPktRx = _TmnxMobPdnGyStatCCAInitMalfPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 19),
    _TmnxMobPdnGyStatCCAInitMalfPktRx_Type()
)
tmnxMobPdnGyStatCCAInitMalfPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCCAInitMalfPktRx.setStatus("current")
_TmnxMobPdnGyStatCCAUpdtMalfPktRx_Type = Counter32
_TmnxMobPdnGyStatCCAUpdtMalfPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCCAUpdtMalfPktRx = _TmnxMobPdnGyStatCCAUpdtMalfPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 20),
    _TmnxMobPdnGyStatCCAUpdtMalfPktRx_Type()
)
tmnxMobPdnGyStatCCAUpdtMalfPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCCAUpdtMalfPktRx.setStatus("current")
_TmnxMobPdnGyStatCCATermMalfPktRx_Type = Counter32
_TmnxMobPdnGyStatCCATermMalfPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCCATermMalfPktRx = _TmnxMobPdnGyStatCCATermMalfPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 21),
    _TmnxMobPdnGyStatCCATermMalfPktRx_Type()
)
tmnxMobPdnGyStatCCATermMalfPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCCATermMalfPktRx.setStatus("current")
_TmnxMobPdnGyStatRarMalfPktRx_Type = Counter32
_TmnxMobPdnGyStatRarMalfPktRx_Object = MibTableColumn
tmnxMobPdnGyStatRarMalfPktRx = _TmnxMobPdnGyStatRarMalfPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 22),
    _TmnxMobPdnGyStatRarMalfPktRx_Type()
)
tmnxMobPdnGyStatRarMalfPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRarMalfPktRx.setStatus("current")
_TmnxMobPdnGyStatAsrMalfPktRx_Type = Counter32
_TmnxMobPdnGyStatAsrMalfPktRx_Object = MibTableColumn
tmnxMobPdnGyStatAsrMalfPktRx = _TmnxMobPdnGyStatAsrMalfPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 23),
    _TmnxMobPdnGyStatAsrMalfPktRx_Type()
)
tmnxMobPdnGyStatAsrMalfPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatAsrMalfPktRx.setStatus("current")
_TmnxMobPdnGyStatUnkwnPktsRx_Type = Counter32
_TmnxMobPdnGyStatUnkwnPktsRx_Object = MibTableColumn
tmnxMobPdnGyStatUnkwnPktsRx = _TmnxMobPdnGyStatUnkwnPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 24),
    _TmnxMobPdnGyStatUnkwnPktsRx_Type()
)
tmnxMobPdnGyStatUnkwnPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatUnkwnPktsRx.setStatus("current")
_TmnxMobPdnGyStatCcaInitUnkPktRx_Type = Counter32
_TmnxMobPdnGyStatCcaInitUnkPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaInitUnkPktRx = _TmnxMobPdnGyStatCcaInitUnkPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 25),
    _TmnxMobPdnGyStatCcaInitUnkPktRx_Type()
)
tmnxMobPdnGyStatCcaInitUnkPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaInitUnkPktRx.setStatus("current")
_TmnxMobPdnGyStatCcaUpdUnkPktRx_Type = Counter32
_TmnxMobPdnGyStatCcaUpdUnkPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaUpdUnkPktRx = _TmnxMobPdnGyStatCcaUpdUnkPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 26),
    _TmnxMobPdnGyStatCcaUpdUnkPktRx_Type()
)
tmnxMobPdnGyStatCcaUpdUnkPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaUpdUnkPktRx.setStatus("current")
_TmnxMobPdnGyStatCcaTermUnkPktRx_Type = Counter32
_TmnxMobPdnGyStatCcaTermUnkPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaTermUnkPktRx = _TmnxMobPdnGyStatCcaTermUnkPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 27),
    _TmnxMobPdnGyStatCcaTermUnkPktRx_Type()
)
tmnxMobPdnGyStatCcaTermUnkPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaTermUnkPktRx.setStatus("current")
_TmnxMobPdnGyStatRarUnkPktRx_Type = Counter32
_TmnxMobPdnGyStatRarUnkPktRx_Object = MibTableColumn
tmnxMobPdnGyStatRarUnkPktRx = _TmnxMobPdnGyStatRarUnkPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 28),
    _TmnxMobPdnGyStatRarUnkPktRx_Type()
)
tmnxMobPdnGyStatRarUnkPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRarUnkPktRx.setStatus("current")
_TmnxMobPdnGyStatAsrUnkPktRx_Type = Counter32
_TmnxMobPdnGyStatAsrUnkPktRx_Object = MibTableColumn
tmnxMobPdnGyStatAsrUnkPktRx = _TmnxMobPdnGyStatAsrUnkPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 29),
    _TmnxMobPdnGyStatAsrUnkPktRx_Type()
)
tmnxMobPdnGyStatAsrUnkPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatAsrUnkPktRx.setStatus("current")
_TmnxMobPdnGyStatMissingAvpPktRx_Type = Counter32
_TmnxMobPdnGyStatMissingAvpPktRx_Object = MibTableColumn
tmnxMobPdnGyStatMissingAvpPktRx = _TmnxMobPdnGyStatMissingAvpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 30),
    _TmnxMobPdnGyStatMissingAvpPktRx_Type()
)
tmnxMobPdnGyStatMissingAvpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatMissingAvpPktRx.setStatus("current")
_TmnxMobPdnGyStatCcaIMisAvpPktRx_Type = Counter32
_TmnxMobPdnGyStatCcaIMisAvpPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaIMisAvpPktRx = _TmnxMobPdnGyStatCcaIMisAvpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 31),
    _TmnxMobPdnGyStatCcaIMisAvpPktRx_Type()
)
tmnxMobPdnGyStatCcaIMisAvpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaIMisAvpPktRx.setStatus("current")
_TmnxMobPdnGyStatCcaUMisAvpPktRx_Type = Counter32
_TmnxMobPdnGyStatCcaUMisAvpPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaUMisAvpPktRx = _TmnxMobPdnGyStatCcaUMisAvpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 32),
    _TmnxMobPdnGyStatCcaUMisAvpPktRx_Type()
)
tmnxMobPdnGyStatCcaUMisAvpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaUMisAvpPktRx.setStatus("current")
_TmnxMobPdnGyStatCcaTMisAvpPktRx_Type = Counter32
_TmnxMobPdnGyStatCcaTMisAvpPktRx_Object = MibTableColumn
tmnxMobPdnGyStatCcaTMisAvpPktRx = _TmnxMobPdnGyStatCcaTMisAvpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 33),
    _TmnxMobPdnGyStatCcaTMisAvpPktRx_Type()
)
tmnxMobPdnGyStatCcaTMisAvpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaTMisAvpPktRx.setStatus("current")
_TmnxMobPdnGyStatRarMisAvpPktRx_Type = Counter32
_TmnxMobPdnGyStatRarMisAvpPktRx_Object = MibTableColumn
tmnxMobPdnGyStatRarMisAvpPktRx = _TmnxMobPdnGyStatRarMisAvpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 34),
    _TmnxMobPdnGyStatRarMisAvpPktRx_Type()
)
tmnxMobPdnGyStatRarMisAvpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRarMisAvpPktRx.setStatus("current")
_TmnxMobPdnGyStatAsrMisAvpPktRx_Type = Counter32
_TmnxMobPdnGyStatAsrMisAvpPktRx_Object = MibTableColumn
tmnxMobPdnGyStatAsrMisAvpPktRx = _TmnxMobPdnGyStatAsrMisAvpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 35),
    _TmnxMobPdnGyStatAsrMisAvpPktRx_Type()
)
tmnxMobPdnGyStatAsrMisAvpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatAsrMisAvpPktRx.setStatus("current")
_TmnxMobPdnGyStatCcaIUnkSessPkts_Type = Counter32
_TmnxMobPdnGyStatCcaIUnkSessPkts_Object = MibTableColumn
tmnxMobPdnGyStatCcaIUnkSessPkts = _TmnxMobPdnGyStatCcaIUnkSessPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 36),
    _TmnxMobPdnGyStatCcaIUnkSessPkts_Type()
)
tmnxMobPdnGyStatCcaIUnkSessPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaIUnkSessPkts.setStatus("current")
_TmnxMobPdnGyStatCcaUUnkSessPkts_Type = Counter32
_TmnxMobPdnGyStatCcaUUnkSessPkts_Object = MibTableColumn
tmnxMobPdnGyStatCcaUUnkSessPkts = _TmnxMobPdnGyStatCcaUUnkSessPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 37),
    _TmnxMobPdnGyStatCcaUUnkSessPkts_Type()
)
tmnxMobPdnGyStatCcaUUnkSessPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaUUnkSessPkts.setStatus("current")
_TmnxMobPdnGyStatCcaTUnkSessPkts_Type = Counter32
_TmnxMobPdnGyStatCcaTUnkSessPkts_Object = MibTableColumn
tmnxMobPdnGyStatCcaTUnkSessPkts = _TmnxMobPdnGyStatCcaTUnkSessPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 38),
    _TmnxMobPdnGyStatCcaTUnkSessPkts_Type()
)
tmnxMobPdnGyStatCcaTUnkSessPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatCcaTUnkSessPkts.setStatus("current")
_TmnxMobPdnGyStatRarUnkSessPkts_Type = Counter32
_TmnxMobPdnGyStatRarUnkSessPkts_Object = MibTableColumn
tmnxMobPdnGyStatRarUnkSessPkts = _TmnxMobPdnGyStatRarUnkSessPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 39),
    _TmnxMobPdnGyStatRarUnkSessPkts_Type()
)
tmnxMobPdnGyStatRarUnkSessPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRarUnkSessPkts.setStatus("current")
_TmnxMobPdnGyStatAsrUnkSessPkts_Type = Counter32
_TmnxMobPdnGyStatAsrUnkSessPkts_Object = MibTableColumn
tmnxMobPdnGyStatAsrUnkSessPkts = _TmnxMobPdnGyStatAsrUnkSessPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 40),
    _TmnxMobPdnGyStatAsrUnkSessPkts_Type()
)
tmnxMobPdnGyStatAsrUnkSessPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatAsrUnkSessPkts.setStatus("current")
_TmnxMobPdnGyStatTxCer_Type = Counter32
_TmnxMobPdnGyStatTxCer_Object = MibTableColumn
tmnxMobPdnGyStatTxCer = _TmnxMobPdnGyStatTxCer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 41),
    _TmnxMobPdnGyStatTxCer_Type()
)
tmnxMobPdnGyStatTxCer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatTxCer.setStatus("current")
_TmnxMobPdnGyStatRxCea_Type = Counter32
_TmnxMobPdnGyStatRxCea_Object = MibTableColumn
tmnxMobPdnGyStatRxCea = _TmnxMobPdnGyStatRxCea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 42),
    _TmnxMobPdnGyStatRxCea_Type()
)
tmnxMobPdnGyStatRxCea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxCea.setStatus("current")
_TmnxMobPdnGyStatRxDpr_Type = Counter32
_TmnxMobPdnGyStatRxDpr_Object = MibTableColumn
tmnxMobPdnGyStatRxDpr = _TmnxMobPdnGyStatRxDpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 43),
    _TmnxMobPdnGyStatRxDpr_Type()
)
tmnxMobPdnGyStatRxDpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxDpr.setStatus("current")
_TmnxMobPdnGyStatTxDpa_Type = Counter32
_TmnxMobPdnGyStatTxDpa_Object = MibTableColumn
tmnxMobPdnGyStatTxDpa = _TmnxMobPdnGyStatTxDpa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 44),
    _TmnxMobPdnGyStatTxDpa_Type()
)
tmnxMobPdnGyStatTxDpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatTxDpa.setStatus("current")
_TmnxMobPdnGyStatTxDwr_Type = Counter32
_TmnxMobPdnGyStatTxDwr_Object = MibTableColumn
tmnxMobPdnGyStatTxDwr = _TmnxMobPdnGyStatTxDwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 45),
    _TmnxMobPdnGyStatTxDwr_Type()
)
tmnxMobPdnGyStatTxDwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatTxDwr.setStatus("current")
_TmnxMobPdnGyStatRxDwa_Type = Counter32
_TmnxMobPdnGyStatRxDwa_Object = MibTableColumn
tmnxMobPdnGyStatRxDwa = _TmnxMobPdnGyStatRxDwa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 46),
    _TmnxMobPdnGyStatRxDwa_Type()
)
tmnxMobPdnGyStatRxDwa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxDwa.setStatus("current")
_TmnxMobPdnGyStatConnAttempts_Type = Counter32
_TmnxMobPdnGyStatConnAttempts_Object = MibTableColumn
tmnxMobPdnGyStatConnAttempts = _TmnxMobPdnGyStatConnAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 47),
    _TmnxMobPdnGyStatConnAttempts_Type()
)
tmnxMobPdnGyStatConnAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatConnAttempts.setStatus("current")
_TmnxMobPdnGyStatConnFailures_Type = Counter32
_TmnxMobPdnGyStatConnFailures_Object = MibTableColumn
tmnxMobPdnGyStatConnFailures = _TmnxMobPdnGyStatConnFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 48),
    _TmnxMobPdnGyStatConnFailures_Type()
)
tmnxMobPdnGyStatConnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatConnFailures.setStatus("current")
_TmnxMobPdnGyStatRxTransportDisc_Type = Counter32
_TmnxMobPdnGyStatRxTransportDisc_Object = MibTableColumn
tmnxMobPdnGyStatRxTransportDisc = _TmnxMobPdnGyStatRxTransportDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 49),
    _TmnxMobPdnGyStatRxTransportDisc_Type()
)
tmnxMobPdnGyStatRxTransportDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxTransportDisc.setStatus("current")
_TmnxMobPdnGyStatRxMsgUnexpectVer_Type = Counter32
_TmnxMobPdnGyStatRxMsgUnexpectVer_Object = MibTableColumn
tmnxMobPdnGyStatRxMsgUnexpectVer = _TmnxMobPdnGyStatRxMsgUnexpectVer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 50),
    _TmnxMobPdnGyStatRxMsgUnexpectVer_Type()
)
tmnxMobPdnGyStatRxMsgUnexpectVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxMsgUnexpectVer.setStatus("current")
_TmnxMobPdnGyStatRxMsgTooBig_Type = Counter32
_TmnxMobPdnGyStatRxMsgTooBig_Object = MibTableColumn
tmnxMobPdnGyStatRxMsgTooBig = _TmnxMobPdnGyStatRxMsgTooBig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 51),
    _TmnxMobPdnGyStatRxMsgTooBig_Type()
)
tmnxMobPdnGyStatRxMsgTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxMsgTooBig.setStatus("current")
_TmnxMobPdnGyStatRxMsgTooSmall_Type = Counter32
_TmnxMobPdnGyStatRxMsgTooSmall_Object = MibTableColumn
tmnxMobPdnGyStatRxMsgTooSmall = _TmnxMobPdnGyStatRxMsgTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 52),
    _TmnxMobPdnGyStatRxMsgTooSmall_Type()
)
tmnxMobPdnGyStatRxMsgTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxMsgTooSmall.setStatus("current")
_TmnxMobPdnGyStatRxInvalidCea_Type = Counter32
_TmnxMobPdnGyStatRxInvalidCea_Object = MibTableColumn
tmnxMobPdnGyStatRxInvalidCea = _TmnxMobPdnGyStatRxInvalidCea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 53),
    _TmnxMobPdnGyStatRxInvalidCea_Type()
)
tmnxMobPdnGyStatRxInvalidCea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxInvalidCea.setStatus("current")
_TmnxMobPdnGyStatRxMsgs_Type = Counter32
_TmnxMobPdnGyStatRxMsgs_Object = MibTableColumn
tmnxMobPdnGyStatRxMsgs = _TmnxMobPdnGyStatRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 54),
    _TmnxMobPdnGyStatRxMsgs_Type()
)
tmnxMobPdnGyStatRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxMsgs.setStatus("current")
_TmnxMobPdnGyStatTxMsgs_Type = Counter32
_TmnxMobPdnGyStatTxMsgs_Object = MibTableColumn
tmnxMobPdnGyStatTxMsgs = _TmnxMobPdnGyStatTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 55),
    _TmnxMobPdnGyStatTxMsgs_Type()
)
tmnxMobPdnGyStatTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatTxMsgs.setStatus("current")
_TmnxMobPdnGyStatTxRetransmitMsgs_Type = Counter32
_TmnxMobPdnGyStatTxRetransmitMsgs_Object = MibTableColumn
tmnxMobPdnGyStatTxRetransmitMsgs = _TmnxMobPdnGyStatTxRetransmitMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 56),
    _TmnxMobPdnGyStatTxRetransmitMsgs_Type()
)
tmnxMobPdnGyStatTxRetransmitMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatTxRetransmitMsgs.setStatus("current")
_TmnxMobPdnGyStatTxDpr_Type = Counter32
_TmnxMobPdnGyStatTxDpr_Object = MibTableColumn
tmnxMobPdnGyStatTxDpr = _TmnxMobPdnGyStatTxDpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 57),
    _TmnxMobPdnGyStatTxDpr_Type()
)
tmnxMobPdnGyStatTxDpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatTxDpr.setStatus("current")
_TmnxMobPdnGyStatRxDpa_Type = Counter32
_TmnxMobPdnGyStatRxDpa_Object = MibTableColumn
tmnxMobPdnGyStatRxDpa = _TmnxMobPdnGyStatRxDpa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 58),
    _TmnxMobPdnGyStatRxDpa_Type()
)
tmnxMobPdnGyStatRxDpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxDpa.setStatus("current")
_TmnxMobPdnGyStatRxDwr_Type = Counter32
_TmnxMobPdnGyStatRxDwr_Object = MibTableColumn
tmnxMobPdnGyStatRxDwr = _TmnxMobPdnGyStatRxDwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 59),
    _TmnxMobPdnGyStatRxDwr_Type()
)
tmnxMobPdnGyStatRxDwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatRxDwr.setStatus("current")
_TmnxMobPdnGyStatTxDwa_Type = Counter32
_TmnxMobPdnGyStatTxDwa_Object = MibTableColumn
tmnxMobPdnGyStatTxDwa = _TmnxMobPdnGyStatTxDwa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 13, 1, 60),
    _TmnxMobPdnGyStatTxDwa_Type()
)
tmnxMobPdnGyStatTxDwa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatTxDwa.setStatus("current")
_TmnxMobPdnGaPeerTable_Object = MibTable
tmnxMobPdnGaPeerTable = _TmnxMobPdnGaPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 14)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGaPeerTable.setStatus("current")
_TmnxMobPdnGaPeerEntry_Object = MibTableRow
tmnxMobPdnGaPeerEntry = _TmnxMobPdnGaPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 14, 1)
)
tmnxMobPdnGaPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatPort"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGaPeerEntry.setStatus("current")
_TmnxMobPdnGaPeerLastChanged_Type = TimeStamp
_TmnxMobPdnGaPeerLastChanged_Object = MibTableColumn
tmnxMobPdnGaPeerLastChanged = _TmnxMobPdnGaPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 14, 1, 1),
    _TmnxMobPdnGaPeerLastChanged_Type()
)
tmnxMobPdnGaPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaPeerLastChanged.setStatus("current")
_TmnxMobPdnGaPeerCreateTime_Type = TimeStamp
_TmnxMobPdnGaPeerCreateTime_Object = MibTableColumn
tmnxMobPdnGaPeerCreateTime = _TmnxMobPdnGaPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 14, 1, 2),
    _TmnxMobPdnGaPeerCreateTime_Type()
)
tmnxMobPdnGaPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaPeerCreateTime.setStatus("current")
_TmnxMobPdnGaPeerPathMgmtState_Type = TmnxMobDiaPathMgmtState
_TmnxMobPdnGaPeerPathMgmtState_Object = MibTableColumn
tmnxMobPdnGaPeerPathMgmtState = _TmnxMobPdnGaPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 14, 1, 3),
    _TmnxMobPdnGaPeerPathMgmtState_Type()
)
tmnxMobPdnGaPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaPeerPathMgmtState.setStatus("current")
_TmnxMobPdnGaPeerDetailState_Type = TmnxMobDiaDetailPathMgmtState
_TmnxMobPdnGaPeerDetailState_Object = MibTableColumn
tmnxMobPdnGaPeerDetailState = _TmnxMobPdnGaPeerDetailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 14, 1, 4),
    _TmnxMobPdnGaPeerDetailState_Type()
)
tmnxMobPdnGaPeerDetailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaPeerDetailState.setStatus("current")
_TmnxMobPdnRadPeerTable_Object = MibTable
tmnxMobPdnRadPeerTable = _TmnxMobPdnRadPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 15)
)
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerTable.setStatus("current")
_TmnxMobPdnRadPeerEntry_Object = MibTableRow
tmnxMobPdnRadPeerEntry = _TmnxMobPdnRadPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 15, 1)
)
tmnxMobPdnRadPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerAddress"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerEntry.setStatus("current")
_TmnxMobPdnRadPeerAddressType_Type = InetAddressType
_TmnxMobPdnRadPeerAddressType_Object = MibTableColumn
tmnxMobPdnRadPeerAddressType = _TmnxMobPdnRadPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 15, 1, 1),
    _TmnxMobPdnRadPeerAddressType_Type()
)
tmnxMobPdnRadPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerAddressType.setStatus("current")


class _TmnxMobPdnRadPeerAddress_Type(InetAddress):
    """Custom type tmnxMobPdnRadPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnRadPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnRadPeerAddress_Object = MibTableColumn
tmnxMobPdnRadPeerAddress = _TmnxMobPdnRadPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 15, 1, 2),
    _TmnxMobPdnRadPeerAddress_Type()
)
tmnxMobPdnRadPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerAddress.setStatus("current")
_TmnxMobPdnRadPeerLastChanged_Type = TimeStamp
_TmnxMobPdnRadPeerLastChanged_Object = MibTableColumn
tmnxMobPdnRadPeerLastChanged = _TmnxMobPdnRadPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 15, 1, 3),
    _TmnxMobPdnRadPeerLastChanged_Type()
)
tmnxMobPdnRadPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerLastChanged.setStatus("current")
_TmnxMobPdnRadPeerCreateTime_Type = TimeStamp
_TmnxMobPdnRadPeerCreateTime_Object = MibTableColumn
tmnxMobPdnRadPeerCreateTime = _TmnxMobPdnRadPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 15, 1, 4),
    _TmnxMobPdnRadPeerCreateTime_Type()
)
tmnxMobPdnRadPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerCreateTime.setStatus("current")
_TmnxMobPdnRadPeerPathMgmtState_Type = TmnxMobDiaPathMgmtState
_TmnxMobPdnRadPeerPathMgmtState_Object = MibTableColumn
tmnxMobPdnRadPeerPathMgmtState = _TmnxMobPdnRadPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 15, 1, 5),
    _TmnxMobPdnRadPeerPathMgmtState_Type()
)
tmnxMobPdnRadPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerPathMgmtState.setStatus("current")
_TmnxMobPdnRadPeerDetailState_Type = TmnxMobDiaDetailPathMgmtState
_TmnxMobPdnRadPeerDetailState_Object = MibTableColumn
tmnxMobPdnRadPeerDetailState = _TmnxMobPdnRadPeerDetailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 15, 1, 6),
    _TmnxMobPdnRadPeerDetailState_Type()
)
tmnxMobPdnRadPeerDetailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerDetailState.setStatus("current")
_TmnxMobPdnRadStatTable_Object = MibTable
tmnxMobPdnRadStatTable = _TmnxMobPdnRadStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16)
)
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatTable.setStatus("current")
_TmnxMobPdnRadStatEntry_Object = MibTableRow
tmnxMobPdnRadStatEntry = _TmnxMobPdnRadStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1)
)
tmnxMobPdnRadStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadGrpName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfRadPeerIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerAddress"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatEntry.setStatus("current")
_TmnxMobPdnRadStatLastChanged_Type = TimeStamp
_TmnxMobPdnRadStatLastChanged_Object = MibTableColumn
tmnxMobPdnRadStatLastChanged = _TmnxMobPdnRadStatLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 1),
    _TmnxMobPdnRadStatLastChanged_Type()
)
tmnxMobPdnRadStatLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatLastChanged.setStatus("current")
_TmnxMobPdnRadStatAccessReqTx_Type = Counter32
_TmnxMobPdnRadStatAccessReqTx_Object = MibTableColumn
tmnxMobPdnRadStatAccessReqTx = _TmnxMobPdnRadStatAccessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 2),
    _TmnxMobPdnRadStatAccessReqTx_Type()
)
tmnxMobPdnRadStatAccessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatAccessReqTx.setStatus("current")
_TmnxMobPdnRadStatAccessAcceptRx_Type = Counter32
_TmnxMobPdnRadStatAccessAcceptRx_Object = MibTableColumn
tmnxMobPdnRadStatAccessAcceptRx = _TmnxMobPdnRadStatAccessAcceptRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 3),
    _TmnxMobPdnRadStatAccessAcceptRx_Type()
)
tmnxMobPdnRadStatAccessAcceptRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatAccessAcceptRx.setStatus("current")
_TmnxMobPdnRadStatAccessRejectRx_Type = Counter32
_TmnxMobPdnRadStatAccessRejectRx_Object = MibTableColumn
tmnxMobPdnRadStatAccessRejectRx = _TmnxMobPdnRadStatAccessRejectRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 4),
    _TmnxMobPdnRadStatAccessRejectRx_Type()
)
tmnxMobPdnRadStatAccessRejectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatAccessRejectRx.setStatus("current")
_TmnxMobPdnRadStatAcctReqStartTx_Type = Counter32
_TmnxMobPdnRadStatAcctReqStartTx_Object = MibTableColumn
tmnxMobPdnRadStatAcctReqStartTx = _TmnxMobPdnRadStatAcctReqStartTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 5),
    _TmnxMobPdnRadStatAcctReqStartTx_Type()
)
tmnxMobPdnRadStatAcctReqStartTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatAcctReqStartTx.setStatus("current")
_TmnxMobPdnRadStatAcctReqIntrmTx_Type = Counter32
_TmnxMobPdnRadStatAcctReqIntrmTx_Object = MibTableColumn
tmnxMobPdnRadStatAcctReqIntrmTx = _TmnxMobPdnRadStatAcctReqIntrmTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 6),
    _TmnxMobPdnRadStatAcctReqIntrmTx_Type()
)
tmnxMobPdnRadStatAcctReqIntrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatAcctReqIntrmTx.setStatus("current")
_TmnxMobPdnRadStatAcctReqStopTx_Type = Counter32
_TmnxMobPdnRadStatAcctReqStopTx_Object = MibTableColumn
tmnxMobPdnRadStatAcctReqStopTx = _TmnxMobPdnRadStatAcctReqStopTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 7),
    _TmnxMobPdnRadStatAcctReqStopTx_Type()
)
tmnxMobPdnRadStatAcctReqStopTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatAcctReqStopTx.setStatus("current")
_TmnxMobPdnRadStatAcctResponseRx_Type = Counter32
_TmnxMobPdnRadStatAcctResponseRx_Object = MibTableColumn
tmnxMobPdnRadStatAcctResponseRx = _TmnxMobPdnRadStatAcctResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 8),
    _TmnxMobPdnRadStatAcctResponseRx_Type()
)
tmnxMobPdnRadStatAcctResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatAcctResponseRx.setStatus("current")
_TmnxMobPdnRadStatMandAttrMissing_Type = Counter32
_TmnxMobPdnRadStatMandAttrMissing_Object = MibTableColumn
tmnxMobPdnRadStatMandAttrMissing = _TmnxMobPdnRadStatMandAttrMissing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 9),
    _TmnxMobPdnRadStatMandAttrMissing_Type()
)
tmnxMobPdnRadStatMandAttrMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatMandAttrMissing.setStatus("current")
_TmnxMobPdnRadStatMandAttrErrors_Type = Counter32
_TmnxMobPdnRadStatMandAttrErrors_Object = MibTableColumn
tmnxMobPdnRadStatMandAttrErrors = _TmnxMobPdnRadStatMandAttrErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 10),
    _TmnxMobPdnRadStatMandAttrErrors_Type()
)
tmnxMobPdnRadStatMandAttrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatMandAttrErrors.setStatus("current")
_TmnxMobPdnRadStatUnsupportedAttr_Type = Counter32
_TmnxMobPdnRadStatUnsupportedAttr_Object = MibTableColumn
tmnxMobPdnRadStatUnsupportedAttr = _TmnxMobPdnRadStatUnsupportedAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 11),
    _TmnxMobPdnRadStatUnsupportedAttr_Type()
)
tmnxMobPdnRadStatUnsupportedAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatUnsupportedAttr.setStatus("current")
_TmnxMobPdnRadStatOptionalAttrErr_Type = Counter32
_TmnxMobPdnRadStatOptionalAttrErr_Object = MibTableColumn
tmnxMobPdnRadStatOptionalAttrErr = _TmnxMobPdnRadStatOptionalAttrErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 12),
    _TmnxMobPdnRadStatOptionalAttrErr_Type()
)
tmnxMobPdnRadStatOptionalAttrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatOptionalAttrErr.setStatus("current")
_TmnxMobPdnRadStatAuthError_Type = Counter32
_TmnxMobPdnRadStatAuthError_Object = MibTableColumn
tmnxMobPdnRadStatAuthError = _TmnxMobPdnRadStatAuthError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 13),
    _TmnxMobPdnRadStatAuthError_Type()
)
tmnxMobPdnRadStatAuthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatAuthError.setStatus("current")
_TmnxMobPdnRadStatUnexpectedCode_Type = Counter32
_TmnxMobPdnRadStatUnexpectedCode_Object = MibTableColumn
tmnxMobPdnRadStatUnexpectedCode = _TmnxMobPdnRadStatUnexpectedCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 14),
    _TmnxMobPdnRadStatUnexpectedCode_Type()
)
tmnxMobPdnRadStatUnexpectedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatUnexpectedCode.setStatus("current")
_TmnxMobPdnRadStatRespTimeBelow1_Type = Counter32
_TmnxMobPdnRadStatRespTimeBelow1_Object = MibTableColumn
tmnxMobPdnRadStatRespTimeBelow1 = _TmnxMobPdnRadStatRespTimeBelow1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 15),
    _TmnxMobPdnRadStatRespTimeBelow1_Type()
)
tmnxMobPdnRadStatRespTimeBelow1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatRespTimeBelow1.setStatus("current")
_TmnxMobPdnRadStatRespTime1to4_Type = Counter32
_TmnxMobPdnRadStatRespTime1to4_Object = MibTableColumn
tmnxMobPdnRadStatRespTime1to4 = _TmnxMobPdnRadStatRespTime1to4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 16),
    _TmnxMobPdnRadStatRespTime1to4_Type()
)
tmnxMobPdnRadStatRespTime1to4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatRespTime1to4.setStatus("current")
_TmnxMobPdnRadStatRespTimeAbove4_Type = Counter32
_TmnxMobPdnRadStatRespTimeAbove4_Object = MibTableColumn
tmnxMobPdnRadStatRespTimeAbove4 = _TmnxMobPdnRadStatRespTimeAbove4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 17),
    _TmnxMobPdnRadStatRespTimeAbove4_Type()
)
tmnxMobPdnRadStatRespTimeAbove4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatRespTimeAbove4.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatRespTimeAbove4.setUnits("seconds")
_TmnxMobPdnRadStatRetries_Type = Counter32
_TmnxMobPdnRadStatRetries_Object = MibTableColumn
tmnxMobPdnRadStatRetries = _TmnxMobPdnRadStatRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 18),
    _TmnxMobPdnRadStatRetries_Type()
)
tmnxMobPdnRadStatRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatRetries.setStatus("current")
_TmnxMobPdnRadStatPrFinalTimeout_Type = Counter32
_TmnxMobPdnRadStatPrFinalTimeout_Object = MibTableColumn
tmnxMobPdnRadStatPrFinalTimeout = _TmnxMobPdnRadStatPrFinalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 19),
    _TmnxMobPdnRadStatPrFinalTimeout_Type()
)
tmnxMobPdnRadStatPrFinalTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatPrFinalTimeout.setStatus("current")
_TmnxMobPdnRadStatDiscReqRx_Type = Counter32
_TmnxMobPdnRadStatDiscReqRx_Object = MibTableColumn
tmnxMobPdnRadStatDiscReqRx = _TmnxMobPdnRadStatDiscReqRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 20),
    _TmnxMobPdnRadStatDiscReqRx_Type()
)
tmnxMobPdnRadStatDiscReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatDiscReqRx.setStatus("current")
_TmnxMobPdnRadStatDiscAckTx_Type = Counter32
_TmnxMobPdnRadStatDiscAckTx_Object = MibTableColumn
tmnxMobPdnRadStatDiscAckTx = _TmnxMobPdnRadStatDiscAckTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 21),
    _TmnxMobPdnRadStatDiscAckTx_Type()
)
tmnxMobPdnRadStatDiscAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatDiscAckTx.setStatus("current")
_TmnxMobPdnRadStatDiscNakTx_Type = Counter32
_TmnxMobPdnRadStatDiscNakTx_Object = MibTableColumn
tmnxMobPdnRadStatDiscNakTx = _TmnxMobPdnRadStatDiscNakTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 22),
    _TmnxMobPdnRadStatDiscNakTx_Type()
)
tmnxMobPdnRadStatDiscNakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatDiscNakTx.setStatus("current")
_TmnxMobPdnRadStatDiscMandAtrMiss_Type = Counter32
_TmnxMobPdnRadStatDiscMandAtrMiss_Object = MibTableColumn
tmnxMobPdnRadStatDiscMandAtrMiss = _TmnxMobPdnRadStatDiscMandAtrMiss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 23),
    _TmnxMobPdnRadStatDiscMandAtrMiss_Type()
)
tmnxMobPdnRadStatDiscMandAtrMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatDiscMandAtrMiss.setStatus("current")
_TmnxMobPdnRadStatDiscUnsupprAttr_Type = Counter32
_TmnxMobPdnRadStatDiscUnsupprAttr_Object = MibTableColumn
tmnxMobPdnRadStatDiscUnsupprAttr = _TmnxMobPdnRadStatDiscUnsupprAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 24),
    _TmnxMobPdnRadStatDiscUnsupprAttr_Type()
)
tmnxMobPdnRadStatDiscUnsupprAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatDiscUnsupprAttr.setStatus("current")
_TmnxMobPdnRadStatDiscSessNotFnd_Type = Counter32
_TmnxMobPdnRadStatDiscSessNotFnd_Object = MibTableColumn
tmnxMobPdnRadStatDiscSessNotFnd = _TmnxMobPdnRadStatDiscSessNotFnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 25),
    _TmnxMobPdnRadStatDiscSessNotFnd_Type()
)
tmnxMobPdnRadStatDiscSessNotFnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatDiscSessNotFnd.setStatus("current")
_TmnxMobPdnRadStatDiscAuthError_Type = Counter32
_TmnxMobPdnRadStatDiscAuthError_Object = MibTableColumn
tmnxMobPdnRadStatDiscAuthError = _TmnxMobPdnRadStatDiscAuthError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 26),
    _TmnxMobPdnRadStatDiscAuthError_Type()
)
tmnxMobPdnRadStatDiscAuthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatDiscAuthError.setStatus("current")
_TmnxMobPdnRadStatDiscUnexpcCode_Type = Counter32
_TmnxMobPdnRadStatDiscUnexpcCode_Object = MibTableColumn
tmnxMobPdnRadStatDiscUnexpcCode = _TmnxMobPdnRadStatDiscUnexpcCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 27),
    _TmnxMobPdnRadStatDiscUnexpcCode_Type()
)
tmnxMobPdnRadStatDiscUnexpcCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatDiscUnexpcCode.setStatus("current")
_TmnxMobPdnRadStatMsgFinalTimeout_Type = Counter32
_TmnxMobPdnRadStatMsgFinalTimeout_Object = MibTableColumn
tmnxMobPdnRadStatMsgFinalTimeout = _TmnxMobPdnRadStatMsgFinalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 16, 1, 28),
    _TmnxMobPdnRadStatMsgFinalTimeout_Type()
)
tmnxMobPdnRadStatMsgFinalTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadStatMsgFinalTimeout.setStatus("current")
_TmnxMobPdnThresTable_Object = MibTable
tmnxMobPdnThresTable = _TmnxMobPdnThresTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17)
)
if mibBuilder.loadTexts:
    tmnxMobPdnThresTable.setStatus("current")
_TmnxMobPdnThresEntry_Object = MibTableRow
tmnxMobPdnThresEntry = _TmnxMobPdnThresEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1)
)
tmnxMobPdnThresEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnThresEntry.setStatus("current")
_TmnxMobPdnThresLastChanged_Type = TimeStamp
_TmnxMobPdnThresLastChanged_Object = MibTableColumn
tmnxMobPdnThresLastChanged = _TmnxMobPdnThresLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 1),
    _TmnxMobPdnThresLastChanged_Type()
)
tmnxMobPdnThresLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresLastChanged.setStatus("current")
_TmnxMobPdnThresBrMgmtLmtUe_Type = Gauge32
_TmnxMobPdnThresBrMgmtLmtUe_Object = MibTableColumn
tmnxMobPdnThresBrMgmtLmtUe = _TmnxMobPdnThresBrMgmtLmtUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 2),
    _TmnxMobPdnThresBrMgmtLmtUe_Type()
)
tmnxMobPdnThresBrMgmtLmtUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtLmtUe.setStatus("current")
_TmnxMobPdnThresBrMgmtLmtBr_Type = Gauge32
_TmnxMobPdnThresBrMgmtLmtBr_Object = MibTableColumn
tmnxMobPdnThresBrMgmtLmtBr = _TmnxMobPdnThresBrMgmtLmtBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 3),
    _TmnxMobPdnThresBrMgmtLmtBr_Type()
)
tmnxMobPdnThresBrMgmtLmtBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtLmtBr.setStatus("current")
_TmnxMobPdnThresBrMgmtLmtDefBr_Type = Gauge32
_TmnxMobPdnThresBrMgmtLmtDefBr_Object = MibTableColumn
tmnxMobPdnThresBrMgmtLmtDefBr = _TmnxMobPdnThresBrMgmtLmtDefBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 4),
    _TmnxMobPdnThresBrMgmtLmtDefBr_Type()
)
tmnxMobPdnThresBrMgmtLmtDefBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtLmtDefBr.setStatus("current")
_TmnxMobPdnThresBrMgmtLmtDedBr_Type = Gauge32
_TmnxMobPdnThresBrMgmtLmtDedBr_Object = MibTableColumn
tmnxMobPdnThresBrMgmtLmtDedBr = _TmnxMobPdnThresBrMgmtLmtDedBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 5),
    _TmnxMobPdnThresBrMgmtLmtDedBr_Type()
)
tmnxMobPdnThresBrMgmtLmtDedBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtLmtDedBr.setStatus("current")
_TmnxMobPdnThresBrMgmtLmtActBr_Type = Gauge32
_TmnxMobPdnThresBrMgmtLmtActBr_Object = MibTableColumn
tmnxMobPdnThresBrMgmtLmtActBr = _TmnxMobPdnThresBrMgmtLmtActBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 6),
    _TmnxMobPdnThresBrMgmtLmtActBr_Type()
)
tmnxMobPdnThresBrMgmtLmtActBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtLmtActBr.setStatus("current")
_TmnxMobPdnThresBrMgmtLmtUePgd_Type = Gauge32
_TmnxMobPdnThresBrMgmtLmtUePgd_Object = MibTableColumn
tmnxMobPdnThresBrMgmtLmtUePgd = _TmnxMobPdnThresBrMgmtLmtUePgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 7),
    _TmnxMobPdnThresBrMgmtLmtUePgd_Type()
)
tmnxMobPdnThresBrMgmtLmtUePgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtLmtUePgd.setStatus("current")
_TmnxMobPdnThresBrMgmtCfsAttch_Type = Gauge32
_TmnxMobPdnThresBrMgmtCfsAttch_Object = MibTableColumn
tmnxMobPdnThresBrMgmtCfsAttch = _TmnxMobPdnThresBrMgmtCfsAttch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 8),
    _TmnxMobPdnThresBrMgmtCfsAttch_Type()
)
tmnxMobPdnThresBrMgmtCfsAttch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCfsAttch.setStatus("current")
_TmnxMobPdnThresBrMgmtCfsDedBr_Type = Gauge32
_TmnxMobPdnThresBrMgmtCfsDedBr_Object = MibTableColumn
tmnxMobPdnThresBrMgmtCfsDedBr = _TmnxMobPdnThresBrMgmtCfsDedBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 9),
    _TmnxMobPdnThresBrMgmtCfsDedBr_Type()
)
tmnxMobPdnThresBrMgmtCfsDedBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCfsDedBr.setStatus("current")
_TmnxMobPdnThresBrMgmtCfsReloc_Type = Gauge32
_TmnxMobPdnThresBrMgmtCfsReloc_Object = MibTableColumn
tmnxMobPdnThresBrMgmtCfsReloc = _TmnxMobPdnThresBrMgmtCfsReloc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 10),
    _TmnxMobPdnThresBrMgmtCfsReloc_Type()
)
tmnxMobPdnThresBrMgmtCfsReloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCfsReloc.setStatus("current")


class _TmnxMobPdnThresBrMgmtCffAttch_Type(Gauge32):
    """Custom type tmnxMobPdnThresBrMgmtCffAttch based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobPdnThresBrMgmtCffAttch_Type.__name__ = "Gauge32"
_TmnxMobPdnThresBrMgmtCffAttch_Object = MibTableColumn
tmnxMobPdnThresBrMgmtCffAttch = _TmnxMobPdnThresBrMgmtCffAttch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 11),
    _TmnxMobPdnThresBrMgmtCffAttch_Type()
)
tmnxMobPdnThresBrMgmtCffAttch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCffAttch.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCffAttch.setUnits("Percent")


class _TmnxMobPdnThresBrMgmtCffDedBr_Type(Gauge32):
    """Custom type tmnxMobPdnThresBrMgmtCffDedBr based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobPdnThresBrMgmtCffDedBr_Type.__name__ = "Gauge32"
_TmnxMobPdnThresBrMgmtCffDedBr_Object = MibTableColumn
tmnxMobPdnThresBrMgmtCffDedBr = _TmnxMobPdnThresBrMgmtCffDedBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 12),
    _TmnxMobPdnThresBrMgmtCffDedBr_Type()
)
tmnxMobPdnThresBrMgmtCffDedBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCffDedBr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCffDedBr.setUnits("Percent")


class _TmnxMobPdnThresBrMgmtCffHdOver_Type(Gauge32):
    """Custom type tmnxMobPdnThresBrMgmtCffHdOver based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobPdnThresBrMgmtCffHdOver_Type.__name__ = "Gauge32"
_TmnxMobPdnThresBrMgmtCffHdOver_Object = MibTableColumn
tmnxMobPdnThresBrMgmtCffHdOver = _TmnxMobPdnThresBrMgmtCffHdOver_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 13),
    _TmnxMobPdnThresBrMgmtCffHdOver_Type()
)
tmnxMobPdnThresBrMgmtCffHdOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCffHdOver.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCffHdOver.setUnits("Percent")


class _TmnxMobPdnThresBrMgmtCffSrUnavl_Type(Gauge32):
    """Custom type tmnxMobPdnThresBrMgmtCffSrUnavl based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobPdnThresBrMgmtCffSrUnavl_Type.__name__ = "Gauge32"
_TmnxMobPdnThresBrMgmtCffSrUnavl_Object = MibTableColumn
tmnxMobPdnThresBrMgmtCffSrUnavl = _TmnxMobPdnThresBrMgmtCffSrUnavl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 14),
    _TmnxMobPdnThresBrMgmtCffSrUnavl_Type()
)
tmnxMobPdnThresBrMgmtCffSrUnavl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCffSrUnavl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrMgmtCffSrUnavl.setUnits("Percent")
_TmnxMobPdnThresBrTrfcThrptUL_Type = Gauge32
_TmnxMobPdnThresBrTrfcThrptUL_Object = MibTableColumn
tmnxMobPdnThresBrTrfcThrptUL = _TmnxMobPdnThresBrTrfcThrptUL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 15),
    _TmnxMobPdnThresBrTrfcThrptUL_Type()
)
tmnxMobPdnThresBrTrfcThrptUL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrTrfcThrptUL.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrTrfcThrptUL.setUnits("megabytes")
_TmnxMobPdnThresBrTrfcThrptDL_Type = Gauge32
_TmnxMobPdnThresBrTrfcThrptDL_Object = MibTableColumn
tmnxMobPdnThresBrTrfcThrptDL = _TmnxMobPdnThresBrTrfcThrptDL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 16),
    _TmnxMobPdnThresBrTrfcThrptDL_Type()
)
tmnxMobPdnThresBrTrfcThrptDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrTrfcThrptDL.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrTrfcThrptDL.setUnits("megabytes")
_TmnxMobPdnThresBrTrfcAspFail_Type = Gauge32
_TmnxMobPdnThresBrTrfcAspFail_Object = MibTableColumn
tmnxMobPdnThresBrTrfcAspFail = _TmnxMobPdnThresBrTrfcAspFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 17),
    _TmnxMobPdnThresBrTrfcAspFail_Type()
)
tmnxMobPdnThresBrTrfcAspFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrTrfcAspFail.setStatus("current")
_TmnxMobPdnThresBrTrfcBrBdvErr_Type = Gauge32
_TmnxMobPdnThresBrTrfcBrBdvErr_Object = MibTableColumn
tmnxMobPdnThresBrTrfcBrBdvErr = _TmnxMobPdnThresBrTrfcBrBdvErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 18),
    _TmnxMobPdnThresBrTrfcBrBdvErr_Type()
)
tmnxMobPdnThresBrTrfcBrBdvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresBrTrfcBrBdvErr.setStatus("current")
_TmnxMobPdnThresPthMgmtS5Fail_Type = Gauge32
_TmnxMobPdnThresPthMgmtS5Fail_Object = MibTableColumn
tmnxMobPdnThresPthMgmtS5Fail = _TmnxMobPdnThresPthMgmtS5Fail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 19),
    _TmnxMobPdnThresPthMgmtS5Fail_Type()
)
tmnxMobPdnThresPthMgmtS5Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresPthMgmtS5Fail.setStatus("current")
_TmnxMobPdnThresPthMgmtS5Restart_Type = Gauge32
_TmnxMobPdnThresPthMgmtS5Restart_Object = MibTableColumn
tmnxMobPdnThresPthMgmtS5Restart = _TmnxMobPdnThresPthMgmtS5Restart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 20),
    _TmnxMobPdnThresPthMgmtS5Restart_Type()
)
tmnxMobPdnThresPthMgmtS5Restart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresPthMgmtS5Restart.setStatus("current")
_TmnxMobPdnThresPthMgmtS5NoResp_Type = Gauge32
_TmnxMobPdnThresPthMgmtS5NoResp_Object = MibTableColumn
tmnxMobPdnThresPthMgmtS5NoResp = _TmnxMobPdnThresPthMgmtS5NoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 21),
    _TmnxMobPdnThresPthMgmtS5NoResp_Type()
)
tmnxMobPdnThresPthMgmtS5NoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresPthMgmtS5NoResp.setStatus("current")
_TmnxMobPdnThresPthMgmtS5Peer_Type = Gauge32
_TmnxMobPdnThresPthMgmtS5Peer_Object = MibTableColumn
tmnxMobPdnThresPthMgmtS5Peer = _TmnxMobPdnThresPthMgmtS5Peer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 22),
    _TmnxMobPdnThresPthMgmtS5Peer_Type()
)
tmnxMobPdnThresPthMgmtS5Peer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresPthMgmtS5Peer.setStatus("current")
_TmnxMobPdnThresPthMgmtS8Peer_Type = Gauge32
_TmnxMobPdnThresPthMgmtS8Peer_Object = MibTableColumn
tmnxMobPdnThresPthMgmtS8Peer = _TmnxMobPdnThresPthMgmtS8Peer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 23),
    _TmnxMobPdnThresPthMgmtS8Peer_Type()
)
tmnxMobPdnThresPthMgmtS8Peer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresPthMgmtS8Peer.setStatus("current")
_TmnxMobPdnThresPthMgmtGxFail_Type = Gauge32
_TmnxMobPdnThresPthMgmtGxFail_Object = MibTableColumn
tmnxMobPdnThresPthMgmtGxFail = _TmnxMobPdnThresPthMgmtGxFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 24),
    _TmnxMobPdnThresPthMgmtGxFail_Type()
)
tmnxMobPdnThresPthMgmtGxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresPthMgmtGxFail.setStatus("current")
_TmnxMobPdnThresPthMgmtRfFail_Type = Gauge32
_TmnxMobPdnThresPthMgmtRfFail_Object = MibTableColumn
tmnxMobPdnThresPthMgmtRfFail = _TmnxMobPdnThresPthMgmtRfFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 17, 1, 25),
    _TmnxMobPdnThresPthMgmtRfFail_Type()
)
tmnxMobPdnThresPthMgmtRfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnThresPthMgmtRfFail.setStatus("current")
_TmnxMobPdnGpStatTable_Object = MibTable
tmnxMobPdnGpStatTable = _TmnxMobPdnGpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18)
)
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatTable.setStatus("current")
_TmnxMobPdnGpStatEntry_Object = MibTableRow
tmnxMobPdnGpStatEntry = _TmnxMobPdnGpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1)
)
tmnxMobPdnGpStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatEntry.setStatus("current")
_TmnxMobPdnGpStatCreatePdpReq_Type = Counter32
_TmnxMobPdnGpStatCreatePdpReq_Object = MibTableColumn
tmnxMobPdnGpStatCreatePdpReq = _TmnxMobPdnGpStatCreatePdpReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 1),
    _TmnxMobPdnGpStatCreatePdpReq_Type()
)
tmnxMobPdnGpStatCreatePdpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatCreatePdpReq.setStatus("current")
_TmnxMobPdnGpStatCreatePdpRsp_Type = Counter32
_TmnxMobPdnGpStatCreatePdpRsp_Object = MibTableColumn
tmnxMobPdnGpStatCreatePdpRsp = _TmnxMobPdnGpStatCreatePdpRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 2),
    _TmnxMobPdnGpStatCreatePdpRsp_Type()
)
tmnxMobPdnGpStatCreatePdpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatCreatePdpRsp.setStatus("current")
_TmnxMobPdnGpStatDeletePdpReq_Type = Counter32
_TmnxMobPdnGpStatDeletePdpReq_Object = MibTableColumn
tmnxMobPdnGpStatDeletePdpReq = _TmnxMobPdnGpStatDeletePdpReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 3),
    _TmnxMobPdnGpStatDeletePdpReq_Type()
)
tmnxMobPdnGpStatDeletePdpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatDeletePdpReq.setStatus("current")
_TmnxMobPdnGpStatDeletePdpRsp_Type = Counter32
_TmnxMobPdnGpStatDeletePdpRsp_Object = MibTableColumn
tmnxMobPdnGpStatDeletePdpRsp = _TmnxMobPdnGpStatDeletePdpRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 4),
    _TmnxMobPdnGpStatDeletePdpRsp_Type()
)
tmnxMobPdnGpStatDeletePdpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatDeletePdpRsp.setStatus("current")
_TmnxMobPdnGpStatModifyPdpReq_Type = Counter32
_TmnxMobPdnGpStatModifyPdpReq_Object = MibTableColumn
tmnxMobPdnGpStatModifyPdpReq = _TmnxMobPdnGpStatModifyPdpReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 5),
    _TmnxMobPdnGpStatModifyPdpReq_Type()
)
tmnxMobPdnGpStatModifyPdpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatModifyPdpReq.setStatus("current")
_TmnxMobPdnGpStatModifyPdpRsp_Type = Counter32
_TmnxMobPdnGpStatModifyPdpRsp_Object = MibTableColumn
tmnxMobPdnGpStatModifyPdpRsp = _TmnxMobPdnGpStatModifyPdpRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 6),
    _TmnxMobPdnGpStatModifyPdpRsp_Type()
)
tmnxMobPdnGpStatModifyPdpRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatModifyPdpRsp.setStatus("current")
_TmnxMobPdnGpStatRxEchoRequests_Type = Counter32
_TmnxMobPdnGpStatRxEchoRequests_Object = MibTableColumn
tmnxMobPdnGpStatRxEchoRequests = _TmnxMobPdnGpStatRxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 7),
    _TmnxMobPdnGpStatRxEchoRequests_Type()
)
tmnxMobPdnGpStatRxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatRxEchoRequests.setStatus("current")
_TmnxMobPdnGpStatTxEchoResponses_Type = Counter32
_TmnxMobPdnGpStatTxEchoResponses_Object = MibTableColumn
tmnxMobPdnGpStatTxEchoResponses = _TmnxMobPdnGpStatTxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 8),
    _TmnxMobPdnGpStatTxEchoResponses_Type()
)
tmnxMobPdnGpStatTxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatTxEchoResponses.setStatus("current")
_TmnxMobPdnGpStatTxEchoRequests_Type = Counter32
_TmnxMobPdnGpStatTxEchoRequests_Object = MibTableColumn
tmnxMobPdnGpStatTxEchoRequests = _TmnxMobPdnGpStatTxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 9),
    _TmnxMobPdnGpStatTxEchoRequests_Type()
)
tmnxMobPdnGpStatTxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatTxEchoRequests.setStatus("current")
_TmnxMobPdnGpStatRxEchoResponses_Type = Counter32
_TmnxMobPdnGpStatRxEchoResponses_Object = MibTableColumn
tmnxMobPdnGpStatRxEchoResponses = _TmnxMobPdnGpStatRxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 10),
    _TmnxMobPdnGpStatRxEchoResponses_Type()
)
tmnxMobPdnGpStatRxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatRxEchoResponses.setStatus("current")
_TmnxMobPdnGpStatRxErrorsIndCnt_Type = Counter32
_TmnxMobPdnGpStatRxErrorsIndCnt_Object = MibTableColumn
tmnxMobPdnGpStatRxErrorsIndCnt = _TmnxMobPdnGpStatRxErrorsIndCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 11),
    _TmnxMobPdnGpStatRxErrorsIndCnt_Type()
)
tmnxMobPdnGpStatRxErrorsIndCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatRxErrorsIndCnt.setStatus("current")
_TmnxMobPdnGpStatTxErrorsIndCnt_Type = Counter32
_TmnxMobPdnGpStatTxErrorsIndCnt_Object = MibTableColumn
tmnxMobPdnGpStatTxErrorsIndCnt = _TmnxMobPdnGpStatTxErrorsIndCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 12),
    _TmnxMobPdnGpStatTxErrorsIndCnt_Type()
)
tmnxMobPdnGpStatTxErrorsIndCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatTxErrorsIndCnt.setStatus("current")
_TmnxMobPdnGpStatRxMalformedPkts_Type = Counter32
_TmnxMobPdnGpStatRxMalformedPkts_Object = MibTableColumn
tmnxMobPdnGpStatRxMalformedPkts = _TmnxMobPdnGpStatRxMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 13),
    _TmnxMobPdnGpStatRxMalformedPkts_Type()
)
tmnxMobPdnGpStatRxMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatRxMalformedPkts.setStatus("current")
_TmnxMobPdnGpStatRxUnknownPkts_Type = Counter32
_TmnxMobPdnGpStatRxUnknownPkts_Object = MibTableColumn
tmnxMobPdnGpStatRxUnknownPkts = _TmnxMobPdnGpStatRxUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 14),
    _TmnxMobPdnGpStatRxUnknownPkts_Type()
)
tmnxMobPdnGpStatRxUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatRxUnknownPkts.setStatus("current")
_TmnxMobPdnGpStatRxMissingIePkts_Type = Counter32
_TmnxMobPdnGpStatRxMissingIePkts_Object = MibTableColumn
tmnxMobPdnGpStatRxMissingIePkts = _TmnxMobPdnGpStatRxMissingIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 15),
    _TmnxMobPdnGpStatRxMissingIePkts_Type()
)
tmnxMobPdnGpStatRxMissingIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatRxMissingIePkts.setStatus("current")
_TmnxMobPdnGpStatPeerRestarts_Type = Counter32
_TmnxMobPdnGpStatPeerRestarts_Object = MibTableColumn
tmnxMobPdnGpStatPeerRestarts = _TmnxMobPdnGpStatPeerRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 16),
    _TmnxMobPdnGpStatPeerRestarts_Type()
)
tmnxMobPdnGpStatPeerRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatPeerRestarts.setStatus("current")
_TmnxMobPdnGpStatPeerRestrtCount_Type = Counter32
_TmnxMobPdnGpStatPeerRestrtCount_Object = MibTableColumn
tmnxMobPdnGpStatPeerRestrtCount = _TmnxMobPdnGpStatPeerRestrtCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 17),
    _TmnxMobPdnGpStatPeerRestrtCount_Type()
)
tmnxMobPdnGpStatPeerRestrtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatPeerRestrtCount.setStatus("current")
_TmnxMobPdnGpStatPathMgmtFails_Type = Counter32
_TmnxMobPdnGpStatPathMgmtFails_Object = MibTableColumn
tmnxMobPdnGpStatPathMgmtFails = _TmnxMobPdnGpStatPathMgmtFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 18, 1, 18),
    _TmnxMobPdnGpStatPathMgmtFails_Type()
)
tmnxMobPdnGpStatPathMgmtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpStatPathMgmtFails.setStatus("current")
_TmnxMobPdnS2aPeerTable_Object = MibTable
tmnxMobPdnS2aPeerTable = _TmnxMobPdnS2aPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerTable.setStatus("current")
_TmnxMobPdnS2aPeerEntry_Object = MibTableRow
tmnxMobPdnS2aPeerEntry = _TmnxMobPdnS2aPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1)
)
tmnxMobPdnS2aPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerEntry.setStatus("current")
_TmnxMobPdnS2aPeerAddressType_Type = InetAddressType
_TmnxMobPdnS2aPeerAddressType_Object = MibTableColumn
tmnxMobPdnS2aPeerAddressType = _TmnxMobPdnS2aPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 1),
    _TmnxMobPdnS2aPeerAddressType_Type()
)
tmnxMobPdnS2aPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerAddressType.setStatus("current")


class _TmnxMobPdnS2aPeerAddress_Type(InetAddress):
    """Custom type tmnxMobPdnS2aPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnS2aPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnS2aPeerAddress_Object = MibTableColumn
tmnxMobPdnS2aPeerAddress = _TmnxMobPdnS2aPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 2),
    _TmnxMobPdnS2aPeerAddress_Type()
)
tmnxMobPdnS2aPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerAddress.setStatus("current")
_TmnxMobPdnS2aPeerPort_Type = InetPortNumber
_TmnxMobPdnS2aPeerPort_Object = MibTableColumn
tmnxMobPdnS2aPeerPort = _TmnxMobPdnS2aPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 3),
    _TmnxMobPdnS2aPeerPort_Type()
)
tmnxMobPdnS2aPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerPort.setStatus("current")
_TmnxMobPdnS2aPeerLastChanged_Type = TimeStamp
_TmnxMobPdnS2aPeerLastChanged_Object = MibTableColumn
tmnxMobPdnS2aPeerLastChanged = _TmnxMobPdnS2aPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 4),
    _TmnxMobPdnS2aPeerLastChanged_Type()
)
tmnxMobPdnS2aPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerLastChanged.setStatus("current")
_TmnxMobPdnS2aPeerCreateTime_Type = TimeStamp
_TmnxMobPdnS2aPeerCreateTime_Object = MibTableColumn
tmnxMobPdnS2aPeerCreateTime = _TmnxMobPdnS2aPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 5),
    _TmnxMobPdnS2aPeerCreateTime_Type()
)
tmnxMobPdnS2aPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerCreateTime.setStatus("current")
_TmnxMobPdnS2aPeerPathMgmtState_Type = TmnxMobPathMgmtState
_TmnxMobPdnS2aPeerPathMgmtState_Object = MibTableColumn
tmnxMobPdnS2aPeerPathMgmtState = _TmnxMobPdnS2aPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 6),
    _TmnxMobPdnS2aPeerPathMgmtState_Type()
)
tmnxMobPdnS2aPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerPathMgmtState.setStatus("current")
_TmnxMobPdnS2aPeerGatewayId_Type = TmnxMobGwId
_TmnxMobPdnS2aPeerGatewayId_Object = MibTableColumn
tmnxMobPdnS2aPeerGatewayId = _TmnxMobPdnS2aPeerGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 7),
    _TmnxMobPdnS2aPeerGatewayId_Type()
)
tmnxMobPdnS2aPeerGatewayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerGatewayId.setStatus("current")
_TmnxMobPdnS2aPeerType_Type = TmnxMobPeerType
_TmnxMobPdnS2aPeerType_Object = MibTableColumn
tmnxMobPdnS2aPeerType = _TmnxMobPdnS2aPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 8),
    _TmnxMobPdnS2aPeerType_Type()
)
tmnxMobPdnS2aPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerType.setStatus("current")
_TmnxMobPdnS2aPeerHBCompatible_Type = TruthValue
_TmnxMobPdnS2aPeerHBCompatible_Object = MibTableColumn
tmnxMobPdnS2aPeerHBCompatible = _TmnxMobPdnS2aPeerHBCompatible_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 19, 1, 9),
    _TmnxMobPdnS2aPeerHBCompatible_Type()
)
tmnxMobPdnS2aPeerHBCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerHBCompatible.setStatus("current")
_TmnxMobPdnS2aStatTable_Object = MibTable
tmnxMobPdnS2aStatTable = _TmnxMobPdnS2aStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatTable.setStatus("current")
_TmnxMobPdnS2aStatEntry_Object = MibTableRow
tmnxMobPdnS2aStatEntry = _TmnxMobPdnS2aStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1)
)
tmnxMobPdnS2aStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatEntry.setStatus("current")
_TmnxMobPdnS2aStatPeerRestart_Type = Counter32
_TmnxMobPdnS2aStatPeerRestart_Object = MibTableColumn
tmnxMobPdnS2aStatPeerRestart = _TmnxMobPdnS2aStatPeerRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 1),
    _TmnxMobPdnS2aStatPeerRestart_Type()
)
tmnxMobPdnS2aStatPeerRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatPeerRestart.setStatus("current")
_TmnxMobPdnS2aStatPathMgmtFail_Type = Counter32
_TmnxMobPdnS2aStatPathMgmtFail_Object = MibTableColumn
tmnxMobPdnS2aStatPathMgmtFail = _TmnxMobPdnS2aStatPathMgmtFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 2),
    _TmnxMobPdnS2aStatPathMgmtFail_Type()
)
tmnxMobPdnS2aStatPathMgmtFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatPathMgmtFail.setStatus("current")
_TmnxMobPdnS2aStatPeerRestartCnt_Type = Counter32
_TmnxMobPdnS2aStatPeerRestartCnt_Object = MibTableColumn
tmnxMobPdnS2aStatPeerRestartCnt = _TmnxMobPdnS2aStatPeerRestartCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 3),
    _TmnxMobPdnS2aStatPeerRestartCnt_Type()
)
tmnxMobPdnS2aStatPeerRestartCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatPeerRestartCnt.setStatus("current")
_TmnxMobPdnS2aStatHeartBeatReqTx_Type = Counter32
_TmnxMobPdnS2aStatHeartBeatReqTx_Object = MibTableColumn
tmnxMobPdnS2aStatHeartBeatReqTx = _TmnxMobPdnS2aStatHeartBeatReqTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 4),
    _TmnxMobPdnS2aStatHeartBeatReqTx_Type()
)
tmnxMobPdnS2aStatHeartBeatReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatHeartBeatReqTx.setStatus("current")
_TmnxMobPdnS2aStatHeartBeatReqRx_Type = Counter32
_TmnxMobPdnS2aStatHeartBeatReqRx_Object = MibTableColumn
tmnxMobPdnS2aStatHeartBeatReqRx = _TmnxMobPdnS2aStatHeartBeatReqRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 5),
    _TmnxMobPdnS2aStatHeartBeatReqRx_Type()
)
tmnxMobPdnS2aStatHeartBeatReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatHeartBeatReqRx.setStatus("current")
_TmnxMobPdnS2aStatHeartBeatRespTx_Type = Counter32
_TmnxMobPdnS2aStatHeartBeatRespTx_Object = MibTableColumn
tmnxMobPdnS2aStatHeartBeatRespTx = _TmnxMobPdnS2aStatHeartBeatRespTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 6),
    _TmnxMobPdnS2aStatHeartBeatRespTx_Type()
)
tmnxMobPdnS2aStatHeartBeatRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatHeartBeatRespTx.setStatus("current")
_TmnxMobPdnS2aStatHeartBeatRespRx_Type = Counter32
_TmnxMobPdnS2aStatHeartBeatRespRx_Object = MibTableColumn
tmnxMobPdnS2aStatHeartBeatRespRx = _TmnxMobPdnS2aStatHeartBeatRespRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 7),
    _TmnxMobPdnS2aStatHeartBeatRespRx_Type()
)
tmnxMobPdnS2aStatHeartBeatRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatHeartBeatRespRx.setStatus("current")
_TmnxMobPdnS2aStatPbu_Type = Counter32
_TmnxMobPdnS2aStatPbu_Object = MibTableColumn
tmnxMobPdnS2aStatPbu = _TmnxMobPdnS2aStatPbu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 8),
    _TmnxMobPdnS2aStatPbu_Type()
)
tmnxMobPdnS2aStatPbu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatPbu.setStatus("current")
_TmnxMobPdnS2aStatBri_Type = Counter32
_TmnxMobPdnS2aStatBri_Object = MibTableColumn
tmnxMobPdnS2aStatBri = _TmnxMobPdnS2aStatBri_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 9),
    _TmnxMobPdnS2aStatBri_Type()
)
tmnxMobPdnS2aStatBri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatBri.setStatus("current")
_TmnxMobPdnS2aStatRxMalformedPkts_Type = Counter32
_TmnxMobPdnS2aStatRxMalformedPkts_Object = MibTableColumn
tmnxMobPdnS2aStatRxMalformedPkts = _TmnxMobPdnS2aStatRxMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 10),
    _TmnxMobPdnS2aStatRxMalformedPkts_Type()
)
tmnxMobPdnS2aStatRxMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatRxMalformedPkts.setStatus("current")
_TmnxMobPdnS2aStatRxMissingIePkts_Type = Counter32
_TmnxMobPdnS2aStatRxMissingIePkts_Object = MibTableColumn
tmnxMobPdnS2aStatRxMissingIePkts = _TmnxMobPdnS2aStatRxMissingIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 11),
    _TmnxMobPdnS2aStatRxMissingIePkts_Type()
)
tmnxMobPdnS2aStatRxMissingIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatRxMissingIePkts.setStatus("current")
_TmnxMobPdnS2aStatRxUnknownPkts_Type = Counter32
_TmnxMobPdnS2aStatRxUnknownPkts_Object = MibTableColumn
tmnxMobPdnS2aStatRxUnknownPkts = _TmnxMobPdnS2aStatRxUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 12),
    _TmnxMobPdnS2aStatRxUnknownPkts_Type()
)
tmnxMobPdnS2aStatRxUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatRxUnknownPkts.setStatus("current")
_TmnxMobPdnS2aStatPbaFailure_Type = Counter32
_TmnxMobPdnS2aStatPbaFailure_Object = MibTableColumn
tmnxMobPdnS2aStatPbaFailure = _TmnxMobPdnS2aStatPbaFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 13),
    _TmnxMobPdnS2aStatPbaFailure_Type()
)
tmnxMobPdnS2aStatPbaFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatPbaFailure.setStatus("current")
_TmnxMobPdnS2aStatBraFailure_Type = Counter32
_TmnxMobPdnS2aStatBraFailure_Object = MibTableColumn
tmnxMobPdnS2aStatBraFailure = _TmnxMobPdnS2aStatBraFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 14),
    _TmnxMobPdnS2aStatBraFailure_Type()
)
tmnxMobPdnS2aStatBraFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatBraFailure.setStatus("current")
_TmnxMobPdnS2aStatPbaSuccess_Type = Counter32
_TmnxMobPdnS2aStatPbaSuccess_Object = MibTableColumn
tmnxMobPdnS2aStatPbaSuccess = _TmnxMobPdnS2aStatPbaSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 15),
    _TmnxMobPdnS2aStatPbaSuccess_Type()
)
tmnxMobPdnS2aStatPbaSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatPbaSuccess.setStatus("current")
_TmnxMobPdnS2aStatBraSuccess_Type = Counter32
_TmnxMobPdnS2aStatBraSuccess_Object = MibTableColumn
tmnxMobPdnS2aStatBraSuccess = _TmnxMobPdnS2aStatBraSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 16),
    _TmnxMobPdnS2aStatBraSuccess_Type()
)
tmnxMobPdnS2aStatBraSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatBraSuccess.setStatus("current")
_TmnxMobPdnS2aStatHBCompatible_Type = TruthValue
_TmnxMobPdnS2aStatHBCompatible_Object = MibTableColumn
tmnxMobPdnS2aStatHBCompatible = _TmnxMobPdnS2aStatHBCompatible_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 20, 1, 17),
    _TmnxMobPdnS2aStatHBCompatible_Type()
)
tmnxMobPdnS2aStatHBCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aStatHBCompatible.setStatus("current")
_TmnxMobPdnBcAcctGaTable_Object = MibTable
tmnxMobPdnBcAcctGaTable = _TmnxMobPdnBcAcctGaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaTable.setStatus("current")
_TmnxMobPdnBcAcctGaEntry_Object = MibTableRow
tmnxMobPdnBcAcctGaEntry = _TmnxMobPdnBcAcctGaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaEntry.setStatus("current")
_TmnxMobPdnBcAcctGaChargingId_Type = TmnxMobChargingProfile
_TmnxMobPdnBcAcctGaChargingId_Object = MibTableColumn
tmnxMobPdnBcAcctGaChargingId = _TmnxMobPdnBcAcctGaChargingId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 1),
    _TmnxMobPdnBcAcctGaChargingId_Type()
)
tmnxMobPdnBcAcctGaChargingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaChargingId.setStatus("current")
_TmnxMobPdnBcAcctGaUlSustRate_Type = Counter32
_TmnxMobPdnBcAcctGaUlSustRate_Object = MibTableColumn
tmnxMobPdnBcAcctGaUlSustRate = _TmnxMobPdnBcAcctGaUlSustRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 2),
    _TmnxMobPdnBcAcctGaUlSustRate_Type()
)
tmnxMobPdnBcAcctGaUlSustRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaUlSustRate.setStatus("current")
_TmnxMobPdnBcAcctGaDlSustRate_Type = Counter32
_TmnxMobPdnBcAcctGaDlSustRate_Object = MibTableColumn
tmnxMobPdnBcAcctGaDlSustRate = _TmnxMobPdnBcAcctGaDlSustRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 3),
    _TmnxMobPdnBcAcctGaDlSustRate_Type()
)
tmnxMobPdnBcAcctGaDlSustRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaDlSustRate.setStatus("current")
_TmnxMobPdnBcAcctGaAggrUlPkts_Type = Counter64
_TmnxMobPdnBcAcctGaAggrUlPkts_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrUlPkts = _TmnxMobPdnBcAcctGaAggrUlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 4),
    _TmnxMobPdnBcAcctGaAggrUlPkts_Type()
)
tmnxMobPdnBcAcctGaAggrUlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrUlPkts.setStatus("current")
_TmnxMobPdnBcAcctGaAggrUlPktsLow_Type = Counter32
_TmnxMobPdnBcAcctGaAggrUlPktsLow_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrUlPktsLow = _TmnxMobPdnBcAcctGaAggrUlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 5),
    _TmnxMobPdnBcAcctGaAggrUlPktsLow_Type()
)
tmnxMobPdnBcAcctGaAggrUlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrUlPktsLow.setStatus("current")
_TmnxMobPdnBcAcctGaAggrUlPktsHigh_Type = Counter32
_TmnxMobPdnBcAcctGaAggrUlPktsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrUlPktsHigh = _TmnxMobPdnBcAcctGaAggrUlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 6),
    _TmnxMobPdnBcAcctGaAggrUlPktsHigh_Type()
)
tmnxMobPdnBcAcctGaAggrUlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrUlPktsHigh.setStatus("current")
_TmnxMobPdnBcAcctGaAggrDlPkts_Type = Counter64
_TmnxMobPdnBcAcctGaAggrDlPkts_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrDlPkts = _TmnxMobPdnBcAcctGaAggrDlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 7),
    _TmnxMobPdnBcAcctGaAggrDlPkts_Type()
)
tmnxMobPdnBcAcctGaAggrDlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrDlPkts.setStatus("current")
_TmnxMobPdnBcAcctGaAggrDlPktsLow_Type = Counter32
_TmnxMobPdnBcAcctGaAggrDlPktsLow_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrDlPktsLow = _TmnxMobPdnBcAcctGaAggrDlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 8),
    _TmnxMobPdnBcAcctGaAggrDlPktsLow_Type()
)
tmnxMobPdnBcAcctGaAggrDlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrDlPktsLow.setStatus("current")
_TmnxMobPdnBcAcctGaAggrDlPktsHigh_Type = Counter32
_TmnxMobPdnBcAcctGaAggrDlPktsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrDlPktsHigh = _TmnxMobPdnBcAcctGaAggrDlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 9),
    _TmnxMobPdnBcAcctGaAggrDlPktsHigh_Type()
)
tmnxMobPdnBcAcctGaAggrDlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrDlPktsHigh.setStatus("current")
_TmnxMobPdnBcAcctGaAggrUlByts_Type = Counter64
_TmnxMobPdnBcAcctGaAggrUlByts_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrUlByts = _TmnxMobPdnBcAcctGaAggrUlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 10),
    _TmnxMobPdnBcAcctGaAggrUlByts_Type()
)
tmnxMobPdnBcAcctGaAggrUlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrUlByts.setStatus("current")
_TmnxMobPdnBcAcctGaAggrUlBytsLow_Type = Counter32
_TmnxMobPdnBcAcctGaAggrUlBytsLow_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrUlBytsLow = _TmnxMobPdnBcAcctGaAggrUlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 11),
    _TmnxMobPdnBcAcctGaAggrUlBytsLow_Type()
)
tmnxMobPdnBcAcctGaAggrUlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrUlBytsLow.setStatus("current")
_TmnxMobPdnBcAcctGaAggrUlBytsHigh_Type = Counter32
_TmnxMobPdnBcAcctGaAggrUlBytsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrUlBytsHigh = _TmnxMobPdnBcAcctGaAggrUlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 12),
    _TmnxMobPdnBcAcctGaAggrUlBytsHigh_Type()
)
tmnxMobPdnBcAcctGaAggrUlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrUlBytsHigh.setStatus("current")
_TmnxMobPdnBcAcctGaAggrDlByts_Type = Counter64
_TmnxMobPdnBcAcctGaAggrDlByts_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrDlByts = _TmnxMobPdnBcAcctGaAggrDlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 13),
    _TmnxMobPdnBcAcctGaAggrDlByts_Type()
)
tmnxMobPdnBcAcctGaAggrDlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrDlByts.setStatus("current")
_TmnxMobPdnBcAcctGaAggrDlBytsLow_Type = Counter32
_TmnxMobPdnBcAcctGaAggrDlBytsLow_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrDlBytsLow = _TmnxMobPdnBcAcctGaAggrDlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 14),
    _TmnxMobPdnBcAcctGaAggrDlBytsLow_Type()
)
tmnxMobPdnBcAcctGaAggrDlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrDlBytsLow.setStatus("current")
_TmnxMobPdnBcAcctGaAggrDlBytsHigh_Type = Counter32
_TmnxMobPdnBcAcctGaAggrDlBytsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctGaAggrDlBytsHigh = _TmnxMobPdnBcAcctGaAggrDlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 15),
    _TmnxMobPdnBcAcctGaAggrDlBytsHigh_Type()
)
tmnxMobPdnBcAcctGaAggrDlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaAggrDlBytsHigh.setStatus("current")
_TmnxMobPdnBcAcctGaNumPartCdrs_Type = Counter32
_TmnxMobPdnBcAcctGaNumPartCdrs_Object = MibTableColumn
tmnxMobPdnBcAcctGaNumPartCdrs = _TmnxMobPdnBcAcctGaNumPartCdrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 16),
    _TmnxMobPdnBcAcctGaNumPartCdrs_Type()
)
tmnxMobPdnBcAcctGaNumPartCdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaNumPartCdrs.setStatus("current")
_TmnxMobPdnBcAcctGaNumContainers_Type = Counter32
_TmnxMobPdnBcAcctGaNumContainers_Object = MibTableColumn
tmnxMobPdnBcAcctGaNumContainers = _TmnxMobPdnBcAcctGaNumContainers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 17),
    _TmnxMobPdnBcAcctGaNumContainers_Type()
)
tmnxMobPdnBcAcctGaNumContainers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaNumContainers.setStatus("current")
_TmnxMobPdnBcAcctGaNumMaxChanges_Type = Counter32
_TmnxMobPdnBcAcctGaNumMaxChanges_Object = MibTableColumn
tmnxMobPdnBcAcctGaNumMaxChanges = _TmnxMobPdnBcAcctGaNumMaxChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 18),
    _TmnxMobPdnBcAcctGaNumMaxChanges_Type()
)
tmnxMobPdnBcAcctGaNumMaxChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaNumMaxChanges.setStatus("current")
_TmnxMobPdnBcAcctGaNumRgs_Type = Counter32
_TmnxMobPdnBcAcctGaNumRgs_Object = MibTableColumn
tmnxMobPdnBcAcctGaNumRgs = _TmnxMobPdnBcAcctGaNumRgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 19),
    _TmnxMobPdnBcAcctGaNumRgs_Type()
)
tmnxMobPdnBcAcctGaNumRgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaNumRgs.setStatus("current")
_TmnxMobPdnBcAcctGaNumOfRgSvcId_Type = Counter32
_TmnxMobPdnBcAcctGaNumOfRgSvcId_Object = MibTableColumn
tmnxMobPdnBcAcctGaNumOfRgSvcId = _TmnxMobPdnBcAcctGaNumOfRgSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 21, 1, 20),
    _TmnxMobPdnBcAcctGaNumOfRgSvcId_Type()
)
tmnxMobPdnBcAcctGaNumOfRgSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGaNumOfRgSvcId.setStatus("current")
_TmnxMobPdnBcGaChrgTable_Object = MibTable
tmnxMobPdnBcGaChrgTable = _TmnxMobPdnBcGaChrgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgTable.setStatus("current")
_TmnxMobPdnBcGaChrgEntry_Object = MibTableRow
tmnxMobPdnBcGaChrgEntry = _TmnxMobPdnBcGaChrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1)
)
tmnxMobPdnBcGaChrgEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsi"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcApn"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPdnType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcBearerId"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitRatingGroup"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitServIdentifier"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgEntry.setStatus("current")
_TmnxMobPdnBcGaChrgOnlnCharging_Type = TruthValue
_TmnxMobPdnBcGaChrgOnlnCharging_Object = MibTableColumn
tmnxMobPdnBcGaChrgOnlnCharging = _TmnxMobPdnBcGaChrgOnlnCharging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 1),
    _TmnxMobPdnBcGaChrgOnlnCharging_Type()
)
tmnxMobPdnBcGaChrgOnlnCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgOnlnCharging.setStatus("current")
_TmnxMobPdnBcGaChrgOfflnCharging_Type = TruthValue
_TmnxMobPdnBcGaChrgOfflnCharging_Object = MibTableColumn
tmnxMobPdnBcGaChrgOfflnCharging = _TmnxMobPdnBcGaChrgOfflnCharging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 2),
    _TmnxMobPdnBcGaChrgOfflnCharging_Type()
)
tmnxMobPdnBcGaChrgOfflnCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgOfflnCharging.setStatus("current")
_TmnxMobPdnBcGaChrgUlPkts_Type = Counter64
_TmnxMobPdnBcGaChrgUlPkts_Object = MibTableColumn
tmnxMobPdnBcGaChrgUlPkts = _TmnxMobPdnBcGaChrgUlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 3),
    _TmnxMobPdnBcGaChrgUlPkts_Type()
)
tmnxMobPdnBcGaChrgUlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgUlPkts.setStatus("current")
_TmnxMobPdnBcGaChrgUlPktsLow_Type = Counter32
_TmnxMobPdnBcGaChrgUlPktsLow_Object = MibTableColumn
tmnxMobPdnBcGaChrgUlPktsLow = _TmnxMobPdnBcGaChrgUlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 4),
    _TmnxMobPdnBcGaChrgUlPktsLow_Type()
)
tmnxMobPdnBcGaChrgUlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgUlPktsLow.setStatus("current")
_TmnxMobPdnBcGaChrgUlPktsHigh_Type = Counter32
_TmnxMobPdnBcGaChrgUlPktsHigh_Object = MibTableColumn
tmnxMobPdnBcGaChrgUlPktsHigh = _TmnxMobPdnBcGaChrgUlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 5),
    _TmnxMobPdnBcGaChrgUlPktsHigh_Type()
)
tmnxMobPdnBcGaChrgUlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgUlPktsHigh.setStatus("current")
_TmnxMobPdnBcGaChrgDlPkts_Type = Counter64
_TmnxMobPdnBcGaChrgDlPkts_Object = MibTableColumn
tmnxMobPdnBcGaChrgDlPkts = _TmnxMobPdnBcGaChrgDlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 6),
    _TmnxMobPdnBcGaChrgDlPkts_Type()
)
tmnxMobPdnBcGaChrgDlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgDlPkts.setStatus("current")
_TmnxMobPdnBcGaChrgDlPktsLow_Type = Counter32
_TmnxMobPdnBcGaChrgDlPktsLow_Object = MibTableColumn
tmnxMobPdnBcGaChrgDlPktsLow = _TmnxMobPdnBcGaChrgDlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 7),
    _TmnxMobPdnBcGaChrgDlPktsLow_Type()
)
tmnxMobPdnBcGaChrgDlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgDlPktsLow.setStatus("current")
_TmnxMobPdnBcGaChrgDlPktsHigh_Type = Counter32
_TmnxMobPdnBcGaChrgDlPktsHigh_Object = MibTableColumn
tmnxMobPdnBcGaChrgDlPktsHigh = _TmnxMobPdnBcGaChrgDlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 8),
    _TmnxMobPdnBcGaChrgDlPktsHigh_Type()
)
tmnxMobPdnBcGaChrgDlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgDlPktsHigh.setStatus("current")
_TmnxMobPdnBcGaChrgUlByts_Type = Counter64
_TmnxMobPdnBcGaChrgUlByts_Object = MibTableColumn
tmnxMobPdnBcGaChrgUlByts = _TmnxMobPdnBcGaChrgUlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 9),
    _TmnxMobPdnBcGaChrgUlByts_Type()
)
tmnxMobPdnBcGaChrgUlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgUlByts.setStatus("current")
_TmnxMobPdnBcGaChrgUlBytsLow_Type = Counter32
_TmnxMobPdnBcGaChrgUlBytsLow_Object = MibTableColumn
tmnxMobPdnBcGaChrgUlBytsLow = _TmnxMobPdnBcGaChrgUlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 10),
    _TmnxMobPdnBcGaChrgUlBytsLow_Type()
)
tmnxMobPdnBcGaChrgUlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgUlBytsLow.setStatus("current")
_TmnxMobPdnBcGaChrgUlBytsHigh_Type = Counter32
_TmnxMobPdnBcGaChrgUlBytsHigh_Object = MibTableColumn
tmnxMobPdnBcGaChrgUlBytsHigh = _TmnxMobPdnBcGaChrgUlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 11),
    _TmnxMobPdnBcGaChrgUlBytsHigh_Type()
)
tmnxMobPdnBcGaChrgUlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgUlBytsHigh.setStatus("current")
_TmnxMobPdnBcGaChrgDlByts_Type = Counter64
_TmnxMobPdnBcGaChrgDlByts_Object = MibTableColumn
tmnxMobPdnBcGaChrgDlByts = _TmnxMobPdnBcGaChrgDlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 12),
    _TmnxMobPdnBcGaChrgDlByts_Type()
)
tmnxMobPdnBcGaChrgDlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgDlByts.setStatus("current")
_TmnxMobPdnBcGaChrgDlBytsLow_Type = Counter32
_TmnxMobPdnBcGaChrgDlBytsLow_Object = MibTableColumn
tmnxMobPdnBcGaChrgDlBytsLow = _TmnxMobPdnBcGaChrgDlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 13),
    _TmnxMobPdnBcGaChrgDlBytsLow_Type()
)
tmnxMobPdnBcGaChrgDlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgDlBytsLow.setStatus("current")
_TmnxMobPdnBcGaChrgDlBytsHigh_Type = Counter32
_TmnxMobPdnBcGaChrgDlBytsHigh_Object = MibTableColumn
tmnxMobPdnBcGaChrgDlBytsHigh = _TmnxMobPdnBcGaChrgDlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 22, 1, 14),
    _TmnxMobPdnBcGaChrgDlBytsHigh_Type()
)
tmnxMobPdnBcGaChrgDlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGaChrgDlBytsHigh.setStatus("current")
_TmnxMobPdnBcAcctGyTable_Object = MibTable
tmnxMobPdnBcAcctGyTable = _TmnxMobPdnBcAcctGyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyTable.setStatus("current")
_TmnxMobPdnBcAcctGyEntry_Object = MibTableRow
tmnxMobPdnBcAcctGyEntry = _TmnxMobPdnBcAcctGyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyEntry.setStatus("current")
_TmnxMobPdnBcAcctGyChargingId_Type = TmnxMobChargingProfile
_TmnxMobPdnBcAcctGyChargingId_Object = MibTableColumn
tmnxMobPdnBcAcctGyChargingId = _TmnxMobPdnBcAcctGyChargingId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 1),
    _TmnxMobPdnBcAcctGyChargingId_Type()
)
tmnxMobPdnBcAcctGyChargingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyChargingId.setStatus("current")
_TmnxMobPdnBcAcctGyUlSustRate_Type = Counter32
_TmnxMobPdnBcAcctGyUlSustRate_Object = MibTableColumn
tmnxMobPdnBcAcctGyUlSustRate = _TmnxMobPdnBcAcctGyUlSustRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 2),
    _TmnxMobPdnBcAcctGyUlSustRate_Type()
)
tmnxMobPdnBcAcctGyUlSustRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyUlSustRate.setStatus("current")
_TmnxMobPdnBcAcctGyDlSustRate_Type = Counter32
_TmnxMobPdnBcAcctGyDlSustRate_Object = MibTableColumn
tmnxMobPdnBcAcctGyDlSustRate = _TmnxMobPdnBcAcctGyDlSustRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 3),
    _TmnxMobPdnBcAcctGyDlSustRate_Type()
)
tmnxMobPdnBcAcctGyDlSustRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyDlSustRate.setStatus("current")
_TmnxMobPdnBcAcctGyAggrUlPkts_Type = Counter64
_TmnxMobPdnBcAcctGyAggrUlPkts_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrUlPkts = _TmnxMobPdnBcAcctGyAggrUlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 4),
    _TmnxMobPdnBcAcctGyAggrUlPkts_Type()
)
tmnxMobPdnBcAcctGyAggrUlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrUlPkts.setStatus("current")
_TmnxMobPdnBcAcctGyAggrUlPktsLow_Type = Counter32
_TmnxMobPdnBcAcctGyAggrUlPktsLow_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrUlPktsLow = _TmnxMobPdnBcAcctGyAggrUlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 5),
    _TmnxMobPdnBcAcctGyAggrUlPktsLow_Type()
)
tmnxMobPdnBcAcctGyAggrUlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrUlPktsLow.setStatus("current")
_TmnxMobPdnBcAcctGyAggrUlPktsHigh_Type = Counter32
_TmnxMobPdnBcAcctGyAggrUlPktsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrUlPktsHigh = _TmnxMobPdnBcAcctGyAggrUlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 6),
    _TmnxMobPdnBcAcctGyAggrUlPktsHigh_Type()
)
tmnxMobPdnBcAcctGyAggrUlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrUlPktsHigh.setStatus("current")
_TmnxMobPdnBcAcctGyAggrDlPkts_Type = Counter64
_TmnxMobPdnBcAcctGyAggrDlPkts_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrDlPkts = _TmnxMobPdnBcAcctGyAggrDlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 7),
    _TmnxMobPdnBcAcctGyAggrDlPkts_Type()
)
tmnxMobPdnBcAcctGyAggrDlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrDlPkts.setStatus("current")
_TmnxMobPdnBcAcctGyAggrDlPktsLow_Type = Counter32
_TmnxMobPdnBcAcctGyAggrDlPktsLow_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrDlPktsLow = _TmnxMobPdnBcAcctGyAggrDlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 8),
    _TmnxMobPdnBcAcctGyAggrDlPktsLow_Type()
)
tmnxMobPdnBcAcctGyAggrDlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrDlPktsLow.setStatus("current")
_TmnxMobPdnBcAcctGyAggrDlPktsHigh_Type = Counter32
_TmnxMobPdnBcAcctGyAggrDlPktsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrDlPktsHigh = _TmnxMobPdnBcAcctGyAggrDlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 9),
    _TmnxMobPdnBcAcctGyAggrDlPktsHigh_Type()
)
tmnxMobPdnBcAcctGyAggrDlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrDlPktsHigh.setStatus("current")
_TmnxMobPdnBcAcctGyAggrUlByts_Type = Counter64
_TmnxMobPdnBcAcctGyAggrUlByts_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrUlByts = _TmnxMobPdnBcAcctGyAggrUlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 10),
    _TmnxMobPdnBcAcctGyAggrUlByts_Type()
)
tmnxMobPdnBcAcctGyAggrUlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrUlByts.setStatus("current")
_TmnxMobPdnBcAcctGyAggrUlBytsLow_Type = Counter32
_TmnxMobPdnBcAcctGyAggrUlBytsLow_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrUlBytsLow = _TmnxMobPdnBcAcctGyAggrUlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 11),
    _TmnxMobPdnBcAcctGyAggrUlBytsLow_Type()
)
tmnxMobPdnBcAcctGyAggrUlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrUlBytsLow.setStatus("current")
_TmnxMobPdnBcAcctGyAggrUlBytsHigh_Type = Counter32
_TmnxMobPdnBcAcctGyAggrUlBytsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrUlBytsHigh = _TmnxMobPdnBcAcctGyAggrUlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 12),
    _TmnxMobPdnBcAcctGyAggrUlBytsHigh_Type()
)
tmnxMobPdnBcAcctGyAggrUlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrUlBytsHigh.setStatus("current")
_TmnxMobPdnBcAcctGyAggrDlByts_Type = Counter64
_TmnxMobPdnBcAcctGyAggrDlByts_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrDlByts = _TmnxMobPdnBcAcctGyAggrDlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 13),
    _TmnxMobPdnBcAcctGyAggrDlByts_Type()
)
tmnxMobPdnBcAcctGyAggrDlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrDlByts.setStatus("current")
_TmnxMobPdnBcAcctGyAggrDlBytsLow_Type = Counter32
_TmnxMobPdnBcAcctGyAggrDlBytsLow_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrDlBytsLow = _TmnxMobPdnBcAcctGyAggrDlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 14),
    _TmnxMobPdnBcAcctGyAggrDlBytsLow_Type()
)
tmnxMobPdnBcAcctGyAggrDlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrDlBytsLow.setStatus("current")
_TmnxMobPdnBcAcctGyAggrDlBytsHigh_Type = Counter32
_TmnxMobPdnBcAcctGyAggrDlBytsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctGyAggrDlBytsHigh = _TmnxMobPdnBcAcctGyAggrDlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 15),
    _TmnxMobPdnBcAcctGyAggrDlBytsHigh_Type()
)
tmnxMobPdnBcAcctGyAggrDlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyAggrDlBytsHigh.setStatus("current")
_TmnxMobPdnBcAcctGyNumRedirection_Type = Counter32
_TmnxMobPdnBcAcctGyNumRedirection_Object = MibTableColumn
tmnxMobPdnBcAcctGyNumRedirection = _TmnxMobPdnBcAcctGyNumRedirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 16),
    _TmnxMobPdnBcAcctGyNumRedirection_Type()
)
tmnxMobPdnBcAcctGyNumRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyNumRedirection.setStatus("current")
_TmnxMobPdnBcAcctGyLastRedctTime_Type = TimeStamp
_TmnxMobPdnBcAcctGyLastRedctTime_Object = MibTableColumn
tmnxMobPdnBcAcctGyLastRedctTime = _TmnxMobPdnBcAcctGyLastRedctTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 17),
    _TmnxMobPdnBcAcctGyLastRedctTime_Type()
)
tmnxMobPdnBcAcctGyLastRedctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyLastRedctTime.setStatus("current")
_TmnxMobPdnBcAcctGyNumCreditsRepl_Type = Counter32
_TmnxMobPdnBcAcctGyNumCreditsRepl_Object = MibTableColumn
tmnxMobPdnBcAcctGyNumCreditsRepl = _TmnxMobPdnBcAcctGyNumCreditsRepl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 18),
    _TmnxMobPdnBcAcctGyNumCreditsRepl_Type()
)
tmnxMobPdnBcAcctGyNumCreditsRepl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyNumCreditsRepl.setStatus("current")
_TmnxMobPdnBcAcctGyLstCrdReplTime_Type = TimeStamp
_TmnxMobPdnBcAcctGyLstCrdReplTime_Object = MibTableColumn
tmnxMobPdnBcAcctGyLstCrdReplTime = _TmnxMobPdnBcAcctGyLstCrdReplTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 19),
    _TmnxMobPdnBcAcctGyLstCrdReplTime_Type()
)
tmnxMobPdnBcAcctGyLstCrdReplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyLstCrdReplTime.setStatus("current")
_TmnxMobPdnBcAcctGyNumRgs_Type = Counter32
_TmnxMobPdnBcAcctGyNumRgs_Object = MibTableColumn
tmnxMobPdnBcAcctGyNumRgs = _TmnxMobPdnBcAcctGyNumRgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 20),
    _TmnxMobPdnBcAcctGyNumRgs_Type()
)
tmnxMobPdnBcAcctGyNumRgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyNumRgs.setStatus("current")
_TmnxMobPdnBcAcctGyNumOfRgSvcId_Type = Counter32
_TmnxMobPdnBcAcctGyNumOfRgSvcId_Object = MibTableColumn
tmnxMobPdnBcAcctGyNumOfRgSvcId = _TmnxMobPdnBcAcctGyNumOfRgSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 23, 1, 21),
    _TmnxMobPdnBcAcctGyNumOfRgSvcId_Type()
)
tmnxMobPdnBcAcctGyNumOfRgSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctGyNumOfRgSvcId.setStatus("current")
_TmnxMobPdnBcGyChrgTable_Object = MibTable
tmnxMobPdnBcGyChrgTable = _TmnxMobPdnBcGyChrgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTable.setStatus("current")
_TmnxMobPdnBcGyChrgEntry_Object = MibTableRow
tmnxMobPdnBcGyChrgEntry = _TmnxMobPdnBcGyChrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1)
)
tmnxMobPdnBcGyChrgEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsi"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcApn"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPdnType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcBearerId"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitRatingGroup"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitServIdentifier"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgEntry.setStatus("current")
_TmnxMobPdnBcGyChrgTimeGranted_Type = TimeStamp
_TmnxMobPdnBcGyChrgTimeGranted_Object = MibTableColumn
tmnxMobPdnBcGyChrgTimeGranted = _TmnxMobPdnBcGyChrgTimeGranted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 1),
    _TmnxMobPdnBcGyChrgTimeGranted_Type()
)
tmnxMobPdnBcGyChrgTimeGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTimeGranted.setStatus("current")
_TmnxMobPdnBcGyChrgTimeUsed_Type = TimeStamp
_TmnxMobPdnBcGyChrgTimeUsed_Object = MibTableColumn
tmnxMobPdnBcGyChrgTimeUsed = _TmnxMobPdnBcGyChrgTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 2),
    _TmnxMobPdnBcGyChrgTimeUsed_Type()
)
tmnxMobPdnBcGyChrgTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTimeUsed.setStatus("current")
_TmnxMobPdnBcGyChrgGrntTtlOct_Type = Counter64
_TmnxMobPdnBcGyChrgGrntTtlOct_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntTtlOct = _TmnxMobPdnBcGyChrgGrntTtlOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 3),
    _TmnxMobPdnBcGyChrgGrntTtlOct_Type()
)
tmnxMobPdnBcGyChrgGrntTtlOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntTtlOct.setStatus("current")
_TmnxMobPdnBcGyChrgGrntTtlOctLow_Type = Counter32
_TmnxMobPdnBcGyChrgGrntTtlOctLow_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntTtlOctLow = _TmnxMobPdnBcGyChrgGrntTtlOctLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 4),
    _TmnxMobPdnBcGyChrgGrntTtlOctLow_Type()
)
tmnxMobPdnBcGyChrgGrntTtlOctLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntTtlOctLow.setStatus("current")
_TmnxMobPdnBcGyChrgGrntTtlOctHigh_Type = Counter32
_TmnxMobPdnBcGyChrgGrntTtlOctHigh_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntTtlOctHigh = _TmnxMobPdnBcGyChrgGrntTtlOctHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 5),
    _TmnxMobPdnBcGyChrgGrntTtlOctHigh_Type()
)
tmnxMobPdnBcGyChrgGrntTtlOctHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntTtlOctHigh.setStatus("current")
_TmnxMobPdnBcGyChrgGrntInOct_Type = Counter64
_TmnxMobPdnBcGyChrgGrntInOct_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntInOct = _TmnxMobPdnBcGyChrgGrntInOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 6),
    _TmnxMobPdnBcGyChrgGrntInOct_Type()
)
tmnxMobPdnBcGyChrgGrntInOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntInOct.setStatus("current")
_TmnxMobPdnBcGyChrgGrntInOctLow_Type = Counter32
_TmnxMobPdnBcGyChrgGrntInOctLow_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntInOctLow = _TmnxMobPdnBcGyChrgGrntInOctLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 7),
    _TmnxMobPdnBcGyChrgGrntInOctLow_Type()
)
tmnxMobPdnBcGyChrgGrntInOctLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntInOctLow.setStatus("current")
_TmnxMobPdnBcGyChrgGrntInOctHigh_Type = Counter32
_TmnxMobPdnBcGyChrgGrntInOctHigh_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntInOctHigh = _TmnxMobPdnBcGyChrgGrntInOctHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 8),
    _TmnxMobPdnBcGyChrgGrntInOctHigh_Type()
)
tmnxMobPdnBcGyChrgGrntInOctHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntInOctHigh.setStatus("current")
_TmnxMobPdnBcGyChrgGrntOutOct_Type = Counter64
_TmnxMobPdnBcGyChrgGrntOutOct_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntOutOct = _TmnxMobPdnBcGyChrgGrntOutOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 9),
    _TmnxMobPdnBcGyChrgGrntOutOct_Type()
)
tmnxMobPdnBcGyChrgGrntOutOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntOutOct.setStatus("current")
_TmnxMobPdnBcGyChrgGrntOutOctLow_Type = Counter32
_TmnxMobPdnBcGyChrgGrntOutOctLow_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntOutOctLow = _TmnxMobPdnBcGyChrgGrntOutOctLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 10),
    _TmnxMobPdnBcGyChrgGrntOutOctLow_Type()
)
tmnxMobPdnBcGyChrgGrntOutOctLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntOutOctLow.setStatus("current")
_TmnxMobPdnBcGyChrgGrntOutOctHigh_Type = Counter32
_TmnxMobPdnBcGyChrgGrntOutOctHigh_Object = MibTableColumn
tmnxMobPdnBcGyChrgGrntOutOctHigh = _TmnxMobPdnBcGyChrgGrntOutOctHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 11),
    _TmnxMobPdnBcGyChrgGrntOutOctHigh_Type()
)
tmnxMobPdnBcGyChrgGrntOutOctHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgGrntOutOctHigh.setStatus("current")
_TmnxMobPdnBcGyChrgUsedTtlOct_Type = Counter64
_TmnxMobPdnBcGyChrgUsedTtlOct_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedTtlOct = _TmnxMobPdnBcGyChrgUsedTtlOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 12),
    _TmnxMobPdnBcGyChrgUsedTtlOct_Type()
)
tmnxMobPdnBcGyChrgUsedTtlOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedTtlOct.setStatus("current")
_TmnxMobPdnBcGyChrgUsedTtlOctLow_Type = Counter32
_TmnxMobPdnBcGyChrgUsedTtlOctLow_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedTtlOctLow = _TmnxMobPdnBcGyChrgUsedTtlOctLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 13),
    _TmnxMobPdnBcGyChrgUsedTtlOctLow_Type()
)
tmnxMobPdnBcGyChrgUsedTtlOctLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedTtlOctLow.setStatus("current")
_TmnxMobPdnBcGyChrgUsedTtlOctHigh_Type = Counter32
_TmnxMobPdnBcGyChrgUsedTtlOctHigh_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedTtlOctHigh = _TmnxMobPdnBcGyChrgUsedTtlOctHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 14),
    _TmnxMobPdnBcGyChrgUsedTtlOctHigh_Type()
)
tmnxMobPdnBcGyChrgUsedTtlOctHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedTtlOctHigh.setStatus("current")
_TmnxMobPdnBcGyChrgUsedInOct_Type = Counter64
_TmnxMobPdnBcGyChrgUsedInOct_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedInOct = _TmnxMobPdnBcGyChrgUsedInOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 15),
    _TmnxMobPdnBcGyChrgUsedInOct_Type()
)
tmnxMobPdnBcGyChrgUsedInOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedInOct.setStatus("current")
_TmnxMobPdnBcGyChrgUsedInOctLow_Type = Counter32
_TmnxMobPdnBcGyChrgUsedInOctLow_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedInOctLow = _TmnxMobPdnBcGyChrgUsedInOctLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 16),
    _TmnxMobPdnBcGyChrgUsedInOctLow_Type()
)
tmnxMobPdnBcGyChrgUsedInOctLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedInOctLow.setStatus("current")
_TmnxMobPdnBcGyChrgUsedInOctHigh_Type = Counter32
_TmnxMobPdnBcGyChrgUsedInOctHigh_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedInOctHigh = _TmnxMobPdnBcGyChrgUsedInOctHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 17),
    _TmnxMobPdnBcGyChrgUsedInOctHigh_Type()
)
tmnxMobPdnBcGyChrgUsedInOctHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedInOctHigh.setStatus("current")
_TmnxMobPdnBcGyChrgUsedOutOct_Type = Counter64
_TmnxMobPdnBcGyChrgUsedOutOct_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedOutOct = _TmnxMobPdnBcGyChrgUsedOutOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 18),
    _TmnxMobPdnBcGyChrgUsedOutOct_Type()
)
tmnxMobPdnBcGyChrgUsedOutOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedOutOct.setStatus("current")
_TmnxMobPdnBcGyChrgUsedOutOctLow_Type = Counter32
_TmnxMobPdnBcGyChrgUsedOutOctLow_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedOutOctLow = _TmnxMobPdnBcGyChrgUsedOutOctLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 19),
    _TmnxMobPdnBcGyChrgUsedOutOctLow_Type()
)
tmnxMobPdnBcGyChrgUsedOutOctLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedOutOctLow.setStatus("current")
_TmnxMobPdnBcGyChrgUsedOutOctHigh_Type = Counter32
_TmnxMobPdnBcGyChrgUsedOutOctHigh_Object = MibTableColumn
tmnxMobPdnBcGyChrgUsedOutOctHigh = _TmnxMobPdnBcGyChrgUsedOutOctHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 20),
    _TmnxMobPdnBcGyChrgUsedOutOctHigh_Type()
)
tmnxMobPdnBcGyChrgUsedOutOctHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgUsedOutOctHigh.setStatus("current")
_TmnxMobPdnBcGyChrgRatingGrpState_Type = TmnxMobRatingGrpState
_TmnxMobPdnBcGyChrgRatingGrpState_Object = MibTableColumn
tmnxMobPdnBcGyChrgRatingGrpState = _TmnxMobPdnBcGyChrgRatingGrpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 21),
    _TmnxMobPdnBcGyChrgRatingGrpState_Type()
)
tmnxMobPdnBcGyChrgRatingGrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgRatingGrpState.setStatus("current")
_TmnxMobPdnBcGyChrgTimeBasedRep_Type = TmnxEnabledDisabled
_TmnxMobPdnBcGyChrgTimeBasedRep_Object = MibTableColumn
tmnxMobPdnBcGyChrgTimeBasedRep = _TmnxMobPdnBcGyChrgTimeBasedRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 22),
    _TmnxMobPdnBcGyChrgTimeBasedRep_Type()
)
tmnxMobPdnBcGyChrgTimeBasedRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTimeBasedRep.setStatus("current")
_TmnxMobPdnBcGyChrgVolumeBasedRep_Type = TmnxEnabledDisabled
_TmnxMobPdnBcGyChrgVolumeBasedRep_Object = MibTableColumn
tmnxMobPdnBcGyChrgVolumeBasedRep = _TmnxMobPdnBcGyChrgVolumeBasedRep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 23),
    _TmnxMobPdnBcGyChrgVolumeBasedRep_Type()
)
tmnxMobPdnBcGyChrgVolumeBasedRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgVolumeBasedRep.setStatus("current")
_TmnxMobPdnBcGyChrgQctPresent_Type = TmnxMobPresenceState
_TmnxMobPdnBcGyChrgQctPresent_Object = MibTableColumn
tmnxMobPdnBcGyChrgQctPresent = _TmnxMobPdnBcGyChrgQctPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 24),
    _TmnxMobPdnBcGyChrgQctPresent_Type()
)
tmnxMobPdnBcGyChrgQctPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQctPresent.setStatus("current")
_TmnxMobPdnBcGyChrgQctGranted_Type = Unsigned32
_TmnxMobPdnBcGyChrgQctGranted_Object = MibTableColumn
tmnxMobPdnBcGyChrgQctGranted = _TmnxMobPdnBcGyChrgQctGranted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 25),
    _TmnxMobPdnBcGyChrgQctGranted_Type()
)
tmnxMobPdnBcGyChrgQctGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQctGranted.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQctGranted.setUnits("seconds")
_TmnxMobPdnBcGyChrgQhtPresent_Type = TmnxMobPresenceState
_TmnxMobPdnBcGyChrgQhtPresent_Object = MibTableColumn
tmnxMobPdnBcGyChrgQhtPresent = _TmnxMobPdnBcGyChrgQhtPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 26),
    _TmnxMobPdnBcGyChrgQhtPresent_Type()
)
tmnxMobPdnBcGyChrgQhtPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQhtPresent.setStatus("current")
_TmnxMobPdnBcGyChrgQhtGranted_Type = Unsigned32
_TmnxMobPdnBcGyChrgQhtGranted_Object = MibTableColumn
tmnxMobPdnBcGyChrgQhtGranted = _TmnxMobPdnBcGyChrgQhtGranted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 27),
    _TmnxMobPdnBcGyChrgQhtGranted_Type()
)
tmnxMobPdnBcGyChrgQhtGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQhtGranted.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQhtGranted.setUnits("seconds")
_TmnxMobPdnBcGyChrgQhtRemaining_Type = Unsigned32
_TmnxMobPdnBcGyChrgQhtRemaining_Object = MibTableColumn
tmnxMobPdnBcGyChrgQhtRemaining = _TmnxMobPdnBcGyChrgQhtRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 28),
    _TmnxMobPdnBcGyChrgQhtRemaining_Type()
)
tmnxMobPdnBcGyChrgQhtRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQhtRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQhtRemaining.setUnits("seconds")
_TmnxMobPdnBcGyChrgQvtPresent_Type = TmnxMobPresenceState
_TmnxMobPdnBcGyChrgQvtPresent_Object = MibTableColumn
tmnxMobPdnBcGyChrgQvtPresent = _TmnxMobPdnBcGyChrgQvtPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 29),
    _TmnxMobPdnBcGyChrgQvtPresent_Type()
)
tmnxMobPdnBcGyChrgQvtPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQvtPresent.setStatus("current")
_TmnxMobPdnBcGyChrgQvtRemaining_Type = Unsigned32
_TmnxMobPdnBcGyChrgQvtRemaining_Object = MibTableColumn
tmnxMobPdnBcGyChrgQvtRemaining = _TmnxMobPdnBcGyChrgQvtRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 30),
    _TmnxMobPdnBcGyChrgQvtRemaining_Type()
)
tmnxMobPdnBcGyChrgQvtRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQvtRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgQvtRemaining.setUnits("seconds")
_TmnxMobPdnBcGyChrgTtcPresent_Type = TmnxMobPresenceState
_TmnxMobPdnBcGyChrgTtcPresent_Object = MibTableColumn
tmnxMobPdnBcGyChrgTtcPresent = _TmnxMobPdnBcGyChrgTtcPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 31),
    _TmnxMobPdnBcGyChrgTtcPresent_Type()
)
tmnxMobPdnBcGyChrgTtcPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTtcPresent.setStatus("current")
_TmnxMobPdnBcGyChrgTarrifTimeChng_Type = Unsigned32
_TmnxMobPdnBcGyChrgTarrifTimeChng_Object = MibTableColumn
tmnxMobPdnBcGyChrgTarrifTimeChng = _TmnxMobPdnBcGyChrgTarrifTimeChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 32),
    _TmnxMobPdnBcGyChrgTarrifTimeChng_Type()
)
tmnxMobPdnBcGyChrgTarrifTimeChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTarrifTimeChng.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTarrifTimeChng.setUnits("seconds")
_TmnxMobPdnBcGyChrgFuiPresent_Type = TmnxMobPresenceState
_TmnxMobPdnBcGyChrgFuiPresent_Object = MibTableColumn
tmnxMobPdnBcGyChrgFuiPresent = _TmnxMobPdnBcGyChrgFuiPresent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 33),
    _TmnxMobPdnBcGyChrgFuiPresent_Type()
)
tmnxMobPdnBcGyChrgFuiPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgFuiPresent.setStatus("current")
_TmnxMobPdnBcGyChrgOnlineEnabled_Type = TmnxEnabledDisabled
_TmnxMobPdnBcGyChrgOnlineEnabled_Object = MibTableColumn
tmnxMobPdnBcGyChrgOnlineEnabled = _TmnxMobPdnBcGyChrgOnlineEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 34),
    _TmnxMobPdnBcGyChrgOnlineEnabled_Type()
)
tmnxMobPdnBcGyChrgOnlineEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgOnlineEnabled.setStatus("current")
_TmnxMobPdnBcGyChrgTimeThreshold_Type = Unsigned32
_TmnxMobPdnBcGyChrgTimeThreshold_Object = MibTableColumn
tmnxMobPdnBcGyChrgTimeThreshold = _TmnxMobPdnBcGyChrgTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 35),
    _TmnxMobPdnBcGyChrgTimeThreshold_Type()
)
tmnxMobPdnBcGyChrgTimeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTimeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTimeThreshold.setUnits("seconds")
_TmnxMobPdnBcGyChrgVolThreshold_Type = Unsigned32
_TmnxMobPdnBcGyChrgVolThreshold_Object = MibTableColumn
tmnxMobPdnBcGyChrgVolThreshold = _TmnxMobPdnBcGyChrgVolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 36),
    _TmnxMobPdnBcGyChrgVolThreshold_Type()
)
tmnxMobPdnBcGyChrgVolThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgVolThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgVolThreshold.setUnits("bytes")
_TmnxMobPdnBcGyChrgTrigger_Type = TmnxMobPdnGyChrgTriggerType
_TmnxMobPdnBcGyChrgTrigger_Object = MibTableColumn
tmnxMobPdnBcGyChrgTrigger = _TmnxMobPdnBcGyChrgTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 37),
    _TmnxMobPdnBcGyChrgTrigger_Type()
)
tmnxMobPdnBcGyChrgTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgTrigger.setStatus("current")
_TmnxMobPdnBcGyChrgActvThreshold_Type = Unsigned32
_TmnxMobPdnBcGyChrgActvThreshold_Object = MibTableColumn
tmnxMobPdnBcGyChrgActvThreshold = _TmnxMobPdnBcGyChrgActvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 38),
    _TmnxMobPdnBcGyChrgActvThreshold_Type()
)
tmnxMobPdnBcGyChrgActvThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgActvThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgActvThreshold.setUnits("bytes")
_TmnxMobPdnBcGyChrgRedServerType_Type = InetAddressType
_TmnxMobPdnBcGyChrgRedServerType_Object = MibTableColumn
tmnxMobPdnBcGyChrgRedServerType = _TmnxMobPdnBcGyChrgRedServerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 39),
    _TmnxMobPdnBcGyChrgRedServerType_Type()
)
tmnxMobPdnBcGyChrgRedServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgRedServerType.setStatus("current")
_TmnxMobPdnBcGyChrgRedServer_Type = InetAddress
_TmnxMobPdnBcGyChrgRedServer_Object = MibTableColumn
tmnxMobPdnBcGyChrgRedServer = _TmnxMobPdnBcGyChrgRedServer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 40),
    _TmnxMobPdnBcGyChrgRedServer_Type()
)
tmnxMobPdnBcGyChrgRedServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgRedServer.setStatus("current")


class _TmnxMobPdnBcGyChrgBillingMethod_Type(Integer32):
    """Custom type tmnxMobPdnBcGyChrgBillingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("onlineOffline", 3))
    )


_TmnxMobPdnBcGyChrgBillingMethod_Type.__name__ = "Integer32"
_TmnxMobPdnBcGyChrgBillingMethod_Object = MibTableColumn
tmnxMobPdnBcGyChrgBillingMethod = _TmnxMobPdnBcGyChrgBillingMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 41),
    _TmnxMobPdnBcGyChrgBillingMethod_Type()
)
tmnxMobPdnBcGyChrgBillingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgBillingMethod.setStatus("current")


class _TmnxMobPdnBcGyChrgReportingLevel_Type(Integer32):
    """Custom type tmnxMobPdnBcGyChrgReportingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("svcIdLevel", 1),
          ("rgLevel", 2))
    )


_TmnxMobPdnBcGyChrgReportingLevel_Type.__name__ = "Integer32"
_TmnxMobPdnBcGyChrgReportingLevel_Object = MibTableColumn
tmnxMobPdnBcGyChrgReportingLevel = _TmnxMobPdnBcGyChrgReportingLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 42),
    _TmnxMobPdnBcGyChrgReportingLevel_Type()
)
tmnxMobPdnBcGyChrgReportingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgReportingLevel.setStatus("current")
_TmnxMobPdnBcGyChrgResultCode_Type = Unsigned32
_TmnxMobPdnBcGyChrgResultCode_Object = MibTableColumn
tmnxMobPdnBcGyChrgResultCode = _TmnxMobPdnBcGyChrgResultCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 24, 1, 43),
    _TmnxMobPdnBcGyChrgResultCode_Type()
)
tmnxMobPdnBcGyChrgResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcGyChrgResultCode.setStatus("current")
_TmnxMobPdnBcAcctRfTable_Object = MibTable
tmnxMobPdnBcAcctRfTable = _TmnxMobPdnBcAcctRfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfTable.setStatus("current")
_TmnxMobPdnBcAcctRfEntry_Object = MibTableRow
tmnxMobPdnBcAcctRfEntry = _TmnxMobPdnBcAcctRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfEntry.setStatus("current")
_TmnxMobPdnBcAcctRfChargingId_Type = TmnxMobChargingProfile
_TmnxMobPdnBcAcctRfChargingId_Object = MibTableColumn
tmnxMobPdnBcAcctRfChargingId = _TmnxMobPdnBcAcctRfChargingId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 1),
    _TmnxMobPdnBcAcctRfChargingId_Type()
)
tmnxMobPdnBcAcctRfChargingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfChargingId.setStatus("current")
_TmnxMobPdnBcAcctRfUlSustRate_Type = Counter32
_TmnxMobPdnBcAcctRfUlSustRate_Object = MibTableColumn
tmnxMobPdnBcAcctRfUlSustRate = _TmnxMobPdnBcAcctRfUlSustRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 2),
    _TmnxMobPdnBcAcctRfUlSustRate_Type()
)
tmnxMobPdnBcAcctRfUlSustRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfUlSustRate.setStatus("current")
_TmnxMobPdnBcAcctRfDlSustRate_Type = Counter32
_TmnxMobPdnBcAcctRfDlSustRate_Object = MibTableColumn
tmnxMobPdnBcAcctRfDlSustRate = _TmnxMobPdnBcAcctRfDlSustRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 3),
    _TmnxMobPdnBcAcctRfDlSustRate_Type()
)
tmnxMobPdnBcAcctRfDlSustRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfDlSustRate.setStatus("current")
_TmnxMobPdnBcAcctRfAggrUlPkts_Type = Counter64
_TmnxMobPdnBcAcctRfAggrUlPkts_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrUlPkts = _TmnxMobPdnBcAcctRfAggrUlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 4),
    _TmnxMobPdnBcAcctRfAggrUlPkts_Type()
)
tmnxMobPdnBcAcctRfAggrUlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrUlPkts.setStatus("current")
_TmnxMobPdnBcAcctRfAggrUlPktsLow_Type = Counter32
_TmnxMobPdnBcAcctRfAggrUlPktsLow_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrUlPktsLow = _TmnxMobPdnBcAcctRfAggrUlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 5),
    _TmnxMobPdnBcAcctRfAggrUlPktsLow_Type()
)
tmnxMobPdnBcAcctRfAggrUlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrUlPktsLow.setStatus("current")
_TmnxMobPdnBcAcctRfAggrUlPktsHigh_Type = Counter32
_TmnxMobPdnBcAcctRfAggrUlPktsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrUlPktsHigh = _TmnxMobPdnBcAcctRfAggrUlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 6),
    _TmnxMobPdnBcAcctRfAggrUlPktsHigh_Type()
)
tmnxMobPdnBcAcctRfAggrUlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrUlPktsHigh.setStatus("current")
_TmnxMobPdnBcAcctRfAggrDlPkts_Type = Counter64
_TmnxMobPdnBcAcctRfAggrDlPkts_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrDlPkts = _TmnxMobPdnBcAcctRfAggrDlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 7),
    _TmnxMobPdnBcAcctRfAggrDlPkts_Type()
)
tmnxMobPdnBcAcctRfAggrDlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrDlPkts.setStatus("current")
_TmnxMobPdnBcAcctRfAggrDlPktsLow_Type = Counter32
_TmnxMobPdnBcAcctRfAggrDlPktsLow_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrDlPktsLow = _TmnxMobPdnBcAcctRfAggrDlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 8),
    _TmnxMobPdnBcAcctRfAggrDlPktsLow_Type()
)
tmnxMobPdnBcAcctRfAggrDlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrDlPktsLow.setStatus("current")
_TmnxMobPdnBcAcctRfAggrDlPktsHigh_Type = Counter32
_TmnxMobPdnBcAcctRfAggrDlPktsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrDlPktsHigh = _TmnxMobPdnBcAcctRfAggrDlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 9),
    _TmnxMobPdnBcAcctRfAggrDlPktsHigh_Type()
)
tmnxMobPdnBcAcctRfAggrDlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrDlPktsHigh.setStatus("current")
_TmnxMobPdnBcAcctRfAggrUlByts_Type = Counter64
_TmnxMobPdnBcAcctRfAggrUlByts_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrUlByts = _TmnxMobPdnBcAcctRfAggrUlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 10),
    _TmnxMobPdnBcAcctRfAggrUlByts_Type()
)
tmnxMobPdnBcAcctRfAggrUlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrUlByts.setStatus("current")
_TmnxMobPdnBcAcctRfAggrUlBytsLow_Type = Counter32
_TmnxMobPdnBcAcctRfAggrUlBytsLow_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrUlBytsLow = _TmnxMobPdnBcAcctRfAggrUlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 11),
    _TmnxMobPdnBcAcctRfAggrUlBytsLow_Type()
)
tmnxMobPdnBcAcctRfAggrUlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrUlBytsLow.setStatus("current")
_TmnxMobPdnBcAcctRfAggrUlBytsHigh_Type = Counter32
_TmnxMobPdnBcAcctRfAggrUlBytsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrUlBytsHigh = _TmnxMobPdnBcAcctRfAggrUlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 12),
    _TmnxMobPdnBcAcctRfAggrUlBytsHigh_Type()
)
tmnxMobPdnBcAcctRfAggrUlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrUlBytsHigh.setStatus("current")
_TmnxMobPdnBcAcctRfAggrDlByts_Type = Counter64
_TmnxMobPdnBcAcctRfAggrDlByts_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrDlByts = _TmnxMobPdnBcAcctRfAggrDlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 13),
    _TmnxMobPdnBcAcctRfAggrDlByts_Type()
)
tmnxMobPdnBcAcctRfAggrDlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrDlByts.setStatus("current")
_TmnxMobPdnBcAcctRfAggrDlBytsLow_Type = Counter32
_TmnxMobPdnBcAcctRfAggrDlBytsLow_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrDlBytsLow = _TmnxMobPdnBcAcctRfAggrDlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 14),
    _TmnxMobPdnBcAcctRfAggrDlBytsLow_Type()
)
tmnxMobPdnBcAcctRfAggrDlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrDlBytsLow.setStatus("current")
_TmnxMobPdnBcAcctRfAggrDlBytsHigh_Type = Counter32
_TmnxMobPdnBcAcctRfAggrDlBytsHigh_Object = MibTableColumn
tmnxMobPdnBcAcctRfAggrDlBytsHigh = _TmnxMobPdnBcAcctRfAggrDlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 15),
    _TmnxMobPdnBcAcctRfAggrDlBytsHigh_Type()
)
tmnxMobPdnBcAcctRfAggrDlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfAggrDlBytsHigh.setStatus("current")
_TmnxMobPdnBcAcctRfNumInterimSent_Type = Counter32
_TmnxMobPdnBcAcctRfNumInterimSent_Object = MibTableColumn
tmnxMobPdnBcAcctRfNumInterimSent = _TmnxMobPdnBcAcctRfNumInterimSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 16),
    _TmnxMobPdnBcAcctRfNumInterimSent_Type()
)
tmnxMobPdnBcAcctRfNumInterimSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfNumInterimSent.setStatus("current")
_TmnxMobPdnBcAcctRfNumRgs_Type = Counter32
_TmnxMobPdnBcAcctRfNumRgs_Object = MibTableColumn
tmnxMobPdnBcAcctRfNumRgs = _TmnxMobPdnBcAcctRfNumRgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 17),
    _TmnxMobPdnBcAcctRfNumRgs_Type()
)
tmnxMobPdnBcAcctRfNumRgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfNumRgs.setStatus("current")
_TmnxMobPdnBcAcctRfNumOfRgSvcId_Type = Counter32
_TmnxMobPdnBcAcctRfNumOfRgSvcId_Object = MibTableColumn
tmnxMobPdnBcAcctRfNumOfRgSvcId = _TmnxMobPdnBcAcctRfNumOfRgSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 25, 1, 18),
    _TmnxMobPdnBcAcctRfNumOfRgSvcId_Type()
)
tmnxMobPdnBcAcctRfNumOfRgSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnBcAcctRfNumOfRgSvcId.setStatus("current")
_TmnxMobPdnPcAcctRfTable_Object = MibTable
tmnxMobPdnPcAcctRfTable = _TmnxMobPdnPcAcctRfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26)
)
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfTable.setStatus("current")
_TmnxMobPdnPcAcctRfEntry_Object = MibTableRow
tmnxMobPdnPcAcctRfEntry = _TmnxMobPdnPcAcctRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1)
)
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfEntry.setStatus("current")
_TmnxMobPdnPcAcctRfAggrUlPkts_Type = Counter64
_TmnxMobPdnPcAcctRfAggrUlPkts_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrUlPkts = _TmnxMobPdnPcAcctRfAggrUlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 1),
    _TmnxMobPdnPcAcctRfAggrUlPkts_Type()
)
tmnxMobPdnPcAcctRfAggrUlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrUlPkts.setStatus("current")
_TmnxMobPdnPcAcctRfAggrUlPktsLow_Type = Counter32
_TmnxMobPdnPcAcctRfAggrUlPktsLow_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrUlPktsLow = _TmnxMobPdnPcAcctRfAggrUlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 2),
    _TmnxMobPdnPcAcctRfAggrUlPktsLow_Type()
)
tmnxMobPdnPcAcctRfAggrUlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrUlPktsLow.setStatus("current")
_TmnxMobPdnPcAcctRfAggrUlPktsHigh_Type = Counter32
_TmnxMobPdnPcAcctRfAggrUlPktsHigh_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrUlPktsHigh = _TmnxMobPdnPcAcctRfAggrUlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 3),
    _TmnxMobPdnPcAcctRfAggrUlPktsHigh_Type()
)
tmnxMobPdnPcAcctRfAggrUlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrUlPktsHigh.setStatus("current")
_TmnxMobPdnPcAcctRfAggrDlPkts_Type = Counter64
_TmnxMobPdnPcAcctRfAggrDlPkts_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrDlPkts = _TmnxMobPdnPcAcctRfAggrDlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 4),
    _TmnxMobPdnPcAcctRfAggrDlPkts_Type()
)
tmnxMobPdnPcAcctRfAggrDlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrDlPkts.setStatus("current")
_TmnxMobPdnPcAcctRfAggrDlPktsLow_Type = Counter32
_TmnxMobPdnPcAcctRfAggrDlPktsLow_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrDlPktsLow = _TmnxMobPdnPcAcctRfAggrDlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 5),
    _TmnxMobPdnPcAcctRfAggrDlPktsLow_Type()
)
tmnxMobPdnPcAcctRfAggrDlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrDlPktsLow.setStatus("current")
_TmnxMobPdnPcAcctRfAggrDlPktsHigh_Type = Counter32
_TmnxMobPdnPcAcctRfAggrDlPktsHigh_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrDlPktsHigh = _TmnxMobPdnPcAcctRfAggrDlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 6),
    _TmnxMobPdnPcAcctRfAggrDlPktsHigh_Type()
)
tmnxMobPdnPcAcctRfAggrDlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrDlPktsHigh.setStatus("current")
_TmnxMobPdnPcAcctRfAggrUlByts_Type = Counter64
_TmnxMobPdnPcAcctRfAggrUlByts_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrUlByts = _TmnxMobPdnPcAcctRfAggrUlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 7),
    _TmnxMobPdnPcAcctRfAggrUlByts_Type()
)
tmnxMobPdnPcAcctRfAggrUlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrUlByts.setStatus("current")
_TmnxMobPdnPcAcctRfAggrUlBytsLow_Type = Counter32
_TmnxMobPdnPcAcctRfAggrUlBytsLow_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrUlBytsLow = _TmnxMobPdnPcAcctRfAggrUlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 8),
    _TmnxMobPdnPcAcctRfAggrUlBytsLow_Type()
)
tmnxMobPdnPcAcctRfAggrUlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrUlBytsLow.setStatus("current")
_TmnxMobPdnPcAcctRfAggrUlBytsHigh_Type = Counter32
_TmnxMobPdnPcAcctRfAggrUlBytsHigh_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrUlBytsHigh = _TmnxMobPdnPcAcctRfAggrUlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 9),
    _TmnxMobPdnPcAcctRfAggrUlBytsHigh_Type()
)
tmnxMobPdnPcAcctRfAggrUlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrUlBytsHigh.setStatus("current")
_TmnxMobPdnPcAcctRfAggrDlByts_Type = Counter64
_TmnxMobPdnPcAcctRfAggrDlByts_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrDlByts = _TmnxMobPdnPcAcctRfAggrDlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 10),
    _TmnxMobPdnPcAcctRfAggrDlByts_Type()
)
tmnxMobPdnPcAcctRfAggrDlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrDlByts.setStatus("current")
_TmnxMobPdnPcAcctRfAggrDlBytsLow_Type = Counter32
_TmnxMobPdnPcAcctRfAggrDlBytsLow_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrDlBytsLow = _TmnxMobPdnPcAcctRfAggrDlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 11),
    _TmnxMobPdnPcAcctRfAggrDlBytsLow_Type()
)
tmnxMobPdnPcAcctRfAggrDlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrDlBytsLow.setStatus("current")
_TmnxMobPdnPcAcctRfAggrDlBytsHigh_Type = Counter32
_TmnxMobPdnPcAcctRfAggrDlBytsHigh_Object = MibTableColumn
tmnxMobPdnPcAcctRfAggrDlBytsHigh = _TmnxMobPdnPcAcctRfAggrDlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 12),
    _TmnxMobPdnPcAcctRfAggrDlBytsHigh_Type()
)
tmnxMobPdnPcAcctRfAggrDlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfAggrDlBytsHigh.setStatus("current")
_TmnxMobPdnPcAcctRfUlAvgRate_Type = Counter32
_TmnxMobPdnPcAcctRfUlAvgRate_Object = MibTableColumn
tmnxMobPdnPcAcctRfUlAvgRate = _TmnxMobPdnPcAcctRfUlAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 13),
    _TmnxMobPdnPcAcctRfUlAvgRate_Type()
)
tmnxMobPdnPcAcctRfUlAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfUlAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfUlAvgRate.setUnits("kbps")
_TmnxMobPdnPcAcctRfDlAvgRate_Type = Counter32
_TmnxMobPdnPcAcctRfDlAvgRate_Object = MibTableColumn
tmnxMobPdnPcAcctRfDlAvgRate = _TmnxMobPdnPcAcctRfDlAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 14),
    _TmnxMobPdnPcAcctRfDlAvgRate_Type()
)
tmnxMobPdnPcAcctRfDlAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfDlAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfDlAvgRate.setUnits("kbps")
_TmnxMobPdnPcAcctRfNumInterimSent_Type = Counter32
_TmnxMobPdnPcAcctRfNumInterimSent_Object = MibTableColumn
tmnxMobPdnPcAcctRfNumInterimSent = _TmnxMobPdnPcAcctRfNumInterimSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 15),
    _TmnxMobPdnPcAcctRfNumInterimSent_Type()
)
tmnxMobPdnPcAcctRfNumInterimSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfNumInterimSent.setStatus("current")
_TmnxMobPdnPcAcctRfNumRgs_Type = Counter32
_TmnxMobPdnPcAcctRfNumRgs_Object = MibTableColumn
tmnxMobPdnPcAcctRfNumRgs = _TmnxMobPdnPcAcctRfNumRgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 16),
    _TmnxMobPdnPcAcctRfNumRgs_Type()
)
tmnxMobPdnPcAcctRfNumRgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfNumRgs.setStatus("current")
_TmnxMobPdnPcAcctRfNumOfRgSvcId_Type = Counter32
_TmnxMobPdnPcAcctRfNumOfRgSvcId_Object = MibTableColumn
tmnxMobPdnPcAcctRfNumOfRgSvcId = _TmnxMobPdnPcAcctRfNumOfRgSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 26, 1, 17),
    _TmnxMobPdnPcAcctRfNumOfRgSvcId_Type()
)
tmnxMobPdnPcAcctRfNumOfRgSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcAcctRfNumOfRgSvcId.setStatus("current")
_TmnxMobPdnPcRfChrgTable_Object = MibTable
tmnxMobPdnPcRfChrgTable = _TmnxMobPdnPcRfChrgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27)
)
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgTable.setStatus("current")
_TmnxMobPdnPcRfChrgEntry_Object = MibTableRow
tmnxMobPdnPcRfChrgEntry = _TmnxMobPdnPcRfChrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1)
)
tmnxMobPdnPcRfChrgEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsi"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcApn"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPdnType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcBearerId"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitRatingGroup"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfChgUnitServIdentifier"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgEntry.setStatus("current")
_TmnxMobPdnPcRfChrgOnlnCharging_Type = TruthValue
_TmnxMobPdnPcRfChrgOnlnCharging_Object = MibTableColumn
tmnxMobPdnPcRfChrgOnlnCharging = _TmnxMobPdnPcRfChrgOnlnCharging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 1),
    _TmnxMobPdnPcRfChrgOnlnCharging_Type()
)
tmnxMobPdnPcRfChrgOnlnCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgOnlnCharging.setStatus("current")
_TmnxMobPdnPcRfChrgOfflnCharging_Type = TruthValue
_TmnxMobPdnPcRfChrgOfflnCharging_Object = MibTableColumn
tmnxMobPdnPcRfChrgOfflnCharging = _TmnxMobPdnPcRfChrgOfflnCharging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 2),
    _TmnxMobPdnPcRfChrgOfflnCharging_Type()
)
tmnxMobPdnPcRfChrgOfflnCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgOfflnCharging.setStatus("current")
_TmnxMobPdnPcRfChrgUlPkts_Type = Counter64
_TmnxMobPdnPcRfChrgUlPkts_Object = MibTableColumn
tmnxMobPdnPcRfChrgUlPkts = _TmnxMobPdnPcRfChrgUlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 3),
    _TmnxMobPdnPcRfChrgUlPkts_Type()
)
tmnxMobPdnPcRfChrgUlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgUlPkts.setStatus("current")
_TmnxMobPdnPcRfChrgUlPktsLow_Type = Counter32
_TmnxMobPdnPcRfChrgUlPktsLow_Object = MibTableColumn
tmnxMobPdnPcRfChrgUlPktsLow = _TmnxMobPdnPcRfChrgUlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 4),
    _TmnxMobPdnPcRfChrgUlPktsLow_Type()
)
tmnxMobPdnPcRfChrgUlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgUlPktsLow.setStatus("current")
_TmnxMobPdnPcRfChrgUlPktsHigh_Type = Counter32
_TmnxMobPdnPcRfChrgUlPktsHigh_Object = MibTableColumn
tmnxMobPdnPcRfChrgUlPktsHigh = _TmnxMobPdnPcRfChrgUlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 5),
    _TmnxMobPdnPcRfChrgUlPktsHigh_Type()
)
tmnxMobPdnPcRfChrgUlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgUlPktsHigh.setStatus("current")
_TmnxMobPdnPcRfChrgDlPkts_Type = Counter64
_TmnxMobPdnPcRfChrgDlPkts_Object = MibTableColumn
tmnxMobPdnPcRfChrgDlPkts = _TmnxMobPdnPcRfChrgDlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 6),
    _TmnxMobPdnPcRfChrgDlPkts_Type()
)
tmnxMobPdnPcRfChrgDlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgDlPkts.setStatus("current")
_TmnxMobPdnPcRfChrgDlPktsLow_Type = Counter32
_TmnxMobPdnPcRfChrgDlPktsLow_Object = MibTableColumn
tmnxMobPdnPcRfChrgDlPktsLow = _TmnxMobPdnPcRfChrgDlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 7),
    _TmnxMobPdnPcRfChrgDlPktsLow_Type()
)
tmnxMobPdnPcRfChrgDlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgDlPktsLow.setStatus("current")
_TmnxMobPdnPcRfChrgDlPktsHigh_Type = Counter32
_TmnxMobPdnPcRfChrgDlPktsHigh_Object = MibTableColumn
tmnxMobPdnPcRfChrgDlPktsHigh = _TmnxMobPdnPcRfChrgDlPktsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 8),
    _TmnxMobPdnPcRfChrgDlPktsHigh_Type()
)
tmnxMobPdnPcRfChrgDlPktsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgDlPktsHigh.setStatus("current")
_TmnxMobPdnPcRfChrgUlByts_Type = Counter64
_TmnxMobPdnPcRfChrgUlByts_Object = MibTableColumn
tmnxMobPdnPcRfChrgUlByts = _TmnxMobPdnPcRfChrgUlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 9),
    _TmnxMobPdnPcRfChrgUlByts_Type()
)
tmnxMobPdnPcRfChrgUlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgUlByts.setStatus("current")
_TmnxMobPdnPcRfChrgUlBytsLow_Type = Counter32
_TmnxMobPdnPcRfChrgUlBytsLow_Object = MibTableColumn
tmnxMobPdnPcRfChrgUlBytsLow = _TmnxMobPdnPcRfChrgUlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 10),
    _TmnxMobPdnPcRfChrgUlBytsLow_Type()
)
tmnxMobPdnPcRfChrgUlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgUlBytsLow.setStatus("current")
_TmnxMobPdnPcRfChrgUlBytsHigh_Type = Counter32
_TmnxMobPdnPcRfChrgUlBytsHigh_Object = MibTableColumn
tmnxMobPdnPcRfChrgUlBytsHigh = _TmnxMobPdnPcRfChrgUlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 11),
    _TmnxMobPdnPcRfChrgUlBytsHigh_Type()
)
tmnxMobPdnPcRfChrgUlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgUlBytsHigh.setStatus("current")
_TmnxMobPdnPcRfChrgDlByts_Type = Counter64
_TmnxMobPdnPcRfChrgDlByts_Object = MibTableColumn
tmnxMobPdnPcRfChrgDlByts = _TmnxMobPdnPcRfChrgDlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 12),
    _TmnxMobPdnPcRfChrgDlByts_Type()
)
tmnxMobPdnPcRfChrgDlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgDlByts.setStatus("current")
_TmnxMobPdnPcRfChrgDlBytsLow_Type = Counter32
_TmnxMobPdnPcRfChrgDlBytsLow_Object = MibTableColumn
tmnxMobPdnPcRfChrgDlBytsLow = _TmnxMobPdnPcRfChrgDlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 13),
    _TmnxMobPdnPcRfChrgDlBytsLow_Type()
)
tmnxMobPdnPcRfChrgDlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgDlBytsLow.setStatus("current")
_TmnxMobPdnPcRfChrgDlBytsHigh_Type = Counter32
_TmnxMobPdnPcRfChrgDlBytsHigh_Object = MibTableColumn
tmnxMobPdnPcRfChrgDlBytsHigh = _TmnxMobPdnPcRfChrgDlBytsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 27, 1, 14),
    _TmnxMobPdnPcRfChrgDlBytsHigh_Type()
)
tmnxMobPdnPcRfChrgDlBytsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPcRfChrgDlBytsHigh.setStatus("current")
_TmnxMobPdnS6bPeerTable_Object = MibTable
tmnxMobPdnS6bPeerTable = _TmnxMobPdnS6bPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerTable.setStatus("current")
_TmnxMobPdnS6bPeerEntry_Object = MibTableRow
tmnxMobPdnS6bPeerEntry = _TmnxMobPdnS6bPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28, 1)
)
tmnxMobPdnS6bPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerEntry.setStatus("current")
_TmnxMobPdnS6bPeerAddressType_Type = InetAddressType
_TmnxMobPdnS6bPeerAddressType_Object = MibTableColumn
tmnxMobPdnS6bPeerAddressType = _TmnxMobPdnS6bPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28, 1, 1),
    _TmnxMobPdnS6bPeerAddressType_Type()
)
tmnxMobPdnS6bPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerAddressType.setStatus("current")


class _TmnxMobPdnS6bPeerAddress_Type(InetAddress):
    """Custom type tmnxMobPdnS6bPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobPdnS6bPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobPdnS6bPeerAddress_Object = MibTableColumn
tmnxMobPdnS6bPeerAddress = _TmnxMobPdnS6bPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28, 1, 2),
    _TmnxMobPdnS6bPeerAddress_Type()
)
tmnxMobPdnS6bPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerAddress.setStatus("current")
_TmnxMobPdnS6bPeerPort_Type = InetPortNumber
_TmnxMobPdnS6bPeerPort_Object = MibTableColumn
tmnxMobPdnS6bPeerPort = _TmnxMobPdnS6bPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28, 1, 3),
    _TmnxMobPdnS6bPeerPort_Type()
)
tmnxMobPdnS6bPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerPort.setStatus("current")
_TmnxMobPdnS6bPeerLastChanged_Type = TimeStamp
_TmnxMobPdnS6bPeerLastChanged_Object = MibTableColumn
tmnxMobPdnS6bPeerLastChanged = _TmnxMobPdnS6bPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28, 1, 4),
    _TmnxMobPdnS6bPeerLastChanged_Type()
)
tmnxMobPdnS6bPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerLastChanged.setStatus("current")
_TmnxMobPdnS6bPeerCreateTime_Type = TimeStamp
_TmnxMobPdnS6bPeerCreateTime_Object = MibTableColumn
tmnxMobPdnS6bPeerCreateTime = _TmnxMobPdnS6bPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28, 1, 5),
    _TmnxMobPdnS6bPeerCreateTime_Type()
)
tmnxMobPdnS6bPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerCreateTime.setStatus("current")
_TmnxMobPdnS6bPeerPathMgmtState_Type = TmnxMobDiaPathMgmtState
_TmnxMobPdnS6bPeerPathMgmtState_Object = MibTableColumn
tmnxMobPdnS6bPeerPathMgmtState = _TmnxMobPdnS6bPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28, 1, 6),
    _TmnxMobPdnS6bPeerPathMgmtState_Type()
)
tmnxMobPdnS6bPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerPathMgmtState.setStatus("current")
_TmnxMobPdnS6bPeerDetailState_Type = TmnxMobDiaDetailPathMgmtState
_TmnxMobPdnS6bPeerDetailState_Object = MibTableColumn
tmnxMobPdnS6bPeerDetailState = _TmnxMobPdnS6bPeerDetailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 28, 1, 7),
    _TmnxMobPdnS6bPeerDetailState_Type()
)
tmnxMobPdnS6bPeerDetailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerDetailState.setStatus("current")
_TmnxMobPdnS6bStatTable_Object = MibTable
tmnxMobPdnS6bStatTable = _TmnxMobPdnS6bStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29)
)
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatTable.setStatus("current")
_TmnxMobPdnS6bStatEntry_Object = MibTableRow
tmnxMobPdnS6bStatEntry = _TmnxMobPdnS6bStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1)
)
tmnxMobPdnS6bStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobProfDiaPeerListIndex"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerAddressType"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerAddress"),
    (0, "TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatEntry.setStatus("current")
_TmnxMobPdnS6bStatAARInitTx_Type = Counter32
_TmnxMobPdnS6bStatAARInitTx_Object = MibTableColumn
tmnxMobPdnS6bStatAARInitTx = _TmnxMobPdnS6bStatAARInitTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 1),
    _TmnxMobPdnS6bStatAARInitTx_Type()
)
tmnxMobPdnS6bStatAARInitTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAARInitTx.setStatus("current")
_TmnxMobPdnS6bStatAARExtnTx_Type = Counter32
_TmnxMobPdnS6bStatAARExtnTx_Object = MibTableColumn
tmnxMobPdnS6bStatAARExtnTx = _TmnxMobPdnS6bStatAARExtnTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 2),
    _TmnxMobPdnS6bStatAARExtnTx_Type()
)
tmnxMobPdnS6bStatAARExtnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAARExtnTx.setStatus("current")
_TmnxMobPdnS6bStatAARDetachTx_Type = Counter32
_TmnxMobPdnS6bStatAARDetachTx_Object = MibTableColumn
tmnxMobPdnS6bStatAARDetachTx = _TmnxMobPdnS6bStatAARDetachTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 3),
    _TmnxMobPdnS6bStatAARDetachTx_Type()
)
tmnxMobPdnS6bStatAARDetachTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAARDetachTx.setStatus("current")
_TmnxMobPdnS6bStatAARReauthTx_Type = Counter32
_TmnxMobPdnS6bStatAARReauthTx_Object = MibTableColumn
tmnxMobPdnS6bStatAARReauthTx = _TmnxMobPdnS6bStatAARReauthTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 4),
    _TmnxMobPdnS6bStatAARReauthTx_Type()
)
tmnxMobPdnS6bStatAARReauthTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAARReauthTx.setStatus("current")
_TmnxMobPdnS6bStatAAAInitAtchRx_Type = Counter32
_TmnxMobPdnS6bStatAAAInitAtchRx_Object = MibTableColumn
tmnxMobPdnS6bStatAAAInitAtchRx = _TmnxMobPdnS6bStatAAAInitAtchRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 5),
    _TmnxMobPdnS6bStatAAAInitAtchRx_Type()
)
tmnxMobPdnS6bStatAAAInitAtchRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAAAInitAtchRx.setStatus("current")
_TmnxMobPdnS6bStatAAAExtnRx_Type = Counter32
_TmnxMobPdnS6bStatAAAExtnRx_Object = MibTableColumn
tmnxMobPdnS6bStatAAAExtnRx = _TmnxMobPdnS6bStatAAAExtnRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 6),
    _TmnxMobPdnS6bStatAAAExtnRx_Type()
)
tmnxMobPdnS6bStatAAAExtnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAAAExtnRx.setStatus("current")
_TmnxMobPdnS6bStatAAADetachRx_Type = Counter32
_TmnxMobPdnS6bStatAAADetachRx_Object = MibTableColumn
tmnxMobPdnS6bStatAAADetachRx = _TmnxMobPdnS6bStatAAADetachRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 7),
    _TmnxMobPdnS6bStatAAADetachRx_Type()
)
tmnxMobPdnS6bStatAAADetachRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAAADetachRx.setStatus("current")
_TmnxMobPdnS6bStatAAAReauthRx_Type = Counter32
_TmnxMobPdnS6bStatAAAReauthRx_Object = MibTableColumn
tmnxMobPdnS6bStatAAAReauthRx = _TmnxMobPdnS6bStatAAAReauthRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 8),
    _TmnxMobPdnS6bStatAAAReauthRx_Type()
)
tmnxMobPdnS6bStatAAAReauthRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAAAReauthRx.setStatus("current")
_TmnxMobPdnS6bStatAAASuccessRx_Type = Counter32
_TmnxMobPdnS6bStatAAASuccessRx_Object = MibTableColumn
tmnxMobPdnS6bStatAAASuccessRx = _TmnxMobPdnS6bStatAAASuccessRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 9),
    _TmnxMobPdnS6bStatAAASuccessRx_Type()
)
tmnxMobPdnS6bStatAAASuccessRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAAASuccessRx.setStatus("current")
_TmnxMobPdnS6bStatAAARejectRx_Type = Counter32
_TmnxMobPdnS6bStatAAARejectRx_Object = MibTableColumn
tmnxMobPdnS6bStatAAARejectRx = _TmnxMobPdnS6bStatAAARejectRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 10),
    _TmnxMobPdnS6bStatAAARejectRx_Type()
)
tmnxMobPdnS6bStatAAARejectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAAARejectRx.setStatus("current")
_TmnxMobPdnS6bStatRARequestRx_Type = Counter32
_TmnxMobPdnS6bStatRARequestRx_Object = MibTableColumn
tmnxMobPdnS6bStatRARequestRx = _TmnxMobPdnS6bStatRARequestRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 11),
    _TmnxMobPdnS6bStatRARequestRx_Type()
)
tmnxMobPdnS6bStatRARequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatRARequestRx.setStatus("current")
_TmnxMobPdnS6bStatRAAnswerTx_Type = Counter32
_TmnxMobPdnS6bStatRAAnswerTx_Object = MibTableColumn
tmnxMobPdnS6bStatRAAnswerTx = _TmnxMobPdnS6bStatRAAnswerTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 12),
    _TmnxMobPdnS6bStatRAAnswerTx_Type()
)
tmnxMobPdnS6bStatRAAnswerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatRAAnswerTx.setStatus("current")
_TmnxMobPdnS6bStatSTRequestTx_Type = Counter32
_TmnxMobPdnS6bStatSTRequestTx_Object = MibTableColumn
tmnxMobPdnS6bStatSTRequestTx = _TmnxMobPdnS6bStatSTRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 13),
    _TmnxMobPdnS6bStatSTRequestTx_Type()
)
tmnxMobPdnS6bStatSTRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatSTRequestTx.setStatus("current")
_TmnxMobPdnS6bStatSTAnswerRx_Type = Counter32
_TmnxMobPdnS6bStatSTAnswerRx_Object = MibTableColumn
tmnxMobPdnS6bStatSTAnswerRx = _TmnxMobPdnS6bStatSTAnswerRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 14),
    _TmnxMobPdnS6bStatSTAnswerRx_Type()
)
tmnxMobPdnS6bStatSTAnswerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatSTAnswerRx.setStatus("current")
_TmnxMobPdnS6bStatASRequestRx_Type = Counter32
_TmnxMobPdnS6bStatASRequestRx_Object = MibTableColumn
tmnxMobPdnS6bStatASRequestRx = _TmnxMobPdnS6bStatASRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 15),
    _TmnxMobPdnS6bStatASRequestRx_Type()
)
tmnxMobPdnS6bStatASRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatASRequestRx.setStatus("current")
_TmnxMobPdnS6bStatASAnswerTx_Type = Counter32
_TmnxMobPdnS6bStatASAnswerTx_Object = MibTableColumn
tmnxMobPdnS6bStatASAnswerTx = _TmnxMobPdnS6bStatASAnswerTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 16),
    _TmnxMobPdnS6bStatASAnswerTx_Type()
)
tmnxMobPdnS6bStatASAnswerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatASAnswerTx.setStatus("current")
_TmnxMobPdnS6bStatAAAMissAVPPktRx_Type = Counter32
_TmnxMobPdnS6bStatAAAMissAVPPktRx_Object = MibTableColumn
tmnxMobPdnS6bStatAAAMissAVPPktRx = _TmnxMobPdnS6bStatAAAMissAVPPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 17),
    _TmnxMobPdnS6bStatAAAMissAVPPktRx_Type()
)
tmnxMobPdnS6bStatAAAMissAVPPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAAAMissAVPPktRx.setStatus("current")
_TmnxMobPdnS6bStatRARMissAVPPktRx_Type = Counter32
_TmnxMobPdnS6bStatRARMissAVPPktRx_Object = MibTableColumn
tmnxMobPdnS6bStatRARMissAVPPktRx = _TmnxMobPdnS6bStatRARMissAVPPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 18),
    _TmnxMobPdnS6bStatRARMissAVPPktRx_Type()
)
tmnxMobPdnS6bStatRARMissAVPPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatRARMissAVPPktRx.setStatus("current")
_TmnxMobPdnS6bStatSTAMissAVPPktRx_Type = Counter32
_TmnxMobPdnS6bStatSTAMissAVPPktRx_Object = MibTableColumn
tmnxMobPdnS6bStatSTAMissAVPPktRx = _TmnxMobPdnS6bStatSTAMissAVPPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 19),
    _TmnxMobPdnS6bStatSTAMissAVPPktRx_Type()
)
tmnxMobPdnS6bStatSTAMissAVPPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatSTAMissAVPPktRx.setStatus("current")
_TmnxMobPdnS6bStatASRMissAVPPktRx_Type = Counter32
_TmnxMobPdnS6bStatASRMissAVPPktRx_Object = MibTableColumn
tmnxMobPdnS6bStatASRMissAVPPktRx = _TmnxMobPdnS6bStatASRMissAVPPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 20),
    _TmnxMobPdnS6bStatASRMissAVPPktRx_Type()
)
tmnxMobPdnS6bStatASRMissAVPPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatASRMissAVPPktRx.setStatus("current")
_TmnxMobPdnS6bStatAAAUnknSesPktRx_Type = Counter32
_TmnxMobPdnS6bStatAAAUnknSesPktRx_Object = MibTableColumn
tmnxMobPdnS6bStatAAAUnknSesPktRx = _TmnxMobPdnS6bStatAAAUnknSesPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 21),
    _TmnxMobPdnS6bStatAAAUnknSesPktRx_Type()
)
tmnxMobPdnS6bStatAAAUnknSesPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAAAUnknSesPktRx.setStatus("current")
_TmnxMobPdnS6bStatAARRetries_Type = Counter32
_TmnxMobPdnS6bStatAARRetries_Object = MibTableColumn
tmnxMobPdnS6bStatAARRetries = _TmnxMobPdnS6bStatAARRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 22),
    _TmnxMobPdnS6bStatAARRetries_Type()
)
tmnxMobPdnS6bStatAARRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatAARRetries.setStatus("current")
_TmnxMobPdnS6bStatSTRRetries_Type = Counter32
_TmnxMobPdnS6bStatSTRRetries_Object = MibTableColumn
tmnxMobPdnS6bStatSTRRetries = _TmnxMobPdnS6bStatSTRRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 23),
    _TmnxMobPdnS6bStatSTRRetries_Type()
)
tmnxMobPdnS6bStatSTRRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatSTRRetries.setStatus("current")
_TmnxMobPdnS6bStatMessagesTx_Type = Counter32
_TmnxMobPdnS6bStatMessagesTx_Object = MibTableColumn
tmnxMobPdnS6bStatMessagesTx = _TmnxMobPdnS6bStatMessagesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 24),
    _TmnxMobPdnS6bStatMessagesTx_Type()
)
tmnxMobPdnS6bStatMessagesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatMessagesTx.setStatus("current")
_TmnxMobPdnS6bStatMessagesRx_Type = Counter32
_TmnxMobPdnS6bStatMessagesRx_Object = MibTableColumn
tmnxMobPdnS6bStatMessagesRx = _TmnxMobPdnS6bStatMessagesRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 25),
    _TmnxMobPdnS6bStatMessagesRx_Type()
)
tmnxMobPdnS6bStatMessagesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatMessagesRx.setStatus("current")
_TmnxMobPdnS6bStatCERMsgsTx_Type = Counter32
_TmnxMobPdnS6bStatCERMsgsTx_Object = MibTableColumn
tmnxMobPdnS6bStatCERMsgsTx = _TmnxMobPdnS6bStatCERMsgsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 26),
    _TmnxMobPdnS6bStatCERMsgsTx_Type()
)
tmnxMobPdnS6bStatCERMsgsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatCERMsgsTx.setStatus("current")
_TmnxMobPdnS6bStatCEAMsgsRx_Type = Counter32
_TmnxMobPdnS6bStatCEAMsgsRx_Object = MibTableColumn
tmnxMobPdnS6bStatCEAMsgsRx = _TmnxMobPdnS6bStatCEAMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 27),
    _TmnxMobPdnS6bStatCEAMsgsRx_Type()
)
tmnxMobPdnS6bStatCEAMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatCEAMsgsRx.setStatus("current")
_TmnxMobPdnS6bStatDPRMsgsTx_Type = Counter32
_TmnxMobPdnS6bStatDPRMsgsTx_Object = MibTableColumn
tmnxMobPdnS6bStatDPRMsgsTx = _TmnxMobPdnS6bStatDPRMsgsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 28),
    _TmnxMobPdnS6bStatDPRMsgsTx_Type()
)
tmnxMobPdnS6bStatDPRMsgsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatDPRMsgsTx.setStatus("current")
_TmnxMobPdnS6bStatDPRMsgsRx_Type = Counter32
_TmnxMobPdnS6bStatDPRMsgsRx_Object = MibTableColumn
tmnxMobPdnS6bStatDPRMsgsRx = _TmnxMobPdnS6bStatDPRMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 29),
    _TmnxMobPdnS6bStatDPRMsgsRx_Type()
)
tmnxMobPdnS6bStatDPRMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatDPRMsgsRx.setStatus("current")
_TmnxMobPdnS6bStatDPAMsgsTx_Type = Counter32
_TmnxMobPdnS6bStatDPAMsgsTx_Object = MibTableColumn
tmnxMobPdnS6bStatDPAMsgsTx = _TmnxMobPdnS6bStatDPAMsgsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 30),
    _TmnxMobPdnS6bStatDPAMsgsTx_Type()
)
tmnxMobPdnS6bStatDPAMsgsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatDPAMsgsTx.setStatus("current")
_TmnxMobPdnS6bStatDPAMsgsRx_Type = Counter32
_TmnxMobPdnS6bStatDPAMsgsRx_Object = MibTableColumn
tmnxMobPdnS6bStatDPAMsgsRx = _TmnxMobPdnS6bStatDPAMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 31),
    _TmnxMobPdnS6bStatDPAMsgsRx_Type()
)
tmnxMobPdnS6bStatDPAMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatDPAMsgsRx.setStatus("current")
_TmnxMobPdnS6bStatDWRMsgsTx_Type = Counter32
_TmnxMobPdnS6bStatDWRMsgsTx_Object = MibTableColumn
tmnxMobPdnS6bStatDWRMsgsTx = _TmnxMobPdnS6bStatDWRMsgsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 32),
    _TmnxMobPdnS6bStatDWRMsgsTx_Type()
)
tmnxMobPdnS6bStatDWRMsgsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatDWRMsgsTx.setStatus("current")
_TmnxMobPdnS6bStatDWRMsgsRx_Type = Counter32
_TmnxMobPdnS6bStatDWRMsgsRx_Object = MibTableColumn
tmnxMobPdnS6bStatDWRMsgsRx = _TmnxMobPdnS6bStatDWRMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 33),
    _TmnxMobPdnS6bStatDWRMsgsRx_Type()
)
tmnxMobPdnS6bStatDWRMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatDWRMsgsRx.setStatus("current")
_TmnxMobPdnS6bStatDWAMsgsTx_Type = Counter32
_TmnxMobPdnS6bStatDWAMsgsTx_Object = MibTableColumn
tmnxMobPdnS6bStatDWAMsgsTx = _TmnxMobPdnS6bStatDWAMsgsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 34),
    _TmnxMobPdnS6bStatDWAMsgsTx_Type()
)
tmnxMobPdnS6bStatDWAMsgsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatDWAMsgsTx.setStatus("current")
_TmnxMobPdnS6bStatDWAMsgsRx_Type = Counter32
_TmnxMobPdnS6bStatDWAMsgsRx_Object = MibTableColumn
tmnxMobPdnS6bStatDWAMsgsRx = _TmnxMobPdnS6bStatDWAMsgsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 35),
    _TmnxMobPdnS6bStatDWAMsgsRx_Type()
)
tmnxMobPdnS6bStatDWAMsgsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatDWAMsgsRx.setStatus("current")
_TmnxMobPdnS6bStatConnAttempts_Type = Counter32
_TmnxMobPdnS6bStatConnAttempts_Object = MibTableColumn
tmnxMobPdnS6bStatConnAttempts = _TmnxMobPdnS6bStatConnAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 36),
    _TmnxMobPdnS6bStatConnAttempts_Type()
)
tmnxMobPdnS6bStatConnAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatConnAttempts.setStatus("current")
_TmnxMobPdnS6bStatConnFailures_Type = Counter32
_TmnxMobPdnS6bStatConnFailures_Object = MibTableColumn
tmnxMobPdnS6bStatConnFailures = _TmnxMobPdnS6bStatConnFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 37),
    _TmnxMobPdnS6bStatConnFailures_Type()
)
tmnxMobPdnS6bStatConnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatConnFailures.setStatus("current")
_TmnxMobPdnS6bStatRxMsgUnexpctVer_Type = Counter32
_TmnxMobPdnS6bStatRxMsgUnexpctVer_Object = MibTableColumn
tmnxMobPdnS6bStatRxMsgUnexpctVer = _TmnxMobPdnS6bStatRxMsgUnexpctVer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 38),
    _TmnxMobPdnS6bStatRxMsgUnexpctVer_Type()
)
tmnxMobPdnS6bStatRxMsgUnexpctVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatRxMsgUnexpctVer.setStatus("current")
_TmnxMobPdnS6bStatRxMsgTooBig_Type = Counter32
_TmnxMobPdnS6bStatRxMsgTooBig_Object = MibTableColumn
tmnxMobPdnS6bStatRxMsgTooBig = _TmnxMobPdnS6bStatRxMsgTooBig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 39),
    _TmnxMobPdnS6bStatRxMsgTooBig_Type()
)
tmnxMobPdnS6bStatRxMsgTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatRxMsgTooBig.setStatus("current")
_TmnxMobPdnS6bStatRxMsgTooSmall_Type = Counter32
_TmnxMobPdnS6bStatRxMsgTooSmall_Object = MibTableColumn
tmnxMobPdnS6bStatRxMsgTooSmall = _TmnxMobPdnS6bStatRxMsgTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 40),
    _TmnxMobPdnS6bStatRxMsgTooSmall_Type()
)
tmnxMobPdnS6bStatRxMsgTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatRxMsgTooSmall.setStatus("current")
_TmnxMobPdnS6bStatRxInvalidCea_Type = Counter32
_TmnxMobPdnS6bStatRxInvalidCea_Object = MibTableColumn
tmnxMobPdnS6bStatRxInvalidCea = _TmnxMobPdnS6bStatRxInvalidCea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 41),
    _TmnxMobPdnS6bStatRxInvalidCea_Type()
)
tmnxMobPdnS6bStatRxInvalidCea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatRxInvalidCea.setStatus("current")
_TmnxMobPdnS6bStatTxRetrnsmitMsgs_Type = Counter32
_TmnxMobPdnS6bStatTxRetrnsmitMsgs_Object = MibTableColumn
tmnxMobPdnS6bStatTxRetrnsmitMsgs = _TmnxMobPdnS6bStatTxRetrnsmitMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 42),
    _TmnxMobPdnS6bStatTxRetrnsmitMsgs_Type()
)
tmnxMobPdnS6bStatTxRetrnsmitMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatTxRetrnsmitMsgs.setStatus("current")
_TmnxMobPdnS6bStatRxTransportDisc_Type = Counter32
_TmnxMobPdnS6bStatRxTransportDisc_Object = MibTableColumn
tmnxMobPdnS6bStatRxTransportDisc = _TmnxMobPdnS6bStatRxTransportDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 43),
    _TmnxMobPdnS6bStatRxTransportDisc_Type()
)
tmnxMobPdnS6bStatRxTransportDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bStatRxTransportDisc.setStatus("current")
_TmnxMobPdnS6bAARFinalTOTx_Type = Counter32
_TmnxMobPdnS6bAARFinalTOTx_Object = MibTableColumn
tmnxMobPdnS6bAARFinalTOTx = _TmnxMobPdnS6bAARFinalTOTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 44),
    _TmnxMobPdnS6bAARFinalTOTx_Type()
)
tmnxMobPdnS6bAARFinalTOTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bAARFinalTOTx.setStatus("current")
_TmnxMobPdnS6bSTRUnknownSessTx_Type = Counter32
_TmnxMobPdnS6bSTRUnknownSessTx_Object = MibTableColumn
tmnxMobPdnS6bSTRUnknownSessTx = _TmnxMobPdnS6bSTRUnknownSessTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 45),
    _TmnxMobPdnS6bSTRUnknownSessTx_Type()
)
tmnxMobPdnS6bSTRUnknownSessTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bSTRUnknownSessTx.setStatus("current")
_TmnxMobPdnS6bSTRFinalTOTx_Type = Counter32
_TmnxMobPdnS6bSTRFinalTOTx_Object = MibTableColumn
tmnxMobPdnS6bSTRFinalTOTx = _TmnxMobPdnS6bSTRFinalTOTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 46),
    _TmnxMobPdnS6bSTRFinalTOTx_Type()
)
tmnxMobPdnS6bSTRFinalTOTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bSTRFinalTOTx.setStatus("current")
_TmnxMobPdnS6bASAUnknownSessTx_Type = Counter32
_TmnxMobPdnS6bASAUnknownSessTx_Object = MibTableColumn
tmnxMobPdnS6bASAUnknownSessTx = _TmnxMobPdnS6bASAUnknownSessTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 47),
    _TmnxMobPdnS6bASAUnknownSessTx_Type()
)
tmnxMobPdnS6bASAUnknownSessTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bASAUnknownSessTx.setStatus("current")
_TmnxMobPdnS6bRAAUnknownSessTx_Type = Counter32
_TmnxMobPdnS6bRAAUnknownSessTx_Object = MibTableColumn
tmnxMobPdnS6bRAAUnknownSessTx = _TmnxMobPdnS6bRAAUnknownSessTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 48),
    _TmnxMobPdnS6bRAAUnknownSessTx_Type()
)
tmnxMobPdnS6bRAAUnknownSessTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bRAAUnknownSessTx.setStatus("current")
_TmnxMobPdnS6bAAAMalformedPktsRx_Type = Counter32
_TmnxMobPdnS6bAAAMalformedPktsRx_Object = MibTableColumn
tmnxMobPdnS6bAAAMalformedPktsRx = _TmnxMobPdnS6bAAAMalformedPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 49),
    _TmnxMobPdnS6bAAAMalformedPktsRx_Type()
)
tmnxMobPdnS6bAAAMalformedPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bAAAMalformedPktsRx.setStatus("current")
_TmnxMobPdnS6bAAABadAVPValue_Type = Counter32
_TmnxMobPdnS6bAAABadAVPValue_Object = MibTableColumn
tmnxMobPdnS6bAAABadAVPValue = _TmnxMobPdnS6bAAABadAVPValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 50),
    _TmnxMobPdnS6bAAABadAVPValue_Type()
)
tmnxMobPdnS6bAAABadAVPValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bAAABadAVPValue.setStatus("current")
_TmnxMobPdnS6bSTAMalformedPktsRx_Type = Counter32
_TmnxMobPdnS6bSTAMalformedPktsRx_Object = MibTableColumn
tmnxMobPdnS6bSTAMalformedPktsRx = _TmnxMobPdnS6bSTAMalformedPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 51),
    _TmnxMobPdnS6bSTAMalformedPktsRx_Type()
)
tmnxMobPdnS6bSTAMalformedPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bSTAMalformedPktsRx.setStatus("current")
_TmnxMobPdnS6bSTABadAVPValueRx_Type = Counter32
_TmnxMobPdnS6bSTABadAVPValueRx_Object = MibTableColumn
tmnxMobPdnS6bSTABadAVPValueRx = _TmnxMobPdnS6bSTABadAVPValueRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 52),
    _TmnxMobPdnS6bSTABadAVPValueRx_Type()
)
tmnxMobPdnS6bSTABadAVPValueRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bSTABadAVPValueRx.setStatus("current")
_TmnxMobPdnS6bRARBadAVPValueRx_Type = Counter32
_TmnxMobPdnS6bRARBadAVPValueRx_Object = MibTableColumn
tmnxMobPdnS6bRARBadAVPValueRx = _TmnxMobPdnS6bRARBadAVPValueRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 53),
    _TmnxMobPdnS6bRARBadAVPValueRx_Type()
)
tmnxMobPdnS6bRARBadAVPValueRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bRARBadAVPValueRx.setStatus("current")
_TmnxMobPdnS6bRARDuplicateRx_Type = Counter32
_TmnxMobPdnS6bRARDuplicateRx_Object = MibTableColumn
tmnxMobPdnS6bRARDuplicateRx = _TmnxMobPdnS6bRARDuplicateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 54),
    _TmnxMobPdnS6bRARDuplicateRx_Type()
)
tmnxMobPdnS6bRARDuplicateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bRARDuplicateRx.setStatus("current")
_TmnxMobPdnS6bASRBadAVPValueRx_Type = Counter32
_TmnxMobPdnS6bASRBadAVPValueRx_Object = MibTableColumn
tmnxMobPdnS6bASRBadAVPValueRx = _TmnxMobPdnS6bASRBadAVPValueRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 55),
    _TmnxMobPdnS6bASRBadAVPValueRx_Type()
)
tmnxMobPdnS6bASRBadAVPValueRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bASRBadAVPValueRx.setStatus("current")
_TmnxMobPdnS6bASRDuplicateRx_Type = Counter32
_TmnxMobPdnS6bASRDuplicateRx_Object = MibTableColumn
tmnxMobPdnS6bASRDuplicateRx = _TmnxMobPdnS6bASRDuplicateRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 2, 29, 1, 56),
    _TmnxMobPdnS6bASRDuplicateRx_Type()
)
tmnxMobPdnS6bASRDuplicateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bASRDuplicateRx.setStatus("current")
_TmnxMobPdnGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxMobPdnGlobalObjs = _TmnxMobPdnGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3)
)
_TmnxMobPdnTableLastChanged_Type = TimeStamp
_TmnxMobPdnTableLastChanged_Object = MibScalar
tmnxMobPdnTableLastChanged = _TmnxMobPdnTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 1),
    _TmnxMobPdnTableLastChanged_Type()
)
tmnxMobPdnTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnTableLastChanged.setStatus("current")
_TmnxMobPdnSigTableLastChanged_Type = TimeStamp
_TmnxMobPdnSigTableLastChanged_Object = MibScalar
tmnxMobPdnSigTableLastChanged = _TmnxMobPdnSigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 2),
    _TmnxMobPdnSigTableLastChanged_Type()
)
tmnxMobPdnSigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnSigTableLastChanged.setStatus("current")
_TmnxMobPdnGxTableLastChanged_Type = TimeStamp
_TmnxMobPdnGxTableLastChanged_Object = MibScalar
tmnxMobPdnGxTableLastChanged = _TmnxMobPdnGxTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 3),
    _TmnxMobPdnGxTableLastChanged_Type()
)
tmnxMobPdnGxTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxTableLastChanged.setStatus("current")
_TmnxMobPdnS5TableLastChanged_Type = TimeStamp
_TmnxMobPdnS5TableLastChanged_Object = MibScalar
tmnxMobPdnS5TableLastChanged = _TmnxMobPdnS5TableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 4),
    _TmnxMobPdnS5TableLastChanged_Type()
)
tmnxMobPdnS5TableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS5TableLastChanged.setStatus("current")
_TmnxMobPdnS8TableLastChanged_Type = TimeStamp
_TmnxMobPdnS8TableLastChanged_Object = MibScalar
tmnxMobPdnS8TableLastChanged = _TmnxMobPdnS8TableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 5),
    _TmnxMobPdnS8TableLastChanged_Type()
)
tmnxMobPdnS8TableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS8TableLastChanged.setStatus("current")
_TmnxMobPdnS2aTableLastChanged_Type = TimeStamp
_TmnxMobPdnS2aTableLastChanged_Object = MibScalar
tmnxMobPdnS2aTableLastChanged = _TmnxMobPdnS2aTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 6),
    _TmnxMobPdnS2aTableLastChanged_Type()
)
tmnxMobPdnS2aTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aTableLastChanged.setStatus("current")
_TmnxMobPdnRfTableLastChanged_Type = TimeStamp
_TmnxMobPdnRfTableLastChanged_Object = MibScalar
tmnxMobPdnRfTableLastChanged = _TmnxMobPdnRfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 7),
    _TmnxMobPdnRfTableLastChanged_Type()
)
tmnxMobPdnRfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRfTableLastChanged.setStatus("current")
_TmnxMobPdnPccBasePolTableLstChgd_Type = TimeStamp
_TmnxMobPdnPccBasePolTableLstChgd_Object = MibScalar
tmnxMobPdnPccBasePolTableLstChgd = _TmnxMobPdnPccBasePolTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 8),
    _TmnxMobPdnPccBasePolTableLstChgd_Type()
)
tmnxMobPdnPccBasePolTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnPccBasePolTableLstChgd.setStatus("current")
_TmnxMobPdnApnTableLastChanged_Type = TimeStamp
_TmnxMobPdnApnTableLastChanged_Object = MibScalar
tmnxMobPdnApnTableLastChanged = _TmnxMobPdnApnTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 9),
    _TmnxMobPdnApnTableLastChanged_Type()
)
tmnxMobPdnApnTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnTableLastChanged.setStatus("current")
_TmnxMobPdnApnExtTableLastChanged_Type = TimeStamp
_TmnxMobPdnApnExtTableLastChanged_Object = MibScalar
tmnxMobPdnApnExtTableLastChanged = _TmnxMobPdnApnExtTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 10),
    _TmnxMobPdnApnExtTableLastChanged_Type()
)
tmnxMobPdnApnExtTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnExtTableLastChanged.setStatus("current")
_TmnxMobPdnApnExt2TableLastChangd_Type = TimeStamp
_TmnxMobPdnApnExt2TableLastChangd_Object = MibScalar
tmnxMobPdnApnExt2TableLastChangd = _TmnxMobPdnApnExt2TableLastChangd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 11),
    _TmnxMobPdnApnExt2TableLastChangd_Type()
)
tmnxMobPdnApnExt2TableLastChangd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnExt2TableLastChangd.setStatus("current")
_TmnxMobPdnApnIpPoolTableLastChgd_Type = TimeStamp
_TmnxMobPdnApnIpPoolTableLastChgd_Object = MibScalar
tmnxMobPdnApnIpPoolTableLastChgd = _TmnxMobPdnApnIpPoolTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 12),
    _TmnxMobPdnApnIpPoolTableLastChgd_Type()
)
tmnxMobPdnApnIpPoolTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnIpPoolTableLastChgd.setStatus("current")
_TmnxMobPdnApnBasePolTableLstChgd_Type = TimeStamp
_TmnxMobPdnApnBasePolTableLstChgd_Object = MibScalar
tmnxMobPdnApnBasePolTableLstChgd = _TmnxMobPdnApnBasePolTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 13),
    _TmnxMobPdnApnBasePolTableLstChgd_Type()
)
tmnxMobPdnApnBasePolTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnBasePolTableLstChgd.setStatus("current")
_TmnxMobPdnGxPeerTableLastChngd_Type = TimeStamp
_TmnxMobPdnGxPeerTableLastChngd_Object = MibScalar
tmnxMobPdnGxPeerTableLastChngd = _TmnxMobPdnGxPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 14),
    _TmnxMobPdnGxPeerTableLastChngd_Type()
)
tmnxMobPdnGxPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGxPeerTableLastChngd.setStatus("current")
_TmnxMobPdnGaTableLastChanged_Type = TimeStamp
_TmnxMobPdnGaTableLastChanged_Object = MibScalar
tmnxMobPdnGaTableLastChanged = _TmnxMobPdnGaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 15),
    _TmnxMobPdnGaTableLastChanged_Type()
)
tmnxMobPdnGaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaTableLastChanged.setStatus("current")
_TmnxMobPdnGnTableLastChanged_Type = TimeStamp
_TmnxMobPdnGnTableLastChanged_Object = MibScalar
tmnxMobPdnGnTableLastChanged = _TmnxMobPdnGnTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 16),
    _TmnxMobPdnGnTableLastChanged_Type()
)
tmnxMobPdnGnTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnTableLastChanged.setStatus("current")
_TmnxMobPdnApTableLastChanged_Type = TimeStamp
_TmnxMobPdnApTableLastChanged_Object = MibScalar
tmnxMobPdnApTableLastChanged = _TmnxMobPdnApTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 17),
    _TmnxMobPdnApTableLastChanged_Type()
)
tmnxMobPdnApTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApTableLastChanged.setStatus("current")
_TmnxMobPdnGnPeerTableLastChanged_Type = TimeStamp
_TmnxMobPdnGnPeerTableLastChanged_Object = MibScalar
tmnxMobPdnGnPeerTableLastChanged = _TmnxMobPdnGnPeerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 18),
    _TmnxMobPdnGnPeerTableLastChanged_Type()
)
tmnxMobPdnGnPeerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGnPeerTableLastChanged.setStatus("current")
_TmnxMobPdnRadiusTableLastChanged_Type = TimeStamp
_TmnxMobPdnRadiusTableLastChanged_Object = MibScalar
tmnxMobPdnRadiusTableLastChanged = _TmnxMobPdnRadiusTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 19),
    _TmnxMobPdnRadiusTableLastChanged_Type()
)
tmnxMobPdnRadiusTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusTableLastChanged.setStatus("current")
_TmnxMobPdnApnDaccGrpTblLastChngd_Type = TimeStamp
_TmnxMobPdnApnDaccGrpTblLastChngd_Object = MibScalar
tmnxMobPdnApnDaccGrpTblLastChngd = _TmnxMobPdnApnDaccGrpTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 20),
    _TmnxMobPdnApnDaccGrpTblLastChngd_Type()
)
tmnxMobPdnApnDaccGrpTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnDaccGrpTblLastChngd.setStatus("current")
_TmnxMobPdnGyTableLastChanged_Type = TimeStamp
_TmnxMobPdnGyTableLastChanged_Object = MibScalar
tmnxMobPdnGyTableLastChanged = _TmnxMobPdnGyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 21),
    _TmnxMobPdnGyTableLastChanged_Type()
)
tmnxMobPdnGyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyTableLastChanged.setStatus("current")
_TmnxMobPdnRatingGrpTableLastChgd_Type = TimeStamp
_TmnxMobPdnRatingGrpTableLastChgd_Object = MibScalar
tmnxMobPdnRatingGrpTableLastChgd = _TmnxMobPdnRatingGrpTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 22),
    _TmnxMobPdnRatingGrpTableLastChgd_Type()
)
tmnxMobPdnRatingGrpTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRatingGrpTableLastChgd.setStatus("current")
_TmnxMobPdnGyPeerTableLastChngd_Type = TimeStamp
_TmnxMobPdnGyPeerTableLastChngd_Object = MibScalar
tmnxMobPdnGyPeerTableLastChngd = _TmnxMobPdnGyPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 23),
    _TmnxMobPdnGyPeerTableLastChngd_Type()
)
tmnxMobPdnGyPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyPeerTableLastChngd.setStatus("current")
_TmnxMobPdnGaPeerTableLastChngd_Type = TimeStamp
_TmnxMobPdnGaPeerTableLastChngd_Object = MibScalar
tmnxMobPdnGaPeerTableLastChngd = _TmnxMobPdnGaPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 24),
    _TmnxMobPdnGaPeerTableLastChngd_Type()
)
tmnxMobPdnGaPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGaPeerTableLastChngd.setStatus("current")
_TmnxMobPdnRadPeerTableLastChngd_Type = TimeStamp
_TmnxMobPdnRadPeerTableLastChngd_Object = MibScalar
tmnxMobPdnRadPeerTableLastChngd = _TmnxMobPdnRadPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 25),
    _TmnxMobPdnRadPeerTableLastChngd_Type()
)
tmnxMobPdnRadPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnRadPeerTableLastChngd.setStatus("current")
_TmnxMobPdnGpTableLastChanged_Type = TimeStamp
_TmnxMobPdnGpTableLastChanged_Object = MibScalar
tmnxMobPdnGpTableLastChanged = _TmnxMobPdnGpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 26),
    _TmnxMobPdnGpTableLastChanged_Type()
)
tmnxMobPdnGpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpTableLastChanged.setStatus("current")
_TmnxMobPdnGpPeerTableLastChanged_Type = TimeStamp
_TmnxMobPdnGpPeerTableLastChanged_Object = MibScalar
tmnxMobPdnGpPeerTableLastChanged = _TmnxMobPdnGpPeerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 27),
    _TmnxMobPdnGpPeerTableLastChanged_Type()
)
tmnxMobPdnGpPeerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGpPeerTableLastChanged.setStatus("current")
_TmnxMobPdnS2aPeerTblLastChanged_Type = TimeStamp
_TmnxMobPdnS2aPeerTblLastChanged_Object = MibScalar
tmnxMobPdnS2aPeerTblLastChanged = _TmnxMobPdnS2aPeerTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 28),
    _TmnxMobPdnS2aPeerTblLastChanged_Type()
)
tmnxMobPdnS2aPeerTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS2aPeerTblLastChanged.setStatus("current")
_TmnxMobPdnApnExt3TableLastChangd_Type = TimeStamp
_TmnxMobPdnApnExt3TableLastChangd_Object = MibScalar
tmnxMobPdnApnExt3TableLastChangd = _TmnxMobPdnApnExt3TableLastChangd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 29),
    _TmnxMobPdnApnExt3TableLastChangd_Type()
)
tmnxMobPdnApnExt3TableLastChangd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnApnExt3TableLastChangd.setStatus("current")
_TmnxMobPdnS6bPeerTableLastChngd_Type = TimeStamp
_TmnxMobPdnS6bPeerTableLastChngd_Object = MibScalar
tmnxMobPdnS6bPeerTableLastChngd = _TmnxMobPdnS6bPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 30),
    _TmnxMobPdnS6bPeerTableLastChngd_Type()
)
tmnxMobPdnS6bPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bPeerTableLastChngd.setStatus("current")
_TmnxMobPdnGyOcsTableLastChanged_Type = TimeStamp
_TmnxMobPdnGyOcsTableLastChanged_Object = MibScalar
tmnxMobPdnGyOcsTableLastChanged = _TmnxMobPdnGyOcsTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 31),
    _TmnxMobPdnGyOcsTableLastChanged_Type()
)
tmnxMobPdnGyOcsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnGyOcsTableLastChanged.setStatus("current")
_TmnxMobPdnS6bTableLastChanged_Type = TimeStamp
_TmnxMobPdnS6bTableLastChanged_Object = MibScalar
tmnxMobPdnS6bTableLastChanged = _TmnxMobPdnS6bTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 71, 3, 32),
    _TmnxMobPdnS6bTableLastChanged_Type()
)
tmnxMobPdnS6bTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobPdnS6bTableLastChanged.setStatus("current")
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnSigEntry")
)
tmnxMobPdnSigEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnGxEntry")
)
tmnxMobPdnGxEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnS5Entry")
)
tmnxMobPdnS5Entry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnS8Entry")
)
tmnxMobPdnS8Entry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnS2aEntry")
)
tmnxMobPdnS2aEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnRfEntry")
)
tmnxMobPdnRfEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnApnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnApnExtEntry")
)
tmnxMobPdnApnExtEntry.setIndexNames(*tmnxMobPdnApnEntry.getIndexNames())
tmnxMobPdnApnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnApnExt2Entry")
)
tmnxMobPdnApnExt2Entry.setIndexNames(*tmnxMobPdnApnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnGaEntry")
)
tmnxMobPdnGaEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnGnEntry")
)
tmnxMobPdnGnEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnRadiusEntry")
)
tmnxMobPdnRadiusEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnGyEntry")
)
tmnxMobPdnGyEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnGpEntry")
)
tmnxMobPdnGpEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnApnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnApnExt3Entry")
)
tmnxMobPdnApnExt3Entry.setIndexNames(*tmnxMobPdnApnEntry.getIndexNames())
tmnxMobPdnEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnS6bEntry")
)
tmnxMobPdnS6bEntry.setIndexNames(*tmnxMobPdnEntry.getIndexNames())
tmnxMobPdnStatEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnProcEntry")
)
tmnxMobPdnProcEntry.setIndexNames(*tmnxMobPdnStatEntry.getIndexNames())
tmnxMobPdnBearerContextEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnBcAcctGaEntry")
)
tmnxMobPdnBcAcctGaEntry.setIndexNames(*tmnxMobPdnBearerContextEntry.getIndexNames())
tmnxMobPdnBearerContextEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnBcAcctGyEntry")
)
tmnxMobPdnBcAcctGyEntry.setIndexNames(*tmnxMobPdnBearerContextEntry.getIndexNames())
tmnxMobPdnBearerContextEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnBcAcctRfEntry")
)
tmnxMobPdnBcAcctRfEntry.setIndexNames(*tmnxMobPdnBearerContextEntry.getIndexNames())
tmnxMobPdnPdnContextEntry.registerAugmentions(
    ("TIMETRA-MOBILE-PDN-MIB",
     "tmnxMobPdnPcAcctRfEntry")
)
tmnxMobPdnPcAcctRfEntry.setIndexNames(*tmnxMobPdnPdnContextEntry.getIndexNames())

# Managed Objects groups

tmnxMobPdnGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 1)
)
tmnxMobPdnGlobalGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5TableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnExtTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnExt2TableLastChangd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpPoolTableLastChgd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerTableLastChngd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPccBasePolTableLstChgd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnBasePolTableLstChgd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDaccGrpTblLastChngd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRatingGrpTableLastChgd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerTableLastChngd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaPeerTableLastChngd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnExt3TableLastChangd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerTableLastChngd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnGlobalGroup.setStatus("current")

tmnxMobPdnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 2)
)
tmnxMobPdnGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAdminState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnOperState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGracefulShutTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnMobNode"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPccDynamicState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPccPrecedenceBoundary"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUplinkQciPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnDownlinkQciPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigGtpcProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigGtpuProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigDiaOriginHost"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigDiaOriginRealm"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigDiaProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigDefaultIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigDefaultIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBearerGtpuUdpChecksum"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBearerGtpuSeqNumber"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxDiaIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxDiaIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxDiaTransTimer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxDiaRetryCount"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxDefPriDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxDefSecDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5LastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5PeerList"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5GtpcIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5GtpcIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5GtpuIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5GtpuIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5GtpcProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5GtpuProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS5DualStackPref"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPccBasePolRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUmtsQosPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigMIP6AgntInfType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigMIP6AgntInfFqdnType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigMIP6AgntInfFqdn"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigMIP6AgntInfRealm"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnGroup.setStatus("current")

tmnxMobPdnApnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 3)
)
tmnxMobPdnApnGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAdminState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnOperState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnGracefulShutTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnVirtualApnName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnTypeIpv4"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnTypeIpv6"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnTypeIpv4v6"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnAllocType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnRestrictionType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAllowMultiplePdns"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSelectSubscribed"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSelectMsProvided"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSelectNwProvided"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocLocalPool"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocHssStatic"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocAaa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocDhcpProxy"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocDhcpRelay"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocDhcpServer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcrfDynamicPcc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcrfPriDiameterPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcrfSecDiameterPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnUplinkQciPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDownlinkQciPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAggrRateUplink"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAggrRateDownlink"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIdleTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSessionTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnRejectForeignSub"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnBlockedPlmnList"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnUliReporting"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnExtLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDnsServerV4AddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDnsServerV4Addr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDnsServerV6AddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDnsServerV6Addr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRelayV4RouterId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRlyV4GiAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRelayV4GiAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRelayV6RouterId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRlyV6GiAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRelayV6GiAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpProxyV4RouterId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpPxyV4GiAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpProxyV4GiAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpProxyV6RouterId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpPxyV6GiAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpProxyV6GiAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV4PriAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV4PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV4SecAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV4SecAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV6PriAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV6PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV6SecAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV6SecAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoPcscfV4PriAdrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoPcscfV4PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoPcscfV6PriAdrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoPcscfV6PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV4PriAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV4PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV4SecAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV4SecAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV6PriAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV6PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV6SecAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV6SecAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnExt2LastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgProfileHome"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgProfileVisiting"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgProfileRoaming"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcIgnoreAny"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcIgnoreHome"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcIgnoreVisit"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcIgnoreRoaming"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnCdfPriDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnCdfSecDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPreAuthType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPreAuthUserName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthUserName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctUserName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctInterimReport"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpPoolRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnBasePolRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnUmtsQosPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcReject"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthServerGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthAcctSupImsi"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctServerGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnWaitAccounting"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPreAuthServerGroup"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnGroup.setStatus("obsolete")

tmnxMobPdnUnsupportedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 4)
)
tmnxMobPdnUnsupportedGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnHomePlmnList"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnVisitingPlmnList"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigPmipv6Profile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigPmipv6AddrScheme"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigPmipv6RtrAdIntvl"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnSigPmipv6RtrAdLife"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDescription"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnGracefulShutTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatVirtualApn"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnUnsupportedGroup.setStatus("current")

tmnxMobPdnChargingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 5)
)
tmnxMobPdnChargingGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingProfHome"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingProfVisiting"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingProfRoaming"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChrgCcIgnoreAny"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChrgCcIgnoreHome"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChrgCcIgnoreVisiting"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChrgCcIgnoreRoaming"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfPriDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfSecDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfAcctIntmInterval"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfApplTxTimer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfRetryCount"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfChargingGroupID"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOperatorString"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfAcctLevel"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfNodeId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcFilePrivateInfo"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcFileExtension"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcFileClosureSize"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcFileClsLifeTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcFileClsMaxAcrs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcFileObsoleteTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcPrimaryCf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcCf1State"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcCf1Limit"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcCf2State"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfOcCf2Limit"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChrgCcReject"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChrgNodeId"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnChargingGroup.setStatus("current")

tmnxMobPdnBcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 6)
)
tmnxMobPdnBcGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeMsIsdn"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImei"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeNai"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeNwkMcc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeNwkMnc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeTrackingAreaId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeCellId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeRat"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUePdnContexts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeBearerContexts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeRfPgwAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeRfPgwAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcLinkedBearerId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcApnRestriction"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcUlApnAmbr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcDlApnAmbr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcIpv4AddressType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcIpv4Address"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcIpv6AddressType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcIpv6Address"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcBearerContexts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSessionState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcLastEvent"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSigProtocol"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlRemoteCtrlTeid"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlRemoteCtrlAddrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlRemoteCtrlAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlRemV6CtrlAddrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlRemV6CtrlAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlLocalCtrlTeid"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlLocalCtrlAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlLocalCtrlAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlLocalV6CtrlAdrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlLocalV6CtrlAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcOfcBearerType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPcrfEventTriggers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcGxPcrfAddressType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcGxPcrfAddress"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcGxPgwAddressType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcGxPgwAddress"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcBearerType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcUpTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcQci"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcArp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcFilters"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlRemoteTeid"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlRemoteDataAddrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlRemoteDataAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlLocalTeid"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlLocalDataAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlLocalDataAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlDLPackets"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlDLBytes"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSgiULPackets"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSgiULBytes"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlDLPacketsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlDLPacketsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlDLBytesLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcTnlDLBytesHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSgiULPacketsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSgiULPacketsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSgiULBytesLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSgiULBytesHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcOfcServerAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcOfcServerAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcOfcServerState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcOfcChargingProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcOfcTriggeredRecords"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcOfcInterimRecords"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfPcrfPrecedence"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfRuleName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfPacketFilters"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfQosUlMbr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfQosDlMbr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfQosUlGbr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfQosDlGbr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterProtocol"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterSrcAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterSrcAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterSrcPfxLen"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterDstAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterDestAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterDestPfxLen"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterSrcPorts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFilterDestPorts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFirstSrcPortOper"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFirstSrcPortVal1"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFirstSrcPortVal2"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfSecndSrcPortOper"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfSecndSrcPortVal1"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfSecndSrcPortVal2"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFirstDstPortOper"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFirstDstPortVal1"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfFirstDstPortVal2"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfSecndDstPortOper"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfSecndDstPortVal1"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcSdfSecndDstPortVal2"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeCtxAccessType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeSubType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAccessType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAccessType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSelectionMode"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlLocalDataAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlLocalDataAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcPGWGREkey"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcMAGGREkey"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlRemoteDataAddrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlRemoteDataAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfSrvAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfSrvAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfServerState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChargingLevel"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChargingProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfInterimRecords"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfTriggeredRecords"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcPGWGreKey"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcMAGGreKey"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlDLPackets"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlDLBytes"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSgiULPackets"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSgiULBytes"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlDLPacketsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlDLPacketsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlDLBytesLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcTnlDLBytesHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSgiULPacketsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSgiULPacketsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSgiULBytesLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSgiULBytesHigh"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcGroup.setStatus("current")

tmnxMobPdnRefPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 7)
)
tmnxMobPdnRefPointGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerPathMgmtState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxPeerDetailState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxCer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCea"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxDpr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxDpa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxDwr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxDwa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatConnAttempts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatConnFailures"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxTransportDisc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxMsgUnexpectVer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxMsgTooBig"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxMsgTooSmall"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxInvalidCea"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxMsgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxMsgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxRetransmitMsgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxCcrInitial"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaInitial"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxCcrUpdate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaUpdate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxCcrTerminate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaTerminate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatCcrInitFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatCcrUpdateFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatCcrTermFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxRar"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxRaa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxRaaNack"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatBberfs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxMalformedPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaIMalformPkt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaUMalformPkt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaTMalformPkt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxRarMalformPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxUnknownPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaIUnknownPkt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaUUnknownPkt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaTUnknownPkt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxRarUnknownPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxMissingIePkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaIMissIePkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaUMissIePkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaTMissIePkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxRarMissIePkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaIUnkSession"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaUUnkSession"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaTUnkSession"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxRarUnkSession"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerPathMgmtState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerGatewayId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatCreatePdpReq"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatCreatePdpRsp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatDeletePdpReq"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatDeletePdpRsp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatModifyPdpReq"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatModifyPdpRsp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatRxEchoRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatTxEchoResponses"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatTxEchoRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatRxEchoResponses"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatRxErrorsIndCnt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatTxErrorsIndCnt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatRxMalformedPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatRxUnknownPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatRxMissingIePkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatPeerRestarts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatPeerRestrtCount"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnStatPathMgmtFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxEchoRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxEchoResponses"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxEchoRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxEchoResponses"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxNodeAlRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxNodeAlResps"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxDataRecReqs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxDataRecTferReq"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRetrDataRecReqs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxDataRecReqs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatUnackDataRexReqs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxRedirectionReq"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxRedrnResp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxInvalidMsgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxVerNotSupp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrTermination"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrMaxChngCond"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrMsTmzChng"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrRatChng"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrTimeLimit"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrVolLimit"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrReqAcc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrNoResAva"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrReqNotFf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrReqFfilled"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrDupReqFf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrInvMsgFmat"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrVerNotSupp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrSrvcNotSupp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrMandIeInc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrMandIeMiss"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrOptIeInc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxCdrSystemFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRtrEchoRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatGtpPrimeFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatOperState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatUpTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAARInitTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAARExtnTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAARDetachTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAARReauthTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAAAInitAtchRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAAAExtnRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAAADetachRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAAAReauthRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAAASuccessRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAAARejectRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatRARequestRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatRAAnswerTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatSTRequestTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatSTAnswerRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatASRequestRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatASAnswerTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAAAMissAVPPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatRARMissAVPPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatSTAMissAVPPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatASRMissAVPPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAAAUnknSesPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatAARRetries"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatSTRRetries"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatMessagesTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatMessagesRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatCERMsgsTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatCEAMsgsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatDPRMsgsTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatDPRMsgsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatDPAMsgsTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatDPAMsgsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatDWRMsgsTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatDWRMsgsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatDWAMsgsTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatDWAMsgsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerPathMgmtState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bPeerDetailState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatConnAttempts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatConnFailures"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatRxMsgUnexpctVer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatRxMsgTooBig"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatRxMsgTooSmall"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatRxInvalidCea"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatTxRetrnsmitMsgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bStatRxTransportDisc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxDpr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxDpa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxDwr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatTxDwa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bAARFinalTOTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bSTRUnknownSessTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bSTRFinalTOTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bASAUnknownSessTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bRAAUnknownSessTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bAAAMalformedPktsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bSTAMalformedPktsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bAAABadAVPValue"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bSTABadAVPValueRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bRARBadAVPValueRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bRARDuplicateRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bASRBadAVPValueRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bASRDuplicateRx"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnRefPointGroup.setStatus("current")

tmnxMobPdnStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 8)
)
tmnxMobPdnStatGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatBearers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatDedicatedBearers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatDefaultBearers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpLocalPools"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpv4Bearers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpv4Sdf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpv4PdnSessions"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpv4v6Bearers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpv4v6PdnSessions"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpv6Bearers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpv6Sdf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatIpv6PdnSessions"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatRealApn"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatRoamers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatPdnSessions"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatVPRNs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcDetach"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcDetachFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcHssQosModify"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcHssQosModifyFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcNwDedBrActv"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcNwDedBrActvFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcNwDedBrDeActv"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcNwDedBrDeActvFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcNwDedBrModify"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcNwDedBrModifyFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcPcrfQosModify"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcPcrfQosModifyFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcPgwPdnSessDel"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcPgwPdnSessDelFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcAttach"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcAttachFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcSgwReloc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcSgwRelocFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcUeDedBrActv"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcUeDedBrActvFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcUeDedBrDeActv"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcUeDedBrDeActvFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcUeDedBrModify"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcUeDedBrModifyFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatGnSgsns"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnStatGroup.setStatus("current")

tmnxMobPdnGgsnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 9)
)
tmnxMobPdnGgsnGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaGtpcProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaGtpPrimeGrpName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnGtpcIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnGtpcIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnGtpuIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnGtpuIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnGtpcProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnGtpuProfile"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnGgsnGroup.setStatus("current")

tmnxMobPdnApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 10)
)
tmnxMobPdnApGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApCollectAcctStats"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnApGroup.setStatus("current")

tmnxMobPdnRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 11)
)
tmnxMobPdnRadiusGroup.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusDisconnect"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDaccGrpRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDaccGrpLastChngd"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusGroup.setStatus("current")

tmnxMobPdnApnV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 12)
)
tmnxMobPdnApnV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnOcsPriDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnOcsSecDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnGyDccaProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChangeRepAction"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSuppFramedRoute"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPccQciValue"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPccArpValue"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnHttpRedirect"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthPriDiamPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthSecDiamPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthFixUserName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthFixPassword"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDefAppProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnRedirTrafficPol"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnRedirPolRouterInst"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnRedirPolNHopAddrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnRedirPolNHopAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAllowEmergency"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnV3v0Group.setStatus("current")

tmnxMobPdnGyV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 13)
)
tmnxMobPdnGyV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPriDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGySecDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyDccaProf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRatingGrpRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRatingGrpLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRatingGrpActvtThresold"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyV3v0Group.setStatus("current")

tmnxMobPdnGyStatsV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 14)
)
tmnxMobPdnGyStatsV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerPathMgmtState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerDetailState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcrGranted"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcrDenied"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcrInitialMsgTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcrUpdateMsgTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcrTermMsgTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaInitialMsgRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaUpdateMsgRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaTermMsgRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcrInitMsgFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcrUpdMsgFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcrTermMsgFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatAsrMsgRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatAsaMsgTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatAsaNackMsgTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRarMsgRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRaaMsgTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRaaNackMsgTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatMalformedPktsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCCAInitMalfPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCCAUpdtMalfPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCCATermMalfPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRarMalfPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatAsrMalfPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatUnkwnPktsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaInitUnkPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaUpdUnkPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaTermUnkPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRarUnkPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatAsrUnkPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatMissingAvpPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaIMisAvpPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaUMisAvpPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaTMisAvpPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRarMisAvpPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatAsrMisAvpPktRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaIUnkSessPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaUUnkSessPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatCcaTUnkSessPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRarUnkSessPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatAsrUnkSessPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatTxCer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxCea"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxDpr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatTxDpa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatTxDwr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxDwa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatConnAttempts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatConnFailures"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxTransportDisc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxMsgUnexpectVer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxMsgTooBig"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxMsgTooSmall"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxInvalidCea"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxMsgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatTxMsgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatTxRetransmitMsgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatTxDpr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxDpa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatRxDwr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatTxDwa"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnGyStatsV3v0Group.setStatus("current")

tmnxMobPdnGlobalV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 15)
)
tmnxMobPdnGlobalV3Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDaccGrpTblLastChngd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRatingGrpTableLastChgd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyPeerTableLastChngd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerTableLastChngd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerTblLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnGlobalV3Group.setStatus("current")

tmnxMobPdnAAGrpV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 16)
)
tmnxMobPdnAAGrpV3Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAaGroupIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAaGrpPartIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAaGroupIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAaGrpPartIndex"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnAAGrpV3Group.setStatus("current")

tmnxMobPdnRefPointV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 17)
)
tmnxMobPdnRefPointV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxNodeAlRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatRxNodeAlResps"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatNodeAlReqRetried"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatCdrsTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatCdrsRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaPeerLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaPeerCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaPeerPathMgmtState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaPeerDetailState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrPlmnChange"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrSerNdChLmt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxVerNotSupp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerPathMgmtState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerGatewayId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatCreatePdpReq"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatCreatePdpRsp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatDeletePdpReq"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatDeletePdpRsp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatModifyPdpReq"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatModifyPdpRsp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatRxEchoRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatTxEchoResponses"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatTxEchoRequests"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatRxEchoResponses"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatRxErrorsIndCnt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatTxErrorsIndCnt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatRxMalformedPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatRxUnknownPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatRxMissingIePkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatPeerRestarts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatPeerRestrtCount"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpStatPathMgmtFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerPathMgmtState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerGatewayId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatPeerRestart"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatPathMgmtFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatPeerRestartCnt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatHeartBeatReqTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatHeartBeatReqRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatHeartBeatRespTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatHeartBeatRespRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatPbu"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatBri"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatRxMalformedPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatRxMissingIePkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatRxUnknownPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatPbaFailure"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatBraFailure"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatPbaSuccess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatBraSuccess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGaStatTxCdrMgmtInterv"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aStatHBCompatible"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerHBCompatible"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnRefPointV3v0Group.setStatus("current")

tmnxMobPdnChargingV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 18)
)
tmnxMobPdnChargingV3Group.setObjects(
    ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnCdrType")
)
if mibBuilder.loadTexts:
    tmnxMobPdnChargingV3Group.setStatus("current")

tmnxMobPdnGgsnV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 19)
)
tmnxMobPdnGgsnV3Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGnPeerList"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpGtpcIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpGtpcIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpGtpuIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpGtpuIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpGtpcProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpGtpuProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGpPeerList"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnGgsnV3Group.setStatus("current")

tmnxMobPdnStatV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 20)
)
tmnxMobPdnStatV3Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcAttachPiggyBack"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatHomers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatVisitors"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdneHRPDAttachSuccess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdneHRPDAttachFailure"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdneHRPDDetachSuccess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdneHRPDDetachFailure"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdneHRPDToLTEHandOverSucc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdneHRPDToLTEHandOverFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnLTEToeHRPDHandOverSucc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnLTEToeHRPDHandOverFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnInterHSGWHandOvrSucc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnInterHSGWHandOvrFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatHSSStaticIpv4Sess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatHSSStaticIpv6Sess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatHSSSttIpv4v6Sess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStateHRPDPDNSess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatLTEPDNSess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStat2G3GPDNSess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatNumSuspendedPDN"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcPDNSuspendNotice"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcPDNResumeNotice"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcPDNIRSRP"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcEmergncyAttachSuc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatEmergencyPdnSess"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcMmeDedBrDeActiv"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcMmeDedBrDeAcFails"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcSessDeactDueToSt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnProcSessDeactDueToIt"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnInterRat3gToEutranSucc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnInterRat3gToEutranFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnInterRatEutranTo3gSucc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnInterRatEutranTo3gFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatRfPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatRfAcctStartBuf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatRfAcctIntBuf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatRfAcctStopBuf"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdneHRPDSessDeactSessTO"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdneHRPDSessDeactIdleTO"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnStatV3Group.setStatus("current")

tmnxMobPdnRadiusStatsV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 21)
)
tmnxMobPdnRadiusStatsV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerCreateTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerPathMgmtState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadPeerDetailState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatAccessReqTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatAccessAcceptRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatAccessRejectRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatAcctReqStartTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatAcctReqIntrmTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatAcctReqStopTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatAcctResponseRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatMandAttrMissing"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatMandAttrErrors"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatUnsupportedAttr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatOptionalAttrErr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatAuthError"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatUnexpectedCode"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatRespTimeBelow1"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatRespTime1to4"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatRespTimeAbove4"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatRetries"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatPrFinalTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatDiscReqRx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatDiscAckTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatDiscNakTx"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatDiscMandAtrMiss"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatDiscUnsupprAttr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatDiscSessNotFnd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatDiscAuthError"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatDiscUnexpcCode"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadStatMsgFinalTimeout"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnRadiusStatsV3v0Group.setStatus("current")

tmnxMobPdnS2aV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 22)
)
tmnxMobPdnS2aV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aPeerList"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aIfPmipv6RtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aIfPmipv6Interface"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aIfPmipv6Profile"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnS2aV3v0Group.setStatus("current")

tmnxMobPdnObsoletedV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 23)
)
tmnxMobPdnObsoletedV3Group.setObjects(
    ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthAcctSupImsi")
)
if mibBuilder.loadTexts:
    tmnxMobPdnObsoletedV3Group.setStatus("current")

tmnxMobPdnThresV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 24)
)
tmnxMobPdnThresV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtLmtUe"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtLmtBr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtLmtDefBr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtLmtDedBr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtLmtActBr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtLmtUePgd"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtCfsAttch"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtCfsDedBr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtCfsReloc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtCffAttch"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtCffDedBr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtCffHdOver"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrMgmtCffSrUnavl"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrTrfcThrptUL"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrTrfcThrptDL"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrTrfcAspFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresBrTrfcBrBdvErr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresPthMgmtS5Fail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresPthMgmtS5Restart"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresPthMgmtS5NoResp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresPthMgmtS5Peer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresPthMgmtS8Peer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresPthMgmtGxFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresPthMgmtRfFail"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnThresV3v0Group.setStatus("current")

tmnxMobPdnV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 25)
)
tmnxMobPdnV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnHttpRedirect"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8TableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8LastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8PeerList"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8GtpcIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8GtpcIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8GtpuIfVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8GtpuIfIndex"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8GtpcProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8GtpuProfile"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS8DualStackPref"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnDefAppProfile"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnV3v0Group.setStatus("current")

tmnxMobPdnApnV3v5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 26)
)
tmnxMobPdnApnV3v5Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAdminState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnOperState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnGracefulShutTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnVRtrId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnVirtualApnName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnTypeIpv4"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnTypeIpv6"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnTypeIpv4v6"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnAllocType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPdnRestrictionType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAllowMultiplePdns"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSelectSubscribed"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSelectMsProvided"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSelectNwProvided"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocLocalPool"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocHssStatic"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocAaa"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocDhcpProxy"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocDhcpRelay"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpAllocDhcpServer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcrfDynamicPcc"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcrfPriDiameterPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcrfSecDiameterPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnUplinkQciPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDownlinkQciPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAggrRateUplink"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAggrRateDownlink"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIdleTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnSessionTimeout"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnRejectForeignSub"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnBlockedPlmnList"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnUliReporting"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnExtLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDnsServerV4AddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDnsServerV4Addr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDnsServerV6AddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDnsServerV6Addr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRelayV4RouterId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRlyV4GiAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRelayV4GiAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRelayV6RouterId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRlyV6GiAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpRelayV6GiAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpProxyV4RouterId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpPxyV4GiAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpProxyV4GiAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpProxyV6RouterId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpPxyV6GiAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnDhcpProxyV6GiAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV4PriAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV4PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV4SecAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV4SecAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV6PriAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV6PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV6SecAddrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoDnsV6SecAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoPcscfV4PriAdrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoPcscfV4PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoPcscfV6PriAdrTyp"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoPcscfV6PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV4PriAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV4PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV4SecAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV4SecAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV6PriAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV6PriAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV6SecAdrType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcoNbnsV6SecAddr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnExt2LastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgProfileHome"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgProfileVisiting"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgProfileRoaming"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcIgnoreAny"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcIgnoreHome"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcIgnoreVisit"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcIgnoreRoaming"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnCdfPriDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnCdfSecDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPreAuthType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPreAuthUserName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthUserName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctUserName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctInterimReport"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnIpPoolRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnBasePolRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnUmtsQosPolName"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnChrgCcReject"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthServerGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctServerGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnWaitAccounting"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPreAuthServerGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAuthSupImsi"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnAcctSupImsi"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPreAuthSupImsi"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnExt3LastChanged"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnV3v5Group.setStatus("current")

tmnxMobPdnAcctStatsV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 27)
)
tmnxMobPdnAcctStatsV3Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaChargingId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaUlSustRate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaDlSustRate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrUlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrUlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrUlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrDlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrDlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrDlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrUlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrUlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrUlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrDlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrDlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaAggrDlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaNumPartCdrs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaNumContainers"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaNumMaxChanges"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaNumRgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGaNumOfRgSvcId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgOnlnCharging"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgOfflnCharging"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgUlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgUlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgUlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgDlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgDlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgDlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgUlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgUlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgUlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgDlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgDlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGaChrgDlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyChargingId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyUlSustRate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyDlSustRate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrUlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrUlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrUlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrDlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrDlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrDlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrUlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrUlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrUlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrDlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrDlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyAggrDlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyNumRedirection"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyLastRedctTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyNumCreditsRepl"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyLstCrdReplTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyNumRgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctGyNumOfRgSvcId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgTimeGranted"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgTimeUsed"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntTtlOct"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntTtlOctLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntTtlOctHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntInOct"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntInOctLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntInOctHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntOutOct"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntOutOctLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgGrntOutOctHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedTtlOct"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedTtlOctLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedTtlOctHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedInOct"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedInOctLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedInOctHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedOutOct"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedOutOctLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgUsedOutOctHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfChargingId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfUlSustRate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfDlSustRate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrUlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrUlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrUlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrDlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrDlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrDlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrUlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrUlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrUlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrDlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrDlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfAggrDlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfNumInterimSent"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfNumRgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcAcctRfNumOfRgSvcId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrUlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrUlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrUlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrDlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrDlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrDlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrUlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrUlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrUlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrDlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrDlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfAggrDlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfUlAvgRate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfDlAvgRate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfNumInterimSent"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfNumRgs"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcAcctRfNumOfRgSvcId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgOnlnCharging"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgOfflnCharging"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgUlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgUlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgUlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgDlPkts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgDlPktsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgDlPktsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgUlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgUlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgUlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgDlByts"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgDlBytsLow"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRfChrgDlBytsHigh"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgRatingGrpState"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgTimeBasedRep"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgVolumeBasedRep"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgQctPresent"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgQctGranted"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgQhtPresent"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgQhtGranted"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgQhtRemaining"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgQvtPresent"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgQvtRemaining"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgTtcPresent"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgTarrifTimeChng"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgFuiPresent"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgOnlineEnabled"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgTimeThreshold"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgVolThreshold"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgTrigger"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgActvThreshold"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgRedServerType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgRedServer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgBillingMethod"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgReportingLevel"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGyChrgResultCode"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnAcctStatsV3Group.setStatus("current")

tmnxMobPdnBcV3v5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 28)
)
tmnxMobPdnBcV3v5Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnKeyType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcImsiAuthStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcImeiStr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcImsiStr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUeImsiStr"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSessConfigTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSessRemExpTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcSessTimeDerivedFrom"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcIdleConfigTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcIdleRemExpTime"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcIdleTimeDerivedFrom"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnPcRefPointType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcRefPointType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcChargingChar"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcQosBytes"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnBcV3v5Group.setStatus("current")

tmnxMobPdnRefPointV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 29)
)
tmnxMobPdnRefPointV4v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaInitialFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaUpdateFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatRxCcaTermFail"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatReTxCcrInitial"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatReTxCcrUpdate"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGxStatReTxCcrTerm"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnRefPointV4v0Group.setStatus("current")

tmnxMobPdnOnlineChargV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 30)
)
tmnxMobPdnOnlineChargV4v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsTableLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyDiaSession"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsSelIdType"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsSelIdMappingStyle"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsRowStatus"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsUeStartId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsUeEndId"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsPriDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsSecDiaPeer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyOcsDccaProf"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnOnlineChargV4v0Group.setStatus("current")

tmnxMobPdnApnV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 31)
)
tmnxMobPdnApnV4v0Group.setObjects(
    ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnPcrfDynPccFHSession")
)
if mibBuilder.loadTexts:
    tmnxMobPdnApnV4v0Group.setStatus("current")

tmnxMobPdnS6bV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 32)
)
tmnxMobPdnS6bV4v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bLastChanged"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bTransactionTimer"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bRetryCount"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnS6bV4v0Group.setStatus("current")

tmnxMobPdnV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 2, 33)
)
tmnxMobPdnV4v0Group.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingAvpDiag"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRfSuppVendorAvps"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnV4v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxMobPdnV1v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 1, 1)
)
tmnxMobPdnV1v0Compliance.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApGroup"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnV1v0Compliance.setStatus(
        "obsolete"
    )

tmnxMobPdnV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 1, 2)
)
tmnxMobPdnV3v0Compliance.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatsV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAAGrpV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusStatsV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnV3v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxMobPdnV3v5Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 1, 3)
)
tmnxMobPdnV3v5Compliance.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatsV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAAGrpV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusStatsV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnV3v5Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAcctStatsV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcV3v5Group"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnV3v5Compliance.setStatus(
        "obsolete"
    )

tmnxMobPdn7xxxV10v0Compl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 1, 4)
)
tmnxMobPdn7xxxV10v0Compl.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAAGrpV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAcctStatsV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnV3v5Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcV3v5Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatsV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusStatsV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointV4v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUnsupportedGroup"))
)
if mibBuilder.loadTexts:
    tmnxMobPdn7xxxV10v0Compl.setStatus(
        "current"
    )

tmnxMobPdnV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 71, 1, 5)
)
tmnxMobPdnV4v0Compliance.setObjects(
      *(("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAAGrpV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnAcctStatsV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnV3v5Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnApnV4v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnBcV3v5Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnChargingV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGgsnV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGlobalV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyStatsV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnGyV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRadiusStatsV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnRefPointV4v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS2aV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnStatV3Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnThresV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnV3v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnUnsupportedGroup"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnOnlineChargV4v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnS6bV4v0Group"),
        ("TIMETRA-MOBILE-PDN-MIB", "tmnxMobPdnV4v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMobPdnV4v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MOBILE-PDN-MIB",
    **{"timetraMobPdnMIBModule": timetraMobPdnMIBModule,
       "tmnxMobPdnConformance": tmnxMobPdnConformance,
       "tmnxMobPdnCompliances": tmnxMobPdnCompliances,
       "tmnxMobPdnV1v0Compliance": tmnxMobPdnV1v0Compliance,
       "tmnxMobPdnV3v0Compliance": tmnxMobPdnV3v0Compliance,
       "tmnxMobPdnV3v5Compliance": tmnxMobPdnV3v5Compliance,
       "tmnxMobPdn7xxxV10v0Compl": tmnxMobPdn7xxxV10v0Compl,
       "tmnxMobPdnV4v0Compliance": tmnxMobPdnV4v0Compliance,
       "tmnxMobPdnGroups": tmnxMobPdnGroups,
       "tmnxMobPdnGlobalGroup": tmnxMobPdnGlobalGroup,
       "tmnxMobPdnGroup": tmnxMobPdnGroup,
       "tmnxMobPdnApnGroup": tmnxMobPdnApnGroup,
       "tmnxMobPdnUnsupportedGroup": tmnxMobPdnUnsupportedGroup,
       "tmnxMobPdnChargingGroup": tmnxMobPdnChargingGroup,
       "tmnxMobPdnBcGroup": tmnxMobPdnBcGroup,
       "tmnxMobPdnRefPointGroup": tmnxMobPdnRefPointGroup,
       "tmnxMobPdnStatGroup": tmnxMobPdnStatGroup,
       "tmnxMobPdnGgsnGroup": tmnxMobPdnGgsnGroup,
       "tmnxMobPdnApGroup": tmnxMobPdnApGroup,
       "tmnxMobPdnRadiusGroup": tmnxMobPdnRadiusGroup,
       "tmnxMobPdnApnV3v0Group": tmnxMobPdnApnV3v0Group,
       "tmnxMobPdnGyV3v0Group": tmnxMobPdnGyV3v0Group,
       "tmnxMobPdnGyStatsV3v0Group": tmnxMobPdnGyStatsV3v0Group,
       "tmnxMobPdnGlobalV3Group": tmnxMobPdnGlobalV3Group,
       "tmnxMobPdnAAGrpV3Group": tmnxMobPdnAAGrpV3Group,
       "tmnxMobPdnRefPointV3v0Group": tmnxMobPdnRefPointV3v0Group,
       "tmnxMobPdnChargingV3Group": tmnxMobPdnChargingV3Group,
       "tmnxMobPdnGgsnV3Group": tmnxMobPdnGgsnV3Group,
       "tmnxMobPdnStatV3Group": tmnxMobPdnStatV3Group,
       "tmnxMobPdnRadiusStatsV3v0Group": tmnxMobPdnRadiusStatsV3v0Group,
       "tmnxMobPdnS2aV3v0Group": tmnxMobPdnS2aV3v0Group,
       "tmnxMobPdnObsoletedV3Group": tmnxMobPdnObsoletedV3Group,
       "tmnxMobPdnThresV3v0Group": tmnxMobPdnThresV3v0Group,
       "tmnxMobPdnV3v0Group": tmnxMobPdnV3v0Group,
       "tmnxMobPdnApnV3v5Group": tmnxMobPdnApnV3v5Group,
       "tmnxMobPdnAcctStatsV3Group": tmnxMobPdnAcctStatsV3Group,
       "tmnxMobPdnBcV3v5Group": tmnxMobPdnBcV3v5Group,
       "tmnxMobPdnRefPointV4v0Group": tmnxMobPdnRefPointV4v0Group,
       "tmnxMobPdnOnlineChargV4v0Group": tmnxMobPdnOnlineChargV4v0Group,
       "tmnxMobPdnApnV4v0Group": tmnxMobPdnApnV4v0Group,
       "tmnxMobPdnS6bV4v0Group": tmnxMobPdnS6bV4v0Group,
       "tmnxMobPdnV4v0Group": tmnxMobPdnV4v0Group,
       "tmnxMobPdn": tmnxMobPdn,
       "tmnxMobPdnConfObjs": tmnxMobPdnConfObjs,
       "tmnxMobPdnTable": tmnxMobPdnTable,
       "tmnxMobPdnEntry": tmnxMobPdnEntry,
       "tmnxMobPdnLastChanged": tmnxMobPdnLastChanged,
       "tmnxMobPdnAdminState": tmnxMobPdnAdminState,
       "tmnxMobPdnOperState": tmnxMobPdnOperState,
       "tmnxMobPdnGracefulShutTimeout": tmnxMobPdnGracefulShutTimeout,
       "tmnxMobPdnMobNode": tmnxMobPdnMobNode,
       "tmnxMobPdnPccDynamicState": tmnxMobPdnPccDynamicState,
       "tmnxMobPdnPccPrecedenceBoundary": tmnxMobPdnPccPrecedenceBoundary,
       "tmnxMobPdnUplinkQciPolName": tmnxMobPdnUplinkQciPolName,
       "tmnxMobPdnDownlinkQciPolName": tmnxMobPdnDownlinkQciPolName,
       "tmnxMobPdnHomePlmnList": tmnxMobPdnHomePlmnList,
       "tmnxMobPdnVisitingPlmnList": tmnxMobPdnVisitingPlmnList,
       "tmnxMobPdnBearerGtpuUdpChecksum": tmnxMobPdnBearerGtpuUdpChecksum,
       "tmnxMobPdnBearerGtpuSeqNumber": tmnxMobPdnBearerGtpuSeqNumber,
       "tmnxMobPdnChargingProfHome": tmnxMobPdnChargingProfHome,
       "tmnxMobPdnChargingProfVisiting": tmnxMobPdnChargingProfVisiting,
       "tmnxMobPdnChargingProfRoaming": tmnxMobPdnChargingProfRoaming,
       "tmnxMobPdnChrgCcIgnoreAny": tmnxMobPdnChrgCcIgnoreAny,
       "tmnxMobPdnChrgCcIgnoreHome": tmnxMobPdnChrgCcIgnoreHome,
       "tmnxMobPdnChrgCcIgnoreVisiting": tmnxMobPdnChrgCcIgnoreVisiting,
       "tmnxMobPdnChrgCcIgnoreRoaming": tmnxMobPdnChrgCcIgnoreRoaming,
       "tmnxMobPdnUmtsQosPolName": tmnxMobPdnUmtsQosPolName,
       "tmnxMobPdnChrgCcReject": tmnxMobPdnChrgCcReject,
       "tmnxMobPdnChrgNodeId": tmnxMobPdnChrgNodeId,
       "tmnxMobPdnAaGroupIndex": tmnxMobPdnAaGroupIndex,
       "tmnxMobPdnAaGrpPartIndex": tmnxMobPdnAaGrpPartIndex,
       "tmnxMobPdnCdrType": tmnxMobPdnCdrType,
       "tmnxMobPdnHttpRedirect": tmnxMobPdnHttpRedirect,
       "tmnxMobPdnDefAppProfile": tmnxMobPdnDefAppProfile,
       "tmnxMobPdnChargingAvpDiag": tmnxMobPdnChargingAvpDiag,
       "tmnxMobPdnSigTable": tmnxMobPdnSigTable,
       "tmnxMobPdnSigEntry": tmnxMobPdnSigEntry,
       "tmnxMobPdnSigLastChanged": tmnxMobPdnSigLastChanged,
       "tmnxMobPdnSigGtpcProfile": tmnxMobPdnSigGtpcProfile,
       "tmnxMobPdnSigGtpuProfile": tmnxMobPdnSigGtpuProfile,
       "tmnxMobPdnSigPmipv6Profile": tmnxMobPdnSigPmipv6Profile,
       "tmnxMobPdnSigPmipv6RtrAdIntvl": tmnxMobPdnSigPmipv6RtrAdIntvl,
       "tmnxMobPdnSigPmipv6RtrAdLife": tmnxMobPdnSigPmipv6RtrAdLife,
       "tmnxMobPdnSigPmipv6AddrScheme": tmnxMobPdnSigPmipv6AddrScheme,
       "tmnxMobPdnSigDiaProfile": tmnxMobPdnSigDiaProfile,
       "tmnxMobPdnSigDiaOriginRealm": tmnxMobPdnSigDiaOriginRealm,
       "tmnxMobPdnSigDiaOriginHost": tmnxMobPdnSigDiaOriginHost,
       "tmnxMobPdnSigDefaultIfVRtrId": tmnxMobPdnSigDefaultIfVRtrId,
       "tmnxMobPdnSigDefaultIfIndex": tmnxMobPdnSigDefaultIfIndex,
       "tmnxMobPdnSigMIP6AgntInfType": tmnxMobPdnSigMIP6AgntInfType,
       "tmnxMobPdnSigMIP6AgntInfFqdnType": tmnxMobPdnSigMIP6AgntInfFqdnType,
       "tmnxMobPdnSigMIP6AgntInfFqdn": tmnxMobPdnSigMIP6AgntInfFqdn,
       "tmnxMobPdnSigMIP6AgntInfRealm": tmnxMobPdnSigMIP6AgntInfRealm,
       "tmnxMobPdnGxTable": tmnxMobPdnGxTable,
       "tmnxMobPdnGxEntry": tmnxMobPdnGxEntry,
       "tmnxMobPdnGxLastChanged": tmnxMobPdnGxLastChanged,
       "tmnxMobPdnGxDiaIfVRtrId": tmnxMobPdnGxDiaIfVRtrId,
       "tmnxMobPdnGxDiaIfIndex": tmnxMobPdnGxDiaIfIndex,
       "tmnxMobPdnGxDiaTransTimer": tmnxMobPdnGxDiaTransTimer,
       "tmnxMobPdnGxDiaRetryCount": tmnxMobPdnGxDiaRetryCount,
       "tmnxMobPdnGxDefPriDiaPeer": tmnxMobPdnGxDefPriDiaPeer,
       "tmnxMobPdnGxDefSecDiaPeer": tmnxMobPdnGxDefSecDiaPeer,
       "tmnxMobPdnS5Table": tmnxMobPdnS5Table,
       "tmnxMobPdnS5Entry": tmnxMobPdnS5Entry,
       "tmnxMobPdnS5LastChanged": tmnxMobPdnS5LastChanged,
       "tmnxMobPdnS5PeerList": tmnxMobPdnS5PeerList,
       "tmnxMobPdnS5GtpcIfVRtrId": tmnxMobPdnS5GtpcIfVRtrId,
       "tmnxMobPdnS5GtpcIfIndex": tmnxMobPdnS5GtpcIfIndex,
       "tmnxMobPdnS5GtpuIfVRtrId": tmnxMobPdnS5GtpuIfVRtrId,
       "tmnxMobPdnS5GtpuIfIndex": tmnxMobPdnS5GtpuIfIndex,
       "tmnxMobPdnS5GtpcProfile": tmnxMobPdnS5GtpcProfile,
       "tmnxMobPdnS5GtpuProfile": tmnxMobPdnS5GtpuProfile,
       "tmnxMobPdnS5DualStackPref": tmnxMobPdnS5DualStackPref,
       "tmnxMobPdnS8Table": tmnxMobPdnS8Table,
       "tmnxMobPdnS8Entry": tmnxMobPdnS8Entry,
       "tmnxMobPdnS8LastChanged": tmnxMobPdnS8LastChanged,
       "tmnxMobPdnS8PeerList": tmnxMobPdnS8PeerList,
       "tmnxMobPdnS8GtpcIfVRtrId": tmnxMobPdnS8GtpcIfVRtrId,
       "tmnxMobPdnS8GtpcIfIndex": tmnxMobPdnS8GtpcIfIndex,
       "tmnxMobPdnS8GtpuIfVRtrId": tmnxMobPdnS8GtpuIfVRtrId,
       "tmnxMobPdnS8GtpuIfIndex": tmnxMobPdnS8GtpuIfIndex,
       "tmnxMobPdnS8GtpcProfile": tmnxMobPdnS8GtpcProfile,
       "tmnxMobPdnS8GtpuProfile": tmnxMobPdnS8GtpuProfile,
       "tmnxMobPdnS8DualStackPref": tmnxMobPdnS8DualStackPref,
       "tmnxMobPdnS2aTable": tmnxMobPdnS2aTable,
       "tmnxMobPdnS2aEntry": tmnxMobPdnS2aEntry,
       "tmnxMobPdnS2aLastChanged": tmnxMobPdnS2aLastChanged,
       "tmnxMobPdnS2aPeerList": tmnxMobPdnS2aPeerList,
       "tmnxMobPdnS2aIfPmipv6RtrId": tmnxMobPdnS2aIfPmipv6RtrId,
       "tmnxMobPdnS2aIfPmipv6Interface": tmnxMobPdnS2aIfPmipv6Interface,
       "tmnxMobPdnS2aIfPmipv6Profile": tmnxMobPdnS2aIfPmipv6Profile,
       "tmnxMobPdnRfTable": tmnxMobPdnRfTable,
       "tmnxMobPdnRfEntry": tmnxMobPdnRfEntry,
       "tmnxMobPdnRfLastChanged": tmnxMobPdnRfLastChanged,
       "tmnxMobPdnRfVRtrId": tmnxMobPdnRfVRtrId,
       "tmnxMobPdnRfIfIndex": tmnxMobPdnRfIfIndex,
       "tmnxMobPdnRfPriDiaPeer": tmnxMobPdnRfPriDiaPeer,
       "tmnxMobPdnRfSecDiaPeer": tmnxMobPdnRfSecDiaPeer,
       "tmnxMobPdnRfAcctIntmInterval": tmnxMobPdnRfAcctIntmInterval,
       "tmnxMobPdnRfApplTxTimer": tmnxMobPdnRfApplTxTimer,
       "tmnxMobPdnRfRetryCount": tmnxMobPdnRfRetryCount,
       "tmnxMobPdnRfChargingGroupID": tmnxMobPdnRfChargingGroupID,
       "tmnxMobPdnRfOperatorString": tmnxMobPdnRfOperatorString,
       "tmnxMobPdnRfAcctLevel": tmnxMobPdnRfAcctLevel,
       "tmnxMobPdnRfNodeId": tmnxMobPdnRfNodeId,
       "tmnxMobPdnRfOcFilePrivateInfo": tmnxMobPdnRfOcFilePrivateInfo,
       "tmnxMobPdnRfOcFileExtension": tmnxMobPdnRfOcFileExtension,
       "tmnxMobPdnRfOcFileClosureSize": tmnxMobPdnRfOcFileClosureSize,
       "tmnxMobPdnRfOcFileClsLifeTime": tmnxMobPdnRfOcFileClsLifeTime,
       "tmnxMobPdnRfOcFileClsMaxAcrs": tmnxMobPdnRfOcFileClsMaxAcrs,
       "tmnxMobPdnRfOcFileObsoleteTime": tmnxMobPdnRfOcFileObsoleteTime,
       "tmnxMobPdnRfOcPrimaryCf": tmnxMobPdnRfOcPrimaryCf,
       "tmnxMobPdnRfOcCf1State": tmnxMobPdnRfOcCf1State,
       "tmnxMobPdnRfOcCf1Limit": tmnxMobPdnRfOcCf1Limit,
       "tmnxMobPdnRfOcCf2State": tmnxMobPdnRfOcCf2State,
       "tmnxMobPdnRfOcCf2Limit": tmnxMobPdnRfOcCf2Limit,
       "tmnxMobPdnRfSuppVendorAvps": tmnxMobPdnRfSuppVendorAvps,
       "tmnxMobPdnPccBasePolTable": tmnxMobPdnPccBasePolTable,
       "tmnxMobPdnPccBasePolEntry": tmnxMobPdnPccBasePolEntry,
       "tmnxMobPdnPccIpCanType": tmnxMobPdnPccIpCanType,
       "tmnxMobPdnPccBasePolRowStatus": tmnxMobPdnPccBasePolRowStatus,
       "tmnxMobPdnApnTable": tmnxMobPdnApnTable,
       "tmnxMobPdnApnEntry": tmnxMobPdnApnEntry,
       "tmnxMobPdnApnName": tmnxMobPdnApnName,
       "tmnxMobPdnApnRowStatus": tmnxMobPdnApnRowStatus,
       "tmnxMobPdnApnLastChanged": tmnxMobPdnApnLastChanged,
       "tmnxMobPdnApnDescription": tmnxMobPdnApnDescription,
       "tmnxMobPdnApnAdminState": tmnxMobPdnApnAdminState,
       "tmnxMobPdnApnOperState": tmnxMobPdnApnOperState,
       "tmnxMobPdnApnGracefulShutTimeout": tmnxMobPdnApnGracefulShutTimeout,
       "tmnxMobPdnApnType": tmnxMobPdnApnType,
       "tmnxMobPdnApnVRtrId": tmnxMobPdnApnVRtrId,
       "tmnxMobPdnApnVirtualApnName": tmnxMobPdnApnVirtualApnName,
       "tmnxMobPdnApnPdnTypeIpv4": tmnxMobPdnApnPdnTypeIpv4,
       "tmnxMobPdnApnPdnTypeIpv6": tmnxMobPdnApnPdnTypeIpv6,
       "tmnxMobPdnApnPdnTypeIpv4v6": tmnxMobPdnApnPdnTypeIpv4v6,
       "tmnxMobPdnApnPdnAllocType": tmnxMobPdnApnPdnAllocType,
       "tmnxMobPdnApnPdnRestrictionType": tmnxMobPdnApnPdnRestrictionType,
       "tmnxMobPdnApnAllowMultiplePdns": tmnxMobPdnApnAllowMultiplePdns,
       "tmnxMobPdnApnSelectSubscribed": tmnxMobPdnApnSelectSubscribed,
       "tmnxMobPdnApnSelectMsProvided": tmnxMobPdnApnSelectMsProvided,
       "tmnxMobPdnApnSelectNwProvided": tmnxMobPdnApnSelectNwProvided,
       "tmnxMobPdnApnIpAllocLocalPool": tmnxMobPdnApnIpAllocLocalPool,
       "tmnxMobPdnApnIpAllocHssStatic": tmnxMobPdnApnIpAllocHssStatic,
       "tmnxMobPdnApnIpAllocAaa": tmnxMobPdnApnIpAllocAaa,
       "tmnxMobPdnApnIpAllocDhcpProxy": tmnxMobPdnApnIpAllocDhcpProxy,
       "tmnxMobPdnApnIpAllocDhcpRelay": tmnxMobPdnApnIpAllocDhcpRelay,
       "tmnxMobPdnApnIpAllocDhcpServer": tmnxMobPdnApnIpAllocDhcpServer,
       "tmnxMobPdnApnPcrfDynamicPcc": tmnxMobPdnApnPcrfDynamicPcc,
       "tmnxMobPdnApnPcrfPriDiameterPeer": tmnxMobPdnApnPcrfPriDiameterPeer,
       "tmnxMobPdnApnPcrfSecDiameterPeer": tmnxMobPdnApnPcrfSecDiameterPeer,
       "tmnxMobPdnApnUplinkQciPolName": tmnxMobPdnApnUplinkQciPolName,
       "tmnxMobPdnApnDownlinkQciPolName": tmnxMobPdnApnDownlinkQciPolName,
       "tmnxMobPdnApnAggrRateUplink": tmnxMobPdnApnAggrRateUplink,
       "tmnxMobPdnApnAggrRateDownlink": tmnxMobPdnApnAggrRateDownlink,
       "tmnxMobPdnApnIdleTimeout": tmnxMobPdnApnIdleTimeout,
       "tmnxMobPdnApnSessionTimeout": tmnxMobPdnApnSessionTimeout,
       "tmnxMobPdnApnRejectForeignSub": tmnxMobPdnApnRejectForeignSub,
       "tmnxMobPdnApnBlockedPlmnList": tmnxMobPdnApnBlockedPlmnList,
       "tmnxMobPdnApnUliReporting": tmnxMobPdnApnUliReporting,
       "tmnxMobPdnApnUmtsQosPolName": tmnxMobPdnApnUmtsQosPolName,
       "tmnxMobPdnApnPcrfDynPccFHSession": tmnxMobPdnApnPcrfDynPccFHSession,
       "tmnxMobPdnApnExtTable": tmnxMobPdnApnExtTable,
       "tmnxMobPdnApnExtEntry": tmnxMobPdnApnExtEntry,
       "tmnxMobPdnApnExtLastChanged": tmnxMobPdnApnExtLastChanged,
       "tmnxMobPdnApnDnsServerV4AddrType": tmnxMobPdnApnDnsServerV4AddrType,
       "tmnxMobPdnApnDnsServerV4Addr": tmnxMobPdnApnDnsServerV4Addr,
       "tmnxMobPdnApnDnsServerV6AddrType": tmnxMobPdnApnDnsServerV6AddrType,
       "tmnxMobPdnApnDnsServerV6Addr": tmnxMobPdnApnDnsServerV6Addr,
       "tmnxMobPdnApnDhcpRelayV4RouterId": tmnxMobPdnApnDhcpRelayV4RouterId,
       "tmnxMobPdnApnDhcpRlyV4GiAddrType": tmnxMobPdnApnDhcpRlyV4GiAddrType,
       "tmnxMobPdnApnDhcpRelayV4GiAddr": tmnxMobPdnApnDhcpRelayV4GiAddr,
       "tmnxMobPdnApnDhcpRelayV6RouterId": tmnxMobPdnApnDhcpRelayV6RouterId,
       "tmnxMobPdnApnDhcpRlyV6GiAddrType": tmnxMobPdnApnDhcpRlyV6GiAddrType,
       "tmnxMobPdnApnDhcpRelayV6GiAddr": tmnxMobPdnApnDhcpRelayV6GiAddr,
       "tmnxMobPdnApnDhcpProxyV4RouterId": tmnxMobPdnApnDhcpProxyV4RouterId,
       "tmnxMobPdnApnDhcpPxyV4GiAddrType": tmnxMobPdnApnDhcpPxyV4GiAddrType,
       "tmnxMobPdnApnDhcpProxyV4GiAddr": tmnxMobPdnApnDhcpProxyV4GiAddr,
       "tmnxMobPdnApnDhcpProxyV6RouterId": tmnxMobPdnApnDhcpProxyV6RouterId,
       "tmnxMobPdnApnDhcpPxyV6GiAddrType": tmnxMobPdnApnDhcpPxyV6GiAddrType,
       "tmnxMobPdnApnDhcpProxyV6GiAddr": tmnxMobPdnApnDhcpProxyV6GiAddr,
       "tmnxMobPdnApnPcoDnsV4PriAddrType": tmnxMobPdnApnPcoDnsV4PriAddrType,
       "tmnxMobPdnApnPcoDnsV4PriAddr": tmnxMobPdnApnPcoDnsV4PriAddr,
       "tmnxMobPdnApnPcoDnsV4SecAddrType": tmnxMobPdnApnPcoDnsV4SecAddrType,
       "tmnxMobPdnApnPcoDnsV4SecAddr": tmnxMobPdnApnPcoDnsV4SecAddr,
       "tmnxMobPdnApnPcoDnsV6PriAddrType": tmnxMobPdnApnPcoDnsV6PriAddrType,
       "tmnxMobPdnApnPcoDnsV6PriAddr": tmnxMobPdnApnPcoDnsV6PriAddr,
       "tmnxMobPdnApnPcoDnsV6SecAddrType": tmnxMobPdnApnPcoDnsV6SecAddrType,
       "tmnxMobPdnApnPcoDnsV6SecAddr": tmnxMobPdnApnPcoDnsV6SecAddr,
       "tmnxMobPdnApnPcoPcscfV4PriAdrTyp": tmnxMobPdnApnPcoPcscfV4PriAdrTyp,
       "tmnxMobPdnApnPcoPcscfV4PriAddr": tmnxMobPdnApnPcoPcscfV4PriAddr,
       "tmnxMobPdnApnPcoPcscfV6PriAdrTyp": tmnxMobPdnApnPcoPcscfV6PriAdrTyp,
       "tmnxMobPdnApnPcoPcscfV6PriAddr": tmnxMobPdnApnPcoPcscfV6PriAddr,
       "tmnxMobPdnApnPcoNbnsV4PriAdrType": tmnxMobPdnApnPcoNbnsV4PriAdrType,
       "tmnxMobPdnApnPcoNbnsV4PriAddr": tmnxMobPdnApnPcoNbnsV4PriAddr,
       "tmnxMobPdnApnPcoNbnsV4SecAdrType": tmnxMobPdnApnPcoNbnsV4SecAdrType,
       "tmnxMobPdnApnPcoNbnsV4SecAddr": tmnxMobPdnApnPcoNbnsV4SecAddr,
       "tmnxMobPdnApnPcoNbnsV6PriAdrType": tmnxMobPdnApnPcoNbnsV6PriAdrType,
       "tmnxMobPdnApnPcoNbnsV6PriAddr": tmnxMobPdnApnPcoNbnsV6PriAddr,
       "tmnxMobPdnApnPcoNbnsV6SecAdrType": tmnxMobPdnApnPcoNbnsV6SecAdrType,
       "tmnxMobPdnApnPcoNbnsV6SecAddr": tmnxMobPdnApnPcoNbnsV6SecAddr,
       "tmnxMobPdnApnExt2Table": tmnxMobPdnApnExt2Table,
       "tmnxMobPdnApnExt2Entry": tmnxMobPdnApnExt2Entry,
       "tmnxMobPdnApnExt2LastChanged": tmnxMobPdnApnExt2LastChanged,
       "tmnxMobPdnApnChrgProfileHome": tmnxMobPdnApnChrgProfileHome,
       "tmnxMobPdnApnChrgProfileVisiting": tmnxMobPdnApnChrgProfileVisiting,
       "tmnxMobPdnApnChrgProfileRoaming": tmnxMobPdnApnChrgProfileRoaming,
       "tmnxMobPdnApnChrgCcIgnoreAny": tmnxMobPdnApnChrgCcIgnoreAny,
       "tmnxMobPdnApnChrgCcIgnoreHome": tmnxMobPdnApnChrgCcIgnoreHome,
       "tmnxMobPdnApnChrgCcIgnoreVisit": tmnxMobPdnApnChrgCcIgnoreVisit,
       "tmnxMobPdnApnChrgCcIgnoreRoaming": tmnxMobPdnApnChrgCcIgnoreRoaming,
       "tmnxMobPdnApnCdfPriDiaPeer": tmnxMobPdnApnCdfPriDiaPeer,
       "tmnxMobPdnApnCdfSecDiaPeer": tmnxMobPdnApnCdfSecDiaPeer,
       "tmnxMobPdnApnPreAuthType": tmnxMobPdnApnPreAuthType,
       "tmnxMobPdnApnPreAuthUserName": tmnxMobPdnApnPreAuthUserName,
       "tmnxMobPdnApnAuthType": tmnxMobPdnApnAuthType,
       "tmnxMobPdnApnAuthUserName": tmnxMobPdnApnAuthUserName,
       "tmnxMobPdnApnAcctType": tmnxMobPdnApnAcctType,
       "tmnxMobPdnApnAcctUserName": tmnxMobPdnApnAcctUserName,
       "tmnxMobPdnApnAcctInterimReport": tmnxMobPdnApnAcctInterimReport,
       "tmnxMobPdnApnChrgCcReject": tmnxMobPdnApnChrgCcReject,
       "tmnxMobPdnApnAuthServerGroup": tmnxMobPdnApnAuthServerGroup,
       "tmnxMobPdnApnAuthAcctSupImsi": tmnxMobPdnApnAuthAcctSupImsi,
       "tmnxMobPdnApnAcctServerGroup": tmnxMobPdnApnAcctServerGroup,
       "tmnxMobPdnApnWaitAccounting": tmnxMobPdnApnWaitAccounting,
       "tmnxMobPdnApnOcsPriDiaPeer": tmnxMobPdnApnOcsPriDiaPeer,
       "tmnxMobPdnApnOcsSecDiaPeer": tmnxMobPdnApnOcsSecDiaPeer,
       "tmnxMobPdnApnGyDccaProfile": tmnxMobPdnApnGyDccaProfile,
       "tmnxMobPdnApnPreAuthServerGroup": tmnxMobPdnApnPreAuthServerGroup,
       "tmnxMobPdnApnChangeRepAction": tmnxMobPdnApnChangeRepAction,
       "tmnxMobPdnApnSuppFramedRoute": tmnxMobPdnApnSuppFramedRoute,
       "tmnxMobPdnApnPccQciValue": tmnxMobPdnApnPccQciValue,
       "tmnxMobPdnApnPccArpValue": tmnxMobPdnApnPccArpValue,
       "tmnxMobPdnApnAuthFixUserName": tmnxMobPdnApnAuthFixUserName,
       "tmnxMobPdnApnAuthFixPassword": tmnxMobPdnApnAuthFixPassword,
       "tmnxMobPdnApnIpPoolTable": tmnxMobPdnApnIpPoolTable,
       "tmnxMobPdnApnIpPoolEntry": tmnxMobPdnApnIpPoolEntry,
       "tmnxMobPdnApnIpPoolRowStatus": tmnxMobPdnApnIpPoolRowStatus,
       "tmnxMobPdnApnBasePolTable": tmnxMobPdnApnBasePolTable,
       "tmnxMobPdnApnBasePolEntry": tmnxMobPdnApnBasePolEntry,
       "tmnxMobPdnApnBasePolRowStatus": tmnxMobPdnApnBasePolRowStatus,
       "tmnxMobPdnGaTable": tmnxMobPdnGaTable,
       "tmnxMobPdnGaEntry": tmnxMobPdnGaEntry,
       "tmnxMobPdnGaLastChanged": tmnxMobPdnGaLastChanged,
       "tmnxMobPdnGaIfVRtrId": tmnxMobPdnGaIfVRtrId,
       "tmnxMobPdnGaIfIndex": tmnxMobPdnGaIfIndex,
       "tmnxMobPdnGaGtpcProfile": tmnxMobPdnGaGtpcProfile,
       "tmnxMobPdnGaGtpPrimeGrpName": tmnxMobPdnGaGtpPrimeGrpName,
       "tmnxMobPdnGnTable": tmnxMobPdnGnTable,
       "tmnxMobPdnGnEntry": tmnxMobPdnGnEntry,
       "tmnxMobPdnGnLastChanged": tmnxMobPdnGnLastChanged,
       "tmnxMobPdnGnGtpcIfVRtrId": tmnxMobPdnGnGtpcIfVRtrId,
       "tmnxMobPdnGnGtpcIfIndex": tmnxMobPdnGnGtpcIfIndex,
       "tmnxMobPdnGnGtpuIfVRtrId": tmnxMobPdnGnGtpuIfVRtrId,
       "tmnxMobPdnGnGtpuIfIndex": tmnxMobPdnGnGtpuIfIndex,
       "tmnxMobPdnGnGtpcProfile": tmnxMobPdnGnGtpcProfile,
       "tmnxMobPdnGnGtpuProfile": tmnxMobPdnGnGtpuProfile,
       "tmnxMobPdnGnPeerList": tmnxMobPdnGnPeerList,
       "tmnxMobPdnApTable": tmnxMobPdnApTable,
       "tmnxMobPdnApEntry": tmnxMobPdnApEntry,
       "tmnxMobPdnApPolicyId": tmnxMobPdnApPolicyId,
       "tmnxMobPdnApRowStatus": tmnxMobPdnApRowStatus,
       "tmnxMobPdnApLastChanged": tmnxMobPdnApLastChanged,
       "tmnxMobPdnApCollectAcctStats": tmnxMobPdnApCollectAcctStats,
       "tmnxMobPdnGnPeerTable": tmnxMobPdnGnPeerTable,
       "tmnxMobPdnGnPeerEntry": tmnxMobPdnGnPeerEntry,
       "tmnxMobPdnGnPeerAddressType": tmnxMobPdnGnPeerAddressType,
       "tmnxMobPdnGnPeerAddress": tmnxMobPdnGnPeerAddress,
       "tmnxMobPdnGnPeerPort": tmnxMobPdnGnPeerPort,
       "tmnxMobPdnGnPeerLastChanged": tmnxMobPdnGnPeerLastChanged,
       "tmnxMobPdnGnPeerCreateTime": tmnxMobPdnGnPeerCreateTime,
       "tmnxMobPdnGnPeerPathMgmtState": tmnxMobPdnGnPeerPathMgmtState,
       "tmnxMobPdnGnPeerGatewayId": tmnxMobPdnGnPeerGatewayId,
       "tmnxMobPdnGnPeerType": tmnxMobPdnGnPeerType,
       "tmnxMobPdnRadiusTable": tmnxMobPdnRadiusTable,
       "tmnxMobPdnRadiusEntry": tmnxMobPdnRadiusEntry,
       "tmnxMobPdnRadiusLastChanged": tmnxMobPdnRadiusLastChanged,
       "tmnxMobPdnRadiusIfVRtrId": tmnxMobPdnRadiusIfVRtrId,
       "tmnxMobPdnRadiusIfIndex": tmnxMobPdnRadiusIfIndex,
       "tmnxMobPdnRadiusDisconnect": tmnxMobPdnRadiusDisconnect,
       "tmnxMobPdnApnDaccGrpTable": tmnxMobPdnApnDaccGrpTable,
       "tmnxMobPdnApnDaccGrpEntry": tmnxMobPdnApnDaccGrpEntry,
       "tmnxMobPdnApnDaccGrpName": tmnxMobPdnApnDaccGrpName,
       "tmnxMobPdnApnDaccGrpRowStatus": tmnxMobPdnApnDaccGrpRowStatus,
       "tmnxMobPdnApnDaccGrpLastChngd": tmnxMobPdnApnDaccGrpLastChngd,
       "tmnxMobPdnGyTable": tmnxMobPdnGyTable,
       "tmnxMobPdnGyEntry": tmnxMobPdnGyEntry,
       "tmnxMobPdnGyLastChanged": tmnxMobPdnGyLastChanged,
       "tmnxMobPdnGyVRtrId": tmnxMobPdnGyVRtrId,
       "tmnxMobPdnGyIfIndex": tmnxMobPdnGyIfIndex,
       "tmnxMobPdnGyPriDiaPeer": tmnxMobPdnGyPriDiaPeer,
       "tmnxMobPdnGySecDiaPeer": tmnxMobPdnGySecDiaPeer,
       "tmnxMobPdnGyDccaProf": tmnxMobPdnGyDccaProf,
       "tmnxMobPdnGyDiaSession": tmnxMobPdnGyDiaSession,
       "tmnxMobPdnGyOcsSelIdType": tmnxMobPdnGyOcsSelIdType,
       "tmnxMobPdnGyOcsSelIdMappingStyle": tmnxMobPdnGyOcsSelIdMappingStyle,
       "tmnxMobPdnRatingGrpTable": tmnxMobPdnRatingGrpTable,
       "tmnxMobPdnRatingGrpEntry": tmnxMobPdnRatingGrpEntry,
       "tmnxMobPdnGyRatingGroupId": tmnxMobPdnGyRatingGroupId,
       "tmnxMobPdnRatingGrpRowStatus": tmnxMobPdnRatingGrpRowStatus,
       "tmnxMobPdnRatingGrpLastChanged": tmnxMobPdnRatingGrpLastChanged,
       "tmnxMobPdnRatingGrpActvtThresold": tmnxMobPdnRatingGrpActvtThresold,
       "tmnxMobPdnGpTable": tmnxMobPdnGpTable,
       "tmnxMobPdnGpEntry": tmnxMobPdnGpEntry,
       "tmnxMobPdnGpLastChanged": tmnxMobPdnGpLastChanged,
       "tmnxMobPdnGpGtpcIfVRtrId": tmnxMobPdnGpGtpcIfVRtrId,
       "tmnxMobPdnGpGtpcIfIndex": tmnxMobPdnGpGtpcIfIndex,
       "tmnxMobPdnGpGtpuIfVRtrId": tmnxMobPdnGpGtpuIfVRtrId,
       "tmnxMobPdnGpGtpuIfIndex": tmnxMobPdnGpGtpuIfIndex,
       "tmnxMobPdnGpGtpcProfile": tmnxMobPdnGpGtpcProfile,
       "tmnxMobPdnGpGtpuProfile": tmnxMobPdnGpGtpuProfile,
       "tmnxMobPdnGpPeerList": tmnxMobPdnGpPeerList,
       "tmnxMobPdnGpPeerTable": tmnxMobPdnGpPeerTable,
       "tmnxMobPdnGpPeerEntry": tmnxMobPdnGpPeerEntry,
       "tmnxMobPdnGpPeerAddressType": tmnxMobPdnGpPeerAddressType,
       "tmnxMobPdnGpPeerAddress": tmnxMobPdnGpPeerAddress,
       "tmnxMobPdnGpPeerPort": tmnxMobPdnGpPeerPort,
       "tmnxMobPdnGpPeerLastChanged": tmnxMobPdnGpPeerLastChanged,
       "tmnxMobPdnGpPeerCreateTime": tmnxMobPdnGpPeerCreateTime,
       "tmnxMobPdnGpPeerPathMgmtState": tmnxMobPdnGpPeerPathMgmtState,
       "tmnxMobPdnGpPeerGatewayId": tmnxMobPdnGpPeerGatewayId,
       "tmnxMobPdnGpPeerType": tmnxMobPdnGpPeerType,
       "tmnxMobPdnApnExt3Table": tmnxMobPdnApnExt3Table,
       "tmnxMobPdnApnExt3Entry": tmnxMobPdnApnExt3Entry,
       "tmnxMobPdnApnExt3LastChanged": tmnxMobPdnApnExt3LastChanged,
       "tmnxMobPdnApnAuthPriDiamPeer": tmnxMobPdnApnAuthPriDiamPeer,
       "tmnxMobPdnApnAuthSecDiamPeer": tmnxMobPdnApnAuthSecDiamPeer,
       "tmnxMobPdnApnDefAppProfile": tmnxMobPdnApnDefAppProfile,
       "tmnxMobPdnApnAuthSupImsi": tmnxMobPdnApnAuthSupImsi,
       "tmnxMobPdnApnAcctSupImsi": tmnxMobPdnApnAcctSupImsi,
       "tmnxMobPdnApnPreAuthSupImsi": tmnxMobPdnApnPreAuthSupImsi,
       "tmnxMobPdnApnAaGroupIndex": tmnxMobPdnApnAaGroupIndex,
       "tmnxMobPdnApnAaGrpPartIndex": tmnxMobPdnApnAaGrpPartIndex,
       "tmnxMobPdnApnHttpRedirect": tmnxMobPdnApnHttpRedirect,
       "tmnxMobPdnApnRedirTrafficPol": tmnxMobPdnApnRedirTrafficPol,
       "tmnxMobPdnApnRedirPolRouterInst": tmnxMobPdnApnRedirPolRouterInst,
       "tmnxMobPdnApnRedirPolNHopAddrTyp": tmnxMobPdnApnRedirPolNHopAddrTyp,
       "tmnxMobPdnApnRedirPolNHopAddr": tmnxMobPdnApnRedirPolNHopAddr,
       "tmnxMobPdnApnAllowEmergency": tmnxMobPdnApnAllowEmergency,
       "tmnxMobPdnGyOcsTable": tmnxMobPdnGyOcsTable,
       "tmnxMobPdnGyOcsEntry": tmnxMobPdnGyOcsEntry,
       "tmnxMobPdnGyOcsUserRangeName": tmnxMobPdnGyOcsUserRangeName,
       "tmnxMobPdnGyOcsRowStatus": tmnxMobPdnGyOcsRowStatus,
       "tmnxMobPdnGyOcsLastChanged": tmnxMobPdnGyOcsLastChanged,
       "tmnxMobPdnGyOcsUeStartId": tmnxMobPdnGyOcsUeStartId,
       "tmnxMobPdnGyOcsUeEndId": tmnxMobPdnGyOcsUeEndId,
       "tmnxMobPdnGyOcsPriDiaPeer": tmnxMobPdnGyOcsPriDiaPeer,
       "tmnxMobPdnGyOcsSecDiaPeer": tmnxMobPdnGyOcsSecDiaPeer,
       "tmnxMobPdnGyOcsDccaProf": tmnxMobPdnGyOcsDccaProf,
       "tmnxMobPdnS6bTable": tmnxMobPdnS6bTable,
       "tmnxMobPdnS6bEntry": tmnxMobPdnS6bEntry,
       "tmnxMobPdnS6bLastChanged": tmnxMobPdnS6bLastChanged,
       "tmnxMobPdnS6bTransactionTimer": tmnxMobPdnS6bTransactionTimer,
       "tmnxMobPdnS6bRetryCount": tmnxMobPdnS6bRetryCount,
       "tmnxMobPdnStatObjs": tmnxMobPdnStatObjs,
       "tmnxMobPdnUeTable": tmnxMobPdnUeTable,
       "tmnxMobPdnUeEntry": tmnxMobPdnUeEntry,
       "tmnxMobPdnUeImsi": tmnxMobPdnUeImsi,
       "tmnxMobPdnUeRowStatus": tmnxMobPdnUeRowStatus,
       "tmnxMobPdnUeMsIsdn": tmnxMobPdnUeMsIsdn,
       "tmnxMobPdnUeImei": tmnxMobPdnUeImei,
       "tmnxMobPdnUeNai": tmnxMobPdnUeNai,
       "tmnxMobPdnUeNwkMcc": tmnxMobPdnUeNwkMcc,
       "tmnxMobPdnUeNwkMnc": tmnxMobPdnUeNwkMnc,
       "tmnxMobPdnUeTrackingAreaId": tmnxMobPdnUeTrackingAreaId,
       "tmnxMobPdnUeCellId": tmnxMobPdnUeCellId,
       "tmnxMobPdnUeState": tmnxMobPdnUeState,
       "tmnxMobPdnUeRat": tmnxMobPdnUeRat,
       "tmnxMobPdnUePdnContexts": tmnxMobPdnUePdnContexts,
       "tmnxMobPdnUeBearerContexts": tmnxMobPdnUeBearerContexts,
       "tmnxMobPdnUeRfPgwAddrType": tmnxMobPdnUeRfPgwAddrType,
       "tmnxMobPdnUeRfPgwAddr": tmnxMobPdnUeRfPgwAddr,
       "tmnxMobPdnUeCtxAccessType": tmnxMobPdnUeCtxAccessType,
       "tmnxMobPdnUeSubType": tmnxMobPdnUeSubType,
       "tmnxMobPdnKeyType": tmnxMobPdnKeyType,
       "tmnxMobPdnUeImsiStr": tmnxMobPdnUeImsiStr,
       "tmnxMobPdnPdnContextTable": tmnxMobPdnPdnContextTable,
       "tmnxMobPdnPdnContextEntry": tmnxMobPdnPdnContextEntry,
       "tmnxMobPdnPcApn": tmnxMobPdnPcApn,
       "tmnxMobPdnPcPdnType": tmnxMobPdnPcPdnType,
       "tmnxMobPdnPcLinkedBearerId": tmnxMobPdnPcLinkedBearerId,
       "tmnxMobPdnPcApnRestriction": tmnxMobPdnPcApnRestriction,
       "tmnxMobPdnPcUlApnAmbr": tmnxMobPdnPcUlApnAmbr,
       "tmnxMobPdnPcDlApnAmbr": tmnxMobPdnPcDlApnAmbr,
       "tmnxMobPdnPcIpv4AddressType": tmnxMobPdnPcIpv4AddressType,
       "tmnxMobPdnPcIpv4Address": tmnxMobPdnPcIpv4Address,
       "tmnxMobPdnPcIpv6AddressType": tmnxMobPdnPcIpv6AddressType,
       "tmnxMobPdnPcIpv6Address": tmnxMobPdnPcIpv6Address,
       "tmnxMobPdnPcBearerContexts": tmnxMobPdnPcBearerContexts,
       "tmnxMobPdnPcSessionState": tmnxMobPdnPcSessionState,
       "tmnxMobPdnPcLastEvent": tmnxMobPdnPcLastEvent,
       "tmnxMobPdnPcSigProtocol": tmnxMobPdnPcSigProtocol,
       "tmnxMobPdnPcTnlRemoteCtrlTeid": tmnxMobPdnPcTnlRemoteCtrlTeid,
       "tmnxMobPdnPcTnlRemoteCtrlAddrTyp": tmnxMobPdnPcTnlRemoteCtrlAddrTyp,
       "tmnxMobPdnPcTnlRemoteCtrlAddr": tmnxMobPdnPcTnlRemoteCtrlAddr,
       "tmnxMobPdnPcTnlRemV6CtrlAddrTyp": tmnxMobPdnPcTnlRemV6CtrlAddrTyp,
       "tmnxMobPdnPcTnlRemV6CtrlAddr": tmnxMobPdnPcTnlRemV6CtrlAddr,
       "tmnxMobPdnPcTnlLocalCtrlTeid": tmnxMobPdnPcTnlLocalCtrlTeid,
       "tmnxMobPdnPcTnlLocalCtrlAddrType": tmnxMobPdnPcTnlLocalCtrlAddrType,
       "tmnxMobPdnPcTnlLocalCtrlAddr": tmnxMobPdnPcTnlLocalCtrlAddr,
       "tmnxMobPdnPcTnlLocalV6CtrlAdrTyp": tmnxMobPdnPcTnlLocalV6CtrlAdrTyp,
       "tmnxMobPdnPcTnlLocalV6CtrlAddr": tmnxMobPdnPcTnlLocalV6CtrlAddr,
       "tmnxMobPdnPcOfcBearerType": tmnxMobPdnPcOfcBearerType,
       "tmnxMobPdnPcPcrfEventTriggers": tmnxMobPdnPcPcrfEventTriggers,
       "tmnxMobPdnPcGxPcrfAddressType": tmnxMobPdnPcGxPcrfAddressType,
       "tmnxMobPdnPcGxPcrfAddress": tmnxMobPdnPcGxPcrfAddress,
       "tmnxMobPdnPcGxPgwAddressType": tmnxMobPdnPcGxPgwAddressType,
       "tmnxMobPdnPcGxPgwAddress": tmnxMobPdnPcGxPgwAddress,
       "tmnxMobPdnPcAccessType": tmnxMobPdnPcAccessType,
       "tmnxMobPdnPcSelectionMode": tmnxMobPdnPcSelectionMode,
       "tmnxMobPdnPcTnlLocalDataAddrType": tmnxMobPdnPcTnlLocalDataAddrType,
       "tmnxMobPdnPcTnlLocalDataAddr": tmnxMobPdnPcTnlLocalDataAddr,
       "tmnxMobPdnPcPGWGREkey": tmnxMobPdnPcPGWGREkey,
       "tmnxMobPdnPcMAGGREkey": tmnxMobPdnPcMAGGREkey,
       "tmnxMobPdnPcTnlRemoteDataAddrTyp": tmnxMobPdnPcTnlRemoteDataAddrTyp,
       "tmnxMobPdnPcTnlRemoteDataAddr": tmnxMobPdnPcTnlRemoteDataAddr,
       "tmnxMobPdnPcRfSrvAddrType": tmnxMobPdnPcRfSrvAddrType,
       "tmnxMobPdnPcRfSrvAddr": tmnxMobPdnPcRfSrvAddr,
       "tmnxMobPdnPcRfServerState": tmnxMobPdnPcRfServerState,
       "tmnxMobPdnPcRfChargingLevel": tmnxMobPdnPcRfChargingLevel,
       "tmnxMobPdnPcRfChargingProfile": tmnxMobPdnPcRfChargingProfile,
       "tmnxMobPdnPcRfInterimRecords": tmnxMobPdnPcRfInterimRecords,
       "tmnxMobPdnPcRfTriggeredRecords": tmnxMobPdnPcRfTriggeredRecords,
       "tmnxMobPdnPcTnlDLPackets": tmnxMobPdnPcTnlDLPackets,
       "tmnxMobPdnPcTnlDLBytes": tmnxMobPdnPcTnlDLBytes,
       "tmnxMobPdnPcSgiULPackets": tmnxMobPdnPcSgiULPackets,
       "tmnxMobPdnPcSgiULBytes": tmnxMobPdnPcSgiULBytes,
       "tmnxMobPdnPcTnlDLPacketsLow": tmnxMobPdnPcTnlDLPacketsLow,
       "tmnxMobPdnPcTnlDLPacketsHigh": tmnxMobPdnPcTnlDLPacketsHigh,
       "tmnxMobPdnPcTnlDLBytesLow": tmnxMobPdnPcTnlDLBytesLow,
       "tmnxMobPdnPcTnlDLBytesHigh": tmnxMobPdnPcTnlDLBytesHigh,
       "tmnxMobPdnPcSgiULPacketsLow": tmnxMobPdnPcSgiULPacketsLow,
       "tmnxMobPdnPcSgiULPacketsHigh": tmnxMobPdnPcSgiULPacketsHigh,
       "tmnxMobPdnPcSgiULBytesLow": tmnxMobPdnPcSgiULBytesLow,
       "tmnxMobPdnPcSgiULBytesHigh": tmnxMobPdnPcSgiULBytesHigh,
       "tmnxMobPdnPcImsiAuthStatus": tmnxMobPdnPcImsiAuthStatus,
       "tmnxMobPdnPcImeiStr": tmnxMobPdnPcImeiStr,
       "tmnxMobPdnPcImsiStr": tmnxMobPdnPcImsiStr,
       "tmnxMobPdnPcSessConfigTime": tmnxMobPdnPcSessConfigTime,
       "tmnxMobPdnPcSessRemExpTime": tmnxMobPdnPcSessRemExpTime,
       "tmnxMobPdnPcSessTimeDerivedFrom": tmnxMobPdnPcSessTimeDerivedFrom,
       "tmnxMobPdnPcIdleConfigTime": tmnxMobPdnPcIdleConfigTime,
       "tmnxMobPdnPcIdleRemExpTime": tmnxMobPdnPcIdleRemExpTime,
       "tmnxMobPdnPcIdleTimeDerivedFrom": tmnxMobPdnPcIdleTimeDerivedFrom,
       "tmnxMobPdnPcRefPointType": tmnxMobPdnPcRefPointType,
       "tmnxMobPdnBearerContextTable": tmnxMobPdnBearerContextTable,
       "tmnxMobPdnBearerContextEntry": tmnxMobPdnBearerContextEntry,
       "tmnxMobPdnBcBearerId": tmnxMobPdnBcBearerId,
       "tmnxMobPdnBcBearerType": tmnxMobPdnBcBearerType,
       "tmnxMobPdnBcUpTime": tmnxMobPdnBcUpTime,
       "tmnxMobPdnBcQci": tmnxMobPdnBcQci,
       "tmnxMobPdnBcArp": tmnxMobPdnBcArp,
       "tmnxMobPdnBcSdfs": tmnxMobPdnBcSdfs,
       "tmnxMobPdnBcFilters": tmnxMobPdnBcFilters,
       "tmnxMobPdnBcTnlRemoteTeid": tmnxMobPdnBcTnlRemoteTeid,
       "tmnxMobPdnBcTnlRemoteDataAddrTyp": tmnxMobPdnBcTnlRemoteDataAddrTyp,
       "tmnxMobPdnBcTnlRemoteDataAddr": tmnxMobPdnBcTnlRemoteDataAddr,
       "tmnxMobPdnBcTnlLocalTeid": tmnxMobPdnBcTnlLocalTeid,
       "tmnxMobPdnBcTnlLocalDataAddrType": tmnxMobPdnBcTnlLocalDataAddrType,
       "tmnxMobPdnBcTnlLocalDataAddr": tmnxMobPdnBcTnlLocalDataAddr,
       "tmnxMobPdnBcTnlDLPackets": tmnxMobPdnBcTnlDLPackets,
       "tmnxMobPdnBcTnlDLBytes": tmnxMobPdnBcTnlDLBytes,
       "tmnxMobPdnBcSgiULPackets": tmnxMobPdnBcSgiULPackets,
       "tmnxMobPdnBcSgiULBytes": tmnxMobPdnBcSgiULBytes,
       "tmnxMobPdnBcTnlDLPacketsLow": tmnxMobPdnBcTnlDLPacketsLow,
       "tmnxMobPdnBcTnlDLPacketsHigh": tmnxMobPdnBcTnlDLPacketsHigh,
       "tmnxMobPdnBcTnlDLBytesLow": tmnxMobPdnBcTnlDLBytesLow,
       "tmnxMobPdnBcTnlDLBytesHigh": tmnxMobPdnBcTnlDLBytesHigh,
       "tmnxMobPdnBcSgiULPacketsLow": tmnxMobPdnBcSgiULPacketsLow,
       "tmnxMobPdnBcSgiULPacketsHigh": tmnxMobPdnBcSgiULPacketsHigh,
       "tmnxMobPdnBcSgiULBytesLow": tmnxMobPdnBcSgiULBytesLow,
       "tmnxMobPdnBcSgiULBytesHigh": tmnxMobPdnBcSgiULBytesHigh,
       "tmnxMobPdnBcOfcServerAddrType": tmnxMobPdnBcOfcServerAddrType,
       "tmnxMobPdnBcOfcServerAddr": tmnxMobPdnBcOfcServerAddr,
       "tmnxMobPdnBcOfcServerState": tmnxMobPdnBcOfcServerState,
       "tmnxMobPdnBcOfcChargingProfile": tmnxMobPdnBcOfcChargingProfile,
       "tmnxMobPdnBcOfcTriggeredRecords": tmnxMobPdnBcOfcTriggeredRecords,
       "tmnxMobPdnBcOfcInterimRecords": tmnxMobPdnBcOfcInterimRecords,
       "tmnxMobPdnBcAccessType": tmnxMobPdnBcAccessType,
       "tmnxMobPdnBcPGWGreKey": tmnxMobPdnBcPGWGreKey,
       "tmnxMobPdnBcMAGGreKey": tmnxMobPdnBcMAGGreKey,
       "tmnxMobPdnBcRefPointType": tmnxMobPdnBcRefPointType,
       "tmnxMobPdnBcChargingChar": tmnxMobPdnBcChargingChar,
       "tmnxMobPdnBcQosBytes": tmnxMobPdnBcQosBytes,
       "tmnxMobPdnBcSdfTable": tmnxMobPdnBcSdfTable,
       "tmnxMobPdnBcSdfEntry": tmnxMobPdnBcSdfEntry,
       "tmnxMobPdnBcSdfPrecedence": tmnxMobPdnBcSdfPrecedence,
       "tmnxMobPdnBcSdfPcrfPrecedence": tmnxMobPdnBcSdfPcrfPrecedence,
       "tmnxMobPdnBcSdfRuleName": tmnxMobPdnBcSdfRuleName,
       "tmnxMobPdnBcSdfPacketFilters": tmnxMobPdnBcSdfPacketFilters,
       "tmnxMobPdnBcSdfQosUlMbr": tmnxMobPdnBcSdfQosUlMbr,
       "tmnxMobPdnBcSdfQosDlMbr": tmnxMobPdnBcSdfQosDlMbr,
       "tmnxMobPdnBcSdfQosUlGbr": tmnxMobPdnBcSdfQosUlGbr,
       "tmnxMobPdnBcSdfQosDlGbr": tmnxMobPdnBcSdfQosDlGbr,
       "tmnxMobPdnBcSdfFilterTable": tmnxMobPdnBcSdfFilterTable,
       "tmnxMobPdnBcSdfFilterEntry": tmnxMobPdnBcSdfFilterEntry,
       "tmnxMobPdnBcSdfFilterDirection": tmnxMobPdnBcSdfFilterDirection,
       "tmnxMobPdnBcSdfFilterId": tmnxMobPdnBcSdfFilterId,
       "tmnxMobPdnBcSdfFilterProtocol": tmnxMobPdnBcSdfFilterProtocol,
       "tmnxMobPdnBcSdfFilterSrcAdrType": tmnxMobPdnBcSdfFilterSrcAdrType,
       "tmnxMobPdnBcSdfFilterSrcAddr": tmnxMobPdnBcSdfFilterSrcAddr,
       "tmnxMobPdnBcSdfFilterSrcPfxLen": tmnxMobPdnBcSdfFilterSrcPfxLen,
       "tmnxMobPdnBcSdfFilterDstAdrType": tmnxMobPdnBcSdfFilterDstAdrType,
       "tmnxMobPdnBcSdfFilterDestAddr": tmnxMobPdnBcSdfFilterDestAddr,
       "tmnxMobPdnBcSdfFilterDestPfxLen": tmnxMobPdnBcSdfFilterDestPfxLen,
       "tmnxMobPdnBcSdfFilterSrcPorts": tmnxMobPdnBcSdfFilterSrcPorts,
       "tmnxMobPdnBcSdfFilterDestPorts": tmnxMobPdnBcSdfFilterDestPorts,
       "tmnxMobPdnBcSdfFirstSrcPortOper": tmnxMobPdnBcSdfFirstSrcPortOper,
       "tmnxMobPdnBcSdfFirstSrcPortVal1": tmnxMobPdnBcSdfFirstSrcPortVal1,
       "tmnxMobPdnBcSdfFirstSrcPortVal2": tmnxMobPdnBcSdfFirstSrcPortVal2,
       "tmnxMobPdnBcSdfSecndSrcPortOper": tmnxMobPdnBcSdfSecndSrcPortOper,
       "tmnxMobPdnBcSdfSecndSrcPortVal1": tmnxMobPdnBcSdfSecndSrcPortVal1,
       "tmnxMobPdnBcSdfSecndSrcPortVal2": tmnxMobPdnBcSdfSecndSrcPortVal2,
       "tmnxMobPdnBcSdfFirstDstPortOper": tmnxMobPdnBcSdfFirstDstPortOper,
       "tmnxMobPdnBcSdfFirstDstPortVal1": tmnxMobPdnBcSdfFirstDstPortVal1,
       "tmnxMobPdnBcSdfFirstDstPortVal2": tmnxMobPdnBcSdfFirstDstPortVal2,
       "tmnxMobPdnBcSdfSecndDstPortOper": tmnxMobPdnBcSdfSecndDstPortOper,
       "tmnxMobPdnBcSdfSecndDstPortVal1": tmnxMobPdnBcSdfSecndDstPortVal1,
       "tmnxMobPdnBcSdfSecndDstPortVal2": tmnxMobPdnBcSdfSecndDstPortVal2,
       "tmnxMobPdnStatTable": tmnxMobPdnStatTable,
       "tmnxMobPdnStatEntry": tmnxMobPdnStatEntry,
       "tmnxMobPdnCardSlotNum": tmnxMobPdnCardSlotNum,
       "tmnxMobPdnStatRealApn": tmnxMobPdnStatRealApn,
       "tmnxMobPdnStatVirtualApn": tmnxMobPdnStatVirtualApn,
       "tmnxMobPdnStatBearers": tmnxMobPdnStatBearers,
       "tmnxMobPdnStatDefaultBearers": tmnxMobPdnStatDefaultBearers,
       "tmnxMobPdnStatDedicatedBearers": tmnxMobPdnStatDedicatedBearers,
       "tmnxMobPdnStatIpv4Bearers": tmnxMobPdnStatIpv4Bearers,
       "tmnxMobPdnStatIpv6Bearers": tmnxMobPdnStatIpv6Bearers,
       "tmnxMobPdnStatIpv4v6Bearers": tmnxMobPdnStatIpv4v6Bearers,
       "tmnxMobPdnStatRoamers": tmnxMobPdnStatRoamers,
       "tmnxMobPdnStatIpv4Sdf": tmnxMobPdnStatIpv4Sdf,
       "tmnxMobPdnStatIpv6Sdf": tmnxMobPdnStatIpv6Sdf,
       "tmnxMobPdnStatVPRNs": tmnxMobPdnStatVPRNs,
       "tmnxMobPdnStatPdnSessions": tmnxMobPdnStatPdnSessions,
       "tmnxMobPdnStatIpv4PdnSessions": tmnxMobPdnStatIpv4PdnSessions,
       "tmnxMobPdnStatIpv6PdnSessions": tmnxMobPdnStatIpv6PdnSessions,
       "tmnxMobPdnStatIpv4v6PdnSessions": tmnxMobPdnStatIpv4v6PdnSessions,
       "tmnxMobPdnStatIpLocalPools": tmnxMobPdnStatIpLocalPools,
       "tmnxMobPdnStatGnSgsns": tmnxMobPdnStatGnSgsns,
       "tmnxMobPdnStatHomers": tmnxMobPdnStatHomers,
       "tmnxMobPdnStatVisitors": tmnxMobPdnStatVisitors,
       "tmnxMobPdnStatHSSStaticIpv4Sess": tmnxMobPdnStatHSSStaticIpv4Sess,
       "tmnxMobPdnStatHSSStaticIpv6Sess": tmnxMobPdnStatHSSStaticIpv6Sess,
       "tmnxMobPdnStatHSSSttIpv4v6Sess": tmnxMobPdnStatHSSSttIpv4v6Sess,
       "tmnxMobPdnStateHRPDPDNSess": tmnxMobPdnStateHRPDPDNSess,
       "tmnxMobPdnStatLTEPDNSess": tmnxMobPdnStatLTEPDNSess,
       "tmnxMobPdnStat2G3GPDNSess": tmnxMobPdnStat2G3GPDNSess,
       "tmnxMobPdnStatNumSuspendedPDN": tmnxMobPdnStatNumSuspendedPDN,
       "tmnxMobPdnStatEmergencyPdnSess": tmnxMobPdnStatEmergencyPdnSess,
       "tmnxMobPdnStatRfPeer": tmnxMobPdnStatRfPeer,
       "tmnxMobPdnStatRfAcctStartBuf": tmnxMobPdnStatRfAcctStartBuf,
       "tmnxMobPdnStatRfAcctIntBuf": tmnxMobPdnStatRfAcctIntBuf,
       "tmnxMobPdnStatRfAcctStopBuf": tmnxMobPdnStatRfAcctStopBuf,
       "tmnxMobPdnProcTable": tmnxMobPdnProcTable,
       "tmnxMobPdnProcEntry": tmnxMobPdnProcEntry,
       "tmnxMobPdnProcAttach": tmnxMobPdnProcAttach,
       "tmnxMobPdnProcAttachFail": tmnxMobPdnProcAttachFail,
       "tmnxMobPdnProcDetach": tmnxMobPdnProcDetach,
       "tmnxMobPdnProcDetachFail": tmnxMobPdnProcDetachFail,
       "tmnxMobPdnProcNwDedBrActv": tmnxMobPdnProcNwDedBrActv,
       "tmnxMobPdnProcNwDedBrActvFail": tmnxMobPdnProcNwDedBrActvFail,
       "tmnxMobPdnProcNwDedBrDeActv": tmnxMobPdnProcNwDedBrDeActv,
       "tmnxMobPdnProcNwDedBrDeActvFail": tmnxMobPdnProcNwDedBrDeActvFail,
       "tmnxMobPdnProcNwDedBrModify": tmnxMobPdnProcNwDedBrModify,
       "tmnxMobPdnProcNwDedBrModifyFail": tmnxMobPdnProcNwDedBrModifyFail,
       "tmnxMobPdnProcUeDedBrActv": tmnxMobPdnProcUeDedBrActv,
       "tmnxMobPdnProcUeDedBrActvFail": tmnxMobPdnProcUeDedBrActvFail,
       "tmnxMobPdnProcUeDedBrDeActv": tmnxMobPdnProcUeDedBrDeActv,
       "tmnxMobPdnProcUeDedBrDeActvFail": tmnxMobPdnProcUeDedBrDeActvFail,
       "tmnxMobPdnProcUeDedBrModify": tmnxMobPdnProcUeDedBrModify,
       "tmnxMobPdnProcUeDedBrModifyFail": tmnxMobPdnProcUeDedBrModifyFail,
       "tmnxMobPdnProcHssQosModify": tmnxMobPdnProcHssQosModify,
       "tmnxMobPdnProcHssQosModifyFail": tmnxMobPdnProcHssQosModifyFail,
       "tmnxMobPdnProcPcrfQosModify": tmnxMobPdnProcPcrfQosModify,
       "tmnxMobPdnProcPcrfQosModifyFail": tmnxMobPdnProcPcrfQosModifyFail,
       "tmnxMobPdnProcSgwReloc": tmnxMobPdnProcSgwReloc,
       "tmnxMobPdnProcSgwRelocFail": tmnxMobPdnProcSgwRelocFail,
       "tmnxMobPdnProcPgwPdnSessDel": tmnxMobPdnProcPgwPdnSessDel,
       "tmnxMobPdnProcPgwPdnSessDelFail": tmnxMobPdnProcPgwPdnSessDelFail,
       "tmnxMobPdnProcAttachPiggyBack": tmnxMobPdnProcAttachPiggyBack,
       "tmnxMobPdneHRPDAttachSuccess": tmnxMobPdneHRPDAttachSuccess,
       "tmnxMobPdneHRPDAttachFailure": tmnxMobPdneHRPDAttachFailure,
       "tmnxMobPdneHRPDDetachSuccess": tmnxMobPdneHRPDDetachSuccess,
       "tmnxMobPdneHRPDDetachFailure": tmnxMobPdneHRPDDetachFailure,
       "tmnxMobPdneHRPDToLTEHandOverSucc": tmnxMobPdneHRPDToLTEHandOverSucc,
       "tmnxMobPdneHRPDToLTEHandOverFail": tmnxMobPdneHRPDToLTEHandOverFail,
       "tmnxMobPdnLTEToeHRPDHandOverSucc": tmnxMobPdnLTEToeHRPDHandOverSucc,
       "tmnxMobPdnLTEToeHRPDHandOverFail": tmnxMobPdnLTEToeHRPDHandOverFail,
       "tmnxMobPdnInterHSGWHandOvrSucc": tmnxMobPdnInterHSGWHandOvrSucc,
       "tmnxMobPdnInterHSGWHandOvrFail": tmnxMobPdnInterHSGWHandOvrFail,
       "tmnxMobPdnProcPDNSuspendNotice": tmnxMobPdnProcPDNSuspendNotice,
       "tmnxMobPdnProcPDNResumeNotice": tmnxMobPdnProcPDNResumeNotice,
       "tmnxMobPdnProcPDNIRSRP": tmnxMobPdnProcPDNIRSRP,
       "tmnxMobPdnProcEmergncyAttachSuc": tmnxMobPdnProcEmergncyAttachSuc,
       "tmnxMobPdnProcMmeDedBrDeActiv": tmnxMobPdnProcMmeDedBrDeActiv,
       "tmnxMobPdnProcMmeDedBrDeAcFails": tmnxMobPdnProcMmeDedBrDeAcFails,
       "tmnxMobPdnProcSessDeactDueToSt": tmnxMobPdnProcSessDeactDueToSt,
       "tmnxMobPdnProcSessDeactDueToIt": tmnxMobPdnProcSessDeactDueToIt,
       "tmnxMobPdnInterRat3gToEutranSucc": tmnxMobPdnInterRat3gToEutranSucc,
       "tmnxMobPdnInterRat3gToEutranFail": tmnxMobPdnInterRat3gToEutranFail,
       "tmnxMobPdnInterRatEutranTo3gSucc": tmnxMobPdnInterRatEutranTo3gSucc,
       "tmnxMobPdnInterRatEutranTo3gFail": tmnxMobPdnInterRatEutranTo3gFail,
       "tmnxMobPdneHRPDSessDeactSessTO": tmnxMobPdneHRPDSessDeactSessTO,
       "tmnxMobPdneHRPDSessDeactIdleTO": tmnxMobPdneHRPDSessDeactIdleTO,
       "tmnxMobPdnGxPeerTable": tmnxMobPdnGxPeerTable,
       "tmnxMobPdnGxPeerEntry": tmnxMobPdnGxPeerEntry,
       "tmnxMobPdnGxPeerAddressType": tmnxMobPdnGxPeerAddressType,
       "tmnxMobPdnGxPeerAddress": tmnxMobPdnGxPeerAddress,
       "tmnxMobPdnGxPeerPort": tmnxMobPdnGxPeerPort,
       "tmnxMobPdnGxPeerLastChanged": tmnxMobPdnGxPeerLastChanged,
       "tmnxMobPdnGxPeerCreateTime": tmnxMobPdnGxPeerCreateTime,
       "tmnxMobPdnGxPeerPathMgmtState": tmnxMobPdnGxPeerPathMgmtState,
       "tmnxMobPdnGxPeerDetailState": tmnxMobPdnGxPeerDetailState,
       "tmnxMobPdnGxStatTable": tmnxMobPdnGxStatTable,
       "tmnxMobPdnGxStatEntry": tmnxMobPdnGxStatEntry,
       "tmnxMobPdnGxStatTxCer": tmnxMobPdnGxStatTxCer,
       "tmnxMobPdnGxStatRxCea": tmnxMobPdnGxStatRxCea,
       "tmnxMobPdnGxStatRxDpr": tmnxMobPdnGxStatRxDpr,
       "tmnxMobPdnGxStatTxDpa": tmnxMobPdnGxStatTxDpa,
       "tmnxMobPdnGxStatTxDwr": tmnxMobPdnGxStatTxDwr,
       "tmnxMobPdnGxStatRxDwa": tmnxMobPdnGxStatRxDwa,
       "tmnxMobPdnGxStatConnAttempts": tmnxMobPdnGxStatConnAttempts,
       "tmnxMobPdnGxStatConnFailures": tmnxMobPdnGxStatConnFailures,
       "tmnxMobPdnGxStatRxTransportDisc": tmnxMobPdnGxStatRxTransportDisc,
       "tmnxMobPdnGxStatRxMsgUnexpectVer": tmnxMobPdnGxStatRxMsgUnexpectVer,
       "tmnxMobPdnGxStatRxMsgTooBig": tmnxMobPdnGxStatRxMsgTooBig,
       "tmnxMobPdnGxStatRxMsgTooSmall": tmnxMobPdnGxStatRxMsgTooSmall,
       "tmnxMobPdnGxStatRxInvalidCea": tmnxMobPdnGxStatRxInvalidCea,
       "tmnxMobPdnGxStatRxMsgs": tmnxMobPdnGxStatRxMsgs,
       "tmnxMobPdnGxStatTxMsgs": tmnxMobPdnGxStatTxMsgs,
       "tmnxMobPdnGxStatTxRetransmitMsgs": tmnxMobPdnGxStatTxRetransmitMsgs,
       "tmnxMobPdnGxStatTxCcrInitial": tmnxMobPdnGxStatTxCcrInitial,
       "tmnxMobPdnGxStatRxCcaInitial": tmnxMobPdnGxStatRxCcaInitial,
       "tmnxMobPdnGxStatTxCcrUpdate": tmnxMobPdnGxStatTxCcrUpdate,
       "tmnxMobPdnGxStatRxCcaUpdate": tmnxMobPdnGxStatRxCcaUpdate,
       "tmnxMobPdnGxStatTxCcrTerminate": tmnxMobPdnGxStatTxCcrTerminate,
       "tmnxMobPdnGxStatRxCcaTerminate": tmnxMobPdnGxStatRxCcaTerminate,
       "tmnxMobPdnGxStatCcrInitFails": tmnxMobPdnGxStatCcrInitFails,
       "tmnxMobPdnGxStatCcrUpdateFails": tmnxMobPdnGxStatCcrUpdateFails,
       "tmnxMobPdnGxStatCcrTermFails": tmnxMobPdnGxStatCcrTermFails,
       "tmnxMobPdnGxStatRxRar": tmnxMobPdnGxStatRxRar,
       "tmnxMobPdnGxStatTxRaa": tmnxMobPdnGxStatTxRaa,
       "tmnxMobPdnGxStatTxRaaNack": tmnxMobPdnGxStatTxRaaNack,
       "tmnxMobPdnGxStatBberfs": tmnxMobPdnGxStatBberfs,
       "tmnxMobPdnGxStatRxMalformedPkts": tmnxMobPdnGxStatRxMalformedPkts,
       "tmnxMobPdnGxStatRxCcaIMalformPkt": tmnxMobPdnGxStatRxCcaIMalformPkt,
       "tmnxMobPdnGxStatRxCcaUMalformPkt": tmnxMobPdnGxStatRxCcaUMalformPkt,
       "tmnxMobPdnGxStatRxCcaTMalformPkt": tmnxMobPdnGxStatRxCcaTMalformPkt,
       "tmnxMobPdnGxStatRxRarMalformPkts": tmnxMobPdnGxStatRxRarMalformPkts,
       "tmnxMobPdnGxStatRxUnknownPkts": tmnxMobPdnGxStatRxUnknownPkts,
       "tmnxMobPdnGxStatRxCcaIUnknownPkt": tmnxMobPdnGxStatRxCcaIUnknownPkt,
       "tmnxMobPdnGxStatRxCcaUUnknownPkt": tmnxMobPdnGxStatRxCcaUUnknownPkt,
       "tmnxMobPdnGxStatRxCcaTUnknownPkt": tmnxMobPdnGxStatRxCcaTUnknownPkt,
       "tmnxMobPdnGxStatRxRarUnknownPkts": tmnxMobPdnGxStatRxRarUnknownPkts,
       "tmnxMobPdnGxStatRxMissingIePkts": tmnxMobPdnGxStatRxMissingIePkts,
       "tmnxMobPdnGxStatRxCcaIMissIePkts": tmnxMobPdnGxStatRxCcaIMissIePkts,
       "tmnxMobPdnGxStatRxCcaUMissIePkts": tmnxMobPdnGxStatRxCcaUMissIePkts,
       "tmnxMobPdnGxStatRxCcaTMissIePkts": tmnxMobPdnGxStatRxCcaTMissIePkts,
       "tmnxMobPdnGxStatRxRarMissIePkts": tmnxMobPdnGxStatRxRarMissIePkts,
       "tmnxMobPdnGxStatRxCcaIUnkSession": tmnxMobPdnGxStatRxCcaIUnkSession,
       "tmnxMobPdnGxStatRxCcaUUnkSession": tmnxMobPdnGxStatRxCcaUUnkSession,
       "tmnxMobPdnGxStatRxCcaTUnkSession": tmnxMobPdnGxStatRxCcaTUnkSession,
       "tmnxMobPdnGxStatRxRarUnkSession": tmnxMobPdnGxStatRxRarUnkSession,
       "tmnxMobPdnGxStatTxDpr": tmnxMobPdnGxStatTxDpr,
       "tmnxMobPdnGxStatRxDpa": tmnxMobPdnGxStatRxDpa,
       "tmnxMobPdnGxStatRxDwr": tmnxMobPdnGxStatRxDwr,
       "tmnxMobPdnGxStatTxDwa": tmnxMobPdnGxStatTxDwa,
       "tmnxMobPdnGxStatRxCcaInitialFail": tmnxMobPdnGxStatRxCcaInitialFail,
       "tmnxMobPdnGxStatRxCcaUpdateFail": tmnxMobPdnGxStatRxCcaUpdateFail,
       "tmnxMobPdnGxStatRxCcaTermFail": tmnxMobPdnGxStatRxCcaTermFail,
       "tmnxMobPdnGxStatReTxCcrInitial": tmnxMobPdnGxStatReTxCcrInitial,
       "tmnxMobPdnGxStatReTxCcrUpdate": tmnxMobPdnGxStatReTxCcrUpdate,
       "tmnxMobPdnGxStatReTxCcrTerm": tmnxMobPdnGxStatReTxCcrTerm,
       "tmnxMobPdnGnStatTable": tmnxMobPdnGnStatTable,
       "tmnxMobPdnGnStatEntry": tmnxMobPdnGnStatEntry,
       "tmnxMobPdnGnStatCreatePdpReq": tmnxMobPdnGnStatCreatePdpReq,
       "tmnxMobPdnGnStatCreatePdpRsp": tmnxMobPdnGnStatCreatePdpRsp,
       "tmnxMobPdnGnStatDeletePdpReq": tmnxMobPdnGnStatDeletePdpReq,
       "tmnxMobPdnGnStatDeletePdpRsp": tmnxMobPdnGnStatDeletePdpRsp,
       "tmnxMobPdnGnStatModifyPdpReq": tmnxMobPdnGnStatModifyPdpReq,
       "tmnxMobPdnGnStatModifyPdpRsp": tmnxMobPdnGnStatModifyPdpRsp,
       "tmnxMobPdnGnStatRxEchoRequests": tmnxMobPdnGnStatRxEchoRequests,
       "tmnxMobPdnGnStatTxEchoResponses": tmnxMobPdnGnStatTxEchoResponses,
       "tmnxMobPdnGnStatTxEchoRequests": tmnxMobPdnGnStatTxEchoRequests,
       "tmnxMobPdnGnStatRxEchoResponses": tmnxMobPdnGnStatRxEchoResponses,
       "tmnxMobPdnGnStatRxErrorsIndCnt": tmnxMobPdnGnStatRxErrorsIndCnt,
       "tmnxMobPdnGnStatTxErrorsIndCnt": tmnxMobPdnGnStatTxErrorsIndCnt,
       "tmnxMobPdnGnStatRxMalformedPkts": tmnxMobPdnGnStatRxMalformedPkts,
       "tmnxMobPdnGnStatRxUnknownPkts": tmnxMobPdnGnStatRxUnknownPkts,
       "tmnxMobPdnGnStatRxMissingIePkts": tmnxMobPdnGnStatRxMissingIePkts,
       "tmnxMobPdnGnStatPeerRestarts": tmnxMobPdnGnStatPeerRestarts,
       "tmnxMobPdnGnStatPeerRestrtCount": tmnxMobPdnGnStatPeerRestrtCount,
       "tmnxMobPdnGnStatPathMgmtFails": tmnxMobPdnGnStatPathMgmtFails,
       "tmnxMobPdnGaStatTable": tmnxMobPdnGaStatTable,
       "tmnxMobPdnGaStatEntry": tmnxMobPdnGaStatEntry,
       "tmnxMobPdnGaStatAddressType": tmnxMobPdnGaStatAddressType,
       "tmnxMobPdnGaStatAddress": tmnxMobPdnGaStatAddress,
       "tmnxMobPdnGaStatPort": tmnxMobPdnGaStatPort,
       "tmnxMobPdnGaStatLastChanged": tmnxMobPdnGaStatLastChanged,
       "tmnxMobPdnGaStatCreateTime": tmnxMobPdnGaStatCreateTime,
       "tmnxMobPdnGaStatRxEchoRequests": tmnxMobPdnGaStatRxEchoRequests,
       "tmnxMobPdnGaStatTxEchoResponses": tmnxMobPdnGaStatTxEchoResponses,
       "tmnxMobPdnGaStatTxEchoRequests": tmnxMobPdnGaStatTxEchoRequests,
       "tmnxMobPdnGaStatRxEchoResponses": tmnxMobPdnGaStatRxEchoResponses,
       "tmnxMobPdnGaStatRxNodeAlRequests": tmnxMobPdnGaStatRxNodeAlRequests,
       "tmnxMobPdnGaStatTxNodeAlResps": tmnxMobPdnGaStatTxNodeAlResps,
       "tmnxMobPdnGaStatTxDataRecReqs": tmnxMobPdnGaStatTxDataRecReqs,
       "tmnxMobPdnGaStatTxDataRecTferReq": tmnxMobPdnGaStatTxDataRecTferReq,
       "tmnxMobPdnGaStatRetrDataRecReqs": tmnxMobPdnGaStatRetrDataRecReqs,
       "tmnxMobPdnGaStatRxDataRecReqs": tmnxMobPdnGaStatRxDataRecReqs,
       "tmnxMobPdnGaStatUnackDataRexReqs": tmnxMobPdnGaStatUnackDataRexReqs,
       "tmnxMobPdnGaStatRxRedirectionReq": tmnxMobPdnGaStatRxRedirectionReq,
       "tmnxMobPdnGaStatTxRedrnResp": tmnxMobPdnGaStatTxRedrnResp,
       "tmnxMobPdnGaStatRxInvalidMsgs": tmnxMobPdnGaStatRxInvalidMsgs,
       "tmnxMobPdnGaStatRxVerNotSupp": tmnxMobPdnGaStatRxVerNotSupp,
       "tmnxMobPdnGaStatTxCdrTermination": tmnxMobPdnGaStatTxCdrTermination,
       "tmnxMobPdnGaStatTxCdrMaxChngCond": tmnxMobPdnGaStatTxCdrMaxChngCond,
       "tmnxMobPdnGaStatTxCdrMsTmzChng": tmnxMobPdnGaStatTxCdrMsTmzChng,
       "tmnxMobPdnGaStatTxCdrRatChng": tmnxMobPdnGaStatTxCdrRatChng,
       "tmnxMobPdnGaStatTxCdrTimeLimit": tmnxMobPdnGaStatTxCdrTimeLimit,
       "tmnxMobPdnGaStatTxCdrVolLimit": tmnxMobPdnGaStatTxCdrVolLimit,
       "tmnxMobPdnGaStatRxCdrReqAcc": tmnxMobPdnGaStatRxCdrReqAcc,
       "tmnxMobPdnGaStatRxCdrNoResAva": tmnxMobPdnGaStatRxCdrNoResAva,
       "tmnxMobPdnGaStatRxCdrReqNotFf": tmnxMobPdnGaStatRxCdrReqNotFf,
       "tmnxMobPdnGaStatRxCdrReqFfilled": tmnxMobPdnGaStatRxCdrReqFfilled,
       "tmnxMobPdnGaStatRxCdrDupReqFf": tmnxMobPdnGaStatRxCdrDupReqFf,
       "tmnxMobPdnGaStatRxCdrInvMsgFmat": tmnxMobPdnGaStatRxCdrInvMsgFmat,
       "tmnxMobPdnGaStatRxCdrVerNotSupp": tmnxMobPdnGaStatRxCdrVerNotSupp,
       "tmnxMobPdnGaStatRxCdrSrvcNotSupp": tmnxMobPdnGaStatRxCdrSrvcNotSupp,
       "tmnxMobPdnGaStatRxCdrMandIeInc": tmnxMobPdnGaStatRxCdrMandIeInc,
       "tmnxMobPdnGaStatRxCdrMandIeMiss": tmnxMobPdnGaStatRxCdrMandIeMiss,
       "tmnxMobPdnGaStatRxCdrOptIeInc": tmnxMobPdnGaStatRxCdrOptIeInc,
       "tmnxMobPdnGaStatRxCdrSystemFail": tmnxMobPdnGaStatRxCdrSystemFail,
       "tmnxMobPdnGaStatRtrEchoRequests": tmnxMobPdnGaStatRtrEchoRequests,
       "tmnxMobPdnGaStatGtpPrimeFail": tmnxMobPdnGaStatGtpPrimeFail,
       "tmnxMobPdnGaStatOperState": tmnxMobPdnGaStatOperState,
       "tmnxMobPdnGaStatUpTime": tmnxMobPdnGaStatUpTime,
       "tmnxMobPdnGaStatTxNodeAlRequests": tmnxMobPdnGaStatTxNodeAlRequests,
       "tmnxMobPdnGaStatRxNodeAlResps": tmnxMobPdnGaStatRxNodeAlResps,
       "tmnxMobPdnGaStatNodeAlReqRetried": tmnxMobPdnGaStatNodeAlReqRetried,
       "tmnxMobPdnGaStatCdrsTx": tmnxMobPdnGaStatCdrsTx,
       "tmnxMobPdnGaStatCdrsRx": tmnxMobPdnGaStatCdrsRx,
       "tmnxMobPdnGaStatTxCdrPlmnChange": tmnxMobPdnGaStatTxCdrPlmnChange,
       "tmnxMobPdnGaStatTxCdrSerNdChLmt": tmnxMobPdnGaStatTxCdrSerNdChLmt,
       "tmnxMobPdnGaStatTxVerNotSupp": tmnxMobPdnGaStatTxVerNotSupp,
       "tmnxMobPdnGaStatTxCdrMgmtInterv": tmnxMobPdnGaStatTxCdrMgmtInterv,
       "tmnxMobPdnGyPeerTable": tmnxMobPdnGyPeerTable,
       "tmnxMobPdnGyPeerEntry": tmnxMobPdnGyPeerEntry,
       "tmnxMobPdnGyPeerAddressType": tmnxMobPdnGyPeerAddressType,
       "tmnxMobPdnGyPeerAddress": tmnxMobPdnGyPeerAddress,
       "tmnxMobPdnGyPeerPort": tmnxMobPdnGyPeerPort,
       "tmnxMobPdnGyPeerLastChanged": tmnxMobPdnGyPeerLastChanged,
       "tmnxMobPdnGyPeerCreateTime": tmnxMobPdnGyPeerCreateTime,
       "tmnxMobPdnGyPeerPathMgmtState": tmnxMobPdnGyPeerPathMgmtState,
       "tmnxMobPdnGyPeerDetailState": tmnxMobPdnGyPeerDetailState,
       "tmnxMobPdnGyStatTable": tmnxMobPdnGyStatTable,
       "tmnxMobPdnGyStatEntry": tmnxMobPdnGyStatEntry,
       "tmnxMobPdnGyStatCcrGranted": tmnxMobPdnGyStatCcrGranted,
       "tmnxMobPdnGyStatCcrDenied": tmnxMobPdnGyStatCcrDenied,
       "tmnxMobPdnGyStatCcrInitialMsgTx": tmnxMobPdnGyStatCcrInitialMsgTx,
       "tmnxMobPdnGyStatCcrUpdateMsgTx": tmnxMobPdnGyStatCcrUpdateMsgTx,
       "tmnxMobPdnGyStatCcrTermMsgTx": tmnxMobPdnGyStatCcrTermMsgTx,
       "tmnxMobPdnGyStatCcaInitialMsgRx": tmnxMobPdnGyStatCcaInitialMsgRx,
       "tmnxMobPdnGyStatCcaUpdateMsgRx": tmnxMobPdnGyStatCcaUpdateMsgRx,
       "tmnxMobPdnGyStatCcaTermMsgRx": tmnxMobPdnGyStatCcaTermMsgRx,
       "tmnxMobPdnGyStatCcrInitMsgFails": tmnxMobPdnGyStatCcrInitMsgFails,
       "tmnxMobPdnGyStatCcrUpdMsgFails": tmnxMobPdnGyStatCcrUpdMsgFails,
       "tmnxMobPdnGyStatCcrTermMsgFails": tmnxMobPdnGyStatCcrTermMsgFails,
       "tmnxMobPdnGyStatAsrMsgRx": tmnxMobPdnGyStatAsrMsgRx,
       "tmnxMobPdnGyStatAsaMsgTx": tmnxMobPdnGyStatAsaMsgTx,
       "tmnxMobPdnGyStatAsaNackMsgTx": tmnxMobPdnGyStatAsaNackMsgTx,
       "tmnxMobPdnGyStatRarMsgRx": tmnxMobPdnGyStatRarMsgRx,
       "tmnxMobPdnGyStatRaaMsgTx": tmnxMobPdnGyStatRaaMsgTx,
       "tmnxMobPdnGyStatRaaNackMsgTx": tmnxMobPdnGyStatRaaNackMsgTx,
       "tmnxMobPdnGyStatMalformedPktsRx": tmnxMobPdnGyStatMalformedPktsRx,
       "tmnxMobPdnGyStatCCAInitMalfPktRx": tmnxMobPdnGyStatCCAInitMalfPktRx,
       "tmnxMobPdnGyStatCCAUpdtMalfPktRx": tmnxMobPdnGyStatCCAUpdtMalfPktRx,
       "tmnxMobPdnGyStatCCATermMalfPktRx": tmnxMobPdnGyStatCCATermMalfPktRx,
       "tmnxMobPdnGyStatRarMalfPktRx": tmnxMobPdnGyStatRarMalfPktRx,
       "tmnxMobPdnGyStatAsrMalfPktRx": tmnxMobPdnGyStatAsrMalfPktRx,
       "tmnxMobPdnGyStatUnkwnPktsRx": tmnxMobPdnGyStatUnkwnPktsRx,
       "tmnxMobPdnGyStatCcaInitUnkPktRx": tmnxMobPdnGyStatCcaInitUnkPktRx,
       "tmnxMobPdnGyStatCcaUpdUnkPktRx": tmnxMobPdnGyStatCcaUpdUnkPktRx,
       "tmnxMobPdnGyStatCcaTermUnkPktRx": tmnxMobPdnGyStatCcaTermUnkPktRx,
       "tmnxMobPdnGyStatRarUnkPktRx": tmnxMobPdnGyStatRarUnkPktRx,
       "tmnxMobPdnGyStatAsrUnkPktRx": tmnxMobPdnGyStatAsrUnkPktRx,
       "tmnxMobPdnGyStatMissingAvpPktRx": tmnxMobPdnGyStatMissingAvpPktRx,
       "tmnxMobPdnGyStatCcaIMisAvpPktRx": tmnxMobPdnGyStatCcaIMisAvpPktRx,
       "tmnxMobPdnGyStatCcaUMisAvpPktRx": tmnxMobPdnGyStatCcaUMisAvpPktRx,
       "tmnxMobPdnGyStatCcaTMisAvpPktRx": tmnxMobPdnGyStatCcaTMisAvpPktRx,
       "tmnxMobPdnGyStatRarMisAvpPktRx": tmnxMobPdnGyStatRarMisAvpPktRx,
       "tmnxMobPdnGyStatAsrMisAvpPktRx": tmnxMobPdnGyStatAsrMisAvpPktRx,
       "tmnxMobPdnGyStatCcaIUnkSessPkts": tmnxMobPdnGyStatCcaIUnkSessPkts,
       "tmnxMobPdnGyStatCcaUUnkSessPkts": tmnxMobPdnGyStatCcaUUnkSessPkts,
       "tmnxMobPdnGyStatCcaTUnkSessPkts": tmnxMobPdnGyStatCcaTUnkSessPkts,
       "tmnxMobPdnGyStatRarUnkSessPkts": tmnxMobPdnGyStatRarUnkSessPkts,
       "tmnxMobPdnGyStatAsrUnkSessPkts": tmnxMobPdnGyStatAsrUnkSessPkts,
       "tmnxMobPdnGyStatTxCer": tmnxMobPdnGyStatTxCer,
       "tmnxMobPdnGyStatRxCea": tmnxMobPdnGyStatRxCea,
       "tmnxMobPdnGyStatRxDpr": tmnxMobPdnGyStatRxDpr,
       "tmnxMobPdnGyStatTxDpa": tmnxMobPdnGyStatTxDpa,
       "tmnxMobPdnGyStatTxDwr": tmnxMobPdnGyStatTxDwr,
       "tmnxMobPdnGyStatRxDwa": tmnxMobPdnGyStatRxDwa,
       "tmnxMobPdnGyStatConnAttempts": tmnxMobPdnGyStatConnAttempts,
       "tmnxMobPdnGyStatConnFailures": tmnxMobPdnGyStatConnFailures,
       "tmnxMobPdnGyStatRxTransportDisc": tmnxMobPdnGyStatRxTransportDisc,
       "tmnxMobPdnGyStatRxMsgUnexpectVer": tmnxMobPdnGyStatRxMsgUnexpectVer,
       "tmnxMobPdnGyStatRxMsgTooBig": tmnxMobPdnGyStatRxMsgTooBig,
       "tmnxMobPdnGyStatRxMsgTooSmall": tmnxMobPdnGyStatRxMsgTooSmall,
       "tmnxMobPdnGyStatRxInvalidCea": tmnxMobPdnGyStatRxInvalidCea,
       "tmnxMobPdnGyStatRxMsgs": tmnxMobPdnGyStatRxMsgs,
       "tmnxMobPdnGyStatTxMsgs": tmnxMobPdnGyStatTxMsgs,
       "tmnxMobPdnGyStatTxRetransmitMsgs": tmnxMobPdnGyStatTxRetransmitMsgs,
       "tmnxMobPdnGyStatTxDpr": tmnxMobPdnGyStatTxDpr,
       "tmnxMobPdnGyStatRxDpa": tmnxMobPdnGyStatRxDpa,
       "tmnxMobPdnGyStatRxDwr": tmnxMobPdnGyStatRxDwr,
       "tmnxMobPdnGyStatTxDwa": tmnxMobPdnGyStatTxDwa,
       "tmnxMobPdnGaPeerTable": tmnxMobPdnGaPeerTable,
       "tmnxMobPdnGaPeerEntry": tmnxMobPdnGaPeerEntry,
       "tmnxMobPdnGaPeerLastChanged": tmnxMobPdnGaPeerLastChanged,
       "tmnxMobPdnGaPeerCreateTime": tmnxMobPdnGaPeerCreateTime,
       "tmnxMobPdnGaPeerPathMgmtState": tmnxMobPdnGaPeerPathMgmtState,
       "tmnxMobPdnGaPeerDetailState": tmnxMobPdnGaPeerDetailState,
       "tmnxMobPdnRadPeerTable": tmnxMobPdnRadPeerTable,
       "tmnxMobPdnRadPeerEntry": tmnxMobPdnRadPeerEntry,
       "tmnxMobPdnRadPeerAddressType": tmnxMobPdnRadPeerAddressType,
       "tmnxMobPdnRadPeerAddress": tmnxMobPdnRadPeerAddress,
       "tmnxMobPdnRadPeerLastChanged": tmnxMobPdnRadPeerLastChanged,
       "tmnxMobPdnRadPeerCreateTime": tmnxMobPdnRadPeerCreateTime,
       "tmnxMobPdnRadPeerPathMgmtState": tmnxMobPdnRadPeerPathMgmtState,
       "tmnxMobPdnRadPeerDetailState": tmnxMobPdnRadPeerDetailState,
       "tmnxMobPdnRadStatTable": tmnxMobPdnRadStatTable,
       "tmnxMobPdnRadStatEntry": tmnxMobPdnRadStatEntry,
       "tmnxMobPdnRadStatLastChanged": tmnxMobPdnRadStatLastChanged,
       "tmnxMobPdnRadStatAccessReqTx": tmnxMobPdnRadStatAccessReqTx,
       "tmnxMobPdnRadStatAccessAcceptRx": tmnxMobPdnRadStatAccessAcceptRx,
       "tmnxMobPdnRadStatAccessRejectRx": tmnxMobPdnRadStatAccessRejectRx,
       "tmnxMobPdnRadStatAcctReqStartTx": tmnxMobPdnRadStatAcctReqStartTx,
       "tmnxMobPdnRadStatAcctReqIntrmTx": tmnxMobPdnRadStatAcctReqIntrmTx,
       "tmnxMobPdnRadStatAcctReqStopTx": tmnxMobPdnRadStatAcctReqStopTx,
       "tmnxMobPdnRadStatAcctResponseRx": tmnxMobPdnRadStatAcctResponseRx,
       "tmnxMobPdnRadStatMandAttrMissing": tmnxMobPdnRadStatMandAttrMissing,
       "tmnxMobPdnRadStatMandAttrErrors": tmnxMobPdnRadStatMandAttrErrors,
       "tmnxMobPdnRadStatUnsupportedAttr": tmnxMobPdnRadStatUnsupportedAttr,
       "tmnxMobPdnRadStatOptionalAttrErr": tmnxMobPdnRadStatOptionalAttrErr,
       "tmnxMobPdnRadStatAuthError": tmnxMobPdnRadStatAuthError,
       "tmnxMobPdnRadStatUnexpectedCode": tmnxMobPdnRadStatUnexpectedCode,
       "tmnxMobPdnRadStatRespTimeBelow1": tmnxMobPdnRadStatRespTimeBelow1,
       "tmnxMobPdnRadStatRespTime1to4": tmnxMobPdnRadStatRespTime1to4,
       "tmnxMobPdnRadStatRespTimeAbove4": tmnxMobPdnRadStatRespTimeAbove4,
       "tmnxMobPdnRadStatRetries": tmnxMobPdnRadStatRetries,
       "tmnxMobPdnRadStatPrFinalTimeout": tmnxMobPdnRadStatPrFinalTimeout,
       "tmnxMobPdnRadStatDiscReqRx": tmnxMobPdnRadStatDiscReqRx,
       "tmnxMobPdnRadStatDiscAckTx": tmnxMobPdnRadStatDiscAckTx,
       "tmnxMobPdnRadStatDiscNakTx": tmnxMobPdnRadStatDiscNakTx,
       "tmnxMobPdnRadStatDiscMandAtrMiss": tmnxMobPdnRadStatDiscMandAtrMiss,
       "tmnxMobPdnRadStatDiscUnsupprAttr": tmnxMobPdnRadStatDiscUnsupprAttr,
       "tmnxMobPdnRadStatDiscSessNotFnd": tmnxMobPdnRadStatDiscSessNotFnd,
       "tmnxMobPdnRadStatDiscAuthError": tmnxMobPdnRadStatDiscAuthError,
       "tmnxMobPdnRadStatDiscUnexpcCode": tmnxMobPdnRadStatDiscUnexpcCode,
       "tmnxMobPdnRadStatMsgFinalTimeout": tmnxMobPdnRadStatMsgFinalTimeout,
       "tmnxMobPdnThresTable": tmnxMobPdnThresTable,
       "tmnxMobPdnThresEntry": tmnxMobPdnThresEntry,
       "tmnxMobPdnThresLastChanged": tmnxMobPdnThresLastChanged,
       "tmnxMobPdnThresBrMgmtLmtUe": tmnxMobPdnThresBrMgmtLmtUe,
       "tmnxMobPdnThresBrMgmtLmtBr": tmnxMobPdnThresBrMgmtLmtBr,
       "tmnxMobPdnThresBrMgmtLmtDefBr": tmnxMobPdnThresBrMgmtLmtDefBr,
       "tmnxMobPdnThresBrMgmtLmtDedBr": tmnxMobPdnThresBrMgmtLmtDedBr,
       "tmnxMobPdnThresBrMgmtLmtActBr": tmnxMobPdnThresBrMgmtLmtActBr,
       "tmnxMobPdnThresBrMgmtLmtUePgd": tmnxMobPdnThresBrMgmtLmtUePgd,
       "tmnxMobPdnThresBrMgmtCfsAttch": tmnxMobPdnThresBrMgmtCfsAttch,
       "tmnxMobPdnThresBrMgmtCfsDedBr": tmnxMobPdnThresBrMgmtCfsDedBr,
       "tmnxMobPdnThresBrMgmtCfsReloc": tmnxMobPdnThresBrMgmtCfsReloc,
       "tmnxMobPdnThresBrMgmtCffAttch": tmnxMobPdnThresBrMgmtCffAttch,
       "tmnxMobPdnThresBrMgmtCffDedBr": tmnxMobPdnThresBrMgmtCffDedBr,
       "tmnxMobPdnThresBrMgmtCffHdOver": tmnxMobPdnThresBrMgmtCffHdOver,
       "tmnxMobPdnThresBrMgmtCffSrUnavl": tmnxMobPdnThresBrMgmtCffSrUnavl,
       "tmnxMobPdnThresBrTrfcThrptUL": tmnxMobPdnThresBrTrfcThrptUL,
       "tmnxMobPdnThresBrTrfcThrptDL": tmnxMobPdnThresBrTrfcThrptDL,
       "tmnxMobPdnThresBrTrfcAspFail": tmnxMobPdnThresBrTrfcAspFail,
       "tmnxMobPdnThresBrTrfcBrBdvErr": tmnxMobPdnThresBrTrfcBrBdvErr,
       "tmnxMobPdnThresPthMgmtS5Fail": tmnxMobPdnThresPthMgmtS5Fail,
       "tmnxMobPdnThresPthMgmtS5Restart": tmnxMobPdnThresPthMgmtS5Restart,
       "tmnxMobPdnThresPthMgmtS5NoResp": tmnxMobPdnThresPthMgmtS5NoResp,
       "tmnxMobPdnThresPthMgmtS5Peer": tmnxMobPdnThresPthMgmtS5Peer,
       "tmnxMobPdnThresPthMgmtS8Peer": tmnxMobPdnThresPthMgmtS8Peer,
       "tmnxMobPdnThresPthMgmtGxFail": tmnxMobPdnThresPthMgmtGxFail,
       "tmnxMobPdnThresPthMgmtRfFail": tmnxMobPdnThresPthMgmtRfFail,
       "tmnxMobPdnGpStatTable": tmnxMobPdnGpStatTable,
       "tmnxMobPdnGpStatEntry": tmnxMobPdnGpStatEntry,
       "tmnxMobPdnGpStatCreatePdpReq": tmnxMobPdnGpStatCreatePdpReq,
       "tmnxMobPdnGpStatCreatePdpRsp": tmnxMobPdnGpStatCreatePdpRsp,
       "tmnxMobPdnGpStatDeletePdpReq": tmnxMobPdnGpStatDeletePdpReq,
       "tmnxMobPdnGpStatDeletePdpRsp": tmnxMobPdnGpStatDeletePdpRsp,
       "tmnxMobPdnGpStatModifyPdpReq": tmnxMobPdnGpStatModifyPdpReq,
       "tmnxMobPdnGpStatModifyPdpRsp": tmnxMobPdnGpStatModifyPdpRsp,
       "tmnxMobPdnGpStatRxEchoRequests": tmnxMobPdnGpStatRxEchoRequests,
       "tmnxMobPdnGpStatTxEchoResponses": tmnxMobPdnGpStatTxEchoResponses,
       "tmnxMobPdnGpStatTxEchoRequests": tmnxMobPdnGpStatTxEchoRequests,
       "tmnxMobPdnGpStatRxEchoResponses": tmnxMobPdnGpStatRxEchoResponses,
       "tmnxMobPdnGpStatRxErrorsIndCnt": tmnxMobPdnGpStatRxErrorsIndCnt,
       "tmnxMobPdnGpStatTxErrorsIndCnt": tmnxMobPdnGpStatTxErrorsIndCnt,
       "tmnxMobPdnGpStatRxMalformedPkts": tmnxMobPdnGpStatRxMalformedPkts,
       "tmnxMobPdnGpStatRxUnknownPkts": tmnxMobPdnGpStatRxUnknownPkts,
       "tmnxMobPdnGpStatRxMissingIePkts": tmnxMobPdnGpStatRxMissingIePkts,
       "tmnxMobPdnGpStatPeerRestarts": tmnxMobPdnGpStatPeerRestarts,
       "tmnxMobPdnGpStatPeerRestrtCount": tmnxMobPdnGpStatPeerRestrtCount,
       "tmnxMobPdnGpStatPathMgmtFails": tmnxMobPdnGpStatPathMgmtFails,
       "tmnxMobPdnS2aPeerTable": tmnxMobPdnS2aPeerTable,
       "tmnxMobPdnS2aPeerEntry": tmnxMobPdnS2aPeerEntry,
       "tmnxMobPdnS2aPeerAddressType": tmnxMobPdnS2aPeerAddressType,
       "tmnxMobPdnS2aPeerAddress": tmnxMobPdnS2aPeerAddress,
       "tmnxMobPdnS2aPeerPort": tmnxMobPdnS2aPeerPort,
       "tmnxMobPdnS2aPeerLastChanged": tmnxMobPdnS2aPeerLastChanged,
       "tmnxMobPdnS2aPeerCreateTime": tmnxMobPdnS2aPeerCreateTime,
       "tmnxMobPdnS2aPeerPathMgmtState": tmnxMobPdnS2aPeerPathMgmtState,
       "tmnxMobPdnS2aPeerGatewayId": tmnxMobPdnS2aPeerGatewayId,
       "tmnxMobPdnS2aPeerType": tmnxMobPdnS2aPeerType,
       "tmnxMobPdnS2aPeerHBCompatible": tmnxMobPdnS2aPeerHBCompatible,
       "tmnxMobPdnS2aStatTable": tmnxMobPdnS2aStatTable,
       "tmnxMobPdnS2aStatEntry": tmnxMobPdnS2aStatEntry,
       "tmnxMobPdnS2aStatPeerRestart": tmnxMobPdnS2aStatPeerRestart,
       "tmnxMobPdnS2aStatPathMgmtFail": tmnxMobPdnS2aStatPathMgmtFail,
       "tmnxMobPdnS2aStatPeerRestartCnt": tmnxMobPdnS2aStatPeerRestartCnt,
       "tmnxMobPdnS2aStatHeartBeatReqTx": tmnxMobPdnS2aStatHeartBeatReqTx,
       "tmnxMobPdnS2aStatHeartBeatReqRx": tmnxMobPdnS2aStatHeartBeatReqRx,
       "tmnxMobPdnS2aStatHeartBeatRespTx": tmnxMobPdnS2aStatHeartBeatRespTx,
       "tmnxMobPdnS2aStatHeartBeatRespRx": tmnxMobPdnS2aStatHeartBeatRespRx,
       "tmnxMobPdnS2aStatPbu": tmnxMobPdnS2aStatPbu,
       "tmnxMobPdnS2aStatBri": tmnxMobPdnS2aStatBri,
       "tmnxMobPdnS2aStatRxMalformedPkts": tmnxMobPdnS2aStatRxMalformedPkts,
       "tmnxMobPdnS2aStatRxMissingIePkts": tmnxMobPdnS2aStatRxMissingIePkts,
       "tmnxMobPdnS2aStatRxUnknownPkts": tmnxMobPdnS2aStatRxUnknownPkts,
       "tmnxMobPdnS2aStatPbaFailure": tmnxMobPdnS2aStatPbaFailure,
       "tmnxMobPdnS2aStatBraFailure": tmnxMobPdnS2aStatBraFailure,
       "tmnxMobPdnS2aStatPbaSuccess": tmnxMobPdnS2aStatPbaSuccess,
       "tmnxMobPdnS2aStatBraSuccess": tmnxMobPdnS2aStatBraSuccess,
       "tmnxMobPdnS2aStatHBCompatible": tmnxMobPdnS2aStatHBCompatible,
       "tmnxMobPdnBcAcctGaTable": tmnxMobPdnBcAcctGaTable,
       "tmnxMobPdnBcAcctGaEntry": tmnxMobPdnBcAcctGaEntry,
       "tmnxMobPdnBcAcctGaChargingId": tmnxMobPdnBcAcctGaChargingId,
       "tmnxMobPdnBcAcctGaUlSustRate": tmnxMobPdnBcAcctGaUlSustRate,
       "tmnxMobPdnBcAcctGaDlSustRate": tmnxMobPdnBcAcctGaDlSustRate,
       "tmnxMobPdnBcAcctGaAggrUlPkts": tmnxMobPdnBcAcctGaAggrUlPkts,
       "tmnxMobPdnBcAcctGaAggrUlPktsLow": tmnxMobPdnBcAcctGaAggrUlPktsLow,
       "tmnxMobPdnBcAcctGaAggrUlPktsHigh": tmnxMobPdnBcAcctGaAggrUlPktsHigh,
       "tmnxMobPdnBcAcctGaAggrDlPkts": tmnxMobPdnBcAcctGaAggrDlPkts,
       "tmnxMobPdnBcAcctGaAggrDlPktsLow": tmnxMobPdnBcAcctGaAggrDlPktsLow,
       "tmnxMobPdnBcAcctGaAggrDlPktsHigh": tmnxMobPdnBcAcctGaAggrDlPktsHigh,
       "tmnxMobPdnBcAcctGaAggrUlByts": tmnxMobPdnBcAcctGaAggrUlByts,
       "tmnxMobPdnBcAcctGaAggrUlBytsLow": tmnxMobPdnBcAcctGaAggrUlBytsLow,
       "tmnxMobPdnBcAcctGaAggrUlBytsHigh": tmnxMobPdnBcAcctGaAggrUlBytsHigh,
       "tmnxMobPdnBcAcctGaAggrDlByts": tmnxMobPdnBcAcctGaAggrDlByts,
       "tmnxMobPdnBcAcctGaAggrDlBytsLow": tmnxMobPdnBcAcctGaAggrDlBytsLow,
       "tmnxMobPdnBcAcctGaAggrDlBytsHigh": tmnxMobPdnBcAcctGaAggrDlBytsHigh,
       "tmnxMobPdnBcAcctGaNumPartCdrs": tmnxMobPdnBcAcctGaNumPartCdrs,
       "tmnxMobPdnBcAcctGaNumContainers": tmnxMobPdnBcAcctGaNumContainers,
       "tmnxMobPdnBcAcctGaNumMaxChanges": tmnxMobPdnBcAcctGaNumMaxChanges,
       "tmnxMobPdnBcAcctGaNumRgs": tmnxMobPdnBcAcctGaNumRgs,
       "tmnxMobPdnBcAcctGaNumOfRgSvcId": tmnxMobPdnBcAcctGaNumOfRgSvcId,
       "tmnxMobPdnBcGaChrgTable": tmnxMobPdnBcGaChrgTable,
       "tmnxMobPdnBcGaChrgEntry": tmnxMobPdnBcGaChrgEntry,
       "tmnxMobPdnBcGaChrgOnlnCharging": tmnxMobPdnBcGaChrgOnlnCharging,
       "tmnxMobPdnBcGaChrgOfflnCharging": tmnxMobPdnBcGaChrgOfflnCharging,
       "tmnxMobPdnBcGaChrgUlPkts": tmnxMobPdnBcGaChrgUlPkts,
       "tmnxMobPdnBcGaChrgUlPktsLow": tmnxMobPdnBcGaChrgUlPktsLow,
       "tmnxMobPdnBcGaChrgUlPktsHigh": tmnxMobPdnBcGaChrgUlPktsHigh,
       "tmnxMobPdnBcGaChrgDlPkts": tmnxMobPdnBcGaChrgDlPkts,
       "tmnxMobPdnBcGaChrgDlPktsLow": tmnxMobPdnBcGaChrgDlPktsLow,
       "tmnxMobPdnBcGaChrgDlPktsHigh": tmnxMobPdnBcGaChrgDlPktsHigh,
       "tmnxMobPdnBcGaChrgUlByts": tmnxMobPdnBcGaChrgUlByts,
       "tmnxMobPdnBcGaChrgUlBytsLow": tmnxMobPdnBcGaChrgUlBytsLow,
       "tmnxMobPdnBcGaChrgUlBytsHigh": tmnxMobPdnBcGaChrgUlBytsHigh,
       "tmnxMobPdnBcGaChrgDlByts": tmnxMobPdnBcGaChrgDlByts,
       "tmnxMobPdnBcGaChrgDlBytsLow": tmnxMobPdnBcGaChrgDlBytsLow,
       "tmnxMobPdnBcGaChrgDlBytsHigh": tmnxMobPdnBcGaChrgDlBytsHigh,
       "tmnxMobPdnBcAcctGyTable": tmnxMobPdnBcAcctGyTable,
       "tmnxMobPdnBcAcctGyEntry": tmnxMobPdnBcAcctGyEntry,
       "tmnxMobPdnBcAcctGyChargingId": tmnxMobPdnBcAcctGyChargingId,
       "tmnxMobPdnBcAcctGyUlSustRate": tmnxMobPdnBcAcctGyUlSustRate,
       "tmnxMobPdnBcAcctGyDlSustRate": tmnxMobPdnBcAcctGyDlSustRate,
       "tmnxMobPdnBcAcctGyAggrUlPkts": tmnxMobPdnBcAcctGyAggrUlPkts,
       "tmnxMobPdnBcAcctGyAggrUlPktsLow": tmnxMobPdnBcAcctGyAggrUlPktsLow,
       "tmnxMobPdnBcAcctGyAggrUlPktsHigh": tmnxMobPdnBcAcctGyAggrUlPktsHigh,
       "tmnxMobPdnBcAcctGyAggrDlPkts": tmnxMobPdnBcAcctGyAggrDlPkts,
       "tmnxMobPdnBcAcctGyAggrDlPktsLow": tmnxMobPdnBcAcctGyAggrDlPktsLow,
       "tmnxMobPdnBcAcctGyAggrDlPktsHigh": tmnxMobPdnBcAcctGyAggrDlPktsHigh,
       "tmnxMobPdnBcAcctGyAggrUlByts": tmnxMobPdnBcAcctGyAggrUlByts,
       "tmnxMobPdnBcAcctGyAggrUlBytsLow": tmnxMobPdnBcAcctGyAggrUlBytsLow,
       "tmnxMobPdnBcAcctGyAggrUlBytsHigh": tmnxMobPdnBcAcctGyAggrUlBytsHigh,
       "tmnxMobPdnBcAcctGyAggrDlByts": tmnxMobPdnBcAcctGyAggrDlByts,
       "tmnxMobPdnBcAcctGyAggrDlBytsLow": tmnxMobPdnBcAcctGyAggrDlBytsLow,
       "tmnxMobPdnBcAcctGyAggrDlBytsHigh": tmnxMobPdnBcAcctGyAggrDlBytsHigh,
       "tmnxMobPdnBcAcctGyNumRedirection": tmnxMobPdnBcAcctGyNumRedirection,
       "tmnxMobPdnBcAcctGyLastRedctTime": tmnxMobPdnBcAcctGyLastRedctTime,
       "tmnxMobPdnBcAcctGyNumCreditsRepl": tmnxMobPdnBcAcctGyNumCreditsRepl,
       "tmnxMobPdnBcAcctGyLstCrdReplTime": tmnxMobPdnBcAcctGyLstCrdReplTime,
       "tmnxMobPdnBcAcctGyNumRgs": tmnxMobPdnBcAcctGyNumRgs,
       "tmnxMobPdnBcAcctGyNumOfRgSvcId": tmnxMobPdnBcAcctGyNumOfRgSvcId,
       "tmnxMobPdnBcGyChrgTable": tmnxMobPdnBcGyChrgTable,
       "tmnxMobPdnBcGyChrgEntry": tmnxMobPdnBcGyChrgEntry,
       "tmnxMobPdnBcGyChrgTimeGranted": tmnxMobPdnBcGyChrgTimeGranted,
       "tmnxMobPdnBcGyChrgTimeUsed": tmnxMobPdnBcGyChrgTimeUsed,
       "tmnxMobPdnBcGyChrgGrntTtlOct": tmnxMobPdnBcGyChrgGrntTtlOct,
       "tmnxMobPdnBcGyChrgGrntTtlOctLow": tmnxMobPdnBcGyChrgGrntTtlOctLow,
       "tmnxMobPdnBcGyChrgGrntTtlOctHigh": tmnxMobPdnBcGyChrgGrntTtlOctHigh,
       "tmnxMobPdnBcGyChrgGrntInOct": tmnxMobPdnBcGyChrgGrntInOct,
       "tmnxMobPdnBcGyChrgGrntInOctLow": tmnxMobPdnBcGyChrgGrntInOctLow,
       "tmnxMobPdnBcGyChrgGrntInOctHigh": tmnxMobPdnBcGyChrgGrntInOctHigh,
       "tmnxMobPdnBcGyChrgGrntOutOct": tmnxMobPdnBcGyChrgGrntOutOct,
       "tmnxMobPdnBcGyChrgGrntOutOctLow": tmnxMobPdnBcGyChrgGrntOutOctLow,
       "tmnxMobPdnBcGyChrgGrntOutOctHigh": tmnxMobPdnBcGyChrgGrntOutOctHigh,
       "tmnxMobPdnBcGyChrgUsedTtlOct": tmnxMobPdnBcGyChrgUsedTtlOct,
       "tmnxMobPdnBcGyChrgUsedTtlOctLow": tmnxMobPdnBcGyChrgUsedTtlOctLow,
       "tmnxMobPdnBcGyChrgUsedTtlOctHigh": tmnxMobPdnBcGyChrgUsedTtlOctHigh,
       "tmnxMobPdnBcGyChrgUsedInOct": tmnxMobPdnBcGyChrgUsedInOct,
       "tmnxMobPdnBcGyChrgUsedInOctLow": tmnxMobPdnBcGyChrgUsedInOctLow,
       "tmnxMobPdnBcGyChrgUsedInOctHigh": tmnxMobPdnBcGyChrgUsedInOctHigh,
       "tmnxMobPdnBcGyChrgUsedOutOct": tmnxMobPdnBcGyChrgUsedOutOct,
       "tmnxMobPdnBcGyChrgUsedOutOctLow": tmnxMobPdnBcGyChrgUsedOutOctLow,
       "tmnxMobPdnBcGyChrgUsedOutOctHigh": tmnxMobPdnBcGyChrgUsedOutOctHigh,
       "tmnxMobPdnBcGyChrgRatingGrpState": tmnxMobPdnBcGyChrgRatingGrpState,
       "tmnxMobPdnBcGyChrgTimeBasedRep": tmnxMobPdnBcGyChrgTimeBasedRep,
       "tmnxMobPdnBcGyChrgVolumeBasedRep": tmnxMobPdnBcGyChrgVolumeBasedRep,
       "tmnxMobPdnBcGyChrgQctPresent": tmnxMobPdnBcGyChrgQctPresent,
       "tmnxMobPdnBcGyChrgQctGranted": tmnxMobPdnBcGyChrgQctGranted,
       "tmnxMobPdnBcGyChrgQhtPresent": tmnxMobPdnBcGyChrgQhtPresent,
       "tmnxMobPdnBcGyChrgQhtGranted": tmnxMobPdnBcGyChrgQhtGranted,
       "tmnxMobPdnBcGyChrgQhtRemaining": tmnxMobPdnBcGyChrgQhtRemaining,
       "tmnxMobPdnBcGyChrgQvtPresent": tmnxMobPdnBcGyChrgQvtPresent,
       "tmnxMobPdnBcGyChrgQvtRemaining": tmnxMobPdnBcGyChrgQvtRemaining,
       "tmnxMobPdnBcGyChrgTtcPresent": tmnxMobPdnBcGyChrgTtcPresent,
       "tmnxMobPdnBcGyChrgTarrifTimeChng": tmnxMobPdnBcGyChrgTarrifTimeChng,
       "tmnxMobPdnBcGyChrgFuiPresent": tmnxMobPdnBcGyChrgFuiPresent,
       "tmnxMobPdnBcGyChrgOnlineEnabled": tmnxMobPdnBcGyChrgOnlineEnabled,
       "tmnxMobPdnBcGyChrgTimeThreshold": tmnxMobPdnBcGyChrgTimeThreshold,
       "tmnxMobPdnBcGyChrgVolThreshold": tmnxMobPdnBcGyChrgVolThreshold,
       "tmnxMobPdnBcGyChrgTrigger": tmnxMobPdnBcGyChrgTrigger,
       "tmnxMobPdnBcGyChrgActvThreshold": tmnxMobPdnBcGyChrgActvThreshold,
       "tmnxMobPdnBcGyChrgRedServerType": tmnxMobPdnBcGyChrgRedServerType,
       "tmnxMobPdnBcGyChrgRedServer": tmnxMobPdnBcGyChrgRedServer,
       "tmnxMobPdnBcGyChrgBillingMethod": tmnxMobPdnBcGyChrgBillingMethod,
       "tmnxMobPdnBcGyChrgReportingLevel": tmnxMobPdnBcGyChrgReportingLevel,
       "tmnxMobPdnBcGyChrgResultCode": tmnxMobPdnBcGyChrgResultCode,
       "tmnxMobPdnBcAcctRfTable": tmnxMobPdnBcAcctRfTable,
       "tmnxMobPdnBcAcctRfEntry": tmnxMobPdnBcAcctRfEntry,
       "tmnxMobPdnBcAcctRfChargingId": tmnxMobPdnBcAcctRfChargingId,
       "tmnxMobPdnBcAcctRfUlSustRate": tmnxMobPdnBcAcctRfUlSustRate,
       "tmnxMobPdnBcAcctRfDlSustRate": tmnxMobPdnBcAcctRfDlSustRate,
       "tmnxMobPdnBcAcctRfAggrUlPkts": tmnxMobPdnBcAcctRfAggrUlPkts,
       "tmnxMobPdnBcAcctRfAggrUlPktsLow": tmnxMobPdnBcAcctRfAggrUlPktsLow,
       "tmnxMobPdnBcAcctRfAggrUlPktsHigh": tmnxMobPdnBcAcctRfAggrUlPktsHigh,
       "tmnxMobPdnBcAcctRfAggrDlPkts": tmnxMobPdnBcAcctRfAggrDlPkts,
       "tmnxMobPdnBcAcctRfAggrDlPktsLow": tmnxMobPdnBcAcctRfAggrDlPktsLow,
       "tmnxMobPdnBcAcctRfAggrDlPktsHigh": tmnxMobPdnBcAcctRfAggrDlPktsHigh,
       "tmnxMobPdnBcAcctRfAggrUlByts": tmnxMobPdnBcAcctRfAggrUlByts,
       "tmnxMobPdnBcAcctRfAggrUlBytsLow": tmnxMobPdnBcAcctRfAggrUlBytsLow,
       "tmnxMobPdnBcAcctRfAggrUlBytsHigh": tmnxMobPdnBcAcctRfAggrUlBytsHigh,
       "tmnxMobPdnBcAcctRfAggrDlByts": tmnxMobPdnBcAcctRfAggrDlByts,
       "tmnxMobPdnBcAcctRfAggrDlBytsLow": tmnxMobPdnBcAcctRfAggrDlBytsLow,
       "tmnxMobPdnBcAcctRfAggrDlBytsHigh": tmnxMobPdnBcAcctRfAggrDlBytsHigh,
       "tmnxMobPdnBcAcctRfNumInterimSent": tmnxMobPdnBcAcctRfNumInterimSent,
       "tmnxMobPdnBcAcctRfNumRgs": tmnxMobPdnBcAcctRfNumRgs,
       "tmnxMobPdnBcAcctRfNumOfRgSvcId": tmnxMobPdnBcAcctRfNumOfRgSvcId,
       "tmnxMobPdnPcAcctRfTable": tmnxMobPdnPcAcctRfTable,
       "tmnxMobPdnPcAcctRfEntry": tmnxMobPdnPcAcctRfEntry,
       "tmnxMobPdnPcAcctRfAggrUlPkts": tmnxMobPdnPcAcctRfAggrUlPkts,
       "tmnxMobPdnPcAcctRfAggrUlPktsLow": tmnxMobPdnPcAcctRfAggrUlPktsLow,
       "tmnxMobPdnPcAcctRfAggrUlPktsHigh": tmnxMobPdnPcAcctRfAggrUlPktsHigh,
       "tmnxMobPdnPcAcctRfAggrDlPkts": tmnxMobPdnPcAcctRfAggrDlPkts,
       "tmnxMobPdnPcAcctRfAggrDlPktsLow": tmnxMobPdnPcAcctRfAggrDlPktsLow,
       "tmnxMobPdnPcAcctRfAggrDlPktsHigh": tmnxMobPdnPcAcctRfAggrDlPktsHigh,
       "tmnxMobPdnPcAcctRfAggrUlByts": tmnxMobPdnPcAcctRfAggrUlByts,
       "tmnxMobPdnPcAcctRfAggrUlBytsLow": tmnxMobPdnPcAcctRfAggrUlBytsLow,
       "tmnxMobPdnPcAcctRfAggrUlBytsHigh": tmnxMobPdnPcAcctRfAggrUlBytsHigh,
       "tmnxMobPdnPcAcctRfAggrDlByts": tmnxMobPdnPcAcctRfAggrDlByts,
       "tmnxMobPdnPcAcctRfAggrDlBytsLow": tmnxMobPdnPcAcctRfAggrDlBytsLow,
       "tmnxMobPdnPcAcctRfAggrDlBytsHigh": tmnxMobPdnPcAcctRfAggrDlBytsHigh,
       "tmnxMobPdnPcAcctRfUlAvgRate": tmnxMobPdnPcAcctRfUlAvgRate,
       "tmnxMobPdnPcAcctRfDlAvgRate": tmnxMobPdnPcAcctRfDlAvgRate,
       "tmnxMobPdnPcAcctRfNumInterimSent": tmnxMobPdnPcAcctRfNumInterimSent,
       "tmnxMobPdnPcAcctRfNumRgs": tmnxMobPdnPcAcctRfNumRgs,
       "tmnxMobPdnPcAcctRfNumOfRgSvcId": tmnxMobPdnPcAcctRfNumOfRgSvcId,
       "tmnxMobPdnPcRfChrgTable": tmnxMobPdnPcRfChrgTable,
       "tmnxMobPdnPcRfChrgEntry": tmnxMobPdnPcRfChrgEntry,
       "tmnxMobPdnPcRfChrgOnlnCharging": tmnxMobPdnPcRfChrgOnlnCharging,
       "tmnxMobPdnPcRfChrgOfflnCharging": tmnxMobPdnPcRfChrgOfflnCharging,
       "tmnxMobPdnPcRfChrgUlPkts": tmnxMobPdnPcRfChrgUlPkts,
       "tmnxMobPdnPcRfChrgUlPktsLow": tmnxMobPdnPcRfChrgUlPktsLow,
       "tmnxMobPdnPcRfChrgUlPktsHigh": tmnxMobPdnPcRfChrgUlPktsHigh,
       "tmnxMobPdnPcRfChrgDlPkts": tmnxMobPdnPcRfChrgDlPkts,
       "tmnxMobPdnPcRfChrgDlPktsLow": tmnxMobPdnPcRfChrgDlPktsLow,
       "tmnxMobPdnPcRfChrgDlPktsHigh": tmnxMobPdnPcRfChrgDlPktsHigh,
       "tmnxMobPdnPcRfChrgUlByts": tmnxMobPdnPcRfChrgUlByts,
       "tmnxMobPdnPcRfChrgUlBytsLow": tmnxMobPdnPcRfChrgUlBytsLow,
       "tmnxMobPdnPcRfChrgUlBytsHigh": tmnxMobPdnPcRfChrgUlBytsHigh,
       "tmnxMobPdnPcRfChrgDlByts": tmnxMobPdnPcRfChrgDlByts,
       "tmnxMobPdnPcRfChrgDlBytsLow": tmnxMobPdnPcRfChrgDlBytsLow,
       "tmnxMobPdnPcRfChrgDlBytsHigh": tmnxMobPdnPcRfChrgDlBytsHigh,
       "tmnxMobPdnS6bPeerTable": tmnxMobPdnS6bPeerTable,
       "tmnxMobPdnS6bPeerEntry": tmnxMobPdnS6bPeerEntry,
       "tmnxMobPdnS6bPeerAddressType": tmnxMobPdnS6bPeerAddressType,
       "tmnxMobPdnS6bPeerAddress": tmnxMobPdnS6bPeerAddress,
       "tmnxMobPdnS6bPeerPort": tmnxMobPdnS6bPeerPort,
       "tmnxMobPdnS6bPeerLastChanged": tmnxMobPdnS6bPeerLastChanged,
       "tmnxMobPdnS6bPeerCreateTime": tmnxMobPdnS6bPeerCreateTime,
       "tmnxMobPdnS6bPeerPathMgmtState": tmnxMobPdnS6bPeerPathMgmtState,
       "tmnxMobPdnS6bPeerDetailState": tmnxMobPdnS6bPeerDetailState,
       "tmnxMobPdnS6bStatTable": tmnxMobPdnS6bStatTable,
       "tmnxMobPdnS6bStatEntry": tmnxMobPdnS6bStatEntry,
       "tmnxMobPdnS6bStatAARInitTx": tmnxMobPdnS6bStatAARInitTx,
       "tmnxMobPdnS6bStatAARExtnTx": tmnxMobPdnS6bStatAARExtnTx,
       "tmnxMobPdnS6bStatAARDetachTx": tmnxMobPdnS6bStatAARDetachTx,
       "tmnxMobPdnS6bStatAARReauthTx": tmnxMobPdnS6bStatAARReauthTx,
       "tmnxMobPdnS6bStatAAAInitAtchRx": tmnxMobPdnS6bStatAAAInitAtchRx,
       "tmnxMobPdnS6bStatAAAExtnRx": tmnxMobPdnS6bStatAAAExtnRx,
       "tmnxMobPdnS6bStatAAADetachRx": tmnxMobPdnS6bStatAAADetachRx,
       "tmnxMobPdnS6bStatAAAReauthRx": tmnxMobPdnS6bStatAAAReauthRx,
       "tmnxMobPdnS6bStatAAASuccessRx": tmnxMobPdnS6bStatAAASuccessRx,
       "tmnxMobPdnS6bStatAAARejectRx": tmnxMobPdnS6bStatAAARejectRx,
       "tmnxMobPdnS6bStatRARequestRx": tmnxMobPdnS6bStatRARequestRx,
       "tmnxMobPdnS6bStatRAAnswerTx": tmnxMobPdnS6bStatRAAnswerTx,
       "tmnxMobPdnS6bStatSTRequestTx": tmnxMobPdnS6bStatSTRequestTx,
       "tmnxMobPdnS6bStatSTAnswerRx": tmnxMobPdnS6bStatSTAnswerRx,
       "tmnxMobPdnS6bStatASRequestRx": tmnxMobPdnS6bStatASRequestRx,
       "tmnxMobPdnS6bStatASAnswerTx": tmnxMobPdnS6bStatASAnswerTx,
       "tmnxMobPdnS6bStatAAAMissAVPPktRx": tmnxMobPdnS6bStatAAAMissAVPPktRx,
       "tmnxMobPdnS6bStatRARMissAVPPktRx": tmnxMobPdnS6bStatRARMissAVPPktRx,
       "tmnxMobPdnS6bStatSTAMissAVPPktRx": tmnxMobPdnS6bStatSTAMissAVPPktRx,
       "tmnxMobPdnS6bStatASRMissAVPPktRx": tmnxMobPdnS6bStatASRMissAVPPktRx,
       "tmnxMobPdnS6bStatAAAUnknSesPktRx": tmnxMobPdnS6bStatAAAUnknSesPktRx,
       "tmnxMobPdnS6bStatAARRetries": tmnxMobPdnS6bStatAARRetries,
       "tmnxMobPdnS6bStatSTRRetries": tmnxMobPdnS6bStatSTRRetries,
       "tmnxMobPdnS6bStatMessagesTx": tmnxMobPdnS6bStatMessagesTx,
       "tmnxMobPdnS6bStatMessagesRx": tmnxMobPdnS6bStatMessagesRx,
       "tmnxMobPdnS6bStatCERMsgsTx": tmnxMobPdnS6bStatCERMsgsTx,
       "tmnxMobPdnS6bStatCEAMsgsRx": tmnxMobPdnS6bStatCEAMsgsRx,
       "tmnxMobPdnS6bStatDPRMsgsTx": tmnxMobPdnS6bStatDPRMsgsTx,
       "tmnxMobPdnS6bStatDPRMsgsRx": tmnxMobPdnS6bStatDPRMsgsRx,
       "tmnxMobPdnS6bStatDPAMsgsTx": tmnxMobPdnS6bStatDPAMsgsTx,
       "tmnxMobPdnS6bStatDPAMsgsRx": tmnxMobPdnS6bStatDPAMsgsRx,
       "tmnxMobPdnS6bStatDWRMsgsTx": tmnxMobPdnS6bStatDWRMsgsTx,
       "tmnxMobPdnS6bStatDWRMsgsRx": tmnxMobPdnS6bStatDWRMsgsRx,
       "tmnxMobPdnS6bStatDWAMsgsTx": tmnxMobPdnS6bStatDWAMsgsTx,
       "tmnxMobPdnS6bStatDWAMsgsRx": tmnxMobPdnS6bStatDWAMsgsRx,
       "tmnxMobPdnS6bStatConnAttempts": tmnxMobPdnS6bStatConnAttempts,
       "tmnxMobPdnS6bStatConnFailures": tmnxMobPdnS6bStatConnFailures,
       "tmnxMobPdnS6bStatRxMsgUnexpctVer": tmnxMobPdnS6bStatRxMsgUnexpctVer,
       "tmnxMobPdnS6bStatRxMsgTooBig": tmnxMobPdnS6bStatRxMsgTooBig,
       "tmnxMobPdnS6bStatRxMsgTooSmall": tmnxMobPdnS6bStatRxMsgTooSmall,
       "tmnxMobPdnS6bStatRxInvalidCea": tmnxMobPdnS6bStatRxInvalidCea,
       "tmnxMobPdnS6bStatTxRetrnsmitMsgs": tmnxMobPdnS6bStatTxRetrnsmitMsgs,
       "tmnxMobPdnS6bStatRxTransportDisc": tmnxMobPdnS6bStatRxTransportDisc,
       "tmnxMobPdnS6bAARFinalTOTx": tmnxMobPdnS6bAARFinalTOTx,
       "tmnxMobPdnS6bSTRUnknownSessTx": tmnxMobPdnS6bSTRUnknownSessTx,
       "tmnxMobPdnS6bSTRFinalTOTx": tmnxMobPdnS6bSTRFinalTOTx,
       "tmnxMobPdnS6bASAUnknownSessTx": tmnxMobPdnS6bASAUnknownSessTx,
       "tmnxMobPdnS6bRAAUnknownSessTx": tmnxMobPdnS6bRAAUnknownSessTx,
       "tmnxMobPdnS6bAAAMalformedPktsRx": tmnxMobPdnS6bAAAMalformedPktsRx,
       "tmnxMobPdnS6bAAABadAVPValue": tmnxMobPdnS6bAAABadAVPValue,
       "tmnxMobPdnS6bSTAMalformedPktsRx": tmnxMobPdnS6bSTAMalformedPktsRx,
       "tmnxMobPdnS6bSTABadAVPValueRx": tmnxMobPdnS6bSTABadAVPValueRx,
       "tmnxMobPdnS6bRARBadAVPValueRx": tmnxMobPdnS6bRARBadAVPValueRx,
       "tmnxMobPdnS6bRARDuplicateRx": tmnxMobPdnS6bRARDuplicateRx,
       "tmnxMobPdnS6bASRBadAVPValueRx": tmnxMobPdnS6bASRBadAVPValueRx,
       "tmnxMobPdnS6bASRDuplicateRx": tmnxMobPdnS6bASRDuplicateRx,
       "tmnxMobPdnGlobalObjs": tmnxMobPdnGlobalObjs,
       "tmnxMobPdnTableLastChanged": tmnxMobPdnTableLastChanged,
       "tmnxMobPdnSigTableLastChanged": tmnxMobPdnSigTableLastChanged,
       "tmnxMobPdnGxTableLastChanged": tmnxMobPdnGxTableLastChanged,
       "tmnxMobPdnS5TableLastChanged": tmnxMobPdnS5TableLastChanged,
       "tmnxMobPdnS8TableLastChanged": tmnxMobPdnS8TableLastChanged,
       "tmnxMobPdnS2aTableLastChanged": tmnxMobPdnS2aTableLastChanged,
       "tmnxMobPdnRfTableLastChanged": tmnxMobPdnRfTableLastChanged,
       "tmnxMobPdnPccBasePolTableLstChgd": tmnxMobPdnPccBasePolTableLstChgd,
       "tmnxMobPdnApnTableLastChanged": tmnxMobPdnApnTableLastChanged,
       "tmnxMobPdnApnExtTableLastChanged": tmnxMobPdnApnExtTableLastChanged,
       "tmnxMobPdnApnExt2TableLastChangd": tmnxMobPdnApnExt2TableLastChangd,
       "tmnxMobPdnApnIpPoolTableLastChgd": tmnxMobPdnApnIpPoolTableLastChgd,
       "tmnxMobPdnApnBasePolTableLstChgd": tmnxMobPdnApnBasePolTableLstChgd,
       "tmnxMobPdnGxPeerTableLastChngd": tmnxMobPdnGxPeerTableLastChngd,
       "tmnxMobPdnGaTableLastChanged": tmnxMobPdnGaTableLastChanged,
       "tmnxMobPdnGnTableLastChanged": tmnxMobPdnGnTableLastChanged,
       "tmnxMobPdnApTableLastChanged": tmnxMobPdnApTableLastChanged,
       "tmnxMobPdnGnPeerTableLastChanged": tmnxMobPdnGnPeerTableLastChanged,
       "tmnxMobPdnRadiusTableLastChanged": tmnxMobPdnRadiusTableLastChanged,
       "tmnxMobPdnApnDaccGrpTblLastChngd": tmnxMobPdnApnDaccGrpTblLastChngd,
       "tmnxMobPdnGyTableLastChanged": tmnxMobPdnGyTableLastChanged,
       "tmnxMobPdnRatingGrpTableLastChgd": tmnxMobPdnRatingGrpTableLastChgd,
       "tmnxMobPdnGyPeerTableLastChngd": tmnxMobPdnGyPeerTableLastChngd,
       "tmnxMobPdnGaPeerTableLastChngd": tmnxMobPdnGaPeerTableLastChngd,
       "tmnxMobPdnRadPeerTableLastChngd": tmnxMobPdnRadPeerTableLastChngd,
       "tmnxMobPdnGpTableLastChanged": tmnxMobPdnGpTableLastChanged,
       "tmnxMobPdnGpPeerTableLastChanged": tmnxMobPdnGpPeerTableLastChanged,
       "tmnxMobPdnS2aPeerTblLastChanged": tmnxMobPdnS2aPeerTblLastChanged,
       "tmnxMobPdnApnExt3TableLastChangd": tmnxMobPdnApnExt3TableLastChangd,
       "tmnxMobPdnS6bPeerTableLastChngd": tmnxMobPdnS6bPeerTableLastChngd,
       "tmnxMobPdnGyOcsTableLastChanged": tmnxMobPdnGyOcsTableLastChanged,
       "tmnxMobPdnS6bTableLastChanged": tmnxMobPdnS6bTableLastChanged}
)
