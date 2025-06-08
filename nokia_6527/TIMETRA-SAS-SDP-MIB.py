# SNMP MIB module (TIMETRA-SAS-SDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-SDP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:16 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(TFilterID,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterID")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(tmnxSASServConformance,) = mibBuilder.importSymbols(
    "TIMETRA-SAS-SERV-MIB",
    "tmnxSASServConformance")

(sdpBindBaseStatsEntry,
 sdpBindEntry) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindBaseStatsEntry",
    "sdpBindEntry")

(BridgeId,
 ConfigStatus,
 L2RouteOrigin,
 L2ptProtocols,
 LspIdList,
 MvplsPruneState,
 PWTemplateId,
 SdpBFHundredthsOfPercent,
 SdpBindBandwidth,
 SdpBindVcType,
 SdpId,
 ServObjDesc,
 ServObjName,
 StpExceptionCondition,
 StpPortRole,
 StpProtocol,
 TStpPortState,
 TdmOptionsCasTrunkFraming,
 TdmOptionsSigPkts,
 TlsLimitMacMove,
 TlsLimitMacMoveLevel,
 VpnId,
 custId,
 svcDhcpClientLease,
 svcDhcpCoAError,
 svcDhcpLseStateNewChAddr,
 svcDhcpLseStateNewCiAddr,
 svcDhcpLseStateOldChAddr,
 svcDhcpLseStateOldCiAddr,
 svcDhcpLseStatePopulateError,
 svcDhcpPacketProblem,
 svcDhcpProxyError,
 svcDhcpSubAuthError,
 svcId,
 svcTlsMacMoveMaxRate,
 svcTlsStpDesignatedRoot,
 svcVpnId,
 tlsDhcpPacketProblem,
 tmnxCustomerBridgeId,
 tmnxCustomerRootBridgeId,
 tmnxOldSdpBindTlsStpPortState,
 tmnxOtherBridgeId,
 tmnxServConformance,
 tmnxServNotifications,
 tmnxServObjs,
 tmnxSvcObjs,
 tstpTraps) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "BridgeId",
    "ConfigStatus",
    "L2RouteOrigin",
    "L2ptProtocols",
    "LspIdList",
    "MvplsPruneState",
    "PWTemplateId",
    "SdpBFHundredthsOfPercent",
    "SdpBindBandwidth",
    "SdpBindVcType",
    "SdpId",
    "ServObjDesc",
    "ServObjName",
    "StpExceptionCondition",
    "StpPortRole",
    "StpProtocol",
    "TStpPortState",
    "TdmOptionsCasTrunkFraming",
    "TdmOptionsSigPkts",
    "TlsLimitMacMove",
    "TlsLimitMacMoveLevel",
    "VpnId",
    "custId",
    "svcDhcpClientLease",
    "svcDhcpCoAError",
    "svcDhcpLseStateNewChAddr",
    "svcDhcpLseStateNewCiAddr",
    "svcDhcpLseStateOldChAddr",
    "svcDhcpLseStateOldCiAddr",
    "svcDhcpLseStatePopulateError",
    "svcDhcpPacketProblem",
    "svcDhcpProxyError",
    "svcDhcpSubAuthError",
    "svcId",
    "svcTlsMacMoveMaxRate",
    "svcTlsStpDesignatedRoot",
    "svcVpnId",
    "tlsDhcpPacketProblem",
    "tmnxCustomerBridgeId",
    "tmnxCustomerRootBridgeId",
    "tmnxOldSdpBindTlsStpPortState",
    "tmnxOtherBridgeId",
    "tmnxServConformance",
    "tmnxServNotifications",
    "tmnxServObjs",
    "tmnxSvcObjs",
    "tstpTraps")

(SdpBindId,
 ServiceAdminStatus,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxActionType,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxIgmpVersion,
 TmnxOperState,
 TmnxServId,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "SdpBindId",
    "ServiceAdminStatus",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxActionType",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxIgmpVersion",
    "TmnxOperState",
    "TmnxServId",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrMplsLspID")


# MODULE-IDENTITY

timetraSASServicesSdpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    timetraSASServicesSdpMIBModule.setRevisions(
        ("1907-10-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASSdpConformance_ObjectIdentity = ObjectIdentity
tmnxSASSdpConformance = _TmnxSASSdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 13)
)
_TmnxSASSdpCompliances_ObjectIdentity = ObjectIdentity
tmnxSASSdpCompliances = _TmnxSASSdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 13, 1)
)
_TmnxSASSdpGroups_ObjectIdentity = ObjectIdentity
tmnxSASSdpGroups = _TmnxSASSdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 13, 2)
)
_TmnxSASSdpObjs_ObjectIdentity = ObjectIdentity
tmnxSASSdpObjs = _TmnxSASSdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 12)
)
_SdpBindExtnTable_Object = MibTable
sdpBindExtnTable = _SdpBindExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 12, 4)
)
if mibBuilder.loadTexts:
    sdpBindExtnTable.setStatus("current")
_SdpBindExtnEntry_Object = MibTableRow
sdpBindExtnEntry = _SdpBindExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 12, 4, 1)
)
if mibBuilder.loadTexts:
    sdpBindExtnEntry.setStatus("current")


class _SdpBindIngressExtraVlanTagDropCount_Type(TruthValue):
    """Custom type sdpBindIngressExtraVlanTagDropCount based on TruthValue"""
    defaultValue = 2


_SdpBindIngressExtraVlanTagDropCount_Type.__name__ = "TruthValue"
_SdpBindIngressExtraVlanTagDropCount_Object = MibTableColumn
sdpBindIngressExtraVlanTagDropCount = _SdpBindIngressExtraVlanTagDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 12, 4, 1, 1),
    _SdpBindIngressExtraVlanTagDropCount_Type()
)
sdpBindIngressExtraVlanTagDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressExtraVlanTagDropCount.setStatus("current")
_SdpBindBaseStatsExtnTable_Object = MibTable
sdpBindBaseStatsExtnTable = _SdpBindBaseStatsExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 12, 5)
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsExtnTable.setStatus("current")
_SdpBindBaseStatsExtnEntry_Object = MibTableRow
sdpBindBaseStatsExtnEntry = _SdpBindBaseStatsExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 12, 5, 1)
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsExtnEntry.setStatus("current")
_SdpBindIngressExtraVlanTagDroppedPackets_Type = Counter64
_SdpBindIngressExtraVlanTagDroppedPackets_Object = MibTableColumn
sdpBindIngressExtraVlanTagDroppedPackets = _SdpBindIngressExtraVlanTagDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 12, 5, 1, 1),
    _SdpBindIngressExtraVlanTagDroppedPackets_Type()
)
sdpBindIngressExtraVlanTagDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIngressExtraVlanTagDroppedPackets.setStatus("current")
_SdpBindIngressExtraVlanTagDroppedOctets_Type = Counter64
_SdpBindIngressExtraVlanTagDroppedOctets_Object = MibTableColumn
sdpBindIngressExtraVlanTagDroppedOctets = _SdpBindIngressExtraVlanTagDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 12, 5, 1, 2),
    _SdpBindIngressExtraVlanTagDroppedOctets_Type()
)
sdpBindIngressExtraVlanTagDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIngressExtraVlanTagDroppedOctets.setStatus("current")
sdpBindEntry.registerAugmentions(
    ("TIMETRA-SAS-SDP-MIB",
     "sdpBindExtnEntry")
)
sdpBindExtnEntry.setIndexNames(*sdpBindEntry.getIndexNames())
sdpBindBaseStatsEntry.registerAugmentions(
    ("TIMETRA-SAS-SDP-MIB",
     "sdpBindBaseStatsExtnEntry")
)
sdpBindBaseStatsExtnEntry.setIndexNames(*sdpBindBaseStatsEntry.getIndexNames())

# Managed Objects groups

tmnxSASSdpV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 13, 2, 1)
)
tmnxSASSdpV3v0Group.setObjects(
      *(("TIMETRA-SAS-SDP-MIB", "sdpBindIngressExtraVlanTagDropCount"),
        ("TIMETRA-SAS-SDP-MIB", "sdpBindIngressExtraVlanTagDroppedPackets"),
        ("TIMETRA-SAS-SDP-MIB", "sdpBindIngressExtraVlanTagDroppedOctets"))
)
if mibBuilder.loadTexts:
    tmnxSASSdpV3v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxSASSdp7210V3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 13, 1, 1)
)
tmnxSASSdp7210V3v0Compliance.setObjects(
    ("TIMETRA-SAS-SDP-MIB", "tmnxSASSdpV3v0Group")
)
if mibBuilder.loadTexts:
    tmnxSASSdp7210V3v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-SDP-MIB",
    **{"timetraSASServicesSdpMIBModule": timetraSASServicesSdpMIBModule,
       "tmnxSASSdpConformance": tmnxSASSdpConformance,
       "tmnxSASSdpCompliances": tmnxSASSdpCompliances,
       "tmnxSASSdp7210V3v0Compliance": tmnxSASSdp7210V3v0Compliance,
       "tmnxSASSdpGroups": tmnxSASSdpGroups,
       "tmnxSASSdpV3v0Group": tmnxSASSdpV3v0Group,
       "tmnxSASSdpObjs": tmnxSASSdpObjs,
       "sdpBindExtnTable": sdpBindExtnTable,
       "sdpBindExtnEntry": sdpBindExtnEntry,
       "sdpBindIngressExtraVlanTagDropCount": sdpBindIngressExtraVlanTagDropCount,
       "sdpBindBaseStatsExtnTable": sdpBindBaseStatsExtnTable,
       "sdpBindBaseStatsExtnEntry": sdpBindBaseStatsExtnEntry,
       "sdpBindIngressExtraVlanTagDroppedPackets": sdpBindIngressExtraVlanTagDroppedPackets,
       "sdpBindIngressExtraVlanTagDroppedOctets": sdpBindIngressExtraVlanTagDroppedOctets}
)
