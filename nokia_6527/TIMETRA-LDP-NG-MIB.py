# SNMP MIB module (TIMETRA-LDP-NG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-LDP-NG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:47 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(MplsLsrIdentifier,) = mibBuilder.importSymbols(
    "MPLS-LDP-MIB",
    "MplsLsrIdentifier")

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
 TestAndIncr,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(TFilterID,
 TFilterLogId) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterID",
    "TFilterLogId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxLabelSigStatus,
 TmnxLabelStatus,
 TmnxLdpAdjacencyType,
 TmnxLdpBackoffTime,
 TmnxLdpFECFlags,
 TmnxLdpFECPolicy,
 TmnxLdpFec129Tlv,
 TmnxLdpGenOperDownReasonCode,
 TmnxLdpHelloFactor,
 TmnxLdpHelloTimeout,
 TmnxLdpInLblWdrawalReasonCode,
 TmnxLdpIntTargOperDownReasonCode,
 TmnxLdpKeepAliveFactor,
 TmnxLdpLabelDistMethod,
 TmnxLdpNewHelloTimeout,
 TmnxLdpNewKeepAliveTimeout,
 TmnxVpnId,
 vRtrLdpSessOverloadDirection,
 vRtrLdpSessOverloadFecType,
 vRtrLdpSessOverloadState) = mibBuilder.importSymbols(
    "TIMETRA-LDP-MIB",
    "TmnxLabelSigStatus",
    "TmnxLabelStatus",
    "TmnxLdpAdjacencyType",
    "TmnxLdpBackoffTime",
    "TmnxLdpFECFlags",
    "TmnxLdpFECPolicy",
    "TmnxLdpFec129Tlv",
    "TmnxLdpGenOperDownReasonCode",
    "TmnxLdpHelloFactor",
    "TmnxLdpHelloTimeout",
    "TmnxLdpInLblWdrawalReasonCode",
    "TmnxLdpIntTargOperDownReasonCode",
    "TmnxLdpKeepAliveFactor",
    "TmnxLdpLabelDistMethod",
    "TmnxLdpNewHelloTimeout",
    "TmnxLdpNewKeepAliveTimeout",
    "TmnxVpnId",
    "vRtrLdpSessOverloadDirection",
    "vRtrLdpSessOverloadFecType",
    "vRtrLdpSessOverloadState")

(SdpId,
 ServType,
 TdmOptionsCasTrunkFraming,
 TdmOptionsSigPkts) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId",
    "ServType",
    "TdmOptionsCasTrunkFraming",
    "TdmOptionsSigPkts")

(TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxLdpFECType,
 TmnxMplsLdpNgIdType,
 TmnxMplsLdpNgIdentifier,
 TmnxMplsLsrNgIdentifier,
 TmnxOperState,
 TmnxServId,
 TmnxVRtrMplsLspID,
 TmnxVcId,
 TmnxVcType) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxLdpFECType",
    "TmnxMplsLdpNgIdType",
    "TmnxMplsLdpNgIdentifier",
    "TmnxMplsLsrNgIdentifier",
    "TmnxOperState",
    "TmnxServId",
    "TmnxVRtrMplsLspID",
    "TmnxVcId",
    "TmnxVcType")

(vRtrID,
 vRtrLdpStatus) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrLdpStatus")


# MODULE-IDENTITY

timetraLdpNgMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 91)
)
if mibBuilder.loadTexts:
    timetraLdpNgMIBModule.setRevisions(
        ("2014-02-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxLdpNgConformance_ObjectIdentity = ObjectIdentity
tmnxLdpNgConformance = _TmnxLdpNgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91)
)
_TmnxLdpNgCompliances_ObjectIdentity = ObjectIdentity
tmnxLdpNgCompliances = _TmnxLdpNgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 1)
)
_TmnxLdpNgGroups_ObjectIdentity = ObjectIdentity
tmnxLdpNgGroups = _TmnxLdpNgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2)
)
_TmnxLdpNgObjs_ObjectIdentity = ObjectIdentity
tmnxLdpNgObjs = _TmnxLdpNgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91)
)
_VRtrLdpNgIfTableLstChanged_Type = TimeStamp
_VRtrLdpNgIfTableLstChanged_Object = MibScalar
vRtrLdpNgIfTableLstChanged = _VRtrLdpNgIfTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 1),
    _VRtrLdpNgIfTableLstChanged_Type()
)
vRtrLdpNgIfTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgIfTableLstChanged.setStatus("current")
_VRtrLdpNgIfTable_Object = MibTable
vRtrLdpNgIfTable = _VRtrLdpNgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2)
)
if mibBuilder.loadTexts:
    vRtrLdpNgIfTable.setStatus("current")
_VRtrLdpNgIfEntry_Object = MibTableRow
vRtrLdpNgIfEntry = _VRtrLdpNgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2, 1)
)
vRtrLdpNgIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgIfEntry.setStatus("current")
_VRtrLdpNgIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpNgIfIndex_Object = MibTableColumn
vRtrLdpNgIfIndex = _VRtrLdpNgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2, 1, 1),
    _VRtrLdpNgIfIndex_Type()
)
vRtrLdpNgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgIfIndex.setStatus("current")
_VRtrLdpNgIfRowStatus_Type = RowStatus
_VRtrLdpNgIfRowStatus_Object = MibTableColumn
vRtrLdpNgIfRowStatus = _VRtrLdpNgIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2, 1, 2),
    _VRtrLdpNgIfRowStatus_Type()
)
vRtrLdpNgIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgIfRowStatus.setStatus("current")
_VRtrLdpNgIfLastChange_Type = TimeStamp
_VRtrLdpNgIfLastChange_Object = MibTableColumn
vRtrLdpNgIfLastChange = _VRtrLdpNgIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2, 1, 3),
    _VRtrLdpNgIfLastChange_Type()
)
vRtrLdpNgIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgIfLastChange.setStatus("current")


class _VRtrLdpNgIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpNgIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrLdpNgIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpNgIfAdminState_Object = MibTableColumn
vRtrLdpNgIfAdminState = _VRtrLdpNgIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2, 1, 4),
    _VRtrLdpNgIfAdminState_Type()
)
vRtrLdpNgIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgIfAdminState.setStatus("current")
_VRtrLdpNgIfOperState_Type = TmnxOperState
_VRtrLdpNgIfOperState_Object = MibTableColumn
vRtrLdpNgIfOperState = _VRtrLdpNgIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2, 1, 5),
    _VRtrLdpNgIfOperState_Type()
)
vRtrLdpNgIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgIfOperState.setStatus("current")
_VRtrLdpNgIfOperDownReason_Type = TmnxLdpIntTargOperDownReasonCode
_VRtrLdpNgIfOperDownReason_Object = MibTableColumn
vRtrLdpNgIfOperDownReason = _VRtrLdpNgIfOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2, 1, 6),
    _VRtrLdpNgIfOperDownReason_Type()
)
vRtrLdpNgIfOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgIfOperDownReason.setStatus("current")


class _VRtrLdpNgIfBfdEnabled_Type(Bits):
    """Custom type vRtrLdpNgIfBfdEnabled based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )

_VRtrLdpNgIfBfdEnabled_Type.__name__ = "Bits"
_VRtrLdpNgIfBfdEnabled_Object = MibTableColumn
vRtrLdpNgIfBfdEnabled = _VRtrLdpNgIfBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 2, 1, 7),
    _VRtrLdpNgIfBfdEnabled_Type()
)
vRtrLdpNgIfBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgIfBfdEnabled.setStatus("current")
_VRtrLdpNgHelloAdjTable_Object = MibTable
vRtrLdpNgHelloAdjTable = _VRtrLdpNgHelloAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3)
)
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjTable.setStatus("current")
_VRtrLdpNgHelloAdjEntry_Object = MibTableRow
vRtrLdpNgHelloAdjEntry = _VRtrLdpNgHelloAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1)
)
vRtrLdpNgHelloAdjEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfIndex"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddressType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjEntry.setStatus("current")
_VRtrLdpNgPeerLdpIdType_Type = TmnxMplsLdpNgIdType
_VRtrLdpNgPeerLdpIdType_Object = MibTableColumn
vRtrLdpNgPeerLdpIdType = _VRtrLdpNgPeerLdpIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 1),
    _VRtrLdpNgPeerLdpIdType_Type()
)
vRtrLdpNgPeerLdpIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgPeerLdpIdType.setStatus("current")


class _VRtrLdpNgPeerLdpId_Type(TmnxMplsLdpNgIdentifier):
    """Custom type vRtrLdpNgPeerLdpId based on TmnxMplsLdpNgIdentifier"""
    subtypeSpec = TmnxMplsLdpNgIdentifier.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(18, 18),
    )


_VRtrLdpNgPeerLdpId_Type.__name__ = "TmnxMplsLdpNgIdentifier"
_VRtrLdpNgPeerLdpId_Object = MibTableColumn
vRtrLdpNgPeerLdpId = _VRtrLdpNgPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 2),
    _VRtrLdpNgPeerLdpId_Type()
)
vRtrLdpNgPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgPeerLdpId.setStatus("current")
_VRtrLdpNgHelloAdjLclLdpIdType_Type = TmnxMplsLdpNgIdType
_VRtrLdpNgHelloAdjLclLdpIdType_Object = MibTableColumn
vRtrLdpNgHelloAdjLclLdpIdType = _VRtrLdpNgHelloAdjLclLdpIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 3),
    _VRtrLdpNgHelloAdjLclLdpIdType_Type()
)
vRtrLdpNgHelloAdjLclLdpIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjLclLdpIdType.setStatus("current")


class _VRtrLdpNgHelloAdjLclLdpId_Type(TmnxMplsLdpNgIdentifier):
    """Custom type vRtrLdpNgHelloAdjLclLdpId based on TmnxMplsLdpNgIdentifier"""
    subtypeSpec = TmnxMplsLdpNgIdentifier.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(18, 18),
    )


_VRtrLdpNgHelloAdjLclLdpId_Type.__name__ = "TmnxMplsLdpNgIdentifier"
_VRtrLdpNgHelloAdjLclLdpId_Object = MibTableColumn
vRtrLdpNgHelloAdjLclLdpId = _VRtrLdpNgHelloAdjLclLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 4),
    _VRtrLdpNgHelloAdjLclLdpId_Type()
)
vRtrLdpNgHelloAdjLclLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjLclLdpId.setStatus("current")


class _VRtrLdpNgHelloAdjEntityIndex_Type(Unsigned32):
    """Custom type vRtrLdpNgHelloAdjEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpNgHelloAdjEntityIndex_Type.__name__ = "Unsigned32"
_VRtrLdpNgHelloAdjEntityIndex_Object = MibTableColumn
vRtrLdpNgHelloAdjEntityIndex = _VRtrLdpNgHelloAdjEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 5),
    _VRtrLdpNgHelloAdjEntityIndex_Type()
)
vRtrLdpNgHelloAdjEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjEntityIndex.setStatus("current")


class _VRtrLdpNgHelloAdjIndex_Type(Unsigned32):
    """Custom type vRtrLdpNgHelloAdjIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpNgHelloAdjIndex_Type.__name__ = "Unsigned32"
_VRtrLdpNgHelloAdjIndex_Object = MibTableColumn
vRtrLdpNgHelloAdjIndex = _VRtrLdpNgHelloAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 6),
    _VRtrLdpNgHelloAdjIndex_Type()
)
vRtrLdpNgHelloAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjIndex.setStatus("current")
_VRtrLdpNgHelloAdjHoldTimeRem_Type = Unsigned32
_VRtrLdpNgHelloAdjHoldTimeRem_Object = MibTableColumn
vRtrLdpNgHelloAdjHoldTimeRem = _VRtrLdpNgHelloAdjHoldTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 7),
    _VRtrLdpNgHelloAdjHoldTimeRem_Type()
)
vRtrLdpNgHelloAdjHoldTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjHoldTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjHoldTimeRem.setUnits("seconds")
_VRtrLdpNgHelloAdjType_Type = TmnxLdpAdjacencyType
_VRtrLdpNgHelloAdjType_Object = MibTableColumn
vRtrLdpNgHelloAdjType = _VRtrLdpNgHelloAdjType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 8),
    _VRtrLdpNgHelloAdjType_Type()
)
vRtrLdpNgHelloAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjType.setStatus("current")
_VRtrLdpNgHelloAdjRemConfSeqNum_Type = Unsigned32
_VRtrLdpNgHelloAdjRemConfSeqNum_Object = MibTableColumn
vRtrLdpNgHelloAdjRemConfSeqNum = _VRtrLdpNgHelloAdjRemConfSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 9),
    _VRtrLdpNgHelloAdjRemConfSeqNum_Type()
)
vRtrLdpNgHelloAdjRemConfSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjRemConfSeqNum.setStatus("current")
_VRtrLdpNgHelloAdjRemIpAddrType_Type = InetAddressType
_VRtrLdpNgHelloAdjRemIpAddrType_Object = MibTableColumn
vRtrLdpNgHelloAdjRemIpAddrType = _VRtrLdpNgHelloAdjRemIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 10),
    _VRtrLdpNgHelloAdjRemIpAddrType_Type()
)
vRtrLdpNgHelloAdjRemIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjRemIpAddrType.setStatus("current")


class _VRtrLdpNgHelloAdjRemIpAddress_Type(InetAddress):
    """Custom type vRtrLdpNgHelloAdjRemIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgHelloAdjRemIpAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgHelloAdjRemIpAddress_Object = MibTableColumn
vRtrLdpNgHelloAdjRemIpAddress = _VRtrLdpNgHelloAdjRemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 11),
    _VRtrLdpNgHelloAdjRemIpAddress_Type()
)
vRtrLdpNgHelloAdjRemIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjRemIpAddress.setStatus("current")
_VRtrLdpNgHelloAdjUpTime_Type = TimeInterval
_VRtrLdpNgHelloAdjUpTime_Object = MibTableColumn
vRtrLdpNgHelloAdjUpTime = _VRtrLdpNgHelloAdjUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 12),
    _VRtrLdpNgHelloAdjUpTime_Type()
)
vRtrLdpNgHelloAdjUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjUpTime.setUnits("hundreds of seconds")
_VRtrLdpNgHelloAdjLclConfSeqNum_Type = Unsigned32
_VRtrLdpNgHelloAdjLclConfSeqNum_Object = MibTableColumn
vRtrLdpNgHelloAdjLclConfSeqNum = _VRtrLdpNgHelloAdjLclConfSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 13),
    _VRtrLdpNgHelloAdjLclConfSeqNum_Type()
)
vRtrLdpNgHelloAdjLclConfSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjLclConfSeqNum.setStatus("current")
_VRtrLdpNgHelloAdjLclIpAddrType_Type = InetAddressType
_VRtrLdpNgHelloAdjLclIpAddrType_Object = MibTableColumn
vRtrLdpNgHelloAdjLclIpAddrType = _VRtrLdpNgHelloAdjLclIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 14),
    _VRtrLdpNgHelloAdjLclIpAddrType_Type()
)
vRtrLdpNgHelloAdjLclIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjLclIpAddrType.setStatus("current")


class _VRtrLdpNgHelloAdjLclIpAddress_Type(InetAddress):
    """Custom type vRtrLdpNgHelloAdjLclIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgHelloAdjLclIpAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgHelloAdjLclIpAddress_Object = MibTableColumn
vRtrLdpNgHelloAdjLclIpAddress = _VRtrLdpNgHelloAdjLclIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 15),
    _VRtrLdpNgHelloAdjLclIpAddress_Type()
)
vRtrLdpNgHelloAdjLclIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjLclIpAddress.setStatus("current")
_VRtrLdpNgHelloAdjInHelloMsgCnt_Type = Counter32
_VRtrLdpNgHelloAdjInHelloMsgCnt_Object = MibTableColumn
vRtrLdpNgHelloAdjInHelloMsgCnt = _VRtrLdpNgHelloAdjInHelloMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 16),
    _VRtrLdpNgHelloAdjInHelloMsgCnt_Type()
)
vRtrLdpNgHelloAdjInHelloMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjInHelloMsgCnt.setStatus("current")
_VRtrLdpNgHelloAdjOutHelloMsgCnt_Type = Counter32
_VRtrLdpNgHelloAdjOutHelloMsgCnt_Object = MibTableColumn
vRtrLdpNgHelloAdjOutHelloMsgCnt = _VRtrLdpNgHelloAdjOutHelloMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 17),
    _VRtrLdpNgHelloAdjOutHelloMsgCnt_Type()
)
vRtrLdpNgHelloAdjOutHelloMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjOutHelloMsgCnt.setStatus("current")
_VRtrLdpNgHelloAdjLclTimeout_Type = TmnxLdpHelloTimeout
_VRtrLdpNgHelloAdjLclTimeout_Object = MibTableColumn
vRtrLdpNgHelloAdjLclTimeout = _VRtrLdpNgHelloAdjLclTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 18),
    _VRtrLdpNgHelloAdjLclTimeout_Type()
)
vRtrLdpNgHelloAdjLclTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjLclTimeout.setStatus("current")
_VRtrLdpNgHelloAdjRemTimeout_Type = TmnxLdpHelloTimeout
_VRtrLdpNgHelloAdjRemTimeout_Object = MibTableColumn
vRtrLdpNgHelloAdjRemTimeout = _VRtrLdpNgHelloAdjRemTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 19),
    _VRtrLdpNgHelloAdjRemTimeout_Type()
)
vRtrLdpNgHelloAdjRemTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjRemTimeout.setStatus("current")


class _VRtrLdpNgHelloAdjBfdStatus_Type(Integer32):
    """Custom type vRtrLdpNgHelloAdjBfdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noService", 1),
          ("inService", 2),
          ("outOfService", 3))
    )


_VRtrLdpNgHelloAdjBfdStatus_Type.__name__ = "Integer32"
_VRtrLdpNgHelloAdjBfdStatus_Object = MibTableColumn
vRtrLdpNgHelloAdjBfdStatus = _VRtrLdpNgHelloAdjBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 3, 1, 20),
    _VRtrLdpNgHelloAdjBfdStatus_Type()
)
vRtrLdpNgHelloAdjBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjBfdStatus.setStatus("current")
_VRtrLdpNgSessionTable_Object = MibTable
vRtrLdpNgSessionTable = _VRtrLdpNgSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4)
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionTable.setStatus("current")
_VRtrLdpNgSessionEntry_Object = MibTableRow
vRtrLdpNgSessionEntry = _VRtrLdpNgSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1)
)
vRtrLdpNgSessionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionEntry.setStatus("current")
_VRtrLdpNgSessLocalLdpIdType_Type = TmnxMplsLdpNgIdType
_VRtrLdpNgSessLocalLdpIdType_Object = MibTableColumn
vRtrLdpNgSessLocalLdpIdType = _VRtrLdpNgSessLocalLdpIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 1),
    _VRtrLdpNgSessLocalLdpIdType_Type()
)
vRtrLdpNgSessLocalLdpIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalLdpIdType.setStatus("current")


class _VRtrLdpNgSessLocalLdpId_Type(TmnxMplsLdpNgIdentifier):
    """Custom type vRtrLdpNgSessLocalLdpId based on TmnxMplsLdpNgIdentifier"""
    subtypeSpec = TmnxMplsLdpNgIdentifier.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(18, 18),
    )


_VRtrLdpNgSessLocalLdpId_Type.__name__ = "TmnxMplsLdpNgIdentifier"
_VRtrLdpNgSessLocalLdpId_Object = MibTableColumn
vRtrLdpNgSessLocalLdpId = _VRtrLdpNgSessLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 2),
    _VRtrLdpNgSessLocalLdpId_Type()
)
vRtrLdpNgSessLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalLdpId.setStatus("current")


class _VRtrLdpNgSessEntityIndex_Type(Unsigned32):
    """Custom type vRtrLdpNgSessEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpNgSessEntityIndex_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessEntityIndex_Object = MibTableColumn
vRtrLdpNgSessEntityIndex = _VRtrLdpNgSessEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 3),
    _VRtrLdpNgSessEntityIndex_Type()
)
vRtrLdpNgSessEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessEntityIndex.setStatus("current")
_VRtrLdpNgSessLabelDistMethod_Type = TmnxLdpLabelDistMethod
_VRtrLdpNgSessLabelDistMethod_Object = MibTableColumn
vRtrLdpNgSessLabelDistMethod = _VRtrLdpNgSessLabelDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 4),
    _VRtrLdpNgSessLabelDistMethod_Type()
)
vRtrLdpNgSessLabelDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLabelDistMethod.setStatus("current")


class _VRtrLdpNgSessLoopDetectForPV_Type(Integer32):
    """Custom type vRtrLdpNgSessLoopDetectForPV based on Integer32"""
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


_VRtrLdpNgSessLoopDetectForPV_Type.__name__ = "Integer32"
_VRtrLdpNgSessLoopDetectForPV_Object = MibTableColumn
vRtrLdpNgSessLoopDetectForPV = _VRtrLdpNgSessLoopDetectForPV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 5),
    _VRtrLdpNgSessLoopDetectForPV_Type()
)
vRtrLdpNgSessLoopDetectForPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLoopDetectForPV.setStatus("current")


class _VRtrLdpNgSessPathVectorLimit_Type(Unsigned32):
    """Custom type vRtrLdpNgSessPathVectorLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpNgSessPathVectorLimit_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessPathVectorLimit_Object = MibTableColumn
vRtrLdpNgSessPathVectorLimit = _VRtrLdpNgSessPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 6),
    _VRtrLdpNgSessPathVectorLimit_Type()
)
vRtrLdpNgSessPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPathVectorLimit.setStatus("current")


class _VRtrLdpNgSessState_Type(Integer32):
    """Custom type vRtrLdpNgSessState based on Integer32"""
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
        *(("nonexistent", 1),
          ("initialized", 2),
          ("openrec", 3),
          ("opensent", 4),
          ("operational", 5))
    )


_VRtrLdpNgSessState_Type.__name__ = "Integer32"
_VRtrLdpNgSessState_Object = MibTableColumn
vRtrLdpNgSessState = _VRtrLdpNgSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 7),
    _VRtrLdpNgSessState_Type()
)
vRtrLdpNgSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessState.setStatus("current")
_VRtrLdpNgSessAdjacencyType_Type = TmnxLdpAdjacencyType
_VRtrLdpNgSessAdjacencyType_Object = MibTableColumn
vRtrLdpNgSessAdjacencyType = _VRtrLdpNgSessAdjacencyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 8),
    _VRtrLdpNgSessAdjacencyType_Type()
)
vRtrLdpNgSessAdjacencyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessAdjacencyType.setStatus("current")
_VRtrLdpNgSessProtocolVersion_Type = Unsigned32
_VRtrLdpNgSessProtocolVersion_Object = MibTableColumn
vRtrLdpNgSessProtocolVersion = _VRtrLdpNgSessProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 9),
    _VRtrLdpNgSessProtocolVersion_Type()
)
vRtrLdpNgSessProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessProtocolVersion.setStatus("current")


class _VRtrLdpNgSessLocalUdpPort_Type(Unsigned32):
    """Custom type vRtrLdpNgSessLocalUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpNgSessLocalUdpPort_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessLocalUdpPort_Object = MibTableColumn
vRtrLdpNgSessLocalUdpPort = _VRtrLdpNgSessLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 10),
    _VRtrLdpNgSessLocalUdpPort_Type()
)
vRtrLdpNgSessLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalUdpPort.setStatus("current")


class _VRtrLdpNgSessPeerUdpPort_Type(Unsigned32):
    """Custom type vRtrLdpNgSessPeerUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpNgSessPeerUdpPort_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessPeerUdpPort_Object = MibTableColumn
vRtrLdpNgSessPeerUdpPort = _VRtrLdpNgSessPeerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 11),
    _VRtrLdpNgSessPeerUdpPort_Type()
)
vRtrLdpNgSessPeerUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerUdpPort.setStatus("current")


class _VRtrLdpNgSessLocalTcpPort_Type(Unsigned32):
    """Custom type vRtrLdpNgSessLocalTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpNgSessLocalTcpPort_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessLocalTcpPort_Object = MibTableColumn
vRtrLdpNgSessLocalTcpPort = _VRtrLdpNgSessLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 12),
    _VRtrLdpNgSessLocalTcpPort_Type()
)
vRtrLdpNgSessLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalTcpPort.setStatus("current")


class _VRtrLdpNgSessPeerTcpPort_Type(Unsigned32):
    """Custom type vRtrLdpNgSessPeerTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpNgSessPeerTcpPort_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessPeerTcpPort_Object = MibTableColumn
vRtrLdpNgSessPeerTcpPort = _VRtrLdpNgSessPeerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 13),
    _VRtrLdpNgSessPeerTcpPort_Type()
)
vRtrLdpNgSessPeerTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerTcpPort.setStatus("current")
_VRtrLdpNgSessLocalAddrType_Type = InetAddressType
_VRtrLdpNgSessLocalAddrType_Object = MibTableColumn
vRtrLdpNgSessLocalAddrType = _VRtrLdpNgSessLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 14),
    _VRtrLdpNgSessLocalAddrType_Type()
)
vRtrLdpNgSessLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalAddrType.setStatus("current")


class _VRtrLdpNgSessLocalAddress_Type(InetAddress):
    """Custom type vRtrLdpNgSessLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgSessLocalAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgSessLocalAddress_Object = MibTableColumn
vRtrLdpNgSessLocalAddress = _VRtrLdpNgSessLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 15),
    _VRtrLdpNgSessLocalAddress_Type()
)
vRtrLdpNgSessLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalAddress.setStatus("current")
_VRtrLdpNgSessPeerAddrType_Type = InetAddressType
_VRtrLdpNgSessPeerAddrType_Object = MibTableColumn
vRtrLdpNgSessPeerAddrType = _VRtrLdpNgSessPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 16),
    _VRtrLdpNgSessPeerAddrType_Type()
)
vRtrLdpNgSessPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerAddrType.setStatus("current")


class _VRtrLdpNgSessPeerAddress_Type(InetAddress):
    """Custom type vRtrLdpNgSessPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgSessPeerAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgSessPeerAddress_Object = MibTableColumn
vRtrLdpNgSessPeerAddress = _VRtrLdpNgSessPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 17),
    _VRtrLdpNgSessPeerAddress_Type()
)
vRtrLdpNgSessPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerAddress.setStatus("current")
_VRtrLdpNgSessKAHoldTimeRemaining_Type = TimeInterval
_VRtrLdpNgSessKAHoldTimeRemaining_Object = MibTableColumn
vRtrLdpNgSessKAHoldTimeRemaining = _VRtrLdpNgSessKAHoldTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 18),
    _VRtrLdpNgSessKAHoldTimeRemaining_Type()
)
vRtrLdpNgSessKAHoldTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessKAHoldTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessKAHoldTimeRemaining.setUnits("seconds")


class _VRtrLdpNgSessMaxPduLength_Type(Unsigned32):
    """Custom type vRtrLdpNgSessMaxPduLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrLdpNgSessMaxPduLength_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessMaxPduLength_Object = MibTableColumn
vRtrLdpNgSessMaxPduLength = _VRtrLdpNgSessMaxPduLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 19),
    _VRtrLdpNgSessMaxPduLength_Type()
)
vRtrLdpNgSessMaxPduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessMaxPduLength.setStatus("current")
_VRtrLdpNgSessUpTime_Type = TimeInterval
_VRtrLdpNgSessUpTime_Object = MibTableColumn
vRtrLdpNgSessUpTime = _VRtrLdpNgSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 20),
    _VRtrLdpNgSessUpTime_Type()
)
vRtrLdpNgSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessUpTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessUpTime.setUnits("hundreds of seconds")
_VRtrLdpNgSessLocalKATimeout_Type = TmnxLdpNewKeepAliveTimeout
_VRtrLdpNgSessLocalKATimeout_Object = MibTableColumn
vRtrLdpNgSessLocalKATimeout = _VRtrLdpNgSessLocalKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 21),
    _VRtrLdpNgSessLocalKATimeout_Type()
)
vRtrLdpNgSessLocalKATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalKATimeout.setStatus("current")
_VRtrLdpNgSessPeerKATimeout_Type = TmnxLdpNewKeepAliveTimeout
_VRtrLdpNgSessPeerKATimeout_Object = MibTableColumn
vRtrLdpNgSessPeerKATimeout = _VRtrLdpNgSessPeerKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 22),
    _VRtrLdpNgSessPeerKATimeout_Type()
)
vRtrLdpNgSessPeerKATimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerKATimeout.setStatus("current")


class _VRtrLdpNgSessAdvertise_Type(Integer32):
    """Custom type vRtrLdpNgSessAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("address", 1),
          ("service", 2),
          ("addressAndService", 3))
    )


_VRtrLdpNgSessAdvertise_Type.__name__ = "Integer32"
_VRtrLdpNgSessAdvertise_Object = MibTableColumn
vRtrLdpNgSessAdvertise = _VRtrLdpNgSessAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 23),
    _VRtrLdpNgSessAdvertise_Type()
)
vRtrLdpNgSessAdvertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessAdvertise.setStatus("current")
_VRtrLdpNgSessLclGRHelperState_Type = TruthValue
_VRtrLdpNgSessLclGRHelperState_Object = MibTableColumn
vRtrLdpNgSessLclGRHelperState = _VRtrLdpNgSessLclGRHelperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 24),
    _VRtrLdpNgSessLclGRHelperState_Type()
)
vRtrLdpNgSessLclGRHelperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLclGRHelperState.setStatus("current")
_VRtrLdpNgSessPeerGRState_Type = TruthValue
_VRtrLdpNgSessPeerGRState_Object = MibTableColumn
vRtrLdpNgSessPeerGRState = _VRtrLdpNgSessPeerGRState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 25),
    _VRtrLdpNgSessPeerGRState_Type()
)
vRtrLdpNgSessPeerGRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerGRState.setStatus("current")
_VRtrLdpNgSessPeerNumRestart_Type = Counter32
_VRtrLdpNgSessPeerNumRestart_Object = MibTableColumn
vRtrLdpNgSessPeerNumRestart = _VRtrLdpNgSessPeerNumRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 26),
    _VRtrLdpNgSessPeerNumRestart_Type()
)
vRtrLdpNgSessPeerNumRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerNumRestart.setStatus("current")
_VRtrLdpNgSessLastRestartTime_Type = TimeStamp
_VRtrLdpNgSessLastRestartTime_Object = MibTableColumn
vRtrLdpNgSessLastRestartTime = _VRtrLdpNgSessLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 27),
    _VRtrLdpNgSessLastRestartTime_Type()
)
vRtrLdpNgSessLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLastRestartTime.setStatus("current")
_VRtrLdpNgSessLocalFtReconTime_Type = Unsigned32
_VRtrLdpNgSessLocalFtReconTime_Object = MibTableColumn
vRtrLdpNgSessLocalFtReconTime = _VRtrLdpNgSessLocalFtReconTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 28),
    _VRtrLdpNgSessLocalFtReconTime_Type()
)
vRtrLdpNgSessLocalFtReconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalFtReconTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalFtReconTime.setUnits("seconds")
_VRtrLdpNgSessPeerFtReconTime_Type = Unsigned32
_VRtrLdpNgSessPeerFtReconTime_Object = MibTableColumn
vRtrLdpNgSessPeerFtReconTime = _VRtrLdpNgSessPeerFtReconTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 29),
    _VRtrLdpNgSessPeerFtReconTime_Type()
)
vRtrLdpNgSessPeerFtReconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerFtReconTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerFtReconTime.setUnits("seconds")
_VRtrLdpNgSessLocalFtRecovTime_Type = Unsigned32
_VRtrLdpNgSessLocalFtRecovTime_Object = MibTableColumn
vRtrLdpNgSessLocalFtRecovTime = _VRtrLdpNgSessLocalFtRecovTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 30),
    _VRtrLdpNgSessLocalFtRecovTime_Type()
)
vRtrLdpNgSessLocalFtRecovTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalFtRecovTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalFtRecovTime.setUnits("seconds")
_VRtrLdpNgSessPeerFtRecovTime_Type = Unsigned32
_VRtrLdpNgSessPeerFtRecovTime_Object = MibTableColumn
vRtrLdpNgSessPeerFtRecovTime = _VRtrLdpNgSessPeerFtRecovTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 31),
    _VRtrLdpNgSessPeerFtRecovTime_Type()
)
vRtrLdpNgSessPeerFtRecovTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerFtRecovTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerFtRecovTime.setUnits("seconds")
_VRtrLdpNgSessFtReconTimeRem_Type = Unsigned32
_VRtrLdpNgSessFtReconTimeRem_Object = MibTableColumn
vRtrLdpNgSessFtReconTimeRem = _VRtrLdpNgSessFtReconTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 32),
    _VRtrLdpNgSessFtReconTimeRem_Type()
)
vRtrLdpNgSessFtReconTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessFtReconTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessFtReconTimeRem.setUnits("seconds")
_VRtrLdpNgSessFtRecovTimeRem_Type = Unsigned32
_VRtrLdpNgSessFtRecovTimeRem_Object = MibTableColumn
vRtrLdpNgSessFtRecovTimeRem = _VRtrLdpNgSessFtRecovTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 33),
    _VRtrLdpNgSessFtRecovTimeRem_Type()
)
vRtrLdpNgSessFtRecovTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessFtRecovTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessFtRecovTimeRem.setUnits("seconds")


class _VRtrLdpNgSessBfdStatus_Type(Integer32):
    """Custom type vRtrLdpNgSessBfdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noService", 1),
          ("inService", 2),
          ("outOfService", 3))
    )


_VRtrLdpNgSessBfdStatus_Type.__name__ = "Integer32"
_VRtrLdpNgSessBfdStatus_Object = MibTableColumn
vRtrLdpNgSessBfdStatus = _VRtrLdpNgSessBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 34),
    _VRtrLdpNgSessBfdStatus_Type()
)
vRtrLdpNgSessBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessBfdStatus.setStatus("current")
_VRtrLdpNgSessLocalP2MPCap_Type = TruthValue
_VRtrLdpNgSessLocalP2MPCap_Object = MibTableColumn
vRtrLdpNgSessLocalP2MPCap = _VRtrLdpNgSessLocalP2MPCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 35),
    _VRtrLdpNgSessLocalP2MPCap_Type()
)
vRtrLdpNgSessLocalP2MPCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalP2MPCap.setStatus("current")
_VRtrLdpNgSessPeerP2MPCap_Type = TruthValue
_VRtrLdpNgSessPeerP2MPCap_Object = MibTableColumn
vRtrLdpNgSessPeerP2MPCap = _VRtrLdpNgSessPeerP2MPCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 36),
    _VRtrLdpNgSessPeerP2MPCap_Type()
)
vRtrLdpNgSessPeerP2MPCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerP2MPCap.setStatus("current")
_VRtrLdpNgSessLocalMPMBBCap_Type = TruthValue
_VRtrLdpNgSessLocalMPMBBCap_Object = MibTableColumn
vRtrLdpNgSessLocalMPMBBCap = _VRtrLdpNgSessLocalMPMBBCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 37),
    _VRtrLdpNgSessLocalMPMBBCap_Type()
)
vRtrLdpNgSessLocalMPMBBCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalMPMBBCap.setStatus("current")
_VRtrLdpNgSessPeerMPMBBCap_Type = TruthValue
_VRtrLdpNgSessPeerMPMBBCap_Object = MibTableColumn
vRtrLdpNgSessPeerMPMBBCap = _VRtrLdpNgSessPeerMPMBBCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 38),
    _VRtrLdpNgSessPeerMPMBBCap_Type()
)
vRtrLdpNgSessPeerMPMBBCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerMPMBBCap.setStatus("current")
_VRtrLdpNgSessLocalDynCap_Type = TruthValue
_VRtrLdpNgSessLocalDynCap_Object = MibTableColumn
vRtrLdpNgSessLocalDynCap = _VRtrLdpNgSessLocalDynCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 39),
    _VRtrLdpNgSessLocalDynCap_Type()
)
vRtrLdpNgSessLocalDynCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalDynCap.setStatus("current")
_VRtrLdpNgSessPeerDynCap_Type = TruthValue
_VRtrLdpNgSessPeerDynCap_Object = MibTableColumn
vRtrLdpNgSessPeerDynCap = _VRtrLdpNgSessPeerDynCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 40),
    _VRtrLdpNgSessPeerDynCap_Type()
)
vRtrLdpNgSessPeerDynCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerDynCap.setStatus("current")
_VRtrLdpNgSessLocalOLoadCap_Type = TruthValue
_VRtrLdpNgSessLocalOLoadCap_Object = MibTableColumn
vRtrLdpNgSessLocalOLoadCap = _VRtrLdpNgSessLocalOLoadCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 41),
    _VRtrLdpNgSessLocalOLoadCap_Type()
)
vRtrLdpNgSessLocalOLoadCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalOLoadCap.setStatus("current")
_VRtrLdpNgSessPeerOLoadCap_Type = TruthValue
_VRtrLdpNgSessPeerOLoadCap_Object = MibTableColumn
vRtrLdpNgSessPeerOLoadCap = _VRtrLdpNgSessPeerOLoadCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 42),
    _VRtrLdpNgSessPeerOLoadCap_Type()
)
vRtrLdpNgSessPeerOLoadCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerOLoadCap.setStatus("current")
_VRtrLdpNgSessIPv4PfxFecOLoadSent_Type = TruthValue
_VRtrLdpNgSessIPv4PfxFecOLoadSent_Object = MibTableColumn
vRtrLdpNgSessIPv4PfxFecOLoadSent = _VRtrLdpNgSessIPv4PfxFecOLoadSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 43),
    _VRtrLdpNgSessIPv4PfxFecOLoadSent_Type()
)
vRtrLdpNgSessIPv4PfxFecOLoadSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessIPv4PfxFecOLoadSent.setStatus("current")
_VRtrLdpNgSessIPv6PfxFecOLoadSent_Type = TruthValue
_VRtrLdpNgSessIPv6PfxFecOLoadSent_Object = MibTableColumn
vRtrLdpNgSessIPv6PfxFecOLoadSent = _VRtrLdpNgSessIPv6PfxFecOLoadSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 44),
    _VRtrLdpNgSessIPv6PfxFecOLoadSent_Type()
)
vRtrLdpNgSessIPv6PfxFecOLoadSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessIPv6PfxFecOLoadSent.setStatus("current")
_VRtrLdpNgSessIPv4PfxFecOLoadRecv_Type = TruthValue
_VRtrLdpNgSessIPv4PfxFecOLoadRecv_Object = MibTableColumn
vRtrLdpNgSessIPv4PfxFecOLoadRecv = _VRtrLdpNgSessIPv4PfxFecOLoadRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 45),
    _VRtrLdpNgSessIPv4PfxFecOLoadRecv_Type()
)
vRtrLdpNgSessIPv4PfxFecOLoadRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessIPv4PfxFecOLoadRecv.setStatus("current")
_VRtrLdpNgSessIPv6PfxFecOLoadRecv_Type = TruthValue
_VRtrLdpNgSessIPv6PfxFecOLoadRecv_Object = MibTableColumn
vRtrLdpNgSessIPv6PfxFecOLoadRecv = _VRtrLdpNgSessIPv6PfxFecOLoadRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 46),
    _VRtrLdpNgSessIPv6PfxFecOLoadRecv_Type()
)
vRtrLdpNgSessIPv6PfxFecOLoadRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessIPv6PfxFecOLoadRecv.setStatus("current")
_VRtrLdpNgSessIPv4P2MPFecOLSent_Type = TruthValue
_VRtrLdpNgSessIPv4P2MPFecOLSent_Object = MibTableColumn
vRtrLdpNgSessIPv4P2MPFecOLSent = _VRtrLdpNgSessIPv4P2MPFecOLSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 47),
    _VRtrLdpNgSessIPv4P2MPFecOLSent_Type()
)
vRtrLdpNgSessIPv4P2MPFecOLSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessIPv4P2MPFecOLSent.setStatus("current")
_VRtrLdpNgSessIPv6P2MPFecOLSent_Type = TruthValue
_VRtrLdpNgSessIPv6P2MPFecOLSent_Object = MibTableColumn
vRtrLdpNgSessIPv6P2MPFecOLSent = _VRtrLdpNgSessIPv6P2MPFecOLSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 48),
    _VRtrLdpNgSessIPv6P2MPFecOLSent_Type()
)
vRtrLdpNgSessIPv6P2MPFecOLSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessIPv6P2MPFecOLSent.setStatus("current")
_VRtrLdpNgSessIPv4P2MPFecOLRecv_Type = TruthValue
_VRtrLdpNgSessIPv4P2MPFecOLRecv_Object = MibTableColumn
vRtrLdpNgSessIPv4P2MPFecOLRecv = _VRtrLdpNgSessIPv4P2MPFecOLRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 49),
    _VRtrLdpNgSessIPv4P2MPFecOLRecv_Type()
)
vRtrLdpNgSessIPv4P2MPFecOLRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessIPv4P2MPFecOLRecv.setStatus("current")
_VRtrLdpNgSessIPv6P2MPFecOLRecv_Type = TruthValue
_VRtrLdpNgSessIPv6P2MPFecOLRecv_Object = MibTableColumn
vRtrLdpNgSessIPv6P2MPFecOLRecv = _VRtrLdpNgSessIPv6P2MPFecOLRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 50),
    _VRtrLdpNgSessIPv6P2MPFecOLRecv_Type()
)
vRtrLdpNgSessIPv6P2MPFecOLRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessIPv6P2MPFecOLRecv.setStatus("current")
_VRtrLdpNgSessSvcFec128OLoadSent_Type = TruthValue
_VRtrLdpNgSessSvcFec128OLoadSent_Object = MibTableColumn
vRtrLdpNgSessSvcFec128OLoadSent = _VRtrLdpNgSessSvcFec128OLoadSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 51),
    _VRtrLdpNgSessSvcFec128OLoadSent_Type()
)
vRtrLdpNgSessSvcFec128OLoadSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessSvcFec128OLoadSent.setStatus("current")
_VRtrLdpNgSessSvcFec128OLoadRecv_Type = TruthValue
_VRtrLdpNgSessSvcFec128OLoadRecv_Object = MibTableColumn
vRtrLdpNgSessSvcFec128OLoadRecv = _VRtrLdpNgSessSvcFec128OLoadRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 52),
    _VRtrLdpNgSessSvcFec128OLoadRecv_Type()
)
vRtrLdpNgSessSvcFec128OLoadRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessSvcFec128OLoadRecv.setStatus("current")
_VRtrLdpNgSessSvcFec129OLoadSent_Type = TruthValue
_VRtrLdpNgSessSvcFec129OLoadSent_Object = MibTableColumn
vRtrLdpNgSessSvcFec129OLoadSent = _VRtrLdpNgSessSvcFec129OLoadSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 53),
    _VRtrLdpNgSessSvcFec129OLoadSent_Type()
)
vRtrLdpNgSessSvcFec129OLoadSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessSvcFec129OLoadSent.setStatus("current")
_VRtrLdpNgSessSvcFec129OLoadRecv_Type = TruthValue
_VRtrLdpNgSessSvcFec129OLoadRecv_Object = MibTableColumn
vRtrLdpNgSessSvcFec129OLoadRecv = _VRtrLdpNgSessSvcFec129OLoadRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 54),
    _VRtrLdpNgSessSvcFec129OLoadRecv_Type()
)
vRtrLdpNgSessSvcFec129OLoadRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessSvcFec129OLoadRecv.setStatus("current")
_VRtrLdpNgSessLocalIPv4PfxFecCap_Type = TruthValue
_VRtrLdpNgSessLocalIPv4PfxFecCap_Object = MibTableColumn
vRtrLdpNgSessLocalIPv4PfxFecCap = _VRtrLdpNgSessLocalIPv4PfxFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 55),
    _VRtrLdpNgSessLocalIPv4PfxFecCap_Type()
)
vRtrLdpNgSessLocalIPv4PfxFecCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalIPv4PfxFecCap.setStatus("current")
_VRtrLdpNgSessPeerIPv4PfxFecCap_Type = TruthValue
_VRtrLdpNgSessPeerIPv4PfxFecCap_Object = MibTableColumn
vRtrLdpNgSessPeerIPv4PfxFecCap = _VRtrLdpNgSessPeerIPv4PfxFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 56),
    _VRtrLdpNgSessPeerIPv4PfxFecCap_Type()
)
vRtrLdpNgSessPeerIPv4PfxFecCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerIPv4PfxFecCap.setStatus("current")
_VRtrLdpNgSessLocalIPv6PfxFecCap_Type = TruthValue
_VRtrLdpNgSessLocalIPv6PfxFecCap_Object = MibTableColumn
vRtrLdpNgSessLocalIPv6PfxFecCap = _VRtrLdpNgSessLocalIPv6PfxFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 57),
    _VRtrLdpNgSessLocalIPv6PfxFecCap_Type()
)
vRtrLdpNgSessLocalIPv6PfxFecCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalIPv6PfxFecCap.setStatus("current")
_VRtrLdpNgSessPeerIPv6PfxFecCap_Type = TruthValue
_VRtrLdpNgSessPeerIPv6PfxFecCap_Object = MibTableColumn
vRtrLdpNgSessPeerIPv6PfxFecCap = _VRtrLdpNgSessPeerIPv6PfxFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 58),
    _VRtrLdpNgSessPeerIPv6PfxFecCap_Type()
)
vRtrLdpNgSessPeerIPv6PfxFecCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerIPv6PfxFecCap.setStatus("current")
_VRtrLdpNgSessLocalSvcFec128Cap_Type = TruthValue
_VRtrLdpNgSessLocalSvcFec128Cap_Object = MibTableColumn
vRtrLdpNgSessLocalSvcFec128Cap = _VRtrLdpNgSessLocalSvcFec128Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 59),
    _VRtrLdpNgSessLocalSvcFec128Cap_Type()
)
vRtrLdpNgSessLocalSvcFec128Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalSvcFec128Cap.setStatus("current")
_VRtrLdpNgSessPeerSvcFec128Cap_Type = TruthValue
_VRtrLdpNgSessPeerSvcFec128Cap_Object = MibTableColumn
vRtrLdpNgSessPeerSvcFec128Cap = _VRtrLdpNgSessPeerSvcFec128Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 60),
    _VRtrLdpNgSessPeerSvcFec128Cap_Type()
)
vRtrLdpNgSessPeerSvcFec128Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerSvcFec128Cap.setStatus("current")
_VRtrLdpNgSessLocalSvcFec129Cap_Type = TruthValue
_VRtrLdpNgSessLocalSvcFec129Cap_Object = MibTableColumn
vRtrLdpNgSessLocalSvcFec129Cap = _VRtrLdpNgSessLocalSvcFec129Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 61),
    _VRtrLdpNgSessLocalSvcFec129Cap_Type()
)
vRtrLdpNgSessLocalSvcFec129Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessLocalSvcFec129Cap.setStatus("current")
_VRtrLdpNgSessPeerSvcFec129Cap_Type = TruthValue
_VRtrLdpNgSessPeerSvcFec129Cap_Object = MibTableColumn
vRtrLdpNgSessPeerSvcFec129Cap = _VRtrLdpNgSessPeerSvcFec129Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 62),
    _VRtrLdpNgSessPeerSvcFec129Cap_Type()
)
vRtrLdpNgSessPeerSvcFec129Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeerSvcFec129Cap.setStatus("current")
_VRtrLdpNgSessOperMaxFecThreshold_Type = Unsigned32
_VRtrLdpNgSessOperMaxFecThreshold_Object = MibTableColumn
vRtrLdpNgSessOperMaxFecThreshold = _VRtrLdpNgSessOperMaxFecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 4, 1, 63),
    _VRtrLdpNgSessOperMaxFecThreshold_Type()
)
vRtrLdpNgSessOperMaxFecThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessOperMaxFecThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessOperMaxFecThreshold.setUnits("percentage")
_VRtrLdpNgTargPeerTunlLspTblLstCh_Type = TimeStamp
_VRtrLdpNgTargPeerTunlLspTblLstCh_Object = MibScalar
vRtrLdpNgTargPeerTunlLspTblLstCh = _VRtrLdpNgTargPeerTunlLspTblLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 5),
    _VRtrLdpNgTargPeerTunlLspTblLstCh_Type()
)
vRtrLdpNgTargPeerTunlLspTblLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerTunlLspTblLstCh.setStatus("current")
_VRtrLdpNgTargPeerTunnelLspTable_Object = MibTable
vRtrLdpNgTargPeerTunnelLspTable = _VRtrLdpNgTargPeerTunnelLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 6)
)
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerTunnelLspTable.setStatus("current")
_VRtrLdpNgTargPeerTunnelLspEntry_Object = MibTableRow
vRtrLdpNgTargPeerTunnelLspEntry = _VRtrLdpNgTargPeerTunnelLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 6, 1)
)
vRtrLdpNgTargPeerTunnelLspEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddressType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddress"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerLspId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerTunnelLspEntry.setStatus("current")
_VRtrLdpNgTargPeerLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpNgTargPeerLspId_Object = MibTableColumn
vRtrLdpNgTargPeerLspId = _VRtrLdpNgTargPeerLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 6, 1, 1),
    _VRtrLdpNgTargPeerLspId_Type()
)
vRtrLdpNgTargPeerLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerLspId.setStatus("current")
_VRtrLdpNgTargPeerLspRowStatus_Type = RowStatus
_VRtrLdpNgTargPeerLspRowStatus_Object = MibTableColumn
vRtrLdpNgTargPeerLspRowStatus = _VRtrLdpNgTargPeerLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 6, 1, 2),
    _VRtrLdpNgTargPeerLspRowStatus_Type()
)
vRtrLdpNgTargPeerLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerLspRowStatus.setStatus("current")
_VRtrLdpNgSessionParamsTableLstCh_Type = TimeStamp
_VRtrLdpNgSessionParamsTableLstCh_Object = MibScalar
vRtrLdpNgSessionParamsTableLstCh = _VRtrLdpNgSessionParamsTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 7),
    _VRtrLdpNgSessionParamsTableLstCh_Type()
)
vRtrLdpNgSessionParamsTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionParamsTableLstCh.setStatus("current")
_VRtrLdpNgSessionParamsTable_Object = MibTable
vRtrLdpNgSessionParamsTable = _VRtrLdpNgSessionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8)
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionParamsTable.setStatus("current")
_VRtrLdpNgSessionParamsEntry_Object = MibTableRow
vRtrLdpNgSessionParamsEntry = _VRtrLdpNgSessionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1)
)
vRtrLdpNgSessionParamsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddressType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionParamsEntry.setStatus("current")
_VRtrLdpNgSessParamRowStatus_Type = RowStatus
_VRtrLdpNgSessParamRowStatus_Object = MibTableColumn
vRtrLdpNgSessParamRowStatus = _VRtrLdpNgSessParamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 1),
    _VRtrLdpNgSessParamRowStatus_Type()
)
vRtrLdpNgSessParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamRowStatus.setStatus("current")


class _VRtrLdpNgSessParamAuth_Type(TruthValue):
    """Custom type vRtrLdpNgSessParamAuth based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgSessParamAuth_Type.__name__ = "TruthValue"
_VRtrLdpNgSessParamAuth_Object = MibTableColumn
vRtrLdpNgSessParamAuth = _VRtrLdpNgSessParamAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 2),
    _VRtrLdpNgSessParamAuth_Type()
)
vRtrLdpNgSessParamAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamAuth.setStatus("current")


class _VRtrLdpNgSessParamAuthKey_Type(OctetString):
    """Custom type vRtrLdpNgSessParamAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VRtrLdpNgSessParamAuthKey_Type.__name__ = "OctetString"
_VRtrLdpNgSessParamAuthKey_Object = MibTableColumn
vRtrLdpNgSessParamAuthKey = _VRtrLdpNgSessParamAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 3),
    _VRtrLdpNgSessParamAuthKey_Type()
)
vRtrLdpNgSessParamAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamAuthKey.setStatus("current")


class _VRtrLdpNgSessParamMinTTLValue_Type(Unsigned32):
    """Custom type vRtrLdpNgSessParamMinTTLValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_VRtrLdpNgSessParamMinTTLValue_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessParamMinTTLValue_Object = MibTableColumn
vRtrLdpNgSessParamMinTTLValue = _VRtrLdpNgSessParamMinTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 4),
    _VRtrLdpNgSessParamMinTTLValue_Type()
)
vRtrLdpNgSessParamMinTTLValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamMinTTLValue.setStatus("current")


class _VRtrLdpNgSessParamTTLLogId_Type(TFilterLogId):
    """Custom type vRtrLdpNgSessParamTTLLogId based on TFilterLogId"""
    defaultValue = 0


_VRtrLdpNgSessParamTTLLogId_Type.__name__ = "TFilterLogId"
_VRtrLdpNgSessParamTTLLogId_Object = MibTableColumn
vRtrLdpNgSessParamTTLLogId = _VRtrLdpNgSessParamTTLLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 5),
    _VRtrLdpNgSessParamTTLLogId_Type()
)
vRtrLdpNgSessParamTTLLogId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamTTLLogId.setStatus("current")


class _VRtrLdpNgSessParamAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type vRtrLdpNgSessParamAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_VRtrLdpNgSessParamAuthKeyChain_Object = MibTableColumn
vRtrLdpNgSessParamAuthKeyChain = _VRtrLdpNgSessParamAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 6),
    _VRtrLdpNgSessParamAuthKeyChain_Type()
)
vRtrLdpNgSessParamAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamAuthKeyChain.setStatus("current")


class _VRtrLdpNgSessParamDODLblDistrib_Type(TruthValue):
    """Custom type vRtrLdpNgSessParamDODLblDistrib based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgSessParamDODLblDistrib_Type.__name__ = "TruthValue"
_VRtrLdpNgSessParamDODLblDistrib_Object = MibTableColumn
vRtrLdpNgSessParamDODLblDistrib = _VRtrLdpNgSessParamDODLblDistrib_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 7),
    _VRtrLdpNgSessParamDODLblDistrib_Type()
)
vRtrLdpNgSessParamDODLblDistrib.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamDODLblDistrib.setStatus("current")


class _VRtrLdpNgSessParamImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamImportPolicy1_Object = MibTableColumn
vRtrLdpNgSessParamImportPolicy1 = _VRtrLdpNgSessParamImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 8),
    _VRtrLdpNgSessParamImportPolicy1_Type()
)
vRtrLdpNgSessParamImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamImportPolicy1.setStatus("current")


class _VRtrLdpNgSessParamImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamImportPolicy2_Object = MibTableColumn
vRtrLdpNgSessParamImportPolicy2 = _VRtrLdpNgSessParamImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 9),
    _VRtrLdpNgSessParamImportPolicy2_Type()
)
vRtrLdpNgSessParamImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamImportPolicy2.setStatus("current")


class _VRtrLdpNgSessParamImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamImportPolicy3_Object = MibTableColumn
vRtrLdpNgSessParamImportPolicy3 = _VRtrLdpNgSessParamImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 10),
    _VRtrLdpNgSessParamImportPolicy3_Type()
)
vRtrLdpNgSessParamImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamImportPolicy3.setStatus("current")


class _VRtrLdpNgSessParamImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamImportPolicy4_Object = MibTableColumn
vRtrLdpNgSessParamImportPolicy4 = _VRtrLdpNgSessParamImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 11),
    _VRtrLdpNgSessParamImportPolicy4_Type()
)
vRtrLdpNgSessParamImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamImportPolicy4.setStatus("current")


class _VRtrLdpNgSessParamImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamImportPolicy5_Object = MibTableColumn
vRtrLdpNgSessParamImportPolicy5 = _VRtrLdpNgSessParamImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 12),
    _VRtrLdpNgSessParamImportPolicy5_Type()
)
vRtrLdpNgSessParamImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamImportPolicy5.setStatus("current")


class _VRtrLdpNgSessParamExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamExportPolicy1_Object = MibTableColumn
vRtrLdpNgSessParamExportPolicy1 = _VRtrLdpNgSessParamExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 13),
    _VRtrLdpNgSessParamExportPolicy1_Type()
)
vRtrLdpNgSessParamExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamExportPolicy1.setStatus("current")


class _VRtrLdpNgSessParamExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamExportPolicy2_Object = MibTableColumn
vRtrLdpNgSessParamExportPolicy2 = _VRtrLdpNgSessParamExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 14),
    _VRtrLdpNgSessParamExportPolicy2_Type()
)
vRtrLdpNgSessParamExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamExportPolicy2.setStatus("current")


class _VRtrLdpNgSessParamExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamExportPolicy3_Object = MibTableColumn
vRtrLdpNgSessParamExportPolicy3 = _VRtrLdpNgSessParamExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 15),
    _VRtrLdpNgSessParamExportPolicy3_Type()
)
vRtrLdpNgSessParamExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamExportPolicy3.setStatus("current")


class _VRtrLdpNgSessParamExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamExportPolicy4_Object = MibTableColumn
vRtrLdpNgSessParamExportPolicy4 = _VRtrLdpNgSessParamExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 16),
    _VRtrLdpNgSessParamExportPolicy4_Type()
)
vRtrLdpNgSessParamExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamExportPolicy4.setStatus("current")


class _VRtrLdpNgSessParamExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgSessParamExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgSessParamExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgSessParamExportPolicy5_Object = MibTableColumn
vRtrLdpNgSessParamExportPolicy5 = _VRtrLdpNgSessParamExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 17),
    _VRtrLdpNgSessParamExportPolicy5_Type()
)
vRtrLdpNgSessParamExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamExportPolicy5.setStatus("current")


class _VRtrLdpNgSessFec129CiscoInterop_Type(TruthValue):
    """Custom type vRtrLdpNgSessFec129CiscoInterop based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgSessFec129CiscoInterop_Type.__name__ = "TruthValue"
_VRtrLdpNgSessFec129CiscoInterop_Object = MibTableColumn
vRtrLdpNgSessFec129CiscoInterop = _VRtrLdpNgSessFec129CiscoInterop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 18),
    _VRtrLdpNgSessFec129CiscoInterop_Type()
)
vRtrLdpNgSessFec129CiscoInterop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessFec129CiscoInterop.setStatus("current")


class _VRtrLdpNgSessParamPMTUDiscovery_Type(TruthValue):
    """Custom type vRtrLdpNgSessParamPMTUDiscovery based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgSessParamPMTUDiscovery_Type.__name__ = "TruthValue"
_VRtrLdpNgSessParamPMTUDiscovery_Object = MibTableColumn
vRtrLdpNgSessParamPMTUDiscovery = _VRtrLdpNgSessParamPMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 19),
    _VRtrLdpNgSessParamPMTUDiscovery_Type()
)
vRtrLdpNgSessParamPMTUDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamPMTUDiscovery.setStatus("current")


class _VRtrLdpNgSessParamAdvAdjAddrOnly_Type(TruthValue):
    """Custom type vRtrLdpNgSessParamAdvAdjAddrOnly based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgSessParamAdvAdjAddrOnly_Type.__name__ = "TruthValue"
_VRtrLdpNgSessParamAdvAdjAddrOnly_Object = MibTableColumn
vRtrLdpNgSessParamAdvAdjAddrOnly = _VRtrLdpNgSessParamAdvAdjAddrOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 20),
    _VRtrLdpNgSessParamAdvAdjAddrOnly_Type()
)
vRtrLdpNgSessParamAdvAdjAddrOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamAdvAdjAddrOnly.setStatus("current")


class _VRtrLdpNgSessPeIDMacFlushInterop_Type(TruthValue):
    """Custom type vRtrLdpNgSessPeIDMacFlushInterop based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgSessPeIDMacFlushInterop_Type.__name__ = "TruthValue"
_VRtrLdpNgSessPeIDMacFlushInterop_Object = MibTableColumn
vRtrLdpNgSessPeIDMacFlushInterop = _VRtrLdpNgSessPeIDMacFlushInterop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 21),
    _VRtrLdpNgSessPeIDMacFlushInterop_Type()
)
vRtrLdpNgSessPeIDMacFlushInterop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessPeIDMacFlushInterop.setStatus("current")


class _VRtrLdpNgSessParamIPv4PfxFecCap_Type(TmnxEnabledDisabled):
    """Custom type vRtrLdpNgSessParamIPv4PfxFecCap based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrLdpNgSessParamIPv4PfxFecCap_Type.__name__ = "TmnxEnabledDisabled"
_VRtrLdpNgSessParamIPv4PfxFecCap_Object = MibTableColumn
vRtrLdpNgSessParamIPv4PfxFecCap = _VRtrLdpNgSessParamIPv4PfxFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 22),
    _VRtrLdpNgSessParamIPv4PfxFecCap_Type()
)
vRtrLdpNgSessParamIPv4PfxFecCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamIPv4PfxFecCap.setStatus("current")


class _VRtrLdpNgSessParamIPv6PfxFecCap_Type(TmnxEnabledDisabled):
    """Custom type vRtrLdpNgSessParamIPv6PfxFecCap based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrLdpNgSessParamIPv6PfxFecCap_Type.__name__ = "TmnxEnabledDisabled"
_VRtrLdpNgSessParamIPv6PfxFecCap_Object = MibTableColumn
vRtrLdpNgSessParamIPv6PfxFecCap = _VRtrLdpNgSessParamIPv6PfxFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 23),
    _VRtrLdpNgSessParamIPv6PfxFecCap_Type()
)
vRtrLdpNgSessParamIPv6PfxFecCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamIPv6PfxFecCap.setStatus("current")


class _VRtrLdpNgSessParamP2MPFecCap_Type(TmnxEnabledDisabled):
    """Custom type vRtrLdpNgSessParamP2MPFecCap based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrLdpNgSessParamP2MPFecCap_Type.__name__ = "TmnxEnabledDisabled"
_VRtrLdpNgSessParamP2MPFecCap_Object = MibTableColumn
vRtrLdpNgSessParamP2MPFecCap = _VRtrLdpNgSessParamP2MPFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 24),
    _VRtrLdpNgSessParamP2MPFecCap_Type()
)
vRtrLdpNgSessParamP2MPFecCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamP2MPFecCap.setStatus("current")


class _VRtrLdpNgSessParamMaxFec_Type(Unsigned32):
    """Custom type vRtrLdpNgSessParamMaxFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpNgSessParamMaxFec_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessParamMaxFec_Object = MibTableColumn
vRtrLdpNgSessParamMaxFec = _VRtrLdpNgSessParamMaxFec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 25),
    _VRtrLdpNgSessParamMaxFec_Type()
)
vRtrLdpNgSessParamMaxFec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamMaxFec.setStatus("current")


class _VRtrLdpNgSessParamMaxFecLogOnly_Type(TruthValue):
    """Custom type vRtrLdpNgSessParamMaxFecLogOnly based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgSessParamMaxFecLogOnly_Type.__name__ = "TruthValue"
_VRtrLdpNgSessParamMaxFecLogOnly_Object = MibTableColumn
vRtrLdpNgSessParamMaxFecLogOnly = _VRtrLdpNgSessParamMaxFecLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 26),
    _VRtrLdpNgSessParamMaxFecLogOnly_Type()
)
vRtrLdpNgSessParamMaxFecLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamMaxFecLogOnly.setStatus("current")


class _VRtrLdpNgSessParamMaxFecThold_Type(Unsigned32):
    """Custom type vRtrLdpNgSessParamMaxFecThold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrLdpNgSessParamMaxFecThold_Type.__name__ = "Unsigned32"
_VRtrLdpNgSessParamMaxFecThold_Object = MibTableColumn
vRtrLdpNgSessParamMaxFecThold = _VRtrLdpNgSessParamMaxFecThold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 8, 1, 27),
    _VRtrLdpNgSessParamMaxFecThold_Type()
)
vRtrLdpNgSessParamMaxFecThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamMaxFecThold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgSessParamMaxFecThold.setUnits("percentage")
_VRtrLdpNgSessionAddrTable_Object = MibTable
vRtrLdpNgSessionAddrTable = _VRtrLdpNgSessionAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 9)
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionAddrTable.setStatus("current")
_VRtrLdpNgSessionAddrEntry_Object = MibTableRow
vRtrLdpNgSessionAddrEntry = _VRtrLdpNgSessionAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 9, 1)
)
vRtrLdpNgSessionAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionAddrEntry.setStatus("current")
_VRtrLdpNgSessAddrLclLdpIdType_Type = TmnxMplsLdpNgIdType
_VRtrLdpNgSessAddrLclLdpIdType_Object = MibTableColumn
vRtrLdpNgSessAddrLclLdpIdType = _VRtrLdpNgSessAddrLclLdpIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 9, 1, 1),
    _VRtrLdpNgSessAddrLclLdpIdType_Type()
)
vRtrLdpNgSessAddrLclLdpIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessAddrLclLdpIdType.setStatus("current")


class _VRtrLdpNgSessionAddrLocalLdpId_Type(TmnxMplsLdpNgIdentifier):
    """Custom type vRtrLdpNgSessionAddrLocalLdpId based on TmnxMplsLdpNgIdentifier"""
    subtypeSpec = TmnxMplsLdpNgIdentifier.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(18, 18),
    )


_VRtrLdpNgSessionAddrLocalLdpId_Type.__name__ = "TmnxMplsLdpNgIdentifier"
_VRtrLdpNgSessionAddrLocalLdpId_Object = MibTableColumn
vRtrLdpNgSessionAddrLocalLdpId = _VRtrLdpNgSessionAddrLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 9, 1, 2),
    _VRtrLdpNgSessionAddrLocalLdpId_Type()
)
vRtrLdpNgSessionAddrLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionAddrLocalLdpId.setStatus("current")
_VRtrLdpNgSessionAddrNumInAddrs_Type = Unsigned32
_VRtrLdpNgSessionAddrNumInAddrs_Object = MibTableColumn
vRtrLdpNgSessionAddrNumInAddrs = _VRtrLdpNgSessionAddrNumInAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 9, 1, 3),
    _VRtrLdpNgSessionAddrNumInAddrs_Type()
)
vRtrLdpNgSessionAddrNumInAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionAddrNumInAddrs.setStatus("current")
_VRtrLdpNgSessionAddrNumOutAddrs_Type = Unsigned32
_VRtrLdpNgSessionAddrNumOutAddrs_Object = MibTableColumn
vRtrLdpNgSessionAddrNumOutAddrs = _VRtrLdpNgSessionAddrNumOutAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 9, 1, 4),
    _VRtrLdpNgSessionAddrNumOutAddrs_Type()
)
vRtrLdpNgSessionAddrNumOutAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionAddrNumOutAddrs.setStatus("current")
_VRtrLdpNgSessionInAddrTable_Object = MibTable
vRtrLdpNgSessionInAddrTable = _VRtrLdpNgSessionInAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 10)
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionInAddrTable.setStatus("current")
_VRtrLdpNgSessionInAddrEntry_Object = MibTableRow
vRtrLdpNgSessionInAddrEntry = _VRtrLdpNgSessionInAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 10, 1)
)
vRtrLdpNgSessionInAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionInAddrAddrType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionInAddrAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionInAddrEntry.setStatus("current")
_VRtrLdpNgSessionInAddrAddrType_Type = InetAddressType
_VRtrLdpNgSessionInAddrAddrType_Object = MibTableColumn
vRtrLdpNgSessionInAddrAddrType = _VRtrLdpNgSessionInAddrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 10, 1, 1),
    _VRtrLdpNgSessionInAddrAddrType_Type()
)
vRtrLdpNgSessionInAddrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionInAddrAddrType.setStatus("current")


class _VRtrLdpNgSessionInAddrAddress_Type(InetAddress):
    """Custom type vRtrLdpNgSessionInAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgSessionInAddrAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgSessionInAddrAddress_Object = MibTableColumn
vRtrLdpNgSessionInAddrAddress = _VRtrLdpNgSessionInAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 10, 1, 2),
    _VRtrLdpNgSessionInAddrAddress_Type()
)
vRtrLdpNgSessionInAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionInAddrAddress.setStatus("current")
_VRtrLdpNgSessInAddrLclLdpIdType_Type = TmnxMplsLdpNgIdType
_VRtrLdpNgSessInAddrLclLdpIdType_Object = MibTableColumn
vRtrLdpNgSessInAddrLclLdpIdType = _VRtrLdpNgSessInAddrLclLdpIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 10, 1, 3),
    _VRtrLdpNgSessInAddrLclLdpIdType_Type()
)
vRtrLdpNgSessInAddrLclLdpIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessInAddrLclLdpIdType.setStatus("current")


class _VRtrLdpNgSessionInAddrLocalLdpId_Type(TmnxMplsLdpNgIdentifier):
    """Custom type vRtrLdpNgSessionInAddrLocalLdpId based on TmnxMplsLdpNgIdentifier"""
    subtypeSpec = TmnxMplsLdpNgIdentifier.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(18, 18),
    )


_VRtrLdpNgSessionInAddrLocalLdpId_Type.__name__ = "TmnxMplsLdpNgIdentifier"
_VRtrLdpNgSessionInAddrLocalLdpId_Object = MibTableColumn
vRtrLdpNgSessionInAddrLocalLdpId = _VRtrLdpNgSessionInAddrLocalLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 10, 1, 4),
    _VRtrLdpNgSessionInAddrLocalLdpId_Type()
)
vRtrLdpNgSessionInAddrLocalLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionInAddrLocalLdpId.setStatus("current")
_VRtrLdpNgSessionOutAddrTable_Object = MibTable
vRtrLdpNgSessionOutAddrTable = _VRtrLdpNgSessionOutAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 11)
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionOutAddrTable.setStatus("current")
_VRtrLdpNgSessionOutAddrEntry_Object = MibTableRow
vRtrLdpNgSessionOutAddrEntry = _VRtrLdpNgSessionOutAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 11, 1)
)
vRtrLdpNgSessionOutAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionOutAddrAddrType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionOutAddrAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionOutAddrEntry.setStatus("current")
_VRtrLdpNgSessionOutAddrAddrType_Type = InetAddressType
_VRtrLdpNgSessionOutAddrAddrType_Object = MibTableColumn
vRtrLdpNgSessionOutAddrAddrType = _VRtrLdpNgSessionOutAddrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 11, 1, 1),
    _VRtrLdpNgSessionOutAddrAddrType_Type()
)
vRtrLdpNgSessionOutAddrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionOutAddrAddrType.setStatus("current")


class _VRtrLdpNgSessionOutAddrAddress_Type(InetAddress):
    """Custom type vRtrLdpNgSessionOutAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgSessionOutAddrAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgSessionOutAddrAddress_Object = MibTableColumn
vRtrLdpNgSessionOutAddrAddress = _VRtrLdpNgSessionOutAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 11, 1, 2),
    _VRtrLdpNgSessionOutAddrAddress_Type()
)
vRtrLdpNgSessionOutAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionOutAddrAddress.setStatus("current")
_VRtrLdpNgSessOutAddrLclLdpIdType_Type = TmnxMplsLdpNgIdType
_VRtrLdpNgSessOutAddrLclLdpIdType_Object = MibTableColumn
vRtrLdpNgSessOutAddrLclLdpIdType = _VRtrLdpNgSessOutAddrLclLdpIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 11, 1, 3),
    _VRtrLdpNgSessOutAddrLclLdpIdType_Type()
)
vRtrLdpNgSessOutAddrLclLdpIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessOutAddrLclLdpIdType.setStatus("current")


class _VRtrLdpNgSessionOutAddrLclLdpId_Type(TmnxMplsLdpNgIdentifier):
    """Custom type vRtrLdpNgSessionOutAddrLclLdpId based on TmnxMplsLdpNgIdentifier"""
    subtypeSpec = TmnxMplsLdpNgIdentifier.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(18, 18),
    )


_VRtrLdpNgSessionOutAddrLclLdpId_Type.__name__ = "TmnxMplsLdpNgIdentifier"
_VRtrLdpNgSessionOutAddrLclLdpId_Object = MibTableColumn
vRtrLdpNgSessionOutAddrLclLdpId = _VRtrLdpNgSessionOutAddrLclLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 11, 1, 4),
    _VRtrLdpNgSessionOutAddrLclLdpId_Type()
)
vRtrLdpNgSessionOutAddrLclLdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessionOutAddrLclLdpId.setStatus("current")
_VRtrLdpNgAddrFecTable_Object = MibTable
vRtrLdpNgAddrFecTable = _VRtrLdpNgAddrFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12)
)
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecTable.setStatus("current")
_VRtrLdpNgAddrFecEntry_Object = MibTableRow
vRtrLdpNgAddrFecEntry = _VRtrLdpNgAddrFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12, 1)
)
vRtrLdpNgAddrFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecFecType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefixType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefix"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefixLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecEntry.setStatus("current")
_VRtrLdpNgAddrFecFecType_Type = TmnxLdpFECType
_VRtrLdpNgAddrFecFecType_Object = MibTableColumn
vRtrLdpNgAddrFecFecType = _VRtrLdpNgAddrFecFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12, 1, 1),
    _VRtrLdpNgAddrFecFecType_Type()
)
vRtrLdpNgAddrFecFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecFecType.setStatus("current")
_VRtrLdpNgAddrFecIpPrefixType_Type = InetAddressType
_VRtrLdpNgAddrFecIpPrefixType_Object = MibTableColumn
vRtrLdpNgAddrFecIpPrefixType = _VRtrLdpNgAddrFecIpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12, 1, 2),
    _VRtrLdpNgAddrFecIpPrefixType_Type()
)
vRtrLdpNgAddrFecIpPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecIpPrefixType.setStatus("current")


class _VRtrLdpNgAddrFecIpPrefix_Type(InetAddress):
    """Custom type vRtrLdpNgAddrFecIpPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgAddrFecIpPrefix_Type.__name__ = "InetAddress"
_VRtrLdpNgAddrFecIpPrefix_Object = MibTableColumn
vRtrLdpNgAddrFecIpPrefix = _VRtrLdpNgAddrFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12, 1, 3),
    _VRtrLdpNgAddrFecIpPrefix_Type()
)
vRtrLdpNgAddrFecIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecIpPrefix.setStatus("current")


class _VRtrLdpNgAddrFecIpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type vRtrLdpNgAddrFecIpPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VRtrLdpNgAddrFecIpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_VRtrLdpNgAddrFecIpPrefixLen_Object = MibTableColumn
vRtrLdpNgAddrFecIpPrefixLen = _VRtrLdpNgAddrFecIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12, 1, 4),
    _VRtrLdpNgAddrFecIpPrefixLen_Type()
)
vRtrLdpNgAddrFecIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecIpPrefixLen.setStatus("current")
_VRtrLdpNgAddrFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpNgAddrFecFlags_Object = MibTableColumn
vRtrLdpNgAddrFecFlags = _VRtrLdpNgAddrFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12, 1, 5),
    _VRtrLdpNgAddrFecFlags_Type()
)
vRtrLdpNgAddrFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecFlags.setStatus("current")
_VRtrLdpNgAddrFecNumInLabels_Type = Unsigned32
_VRtrLdpNgAddrFecNumInLabels_Object = MibTableColumn
vRtrLdpNgAddrFecNumInLabels = _VRtrLdpNgAddrFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12, 1, 6),
    _VRtrLdpNgAddrFecNumInLabels_Type()
)
vRtrLdpNgAddrFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecNumInLabels.setStatus("current")
_VRtrLdpNgAddrFecNumOutLabels_Type = Unsigned32
_VRtrLdpNgAddrFecNumOutLabels_Object = MibTableColumn
vRtrLdpNgAddrFecNumOutLabels = _VRtrLdpNgAddrFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 12, 1, 7),
    _VRtrLdpNgAddrFecNumOutLabels_Type()
)
vRtrLdpNgAddrFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecNumOutLabels.setStatus("current")
_VRtrLdpNgAddrFecInLblTable_Object = MibTable
vRtrLdpNgAddrFecInLblTable = _VRtrLdpNgAddrFecInLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 13)
)
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecInLblTable.setStatus("current")
_VRtrLdpNgAddrFecInLblEntry_Object = MibTableRow
vRtrLdpNgAddrFecInLblEntry = _VRtrLdpNgAddrFecInLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 13, 1)
)
vRtrLdpNgAddrFecInLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecFecType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefixType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefix"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefixLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecInLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecInLblEntry.setStatus("current")
_VRtrLdpNgAddrFecInLblId_Type = Unsigned32
_VRtrLdpNgAddrFecInLblId_Object = MibTableColumn
vRtrLdpNgAddrFecInLblId = _VRtrLdpNgAddrFecInLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 13, 1, 1),
    _VRtrLdpNgAddrFecInLblId_Type()
)
vRtrLdpNgAddrFecInLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecInLblId.setStatus("current")
_VRtrLdpNgAddrFecInLbl_Type = Unsigned32
_VRtrLdpNgAddrFecInLbl_Object = MibTableColumn
vRtrLdpNgAddrFecInLbl = _VRtrLdpNgAddrFecInLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 13, 1, 2),
    _VRtrLdpNgAddrFecInLbl_Type()
)
vRtrLdpNgAddrFecInLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecInLbl.setStatus("current")
_VRtrLdpNgAddrFecInLblStatus_Type = TmnxLabelStatus
_VRtrLdpNgAddrFecInLblStatus_Object = MibTableColumn
vRtrLdpNgAddrFecInLblStatus = _VRtrLdpNgAddrFecInLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 13, 1, 3),
    _VRtrLdpNgAddrFecInLblStatus_Type()
)
vRtrLdpNgAddrFecInLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecInLblStatus.setStatus("current")
_VRtrLdpNgAddrFecInLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpNgAddrFecInLblIfIndex_Object = MibTableColumn
vRtrLdpNgAddrFecInLblIfIndex = _VRtrLdpNgAddrFecInLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 13, 1, 4),
    _VRtrLdpNgAddrFecInLblIfIndex_Type()
)
vRtrLdpNgAddrFecInLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecInLblIfIndex.setStatus("current")
_VRtrLdpNgAddrFecOutLblTable_Object = MibTable
vRtrLdpNgAddrFecOutLblTable = _VRtrLdpNgAddrFecOutLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14)
)
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblTable.setStatus("current")
_VRtrLdpNgAddrFecOutLblEntry_Object = MibTableRow
vRtrLdpNgAddrFecOutLblEntry = _VRtrLdpNgAddrFecOutLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1)
)
vRtrLdpNgAddrFecOutLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecFecType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefixType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefix"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefixLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblEntry.setStatus("current")
_VRtrLdpNgAddrFecOutLblId_Type = Unsigned32
_VRtrLdpNgAddrFecOutLblId_Object = MibTableColumn
vRtrLdpNgAddrFecOutLblId = _VRtrLdpNgAddrFecOutLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 1),
    _VRtrLdpNgAddrFecOutLblId_Type()
)
vRtrLdpNgAddrFecOutLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblId.setStatus("current")
_VRtrLdpNgAddrFecOutLbl_Type = Unsigned32
_VRtrLdpNgAddrFecOutLbl_Object = MibTableColumn
vRtrLdpNgAddrFecOutLbl = _VRtrLdpNgAddrFecOutLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 2),
    _VRtrLdpNgAddrFecOutLbl_Type()
)
vRtrLdpNgAddrFecOutLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLbl.setStatus("current")
_VRtrLdpNgAddrFecOutLblStatus_Type = TmnxLabelStatus
_VRtrLdpNgAddrFecOutLblStatus_Object = MibTableColumn
vRtrLdpNgAddrFecOutLblStatus = _VRtrLdpNgAddrFecOutLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 3),
    _VRtrLdpNgAddrFecOutLblStatus_Type()
)
vRtrLdpNgAddrFecOutLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblStatus.setStatus("current")
_VRtrLdpNgAddrFecOutLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpNgAddrFecOutLblIfIndex_Object = MibTableColumn
vRtrLdpNgAddrFecOutLblIfIndex = _VRtrLdpNgAddrFecOutLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 4),
    _VRtrLdpNgAddrFecOutLblIfIndex_Type()
)
vRtrLdpNgAddrFecOutLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblIfIndex.setStatus("current")
_VRtrLdpNgAddrFecOutLblNHType_Type = InetAddressType
_VRtrLdpNgAddrFecOutLblNHType_Object = MibTableColumn
vRtrLdpNgAddrFecOutLblNHType = _VRtrLdpNgAddrFecOutLblNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 5),
    _VRtrLdpNgAddrFecOutLblNHType_Type()
)
vRtrLdpNgAddrFecOutLblNHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblNHType.setStatus("current")


class _VRtrLdpNgAddrFecOutLblNHAddr_Type(InetAddress):
    """Custom type vRtrLdpNgAddrFecOutLblNHAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgAddrFecOutLblNHAddr_Type.__name__ = "InetAddress"
_VRtrLdpNgAddrFecOutLblNHAddr_Object = MibTableColumn
vRtrLdpNgAddrFecOutLblNHAddr = _VRtrLdpNgAddrFecOutLblNHAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 6),
    _VRtrLdpNgAddrFecOutLblNHAddr_Type()
)
vRtrLdpNgAddrFecOutLblNHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblNHAddr.setStatus("current")
_VRtrLdpNgAddrFecOutLblMetric_Type = Unsigned32
_VRtrLdpNgAddrFecOutLblMetric_Object = MibTableColumn
vRtrLdpNgAddrFecOutLblMetric = _VRtrLdpNgAddrFecOutLblMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 7),
    _VRtrLdpNgAddrFecOutLblMetric_Type()
)
vRtrLdpNgAddrFecOutLblMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblMetric.setStatus("current")
_VRtrLdpNgAddrFecOutLblMtu_Type = Unsigned32
_VRtrLdpNgAddrFecOutLblMtu_Object = MibTableColumn
vRtrLdpNgAddrFecOutLblMtu = _VRtrLdpNgAddrFecOutLblMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 8),
    _VRtrLdpNgAddrFecOutLblMtu_Type()
)
vRtrLdpNgAddrFecOutLblMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblMtu.setStatus("current")
_VRtrLdpNgAddrFecOutLblLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpNgAddrFecOutLblLspId_Object = MibTableColumn
vRtrLdpNgAddrFecOutLblLspId = _VRtrLdpNgAddrFecOutLblLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 14, 1, 9),
    _VRtrLdpNgAddrFecOutLblLspId_Type()
)
vRtrLdpNgAddrFecOutLblLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecOutLblLspId.setStatus("current")
_VRtrLdpNgAddrFecMapTable_Object = MibTable
vRtrLdpNgAddrFecMapTable = _VRtrLdpNgAddrFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 15)
)
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecMapTable.setStatus("current")
_VRtrLdpNgAddrFecMapEntry_Object = MibTableRow
vRtrLdpNgAddrFecMapEntry = _VRtrLdpNgAddrFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 15, 1)
)
vRtrLdpNgAddrFecMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecFecType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefixType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefix"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecIpPrefixLen"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecMapEntry.setStatus("current")
_VRtrLdpNgAddrFecMapFlags_Type = TmnxLdpFECFlags
_VRtrLdpNgAddrFecMapFlags_Object = MibTableColumn
vRtrLdpNgAddrFecMapFlags = _VRtrLdpNgAddrFecMapFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 15, 1, 1),
    _VRtrLdpNgAddrFecMapFlags_Type()
)
vRtrLdpNgAddrFecMapFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecMapFlags.setStatus("current")
_VRtrLdpNgAddrFecMapNumInLabels_Type = Unsigned32
_VRtrLdpNgAddrFecMapNumInLabels_Object = MibTableColumn
vRtrLdpNgAddrFecMapNumInLabels = _VRtrLdpNgAddrFecMapNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 15, 1, 2),
    _VRtrLdpNgAddrFecMapNumInLabels_Type()
)
vRtrLdpNgAddrFecMapNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecMapNumInLabels.setStatus("current")
_VRtrLdpNgAddrFecMapNumOutLabels_Type = Unsigned32
_VRtrLdpNgAddrFecMapNumOutLabels_Object = MibTableColumn
vRtrLdpNgAddrFecMapNumOutLabels = _VRtrLdpNgAddrFecMapNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 15, 1, 3),
    _VRtrLdpNgAddrFecMapNumOutLabels_Type()
)
vRtrLdpNgAddrFecMapNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAddrFecMapNumOutLabels.setStatus("current")
_VRtrLdpNgExtP2MPFecTable_Object = MibTable
vRtrLdpNgExtP2MPFecTable = _VRtrLdpNgExtP2MPFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16)
)
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecTable.setStatus("current")
_VRtrLdpNgExtP2MPFecEntry_Object = MibTableRow
vRtrLdpNgExtP2MPFecEntry = _VRtrLdpNgExtP2MPFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1)
)
vRtrLdpNgExtP2MPFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueLength"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueValue"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecEntry.setStatus("current")


class _VRtrLdpNgExtP2MPFecOpaqueType_Type(Unsigned32):
    """Custom type vRtrLdpNgExtP2MPFecOpaqueType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpNgExtP2MPFecOpaqueType_Type.__name__ = "Unsigned32"
_VRtrLdpNgExtP2MPFecOpaqueType_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOpaqueType = _VRtrLdpNgExtP2MPFecOpaqueType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 1),
    _VRtrLdpNgExtP2MPFecOpaqueType_Type()
)
vRtrLdpNgExtP2MPFecOpaqueType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOpaqueType.setStatus("current")


class _VRtrLdpNgExtP2MPFecOpaqueLength_Type(Unsigned32):
    """Custom type vRtrLdpNgExtP2MPFecOpaqueLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrLdpNgExtP2MPFecOpaqueLength_Type.__name__ = "Unsigned32"
_VRtrLdpNgExtP2MPFecOpaqueLength_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOpaqueLength = _VRtrLdpNgExtP2MPFecOpaqueLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 2),
    _VRtrLdpNgExtP2MPFecOpaqueLength_Type()
)
vRtrLdpNgExtP2MPFecOpaqueLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOpaqueLength.setStatus("current")


class _VRtrLdpNgExtP2MPFecOpaqueValue_Type(OctetString):
    """Custom type vRtrLdpNgExtP2MPFecOpaqueValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrLdpNgExtP2MPFecOpaqueValue_Type.__name__ = "OctetString"
_VRtrLdpNgExtP2MPFecOpaqueValue_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOpaqueValue = _VRtrLdpNgExtP2MPFecOpaqueValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 3),
    _VRtrLdpNgExtP2MPFecOpaqueValue_Type()
)
vRtrLdpNgExtP2MPFecOpaqueValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOpaqueValue.setStatus("current")
_VRtrLdpNgExtP2MPFecRootAddrType_Type = InetAddressType
_VRtrLdpNgExtP2MPFecRootAddrType_Object = MibTableColumn
vRtrLdpNgExtP2MPFecRootAddrType = _VRtrLdpNgExtP2MPFecRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 4),
    _VRtrLdpNgExtP2MPFecRootAddrType_Type()
)
vRtrLdpNgExtP2MPFecRootAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecRootAddrType.setStatus("current")


class _VRtrLdpNgExtP2MPFecRootAddress_Type(InetAddress):
    """Custom type vRtrLdpNgExtP2MPFecRootAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgExtP2MPFecRootAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgExtP2MPFecRootAddress_Object = MibTableColumn
vRtrLdpNgExtP2MPFecRootAddress = _VRtrLdpNgExtP2MPFecRootAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 5),
    _VRtrLdpNgExtP2MPFecRootAddress_Type()
)
vRtrLdpNgExtP2MPFecRootAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecRootAddress.setStatus("current")
_VRtrLdpNgExtP2MPFecFlags_Type = TmnxLdpFECFlags
_VRtrLdpNgExtP2MPFecFlags_Object = MibTableColumn
vRtrLdpNgExtP2MPFecFlags = _VRtrLdpNgExtP2MPFecFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 6),
    _VRtrLdpNgExtP2MPFecFlags_Type()
)
vRtrLdpNgExtP2MPFecFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecFlags.setStatus("current")
_VRtrLdpNgExtP2MPFecNumInLabels_Type = Gauge32
_VRtrLdpNgExtP2MPFecNumInLabels_Object = MibTableColumn
vRtrLdpNgExtP2MPFecNumInLabels = _VRtrLdpNgExtP2MPFecNumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 7),
    _VRtrLdpNgExtP2MPFecNumInLabels_Type()
)
vRtrLdpNgExtP2MPFecNumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecNumInLabels.setStatus("current")
_VRtrLdpNgExtP2MPFecNumOutLabels_Type = Gauge32
_VRtrLdpNgExtP2MPFecNumOutLabels_Object = MibTableColumn
vRtrLdpNgExtP2MPFecNumOutLabels = _VRtrLdpNgExtP2MPFecNumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 8),
    _VRtrLdpNgExtP2MPFecNumOutLabels_Type()
)
vRtrLdpNgExtP2MPFecNumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecNumOutLabels.setStatus("current")
_VRtrLdpNgExtP2MPFecTunnelIfId_Type = Unsigned32
_VRtrLdpNgExtP2MPFecTunnelIfId_Object = MibTableColumn
vRtrLdpNgExtP2MPFecTunnelIfId = _VRtrLdpNgExtP2MPFecTunnelIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 9),
    _VRtrLdpNgExtP2MPFecTunnelIfId_Type()
)
vRtrLdpNgExtP2MPFecTunnelIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecTunnelIfId.setStatus("current")
_VRtrLdpNgExtP2MPFecMetric_Type = Unsigned32
_VRtrLdpNgExtP2MPFecMetric_Object = MibTableColumn
vRtrLdpNgExtP2MPFecMetric = _VRtrLdpNgExtP2MPFecMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 10),
    _VRtrLdpNgExtP2MPFecMetric_Type()
)
vRtrLdpNgExtP2MPFecMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMetric.setStatus("current")
_VRtrLdpNgExtP2MPFecMTU_Type = Unsigned32
_VRtrLdpNgExtP2MPFecMTU_Object = MibTableColumn
vRtrLdpNgExtP2MPFecMTU = _VRtrLdpNgExtP2MPFecMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 16, 1, 11),
    _VRtrLdpNgExtP2MPFecMTU_Type()
)
vRtrLdpNgExtP2MPFecMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMTU.setStatus("current")
_VRtrLdpNgExtP2MPFecInLblTable_Object = MibTable
vRtrLdpNgExtP2MPFecInLblTable = _VRtrLdpNgExtP2MPFecInLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 17)
)
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecInLblTable.setStatus("current")
_VRtrLdpNgExtP2MPFecInLblEntry_Object = MibTableRow
vRtrLdpNgExtP2MPFecInLblEntry = _VRtrLdpNgExtP2MPFecInLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 17, 1)
)
vRtrLdpNgExtP2MPFecInLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueLength"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueValue"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecInLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecInLblEntry.setStatus("current")
_VRtrLdpNgExtP2MPFecInLblId_Type = Unsigned32
_VRtrLdpNgExtP2MPFecInLblId_Object = MibTableColumn
vRtrLdpNgExtP2MPFecInLblId = _VRtrLdpNgExtP2MPFecInLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 17, 1, 1),
    _VRtrLdpNgExtP2MPFecInLblId_Type()
)
vRtrLdpNgExtP2MPFecInLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecInLblId.setStatus("current")
_VRtrLdpNgExtP2MPFecInLbl_Type = Unsigned32
_VRtrLdpNgExtP2MPFecInLbl_Object = MibTableColumn
vRtrLdpNgExtP2MPFecInLbl = _VRtrLdpNgExtP2MPFecInLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 17, 1, 2),
    _VRtrLdpNgExtP2MPFecInLbl_Type()
)
vRtrLdpNgExtP2MPFecInLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecInLbl.setStatus("current")
_VRtrLdpNgExtP2MPFecInLblStatus_Type = TmnxLabelStatus
_VRtrLdpNgExtP2MPFecInLblStatus_Object = MibTableColumn
vRtrLdpNgExtP2MPFecInLblStatus = _VRtrLdpNgExtP2MPFecInLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 17, 1, 3),
    _VRtrLdpNgExtP2MPFecInLblStatus_Type()
)
vRtrLdpNgExtP2MPFecInLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecInLblStatus.setStatus("current")
_VRtrLdpNgExtP2MPFecOutLblTable_Object = MibTable
vRtrLdpNgExtP2MPFecOutLblTable = _VRtrLdpNgExtP2MPFecOutLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18)
)
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLblTable.setStatus("current")
_VRtrLdpNgExtP2MPFecOutLblEntry_Object = MibTableRow
vRtrLdpNgExtP2MPFecOutLblEntry = _VRtrLdpNgExtP2MPFecOutLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18, 1)
)
vRtrLdpNgExtP2MPFecOutLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueLength"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueValue"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOutLblId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLblEntry.setStatus("current")
_VRtrLdpNgExtP2MPFecOutLblId_Type = Unsigned32
_VRtrLdpNgExtP2MPFecOutLblId_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOutLblId = _VRtrLdpNgExtP2MPFecOutLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18, 1, 1),
    _VRtrLdpNgExtP2MPFecOutLblId_Type()
)
vRtrLdpNgExtP2MPFecOutLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLblId.setStatus("current")
_VRtrLdpNgExtP2MPFecOutLbl_Type = Unsigned32
_VRtrLdpNgExtP2MPFecOutLbl_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOutLbl = _VRtrLdpNgExtP2MPFecOutLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18, 1, 2),
    _VRtrLdpNgExtP2MPFecOutLbl_Type()
)
vRtrLdpNgExtP2MPFecOutLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLbl.setStatus("current")
_VRtrLdpNgExtP2MPFecOutLblStatus_Type = TmnxLabelStatus
_VRtrLdpNgExtP2MPFecOutLblStatus_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOutLblStatus = _VRtrLdpNgExtP2MPFecOutLblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18, 1, 3),
    _VRtrLdpNgExtP2MPFecOutLblStatus_Type()
)
vRtrLdpNgExtP2MPFecOutLblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLblStatus.setStatus("current")
_VRtrLdpNgExtP2MPFecOutLblNHType_Type = InetAddressType
_VRtrLdpNgExtP2MPFecOutLblNHType_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOutLblNHType = _VRtrLdpNgExtP2MPFecOutLblNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18, 1, 4),
    _VRtrLdpNgExtP2MPFecOutLblNHType_Type()
)
vRtrLdpNgExtP2MPFecOutLblNHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLblNHType.setStatus("current")


class _VRtrLdpNgExtP2MPFecOutLblNHAdr_Type(InetAddress):
    """Custom type vRtrLdpNgExtP2MPFecOutLblNHAdr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgExtP2MPFecOutLblNHAdr_Type.__name__ = "InetAddress"
_VRtrLdpNgExtP2MPFecOutLblNHAdr_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOutLblNHAdr = _VRtrLdpNgExtP2MPFecOutLblNHAdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18, 1, 5),
    _VRtrLdpNgExtP2MPFecOutLblNHAdr_Type()
)
vRtrLdpNgExtP2MPFecOutLblNHAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLblNHAdr.setStatus("current")
_VRtrLdpNgExtP2MPFecOutLblIfIndex_Type = InterfaceIndexOrZero
_VRtrLdpNgExtP2MPFecOutLblIfIndex_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOutLblIfIndex = _VRtrLdpNgExtP2MPFecOutLblIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18, 1, 6),
    _VRtrLdpNgExtP2MPFecOutLblIfIndex_Type()
)
vRtrLdpNgExtP2MPFecOutLblIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLblIfIndex.setStatus("current")
_VRtrLdpNgExtP2MPFecOutLblLspId_Type = TmnxVRtrMplsLspID
_VRtrLdpNgExtP2MPFecOutLblLspId_Object = MibTableColumn
vRtrLdpNgExtP2MPFecOutLblLspId = _VRtrLdpNgExtP2MPFecOutLblLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 18, 1, 7),
    _VRtrLdpNgExtP2MPFecOutLblLspId_Type()
)
vRtrLdpNgExtP2MPFecOutLblLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecOutLblLspId.setStatus("current")
_VRtrLdpNgExtP2MPFecMapTable_Object = MibTable
vRtrLdpNgExtP2MPFecMapTable = _VRtrLdpNgExtP2MPFecMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 19)
)
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMapTable.setStatus("current")
_VRtrLdpNgExtP2MPFecMapEntry_Object = MibTableRow
vRtrLdpNgExtP2MPFecMapEntry = _VRtrLdpNgExtP2MPFecMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 19, 1)
)
vRtrLdpNgExtP2MPFecMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecRootAddrType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecRootAddress"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueLength"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOpaqueValue"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMapEntry.setStatus("current")
_VRtrLdpNgExtP2MPFecMapFlags_Type = TmnxLdpFECFlags
_VRtrLdpNgExtP2MPFecMapFlags_Object = MibTableColumn
vRtrLdpNgExtP2MPFecMapFlags = _VRtrLdpNgExtP2MPFecMapFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 19, 1, 1),
    _VRtrLdpNgExtP2MPFecMapFlags_Type()
)
vRtrLdpNgExtP2MPFecMapFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMapFlags.setStatus("current")
_VRtrLdpNgExtP2MPFecMapNumInLbls_Type = Gauge32
_VRtrLdpNgExtP2MPFecMapNumInLbls_Object = MibTableColumn
vRtrLdpNgExtP2MPFecMapNumInLbls = _VRtrLdpNgExtP2MPFecMapNumInLbls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 19, 1, 2),
    _VRtrLdpNgExtP2MPFecMapNumInLbls_Type()
)
vRtrLdpNgExtP2MPFecMapNumInLbls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMapNumInLbls.setStatus("current")
_VRtrLdpNgExtP2MPFecMapNumOutLbls_Type = Gauge32
_VRtrLdpNgExtP2MPFecMapNumOutLbls_Object = MibTableColumn
vRtrLdpNgExtP2MPFecMapNumOutLbls = _VRtrLdpNgExtP2MPFecMapNumOutLbls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 19, 1, 3),
    _VRtrLdpNgExtP2MPFecMapNumOutLbls_Type()
)
vRtrLdpNgExtP2MPFecMapNumOutLbls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMapNumOutLbls.setStatus("current")
_VRtrLdpNgExtP2MPFecMapTunnelIfId_Type = Unsigned32
_VRtrLdpNgExtP2MPFecMapTunnelIfId_Object = MibTableColumn
vRtrLdpNgExtP2MPFecMapTunnelIfId = _VRtrLdpNgExtP2MPFecMapTunnelIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 19, 1, 4),
    _VRtrLdpNgExtP2MPFecMapTunnelIfId_Type()
)
vRtrLdpNgExtP2MPFecMapTunnelIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMapTunnelIfId.setStatus("current")
_VRtrLdpNgExtP2MPFecMapMetric_Type = Unsigned32
_VRtrLdpNgExtP2MPFecMapMetric_Object = MibTableColumn
vRtrLdpNgExtP2MPFecMapMetric = _VRtrLdpNgExtP2MPFecMapMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 19, 1, 5),
    _VRtrLdpNgExtP2MPFecMapMetric_Type()
)
vRtrLdpNgExtP2MPFecMapMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMapMetric.setStatus("current")
_VRtrLdpNgExtP2MPFecMapMTU_Type = Unsigned32
_VRtrLdpNgExtP2MPFecMapMTU_Object = MibTableColumn
vRtrLdpNgExtP2MPFecMapMTU = _VRtrLdpNgExtP2MPFecMapMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 19, 1, 6),
    _VRtrLdpNgExtP2MPFecMapMTU_Type()
)
vRtrLdpNgExtP2MPFecMapMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgExtP2MPFecMapMTU.setStatus("current")
_VRtrLdpNgInetIfStatsTable_Object = MibTable
vRtrLdpNgInetIfStatsTable = _VRtrLdpNgInetIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 20)
)
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfStatsTable.setStatus("current")
_VRtrLdpNgInetIfStatsEntry_Object = MibTableRow
vRtrLdpNgInetIfStatsEntry = _VRtrLdpNgInetIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 20, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfStatsEntry.setStatus("current")
_VRtrLdpNgInetIfStatsExistingAdj_Type = Gauge32
_VRtrLdpNgInetIfStatsExistingAdj_Object = MibTableColumn
vRtrLdpNgInetIfStatsExistingAdj = _VRtrLdpNgInetIfStatsExistingAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 20, 1, 1),
    _VRtrLdpNgInetIfStatsExistingAdj_Type()
)
vRtrLdpNgInetIfStatsExistingAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfStatsExistingAdj.setStatus("current")
_VRtrLdpNgSessionStatsTable_Object = MibTable
vRtrLdpNgSessionStatsTable = _VRtrLdpNgSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21)
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionStatsTable.setStatus("current")
_VRtrLdpNgSessionStatsEntry_Object = MibTableRow
vRtrLdpNgSessionStatsEntry = _VRtrLdpNgSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessionStatsEntry.setStatus("current")
_VRtrLdpNgSessStatsTargAdj_Type = Gauge32
_VRtrLdpNgSessStatsTargAdj_Object = MibTableColumn
vRtrLdpNgSessStatsTargAdj = _VRtrLdpNgSessStatsTargAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 1),
    _VRtrLdpNgSessStatsTargAdj_Type()
)
vRtrLdpNgSessStatsTargAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsTargAdj.setStatus("current")
_VRtrLdpNgSessStatsLinkAdj_Type = Gauge32
_VRtrLdpNgSessStatsLinkAdj_Object = MibTableColumn
vRtrLdpNgSessStatsLinkAdj = _VRtrLdpNgSessStatsLinkAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 2),
    _VRtrLdpNgSessStatsLinkAdj_Type()
)
vRtrLdpNgSessStatsLinkAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLinkAdj.setStatus("current")
_VRtrLdpNgSessStatsHelloIn_Type = Counter32
_VRtrLdpNgSessStatsHelloIn_Object = MibTableColumn
vRtrLdpNgSessStatsHelloIn = _VRtrLdpNgSessStatsHelloIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 3),
    _VRtrLdpNgSessStatsHelloIn_Type()
)
vRtrLdpNgSessStatsHelloIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsHelloIn.setStatus("current")
_VRtrLdpNgSessStatsHelloOut_Type = Counter32
_VRtrLdpNgSessStatsHelloOut_Object = MibTableColumn
vRtrLdpNgSessStatsHelloOut = _VRtrLdpNgSessStatsHelloOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 4),
    _VRtrLdpNgSessStatsHelloOut_Type()
)
vRtrLdpNgSessStatsHelloOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsHelloOut.setStatus("current")
_VRtrLdpNgSessStatsKeepaliveIn_Type = Counter32
_VRtrLdpNgSessStatsKeepaliveIn_Object = MibTableColumn
vRtrLdpNgSessStatsKeepaliveIn = _VRtrLdpNgSessStatsKeepaliveIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 5),
    _VRtrLdpNgSessStatsKeepaliveIn_Type()
)
vRtrLdpNgSessStatsKeepaliveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsKeepaliveIn.setStatus("current")
_VRtrLdpNgSessStatsKeepaliveOut_Type = Counter32
_VRtrLdpNgSessStatsKeepaliveOut_Object = MibTableColumn
vRtrLdpNgSessStatsKeepaliveOut = _VRtrLdpNgSessStatsKeepaliveOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 6),
    _VRtrLdpNgSessStatsKeepaliveOut_Type()
)
vRtrLdpNgSessStatsKeepaliveOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsKeepaliveOut.setStatus("current")
_VRtrLdpNgSessStatsInitIn_Type = Counter32
_VRtrLdpNgSessStatsInitIn_Object = MibTableColumn
vRtrLdpNgSessStatsInitIn = _VRtrLdpNgSessStatsInitIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 7),
    _VRtrLdpNgSessStatsInitIn_Type()
)
vRtrLdpNgSessStatsInitIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsInitIn.setStatus("current")
_VRtrLdpNgSessStatsInitOut_Type = Counter32
_VRtrLdpNgSessStatsInitOut_Object = MibTableColumn
vRtrLdpNgSessStatsInitOut = _VRtrLdpNgSessStatsInitOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 8),
    _VRtrLdpNgSessStatsInitOut_Type()
)
vRtrLdpNgSessStatsInitOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsInitOut.setStatus("current")
_VRtrLdpNgSessStatsLblMappingIn_Type = Counter32
_VRtrLdpNgSessStatsLblMappingIn_Object = MibTableColumn
vRtrLdpNgSessStatsLblMappingIn = _VRtrLdpNgSessStatsLblMappingIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 9),
    _VRtrLdpNgSessStatsLblMappingIn_Type()
)
vRtrLdpNgSessStatsLblMappingIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblMappingIn.setStatus("current")
_VRtrLdpNgSessStatsLblMappingOut_Type = Counter32
_VRtrLdpNgSessStatsLblMappingOut_Object = MibTableColumn
vRtrLdpNgSessStatsLblMappingOut = _VRtrLdpNgSessStatsLblMappingOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 10),
    _VRtrLdpNgSessStatsLblMappingOut_Type()
)
vRtrLdpNgSessStatsLblMappingOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblMappingOut.setStatus("current")
_VRtrLdpNgSessStatsLblRequestIn_Type = Counter32
_VRtrLdpNgSessStatsLblRequestIn_Object = MibTableColumn
vRtrLdpNgSessStatsLblRequestIn = _VRtrLdpNgSessStatsLblRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 11),
    _VRtrLdpNgSessStatsLblRequestIn_Type()
)
vRtrLdpNgSessStatsLblRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblRequestIn.setStatus("current")
_VRtrLdpNgSessStatsLblRequestOut_Type = Counter32
_VRtrLdpNgSessStatsLblRequestOut_Object = MibTableColumn
vRtrLdpNgSessStatsLblRequestOut = _VRtrLdpNgSessStatsLblRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 12),
    _VRtrLdpNgSessStatsLblRequestOut_Type()
)
vRtrLdpNgSessStatsLblRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblRequestOut.setStatus("current")
_VRtrLdpNgSessStatsLblReleaseIn_Type = Counter32
_VRtrLdpNgSessStatsLblReleaseIn_Object = MibTableColumn
vRtrLdpNgSessStatsLblReleaseIn = _VRtrLdpNgSessStatsLblReleaseIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 13),
    _VRtrLdpNgSessStatsLblReleaseIn_Type()
)
vRtrLdpNgSessStatsLblReleaseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblReleaseIn.setStatus("current")
_VRtrLdpNgSessStatsLblReleaseOut_Type = Counter32
_VRtrLdpNgSessStatsLblReleaseOut_Object = MibTableColumn
vRtrLdpNgSessStatsLblReleaseOut = _VRtrLdpNgSessStatsLblReleaseOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 14),
    _VRtrLdpNgSessStatsLblReleaseOut_Type()
)
vRtrLdpNgSessStatsLblReleaseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblReleaseOut.setStatus("current")
_VRtrLdpNgSessStatsLblWithdrawIn_Type = Counter32
_VRtrLdpNgSessStatsLblWithdrawIn_Object = MibTableColumn
vRtrLdpNgSessStatsLblWithdrawIn = _VRtrLdpNgSessStatsLblWithdrawIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 15),
    _VRtrLdpNgSessStatsLblWithdrawIn_Type()
)
vRtrLdpNgSessStatsLblWithdrawIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblWithdrawIn.setStatus("current")
_VRtrLdpNgSessStatsLblWithdrawOut_Type = Counter32
_VRtrLdpNgSessStatsLblWithdrawOut_Object = MibTableColumn
vRtrLdpNgSessStatsLblWithdrawOut = _VRtrLdpNgSessStatsLblWithdrawOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 16),
    _VRtrLdpNgSessStatsLblWithdrawOut_Type()
)
vRtrLdpNgSessStatsLblWithdrawOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblWithdrawOut.setStatus("current")
_VRtrLdpNgSessStatsLblAbortIn_Type = Counter32
_VRtrLdpNgSessStatsLblAbortIn_Object = MibTableColumn
vRtrLdpNgSessStatsLblAbortIn = _VRtrLdpNgSessStatsLblAbortIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 17),
    _VRtrLdpNgSessStatsLblAbortIn_Type()
)
vRtrLdpNgSessStatsLblAbortIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblAbortIn.setStatus("current")
_VRtrLdpNgSessStatsLblAbortOut_Type = Counter32
_VRtrLdpNgSessStatsLblAbortOut_Object = MibTableColumn
vRtrLdpNgSessStatsLblAbortOut = _VRtrLdpNgSessStatsLblAbortOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 18),
    _VRtrLdpNgSessStatsLblAbortOut_Type()
)
vRtrLdpNgSessStatsLblAbortOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsLblAbortOut.setStatus("current")
_VRtrLdpNgSessStatsAddrIn_Type = Counter32
_VRtrLdpNgSessStatsAddrIn_Object = MibTableColumn
vRtrLdpNgSessStatsAddrIn = _VRtrLdpNgSessStatsAddrIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 19),
    _VRtrLdpNgSessStatsAddrIn_Type()
)
vRtrLdpNgSessStatsAddrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsAddrIn.setStatus("current")
_VRtrLdpNgSessStatsAddrOut_Type = Counter32
_VRtrLdpNgSessStatsAddrOut_Object = MibTableColumn
vRtrLdpNgSessStatsAddrOut = _VRtrLdpNgSessStatsAddrOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 20),
    _VRtrLdpNgSessStatsAddrOut_Type()
)
vRtrLdpNgSessStatsAddrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsAddrOut.setStatus("current")
_VRtrLdpNgSessStatsAddrWithdrIn_Type = Counter32
_VRtrLdpNgSessStatsAddrWithdrIn_Object = MibTableColumn
vRtrLdpNgSessStatsAddrWithdrIn = _VRtrLdpNgSessStatsAddrWithdrIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 21),
    _VRtrLdpNgSessStatsAddrWithdrIn_Type()
)
vRtrLdpNgSessStatsAddrWithdrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsAddrWithdrIn.setStatus("current")
_VRtrLdpNgSessStatsAddrWithdrOut_Type = Counter32
_VRtrLdpNgSessStatsAddrWithdrOut_Object = MibTableColumn
vRtrLdpNgSessStatsAddrWithdrOut = _VRtrLdpNgSessStatsAddrWithdrOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 22),
    _VRtrLdpNgSessStatsAddrWithdrOut_Type()
)
vRtrLdpNgSessStatsAddrWithdrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsAddrWithdrOut.setStatus("current")
_VRtrLdpNgSessStatsNotifIn_Type = Counter32
_VRtrLdpNgSessStatsNotifIn_Object = MibTableColumn
vRtrLdpNgSessStatsNotifIn = _VRtrLdpNgSessStatsNotifIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 23),
    _VRtrLdpNgSessStatsNotifIn_Type()
)
vRtrLdpNgSessStatsNotifIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsNotifIn.setStatus("current")
_VRtrLdpNgSessStatsNotifOut_Type = Counter32
_VRtrLdpNgSessStatsNotifOut_Object = MibTableColumn
vRtrLdpNgSessStatsNotifOut = _VRtrLdpNgSessStatsNotifOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 24),
    _VRtrLdpNgSessStatsNotifOut_Type()
)
vRtrLdpNgSessStatsNotifOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsNotifOut.setStatus("current")
_VRtrLdpNgSessStatsIPv4PfxFecRcv_Type = Counter32
_VRtrLdpNgSessStatsIPv4PfxFecRcv_Object = MibTableColumn
vRtrLdpNgSessStatsIPv4PfxFecRcv = _VRtrLdpNgSessStatsIPv4PfxFecRcv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 25),
    _VRtrLdpNgSessStatsIPv4PfxFecRcv_Type()
)
vRtrLdpNgSessStatsIPv4PfxFecRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv4PfxFecRcv.setStatus("current")
_VRtrLdpNgSessStatsIPv6PfxFecRcv_Type = Counter32
_VRtrLdpNgSessStatsIPv6PfxFecRcv_Object = MibTableColumn
vRtrLdpNgSessStatsIPv6PfxFecRcv = _VRtrLdpNgSessStatsIPv6PfxFecRcv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 26),
    _VRtrLdpNgSessStatsIPv6PfxFecRcv_Type()
)
vRtrLdpNgSessStatsIPv6PfxFecRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv6PfxFecRcv.setStatus("current")
_VRtrLdpNgSessStatsIPv4PfxFecSnt_Type = Counter32
_VRtrLdpNgSessStatsIPv4PfxFecSnt_Object = MibTableColumn
vRtrLdpNgSessStatsIPv4PfxFecSnt = _VRtrLdpNgSessStatsIPv4PfxFecSnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 27),
    _VRtrLdpNgSessStatsIPv4PfxFecSnt_Type()
)
vRtrLdpNgSessStatsIPv4PfxFecSnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv4PfxFecSnt.setStatus("current")
_VRtrLdpNgSessStatsIPv6PfxFecSnt_Type = Counter32
_VRtrLdpNgSessStatsIPv6PfxFecSnt_Object = MibTableColumn
vRtrLdpNgSessStatsIPv6PfxFecSnt = _VRtrLdpNgSessStatsIPv6PfxFecSnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 28),
    _VRtrLdpNgSessStatsIPv6PfxFecSnt_Type()
)
vRtrLdpNgSessStatsIPv6PfxFecSnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv6PfxFecSnt.setStatus("current")
_VRtrLdpNgSessStatsIPv4P2MPFecRcv_Type = Counter32
_VRtrLdpNgSessStatsIPv4P2MPFecRcv_Object = MibTableColumn
vRtrLdpNgSessStatsIPv4P2MPFecRcv = _VRtrLdpNgSessStatsIPv4P2MPFecRcv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 29),
    _VRtrLdpNgSessStatsIPv4P2MPFecRcv_Type()
)
vRtrLdpNgSessStatsIPv4P2MPFecRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv4P2MPFecRcv.setStatus("current")
_VRtrLdpNgSessStatsIPv6P2MPFecRcv_Type = Counter32
_VRtrLdpNgSessStatsIPv6P2MPFecRcv_Object = MibTableColumn
vRtrLdpNgSessStatsIPv6P2MPFecRcv = _VRtrLdpNgSessStatsIPv6P2MPFecRcv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 30),
    _VRtrLdpNgSessStatsIPv6P2MPFecRcv_Type()
)
vRtrLdpNgSessStatsIPv6P2MPFecRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv6P2MPFecRcv.setStatus("current")
_VRtrLdpNgSessStatsIPv4P2MPFecSnt_Type = Counter32
_VRtrLdpNgSessStatsIPv4P2MPFecSnt_Object = MibTableColumn
vRtrLdpNgSessStatsIPv4P2MPFecSnt = _VRtrLdpNgSessStatsIPv4P2MPFecSnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 31),
    _VRtrLdpNgSessStatsIPv4P2MPFecSnt_Type()
)
vRtrLdpNgSessStatsIPv4P2MPFecSnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv4P2MPFecSnt.setStatus("current")
_VRtrLdpNgSessStatsIPv6P2MPFecSnt_Type = Counter32
_VRtrLdpNgSessStatsIPv6P2MPFecSnt_Object = MibTableColumn
vRtrLdpNgSessStatsIPv6P2MPFecSnt = _VRtrLdpNgSessStatsIPv6P2MPFecSnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 32),
    _VRtrLdpNgSessStatsIPv6P2MPFecSnt_Type()
)
vRtrLdpNgSessStatsIPv6P2MPFecSnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv6P2MPFecSnt.setStatus("current")
_VRtrLdpNgSessStatsSvcFec128Recv_Type = Counter32
_VRtrLdpNgSessStatsSvcFec128Recv_Object = MibTableColumn
vRtrLdpNgSessStatsSvcFec128Recv = _VRtrLdpNgSessStatsSvcFec128Recv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 33),
    _VRtrLdpNgSessStatsSvcFec128Recv_Type()
)
vRtrLdpNgSessStatsSvcFec128Recv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsSvcFec128Recv.setStatus("current")
_VRtrLdpNgSessStatsSvcFec128Sent_Type = Counter32
_VRtrLdpNgSessStatsSvcFec128Sent_Object = MibTableColumn
vRtrLdpNgSessStatsSvcFec128Sent = _VRtrLdpNgSessStatsSvcFec128Sent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 34),
    _VRtrLdpNgSessStatsSvcFec128Sent_Type()
)
vRtrLdpNgSessStatsSvcFec128Sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsSvcFec128Sent.setStatus("current")
_VRtrLdpNgSessStatsSvcFec129Recv_Type = Counter32
_VRtrLdpNgSessStatsSvcFec129Recv_Object = MibTableColumn
vRtrLdpNgSessStatsSvcFec129Recv = _VRtrLdpNgSessStatsSvcFec129Recv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 35),
    _VRtrLdpNgSessStatsSvcFec129Recv_Type()
)
vRtrLdpNgSessStatsSvcFec129Recv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsSvcFec129Recv.setStatus("current")
_VRtrLdpNgSessStatsSvcFec129Sent_Type = Counter32
_VRtrLdpNgSessStatsSvcFec129Sent_Object = MibTableColumn
vRtrLdpNgSessStatsSvcFec129Sent = _VRtrLdpNgSessStatsSvcFec129Sent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 36),
    _VRtrLdpNgSessStatsSvcFec129Sent_Type()
)
vRtrLdpNgSessStatsSvcFec129Sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsSvcFec129Sent.setStatus("current")
_VRtrLdpNgSessStatsIPv4AddrRecv_Type = Counter32
_VRtrLdpNgSessStatsIPv4AddrRecv_Object = MibTableColumn
vRtrLdpNgSessStatsIPv4AddrRecv = _VRtrLdpNgSessStatsIPv4AddrRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 37),
    _VRtrLdpNgSessStatsIPv4AddrRecv_Type()
)
vRtrLdpNgSessStatsIPv4AddrRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv4AddrRecv.setStatus("current")
_VRtrLdpNgSessStatsIPv6AddrRecv_Type = Counter32
_VRtrLdpNgSessStatsIPv6AddrRecv_Object = MibTableColumn
vRtrLdpNgSessStatsIPv6AddrRecv = _VRtrLdpNgSessStatsIPv6AddrRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 38),
    _VRtrLdpNgSessStatsIPv6AddrRecv_Type()
)
vRtrLdpNgSessStatsIPv6AddrRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv6AddrRecv.setStatus("current")
_VRtrLdpNgSessStatsIPv4AddrSent_Type = Counter32
_VRtrLdpNgSessStatsIPv4AddrSent_Object = MibTableColumn
vRtrLdpNgSessStatsIPv4AddrSent = _VRtrLdpNgSessStatsIPv4AddrSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 39),
    _VRtrLdpNgSessStatsIPv4AddrSent_Type()
)
vRtrLdpNgSessStatsIPv4AddrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv4AddrSent.setStatus("current")
_VRtrLdpNgSessStatsIPv6AddrSent_Type = Counter32
_VRtrLdpNgSessStatsIPv6AddrSent_Object = MibTableColumn
vRtrLdpNgSessStatsIPv6AddrSent = _VRtrLdpNgSessStatsIPv6AddrSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 40),
    _VRtrLdpNgSessStatsIPv6AddrSent_Type()
)
vRtrLdpNgSessStatsIPv6AddrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsIPv6AddrSent.setStatus("current")
_VRtrLdpNgSessStatsCapabilityIn_Type = Counter32
_VRtrLdpNgSessStatsCapabilityIn_Object = MibTableColumn
vRtrLdpNgSessStatsCapabilityIn = _VRtrLdpNgSessStatsCapabilityIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 41),
    _VRtrLdpNgSessStatsCapabilityIn_Type()
)
vRtrLdpNgSessStatsCapabilityIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsCapabilityIn.setStatus("current")
_VRtrLdpNgSessStatsCapabilityOut_Type = Counter32
_VRtrLdpNgSessStatsCapabilityOut_Object = MibTableColumn
vRtrLdpNgSessStatsCapabilityOut = _VRtrLdpNgSessStatsCapabilityOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 21, 1, 42),
    _VRtrLdpNgSessStatsCapabilityOut_Type()
)
vRtrLdpNgSessStatsCapabilityOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSessStatsCapabilityOut.setStatus("current")
_VLdpNgSvcFec128Table_Object = MibTable
vLdpNgSvcFec128Table = _VLdpNgSvcFec128Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22)
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec128Table.setStatus("current")
_VLdpNgSvcFec128Entry_Object = MibTableRow
vLdpNgSvcFec128Entry = _VLdpNgSvcFec128Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1)
)
vLdpNgSvcFec128Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128FecType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec128Entry.setStatus("current")
_VLdpNgFec128FecType_Type = TmnxLdpFECType
_VLdpNgFec128FecType_Object = MibTableColumn
vLdpNgFec128FecType = _VLdpNgFec128FecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 1),
    _VLdpNgFec128FecType_Type()
)
vLdpNgFec128FecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec128FecType.setStatus("current")
_VLdpNgFec128VcType_Type = TmnxVcType
_VLdpNgFec128VcType_Object = MibTableColumn
vLdpNgFec128VcType = _VLdpNgFec128VcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 2),
    _VLdpNgFec128VcType_Type()
)
vLdpNgFec128VcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec128VcType.setStatus("current")
_VLdpNgFec128VcId_Type = TmnxVcId
_VLdpNgFec128VcId_Object = MibTableColumn
vLdpNgFec128VcId = _VLdpNgFec128VcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 3),
    _VLdpNgFec128VcId_Type()
)
vLdpNgFec128VcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec128VcId.setStatus("current")
_VLdpNgFec128ServType_Type = ServType
_VLdpNgFec128ServType_Object = MibTableColumn
vLdpNgFec128ServType = _VLdpNgFec128ServType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 4),
    _VLdpNgFec128ServType_Type()
)
vLdpNgFec128ServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128ServType.setStatus("current")


class _VLdpNgFec128ServId_Type(TmnxServId):
    """Custom type vLdpNgFec128ServId based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VLdpNgFec128ServId_Type.__name__ = "TmnxServId"
_VLdpNgFec128ServId_Object = MibTableColumn
vLdpNgFec128ServId = _VLdpNgFec128ServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 5),
    _VLdpNgFec128ServId_Type()
)
vLdpNgFec128ServId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128ServId.setStatus("current")
_VLdpNgFec128VpnId_Type = TmnxVpnId
_VLdpNgFec128VpnId_Object = MibTableColumn
vLdpNgFec128VpnId = _VLdpNgFec128VpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 6),
    _VLdpNgFec128VpnId_Type()
)
vLdpNgFec128VpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128VpnId.setStatus("current")
_VLdpNgFec128Flags_Type = TmnxLdpFECFlags
_VLdpNgFec128Flags_Object = MibTableColumn
vLdpNgFec128Flags = _VLdpNgFec128Flags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 7),
    _VLdpNgFec128Flags_Type()
)
vLdpNgFec128Flags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128Flags.setStatus("current")
_VLdpNgFec128NumInLabels_Type = Unsigned32
_VLdpNgFec128NumInLabels_Object = MibTableColumn
vLdpNgFec128NumInLabels = _VLdpNgFec128NumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 8),
    _VLdpNgFec128NumInLabels_Type()
)
vLdpNgFec128NumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128NumInLabels.setStatus("current")
_VLdpNgFec128NumOutLabels_Type = Unsigned32
_VLdpNgFec128NumOutLabels_Object = MibTableColumn
vLdpNgFec128NumOutLabels = _VLdpNgFec128NumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 9),
    _VLdpNgFec128NumOutLabels_Type()
)
vLdpNgFec128NumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128NumOutLabels.setStatus("current")
_VLdpNgFec128SdpId_Type = SdpId
_VLdpNgFec128SdpId_Object = MibTableColumn
vLdpNgFec128SdpId = _VLdpNgFec128SdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 10),
    _VLdpNgFec128SdpId_Type()
)
vLdpNgFec128SdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128SdpId.setStatus("current")
_VLdpNgFec128MateEndptVcId_Type = TmnxVcId
_VLdpNgFec128MateEndptVcId_Object = MibTableColumn
vLdpNgFec128MateEndptVcId = _VLdpNgFec128MateEndptVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 11),
    _VLdpNgFec128MateEndptVcId_Type()
)
vLdpNgFec128MateEndptVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128MateEndptVcId.setStatus("current")
_VLdpNgFec128MateEndptSdpId_Type = SdpId
_VLdpNgFec128MateEndptSdpId_Object = MibTableColumn
vLdpNgFec128MateEndptSdpId = _VLdpNgFec128MateEndptSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 22, 1, 12),
    _VLdpNgFec128MateEndptSdpId_Type()
)
vLdpNgFec128MateEndptSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128MateEndptSdpId.setStatus("current")
_VLdpNgSvcFec128InLblTable_Object = MibTable
vLdpNgSvcFec128InLblTable = _VLdpNgSvcFec128InLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23)
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec128InLblTable.setStatus("current")
_VLdpNgSvcFec128InLblEntry_Object = MibTableRow
vLdpNgSvcFec128InLblEntry = _VLdpNgSvcFec128InLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1)
)
vLdpNgSvcFec128InLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128FecType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLabelId"),
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec128InLblEntry.setStatus("current")
_VLdpNgFec128InLabelId_Type = Unsigned32
_VLdpNgFec128InLabelId_Object = MibTableColumn
vLdpNgFec128InLabelId = _VLdpNgFec128InLabelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 1),
    _VLdpNgFec128InLabelId_Type()
)
vLdpNgFec128InLabelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec128InLabelId.setStatus("current")
_VLdpNgFec128InLabel_Type = Unsigned32
_VLdpNgFec128InLabel_Object = MibTableColumn
vLdpNgFec128InLabel = _VLdpNgFec128InLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 2),
    _VLdpNgFec128InLabel_Type()
)
vLdpNgFec128InLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLabel.setStatus("current")
_VLdpNgFec128InLabelStatus_Type = TmnxLabelStatus
_VLdpNgFec128InLabelStatus_Object = MibTableColumn
vLdpNgFec128InLabelStatus = _VLdpNgFec128InLabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 3),
    _VLdpNgFec128InLabelStatus_Type()
)
vLdpNgFec128InLabelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLabelStatus.setStatus("current")
_VLdpNgFec128InLabelSigStatus_Type = TmnxLabelSigStatus
_VLdpNgFec128InLabelSigStatus_Object = MibTableColumn
vLdpNgFec128InLabelSigStatus = _VLdpNgFec128InLabelSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 4),
    _VLdpNgFec128InLabelSigStatus_Type()
)
vLdpNgFec128InLabelSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLabelSigStatus.setStatus("current")
_VLdpNgFec128InLblWdwReason_Type = TmnxLdpInLblWdrawalReasonCode
_VLdpNgFec128InLblWdwReason_Object = MibTableColumn
vLdpNgFec128InLblWdwReason = _VLdpNgFec128InLblWdwReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 5),
    _VLdpNgFec128InLblWdwReason_Type()
)
vLdpNgFec128InLblWdwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblWdwReason.setStatus("current")
_VLdpNgFec128InLblMaxCellConcat_Type = Unsigned32
_VLdpNgFec128InLblMaxCellConcat_Object = MibTableColumn
vLdpNgFec128InLblMaxCellConcat = _VLdpNgFec128InLblMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 6),
    _VLdpNgFec128InLblMaxCellConcat_Type()
)
vLdpNgFec128InLblMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblMaxCellConcat.setStatus("current")
_VLdpNgFec128InLblFLTxCap_Type = TruthValue
_VLdpNgFec128InLblFLTxCap_Object = MibTableColumn
vLdpNgFec128InLblFLTxCap = _VLdpNgFec128InLblFLTxCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 7),
    _VLdpNgFec128InLblFLTxCap_Type()
)
vLdpNgFec128InLblFLTxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblFLTxCap.setStatus("current")
_VLdpNgFec128InLblFLRxCap_Type = TruthValue
_VLdpNgFec128InLblFLRxCap_Object = MibTableColumn
vLdpNgFec128InLblFLRxCap = _VLdpNgFec128InLblFLRxCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 8),
    _VLdpNgFec128InLblFLRxCap_Type()
)
vLdpNgFec128InLblFLRxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblFLRxCap.setStatus("current")
_VLdpNgFec128InLblIPv4CeIpAdType_Type = InetAddressType
_VLdpNgFec128InLblIPv4CeIpAdType_Object = MibTableColumn
vLdpNgFec128InLblIPv4CeIpAdType = _VLdpNgFec128InLblIPv4CeIpAdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 9),
    _VLdpNgFec128InLblIPv4CeIpAdType_Type()
)
vLdpNgFec128InLblIPv4CeIpAdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblIPv4CeIpAdType.setStatus("current")


class _VLdpNgFec128InLblIPv4CeIpAddr_Type(InetAddress):
    """Custom type vLdpNgFec128InLblIPv4CeIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VLdpNgFec128InLblIPv4CeIpAddr_Type.__name__ = "InetAddress"
_VLdpNgFec128InLblIPv4CeIpAddr_Object = MibTableColumn
vLdpNgFec128InLblIPv4CeIpAddr = _VLdpNgFec128InLblIPv4CeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 10),
    _VLdpNgFec128InLblIPv4CeIpAddr_Type()
)
vLdpNgFec128InLblIPv4CeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblIPv4CeIpAddr.setStatus("current")
_VLdpNgFec128InLblIPv4Cap_Type = TruthValue
_VLdpNgFec128InLblIPv4Cap_Object = MibTableColumn
vLdpNgFec128InLblIPv4Cap = _VLdpNgFec128InLblIPv4Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 11),
    _VLdpNgFec128InLblIPv4Cap_Type()
)
vLdpNgFec128InLblIPv4Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblIPv4Cap.setStatus("current")
_VLdpNgFec128InLblIPv6Cap_Type = TruthValue
_VLdpNgFec128InLblIPv6Cap_Object = MibTableColumn
vLdpNgFec128InLblIPv6Cap = _VLdpNgFec128InLblIPv6Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 12),
    _VLdpNgFec128InLblIPv6Cap_Type()
)
vLdpNgFec128InLblIPv6Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblIPv6Cap.setStatus("current")
_VLdpNgFec128InLblMTU_Type = Unsigned32
_VLdpNgFec128InLblMTU_Object = MibTableColumn
vLdpNgFec128InLblMTU = _VLdpNgFec128InLblMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 13),
    _VLdpNgFec128InLblMTU_Type()
)
vLdpNgFec128InLblMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblMTU.setStatus("current")
_VLdpNgFec128InLblVlanTag_Type = Unsigned32
_VLdpNgFec128InLblVlanTag_Object = MibTableColumn
vLdpNgFec128InLblVlanTag = _VLdpNgFec128InLblVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 14),
    _VLdpNgFec128InLblVlanTag_Type()
)
vLdpNgFec128InLblVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblVlanTag.setStatus("current")


class _VLdpNgFec128InLblVccvCV_Type(Bits):
    """Custom type vLdpNgFec128InLblVccvCV based on Bits"""
    namedValues = NamedValues(
        *(("icmpPing", 0),
          ("lspPing", 1),
          ("bfdFaultDetect", 2),
          ("bfdFaultDetectSignalling", 3))
    )

_VLdpNgFec128InLblVccvCV_Type.__name__ = "Bits"
_VLdpNgFec128InLblVccvCV_Object = MibTableColumn
vLdpNgFec128InLblVccvCV = _VLdpNgFec128InLblVccvCV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 15),
    _VLdpNgFec128InLblVccvCV_Type()
)
vLdpNgFec128InLblVccvCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblVccvCV.setStatus("current")


class _VLdpNgFec128InLblVccvCC_Type(Bits):
    """Custom type vLdpNgFec128InLblVccvCC based on Bits"""
    namedValues = NamedValues(
        *(("pwe3ControlWord", 0),
          ("routerAlertLabel", 1),
          ("mplsDemuxLabelTL1", 2))
    )

_VLdpNgFec128InLblVccvCC_Type.__name__ = "Bits"
_VLdpNgFec128InLblVccvCC_Object = MibTableColumn
vLdpNgFec128InLblVccvCC = _VLdpNgFec128InLblVccvCC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 16),
    _VLdpNgFec128InLblVccvCC_Type()
)
vLdpNgFec128InLblVccvCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblVccvCC.setStatus("current")
_VLdpNgFec128InLblPwStatus_Type = TruthValue
_VLdpNgFec128InLblPwStatus_Object = MibTableColumn
vLdpNgFec128InLblPwStatus = _VLdpNgFec128InLblPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 23, 1, 17),
    _VLdpNgFec128InLblPwStatus_Type()
)
vLdpNgFec128InLblPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128InLblPwStatus.setStatus("current")
_VLdpNgSvcFec128OutLblTable_Object = MibTable
vLdpNgSvcFec128OutLblTable = _VLdpNgSvcFec128OutLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24)
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec128OutLblTable.setStatus("current")
_VLdpNgSvcFec128OutLblEntry_Object = MibTableRow
vLdpNgSvcFec128OutLblEntry = _VLdpNgSvcFec128OutLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1)
)
vLdpNgSvcFec128OutLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128FecType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcId"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLabelId"),
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec128OutLblEntry.setStatus("current")
_VLdpNgFec128OutLabelId_Type = Unsigned32
_VLdpNgFec128OutLabelId_Object = MibTableColumn
vLdpNgFec128OutLabelId = _VLdpNgFec128OutLabelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 1),
    _VLdpNgFec128OutLabelId_Type()
)
vLdpNgFec128OutLabelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLabelId.setStatus("current")
_VLdpNgFec128OutLabel_Type = Unsigned32
_VLdpNgFec128OutLabel_Object = MibTableColumn
vLdpNgFec128OutLabel = _VLdpNgFec128OutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 2),
    _VLdpNgFec128OutLabel_Type()
)
vLdpNgFec128OutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLabel.setStatus("current")
_VLdpNgFec128OutLabelStatus_Type = TmnxLabelStatus
_VLdpNgFec128OutLabelStatus_Object = MibTableColumn
vLdpNgFec128OutLabelStatus = _VLdpNgFec128OutLabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 3),
    _VLdpNgFec128OutLabelStatus_Type()
)
vLdpNgFec128OutLabelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLabelStatus.setStatus("current")
_VLdpNgFec128OutLabelSigStatus_Type = TmnxLabelSigStatus
_VLdpNgFec128OutLabelSigStatus_Object = MibTableColumn
vLdpNgFec128OutLabelSigStatus = _VLdpNgFec128OutLabelSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 4),
    _VLdpNgFec128OutLabelSigStatus_Type()
)
vLdpNgFec128OutLabelSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLabelSigStatus.setStatus("current")
_VLdpNgFec128OutLblMaxCellConcat_Type = Unsigned32
_VLdpNgFec128OutLblMaxCellConcat_Object = MibTableColumn
vLdpNgFec128OutLblMaxCellConcat = _VLdpNgFec128OutLblMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 5),
    _VLdpNgFec128OutLblMaxCellConcat_Type()
)
vLdpNgFec128OutLblMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblMaxCellConcat.setStatus("current")
_VLdpNgFec128OutLblFLTxCap_Type = TruthValue
_VLdpNgFec128OutLblFLTxCap_Object = MibTableColumn
vLdpNgFec128OutLblFLTxCap = _VLdpNgFec128OutLblFLTxCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 6),
    _VLdpNgFec128OutLblFLTxCap_Type()
)
vLdpNgFec128OutLblFLTxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblFLTxCap.setStatus("current")
_VLdpNgFec128OutLblFLRxCap_Type = TruthValue
_VLdpNgFec128OutLblFLRxCap_Object = MibTableColumn
vLdpNgFec128OutLblFLRxCap = _VLdpNgFec128OutLblFLRxCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 7),
    _VLdpNgFec128OutLblFLRxCap_Type()
)
vLdpNgFec128OutLblFLRxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblFLRxCap.setStatus("current")
_VLdpNgFec128OutLblIPv4CeAddrType_Type = InetAddressType
_VLdpNgFec128OutLblIPv4CeAddrType_Object = MibTableColumn
vLdpNgFec128OutLblIPv4CeAddrType = _VLdpNgFec128OutLblIPv4CeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 8),
    _VLdpNgFec128OutLblIPv4CeAddrType_Type()
)
vLdpNgFec128OutLblIPv4CeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblIPv4CeAddrType.setStatus("current")


class _VLdpNgFec128OutLblIPv4CeIpAddr_Type(InetAddress):
    """Custom type vLdpNgFec128OutLblIPv4CeIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VLdpNgFec128OutLblIPv4CeIpAddr_Type.__name__ = "InetAddress"
_VLdpNgFec128OutLblIPv4CeIpAddr_Object = MibTableColumn
vLdpNgFec128OutLblIPv4CeIpAddr = _VLdpNgFec128OutLblIPv4CeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 9),
    _VLdpNgFec128OutLblIPv4CeIpAddr_Type()
)
vLdpNgFec128OutLblIPv4CeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblIPv4CeIpAddr.setStatus("current")
_VLdpNgFec128OutLblIPv4Cap_Type = TruthValue
_VLdpNgFec128OutLblIPv4Cap_Object = MibTableColumn
vLdpNgFec128OutLblIPv4Cap = _VLdpNgFec128OutLblIPv4Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 10),
    _VLdpNgFec128OutLblIPv4Cap_Type()
)
vLdpNgFec128OutLblIPv4Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblIPv4Cap.setStatus("current")
_VLdpNgFec128OutLblIPv6Cap_Type = TruthValue
_VLdpNgFec128OutLblIPv6Cap_Object = MibTableColumn
vLdpNgFec128OutLblIPv6Cap = _VLdpNgFec128OutLblIPv6Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 11),
    _VLdpNgFec128OutLblIPv6Cap_Type()
)
vLdpNgFec128OutLblIPv6Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblIPv6Cap.setStatus("current")
_VLdpNgFec128OutLblMTU_Type = Unsigned32
_VLdpNgFec128OutLblMTU_Object = MibTableColumn
vLdpNgFec128OutLblMTU = _VLdpNgFec128OutLblMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 12),
    _VLdpNgFec128OutLblMTU_Type()
)
vLdpNgFec128OutLblMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblMTU.setStatus("current")
_VLdpNgFec128OutLblVlanTag_Type = Unsigned32
_VLdpNgFec128OutLblVlanTag_Object = MibTableColumn
vLdpNgFec128OutLblVlanTag = _VLdpNgFec128OutLblVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 13),
    _VLdpNgFec128OutLblVlanTag_Type()
)
vLdpNgFec128OutLblVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblVlanTag.setStatus("current")


class _VLdpNgFec128OutLblVccvCV_Type(Bits):
    """Custom type vLdpNgFec128OutLblVccvCV based on Bits"""
    namedValues = NamedValues(
        *(("icmpPing", 0),
          ("lspPing", 1),
          ("bfdFaultDetect", 2),
          ("bfdFaultDetectSignalling", 3))
    )

_VLdpNgFec128OutLblVccvCV_Type.__name__ = "Bits"
_VLdpNgFec128OutLblVccvCV_Object = MibTableColumn
vLdpNgFec128OutLblVccvCV = _VLdpNgFec128OutLblVccvCV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 14),
    _VLdpNgFec128OutLblVccvCV_Type()
)
vLdpNgFec128OutLblVccvCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblVccvCV.setStatus("current")


class _VLdpNgFec128OutLblVccvCC_Type(Bits):
    """Custom type vLdpNgFec128OutLblVccvCC based on Bits"""
    namedValues = NamedValues(
        *(("pwe3ControlWord", 0),
          ("routerAlertLabel", 1),
          ("mplsDemuxLabelTL1", 2))
    )

_VLdpNgFec128OutLblVccvCC_Type.__name__ = "Bits"
_VLdpNgFec128OutLblVccvCC_Object = MibTableColumn
vLdpNgFec128OutLblVccvCC = _VLdpNgFec128OutLblVccvCC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 15),
    _VLdpNgFec128OutLblVccvCC_Type()
)
vLdpNgFec128OutLblVccvCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblVccvCC.setStatus("current")
_VLdpNgFec128OutLblPwStatus_Type = TruthValue
_VLdpNgFec128OutLblPwStatus_Object = MibTableColumn
vLdpNgFec128OutLblPwStatus = _VLdpNgFec128OutLblPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 24, 1, 16),
    _VLdpNgFec128OutLblPwStatus_Type()
)
vLdpNgFec128OutLblPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec128OutLblPwStatus.setStatus("current")
_VRtrLdpNgHelloAdjMapTable_Object = MibTable
vRtrLdpNgHelloAdjMapTable = _VRtrLdpNgHelloAdjMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 25)
)
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjMapTable.setStatus("current")
_VRtrLdpNgHelloAdjMapEntry_Object = MibTableRow
vRtrLdpNgHelloAdjMapEntry = _VRtrLdpNgHelloAdjMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 25, 1)
)
vRtrLdpNgHelloAdjMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfIndex"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddressType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddress"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjMapLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjMapLdpId"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjMapEntry.setStatus("current")
_VRtrLdpNgHelloAdjMapLdpIdType_Type = TmnxMplsLdpNgIdType
_VRtrLdpNgHelloAdjMapLdpIdType_Object = MibTableColumn
vRtrLdpNgHelloAdjMapLdpIdType = _VRtrLdpNgHelloAdjMapLdpIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 25, 1, 1),
    _VRtrLdpNgHelloAdjMapLdpIdType_Type()
)
vRtrLdpNgHelloAdjMapLdpIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjMapLdpIdType.setStatus("current")


class _VRtrLdpNgHelloAdjMapLdpId_Type(TmnxMplsLdpNgIdentifier):
    """Custom type vRtrLdpNgHelloAdjMapLdpId based on TmnxMplsLdpNgIdentifier"""
    subtypeSpec = TmnxMplsLdpNgIdentifier.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(18, 18),
    )


_VRtrLdpNgHelloAdjMapLdpId_Type.__name__ = "TmnxMplsLdpNgIdentifier"
_VRtrLdpNgHelloAdjMapLdpId_Object = MibTableColumn
vRtrLdpNgHelloAdjMapLdpId = _VRtrLdpNgHelloAdjMapLdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 25, 1, 2),
    _VRtrLdpNgHelloAdjMapLdpId_Type()
)
vRtrLdpNgHelloAdjMapLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjMapLdpId.setStatus("current")


class _VRtrLdpNgHelloAdjMapIndex_Type(Unsigned32):
    """Custom type vRtrLdpNgHelloAdjMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrLdpNgHelloAdjMapIndex_Type.__name__ = "Unsigned32"
_VRtrLdpNgHelloAdjMapIndex_Object = MibTableColumn
vRtrLdpNgHelloAdjMapIndex = _VRtrLdpNgHelloAdjMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 25, 1, 3),
    _VRtrLdpNgHelloAdjMapIndex_Type()
)
vRtrLdpNgHelloAdjMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgHelloAdjMapIndex.setStatus("current")
_VLdpNgSvcFec129Table_Object = MibTable
vLdpNgSvcFec129Table = _VLdpNgSvcFec129Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26)
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec129Table.setStatus("current")
_VLdpNgSvcFec129Entry_Object = MibTableRow
vLdpNgSvcFec129Entry = _VLdpNgSvcFec129Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1)
)
vLdpNgSvcFec129Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec129Entry.setStatus("current")


class _VLdpNgFec129AgiType_Type(Unsigned32):
    """Custom type vLdpNgFec129AgiType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VLdpNgFec129AgiType_Type.__name__ = "Unsigned32"
_VLdpNgFec129AgiType_Object = MibTableColumn
vLdpNgFec129AgiType = _VLdpNgFec129AgiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 1),
    _VLdpNgFec129AgiType_Type()
)
vLdpNgFec129AgiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129AgiType.setStatus("current")


class _VLdpNgFec129AgiLen_Type(Unsigned32):
    """Custom type vLdpNgFec129AgiLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VLdpNgFec129AgiLen_Type.__name__ = "Unsigned32"
_VLdpNgFec129AgiLen_Object = MibTableColumn
vLdpNgFec129AgiLen = _VLdpNgFec129AgiLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 2),
    _VLdpNgFec129AgiLen_Type()
)
vLdpNgFec129AgiLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129AgiLen.setStatus("current")


class _VLdpNgFec129AgiVal_Type(OctetString):
    """Custom type vLdpNgFec129AgiVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VLdpNgFec129AgiVal_Type.__name__ = "OctetString"
_VLdpNgFec129AgiVal_Object = MibTableColumn
vLdpNgFec129AgiVal = _VLdpNgFec129AgiVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 3),
    _VLdpNgFec129AgiVal_Type()
)
vLdpNgFec129AgiVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129AgiVal.setStatus("current")


class _VLdpNgFec129SrcAiiType_Type(Unsigned32):
    """Custom type vLdpNgFec129SrcAiiType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VLdpNgFec129SrcAiiType_Type.__name__ = "Unsigned32"
_VLdpNgFec129SrcAiiType_Object = MibTableColumn
vLdpNgFec129SrcAiiType = _VLdpNgFec129SrcAiiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 4),
    _VLdpNgFec129SrcAiiType_Type()
)
vLdpNgFec129SrcAiiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129SrcAiiType.setStatus("current")


class _VLdpNgFec129SrcAiiLen_Type(Unsigned32):
    """Custom type vLdpNgFec129SrcAiiLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VLdpNgFec129SrcAiiLen_Type.__name__ = "Unsigned32"
_VLdpNgFec129SrcAiiLen_Object = MibTableColumn
vLdpNgFec129SrcAiiLen = _VLdpNgFec129SrcAiiLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 5),
    _VLdpNgFec129SrcAiiLen_Type()
)
vLdpNgFec129SrcAiiLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129SrcAiiLen.setStatus("current")


class _VLdpNgFec129SrcAiiVal_Type(OctetString):
    """Custom type vLdpNgFec129SrcAiiVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VLdpNgFec129SrcAiiVal_Type.__name__ = "OctetString"
_VLdpNgFec129SrcAiiVal_Object = MibTableColumn
vLdpNgFec129SrcAiiVal = _VLdpNgFec129SrcAiiVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 6),
    _VLdpNgFec129SrcAiiVal_Type()
)
vLdpNgFec129SrcAiiVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129SrcAiiVal.setStatus("current")


class _VLdpNgFec129TgtAiiType_Type(Unsigned32):
    """Custom type vLdpNgFec129TgtAiiType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VLdpNgFec129TgtAiiType_Type.__name__ = "Unsigned32"
_VLdpNgFec129TgtAiiType_Object = MibTableColumn
vLdpNgFec129TgtAiiType = _VLdpNgFec129TgtAiiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 7),
    _VLdpNgFec129TgtAiiType_Type()
)
vLdpNgFec129TgtAiiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129TgtAiiType.setStatus("current")


class _VLdpNgFec129TgtAiiLen_Type(Unsigned32):
    """Custom type vLdpNgFec129TgtAiiLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VLdpNgFec129TgtAiiLen_Type.__name__ = "Unsigned32"
_VLdpNgFec129TgtAiiLen_Object = MibTableColumn
vLdpNgFec129TgtAiiLen = _VLdpNgFec129TgtAiiLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 8),
    _VLdpNgFec129TgtAiiLen_Type()
)
vLdpNgFec129TgtAiiLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129TgtAiiLen.setStatus("current")


class _VLdpNgFec129TgtAiiVal_Type(OctetString):
    """Custom type vLdpNgFec129TgtAiiVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VLdpNgFec129TgtAiiVal_Type.__name__ = "OctetString"
_VLdpNgFec129TgtAiiVal_Object = MibTableColumn
vLdpNgFec129TgtAiiVal = _VLdpNgFec129TgtAiiVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 9),
    _VLdpNgFec129TgtAiiVal_Type()
)
vLdpNgFec129TgtAiiVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129TgtAiiVal.setStatus("current")
_VLdpNgFec129ServType_Type = ServType
_VLdpNgFec129ServType_Object = MibTableColumn
vLdpNgFec129ServType = _VLdpNgFec129ServType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 10),
    _VLdpNgFec129ServType_Type()
)
vLdpNgFec129ServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129ServType.setStatus("current")


class _VLdpNgFec129ServId_Type(TmnxServId):
    """Custom type vLdpNgFec129ServId based on TmnxServId"""
    subtypeSpec = TmnxServId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VLdpNgFec129ServId_Type.__name__ = "TmnxServId"
_VLdpNgFec129ServId_Object = MibTableColumn
vLdpNgFec129ServId = _VLdpNgFec129ServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 11),
    _VLdpNgFec129ServId_Type()
)
vLdpNgFec129ServId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129ServId.setStatus("current")
_VLdpNgFec129VpnId_Type = TmnxVpnId
_VLdpNgFec129VpnId_Object = MibTableColumn
vLdpNgFec129VpnId = _VLdpNgFec129VpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 12),
    _VLdpNgFec129VpnId_Type()
)
vLdpNgFec129VpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129VpnId.setStatus("current")
_VLdpNgFec129Flags_Type = TmnxLdpFECFlags
_VLdpNgFec129Flags_Object = MibTableColumn
vLdpNgFec129Flags = _VLdpNgFec129Flags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 13),
    _VLdpNgFec129Flags_Type()
)
vLdpNgFec129Flags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129Flags.setStatus("current")
_VLdpNgFec129NumInLabels_Type = Unsigned32
_VLdpNgFec129NumInLabels_Object = MibTableColumn
vLdpNgFec129NumInLabels = _VLdpNgFec129NumInLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 14),
    _VLdpNgFec129NumInLabels_Type()
)
vLdpNgFec129NumInLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129NumInLabels.setStatus("current")
_VLdpNgFec129NumOutLabels_Type = Unsigned32
_VLdpNgFec129NumOutLabels_Object = MibTableColumn
vLdpNgFec129NumOutLabels = _VLdpNgFec129NumOutLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 15),
    _VLdpNgFec129NumOutLabels_Type()
)
vLdpNgFec129NumOutLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129NumOutLabels.setStatus("current")
_VLdpNgFec129SdpId_Type = SdpId
_VLdpNgFec129SdpId_Object = MibTableColumn
vLdpNgFec129SdpId = _VLdpNgFec129SdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 16),
    _VLdpNgFec129SdpId_Type()
)
vLdpNgFec129SdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129SdpId.setStatus("current")


class _VLdpNgFec129MateAgiType_Type(Unsigned32):
    """Custom type vLdpNgFec129MateAgiType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VLdpNgFec129MateAgiType_Type.__name__ = "Unsigned32"
_VLdpNgFec129MateAgiType_Object = MibTableColumn
vLdpNgFec129MateAgiType = _VLdpNgFec129MateAgiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 17),
    _VLdpNgFec129MateAgiType_Type()
)
vLdpNgFec129MateAgiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateAgiType.setStatus("current")


class _VLdpNgFec129MateAgiLen_Type(Unsigned32):
    """Custom type vLdpNgFec129MateAgiLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VLdpNgFec129MateAgiLen_Type.__name__ = "Unsigned32"
_VLdpNgFec129MateAgiLen_Object = MibTableColumn
vLdpNgFec129MateAgiLen = _VLdpNgFec129MateAgiLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 18),
    _VLdpNgFec129MateAgiLen_Type()
)
vLdpNgFec129MateAgiLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateAgiLen.setStatus("current")


class _VLdpNgFec129MateAgiVal_Type(OctetString):
    """Custom type vLdpNgFec129MateAgiVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VLdpNgFec129MateAgiVal_Type.__name__ = "OctetString"
_VLdpNgFec129MateAgiVal_Object = MibTableColumn
vLdpNgFec129MateAgiVal = _VLdpNgFec129MateAgiVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 19),
    _VLdpNgFec129MateAgiVal_Type()
)
vLdpNgFec129MateAgiVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateAgiVal.setStatus("current")


class _VLdpNgFec129MateSrcAiiType_Type(Unsigned32):
    """Custom type vLdpNgFec129MateSrcAiiType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VLdpNgFec129MateSrcAiiType_Type.__name__ = "Unsigned32"
_VLdpNgFec129MateSrcAiiType_Object = MibTableColumn
vLdpNgFec129MateSrcAiiType = _VLdpNgFec129MateSrcAiiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 20),
    _VLdpNgFec129MateSrcAiiType_Type()
)
vLdpNgFec129MateSrcAiiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateSrcAiiType.setStatus("current")


class _VLdpNgFec129MateSrcAiiLen_Type(Unsigned32):
    """Custom type vLdpNgFec129MateSrcAiiLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VLdpNgFec129MateSrcAiiLen_Type.__name__ = "Unsigned32"
_VLdpNgFec129MateSrcAiiLen_Object = MibTableColumn
vLdpNgFec129MateSrcAiiLen = _VLdpNgFec129MateSrcAiiLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 21),
    _VLdpNgFec129MateSrcAiiLen_Type()
)
vLdpNgFec129MateSrcAiiLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateSrcAiiLen.setStatus("current")


class _VLdpNgFec129MateSrcAiiVal_Type(OctetString):
    """Custom type vLdpNgFec129MateSrcAiiVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VLdpNgFec129MateSrcAiiVal_Type.__name__ = "OctetString"
_VLdpNgFec129MateSrcAiiVal_Object = MibTableColumn
vLdpNgFec129MateSrcAiiVal = _VLdpNgFec129MateSrcAiiVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 22),
    _VLdpNgFec129MateSrcAiiVal_Type()
)
vLdpNgFec129MateSrcAiiVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateSrcAiiVal.setStatus("current")


class _VLdpNgFec129MateTgtAiiType_Type(Unsigned32):
    """Custom type vLdpNgFec129MateTgtAiiType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VLdpNgFec129MateTgtAiiType_Type.__name__ = "Unsigned32"
_VLdpNgFec129MateTgtAiiType_Object = MibTableColumn
vLdpNgFec129MateTgtAiiType = _VLdpNgFec129MateTgtAiiType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 23),
    _VLdpNgFec129MateTgtAiiType_Type()
)
vLdpNgFec129MateTgtAiiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateTgtAiiType.setStatus("current")


class _VLdpNgFec129MateTgtAiiLen_Type(Unsigned32):
    """Custom type vLdpNgFec129MateTgtAiiLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VLdpNgFec129MateTgtAiiLen_Type.__name__ = "Unsigned32"
_VLdpNgFec129MateTgtAiiLen_Object = MibTableColumn
vLdpNgFec129MateTgtAiiLen = _VLdpNgFec129MateTgtAiiLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 24),
    _VLdpNgFec129MateTgtAiiLen_Type()
)
vLdpNgFec129MateTgtAiiLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateTgtAiiLen.setStatus("current")


class _VLdpNgFec129MateTgtAiiVal_Type(OctetString):
    """Custom type vLdpNgFec129MateTgtAiiVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VLdpNgFec129MateTgtAiiVal_Type.__name__ = "OctetString"
_VLdpNgFec129MateTgtAiiVal_Object = MibTableColumn
vLdpNgFec129MateTgtAiiVal = _VLdpNgFec129MateTgtAiiVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 25),
    _VLdpNgFec129MateTgtAiiVal_Type()
)
vLdpNgFec129MateTgtAiiVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateTgtAiiVal.setStatus("current")
_VLdpNgFec129MateSdpId_Type = SdpId
_VLdpNgFec129MateSdpId_Object = MibTableColumn
vLdpNgFec129MateSdpId = _VLdpNgFec129MateSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 26, 1, 26),
    _VLdpNgFec129MateSdpId_Type()
)
vLdpNgFec129MateSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129MateSdpId.setStatus("current")
_VLdpNgSvcFec129InLblTable_Object = MibTable
vLdpNgSvcFec129InLblTable = _VLdpNgSvcFec129InLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27)
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec129InLblTable.setStatus("current")
_VLdpNgSvcFec129InLblEntry_Object = MibTableRow
vLdpNgSvcFec129InLblEntry = _VLdpNgSvcFec129InLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1)
)
vLdpNgSvcFec129InLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblId"),
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec129InLblEntry.setStatus("current")
_VLdpNgFec129InLblId_Type = Unsigned32
_VLdpNgFec129InLblId_Object = MibTableColumn
vLdpNgFec129InLblId = _VLdpNgFec129InLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 1),
    _VLdpNgFec129InLblId_Type()
)
vLdpNgFec129InLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblId.setStatus("current")
_VLdpNgFec129InLabel_Type = Unsigned32
_VLdpNgFec129InLabel_Object = MibTableColumn
vLdpNgFec129InLabel = _VLdpNgFec129InLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 2),
    _VLdpNgFec129InLabel_Type()
)
vLdpNgFec129InLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLabel.setStatus("current")
_VLdpNgFec129InLabelStatus_Type = TmnxLabelStatus
_VLdpNgFec129InLabelStatus_Object = MibTableColumn
vLdpNgFec129InLabelStatus = _VLdpNgFec129InLabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 3),
    _VLdpNgFec129InLabelStatus_Type()
)
vLdpNgFec129InLabelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLabelStatus.setStatus("current")
_VLdpNgFec129InLblMTU_Type = Unsigned32
_VLdpNgFec129InLblMTU_Object = MibTableColumn
vLdpNgFec129InLblMTU = _VLdpNgFec129InLblMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 4),
    _VLdpNgFec129InLblMTU_Type()
)
vLdpNgFec129InLblMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblMTU.setStatus("current")
_VLdpNgFec129InLblVlanTag_Type = Unsigned32
_VLdpNgFec129InLblVlanTag_Object = MibTableColumn
vLdpNgFec129InLblVlanTag = _VLdpNgFec129InLblVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 5),
    _VLdpNgFec129InLblVlanTag_Type()
)
vLdpNgFec129InLblVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblVlanTag.setStatus("current")
_VLdpNgFec129InLblMaxCellConcat_Type = Unsigned32
_VLdpNgFec129InLblMaxCellConcat_Object = MibTableColumn
vLdpNgFec129InLblMaxCellConcat = _VLdpNgFec129InLblMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 6),
    _VLdpNgFec129InLblMaxCellConcat_Type()
)
vLdpNgFec129InLblMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblMaxCellConcat.setStatus("current")
_VLdpNgFec129InLblSigStatus_Type = TmnxLabelSigStatus
_VLdpNgFec129InLblSigStatus_Object = MibTableColumn
vLdpNgFec129InLblSigStatus = _VLdpNgFec129InLblSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 7),
    _VLdpNgFec129InLblSigStatus_Type()
)
vLdpNgFec129InLblSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblSigStatus.setStatus("current")
_VLdpNgFec129InLblIPv4Cap_Type = TruthValue
_VLdpNgFec129InLblIPv4Cap_Object = MibTableColumn
vLdpNgFec129InLblIPv4Cap = _VLdpNgFec129InLblIPv4Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 8),
    _VLdpNgFec129InLblIPv4Cap_Type()
)
vLdpNgFec129InLblIPv4Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblIPv4Cap.setStatus("current")
_VLdpNgFec129InLblIPv6Cap_Type = TruthValue
_VLdpNgFec129InLblIPv6Cap_Object = MibTableColumn
vLdpNgFec129InLblIPv6Cap = _VLdpNgFec129InLblIPv6Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 9),
    _VLdpNgFec129InLblIPv6Cap_Type()
)
vLdpNgFec129InLblIPv6Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblIPv6Cap.setStatus("current")
_VLdpNgFec129InLblIPv4CeAddrType_Type = InetAddressType
_VLdpNgFec129InLblIPv4CeAddrType_Object = MibTableColumn
vLdpNgFec129InLblIPv4CeAddrType = _VLdpNgFec129InLblIPv4CeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 10),
    _VLdpNgFec129InLblIPv4CeAddrType_Type()
)
vLdpNgFec129InLblIPv4CeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblIPv4CeAddrType.setStatus("current")


class _VLdpNgFec129InLblIPv4CeIpAddr_Type(InetAddress):
    """Custom type vLdpNgFec129InLblIPv4CeIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VLdpNgFec129InLblIPv4CeIpAddr_Type.__name__ = "InetAddress"
_VLdpNgFec129InLblIPv4CeIpAddr_Object = MibTableColumn
vLdpNgFec129InLblIPv4CeIpAddr = _VLdpNgFec129InLblIPv4CeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 11),
    _VLdpNgFec129InLblIPv4CeIpAddr_Type()
)
vLdpNgFec129InLblIPv4CeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblIPv4CeIpAddr.setStatus("current")
_VLdpNgFec129InLblWdwReason_Type = TmnxLdpInLblWdrawalReasonCode
_VLdpNgFec129InLblWdwReason_Object = MibTableColumn
vLdpNgFec129InLblWdwReason = _VLdpNgFec129InLblWdwReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 12),
    _VLdpNgFec129InLblWdwReason_Type()
)
vLdpNgFec129InLblWdwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblWdwReason.setStatus("current")
_VLdpNgFec129InLblFLTxCap_Type = TruthValue
_VLdpNgFec129InLblFLTxCap_Object = MibTableColumn
vLdpNgFec129InLblFLTxCap = _VLdpNgFec129InLblFLTxCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 13),
    _VLdpNgFec129InLblFLTxCap_Type()
)
vLdpNgFec129InLblFLTxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblFLTxCap.setStatus("current")
_VLdpNgFec129InLblFLRxCap_Type = TruthValue
_VLdpNgFec129InLblFLRxCap_Object = MibTableColumn
vLdpNgFec129InLblFLRxCap = _VLdpNgFec129InLblFLRxCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 14),
    _VLdpNgFec129InLblFLRxCap_Type()
)
vLdpNgFec129InLblFLRxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblFLRxCap.setStatus("current")


class _VLdpNgFec129InLblVccvCV_Type(Bits):
    """Custom type vLdpNgFec129InLblVccvCV based on Bits"""
    namedValues = NamedValues(
        *(("icmpPing", 0),
          ("lspPing", 1),
          ("bfdFaultDetect", 2),
          ("bfdFaultDetectSignalling", 3))
    )

_VLdpNgFec129InLblVccvCV_Type.__name__ = "Bits"
_VLdpNgFec129InLblVccvCV_Object = MibTableColumn
vLdpNgFec129InLblVccvCV = _VLdpNgFec129InLblVccvCV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 15),
    _VLdpNgFec129InLblVccvCV_Type()
)
vLdpNgFec129InLblVccvCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblVccvCV.setStatus("current")


class _VLdpNgFec129InLblVccvCC_Type(Bits):
    """Custom type vLdpNgFec129InLblVccvCC based on Bits"""
    namedValues = NamedValues(
        *(("pwe3ControlWord", 0),
          ("routerAlertLabel", 1),
          ("mplsDemuxLabelTL1", 2))
    )

_VLdpNgFec129InLblVccvCC_Type.__name__ = "Bits"
_VLdpNgFec129InLblVccvCC_Object = MibTableColumn
vLdpNgFec129InLblVccvCC = _VLdpNgFec129InLblVccvCC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 16),
    _VLdpNgFec129InLblVccvCC_Type()
)
vLdpNgFec129InLblVccvCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblVccvCC.setStatus("current")
_VLdpNgFec129InLblPwStatus_Type = TruthValue
_VLdpNgFec129InLblPwStatus_Object = MibTableColumn
vLdpNgFec129InLblPwStatus = _VLdpNgFec129InLblPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 27, 1, 17),
    _VLdpNgFec129InLblPwStatus_Type()
)
vLdpNgFec129InLblPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129InLblPwStatus.setStatus("current")
_VLdpNgSvcFec129OutLblTable_Object = MibTable
vLdpNgSvcFec129OutLblTable = _VLdpNgSvcFec129OutLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28)
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec129OutLblTable.setStatus("current")
_VLdpNgSvcFec129OutLblEntry_Object = MibTableRow
vLdpNgSvcFec129OutLblEntry = _VLdpNgSvcFec129OutLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1)
)
vLdpNgSvcFec129OutLblEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec128VcType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129AgiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129SrcAiiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiType"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129TgtAiiVal"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpIdType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerLdpId"),
    (0, "TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblId"),
)
if mibBuilder.loadTexts:
    vLdpNgSvcFec129OutLblEntry.setStatus("current")
_VLdpNgFec129OutLblId_Type = Unsigned32
_VLdpNgFec129OutLblId_Object = MibTableColumn
vLdpNgFec129OutLblId = _VLdpNgFec129OutLblId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 1),
    _VLdpNgFec129OutLblId_Type()
)
vLdpNgFec129OutLblId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblId.setStatus("current")
_VLdpNgFec129OutLabel_Type = Unsigned32
_VLdpNgFec129OutLabel_Object = MibTableColumn
vLdpNgFec129OutLabel = _VLdpNgFec129OutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 2),
    _VLdpNgFec129OutLabel_Type()
)
vLdpNgFec129OutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLabel.setStatus("current")
_VLdpNgFec129OutLabelStatus_Type = TmnxLabelStatus
_VLdpNgFec129OutLabelStatus_Object = MibTableColumn
vLdpNgFec129OutLabelStatus = _VLdpNgFec129OutLabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 3),
    _VLdpNgFec129OutLabelStatus_Type()
)
vLdpNgFec129OutLabelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLabelStatus.setStatus("current")
_VLdpNgFec129OutLblMTU_Type = Unsigned32
_VLdpNgFec129OutLblMTU_Object = MibTableColumn
vLdpNgFec129OutLblMTU = _VLdpNgFec129OutLblMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 4),
    _VLdpNgFec129OutLblMTU_Type()
)
vLdpNgFec129OutLblMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblMTU.setStatus("current")
_VLdpNgFec129OutLblVlanTag_Type = Unsigned32
_VLdpNgFec129OutLblVlanTag_Object = MibTableColumn
vLdpNgFec129OutLblVlanTag = _VLdpNgFec129OutLblVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 5),
    _VLdpNgFec129OutLblVlanTag_Type()
)
vLdpNgFec129OutLblVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblVlanTag.setStatus("current")
_VLdpNgFec129OutLblMaxCellConcat_Type = Unsigned32
_VLdpNgFec129OutLblMaxCellConcat_Object = MibTableColumn
vLdpNgFec129OutLblMaxCellConcat = _VLdpNgFec129OutLblMaxCellConcat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 6),
    _VLdpNgFec129OutLblMaxCellConcat_Type()
)
vLdpNgFec129OutLblMaxCellConcat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblMaxCellConcat.setStatus("current")
_VLdpNgFec129OutLblSigStatus_Type = TmnxLabelSigStatus
_VLdpNgFec129OutLblSigStatus_Object = MibTableColumn
vLdpNgFec129OutLblSigStatus = _VLdpNgFec129OutLblSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 7),
    _VLdpNgFec129OutLblSigStatus_Type()
)
vLdpNgFec129OutLblSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblSigStatus.setStatus("current")
_VLdpNgFec129OutLblIPv4Cap_Type = TruthValue
_VLdpNgFec129OutLblIPv4Cap_Object = MibTableColumn
vLdpNgFec129OutLblIPv4Cap = _VLdpNgFec129OutLblIPv4Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 8),
    _VLdpNgFec129OutLblIPv4Cap_Type()
)
vLdpNgFec129OutLblIPv4Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblIPv4Cap.setStatus("current")
_VLdpNgFec129OutLblIPv6Cap_Type = TruthValue
_VLdpNgFec129OutLblIPv6Cap_Object = MibTableColumn
vLdpNgFec129OutLblIPv6Cap = _VLdpNgFec129OutLblIPv6Cap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 9),
    _VLdpNgFec129OutLblIPv6Cap_Type()
)
vLdpNgFec129OutLblIPv6Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblIPv6Cap.setStatus("current")
_VLdpNgFec129OutLblIPv4CeAddrType_Type = InetAddressType
_VLdpNgFec129OutLblIPv4CeAddrType_Object = MibTableColumn
vLdpNgFec129OutLblIPv4CeAddrType = _VLdpNgFec129OutLblIPv4CeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 10),
    _VLdpNgFec129OutLblIPv4CeAddrType_Type()
)
vLdpNgFec129OutLblIPv4CeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblIPv4CeAddrType.setStatus("current")


class _VLdpNgFec129OutLblIPv4CeIpAddr_Type(InetAddress):
    """Custom type vLdpNgFec129OutLblIPv4CeIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VLdpNgFec129OutLblIPv4CeIpAddr_Type.__name__ = "InetAddress"
_VLdpNgFec129OutLblIPv4CeIpAddr_Object = MibTableColumn
vLdpNgFec129OutLblIPv4CeIpAddr = _VLdpNgFec129OutLblIPv4CeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 11),
    _VLdpNgFec129OutLblIPv4CeIpAddr_Type()
)
vLdpNgFec129OutLblIPv4CeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblIPv4CeIpAddr.setStatus("current")
_VLdpNgFec129OutLblFLTxCap_Type = TruthValue
_VLdpNgFec129OutLblFLTxCap_Object = MibTableColumn
vLdpNgFec129OutLblFLTxCap = _VLdpNgFec129OutLblFLTxCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 12),
    _VLdpNgFec129OutLblFLTxCap_Type()
)
vLdpNgFec129OutLblFLTxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblFLTxCap.setStatus("current")
_VLdpNgFec129OutLblFLRxCap_Type = TruthValue
_VLdpNgFec129OutLblFLRxCap_Object = MibTableColumn
vLdpNgFec129OutLblFLRxCap = _VLdpNgFec129OutLblFLRxCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 13),
    _VLdpNgFec129OutLblFLRxCap_Type()
)
vLdpNgFec129OutLblFLRxCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblFLRxCap.setStatus("current")


class _VLdpNgFec129OutLblVccvCV_Type(Bits):
    """Custom type vLdpNgFec129OutLblVccvCV based on Bits"""
    namedValues = NamedValues(
        *(("icmpPing", 0),
          ("lspPing", 1),
          ("bfdFaultDetect", 2),
          ("bfdFaultDetectSignalling", 3))
    )

_VLdpNgFec129OutLblVccvCV_Type.__name__ = "Bits"
_VLdpNgFec129OutLblVccvCV_Object = MibTableColumn
vLdpNgFec129OutLblVccvCV = _VLdpNgFec129OutLblVccvCV_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 14),
    _VLdpNgFec129OutLblVccvCV_Type()
)
vLdpNgFec129OutLblVccvCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblVccvCV.setStatus("current")


class _VLdpNgFec129OutLblVccvCC_Type(Bits):
    """Custom type vLdpNgFec129OutLblVccvCC based on Bits"""
    namedValues = NamedValues(
        *(("pwe3ControlWord", 0),
          ("routerAlertLabel", 1),
          ("mplsDemuxLabelTL1", 2))
    )

_VLdpNgFec129OutLblVccvCC_Type.__name__ = "Bits"
_VLdpNgFec129OutLblVccvCC_Object = MibTableColumn
vLdpNgFec129OutLblVccvCC = _VLdpNgFec129OutLblVccvCC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 15),
    _VLdpNgFec129OutLblVccvCC_Type()
)
vLdpNgFec129OutLblVccvCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblVccvCC.setStatus("current")
_VLdpNgFec129OutLblPwStatus_Type = TruthValue
_VLdpNgFec129OutLblPwStatus_Object = MibTableColumn
vLdpNgFec129OutLblPwStatus = _VLdpNgFec129OutLblPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 28, 1, 16),
    _VLdpNgFec129OutLblPwStatus_Type()
)
vLdpNgFec129OutLblPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgFec129OutLblPwStatus.setStatus("current")
_VLdpNgCepTdmFec128InLblTable_Object = MibTable
vLdpNgCepTdmFec128InLblTable = _VLdpNgCepTdmFec128InLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29)
)
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblTable.setStatus("current")
_VLdpNgCepTdmFec128InLblEntry_Object = MibTableRow
vLdpNgCepTdmFec128InLblEntry = _VLdpNgCepTdmFec128InLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1)
)
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblEntry.setStatus("current")
_VLdpNgCepTdmFec128InLblPayldSize_Type = Unsigned32
_VLdpNgCepTdmFec128InLblPayldSize_Object = MibTableColumn
vLdpNgCepTdmFec128InLblPayldSize = _VLdpNgCepTdmFec128InLblPayldSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 1),
    _VLdpNgCepTdmFec128InLblPayldSize_Type()
)
vLdpNgCepTdmFec128InLblPayldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblPayldSize.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblPayldSize.setUnits("bytes")
_VLdpNgCepTdmFec128InLblBitrate_Type = Unsigned32
_VLdpNgCepTdmFec128InLblBitrate_Object = MibTableColumn
vLdpNgCepTdmFec128InLblBitrate = _VLdpNgCepTdmFec128InLblBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 2),
    _VLdpNgCepTdmFec128InLblBitrate_Type()
)
vLdpNgCepTdmFec128InLblBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblBitrate.setUnits("64 Kbits/s")
_VLdpNgCepTdmFec128InLblRtpHeader_Type = TruthValue
_VLdpNgCepTdmFec128InLblRtpHeader_Object = MibTableColumn
vLdpNgCepTdmFec128InLblRtpHeader = _VLdpNgCepTdmFec128InLblRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 3),
    _VLdpNgCepTdmFec128InLblRtpHeader_Type()
)
vLdpNgCepTdmFec128InLblRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblRtpHeader.setStatus("current")
_VLdpNgCepTdmFec128InLblDiffTStmp_Type = TruthValue
_VLdpNgCepTdmFec128InLblDiffTStmp_Object = MibTableColumn
vLdpNgCepTdmFec128InLblDiffTStmp = _VLdpNgCepTdmFec128InLblDiffTStmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 4),
    _VLdpNgCepTdmFec128InLblDiffTStmp_Type()
)
vLdpNgCepTdmFec128InLblDiffTStmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblDiffTStmp.setStatus("current")
_VLdpNgCepTdmFec128InLblSigPkts_Type = TdmOptionsSigPkts
_VLdpNgCepTdmFec128InLblSigPkts_Object = MibTableColumn
vLdpNgCepTdmFec128InLblSigPkts = _VLdpNgCepTdmFec128InLblSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 5),
    _VLdpNgCepTdmFec128InLblSigPkts_Type()
)
vLdpNgCepTdmFec128InLblSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblSigPkts.setStatus("current")
_VLdpNgCepTdmFec128InLblCasTrunk_Type = TdmOptionsCasTrunkFraming
_VLdpNgCepTdmFec128InLblCasTrunk_Object = MibTableColumn
vLdpNgCepTdmFec128InLblCasTrunk = _VLdpNgCepTdmFec128InLblCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 6),
    _VLdpNgCepTdmFec128InLblCasTrunk_Type()
)
vLdpNgCepTdmFec128InLblCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblCasTrunk.setStatus("current")
_VLdpNgCepTdmFec128InLblTStmpFreq_Type = Unsigned32
_VLdpNgCepTdmFec128InLblTStmpFreq_Object = MibTableColumn
vLdpNgCepTdmFec128InLblTStmpFreq = _VLdpNgCepTdmFec128InLblTStmpFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 7),
    _VLdpNgCepTdmFec128InLblTStmpFreq_Type()
)
vLdpNgCepTdmFec128InLblTStmpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblTStmpFreq.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblTStmpFreq.setUnits("8 KHz")
_VLdpNgCepTdmFec128InLblPayldType_Type = Unsigned32
_VLdpNgCepTdmFec128InLblPayldType_Object = MibTableColumn
vLdpNgCepTdmFec128InLblPayldType = _VLdpNgCepTdmFec128InLblPayldType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 8),
    _VLdpNgCepTdmFec128InLblPayldType_Type()
)
vLdpNgCepTdmFec128InLblPayldType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblPayldType.setStatus("current")
_VLdpNgCepTdmFec128InLblSsrcId_Type = Unsigned32
_VLdpNgCepTdmFec128InLblSsrcId_Object = MibTableColumn
vLdpNgCepTdmFec128InLblSsrcId = _VLdpNgCepTdmFec128InLblSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 29, 1, 9),
    _VLdpNgCepTdmFec128InLblSsrcId_Type()
)
vLdpNgCepTdmFec128InLblSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128InLblSsrcId.setStatus("current")
_VLdpNgCepTdmFec128OutLblTable_Object = MibTable
vLdpNgCepTdmFec128OutLblTable = _VLdpNgCepTdmFec128OutLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30)
)
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblTable.setStatus("current")
_VLdpNgCepTdmFec128OutLblEntry_Object = MibTableRow
vLdpNgCepTdmFec128OutLblEntry = _VLdpNgCepTdmFec128OutLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1)
)
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblEntry.setStatus("current")
_VLdpNgCepTdmFec128OutLblPyldSze_Type = Unsigned32
_VLdpNgCepTdmFec128OutLblPyldSze_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblPyldSze = _VLdpNgCepTdmFec128OutLblPyldSze_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 1),
    _VLdpNgCepTdmFec128OutLblPyldSze_Type()
)
vLdpNgCepTdmFec128OutLblPyldSze.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblPyldSze.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblPyldSze.setUnits("bytes")
_VLdpNgCepTdmFec128OutLblBitrate_Type = Unsigned32
_VLdpNgCepTdmFec128OutLblBitrate_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblBitrate = _VLdpNgCepTdmFec128OutLblBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 2),
    _VLdpNgCepTdmFec128OutLblBitrate_Type()
)
vLdpNgCepTdmFec128OutLblBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblBitrate.setUnits("64 Kbits/s")
_VLdpNgCepTdmFec128OutLblRtpHdr_Type = TruthValue
_VLdpNgCepTdmFec128OutLblRtpHdr_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblRtpHdr = _VLdpNgCepTdmFec128OutLblRtpHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 3),
    _VLdpNgCepTdmFec128OutLblRtpHdr_Type()
)
vLdpNgCepTdmFec128OutLblRtpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblRtpHdr.setStatus("current")
_VLdpNgCepTdmFec128OutLblDfTstmp_Type = TruthValue
_VLdpNgCepTdmFec128OutLblDfTstmp_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblDfTstmp = _VLdpNgCepTdmFec128OutLblDfTstmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 4),
    _VLdpNgCepTdmFec128OutLblDfTstmp_Type()
)
vLdpNgCepTdmFec128OutLblDfTstmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblDfTstmp.setStatus("current")
_VLdpNgCepTdmFec128OutLblSigPkts_Type = TdmOptionsSigPkts
_VLdpNgCepTdmFec128OutLblSigPkts_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblSigPkts = _VLdpNgCepTdmFec128OutLblSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 5),
    _VLdpNgCepTdmFec128OutLblSigPkts_Type()
)
vLdpNgCepTdmFec128OutLblSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblSigPkts.setStatus("current")
_VLdpNgCepTdmFec128OutLblCasTrnk_Type = TdmOptionsCasTrunkFraming
_VLdpNgCepTdmFec128OutLblCasTrnk_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblCasTrnk = _VLdpNgCepTdmFec128OutLblCasTrnk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 6),
    _VLdpNgCepTdmFec128OutLblCasTrnk_Type()
)
vLdpNgCepTdmFec128OutLblCasTrnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblCasTrnk.setStatus("current")
_VLdpNgCepTdmFec128OutLblTstmpFq_Type = Unsigned32
_VLdpNgCepTdmFec128OutLblTstmpFq_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblTstmpFq = _VLdpNgCepTdmFec128OutLblTstmpFq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 7),
    _VLdpNgCepTdmFec128OutLblTstmpFq_Type()
)
vLdpNgCepTdmFec128OutLblTstmpFq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblTstmpFq.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblTstmpFq.setUnits("8 KHz")
_VLdpNgCepTdmFec128OutLblPyldTyp_Type = Unsigned32
_VLdpNgCepTdmFec128OutLblPyldTyp_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblPyldTyp = _VLdpNgCepTdmFec128OutLblPyldTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 8),
    _VLdpNgCepTdmFec128OutLblPyldTyp_Type()
)
vLdpNgCepTdmFec128OutLblPyldTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblPyldTyp.setStatus("current")
_VLdpNgCepTdmFec128OutLblSsrcId_Type = Unsigned32
_VLdpNgCepTdmFec128OutLblSsrcId_Object = MibTableColumn
vLdpNgCepTdmFec128OutLblSsrcId = _VLdpNgCepTdmFec128OutLblSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 30, 1, 9),
    _VLdpNgCepTdmFec128OutLblSsrcId_Type()
)
vLdpNgCepTdmFec128OutLblSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec128OutLblSsrcId.setStatus("current")
_VLdpNgCepTdmFec129InLblTable_Object = MibTable
vLdpNgCepTdmFec129InLblTable = _VLdpNgCepTdmFec129InLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31)
)
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblTable.setStatus("current")
_VLdpNgCepTdmFec129InLblEntry_Object = MibTableRow
vLdpNgCepTdmFec129InLblEntry = _VLdpNgCepTdmFec129InLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1)
)
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblEntry.setStatus("current")
_VLdpNgCepTdmFec129InLblPayldSize_Type = Unsigned32
_VLdpNgCepTdmFec129InLblPayldSize_Object = MibTableColumn
vLdpNgCepTdmFec129InLblPayldSize = _VLdpNgCepTdmFec129InLblPayldSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 1),
    _VLdpNgCepTdmFec129InLblPayldSize_Type()
)
vLdpNgCepTdmFec129InLblPayldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblPayldSize.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblPayldSize.setUnits("bytes")
_VLdpNgCepTdmFec129InLblBitrate_Type = Unsigned32
_VLdpNgCepTdmFec129InLblBitrate_Object = MibTableColumn
vLdpNgCepTdmFec129InLblBitrate = _VLdpNgCepTdmFec129InLblBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 2),
    _VLdpNgCepTdmFec129InLblBitrate_Type()
)
vLdpNgCepTdmFec129InLblBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblBitrate.setUnits("64 Kbits/s")
_VLdpNgCepTdmFec129InLblRtpHeader_Type = TruthValue
_VLdpNgCepTdmFec129InLblRtpHeader_Object = MibTableColumn
vLdpNgCepTdmFec129InLblRtpHeader = _VLdpNgCepTdmFec129InLblRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 3),
    _VLdpNgCepTdmFec129InLblRtpHeader_Type()
)
vLdpNgCepTdmFec129InLblRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblRtpHeader.setStatus("current")
_VLdpNgCepTdmFec129InLblDiffTStmp_Type = TruthValue
_VLdpNgCepTdmFec129InLblDiffTStmp_Object = MibTableColumn
vLdpNgCepTdmFec129InLblDiffTStmp = _VLdpNgCepTdmFec129InLblDiffTStmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 4),
    _VLdpNgCepTdmFec129InLblDiffTStmp_Type()
)
vLdpNgCepTdmFec129InLblDiffTStmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblDiffTStmp.setStatus("current")
_VLdpNgCepTdmFec129InLblSigPkts_Type = TdmOptionsSigPkts
_VLdpNgCepTdmFec129InLblSigPkts_Object = MibTableColumn
vLdpNgCepTdmFec129InLblSigPkts = _VLdpNgCepTdmFec129InLblSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 5),
    _VLdpNgCepTdmFec129InLblSigPkts_Type()
)
vLdpNgCepTdmFec129InLblSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblSigPkts.setStatus("current")
_VLdpNgCepTdmFec129InLblCasTrunk_Type = TdmOptionsCasTrunkFraming
_VLdpNgCepTdmFec129InLblCasTrunk_Object = MibTableColumn
vLdpNgCepTdmFec129InLblCasTrunk = _VLdpNgCepTdmFec129InLblCasTrunk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 6),
    _VLdpNgCepTdmFec129InLblCasTrunk_Type()
)
vLdpNgCepTdmFec129InLblCasTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblCasTrunk.setStatus("current")
_VLdpNgCepTdmFec129InLblTStmpFreq_Type = Unsigned32
_VLdpNgCepTdmFec129InLblTStmpFreq_Object = MibTableColumn
vLdpNgCepTdmFec129InLblTStmpFreq = _VLdpNgCepTdmFec129InLblTStmpFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 7),
    _VLdpNgCepTdmFec129InLblTStmpFreq_Type()
)
vLdpNgCepTdmFec129InLblTStmpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblTStmpFreq.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblTStmpFreq.setUnits("8 KHz")
_VLdpNgCepTdmFec129InLblPayldType_Type = Unsigned32
_VLdpNgCepTdmFec129InLblPayldType_Object = MibTableColumn
vLdpNgCepTdmFec129InLblPayldType = _VLdpNgCepTdmFec129InLblPayldType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 8),
    _VLdpNgCepTdmFec129InLblPayldType_Type()
)
vLdpNgCepTdmFec129InLblPayldType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblPayldType.setStatus("current")
_VLdpNgCepTdmFec129InLblSsrcId_Type = Unsigned32
_VLdpNgCepTdmFec129InLblSsrcId_Object = MibTableColumn
vLdpNgCepTdmFec129InLblSsrcId = _VLdpNgCepTdmFec129InLblSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 31, 1, 9),
    _VLdpNgCepTdmFec129InLblSsrcId_Type()
)
vLdpNgCepTdmFec129InLblSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129InLblSsrcId.setStatus("current")
_VLdpNgCepTdmFec129OutLblTable_Object = MibTable
vLdpNgCepTdmFec129OutLblTable = _VLdpNgCepTdmFec129OutLblTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32)
)
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblTable.setStatus("current")
_VLdpNgCepTdmFec129OutLblEntry_Object = MibTableRow
vLdpNgCepTdmFec129OutLblEntry = _VLdpNgCepTdmFec129OutLblEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1)
)
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblEntry.setStatus("current")
_VLdpNgCepTdmFec129OutLblPyldSize_Type = Unsigned32
_VLdpNgCepTdmFec129OutLblPyldSize_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblPyldSize = _VLdpNgCepTdmFec129OutLblPyldSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 1),
    _VLdpNgCepTdmFec129OutLblPyldSize_Type()
)
vLdpNgCepTdmFec129OutLblPyldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblPyldSize.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblPyldSize.setUnits("bytes")
_VLdpNgCepTdmFec129OutLblBitrate_Type = Unsigned32
_VLdpNgCepTdmFec129OutLblBitrate_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblBitrate = _VLdpNgCepTdmFec129OutLblBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 2),
    _VLdpNgCepTdmFec129OutLblBitrate_Type()
)
vLdpNgCepTdmFec129OutLblBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblBitrate.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblBitrate.setUnits("64 Kbits/s")
_VLdpNgCepTdmFec129OutLblRtpHdr_Type = TruthValue
_VLdpNgCepTdmFec129OutLblRtpHdr_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblRtpHdr = _VLdpNgCepTdmFec129OutLblRtpHdr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 3),
    _VLdpNgCepTdmFec129OutLblRtpHdr_Type()
)
vLdpNgCepTdmFec129OutLblRtpHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblRtpHdr.setStatus("current")
_VLdpNgCepTdmFec129OutLblDifTStmp_Type = TruthValue
_VLdpNgCepTdmFec129OutLblDifTStmp_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblDifTStmp = _VLdpNgCepTdmFec129OutLblDifTStmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 4),
    _VLdpNgCepTdmFec129OutLblDifTStmp_Type()
)
vLdpNgCepTdmFec129OutLblDifTStmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblDifTStmp.setStatus("current")
_VLdpNgCepTdmFec129OutLblSigPkts_Type = TdmOptionsSigPkts
_VLdpNgCepTdmFec129OutLblSigPkts_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblSigPkts = _VLdpNgCepTdmFec129OutLblSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 5),
    _VLdpNgCepTdmFec129OutLblSigPkts_Type()
)
vLdpNgCepTdmFec129OutLblSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblSigPkts.setStatus("current")
_VLdpNgCepTdmFec129OutLblCasTrnk_Type = TdmOptionsCasTrunkFraming
_VLdpNgCepTdmFec129OutLblCasTrnk_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblCasTrnk = _VLdpNgCepTdmFec129OutLblCasTrnk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 6),
    _VLdpNgCepTdmFec129OutLblCasTrnk_Type()
)
vLdpNgCepTdmFec129OutLblCasTrnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblCasTrnk.setStatus("current")
_VLdpNgCepTdmFec129OutLblTStmpFrq_Type = Unsigned32
_VLdpNgCepTdmFec129OutLblTStmpFrq_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblTStmpFrq = _VLdpNgCepTdmFec129OutLblTStmpFrq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 7),
    _VLdpNgCepTdmFec129OutLblTStmpFrq_Type()
)
vLdpNgCepTdmFec129OutLblTStmpFrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblTStmpFrq.setStatus("current")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblTStmpFrq.setUnits("8 KHz")
_VLdpNgCepTdmFec129OutLblPyldType_Type = Unsigned32
_VLdpNgCepTdmFec129OutLblPyldType_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblPyldType = _VLdpNgCepTdmFec129OutLblPyldType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 8),
    _VLdpNgCepTdmFec129OutLblPyldType_Type()
)
vLdpNgCepTdmFec129OutLblPyldType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblPyldType.setStatus("current")
_VLdpNgCepTdmFec129OutLblSsrcId_Type = Unsigned32
_VLdpNgCepTdmFec129OutLblSsrcId_Object = MibTableColumn
vLdpNgCepTdmFec129OutLblSsrcId = _VLdpNgCepTdmFec129OutLblSsrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 32, 1, 9),
    _VLdpNgCepTdmFec129OutLblSsrcId_Type()
)
vLdpNgCepTdmFec129OutLblSsrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgCepTdmFec129OutLblSsrcId.setStatus("current")
_VRtrLdpNgStaticFecTableLstCh_Type = TimeStamp
_VRtrLdpNgStaticFecTableLstCh_Object = MibScalar
vRtrLdpNgStaticFecTableLstCh = _VRtrLdpNgStaticFecTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 33),
    _VRtrLdpNgStaticFecTableLstCh_Type()
)
vRtrLdpNgStaticFecTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecTableLstCh.setStatus("current")
_VRtrLdpNgStaticFecTable_Object = MibTable
vRtrLdpNgStaticFecTable = _VRtrLdpNgStaticFecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 34)
)
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecTable.setStatus("current")
_VRtrLdpNgStaticFecEntry_Object = MibTableRow
vRtrLdpNgStaticFecEntry = _VRtrLdpNgStaticFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 34, 1)
)
vRtrLdpNgStaticFecEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefixType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefix"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefixLen"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecEntry.setStatus("current")
_VRtrLdpNgStaticFecIpPrefixType_Type = InetAddressType
_VRtrLdpNgStaticFecIpPrefixType_Object = MibTableColumn
vRtrLdpNgStaticFecIpPrefixType = _VRtrLdpNgStaticFecIpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 34, 1, 1),
    _VRtrLdpNgStaticFecIpPrefixType_Type()
)
vRtrLdpNgStaticFecIpPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecIpPrefixType.setStatus("current")


class _VRtrLdpNgStaticFecIpPrefix_Type(InetAddress):
    """Custom type vRtrLdpNgStaticFecIpPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgStaticFecIpPrefix_Type.__name__ = "InetAddress"
_VRtrLdpNgStaticFecIpPrefix_Object = MibTableColumn
vRtrLdpNgStaticFecIpPrefix = _VRtrLdpNgStaticFecIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 34, 1, 2),
    _VRtrLdpNgStaticFecIpPrefix_Type()
)
vRtrLdpNgStaticFecIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecIpPrefix.setStatus("current")


class _VRtrLdpNgStaticFecIpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type vRtrLdpNgStaticFecIpPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VRtrLdpNgStaticFecIpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_VRtrLdpNgStaticFecIpPrefixLen_Object = MibTableColumn
vRtrLdpNgStaticFecIpPrefixLen = _VRtrLdpNgStaticFecIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 34, 1, 3),
    _VRtrLdpNgStaticFecIpPrefixLen_Type()
)
vRtrLdpNgStaticFecIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecIpPrefixLen.setStatus("current")
_VRtrLdpNgStaticFecRowStatus_Type = RowStatus
_VRtrLdpNgStaticFecRowStatus_Object = MibTableColumn
vRtrLdpNgStaticFecRowStatus = _VRtrLdpNgStaticFecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 34, 1, 4),
    _VRtrLdpNgStaticFecRowStatus_Type()
)
vRtrLdpNgStaticFecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecRowStatus.setStatus("current")
_VRtrLdpNgStaticFecNumInLabel_Type = Unsigned32
_VRtrLdpNgStaticFecNumInLabel_Object = MibTableColumn
vRtrLdpNgStaticFecNumInLabel = _VRtrLdpNgStaticFecNumInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 34, 1, 5),
    _VRtrLdpNgStaticFecNumInLabel_Type()
)
vRtrLdpNgStaticFecNumInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecNumInLabel.setStatus("current")
_VRtrLdpNgStaticFecNumOutLabel_Type = Unsigned32
_VRtrLdpNgStaticFecNumOutLabel_Object = MibTableColumn
vRtrLdpNgStaticFecNumOutLabel = _VRtrLdpNgStaticFecNumOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 34, 1, 6),
    _VRtrLdpNgStaticFecNumOutLabel_Type()
)
vRtrLdpNgStaticFecNumOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecNumOutLabel.setStatus("current")
_VRtrLdpNgStaticFecInLabelTable_Object = MibTable
vRtrLdpNgStaticFecInLabelTable = _VRtrLdpNgStaticFecInLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 35)
)
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecInLabelTable.setStatus("current")
_VRtrLdpNgStaticFecInLabelEntry_Object = MibTableRow
vRtrLdpNgStaticFecInLabelEntry = _VRtrLdpNgStaticFecInLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 35, 1)
)
vRtrLdpNgStaticFecInLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefixType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefix"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefixLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecInLabel"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecInLabelEntry.setStatus("current")


class _VRtrLdpNgSFecInLabel_Type(Unsigned32):
    """Custom type vRtrLdpNgSFecInLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 262112),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrLdpNgSFecInLabel_Type.__name__ = "Unsigned32"
_VRtrLdpNgSFecInLabel_Object = MibTableColumn
vRtrLdpNgSFecInLabel = _VRtrLdpNgSFecInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 35, 1, 1),
    _VRtrLdpNgSFecInLabel_Type()
)
vRtrLdpNgSFecInLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecInLabel.setStatus("current")
_VRtrLdpNgSFecInLabelRowStatus_Type = RowStatus
_VRtrLdpNgSFecInLabelRowStatus_Object = MibTableColumn
vRtrLdpNgSFecInLabelRowStatus = _VRtrLdpNgSFecInLabelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 35, 1, 2),
    _VRtrLdpNgSFecInLabelRowStatus_Type()
)
vRtrLdpNgSFecInLabelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecInLabelRowStatus.setStatus("current")
_VRtrLdpNgSFecOperInLabel_Type = Unsigned32
_VRtrLdpNgSFecOperInLabel_Object = MibTableColumn
vRtrLdpNgSFecOperInLabel = _VRtrLdpNgSFecOperInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 35, 1, 3),
    _VRtrLdpNgSFecOperInLabel_Type()
)
vRtrLdpNgSFecOperInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecOperInLabel.setStatus("current")
_VRtrLdpNgStaticFecOutLabelTable_Object = MibTable
vRtrLdpNgStaticFecOutLabelTable = _VRtrLdpNgStaticFecOutLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 36)
)
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecOutLabelTable.setStatus("current")
_VRtrLdpNgStaticFecOutLabelEntry_Object = MibTableRow
vRtrLdpNgStaticFecOutLabelEntry = _VRtrLdpNgStaticFecOutLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 36, 1)
)
vRtrLdpNgStaticFecOutLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefixType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefix"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecIpPrefixLen"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecOutLabelType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecOutLabelIfName"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecOutLabelIpAddrType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecOutLabelIpAddr"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgStaticFecOutLabelEntry.setStatus("current")


class _VRtrLdpNgSFecOutLabelType_Type(Integer32):
    """Custom type vRtrLdpNgSFecOutLabelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("pop", 1),
          ("push", 2),
          ("swap", 3))
    )


_VRtrLdpNgSFecOutLabelType_Type.__name__ = "Integer32"
_VRtrLdpNgSFecOutLabelType_Object = MibTableColumn
vRtrLdpNgSFecOutLabelType = _VRtrLdpNgSFecOutLabelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 36, 1, 1),
    _VRtrLdpNgSFecOutLabelType_Type()
)
vRtrLdpNgSFecOutLabelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecOutLabelType.setStatus("current")


class _VRtrLdpNgSFecOutLabelIfName_Type(DisplayString):
    """Custom type vRtrLdpNgSFecOutLabelIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrLdpNgSFecOutLabelIfName_Type.__name__ = "DisplayString"
_VRtrLdpNgSFecOutLabelIfName_Object = MibTableColumn
vRtrLdpNgSFecOutLabelIfName = _VRtrLdpNgSFecOutLabelIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 36, 1, 2),
    _VRtrLdpNgSFecOutLabelIfName_Type()
)
vRtrLdpNgSFecOutLabelIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecOutLabelIfName.setStatus("current")
_VRtrLdpNgSFecOutLabelIpAddrType_Type = InetAddressType
_VRtrLdpNgSFecOutLabelIpAddrType_Object = MibTableColumn
vRtrLdpNgSFecOutLabelIpAddrType = _VRtrLdpNgSFecOutLabelIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 36, 1, 3),
    _VRtrLdpNgSFecOutLabelIpAddrType_Type()
)
vRtrLdpNgSFecOutLabelIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecOutLabelIpAddrType.setStatus("current")


class _VRtrLdpNgSFecOutLabelIpAddr_Type(InetAddress):
    """Custom type vRtrLdpNgSFecOutLabelIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgSFecOutLabelIpAddr_Type.__name__ = "InetAddress"
_VRtrLdpNgSFecOutLabelIpAddr_Object = MibTableColumn
vRtrLdpNgSFecOutLabelIpAddr = _VRtrLdpNgSFecOutLabelIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 36, 1, 4),
    _VRtrLdpNgSFecOutLabelIpAddr_Type()
)
vRtrLdpNgSFecOutLabelIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecOutLabelIpAddr.setStatus("current")
_VRtrLdpNgSFecOutLabelRowStatus_Type = RowStatus
_VRtrLdpNgSFecOutLabelRowStatus_Object = MibTableColumn
vRtrLdpNgSFecOutLabelRowStatus = _VRtrLdpNgSFecOutLabelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 36, 1, 5),
    _VRtrLdpNgSFecOutLabelRowStatus_Type()
)
vRtrLdpNgSFecOutLabelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecOutLabelRowStatus.setStatus("current")


class _VRtrLdpNgSFecOutLabel_Type(Unsigned32):
    """Custom type vRtrLdpNgSFecOutLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrLdpNgSFecOutLabel_Type.__name__ = "Unsigned32"
_VRtrLdpNgSFecOutLabel_Object = MibTableColumn
vRtrLdpNgSFecOutLabel = _VRtrLdpNgSFecOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 36, 1, 6),
    _VRtrLdpNgSFecOutLabel_Type()
)
vRtrLdpNgSFecOutLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgSFecOutLabel.setStatus("current")
_VRtrLdpNgTargPeerTableLstCh_Type = TimeStamp
_VRtrLdpNgTargPeerTableLstCh_Object = MibScalar
vRtrLdpNgTargPeerTableLstCh = _VRtrLdpNgTargPeerTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 37),
    _VRtrLdpNgTargPeerTableLstCh_Type()
)
vRtrLdpNgTargPeerTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerTableLstCh.setStatus("current")
_VRtrLdpNgTargPeerTable_Object = MibTable
vRtrLdpNgTargPeerTable = _VRtrLdpNgTargPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38)
)
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerTable.setStatus("current")
_VRtrLdpNgTargPeerEntry_Object = MibTableRow
vRtrLdpNgTargPeerEntry = _VRtrLdpNgTargPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1)
)
vRtrLdpNgTargPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddressType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgPeerAddress"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerEntry.setStatus("current")
_VRtrLdpNgPeerAddressType_Type = InetAddressType
_VRtrLdpNgPeerAddressType_Object = MibTableColumn
vRtrLdpNgPeerAddressType = _VRtrLdpNgPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 1),
    _VRtrLdpNgPeerAddressType_Type()
)
vRtrLdpNgPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgPeerAddressType.setStatus("current")


class _VRtrLdpNgPeerAddress_Type(InetAddress):
    """Custom type vRtrLdpNgPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgPeerAddress_Type.__name__ = "InetAddress"
_VRtrLdpNgPeerAddress_Object = MibTableColumn
vRtrLdpNgPeerAddress = _VRtrLdpNgPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 2),
    _VRtrLdpNgPeerAddress_Type()
)
vRtrLdpNgPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgPeerAddress.setStatus("current")
_VRtrLdpNgTargPeerRowStatus_Type = RowStatus
_VRtrLdpNgTargPeerRowStatus_Object = MibTableColumn
vRtrLdpNgTargPeerRowStatus = _VRtrLdpNgTargPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 3),
    _VRtrLdpNgTargPeerRowStatus_Type()
)
vRtrLdpNgTargPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerRowStatus.setStatus("current")
_VRtrLdpNgTargPeerLastChange_Type = TimeStamp
_VRtrLdpNgTargPeerLastChange_Object = MibTableColumn
vRtrLdpNgTargPeerLastChange = _VRtrLdpNgTargPeerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 4),
    _VRtrLdpNgTargPeerLastChange_Type()
)
vRtrLdpNgTargPeerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerLastChange.setStatus("current")


class _VRtrLdpNgTargPeerAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpNgTargPeerAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrLdpNgTargPeerAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpNgTargPeerAdminState_Object = MibTableColumn
vRtrLdpNgTargPeerAdminState = _VRtrLdpNgTargPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 5),
    _VRtrLdpNgTargPeerAdminState_Type()
)
vRtrLdpNgTargPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerAdminState.setStatus("current")
_VRtrLdpNgTargPeerOperState_Type = TmnxOperState
_VRtrLdpNgTargPeerOperState_Object = MibTableColumn
vRtrLdpNgTargPeerOperState = _VRtrLdpNgTargPeerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 6),
    _VRtrLdpNgTargPeerOperState_Type()
)
vRtrLdpNgTargPeerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerOperState.setStatus("current")
_VRtrLdpNgTargPeerUpTime_Type = TimeInterval
_VRtrLdpNgTargPeerUpTime_Object = MibTableColumn
vRtrLdpNgTargPeerUpTime = _VRtrLdpNgTargPeerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 7),
    _VRtrLdpNgTargPeerUpTime_Type()
)
vRtrLdpNgTargPeerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerUpTime.setStatus("current")
_VRtrLdpNgTargPeerOperDownReason_Type = TmnxLdpIntTargOperDownReasonCode
_VRtrLdpNgTargPeerOperDownReason_Object = MibTableColumn
vRtrLdpNgTargPeerOperDownReason = _VRtrLdpNgTargPeerOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 8),
    _VRtrLdpNgTargPeerOperDownReason_Type()
)
vRtrLdpNgTargPeerOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerOperDownReason.setStatus("current")


class _VRtrLdpNgTargPeerInheritance_Type(Unsigned32):
    """Custom type vRtrLdpNgTargPeerInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrLdpNgTargPeerInheritance_Type.__name__ = "Unsigned32"
_VRtrLdpNgTargPeerInheritance_Object = MibTableColumn
vRtrLdpNgTargPeerInheritance = _VRtrLdpNgTargPeerInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 9),
    _VRtrLdpNgTargPeerInheritance_Type()
)
vRtrLdpNgTargPeerInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerInheritance.setStatus("current")


class _VRtrLdpNgTargPeerKAFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpNgTargPeerKAFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 4


_VRtrLdpNgTargPeerKAFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpNgTargPeerKAFactor_Object = MibTableColumn
vRtrLdpNgTargPeerKAFactor = _VRtrLdpNgTargPeerKAFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 10),
    _VRtrLdpNgTargPeerKAFactor_Type()
)
vRtrLdpNgTargPeerKAFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerKAFactor.setStatus("current")


class _VRtrLdpNgTargPeerKATimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpNgTargPeerKATimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 40


_VRtrLdpNgTargPeerKATimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpNgTargPeerKATimeout_Object = MibTableColumn
vRtrLdpNgTargPeerKATimeout = _VRtrLdpNgTargPeerKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 11),
    _VRtrLdpNgTargPeerKATimeout_Type()
)
vRtrLdpNgTargPeerKATimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerKATimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerKATimeout.setUnits("seconds")


class _VRtrLdpNgTargPeerHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpNgTargPeerHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpNgTargPeerHelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpNgTargPeerHelloFactor_Object = MibTableColumn
vRtrLdpNgTargPeerHelloFactor = _VRtrLdpNgTargPeerHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 12),
    _VRtrLdpNgTargPeerHelloFactor_Type()
)
vRtrLdpNgTargPeerHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerHelloFactor.setStatus("current")


class _VRtrLdpNgTargPeerHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpNgTargPeerHelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 45


_VRtrLdpNgTargPeerHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpNgTargPeerHelloTimeout_Object = MibTableColumn
vRtrLdpNgTargPeerHelloTimeout = _VRtrLdpNgTargPeerHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 13),
    _VRtrLdpNgTargPeerHelloTimeout_Type()
)
vRtrLdpNgTargPeerHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerHelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerHelloTimeout.setUnits("seconds")


class _VRtrLdpNgTargPeerOprHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpNgTargPeerOprHelloTimeout based on TmnxLdpNewHelloTimeout"""
    subtypeSpec = TmnxLdpNewHelloTimeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_VRtrLdpNgTargPeerOprHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpNgTargPeerOprHelloTimeout_Object = MibTableColumn
vRtrLdpNgTargPeerOprHelloTimeout = _VRtrLdpNgTargPeerOprHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 14),
    _VRtrLdpNgTargPeerOprHelloTimeout_Type()
)
vRtrLdpNgTargPeerOprHelloTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerOprHelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerOprHelloTimeout.setUnits("seconds")


class _VRtrLdpNgTargPeerHelloReduction_Type(TruthValue):
    """Custom type vRtrLdpNgTargPeerHelloReduction based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgTargPeerHelloReduction_Type.__name__ = "TruthValue"
_VRtrLdpNgTargPeerHelloReduction_Object = MibTableColumn
vRtrLdpNgTargPeerHelloReduction = _VRtrLdpNgTargPeerHelloReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 15),
    _VRtrLdpNgTargPeerHelloReduction_Type()
)
vRtrLdpNgTargPeerHelloReduction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerHelloReduction.setStatus("current")


class _VRtrLdpNgTargPeerHelloRdctnFctr_Type(Unsigned32):
    """Custom type vRtrLdpNgTargPeerHelloRdctnFctr based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_VRtrLdpNgTargPeerHelloRdctnFctr_Type.__name__ = "Unsigned32"
_VRtrLdpNgTargPeerHelloRdctnFctr_Object = MibTableColumn
vRtrLdpNgTargPeerHelloRdctnFctr = _VRtrLdpNgTargPeerHelloRdctnFctr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 16),
    _VRtrLdpNgTargPeerHelloRdctnFctr_Type()
)
vRtrLdpNgTargPeerHelloRdctnFctr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerHelloRdctnFctr.setStatus("current")


class _VRtrLdpNgTargPeerBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpNgTargPeerBackoffTime based on TmnxLdpBackoffTime"""
    subtypeSpec = TmnxLdpBackoffTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpNgTargPeerBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpNgTargPeerBackoffTime_Object = MibTableColumn
vRtrLdpNgTargPeerBackoffTime = _VRtrLdpNgTargPeerBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 17),
    _VRtrLdpNgTargPeerBackoffTime_Type()
)
vRtrLdpNgTargPeerBackoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerBackoffTime.setUnits("seconds")
_VRtrLdpNgTargPeerMaxBackoffTime_Type = TmnxLdpBackoffTime
_VRtrLdpNgTargPeerMaxBackoffTime_Object = MibTableColumn
vRtrLdpNgTargPeerMaxBackoffTime = _VRtrLdpNgTargPeerMaxBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 18),
    _VRtrLdpNgTargPeerMaxBackoffTime_Type()
)
vRtrLdpNgTargPeerMaxBackoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerMaxBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerMaxBackoffTime.setUnits("seconds")


class _VRtrLdpNgTargPeerTunneling_Type(TruthValue):
    """Custom type vRtrLdpNgTargPeerTunneling based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgTargPeerTunneling_Type.__name__ = "TruthValue"
_VRtrLdpNgTargPeerTunneling_Object = MibTableColumn
vRtrLdpNgTargPeerTunneling = _VRtrLdpNgTargPeerTunneling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 19),
    _VRtrLdpNgTargPeerTunneling_Type()
)
vRtrLdpNgTargPeerTunneling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerTunneling.setStatus("current")


class _VRtrLdpNgTargPeerBfdEnabled_Type(TruthValue):
    """Custom type vRtrLdpNgTargPeerBfdEnabled based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgTargPeerBfdEnabled_Type.__name__ = "TruthValue"
_VRtrLdpNgTargPeerBfdEnabled_Object = MibTableColumn
vRtrLdpNgTargPeerBfdEnabled = _VRtrLdpNgTargPeerBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 20),
    _VRtrLdpNgTargPeerBfdEnabled_Type()
)
vRtrLdpNgTargPeerBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerBfdEnabled.setStatus("current")


class _VRtrLdpNgTargPeerLsrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type vRtrLdpNgTargPeerLsrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrLdpNgTargPeerLsrIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_VRtrLdpNgTargPeerLsrIfIndex_Object = MibTableColumn
vRtrLdpNgTargPeerLsrIfIndex = _VRtrLdpNgTargPeerLsrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 21),
    _VRtrLdpNgTargPeerLsrIfIndex_Type()
)
vRtrLdpNgTargPeerLsrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerLsrIfIndex.setStatus("current")
_VRtrLdpNgTargPeerAutoCreate_Type = TruthValue
_VRtrLdpNgTargPeerAutoCreate_Object = MibTableColumn
vRtrLdpNgTargPeerAutoCreate = _VRtrLdpNgTargPeerAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 22),
    _VRtrLdpNgTargPeerAutoCreate_Type()
)
vRtrLdpNgTargPeerAutoCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerAutoCreate.setStatus("current")


class _VRtrLdpNgTargPeerCreator_Type(Integer32):
    """Custom type vRtrLdpNgTargPeerCreator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("template", 2),
          ("sdp", 3))
    )


_VRtrLdpNgTargPeerCreator_Type.__name__ = "Integer32"
_VRtrLdpNgTargPeerCreator_Object = MibTableColumn
vRtrLdpNgTargPeerCreator = _VRtrLdpNgTargPeerCreator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 23),
    _VRtrLdpNgTargPeerCreator_Type()
)
vRtrLdpNgTargPeerCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerCreator.setStatus("current")
_VRtrLdpNgTargPeerTemplName_Type = TNamedItemOrEmpty
_VRtrLdpNgTargPeerTemplName_Object = MibTableColumn
vRtrLdpNgTargPeerTemplName = _VRtrLdpNgTargPeerTemplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 38, 1, 24),
    _VRtrLdpNgTargPeerTemplName_Type()
)
vRtrLdpNgTargPeerTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerTemplName.setStatus("current")
_VRtrLdpNgTargPeerStatsTable_Object = MibTable
vRtrLdpNgTargPeerStatsTable = _VRtrLdpNgTargPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 39)
)
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerStatsTable.setStatus("current")
_VRtrLdpNgTargPeerStatsEntry_Object = MibTableRow
vRtrLdpNgTargPeerStatsEntry = _VRtrLdpNgTargPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 39, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerStatsEntry.setStatus("current")
_VRtrLdpNgTargPeerStatExistingAdj_Type = Gauge32
_VRtrLdpNgTargPeerStatExistingAdj_Object = MibTableColumn
vRtrLdpNgTargPeerStatExistingAdj = _VRtrLdpNgTargPeerStatExistingAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 39, 1, 1),
    _VRtrLdpNgTargPeerStatExistingAdj_Type()
)
vRtrLdpNgTargPeerStatExistingAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargPeerStatExistingAdj.setStatus("current")
_VRtrLdpNgInetIfTableLstCh_Type = TimeStamp
_VRtrLdpNgInetIfTableLstCh_Object = MibScalar
vRtrLdpNgInetIfTableLstCh = _VRtrLdpNgInetIfTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 40),
    _VRtrLdpNgInetIfTableLstCh_Type()
)
vRtrLdpNgInetIfTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfTableLstCh.setStatus("current")
_VRtrLdpNgInetIfTable_Object = MibTable
vRtrLdpNgInetIfTable = _VRtrLdpNgInetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41)
)
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfTable.setStatus("current")
_VRtrLdpNgInetIfEntry_Object = MibTableRow
vRtrLdpNgInetIfEntry = _VRtrLdpNgInetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1)
)
vRtrLdpNgInetIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfIndex"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfAddrType"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfEntry.setStatus("current")
_VRtrLdpNgIfAddrType_Type = InetAddressType
_VRtrLdpNgIfAddrType_Object = MibTableColumn
vRtrLdpNgIfAddrType = _VRtrLdpNgIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 1),
    _VRtrLdpNgIfAddrType_Type()
)
vRtrLdpNgIfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgIfAddrType.setStatus("current")
_VRtrLdpNgInetIfRowStatus_Type = RowStatus
_VRtrLdpNgInetIfRowStatus_Object = MibTableColumn
vRtrLdpNgInetIfRowStatus = _VRtrLdpNgInetIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 2),
    _VRtrLdpNgInetIfRowStatus_Type()
)
vRtrLdpNgInetIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfRowStatus.setStatus("current")
_VRtrLdpNgInetIfUpTime_Type = TimeInterval
_VRtrLdpNgInetIfUpTime_Object = MibTableColumn
vRtrLdpNgInetIfUpTime = _VRtrLdpNgInetIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 3),
    _VRtrLdpNgInetIfUpTime_Type()
)
vRtrLdpNgInetIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfUpTime.setStatus("current")
_VRtrLdpNgInetIfLastChange_Type = TimeStamp
_VRtrLdpNgInetIfLastChange_Object = MibTableColumn
vRtrLdpNgInetIfLastChange = _VRtrLdpNgInetIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 4),
    _VRtrLdpNgInetIfLastChange_Type()
)
vRtrLdpNgInetIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfLastChange.setStatus("current")


class _VRtrLdpNgInetIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpNgInetIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrLdpNgInetIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpNgInetIfAdminState_Object = MibTableColumn
vRtrLdpNgInetIfAdminState = _VRtrLdpNgInetIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 5),
    _VRtrLdpNgInetIfAdminState_Type()
)
vRtrLdpNgInetIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfAdminState.setStatus("current")
_VRtrLdpNgInetIfOperState_Type = TmnxOperState
_VRtrLdpNgInetIfOperState_Object = MibTableColumn
vRtrLdpNgInetIfOperState = _VRtrLdpNgInetIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 6),
    _VRtrLdpNgInetIfOperState_Type()
)
vRtrLdpNgInetIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfOperState.setStatus("current")
_VRtrLdpNgInetIfOperDownReason_Type = TmnxLdpIntTargOperDownReasonCode
_VRtrLdpNgInetIfOperDownReason_Object = MibTableColumn
vRtrLdpNgInetIfOperDownReason = _VRtrLdpNgInetIfOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 7),
    _VRtrLdpNgInetIfOperDownReason_Type()
)
vRtrLdpNgInetIfOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfOperDownReason.setStatus("current")


class _VRtrLdpNgInetIfInheritance_Type(Integer32):
    """Custom type vRtrLdpNgInetIfInheritance based on Integer32"""
    defaultValue = 0


_VRtrLdpNgInetIfInheritance_Type.__name__ = "Integer32"
_VRtrLdpNgInetIfInheritance_Object = MibTableColumn
vRtrLdpNgInetIfInheritance = _VRtrLdpNgInetIfInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 8),
    _VRtrLdpNgInetIfInheritance_Type()
)
vRtrLdpNgInetIfInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfInheritance.setStatus("current")


class _VRtrLdpNgInetIfKAFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpNgInetIfKAFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 3


_VRtrLdpNgInetIfKAFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpNgInetIfKAFactor_Object = MibTableColumn
vRtrLdpNgInetIfKAFactor = _VRtrLdpNgInetIfKAFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 9),
    _VRtrLdpNgInetIfKAFactor_Type()
)
vRtrLdpNgInetIfKAFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfKAFactor.setStatus("current")


class _VRtrLdpNgInetIfKATimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpNgInetIfKATimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 30


_VRtrLdpNgInetIfKATimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpNgInetIfKATimeout_Object = MibTableColumn
vRtrLdpNgInetIfKATimeout = _VRtrLdpNgInetIfKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 10),
    _VRtrLdpNgInetIfKATimeout_Type()
)
vRtrLdpNgInetIfKATimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfKATimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfKATimeout.setUnits("seconds")


class _VRtrLdpNgInetIfHelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpNgInetIfHelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpNgInetIfHelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpNgInetIfHelloFactor_Object = MibTableColumn
vRtrLdpNgInetIfHelloFactor = _VRtrLdpNgInetIfHelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 11),
    _VRtrLdpNgInetIfHelloFactor_Type()
)
vRtrLdpNgInetIfHelloFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfHelloFactor.setStatus("current")


class _VRtrLdpNgInetIfHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpNgInetIfHelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 15


_VRtrLdpNgInetIfHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpNgInetIfHelloTimeout_Object = MibTableColumn
vRtrLdpNgInetIfHelloTimeout = _VRtrLdpNgInetIfHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 12),
    _VRtrLdpNgInetIfHelloTimeout_Type()
)
vRtrLdpNgInetIfHelloTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfHelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfHelloTimeout.setUnits("seconds")


class _VRtrLdpNgInetIfOperHelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpNgInetIfOperHelloTimeout based on TmnxLdpNewHelloTimeout"""
    subtypeSpec = TmnxLdpNewHelloTimeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_VRtrLdpNgInetIfOperHelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpNgInetIfOperHelloTimeout_Object = MibTableColumn
vRtrLdpNgInetIfOperHelloTimeout = _VRtrLdpNgInetIfOperHelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 13),
    _VRtrLdpNgInetIfOperHelloTimeout_Type()
)
vRtrLdpNgInetIfOperHelloTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfOperHelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfOperHelloTimeout.setUnits("seconds")


class _VRtrLdpNgInetIfBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpNgInetIfBackoffTime based on TmnxLdpBackoffTime"""
    subtypeSpec = TmnxLdpBackoffTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpNgInetIfBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpNgInetIfBackoffTime_Object = MibTableColumn
vRtrLdpNgInetIfBackoffTime = _VRtrLdpNgInetIfBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 14),
    _VRtrLdpNgInetIfBackoffTime_Type()
)
vRtrLdpNgInetIfBackoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfBackoffTime.setUnits("seconds")
_VRtrLdpNgInetIfMaxBackoffTime_Type = TmnxLdpBackoffTime
_VRtrLdpNgInetIfMaxBackoffTime_Object = MibTableColumn
vRtrLdpNgInetIfMaxBackoffTime = _VRtrLdpNgInetIfMaxBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 15),
    _VRtrLdpNgInetIfMaxBackoffTime_Type()
)
vRtrLdpNgInetIfMaxBackoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfMaxBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfMaxBackoffTime.setUnits("seconds")


class _VRtrLdpNgInetIfTransAddrType_Type(Integer32):
    """Custom type vRtrLdpNgInetIfTransAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("system", 2))
    )


_VRtrLdpNgInetIfTransAddrType_Type.__name__ = "Integer32"
_VRtrLdpNgInetIfTransAddrType_Object = MibTableColumn
vRtrLdpNgInetIfTransAddrType = _VRtrLdpNgInetIfTransAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 16),
    _VRtrLdpNgInetIfTransAddrType_Type()
)
vRtrLdpNgInetIfTransAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfTransAddrType.setStatus("current")


class _VRtrLdpNgInetIfLsrIfType_Type(Integer32):
    """Custom type vRtrLdpNgInetIfLsrIfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("interface", 2))
    )


_VRtrLdpNgInetIfLsrIfType_Type.__name__ = "Integer32"
_VRtrLdpNgInetIfLsrIfType_Object = MibTableColumn
vRtrLdpNgInetIfLsrIfType = _VRtrLdpNgInetIfLsrIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 17),
    _VRtrLdpNgInetIfLsrIfType_Type()
)
vRtrLdpNgInetIfLsrIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfLsrIfType.setStatus("current")


class _VRtrLdpNgInetIfLsrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type vRtrLdpNgInetIfLsrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrLdpNgInetIfLsrIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_VRtrLdpNgInetIfLsrIfIndex_Object = MibTableColumn
vRtrLdpNgInetIfLsrIfIndex = _VRtrLdpNgInetIfLsrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 18),
    _VRtrLdpNgInetIfLsrIfIndex_Type()
)
vRtrLdpNgInetIfLsrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfLsrIfIndex.setStatus("current")


class _VRtrLdpNgInetIfIPv4P2MPFecCap_Type(TmnxEnabledDisabled):
    """Custom type vRtrLdpNgInetIfIPv4P2MPFecCap based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrLdpNgInetIfIPv4P2MPFecCap_Type.__name__ = "TmnxEnabledDisabled"
_VRtrLdpNgInetIfIPv4P2MPFecCap_Object = MibTableColumn
vRtrLdpNgInetIfIPv4P2MPFecCap = _VRtrLdpNgInetIfIPv4P2MPFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 19),
    _VRtrLdpNgInetIfIPv4P2MPFecCap_Type()
)
vRtrLdpNgInetIfIPv4P2MPFecCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfIPv4P2MPFecCap.setStatus("current")


class _VRtrLdpNgInetIfIPv6P2MPFecCap_Type(TmnxEnabledDisabled):
    """Custom type vRtrLdpNgInetIfIPv6P2MPFecCap based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrLdpNgInetIfIPv6P2MPFecCap_Type.__name__ = "TmnxEnabledDisabled"
_VRtrLdpNgInetIfIPv6P2MPFecCap_Object = MibTableColumn
vRtrLdpNgInetIfIPv6P2MPFecCap = _VRtrLdpNgInetIfIPv6P2MPFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 20),
    _VRtrLdpNgInetIfIPv6P2MPFecCap_Type()
)
vRtrLdpNgInetIfIPv6P2MPFecCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfIPv6P2MPFecCap.setStatus("current")


class _VRtrLdpNgInetIfIPv4PfxFecCap_Type(TmnxEnabledDisabled):
    """Custom type vRtrLdpNgInetIfIPv4PfxFecCap based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrLdpNgInetIfIPv4PfxFecCap_Type.__name__ = "TmnxEnabledDisabled"
_VRtrLdpNgInetIfIPv4PfxFecCap_Object = MibTableColumn
vRtrLdpNgInetIfIPv4PfxFecCap = _VRtrLdpNgInetIfIPv4PfxFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 21),
    _VRtrLdpNgInetIfIPv4PfxFecCap_Type()
)
vRtrLdpNgInetIfIPv4PfxFecCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfIPv4PfxFecCap.setStatus("current")


class _VRtrLdpNgInetIfIPv6PfxFecCap_Type(TmnxEnabledDisabled):
    """Custom type vRtrLdpNgInetIfIPv6PfxFecCap based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrLdpNgInetIfIPv6PfxFecCap_Type.__name__ = "TmnxEnabledDisabled"
_VRtrLdpNgInetIfIPv6PfxFecCap_Object = MibTableColumn
vRtrLdpNgInetIfIPv6PfxFecCap = _VRtrLdpNgInetIfIPv6PfxFecCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 41, 1, 22),
    _VRtrLdpNgInetIfIPv6PfxFecCap_Type()
)
vRtrLdpNgInetIfIPv6PfxFecCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgInetIfIPv6PfxFecCap.setStatus("current")
_VLdpNgStatsTable_Object = MibTable
vLdpNgStatsTable = _VLdpNgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42)
)
if mibBuilder.loadTexts:
    vLdpNgStatsTable.setStatus("current")
_VLdpNgStatsEntry_Object = MibTableRow
vLdpNgStatsEntry = _VLdpNgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1)
)
if mibBuilder.loadTexts:
    vLdpNgStatsEntry.setStatus("current")
_VLdpNgStatsOperDownEvents_Type = Counter32
_VLdpNgStatsOperDownEvents_Object = MibTableColumn
vLdpNgStatsOperDownEvents = _VLdpNgStatsOperDownEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 1),
    _VLdpNgStatsOperDownEvents_Type()
)
vLdpNgStatsOperDownEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsOperDownEvents.setStatus("current")
_VLdpNgStatsIPv4ActiveSess_Type = Gauge32
_VLdpNgStatsIPv4ActiveSess_Object = MibTableColumn
vLdpNgStatsIPv4ActiveSess = _VLdpNgStatsIPv4ActiveSess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 2),
    _VLdpNgStatsIPv4ActiveSess_Type()
)
vLdpNgStatsIPv4ActiveSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4ActiveSess.setStatus("current")
_VLdpNgStatsIPv6ActiveSess_Type = Gauge32
_VLdpNgStatsIPv6ActiveSess_Object = MibTableColumn
vLdpNgStatsIPv6ActiveSess = _VLdpNgStatsIPv6ActiveSess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 3),
    _VLdpNgStatsIPv6ActiveSess_Type()
)
vLdpNgStatsIPv6ActiveSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6ActiveSess.setStatus("current")
_VLdpNgStatsIPv4ActiveLinkAdj_Type = Gauge32
_VLdpNgStatsIPv4ActiveLinkAdj_Object = MibTableColumn
vLdpNgStatsIPv4ActiveLinkAdj = _VLdpNgStatsIPv4ActiveLinkAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 4),
    _VLdpNgStatsIPv4ActiveLinkAdj_Type()
)
vLdpNgStatsIPv4ActiveLinkAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4ActiveLinkAdj.setStatus("current")
_VLdpNgStatsIPv6ActiveLinkAdj_Type = Gauge32
_VLdpNgStatsIPv6ActiveLinkAdj_Object = MibTableColumn
vLdpNgStatsIPv6ActiveLinkAdj = _VLdpNgStatsIPv6ActiveLinkAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 5),
    _VLdpNgStatsIPv6ActiveLinkAdj_Type()
)
vLdpNgStatsIPv6ActiveLinkAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6ActiveLinkAdj.setStatus("current")
_VLdpNgStatsIPv4ActiveTargAdj_Type = Gauge32
_VLdpNgStatsIPv4ActiveTargAdj_Object = MibTableColumn
vLdpNgStatsIPv4ActiveTargAdj = _VLdpNgStatsIPv4ActiveTargAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 6),
    _VLdpNgStatsIPv4ActiveTargAdj_Type()
)
vLdpNgStatsIPv4ActiveTargAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4ActiveTargAdj.setStatus("current")
_VLdpNgStatsIPv6ActiveTargAdj_Type = Gauge32
_VLdpNgStatsIPv6ActiveTargAdj_Object = MibTableColumn
vLdpNgStatsIPv6ActiveTargAdj = _VLdpNgStatsIPv6ActiveTargAdj_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 7),
    _VLdpNgStatsIPv6ActiveTargAdj_Type()
)
vLdpNgStatsIPv6ActiveTargAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6ActiveTargAdj.setStatus("current")
_VLdpNgStatsIPv4ActiveIf_Type = Gauge32
_VLdpNgStatsIPv4ActiveIf_Object = MibTableColumn
vLdpNgStatsIPv4ActiveIf = _VLdpNgStatsIPv4ActiveIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 8),
    _VLdpNgStatsIPv4ActiveIf_Type()
)
vLdpNgStatsIPv4ActiveIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4ActiveIf.setStatus("current")
_VLdpNgStatsIPv6ActiveIf_Type = Gauge32
_VLdpNgStatsIPv6ActiveIf_Object = MibTableColumn
vLdpNgStatsIPv6ActiveIf = _VLdpNgStatsIPv6ActiveIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 9),
    _VLdpNgStatsIPv6ActiveIf_Type()
)
vLdpNgStatsIPv6ActiveIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6ActiveIf.setStatus("current")
_VLdpNgStatsIPv4InactiveIf_Type = Gauge32
_VLdpNgStatsIPv4InactiveIf_Object = MibTableColumn
vLdpNgStatsIPv4InactiveIf = _VLdpNgStatsIPv4InactiveIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 10),
    _VLdpNgStatsIPv4InactiveIf_Type()
)
vLdpNgStatsIPv4InactiveIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4InactiveIf.setStatus("current")
_VLdpNgStatsIPv6InactiveIf_Type = Gauge32
_VLdpNgStatsIPv6InactiveIf_Object = MibTableColumn
vLdpNgStatsIPv6InactiveIf = _VLdpNgStatsIPv6InactiveIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 11),
    _VLdpNgStatsIPv6InactiveIf_Type()
)
vLdpNgStatsIPv6InactiveIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6InactiveIf.setStatus("current")
_VLdpNgStatsIPv4ActiveTargPeers_Type = Gauge32
_VLdpNgStatsIPv4ActiveTargPeers_Object = MibTableColumn
vLdpNgStatsIPv4ActiveTargPeers = _VLdpNgStatsIPv4ActiveTargPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 12),
    _VLdpNgStatsIPv4ActiveTargPeers_Type()
)
vLdpNgStatsIPv4ActiveTargPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4ActiveTargPeers.setStatus("current")
_VLdpNgStatsIPv6ActiveTargPeers_Type = Gauge32
_VLdpNgStatsIPv6ActiveTargPeers_Object = MibTableColumn
vLdpNgStatsIPv6ActiveTargPeers = _VLdpNgStatsIPv6ActiveTargPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 13),
    _VLdpNgStatsIPv6ActiveTargPeers_Type()
)
vLdpNgStatsIPv6ActiveTargPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6ActiveTargPeers.setStatus("current")
_VLdpNgStatsIPv4InactiveTargPeers_Type = Gauge32
_VLdpNgStatsIPv4InactiveTargPeers_Object = MibTableColumn
vLdpNgStatsIPv4InactiveTargPeers = _VLdpNgStatsIPv4InactiveTargPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 14),
    _VLdpNgStatsIPv4InactiveTargPeers_Type()
)
vLdpNgStatsIPv4InactiveTargPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4InactiveTargPeers.setStatus("current")
_VLdpNgStatsIPv6InactiveTargPeers_Type = Gauge32
_VLdpNgStatsIPv6InactiveTargPeers_Object = MibTableColumn
vLdpNgStatsIPv6InactiveTargPeers = _VLdpNgStatsIPv6InactiveTargPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 15),
    _VLdpNgStatsIPv6InactiveTargPeers_Type()
)
vLdpNgStatsIPv6InactiveTargPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6InactiveTargPeers.setStatus("current")
_VLdpNgStatsIPv4PfxFecRecv_Type = Gauge32
_VLdpNgStatsIPv4PfxFecRecv_Object = MibTableColumn
vLdpNgStatsIPv4PfxFecRecv = _VLdpNgStatsIPv4PfxFecRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 16),
    _VLdpNgStatsIPv4PfxFecRecv_Type()
)
vLdpNgStatsIPv4PfxFecRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4PfxFecRecv.setStatus("current")
_VLdpNgStatsIPv6PfxFecRecv_Type = Gauge32
_VLdpNgStatsIPv6PfxFecRecv_Object = MibTableColumn
vLdpNgStatsIPv6PfxFecRecv = _VLdpNgStatsIPv6PfxFecRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 17),
    _VLdpNgStatsIPv6PfxFecRecv_Type()
)
vLdpNgStatsIPv6PfxFecRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6PfxFecRecv.setStatus("current")
_VLdpNgStatsIPv4PfxFecSent_Type = Gauge32
_VLdpNgStatsIPv4PfxFecSent_Object = MibTableColumn
vLdpNgStatsIPv4PfxFecSent = _VLdpNgStatsIPv4PfxFecSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 18),
    _VLdpNgStatsIPv4PfxFecSent_Type()
)
vLdpNgStatsIPv4PfxFecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4PfxFecSent.setStatus("current")
_VLdpNgStatsIPv6PfxFecSent_Type = Gauge32
_VLdpNgStatsIPv6PfxFecSent_Object = MibTableColumn
vLdpNgStatsIPv6PfxFecSent = _VLdpNgStatsIPv6PfxFecSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 19),
    _VLdpNgStatsIPv6PfxFecSent_Type()
)
vLdpNgStatsIPv6PfxFecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6PfxFecSent.setStatus("current")
_VLdpNgStatsFec128FecSent_Type = Gauge32
_VLdpNgStatsFec128FecSent_Object = MibTableColumn
vLdpNgStatsFec128FecSent = _VLdpNgStatsFec128FecSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 20),
    _VLdpNgStatsFec128FecSent_Type()
)
vLdpNgStatsFec128FecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec128FecSent.setStatus("current")
_VLdpNgStatsFec128FecRecv_Type = Gauge32
_VLdpNgStatsFec128FecRecv_Object = MibTableColumn
vLdpNgStatsFec128FecRecv = _VLdpNgStatsFec128FecRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 21),
    _VLdpNgStatsFec128FecRecv_Type()
)
vLdpNgStatsFec128FecRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec128FecRecv.setStatus("current")
_VLdpNgStatsFec129FecSent_Type = Gauge32
_VLdpNgStatsFec129FecSent_Object = MibTableColumn
vLdpNgStatsFec129FecSent = _VLdpNgStatsFec129FecSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 22),
    _VLdpNgStatsFec129FecSent_Type()
)
vLdpNgStatsFec129FecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec129FecSent.setStatus("current")
_VLdpNgStatsFec129FecRecv_Type = Gauge32
_VLdpNgStatsFec129FecRecv_Object = MibTableColumn
vLdpNgStatsFec129FecRecv = _VLdpNgStatsFec129FecRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 23),
    _VLdpNgStatsFec129FecRecv_Type()
)
vLdpNgStatsFec129FecRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec129FecRecv.setStatus("current")
_VLdpNgStatsIPv4AttemptedSessions_Type = Counter32
_VLdpNgStatsIPv4AttemptedSessions_Object = MibTableColumn
vLdpNgStatsIPv4AttemptedSessions = _VLdpNgStatsIPv4AttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 24),
    _VLdpNgStatsIPv4AttemptedSessions_Type()
)
vLdpNgStatsIPv4AttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4AttemptedSessions.setStatus("current")
_VLdpNgStatsIPv6AttemptedSessions_Type = Counter32
_VLdpNgStatsIPv6AttemptedSessions_Object = MibTableColumn
vLdpNgStatsIPv6AttemptedSessions = _VLdpNgStatsIPv6AttemptedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 25),
    _VLdpNgStatsIPv6AttemptedSessions_Type()
)
vLdpNgStatsIPv6AttemptedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6AttemptedSessions.setStatus("current")
_VLdpNgStatsSessRejNoHelloErrs_Type = Counter32
_VLdpNgStatsSessRejNoHelloErrs_Object = MibTableColumn
vLdpNgStatsSessRejNoHelloErrs = _VLdpNgStatsSessRejNoHelloErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 26),
    _VLdpNgStatsSessRejNoHelloErrs_Type()
)
vLdpNgStatsSessRejNoHelloErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsSessRejNoHelloErrs.setStatus("current")
_VLdpNgStatsSessRejAdvErrors_Type = Counter32
_VLdpNgStatsSessRejAdvErrors_Object = MibTableColumn
vLdpNgStatsSessRejAdvErrors = _VLdpNgStatsSessRejAdvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 27),
    _VLdpNgStatsSessRejAdvErrors_Type()
)
vLdpNgStatsSessRejAdvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsSessRejAdvErrors.setStatus("current")
_VLdpNgStatsSessRejMaxPduErrs_Type = Counter32
_VLdpNgStatsSessRejMaxPduErrs_Object = MibTableColumn
vLdpNgStatsSessRejMaxPduErrs = _VLdpNgStatsSessRejMaxPduErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 28),
    _VLdpNgStatsSessRejMaxPduErrs_Type()
)
vLdpNgStatsSessRejMaxPduErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsSessRejMaxPduErrs.setStatus("current")
_VLdpNgStatsSessRejLblRngeErrs_Type = Counter32
_VLdpNgStatsSessRejLblRngeErrs_Object = MibTableColumn
vLdpNgStatsSessRejLblRngeErrs = _VLdpNgStatsSessRejLblRngeErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 29),
    _VLdpNgStatsSessRejLblRngeErrs_Type()
)
vLdpNgStatsSessRejLblRngeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsSessRejLblRngeErrs.setStatus("current")
_VLdpNgStatsBadLdpIdErrors_Type = Counter32
_VLdpNgStatsBadLdpIdErrors_Object = MibTableColumn
vLdpNgStatsBadLdpIdErrors = _VLdpNgStatsBadLdpIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 30),
    _VLdpNgStatsBadLdpIdErrors_Type()
)
vLdpNgStatsBadLdpIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsBadLdpIdErrors.setStatus("current")
_VLdpNgStatsBadPduLengthErrors_Type = Counter32
_VLdpNgStatsBadPduLengthErrors_Object = MibTableColumn
vLdpNgStatsBadPduLengthErrors = _VLdpNgStatsBadPduLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 31),
    _VLdpNgStatsBadPduLengthErrors_Type()
)
vLdpNgStatsBadPduLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsBadPduLengthErrors.setStatus("current")
_VLdpNgStatsBadMsgLengthErrors_Type = Counter32
_VLdpNgStatsBadMsgLengthErrors_Object = MibTableColumn
vLdpNgStatsBadMsgLengthErrors = _VLdpNgStatsBadMsgLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 32),
    _VLdpNgStatsBadMsgLengthErrors_Type()
)
vLdpNgStatsBadMsgLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsBadMsgLengthErrors.setStatus("current")
_VLdpNgStatsBadTlvLengthErrors_Type = Counter32
_VLdpNgStatsBadTlvLengthErrors_Object = MibTableColumn
vLdpNgStatsBadTlvLengthErrors = _VLdpNgStatsBadTlvLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 33),
    _VLdpNgStatsBadTlvLengthErrors_Type()
)
vLdpNgStatsBadTlvLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsBadTlvLengthErrors.setStatus("current")
_VLdpNgStatsMalformedTlvErrors_Type = Counter32
_VLdpNgStatsMalformedTlvErrors_Object = MibTableColumn
vLdpNgStatsMalformedTlvErrors = _VLdpNgStatsMalformedTlvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 34),
    _VLdpNgStatsMalformedTlvErrors_Type()
)
vLdpNgStatsMalformedTlvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsMalformedTlvErrors.setStatus("current")
_VLdpNgStatsKeepAliveExpErrors_Type = Counter32
_VLdpNgStatsKeepAliveExpErrors_Object = MibTableColumn
vLdpNgStatsKeepAliveExpErrors = _VLdpNgStatsKeepAliveExpErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 35),
    _VLdpNgStatsKeepAliveExpErrors_Type()
)
vLdpNgStatsKeepAliveExpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsKeepAliveExpErrors.setStatus("current")
_VLdpNgStatsShutdownNotifRecv_Type = Counter32
_VLdpNgStatsShutdownNotifRecv_Object = MibTableColumn
vLdpNgStatsShutdownNotifRecv = _VLdpNgStatsShutdownNotifRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 36),
    _VLdpNgStatsShutdownNotifRecv_Type()
)
vLdpNgStatsShutdownNotifRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsShutdownNotifRecv.setStatus("current")
_VLdpNgStatsShutdownNotifSent_Type = Counter32
_VLdpNgStatsShutdownNotifSent_Object = MibTableColumn
vLdpNgStatsShutdownNotifSent = _VLdpNgStatsShutdownNotifSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 37),
    _VLdpNgStatsShutdownNotifSent_Type()
)
vLdpNgStatsShutdownNotifSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsShutdownNotifSent.setStatus("current")
_VLdpNgStatsIPv4EgrFecPfxCount_Type = Counter32
_VLdpNgStatsIPv4EgrFecPfxCount_Object = MibTableColumn
vLdpNgStatsIPv4EgrFecPfxCount = _VLdpNgStatsIPv4EgrFecPfxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 38),
    _VLdpNgStatsIPv4EgrFecPfxCount_Type()
)
vLdpNgStatsIPv4EgrFecPfxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4EgrFecPfxCount.setStatus("current")
_VLdpNgStatsIPv6EgrFecPfxCount_Type = Counter32
_VLdpNgStatsIPv6EgrFecPfxCount_Object = MibTableColumn
vLdpNgStatsIPv6EgrFecPfxCount = _VLdpNgStatsIPv6EgrFecPfxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 39),
    _VLdpNgStatsIPv6EgrFecPfxCount_Type()
)
vLdpNgStatsIPv6EgrFecPfxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6EgrFecPfxCount.setStatus("current")
_VLdpNgStatsUnknownTlvErrors_Type = Counter32
_VLdpNgStatsUnknownTlvErrors_Object = MibTableColumn
vLdpNgStatsUnknownTlvErrors = _VLdpNgStatsUnknownTlvErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 40),
    _VLdpNgStatsUnknownTlvErrors_Type()
)
vLdpNgStatsUnknownTlvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsUnknownTlvErrors.setStatus("current")
_VLdpNgStatsIPv4P2MPFecSent_Type = Gauge32
_VLdpNgStatsIPv4P2MPFecSent_Object = MibTableColumn
vLdpNgStatsIPv4P2MPFecSent = _VLdpNgStatsIPv4P2MPFecSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 41),
    _VLdpNgStatsIPv4P2MPFecSent_Type()
)
vLdpNgStatsIPv4P2MPFecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4P2MPFecSent.setStatus("current")
_VLdpNgStatsIPv6P2MPFecSent_Type = Gauge32
_VLdpNgStatsIPv6P2MPFecSent_Object = MibTableColumn
vLdpNgStatsIPv6P2MPFecSent = _VLdpNgStatsIPv6P2MPFecSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 42),
    _VLdpNgStatsIPv6P2MPFecSent_Type()
)
vLdpNgStatsIPv6P2MPFecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6P2MPFecSent.setStatus("current")
_VLdpNgStatsIPv4P2MPFecRecv_Type = Gauge32
_VLdpNgStatsIPv4P2MPFecRecv_Object = MibTableColumn
vLdpNgStatsIPv4P2MPFecRecv = _VLdpNgStatsIPv4P2MPFecRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 43),
    _VLdpNgStatsIPv4P2MPFecRecv_Type()
)
vLdpNgStatsIPv4P2MPFecRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4P2MPFecRecv.setStatus("current")
_VLdpNgStatsIPv6P2MPFecRecv_Type = Gauge32
_VLdpNgStatsIPv6P2MPFecRecv_Object = MibTableColumn
vLdpNgStatsIPv6P2MPFecRecv = _VLdpNgStatsIPv6P2MPFecRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 44),
    _VLdpNgStatsIPv6P2MPFecRecv_Type()
)
vLdpNgStatsIPv6P2MPFecRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6P2MPFecRecv.setStatus("current")
_VLdpNgStatsIPv4PfxFecOLSessSent_Type = Gauge32
_VLdpNgStatsIPv4PfxFecOLSessSent_Object = MibTableColumn
vLdpNgStatsIPv4PfxFecOLSessSent = _VLdpNgStatsIPv4PfxFecOLSessSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 45),
    _VLdpNgStatsIPv4PfxFecOLSessSent_Type()
)
vLdpNgStatsIPv4PfxFecOLSessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4PfxFecOLSessSent.setStatus("current")
_VLdpNgStatsIPv6PfxFecOLSessSent_Type = Gauge32
_VLdpNgStatsIPv6PfxFecOLSessSent_Object = MibTableColumn
vLdpNgStatsIPv6PfxFecOLSessSent = _VLdpNgStatsIPv6PfxFecOLSessSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 46),
    _VLdpNgStatsIPv6PfxFecOLSessSent_Type()
)
vLdpNgStatsIPv6PfxFecOLSessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6PfxFecOLSessSent.setStatus("current")
_VLdpNgStatsIPv4PfxFecOLSessRecv_Type = Gauge32
_VLdpNgStatsIPv4PfxFecOLSessRecv_Object = MibTableColumn
vLdpNgStatsIPv4PfxFecOLSessRecv = _VLdpNgStatsIPv4PfxFecOLSessRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 47),
    _VLdpNgStatsIPv4PfxFecOLSessRecv_Type()
)
vLdpNgStatsIPv4PfxFecOLSessRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4PfxFecOLSessRecv.setStatus("current")
_VLdpNgStatsIPv6PfxFecOLSessRecv_Type = Gauge32
_VLdpNgStatsIPv6PfxFecOLSessRecv_Object = MibTableColumn
vLdpNgStatsIPv6PfxFecOLSessRecv = _VLdpNgStatsIPv6PfxFecOLSessRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 48),
    _VLdpNgStatsIPv6PfxFecOLSessRecv_Type()
)
vLdpNgStatsIPv6PfxFecOLSessRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6PfxFecOLSessRecv.setStatus("current")
_VLdpNgStatsIPv4P2MPFecOLSessSent_Type = Gauge32
_VLdpNgStatsIPv4P2MPFecOLSessSent_Object = MibTableColumn
vLdpNgStatsIPv4P2MPFecOLSessSent = _VLdpNgStatsIPv4P2MPFecOLSessSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 49),
    _VLdpNgStatsIPv4P2MPFecOLSessSent_Type()
)
vLdpNgStatsIPv4P2MPFecOLSessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4P2MPFecOLSessSent.setStatus("current")
_VLdpNgStatsIPv6P2MPFecOLSessSent_Type = Gauge32
_VLdpNgStatsIPv6P2MPFecOLSessSent_Object = MibTableColumn
vLdpNgStatsIPv6P2MPFecOLSessSent = _VLdpNgStatsIPv6P2MPFecOLSessSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 50),
    _VLdpNgStatsIPv6P2MPFecOLSessSent_Type()
)
vLdpNgStatsIPv6P2MPFecOLSessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6P2MPFecOLSessSent.setStatus("current")
_VLdpNgStatsIPv4P2MPFecOLSessRecv_Type = Gauge32
_VLdpNgStatsIPv4P2MPFecOLSessRecv_Object = MibTableColumn
vLdpNgStatsIPv4P2MPFecOLSessRecv = _VLdpNgStatsIPv4P2MPFecOLSessRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 51),
    _VLdpNgStatsIPv4P2MPFecOLSessRecv_Type()
)
vLdpNgStatsIPv4P2MPFecOLSessRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4P2MPFecOLSessRecv.setStatus("current")
_VLdpNgStatsIPv6P2MPFecOLSessRecv_Type = Gauge32
_VLdpNgStatsIPv6P2MPFecOLSessRecv_Object = MibTableColumn
vLdpNgStatsIPv6P2MPFecOLSessRecv = _VLdpNgStatsIPv6P2MPFecOLSessRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 52),
    _VLdpNgStatsIPv6P2MPFecOLSessRecv_Type()
)
vLdpNgStatsIPv6P2MPFecOLSessRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6P2MPFecOLSessRecv.setStatus("current")
_VLdpNgStatsFec128FecOLSessSent_Type = Gauge32
_VLdpNgStatsFec128FecOLSessSent_Object = MibTableColumn
vLdpNgStatsFec128FecOLSessSent = _VLdpNgStatsFec128FecOLSessSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 53),
    _VLdpNgStatsFec128FecOLSessSent_Type()
)
vLdpNgStatsFec128FecOLSessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec128FecOLSessSent.setStatus("current")
_VLdpNgStatsFec128FecOLSessRecv_Type = Gauge32
_VLdpNgStatsFec128FecOLSessRecv_Object = MibTableColumn
vLdpNgStatsFec128FecOLSessRecv = _VLdpNgStatsFec128FecOLSessRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 54),
    _VLdpNgStatsFec128FecOLSessRecv_Type()
)
vLdpNgStatsFec128FecOLSessRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec128FecOLSessRecv.setStatus("current")
_VLdpNgStatsFec129FecOLSessSent_Type = Gauge32
_VLdpNgStatsFec129FecOLSessSent_Object = MibTableColumn
vLdpNgStatsFec129FecOLSessSent = _VLdpNgStatsFec129FecOLSessSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 55),
    _VLdpNgStatsFec129FecOLSessSent_Type()
)
vLdpNgStatsFec129FecOLSessSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec129FecOLSessSent.setStatus("current")
_VLdpNgStatsFec129FecOLSessRecv_Type = Gauge32
_VLdpNgStatsFec129FecOLSessRecv_Object = MibTableColumn
vLdpNgStatsFec129FecOLSessRecv = _VLdpNgStatsFec129FecOLSessRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 56),
    _VLdpNgStatsFec129FecOLSessRecv_Type()
)
vLdpNgStatsFec129FecOLSessRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec129FecOLSessRecv.setStatus("current")
_VLdpNgStatsIPv4OLoadInterfaces_Type = Gauge32
_VLdpNgStatsIPv4OLoadInterfaces_Object = MibTableColumn
vLdpNgStatsIPv4OLoadInterfaces = _VLdpNgStatsIPv4OLoadInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 57),
    _VLdpNgStatsIPv4OLoadInterfaces_Type()
)
vLdpNgStatsIPv4OLoadInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4OLoadInterfaces.setStatus("current")
_VLdpNgStatsIPv6OLoadInterfaces_Type = Gauge32
_VLdpNgStatsIPv6OLoadInterfaces_Object = MibTableColumn
vLdpNgStatsIPv6OLoadInterfaces = _VLdpNgStatsIPv6OLoadInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 58),
    _VLdpNgStatsIPv6OLoadInterfaces_Type()
)
vLdpNgStatsIPv6OLoadInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6OLoadInterfaces.setStatus("current")
_VLdpNgStatsIPv4OLoadTargPeers_Type = Gauge32
_VLdpNgStatsIPv4OLoadTargPeers_Object = MibTableColumn
vLdpNgStatsIPv4OLoadTargPeers = _VLdpNgStatsIPv4OLoadTargPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 59),
    _VLdpNgStatsIPv4OLoadTargPeers_Type()
)
vLdpNgStatsIPv4OLoadTargPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4OLoadTargPeers.setStatus("current")
_VLdpNgStatsIPv6OLoadTargPeers_Type = Gauge32
_VLdpNgStatsIPv6OLoadTargPeers_Object = MibTableColumn
vLdpNgStatsIPv6OLoadTargPeers = _VLdpNgStatsIPv6OLoadTargPeers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 60),
    _VLdpNgStatsIPv6OLoadTargPeers_Type()
)
vLdpNgStatsIPv6OLoadTargPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6OLoadTargPeers.setStatus("current")
_VLdpNgStatsIPv4PfxFecInOLoad_Type = Gauge32
_VLdpNgStatsIPv4PfxFecInOLoad_Object = MibTableColumn
vLdpNgStatsIPv4PfxFecInOLoad = _VLdpNgStatsIPv4PfxFecInOLoad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 61),
    _VLdpNgStatsIPv4PfxFecInOLoad_Type()
)
vLdpNgStatsIPv4PfxFecInOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4PfxFecInOLoad.setStatus("current")
_VLdpNgStatsIPv6PfxFecInOLoad_Type = Gauge32
_VLdpNgStatsIPv6PfxFecInOLoad_Object = MibTableColumn
vLdpNgStatsIPv6PfxFecInOLoad = _VLdpNgStatsIPv6PfxFecInOLoad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 62),
    _VLdpNgStatsIPv6PfxFecInOLoad_Type()
)
vLdpNgStatsIPv6PfxFecInOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6PfxFecInOLoad.setStatus("current")
_VLdpNgStatsIPv4P2MPFecInOLoad_Type = Gauge32
_VLdpNgStatsIPv4P2MPFecInOLoad_Object = MibTableColumn
vLdpNgStatsIPv4P2MPFecInOLoad = _VLdpNgStatsIPv4P2MPFecInOLoad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 63),
    _VLdpNgStatsIPv4P2MPFecInOLoad_Type()
)
vLdpNgStatsIPv4P2MPFecInOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv4P2MPFecInOLoad.setStatus("current")
_VLdpNgStatsIPv6P2MPFecInOLoad_Type = Gauge32
_VLdpNgStatsIPv6P2MPFecInOLoad_Object = MibTableColumn
vLdpNgStatsIPv6P2MPFecInOLoad = _VLdpNgStatsIPv6P2MPFecInOLoad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 64),
    _VLdpNgStatsIPv6P2MPFecInOLoad_Type()
)
vLdpNgStatsIPv6P2MPFecInOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsIPv6P2MPFecInOLoad.setStatus("current")
_VLdpNgStatsFec128FecInOLoad_Type = Gauge32
_VLdpNgStatsFec128FecInOLoad_Object = MibTableColumn
vLdpNgStatsFec128FecInOLoad = _VLdpNgStatsFec128FecInOLoad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 65),
    _VLdpNgStatsFec128FecInOLoad_Type()
)
vLdpNgStatsFec128FecInOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec128FecInOLoad.setStatus("current")
_VLdpNgStatsFec129FecInOLoad_Type = Gauge32
_VLdpNgStatsFec129FecInOLoad_Object = MibTableColumn
vLdpNgStatsFec129FecInOLoad = _VLdpNgStatsFec129FecInOLoad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 42, 1, 66),
    _VLdpNgStatsFec129FecInOLoad_Type()
)
vLdpNgStatsFec129FecInOLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLdpNgStatsFec129FecInOLoad.setStatus("current")
_VRtrLdpNgCapabilityTable_Object = MibTable
vRtrLdpNgCapabilityTable = _VRtrLdpNgCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43)
)
if mibBuilder.loadTexts:
    vRtrLdpNgCapabilityTable.setStatus("current")
_VRtrLdpNgCapabilityEntry_Object = MibTableRow
vRtrLdpNgCapabilityEntry = _VRtrLdpNgCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpNgCapabilityEntry.setStatus("current")
_VRtrLdpNgGenP2MPCapability_Type = TruthValue
_VRtrLdpNgGenP2MPCapability_Object = MibTableColumn
vRtrLdpNgGenP2MPCapability = _VRtrLdpNgGenP2MPCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1, 1),
    _VRtrLdpNgGenP2MPCapability_Type()
)
vRtrLdpNgGenP2MPCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenP2MPCapability.setStatus("current")
_VRtrLdpNgGenMPMBBCapability_Type = TruthValue
_VRtrLdpNgGenMPMBBCapability_Object = MibTableColumn
vRtrLdpNgGenMPMBBCapability = _VRtrLdpNgGenMPMBBCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1, 2),
    _VRtrLdpNgGenMPMBBCapability_Type()
)
vRtrLdpNgGenMPMBBCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenMPMBBCapability.setStatus("current")
_VRtrLdpNgGenDynamicCapability_Type = TruthValue
_VRtrLdpNgGenDynamicCapability_Object = MibTableColumn
vRtrLdpNgGenDynamicCapability = _VRtrLdpNgGenDynamicCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1, 3),
    _VRtrLdpNgGenDynamicCapability_Type()
)
vRtrLdpNgGenDynamicCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenDynamicCapability.setStatus("current")
_VRtrLdpNgGenOverloadCapability_Type = TruthValue
_VRtrLdpNgGenOverloadCapability_Object = MibTableColumn
vRtrLdpNgGenOverloadCapability = _VRtrLdpNgGenOverloadCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1, 4),
    _VRtrLdpNgGenOverloadCapability_Type()
)
vRtrLdpNgGenOverloadCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenOverloadCapability.setStatus("current")
_VRtrLdpNgGenFec128Capability_Type = TruthValue
_VRtrLdpNgGenFec128Capability_Object = MibTableColumn
vRtrLdpNgGenFec128Capability = _VRtrLdpNgGenFec128Capability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1, 5),
    _VRtrLdpNgGenFec128Capability_Type()
)
vRtrLdpNgGenFec128Capability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenFec128Capability.setStatus("current")
_VRtrLdpNgGenFec129Capability_Type = TruthValue
_VRtrLdpNgGenFec129Capability_Object = MibTableColumn
vRtrLdpNgGenFec129Capability = _VRtrLdpNgGenFec129Capability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1, 6),
    _VRtrLdpNgGenFec129Capability_Type()
)
vRtrLdpNgGenFec129Capability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenFec129Capability.setStatus("current")
_VRtrLdpNgGenIPv4PfxFecCapability_Type = TruthValue
_VRtrLdpNgGenIPv4PfxFecCapability_Object = MibTableColumn
vRtrLdpNgGenIPv4PfxFecCapability = _VRtrLdpNgGenIPv4PfxFecCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1, 7),
    _VRtrLdpNgGenIPv4PfxFecCapability_Type()
)
vRtrLdpNgGenIPv4PfxFecCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenIPv4PfxFecCapability.setStatus("current")
_VRtrLdpNgGenIPv6PfxFecCapability_Type = TruthValue
_VRtrLdpNgGenIPv6PfxFecCapability_Object = MibTableColumn
vRtrLdpNgGenIPv6PfxFecCapability = _VRtrLdpNgGenIPv6PfxFecCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 43, 1, 8),
    _VRtrLdpNgGenIPv6PfxFecCapability_Type()
)
vRtrLdpNgGenIPv6PfxFecCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenIPv6PfxFecCapability.setStatus("current")
_VRtrLdpNgTcpSessParamsTableLstCh_Type = TimeStamp
_VRtrLdpNgTcpSessParamsTableLstCh_Object = MibScalar
vRtrLdpNgTcpSessParamsTableLstCh = _VRtrLdpNgTcpSessParamsTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 44),
    _VRtrLdpNgTcpSessParamsTableLstCh_Type()
)
vRtrLdpNgTcpSessParamsTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessParamsTableLstCh.setStatus("current")
_VRtrLdpNgTcpSessParamsTable_Object = MibTable
vRtrLdpNgTcpSessParamsTable = _VRtrLdpNgTcpSessParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45)
)
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessParamsTable.setStatus("current")
_VRtrLdpNgTcpSessParamsEntry_Object = MibTableRow
vRtrLdpNgTcpSessParamsEntry = _VRtrLdpNgTcpSessParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45, 1)
)
vRtrLdpNgTcpSessParamsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgTcpSessPeerAddrType"),
    (0, "TIMETRA-LDP-NG-MIB", "vRtrLdpNgTcpSessPeerAddr"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessParamsEntry.setStatus("current")
_VRtrLdpNgTcpSessPeerAddrType_Type = InetAddressType
_VRtrLdpNgTcpSessPeerAddrType_Object = MibTableColumn
vRtrLdpNgTcpSessPeerAddrType = _VRtrLdpNgTcpSessPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45, 1, 1),
    _VRtrLdpNgTcpSessPeerAddrType_Type()
)
vRtrLdpNgTcpSessPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessPeerAddrType.setStatus("current")


class _VRtrLdpNgTcpSessPeerAddr_Type(InetAddress):
    """Custom type vRtrLdpNgTcpSessPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrLdpNgTcpSessPeerAddr_Type.__name__ = "InetAddress"
_VRtrLdpNgTcpSessPeerAddr_Object = MibTableColumn
vRtrLdpNgTcpSessPeerAddr = _VRtrLdpNgTcpSessPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45, 1, 2),
    _VRtrLdpNgTcpSessPeerAddr_Type()
)
vRtrLdpNgTcpSessPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessPeerAddr.setStatus("current")
_VRtrLdpNgTcpSessRowStatus_Type = RowStatus
_VRtrLdpNgTcpSessRowStatus_Object = MibTableColumn
vRtrLdpNgTcpSessRowStatus = _VRtrLdpNgTcpSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45, 1, 3),
    _VRtrLdpNgTcpSessRowStatus_Type()
)
vRtrLdpNgTcpSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessRowStatus.setStatus("current")


class _VRtrLdpNgTcpSessAuth_Type(TruthValue):
    """Custom type vRtrLdpNgTcpSessAuth based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgTcpSessAuth_Type.__name__ = "TruthValue"
_VRtrLdpNgTcpSessAuth_Object = MibTableColumn
vRtrLdpNgTcpSessAuth = _VRtrLdpNgTcpSessAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45, 1, 4),
    _VRtrLdpNgTcpSessAuth_Type()
)
vRtrLdpNgTcpSessAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessAuth.setStatus("current")


class _VRtrLdpNgTcpSessAuthKey_Type(OctetString):
    """Custom type vRtrLdpNgTcpSessAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VRtrLdpNgTcpSessAuthKey_Type.__name__ = "OctetString"
_VRtrLdpNgTcpSessAuthKey_Object = MibTableColumn
vRtrLdpNgTcpSessAuthKey = _VRtrLdpNgTcpSessAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45, 1, 5),
    _VRtrLdpNgTcpSessAuthKey_Type()
)
vRtrLdpNgTcpSessAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessAuthKey.setStatus("current")


class _VRtrLdpNgTcpSessAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type vRtrLdpNgTcpSessAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTcpSessAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_VRtrLdpNgTcpSessAuthKeyChain_Object = MibTableColumn
vRtrLdpNgTcpSessAuthKeyChain = _VRtrLdpNgTcpSessAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45, 1, 6),
    _VRtrLdpNgTcpSessAuthKeyChain_Type()
)
vRtrLdpNgTcpSessAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessAuthKeyChain.setStatus("current")


class _VRtrLdpNgTcpSessPMTUDiscovery_Type(TruthValue):
    """Custom type vRtrLdpNgTcpSessPMTUDiscovery based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgTcpSessPMTUDiscovery_Type.__name__ = "TruthValue"
_VRtrLdpNgTcpSessPMTUDiscovery_Object = MibTableColumn
vRtrLdpNgTcpSessPMTUDiscovery = _VRtrLdpNgTcpSessPMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 45, 1, 7),
    _VRtrLdpNgTcpSessPMTUDiscovery_Type()
)
vRtrLdpNgTcpSessPMTUDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpNgTcpSessPMTUDiscovery.setStatus("current")
_VRtrLdpNgGeneralTableLstCh_Type = TimeStamp
_VRtrLdpNgGeneralTableLstCh_Object = MibScalar
vRtrLdpNgGeneralTableLstCh = _VRtrLdpNgGeneralTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 46),
    _VRtrLdpNgGeneralTableLstCh_Type()
)
vRtrLdpNgGeneralTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGeneralTableLstCh.setStatus("current")
_VRtrLdpNgGeneralTable_Object = MibTable
vRtrLdpNgGeneralTable = _VRtrLdpNgGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47)
)
if mibBuilder.loadTexts:
    vRtrLdpNgGeneralTable.setStatus("current")
_VRtrLdpNgGeneralEntry_Object = MibTableRow
vRtrLdpNgGeneralEntry = _VRtrLdpNgGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1)
)
vRtrLdpNgGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrLdpNgGeneralEntry.setStatus("current")
_VRtrLdpNgGenCreateTime_Type = TimeStamp
_VRtrLdpNgGenCreateTime_Object = MibTableColumn
vRtrLdpNgGenCreateTime = _VRtrLdpNgGenCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 1),
    _VRtrLdpNgGenCreateTime_Type()
)
vRtrLdpNgGenCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenCreateTime.setStatus("current")
_VRtrLdpNgGenUpTime_Type = TimeInterval
_VRtrLdpNgGenUpTime_Object = MibTableColumn
vRtrLdpNgGenUpTime = _VRtrLdpNgGenUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 2),
    _VRtrLdpNgGenUpTime_Type()
)
vRtrLdpNgGenUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenUpTime.setStatus("current")
_VRtrLdpNgGenRowLastCh_Type = TimeStamp
_VRtrLdpNgGenRowLastCh_Object = MibTableColumn
vRtrLdpNgGenRowLastCh = _VRtrLdpNgGenRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 3),
    _VRtrLdpNgGenRowLastCh_Type()
)
vRtrLdpNgGenRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenRowLastCh.setStatus("current")
_VRtrLdpNgGenLastChange_Type = TimeStamp
_VRtrLdpNgGenLastChange_Object = MibTableColumn
vRtrLdpNgGenLastChange = _VRtrLdpNgGenLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 4),
    _VRtrLdpNgGenLastChange_Type()
)
vRtrLdpNgGenLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenLastChange.setStatus("current")


class _VRtrLdpNgGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpNgGenAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrLdpNgGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpNgGenAdminState_Object = MibTableColumn
vRtrLdpNgGenAdminState = _VRtrLdpNgGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 5),
    _VRtrLdpNgGenAdminState_Type()
)
vRtrLdpNgGenAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenAdminState.setStatus("current")
_VRtrLdpNgGenOperState_Type = TmnxOperState
_VRtrLdpNgGenOperState_Object = MibTableColumn
vRtrLdpNgGenOperState = _VRtrLdpNgGenOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 6),
    _VRtrLdpNgGenOperState_Type()
)
vRtrLdpNgGenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenOperState.setStatus("current")
_VRtrLdpNgGenOperDownReason_Type = TmnxLdpGenOperDownReasonCode
_VRtrLdpNgGenOperDownReason_Object = MibTableColumn
vRtrLdpNgGenOperDownReason = _VRtrLdpNgGenOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 7),
    _VRtrLdpNgGenOperDownReason_Type()
)
vRtrLdpNgGenOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenOperDownReason.setStatus("current")
_VRtrLdpNgGenLdpIPv4LsrId_Type = MplsLsrIdentifier
_VRtrLdpNgGenLdpIPv4LsrId_Object = MibTableColumn
vRtrLdpNgGenLdpIPv4LsrId = _VRtrLdpNgGenLdpIPv4LsrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 8),
    _VRtrLdpNgGenLdpIPv4LsrId_Type()
)
vRtrLdpNgGenLdpIPv4LsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenLdpIPv4LsrId.setStatus("current")
_VRtrLdpNgGenLdpIPv6LsrId_Type = TmnxMplsLsrNgIdentifier
_VRtrLdpNgGenLdpIPv6LsrId_Object = MibTableColumn
vRtrLdpNgGenLdpIPv6LsrId = _VRtrLdpNgGenLdpIPv6LsrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 9),
    _VRtrLdpNgGenLdpIPv6LsrId_Type()
)
vRtrLdpNgGenLdpIPv6LsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenLdpIPv6LsrId.setStatus("current")
_VRtrLdpNgGenProtocolVersion_Type = Unsigned32
_VRtrLdpNgGenProtocolVersion_Object = MibTableColumn
vRtrLdpNgGenProtocolVersion = _VRtrLdpNgGenProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 10),
    _VRtrLdpNgGenProtocolVersion_Type()
)
vRtrLdpNgGenProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenProtocolVersion.setStatus("current")


class _VRtrLdpNgGenBackoffTime_Type(TmnxLdpBackoffTime):
    """Custom type vRtrLdpNgGenBackoffTime based on TmnxLdpBackoffTime"""
    subtypeSpec = TmnxLdpBackoffTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2592000),
    )


_VRtrLdpNgGenBackoffTime_Type.__name__ = "TmnxLdpBackoffTime"
_VRtrLdpNgGenBackoffTime_Object = MibTableColumn
vRtrLdpNgGenBackoffTime = _VRtrLdpNgGenBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 11),
    _VRtrLdpNgGenBackoffTime_Type()
)
vRtrLdpNgGenBackoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgGenBackoffTime.setUnits("seconds")
_VRtrLdpNgGenMaxBackoffTime_Type = TmnxLdpBackoffTime
_VRtrLdpNgGenMaxBackoffTime_Object = MibTableColumn
vRtrLdpNgGenMaxBackoffTime = _VRtrLdpNgGenMaxBackoffTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 12),
    _VRtrLdpNgGenMaxBackoffTime_Type()
)
vRtrLdpNgGenMaxBackoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenMaxBackoffTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgGenMaxBackoffTime.setUnits("seconds")


class _VRtrLdpNgGenTunnelDownDampTime_Type(Unsigned32):
    """Custom type vRtrLdpNgGenTunnelDownDampTime based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_VRtrLdpNgGenTunnelDownDampTime_Type.__name__ = "Unsigned32"
_VRtrLdpNgGenTunnelDownDampTime_Object = MibTableColumn
vRtrLdpNgGenTunnelDownDampTime = _VRtrLdpNgGenTunnelDownDampTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 13),
    _VRtrLdpNgGenTunnelDownDampTime_Type()
)
vRtrLdpNgGenTunnelDownDampTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenTunnelDownDampTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgGenTunnelDownDampTime.setUnits("seconds")


class _VRtrLdpNgGenGracefulRestart_Type(TruthValue):
    """Custom type vRtrLdpNgGenGracefulRestart based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgGenGracefulRestart_Type.__name__ = "TruthValue"
_VRtrLdpNgGenGracefulRestart_Object = MibTableColumn
vRtrLdpNgGenGracefulRestart = _VRtrLdpNgGenGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 14),
    _VRtrLdpNgGenGracefulRestart_Type()
)
vRtrLdpNgGenGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenGracefulRestart.setStatus("current")


class _VRtrLdpNgGenGRNbrLiveTime_Type(Unsigned32):
    """Custom type vRtrLdpNgGenGRNbrLiveTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_VRtrLdpNgGenGRNbrLiveTime_Type.__name__ = "Unsigned32"
_VRtrLdpNgGenGRNbrLiveTime_Object = MibTableColumn
vRtrLdpNgGenGRNbrLiveTime = _VRtrLdpNgGenGRNbrLiveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 15),
    _VRtrLdpNgGenGRNbrLiveTime_Type()
)
vRtrLdpNgGenGRNbrLiveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenGRNbrLiveTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgGenGRNbrLiveTime.setUnits("seconds")


class _VRtrLdpNgGenGRMaxRecoveryTime_Type(Unsigned32):
    """Custom type vRtrLdpNgGenGRMaxRecoveryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 1800),
    )


_VRtrLdpNgGenGRMaxRecoveryTime_Type.__name__ = "Unsigned32"
_VRtrLdpNgGenGRMaxRecoveryTime_Object = MibTableColumn
vRtrLdpNgGenGRMaxRecoveryTime = _VRtrLdpNgGenGRMaxRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 16),
    _VRtrLdpNgGenGRMaxRecoveryTime_Type()
)
vRtrLdpNgGenGRMaxRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenGRMaxRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgGenGRMaxRecoveryTime.setUnits("seconds")


class _VRtrLdpNgGenLabelWithdrawalDelay_Type(Unsigned32):
    """Custom type vRtrLdpNgGenLabelWithdrawalDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 120),
    )


_VRtrLdpNgGenLabelWithdrawalDelay_Type.__name__ = "Unsigned32"
_VRtrLdpNgGenLabelWithdrawalDelay_Object = MibTableColumn
vRtrLdpNgGenLabelWithdrawalDelay = _VRtrLdpNgGenLabelWithdrawalDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 17),
    _VRtrLdpNgGenLabelWithdrawalDelay_Type()
)
vRtrLdpNgGenLabelWithdrawalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenLabelWithdrawalDelay.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgGenLabelWithdrawalDelay.setUnits("seconds")


class _VRtrLdpNgGenImplicitNull_Type(TruthValue):
    """Custom type vRtrLdpNgGenImplicitNull based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgGenImplicitNull_Type.__name__ = "TruthValue"
_VRtrLdpNgGenImplicitNull_Object = MibTableColumn
vRtrLdpNgGenImplicitNull = _VRtrLdpNgGenImplicitNull_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 18),
    _VRtrLdpNgGenImplicitNull_Type()
)
vRtrLdpNgGenImplicitNull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenImplicitNull.setStatus("current")


class _VRtrLdpNgGenShortTTLPropLocal_Type(TruthValue):
    """Custom type vRtrLdpNgGenShortTTLPropLocal based on TruthValue"""
    defaultValue = 1


_VRtrLdpNgGenShortTTLPropLocal_Type.__name__ = "TruthValue"
_VRtrLdpNgGenShortTTLPropLocal_Object = MibTableColumn
vRtrLdpNgGenShortTTLPropLocal = _VRtrLdpNgGenShortTTLPropLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 19),
    _VRtrLdpNgGenShortTTLPropLocal_Type()
)
vRtrLdpNgGenShortTTLPropLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenShortTTLPropLocal.setStatus("current")


class _VRtrLdpNgGenShortTTLPropTransit_Type(TruthValue):
    """Custom type vRtrLdpNgGenShortTTLPropTransit based on TruthValue"""
    defaultValue = 1


_VRtrLdpNgGenShortTTLPropTransit_Type.__name__ = "TruthValue"
_VRtrLdpNgGenShortTTLPropTransit_Object = MibTableColumn
vRtrLdpNgGenShortTTLPropTransit = _VRtrLdpNgGenShortTTLPropTransit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 20),
    _VRtrLdpNgGenShortTTLPropTransit_Type()
)
vRtrLdpNgGenShortTTLPropTransit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenShortTTLPropTransit.setStatus("current")


class _VRtrLdpNgGenMPMBBTime_Type(Unsigned32):
    """Custom type vRtrLdpNgGenMPMBBTime based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrLdpNgGenMPMBBTime_Type.__name__ = "Unsigned32"
_VRtrLdpNgGenMPMBBTime_Object = MibTableColumn
vRtrLdpNgGenMPMBBTime = _VRtrLdpNgGenMPMBBTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 21),
    _VRtrLdpNgGenMPMBBTime_Type()
)
vRtrLdpNgGenMPMBBTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenMPMBBTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgGenMPMBBTime.setUnits("seconds")


class _VRtrLdpNgGenLdpFrr_Type(TruthValue):
    """Custom type vRtrLdpNgGenLdpFrr based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgGenLdpFrr_Type.__name__ = "TruthValue"
_VRtrLdpNgGenLdpFrr_Object = MibTableColumn
vRtrLdpNgGenLdpFrr = _VRtrLdpNgGenLdpFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 22),
    _VRtrLdpNgGenLdpFrr_Type()
)
vRtrLdpNgGenLdpFrr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenLdpFrr.setStatus("current")


class _VRtrLdpNgGenMcastUpstreamFrr_Type(TruthValue):
    """Custom type vRtrLdpNgGenMcastUpstreamFrr based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgGenMcastUpstreamFrr_Type.__name__ = "TruthValue"
_VRtrLdpNgGenMcastUpstreamFrr_Object = MibTableColumn
vRtrLdpNgGenMcastUpstreamFrr = _VRtrLdpNgGenMcastUpstreamFrr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 23),
    _VRtrLdpNgGenMcastUpstreamFrr_Type()
)
vRtrLdpNgGenMcastUpstreamFrr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgGenMcastUpstreamFrr.setStatus("current")
_VRtrLdpNgGenDeaggregateFec_Type = TruthValue
_VRtrLdpNgGenDeaggregateFec_Object = MibTableColumn
vRtrLdpNgGenDeaggregateFec = _VRtrLdpNgGenDeaggregateFec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 24),
    _VRtrLdpNgGenDeaggregateFec_Type()
)
vRtrLdpNgGenDeaggregateFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenDeaggregateFec.setStatus("current")


class _VRtrLdpNgGenControlMode_Type(Integer32):
    """Custom type vRtrLdpNgGenControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ordered", 1),
          ("independent", 2))
    )


_VRtrLdpNgGenControlMode_Type.__name__ = "Integer32"
_VRtrLdpNgGenControlMode_Object = MibTableColumn
vRtrLdpNgGenControlMode = _VRtrLdpNgGenControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 25),
    _VRtrLdpNgGenControlMode_Type()
)
vRtrLdpNgGenControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenControlMode.setStatus("current")
_VRtrLdpNgGenDistMethod_Type = TmnxLdpLabelDistMethod
_VRtrLdpNgGenDistMethod_Object = MibTableColumn
vRtrLdpNgGenDistMethod = _VRtrLdpNgGenDistMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 26),
    _VRtrLdpNgGenDistMethod_Type()
)
vRtrLdpNgGenDistMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenDistMethod.setStatus("current")


class _VRtrLdpNgGenRetentionMode_Type(Integer32):
    """Custom type vRtrLdpNgGenRetentionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conservative", 1),
          ("liberal", 2))
    )


_VRtrLdpNgGenRetentionMode_Type.__name__ = "Integer32"
_VRtrLdpNgGenRetentionMode_Object = MibTableColumn
vRtrLdpNgGenRetentionMode = _VRtrLdpNgGenRetentionMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 27),
    _VRtrLdpNgGenRetentionMode_Type()
)
vRtrLdpNgGenRetentionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenRetentionMode.setStatus("current")
_VRtrLdpNgGenPropagatePolicy_Type = TmnxLdpFECPolicy
_VRtrLdpNgGenPropagatePolicy_Object = MibTableColumn
vRtrLdpNgGenPropagatePolicy = _VRtrLdpNgGenPropagatePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 28),
    _VRtrLdpNgGenPropagatePolicy_Type()
)
vRtrLdpNgGenPropagatePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenPropagatePolicy.setStatus("current")


class _VRtrLdpNgGenLoopDetectCap_Type(Integer32):
    """Custom type vRtrLdpNgGenLoopDetectCap based on Integer32"""
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
        *(("none", 1),
          ("other", 2),
          ("hopCount", 3),
          ("pathVector", 4),
          ("hopCountAndPathVector", 5))
    )


_VRtrLdpNgGenLoopDetectCap_Type.__name__ = "Integer32"
_VRtrLdpNgGenLoopDetectCap_Object = MibTableColumn
vRtrLdpNgGenLoopDetectCap = _VRtrLdpNgGenLoopDetectCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 29),
    _VRtrLdpNgGenLoopDetectCap_Type()
)
vRtrLdpNgGenLoopDetectCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenLoopDetectCap.setStatus("current")


class _VRtrLdpNgGenHopLimit_Type(Unsigned32):
    """Custom type vRtrLdpNgGenHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpNgGenHopLimit_Type.__name__ = "Unsigned32"
_VRtrLdpNgGenHopLimit_Object = MibTableColumn
vRtrLdpNgGenHopLimit = _VRtrLdpNgGenHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 30),
    _VRtrLdpNgGenHopLimit_Type()
)
vRtrLdpNgGenHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenHopLimit.setStatus("current")


class _VRtrLdpNgGenPathVectorLimit_Type(Unsigned32):
    """Custom type vRtrLdpNgGenPathVectorLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrLdpNgGenPathVectorLimit_Type.__name__ = "Unsigned32"
_VRtrLdpNgGenPathVectorLimit_Object = MibTableColumn
vRtrLdpNgGenPathVectorLimit = _VRtrLdpNgGenPathVectorLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 31),
    _VRtrLdpNgGenPathVectorLimit_Type()
)
vRtrLdpNgGenPathVectorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenPathVectorLimit.setStatus("current")


class _VRtrLdpNgGenRoutePreference_Type(Unsigned32):
    """Custom type vRtrLdpNgGenRoutePreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrLdpNgGenRoutePreference_Type.__name__ = "Unsigned32"
_VRtrLdpNgGenRoutePreference_Object = MibTableColumn
vRtrLdpNgGenRoutePreference = _VRtrLdpNgGenRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 47, 1, 32),
    _VRtrLdpNgGenRoutePreference_Type()
)
vRtrLdpNgGenRoutePreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgGenRoutePreference.setStatus("current")
_VRtrLdpNgPolicyTableLstCh_Type = TimeStamp
_VRtrLdpNgPolicyTableLstCh_Object = MibScalar
vRtrLdpNgPolicyTableLstCh = _VRtrLdpNgPolicyTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 48),
    _VRtrLdpNgPolicyTableLstCh_Type()
)
vRtrLdpNgPolicyTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgPolicyTableLstCh.setStatus("current")
_VRtrLdpNgPolicyTable_Object = MibTable
vRtrLdpNgPolicyTable = _VRtrLdpNgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49)
)
if mibBuilder.loadTexts:
    vRtrLdpNgPolicyTable.setStatus("current")
_VRtrLdpNgPolicyEntry_Object = MibTableRow
vRtrLdpNgPolicyEntry = _VRtrLdpNgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpNgPolicyEntry.setStatus("current")
_VRtrLdpNgPolRowLastCh_Type = TimeStamp
_VRtrLdpNgPolRowLastCh_Object = MibTableColumn
vRtrLdpNgPolRowLastCh = _VRtrLdpNgPolRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 1),
    _VRtrLdpNgPolRowLastCh_Type()
)
vRtrLdpNgPolRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgPolRowLastCh.setStatus("current")


class _VRtrLdpNgPolImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolImportPolicy1_Object = MibTableColumn
vRtrLdpNgPolImportPolicy1 = _VRtrLdpNgPolImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 2),
    _VRtrLdpNgPolImportPolicy1_Type()
)
vRtrLdpNgPolImportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolImportPolicy1.setStatus("current")


class _VRtrLdpNgPolImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolImportPolicy2_Object = MibTableColumn
vRtrLdpNgPolImportPolicy2 = _VRtrLdpNgPolImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 3),
    _VRtrLdpNgPolImportPolicy2_Type()
)
vRtrLdpNgPolImportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolImportPolicy2.setStatus("current")


class _VRtrLdpNgPolImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolImportPolicy3_Object = MibTableColumn
vRtrLdpNgPolImportPolicy3 = _VRtrLdpNgPolImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 4),
    _VRtrLdpNgPolImportPolicy3_Type()
)
vRtrLdpNgPolImportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolImportPolicy3.setStatus("current")


class _VRtrLdpNgPolImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolImportPolicy4_Object = MibTableColumn
vRtrLdpNgPolImportPolicy4 = _VRtrLdpNgPolImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 5),
    _VRtrLdpNgPolImportPolicy4_Type()
)
vRtrLdpNgPolImportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolImportPolicy4.setStatus("current")


class _VRtrLdpNgPolImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolImportPolicy5_Object = MibTableColumn
vRtrLdpNgPolImportPolicy5 = _VRtrLdpNgPolImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 6),
    _VRtrLdpNgPolImportPolicy5_Type()
)
vRtrLdpNgPolImportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolImportPolicy5.setStatus("current")


class _VRtrLdpNgPolExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolExportPolicy1_Object = MibTableColumn
vRtrLdpNgPolExportPolicy1 = _VRtrLdpNgPolExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 7),
    _VRtrLdpNgPolExportPolicy1_Type()
)
vRtrLdpNgPolExportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolExportPolicy1.setStatus("current")


class _VRtrLdpNgPolExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolExportPolicy2_Object = MibTableColumn
vRtrLdpNgPolExportPolicy2 = _VRtrLdpNgPolExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 8),
    _VRtrLdpNgPolExportPolicy2_Type()
)
vRtrLdpNgPolExportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolExportPolicy2.setStatus("current")


class _VRtrLdpNgPolExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolExportPolicy3_Object = MibTableColumn
vRtrLdpNgPolExportPolicy3 = _VRtrLdpNgPolExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 9),
    _VRtrLdpNgPolExportPolicy3_Type()
)
vRtrLdpNgPolExportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolExportPolicy3.setStatus("current")


class _VRtrLdpNgPolExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolExportPolicy4_Object = MibTableColumn
vRtrLdpNgPolExportPolicy4 = _VRtrLdpNgPolExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 10),
    _VRtrLdpNgPolExportPolicy4_Type()
)
vRtrLdpNgPolExportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolExportPolicy4.setStatus("current")


class _VRtrLdpNgPolExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolExportPolicy5_Object = MibTableColumn
vRtrLdpNgPolExportPolicy5 = _VRtrLdpNgPolExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 11),
    _VRtrLdpNgPolExportPolicy5_Type()
)
vRtrLdpNgPolExportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolExportPolicy5.setStatus("current")


class _VRtrLdpNgPolTunlTblExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolTunlTblExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolTunlTblExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolTunlTblExportPolicy1_Object = MibTableColumn
vRtrLdpNgPolTunlTblExportPolicy1 = _VRtrLdpNgPolTunlTblExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 12),
    _VRtrLdpNgPolTunlTblExportPolicy1_Type()
)
vRtrLdpNgPolTunlTblExportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolTunlTblExportPolicy1.setStatus("current")


class _VRtrLdpNgPolTunlTblExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolTunlTblExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolTunlTblExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolTunlTblExportPolicy2_Object = MibTableColumn
vRtrLdpNgPolTunlTblExportPolicy2 = _VRtrLdpNgPolTunlTblExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 13),
    _VRtrLdpNgPolTunlTblExportPolicy2_Type()
)
vRtrLdpNgPolTunlTblExportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolTunlTblExportPolicy2.setStatus("current")


class _VRtrLdpNgPolTunlTblExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolTunlTblExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolTunlTblExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolTunlTblExportPolicy3_Object = MibTableColumn
vRtrLdpNgPolTunlTblExportPolicy3 = _VRtrLdpNgPolTunlTblExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 14),
    _VRtrLdpNgPolTunlTblExportPolicy3_Type()
)
vRtrLdpNgPolTunlTblExportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolTunlTblExportPolicy3.setStatus("current")


class _VRtrLdpNgPolTunlTblExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolTunlTblExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolTunlTblExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolTunlTblExportPolicy4_Object = MibTableColumn
vRtrLdpNgPolTunlTblExportPolicy4 = _VRtrLdpNgPolTunlTblExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 15),
    _VRtrLdpNgPolTunlTblExportPolicy4_Type()
)
vRtrLdpNgPolTunlTblExportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolTunlTblExportPolicy4.setStatus("current")


class _VRtrLdpNgPolTunlTblExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgPolTunlTblExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgPolTunlTblExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgPolTunlTblExportPolicy5_Object = MibTableColumn
vRtrLdpNgPolTunlTblExportPolicy5 = _VRtrLdpNgPolTunlTblExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 49, 1, 16),
    _VRtrLdpNgPolTunlTblExportPolicy5_Type()
)
vRtrLdpNgPolTunlTblExportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgPolTunlTblExportPolicy5.setStatus("current")
_VRtrLdpNgIfParamsTableLstCh_Type = TimeStamp
_VRtrLdpNgIfParamsTableLstCh_Object = MibScalar
vRtrLdpNgIfParamsTableLstCh = _VRtrLdpNgIfParamsTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 50),
    _VRtrLdpNgIfParamsTableLstCh_Type()
)
vRtrLdpNgIfParamsTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamsTableLstCh.setStatus("current")
_VRtrLdpNgIfParamsTable_Object = MibTable
vRtrLdpNgIfParamsTable = _VRtrLdpNgIfParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51)
)
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamsTable.setStatus("current")
_VRtrLdpNgIfParamsEntry_Object = MibTableRow
vRtrLdpNgIfParamsEntry = _VRtrLdpNgIfParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamsEntry.setStatus("current")
_VRtrLdpNgIfParamRowLastCh_Type = TimeStamp
_VRtrLdpNgIfParamRowLastCh_Object = MibTableColumn
vRtrLdpNgIfParamRowLastCh = _VRtrLdpNgIfParamRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 1),
    _VRtrLdpNgIfParamRowLastCh_Type()
)
vRtrLdpNgIfParamRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamRowLastCh.setStatus("current")


class _VRtrLdpNgIfParamIPv4KAFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpNgIfParamIPv4KAFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 3


_VRtrLdpNgIfParamIPv4KAFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpNgIfParamIPv4KAFactor_Object = MibTableColumn
vRtrLdpNgIfParamIPv4KAFactor = _VRtrLdpNgIfParamIPv4KAFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 2),
    _VRtrLdpNgIfParamIPv4KAFactor_Type()
)
vRtrLdpNgIfParamIPv4KAFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv4KAFactor.setStatus("current")


class _VRtrLdpNgIfParamIPv6KAFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpNgIfParamIPv6KAFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 3


_VRtrLdpNgIfParamIPv6KAFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpNgIfParamIPv6KAFactor_Object = MibTableColumn
vRtrLdpNgIfParamIPv6KAFactor = _VRtrLdpNgIfParamIPv6KAFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 3),
    _VRtrLdpNgIfParamIPv6KAFactor_Type()
)
vRtrLdpNgIfParamIPv6KAFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv6KAFactor.setStatus("current")


class _VRtrLdpNgIfParamIPv4KATimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpNgIfParamIPv4KATimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 30


_VRtrLdpNgIfParamIPv4KATimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpNgIfParamIPv4KATimeout_Object = MibTableColumn
vRtrLdpNgIfParamIPv4KATimeout = _VRtrLdpNgIfParamIPv4KATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 4),
    _VRtrLdpNgIfParamIPv4KATimeout_Type()
)
vRtrLdpNgIfParamIPv4KATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv4KATimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv4KATimeout.setUnits("seconds")


class _VRtrLdpNgIfParamIPv6KATimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpNgIfParamIPv6KATimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 30


_VRtrLdpNgIfParamIPv6KATimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpNgIfParamIPv6KATimeout_Object = MibTableColumn
vRtrLdpNgIfParamIPv6KATimeout = _VRtrLdpNgIfParamIPv6KATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 5),
    _VRtrLdpNgIfParamIPv6KATimeout_Type()
)
vRtrLdpNgIfParamIPv6KATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv6KATimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv6KATimeout.setUnits("seconds")


class _VRtrLdpNgIfParamIPv4HelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpNgIfParamIPv4HelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpNgIfParamIPv4HelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpNgIfParamIPv4HelloFactor_Object = MibTableColumn
vRtrLdpNgIfParamIPv4HelloFactor = _VRtrLdpNgIfParamIPv4HelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 6),
    _VRtrLdpNgIfParamIPv4HelloFactor_Type()
)
vRtrLdpNgIfParamIPv4HelloFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv4HelloFactor.setStatus("current")


class _VRtrLdpNgIfParamIPv6HelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpNgIfParamIPv6HelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpNgIfParamIPv6HelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpNgIfParamIPv6HelloFactor_Object = MibTableColumn
vRtrLdpNgIfParamIPv6HelloFactor = _VRtrLdpNgIfParamIPv6HelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 7),
    _VRtrLdpNgIfParamIPv6HelloFactor_Type()
)
vRtrLdpNgIfParamIPv6HelloFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv6HelloFactor.setStatus("current")


class _VRtrLdpNgIfParamIPv4HelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpNgIfParamIPv4HelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 15


_VRtrLdpNgIfParamIPv4HelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpNgIfParamIPv4HelloTimeout_Object = MibTableColumn
vRtrLdpNgIfParamIPv4HelloTimeout = _VRtrLdpNgIfParamIPv4HelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 8),
    _VRtrLdpNgIfParamIPv4HelloTimeout_Type()
)
vRtrLdpNgIfParamIPv4HelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv4HelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv4HelloTimeout.setUnits("seconds")


class _VRtrLdpNgIfParamIPv6HelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpNgIfParamIPv6HelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 15


_VRtrLdpNgIfParamIPv6HelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpNgIfParamIPv6HelloTimeout_Object = MibTableColumn
vRtrLdpNgIfParamIPv6HelloTimeout = _VRtrLdpNgIfParamIPv6HelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 9),
    _VRtrLdpNgIfParamIPv6HelloTimeout_Type()
)
vRtrLdpNgIfParamIPv6HelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv6HelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv6HelloTimeout.setUnits("seconds")


class _VRtrLdpNgIfParamIPv4TransAddrTyp_Type(Integer32):
    """Custom type vRtrLdpNgIfParamIPv4TransAddrTyp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("system", 2))
    )


_VRtrLdpNgIfParamIPv4TransAddrTyp_Type.__name__ = "Integer32"
_VRtrLdpNgIfParamIPv4TransAddrTyp_Object = MibTableColumn
vRtrLdpNgIfParamIPv4TransAddrTyp = _VRtrLdpNgIfParamIPv4TransAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 10),
    _VRtrLdpNgIfParamIPv4TransAddrTyp_Type()
)
vRtrLdpNgIfParamIPv4TransAddrTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv4TransAddrTyp.setStatus("current")


class _VRtrLdpNgIfParamIPv6TransAddrTyp_Type(Integer32):
    """Custom type vRtrLdpNgIfParamIPv6TransAddrTyp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("system", 2))
    )


_VRtrLdpNgIfParamIPv6TransAddrTyp_Type.__name__ = "Integer32"
_VRtrLdpNgIfParamIPv6TransAddrTyp_Object = MibTableColumn
vRtrLdpNgIfParamIPv6TransAddrTyp = _VRtrLdpNgIfParamIPv6TransAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 51, 1, 11),
    _VRtrLdpNgIfParamIPv6TransAddrTyp_Type()
)
vRtrLdpNgIfParamIPv6TransAddrTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgIfParamIPv6TransAddrTyp.setStatus("current")
_VRtrLdpNgTargTableLstCh_Type = TimeStamp
_VRtrLdpNgTargTableLstCh_Object = MibScalar
vRtrLdpNgTargTableLstCh = _VRtrLdpNgTargTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 52),
    _VRtrLdpNgTargTableLstCh_Type()
)
vRtrLdpNgTargTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargTableLstCh.setStatus("current")
_VRtrLdpNgTargTable_Object = MibTable
vRtrLdpNgTargTable = _VRtrLdpNgTargTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53)
)
if mibBuilder.loadTexts:
    vRtrLdpNgTargTable.setStatus("current")
_VRtrLdpNgTargEntry_Object = MibTableRow
vRtrLdpNgTargEntry = _VRtrLdpNgTargEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpNgTargEntry.setStatus("current")
_VRtrLdpNgTargRowLastCh_Type = TimeStamp
_VRtrLdpNgTargRowLastCh_Object = MibTableColumn
vRtrLdpNgTargRowLastCh = _VRtrLdpNgTargRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 1),
    _VRtrLdpNgTargRowLastCh_Type()
)
vRtrLdpNgTargRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgTargRowLastCh.setStatus("current")


class _VRtrLdpNgTargImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargImportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargImportPolicy1_Object = MibTableColumn
vRtrLdpNgTargImportPolicy1 = _VRtrLdpNgTargImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 2),
    _VRtrLdpNgTargImportPolicy1_Type()
)
vRtrLdpNgTargImportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargImportPolicy1.setStatus("current")


class _VRtrLdpNgTargImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargImportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargImportPolicy2_Object = MibTableColumn
vRtrLdpNgTargImportPolicy2 = _VRtrLdpNgTargImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 3),
    _VRtrLdpNgTargImportPolicy2_Type()
)
vRtrLdpNgTargImportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargImportPolicy2.setStatus("current")


class _VRtrLdpNgTargImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargImportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargImportPolicy3_Object = MibTableColumn
vRtrLdpNgTargImportPolicy3 = _VRtrLdpNgTargImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 4),
    _VRtrLdpNgTargImportPolicy3_Type()
)
vRtrLdpNgTargImportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargImportPolicy3.setStatus("current")


class _VRtrLdpNgTargImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargImportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargImportPolicy4_Object = MibTableColumn
vRtrLdpNgTargImportPolicy4 = _VRtrLdpNgTargImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 5),
    _VRtrLdpNgTargImportPolicy4_Type()
)
vRtrLdpNgTargImportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargImportPolicy4.setStatus("current")


class _VRtrLdpNgTargImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargImportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargImportPolicy5_Object = MibTableColumn
vRtrLdpNgTargImportPolicy5 = _VRtrLdpNgTargImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 6),
    _VRtrLdpNgTargImportPolicy5_Type()
)
vRtrLdpNgTargImportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargImportPolicy5.setStatus("current")


class _VRtrLdpNgTargExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargExportPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargExportPolicy1_Object = MibTableColumn
vRtrLdpNgTargExportPolicy1 = _VRtrLdpNgTargExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 7),
    _VRtrLdpNgTargExportPolicy1_Type()
)
vRtrLdpNgTargExportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargExportPolicy1.setStatus("current")


class _VRtrLdpNgTargExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargExportPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargExportPolicy2_Object = MibTableColumn
vRtrLdpNgTargExportPolicy2 = _VRtrLdpNgTargExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 8),
    _VRtrLdpNgTargExportPolicy2_Type()
)
vRtrLdpNgTargExportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargExportPolicy2.setStatus("current")


class _VRtrLdpNgTargExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargExportPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargExportPolicy3_Object = MibTableColumn
vRtrLdpNgTargExportPolicy3 = _VRtrLdpNgTargExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 9),
    _VRtrLdpNgTargExportPolicy3_Type()
)
vRtrLdpNgTargExportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargExportPolicy3.setStatus("current")


class _VRtrLdpNgTargExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargExportPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargExportPolicy4_Object = MibTableColumn
vRtrLdpNgTargExportPolicy4 = _VRtrLdpNgTargExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 10),
    _VRtrLdpNgTargExportPolicy4_Type()
)
vRtrLdpNgTargExportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargExportPolicy4.setStatus("current")


class _VRtrLdpNgTargExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgTargExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgTargExportPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgTargExportPolicy5_Object = MibTableColumn
vRtrLdpNgTargExportPolicy5 = _VRtrLdpNgTargExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 11),
    _VRtrLdpNgTargExportPolicy5_Type()
)
vRtrLdpNgTargExportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargExportPolicy5.setStatus("current")


class _VRtrLdpNgTargTunnelPreference_Type(TruthValue):
    """Custom type vRtrLdpNgTargTunnelPreference based on TruthValue"""
    defaultValue = 1


_VRtrLdpNgTargTunnelPreference_Type.__name__ = "TruthValue"
_VRtrLdpNgTargTunnelPreference_Object = MibTableColumn
vRtrLdpNgTargTunnelPreference = _VRtrLdpNgTargTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 12),
    _VRtrLdpNgTargTunnelPreference_Type()
)
vRtrLdpNgTargTunnelPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargTunnelPreference.setStatus("current")


class _VRtrLdpNgTargetedSessions_Type(TruthValue):
    """Custom type vRtrLdpNgTargetedSessions based on TruthValue"""
    defaultValue = 1


_VRtrLdpNgTargetedSessions_Type.__name__ = "TruthValue"
_VRtrLdpNgTargetedSessions_Object = MibTableColumn
vRtrLdpNgTargetedSessions = _VRtrLdpNgTargetedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 13),
    _VRtrLdpNgTargetedSessions_Type()
)
vRtrLdpNgTargetedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargetedSessions.setStatus("current")


class _VRtrLdpNgTargIPv4KAFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpNgTargIPv4KAFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 4


_VRtrLdpNgTargIPv4KAFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpNgTargIPv4KAFactor_Object = MibTableColumn
vRtrLdpNgTargIPv4KAFactor = _VRtrLdpNgTargIPv4KAFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 14),
    _VRtrLdpNgTargIPv4KAFactor_Type()
)
vRtrLdpNgTargIPv4KAFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv4KAFactor.setStatus("current")


class _VRtrLdpNgTargIPv6KAFactor_Type(TmnxLdpKeepAliveFactor):
    """Custom type vRtrLdpNgTargIPv6KAFactor based on TmnxLdpKeepAliveFactor"""
    defaultValue = 4


_VRtrLdpNgTargIPv6KAFactor_Type.__name__ = "TmnxLdpKeepAliveFactor"
_VRtrLdpNgTargIPv6KAFactor_Object = MibTableColumn
vRtrLdpNgTargIPv6KAFactor = _VRtrLdpNgTargIPv6KAFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 15),
    _VRtrLdpNgTargIPv6KAFactor_Type()
)
vRtrLdpNgTargIPv6KAFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv6KAFactor.setStatus("current")


class _VRtrLdpNgTargIPv4KATimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpNgTargIPv4KATimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 40


_VRtrLdpNgTargIPv4KATimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpNgTargIPv4KATimeout_Object = MibTableColumn
vRtrLdpNgTargIPv4KATimeout = _VRtrLdpNgTargIPv4KATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 16),
    _VRtrLdpNgTargIPv4KATimeout_Type()
)
vRtrLdpNgTargIPv4KATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv4KATimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv4KATimeout.setUnits("seconds")


class _VRtrLdpNgTargIPv6KATimeout_Type(TmnxLdpNewKeepAliveTimeout):
    """Custom type vRtrLdpNgTargIPv6KATimeout based on TmnxLdpNewKeepAliveTimeout"""
    defaultValue = 40


_VRtrLdpNgTargIPv6KATimeout_Type.__name__ = "TmnxLdpNewKeepAliveTimeout"
_VRtrLdpNgTargIPv6KATimeout_Object = MibTableColumn
vRtrLdpNgTargIPv6KATimeout = _VRtrLdpNgTargIPv6KATimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 17),
    _VRtrLdpNgTargIPv6KATimeout_Type()
)
vRtrLdpNgTargIPv6KATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv6KATimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv6KATimeout.setUnits("seconds")


class _VRtrLdpNgTargIPv4HelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpNgTargIPv4HelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpNgTargIPv4HelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpNgTargIPv4HelloFactor_Object = MibTableColumn
vRtrLdpNgTargIPv4HelloFactor = _VRtrLdpNgTargIPv4HelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 18),
    _VRtrLdpNgTargIPv4HelloFactor_Type()
)
vRtrLdpNgTargIPv4HelloFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv4HelloFactor.setStatus("current")


class _VRtrLdpNgTargIPv6HelloFactor_Type(TmnxLdpHelloFactor):
    """Custom type vRtrLdpNgTargIPv6HelloFactor based on TmnxLdpHelloFactor"""
    defaultValue = 3


_VRtrLdpNgTargIPv6HelloFactor_Type.__name__ = "TmnxLdpHelloFactor"
_VRtrLdpNgTargIPv6HelloFactor_Object = MibTableColumn
vRtrLdpNgTargIPv6HelloFactor = _VRtrLdpNgTargIPv6HelloFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 19),
    _VRtrLdpNgTargIPv6HelloFactor_Type()
)
vRtrLdpNgTargIPv6HelloFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv6HelloFactor.setStatus("current")


class _VRtrLdpNgTargIPv4HelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpNgTargIPv4HelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 45


_VRtrLdpNgTargIPv4HelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpNgTargIPv4HelloTimeout_Object = MibTableColumn
vRtrLdpNgTargIPv4HelloTimeout = _VRtrLdpNgTargIPv4HelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 20),
    _VRtrLdpNgTargIPv4HelloTimeout_Type()
)
vRtrLdpNgTargIPv4HelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv4HelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv4HelloTimeout.setUnits("seconds")


class _VRtrLdpNgTargIPv6HelloTimeout_Type(TmnxLdpNewHelloTimeout):
    """Custom type vRtrLdpNgTargIPv6HelloTimeout based on TmnxLdpNewHelloTimeout"""
    defaultValue = 45


_VRtrLdpNgTargIPv6HelloTimeout_Type.__name__ = "TmnxLdpNewHelloTimeout"
_VRtrLdpNgTargIPv6HelloTimeout_Object = MibTableColumn
vRtrLdpNgTargIPv6HelloTimeout = _VRtrLdpNgTargIPv6HelloTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 21),
    _VRtrLdpNgTargIPv6HelloTimeout_Type()
)
vRtrLdpNgTargIPv6HelloTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv6HelloTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv6HelloTimeout.setUnits("seconds")


class _VRtrLdpNgTargIPv4HelloReduction_Type(TruthValue):
    """Custom type vRtrLdpNgTargIPv4HelloReduction based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgTargIPv4HelloReduction_Type.__name__ = "TruthValue"
_VRtrLdpNgTargIPv4HelloReduction_Object = MibTableColumn
vRtrLdpNgTargIPv4HelloReduction = _VRtrLdpNgTargIPv4HelloReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 22),
    _VRtrLdpNgTargIPv4HelloReduction_Type()
)
vRtrLdpNgTargIPv4HelloReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv4HelloReduction.setStatus("current")


class _VRtrLdpNgTargIPv6HelloReduction_Type(TruthValue):
    """Custom type vRtrLdpNgTargIPv6HelloReduction based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgTargIPv6HelloReduction_Type.__name__ = "TruthValue"
_VRtrLdpNgTargIPv6HelloReduction_Object = MibTableColumn
vRtrLdpNgTargIPv6HelloReduction = _VRtrLdpNgTargIPv6HelloReduction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 23),
    _VRtrLdpNgTargIPv6HelloReduction_Type()
)
vRtrLdpNgTargIPv6HelloReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv6HelloReduction.setStatus("current")


class _VRtrLdpNgTargIPv4HelloReduceFctr_Type(Unsigned32):
    """Custom type vRtrLdpNgTargIPv4HelloReduceFctr based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_VRtrLdpNgTargIPv4HelloReduceFctr_Type.__name__ = "Unsigned32"
_VRtrLdpNgTargIPv4HelloReduceFctr_Object = MibTableColumn
vRtrLdpNgTargIPv4HelloReduceFctr = _VRtrLdpNgTargIPv4HelloReduceFctr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 24),
    _VRtrLdpNgTargIPv4HelloReduceFctr_Type()
)
vRtrLdpNgTargIPv4HelloReduceFctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv4HelloReduceFctr.setStatus("current")


class _VRtrLdpNgTargIPv6HelloReduceFctr_Type(Unsigned32):
    """Custom type vRtrLdpNgTargIPv6HelloReduceFctr based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_VRtrLdpNgTargIPv6HelloReduceFctr_Type.__name__ = "Unsigned32"
_VRtrLdpNgTargIPv6HelloReduceFctr_Object = MibTableColumn
vRtrLdpNgTargIPv6HelloReduceFctr = _VRtrLdpNgTargIPv6HelloReduceFctr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 53, 1, 25),
    _VRtrLdpNgTargIPv6HelloReduceFctr_Type()
)
vRtrLdpNgTargIPv6HelloReduceFctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgTargIPv6HelloReduceFctr.setStatus("current")
_VRtrLdpNgAggrPreMatchTableLstCh_Type = TimeStamp
_VRtrLdpNgAggrPreMatchTableLstCh_Object = MibScalar
vRtrLdpNgAggrPreMatchTableLstCh = _VRtrLdpNgAggrPreMatchTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 54),
    _VRtrLdpNgAggrPreMatchTableLstCh_Type()
)
vRtrLdpNgAggrPreMatchTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchTableLstCh.setStatus("current")
_VRtrLdpNgAggrPreMatchTable_Object = MibTable
vRtrLdpNgAggrPreMatchTable = _VRtrLdpNgAggrPreMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55)
)
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchTable.setStatus("current")
_VRtrLdpNgAggrPreMatchEntry_Object = MibTableRow
vRtrLdpNgAggrPreMatchEntry = _VRtrLdpNgAggrPreMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1)
)
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchEntry.setStatus("current")
_VRtrLdpNgAggrPreMatchRowLastCh_Type = TimeStamp
_VRtrLdpNgAggrPreMatchRowLastCh_Object = MibTableColumn
vRtrLdpNgAggrPreMatchRowLastCh = _VRtrLdpNgAggrPreMatchRowLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1, 1),
    _VRtrLdpNgAggrPreMatchRowLastCh_Type()
)
vRtrLdpNgAggrPreMatchRowLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchRowLastCh.setStatus("current")


class _VRtrLdpNgAggrPreMatchEnabled_Type(TruthValue):
    """Custom type vRtrLdpNgAggrPreMatchEnabled based on TruthValue"""
    defaultValue = 2


_VRtrLdpNgAggrPreMatchEnabled_Type.__name__ = "TruthValue"
_VRtrLdpNgAggrPreMatchEnabled_Object = MibTableColumn
vRtrLdpNgAggrPreMatchEnabled = _VRtrLdpNgAggrPreMatchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1, 2),
    _VRtrLdpNgAggrPreMatchEnabled_Type()
)
vRtrLdpNgAggrPreMatchEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchEnabled.setStatus("current")


class _VRtrLdpNgAggrPreMatchExcPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgAggrPreMatchExcPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgAggrPreMatchExcPolicy1_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgAggrPreMatchExcPolicy1_Object = MibTableColumn
vRtrLdpNgAggrPreMatchExcPolicy1 = _VRtrLdpNgAggrPreMatchExcPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1, 3),
    _VRtrLdpNgAggrPreMatchExcPolicy1_Type()
)
vRtrLdpNgAggrPreMatchExcPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchExcPolicy1.setStatus("current")


class _VRtrLdpNgAggrPreMatchExcPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgAggrPreMatchExcPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgAggrPreMatchExcPolicy2_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgAggrPreMatchExcPolicy2_Object = MibTableColumn
vRtrLdpNgAggrPreMatchExcPolicy2 = _VRtrLdpNgAggrPreMatchExcPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1, 4),
    _VRtrLdpNgAggrPreMatchExcPolicy2_Type()
)
vRtrLdpNgAggrPreMatchExcPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchExcPolicy2.setStatus("current")


class _VRtrLdpNgAggrPreMatchExcPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgAggrPreMatchExcPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgAggrPreMatchExcPolicy3_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgAggrPreMatchExcPolicy3_Object = MibTableColumn
vRtrLdpNgAggrPreMatchExcPolicy3 = _VRtrLdpNgAggrPreMatchExcPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1, 5),
    _VRtrLdpNgAggrPreMatchExcPolicy3_Type()
)
vRtrLdpNgAggrPreMatchExcPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchExcPolicy3.setStatus("current")


class _VRtrLdpNgAggrPreMatchExcPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgAggrPreMatchExcPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgAggrPreMatchExcPolicy4_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgAggrPreMatchExcPolicy4_Object = MibTableColumn
vRtrLdpNgAggrPreMatchExcPolicy4 = _VRtrLdpNgAggrPreMatchExcPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1, 6),
    _VRtrLdpNgAggrPreMatchExcPolicy4_Type()
)
vRtrLdpNgAggrPreMatchExcPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchExcPolicy4.setStatus("current")


class _VRtrLdpNgAggrPreMatchExcPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrLdpNgAggrPreMatchExcPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrLdpNgAggrPreMatchExcPolicy5_Type.__name__ = "TPolicyStatementNameOrEmpty"
_VRtrLdpNgAggrPreMatchExcPolicy5_Object = MibTableColumn
vRtrLdpNgAggrPreMatchExcPolicy5 = _VRtrLdpNgAggrPreMatchExcPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1, 7),
    _VRtrLdpNgAggrPreMatchExcPolicy5_Type()
)
vRtrLdpNgAggrPreMatchExcPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchExcPolicy5.setStatus("current")


class _VRtrLdpNgAggrPreMatchAdminState_Type(TmnxAdminState):
    """Custom type vRtrLdpNgAggrPreMatchAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrLdpNgAggrPreMatchAdminState_Type.__name__ = "TmnxAdminState"
_VRtrLdpNgAggrPreMatchAdminState_Object = MibTableColumn
vRtrLdpNgAggrPreMatchAdminState = _VRtrLdpNgAggrPreMatchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 91, 55, 1, 8),
    _VRtrLdpNgAggrPreMatchAdminState_Type()
)
vRtrLdpNgAggrPreMatchAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrLdpNgAggrPreMatchAdminState.setStatus("current")
_TmnxLdpNgNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxLdpNgNotifyPrefix = _TmnxLdpNgNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 91)
)
_TmnxLdpNgNotifications_ObjectIdentity = ObjectIdentity
tmnxLdpNgNotifications = _TmnxLdpNgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 91, 0)
)
vRtrLdpNgInetIfEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vRtrLdpNgInetIfStatsEntry")
)
vRtrLdpNgInetIfStatsEntry.setIndexNames(*vRtrLdpNgInetIfEntry.getIndexNames())
vRtrLdpNgSessionEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vRtrLdpNgSessionStatsEntry")
)
vRtrLdpNgSessionStatsEntry.setIndexNames(*vRtrLdpNgSessionEntry.getIndexNames())
vLdpNgSvcFec128InLblEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vLdpNgCepTdmFec128InLblEntry")
)
vLdpNgCepTdmFec128InLblEntry.setIndexNames(*vLdpNgSvcFec128InLblEntry.getIndexNames())
vLdpNgSvcFec128OutLblEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vLdpNgCepTdmFec128OutLblEntry")
)
vLdpNgCepTdmFec128OutLblEntry.setIndexNames(*vLdpNgSvcFec128OutLblEntry.getIndexNames())
vLdpNgSvcFec129InLblEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vLdpNgCepTdmFec129InLblEntry")
)
vLdpNgCepTdmFec129InLblEntry.setIndexNames(*vLdpNgSvcFec129InLblEntry.getIndexNames())
vLdpNgSvcFec129OutLblEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vLdpNgCepTdmFec129OutLblEntry")
)
vLdpNgCepTdmFec129OutLblEntry.setIndexNames(*vLdpNgSvcFec129OutLblEntry.getIndexNames())
vRtrLdpNgTargPeerEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vRtrLdpNgTargPeerStatsEntry")
)
vRtrLdpNgTargPeerStatsEntry.setIndexNames(*vRtrLdpNgTargPeerEntry.getIndexNames())
vRtrLdpNgGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vLdpNgStatsEntry")
)
vLdpNgStatsEntry.setIndexNames(*vRtrLdpNgGeneralEntry.getIndexNames())
vRtrLdpNgGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vRtrLdpNgCapabilityEntry")
)
vRtrLdpNgCapabilityEntry.setIndexNames(*vRtrLdpNgGeneralEntry.getIndexNames())
vRtrLdpNgGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vRtrLdpNgPolicyEntry")
)
vRtrLdpNgPolicyEntry.setIndexNames(*vRtrLdpNgGeneralEntry.getIndexNames())
vRtrLdpNgGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vRtrLdpNgIfParamsEntry")
)
vRtrLdpNgIfParamsEntry.setIndexNames(*vRtrLdpNgGeneralEntry.getIndexNames())
vRtrLdpNgGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vRtrLdpNgTargEntry")
)
vRtrLdpNgTargEntry.setIndexNames(*vRtrLdpNgGeneralEntry.getIndexNames())
vRtrLdpNgGeneralEntry.registerAugmentions(
    ("TIMETRA-LDP-NG-MIB",
     "vRtrLdpNgAggrPreMatchEntry")
)
vRtrLdpNgAggrPreMatchEntry.setIndexNames(*vRtrLdpNgGeneralEntry.getIndexNames())

# Managed Objects groups

tmnxLdpNgIfV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 1)
)
tmnxLdpNgIfV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfTableLstChanged"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfLastChange"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfAdminState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfOperState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfOperDownReason"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfBfdEnabled"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfStatsExistingAdj"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgIfV12v0Group.setStatus("current")

tmnxLdpNgAdjV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 2)
)
tmnxLdpNgAdjV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjLclLdpIdType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjLclLdpId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjEntityIndex"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjIndex"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjHoldTimeRem"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjRemConfSeqNum"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjRemIpAddrType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjRemIpAddress"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjUpTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjLclConfSeqNum"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjLclIpAddrType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjLclIpAddress"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjInHelloMsgCnt"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjOutHelloMsgCnt"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjLclTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjRemTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjBfdStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgHelloAdjMapIndex"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgAdjV12v0Group.setStatus("current")

tmnxLdpNgSessionV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 3)
)
tmnxLdpNgSessionV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalLdpIdType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalLdpId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessEntityIndex"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLabelDistMethod"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLoopDetectForPV"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPathVectorLimit"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessAdjacencyType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessProtocolVersion"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalUdpPort"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerUdpPort"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalTcpPort"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerTcpPort"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalAddrType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalAddress"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerAddrType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerAddress"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessKAHoldTimeRemaining"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessMaxPduLength"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessUpTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalKATimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerKATimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessAdvertise"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLclGRHelperState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerGRState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerNumRestart"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLastRestartTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalFtReconTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerFtReconTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalFtRecovTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerFtRecovTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessFtReconTimeRem"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessFtRecovTimeRem"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessBfdStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalP2MPCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerP2MPCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalMPMBBCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerMPMBBCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalDynCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerDynCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalOLoadCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerOLoadCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessIPv4PfxFecOLoadSent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessIPv6PfxFecOLoadSent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessIPv4PfxFecOLoadRecv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessIPv6PfxFecOLoadRecv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessIPv4P2MPFecOLSent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessIPv6P2MPFecOLSent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessIPv4P2MPFecOLRecv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessIPv6P2MPFecOLRecv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessSvcFec128OLoadSent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessSvcFec128OLoadRecv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessSvcFec129OLoadSent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessSvcFec129OLoadRecv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalIPv4PfxFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerIPv4PfxFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalIPv6PfxFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerIPv6PfxFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalSvcFec128Cap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerSvcFec128Cap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessLocalSvcFec129Cap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeerSvcFec129Cap"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgSessionV12v0Group.setStatus("current")

tmnxLdpNgSessionStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 4)
)
tmnxLdpNgSessionStatsV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsTargAdj"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLinkAdj"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsHelloIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsHelloOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsKeepaliveIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsKeepaliveOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsInitIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsInitOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblMappingIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblMappingOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblRequestIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblRequestOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblReleaseIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblReleaseOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblWithdrawIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblWithdrawOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblAbortIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsLblAbortOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsAddrIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsAddrOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsAddrWithdrIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsAddrWithdrOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsNotifIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsNotifOut"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv4PfxFecRcv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv6PfxFecRcv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv4PfxFecSnt"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv6PfxFecSnt"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv4P2MPFecRcv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv6P2MPFecRcv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv4P2MPFecSnt"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv6P2MPFecSnt"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsSvcFec128Recv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsSvcFec128Sent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsSvcFec129Recv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsSvcFec129Sent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv4AddrRecv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv6AddrRecv"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv4AddrSent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsIPv6AddrSent"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsCapabilityIn"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessStatsCapabilityOut"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgSessionStatsV12v0Group.setStatus("current")

tmnxLdpNgPeerParamsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 5)
)
tmnxLdpNgPeerParamsV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerLspRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamAuth"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamAuthKey"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamMinTTLValue"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamTTLLogId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamAuthKeyChain"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamDODLblDistrib"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamImportPolicy1"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamImportPolicy2"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamImportPolicy3"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamImportPolicy4"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamImportPolicy5"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamExportPolicy1"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamExportPolicy2"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamExportPolicy3"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamExportPolicy4"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamExportPolicy5"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessFec129CiscoInterop"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamPMTUDiscovery"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamAdvAdjAddrOnly"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessAddrLclLdpIdType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionAddrLocalLdpId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionAddrNumInAddrs"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionAddrNumOutAddrs"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessInAddrLclLdpIdType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionInAddrLocalLdpId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessOutAddrLclLdpIdType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionOutAddrLclLdpId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerTunlLspTblLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessionParamsTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessPeIDMacFlushInterop"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamIPv4PfxFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamIPv6PfxFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamP2MPFecCap"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgPeerParamsV12v0Group.setStatus("current")

tmnxLdpNgAddrFecV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 6)
)
tmnxLdpNgAddrFecV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecFlags"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecNumInLabels"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecNumOutLabels"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecInLbl"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecInLblStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecInLblIfIndex"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLbl"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLblStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLblIfIndex"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLblNHType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLblNHAddr"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLblMetric"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLblMtu"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecOutLblLspId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecMapFlags"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecMapNumInLabels"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAddrFecMapNumOutLabels"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgAddrFecV12v0Group.setStatus("current")

tmnxLdpNgP2MPFecV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 7)
)
tmnxLdpNgP2MPFecV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecFlags"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecNumInLabels"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecNumOutLabels"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecTunnelIfId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecMetric"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecMTU"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecInLbl"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecInLblStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOutLbl"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOutLblStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOutLblNHType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOutLblNHAdr"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOutLblIfIndex"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecOutLblLspId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecMapFlags"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecMapNumInLbls"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecMapNumOutLbls"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecMapTunnelIfId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecMapMetric"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgExtP2MPFecMapMTU"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgP2MPFecV12v0Group.setStatus("current")

tmnxLdpNgServFecV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 8)
)
tmnxLdpNgServFecV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vLdpNgFec128ServType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128ServId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128VpnId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128Flags"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128NumInLabels"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128NumOutLabels"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128SdpId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128MateEndptVcId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128MateEndptSdpId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLabel"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLabelStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLabelSigStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblWdwReason"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblMaxCellConcat"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblFLTxCap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblFLRxCap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblIPv4CeIpAdType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblIPv4CeIpAddr"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblIPv4Cap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblIPv6Cap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblMTU"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblVlanTag"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblVccvCV"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblVccvCC"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128InLblPwStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLabel"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLabelStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLabelSigStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblMaxCellConcat"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblFLTxCap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblFLRxCap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblIPv4CeAddrType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblIPv4CeIpAddr"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblIPv4Cap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblIPv6Cap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblMTU"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblVlanTag"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblVccvCV"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblVccvCC"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec128OutLblPwStatus"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgServFecV12v0Group.setStatus("current")

tmnxLdpNgFec129V12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 9)
)
tmnxLdpNgFec129V12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vLdpNgFec129ServType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129ServId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129VpnId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129Flags"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129NumInLabels"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129NumOutLabels"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129SdpId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateAgiType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateAgiLen"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateAgiVal"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateSrcAiiType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateSrcAiiLen"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateSrcAiiVal"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateTgtAiiType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateTgtAiiLen"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateTgtAiiVal"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129MateSdpId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLabel"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLabelStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblMTU"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblVlanTag"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblMaxCellConcat"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblSigStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblIPv4Cap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblIPv6Cap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblIPv4CeAddrType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblIPv4CeIpAddr"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblWdwReason"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblFLTxCap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblFLRxCap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblVccvCV"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblVccvCC"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129InLblPwStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLabel"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLabelStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblMTU"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblVlanTag"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblMaxCellConcat"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblSigStatus"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblIPv4Cap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblIPv6Cap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblIPv4CeAddrType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblIPv4CeIpAddr"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblFLTxCap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblFLRxCap"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblVccvCV"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblVccvCC"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgFec129OutLblPwStatus"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgFec129V12v0Group.setStatus("current")

tmnxLdpNgCepTdmFecV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 10)
)
tmnxLdpNgCepTdmFecV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblPayldSize"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblBitrate"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblRtpHeader"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblDiffTStmp"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblSigPkts"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblCasTrunk"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblTStmpFreq"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblPayldType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128InLblSsrcId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblPyldSze"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblBitrate"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblRtpHdr"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblDfTstmp"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblSigPkts"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblCasTrnk"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblTstmpFq"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblPyldTyp"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec128OutLblSsrcId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblPayldSize"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblBitrate"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblRtpHeader"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblDiffTStmp"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblSigPkts"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblCasTrunk"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblTStmpFreq"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblPayldType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129InLblSsrcId"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblPyldSize"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblBitrate"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblRtpHdr"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblDifTStmp"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblSigPkts"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblCasTrnk"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblTStmpFrq"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblPyldType"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgCepTdmFec129OutLblSsrcId"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgCepTdmFecV12v0Group.setStatus("current")

tmnxLdpNgStaticFecV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 11)
)
tmnxLdpNgStaticFecV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecNumInLabel"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgStaticFecNumOutLabel"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecInLabelRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecOperInLabel"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecOutLabelRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSFecOutLabel"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgStaticFecV12v0Group.setStatus("current")

tmnxLdpNgTargPeerV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 14)
)
tmnxLdpNgTargPeerV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerLastChange"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerAdminState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerOperState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerUpTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerOperDownReason"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerInheritance"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerKAFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerKATimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerHelloFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerHelloTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerOprHelloTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerHelloReduction"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerHelloRdctnFctr"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerBackoffTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerMaxBackoffTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerTunneling"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerBfdEnabled"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerLsrIfIndex"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerAutoCreate"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerCreator"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerTemplName"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargPeerStatExistingAdj"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgTargPeerV12v0Group.setStatus("current")

tmnxLdpNgInetIfV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 15)
)
tmnxLdpNgInetIfV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfUpTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfLastChange"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfAdminState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfOperState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfOperDownReason"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfInheritance"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfKAFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfKATimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfHelloFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfHelloTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfOperHelloTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfBackoffTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfMaxBackoffTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfTransAddrType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfLsrIfType"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfLsrIfIndex"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfIPv4P2MPFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfIPv6P2MPFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfIPv4PfxFecCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgInetIfIPv6PfxFecCap"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgInetIfV12v0Group.setStatus("current")

tmnxLdpNgStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 16)
)
tmnxLdpNgStatsV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vLdpNgStatsOperDownEvents"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4ActiveSess"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6ActiveSess"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4ActiveLinkAdj"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6ActiveLinkAdj"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4ActiveTargAdj"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6ActiveTargAdj"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4ActiveIf"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6ActiveIf"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4InactiveIf"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6InactiveIf"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4ActiveTargPeers"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6ActiveTargPeers"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4InactiveTargPeers"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6InactiveTargPeers"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4PfxFecRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6PfxFecRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4PfxFecSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6PfxFecSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec128FecSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec128FecRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec129FecSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec129FecRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4AttemptedSessions"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6AttemptedSessions"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsSessRejNoHelloErrs"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsSessRejAdvErrors"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsSessRejMaxPduErrs"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsSessRejLblRngeErrs"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsBadLdpIdErrors"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsBadPduLengthErrors"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsBadMsgLengthErrors"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsBadTlvLengthErrors"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsMalformedTlvErrors"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsKeepAliveExpErrors"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsShutdownNotifRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsShutdownNotifSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4EgrFecPfxCount"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6EgrFecPfxCount"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsUnknownTlvErrors"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4P2MPFecSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6P2MPFecSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4P2MPFecRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6P2MPFecRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4PfxFecOLSessSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6PfxFecOLSessSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4PfxFecOLSessRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6PfxFecOLSessRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4P2MPFecOLSessSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6P2MPFecOLSessSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4P2MPFecOLSessRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6P2MPFecOLSessRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec128FecOLSessSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec128FecOLSessRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec129FecOLSessSent"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec129FecOLSessRecv"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4OLoadInterfaces"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6OLoadInterfaces"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4OLoadTargPeers"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6OLoadTargPeers"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4PfxFecInOLoad"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6PfxFecInOLoad"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv4P2MPFecInOLoad"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsIPv6P2MPFecInOLoad"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec128FecInOLoad"),
        ("TIMETRA-LDP-NG-MIB", "vLdpNgStatsFec129FecInOLoad"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgStatsV12v0Group.setStatus("current")

tmnxLdpNgCapabilityV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 17)
)
tmnxLdpNgCapabilityV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenP2MPCapability"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenMPMBBCapability"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenDynamicCapability"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenOverloadCapability"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenFec128Capability"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenFec129Capability"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenIPv4PfxFecCapability"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenIPv6PfxFecCapability"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgCapabilityV12v0Group.setStatus("current")

tmnxLdpNgTcpSessParamsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 18)
)
tmnxLdpNgTcpSessParamsV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTcpSessParamsTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTcpSessRowStatus"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTcpSessAuth"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTcpSessAuthKey"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTcpSessAuthKeyChain"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTcpSessPMTUDiscovery"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgTcpSessParamsV12v0Group.setStatus("current")

tmnxLdpNgGeneralV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 19)
)
tmnxLdpNgGeneralV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGeneralTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenCreateTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenUpTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenRowLastCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenLastChange"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenAdminState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenOperState"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenOperDownReason"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenLdpIPv4LsrId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenLdpIPv6LsrId"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenProtocolVersion"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenBackoffTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenMaxBackoffTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenTunnelDownDampTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenGracefulRestart"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenGRNbrLiveTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenGRMaxRecoveryTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenLabelWithdrawalDelay"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenImplicitNull"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenShortTTLPropLocal"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenShortTTLPropTransit"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenMPMBBTime"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenLdpFrr"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenMcastUpstreamFrr"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenDeaggregateFec"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenControlMode"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenDistMethod"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenRetentionMode"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenPropagatePolicy"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenLoopDetectCap"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenHopLimit"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenPathVectorLimit"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgGenRoutePreference"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgGeneralV12v0Group.setStatus("current")

tmnxLdpNgPolicyV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 20)
)
tmnxLdpNgPolicyV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolicyTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolRowLastCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolImportPolicy1"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolImportPolicy2"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolImportPolicy3"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolImportPolicy4"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolImportPolicy5"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolExportPolicy1"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolExportPolicy2"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolExportPolicy3"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolExportPolicy4"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolExportPolicy5"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolTunlTblExportPolicy1"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolTunlTblExportPolicy2"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolTunlTblExportPolicy3"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolTunlTblExportPolicy4"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgPolTunlTblExportPolicy5"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgPolicyV12v0Group.setStatus("current")

tmnxLdpNgIfParamsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 21)
)
tmnxLdpNgIfParamsV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamsTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamRowLastCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv4KAFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv6KAFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv4KATimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv6KATimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv4HelloFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv6HelloFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv4HelloTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv6HelloTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv4TransAddrTyp"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgIfParamIPv6TransAddrTyp"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgIfParamsV12v0Group.setStatus("current")

tmnxLdpNgTargetedPeerV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 22)
)
tmnxLdpNgTargetedPeerV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargRowLastCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargImportPolicy1"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargImportPolicy2"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargImportPolicy3"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargImportPolicy4"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargImportPolicy5"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargExportPolicy1"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargExportPolicy2"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargExportPolicy3"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargExportPolicy4"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargExportPolicy5"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargTunnelPreference"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargetedSessions"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv4KAFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv6KAFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv4KATimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv6KATimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv4HelloFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv6HelloFactor"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv4HelloTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv6HelloTimeout"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv4HelloReduction"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv6HelloReduction"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv4HelloReduceFctr"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgTargIPv6HelloReduceFctr"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgTargetedPeerV12v0Group.setStatus("current")

tmnxLdpNgAggrPreMatchV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 23)
)
tmnxLdpNgAggrPreMatchV12v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchTableLstCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchRowLastCh"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchEnabled"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchExcPolicy1"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchExcPolicy2"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchExcPolicy3"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchExcPolicy4"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchExcPolicy5"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgAggrPreMatchAdminState"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgAggrPreMatchV12v0Group.setStatus("current")

tmnxLdpNgFecLimPerPeerV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 24)
)
tmnxLdpNgFecLimPerPeerV13v0Group.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamMaxFec"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamMaxFecLogOnly"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamMaxFecThold"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessOperMaxFecThreshold"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgFecLimPerPeerV13v0Group.setStatus("current")


# Notification objects

vRtrLdpNgSessMaxFecThresReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 91, 0, 1)
)
vRtrLdpNgSessMaxFecThresReached.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessParamMaxFec"),
        ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessOperMaxFecThreshold"))
)
if mibBuilder.loadTexts:
    vRtrLdpNgSessMaxFecThresReached.setStatus(
        "current"
    )


# Notifications groups

tmnxLdpNgFecLimitPerPeerNotify = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 2, 25)
)
tmnxLdpNgFecLimitPerPeerNotify.setObjects(
    ("TIMETRA-LDP-NG-MIB", "vRtrLdpNgSessMaxFecThresReached")
)
if mibBuilder.loadTexts:
    tmnxLdpNgFecLimitPerPeerNotify.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLdpNgV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 1, 1)
)
tmnxLdpNgV12v0Compliance.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "tmnxLdpNgIfV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgAdjV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgSessionV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgPeerParamsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgAddrFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgP2MPFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgServFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgFec129V12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgCepTdmFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgStaticFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgSessionStatsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgTargPeerV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgInetIfV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgStatsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgCapabilityV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgTcpSessParamsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgGeneralV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgPolicyV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgIfParamsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgTargetedPeerV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgAggrPreMatchV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxLdpNgV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 91, 1, 2)
)
tmnxLdpNgV13v0Compliance.setObjects(
      *(("TIMETRA-LDP-NG-MIB", "tmnxLdpNgIfV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgAdjV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgSessionV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgPeerParamsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgAddrFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgP2MPFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgServFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgFec129V12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgCepTdmFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgStaticFecV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgSessionStatsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgTargPeerV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgInetIfV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgStatsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgCapabilityV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgTcpSessParamsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgGeneralV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgPolicyV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgIfParamsV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgTargetedPeerV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgAggrPreMatchV12v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgFecLimPerPeerV13v0Group"),
        ("TIMETRA-LDP-NG-MIB", "tmnxLdpNgFecLimitPerPeerNotify"))
)
if mibBuilder.loadTexts:
    tmnxLdpNgV13v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LDP-NG-MIB",
    **{"timetraLdpNgMIBModule": timetraLdpNgMIBModule,
       "tmnxLdpNgConformance": tmnxLdpNgConformance,
       "tmnxLdpNgCompliances": tmnxLdpNgCompliances,
       "tmnxLdpNgV12v0Compliance": tmnxLdpNgV12v0Compliance,
       "tmnxLdpNgV13v0Compliance": tmnxLdpNgV13v0Compliance,
       "tmnxLdpNgGroups": tmnxLdpNgGroups,
       "tmnxLdpNgIfV12v0Group": tmnxLdpNgIfV12v0Group,
       "tmnxLdpNgAdjV12v0Group": tmnxLdpNgAdjV12v0Group,
       "tmnxLdpNgSessionV12v0Group": tmnxLdpNgSessionV12v0Group,
       "tmnxLdpNgSessionStatsV12v0Group": tmnxLdpNgSessionStatsV12v0Group,
       "tmnxLdpNgPeerParamsV12v0Group": tmnxLdpNgPeerParamsV12v0Group,
       "tmnxLdpNgAddrFecV12v0Group": tmnxLdpNgAddrFecV12v0Group,
       "tmnxLdpNgP2MPFecV12v0Group": tmnxLdpNgP2MPFecV12v0Group,
       "tmnxLdpNgServFecV12v0Group": tmnxLdpNgServFecV12v0Group,
       "tmnxLdpNgFec129V12v0Group": tmnxLdpNgFec129V12v0Group,
       "tmnxLdpNgCepTdmFecV12v0Group": tmnxLdpNgCepTdmFecV12v0Group,
       "tmnxLdpNgStaticFecV12v0Group": tmnxLdpNgStaticFecV12v0Group,
       "tmnxLdpNgTargPeerV12v0Group": tmnxLdpNgTargPeerV12v0Group,
       "tmnxLdpNgInetIfV12v0Group": tmnxLdpNgInetIfV12v0Group,
       "tmnxLdpNgStatsV12v0Group": tmnxLdpNgStatsV12v0Group,
       "tmnxLdpNgCapabilityV12v0Group": tmnxLdpNgCapabilityV12v0Group,
       "tmnxLdpNgTcpSessParamsV12v0Group": tmnxLdpNgTcpSessParamsV12v0Group,
       "tmnxLdpNgGeneralV12v0Group": tmnxLdpNgGeneralV12v0Group,
       "tmnxLdpNgPolicyV12v0Group": tmnxLdpNgPolicyV12v0Group,
       "tmnxLdpNgIfParamsV12v0Group": tmnxLdpNgIfParamsV12v0Group,
       "tmnxLdpNgTargetedPeerV12v0Group": tmnxLdpNgTargetedPeerV12v0Group,
       "tmnxLdpNgAggrPreMatchV12v0Group": tmnxLdpNgAggrPreMatchV12v0Group,
       "tmnxLdpNgFecLimPerPeerV13v0Group": tmnxLdpNgFecLimPerPeerV13v0Group,
       "tmnxLdpNgFecLimitPerPeerNotify": tmnxLdpNgFecLimitPerPeerNotify,
       "tmnxLdpNgObjs": tmnxLdpNgObjs,
       "vRtrLdpNgIfTableLstChanged": vRtrLdpNgIfTableLstChanged,
       "vRtrLdpNgIfTable": vRtrLdpNgIfTable,
       "vRtrLdpNgIfEntry": vRtrLdpNgIfEntry,
       "vRtrLdpNgIfIndex": vRtrLdpNgIfIndex,
       "vRtrLdpNgIfRowStatus": vRtrLdpNgIfRowStatus,
       "vRtrLdpNgIfLastChange": vRtrLdpNgIfLastChange,
       "vRtrLdpNgIfAdminState": vRtrLdpNgIfAdminState,
       "vRtrLdpNgIfOperState": vRtrLdpNgIfOperState,
       "vRtrLdpNgIfOperDownReason": vRtrLdpNgIfOperDownReason,
       "vRtrLdpNgIfBfdEnabled": vRtrLdpNgIfBfdEnabled,
       "vRtrLdpNgHelloAdjTable": vRtrLdpNgHelloAdjTable,
       "vRtrLdpNgHelloAdjEntry": vRtrLdpNgHelloAdjEntry,
       "vRtrLdpNgPeerLdpIdType": vRtrLdpNgPeerLdpIdType,
       "vRtrLdpNgPeerLdpId": vRtrLdpNgPeerLdpId,
       "vRtrLdpNgHelloAdjLclLdpIdType": vRtrLdpNgHelloAdjLclLdpIdType,
       "vRtrLdpNgHelloAdjLclLdpId": vRtrLdpNgHelloAdjLclLdpId,
       "vRtrLdpNgHelloAdjEntityIndex": vRtrLdpNgHelloAdjEntityIndex,
       "vRtrLdpNgHelloAdjIndex": vRtrLdpNgHelloAdjIndex,
       "vRtrLdpNgHelloAdjHoldTimeRem": vRtrLdpNgHelloAdjHoldTimeRem,
       "vRtrLdpNgHelloAdjType": vRtrLdpNgHelloAdjType,
       "vRtrLdpNgHelloAdjRemConfSeqNum": vRtrLdpNgHelloAdjRemConfSeqNum,
       "vRtrLdpNgHelloAdjRemIpAddrType": vRtrLdpNgHelloAdjRemIpAddrType,
       "vRtrLdpNgHelloAdjRemIpAddress": vRtrLdpNgHelloAdjRemIpAddress,
       "vRtrLdpNgHelloAdjUpTime": vRtrLdpNgHelloAdjUpTime,
       "vRtrLdpNgHelloAdjLclConfSeqNum": vRtrLdpNgHelloAdjLclConfSeqNum,
       "vRtrLdpNgHelloAdjLclIpAddrType": vRtrLdpNgHelloAdjLclIpAddrType,
       "vRtrLdpNgHelloAdjLclIpAddress": vRtrLdpNgHelloAdjLclIpAddress,
       "vRtrLdpNgHelloAdjInHelloMsgCnt": vRtrLdpNgHelloAdjInHelloMsgCnt,
       "vRtrLdpNgHelloAdjOutHelloMsgCnt": vRtrLdpNgHelloAdjOutHelloMsgCnt,
       "vRtrLdpNgHelloAdjLclTimeout": vRtrLdpNgHelloAdjLclTimeout,
       "vRtrLdpNgHelloAdjRemTimeout": vRtrLdpNgHelloAdjRemTimeout,
       "vRtrLdpNgHelloAdjBfdStatus": vRtrLdpNgHelloAdjBfdStatus,
       "vRtrLdpNgSessionTable": vRtrLdpNgSessionTable,
       "vRtrLdpNgSessionEntry": vRtrLdpNgSessionEntry,
       "vRtrLdpNgSessLocalLdpIdType": vRtrLdpNgSessLocalLdpIdType,
       "vRtrLdpNgSessLocalLdpId": vRtrLdpNgSessLocalLdpId,
       "vRtrLdpNgSessEntityIndex": vRtrLdpNgSessEntityIndex,
       "vRtrLdpNgSessLabelDistMethod": vRtrLdpNgSessLabelDistMethod,
       "vRtrLdpNgSessLoopDetectForPV": vRtrLdpNgSessLoopDetectForPV,
       "vRtrLdpNgSessPathVectorLimit": vRtrLdpNgSessPathVectorLimit,
       "vRtrLdpNgSessState": vRtrLdpNgSessState,
       "vRtrLdpNgSessAdjacencyType": vRtrLdpNgSessAdjacencyType,
       "vRtrLdpNgSessProtocolVersion": vRtrLdpNgSessProtocolVersion,
       "vRtrLdpNgSessLocalUdpPort": vRtrLdpNgSessLocalUdpPort,
       "vRtrLdpNgSessPeerUdpPort": vRtrLdpNgSessPeerUdpPort,
       "vRtrLdpNgSessLocalTcpPort": vRtrLdpNgSessLocalTcpPort,
       "vRtrLdpNgSessPeerTcpPort": vRtrLdpNgSessPeerTcpPort,
       "vRtrLdpNgSessLocalAddrType": vRtrLdpNgSessLocalAddrType,
       "vRtrLdpNgSessLocalAddress": vRtrLdpNgSessLocalAddress,
       "vRtrLdpNgSessPeerAddrType": vRtrLdpNgSessPeerAddrType,
       "vRtrLdpNgSessPeerAddress": vRtrLdpNgSessPeerAddress,
       "vRtrLdpNgSessKAHoldTimeRemaining": vRtrLdpNgSessKAHoldTimeRemaining,
       "vRtrLdpNgSessMaxPduLength": vRtrLdpNgSessMaxPduLength,
       "vRtrLdpNgSessUpTime": vRtrLdpNgSessUpTime,
       "vRtrLdpNgSessLocalKATimeout": vRtrLdpNgSessLocalKATimeout,
       "vRtrLdpNgSessPeerKATimeout": vRtrLdpNgSessPeerKATimeout,
       "vRtrLdpNgSessAdvertise": vRtrLdpNgSessAdvertise,
       "vRtrLdpNgSessLclGRHelperState": vRtrLdpNgSessLclGRHelperState,
       "vRtrLdpNgSessPeerGRState": vRtrLdpNgSessPeerGRState,
       "vRtrLdpNgSessPeerNumRestart": vRtrLdpNgSessPeerNumRestart,
       "vRtrLdpNgSessLastRestartTime": vRtrLdpNgSessLastRestartTime,
       "vRtrLdpNgSessLocalFtReconTime": vRtrLdpNgSessLocalFtReconTime,
       "vRtrLdpNgSessPeerFtReconTime": vRtrLdpNgSessPeerFtReconTime,
       "vRtrLdpNgSessLocalFtRecovTime": vRtrLdpNgSessLocalFtRecovTime,
       "vRtrLdpNgSessPeerFtRecovTime": vRtrLdpNgSessPeerFtRecovTime,
       "vRtrLdpNgSessFtReconTimeRem": vRtrLdpNgSessFtReconTimeRem,
       "vRtrLdpNgSessFtRecovTimeRem": vRtrLdpNgSessFtRecovTimeRem,
       "vRtrLdpNgSessBfdStatus": vRtrLdpNgSessBfdStatus,
       "vRtrLdpNgSessLocalP2MPCap": vRtrLdpNgSessLocalP2MPCap,
       "vRtrLdpNgSessPeerP2MPCap": vRtrLdpNgSessPeerP2MPCap,
       "vRtrLdpNgSessLocalMPMBBCap": vRtrLdpNgSessLocalMPMBBCap,
       "vRtrLdpNgSessPeerMPMBBCap": vRtrLdpNgSessPeerMPMBBCap,
       "vRtrLdpNgSessLocalDynCap": vRtrLdpNgSessLocalDynCap,
       "vRtrLdpNgSessPeerDynCap": vRtrLdpNgSessPeerDynCap,
       "vRtrLdpNgSessLocalOLoadCap": vRtrLdpNgSessLocalOLoadCap,
       "vRtrLdpNgSessPeerOLoadCap": vRtrLdpNgSessPeerOLoadCap,
       "vRtrLdpNgSessIPv4PfxFecOLoadSent": vRtrLdpNgSessIPv4PfxFecOLoadSent,
       "vRtrLdpNgSessIPv6PfxFecOLoadSent": vRtrLdpNgSessIPv6PfxFecOLoadSent,
       "vRtrLdpNgSessIPv4PfxFecOLoadRecv": vRtrLdpNgSessIPv4PfxFecOLoadRecv,
       "vRtrLdpNgSessIPv6PfxFecOLoadRecv": vRtrLdpNgSessIPv6PfxFecOLoadRecv,
       "vRtrLdpNgSessIPv4P2MPFecOLSent": vRtrLdpNgSessIPv4P2MPFecOLSent,
       "vRtrLdpNgSessIPv6P2MPFecOLSent": vRtrLdpNgSessIPv6P2MPFecOLSent,
       "vRtrLdpNgSessIPv4P2MPFecOLRecv": vRtrLdpNgSessIPv4P2MPFecOLRecv,
       "vRtrLdpNgSessIPv6P2MPFecOLRecv": vRtrLdpNgSessIPv6P2MPFecOLRecv,
       "vRtrLdpNgSessSvcFec128OLoadSent": vRtrLdpNgSessSvcFec128OLoadSent,
       "vRtrLdpNgSessSvcFec128OLoadRecv": vRtrLdpNgSessSvcFec128OLoadRecv,
       "vRtrLdpNgSessSvcFec129OLoadSent": vRtrLdpNgSessSvcFec129OLoadSent,
       "vRtrLdpNgSessSvcFec129OLoadRecv": vRtrLdpNgSessSvcFec129OLoadRecv,
       "vRtrLdpNgSessLocalIPv4PfxFecCap": vRtrLdpNgSessLocalIPv4PfxFecCap,
       "vRtrLdpNgSessPeerIPv4PfxFecCap": vRtrLdpNgSessPeerIPv4PfxFecCap,
       "vRtrLdpNgSessLocalIPv6PfxFecCap": vRtrLdpNgSessLocalIPv6PfxFecCap,
       "vRtrLdpNgSessPeerIPv6PfxFecCap": vRtrLdpNgSessPeerIPv6PfxFecCap,
       "vRtrLdpNgSessLocalSvcFec128Cap": vRtrLdpNgSessLocalSvcFec128Cap,
       "vRtrLdpNgSessPeerSvcFec128Cap": vRtrLdpNgSessPeerSvcFec128Cap,
       "vRtrLdpNgSessLocalSvcFec129Cap": vRtrLdpNgSessLocalSvcFec129Cap,
       "vRtrLdpNgSessPeerSvcFec129Cap": vRtrLdpNgSessPeerSvcFec129Cap,
       "vRtrLdpNgSessOperMaxFecThreshold": vRtrLdpNgSessOperMaxFecThreshold,
       "vRtrLdpNgTargPeerTunlLspTblLstCh": vRtrLdpNgTargPeerTunlLspTblLstCh,
       "vRtrLdpNgTargPeerTunnelLspTable": vRtrLdpNgTargPeerTunnelLspTable,
       "vRtrLdpNgTargPeerTunnelLspEntry": vRtrLdpNgTargPeerTunnelLspEntry,
       "vRtrLdpNgTargPeerLspId": vRtrLdpNgTargPeerLspId,
       "vRtrLdpNgTargPeerLspRowStatus": vRtrLdpNgTargPeerLspRowStatus,
       "vRtrLdpNgSessionParamsTableLstCh": vRtrLdpNgSessionParamsTableLstCh,
       "vRtrLdpNgSessionParamsTable": vRtrLdpNgSessionParamsTable,
       "vRtrLdpNgSessionParamsEntry": vRtrLdpNgSessionParamsEntry,
       "vRtrLdpNgSessParamRowStatus": vRtrLdpNgSessParamRowStatus,
       "vRtrLdpNgSessParamAuth": vRtrLdpNgSessParamAuth,
       "vRtrLdpNgSessParamAuthKey": vRtrLdpNgSessParamAuthKey,
       "vRtrLdpNgSessParamMinTTLValue": vRtrLdpNgSessParamMinTTLValue,
       "vRtrLdpNgSessParamTTLLogId": vRtrLdpNgSessParamTTLLogId,
       "vRtrLdpNgSessParamAuthKeyChain": vRtrLdpNgSessParamAuthKeyChain,
       "vRtrLdpNgSessParamDODLblDistrib": vRtrLdpNgSessParamDODLblDistrib,
       "vRtrLdpNgSessParamImportPolicy1": vRtrLdpNgSessParamImportPolicy1,
       "vRtrLdpNgSessParamImportPolicy2": vRtrLdpNgSessParamImportPolicy2,
       "vRtrLdpNgSessParamImportPolicy3": vRtrLdpNgSessParamImportPolicy3,
       "vRtrLdpNgSessParamImportPolicy4": vRtrLdpNgSessParamImportPolicy4,
       "vRtrLdpNgSessParamImportPolicy5": vRtrLdpNgSessParamImportPolicy5,
       "vRtrLdpNgSessParamExportPolicy1": vRtrLdpNgSessParamExportPolicy1,
       "vRtrLdpNgSessParamExportPolicy2": vRtrLdpNgSessParamExportPolicy2,
       "vRtrLdpNgSessParamExportPolicy3": vRtrLdpNgSessParamExportPolicy3,
       "vRtrLdpNgSessParamExportPolicy4": vRtrLdpNgSessParamExportPolicy4,
       "vRtrLdpNgSessParamExportPolicy5": vRtrLdpNgSessParamExportPolicy5,
       "vRtrLdpNgSessFec129CiscoInterop": vRtrLdpNgSessFec129CiscoInterop,
       "vRtrLdpNgSessParamPMTUDiscovery": vRtrLdpNgSessParamPMTUDiscovery,
       "vRtrLdpNgSessParamAdvAdjAddrOnly": vRtrLdpNgSessParamAdvAdjAddrOnly,
       "vRtrLdpNgSessPeIDMacFlushInterop": vRtrLdpNgSessPeIDMacFlushInterop,
       "vRtrLdpNgSessParamIPv4PfxFecCap": vRtrLdpNgSessParamIPv4PfxFecCap,
       "vRtrLdpNgSessParamIPv6PfxFecCap": vRtrLdpNgSessParamIPv6PfxFecCap,
       "vRtrLdpNgSessParamP2MPFecCap": vRtrLdpNgSessParamP2MPFecCap,
       "vRtrLdpNgSessParamMaxFec": vRtrLdpNgSessParamMaxFec,
       "vRtrLdpNgSessParamMaxFecLogOnly": vRtrLdpNgSessParamMaxFecLogOnly,
       "vRtrLdpNgSessParamMaxFecThold": vRtrLdpNgSessParamMaxFecThold,
       "vRtrLdpNgSessionAddrTable": vRtrLdpNgSessionAddrTable,
       "vRtrLdpNgSessionAddrEntry": vRtrLdpNgSessionAddrEntry,
       "vRtrLdpNgSessAddrLclLdpIdType": vRtrLdpNgSessAddrLclLdpIdType,
       "vRtrLdpNgSessionAddrLocalLdpId": vRtrLdpNgSessionAddrLocalLdpId,
       "vRtrLdpNgSessionAddrNumInAddrs": vRtrLdpNgSessionAddrNumInAddrs,
       "vRtrLdpNgSessionAddrNumOutAddrs": vRtrLdpNgSessionAddrNumOutAddrs,
       "vRtrLdpNgSessionInAddrTable": vRtrLdpNgSessionInAddrTable,
       "vRtrLdpNgSessionInAddrEntry": vRtrLdpNgSessionInAddrEntry,
       "vRtrLdpNgSessionInAddrAddrType": vRtrLdpNgSessionInAddrAddrType,
       "vRtrLdpNgSessionInAddrAddress": vRtrLdpNgSessionInAddrAddress,
       "vRtrLdpNgSessInAddrLclLdpIdType": vRtrLdpNgSessInAddrLclLdpIdType,
       "vRtrLdpNgSessionInAddrLocalLdpId": vRtrLdpNgSessionInAddrLocalLdpId,
       "vRtrLdpNgSessionOutAddrTable": vRtrLdpNgSessionOutAddrTable,
       "vRtrLdpNgSessionOutAddrEntry": vRtrLdpNgSessionOutAddrEntry,
       "vRtrLdpNgSessionOutAddrAddrType": vRtrLdpNgSessionOutAddrAddrType,
       "vRtrLdpNgSessionOutAddrAddress": vRtrLdpNgSessionOutAddrAddress,
       "vRtrLdpNgSessOutAddrLclLdpIdType": vRtrLdpNgSessOutAddrLclLdpIdType,
       "vRtrLdpNgSessionOutAddrLclLdpId": vRtrLdpNgSessionOutAddrLclLdpId,
       "vRtrLdpNgAddrFecTable": vRtrLdpNgAddrFecTable,
       "vRtrLdpNgAddrFecEntry": vRtrLdpNgAddrFecEntry,
       "vRtrLdpNgAddrFecFecType": vRtrLdpNgAddrFecFecType,
       "vRtrLdpNgAddrFecIpPrefixType": vRtrLdpNgAddrFecIpPrefixType,
       "vRtrLdpNgAddrFecIpPrefix": vRtrLdpNgAddrFecIpPrefix,
       "vRtrLdpNgAddrFecIpPrefixLen": vRtrLdpNgAddrFecIpPrefixLen,
       "vRtrLdpNgAddrFecFlags": vRtrLdpNgAddrFecFlags,
       "vRtrLdpNgAddrFecNumInLabels": vRtrLdpNgAddrFecNumInLabels,
       "vRtrLdpNgAddrFecNumOutLabels": vRtrLdpNgAddrFecNumOutLabels,
       "vRtrLdpNgAddrFecInLblTable": vRtrLdpNgAddrFecInLblTable,
       "vRtrLdpNgAddrFecInLblEntry": vRtrLdpNgAddrFecInLblEntry,
       "vRtrLdpNgAddrFecInLblId": vRtrLdpNgAddrFecInLblId,
       "vRtrLdpNgAddrFecInLbl": vRtrLdpNgAddrFecInLbl,
       "vRtrLdpNgAddrFecInLblStatus": vRtrLdpNgAddrFecInLblStatus,
       "vRtrLdpNgAddrFecInLblIfIndex": vRtrLdpNgAddrFecInLblIfIndex,
       "vRtrLdpNgAddrFecOutLblTable": vRtrLdpNgAddrFecOutLblTable,
       "vRtrLdpNgAddrFecOutLblEntry": vRtrLdpNgAddrFecOutLblEntry,
       "vRtrLdpNgAddrFecOutLblId": vRtrLdpNgAddrFecOutLblId,
       "vRtrLdpNgAddrFecOutLbl": vRtrLdpNgAddrFecOutLbl,
       "vRtrLdpNgAddrFecOutLblStatus": vRtrLdpNgAddrFecOutLblStatus,
       "vRtrLdpNgAddrFecOutLblIfIndex": vRtrLdpNgAddrFecOutLblIfIndex,
       "vRtrLdpNgAddrFecOutLblNHType": vRtrLdpNgAddrFecOutLblNHType,
       "vRtrLdpNgAddrFecOutLblNHAddr": vRtrLdpNgAddrFecOutLblNHAddr,
       "vRtrLdpNgAddrFecOutLblMetric": vRtrLdpNgAddrFecOutLblMetric,
       "vRtrLdpNgAddrFecOutLblMtu": vRtrLdpNgAddrFecOutLblMtu,
       "vRtrLdpNgAddrFecOutLblLspId": vRtrLdpNgAddrFecOutLblLspId,
       "vRtrLdpNgAddrFecMapTable": vRtrLdpNgAddrFecMapTable,
       "vRtrLdpNgAddrFecMapEntry": vRtrLdpNgAddrFecMapEntry,
       "vRtrLdpNgAddrFecMapFlags": vRtrLdpNgAddrFecMapFlags,
       "vRtrLdpNgAddrFecMapNumInLabels": vRtrLdpNgAddrFecMapNumInLabels,
       "vRtrLdpNgAddrFecMapNumOutLabels": vRtrLdpNgAddrFecMapNumOutLabels,
       "vRtrLdpNgExtP2MPFecTable": vRtrLdpNgExtP2MPFecTable,
       "vRtrLdpNgExtP2MPFecEntry": vRtrLdpNgExtP2MPFecEntry,
       "vRtrLdpNgExtP2MPFecOpaqueType": vRtrLdpNgExtP2MPFecOpaqueType,
       "vRtrLdpNgExtP2MPFecOpaqueLength": vRtrLdpNgExtP2MPFecOpaqueLength,
       "vRtrLdpNgExtP2MPFecOpaqueValue": vRtrLdpNgExtP2MPFecOpaqueValue,
       "vRtrLdpNgExtP2MPFecRootAddrType": vRtrLdpNgExtP2MPFecRootAddrType,
       "vRtrLdpNgExtP2MPFecRootAddress": vRtrLdpNgExtP2MPFecRootAddress,
       "vRtrLdpNgExtP2MPFecFlags": vRtrLdpNgExtP2MPFecFlags,
       "vRtrLdpNgExtP2MPFecNumInLabels": vRtrLdpNgExtP2MPFecNumInLabels,
       "vRtrLdpNgExtP2MPFecNumOutLabels": vRtrLdpNgExtP2MPFecNumOutLabels,
       "vRtrLdpNgExtP2MPFecTunnelIfId": vRtrLdpNgExtP2MPFecTunnelIfId,
       "vRtrLdpNgExtP2MPFecMetric": vRtrLdpNgExtP2MPFecMetric,
       "vRtrLdpNgExtP2MPFecMTU": vRtrLdpNgExtP2MPFecMTU,
       "vRtrLdpNgExtP2MPFecInLblTable": vRtrLdpNgExtP2MPFecInLblTable,
       "vRtrLdpNgExtP2MPFecInLblEntry": vRtrLdpNgExtP2MPFecInLblEntry,
       "vRtrLdpNgExtP2MPFecInLblId": vRtrLdpNgExtP2MPFecInLblId,
       "vRtrLdpNgExtP2MPFecInLbl": vRtrLdpNgExtP2MPFecInLbl,
       "vRtrLdpNgExtP2MPFecInLblStatus": vRtrLdpNgExtP2MPFecInLblStatus,
       "vRtrLdpNgExtP2MPFecOutLblTable": vRtrLdpNgExtP2MPFecOutLblTable,
       "vRtrLdpNgExtP2MPFecOutLblEntry": vRtrLdpNgExtP2MPFecOutLblEntry,
       "vRtrLdpNgExtP2MPFecOutLblId": vRtrLdpNgExtP2MPFecOutLblId,
       "vRtrLdpNgExtP2MPFecOutLbl": vRtrLdpNgExtP2MPFecOutLbl,
       "vRtrLdpNgExtP2MPFecOutLblStatus": vRtrLdpNgExtP2MPFecOutLblStatus,
       "vRtrLdpNgExtP2MPFecOutLblNHType": vRtrLdpNgExtP2MPFecOutLblNHType,
       "vRtrLdpNgExtP2MPFecOutLblNHAdr": vRtrLdpNgExtP2MPFecOutLblNHAdr,
       "vRtrLdpNgExtP2MPFecOutLblIfIndex": vRtrLdpNgExtP2MPFecOutLblIfIndex,
       "vRtrLdpNgExtP2MPFecOutLblLspId": vRtrLdpNgExtP2MPFecOutLblLspId,
       "vRtrLdpNgExtP2MPFecMapTable": vRtrLdpNgExtP2MPFecMapTable,
       "vRtrLdpNgExtP2MPFecMapEntry": vRtrLdpNgExtP2MPFecMapEntry,
       "vRtrLdpNgExtP2MPFecMapFlags": vRtrLdpNgExtP2MPFecMapFlags,
       "vRtrLdpNgExtP2MPFecMapNumInLbls": vRtrLdpNgExtP2MPFecMapNumInLbls,
       "vRtrLdpNgExtP2MPFecMapNumOutLbls": vRtrLdpNgExtP2MPFecMapNumOutLbls,
       "vRtrLdpNgExtP2MPFecMapTunnelIfId": vRtrLdpNgExtP2MPFecMapTunnelIfId,
       "vRtrLdpNgExtP2MPFecMapMetric": vRtrLdpNgExtP2MPFecMapMetric,
       "vRtrLdpNgExtP2MPFecMapMTU": vRtrLdpNgExtP2MPFecMapMTU,
       "vRtrLdpNgInetIfStatsTable": vRtrLdpNgInetIfStatsTable,
       "vRtrLdpNgInetIfStatsEntry": vRtrLdpNgInetIfStatsEntry,
       "vRtrLdpNgInetIfStatsExistingAdj": vRtrLdpNgInetIfStatsExistingAdj,
       "vRtrLdpNgSessionStatsTable": vRtrLdpNgSessionStatsTable,
       "vRtrLdpNgSessionStatsEntry": vRtrLdpNgSessionStatsEntry,
       "vRtrLdpNgSessStatsTargAdj": vRtrLdpNgSessStatsTargAdj,
       "vRtrLdpNgSessStatsLinkAdj": vRtrLdpNgSessStatsLinkAdj,
       "vRtrLdpNgSessStatsHelloIn": vRtrLdpNgSessStatsHelloIn,
       "vRtrLdpNgSessStatsHelloOut": vRtrLdpNgSessStatsHelloOut,
       "vRtrLdpNgSessStatsKeepaliveIn": vRtrLdpNgSessStatsKeepaliveIn,
       "vRtrLdpNgSessStatsKeepaliveOut": vRtrLdpNgSessStatsKeepaliveOut,
       "vRtrLdpNgSessStatsInitIn": vRtrLdpNgSessStatsInitIn,
       "vRtrLdpNgSessStatsInitOut": vRtrLdpNgSessStatsInitOut,
       "vRtrLdpNgSessStatsLblMappingIn": vRtrLdpNgSessStatsLblMappingIn,
       "vRtrLdpNgSessStatsLblMappingOut": vRtrLdpNgSessStatsLblMappingOut,
       "vRtrLdpNgSessStatsLblRequestIn": vRtrLdpNgSessStatsLblRequestIn,
       "vRtrLdpNgSessStatsLblRequestOut": vRtrLdpNgSessStatsLblRequestOut,
       "vRtrLdpNgSessStatsLblReleaseIn": vRtrLdpNgSessStatsLblReleaseIn,
       "vRtrLdpNgSessStatsLblReleaseOut": vRtrLdpNgSessStatsLblReleaseOut,
       "vRtrLdpNgSessStatsLblWithdrawIn": vRtrLdpNgSessStatsLblWithdrawIn,
       "vRtrLdpNgSessStatsLblWithdrawOut": vRtrLdpNgSessStatsLblWithdrawOut,
       "vRtrLdpNgSessStatsLblAbortIn": vRtrLdpNgSessStatsLblAbortIn,
       "vRtrLdpNgSessStatsLblAbortOut": vRtrLdpNgSessStatsLblAbortOut,
       "vRtrLdpNgSessStatsAddrIn": vRtrLdpNgSessStatsAddrIn,
       "vRtrLdpNgSessStatsAddrOut": vRtrLdpNgSessStatsAddrOut,
       "vRtrLdpNgSessStatsAddrWithdrIn": vRtrLdpNgSessStatsAddrWithdrIn,
       "vRtrLdpNgSessStatsAddrWithdrOut": vRtrLdpNgSessStatsAddrWithdrOut,
       "vRtrLdpNgSessStatsNotifIn": vRtrLdpNgSessStatsNotifIn,
       "vRtrLdpNgSessStatsNotifOut": vRtrLdpNgSessStatsNotifOut,
       "vRtrLdpNgSessStatsIPv4PfxFecRcv": vRtrLdpNgSessStatsIPv4PfxFecRcv,
       "vRtrLdpNgSessStatsIPv6PfxFecRcv": vRtrLdpNgSessStatsIPv6PfxFecRcv,
       "vRtrLdpNgSessStatsIPv4PfxFecSnt": vRtrLdpNgSessStatsIPv4PfxFecSnt,
       "vRtrLdpNgSessStatsIPv6PfxFecSnt": vRtrLdpNgSessStatsIPv6PfxFecSnt,
       "vRtrLdpNgSessStatsIPv4P2MPFecRcv": vRtrLdpNgSessStatsIPv4P2MPFecRcv,
       "vRtrLdpNgSessStatsIPv6P2MPFecRcv": vRtrLdpNgSessStatsIPv6P2MPFecRcv,
       "vRtrLdpNgSessStatsIPv4P2MPFecSnt": vRtrLdpNgSessStatsIPv4P2MPFecSnt,
       "vRtrLdpNgSessStatsIPv6P2MPFecSnt": vRtrLdpNgSessStatsIPv6P2MPFecSnt,
       "vRtrLdpNgSessStatsSvcFec128Recv": vRtrLdpNgSessStatsSvcFec128Recv,
       "vRtrLdpNgSessStatsSvcFec128Sent": vRtrLdpNgSessStatsSvcFec128Sent,
       "vRtrLdpNgSessStatsSvcFec129Recv": vRtrLdpNgSessStatsSvcFec129Recv,
       "vRtrLdpNgSessStatsSvcFec129Sent": vRtrLdpNgSessStatsSvcFec129Sent,
       "vRtrLdpNgSessStatsIPv4AddrRecv": vRtrLdpNgSessStatsIPv4AddrRecv,
       "vRtrLdpNgSessStatsIPv6AddrRecv": vRtrLdpNgSessStatsIPv6AddrRecv,
       "vRtrLdpNgSessStatsIPv4AddrSent": vRtrLdpNgSessStatsIPv4AddrSent,
       "vRtrLdpNgSessStatsIPv6AddrSent": vRtrLdpNgSessStatsIPv6AddrSent,
       "vRtrLdpNgSessStatsCapabilityIn": vRtrLdpNgSessStatsCapabilityIn,
       "vRtrLdpNgSessStatsCapabilityOut": vRtrLdpNgSessStatsCapabilityOut,
       "vLdpNgSvcFec128Table": vLdpNgSvcFec128Table,
       "vLdpNgSvcFec128Entry": vLdpNgSvcFec128Entry,
       "vLdpNgFec128FecType": vLdpNgFec128FecType,
       "vLdpNgFec128VcType": vLdpNgFec128VcType,
       "vLdpNgFec128VcId": vLdpNgFec128VcId,
       "vLdpNgFec128ServType": vLdpNgFec128ServType,
       "vLdpNgFec128ServId": vLdpNgFec128ServId,
       "vLdpNgFec128VpnId": vLdpNgFec128VpnId,
       "vLdpNgFec128Flags": vLdpNgFec128Flags,
       "vLdpNgFec128NumInLabels": vLdpNgFec128NumInLabels,
       "vLdpNgFec128NumOutLabels": vLdpNgFec128NumOutLabels,
       "vLdpNgFec128SdpId": vLdpNgFec128SdpId,
       "vLdpNgFec128MateEndptVcId": vLdpNgFec128MateEndptVcId,
       "vLdpNgFec128MateEndptSdpId": vLdpNgFec128MateEndptSdpId,
       "vLdpNgSvcFec128InLblTable": vLdpNgSvcFec128InLblTable,
       "vLdpNgSvcFec128InLblEntry": vLdpNgSvcFec128InLblEntry,
       "vLdpNgFec128InLabelId": vLdpNgFec128InLabelId,
       "vLdpNgFec128InLabel": vLdpNgFec128InLabel,
       "vLdpNgFec128InLabelStatus": vLdpNgFec128InLabelStatus,
       "vLdpNgFec128InLabelSigStatus": vLdpNgFec128InLabelSigStatus,
       "vLdpNgFec128InLblWdwReason": vLdpNgFec128InLblWdwReason,
       "vLdpNgFec128InLblMaxCellConcat": vLdpNgFec128InLblMaxCellConcat,
       "vLdpNgFec128InLblFLTxCap": vLdpNgFec128InLblFLTxCap,
       "vLdpNgFec128InLblFLRxCap": vLdpNgFec128InLblFLRxCap,
       "vLdpNgFec128InLblIPv4CeIpAdType": vLdpNgFec128InLblIPv4CeIpAdType,
       "vLdpNgFec128InLblIPv4CeIpAddr": vLdpNgFec128InLblIPv4CeIpAddr,
       "vLdpNgFec128InLblIPv4Cap": vLdpNgFec128InLblIPv4Cap,
       "vLdpNgFec128InLblIPv6Cap": vLdpNgFec128InLblIPv6Cap,
       "vLdpNgFec128InLblMTU": vLdpNgFec128InLblMTU,
       "vLdpNgFec128InLblVlanTag": vLdpNgFec128InLblVlanTag,
       "vLdpNgFec128InLblVccvCV": vLdpNgFec128InLblVccvCV,
       "vLdpNgFec128InLblVccvCC": vLdpNgFec128InLblVccvCC,
       "vLdpNgFec128InLblPwStatus": vLdpNgFec128InLblPwStatus,
       "vLdpNgSvcFec128OutLblTable": vLdpNgSvcFec128OutLblTable,
       "vLdpNgSvcFec128OutLblEntry": vLdpNgSvcFec128OutLblEntry,
       "vLdpNgFec128OutLabelId": vLdpNgFec128OutLabelId,
       "vLdpNgFec128OutLabel": vLdpNgFec128OutLabel,
       "vLdpNgFec128OutLabelStatus": vLdpNgFec128OutLabelStatus,
       "vLdpNgFec128OutLabelSigStatus": vLdpNgFec128OutLabelSigStatus,
       "vLdpNgFec128OutLblMaxCellConcat": vLdpNgFec128OutLblMaxCellConcat,
       "vLdpNgFec128OutLblFLTxCap": vLdpNgFec128OutLblFLTxCap,
       "vLdpNgFec128OutLblFLRxCap": vLdpNgFec128OutLblFLRxCap,
       "vLdpNgFec128OutLblIPv4CeAddrType": vLdpNgFec128OutLblIPv4CeAddrType,
       "vLdpNgFec128OutLblIPv4CeIpAddr": vLdpNgFec128OutLblIPv4CeIpAddr,
       "vLdpNgFec128OutLblIPv4Cap": vLdpNgFec128OutLblIPv4Cap,
       "vLdpNgFec128OutLblIPv6Cap": vLdpNgFec128OutLblIPv6Cap,
       "vLdpNgFec128OutLblMTU": vLdpNgFec128OutLblMTU,
       "vLdpNgFec128OutLblVlanTag": vLdpNgFec128OutLblVlanTag,
       "vLdpNgFec128OutLblVccvCV": vLdpNgFec128OutLblVccvCV,
       "vLdpNgFec128OutLblVccvCC": vLdpNgFec128OutLblVccvCC,
       "vLdpNgFec128OutLblPwStatus": vLdpNgFec128OutLblPwStatus,
       "vRtrLdpNgHelloAdjMapTable": vRtrLdpNgHelloAdjMapTable,
       "vRtrLdpNgHelloAdjMapEntry": vRtrLdpNgHelloAdjMapEntry,
       "vRtrLdpNgHelloAdjMapLdpIdType": vRtrLdpNgHelloAdjMapLdpIdType,
       "vRtrLdpNgHelloAdjMapLdpId": vRtrLdpNgHelloAdjMapLdpId,
       "vRtrLdpNgHelloAdjMapIndex": vRtrLdpNgHelloAdjMapIndex,
       "vLdpNgSvcFec129Table": vLdpNgSvcFec129Table,
       "vLdpNgSvcFec129Entry": vLdpNgSvcFec129Entry,
       "vLdpNgFec129AgiType": vLdpNgFec129AgiType,
       "vLdpNgFec129AgiLen": vLdpNgFec129AgiLen,
       "vLdpNgFec129AgiVal": vLdpNgFec129AgiVal,
       "vLdpNgFec129SrcAiiType": vLdpNgFec129SrcAiiType,
       "vLdpNgFec129SrcAiiLen": vLdpNgFec129SrcAiiLen,
       "vLdpNgFec129SrcAiiVal": vLdpNgFec129SrcAiiVal,
       "vLdpNgFec129TgtAiiType": vLdpNgFec129TgtAiiType,
       "vLdpNgFec129TgtAiiLen": vLdpNgFec129TgtAiiLen,
       "vLdpNgFec129TgtAiiVal": vLdpNgFec129TgtAiiVal,
       "vLdpNgFec129ServType": vLdpNgFec129ServType,
       "vLdpNgFec129ServId": vLdpNgFec129ServId,
       "vLdpNgFec129VpnId": vLdpNgFec129VpnId,
       "vLdpNgFec129Flags": vLdpNgFec129Flags,
       "vLdpNgFec129NumInLabels": vLdpNgFec129NumInLabels,
       "vLdpNgFec129NumOutLabels": vLdpNgFec129NumOutLabels,
       "vLdpNgFec129SdpId": vLdpNgFec129SdpId,
       "vLdpNgFec129MateAgiType": vLdpNgFec129MateAgiType,
       "vLdpNgFec129MateAgiLen": vLdpNgFec129MateAgiLen,
       "vLdpNgFec129MateAgiVal": vLdpNgFec129MateAgiVal,
       "vLdpNgFec129MateSrcAiiType": vLdpNgFec129MateSrcAiiType,
       "vLdpNgFec129MateSrcAiiLen": vLdpNgFec129MateSrcAiiLen,
       "vLdpNgFec129MateSrcAiiVal": vLdpNgFec129MateSrcAiiVal,
       "vLdpNgFec129MateTgtAiiType": vLdpNgFec129MateTgtAiiType,
       "vLdpNgFec129MateTgtAiiLen": vLdpNgFec129MateTgtAiiLen,
       "vLdpNgFec129MateTgtAiiVal": vLdpNgFec129MateTgtAiiVal,
       "vLdpNgFec129MateSdpId": vLdpNgFec129MateSdpId,
       "vLdpNgSvcFec129InLblTable": vLdpNgSvcFec129InLblTable,
       "vLdpNgSvcFec129InLblEntry": vLdpNgSvcFec129InLblEntry,
       "vLdpNgFec129InLblId": vLdpNgFec129InLblId,
       "vLdpNgFec129InLabel": vLdpNgFec129InLabel,
       "vLdpNgFec129InLabelStatus": vLdpNgFec129InLabelStatus,
       "vLdpNgFec129InLblMTU": vLdpNgFec129InLblMTU,
       "vLdpNgFec129InLblVlanTag": vLdpNgFec129InLblVlanTag,
       "vLdpNgFec129InLblMaxCellConcat": vLdpNgFec129InLblMaxCellConcat,
       "vLdpNgFec129InLblSigStatus": vLdpNgFec129InLblSigStatus,
       "vLdpNgFec129InLblIPv4Cap": vLdpNgFec129InLblIPv4Cap,
       "vLdpNgFec129InLblIPv6Cap": vLdpNgFec129InLblIPv6Cap,
       "vLdpNgFec129InLblIPv4CeAddrType": vLdpNgFec129InLblIPv4CeAddrType,
       "vLdpNgFec129InLblIPv4CeIpAddr": vLdpNgFec129InLblIPv4CeIpAddr,
       "vLdpNgFec129InLblWdwReason": vLdpNgFec129InLblWdwReason,
       "vLdpNgFec129InLblFLTxCap": vLdpNgFec129InLblFLTxCap,
       "vLdpNgFec129InLblFLRxCap": vLdpNgFec129InLblFLRxCap,
       "vLdpNgFec129InLblVccvCV": vLdpNgFec129InLblVccvCV,
       "vLdpNgFec129InLblVccvCC": vLdpNgFec129InLblVccvCC,
       "vLdpNgFec129InLblPwStatus": vLdpNgFec129InLblPwStatus,
       "vLdpNgSvcFec129OutLblTable": vLdpNgSvcFec129OutLblTable,
       "vLdpNgSvcFec129OutLblEntry": vLdpNgSvcFec129OutLblEntry,
       "vLdpNgFec129OutLblId": vLdpNgFec129OutLblId,
       "vLdpNgFec129OutLabel": vLdpNgFec129OutLabel,
       "vLdpNgFec129OutLabelStatus": vLdpNgFec129OutLabelStatus,
       "vLdpNgFec129OutLblMTU": vLdpNgFec129OutLblMTU,
       "vLdpNgFec129OutLblVlanTag": vLdpNgFec129OutLblVlanTag,
       "vLdpNgFec129OutLblMaxCellConcat": vLdpNgFec129OutLblMaxCellConcat,
       "vLdpNgFec129OutLblSigStatus": vLdpNgFec129OutLblSigStatus,
       "vLdpNgFec129OutLblIPv4Cap": vLdpNgFec129OutLblIPv4Cap,
       "vLdpNgFec129OutLblIPv6Cap": vLdpNgFec129OutLblIPv6Cap,
       "vLdpNgFec129OutLblIPv4CeAddrType": vLdpNgFec129OutLblIPv4CeAddrType,
       "vLdpNgFec129OutLblIPv4CeIpAddr": vLdpNgFec129OutLblIPv4CeIpAddr,
       "vLdpNgFec129OutLblFLTxCap": vLdpNgFec129OutLblFLTxCap,
       "vLdpNgFec129OutLblFLRxCap": vLdpNgFec129OutLblFLRxCap,
       "vLdpNgFec129OutLblVccvCV": vLdpNgFec129OutLblVccvCV,
       "vLdpNgFec129OutLblVccvCC": vLdpNgFec129OutLblVccvCC,
       "vLdpNgFec129OutLblPwStatus": vLdpNgFec129OutLblPwStatus,
       "vLdpNgCepTdmFec128InLblTable": vLdpNgCepTdmFec128InLblTable,
       "vLdpNgCepTdmFec128InLblEntry": vLdpNgCepTdmFec128InLblEntry,
       "vLdpNgCepTdmFec128InLblPayldSize": vLdpNgCepTdmFec128InLblPayldSize,
       "vLdpNgCepTdmFec128InLblBitrate": vLdpNgCepTdmFec128InLblBitrate,
       "vLdpNgCepTdmFec128InLblRtpHeader": vLdpNgCepTdmFec128InLblRtpHeader,
       "vLdpNgCepTdmFec128InLblDiffTStmp": vLdpNgCepTdmFec128InLblDiffTStmp,
       "vLdpNgCepTdmFec128InLblSigPkts": vLdpNgCepTdmFec128InLblSigPkts,
       "vLdpNgCepTdmFec128InLblCasTrunk": vLdpNgCepTdmFec128InLblCasTrunk,
       "vLdpNgCepTdmFec128InLblTStmpFreq": vLdpNgCepTdmFec128InLblTStmpFreq,
       "vLdpNgCepTdmFec128InLblPayldType": vLdpNgCepTdmFec128InLblPayldType,
       "vLdpNgCepTdmFec128InLblSsrcId": vLdpNgCepTdmFec128InLblSsrcId,
       "vLdpNgCepTdmFec128OutLblTable": vLdpNgCepTdmFec128OutLblTable,
       "vLdpNgCepTdmFec128OutLblEntry": vLdpNgCepTdmFec128OutLblEntry,
       "vLdpNgCepTdmFec128OutLblPyldSze": vLdpNgCepTdmFec128OutLblPyldSze,
       "vLdpNgCepTdmFec128OutLblBitrate": vLdpNgCepTdmFec128OutLblBitrate,
       "vLdpNgCepTdmFec128OutLblRtpHdr": vLdpNgCepTdmFec128OutLblRtpHdr,
       "vLdpNgCepTdmFec128OutLblDfTstmp": vLdpNgCepTdmFec128OutLblDfTstmp,
       "vLdpNgCepTdmFec128OutLblSigPkts": vLdpNgCepTdmFec128OutLblSigPkts,
       "vLdpNgCepTdmFec128OutLblCasTrnk": vLdpNgCepTdmFec128OutLblCasTrnk,
       "vLdpNgCepTdmFec128OutLblTstmpFq": vLdpNgCepTdmFec128OutLblTstmpFq,
       "vLdpNgCepTdmFec128OutLblPyldTyp": vLdpNgCepTdmFec128OutLblPyldTyp,
       "vLdpNgCepTdmFec128OutLblSsrcId": vLdpNgCepTdmFec128OutLblSsrcId,
       "vLdpNgCepTdmFec129InLblTable": vLdpNgCepTdmFec129InLblTable,
       "vLdpNgCepTdmFec129InLblEntry": vLdpNgCepTdmFec129InLblEntry,
       "vLdpNgCepTdmFec129InLblPayldSize": vLdpNgCepTdmFec129InLblPayldSize,
       "vLdpNgCepTdmFec129InLblBitrate": vLdpNgCepTdmFec129InLblBitrate,
       "vLdpNgCepTdmFec129InLblRtpHeader": vLdpNgCepTdmFec129InLblRtpHeader,
       "vLdpNgCepTdmFec129InLblDiffTStmp": vLdpNgCepTdmFec129InLblDiffTStmp,
       "vLdpNgCepTdmFec129InLblSigPkts": vLdpNgCepTdmFec129InLblSigPkts,
       "vLdpNgCepTdmFec129InLblCasTrunk": vLdpNgCepTdmFec129InLblCasTrunk,
       "vLdpNgCepTdmFec129InLblTStmpFreq": vLdpNgCepTdmFec129InLblTStmpFreq,
       "vLdpNgCepTdmFec129InLblPayldType": vLdpNgCepTdmFec129InLblPayldType,
       "vLdpNgCepTdmFec129InLblSsrcId": vLdpNgCepTdmFec129InLblSsrcId,
       "vLdpNgCepTdmFec129OutLblTable": vLdpNgCepTdmFec129OutLblTable,
       "vLdpNgCepTdmFec129OutLblEntry": vLdpNgCepTdmFec129OutLblEntry,
       "vLdpNgCepTdmFec129OutLblPyldSize": vLdpNgCepTdmFec129OutLblPyldSize,
       "vLdpNgCepTdmFec129OutLblBitrate": vLdpNgCepTdmFec129OutLblBitrate,
       "vLdpNgCepTdmFec129OutLblRtpHdr": vLdpNgCepTdmFec129OutLblRtpHdr,
       "vLdpNgCepTdmFec129OutLblDifTStmp": vLdpNgCepTdmFec129OutLblDifTStmp,
       "vLdpNgCepTdmFec129OutLblSigPkts": vLdpNgCepTdmFec129OutLblSigPkts,
       "vLdpNgCepTdmFec129OutLblCasTrnk": vLdpNgCepTdmFec129OutLblCasTrnk,
       "vLdpNgCepTdmFec129OutLblTStmpFrq": vLdpNgCepTdmFec129OutLblTStmpFrq,
       "vLdpNgCepTdmFec129OutLblPyldType": vLdpNgCepTdmFec129OutLblPyldType,
       "vLdpNgCepTdmFec129OutLblSsrcId": vLdpNgCepTdmFec129OutLblSsrcId,
       "vRtrLdpNgStaticFecTableLstCh": vRtrLdpNgStaticFecTableLstCh,
       "vRtrLdpNgStaticFecTable": vRtrLdpNgStaticFecTable,
       "vRtrLdpNgStaticFecEntry": vRtrLdpNgStaticFecEntry,
       "vRtrLdpNgStaticFecIpPrefixType": vRtrLdpNgStaticFecIpPrefixType,
       "vRtrLdpNgStaticFecIpPrefix": vRtrLdpNgStaticFecIpPrefix,
       "vRtrLdpNgStaticFecIpPrefixLen": vRtrLdpNgStaticFecIpPrefixLen,
       "vRtrLdpNgStaticFecRowStatus": vRtrLdpNgStaticFecRowStatus,
       "vRtrLdpNgStaticFecNumInLabel": vRtrLdpNgStaticFecNumInLabel,
       "vRtrLdpNgStaticFecNumOutLabel": vRtrLdpNgStaticFecNumOutLabel,
       "vRtrLdpNgStaticFecInLabelTable": vRtrLdpNgStaticFecInLabelTable,
       "vRtrLdpNgStaticFecInLabelEntry": vRtrLdpNgStaticFecInLabelEntry,
       "vRtrLdpNgSFecInLabel": vRtrLdpNgSFecInLabel,
       "vRtrLdpNgSFecInLabelRowStatus": vRtrLdpNgSFecInLabelRowStatus,
       "vRtrLdpNgSFecOperInLabel": vRtrLdpNgSFecOperInLabel,
       "vRtrLdpNgStaticFecOutLabelTable": vRtrLdpNgStaticFecOutLabelTable,
       "vRtrLdpNgStaticFecOutLabelEntry": vRtrLdpNgStaticFecOutLabelEntry,
       "vRtrLdpNgSFecOutLabelType": vRtrLdpNgSFecOutLabelType,
       "vRtrLdpNgSFecOutLabelIfName": vRtrLdpNgSFecOutLabelIfName,
       "vRtrLdpNgSFecOutLabelIpAddrType": vRtrLdpNgSFecOutLabelIpAddrType,
       "vRtrLdpNgSFecOutLabelIpAddr": vRtrLdpNgSFecOutLabelIpAddr,
       "vRtrLdpNgSFecOutLabelRowStatus": vRtrLdpNgSFecOutLabelRowStatus,
       "vRtrLdpNgSFecOutLabel": vRtrLdpNgSFecOutLabel,
       "vRtrLdpNgTargPeerTableLstCh": vRtrLdpNgTargPeerTableLstCh,
       "vRtrLdpNgTargPeerTable": vRtrLdpNgTargPeerTable,
       "vRtrLdpNgTargPeerEntry": vRtrLdpNgTargPeerEntry,
       "vRtrLdpNgPeerAddressType": vRtrLdpNgPeerAddressType,
       "vRtrLdpNgPeerAddress": vRtrLdpNgPeerAddress,
       "vRtrLdpNgTargPeerRowStatus": vRtrLdpNgTargPeerRowStatus,
       "vRtrLdpNgTargPeerLastChange": vRtrLdpNgTargPeerLastChange,
       "vRtrLdpNgTargPeerAdminState": vRtrLdpNgTargPeerAdminState,
       "vRtrLdpNgTargPeerOperState": vRtrLdpNgTargPeerOperState,
       "vRtrLdpNgTargPeerUpTime": vRtrLdpNgTargPeerUpTime,
       "vRtrLdpNgTargPeerOperDownReason": vRtrLdpNgTargPeerOperDownReason,
       "vRtrLdpNgTargPeerInheritance": vRtrLdpNgTargPeerInheritance,
       "vRtrLdpNgTargPeerKAFactor": vRtrLdpNgTargPeerKAFactor,
       "vRtrLdpNgTargPeerKATimeout": vRtrLdpNgTargPeerKATimeout,
       "vRtrLdpNgTargPeerHelloFactor": vRtrLdpNgTargPeerHelloFactor,
       "vRtrLdpNgTargPeerHelloTimeout": vRtrLdpNgTargPeerHelloTimeout,
       "vRtrLdpNgTargPeerOprHelloTimeout": vRtrLdpNgTargPeerOprHelloTimeout,
       "vRtrLdpNgTargPeerHelloReduction": vRtrLdpNgTargPeerHelloReduction,
       "vRtrLdpNgTargPeerHelloRdctnFctr": vRtrLdpNgTargPeerHelloRdctnFctr,
       "vRtrLdpNgTargPeerBackoffTime": vRtrLdpNgTargPeerBackoffTime,
       "vRtrLdpNgTargPeerMaxBackoffTime": vRtrLdpNgTargPeerMaxBackoffTime,
       "vRtrLdpNgTargPeerTunneling": vRtrLdpNgTargPeerTunneling,
       "vRtrLdpNgTargPeerBfdEnabled": vRtrLdpNgTargPeerBfdEnabled,
       "vRtrLdpNgTargPeerLsrIfIndex": vRtrLdpNgTargPeerLsrIfIndex,
       "vRtrLdpNgTargPeerAutoCreate": vRtrLdpNgTargPeerAutoCreate,
       "vRtrLdpNgTargPeerCreator": vRtrLdpNgTargPeerCreator,
       "vRtrLdpNgTargPeerTemplName": vRtrLdpNgTargPeerTemplName,
       "vRtrLdpNgTargPeerStatsTable": vRtrLdpNgTargPeerStatsTable,
       "vRtrLdpNgTargPeerStatsEntry": vRtrLdpNgTargPeerStatsEntry,
       "vRtrLdpNgTargPeerStatExistingAdj": vRtrLdpNgTargPeerStatExistingAdj,
       "vRtrLdpNgInetIfTableLstCh": vRtrLdpNgInetIfTableLstCh,
       "vRtrLdpNgInetIfTable": vRtrLdpNgInetIfTable,
       "vRtrLdpNgInetIfEntry": vRtrLdpNgInetIfEntry,
       "vRtrLdpNgIfAddrType": vRtrLdpNgIfAddrType,
       "vRtrLdpNgInetIfRowStatus": vRtrLdpNgInetIfRowStatus,
       "vRtrLdpNgInetIfUpTime": vRtrLdpNgInetIfUpTime,
       "vRtrLdpNgInetIfLastChange": vRtrLdpNgInetIfLastChange,
       "vRtrLdpNgInetIfAdminState": vRtrLdpNgInetIfAdminState,
       "vRtrLdpNgInetIfOperState": vRtrLdpNgInetIfOperState,
       "vRtrLdpNgInetIfOperDownReason": vRtrLdpNgInetIfOperDownReason,
       "vRtrLdpNgInetIfInheritance": vRtrLdpNgInetIfInheritance,
       "vRtrLdpNgInetIfKAFactor": vRtrLdpNgInetIfKAFactor,
       "vRtrLdpNgInetIfKATimeout": vRtrLdpNgInetIfKATimeout,
       "vRtrLdpNgInetIfHelloFactor": vRtrLdpNgInetIfHelloFactor,
       "vRtrLdpNgInetIfHelloTimeout": vRtrLdpNgInetIfHelloTimeout,
       "vRtrLdpNgInetIfOperHelloTimeout": vRtrLdpNgInetIfOperHelloTimeout,
       "vRtrLdpNgInetIfBackoffTime": vRtrLdpNgInetIfBackoffTime,
       "vRtrLdpNgInetIfMaxBackoffTime": vRtrLdpNgInetIfMaxBackoffTime,
       "vRtrLdpNgInetIfTransAddrType": vRtrLdpNgInetIfTransAddrType,
       "vRtrLdpNgInetIfLsrIfType": vRtrLdpNgInetIfLsrIfType,
       "vRtrLdpNgInetIfLsrIfIndex": vRtrLdpNgInetIfLsrIfIndex,
       "vRtrLdpNgInetIfIPv4P2MPFecCap": vRtrLdpNgInetIfIPv4P2MPFecCap,
       "vRtrLdpNgInetIfIPv6P2MPFecCap": vRtrLdpNgInetIfIPv6P2MPFecCap,
       "vRtrLdpNgInetIfIPv4PfxFecCap": vRtrLdpNgInetIfIPv4PfxFecCap,
       "vRtrLdpNgInetIfIPv6PfxFecCap": vRtrLdpNgInetIfIPv6PfxFecCap,
       "vLdpNgStatsTable": vLdpNgStatsTable,
       "vLdpNgStatsEntry": vLdpNgStatsEntry,
       "vLdpNgStatsOperDownEvents": vLdpNgStatsOperDownEvents,
       "vLdpNgStatsIPv4ActiveSess": vLdpNgStatsIPv4ActiveSess,
       "vLdpNgStatsIPv6ActiveSess": vLdpNgStatsIPv6ActiveSess,
       "vLdpNgStatsIPv4ActiveLinkAdj": vLdpNgStatsIPv4ActiveLinkAdj,
       "vLdpNgStatsIPv6ActiveLinkAdj": vLdpNgStatsIPv6ActiveLinkAdj,
       "vLdpNgStatsIPv4ActiveTargAdj": vLdpNgStatsIPv4ActiveTargAdj,
       "vLdpNgStatsIPv6ActiveTargAdj": vLdpNgStatsIPv6ActiveTargAdj,
       "vLdpNgStatsIPv4ActiveIf": vLdpNgStatsIPv4ActiveIf,
       "vLdpNgStatsIPv6ActiveIf": vLdpNgStatsIPv6ActiveIf,
       "vLdpNgStatsIPv4InactiveIf": vLdpNgStatsIPv4InactiveIf,
       "vLdpNgStatsIPv6InactiveIf": vLdpNgStatsIPv6InactiveIf,
       "vLdpNgStatsIPv4ActiveTargPeers": vLdpNgStatsIPv4ActiveTargPeers,
       "vLdpNgStatsIPv6ActiveTargPeers": vLdpNgStatsIPv6ActiveTargPeers,
       "vLdpNgStatsIPv4InactiveTargPeers": vLdpNgStatsIPv4InactiveTargPeers,
       "vLdpNgStatsIPv6InactiveTargPeers": vLdpNgStatsIPv6InactiveTargPeers,
       "vLdpNgStatsIPv4PfxFecRecv": vLdpNgStatsIPv4PfxFecRecv,
       "vLdpNgStatsIPv6PfxFecRecv": vLdpNgStatsIPv6PfxFecRecv,
       "vLdpNgStatsIPv4PfxFecSent": vLdpNgStatsIPv4PfxFecSent,
       "vLdpNgStatsIPv6PfxFecSent": vLdpNgStatsIPv6PfxFecSent,
       "vLdpNgStatsFec128FecSent": vLdpNgStatsFec128FecSent,
       "vLdpNgStatsFec128FecRecv": vLdpNgStatsFec128FecRecv,
       "vLdpNgStatsFec129FecSent": vLdpNgStatsFec129FecSent,
       "vLdpNgStatsFec129FecRecv": vLdpNgStatsFec129FecRecv,
       "vLdpNgStatsIPv4AttemptedSessions": vLdpNgStatsIPv4AttemptedSessions,
       "vLdpNgStatsIPv6AttemptedSessions": vLdpNgStatsIPv6AttemptedSessions,
       "vLdpNgStatsSessRejNoHelloErrs": vLdpNgStatsSessRejNoHelloErrs,
       "vLdpNgStatsSessRejAdvErrors": vLdpNgStatsSessRejAdvErrors,
       "vLdpNgStatsSessRejMaxPduErrs": vLdpNgStatsSessRejMaxPduErrs,
       "vLdpNgStatsSessRejLblRngeErrs": vLdpNgStatsSessRejLblRngeErrs,
       "vLdpNgStatsBadLdpIdErrors": vLdpNgStatsBadLdpIdErrors,
       "vLdpNgStatsBadPduLengthErrors": vLdpNgStatsBadPduLengthErrors,
       "vLdpNgStatsBadMsgLengthErrors": vLdpNgStatsBadMsgLengthErrors,
       "vLdpNgStatsBadTlvLengthErrors": vLdpNgStatsBadTlvLengthErrors,
       "vLdpNgStatsMalformedTlvErrors": vLdpNgStatsMalformedTlvErrors,
       "vLdpNgStatsKeepAliveExpErrors": vLdpNgStatsKeepAliveExpErrors,
       "vLdpNgStatsShutdownNotifRecv": vLdpNgStatsShutdownNotifRecv,
       "vLdpNgStatsShutdownNotifSent": vLdpNgStatsShutdownNotifSent,
       "vLdpNgStatsIPv4EgrFecPfxCount": vLdpNgStatsIPv4EgrFecPfxCount,
       "vLdpNgStatsIPv6EgrFecPfxCount": vLdpNgStatsIPv6EgrFecPfxCount,
       "vLdpNgStatsUnknownTlvErrors": vLdpNgStatsUnknownTlvErrors,
       "vLdpNgStatsIPv4P2MPFecSent": vLdpNgStatsIPv4P2MPFecSent,
       "vLdpNgStatsIPv6P2MPFecSent": vLdpNgStatsIPv6P2MPFecSent,
       "vLdpNgStatsIPv4P2MPFecRecv": vLdpNgStatsIPv4P2MPFecRecv,
       "vLdpNgStatsIPv6P2MPFecRecv": vLdpNgStatsIPv6P2MPFecRecv,
       "vLdpNgStatsIPv4PfxFecOLSessSent": vLdpNgStatsIPv4PfxFecOLSessSent,
       "vLdpNgStatsIPv6PfxFecOLSessSent": vLdpNgStatsIPv6PfxFecOLSessSent,
       "vLdpNgStatsIPv4PfxFecOLSessRecv": vLdpNgStatsIPv4PfxFecOLSessRecv,
       "vLdpNgStatsIPv6PfxFecOLSessRecv": vLdpNgStatsIPv6PfxFecOLSessRecv,
       "vLdpNgStatsIPv4P2MPFecOLSessSent": vLdpNgStatsIPv4P2MPFecOLSessSent,
       "vLdpNgStatsIPv6P2MPFecOLSessSent": vLdpNgStatsIPv6P2MPFecOLSessSent,
       "vLdpNgStatsIPv4P2MPFecOLSessRecv": vLdpNgStatsIPv4P2MPFecOLSessRecv,
       "vLdpNgStatsIPv6P2MPFecOLSessRecv": vLdpNgStatsIPv6P2MPFecOLSessRecv,
       "vLdpNgStatsFec128FecOLSessSent": vLdpNgStatsFec128FecOLSessSent,
       "vLdpNgStatsFec128FecOLSessRecv": vLdpNgStatsFec128FecOLSessRecv,
       "vLdpNgStatsFec129FecOLSessSent": vLdpNgStatsFec129FecOLSessSent,
       "vLdpNgStatsFec129FecOLSessRecv": vLdpNgStatsFec129FecOLSessRecv,
       "vLdpNgStatsIPv4OLoadInterfaces": vLdpNgStatsIPv4OLoadInterfaces,
       "vLdpNgStatsIPv6OLoadInterfaces": vLdpNgStatsIPv6OLoadInterfaces,
       "vLdpNgStatsIPv4OLoadTargPeers": vLdpNgStatsIPv4OLoadTargPeers,
       "vLdpNgStatsIPv6OLoadTargPeers": vLdpNgStatsIPv6OLoadTargPeers,
       "vLdpNgStatsIPv4PfxFecInOLoad": vLdpNgStatsIPv4PfxFecInOLoad,
       "vLdpNgStatsIPv6PfxFecInOLoad": vLdpNgStatsIPv6PfxFecInOLoad,
       "vLdpNgStatsIPv4P2MPFecInOLoad": vLdpNgStatsIPv4P2MPFecInOLoad,
       "vLdpNgStatsIPv6P2MPFecInOLoad": vLdpNgStatsIPv6P2MPFecInOLoad,
       "vLdpNgStatsFec128FecInOLoad": vLdpNgStatsFec128FecInOLoad,
       "vLdpNgStatsFec129FecInOLoad": vLdpNgStatsFec129FecInOLoad,
       "vRtrLdpNgCapabilityTable": vRtrLdpNgCapabilityTable,
       "vRtrLdpNgCapabilityEntry": vRtrLdpNgCapabilityEntry,
       "vRtrLdpNgGenP2MPCapability": vRtrLdpNgGenP2MPCapability,
       "vRtrLdpNgGenMPMBBCapability": vRtrLdpNgGenMPMBBCapability,
       "vRtrLdpNgGenDynamicCapability": vRtrLdpNgGenDynamicCapability,
       "vRtrLdpNgGenOverloadCapability": vRtrLdpNgGenOverloadCapability,
       "vRtrLdpNgGenFec128Capability": vRtrLdpNgGenFec128Capability,
       "vRtrLdpNgGenFec129Capability": vRtrLdpNgGenFec129Capability,
       "vRtrLdpNgGenIPv4PfxFecCapability": vRtrLdpNgGenIPv4PfxFecCapability,
       "vRtrLdpNgGenIPv6PfxFecCapability": vRtrLdpNgGenIPv6PfxFecCapability,
       "vRtrLdpNgTcpSessParamsTableLstCh": vRtrLdpNgTcpSessParamsTableLstCh,
       "vRtrLdpNgTcpSessParamsTable": vRtrLdpNgTcpSessParamsTable,
       "vRtrLdpNgTcpSessParamsEntry": vRtrLdpNgTcpSessParamsEntry,
       "vRtrLdpNgTcpSessPeerAddrType": vRtrLdpNgTcpSessPeerAddrType,
       "vRtrLdpNgTcpSessPeerAddr": vRtrLdpNgTcpSessPeerAddr,
       "vRtrLdpNgTcpSessRowStatus": vRtrLdpNgTcpSessRowStatus,
       "vRtrLdpNgTcpSessAuth": vRtrLdpNgTcpSessAuth,
       "vRtrLdpNgTcpSessAuthKey": vRtrLdpNgTcpSessAuthKey,
       "vRtrLdpNgTcpSessAuthKeyChain": vRtrLdpNgTcpSessAuthKeyChain,
       "vRtrLdpNgTcpSessPMTUDiscovery": vRtrLdpNgTcpSessPMTUDiscovery,
       "vRtrLdpNgGeneralTableLstCh": vRtrLdpNgGeneralTableLstCh,
       "vRtrLdpNgGeneralTable": vRtrLdpNgGeneralTable,
       "vRtrLdpNgGeneralEntry": vRtrLdpNgGeneralEntry,
       "vRtrLdpNgGenCreateTime": vRtrLdpNgGenCreateTime,
       "vRtrLdpNgGenUpTime": vRtrLdpNgGenUpTime,
       "vRtrLdpNgGenRowLastCh": vRtrLdpNgGenRowLastCh,
       "vRtrLdpNgGenLastChange": vRtrLdpNgGenLastChange,
       "vRtrLdpNgGenAdminState": vRtrLdpNgGenAdminState,
       "vRtrLdpNgGenOperState": vRtrLdpNgGenOperState,
       "vRtrLdpNgGenOperDownReason": vRtrLdpNgGenOperDownReason,
       "vRtrLdpNgGenLdpIPv4LsrId": vRtrLdpNgGenLdpIPv4LsrId,
       "vRtrLdpNgGenLdpIPv6LsrId": vRtrLdpNgGenLdpIPv6LsrId,
       "vRtrLdpNgGenProtocolVersion": vRtrLdpNgGenProtocolVersion,
       "vRtrLdpNgGenBackoffTime": vRtrLdpNgGenBackoffTime,
       "vRtrLdpNgGenMaxBackoffTime": vRtrLdpNgGenMaxBackoffTime,
       "vRtrLdpNgGenTunnelDownDampTime": vRtrLdpNgGenTunnelDownDampTime,
       "vRtrLdpNgGenGracefulRestart": vRtrLdpNgGenGracefulRestart,
       "vRtrLdpNgGenGRNbrLiveTime": vRtrLdpNgGenGRNbrLiveTime,
       "vRtrLdpNgGenGRMaxRecoveryTime": vRtrLdpNgGenGRMaxRecoveryTime,
       "vRtrLdpNgGenLabelWithdrawalDelay": vRtrLdpNgGenLabelWithdrawalDelay,
       "vRtrLdpNgGenImplicitNull": vRtrLdpNgGenImplicitNull,
       "vRtrLdpNgGenShortTTLPropLocal": vRtrLdpNgGenShortTTLPropLocal,
       "vRtrLdpNgGenShortTTLPropTransit": vRtrLdpNgGenShortTTLPropTransit,
       "vRtrLdpNgGenMPMBBTime": vRtrLdpNgGenMPMBBTime,
       "vRtrLdpNgGenLdpFrr": vRtrLdpNgGenLdpFrr,
       "vRtrLdpNgGenMcastUpstreamFrr": vRtrLdpNgGenMcastUpstreamFrr,
       "vRtrLdpNgGenDeaggregateFec": vRtrLdpNgGenDeaggregateFec,
       "vRtrLdpNgGenControlMode": vRtrLdpNgGenControlMode,
       "vRtrLdpNgGenDistMethod": vRtrLdpNgGenDistMethod,
       "vRtrLdpNgGenRetentionMode": vRtrLdpNgGenRetentionMode,
       "vRtrLdpNgGenPropagatePolicy": vRtrLdpNgGenPropagatePolicy,
       "vRtrLdpNgGenLoopDetectCap": vRtrLdpNgGenLoopDetectCap,
       "vRtrLdpNgGenHopLimit": vRtrLdpNgGenHopLimit,
       "vRtrLdpNgGenPathVectorLimit": vRtrLdpNgGenPathVectorLimit,
       "vRtrLdpNgGenRoutePreference": vRtrLdpNgGenRoutePreference,
       "vRtrLdpNgPolicyTableLstCh": vRtrLdpNgPolicyTableLstCh,
       "vRtrLdpNgPolicyTable": vRtrLdpNgPolicyTable,
       "vRtrLdpNgPolicyEntry": vRtrLdpNgPolicyEntry,
       "vRtrLdpNgPolRowLastCh": vRtrLdpNgPolRowLastCh,
       "vRtrLdpNgPolImportPolicy1": vRtrLdpNgPolImportPolicy1,
       "vRtrLdpNgPolImportPolicy2": vRtrLdpNgPolImportPolicy2,
       "vRtrLdpNgPolImportPolicy3": vRtrLdpNgPolImportPolicy3,
       "vRtrLdpNgPolImportPolicy4": vRtrLdpNgPolImportPolicy4,
       "vRtrLdpNgPolImportPolicy5": vRtrLdpNgPolImportPolicy5,
       "vRtrLdpNgPolExportPolicy1": vRtrLdpNgPolExportPolicy1,
       "vRtrLdpNgPolExportPolicy2": vRtrLdpNgPolExportPolicy2,
       "vRtrLdpNgPolExportPolicy3": vRtrLdpNgPolExportPolicy3,
       "vRtrLdpNgPolExportPolicy4": vRtrLdpNgPolExportPolicy4,
       "vRtrLdpNgPolExportPolicy5": vRtrLdpNgPolExportPolicy5,
       "vRtrLdpNgPolTunlTblExportPolicy1": vRtrLdpNgPolTunlTblExportPolicy1,
       "vRtrLdpNgPolTunlTblExportPolicy2": vRtrLdpNgPolTunlTblExportPolicy2,
       "vRtrLdpNgPolTunlTblExportPolicy3": vRtrLdpNgPolTunlTblExportPolicy3,
       "vRtrLdpNgPolTunlTblExportPolicy4": vRtrLdpNgPolTunlTblExportPolicy4,
       "vRtrLdpNgPolTunlTblExportPolicy5": vRtrLdpNgPolTunlTblExportPolicy5,
       "vRtrLdpNgIfParamsTableLstCh": vRtrLdpNgIfParamsTableLstCh,
       "vRtrLdpNgIfParamsTable": vRtrLdpNgIfParamsTable,
       "vRtrLdpNgIfParamsEntry": vRtrLdpNgIfParamsEntry,
       "vRtrLdpNgIfParamRowLastCh": vRtrLdpNgIfParamRowLastCh,
       "vRtrLdpNgIfParamIPv4KAFactor": vRtrLdpNgIfParamIPv4KAFactor,
       "vRtrLdpNgIfParamIPv6KAFactor": vRtrLdpNgIfParamIPv6KAFactor,
       "vRtrLdpNgIfParamIPv4KATimeout": vRtrLdpNgIfParamIPv4KATimeout,
       "vRtrLdpNgIfParamIPv6KATimeout": vRtrLdpNgIfParamIPv6KATimeout,
       "vRtrLdpNgIfParamIPv4HelloFactor": vRtrLdpNgIfParamIPv4HelloFactor,
       "vRtrLdpNgIfParamIPv6HelloFactor": vRtrLdpNgIfParamIPv6HelloFactor,
       "vRtrLdpNgIfParamIPv4HelloTimeout": vRtrLdpNgIfParamIPv4HelloTimeout,
       "vRtrLdpNgIfParamIPv6HelloTimeout": vRtrLdpNgIfParamIPv6HelloTimeout,
       "vRtrLdpNgIfParamIPv4TransAddrTyp": vRtrLdpNgIfParamIPv4TransAddrTyp,
       "vRtrLdpNgIfParamIPv6TransAddrTyp": vRtrLdpNgIfParamIPv6TransAddrTyp,
       "vRtrLdpNgTargTableLstCh": vRtrLdpNgTargTableLstCh,
       "vRtrLdpNgTargTable": vRtrLdpNgTargTable,
       "vRtrLdpNgTargEntry": vRtrLdpNgTargEntry,
       "vRtrLdpNgTargRowLastCh": vRtrLdpNgTargRowLastCh,
       "vRtrLdpNgTargImportPolicy1": vRtrLdpNgTargImportPolicy1,
       "vRtrLdpNgTargImportPolicy2": vRtrLdpNgTargImportPolicy2,
       "vRtrLdpNgTargImportPolicy3": vRtrLdpNgTargImportPolicy3,
       "vRtrLdpNgTargImportPolicy4": vRtrLdpNgTargImportPolicy4,
       "vRtrLdpNgTargImportPolicy5": vRtrLdpNgTargImportPolicy5,
       "vRtrLdpNgTargExportPolicy1": vRtrLdpNgTargExportPolicy1,
       "vRtrLdpNgTargExportPolicy2": vRtrLdpNgTargExportPolicy2,
       "vRtrLdpNgTargExportPolicy3": vRtrLdpNgTargExportPolicy3,
       "vRtrLdpNgTargExportPolicy4": vRtrLdpNgTargExportPolicy4,
       "vRtrLdpNgTargExportPolicy5": vRtrLdpNgTargExportPolicy5,
       "vRtrLdpNgTargTunnelPreference": vRtrLdpNgTargTunnelPreference,
       "vRtrLdpNgTargetedSessions": vRtrLdpNgTargetedSessions,
       "vRtrLdpNgTargIPv4KAFactor": vRtrLdpNgTargIPv4KAFactor,
       "vRtrLdpNgTargIPv6KAFactor": vRtrLdpNgTargIPv6KAFactor,
       "vRtrLdpNgTargIPv4KATimeout": vRtrLdpNgTargIPv4KATimeout,
       "vRtrLdpNgTargIPv6KATimeout": vRtrLdpNgTargIPv6KATimeout,
       "vRtrLdpNgTargIPv4HelloFactor": vRtrLdpNgTargIPv4HelloFactor,
       "vRtrLdpNgTargIPv6HelloFactor": vRtrLdpNgTargIPv6HelloFactor,
       "vRtrLdpNgTargIPv4HelloTimeout": vRtrLdpNgTargIPv4HelloTimeout,
       "vRtrLdpNgTargIPv6HelloTimeout": vRtrLdpNgTargIPv6HelloTimeout,
       "vRtrLdpNgTargIPv4HelloReduction": vRtrLdpNgTargIPv4HelloReduction,
       "vRtrLdpNgTargIPv6HelloReduction": vRtrLdpNgTargIPv6HelloReduction,
       "vRtrLdpNgTargIPv4HelloReduceFctr": vRtrLdpNgTargIPv4HelloReduceFctr,
       "vRtrLdpNgTargIPv6HelloReduceFctr": vRtrLdpNgTargIPv6HelloReduceFctr,
       "vRtrLdpNgAggrPreMatchTableLstCh": vRtrLdpNgAggrPreMatchTableLstCh,
       "vRtrLdpNgAggrPreMatchTable": vRtrLdpNgAggrPreMatchTable,
       "vRtrLdpNgAggrPreMatchEntry": vRtrLdpNgAggrPreMatchEntry,
       "vRtrLdpNgAggrPreMatchRowLastCh": vRtrLdpNgAggrPreMatchRowLastCh,
       "vRtrLdpNgAggrPreMatchEnabled": vRtrLdpNgAggrPreMatchEnabled,
       "vRtrLdpNgAggrPreMatchExcPolicy1": vRtrLdpNgAggrPreMatchExcPolicy1,
       "vRtrLdpNgAggrPreMatchExcPolicy2": vRtrLdpNgAggrPreMatchExcPolicy2,
       "vRtrLdpNgAggrPreMatchExcPolicy3": vRtrLdpNgAggrPreMatchExcPolicy3,
       "vRtrLdpNgAggrPreMatchExcPolicy4": vRtrLdpNgAggrPreMatchExcPolicy4,
       "vRtrLdpNgAggrPreMatchExcPolicy5": vRtrLdpNgAggrPreMatchExcPolicy5,
       "vRtrLdpNgAggrPreMatchAdminState": vRtrLdpNgAggrPreMatchAdminState,
       "tmnxLdpNgNotifyPrefix": tmnxLdpNgNotifyPrefix,
       "tmnxLdpNgNotifications": tmnxLdpNgNotifications,
       "vRtrLdpNgSessMaxFecThresReached": vRtrLdpNgSessMaxFecThresReached}
)
