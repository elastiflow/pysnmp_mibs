# SNMP MIB module (TIMETRA-MOBILE-SERVING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MOBILE-SERVING-MIB.mib
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

(TmnxChassisIndex,
 TmnxSlotNum,
 TmnxSlotNumOrZero,
 tmnxCardSlotNum,
 tmnxChassisIndex) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxChassisIndex",
    "TmnxSlotNum",
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
 tmnxMobGtpPriServerIndex) = mibBuilder.importSymbols(
    "TIMETRA-MOBILE-PROFILE-MIB",
    "tmnxMobGtpPriGrpName",
    "tmnxMobGtpPriServerIndex")

(TItemDescription,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TmnxAdminState,
 TmnxCdrDiagnosticAction,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledOrInherit,
 TmnxMobAddrScheme,
 TmnxMobApn,
 TmnxMobArp,
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
 TmnxMobMcc,
 TmnxMobMnc,
 TmnxMobMsisdn,
 TmnxMobNai,
 TmnxMobNode,
 TmnxMobPathMgmtState,
 TmnxMobPdnSessionEvent,
 TmnxMobPdnSessionState,
 TmnxMobPdnType,
 TmnxMobPgwSigProtocol,
 TmnxMobProfName,
 TmnxMobProfNameOrEmpty,
 TmnxMobQci,
 TmnxMobRfAcctLevel,
 TmnxMobRtrAdvtInterval,
 TmnxMobRtrAdvtLifeTime,
 TmnxMobSdf,
 TmnxMobSdfFilter,
 TmnxMobSdfFilterDirection,
 TmnxMobSdfFilterNum,
 TmnxMobSdfFilterProtocol,
 TmnxMobSdfRuleName,
 TmnxMobServRefPointType,
 TmnxMobServerState,
 TmnxMobUeId,
 TmnxMobUeIdType,
 TmnxMobUeRat,
 TmnxMobUeState,
 TmnxOperState,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TmnxAdminState",
    "TmnxCdrDiagnosticAction",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledOrInherit",
    "TmnxMobAddrScheme",
    "TmnxMobApn",
    "TmnxMobArp",
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
    "TmnxMobMcc",
    "TmnxMobMnc",
    "TmnxMobMsisdn",
    "TmnxMobNai",
    "TmnxMobNode",
    "TmnxMobPathMgmtState",
    "TmnxMobPdnSessionEvent",
    "TmnxMobPdnSessionState",
    "TmnxMobPdnType",
    "TmnxMobPgwSigProtocol",
    "TmnxMobProfName",
    "TmnxMobProfNameOrEmpty",
    "TmnxMobQci",
    "TmnxMobRfAcctLevel",
    "TmnxMobRtrAdvtInterval",
    "TmnxMobRtrAdvtLifeTime",
    "TmnxMobSdf",
    "TmnxMobSdfFilter",
    "TmnxMobSdfFilterDirection",
    "TmnxMobSdfFilterNum",
    "TmnxMobSdfFilterProtocol",
    "TmnxMobSdfRuleName",
    "TmnxMobServRefPointType",
    "TmnxMobServerState",
    "TmnxMobUeId",
    "TmnxMobUeIdType",
    "TmnxMobUeRat",
    "TmnxMobUeState",
    "TmnxOperState",
    "TmnxVRtrID")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraMobServingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 66)
)
if mibBuilder.loadTexts:
    timetraMobServingMIBModule.setRevisions(
        ("1909-12-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxMobServingConformance_ObjectIdentity = ObjectIdentity
tmnxMobServingConformance = _TmnxMobServingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66)
)
_TmnxMobServingCompliances_ObjectIdentity = ObjectIdentity
tmnxMobServingCompliances = _TmnxMobServingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 1)
)
_TmnxMobServingGroups_ObjectIdentity = ObjectIdentity
tmnxMobServingGroups = _TmnxMobServingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2)
)
_TmnxMobServing_ObjectIdentity = ObjectIdentity
tmnxMobServing = _TmnxMobServing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66)
)
_TmnxMobServingConfObjs_ObjectIdentity = ObjectIdentity
tmnxMobServingConfObjs = _TmnxMobServingConfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1)
)
_TmnxMobServTable_Object = MibTable
tmnxMobServTable = _TmnxMobServTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServTable.setStatus("current")
_TmnxMobServEntry_Object = MibTableRow
tmnxMobServEntry = _TmnxMobServEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1)
)
tmnxMobServEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
)
if mibBuilder.loadTexts:
    tmnxMobServEntry.setStatus("current")
_TmnxMobServLastChanged_Type = TimeStamp
_TmnxMobServLastChanged_Object = MibTableColumn
tmnxMobServLastChanged = _TmnxMobServLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 1),
    _TmnxMobServLastChanged_Type()
)
tmnxMobServLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServLastChanged.setStatus("current")


class _TmnxMobServAdminState_Type(TmnxAdminState):
    """Custom type tmnxMobServAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxMobServAdminState_Type.__name__ = "TmnxAdminState"
_TmnxMobServAdminState_Object = MibTableColumn
tmnxMobServAdminState = _TmnxMobServAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 2),
    _TmnxMobServAdminState_Type()
)
tmnxMobServAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServAdminState.setStatus("current")
_TmnxMobServOperState_Type = TmnxOperState
_TmnxMobServOperState_Object = MibTableColumn
tmnxMobServOperState = _TmnxMobServOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 3),
    _TmnxMobServOperState_Type()
)
tmnxMobServOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServOperState.setStatus("current")


class _TmnxMobServGracefulShutTimeout_Type(Unsigned32):
    """Custom type tmnxMobServGracefulShutTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_TmnxMobServGracefulShutTimeout_Type.__name__ = "Unsigned32"
_TmnxMobServGracefulShutTimeout_Object = MibTableColumn
tmnxMobServGracefulShutTimeout = _TmnxMobServGracefulShutTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 4),
    _TmnxMobServGracefulShutTimeout_Type()
)
tmnxMobServGracefulShutTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGracefulShutTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServGracefulShutTimeout.setUnits("minutes")


class _TmnxMobServMobNode_Type(TmnxMobNode):
    """Custom type tmnxMobServMobNode based on TmnxMobNode"""
    defaultHexValue = ""


_TmnxMobServMobNode_Type.__name__ = "TmnxMobNode"
_TmnxMobServMobNode_Object = MibTableColumn
tmnxMobServMobNode = _TmnxMobServMobNode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 5),
    _TmnxMobServMobNode_Type()
)
tmnxMobServMobNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServMobNode.setStatus("current")


class _TmnxMobServPccDynamicState_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServPccDynamicState based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServPccDynamicState_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServPccDynamicState_Object = MibTableColumn
tmnxMobServPccDynamicState = _TmnxMobServPccDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 6),
    _TmnxMobServPccDynamicState_Type()
)
tmnxMobServPccDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServPccDynamicState.setStatus("current")


class _TmnxMobServBearerGtpuUdpChecksum_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServBearerGtpuUdpChecksum based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServBearerGtpuUdpChecksum_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServBearerGtpuUdpChecksum_Object = MibTableColumn
tmnxMobServBearerGtpuUdpChecksum = _TmnxMobServBearerGtpuUdpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 7),
    _TmnxMobServBearerGtpuUdpChecksum_Type()
)
tmnxMobServBearerGtpuUdpChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServBearerGtpuUdpChecksum.setStatus("current")


class _TmnxMobServBearerGtpuSeqNumber_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServBearerGtpuSeqNumber based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServBearerGtpuSeqNumber_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServBearerGtpuSeqNumber_Object = MibTableColumn
tmnxMobServBearerGtpuSeqNumber = _TmnxMobServBearerGtpuSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 8),
    _TmnxMobServBearerGtpuSeqNumber_Type()
)
tmnxMobServBearerGtpuSeqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServBearerGtpuSeqNumber.setStatus("current")


class _TmnxMobServUplinkQciPolName_Type(TmnxMobProfName):
    """Custom type tmnxMobServUplinkQciPolName based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobServUplinkQciPolName_Type.__name__ = "TmnxMobProfName"
_TmnxMobServUplinkQciPolName_Object = MibTableColumn
tmnxMobServUplinkQciPolName = _TmnxMobServUplinkQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 9),
    _TmnxMobServUplinkQciPolName_Type()
)
tmnxMobServUplinkQciPolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServUplinkQciPolName.setStatus("current")


class _TmnxMobServDownlinkQciPolName_Type(TmnxMobProfName):
    """Custom type tmnxMobServDownlinkQciPolName based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobServDownlinkQciPolName_Type.__name__ = "TmnxMobProfName"
_TmnxMobServDownlinkQciPolName_Object = MibTableColumn
tmnxMobServDownlinkQciPolName = _TmnxMobServDownlinkQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 10),
    _TmnxMobServDownlinkQciPolName_Type()
)
tmnxMobServDownlinkQciPolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServDownlinkQciPolName.setStatus("current")


class _TmnxMobServHomePlmnList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServHomePlmnList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServHomePlmnList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServHomePlmnList_Object = MibTableColumn
tmnxMobServHomePlmnList = _TmnxMobServHomePlmnList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 11),
    _TmnxMobServHomePlmnList_Type()
)
tmnxMobServHomePlmnList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServHomePlmnList.setStatus("current")


class _TmnxMobServVisitingPlmnList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServVisitingPlmnList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServVisitingPlmnList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServVisitingPlmnList_Object = MibTableColumn
tmnxMobServVisitingPlmnList = _TmnxMobServVisitingPlmnList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 12),
    _TmnxMobServVisitingPlmnList_Type()
)
tmnxMobServVisitingPlmnList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServVisitingPlmnList.setStatus("current")


class _TmnxMobServPolBaseName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServPolBaseName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServPolBaseName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServPolBaseName_Object = MibTableColumn
tmnxMobServPolBaseName = _TmnxMobServPolBaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 13),
    _TmnxMobServPolBaseName_Type()
)
tmnxMobServPolBaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServPolBaseName.setStatus("current")


class _TmnxMobServChargingProfHome_Type(TmnxMobChargingProfile):
    """Custom type tmnxMobServChargingProfHome based on TmnxMobChargingProfile"""
    defaultValue = 0


_TmnxMobServChargingProfHome_Type.__name__ = "TmnxMobChargingProfile"
_TmnxMobServChargingProfHome_Object = MibTableColumn
tmnxMobServChargingProfHome = _TmnxMobServChargingProfHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 14),
    _TmnxMobServChargingProfHome_Type()
)
tmnxMobServChargingProfHome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChargingProfHome.setStatus("current")


class _TmnxMobServChargingProfVisiting_Type(TmnxMobChargingProfile):
    """Custom type tmnxMobServChargingProfVisiting based on TmnxMobChargingProfile"""
    defaultValue = 0


_TmnxMobServChargingProfVisiting_Type.__name__ = "TmnxMobChargingProfile"
_TmnxMobServChargingProfVisiting_Object = MibTableColumn
tmnxMobServChargingProfVisiting = _TmnxMobServChargingProfVisiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 15),
    _TmnxMobServChargingProfVisiting_Type()
)
tmnxMobServChargingProfVisiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChargingProfVisiting.setStatus("current")


class _TmnxMobServChargingProfRoaming_Type(TmnxMobChargingProfile):
    """Custom type tmnxMobServChargingProfRoaming based on TmnxMobChargingProfile"""
    defaultValue = 0


_TmnxMobServChargingProfRoaming_Type.__name__ = "TmnxMobChargingProfile"
_TmnxMobServChargingProfRoaming_Object = MibTableColumn
tmnxMobServChargingProfRoaming = _TmnxMobServChargingProfRoaming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 16),
    _TmnxMobServChargingProfRoaming_Type()
)
tmnxMobServChargingProfRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChargingProfRoaming.setStatus("current")


class _TmnxMobServChrgCcIgnoreAny_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServChrgCcIgnoreAny based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServChrgCcIgnoreAny_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServChrgCcIgnoreAny_Object = MibTableColumn
tmnxMobServChrgCcIgnoreAny = _TmnxMobServChrgCcIgnoreAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 17),
    _TmnxMobServChrgCcIgnoreAny_Type()
)
tmnxMobServChrgCcIgnoreAny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChrgCcIgnoreAny.setStatus("current")


class _TmnxMobServChrgCcIgnoreHome_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServChrgCcIgnoreHome based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServChrgCcIgnoreHome_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServChrgCcIgnoreHome_Object = MibTableColumn
tmnxMobServChrgCcIgnoreHome = _TmnxMobServChrgCcIgnoreHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 18),
    _TmnxMobServChrgCcIgnoreHome_Type()
)
tmnxMobServChrgCcIgnoreHome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChrgCcIgnoreHome.setStatus("current")


class _TmnxMobServChrgCcIgnoreVisiting_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServChrgCcIgnoreVisiting based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServChrgCcIgnoreVisiting_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServChrgCcIgnoreVisiting_Object = MibTableColumn
tmnxMobServChrgCcIgnoreVisiting = _TmnxMobServChrgCcIgnoreVisiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 19),
    _TmnxMobServChrgCcIgnoreVisiting_Type()
)
tmnxMobServChrgCcIgnoreVisiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChrgCcIgnoreVisiting.setStatus("current")


class _TmnxMobServChrgCcIgnoreRoaming_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServChrgCcIgnoreRoaming based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServChrgCcIgnoreRoaming_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServChrgCcIgnoreRoaming_Object = MibTableColumn
tmnxMobServChrgCcIgnoreRoaming = _TmnxMobServChrgCcIgnoreRoaming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 20),
    _TmnxMobServChrgCcIgnoreRoaming_Type()
)
tmnxMobServChrgCcIgnoreRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChrgCcIgnoreRoaming.setStatus("current")


class _TmnxMobServChrgCcReject_Type(TruthValue):
    """Custom type tmnxMobServChrgCcReject based on TruthValue"""
    defaultValue = 2


_TmnxMobServChrgCcReject_Type.__name__ = "TruthValue"
_TmnxMobServChrgCcReject_Object = MibTableColumn
tmnxMobServChrgCcReject = _TmnxMobServChrgCcReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 21),
    _TmnxMobServChrgCcReject_Type()
)
tmnxMobServChrgCcReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServChrgCcReject.setStatus("current")


class _TmnxMobServChrgNodeId_Type(DisplayString):
    """Custom type tmnxMobServChrgNodeId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMobServChrgNodeId_Type.__name__ = "DisplayString"
_TmnxMobServChrgNodeId_Object = MibTableColumn
tmnxMobServChrgNodeId = _TmnxMobServChrgNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 22),
    _TmnxMobServChrgNodeId_Type()
)
tmnxMobServChrgNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChrgNodeId.setStatus("current")


class _TmnxMobServChargingAvpDiag_Type(TmnxCdrDiagnosticAction):
    """Custom type tmnxMobServChargingAvpDiag based on TmnxCdrDiagnosticAction"""
    defaultValue = 1


_TmnxMobServChargingAvpDiag_Type.__name__ = "TmnxCdrDiagnosticAction"
_TmnxMobServChargingAvpDiag_Object = MibTableColumn
tmnxMobServChargingAvpDiag = _TmnxMobServChargingAvpDiag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 1, 1, 23),
    _TmnxMobServChargingAvpDiag_Type()
)
tmnxMobServChargingAvpDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServChargingAvpDiag.setStatus("current")
_TmnxMobServSigTable_Object = MibTable
tmnxMobServSigTable = _TmnxMobServSigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxMobServSigTable.setStatus("current")
_TmnxMobServSigEntry_Object = MibTableRow
tmnxMobServSigEntry = _TmnxMobServSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServSigEntry.setStatus("current")
_TmnxMobServSigLastChanged_Type = TimeStamp
_TmnxMobServSigLastChanged_Object = MibTableColumn
tmnxMobServSigLastChanged = _TmnxMobServSigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 1),
    _TmnxMobServSigLastChanged_Type()
)
tmnxMobServSigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServSigLastChanged.setStatus("current")


class _TmnxMobServSigGtpcProfile_Type(TmnxMobProfName):
    """Custom type tmnxMobServSigGtpcProfile based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobServSigGtpcProfile_Type.__name__ = "TmnxMobProfName"
_TmnxMobServSigGtpcProfile_Object = MibTableColumn
tmnxMobServSigGtpcProfile = _TmnxMobServSigGtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 2),
    _TmnxMobServSigGtpcProfile_Type()
)
tmnxMobServSigGtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigGtpcProfile.setStatus("current")


class _TmnxMobServSigGtpuProfile_Type(TmnxMobProfName):
    """Custom type tmnxMobServSigGtpuProfile based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobServSigGtpuProfile_Type.__name__ = "TmnxMobProfName"
_TmnxMobServSigGtpuProfile_Object = MibTableColumn
tmnxMobServSigGtpuProfile = _TmnxMobServSigGtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 3),
    _TmnxMobServSigGtpuProfile_Type()
)
tmnxMobServSigGtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigGtpuProfile.setStatus("current")


class _TmnxMobServSigPmipv6Profile_Type(TmnxMobProfName):
    """Custom type tmnxMobServSigPmipv6Profile based on TmnxMobProfName"""
    defaultValue = OctetString("default")


_TmnxMobServSigPmipv6Profile_Type.__name__ = "TmnxMobProfName"
_TmnxMobServSigPmipv6Profile_Object = MibTableColumn
tmnxMobServSigPmipv6Profile = _TmnxMobServSigPmipv6Profile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 4),
    _TmnxMobServSigPmipv6Profile_Type()
)
tmnxMobServSigPmipv6Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigPmipv6Profile.setStatus("current")


class _TmnxMobServSigPmipv6RtrAdIntvl_Type(TmnxMobRtrAdvtInterval):
    """Custom type tmnxMobServSigPmipv6RtrAdIntvl based on TmnxMobRtrAdvtInterval"""
    defaultValue = 30


_TmnxMobServSigPmipv6RtrAdIntvl_Type.__name__ = "TmnxMobRtrAdvtInterval"
_TmnxMobServSigPmipv6RtrAdIntvl_Object = MibTableColumn
tmnxMobServSigPmipv6RtrAdIntvl = _TmnxMobServSigPmipv6RtrAdIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 5),
    _TmnxMobServSigPmipv6RtrAdIntvl_Type()
)
tmnxMobServSigPmipv6RtrAdIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigPmipv6RtrAdIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServSigPmipv6RtrAdIntvl.setUnits("minutes")


class _TmnxMobServSigPmipv6RtrAdLife_Type(TmnxMobRtrAdvtLifeTime):
    """Custom type tmnxMobServSigPmipv6RtrAdLife based on TmnxMobRtrAdvtLifeTime"""
    defaultValue = 12


_TmnxMobServSigPmipv6RtrAdLife_Type.__name__ = "TmnxMobRtrAdvtLifeTime"
_TmnxMobServSigPmipv6RtrAdLife_Object = MibTableColumn
tmnxMobServSigPmipv6RtrAdLife = _TmnxMobServSigPmipv6RtrAdLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 6),
    _TmnxMobServSigPmipv6RtrAdLife_Type()
)
tmnxMobServSigPmipv6RtrAdLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigPmipv6RtrAdLife.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServSigPmipv6RtrAdLife.setUnits("hours")


class _TmnxMobServSigPmipv6AddrScheme_Type(TmnxMobAddrScheme):
    """Custom type tmnxMobServSigPmipv6AddrScheme based on TmnxMobAddrScheme"""
    defaultValue = 2


_TmnxMobServSigPmipv6AddrScheme_Type.__name__ = "TmnxMobAddrScheme"
_TmnxMobServSigPmipv6AddrScheme_Object = MibTableColumn
tmnxMobServSigPmipv6AddrScheme = _TmnxMobServSigPmipv6AddrScheme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 7),
    _TmnxMobServSigPmipv6AddrScheme_Type()
)
tmnxMobServSigPmipv6AddrScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigPmipv6AddrScheme.setStatus("current")


class _TmnxMobServSigDiaProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServSigDiaProfile based on TmnxMobProfNameOrEmpty"""
    defaultValue = OctetString("default")


_TmnxMobServSigDiaProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServSigDiaProfile_Object = MibTableColumn
tmnxMobServSigDiaProfile = _TmnxMobServSigDiaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 8),
    _TmnxMobServSigDiaProfile_Type()
)
tmnxMobServSigDiaProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigDiaProfile.setStatus("current")


class _TmnxMobServSigDiaOriginRealm_Type(TmnxMobDiaPeerHost):
    """Custom type tmnxMobServSigDiaOriginRealm based on TmnxMobDiaPeerHost"""
    defaultHexValue = ""


_TmnxMobServSigDiaOriginRealm_Type.__name__ = "TmnxMobDiaPeerHost"
_TmnxMobServSigDiaOriginRealm_Object = MibTableColumn
tmnxMobServSigDiaOriginRealm = _TmnxMobServSigDiaOriginRealm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 9),
    _TmnxMobServSigDiaOriginRealm_Type()
)
tmnxMobServSigDiaOriginRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigDiaOriginRealm.setStatus("current")


class _TmnxMobServSigDiaOriginHost_Type(TmnxMobDiaPeerHost):
    """Custom type tmnxMobServSigDiaOriginHost based on TmnxMobDiaPeerHost"""
    defaultHexValue = ""


_TmnxMobServSigDiaOriginHost_Type.__name__ = "TmnxMobDiaPeerHost"
_TmnxMobServSigDiaOriginHost_Object = MibTableColumn
tmnxMobServSigDiaOriginHost = _TmnxMobServSigDiaOriginHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 10),
    _TmnxMobServSigDiaOriginHost_Type()
)
tmnxMobServSigDiaOriginHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigDiaOriginHost.setStatus("current")


class _TmnxMobServSigDefaultIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServSigDefaultIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServSigDefaultIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServSigDefaultIfVRtrId_Object = MibTableColumn
tmnxMobServSigDefaultIfVRtrId = _TmnxMobServSigDefaultIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 11),
    _TmnxMobServSigDefaultIfVRtrId_Type()
)
tmnxMobServSigDefaultIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigDefaultIfVRtrId.setStatus("current")


class _TmnxMobServSigDefaultIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServSigDefaultIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServSigDefaultIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServSigDefaultIfIndex_Object = MibTableColumn
tmnxMobServSigDefaultIfIndex = _TmnxMobServSigDefaultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 2, 1, 12),
    _TmnxMobServSigDefaultIfIndex_Type()
)
tmnxMobServSigDefaultIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServSigDefaultIfIndex.setStatus("current")
_TmnxMobServGxcTable_Object = MibTable
tmnxMobServGxcTable = _TmnxMobServGxcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxMobServGxcTable.setStatus("current")
_TmnxMobServGxcEntry_Object = MibTableRow
tmnxMobServGxcEntry = _TmnxMobServGxcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServGxcEntry.setStatus("current")
_TmnxMobServGxcLastChanged_Type = TimeStamp
_TmnxMobServGxcLastChanged_Object = MibTableColumn
tmnxMobServGxcLastChanged = _TmnxMobServGxcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1, 1),
    _TmnxMobServGxcLastChanged_Type()
)
tmnxMobServGxcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcLastChanged.setStatus("current")


class _TmnxMobServGxcDiaIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServGxcDiaIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServGxcDiaIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServGxcDiaIfVRtrId_Object = MibTableColumn
tmnxMobServGxcDiaIfVRtrId = _TmnxMobServGxcDiaIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1, 2),
    _TmnxMobServGxcDiaIfVRtrId_Type()
)
tmnxMobServGxcDiaIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGxcDiaIfVRtrId.setStatus("current")


class _TmnxMobServGxcDiaIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServGxcDiaIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServGxcDiaIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServGxcDiaIfIndex_Object = MibTableColumn
tmnxMobServGxcDiaIfIndex = _TmnxMobServGxcDiaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1, 3),
    _TmnxMobServGxcDiaIfIndex_Type()
)
tmnxMobServGxcDiaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGxcDiaIfIndex.setStatus("current")


class _TmnxMobServGxcDiaTransTimer_Type(TmnxMobDiaTransTimer):
    """Custom type tmnxMobServGxcDiaTransTimer based on TmnxMobDiaTransTimer"""
    defaultValue = 5


_TmnxMobServGxcDiaTransTimer_Type.__name__ = "TmnxMobDiaTransTimer"
_TmnxMobServGxcDiaTransTimer_Object = MibTableColumn
tmnxMobServGxcDiaTransTimer = _TmnxMobServGxcDiaTransTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1, 4),
    _TmnxMobServGxcDiaTransTimer_Type()
)
tmnxMobServGxcDiaTransTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGxcDiaTransTimer.setStatus("current")


class _TmnxMobServGxcDiaRetryCount_Type(TmnxMobDiaRetryCount):
    """Custom type tmnxMobServGxcDiaRetryCount based on TmnxMobDiaRetryCount"""
    defaultValue = 3


_TmnxMobServGxcDiaRetryCount_Type.__name__ = "TmnxMobDiaRetryCount"
_TmnxMobServGxcDiaRetryCount_Object = MibTableColumn
tmnxMobServGxcDiaRetryCount = _TmnxMobServGxcDiaRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1, 5),
    _TmnxMobServGxcDiaRetryCount_Type()
)
tmnxMobServGxcDiaRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGxcDiaRetryCount.setStatus("current")


class _TmnxMobServGxcDiameterApp_Type(Unsigned32):
    """Custom type tmnxMobServGxcDiameterApp based on Unsigned32"""
    defaultValue = 0


_TmnxMobServGxcDiameterApp_Type.__name__ = "Unsigned32"
_TmnxMobServGxcDiameterApp_Object = MibTableColumn
tmnxMobServGxcDiameterApp = _TmnxMobServGxcDiameterApp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1, 6),
    _TmnxMobServGxcDiameterApp_Type()
)
tmnxMobServGxcDiameterApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGxcDiameterApp.setStatus("current")


class _TmnxMobServGxcDefPriDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServGxcDefPriDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServGxcDefPriDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServGxcDefPriDiaPeer_Object = MibTableColumn
tmnxMobServGxcDefPriDiaPeer = _TmnxMobServGxcDefPriDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1, 7),
    _TmnxMobServGxcDefPriDiaPeer_Type()
)
tmnxMobServGxcDefPriDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGxcDefPriDiaPeer.setStatus("current")


class _TmnxMobServGxcDefSecDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServGxcDefSecDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServGxcDefSecDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServGxcDefSecDiaPeer_Object = MibTableColumn
tmnxMobServGxcDefSecDiaPeer = _TmnxMobServGxcDefSecDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 3, 1, 8),
    _TmnxMobServGxcDefSecDiaPeer_Type()
)
tmnxMobServGxcDefSecDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGxcDefSecDiaPeer.setStatus("current")
_TmnxMobServS5Table_Object = MibTable
tmnxMobServS5Table = _TmnxMobServS5Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxMobServS5Table.setStatus("current")
_TmnxMobServS5Entry_Object = MibTableRow
tmnxMobServS5Entry = _TmnxMobServS5Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServS5Entry.setStatus("current")
_TmnxMobServS5LastChanged_Type = TimeStamp
_TmnxMobServS5LastChanged_Object = MibTableColumn
tmnxMobServS5LastChanged = _TmnxMobServS5LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 1),
    _TmnxMobServS5LastChanged_Type()
)
tmnxMobServS5LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS5LastChanged.setStatus("current")


class _TmnxMobServS5PeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS5PeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS5PeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS5PeerList_Object = MibTableColumn
tmnxMobServS5PeerList = _TmnxMobServS5PeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 2),
    _TmnxMobServS5PeerList_Type()
)
tmnxMobServS5PeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5PeerList.setStatus("current")


class _TmnxMobServS5GtpcIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS5GtpcIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS5GtpcIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS5GtpcIfVRtrId_Object = MibTableColumn
tmnxMobServS5GtpcIfVRtrId = _TmnxMobServS5GtpcIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 3),
    _TmnxMobServS5GtpcIfVRtrId_Type()
)
tmnxMobServS5GtpcIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5GtpcIfVRtrId.setStatus("current")


class _TmnxMobServS5GtpcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS5GtpcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS5GtpcIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS5GtpcIfIndex_Object = MibTableColumn
tmnxMobServS5GtpcIfIndex = _TmnxMobServS5GtpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 4),
    _TmnxMobServS5GtpcIfIndex_Type()
)
tmnxMobServS5GtpcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5GtpcIfIndex.setStatus("current")


class _TmnxMobServS5GtpuIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS5GtpuIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS5GtpuIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS5GtpuIfVRtrId_Object = MibTableColumn
tmnxMobServS5GtpuIfVRtrId = _TmnxMobServS5GtpuIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 5),
    _TmnxMobServS5GtpuIfVRtrId_Type()
)
tmnxMobServS5GtpuIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5GtpuIfVRtrId.setStatus("current")


class _TmnxMobServS5GtpuIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS5GtpuIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS5GtpuIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS5GtpuIfIndex_Object = MibTableColumn
tmnxMobServS5GtpuIfIndex = _TmnxMobServS5GtpuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 6),
    _TmnxMobServS5GtpuIfIndex_Type()
)
tmnxMobServS5GtpuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5GtpuIfIndex.setStatus("current")


class _TmnxMobServS5Pmipv6IfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS5Pmipv6IfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS5Pmipv6IfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS5Pmipv6IfVRtrId_Object = MibTableColumn
tmnxMobServS5Pmipv6IfVRtrId = _TmnxMobServS5Pmipv6IfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 7),
    _TmnxMobServS5Pmipv6IfVRtrId_Type()
)
tmnxMobServS5Pmipv6IfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6IfVRtrId.setStatus("current")


class _TmnxMobServS5Pmipv6IfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS5Pmipv6IfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS5Pmipv6IfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS5Pmipv6IfIndex_Object = MibTableColumn
tmnxMobServS5Pmipv6IfIndex = _TmnxMobServS5Pmipv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 8),
    _TmnxMobServS5Pmipv6IfIndex_Type()
)
tmnxMobServS5Pmipv6IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6IfIndex.setStatus("current")


class _TmnxMobServS5Pmipv6LnkLclAdrType_Type(InetAddressType):
    """Custom type tmnxMobServS5Pmipv6LnkLclAdrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobServS5Pmipv6LnkLclAdrType_Type.__name__ = "InetAddressType"
_TmnxMobServS5Pmipv6LnkLclAdrType_Object = MibTableColumn
tmnxMobServS5Pmipv6LnkLclAdrType = _TmnxMobServS5Pmipv6LnkLclAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 9),
    _TmnxMobServS5Pmipv6LnkLclAdrType_Type()
)
tmnxMobServS5Pmipv6LnkLclAdrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6LnkLclAdrType.setStatus("current")


class _TmnxMobServS5Pmipv6LnkLclAddress_Type(InetAddress):
    """Custom type tmnxMobServS5Pmipv6LnkLclAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServS5Pmipv6LnkLclAddress_Type.__name__ = "InetAddress"
_TmnxMobServS5Pmipv6LnkLclAddress_Object = MibTableColumn
tmnxMobServS5Pmipv6LnkLclAddress = _TmnxMobServS5Pmipv6LnkLclAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 10),
    _TmnxMobServS5Pmipv6LnkLclAddress_Type()
)
tmnxMobServS5Pmipv6LnkLclAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6LnkLclAddress.setStatus("current")


class _TmnxMobServS5GtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS5GtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS5GtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS5GtpcProfile_Object = MibTableColumn
tmnxMobServS5GtpcProfile = _TmnxMobServS5GtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 11),
    _TmnxMobServS5GtpcProfile_Type()
)
tmnxMobServS5GtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5GtpcProfile.setStatus("current")


class _TmnxMobServS5GtpuProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS5GtpuProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS5GtpuProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS5GtpuProfile_Object = MibTableColumn
tmnxMobServS5GtpuProfile = _TmnxMobServS5GtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 12),
    _TmnxMobServS5GtpuProfile_Type()
)
tmnxMobServS5GtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5GtpuProfile.setStatus("current")


class _TmnxMobServS5Pmipv6Profile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS5Pmipv6Profile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS5Pmipv6Profile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS5Pmipv6Profile_Object = MibTableColumn
tmnxMobServS5Pmipv6Profile = _TmnxMobServS5Pmipv6Profile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 13),
    _TmnxMobServS5Pmipv6Profile_Type()
)
tmnxMobServS5Pmipv6Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6Profile.setStatus("current")


class _TmnxMobServS5Pmipv6RtrAdIntvl_Type(TmnxMobRtrAdvtInterval):
    """Custom type tmnxMobServS5Pmipv6RtrAdIntvl based on TmnxMobRtrAdvtInterval"""
    defaultValue = 30


_TmnxMobServS5Pmipv6RtrAdIntvl_Type.__name__ = "TmnxMobRtrAdvtInterval"
_TmnxMobServS5Pmipv6RtrAdIntvl_Object = MibTableColumn
tmnxMobServS5Pmipv6RtrAdIntvl = _TmnxMobServS5Pmipv6RtrAdIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 14),
    _TmnxMobServS5Pmipv6RtrAdIntvl_Type()
)
tmnxMobServS5Pmipv6RtrAdIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6RtrAdIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6RtrAdIntvl.setUnits("minutes")


class _TmnxMobServS5Pmipv6RtrAdLife_Type(TmnxMobRtrAdvtLifeTime):
    """Custom type tmnxMobServS5Pmipv6RtrAdLife based on TmnxMobRtrAdvtLifeTime"""
    defaultValue = 12


_TmnxMobServS5Pmipv6RtrAdLife_Type.__name__ = "TmnxMobRtrAdvtLifeTime"
_TmnxMobServS5Pmipv6RtrAdLife_Object = MibTableColumn
tmnxMobServS5Pmipv6RtrAdLife = _TmnxMobServS5Pmipv6RtrAdLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 15),
    _TmnxMobServS5Pmipv6RtrAdLife_Type()
)
tmnxMobServS5Pmipv6RtrAdLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6RtrAdLife.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6RtrAdLife.setUnits("hours")


class _TmnxMobServS5Pmipv6RtrAddrScheme_Type(TmnxMobAddrScheme):
    """Custom type tmnxMobServS5Pmipv6RtrAddrScheme based on TmnxMobAddrScheme"""
    defaultValue = 2


_TmnxMobServS5Pmipv6RtrAddrScheme_Type.__name__ = "TmnxMobAddrScheme"
_TmnxMobServS5Pmipv6RtrAddrScheme_Object = MibTableColumn
tmnxMobServS5Pmipv6RtrAddrScheme = _TmnxMobServS5Pmipv6RtrAddrScheme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 16),
    _TmnxMobServS5Pmipv6RtrAddrScheme_Type()
)
tmnxMobServS5Pmipv6RtrAddrScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5Pmipv6RtrAddrScheme.setStatus("current")


class _TmnxMobServS5DualStackPref_Type(TmnxMobDualStackPref):
    """Custom type tmnxMobServS5DualStackPref based on TmnxMobDualStackPref"""
    defaultValue = 3


_TmnxMobServS5DualStackPref_Type.__name__ = "TmnxMobDualStackPref"
_TmnxMobServS5DualStackPref_Object = MibTableColumn
tmnxMobServS5DualStackPref = _TmnxMobServS5DualStackPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 17),
    _TmnxMobServS5DualStackPref_Type()
)
tmnxMobServS5DualStackPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5DualStackPref.setStatus("current")


class _TmnxMobServS5DualStackPrefCplane_Type(Integer32):
    """Custom type tmnxMobServS5DualStackPrefCplane based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_TmnxMobServS5DualStackPrefCplane_Type.__name__ = "Integer32"
_TmnxMobServS5DualStackPrefCplane_Object = MibTableColumn
tmnxMobServS5DualStackPrefCplane = _TmnxMobServS5DualStackPrefCplane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 4, 1, 18),
    _TmnxMobServS5DualStackPrefCplane_Type()
)
tmnxMobServS5DualStackPrefCplane.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS5DualStackPrefCplane.setStatus("current")
_TmnxMobServS8Table_Object = MibTable
tmnxMobServS8Table = _TmnxMobServS8Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxMobServS8Table.setStatus("current")
_TmnxMobServS8Entry_Object = MibTableRow
tmnxMobServS8Entry = _TmnxMobServS8Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServS8Entry.setStatus("current")
_TmnxMobServS8LastChanged_Type = TimeStamp
_TmnxMobServS8LastChanged_Object = MibTableColumn
tmnxMobServS8LastChanged = _TmnxMobServS8LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 1),
    _TmnxMobServS8LastChanged_Type()
)
tmnxMobServS8LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS8LastChanged.setStatus("current")


class _TmnxMobServS8PeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS8PeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS8PeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS8PeerList_Object = MibTableColumn
tmnxMobServS8PeerList = _TmnxMobServS8PeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 2),
    _TmnxMobServS8PeerList_Type()
)
tmnxMobServS8PeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8PeerList.setStatus("current")


class _TmnxMobServS8GtpcIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS8GtpcIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS8GtpcIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS8GtpcIfVRtrId_Object = MibTableColumn
tmnxMobServS8GtpcIfVRtrId = _TmnxMobServS8GtpcIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 3),
    _TmnxMobServS8GtpcIfVRtrId_Type()
)
tmnxMobServS8GtpcIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8GtpcIfVRtrId.setStatus("current")


class _TmnxMobServS8GtpcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS8GtpcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS8GtpcIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS8GtpcIfIndex_Object = MibTableColumn
tmnxMobServS8GtpcIfIndex = _TmnxMobServS8GtpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 4),
    _TmnxMobServS8GtpcIfIndex_Type()
)
tmnxMobServS8GtpcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8GtpcIfIndex.setStatus("current")


class _TmnxMobServS8GtpuIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS8GtpuIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS8GtpuIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS8GtpuIfVRtrId_Object = MibTableColumn
tmnxMobServS8GtpuIfVRtrId = _TmnxMobServS8GtpuIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 5),
    _TmnxMobServS8GtpuIfVRtrId_Type()
)
tmnxMobServS8GtpuIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8GtpuIfVRtrId.setStatus("current")


class _TmnxMobServS8GtpuIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS8GtpuIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS8GtpuIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS8GtpuIfIndex_Object = MibTableColumn
tmnxMobServS8GtpuIfIndex = _TmnxMobServS8GtpuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 6),
    _TmnxMobServS8GtpuIfIndex_Type()
)
tmnxMobServS8GtpuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8GtpuIfIndex.setStatus("current")


class _TmnxMobServS8Pmipv6IfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS8Pmipv6IfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS8Pmipv6IfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS8Pmipv6IfVRtrId_Object = MibTableColumn
tmnxMobServS8Pmipv6IfVRtrId = _TmnxMobServS8Pmipv6IfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 7),
    _TmnxMobServS8Pmipv6IfVRtrId_Type()
)
tmnxMobServS8Pmipv6IfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6IfVRtrId.setStatus("current")


class _TmnxMobServS8Pmipv6IfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS8Pmipv6IfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS8Pmipv6IfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS8Pmipv6IfIndex_Object = MibTableColumn
tmnxMobServS8Pmipv6IfIndex = _TmnxMobServS8Pmipv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 8),
    _TmnxMobServS8Pmipv6IfIndex_Type()
)
tmnxMobServS8Pmipv6IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6IfIndex.setStatus("current")


class _TmnxMobServS8Pmipv6LnkLclAdrType_Type(InetAddressType):
    """Custom type tmnxMobServS8Pmipv6LnkLclAdrType based on InetAddressType"""
    defaultValue = 0


_TmnxMobServS8Pmipv6LnkLclAdrType_Type.__name__ = "InetAddressType"
_TmnxMobServS8Pmipv6LnkLclAdrType_Object = MibTableColumn
tmnxMobServS8Pmipv6LnkLclAdrType = _TmnxMobServS8Pmipv6LnkLclAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 9),
    _TmnxMobServS8Pmipv6LnkLclAdrType_Type()
)
tmnxMobServS8Pmipv6LnkLclAdrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6LnkLclAdrType.setStatus("current")


class _TmnxMobServS8Pmipv6LnkLclAddress_Type(InetAddress):
    """Custom type tmnxMobServS8Pmipv6LnkLclAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServS8Pmipv6LnkLclAddress_Type.__name__ = "InetAddress"
_TmnxMobServS8Pmipv6LnkLclAddress_Object = MibTableColumn
tmnxMobServS8Pmipv6LnkLclAddress = _TmnxMobServS8Pmipv6LnkLclAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 10),
    _TmnxMobServS8Pmipv6LnkLclAddress_Type()
)
tmnxMobServS8Pmipv6LnkLclAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6LnkLclAddress.setStatus("current")


class _TmnxMobServS8GtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS8GtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS8GtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS8GtpcProfile_Object = MibTableColumn
tmnxMobServS8GtpcProfile = _TmnxMobServS8GtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 11),
    _TmnxMobServS8GtpcProfile_Type()
)
tmnxMobServS8GtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8GtpcProfile.setStatus("current")


class _TmnxMobServS8GtpuProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS8GtpuProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS8GtpuProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS8GtpuProfile_Object = MibTableColumn
tmnxMobServS8GtpuProfile = _TmnxMobServS8GtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 12),
    _TmnxMobServS8GtpuProfile_Type()
)
tmnxMobServS8GtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8GtpuProfile.setStatus("current")


class _TmnxMobServS8Pmipv6Profile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS8Pmipv6Profile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS8Pmipv6Profile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS8Pmipv6Profile_Object = MibTableColumn
tmnxMobServS8Pmipv6Profile = _TmnxMobServS8Pmipv6Profile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 13),
    _TmnxMobServS8Pmipv6Profile_Type()
)
tmnxMobServS8Pmipv6Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6Profile.setStatus("current")


class _TmnxMobServS8Pmipv6RtrAdIntvl_Type(TmnxMobRtrAdvtInterval):
    """Custom type tmnxMobServS8Pmipv6RtrAdIntvl based on TmnxMobRtrAdvtInterval"""
    defaultValue = 30


_TmnxMobServS8Pmipv6RtrAdIntvl_Type.__name__ = "TmnxMobRtrAdvtInterval"
_TmnxMobServS8Pmipv6RtrAdIntvl_Object = MibTableColumn
tmnxMobServS8Pmipv6RtrAdIntvl = _TmnxMobServS8Pmipv6RtrAdIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 14),
    _TmnxMobServS8Pmipv6RtrAdIntvl_Type()
)
tmnxMobServS8Pmipv6RtrAdIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6RtrAdIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6RtrAdIntvl.setUnits("minutes")


class _TmnxMobServS8Pmipv6RtrAdLife_Type(TmnxMobRtrAdvtLifeTime):
    """Custom type tmnxMobServS8Pmipv6RtrAdLife based on TmnxMobRtrAdvtLifeTime"""
    defaultValue = 12


_TmnxMobServS8Pmipv6RtrAdLife_Type.__name__ = "TmnxMobRtrAdvtLifeTime"
_TmnxMobServS8Pmipv6RtrAdLife_Object = MibTableColumn
tmnxMobServS8Pmipv6RtrAdLife = _TmnxMobServS8Pmipv6RtrAdLife_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 15),
    _TmnxMobServS8Pmipv6RtrAdLife_Type()
)
tmnxMobServS8Pmipv6RtrAdLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6RtrAdLife.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6RtrAdLife.setUnits("hours")


class _TmnxMobServS8Pmipv6RtrAddrScheme_Type(TmnxMobAddrScheme):
    """Custom type tmnxMobServS8Pmipv6RtrAddrScheme based on TmnxMobAddrScheme"""
    defaultValue = 2


_TmnxMobServS8Pmipv6RtrAddrScheme_Type.__name__ = "TmnxMobAddrScheme"
_TmnxMobServS8Pmipv6RtrAddrScheme_Object = MibTableColumn
tmnxMobServS8Pmipv6RtrAddrScheme = _TmnxMobServS8Pmipv6RtrAddrScheme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 16),
    _TmnxMobServS8Pmipv6RtrAddrScheme_Type()
)
tmnxMobServS8Pmipv6RtrAddrScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8Pmipv6RtrAddrScheme.setStatus("current")


class _TmnxMobServS8DualStackPref_Type(TmnxMobDualStackPref):
    """Custom type tmnxMobServS8DualStackPref based on TmnxMobDualStackPref"""
    defaultValue = 3


_TmnxMobServS8DualStackPref_Type.__name__ = "TmnxMobDualStackPref"
_TmnxMobServS8DualStackPref_Object = MibTableColumn
tmnxMobServS8DualStackPref = _TmnxMobServS8DualStackPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 17),
    _TmnxMobServS8DualStackPref_Type()
)
tmnxMobServS8DualStackPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8DualStackPref.setStatus("current")


class _TmnxMobServS8DualStackPrefCplane_Type(Integer32):
    """Custom type tmnxMobServS8DualStackPrefCplane based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_TmnxMobServS8DualStackPrefCplane_Type.__name__ = "Integer32"
_TmnxMobServS8DualStackPrefCplane_Object = MibTableColumn
tmnxMobServS8DualStackPrefCplane = _TmnxMobServS8DualStackPrefCplane_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 5, 1, 18),
    _TmnxMobServS8DualStackPrefCplane_Type()
)
tmnxMobServS8DualStackPrefCplane.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS8DualStackPrefCplane.setStatus("current")
_TmnxMobServS11Table_Object = MibTable
tmnxMobServS11Table = _TmnxMobServS11Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxMobServS11Table.setStatus("current")
_TmnxMobServS11Entry_Object = MibTableRow
tmnxMobServS11Entry = _TmnxMobServS11Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServS11Entry.setStatus("current")
_TmnxMobServS11LastChanged_Type = TimeStamp
_TmnxMobServS11LastChanged_Object = MibTableColumn
tmnxMobServS11LastChanged = _TmnxMobServS11LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 6, 1, 1),
    _TmnxMobServS11LastChanged_Type()
)
tmnxMobServS11LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11LastChanged.setStatus("current")


class _TmnxMobServS11PeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS11PeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS11PeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS11PeerList_Object = MibTableColumn
tmnxMobServS11PeerList = _TmnxMobServS11PeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 6, 1, 2),
    _TmnxMobServS11PeerList_Type()
)
tmnxMobServS11PeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerList.setStatus("current")


class _TmnxMobServS11GtpcIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS11GtpcIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS11GtpcIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS11GtpcIfVRtrId_Object = MibTableColumn
tmnxMobServS11GtpcIfVRtrId = _TmnxMobServS11GtpcIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 6, 1, 3),
    _TmnxMobServS11GtpcIfVRtrId_Type()
)
tmnxMobServS11GtpcIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS11GtpcIfVRtrId.setStatus("current")


class _TmnxMobServS11GtpcIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS11GtpcIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS11GtpcIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS11GtpcIfIndex_Object = MibTableColumn
tmnxMobServS11GtpcIfIndex = _TmnxMobServS11GtpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 6, 1, 4),
    _TmnxMobServS11GtpcIfIndex_Type()
)
tmnxMobServS11GtpcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS11GtpcIfIndex.setStatus("current")


class _TmnxMobServS11GtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS11GtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS11GtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS11GtpcProfile_Object = MibTableColumn
tmnxMobServS11GtpcProfile = _TmnxMobServS11GtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 6, 1, 5),
    _TmnxMobServS11GtpcProfile_Type()
)
tmnxMobServS11GtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS11GtpcProfile.setStatus("current")


class _TmnxMobServS11GtpcDdnDumpTimer_Type(Unsigned32):
    """Custom type tmnxMobServS11GtpcDdnDumpTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 3600),
    )


_TmnxMobServS11GtpcDdnDumpTimer_Type.__name__ = "Unsigned32"
_TmnxMobServS11GtpcDdnDumpTimer_Object = MibTableColumn
tmnxMobServS11GtpcDdnDumpTimer = _TmnxMobServS11GtpcDdnDumpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 6, 1, 6),
    _TmnxMobServS11GtpcDdnDumpTimer_Type()
)
tmnxMobServS11GtpcDdnDumpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS11GtpcDdnDumpTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServS11GtpcDdnDumpTimer.setUnits("seconds")
_TmnxMobServS1uTable_Object = MibTable
tmnxMobServS1uTable = _TmnxMobServS1uTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxMobServS1uTable.setStatus("current")
_TmnxMobServS1uEntry_Object = MibTableRow
tmnxMobServS1uEntry = _TmnxMobServS1uEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServS1uEntry.setStatus("current")
_TmnxMobServS1uLastChanged_Type = TimeStamp
_TmnxMobServS1uLastChanged_Object = MibTableColumn
tmnxMobServS1uLastChanged = _TmnxMobServS1uLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1, 1),
    _TmnxMobServS1uLastChanged_Type()
)
tmnxMobServS1uLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uLastChanged.setStatus("current")


class _TmnxMobServS1uPeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS1uPeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS1uPeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS1uPeerList_Object = MibTableColumn
tmnxMobServS1uPeerList = _TmnxMobServS1uPeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1, 2),
    _TmnxMobServS1uPeerList_Type()
)
tmnxMobServS1uPeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerList.setStatus("current")


class _TmnxMobServS1uGtpuIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS1uGtpuIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS1uGtpuIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS1uGtpuIfVRtrId_Object = MibTableColumn
tmnxMobServS1uGtpuIfVRtrId = _TmnxMobServS1uGtpuIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1, 3),
    _TmnxMobServS1uGtpuIfVRtrId_Type()
)
tmnxMobServS1uGtpuIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS1uGtpuIfVRtrId.setStatus("current")


class _TmnxMobServS1uGtpuIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS1uGtpuIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS1uGtpuIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS1uGtpuIfIndex_Object = MibTableColumn
tmnxMobServS1uGtpuIfIndex = _TmnxMobServS1uGtpuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1, 4),
    _TmnxMobServS1uGtpuIfIndex_Type()
)
tmnxMobServS1uGtpuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS1uGtpuIfIndex.setStatus("current")


class _TmnxMobServS1uGtpuProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS1uGtpuProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS1uGtpuProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS1uGtpuProfile_Object = MibTableColumn
tmnxMobServS1uGtpuProfile = _TmnxMobServS1uGtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1, 5),
    _TmnxMobServS1uGtpuProfile_Type()
)
tmnxMobServS1uGtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS1uGtpuProfile.setStatus("current")


class _TmnxMobServS1uGtpuUdpCheckSum_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServS1uGtpuUdpCheckSum based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServS1uGtpuUdpCheckSum_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServS1uGtpuUdpCheckSum_Object = MibTableColumn
tmnxMobServS1uGtpuUdpCheckSum = _TmnxMobServS1uGtpuUdpCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1, 6),
    _TmnxMobServS1uGtpuUdpCheckSum_Type()
)
tmnxMobServS1uGtpuUdpCheckSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS1uGtpuUdpCheckSum.setStatus("current")


class _TmnxMobServS1uGtpuSeqNumber_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServS1uGtpuSeqNumber based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServS1uGtpuSeqNumber_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServS1uGtpuSeqNumber_Object = MibTableColumn
tmnxMobServS1uGtpuSeqNumber = _TmnxMobServS1uGtpuSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1, 7),
    _TmnxMobServS1uGtpuSeqNumber_Type()
)
tmnxMobServS1uGtpuSeqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS1uGtpuSeqNumber.setStatus("current")


class _TmnxMobServS1uDualStackPref_Type(Integer32):
    """Custom type tmnxMobServS1uDualStackPref based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_TmnxMobServS1uDualStackPref_Type.__name__ = "Integer32"
_TmnxMobServS1uDualStackPref_Object = MibTableColumn
tmnxMobServS1uDualStackPref = _TmnxMobServS1uDualStackPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 7, 1, 8),
    _TmnxMobServS1uDualStackPref_Type()
)
tmnxMobServS1uDualStackPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS1uDualStackPref.setStatus("current")
_TmnxMobServS12Table_Object = MibTable
tmnxMobServS12Table = _TmnxMobServS12Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxMobServS12Table.setStatus("current")
_TmnxMobServS12Entry_Object = MibTableRow
tmnxMobServS12Entry = _TmnxMobServS12Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServS12Entry.setStatus("current")
_TmnxMobServS12LastChanged_Type = TimeStamp
_TmnxMobServS12LastChanged_Object = MibTableColumn
tmnxMobServS12LastChanged = _TmnxMobServS12LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8, 1, 1),
    _TmnxMobServS12LastChanged_Type()
)
tmnxMobServS12LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS12LastChanged.setStatus("current")


class _TmnxMobServS12PeerList_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS12PeerList based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS12PeerList_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS12PeerList_Object = MibTableColumn
tmnxMobServS12PeerList = _TmnxMobServS12PeerList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8, 1, 2),
    _TmnxMobServS12PeerList_Type()
)
tmnxMobServS12PeerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS12PeerList.setStatus("current")


class _TmnxMobServS12GtpuIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServS12GtpuIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServS12GtpuIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServS12GtpuIfVRtrId_Object = MibTableColumn
tmnxMobServS12GtpuIfVRtrId = _TmnxMobServS12GtpuIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8, 1, 3),
    _TmnxMobServS12GtpuIfVRtrId_Type()
)
tmnxMobServS12GtpuIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS12GtpuIfVRtrId.setStatus("current")


class _TmnxMobServS12GtpuIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServS12GtpuIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServS12GtpuIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServS12GtpuIfIndex_Object = MibTableColumn
tmnxMobServS12GtpuIfIndex = _TmnxMobServS12GtpuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8, 1, 4),
    _TmnxMobServS12GtpuIfIndex_Type()
)
tmnxMobServS12GtpuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS12GtpuIfIndex.setStatus("current")


class _TmnxMobServS12GtpuProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServS12GtpuProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServS12GtpuProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServS12GtpuProfile_Object = MibTableColumn
tmnxMobServS12GtpuProfile = _TmnxMobServS12GtpuProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8, 1, 5),
    _TmnxMobServS12GtpuProfile_Type()
)
tmnxMobServS12GtpuProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS12GtpuProfile.setStatus("current")


class _TmnxMobServS12GtpuUdpCheckSum_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServS12GtpuUdpCheckSum based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServS12GtpuUdpCheckSum_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServS12GtpuUdpCheckSum_Object = MibTableColumn
tmnxMobServS12GtpuUdpCheckSum = _TmnxMobServS12GtpuUdpCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8, 1, 6),
    _TmnxMobServS12GtpuUdpCheckSum_Type()
)
tmnxMobServS12GtpuUdpCheckSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS12GtpuUdpCheckSum.setStatus("current")


class _TmnxMobServS12GtpuSeqNumber_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServS12GtpuSeqNumber based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServS12GtpuSeqNumber_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServS12GtpuSeqNumber_Object = MibTableColumn
tmnxMobServS12GtpuSeqNumber = _TmnxMobServS12GtpuSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 8, 1, 7),
    _TmnxMobServS12GtpuSeqNumber_Type()
)
tmnxMobServS12GtpuSeqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServS12GtpuSeqNumber.setStatus("current")
_TmnxMobServRfTable_Object = MibTable
tmnxMobServRfTable = _TmnxMobServRfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxMobServRfTable.setStatus("current")
_TmnxMobServRfEntry_Object = MibTableRow
tmnxMobServRfEntry = _TmnxMobServRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServRfEntry.setStatus("current")
_TmnxMobServRfLastChanged_Type = TimeStamp
_TmnxMobServRfLastChanged_Object = MibTableColumn
tmnxMobServRfLastChanged = _TmnxMobServRfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 1),
    _TmnxMobServRfLastChanged_Type()
)
tmnxMobServRfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServRfLastChanged.setStatus("current")


class _TmnxMobServRfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServRfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServRfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServRfVRtrId_Object = MibTableColumn
tmnxMobServRfVRtrId = _TmnxMobServRfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 2),
    _TmnxMobServRfVRtrId_Type()
)
tmnxMobServRfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfVRtrId.setStatus("current")


class _TmnxMobServRfIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServRfIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServRfIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServRfIfIndex_Object = MibTableColumn
tmnxMobServRfIfIndex = _TmnxMobServRfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 3),
    _TmnxMobServRfIfIndex_Type()
)
tmnxMobServRfIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfIfIndex.setStatus("current")


class _TmnxMobServRfPriDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServRfPriDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServRfPriDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServRfPriDiaPeer_Object = MibTableColumn
tmnxMobServRfPriDiaPeer = _TmnxMobServRfPriDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 4),
    _TmnxMobServRfPriDiaPeer_Type()
)
tmnxMobServRfPriDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfPriDiaPeer.setStatus("current")


class _TmnxMobServRfSecDiaPeer_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServRfSecDiaPeer based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServRfSecDiaPeer_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServRfSecDiaPeer_Object = MibTableColumn
tmnxMobServRfSecDiaPeer = _TmnxMobServRfSecDiaPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 5),
    _TmnxMobServRfSecDiaPeer_Type()
)
tmnxMobServRfSecDiaPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfSecDiaPeer.setStatus("current")


class _TmnxMobServRfAcctIntmInterval_Type(Unsigned32):
    """Custom type tmnxMobServRfAcctIntmInterval based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_TmnxMobServRfAcctIntmInterval_Type.__name__ = "Unsigned32"
_TmnxMobServRfAcctIntmInterval_Object = MibTableColumn
tmnxMobServRfAcctIntmInterval = _TmnxMobServRfAcctIntmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 6),
    _TmnxMobServRfAcctIntmInterval_Type()
)
tmnxMobServRfAcctIntmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfAcctIntmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServRfAcctIntmInterval.setUnits("seconds")


class _TmnxMobServRfApplTxTimer_Type(Unsigned32):
    """Custom type tmnxMobServRfApplTxTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TmnxMobServRfApplTxTimer_Type.__name__ = "Unsigned32"
_TmnxMobServRfApplTxTimer_Object = MibTableColumn
tmnxMobServRfApplTxTimer = _TmnxMobServRfApplTxTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 7),
    _TmnxMobServRfApplTxTimer_Type()
)
tmnxMobServRfApplTxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfApplTxTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServRfApplTxTimer.setUnits("seconds")


class _TmnxMobServRfRetryCount_Type(TmnxMobDiaRetryCount):
    """Custom type tmnxMobServRfRetryCount based on TmnxMobDiaRetryCount"""
    defaultValue = 3


_TmnxMobServRfRetryCount_Type.__name__ = "TmnxMobDiaRetryCount"
_TmnxMobServRfRetryCount_Object = MibTableColumn
tmnxMobServRfRetryCount = _TmnxMobServRfRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 8),
    _TmnxMobServRfRetryCount_Type()
)
tmnxMobServRfRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServRfRetryCount.setUnits("seconds")


class _TmnxMobServRfChargingGroupID_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServRfChargingGroupID based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServRfChargingGroupID_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServRfChargingGroupID_Object = MibTableColumn
tmnxMobServRfChargingGroupID = _TmnxMobServRfChargingGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 9),
    _TmnxMobServRfChargingGroupID_Type()
)
tmnxMobServRfChargingGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfChargingGroupID.setStatus("current")


class _TmnxMobServRfOperatorString_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobServRfOperatorString based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobServRfOperatorString_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobServRfOperatorString_Object = MibTableColumn
tmnxMobServRfOperatorString = _TmnxMobServRfOperatorString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 10),
    _TmnxMobServRfOperatorString_Type()
)
tmnxMobServRfOperatorString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOperatorString.setStatus("current")


class _TmnxMobServRfAcctLevel_Type(TmnxMobRfAcctLevel):
    """Custom type tmnxMobServRfAcctLevel based on TmnxMobRfAcctLevel"""
    defaultValue = 2


_TmnxMobServRfAcctLevel_Type.__name__ = "TmnxMobRfAcctLevel"
_TmnxMobServRfAcctLevel_Object = MibTableColumn
tmnxMobServRfAcctLevel = _TmnxMobServRfAcctLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 11),
    _TmnxMobServRfAcctLevel_Type()
)
tmnxMobServRfAcctLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfAcctLevel.setStatus("current")


class _TmnxMobServRfNodeId_Type(DisplayString):
    """Custom type tmnxMobServRfNodeId based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxMobServRfNodeId_Type.__name__ = "DisplayString"
_TmnxMobServRfNodeId_Object = MibTableColumn
tmnxMobServRfNodeId = _TmnxMobServRfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 12),
    _TmnxMobServRfNodeId_Type()
)
tmnxMobServRfNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfNodeId.setStatus("current")


class _TmnxMobServRfOcFilePrivateInfo_Type(TNamedItemOrEmpty):
    """Custom type tmnxMobServRfOcFilePrivateInfo based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxMobServRfOcFilePrivateInfo_Type.__name__ = "TNamedItemOrEmpty"
_TmnxMobServRfOcFilePrivateInfo_Object = MibTableColumn
tmnxMobServRfOcFilePrivateInfo = _TmnxMobServRfOcFilePrivateInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 13),
    _TmnxMobServRfOcFilePrivateInfo_Type()
)
tmnxMobServRfOcFilePrivateInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFilePrivateInfo.setStatus("current")


class _TmnxMobServRfOcFileExtension_Type(DisplayString):
    """Custom type tmnxMobServRfOcFileExtension based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxMobServRfOcFileExtension_Type.__name__ = "DisplayString"
_TmnxMobServRfOcFileExtension_Object = MibTableColumn
tmnxMobServRfOcFileExtension = _TmnxMobServRfOcFileExtension_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 14),
    _TmnxMobServRfOcFileExtension_Type()
)
tmnxMobServRfOcFileExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFileExtension.setStatus("current")


class _TmnxMobServRfOcFileClosureSize_Type(Unsigned32):
    """Custom type tmnxMobServRfOcFileClosureSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxMobServRfOcFileClosureSize_Type.__name__ = "Unsigned32"
_TmnxMobServRfOcFileClosureSize_Object = MibTableColumn
tmnxMobServRfOcFileClosureSize = _TmnxMobServRfOcFileClosureSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 15),
    _TmnxMobServRfOcFileClosureSize_Type()
)
tmnxMobServRfOcFileClosureSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFileClosureSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFileClosureSize.setUnits("megabytes")


class _TmnxMobServRfOcFileClsLifeTime_Type(Unsigned32):
    """Custom type tmnxMobServRfOcFileClsLifeTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_TmnxMobServRfOcFileClsLifeTime_Type.__name__ = "Unsigned32"
_TmnxMobServRfOcFileClsLifeTime_Object = MibTableColumn
tmnxMobServRfOcFileClsLifeTime = _TmnxMobServRfOcFileClsLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 16),
    _TmnxMobServRfOcFileClsLifeTime_Type()
)
tmnxMobServRfOcFileClsLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFileClsLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFileClsLifeTime.setUnits("hours")


class _TmnxMobServRfOcFileClsMaxAcrs_Type(Unsigned32):
    """Custom type tmnxMobServRfOcFileClsMaxAcrs based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 75000),
    )


_TmnxMobServRfOcFileClsMaxAcrs_Type.__name__ = "Unsigned32"
_TmnxMobServRfOcFileClsMaxAcrs_Object = MibTableColumn
tmnxMobServRfOcFileClsMaxAcrs = _TmnxMobServRfOcFileClsMaxAcrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 17),
    _TmnxMobServRfOcFileClsMaxAcrs_Type()
)
tmnxMobServRfOcFileClsMaxAcrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFileClsMaxAcrs.setStatus("current")


class _TmnxMobServRfOcFileObsoleteTime_Type(Unsigned32):
    """Custom type tmnxMobServRfOcFileObsoleteTime based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TmnxMobServRfOcFileObsoleteTime_Type.__name__ = "Unsigned32"
_TmnxMobServRfOcFileObsoleteTime_Object = MibTableColumn
tmnxMobServRfOcFileObsoleteTime = _TmnxMobServRfOcFileObsoleteTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 18),
    _TmnxMobServRfOcFileObsoleteTime_Type()
)
tmnxMobServRfOcFileObsoleteTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFileObsoleteTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServRfOcFileObsoleteTime.setUnits("days")


class _TmnxMobServRfOcPrimaryCf_Type(Integer32):
    """Custom type tmnxMobServRfOcPrimaryCf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cf1", 1),
          ("cf2", 2))
    )


_TmnxMobServRfOcPrimaryCf_Type.__name__ = "Integer32"
_TmnxMobServRfOcPrimaryCf_Object = MibTableColumn
tmnxMobServRfOcPrimaryCf = _TmnxMobServRfOcPrimaryCf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 19),
    _TmnxMobServRfOcPrimaryCf_Type()
)
tmnxMobServRfOcPrimaryCf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcPrimaryCf.setStatus("current")


class _TmnxMobServRfOcCf1State_Type(TruthValue):
    """Custom type tmnxMobServRfOcCf1State based on TruthValue"""
    defaultValue = 1


_TmnxMobServRfOcCf1State_Type.__name__ = "TruthValue"
_TmnxMobServRfOcCf1State_Object = MibTableColumn
tmnxMobServRfOcCf1State = _TmnxMobServRfOcCf1State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 20),
    _TmnxMobServRfOcCf1State_Type()
)
tmnxMobServRfOcCf1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcCf1State.setStatus("current")


class _TmnxMobServRfOcCf1Limit_Type(Unsigned32):
    """Custom type tmnxMobServRfOcCf1Limit based on Unsigned32"""
    defaultValue = 0


_TmnxMobServRfOcCf1Limit_Type.__name__ = "Unsigned32"
_TmnxMobServRfOcCf1Limit_Object = MibTableColumn
tmnxMobServRfOcCf1Limit = _TmnxMobServRfOcCf1Limit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 21),
    _TmnxMobServRfOcCf1Limit_Type()
)
tmnxMobServRfOcCf1Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcCf1Limit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServRfOcCf1Limit.setUnits("megabytes")


class _TmnxMobServRfOcCf2State_Type(TruthValue):
    """Custom type tmnxMobServRfOcCf2State based on TruthValue"""
    defaultValue = 1


_TmnxMobServRfOcCf2State_Type.__name__ = "TruthValue"
_TmnxMobServRfOcCf2State_Object = MibTableColumn
tmnxMobServRfOcCf2State = _TmnxMobServRfOcCf2State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 22),
    _TmnxMobServRfOcCf2State_Type()
)
tmnxMobServRfOcCf2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcCf2State.setStatus("current")


class _TmnxMobServRfOcCf2Limit_Type(Unsigned32):
    """Custom type tmnxMobServRfOcCf2Limit based on Unsigned32"""
    defaultValue = 0


_TmnxMobServRfOcCf2Limit_Type.__name__ = "Unsigned32"
_TmnxMobServRfOcCf2Limit_Object = MibTableColumn
tmnxMobServRfOcCf2Limit = _TmnxMobServRfOcCf2Limit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 23),
    _TmnxMobServRfOcCf2Limit_Type()
)
tmnxMobServRfOcCf2Limit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfOcCf2Limit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServRfOcCf2Limit.setUnits("megabytes")


class _TmnxMobServRfSuppVendorAvps_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServRfSuppVendorAvps based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxMobServRfSuppVendorAvps_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServRfSuppVendorAvps_Object = MibTableColumn
tmnxMobServRfSuppVendorAvps = _TmnxMobServRfSuppVendorAvps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 9, 1, 24),
    _TmnxMobServRfSuppVendorAvps_Type()
)
tmnxMobServRfSuppVendorAvps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServRfSuppVendorAvps.setStatus("current")
_TmnxMobServApnTable_Object = MibTable
tmnxMobServApnTable = _TmnxMobServApnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxMobServApnTable.setStatus("current")
_TmnxMobServApnEntry_Object = MibTableRow
tmnxMobServApnEntry = _TmnxMobServApnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1)
)
tmnxMobServApnEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnName"),
)
if mibBuilder.loadTexts:
    tmnxMobServApnEntry.setStatus("current")
_TmnxMobServApnName_Type = TmnxMobApn
_TmnxMobServApnName_Object = MibTableColumn
tmnxMobServApnName = _TmnxMobServApnName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 1),
    _TmnxMobServApnName_Type()
)
tmnxMobServApnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServApnName.setStatus("current")
_TmnxMobServApnRowStatus_Type = RowStatus
_TmnxMobServApnRowStatus_Object = MibTableColumn
tmnxMobServApnRowStatus = _TmnxMobServApnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 2),
    _TmnxMobServApnRowStatus_Type()
)
tmnxMobServApnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnRowStatus.setStatus("current")
_TmnxMobServApnLastChanged_Type = TimeStamp
_TmnxMobServApnLastChanged_Object = MibTableColumn
tmnxMobServApnLastChanged = _TmnxMobServApnLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 3),
    _TmnxMobServApnLastChanged_Type()
)
tmnxMobServApnLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServApnLastChanged.setStatus("current")


class _TmnxMobServApnDescription_Type(TItemDescription):
    """Custom type tmnxMobServApnDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxMobServApnDescription_Type.__name__ = "TItemDescription"
_TmnxMobServApnDescription_Object = MibTableColumn
tmnxMobServApnDescription = _TmnxMobServApnDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 4),
    _TmnxMobServApnDescription_Type()
)
tmnxMobServApnDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnDescription.setStatus("current")


class _TmnxMobServApnDynamicPcc_Type(TmnxEnabledDisabled):
    """Custom type tmnxMobServApnDynamicPcc based on TmnxEnabledDisabled"""
    defaultValue = 1


_TmnxMobServApnDynamicPcc_Type.__name__ = "TmnxEnabledDisabled"
_TmnxMobServApnDynamicPcc_Object = MibTableColumn
tmnxMobServApnDynamicPcc = _TmnxMobServApnDynamicPcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 5),
    _TmnxMobServApnDynamicPcc_Type()
)
tmnxMobServApnDynamicPcc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnDynamicPcc.setStatus("current")


class _TmnxMobServApnUplinkQciPolName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServApnUplinkQciPolName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServApnUplinkQciPolName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServApnUplinkQciPolName_Object = MibTableColumn
tmnxMobServApnUplinkQciPolName = _TmnxMobServApnUplinkQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 6),
    _TmnxMobServApnUplinkQciPolName_Type()
)
tmnxMobServApnUplinkQciPolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnUplinkQciPolName.setStatus("current")


class _TmnxMobServApnDownlinkQciPolName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServApnDownlinkQciPolName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServApnDownlinkQciPolName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServApnDownlinkQciPolName_Object = MibTableColumn
tmnxMobServApnDownlinkQciPolName = _TmnxMobServApnDownlinkQciPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 7),
    _TmnxMobServApnDownlinkQciPolName_Type()
)
tmnxMobServApnDownlinkQciPolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnDownlinkQciPolName.setStatus("current")


class _TmnxMobServApnPolBaseName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServApnPolBaseName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServApnPolBaseName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServApnPolBaseName_Object = MibTableColumn
tmnxMobServApnPolBaseName = _TmnxMobServApnPolBaseName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 8),
    _TmnxMobServApnPolBaseName_Type()
)
tmnxMobServApnPolBaseName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnPolBaseName.setStatus("current")


class _TmnxMobServApnChrgProfileHome_Type(TmnxMobChargingProfileOrInherit):
    """Custom type tmnxMobServApnChrgProfileHome based on TmnxMobChargingProfileOrInherit"""
    defaultValue = -1


_TmnxMobServApnChrgProfileHome_Type.__name__ = "TmnxMobChargingProfileOrInherit"
_TmnxMobServApnChrgProfileHome_Object = MibTableColumn
tmnxMobServApnChrgProfileHome = _TmnxMobServApnChrgProfileHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 9),
    _TmnxMobServApnChrgProfileHome_Type()
)
tmnxMobServApnChrgProfileHome.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnChrgProfileHome.setStatus("current")


class _TmnxMobServApnChrgProfVisiting_Type(TmnxMobChargingProfileOrInherit):
    """Custom type tmnxMobServApnChrgProfVisiting based on TmnxMobChargingProfileOrInherit"""
    defaultValue = -1


_TmnxMobServApnChrgProfVisiting_Type.__name__ = "TmnxMobChargingProfileOrInherit"
_TmnxMobServApnChrgProfVisiting_Object = MibTableColumn
tmnxMobServApnChrgProfVisiting = _TmnxMobServApnChrgProfVisiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 10),
    _TmnxMobServApnChrgProfVisiting_Type()
)
tmnxMobServApnChrgProfVisiting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnChrgProfVisiting.setStatus("current")


class _TmnxMobServApnChrgProfileRoaming_Type(TmnxMobChargingProfileOrInherit):
    """Custom type tmnxMobServApnChrgProfileRoaming based on TmnxMobChargingProfileOrInherit"""
    defaultValue = -1


_TmnxMobServApnChrgProfileRoaming_Type.__name__ = "TmnxMobChargingProfileOrInherit"
_TmnxMobServApnChrgProfileRoaming_Object = MibTableColumn
tmnxMobServApnChrgProfileRoaming = _TmnxMobServApnChrgProfileRoaming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 11),
    _TmnxMobServApnChrgProfileRoaming_Type()
)
tmnxMobServApnChrgProfileRoaming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnChrgProfileRoaming.setStatus("current")


class _TmnxMobServApnChrgCcIgnoreAny_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobServApnChrgCcIgnoreAny based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobServApnChrgCcIgnoreAny_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobServApnChrgCcIgnoreAny_Object = MibTableColumn
tmnxMobServApnChrgCcIgnoreAny = _TmnxMobServApnChrgCcIgnoreAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 12),
    _TmnxMobServApnChrgCcIgnoreAny_Type()
)
tmnxMobServApnChrgCcIgnoreAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnChrgCcIgnoreAny.setStatus("current")


class _TmnxMobServApnChrgCcIgnoreHome_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobServApnChrgCcIgnoreHome based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobServApnChrgCcIgnoreHome_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobServApnChrgCcIgnoreHome_Object = MibTableColumn
tmnxMobServApnChrgCcIgnoreHome = _TmnxMobServApnChrgCcIgnoreHome_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 13),
    _TmnxMobServApnChrgCcIgnoreHome_Type()
)
tmnxMobServApnChrgCcIgnoreHome.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnChrgCcIgnoreHome.setStatus("current")


class _TmnxMobServApnChrgCcIgnoreVisit_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobServApnChrgCcIgnoreVisit based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobServApnChrgCcIgnoreVisit_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobServApnChrgCcIgnoreVisit_Object = MibTableColumn
tmnxMobServApnChrgCcIgnoreVisit = _TmnxMobServApnChrgCcIgnoreVisit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 14),
    _TmnxMobServApnChrgCcIgnoreVisit_Type()
)
tmnxMobServApnChrgCcIgnoreVisit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnChrgCcIgnoreVisit.setStatus("current")


class _TmnxMobServApnChrgCcIgnorRoaming_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobServApnChrgCcIgnorRoaming based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobServApnChrgCcIgnorRoaming_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobServApnChrgCcIgnorRoaming_Object = MibTableColumn
tmnxMobServApnChrgCcIgnorRoaming = _TmnxMobServApnChrgCcIgnorRoaming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 15),
    _TmnxMobServApnChrgCcIgnorRoaming_Type()
)
tmnxMobServApnChrgCcIgnorRoaming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnChrgCcIgnorRoaming.setStatus("current")


class _TmnxMobServApnChrgCcReject_Type(TmnxEnabledDisabledOrInherit):
    """Custom type tmnxMobServApnChrgCcReject based on TmnxEnabledDisabledOrInherit"""
    defaultValue = 3


_TmnxMobServApnChrgCcReject_Type.__name__ = "TmnxEnabledDisabledOrInherit"
_TmnxMobServApnChrgCcReject_Object = MibTableColumn
tmnxMobServApnChrgCcReject = _TmnxMobServApnChrgCcReject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 10, 1, 16),
    _TmnxMobServApnChrgCcReject_Type()
)
tmnxMobServApnChrgCcReject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApnChrgCcReject.setStatus("current")
_TmnxMobServApTable_Object = MibTable
tmnxMobServApTable = _TmnxMobServApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxMobServApTable.setStatus("current")
_TmnxMobServApEntry_Object = MibTableRow
tmnxMobServApEntry = _TmnxMobServApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 11, 1)
)
tmnxMobServApEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxMobServApEntry.setStatus("current")


class _TmnxMobServApPolicyId_Type(Unsigned32):
    """Custom type tmnxMobServApPolicyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TmnxMobServApPolicyId_Type.__name__ = "Unsigned32"
_TmnxMobServApPolicyId_Object = MibTableColumn
tmnxMobServApPolicyId = _TmnxMobServApPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 11, 1, 1),
    _TmnxMobServApPolicyId_Type()
)
tmnxMobServApPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServApPolicyId.setStatus("current")
_TmnxMobServApRowStatus_Type = RowStatus
_TmnxMobServApRowStatus_Object = MibTableColumn
tmnxMobServApRowStatus = _TmnxMobServApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 11, 1, 2),
    _TmnxMobServApRowStatus_Type()
)
tmnxMobServApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApRowStatus.setStatus("current")
_TmnxMobServApLastChanged_Type = TimeStamp
_TmnxMobServApLastChanged_Object = MibTableColumn
tmnxMobServApLastChanged = _TmnxMobServApLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 11, 1, 3),
    _TmnxMobServApLastChanged_Type()
)
tmnxMobServApLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServApLastChanged.setStatus("current")


class _TmnxMobServApCollectAcctStats_Type(TruthValue):
    """Custom type tmnxMobServApCollectAcctStats based on TruthValue"""
    defaultValue = 2


_TmnxMobServApCollectAcctStats_Type.__name__ = "TruthValue"
_TmnxMobServApCollectAcctStats_Object = MibTableColumn
tmnxMobServApCollectAcctStats = _TmnxMobServApCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 11, 1, 4),
    _TmnxMobServApCollectAcctStats_Type()
)
tmnxMobServApCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServApCollectAcctStats.setStatus("current")
_TmnxMobServGaTable_Object = MibTable
tmnxMobServGaTable = _TmnxMobServGaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxMobServGaTable.setStatus("current")
_TmnxMobServGaEntry_Object = MibTableRow
tmnxMobServGaEntry = _TmnxMobServGaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 14, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServGaEntry.setStatus("current")
_TmnxMobServGaLastChanged_Type = TimeStamp
_TmnxMobServGaLastChanged_Object = MibTableColumn
tmnxMobServGaLastChanged = _TmnxMobServGaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 14, 1, 1),
    _TmnxMobServGaLastChanged_Type()
)
tmnxMobServGaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGaLastChanged.setStatus("current")


class _TmnxMobServGaIfVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxMobServGaIfVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxMobServGaIfVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxMobServGaIfVRtrId_Object = MibTableColumn
tmnxMobServGaIfVRtrId = _TmnxMobServGaIfVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 14, 1, 2),
    _TmnxMobServGaIfVRtrId_Type()
)
tmnxMobServGaIfVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGaIfVRtrId.setStatus("current")


class _TmnxMobServGaIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxMobServGaIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxMobServGaIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxMobServGaIfIndex_Object = MibTableColumn
tmnxMobServGaIfIndex = _TmnxMobServGaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 14, 1, 3),
    _TmnxMobServGaIfIndex_Type()
)
tmnxMobServGaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGaIfIndex.setStatus("current")


class _TmnxMobServGaGtpcProfile_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServGaGtpcProfile based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServGaGtpcProfile_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServGaGtpcProfile_Object = MibTableColumn
tmnxMobServGaGtpcProfile = _TmnxMobServGaGtpcProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 14, 1, 4),
    _TmnxMobServGaGtpcProfile_Type()
)
tmnxMobServGaGtpcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGaGtpcProfile.setStatus("current")


class _TmnxMobServGaGtpPrimeGrpName_Type(TmnxMobProfNameOrEmpty):
    """Custom type tmnxMobServGaGtpPrimeGrpName based on TmnxMobProfNameOrEmpty"""
    defaultHexValue = ""


_TmnxMobServGaGtpPrimeGrpName_Type.__name__ = "TmnxMobProfNameOrEmpty"
_TmnxMobServGaGtpPrimeGrpName_Object = MibTableColumn
tmnxMobServGaGtpPrimeGrpName = _TmnxMobServGaGtpPrimeGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 1, 14, 1, 5),
    _TmnxMobServGaGtpPrimeGrpName_Type()
)
tmnxMobServGaGtpPrimeGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxMobServGaGtpPrimeGrpName.setStatus("current")
_TmnxMobServingStatObjs_ObjectIdentity = ObjectIdentity
tmnxMobServingStatObjs = _TmnxMobServingStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2)
)
_TmnxMobServStatTable_Object = MibTable
tmnxMobServStatTable = _TmnxMobServStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServStatTable.setStatus("current")
_TmnxMobServStatEntry_Object = MibTableRow
tmnxMobServStatEntry = _TmnxMobServStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1)
)
tmnxMobServStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobServStatEntry.setStatus("current")
_TmnxMobServCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxMobServCardSlotNum_Object = MibTableColumn
tmnxMobServCardSlotNum = _TmnxMobServCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 1),
    _TmnxMobServCardSlotNum_Type()
)
tmnxMobServCardSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServCardSlotNum.setStatus("current")
_TmnxMobServStatApn_Type = Gauge32
_TmnxMobServStatApn_Object = MibTableColumn
tmnxMobServStatApn = _TmnxMobServStatApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 2),
    _TmnxMobServStatApn_Type()
)
tmnxMobServStatApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatApn.setStatus("current")
_TmnxMobServStatBearers_Type = Gauge32
_TmnxMobServStatBearers_Object = MibTableColumn
tmnxMobServStatBearers = _TmnxMobServStatBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 3),
    _TmnxMobServStatBearers_Type()
)
tmnxMobServStatBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatBearers.setStatus("current")
_TmnxMobServStatDefaultBearers_Type = Gauge32
_TmnxMobServStatDefaultBearers_Object = MibTableColumn
tmnxMobServStatDefaultBearers = _TmnxMobServStatDefaultBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 4),
    _TmnxMobServStatDefaultBearers_Type()
)
tmnxMobServStatDefaultBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatDefaultBearers.setStatus("current")
_TmnxMobServStatDedicatedBearers_Type = Gauge32
_TmnxMobServStatDedicatedBearers_Object = MibTableColumn
tmnxMobServStatDedicatedBearers = _TmnxMobServStatDedicatedBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 5),
    _TmnxMobServStatDedicatedBearers_Type()
)
tmnxMobServStatDedicatedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatDedicatedBearers.setStatus("current")
_TmnxMobServStatIpv4Bearers_Type = Gauge32
_TmnxMobServStatIpv4Bearers_Object = MibTableColumn
tmnxMobServStatIpv4Bearers = _TmnxMobServStatIpv4Bearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 6),
    _TmnxMobServStatIpv4Bearers_Type()
)
tmnxMobServStatIpv4Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatIpv4Bearers.setStatus("current")
_TmnxMobServStatIpv6Bearers_Type = Gauge32
_TmnxMobServStatIpv6Bearers_Object = MibTableColumn
tmnxMobServStatIpv6Bearers = _TmnxMobServStatIpv6Bearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 7),
    _TmnxMobServStatIpv6Bearers_Type()
)
tmnxMobServStatIpv6Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatIpv6Bearers.setStatus("current")
_TmnxMobServStatIpv4v6Bearers_Type = Gauge32
_TmnxMobServStatIpv4v6Bearers_Object = MibTableColumn
tmnxMobServStatIpv4v6Bearers = _TmnxMobServStatIpv4v6Bearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 8),
    _TmnxMobServStatIpv4v6Bearers_Type()
)
tmnxMobServStatIpv4v6Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatIpv4v6Bearers.setStatus("current")
_TmnxMobServStatActiveBearers_Type = Gauge32
_TmnxMobServStatActiveBearers_Object = MibTableColumn
tmnxMobServStatActiveBearers = _TmnxMobServStatActiveBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 9),
    _TmnxMobServStatActiveBearers_Type()
)
tmnxMobServStatActiveBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatActiveBearers.setStatus("current")
_TmnxMobServStatIdleBearers_Type = Gauge32
_TmnxMobServStatIdleBearers_Object = MibTableColumn
tmnxMobServStatIdleBearers = _TmnxMobServStatIdleBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 10),
    _TmnxMobServStatIdleBearers_Type()
)
tmnxMobServStatIdleBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatIdleBearers.setStatus("current")
_TmnxMobServStatRoamers_Type = Gauge32
_TmnxMobServStatRoamers_Object = MibTableColumn
tmnxMobServStatRoamers = _TmnxMobServStatRoamers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 11),
    _TmnxMobServStatRoamers_Type()
)
tmnxMobServStatRoamers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatRoamers.setStatus("current")
_TmnxMobServStatPagingInProgress_Type = Gauge32
_TmnxMobServStatPagingInProgress_Object = MibTableColumn
tmnxMobServStatPagingInProgress = _TmnxMobServStatPagingInProgress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 12),
    _TmnxMobServStatPagingInProgress_Type()
)
tmnxMobServStatPagingInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatPagingInProgress.setStatus("current")
_TmnxMobServStatIpv4Sdf_Type = Gauge32
_TmnxMobServStatIpv4Sdf_Object = MibTableColumn
tmnxMobServStatIpv4Sdf = _TmnxMobServStatIpv4Sdf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 13),
    _TmnxMobServStatIpv4Sdf_Type()
)
tmnxMobServStatIpv4Sdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatIpv4Sdf.setStatus("current")
_TmnxMobServStatIpv6Sdf_Type = Gauge32
_TmnxMobServStatIpv6Sdf_Object = MibTableColumn
tmnxMobServStatIpv6Sdf = _TmnxMobServStatIpv6Sdf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 14),
    _TmnxMobServStatIpv6Sdf_Type()
)
tmnxMobServStatIpv6Sdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatIpv6Sdf.setStatus("current")
_TmnxMobServStatBuffersAllocated_Type = Gauge32
_TmnxMobServStatBuffersAllocated_Object = MibTableColumn
tmnxMobServStatBuffersAllocated = _TmnxMobServStatBuffersAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 15),
    _TmnxMobServStatBuffersAllocated_Type()
)
tmnxMobServStatBuffersAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatBuffersAllocated.setStatus("current")
_TmnxMobServStatBuffersAvailable_Type = Gauge32
_TmnxMobServStatBuffersAvailable_Object = MibTableColumn
tmnxMobServStatBuffersAvailable = _TmnxMobServStatBuffersAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 16),
    _TmnxMobServStatBuffersAvailable_Type()
)
tmnxMobServStatBuffersAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatBuffersAvailable.setStatus("current")
_TmnxMobServStatBuffersAllocErr_Type = Gauge32
_TmnxMobServStatBuffersAllocErr_Object = MibTableColumn
tmnxMobServStatBuffersAllocErr = _TmnxMobServStatBuffersAllocErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 17),
    _TmnxMobServStatBuffersAllocErr_Type()
)
tmnxMobServStatBuffersAllocErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatBuffersAllocErr.setStatus("current")
_TmnxMobServStatHomers_Type = Gauge32
_TmnxMobServStatHomers_Object = MibTableColumn
tmnxMobServStatHomers = _TmnxMobServStatHomers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 18),
    _TmnxMobServStatHomers_Type()
)
tmnxMobServStatHomers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatHomers.setStatus("current")
_TmnxMobServStatVisitors_Type = Gauge32
_TmnxMobServStatVisitors_Object = MibTableColumn
tmnxMobServStatVisitors = _TmnxMobServStatVisitors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 19),
    _TmnxMobServStatVisitors_Type()
)
tmnxMobServStatVisitors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatVisitors.setStatus("current")
_TmnxMobServStatENBs_Type = Gauge32
_TmnxMobServStatENBs_Object = MibTableColumn
tmnxMobServStatENBs = _TmnxMobServStatENBs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 20),
    _TmnxMobServStatENBs_Type()
)
tmnxMobServStatENBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatENBs.setStatus("current")
_TmnxMobServStatMmes_Type = Gauge32
_TmnxMobServStatMmes_Object = MibTableColumn
tmnxMobServStatMmes = _TmnxMobServStatMmes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 21),
    _TmnxMobServStatMmes_Type()
)
tmnxMobServStatMmes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatMmes.setStatus("current")
_TmnxMobServStatPgws_Type = Gauge32
_TmnxMobServStatPgws_Object = MibTableColumn
tmnxMobServStatPgws = _TmnxMobServStatPgws_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 22),
    _TmnxMobServStatPgws_Type()
)
tmnxMobServStatPgws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatPgws.setStatus("current")
_TmnxMobServStatUes_Type = Gauge32
_TmnxMobServStatUes_Object = MibTableColumn
tmnxMobServStatUes = _TmnxMobServStatUes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 23),
    _TmnxMobServStatUes_Type()
)
tmnxMobServStatUes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatUes.setStatus("current")
_TmnxMobServStatRfPeer_Type = Gauge32
_TmnxMobServStatRfPeer_Object = MibTableColumn
tmnxMobServStatRfPeer = _TmnxMobServStatRfPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 24),
    _TmnxMobServStatRfPeer_Type()
)
tmnxMobServStatRfPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatRfPeer.setStatus("current")
_TmnxMobServStatRfAcctStartBuf_Type = Gauge32
_TmnxMobServStatRfAcctStartBuf_Object = MibTableColumn
tmnxMobServStatRfAcctStartBuf = _TmnxMobServStatRfAcctStartBuf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 25),
    _TmnxMobServStatRfAcctStartBuf_Type()
)
tmnxMobServStatRfAcctStartBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatRfAcctStartBuf.setStatus("current")
_TmnxMobServStatRfAcctIntBuf_Type = Gauge32
_TmnxMobServStatRfAcctIntBuf_Object = MibTableColumn
tmnxMobServStatRfAcctIntBuf = _TmnxMobServStatRfAcctIntBuf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 26),
    _TmnxMobServStatRfAcctIntBuf_Type()
)
tmnxMobServStatRfAcctIntBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatRfAcctIntBuf.setStatus("current")
_TmnxMobServStatRfAcctStopBuf_Type = Gauge32
_TmnxMobServStatRfAcctStopBuf_Object = MibTableColumn
tmnxMobServStatRfAcctStopBuf = _TmnxMobServStatRfAcctStopBuf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 27),
    _TmnxMobServStatRfAcctStopBuf_Type()
)
tmnxMobServStatRfAcctStopBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatRfAcctStopBuf.setStatus("current")
_TmnxMobServStatIdleUes_Type = Gauge32
_TmnxMobServStatIdleUes_Object = MibTableColumn
tmnxMobServStatIdleUes = _TmnxMobServStatIdleUes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 28),
    _TmnxMobServStatIdleUes_Type()
)
tmnxMobServStatIdleUes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatIdleUes.setStatus("current")
_TmnxMobServStatNumSuspendedUE_Type = Gauge32
_TmnxMobServStatNumSuspendedUE_Object = MibTableColumn
tmnxMobServStatNumSuspendedUE = _TmnxMobServStatNumSuspendedUE_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 29),
    _TmnxMobServStatNumSuspendedUE_Type()
)
tmnxMobServStatNumSuspendedUE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatNumSuspendedUE.setStatus("current")
_TmnxMobServStatEmergencyPdnSess_Type = Gauge32
_TmnxMobServStatEmergencyPdnSess_Object = MibTableColumn
tmnxMobServStatEmergencyPdnSess = _TmnxMobServStatEmergencyPdnSess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 30),
    _TmnxMobServStatEmergencyPdnSess_Type()
)
tmnxMobServStatEmergencyPdnSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatEmergencyPdnSess.setStatus("current")
_TmnxMobServStatPagingDrops_Type = Gauge32
_TmnxMobServStatPagingDrops_Object = MibTableColumn
tmnxMobServStatPagingDrops = _TmnxMobServStatPagingDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 1, 1, 31),
    _TmnxMobServStatPagingDrops_Type()
)
tmnxMobServStatPagingDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServStatPagingDrops.setStatus("current")
_TmnxMobServProcsTable_Object = MibTable
tmnxMobServProcsTable = _TmnxMobServProcsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxMobServProcsTable.setStatus("current")
_TmnxMobServProcsEntry_Object = MibTableRow
tmnxMobServProcsEntry = _TmnxMobServProcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServProcsEntry.setStatus("current")
_TmnxMobServProcAttach_Type = Counter32
_TmnxMobServProcAttach_Object = MibTableColumn
tmnxMobServProcAttach = _TmnxMobServProcAttach_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 1),
    _TmnxMobServProcAttach_Type()
)
tmnxMobServProcAttach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcAttach.setStatus("current")
_TmnxMobServProcDetach_Type = Counter32
_TmnxMobServProcDetach_Object = MibTableColumn
tmnxMobServProcDetach = _TmnxMobServProcDetach_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 2),
    _TmnxMobServProcDetach_Type()
)
tmnxMobServProcDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcDetach.setStatus("current")
_TmnxMobServProcNwServiceReq_Type = Counter32
_TmnxMobServProcNwServiceReq_Object = MibTableColumn
tmnxMobServProcNwServiceReq = _TmnxMobServProcNwServiceReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 3),
    _TmnxMobServProcNwServiceReq_Type()
)
tmnxMobServProcNwServiceReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwServiceReq.setStatus("obsolete")
_TmnxMobServProcUeServiceReq_Type = Counter32
_TmnxMobServProcUeServiceReq_Object = MibTableColumn
tmnxMobServProcUeServiceReq = _TmnxMobServProcUeServiceReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 4),
    _TmnxMobServProcUeServiceReq_Type()
)
tmnxMobServProcUeServiceReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcUeServiceReq.setStatus("current")
_TmnxMobServProcS1Release_Type = Counter32
_TmnxMobServProcS1Release_Object = MibTableColumn
tmnxMobServProcS1Release = _TmnxMobServProcS1Release_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 5),
    _TmnxMobServProcS1Release_Type()
)
tmnxMobServProcS1Release.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcS1Release.setStatus("current")
_TmnxMobServProcInterENBX2Hndovr_Type = Counter32
_TmnxMobServProcInterENBX2Hndovr_Object = MibTableColumn
tmnxMobServProcInterENBX2Hndovr = _TmnxMobServProcInterENBX2Hndovr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 6),
    _TmnxMobServProcInterENBX2Hndovr_Type()
)
tmnxMobServProcInterENBX2Hndovr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterENBX2Hndovr.setStatus("obsolete")
_TmnxMobServProcInterENBS1Hndovr_Type = Counter32
_TmnxMobServProcInterENBS1Hndovr_Object = MibTableColumn
tmnxMobServProcInterENBS1Hndovr = _TmnxMobServProcInterENBS1Hndovr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 7),
    _TmnxMobServProcInterENBS1Hndovr_Type()
)
tmnxMobServProcInterENBS1Hndovr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterENBS1Hndovr.setStatus("obsolete")
_TmnxMobServProcUeDedBrActivation_Type = Counter32
_TmnxMobServProcUeDedBrActivation_Object = MibTableColumn
tmnxMobServProcUeDedBrActivation = _TmnxMobServProcUeDedBrActivation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 8),
    _TmnxMobServProcUeDedBrActivation_Type()
)
tmnxMobServProcUeDedBrActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcUeDedBrActivation.setStatus("current")
_TmnxMobServProcNwDedBrActivtn_Type = Counter32
_TmnxMobServProcNwDedBrActivtn_Object = MibTableColumn
tmnxMobServProcNwDedBrActivtn = _TmnxMobServProcNwDedBrActivtn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 9),
    _TmnxMobServProcNwDedBrActivtn_Type()
)
tmnxMobServProcNwDedBrActivtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwDedBrActivtn.setStatus("current")
_TmnxMobServProcNwDedBrDeActiv_Type = Counter32
_TmnxMobServProcNwDedBrDeActiv_Object = MibTableColumn
tmnxMobServProcNwDedBrDeActiv = _TmnxMobServProcNwDedBrDeActiv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 10),
    _TmnxMobServProcNwDedBrDeActiv_Type()
)
tmnxMobServProcNwDedBrDeActiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwDedBrDeActiv.setStatus("current")
_TmnxMobServProcMmeDedBrDeActiv_Type = Counter32
_TmnxMobServProcMmeDedBrDeActiv_Object = MibTableColumn
tmnxMobServProcMmeDedBrDeActiv = _TmnxMobServProcMmeDedBrDeActiv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 11),
    _TmnxMobServProcMmeDedBrDeActiv_Type()
)
tmnxMobServProcMmeDedBrDeActiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcMmeDedBrDeActiv.setStatus("current")
_TmnxMobServProcHssQosModificatn_Type = Counter32
_TmnxMobServProcHssQosModificatn_Object = MibTableColumn
tmnxMobServProcHssQosModificatn = _TmnxMobServProcHssQosModificatn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 12),
    _TmnxMobServProcHssQosModificatn_Type()
)
tmnxMobServProcHssQosModificatn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcHssQosModificatn.setStatus("current")
_TmnxMobServProcAttachFailures_Type = Counter32
_TmnxMobServProcAttachFailures_Object = MibTableColumn
tmnxMobServProcAttachFailures = _TmnxMobServProcAttachFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 13),
    _TmnxMobServProcAttachFailures_Type()
)
tmnxMobServProcAttachFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcAttachFailures.setStatus("current")
_TmnxMobServProcDetachFailures_Type = Counter32
_TmnxMobServProcDetachFailures_Object = MibTableColumn
tmnxMobServProcDetachFailures = _TmnxMobServProcDetachFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 14),
    _TmnxMobServProcDetachFailures_Type()
)
tmnxMobServProcDetachFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcDetachFailures.setStatus("current")
_TmnxMobServProcNwServiceReqFails_Type = Counter32
_TmnxMobServProcNwServiceReqFails_Object = MibTableColumn
tmnxMobServProcNwServiceReqFails = _TmnxMobServProcNwServiceReqFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 15),
    _TmnxMobServProcNwServiceReqFails_Type()
)
tmnxMobServProcNwServiceReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwServiceReqFails.setStatus("obsolete")
_TmnxMobServProcUeServiceReqFails_Type = Counter32
_TmnxMobServProcUeServiceReqFails_Object = MibTableColumn
tmnxMobServProcUeServiceReqFails = _TmnxMobServProcUeServiceReqFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 16),
    _TmnxMobServProcUeServiceReqFails_Type()
)
tmnxMobServProcUeServiceReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcUeServiceReqFails.setStatus("current")
_TmnxMobServProcS1ReleaseFailures_Type = Counter32
_TmnxMobServProcS1ReleaseFailures_Object = MibTableColumn
tmnxMobServProcS1ReleaseFailures = _TmnxMobServProcS1ReleaseFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 17),
    _TmnxMobServProcS1ReleaseFailures_Type()
)
tmnxMobServProcS1ReleaseFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcS1ReleaseFailures.setStatus("current")
_TmnxMobServProcEnbX2HndovrFails_Type = Counter32
_TmnxMobServProcEnbX2HndovrFails_Object = MibTableColumn
tmnxMobServProcEnbX2HndovrFails = _TmnxMobServProcEnbX2HndovrFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 18),
    _TmnxMobServProcEnbX2HndovrFails_Type()
)
tmnxMobServProcEnbX2HndovrFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcEnbX2HndovrFails.setStatus("obsolete")
_TmnxMobServProcEnbS1HndovrFails_Type = Counter32
_TmnxMobServProcEnbS1HndovrFails_Object = MibTableColumn
tmnxMobServProcEnbS1HndovrFails = _TmnxMobServProcEnbS1HndovrFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 19),
    _TmnxMobServProcEnbS1HndovrFails_Type()
)
tmnxMobServProcEnbS1HndovrFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcEnbS1HndovrFails.setStatus("obsolete")
_TmnxMobServProcUeDedBrActvFails_Type = Counter32
_TmnxMobServProcUeDedBrActvFails_Object = MibTableColumn
tmnxMobServProcUeDedBrActvFails = _TmnxMobServProcUeDedBrActvFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 20),
    _TmnxMobServProcUeDedBrActvFails_Type()
)
tmnxMobServProcUeDedBrActvFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcUeDedBrActvFails.setStatus("current")
_TmnxMobServProcNwDedBrActvFails_Type = Counter32
_TmnxMobServProcNwDedBrActvFails_Object = MibTableColumn
tmnxMobServProcNwDedBrActvFails = _TmnxMobServProcNwDedBrActvFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 21),
    _TmnxMobServProcNwDedBrActvFails_Type()
)
tmnxMobServProcNwDedBrActvFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwDedBrActvFails.setStatus("current")
_TmnxMobServProcNwDedBrDeActFails_Type = Counter32
_TmnxMobServProcNwDedBrDeActFails_Object = MibTableColumn
tmnxMobServProcNwDedBrDeActFails = _TmnxMobServProcNwDedBrDeActFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 22),
    _TmnxMobServProcNwDedBrDeActFails_Type()
)
tmnxMobServProcNwDedBrDeActFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwDedBrDeActFails.setStatus("current")
_TmnxMobServProcMmeDedBrDeAcFails_Type = Counter32
_TmnxMobServProcMmeDedBrDeAcFails_Object = MibTableColumn
tmnxMobServProcMmeDedBrDeAcFails = _TmnxMobServProcMmeDedBrDeAcFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 23),
    _TmnxMobServProcMmeDedBrDeAcFails_Type()
)
tmnxMobServProcMmeDedBrDeAcFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcMmeDedBrDeAcFails.setStatus("current")
_TmnxMobServProcHssQosModifyFails_Type = Counter32
_TmnxMobServProcHssQosModifyFails_Object = MibTableColumn
tmnxMobServProcHssQosModifyFails = _TmnxMobServProcHssQosModifyFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 24),
    _TmnxMobServProcHssQosModifyFails_Type()
)
tmnxMobServProcHssQosModifyFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcHssQosModifyFails.setStatus("current")
_TmnxMobServProcPagingTimeoutExp_Type = Counter32
_TmnxMobServProcPagingTimeoutExp_Object = MibTableColumn
tmnxMobServProcPagingTimeoutExp = _TmnxMobServProcPagingTimeoutExp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 25),
    _TmnxMobServProcPagingTimeoutExp_Type()
)
tmnxMobServProcPagingTimeoutExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcPagingTimeoutExp.setStatus("current")
_TmnxMobServProcIntraIdleModeTau_Type = Counter32
_TmnxMobServProcIntraIdleModeTau_Object = MibTableColumn
tmnxMobServProcIntraIdleModeTau = _TmnxMobServProcIntraIdleModeTau_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 26),
    _TmnxMobServProcIntraIdleModeTau_Type()
)
tmnxMobServProcIntraIdleModeTau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcIntraIdleModeTau.setStatus("current")
_TmnxMobServProcInterMmeRel_Type = Counter32
_TmnxMobServProcInterMmeRel_Object = MibTableColumn
tmnxMobServProcInterMmeRel = _TmnxMobServProcInterMmeRel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 27),
    _TmnxMobServProcInterMmeRel_Type()
)
tmnxMobServProcInterMmeRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeRel.setStatus("obsolete")
_TmnxMobServProcInterMmeRelFails_Type = Counter32
_TmnxMobServProcInterMmeRelFails_Object = MibTableColumn
tmnxMobServProcInterMmeRelFails = _TmnxMobServProcInterMmeRelFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 28),
    _TmnxMobServProcInterMmeRelFails_Type()
)
tmnxMobServProcInterMmeRelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeRelFails.setStatus("obsolete")
_TmnxMobServProcInterIdleTau_Type = Counter32
_TmnxMobServProcInterIdleTau_Object = MibTableColumn
tmnxMobServProcInterIdleTau = _TmnxMobServProcInterIdleTau_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 29),
    _TmnxMobServProcInterIdleTau_Type()
)
tmnxMobServProcInterIdleTau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterIdleTau.setStatus("current")
_TmnxMobServProcInterIdleTauFails_Type = Counter32
_TmnxMobServProcInterIdleTauFails_Object = MibTableColumn
tmnxMobServProcInterIdleTauFails = _TmnxMobServProcInterIdleTauFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 30),
    _TmnxMobServProcInterIdleTauFails_Type()
)
tmnxMobServProcInterIdleTauFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterIdleTauFails.setStatus("current")
_TmnxMobServProcS1WithIndTnl_Type = Counter32
_TmnxMobServProcS1WithIndTnl_Object = MibTableColumn
tmnxMobServProcS1WithIndTnl = _TmnxMobServProcS1WithIndTnl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 31),
    _TmnxMobServProcS1WithIndTnl_Type()
)
tmnxMobServProcS1WithIndTnl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcS1WithIndTnl.setStatus("current")
_TmnxMobServProcS1WithIndTnlFails_Type = Counter32
_TmnxMobServProcS1WithIndTnlFails_Object = MibTableColumn
tmnxMobServProcS1WithIndTnlFails = _TmnxMobServProcS1WithIndTnlFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 32),
    _TmnxMobServProcS1WithIndTnlFails_Type()
)
tmnxMobServProcS1WithIndTnlFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcS1WithIndTnlFails.setStatus("current")
_TmnxMobServProcS1WoIndTnl_Type = Counter32
_TmnxMobServProcS1WoIndTnl_Object = MibTableColumn
tmnxMobServProcS1WoIndTnl = _TmnxMobServProcS1WoIndTnl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 33),
    _TmnxMobServProcS1WoIndTnl_Type()
)
tmnxMobServProcS1WoIndTnl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcS1WoIndTnl.setStatus("current")
_TmnxMobServProcS1WoIndTnlFails_Type = Counter32
_TmnxMobServProcS1WoIndTnlFails_Object = MibTableColumn
tmnxMobServProcS1WoIndTnlFails = _TmnxMobServProcS1WoIndTnlFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 34),
    _TmnxMobServProcS1WoIndTnlFails_Type()
)
tmnxMobServProcS1WoIndTnlFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcS1WoIndTnlFails.setStatus("current")
_TmnxMobServProcInterX2Hndor_Type = Counter32
_TmnxMobServProcInterX2Hndor_Object = MibTableColumn
tmnxMobServProcInterX2Hndor = _TmnxMobServProcInterX2Hndor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 35),
    _TmnxMobServProcInterX2Hndor_Type()
)
tmnxMobServProcInterX2Hndor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterX2Hndor.setStatus("current")
_TmnxMobServProcInterX2HndorFails_Type = Counter32
_TmnxMobServProcInterX2HndorFails_Object = MibTableColumn
tmnxMobServProcInterX2HndorFails = _TmnxMobServProcInterX2HndorFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 36),
    _TmnxMobServProcInterX2HndorFails_Type()
)
tmnxMobServProcInterX2HndorFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterX2HndorFails.setStatus("current")
_TmnxMobServProcInterSgwHoOut_Type = Counter32
_TmnxMobServProcInterSgwHoOut_Object = MibTableColumn
tmnxMobServProcInterSgwHoOut = _TmnxMobServProcInterSgwHoOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 37),
    _TmnxMobServProcInterSgwHoOut_Type()
)
tmnxMobServProcInterSgwHoOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterSgwHoOut.setStatus("current")
_TmnxMobServProcMltPdnConcvtReqs_Type = Counter32
_TmnxMobServProcMltPdnConcvtReqs_Object = MibTableColumn
tmnxMobServProcMltPdnConcvtReqs = _TmnxMobServProcMltPdnConcvtReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 38),
    _TmnxMobServProcMltPdnConcvtReqs_Type()
)
tmnxMobServProcMltPdnConcvtReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcMltPdnConcvtReqs.setStatus("obsolete")
_TmnxMobServProcMltPdnConcvtFails_Type = Counter32
_TmnxMobServProcMltPdnConcvtFails_Object = MibTableColumn
tmnxMobServProcMltPdnConcvtFails = _TmnxMobServProcMltPdnConcvtFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 39),
    _TmnxMobServProcMltPdnConcvtFails_Type()
)
tmnxMobServProcMltPdnConcvtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcMltPdnConcvtFails.setStatus("obsolete")
_TmnxMobServProcModBearers_Type = Counter32
_TmnxMobServProcModBearers_Object = MibTableColumn
tmnxMobServProcModBearers = _TmnxMobServProcModBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 40),
    _TmnxMobServProcModBearers_Type()
)
tmnxMobServProcModBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcModBearers.setStatus("obsolete")
_TmnxMobServProcModBearersFails_Type = Counter32
_TmnxMobServProcModBearersFails_Object = MibTableColumn
tmnxMobServProcModBearersFails = _TmnxMobServProcModBearersFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 41),
    _TmnxMobServProcModBearersFails_Type()
)
tmnxMobServProcModBearersFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcModBearersFails.setStatus("obsolete")
_TmnxMobServProcDelBearers_Type = Counter32
_TmnxMobServProcDelBearers_Object = MibTableColumn
tmnxMobServProcDelBearers = _TmnxMobServProcDelBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 42),
    _TmnxMobServProcDelBearers_Type()
)
tmnxMobServProcDelBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcDelBearers.setStatus("obsolete")
_TmnxMobServProcDelBearersFails_Type = Counter32
_TmnxMobServProcDelBearersFails_Object = MibTableColumn
tmnxMobServProcDelBearersFails = _TmnxMobServProcDelBearersFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 43),
    _TmnxMobServProcDelBearersFails_Type()
)
tmnxMobServProcDelBearersFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcDelBearersFails.setStatus("obsolete")
_TmnxMobServProcBearerRes_Type = Counter32
_TmnxMobServProcBearerRes_Object = MibTableColumn
tmnxMobServProcBearerRes = _TmnxMobServProcBearerRes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 44),
    _TmnxMobServProcBearerRes_Type()
)
tmnxMobServProcBearerRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcBearerRes.setStatus("obsolete")
_TmnxMobServProcBearerResFails_Type = Counter32
_TmnxMobServProcBearerResFails_Object = MibTableColumn
tmnxMobServProcBearerResFails = _TmnxMobServProcBearerResFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 45),
    _TmnxMobServProcBearerResFails_Type()
)
tmnxMobServProcBearerResFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcBearerResFails.setStatus("obsolete")
_TmnxMobServProcEhrpdLteHo_Type = Counter32
_TmnxMobServProcEhrpdLteHo_Object = MibTableColumn
tmnxMobServProcEhrpdLteHo = _TmnxMobServProcEhrpdLteHo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 46),
    _TmnxMobServProcEhrpdLteHo_Type()
)
tmnxMobServProcEhrpdLteHo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcEhrpdLteHo.setStatus("current")
_TmnxMobServProcEhrpdLteHoFails_Type = Counter32
_TmnxMobServProcEhrpdLteHoFails_Object = MibTableColumn
tmnxMobServProcEhrpdLteHoFails = _TmnxMobServProcEhrpdLteHoFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 47),
    _TmnxMobServProcEhrpdLteHoFails_Type()
)
tmnxMobServProcEhrpdLteHoFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcEhrpdLteHoFails.setStatus("current")
_TmnxMobServProcIntraIdleTauFails_Type = Counter32
_TmnxMobServProcIntraIdleTauFails_Object = MibTableColumn
tmnxMobServProcIntraIdleTauFails = _TmnxMobServProcIntraIdleTauFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 48),
    _TmnxMobServProcIntraIdleTauFails_Type()
)
tmnxMobServProcIntraIdleTauFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcIntraIdleTauFails.setStatus("current")
_TmnxMobServProcNwPdnSessDeActiv_Type = Counter32
_TmnxMobServProcNwPdnSessDeActiv_Object = MibTableColumn
tmnxMobServProcNwPdnSessDeActiv = _TmnxMobServProcNwPdnSessDeActiv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 49),
    _TmnxMobServProcNwPdnSessDeActiv_Type()
)
tmnxMobServProcNwPdnSessDeActiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwPdnSessDeActiv.setStatus("current")
_TmnxMobServProcNwPdnSesDeActFail_Type = Counter32
_TmnxMobServProcNwPdnSesDeActFail_Object = MibTableColumn
tmnxMobServProcNwPdnSesDeActFail = _TmnxMobServProcNwPdnSesDeActFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 50),
    _TmnxMobServProcNwPdnSesDeActFail_Type()
)
tmnxMobServProcNwPdnSesDeActFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwPdnSesDeActFail.setStatus("current")
_TmnxMobServProcPagingAttempts_Type = Counter32
_TmnxMobServProcPagingAttempts_Object = MibTableColumn
tmnxMobServProcPagingAttempts = _TmnxMobServProcPagingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 51),
    _TmnxMobServProcPagingAttempts_Type()
)
tmnxMobServProcPagingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcPagingAttempts.setStatus("current")
_TmnxMobServProcPagingFails_Type = Counter32
_TmnxMobServProcPagingFails_Object = MibTableColumn
tmnxMobServProcPagingFails = _TmnxMobServProcPagingFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 52),
    _TmnxMobServProcPagingFails_Type()
)
tmnxMobServProcPagingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcPagingFails.setStatus("current")
_TmnxMobServProcIntraSgwHndvr_Type = Counter32
_TmnxMobServProcIntraSgwHndvr_Object = MibTableColumn
tmnxMobServProcIntraSgwHndvr = _TmnxMobServProcIntraSgwHndvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 53),
    _TmnxMobServProcIntraSgwHndvr_Type()
)
tmnxMobServProcIntraSgwHndvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcIntraSgwHndvr.setStatus("current")
_TmnxMobServProcIntraSgwHndvrFail_Type = Counter32
_TmnxMobServProcIntraSgwHndvrFail_Object = MibTableColumn
tmnxMobServProcIntraSgwHndvrFail = _TmnxMobServProcIntraSgwHndvrFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 54),
    _TmnxMobServProcIntraSgwHndvrFail_Type()
)
tmnxMobServProcIntraSgwHndvrFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcIntraSgwHndvrFail.setStatus("current")
_TmnxMobServProcIntraSgwS1IndTnl_Type = Counter32
_TmnxMobServProcIntraSgwS1IndTnl_Object = MibTableColumn
tmnxMobServProcIntraSgwS1IndTnl = _TmnxMobServProcIntraSgwS1IndTnl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 55),
    _TmnxMobServProcIntraSgwS1IndTnl_Type()
)
tmnxMobServProcIntraSgwS1IndTnl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcIntraSgwS1IndTnl.setStatus("current")
_TmnxMobServProcIntraS1IndTnlFail_Type = Counter32
_TmnxMobServProcIntraS1IndTnlFail_Object = MibTableColumn
tmnxMobServProcIntraS1IndTnlFail = _TmnxMobServProcIntraS1IndTnlFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 56),
    _TmnxMobServProcIntraS1IndTnlFail_Type()
)
tmnxMobServProcIntraS1IndTnlFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcIntraS1IndTnlFail.setStatus("current")
_TmnxMobServProcInterMmeIdleTau_Type = Counter32
_TmnxMobServProcInterMmeIdleTau_Object = MibTableColumn
tmnxMobServProcInterMmeIdleTau = _TmnxMobServProcInterMmeIdleTau_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 57),
    _TmnxMobServProcInterMmeIdleTau_Type()
)
tmnxMobServProcInterMmeIdleTau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeIdleTau.setStatus("current")
_TmnxMobServProcInterMmeIdlTauFls_Type = Counter32
_TmnxMobServProcInterMmeIdlTauFls_Object = MibTableColumn
tmnxMobServProcInterMmeIdlTauFls = _TmnxMobServProcInterMmeIdlTauFls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 58),
    _TmnxMobServProcInterMmeIdlTauFls_Type()
)
tmnxMobServProcInterMmeIdlTauFls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeIdlTauFls.setStatus("current")
_TmnxMobServProcInterMmeS1X2RlSuc_Type = Counter32
_TmnxMobServProcInterMmeS1X2RlSuc_Object = MibTableColumn
tmnxMobServProcInterMmeS1X2RlSuc = _TmnxMobServProcInterMmeS1X2RlSuc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 59),
    _TmnxMobServProcInterMmeS1X2RlSuc_Type()
)
tmnxMobServProcInterMmeS1X2RlSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeS1X2RlSuc.setStatus("current")
_TmnxMobServProcInterMmeS1X2RlFls_Type = Counter32
_TmnxMobServProcInterMmeS1X2RlFls_Object = MibTableColumn
tmnxMobServProcInterMmeS1X2RlFls = _TmnxMobServProcInterMmeS1X2RlFls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 60),
    _TmnxMobServProcInterMmeS1X2RlFls_Type()
)
tmnxMobServProcInterMmeS1X2RlFls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeS1X2RlFls.setStatus("current")
_TmnxMobServProcInterMmeS1RlTnSuc_Type = Counter32
_TmnxMobServProcInterMmeS1RlTnSuc_Object = MibTableColumn
tmnxMobServProcInterMmeS1RlTnSuc = _TmnxMobServProcInterMmeS1RlTnSuc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 61),
    _TmnxMobServProcInterMmeS1RlTnSuc_Type()
)
tmnxMobServProcInterMmeS1RlTnSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeS1RlTnSuc.setStatus("current")
_TmnxMobServProcInterMmeS1RlTnFls_Type = Counter32
_TmnxMobServProcInterMmeS1RlTnFls_Object = MibTableColumn
tmnxMobServProcInterMmeS1RlTnFls = _TmnxMobServProcInterMmeS1RlTnFls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 62),
    _TmnxMobServProcInterMmeS1RlTnFls_Type()
)
tmnxMobServProcInterMmeS1RlTnFls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeS1RlTnFls.setStatus("current")
_TmnxMobServProcInterMmeRelocs_Type = Counter32
_TmnxMobServProcInterMmeRelocs_Object = MibTableColumn
tmnxMobServProcInterMmeRelocs = _TmnxMobServProcInterMmeRelocs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 63),
    _TmnxMobServProcInterMmeRelocs_Type()
)
tmnxMobServProcInterMmeRelocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcInterMmeRelocs.setStatus("current")
_TmnxMobServProcAttachPiggyBack_Type = Counter32
_TmnxMobServProcAttachPiggyBack_Object = MibTableColumn
tmnxMobServProcAttachPiggyBack = _TmnxMobServProcAttachPiggyBack_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 64),
    _TmnxMobServProcAttachPiggyBack_Type()
)
tmnxMobServProcAttachPiggyBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcAttachPiggyBack.setStatus("current")
_TmnxMobServProcAttachPiggyFail_Type = Counter32
_TmnxMobServProcAttachPiggyFail_Object = MibTableColumn
tmnxMobServProcAttachPiggyFail = _TmnxMobServProcAttachPiggyFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 65),
    _TmnxMobServProcAttachPiggyFail_Type()
)
tmnxMobServProcAttachPiggyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcAttachPiggyFail.setStatus("current")
_TmnxMobServProcUeDedBrDeActv_Type = Counter32
_TmnxMobServProcUeDedBrDeActv_Object = MibTableColumn
tmnxMobServProcUeDedBrDeActv = _TmnxMobServProcUeDedBrDeActv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 66),
    _TmnxMobServProcUeDedBrDeActv_Type()
)
tmnxMobServProcUeDedBrDeActv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcUeDedBrDeActv.setStatus("current")
_TmnxMobServProcUeDedBrDeActvFail_Type = Counter32
_TmnxMobServProcUeDedBrDeActvFail_Object = MibTableColumn
tmnxMobServProcUeDedBrDeActvFail = _TmnxMobServProcUeDedBrDeActvFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 67),
    _TmnxMobServProcUeDedBrDeActvFail_Type()
)
tmnxMobServProcUeDedBrDeActvFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcUeDedBrDeActvFail.setStatus("current")
_TmnxMobServProcUeDedBrModify_Type = Counter32
_TmnxMobServProcUeDedBrModify_Object = MibTableColumn
tmnxMobServProcUeDedBrModify = _TmnxMobServProcUeDedBrModify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 68),
    _TmnxMobServProcUeDedBrModify_Type()
)
tmnxMobServProcUeDedBrModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcUeDedBrModify.setStatus("current")
_TmnxMobServProcUeDedBrModifyFail_Type = Counter32
_TmnxMobServProcUeDedBrModifyFail_Object = MibTableColumn
tmnxMobServProcUeDedBrModifyFail = _TmnxMobServProcUeDedBrModifyFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 69),
    _TmnxMobServProcUeDedBrModifyFail_Type()
)
tmnxMobServProcUeDedBrModifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcUeDedBrModifyFail.setStatus("current")
_TmnxMobServProcNwBrModify_Type = Counter32
_TmnxMobServProcNwBrModify_Object = MibTableColumn
tmnxMobServProcNwBrModify = _TmnxMobServProcNwBrModify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 70),
    _TmnxMobServProcNwBrModify_Type()
)
tmnxMobServProcNwBrModify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwBrModify.setStatus("current")
_TmnxMobServProcNwBrModifyFail_Type = Counter32
_TmnxMobServProcNwBrModifyFail_Object = MibTableColumn
tmnxMobServProcNwBrModifyFail = _TmnxMobServProcNwBrModifyFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 71),
    _TmnxMobServProcNwBrModifyFail_Type()
)
tmnxMobServProcNwBrModifyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcNwBrModifyFail.setStatus("current")
_TmnxMobServProcPDNSuspNotice_Type = Counter32
_TmnxMobServProcPDNSuspNotice_Object = MibTableColumn
tmnxMobServProcPDNSuspNotice = _TmnxMobServProcPDNSuspNotice_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 72),
    _TmnxMobServProcPDNSuspNotice_Type()
)
tmnxMobServProcPDNSuspNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcPDNSuspNotice.setStatus("current")
_TmnxMobServProcPDNResumeNotice_Type = Counter32
_TmnxMobServProcPDNResumeNotice_Object = MibTableColumn
tmnxMobServProcPDNResumeNotice = _TmnxMobServProcPDNResumeNotice_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 73),
    _TmnxMobServProcPDNResumeNotice_Type()
)
tmnxMobServProcPDNResumeNotice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcPDNResumeNotice.setStatus("current")
_TmnxMobServProcIRSR_Type = Counter32
_TmnxMobServProcIRSR_Object = MibTableColumn
tmnxMobServProcIRSR = _TmnxMobServProcIRSR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 74),
    _TmnxMobServProcIRSR_Type()
)
tmnxMobServProcIRSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcIRSR.setStatus("current")
_TmnxMobServProcEmergncyAttachSuc_Type = Counter32
_TmnxMobServProcEmergncyAttachSuc_Object = MibTableColumn
tmnxMobServProcEmergncyAttachSuc = _TmnxMobServProcEmergncyAttachSuc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 2, 1, 75),
    _TmnxMobServProcEmergncyAttachSuc_Type()
)
tmnxMobServProcEmergncyAttachSuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServProcEmergncyAttachSuc.setStatus("current")
_TmnxMobServUeTable_Object = MibTable
tmnxMobServUeTable = _TmnxMobServUeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxMobServUeTable.setStatus("current")
_TmnxMobServUeEntry_Object = MibTableRow
tmnxMobServUeEntry = _TmnxMobServUeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1)
)
tmnxMobServUeEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImsi"),
)
if mibBuilder.loadTexts:
    tmnxMobServUeEntry.setStatus("current")
_TmnxMobServUeImsi_Type = TmnxMobUeId
_TmnxMobServUeImsi_Object = MibTableColumn
tmnxMobServUeImsi = _TmnxMobServUeImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 1),
    _TmnxMobServUeImsi_Type()
)
tmnxMobServUeImsi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServUeImsi.setStatus("current")
_TmnxMobServUeRowStatus_Type = RowStatus
_TmnxMobServUeRowStatus_Object = MibTableColumn
tmnxMobServUeRowStatus = _TmnxMobServUeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 2),
    _TmnxMobServUeRowStatus_Type()
)
tmnxMobServUeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServUeRowStatus.setStatus("current")
_TmnxMobServUeMsIsdn_Type = TmnxMobMsisdn
_TmnxMobServUeMsIsdn_Object = MibTableColumn
tmnxMobServUeMsIsdn = _TmnxMobServUeMsIsdn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 3),
    _TmnxMobServUeMsIsdn_Type()
)
tmnxMobServUeMsIsdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeMsIsdn.setStatus("current")
_TmnxMobServUeImei_Type = TmnxMobImei
_TmnxMobServUeImei_Object = MibTableColumn
tmnxMobServUeImei = _TmnxMobServUeImei_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 4),
    _TmnxMobServUeImei_Type()
)
tmnxMobServUeImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeImei.setStatus("current")
_TmnxMobServUeNai_Type = TmnxMobNai
_TmnxMobServUeNai_Object = MibTableColumn
tmnxMobServUeNai = _TmnxMobServUeNai_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 5),
    _TmnxMobServUeNai_Type()
)
tmnxMobServUeNai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeNai.setStatus("current")
_TmnxMobServUeNwkMcc_Type = TmnxMobMcc
_TmnxMobServUeNwkMcc_Object = MibTableColumn
tmnxMobServUeNwkMcc = _TmnxMobServUeNwkMcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 6),
    _TmnxMobServUeNwkMcc_Type()
)
tmnxMobServUeNwkMcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeNwkMcc.setStatus("current")
_TmnxMobServUeNwkMnc_Type = TmnxMobMnc
_TmnxMobServUeNwkMnc_Object = MibTableColumn
tmnxMobServUeNwkMnc = _TmnxMobServUeNwkMnc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 7),
    _TmnxMobServUeNwkMnc_Type()
)
tmnxMobServUeNwkMnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeNwkMnc.setStatus("current")
_TmnxMobServUeTrackingAreaId_Type = Unsigned32
_TmnxMobServUeTrackingAreaId_Object = MibTableColumn
tmnxMobServUeTrackingAreaId = _TmnxMobServUeTrackingAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 8),
    _TmnxMobServUeTrackingAreaId_Type()
)
tmnxMobServUeTrackingAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeTrackingAreaId.setStatus("current")
_TmnxMobServUeCellId_Type = Unsigned32
_TmnxMobServUeCellId_Object = MibTableColumn
tmnxMobServUeCellId = _TmnxMobServUeCellId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 9),
    _TmnxMobServUeCellId_Type()
)
tmnxMobServUeCellId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeCellId.setStatus("current")
_TmnxMobServUeState_Type = TmnxMobUeState
_TmnxMobServUeState_Object = MibTableColumn
tmnxMobServUeState = _TmnxMobServUeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 10),
    _TmnxMobServUeState_Type()
)
tmnxMobServUeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeState.setStatus("current")
_TmnxMobServUeRat_Type = TmnxMobUeRat
_TmnxMobServUeRat_Object = MibTableColumn
tmnxMobServUeRat = _TmnxMobServUeRat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 11),
    _TmnxMobServUeRat_Type()
)
tmnxMobServUeRat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeRat.setStatus("current")
_TmnxMobServUePdnContexts_Type = Unsigned32
_TmnxMobServUePdnContexts_Object = MibTableColumn
tmnxMobServUePdnContexts = _TmnxMobServUePdnContexts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 12),
    _TmnxMobServUePdnContexts_Type()
)
tmnxMobServUePdnContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUePdnContexts.setStatus("current")
_TmnxMobServUeBearerContexts_Type = Unsigned32
_TmnxMobServUeBearerContexts_Object = MibTableColumn
tmnxMobServUeBearerContexts = _TmnxMobServUeBearerContexts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 13),
    _TmnxMobServUeBearerContexts_Type()
)
tmnxMobServUeBearerContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeBearerContexts.setStatus("current")
_TmnxMobServUeChassisIndex_Type = TmnxChassisIndex
_TmnxMobServUeChassisIndex_Object = MibTableColumn
tmnxMobServUeChassisIndex = _TmnxMobServUeChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 14),
    _TmnxMobServUeChassisIndex_Type()
)
tmnxMobServUeChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeChassisIndex.setStatus("current")
_TmnxMobServUeCardSlotNum_Type = TmnxSlotNum
_TmnxMobServUeCardSlotNum_Object = MibTableColumn
tmnxMobServUeCardSlotNum = _TmnxMobServUeCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 15),
    _TmnxMobServUeCardSlotNum_Type()
)
tmnxMobServUeCardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeCardSlotNum.setStatus("current")
_TmnxMobServUeS11MmeCtrlTeid_Type = Unsigned32
_TmnxMobServUeS11MmeCtrlTeid_Object = MibTableColumn
tmnxMobServUeS11MmeCtrlTeid = _TmnxMobServUeS11MmeCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 16),
    _TmnxMobServUeS11MmeCtrlTeid_Type()
)
tmnxMobServUeS11MmeCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS11MmeCtrlTeid.setStatus("current")
_TmnxMobServUeS11MmeCtrlAddrType_Type = InetAddressType
_TmnxMobServUeS11MmeCtrlAddrType_Object = MibTableColumn
tmnxMobServUeS11MmeCtrlAddrType = _TmnxMobServUeS11MmeCtrlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 17),
    _TmnxMobServUeS11MmeCtrlAddrType_Type()
)
tmnxMobServUeS11MmeCtrlAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS11MmeCtrlAddrType.setStatus("current")


class _TmnxMobServUeS11MmeCtrlAddr_Type(InetAddress):
    """Custom type tmnxMobServUeS11MmeCtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServUeS11MmeCtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobServUeS11MmeCtrlAddr_Object = MibTableColumn
tmnxMobServUeS11MmeCtrlAddr = _TmnxMobServUeS11MmeCtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 18),
    _TmnxMobServUeS11MmeCtrlAddr_Type()
)
tmnxMobServUeS11MmeCtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS11MmeCtrlAddr.setStatus("current")
_TmnxMobServUeS11SgwCtrlTeid_Type = Unsigned32
_TmnxMobServUeS11SgwCtrlTeid_Object = MibTableColumn
tmnxMobServUeS11SgwCtrlTeid = _TmnxMobServUeS11SgwCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 19),
    _TmnxMobServUeS11SgwCtrlTeid_Type()
)
tmnxMobServUeS11SgwCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS11SgwCtrlTeid.setStatus("current")
_TmnxMobServUeS11SgwCtrlAddrType_Type = InetAddressType
_TmnxMobServUeS11SgwCtrlAddrType_Object = MibTableColumn
tmnxMobServUeS11SgwCtrlAddrType = _TmnxMobServUeS11SgwCtrlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 20),
    _TmnxMobServUeS11SgwCtrlAddrType_Type()
)
tmnxMobServUeS11SgwCtrlAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS11SgwCtrlAddrType.setStatus("current")


class _TmnxMobServUeS11SgwCtrlAddr_Type(InetAddress):
    """Custom type tmnxMobServUeS11SgwCtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServUeS11SgwCtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobServUeS11SgwCtrlAddr_Object = MibTableColumn
tmnxMobServUeS11SgwCtrlAddr = _TmnxMobServUeS11SgwCtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 21),
    _TmnxMobServUeS11SgwCtrlAddr_Type()
)
tmnxMobServUeS11SgwCtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS11SgwCtrlAddr.setStatus("current")
_TmnxMobServUeS11InterEnbX2HandOv_Type = Counter32
_TmnxMobServUeS11InterEnbX2HandOv_Object = MibTableColumn
tmnxMobServUeS11InterEnbX2HandOv = _TmnxMobServUeS11InterEnbX2HandOv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 22),
    _TmnxMobServUeS11InterEnbX2HandOv_Type()
)
tmnxMobServUeS11InterEnbX2HandOv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS11InterEnbX2HandOv.setStatus("current")
_TmnxMobServUeS11InterEnbS1HandOv_Type = Counter32
_TmnxMobServUeS11InterEnbS1HandOv_Object = MibTableColumn
tmnxMobServUeS11InterEnbS1HandOv = _TmnxMobServUeS11InterEnbS1HandOv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 23),
    _TmnxMobServUeS11InterEnbS1HandOv_Type()
)
tmnxMobServUeS11InterEnbS1HandOv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS11InterEnbS1HandOv.setStatus("current")
_TmnxMobServUeS1ReleaseProcedures_Type = Counter32
_TmnxMobServUeS1ReleaseProcedures_Object = MibTableColumn
tmnxMobServUeS1ReleaseProcedures = _TmnxMobServUeS1ReleaseProcedures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 24),
    _TmnxMobServUeS1ReleaseProcedures_Type()
)
tmnxMobServUeS1ReleaseProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeS1ReleaseProcedures.setStatus("current")
_TmnxMobServUePagingReq_Type = Counter32
_TmnxMobServUePagingReq_Object = MibTableColumn
tmnxMobServUePagingReq = _TmnxMobServUePagingReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 25),
    _TmnxMobServUePagingReq_Type()
)
tmnxMobServUePagingReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUePagingReq.setStatus("current")
_TmnxMobServUeRfSgwAddrType_Type = InetAddressType
_TmnxMobServUeRfSgwAddrType_Object = MibTableColumn
tmnxMobServUeRfSgwAddrType = _TmnxMobServUeRfSgwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 26),
    _TmnxMobServUeRfSgwAddrType_Type()
)
tmnxMobServUeRfSgwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeRfSgwAddrType.setStatus("current")


class _TmnxMobServUeRfSgwAddr_Type(InetAddress):
    """Custom type tmnxMobServUeRfSgwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServUeRfSgwAddr_Type.__name__ = "InetAddress"
_TmnxMobServUeRfSgwAddr_Object = MibTableColumn
tmnxMobServUeRfSgwAddr = _TmnxMobServUeRfSgwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 27),
    _TmnxMobServUeRfSgwAddr_Type()
)
tmnxMobServUeRfSgwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeRfSgwAddr.setStatus("current")
_TmnxMobServUeIntraSgwIdleTau_Type = Counter32
_TmnxMobServUeIntraSgwIdleTau_Object = MibTableColumn
tmnxMobServUeIntraSgwIdleTau = _TmnxMobServUeIntraSgwIdleTau_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 28),
    _TmnxMobServUeIntraSgwIdleTau_Type()
)
tmnxMobServUeIntraSgwIdleTau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeIntraSgwIdleTau.setStatus("current")
_TmnxMobServUeInitServReqProcs_Type = Counter32
_TmnxMobServUeInitServReqProcs_Object = MibTableColumn
tmnxMobServUeInitServReqProcs = _TmnxMobServUeInitServReqProcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 29),
    _TmnxMobServUeInitServReqProcs_Type()
)
tmnxMobServUeInitServReqProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeInitServReqProcs.setStatus("current")
_TmnxMobServUePagedCount_Type = Counter32
_TmnxMobServUePagedCount_Object = MibTableColumn
tmnxMobServUePagedCount = _TmnxMobServUePagedCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 30),
    _TmnxMobServUePagedCount_Type()
)
tmnxMobServUePagedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUePagedCount.setStatus("obsolete")
_TmnxMobServKeyType_Type = TmnxMobUeIdType
_TmnxMobServKeyType_Object = MibTableColumn
tmnxMobServKeyType = _TmnxMobServKeyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 31),
    _TmnxMobServKeyType_Type()
)
tmnxMobServKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMobServKeyType.setStatus("current")
_TmnxMobServUeImsiStr_Type = TmnxMobImsiStr
_TmnxMobServUeImsiStr_Object = MibTableColumn
tmnxMobServUeImsiStr = _TmnxMobServUeImsiStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 3, 1, 32),
    _TmnxMobServUeImsiStr_Type()
)
tmnxMobServUeImsiStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServUeImsiStr.setStatus("current")
_TmnxMobServPdnContextTable_Object = MibTable
tmnxMobServPdnContextTable = _TmnxMobServPdnContextTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxMobServPdnContextTable.setStatus("current")
_TmnxMobServPdnContextEntry_Object = MibTableRow
tmnxMobServPdnContextEntry = _TmnxMobServPdnContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1)
)
tmnxMobServPdnContextEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImsi"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcApn"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcPdnType"),
)
if mibBuilder.loadTexts:
    tmnxMobServPdnContextEntry.setStatus("current")
_TmnxMobServPcApn_Type = TmnxMobApn
_TmnxMobServPcApn_Object = MibTableColumn
tmnxMobServPcApn = _TmnxMobServPcApn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 1),
    _TmnxMobServPcApn_Type()
)
tmnxMobServPcApn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServPcApn.setStatus("current")
_TmnxMobServPcPdnType_Type = TmnxMobPdnType
_TmnxMobServPcPdnType_Object = MibTableColumn
tmnxMobServPcPdnType = _TmnxMobServPcPdnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 2),
    _TmnxMobServPcPdnType_Type()
)
tmnxMobServPcPdnType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServPcPdnType.setStatus("current")
_TmnxMobServPcLinkedBearerId_Type = TmnxMobBearerId
_TmnxMobServPcLinkedBearerId_Object = MibTableColumn
tmnxMobServPcLinkedBearerId = _TmnxMobServPcLinkedBearerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 3),
    _TmnxMobServPcLinkedBearerId_Type()
)
tmnxMobServPcLinkedBearerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcLinkedBearerId.setStatus("current")
_TmnxMobServPcApnRestriction_Type = Unsigned32
_TmnxMobServPcApnRestriction_Object = MibTableColumn
tmnxMobServPcApnRestriction = _TmnxMobServPcApnRestriction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 4),
    _TmnxMobServPcApnRestriction_Type()
)
tmnxMobServPcApnRestriction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcApnRestriction.setStatus("current")
_TmnxMobServPcUlApnAmbr_Type = Unsigned32
_TmnxMobServPcUlApnAmbr_Object = MibTableColumn
tmnxMobServPcUlApnAmbr = _TmnxMobServPcUlApnAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 5),
    _TmnxMobServPcUlApnAmbr_Type()
)
tmnxMobServPcUlApnAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcUlApnAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServPcUlApnAmbr.setUnits("kbps")
_TmnxMobServPcDlApnAmbr_Type = Unsigned32
_TmnxMobServPcDlApnAmbr_Object = MibTableColumn
tmnxMobServPcDlApnAmbr = _TmnxMobServPcDlApnAmbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 6),
    _TmnxMobServPcDlApnAmbr_Type()
)
tmnxMobServPcDlApnAmbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcDlApnAmbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServPcDlApnAmbr.setUnits("kbps")
_TmnxMobServPcIpv4AddressType_Type = InetAddressType
_TmnxMobServPcIpv4AddressType_Object = MibTableColumn
tmnxMobServPcIpv4AddressType = _TmnxMobServPcIpv4AddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 7),
    _TmnxMobServPcIpv4AddressType_Type()
)
tmnxMobServPcIpv4AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcIpv4AddressType.setStatus("current")


class _TmnxMobServPcIpv4Address_Type(InetAddress):
    """Custom type tmnxMobServPcIpv4Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobServPcIpv4Address_Type.__name__ = "InetAddress"
_TmnxMobServPcIpv4Address_Object = MibTableColumn
tmnxMobServPcIpv4Address = _TmnxMobServPcIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 8),
    _TmnxMobServPcIpv4Address_Type()
)
tmnxMobServPcIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcIpv4Address.setStatus("current")
_TmnxMobServPcIpv6AddressType_Type = InetAddressType
_TmnxMobServPcIpv6AddressType_Object = MibTableColumn
tmnxMobServPcIpv6AddressType = _TmnxMobServPcIpv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 9),
    _TmnxMobServPcIpv6AddressType_Type()
)
tmnxMobServPcIpv6AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcIpv6AddressType.setStatus("current")


class _TmnxMobServPcIpv6Address_Type(InetAddress):
    """Custom type tmnxMobServPcIpv6Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServPcIpv6Address_Type.__name__ = "InetAddress"
_TmnxMobServPcIpv6Address_Object = MibTableColumn
tmnxMobServPcIpv6Address = _TmnxMobServPcIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 10),
    _TmnxMobServPcIpv6Address_Type()
)
tmnxMobServPcIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcIpv6Address.setStatus("current")
_TmnxMobServPcBearerContexts_Type = Unsigned32
_TmnxMobServPcBearerContexts_Object = MibTableColumn
tmnxMobServPcBearerContexts = _TmnxMobServPcBearerContexts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 11),
    _TmnxMobServPcBearerContexts_Type()
)
tmnxMobServPcBearerContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcBearerContexts.setStatus("current")
_TmnxMobServPcSessionState_Type = TmnxMobPdnSessionState
_TmnxMobServPcSessionState_Object = MibTableColumn
tmnxMobServPcSessionState = _TmnxMobServPcSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 12),
    _TmnxMobServPcSessionState_Type()
)
tmnxMobServPcSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcSessionState.setStatus("current")
_TmnxMobServPcLastEvent_Type = TmnxMobPdnSessionEvent
_TmnxMobServPcLastEvent_Object = MibTableColumn
tmnxMobServPcLastEvent = _TmnxMobServPcLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 13),
    _TmnxMobServPcLastEvent_Type()
)
tmnxMobServPcLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcLastEvent.setStatus("current")
_TmnxMobServPcS5S8SigProtocol_Type = TmnxMobPgwSigProtocol
_TmnxMobServPcS5S8SigProtocol_Object = MibTableColumn
tmnxMobServPcS5S8SigProtocol = _TmnxMobServPcS5S8SigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 14),
    _TmnxMobServPcS5S8SigProtocol_Type()
)
tmnxMobServPcS5S8SigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8SigProtocol.setStatus("current")
_TmnxMobServPcS5S8SgwCtrlTeid_Type = Unsigned32
_TmnxMobServPcS5S8SgwCtrlTeid_Object = MibTableColumn
tmnxMobServPcS5S8SgwCtrlTeid = _TmnxMobServPcS5S8SgwCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 15),
    _TmnxMobServPcS5S8SgwCtrlTeid_Type()
)
tmnxMobServPcS5S8SgwCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8SgwCtrlTeid.setStatus("current")
_TmnxMobServPcS5S8SgwCtrlAddrType_Type = InetAddressType
_TmnxMobServPcS5S8SgwCtrlAddrType_Object = MibTableColumn
tmnxMobServPcS5S8SgwCtrlAddrType = _TmnxMobServPcS5S8SgwCtrlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 16),
    _TmnxMobServPcS5S8SgwCtrlAddrType_Type()
)
tmnxMobServPcS5S8SgwCtrlAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8SgwCtrlAddrType.setStatus("current")


class _TmnxMobServPcS5S8SgwCtrlAddr_Type(InetAddress):
    """Custom type tmnxMobServPcS5S8SgwCtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobServPcS5S8SgwCtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobServPcS5S8SgwCtrlAddr_Object = MibTableColumn
tmnxMobServPcS5S8SgwCtrlAddr = _TmnxMobServPcS5S8SgwCtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 17),
    _TmnxMobServPcS5S8SgwCtrlAddr_Type()
)
tmnxMobServPcS5S8SgwCtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8SgwCtrlAddr.setStatus("current")
_TmnxMobServPcS5S8PgwCtrlTeid_Type = Unsigned32
_TmnxMobServPcS5S8PgwCtrlTeid_Object = MibTableColumn
tmnxMobServPcS5S8PgwCtrlTeid = _TmnxMobServPcS5S8PgwCtrlTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 18),
    _TmnxMobServPcS5S8PgwCtrlTeid_Type()
)
tmnxMobServPcS5S8PgwCtrlTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8PgwCtrlTeid.setStatus("current")
_TmnxMobServPcS5S8PgwCtrlAddrType_Type = InetAddressType
_TmnxMobServPcS5S8PgwCtrlAddrType_Object = MibTableColumn
tmnxMobServPcS5S8PgwCtrlAddrType = _TmnxMobServPcS5S8PgwCtrlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 19),
    _TmnxMobServPcS5S8PgwCtrlAddrType_Type()
)
tmnxMobServPcS5S8PgwCtrlAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8PgwCtrlAddrType.setStatus("current")


class _TmnxMobServPcS5S8PgwCtrlAddr_Type(InetAddress):
    """Custom type tmnxMobServPcS5S8PgwCtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobServPcS5S8PgwCtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobServPcS5S8PgwCtrlAddr_Object = MibTableColumn
tmnxMobServPcS5S8PgwCtrlAddr = _TmnxMobServPcS5S8PgwCtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 20),
    _TmnxMobServPcS5S8PgwCtrlAddr_Type()
)
tmnxMobServPcS5S8PgwCtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8PgwCtrlAddr.setStatus("current")
_TmnxMobServPcRfServerAddrType_Type = InetAddressType
_TmnxMobServPcRfServerAddrType_Object = MibTableColumn
tmnxMobServPcRfServerAddrType = _TmnxMobServPcRfServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 21),
    _TmnxMobServPcRfServerAddrType_Type()
)
tmnxMobServPcRfServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRfServerAddrType.setStatus("current")


class _TmnxMobServPcRfServerAddr_Type(InetAddress):
    """Custom type tmnxMobServPcRfServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServPcRfServerAddr_Type.__name__ = "InetAddress"
_TmnxMobServPcRfServerAddr_Object = MibTableColumn
tmnxMobServPcRfServerAddr = _TmnxMobServPcRfServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 22),
    _TmnxMobServPcRfServerAddr_Type()
)
tmnxMobServPcRfServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRfServerAddr.setStatus("current")
_TmnxMobServPcRfServerState_Type = TmnxMobServerState
_TmnxMobServPcRfServerState_Object = MibTableColumn
tmnxMobServPcRfServerState = _TmnxMobServPcRfServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 23),
    _TmnxMobServPcRfServerState_Type()
)
tmnxMobServPcRfServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRfServerState.setStatus("current")
_TmnxMobServPcRfBearerType_Type = TmnxMobChargingBearerType
_TmnxMobServPcRfBearerType_Object = MibTableColumn
tmnxMobServPcRfBearerType = _TmnxMobServPcRfBearerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 24),
    _TmnxMobServPcRfBearerType_Type()
)
tmnxMobServPcRfBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRfBearerType.setStatus("current")
_TmnxMobServPcRfChargingLevel_Type = TmnxMobChargingLevel
_TmnxMobServPcRfChargingLevel_Object = MibTableColumn
tmnxMobServPcRfChargingLevel = _TmnxMobServPcRfChargingLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 25),
    _TmnxMobServPcRfChargingLevel_Type()
)
tmnxMobServPcRfChargingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRfChargingLevel.setStatus("current")
_TmnxMobServPcRfChargingProfile_Type = TmnxMobChargingProfile
_TmnxMobServPcRfChargingProfile_Object = MibTableColumn
tmnxMobServPcRfChargingProfile = _TmnxMobServPcRfChargingProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 26),
    _TmnxMobServPcRfChargingProfile_Type()
)
tmnxMobServPcRfChargingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRfChargingProfile.setStatus("current")
_TmnxMobServPcRfTriggeredRecords_Type = Counter32
_TmnxMobServPcRfTriggeredRecords_Object = MibTableColumn
tmnxMobServPcRfTriggeredRecords = _TmnxMobServPcRfTriggeredRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 27),
    _TmnxMobServPcRfTriggeredRecords_Type()
)
tmnxMobServPcRfTriggeredRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRfTriggeredRecords.setStatus("current")
_TmnxMobServPcRfInterimRecords_Type = Counter32
_TmnxMobServPcRfInterimRecords_Object = MibTableColumn
tmnxMobServPcRfInterimRecords = _TmnxMobServPcRfInterimRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 28),
    _TmnxMobServPcRfInterimRecords_Type()
)
tmnxMobServPcRfInterimRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRfInterimRecords.setStatus("current")
_TmnxMobServPcPcrfEventTriggers_Type = Unsigned32
_TmnxMobServPcPcrfEventTriggers_Object = MibTableColumn
tmnxMobServPcPcrfEventTriggers = _TmnxMobServPcPcrfEventTriggers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 29),
    _TmnxMobServPcPcrfEventTriggers_Type()
)
tmnxMobServPcPcrfEventTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcPcrfEventTriggers.setStatus("current")
_TmnxMobServPcGxcPcrfAddressType_Type = InetAddressType
_TmnxMobServPcGxcPcrfAddressType_Object = MibTableColumn
tmnxMobServPcGxcPcrfAddressType = _TmnxMobServPcGxcPcrfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 30),
    _TmnxMobServPcGxcPcrfAddressType_Type()
)
tmnxMobServPcGxcPcrfAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcGxcPcrfAddressType.setStatus("current")


class _TmnxMobServPcGxcPcrfAddress_Type(InetAddress):
    """Custom type tmnxMobServPcGxcPcrfAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServPcGxcPcrfAddress_Type.__name__ = "InetAddress"
_TmnxMobServPcGxcPcrfAddress_Object = MibTableColumn
tmnxMobServPcGxcPcrfAddress = _TmnxMobServPcGxcPcrfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 31),
    _TmnxMobServPcGxcPcrfAddress_Type()
)
tmnxMobServPcGxcPcrfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcGxcPcrfAddress.setStatus("current")
_TmnxMobServPcGxcSgwAddressType_Type = InetAddressType
_TmnxMobServPcGxcSgwAddressType_Object = MibTableColumn
tmnxMobServPcGxcSgwAddressType = _TmnxMobServPcGxcSgwAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 32),
    _TmnxMobServPcGxcSgwAddressType_Type()
)
tmnxMobServPcGxcSgwAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcGxcSgwAddressType.setStatus("current")


class _TmnxMobServPcGxcSgwAddress_Type(InetAddress):
    """Custom type tmnxMobServPcGxcSgwAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServPcGxcSgwAddress_Type.__name__ = "InetAddress"
_TmnxMobServPcGxcSgwAddress_Object = MibTableColumn
tmnxMobServPcGxcSgwAddress = _TmnxMobServPcGxcSgwAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 33),
    _TmnxMobServPcGxcSgwAddress_Type()
)
tmnxMobServPcGxcSgwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcGxcSgwAddress.setStatus("current")
_TmnxMobServPcS5S8SgwGreKey_Type = Unsigned32
_TmnxMobServPcS5S8SgwGreKey_Object = MibTableColumn
tmnxMobServPcS5S8SgwGreKey = _TmnxMobServPcS5S8SgwGreKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 34),
    _TmnxMobServPcS5S8SgwGreKey_Type()
)
tmnxMobServPcS5S8SgwGreKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8SgwGreKey.setStatus("current")
_TmnxMobServPcS5S8PgwGreKey_Type = Unsigned32
_TmnxMobServPcS5S8PgwGreKey_Object = MibTableColumn
tmnxMobServPcS5S8PgwGreKey = _TmnxMobServPcS5S8PgwGreKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 35),
    _TmnxMobServPcS5S8PgwGreKey_Type()
)
tmnxMobServPcS5S8PgwGreKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8PgwGreKey.setStatus("current")
_TmnxMobServPcS5S8PgwTrprtAdrType_Type = InetAddressType
_TmnxMobServPcS5S8PgwTrprtAdrType_Object = MibTableColumn
tmnxMobServPcS5S8PgwTrprtAdrType = _TmnxMobServPcS5S8PgwTrprtAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 36),
    _TmnxMobServPcS5S8PgwTrprtAdrType_Type()
)
tmnxMobServPcS5S8PgwTrprtAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8PgwTrprtAdrType.setStatus("current")


class _TmnxMobServPcS5S8PgwTransprtAddr_Type(InetAddress):
    """Custom type tmnxMobServPcS5S8PgwTransprtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxMobServPcS5S8PgwTransprtAddr_Type.__name__ = "InetAddress"
_TmnxMobServPcS5S8PgwTransprtAddr_Object = MibTableColumn
tmnxMobServPcS5S8PgwTransprtAddr = _TmnxMobServPcS5S8PgwTransprtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 37),
    _TmnxMobServPcS5S8PgwTransprtAddr_Type()
)
tmnxMobServPcS5S8PgwTransprtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8PgwTransprtAddr.setStatus("current")
_TmnxMobServPcS5S8SgwV6CtrlAdrTyp_Type = InetAddressType
_TmnxMobServPcS5S8SgwV6CtrlAdrTyp_Object = MibTableColumn
tmnxMobServPcS5S8SgwV6CtrlAdrTyp = _TmnxMobServPcS5S8SgwV6CtrlAdrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 38),
    _TmnxMobServPcS5S8SgwV6CtrlAdrTyp_Type()
)
tmnxMobServPcS5S8SgwV6CtrlAdrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8SgwV6CtrlAdrTyp.setStatus("current")


class _TmnxMobServPcS5S8SgwV6CtrlAddr_Type(InetAddress):
    """Custom type tmnxMobServPcS5S8SgwV6CtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServPcS5S8SgwV6CtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobServPcS5S8SgwV6CtrlAddr_Object = MibTableColumn
tmnxMobServPcS5S8SgwV6CtrlAddr = _TmnxMobServPcS5S8SgwV6CtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 39),
    _TmnxMobServPcS5S8SgwV6CtrlAddr_Type()
)
tmnxMobServPcS5S8SgwV6CtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8SgwV6CtrlAddr.setStatus("current")
_TmnxMobServPcS5S8PgwV6CtrlAdrTyp_Type = InetAddressType
_TmnxMobServPcS5S8PgwV6CtrlAdrTyp_Object = MibTableColumn
tmnxMobServPcS5S8PgwV6CtrlAdrTyp = _TmnxMobServPcS5S8PgwV6CtrlAdrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 40),
    _TmnxMobServPcS5S8PgwV6CtrlAdrTyp_Type()
)
tmnxMobServPcS5S8PgwV6CtrlAdrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8PgwV6CtrlAdrTyp.setStatus("current")


class _TmnxMobServPcS5S8PgwV6CtrlAddr_Type(InetAddress):
    """Custom type tmnxMobServPcS5S8PgwV6CtrlAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServPcS5S8PgwV6CtrlAddr_Type.__name__ = "InetAddress"
_TmnxMobServPcS5S8PgwV6CtrlAddr_Object = MibTableColumn
tmnxMobServPcS5S8PgwV6CtrlAddr = _TmnxMobServPcS5S8PgwV6CtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 41),
    _TmnxMobServPcS5S8PgwV6CtrlAddr_Type()
)
tmnxMobServPcS5S8PgwV6CtrlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcS5S8PgwV6CtrlAddr.setStatus("current")
_TmnxMobServPcAntiSpoofFailureCnt_Type = Counter32
_TmnxMobServPcAntiSpoofFailureCnt_Object = MibTableColumn
tmnxMobServPcAntiSpoofFailureCnt = _TmnxMobServPcAntiSpoofFailureCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 42),
    _TmnxMobServPcAntiSpoofFailureCnt_Type()
)
tmnxMobServPcAntiSpoofFailureCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAntiSpoofFailureCnt.setStatus("current")


class _TmnxMobServPcImsiAuthStatus_Type(Integer32):
    """Custom type tmnxMobServPcImsiAuthStatus based on Integer32"""
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


_TmnxMobServPcImsiAuthStatus_Type.__name__ = "Integer32"
_TmnxMobServPcImsiAuthStatus_Object = MibTableColumn
tmnxMobServPcImsiAuthStatus = _TmnxMobServPcImsiAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 43),
    _TmnxMobServPcImsiAuthStatus_Type()
)
tmnxMobServPcImsiAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcImsiAuthStatus.setStatus("current")
_TmnxMobServPcImeiStr_Type = TmnxMobImei
_TmnxMobServPcImeiStr_Object = MibTableColumn
tmnxMobServPcImeiStr = _TmnxMobServPcImeiStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 44),
    _TmnxMobServPcImeiStr_Type()
)
tmnxMobServPcImeiStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcImeiStr.setStatus("current")
_TmnxMobServPcImsiStr_Type = TmnxMobImsiStr
_TmnxMobServPcImsiStr_Object = MibTableColumn
tmnxMobServPcImsiStr = _TmnxMobServPcImsiStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 60),
    _TmnxMobServPcImsiStr_Type()
)
tmnxMobServPcImsiStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcImsiStr.setStatus("current")
_TmnxMobServPcRefPointType_Type = TmnxMobServRefPointType
_TmnxMobServPcRefPointType_Object = MibTableColumn
tmnxMobServPcRefPointType = _TmnxMobServPcRefPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 4, 1, 61),
    _TmnxMobServPcRefPointType_Type()
)
tmnxMobServPcRefPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcRefPointType.setStatus("current")
_TmnxMobServBearerContextTable_Object = MibTable
tmnxMobServBearerContextTable = _TmnxMobServBearerContextTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxMobServBearerContextTable.setStatus("current")
_TmnxMobServBearerContextEntry_Object = MibTableRow
tmnxMobServBearerContextEntry = _TmnxMobServBearerContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1)
)
tmnxMobServBearerContextEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImsi"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcApn"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcPdnType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcBearerId"),
)
if mibBuilder.loadTexts:
    tmnxMobServBearerContextEntry.setStatus("current")
_TmnxMobServBcBearerId_Type = TmnxMobBearerId
_TmnxMobServBcBearerId_Object = MibTableColumn
tmnxMobServBcBearerId = _TmnxMobServBcBearerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 1),
    _TmnxMobServBcBearerId_Type()
)
tmnxMobServBcBearerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServBcBearerId.setStatus("current")
_TmnxMobServBcBearerType_Type = TmnxMobBearerType
_TmnxMobServBcBearerType_Object = MibTableColumn
tmnxMobServBcBearerType = _TmnxMobServBcBearerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 2),
    _TmnxMobServBcBearerType_Type()
)
tmnxMobServBcBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcBearerType.setStatus("current")
_TmnxMobServBcUpTime_Type = Unsigned32
_TmnxMobServBcUpTime_Object = MibTableColumn
tmnxMobServBcUpTime = _TmnxMobServBcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 3),
    _TmnxMobServBcUpTime_Type()
)
tmnxMobServBcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcUpTime.setUnits("seconds")
_TmnxMobServBcQci_Type = TmnxMobQci
_TmnxMobServBcQci_Object = MibTableColumn
tmnxMobServBcQci = _TmnxMobServBcQci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 4),
    _TmnxMobServBcQci_Type()
)
tmnxMobServBcQci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcQci.setStatus("current")
_TmnxMobServBcArp_Type = TmnxMobArp
_TmnxMobServBcArp_Object = MibTableColumn
tmnxMobServBcArp = _TmnxMobServBcArp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 5),
    _TmnxMobServBcArp_Type()
)
tmnxMobServBcArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcArp.setStatus("current")
_TmnxMobServBcSdfs_Type = TmnxMobSdf
_TmnxMobServBcSdfs_Object = MibTableColumn
tmnxMobServBcSdfs = _TmnxMobServBcSdfs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 6),
    _TmnxMobServBcSdfs_Type()
)
tmnxMobServBcSdfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfs.setStatus("current")
_TmnxMobServBcFilters_Type = TmnxMobSdfFilterNum
_TmnxMobServBcFilters_Object = MibTableColumn
tmnxMobServBcFilters = _TmnxMobServBcFilters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 7),
    _TmnxMobServBcFilters_Type()
)
tmnxMobServBcFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcFilters.setStatus("current")
_TmnxMobServBcQosUlMbr_Type = Unsigned32
_TmnxMobServBcQosUlMbr_Object = MibTableColumn
tmnxMobServBcQosUlMbr = _TmnxMobServBcQosUlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 8),
    _TmnxMobServBcQosUlMbr_Type()
)
tmnxMobServBcQosUlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcQosUlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcQosUlMbr.setUnits("Kbps")
_TmnxMobServBcQosDlMbr_Type = Unsigned32
_TmnxMobServBcQosDlMbr_Object = MibTableColumn
tmnxMobServBcQosDlMbr = _TmnxMobServBcQosDlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 9),
    _TmnxMobServBcQosDlMbr_Type()
)
tmnxMobServBcQosDlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcQosDlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcQosDlMbr.setUnits("Kbps")
_TmnxMobServBcQosUlGbr_Type = Unsigned32
_TmnxMobServBcQosUlGbr_Object = MibTableColumn
tmnxMobServBcQosUlGbr = _TmnxMobServBcQosUlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 10),
    _TmnxMobServBcQosUlGbr_Type()
)
tmnxMobServBcQosUlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcQosUlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcQosUlGbr.setUnits("Kbps")
_TmnxMobServBcQosDlGbr_Type = Unsigned32
_TmnxMobServBcQosDlGbr_Object = MibTableColumn
tmnxMobServBcQosDlGbr = _TmnxMobServBcQosDlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 11),
    _TmnxMobServBcQosDlGbr_Type()
)
tmnxMobServBcQosDlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcQosDlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcQosDlGbr.setUnits("Kbps")
_TmnxMobServBcS1uEnodebTeid_Type = Unsigned32
_TmnxMobServBcS1uEnodebTeid_Object = MibTableColumn
tmnxMobServBcS1uEnodebTeid = _TmnxMobServBcS1uEnodebTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 12),
    _TmnxMobServBcS1uEnodebTeid_Type()
)
tmnxMobServBcS1uEnodebTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uEnodebTeid.setStatus("current")
_TmnxMobServBcS1uEnodebAddrType_Type = InetAddressType
_TmnxMobServBcS1uEnodebAddrType_Object = MibTableColumn
tmnxMobServBcS1uEnodebAddrType = _TmnxMobServBcS1uEnodebAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 13),
    _TmnxMobServBcS1uEnodebAddrType_Type()
)
tmnxMobServBcS1uEnodebAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uEnodebAddrType.setStatus("current")


class _TmnxMobServBcS1uEnodebAddr_Type(InetAddress):
    """Custom type tmnxMobServBcS1uEnodebAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcS1uEnodebAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcS1uEnodebAddr_Object = MibTableColumn
tmnxMobServBcS1uEnodebAddr = _TmnxMobServBcS1uEnodebAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 14),
    _TmnxMobServBcS1uEnodebAddr_Type()
)
tmnxMobServBcS1uEnodebAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uEnodebAddr.setStatus("current")
_TmnxMobServBcS1uSgwTeid_Type = Unsigned32
_TmnxMobServBcS1uSgwTeid_Object = MibTableColumn
tmnxMobServBcS1uSgwTeid = _TmnxMobServBcS1uSgwTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 15),
    _TmnxMobServBcS1uSgwTeid_Type()
)
tmnxMobServBcS1uSgwTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uSgwTeid.setStatus("current")
_TmnxMobServBcS1uSgwAddrType_Type = InetAddressType
_TmnxMobServBcS1uSgwAddrType_Object = MibTableColumn
tmnxMobServBcS1uSgwAddrType = _TmnxMobServBcS1uSgwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 16),
    _TmnxMobServBcS1uSgwAddrType_Type()
)
tmnxMobServBcS1uSgwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uSgwAddrType.setStatus("current")


class _TmnxMobServBcS1uSgwAddr_Type(InetAddress):
    """Custom type tmnxMobServBcS1uSgwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcS1uSgwAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcS1uSgwAddr_Object = MibTableColumn
tmnxMobServBcS1uSgwAddr = _TmnxMobServBcS1uSgwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 17),
    _TmnxMobServBcS1uSgwAddr_Type()
)
tmnxMobServBcS1uSgwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uSgwAddr.setStatus("current")
_TmnxMobServBcS5S8SgwTeid_Type = Unsigned32
_TmnxMobServBcS5S8SgwTeid_Object = MibTableColumn
tmnxMobServBcS5S8SgwTeid = _TmnxMobServBcS5S8SgwTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 18),
    _TmnxMobServBcS5S8SgwTeid_Type()
)
tmnxMobServBcS5S8SgwTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5S8SgwTeid.setStatus("current")
_TmnxMobServBcS5S8SgwDataAddrType_Type = InetAddressType
_TmnxMobServBcS5S8SgwDataAddrType_Object = MibTableColumn
tmnxMobServBcS5S8SgwDataAddrType = _TmnxMobServBcS5S8SgwDataAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 19),
    _TmnxMobServBcS5S8SgwDataAddrType_Type()
)
tmnxMobServBcS5S8SgwDataAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5S8SgwDataAddrType.setStatus("current")


class _TmnxMobServBcS5S8SgwDataAddr_Type(InetAddress):
    """Custom type tmnxMobServBcS5S8SgwDataAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcS5S8SgwDataAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcS5S8SgwDataAddr_Object = MibTableColumn
tmnxMobServBcS5S8SgwDataAddr = _TmnxMobServBcS5S8SgwDataAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 20),
    _TmnxMobServBcS5S8SgwDataAddr_Type()
)
tmnxMobServBcS5S8SgwDataAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5S8SgwDataAddr.setStatus("current")
_TmnxMobServBcS5S8PgwTeid_Type = Unsigned32
_TmnxMobServBcS5S8PgwTeid_Object = MibTableColumn
tmnxMobServBcS5S8PgwTeid = _TmnxMobServBcS5S8PgwTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 21),
    _TmnxMobServBcS5S8PgwTeid_Type()
)
tmnxMobServBcS5S8PgwTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5S8PgwTeid.setStatus("current")
_TmnxMobServBcS5S8PgwDataAddrType_Type = InetAddressType
_TmnxMobServBcS5S8PgwDataAddrType_Object = MibTableColumn
tmnxMobServBcS5S8PgwDataAddrType = _TmnxMobServBcS5S8PgwDataAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 22),
    _TmnxMobServBcS5S8PgwDataAddrType_Type()
)
tmnxMobServBcS5S8PgwDataAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5S8PgwDataAddrType.setStatus("current")


class _TmnxMobServBcS5S8PgwDataAddr_Type(InetAddress):
    """Custom type tmnxMobServBcS5S8PgwDataAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcS5S8PgwDataAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcS5S8PgwDataAddr_Object = MibTableColumn
tmnxMobServBcS5S8PgwDataAddr = _TmnxMobServBcS5S8PgwDataAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 23),
    _TmnxMobServBcS5S8PgwDataAddr_Type()
)
tmnxMobServBcS5S8PgwDataAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5S8PgwDataAddr.setStatus("current")
_TmnxMobServBcS11QosModifications_Type = Counter32
_TmnxMobServBcS11QosModifications_Object = MibTableColumn
tmnxMobServBcS11QosModifications = _TmnxMobServBcS11QosModifications_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 24),
    _TmnxMobServBcS11QosModifications_Type()
)
tmnxMobServBcS11QosModifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS11QosModifications.setStatus("current")
_TmnxMobServBcS5ULPackets_Type = Counter64
_TmnxMobServBcS5ULPackets_Object = MibTableColumn
tmnxMobServBcS5ULPackets = _TmnxMobServBcS5ULPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 25),
    _TmnxMobServBcS5ULPackets_Type()
)
tmnxMobServBcS5ULPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5ULPackets.setStatus("current")
_TmnxMobServBcS5ULBytes_Type = Counter64
_TmnxMobServBcS5ULBytes_Object = MibTableColumn
tmnxMobServBcS5ULBytes = _TmnxMobServBcS5ULBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 26),
    _TmnxMobServBcS5ULBytes_Type()
)
tmnxMobServBcS5ULBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5ULBytes.setStatus("current")
_TmnxMobServBcS1uDLPackets_Type = Counter64
_TmnxMobServBcS1uDLPackets_Object = MibTableColumn
tmnxMobServBcS1uDLPackets = _TmnxMobServBcS1uDLPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 27),
    _TmnxMobServBcS1uDLPackets_Type()
)
tmnxMobServBcS1uDLPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uDLPackets.setStatus("current")
_TmnxMobServBcS1uDLBytes_Type = Counter64
_TmnxMobServBcS1uDLBytes_Object = MibTableColumn
tmnxMobServBcS1uDLBytes = _TmnxMobServBcS1uDLBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 28),
    _TmnxMobServBcS1uDLBytes_Type()
)
tmnxMobServBcS1uDLBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uDLBytes.setStatus("current")
_TmnxMobServBcS5ULPacketsLow_Type = Counter32
_TmnxMobServBcS5ULPacketsLow_Object = MibTableColumn
tmnxMobServBcS5ULPacketsLow = _TmnxMobServBcS5ULPacketsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 29),
    _TmnxMobServBcS5ULPacketsLow_Type()
)
tmnxMobServBcS5ULPacketsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5ULPacketsLow.setStatus("current")
_TmnxMobServBcS5ULPacketsHigh_Type = Counter32
_TmnxMobServBcS5ULPacketsHigh_Object = MibTableColumn
tmnxMobServBcS5ULPacketsHigh = _TmnxMobServBcS5ULPacketsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 30),
    _TmnxMobServBcS5ULPacketsHigh_Type()
)
tmnxMobServBcS5ULPacketsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5ULPacketsHigh.setStatus("current")
_TmnxMobServBcS5ULBytesLow_Type = Counter32
_TmnxMobServBcS5ULBytesLow_Object = MibTableColumn
tmnxMobServBcS5ULBytesLow = _TmnxMobServBcS5ULBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 31),
    _TmnxMobServBcS5ULBytesLow_Type()
)
tmnxMobServBcS5ULBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5ULBytesLow.setStatus("current")
_TmnxMobServBcS5ULBytesHigh_Type = Counter32
_TmnxMobServBcS5ULBytesHigh_Object = MibTableColumn
tmnxMobServBcS5ULBytesHigh = _TmnxMobServBcS5ULBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 32),
    _TmnxMobServBcS5ULBytesHigh_Type()
)
tmnxMobServBcS5ULBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS5ULBytesHigh.setStatus("current")
_TmnxMobServBcS1uDLPacketsLow_Type = Counter32
_TmnxMobServBcS1uDLPacketsLow_Object = MibTableColumn
tmnxMobServBcS1uDLPacketsLow = _TmnxMobServBcS1uDLPacketsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 33),
    _TmnxMobServBcS1uDLPacketsLow_Type()
)
tmnxMobServBcS1uDLPacketsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uDLPacketsLow.setStatus("current")
_TmnxMobServBcS1uDLPacketsHigh_Type = Counter32
_TmnxMobServBcS1uDLPacketsHigh_Object = MibTableColumn
tmnxMobServBcS1uDLPacketsHigh = _TmnxMobServBcS1uDLPacketsHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 34),
    _TmnxMobServBcS1uDLPacketsHigh_Type()
)
tmnxMobServBcS1uDLPacketsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uDLPacketsHigh.setStatus("current")
_TmnxMobServBcS1uDLBytesLow_Type = Counter32
_TmnxMobServBcS1uDLBytesLow_Object = MibTableColumn
tmnxMobServBcS1uDLBytesLow = _TmnxMobServBcS1uDLBytesLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 35),
    _TmnxMobServBcS1uDLBytesLow_Type()
)
tmnxMobServBcS1uDLBytesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uDLBytesLow.setStatus("current")
_TmnxMobServBcS1uDLBytesHigh_Type = Counter32
_TmnxMobServBcS1uDLBytesHigh_Object = MibTableColumn
tmnxMobServBcS1uDLBytesHigh = _TmnxMobServBcS1uDLBytesHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 36),
    _TmnxMobServBcS1uDLBytesHigh_Type()
)
tmnxMobServBcS1uDLBytesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcS1uDLBytesHigh.setStatus("current")
_TmnxMobServBcSetupLatencyTime_Type = Unsigned32
_TmnxMobServBcSetupLatencyTime_Object = MibTableColumn
tmnxMobServBcSetupLatencyTime = _TmnxMobServBcSetupLatencyTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 37),
    _TmnxMobServBcSetupLatencyTime_Type()
)
tmnxMobServBcSetupLatencyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSetupLatencyTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcSetupLatencyTime.setUnits("milliseconds")
_TmnxMobServBcIndTnlRemTeid_Type = Unsigned32
_TmnxMobServBcIndTnlRemTeid_Object = MibTableColumn
tmnxMobServBcIndTnlRemTeid = _TmnxMobServBcIndTnlRemTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 38),
    _TmnxMobServBcIndTnlRemTeid_Type()
)
tmnxMobServBcIndTnlRemTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcIndTnlRemTeid.setStatus("current")
_TmnxMobServBcIndTnlRemAddrType_Type = InetAddressType
_TmnxMobServBcIndTnlRemAddrType_Object = MibTableColumn
tmnxMobServBcIndTnlRemAddrType = _TmnxMobServBcIndTnlRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 39),
    _TmnxMobServBcIndTnlRemAddrType_Type()
)
tmnxMobServBcIndTnlRemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcIndTnlRemAddrType.setStatus("current")


class _TmnxMobServBcIndTnlRemAddr_Type(InetAddress):
    """Custom type tmnxMobServBcIndTnlRemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcIndTnlRemAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcIndTnlRemAddr_Object = MibTableColumn
tmnxMobServBcIndTnlRemAddr = _TmnxMobServBcIndTnlRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 40),
    _TmnxMobServBcIndTnlRemAddr_Type()
)
tmnxMobServBcIndTnlRemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcIndTnlRemAddr.setStatus("current")
_TmnxMobServBcIndTnlLocalTeid_Type = Unsigned32
_TmnxMobServBcIndTnlLocalTeid_Object = MibTableColumn
tmnxMobServBcIndTnlLocalTeid = _TmnxMobServBcIndTnlLocalTeid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 41),
    _TmnxMobServBcIndTnlLocalTeid_Type()
)
tmnxMobServBcIndTnlLocalTeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcIndTnlLocalTeid.setStatus("current")
_TmnxMobServBcIndTnlLocalAddrType_Type = InetAddressType
_TmnxMobServBcIndTnlLocalAddrType_Object = MibTableColumn
tmnxMobServBcIndTnlLocalAddrType = _TmnxMobServBcIndTnlLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 42),
    _TmnxMobServBcIndTnlLocalAddrType_Type()
)
tmnxMobServBcIndTnlLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcIndTnlLocalAddrType.setStatus("current")


class _TmnxMobServBcIndTnlLocalAddr_Type(InetAddress):
    """Custom type tmnxMobServBcIndTnlLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcIndTnlLocalAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcIndTnlLocalAddr_Object = MibTableColumn
tmnxMobServBcIndTnlLocalAddr = _TmnxMobServBcIndTnlLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 43),
    _TmnxMobServBcIndTnlLocalAddr_Type()
)
tmnxMobServBcIndTnlLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcIndTnlLocalAddr.setStatus("current")
_TmnxMobServBcRfServerAddrType_Type = InetAddressType
_TmnxMobServBcRfServerAddrType_Object = MibTableColumn
tmnxMobServBcRfServerAddrType = _TmnxMobServBcRfServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 44),
    _TmnxMobServBcRfServerAddrType_Type()
)
tmnxMobServBcRfServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcRfServerAddrType.setStatus("current")


class _TmnxMobServBcRfServerAddr_Type(InetAddress):
    """Custom type tmnxMobServBcRfServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcRfServerAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcRfServerAddr_Object = MibTableColumn
tmnxMobServBcRfServerAddr = _TmnxMobServBcRfServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 45),
    _TmnxMobServBcRfServerAddr_Type()
)
tmnxMobServBcRfServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcRfServerAddr.setStatus("current")
_TmnxMobServBcRfServerState_Type = TmnxMobServerState
_TmnxMobServBcRfServerState_Object = MibTableColumn
tmnxMobServBcRfServerState = _TmnxMobServBcRfServerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 46),
    _TmnxMobServBcRfServerState_Type()
)
tmnxMobServBcRfServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcRfServerState.setStatus("current")
_TmnxMobServBcRfChargingProfile_Type = TmnxMobChargingProfile
_TmnxMobServBcRfChargingProfile_Object = MibTableColumn
tmnxMobServBcRfChargingProfile = _TmnxMobServBcRfChargingProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 47),
    _TmnxMobServBcRfChargingProfile_Type()
)
tmnxMobServBcRfChargingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcRfChargingProfile.setStatus("current")
_TmnxMobServBcRfTriggeredRecords_Type = Counter32
_TmnxMobServBcRfTriggeredRecords_Object = MibTableColumn
tmnxMobServBcRfTriggeredRecords = _TmnxMobServBcRfTriggeredRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 48),
    _TmnxMobServBcRfTriggeredRecords_Type()
)
tmnxMobServBcRfTriggeredRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcRfTriggeredRecords.setStatus("current")
_TmnxMobServBcRfInterimRecords_Type = Counter32
_TmnxMobServBcRfInterimRecords_Object = MibTableColumn
tmnxMobServBcRfInterimRecords = _TmnxMobServBcRfInterimRecords_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 49),
    _TmnxMobServBcRfInterimRecords_Type()
)
tmnxMobServBcRfInterimRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcRfInterimRecords.setStatus("current")
_TmnxMobServBcRefPointType_Type = TmnxMobServRefPointType
_TmnxMobServBcRefPointType_Object = MibTableColumn
tmnxMobServBcRefPointType = _TmnxMobServBcRefPointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 5, 1, 50),
    _TmnxMobServBcRefPointType_Type()
)
tmnxMobServBcRefPointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcRefPointType.setStatus("current")
_TmnxMobServBcSdfTable_Object = MibTable
tmnxMobServBcSdfTable = _TmnxMobServBcSdfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxMobServBcSdfTable.setStatus("current")
_TmnxMobServBcSdfEntry_Object = MibTableRow
tmnxMobServBcSdfEntry = _TmnxMobServBcSdfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1)
)
tmnxMobServBcSdfEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImsi"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcApn"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcPdnType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcBearerId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfPrecedence"),
)
if mibBuilder.loadTexts:
    tmnxMobServBcSdfEntry.setStatus("current")


class _TmnxMobServBcSdfPrecedence_Type(Unsigned32):
    """Custom type tmnxMobServBcSdfPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxMobServBcSdfPrecedence_Type.__name__ = "Unsigned32"
_TmnxMobServBcSdfPrecedence_Object = MibTableColumn
tmnxMobServBcSdfPrecedence = _TmnxMobServBcSdfPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1, 1),
    _TmnxMobServBcSdfPrecedence_Type()
)
tmnxMobServBcSdfPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfPrecedence.setStatus("current")
_TmnxMobServBcSdfPcrfPrecedence_Type = Unsigned32
_TmnxMobServBcSdfPcrfPrecedence_Object = MibTableColumn
tmnxMobServBcSdfPcrfPrecedence = _TmnxMobServBcSdfPcrfPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1, 2),
    _TmnxMobServBcSdfPcrfPrecedence_Type()
)
tmnxMobServBcSdfPcrfPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfPcrfPrecedence.setStatus("current")
_TmnxMobServBcSdfRuleName_Type = TmnxMobSdfRuleName
_TmnxMobServBcSdfRuleName_Object = MibTableColumn
tmnxMobServBcSdfRuleName = _TmnxMobServBcSdfRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1, 3),
    _TmnxMobServBcSdfRuleName_Type()
)
tmnxMobServBcSdfRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfRuleName.setStatus("current")
_TmnxMobServBcSdfPacketFilters_Type = Unsigned32
_TmnxMobServBcSdfPacketFilters_Object = MibTableColumn
tmnxMobServBcSdfPacketFilters = _TmnxMobServBcSdfPacketFilters_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1, 4),
    _TmnxMobServBcSdfPacketFilters_Type()
)
tmnxMobServBcSdfPacketFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfPacketFilters.setStatus("current")
_TmnxMobServBcSdfQosUlMbr_Type = Unsigned32
_TmnxMobServBcSdfQosUlMbr_Object = MibTableColumn
tmnxMobServBcSdfQosUlMbr = _TmnxMobServBcSdfQosUlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1, 5),
    _TmnxMobServBcSdfQosUlMbr_Type()
)
tmnxMobServBcSdfQosUlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfQosUlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfQosUlMbr.setUnits("Kbps")
_TmnxMobServBcSdfQosDlMbr_Type = Unsigned32
_TmnxMobServBcSdfQosDlMbr_Object = MibTableColumn
tmnxMobServBcSdfQosDlMbr = _TmnxMobServBcSdfQosDlMbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1, 6),
    _TmnxMobServBcSdfQosDlMbr_Type()
)
tmnxMobServBcSdfQosDlMbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfQosDlMbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfQosDlMbr.setUnits("Kbps")
_TmnxMobServBcSdfQosUlGbr_Type = Unsigned32
_TmnxMobServBcSdfQosUlGbr_Object = MibTableColumn
tmnxMobServBcSdfQosUlGbr = _TmnxMobServBcSdfQosUlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1, 7),
    _TmnxMobServBcSdfQosUlGbr_Type()
)
tmnxMobServBcSdfQosUlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfQosUlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfQosUlGbr.setUnits("Kbps")
_TmnxMobServBcSdfQosDlGbr_Type = Unsigned32
_TmnxMobServBcSdfQosDlGbr_Object = MibTableColumn
tmnxMobServBcSdfQosDlGbr = _TmnxMobServBcSdfQosDlGbr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 6, 1, 8),
    _TmnxMobServBcSdfQosDlGbr_Type()
)
tmnxMobServBcSdfQosDlGbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfQosDlGbr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfQosDlGbr.setUnits("Kbps")
_TmnxMobServBcSdfFilterTable_Object = MibTable
tmnxMobServBcSdfFilterTable = _TmnxMobServBcSdfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterTable.setStatus("current")
_TmnxMobServBcSdfFilterEntry_Object = MibTableRow
tmnxMobServBcSdfFilterEntry = _TmnxMobServBcSdfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1)
)
tmnxMobServBcSdfFilterEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImsi"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcApn"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcPdnType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcBearerId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfPrecedence"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterDirection"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterId"),
)
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterEntry.setStatus("current")
_TmnxMobServBcSdfFilterDirection_Type = TmnxMobSdfFilterDirection
_TmnxMobServBcSdfFilterDirection_Object = MibTableColumn
tmnxMobServBcSdfFilterDirection = _TmnxMobServBcSdfFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 1),
    _TmnxMobServBcSdfFilterDirection_Type()
)
tmnxMobServBcSdfFilterDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterDirection.setStatus("current")
_TmnxMobServBcSdfFilterId_Type = TmnxMobSdfFilter
_TmnxMobServBcSdfFilterId_Object = MibTableColumn
tmnxMobServBcSdfFilterId = _TmnxMobServBcSdfFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 2),
    _TmnxMobServBcSdfFilterId_Type()
)
tmnxMobServBcSdfFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterId.setStatus("current")
_TmnxMobServBcSdfFilterProtocol_Type = TmnxMobSdfFilterProtocol
_TmnxMobServBcSdfFilterProtocol_Object = MibTableColumn
tmnxMobServBcSdfFilterProtocol = _TmnxMobServBcSdfFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 3),
    _TmnxMobServBcSdfFilterProtocol_Type()
)
tmnxMobServBcSdfFilterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterProtocol.setStatus("current")
_TmnxMobServBcSdfFilterSrcAdrType_Type = InetAddressType
_TmnxMobServBcSdfFilterSrcAdrType_Object = MibTableColumn
tmnxMobServBcSdfFilterSrcAdrType = _TmnxMobServBcSdfFilterSrcAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 4),
    _TmnxMobServBcSdfFilterSrcAdrType_Type()
)
tmnxMobServBcSdfFilterSrcAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterSrcAdrType.setStatus("current")


class _TmnxMobServBcSdfFilterSrcAddr_Type(InetAddress):
    """Custom type tmnxMobServBcSdfFilterSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcSdfFilterSrcAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcSdfFilterSrcAddr_Object = MibTableColumn
tmnxMobServBcSdfFilterSrcAddr = _TmnxMobServBcSdfFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 5),
    _TmnxMobServBcSdfFilterSrcAddr_Type()
)
tmnxMobServBcSdfFilterSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterSrcAddr.setStatus("current")
_TmnxMobServBcSdfFilterSrcPfxLen_Type = InetAddressPrefixLength
_TmnxMobServBcSdfFilterSrcPfxLen_Object = MibTableColumn
tmnxMobServBcSdfFilterSrcPfxLen = _TmnxMobServBcSdfFilterSrcPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 6),
    _TmnxMobServBcSdfFilterSrcPfxLen_Type()
)
tmnxMobServBcSdfFilterSrcPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterSrcPfxLen.setStatus("current")
_TmnxMobServBcSdfFilterDstAdrType_Type = InetAddressType
_TmnxMobServBcSdfFilterDstAdrType_Object = MibTableColumn
tmnxMobServBcSdfFilterDstAdrType = _TmnxMobServBcSdfFilterDstAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 7),
    _TmnxMobServBcSdfFilterDstAdrType_Type()
)
tmnxMobServBcSdfFilterDstAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterDstAdrType.setStatus("current")


class _TmnxMobServBcSdfFilterDestAddr_Type(InetAddress):
    """Custom type tmnxMobServBcSdfFilterDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcSdfFilterDestAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcSdfFilterDestAddr_Object = MibTableColumn
tmnxMobServBcSdfFilterDestAddr = _TmnxMobServBcSdfFilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 8),
    _TmnxMobServBcSdfFilterDestAddr_Type()
)
tmnxMobServBcSdfFilterDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterDestAddr.setStatus("current")
_TmnxMobServBcSdfFilterDestPfxLen_Type = InetAddressPrefixLength
_TmnxMobServBcSdfFilterDestPfxLen_Object = MibTableColumn
tmnxMobServBcSdfFilterDestPfxLen = _TmnxMobServBcSdfFilterDestPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 9),
    _TmnxMobServBcSdfFilterDestPfxLen_Type()
)
tmnxMobServBcSdfFilterDestPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterDestPfxLen.setStatus("current")
_TmnxMobServBcSdfFilterSrcPorts_Type = Unsigned32
_TmnxMobServBcSdfFilterSrcPorts_Object = MibTableColumn
tmnxMobServBcSdfFilterSrcPorts = _TmnxMobServBcSdfFilterSrcPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 10),
    _TmnxMobServBcSdfFilterSrcPorts_Type()
)
tmnxMobServBcSdfFilterSrcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterSrcPorts.setStatus("current")
_TmnxMobServBcSdfFilterDestPorts_Type = Unsigned32
_TmnxMobServBcSdfFilterDestPorts_Object = MibTableColumn
tmnxMobServBcSdfFilterDestPorts = _TmnxMobServBcSdfFilterDestPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 11),
    _TmnxMobServBcSdfFilterDestPorts_Type()
)
tmnxMobServBcSdfFilterDestPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFilterDestPorts.setStatus("current")
_TmnxMobServBcSdfFirstSrcPortOper_Type = TTcpUdpPortOperator
_TmnxMobServBcSdfFirstSrcPortOper_Object = MibTableColumn
tmnxMobServBcSdfFirstSrcPortOper = _TmnxMobServBcSdfFirstSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 12),
    _TmnxMobServBcSdfFirstSrcPortOper_Type()
)
tmnxMobServBcSdfFirstSrcPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFirstSrcPortOper.setStatus("current")
_TmnxMobServBcSdfFirstSrcPortVal1_Type = TTcpUdpPort
_TmnxMobServBcSdfFirstSrcPortVal1_Object = MibTableColumn
tmnxMobServBcSdfFirstSrcPortVal1 = _TmnxMobServBcSdfFirstSrcPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 13),
    _TmnxMobServBcSdfFirstSrcPortVal1_Type()
)
tmnxMobServBcSdfFirstSrcPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFirstSrcPortVal1.setStatus("current")
_TmnxMobServBcSdfFirstSrcPortVal2_Type = TTcpUdpPort
_TmnxMobServBcSdfFirstSrcPortVal2_Object = MibTableColumn
tmnxMobServBcSdfFirstSrcPortVal2 = _TmnxMobServBcSdfFirstSrcPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 14),
    _TmnxMobServBcSdfFirstSrcPortVal2_Type()
)
tmnxMobServBcSdfFirstSrcPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFirstSrcPortVal2.setStatus("current")
_TmnxMobServBcSdfSecndSrcPortOper_Type = TTcpUdpPortOperator
_TmnxMobServBcSdfSecndSrcPortOper_Object = MibTableColumn
tmnxMobServBcSdfSecndSrcPortOper = _TmnxMobServBcSdfSecndSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 15),
    _TmnxMobServBcSdfSecndSrcPortOper_Type()
)
tmnxMobServBcSdfSecndSrcPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfSecndSrcPortOper.setStatus("current")
_TmnxMobServBcSdfSecndSrcPortVal1_Type = TTcpUdpPort
_TmnxMobServBcSdfSecndSrcPortVal1_Object = MibTableColumn
tmnxMobServBcSdfSecndSrcPortVal1 = _TmnxMobServBcSdfSecndSrcPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 16),
    _TmnxMobServBcSdfSecndSrcPortVal1_Type()
)
tmnxMobServBcSdfSecndSrcPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfSecndSrcPortVal1.setStatus("current")
_TmnxMobServBcSdfSecndSrcPortVal2_Type = TTcpUdpPort
_TmnxMobServBcSdfSecndSrcPortVal2_Object = MibTableColumn
tmnxMobServBcSdfSecndSrcPortVal2 = _TmnxMobServBcSdfSecndSrcPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 17),
    _TmnxMobServBcSdfSecndSrcPortVal2_Type()
)
tmnxMobServBcSdfSecndSrcPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfSecndSrcPortVal2.setStatus("current")
_TmnxMobServBcSdfFirstDstPortOper_Type = TTcpUdpPortOperator
_TmnxMobServBcSdfFirstDstPortOper_Object = MibTableColumn
tmnxMobServBcSdfFirstDstPortOper = _TmnxMobServBcSdfFirstDstPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 18),
    _TmnxMobServBcSdfFirstDstPortOper_Type()
)
tmnxMobServBcSdfFirstDstPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFirstDstPortOper.setStatus("current")
_TmnxMobServBcSdfFirstDstPortVal1_Type = TTcpUdpPort
_TmnxMobServBcSdfFirstDstPortVal1_Object = MibTableColumn
tmnxMobServBcSdfFirstDstPortVal1 = _TmnxMobServBcSdfFirstDstPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 19),
    _TmnxMobServBcSdfFirstDstPortVal1_Type()
)
tmnxMobServBcSdfFirstDstPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFirstDstPortVal1.setStatus("current")
_TmnxMobServBcSdfFirstDstPortVal2_Type = TTcpUdpPort
_TmnxMobServBcSdfFirstDstPortVal2_Object = MibTableColumn
tmnxMobServBcSdfFirstDstPortVal2 = _TmnxMobServBcSdfFirstDstPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 20),
    _TmnxMobServBcSdfFirstDstPortVal2_Type()
)
tmnxMobServBcSdfFirstDstPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfFirstDstPortVal2.setStatus("current")
_TmnxMobServBcSdfSecndDstPortOper_Type = TTcpUdpPortOperator
_TmnxMobServBcSdfSecndDstPortOper_Object = MibTableColumn
tmnxMobServBcSdfSecndDstPortOper = _TmnxMobServBcSdfSecndDstPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 21),
    _TmnxMobServBcSdfSecndDstPortOper_Type()
)
tmnxMobServBcSdfSecndDstPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfSecndDstPortOper.setStatus("current")
_TmnxMobServBcSdfSecndDstPortVal1_Type = TTcpUdpPort
_TmnxMobServBcSdfSecndDstPortVal1_Object = MibTableColumn
tmnxMobServBcSdfSecndDstPortVal1 = _TmnxMobServBcSdfSecndDstPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 22),
    _TmnxMobServBcSdfSecndDstPortVal1_Type()
)
tmnxMobServBcSdfSecndDstPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfSecndDstPortVal1.setStatus("current")
_TmnxMobServBcSdfSecndDstPortVal2_Type = TTcpUdpPort
_TmnxMobServBcSdfSecndDstPortVal2_Object = MibTableColumn
tmnxMobServBcSdfSecndDstPortVal2 = _TmnxMobServBcSdfSecndDstPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 7, 1, 23),
    _TmnxMobServBcSdfSecndDstPortVal2_Type()
)
tmnxMobServBcSdfSecndDstPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcSdfSecndDstPortVal2.setStatus("current")
_TmnxMobServBcTftFilterTable_Object = MibTable
tmnxMobServBcTftFilterTable = _TmnxMobServBcTftFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterTable.setStatus("current")
_TmnxMobServBcTftFilterEntry_Object = MibTableRow
tmnxMobServBcTftFilterEntry = _TmnxMobServBcTftFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1)
)
tmnxMobServBcTftFilterEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImsi"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcApn"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcPdnType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcBearerId"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterDirection"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterId"),
)
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterEntry.setStatus("current")
_TmnxMobServBcTftFilterDirection_Type = TmnxMobSdfFilterDirection
_TmnxMobServBcTftFilterDirection_Object = MibTableColumn
tmnxMobServBcTftFilterDirection = _TmnxMobServBcTftFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 1),
    _TmnxMobServBcTftFilterDirection_Type()
)
tmnxMobServBcTftFilterDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterDirection.setStatus("current")
_TmnxMobServBcTftFilterId_Type = TmnxMobSdfFilter
_TmnxMobServBcTftFilterId_Object = MibTableColumn
tmnxMobServBcTftFilterId = _TmnxMobServBcTftFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 2),
    _TmnxMobServBcTftFilterId_Type()
)
tmnxMobServBcTftFilterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterId.setStatus("current")
_TmnxMobServBcTftFilterProtocol_Type = TmnxMobSdfFilterProtocol
_TmnxMobServBcTftFilterProtocol_Object = MibTableColumn
tmnxMobServBcTftFilterProtocol = _TmnxMobServBcTftFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 3),
    _TmnxMobServBcTftFilterProtocol_Type()
)
tmnxMobServBcTftFilterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterProtocol.setStatus("current")
_TmnxMobServBcTftFilterSrcAdrType_Type = InetAddressType
_TmnxMobServBcTftFilterSrcAdrType_Object = MibTableColumn
tmnxMobServBcTftFilterSrcAdrType = _TmnxMobServBcTftFilterSrcAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 4),
    _TmnxMobServBcTftFilterSrcAdrType_Type()
)
tmnxMobServBcTftFilterSrcAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterSrcAdrType.setStatus("current")


class _TmnxMobServBcTftFilterSrcAddr_Type(InetAddress):
    """Custom type tmnxMobServBcTftFilterSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcTftFilterSrcAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcTftFilterSrcAddr_Object = MibTableColumn
tmnxMobServBcTftFilterSrcAddr = _TmnxMobServBcTftFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 5),
    _TmnxMobServBcTftFilterSrcAddr_Type()
)
tmnxMobServBcTftFilterSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterSrcAddr.setStatus("current")
_TmnxMobServBcTftFilterSrcPfxLen_Type = InetAddressPrefixLength
_TmnxMobServBcTftFilterSrcPfxLen_Object = MibTableColumn
tmnxMobServBcTftFilterSrcPfxLen = _TmnxMobServBcTftFilterSrcPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 6),
    _TmnxMobServBcTftFilterSrcPfxLen_Type()
)
tmnxMobServBcTftFilterSrcPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterSrcPfxLen.setStatus("current")
_TmnxMobServBcTftFilterDstAdrType_Type = InetAddressType
_TmnxMobServBcTftFilterDstAdrType_Object = MibTableColumn
tmnxMobServBcTftFilterDstAdrType = _TmnxMobServBcTftFilterDstAdrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 7),
    _TmnxMobServBcTftFilterDstAdrType_Type()
)
tmnxMobServBcTftFilterDstAdrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterDstAdrType.setStatus("current")


class _TmnxMobServBcTftFilterDestAddr_Type(InetAddress):
    """Custom type tmnxMobServBcTftFilterDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServBcTftFilterDestAddr_Type.__name__ = "InetAddress"
_TmnxMobServBcTftFilterDestAddr_Object = MibTableColumn
tmnxMobServBcTftFilterDestAddr = _TmnxMobServBcTftFilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 8),
    _TmnxMobServBcTftFilterDestAddr_Type()
)
tmnxMobServBcTftFilterDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterDestAddr.setStatus("current")
_TmnxMobServBcTftFilterDestPfxLen_Type = InetAddressPrefixLength
_TmnxMobServBcTftFilterDestPfxLen_Object = MibTableColumn
tmnxMobServBcTftFilterDestPfxLen = _TmnxMobServBcTftFilterDestPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 9),
    _TmnxMobServBcTftFilterDestPfxLen_Type()
)
tmnxMobServBcTftFilterDestPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterDestPfxLen.setStatus("current")
_TmnxMobServBcTftFilterSrcPorts_Type = Unsigned32
_TmnxMobServBcTftFilterSrcPorts_Object = MibTableColumn
tmnxMobServBcTftFilterSrcPorts = _TmnxMobServBcTftFilterSrcPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 10),
    _TmnxMobServBcTftFilterSrcPorts_Type()
)
tmnxMobServBcTftFilterSrcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterSrcPorts.setStatus("current")
_TmnxMobServBcTftFilterDestPorts_Type = Unsigned32
_TmnxMobServBcTftFilterDestPorts_Object = MibTableColumn
tmnxMobServBcTftFilterDestPorts = _TmnxMobServBcTftFilterDestPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 11),
    _TmnxMobServBcTftFilterDestPorts_Type()
)
tmnxMobServBcTftFilterDestPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFilterDestPorts.setStatus("current")
_TmnxMobServBcTftFirstSrcPortOper_Type = TTcpUdpPortOperator
_TmnxMobServBcTftFirstSrcPortOper_Object = MibTableColumn
tmnxMobServBcTftFirstSrcPortOper = _TmnxMobServBcTftFirstSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 12),
    _TmnxMobServBcTftFirstSrcPortOper_Type()
)
tmnxMobServBcTftFirstSrcPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFirstSrcPortOper.setStatus("current")
_TmnxMobServBcTftFirstSrcPortVal1_Type = TTcpUdpPort
_TmnxMobServBcTftFirstSrcPortVal1_Object = MibTableColumn
tmnxMobServBcTftFirstSrcPortVal1 = _TmnxMobServBcTftFirstSrcPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 13),
    _TmnxMobServBcTftFirstSrcPortVal1_Type()
)
tmnxMobServBcTftFirstSrcPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFirstSrcPortVal1.setStatus("current")
_TmnxMobServBcTftFirstSrcPortVal2_Type = TTcpUdpPort
_TmnxMobServBcTftFirstSrcPortVal2_Object = MibTableColumn
tmnxMobServBcTftFirstSrcPortVal2 = _TmnxMobServBcTftFirstSrcPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 14),
    _TmnxMobServBcTftFirstSrcPortVal2_Type()
)
tmnxMobServBcTftFirstSrcPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFirstSrcPortVal2.setStatus("current")
_TmnxMobServBcTftSecndSrcPortOper_Type = TTcpUdpPortOperator
_TmnxMobServBcTftSecndSrcPortOper_Object = MibTableColumn
tmnxMobServBcTftSecndSrcPortOper = _TmnxMobServBcTftSecndSrcPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 15),
    _TmnxMobServBcTftSecndSrcPortOper_Type()
)
tmnxMobServBcTftSecndSrcPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftSecndSrcPortOper.setStatus("current")
_TmnxMobServBcTftSecndSrcPortVal1_Type = TTcpUdpPort
_TmnxMobServBcTftSecndSrcPortVal1_Object = MibTableColumn
tmnxMobServBcTftSecndSrcPortVal1 = _TmnxMobServBcTftSecndSrcPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 16),
    _TmnxMobServBcTftSecndSrcPortVal1_Type()
)
tmnxMobServBcTftSecndSrcPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftSecndSrcPortVal1.setStatus("current")
_TmnxMobServBcTftSecndSrcPortVal2_Type = TTcpUdpPort
_TmnxMobServBcTftSecndSrcPortVal2_Object = MibTableColumn
tmnxMobServBcTftSecndSrcPortVal2 = _TmnxMobServBcTftSecndSrcPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 17),
    _TmnxMobServBcTftSecndSrcPortVal2_Type()
)
tmnxMobServBcTftSecndSrcPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftSecndSrcPortVal2.setStatus("current")
_TmnxMobServBcTftFirstDstPortOper_Type = TTcpUdpPortOperator
_TmnxMobServBcTftFirstDstPortOper_Object = MibTableColumn
tmnxMobServBcTftFirstDstPortOper = _TmnxMobServBcTftFirstDstPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 18),
    _TmnxMobServBcTftFirstDstPortOper_Type()
)
tmnxMobServBcTftFirstDstPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFirstDstPortOper.setStatus("current")
_TmnxMobServBcTftFirstDstPortVal1_Type = TTcpUdpPort
_TmnxMobServBcTftFirstDstPortVal1_Object = MibTableColumn
tmnxMobServBcTftFirstDstPortVal1 = _TmnxMobServBcTftFirstDstPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 19),
    _TmnxMobServBcTftFirstDstPortVal1_Type()
)
tmnxMobServBcTftFirstDstPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFirstDstPortVal1.setStatus("current")
_TmnxMobServBcTftFirstDstPortVal2_Type = TTcpUdpPort
_TmnxMobServBcTftFirstDstPortVal2_Object = MibTableColumn
tmnxMobServBcTftFirstDstPortVal2 = _TmnxMobServBcTftFirstDstPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 20),
    _TmnxMobServBcTftFirstDstPortVal2_Type()
)
tmnxMobServBcTftFirstDstPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftFirstDstPortVal2.setStatus("current")
_TmnxMobServBcTftSecndDstPortOper_Type = TTcpUdpPortOperator
_TmnxMobServBcTftSecndDstPortOper_Object = MibTableColumn
tmnxMobServBcTftSecndDstPortOper = _TmnxMobServBcTftSecndDstPortOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 21),
    _TmnxMobServBcTftSecndDstPortOper_Type()
)
tmnxMobServBcTftSecndDstPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftSecndDstPortOper.setStatus("current")
_TmnxMobServBcTftSecndDstPortVal1_Type = TTcpUdpPort
_TmnxMobServBcTftSecndDstPortVal1_Object = MibTableColumn
tmnxMobServBcTftSecndDstPortVal1 = _TmnxMobServBcTftSecndDstPortVal1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 22),
    _TmnxMobServBcTftSecndDstPortVal1_Type()
)
tmnxMobServBcTftSecndDstPortVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftSecndDstPortVal1.setStatus("current")
_TmnxMobServBcTftSecndDstPortVal2_Type = TTcpUdpPort
_TmnxMobServBcTftSecndDstPortVal2_Object = MibTableColumn
tmnxMobServBcTftSecndDstPortVal2 = _TmnxMobServBcTftSecndDstPortVal2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 8, 1, 23),
    _TmnxMobServBcTftSecndDstPortVal2_Type()
)
tmnxMobServBcTftSecndDstPortVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcTftSecndDstPortVal2.setStatus("current")
_TmnxMobServGxcStatTable_Object = MibTable
tmnxMobServGxcStatTable = _TmnxMobServGxcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxMobServGxcStatTable.setStatus("current")
_TmnxMobServGxcStatEntry_Object = MibTableRow
tmnxMobServGxcStatEntry = _TmnxMobServGxcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1)
)
tmnxMobServGxcStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcPeerAddressType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcPeerAddress"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobServGxcStatEntry.setStatus("current")
_TmnxMobServGxcPeerAddressType_Type = InetAddressType
_TmnxMobServGxcPeerAddressType_Object = MibTableColumn
tmnxMobServGxcPeerAddressType = _TmnxMobServGxcPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 1),
    _TmnxMobServGxcPeerAddressType_Type()
)
tmnxMobServGxcPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServGxcPeerAddressType.setStatus("current")


class _TmnxMobServGxcPeerAddress_Type(InetAddress):
    """Custom type tmnxMobServGxcPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServGxcPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobServGxcPeerAddress_Object = MibTableColumn
tmnxMobServGxcPeerAddress = _TmnxMobServGxcPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 2),
    _TmnxMobServGxcPeerAddress_Type()
)
tmnxMobServGxcPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServGxcPeerAddress.setStatus("current")
_TmnxMobServGxcPeerPort_Type = InetPortNumber
_TmnxMobServGxcPeerPort_Object = MibTableColumn
tmnxMobServGxcPeerPort = _TmnxMobServGxcPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 3),
    _TmnxMobServGxcPeerPort_Type()
)
tmnxMobServGxcPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServGxcPeerPort.setStatus("current")
_TmnxMobServGxcStatCcr_Type = Counter32
_TmnxMobServGxcStatCcr_Object = MibTableColumn
tmnxMobServGxcStatCcr = _TmnxMobServGxcStatCcr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 4),
    _TmnxMobServGxcStatCcr_Type()
)
tmnxMobServGxcStatCcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatCcr.setStatus("current")
_TmnxMobServGxcStatCca_Type = Counter32
_TmnxMobServGxcStatCca_Object = MibTableColumn
tmnxMobServGxcStatCca = _TmnxMobServGxcStatCca_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 5),
    _TmnxMobServGxcStatCca_Type()
)
tmnxMobServGxcStatCca.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatCca.setStatus("current")
_TmnxMobServGxcStatCcrFailures_Type = Counter32
_TmnxMobServGxcStatCcrFailures_Object = MibTableColumn
tmnxMobServGxcStatCcrFailures = _TmnxMobServGxcStatCcrFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 6),
    _TmnxMobServGxcStatCcrFailures_Type()
)
tmnxMobServGxcStatCcrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatCcrFailures.setStatus("current")
_TmnxMobServGxcStatRar_Type = Counter32
_TmnxMobServGxcStatRar_Object = MibTableColumn
tmnxMobServGxcStatRar = _TmnxMobServGxcStatRar_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 7),
    _TmnxMobServGxcStatRar_Type()
)
tmnxMobServGxcStatRar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatRar.setStatus("current")
_TmnxMobServGxcStatRaa_Type = Counter32
_TmnxMobServGxcStatRaa_Object = MibTableColumn
tmnxMobServGxcStatRaa = _TmnxMobServGxcStatRaa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 8),
    _TmnxMobServGxcStatRaa_Type()
)
tmnxMobServGxcStatRaa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatRaa.setStatus("current")
_TmnxMobServGxcStatBberf_Type = Counter32
_TmnxMobServGxcStatBberf_Object = MibTableColumn
tmnxMobServGxcStatBberf = _TmnxMobServGxcStatBberf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 9),
    _TmnxMobServGxcStatBberf_Type()
)
tmnxMobServGxcStatBberf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatBberf.setStatus("current")
_TmnxMobServGxcStatRxMalformedPkt_Type = Counter32
_TmnxMobServGxcStatRxMalformedPkt_Object = MibTableColumn
tmnxMobServGxcStatRxMalformedPkt = _TmnxMobServGxcStatRxMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 10),
    _TmnxMobServGxcStatRxMalformedPkt_Type()
)
tmnxMobServGxcStatRxMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatRxMalformedPkt.setStatus("current")
_TmnxMobServGxcStatRxUnknownPkts_Type = Counter32
_TmnxMobServGxcStatRxUnknownPkts_Object = MibTableColumn
tmnxMobServGxcStatRxUnknownPkts = _TmnxMobServGxcStatRxUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 11),
    _TmnxMobServGxcStatRxUnknownPkts_Type()
)
tmnxMobServGxcStatRxUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatRxUnknownPkts.setStatus("current")
_TmnxMobServGxcStatRxMissingIePkt_Type = Counter32
_TmnxMobServGxcStatRxMissingIePkt_Object = MibTableColumn
tmnxMobServGxcStatRxMissingIePkt = _TmnxMobServGxcStatRxMissingIePkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 12),
    _TmnxMobServGxcStatRxMissingIePkt_Type()
)
tmnxMobServGxcStatRxMissingIePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatRxMissingIePkt.setStatus("current")
_TmnxMobServGxcStatStr_Type = Counter32
_TmnxMobServGxcStatStr_Object = MibTableColumn
tmnxMobServGxcStatStr = _TmnxMobServGxcStatStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 13),
    _TmnxMobServGxcStatStr_Type()
)
tmnxMobServGxcStatStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatStr.setStatus("current")
_TmnxMobServGxcStatSta_Type = Counter32
_TmnxMobServGxcStatSta_Object = MibTableColumn
tmnxMobServGxcStatSta = _TmnxMobServGxcStatSta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 14),
    _TmnxMobServGxcStatSta_Type()
)
tmnxMobServGxcStatSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatSta.setStatus("current")
_TmnxMobServGxcStatAsr_Type = Counter32
_TmnxMobServGxcStatAsr_Object = MibTableColumn
tmnxMobServGxcStatAsr = _TmnxMobServGxcStatAsr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 15),
    _TmnxMobServGxcStatAsr_Type()
)
tmnxMobServGxcStatAsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatAsr.setStatus("current")
_TmnxMobServGxcStatAsa_Type = Counter32
_TmnxMobServGxcStatAsa_Object = MibTableColumn
tmnxMobServGxcStatAsa = _TmnxMobServGxcStatAsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 16),
    _TmnxMobServGxcStatAsa_Type()
)
tmnxMobServGxcStatAsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatAsa.setStatus("current")
_TmnxMobServGxcStatCer_Type = Counter32
_TmnxMobServGxcStatCer_Object = MibTableColumn
tmnxMobServGxcStatCer = _TmnxMobServGxcStatCer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 17),
    _TmnxMobServGxcStatCer_Type()
)
tmnxMobServGxcStatCer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatCer.setStatus("current")
_TmnxMobServGxcStatCea_Type = Counter32
_TmnxMobServGxcStatCea_Object = MibTableColumn
tmnxMobServGxcStatCea = _TmnxMobServGxcStatCea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 18),
    _TmnxMobServGxcStatCea_Type()
)
tmnxMobServGxcStatCea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatCea.setStatus("current")
_TmnxMobServGxcStatDpr_Type = Counter32
_TmnxMobServGxcStatDpr_Object = MibTableColumn
tmnxMobServGxcStatDpr = _TmnxMobServGxcStatDpr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 19),
    _TmnxMobServGxcStatDpr_Type()
)
tmnxMobServGxcStatDpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatDpr.setStatus("current")
_TmnxMobServGxcStatDpa_Type = Counter32
_TmnxMobServGxcStatDpa_Object = MibTableColumn
tmnxMobServGxcStatDpa = _TmnxMobServGxcStatDpa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 20),
    _TmnxMobServGxcStatDpa_Type()
)
tmnxMobServGxcStatDpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatDpa.setStatus("current")
_TmnxMobServGxcStatDwr_Type = Counter32
_TmnxMobServGxcStatDwr_Object = MibTableColumn
tmnxMobServGxcStatDwr = _TmnxMobServGxcStatDwr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 21),
    _TmnxMobServGxcStatDwr_Type()
)
tmnxMobServGxcStatDwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatDwr.setStatus("current")
_TmnxMobServGxcStatDwa_Type = Counter32
_TmnxMobServGxcStatDwa_Object = MibTableColumn
tmnxMobServGxcStatDwa = _TmnxMobServGxcStatDwa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 22),
    _TmnxMobServGxcStatDwa_Type()
)
tmnxMobServGxcStatDwa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatDwa.setStatus("current")


class _TmnxMobServGxcStatPrProfStatus_Type(Integer32):
    """Custom type tmnxMobServGxcStatPrProfStatus based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("shutdown", 3),
          ("shutingDown", 4))
    )


_TmnxMobServGxcStatPrProfStatus_Type.__name__ = "Integer32"
_TmnxMobServGxcStatPrProfStatus_Object = MibTableColumn
tmnxMobServGxcStatPrProfStatus = _TmnxMobServGxcStatPrProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 23),
    _TmnxMobServGxcStatPrProfStatus_Type()
)
tmnxMobServGxcStatPrProfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatPrProfStatus.setStatus("current")


class _TmnxMobServGxcStatPrDetailStatus_Type(Integer32):
    """Custom type tmnxMobServGxcStatPrDetailStatus based on Integer32"""
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
        *(("error", 1),
          ("idle", 2),
          ("closed", 3),
          ("localShutdown", 4),
          ("remoteClosing", 5),
          ("waitConnack", 6),
          ("waitCea", 7),
          ("open", 8),
          ("openCoolingDown", 9),
          ("waitDns", 10))
    )


_TmnxMobServGxcStatPrDetailStatus_Type.__name__ = "Integer32"
_TmnxMobServGxcStatPrDetailStatus_Object = MibTableColumn
tmnxMobServGxcStatPrDetailStatus = _TmnxMobServGxcStatPrDetailStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 9, 1, 24),
    _TmnxMobServGxcStatPrDetailStatus_Type()
)
tmnxMobServGxcStatPrDetailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcStatPrDetailStatus.setStatus("current")
_TmnxMobServS11PeerTable_Object = MibTable
tmnxMobServS11PeerTable = _TmnxMobServS11PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10)
)
if mibBuilder.loadTexts:
    tmnxMobServS11PeerTable.setStatus("current")
_TmnxMobServS11PeerEntry_Object = MibTableRow
tmnxMobServS11PeerEntry = _TmnxMobServS11PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10, 1)
)
tmnxMobServS11PeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerAddressType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerAddress"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobServS11PeerEntry.setStatus("current")
_TmnxMobServS11PeerAddressType_Type = InetAddressType
_TmnxMobServS11PeerAddressType_Object = MibTableColumn
tmnxMobServS11PeerAddressType = _TmnxMobServS11PeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10, 1, 1),
    _TmnxMobServS11PeerAddressType_Type()
)
tmnxMobServS11PeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerAddressType.setStatus("current")


class _TmnxMobServS11PeerAddress_Type(InetAddress):
    """Custom type tmnxMobServS11PeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServS11PeerAddress_Type.__name__ = "InetAddress"
_TmnxMobServS11PeerAddress_Object = MibTableColumn
tmnxMobServS11PeerAddress = _TmnxMobServS11PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10, 1, 2),
    _TmnxMobServS11PeerAddress_Type()
)
tmnxMobServS11PeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerAddress.setStatus("current")
_TmnxMobServS11PeerPort_Type = InetPortNumber
_TmnxMobServS11PeerPort_Object = MibTableColumn
tmnxMobServS11PeerPort = _TmnxMobServS11PeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10, 1, 3),
    _TmnxMobServS11PeerPort_Type()
)
tmnxMobServS11PeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerPort.setStatus("current")
_TmnxMobServS11PeerLastChanged_Type = TimeStamp
_TmnxMobServS11PeerLastChanged_Object = MibTableColumn
tmnxMobServS11PeerLastChanged = _TmnxMobServS11PeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10, 1, 4),
    _TmnxMobServS11PeerLastChanged_Type()
)
tmnxMobServS11PeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerLastChanged.setStatus("current")
_TmnxMobServS11PeerCreateTime_Type = TimeStamp
_TmnxMobServS11PeerCreateTime_Object = MibTableColumn
tmnxMobServS11PeerCreateTime = _TmnxMobServS11PeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10, 1, 5),
    _TmnxMobServS11PeerCreateTime_Type()
)
tmnxMobServS11PeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerCreateTime.setStatus("current")
_TmnxMobServS11PeerPathMgmtState_Type = TmnxMobPathMgmtState
_TmnxMobServS11PeerPathMgmtState_Object = MibTableColumn
tmnxMobServS11PeerPathMgmtState = _TmnxMobServS11PeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10, 1, 6),
    _TmnxMobServS11PeerPathMgmtState_Type()
)
tmnxMobServS11PeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerPathMgmtState.setStatus("current")
_TmnxMobServS11PeerGatewayId_Type = TmnxMobGwId
_TmnxMobServS11PeerGatewayId_Object = MibTableColumn
tmnxMobServS11PeerGatewayId = _TmnxMobServS11PeerGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 10, 1, 7),
    _TmnxMobServS11PeerGatewayId_Type()
)
tmnxMobServS11PeerGatewayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerGatewayId.setStatus("current")
_TmnxMobServS11StatTable_Object = MibTable
tmnxMobServS11StatTable = _TmnxMobServS11StatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11)
)
if mibBuilder.loadTexts:
    tmnxMobServS11StatTable.setStatus("current")
_TmnxMobServS11StatEntry_Object = MibTableRow
tmnxMobServS11StatEntry = _TmnxMobServS11StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1)
)
tmnxMobServS11StatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerAddressType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerAddress"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobServS11StatEntry.setStatus("current")
_TmnxMobServS11StatCreateSessnReq_Type = Counter32
_TmnxMobServS11StatCreateSessnReq_Object = MibTableColumn
tmnxMobServS11StatCreateSessnReq = _TmnxMobServS11StatCreateSessnReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 1),
    _TmnxMobServS11StatCreateSessnReq_Type()
)
tmnxMobServS11StatCreateSessnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCreateSessnReq.setStatus("current")
_TmnxMobServS11StatCreateSessnRsp_Type = Counter32
_TmnxMobServS11StatCreateSessnRsp_Object = MibTableColumn
tmnxMobServS11StatCreateSessnRsp = _TmnxMobServS11StatCreateSessnRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 2),
    _TmnxMobServS11StatCreateSessnRsp_Type()
)
tmnxMobServS11StatCreateSessnRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCreateSessnRsp.setStatus("current")
_TmnxMobServS11StatDeleteSessnReq_Type = Counter32
_TmnxMobServS11StatDeleteSessnReq_Object = MibTableColumn
tmnxMobServS11StatDeleteSessnReq = _TmnxMobServS11StatDeleteSessnReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 3),
    _TmnxMobServS11StatDeleteSessnReq_Type()
)
tmnxMobServS11StatDeleteSessnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDeleteSessnReq.setStatus("current")
_TmnxMobServS11StatDeleteSessnRsp_Type = Counter32
_TmnxMobServS11StatDeleteSessnRsp_Object = MibTableColumn
tmnxMobServS11StatDeleteSessnRsp = _TmnxMobServS11StatDeleteSessnRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 4),
    _TmnxMobServS11StatDeleteSessnRsp_Type()
)
tmnxMobServS11StatDeleteSessnRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDeleteSessnRsp.setStatus("current")
_TmnxMobServS11StatCreateBearrReq_Type = Counter32
_TmnxMobServS11StatCreateBearrReq_Object = MibTableColumn
tmnxMobServS11StatCreateBearrReq = _TmnxMobServS11StatCreateBearrReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 5),
    _TmnxMobServS11StatCreateBearrReq_Type()
)
tmnxMobServS11StatCreateBearrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCreateBearrReq.setStatus("current")
_TmnxMobServS11StatCreateBearrRsp_Type = Counter32
_TmnxMobServS11StatCreateBearrRsp_Object = MibTableColumn
tmnxMobServS11StatCreateBearrRsp = _TmnxMobServS11StatCreateBearrRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 6),
    _TmnxMobServS11StatCreateBearrRsp_Type()
)
tmnxMobServS11StatCreateBearrRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCreateBearrRsp.setStatus("current")
_TmnxMobServS11StatDeleteBearrReq_Type = Counter32
_TmnxMobServS11StatDeleteBearrReq_Object = MibTableColumn
tmnxMobServS11StatDeleteBearrReq = _TmnxMobServS11StatDeleteBearrReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 7),
    _TmnxMobServS11StatDeleteBearrReq_Type()
)
tmnxMobServS11StatDeleteBearrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDeleteBearrReq.setStatus("current")
_TmnxMobServS11StatDeleteBearrRsp_Type = Counter32
_TmnxMobServS11StatDeleteBearrRsp_Object = MibTableColumn
tmnxMobServS11StatDeleteBearrRsp = _TmnxMobServS11StatDeleteBearrRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 8),
    _TmnxMobServS11StatDeleteBearrRsp_Type()
)
tmnxMobServS11StatDeleteBearrRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDeleteBearrRsp.setStatus("current")
_TmnxMobServS11StatModifyBearrReq_Type = Counter32
_TmnxMobServS11StatModifyBearrReq_Object = MibTableColumn
tmnxMobServS11StatModifyBearrReq = _TmnxMobServS11StatModifyBearrReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 9),
    _TmnxMobServS11StatModifyBearrReq_Type()
)
tmnxMobServS11StatModifyBearrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatModifyBearrReq.setStatus("current")
_TmnxMobServS11StatModifyBearrRsp_Type = Counter32
_TmnxMobServS11StatModifyBearrRsp_Object = MibTableColumn
tmnxMobServS11StatModifyBearrRsp = _TmnxMobServS11StatModifyBearrRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 10),
    _TmnxMobServS11StatModifyBearrRsp_Type()
)
tmnxMobServS11StatModifyBearrRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatModifyBearrRsp.setStatus("current")
_TmnxMobServS11StatRxEchoRequests_Type = Counter32
_TmnxMobServS11StatRxEchoRequests_Object = MibTableColumn
tmnxMobServS11StatRxEchoRequests = _TmnxMobServS11StatRxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 11),
    _TmnxMobServS11StatRxEchoRequests_Type()
)
tmnxMobServS11StatRxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRxEchoRequests.setStatus("current")
_TmnxMobServS11StatTxEchoResp_Type = Counter32
_TmnxMobServS11StatTxEchoResp_Object = MibTableColumn
tmnxMobServS11StatTxEchoResp = _TmnxMobServS11StatTxEchoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 12),
    _TmnxMobServS11StatTxEchoResp_Type()
)
tmnxMobServS11StatTxEchoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatTxEchoResp.setStatus("current")
_TmnxMobServS11StatTxEchoRequests_Type = Counter32
_TmnxMobServS11StatTxEchoRequests_Object = MibTableColumn
tmnxMobServS11StatTxEchoRequests = _TmnxMobServS11StatTxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 13),
    _TmnxMobServS11StatTxEchoRequests_Type()
)
tmnxMobServS11StatTxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatTxEchoRequests.setStatus("current")
_TmnxMobServS11StatRxEchoResp_Type = Counter32
_TmnxMobServS11StatRxEchoResp_Object = MibTableColumn
tmnxMobServS11StatRxEchoResp = _TmnxMobServS11StatRxEchoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 14),
    _TmnxMobServS11StatRxEchoResp_Type()
)
tmnxMobServS11StatRxEchoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRxEchoResp.setStatus("current")
_TmnxMobServS11StatTxDlNotify_Type = Counter32
_TmnxMobServS11StatTxDlNotify_Object = MibTableColumn
tmnxMobServS11StatTxDlNotify = _TmnxMobServS11StatTxDlNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 15),
    _TmnxMobServS11StatTxDlNotify_Type()
)
tmnxMobServS11StatTxDlNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatTxDlNotify.setStatus("current")
_TmnxMobServS11StatRxDlAcks_Type = Counter32
_TmnxMobServS11StatRxDlAcks_Object = MibTableColumn
tmnxMobServS11StatRxDlAcks = _TmnxMobServS11StatRxDlAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 16),
    _TmnxMobServS11StatRxDlAcks_Type()
)
tmnxMobServS11StatRxDlAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRxDlAcks.setStatus("current")
_TmnxMobServS11StatRxDlFailNotify_Type = Counter32
_TmnxMobServS11StatRxDlFailNotify_Object = MibTableColumn
tmnxMobServS11StatRxDlFailNotify = _TmnxMobServS11StatRxDlFailNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 17),
    _TmnxMobServS11StatRxDlFailNotify_Type()
)
tmnxMobServS11StatRxDlFailNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRxDlFailNotify.setStatus("current")
_TmnxMobServS11StatPagingSvcReq_Type = Counter32
_TmnxMobServS11StatPagingSvcReq_Object = MibTableColumn
tmnxMobServS11StatPagingSvcReq = _TmnxMobServS11StatPagingSvcReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 18),
    _TmnxMobServS11StatPagingSvcReq_Type()
)
tmnxMobServS11StatPagingSvcReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatPagingSvcReq.setStatus("obsolete")
_TmnxMobServS11StatRxMalfrmedPkts_Type = Counter32
_TmnxMobServS11StatRxMalfrmedPkts_Object = MibTableColumn
tmnxMobServS11StatRxMalfrmedPkts = _TmnxMobServS11StatRxMalfrmedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 19),
    _TmnxMobServS11StatRxMalfrmedPkts_Type()
)
tmnxMobServS11StatRxMalfrmedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRxMalfrmedPkts.setStatus("current")
_TmnxMobServS11StatRxUnknownPkts_Type = Counter32
_TmnxMobServS11StatRxUnknownPkts_Object = MibTableColumn
tmnxMobServS11StatRxUnknownPkts = _TmnxMobServS11StatRxUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 20),
    _TmnxMobServS11StatRxUnknownPkts_Type()
)
tmnxMobServS11StatRxUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRxUnknownPkts.setStatus("current")
_TmnxMobServS11StatRxMissngIePkts_Type = Counter32
_TmnxMobServS11StatRxMissngIePkts_Object = MibTableColumn
tmnxMobServS11StatRxMissngIePkts = _TmnxMobServS11StatRxMissngIePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 21),
    _TmnxMobServS11StatRxMissngIePkts_Type()
)
tmnxMobServS11StatRxMissngIePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRxMissngIePkts.setStatus("current")
_TmnxMobServS11StatPeerRestarts_Type = Counter32
_TmnxMobServS11StatPeerRestarts_Object = MibTableColumn
tmnxMobServS11StatPeerRestarts = _TmnxMobServS11StatPeerRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 22),
    _TmnxMobServS11StatPeerRestarts_Type()
)
tmnxMobServS11StatPeerRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatPeerRestarts.setStatus("current")
_TmnxMobServS11StatPeerRestartCnt_Type = Counter32
_TmnxMobServS11StatPeerRestartCnt_Object = MibTableColumn
tmnxMobServS11StatPeerRestartCnt = _TmnxMobServS11StatPeerRestartCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 23),
    _TmnxMobServS11StatPeerRestartCnt_Type()
)
tmnxMobServS11StatPeerRestartCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatPeerRestartCnt.setStatus("current")
_TmnxMobServS11StatPathMgmtFails_Type = Counter32
_TmnxMobServS11StatPathMgmtFails_Object = MibTableColumn
tmnxMobServS11StatPathMgmtFails = _TmnxMobServS11StatPathMgmtFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 24),
    _TmnxMobServS11StatPathMgmtFails_Type()
)
tmnxMobServS11StatPathMgmtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatPathMgmtFails.setStatus("current")
_TmnxMobServS11StatRelBearersReq_Type = Counter32
_TmnxMobServS11StatRelBearersReq_Object = MibTableColumn
tmnxMobServS11StatRelBearersReq = _TmnxMobServS11StatRelBearersReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 25),
    _TmnxMobServS11StatRelBearersReq_Type()
)
tmnxMobServS11StatRelBearersReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRelBearersReq.setStatus("current")
_TmnxMobServS11StatRelBearersResp_Type = Counter32
_TmnxMobServS11StatRelBearersResp_Object = MibTableColumn
tmnxMobServS11StatRelBearersResp = _TmnxMobServS11StatRelBearersResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 26),
    _TmnxMobServS11StatRelBearersResp_Type()
)
tmnxMobServS11StatRelBearersResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRelBearersResp.setStatus("current")
_TmnxMobServS11StatCrtIndrTnlReq_Type = Counter32
_TmnxMobServS11StatCrtIndrTnlReq_Object = MibTableColumn
tmnxMobServS11StatCrtIndrTnlReq = _TmnxMobServS11StatCrtIndrTnlReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 27),
    _TmnxMobServS11StatCrtIndrTnlReq_Type()
)
tmnxMobServS11StatCrtIndrTnlReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCrtIndrTnlReq.setStatus("current")
_TmnxMobServS11StatCrtIndrTnlResp_Type = Counter32
_TmnxMobServS11StatCrtIndrTnlResp_Object = MibTableColumn
tmnxMobServS11StatCrtIndrTnlResp = _TmnxMobServS11StatCrtIndrTnlResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 28),
    _TmnxMobServS11StatCrtIndrTnlResp_Type()
)
tmnxMobServS11StatCrtIndrTnlResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCrtIndrTnlResp.setStatus("current")
_TmnxMobServS11StatDelIndrTnlReq_Type = Counter32
_TmnxMobServS11StatDelIndrTnlReq_Object = MibTableColumn
tmnxMobServS11StatDelIndrTnlReq = _TmnxMobServS11StatDelIndrTnlReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 29),
    _TmnxMobServS11StatDelIndrTnlReq_Type()
)
tmnxMobServS11StatDelIndrTnlReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDelIndrTnlReq.setStatus("current")
_TmnxMobServS11StatDelIndrTnlResp_Type = Counter32
_TmnxMobServS11StatDelIndrTnlResp_Object = MibTableColumn
tmnxMobServS11StatDelIndrTnlResp = _TmnxMobServS11StatDelIndrTnlResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 30),
    _TmnxMobServS11StatDelIndrTnlResp_Type()
)
tmnxMobServS11StatDelIndrTnlResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDelIndrTnlResp.setStatus("current")
_TmnxMobServS11StatBearersIpv4_Type = Gauge32
_TmnxMobServS11StatBearersIpv4_Object = MibTableColumn
tmnxMobServS11StatBearersIpv4 = _TmnxMobServS11StatBearersIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 31),
    _TmnxMobServS11StatBearersIpv4_Type()
)
tmnxMobServS11StatBearersIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatBearersIpv4.setStatus("obsolete")
_TmnxMobServS11StatBearersIpv6_Type = Gauge32
_TmnxMobServS11StatBearersIpv6_Object = MibTableColumn
tmnxMobServS11StatBearersIpv6 = _TmnxMobServS11StatBearersIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 32),
    _TmnxMobServS11StatBearersIpv6_Type()
)
tmnxMobServS11StatBearersIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatBearersIpv6.setStatus("obsolete")
_TmnxMobServS11StatBearerIpv4v6_Type = Gauge32
_TmnxMobServS11StatBearerIpv4v6_Object = MibTableColumn
tmnxMobServS11StatBearerIpv4v6 = _TmnxMobServS11StatBearerIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 33),
    _TmnxMobServS11StatBearerIpv4v6_Type()
)
tmnxMobServS11StatBearerIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatBearerIpv4v6.setStatus("obsolete")
_TmnxMobServS11StatDedctdBearers_Type = Gauge32
_TmnxMobServS11StatDedctdBearers_Object = MibTableColumn
tmnxMobServS11StatDedctdBearers = _TmnxMobServS11StatDedctdBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 34),
    _TmnxMobServS11StatDedctdBearers_Type()
)
tmnxMobServS11StatDedctdBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDedctdBearers.setStatus("obsolete")
_TmnxMobServS11StatBearers_Type = Gauge32
_TmnxMobServS11StatBearers_Object = MibTableColumn
tmnxMobServS11StatBearers = _TmnxMobServS11StatBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 35),
    _TmnxMobServS11StatBearers_Type()
)
tmnxMobServS11StatBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatBearers.setStatus("current")
_TmnxMobServS11StatDefBearers_Type = Gauge32
_TmnxMobServS11StatDefBearers_Object = MibTableColumn
tmnxMobServS11StatDefBearers = _TmnxMobServS11StatDefBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 36),
    _TmnxMobServS11StatDefBearers_Type()
)
tmnxMobServS11StatDefBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDefBearers.setStatus("obsolete")
_TmnxMobServS11StatRoamers_Type = Gauge32
_TmnxMobServS11StatRoamers_Object = MibTableColumn
tmnxMobServS11StatRoamers = _TmnxMobServS11StatRoamers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 37),
    _TmnxMobServS11StatRoamers_Type()
)
tmnxMobServS11StatRoamers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRoamers.setStatus("obsolete")
_TmnxMobServS11StatActiveBearers_Type = Gauge32
_TmnxMobServS11StatActiveBearers_Object = MibTableColumn
tmnxMobServS11StatActiveBearers = _TmnxMobServS11StatActiveBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 38),
    _TmnxMobServS11StatActiveBearers_Type()
)
tmnxMobServS11StatActiveBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatActiveBearers.setStatus("obsolete")
_TmnxMobServS11StatIdleBearers_Type = Gauge32
_TmnxMobServS11StatIdleBearers_Object = MibTableColumn
tmnxMobServS11StatIdleBearers = _TmnxMobServS11StatIdleBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 39),
    _TmnxMobServS11StatIdleBearers_Type()
)
tmnxMobServS11StatIdleBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatIdleBearers.setStatus("obsolete")
_TmnxMobServS11StatUpdateBearrReq_Type = Counter32
_TmnxMobServS11StatUpdateBearrReq_Object = MibTableColumn
tmnxMobServS11StatUpdateBearrReq = _TmnxMobServS11StatUpdateBearrReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 40),
    _TmnxMobServS11StatUpdateBearrReq_Type()
)
tmnxMobServS11StatUpdateBearrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatUpdateBearrReq.setStatus("current")
_TmnxMobServS11StatUpdateBearrRsp_Type = Counter32
_TmnxMobServS11StatUpdateBearrRsp_Object = MibTableColumn
tmnxMobServS11StatUpdateBearrRsp = _TmnxMobServS11StatUpdateBearrRsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 41),
    _TmnxMobServS11StatUpdateBearrRsp_Type()
)
tmnxMobServS11StatUpdateBearrRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatUpdateBearrRsp.setStatus("current")
_TmnxMobServS11StatModifyBearrCmd_Type = Counter32
_TmnxMobServS11StatModifyBearrCmd_Object = MibTableColumn
tmnxMobServS11StatModifyBearrCmd = _TmnxMobServS11StatModifyBearrCmd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 42),
    _TmnxMobServS11StatModifyBearrCmd_Type()
)
tmnxMobServS11StatModifyBearrCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatModifyBearrCmd.setStatus("current")
_TmnxMobServS11StatModifyBearrFlr_Type = Counter32
_TmnxMobServS11StatModifyBearrFlr_Object = MibTableColumn
tmnxMobServS11StatModifyBearrFlr = _TmnxMobServS11StatModifyBearrFlr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 43),
    _TmnxMobServS11StatModifyBearrFlr_Type()
)
tmnxMobServS11StatModifyBearrFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatModifyBearrFlr.setStatus("current")
_TmnxMobServS11StatDeleteBearrCmd_Type = Counter32
_TmnxMobServS11StatDeleteBearrCmd_Object = MibTableColumn
tmnxMobServS11StatDeleteBearrCmd = _TmnxMobServS11StatDeleteBearrCmd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 44),
    _TmnxMobServS11StatDeleteBearrCmd_Type()
)
tmnxMobServS11StatDeleteBearrCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDeleteBearrCmd.setStatus("current")
_TmnxMobServS11StatDeleteBearrFlr_Type = Counter32
_TmnxMobServS11StatDeleteBearrFlr_Object = MibTableColumn
tmnxMobServS11StatDeleteBearrFlr = _TmnxMobServS11StatDeleteBearrFlr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 45),
    _TmnxMobServS11StatDeleteBearrFlr_Type()
)
tmnxMobServS11StatDeleteBearrFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDeleteBearrFlr.setStatus("current")
_TmnxMobServS11StatBearrResCmd_Type = Counter32
_TmnxMobServS11StatBearrResCmd_Object = MibTableColumn
tmnxMobServS11StatBearrResCmd = _TmnxMobServS11StatBearrResCmd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 46),
    _TmnxMobServS11StatBearrResCmd_Type()
)
tmnxMobServS11StatBearrResCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatBearrResCmd.setStatus("current")
_TmnxMobServS11StatBrrResFailInd_Type = Counter32
_TmnxMobServS11StatBrrResFailInd_Object = MibTableColumn
tmnxMobServS11StatBrrResFailInd = _TmnxMobServS11StatBrrResFailInd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 47),
    _TmnxMobServS11StatBrrResFailInd_Type()
)
tmnxMobServS11StatBrrResFailInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatBrrResFailInd.setStatus("current")
_TmnxMobServS11StatSuspNoticeReq_Type = Counter32
_TmnxMobServS11StatSuspNoticeReq_Object = MibTableColumn
tmnxMobServS11StatSuspNoticeReq = _TmnxMobServS11StatSuspNoticeReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 48),
    _TmnxMobServS11StatSuspNoticeReq_Type()
)
tmnxMobServS11StatSuspNoticeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatSuspNoticeReq.setStatus("current")
_TmnxMobServS11StatSuspNoticeAck_Type = Counter32
_TmnxMobServS11StatSuspNoticeAck_Object = MibTableColumn
tmnxMobServS11StatSuspNoticeAck = _TmnxMobServS11StatSuspNoticeAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 49),
    _TmnxMobServS11StatSuspNoticeAck_Type()
)
tmnxMobServS11StatSuspNoticeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatSuspNoticeAck.setStatus("current")
_TmnxMobServS11StatResNoticeReq_Type = Counter32
_TmnxMobServS11StatResNoticeReq_Object = MibTableColumn
tmnxMobServS11StatResNoticeReq = _TmnxMobServS11StatResNoticeReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 50),
    _TmnxMobServS11StatResNoticeReq_Type()
)
tmnxMobServS11StatResNoticeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatResNoticeReq.setStatus("current")
_TmnxMobServS11StatResNoticeAck_Type = Counter32
_TmnxMobServS11StatResNoticeAck_Object = MibTableColumn
tmnxMobServS11StatResNoticeAck = _TmnxMobServS11StatResNoticeAck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 51),
    _TmnxMobServS11StatResNoticeAck_Type()
)
tmnxMobServS11StatResNoticeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatResNoticeAck.setStatus("current")
_TmnxMobServS11StatDelSesnRspFl_Type = Counter32
_TmnxMobServS11StatDelSesnRspFl_Object = MibTableColumn
tmnxMobServS11StatDelSesnRspFl = _TmnxMobServS11StatDelSesnRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 52),
    _TmnxMobServS11StatDelSesnRspFl_Type()
)
tmnxMobServS11StatDelSesnRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDelSesnRspFl.setStatus("current")
_TmnxMobServS11StatUpdtBearrRspFl_Type = Counter32
_TmnxMobServS11StatUpdtBearrRspFl_Object = MibTableColumn
tmnxMobServS11StatUpdtBearrRspFl = _TmnxMobServS11StatUpdtBearrRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 53),
    _TmnxMobServS11StatUpdtBearrRspFl_Type()
)
tmnxMobServS11StatUpdtBearrRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatUpdtBearrRspFl.setStatus("current")
_TmnxMobServS11StatModBearrRspFl_Type = Counter32
_TmnxMobServS11StatModBearrRspFl_Object = MibTableColumn
tmnxMobServS11StatModBearrRspFl = _TmnxMobServS11StatModBearrRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 54),
    _TmnxMobServS11StatModBearrRspFl_Type()
)
tmnxMobServS11StatModBearrRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatModBearrRspFl.setStatus("current")
_TmnxMobServS11StatDelBearrRspFl_Type = Counter32
_TmnxMobServS11StatDelBearrRspFl_Object = MibTableColumn
tmnxMobServS11StatDelBearrRspFl = _TmnxMobServS11StatDelBearrRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 55),
    _TmnxMobServS11StatDelBearrRspFl_Type()
)
tmnxMobServS11StatDelBearrRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDelBearrRspFl.setStatus("current")
_TmnxMobServS11StatCreatBearRspFl_Type = Counter32
_TmnxMobServS11StatCreatBearRspFl_Object = MibTableColumn
tmnxMobServS11StatCreatBearRspFl = _TmnxMobServS11StatCreatBearRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 56),
    _TmnxMobServS11StatCreatBearRspFl_Type()
)
tmnxMobServS11StatCreatBearRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCreatBearRspFl.setStatus("current")
_TmnxMobServS11StatCreatSesnRspFl_Type = Counter32
_TmnxMobServS11StatCreatSesnRspFl_Object = MibTableColumn
tmnxMobServS11StatCreatSesnRspFl = _TmnxMobServS11StatCreatSesnRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 57),
    _TmnxMobServS11StatCreatSesnRspFl_Type()
)
tmnxMobServS11StatCreatSesnRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCreatSesnRspFl.setStatus("current")
_TmnxMobServS11StatRelBearrRespFl_Type = Counter32
_TmnxMobServS11StatRelBearrRespFl_Object = MibTableColumn
tmnxMobServS11StatRelBearrRespFl = _TmnxMobServS11StatRelBearrRespFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 58),
    _TmnxMobServS11StatRelBearrRespFl_Type()
)
tmnxMobServS11StatRelBearrRespFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRelBearrRespFl.setStatus("current")
_TmnxMobServS11StatCrtIndTnlRspFl_Type = Counter32
_TmnxMobServS11StatCrtIndTnlRspFl_Object = MibTableColumn
tmnxMobServS11StatCrtIndTnlRspFl = _TmnxMobServS11StatCrtIndTnlRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 59),
    _TmnxMobServS11StatCrtIndTnlRspFl_Type()
)
tmnxMobServS11StatCrtIndTnlRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatCrtIndTnlRspFl.setStatus("current")
_TmnxMobServS11StatDelIndTnlRspFl_Type = Counter32
_TmnxMobServS11StatDelIndTnlRspFl_Object = MibTableColumn
tmnxMobServS11StatDelIndTnlRspFl = _TmnxMobServS11StatDelIndTnlRspFl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 60),
    _TmnxMobServS11StatDelIndTnlRspFl_Type()
)
tmnxMobServS11StatDelIndTnlRspFl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatDelIndTnlRspFl.setStatus("current")
_TmnxMobServS11StatRxDlAcksFail_Type = Counter32
_TmnxMobServS11StatRxDlAcksFail_Object = MibTableColumn
tmnxMobServS11StatRxDlAcksFail = _TmnxMobServS11StatRxDlAcksFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 11, 1, 61),
    _TmnxMobServS11StatRxDlAcksFail_Type()
)
tmnxMobServS11StatRxDlAcksFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11StatRxDlAcksFail.setStatus("current")
_TmnxMobServS1uPeerTable_Object = MibTable
tmnxMobServS1uPeerTable = _TmnxMobServS1uPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12)
)
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerTable.setStatus("current")
_TmnxMobServS1uPeerEntry_Object = MibTableRow
tmnxMobServS1uPeerEntry = _TmnxMobServS1uPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12, 1)
)
tmnxMobServS1uPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerAddressType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerAddress"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerPort"),
)
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerEntry.setStatus("current")
_TmnxMobServS1uPeerAddressType_Type = InetAddressType
_TmnxMobServS1uPeerAddressType_Object = MibTableColumn
tmnxMobServS1uPeerAddressType = _TmnxMobServS1uPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12, 1, 1),
    _TmnxMobServS1uPeerAddressType_Type()
)
tmnxMobServS1uPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerAddressType.setStatus("current")


class _TmnxMobServS1uPeerAddress_Type(InetAddress):
    """Custom type tmnxMobServS1uPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobServS1uPeerAddress_Type.__name__ = "InetAddress"
_TmnxMobServS1uPeerAddress_Object = MibTableColumn
tmnxMobServS1uPeerAddress = _TmnxMobServS1uPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12, 1, 2),
    _TmnxMobServS1uPeerAddress_Type()
)
tmnxMobServS1uPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerAddress.setStatus("current")
_TmnxMobServS1uPeerPort_Type = InetPortNumber
_TmnxMobServS1uPeerPort_Object = MibTableColumn
tmnxMobServS1uPeerPort = _TmnxMobServS1uPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12, 1, 3),
    _TmnxMobServS1uPeerPort_Type()
)
tmnxMobServS1uPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerPort.setStatus("current")
_TmnxMobServS1uPeerLastChanged_Type = TimeStamp
_TmnxMobServS1uPeerLastChanged_Object = MibTableColumn
tmnxMobServS1uPeerLastChanged = _TmnxMobServS1uPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12, 1, 4),
    _TmnxMobServS1uPeerLastChanged_Type()
)
tmnxMobServS1uPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerLastChanged.setStatus("current")
_TmnxMobServS1uPeerCreateTime_Type = TimeStamp
_TmnxMobServS1uPeerCreateTime_Object = MibTableColumn
tmnxMobServS1uPeerCreateTime = _TmnxMobServS1uPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12, 1, 5),
    _TmnxMobServS1uPeerCreateTime_Type()
)
tmnxMobServS1uPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerCreateTime.setStatus("current")
_TmnxMobServS1uPeerPathMgmtState_Type = TmnxMobPathMgmtState
_TmnxMobServS1uPeerPathMgmtState_Object = MibTableColumn
tmnxMobServS1uPeerPathMgmtState = _TmnxMobServS1uPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12, 1, 6),
    _TmnxMobServS1uPeerPathMgmtState_Type()
)
tmnxMobServS1uPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerPathMgmtState.setStatus("current")
_TmnxMobServS1uPeerGatewayId_Type = TmnxMobGwId
_TmnxMobServS1uPeerGatewayId_Object = MibTableColumn
tmnxMobServS1uPeerGatewayId = _TmnxMobServS1uPeerGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 12, 1, 7),
    _TmnxMobServS1uPeerGatewayId_Type()
)
tmnxMobServS1uPeerGatewayId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerGatewayId.setStatus("current")
_TmnxMobServS1uStatTable_Object = MibTable
tmnxMobServS1uStatTable = _TmnxMobServS1uStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13)
)
if mibBuilder.loadTexts:
    tmnxMobServS1uStatTable.setStatus("current")
_TmnxMobServS1uStatEntry_Object = MibTableRow
tmnxMobServS1uStatEntry = _TmnxMobServS1uStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1)
)
tmnxMobServS1uStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerAddressType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerAddress"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobServS1uStatEntry.setStatus("current")
_TmnxMobServS1uStatBcNotFound_Type = Counter32
_TmnxMobServS1uStatBcNotFound_Object = MibTableColumn
tmnxMobServS1uStatBcNotFound = _TmnxMobServS1uStatBcNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 1),
    _TmnxMobServS1uStatBcNotFound_Type()
)
tmnxMobServS1uStatBcNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatBcNotFound.setStatus("current")
_TmnxMobServS1uStatRxEchoRequests_Type = Counter32
_TmnxMobServS1uStatRxEchoRequests_Object = MibTableColumn
tmnxMobServS1uStatRxEchoRequests = _TmnxMobServS1uStatRxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 2),
    _TmnxMobServS1uStatRxEchoRequests_Type()
)
tmnxMobServS1uStatRxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatRxEchoRequests.setStatus("current")
_TmnxMobServS1uStatTxEchoResponse_Type = Counter32
_TmnxMobServS1uStatTxEchoResponse_Object = MibTableColumn
tmnxMobServS1uStatTxEchoResponse = _TmnxMobServS1uStatTxEchoResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 3),
    _TmnxMobServS1uStatTxEchoResponse_Type()
)
tmnxMobServS1uStatTxEchoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatTxEchoResponse.setStatus("current")
_TmnxMobServS1uStatTxEchoRequests_Type = Counter32
_TmnxMobServS1uStatTxEchoRequests_Object = MibTableColumn
tmnxMobServS1uStatTxEchoRequests = _TmnxMobServS1uStatTxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 4),
    _TmnxMobServS1uStatTxEchoRequests_Type()
)
tmnxMobServS1uStatTxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatTxEchoRequests.setStatus("current")
_TmnxMobServS1uStatRxEchoResponse_Type = Counter32
_TmnxMobServS1uStatRxEchoResponse_Object = MibTableColumn
tmnxMobServS1uStatRxEchoResponse = _TmnxMobServS1uStatRxEchoResponse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 5),
    _TmnxMobServS1uStatRxEchoResponse_Type()
)
tmnxMobServS1uStatRxEchoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatRxEchoResponse.setStatus("current")
_TmnxMobServS1uStatPeerRestarts_Type = Counter32
_TmnxMobServS1uStatPeerRestarts_Object = MibTableColumn
tmnxMobServS1uStatPeerRestarts = _TmnxMobServS1uStatPeerRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 6),
    _TmnxMobServS1uStatPeerRestarts_Type()
)
tmnxMobServS1uStatPeerRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatPeerRestarts.setStatus("current")
_TmnxMobServS1uStatPeerRestartCnt_Type = Counter32
_TmnxMobServS1uStatPeerRestartCnt_Object = MibTableColumn
tmnxMobServS1uStatPeerRestartCnt = _TmnxMobServS1uStatPeerRestartCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 7),
    _TmnxMobServS1uStatPeerRestartCnt_Type()
)
tmnxMobServS1uStatPeerRestartCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatPeerRestartCnt.setStatus("current")
_TmnxMobServS1uStatPathMgmtFails_Type = Counter32
_TmnxMobServS1uStatPathMgmtFails_Object = MibTableColumn
tmnxMobServS1uStatPathMgmtFails = _TmnxMobServS1uStatPathMgmtFails_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 8),
    _TmnxMobServS1uStatPathMgmtFails_Type()
)
tmnxMobServS1uStatPathMgmtFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatPathMgmtFails.setStatus("current")
_TmnxMobServS1uStatBearersIpv4_Type = Gauge32
_TmnxMobServS1uStatBearersIpv4_Object = MibTableColumn
tmnxMobServS1uStatBearersIpv4 = _TmnxMobServS1uStatBearersIpv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 9),
    _TmnxMobServS1uStatBearersIpv4_Type()
)
tmnxMobServS1uStatBearersIpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatBearersIpv4.setStatus("obsolete")
_TmnxMobServS1uStatBearersIpv6_Type = Gauge32
_TmnxMobServS1uStatBearersIpv6_Object = MibTableColumn
tmnxMobServS1uStatBearersIpv6 = _TmnxMobServS1uStatBearersIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 10),
    _TmnxMobServS1uStatBearersIpv6_Type()
)
tmnxMobServS1uStatBearersIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatBearersIpv6.setStatus("obsolete")
_TmnxMobServS1uStatBearerIpv4v6_Type = Gauge32
_TmnxMobServS1uStatBearerIpv4v6_Object = MibTableColumn
tmnxMobServS1uStatBearerIpv4v6 = _TmnxMobServS1uStatBearerIpv4v6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 11),
    _TmnxMobServS1uStatBearerIpv4v6_Type()
)
tmnxMobServS1uStatBearerIpv4v6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatBearerIpv4v6.setStatus("obsolete")
_TmnxMobServS1uStatDedctdBearers_Type = Gauge32
_TmnxMobServS1uStatDedctdBearers_Object = MibTableColumn
tmnxMobServS1uStatDedctdBearers = _TmnxMobServS1uStatDedctdBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 12),
    _TmnxMobServS1uStatDedctdBearers_Type()
)
tmnxMobServS1uStatDedctdBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatDedctdBearers.setStatus("obsolete")
_TmnxMobServS1uStatUlBytes_Type = Counter32
_TmnxMobServS1uStatUlBytes_Object = MibTableColumn
tmnxMobServS1uStatUlBytes = _TmnxMobServS1uStatUlBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 13),
    _TmnxMobServS1uStatUlBytes_Type()
)
tmnxMobServS1uStatUlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatUlBytes.setStatus("current")
_TmnxMobServS1uStatDlBytes_Type = Counter32
_TmnxMobServS1uStatDlBytes_Object = MibTableColumn
tmnxMobServS1uStatDlBytes = _TmnxMobServS1uStatDlBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 14),
    _TmnxMobServS1uStatDlBytes_Type()
)
tmnxMobServS1uStatDlBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatDlBytes.setStatus("current")
_TmnxMobServS1uStatUlPackets_Type = Counter32
_TmnxMobServS1uStatUlPackets_Object = MibTableColumn
tmnxMobServS1uStatUlPackets = _TmnxMobServS1uStatUlPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 15),
    _TmnxMobServS1uStatUlPackets_Type()
)
tmnxMobServS1uStatUlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatUlPackets.setStatus("current")
_TmnxMobServS1uStatDlPackets_Type = Counter32
_TmnxMobServS1uStatDlPackets_Object = MibTableColumn
tmnxMobServS1uStatDlPackets = _TmnxMobServS1uStatDlPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 16),
    _TmnxMobServS1uStatDlPackets_Type()
)
tmnxMobServS1uStatDlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatDlPackets.setStatus("current")
_TmnxMobServS1uStatBearers_Type = Gauge32
_TmnxMobServS1uStatBearers_Object = MibTableColumn
tmnxMobServS1uStatBearers = _TmnxMobServS1uStatBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 17),
    _TmnxMobServS1uStatBearers_Type()
)
tmnxMobServS1uStatBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatBearers.setStatus("current")
_TmnxMobServS1uStatDefBearers_Type = Gauge32
_TmnxMobServS1uStatDefBearers_Object = MibTableColumn
tmnxMobServS1uStatDefBearers = _TmnxMobServS1uStatDefBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 18),
    _TmnxMobServS1uStatDefBearers_Type()
)
tmnxMobServS1uStatDefBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatDefBearers.setStatus("obsolete")
_TmnxMobServS1uStatRoamers_Type = Gauge32
_TmnxMobServS1uStatRoamers_Object = MibTableColumn
tmnxMobServS1uStatRoamers = _TmnxMobServS1uStatRoamers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 19),
    _TmnxMobServS1uStatRoamers_Type()
)
tmnxMobServS1uStatRoamers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatRoamers.setStatus("obsolete")
_TmnxMobServS1uStatActiveBearers_Type = Gauge32
_TmnxMobServS1uStatActiveBearers_Object = MibTableColumn
tmnxMobServS1uStatActiveBearers = _TmnxMobServS1uStatActiveBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 20),
    _TmnxMobServS1uStatActiveBearers_Type()
)
tmnxMobServS1uStatActiveBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatActiveBearers.setStatus("obsolete")
_TmnxMobServS1uStatIdleBearers_Type = Gauge32
_TmnxMobServS1uStatIdleBearers_Object = MibTableColumn
tmnxMobServS1uStatIdleBearers = _TmnxMobServS1uStatIdleBearers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 13, 1, 21),
    _TmnxMobServS1uStatIdleBearers_Type()
)
tmnxMobServS1uStatIdleBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uStatIdleBearers.setStatus("obsolete")
_TmnxMobSgwGaPeerTable_Object = MibTable
tmnxMobSgwGaPeerTable = _TmnxMobSgwGaPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 14)
)
if mibBuilder.loadTexts:
    tmnxMobSgwGaPeerTable.setStatus("current")
_TmnxMobSgwGaPeerEntry_Object = MibTableRow
tmnxMobSgwGaPeerEntry = _TmnxMobSgwGaPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 14, 1)
)
tmnxMobSgwGaPeerEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerIndex"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatAddressType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatAddress"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatPort"),
)
if mibBuilder.loadTexts:
    tmnxMobSgwGaPeerEntry.setStatus("current")
_TmnxMobSgwGaPeerLastChanged_Type = TimeStamp
_TmnxMobSgwGaPeerLastChanged_Object = MibTableColumn
tmnxMobSgwGaPeerLastChanged = _TmnxMobSgwGaPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 14, 1, 1),
    _TmnxMobSgwGaPeerLastChanged_Type()
)
tmnxMobSgwGaPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaPeerLastChanged.setStatus("current")
_TmnxMobSgwGaPeerCreateTime_Type = TimeStamp
_TmnxMobSgwGaPeerCreateTime_Object = MibTableColumn
tmnxMobSgwGaPeerCreateTime = _TmnxMobSgwGaPeerCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 14, 1, 2),
    _TmnxMobSgwGaPeerCreateTime_Type()
)
tmnxMobSgwGaPeerCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaPeerCreateTime.setStatus("current")
_TmnxMobSgwGaPeerPathMgmtState_Type = TmnxMobDiaPathMgmtState
_TmnxMobSgwGaPeerPathMgmtState_Object = MibTableColumn
tmnxMobSgwGaPeerPathMgmtState = _TmnxMobSgwGaPeerPathMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 14, 1, 3),
    _TmnxMobSgwGaPeerPathMgmtState_Type()
)
tmnxMobSgwGaPeerPathMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaPeerPathMgmtState.setStatus("current")
_TmnxMobSgwGaPeerDetailState_Type = TmnxMobDiaDetailPathMgmtState
_TmnxMobSgwGaPeerDetailState_Object = MibTableColumn
tmnxMobSgwGaPeerDetailState = _TmnxMobSgwGaPeerDetailState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 14, 1, 4),
    _TmnxMobSgwGaPeerDetailState_Type()
)
tmnxMobSgwGaPeerDetailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaPeerDetailState.setStatus("current")
_TmnxMobSgwGaStatTable_Object = MibTable
tmnxMobSgwGaStatTable = _TmnxMobSgwGaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15)
)
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTable.setStatus("current")
_TmnxMobSgwGaStatEntry_Object = MibTableRow
tmnxMobSgwGaStatEntry = _TmnxMobSgwGaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1)
)
tmnxMobSgwGaStatEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriGrpName"),
    (0, "TIMETRA-MOBILE-PROFILE-MIB", "tmnxMobGtpPriServerIndex"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatAddressType"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatAddress"),
    (0, "TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatPort"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
)
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatEntry.setStatus("current")
_TmnxMobSgwGaStatAddressType_Type = InetAddressType
_TmnxMobSgwGaStatAddressType_Object = MibTableColumn
tmnxMobSgwGaStatAddressType = _TmnxMobSgwGaStatAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 1),
    _TmnxMobSgwGaStatAddressType_Type()
)
tmnxMobSgwGaStatAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatAddressType.setStatus("current")


class _TmnxMobSgwGaStatAddress_Type(InetAddress):
    """Custom type tmnxMobSgwGaStatAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMobSgwGaStatAddress_Type.__name__ = "InetAddress"
_TmnxMobSgwGaStatAddress_Object = MibTableColumn
tmnxMobSgwGaStatAddress = _TmnxMobSgwGaStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 2),
    _TmnxMobSgwGaStatAddress_Type()
)
tmnxMobSgwGaStatAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatAddress.setStatus("current")
_TmnxMobSgwGaStatPort_Type = InetPortNumber
_TmnxMobSgwGaStatPort_Object = MibTableColumn
tmnxMobSgwGaStatPort = _TmnxMobSgwGaStatPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 3),
    _TmnxMobSgwGaStatPort_Type()
)
tmnxMobSgwGaStatPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatPort.setStatus("current")
_TmnxMobSgwGaStatLastChanged_Type = TimeStamp
_TmnxMobSgwGaStatLastChanged_Object = MibTableColumn
tmnxMobSgwGaStatLastChanged = _TmnxMobSgwGaStatLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 4),
    _TmnxMobSgwGaStatLastChanged_Type()
)
tmnxMobSgwGaStatLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatLastChanged.setStatus("current")
_TmnxMobSgwGaStatCreateTime_Type = TimeStamp
_TmnxMobSgwGaStatCreateTime_Object = MibTableColumn
tmnxMobSgwGaStatCreateTime = _TmnxMobSgwGaStatCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 5),
    _TmnxMobSgwGaStatCreateTime_Type()
)
tmnxMobSgwGaStatCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatCreateTime.setStatus("current")
_TmnxMobSgwGaStatRxEchoRequests_Type = Counter32
_TmnxMobSgwGaStatRxEchoRequests_Object = MibTableColumn
tmnxMobSgwGaStatRxEchoRequests = _TmnxMobSgwGaStatRxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 6),
    _TmnxMobSgwGaStatRxEchoRequests_Type()
)
tmnxMobSgwGaStatRxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxEchoRequests.setStatus("current")
_TmnxMobSgwGaStatTxEchoResponses_Type = Counter32
_TmnxMobSgwGaStatTxEchoResponses_Object = MibTableColumn
tmnxMobSgwGaStatTxEchoResponses = _TmnxMobSgwGaStatTxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 7),
    _TmnxMobSgwGaStatTxEchoResponses_Type()
)
tmnxMobSgwGaStatTxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxEchoResponses.setStatus("current")
_TmnxMobSgwGaStatTxEchoRequests_Type = Counter32
_TmnxMobSgwGaStatTxEchoRequests_Object = MibTableColumn
tmnxMobSgwGaStatTxEchoRequests = _TmnxMobSgwGaStatTxEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 8),
    _TmnxMobSgwGaStatTxEchoRequests_Type()
)
tmnxMobSgwGaStatTxEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxEchoRequests.setStatus("current")
_TmnxMobSgwGaStatRxEchoResponses_Type = Counter32
_TmnxMobSgwGaStatRxEchoResponses_Object = MibTableColumn
tmnxMobSgwGaStatRxEchoResponses = _TmnxMobSgwGaStatRxEchoResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 9),
    _TmnxMobSgwGaStatRxEchoResponses_Type()
)
tmnxMobSgwGaStatRxEchoResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxEchoResponses.setStatus("current")
_TmnxMobSgwGaStatRxNodeAlRequests_Type = Counter32
_TmnxMobSgwGaStatRxNodeAlRequests_Object = MibTableColumn
tmnxMobSgwGaStatRxNodeAlRequests = _TmnxMobSgwGaStatRxNodeAlRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 10),
    _TmnxMobSgwGaStatRxNodeAlRequests_Type()
)
tmnxMobSgwGaStatRxNodeAlRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxNodeAlRequests.setStatus("current")
_TmnxMobSgwGaStatTxNodeAlResps_Type = Counter32
_TmnxMobSgwGaStatTxNodeAlResps_Object = MibTableColumn
tmnxMobSgwGaStatTxNodeAlResps = _TmnxMobSgwGaStatTxNodeAlResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 11),
    _TmnxMobSgwGaStatTxNodeAlResps_Type()
)
tmnxMobSgwGaStatTxNodeAlResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxNodeAlResps.setStatus("current")
_TmnxMobSgwGaStatTxDataRecReqs_Type = Counter32
_TmnxMobSgwGaStatTxDataRecReqs_Object = MibTableColumn
tmnxMobSgwGaStatTxDataRecReqs = _TmnxMobSgwGaStatTxDataRecReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 12),
    _TmnxMobSgwGaStatTxDataRecReqs_Type()
)
tmnxMobSgwGaStatTxDataRecReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxDataRecReqs.setStatus("current")
_TmnxMobSgwGaStatTxDataRecTferReq_Type = Counter32
_TmnxMobSgwGaStatTxDataRecTferReq_Object = MibTableColumn
tmnxMobSgwGaStatTxDataRecTferReq = _TmnxMobSgwGaStatTxDataRecTferReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 13),
    _TmnxMobSgwGaStatTxDataRecTferReq_Type()
)
tmnxMobSgwGaStatTxDataRecTferReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxDataRecTferReq.setStatus("current")
_TmnxMobSgwGaStatRetrDataRecReqs_Type = Counter32
_TmnxMobSgwGaStatRetrDataRecReqs_Object = MibTableColumn
tmnxMobSgwGaStatRetrDataRecReqs = _TmnxMobSgwGaStatRetrDataRecReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 14),
    _TmnxMobSgwGaStatRetrDataRecReqs_Type()
)
tmnxMobSgwGaStatRetrDataRecReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRetrDataRecReqs.setStatus("current")
_TmnxMobSgwGaStatRxDataRecReqs_Type = Counter32
_TmnxMobSgwGaStatRxDataRecReqs_Object = MibTableColumn
tmnxMobSgwGaStatRxDataRecReqs = _TmnxMobSgwGaStatRxDataRecReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 15),
    _TmnxMobSgwGaStatRxDataRecReqs_Type()
)
tmnxMobSgwGaStatRxDataRecReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxDataRecReqs.setStatus("current")
_TmnxMobSgwGaStatUnackDataRexReqs_Type = Counter32
_TmnxMobSgwGaStatUnackDataRexReqs_Object = MibTableColumn
tmnxMobSgwGaStatUnackDataRexReqs = _TmnxMobSgwGaStatUnackDataRexReqs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 16),
    _TmnxMobSgwGaStatUnackDataRexReqs_Type()
)
tmnxMobSgwGaStatUnackDataRexReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatUnackDataRexReqs.setStatus("current")
_TmnxMobSgwGaStatRxRedirectionReq_Type = Counter32
_TmnxMobSgwGaStatRxRedirectionReq_Object = MibTableColumn
tmnxMobSgwGaStatRxRedirectionReq = _TmnxMobSgwGaStatRxRedirectionReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 17),
    _TmnxMobSgwGaStatRxRedirectionReq_Type()
)
tmnxMobSgwGaStatRxRedirectionReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxRedirectionReq.setStatus("current")
_TmnxMobSgwGaStatTxRedrnResp_Type = Counter32
_TmnxMobSgwGaStatTxRedrnResp_Object = MibTableColumn
tmnxMobSgwGaStatTxRedrnResp = _TmnxMobSgwGaStatTxRedrnResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 18),
    _TmnxMobSgwGaStatTxRedrnResp_Type()
)
tmnxMobSgwGaStatTxRedrnResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxRedrnResp.setStatus("current")
_TmnxMobSgwGaStatRxInvalidMsgs_Type = Counter32
_TmnxMobSgwGaStatRxInvalidMsgs_Object = MibTableColumn
tmnxMobSgwGaStatRxInvalidMsgs = _TmnxMobSgwGaStatRxInvalidMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 19),
    _TmnxMobSgwGaStatRxInvalidMsgs_Type()
)
tmnxMobSgwGaStatRxInvalidMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxInvalidMsgs.setStatus("current")
_TmnxMobSgwGaStatRxVerNotSupp_Type = Counter32
_TmnxMobSgwGaStatRxVerNotSupp_Object = MibTableColumn
tmnxMobSgwGaStatRxVerNotSupp = _TmnxMobSgwGaStatRxVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 20),
    _TmnxMobSgwGaStatRxVerNotSupp_Type()
)
tmnxMobSgwGaStatRxVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxVerNotSupp.setStatus("current")
_TmnxMobSgwGaStatTxCdrTermination_Type = Counter32
_TmnxMobSgwGaStatTxCdrTermination_Object = MibTableColumn
tmnxMobSgwGaStatTxCdrTermination = _TmnxMobSgwGaStatTxCdrTermination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 21),
    _TmnxMobSgwGaStatTxCdrTermination_Type()
)
tmnxMobSgwGaStatTxCdrTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxCdrTermination.setStatus("current")
_TmnxMobSgwGaStatTxCdrMaxChngCond_Type = Counter32
_TmnxMobSgwGaStatTxCdrMaxChngCond_Object = MibTableColumn
tmnxMobSgwGaStatTxCdrMaxChngCond = _TmnxMobSgwGaStatTxCdrMaxChngCond_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 22),
    _TmnxMobSgwGaStatTxCdrMaxChngCond_Type()
)
tmnxMobSgwGaStatTxCdrMaxChngCond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxCdrMaxChngCond.setStatus("current")
_TmnxMobSgwGaStatTxCdrMsTmzChng_Type = Counter32
_TmnxMobSgwGaStatTxCdrMsTmzChng_Object = MibTableColumn
tmnxMobSgwGaStatTxCdrMsTmzChng = _TmnxMobSgwGaStatTxCdrMsTmzChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 23),
    _TmnxMobSgwGaStatTxCdrMsTmzChng_Type()
)
tmnxMobSgwGaStatTxCdrMsTmzChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxCdrMsTmzChng.setStatus("current")
_TmnxMobSgwGaStatTxCdrRatChng_Type = Counter32
_TmnxMobSgwGaStatTxCdrRatChng_Object = MibTableColumn
tmnxMobSgwGaStatTxCdrRatChng = _TmnxMobSgwGaStatTxCdrRatChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 24),
    _TmnxMobSgwGaStatTxCdrRatChng_Type()
)
tmnxMobSgwGaStatTxCdrRatChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxCdrRatChng.setStatus("current")
_TmnxMobSgwGaStatTxCdrTimeLimit_Type = Counter32
_TmnxMobSgwGaStatTxCdrTimeLimit_Object = MibTableColumn
tmnxMobSgwGaStatTxCdrTimeLimit = _TmnxMobSgwGaStatTxCdrTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 25),
    _TmnxMobSgwGaStatTxCdrTimeLimit_Type()
)
tmnxMobSgwGaStatTxCdrTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxCdrTimeLimit.setStatus("current")
_TmnxMobSgwGaStatTxCdrVolLimit_Type = Counter32
_TmnxMobSgwGaStatTxCdrVolLimit_Object = MibTableColumn
tmnxMobSgwGaStatTxCdrVolLimit = _TmnxMobSgwGaStatTxCdrVolLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 26),
    _TmnxMobSgwGaStatTxCdrVolLimit_Type()
)
tmnxMobSgwGaStatTxCdrVolLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxCdrVolLimit.setStatus("current")
_TmnxMobSgwGaStatRxCdrReqAcc_Type = Counter32
_TmnxMobSgwGaStatRxCdrReqAcc_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrReqAcc = _TmnxMobSgwGaStatRxCdrReqAcc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 27),
    _TmnxMobSgwGaStatRxCdrReqAcc_Type()
)
tmnxMobSgwGaStatRxCdrReqAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrReqAcc.setStatus("current")
_TmnxMobSgwGaStatRxCdrNoResAva_Type = Counter32
_TmnxMobSgwGaStatRxCdrNoResAva_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrNoResAva = _TmnxMobSgwGaStatRxCdrNoResAva_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 28),
    _TmnxMobSgwGaStatRxCdrNoResAva_Type()
)
tmnxMobSgwGaStatRxCdrNoResAva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrNoResAva.setStatus("current")
_TmnxMobSgwGaStatRxCdrReqNotFf_Type = Counter32
_TmnxMobSgwGaStatRxCdrReqNotFf_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrReqNotFf = _TmnxMobSgwGaStatRxCdrReqNotFf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 29),
    _TmnxMobSgwGaStatRxCdrReqNotFf_Type()
)
tmnxMobSgwGaStatRxCdrReqNotFf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrReqNotFf.setStatus("current")
_TmnxMobSgwGaStatRxCdrReqFfilled_Type = Counter32
_TmnxMobSgwGaStatRxCdrReqFfilled_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrReqFfilled = _TmnxMobSgwGaStatRxCdrReqFfilled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 30),
    _TmnxMobSgwGaStatRxCdrReqFfilled_Type()
)
tmnxMobSgwGaStatRxCdrReqFfilled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrReqFfilled.setStatus("current")
_TmnxMobSgwGaStatRxCdrDupReqFf_Type = Counter32
_TmnxMobSgwGaStatRxCdrDupReqFf_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrDupReqFf = _TmnxMobSgwGaStatRxCdrDupReqFf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 31),
    _TmnxMobSgwGaStatRxCdrDupReqFf_Type()
)
tmnxMobSgwGaStatRxCdrDupReqFf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrDupReqFf.setStatus("current")
_TmnxMobSgwGaStatRxCdrInvMsgFmat_Type = Counter32
_TmnxMobSgwGaStatRxCdrInvMsgFmat_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrInvMsgFmat = _TmnxMobSgwGaStatRxCdrInvMsgFmat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 32),
    _TmnxMobSgwGaStatRxCdrInvMsgFmat_Type()
)
tmnxMobSgwGaStatRxCdrInvMsgFmat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrInvMsgFmat.setStatus("current")
_TmnxMobSgwGaStatRxCdrVerNotSupp_Type = Counter32
_TmnxMobSgwGaStatRxCdrVerNotSupp_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrVerNotSupp = _TmnxMobSgwGaStatRxCdrVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 33),
    _TmnxMobSgwGaStatRxCdrVerNotSupp_Type()
)
tmnxMobSgwGaStatRxCdrVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrVerNotSupp.setStatus("current")
_TmnxMobSgwGaStatRxCdrSrvcNotSupp_Type = Counter32
_TmnxMobSgwGaStatRxCdrSrvcNotSupp_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrSrvcNotSupp = _TmnxMobSgwGaStatRxCdrSrvcNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 34),
    _TmnxMobSgwGaStatRxCdrSrvcNotSupp_Type()
)
tmnxMobSgwGaStatRxCdrSrvcNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrSrvcNotSupp.setStatus("current")
_TmnxMobSgwGaStatRxCdrMandIeInc_Type = Counter32
_TmnxMobSgwGaStatRxCdrMandIeInc_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrMandIeInc = _TmnxMobSgwGaStatRxCdrMandIeInc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 35),
    _TmnxMobSgwGaStatRxCdrMandIeInc_Type()
)
tmnxMobSgwGaStatRxCdrMandIeInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrMandIeInc.setStatus("current")
_TmnxMobSgwGaStatRxCdrMandIeMiss_Type = Counter32
_TmnxMobSgwGaStatRxCdrMandIeMiss_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrMandIeMiss = _TmnxMobSgwGaStatRxCdrMandIeMiss_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 36),
    _TmnxMobSgwGaStatRxCdrMandIeMiss_Type()
)
tmnxMobSgwGaStatRxCdrMandIeMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrMandIeMiss.setStatus("current")
_TmnxMobSgwGaStatRxCdrOptIeInc_Type = Counter32
_TmnxMobSgwGaStatRxCdrOptIeInc_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrOptIeInc = _TmnxMobSgwGaStatRxCdrOptIeInc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 37),
    _TmnxMobSgwGaStatRxCdrOptIeInc_Type()
)
tmnxMobSgwGaStatRxCdrOptIeInc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrOptIeInc.setStatus("current")
_TmnxMobSgwGaStatRxCdrSystemFail_Type = Counter32
_TmnxMobSgwGaStatRxCdrSystemFail_Object = MibTableColumn
tmnxMobSgwGaStatRxCdrSystemFail = _TmnxMobSgwGaStatRxCdrSystemFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 38),
    _TmnxMobSgwGaStatRxCdrSystemFail_Type()
)
tmnxMobSgwGaStatRxCdrSystemFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxCdrSystemFail.setStatus("current")
_TmnxMobSgwGaStatRtrEchoRequests_Type = Counter32
_TmnxMobSgwGaStatRtrEchoRequests_Object = MibTableColumn
tmnxMobSgwGaStatRtrEchoRequests = _TmnxMobSgwGaStatRtrEchoRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 39),
    _TmnxMobSgwGaStatRtrEchoRequests_Type()
)
tmnxMobSgwGaStatRtrEchoRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRtrEchoRequests.setStatus("current")
_TmnxMobSgwGaStatGtpPrimeFail_Type = Counter32
_TmnxMobSgwGaStatGtpPrimeFail_Object = MibTableColumn
tmnxMobSgwGaStatGtpPrimeFail = _TmnxMobSgwGaStatGtpPrimeFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 40),
    _TmnxMobSgwGaStatGtpPrimeFail_Type()
)
tmnxMobSgwGaStatGtpPrimeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatGtpPrimeFail.setStatus("current")


class _TmnxMobSgwGaStatOperState_Type(Integer32):
    """Custom type tmnxMobSgwGaStatOperState based on Integer32"""
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


_TmnxMobSgwGaStatOperState_Type.__name__ = "Integer32"
_TmnxMobSgwGaStatOperState_Object = MibTableColumn
tmnxMobSgwGaStatOperState = _TmnxMobSgwGaStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 41),
    _TmnxMobSgwGaStatOperState_Type()
)
tmnxMobSgwGaStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatOperState.setStatus("current")
_TmnxMobSgwGaStatUpTime_Type = TimeStamp
_TmnxMobSgwGaStatUpTime_Object = MibTableColumn
tmnxMobSgwGaStatUpTime = _TmnxMobSgwGaStatUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 42),
    _TmnxMobSgwGaStatUpTime_Type()
)
tmnxMobSgwGaStatUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatUpTime.setStatus("current")
_TmnxMobSgwGaStatTxNodeAlRequests_Type = Counter32
_TmnxMobSgwGaStatTxNodeAlRequests_Object = MibTableColumn
tmnxMobSgwGaStatTxNodeAlRequests = _TmnxMobSgwGaStatTxNodeAlRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 43),
    _TmnxMobSgwGaStatTxNodeAlRequests_Type()
)
tmnxMobSgwGaStatTxNodeAlRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxNodeAlRequests.setStatus("current")
_TmnxMobSgwGaStatRxNodeAlResps_Type = Counter32
_TmnxMobSgwGaStatRxNodeAlResps_Object = MibTableColumn
tmnxMobSgwGaStatRxNodeAlResps = _TmnxMobSgwGaStatRxNodeAlResps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 44),
    _TmnxMobSgwGaStatRxNodeAlResps_Type()
)
tmnxMobSgwGaStatRxNodeAlResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatRxNodeAlResps.setStatus("current")
_TmnxMobSgwGaStatNodeAlReqRetried_Type = Counter32
_TmnxMobSgwGaStatNodeAlReqRetried_Object = MibTableColumn
tmnxMobSgwGaStatNodeAlReqRetried = _TmnxMobSgwGaStatNodeAlReqRetried_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 45),
    _TmnxMobSgwGaStatNodeAlReqRetried_Type()
)
tmnxMobSgwGaStatNodeAlReqRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatNodeAlReqRetried.setStatus("current")
_TmnxMobSgwGaStatCdrsTx_Type = Counter32
_TmnxMobSgwGaStatCdrsTx_Object = MibTableColumn
tmnxMobSgwGaStatCdrsTx = _TmnxMobSgwGaStatCdrsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 46),
    _TmnxMobSgwGaStatCdrsTx_Type()
)
tmnxMobSgwGaStatCdrsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatCdrsTx.setStatus("current")
_TmnxMobSgwGaStatCdrsRx_Type = Counter32
_TmnxMobSgwGaStatCdrsRx_Object = MibTableColumn
tmnxMobSgwGaStatCdrsRx = _TmnxMobSgwGaStatCdrsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 47),
    _TmnxMobSgwGaStatCdrsRx_Type()
)
tmnxMobSgwGaStatCdrsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatCdrsRx.setStatus("current")
_TmnxMobSgwGaStatTxCdrSerNdChLmt_Type = Counter32
_TmnxMobSgwGaStatTxCdrSerNdChLmt_Object = MibTableColumn
tmnxMobSgwGaStatTxCdrSerNdChLmt = _TmnxMobSgwGaStatTxCdrSerNdChLmt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 48),
    _TmnxMobSgwGaStatTxCdrSerNdChLmt_Type()
)
tmnxMobSgwGaStatTxCdrSerNdChLmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxCdrSerNdChLmt.setStatus("current")
_TmnxMobSgwGaStatTxVerNotSupp_Type = Counter32
_TmnxMobSgwGaStatTxVerNotSupp_Object = MibTableColumn
tmnxMobSgwGaStatTxVerNotSupp = _TmnxMobSgwGaStatTxVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 49),
    _TmnxMobSgwGaStatTxVerNotSupp_Type()
)
tmnxMobSgwGaStatTxVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxVerNotSupp.setStatus("current")
_TmnxMobSgwGaStatTxCdrMgmtInterv_Type = Counter32
_TmnxMobSgwGaStatTxCdrMgmtInterv_Object = MibTableColumn
tmnxMobSgwGaStatTxCdrMgmtInterv = _TmnxMobSgwGaStatTxCdrMgmtInterv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 15, 1, 50),
    _TmnxMobSgwGaStatTxCdrMgmtInterv_Type()
)
tmnxMobSgwGaStatTxCdrMgmtInterv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaStatTxCdrMgmtInterv.setStatus("current")
_TmnxMobServThresTable_Object = MibTable
tmnxMobServThresTable = _TmnxMobServThresTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16)
)
if mibBuilder.loadTexts:
    tmnxMobServThresTable.setStatus("current")
_TmnxMobServThresEntry_Object = MibTableRow
tmnxMobServThresEntry = _TmnxMobServThresEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1)
)
tmnxMobServThresEntry.setIndexNames(
    (0, "TIMETRA-MOBILE-GATEWAY-MIB", "tmnxMobGwId"),
)
if mibBuilder.loadTexts:
    tmnxMobServThresEntry.setStatus("current")
_TmnxMobServThresLastChanged_Type = TimeStamp
_TmnxMobServThresLastChanged_Object = MibTableColumn
tmnxMobServThresLastChanged = _TmnxMobServThresLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 1),
    _TmnxMobServThresLastChanged_Type()
)
tmnxMobServThresLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresLastChanged.setStatus("current")
_TmnxMobServThresBrMgmtLmtUe_Type = Gauge32
_TmnxMobServThresBrMgmtLmtUe_Object = MibTableColumn
tmnxMobServThresBrMgmtLmtUe = _TmnxMobServThresBrMgmtLmtUe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 2),
    _TmnxMobServThresBrMgmtLmtUe_Type()
)
tmnxMobServThresBrMgmtLmtUe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtLmtUe.setStatus("current")
_TmnxMobServThresBrMgmtLmtBr_Type = Gauge32
_TmnxMobServThresBrMgmtLmtBr_Object = MibTableColumn
tmnxMobServThresBrMgmtLmtBr = _TmnxMobServThresBrMgmtLmtBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 3),
    _TmnxMobServThresBrMgmtLmtBr_Type()
)
tmnxMobServThresBrMgmtLmtBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtLmtBr.setStatus("current")
_TmnxMobServThresBrMgmtLmtDefBr_Type = Gauge32
_TmnxMobServThresBrMgmtLmtDefBr_Object = MibTableColumn
tmnxMobServThresBrMgmtLmtDefBr = _TmnxMobServThresBrMgmtLmtDefBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 4),
    _TmnxMobServThresBrMgmtLmtDefBr_Type()
)
tmnxMobServThresBrMgmtLmtDefBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtLmtDefBr.setStatus("current")
_TmnxMobServThresBrMgmtLmtDedBr_Type = Gauge32
_TmnxMobServThresBrMgmtLmtDedBr_Object = MibTableColumn
tmnxMobServThresBrMgmtLmtDedBr = _TmnxMobServThresBrMgmtLmtDedBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 5),
    _TmnxMobServThresBrMgmtLmtDedBr_Type()
)
tmnxMobServThresBrMgmtLmtDedBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtLmtDedBr.setStatus("current")
_TmnxMobServThresBrMgmtLmtActBr_Type = Gauge32
_TmnxMobServThresBrMgmtLmtActBr_Object = MibTableColumn
tmnxMobServThresBrMgmtLmtActBr = _TmnxMobServThresBrMgmtLmtActBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 6),
    _TmnxMobServThresBrMgmtLmtActBr_Type()
)
tmnxMobServThresBrMgmtLmtActBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtLmtActBr.setStatus("current")
_TmnxMobServThresBrMgmtLmtUePgd_Type = Gauge32
_TmnxMobServThresBrMgmtLmtUePgd_Object = MibTableColumn
tmnxMobServThresBrMgmtLmtUePgd = _TmnxMobServThresBrMgmtLmtUePgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 7),
    _TmnxMobServThresBrMgmtLmtUePgd_Type()
)
tmnxMobServThresBrMgmtLmtUePgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtLmtUePgd.setStatus("current")
_TmnxMobServThresBrMgmtCfsAttch_Type = Gauge32
_TmnxMobServThresBrMgmtCfsAttch_Object = MibTableColumn
tmnxMobServThresBrMgmtCfsAttch = _TmnxMobServThresBrMgmtCfsAttch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 8),
    _TmnxMobServThresBrMgmtCfsAttch_Type()
)
tmnxMobServThresBrMgmtCfsAttch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCfsAttch.setStatus("current")
_TmnxMobServThresBrMgmtCfsDedBr_Type = Gauge32
_TmnxMobServThresBrMgmtCfsDedBr_Object = MibTableColumn
tmnxMobServThresBrMgmtCfsDedBr = _TmnxMobServThresBrMgmtCfsDedBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 9),
    _TmnxMobServThresBrMgmtCfsDedBr_Type()
)
tmnxMobServThresBrMgmtCfsDedBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCfsDedBr.setStatus("current")
_TmnxMobServThresBrMgmtCfsSvrReq_Type = Gauge32
_TmnxMobServThresBrMgmtCfsSvrReq_Object = MibTableColumn
tmnxMobServThresBrMgmtCfsSvrReq = _TmnxMobServThresBrMgmtCfsSvrReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 10),
    _TmnxMobServThresBrMgmtCfsSvrReq_Type()
)
tmnxMobServThresBrMgmtCfsSvrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCfsSvrReq.setStatus("current")
_TmnxMobServThresBrMgmtCfsItaRlc_Type = Gauge32
_TmnxMobServThresBrMgmtCfsItaRlc_Object = MibTableColumn
tmnxMobServThresBrMgmtCfsItaRlc = _TmnxMobServThresBrMgmtCfsItaRlc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 11),
    _TmnxMobServThresBrMgmtCfsItaRlc_Type()
)
tmnxMobServThresBrMgmtCfsItaRlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCfsItaRlc.setStatus("current")
_TmnxMobServThresBrMgmtCfsItrRlc_Type = Gauge32
_TmnxMobServThresBrMgmtCfsItrRlc_Object = MibTableColumn
tmnxMobServThresBrMgmtCfsItrRlc = _TmnxMobServThresBrMgmtCfsItrRlc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 12),
    _TmnxMobServThresBrMgmtCfsItrRlc_Type()
)
tmnxMobServThresBrMgmtCfsItrRlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCfsItrRlc.setStatus("current")
_TmnxMobServThresBrMgmtCfsIdlRlc_Type = Gauge32
_TmnxMobServThresBrMgmtCfsIdlRlc_Object = MibTableColumn
tmnxMobServThresBrMgmtCfsIdlRlc = _TmnxMobServThresBrMgmtCfsIdlRlc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 13),
    _TmnxMobServThresBrMgmtCfsIdlRlc_Type()
)
tmnxMobServThresBrMgmtCfsIdlRlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCfsIdlRlc.setStatus("current")


class _TmnxMobServThresBrMgmtCffAttch_Type(Gauge32):
    """Custom type tmnxMobServThresBrMgmtCffAttch based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobServThresBrMgmtCffAttch_Type.__name__ = "Gauge32"
_TmnxMobServThresBrMgmtCffAttch_Object = MibTableColumn
tmnxMobServThresBrMgmtCffAttch = _TmnxMobServThresBrMgmtCffAttch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 14),
    _TmnxMobServThresBrMgmtCffAttch_Type()
)
tmnxMobServThresBrMgmtCffAttch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffAttch.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffAttch.setUnits("Percent")


class _TmnxMobServThresBrMgmtCffDedBr_Type(Gauge32):
    """Custom type tmnxMobServThresBrMgmtCffDedBr based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobServThresBrMgmtCffDedBr_Type.__name__ = "Gauge32"
_TmnxMobServThresBrMgmtCffDedBr_Object = MibTableColumn
tmnxMobServThresBrMgmtCffDedBr = _TmnxMobServThresBrMgmtCffDedBr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 15),
    _TmnxMobServThresBrMgmtCffDedBr_Type()
)
tmnxMobServThresBrMgmtCffDedBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffDedBr.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffDedBr.setUnits("Percent")


class _TmnxMobServThresBrMgmtCffPaging_Type(Gauge32):
    """Custom type tmnxMobServThresBrMgmtCffPaging based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobServThresBrMgmtCffPaging_Type.__name__ = "Gauge32"
_TmnxMobServThresBrMgmtCffPaging_Object = MibTableColumn
tmnxMobServThresBrMgmtCffPaging = _TmnxMobServThresBrMgmtCffPaging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 16),
    _TmnxMobServThresBrMgmtCffPaging_Type()
)
tmnxMobServThresBrMgmtCffPaging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffPaging.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffPaging.setUnits("Percent")


class _TmnxMobServThresBrMgmtCffHdOver_Type(Gauge32):
    """Custom type tmnxMobServThresBrMgmtCffHdOver based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobServThresBrMgmtCffHdOver_Type.__name__ = "Gauge32"
_TmnxMobServThresBrMgmtCffHdOver_Object = MibTableColumn
tmnxMobServThresBrMgmtCffHdOver = _TmnxMobServThresBrMgmtCffHdOver_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 17),
    _TmnxMobServThresBrMgmtCffHdOver_Type()
)
tmnxMobServThresBrMgmtCffHdOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffHdOver.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffHdOver.setUnits("Percent")


class _TmnxMobServThresBrMgmtCffSvrReq_Type(Gauge32):
    """Custom type tmnxMobServThresBrMgmtCffSvrReq based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobServThresBrMgmtCffSvrReq_Type.__name__ = "Gauge32"
_TmnxMobServThresBrMgmtCffSvrReq_Object = MibTableColumn
tmnxMobServThresBrMgmtCffSvrReq = _TmnxMobServThresBrMgmtCffSvrReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 18),
    _TmnxMobServThresBrMgmtCffSvrReq_Type()
)
tmnxMobServThresBrMgmtCffSvrReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffSvrReq.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffSvrReq.setUnits("Percent")


class _TmnxMobServThresBrMgmtCffSrUnavl_Type(Gauge32):
    """Custom type tmnxMobServThresBrMgmtCffSrUnavl based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxMobServThresBrMgmtCffSrUnavl_Type.__name__ = "Gauge32"
_TmnxMobServThresBrMgmtCffSrUnavl_Object = MibTableColumn
tmnxMobServThresBrMgmtCffSrUnavl = _TmnxMobServThresBrMgmtCffSrUnavl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 19),
    _TmnxMobServThresBrMgmtCffSrUnavl_Type()
)
tmnxMobServThresBrMgmtCffSrUnavl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffSrUnavl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServThresBrMgmtCffSrUnavl.setUnits("Percent")
_TmnxMobServThresBrTrfcThrptUL_Type = Gauge32
_TmnxMobServThresBrTrfcThrptUL_Object = MibTableColumn
tmnxMobServThresBrTrfcThrptUL = _TmnxMobServThresBrTrfcThrptUL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 20),
    _TmnxMobServThresBrTrfcThrptUL_Type()
)
tmnxMobServThresBrTrfcThrptUL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrTrfcThrptUL.setStatus("current")
_TmnxMobServThresBrTrfcThrptDL_Type = Gauge32
_TmnxMobServThresBrTrfcThrptDL_Object = MibTableColumn
tmnxMobServThresBrTrfcThrptDL = _TmnxMobServThresBrTrfcThrptDL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 21),
    _TmnxMobServThresBrTrfcThrptDL_Type()
)
tmnxMobServThresBrTrfcThrptDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresBrTrfcThrptDL.setStatus("current")
_TmnxMobServThresPthMgmtS5Fail_Type = Gauge32
_TmnxMobServThresPthMgmtS5Fail_Object = MibTableColumn
tmnxMobServThresPthMgmtS5Fail = _TmnxMobServThresPthMgmtS5Fail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 22),
    _TmnxMobServThresPthMgmtS5Fail_Type()
)
tmnxMobServThresPthMgmtS5Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS5Fail.setStatus("current")
_TmnxMobServThresPthMgmtS5Restart_Type = Gauge32
_TmnxMobServThresPthMgmtS5Restart_Object = MibTableColumn
tmnxMobServThresPthMgmtS5Restart = _TmnxMobServThresPthMgmtS5Restart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 23),
    _TmnxMobServThresPthMgmtS5Restart_Type()
)
tmnxMobServThresPthMgmtS5Restart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS5Restart.setStatus("current")
_TmnxMobServThresPthMgmtS5NoResp_Type = Gauge32
_TmnxMobServThresPthMgmtS5NoResp_Object = MibTableColumn
tmnxMobServThresPthMgmtS5NoResp = _TmnxMobServThresPthMgmtS5NoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 24),
    _TmnxMobServThresPthMgmtS5NoResp_Type()
)
tmnxMobServThresPthMgmtS5NoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS5NoResp.setStatus("current")
_TmnxMobServThresPthMgmtS11PrPath_Type = Gauge32
_TmnxMobServThresPthMgmtS11PrPath_Object = MibTableColumn
tmnxMobServThresPthMgmtS11PrPath = _TmnxMobServThresPthMgmtS11PrPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 25),
    _TmnxMobServThresPthMgmtS11PrPath_Type()
)
tmnxMobServThresPthMgmtS11PrPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS11PrPath.setStatus("current")
_TmnxMobServThresPthMgmtS11PrRstt_Type = Gauge32
_TmnxMobServThresPthMgmtS11PrRstt_Object = MibTableColumn
tmnxMobServThresPthMgmtS11PrRstt = _TmnxMobServThresPthMgmtS11PrRstt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 26),
    _TmnxMobServThresPthMgmtS11PrRstt_Type()
)
tmnxMobServThresPthMgmtS11PrRstt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS11PrRstt.setStatus("current")
_TmnxMobServThresPthMgmtS11NoResp_Type = Gauge32
_TmnxMobServThresPthMgmtS11NoResp_Object = MibTableColumn
tmnxMobServThresPthMgmtS11NoResp = _TmnxMobServThresPthMgmtS11NoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 27),
    _TmnxMobServThresPthMgmtS11NoResp_Type()
)
tmnxMobServThresPthMgmtS11NoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS11NoResp.setStatus("current")
_TmnxMobServThresPthMgmtS1UENB_Type = Gauge32
_TmnxMobServThresPthMgmtS1UENB_Object = MibTableColumn
tmnxMobServThresPthMgmtS1UENB = _TmnxMobServThresPthMgmtS1UENB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 28),
    _TmnxMobServThresPthMgmtS1UENB_Type()
)
tmnxMobServThresPthMgmtS1UENB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS1UENB.setStatus("current")
_TmnxMobServThresPthMgmtS11MME_Type = Gauge32
_TmnxMobServThresPthMgmtS11MME_Object = MibTableColumn
tmnxMobServThresPthMgmtS11MME = _TmnxMobServThresPthMgmtS11MME_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 29),
    _TmnxMobServThresPthMgmtS11MME_Type()
)
tmnxMobServThresPthMgmtS11MME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS11MME.setStatus("current")
_TmnxMobServThresPthMgmtS5Peer_Type = Gauge32
_TmnxMobServThresPthMgmtS5Peer_Object = MibTableColumn
tmnxMobServThresPthMgmtS5Peer = _TmnxMobServThresPthMgmtS5Peer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 30),
    _TmnxMobServThresPthMgmtS5Peer_Type()
)
tmnxMobServThresPthMgmtS5Peer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS5Peer.setStatus("current")
_TmnxMobServThresPthMgmtS8Peer_Type = Gauge32
_TmnxMobServThresPthMgmtS8Peer_Object = MibTableColumn
tmnxMobServThresPthMgmtS8Peer = _TmnxMobServThresPthMgmtS8Peer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 31),
    _TmnxMobServThresPthMgmtS8Peer_Type()
)
tmnxMobServThresPthMgmtS8Peer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtS8Peer.setStatus("current")
_TmnxMobServThresPthMgmtRfFail_Type = Gauge32
_TmnxMobServThresPthMgmtRfFail_Object = MibTableColumn
tmnxMobServThresPthMgmtRfFail = _TmnxMobServThresPthMgmtRfFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 16, 1, 32),
    _TmnxMobServThresPthMgmtRfFail_Type()
)
tmnxMobServThresPthMgmtRfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServThresPthMgmtRfFail.setStatus("current")
_TmnxMobServBcAcctGaTable_Object = MibTable
tmnxMobServBcAcctGaTable = _TmnxMobServBcAcctGaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17)
)
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaTable.setStatus("current")
_TmnxMobServBcAcctGaEntry_Object = MibTableRow
tmnxMobServBcAcctGaEntry = _TmnxMobServBcAcctGaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaEntry.setStatus("current")
_TmnxMobServBcAcctGaChargingId_Type = TmnxMobChargingProfile
_TmnxMobServBcAcctGaChargingId_Object = MibTableColumn
tmnxMobServBcAcctGaChargingId = _TmnxMobServBcAcctGaChargingId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 1),
    _TmnxMobServBcAcctGaChargingId_Type()
)
tmnxMobServBcAcctGaChargingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaChargingId.setStatus("current")
_TmnxMobServBcAcctGaUlSustRate_Type = Counter32
_TmnxMobServBcAcctGaUlSustRate_Object = MibTableColumn
tmnxMobServBcAcctGaUlSustRate = _TmnxMobServBcAcctGaUlSustRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 2),
    _TmnxMobServBcAcctGaUlSustRate_Type()
)
tmnxMobServBcAcctGaUlSustRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaUlSustRate.setStatus("current")
_TmnxMobServBcAcctGaDlSustRate_Type = Counter32
_TmnxMobServBcAcctGaDlSustRate_Object = MibTableColumn
tmnxMobServBcAcctGaDlSustRate = _TmnxMobServBcAcctGaDlSustRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 3),
    _TmnxMobServBcAcctGaDlSustRate_Type()
)
tmnxMobServBcAcctGaDlSustRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaDlSustRate.setStatus("current")
_TmnxMobServBcAcctGaAggrUlPkts_Type = Counter64
_TmnxMobServBcAcctGaAggrUlPkts_Object = MibTableColumn
tmnxMobServBcAcctGaAggrUlPkts = _TmnxMobServBcAcctGaAggrUlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 4),
    _TmnxMobServBcAcctGaAggrUlPkts_Type()
)
tmnxMobServBcAcctGaAggrUlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrUlPkts.setStatus("current")
_TmnxMobServBcAcctGaAggrUlPktsLow_Type = Counter32
_TmnxMobServBcAcctGaAggrUlPktsLow_Object = MibTableColumn
tmnxMobServBcAcctGaAggrUlPktsLow = _TmnxMobServBcAcctGaAggrUlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 5),
    _TmnxMobServBcAcctGaAggrUlPktsLow_Type()
)
tmnxMobServBcAcctGaAggrUlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrUlPktsLow.setStatus("current")
_TmnxMobServBcAcctGaAggrUlPktsHi_Type = Counter32
_TmnxMobServBcAcctGaAggrUlPktsHi_Object = MibTableColumn
tmnxMobServBcAcctGaAggrUlPktsHi = _TmnxMobServBcAcctGaAggrUlPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 6),
    _TmnxMobServBcAcctGaAggrUlPktsHi_Type()
)
tmnxMobServBcAcctGaAggrUlPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrUlPktsHi.setStatus("current")
_TmnxMobServBcAcctGaAggrDlPkts_Type = Counter64
_TmnxMobServBcAcctGaAggrDlPkts_Object = MibTableColumn
tmnxMobServBcAcctGaAggrDlPkts = _TmnxMobServBcAcctGaAggrDlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 7),
    _TmnxMobServBcAcctGaAggrDlPkts_Type()
)
tmnxMobServBcAcctGaAggrDlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrDlPkts.setStatus("current")
_TmnxMobServBcAcctGaAggrDlPktsLow_Type = Counter32
_TmnxMobServBcAcctGaAggrDlPktsLow_Object = MibTableColumn
tmnxMobServBcAcctGaAggrDlPktsLow = _TmnxMobServBcAcctGaAggrDlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 8),
    _TmnxMobServBcAcctGaAggrDlPktsLow_Type()
)
tmnxMobServBcAcctGaAggrDlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrDlPktsLow.setStatus("current")
_TmnxMobServBcAcctGaAggrDlPktsHi_Type = Counter32
_TmnxMobServBcAcctGaAggrDlPktsHi_Object = MibTableColumn
tmnxMobServBcAcctGaAggrDlPktsHi = _TmnxMobServBcAcctGaAggrDlPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 9),
    _TmnxMobServBcAcctGaAggrDlPktsHi_Type()
)
tmnxMobServBcAcctGaAggrDlPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrDlPktsHi.setStatus("current")
_TmnxMobServBcAcctGaAggrUlByts_Type = Counter64
_TmnxMobServBcAcctGaAggrUlByts_Object = MibTableColumn
tmnxMobServBcAcctGaAggrUlByts = _TmnxMobServBcAcctGaAggrUlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 10),
    _TmnxMobServBcAcctGaAggrUlByts_Type()
)
tmnxMobServBcAcctGaAggrUlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrUlByts.setStatus("current")
_TmnxMobServBcAcctGaAggrUlBytsLow_Type = Counter32
_TmnxMobServBcAcctGaAggrUlBytsLow_Object = MibTableColumn
tmnxMobServBcAcctGaAggrUlBytsLow = _TmnxMobServBcAcctGaAggrUlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 11),
    _TmnxMobServBcAcctGaAggrUlBytsLow_Type()
)
tmnxMobServBcAcctGaAggrUlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrUlBytsLow.setStatus("current")
_TmnxMobServBcAcctGaAggrUlBytsHi_Type = Counter32
_TmnxMobServBcAcctGaAggrUlBytsHi_Object = MibTableColumn
tmnxMobServBcAcctGaAggrUlBytsHi = _TmnxMobServBcAcctGaAggrUlBytsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 12),
    _TmnxMobServBcAcctGaAggrUlBytsHi_Type()
)
tmnxMobServBcAcctGaAggrUlBytsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrUlBytsHi.setStatus("current")
_TmnxMobServBcAcctGaAggrDlByts_Type = Counter64
_TmnxMobServBcAcctGaAggrDlByts_Object = MibTableColumn
tmnxMobServBcAcctGaAggrDlByts = _TmnxMobServBcAcctGaAggrDlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 13),
    _TmnxMobServBcAcctGaAggrDlByts_Type()
)
tmnxMobServBcAcctGaAggrDlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrDlByts.setStatus("current")
_TmnxMobServBcAcctGaAggrDlBytsLow_Type = Counter32
_TmnxMobServBcAcctGaAggrDlBytsLow_Object = MibTableColumn
tmnxMobServBcAcctGaAggrDlBytsLow = _TmnxMobServBcAcctGaAggrDlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 14),
    _TmnxMobServBcAcctGaAggrDlBytsLow_Type()
)
tmnxMobServBcAcctGaAggrDlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrDlBytsLow.setStatus("current")
_TmnxMobServBcAcctGaAggrDlBytsHi_Type = Counter32
_TmnxMobServBcAcctGaAggrDlBytsHi_Object = MibTableColumn
tmnxMobServBcAcctGaAggrDlBytsHi = _TmnxMobServBcAcctGaAggrDlBytsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 15),
    _TmnxMobServBcAcctGaAggrDlBytsHi_Type()
)
tmnxMobServBcAcctGaAggrDlBytsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaAggrDlBytsHi.setStatus("current")
_TmnxMobServBcAcctGaNumPartCdrs_Type = Counter32
_TmnxMobServBcAcctGaNumPartCdrs_Object = MibTableColumn
tmnxMobServBcAcctGaNumPartCdrs = _TmnxMobServBcAcctGaNumPartCdrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 16),
    _TmnxMobServBcAcctGaNumPartCdrs_Type()
)
tmnxMobServBcAcctGaNumPartCdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaNumPartCdrs.setStatus("current")
_TmnxMobServBcAcctGaNumTdvs_Type = Counter32
_TmnxMobServBcAcctGaNumTdvs_Object = MibTableColumn
tmnxMobServBcAcctGaNumTdvs = _TmnxMobServBcAcctGaNumTdvs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 17),
    _TmnxMobServBcAcctGaNumTdvs_Type()
)
tmnxMobServBcAcctGaNumTdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaNumTdvs.setStatus("current")
_TmnxMobServBcAcctGaNumMaxChanges_Type = Counter32
_TmnxMobServBcAcctGaNumMaxChanges_Object = MibTableColumn
tmnxMobServBcAcctGaNumMaxChanges = _TmnxMobServBcAcctGaNumMaxChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 17, 1, 18),
    _TmnxMobServBcAcctGaNumMaxChanges_Type()
)
tmnxMobServBcAcctGaNumMaxChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServBcAcctGaNumMaxChanges.setStatus("current")
_TmnxMobServPcAcctRfTable_Object = MibTable
tmnxMobServPcAcctRfTable = _TmnxMobServPcAcctRfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18)
)
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfTable.setStatus("current")
_TmnxMobServPcAcctRfEntry_Object = MibTableRow
tmnxMobServPcAcctRfEntry = _TmnxMobServPcAcctRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfEntry.setStatus("current")
_TmnxMobServPcAcctRfAggrUlPkts_Type = Counter64
_TmnxMobServPcAcctRfAggrUlPkts_Object = MibTableColumn
tmnxMobServPcAcctRfAggrUlPkts = _TmnxMobServPcAcctRfAggrUlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 1),
    _TmnxMobServPcAcctRfAggrUlPkts_Type()
)
tmnxMobServPcAcctRfAggrUlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrUlPkts.setStatus("current")
_TmnxMobServPcAcctRfAggrUlPktsLow_Type = Counter32
_TmnxMobServPcAcctRfAggrUlPktsLow_Object = MibTableColumn
tmnxMobServPcAcctRfAggrUlPktsLow = _TmnxMobServPcAcctRfAggrUlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 2),
    _TmnxMobServPcAcctRfAggrUlPktsLow_Type()
)
tmnxMobServPcAcctRfAggrUlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrUlPktsLow.setStatus("current")
_TmnxMobServPcAcctRfAggrUlPktsHi_Type = Counter32
_TmnxMobServPcAcctRfAggrUlPktsHi_Object = MibTableColumn
tmnxMobServPcAcctRfAggrUlPktsHi = _TmnxMobServPcAcctRfAggrUlPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 3),
    _TmnxMobServPcAcctRfAggrUlPktsHi_Type()
)
tmnxMobServPcAcctRfAggrUlPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrUlPktsHi.setStatus("current")
_TmnxMobServPcAcctRfAggrDlPkts_Type = Counter64
_TmnxMobServPcAcctRfAggrDlPkts_Object = MibTableColumn
tmnxMobServPcAcctRfAggrDlPkts = _TmnxMobServPcAcctRfAggrDlPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 4),
    _TmnxMobServPcAcctRfAggrDlPkts_Type()
)
tmnxMobServPcAcctRfAggrDlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrDlPkts.setStatus("current")
_TmnxMobServPcAcctRfAggrDlPktsLow_Type = Counter32
_TmnxMobServPcAcctRfAggrDlPktsLow_Object = MibTableColumn
tmnxMobServPcAcctRfAggrDlPktsLow = _TmnxMobServPcAcctRfAggrDlPktsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 5),
    _TmnxMobServPcAcctRfAggrDlPktsLow_Type()
)
tmnxMobServPcAcctRfAggrDlPktsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrDlPktsLow.setStatus("current")
_TmnxMobServPcAcctRfAggrDlPktsHi_Type = Counter32
_TmnxMobServPcAcctRfAggrDlPktsHi_Object = MibTableColumn
tmnxMobServPcAcctRfAggrDlPktsHi = _TmnxMobServPcAcctRfAggrDlPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 6),
    _TmnxMobServPcAcctRfAggrDlPktsHi_Type()
)
tmnxMobServPcAcctRfAggrDlPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrDlPktsHi.setStatus("current")
_TmnxMobServPcAcctRfAggrUlByts_Type = Counter64
_TmnxMobServPcAcctRfAggrUlByts_Object = MibTableColumn
tmnxMobServPcAcctRfAggrUlByts = _TmnxMobServPcAcctRfAggrUlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 7),
    _TmnxMobServPcAcctRfAggrUlByts_Type()
)
tmnxMobServPcAcctRfAggrUlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrUlByts.setStatus("current")
_TmnxMobServPcAcctRfAggrUlBytsLow_Type = Counter32
_TmnxMobServPcAcctRfAggrUlBytsLow_Object = MibTableColumn
tmnxMobServPcAcctRfAggrUlBytsLow = _TmnxMobServPcAcctRfAggrUlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 8),
    _TmnxMobServPcAcctRfAggrUlBytsLow_Type()
)
tmnxMobServPcAcctRfAggrUlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrUlBytsLow.setStatus("current")
_TmnxMobServPcAcctRfAggrUlBytsHi_Type = Counter32
_TmnxMobServPcAcctRfAggrUlBytsHi_Object = MibTableColumn
tmnxMobServPcAcctRfAggrUlBytsHi = _TmnxMobServPcAcctRfAggrUlBytsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 9),
    _TmnxMobServPcAcctRfAggrUlBytsHi_Type()
)
tmnxMobServPcAcctRfAggrUlBytsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrUlBytsHi.setStatus("current")
_TmnxMobServPcAcctRfAggrDlByts_Type = Counter64
_TmnxMobServPcAcctRfAggrDlByts_Object = MibTableColumn
tmnxMobServPcAcctRfAggrDlByts = _TmnxMobServPcAcctRfAggrDlByts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 10),
    _TmnxMobServPcAcctRfAggrDlByts_Type()
)
tmnxMobServPcAcctRfAggrDlByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrDlByts.setStatus("current")
_TmnxMobServPcAcctRfAggrDlBytsLow_Type = Counter32
_TmnxMobServPcAcctRfAggrDlBytsLow_Object = MibTableColumn
tmnxMobServPcAcctRfAggrDlBytsLow = _TmnxMobServPcAcctRfAggrDlBytsLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 11),
    _TmnxMobServPcAcctRfAggrDlBytsLow_Type()
)
tmnxMobServPcAcctRfAggrDlBytsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrDlBytsLow.setStatus("current")
_TmnxMobServPcAcctRfAggrDlBytsHi_Type = Counter32
_TmnxMobServPcAcctRfAggrDlBytsHi_Object = MibTableColumn
tmnxMobServPcAcctRfAggrDlBytsHi = _TmnxMobServPcAcctRfAggrDlBytsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 12),
    _TmnxMobServPcAcctRfAggrDlBytsHi_Type()
)
tmnxMobServPcAcctRfAggrDlBytsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfAggrDlBytsHi.setStatus("current")
_TmnxMobServPcAcctRfUlAvgRate_Type = Counter32
_TmnxMobServPcAcctRfUlAvgRate_Object = MibTableColumn
tmnxMobServPcAcctRfUlAvgRate = _TmnxMobServPcAcctRfUlAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 13),
    _TmnxMobServPcAcctRfUlAvgRate_Type()
)
tmnxMobServPcAcctRfUlAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfUlAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfUlAvgRate.setUnits("kbps")
_TmnxMobServPcAcctRfDlAvgRate_Type = Counter32
_TmnxMobServPcAcctRfDlAvgRate_Object = MibTableColumn
tmnxMobServPcAcctRfDlAvgRate = _TmnxMobServPcAcctRfDlAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 14),
    _TmnxMobServPcAcctRfDlAvgRate_Type()
)
tmnxMobServPcAcctRfDlAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfDlAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfDlAvgRate.setUnits("kbps")
_TmnxMobServPcAcctRfNumIntrimSent_Type = Counter32
_TmnxMobServPcAcctRfNumIntrimSent_Object = MibTableColumn
tmnxMobServPcAcctRfNumIntrimSent = _TmnxMobServPcAcctRfNumIntrimSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 18, 1, 15),
    _TmnxMobServPcAcctRfNumIntrimSent_Type()
)
tmnxMobServPcAcctRfNumIntrimSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServPcAcctRfNumIntrimSent.setStatus("current")
_TmnxMobServS11CauseCodeTable_Object = MibTable
tmnxMobServS11CauseCodeTable = _TmnxMobServS11CauseCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19)
)
if mibBuilder.loadTexts:
    tmnxMobServS11CauseCodeTable.setStatus("current")
_TmnxMobServS11CauseCodeEntry_Object = MibTableRow
tmnxMobServS11CauseCodeEntry = _TmnxMobServS11CauseCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1)
)
if mibBuilder.loadTexts:
    tmnxMobServS11CauseCodeEntry.setStatus("current")
_TmnxMobServS11CcRxReqAccepted_Type = Counter32
_TmnxMobServS11CcRxReqAccepted_Object = MibTableColumn
tmnxMobServS11CcRxReqAccepted = _TmnxMobServS11CcRxReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 1),
    _TmnxMobServS11CcRxReqAccepted_Type()
)
tmnxMobServS11CcRxReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxReqAccepted.setStatus("current")
_TmnxMobServS11CcRxCtxNotFound_Type = Counter32
_TmnxMobServS11CcRxCtxNotFound_Object = MibTableColumn
tmnxMobServS11CcRxCtxNotFound = _TmnxMobServS11CcRxCtxNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 2),
    _TmnxMobServS11CcRxCtxNotFound_Type()
)
tmnxMobServS11CcRxCtxNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxCtxNotFound.setStatus("current")
_TmnxMobServS11CcRxInvalidLength_Type = Counter32
_TmnxMobServS11CcRxInvalidLength_Object = MibTableColumn
tmnxMobServS11CcRxInvalidLength = _TmnxMobServS11CcRxInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 3),
    _TmnxMobServS11CcRxInvalidLength_Type()
)
tmnxMobServS11CcRxInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxInvalidLength.setStatus("current")
_TmnxMobServS11CcRxMndIeIncorrect_Type = Counter32
_TmnxMobServS11CcRxMndIeIncorrect_Object = MibTableColumn
tmnxMobServS11CcRxMndIeIncorrect = _TmnxMobServS11CcRxMndIeIncorrect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 4),
    _TmnxMobServS11CcRxMndIeIncorrect_Type()
)
tmnxMobServS11CcRxMndIeIncorrect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxMndIeIncorrect.setStatus("current")
_TmnxMobServS11CcRxMandIeMissing_Type = Counter32
_TmnxMobServS11CcRxMandIeMissing_Object = MibTableColumn
tmnxMobServS11CcRxMandIeMissing = _TmnxMobServS11CcRxMandIeMissing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 5),
    _TmnxMobServS11CcRxMandIeMissing_Type()
)
tmnxMobServS11CcRxMandIeMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxMandIeMissing.setStatus("current")
_TmnxMobServS11CcRxReqRejected_Type = Counter32
_TmnxMobServS11CcRxReqRejected_Object = MibTableColumn
tmnxMobServS11CcRxReqRejected = _TmnxMobServS11CcRxReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 6),
    _TmnxMobServS11CcRxReqRejected_Type()
)
tmnxMobServS11CcRxReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxReqRejected.setStatus("current")
_TmnxMobServS11CcRxRemPeerNoResp_Type = Counter32
_TmnxMobServS11CcRxRemPeerNoResp_Object = MibTableColumn
tmnxMobServS11CcRxRemPeerNoResp = _TmnxMobServS11CcRxRemPeerNoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 7),
    _TmnxMobServS11CcRxRemPeerNoResp_Type()
)
tmnxMobServS11CcRxRemPeerNoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxRemPeerNoResp.setStatus("current")
_TmnxMobServS11CcRxNoResAvailable_Type = Counter32
_TmnxMobServS11CcRxNoResAvailable_Object = MibTableColumn
tmnxMobServS11CcRxNoResAvailable = _TmnxMobServS11CcRxNoResAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 8),
    _TmnxMobServS11CcRxNoResAvailable_Type()
)
tmnxMobServS11CcRxNoResAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxNoResAvailable.setStatus("current")
_TmnxMobServS11CcRxUsrAuthFailure_Type = Counter32
_TmnxMobServS11CcRxUsrAuthFailure_Object = MibTableColumn
tmnxMobServS11CcRxUsrAuthFailure = _TmnxMobServS11CcRxUsrAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 9),
    _TmnxMobServS11CcRxUsrAuthFailure_Type()
)
tmnxMobServS11CcRxUsrAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxUsrAuthFailure.setStatus("current")
_TmnxMobServS11CcRxOthers_Type = Counter32
_TmnxMobServS11CcRxOthers_Object = MibTableColumn
tmnxMobServS11CcRxOthers = _TmnxMobServS11CcRxOthers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 10),
    _TmnxMobServS11CcRxOthers_Type()
)
tmnxMobServS11CcRxOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcRxOthers.setStatus("current")
_TmnxMobServS11CcTxReqAccepted_Type = Counter32
_TmnxMobServS11CcTxReqAccepted_Object = MibTableColumn
tmnxMobServS11CcTxReqAccepted = _TmnxMobServS11CcTxReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 11),
    _TmnxMobServS11CcTxReqAccepted_Type()
)
tmnxMobServS11CcTxReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxReqAccepted.setStatus("current")
_TmnxMobServS11CcTxCtxNotFound_Type = Counter32
_TmnxMobServS11CcTxCtxNotFound_Object = MibTableColumn
tmnxMobServS11CcTxCtxNotFound = _TmnxMobServS11CcTxCtxNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 12),
    _TmnxMobServS11CcTxCtxNotFound_Type()
)
tmnxMobServS11CcTxCtxNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxCtxNotFound.setStatus("current")
_TmnxMobServS11CcTxInvalidLength_Type = Counter32
_TmnxMobServS11CcTxInvalidLength_Object = MibTableColumn
tmnxMobServS11CcTxInvalidLength = _TmnxMobServS11CcTxInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 13),
    _TmnxMobServS11CcTxInvalidLength_Type()
)
tmnxMobServS11CcTxInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxInvalidLength.setStatus("current")
_TmnxMobServS11CcTxMndIeIncorrect_Type = Counter32
_TmnxMobServS11CcTxMndIeIncorrect_Object = MibTableColumn
tmnxMobServS11CcTxMndIeIncorrect = _TmnxMobServS11CcTxMndIeIncorrect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 14),
    _TmnxMobServS11CcTxMndIeIncorrect_Type()
)
tmnxMobServS11CcTxMndIeIncorrect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxMndIeIncorrect.setStatus("current")
_TmnxMobServS11CcTxMandIeMissing_Type = Counter32
_TmnxMobServS11CcTxMandIeMissing_Object = MibTableColumn
tmnxMobServS11CcTxMandIeMissing = _TmnxMobServS11CcTxMandIeMissing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 15),
    _TmnxMobServS11CcTxMandIeMissing_Type()
)
tmnxMobServS11CcTxMandIeMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxMandIeMissing.setStatus("current")
_TmnxMobServS11CcTxReqRejected_Type = Counter32
_TmnxMobServS11CcTxReqRejected_Object = MibTableColumn
tmnxMobServS11CcTxReqRejected = _TmnxMobServS11CcTxReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 16),
    _TmnxMobServS11CcTxReqRejected_Type()
)
tmnxMobServS11CcTxReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxReqRejected.setStatus("current")
_TmnxMobServS11CcTxRemPeerNoResp_Type = Counter32
_TmnxMobServS11CcTxRemPeerNoResp_Object = MibTableColumn
tmnxMobServS11CcTxRemPeerNoResp = _TmnxMobServS11CcTxRemPeerNoResp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 17),
    _TmnxMobServS11CcTxRemPeerNoResp_Type()
)
tmnxMobServS11CcTxRemPeerNoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxRemPeerNoResp.setStatus("current")
_TmnxMobServS11CcTxNoResAvailable_Type = Counter32
_TmnxMobServS11CcTxNoResAvailable_Object = MibTableColumn
tmnxMobServS11CcTxNoResAvailable = _TmnxMobServS11CcTxNoResAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 18),
    _TmnxMobServS11CcTxNoResAvailable_Type()
)
tmnxMobServS11CcTxNoResAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxNoResAvailable.setStatus("current")
_TmnxMobServS11CcTxUsrAuthFailure_Type = Counter32
_TmnxMobServS11CcTxUsrAuthFailure_Object = MibTableColumn
tmnxMobServS11CcTxUsrAuthFailure = _TmnxMobServS11CcTxUsrAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 19),
    _TmnxMobServS11CcTxUsrAuthFailure_Type()
)
tmnxMobServS11CcTxUsrAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxUsrAuthFailure.setStatus("current")
_TmnxMobServS11CcTxOthers_Type = Counter32
_TmnxMobServS11CcTxOthers_Object = MibTableColumn
tmnxMobServS11CcTxOthers = _TmnxMobServS11CcTxOthers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 2, 19, 1, 20),
    _TmnxMobServS11CcTxOthers_Type()
)
tmnxMobServS11CcTxOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11CcTxOthers.setStatus("current")
_TmnxMobServingGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxMobServingGlobalObjs = _TmnxMobServingGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3)
)
_TmnxMobServTableLastChanged_Type = TimeStamp
_TmnxMobServTableLastChanged_Object = MibScalar
tmnxMobServTableLastChanged = _TmnxMobServTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 1),
    _TmnxMobServTableLastChanged_Type()
)
tmnxMobServTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServTableLastChanged.setStatus("current")
_TmnxMobServSigTableLastChanged_Type = TimeStamp
_TmnxMobServSigTableLastChanged_Object = MibScalar
tmnxMobServSigTableLastChanged = _TmnxMobServSigTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 2),
    _TmnxMobServSigTableLastChanged_Type()
)
tmnxMobServSigTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServSigTableLastChanged.setStatus("current")
_TmnxMobServGxcTableLastChanged_Type = TimeStamp
_TmnxMobServGxcTableLastChanged_Object = MibScalar
tmnxMobServGxcTableLastChanged = _TmnxMobServGxcTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 3),
    _TmnxMobServGxcTableLastChanged_Type()
)
tmnxMobServGxcTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGxcTableLastChanged.setStatus("current")
_TmnxMobServS5TableLastChanged_Type = TimeStamp
_TmnxMobServS5TableLastChanged_Object = MibScalar
tmnxMobServS5TableLastChanged = _TmnxMobServS5TableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 4),
    _TmnxMobServS5TableLastChanged_Type()
)
tmnxMobServS5TableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS5TableLastChanged.setStatus("current")
_TmnxMobServS8TableLastChanged_Type = TimeStamp
_TmnxMobServS8TableLastChanged_Object = MibScalar
tmnxMobServS8TableLastChanged = _TmnxMobServS8TableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 5),
    _TmnxMobServS8TableLastChanged_Type()
)
tmnxMobServS8TableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS8TableLastChanged.setStatus("current")
_TmnxMobServS11TableLastChanged_Type = TimeStamp
_TmnxMobServS11TableLastChanged_Object = MibScalar
tmnxMobServS11TableLastChanged = _TmnxMobServS11TableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 6),
    _TmnxMobServS11TableLastChanged_Type()
)
tmnxMobServS11TableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11TableLastChanged.setStatus("current")
_TmnxMobServS1uTableLastChanged_Type = TimeStamp
_TmnxMobServS1uTableLastChanged_Object = MibScalar
tmnxMobServS1uTableLastChanged = _TmnxMobServS1uTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 7),
    _TmnxMobServS1uTableLastChanged_Type()
)
tmnxMobServS1uTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uTableLastChanged.setStatus("current")
_TmnxMobServS12TableLastChanged_Type = TimeStamp
_TmnxMobServS12TableLastChanged_Object = MibScalar
tmnxMobServS12TableLastChanged = _TmnxMobServS12TableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 8),
    _TmnxMobServS12TableLastChanged_Type()
)
tmnxMobServS12TableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS12TableLastChanged.setStatus("current")
_TmnxMobServRfTableLastChanged_Type = TimeStamp
_TmnxMobServRfTableLastChanged_Object = MibScalar
tmnxMobServRfTableLastChanged = _TmnxMobServRfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 9),
    _TmnxMobServRfTableLastChanged_Type()
)
tmnxMobServRfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServRfTableLastChanged.setStatus("current")
_TmnxMobServApnTableLastChanged_Type = TimeStamp
_TmnxMobServApnTableLastChanged_Object = MibScalar
tmnxMobServApnTableLastChanged = _TmnxMobServApnTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 10),
    _TmnxMobServApnTableLastChanged_Type()
)
tmnxMobServApnTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServApnTableLastChanged.setStatus("current")
_TmnxMobServS11PeerTableLastChngd_Type = TimeStamp
_TmnxMobServS11PeerTableLastChngd_Object = MibScalar
tmnxMobServS11PeerTableLastChngd = _TmnxMobServS11PeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 11),
    _TmnxMobServS11PeerTableLastChngd_Type()
)
tmnxMobServS11PeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS11PeerTableLastChngd.setStatus("current")
_TmnxMobServS1uPeerTableLastChngd_Type = TimeStamp
_TmnxMobServS1uPeerTableLastChngd_Object = MibScalar
tmnxMobServS1uPeerTableLastChngd = _TmnxMobServS1uPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 12),
    _TmnxMobServS1uPeerTableLastChngd_Type()
)
tmnxMobServS1uPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServS1uPeerTableLastChngd.setStatus("current")
_TmnxMobServApTableLastChanged_Type = TimeStamp
_TmnxMobServApTableLastChanged_Object = MibScalar
tmnxMobServApTableLastChanged = _TmnxMobServApTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 13),
    _TmnxMobServApTableLastChanged_Type()
)
tmnxMobServApTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServApTableLastChanged.setStatus("current")
_TmnxMobServGaTableLastChanged_Type = TimeStamp
_TmnxMobServGaTableLastChanged_Object = MibScalar
tmnxMobServGaTableLastChanged = _TmnxMobServGaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 15),
    _TmnxMobServGaTableLastChanged_Type()
)
tmnxMobServGaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobServGaTableLastChanged.setStatus("current")
_TmnxMobSgwGaPeerTableLastChngd_Type = TimeStamp
_TmnxMobSgwGaPeerTableLastChngd_Object = MibScalar
tmnxMobSgwGaPeerTableLastChngd = _TmnxMobSgwGaPeerTableLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 66, 3, 24),
    _TmnxMobSgwGaPeerTableLastChngd_Type()
)
tmnxMobSgwGaPeerTableLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMobSgwGaPeerTableLastChngd.setStatus("current")
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServSigEntry")
)
tmnxMobServSigEntry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServGxcEntry")
)
tmnxMobServGxcEntry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServS5Entry")
)
tmnxMobServS5Entry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServS8Entry")
)
tmnxMobServS8Entry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServS11Entry")
)
tmnxMobServS11Entry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServS1uEntry")
)
tmnxMobServS1uEntry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServS12Entry")
)
tmnxMobServS12Entry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServRfEntry")
)
tmnxMobServRfEntry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServGaEntry")
)
tmnxMobServGaEntry.setIndexNames(*tmnxMobServEntry.getIndexNames())
tmnxMobServStatEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServProcsEntry")
)
tmnxMobServProcsEntry.setIndexNames(*tmnxMobServStatEntry.getIndexNames())
tmnxMobServBearerContextEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServBcAcctGaEntry")
)
tmnxMobServBcAcctGaEntry.setIndexNames(*tmnxMobServBearerContextEntry.getIndexNames())
tmnxMobServPdnContextEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServPcAcctRfEntry")
)
tmnxMobServPcAcctRfEntry.setIndexNames(*tmnxMobServPdnContextEntry.getIndexNames())
tmnxMobServS11StatEntry.registerAugmentions(
    ("TIMETRA-MOBILE-SERVING-MIB",
     "tmnxMobServS11CauseCodeEntry")
)
tmnxMobServS11CauseCodeEntry.setIndexNames(*tmnxMobServS11StatEntry.getIndexNames())

# Managed Objects groups

tmnxMobServingGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 1)
)
tmnxMobServingGlobalGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServTableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigTableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5TableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11TableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uTableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnTableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerTableLastChngd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerTableLastChngd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfTableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApTableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerTableLastChngd"))
)
if mibBuilder.loadTexts:
    tmnxMobServingGlobalGroup.setStatus("current")

tmnxMobServingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 2)
)
tmnxMobServingGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServAdminState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServOperState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGracefulShutTimeout"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServMobNode"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUplinkQciPolName"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServDownlinkQciPolName"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigGtpcProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigGtpuProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigDiaOriginHost"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigDiaOriginRealm"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigDiaProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigDefaultIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigDefaultIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBearerGtpuUdpChecksum"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBearerGtpuSeqNumber"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5LastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5PeerList"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5GtpcIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5GtpcIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5GtpuIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5DualStackPref"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5GtpuIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5GtpcProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5GtpuProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11LastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerList"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11GtpcIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11GtpcIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11GtpcProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerList"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uGtpuIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uGtpuIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uGtpuProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uGtpuUdpCheckSum"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uGtpuSeqNumber"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uDualStackPref"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnRowStatus"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnUplinkQciPolName"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnDownlinkQciPolName"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5DualStackPrefCplane"))
)
if mibBuilder.loadTexts:
    tmnxMobServingGroup.setStatus("current")

tmnxMobServingStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 3)
)
tmnxMobServingStatGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatApn"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatDefaultBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatDedicatedBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIpv4Bearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIpv6Bearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIpv4v6Bearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatActiveBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIdleBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRoamers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatPagingInProgress"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatBuffersAllocated"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatBuffersAvailable"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatBuffersAllocErr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcAttach"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDetach"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwServiceReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeServiceReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1Release"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterENBX2Hndovr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterENBS1Hndovr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeDedBrActivation"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwDedBrActivtn"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwDedBrDeActiv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMmeDedBrDeActiv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcHssQosModificatn"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcAttachFailures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDetachFailures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwServiceReqFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeServiceReqFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1ReleaseFailures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEnbX2HndovrFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEnbS1HndovrFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeDedBrActvFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwDedBrActvFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwDedBrDeActFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMmeDedBrDeAcFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcHssQosModifyFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatHomers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatVisitors"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatENBs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatMmes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatPgws"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatUes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRfPeer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRfAcctStartBuf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRfAcctIntBuf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRfAcctStopBuf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcPagingTimeoutExp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcIntraIdleModeTau"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeRel"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeRelFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterIdleTau"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterIdleTauFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1WithIndTnl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1WithIndTnlFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1WoIndTnl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1WoIndTnlFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterX2Hndor"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterX2HndorFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterSgwHoOut"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMltPdnConcvtReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMltPdnConcvtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcModBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcModBearersFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDelBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDelBearersFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcBearerRes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcBearerResFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEhrpdLteHo"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEhrpdLteHoFails"))
)
if mibBuilder.loadTexts:
    tmnxMobServingStatGroup.setStatus("obsolete")

tmnxMobServingBcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 4)
)
tmnxMobServingBcGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeRowStatus"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeMsIsdn"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImei"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeNai"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeNwkMcc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeNwkMnc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeTrackingAreaId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeCellId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeRat"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUePdnContexts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeBearerContexts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeChassisIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeCardSlotNum"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11MmeCtrlTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11MmeCtrlAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11MmeCtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11SgwCtrlTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11SgwCtrlAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11SgwCtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11InterEnbX2HandOv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11InterEnbS1HandOv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS1ReleaseProcedures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUePagingReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeRfSgwAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeRfSgwAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcLinkedBearerId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcApnRestriction"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcUlApnAmbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcDlApnAmbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcIpv4AddressType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcIpv4Address"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcIpv6AddressType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcIpv6Address"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcBearerContexts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcSessionState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcLastEvent"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SigProtocol"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwCtrlTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwCtrlAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwCtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwCtrlTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwCtrlAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwCtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfServerAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfServerAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfServerState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfBearerType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfChargingLevel"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfChargingProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfTriggeredRecords"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfInterimRecords"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwV6CtrlAdrTyp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwV6CtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwV6CtrlAdrTyp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwV6CtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcBearerType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcUpTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQci"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcArp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQosUlMbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQosDlMbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQosUlGbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQosDlGbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uEnodebTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uEnodebAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uEnodebAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uSgwTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uSgwAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uSgwAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8SgwTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8SgwDataAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8SgwDataAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8PgwTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8PgwDataAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8PgwDataAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS11QosModifications"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULPacketsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULPacketsHigh"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULBytesLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULBytesHigh"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLPacketsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLPacketsHigh"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLBytesLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLBytesHigh"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeIntraSgwIdleTau"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeInitServReqProcs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUePagedCount"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAntiSpoofFailureCnt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSetupLatencyTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlRemTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlRemAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlRemAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlLocalTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlLocalAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlLocalAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfServerAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfServerAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfServerState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfChargingProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfTriggeredRecords"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfInterimRecords"))
)
if mibBuilder.loadTexts:
    tmnxMobServingBcGroup.setStatus("obsolete")

tmnxMobServingRefPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 5)
)
tmnxMobServingRefPointGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerPathMgmtState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerGatewayId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateSessnReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateSessnRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteSessnReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteSessnRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxEchoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxEchoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxDlNotify"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxDlAcks"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxDlFailNotify"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPagingSvcReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxMalfrmedPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxUnknownPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxMissngIePkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPeerRestarts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPeerRestartCnt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPathMgmtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRelBearersReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRelBearersResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCrtIndrTnlReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCrtIndrTnlResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelIndrTnlReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelIndrTnlResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerPathMgmtState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerGatewayId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBcNotFound"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatTxEchoResponse"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatTxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRxEchoResponse"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPeerRestarts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPeerRestartCnt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPathMgmtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearersIpv4"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearersIpv6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearerIpv4v6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDedctdBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDefBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRoamers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatActiveBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatIdleBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatUpdateBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatUpdateBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearersIpv4"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearersIpv6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearerIpv4v6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDedctdBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatUlBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDlBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatUlPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDlPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDefBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRoamers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatActiveBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatIdleBearers"))
)
if mibBuilder.loadTexts:
    tmnxMobServingRefPointGroup.setStatus("obsolete")

tmnxMobServingUnsupportedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 6)
)
tmnxMobServingUnsupportedGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcTableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS12TableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPccDynamicState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServVisitingPlmnList"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPolBaseName"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigPmipv6Profile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigPmipv6AddrScheme"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigPmipv6RtrAdIntvl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServSigPmipv6RtrAdLife"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcDiaIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcDiaIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcDiaTransTimer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcDiaRetryCount"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcDefPriDiaPeer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcDefSecDiaPeer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcDiameterApp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5Pmipv6IfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5Pmipv6IfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5Pmipv6LnkLclAdrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5Pmipv6LnkLclAddress"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5Pmipv6Profile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5Pmipv6RtrAdIntvl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5Pmipv6RtrAdLife"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS5Pmipv6RtrAddrScheme"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8Pmipv6IfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8Pmipv6IfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8Pmipv6LnkLclAdrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8Pmipv6LnkLclAddress"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8Pmipv6Profile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8Pmipv6RtrAdIntvl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8Pmipv6RtrAdLife"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8Pmipv6RtrAddrScheme"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS12LastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS12PeerList"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS12GtpuIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS12GtpuIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS12GtpuProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS12GtpuUdpCheckSum"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS12GtpuSeqNumber"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnDescription"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnDynamicPcc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnPolBaseName"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatCcr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatCca"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatCcrFailures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatRar"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatRaa"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatBberf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatRxMalformedPkt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatRxUnknownPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatRxMissingIePkt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatStr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatSta"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatAsr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatAsa"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatCer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatCea"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatDpr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatDpa"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatDwr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatDwa"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatPrProfStatus"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGxcStatPrDetailStatus"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcPcrfEventTriggers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwGreKey"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwGreKey"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwTrprtAdrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwTransprtAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcGxcPcrfAddressType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcGxcPcrfAddress"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcGxcSgwAddressType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcGxcSgwAddress"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcFilters"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfPcrfPrecedence"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfRuleName"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfPacketFilters"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfQosUlMbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfQosDlMbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfQosUlGbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfQosDlGbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterProtocol"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterSrcAdrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterSrcAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterSrcPfxLen"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterDstAdrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterDestAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterDestPfxLen"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterSrcPorts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFilterDestPorts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFirstSrcPortOper"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFirstSrcPortVal1"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFirstSrcPortVal2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfSecndSrcPortOper"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfSecndSrcPortVal1"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfSecndSrcPortVal2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFirstDstPortOper"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFirstDstPortVal1"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfFirstDstPortVal2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfSecndDstPortOper"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfSecndDstPortVal1"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSdfSecndDstPortVal2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterProtocol"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterSrcAdrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterSrcAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterSrcPfxLen"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterDstAdrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterDestAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterDestPfxLen"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterSrcPorts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFilterDestPorts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFirstSrcPortOper"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFirstSrcPortVal1"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFirstSrcPortVal2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftSecndSrcPortOper"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftSecndSrcPortVal1"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftSecndSrcPortVal2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFirstDstPortOper"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFirstDstPortVal1"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftFirstDstPortVal2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftSecndDstPortOper"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftSecndDstPortVal1"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcTftSecndDstPortVal2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIpv4Sdf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIpv6Sdf"))
)
if mibBuilder.loadTexts:
    tmnxMobServingUnsupportedGroup.setStatus("current")

tmnxMobServingChargingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 7)
)
tmnxMobServingChargingGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChargingProfHome"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChargingProfVisiting"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChargingProfRoaming"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChrgCcIgnoreAny"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChrgCcIgnoreHome"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChrgCcIgnoreVisiting"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChrgCcIgnoreRoaming"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfPriDiaPeer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfSecDiaPeer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfAcctIntmInterval"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfApplTxTimer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfRetryCount"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfChargingGroupID"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOperatorString"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfAcctLevel"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfNodeId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcFilePrivateInfo"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcFileExtension"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcFileClosureSize"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcFileClsLifeTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcFileClsMaxAcrs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcFileObsoleteTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcPrimaryCf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcCf1State"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcCf1Limit"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcCf2State"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfOcCf2Limit"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChrgCcReject"))
)
if mibBuilder.loadTexts:
    tmnxMobServingChargingGroup.setStatus("current")

tmnxMobServingApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 8)
)
tmnxMobServingApGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApRowStatus"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApCollectAcctStats"))
)
if mibBuilder.loadTexts:
    tmnxMobServingApGroup.setStatus("current")

tmnxMobServingObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 9)
)
tmnxMobServingObsoletedGroup.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcBearerRes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcBearerResFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDelBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDelBearersFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEnbS1HndovrFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEnbX2HndovrFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterENBS1Hndovr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterENBX2Hndovr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeRel"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeRelFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMltPdnConcvtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMltPdnConcvtReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcModBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcModBearersFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwServiceReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwServiceReqFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPagingSvcReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUePagedCount"))
)
if mibBuilder.loadTexts:
    tmnxMobServingObsoletedGroup.setStatus("obsolete")

tmnxMobServingStatV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 10)
)
tmnxMobServingStatV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatApn"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatDefaultBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatDedicatedBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIpv4Bearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIpv6Bearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIpv4v6Bearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatActiveBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIdleBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRoamers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatPagingInProgress"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatBuffersAllocated"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatBuffersAvailable"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatBuffersAllocErr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcAttach"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDetach"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeServiceReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1Release"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeDedBrActivation"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwDedBrActivtn"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwDedBrDeActiv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMmeDedBrDeActiv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcHssQosModificatn"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcAttachFailures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDetachFailures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeServiceReqFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1ReleaseFailures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeDedBrActvFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwDedBrActvFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwDedBrDeActFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMmeDedBrDeAcFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcHssQosModifyFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatHomers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatVisitors"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatENBs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatMmes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatPgws"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatUes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRfPeer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRfAcctStartBuf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRfAcctIntBuf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatRfAcctStopBuf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcPagingTimeoutExp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcIntraIdleModeTau"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterIdleTau"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterIdleTauFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1WithIndTnl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1WithIndTnlFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1WoIndTnl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcS1WoIndTnlFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterX2Hndor"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterX2HndorFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterSgwHoOut"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEhrpdLteHo"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEhrpdLteHoFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcIntraIdleTauFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwPdnSessDeActiv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwPdnSesDeActFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcPagingAttempts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcPagingFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcIntraSgwHndvr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcIntraSgwHndvrFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcIntraSgwS1IndTnl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcIntraS1IndTnlFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeIdleTau"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeIdlTauFls"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeS1X2RlSuc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeS1X2RlFls"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeS1RlTnSuc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeS1RlTnFls"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatIdleUes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeRelocs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcAttachPiggyBack"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcAttachPiggyFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeDedBrDeActv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeDedBrDeActvFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeDedBrModify"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcUeDedBrModifyFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwBrModify"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwBrModifyFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatNumSuspendedUE"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcPDNSuspNotice"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcPDNResumeNotice"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcIRSR"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEmergncyAttachSuc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatEmergencyPdnSess"))
)
if mibBuilder.loadTexts:
    tmnxMobServingStatV3v0Group.setStatus("current")

tmnxMobServingRefPointV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 11)
)
tmnxMobServingRefPointV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerPathMgmtState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerGatewayId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateSessnReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateSessnRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteSessnReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteSessnRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxEchoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxEchoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxDlNotify"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxDlAcks"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxDlFailNotify"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxMalfrmedPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxUnknownPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxMissngIePkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPeerRestarts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPeerRestartCnt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPathMgmtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRelBearersReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRelBearersResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCrtIndrTnlReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCrtIndrTnlResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelIndrTnlReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelIndrTnlResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerPathMgmtState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerGatewayId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBcNotFound"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatTxEchoResponse"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatTxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRxEchoResponse"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPeerRestarts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPeerRestartCnt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPathMgmtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearersIpv4"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearersIpv6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearerIpv4v6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDedctdBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDefBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRoamers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatActiveBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatIdleBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatUpdateBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatUpdateBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearersIpv4"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearersIpv6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearerIpv4v6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDedctdBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatUlBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDlBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatUlPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDlPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDefBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRoamers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatActiveBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatIdleBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrCmd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrFlr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrCmd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrFlr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerPathMgmtState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerDetailState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxEchoResponses"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxEchoResponses"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxNodeAlRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxNodeAlResps"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxDataRecReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxDataRecTferReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRetrDataRecReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxDataRecReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatUnackDataRexReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxRedirectionReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxRedrnResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxInvalidMsgs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxVerNotSupp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrTermination"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrMaxChngCond"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrMsTmzChng"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrRatChng"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrTimeLimit"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrVolLimit"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrReqAcc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrNoResAva"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrReqNotFf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrReqFfilled"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrDupReqFf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrInvMsgFmat"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrVerNotSupp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrSrvcNotSupp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrMandIeInc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrMandIeMiss"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrOptIeInc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrSystemFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRtrEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatGtpPrimeFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatOperState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatUpTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxNodeAlRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxNodeAlResps"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatNodeAlReqRetried"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatCdrsTx"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatCdrsRx"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrSerNdChLmt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearrResCmd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBrrResFailInd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxVerNotSupp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatSuspNoticeReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatSuspNoticeAck"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatResNoticeReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatResNoticeAck"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrMgmtInterv"))
)
if mibBuilder.loadTexts:
    tmnxMobServingRefPointV3v0Group.setStatus("obsolete")

tmnxMobServingBcV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 12)
)
tmnxMobServingBcV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeRowStatus"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeMsIsdn"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImei"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeNai"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeNwkMcc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeNwkMnc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeTrackingAreaId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeCellId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeRat"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUePdnContexts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeBearerContexts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeChassisIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeCardSlotNum"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11MmeCtrlTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11MmeCtrlAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11MmeCtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11SgwCtrlTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11SgwCtrlAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11SgwCtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11InterEnbX2HandOv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS11InterEnbS1HandOv"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeS1ReleaseProcedures"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUePagingReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeRfSgwAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeRfSgwAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcLinkedBearerId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcApnRestriction"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcUlApnAmbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcDlApnAmbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcIpv4AddressType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcIpv4Address"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcIpv6AddressType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcIpv6Address"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcBearerContexts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcSessionState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcLastEvent"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SigProtocol"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwCtrlTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwCtrlAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwCtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwCtrlTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwCtrlAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwCtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfServerAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfServerAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfServerState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfBearerType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfChargingLevel"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfChargingProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfTriggeredRecords"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRfInterimRecords"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwV6CtrlAdrTyp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8SgwV6CtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwV6CtrlAdrTyp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcS5S8PgwV6CtrlAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcBearerType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcUpTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQci"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcArp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQosUlMbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQosDlMbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQosUlGbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcQosDlGbr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uEnodebTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uEnodebAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uEnodebAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uSgwTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uSgwAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uSgwAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8SgwTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8SgwDataAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8SgwDataAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8PgwTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8PgwDataAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5S8PgwDataAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS11QosModifications"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULPacketsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULPacketsHigh"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULBytesLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS5ULBytesHigh"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLPacketsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLPacketsHigh"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLBytesLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcS1uDLBytesHigh"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeIntraSgwIdleTau"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeInitServReqProcs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAntiSpoofFailureCnt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcSetupLatencyTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlRemTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlRemAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlRemAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlLocalTeid"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlLocalAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcIndTnlLocalAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfServerAddrType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfServerAddr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfServerState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfChargingProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfTriggeredRecords"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRfInterimRecords"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServKeyType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUeImsiStr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcImsiAuthStatus"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcImeiStr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcImsiStr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcRefPointType"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcRefPointType"))
)
if mibBuilder.loadTexts:
    tmnxMobServingBcV3v0Group.setStatus("current")

tmnxMobServingGlobalV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 13)
)
tmnxMobServingGlobalV3v0Group.setObjects(
    ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGaTableLastChanged")
)
if mibBuilder.loadTexts:
    tmnxMobServingGlobalV3v0Group.setStatus("current")

tmnxMobServingV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 14)
)
tmnxMobServingV3v0Group.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGaLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGaIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGaIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGaGtpcProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServGaGtpPrimeGrpName"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnChrgProfileHome"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnChrgProfVisiting"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnChrgProfileRoaming"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnChrgCcIgnoreAny"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnChrgCcIgnoreHome"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnChrgCcIgnoreVisit"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnChrgCcIgnorRoaming"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServApnChrgCcReject"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8TableLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8LastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8PeerList"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8GtpcIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8GtpcIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8GtpuIfVRtrId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8GtpuIfIndex"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8GtpcProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8GtpuProfile"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8DualStackPref"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS8DualStackPrefCplane"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServHomePlmnList"))
)
if mibBuilder.loadTexts:
    tmnxMobServingV3v0Group.setStatus("current")

tmnxMobServingChargingV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 15)
)
tmnxMobServingChargingV3Group.setObjects(
    ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChrgNodeId")
)
if mibBuilder.loadTexts:
    tmnxMobServingChargingV3Group.setStatus("current")

tmnxMobServingThresholdV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 16)
)
tmnxMobServingThresholdV3Group.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtLmtUe"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtLmtBr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtLmtDefBr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtLmtDedBr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtLmtActBr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtLmtUePgd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCfsAttch"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCfsDedBr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCfsSvrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCfsItaRlc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCfsItrRlc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCfsIdlRlc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCffAttch"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCffDedBr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCffPaging"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCffHdOver"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCffSvrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrMgmtCffSrUnavl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrTrfcThrptUL"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresBrTrfcThrptDL"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS5Fail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS5Restart"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS5NoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS11PrPath"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS11PrRstt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS11NoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS1UENB"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS11MME"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS5Peer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtS8Peer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServThresPthMgmtRfFail"))
)
if mibBuilder.loadTexts:
    tmnxMobServingThresholdV3Group.setStatus("current")

tmnxMobServingAcctStatsV3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 17)
)
tmnxMobServingAcctStatsV3Group.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaChargingId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaUlSustRate"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaDlSustRate"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrUlPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrUlPktsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrUlPktsHi"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrDlPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrDlPktsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrDlPktsHi"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrUlByts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrUlBytsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrUlBytsHi"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrDlByts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrDlBytsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaAggrDlBytsHi"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaNumPartCdrs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaNumTdvs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServBcAcctGaNumMaxChanges"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrUlPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrUlPktsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrUlPktsHi"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrDlPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrDlPktsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrDlPktsHi"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrUlByts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrUlBytsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrUlBytsHi"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrDlByts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrDlBytsLow"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfAggrDlBytsHi"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfUlAvgRate"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfDlAvgRate"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServPcAcctRfNumIntrimSent"))
)
if mibBuilder.loadTexts:
    tmnxMobServingAcctStatsV3Group.setStatus("current")

tmnxMobServingRefPointV3v5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 18)
)
tmnxMobServingRefPointV3v5Group.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelSesnRspFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatUpdtBearrRspFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModBearrRspFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelBearrRspFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreatBearRspFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreatSesnRspFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRelBearrRespFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCrtIndTnlRspFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelIndTnlRspFl"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxDlAcksFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxReqAccepted"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxCtxNotFound"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxInvalidLength"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxMndIeIncorrect"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxMandIeMissing"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxReqRejected"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxRemPeerNoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxNoResAvailable"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxUsrAuthFailure"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcRxOthers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxReqAccepted"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxCtxNotFound"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxInvalidLength"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxMndIeIncorrect"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxMandIeMissing"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxReqRejected"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxRemPeerNoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxNoResAvailable"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxUsrAuthFailure"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11CcTxOthers"))
)
if mibBuilder.loadTexts:
    tmnxMobServingRefPointV3v5Group.setStatus("current")

tmnxMobServingRefPointGroupV31v2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 19)
)
tmnxMobServingRefPointGroupV31v2.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerPathMgmtState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11PeerGatewayId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateSessnReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateSessnRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteSessnReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteSessnRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCreateBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxEchoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxEchoResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatTxDlNotify"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxDlAcks"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxDlFailNotify"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxMalfrmedPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxUnknownPkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRxMissngIePkts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPeerRestarts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPeerRestartCnt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPathMgmtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRelBearersReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRelBearersResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCrtIndrTnlReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatCrtIndrTnlResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelIndrTnlReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDelIndrTnlResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerPathMgmtState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uPeerGatewayId"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBcNotFound"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatTxEchoResponse"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatTxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRxEchoResponse"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPeerRestarts"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPeerRestartCnt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatPathMgmtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatUpdateBearrReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatUpdateBearrRsp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatUlBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDlBytes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatUlPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDlPackets"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrCmd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatModifyBearrFlr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrCmd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDeleteBearrFlr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerPathMgmtState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaPeerDetailState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatLastChanged"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatCreateTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxEchoResponses"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxEchoResponses"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxNodeAlRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxNodeAlResps"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxDataRecReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxDataRecTferReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRetrDataRecReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxDataRecReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatUnackDataRexReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxRedirectionReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxRedrnResp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxInvalidMsgs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxVerNotSupp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrTermination"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrMaxChngCond"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrMsTmzChng"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrRatChng"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrTimeLimit"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrVolLimit"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrReqAcc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrNoResAva"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrReqNotFf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrReqFfilled"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrDupReqFf"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrInvMsgFmat"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrVerNotSupp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrSrvcNotSupp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrMandIeInc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrMandIeMiss"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrOptIeInc"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxCdrSystemFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRtrEchoRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatGtpPrimeFail"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatOperState"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatUpTime"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxNodeAlRequests"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatRxNodeAlResps"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatNodeAlReqRetried"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatCdrsTx"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatCdrsRx"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrSerNdChLmt"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearrResCmd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBrrResFailInd"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxVerNotSupp"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatSuspNoticeReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatSuspNoticeAck"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatResNoticeReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatResNoticeAck"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobSgwGaStatTxCdrMgmtInterv"))
)
if mibBuilder.loadTexts:
    tmnxMobServingRefPointGroupV31v2.setStatus("current")

tmnxMobServingObsoletedGrpV31v2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 20)
)
tmnxMobServingObsoletedGrpV31v2.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcBearerRes"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcBearerResFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDelBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcDelBearersFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEnbS1HndovrFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcEnbX2HndovrFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterENBS1Hndovr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterENBX2Hndovr"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeRel"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcInterMmeRelFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMltPdnConcvtFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcMltPdnConcvtReqs"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcModBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcModBearersFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwServiceReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServProcNwServiceReqFails"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatPagingSvcReq"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServUePagedCount"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearersIpv4"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearersIpv6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatBearerIpv4v6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDedctdBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatDefBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatRoamers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatActiveBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS1uStatIdleBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearersIpv4"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearersIpv6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatBearerIpv4v6"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDedctdBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatDefBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatRoamers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatActiveBearers"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11StatIdleBearers"))
)
if mibBuilder.loadTexts:
    tmnxMobServingObsoletedGrpV31v2.setStatus("current")

tmnxMobServingV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 21)
)
tmnxMobServingV4v0Group.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServS11GtpcDdnDumpTimer"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServChargingAvpDiag"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServRfSuppVendorAvps"))
)
if mibBuilder.loadTexts:
    tmnxMobServingV4v0Group.setStatus("current")

tmnxMobServStatV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 2, 22)
)
tmnxMobServStatV4v0Group.setObjects(
    ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatPagingDrops")
)
if mibBuilder.loadTexts:
    tmnxMobServStatV4v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxMobServV1v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 1, 1)
)
tmnxMobServV1v0Compliance.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingGlobalGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingStatGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingBcGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingRefPointGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingChargingGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingApGroup"))
)
if mibBuilder.loadTexts:
    tmnxMobServV1v0Compliance.setStatus(
        "obsolete"
    )

tmnxMobServV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 1, 2)
)
tmnxMobServV3v0Compliance.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingGlobalGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingChargingGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingApGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingStatV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingRefPointV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingBcV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingGlobalV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingChargingV3Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingThresholdV3Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingAcctStatsV3Group"))
)
if mibBuilder.loadTexts:
    tmnxMobServV3v0Compliance.setStatus(
        "obsolete"
    )

tmnxMobServ7xxxV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 66, 1, 3)
)
tmnxMobServ7xxxV10v0Compliance.setObjects(
      *(("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingAcctStatsV3Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingApGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingBcV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingChargingGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingChargingV3Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingGlobalGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingGlobalV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingRefPointGroupV31v2"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingStatV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingThresholdV3Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingV3v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingV4v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServStatV4v0Group"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingUnsupportedGroup"),
        ("TIMETRA-MOBILE-SERVING-MIB", "tmnxMobServingRefPointV3v5Group"))
)
if mibBuilder.loadTexts:
    tmnxMobServ7xxxV10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MOBILE-SERVING-MIB",
    **{"timetraMobServingMIBModule": timetraMobServingMIBModule,
       "tmnxMobServingConformance": tmnxMobServingConformance,
       "tmnxMobServingCompliances": tmnxMobServingCompliances,
       "tmnxMobServV1v0Compliance": tmnxMobServV1v0Compliance,
       "tmnxMobServV3v0Compliance": tmnxMobServV3v0Compliance,
       "tmnxMobServ7xxxV10v0Compliance": tmnxMobServ7xxxV10v0Compliance,
       "tmnxMobServingGroups": tmnxMobServingGroups,
       "tmnxMobServingGlobalGroup": tmnxMobServingGlobalGroup,
       "tmnxMobServingGroup": tmnxMobServingGroup,
       "tmnxMobServingStatGroup": tmnxMobServingStatGroup,
       "tmnxMobServingBcGroup": tmnxMobServingBcGroup,
       "tmnxMobServingRefPointGroup": tmnxMobServingRefPointGroup,
       "tmnxMobServingUnsupportedGroup": tmnxMobServingUnsupportedGroup,
       "tmnxMobServingChargingGroup": tmnxMobServingChargingGroup,
       "tmnxMobServingApGroup": tmnxMobServingApGroup,
       "tmnxMobServingObsoletedGroup": tmnxMobServingObsoletedGroup,
       "tmnxMobServingStatV3v0Group": tmnxMobServingStatV3v0Group,
       "tmnxMobServingRefPointV3v0Group": tmnxMobServingRefPointV3v0Group,
       "tmnxMobServingBcV3v0Group": tmnxMobServingBcV3v0Group,
       "tmnxMobServingGlobalV3v0Group": tmnxMobServingGlobalV3v0Group,
       "tmnxMobServingV3v0Group": tmnxMobServingV3v0Group,
       "tmnxMobServingChargingV3Group": tmnxMobServingChargingV3Group,
       "tmnxMobServingThresholdV3Group": tmnxMobServingThresholdV3Group,
       "tmnxMobServingAcctStatsV3Group": tmnxMobServingAcctStatsV3Group,
       "tmnxMobServingRefPointV3v5Group": tmnxMobServingRefPointV3v5Group,
       "tmnxMobServingRefPointGroupV31v2": tmnxMobServingRefPointGroupV31v2,
       "tmnxMobServingObsoletedGrpV31v2": tmnxMobServingObsoletedGrpV31v2,
       "tmnxMobServingV4v0Group": tmnxMobServingV4v0Group,
       "tmnxMobServStatV4v0Group": tmnxMobServStatV4v0Group,
       "tmnxMobServing": tmnxMobServing,
       "tmnxMobServingConfObjs": tmnxMobServingConfObjs,
       "tmnxMobServTable": tmnxMobServTable,
       "tmnxMobServEntry": tmnxMobServEntry,
       "tmnxMobServLastChanged": tmnxMobServLastChanged,
       "tmnxMobServAdminState": tmnxMobServAdminState,
       "tmnxMobServOperState": tmnxMobServOperState,
       "tmnxMobServGracefulShutTimeout": tmnxMobServGracefulShutTimeout,
       "tmnxMobServMobNode": tmnxMobServMobNode,
       "tmnxMobServPccDynamicState": tmnxMobServPccDynamicState,
       "tmnxMobServBearerGtpuUdpChecksum": tmnxMobServBearerGtpuUdpChecksum,
       "tmnxMobServBearerGtpuSeqNumber": tmnxMobServBearerGtpuSeqNumber,
       "tmnxMobServUplinkQciPolName": tmnxMobServUplinkQciPolName,
       "tmnxMobServDownlinkQciPolName": tmnxMobServDownlinkQciPolName,
       "tmnxMobServHomePlmnList": tmnxMobServHomePlmnList,
       "tmnxMobServVisitingPlmnList": tmnxMobServVisitingPlmnList,
       "tmnxMobServPolBaseName": tmnxMobServPolBaseName,
       "tmnxMobServChargingProfHome": tmnxMobServChargingProfHome,
       "tmnxMobServChargingProfVisiting": tmnxMobServChargingProfVisiting,
       "tmnxMobServChargingProfRoaming": tmnxMobServChargingProfRoaming,
       "tmnxMobServChrgCcIgnoreAny": tmnxMobServChrgCcIgnoreAny,
       "tmnxMobServChrgCcIgnoreHome": tmnxMobServChrgCcIgnoreHome,
       "tmnxMobServChrgCcIgnoreVisiting": tmnxMobServChrgCcIgnoreVisiting,
       "tmnxMobServChrgCcIgnoreRoaming": tmnxMobServChrgCcIgnoreRoaming,
       "tmnxMobServChrgCcReject": tmnxMobServChrgCcReject,
       "tmnxMobServChrgNodeId": tmnxMobServChrgNodeId,
       "tmnxMobServChargingAvpDiag": tmnxMobServChargingAvpDiag,
       "tmnxMobServSigTable": tmnxMobServSigTable,
       "tmnxMobServSigEntry": tmnxMobServSigEntry,
       "tmnxMobServSigLastChanged": tmnxMobServSigLastChanged,
       "tmnxMobServSigGtpcProfile": tmnxMobServSigGtpcProfile,
       "tmnxMobServSigGtpuProfile": tmnxMobServSigGtpuProfile,
       "tmnxMobServSigPmipv6Profile": tmnxMobServSigPmipv6Profile,
       "tmnxMobServSigPmipv6RtrAdIntvl": tmnxMobServSigPmipv6RtrAdIntvl,
       "tmnxMobServSigPmipv6RtrAdLife": tmnxMobServSigPmipv6RtrAdLife,
       "tmnxMobServSigPmipv6AddrScheme": tmnxMobServSigPmipv6AddrScheme,
       "tmnxMobServSigDiaProfile": tmnxMobServSigDiaProfile,
       "tmnxMobServSigDiaOriginRealm": tmnxMobServSigDiaOriginRealm,
       "tmnxMobServSigDiaOriginHost": tmnxMobServSigDiaOriginHost,
       "tmnxMobServSigDefaultIfVRtrId": tmnxMobServSigDefaultIfVRtrId,
       "tmnxMobServSigDefaultIfIndex": tmnxMobServSigDefaultIfIndex,
       "tmnxMobServGxcTable": tmnxMobServGxcTable,
       "tmnxMobServGxcEntry": tmnxMobServGxcEntry,
       "tmnxMobServGxcLastChanged": tmnxMobServGxcLastChanged,
       "tmnxMobServGxcDiaIfVRtrId": tmnxMobServGxcDiaIfVRtrId,
       "tmnxMobServGxcDiaIfIndex": tmnxMobServGxcDiaIfIndex,
       "tmnxMobServGxcDiaTransTimer": tmnxMobServGxcDiaTransTimer,
       "tmnxMobServGxcDiaRetryCount": tmnxMobServGxcDiaRetryCount,
       "tmnxMobServGxcDiameterApp": tmnxMobServGxcDiameterApp,
       "tmnxMobServGxcDefPriDiaPeer": tmnxMobServGxcDefPriDiaPeer,
       "tmnxMobServGxcDefSecDiaPeer": tmnxMobServGxcDefSecDiaPeer,
       "tmnxMobServS5Table": tmnxMobServS5Table,
       "tmnxMobServS5Entry": tmnxMobServS5Entry,
       "tmnxMobServS5LastChanged": tmnxMobServS5LastChanged,
       "tmnxMobServS5PeerList": tmnxMobServS5PeerList,
       "tmnxMobServS5GtpcIfVRtrId": tmnxMobServS5GtpcIfVRtrId,
       "tmnxMobServS5GtpcIfIndex": tmnxMobServS5GtpcIfIndex,
       "tmnxMobServS5GtpuIfVRtrId": tmnxMobServS5GtpuIfVRtrId,
       "tmnxMobServS5GtpuIfIndex": tmnxMobServS5GtpuIfIndex,
       "tmnxMobServS5Pmipv6IfVRtrId": tmnxMobServS5Pmipv6IfVRtrId,
       "tmnxMobServS5Pmipv6IfIndex": tmnxMobServS5Pmipv6IfIndex,
       "tmnxMobServS5Pmipv6LnkLclAdrType": tmnxMobServS5Pmipv6LnkLclAdrType,
       "tmnxMobServS5Pmipv6LnkLclAddress": tmnxMobServS5Pmipv6LnkLclAddress,
       "tmnxMobServS5GtpcProfile": tmnxMobServS5GtpcProfile,
       "tmnxMobServS5GtpuProfile": tmnxMobServS5GtpuProfile,
       "tmnxMobServS5Pmipv6Profile": tmnxMobServS5Pmipv6Profile,
       "tmnxMobServS5Pmipv6RtrAdIntvl": tmnxMobServS5Pmipv6RtrAdIntvl,
       "tmnxMobServS5Pmipv6RtrAdLife": tmnxMobServS5Pmipv6RtrAdLife,
       "tmnxMobServS5Pmipv6RtrAddrScheme": tmnxMobServS5Pmipv6RtrAddrScheme,
       "tmnxMobServS5DualStackPref": tmnxMobServS5DualStackPref,
       "tmnxMobServS5DualStackPrefCplane": tmnxMobServS5DualStackPrefCplane,
       "tmnxMobServS8Table": tmnxMobServS8Table,
       "tmnxMobServS8Entry": tmnxMobServS8Entry,
       "tmnxMobServS8LastChanged": tmnxMobServS8LastChanged,
       "tmnxMobServS8PeerList": tmnxMobServS8PeerList,
       "tmnxMobServS8GtpcIfVRtrId": tmnxMobServS8GtpcIfVRtrId,
       "tmnxMobServS8GtpcIfIndex": tmnxMobServS8GtpcIfIndex,
       "tmnxMobServS8GtpuIfVRtrId": tmnxMobServS8GtpuIfVRtrId,
       "tmnxMobServS8GtpuIfIndex": tmnxMobServS8GtpuIfIndex,
       "tmnxMobServS8Pmipv6IfVRtrId": tmnxMobServS8Pmipv6IfVRtrId,
       "tmnxMobServS8Pmipv6IfIndex": tmnxMobServS8Pmipv6IfIndex,
       "tmnxMobServS8Pmipv6LnkLclAdrType": tmnxMobServS8Pmipv6LnkLclAdrType,
       "tmnxMobServS8Pmipv6LnkLclAddress": tmnxMobServS8Pmipv6LnkLclAddress,
       "tmnxMobServS8GtpcProfile": tmnxMobServS8GtpcProfile,
       "tmnxMobServS8GtpuProfile": tmnxMobServS8GtpuProfile,
       "tmnxMobServS8Pmipv6Profile": tmnxMobServS8Pmipv6Profile,
       "tmnxMobServS8Pmipv6RtrAdIntvl": tmnxMobServS8Pmipv6RtrAdIntvl,
       "tmnxMobServS8Pmipv6RtrAdLife": tmnxMobServS8Pmipv6RtrAdLife,
       "tmnxMobServS8Pmipv6RtrAddrScheme": tmnxMobServS8Pmipv6RtrAddrScheme,
       "tmnxMobServS8DualStackPref": tmnxMobServS8DualStackPref,
       "tmnxMobServS8DualStackPrefCplane": tmnxMobServS8DualStackPrefCplane,
       "tmnxMobServS11Table": tmnxMobServS11Table,
       "tmnxMobServS11Entry": tmnxMobServS11Entry,
       "tmnxMobServS11LastChanged": tmnxMobServS11LastChanged,
       "tmnxMobServS11PeerList": tmnxMobServS11PeerList,
       "tmnxMobServS11GtpcIfVRtrId": tmnxMobServS11GtpcIfVRtrId,
       "tmnxMobServS11GtpcIfIndex": tmnxMobServS11GtpcIfIndex,
       "tmnxMobServS11GtpcProfile": tmnxMobServS11GtpcProfile,
       "tmnxMobServS11GtpcDdnDumpTimer": tmnxMobServS11GtpcDdnDumpTimer,
       "tmnxMobServS1uTable": tmnxMobServS1uTable,
       "tmnxMobServS1uEntry": tmnxMobServS1uEntry,
       "tmnxMobServS1uLastChanged": tmnxMobServS1uLastChanged,
       "tmnxMobServS1uPeerList": tmnxMobServS1uPeerList,
       "tmnxMobServS1uGtpuIfVRtrId": tmnxMobServS1uGtpuIfVRtrId,
       "tmnxMobServS1uGtpuIfIndex": tmnxMobServS1uGtpuIfIndex,
       "tmnxMobServS1uGtpuProfile": tmnxMobServS1uGtpuProfile,
       "tmnxMobServS1uGtpuUdpCheckSum": tmnxMobServS1uGtpuUdpCheckSum,
       "tmnxMobServS1uGtpuSeqNumber": tmnxMobServS1uGtpuSeqNumber,
       "tmnxMobServS1uDualStackPref": tmnxMobServS1uDualStackPref,
       "tmnxMobServS12Table": tmnxMobServS12Table,
       "tmnxMobServS12Entry": tmnxMobServS12Entry,
       "tmnxMobServS12LastChanged": tmnxMobServS12LastChanged,
       "tmnxMobServS12PeerList": tmnxMobServS12PeerList,
       "tmnxMobServS12GtpuIfVRtrId": tmnxMobServS12GtpuIfVRtrId,
       "tmnxMobServS12GtpuIfIndex": tmnxMobServS12GtpuIfIndex,
       "tmnxMobServS12GtpuProfile": tmnxMobServS12GtpuProfile,
       "tmnxMobServS12GtpuUdpCheckSum": tmnxMobServS12GtpuUdpCheckSum,
       "tmnxMobServS12GtpuSeqNumber": tmnxMobServS12GtpuSeqNumber,
       "tmnxMobServRfTable": tmnxMobServRfTable,
       "tmnxMobServRfEntry": tmnxMobServRfEntry,
       "tmnxMobServRfLastChanged": tmnxMobServRfLastChanged,
       "tmnxMobServRfVRtrId": tmnxMobServRfVRtrId,
       "tmnxMobServRfIfIndex": tmnxMobServRfIfIndex,
       "tmnxMobServRfPriDiaPeer": tmnxMobServRfPriDiaPeer,
       "tmnxMobServRfSecDiaPeer": tmnxMobServRfSecDiaPeer,
       "tmnxMobServRfAcctIntmInterval": tmnxMobServRfAcctIntmInterval,
       "tmnxMobServRfApplTxTimer": tmnxMobServRfApplTxTimer,
       "tmnxMobServRfRetryCount": tmnxMobServRfRetryCount,
       "tmnxMobServRfChargingGroupID": tmnxMobServRfChargingGroupID,
       "tmnxMobServRfOperatorString": tmnxMobServRfOperatorString,
       "tmnxMobServRfAcctLevel": tmnxMobServRfAcctLevel,
       "tmnxMobServRfNodeId": tmnxMobServRfNodeId,
       "tmnxMobServRfOcFilePrivateInfo": tmnxMobServRfOcFilePrivateInfo,
       "tmnxMobServRfOcFileExtension": tmnxMobServRfOcFileExtension,
       "tmnxMobServRfOcFileClosureSize": tmnxMobServRfOcFileClosureSize,
       "tmnxMobServRfOcFileClsLifeTime": tmnxMobServRfOcFileClsLifeTime,
       "tmnxMobServRfOcFileClsMaxAcrs": tmnxMobServRfOcFileClsMaxAcrs,
       "tmnxMobServRfOcFileObsoleteTime": tmnxMobServRfOcFileObsoleteTime,
       "tmnxMobServRfOcPrimaryCf": tmnxMobServRfOcPrimaryCf,
       "tmnxMobServRfOcCf1State": tmnxMobServRfOcCf1State,
       "tmnxMobServRfOcCf1Limit": tmnxMobServRfOcCf1Limit,
       "tmnxMobServRfOcCf2State": tmnxMobServRfOcCf2State,
       "tmnxMobServRfOcCf2Limit": tmnxMobServRfOcCf2Limit,
       "tmnxMobServRfSuppVendorAvps": tmnxMobServRfSuppVendorAvps,
       "tmnxMobServApnTable": tmnxMobServApnTable,
       "tmnxMobServApnEntry": tmnxMobServApnEntry,
       "tmnxMobServApnName": tmnxMobServApnName,
       "tmnxMobServApnRowStatus": tmnxMobServApnRowStatus,
       "tmnxMobServApnLastChanged": tmnxMobServApnLastChanged,
       "tmnxMobServApnDescription": tmnxMobServApnDescription,
       "tmnxMobServApnDynamicPcc": tmnxMobServApnDynamicPcc,
       "tmnxMobServApnUplinkQciPolName": tmnxMobServApnUplinkQciPolName,
       "tmnxMobServApnDownlinkQciPolName": tmnxMobServApnDownlinkQciPolName,
       "tmnxMobServApnPolBaseName": tmnxMobServApnPolBaseName,
       "tmnxMobServApnChrgProfileHome": tmnxMobServApnChrgProfileHome,
       "tmnxMobServApnChrgProfVisiting": tmnxMobServApnChrgProfVisiting,
       "tmnxMobServApnChrgProfileRoaming": tmnxMobServApnChrgProfileRoaming,
       "tmnxMobServApnChrgCcIgnoreAny": tmnxMobServApnChrgCcIgnoreAny,
       "tmnxMobServApnChrgCcIgnoreHome": tmnxMobServApnChrgCcIgnoreHome,
       "tmnxMobServApnChrgCcIgnoreVisit": tmnxMobServApnChrgCcIgnoreVisit,
       "tmnxMobServApnChrgCcIgnorRoaming": tmnxMobServApnChrgCcIgnorRoaming,
       "tmnxMobServApnChrgCcReject": tmnxMobServApnChrgCcReject,
       "tmnxMobServApTable": tmnxMobServApTable,
       "tmnxMobServApEntry": tmnxMobServApEntry,
       "tmnxMobServApPolicyId": tmnxMobServApPolicyId,
       "tmnxMobServApRowStatus": tmnxMobServApRowStatus,
       "tmnxMobServApLastChanged": tmnxMobServApLastChanged,
       "tmnxMobServApCollectAcctStats": tmnxMobServApCollectAcctStats,
       "tmnxMobServGaTable": tmnxMobServGaTable,
       "tmnxMobServGaEntry": tmnxMobServGaEntry,
       "tmnxMobServGaLastChanged": tmnxMobServGaLastChanged,
       "tmnxMobServGaIfVRtrId": tmnxMobServGaIfVRtrId,
       "tmnxMobServGaIfIndex": tmnxMobServGaIfIndex,
       "tmnxMobServGaGtpcProfile": tmnxMobServGaGtpcProfile,
       "tmnxMobServGaGtpPrimeGrpName": tmnxMobServGaGtpPrimeGrpName,
       "tmnxMobServingStatObjs": tmnxMobServingStatObjs,
       "tmnxMobServStatTable": tmnxMobServStatTable,
       "tmnxMobServStatEntry": tmnxMobServStatEntry,
       "tmnxMobServCardSlotNum": tmnxMobServCardSlotNum,
       "tmnxMobServStatApn": tmnxMobServStatApn,
       "tmnxMobServStatBearers": tmnxMobServStatBearers,
       "tmnxMobServStatDefaultBearers": tmnxMobServStatDefaultBearers,
       "tmnxMobServStatDedicatedBearers": tmnxMobServStatDedicatedBearers,
       "tmnxMobServStatIpv4Bearers": tmnxMobServStatIpv4Bearers,
       "tmnxMobServStatIpv6Bearers": tmnxMobServStatIpv6Bearers,
       "tmnxMobServStatIpv4v6Bearers": tmnxMobServStatIpv4v6Bearers,
       "tmnxMobServStatActiveBearers": tmnxMobServStatActiveBearers,
       "tmnxMobServStatIdleBearers": tmnxMobServStatIdleBearers,
       "tmnxMobServStatRoamers": tmnxMobServStatRoamers,
       "tmnxMobServStatPagingInProgress": tmnxMobServStatPagingInProgress,
       "tmnxMobServStatIpv4Sdf": tmnxMobServStatIpv4Sdf,
       "tmnxMobServStatIpv6Sdf": tmnxMobServStatIpv6Sdf,
       "tmnxMobServStatBuffersAllocated": tmnxMobServStatBuffersAllocated,
       "tmnxMobServStatBuffersAvailable": tmnxMobServStatBuffersAvailable,
       "tmnxMobServStatBuffersAllocErr": tmnxMobServStatBuffersAllocErr,
       "tmnxMobServStatHomers": tmnxMobServStatHomers,
       "tmnxMobServStatVisitors": tmnxMobServStatVisitors,
       "tmnxMobServStatENBs": tmnxMobServStatENBs,
       "tmnxMobServStatMmes": tmnxMobServStatMmes,
       "tmnxMobServStatPgws": tmnxMobServStatPgws,
       "tmnxMobServStatUes": tmnxMobServStatUes,
       "tmnxMobServStatRfPeer": tmnxMobServStatRfPeer,
       "tmnxMobServStatRfAcctStartBuf": tmnxMobServStatRfAcctStartBuf,
       "tmnxMobServStatRfAcctIntBuf": tmnxMobServStatRfAcctIntBuf,
       "tmnxMobServStatRfAcctStopBuf": tmnxMobServStatRfAcctStopBuf,
       "tmnxMobServStatIdleUes": tmnxMobServStatIdleUes,
       "tmnxMobServStatNumSuspendedUE": tmnxMobServStatNumSuspendedUE,
       "tmnxMobServStatEmergencyPdnSess": tmnxMobServStatEmergencyPdnSess,
       "tmnxMobServStatPagingDrops": tmnxMobServStatPagingDrops,
       "tmnxMobServProcsTable": tmnxMobServProcsTable,
       "tmnxMobServProcsEntry": tmnxMobServProcsEntry,
       "tmnxMobServProcAttach": tmnxMobServProcAttach,
       "tmnxMobServProcDetach": tmnxMobServProcDetach,
       "tmnxMobServProcNwServiceReq": tmnxMobServProcNwServiceReq,
       "tmnxMobServProcUeServiceReq": tmnxMobServProcUeServiceReq,
       "tmnxMobServProcS1Release": tmnxMobServProcS1Release,
       "tmnxMobServProcInterENBX2Hndovr": tmnxMobServProcInterENBX2Hndovr,
       "tmnxMobServProcInterENBS1Hndovr": tmnxMobServProcInterENBS1Hndovr,
       "tmnxMobServProcUeDedBrActivation": tmnxMobServProcUeDedBrActivation,
       "tmnxMobServProcNwDedBrActivtn": tmnxMobServProcNwDedBrActivtn,
       "tmnxMobServProcNwDedBrDeActiv": tmnxMobServProcNwDedBrDeActiv,
       "tmnxMobServProcMmeDedBrDeActiv": tmnxMobServProcMmeDedBrDeActiv,
       "tmnxMobServProcHssQosModificatn": tmnxMobServProcHssQosModificatn,
       "tmnxMobServProcAttachFailures": tmnxMobServProcAttachFailures,
       "tmnxMobServProcDetachFailures": tmnxMobServProcDetachFailures,
       "tmnxMobServProcNwServiceReqFails": tmnxMobServProcNwServiceReqFails,
       "tmnxMobServProcUeServiceReqFails": tmnxMobServProcUeServiceReqFails,
       "tmnxMobServProcS1ReleaseFailures": tmnxMobServProcS1ReleaseFailures,
       "tmnxMobServProcEnbX2HndovrFails": tmnxMobServProcEnbX2HndovrFails,
       "tmnxMobServProcEnbS1HndovrFails": tmnxMobServProcEnbS1HndovrFails,
       "tmnxMobServProcUeDedBrActvFails": tmnxMobServProcUeDedBrActvFails,
       "tmnxMobServProcNwDedBrActvFails": tmnxMobServProcNwDedBrActvFails,
       "tmnxMobServProcNwDedBrDeActFails": tmnxMobServProcNwDedBrDeActFails,
       "tmnxMobServProcMmeDedBrDeAcFails": tmnxMobServProcMmeDedBrDeAcFails,
       "tmnxMobServProcHssQosModifyFails": tmnxMobServProcHssQosModifyFails,
       "tmnxMobServProcPagingTimeoutExp": tmnxMobServProcPagingTimeoutExp,
       "tmnxMobServProcIntraIdleModeTau": tmnxMobServProcIntraIdleModeTau,
       "tmnxMobServProcInterMmeRel": tmnxMobServProcInterMmeRel,
       "tmnxMobServProcInterMmeRelFails": tmnxMobServProcInterMmeRelFails,
       "tmnxMobServProcInterIdleTau": tmnxMobServProcInterIdleTau,
       "tmnxMobServProcInterIdleTauFails": tmnxMobServProcInterIdleTauFails,
       "tmnxMobServProcS1WithIndTnl": tmnxMobServProcS1WithIndTnl,
       "tmnxMobServProcS1WithIndTnlFails": tmnxMobServProcS1WithIndTnlFails,
       "tmnxMobServProcS1WoIndTnl": tmnxMobServProcS1WoIndTnl,
       "tmnxMobServProcS1WoIndTnlFails": tmnxMobServProcS1WoIndTnlFails,
       "tmnxMobServProcInterX2Hndor": tmnxMobServProcInterX2Hndor,
       "tmnxMobServProcInterX2HndorFails": tmnxMobServProcInterX2HndorFails,
       "tmnxMobServProcInterSgwHoOut": tmnxMobServProcInterSgwHoOut,
       "tmnxMobServProcMltPdnConcvtReqs": tmnxMobServProcMltPdnConcvtReqs,
       "tmnxMobServProcMltPdnConcvtFails": tmnxMobServProcMltPdnConcvtFails,
       "tmnxMobServProcModBearers": tmnxMobServProcModBearers,
       "tmnxMobServProcModBearersFails": tmnxMobServProcModBearersFails,
       "tmnxMobServProcDelBearers": tmnxMobServProcDelBearers,
       "tmnxMobServProcDelBearersFails": tmnxMobServProcDelBearersFails,
       "tmnxMobServProcBearerRes": tmnxMobServProcBearerRes,
       "tmnxMobServProcBearerResFails": tmnxMobServProcBearerResFails,
       "tmnxMobServProcEhrpdLteHo": tmnxMobServProcEhrpdLteHo,
       "tmnxMobServProcEhrpdLteHoFails": tmnxMobServProcEhrpdLteHoFails,
       "tmnxMobServProcIntraIdleTauFails": tmnxMobServProcIntraIdleTauFails,
       "tmnxMobServProcNwPdnSessDeActiv": tmnxMobServProcNwPdnSessDeActiv,
       "tmnxMobServProcNwPdnSesDeActFail": tmnxMobServProcNwPdnSesDeActFail,
       "tmnxMobServProcPagingAttempts": tmnxMobServProcPagingAttempts,
       "tmnxMobServProcPagingFails": tmnxMobServProcPagingFails,
       "tmnxMobServProcIntraSgwHndvr": tmnxMobServProcIntraSgwHndvr,
       "tmnxMobServProcIntraSgwHndvrFail": tmnxMobServProcIntraSgwHndvrFail,
       "tmnxMobServProcIntraSgwS1IndTnl": tmnxMobServProcIntraSgwS1IndTnl,
       "tmnxMobServProcIntraS1IndTnlFail": tmnxMobServProcIntraS1IndTnlFail,
       "tmnxMobServProcInterMmeIdleTau": tmnxMobServProcInterMmeIdleTau,
       "tmnxMobServProcInterMmeIdlTauFls": tmnxMobServProcInterMmeIdlTauFls,
       "tmnxMobServProcInterMmeS1X2RlSuc": tmnxMobServProcInterMmeS1X2RlSuc,
       "tmnxMobServProcInterMmeS1X2RlFls": tmnxMobServProcInterMmeS1X2RlFls,
       "tmnxMobServProcInterMmeS1RlTnSuc": tmnxMobServProcInterMmeS1RlTnSuc,
       "tmnxMobServProcInterMmeS1RlTnFls": tmnxMobServProcInterMmeS1RlTnFls,
       "tmnxMobServProcInterMmeRelocs": tmnxMobServProcInterMmeRelocs,
       "tmnxMobServProcAttachPiggyBack": tmnxMobServProcAttachPiggyBack,
       "tmnxMobServProcAttachPiggyFail": tmnxMobServProcAttachPiggyFail,
       "tmnxMobServProcUeDedBrDeActv": tmnxMobServProcUeDedBrDeActv,
       "tmnxMobServProcUeDedBrDeActvFail": tmnxMobServProcUeDedBrDeActvFail,
       "tmnxMobServProcUeDedBrModify": tmnxMobServProcUeDedBrModify,
       "tmnxMobServProcUeDedBrModifyFail": tmnxMobServProcUeDedBrModifyFail,
       "tmnxMobServProcNwBrModify": tmnxMobServProcNwBrModify,
       "tmnxMobServProcNwBrModifyFail": tmnxMobServProcNwBrModifyFail,
       "tmnxMobServProcPDNSuspNotice": tmnxMobServProcPDNSuspNotice,
       "tmnxMobServProcPDNResumeNotice": tmnxMobServProcPDNResumeNotice,
       "tmnxMobServProcIRSR": tmnxMobServProcIRSR,
       "tmnxMobServProcEmergncyAttachSuc": tmnxMobServProcEmergncyAttachSuc,
       "tmnxMobServUeTable": tmnxMobServUeTable,
       "tmnxMobServUeEntry": tmnxMobServUeEntry,
       "tmnxMobServUeImsi": tmnxMobServUeImsi,
       "tmnxMobServUeRowStatus": tmnxMobServUeRowStatus,
       "tmnxMobServUeMsIsdn": tmnxMobServUeMsIsdn,
       "tmnxMobServUeImei": tmnxMobServUeImei,
       "tmnxMobServUeNai": tmnxMobServUeNai,
       "tmnxMobServUeNwkMcc": tmnxMobServUeNwkMcc,
       "tmnxMobServUeNwkMnc": tmnxMobServUeNwkMnc,
       "tmnxMobServUeTrackingAreaId": tmnxMobServUeTrackingAreaId,
       "tmnxMobServUeCellId": tmnxMobServUeCellId,
       "tmnxMobServUeState": tmnxMobServUeState,
       "tmnxMobServUeRat": tmnxMobServUeRat,
       "tmnxMobServUePdnContexts": tmnxMobServUePdnContexts,
       "tmnxMobServUeBearerContexts": tmnxMobServUeBearerContexts,
       "tmnxMobServUeChassisIndex": tmnxMobServUeChassisIndex,
       "tmnxMobServUeCardSlotNum": tmnxMobServUeCardSlotNum,
       "tmnxMobServUeS11MmeCtrlTeid": tmnxMobServUeS11MmeCtrlTeid,
       "tmnxMobServUeS11MmeCtrlAddrType": tmnxMobServUeS11MmeCtrlAddrType,
       "tmnxMobServUeS11MmeCtrlAddr": tmnxMobServUeS11MmeCtrlAddr,
       "tmnxMobServUeS11SgwCtrlTeid": tmnxMobServUeS11SgwCtrlTeid,
       "tmnxMobServUeS11SgwCtrlAddrType": tmnxMobServUeS11SgwCtrlAddrType,
       "tmnxMobServUeS11SgwCtrlAddr": tmnxMobServUeS11SgwCtrlAddr,
       "tmnxMobServUeS11InterEnbX2HandOv": tmnxMobServUeS11InterEnbX2HandOv,
       "tmnxMobServUeS11InterEnbS1HandOv": tmnxMobServUeS11InterEnbS1HandOv,
       "tmnxMobServUeS1ReleaseProcedures": tmnxMobServUeS1ReleaseProcedures,
       "tmnxMobServUePagingReq": tmnxMobServUePagingReq,
       "tmnxMobServUeRfSgwAddrType": tmnxMobServUeRfSgwAddrType,
       "tmnxMobServUeRfSgwAddr": tmnxMobServUeRfSgwAddr,
       "tmnxMobServUeIntraSgwIdleTau": tmnxMobServUeIntraSgwIdleTau,
       "tmnxMobServUeInitServReqProcs": tmnxMobServUeInitServReqProcs,
       "tmnxMobServUePagedCount": tmnxMobServUePagedCount,
       "tmnxMobServKeyType": tmnxMobServKeyType,
       "tmnxMobServUeImsiStr": tmnxMobServUeImsiStr,
       "tmnxMobServPdnContextTable": tmnxMobServPdnContextTable,
       "tmnxMobServPdnContextEntry": tmnxMobServPdnContextEntry,
       "tmnxMobServPcApn": tmnxMobServPcApn,
       "tmnxMobServPcPdnType": tmnxMobServPcPdnType,
       "tmnxMobServPcLinkedBearerId": tmnxMobServPcLinkedBearerId,
       "tmnxMobServPcApnRestriction": tmnxMobServPcApnRestriction,
       "tmnxMobServPcUlApnAmbr": tmnxMobServPcUlApnAmbr,
       "tmnxMobServPcDlApnAmbr": tmnxMobServPcDlApnAmbr,
       "tmnxMobServPcIpv4AddressType": tmnxMobServPcIpv4AddressType,
       "tmnxMobServPcIpv4Address": tmnxMobServPcIpv4Address,
       "tmnxMobServPcIpv6AddressType": tmnxMobServPcIpv6AddressType,
       "tmnxMobServPcIpv6Address": tmnxMobServPcIpv6Address,
       "tmnxMobServPcBearerContexts": tmnxMobServPcBearerContexts,
       "tmnxMobServPcSessionState": tmnxMobServPcSessionState,
       "tmnxMobServPcLastEvent": tmnxMobServPcLastEvent,
       "tmnxMobServPcS5S8SigProtocol": tmnxMobServPcS5S8SigProtocol,
       "tmnxMobServPcS5S8SgwCtrlTeid": tmnxMobServPcS5S8SgwCtrlTeid,
       "tmnxMobServPcS5S8SgwCtrlAddrType": tmnxMobServPcS5S8SgwCtrlAddrType,
       "tmnxMobServPcS5S8SgwCtrlAddr": tmnxMobServPcS5S8SgwCtrlAddr,
       "tmnxMobServPcS5S8PgwCtrlTeid": tmnxMobServPcS5S8PgwCtrlTeid,
       "tmnxMobServPcS5S8PgwCtrlAddrType": tmnxMobServPcS5S8PgwCtrlAddrType,
       "tmnxMobServPcS5S8PgwCtrlAddr": tmnxMobServPcS5S8PgwCtrlAddr,
       "tmnxMobServPcRfServerAddrType": tmnxMobServPcRfServerAddrType,
       "tmnxMobServPcRfServerAddr": tmnxMobServPcRfServerAddr,
       "tmnxMobServPcRfServerState": tmnxMobServPcRfServerState,
       "tmnxMobServPcRfBearerType": tmnxMobServPcRfBearerType,
       "tmnxMobServPcRfChargingLevel": tmnxMobServPcRfChargingLevel,
       "tmnxMobServPcRfChargingProfile": tmnxMobServPcRfChargingProfile,
       "tmnxMobServPcRfTriggeredRecords": tmnxMobServPcRfTriggeredRecords,
       "tmnxMobServPcRfInterimRecords": tmnxMobServPcRfInterimRecords,
       "tmnxMobServPcPcrfEventTriggers": tmnxMobServPcPcrfEventTriggers,
       "tmnxMobServPcGxcPcrfAddressType": tmnxMobServPcGxcPcrfAddressType,
       "tmnxMobServPcGxcPcrfAddress": tmnxMobServPcGxcPcrfAddress,
       "tmnxMobServPcGxcSgwAddressType": tmnxMobServPcGxcSgwAddressType,
       "tmnxMobServPcGxcSgwAddress": tmnxMobServPcGxcSgwAddress,
       "tmnxMobServPcS5S8SgwGreKey": tmnxMobServPcS5S8SgwGreKey,
       "tmnxMobServPcS5S8PgwGreKey": tmnxMobServPcS5S8PgwGreKey,
       "tmnxMobServPcS5S8PgwTrprtAdrType": tmnxMobServPcS5S8PgwTrprtAdrType,
       "tmnxMobServPcS5S8PgwTransprtAddr": tmnxMobServPcS5S8PgwTransprtAddr,
       "tmnxMobServPcS5S8SgwV6CtrlAdrTyp": tmnxMobServPcS5S8SgwV6CtrlAdrTyp,
       "tmnxMobServPcS5S8SgwV6CtrlAddr": tmnxMobServPcS5S8SgwV6CtrlAddr,
       "tmnxMobServPcS5S8PgwV6CtrlAdrTyp": tmnxMobServPcS5S8PgwV6CtrlAdrTyp,
       "tmnxMobServPcS5S8PgwV6CtrlAddr": tmnxMobServPcS5S8PgwV6CtrlAddr,
       "tmnxMobServPcAntiSpoofFailureCnt": tmnxMobServPcAntiSpoofFailureCnt,
       "tmnxMobServPcImsiAuthStatus": tmnxMobServPcImsiAuthStatus,
       "tmnxMobServPcImeiStr": tmnxMobServPcImeiStr,
       "tmnxMobServPcImsiStr": tmnxMobServPcImsiStr,
       "tmnxMobServPcRefPointType": tmnxMobServPcRefPointType,
       "tmnxMobServBearerContextTable": tmnxMobServBearerContextTable,
       "tmnxMobServBearerContextEntry": tmnxMobServBearerContextEntry,
       "tmnxMobServBcBearerId": tmnxMobServBcBearerId,
       "tmnxMobServBcBearerType": tmnxMobServBcBearerType,
       "tmnxMobServBcUpTime": tmnxMobServBcUpTime,
       "tmnxMobServBcQci": tmnxMobServBcQci,
       "tmnxMobServBcArp": tmnxMobServBcArp,
       "tmnxMobServBcSdfs": tmnxMobServBcSdfs,
       "tmnxMobServBcFilters": tmnxMobServBcFilters,
       "tmnxMobServBcQosUlMbr": tmnxMobServBcQosUlMbr,
       "tmnxMobServBcQosDlMbr": tmnxMobServBcQosDlMbr,
       "tmnxMobServBcQosUlGbr": tmnxMobServBcQosUlGbr,
       "tmnxMobServBcQosDlGbr": tmnxMobServBcQosDlGbr,
       "tmnxMobServBcS1uEnodebTeid": tmnxMobServBcS1uEnodebTeid,
       "tmnxMobServBcS1uEnodebAddrType": tmnxMobServBcS1uEnodebAddrType,
       "tmnxMobServBcS1uEnodebAddr": tmnxMobServBcS1uEnodebAddr,
       "tmnxMobServBcS1uSgwTeid": tmnxMobServBcS1uSgwTeid,
       "tmnxMobServBcS1uSgwAddrType": tmnxMobServBcS1uSgwAddrType,
       "tmnxMobServBcS1uSgwAddr": tmnxMobServBcS1uSgwAddr,
       "tmnxMobServBcS5S8SgwTeid": tmnxMobServBcS5S8SgwTeid,
       "tmnxMobServBcS5S8SgwDataAddrType": tmnxMobServBcS5S8SgwDataAddrType,
       "tmnxMobServBcS5S8SgwDataAddr": tmnxMobServBcS5S8SgwDataAddr,
       "tmnxMobServBcS5S8PgwTeid": tmnxMobServBcS5S8PgwTeid,
       "tmnxMobServBcS5S8PgwDataAddrType": tmnxMobServBcS5S8PgwDataAddrType,
       "tmnxMobServBcS5S8PgwDataAddr": tmnxMobServBcS5S8PgwDataAddr,
       "tmnxMobServBcS11QosModifications": tmnxMobServBcS11QosModifications,
       "tmnxMobServBcS5ULPackets": tmnxMobServBcS5ULPackets,
       "tmnxMobServBcS5ULBytes": tmnxMobServBcS5ULBytes,
       "tmnxMobServBcS1uDLPackets": tmnxMobServBcS1uDLPackets,
       "tmnxMobServBcS1uDLBytes": tmnxMobServBcS1uDLBytes,
       "tmnxMobServBcS5ULPacketsLow": tmnxMobServBcS5ULPacketsLow,
       "tmnxMobServBcS5ULPacketsHigh": tmnxMobServBcS5ULPacketsHigh,
       "tmnxMobServBcS5ULBytesLow": tmnxMobServBcS5ULBytesLow,
       "tmnxMobServBcS5ULBytesHigh": tmnxMobServBcS5ULBytesHigh,
       "tmnxMobServBcS1uDLPacketsLow": tmnxMobServBcS1uDLPacketsLow,
       "tmnxMobServBcS1uDLPacketsHigh": tmnxMobServBcS1uDLPacketsHigh,
       "tmnxMobServBcS1uDLBytesLow": tmnxMobServBcS1uDLBytesLow,
       "tmnxMobServBcS1uDLBytesHigh": tmnxMobServBcS1uDLBytesHigh,
       "tmnxMobServBcSetupLatencyTime": tmnxMobServBcSetupLatencyTime,
       "tmnxMobServBcIndTnlRemTeid": tmnxMobServBcIndTnlRemTeid,
       "tmnxMobServBcIndTnlRemAddrType": tmnxMobServBcIndTnlRemAddrType,
       "tmnxMobServBcIndTnlRemAddr": tmnxMobServBcIndTnlRemAddr,
       "tmnxMobServBcIndTnlLocalTeid": tmnxMobServBcIndTnlLocalTeid,
       "tmnxMobServBcIndTnlLocalAddrType": tmnxMobServBcIndTnlLocalAddrType,
       "tmnxMobServBcIndTnlLocalAddr": tmnxMobServBcIndTnlLocalAddr,
       "tmnxMobServBcRfServerAddrType": tmnxMobServBcRfServerAddrType,
       "tmnxMobServBcRfServerAddr": tmnxMobServBcRfServerAddr,
       "tmnxMobServBcRfServerState": tmnxMobServBcRfServerState,
       "tmnxMobServBcRfChargingProfile": tmnxMobServBcRfChargingProfile,
       "tmnxMobServBcRfTriggeredRecords": tmnxMobServBcRfTriggeredRecords,
       "tmnxMobServBcRfInterimRecords": tmnxMobServBcRfInterimRecords,
       "tmnxMobServBcRefPointType": tmnxMobServBcRefPointType,
       "tmnxMobServBcSdfTable": tmnxMobServBcSdfTable,
       "tmnxMobServBcSdfEntry": tmnxMobServBcSdfEntry,
       "tmnxMobServBcSdfPrecedence": tmnxMobServBcSdfPrecedence,
       "tmnxMobServBcSdfPcrfPrecedence": tmnxMobServBcSdfPcrfPrecedence,
       "tmnxMobServBcSdfRuleName": tmnxMobServBcSdfRuleName,
       "tmnxMobServBcSdfPacketFilters": tmnxMobServBcSdfPacketFilters,
       "tmnxMobServBcSdfQosUlMbr": tmnxMobServBcSdfQosUlMbr,
       "tmnxMobServBcSdfQosDlMbr": tmnxMobServBcSdfQosDlMbr,
       "tmnxMobServBcSdfQosUlGbr": tmnxMobServBcSdfQosUlGbr,
       "tmnxMobServBcSdfQosDlGbr": tmnxMobServBcSdfQosDlGbr,
       "tmnxMobServBcSdfFilterTable": tmnxMobServBcSdfFilterTable,
       "tmnxMobServBcSdfFilterEntry": tmnxMobServBcSdfFilterEntry,
       "tmnxMobServBcSdfFilterDirection": tmnxMobServBcSdfFilterDirection,
       "tmnxMobServBcSdfFilterId": tmnxMobServBcSdfFilterId,
       "tmnxMobServBcSdfFilterProtocol": tmnxMobServBcSdfFilterProtocol,
       "tmnxMobServBcSdfFilterSrcAdrType": tmnxMobServBcSdfFilterSrcAdrType,
       "tmnxMobServBcSdfFilterSrcAddr": tmnxMobServBcSdfFilterSrcAddr,
       "tmnxMobServBcSdfFilterSrcPfxLen": tmnxMobServBcSdfFilterSrcPfxLen,
       "tmnxMobServBcSdfFilterDstAdrType": tmnxMobServBcSdfFilterDstAdrType,
       "tmnxMobServBcSdfFilterDestAddr": tmnxMobServBcSdfFilterDestAddr,
       "tmnxMobServBcSdfFilterDestPfxLen": tmnxMobServBcSdfFilterDestPfxLen,
       "tmnxMobServBcSdfFilterSrcPorts": tmnxMobServBcSdfFilterSrcPorts,
       "tmnxMobServBcSdfFilterDestPorts": tmnxMobServBcSdfFilterDestPorts,
       "tmnxMobServBcSdfFirstSrcPortOper": tmnxMobServBcSdfFirstSrcPortOper,
       "tmnxMobServBcSdfFirstSrcPortVal1": tmnxMobServBcSdfFirstSrcPortVal1,
       "tmnxMobServBcSdfFirstSrcPortVal2": tmnxMobServBcSdfFirstSrcPortVal2,
       "tmnxMobServBcSdfSecndSrcPortOper": tmnxMobServBcSdfSecndSrcPortOper,
       "tmnxMobServBcSdfSecndSrcPortVal1": tmnxMobServBcSdfSecndSrcPortVal1,
       "tmnxMobServBcSdfSecndSrcPortVal2": tmnxMobServBcSdfSecndSrcPortVal2,
       "tmnxMobServBcSdfFirstDstPortOper": tmnxMobServBcSdfFirstDstPortOper,
       "tmnxMobServBcSdfFirstDstPortVal1": tmnxMobServBcSdfFirstDstPortVal1,
       "tmnxMobServBcSdfFirstDstPortVal2": tmnxMobServBcSdfFirstDstPortVal2,
       "tmnxMobServBcSdfSecndDstPortOper": tmnxMobServBcSdfSecndDstPortOper,
       "tmnxMobServBcSdfSecndDstPortVal1": tmnxMobServBcSdfSecndDstPortVal1,
       "tmnxMobServBcSdfSecndDstPortVal2": tmnxMobServBcSdfSecndDstPortVal2,
       "tmnxMobServBcTftFilterTable": tmnxMobServBcTftFilterTable,
       "tmnxMobServBcTftFilterEntry": tmnxMobServBcTftFilterEntry,
       "tmnxMobServBcTftFilterDirection": tmnxMobServBcTftFilterDirection,
       "tmnxMobServBcTftFilterId": tmnxMobServBcTftFilterId,
       "tmnxMobServBcTftFilterProtocol": tmnxMobServBcTftFilterProtocol,
       "tmnxMobServBcTftFilterSrcAdrType": tmnxMobServBcTftFilterSrcAdrType,
       "tmnxMobServBcTftFilterSrcAddr": tmnxMobServBcTftFilterSrcAddr,
       "tmnxMobServBcTftFilterSrcPfxLen": tmnxMobServBcTftFilterSrcPfxLen,
       "tmnxMobServBcTftFilterDstAdrType": tmnxMobServBcTftFilterDstAdrType,
       "tmnxMobServBcTftFilterDestAddr": tmnxMobServBcTftFilterDestAddr,
       "tmnxMobServBcTftFilterDestPfxLen": tmnxMobServBcTftFilterDestPfxLen,
       "tmnxMobServBcTftFilterSrcPorts": tmnxMobServBcTftFilterSrcPorts,
       "tmnxMobServBcTftFilterDestPorts": tmnxMobServBcTftFilterDestPorts,
       "tmnxMobServBcTftFirstSrcPortOper": tmnxMobServBcTftFirstSrcPortOper,
       "tmnxMobServBcTftFirstSrcPortVal1": tmnxMobServBcTftFirstSrcPortVal1,
       "tmnxMobServBcTftFirstSrcPortVal2": tmnxMobServBcTftFirstSrcPortVal2,
       "tmnxMobServBcTftSecndSrcPortOper": tmnxMobServBcTftSecndSrcPortOper,
       "tmnxMobServBcTftSecndSrcPortVal1": tmnxMobServBcTftSecndSrcPortVal1,
       "tmnxMobServBcTftSecndSrcPortVal2": tmnxMobServBcTftSecndSrcPortVal2,
       "tmnxMobServBcTftFirstDstPortOper": tmnxMobServBcTftFirstDstPortOper,
       "tmnxMobServBcTftFirstDstPortVal1": tmnxMobServBcTftFirstDstPortVal1,
       "tmnxMobServBcTftFirstDstPortVal2": tmnxMobServBcTftFirstDstPortVal2,
       "tmnxMobServBcTftSecndDstPortOper": tmnxMobServBcTftSecndDstPortOper,
       "tmnxMobServBcTftSecndDstPortVal1": tmnxMobServBcTftSecndDstPortVal1,
       "tmnxMobServBcTftSecndDstPortVal2": tmnxMobServBcTftSecndDstPortVal2,
       "tmnxMobServGxcStatTable": tmnxMobServGxcStatTable,
       "tmnxMobServGxcStatEntry": tmnxMobServGxcStatEntry,
       "tmnxMobServGxcPeerAddressType": tmnxMobServGxcPeerAddressType,
       "tmnxMobServGxcPeerAddress": tmnxMobServGxcPeerAddress,
       "tmnxMobServGxcPeerPort": tmnxMobServGxcPeerPort,
       "tmnxMobServGxcStatCcr": tmnxMobServGxcStatCcr,
       "tmnxMobServGxcStatCca": tmnxMobServGxcStatCca,
       "tmnxMobServGxcStatCcrFailures": tmnxMobServGxcStatCcrFailures,
       "tmnxMobServGxcStatRar": tmnxMobServGxcStatRar,
       "tmnxMobServGxcStatRaa": tmnxMobServGxcStatRaa,
       "tmnxMobServGxcStatBberf": tmnxMobServGxcStatBberf,
       "tmnxMobServGxcStatRxMalformedPkt": tmnxMobServGxcStatRxMalformedPkt,
       "tmnxMobServGxcStatRxUnknownPkts": tmnxMobServGxcStatRxUnknownPkts,
       "tmnxMobServGxcStatRxMissingIePkt": tmnxMobServGxcStatRxMissingIePkt,
       "tmnxMobServGxcStatStr": tmnxMobServGxcStatStr,
       "tmnxMobServGxcStatSta": tmnxMobServGxcStatSta,
       "tmnxMobServGxcStatAsr": tmnxMobServGxcStatAsr,
       "tmnxMobServGxcStatAsa": tmnxMobServGxcStatAsa,
       "tmnxMobServGxcStatCer": tmnxMobServGxcStatCer,
       "tmnxMobServGxcStatCea": tmnxMobServGxcStatCea,
       "tmnxMobServGxcStatDpr": tmnxMobServGxcStatDpr,
       "tmnxMobServGxcStatDpa": tmnxMobServGxcStatDpa,
       "tmnxMobServGxcStatDwr": tmnxMobServGxcStatDwr,
       "tmnxMobServGxcStatDwa": tmnxMobServGxcStatDwa,
       "tmnxMobServGxcStatPrProfStatus": tmnxMobServGxcStatPrProfStatus,
       "tmnxMobServGxcStatPrDetailStatus": tmnxMobServGxcStatPrDetailStatus,
       "tmnxMobServS11PeerTable": tmnxMobServS11PeerTable,
       "tmnxMobServS11PeerEntry": tmnxMobServS11PeerEntry,
       "tmnxMobServS11PeerAddressType": tmnxMobServS11PeerAddressType,
       "tmnxMobServS11PeerAddress": tmnxMobServS11PeerAddress,
       "tmnxMobServS11PeerPort": tmnxMobServS11PeerPort,
       "tmnxMobServS11PeerLastChanged": tmnxMobServS11PeerLastChanged,
       "tmnxMobServS11PeerCreateTime": tmnxMobServS11PeerCreateTime,
       "tmnxMobServS11PeerPathMgmtState": tmnxMobServS11PeerPathMgmtState,
       "tmnxMobServS11PeerGatewayId": tmnxMobServS11PeerGatewayId,
       "tmnxMobServS11StatTable": tmnxMobServS11StatTable,
       "tmnxMobServS11StatEntry": tmnxMobServS11StatEntry,
       "tmnxMobServS11StatCreateSessnReq": tmnxMobServS11StatCreateSessnReq,
       "tmnxMobServS11StatCreateSessnRsp": tmnxMobServS11StatCreateSessnRsp,
       "tmnxMobServS11StatDeleteSessnReq": tmnxMobServS11StatDeleteSessnReq,
       "tmnxMobServS11StatDeleteSessnRsp": tmnxMobServS11StatDeleteSessnRsp,
       "tmnxMobServS11StatCreateBearrReq": tmnxMobServS11StatCreateBearrReq,
       "tmnxMobServS11StatCreateBearrRsp": tmnxMobServS11StatCreateBearrRsp,
       "tmnxMobServS11StatDeleteBearrReq": tmnxMobServS11StatDeleteBearrReq,
       "tmnxMobServS11StatDeleteBearrRsp": tmnxMobServS11StatDeleteBearrRsp,
       "tmnxMobServS11StatModifyBearrReq": tmnxMobServS11StatModifyBearrReq,
       "tmnxMobServS11StatModifyBearrRsp": tmnxMobServS11StatModifyBearrRsp,
       "tmnxMobServS11StatRxEchoRequests": tmnxMobServS11StatRxEchoRequests,
       "tmnxMobServS11StatTxEchoResp": tmnxMobServS11StatTxEchoResp,
       "tmnxMobServS11StatTxEchoRequests": tmnxMobServS11StatTxEchoRequests,
       "tmnxMobServS11StatRxEchoResp": tmnxMobServS11StatRxEchoResp,
       "tmnxMobServS11StatTxDlNotify": tmnxMobServS11StatTxDlNotify,
       "tmnxMobServS11StatRxDlAcks": tmnxMobServS11StatRxDlAcks,
       "tmnxMobServS11StatRxDlFailNotify": tmnxMobServS11StatRxDlFailNotify,
       "tmnxMobServS11StatPagingSvcReq": tmnxMobServS11StatPagingSvcReq,
       "tmnxMobServS11StatRxMalfrmedPkts": tmnxMobServS11StatRxMalfrmedPkts,
       "tmnxMobServS11StatRxUnknownPkts": tmnxMobServS11StatRxUnknownPkts,
       "tmnxMobServS11StatRxMissngIePkts": tmnxMobServS11StatRxMissngIePkts,
       "tmnxMobServS11StatPeerRestarts": tmnxMobServS11StatPeerRestarts,
       "tmnxMobServS11StatPeerRestartCnt": tmnxMobServS11StatPeerRestartCnt,
       "tmnxMobServS11StatPathMgmtFails": tmnxMobServS11StatPathMgmtFails,
       "tmnxMobServS11StatRelBearersReq": tmnxMobServS11StatRelBearersReq,
       "tmnxMobServS11StatRelBearersResp": tmnxMobServS11StatRelBearersResp,
       "tmnxMobServS11StatCrtIndrTnlReq": tmnxMobServS11StatCrtIndrTnlReq,
       "tmnxMobServS11StatCrtIndrTnlResp": tmnxMobServS11StatCrtIndrTnlResp,
       "tmnxMobServS11StatDelIndrTnlReq": tmnxMobServS11StatDelIndrTnlReq,
       "tmnxMobServS11StatDelIndrTnlResp": tmnxMobServS11StatDelIndrTnlResp,
       "tmnxMobServS11StatBearersIpv4": tmnxMobServS11StatBearersIpv4,
       "tmnxMobServS11StatBearersIpv6": tmnxMobServS11StatBearersIpv6,
       "tmnxMobServS11StatBearerIpv4v6": tmnxMobServS11StatBearerIpv4v6,
       "tmnxMobServS11StatDedctdBearers": tmnxMobServS11StatDedctdBearers,
       "tmnxMobServS11StatBearers": tmnxMobServS11StatBearers,
       "tmnxMobServS11StatDefBearers": tmnxMobServS11StatDefBearers,
       "tmnxMobServS11StatRoamers": tmnxMobServS11StatRoamers,
       "tmnxMobServS11StatActiveBearers": tmnxMobServS11StatActiveBearers,
       "tmnxMobServS11StatIdleBearers": tmnxMobServS11StatIdleBearers,
       "tmnxMobServS11StatUpdateBearrReq": tmnxMobServS11StatUpdateBearrReq,
       "tmnxMobServS11StatUpdateBearrRsp": tmnxMobServS11StatUpdateBearrRsp,
       "tmnxMobServS11StatModifyBearrCmd": tmnxMobServS11StatModifyBearrCmd,
       "tmnxMobServS11StatModifyBearrFlr": tmnxMobServS11StatModifyBearrFlr,
       "tmnxMobServS11StatDeleteBearrCmd": tmnxMobServS11StatDeleteBearrCmd,
       "tmnxMobServS11StatDeleteBearrFlr": tmnxMobServS11StatDeleteBearrFlr,
       "tmnxMobServS11StatBearrResCmd": tmnxMobServS11StatBearrResCmd,
       "tmnxMobServS11StatBrrResFailInd": tmnxMobServS11StatBrrResFailInd,
       "tmnxMobServS11StatSuspNoticeReq": tmnxMobServS11StatSuspNoticeReq,
       "tmnxMobServS11StatSuspNoticeAck": tmnxMobServS11StatSuspNoticeAck,
       "tmnxMobServS11StatResNoticeReq": tmnxMobServS11StatResNoticeReq,
       "tmnxMobServS11StatResNoticeAck": tmnxMobServS11StatResNoticeAck,
       "tmnxMobServS11StatDelSesnRspFl": tmnxMobServS11StatDelSesnRspFl,
       "tmnxMobServS11StatUpdtBearrRspFl": tmnxMobServS11StatUpdtBearrRspFl,
       "tmnxMobServS11StatModBearrRspFl": tmnxMobServS11StatModBearrRspFl,
       "tmnxMobServS11StatDelBearrRspFl": tmnxMobServS11StatDelBearrRspFl,
       "tmnxMobServS11StatCreatBearRspFl": tmnxMobServS11StatCreatBearRspFl,
       "tmnxMobServS11StatCreatSesnRspFl": tmnxMobServS11StatCreatSesnRspFl,
       "tmnxMobServS11StatRelBearrRespFl": tmnxMobServS11StatRelBearrRespFl,
       "tmnxMobServS11StatCrtIndTnlRspFl": tmnxMobServS11StatCrtIndTnlRspFl,
       "tmnxMobServS11StatDelIndTnlRspFl": tmnxMobServS11StatDelIndTnlRspFl,
       "tmnxMobServS11StatRxDlAcksFail": tmnxMobServS11StatRxDlAcksFail,
       "tmnxMobServS1uPeerTable": tmnxMobServS1uPeerTable,
       "tmnxMobServS1uPeerEntry": tmnxMobServS1uPeerEntry,
       "tmnxMobServS1uPeerAddressType": tmnxMobServS1uPeerAddressType,
       "tmnxMobServS1uPeerAddress": tmnxMobServS1uPeerAddress,
       "tmnxMobServS1uPeerPort": tmnxMobServS1uPeerPort,
       "tmnxMobServS1uPeerLastChanged": tmnxMobServS1uPeerLastChanged,
       "tmnxMobServS1uPeerCreateTime": tmnxMobServS1uPeerCreateTime,
       "tmnxMobServS1uPeerPathMgmtState": tmnxMobServS1uPeerPathMgmtState,
       "tmnxMobServS1uPeerGatewayId": tmnxMobServS1uPeerGatewayId,
       "tmnxMobServS1uStatTable": tmnxMobServS1uStatTable,
       "tmnxMobServS1uStatEntry": tmnxMobServS1uStatEntry,
       "tmnxMobServS1uStatBcNotFound": tmnxMobServS1uStatBcNotFound,
       "tmnxMobServS1uStatRxEchoRequests": tmnxMobServS1uStatRxEchoRequests,
       "tmnxMobServS1uStatTxEchoResponse": tmnxMobServS1uStatTxEchoResponse,
       "tmnxMobServS1uStatTxEchoRequests": tmnxMobServS1uStatTxEchoRequests,
       "tmnxMobServS1uStatRxEchoResponse": tmnxMobServS1uStatRxEchoResponse,
       "tmnxMobServS1uStatPeerRestarts": tmnxMobServS1uStatPeerRestarts,
       "tmnxMobServS1uStatPeerRestartCnt": tmnxMobServS1uStatPeerRestartCnt,
       "tmnxMobServS1uStatPathMgmtFails": tmnxMobServS1uStatPathMgmtFails,
       "tmnxMobServS1uStatBearersIpv4": tmnxMobServS1uStatBearersIpv4,
       "tmnxMobServS1uStatBearersIpv6": tmnxMobServS1uStatBearersIpv6,
       "tmnxMobServS1uStatBearerIpv4v6": tmnxMobServS1uStatBearerIpv4v6,
       "tmnxMobServS1uStatDedctdBearers": tmnxMobServS1uStatDedctdBearers,
       "tmnxMobServS1uStatUlBytes": tmnxMobServS1uStatUlBytes,
       "tmnxMobServS1uStatDlBytes": tmnxMobServS1uStatDlBytes,
       "tmnxMobServS1uStatUlPackets": tmnxMobServS1uStatUlPackets,
       "tmnxMobServS1uStatDlPackets": tmnxMobServS1uStatDlPackets,
       "tmnxMobServS1uStatBearers": tmnxMobServS1uStatBearers,
       "tmnxMobServS1uStatDefBearers": tmnxMobServS1uStatDefBearers,
       "tmnxMobServS1uStatRoamers": tmnxMobServS1uStatRoamers,
       "tmnxMobServS1uStatActiveBearers": tmnxMobServS1uStatActiveBearers,
       "tmnxMobServS1uStatIdleBearers": tmnxMobServS1uStatIdleBearers,
       "tmnxMobSgwGaPeerTable": tmnxMobSgwGaPeerTable,
       "tmnxMobSgwGaPeerEntry": tmnxMobSgwGaPeerEntry,
       "tmnxMobSgwGaPeerLastChanged": tmnxMobSgwGaPeerLastChanged,
       "tmnxMobSgwGaPeerCreateTime": tmnxMobSgwGaPeerCreateTime,
       "tmnxMobSgwGaPeerPathMgmtState": tmnxMobSgwGaPeerPathMgmtState,
       "tmnxMobSgwGaPeerDetailState": tmnxMobSgwGaPeerDetailState,
       "tmnxMobSgwGaStatTable": tmnxMobSgwGaStatTable,
       "tmnxMobSgwGaStatEntry": tmnxMobSgwGaStatEntry,
       "tmnxMobSgwGaStatAddressType": tmnxMobSgwGaStatAddressType,
       "tmnxMobSgwGaStatAddress": tmnxMobSgwGaStatAddress,
       "tmnxMobSgwGaStatPort": tmnxMobSgwGaStatPort,
       "tmnxMobSgwGaStatLastChanged": tmnxMobSgwGaStatLastChanged,
       "tmnxMobSgwGaStatCreateTime": tmnxMobSgwGaStatCreateTime,
       "tmnxMobSgwGaStatRxEchoRequests": tmnxMobSgwGaStatRxEchoRequests,
       "tmnxMobSgwGaStatTxEchoResponses": tmnxMobSgwGaStatTxEchoResponses,
       "tmnxMobSgwGaStatTxEchoRequests": tmnxMobSgwGaStatTxEchoRequests,
       "tmnxMobSgwGaStatRxEchoResponses": tmnxMobSgwGaStatRxEchoResponses,
       "tmnxMobSgwGaStatRxNodeAlRequests": tmnxMobSgwGaStatRxNodeAlRequests,
       "tmnxMobSgwGaStatTxNodeAlResps": tmnxMobSgwGaStatTxNodeAlResps,
       "tmnxMobSgwGaStatTxDataRecReqs": tmnxMobSgwGaStatTxDataRecReqs,
       "tmnxMobSgwGaStatTxDataRecTferReq": tmnxMobSgwGaStatTxDataRecTferReq,
       "tmnxMobSgwGaStatRetrDataRecReqs": tmnxMobSgwGaStatRetrDataRecReqs,
       "tmnxMobSgwGaStatRxDataRecReqs": tmnxMobSgwGaStatRxDataRecReqs,
       "tmnxMobSgwGaStatUnackDataRexReqs": tmnxMobSgwGaStatUnackDataRexReqs,
       "tmnxMobSgwGaStatRxRedirectionReq": tmnxMobSgwGaStatRxRedirectionReq,
       "tmnxMobSgwGaStatTxRedrnResp": tmnxMobSgwGaStatTxRedrnResp,
       "tmnxMobSgwGaStatRxInvalidMsgs": tmnxMobSgwGaStatRxInvalidMsgs,
       "tmnxMobSgwGaStatRxVerNotSupp": tmnxMobSgwGaStatRxVerNotSupp,
       "tmnxMobSgwGaStatTxCdrTermination": tmnxMobSgwGaStatTxCdrTermination,
       "tmnxMobSgwGaStatTxCdrMaxChngCond": tmnxMobSgwGaStatTxCdrMaxChngCond,
       "tmnxMobSgwGaStatTxCdrMsTmzChng": tmnxMobSgwGaStatTxCdrMsTmzChng,
       "tmnxMobSgwGaStatTxCdrRatChng": tmnxMobSgwGaStatTxCdrRatChng,
       "tmnxMobSgwGaStatTxCdrTimeLimit": tmnxMobSgwGaStatTxCdrTimeLimit,
       "tmnxMobSgwGaStatTxCdrVolLimit": tmnxMobSgwGaStatTxCdrVolLimit,
       "tmnxMobSgwGaStatRxCdrReqAcc": tmnxMobSgwGaStatRxCdrReqAcc,
       "tmnxMobSgwGaStatRxCdrNoResAva": tmnxMobSgwGaStatRxCdrNoResAva,
       "tmnxMobSgwGaStatRxCdrReqNotFf": tmnxMobSgwGaStatRxCdrReqNotFf,
       "tmnxMobSgwGaStatRxCdrReqFfilled": tmnxMobSgwGaStatRxCdrReqFfilled,
       "tmnxMobSgwGaStatRxCdrDupReqFf": tmnxMobSgwGaStatRxCdrDupReqFf,
       "tmnxMobSgwGaStatRxCdrInvMsgFmat": tmnxMobSgwGaStatRxCdrInvMsgFmat,
       "tmnxMobSgwGaStatRxCdrVerNotSupp": tmnxMobSgwGaStatRxCdrVerNotSupp,
       "tmnxMobSgwGaStatRxCdrSrvcNotSupp": tmnxMobSgwGaStatRxCdrSrvcNotSupp,
       "tmnxMobSgwGaStatRxCdrMandIeInc": tmnxMobSgwGaStatRxCdrMandIeInc,
       "tmnxMobSgwGaStatRxCdrMandIeMiss": tmnxMobSgwGaStatRxCdrMandIeMiss,
       "tmnxMobSgwGaStatRxCdrOptIeInc": tmnxMobSgwGaStatRxCdrOptIeInc,
       "tmnxMobSgwGaStatRxCdrSystemFail": tmnxMobSgwGaStatRxCdrSystemFail,
       "tmnxMobSgwGaStatRtrEchoRequests": tmnxMobSgwGaStatRtrEchoRequests,
       "tmnxMobSgwGaStatGtpPrimeFail": tmnxMobSgwGaStatGtpPrimeFail,
       "tmnxMobSgwGaStatOperState": tmnxMobSgwGaStatOperState,
       "tmnxMobSgwGaStatUpTime": tmnxMobSgwGaStatUpTime,
       "tmnxMobSgwGaStatTxNodeAlRequests": tmnxMobSgwGaStatTxNodeAlRequests,
       "tmnxMobSgwGaStatRxNodeAlResps": tmnxMobSgwGaStatRxNodeAlResps,
       "tmnxMobSgwGaStatNodeAlReqRetried": tmnxMobSgwGaStatNodeAlReqRetried,
       "tmnxMobSgwGaStatCdrsTx": tmnxMobSgwGaStatCdrsTx,
       "tmnxMobSgwGaStatCdrsRx": tmnxMobSgwGaStatCdrsRx,
       "tmnxMobSgwGaStatTxCdrSerNdChLmt": tmnxMobSgwGaStatTxCdrSerNdChLmt,
       "tmnxMobSgwGaStatTxVerNotSupp": tmnxMobSgwGaStatTxVerNotSupp,
       "tmnxMobSgwGaStatTxCdrMgmtInterv": tmnxMobSgwGaStatTxCdrMgmtInterv,
       "tmnxMobServThresTable": tmnxMobServThresTable,
       "tmnxMobServThresEntry": tmnxMobServThresEntry,
       "tmnxMobServThresLastChanged": tmnxMobServThresLastChanged,
       "tmnxMobServThresBrMgmtLmtUe": tmnxMobServThresBrMgmtLmtUe,
       "tmnxMobServThresBrMgmtLmtBr": tmnxMobServThresBrMgmtLmtBr,
       "tmnxMobServThresBrMgmtLmtDefBr": tmnxMobServThresBrMgmtLmtDefBr,
       "tmnxMobServThresBrMgmtLmtDedBr": tmnxMobServThresBrMgmtLmtDedBr,
       "tmnxMobServThresBrMgmtLmtActBr": tmnxMobServThresBrMgmtLmtActBr,
       "tmnxMobServThresBrMgmtLmtUePgd": tmnxMobServThresBrMgmtLmtUePgd,
       "tmnxMobServThresBrMgmtCfsAttch": tmnxMobServThresBrMgmtCfsAttch,
       "tmnxMobServThresBrMgmtCfsDedBr": tmnxMobServThresBrMgmtCfsDedBr,
       "tmnxMobServThresBrMgmtCfsSvrReq": tmnxMobServThresBrMgmtCfsSvrReq,
       "tmnxMobServThresBrMgmtCfsItaRlc": tmnxMobServThresBrMgmtCfsItaRlc,
       "tmnxMobServThresBrMgmtCfsItrRlc": tmnxMobServThresBrMgmtCfsItrRlc,
       "tmnxMobServThresBrMgmtCfsIdlRlc": tmnxMobServThresBrMgmtCfsIdlRlc,
       "tmnxMobServThresBrMgmtCffAttch": tmnxMobServThresBrMgmtCffAttch,
       "tmnxMobServThresBrMgmtCffDedBr": tmnxMobServThresBrMgmtCffDedBr,
       "tmnxMobServThresBrMgmtCffPaging": tmnxMobServThresBrMgmtCffPaging,
       "tmnxMobServThresBrMgmtCffHdOver": tmnxMobServThresBrMgmtCffHdOver,
       "tmnxMobServThresBrMgmtCffSvrReq": tmnxMobServThresBrMgmtCffSvrReq,
       "tmnxMobServThresBrMgmtCffSrUnavl": tmnxMobServThresBrMgmtCffSrUnavl,
       "tmnxMobServThresBrTrfcThrptUL": tmnxMobServThresBrTrfcThrptUL,
       "tmnxMobServThresBrTrfcThrptDL": tmnxMobServThresBrTrfcThrptDL,
       "tmnxMobServThresPthMgmtS5Fail": tmnxMobServThresPthMgmtS5Fail,
       "tmnxMobServThresPthMgmtS5Restart": tmnxMobServThresPthMgmtS5Restart,
       "tmnxMobServThresPthMgmtS5NoResp": tmnxMobServThresPthMgmtS5NoResp,
       "tmnxMobServThresPthMgmtS11PrPath": tmnxMobServThresPthMgmtS11PrPath,
       "tmnxMobServThresPthMgmtS11PrRstt": tmnxMobServThresPthMgmtS11PrRstt,
       "tmnxMobServThresPthMgmtS11NoResp": tmnxMobServThresPthMgmtS11NoResp,
       "tmnxMobServThresPthMgmtS1UENB": tmnxMobServThresPthMgmtS1UENB,
       "tmnxMobServThresPthMgmtS11MME": tmnxMobServThresPthMgmtS11MME,
       "tmnxMobServThresPthMgmtS5Peer": tmnxMobServThresPthMgmtS5Peer,
       "tmnxMobServThresPthMgmtS8Peer": tmnxMobServThresPthMgmtS8Peer,
       "tmnxMobServThresPthMgmtRfFail": tmnxMobServThresPthMgmtRfFail,
       "tmnxMobServBcAcctGaTable": tmnxMobServBcAcctGaTable,
       "tmnxMobServBcAcctGaEntry": tmnxMobServBcAcctGaEntry,
       "tmnxMobServBcAcctGaChargingId": tmnxMobServBcAcctGaChargingId,
       "tmnxMobServBcAcctGaUlSustRate": tmnxMobServBcAcctGaUlSustRate,
       "tmnxMobServBcAcctGaDlSustRate": tmnxMobServBcAcctGaDlSustRate,
       "tmnxMobServBcAcctGaAggrUlPkts": tmnxMobServBcAcctGaAggrUlPkts,
       "tmnxMobServBcAcctGaAggrUlPktsLow": tmnxMobServBcAcctGaAggrUlPktsLow,
       "tmnxMobServBcAcctGaAggrUlPktsHi": tmnxMobServBcAcctGaAggrUlPktsHi,
       "tmnxMobServBcAcctGaAggrDlPkts": tmnxMobServBcAcctGaAggrDlPkts,
       "tmnxMobServBcAcctGaAggrDlPktsLow": tmnxMobServBcAcctGaAggrDlPktsLow,
       "tmnxMobServBcAcctGaAggrDlPktsHi": tmnxMobServBcAcctGaAggrDlPktsHi,
       "tmnxMobServBcAcctGaAggrUlByts": tmnxMobServBcAcctGaAggrUlByts,
       "tmnxMobServBcAcctGaAggrUlBytsLow": tmnxMobServBcAcctGaAggrUlBytsLow,
       "tmnxMobServBcAcctGaAggrUlBytsHi": tmnxMobServBcAcctGaAggrUlBytsHi,
       "tmnxMobServBcAcctGaAggrDlByts": tmnxMobServBcAcctGaAggrDlByts,
       "tmnxMobServBcAcctGaAggrDlBytsLow": tmnxMobServBcAcctGaAggrDlBytsLow,
       "tmnxMobServBcAcctGaAggrDlBytsHi": tmnxMobServBcAcctGaAggrDlBytsHi,
       "tmnxMobServBcAcctGaNumPartCdrs": tmnxMobServBcAcctGaNumPartCdrs,
       "tmnxMobServBcAcctGaNumTdvs": tmnxMobServBcAcctGaNumTdvs,
       "tmnxMobServBcAcctGaNumMaxChanges": tmnxMobServBcAcctGaNumMaxChanges,
       "tmnxMobServPcAcctRfTable": tmnxMobServPcAcctRfTable,
       "tmnxMobServPcAcctRfEntry": tmnxMobServPcAcctRfEntry,
       "tmnxMobServPcAcctRfAggrUlPkts": tmnxMobServPcAcctRfAggrUlPkts,
       "tmnxMobServPcAcctRfAggrUlPktsLow": tmnxMobServPcAcctRfAggrUlPktsLow,
       "tmnxMobServPcAcctRfAggrUlPktsHi": tmnxMobServPcAcctRfAggrUlPktsHi,
       "tmnxMobServPcAcctRfAggrDlPkts": tmnxMobServPcAcctRfAggrDlPkts,
       "tmnxMobServPcAcctRfAggrDlPktsLow": tmnxMobServPcAcctRfAggrDlPktsLow,
       "tmnxMobServPcAcctRfAggrDlPktsHi": tmnxMobServPcAcctRfAggrDlPktsHi,
       "tmnxMobServPcAcctRfAggrUlByts": tmnxMobServPcAcctRfAggrUlByts,
       "tmnxMobServPcAcctRfAggrUlBytsLow": tmnxMobServPcAcctRfAggrUlBytsLow,
       "tmnxMobServPcAcctRfAggrUlBytsHi": tmnxMobServPcAcctRfAggrUlBytsHi,
       "tmnxMobServPcAcctRfAggrDlByts": tmnxMobServPcAcctRfAggrDlByts,
       "tmnxMobServPcAcctRfAggrDlBytsLow": tmnxMobServPcAcctRfAggrDlBytsLow,
       "tmnxMobServPcAcctRfAggrDlBytsHi": tmnxMobServPcAcctRfAggrDlBytsHi,
       "tmnxMobServPcAcctRfUlAvgRate": tmnxMobServPcAcctRfUlAvgRate,
       "tmnxMobServPcAcctRfDlAvgRate": tmnxMobServPcAcctRfDlAvgRate,
       "tmnxMobServPcAcctRfNumIntrimSent": tmnxMobServPcAcctRfNumIntrimSent,
       "tmnxMobServS11CauseCodeTable": tmnxMobServS11CauseCodeTable,
       "tmnxMobServS11CauseCodeEntry": tmnxMobServS11CauseCodeEntry,
       "tmnxMobServS11CcRxReqAccepted": tmnxMobServS11CcRxReqAccepted,
       "tmnxMobServS11CcRxCtxNotFound": tmnxMobServS11CcRxCtxNotFound,
       "tmnxMobServS11CcRxInvalidLength": tmnxMobServS11CcRxInvalidLength,
       "tmnxMobServS11CcRxMndIeIncorrect": tmnxMobServS11CcRxMndIeIncorrect,
       "tmnxMobServS11CcRxMandIeMissing": tmnxMobServS11CcRxMandIeMissing,
       "tmnxMobServS11CcRxReqRejected": tmnxMobServS11CcRxReqRejected,
       "tmnxMobServS11CcRxRemPeerNoResp": tmnxMobServS11CcRxRemPeerNoResp,
       "tmnxMobServS11CcRxNoResAvailable": tmnxMobServS11CcRxNoResAvailable,
       "tmnxMobServS11CcRxUsrAuthFailure": tmnxMobServS11CcRxUsrAuthFailure,
       "tmnxMobServS11CcRxOthers": tmnxMobServS11CcRxOthers,
       "tmnxMobServS11CcTxReqAccepted": tmnxMobServS11CcTxReqAccepted,
       "tmnxMobServS11CcTxCtxNotFound": tmnxMobServS11CcTxCtxNotFound,
       "tmnxMobServS11CcTxInvalidLength": tmnxMobServS11CcTxInvalidLength,
       "tmnxMobServS11CcTxMndIeIncorrect": tmnxMobServS11CcTxMndIeIncorrect,
       "tmnxMobServS11CcTxMandIeMissing": tmnxMobServS11CcTxMandIeMissing,
       "tmnxMobServS11CcTxReqRejected": tmnxMobServS11CcTxReqRejected,
       "tmnxMobServS11CcTxRemPeerNoResp": tmnxMobServS11CcTxRemPeerNoResp,
       "tmnxMobServS11CcTxNoResAvailable": tmnxMobServS11CcTxNoResAvailable,
       "tmnxMobServS11CcTxUsrAuthFailure": tmnxMobServS11CcTxUsrAuthFailure,
       "tmnxMobServS11CcTxOthers": tmnxMobServS11CcTxOthers,
       "tmnxMobServingGlobalObjs": tmnxMobServingGlobalObjs,
       "tmnxMobServTableLastChanged": tmnxMobServTableLastChanged,
       "tmnxMobServSigTableLastChanged": tmnxMobServSigTableLastChanged,
       "tmnxMobServGxcTableLastChanged": tmnxMobServGxcTableLastChanged,
       "tmnxMobServS5TableLastChanged": tmnxMobServS5TableLastChanged,
       "tmnxMobServS8TableLastChanged": tmnxMobServS8TableLastChanged,
       "tmnxMobServS11TableLastChanged": tmnxMobServS11TableLastChanged,
       "tmnxMobServS1uTableLastChanged": tmnxMobServS1uTableLastChanged,
       "tmnxMobServS12TableLastChanged": tmnxMobServS12TableLastChanged,
       "tmnxMobServRfTableLastChanged": tmnxMobServRfTableLastChanged,
       "tmnxMobServApnTableLastChanged": tmnxMobServApnTableLastChanged,
       "tmnxMobServS11PeerTableLastChngd": tmnxMobServS11PeerTableLastChngd,
       "tmnxMobServS1uPeerTableLastChngd": tmnxMobServS1uPeerTableLastChngd,
       "tmnxMobServApTableLastChanged": tmnxMobServApTableLastChanged,
       "tmnxMobServGaTableLastChanged": tmnxMobServGaTableLastChanged,
       "tmnxMobSgwGaPeerTableLastChngd": tmnxMobSgwGaPeerTableLastChngd}
)
