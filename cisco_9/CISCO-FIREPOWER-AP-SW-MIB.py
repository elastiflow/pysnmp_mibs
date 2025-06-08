# SNMP MIB module (CISCO-FIREPOWER-AP-SW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-SW-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:39 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApConditionRemoteInvRslt,
 CfprApDpsecForgedTransmit,
 CfprApFabricAVlanAssocPrimaryVlanSwitchId,
 CfprApFabricAVlanSharing,
 CfprApFabricAVlanTransport,
 CfprApFabricAVlanType,
 CfprApFabricAVsanTransport,
 CfprApFabricAVsanType,
 CfprApFabricAdminState,
 CfprApFabricDefaultZoningState,
 CfprApFabricEpVlanVlanType,
 CfprApFabricEthEstcPortMode,
 CfprApFabricEthPcProtocol,
 CfprApFabricExternalEpLocale,
 CfprApFabricFcZoneSharingMode,
 CfprApFabricFillPattern,
 CfprApFabricLacpMode,
 CfprApFabricPIoEpIfType,
 CfprApFabricPIoEpOperState,
 CfprApFabricPIoEpPortId,
 CfprApFabricPIoEpSlotId,
 CfprApFabricPktCaptureAppendFlag,
 CfprApFabricPort,
 CfprApFabricQosPrio,
 CfprApFabricRecoveryAction,
 CfprApFabricSpannedCluster,
 CfprApFabricTrafficDirection,
 CfprApFabricVlanAssocPrimaryVlanState,
 CfprApFabricVlanOperState,
 CfprApFabricVlanOverlapState,
 CfprApFabricVnetEpIfRole,
 CfprApFabricVnetEpLocale,
 CfprApFabricVnetEpPolicyOwner,
 CfprApFabricVsanOperState,
 CfprApFabricWarnings,
 CfprApFabricZoningState,
 CfprApFlowctrlFlowControl,
 CfprApFlowctrlPriorityPause,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApFsmLifecycle,
 CfprApLicenseState,
 CfprApLsFcZoneState,
 CfprApNetworkConnectionType,
 CfprApNetworkLocale,
 CfprApNetworkPortRole,
 CfprApNetworkSwitchId,
 CfprApNetworkTransport,
 CfprApNetworkVlanCountStatus,
 CfprApNetworkVnetEpIfType,
 CfprApNwctrlAdminState,
 CfprApNwctrlLinkFailAction,
 CfprApPortDuplex,
 CfprApPortEthSpeed,
 CfprApPortSpeed,
 CfprApSwAccessDomainFsmCurrentFsm,
 CfprApSwAccessDomainFsmStageName,
 CfprApSwAccessDomainFsmTaskItem,
 CfprApSwAccessDomainLocale,
 CfprApSwAccessDomainType,
 CfprApSwAccessEpLocale,
 CfprApSwAccessEpTransport,
 CfprApSwAdminState,
 CfprApSwBorderDomainLocale,
 CfprApSwBorderEpLocale,
 CfprApSwBorderPcLocale,
 CfprApSwBreakoutType,
 CfprApSwCIoEpIfType,
 CfprApSwCardEnvStatsHistThresholded,
 CfprApSwCardEnvStatsThresholded,
 CfprApSwCimcId,
 CfprApSwConfMode,
 CfprApSwConfigStatus,
 CfprApSwEnvStatsHistThresholded,
 CfprApSwEnvStatsThresholded,
 CfprApSwEstcEpLocale,
 CfprApSwEthEstcEpTransport,
 CfprApSwEthEstcPcTransport,
 CfprApSwEthLanBorderFsmCurrentFsm,
 CfprApSwEthLanBorderFsmStageName,
 CfprApSwEthLanBorderFsmTaskFlags,
 CfprApSwEthLanBorderFsmTaskItem,
 CfprApSwEthLanBorderTransport,
 CfprApSwEthLanEpTransport,
 CfprApSwEthLanEpUdldAdminState,
 CfprApSwEthLanEpUdldMode,
 CfprApSwEthLanMonTransport,
 CfprApSwEthLanPcTransport,
 CfprApSwEthMonDestEpTransport,
 CfprApSwEthMonFsmCurrentFsm,
 CfprApSwEthMonFsmStageName,
 CfprApSwEthMonFsmTaskItem,
 CfprApSwEthMonSrcEpTransport,
 CfprApSwEthMonTransport,
 CfprApSwEthMonType,
 CfprApSwEthTargetEpAdminState,
 CfprApSwEthTargetEpTransport,
 CfprApSwExtUtilityFsmCurrentFsm,
 CfprApSwExtUtilityFsmStageName,
 CfprApSwExtUtilityFsmTaskItem,
 CfprApSwFabricRole,
 CfprApSwFabricZoneNsAllocStatus,
 CfprApSwFcSanBorderFsmCurrentFsm,
 CfprApSwFcSanBorderFsmStageName,
 CfprApSwFcSanBorderFsmTaskItem,
 CfprApSwFcSanBorderTransport,
 CfprApSwFcSanBorderUplinkTrunking,
 CfprApSwFcSanEpTransport,
 CfprApSwFcSanPcTransport,
 CfprApSwFcServerZoneGroupLc,
 CfprApSwFcZoneLc,
 CfprApSwFcZoneMemberLc,
 CfprApSwFcZoneSetLc,
 CfprApSwFcoeSanEpTransport,
 CfprApSwFcoeSanEpUdldAdminState,
 CfprApSwFcoeSanEpUdldMode,
 CfprApSwFcoeSanPcTransport,
 CfprApSwLanBorderType,
 CfprApSwLanEpIfRole,
 CfprApSwLanEpType,
 CfprApSwLanMonType,
 CfprApSwLanPcIfRole,
 CfprApSwLanPcType,
 CfprApSwMonAdminState,
 CfprApSwMonDomainLocale,
 CfprApSwMonLifeCycle,
 CfprApSwMonSrcEpLocale,
 CfprApSwPIoEpIfType,
 CfprApSwPIoEpLc,
 CfprApSwPeerStatus,
 CfprApSwPhysFsmCurrentFsm,
 CfprApSwPhysFsmStageName,
 CfprApSwPhysFsmTaskItem,
 CfprApSwPktCaptureLifeCycle,
 CfprApSwPortBreakoutPortId,
 CfprApSwPortBreakoutSlotId,
 CfprApSwSanBorderType,
 CfprApSwSanEpIfRole,
 CfprApSwSanEpType,
 CfprApSwSanPcIfRole,
 CfprApSwSanPcType,
 CfprApSwSspEthLanMonTransport,
 CfprApSwSspEthMonFsmCurrentFsm,
 CfprApSwSspEthMonFsmStageName,
 CfprApSwSspEthMonFsmTaskItem,
 CfprApSwSspEthMonSrcPhyEpFsmCurrentFsm,
 CfprApSwSspEthMonSrcPhyEpFsmStageName,
 CfprApSwSspEthMonSrcPhyEpFsmTaskItem,
 CfprApSwSspEthMonTransport,
 CfprApSwSspEthMonType,
 CfprApSwSspLanMonType,
 CfprApSwSspMonAdminState,
 CfprApSwSspMonDelPcap,
 CfprApSwSspMonDomainLocale,
 CfprApSwSubGroupAggrPortId,
 CfprApSwSubGroupSlotId,
 CfprApSwSystemStatsHistThresholded,
 CfprApSwSystemStatsThresholded,
 CfprApSwTargetEpType,
 CfprApSwUlanPurpose,
 CfprApSwUtilityDomainFsmCurrentFsm,
 CfprApSwUtilityDomainFsmStageName,
 CfprApSwUtilityDomainFsmTaskItem,
 CfprApSwUtilityDomainLocale,
 CfprApSwUtilityDomainType,
 CfprApSwVlanCompType,
 CfprApSwVlanConfigStatusType,
 CfprApSwVlanGroupType,
 CfprApSwVlanLc,
 CfprApSwVlanPortNsAllocStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApConditionRemoteInvRslt",
    "CfprApDpsecForgedTransmit",
    "CfprApFabricAVlanAssocPrimaryVlanSwitchId",
    "CfprApFabricAVlanSharing",
    "CfprApFabricAVlanTransport",
    "CfprApFabricAVlanType",
    "CfprApFabricAVsanTransport",
    "CfprApFabricAVsanType",
    "CfprApFabricAdminState",
    "CfprApFabricDefaultZoningState",
    "CfprApFabricEpVlanVlanType",
    "CfprApFabricEthEstcPortMode",
    "CfprApFabricEthPcProtocol",
    "CfprApFabricExternalEpLocale",
    "CfprApFabricFcZoneSharingMode",
    "CfprApFabricFillPattern",
    "CfprApFabricLacpMode",
    "CfprApFabricPIoEpIfType",
    "CfprApFabricPIoEpOperState",
    "CfprApFabricPIoEpPortId",
    "CfprApFabricPIoEpSlotId",
    "CfprApFabricPktCaptureAppendFlag",
    "CfprApFabricPort",
    "CfprApFabricQosPrio",
    "CfprApFabricRecoveryAction",
    "CfprApFabricSpannedCluster",
    "CfprApFabricTrafficDirection",
    "CfprApFabricVlanAssocPrimaryVlanState",
    "CfprApFabricVlanOperState",
    "CfprApFabricVlanOverlapState",
    "CfprApFabricVnetEpIfRole",
    "CfprApFabricVnetEpLocale",
    "CfprApFabricVnetEpPolicyOwner",
    "CfprApFabricVsanOperState",
    "CfprApFabricWarnings",
    "CfprApFabricZoningState",
    "CfprApFlowctrlFlowControl",
    "CfprApFlowctrlPriorityPause",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApFsmLifecycle",
    "CfprApLicenseState",
    "CfprApLsFcZoneState",
    "CfprApNetworkConnectionType",
    "CfprApNetworkLocale",
    "CfprApNetworkPortRole",
    "CfprApNetworkSwitchId",
    "CfprApNetworkTransport",
    "CfprApNetworkVlanCountStatus",
    "CfprApNetworkVnetEpIfType",
    "CfprApNwctrlAdminState",
    "CfprApNwctrlLinkFailAction",
    "CfprApPortDuplex",
    "CfprApPortEthSpeed",
    "CfprApPortSpeed",
    "CfprApSwAccessDomainFsmCurrentFsm",
    "CfprApSwAccessDomainFsmStageName",
    "CfprApSwAccessDomainFsmTaskItem",
    "CfprApSwAccessDomainLocale",
    "CfprApSwAccessDomainType",
    "CfprApSwAccessEpLocale",
    "CfprApSwAccessEpTransport",
    "CfprApSwAdminState",
    "CfprApSwBorderDomainLocale",
    "CfprApSwBorderEpLocale",
    "CfprApSwBorderPcLocale",
    "CfprApSwBreakoutType",
    "CfprApSwCIoEpIfType",
    "CfprApSwCardEnvStatsHistThresholded",
    "CfprApSwCardEnvStatsThresholded",
    "CfprApSwCimcId",
    "CfprApSwConfMode",
    "CfprApSwConfigStatus",
    "CfprApSwEnvStatsHistThresholded",
    "CfprApSwEnvStatsThresholded",
    "CfprApSwEstcEpLocale",
    "CfprApSwEthEstcEpTransport",
    "CfprApSwEthEstcPcTransport",
    "CfprApSwEthLanBorderFsmCurrentFsm",
    "CfprApSwEthLanBorderFsmStageName",
    "CfprApSwEthLanBorderFsmTaskFlags",
    "CfprApSwEthLanBorderFsmTaskItem",
    "CfprApSwEthLanBorderTransport",
    "CfprApSwEthLanEpTransport",
    "CfprApSwEthLanEpUdldAdminState",
    "CfprApSwEthLanEpUdldMode",
    "CfprApSwEthLanMonTransport",
    "CfprApSwEthLanPcTransport",
    "CfprApSwEthMonDestEpTransport",
    "CfprApSwEthMonFsmCurrentFsm",
    "CfprApSwEthMonFsmStageName",
    "CfprApSwEthMonFsmTaskItem",
    "CfprApSwEthMonSrcEpTransport",
    "CfprApSwEthMonTransport",
    "CfprApSwEthMonType",
    "CfprApSwEthTargetEpAdminState",
    "CfprApSwEthTargetEpTransport",
    "CfprApSwExtUtilityFsmCurrentFsm",
    "CfprApSwExtUtilityFsmStageName",
    "CfprApSwExtUtilityFsmTaskItem",
    "CfprApSwFabricRole",
    "CfprApSwFabricZoneNsAllocStatus",
    "CfprApSwFcSanBorderFsmCurrentFsm",
    "CfprApSwFcSanBorderFsmStageName",
    "CfprApSwFcSanBorderFsmTaskItem",
    "CfprApSwFcSanBorderTransport",
    "CfprApSwFcSanBorderUplinkTrunking",
    "CfprApSwFcSanEpTransport",
    "CfprApSwFcSanPcTransport",
    "CfprApSwFcServerZoneGroupLc",
    "CfprApSwFcZoneLc",
    "CfprApSwFcZoneMemberLc",
    "CfprApSwFcZoneSetLc",
    "CfprApSwFcoeSanEpTransport",
    "CfprApSwFcoeSanEpUdldAdminState",
    "CfprApSwFcoeSanEpUdldMode",
    "CfprApSwFcoeSanPcTransport",
    "CfprApSwLanBorderType",
    "CfprApSwLanEpIfRole",
    "CfprApSwLanEpType",
    "CfprApSwLanMonType",
    "CfprApSwLanPcIfRole",
    "CfprApSwLanPcType",
    "CfprApSwMonAdminState",
    "CfprApSwMonDomainLocale",
    "CfprApSwMonLifeCycle",
    "CfprApSwMonSrcEpLocale",
    "CfprApSwPIoEpIfType",
    "CfprApSwPIoEpLc",
    "CfprApSwPeerStatus",
    "CfprApSwPhysFsmCurrentFsm",
    "CfprApSwPhysFsmStageName",
    "CfprApSwPhysFsmTaskItem",
    "CfprApSwPktCaptureLifeCycle",
    "CfprApSwPortBreakoutPortId",
    "CfprApSwPortBreakoutSlotId",
    "CfprApSwSanBorderType",
    "CfprApSwSanEpIfRole",
    "CfprApSwSanEpType",
    "CfprApSwSanPcIfRole",
    "CfprApSwSanPcType",
    "CfprApSwSspEthLanMonTransport",
    "CfprApSwSspEthMonFsmCurrentFsm",
    "CfprApSwSspEthMonFsmStageName",
    "CfprApSwSspEthMonFsmTaskItem",
    "CfprApSwSspEthMonSrcPhyEpFsmCurrentFsm",
    "CfprApSwSspEthMonSrcPhyEpFsmStageName",
    "CfprApSwSspEthMonSrcPhyEpFsmTaskItem",
    "CfprApSwSspEthMonTransport",
    "CfprApSwSspEthMonType",
    "CfprApSwSspLanMonType",
    "CfprApSwSspMonAdminState",
    "CfprApSwSspMonDelPcap",
    "CfprApSwSspMonDomainLocale",
    "CfprApSwSubGroupAggrPortId",
    "CfprApSwSubGroupSlotId",
    "CfprApSwSystemStatsHistThresholded",
    "CfprApSwSystemStatsThresholded",
    "CfprApSwTargetEpType",
    "CfprApSwUlanPurpose",
    "CfprApSwUtilityDomainFsmCurrentFsm",
    "CfprApSwUtilityDomainFsmStageName",
    "CfprApSwUtilityDomainFsmTaskItem",
    "CfprApSwUtilityDomainLocale",
    "CfprApSwUtilityDomainType",
    "CfprApSwVlanCompType",
    "CfprApSwVlanConfigStatusType",
    "CfprApSwVlanGroupType",
    "CfprApSwVlanLc",
    "CfprApSwVlanPortNsAllocStatus")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprApSwObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApSwAccessDomainTable_Object = MibTable
cfprApSwAccessDomainTable = _CfprApSwAccessDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1)
)
if mibBuilder.loadTexts:
    cfprApSwAccessDomainTable.setStatus("current")
_CfprApSwAccessDomainEntry_Object = MibTableRow
cfprApSwAccessDomainEntry = _CfprApSwAccessDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1)
)
cfprApSwAccessDomainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwAccessDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwAccessDomainEntry.setStatus("current")
_CfprApSwAccessDomainInstanceId_Type = CfprApManagedObjectId
_CfprApSwAccessDomainInstanceId_Object = MibTableColumn
cfprApSwAccessDomainInstanceId = _CfprApSwAccessDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 1),
    _CfprApSwAccessDomainInstanceId_Type()
)
cfprApSwAccessDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainInstanceId.setStatus("current")
_CfprApSwAccessDomainDn_Type = CfprApManagedObjectDn
_CfprApSwAccessDomainDn_Object = MibTableColumn
cfprApSwAccessDomainDn = _CfprApSwAccessDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 2),
    _CfprApSwAccessDomainDn_Type()
)
cfprApSwAccessDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainDn.setStatus("current")
_CfprApSwAccessDomainRn_Type = SnmpAdminString
_CfprApSwAccessDomainRn_Object = MibTableColumn
cfprApSwAccessDomainRn = _CfprApSwAccessDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 3),
    _CfprApSwAccessDomainRn_Type()
)
cfprApSwAccessDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainRn.setStatus("current")
_CfprApSwAccessDomainFsmDescr_Type = SnmpAdminString
_CfprApSwAccessDomainFsmDescr_Object = MibTableColumn
cfprApSwAccessDomainFsmDescr = _CfprApSwAccessDomainFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 4),
    _CfprApSwAccessDomainFsmDescr_Type()
)
cfprApSwAccessDomainFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmDescr.setStatus("current")
_CfprApSwAccessDomainFsmPrev_Type = SnmpAdminString
_CfprApSwAccessDomainFsmPrev_Object = MibTableColumn
cfprApSwAccessDomainFsmPrev = _CfprApSwAccessDomainFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 5),
    _CfprApSwAccessDomainFsmPrev_Type()
)
cfprApSwAccessDomainFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmPrev.setStatus("current")
_CfprApSwAccessDomainFsmProgr_Type = Gauge32
_CfprApSwAccessDomainFsmProgr_Object = MibTableColumn
cfprApSwAccessDomainFsmProgr = _CfprApSwAccessDomainFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 6),
    _CfprApSwAccessDomainFsmProgr_Type()
)
cfprApSwAccessDomainFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmProgr.setStatus("current")
_CfprApSwAccessDomainFsmRmtInvErrCode_Type = Gauge32
_CfprApSwAccessDomainFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwAccessDomainFsmRmtInvErrCode = _CfprApSwAccessDomainFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 7),
    _CfprApSwAccessDomainFsmRmtInvErrCode_Type()
)
cfprApSwAccessDomainFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmRmtInvErrCode.setStatus("current")
_CfprApSwAccessDomainFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwAccessDomainFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwAccessDomainFsmRmtInvErrDescr = _CfprApSwAccessDomainFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 8),
    _CfprApSwAccessDomainFsmRmtInvErrDescr_Type()
)
cfprApSwAccessDomainFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmRmtInvErrDescr.setStatus("current")
_CfprApSwAccessDomainFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwAccessDomainFsmRmtInvRslt_Object = MibTableColumn
cfprApSwAccessDomainFsmRmtInvRslt = _CfprApSwAccessDomainFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 9),
    _CfprApSwAccessDomainFsmRmtInvRslt_Type()
)
cfprApSwAccessDomainFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmRmtInvRslt.setStatus("current")
_CfprApSwAccessDomainFsmStageDescr_Type = SnmpAdminString
_CfprApSwAccessDomainFsmStageDescr_Object = MibTableColumn
cfprApSwAccessDomainFsmStageDescr = _CfprApSwAccessDomainFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 10),
    _CfprApSwAccessDomainFsmStageDescr_Type()
)
cfprApSwAccessDomainFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageDescr.setStatus("current")
_CfprApSwAccessDomainFsmStamp_Type = DateAndTime
_CfprApSwAccessDomainFsmStamp_Object = MibTableColumn
cfprApSwAccessDomainFsmStamp = _CfprApSwAccessDomainFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 11),
    _CfprApSwAccessDomainFsmStamp_Type()
)
cfprApSwAccessDomainFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStamp.setStatus("current")
_CfprApSwAccessDomainFsmStatus_Type = SnmpAdminString
_CfprApSwAccessDomainFsmStatus_Object = MibTableColumn
cfprApSwAccessDomainFsmStatus = _CfprApSwAccessDomainFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 12),
    _CfprApSwAccessDomainFsmStatus_Type()
)
cfprApSwAccessDomainFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStatus.setStatus("current")
_CfprApSwAccessDomainFsmTry_Type = Gauge32
_CfprApSwAccessDomainFsmTry_Object = MibTableColumn
cfprApSwAccessDomainFsmTry = _CfprApSwAccessDomainFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 13),
    _CfprApSwAccessDomainFsmTry_Type()
)
cfprApSwAccessDomainFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTry.setStatus("current")
_CfprApSwAccessDomainLocale_Type = CfprApSwAccessDomainLocale
_CfprApSwAccessDomainLocale_Object = MibTableColumn
cfprApSwAccessDomainLocale = _CfprApSwAccessDomainLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 14),
    _CfprApSwAccessDomainLocale_Type()
)
cfprApSwAccessDomainLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainLocale.setStatus("current")
_CfprApSwAccessDomainName_Type = SnmpAdminString
_CfprApSwAccessDomainName_Object = MibTableColumn
cfprApSwAccessDomainName = _CfprApSwAccessDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 15),
    _CfprApSwAccessDomainName_Type()
)
cfprApSwAccessDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainName.setStatus("current")
_CfprApSwAccessDomainSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwAccessDomainSwitchId_Object = MibTableColumn
cfprApSwAccessDomainSwitchId = _CfprApSwAccessDomainSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 16),
    _CfprApSwAccessDomainSwitchId_Type()
)
cfprApSwAccessDomainSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainSwitchId.setStatus("current")
_CfprApSwAccessDomainTransport_Type = CfprApNetworkTransport
_CfprApSwAccessDomainTransport_Object = MibTableColumn
cfprApSwAccessDomainTransport = _CfprApSwAccessDomainTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 17),
    _CfprApSwAccessDomainTransport_Type()
)
cfprApSwAccessDomainTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainTransport.setStatus("current")
_CfprApSwAccessDomainType_Type = CfprApSwAccessDomainType
_CfprApSwAccessDomainType_Object = MibTableColumn
cfprApSwAccessDomainType = _CfprApSwAccessDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 1, 1, 18),
    _CfprApSwAccessDomainType_Type()
)
cfprApSwAccessDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainType.setStatus("current")
_CfprApSwAccessDomainFsmTable_Object = MibTable
cfprApSwAccessDomainFsmTable = _CfprApSwAccessDomainFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2)
)
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTable.setStatus("current")
_CfprApSwAccessDomainFsmEntry_Object = MibTableRow
cfprApSwAccessDomainFsmEntry = _CfprApSwAccessDomainFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1)
)
cfprApSwAccessDomainFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwAccessDomainFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmEntry.setStatus("current")
_CfprApSwAccessDomainFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwAccessDomainFsmInstanceId_Object = MibTableColumn
cfprApSwAccessDomainFsmInstanceId = _CfprApSwAccessDomainFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 1),
    _CfprApSwAccessDomainFsmInstanceId_Type()
)
cfprApSwAccessDomainFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmInstanceId.setStatus("current")
_CfprApSwAccessDomainFsmDn_Type = CfprApManagedObjectDn
_CfprApSwAccessDomainFsmDn_Object = MibTableColumn
cfprApSwAccessDomainFsmDn = _CfprApSwAccessDomainFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 2),
    _CfprApSwAccessDomainFsmDn_Type()
)
cfprApSwAccessDomainFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmDn.setStatus("current")
_CfprApSwAccessDomainFsmRn_Type = SnmpAdminString
_CfprApSwAccessDomainFsmRn_Object = MibTableColumn
cfprApSwAccessDomainFsmRn = _CfprApSwAccessDomainFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 3),
    _CfprApSwAccessDomainFsmRn_Type()
)
cfprApSwAccessDomainFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmRn.setStatus("current")
_CfprApSwAccessDomainFsmCompletionTime_Type = DateAndTime
_CfprApSwAccessDomainFsmCompletionTime_Object = MibTableColumn
cfprApSwAccessDomainFsmCompletionTime = _CfprApSwAccessDomainFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 4),
    _CfprApSwAccessDomainFsmCompletionTime_Type()
)
cfprApSwAccessDomainFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmCompletionTime.setStatus("current")
_CfprApSwAccessDomainFsmCurrentFsm_Type = CfprApSwAccessDomainFsmCurrentFsm
_CfprApSwAccessDomainFsmCurrentFsm_Object = MibTableColumn
cfprApSwAccessDomainFsmCurrentFsm = _CfprApSwAccessDomainFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 5),
    _CfprApSwAccessDomainFsmCurrentFsm_Type()
)
cfprApSwAccessDomainFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmCurrentFsm.setStatus("current")
_CfprApSwAccessDomainFsmDescrData_Type = SnmpAdminString
_CfprApSwAccessDomainFsmDescrData_Object = MibTableColumn
cfprApSwAccessDomainFsmDescrData = _CfprApSwAccessDomainFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 6),
    _CfprApSwAccessDomainFsmDescrData_Type()
)
cfprApSwAccessDomainFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmDescrData.setStatus("current")
_CfprApSwAccessDomainFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwAccessDomainFsmFsmStatus_Object = MibTableColumn
cfprApSwAccessDomainFsmFsmStatus = _CfprApSwAccessDomainFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 7),
    _CfprApSwAccessDomainFsmFsmStatus_Type()
)
cfprApSwAccessDomainFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmFsmStatus.setStatus("current")
_CfprApSwAccessDomainFsmProgress_Type = Gauge32
_CfprApSwAccessDomainFsmProgress_Object = MibTableColumn
cfprApSwAccessDomainFsmProgress = _CfprApSwAccessDomainFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 8),
    _CfprApSwAccessDomainFsmProgress_Type()
)
cfprApSwAccessDomainFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmProgress.setStatus("current")
_CfprApSwAccessDomainFsmRmtErrCode_Type = Gauge32
_CfprApSwAccessDomainFsmRmtErrCode_Object = MibTableColumn
cfprApSwAccessDomainFsmRmtErrCode = _CfprApSwAccessDomainFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 9),
    _CfprApSwAccessDomainFsmRmtErrCode_Type()
)
cfprApSwAccessDomainFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmRmtErrCode.setStatus("current")
_CfprApSwAccessDomainFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwAccessDomainFsmRmtErrDescr_Object = MibTableColumn
cfprApSwAccessDomainFsmRmtErrDescr = _CfprApSwAccessDomainFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 10),
    _CfprApSwAccessDomainFsmRmtErrDescr_Type()
)
cfprApSwAccessDomainFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmRmtErrDescr.setStatus("current")
_CfprApSwAccessDomainFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwAccessDomainFsmRmtRslt_Object = MibTableColumn
cfprApSwAccessDomainFsmRmtRslt = _CfprApSwAccessDomainFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 2, 1, 11),
    _CfprApSwAccessDomainFsmRmtRslt_Type()
)
cfprApSwAccessDomainFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmRmtRslt.setStatus("current")
_CfprApSwAccessDomainFsmStageTable_Object = MibTable
cfprApSwAccessDomainFsmStageTable = _CfprApSwAccessDomainFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3)
)
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageTable.setStatus("current")
_CfprApSwAccessDomainFsmStageEntry_Object = MibTableRow
cfprApSwAccessDomainFsmStageEntry = _CfprApSwAccessDomainFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1)
)
cfprApSwAccessDomainFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwAccessDomainFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageEntry.setStatus("current")
_CfprApSwAccessDomainFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwAccessDomainFsmStageInstanceId_Object = MibTableColumn
cfprApSwAccessDomainFsmStageInstanceId = _CfprApSwAccessDomainFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 1),
    _CfprApSwAccessDomainFsmStageInstanceId_Type()
)
cfprApSwAccessDomainFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageInstanceId.setStatus("current")
_CfprApSwAccessDomainFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwAccessDomainFsmStageDn_Object = MibTableColumn
cfprApSwAccessDomainFsmStageDn = _CfprApSwAccessDomainFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 2),
    _CfprApSwAccessDomainFsmStageDn_Type()
)
cfprApSwAccessDomainFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageDn.setStatus("current")
_CfprApSwAccessDomainFsmStageRn_Type = SnmpAdminString
_CfprApSwAccessDomainFsmStageRn_Object = MibTableColumn
cfprApSwAccessDomainFsmStageRn = _CfprApSwAccessDomainFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 3),
    _CfprApSwAccessDomainFsmStageRn_Type()
)
cfprApSwAccessDomainFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageRn.setStatus("current")
_CfprApSwAccessDomainFsmStageDescrData_Type = SnmpAdminString
_CfprApSwAccessDomainFsmStageDescrData_Object = MibTableColumn
cfprApSwAccessDomainFsmStageDescrData = _CfprApSwAccessDomainFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 4),
    _CfprApSwAccessDomainFsmStageDescrData_Type()
)
cfprApSwAccessDomainFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageDescrData.setStatus("current")
_CfprApSwAccessDomainFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwAccessDomainFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwAccessDomainFsmStageLastUpdateTime = _CfprApSwAccessDomainFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 5),
    _CfprApSwAccessDomainFsmStageLastUpdateTime_Type()
)
cfprApSwAccessDomainFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageLastUpdateTime.setStatus("current")
_CfprApSwAccessDomainFsmStageName_Type = CfprApSwAccessDomainFsmStageName
_CfprApSwAccessDomainFsmStageName_Object = MibTableColumn
cfprApSwAccessDomainFsmStageName = _CfprApSwAccessDomainFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 6),
    _CfprApSwAccessDomainFsmStageName_Type()
)
cfprApSwAccessDomainFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageName.setStatus("current")
_CfprApSwAccessDomainFsmStageOrder_Type = Gauge32
_CfprApSwAccessDomainFsmStageOrder_Object = MibTableColumn
cfprApSwAccessDomainFsmStageOrder = _CfprApSwAccessDomainFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 7),
    _CfprApSwAccessDomainFsmStageOrder_Type()
)
cfprApSwAccessDomainFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageOrder.setStatus("current")
_CfprApSwAccessDomainFsmStageRetry_Type = Gauge32
_CfprApSwAccessDomainFsmStageRetry_Object = MibTableColumn
cfprApSwAccessDomainFsmStageRetry = _CfprApSwAccessDomainFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 8),
    _CfprApSwAccessDomainFsmStageRetry_Type()
)
cfprApSwAccessDomainFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageRetry.setStatus("current")
_CfprApSwAccessDomainFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwAccessDomainFsmStageStageStatus_Object = MibTableColumn
cfprApSwAccessDomainFsmStageStageStatus = _CfprApSwAccessDomainFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 3, 1, 9),
    _CfprApSwAccessDomainFsmStageStageStatus_Type()
)
cfprApSwAccessDomainFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmStageStageStatus.setStatus("current")
_CfprApSwAccessDomainFsmTaskTable_Object = MibTable
cfprApSwAccessDomainFsmTaskTable = _CfprApSwAccessDomainFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4)
)
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskTable.setStatus("current")
_CfprApSwAccessDomainFsmTaskEntry_Object = MibTableRow
cfprApSwAccessDomainFsmTaskEntry = _CfprApSwAccessDomainFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4, 1)
)
cfprApSwAccessDomainFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwAccessDomainFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskEntry.setStatus("current")
_CfprApSwAccessDomainFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwAccessDomainFsmTaskInstanceId_Object = MibTableColumn
cfprApSwAccessDomainFsmTaskInstanceId = _CfprApSwAccessDomainFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4, 1, 1),
    _CfprApSwAccessDomainFsmTaskInstanceId_Type()
)
cfprApSwAccessDomainFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskInstanceId.setStatus("current")
_CfprApSwAccessDomainFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwAccessDomainFsmTaskDn_Object = MibTableColumn
cfprApSwAccessDomainFsmTaskDn = _CfprApSwAccessDomainFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4, 1, 2),
    _CfprApSwAccessDomainFsmTaskDn_Type()
)
cfprApSwAccessDomainFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskDn.setStatus("current")
_CfprApSwAccessDomainFsmTaskRn_Type = SnmpAdminString
_CfprApSwAccessDomainFsmTaskRn_Object = MibTableColumn
cfprApSwAccessDomainFsmTaskRn = _CfprApSwAccessDomainFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4, 1, 3),
    _CfprApSwAccessDomainFsmTaskRn_Type()
)
cfprApSwAccessDomainFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskRn.setStatus("current")
_CfprApSwAccessDomainFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwAccessDomainFsmTaskCompletion_Object = MibTableColumn
cfprApSwAccessDomainFsmTaskCompletion = _CfprApSwAccessDomainFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4, 1, 4),
    _CfprApSwAccessDomainFsmTaskCompletion_Type()
)
cfprApSwAccessDomainFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskCompletion.setStatus("current")
_CfprApSwAccessDomainFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSwAccessDomainFsmTaskFlags_Object = MibTableColumn
cfprApSwAccessDomainFsmTaskFlags = _CfprApSwAccessDomainFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4, 1, 5),
    _CfprApSwAccessDomainFsmTaskFlags_Type()
)
cfprApSwAccessDomainFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskFlags.setStatus("current")
_CfprApSwAccessDomainFsmTaskItem_Type = CfprApSwAccessDomainFsmTaskItem
_CfprApSwAccessDomainFsmTaskItem_Object = MibTableColumn
cfprApSwAccessDomainFsmTaskItem = _CfprApSwAccessDomainFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4, 1, 6),
    _CfprApSwAccessDomainFsmTaskItem_Type()
)
cfprApSwAccessDomainFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskItem.setStatus("current")
_CfprApSwAccessDomainFsmTaskSeqId_Type = Gauge32
_CfprApSwAccessDomainFsmTaskSeqId_Object = MibTableColumn
cfprApSwAccessDomainFsmTaskSeqId = _CfprApSwAccessDomainFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 4, 1, 7),
    _CfprApSwAccessDomainFsmTaskSeqId_Type()
)
cfprApSwAccessDomainFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessDomainFsmTaskSeqId.setStatus("current")
_CfprApSwAccessEpTable_Object = MibTable
cfprApSwAccessEpTable = _CfprApSwAccessEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5)
)
if mibBuilder.loadTexts:
    cfprApSwAccessEpTable.setStatus("current")
_CfprApSwAccessEpEntry_Object = MibTableRow
cfprApSwAccessEpEntry = _CfprApSwAccessEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1)
)
cfprApSwAccessEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwAccessEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwAccessEpEntry.setStatus("current")
_CfprApSwAccessEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwAccessEpInstanceId_Object = MibTableColumn
cfprApSwAccessEpInstanceId = _CfprApSwAccessEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 1),
    _CfprApSwAccessEpInstanceId_Type()
)
cfprApSwAccessEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwAccessEpInstanceId.setStatus("current")
_CfprApSwAccessEpDn_Type = CfprApManagedObjectDn
_CfprApSwAccessEpDn_Object = MibTableColumn
cfprApSwAccessEpDn = _CfprApSwAccessEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 2),
    _CfprApSwAccessEpDn_Type()
)
cfprApSwAccessEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpDn.setStatus("current")
_CfprApSwAccessEpRn_Type = SnmpAdminString
_CfprApSwAccessEpRn_Object = MibTableColumn
cfprApSwAccessEpRn = _CfprApSwAccessEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 3),
    _CfprApSwAccessEpRn_Type()
)
cfprApSwAccessEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpRn.setStatus("current")
_CfprApSwAccessEpAdminState_Type = CfprApFabricAdminState
_CfprApSwAccessEpAdminState_Object = MibTableColumn
cfprApSwAccessEpAdminState = _CfprApSwAccessEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 4),
    _CfprApSwAccessEpAdminState_Type()
)
cfprApSwAccessEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpAdminState.setStatus("current")
_CfprApSwAccessEpAggrPortId_Type = Gauge32
_CfprApSwAccessEpAggrPortId_Object = MibTableColumn
cfprApSwAccessEpAggrPortId = _CfprApSwAccessEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 5),
    _CfprApSwAccessEpAggrPortId_Type()
)
cfprApSwAccessEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpAggrPortId.setStatus("current")
_CfprApSwAccessEpChassisId_Type = Gauge32
_CfprApSwAccessEpChassisId_Object = MibTableColumn
cfprApSwAccessEpChassisId = _CfprApSwAccessEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 6),
    _CfprApSwAccessEpChassisId_Type()
)
cfprApSwAccessEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpChassisId.setStatus("current")
_CfprApSwAccessEpEncap_Type = Gauge32
_CfprApSwAccessEpEncap_Object = MibTableColumn
cfprApSwAccessEpEncap = _CfprApSwAccessEpEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 7),
    _CfprApSwAccessEpEncap_Type()
)
cfprApSwAccessEpEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpEncap.setStatus("current")
_CfprApSwAccessEpEpDn_Type = SnmpAdminString
_CfprApSwAccessEpEpDn_Object = MibTableColumn
cfprApSwAccessEpEpDn = _CfprApSwAccessEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 8),
    _CfprApSwAccessEpEpDn_Type()
)
cfprApSwAccessEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpEpDn.setStatus("current")
_CfprApSwAccessEpIfRole_Type = CfprApNetworkPortRole
_CfprApSwAccessEpIfRole_Object = MibTableColumn
cfprApSwAccessEpIfRole = _CfprApSwAccessEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 9),
    _CfprApSwAccessEpIfRole_Type()
)
cfprApSwAccessEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpIfRole.setStatus("current")
_CfprApSwAccessEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwAccessEpIfType_Object = MibTableColumn
cfprApSwAccessEpIfType = _CfprApSwAccessEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 10),
    _CfprApSwAccessEpIfType_Type()
)
cfprApSwAccessEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpIfType.setStatus("current")
_CfprApSwAccessEpLc_Type = CfprApSwPIoEpLc
_CfprApSwAccessEpLc_Object = MibTableColumn
cfprApSwAccessEpLc = _CfprApSwAccessEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 11),
    _CfprApSwAccessEpLc_Type()
)
cfprApSwAccessEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpLc.setStatus("current")
_CfprApSwAccessEpLocale_Type = CfprApSwAccessEpLocale
_CfprApSwAccessEpLocale_Object = MibTableColumn
cfprApSwAccessEpLocale = _CfprApSwAccessEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 12),
    _CfprApSwAccessEpLocale_Type()
)
cfprApSwAccessEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpLocale.setStatus("current")
_CfprApSwAccessEpName_Type = SnmpAdminString
_CfprApSwAccessEpName_Object = MibTableColumn
cfprApSwAccessEpName = _CfprApSwAccessEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 13),
    _CfprApSwAccessEpName_Type()
)
cfprApSwAccessEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpName.setStatus("current")
_CfprApSwAccessEpNsSize_Type = Gauge32
_CfprApSwAccessEpNsSize_Object = MibTableColumn
cfprApSwAccessEpNsSize = _CfprApSwAccessEpNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 14),
    _CfprApSwAccessEpNsSize_Type()
)
cfprApSwAccessEpNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpNsSize.setStatus("current")
_CfprApSwAccessEpPeerAggrPortId_Type = Gauge32
_CfprApSwAccessEpPeerAggrPortId_Object = MibTableColumn
cfprApSwAccessEpPeerAggrPortId = _CfprApSwAccessEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 15),
    _CfprApSwAccessEpPeerAggrPortId_Type()
)
cfprApSwAccessEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpPeerAggrPortId.setStatus("current")
_CfprApSwAccessEpPeerChassisId_Type = Gauge32
_CfprApSwAccessEpPeerChassisId_Object = MibTableColumn
cfprApSwAccessEpPeerChassisId = _CfprApSwAccessEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 16),
    _CfprApSwAccessEpPeerChassisId_Type()
)
cfprApSwAccessEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpPeerChassisId.setStatus("current")
_CfprApSwAccessEpPeerDn_Type = SnmpAdminString
_CfprApSwAccessEpPeerDn_Object = MibTableColumn
cfprApSwAccessEpPeerDn = _CfprApSwAccessEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 17),
    _CfprApSwAccessEpPeerDn_Type()
)
cfprApSwAccessEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpPeerDn.setStatus("current")
_CfprApSwAccessEpPeerPortId_Type = Gauge32
_CfprApSwAccessEpPeerPortId_Object = MibTableColumn
cfprApSwAccessEpPeerPortId = _CfprApSwAccessEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 18),
    _CfprApSwAccessEpPeerPortId_Type()
)
cfprApSwAccessEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpPeerPortId.setStatus("current")
_CfprApSwAccessEpPeerSlotId_Type = Gauge32
_CfprApSwAccessEpPeerSlotId_Object = MibTableColumn
cfprApSwAccessEpPeerSlotId = _CfprApSwAccessEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 19),
    _CfprApSwAccessEpPeerSlotId_Type()
)
cfprApSwAccessEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpPeerSlotId.setStatus("current")
_CfprApSwAccessEpPortId_Type = Gauge32
_CfprApSwAccessEpPortId_Object = MibTableColumn
cfprApSwAccessEpPortId = _CfprApSwAccessEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 20),
    _CfprApSwAccessEpPortId_Type()
)
cfprApSwAccessEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpPortId.setStatus("current")
_CfprApSwAccessEpSlotId_Type = Gauge32
_CfprApSwAccessEpSlotId_Object = MibTableColumn
cfprApSwAccessEpSlotId = _CfprApSwAccessEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 21),
    _CfprApSwAccessEpSlotId_Type()
)
cfprApSwAccessEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpSlotId.setStatus("current")
_CfprApSwAccessEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwAccessEpSwitchId_Object = MibTableColumn
cfprApSwAccessEpSwitchId = _CfprApSwAccessEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 22),
    _CfprApSwAccessEpSwitchId_Type()
)
cfprApSwAccessEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpSwitchId.setStatus("current")
_CfprApSwAccessEpTransport_Type = CfprApSwAccessEpTransport
_CfprApSwAccessEpTransport_Object = MibTableColumn
cfprApSwAccessEpTransport = _CfprApSwAccessEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 23),
    _CfprApSwAccessEpTransport_Type()
)
cfprApSwAccessEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpTransport.setStatus("current")
_CfprApSwAccessEpType_Type = CfprApNetworkConnectionType
_CfprApSwAccessEpType_Object = MibTableColumn
cfprApSwAccessEpType = _CfprApSwAccessEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 5, 1, 24),
    _CfprApSwAccessEpType_Type()
)
cfprApSwAccessEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwAccessEpType.setStatus("current")
_CfprApSwCardEnvStatsTable_Object = MibTable
cfprApSwCardEnvStatsTable = _CfprApSwCardEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6)
)
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsTable.setStatus("current")
_CfprApSwCardEnvStatsEntry_Object = MibTableRow
cfprApSwCardEnvStatsEntry = _CfprApSwCardEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1)
)
cfprApSwCardEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwCardEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsEntry.setStatus("current")
_CfprApSwCardEnvStatsInstanceId_Type = CfprApManagedObjectId
_CfprApSwCardEnvStatsInstanceId_Object = MibTableColumn
cfprApSwCardEnvStatsInstanceId = _CfprApSwCardEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 1),
    _CfprApSwCardEnvStatsInstanceId_Type()
)
cfprApSwCardEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsInstanceId.setStatus("current")
_CfprApSwCardEnvStatsDn_Type = CfprApManagedObjectDn
_CfprApSwCardEnvStatsDn_Object = MibTableColumn
cfprApSwCardEnvStatsDn = _CfprApSwCardEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 2),
    _CfprApSwCardEnvStatsDn_Type()
)
cfprApSwCardEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsDn.setStatus("current")
_CfprApSwCardEnvStatsRn_Type = SnmpAdminString
_CfprApSwCardEnvStatsRn_Object = MibTableColumn
cfprApSwCardEnvStatsRn = _CfprApSwCardEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 3),
    _CfprApSwCardEnvStatsRn_Type()
)
cfprApSwCardEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsRn.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet1_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet1_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet1 = _CfprApSwCardEnvStatsSlotOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 4),
    _CfprApSwCardEnvStatsSlotOutlet1_Type()
)
cfprApSwCardEnvStatsSlotOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet1.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet1Avg_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet1Avg_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet1Avg = _CfprApSwCardEnvStatsSlotOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 5),
    _CfprApSwCardEnvStatsSlotOutlet1Avg_Type()
)
cfprApSwCardEnvStatsSlotOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet1Avg.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet1Max_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet1Max_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet1Max = _CfprApSwCardEnvStatsSlotOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 6),
    _CfprApSwCardEnvStatsSlotOutlet1Max_Type()
)
cfprApSwCardEnvStatsSlotOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet1Max.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet1Min_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet1Min_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet1Min = _CfprApSwCardEnvStatsSlotOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 7),
    _CfprApSwCardEnvStatsSlotOutlet1Min_Type()
)
cfprApSwCardEnvStatsSlotOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet1Min.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet2_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet2_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet2 = _CfprApSwCardEnvStatsSlotOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 8),
    _CfprApSwCardEnvStatsSlotOutlet2_Type()
)
cfprApSwCardEnvStatsSlotOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet2.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet2Avg_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet2Avg_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet2Avg = _CfprApSwCardEnvStatsSlotOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 9),
    _CfprApSwCardEnvStatsSlotOutlet2Avg_Type()
)
cfprApSwCardEnvStatsSlotOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet2Avg.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet2Max_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet2Max_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet2Max = _CfprApSwCardEnvStatsSlotOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 10),
    _CfprApSwCardEnvStatsSlotOutlet2Max_Type()
)
cfprApSwCardEnvStatsSlotOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet2Max.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet2Min_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet2Min_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet2Min = _CfprApSwCardEnvStatsSlotOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 11),
    _CfprApSwCardEnvStatsSlotOutlet2Min_Type()
)
cfprApSwCardEnvStatsSlotOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet2Min.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet3_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet3_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet3 = _CfprApSwCardEnvStatsSlotOutlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 12),
    _CfprApSwCardEnvStatsSlotOutlet3_Type()
)
cfprApSwCardEnvStatsSlotOutlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet3.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet3Avg_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet3Avg_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet3Avg = _CfprApSwCardEnvStatsSlotOutlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 13),
    _CfprApSwCardEnvStatsSlotOutlet3Avg_Type()
)
cfprApSwCardEnvStatsSlotOutlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet3Avg.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet3Max_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet3Max_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet3Max = _CfprApSwCardEnvStatsSlotOutlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 14),
    _CfprApSwCardEnvStatsSlotOutlet3Max_Type()
)
cfprApSwCardEnvStatsSlotOutlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet3Max.setStatus("current")
_CfprApSwCardEnvStatsSlotOutlet3Min_Type = Integer32
_CfprApSwCardEnvStatsSlotOutlet3Min_Object = MibTableColumn
cfprApSwCardEnvStatsSlotOutlet3Min = _CfprApSwCardEnvStatsSlotOutlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 15),
    _CfprApSwCardEnvStatsSlotOutlet3Min_Type()
)
cfprApSwCardEnvStatsSlotOutlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSlotOutlet3Min.setStatus("current")
_CfprApSwCardEnvStatsIntervals_Type = Gauge32
_CfprApSwCardEnvStatsIntervals_Object = MibTableColumn
cfprApSwCardEnvStatsIntervals = _CfprApSwCardEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 16),
    _CfprApSwCardEnvStatsIntervals_Type()
)
cfprApSwCardEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsIntervals.setStatus("current")
_CfprApSwCardEnvStatsSuspect_Type = TruthValue
_CfprApSwCardEnvStatsSuspect_Object = MibTableColumn
cfprApSwCardEnvStatsSuspect = _CfprApSwCardEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 17),
    _CfprApSwCardEnvStatsSuspect_Type()
)
cfprApSwCardEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsSuspect.setStatus("current")
_CfprApSwCardEnvStatsThresholded_Type = CfprApSwCardEnvStatsThresholded
_CfprApSwCardEnvStatsThresholded_Object = MibTableColumn
cfprApSwCardEnvStatsThresholded = _CfprApSwCardEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 18),
    _CfprApSwCardEnvStatsThresholded_Type()
)
cfprApSwCardEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsThresholded.setStatus("current")
_CfprApSwCardEnvStatsTimeCollected_Type = DateAndTime
_CfprApSwCardEnvStatsTimeCollected_Object = MibTableColumn
cfprApSwCardEnvStatsTimeCollected = _CfprApSwCardEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 19),
    _CfprApSwCardEnvStatsTimeCollected_Type()
)
cfprApSwCardEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsTimeCollected.setStatus("current")
_CfprApSwCardEnvStatsUpdate_Type = Gauge32
_CfprApSwCardEnvStatsUpdate_Object = MibTableColumn
cfprApSwCardEnvStatsUpdate = _CfprApSwCardEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 6, 1, 20),
    _CfprApSwCardEnvStatsUpdate_Type()
)
cfprApSwCardEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsUpdate.setStatus("current")
_CfprApSwCardEnvStatsHistTable_Object = MibTable
cfprApSwCardEnvStatsHistTable = _CfprApSwCardEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7)
)
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistTable.setStatus("current")
_CfprApSwCardEnvStatsHistEntry_Object = MibTableRow
cfprApSwCardEnvStatsHistEntry = _CfprApSwCardEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1)
)
cfprApSwCardEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwCardEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistEntry.setStatus("current")
_CfprApSwCardEnvStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApSwCardEnvStatsHistInstanceId_Object = MibTableColumn
cfprApSwCardEnvStatsHistInstanceId = _CfprApSwCardEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 1),
    _CfprApSwCardEnvStatsHistInstanceId_Type()
)
cfprApSwCardEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistInstanceId.setStatus("current")
_CfprApSwCardEnvStatsHistDn_Type = CfprApManagedObjectDn
_CfprApSwCardEnvStatsHistDn_Object = MibTableColumn
cfprApSwCardEnvStatsHistDn = _CfprApSwCardEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 2),
    _CfprApSwCardEnvStatsHistDn_Type()
)
cfprApSwCardEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistDn.setStatus("current")
_CfprApSwCardEnvStatsHistRn_Type = SnmpAdminString
_CfprApSwCardEnvStatsHistRn_Object = MibTableColumn
cfprApSwCardEnvStatsHistRn = _CfprApSwCardEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 3),
    _CfprApSwCardEnvStatsHistRn_Type()
)
cfprApSwCardEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistRn.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet1_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet1_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet1 = _CfprApSwCardEnvStatsHistSlotOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 4),
    _CfprApSwCardEnvStatsHistSlotOutlet1_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet1.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet1Avg_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet1Avg_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet1Avg = _CfprApSwCardEnvStatsHistSlotOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 5),
    _CfprApSwCardEnvStatsHistSlotOutlet1Avg_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet1Avg.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet1Max_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet1Max_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet1Max = _CfprApSwCardEnvStatsHistSlotOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 6),
    _CfprApSwCardEnvStatsHistSlotOutlet1Max_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet1Max.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet1Min_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet1Min_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet1Min = _CfprApSwCardEnvStatsHistSlotOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 7),
    _CfprApSwCardEnvStatsHistSlotOutlet1Min_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet1Min.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet2_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet2_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet2 = _CfprApSwCardEnvStatsHistSlotOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 8),
    _CfprApSwCardEnvStatsHistSlotOutlet2_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet2.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet2Avg_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet2Avg_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet2Avg = _CfprApSwCardEnvStatsHistSlotOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 9),
    _CfprApSwCardEnvStatsHistSlotOutlet2Avg_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet2Avg.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet2Max_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet2Max_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet2Max = _CfprApSwCardEnvStatsHistSlotOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 10),
    _CfprApSwCardEnvStatsHistSlotOutlet2Max_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet2Max.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet2Min_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet2Min_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet2Min = _CfprApSwCardEnvStatsHistSlotOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 11),
    _CfprApSwCardEnvStatsHistSlotOutlet2Min_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet2Min.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet3_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet3_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet3 = _CfprApSwCardEnvStatsHistSlotOutlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 12),
    _CfprApSwCardEnvStatsHistSlotOutlet3_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet3.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet3Avg_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet3Avg_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet3Avg = _CfprApSwCardEnvStatsHistSlotOutlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 13),
    _CfprApSwCardEnvStatsHistSlotOutlet3Avg_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet3Avg.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet3Max_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet3Max_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet3Max = _CfprApSwCardEnvStatsHistSlotOutlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 14),
    _CfprApSwCardEnvStatsHistSlotOutlet3Max_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet3Max.setStatus("current")
_CfprApSwCardEnvStatsHistSlotOutlet3Min_Type = Integer32
_CfprApSwCardEnvStatsHistSlotOutlet3Min_Object = MibTableColumn
cfprApSwCardEnvStatsHistSlotOutlet3Min = _CfprApSwCardEnvStatsHistSlotOutlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 15),
    _CfprApSwCardEnvStatsHistSlotOutlet3Min_Type()
)
cfprApSwCardEnvStatsHistSlotOutlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSlotOutlet3Min.setStatus("current")
_CfprApSwCardEnvStatsHistId_Type = Unsigned64
_CfprApSwCardEnvStatsHistId_Object = MibTableColumn
cfprApSwCardEnvStatsHistId = _CfprApSwCardEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 16),
    _CfprApSwCardEnvStatsHistId_Type()
)
cfprApSwCardEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistId.setStatus("current")
_CfprApSwCardEnvStatsHistMostRecent_Type = TruthValue
_CfprApSwCardEnvStatsHistMostRecent_Object = MibTableColumn
cfprApSwCardEnvStatsHistMostRecent = _CfprApSwCardEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 17),
    _CfprApSwCardEnvStatsHistMostRecent_Type()
)
cfprApSwCardEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistMostRecent.setStatus("current")
_CfprApSwCardEnvStatsHistSuspect_Type = TruthValue
_CfprApSwCardEnvStatsHistSuspect_Object = MibTableColumn
cfprApSwCardEnvStatsHistSuspect = _CfprApSwCardEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 18),
    _CfprApSwCardEnvStatsHistSuspect_Type()
)
cfprApSwCardEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistSuspect.setStatus("current")
_CfprApSwCardEnvStatsHistThresholded_Type = CfprApSwCardEnvStatsHistThresholded
_CfprApSwCardEnvStatsHistThresholded_Object = MibTableColumn
cfprApSwCardEnvStatsHistThresholded = _CfprApSwCardEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 19),
    _CfprApSwCardEnvStatsHistThresholded_Type()
)
cfprApSwCardEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistThresholded.setStatus("current")
_CfprApSwCardEnvStatsHistTimeCollected_Type = DateAndTime
_CfprApSwCardEnvStatsHistTimeCollected_Object = MibTableColumn
cfprApSwCardEnvStatsHistTimeCollected = _CfprApSwCardEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 7, 1, 20),
    _CfprApSwCardEnvStatsHistTimeCollected_Type()
)
cfprApSwCardEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCardEnvStatsHistTimeCollected.setStatus("current")
_CfprApSwCmclanTable_Object = MibTable
cfprApSwCmclanTable = _CfprApSwCmclanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8)
)
if mibBuilder.loadTexts:
    cfprApSwCmclanTable.setStatus("current")
_CfprApSwCmclanEntry_Object = MibTableRow
cfprApSwCmclanEntry = _CfprApSwCmclanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1)
)
cfprApSwCmclanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwCmclanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwCmclanEntry.setStatus("current")
_CfprApSwCmclanInstanceId_Type = CfprApManagedObjectId
_CfprApSwCmclanInstanceId_Object = MibTableColumn
cfprApSwCmclanInstanceId = _CfprApSwCmclanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 1),
    _CfprApSwCmclanInstanceId_Type()
)
cfprApSwCmclanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwCmclanInstanceId.setStatus("current")
_CfprApSwCmclanDn_Type = CfprApManagedObjectDn
_CfprApSwCmclanDn_Object = MibTableColumn
cfprApSwCmclanDn = _CfprApSwCmclanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 2),
    _CfprApSwCmclanDn_Type()
)
cfprApSwCmclanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanDn.setStatus("current")
_CfprApSwCmclanRn_Type = SnmpAdminString
_CfprApSwCmclanRn_Object = MibTableColumn
cfprApSwCmclanRn = _CfprApSwCmclanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 3),
    _CfprApSwCmclanRn_Type()
)
cfprApSwCmclanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanRn.setStatus("current")
_CfprApSwCmclanCimcIds_Type = CfprApSwCimcId
_CfprApSwCmclanCimcIds_Object = MibTableColumn
cfprApSwCmclanCimcIds = _CfprApSwCmclanCimcIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 4),
    _CfprApSwCmclanCimcIds_Type()
)
cfprApSwCmclanCimcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanCimcIds.setStatus("current")
_CfprApSwCmclanEpDn_Type = SnmpAdminString
_CfprApSwCmclanEpDn_Object = MibTableColumn
cfprApSwCmclanEpDn = _CfprApSwCmclanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 5),
    _CfprApSwCmclanEpDn_Type()
)
cfprApSwCmclanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanEpDn.setStatus("current")
_CfprApSwCmclanId_Type = Gauge32
_CfprApSwCmclanId_Object = MibTableColumn
cfprApSwCmclanId = _CfprApSwCmclanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 6),
    _CfprApSwCmclanId_Type()
)
cfprApSwCmclanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanId.setStatus("current")
_CfprApSwCmclanIfRole_Type = CfprApNetworkPortRole
_CfprApSwCmclanIfRole_Object = MibTableColumn
cfprApSwCmclanIfRole = _CfprApSwCmclanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 7),
    _CfprApSwCmclanIfRole_Type()
)
cfprApSwCmclanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanIfRole.setStatus("current")
_CfprApSwCmclanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApSwCmclanIfType_Object = MibTableColumn
cfprApSwCmclanIfType = _CfprApSwCmclanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 8),
    _CfprApSwCmclanIfType_Type()
)
cfprApSwCmclanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanIfType.setStatus("current")
_CfprApSwCmclanLocale_Type = CfprApNetworkLocale
_CfprApSwCmclanLocale_Object = MibTableColumn
cfprApSwCmclanLocale = _CfprApSwCmclanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 9),
    _CfprApSwCmclanLocale_Type()
)
cfprApSwCmclanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanLocale.setStatus("current")
_CfprApSwCmclanName_Type = SnmpAdminString
_CfprApSwCmclanName_Object = MibTableColumn
cfprApSwCmclanName = _CfprApSwCmclanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 10),
    _CfprApSwCmclanName_Type()
)
cfprApSwCmclanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanName.setStatus("current")
_CfprApSwCmclanPeerDn_Type = SnmpAdminString
_CfprApSwCmclanPeerDn_Object = MibTableColumn
cfprApSwCmclanPeerDn = _CfprApSwCmclanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 11),
    _CfprApSwCmclanPeerDn_Type()
)
cfprApSwCmclanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanPeerDn.setStatus("current")
_CfprApSwCmclanTransport_Type = CfprApNetworkTransport
_CfprApSwCmclanTransport_Object = MibTableColumn
cfprApSwCmclanTransport = _CfprApSwCmclanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 12),
    _CfprApSwCmclanTransport_Type()
)
cfprApSwCmclanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanTransport.setStatus("current")
_CfprApSwCmclanType_Type = CfprApNetworkConnectionType
_CfprApSwCmclanType_Object = MibTableColumn
cfprApSwCmclanType = _CfprApSwCmclanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 8, 1, 13),
    _CfprApSwCmclanType_Type()
)
cfprApSwCmclanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwCmclanType.setStatus("current")
_CfprApSwEnvStatsTable_Object = MibTable
cfprApSwEnvStatsTable = _CfprApSwEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9)
)
if mibBuilder.loadTexts:
    cfprApSwEnvStatsTable.setStatus("current")
_CfprApSwEnvStatsEntry_Object = MibTableRow
cfprApSwEnvStatsEntry = _CfprApSwEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1)
)
cfprApSwEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEnvStatsEntry.setStatus("current")
_CfprApSwEnvStatsInstanceId_Type = CfprApManagedObjectId
_CfprApSwEnvStatsInstanceId_Object = MibTableColumn
cfprApSwEnvStatsInstanceId = _CfprApSwEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 1),
    _CfprApSwEnvStatsInstanceId_Type()
)
cfprApSwEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsInstanceId.setStatus("current")
_CfprApSwEnvStatsDn_Type = CfprApManagedObjectDn
_CfprApSwEnvStatsDn_Object = MibTableColumn
cfprApSwEnvStatsDn = _CfprApSwEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 2),
    _CfprApSwEnvStatsDn_Type()
)
cfprApSwEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsDn.setStatus("current")
_CfprApSwEnvStatsRn_Type = SnmpAdminString
_CfprApSwEnvStatsRn_Object = MibTableColumn
cfprApSwEnvStatsRn = _CfprApSwEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 3),
    _CfprApSwEnvStatsRn_Type()
)
cfprApSwEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsRn.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet1_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet1_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet1 = _CfprApSwEnvStatsFanCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 4),
    _CfprApSwEnvStatsFanCtrlrInlet1_Type()
)
cfprApSwEnvStatsFanCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet1.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet1Avg_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet1Avg_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet1Avg = _CfprApSwEnvStatsFanCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 5),
    _CfprApSwEnvStatsFanCtrlrInlet1Avg_Type()
)
cfprApSwEnvStatsFanCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet1Avg.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet1Max_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet1Max_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet1Max = _CfprApSwEnvStatsFanCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 6),
    _CfprApSwEnvStatsFanCtrlrInlet1Max_Type()
)
cfprApSwEnvStatsFanCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet1Max.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet1Min_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet1Min_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet1Min = _CfprApSwEnvStatsFanCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 7),
    _CfprApSwEnvStatsFanCtrlrInlet1Min_Type()
)
cfprApSwEnvStatsFanCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet1Min.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet2_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet2_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet2 = _CfprApSwEnvStatsFanCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 8),
    _CfprApSwEnvStatsFanCtrlrInlet2_Type()
)
cfprApSwEnvStatsFanCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet2.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet2Avg_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet2Avg_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet2Avg = _CfprApSwEnvStatsFanCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 9),
    _CfprApSwEnvStatsFanCtrlrInlet2Avg_Type()
)
cfprApSwEnvStatsFanCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet2Avg.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet2Max_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet2Max_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet2Max = _CfprApSwEnvStatsFanCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 10),
    _CfprApSwEnvStatsFanCtrlrInlet2Max_Type()
)
cfprApSwEnvStatsFanCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet2Max.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet2Min_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet2Min_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet2Min = _CfprApSwEnvStatsFanCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 11),
    _CfprApSwEnvStatsFanCtrlrInlet2Min_Type()
)
cfprApSwEnvStatsFanCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet2Min.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet3_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet3_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet3 = _CfprApSwEnvStatsFanCtrlrInlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 12),
    _CfprApSwEnvStatsFanCtrlrInlet3_Type()
)
cfprApSwEnvStatsFanCtrlrInlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet3.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet3Avg_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet3Avg_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet3Avg = _CfprApSwEnvStatsFanCtrlrInlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 13),
    _CfprApSwEnvStatsFanCtrlrInlet3Avg_Type()
)
cfprApSwEnvStatsFanCtrlrInlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet3Avg.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet3Max_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet3Max_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet3Max = _CfprApSwEnvStatsFanCtrlrInlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 14),
    _CfprApSwEnvStatsFanCtrlrInlet3Max_Type()
)
cfprApSwEnvStatsFanCtrlrInlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet3Max.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet3Min_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet3Min_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet3Min = _CfprApSwEnvStatsFanCtrlrInlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 15),
    _CfprApSwEnvStatsFanCtrlrInlet3Min_Type()
)
cfprApSwEnvStatsFanCtrlrInlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet3Min.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet4_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet4_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet4 = _CfprApSwEnvStatsFanCtrlrInlet4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 16),
    _CfprApSwEnvStatsFanCtrlrInlet4_Type()
)
cfprApSwEnvStatsFanCtrlrInlet4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet4.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet4Avg_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet4Avg_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet4Avg = _CfprApSwEnvStatsFanCtrlrInlet4Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 17),
    _CfprApSwEnvStatsFanCtrlrInlet4Avg_Type()
)
cfprApSwEnvStatsFanCtrlrInlet4Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet4Avg.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet4Max_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet4Max_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet4Max = _CfprApSwEnvStatsFanCtrlrInlet4Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 18),
    _CfprApSwEnvStatsFanCtrlrInlet4Max_Type()
)
cfprApSwEnvStatsFanCtrlrInlet4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet4Max.setStatus("current")
_CfprApSwEnvStatsFanCtrlrInlet4Min_Type = Integer32
_CfprApSwEnvStatsFanCtrlrInlet4Min_Object = MibTableColumn
cfprApSwEnvStatsFanCtrlrInlet4Min = _CfprApSwEnvStatsFanCtrlrInlet4Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 19),
    _CfprApSwEnvStatsFanCtrlrInlet4Min_Type()
)
cfprApSwEnvStatsFanCtrlrInlet4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsFanCtrlrInlet4Min.setStatus("current")
_CfprApSwEnvStatsIntervals_Type = Gauge32
_CfprApSwEnvStatsIntervals_Object = MibTableColumn
cfprApSwEnvStatsIntervals = _CfprApSwEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 20),
    _CfprApSwEnvStatsIntervals_Type()
)
cfprApSwEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsIntervals.setStatus("current")
_CfprApSwEnvStatsMainBoardOutlet1_Type = Integer32
_CfprApSwEnvStatsMainBoardOutlet1_Object = MibTableColumn
cfprApSwEnvStatsMainBoardOutlet1 = _CfprApSwEnvStatsMainBoardOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 21),
    _CfprApSwEnvStatsMainBoardOutlet1_Type()
)
cfprApSwEnvStatsMainBoardOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsMainBoardOutlet1.setStatus("current")
_CfprApSwEnvStatsMainBoardOutlet1Avg_Type = Integer32
_CfprApSwEnvStatsMainBoardOutlet1Avg_Object = MibTableColumn
cfprApSwEnvStatsMainBoardOutlet1Avg = _CfprApSwEnvStatsMainBoardOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 22),
    _CfprApSwEnvStatsMainBoardOutlet1Avg_Type()
)
cfprApSwEnvStatsMainBoardOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsMainBoardOutlet1Avg.setStatus("current")
_CfprApSwEnvStatsMainBoardOutlet1Max_Type = Integer32
_CfprApSwEnvStatsMainBoardOutlet1Max_Object = MibTableColumn
cfprApSwEnvStatsMainBoardOutlet1Max = _CfprApSwEnvStatsMainBoardOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 23),
    _CfprApSwEnvStatsMainBoardOutlet1Max_Type()
)
cfprApSwEnvStatsMainBoardOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsMainBoardOutlet1Max.setStatus("current")
_CfprApSwEnvStatsMainBoardOutlet1Min_Type = Integer32
_CfprApSwEnvStatsMainBoardOutlet1Min_Object = MibTableColumn
cfprApSwEnvStatsMainBoardOutlet1Min = _CfprApSwEnvStatsMainBoardOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 24),
    _CfprApSwEnvStatsMainBoardOutlet1Min_Type()
)
cfprApSwEnvStatsMainBoardOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsMainBoardOutlet1Min.setStatus("current")
_CfprApSwEnvStatsMainBoardOutlet2_Type = Integer32
_CfprApSwEnvStatsMainBoardOutlet2_Object = MibTableColumn
cfprApSwEnvStatsMainBoardOutlet2 = _CfprApSwEnvStatsMainBoardOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 25),
    _CfprApSwEnvStatsMainBoardOutlet2_Type()
)
cfprApSwEnvStatsMainBoardOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsMainBoardOutlet2.setStatus("current")
_CfprApSwEnvStatsMainBoardOutlet2Avg_Type = Integer32
_CfprApSwEnvStatsMainBoardOutlet2Avg_Object = MibTableColumn
cfprApSwEnvStatsMainBoardOutlet2Avg = _CfprApSwEnvStatsMainBoardOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 26),
    _CfprApSwEnvStatsMainBoardOutlet2Avg_Type()
)
cfprApSwEnvStatsMainBoardOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsMainBoardOutlet2Avg.setStatus("current")
_CfprApSwEnvStatsMainBoardOutlet2Max_Type = Integer32
_CfprApSwEnvStatsMainBoardOutlet2Max_Object = MibTableColumn
cfprApSwEnvStatsMainBoardOutlet2Max = _CfprApSwEnvStatsMainBoardOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 27),
    _CfprApSwEnvStatsMainBoardOutlet2Max_Type()
)
cfprApSwEnvStatsMainBoardOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsMainBoardOutlet2Max.setStatus("current")
_CfprApSwEnvStatsMainBoardOutlet2Min_Type = Integer32
_CfprApSwEnvStatsMainBoardOutlet2Min_Object = MibTableColumn
cfprApSwEnvStatsMainBoardOutlet2Min = _CfprApSwEnvStatsMainBoardOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 28),
    _CfprApSwEnvStatsMainBoardOutlet2Min_Type()
)
cfprApSwEnvStatsMainBoardOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsMainBoardOutlet2Min.setStatus("current")
_CfprApSwEnvStatsPsuCtrlrInlet1_Type = Integer32
_CfprApSwEnvStatsPsuCtrlrInlet1_Object = MibTableColumn
cfprApSwEnvStatsPsuCtrlrInlet1 = _CfprApSwEnvStatsPsuCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 29),
    _CfprApSwEnvStatsPsuCtrlrInlet1_Type()
)
cfprApSwEnvStatsPsuCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsPsuCtrlrInlet1.setStatus("current")
_CfprApSwEnvStatsPsuCtrlrInlet1Avg_Type = Integer32
_CfprApSwEnvStatsPsuCtrlrInlet1Avg_Object = MibTableColumn
cfprApSwEnvStatsPsuCtrlrInlet1Avg = _CfprApSwEnvStatsPsuCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 30),
    _CfprApSwEnvStatsPsuCtrlrInlet1Avg_Type()
)
cfprApSwEnvStatsPsuCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsPsuCtrlrInlet1Avg.setStatus("current")
_CfprApSwEnvStatsPsuCtrlrInlet1Max_Type = Integer32
_CfprApSwEnvStatsPsuCtrlrInlet1Max_Object = MibTableColumn
cfprApSwEnvStatsPsuCtrlrInlet1Max = _CfprApSwEnvStatsPsuCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 31),
    _CfprApSwEnvStatsPsuCtrlrInlet1Max_Type()
)
cfprApSwEnvStatsPsuCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsPsuCtrlrInlet1Max.setStatus("current")
_CfprApSwEnvStatsPsuCtrlrInlet1Min_Type = Integer32
_CfprApSwEnvStatsPsuCtrlrInlet1Min_Object = MibTableColumn
cfprApSwEnvStatsPsuCtrlrInlet1Min = _CfprApSwEnvStatsPsuCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 32),
    _CfprApSwEnvStatsPsuCtrlrInlet1Min_Type()
)
cfprApSwEnvStatsPsuCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsPsuCtrlrInlet1Min.setStatus("current")
_CfprApSwEnvStatsPsuCtrlrInlet2_Type = Integer32
_CfprApSwEnvStatsPsuCtrlrInlet2_Object = MibTableColumn
cfprApSwEnvStatsPsuCtrlrInlet2 = _CfprApSwEnvStatsPsuCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 33),
    _CfprApSwEnvStatsPsuCtrlrInlet2_Type()
)
cfprApSwEnvStatsPsuCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsPsuCtrlrInlet2.setStatus("current")
_CfprApSwEnvStatsPsuCtrlrInlet2Avg_Type = Integer32
_CfprApSwEnvStatsPsuCtrlrInlet2Avg_Object = MibTableColumn
cfprApSwEnvStatsPsuCtrlrInlet2Avg = _CfprApSwEnvStatsPsuCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 34),
    _CfprApSwEnvStatsPsuCtrlrInlet2Avg_Type()
)
cfprApSwEnvStatsPsuCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsPsuCtrlrInlet2Avg.setStatus("current")
_CfprApSwEnvStatsPsuCtrlrInlet2Max_Type = Integer32
_CfprApSwEnvStatsPsuCtrlrInlet2Max_Object = MibTableColumn
cfprApSwEnvStatsPsuCtrlrInlet2Max = _CfprApSwEnvStatsPsuCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 35),
    _CfprApSwEnvStatsPsuCtrlrInlet2Max_Type()
)
cfprApSwEnvStatsPsuCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsPsuCtrlrInlet2Max.setStatus("current")
_CfprApSwEnvStatsPsuCtrlrInlet2Min_Type = Integer32
_CfprApSwEnvStatsPsuCtrlrInlet2Min_Object = MibTableColumn
cfprApSwEnvStatsPsuCtrlrInlet2Min = _CfprApSwEnvStatsPsuCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 36),
    _CfprApSwEnvStatsPsuCtrlrInlet2Min_Type()
)
cfprApSwEnvStatsPsuCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsPsuCtrlrInlet2Min.setStatus("current")
_CfprApSwEnvStatsSuspect_Type = TruthValue
_CfprApSwEnvStatsSuspect_Object = MibTableColumn
cfprApSwEnvStatsSuspect = _CfprApSwEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 37),
    _CfprApSwEnvStatsSuspect_Type()
)
cfprApSwEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsSuspect.setStatus("current")
_CfprApSwEnvStatsThresholded_Type = CfprApSwEnvStatsThresholded
_CfprApSwEnvStatsThresholded_Object = MibTableColumn
cfprApSwEnvStatsThresholded = _CfprApSwEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 38),
    _CfprApSwEnvStatsThresholded_Type()
)
cfprApSwEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsThresholded.setStatus("current")
_CfprApSwEnvStatsTimeCollected_Type = DateAndTime
_CfprApSwEnvStatsTimeCollected_Object = MibTableColumn
cfprApSwEnvStatsTimeCollected = _CfprApSwEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 39),
    _CfprApSwEnvStatsTimeCollected_Type()
)
cfprApSwEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsTimeCollected.setStatus("current")
_CfprApSwEnvStatsUpdate_Type = Gauge32
_CfprApSwEnvStatsUpdate_Object = MibTableColumn
cfprApSwEnvStatsUpdate = _CfprApSwEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 9, 1, 40),
    _CfprApSwEnvStatsUpdate_Type()
)
cfprApSwEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsUpdate.setStatus("current")
_CfprApSwEnvStatsHistTable_Object = MibTable
cfprApSwEnvStatsHistTable = _CfprApSwEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10)
)
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistTable.setStatus("current")
_CfprApSwEnvStatsHistEntry_Object = MibTableRow
cfprApSwEnvStatsHistEntry = _CfprApSwEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1)
)
cfprApSwEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistEntry.setStatus("current")
_CfprApSwEnvStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApSwEnvStatsHistInstanceId_Object = MibTableColumn
cfprApSwEnvStatsHistInstanceId = _CfprApSwEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 1),
    _CfprApSwEnvStatsHistInstanceId_Type()
)
cfprApSwEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistInstanceId.setStatus("current")
_CfprApSwEnvStatsHistDn_Type = CfprApManagedObjectDn
_CfprApSwEnvStatsHistDn_Object = MibTableColumn
cfprApSwEnvStatsHistDn = _CfprApSwEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 2),
    _CfprApSwEnvStatsHistDn_Type()
)
cfprApSwEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistDn.setStatus("current")
_CfprApSwEnvStatsHistRn_Type = SnmpAdminString
_CfprApSwEnvStatsHistRn_Object = MibTableColumn
cfprApSwEnvStatsHistRn = _CfprApSwEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 3),
    _CfprApSwEnvStatsHistRn_Type()
)
cfprApSwEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistRn.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet1_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet1_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet1 = _CfprApSwEnvStatsHistFanCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 4),
    _CfprApSwEnvStatsHistFanCtrlrInlet1_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet1.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet1Avg_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet1Avg_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet1Avg = _CfprApSwEnvStatsHistFanCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 5),
    _CfprApSwEnvStatsHistFanCtrlrInlet1Avg_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet1Avg.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet1Max_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet1Max_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet1Max = _CfprApSwEnvStatsHistFanCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 6),
    _CfprApSwEnvStatsHistFanCtrlrInlet1Max_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet1Max.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet1Min_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet1Min_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet1Min = _CfprApSwEnvStatsHistFanCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 7),
    _CfprApSwEnvStatsHistFanCtrlrInlet1Min_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet1Min.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet2_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet2_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet2 = _CfprApSwEnvStatsHistFanCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 8),
    _CfprApSwEnvStatsHistFanCtrlrInlet2_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet2.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet2Avg_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet2Avg_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet2Avg = _CfprApSwEnvStatsHistFanCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 9),
    _CfprApSwEnvStatsHistFanCtrlrInlet2Avg_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet2Avg.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet2Max_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet2Max_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet2Max = _CfprApSwEnvStatsHistFanCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 10),
    _CfprApSwEnvStatsHistFanCtrlrInlet2Max_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet2Max.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet2Min_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet2Min_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet2Min = _CfprApSwEnvStatsHistFanCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 11),
    _CfprApSwEnvStatsHistFanCtrlrInlet2Min_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet2Min.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet3_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet3_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet3 = _CfprApSwEnvStatsHistFanCtrlrInlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 12),
    _CfprApSwEnvStatsHistFanCtrlrInlet3_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet3.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet3Avg_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet3Avg_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet3Avg = _CfprApSwEnvStatsHistFanCtrlrInlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 13),
    _CfprApSwEnvStatsHistFanCtrlrInlet3Avg_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet3Avg.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet3Max_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet3Max_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet3Max = _CfprApSwEnvStatsHistFanCtrlrInlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 14),
    _CfprApSwEnvStatsHistFanCtrlrInlet3Max_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet3Max.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet3Min_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet3Min_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet3Min = _CfprApSwEnvStatsHistFanCtrlrInlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 15),
    _CfprApSwEnvStatsHistFanCtrlrInlet3Min_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet3Min.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet4_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet4_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet4 = _CfprApSwEnvStatsHistFanCtrlrInlet4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 16),
    _CfprApSwEnvStatsHistFanCtrlrInlet4_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet4.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet4Avg_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet4Avg_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet4Avg = _CfprApSwEnvStatsHistFanCtrlrInlet4Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 17),
    _CfprApSwEnvStatsHistFanCtrlrInlet4Avg_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet4Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet4Avg.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet4Max_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet4Max_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet4Max = _CfprApSwEnvStatsHistFanCtrlrInlet4Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 18),
    _CfprApSwEnvStatsHistFanCtrlrInlet4Max_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet4Max.setStatus("current")
_CfprApSwEnvStatsHistFanCtrlrInlet4Min_Type = Integer32
_CfprApSwEnvStatsHistFanCtrlrInlet4Min_Object = MibTableColumn
cfprApSwEnvStatsHistFanCtrlrInlet4Min = _CfprApSwEnvStatsHistFanCtrlrInlet4Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 19),
    _CfprApSwEnvStatsHistFanCtrlrInlet4Min_Type()
)
cfprApSwEnvStatsHistFanCtrlrInlet4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistFanCtrlrInlet4Min.setStatus("current")
_CfprApSwEnvStatsHistId_Type = Unsigned64
_CfprApSwEnvStatsHistId_Object = MibTableColumn
cfprApSwEnvStatsHistId = _CfprApSwEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 20),
    _CfprApSwEnvStatsHistId_Type()
)
cfprApSwEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistId.setStatus("current")
_CfprApSwEnvStatsHistMainBoardOutlet1_Type = Integer32
_CfprApSwEnvStatsHistMainBoardOutlet1_Object = MibTableColumn
cfprApSwEnvStatsHistMainBoardOutlet1 = _CfprApSwEnvStatsHistMainBoardOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 21),
    _CfprApSwEnvStatsHistMainBoardOutlet1_Type()
)
cfprApSwEnvStatsHistMainBoardOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMainBoardOutlet1.setStatus("current")
_CfprApSwEnvStatsHistMainBoardOutlet1Avg_Type = Integer32
_CfprApSwEnvStatsHistMainBoardOutlet1Avg_Object = MibTableColumn
cfprApSwEnvStatsHistMainBoardOutlet1Avg = _CfprApSwEnvStatsHistMainBoardOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 22),
    _CfprApSwEnvStatsHistMainBoardOutlet1Avg_Type()
)
cfprApSwEnvStatsHistMainBoardOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMainBoardOutlet1Avg.setStatus("current")
_CfprApSwEnvStatsHistMainBoardOutlet1Max_Type = Integer32
_CfprApSwEnvStatsHistMainBoardOutlet1Max_Object = MibTableColumn
cfprApSwEnvStatsHistMainBoardOutlet1Max = _CfprApSwEnvStatsHistMainBoardOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 23),
    _CfprApSwEnvStatsHistMainBoardOutlet1Max_Type()
)
cfprApSwEnvStatsHistMainBoardOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMainBoardOutlet1Max.setStatus("current")
_CfprApSwEnvStatsHistMainBoardOutlet1Min_Type = Integer32
_CfprApSwEnvStatsHistMainBoardOutlet1Min_Object = MibTableColumn
cfprApSwEnvStatsHistMainBoardOutlet1Min = _CfprApSwEnvStatsHistMainBoardOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 24),
    _CfprApSwEnvStatsHistMainBoardOutlet1Min_Type()
)
cfprApSwEnvStatsHistMainBoardOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMainBoardOutlet1Min.setStatus("current")
_CfprApSwEnvStatsHistMainBoardOutlet2_Type = Integer32
_CfprApSwEnvStatsHistMainBoardOutlet2_Object = MibTableColumn
cfprApSwEnvStatsHistMainBoardOutlet2 = _CfprApSwEnvStatsHistMainBoardOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 25),
    _CfprApSwEnvStatsHistMainBoardOutlet2_Type()
)
cfprApSwEnvStatsHistMainBoardOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMainBoardOutlet2.setStatus("current")
_CfprApSwEnvStatsHistMainBoardOutlet2Avg_Type = Integer32
_CfprApSwEnvStatsHistMainBoardOutlet2Avg_Object = MibTableColumn
cfprApSwEnvStatsHistMainBoardOutlet2Avg = _CfprApSwEnvStatsHistMainBoardOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 26),
    _CfprApSwEnvStatsHistMainBoardOutlet2Avg_Type()
)
cfprApSwEnvStatsHistMainBoardOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMainBoardOutlet2Avg.setStatus("current")
_CfprApSwEnvStatsHistMainBoardOutlet2Max_Type = Integer32
_CfprApSwEnvStatsHistMainBoardOutlet2Max_Object = MibTableColumn
cfprApSwEnvStatsHistMainBoardOutlet2Max = _CfprApSwEnvStatsHistMainBoardOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 27),
    _CfprApSwEnvStatsHistMainBoardOutlet2Max_Type()
)
cfprApSwEnvStatsHistMainBoardOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMainBoardOutlet2Max.setStatus("current")
_CfprApSwEnvStatsHistMainBoardOutlet2Min_Type = Integer32
_CfprApSwEnvStatsHistMainBoardOutlet2Min_Object = MibTableColumn
cfprApSwEnvStatsHistMainBoardOutlet2Min = _CfprApSwEnvStatsHistMainBoardOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 28),
    _CfprApSwEnvStatsHistMainBoardOutlet2Min_Type()
)
cfprApSwEnvStatsHistMainBoardOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMainBoardOutlet2Min.setStatus("current")
_CfprApSwEnvStatsHistMostRecent_Type = TruthValue
_CfprApSwEnvStatsHistMostRecent_Object = MibTableColumn
cfprApSwEnvStatsHistMostRecent = _CfprApSwEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 29),
    _CfprApSwEnvStatsHistMostRecent_Type()
)
cfprApSwEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistMostRecent.setStatus("current")
_CfprApSwEnvStatsHistPsuCtrlrInlet1_Type = Integer32
_CfprApSwEnvStatsHistPsuCtrlrInlet1_Object = MibTableColumn
cfprApSwEnvStatsHistPsuCtrlrInlet1 = _CfprApSwEnvStatsHistPsuCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 30),
    _CfprApSwEnvStatsHistPsuCtrlrInlet1_Type()
)
cfprApSwEnvStatsHistPsuCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistPsuCtrlrInlet1.setStatus("current")
_CfprApSwEnvStatsHistPsuCtrlrInlet1Avg_Type = Integer32
_CfprApSwEnvStatsHistPsuCtrlrInlet1Avg_Object = MibTableColumn
cfprApSwEnvStatsHistPsuCtrlrInlet1Avg = _CfprApSwEnvStatsHistPsuCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 31),
    _CfprApSwEnvStatsHistPsuCtrlrInlet1Avg_Type()
)
cfprApSwEnvStatsHistPsuCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistPsuCtrlrInlet1Avg.setStatus("current")
_CfprApSwEnvStatsHistPsuCtrlrInlet1Max_Type = Integer32
_CfprApSwEnvStatsHistPsuCtrlrInlet1Max_Object = MibTableColumn
cfprApSwEnvStatsHistPsuCtrlrInlet1Max = _CfprApSwEnvStatsHistPsuCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 32),
    _CfprApSwEnvStatsHistPsuCtrlrInlet1Max_Type()
)
cfprApSwEnvStatsHistPsuCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistPsuCtrlrInlet1Max.setStatus("current")
_CfprApSwEnvStatsHistPsuCtrlrInlet1Min_Type = Integer32
_CfprApSwEnvStatsHistPsuCtrlrInlet1Min_Object = MibTableColumn
cfprApSwEnvStatsHistPsuCtrlrInlet1Min = _CfprApSwEnvStatsHistPsuCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 33),
    _CfprApSwEnvStatsHistPsuCtrlrInlet1Min_Type()
)
cfprApSwEnvStatsHistPsuCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistPsuCtrlrInlet1Min.setStatus("current")
_CfprApSwEnvStatsHistPsuCtrlrInlet2_Type = Integer32
_CfprApSwEnvStatsHistPsuCtrlrInlet2_Object = MibTableColumn
cfprApSwEnvStatsHistPsuCtrlrInlet2 = _CfprApSwEnvStatsHistPsuCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 34),
    _CfprApSwEnvStatsHistPsuCtrlrInlet2_Type()
)
cfprApSwEnvStatsHistPsuCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistPsuCtrlrInlet2.setStatus("current")
_CfprApSwEnvStatsHistPsuCtrlrInlet2Avg_Type = Integer32
_CfprApSwEnvStatsHistPsuCtrlrInlet2Avg_Object = MibTableColumn
cfprApSwEnvStatsHistPsuCtrlrInlet2Avg = _CfprApSwEnvStatsHistPsuCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 35),
    _CfprApSwEnvStatsHistPsuCtrlrInlet2Avg_Type()
)
cfprApSwEnvStatsHistPsuCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistPsuCtrlrInlet2Avg.setStatus("current")
_CfprApSwEnvStatsHistPsuCtrlrInlet2Max_Type = Integer32
_CfprApSwEnvStatsHistPsuCtrlrInlet2Max_Object = MibTableColumn
cfprApSwEnvStatsHistPsuCtrlrInlet2Max = _CfprApSwEnvStatsHistPsuCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 36),
    _CfprApSwEnvStatsHistPsuCtrlrInlet2Max_Type()
)
cfprApSwEnvStatsHistPsuCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistPsuCtrlrInlet2Max.setStatus("current")
_CfprApSwEnvStatsHistPsuCtrlrInlet2Min_Type = Integer32
_CfprApSwEnvStatsHistPsuCtrlrInlet2Min_Object = MibTableColumn
cfprApSwEnvStatsHistPsuCtrlrInlet2Min = _CfprApSwEnvStatsHistPsuCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 37),
    _CfprApSwEnvStatsHistPsuCtrlrInlet2Min_Type()
)
cfprApSwEnvStatsHistPsuCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistPsuCtrlrInlet2Min.setStatus("current")
_CfprApSwEnvStatsHistSuspect_Type = TruthValue
_CfprApSwEnvStatsHistSuspect_Object = MibTableColumn
cfprApSwEnvStatsHistSuspect = _CfprApSwEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 38),
    _CfprApSwEnvStatsHistSuspect_Type()
)
cfprApSwEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistSuspect.setStatus("current")
_CfprApSwEnvStatsHistThresholded_Type = CfprApSwEnvStatsHistThresholded
_CfprApSwEnvStatsHistThresholded_Object = MibTableColumn
cfprApSwEnvStatsHistThresholded = _CfprApSwEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 39),
    _CfprApSwEnvStatsHistThresholded_Type()
)
cfprApSwEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistThresholded.setStatus("current")
_CfprApSwEnvStatsHistTimeCollected_Type = DateAndTime
_CfprApSwEnvStatsHistTimeCollected_Object = MibTableColumn
cfprApSwEnvStatsHistTimeCollected = _CfprApSwEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 10, 1, 40),
    _CfprApSwEnvStatsHistTimeCollected_Type()
)
cfprApSwEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEnvStatsHistTimeCollected.setStatus("current")
_CfprApSwEthEstcEpTable_Object = MibTable
cfprApSwEthEstcEpTable = _CfprApSwEthEstcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11)
)
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpTable.setStatus("current")
_CfprApSwEthEstcEpEntry_Object = MibTableRow
cfprApSwEthEstcEpEntry = _CfprApSwEthEstcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1)
)
cfprApSwEthEstcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthEstcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpEntry.setStatus("current")
_CfprApSwEthEstcEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthEstcEpInstanceId_Object = MibTableColumn
cfprApSwEthEstcEpInstanceId = _CfprApSwEthEstcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 1),
    _CfprApSwEthEstcEpInstanceId_Type()
)
cfprApSwEthEstcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpInstanceId.setStatus("current")
_CfprApSwEthEstcEpDn_Type = CfprApManagedObjectDn
_CfprApSwEthEstcEpDn_Object = MibTableColumn
cfprApSwEthEstcEpDn = _CfprApSwEthEstcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 2),
    _CfprApSwEthEstcEpDn_Type()
)
cfprApSwEthEstcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpDn.setStatus("current")
_CfprApSwEthEstcEpRn_Type = SnmpAdminString
_CfprApSwEthEstcEpRn_Object = MibTableColumn
cfprApSwEthEstcEpRn = _CfprApSwEthEstcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 3),
    _CfprApSwEthEstcEpRn_Type()
)
cfprApSwEthEstcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpRn.setStatus("current")
_CfprApSwEthEstcEpAdminSpeed_Type = CfprApPortEthSpeed
_CfprApSwEthEstcEpAdminSpeed_Object = MibTableColumn
cfprApSwEthEstcEpAdminSpeed = _CfprApSwEthEstcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 4),
    _CfprApSwEthEstcEpAdminSpeed_Type()
)
cfprApSwEthEstcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpAdminSpeed.setStatus("current")
_CfprApSwEthEstcEpAdminState_Type = CfprApFabricAdminState
_CfprApSwEthEstcEpAdminState_Object = MibTableColumn
cfprApSwEthEstcEpAdminState = _CfprApSwEthEstcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 5),
    _CfprApSwEthEstcEpAdminState_Type()
)
cfprApSwEthEstcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpAdminState.setStatus("current")
_CfprApSwEthEstcEpAggrPortId_Type = Gauge32
_CfprApSwEthEstcEpAggrPortId_Object = MibTableColumn
cfprApSwEthEstcEpAggrPortId = _CfprApSwEthEstcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 6),
    _CfprApSwEthEstcEpAggrPortId_Type()
)
cfprApSwEthEstcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpAggrPortId.setStatus("current")
_CfprApSwEthEstcEpBorderAggrPortId_Type = Gauge32
_CfprApSwEthEstcEpBorderAggrPortId_Object = MibTableColumn
cfprApSwEthEstcEpBorderAggrPortId = _CfprApSwEthEstcEpBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 7),
    _CfprApSwEthEstcEpBorderAggrPortId_Type()
)
cfprApSwEthEstcEpBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpBorderAggrPortId.setStatus("current")
_CfprApSwEthEstcEpBorderPortId_Type = Gauge32
_CfprApSwEthEstcEpBorderPortId_Object = MibTableColumn
cfprApSwEthEstcEpBorderPortId = _CfprApSwEthEstcEpBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 8),
    _CfprApSwEthEstcEpBorderPortId_Type()
)
cfprApSwEthEstcEpBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpBorderPortId.setStatus("current")
_CfprApSwEthEstcEpBorderSlotId_Type = Gauge32
_CfprApSwEthEstcEpBorderSlotId_Object = MibTableColumn
cfprApSwEthEstcEpBorderSlotId = _CfprApSwEthEstcEpBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 9),
    _CfprApSwEthEstcEpBorderSlotId_Type()
)
cfprApSwEthEstcEpBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpBorderSlotId.setStatus("current")
_CfprApSwEthEstcEpCdp_Type = CfprApNwctrlAdminState
_CfprApSwEthEstcEpCdp_Object = MibTableColumn
cfprApSwEthEstcEpCdp = _CfprApSwEthEstcEpCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 10),
    _CfprApSwEthEstcEpCdp_Type()
)
cfprApSwEthEstcEpCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpCdp.setStatus("current")
_CfprApSwEthEstcEpChassisId_Type = Gauge32
_CfprApSwEthEstcEpChassisId_Object = MibTableColumn
cfprApSwEthEstcEpChassisId = _CfprApSwEthEstcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 11),
    _CfprApSwEthEstcEpChassisId_Type()
)
cfprApSwEthEstcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpChassisId.setStatus("current")
_CfprApSwEthEstcEpCosValue_Type = Gauge32
_CfprApSwEthEstcEpCosValue_Object = MibTableColumn
cfprApSwEthEstcEpCosValue = _CfprApSwEthEstcEpCosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 12),
    _CfprApSwEthEstcEpCosValue_Type()
)
cfprApSwEthEstcEpCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpCosValue.setStatus("current")
_CfprApSwEthEstcEpEpDn_Type = SnmpAdminString
_CfprApSwEthEstcEpEpDn_Object = MibTableColumn
cfprApSwEthEstcEpEpDn = _CfprApSwEthEstcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 13),
    _CfprApSwEthEstcEpEpDn_Type()
)
cfprApSwEthEstcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpEpDn.setStatus("current")
_CfprApSwEthEstcEpForgeMac_Type = CfprApDpsecForgedTransmit
_CfprApSwEthEstcEpForgeMac_Object = MibTableColumn
cfprApSwEthEstcEpForgeMac = _CfprApSwEthEstcEpForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 14),
    _CfprApSwEthEstcEpForgeMac_Type()
)
cfprApSwEthEstcEpForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpForgeMac.setStatus("current")
_CfprApSwEthEstcEpIfRole_Type = CfprApNetworkPortRole
_CfprApSwEthEstcEpIfRole_Object = MibTableColumn
cfprApSwEthEstcEpIfRole = _CfprApSwEthEstcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 15),
    _CfprApSwEthEstcEpIfRole_Type()
)
cfprApSwEthEstcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpIfRole.setStatus("current")
_CfprApSwEthEstcEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwEthEstcEpIfType_Object = MibTableColumn
cfprApSwEthEstcEpIfType = _CfprApSwEthEstcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 16),
    _CfprApSwEthEstcEpIfType_Type()
)
cfprApSwEthEstcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpIfType.setStatus("current")
_CfprApSwEthEstcEpLc_Type = CfprApSwPIoEpLc
_CfprApSwEthEstcEpLc_Object = MibTableColumn
cfprApSwEthEstcEpLc = _CfprApSwEthEstcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 17),
    _CfprApSwEthEstcEpLc_Type()
)
cfprApSwEthEstcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpLc.setStatus("current")
_CfprApSwEthEstcEpLocale_Type = CfprApSwEstcEpLocale
_CfprApSwEthEstcEpLocale_Object = MibTableColumn
cfprApSwEthEstcEpLocale = _CfprApSwEthEstcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 18),
    _CfprApSwEthEstcEpLocale_Type()
)
cfprApSwEthEstcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpLocale.setStatus("current")
_CfprApSwEthEstcEpName_Type = SnmpAdminString
_CfprApSwEthEstcEpName_Object = MibTableColumn
cfprApSwEthEstcEpName = _CfprApSwEthEstcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 19),
    _CfprApSwEthEstcEpName_Type()
)
cfprApSwEthEstcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpName.setStatus("current")
_CfprApSwEthEstcEpPcId_Type = Gauge32
_CfprApSwEthEstcEpPcId_Object = MibTableColumn
cfprApSwEthEstcEpPcId = _CfprApSwEthEstcEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 20),
    _CfprApSwEthEstcEpPcId_Type()
)
cfprApSwEthEstcEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPcId.setStatus("current")
_CfprApSwEthEstcEpPeerAggrPortId_Type = Gauge32
_CfprApSwEthEstcEpPeerAggrPortId_Object = MibTableColumn
cfprApSwEthEstcEpPeerAggrPortId = _CfprApSwEthEstcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 21),
    _CfprApSwEthEstcEpPeerAggrPortId_Type()
)
cfprApSwEthEstcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPeerAggrPortId.setStatus("current")
_CfprApSwEthEstcEpPeerChassisId_Type = Gauge32
_CfprApSwEthEstcEpPeerChassisId_Object = MibTableColumn
cfprApSwEthEstcEpPeerChassisId = _CfprApSwEthEstcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 22),
    _CfprApSwEthEstcEpPeerChassisId_Type()
)
cfprApSwEthEstcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPeerChassisId.setStatus("current")
_CfprApSwEthEstcEpPeerDn_Type = SnmpAdminString
_CfprApSwEthEstcEpPeerDn_Object = MibTableColumn
cfprApSwEthEstcEpPeerDn = _CfprApSwEthEstcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 23),
    _CfprApSwEthEstcEpPeerDn_Type()
)
cfprApSwEthEstcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPeerDn.setStatus("current")
_CfprApSwEthEstcEpPeerPortId_Type = Gauge32
_CfprApSwEthEstcEpPeerPortId_Object = MibTableColumn
cfprApSwEthEstcEpPeerPortId = _CfprApSwEthEstcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 24),
    _CfprApSwEthEstcEpPeerPortId_Type()
)
cfprApSwEthEstcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPeerPortId.setStatus("current")
_CfprApSwEthEstcEpPeerSlotId_Type = Gauge32
_CfprApSwEthEstcEpPeerSlotId_Object = MibTableColumn
cfprApSwEthEstcEpPeerSlotId = _CfprApSwEthEstcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 25),
    _CfprApSwEthEstcEpPeerSlotId_Type()
)
cfprApSwEthEstcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPeerSlotId.setStatus("current")
_CfprApSwEthEstcEpPinGroupName_Type = SnmpAdminString
_CfprApSwEthEstcEpPinGroupName_Object = MibTableColumn
cfprApSwEthEstcEpPinGroupName = _CfprApSwEthEstcEpPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 26),
    _CfprApSwEthEstcEpPinGroupName_Type()
)
cfprApSwEthEstcEpPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPinGroupName.setStatus("current")
_CfprApSwEthEstcEpPortId_Type = Gauge32
_CfprApSwEthEstcEpPortId_Object = MibTableColumn
cfprApSwEthEstcEpPortId = _CfprApSwEthEstcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 27),
    _CfprApSwEthEstcEpPortId_Type()
)
cfprApSwEthEstcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPortId.setStatus("current")
_CfprApSwEthEstcEpPortMode_Type = CfprApFabricEthEstcPortMode
_CfprApSwEthEstcEpPortMode_Object = MibTableColumn
cfprApSwEthEstcEpPortMode = _CfprApSwEthEstcEpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 28),
    _CfprApSwEthEstcEpPortMode_Type()
)
cfprApSwEthEstcEpPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPortMode.setStatus("current")
_CfprApSwEthEstcEpPriorityFlowCtrl_Type = CfprApFlowctrlPriorityPause
_CfprApSwEthEstcEpPriorityFlowCtrl_Object = MibTableColumn
cfprApSwEthEstcEpPriorityFlowCtrl = _CfprApSwEthEstcEpPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 29),
    _CfprApSwEthEstcEpPriorityFlowCtrl_Type()
)
cfprApSwEthEstcEpPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpPriorityFlowCtrl.setStatus("current")
_CfprApSwEthEstcEpRecvFlowCtrl_Type = CfprApFlowctrlFlowControl
_CfprApSwEthEstcEpRecvFlowCtrl_Object = MibTableColumn
cfprApSwEthEstcEpRecvFlowCtrl = _CfprApSwEthEstcEpRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 30),
    _CfprApSwEthEstcEpRecvFlowCtrl_Type()
)
cfprApSwEthEstcEpRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpRecvFlowCtrl.setStatus("current")
_CfprApSwEthEstcEpSendFlowCtrl_Type = CfprApFlowctrlFlowControl
_CfprApSwEthEstcEpSendFlowCtrl_Object = MibTableColumn
cfprApSwEthEstcEpSendFlowCtrl = _CfprApSwEthEstcEpSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 31),
    _CfprApSwEthEstcEpSendFlowCtrl_Type()
)
cfprApSwEthEstcEpSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpSendFlowCtrl.setStatus("current")
_CfprApSwEthEstcEpSlotId_Type = Gauge32
_CfprApSwEthEstcEpSlotId_Object = MibTableColumn
cfprApSwEthEstcEpSlotId = _CfprApSwEthEstcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 32),
    _CfprApSwEthEstcEpSlotId_Type()
)
cfprApSwEthEstcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpSlotId.setStatus("current")
_CfprApSwEthEstcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthEstcEpSwitchId_Object = MibTableColumn
cfprApSwEthEstcEpSwitchId = _CfprApSwEthEstcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 33),
    _CfprApSwEthEstcEpSwitchId_Type()
)
cfprApSwEthEstcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpSwitchId.setStatus("current")
_CfprApSwEthEstcEpTransport_Type = CfprApSwEthEstcEpTransport
_CfprApSwEthEstcEpTransport_Object = MibTableColumn
cfprApSwEthEstcEpTransport = _CfprApSwEthEstcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 34),
    _CfprApSwEthEstcEpTransport_Type()
)
cfprApSwEthEstcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpTransport.setStatus("current")
_CfprApSwEthEstcEpType_Type = CfprApNetworkConnectionType
_CfprApSwEthEstcEpType_Object = MibTableColumn
cfprApSwEthEstcEpType = _CfprApSwEthEstcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 35),
    _CfprApSwEthEstcEpType_Type()
)
cfprApSwEthEstcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpType.setStatus("current")
_CfprApSwEthEstcEpUplinkFailAction_Type = CfprApNwctrlLinkFailAction
_CfprApSwEthEstcEpUplinkFailAction_Object = MibTableColumn
cfprApSwEthEstcEpUplinkFailAction = _CfprApSwEthEstcEpUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 11, 1, 36),
    _CfprApSwEthEstcEpUplinkFailAction_Type()
)
cfprApSwEthEstcEpUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcEpUplinkFailAction.setStatus("current")
_CfprApSwEthEstcPcTable_Object = MibTable
cfprApSwEthEstcPcTable = _CfprApSwEthEstcPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12)
)
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcTable.setStatus("current")
_CfprApSwEthEstcPcEntry_Object = MibTableRow
cfprApSwEthEstcPcEntry = _CfprApSwEthEstcPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1)
)
cfprApSwEthEstcPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthEstcPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcEntry.setStatus("current")
_CfprApSwEthEstcPcInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthEstcPcInstanceId_Object = MibTableColumn
cfprApSwEthEstcPcInstanceId = _CfprApSwEthEstcPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 1),
    _CfprApSwEthEstcPcInstanceId_Type()
)
cfprApSwEthEstcPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcInstanceId.setStatus("current")
_CfprApSwEthEstcPcDn_Type = CfprApManagedObjectDn
_CfprApSwEthEstcPcDn_Object = MibTableColumn
cfprApSwEthEstcPcDn = _CfprApSwEthEstcPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 2),
    _CfprApSwEthEstcPcDn_Type()
)
cfprApSwEthEstcPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcDn.setStatus("current")
_CfprApSwEthEstcPcRn_Type = SnmpAdminString
_CfprApSwEthEstcPcRn_Object = MibTableColumn
cfprApSwEthEstcPcRn = _CfprApSwEthEstcPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 3),
    _CfprApSwEthEstcPcRn_Type()
)
cfprApSwEthEstcPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcRn.setStatus("current")
_CfprApSwEthEstcPcAdminSpeed_Type = CfprApPortEthSpeed
_CfprApSwEthEstcPcAdminSpeed_Object = MibTableColumn
cfprApSwEthEstcPcAdminSpeed = _CfprApSwEthEstcPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 4),
    _CfprApSwEthEstcPcAdminSpeed_Type()
)
cfprApSwEthEstcPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcAdminSpeed.setStatus("current")
_CfprApSwEthEstcPcAdminState_Type = CfprApFabricAdminState
_CfprApSwEthEstcPcAdminState_Object = MibTableColumn
cfprApSwEthEstcPcAdminState = _CfprApSwEthEstcPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 5),
    _CfprApSwEthEstcPcAdminState_Type()
)
cfprApSwEthEstcPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcAdminState.setStatus("current")
_CfprApSwEthEstcPcBorderAggrPortId_Type = Gauge32
_CfprApSwEthEstcPcBorderAggrPortId_Object = MibTableColumn
cfprApSwEthEstcPcBorderAggrPortId = _CfprApSwEthEstcPcBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 6),
    _CfprApSwEthEstcPcBorderAggrPortId_Type()
)
cfprApSwEthEstcPcBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcBorderAggrPortId.setStatus("current")
_CfprApSwEthEstcPcBorderPortId_Type = Gauge32
_CfprApSwEthEstcPcBorderPortId_Object = MibTableColumn
cfprApSwEthEstcPcBorderPortId = _CfprApSwEthEstcPcBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 7),
    _CfprApSwEthEstcPcBorderPortId_Type()
)
cfprApSwEthEstcPcBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcBorderPortId.setStatus("current")
_CfprApSwEthEstcPcBorderSlotId_Type = Gauge32
_CfprApSwEthEstcPcBorderSlotId_Object = MibTableColumn
cfprApSwEthEstcPcBorderSlotId = _CfprApSwEthEstcPcBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 8),
    _CfprApSwEthEstcPcBorderSlotId_Type()
)
cfprApSwEthEstcPcBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcBorderSlotId.setStatus("current")
_CfprApSwEthEstcPcCdp_Type = CfprApNwctrlAdminState
_CfprApSwEthEstcPcCdp_Object = MibTableColumn
cfprApSwEthEstcPcCdp = _CfprApSwEthEstcPcCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 9),
    _CfprApSwEthEstcPcCdp_Type()
)
cfprApSwEthEstcPcCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcCdp.setStatus("current")
_CfprApSwEthEstcPcCosValue_Type = Gauge32
_CfprApSwEthEstcPcCosValue_Object = MibTableColumn
cfprApSwEthEstcPcCosValue = _CfprApSwEthEstcPcCosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 10),
    _CfprApSwEthEstcPcCosValue_Type()
)
cfprApSwEthEstcPcCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcCosValue.setStatus("current")
_CfprApSwEthEstcPcEpDn_Type = SnmpAdminString
_CfprApSwEthEstcPcEpDn_Object = MibTableColumn
cfprApSwEthEstcPcEpDn = _CfprApSwEthEstcPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 11),
    _CfprApSwEthEstcPcEpDn_Type()
)
cfprApSwEthEstcPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcEpDn.setStatus("current")
_CfprApSwEthEstcPcForgeMac_Type = CfprApDpsecForgedTransmit
_CfprApSwEthEstcPcForgeMac_Object = MibTableColumn
cfprApSwEthEstcPcForgeMac = _CfprApSwEthEstcPcForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 12),
    _CfprApSwEthEstcPcForgeMac_Type()
)
cfprApSwEthEstcPcForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcForgeMac.setStatus("current")
_CfprApSwEthEstcPcIfRole_Type = CfprApSwLanPcIfRole
_CfprApSwEthEstcPcIfRole_Object = MibTableColumn
cfprApSwEthEstcPcIfRole = _CfprApSwEthEstcPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 13),
    _CfprApSwEthEstcPcIfRole_Type()
)
cfprApSwEthEstcPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcIfRole.setStatus("current")
_CfprApSwEthEstcPcIfType_Type = CfprApSwCIoEpIfType
_CfprApSwEthEstcPcIfType_Object = MibTableColumn
cfprApSwEthEstcPcIfType = _CfprApSwEthEstcPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 14),
    _CfprApSwEthEstcPcIfType_Type()
)
cfprApSwEthEstcPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcIfType.setStatus("current")
_CfprApSwEthEstcPcLacpFastTimer_Type = TruthValue
_CfprApSwEthEstcPcLacpFastTimer_Object = MibTableColumn
cfprApSwEthEstcPcLacpFastTimer = _CfprApSwEthEstcPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 15),
    _CfprApSwEthEstcPcLacpFastTimer_Type()
)
cfprApSwEthEstcPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcLacpFastTimer.setStatus("current")
_CfprApSwEthEstcPcLacpSuspendIndividual_Type = TruthValue
_CfprApSwEthEstcPcLacpSuspendIndividual_Object = MibTableColumn
cfprApSwEthEstcPcLacpSuspendIndividual = _CfprApSwEthEstcPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 16),
    _CfprApSwEthEstcPcLacpSuspendIndividual_Type()
)
cfprApSwEthEstcPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcLacpSuspendIndividual.setStatus("current")
_CfprApSwEthEstcPcLocale_Type = CfprApSwBorderPcLocale
_CfprApSwEthEstcPcLocale_Object = MibTableColumn
cfprApSwEthEstcPcLocale = _CfprApSwEthEstcPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 17),
    _CfprApSwEthEstcPcLocale_Type()
)
cfprApSwEthEstcPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcLocale.setStatus("current")
_CfprApSwEthEstcPcMonTrafDir_Type = CfprApFabricTrafficDirection
_CfprApSwEthEstcPcMonTrafDir_Object = MibTableColumn
cfprApSwEthEstcPcMonTrafDir = _CfprApSwEthEstcPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 18),
    _CfprApSwEthEstcPcMonTrafDir_Type()
)
cfprApSwEthEstcPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcMonTrafDir.setStatus("current")
_CfprApSwEthEstcPcName_Type = SnmpAdminString
_CfprApSwEthEstcPcName_Object = MibTableColumn
cfprApSwEthEstcPcName = _CfprApSwEthEstcPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 19),
    _CfprApSwEthEstcPcName_Type()
)
cfprApSwEthEstcPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcName.setStatus("current")
_CfprApSwEthEstcPcPeerDn_Type = SnmpAdminString
_CfprApSwEthEstcPcPeerDn_Object = MibTableColumn
cfprApSwEthEstcPcPeerDn = _CfprApSwEthEstcPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 20),
    _CfprApSwEthEstcPcPeerDn_Type()
)
cfprApSwEthEstcPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcPeerDn.setStatus("current")
_CfprApSwEthEstcPcPortId_Type = Gauge32
_CfprApSwEthEstcPcPortId_Object = MibTableColumn
cfprApSwEthEstcPcPortId = _CfprApSwEthEstcPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 21),
    _CfprApSwEthEstcPcPortId_Type()
)
cfprApSwEthEstcPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcPortId.setStatus("current")
_CfprApSwEthEstcPcPortMode_Type = CfprApFabricEthEstcPortMode
_CfprApSwEthEstcPcPortMode_Object = MibTableColumn
cfprApSwEthEstcPcPortMode = _CfprApSwEthEstcPcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 22),
    _CfprApSwEthEstcPcPortMode_Type()
)
cfprApSwEthEstcPcPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcPortMode.setStatus("current")
_CfprApSwEthEstcPcPriorityFlowCtrl_Type = CfprApFlowctrlPriorityPause
_CfprApSwEthEstcPcPriorityFlowCtrl_Object = MibTableColumn
cfprApSwEthEstcPcPriorityFlowCtrl = _CfprApSwEthEstcPcPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 23),
    _CfprApSwEthEstcPcPriorityFlowCtrl_Type()
)
cfprApSwEthEstcPcPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcPriorityFlowCtrl.setStatus("current")
_CfprApSwEthEstcPcProtocol_Type = CfprApFabricEthPcProtocol
_CfprApSwEthEstcPcProtocol_Object = MibTableColumn
cfprApSwEthEstcPcProtocol = _CfprApSwEthEstcPcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 24),
    _CfprApSwEthEstcPcProtocol_Type()
)
cfprApSwEthEstcPcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcProtocol.setStatus("current")
_CfprApSwEthEstcPcRecvFlowCtrl_Type = CfprApFlowctrlFlowControl
_CfprApSwEthEstcPcRecvFlowCtrl_Object = MibTableColumn
cfprApSwEthEstcPcRecvFlowCtrl = _CfprApSwEthEstcPcRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 25),
    _CfprApSwEthEstcPcRecvFlowCtrl_Type()
)
cfprApSwEthEstcPcRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcRecvFlowCtrl.setStatus("current")
_CfprApSwEthEstcPcSendFlowCtrl_Type = CfprApFlowctrlFlowControl
_CfprApSwEthEstcPcSendFlowCtrl_Object = MibTableColumn
cfprApSwEthEstcPcSendFlowCtrl = _CfprApSwEthEstcPcSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 26),
    _CfprApSwEthEstcPcSendFlowCtrl_Type()
)
cfprApSwEthEstcPcSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcSendFlowCtrl.setStatus("current")
_CfprApSwEthEstcPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthEstcPcSwitchId_Object = MibTableColumn
cfprApSwEthEstcPcSwitchId = _CfprApSwEthEstcPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 27),
    _CfprApSwEthEstcPcSwitchId_Type()
)
cfprApSwEthEstcPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcSwitchId.setStatus("current")
_CfprApSwEthEstcPcTransport_Type = CfprApSwEthEstcPcTransport
_CfprApSwEthEstcPcTransport_Object = MibTableColumn
cfprApSwEthEstcPcTransport = _CfprApSwEthEstcPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 28),
    _CfprApSwEthEstcPcTransport_Type()
)
cfprApSwEthEstcPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcTransport.setStatus("current")
_CfprApSwEthEstcPcType_Type = CfprApSwLanPcType
_CfprApSwEthEstcPcType_Object = MibTableColumn
cfprApSwEthEstcPcType = _CfprApSwEthEstcPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 29),
    _CfprApSwEthEstcPcType_Type()
)
cfprApSwEthEstcPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcType.setStatus("current")
_CfprApSwEthEstcPcUplinkFailAction_Type = CfprApNwctrlLinkFailAction
_CfprApSwEthEstcPcUplinkFailAction_Object = MibTableColumn
cfprApSwEthEstcPcUplinkFailAction = _CfprApSwEthEstcPcUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 12, 1, 30),
    _CfprApSwEthEstcPcUplinkFailAction_Type()
)
cfprApSwEthEstcPcUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthEstcPcUplinkFailAction.setStatus("current")
_CfprApSwEthLanBorderTable_Object = MibTable
cfprApSwEthLanBorderTable = _CfprApSwEthLanBorderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13)
)
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderTable.setStatus("current")
_CfprApSwEthLanBorderEntry_Object = MibTableRow
cfprApSwEthLanBorderEntry = _CfprApSwEthLanBorderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1)
)
cfprApSwEthLanBorderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthLanBorderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderEntry.setStatus("current")
_CfprApSwEthLanBorderInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthLanBorderInstanceId_Object = MibTableColumn
cfprApSwEthLanBorderInstanceId = _CfprApSwEthLanBorderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 1),
    _CfprApSwEthLanBorderInstanceId_Type()
)
cfprApSwEthLanBorderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderInstanceId.setStatus("current")
_CfprApSwEthLanBorderDn_Type = CfprApManagedObjectDn
_CfprApSwEthLanBorderDn_Object = MibTableColumn
cfprApSwEthLanBorderDn = _CfprApSwEthLanBorderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 2),
    _CfprApSwEthLanBorderDn_Type()
)
cfprApSwEthLanBorderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderDn.setStatus("current")
_CfprApSwEthLanBorderRn_Type = SnmpAdminString
_CfprApSwEthLanBorderRn_Object = MibTableColumn
cfprApSwEthLanBorderRn = _CfprApSwEthLanBorderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 3),
    _CfprApSwEthLanBorderRn_Type()
)
cfprApSwEthLanBorderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderRn.setStatus("current")
_CfprApSwEthLanBorderDeployFlag_Type = Integer32
_CfprApSwEthLanBorderDeployFlag_Object = MibTableColumn
cfprApSwEthLanBorderDeployFlag = _CfprApSwEthLanBorderDeployFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 4),
    _CfprApSwEthLanBorderDeployFlag_Type()
)
cfprApSwEthLanBorderDeployFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderDeployFlag.setStatus("current")
_CfprApSwEthLanBorderFsmDescr_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmDescr_Object = MibTableColumn
cfprApSwEthLanBorderFsmDescr = _CfprApSwEthLanBorderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 5),
    _CfprApSwEthLanBorderFsmDescr_Type()
)
cfprApSwEthLanBorderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmDescr.setStatus("current")
_CfprApSwEthLanBorderFsmFlags_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmFlags_Object = MibTableColumn
cfprApSwEthLanBorderFsmFlags = _CfprApSwEthLanBorderFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 6),
    _CfprApSwEthLanBorderFsmFlags_Type()
)
cfprApSwEthLanBorderFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmFlags.setStatus("current")
_CfprApSwEthLanBorderFsmPrev_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmPrev_Object = MibTableColumn
cfprApSwEthLanBorderFsmPrev = _CfprApSwEthLanBorderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 7),
    _CfprApSwEthLanBorderFsmPrev_Type()
)
cfprApSwEthLanBorderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmPrev.setStatus("current")
_CfprApSwEthLanBorderFsmProgr_Type = Gauge32
_CfprApSwEthLanBorderFsmProgr_Object = MibTableColumn
cfprApSwEthLanBorderFsmProgr = _CfprApSwEthLanBorderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 8),
    _CfprApSwEthLanBorderFsmProgr_Type()
)
cfprApSwEthLanBorderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmProgr.setStatus("current")
_CfprApSwEthLanBorderFsmRmtInvErrCode_Type = Gauge32
_CfprApSwEthLanBorderFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwEthLanBorderFsmRmtInvErrCode = _CfprApSwEthLanBorderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 9),
    _CfprApSwEthLanBorderFsmRmtInvErrCode_Type()
)
cfprApSwEthLanBorderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmRmtInvErrCode.setStatus("current")
_CfprApSwEthLanBorderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwEthLanBorderFsmRmtInvErrDescr = _CfprApSwEthLanBorderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 10),
    _CfprApSwEthLanBorderFsmRmtInvErrDescr_Type()
)
cfprApSwEthLanBorderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmRmtInvErrDescr.setStatus("current")
_CfprApSwEthLanBorderFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwEthLanBorderFsmRmtInvRslt_Object = MibTableColumn
cfprApSwEthLanBorderFsmRmtInvRslt = _CfprApSwEthLanBorderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 11),
    _CfprApSwEthLanBorderFsmRmtInvRslt_Type()
)
cfprApSwEthLanBorderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmRmtInvRslt.setStatus("current")
_CfprApSwEthLanBorderFsmStageDescr_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmStageDescr_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageDescr = _CfprApSwEthLanBorderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 12),
    _CfprApSwEthLanBorderFsmStageDescr_Type()
)
cfprApSwEthLanBorderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageDescr.setStatus("current")
_CfprApSwEthLanBorderFsmStamp_Type = DateAndTime
_CfprApSwEthLanBorderFsmStamp_Object = MibTableColumn
cfprApSwEthLanBorderFsmStamp = _CfprApSwEthLanBorderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 13),
    _CfprApSwEthLanBorderFsmStamp_Type()
)
cfprApSwEthLanBorderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStamp.setStatus("current")
_CfprApSwEthLanBorderFsmStatus_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmStatus_Object = MibTableColumn
cfprApSwEthLanBorderFsmStatus = _CfprApSwEthLanBorderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 14),
    _CfprApSwEthLanBorderFsmStatus_Type()
)
cfprApSwEthLanBorderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStatus.setStatus("current")
_CfprApSwEthLanBorderFsmTry_Type = Gauge32
_CfprApSwEthLanBorderFsmTry_Object = MibTableColumn
cfprApSwEthLanBorderFsmTry = _CfprApSwEthLanBorderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 15),
    _CfprApSwEthLanBorderFsmTry_Type()
)
cfprApSwEthLanBorderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTry.setStatus("current")
_CfprApSwEthLanBorderLocale_Type = CfprApSwBorderDomainLocale
_CfprApSwEthLanBorderLocale_Object = MibTableColumn
cfprApSwEthLanBorderLocale = _CfprApSwEthLanBorderLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 16),
    _CfprApSwEthLanBorderLocale_Type()
)
cfprApSwEthLanBorderLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderLocale.setStatus("current")
_CfprApSwEthLanBorderName_Type = SnmpAdminString
_CfprApSwEthLanBorderName_Object = MibTableColumn
cfprApSwEthLanBorderName = _CfprApSwEthLanBorderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 17),
    _CfprApSwEthLanBorderName_Type()
)
cfprApSwEthLanBorderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderName.setStatus("current")
_CfprApSwEthLanBorderSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthLanBorderSwitchId_Object = MibTableColumn
cfprApSwEthLanBorderSwitchId = _CfprApSwEthLanBorderSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 18),
    _CfprApSwEthLanBorderSwitchId_Type()
)
cfprApSwEthLanBorderSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderSwitchId.setStatus("current")
_CfprApSwEthLanBorderTransport_Type = CfprApSwEthLanBorderTransport
_CfprApSwEthLanBorderTransport_Object = MibTableColumn
cfprApSwEthLanBorderTransport = _CfprApSwEthLanBorderTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 19),
    _CfprApSwEthLanBorderTransport_Type()
)
cfprApSwEthLanBorderTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderTransport.setStatus("current")
_CfprApSwEthLanBorderType_Type = CfprApSwLanBorderType
_CfprApSwEthLanBorderType_Object = MibTableColumn
cfprApSwEthLanBorderType = _CfprApSwEthLanBorderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 20),
    _CfprApSwEthLanBorderType_Type()
)
cfprApSwEthLanBorderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderType.setStatus("current")
_CfprApSwEthLanBorderUdldMsgInterval_Type = Gauge32
_CfprApSwEthLanBorderUdldMsgInterval_Object = MibTableColumn
cfprApSwEthLanBorderUdldMsgInterval = _CfprApSwEthLanBorderUdldMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 21),
    _CfprApSwEthLanBorderUdldMsgInterval_Type()
)
cfprApSwEthLanBorderUdldMsgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderUdldMsgInterval.setStatus("current")
_CfprApSwEthLanBorderUdldRecoveryAction_Type = CfprApFabricRecoveryAction
_CfprApSwEthLanBorderUdldRecoveryAction_Object = MibTableColumn
cfprApSwEthLanBorderUdldRecoveryAction = _CfprApSwEthLanBorderUdldRecoveryAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 13, 1, 22),
    _CfprApSwEthLanBorderUdldRecoveryAction_Type()
)
cfprApSwEthLanBorderUdldRecoveryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderUdldRecoveryAction.setStatus("current")
_CfprApSwEthLanBorderFsmTable_Object = MibTable
cfprApSwEthLanBorderFsmTable = _CfprApSwEthLanBorderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14)
)
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTable.setStatus("current")
_CfprApSwEthLanBorderFsmEntry_Object = MibTableRow
cfprApSwEthLanBorderFsmEntry = _CfprApSwEthLanBorderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1)
)
cfprApSwEthLanBorderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthLanBorderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmEntry.setStatus("current")
_CfprApSwEthLanBorderFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthLanBorderFsmInstanceId_Object = MibTableColumn
cfprApSwEthLanBorderFsmInstanceId = _CfprApSwEthLanBorderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 1),
    _CfprApSwEthLanBorderFsmInstanceId_Type()
)
cfprApSwEthLanBorderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmInstanceId.setStatus("current")
_CfprApSwEthLanBorderFsmDn_Type = CfprApManagedObjectDn
_CfprApSwEthLanBorderFsmDn_Object = MibTableColumn
cfprApSwEthLanBorderFsmDn = _CfprApSwEthLanBorderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 2),
    _CfprApSwEthLanBorderFsmDn_Type()
)
cfprApSwEthLanBorderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmDn.setStatus("current")
_CfprApSwEthLanBorderFsmRn_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmRn_Object = MibTableColumn
cfprApSwEthLanBorderFsmRn = _CfprApSwEthLanBorderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 3),
    _CfprApSwEthLanBorderFsmRn_Type()
)
cfprApSwEthLanBorderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmRn.setStatus("current")
_CfprApSwEthLanBorderFsmCompletionTime_Type = DateAndTime
_CfprApSwEthLanBorderFsmCompletionTime_Object = MibTableColumn
cfprApSwEthLanBorderFsmCompletionTime = _CfprApSwEthLanBorderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 4),
    _CfprApSwEthLanBorderFsmCompletionTime_Type()
)
cfprApSwEthLanBorderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmCompletionTime.setStatus("current")
_CfprApSwEthLanBorderFsmCurrentFsm_Type = CfprApSwEthLanBorderFsmCurrentFsm
_CfprApSwEthLanBorderFsmCurrentFsm_Object = MibTableColumn
cfprApSwEthLanBorderFsmCurrentFsm = _CfprApSwEthLanBorderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 5),
    _CfprApSwEthLanBorderFsmCurrentFsm_Type()
)
cfprApSwEthLanBorderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmCurrentFsm.setStatus("current")
_CfprApSwEthLanBorderFsmDescrData_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmDescrData_Object = MibTableColumn
cfprApSwEthLanBorderFsmDescrData = _CfprApSwEthLanBorderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 6),
    _CfprApSwEthLanBorderFsmDescrData_Type()
)
cfprApSwEthLanBorderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmDescrData.setStatus("current")
_CfprApSwEthLanBorderFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwEthLanBorderFsmFsmStatus_Object = MibTableColumn
cfprApSwEthLanBorderFsmFsmStatus = _CfprApSwEthLanBorderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 7),
    _CfprApSwEthLanBorderFsmFsmStatus_Type()
)
cfprApSwEthLanBorderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmFsmStatus.setStatus("current")
_CfprApSwEthLanBorderFsmProgress_Type = Gauge32
_CfprApSwEthLanBorderFsmProgress_Object = MibTableColumn
cfprApSwEthLanBorderFsmProgress = _CfprApSwEthLanBorderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 8),
    _CfprApSwEthLanBorderFsmProgress_Type()
)
cfprApSwEthLanBorderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmProgress.setStatus("current")
_CfprApSwEthLanBorderFsmRmtErrCode_Type = Gauge32
_CfprApSwEthLanBorderFsmRmtErrCode_Object = MibTableColumn
cfprApSwEthLanBorderFsmRmtErrCode = _CfprApSwEthLanBorderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 9),
    _CfprApSwEthLanBorderFsmRmtErrCode_Type()
)
cfprApSwEthLanBorderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmRmtErrCode.setStatus("current")
_CfprApSwEthLanBorderFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmRmtErrDescr_Object = MibTableColumn
cfprApSwEthLanBorderFsmRmtErrDescr = _CfprApSwEthLanBorderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 10),
    _CfprApSwEthLanBorderFsmRmtErrDescr_Type()
)
cfprApSwEthLanBorderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmRmtErrDescr.setStatus("current")
_CfprApSwEthLanBorderFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwEthLanBorderFsmRmtRslt_Object = MibTableColumn
cfprApSwEthLanBorderFsmRmtRslt = _CfprApSwEthLanBorderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 14, 1, 11),
    _CfprApSwEthLanBorderFsmRmtRslt_Type()
)
cfprApSwEthLanBorderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmRmtRslt.setStatus("current")
_CfprApSwEthLanBorderFsmStageTable_Object = MibTable
cfprApSwEthLanBorderFsmStageTable = _CfprApSwEthLanBorderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15)
)
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageTable.setStatus("current")
_CfprApSwEthLanBorderFsmStageEntry_Object = MibTableRow
cfprApSwEthLanBorderFsmStageEntry = _CfprApSwEthLanBorderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1)
)
cfprApSwEthLanBorderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthLanBorderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageEntry.setStatus("current")
_CfprApSwEthLanBorderFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthLanBorderFsmStageInstanceId_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageInstanceId = _CfprApSwEthLanBorderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 1),
    _CfprApSwEthLanBorderFsmStageInstanceId_Type()
)
cfprApSwEthLanBorderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageInstanceId.setStatus("current")
_CfprApSwEthLanBorderFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwEthLanBorderFsmStageDn_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageDn = _CfprApSwEthLanBorderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 2),
    _CfprApSwEthLanBorderFsmStageDn_Type()
)
cfprApSwEthLanBorderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageDn.setStatus("current")
_CfprApSwEthLanBorderFsmStageRn_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmStageRn_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageRn = _CfprApSwEthLanBorderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 3),
    _CfprApSwEthLanBorderFsmStageRn_Type()
)
cfprApSwEthLanBorderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageRn.setStatus("current")
_CfprApSwEthLanBorderFsmStageDescrData_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmStageDescrData_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageDescrData = _CfprApSwEthLanBorderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 4),
    _CfprApSwEthLanBorderFsmStageDescrData_Type()
)
cfprApSwEthLanBorderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageDescrData.setStatus("current")
_CfprApSwEthLanBorderFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwEthLanBorderFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageLastUpdateTime = _CfprApSwEthLanBorderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 5),
    _CfprApSwEthLanBorderFsmStageLastUpdateTime_Type()
)
cfprApSwEthLanBorderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageLastUpdateTime.setStatus("current")
_CfprApSwEthLanBorderFsmStageName_Type = CfprApSwEthLanBorderFsmStageName
_CfprApSwEthLanBorderFsmStageName_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageName = _CfprApSwEthLanBorderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 6),
    _CfprApSwEthLanBorderFsmStageName_Type()
)
cfprApSwEthLanBorderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageName.setStatus("current")
_CfprApSwEthLanBorderFsmStageOrder_Type = Gauge32
_CfprApSwEthLanBorderFsmStageOrder_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageOrder = _CfprApSwEthLanBorderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 7),
    _CfprApSwEthLanBorderFsmStageOrder_Type()
)
cfprApSwEthLanBorderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageOrder.setStatus("current")
_CfprApSwEthLanBorderFsmStageRetry_Type = Gauge32
_CfprApSwEthLanBorderFsmStageRetry_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageRetry = _CfprApSwEthLanBorderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 8),
    _CfprApSwEthLanBorderFsmStageRetry_Type()
)
cfprApSwEthLanBorderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageRetry.setStatus("current")
_CfprApSwEthLanBorderFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwEthLanBorderFsmStageStageStatus_Object = MibTableColumn
cfprApSwEthLanBorderFsmStageStageStatus = _CfprApSwEthLanBorderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 15, 1, 9),
    _CfprApSwEthLanBorderFsmStageStageStatus_Type()
)
cfprApSwEthLanBorderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmStageStageStatus.setStatus("current")
_CfprApSwEthLanBorderFsmTaskTable_Object = MibTable
cfprApSwEthLanBorderFsmTaskTable = _CfprApSwEthLanBorderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16)
)
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskTable.setStatus("current")
_CfprApSwEthLanBorderFsmTaskEntry_Object = MibTableRow
cfprApSwEthLanBorderFsmTaskEntry = _CfprApSwEthLanBorderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16, 1)
)
cfprApSwEthLanBorderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthLanBorderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskEntry.setStatus("current")
_CfprApSwEthLanBorderFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthLanBorderFsmTaskInstanceId_Object = MibTableColumn
cfprApSwEthLanBorderFsmTaskInstanceId = _CfprApSwEthLanBorderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16, 1, 1),
    _CfprApSwEthLanBorderFsmTaskInstanceId_Type()
)
cfprApSwEthLanBorderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskInstanceId.setStatus("current")
_CfprApSwEthLanBorderFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwEthLanBorderFsmTaskDn_Object = MibTableColumn
cfprApSwEthLanBorderFsmTaskDn = _CfprApSwEthLanBorderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16, 1, 2),
    _CfprApSwEthLanBorderFsmTaskDn_Type()
)
cfprApSwEthLanBorderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskDn.setStatus("current")
_CfprApSwEthLanBorderFsmTaskRn_Type = SnmpAdminString
_CfprApSwEthLanBorderFsmTaskRn_Object = MibTableColumn
cfprApSwEthLanBorderFsmTaskRn = _CfprApSwEthLanBorderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16, 1, 3),
    _CfprApSwEthLanBorderFsmTaskRn_Type()
)
cfprApSwEthLanBorderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskRn.setStatus("current")
_CfprApSwEthLanBorderFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwEthLanBorderFsmTaskCompletion_Object = MibTableColumn
cfprApSwEthLanBorderFsmTaskCompletion = _CfprApSwEthLanBorderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16, 1, 4),
    _CfprApSwEthLanBorderFsmTaskCompletion_Type()
)
cfprApSwEthLanBorderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskCompletion.setStatus("current")
_CfprApSwEthLanBorderFsmTaskFlags_Type = CfprApSwEthLanBorderFsmTaskFlags
_CfprApSwEthLanBorderFsmTaskFlags_Object = MibTableColumn
cfprApSwEthLanBorderFsmTaskFlags = _CfprApSwEthLanBorderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16, 1, 5),
    _CfprApSwEthLanBorderFsmTaskFlags_Type()
)
cfprApSwEthLanBorderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskFlags.setStatus("current")
_CfprApSwEthLanBorderFsmTaskItem_Type = CfprApSwEthLanBorderFsmTaskItem
_CfprApSwEthLanBorderFsmTaskItem_Object = MibTableColumn
cfprApSwEthLanBorderFsmTaskItem = _CfprApSwEthLanBorderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16, 1, 6),
    _CfprApSwEthLanBorderFsmTaskItem_Type()
)
cfprApSwEthLanBorderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskItem.setStatus("current")
_CfprApSwEthLanBorderFsmTaskSeqId_Type = Gauge32
_CfprApSwEthLanBorderFsmTaskSeqId_Object = MibTableColumn
cfprApSwEthLanBorderFsmTaskSeqId = _CfprApSwEthLanBorderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 16, 1, 7),
    _CfprApSwEthLanBorderFsmTaskSeqId_Type()
)
cfprApSwEthLanBorderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanBorderFsmTaskSeqId.setStatus("current")
_CfprApSwEthLanEpTable_Object = MibTable
cfprApSwEthLanEpTable = _CfprApSwEthLanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17)
)
if mibBuilder.loadTexts:
    cfprApSwEthLanEpTable.setStatus("current")
_CfprApSwEthLanEpEntry_Object = MibTableRow
cfprApSwEthLanEpEntry = _CfprApSwEthLanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1)
)
cfprApSwEthLanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthLanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthLanEpEntry.setStatus("current")
_CfprApSwEthLanEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthLanEpInstanceId_Object = MibTableColumn
cfprApSwEthLanEpInstanceId = _CfprApSwEthLanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 1),
    _CfprApSwEthLanEpInstanceId_Type()
)
cfprApSwEthLanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpInstanceId.setStatus("current")
_CfprApSwEthLanEpDn_Type = CfprApManagedObjectDn
_CfprApSwEthLanEpDn_Object = MibTableColumn
cfprApSwEthLanEpDn = _CfprApSwEthLanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 2),
    _CfprApSwEthLanEpDn_Type()
)
cfprApSwEthLanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpDn.setStatus("current")
_CfprApSwEthLanEpRn_Type = SnmpAdminString
_CfprApSwEthLanEpRn_Object = MibTableColumn
cfprApSwEthLanEpRn = _CfprApSwEthLanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 3),
    _CfprApSwEthLanEpRn_Type()
)
cfprApSwEthLanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpRn.setStatus("current")
_CfprApSwEthLanEpAdminDuplex_Type = CfprApPortDuplex
_CfprApSwEthLanEpAdminDuplex_Object = MibTableColumn
cfprApSwEthLanEpAdminDuplex = _CfprApSwEthLanEpAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 4),
    _CfprApSwEthLanEpAdminDuplex_Type()
)
cfprApSwEthLanEpAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpAdminDuplex.setStatus("current")
_CfprApSwEthLanEpAdminSpeed_Type = CfprApPortEthSpeed
_CfprApSwEthLanEpAdminSpeed_Object = MibTableColumn
cfprApSwEthLanEpAdminSpeed = _CfprApSwEthLanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 5),
    _CfprApSwEthLanEpAdminSpeed_Type()
)
cfprApSwEthLanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpAdminSpeed.setStatus("current")
_CfprApSwEthLanEpAdminState_Type = CfprApFabricAdminState
_CfprApSwEthLanEpAdminState_Object = MibTableColumn
cfprApSwEthLanEpAdminState = _CfprApSwEthLanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 6),
    _CfprApSwEthLanEpAdminState_Type()
)
cfprApSwEthLanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpAdminState.setStatus("current")
_CfprApSwEthLanEpAggrPortId_Type = Gauge32
_CfprApSwEthLanEpAggrPortId_Object = MibTableColumn
cfprApSwEthLanEpAggrPortId = _CfprApSwEthLanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 7),
    _CfprApSwEthLanEpAggrPortId_Type()
)
cfprApSwEthLanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpAggrPortId.setStatus("current")
_CfprApSwEthLanEpAutoNeg_Type = TruthValue
_CfprApSwEthLanEpAutoNeg_Object = MibTableColumn
cfprApSwEthLanEpAutoNeg = _CfprApSwEthLanEpAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 8),
    _CfprApSwEthLanEpAutoNeg_Type()
)
cfprApSwEthLanEpAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpAutoNeg.setStatus("current")
_CfprApSwEthLanEpChassisId_Type = Gauge32
_CfprApSwEthLanEpChassisId_Object = MibTableColumn
cfprApSwEthLanEpChassisId = _CfprApSwEthLanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 9),
    _CfprApSwEthLanEpChassisId_Type()
)
cfprApSwEthLanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpChassisId.setStatus("current")
_CfprApSwEthLanEpDtagVlan_Type = Gauge32
_CfprApSwEthLanEpDtagVlan_Object = MibTableColumn
cfprApSwEthLanEpDtagVlan = _CfprApSwEthLanEpDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 10),
    _CfprApSwEthLanEpDtagVlan_Type()
)
cfprApSwEthLanEpDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpDtagVlan.setStatus("current")
_CfprApSwEthLanEpEpDn_Type = SnmpAdminString
_CfprApSwEthLanEpEpDn_Object = MibTableColumn
cfprApSwEthLanEpEpDn = _CfprApSwEthLanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 11),
    _CfprApSwEthLanEpEpDn_Type()
)
cfprApSwEthLanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpEpDn.setStatus("current")
_CfprApSwEthLanEpFabRole_Type = CfprApSwFabricRole
_CfprApSwEthLanEpFabRole_Object = MibTableColumn
cfprApSwEthLanEpFabRole = _CfprApSwEthLanEpFabRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 12),
    _CfprApSwEthLanEpFabRole_Type()
)
cfprApSwEthLanEpFabRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpFabRole.setStatus("current")
_CfprApSwEthLanEpIfRole_Type = CfprApSwLanEpIfRole
_CfprApSwEthLanEpIfRole_Object = MibTableColumn
cfprApSwEthLanEpIfRole = _CfprApSwEthLanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 14),
    _CfprApSwEthLanEpIfRole_Type()
)
cfprApSwEthLanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpIfRole.setStatus("current")
_CfprApSwEthLanEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwEthLanEpIfType_Object = MibTableColumn
cfprApSwEthLanEpIfType = _CfprApSwEthLanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 15),
    _CfprApSwEthLanEpIfType_Type()
)
cfprApSwEthLanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpIfType.setStatus("current")
_CfprApSwEthLanEpLc_Type = CfprApSwPIoEpLc
_CfprApSwEthLanEpLc_Object = MibTableColumn
cfprApSwEthLanEpLc = _CfprApSwEthLanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 16),
    _CfprApSwEthLanEpLc_Type()
)
cfprApSwEthLanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpLc.setStatus("current")
_CfprApSwEthLanEpLocale_Type = CfprApSwBorderEpLocale
_CfprApSwEthLanEpLocale_Object = MibTableColumn
cfprApSwEthLanEpLocale = _CfprApSwEthLanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 17),
    _CfprApSwEthLanEpLocale_Type()
)
cfprApSwEthLanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpLocale.setStatus("current")
_CfprApSwEthLanEpMtu_Type = Gauge32
_CfprApSwEthLanEpMtu_Object = MibTableColumn
cfprApSwEthLanEpMtu = _CfprApSwEthLanEpMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 18),
    _CfprApSwEthLanEpMtu_Type()
)
cfprApSwEthLanEpMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpMtu.setStatus("current")
_CfprApSwEthLanEpName_Type = SnmpAdminString
_CfprApSwEthLanEpName_Object = MibTableColumn
cfprApSwEthLanEpName = _CfprApSwEthLanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 19),
    _CfprApSwEthLanEpName_Type()
)
cfprApSwEthLanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpName.setStatus("current")
_CfprApSwEthLanEpPcId_Type = Gauge32
_CfprApSwEthLanEpPcId_Object = MibTableColumn
cfprApSwEthLanEpPcId = _CfprApSwEthLanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 20),
    _CfprApSwEthLanEpPcId_Type()
)
cfprApSwEthLanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpPcId.setStatus("current")
_CfprApSwEthLanEpPeerAggrPortId_Type = Gauge32
_CfprApSwEthLanEpPeerAggrPortId_Object = MibTableColumn
cfprApSwEthLanEpPeerAggrPortId = _CfprApSwEthLanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 21),
    _CfprApSwEthLanEpPeerAggrPortId_Type()
)
cfprApSwEthLanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpPeerAggrPortId.setStatus("current")
_CfprApSwEthLanEpPeerChassisId_Type = Gauge32
_CfprApSwEthLanEpPeerChassisId_Object = MibTableColumn
cfprApSwEthLanEpPeerChassisId = _CfprApSwEthLanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 22),
    _CfprApSwEthLanEpPeerChassisId_Type()
)
cfprApSwEthLanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpPeerChassisId.setStatus("current")
_CfprApSwEthLanEpPeerDn_Type = SnmpAdminString
_CfprApSwEthLanEpPeerDn_Object = MibTableColumn
cfprApSwEthLanEpPeerDn = _CfprApSwEthLanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 23),
    _CfprApSwEthLanEpPeerDn_Type()
)
cfprApSwEthLanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpPeerDn.setStatus("current")
_CfprApSwEthLanEpPeerPortId_Type = Gauge32
_CfprApSwEthLanEpPeerPortId_Object = MibTableColumn
cfprApSwEthLanEpPeerPortId = _CfprApSwEthLanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 24),
    _CfprApSwEthLanEpPeerPortId_Type()
)
cfprApSwEthLanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpPeerPortId.setStatus("current")
_CfprApSwEthLanEpPeerSlotId_Type = Gauge32
_CfprApSwEthLanEpPeerSlotId_Object = MibTableColumn
cfprApSwEthLanEpPeerSlotId = _CfprApSwEthLanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 25),
    _CfprApSwEthLanEpPeerSlotId_Type()
)
cfprApSwEthLanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpPeerSlotId.setStatus("current")
_CfprApSwEthLanEpPortId_Type = Gauge32
_CfprApSwEthLanEpPortId_Object = MibTableColumn
cfprApSwEthLanEpPortId = _CfprApSwEthLanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 26),
    _CfprApSwEthLanEpPortId_Type()
)
cfprApSwEthLanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpPortId.setStatus("current")
_CfprApSwEthLanEpPriorityFlowCtrl_Type = CfprApFlowctrlPriorityPause
_CfprApSwEthLanEpPriorityFlowCtrl_Object = MibTableColumn
cfprApSwEthLanEpPriorityFlowCtrl = _CfprApSwEthLanEpPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 27),
    _CfprApSwEthLanEpPriorityFlowCtrl_Type()
)
cfprApSwEthLanEpPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpPriorityFlowCtrl.setStatus("current")
_CfprApSwEthLanEpQosPrio_Type = CfprApFabricQosPrio
_CfprApSwEthLanEpQosPrio_Object = MibTableColumn
cfprApSwEthLanEpQosPrio = _CfprApSwEthLanEpQosPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 28),
    _CfprApSwEthLanEpQosPrio_Type()
)
cfprApSwEthLanEpQosPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpQosPrio.setStatus("current")
_CfprApSwEthLanEpRecvFlowCtrl_Type = CfprApFlowctrlFlowControl
_CfprApSwEthLanEpRecvFlowCtrl_Object = MibTableColumn
cfprApSwEthLanEpRecvFlowCtrl = _CfprApSwEthLanEpRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 29),
    _CfprApSwEthLanEpRecvFlowCtrl_Type()
)
cfprApSwEthLanEpRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpRecvFlowCtrl.setStatus("current")
_CfprApSwEthLanEpSendFlowCtrl_Type = CfprApFlowctrlFlowControl
_CfprApSwEthLanEpSendFlowCtrl_Object = MibTableColumn
cfprApSwEthLanEpSendFlowCtrl = _CfprApSwEthLanEpSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 30),
    _CfprApSwEthLanEpSendFlowCtrl_Type()
)
cfprApSwEthLanEpSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpSendFlowCtrl.setStatus("current")
_CfprApSwEthLanEpSlotId_Type = Gauge32
_CfprApSwEthLanEpSlotId_Object = MibTableColumn
cfprApSwEthLanEpSlotId = _CfprApSwEthLanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 31),
    _CfprApSwEthLanEpSlotId_Type()
)
cfprApSwEthLanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpSlotId.setStatus("current")
_CfprApSwEthLanEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthLanEpSwitchId_Object = MibTableColumn
cfprApSwEthLanEpSwitchId = _CfprApSwEthLanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 32),
    _CfprApSwEthLanEpSwitchId_Type()
)
cfprApSwEthLanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpSwitchId.setStatus("current")
_CfprApSwEthLanEpTransport_Type = CfprApSwEthLanEpTransport
_CfprApSwEthLanEpTransport_Object = MibTableColumn
cfprApSwEthLanEpTransport = _CfprApSwEthLanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 33),
    _CfprApSwEthLanEpTransport_Type()
)
cfprApSwEthLanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpTransport.setStatus("current")
_CfprApSwEthLanEpType_Type = CfprApSwLanEpType
_CfprApSwEthLanEpType_Object = MibTableColumn
cfprApSwEthLanEpType = _CfprApSwEthLanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 34),
    _CfprApSwEthLanEpType_Type()
)
cfprApSwEthLanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpType.setStatus("current")
_CfprApSwEthLanEpUdldAdminState_Type = CfprApSwEthLanEpUdldAdminState
_CfprApSwEthLanEpUdldAdminState_Object = MibTableColumn
cfprApSwEthLanEpUdldAdminState = _CfprApSwEthLanEpUdldAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 35),
    _CfprApSwEthLanEpUdldAdminState_Type()
)
cfprApSwEthLanEpUdldAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpUdldAdminState.setStatus("current")
_CfprApSwEthLanEpUdldMode_Type = CfprApSwEthLanEpUdldMode
_CfprApSwEthLanEpUdldMode_Object = MibTableColumn
cfprApSwEthLanEpUdldMode = _CfprApSwEthLanEpUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 17, 1, 36),
    _CfprApSwEthLanEpUdldMode_Type()
)
cfprApSwEthLanEpUdldMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanEpUdldMode.setStatus("current")
_CfprApSwEthLanMonTable_Object = MibTable
cfprApSwEthLanMonTable = _CfprApSwEthLanMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22)
)
if mibBuilder.loadTexts:
    cfprApSwEthLanMonTable.setStatus("current")
_CfprApSwEthLanMonEntry_Object = MibTableRow
cfprApSwEthLanMonEntry = _CfprApSwEthLanMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1)
)
cfprApSwEthLanMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthLanMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthLanMonEntry.setStatus("current")
_CfprApSwEthLanMonInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthLanMonInstanceId_Object = MibTableColumn
cfprApSwEthLanMonInstanceId = _CfprApSwEthLanMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1, 1),
    _CfprApSwEthLanMonInstanceId_Type()
)
cfprApSwEthLanMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthLanMonInstanceId.setStatus("current")
_CfprApSwEthLanMonDn_Type = CfprApManagedObjectDn
_CfprApSwEthLanMonDn_Object = MibTableColumn
cfprApSwEthLanMonDn = _CfprApSwEthLanMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1, 2),
    _CfprApSwEthLanMonDn_Type()
)
cfprApSwEthLanMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanMonDn.setStatus("current")
_CfprApSwEthLanMonRn_Type = SnmpAdminString
_CfprApSwEthLanMonRn_Object = MibTableColumn
cfprApSwEthLanMonRn = _CfprApSwEthLanMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1, 3),
    _CfprApSwEthLanMonRn_Type()
)
cfprApSwEthLanMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanMonRn.setStatus("current")
_CfprApSwEthLanMonLocale_Type = CfprApSwMonDomainLocale
_CfprApSwEthLanMonLocale_Object = MibTableColumn
cfprApSwEthLanMonLocale = _CfprApSwEthLanMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1, 4),
    _CfprApSwEthLanMonLocale_Type()
)
cfprApSwEthLanMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanMonLocale.setStatus("current")
_CfprApSwEthLanMonName_Type = SnmpAdminString
_CfprApSwEthLanMonName_Object = MibTableColumn
cfprApSwEthLanMonName = _CfprApSwEthLanMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1, 5),
    _CfprApSwEthLanMonName_Type()
)
cfprApSwEthLanMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanMonName.setStatus("current")
_CfprApSwEthLanMonSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthLanMonSwitchId_Object = MibTableColumn
cfprApSwEthLanMonSwitchId = _CfprApSwEthLanMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1, 6),
    _CfprApSwEthLanMonSwitchId_Type()
)
cfprApSwEthLanMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanMonSwitchId.setStatus("current")
_CfprApSwEthLanMonTransport_Type = CfprApSwEthLanMonTransport
_CfprApSwEthLanMonTransport_Object = MibTableColumn
cfprApSwEthLanMonTransport = _CfprApSwEthLanMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1, 7),
    _CfprApSwEthLanMonTransport_Type()
)
cfprApSwEthLanMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanMonTransport.setStatus("current")
_CfprApSwEthLanMonType_Type = CfprApSwLanMonType
_CfprApSwEthLanMonType_Object = MibTableColumn
cfprApSwEthLanMonType = _CfprApSwEthLanMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 22, 1, 8),
    _CfprApSwEthLanMonType_Type()
)
cfprApSwEthLanMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanMonType.setStatus("current")
_CfprApSwEthLanPcTable_Object = MibTable
cfprApSwEthLanPcTable = _CfprApSwEthLanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23)
)
if mibBuilder.loadTexts:
    cfprApSwEthLanPcTable.setStatus("current")
_CfprApSwEthLanPcEntry_Object = MibTableRow
cfprApSwEthLanPcEntry = _CfprApSwEthLanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1)
)
cfprApSwEthLanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthLanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthLanPcEntry.setStatus("current")
_CfprApSwEthLanPcInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthLanPcInstanceId_Object = MibTableColumn
cfprApSwEthLanPcInstanceId = _CfprApSwEthLanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 1),
    _CfprApSwEthLanPcInstanceId_Type()
)
cfprApSwEthLanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcInstanceId.setStatus("current")
_CfprApSwEthLanPcDn_Type = CfprApManagedObjectDn
_CfprApSwEthLanPcDn_Object = MibTableColumn
cfprApSwEthLanPcDn = _CfprApSwEthLanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 2),
    _CfprApSwEthLanPcDn_Type()
)
cfprApSwEthLanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcDn.setStatus("current")
_CfprApSwEthLanPcRn_Type = SnmpAdminString
_CfprApSwEthLanPcRn_Object = MibTableColumn
cfprApSwEthLanPcRn = _CfprApSwEthLanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 3),
    _CfprApSwEthLanPcRn_Type()
)
cfprApSwEthLanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcRn.setStatus("current")
_CfprApSwEthLanPcAdminDuplex_Type = CfprApPortDuplex
_CfprApSwEthLanPcAdminDuplex_Object = MibTableColumn
cfprApSwEthLanPcAdminDuplex = _CfprApSwEthLanPcAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 4),
    _CfprApSwEthLanPcAdminDuplex_Type()
)
cfprApSwEthLanPcAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcAdminDuplex.setStatus("current")
_CfprApSwEthLanPcAdminSpeed_Type = CfprApPortEthSpeed
_CfprApSwEthLanPcAdminSpeed_Object = MibTableColumn
cfprApSwEthLanPcAdminSpeed = _CfprApSwEthLanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 5),
    _CfprApSwEthLanPcAdminSpeed_Type()
)
cfprApSwEthLanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcAdminSpeed.setStatus("current")
_CfprApSwEthLanPcAdminState_Type = CfprApFabricAdminState
_CfprApSwEthLanPcAdminState_Object = MibTableColumn
cfprApSwEthLanPcAdminState = _CfprApSwEthLanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 6),
    _CfprApSwEthLanPcAdminState_Type()
)
cfprApSwEthLanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcAdminState.setStatus("current")
_CfprApSwEthLanPcAutoNeg_Type = TruthValue
_CfprApSwEthLanPcAutoNeg_Object = MibTableColumn
cfprApSwEthLanPcAutoNeg = _CfprApSwEthLanPcAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 7),
    _CfprApSwEthLanPcAutoNeg_Type()
)
cfprApSwEthLanPcAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcAutoNeg.setStatus("current")
_CfprApSwEthLanPcCluChassisId_Type = Gauge32
_CfprApSwEthLanPcCluChassisId_Object = MibTableColumn
cfprApSwEthLanPcCluChassisId = _CfprApSwEthLanPcCluChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 8),
    _CfprApSwEthLanPcCluChassisId_Type()
)
cfprApSwEthLanPcCluChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcCluChassisId.setStatus("current")
_CfprApSwEthLanPcClusterName_Type = SnmpAdminString
_CfprApSwEthLanPcClusterName_Object = MibTableColumn
cfprApSwEthLanPcClusterName = _CfprApSwEthLanPcClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 9),
    _CfprApSwEthLanPcClusterName_Type()
)
cfprApSwEthLanPcClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcClusterName.setStatus("current")
_CfprApSwEthLanPcDtagVlan_Type = Gauge32
_CfprApSwEthLanPcDtagVlan_Object = MibTableColumn
cfprApSwEthLanPcDtagVlan = _CfprApSwEthLanPcDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 10),
    _CfprApSwEthLanPcDtagVlan_Type()
)
cfprApSwEthLanPcDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcDtagVlan.setStatus("current")
_CfprApSwEthLanPcEpDn_Type = SnmpAdminString
_CfprApSwEthLanPcEpDn_Object = MibTableColumn
cfprApSwEthLanPcEpDn = _CfprApSwEthLanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 11),
    _CfprApSwEthLanPcEpDn_Type()
)
cfprApSwEthLanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcEpDn.setStatus("current")
_CfprApSwEthLanPcFabRole_Type = CfprApSwFabricRole
_CfprApSwEthLanPcFabRole_Object = MibTableColumn
cfprApSwEthLanPcFabRole = _CfprApSwEthLanPcFabRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 12),
    _CfprApSwEthLanPcFabRole_Type()
)
cfprApSwEthLanPcFabRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcFabRole.setStatus("current")
_CfprApSwEthLanPcIfRole_Type = CfprApSwLanPcIfRole
_CfprApSwEthLanPcIfRole_Object = MibTableColumn
cfprApSwEthLanPcIfRole = _CfprApSwEthLanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 14),
    _CfprApSwEthLanPcIfRole_Type()
)
cfprApSwEthLanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcIfRole.setStatus("current")
_CfprApSwEthLanPcIfType_Type = CfprApSwCIoEpIfType
_CfprApSwEthLanPcIfType_Object = MibTableColumn
cfprApSwEthLanPcIfType = _CfprApSwEthLanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 15),
    _CfprApSwEthLanPcIfType_Type()
)
cfprApSwEthLanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcIfType.setStatus("current")
_CfprApSwEthLanPcLacpDetach_Type = CfprApSwAdminState
_CfprApSwEthLanPcLacpDetach_Object = MibTableColumn
cfprApSwEthLanPcLacpDetach = _CfprApSwEthLanPcLacpDetach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 16),
    _CfprApSwEthLanPcLacpDetach_Type()
)
cfprApSwEthLanPcLacpDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcLacpDetach.setStatus("current")
_CfprApSwEthLanPcLacpFastTimer_Type = TruthValue
_CfprApSwEthLanPcLacpFastTimer_Object = MibTableColumn
cfprApSwEthLanPcLacpFastTimer = _CfprApSwEthLanPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 17),
    _CfprApSwEthLanPcLacpFastTimer_Type()
)
cfprApSwEthLanPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcLacpFastTimer.setStatus("current")
_CfprApSwEthLanPcLacpMode_Type = CfprApFabricLacpMode
_CfprApSwEthLanPcLacpMode_Object = MibTableColumn
cfprApSwEthLanPcLacpMode = _CfprApSwEthLanPcLacpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 18),
    _CfprApSwEthLanPcLacpMode_Type()
)
cfprApSwEthLanPcLacpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcLacpMode.setStatus("current")
_CfprApSwEthLanPcLacpSuspendIndividual_Type = TruthValue
_CfprApSwEthLanPcLacpSuspendIndividual_Object = MibTableColumn
cfprApSwEthLanPcLacpSuspendIndividual = _CfprApSwEthLanPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 19),
    _CfprApSwEthLanPcLacpSuspendIndividual_Type()
)
cfprApSwEthLanPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcLacpSuspendIndividual.setStatus("current")
_CfprApSwEthLanPcLocale_Type = CfprApSwBorderPcLocale
_CfprApSwEthLanPcLocale_Object = MibTableColumn
cfprApSwEthLanPcLocale = _CfprApSwEthLanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 20),
    _CfprApSwEthLanPcLocale_Type()
)
cfprApSwEthLanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcLocale.setStatus("current")
_CfprApSwEthLanPcMonTrafDir_Type = CfprApFabricTrafficDirection
_CfprApSwEthLanPcMonTrafDir_Object = MibTableColumn
cfprApSwEthLanPcMonTrafDir = _CfprApSwEthLanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 21),
    _CfprApSwEthLanPcMonTrafDir_Type()
)
cfprApSwEthLanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcMonTrafDir.setStatus("current")
_CfprApSwEthLanPcMtu_Type = Gauge32
_CfprApSwEthLanPcMtu_Object = MibTableColumn
cfprApSwEthLanPcMtu = _CfprApSwEthLanPcMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 22),
    _CfprApSwEthLanPcMtu_Type()
)
cfprApSwEthLanPcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcMtu.setStatus("current")
_CfprApSwEthLanPcName_Type = SnmpAdminString
_CfprApSwEthLanPcName_Object = MibTableColumn
cfprApSwEthLanPcName = _CfprApSwEthLanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 23),
    _CfprApSwEthLanPcName_Type()
)
cfprApSwEthLanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcName.setStatus("current")
_CfprApSwEthLanPcPeerDn_Type = SnmpAdminString
_CfprApSwEthLanPcPeerDn_Object = MibTableColumn
cfprApSwEthLanPcPeerDn = _CfprApSwEthLanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 24),
    _CfprApSwEthLanPcPeerDn_Type()
)
cfprApSwEthLanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcPeerDn.setStatus("current")
_CfprApSwEthLanPcPortId_Type = Gauge32
_CfprApSwEthLanPcPortId_Object = MibTableColumn
cfprApSwEthLanPcPortId = _CfprApSwEthLanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 25),
    _CfprApSwEthLanPcPortId_Type()
)
cfprApSwEthLanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcPortId.setStatus("current")
_CfprApSwEthLanPcPriorityFlowCtrl_Type = CfprApFlowctrlPriorityPause
_CfprApSwEthLanPcPriorityFlowCtrl_Object = MibTableColumn
cfprApSwEthLanPcPriorityFlowCtrl = _CfprApSwEthLanPcPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 26),
    _CfprApSwEthLanPcPriorityFlowCtrl_Type()
)
cfprApSwEthLanPcPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcPriorityFlowCtrl.setStatus("current")
_CfprApSwEthLanPcQosPrio_Type = CfprApFabricQosPrio
_CfprApSwEthLanPcQosPrio_Object = MibTableColumn
cfprApSwEthLanPcQosPrio = _CfprApSwEthLanPcQosPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 27),
    _CfprApSwEthLanPcQosPrio_Type()
)
cfprApSwEthLanPcQosPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcQosPrio.setStatus("current")
_CfprApSwEthLanPcRecvFlowCtrl_Type = CfprApFlowctrlFlowControl
_CfprApSwEthLanPcRecvFlowCtrl_Object = MibTableColumn
cfprApSwEthLanPcRecvFlowCtrl = _CfprApSwEthLanPcRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 28),
    _CfprApSwEthLanPcRecvFlowCtrl_Type()
)
cfprApSwEthLanPcRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcRecvFlowCtrl.setStatus("current")
_CfprApSwEthLanPcSendFlowCtrl_Type = CfprApFlowctrlFlowControl
_CfprApSwEthLanPcSendFlowCtrl_Object = MibTableColumn
cfprApSwEthLanPcSendFlowCtrl = _CfprApSwEthLanPcSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 29),
    _CfprApSwEthLanPcSendFlowCtrl_Type()
)
cfprApSwEthLanPcSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcSendFlowCtrl.setStatus("current")
_CfprApSwEthLanPcSpannedCluster_Type = CfprApFabricSpannedCluster
_CfprApSwEthLanPcSpannedCluster_Object = MibTableColumn
cfprApSwEthLanPcSpannedCluster = _CfprApSwEthLanPcSpannedCluster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 30),
    _CfprApSwEthLanPcSpannedCluster_Type()
)
cfprApSwEthLanPcSpannedCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcSpannedCluster.setStatus("current")
_CfprApSwEthLanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthLanPcSwitchId_Object = MibTableColumn
cfprApSwEthLanPcSwitchId = _CfprApSwEthLanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 31),
    _CfprApSwEthLanPcSwitchId_Type()
)
cfprApSwEthLanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcSwitchId.setStatus("current")
_CfprApSwEthLanPcTransport_Type = CfprApSwEthLanPcTransport
_CfprApSwEthLanPcTransport_Object = MibTableColumn
cfprApSwEthLanPcTransport = _CfprApSwEthLanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 32),
    _CfprApSwEthLanPcTransport_Type()
)
cfprApSwEthLanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcTransport.setStatus("current")
_CfprApSwEthLanPcType_Type = CfprApSwLanPcType
_CfprApSwEthLanPcType_Object = MibTableColumn
cfprApSwEthLanPcType = _CfprApSwEthLanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 23, 1, 33),
    _CfprApSwEthLanPcType_Type()
)
cfprApSwEthLanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthLanPcType.setStatus("current")
_CfprApSwEthMonTable_Object = MibTable
cfprApSwEthMonTable = _CfprApSwEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24)
)
if mibBuilder.loadTexts:
    cfprApSwEthMonTable.setStatus("current")
_CfprApSwEthMonEntry_Object = MibTableRow
cfprApSwEthMonEntry = _CfprApSwEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1)
)
cfprApSwEthMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthMonEntry.setStatus("current")
_CfprApSwEthMonInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthMonInstanceId_Object = MibTableColumn
cfprApSwEthMonInstanceId = _CfprApSwEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 1),
    _CfprApSwEthMonInstanceId_Type()
)
cfprApSwEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthMonInstanceId.setStatus("current")
_CfprApSwEthMonDn_Type = CfprApManagedObjectDn
_CfprApSwEthMonDn_Object = MibTableColumn
cfprApSwEthMonDn = _CfprApSwEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 2),
    _CfprApSwEthMonDn_Type()
)
cfprApSwEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDn.setStatus("current")
_CfprApSwEthMonRn_Type = SnmpAdminString
_CfprApSwEthMonRn_Object = MibTableColumn
cfprApSwEthMonRn = _CfprApSwEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 3),
    _CfprApSwEthMonRn_Type()
)
cfprApSwEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonRn.setStatus("current")
_CfprApSwEthMonAdminState_Type = CfprApSwMonAdminState
_CfprApSwEthMonAdminState_Object = MibTableColumn
cfprApSwEthMonAdminState = _CfprApSwEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 4),
    _CfprApSwEthMonAdminState_Type()
)
cfprApSwEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonAdminState.setStatus("current")
_CfprApSwEthMonFsmDescr_Type = SnmpAdminString
_CfprApSwEthMonFsmDescr_Object = MibTableColumn
cfprApSwEthMonFsmDescr = _CfprApSwEthMonFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 5),
    _CfprApSwEthMonFsmDescr_Type()
)
cfprApSwEthMonFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmDescr.setStatus("current")
_CfprApSwEthMonFsmPrev_Type = SnmpAdminString
_CfprApSwEthMonFsmPrev_Object = MibTableColumn
cfprApSwEthMonFsmPrev = _CfprApSwEthMonFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 6),
    _CfprApSwEthMonFsmPrev_Type()
)
cfprApSwEthMonFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmPrev.setStatus("current")
_CfprApSwEthMonFsmProgr_Type = Gauge32
_CfprApSwEthMonFsmProgr_Object = MibTableColumn
cfprApSwEthMonFsmProgr = _CfprApSwEthMonFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 7),
    _CfprApSwEthMonFsmProgr_Type()
)
cfprApSwEthMonFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmProgr.setStatus("current")
_CfprApSwEthMonFsmRmtInvErrCode_Type = Gauge32
_CfprApSwEthMonFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwEthMonFsmRmtInvErrCode = _CfprApSwEthMonFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 8),
    _CfprApSwEthMonFsmRmtInvErrCode_Type()
)
cfprApSwEthMonFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmRmtInvErrCode.setStatus("current")
_CfprApSwEthMonFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwEthMonFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwEthMonFsmRmtInvErrDescr = _CfprApSwEthMonFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 9),
    _CfprApSwEthMonFsmRmtInvErrDescr_Type()
)
cfprApSwEthMonFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmRmtInvErrDescr.setStatus("current")
_CfprApSwEthMonFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwEthMonFsmRmtInvRslt_Object = MibTableColumn
cfprApSwEthMonFsmRmtInvRslt = _CfprApSwEthMonFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 10),
    _CfprApSwEthMonFsmRmtInvRslt_Type()
)
cfprApSwEthMonFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmRmtInvRslt.setStatus("current")
_CfprApSwEthMonFsmStageDescr_Type = SnmpAdminString
_CfprApSwEthMonFsmStageDescr_Object = MibTableColumn
cfprApSwEthMonFsmStageDescr = _CfprApSwEthMonFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 11),
    _CfprApSwEthMonFsmStageDescr_Type()
)
cfprApSwEthMonFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageDescr.setStatus("current")
_CfprApSwEthMonFsmStamp_Type = DateAndTime
_CfprApSwEthMonFsmStamp_Object = MibTableColumn
cfprApSwEthMonFsmStamp = _CfprApSwEthMonFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 12),
    _CfprApSwEthMonFsmStamp_Type()
)
cfprApSwEthMonFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStamp.setStatus("current")
_CfprApSwEthMonFsmStatus_Type = SnmpAdminString
_CfprApSwEthMonFsmStatus_Object = MibTableColumn
cfprApSwEthMonFsmStatus = _CfprApSwEthMonFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 13),
    _CfprApSwEthMonFsmStatus_Type()
)
cfprApSwEthMonFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStatus.setStatus("current")
_CfprApSwEthMonFsmTry_Type = Gauge32
_CfprApSwEthMonFsmTry_Object = MibTableColumn
cfprApSwEthMonFsmTry = _CfprApSwEthMonFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 14),
    _CfprApSwEthMonFsmTry_Type()
)
cfprApSwEthMonFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTry.setStatus("current")
_CfprApSwEthMonHasLastDest_Type = TruthValue
_CfprApSwEthMonHasLastDest_Object = MibTableColumn
cfprApSwEthMonHasLastDest = _CfprApSwEthMonHasLastDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 15),
    _CfprApSwEthMonHasLastDest_Type()
)
cfprApSwEthMonHasLastDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonHasLastDest.setStatus("current")
_CfprApSwEthMonLifeCycle_Type = CfprApSwMonLifeCycle
_CfprApSwEthMonLifeCycle_Object = MibTableColumn
cfprApSwEthMonLifeCycle = _CfprApSwEthMonLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 16),
    _CfprApSwEthMonLifeCycle_Type()
)
cfprApSwEthMonLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonLifeCycle.setStatus("current")
_CfprApSwEthMonName_Type = SnmpAdminString
_CfprApSwEthMonName_Object = MibTableColumn
cfprApSwEthMonName = _CfprApSwEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 17),
    _CfprApSwEthMonName_Type()
)
cfprApSwEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonName.setStatus("current")
_CfprApSwEthMonPeerDn_Type = SnmpAdminString
_CfprApSwEthMonPeerDn_Object = MibTableColumn
cfprApSwEthMonPeerDn = _CfprApSwEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 18),
    _CfprApSwEthMonPeerDn_Type()
)
cfprApSwEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonPeerDn.setStatus("current")
_CfprApSwEthMonSession_Type = Gauge32
_CfprApSwEthMonSession_Object = MibTableColumn
cfprApSwEthMonSession = _CfprApSwEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 19),
    _CfprApSwEthMonSession_Type()
)
cfprApSwEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSession.setStatus("current")
_CfprApSwEthMonSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthMonSwitchId_Object = MibTableColumn
cfprApSwEthMonSwitchId = _CfprApSwEthMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 20),
    _CfprApSwEthMonSwitchId_Type()
)
cfprApSwEthMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSwitchId.setStatus("current")
_CfprApSwEthMonTransport_Type = CfprApSwEthMonTransport
_CfprApSwEthMonTransport_Object = MibTableColumn
cfprApSwEthMonTransport = _CfprApSwEthMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 21),
    _CfprApSwEthMonTransport_Type()
)
cfprApSwEthMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonTransport.setStatus("current")
_CfprApSwEthMonType_Type = CfprApSwEthMonType
_CfprApSwEthMonType_Object = MibTableColumn
cfprApSwEthMonType = _CfprApSwEthMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 24, 1, 22),
    _CfprApSwEthMonType_Type()
)
cfprApSwEthMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonType.setStatus("current")
_CfprApSwEthMonDestEpTable_Object = MibTable
cfprApSwEthMonDestEpTable = _CfprApSwEthMonDestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25)
)
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpTable.setStatus("current")
_CfprApSwEthMonDestEpEntry_Object = MibTableRow
cfprApSwEthMonDestEpEntry = _CfprApSwEthMonDestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1)
)
cfprApSwEthMonDestEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthMonDestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpEntry.setStatus("current")
_CfprApSwEthMonDestEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthMonDestEpInstanceId_Object = MibTableColumn
cfprApSwEthMonDestEpInstanceId = _CfprApSwEthMonDestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 1),
    _CfprApSwEthMonDestEpInstanceId_Type()
)
cfprApSwEthMonDestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpInstanceId.setStatus("current")
_CfprApSwEthMonDestEpDn_Type = CfprApManagedObjectDn
_CfprApSwEthMonDestEpDn_Object = MibTableColumn
cfprApSwEthMonDestEpDn = _CfprApSwEthMonDestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 2),
    _CfprApSwEthMonDestEpDn_Type()
)
cfprApSwEthMonDestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpDn.setStatus("current")
_CfprApSwEthMonDestEpRn_Type = SnmpAdminString
_CfprApSwEthMonDestEpRn_Object = MibTableColumn
cfprApSwEthMonDestEpRn = _CfprApSwEthMonDestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 3),
    _CfprApSwEthMonDestEpRn_Type()
)
cfprApSwEthMonDestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpRn.setStatus("current")
_CfprApSwEthMonDestEpAdminSpeed_Type = CfprApPortEthSpeed
_CfprApSwEthMonDestEpAdminSpeed_Object = MibTableColumn
cfprApSwEthMonDestEpAdminSpeed = _CfprApSwEthMonDestEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 4),
    _CfprApSwEthMonDestEpAdminSpeed_Type()
)
cfprApSwEthMonDestEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpAdminSpeed.setStatus("current")
_CfprApSwEthMonDestEpAdminState_Type = CfprApFabricAdminState
_CfprApSwEthMonDestEpAdminState_Object = MibTableColumn
cfprApSwEthMonDestEpAdminState = _CfprApSwEthMonDestEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 5),
    _CfprApSwEthMonDestEpAdminState_Type()
)
cfprApSwEthMonDestEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpAdminState.setStatus("current")
_CfprApSwEthMonDestEpAggrPortId_Type = Gauge32
_CfprApSwEthMonDestEpAggrPortId_Object = MibTableColumn
cfprApSwEthMonDestEpAggrPortId = _CfprApSwEthMonDestEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 6),
    _CfprApSwEthMonDestEpAggrPortId_Type()
)
cfprApSwEthMonDestEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpAggrPortId.setStatus("current")
_CfprApSwEthMonDestEpChassisId_Type = Gauge32
_CfprApSwEthMonDestEpChassisId_Object = MibTableColumn
cfprApSwEthMonDestEpChassisId = _CfprApSwEthMonDestEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 7),
    _CfprApSwEthMonDestEpChassisId_Type()
)
cfprApSwEthMonDestEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpChassisId.setStatus("current")
_CfprApSwEthMonDestEpEpDn_Type = SnmpAdminString
_CfprApSwEthMonDestEpEpDn_Object = MibTableColumn
cfprApSwEthMonDestEpEpDn = _CfprApSwEthMonDestEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 8),
    _CfprApSwEthMonDestEpEpDn_Type()
)
cfprApSwEthMonDestEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpEpDn.setStatus("current")
_CfprApSwEthMonDestEpIfRole_Type = CfprApNetworkPortRole
_CfprApSwEthMonDestEpIfRole_Object = MibTableColumn
cfprApSwEthMonDestEpIfRole = _CfprApSwEthMonDestEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 9),
    _CfprApSwEthMonDestEpIfRole_Type()
)
cfprApSwEthMonDestEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpIfRole.setStatus("current")
_CfprApSwEthMonDestEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwEthMonDestEpIfType_Object = MibTableColumn
cfprApSwEthMonDestEpIfType = _CfprApSwEthMonDestEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 10),
    _CfprApSwEthMonDestEpIfType_Type()
)
cfprApSwEthMonDestEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpIfType.setStatus("current")
_CfprApSwEthMonDestEpLc_Type = CfprApSwPIoEpLc
_CfprApSwEthMonDestEpLc_Object = MibTableColumn
cfprApSwEthMonDestEpLc = _CfprApSwEthMonDestEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 11),
    _CfprApSwEthMonDestEpLc_Type()
)
cfprApSwEthMonDestEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpLc.setStatus("current")
_CfprApSwEthMonDestEpLocale_Type = CfprApNetworkLocale
_CfprApSwEthMonDestEpLocale_Object = MibTableColumn
cfprApSwEthMonDestEpLocale = _CfprApSwEthMonDestEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 12),
    _CfprApSwEthMonDestEpLocale_Type()
)
cfprApSwEthMonDestEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpLocale.setStatus("current")
_CfprApSwEthMonDestEpName_Type = SnmpAdminString
_CfprApSwEthMonDestEpName_Object = MibTableColumn
cfprApSwEthMonDestEpName = _CfprApSwEthMonDestEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 13),
    _CfprApSwEthMonDestEpName_Type()
)
cfprApSwEthMonDestEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpName.setStatus("current")
_CfprApSwEthMonDestEpPeerAggrPortId_Type = Gauge32
_CfprApSwEthMonDestEpPeerAggrPortId_Object = MibTableColumn
cfprApSwEthMonDestEpPeerAggrPortId = _CfprApSwEthMonDestEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 14),
    _CfprApSwEthMonDestEpPeerAggrPortId_Type()
)
cfprApSwEthMonDestEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpPeerAggrPortId.setStatus("current")
_CfprApSwEthMonDestEpPeerChassisId_Type = Gauge32
_CfprApSwEthMonDestEpPeerChassisId_Object = MibTableColumn
cfprApSwEthMonDestEpPeerChassisId = _CfprApSwEthMonDestEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 15),
    _CfprApSwEthMonDestEpPeerChassisId_Type()
)
cfprApSwEthMonDestEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpPeerChassisId.setStatus("current")
_CfprApSwEthMonDestEpPeerDn_Type = SnmpAdminString
_CfprApSwEthMonDestEpPeerDn_Object = MibTableColumn
cfprApSwEthMonDestEpPeerDn = _CfprApSwEthMonDestEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 16),
    _CfprApSwEthMonDestEpPeerDn_Type()
)
cfprApSwEthMonDestEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpPeerDn.setStatus("current")
_CfprApSwEthMonDestEpPeerPortId_Type = Gauge32
_CfprApSwEthMonDestEpPeerPortId_Object = MibTableColumn
cfprApSwEthMonDestEpPeerPortId = _CfprApSwEthMonDestEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 17),
    _CfprApSwEthMonDestEpPeerPortId_Type()
)
cfprApSwEthMonDestEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpPeerPortId.setStatus("current")
_CfprApSwEthMonDestEpPeerSlotId_Type = Gauge32
_CfprApSwEthMonDestEpPeerSlotId_Object = MibTableColumn
cfprApSwEthMonDestEpPeerSlotId = _CfprApSwEthMonDestEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 18),
    _CfprApSwEthMonDestEpPeerSlotId_Type()
)
cfprApSwEthMonDestEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpPeerSlotId.setStatus("current")
_CfprApSwEthMonDestEpPortId_Type = Gauge32
_CfprApSwEthMonDestEpPortId_Object = MibTableColumn
cfprApSwEthMonDestEpPortId = _CfprApSwEthMonDestEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 19),
    _CfprApSwEthMonDestEpPortId_Type()
)
cfprApSwEthMonDestEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpPortId.setStatus("current")
_CfprApSwEthMonDestEpSlotId_Type = Gauge32
_CfprApSwEthMonDestEpSlotId_Object = MibTableColumn
cfprApSwEthMonDestEpSlotId = _CfprApSwEthMonDestEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 20),
    _CfprApSwEthMonDestEpSlotId_Type()
)
cfprApSwEthMonDestEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpSlotId.setStatus("current")
_CfprApSwEthMonDestEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthMonDestEpSwitchId_Object = MibTableColumn
cfprApSwEthMonDestEpSwitchId = _CfprApSwEthMonDestEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 21),
    _CfprApSwEthMonDestEpSwitchId_Type()
)
cfprApSwEthMonDestEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpSwitchId.setStatus("current")
_CfprApSwEthMonDestEpTransport_Type = CfprApSwEthMonDestEpTransport
_CfprApSwEthMonDestEpTransport_Object = MibTableColumn
cfprApSwEthMonDestEpTransport = _CfprApSwEthMonDestEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 22),
    _CfprApSwEthMonDestEpTransport_Type()
)
cfprApSwEthMonDestEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpTransport.setStatus("current")
_CfprApSwEthMonDestEpType_Type = CfprApNetworkConnectionType
_CfprApSwEthMonDestEpType_Object = MibTableColumn
cfprApSwEthMonDestEpType = _CfprApSwEthMonDestEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 25, 1, 23),
    _CfprApSwEthMonDestEpType_Type()
)
cfprApSwEthMonDestEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonDestEpType.setStatus("current")
_CfprApSwEthMonFsmTable_Object = MibTable
cfprApSwEthMonFsmTable = _CfprApSwEthMonFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26)
)
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTable.setStatus("current")
_CfprApSwEthMonFsmEntry_Object = MibTableRow
cfprApSwEthMonFsmEntry = _CfprApSwEthMonFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1)
)
cfprApSwEthMonFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthMonFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmEntry.setStatus("current")
_CfprApSwEthMonFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthMonFsmInstanceId_Object = MibTableColumn
cfprApSwEthMonFsmInstanceId = _CfprApSwEthMonFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 1),
    _CfprApSwEthMonFsmInstanceId_Type()
)
cfprApSwEthMonFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmInstanceId.setStatus("current")
_CfprApSwEthMonFsmDn_Type = CfprApManagedObjectDn
_CfprApSwEthMonFsmDn_Object = MibTableColumn
cfprApSwEthMonFsmDn = _CfprApSwEthMonFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 2),
    _CfprApSwEthMonFsmDn_Type()
)
cfprApSwEthMonFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmDn.setStatus("current")
_CfprApSwEthMonFsmRn_Type = SnmpAdminString
_CfprApSwEthMonFsmRn_Object = MibTableColumn
cfprApSwEthMonFsmRn = _CfprApSwEthMonFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 3),
    _CfprApSwEthMonFsmRn_Type()
)
cfprApSwEthMonFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmRn.setStatus("current")
_CfprApSwEthMonFsmCompletionTime_Type = DateAndTime
_CfprApSwEthMonFsmCompletionTime_Object = MibTableColumn
cfprApSwEthMonFsmCompletionTime = _CfprApSwEthMonFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 4),
    _CfprApSwEthMonFsmCompletionTime_Type()
)
cfprApSwEthMonFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmCompletionTime.setStatus("current")
_CfprApSwEthMonFsmCurrentFsm_Type = CfprApSwEthMonFsmCurrentFsm
_CfprApSwEthMonFsmCurrentFsm_Object = MibTableColumn
cfprApSwEthMonFsmCurrentFsm = _CfprApSwEthMonFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 5),
    _CfprApSwEthMonFsmCurrentFsm_Type()
)
cfprApSwEthMonFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmCurrentFsm.setStatus("current")
_CfprApSwEthMonFsmDescrData_Type = SnmpAdminString
_CfprApSwEthMonFsmDescrData_Object = MibTableColumn
cfprApSwEthMonFsmDescrData = _CfprApSwEthMonFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 6),
    _CfprApSwEthMonFsmDescrData_Type()
)
cfprApSwEthMonFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmDescrData.setStatus("current")
_CfprApSwEthMonFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwEthMonFsmFsmStatus_Object = MibTableColumn
cfprApSwEthMonFsmFsmStatus = _CfprApSwEthMonFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 7),
    _CfprApSwEthMonFsmFsmStatus_Type()
)
cfprApSwEthMonFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmFsmStatus.setStatus("current")
_CfprApSwEthMonFsmProgress_Type = Gauge32
_CfprApSwEthMonFsmProgress_Object = MibTableColumn
cfprApSwEthMonFsmProgress = _CfprApSwEthMonFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 8),
    _CfprApSwEthMonFsmProgress_Type()
)
cfprApSwEthMonFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmProgress.setStatus("current")
_CfprApSwEthMonFsmRmtErrCode_Type = Gauge32
_CfprApSwEthMonFsmRmtErrCode_Object = MibTableColumn
cfprApSwEthMonFsmRmtErrCode = _CfprApSwEthMonFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 9),
    _CfprApSwEthMonFsmRmtErrCode_Type()
)
cfprApSwEthMonFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmRmtErrCode.setStatus("current")
_CfprApSwEthMonFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwEthMonFsmRmtErrDescr_Object = MibTableColumn
cfprApSwEthMonFsmRmtErrDescr = _CfprApSwEthMonFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 10),
    _CfprApSwEthMonFsmRmtErrDescr_Type()
)
cfprApSwEthMonFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmRmtErrDescr.setStatus("current")
_CfprApSwEthMonFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwEthMonFsmRmtRslt_Object = MibTableColumn
cfprApSwEthMonFsmRmtRslt = _CfprApSwEthMonFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 26, 1, 11),
    _CfprApSwEthMonFsmRmtRslt_Type()
)
cfprApSwEthMonFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmRmtRslt.setStatus("current")
_CfprApSwEthMonFsmStageTable_Object = MibTable
cfprApSwEthMonFsmStageTable = _CfprApSwEthMonFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27)
)
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageTable.setStatus("current")
_CfprApSwEthMonFsmStageEntry_Object = MibTableRow
cfprApSwEthMonFsmStageEntry = _CfprApSwEthMonFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1)
)
cfprApSwEthMonFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthMonFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageEntry.setStatus("current")
_CfprApSwEthMonFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthMonFsmStageInstanceId_Object = MibTableColumn
cfprApSwEthMonFsmStageInstanceId = _CfprApSwEthMonFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 1),
    _CfprApSwEthMonFsmStageInstanceId_Type()
)
cfprApSwEthMonFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageInstanceId.setStatus("current")
_CfprApSwEthMonFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwEthMonFsmStageDn_Object = MibTableColumn
cfprApSwEthMonFsmStageDn = _CfprApSwEthMonFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 2),
    _CfprApSwEthMonFsmStageDn_Type()
)
cfprApSwEthMonFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageDn.setStatus("current")
_CfprApSwEthMonFsmStageRn_Type = SnmpAdminString
_CfprApSwEthMonFsmStageRn_Object = MibTableColumn
cfprApSwEthMonFsmStageRn = _CfprApSwEthMonFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 3),
    _CfprApSwEthMonFsmStageRn_Type()
)
cfprApSwEthMonFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageRn.setStatus("current")
_CfprApSwEthMonFsmStageDescrData_Type = SnmpAdminString
_CfprApSwEthMonFsmStageDescrData_Object = MibTableColumn
cfprApSwEthMonFsmStageDescrData = _CfprApSwEthMonFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 4),
    _CfprApSwEthMonFsmStageDescrData_Type()
)
cfprApSwEthMonFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageDescrData.setStatus("current")
_CfprApSwEthMonFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwEthMonFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwEthMonFsmStageLastUpdateTime = _CfprApSwEthMonFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 5),
    _CfprApSwEthMonFsmStageLastUpdateTime_Type()
)
cfprApSwEthMonFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageLastUpdateTime.setStatus("current")
_CfprApSwEthMonFsmStageName_Type = CfprApSwEthMonFsmStageName
_CfprApSwEthMonFsmStageName_Object = MibTableColumn
cfprApSwEthMonFsmStageName = _CfprApSwEthMonFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 6),
    _CfprApSwEthMonFsmStageName_Type()
)
cfprApSwEthMonFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageName.setStatus("current")
_CfprApSwEthMonFsmStageOrder_Type = Gauge32
_CfprApSwEthMonFsmStageOrder_Object = MibTableColumn
cfprApSwEthMonFsmStageOrder = _CfprApSwEthMonFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 7),
    _CfprApSwEthMonFsmStageOrder_Type()
)
cfprApSwEthMonFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageOrder.setStatus("current")
_CfprApSwEthMonFsmStageRetry_Type = Gauge32
_CfprApSwEthMonFsmStageRetry_Object = MibTableColumn
cfprApSwEthMonFsmStageRetry = _CfprApSwEthMonFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 8),
    _CfprApSwEthMonFsmStageRetry_Type()
)
cfprApSwEthMonFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageRetry.setStatus("current")
_CfprApSwEthMonFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwEthMonFsmStageStageStatus_Object = MibTableColumn
cfprApSwEthMonFsmStageStageStatus = _CfprApSwEthMonFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 27, 1, 9),
    _CfprApSwEthMonFsmStageStageStatus_Type()
)
cfprApSwEthMonFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmStageStageStatus.setStatus("current")
_CfprApSwEthMonFsmTaskTable_Object = MibTable
cfprApSwEthMonFsmTaskTable = _CfprApSwEthMonFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28)
)
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskTable.setStatus("current")
_CfprApSwEthMonFsmTaskEntry_Object = MibTableRow
cfprApSwEthMonFsmTaskEntry = _CfprApSwEthMonFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28, 1)
)
cfprApSwEthMonFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthMonFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskEntry.setStatus("current")
_CfprApSwEthMonFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthMonFsmTaskInstanceId_Object = MibTableColumn
cfprApSwEthMonFsmTaskInstanceId = _CfprApSwEthMonFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28, 1, 1),
    _CfprApSwEthMonFsmTaskInstanceId_Type()
)
cfprApSwEthMonFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskInstanceId.setStatus("current")
_CfprApSwEthMonFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwEthMonFsmTaskDn_Object = MibTableColumn
cfprApSwEthMonFsmTaskDn = _CfprApSwEthMonFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28, 1, 2),
    _CfprApSwEthMonFsmTaskDn_Type()
)
cfprApSwEthMonFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskDn.setStatus("current")
_CfprApSwEthMonFsmTaskRn_Type = SnmpAdminString
_CfprApSwEthMonFsmTaskRn_Object = MibTableColumn
cfprApSwEthMonFsmTaskRn = _CfprApSwEthMonFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28, 1, 3),
    _CfprApSwEthMonFsmTaskRn_Type()
)
cfprApSwEthMonFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskRn.setStatus("current")
_CfprApSwEthMonFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwEthMonFsmTaskCompletion_Object = MibTableColumn
cfprApSwEthMonFsmTaskCompletion = _CfprApSwEthMonFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28, 1, 4),
    _CfprApSwEthMonFsmTaskCompletion_Type()
)
cfprApSwEthMonFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskCompletion.setStatus("current")
_CfprApSwEthMonFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSwEthMonFsmTaskFlags_Object = MibTableColumn
cfprApSwEthMonFsmTaskFlags = _CfprApSwEthMonFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28, 1, 5),
    _CfprApSwEthMonFsmTaskFlags_Type()
)
cfprApSwEthMonFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskFlags.setStatus("current")
_CfprApSwEthMonFsmTaskItem_Type = CfprApSwEthMonFsmTaskItem
_CfprApSwEthMonFsmTaskItem_Object = MibTableColumn
cfprApSwEthMonFsmTaskItem = _CfprApSwEthMonFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28, 1, 6),
    _CfprApSwEthMonFsmTaskItem_Type()
)
cfprApSwEthMonFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskItem.setStatus("current")
_CfprApSwEthMonFsmTaskSeqId_Type = Gauge32
_CfprApSwEthMonFsmTaskSeqId_Object = MibTableColumn
cfprApSwEthMonFsmTaskSeqId = _CfprApSwEthMonFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 28, 1, 7),
    _CfprApSwEthMonFsmTaskSeqId_Type()
)
cfprApSwEthMonFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonFsmTaskSeqId.setStatus("current")
_CfprApSwEthMonSrcEpTable_Object = MibTable
cfprApSwEthMonSrcEpTable = _CfprApSwEthMonSrcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29)
)
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpTable.setStatus("current")
_CfprApSwEthMonSrcEpEntry_Object = MibTableRow
cfprApSwEthMonSrcEpEntry = _CfprApSwEthMonSrcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1)
)
cfprApSwEthMonSrcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthMonSrcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpEntry.setStatus("current")
_CfprApSwEthMonSrcEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthMonSrcEpInstanceId_Object = MibTableColumn
cfprApSwEthMonSrcEpInstanceId = _CfprApSwEthMonSrcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 1),
    _CfprApSwEthMonSrcEpInstanceId_Type()
)
cfprApSwEthMonSrcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpInstanceId.setStatus("current")
_CfprApSwEthMonSrcEpDn_Type = CfprApManagedObjectDn
_CfprApSwEthMonSrcEpDn_Object = MibTableColumn
cfprApSwEthMonSrcEpDn = _CfprApSwEthMonSrcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 2),
    _CfprApSwEthMonSrcEpDn_Type()
)
cfprApSwEthMonSrcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpDn.setStatus("current")
_CfprApSwEthMonSrcEpRn_Type = SnmpAdminString
_CfprApSwEthMonSrcEpRn_Object = MibTableColumn
cfprApSwEthMonSrcEpRn = _CfprApSwEthMonSrcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 3),
    _CfprApSwEthMonSrcEpRn_Type()
)
cfprApSwEthMonSrcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpRn.setStatus("current")
_CfprApSwEthMonSrcEpAdminState_Type = CfprApFabricAdminState
_CfprApSwEthMonSrcEpAdminState_Object = MibTableColumn
cfprApSwEthMonSrcEpAdminState = _CfprApSwEthMonSrcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 4),
    _CfprApSwEthMonSrcEpAdminState_Type()
)
cfprApSwEthMonSrcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpAdminState.setStatus("current")
_CfprApSwEthMonSrcEpAggrPortId_Type = Gauge32
_CfprApSwEthMonSrcEpAggrPortId_Object = MibTableColumn
cfprApSwEthMonSrcEpAggrPortId = _CfprApSwEthMonSrcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 5),
    _CfprApSwEthMonSrcEpAggrPortId_Type()
)
cfprApSwEthMonSrcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpAggrPortId.setStatus("current")
_CfprApSwEthMonSrcEpChassisId_Type = Gauge32
_CfprApSwEthMonSrcEpChassisId_Object = MibTableColumn
cfprApSwEthMonSrcEpChassisId = _CfprApSwEthMonSrcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 6),
    _CfprApSwEthMonSrcEpChassisId_Type()
)
cfprApSwEthMonSrcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpChassisId.setStatus("current")
_CfprApSwEthMonSrcEpEpDn_Type = SnmpAdminString
_CfprApSwEthMonSrcEpEpDn_Object = MibTableColumn
cfprApSwEthMonSrcEpEpDn = _CfprApSwEthMonSrcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 7),
    _CfprApSwEthMonSrcEpEpDn_Type()
)
cfprApSwEthMonSrcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpEpDn.setStatus("current")
_CfprApSwEthMonSrcEpIfRole_Type = CfprApNetworkPortRole
_CfprApSwEthMonSrcEpIfRole_Object = MibTableColumn
cfprApSwEthMonSrcEpIfRole = _CfprApSwEthMonSrcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 8),
    _CfprApSwEthMonSrcEpIfRole_Type()
)
cfprApSwEthMonSrcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpIfRole.setStatus("current")
_CfprApSwEthMonSrcEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwEthMonSrcEpIfType_Object = MibTableColumn
cfprApSwEthMonSrcEpIfType = _CfprApSwEthMonSrcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 9),
    _CfprApSwEthMonSrcEpIfType_Type()
)
cfprApSwEthMonSrcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpIfType.setStatus("current")
_CfprApSwEthMonSrcEpLc_Type = CfprApSwPIoEpLc
_CfprApSwEthMonSrcEpLc_Object = MibTableColumn
cfprApSwEthMonSrcEpLc = _CfprApSwEthMonSrcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 10),
    _CfprApSwEthMonSrcEpLc_Type()
)
cfprApSwEthMonSrcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpLc.setStatus("current")
_CfprApSwEthMonSrcEpLocale_Type = CfprApSwMonSrcEpLocale
_CfprApSwEthMonSrcEpLocale_Object = MibTableColumn
cfprApSwEthMonSrcEpLocale = _CfprApSwEthMonSrcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 11),
    _CfprApSwEthMonSrcEpLocale_Type()
)
cfprApSwEthMonSrcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpLocale.setStatus("current")
_CfprApSwEthMonSrcEpMonTrafDir_Type = CfprApFabricTrafficDirection
_CfprApSwEthMonSrcEpMonTrafDir_Object = MibTableColumn
cfprApSwEthMonSrcEpMonTrafDir = _CfprApSwEthMonSrcEpMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 12),
    _CfprApSwEthMonSrcEpMonTrafDir_Type()
)
cfprApSwEthMonSrcEpMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpMonTrafDir.setStatus("current")
_CfprApSwEthMonSrcEpName_Type = SnmpAdminString
_CfprApSwEthMonSrcEpName_Object = MibTableColumn
cfprApSwEthMonSrcEpName = _CfprApSwEthMonSrcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 13),
    _CfprApSwEthMonSrcEpName_Type()
)
cfprApSwEthMonSrcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpName.setStatus("current")
_CfprApSwEthMonSrcEpPeerAggrPortId_Type = Gauge32
_CfprApSwEthMonSrcEpPeerAggrPortId_Object = MibTableColumn
cfprApSwEthMonSrcEpPeerAggrPortId = _CfprApSwEthMonSrcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 14),
    _CfprApSwEthMonSrcEpPeerAggrPortId_Type()
)
cfprApSwEthMonSrcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpPeerAggrPortId.setStatus("current")
_CfprApSwEthMonSrcEpPeerChassisId_Type = Gauge32
_CfprApSwEthMonSrcEpPeerChassisId_Object = MibTableColumn
cfprApSwEthMonSrcEpPeerChassisId = _CfprApSwEthMonSrcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 15),
    _CfprApSwEthMonSrcEpPeerChassisId_Type()
)
cfprApSwEthMonSrcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpPeerChassisId.setStatus("current")
_CfprApSwEthMonSrcEpPeerDn_Type = SnmpAdminString
_CfprApSwEthMonSrcEpPeerDn_Object = MibTableColumn
cfprApSwEthMonSrcEpPeerDn = _CfprApSwEthMonSrcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 16),
    _CfprApSwEthMonSrcEpPeerDn_Type()
)
cfprApSwEthMonSrcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpPeerDn.setStatus("current")
_CfprApSwEthMonSrcEpPeerPortId_Type = Gauge32
_CfprApSwEthMonSrcEpPeerPortId_Object = MibTableColumn
cfprApSwEthMonSrcEpPeerPortId = _CfprApSwEthMonSrcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 17),
    _CfprApSwEthMonSrcEpPeerPortId_Type()
)
cfprApSwEthMonSrcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpPeerPortId.setStatus("current")
_CfprApSwEthMonSrcEpPeerSlotId_Type = Gauge32
_CfprApSwEthMonSrcEpPeerSlotId_Object = MibTableColumn
cfprApSwEthMonSrcEpPeerSlotId = _CfprApSwEthMonSrcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 18),
    _CfprApSwEthMonSrcEpPeerSlotId_Type()
)
cfprApSwEthMonSrcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpPeerSlotId.setStatus("current")
_CfprApSwEthMonSrcEpPortId_Type = Gauge32
_CfprApSwEthMonSrcEpPortId_Object = MibTableColumn
cfprApSwEthMonSrcEpPortId = _CfprApSwEthMonSrcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 19),
    _CfprApSwEthMonSrcEpPortId_Type()
)
cfprApSwEthMonSrcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpPortId.setStatus("current")
_CfprApSwEthMonSrcEpSlotId_Type = Gauge32
_CfprApSwEthMonSrcEpSlotId_Object = MibTableColumn
cfprApSwEthMonSrcEpSlotId = _CfprApSwEthMonSrcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 20),
    _CfprApSwEthMonSrcEpSlotId_Type()
)
cfprApSwEthMonSrcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpSlotId.setStatus("current")
_CfprApSwEthMonSrcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthMonSrcEpSwitchId_Object = MibTableColumn
cfprApSwEthMonSrcEpSwitchId = _CfprApSwEthMonSrcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 21),
    _CfprApSwEthMonSrcEpSwitchId_Type()
)
cfprApSwEthMonSrcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpSwitchId.setStatus("current")
_CfprApSwEthMonSrcEpTransport_Type = CfprApSwEthMonSrcEpTransport
_CfprApSwEthMonSrcEpTransport_Object = MibTableColumn
cfprApSwEthMonSrcEpTransport = _CfprApSwEthMonSrcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 22),
    _CfprApSwEthMonSrcEpTransport_Type()
)
cfprApSwEthMonSrcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpTransport.setStatus("current")
_CfprApSwEthMonSrcEpType_Type = CfprApNetworkConnectionType
_CfprApSwEthMonSrcEpType_Object = MibTableColumn
cfprApSwEthMonSrcEpType = _CfprApSwEthMonSrcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 29, 1, 23),
    _CfprApSwEthMonSrcEpType_Type()
)
cfprApSwEthMonSrcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthMonSrcEpType.setStatus("current")
_CfprApSwEthTargetEpTable_Object = MibTable
cfprApSwEthTargetEpTable = _CfprApSwEthTargetEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30)
)
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpTable.setStatus("current")
_CfprApSwEthTargetEpEntry_Object = MibTableRow
cfprApSwEthTargetEpEntry = _CfprApSwEthTargetEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1)
)
cfprApSwEthTargetEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwEthTargetEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpEntry.setStatus("current")
_CfprApSwEthTargetEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwEthTargetEpInstanceId_Object = MibTableColumn
cfprApSwEthTargetEpInstanceId = _CfprApSwEthTargetEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 1),
    _CfprApSwEthTargetEpInstanceId_Type()
)
cfprApSwEthTargetEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpInstanceId.setStatus("current")
_CfprApSwEthTargetEpDn_Type = CfprApManagedObjectDn
_CfprApSwEthTargetEpDn_Object = MibTableColumn
cfprApSwEthTargetEpDn = _CfprApSwEthTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 2),
    _CfprApSwEthTargetEpDn_Type()
)
cfprApSwEthTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpDn.setStatus("current")
_CfprApSwEthTargetEpRn_Type = SnmpAdminString
_CfprApSwEthTargetEpRn_Object = MibTableColumn
cfprApSwEthTargetEpRn = _CfprApSwEthTargetEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 3),
    _CfprApSwEthTargetEpRn_Type()
)
cfprApSwEthTargetEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpRn.setStatus("current")
_CfprApSwEthTargetEpAdminState_Type = CfprApSwEthTargetEpAdminState
_CfprApSwEthTargetEpAdminState_Object = MibTableColumn
cfprApSwEthTargetEpAdminState = _CfprApSwEthTargetEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 4),
    _CfprApSwEthTargetEpAdminState_Type()
)
cfprApSwEthTargetEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpAdminState.setStatus("current")
_CfprApSwEthTargetEpAggrPortId_Type = Gauge32
_CfprApSwEthTargetEpAggrPortId_Object = MibTableColumn
cfprApSwEthTargetEpAggrPortId = _CfprApSwEthTargetEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 5),
    _CfprApSwEthTargetEpAggrPortId_Type()
)
cfprApSwEthTargetEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpAggrPortId.setStatus("current")
_CfprApSwEthTargetEpChassisId_Type = Gauge32
_CfprApSwEthTargetEpChassisId_Object = MibTableColumn
cfprApSwEthTargetEpChassisId = _CfprApSwEthTargetEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 6),
    _CfprApSwEthTargetEpChassisId_Type()
)
cfprApSwEthTargetEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpChassisId.setStatus("current")
_CfprApSwEthTargetEpEpDn_Type = SnmpAdminString
_CfprApSwEthTargetEpEpDn_Object = MibTableColumn
cfprApSwEthTargetEpEpDn = _CfprApSwEthTargetEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 7),
    _CfprApSwEthTargetEpEpDn_Type()
)
cfprApSwEthTargetEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpEpDn.setStatus("current")
_CfprApSwEthTargetEpFltAggr_Type = Unsigned64
_CfprApSwEthTargetEpFltAggr_Object = MibTableColumn
cfprApSwEthTargetEpFltAggr = _CfprApSwEthTargetEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 8),
    _CfprApSwEthTargetEpFltAggr_Type()
)
cfprApSwEthTargetEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpFltAggr.setStatus("current")
_CfprApSwEthTargetEpIfRole_Type = CfprApNetworkPortRole
_CfprApSwEthTargetEpIfRole_Object = MibTableColumn
cfprApSwEthTargetEpIfRole = _CfprApSwEthTargetEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 9),
    _CfprApSwEthTargetEpIfRole_Type()
)
cfprApSwEthTargetEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpIfRole.setStatus("current")
_CfprApSwEthTargetEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApSwEthTargetEpIfType_Object = MibTableColumn
cfprApSwEthTargetEpIfType = _CfprApSwEthTargetEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 10),
    _CfprApSwEthTargetEpIfType_Type()
)
cfprApSwEthTargetEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpIfType.setStatus("current")
_CfprApSwEthTargetEpLicGP_Type = Unsigned64
_CfprApSwEthTargetEpLicGP_Object = MibTableColumn
cfprApSwEthTargetEpLicGP = _CfprApSwEthTargetEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 11),
    _CfprApSwEthTargetEpLicGP_Type()
)
cfprApSwEthTargetEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpLicGP.setStatus("current")
_CfprApSwEthTargetEpLicState_Type = CfprApLicenseState
_CfprApSwEthTargetEpLicState_Object = MibTableColumn
cfprApSwEthTargetEpLicState = _CfprApSwEthTargetEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 12),
    _CfprApSwEthTargetEpLicState_Type()
)
cfprApSwEthTargetEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpLicState.setStatus("current")
_CfprApSwEthTargetEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApSwEthTargetEpLocale_Object = MibTableColumn
cfprApSwEthTargetEpLocale = _CfprApSwEthTargetEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 13),
    _CfprApSwEthTargetEpLocale_Type()
)
cfprApSwEthTargetEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpLocale.setStatus("current")
_CfprApSwEthTargetEpMacAddress_Type = MacAddress
_CfprApSwEthTargetEpMacAddress_Object = MibTableColumn
cfprApSwEthTargetEpMacAddress = _CfprApSwEthTargetEpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 14),
    _CfprApSwEthTargetEpMacAddress_Type()
)
cfprApSwEthTargetEpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpMacAddress.setStatus("current")
_CfprApSwEthTargetEpName_Type = SnmpAdminString
_CfprApSwEthTargetEpName_Object = MibTableColumn
cfprApSwEthTargetEpName = _CfprApSwEthTargetEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 15),
    _CfprApSwEthTargetEpName_Type()
)
cfprApSwEthTargetEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpName.setStatus("current")
_CfprApSwEthTargetEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApSwEthTargetEpOperState_Object = MibTableColumn
cfprApSwEthTargetEpOperState = _CfprApSwEthTargetEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 16),
    _CfprApSwEthTargetEpOperState_Type()
)
cfprApSwEthTargetEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpOperState.setStatus("current")
_CfprApSwEthTargetEpOperStateReason_Type = SnmpAdminString
_CfprApSwEthTargetEpOperStateReason_Object = MibTableColumn
cfprApSwEthTargetEpOperStateReason = _CfprApSwEthTargetEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 17),
    _CfprApSwEthTargetEpOperStateReason_Type()
)
cfprApSwEthTargetEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpOperStateReason.setStatus("current")
_CfprApSwEthTargetEpPeerAggrPortId_Type = Gauge32
_CfprApSwEthTargetEpPeerAggrPortId_Object = MibTableColumn
cfprApSwEthTargetEpPeerAggrPortId = _CfprApSwEthTargetEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 18),
    _CfprApSwEthTargetEpPeerAggrPortId_Type()
)
cfprApSwEthTargetEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpPeerAggrPortId.setStatus("current")
_CfprApSwEthTargetEpPeerChassisId_Type = Gauge32
_CfprApSwEthTargetEpPeerChassisId_Object = MibTableColumn
cfprApSwEthTargetEpPeerChassisId = _CfprApSwEthTargetEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 19),
    _CfprApSwEthTargetEpPeerChassisId_Type()
)
cfprApSwEthTargetEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpPeerChassisId.setStatus("current")
_CfprApSwEthTargetEpPeerDn_Type = SnmpAdminString
_CfprApSwEthTargetEpPeerDn_Object = MibTableColumn
cfprApSwEthTargetEpPeerDn = _CfprApSwEthTargetEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 20),
    _CfprApSwEthTargetEpPeerDn_Type()
)
cfprApSwEthTargetEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpPeerDn.setStatus("current")
_CfprApSwEthTargetEpPeerPortId_Type = Gauge32
_CfprApSwEthTargetEpPeerPortId_Object = MibTableColumn
cfprApSwEthTargetEpPeerPortId = _CfprApSwEthTargetEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 21),
    _CfprApSwEthTargetEpPeerPortId_Type()
)
cfprApSwEthTargetEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpPeerPortId.setStatus("current")
_CfprApSwEthTargetEpPeerSlotId_Type = Gauge32
_CfprApSwEthTargetEpPeerSlotId_Object = MibTableColumn
cfprApSwEthTargetEpPeerSlotId = _CfprApSwEthTargetEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 22),
    _CfprApSwEthTargetEpPeerSlotId_Type()
)
cfprApSwEthTargetEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpPeerSlotId.setStatus("current")
_CfprApSwEthTargetEpPortId_Type = CfprApFabricPIoEpPortId
_CfprApSwEthTargetEpPortId_Object = MibTableColumn
cfprApSwEthTargetEpPortId = _CfprApSwEthTargetEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 23),
    _CfprApSwEthTargetEpPortId_Type()
)
cfprApSwEthTargetEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpPortId.setStatus("current")
_CfprApSwEthTargetEpSlotId_Type = CfprApFabricPIoEpSlotId
_CfprApSwEthTargetEpSlotId_Object = MibTableColumn
cfprApSwEthTargetEpSlotId = _CfprApSwEthTargetEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 24),
    _CfprApSwEthTargetEpSlotId_Type()
)
cfprApSwEthTargetEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpSlotId.setStatus("current")
_CfprApSwEthTargetEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwEthTargetEpSwitchId_Object = MibTableColumn
cfprApSwEthTargetEpSwitchId = _CfprApSwEthTargetEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 25),
    _CfprApSwEthTargetEpSwitchId_Type()
)
cfprApSwEthTargetEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpSwitchId.setStatus("current")
_CfprApSwEthTargetEpTransport_Type = CfprApSwEthTargetEpTransport
_CfprApSwEthTargetEpTransport_Object = MibTableColumn
cfprApSwEthTargetEpTransport = _CfprApSwEthTargetEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 26),
    _CfprApSwEthTargetEpTransport_Type()
)
cfprApSwEthTargetEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpTransport.setStatus("current")
_CfprApSwEthTargetEpType_Type = CfprApSwTargetEpType
_CfprApSwEthTargetEpType_Object = MibTableColumn
cfprApSwEthTargetEpType = _CfprApSwEthTargetEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 27),
    _CfprApSwEthTargetEpType_Type()
)
cfprApSwEthTargetEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpType.setStatus("current")
_CfprApSwEthTargetEpWarnings_Type = CfprApFabricWarnings
_CfprApSwEthTargetEpWarnings_Object = MibTableColumn
cfprApSwEthTargetEpWarnings = _CfprApSwEthTargetEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 30, 1, 28),
    _CfprApSwEthTargetEpWarnings_Type()
)
cfprApSwEthTargetEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwEthTargetEpWarnings.setStatus("current")
_CfprApSwExtUtilityTable_Object = MibTable
cfprApSwExtUtilityTable = _CfprApSwExtUtilityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31)
)
if mibBuilder.loadTexts:
    cfprApSwExtUtilityTable.setStatus("current")
_CfprApSwExtUtilityEntry_Object = MibTableRow
cfprApSwExtUtilityEntry = _CfprApSwExtUtilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1)
)
cfprApSwExtUtilityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwExtUtilityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwExtUtilityEntry.setStatus("current")
_CfprApSwExtUtilityInstanceId_Type = CfprApManagedObjectId
_CfprApSwExtUtilityInstanceId_Object = MibTableColumn
cfprApSwExtUtilityInstanceId = _CfprApSwExtUtilityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 1),
    _CfprApSwExtUtilityInstanceId_Type()
)
cfprApSwExtUtilityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityInstanceId.setStatus("current")
_CfprApSwExtUtilityDn_Type = CfprApManagedObjectDn
_CfprApSwExtUtilityDn_Object = MibTableColumn
cfprApSwExtUtilityDn = _CfprApSwExtUtilityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 2),
    _CfprApSwExtUtilityDn_Type()
)
cfprApSwExtUtilityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityDn.setStatus("current")
_CfprApSwExtUtilityRn_Type = SnmpAdminString
_CfprApSwExtUtilityRn_Object = MibTableColumn
cfprApSwExtUtilityRn = _CfprApSwExtUtilityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 3),
    _CfprApSwExtUtilityRn_Type()
)
cfprApSwExtUtilityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityRn.setStatus("current")
_CfprApSwExtUtilityConfMode_Type = CfprApSwConfMode
_CfprApSwExtUtilityConfMode_Object = MibTableColumn
cfprApSwExtUtilityConfMode = _CfprApSwExtUtilityConfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 4),
    _CfprApSwExtUtilityConfMode_Type()
)
cfprApSwExtUtilityConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityConfMode.setStatus("current")
_CfprApSwExtUtilityFsmDescr_Type = SnmpAdminString
_CfprApSwExtUtilityFsmDescr_Object = MibTableColumn
cfprApSwExtUtilityFsmDescr = _CfprApSwExtUtilityFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 5),
    _CfprApSwExtUtilityFsmDescr_Type()
)
cfprApSwExtUtilityFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmDescr.setStatus("current")
_CfprApSwExtUtilityFsmPrev_Type = SnmpAdminString
_CfprApSwExtUtilityFsmPrev_Object = MibTableColumn
cfprApSwExtUtilityFsmPrev = _CfprApSwExtUtilityFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 6),
    _CfprApSwExtUtilityFsmPrev_Type()
)
cfprApSwExtUtilityFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmPrev.setStatus("current")
_CfprApSwExtUtilityFsmProgr_Type = Gauge32
_CfprApSwExtUtilityFsmProgr_Object = MibTableColumn
cfprApSwExtUtilityFsmProgr = _CfprApSwExtUtilityFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 7),
    _CfprApSwExtUtilityFsmProgr_Type()
)
cfprApSwExtUtilityFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmProgr.setStatus("current")
_CfprApSwExtUtilityFsmRmtInvErrCode_Type = Gauge32
_CfprApSwExtUtilityFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwExtUtilityFsmRmtInvErrCode = _CfprApSwExtUtilityFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 8),
    _CfprApSwExtUtilityFsmRmtInvErrCode_Type()
)
cfprApSwExtUtilityFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmRmtInvErrCode.setStatus("current")
_CfprApSwExtUtilityFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwExtUtilityFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwExtUtilityFsmRmtInvErrDescr = _CfprApSwExtUtilityFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 9),
    _CfprApSwExtUtilityFsmRmtInvErrDescr_Type()
)
cfprApSwExtUtilityFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmRmtInvErrDescr.setStatus("current")
_CfprApSwExtUtilityFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwExtUtilityFsmRmtInvRslt_Object = MibTableColumn
cfprApSwExtUtilityFsmRmtInvRslt = _CfprApSwExtUtilityFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 10),
    _CfprApSwExtUtilityFsmRmtInvRslt_Type()
)
cfprApSwExtUtilityFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmRmtInvRslt.setStatus("current")
_CfprApSwExtUtilityFsmStageDescr_Type = SnmpAdminString
_CfprApSwExtUtilityFsmStageDescr_Object = MibTableColumn
cfprApSwExtUtilityFsmStageDescr = _CfprApSwExtUtilityFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 11),
    _CfprApSwExtUtilityFsmStageDescr_Type()
)
cfprApSwExtUtilityFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageDescr.setStatus("current")
_CfprApSwExtUtilityFsmStamp_Type = DateAndTime
_CfprApSwExtUtilityFsmStamp_Object = MibTableColumn
cfprApSwExtUtilityFsmStamp = _CfprApSwExtUtilityFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 12),
    _CfprApSwExtUtilityFsmStamp_Type()
)
cfprApSwExtUtilityFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStamp.setStatus("current")
_CfprApSwExtUtilityFsmStatus_Type = SnmpAdminString
_CfprApSwExtUtilityFsmStatus_Object = MibTableColumn
cfprApSwExtUtilityFsmStatus = _CfprApSwExtUtilityFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 13),
    _CfprApSwExtUtilityFsmStatus_Type()
)
cfprApSwExtUtilityFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStatus.setStatus("current")
_CfprApSwExtUtilityFsmTry_Type = Gauge32
_CfprApSwExtUtilityFsmTry_Object = MibTableColumn
cfprApSwExtUtilityFsmTry = _CfprApSwExtUtilityFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 14),
    _CfprApSwExtUtilityFsmTry_Type()
)
cfprApSwExtUtilityFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTry.setStatus("current")
_CfprApSwExtUtilitySwitchId_Type = CfprApNetworkSwitchId
_CfprApSwExtUtilitySwitchId_Object = MibTableColumn
cfprApSwExtUtilitySwitchId = _CfprApSwExtUtilitySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 31, 1, 15),
    _CfprApSwExtUtilitySwitchId_Type()
)
cfprApSwExtUtilitySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilitySwitchId.setStatus("current")
_CfprApSwExtUtilityFsmTable_Object = MibTable
cfprApSwExtUtilityFsmTable = _CfprApSwExtUtilityFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32)
)
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTable.setStatus("current")
_CfprApSwExtUtilityFsmEntry_Object = MibTableRow
cfprApSwExtUtilityFsmEntry = _CfprApSwExtUtilityFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1)
)
cfprApSwExtUtilityFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwExtUtilityFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmEntry.setStatus("current")
_CfprApSwExtUtilityFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwExtUtilityFsmInstanceId_Object = MibTableColumn
cfprApSwExtUtilityFsmInstanceId = _CfprApSwExtUtilityFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 1),
    _CfprApSwExtUtilityFsmInstanceId_Type()
)
cfprApSwExtUtilityFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmInstanceId.setStatus("current")
_CfprApSwExtUtilityFsmDn_Type = CfprApManagedObjectDn
_CfprApSwExtUtilityFsmDn_Object = MibTableColumn
cfprApSwExtUtilityFsmDn = _CfprApSwExtUtilityFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 2),
    _CfprApSwExtUtilityFsmDn_Type()
)
cfprApSwExtUtilityFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmDn.setStatus("current")
_CfprApSwExtUtilityFsmRn_Type = SnmpAdminString
_CfprApSwExtUtilityFsmRn_Object = MibTableColumn
cfprApSwExtUtilityFsmRn = _CfprApSwExtUtilityFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 3),
    _CfprApSwExtUtilityFsmRn_Type()
)
cfprApSwExtUtilityFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmRn.setStatus("current")
_CfprApSwExtUtilityFsmCompletionTime_Type = DateAndTime
_CfprApSwExtUtilityFsmCompletionTime_Object = MibTableColumn
cfprApSwExtUtilityFsmCompletionTime = _CfprApSwExtUtilityFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 4),
    _CfprApSwExtUtilityFsmCompletionTime_Type()
)
cfprApSwExtUtilityFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmCompletionTime.setStatus("current")
_CfprApSwExtUtilityFsmCurrentFsm_Type = CfprApSwExtUtilityFsmCurrentFsm
_CfprApSwExtUtilityFsmCurrentFsm_Object = MibTableColumn
cfprApSwExtUtilityFsmCurrentFsm = _CfprApSwExtUtilityFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 5),
    _CfprApSwExtUtilityFsmCurrentFsm_Type()
)
cfprApSwExtUtilityFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmCurrentFsm.setStatus("current")
_CfprApSwExtUtilityFsmDescrData_Type = SnmpAdminString
_CfprApSwExtUtilityFsmDescrData_Object = MibTableColumn
cfprApSwExtUtilityFsmDescrData = _CfprApSwExtUtilityFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 6),
    _CfprApSwExtUtilityFsmDescrData_Type()
)
cfprApSwExtUtilityFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmDescrData.setStatus("current")
_CfprApSwExtUtilityFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwExtUtilityFsmFsmStatus_Object = MibTableColumn
cfprApSwExtUtilityFsmFsmStatus = _CfprApSwExtUtilityFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 7),
    _CfprApSwExtUtilityFsmFsmStatus_Type()
)
cfprApSwExtUtilityFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmFsmStatus.setStatus("current")
_CfprApSwExtUtilityFsmProgress_Type = Gauge32
_CfprApSwExtUtilityFsmProgress_Object = MibTableColumn
cfprApSwExtUtilityFsmProgress = _CfprApSwExtUtilityFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 8),
    _CfprApSwExtUtilityFsmProgress_Type()
)
cfprApSwExtUtilityFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmProgress.setStatus("current")
_CfprApSwExtUtilityFsmRmtErrCode_Type = Gauge32
_CfprApSwExtUtilityFsmRmtErrCode_Object = MibTableColumn
cfprApSwExtUtilityFsmRmtErrCode = _CfprApSwExtUtilityFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 9),
    _CfprApSwExtUtilityFsmRmtErrCode_Type()
)
cfprApSwExtUtilityFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmRmtErrCode.setStatus("current")
_CfprApSwExtUtilityFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwExtUtilityFsmRmtErrDescr_Object = MibTableColumn
cfprApSwExtUtilityFsmRmtErrDescr = _CfprApSwExtUtilityFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 10),
    _CfprApSwExtUtilityFsmRmtErrDescr_Type()
)
cfprApSwExtUtilityFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmRmtErrDescr.setStatus("current")
_CfprApSwExtUtilityFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwExtUtilityFsmRmtRslt_Object = MibTableColumn
cfprApSwExtUtilityFsmRmtRslt = _CfprApSwExtUtilityFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 32, 1, 11),
    _CfprApSwExtUtilityFsmRmtRslt_Type()
)
cfprApSwExtUtilityFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmRmtRslt.setStatus("current")
_CfprApSwExtUtilityFsmStageTable_Object = MibTable
cfprApSwExtUtilityFsmStageTable = _CfprApSwExtUtilityFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33)
)
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageTable.setStatus("current")
_CfprApSwExtUtilityFsmStageEntry_Object = MibTableRow
cfprApSwExtUtilityFsmStageEntry = _CfprApSwExtUtilityFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1)
)
cfprApSwExtUtilityFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwExtUtilityFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageEntry.setStatus("current")
_CfprApSwExtUtilityFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwExtUtilityFsmStageInstanceId_Object = MibTableColumn
cfprApSwExtUtilityFsmStageInstanceId = _CfprApSwExtUtilityFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 1),
    _CfprApSwExtUtilityFsmStageInstanceId_Type()
)
cfprApSwExtUtilityFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageInstanceId.setStatus("current")
_CfprApSwExtUtilityFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwExtUtilityFsmStageDn_Object = MibTableColumn
cfprApSwExtUtilityFsmStageDn = _CfprApSwExtUtilityFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 2),
    _CfprApSwExtUtilityFsmStageDn_Type()
)
cfprApSwExtUtilityFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageDn.setStatus("current")
_CfprApSwExtUtilityFsmStageRn_Type = SnmpAdminString
_CfprApSwExtUtilityFsmStageRn_Object = MibTableColumn
cfprApSwExtUtilityFsmStageRn = _CfprApSwExtUtilityFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 3),
    _CfprApSwExtUtilityFsmStageRn_Type()
)
cfprApSwExtUtilityFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageRn.setStatus("current")
_CfprApSwExtUtilityFsmStageDescrData_Type = SnmpAdminString
_CfprApSwExtUtilityFsmStageDescrData_Object = MibTableColumn
cfprApSwExtUtilityFsmStageDescrData = _CfprApSwExtUtilityFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 4),
    _CfprApSwExtUtilityFsmStageDescrData_Type()
)
cfprApSwExtUtilityFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageDescrData.setStatus("current")
_CfprApSwExtUtilityFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwExtUtilityFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwExtUtilityFsmStageLastUpdateTime = _CfprApSwExtUtilityFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 5),
    _CfprApSwExtUtilityFsmStageLastUpdateTime_Type()
)
cfprApSwExtUtilityFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageLastUpdateTime.setStatus("current")
_CfprApSwExtUtilityFsmStageName_Type = CfprApSwExtUtilityFsmStageName
_CfprApSwExtUtilityFsmStageName_Object = MibTableColumn
cfprApSwExtUtilityFsmStageName = _CfprApSwExtUtilityFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 6),
    _CfprApSwExtUtilityFsmStageName_Type()
)
cfprApSwExtUtilityFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageName.setStatus("current")
_CfprApSwExtUtilityFsmStageOrder_Type = Gauge32
_CfprApSwExtUtilityFsmStageOrder_Object = MibTableColumn
cfprApSwExtUtilityFsmStageOrder = _CfprApSwExtUtilityFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 7),
    _CfprApSwExtUtilityFsmStageOrder_Type()
)
cfprApSwExtUtilityFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageOrder.setStatus("current")
_CfprApSwExtUtilityFsmStageRetry_Type = Gauge32
_CfprApSwExtUtilityFsmStageRetry_Object = MibTableColumn
cfprApSwExtUtilityFsmStageRetry = _CfprApSwExtUtilityFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 8),
    _CfprApSwExtUtilityFsmStageRetry_Type()
)
cfprApSwExtUtilityFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageRetry.setStatus("current")
_CfprApSwExtUtilityFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwExtUtilityFsmStageStageStatus_Object = MibTableColumn
cfprApSwExtUtilityFsmStageStageStatus = _CfprApSwExtUtilityFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 33, 1, 9),
    _CfprApSwExtUtilityFsmStageStageStatus_Type()
)
cfprApSwExtUtilityFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmStageStageStatus.setStatus("current")
_CfprApSwExtUtilityFsmTaskTable_Object = MibTable
cfprApSwExtUtilityFsmTaskTable = _CfprApSwExtUtilityFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34)
)
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskTable.setStatus("current")
_CfprApSwExtUtilityFsmTaskEntry_Object = MibTableRow
cfprApSwExtUtilityFsmTaskEntry = _CfprApSwExtUtilityFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34, 1)
)
cfprApSwExtUtilityFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwExtUtilityFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskEntry.setStatus("current")
_CfprApSwExtUtilityFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwExtUtilityFsmTaskInstanceId_Object = MibTableColumn
cfprApSwExtUtilityFsmTaskInstanceId = _CfprApSwExtUtilityFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34, 1, 1),
    _CfprApSwExtUtilityFsmTaskInstanceId_Type()
)
cfprApSwExtUtilityFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskInstanceId.setStatus("current")
_CfprApSwExtUtilityFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwExtUtilityFsmTaskDn_Object = MibTableColumn
cfprApSwExtUtilityFsmTaskDn = _CfprApSwExtUtilityFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34, 1, 2),
    _CfprApSwExtUtilityFsmTaskDn_Type()
)
cfprApSwExtUtilityFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskDn.setStatus("current")
_CfprApSwExtUtilityFsmTaskRn_Type = SnmpAdminString
_CfprApSwExtUtilityFsmTaskRn_Object = MibTableColumn
cfprApSwExtUtilityFsmTaskRn = _CfprApSwExtUtilityFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34, 1, 3),
    _CfprApSwExtUtilityFsmTaskRn_Type()
)
cfprApSwExtUtilityFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskRn.setStatus("current")
_CfprApSwExtUtilityFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwExtUtilityFsmTaskCompletion_Object = MibTableColumn
cfprApSwExtUtilityFsmTaskCompletion = _CfprApSwExtUtilityFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34, 1, 4),
    _CfprApSwExtUtilityFsmTaskCompletion_Type()
)
cfprApSwExtUtilityFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskCompletion.setStatus("current")
_CfprApSwExtUtilityFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSwExtUtilityFsmTaskFlags_Object = MibTableColumn
cfprApSwExtUtilityFsmTaskFlags = _CfprApSwExtUtilityFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34, 1, 5),
    _CfprApSwExtUtilityFsmTaskFlags_Type()
)
cfprApSwExtUtilityFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskFlags.setStatus("current")
_CfprApSwExtUtilityFsmTaskItem_Type = CfprApSwExtUtilityFsmTaskItem
_CfprApSwExtUtilityFsmTaskItem_Object = MibTableColumn
cfprApSwExtUtilityFsmTaskItem = _CfprApSwExtUtilityFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34, 1, 6),
    _CfprApSwExtUtilityFsmTaskItem_Type()
)
cfprApSwExtUtilityFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskItem.setStatus("current")
_CfprApSwExtUtilityFsmTaskSeqId_Type = Gauge32
_CfprApSwExtUtilityFsmTaskSeqId_Object = MibTableColumn
cfprApSwExtUtilityFsmTaskSeqId = _CfprApSwExtUtilityFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 34, 1, 7),
    _CfprApSwExtUtilityFsmTaskSeqId_Type()
)
cfprApSwExtUtilityFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwExtUtilityFsmTaskSeqId.setStatus("current")
_CfprApSwFabricZoneNsTable_Object = MibTable
cfprApSwFabricZoneNsTable = _CfprApSwFabricZoneNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35)
)
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsTable.setStatus("current")
_CfprApSwFabricZoneNsEntry_Object = MibTableRow
cfprApSwFabricZoneNsEntry = _CfprApSwFabricZoneNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35, 1)
)
cfprApSwFabricZoneNsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFabricZoneNsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsEntry.setStatus("current")
_CfprApSwFabricZoneNsInstanceId_Type = CfprApManagedObjectId
_CfprApSwFabricZoneNsInstanceId_Object = MibTableColumn
cfprApSwFabricZoneNsInstanceId = _CfprApSwFabricZoneNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35, 1, 1),
    _CfprApSwFabricZoneNsInstanceId_Type()
)
cfprApSwFabricZoneNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsInstanceId.setStatus("current")
_CfprApSwFabricZoneNsDn_Type = CfprApManagedObjectDn
_CfprApSwFabricZoneNsDn_Object = MibTableColumn
cfprApSwFabricZoneNsDn = _CfprApSwFabricZoneNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35, 1, 2),
    _CfprApSwFabricZoneNsDn_Type()
)
cfprApSwFabricZoneNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsDn.setStatus("current")
_CfprApSwFabricZoneNsRn_Type = SnmpAdminString
_CfprApSwFabricZoneNsRn_Object = MibTableColumn
cfprApSwFabricZoneNsRn = _CfprApSwFabricZoneNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35, 1, 3),
    _CfprApSwFabricZoneNsRn_Type()
)
cfprApSwFabricZoneNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsRn.setStatus("current")
_CfprApSwFabricZoneNsAllocStatus_Type = CfprApSwFabricZoneNsAllocStatus
_CfprApSwFabricZoneNsAllocStatus_Object = MibTableColumn
cfprApSwFabricZoneNsAllocStatus = _CfprApSwFabricZoneNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35, 1, 4),
    _CfprApSwFabricZoneNsAllocStatus_Type()
)
cfprApSwFabricZoneNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsAllocStatus.setStatus("current")
_CfprApSwFabricZoneNsLimit_Type = Gauge32
_CfprApSwFabricZoneNsLimit_Object = MibTableColumn
cfprApSwFabricZoneNsLimit = _CfprApSwFabricZoneNsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35, 1, 5),
    _CfprApSwFabricZoneNsLimit_Type()
)
cfprApSwFabricZoneNsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsLimit.setStatus("current")
_CfprApSwFabricZoneNsSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwFabricZoneNsSwitchId_Object = MibTableColumn
cfprApSwFabricZoneNsSwitchId = _CfprApSwFabricZoneNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35, 1, 6),
    _CfprApSwFabricZoneNsSwitchId_Type()
)
cfprApSwFabricZoneNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsSwitchId.setStatus("current")
_CfprApSwFabricZoneNsZoneCount_Type = Gauge32
_CfprApSwFabricZoneNsZoneCount_Object = MibTableColumn
cfprApSwFabricZoneNsZoneCount = _CfprApSwFabricZoneNsZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 35, 1, 7),
    _CfprApSwFabricZoneNsZoneCount_Type()
)
cfprApSwFabricZoneNsZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsZoneCount.setStatus("current")
_CfprApSwFabricZoneNsOverrideTable_Object = MibTable
cfprApSwFabricZoneNsOverrideTable = _CfprApSwFabricZoneNsOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 36)
)
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsOverrideTable.setStatus("current")
_CfprApSwFabricZoneNsOverrideEntry_Object = MibTableRow
cfprApSwFabricZoneNsOverrideEntry = _CfprApSwFabricZoneNsOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 36, 1)
)
cfprApSwFabricZoneNsOverrideEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFabricZoneNsOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsOverrideEntry.setStatus("current")
_CfprApSwFabricZoneNsOverrideInstanceId_Type = CfprApManagedObjectId
_CfprApSwFabricZoneNsOverrideInstanceId_Object = MibTableColumn
cfprApSwFabricZoneNsOverrideInstanceId = _CfprApSwFabricZoneNsOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 36, 1, 1),
    _CfprApSwFabricZoneNsOverrideInstanceId_Type()
)
cfprApSwFabricZoneNsOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsOverrideInstanceId.setStatus("current")
_CfprApSwFabricZoneNsOverrideDn_Type = CfprApManagedObjectDn
_CfprApSwFabricZoneNsOverrideDn_Object = MibTableColumn
cfprApSwFabricZoneNsOverrideDn = _CfprApSwFabricZoneNsOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 36, 1, 2),
    _CfprApSwFabricZoneNsOverrideDn_Type()
)
cfprApSwFabricZoneNsOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsOverrideDn.setStatus("current")
_CfprApSwFabricZoneNsOverrideRn_Type = SnmpAdminString
_CfprApSwFabricZoneNsOverrideRn_Object = MibTableColumn
cfprApSwFabricZoneNsOverrideRn = _CfprApSwFabricZoneNsOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 36, 1, 3),
    _CfprApSwFabricZoneNsOverrideRn_Type()
)
cfprApSwFabricZoneNsOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsOverrideRn.setStatus("current")
_CfprApSwFabricZoneNsOverrideLimit_Type = Gauge32
_CfprApSwFabricZoneNsOverrideLimit_Object = MibTableColumn
cfprApSwFabricZoneNsOverrideLimit = _CfprApSwFabricZoneNsOverrideLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 36, 1, 4),
    _CfprApSwFabricZoneNsOverrideLimit_Type()
)
cfprApSwFabricZoneNsOverrideLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFabricZoneNsOverrideLimit.setStatus("current")
_CfprApSwFcSanBorderTable_Object = MibTable
cfprApSwFcSanBorderTable = _CfprApSwFcSanBorderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44)
)
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderTable.setStatus("current")
_CfprApSwFcSanBorderEntry_Object = MibTableRow
cfprApSwFcSanBorderEntry = _CfprApSwFcSanBorderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1)
)
cfprApSwFcSanBorderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcSanBorderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderEntry.setStatus("current")
_CfprApSwFcSanBorderInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcSanBorderInstanceId_Object = MibTableColumn
cfprApSwFcSanBorderInstanceId = _CfprApSwFcSanBorderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 1),
    _CfprApSwFcSanBorderInstanceId_Type()
)
cfprApSwFcSanBorderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderInstanceId.setStatus("current")
_CfprApSwFcSanBorderDn_Type = CfprApManagedObjectDn
_CfprApSwFcSanBorderDn_Object = MibTableColumn
cfprApSwFcSanBorderDn = _CfprApSwFcSanBorderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 2),
    _CfprApSwFcSanBorderDn_Type()
)
cfprApSwFcSanBorderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderDn.setStatus("current")
_CfprApSwFcSanBorderRn_Type = SnmpAdminString
_CfprApSwFcSanBorderRn_Object = MibTableColumn
cfprApSwFcSanBorderRn = _CfprApSwFcSanBorderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 3),
    _CfprApSwFcSanBorderRn_Type()
)
cfprApSwFcSanBorderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderRn.setStatus("current")
_CfprApSwFcSanBorderFsmDescr_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmDescr_Object = MibTableColumn
cfprApSwFcSanBorderFsmDescr = _CfprApSwFcSanBorderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 4),
    _CfprApSwFcSanBorderFsmDescr_Type()
)
cfprApSwFcSanBorderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmDescr.setStatus("current")
_CfprApSwFcSanBorderFsmPrev_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmPrev_Object = MibTableColumn
cfprApSwFcSanBorderFsmPrev = _CfprApSwFcSanBorderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 5),
    _CfprApSwFcSanBorderFsmPrev_Type()
)
cfprApSwFcSanBorderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmPrev.setStatus("current")
_CfprApSwFcSanBorderFsmProgr_Type = Gauge32
_CfprApSwFcSanBorderFsmProgr_Object = MibTableColumn
cfprApSwFcSanBorderFsmProgr = _CfprApSwFcSanBorderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 6),
    _CfprApSwFcSanBorderFsmProgr_Type()
)
cfprApSwFcSanBorderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmProgr.setStatus("current")
_CfprApSwFcSanBorderFsmRmtInvErrCode_Type = Gauge32
_CfprApSwFcSanBorderFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwFcSanBorderFsmRmtInvErrCode = _CfprApSwFcSanBorderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 7),
    _CfprApSwFcSanBorderFsmRmtInvErrCode_Type()
)
cfprApSwFcSanBorderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmRmtInvErrCode.setStatus("current")
_CfprApSwFcSanBorderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwFcSanBorderFsmRmtInvErrDescr = _CfprApSwFcSanBorderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 8),
    _CfprApSwFcSanBorderFsmRmtInvErrDescr_Type()
)
cfprApSwFcSanBorderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmRmtInvErrDescr.setStatus("current")
_CfprApSwFcSanBorderFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwFcSanBorderFsmRmtInvRslt_Object = MibTableColumn
cfprApSwFcSanBorderFsmRmtInvRslt = _CfprApSwFcSanBorderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 9),
    _CfprApSwFcSanBorderFsmRmtInvRslt_Type()
)
cfprApSwFcSanBorderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmRmtInvRslt.setStatus("current")
_CfprApSwFcSanBorderFsmStageDescr_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmStageDescr_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageDescr = _CfprApSwFcSanBorderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 10),
    _CfprApSwFcSanBorderFsmStageDescr_Type()
)
cfprApSwFcSanBorderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageDescr.setStatus("current")
_CfprApSwFcSanBorderFsmStamp_Type = DateAndTime
_CfprApSwFcSanBorderFsmStamp_Object = MibTableColumn
cfprApSwFcSanBorderFsmStamp = _CfprApSwFcSanBorderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 11),
    _CfprApSwFcSanBorderFsmStamp_Type()
)
cfprApSwFcSanBorderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStamp.setStatus("current")
_CfprApSwFcSanBorderFsmStatus_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmStatus_Object = MibTableColumn
cfprApSwFcSanBorderFsmStatus = _CfprApSwFcSanBorderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 12),
    _CfprApSwFcSanBorderFsmStatus_Type()
)
cfprApSwFcSanBorderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStatus.setStatus("current")
_CfprApSwFcSanBorderFsmTry_Type = Gauge32
_CfprApSwFcSanBorderFsmTry_Object = MibTableColumn
cfprApSwFcSanBorderFsmTry = _CfprApSwFcSanBorderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 13),
    _CfprApSwFcSanBorderFsmTry_Type()
)
cfprApSwFcSanBorderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTry.setStatus("current")
_CfprApSwFcSanBorderLocale_Type = CfprApSwBorderDomainLocale
_CfprApSwFcSanBorderLocale_Object = MibTableColumn
cfprApSwFcSanBorderLocale = _CfprApSwFcSanBorderLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 14),
    _CfprApSwFcSanBorderLocale_Type()
)
cfprApSwFcSanBorderLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderLocale.setStatus("current")
_CfprApSwFcSanBorderName_Type = SnmpAdminString
_CfprApSwFcSanBorderName_Object = MibTableColumn
cfprApSwFcSanBorderName = _CfprApSwFcSanBorderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 15),
    _CfprApSwFcSanBorderName_Type()
)
cfprApSwFcSanBorderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderName.setStatus("current")
_CfprApSwFcSanBorderSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwFcSanBorderSwitchId_Object = MibTableColumn
cfprApSwFcSanBorderSwitchId = _CfprApSwFcSanBorderSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 16),
    _CfprApSwFcSanBorderSwitchId_Type()
)
cfprApSwFcSanBorderSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderSwitchId.setStatus("current")
_CfprApSwFcSanBorderTransport_Type = CfprApSwFcSanBorderTransport
_CfprApSwFcSanBorderTransport_Object = MibTableColumn
cfprApSwFcSanBorderTransport = _CfprApSwFcSanBorderTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 17),
    _CfprApSwFcSanBorderTransport_Type()
)
cfprApSwFcSanBorderTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderTransport.setStatus("current")
_CfprApSwFcSanBorderType_Type = CfprApSwSanBorderType
_CfprApSwFcSanBorderType_Object = MibTableColumn
cfprApSwFcSanBorderType = _CfprApSwFcSanBorderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 18),
    _CfprApSwFcSanBorderType_Type()
)
cfprApSwFcSanBorderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderType.setStatus("current")
_CfprApSwFcSanBorderUplinkTrunking_Type = CfprApSwFcSanBorderUplinkTrunking
_CfprApSwFcSanBorderUplinkTrunking_Object = MibTableColumn
cfprApSwFcSanBorderUplinkTrunking = _CfprApSwFcSanBorderUplinkTrunking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 44, 1, 19),
    _CfprApSwFcSanBorderUplinkTrunking_Type()
)
cfprApSwFcSanBorderUplinkTrunking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderUplinkTrunking.setStatus("current")
_CfprApSwFcSanBorderFsmTable_Object = MibTable
cfprApSwFcSanBorderFsmTable = _CfprApSwFcSanBorderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45)
)
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTable.setStatus("current")
_CfprApSwFcSanBorderFsmEntry_Object = MibTableRow
cfprApSwFcSanBorderFsmEntry = _CfprApSwFcSanBorderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1)
)
cfprApSwFcSanBorderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcSanBorderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmEntry.setStatus("current")
_CfprApSwFcSanBorderFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcSanBorderFsmInstanceId_Object = MibTableColumn
cfprApSwFcSanBorderFsmInstanceId = _CfprApSwFcSanBorderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 1),
    _CfprApSwFcSanBorderFsmInstanceId_Type()
)
cfprApSwFcSanBorderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmInstanceId.setStatus("current")
_CfprApSwFcSanBorderFsmDn_Type = CfprApManagedObjectDn
_CfprApSwFcSanBorderFsmDn_Object = MibTableColumn
cfprApSwFcSanBorderFsmDn = _CfprApSwFcSanBorderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 2),
    _CfprApSwFcSanBorderFsmDn_Type()
)
cfprApSwFcSanBorderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmDn.setStatus("current")
_CfprApSwFcSanBorderFsmRn_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmRn_Object = MibTableColumn
cfprApSwFcSanBorderFsmRn = _CfprApSwFcSanBorderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 3),
    _CfprApSwFcSanBorderFsmRn_Type()
)
cfprApSwFcSanBorderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmRn.setStatus("current")
_CfprApSwFcSanBorderFsmCompletionTime_Type = DateAndTime
_CfprApSwFcSanBorderFsmCompletionTime_Object = MibTableColumn
cfprApSwFcSanBorderFsmCompletionTime = _CfprApSwFcSanBorderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 4),
    _CfprApSwFcSanBorderFsmCompletionTime_Type()
)
cfprApSwFcSanBorderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmCompletionTime.setStatus("current")
_CfprApSwFcSanBorderFsmCurrentFsm_Type = CfprApSwFcSanBorderFsmCurrentFsm
_CfprApSwFcSanBorderFsmCurrentFsm_Object = MibTableColumn
cfprApSwFcSanBorderFsmCurrentFsm = _CfprApSwFcSanBorderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 5),
    _CfprApSwFcSanBorderFsmCurrentFsm_Type()
)
cfprApSwFcSanBorderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmCurrentFsm.setStatus("current")
_CfprApSwFcSanBorderFsmDescrData_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmDescrData_Object = MibTableColumn
cfprApSwFcSanBorderFsmDescrData = _CfprApSwFcSanBorderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 6),
    _CfprApSwFcSanBorderFsmDescrData_Type()
)
cfprApSwFcSanBorderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmDescrData.setStatus("current")
_CfprApSwFcSanBorderFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwFcSanBorderFsmFsmStatus_Object = MibTableColumn
cfprApSwFcSanBorderFsmFsmStatus = _CfprApSwFcSanBorderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 7),
    _CfprApSwFcSanBorderFsmFsmStatus_Type()
)
cfprApSwFcSanBorderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmFsmStatus.setStatus("current")
_CfprApSwFcSanBorderFsmProgress_Type = Gauge32
_CfprApSwFcSanBorderFsmProgress_Object = MibTableColumn
cfprApSwFcSanBorderFsmProgress = _CfprApSwFcSanBorderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 8),
    _CfprApSwFcSanBorderFsmProgress_Type()
)
cfprApSwFcSanBorderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmProgress.setStatus("current")
_CfprApSwFcSanBorderFsmRmtErrCode_Type = Gauge32
_CfprApSwFcSanBorderFsmRmtErrCode_Object = MibTableColumn
cfprApSwFcSanBorderFsmRmtErrCode = _CfprApSwFcSanBorderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 9),
    _CfprApSwFcSanBorderFsmRmtErrCode_Type()
)
cfprApSwFcSanBorderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmRmtErrCode.setStatus("current")
_CfprApSwFcSanBorderFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmRmtErrDescr_Object = MibTableColumn
cfprApSwFcSanBorderFsmRmtErrDescr = _CfprApSwFcSanBorderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 10),
    _CfprApSwFcSanBorderFsmRmtErrDescr_Type()
)
cfprApSwFcSanBorderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmRmtErrDescr.setStatus("current")
_CfprApSwFcSanBorderFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwFcSanBorderFsmRmtRslt_Object = MibTableColumn
cfprApSwFcSanBorderFsmRmtRslt = _CfprApSwFcSanBorderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 45, 1, 11),
    _CfprApSwFcSanBorderFsmRmtRslt_Type()
)
cfprApSwFcSanBorderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmRmtRslt.setStatus("current")
_CfprApSwFcSanBorderFsmStageTable_Object = MibTable
cfprApSwFcSanBorderFsmStageTable = _CfprApSwFcSanBorderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46)
)
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageTable.setStatus("current")
_CfprApSwFcSanBorderFsmStageEntry_Object = MibTableRow
cfprApSwFcSanBorderFsmStageEntry = _CfprApSwFcSanBorderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1)
)
cfprApSwFcSanBorderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcSanBorderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageEntry.setStatus("current")
_CfprApSwFcSanBorderFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcSanBorderFsmStageInstanceId_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageInstanceId = _CfprApSwFcSanBorderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 1),
    _CfprApSwFcSanBorderFsmStageInstanceId_Type()
)
cfprApSwFcSanBorderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageInstanceId.setStatus("current")
_CfprApSwFcSanBorderFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwFcSanBorderFsmStageDn_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageDn = _CfprApSwFcSanBorderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 2),
    _CfprApSwFcSanBorderFsmStageDn_Type()
)
cfprApSwFcSanBorderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageDn.setStatus("current")
_CfprApSwFcSanBorderFsmStageRn_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmStageRn_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageRn = _CfprApSwFcSanBorderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 3),
    _CfprApSwFcSanBorderFsmStageRn_Type()
)
cfprApSwFcSanBorderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageRn.setStatus("current")
_CfprApSwFcSanBorderFsmStageDescrData_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmStageDescrData_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageDescrData = _CfprApSwFcSanBorderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 4),
    _CfprApSwFcSanBorderFsmStageDescrData_Type()
)
cfprApSwFcSanBorderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageDescrData.setStatus("current")
_CfprApSwFcSanBorderFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwFcSanBorderFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageLastUpdateTime = _CfprApSwFcSanBorderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 5),
    _CfprApSwFcSanBorderFsmStageLastUpdateTime_Type()
)
cfprApSwFcSanBorderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageLastUpdateTime.setStatus("current")
_CfprApSwFcSanBorderFsmStageName_Type = CfprApSwFcSanBorderFsmStageName
_CfprApSwFcSanBorderFsmStageName_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageName = _CfprApSwFcSanBorderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 6),
    _CfprApSwFcSanBorderFsmStageName_Type()
)
cfprApSwFcSanBorderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageName.setStatus("current")
_CfprApSwFcSanBorderFsmStageOrder_Type = Gauge32
_CfprApSwFcSanBorderFsmStageOrder_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageOrder = _CfprApSwFcSanBorderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 7),
    _CfprApSwFcSanBorderFsmStageOrder_Type()
)
cfprApSwFcSanBorderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageOrder.setStatus("current")
_CfprApSwFcSanBorderFsmStageRetry_Type = Gauge32
_CfprApSwFcSanBorderFsmStageRetry_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageRetry = _CfprApSwFcSanBorderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 8),
    _CfprApSwFcSanBorderFsmStageRetry_Type()
)
cfprApSwFcSanBorderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageRetry.setStatus("current")
_CfprApSwFcSanBorderFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwFcSanBorderFsmStageStageStatus_Object = MibTableColumn
cfprApSwFcSanBorderFsmStageStageStatus = _CfprApSwFcSanBorderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 46, 1, 9),
    _CfprApSwFcSanBorderFsmStageStageStatus_Type()
)
cfprApSwFcSanBorderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmStageStageStatus.setStatus("current")
_CfprApSwFcSanBorderFsmTaskTable_Object = MibTable
cfprApSwFcSanBorderFsmTaskTable = _CfprApSwFcSanBorderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47)
)
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskTable.setStatus("current")
_CfprApSwFcSanBorderFsmTaskEntry_Object = MibTableRow
cfprApSwFcSanBorderFsmTaskEntry = _CfprApSwFcSanBorderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47, 1)
)
cfprApSwFcSanBorderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcSanBorderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskEntry.setStatus("current")
_CfprApSwFcSanBorderFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcSanBorderFsmTaskInstanceId_Object = MibTableColumn
cfprApSwFcSanBorderFsmTaskInstanceId = _CfprApSwFcSanBorderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47, 1, 1),
    _CfprApSwFcSanBorderFsmTaskInstanceId_Type()
)
cfprApSwFcSanBorderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskInstanceId.setStatus("current")
_CfprApSwFcSanBorderFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwFcSanBorderFsmTaskDn_Object = MibTableColumn
cfprApSwFcSanBorderFsmTaskDn = _CfprApSwFcSanBorderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47, 1, 2),
    _CfprApSwFcSanBorderFsmTaskDn_Type()
)
cfprApSwFcSanBorderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskDn.setStatus("current")
_CfprApSwFcSanBorderFsmTaskRn_Type = SnmpAdminString
_CfprApSwFcSanBorderFsmTaskRn_Object = MibTableColumn
cfprApSwFcSanBorderFsmTaskRn = _CfprApSwFcSanBorderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47, 1, 3),
    _CfprApSwFcSanBorderFsmTaskRn_Type()
)
cfprApSwFcSanBorderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskRn.setStatus("current")
_CfprApSwFcSanBorderFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwFcSanBorderFsmTaskCompletion_Object = MibTableColumn
cfprApSwFcSanBorderFsmTaskCompletion = _CfprApSwFcSanBorderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47, 1, 4),
    _CfprApSwFcSanBorderFsmTaskCompletion_Type()
)
cfprApSwFcSanBorderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskCompletion.setStatus("current")
_CfprApSwFcSanBorderFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSwFcSanBorderFsmTaskFlags_Object = MibTableColumn
cfprApSwFcSanBorderFsmTaskFlags = _CfprApSwFcSanBorderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47, 1, 5),
    _CfprApSwFcSanBorderFsmTaskFlags_Type()
)
cfprApSwFcSanBorderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskFlags.setStatus("current")
_CfprApSwFcSanBorderFsmTaskItem_Type = CfprApSwFcSanBorderFsmTaskItem
_CfprApSwFcSanBorderFsmTaskItem_Object = MibTableColumn
cfprApSwFcSanBorderFsmTaskItem = _CfprApSwFcSanBorderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47, 1, 6),
    _CfprApSwFcSanBorderFsmTaskItem_Type()
)
cfprApSwFcSanBorderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskItem.setStatus("current")
_CfprApSwFcSanBorderFsmTaskSeqId_Type = Gauge32
_CfprApSwFcSanBorderFsmTaskSeqId_Object = MibTableColumn
cfprApSwFcSanBorderFsmTaskSeqId = _CfprApSwFcSanBorderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 47, 1, 7),
    _CfprApSwFcSanBorderFsmTaskSeqId_Type()
)
cfprApSwFcSanBorderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanBorderFsmTaskSeqId.setStatus("current")
_CfprApSwFcSanEpTable_Object = MibTable
cfprApSwFcSanEpTable = _CfprApSwFcSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48)
)
if mibBuilder.loadTexts:
    cfprApSwFcSanEpTable.setStatus("current")
_CfprApSwFcSanEpEntry_Object = MibTableRow
cfprApSwFcSanEpEntry = _CfprApSwFcSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1)
)
cfprApSwFcSanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcSanEpEntry.setStatus("current")
_CfprApSwFcSanEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcSanEpInstanceId_Object = MibTableColumn
cfprApSwFcSanEpInstanceId = _CfprApSwFcSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 1),
    _CfprApSwFcSanEpInstanceId_Type()
)
cfprApSwFcSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpInstanceId.setStatus("current")
_CfprApSwFcSanEpDn_Type = CfprApManagedObjectDn
_CfprApSwFcSanEpDn_Object = MibTableColumn
cfprApSwFcSanEpDn = _CfprApSwFcSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 2),
    _CfprApSwFcSanEpDn_Type()
)
cfprApSwFcSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpDn.setStatus("current")
_CfprApSwFcSanEpRn_Type = SnmpAdminString
_CfprApSwFcSanEpRn_Object = MibTableColumn
cfprApSwFcSanEpRn = _CfprApSwFcSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 3),
    _CfprApSwFcSanEpRn_Type()
)
cfprApSwFcSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpRn.setStatus("current")
_CfprApSwFcSanEpAdminSpeed_Type = CfprApPortSpeed
_CfprApSwFcSanEpAdminSpeed_Object = MibTableColumn
cfprApSwFcSanEpAdminSpeed = _CfprApSwFcSanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 4),
    _CfprApSwFcSanEpAdminSpeed_Type()
)
cfprApSwFcSanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpAdminSpeed.setStatus("current")
_CfprApSwFcSanEpAdminState_Type = CfprApFabricAdminState
_CfprApSwFcSanEpAdminState_Object = MibTableColumn
cfprApSwFcSanEpAdminState = _CfprApSwFcSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 5),
    _CfprApSwFcSanEpAdminState_Type()
)
cfprApSwFcSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpAdminState.setStatus("current")
_CfprApSwFcSanEpAggrPortId_Type = Gauge32
_CfprApSwFcSanEpAggrPortId_Object = MibTableColumn
cfprApSwFcSanEpAggrPortId = _CfprApSwFcSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 6),
    _CfprApSwFcSanEpAggrPortId_Type()
)
cfprApSwFcSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpAggrPortId.setStatus("current")
_CfprApSwFcSanEpChassisId_Type = Gauge32
_CfprApSwFcSanEpChassisId_Object = MibTableColumn
cfprApSwFcSanEpChassisId = _CfprApSwFcSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 7),
    _CfprApSwFcSanEpChassisId_Type()
)
cfprApSwFcSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpChassisId.setStatus("current")
_CfprApSwFcSanEpEpDn_Type = SnmpAdminString
_CfprApSwFcSanEpEpDn_Object = MibTableColumn
cfprApSwFcSanEpEpDn = _CfprApSwFcSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 8),
    _CfprApSwFcSanEpEpDn_Type()
)
cfprApSwFcSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpEpDn.setStatus("current")
_CfprApSwFcSanEpFillPattern_Type = CfprApFabricFillPattern
_CfprApSwFcSanEpFillPattern_Object = MibTableColumn
cfprApSwFcSanEpFillPattern = _CfprApSwFcSanEpFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 9),
    _CfprApSwFcSanEpFillPattern_Type()
)
cfprApSwFcSanEpFillPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpFillPattern.setStatus("current")
_CfprApSwFcSanEpIfRole_Type = CfprApSwSanEpIfRole
_CfprApSwFcSanEpIfRole_Object = MibTableColumn
cfprApSwFcSanEpIfRole = _CfprApSwFcSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 10),
    _CfprApSwFcSanEpIfRole_Type()
)
cfprApSwFcSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpIfRole.setStatus("current")
_CfprApSwFcSanEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwFcSanEpIfType_Object = MibTableColumn
cfprApSwFcSanEpIfType = _CfprApSwFcSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 11),
    _CfprApSwFcSanEpIfType_Type()
)
cfprApSwFcSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpIfType.setStatus("current")
_CfprApSwFcSanEpLc_Type = CfprApSwPIoEpLc
_CfprApSwFcSanEpLc_Object = MibTableColumn
cfprApSwFcSanEpLc = _CfprApSwFcSanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 12),
    _CfprApSwFcSanEpLc_Type()
)
cfprApSwFcSanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpLc.setStatus("current")
_CfprApSwFcSanEpLocale_Type = CfprApSwBorderEpLocale
_CfprApSwFcSanEpLocale_Object = MibTableColumn
cfprApSwFcSanEpLocale = _CfprApSwFcSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 13),
    _CfprApSwFcSanEpLocale_Type()
)
cfprApSwFcSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpLocale.setStatus("current")
_CfprApSwFcSanEpName_Type = SnmpAdminString
_CfprApSwFcSanEpName_Object = MibTableColumn
cfprApSwFcSanEpName = _CfprApSwFcSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 14),
    _CfprApSwFcSanEpName_Type()
)
cfprApSwFcSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpName.setStatus("current")
_CfprApSwFcSanEpPcId_Type = Gauge32
_CfprApSwFcSanEpPcId_Object = MibTableColumn
cfprApSwFcSanEpPcId = _CfprApSwFcSanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 15),
    _CfprApSwFcSanEpPcId_Type()
)
cfprApSwFcSanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpPcId.setStatus("current")
_CfprApSwFcSanEpPeerAggrPortId_Type = Gauge32
_CfprApSwFcSanEpPeerAggrPortId_Object = MibTableColumn
cfprApSwFcSanEpPeerAggrPortId = _CfprApSwFcSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 16),
    _CfprApSwFcSanEpPeerAggrPortId_Type()
)
cfprApSwFcSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpPeerAggrPortId.setStatus("current")
_CfprApSwFcSanEpPeerChassisId_Type = Gauge32
_CfprApSwFcSanEpPeerChassisId_Object = MibTableColumn
cfprApSwFcSanEpPeerChassisId = _CfprApSwFcSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 17),
    _CfprApSwFcSanEpPeerChassisId_Type()
)
cfprApSwFcSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpPeerChassisId.setStatus("current")
_CfprApSwFcSanEpPeerDn_Type = SnmpAdminString
_CfprApSwFcSanEpPeerDn_Object = MibTableColumn
cfprApSwFcSanEpPeerDn = _CfprApSwFcSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 18),
    _CfprApSwFcSanEpPeerDn_Type()
)
cfprApSwFcSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpPeerDn.setStatus("current")
_CfprApSwFcSanEpPeerPortId_Type = Gauge32
_CfprApSwFcSanEpPeerPortId_Object = MibTableColumn
cfprApSwFcSanEpPeerPortId = _CfprApSwFcSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 19),
    _CfprApSwFcSanEpPeerPortId_Type()
)
cfprApSwFcSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpPeerPortId.setStatus("current")
_CfprApSwFcSanEpPeerSlotId_Type = Gauge32
_CfprApSwFcSanEpPeerSlotId_Object = MibTableColumn
cfprApSwFcSanEpPeerSlotId = _CfprApSwFcSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 20),
    _CfprApSwFcSanEpPeerSlotId_Type()
)
cfprApSwFcSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpPeerSlotId.setStatus("current")
_CfprApSwFcSanEpPortId_Type = Gauge32
_CfprApSwFcSanEpPortId_Object = MibTableColumn
cfprApSwFcSanEpPortId = _CfprApSwFcSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 21),
    _CfprApSwFcSanEpPortId_Type()
)
cfprApSwFcSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpPortId.setStatus("current")
_CfprApSwFcSanEpPortVsanId_Type = Gauge32
_CfprApSwFcSanEpPortVsanId_Object = MibTableColumn
cfprApSwFcSanEpPortVsanId = _CfprApSwFcSanEpPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 22),
    _CfprApSwFcSanEpPortVsanId_Type()
)
cfprApSwFcSanEpPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpPortVsanId.setStatus("current")
_CfprApSwFcSanEpSlotId_Type = Gauge32
_CfprApSwFcSanEpSlotId_Object = MibTableColumn
cfprApSwFcSanEpSlotId = _CfprApSwFcSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 23),
    _CfprApSwFcSanEpSlotId_Type()
)
cfprApSwFcSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpSlotId.setStatus("current")
_CfprApSwFcSanEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwFcSanEpSwitchId_Object = MibTableColumn
cfprApSwFcSanEpSwitchId = _CfprApSwFcSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 24),
    _CfprApSwFcSanEpSwitchId_Type()
)
cfprApSwFcSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpSwitchId.setStatus("current")
_CfprApSwFcSanEpTransport_Type = CfprApSwFcSanEpTransport
_CfprApSwFcSanEpTransport_Object = MibTableColumn
cfprApSwFcSanEpTransport = _CfprApSwFcSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 25),
    _CfprApSwFcSanEpTransport_Type()
)
cfprApSwFcSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpTransport.setStatus("current")
_CfprApSwFcSanEpType_Type = CfprApSwSanEpType
_CfprApSwFcSanEpType_Object = MibTableColumn
cfprApSwFcSanEpType = _CfprApSwFcSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 48, 1, 26),
    _CfprApSwFcSanEpType_Type()
)
cfprApSwFcSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanEpType.setStatus("current")
_CfprApSwFcSanPcTable_Object = MibTable
cfprApSwFcSanPcTable = _CfprApSwFcSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50)
)
if mibBuilder.loadTexts:
    cfprApSwFcSanPcTable.setStatus("current")
_CfprApSwFcSanPcEntry_Object = MibTableRow
cfprApSwFcSanPcEntry = _CfprApSwFcSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1)
)
cfprApSwFcSanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcSanPcEntry.setStatus("current")
_CfprApSwFcSanPcInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcSanPcInstanceId_Object = MibTableColumn
cfprApSwFcSanPcInstanceId = _CfprApSwFcSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 1),
    _CfprApSwFcSanPcInstanceId_Type()
)
cfprApSwFcSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcInstanceId.setStatus("current")
_CfprApSwFcSanPcDn_Type = CfprApManagedObjectDn
_CfprApSwFcSanPcDn_Object = MibTableColumn
cfprApSwFcSanPcDn = _CfprApSwFcSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 2),
    _CfprApSwFcSanPcDn_Type()
)
cfprApSwFcSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcDn.setStatus("current")
_CfprApSwFcSanPcRn_Type = SnmpAdminString
_CfprApSwFcSanPcRn_Object = MibTableColumn
cfprApSwFcSanPcRn = _CfprApSwFcSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 3),
    _CfprApSwFcSanPcRn_Type()
)
cfprApSwFcSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcRn.setStatus("current")
_CfprApSwFcSanPcAdminSpeed_Type = CfprApPortSpeed
_CfprApSwFcSanPcAdminSpeed_Object = MibTableColumn
cfprApSwFcSanPcAdminSpeed = _CfprApSwFcSanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 4),
    _CfprApSwFcSanPcAdminSpeed_Type()
)
cfprApSwFcSanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcAdminSpeed.setStatus("current")
_CfprApSwFcSanPcAdminState_Type = CfprApFabricAdminState
_CfprApSwFcSanPcAdminState_Object = MibTableColumn
cfprApSwFcSanPcAdminState = _CfprApSwFcSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 5),
    _CfprApSwFcSanPcAdminState_Type()
)
cfprApSwFcSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcAdminState.setStatus("current")
_CfprApSwFcSanPcEpDn_Type = SnmpAdminString
_CfprApSwFcSanPcEpDn_Object = MibTableColumn
cfprApSwFcSanPcEpDn = _CfprApSwFcSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 6),
    _CfprApSwFcSanPcEpDn_Type()
)
cfprApSwFcSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcEpDn.setStatus("current")
_CfprApSwFcSanPcIfRole_Type = CfprApSwSanPcIfRole
_CfprApSwFcSanPcIfRole_Object = MibTableColumn
cfprApSwFcSanPcIfRole = _CfprApSwFcSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 7),
    _CfprApSwFcSanPcIfRole_Type()
)
cfprApSwFcSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcIfRole.setStatus("current")
_CfprApSwFcSanPcIfType_Type = CfprApSwCIoEpIfType
_CfprApSwFcSanPcIfType_Object = MibTableColumn
cfprApSwFcSanPcIfType = _CfprApSwFcSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 8),
    _CfprApSwFcSanPcIfType_Type()
)
cfprApSwFcSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcIfType.setStatus("current")
_CfprApSwFcSanPcLocale_Type = CfprApSwBorderPcLocale
_CfprApSwFcSanPcLocale_Object = MibTableColumn
cfprApSwFcSanPcLocale = _CfprApSwFcSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 9),
    _CfprApSwFcSanPcLocale_Type()
)
cfprApSwFcSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcLocale.setStatus("current")
_CfprApSwFcSanPcMonTrafDir_Type = CfprApFabricTrafficDirection
_CfprApSwFcSanPcMonTrafDir_Object = MibTableColumn
cfprApSwFcSanPcMonTrafDir = _CfprApSwFcSanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 10),
    _CfprApSwFcSanPcMonTrafDir_Type()
)
cfprApSwFcSanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcMonTrafDir.setStatus("current")
_CfprApSwFcSanPcName_Type = SnmpAdminString
_CfprApSwFcSanPcName_Object = MibTableColumn
cfprApSwFcSanPcName = _CfprApSwFcSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 11),
    _CfprApSwFcSanPcName_Type()
)
cfprApSwFcSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcName.setStatus("current")
_CfprApSwFcSanPcPcId_Type = Gauge32
_CfprApSwFcSanPcPcId_Object = MibTableColumn
cfprApSwFcSanPcPcId = _CfprApSwFcSanPcPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 12),
    _CfprApSwFcSanPcPcId_Type()
)
cfprApSwFcSanPcPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcPcId.setStatus("current")
_CfprApSwFcSanPcPeerDn_Type = SnmpAdminString
_CfprApSwFcSanPcPeerDn_Object = MibTableColumn
cfprApSwFcSanPcPeerDn = _CfprApSwFcSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 13),
    _CfprApSwFcSanPcPeerDn_Type()
)
cfprApSwFcSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcPeerDn.setStatus("current")
_CfprApSwFcSanPcPortId_Type = Gauge32
_CfprApSwFcSanPcPortId_Object = MibTableColumn
cfprApSwFcSanPcPortId = _CfprApSwFcSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 14),
    _CfprApSwFcSanPcPortId_Type()
)
cfprApSwFcSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcPortId.setStatus("current")
_CfprApSwFcSanPcPortVsanId_Type = Gauge32
_CfprApSwFcSanPcPortVsanId_Object = MibTableColumn
cfprApSwFcSanPcPortVsanId = _CfprApSwFcSanPcPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 15),
    _CfprApSwFcSanPcPortVsanId_Type()
)
cfprApSwFcSanPcPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcPortVsanId.setStatus("current")
_CfprApSwFcSanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwFcSanPcSwitchId_Object = MibTableColumn
cfprApSwFcSanPcSwitchId = _CfprApSwFcSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 16),
    _CfprApSwFcSanPcSwitchId_Type()
)
cfprApSwFcSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcSwitchId.setStatus("current")
_CfprApSwFcSanPcTransport_Type = CfprApSwFcSanPcTransport
_CfprApSwFcSanPcTransport_Object = MibTableColumn
cfprApSwFcSanPcTransport = _CfprApSwFcSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 17),
    _CfprApSwFcSanPcTransport_Type()
)
cfprApSwFcSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcTransport.setStatus("current")
_CfprApSwFcSanPcType_Type = CfprApSwSanPcType
_CfprApSwFcSanPcType_Object = MibTableColumn
cfprApSwFcSanPcType = _CfprApSwFcSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 50, 1, 18),
    _CfprApSwFcSanPcType_Type()
)
cfprApSwFcSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcSanPcType.setStatus("current")
_CfprApSwFcServerZoneGroupTable_Object = MibTable
cfprApSwFcServerZoneGroupTable = _CfprApSwFcServerZoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51)
)
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupTable.setStatus("current")
_CfprApSwFcServerZoneGroupEntry_Object = MibTableRow
cfprApSwFcServerZoneGroupEntry = _CfprApSwFcServerZoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1)
)
cfprApSwFcServerZoneGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcServerZoneGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupEntry.setStatus("current")
_CfprApSwFcServerZoneGroupInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcServerZoneGroupInstanceId_Object = MibTableColumn
cfprApSwFcServerZoneGroupInstanceId = _CfprApSwFcServerZoneGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 1),
    _CfprApSwFcServerZoneGroupInstanceId_Type()
)
cfprApSwFcServerZoneGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupInstanceId.setStatus("current")
_CfprApSwFcServerZoneGroupDn_Type = CfprApManagedObjectDn
_CfprApSwFcServerZoneGroupDn_Object = MibTableColumn
cfprApSwFcServerZoneGroupDn = _CfprApSwFcServerZoneGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 2),
    _CfprApSwFcServerZoneGroupDn_Type()
)
cfprApSwFcServerZoneGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupDn.setStatus("current")
_CfprApSwFcServerZoneGroupRn_Type = SnmpAdminString
_CfprApSwFcServerZoneGroupRn_Object = MibTableColumn
cfprApSwFcServerZoneGroupRn = _CfprApSwFcServerZoneGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 3),
    _CfprApSwFcServerZoneGroupRn_Type()
)
cfprApSwFcServerZoneGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupRn.setStatus("current")
_CfprApSwFcServerZoneGroupEpDn_Type = SnmpAdminString
_CfprApSwFcServerZoneGroupEpDn_Object = MibTableColumn
cfprApSwFcServerZoneGroupEpDn = _CfprApSwFcServerZoneGroupEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 4),
    _CfprApSwFcServerZoneGroupEpDn_Type()
)
cfprApSwFcServerZoneGroupEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupEpDn.setStatus("current")
_CfprApSwFcServerZoneGroupId_Type = Gauge32
_CfprApSwFcServerZoneGroupId_Object = MibTableColumn
cfprApSwFcServerZoneGroupId = _CfprApSwFcServerZoneGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 5),
    _CfprApSwFcServerZoneGroupId_Type()
)
cfprApSwFcServerZoneGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupId.setStatus("current")
_CfprApSwFcServerZoneGroupLc_Type = CfprApSwFcServerZoneGroupLc
_CfprApSwFcServerZoneGroupLc_Object = MibTableColumn
cfprApSwFcServerZoneGroupLc = _CfprApSwFcServerZoneGroupLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 6),
    _CfprApSwFcServerZoneGroupLc_Type()
)
cfprApSwFcServerZoneGroupLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupLc.setStatus("current")
_CfprApSwFcServerZoneGroupName_Type = SnmpAdminString
_CfprApSwFcServerZoneGroupName_Object = MibTableColumn
cfprApSwFcServerZoneGroupName = _CfprApSwFcServerZoneGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 7),
    _CfprApSwFcServerZoneGroupName_Type()
)
cfprApSwFcServerZoneGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupName.setStatus("current")
_CfprApSwFcServerZoneGroupPeerDn_Type = SnmpAdminString
_CfprApSwFcServerZoneGroupPeerDn_Object = MibTableColumn
cfprApSwFcServerZoneGroupPeerDn = _CfprApSwFcServerZoneGroupPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 8),
    _CfprApSwFcServerZoneGroupPeerDn_Type()
)
cfprApSwFcServerZoneGroupPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupPeerDn.setStatus("current")
_CfprApSwFcServerZoneGroupServerDn_Type = SnmpAdminString
_CfprApSwFcServerZoneGroupServerDn_Object = MibTableColumn
cfprApSwFcServerZoneGroupServerDn = _CfprApSwFcServerZoneGroupServerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 51, 1, 9),
    _CfprApSwFcServerZoneGroupServerDn_Type()
)
cfprApSwFcServerZoneGroupServerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcServerZoneGroupServerDn.setStatus("current")
_CfprApSwFcZoneTable_Object = MibTable
cfprApSwFcZoneTable = _CfprApSwFcZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52)
)
if mibBuilder.loadTexts:
    cfprApSwFcZoneTable.setStatus("current")
_CfprApSwFcZoneEntry_Object = MibTableRow
cfprApSwFcZoneEntry = _CfprApSwFcZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1)
)
cfprApSwFcZoneEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcZoneInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcZoneEntry.setStatus("current")
_CfprApSwFcZoneInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcZoneInstanceId_Object = MibTableColumn
cfprApSwFcZoneInstanceId = _CfprApSwFcZoneInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 1),
    _CfprApSwFcZoneInstanceId_Type()
)
cfprApSwFcZoneInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcZoneInstanceId.setStatus("current")
_CfprApSwFcZoneDn_Type = CfprApManagedObjectDn
_CfprApSwFcZoneDn_Object = MibTableColumn
cfprApSwFcZoneDn = _CfprApSwFcZoneDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 2),
    _CfprApSwFcZoneDn_Type()
)
cfprApSwFcZoneDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneDn.setStatus("current")
_CfprApSwFcZoneRn_Type = SnmpAdminString
_CfprApSwFcZoneRn_Object = MibTableColumn
cfprApSwFcZoneRn = _CfprApSwFcZoneRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 3),
    _CfprApSwFcZoneRn_Type()
)
cfprApSwFcZoneRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneRn.setStatus("current")
_CfprApSwFcZoneId_Type = Gauge32
_CfprApSwFcZoneId_Object = MibTableColumn
cfprApSwFcZoneId = _CfprApSwFcZoneId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 4),
    _CfprApSwFcZoneId_Type()
)
cfprApSwFcZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneId.setStatus("current")
_CfprApSwFcZoneIdentity_Type = SnmpAdminString
_CfprApSwFcZoneIdentity_Object = MibTableColumn
cfprApSwFcZoneIdentity = _CfprApSwFcZoneIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 5),
    _CfprApSwFcZoneIdentity_Type()
)
cfprApSwFcZoneIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneIdentity.setStatus("current")
_CfprApSwFcZoneLc_Type = CfprApSwFcZoneLc
_CfprApSwFcZoneLc_Object = MibTableColumn
cfprApSwFcZoneLc = _CfprApSwFcZoneLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 6),
    _CfprApSwFcZoneLc_Type()
)
cfprApSwFcZoneLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneLc.setStatus("current")
_CfprApSwFcZoneName_Type = SnmpAdminString
_CfprApSwFcZoneName_Object = MibTableColumn
cfprApSwFcZoneName = _CfprApSwFcZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 7),
    _CfprApSwFcZoneName_Type()
)
cfprApSwFcZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneName.setStatus("current")
_CfprApSwFcZoneOperState_Type = CfprApLsFcZoneState
_CfprApSwFcZoneOperState_Object = MibTableColumn
cfprApSwFcZoneOperState = _CfprApSwFcZoneOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 8),
    _CfprApSwFcZoneOperState_Type()
)
cfprApSwFcZoneOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneOperState.setStatus("current")
_CfprApSwFcZonePeerDn_Type = SnmpAdminString
_CfprApSwFcZonePeerDn_Object = MibTableColumn
cfprApSwFcZonePeerDn = _CfprApSwFcZonePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 52, 1, 9),
    _CfprApSwFcZonePeerDn_Type()
)
cfprApSwFcZonePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZonePeerDn.setStatus("current")
_CfprApSwFcZoneSetTable_Object = MibTable
cfprApSwFcZoneSetTable = _CfprApSwFcZoneSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53)
)
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetTable.setStatus("current")
_CfprApSwFcZoneSetEntry_Object = MibTableRow
cfprApSwFcZoneSetEntry = _CfprApSwFcZoneSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53, 1)
)
cfprApSwFcZoneSetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcZoneSetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetEntry.setStatus("current")
_CfprApSwFcZoneSetInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcZoneSetInstanceId_Object = MibTableColumn
cfprApSwFcZoneSetInstanceId = _CfprApSwFcZoneSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53, 1, 1),
    _CfprApSwFcZoneSetInstanceId_Type()
)
cfprApSwFcZoneSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetInstanceId.setStatus("current")
_CfprApSwFcZoneSetDn_Type = CfprApManagedObjectDn
_CfprApSwFcZoneSetDn_Object = MibTableColumn
cfprApSwFcZoneSetDn = _CfprApSwFcZoneSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53, 1, 2),
    _CfprApSwFcZoneSetDn_Type()
)
cfprApSwFcZoneSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetDn.setStatus("current")
_CfprApSwFcZoneSetRn_Type = SnmpAdminString
_CfprApSwFcZoneSetRn_Object = MibTableColumn
cfprApSwFcZoneSetRn = _CfprApSwFcZoneSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53, 1, 3),
    _CfprApSwFcZoneSetRn_Type()
)
cfprApSwFcZoneSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetRn.setStatus("current")
_CfprApSwFcZoneSetCurrentZonePrefix_Type = SnmpAdminString
_CfprApSwFcZoneSetCurrentZonePrefix_Object = MibTableColumn
cfprApSwFcZoneSetCurrentZonePrefix = _CfprApSwFcZoneSetCurrentZonePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53, 1, 4),
    _CfprApSwFcZoneSetCurrentZonePrefix_Type()
)
cfprApSwFcZoneSetCurrentZonePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetCurrentZonePrefix.setStatus("current")
_CfprApSwFcZoneSetLc_Type = CfprApSwFcZoneSetLc
_CfprApSwFcZoneSetLc_Object = MibTableColumn
cfprApSwFcZoneSetLc = _CfprApSwFcZoneSetLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53, 1, 5),
    _CfprApSwFcZoneSetLc_Type()
)
cfprApSwFcZoneSetLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetLc.setStatus("current")
_CfprApSwFcZoneSetName_Type = SnmpAdminString
_CfprApSwFcZoneSetName_Object = MibTableColumn
cfprApSwFcZoneSetName = _CfprApSwFcZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53, 1, 6),
    _CfprApSwFcZoneSetName_Type()
)
cfprApSwFcZoneSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetName.setStatus("current")
_CfprApSwFcZoneSetOldZonePrefix_Type = SnmpAdminString
_CfprApSwFcZoneSetOldZonePrefix_Object = MibTableColumn
cfprApSwFcZoneSetOldZonePrefix = _CfprApSwFcZoneSetOldZonePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 53, 1, 7),
    _CfprApSwFcZoneSetOldZonePrefix_Type()
)
cfprApSwFcZoneSetOldZonePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcZoneSetOldZonePrefix.setStatus("current")
_CfprApSwFcoeSanEpTable_Object = MibTable
cfprApSwFcoeSanEpTable = _CfprApSwFcoeSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55)
)
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpTable.setStatus("current")
_CfprApSwFcoeSanEpEntry_Object = MibTableRow
cfprApSwFcoeSanEpEntry = _CfprApSwFcoeSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1)
)
cfprApSwFcoeSanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcoeSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpEntry.setStatus("current")
_CfprApSwFcoeSanEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcoeSanEpInstanceId_Object = MibTableColumn
cfprApSwFcoeSanEpInstanceId = _CfprApSwFcoeSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 1),
    _CfprApSwFcoeSanEpInstanceId_Type()
)
cfprApSwFcoeSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpInstanceId.setStatus("current")
_CfprApSwFcoeSanEpDn_Type = CfprApManagedObjectDn
_CfprApSwFcoeSanEpDn_Object = MibTableColumn
cfprApSwFcoeSanEpDn = _CfprApSwFcoeSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 2),
    _CfprApSwFcoeSanEpDn_Type()
)
cfprApSwFcoeSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpDn.setStatus("current")
_CfprApSwFcoeSanEpRn_Type = SnmpAdminString
_CfprApSwFcoeSanEpRn_Object = MibTableColumn
cfprApSwFcoeSanEpRn = _CfprApSwFcoeSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 3),
    _CfprApSwFcoeSanEpRn_Type()
)
cfprApSwFcoeSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpRn.setStatus("current")
_CfprApSwFcoeSanEpAdminSpeed_Type = CfprApPortSpeed
_CfprApSwFcoeSanEpAdminSpeed_Object = MibTableColumn
cfprApSwFcoeSanEpAdminSpeed = _CfprApSwFcoeSanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 4),
    _CfprApSwFcoeSanEpAdminSpeed_Type()
)
cfprApSwFcoeSanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpAdminSpeed.setStatus("current")
_CfprApSwFcoeSanEpAdminState_Type = CfprApFabricAdminState
_CfprApSwFcoeSanEpAdminState_Object = MibTableColumn
cfprApSwFcoeSanEpAdminState = _CfprApSwFcoeSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 5),
    _CfprApSwFcoeSanEpAdminState_Type()
)
cfprApSwFcoeSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpAdminState.setStatus("current")
_CfprApSwFcoeSanEpAggrPortId_Type = Gauge32
_CfprApSwFcoeSanEpAggrPortId_Object = MibTableColumn
cfprApSwFcoeSanEpAggrPortId = _CfprApSwFcoeSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 6),
    _CfprApSwFcoeSanEpAggrPortId_Type()
)
cfprApSwFcoeSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpAggrPortId.setStatus("current")
_CfprApSwFcoeSanEpChassisId_Type = Gauge32
_CfprApSwFcoeSanEpChassisId_Object = MibTableColumn
cfprApSwFcoeSanEpChassisId = _CfprApSwFcoeSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 7),
    _CfprApSwFcoeSanEpChassisId_Type()
)
cfprApSwFcoeSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpChassisId.setStatus("current")
_CfprApSwFcoeSanEpEpDn_Type = SnmpAdminString
_CfprApSwFcoeSanEpEpDn_Object = MibTableColumn
cfprApSwFcoeSanEpEpDn = _CfprApSwFcoeSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 8),
    _CfprApSwFcoeSanEpEpDn_Type()
)
cfprApSwFcoeSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpEpDn.setStatus("current")
_CfprApSwFcoeSanEpIfRole_Type = CfprApSwSanEpIfRole
_CfprApSwFcoeSanEpIfRole_Object = MibTableColumn
cfprApSwFcoeSanEpIfRole = _CfprApSwFcoeSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 9),
    _CfprApSwFcoeSanEpIfRole_Type()
)
cfprApSwFcoeSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpIfRole.setStatus("current")
_CfprApSwFcoeSanEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwFcoeSanEpIfType_Object = MibTableColumn
cfprApSwFcoeSanEpIfType = _CfprApSwFcoeSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 10),
    _CfprApSwFcoeSanEpIfType_Type()
)
cfprApSwFcoeSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpIfType.setStatus("current")
_CfprApSwFcoeSanEpLc_Type = CfprApSwPIoEpLc
_CfprApSwFcoeSanEpLc_Object = MibTableColumn
cfprApSwFcoeSanEpLc = _CfprApSwFcoeSanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 11),
    _CfprApSwFcoeSanEpLc_Type()
)
cfprApSwFcoeSanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpLc.setStatus("current")
_CfprApSwFcoeSanEpLocale_Type = CfprApSwBorderEpLocale
_CfprApSwFcoeSanEpLocale_Object = MibTableColumn
cfprApSwFcoeSanEpLocale = _CfprApSwFcoeSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 12),
    _CfprApSwFcoeSanEpLocale_Type()
)
cfprApSwFcoeSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpLocale.setStatus("current")
_CfprApSwFcoeSanEpName_Type = SnmpAdminString
_CfprApSwFcoeSanEpName_Object = MibTableColumn
cfprApSwFcoeSanEpName = _CfprApSwFcoeSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 13),
    _CfprApSwFcoeSanEpName_Type()
)
cfprApSwFcoeSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpName.setStatus("current")
_CfprApSwFcoeSanEpPcId_Type = Gauge32
_CfprApSwFcoeSanEpPcId_Object = MibTableColumn
cfprApSwFcoeSanEpPcId = _CfprApSwFcoeSanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 14),
    _CfprApSwFcoeSanEpPcId_Type()
)
cfprApSwFcoeSanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPcId.setStatus("current")
_CfprApSwFcoeSanEpPeerAggrPortId_Type = Gauge32
_CfprApSwFcoeSanEpPeerAggrPortId_Object = MibTableColumn
cfprApSwFcoeSanEpPeerAggrPortId = _CfprApSwFcoeSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 15),
    _CfprApSwFcoeSanEpPeerAggrPortId_Type()
)
cfprApSwFcoeSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPeerAggrPortId.setStatus("current")
_CfprApSwFcoeSanEpPeerChassisId_Type = Gauge32
_CfprApSwFcoeSanEpPeerChassisId_Object = MibTableColumn
cfprApSwFcoeSanEpPeerChassisId = _CfprApSwFcoeSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 16),
    _CfprApSwFcoeSanEpPeerChassisId_Type()
)
cfprApSwFcoeSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPeerChassisId.setStatus("current")
_CfprApSwFcoeSanEpPeerDn_Type = SnmpAdminString
_CfprApSwFcoeSanEpPeerDn_Object = MibTableColumn
cfprApSwFcoeSanEpPeerDn = _CfprApSwFcoeSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 17),
    _CfprApSwFcoeSanEpPeerDn_Type()
)
cfprApSwFcoeSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPeerDn.setStatus("current")
_CfprApSwFcoeSanEpPeerPortId_Type = Gauge32
_CfprApSwFcoeSanEpPeerPortId_Object = MibTableColumn
cfprApSwFcoeSanEpPeerPortId = _CfprApSwFcoeSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 18),
    _CfprApSwFcoeSanEpPeerPortId_Type()
)
cfprApSwFcoeSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPeerPortId.setStatus("current")
_CfprApSwFcoeSanEpPeerSlotId_Type = Gauge32
_CfprApSwFcoeSanEpPeerSlotId_Object = MibTableColumn
cfprApSwFcoeSanEpPeerSlotId = _CfprApSwFcoeSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 19),
    _CfprApSwFcoeSanEpPeerSlotId_Type()
)
cfprApSwFcoeSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPeerSlotId.setStatus("current")
_CfprApSwFcoeSanEpPeerState_Type = CfprApSwPeerStatus
_CfprApSwFcoeSanEpPeerState_Object = MibTableColumn
cfprApSwFcoeSanEpPeerState = _CfprApSwFcoeSanEpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 20),
    _CfprApSwFcoeSanEpPeerState_Type()
)
cfprApSwFcoeSanEpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPeerState.setStatus("current")
_CfprApSwFcoeSanEpPortId_Type = Gauge32
_CfprApSwFcoeSanEpPortId_Object = MibTableColumn
cfprApSwFcoeSanEpPortId = _CfprApSwFcoeSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 21),
    _CfprApSwFcoeSanEpPortId_Type()
)
cfprApSwFcoeSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPortId.setStatus("current")
_CfprApSwFcoeSanEpPortVsanId_Type = Gauge32
_CfprApSwFcoeSanEpPortVsanId_Object = MibTableColumn
cfprApSwFcoeSanEpPortVsanId = _CfprApSwFcoeSanEpPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 22),
    _CfprApSwFcoeSanEpPortVsanId_Type()
)
cfprApSwFcoeSanEpPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpPortVsanId.setStatus("current")
_CfprApSwFcoeSanEpSlotId_Type = Gauge32
_CfprApSwFcoeSanEpSlotId_Object = MibTableColumn
cfprApSwFcoeSanEpSlotId = _CfprApSwFcoeSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 23),
    _CfprApSwFcoeSanEpSlotId_Type()
)
cfprApSwFcoeSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpSlotId.setStatus("current")
_CfprApSwFcoeSanEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwFcoeSanEpSwitchId_Object = MibTableColumn
cfprApSwFcoeSanEpSwitchId = _CfprApSwFcoeSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 24),
    _CfprApSwFcoeSanEpSwitchId_Type()
)
cfprApSwFcoeSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpSwitchId.setStatus("current")
_CfprApSwFcoeSanEpTransport_Type = CfprApSwFcoeSanEpTransport
_CfprApSwFcoeSanEpTransport_Object = MibTableColumn
cfprApSwFcoeSanEpTransport = _CfprApSwFcoeSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 25),
    _CfprApSwFcoeSanEpTransport_Type()
)
cfprApSwFcoeSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpTransport.setStatus("current")
_CfprApSwFcoeSanEpType_Type = CfprApSwSanEpType
_CfprApSwFcoeSanEpType_Object = MibTableColumn
cfprApSwFcoeSanEpType = _CfprApSwFcoeSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 26),
    _CfprApSwFcoeSanEpType_Type()
)
cfprApSwFcoeSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpType.setStatus("current")
_CfprApSwFcoeSanEpUdldAdminState_Type = CfprApSwFcoeSanEpUdldAdminState
_CfprApSwFcoeSanEpUdldAdminState_Object = MibTableColumn
cfprApSwFcoeSanEpUdldAdminState = _CfprApSwFcoeSanEpUdldAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 27),
    _CfprApSwFcoeSanEpUdldAdminState_Type()
)
cfprApSwFcoeSanEpUdldAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpUdldAdminState.setStatus("current")
_CfprApSwFcoeSanEpUdldMode_Type = CfprApSwFcoeSanEpUdldMode
_CfprApSwFcoeSanEpUdldMode_Object = MibTableColumn
cfprApSwFcoeSanEpUdldMode = _CfprApSwFcoeSanEpUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 55, 1, 28),
    _CfprApSwFcoeSanEpUdldMode_Type()
)
cfprApSwFcoeSanEpUdldMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanEpUdldMode.setStatus("current")
_CfprApSwFcoeSanPcTable_Object = MibTable
cfprApSwFcoeSanPcTable = _CfprApSwFcoeSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56)
)
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcTable.setStatus("current")
_CfprApSwFcoeSanPcEntry_Object = MibTableRow
cfprApSwFcoeSanPcEntry = _CfprApSwFcoeSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1)
)
cfprApSwFcoeSanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwFcoeSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcEntry.setStatus("current")
_CfprApSwFcoeSanPcInstanceId_Type = CfprApManagedObjectId
_CfprApSwFcoeSanPcInstanceId_Object = MibTableColumn
cfprApSwFcoeSanPcInstanceId = _CfprApSwFcoeSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 1),
    _CfprApSwFcoeSanPcInstanceId_Type()
)
cfprApSwFcoeSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcInstanceId.setStatus("current")
_CfprApSwFcoeSanPcDn_Type = CfprApManagedObjectDn
_CfprApSwFcoeSanPcDn_Object = MibTableColumn
cfprApSwFcoeSanPcDn = _CfprApSwFcoeSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 2),
    _CfprApSwFcoeSanPcDn_Type()
)
cfprApSwFcoeSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcDn.setStatus("current")
_CfprApSwFcoeSanPcRn_Type = SnmpAdminString
_CfprApSwFcoeSanPcRn_Object = MibTableColumn
cfprApSwFcoeSanPcRn = _CfprApSwFcoeSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 3),
    _CfprApSwFcoeSanPcRn_Type()
)
cfprApSwFcoeSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcRn.setStatus("current")
_CfprApSwFcoeSanPcAdminState_Type = CfprApFabricAdminState
_CfprApSwFcoeSanPcAdminState_Object = MibTableColumn
cfprApSwFcoeSanPcAdminState = _CfprApSwFcoeSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 4),
    _CfprApSwFcoeSanPcAdminState_Type()
)
cfprApSwFcoeSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcAdminState.setStatus("current")
_CfprApSwFcoeSanPcEpDn_Type = SnmpAdminString
_CfprApSwFcoeSanPcEpDn_Object = MibTableColumn
cfprApSwFcoeSanPcEpDn = _CfprApSwFcoeSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 5),
    _CfprApSwFcoeSanPcEpDn_Type()
)
cfprApSwFcoeSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcEpDn.setStatus("current")
_CfprApSwFcoeSanPcIfRole_Type = CfprApSwSanPcIfRole
_CfprApSwFcoeSanPcIfRole_Object = MibTableColumn
cfprApSwFcoeSanPcIfRole = _CfprApSwFcoeSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 6),
    _CfprApSwFcoeSanPcIfRole_Type()
)
cfprApSwFcoeSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcIfRole.setStatus("current")
_CfprApSwFcoeSanPcIfType_Type = CfprApSwCIoEpIfType
_CfprApSwFcoeSanPcIfType_Object = MibTableColumn
cfprApSwFcoeSanPcIfType = _CfprApSwFcoeSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 7),
    _CfprApSwFcoeSanPcIfType_Type()
)
cfprApSwFcoeSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcIfType.setStatus("current")
_CfprApSwFcoeSanPcLacpFastTimer_Type = TruthValue
_CfprApSwFcoeSanPcLacpFastTimer_Object = MibTableColumn
cfprApSwFcoeSanPcLacpFastTimer = _CfprApSwFcoeSanPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 8),
    _CfprApSwFcoeSanPcLacpFastTimer_Type()
)
cfprApSwFcoeSanPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcLacpFastTimer.setStatus("current")
_CfprApSwFcoeSanPcLacpSuspendIndividual_Type = TruthValue
_CfprApSwFcoeSanPcLacpSuspendIndividual_Object = MibTableColumn
cfprApSwFcoeSanPcLacpSuspendIndividual = _CfprApSwFcoeSanPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 9),
    _CfprApSwFcoeSanPcLacpSuspendIndividual_Type()
)
cfprApSwFcoeSanPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcLacpSuspendIndividual.setStatus("current")
_CfprApSwFcoeSanPcLocale_Type = CfprApSwBorderPcLocale
_CfprApSwFcoeSanPcLocale_Object = MibTableColumn
cfprApSwFcoeSanPcLocale = _CfprApSwFcoeSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 10),
    _CfprApSwFcoeSanPcLocale_Type()
)
cfprApSwFcoeSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcLocale.setStatus("current")
_CfprApSwFcoeSanPcMonTrafDir_Type = CfprApFabricTrafficDirection
_CfprApSwFcoeSanPcMonTrafDir_Object = MibTableColumn
cfprApSwFcoeSanPcMonTrafDir = _CfprApSwFcoeSanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 11),
    _CfprApSwFcoeSanPcMonTrafDir_Type()
)
cfprApSwFcoeSanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcMonTrafDir.setStatus("current")
_CfprApSwFcoeSanPcName_Type = SnmpAdminString
_CfprApSwFcoeSanPcName_Object = MibTableColumn
cfprApSwFcoeSanPcName = _CfprApSwFcoeSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 12),
    _CfprApSwFcoeSanPcName_Type()
)
cfprApSwFcoeSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcName.setStatus("current")
_CfprApSwFcoeSanPcPcId_Type = Gauge32
_CfprApSwFcoeSanPcPcId_Object = MibTableColumn
cfprApSwFcoeSanPcPcId = _CfprApSwFcoeSanPcPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 13),
    _CfprApSwFcoeSanPcPcId_Type()
)
cfprApSwFcoeSanPcPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcPcId.setStatus("current")
_CfprApSwFcoeSanPcPeerDn_Type = SnmpAdminString
_CfprApSwFcoeSanPcPeerDn_Object = MibTableColumn
cfprApSwFcoeSanPcPeerDn = _CfprApSwFcoeSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 14),
    _CfprApSwFcoeSanPcPeerDn_Type()
)
cfprApSwFcoeSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcPeerDn.setStatus("current")
_CfprApSwFcoeSanPcPeerState_Type = CfprApSwPeerStatus
_CfprApSwFcoeSanPcPeerState_Object = MibTableColumn
cfprApSwFcoeSanPcPeerState = _CfprApSwFcoeSanPcPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 15),
    _CfprApSwFcoeSanPcPeerState_Type()
)
cfprApSwFcoeSanPcPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcPeerState.setStatus("current")
_CfprApSwFcoeSanPcPortId_Type = Gauge32
_CfprApSwFcoeSanPcPortId_Object = MibTableColumn
cfprApSwFcoeSanPcPortId = _CfprApSwFcoeSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 16),
    _CfprApSwFcoeSanPcPortId_Type()
)
cfprApSwFcoeSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcPortId.setStatus("current")
_CfprApSwFcoeSanPcPortVsanId_Type = Gauge32
_CfprApSwFcoeSanPcPortVsanId_Object = MibTableColumn
cfprApSwFcoeSanPcPortVsanId = _CfprApSwFcoeSanPcPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 17),
    _CfprApSwFcoeSanPcPortVsanId_Type()
)
cfprApSwFcoeSanPcPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcPortVsanId.setStatus("current")
_CfprApSwFcoeSanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwFcoeSanPcSwitchId_Object = MibTableColumn
cfprApSwFcoeSanPcSwitchId = _CfprApSwFcoeSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 18),
    _CfprApSwFcoeSanPcSwitchId_Type()
)
cfprApSwFcoeSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcSwitchId.setStatus("current")
_CfprApSwFcoeSanPcTransport_Type = CfprApSwFcoeSanPcTransport
_CfprApSwFcoeSanPcTransport_Object = MibTableColumn
cfprApSwFcoeSanPcTransport = _CfprApSwFcoeSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 19),
    _CfprApSwFcoeSanPcTransport_Type()
)
cfprApSwFcoeSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcTransport.setStatus("current")
_CfprApSwFcoeSanPcType_Type = CfprApSwSanPcType
_CfprApSwFcoeSanPcType_Object = MibTableColumn
cfprApSwFcoeSanPcType = _CfprApSwFcoeSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 56, 1, 20),
    _CfprApSwFcoeSanPcType_Type()
)
cfprApSwFcoeSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwFcoeSanPcType.setStatus("current")
_CfprApSwPhysTable_Object = MibTable
cfprApSwPhysTable = _CfprApSwPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64)
)
if mibBuilder.loadTexts:
    cfprApSwPhysTable.setStatus("current")
_CfprApSwPhysEntry_Object = MibTableRow
cfprApSwPhysEntry = _CfprApSwPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1)
)
cfprApSwPhysEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwPhysInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwPhysEntry.setStatus("current")
_CfprApSwPhysInstanceId_Type = CfprApManagedObjectId
_CfprApSwPhysInstanceId_Object = MibTableColumn
cfprApSwPhysInstanceId = _CfprApSwPhysInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 1),
    _CfprApSwPhysInstanceId_Type()
)
cfprApSwPhysInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwPhysInstanceId.setStatus("current")
_CfprApSwPhysDn_Type = CfprApManagedObjectDn
_CfprApSwPhysDn_Object = MibTableColumn
cfprApSwPhysDn = _CfprApSwPhysDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 2),
    _CfprApSwPhysDn_Type()
)
cfprApSwPhysDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysDn.setStatus("current")
_CfprApSwPhysRn_Type = SnmpAdminString
_CfprApSwPhysRn_Object = MibTableColumn
cfprApSwPhysRn = _CfprApSwPhysRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 3),
    _CfprApSwPhysRn_Type()
)
cfprApSwPhysRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysRn.setStatus("current")
_CfprApSwPhysConfMode_Type = CfprApSwConfMode
_CfprApSwPhysConfMode_Object = MibTableColumn
cfprApSwPhysConfMode = _CfprApSwPhysConfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 4),
    _CfprApSwPhysConfMode_Type()
)
cfprApSwPhysConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysConfMode.setStatus("current")
_CfprApSwPhysFsmDescr_Type = SnmpAdminString
_CfprApSwPhysFsmDescr_Object = MibTableColumn
cfprApSwPhysFsmDescr = _CfprApSwPhysFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 5),
    _CfprApSwPhysFsmDescr_Type()
)
cfprApSwPhysFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmDescr.setStatus("current")
_CfprApSwPhysFsmPrev_Type = SnmpAdminString
_CfprApSwPhysFsmPrev_Object = MibTableColumn
cfprApSwPhysFsmPrev = _CfprApSwPhysFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 6),
    _CfprApSwPhysFsmPrev_Type()
)
cfprApSwPhysFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmPrev.setStatus("current")
_CfprApSwPhysFsmProgr_Type = Gauge32
_CfprApSwPhysFsmProgr_Object = MibTableColumn
cfprApSwPhysFsmProgr = _CfprApSwPhysFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 7),
    _CfprApSwPhysFsmProgr_Type()
)
cfprApSwPhysFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmProgr.setStatus("current")
_CfprApSwPhysFsmRmtInvErrCode_Type = Gauge32
_CfprApSwPhysFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwPhysFsmRmtInvErrCode = _CfprApSwPhysFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 8),
    _CfprApSwPhysFsmRmtInvErrCode_Type()
)
cfprApSwPhysFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmRmtInvErrCode.setStatus("current")
_CfprApSwPhysFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwPhysFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwPhysFsmRmtInvErrDescr = _CfprApSwPhysFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 9),
    _CfprApSwPhysFsmRmtInvErrDescr_Type()
)
cfprApSwPhysFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmRmtInvErrDescr.setStatus("current")
_CfprApSwPhysFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwPhysFsmRmtInvRslt_Object = MibTableColumn
cfprApSwPhysFsmRmtInvRslt = _CfprApSwPhysFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 10),
    _CfprApSwPhysFsmRmtInvRslt_Type()
)
cfprApSwPhysFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmRmtInvRslt.setStatus("current")
_CfprApSwPhysFsmStageDescr_Type = SnmpAdminString
_CfprApSwPhysFsmStageDescr_Object = MibTableColumn
cfprApSwPhysFsmStageDescr = _CfprApSwPhysFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 11),
    _CfprApSwPhysFsmStageDescr_Type()
)
cfprApSwPhysFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageDescr.setStatus("current")
_CfprApSwPhysFsmStamp_Type = DateAndTime
_CfprApSwPhysFsmStamp_Object = MibTableColumn
cfprApSwPhysFsmStamp = _CfprApSwPhysFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 12),
    _CfprApSwPhysFsmStamp_Type()
)
cfprApSwPhysFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStamp.setStatus("current")
_CfprApSwPhysFsmStatus_Type = SnmpAdminString
_CfprApSwPhysFsmStatus_Object = MibTableColumn
cfprApSwPhysFsmStatus = _CfprApSwPhysFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 13),
    _CfprApSwPhysFsmStatus_Type()
)
cfprApSwPhysFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStatus.setStatus("current")
_CfprApSwPhysFsmTry_Type = Gauge32
_CfprApSwPhysFsmTry_Object = MibTableColumn
cfprApSwPhysFsmTry = _CfprApSwPhysFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 64, 1, 14),
    _CfprApSwPhysFsmTry_Type()
)
cfprApSwPhysFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTry.setStatus("current")
_CfprApSwPhysEtherEpTable_Object = MibTable
cfprApSwPhysEtherEpTable = _CfprApSwPhysEtherEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65)
)
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpTable.setStatus("current")
_CfprApSwPhysEtherEpEntry_Object = MibTableRow
cfprApSwPhysEtherEpEntry = _CfprApSwPhysEtherEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1)
)
cfprApSwPhysEtherEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwPhysEtherEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpEntry.setStatus("current")
_CfprApSwPhysEtherEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwPhysEtherEpInstanceId_Object = MibTableColumn
cfprApSwPhysEtherEpInstanceId = _CfprApSwPhysEtherEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 1),
    _CfprApSwPhysEtherEpInstanceId_Type()
)
cfprApSwPhysEtherEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpInstanceId.setStatus("current")
_CfprApSwPhysEtherEpDn_Type = CfprApManagedObjectDn
_CfprApSwPhysEtherEpDn_Object = MibTableColumn
cfprApSwPhysEtherEpDn = _CfprApSwPhysEtherEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 2),
    _CfprApSwPhysEtherEpDn_Type()
)
cfprApSwPhysEtherEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpDn.setStatus("current")
_CfprApSwPhysEtherEpRn_Type = SnmpAdminString
_CfprApSwPhysEtherEpRn_Object = MibTableColumn
cfprApSwPhysEtherEpRn = _CfprApSwPhysEtherEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 3),
    _CfprApSwPhysEtherEpRn_Type()
)
cfprApSwPhysEtherEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpRn.setStatus("current")
_CfprApSwPhysEtherEpAdminState_Type = CfprApFabricAdminState
_CfprApSwPhysEtherEpAdminState_Object = MibTableColumn
cfprApSwPhysEtherEpAdminState = _CfprApSwPhysEtherEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 4),
    _CfprApSwPhysEtherEpAdminState_Type()
)
cfprApSwPhysEtherEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpAdminState.setStatus("current")
_CfprApSwPhysEtherEpAggrPortId_Type = Gauge32
_CfprApSwPhysEtherEpAggrPortId_Object = MibTableColumn
cfprApSwPhysEtherEpAggrPortId = _CfprApSwPhysEtherEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 5),
    _CfprApSwPhysEtherEpAggrPortId_Type()
)
cfprApSwPhysEtherEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpAggrPortId.setStatus("current")
_CfprApSwPhysEtherEpChassisId_Type = Gauge32
_CfprApSwPhysEtherEpChassisId_Object = MibTableColumn
cfprApSwPhysEtherEpChassisId = _CfprApSwPhysEtherEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 6),
    _CfprApSwPhysEtherEpChassisId_Type()
)
cfprApSwPhysEtherEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpChassisId.setStatus("current")
_CfprApSwPhysEtherEpEpDn_Type = SnmpAdminString
_CfprApSwPhysEtherEpEpDn_Object = MibTableColumn
cfprApSwPhysEtherEpEpDn = _CfprApSwPhysEtherEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 7),
    _CfprApSwPhysEtherEpEpDn_Type()
)
cfprApSwPhysEtherEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpEpDn.setStatus("current")
_CfprApSwPhysEtherEpIfRole_Type = CfprApNetworkPortRole
_CfprApSwPhysEtherEpIfRole_Object = MibTableColumn
cfprApSwPhysEtherEpIfRole = _CfprApSwPhysEtherEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 8),
    _CfprApSwPhysEtherEpIfRole_Type()
)
cfprApSwPhysEtherEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpIfRole.setStatus("current")
_CfprApSwPhysEtherEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwPhysEtherEpIfType_Object = MibTableColumn
cfprApSwPhysEtherEpIfType = _CfprApSwPhysEtherEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 9),
    _CfprApSwPhysEtherEpIfType_Type()
)
cfprApSwPhysEtherEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpIfType.setStatus("current")
_CfprApSwPhysEtherEpLc_Type = CfprApSwPIoEpLc
_CfprApSwPhysEtherEpLc_Object = MibTableColumn
cfprApSwPhysEtherEpLc = _CfprApSwPhysEtherEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 10),
    _CfprApSwPhysEtherEpLc_Type()
)
cfprApSwPhysEtherEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpLc.setStatus("current")
_CfprApSwPhysEtherEpLocale_Type = CfprApNetworkLocale
_CfprApSwPhysEtherEpLocale_Object = MibTableColumn
cfprApSwPhysEtherEpLocale = _CfprApSwPhysEtherEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 11),
    _CfprApSwPhysEtherEpLocale_Type()
)
cfprApSwPhysEtherEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpLocale.setStatus("current")
_CfprApSwPhysEtherEpName_Type = SnmpAdminString
_CfprApSwPhysEtherEpName_Object = MibTableColumn
cfprApSwPhysEtherEpName = _CfprApSwPhysEtherEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 12),
    _CfprApSwPhysEtherEpName_Type()
)
cfprApSwPhysEtherEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpName.setStatus("current")
_CfprApSwPhysEtherEpPeerAggrPortId_Type = Gauge32
_CfprApSwPhysEtherEpPeerAggrPortId_Object = MibTableColumn
cfprApSwPhysEtherEpPeerAggrPortId = _CfprApSwPhysEtherEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 13),
    _CfprApSwPhysEtherEpPeerAggrPortId_Type()
)
cfprApSwPhysEtherEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpPeerAggrPortId.setStatus("current")
_CfprApSwPhysEtherEpPeerChassisId_Type = Gauge32
_CfprApSwPhysEtherEpPeerChassisId_Object = MibTableColumn
cfprApSwPhysEtherEpPeerChassisId = _CfprApSwPhysEtherEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 14),
    _CfprApSwPhysEtherEpPeerChassisId_Type()
)
cfprApSwPhysEtherEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpPeerChassisId.setStatus("current")
_CfprApSwPhysEtherEpPeerDn_Type = SnmpAdminString
_CfprApSwPhysEtherEpPeerDn_Object = MibTableColumn
cfprApSwPhysEtherEpPeerDn = _CfprApSwPhysEtherEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 15),
    _CfprApSwPhysEtherEpPeerDn_Type()
)
cfprApSwPhysEtherEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpPeerDn.setStatus("current")
_CfprApSwPhysEtherEpPeerPortId_Type = Gauge32
_CfprApSwPhysEtherEpPeerPortId_Object = MibTableColumn
cfprApSwPhysEtherEpPeerPortId = _CfprApSwPhysEtherEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 16),
    _CfprApSwPhysEtherEpPeerPortId_Type()
)
cfprApSwPhysEtherEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpPeerPortId.setStatus("current")
_CfprApSwPhysEtherEpPeerSlotId_Type = Gauge32
_CfprApSwPhysEtherEpPeerSlotId_Object = MibTableColumn
cfprApSwPhysEtherEpPeerSlotId = _CfprApSwPhysEtherEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 17),
    _CfprApSwPhysEtherEpPeerSlotId_Type()
)
cfprApSwPhysEtherEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpPeerSlotId.setStatus("current")
_CfprApSwPhysEtherEpPortId_Type = Gauge32
_CfprApSwPhysEtherEpPortId_Object = MibTableColumn
cfprApSwPhysEtherEpPortId = _CfprApSwPhysEtherEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 18),
    _CfprApSwPhysEtherEpPortId_Type()
)
cfprApSwPhysEtherEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpPortId.setStatus("current")
_CfprApSwPhysEtherEpSlotId_Type = Gauge32
_CfprApSwPhysEtherEpSlotId_Object = MibTableColumn
cfprApSwPhysEtherEpSlotId = _CfprApSwPhysEtherEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 19),
    _CfprApSwPhysEtherEpSlotId_Type()
)
cfprApSwPhysEtherEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpSlotId.setStatus("current")
_CfprApSwPhysEtherEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwPhysEtherEpSwitchId_Object = MibTableColumn
cfprApSwPhysEtherEpSwitchId = _CfprApSwPhysEtherEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 20),
    _CfprApSwPhysEtherEpSwitchId_Type()
)
cfprApSwPhysEtherEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpSwitchId.setStatus("current")
_CfprApSwPhysEtherEpTransport_Type = CfprApNetworkTransport
_CfprApSwPhysEtherEpTransport_Object = MibTableColumn
cfprApSwPhysEtherEpTransport = _CfprApSwPhysEtherEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 21),
    _CfprApSwPhysEtherEpTransport_Type()
)
cfprApSwPhysEtherEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpTransport.setStatus("current")
_CfprApSwPhysEtherEpType_Type = CfprApNetworkConnectionType
_CfprApSwPhysEtherEpType_Object = MibTableColumn
cfprApSwPhysEtherEpType = _CfprApSwPhysEtherEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 65, 1, 22),
    _CfprApSwPhysEtherEpType_Type()
)
cfprApSwPhysEtherEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysEtherEpType.setStatus("current")
_CfprApSwPhysFcEpTable_Object = MibTable
cfprApSwPhysFcEpTable = _CfprApSwPhysFcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66)
)
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpTable.setStatus("current")
_CfprApSwPhysFcEpEntry_Object = MibTableRow
cfprApSwPhysFcEpEntry = _CfprApSwPhysFcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1)
)
cfprApSwPhysFcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwPhysFcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpEntry.setStatus("current")
_CfprApSwPhysFcEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwPhysFcEpInstanceId_Object = MibTableColumn
cfprApSwPhysFcEpInstanceId = _CfprApSwPhysFcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 1),
    _CfprApSwPhysFcEpInstanceId_Type()
)
cfprApSwPhysFcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpInstanceId.setStatus("current")
_CfprApSwPhysFcEpDn_Type = CfprApManagedObjectDn
_CfprApSwPhysFcEpDn_Object = MibTableColumn
cfprApSwPhysFcEpDn = _CfprApSwPhysFcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 2),
    _CfprApSwPhysFcEpDn_Type()
)
cfprApSwPhysFcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpDn.setStatus("current")
_CfprApSwPhysFcEpRn_Type = SnmpAdminString
_CfprApSwPhysFcEpRn_Object = MibTableColumn
cfprApSwPhysFcEpRn = _CfprApSwPhysFcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 3),
    _CfprApSwPhysFcEpRn_Type()
)
cfprApSwPhysFcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpRn.setStatus("current")
_CfprApSwPhysFcEpAdminState_Type = CfprApFabricAdminState
_CfprApSwPhysFcEpAdminState_Object = MibTableColumn
cfprApSwPhysFcEpAdminState = _CfprApSwPhysFcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 4),
    _CfprApSwPhysFcEpAdminState_Type()
)
cfprApSwPhysFcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpAdminState.setStatus("current")
_CfprApSwPhysFcEpAggrPortId_Type = Gauge32
_CfprApSwPhysFcEpAggrPortId_Object = MibTableColumn
cfprApSwPhysFcEpAggrPortId = _CfprApSwPhysFcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 5),
    _CfprApSwPhysFcEpAggrPortId_Type()
)
cfprApSwPhysFcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpAggrPortId.setStatus("current")
_CfprApSwPhysFcEpChassisId_Type = Gauge32
_CfprApSwPhysFcEpChassisId_Object = MibTableColumn
cfprApSwPhysFcEpChassisId = _CfprApSwPhysFcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 6),
    _CfprApSwPhysFcEpChassisId_Type()
)
cfprApSwPhysFcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpChassisId.setStatus("current")
_CfprApSwPhysFcEpEpDn_Type = SnmpAdminString
_CfprApSwPhysFcEpEpDn_Object = MibTableColumn
cfprApSwPhysFcEpEpDn = _CfprApSwPhysFcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 7),
    _CfprApSwPhysFcEpEpDn_Type()
)
cfprApSwPhysFcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpEpDn.setStatus("current")
_CfprApSwPhysFcEpIfRole_Type = CfprApNetworkPortRole
_CfprApSwPhysFcEpIfRole_Object = MibTableColumn
cfprApSwPhysFcEpIfRole = _CfprApSwPhysFcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 8),
    _CfprApSwPhysFcEpIfRole_Type()
)
cfprApSwPhysFcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpIfRole.setStatus("current")
_CfprApSwPhysFcEpIfType_Type = CfprApSwPIoEpIfType
_CfprApSwPhysFcEpIfType_Object = MibTableColumn
cfprApSwPhysFcEpIfType = _CfprApSwPhysFcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 9),
    _CfprApSwPhysFcEpIfType_Type()
)
cfprApSwPhysFcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpIfType.setStatus("current")
_CfprApSwPhysFcEpLc_Type = CfprApSwPIoEpLc
_CfprApSwPhysFcEpLc_Object = MibTableColumn
cfprApSwPhysFcEpLc = _CfprApSwPhysFcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 10),
    _CfprApSwPhysFcEpLc_Type()
)
cfprApSwPhysFcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpLc.setStatus("current")
_CfprApSwPhysFcEpLocale_Type = CfprApNetworkLocale
_CfprApSwPhysFcEpLocale_Object = MibTableColumn
cfprApSwPhysFcEpLocale = _CfprApSwPhysFcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 11),
    _CfprApSwPhysFcEpLocale_Type()
)
cfprApSwPhysFcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpLocale.setStatus("current")
_CfprApSwPhysFcEpName_Type = SnmpAdminString
_CfprApSwPhysFcEpName_Object = MibTableColumn
cfprApSwPhysFcEpName = _CfprApSwPhysFcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 12),
    _CfprApSwPhysFcEpName_Type()
)
cfprApSwPhysFcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpName.setStatus("current")
_CfprApSwPhysFcEpPeerAggrPortId_Type = Gauge32
_CfprApSwPhysFcEpPeerAggrPortId_Object = MibTableColumn
cfprApSwPhysFcEpPeerAggrPortId = _CfprApSwPhysFcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 13),
    _CfprApSwPhysFcEpPeerAggrPortId_Type()
)
cfprApSwPhysFcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpPeerAggrPortId.setStatus("current")
_CfprApSwPhysFcEpPeerChassisId_Type = Gauge32
_CfprApSwPhysFcEpPeerChassisId_Object = MibTableColumn
cfprApSwPhysFcEpPeerChassisId = _CfprApSwPhysFcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 14),
    _CfprApSwPhysFcEpPeerChassisId_Type()
)
cfprApSwPhysFcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpPeerChassisId.setStatus("current")
_CfprApSwPhysFcEpPeerDn_Type = SnmpAdminString
_CfprApSwPhysFcEpPeerDn_Object = MibTableColumn
cfprApSwPhysFcEpPeerDn = _CfprApSwPhysFcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 15),
    _CfprApSwPhysFcEpPeerDn_Type()
)
cfprApSwPhysFcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpPeerDn.setStatus("current")
_CfprApSwPhysFcEpPeerPortId_Type = Gauge32
_CfprApSwPhysFcEpPeerPortId_Object = MibTableColumn
cfprApSwPhysFcEpPeerPortId = _CfprApSwPhysFcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 16),
    _CfprApSwPhysFcEpPeerPortId_Type()
)
cfprApSwPhysFcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpPeerPortId.setStatus("current")
_CfprApSwPhysFcEpPeerSlotId_Type = Gauge32
_CfprApSwPhysFcEpPeerSlotId_Object = MibTableColumn
cfprApSwPhysFcEpPeerSlotId = _CfprApSwPhysFcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 17),
    _CfprApSwPhysFcEpPeerSlotId_Type()
)
cfprApSwPhysFcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpPeerSlotId.setStatus("current")
_CfprApSwPhysFcEpPortId_Type = Gauge32
_CfprApSwPhysFcEpPortId_Object = MibTableColumn
cfprApSwPhysFcEpPortId = _CfprApSwPhysFcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 18),
    _CfprApSwPhysFcEpPortId_Type()
)
cfprApSwPhysFcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpPortId.setStatus("current")
_CfprApSwPhysFcEpSlotId_Type = Gauge32
_CfprApSwPhysFcEpSlotId_Object = MibTableColumn
cfprApSwPhysFcEpSlotId = _CfprApSwPhysFcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 19),
    _CfprApSwPhysFcEpSlotId_Type()
)
cfprApSwPhysFcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpSlotId.setStatus("current")
_CfprApSwPhysFcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwPhysFcEpSwitchId_Object = MibTableColumn
cfprApSwPhysFcEpSwitchId = _CfprApSwPhysFcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 20),
    _CfprApSwPhysFcEpSwitchId_Type()
)
cfprApSwPhysFcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpSwitchId.setStatus("current")
_CfprApSwPhysFcEpTransport_Type = CfprApNetworkTransport
_CfprApSwPhysFcEpTransport_Object = MibTableColumn
cfprApSwPhysFcEpTransport = _CfprApSwPhysFcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 21),
    _CfprApSwPhysFcEpTransport_Type()
)
cfprApSwPhysFcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpTransport.setStatus("current")
_CfprApSwPhysFcEpType_Type = CfprApNetworkConnectionType
_CfprApSwPhysFcEpType_Object = MibTableColumn
cfprApSwPhysFcEpType = _CfprApSwPhysFcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 66, 1, 22),
    _CfprApSwPhysFcEpType_Type()
)
cfprApSwPhysFcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFcEpType.setStatus("current")
_CfprApSwPhysFsmTable_Object = MibTable
cfprApSwPhysFsmTable = _CfprApSwPhysFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67)
)
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTable.setStatus("current")
_CfprApSwPhysFsmEntry_Object = MibTableRow
cfprApSwPhysFsmEntry = _CfprApSwPhysFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1)
)
cfprApSwPhysFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwPhysFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwPhysFsmEntry.setStatus("current")
_CfprApSwPhysFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwPhysFsmInstanceId_Object = MibTableColumn
cfprApSwPhysFsmInstanceId = _CfprApSwPhysFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 1),
    _CfprApSwPhysFsmInstanceId_Type()
)
cfprApSwPhysFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmInstanceId.setStatus("current")
_CfprApSwPhysFsmDn_Type = CfprApManagedObjectDn
_CfprApSwPhysFsmDn_Object = MibTableColumn
cfprApSwPhysFsmDn = _CfprApSwPhysFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 2),
    _CfprApSwPhysFsmDn_Type()
)
cfprApSwPhysFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmDn.setStatus("current")
_CfprApSwPhysFsmRn_Type = SnmpAdminString
_CfprApSwPhysFsmRn_Object = MibTableColumn
cfprApSwPhysFsmRn = _CfprApSwPhysFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 3),
    _CfprApSwPhysFsmRn_Type()
)
cfprApSwPhysFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmRn.setStatus("current")
_CfprApSwPhysFsmCompletionTime_Type = DateAndTime
_CfprApSwPhysFsmCompletionTime_Object = MibTableColumn
cfprApSwPhysFsmCompletionTime = _CfprApSwPhysFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 4),
    _CfprApSwPhysFsmCompletionTime_Type()
)
cfprApSwPhysFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmCompletionTime.setStatus("current")
_CfprApSwPhysFsmCurrentFsm_Type = CfprApSwPhysFsmCurrentFsm
_CfprApSwPhysFsmCurrentFsm_Object = MibTableColumn
cfprApSwPhysFsmCurrentFsm = _CfprApSwPhysFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 5),
    _CfprApSwPhysFsmCurrentFsm_Type()
)
cfprApSwPhysFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmCurrentFsm.setStatus("current")
_CfprApSwPhysFsmDescrData_Type = SnmpAdminString
_CfprApSwPhysFsmDescrData_Object = MibTableColumn
cfprApSwPhysFsmDescrData = _CfprApSwPhysFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 6),
    _CfprApSwPhysFsmDescrData_Type()
)
cfprApSwPhysFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmDescrData.setStatus("current")
_CfprApSwPhysFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwPhysFsmFsmStatus_Object = MibTableColumn
cfprApSwPhysFsmFsmStatus = _CfprApSwPhysFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 7),
    _CfprApSwPhysFsmFsmStatus_Type()
)
cfprApSwPhysFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmFsmStatus.setStatus("current")
_CfprApSwPhysFsmProgress_Type = Gauge32
_CfprApSwPhysFsmProgress_Object = MibTableColumn
cfprApSwPhysFsmProgress = _CfprApSwPhysFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 8),
    _CfprApSwPhysFsmProgress_Type()
)
cfprApSwPhysFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmProgress.setStatus("current")
_CfprApSwPhysFsmRmtErrCode_Type = Gauge32
_CfprApSwPhysFsmRmtErrCode_Object = MibTableColumn
cfprApSwPhysFsmRmtErrCode = _CfprApSwPhysFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 9),
    _CfprApSwPhysFsmRmtErrCode_Type()
)
cfprApSwPhysFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmRmtErrCode.setStatus("current")
_CfprApSwPhysFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwPhysFsmRmtErrDescr_Object = MibTableColumn
cfprApSwPhysFsmRmtErrDescr = _CfprApSwPhysFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 10),
    _CfprApSwPhysFsmRmtErrDescr_Type()
)
cfprApSwPhysFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmRmtErrDescr.setStatus("current")
_CfprApSwPhysFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwPhysFsmRmtRslt_Object = MibTableColumn
cfprApSwPhysFsmRmtRslt = _CfprApSwPhysFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 67, 1, 11),
    _CfprApSwPhysFsmRmtRslt_Type()
)
cfprApSwPhysFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmRmtRslt.setStatus("current")
_CfprApSwPhysFsmStageTable_Object = MibTable
cfprApSwPhysFsmStageTable = _CfprApSwPhysFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68)
)
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageTable.setStatus("current")
_CfprApSwPhysFsmStageEntry_Object = MibTableRow
cfprApSwPhysFsmStageEntry = _CfprApSwPhysFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1)
)
cfprApSwPhysFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwPhysFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageEntry.setStatus("current")
_CfprApSwPhysFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwPhysFsmStageInstanceId_Object = MibTableColumn
cfprApSwPhysFsmStageInstanceId = _CfprApSwPhysFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 1),
    _CfprApSwPhysFsmStageInstanceId_Type()
)
cfprApSwPhysFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageInstanceId.setStatus("current")
_CfprApSwPhysFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwPhysFsmStageDn_Object = MibTableColumn
cfprApSwPhysFsmStageDn = _CfprApSwPhysFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 2),
    _CfprApSwPhysFsmStageDn_Type()
)
cfprApSwPhysFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageDn.setStatus("current")
_CfprApSwPhysFsmStageRn_Type = SnmpAdminString
_CfprApSwPhysFsmStageRn_Object = MibTableColumn
cfprApSwPhysFsmStageRn = _CfprApSwPhysFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 3),
    _CfprApSwPhysFsmStageRn_Type()
)
cfprApSwPhysFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageRn.setStatus("current")
_CfprApSwPhysFsmStageDescrData_Type = SnmpAdminString
_CfprApSwPhysFsmStageDescrData_Object = MibTableColumn
cfprApSwPhysFsmStageDescrData = _CfprApSwPhysFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 4),
    _CfprApSwPhysFsmStageDescrData_Type()
)
cfprApSwPhysFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageDescrData.setStatus("current")
_CfprApSwPhysFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwPhysFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwPhysFsmStageLastUpdateTime = _CfprApSwPhysFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 5),
    _CfprApSwPhysFsmStageLastUpdateTime_Type()
)
cfprApSwPhysFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageLastUpdateTime.setStatus("current")
_CfprApSwPhysFsmStageName_Type = CfprApSwPhysFsmStageName
_CfprApSwPhysFsmStageName_Object = MibTableColumn
cfprApSwPhysFsmStageName = _CfprApSwPhysFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 6),
    _CfprApSwPhysFsmStageName_Type()
)
cfprApSwPhysFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageName.setStatus("current")
_CfprApSwPhysFsmStageOrder_Type = Gauge32
_CfprApSwPhysFsmStageOrder_Object = MibTableColumn
cfprApSwPhysFsmStageOrder = _CfprApSwPhysFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 7),
    _CfprApSwPhysFsmStageOrder_Type()
)
cfprApSwPhysFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageOrder.setStatus("current")
_CfprApSwPhysFsmStageRetry_Type = Gauge32
_CfprApSwPhysFsmStageRetry_Object = MibTableColumn
cfprApSwPhysFsmStageRetry = _CfprApSwPhysFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 8),
    _CfprApSwPhysFsmStageRetry_Type()
)
cfprApSwPhysFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageRetry.setStatus("current")
_CfprApSwPhysFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwPhysFsmStageStageStatus_Object = MibTableColumn
cfprApSwPhysFsmStageStageStatus = _CfprApSwPhysFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 68, 1, 9),
    _CfprApSwPhysFsmStageStageStatus_Type()
)
cfprApSwPhysFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmStageStageStatus.setStatus("current")
_CfprApSwPhysFsmTaskTable_Object = MibTable
cfprApSwPhysFsmTaskTable = _CfprApSwPhysFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69)
)
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskTable.setStatus("current")
_CfprApSwPhysFsmTaskEntry_Object = MibTableRow
cfprApSwPhysFsmTaskEntry = _CfprApSwPhysFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69, 1)
)
cfprApSwPhysFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwPhysFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskEntry.setStatus("current")
_CfprApSwPhysFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwPhysFsmTaskInstanceId_Object = MibTableColumn
cfprApSwPhysFsmTaskInstanceId = _CfprApSwPhysFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69, 1, 1),
    _CfprApSwPhysFsmTaskInstanceId_Type()
)
cfprApSwPhysFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskInstanceId.setStatus("current")
_CfprApSwPhysFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwPhysFsmTaskDn_Object = MibTableColumn
cfprApSwPhysFsmTaskDn = _CfprApSwPhysFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69, 1, 2),
    _CfprApSwPhysFsmTaskDn_Type()
)
cfprApSwPhysFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskDn.setStatus("current")
_CfprApSwPhysFsmTaskRn_Type = SnmpAdminString
_CfprApSwPhysFsmTaskRn_Object = MibTableColumn
cfprApSwPhysFsmTaskRn = _CfprApSwPhysFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69, 1, 3),
    _CfprApSwPhysFsmTaskRn_Type()
)
cfprApSwPhysFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskRn.setStatus("current")
_CfprApSwPhysFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwPhysFsmTaskCompletion_Object = MibTableColumn
cfprApSwPhysFsmTaskCompletion = _CfprApSwPhysFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69, 1, 4),
    _CfprApSwPhysFsmTaskCompletion_Type()
)
cfprApSwPhysFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskCompletion.setStatus("current")
_CfprApSwPhysFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSwPhysFsmTaskFlags_Object = MibTableColumn
cfprApSwPhysFsmTaskFlags = _CfprApSwPhysFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69, 1, 5),
    _CfprApSwPhysFsmTaskFlags_Type()
)
cfprApSwPhysFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskFlags.setStatus("current")
_CfprApSwPhysFsmTaskItem_Type = CfprApSwPhysFsmTaskItem
_CfprApSwPhysFsmTaskItem_Object = MibTableColumn
cfprApSwPhysFsmTaskItem = _CfprApSwPhysFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69, 1, 6),
    _CfprApSwPhysFsmTaskItem_Type()
)
cfprApSwPhysFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskItem.setStatus("current")
_CfprApSwPhysFsmTaskSeqId_Type = Gauge32
_CfprApSwPhysFsmTaskSeqId_Object = MibTableColumn
cfprApSwPhysFsmTaskSeqId = _CfprApSwPhysFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 69, 1, 7),
    _CfprApSwPhysFsmTaskSeqId_Type()
)
cfprApSwPhysFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPhysFsmTaskSeqId.setStatus("current")
_CfprApSwPortBreakoutTable_Object = MibTable
cfprApSwPortBreakoutTable = _CfprApSwPortBreakoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 70)
)
if mibBuilder.loadTexts:
    cfprApSwPortBreakoutTable.setStatus("current")
_CfprApSwPortBreakoutEntry_Object = MibTableRow
cfprApSwPortBreakoutEntry = _CfprApSwPortBreakoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 70, 1)
)
cfprApSwPortBreakoutEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwPortBreakoutInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwPortBreakoutEntry.setStatus("current")
_CfprApSwPortBreakoutInstanceId_Type = CfprApManagedObjectId
_CfprApSwPortBreakoutInstanceId_Object = MibTableColumn
cfprApSwPortBreakoutInstanceId = _CfprApSwPortBreakoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 70, 1, 1),
    _CfprApSwPortBreakoutInstanceId_Type()
)
cfprApSwPortBreakoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwPortBreakoutInstanceId.setStatus("current")
_CfprApSwPortBreakoutDn_Type = CfprApManagedObjectDn
_CfprApSwPortBreakoutDn_Object = MibTableColumn
cfprApSwPortBreakoutDn = _CfprApSwPortBreakoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 70, 1, 2),
    _CfprApSwPortBreakoutDn_Type()
)
cfprApSwPortBreakoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPortBreakoutDn.setStatus("current")
_CfprApSwPortBreakoutRn_Type = SnmpAdminString
_CfprApSwPortBreakoutRn_Object = MibTableColumn
cfprApSwPortBreakoutRn = _CfprApSwPortBreakoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 70, 1, 3),
    _CfprApSwPortBreakoutRn_Type()
)
cfprApSwPortBreakoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPortBreakoutRn.setStatus("current")
_CfprApSwPortBreakoutBreakoutType_Type = CfprApSwBreakoutType
_CfprApSwPortBreakoutBreakoutType_Object = MibTableColumn
cfprApSwPortBreakoutBreakoutType = _CfprApSwPortBreakoutBreakoutType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 70, 1, 4),
    _CfprApSwPortBreakoutBreakoutType_Type()
)
cfprApSwPortBreakoutBreakoutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPortBreakoutBreakoutType.setStatus("current")
_CfprApSwPortBreakoutPortId_Type = CfprApSwPortBreakoutPortId
_CfprApSwPortBreakoutPortId_Object = MibTableColumn
cfprApSwPortBreakoutPortId = _CfprApSwPortBreakoutPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 70, 1, 5),
    _CfprApSwPortBreakoutPortId_Type()
)
cfprApSwPortBreakoutPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPortBreakoutPortId.setStatus("current")
_CfprApSwPortBreakoutSlotId_Type = CfprApSwPortBreakoutSlotId
_CfprApSwPortBreakoutSlotId_Object = MibTableColumn
cfprApSwPortBreakoutSlotId = _CfprApSwPortBreakoutSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 70, 1, 6),
    _CfprApSwPortBreakoutSlotId_Type()
)
cfprApSwPortBreakoutSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwPortBreakoutSlotId.setStatus("current")
_CfprApSwSspEthLanMonTable_Object = MibTable
cfprApSwSspEthLanMonTable = _CfprApSwSspEthLanMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonTable.setStatus("current")
_CfprApSwSspEthLanMonEntry_Object = MibTableRow
cfprApSwSspEthLanMonEntry = _CfprApSwSspEthLanMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1)
)
cfprApSwSspEthLanMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthLanMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonEntry.setStatus("current")
_CfprApSwSspEthLanMonInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthLanMonInstanceId_Object = MibTableColumn
cfprApSwSspEthLanMonInstanceId = _CfprApSwSspEthLanMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1, 1),
    _CfprApSwSspEthLanMonInstanceId_Type()
)
cfprApSwSspEthLanMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonInstanceId.setStatus("current")
_CfprApSwSspEthLanMonDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthLanMonDn_Object = MibTableColumn
cfprApSwSspEthLanMonDn = _CfprApSwSspEthLanMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1, 2),
    _CfprApSwSspEthLanMonDn_Type()
)
cfprApSwSspEthLanMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonDn.setStatus("current")
_CfprApSwSspEthLanMonRn_Type = SnmpAdminString
_CfprApSwSspEthLanMonRn_Object = MibTableColumn
cfprApSwSspEthLanMonRn = _CfprApSwSspEthLanMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1, 3),
    _CfprApSwSspEthLanMonRn_Type()
)
cfprApSwSspEthLanMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonRn.setStatus("current")
_CfprApSwSspEthLanMonLocale_Type = CfprApSwSspMonDomainLocale
_CfprApSwSspEthLanMonLocale_Object = MibTableColumn
cfprApSwSspEthLanMonLocale = _CfprApSwSspEthLanMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1, 4),
    _CfprApSwSspEthLanMonLocale_Type()
)
cfprApSwSspEthLanMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonLocale.setStatus("current")
_CfprApSwSspEthLanMonName_Type = SnmpAdminString
_CfprApSwSspEthLanMonName_Object = MibTableColumn
cfprApSwSspEthLanMonName = _CfprApSwSspEthLanMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1, 5),
    _CfprApSwSspEthLanMonName_Type()
)
cfprApSwSspEthLanMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonName.setStatus("current")
_CfprApSwSspEthLanMonSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwSspEthLanMonSwitchId_Object = MibTableColumn
cfprApSwSspEthLanMonSwitchId = _CfprApSwSspEthLanMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1, 6),
    _CfprApSwSspEthLanMonSwitchId_Type()
)
cfprApSwSspEthLanMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonSwitchId.setStatus("current")
_CfprApSwSspEthLanMonTransport_Type = CfprApSwSspEthLanMonTransport
_CfprApSwSspEthLanMonTransport_Object = MibTableColumn
cfprApSwSspEthLanMonTransport = _CfprApSwSspEthLanMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1, 7),
    _CfprApSwSspEthLanMonTransport_Type()
)
cfprApSwSspEthLanMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonTransport.setStatus("current")
_CfprApSwSspEthLanMonType_Type = CfprApSwSspLanMonType
_CfprApSwSspEthLanMonType_Object = MibTableColumn
cfprApSwSspEthLanMonType = _CfprApSwSspEthLanMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 71, 1, 8),
    _CfprApSwSspEthLanMonType_Type()
)
cfprApSwSspEthLanMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthLanMonType.setStatus("current")
_CfprApSwSspEthMonTable_Object = MibTable
cfprApSwSspEthMonTable = _CfprApSwSspEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonTable.setStatus("current")
_CfprApSwSspEthMonEntry_Object = MibTableRow
cfprApSwSspEthMonEntry = _CfprApSwSspEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1)
)
cfprApSwSspEthMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonEntry.setStatus("current")
_CfprApSwSspEthMonInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonInstanceId_Object = MibTableColumn
cfprApSwSspEthMonInstanceId = _CfprApSwSspEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 1),
    _CfprApSwSspEthMonInstanceId_Type()
)
cfprApSwSspEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonInstanceId.setStatus("current")
_CfprApSwSspEthMonDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonDn_Object = MibTableColumn
cfprApSwSspEthMonDn = _CfprApSwSspEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 2),
    _CfprApSwSspEthMonDn_Type()
)
cfprApSwSspEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonDn.setStatus("current")
_CfprApSwSspEthMonRn_Type = SnmpAdminString
_CfprApSwSspEthMonRn_Object = MibTableColumn
cfprApSwSspEthMonRn = _CfprApSwSspEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 3),
    _CfprApSwSspEthMonRn_Type()
)
cfprApSwSspEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonRn.setStatus("current")
_CfprApSwSspEthMonAdminState_Type = CfprApSwSspMonAdminState
_CfprApSwSspEthMonAdminState_Object = MibTableColumn
cfprApSwSspEthMonAdminState = _CfprApSwSspEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 4),
    _CfprApSwSspEthMonAdminState_Type()
)
cfprApSwSspEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonAdminState.setStatus("current")
_CfprApSwSspEthMonAppendFlag_Type = CfprApFabricPktCaptureAppendFlag
_CfprApSwSspEthMonAppendFlag_Object = MibTableColumn
cfprApSwSspEthMonAppendFlag = _CfprApSwSspEthMonAppendFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 5),
    _CfprApSwSspEthMonAppendFlag_Type()
)
cfprApSwSspEthMonAppendFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonAppendFlag.setStatus("current")
_CfprApSwSspEthMonDelPcap_Type = CfprApSwSspMonDelPcap
_CfprApSwSspEthMonDelPcap_Object = MibTableColumn
cfprApSwSspEthMonDelPcap = _CfprApSwSspEthMonDelPcap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 6),
    _CfprApSwSspEthMonDelPcap_Type()
)
cfprApSwSspEthMonDelPcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonDelPcap.setStatus("current")
_CfprApSwSspEthMonFsmDescr_Type = SnmpAdminString
_CfprApSwSspEthMonFsmDescr_Object = MibTableColumn
cfprApSwSspEthMonFsmDescr = _CfprApSwSspEthMonFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 7),
    _CfprApSwSspEthMonFsmDescr_Type()
)
cfprApSwSspEthMonFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmDescr.setStatus("current")
_CfprApSwSspEthMonFsmPrev_Type = SnmpAdminString
_CfprApSwSspEthMonFsmPrev_Object = MibTableColumn
cfprApSwSspEthMonFsmPrev = _CfprApSwSspEthMonFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 8),
    _CfprApSwSspEthMonFsmPrev_Type()
)
cfprApSwSspEthMonFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmPrev.setStatus("current")
_CfprApSwSspEthMonFsmProgr_Type = Gauge32
_CfprApSwSspEthMonFsmProgr_Object = MibTableColumn
cfprApSwSspEthMonFsmProgr = _CfprApSwSspEthMonFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 9),
    _CfprApSwSspEthMonFsmProgr_Type()
)
cfprApSwSspEthMonFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmProgr.setStatus("current")
_CfprApSwSspEthMonFsmRmtInvErrCode_Type = Gauge32
_CfprApSwSspEthMonFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwSspEthMonFsmRmtInvErrCode = _CfprApSwSspEthMonFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 10),
    _CfprApSwSspEthMonFsmRmtInvErrCode_Type()
)
cfprApSwSspEthMonFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmRmtInvErrCode.setStatus("current")
_CfprApSwSspEthMonFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwSspEthMonFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwSspEthMonFsmRmtInvErrDescr = _CfprApSwSspEthMonFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 11),
    _CfprApSwSspEthMonFsmRmtInvErrDescr_Type()
)
cfprApSwSspEthMonFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmRmtInvErrDescr.setStatus("current")
_CfprApSwSspEthMonFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwSspEthMonFsmRmtInvRslt_Object = MibTableColumn
cfprApSwSspEthMonFsmRmtInvRslt = _CfprApSwSspEthMonFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 12),
    _CfprApSwSspEthMonFsmRmtInvRslt_Type()
)
cfprApSwSspEthMonFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmRmtInvRslt.setStatus("current")
_CfprApSwSspEthMonFsmStageDescr_Type = SnmpAdminString
_CfprApSwSspEthMonFsmStageDescr_Object = MibTableColumn
cfprApSwSspEthMonFsmStageDescr = _CfprApSwSspEthMonFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 13),
    _CfprApSwSspEthMonFsmStageDescr_Type()
)
cfprApSwSspEthMonFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageDescr.setStatus("current")
_CfprApSwSspEthMonFsmStamp_Type = DateAndTime
_CfprApSwSspEthMonFsmStamp_Object = MibTableColumn
cfprApSwSspEthMonFsmStamp = _CfprApSwSspEthMonFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 14),
    _CfprApSwSspEthMonFsmStamp_Type()
)
cfprApSwSspEthMonFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStamp.setStatus("current")
_CfprApSwSspEthMonFsmStatus_Type = SnmpAdminString
_CfprApSwSspEthMonFsmStatus_Object = MibTableColumn
cfprApSwSspEthMonFsmStatus = _CfprApSwSspEthMonFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 15),
    _CfprApSwSspEthMonFsmStatus_Type()
)
cfprApSwSspEthMonFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStatus.setStatus("current")
_CfprApSwSspEthMonFsmTry_Type = Gauge32
_CfprApSwSspEthMonFsmTry_Object = MibTableColumn
cfprApSwSspEthMonFsmTry = _CfprApSwSspEthMonFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 16),
    _CfprApSwSspEthMonFsmTry_Type()
)
cfprApSwSspEthMonFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTry.setStatus("current")
_CfprApSwSspEthMonLifeCycle_Type = CfprApSwPktCaptureLifeCycle
_CfprApSwSspEthMonLifeCycle_Object = MibTableColumn
cfprApSwSspEthMonLifeCycle = _CfprApSwSspEthMonLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 17),
    _CfprApSwSspEthMonLifeCycle_Type()
)
cfprApSwSspEthMonLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonLifeCycle.setStatus("current")
_CfprApSwSspEthMonName_Type = SnmpAdminString
_CfprApSwSspEthMonName_Object = MibTableColumn
cfprApSwSspEthMonName = _CfprApSwSspEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 18),
    _CfprApSwSspEthMonName_Type()
)
cfprApSwSspEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonName.setStatus("current")
_CfprApSwSspEthMonPeerDn_Type = SnmpAdminString
_CfprApSwSspEthMonPeerDn_Object = MibTableColumn
cfprApSwSspEthMonPeerDn = _CfprApSwSspEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 19),
    _CfprApSwSspEthMonPeerDn_Type()
)
cfprApSwSspEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonPeerDn.setStatus("current")
_CfprApSwSspEthMonSession_Type = Gauge32
_CfprApSwSspEthMonSession_Object = MibTableColumn
cfprApSwSspEthMonSession = _CfprApSwSspEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 20),
    _CfprApSwSspEthMonSession_Type()
)
cfprApSwSspEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSession.setStatus("current")
_CfprApSwSspEthMonSessionMemUsage_Type = Unsigned64
_CfprApSwSspEthMonSessionMemUsage_Object = MibTableColumn
cfprApSwSspEthMonSessionMemUsage = _CfprApSwSspEthMonSessionMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 21),
    _CfprApSwSspEthMonSessionMemUsage_Type()
)
cfprApSwSspEthMonSessionMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSessionMemUsage.setStatus("current")
_CfprApSwSspEthMonSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwSspEthMonSwitchId_Object = MibTableColumn
cfprApSwSspEthMonSwitchId = _CfprApSwSspEthMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 22),
    _CfprApSwSspEthMonSwitchId_Type()
)
cfprApSwSspEthMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSwitchId.setStatus("current")
_CfprApSwSspEthMonTransport_Type = CfprApSwSspEthMonTransport
_CfprApSwSspEthMonTransport_Object = MibTableColumn
cfprApSwSspEthMonTransport = _CfprApSwSspEthMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 23),
    _CfprApSwSspEthMonTransport_Type()
)
cfprApSwSspEthMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonTransport.setStatus("current")
_CfprApSwSspEthMonType_Type = CfprApSwSspEthMonType
_CfprApSwSspEthMonType_Object = MibTableColumn
cfprApSwSspEthMonType = _CfprApSwSspEthMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 72, 1, 24),
    _CfprApSwSspEthMonType_Type()
)
cfprApSwSspEthMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonType.setStatus("current")
_CfprApSwSspEthMonFilterEpTable_Object = MibTable
cfprApSwSspEthMonFilterEpTable = _CfprApSwSspEthMonFilterEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpTable.setStatus("current")
_CfprApSwSspEthMonFilterEpEntry_Object = MibTableRow
cfprApSwSspEthMonFilterEpEntry = _CfprApSwSspEthMonFilterEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1)
)
cfprApSwSspEthMonFilterEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonFilterEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpEntry.setStatus("current")
_CfprApSwSspEthMonFilterEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonFilterEpInstanceId_Object = MibTableColumn
cfprApSwSspEthMonFilterEpInstanceId = _CfprApSwSspEthMonFilterEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 1),
    _CfprApSwSspEthMonFilterEpInstanceId_Type()
)
cfprApSwSspEthMonFilterEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpInstanceId.setStatus("current")
_CfprApSwSspEthMonFilterEpDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonFilterEpDn_Object = MibTableColumn
cfprApSwSspEthMonFilterEpDn = _CfprApSwSspEthMonFilterEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 2),
    _CfprApSwSspEthMonFilterEpDn_Type()
)
cfprApSwSspEthMonFilterEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpDn.setStatus("current")
_CfprApSwSspEthMonFilterEpRn_Type = SnmpAdminString
_CfprApSwSspEthMonFilterEpRn_Object = MibTableColumn
cfprApSwSspEthMonFilterEpRn = _CfprApSwSspEthMonFilterEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 3),
    _CfprApSwSspEthMonFilterEpRn_Type()
)
cfprApSwSspEthMonFilterEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpRn.setStatus("current")
_CfprApSwSspEthMonFilterEpDestIp_Type = InetAddressIPv4
_CfprApSwSspEthMonFilterEpDestIp_Object = MibTableColumn
cfprApSwSspEthMonFilterEpDestIp = _CfprApSwSspEthMonFilterEpDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 4),
    _CfprApSwSspEthMonFilterEpDestIp_Type()
)
cfprApSwSspEthMonFilterEpDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpDestIp.setStatus("current")
_CfprApSwSspEthMonFilterEpDestMAC_Type = MacAddress
_CfprApSwSspEthMonFilterEpDestMAC_Object = MibTableColumn
cfprApSwSspEthMonFilterEpDestMAC = _CfprApSwSspEthMonFilterEpDestMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 5),
    _CfprApSwSspEthMonFilterEpDestMAC_Type()
)
cfprApSwSspEthMonFilterEpDestMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpDestMAC.setStatus("current")
_CfprApSwSspEthMonFilterEpDestPort_Type = CfprApFabricPort
_CfprApSwSspEthMonFilterEpDestPort_Object = MibTableColumn
cfprApSwSspEthMonFilterEpDestPort = _CfprApSwSspEthMonFilterEpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 6),
    _CfprApSwSspEthMonFilterEpDestPort_Type()
)
cfprApSwSspEthMonFilterEpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpDestPort.setStatus("current")
_CfprApSwSspEthMonFilterEpEthertype_Type = Gauge32
_CfprApSwSspEthMonFilterEpEthertype_Object = MibTableColumn
cfprApSwSspEthMonFilterEpEthertype = _CfprApSwSspEthMonFilterEpEthertype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 7),
    _CfprApSwSspEthMonFilterEpEthertype_Type()
)
cfprApSwSspEthMonFilterEpEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpEthertype.setStatus("current")
_CfprApSwSspEthMonFilterEpFilterFlag_Type = Gauge32
_CfprApSwSspEthMonFilterEpFilterFlag_Object = MibTableColumn
cfprApSwSspEthMonFilterEpFilterFlag = _CfprApSwSspEthMonFilterEpFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 8),
    _CfprApSwSspEthMonFilterEpFilterFlag_Type()
)
cfprApSwSspEthMonFilterEpFilterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpFilterFlag.setStatus("current")
_CfprApSwSspEthMonFilterEpIvlan_Type = Gauge32
_CfprApSwSspEthMonFilterEpIvlan_Object = MibTableColumn
cfprApSwSspEthMonFilterEpIvlan = _CfprApSwSspEthMonFilterEpIvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 9),
    _CfprApSwSspEthMonFilterEpIvlan_Type()
)
cfprApSwSspEthMonFilterEpIvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpIvlan.setStatus("current")
_CfprApSwSspEthMonFilterEpLifeCycle_Type = CfprApSwPktCaptureLifeCycle
_CfprApSwSspEthMonFilterEpLifeCycle_Object = MibTableColumn
cfprApSwSspEthMonFilterEpLifeCycle = _CfprApSwSspEthMonFilterEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 10),
    _CfprApSwSspEthMonFilterEpLifeCycle_Type()
)
cfprApSwSspEthMonFilterEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpLifeCycle.setStatus("current")
_CfprApSwSspEthMonFilterEpNameId_Type = SnmpAdminString
_CfprApSwSspEthMonFilterEpNameId_Object = MibTableColumn
cfprApSwSspEthMonFilterEpNameId = _CfprApSwSspEthMonFilterEpNameId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 11),
    _CfprApSwSspEthMonFilterEpNameId_Type()
)
cfprApSwSspEthMonFilterEpNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpNameId.setStatus("current")
_CfprApSwSspEthMonFilterEpOvlan_Type = Gauge32
_CfprApSwSspEthMonFilterEpOvlan_Object = MibTableColumn
cfprApSwSspEthMonFilterEpOvlan = _CfprApSwSspEthMonFilterEpOvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 12),
    _CfprApSwSspEthMonFilterEpOvlan_Type()
)
cfprApSwSspEthMonFilterEpOvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpOvlan.setStatus("current")
_CfprApSwSspEthMonFilterEpPeerDn_Type = SnmpAdminString
_CfprApSwSspEthMonFilterEpPeerDn_Object = MibTableColumn
cfprApSwSspEthMonFilterEpPeerDn = _CfprApSwSspEthMonFilterEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 13),
    _CfprApSwSspEthMonFilterEpPeerDn_Type()
)
cfprApSwSspEthMonFilterEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpPeerDn.setStatus("current")
_CfprApSwSspEthMonFilterEpProtocol_Type = Gauge32
_CfprApSwSspEthMonFilterEpProtocol_Object = MibTableColumn
cfprApSwSspEthMonFilterEpProtocol = _CfprApSwSspEthMonFilterEpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 14),
    _CfprApSwSspEthMonFilterEpProtocol_Type()
)
cfprApSwSspEthMonFilterEpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpProtocol.setStatus("current")
_CfprApSwSspEthMonFilterEpRefCount_Type = Gauge32
_CfprApSwSspEthMonFilterEpRefCount_Object = MibTableColumn
cfprApSwSspEthMonFilterEpRefCount = _CfprApSwSspEthMonFilterEpRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 15),
    _CfprApSwSspEthMonFilterEpRefCount_Type()
)
cfprApSwSspEthMonFilterEpRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpRefCount.setStatus("current")
_CfprApSwSspEthMonFilterEpSrcIp_Type = InetAddressIPv4
_CfprApSwSspEthMonFilterEpSrcIp_Object = MibTableColumn
cfprApSwSspEthMonFilterEpSrcIp = _CfprApSwSspEthMonFilterEpSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 16),
    _CfprApSwSspEthMonFilterEpSrcIp_Type()
)
cfprApSwSspEthMonFilterEpSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpSrcIp.setStatus("current")
_CfprApSwSspEthMonFilterEpSrcMAC_Type = MacAddress
_CfprApSwSspEthMonFilterEpSrcMAC_Object = MibTableColumn
cfprApSwSspEthMonFilterEpSrcMAC = _CfprApSwSspEthMonFilterEpSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 17),
    _CfprApSwSspEthMonFilterEpSrcMAC_Type()
)
cfprApSwSspEthMonFilterEpSrcMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpSrcMAC.setStatus("current")
_CfprApSwSspEthMonFilterEpSrcPort_Type = CfprApFabricPort
_CfprApSwSspEthMonFilterEpSrcPort_Object = MibTableColumn
cfprApSwSspEthMonFilterEpSrcPort = _CfprApSwSspEthMonFilterEpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 73, 1, 18),
    _CfprApSwSspEthMonFilterEpSrcPort_Type()
)
cfprApSwSspEthMonFilterEpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFilterEpSrcPort.setStatus("current")
_CfprApSwSspEthMonFsmTable_Object = MibTable
cfprApSwSspEthMonFsmTable = _CfprApSwSspEthMonFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTable.setStatus("current")
_CfprApSwSspEthMonFsmEntry_Object = MibTableRow
cfprApSwSspEthMonFsmEntry = _CfprApSwSspEthMonFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1)
)
cfprApSwSspEthMonFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmEntry.setStatus("current")
_CfprApSwSspEthMonFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonFsmInstanceId_Object = MibTableColumn
cfprApSwSspEthMonFsmInstanceId = _CfprApSwSspEthMonFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 1),
    _CfprApSwSspEthMonFsmInstanceId_Type()
)
cfprApSwSspEthMonFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmInstanceId.setStatus("current")
_CfprApSwSspEthMonFsmDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonFsmDn_Object = MibTableColumn
cfprApSwSspEthMonFsmDn = _CfprApSwSspEthMonFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 2),
    _CfprApSwSspEthMonFsmDn_Type()
)
cfprApSwSspEthMonFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmDn.setStatus("current")
_CfprApSwSspEthMonFsmRn_Type = SnmpAdminString
_CfprApSwSspEthMonFsmRn_Object = MibTableColumn
cfprApSwSspEthMonFsmRn = _CfprApSwSspEthMonFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 3),
    _CfprApSwSspEthMonFsmRn_Type()
)
cfprApSwSspEthMonFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmRn.setStatus("current")
_CfprApSwSspEthMonFsmCompletionTime_Type = DateAndTime
_CfprApSwSspEthMonFsmCompletionTime_Object = MibTableColumn
cfprApSwSspEthMonFsmCompletionTime = _CfprApSwSspEthMonFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 4),
    _CfprApSwSspEthMonFsmCompletionTime_Type()
)
cfprApSwSspEthMonFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmCompletionTime.setStatus("current")
_CfprApSwSspEthMonFsmCurrentFsm_Type = CfprApSwSspEthMonFsmCurrentFsm
_CfprApSwSspEthMonFsmCurrentFsm_Object = MibTableColumn
cfprApSwSspEthMonFsmCurrentFsm = _CfprApSwSspEthMonFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 5),
    _CfprApSwSspEthMonFsmCurrentFsm_Type()
)
cfprApSwSspEthMonFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmCurrentFsm.setStatus("current")
_CfprApSwSspEthMonFsmDescrData_Type = SnmpAdminString
_CfprApSwSspEthMonFsmDescrData_Object = MibTableColumn
cfprApSwSspEthMonFsmDescrData = _CfprApSwSspEthMonFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 6),
    _CfprApSwSspEthMonFsmDescrData_Type()
)
cfprApSwSspEthMonFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmDescrData.setStatus("current")
_CfprApSwSspEthMonFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwSspEthMonFsmFsmStatus_Object = MibTableColumn
cfprApSwSspEthMonFsmFsmStatus = _CfprApSwSspEthMonFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 7),
    _CfprApSwSspEthMonFsmFsmStatus_Type()
)
cfprApSwSspEthMonFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmFsmStatus.setStatus("current")
_CfprApSwSspEthMonFsmProgress_Type = Gauge32
_CfprApSwSspEthMonFsmProgress_Object = MibTableColumn
cfprApSwSspEthMonFsmProgress = _CfprApSwSspEthMonFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 8),
    _CfprApSwSspEthMonFsmProgress_Type()
)
cfprApSwSspEthMonFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmProgress.setStatus("current")
_CfprApSwSspEthMonFsmRmtErrCode_Type = Gauge32
_CfprApSwSspEthMonFsmRmtErrCode_Object = MibTableColumn
cfprApSwSspEthMonFsmRmtErrCode = _CfprApSwSspEthMonFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 9),
    _CfprApSwSspEthMonFsmRmtErrCode_Type()
)
cfprApSwSspEthMonFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmRmtErrCode.setStatus("current")
_CfprApSwSspEthMonFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwSspEthMonFsmRmtErrDescr_Object = MibTableColumn
cfprApSwSspEthMonFsmRmtErrDescr = _CfprApSwSspEthMonFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 10),
    _CfprApSwSspEthMonFsmRmtErrDescr_Type()
)
cfprApSwSspEthMonFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmRmtErrDescr.setStatus("current")
_CfprApSwSspEthMonFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwSspEthMonFsmRmtRslt_Object = MibTableColumn
cfprApSwSspEthMonFsmRmtRslt = _CfprApSwSspEthMonFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 74, 1, 11),
    _CfprApSwSspEthMonFsmRmtRslt_Type()
)
cfprApSwSspEthMonFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmRmtRslt.setStatus("current")
_CfprApSwSspEthMonFsmStageTable_Object = MibTable
cfprApSwSspEthMonFsmStageTable = _CfprApSwSspEthMonFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageTable.setStatus("current")
_CfprApSwSspEthMonFsmStageEntry_Object = MibTableRow
cfprApSwSspEthMonFsmStageEntry = _CfprApSwSspEthMonFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1)
)
cfprApSwSspEthMonFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageEntry.setStatus("current")
_CfprApSwSspEthMonFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonFsmStageInstanceId_Object = MibTableColumn
cfprApSwSspEthMonFsmStageInstanceId = _CfprApSwSspEthMonFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 1),
    _CfprApSwSspEthMonFsmStageInstanceId_Type()
)
cfprApSwSspEthMonFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageInstanceId.setStatus("current")
_CfprApSwSspEthMonFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonFsmStageDn_Object = MibTableColumn
cfprApSwSspEthMonFsmStageDn = _CfprApSwSspEthMonFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 2),
    _CfprApSwSspEthMonFsmStageDn_Type()
)
cfprApSwSspEthMonFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageDn.setStatus("current")
_CfprApSwSspEthMonFsmStageRn_Type = SnmpAdminString
_CfprApSwSspEthMonFsmStageRn_Object = MibTableColumn
cfprApSwSspEthMonFsmStageRn = _CfprApSwSspEthMonFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 3),
    _CfprApSwSspEthMonFsmStageRn_Type()
)
cfprApSwSspEthMonFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageRn.setStatus("current")
_CfprApSwSspEthMonFsmStageDescrData_Type = SnmpAdminString
_CfprApSwSspEthMonFsmStageDescrData_Object = MibTableColumn
cfprApSwSspEthMonFsmStageDescrData = _CfprApSwSspEthMonFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 4),
    _CfprApSwSspEthMonFsmStageDescrData_Type()
)
cfprApSwSspEthMonFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageDescrData.setStatus("current")
_CfprApSwSspEthMonFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwSspEthMonFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwSspEthMonFsmStageLastUpdateTime = _CfprApSwSspEthMonFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 5),
    _CfprApSwSspEthMonFsmStageLastUpdateTime_Type()
)
cfprApSwSspEthMonFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageLastUpdateTime.setStatus("current")
_CfprApSwSspEthMonFsmStageName_Type = CfprApSwSspEthMonFsmStageName
_CfprApSwSspEthMonFsmStageName_Object = MibTableColumn
cfprApSwSspEthMonFsmStageName = _CfprApSwSspEthMonFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 6),
    _CfprApSwSspEthMonFsmStageName_Type()
)
cfprApSwSspEthMonFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageName.setStatus("current")
_CfprApSwSspEthMonFsmStageOrder_Type = Gauge32
_CfprApSwSspEthMonFsmStageOrder_Object = MibTableColumn
cfprApSwSspEthMonFsmStageOrder = _CfprApSwSspEthMonFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 7),
    _CfprApSwSspEthMonFsmStageOrder_Type()
)
cfprApSwSspEthMonFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageOrder.setStatus("current")
_CfprApSwSspEthMonFsmStageRetry_Type = Gauge32
_CfprApSwSspEthMonFsmStageRetry_Object = MibTableColumn
cfprApSwSspEthMonFsmStageRetry = _CfprApSwSspEthMonFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 8),
    _CfprApSwSspEthMonFsmStageRetry_Type()
)
cfprApSwSspEthMonFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageRetry.setStatus("current")
_CfprApSwSspEthMonFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwSspEthMonFsmStageStageStatus_Object = MibTableColumn
cfprApSwSspEthMonFsmStageStageStatus = _CfprApSwSspEthMonFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 75, 1, 9),
    _CfprApSwSspEthMonFsmStageStageStatus_Type()
)
cfprApSwSspEthMonFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmStageStageStatus.setStatus("current")
_CfprApSwSspEthMonFsmTaskTable_Object = MibTable
cfprApSwSspEthMonFsmTaskTable = _CfprApSwSspEthMonFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskTable.setStatus("current")
_CfprApSwSspEthMonFsmTaskEntry_Object = MibTableRow
cfprApSwSspEthMonFsmTaskEntry = _CfprApSwSspEthMonFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76, 1)
)
cfprApSwSspEthMonFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskEntry.setStatus("current")
_CfprApSwSspEthMonFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonFsmTaskInstanceId_Object = MibTableColumn
cfprApSwSspEthMonFsmTaskInstanceId = _CfprApSwSspEthMonFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76, 1, 1),
    _CfprApSwSspEthMonFsmTaskInstanceId_Type()
)
cfprApSwSspEthMonFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskInstanceId.setStatus("current")
_CfprApSwSspEthMonFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonFsmTaskDn_Object = MibTableColumn
cfprApSwSspEthMonFsmTaskDn = _CfprApSwSspEthMonFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76, 1, 2),
    _CfprApSwSspEthMonFsmTaskDn_Type()
)
cfprApSwSspEthMonFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskDn.setStatus("current")
_CfprApSwSspEthMonFsmTaskRn_Type = SnmpAdminString
_CfprApSwSspEthMonFsmTaskRn_Object = MibTableColumn
cfprApSwSspEthMonFsmTaskRn = _CfprApSwSspEthMonFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76, 1, 3),
    _CfprApSwSspEthMonFsmTaskRn_Type()
)
cfprApSwSspEthMonFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskRn.setStatus("current")
_CfprApSwSspEthMonFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwSspEthMonFsmTaskCompletion_Object = MibTableColumn
cfprApSwSspEthMonFsmTaskCompletion = _CfprApSwSspEthMonFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76, 1, 4),
    _CfprApSwSspEthMonFsmTaskCompletion_Type()
)
cfprApSwSspEthMonFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskCompletion.setStatus("current")
_CfprApSwSspEthMonFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSwSspEthMonFsmTaskFlags_Object = MibTableColumn
cfprApSwSspEthMonFsmTaskFlags = _CfprApSwSspEthMonFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76, 1, 5),
    _CfprApSwSspEthMonFsmTaskFlags_Type()
)
cfprApSwSspEthMonFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskFlags.setStatus("current")
_CfprApSwSspEthMonFsmTaskItem_Type = CfprApSwSspEthMonFsmTaskItem
_CfprApSwSspEthMonFsmTaskItem_Object = MibTableColumn
cfprApSwSspEthMonFsmTaskItem = _CfprApSwSspEthMonFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76, 1, 6),
    _CfprApSwSspEthMonFsmTaskItem_Type()
)
cfprApSwSspEthMonFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskItem.setStatus("current")
_CfprApSwSspEthMonFsmTaskSeqId_Type = Gauge32
_CfprApSwSspEthMonFsmTaskSeqId_Object = MibTableColumn
cfprApSwSspEthMonFsmTaskSeqId = _CfprApSwSspEthMonFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 76, 1, 7),
    _CfprApSwSspEthMonFsmTaskSeqId_Type()
)
cfprApSwSspEthMonFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonFsmTaskSeqId.setStatus("current")
_CfprApSwSspEthMonSrcAppEpTable_Object = MibTable
cfprApSwSspEthMonSrcAppEpTable = _CfprApSwSspEthMonSrcAppEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpTable.setStatus("current")
_CfprApSwSspEthMonSrcAppEpEntry_Object = MibTableRow
cfprApSwSspEthMonSrcAppEpEntry = _CfprApSwSspEthMonSrcAppEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1)
)
cfprApSwSspEthMonSrcAppEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonSrcAppEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpEntry.setStatus("current")
_CfprApSwSspEthMonSrcAppEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonSrcAppEpInstanceId_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpInstanceId = _CfprApSwSspEthMonSrcAppEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 1),
    _CfprApSwSspEthMonSrcAppEpInstanceId_Type()
)
cfprApSwSspEthMonSrcAppEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpInstanceId.setStatus("current")
_CfprApSwSspEthMonSrcAppEpDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonSrcAppEpDn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpDn = _CfprApSwSspEthMonSrcAppEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 2),
    _CfprApSwSspEthMonSrcAppEpDn_Type()
)
cfprApSwSspEthMonSrcAppEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpDn.setStatus("current")
_CfprApSwSspEthMonSrcAppEpRn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpRn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpRn = _CfprApSwSspEthMonSrcAppEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 3),
    _CfprApSwSspEthMonSrcAppEpRn_Type()
)
cfprApSwSspEthMonSrcAppEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpRn.setStatus("current")
_CfprApSwSspEthMonSrcAppEpAppName_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpAppName_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpAppName = _CfprApSwSspEthMonSrcAppEpAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 4),
    _CfprApSwSspEthMonSrcAppEpAppName_Type()
)
cfprApSwSspEthMonSrcAppEpAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpAppName.setStatus("current")
_CfprApSwSspEthMonSrcAppEpExternalPortDn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpExternalPortDn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpExternalPortDn = _CfprApSwSspEthMonSrcAppEpExternalPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 5),
    _CfprApSwSspEthMonSrcAppEpExternalPortDn_Type()
)
cfprApSwSspEthMonSrcAppEpExternalPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpExternalPortDn.setStatus("current")
_CfprApSwSspEthMonSrcAppEpFilter_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpFilter_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpFilter = _CfprApSwSspEthMonSrcAppEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 6),
    _CfprApSwSspEthMonSrcAppEpFilter_Type()
)
cfprApSwSspEthMonSrcAppEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpFilter.setStatus("current")
_CfprApSwSspEthMonSrcAppEpFilterDn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpFilterDn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpFilterDn = _CfprApSwSspEthMonSrcAppEpFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 7),
    _CfprApSwSspEthMonSrcAppEpFilterDn_Type()
)
cfprApSwSspEthMonSrcAppEpFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpFilterDn.setStatus("current")
_CfprApSwSspEthMonSrcAppEpLifeCycle_Type = CfprApSwPktCaptureLifeCycle
_CfprApSwSspEthMonSrcAppEpLifeCycle_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpLifeCycle = _CfprApSwSspEthMonSrcAppEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 8),
    _CfprApSwSspEthMonSrcAppEpLifeCycle_Type()
)
cfprApSwSspEthMonSrcAppEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpLifeCycle.setStatus("current")
_CfprApSwSspEthMonSrcAppEpLinkName_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpLinkName_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpLinkName = _CfprApSwSspEthMonSrcAppEpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 9),
    _CfprApSwSspEthMonSrcAppEpLinkName_Type()
)
cfprApSwSspEthMonSrcAppEpLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpLinkName.setStatus("current")
_CfprApSwSspEthMonSrcAppEpPcapfile_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpPcapfile_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpPcapfile = _CfprApSwSspEthMonSrcAppEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 10),
    _CfprApSwSspEthMonSrcAppEpPcapfile_Type()
)
cfprApSwSspEthMonSrcAppEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpPcapfile.setStatus("current")
_CfprApSwSspEthMonSrcAppEpPcapfilename_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpPcapfilename_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpPcapfilename = _CfprApSwSspEthMonSrcAppEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 11),
    _CfprApSwSspEthMonSrcAppEpPcapfilename_Type()
)
cfprApSwSspEthMonSrcAppEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpPcapfilename.setStatus("current")
_CfprApSwSspEthMonSrcAppEpPcapsize_Type = Gauge32
_CfprApSwSspEthMonSrcAppEpPcapsize_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpPcapsize = _CfprApSwSspEthMonSrcAppEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 12),
    _CfprApSwSspEthMonSrcAppEpPcapsize_Type()
)
cfprApSwSspEthMonSrcAppEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpPcapsize.setStatus("current")
_CfprApSwSspEthMonSrcAppEpPeerDn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpPeerDn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpPeerDn = _CfprApSwSspEthMonSrcAppEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 13),
    _CfprApSwSspEthMonSrcAppEpPeerDn_Type()
)
cfprApSwSspEthMonSrcAppEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpPeerDn.setStatus("current")
_CfprApSwSspEthMonSrcAppEpPortChannelDn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpPortChannelDn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpPortChannelDn = _CfprApSwSspEthMonSrcAppEpPortChannelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 14),
    _CfprApSwSspEthMonSrcAppEpPortChannelDn_Type()
)
cfprApSwSspEthMonSrcAppEpPortChannelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpPortChannelDn.setStatus("current")
_CfprApSwSspEthMonSrcAppEpPortName_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppEpPortName_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpPortName = _CfprApSwSspEthMonSrcAppEpPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 15),
    _CfprApSwSspEthMonSrcAppEpPortName_Type()
)
cfprApSwSspEthMonSrcAppEpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpPortName.setStatus("current")
_CfprApSwSspEthMonSrcAppEpSlotId_Type = Gauge32
_CfprApSwSspEthMonSrcAppEpSlotId_Object = MibTableColumn
cfprApSwSspEthMonSrcAppEpSlotId = _CfprApSwSspEthMonSrcAppEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 77, 1, 16),
    _CfprApSwSspEthMonSrcAppEpSlotId_Type()
)
cfprApSwSspEthMonSrcAppEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppEpSlotId.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpTable_Object = MibTable
cfprApSwSspEthMonSrcAppLinksEpTable = _CfprApSwSspEthMonSrcAppLinksEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpTable.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpEntry_Object = MibTableRow
cfprApSwSspEthMonSrcAppLinksEpEntry = _CfprApSwSspEthMonSrcAppLinksEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1)
)
cfprApSwSspEthMonSrcAppLinksEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonSrcAppLinksEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpEntry.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonSrcAppLinksEpInstanceId_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpInstanceId = _CfprApSwSspEthMonSrcAppLinksEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 1),
    _CfprApSwSspEthMonSrcAppLinksEpInstanceId_Type()
)
cfprApSwSspEthMonSrcAppLinksEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpInstanceId.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonSrcAppLinksEpDn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpDn = _CfprApSwSspEthMonSrcAppLinksEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 2),
    _CfprApSwSspEthMonSrcAppLinksEpDn_Type()
)
cfprApSwSspEthMonSrcAppLinksEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpDn.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpRn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppLinksEpRn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpRn = _CfprApSwSspEthMonSrcAppLinksEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 3),
    _CfprApSwSspEthMonSrcAppLinksEpRn_Type()
)
cfprApSwSspEthMonSrcAppLinksEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpRn.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpChassisId_Type = Gauge32
_CfprApSwSspEthMonSrcAppLinksEpChassisId_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpChassisId = _CfprApSwSspEthMonSrcAppLinksEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 4),
    _CfprApSwSspEthMonSrcAppLinksEpChassisId_Type()
)
cfprApSwSspEthMonSrcAppLinksEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpChassisId.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpEqAggrPortId_Type = Gauge32
_CfprApSwSspEthMonSrcAppLinksEpEqAggrPortId_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpEqAggrPortId = _CfprApSwSspEthMonSrcAppLinksEpEqAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 5),
    _CfprApSwSspEthMonSrcAppLinksEpEqAggrPortId_Type()
)
cfprApSwSspEthMonSrcAppLinksEpEqAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpEqAggrPortId.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpEqPortId_Type = Gauge32
_CfprApSwSspEthMonSrcAppLinksEpEqPortId_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpEqPortId = _CfprApSwSspEthMonSrcAppLinksEpEqPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 6),
    _CfprApSwSspEthMonSrcAppLinksEpEqPortId_Type()
)
cfprApSwSspEthMonSrcAppLinksEpEqPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpEqPortId.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpEqSlotId_Type = Gauge32
_CfprApSwSspEthMonSrcAppLinksEpEqSlotId_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpEqSlotId = _CfprApSwSspEthMonSrcAppLinksEpEqSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 7),
    _CfprApSwSspEthMonSrcAppLinksEpEqSlotId_Type()
)
cfprApSwSspEthMonSrcAppLinksEpEqSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpEqSlotId.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpFilter_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppLinksEpFilter_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpFilter = _CfprApSwSspEthMonSrcAppLinksEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 8),
    _CfprApSwSspEthMonSrcAppLinksEpFilter_Type()
)
cfprApSwSspEthMonSrcAppLinksEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpFilter.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpFilterDn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppLinksEpFilterDn_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpFilterDn = _CfprApSwSspEthMonSrcAppLinksEpFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 9),
    _CfprApSwSspEthMonSrcAppLinksEpFilterDn_Type()
)
cfprApSwSspEthMonSrcAppLinksEpFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpFilterDn.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpLifeCycle_Type = CfprApSwPktCaptureLifeCycle
_CfprApSwSspEthMonSrcAppLinksEpLifeCycle_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpLifeCycle = _CfprApSwSspEthMonSrcAppLinksEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 10),
    _CfprApSwSspEthMonSrcAppLinksEpLifeCycle_Type()
)
cfprApSwSspEthMonSrcAppLinksEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpLifeCycle.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpName_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppLinksEpName_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpName = _CfprApSwSspEthMonSrcAppLinksEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 11),
    _CfprApSwSspEthMonSrcAppLinksEpName_Type()
)
cfprApSwSspEthMonSrcAppLinksEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpName.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpPcapfile_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppLinksEpPcapfile_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpPcapfile = _CfprApSwSspEthMonSrcAppLinksEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 12),
    _CfprApSwSspEthMonSrcAppLinksEpPcapfile_Type()
)
cfprApSwSspEthMonSrcAppLinksEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpPcapfile.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpPcapfilename_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppLinksEpPcapfilename_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpPcapfilename = _CfprApSwSspEthMonSrcAppLinksEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 13),
    _CfprApSwSspEthMonSrcAppLinksEpPcapfilename_Type()
)
cfprApSwSspEthMonSrcAppLinksEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpPcapfilename.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpPcapsize_Type = Gauge32
_CfprApSwSspEthMonSrcAppLinksEpPcapsize_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpPcapsize = _CfprApSwSspEthMonSrcAppLinksEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 14),
    _CfprApSwSspEthMonSrcAppLinksEpPcapsize_Type()
)
cfprApSwSspEthMonSrcAppLinksEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpPcapsize.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwSspEthMonSrcAppLinksEpSwitchId_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpSwitchId = _CfprApSwSspEthMonSrcAppLinksEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 15),
    _CfprApSwSspEthMonSrcAppLinksEpSwitchId_Type()
)
cfprApSwSspEthMonSrcAppLinksEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpSwitchId.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpVlan_Type = Gauge32
_CfprApSwSspEthMonSrcAppLinksEpVlan_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpVlan = _CfprApSwSspEthMonSrcAppLinksEpVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 16),
    _CfprApSwSspEthMonSrcAppLinksEpVlan_Type()
)
cfprApSwSspEthMonSrcAppLinksEpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpVlan.setStatus("current")
_CfprApSwSspEthMonSrcAppLinksEpVnicName1_Type = SnmpAdminString
_CfprApSwSspEthMonSrcAppLinksEpVnicName1_Object = MibTableColumn
cfprApSwSspEthMonSrcAppLinksEpVnicName1 = _CfprApSwSspEthMonSrcAppLinksEpVnicName1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 78, 1, 17),
    _CfprApSwSspEthMonSrcAppLinksEpVnicName1_Type()
)
cfprApSwSspEthMonSrcAppLinksEpVnicName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcAppLinksEpVnicName1.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpTable_Object = MibTable
cfprApSwSspEthMonSrcPhyEpTable = _CfprApSwSspEthMonSrcPhyEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpTable.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpEntry_Object = MibTableRow
cfprApSwSspEthMonSrcPhyEpEntry = _CfprApSwSspEthMonSrcPhyEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1)
)
cfprApSwSspEthMonSrcPhyEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonSrcPhyEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpEntry.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonSrcPhyEpInstanceId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpInstanceId = _CfprApSwSspEthMonSrcPhyEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 1),
    _CfprApSwSspEthMonSrcPhyEpInstanceId_Type()
)
cfprApSwSspEthMonSrcPhyEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpInstanceId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonSrcPhyEpDn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpDn = _CfprApSwSspEthMonSrcPhyEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 2),
    _CfprApSwSspEthMonSrcPhyEpDn_Type()
)
cfprApSwSspEthMonSrcPhyEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpDn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpRn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpRn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpRn = _CfprApSwSspEthMonSrcPhyEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 3),
    _CfprApSwSspEthMonSrcPhyEpRn_Type()
)
cfprApSwSspEthMonSrcPhyEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpRn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpAggrPortId_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpAggrPortId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpAggrPortId = _CfprApSwSspEthMonSrcPhyEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 4),
    _CfprApSwSspEthMonSrcPhyEpAggrPortId_Type()
)
cfprApSwSspEthMonSrcPhyEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpAggrPortId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpChassisId_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpChassisId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpChassisId = _CfprApSwSspEthMonSrcPhyEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 5),
    _CfprApSwSspEthMonSrcPhyEpChassisId_Type()
)
cfprApSwSspEthMonSrcPhyEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpChassisId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFilter_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFilter_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFilter = _CfprApSwSspEthMonSrcPhyEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 6),
    _CfprApSwSspEthMonSrcPhyEpFilter_Type()
)
cfprApSwSspEthMonSrcPhyEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFilter.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFilterDn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFilterDn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFilterDn = _CfprApSwSspEthMonSrcPhyEpFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 7),
    _CfprApSwSspEthMonSrcPhyEpFilterDn_Type()
)
cfprApSwSspEthMonSrcPhyEpFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFilterDn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmDescr_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmDescr_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmDescr = _CfprApSwSspEthMonSrcPhyEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 8),
    _CfprApSwSspEthMonSrcPhyEpFsmDescr_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmDescr.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmPrev_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmPrev_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmPrev = _CfprApSwSspEthMonSrcPhyEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 9),
    _CfprApSwSspEthMonSrcPhyEpFsmPrev_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmPrev.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmProgr_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpFsmProgr_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmProgr = _CfprApSwSspEthMonSrcPhyEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 10),
    _CfprApSwSspEthMonSrcPhyEpFsmProgr_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmProgr.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode = _CfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 11),
    _CfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr = _CfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 12),
    _CfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt = _CfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 13),
    _CfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageDescr_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmStageDescr_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageDescr = _CfprApSwSspEthMonSrcPhyEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 14),
    _CfprApSwSspEthMonSrcPhyEpFsmStageDescr_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageDescr.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStamp_Type = DateAndTime
_CfprApSwSspEthMonSrcPhyEpFsmStamp_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStamp = _CfprApSwSspEthMonSrcPhyEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 15),
    _CfprApSwSspEthMonSrcPhyEpFsmStamp_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStamp.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStatus_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmStatus_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStatus = _CfprApSwSspEthMonSrcPhyEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 16),
    _CfprApSwSspEthMonSrcPhyEpFsmStatus_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStatus.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTry_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpFsmTry_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmTry = _CfprApSwSspEthMonSrcPhyEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 17),
    _CfprApSwSspEthMonSrcPhyEpFsmTry_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTry.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpLifeCycle_Type = CfprApSwPktCaptureLifeCycle
_CfprApSwSspEthMonSrcPhyEpLifeCycle_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpLifeCycle = _CfprApSwSspEthMonSrcPhyEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 18),
    _CfprApSwSspEthMonSrcPhyEpLifeCycle_Type()
)
cfprApSwSspEthMonSrcPhyEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpLifeCycle.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpPcapfile_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpPcapfile_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpPcapfile = _CfprApSwSspEthMonSrcPhyEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 19),
    _CfprApSwSspEthMonSrcPhyEpPcapfile_Type()
)
cfprApSwSspEthMonSrcPhyEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpPcapfile.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpPcapfilename_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpPcapfilename_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpPcapfilename = _CfprApSwSspEthMonSrcPhyEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 20),
    _CfprApSwSspEthMonSrcPhyEpPcapfilename_Type()
)
cfprApSwSspEthMonSrcPhyEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpPcapfilename.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpPcapsize_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpPcapsize_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpPcapsize = _CfprApSwSspEthMonSrcPhyEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 21),
    _CfprApSwSspEthMonSrcPhyEpPcapsize_Type()
)
cfprApSwSspEthMonSrcPhyEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpPcapsize.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpPeerDn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpPeerDn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpPeerDn = _CfprApSwSspEthMonSrcPhyEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 22),
    _CfprApSwSspEthMonSrcPhyEpPeerDn_Type()
)
cfprApSwSspEthMonSrcPhyEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpPeerDn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpPortId_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpPortId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpPortId = _CfprApSwSspEthMonSrcPhyEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 23),
    _CfprApSwSspEthMonSrcPhyEpPortId_Type()
)
cfprApSwSspEthMonSrcPhyEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpPortId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpSlotId_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpSlotId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpSlotId = _CfprApSwSspEthMonSrcPhyEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 24),
    _CfprApSwSspEthMonSrcPhyEpSlotId_Type()
)
cfprApSwSspEthMonSrcPhyEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpSlotId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwSspEthMonSrcPhyEpSwitchId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpSwitchId = _CfprApSwSspEthMonSrcPhyEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 79, 1, 25),
    _CfprApSwSspEthMonSrcPhyEpSwitchId_Type()
)
cfprApSwSspEthMonSrcPhyEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpSwitchId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTable_Object = MibTable
cfprApSwSspEthMonSrcPhyEpFsmTable = _CfprApSwSspEthMonSrcPhyEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTable.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmEntry_Object = MibTableRow
cfprApSwSspEthMonSrcPhyEpFsmEntry = _CfprApSwSspEthMonSrcPhyEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1)
)
cfprApSwSspEthMonSrcPhyEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonSrcPhyEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmEntry.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonSrcPhyEpFsmInstanceId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmInstanceId = _CfprApSwSspEthMonSrcPhyEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 1),
    _CfprApSwSspEthMonSrcPhyEpFsmInstanceId_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmInstanceId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonSrcPhyEpFsmDn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmDn = _CfprApSwSspEthMonSrcPhyEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 2),
    _CfprApSwSspEthMonSrcPhyEpFsmDn_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmDn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmRn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmRn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmRn = _CfprApSwSspEthMonSrcPhyEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 3),
    _CfprApSwSspEthMonSrcPhyEpFsmRn_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmRn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmCompletionTime_Type = DateAndTime
_CfprApSwSspEthMonSrcPhyEpFsmCompletionTime_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmCompletionTime = _CfprApSwSspEthMonSrcPhyEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 4),
    _CfprApSwSspEthMonSrcPhyEpFsmCompletionTime_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmCompletionTime.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmCurrentFsm_Type = CfprApSwSspEthMonSrcPhyEpFsmCurrentFsm
_CfprApSwSspEthMonSrcPhyEpFsmCurrentFsm_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmCurrentFsm = _CfprApSwSspEthMonSrcPhyEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 5),
    _CfprApSwSspEthMonSrcPhyEpFsmCurrentFsm_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmCurrentFsm.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmDescrData_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmDescrData_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmDescrData = _CfprApSwSspEthMonSrcPhyEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 6),
    _CfprApSwSspEthMonSrcPhyEpFsmDescrData_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmDescrData.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwSspEthMonSrcPhyEpFsmFsmStatus_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmFsmStatus = _CfprApSwSspEthMonSrcPhyEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 7),
    _CfprApSwSspEthMonSrcPhyEpFsmFsmStatus_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmFsmStatus.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmProgress_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpFsmProgress_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmProgress = _CfprApSwSspEthMonSrcPhyEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 8),
    _CfprApSwSspEthMonSrcPhyEpFsmProgress_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmProgress.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmRmtErrCode_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpFsmRmtErrCode_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmRmtErrCode = _CfprApSwSspEthMonSrcPhyEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 9),
    _CfprApSwSspEthMonSrcPhyEpFsmRmtErrCode_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmRmtErrCode.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr = _CfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 10),
    _CfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwSspEthMonSrcPhyEpFsmRmtRslt_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmRmtRslt = _CfprApSwSspEthMonSrcPhyEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 80, 1, 11),
    _CfprApSwSspEthMonSrcPhyEpFsmRmtRslt_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmRmtRslt.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageTable_Object = MibTable
cfprApSwSspEthMonSrcPhyEpFsmStageTable = _CfprApSwSspEthMonSrcPhyEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageTable.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageEntry_Object = MibTableRow
cfprApSwSspEthMonSrcPhyEpFsmStageEntry = _CfprApSwSspEthMonSrcPhyEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1)
)
cfprApSwSspEthMonSrcPhyEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonSrcPhyEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageEntry.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonSrcPhyEpFsmStageInstanceId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageInstanceId = _CfprApSwSspEthMonSrcPhyEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 1),
    _CfprApSwSspEthMonSrcPhyEpFsmStageInstanceId_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageInstanceId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonSrcPhyEpFsmStageDn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageDn = _CfprApSwSspEthMonSrcPhyEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 2),
    _CfprApSwSspEthMonSrcPhyEpFsmStageDn_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageDn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageRn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmStageRn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageRn = _CfprApSwSspEthMonSrcPhyEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 3),
    _CfprApSwSspEthMonSrcPhyEpFsmStageRn_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageRn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageDescrData_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmStageDescrData_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageDescrData = _CfprApSwSspEthMonSrcPhyEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 4),
    _CfprApSwSspEthMonSrcPhyEpFsmStageDescrData_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageDescrData.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime = _CfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 5),
    _CfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageName_Type = CfprApSwSspEthMonSrcPhyEpFsmStageName
_CfprApSwSspEthMonSrcPhyEpFsmStageName_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageName = _CfprApSwSspEthMonSrcPhyEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 6),
    _CfprApSwSspEthMonSrcPhyEpFsmStageName_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageName.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageOrder_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpFsmStageOrder_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageOrder = _CfprApSwSspEthMonSrcPhyEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 7),
    _CfprApSwSspEthMonSrcPhyEpFsmStageOrder_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageOrder.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageRetry_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpFsmStageRetry_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageRetry = _CfprApSwSspEthMonSrcPhyEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 8),
    _CfprApSwSspEthMonSrcPhyEpFsmStageRetry_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageRetry.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwSspEthMonSrcPhyEpFsmStageStageStatus_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmStageStageStatus = _CfprApSwSspEthMonSrcPhyEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 81, 1, 9),
    _CfprApSwSspEthMonSrcPhyEpFsmStageStageStatus_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmStageStageStatus.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskTable_Object = MibTable
cfprApSwSspEthMonSrcPhyEpFsmTaskTable = _CfprApSwSspEthMonSrcPhyEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82)
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskTable.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskEntry_Object = MibTableRow
cfprApSwSspEthMonSrcPhyEpFsmTaskEntry = _CfprApSwSspEthMonSrcPhyEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82, 1)
)
cfprApSwSspEthMonSrcPhyEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskEntry.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId = _CfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82, 1, 1),
    _CfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwSspEthMonSrcPhyEpFsmTaskDn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmTaskDn = _CfprApSwSspEthMonSrcPhyEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82, 1, 2),
    _CfprApSwSspEthMonSrcPhyEpFsmTaskDn_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskDn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskRn_Type = SnmpAdminString
_CfprApSwSspEthMonSrcPhyEpFsmTaskRn_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmTaskRn = _CfprApSwSspEthMonSrcPhyEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82, 1, 3),
    _CfprApSwSspEthMonSrcPhyEpFsmTaskRn_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskRn.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwSspEthMonSrcPhyEpFsmTaskCompletion_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmTaskCompletion = _CfprApSwSspEthMonSrcPhyEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82, 1, 4),
    _CfprApSwSspEthMonSrcPhyEpFsmTaskCompletion_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskCompletion.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSwSspEthMonSrcPhyEpFsmTaskFlags_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmTaskFlags = _CfprApSwSspEthMonSrcPhyEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82, 1, 5),
    _CfprApSwSspEthMonSrcPhyEpFsmTaskFlags_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskFlags.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskItem_Type = CfprApSwSspEthMonSrcPhyEpFsmTaskItem
_CfprApSwSspEthMonSrcPhyEpFsmTaskItem_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmTaskItem = _CfprApSwSspEthMonSrcPhyEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82, 1, 6),
    _CfprApSwSspEthMonSrcPhyEpFsmTaskItem_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskItem.setStatus("current")
_CfprApSwSspEthMonSrcPhyEpFsmTaskSeqId_Type = Gauge32
_CfprApSwSspEthMonSrcPhyEpFsmTaskSeqId_Object = MibTableColumn
cfprApSwSspEthMonSrcPhyEpFsmTaskSeqId = _CfprApSwSspEthMonSrcPhyEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 82, 1, 7),
    _CfprApSwSspEthMonSrcPhyEpFsmTaskSeqId_Type()
)
cfprApSwSspEthMonSrcPhyEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSspEthMonSrcPhyEpFsmTaskSeqId.setStatus("current")
_CfprApSwSubGroupTable_Object = MibTable
cfprApSwSubGroupTable = _CfprApSwSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83)
)
if mibBuilder.loadTexts:
    cfprApSwSubGroupTable.setStatus("current")
_CfprApSwSubGroupEntry_Object = MibTableRow
cfprApSwSubGroupEntry = _CfprApSwSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1)
)
cfprApSwSubGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSubGroupEntry.setStatus("current")
_CfprApSwSubGroupInstanceId_Type = CfprApManagedObjectId
_CfprApSwSubGroupInstanceId_Object = MibTableColumn
cfprApSwSubGroupInstanceId = _CfprApSwSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 1),
    _CfprApSwSubGroupInstanceId_Type()
)
cfprApSwSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSubGroupInstanceId.setStatus("current")
_CfprApSwSubGroupDn_Type = CfprApManagedObjectDn
_CfprApSwSubGroupDn_Object = MibTableColumn
cfprApSwSubGroupDn = _CfprApSwSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 2),
    _CfprApSwSubGroupDn_Type()
)
cfprApSwSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupDn.setStatus("current")
_CfprApSwSubGroupRn_Type = SnmpAdminString
_CfprApSwSubGroupRn_Object = MibTableColumn
cfprApSwSubGroupRn = _CfprApSwSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 3),
    _CfprApSwSubGroupRn_Type()
)
cfprApSwSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupRn.setStatus("current")
_CfprApSwSubGroupAggrPortId_Type = CfprApSwSubGroupAggrPortId
_CfprApSwSubGroupAggrPortId_Object = MibTableColumn
cfprApSwSubGroupAggrPortId = _CfprApSwSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 4),
    _CfprApSwSubGroupAggrPortId_Type()
)
cfprApSwSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupAggrPortId.setStatus("current")
_CfprApSwSubGroupLicGP_Type = Unsigned64
_CfprApSwSubGroupLicGP_Object = MibTableColumn
cfprApSwSubGroupLicGP = _CfprApSwSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 5),
    _CfprApSwSubGroupLicGP_Type()
)
cfprApSwSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupLicGP.setStatus("current")
_CfprApSwSubGroupLicState_Type = CfprApLicenseState
_CfprApSwSubGroupLicState_Object = MibTableColumn
cfprApSwSubGroupLicState = _CfprApSwSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 6),
    _CfprApSwSubGroupLicState_Type()
)
cfprApSwSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupLicState.setStatus("current")
_CfprApSwSubGroupLocale_Type = CfprApNetworkLocale
_CfprApSwSubGroupLocale_Object = MibTableColumn
cfprApSwSubGroupLocale = _CfprApSwSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 7),
    _CfprApSwSubGroupLocale_Type()
)
cfprApSwSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupLocale.setStatus("current")
_CfprApSwSubGroupName_Type = SnmpAdminString
_CfprApSwSubGroupName_Object = MibTableColumn
cfprApSwSubGroupName = _CfprApSwSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 8),
    _CfprApSwSubGroupName_Type()
)
cfprApSwSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupName.setStatus("current")
_CfprApSwSubGroupSlotId_Type = CfprApSwSubGroupSlotId
_CfprApSwSubGroupSlotId_Object = MibTableColumn
cfprApSwSubGroupSlotId = _CfprApSwSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 9),
    _CfprApSwSubGroupSlotId_Type()
)
cfprApSwSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupSlotId.setStatus("current")
_CfprApSwSubGroupSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwSubGroupSwitchId_Object = MibTableColumn
cfprApSwSubGroupSwitchId = _CfprApSwSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 10),
    _CfprApSwSubGroupSwitchId_Type()
)
cfprApSwSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupSwitchId.setStatus("current")
_CfprApSwSubGroupTransport_Type = CfprApNetworkTransport
_CfprApSwSubGroupTransport_Object = MibTableColumn
cfprApSwSubGroupTransport = _CfprApSwSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 11),
    _CfprApSwSubGroupTransport_Type()
)
cfprApSwSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupTransport.setStatus("current")
_CfprApSwSubGroupType_Type = CfprApNetworkConnectionType
_CfprApSwSubGroupType_Object = MibTableColumn
cfprApSwSubGroupType = _CfprApSwSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 83, 1, 12),
    _CfprApSwSubGroupType_Type()
)
cfprApSwSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSubGroupType.setStatus("current")
_CfprApSwSystemStatsTable_Object = MibTable
cfprApSwSystemStatsTable = _CfprApSwSystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84)
)
if mibBuilder.loadTexts:
    cfprApSwSystemStatsTable.setStatus("current")
_CfprApSwSystemStatsEntry_Object = MibTableRow
cfprApSwSystemStatsEntry = _CfprApSwSystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1)
)
cfprApSwSystemStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSystemStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSystemStatsEntry.setStatus("current")
_CfprApSwSystemStatsInstanceId_Type = CfprApManagedObjectId
_CfprApSwSystemStatsInstanceId_Object = MibTableColumn
cfprApSwSystemStatsInstanceId = _CfprApSwSystemStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 1),
    _CfprApSwSystemStatsInstanceId_Type()
)
cfprApSwSystemStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsInstanceId.setStatus("current")
_CfprApSwSystemStatsDn_Type = CfprApManagedObjectDn
_CfprApSwSystemStatsDn_Object = MibTableColumn
cfprApSwSystemStatsDn = _CfprApSwSystemStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 2),
    _CfprApSwSystemStatsDn_Type()
)
cfprApSwSystemStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsDn.setStatus("current")
_CfprApSwSystemStatsRn_Type = SnmpAdminString
_CfprApSwSystemStatsRn_Object = MibTableColumn
cfprApSwSystemStatsRn = _CfprApSwSystemStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 3),
    _CfprApSwSystemStatsRn_Type()
)
cfprApSwSystemStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsRn.setStatus("current")
_CfprApSwSystemStatsIntervals_Type = Gauge32
_CfprApSwSystemStatsIntervals_Object = MibTableColumn
cfprApSwSystemStatsIntervals = _CfprApSwSystemStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 4),
    _CfprApSwSystemStatsIntervals_Type()
)
cfprApSwSystemStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsIntervals.setStatus("current")
_CfprApSwSystemStatsLoad_Type = Integer32
_CfprApSwSystemStatsLoad_Object = MibTableColumn
cfprApSwSystemStatsLoad = _CfprApSwSystemStatsLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 5),
    _CfprApSwSystemStatsLoad_Type()
)
cfprApSwSystemStatsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsLoad.setStatus("current")
_CfprApSwSystemStatsLoadAvg_Type = Integer32
_CfprApSwSystemStatsLoadAvg_Object = MibTableColumn
cfprApSwSystemStatsLoadAvg = _CfprApSwSystemStatsLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 6),
    _CfprApSwSystemStatsLoadAvg_Type()
)
cfprApSwSystemStatsLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsLoadAvg.setStatus("current")
_CfprApSwSystemStatsLoadMax_Type = Integer32
_CfprApSwSystemStatsLoadMax_Object = MibTableColumn
cfprApSwSystemStatsLoadMax = _CfprApSwSystemStatsLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 7),
    _CfprApSwSystemStatsLoadMax_Type()
)
cfprApSwSystemStatsLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsLoadMax.setStatus("current")
_CfprApSwSystemStatsLoadMin_Type = Integer32
_CfprApSwSystemStatsLoadMin_Object = MibTableColumn
cfprApSwSystemStatsLoadMin = _CfprApSwSystemStatsLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 8),
    _CfprApSwSystemStatsLoadMin_Type()
)
cfprApSwSystemStatsLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsLoadMin.setStatus("current")
_CfprApSwSystemStatsMemAvailable_Type = Gauge32
_CfprApSwSystemStatsMemAvailable_Object = MibTableColumn
cfprApSwSystemStatsMemAvailable = _CfprApSwSystemStatsMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 9),
    _CfprApSwSystemStatsMemAvailable_Type()
)
cfprApSwSystemStatsMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsMemAvailable.setStatus("current")
_CfprApSwSystemStatsMemAvailableAvg_Type = Gauge32
_CfprApSwSystemStatsMemAvailableAvg_Object = MibTableColumn
cfprApSwSystemStatsMemAvailableAvg = _CfprApSwSystemStatsMemAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 10),
    _CfprApSwSystemStatsMemAvailableAvg_Type()
)
cfprApSwSystemStatsMemAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsMemAvailableAvg.setStatus("current")
_CfprApSwSystemStatsMemAvailableMax_Type = Gauge32
_CfprApSwSystemStatsMemAvailableMax_Object = MibTableColumn
cfprApSwSystemStatsMemAvailableMax = _CfprApSwSystemStatsMemAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 11),
    _CfprApSwSystemStatsMemAvailableMax_Type()
)
cfprApSwSystemStatsMemAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsMemAvailableMax.setStatus("current")
_CfprApSwSystemStatsMemAvailableMin_Type = Gauge32
_CfprApSwSystemStatsMemAvailableMin_Object = MibTableColumn
cfprApSwSystemStatsMemAvailableMin = _CfprApSwSystemStatsMemAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 12),
    _CfprApSwSystemStatsMemAvailableMin_Type()
)
cfprApSwSystemStatsMemAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsMemAvailableMin.setStatus("current")
_CfprApSwSystemStatsMemCached_Type = Gauge32
_CfprApSwSystemStatsMemCached_Object = MibTableColumn
cfprApSwSystemStatsMemCached = _CfprApSwSystemStatsMemCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 13),
    _CfprApSwSystemStatsMemCached_Type()
)
cfprApSwSystemStatsMemCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsMemCached.setStatus("current")
_CfprApSwSystemStatsMemCachedAvg_Type = Gauge32
_CfprApSwSystemStatsMemCachedAvg_Object = MibTableColumn
cfprApSwSystemStatsMemCachedAvg = _CfprApSwSystemStatsMemCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 14),
    _CfprApSwSystemStatsMemCachedAvg_Type()
)
cfprApSwSystemStatsMemCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsMemCachedAvg.setStatus("current")
_CfprApSwSystemStatsMemCachedMax_Type = Gauge32
_CfprApSwSystemStatsMemCachedMax_Object = MibTableColumn
cfprApSwSystemStatsMemCachedMax = _CfprApSwSystemStatsMemCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 15),
    _CfprApSwSystemStatsMemCachedMax_Type()
)
cfprApSwSystemStatsMemCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsMemCachedMax.setStatus("current")
_CfprApSwSystemStatsMemCachedMin_Type = Gauge32
_CfprApSwSystemStatsMemCachedMin_Object = MibTableColumn
cfprApSwSystemStatsMemCachedMin = _CfprApSwSystemStatsMemCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 16),
    _CfprApSwSystemStatsMemCachedMin_Type()
)
cfprApSwSystemStatsMemCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsMemCachedMin.setStatus("current")
_CfprApSwSystemStatsSuspect_Type = TruthValue
_CfprApSwSystemStatsSuspect_Object = MibTableColumn
cfprApSwSystemStatsSuspect = _CfprApSwSystemStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 17),
    _CfprApSwSystemStatsSuspect_Type()
)
cfprApSwSystemStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsSuspect.setStatus("current")
_CfprApSwSystemStatsThresholded_Type = CfprApSwSystemStatsThresholded
_CfprApSwSystemStatsThresholded_Object = MibTableColumn
cfprApSwSystemStatsThresholded = _CfprApSwSystemStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 18),
    _CfprApSwSystemStatsThresholded_Type()
)
cfprApSwSystemStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsThresholded.setStatus("current")
_CfprApSwSystemStatsTimeCollected_Type = DateAndTime
_CfprApSwSystemStatsTimeCollected_Object = MibTableColumn
cfprApSwSystemStatsTimeCollected = _CfprApSwSystemStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 19),
    _CfprApSwSystemStatsTimeCollected_Type()
)
cfprApSwSystemStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsTimeCollected.setStatus("current")
_CfprApSwSystemStatsUpdate_Type = Gauge32
_CfprApSwSystemStatsUpdate_Object = MibTableColumn
cfprApSwSystemStatsUpdate = _CfprApSwSystemStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 84, 1, 20),
    _CfprApSwSystemStatsUpdate_Type()
)
cfprApSwSystemStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsUpdate.setStatus("current")
_CfprApSwSystemStatsHistTable_Object = MibTable
cfprApSwSystemStatsHistTable = _CfprApSwSystemStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85)
)
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistTable.setStatus("current")
_CfprApSwSystemStatsHistEntry_Object = MibTableRow
cfprApSwSystemStatsHistEntry = _CfprApSwSystemStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1)
)
cfprApSwSystemStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwSystemStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistEntry.setStatus("current")
_CfprApSwSystemStatsHistInstanceId_Type = CfprApManagedObjectId
_CfprApSwSystemStatsHistInstanceId_Object = MibTableColumn
cfprApSwSystemStatsHistInstanceId = _CfprApSwSystemStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 1),
    _CfprApSwSystemStatsHistInstanceId_Type()
)
cfprApSwSystemStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistInstanceId.setStatus("current")
_CfprApSwSystemStatsHistDn_Type = CfprApManagedObjectDn
_CfprApSwSystemStatsHistDn_Object = MibTableColumn
cfprApSwSystemStatsHistDn = _CfprApSwSystemStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 2),
    _CfprApSwSystemStatsHistDn_Type()
)
cfprApSwSystemStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistDn.setStatus("current")
_CfprApSwSystemStatsHistRn_Type = SnmpAdminString
_CfprApSwSystemStatsHistRn_Object = MibTableColumn
cfprApSwSystemStatsHistRn = _CfprApSwSystemStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 3),
    _CfprApSwSystemStatsHistRn_Type()
)
cfprApSwSystemStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistRn.setStatus("current")
_CfprApSwSystemStatsHistId_Type = Unsigned64
_CfprApSwSystemStatsHistId_Object = MibTableColumn
cfprApSwSystemStatsHistId = _CfprApSwSystemStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 4),
    _CfprApSwSystemStatsHistId_Type()
)
cfprApSwSystemStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistId.setStatus("current")
_CfprApSwSystemStatsHistLoad_Type = Integer32
_CfprApSwSystemStatsHistLoad_Object = MibTableColumn
cfprApSwSystemStatsHistLoad = _CfprApSwSystemStatsHistLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 5),
    _CfprApSwSystemStatsHistLoad_Type()
)
cfprApSwSystemStatsHistLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistLoad.setStatus("current")
_CfprApSwSystemStatsHistLoadAvg_Type = Integer32
_CfprApSwSystemStatsHistLoadAvg_Object = MibTableColumn
cfprApSwSystemStatsHistLoadAvg = _CfprApSwSystemStatsHistLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 6),
    _CfprApSwSystemStatsHistLoadAvg_Type()
)
cfprApSwSystemStatsHistLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistLoadAvg.setStatus("current")
_CfprApSwSystemStatsHistLoadMax_Type = Integer32
_CfprApSwSystemStatsHistLoadMax_Object = MibTableColumn
cfprApSwSystemStatsHistLoadMax = _CfprApSwSystemStatsHistLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 7),
    _CfprApSwSystemStatsHistLoadMax_Type()
)
cfprApSwSystemStatsHistLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistLoadMax.setStatus("current")
_CfprApSwSystemStatsHistLoadMin_Type = Integer32
_CfprApSwSystemStatsHistLoadMin_Object = MibTableColumn
cfprApSwSystemStatsHistLoadMin = _CfprApSwSystemStatsHistLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 8),
    _CfprApSwSystemStatsHistLoadMin_Type()
)
cfprApSwSystemStatsHistLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistLoadMin.setStatus("current")
_CfprApSwSystemStatsHistMemAvailable_Type = Gauge32
_CfprApSwSystemStatsHistMemAvailable_Object = MibTableColumn
cfprApSwSystemStatsHistMemAvailable = _CfprApSwSystemStatsHistMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 9),
    _CfprApSwSystemStatsHistMemAvailable_Type()
)
cfprApSwSystemStatsHistMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMemAvailable.setStatus("current")
_CfprApSwSystemStatsHistMemAvailableAvg_Type = Gauge32
_CfprApSwSystemStatsHistMemAvailableAvg_Object = MibTableColumn
cfprApSwSystemStatsHistMemAvailableAvg = _CfprApSwSystemStatsHistMemAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 10),
    _CfprApSwSystemStatsHistMemAvailableAvg_Type()
)
cfprApSwSystemStatsHistMemAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMemAvailableAvg.setStatus("current")
_CfprApSwSystemStatsHistMemAvailableMax_Type = Gauge32
_CfprApSwSystemStatsHistMemAvailableMax_Object = MibTableColumn
cfprApSwSystemStatsHistMemAvailableMax = _CfprApSwSystemStatsHistMemAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 11),
    _CfprApSwSystemStatsHistMemAvailableMax_Type()
)
cfprApSwSystemStatsHistMemAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMemAvailableMax.setStatus("current")
_CfprApSwSystemStatsHistMemAvailableMin_Type = Gauge32
_CfprApSwSystemStatsHistMemAvailableMin_Object = MibTableColumn
cfprApSwSystemStatsHistMemAvailableMin = _CfprApSwSystemStatsHistMemAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 12),
    _CfprApSwSystemStatsHistMemAvailableMin_Type()
)
cfprApSwSystemStatsHistMemAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMemAvailableMin.setStatus("current")
_CfprApSwSystemStatsHistMemCached_Type = Gauge32
_CfprApSwSystemStatsHistMemCached_Object = MibTableColumn
cfprApSwSystemStatsHistMemCached = _CfprApSwSystemStatsHistMemCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 13),
    _CfprApSwSystemStatsHistMemCached_Type()
)
cfprApSwSystemStatsHistMemCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMemCached.setStatus("current")
_CfprApSwSystemStatsHistMemCachedAvg_Type = Gauge32
_CfprApSwSystemStatsHistMemCachedAvg_Object = MibTableColumn
cfprApSwSystemStatsHistMemCachedAvg = _CfprApSwSystemStatsHistMemCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 14),
    _CfprApSwSystemStatsHistMemCachedAvg_Type()
)
cfprApSwSystemStatsHistMemCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMemCachedAvg.setStatus("current")
_CfprApSwSystemStatsHistMemCachedMax_Type = Gauge32
_CfprApSwSystemStatsHistMemCachedMax_Object = MibTableColumn
cfprApSwSystemStatsHistMemCachedMax = _CfprApSwSystemStatsHistMemCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 15),
    _CfprApSwSystemStatsHistMemCachedMax_Type()
)
cfprApSwSystemStatsHistMemCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMemCachedMax.setStatus("current")
_CfprApSwSystemStatsHistMemCachedMin_Type = Gauge32
_CfprApSwSystemStatsHistMemCachedMin_Object = MibTableColumn
cfprApSwSystemStatsHistMemCachedMin = _CfprApSwSystemStatsHistMemCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 16),
    _CfprApSwSystemStatsHistMemCachedMin_Type()
)
cfprApSwSystemStatsHistMemCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMemCachedMin.setStatus("current")
_CfprApSwSystemStatsHistMostRecent_Type = TruthValue
_CfprApSwSystemStatsHistMostRecent_Object = MibTableColumn
cfprApSwSystemStatsHistMostRecent = _CfprApSwSystemStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 17),
    _CfprApSwSystemStatsHistMostRecent_Type()
)
cfprApSwSystemStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistMostRecent.setStatus("current")
_CfprApSwSystemStatsHistSuspect_Type = TruthValue
_CfprApSwSystemStatsHistSuspect_Object = MibTableColumn
cfprApSwSystemStatsHistSuspect = _CfprApSwSystemStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 18),
    _CfprApSwSystemStatsHistSuspect_Type()
)
cfprApSwSystemStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistSuspect.setStatus("current")
_CfprApSwSystemStatsHistThresholded_Type = CfprApSwSystemStatsHistThresholded
_CfprApSwSystemStatsHistThresholded_Object = MibTableColumn
cfprApSwSystemStatsHistThresholded = _CfprApSwSystemStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 19),
    _CfprApSwSystemStatsHistThresholded_Type()
)
cfprApSwSystemStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistThresholded.setStatus("current")
_CfprApSwSystemStatsHistTimeCollected_Type = DateAndTime
_CfprApSwSystemStatsHistTimeCollected_Object = MibTableColumn
cfprApSwSystemStatsHistTimeCollected = _CfprApSwSystemStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 85, 1, 20),
    _CfprApSwSystemStatsHistTimeCollected_Type()
)
cfprApSwSystemStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwSystemStatsHistTimeCollected.setStatus("current")
_CfprApSwUlanTable_Object = MibTable
cfprApSwUlanTable = _CfprApSwUlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86)
)
if mibBuilder.loadTexts:
    cfprApSwUlanTable.setStatus("current")
_CfprApSwUlanEntry_Object = MibTableRow
cfprApSwUlanEntry = _CfprApSwUlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1)
)
cfprApSwUlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwUlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwUlanEntry.setStatus("current")
_CfprApSwUlanInstanceId_Type = CfprApManagedObjectId
_CfprApSwUlanInstanceId_Object = MibTableColumn
cfprApSwUlanInstanceId = _CfprApSwUlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 1),
    _CfprApSwUlanInstanceId_Type()
)
cfprApSwUlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwUlanInstanceId.setStatus("current")
_CfprApSwUlanDn_Type = CfprApManagedObjectDn
_CfprApSwUlanDn_Object = MibTableColumn
cfprApSwUlanDn = _CfprApSwUlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 2),
    _CfprApSwUlanDn_Type()
)
cfprApSwUlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanDn.setStatus("current")
_CfprApSwUlanRn_Type = SnmpAdminString
_CfprApSwUlanRn_Object = MibTableColumn
cfprApSwUlanRn = _CfprApSwUlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 3),
    _CfprApSwUlanRn_Type()
)
cfprApSwUlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanRn.setStatus("current")
_CfprApSwUlanAssocPrimaryVlanState_Type = CfprApFabricVlanAssocPrimaryVlanState
_CfprApSwUlanAssocPrimaryVlanState_Object = MibTableColumn
cfprApSwUlanAssocPrimaryVlanState = _CfprApSwUlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 4),
    _CfprApSwUlanAssocPrimaryVlanState_Type()
)
cfprApSwUlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanAssocPrimaryVlanState.setStatus("current")
_CfprApSwUlanAssocPrimaryVlanSwitchId_Type = CfprApFabricAVlanAssocPrimaryVlanSwitchId
_CfprApSwUlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprApSwUlanAssocPrimaryVlanSwitchId = _CfprApSwUlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 5),
    _CfprApSwUlanAssocPrimaryVlanSwitchId_Type()
)
cfprApSwUlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprApSwUlanEpDn_Type = SnmpAdminString
_CfprApSwUlanEpDn_Object = MibTableColumn
cfprApSwUlanEpDn = _CfprApSwUlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 6),
    _CfprApSwUlanEpDn_Type()
)
cfprApSwUlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanEpDn.setStatus("current")
_CfprApSwUlanId_Type = Gauge32
_CfprApSwUlanId_Object = MibTableColumn
cfprApSwUlanId = _CfprApSwUlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 7),
    _CfprApSwUlanId_Type()
)
cfprApSwUlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanId.setStatus("current")
_CfprApSwUlanIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApSwUlanIfRole_Object = MibTableColumn
cfprApSwUlanIfRole = _CfprApSwUlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 8),
    _CfprApSwUlanIfRole_Type()
)
cfprApSwUlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanIfRole.setStatus("current")
_CfprApSwUlanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApSwUlanIfType_Object = MibTableColumn
cfprApSwUlanIfType = _CfprApSwUlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 9),
    _CfprApSwUlanIfType_Type()
)
cfprApSwUlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanIfType.setStatus("current")
_CfprApSwUlanLocale_Type = CfprApFabricVnetEpLocale
_CfprApSwUlanLocale_Object = MibTableColumn
cfprApSwUlanLocale = _CfprApSwUlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 10),
    _CfprApSwUlanLocale_Type()
)
cfprApSwUlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanLocale.setStatus("current")
_CfprApSwUlanName_Type = SnmpAdminString
_CfprApSwUlanName_Object = MibTableColumn
cfprApSwUlanName = _CfprApSwUlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 11),
    _CfprApSwUlanName_Type()
)
cfprApSwUlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanName.setStatus("current")
_CfprApSwUlanOperState_Type = CfprApFabricVlanOperState
_CfprApSwUlanOperState_Object = MibTableColumn
cfprApSwUlanOperState = _CfprApSwUlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 12),
    _CfprApSwUlanOperState_Type()
)
cfprApSwUlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanOperState.setStatus("current")
_CfprApSwUlanOverlapStateForA_Type = CfprApFabricVlanOverlapState
_CfprApSwUlanOverlapStateForA_Object = MibTableColumn
cfprApSwUlanOverlapStateForA = _CfprApSwUlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 13),
    _CfprApSwUlanOverlapStateForA_Type()
)
cfprApSwUlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanOverlapStateForA.setStatus("current")
_CfprApSwUlanOverlapStateForB_Type = CfprApFabricVlanOverlapState
_CfprApSwUlanOverlapStateForB_Object = MibTableColumn
cfprApSwUlanOverlapStateForB = _CfprApSwUlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 14),
    _CfprApSwUlanOverlapStateForB_Type()
)
cfprApSwUlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanOverlapStateForB.setStatus("current")
_CfprApSwUlanPeerDn_Type = SnmpAdminString
_CfprApSwUlanPeerDn_Object = MibTableColumn
cfprApSwUlanPeerDn = _CfprApSwUlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 15),
    _CfprApSwUlanPeerDn_Type()
)
cfprApSwUlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanPeerDn.setStatus("current")
_CfprApSwUlanPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApSwUlanPolicyOwner_Object = MibTableColumn
cfprApSwUlanPolicyOwner = _CfprApSwUlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 16),
    _CfprApSwUlanPolicyOwner_Type()
)
cfprApSwUlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanPolicyOwner.setStatus("current")
_CfprApSwUlanPubNwDn_Type = SnmpAdminString
_CfprApSwUlanPubNwDn_Object = MibTableColumn
cfprApSwUlanPubNwDn = _CfprApSwUlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 17),
    _CfprApSwUlanPubNwDn_Type()
)
cfprApSwUlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanPubNwDn.setStatus("current")
_CfprApSwUlanPubNwId_Type = Gauge32
_CfprApSwUlanPubNwId_Object = MibTableColumn
cfprApSwUlanPubNwId = _CfprApSwUlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 18),
    _CfprApSwUlanPubNwId_Type()
)
cfprApSwUlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanPubNwId.setStatus("current")
_CfprApSwUlanPubNwName_Type = SnmpAdminString
_CfprApSwUlanPubNwName_Object = MibTableColumn
cfprApSwUlanPubNwName = _CfprApSwUlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 19),
    _CfprApSwUlanPubNwName_Type()
)
cfprApSwUlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanPubNwName.setStatus("current")
_CfprApSwUlanPurpose_Type = CfprApSwUlanPurpose
_CfprApSwUlanPurpose_Object = MibTableColumn
cfprApSwUlanPurpose = _CfprApSwUlanPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 20),
    _CfprApSwUlanPurpose_Type()
)
cfprApSwUlanPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanPurpose.setStatus("current")
_CfprApSwUlanSharing_Type = CfprApFabricAVlanSharing
_CfprApSwUlanSharing_Object = MibTableColumn
cfprApSwUlanSharing = _CfprApSwUlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 21),
    _CfprApSwUlanSharing_Type()
)
cfprApSwUlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanSharing.setStatus("current")
_CfprApSwUlanSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwUlanSwitchId_Object = MibTableColumn
cfprApSwUlanSwitchId = _CfprApSwUlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 22),
    _CfprApSwUlanSwitchId_Type()
)
cfprApSwUlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanSwitchId.setStatus("current")
_CfprApSwUlanTransport_Type = CfprApFabricAVlanTransport
_CfprApSwUlanTransport_Object = MibTableColumn
cfprApSwUlanTransport = _CfprApSwUlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 23),
    _CfprApSwUlanTransport_Type()
)
cfprApSwUlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanTransport.setStatus("current")
_CfprApSwUlanType_Type = CfprApFabricAVlanType
_CfprApSwUlanType_Object = MibTableColumn
cfprApSwUlanType = _CfprApSwUlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 24),
    _CfprApSwUlanType_Type()
)
cfprApSwUlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanType.setStatus("current")
_CfprApSwUlanVlanType_Type = CfprApFabricEpVlanVlanType
_CfprApSwUlanVlanType_Object = MibTableColumn
cfprApSwUlanVlanType = _CfprApSwUlanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 86, 1, 25),
    _CfprApSwUlanVlanType_Type()
)
cfprApSwUlanVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUlanVlanType.setStatus("current")
_CfprApSwUtilityDomainTable_Object = MibTable
cfprApSwUtilityDomainTable = _CfprApSwUtilityDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87)
)
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainTable.setStatus("current")
_CfprApSwUtilityDomainEntry_Object = MibTableRow
cfprApSwUtilityDomainEntry = _CfprApSwUtilityDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1)
)
cfprApSwUtilityDomainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwUtilityDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainEntry.setStatus("current")
_CfprApSwUtilityDomainInstanceId_Type = CfprApManagedObjectId
_CfprApSwUtilityDomainInstanceId_Object = MibTableColumn
cfprApSwUtilityDomainInstanceId = _CfprApSwUtilityDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 1),
    _CfprApSwUtilityDomainInstanceId_Type()
)
cfprApSwUtilityDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainInstanceId.setStatus("current")
_CfprApSwUtilityDomainDn_Type = CfprApManagedObjectDn
_CfprApSwUtilityDomainDn_Object = MibTableColumn
cfprApSwUtilityDomainDn = _CfprApSwUtilityDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 2),
    _CfprApSwUtilityDomainDn_Type()
)
cfprApSwUtilityDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainDn.setStatus("current")
_CfprApSwUtilityDomainRn_Type = SnmpAdminString
_CfprApSwUtilityDomainRn_Object = MibTableColumn
cfprApSwUtilityDomainRn = _CfprApSwUtilityDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 3),
    _CfprApSwUtilityDomainRn_Type()
)
cfprApSwUtilityDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainRn.setStatus("current")
_CfprApSwUtilityDomainFsmDescr_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmDescr_Object = MibTableColumn
cfprApSwUtilityDomainFsmDescr = _CfprApSwUtilityDomainFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 4),
    _CfprApSwUtilityDomainFsmDescr_Type()
)
cfprApSwUtilityDomainFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmDescr.setStatus("current")
_CfprApSwUtilityDomainFsmPrev_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmPrev_Object = MibTableColumn
cfprApSwUtilityDomainFsmPrev = _CfprApSwUtilityDomainFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 5),
    _CfprApSwUtilityDomainFsmPrev_Type()
)
cfprApSwUtilityDomainFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmPrev.setStatus("current")
_CfprApSwUtilityDomainFsmProgr_Type = Gauge32
_CfprApSwUtilityDomainFsmProgr_Object = MibTableColumn
cfprApSwUtilityDomainFsmProgr = _CfprApSwUtilityDomainFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 6),
    _CfprApSwUtilityDomainFsmProgr_Type()
)
cfprApSwUtilityDomainFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmProgr.setStatus("current")
_CfprApSwUtilityDomainFsmRmtInvErrCode_Type = Gauge32
_CfprApSwUtilityDomainFsmRmtInvErrCode_Object = MibTableColumn
cfprApSwUtilityDomainFsmRmtInvErrCode = _CfprApSwUtilityDomainFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 7),
    _CfprApSwUtilityDomainFsmRmtInvErrCode_Type()
)
cfprApSwUtilityDomainFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmRmtInvErrCode.setStatus("current")
_CfprApSwUtilityDomainFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmRmtInvErrDescr_Object = MibTableColumn
cfprApSwUtilityDomainFsmRmtInvErrDescr = _CfprApSwUtilityDomainFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 8),
    _CfprApSwUtilityDomainFsmRmtInvErrDescr_Type()
)
cfprApSwUtilityDomainFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmRmtInvErrDescr.setStatus("current")
_CfprApSwUtilityDomainFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwUtilityDomainFsmRmtInvRslt_Object = MibTableColumn
cfprApSwUtilityDomainFsmRmtInvRslt = _CfprApSwUtilityDomainFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 9),
    _CfprApSwUtilityDomainFsmRmtInvRslt_Type()
)
cfprApSwUtilityDomainFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmRmtInvRslt.setStatus("current")
_CfprApSwUtilityDomainFsmStageDescr_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmStageDescr_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageDescr = _CfprApSwUtilityDomainFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 10),
    _CfprApSwUtilityDomainFsmStageDescr_Type()
)
cfprApSwUtilityDomainFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageDescr.setStatus("current")
_CfprApSwUtilityDomainFsmStamp_Type = DateAndTime
_CfprApSwUtilityDomainFsmStamp_Object = MibTableColumn
cfprApSwUtilityDomainFsmStamp = _CfprApSwUtilityDomainFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 11),
    _CfprApSwUtilityDomainFsmStamp_Type()
)
cfprApSwUtilityDomainFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStamp.setStatus("current")
_CfprApSwUtilityDomainFsmStatus_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmStatus_Object = MibTableColumn
cfprApSwUtilityDomainFsmStatus = _CfprApSwUtilityDomainFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 12),
    _CfprApSwUtilityDomainFsmStatus_Type()
)
cfprApSwUtilityDomainFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStatus.setStatus("current")
_CfprApSwUtilityDomainFsmTry_Type = Gauge32
_CfprApSwUtilityDomainFsmTry_Object = MibTableColumn
cfprApSwUtilityDomainFsmTry = _CfprApSwUtilityDomainFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 13),
    _CfprApSwUtilityDomainFsmTry_Type()
)
cfprApSwUtilityDomainFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTry.setStatus("current")
_CfprApSwUtilityDomainLocale_Type = CfprApSwUtilityDomainLocale
_CfprApSwUtilityDomainLocale_Object = MibTableColumn
cfprApSwUtilityDomainLocale = _CfprApSwUtilityDomainLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 14),
    _CfprApSwUtilityDomainLocale_Type()
)
cfprApSwUtilityDomainLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainLocale.setStatus("current")
_CfprApSwUtilityDomainName_Type = SnmpAdminString
_CfprApSwUtilityDomainName_Object = MibTableColumn
cfprApSwUtilityDomainName = _CfprApSwUtilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 15),
    _CfprApSwUtilityDomainName_Type()
)
cfprApSwUtilityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainName.setStatus("current")
_CfprApSwUtilityDomainSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwUtilityDomainSwitchId_Object = MibTableColumn
cfprApSwUtilityDomainSwitchId = _CfprApSwUtilityDomainSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 16),
    _CfprApSwUtilityDomainSwitchId_Type()
)
cfprApSwUtilityDomainSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainSwitchId.setStatus("current")
_CfprApSwUtilityDomainTransport_Type = CfprApNetworkTransport
_CfprApSwUtilityDomainTransport_Object = MibTableColumn
cfprApSwUtilityDomainTransport = _CfprApSwUtilityDomainTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 17),
    _CfprApSwUtilityDomainTransport_Type()
)
cfprApSwUtilityDomainTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainTransport.setStatus("current")
_CfprApSwUtilityDomainType_Type = CfprApSwUtilityDomainType
_CfprApSwUtilityDomainType_Object = MibTableColumn
cfprApSwUtilityDomainType = _CfprApSwUtilityDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 87, 1, 18),
    _CfprApSwUtilityDomainType_Type()
)
cfprApSwUtilityDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainType.setStatus("current")
_CfprApSwUtilityDomainFsmTable_Object = MibTable
cfprApSwUtilityDomainFsmTable = _CfprApSwUtilityDomainFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88)
)
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTable.setStatus("current")
_CfprApSwUtilityDomainFsmEntry_Object = MibTableRow
cfprApSwUtilityDomainFsmEntry = _CfprApSwUtilityDomainFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1)
)
cfprApSwUtilityDomainFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwUtilityDomainFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmEntry.setStatus("current")
_CfprApSwUtilityDomainFsmInstanceId_Type = CfprApManagedObjectId
_CfprApSwUtilityDomainFsmInstanceId_Object = MibTableColumn
cfprApSwUtilityDomainFsmInstanceId = _CfprApSwUtilityDomainFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 1),
    _CfprApSwUtilityDomainFsmInstanceId_Type()
)
cfprApSwUtilityDomainFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmInstanceId.setStatus("current")
_CfprApSwUtilityDomainFsmDn_Type = CfprApManagedObjectDn
_CfprApSwUtilityDomainFsmDn_Object = MibTableColumn
cfprApSwUtilityDomainFsmDn = _CfprApSwUtilityDomainFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 2),
    _CfprApSwUtilityDomainFsmDn_Type()
)
cfprApSwUtilityDomainFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmDn.setStatus("current")
_CfprApSwUtilityDomainFsmRn_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmRn_Object = MibTableColumn
cfprApSwUtilityDomainFsmRn = _CfprApSwUtilityDomainFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 3),
    _CfprApSwUtilityDomainFsmRn_Type()
)
cfprApSwUtilityDomainFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmRn.setStatus("current")
_CfprApSwUtilityDomainFsmCompletionTime_Type = DateAndTime
_CfprApSwUtilityDomainFsmCompletionTime_Object = MibTableColumn
cfprApSwUtilityDomainFsmCompletionTime = _CfprApSwUtilityDomainFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 4),
    _CfprApSwUtilityDomainFsmCompletionTime_Type()
)
cfprApSwUtilityDomainFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmCompletionTime.setStatus("current")
_CfprApSwUtilityDomainFsmCurrentFsm_Type = CfprApSwUtilityDomainFsmCurrentFsm
_CfprApSwUtilityDomainFsmCurrentFsm_Object = MibTableColumn
cfprApSwUtilityDomainFsmCurrentFsm = _CfprApSwUtilityDomainFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 5),
    _CfprApSwUtilityDomainFsmCurrentFsm_Type()
)
cfprApSwUtilityDomainFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmCurrentFsm.setStatus("current")
_CfprApSwUtilityDomainFsmDescrData_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmDescrData_Object = MibTableColumn
cfprApSwUtilityDomainFsmDescrData = _CfprApSwUtilityDomainFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 6),
    _CfprApSwUtilityDomainFsmDescrData_Type()
)
cfprApSwUtilityDomainFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmDescrData.setStatus("current")
_CfprApSwUtilityDomainFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwUtilityDomainFsmFsmStatus_Object = MibTableColumn
cfprApSwUtilityDomainFsmFsmStatus = _CfprApSwUtilityDomainFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 7),
    _CfprApSwUtilityDomainFsmFsmStatus_Type()
)
cfprApSwUtilityDomainFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmFsmStatus.setStatus("current")
_CfprApSwUtilityDomainFsmProgress_Type = Gauge32
_CfprApSwUtilityDomainFsmProgress_Object = MibTableColumn
cfprApSwUtilityDomainFsmProgress = _CfprApSwUtilityDomainFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 8),
    _CfprApSwUtilityDomainFsmProgress_Type()
)
cfprApSwUtilityDomainFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmProgress.setStatus("current")
_CfprApSwUtilityDomainFsmRmtErrCode_Type = Gauge32
_CfprApSwUtilityDomainFsmRmtErrCode_Object = MibTableColumn
cfprApSwUtilityDomainFsmRmtErrCode = _CfprApSwUtilityDomainFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 9),
    _CfprApSwUtilityDomainFsmRmtErrCode_Type()
)
cfprApSwUtilityDomainFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmRmtErrCode.setStatus("current")
_CfprApSwUtilityDomainFsmRmtErrDescr_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmRmtErrDescr_Object = MibTableColumn
cfprApSwUtilityDomainFsmRmtErrDescr = _CfprApSwUtilityDomainFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 10),
    _CfprApSwUtilityDomainFsmRmtErrDescr_Type()
)
cfprApSwUtilityDomainFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmRmtErrDescr.setStatus("current")
_CfprApSwUtilityDomainFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApSwUtilityDomainFsmRmtRslt_Object = MibTableColumn
cfprApSwUtilityDomainFsmRmtRslt = _CfprApSwUtilityDomainFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 88, 1, 11),
    _CfprApSwUtilityDomainFsmRmtRslt_Type()
)
cfprApSwUtilityDomainFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmRmtRslt.setStatus("current")
_CfprApSwUtilityDomainFsmStageTable_Object = MibTable
cfprApSwUtilityDomainFsmStageTable = _CfprApSwUtilityDomainFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89)
)
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageTable.setStatus("current")
_CfprApSwUtilityDomainFsmStageEntry_Object = MibTableRow
cfprApSwUtilityDomainFsmStageEntry = _CfprApSwUtilityDomainFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1)
)
cfprApSwUtilityDomainFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwUtilityDomainFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageEntry.setStatus("current")
_CfprApSwUtilityDomainFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApSwUtilityDomainFsmStageInstanceId_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageInstanceId = _CfprApSwUtilityDomainFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 1),
    _CfprApSwUtilityDomainFsmStageInstanceId_Type()
)
cfprApSwUtilityDomainFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageInstanceId.setStatus("current")
_CfprApSwUtilityDomainFsmStageDn_Type = CfprApManagedObjectDn
_CfprApSwUtilityDomainFsmStageDn_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageDn = _CfprApSwUtilityDomainFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 2),
    _CfprApSwUtilityDomainFsmStageDn_Type()
)
cfprApSwUtilityDomainFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageDn.setStatus("current")
_CfprApSwUtilityDomainFsmStageRn_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmStageRn_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageRn = _CfprApSwUtilityDomainFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 3),
    _CfprApSwUtilityDomainFsmStageRn_Type()
)
cfprApSwUtilityDomainFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageRn.setStatus("current")
_CfprApSwUtilityDomainFsmStageDescrData_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmStageDescrData_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageDescrData = _CfprApSwUtilityDomainFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 4),
    _CfprApSwUtilityDomainFsmStageDescrData_Type()
)
cfprApSwUtilityDomainFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageDescrData.setStatus("current")
_CfprApSwUtilityDomainFsmStageLastUpdateTime_Type = DateAndTime
_CfprApSwUtilityDomainFsmStageLastUpdateTime_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageLastUpdateTime = _CfprApSwUtilityDomainFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 5),
    _CfprApSwUtilityDomainFsmStageLastUpdateTime_Type()
)
cfprApSwUtilityDomainFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageLastUpdateTime.setStatus("current")
_CfprApSwUtilityDomainFsmStageName_Type = CfprApSwUtilityDomainFsmStageName
_CfprApSwUtilityDomainFsmStageName_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageName = _CfprApSwUtilityDomainFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 6),
    _CfprApSwUtilityDomainFsmStageName_Type()
)
cfprApSwUtilityDomainFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageName.setStatus("current")
_CfprApSwUtilityDomainFsmStageOrder_Type = Gauge32
_CfprApSwUtilityDomainFsmStageOrder_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageOrder = _CfprApSwUtilityDomainFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 7),
    _CfprApSwUtilityDomainFsmStageOrder_Type()
)
cfprApSwUtilityDomainFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageOrder.setStatus("current")
_CfprApSwUtilityDomainFsmStageRetry_Type = Gauge32
_CfprApSwUtilityDomainFsmStageRetry_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageRetry = _CfprApSwUtilityDomainFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 8),
    _CfprApSwUtilityDomainFsmStageRetry_Type()
)
cfprApSwUtilityDomainFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageRetry.setStatus("current")
_CfprApSwUtilityDomainFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApSwUtilityDomainFsmStageStageStatus_Object = MibTableColumn
cfprApSwUtilityDomainFsmStageStageStatus = _CfprApSwUtilityDomainFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 89, 1, 9),
    _CfprApSwUtilityDomainFsmStageStageStatus_Type()
)
cfprApSwUtilityDomainFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmStageStageStatus.setStatus("current")
_CfprApSwUtilityDomainFsmTaskTable_Object = MibTable
cfprApSwUtilityDomainFsmTaskTable = _CfprApSwUtilityDomainFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90)
)
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskTable.setStatus("current")
_CfprApSwUtilityDomainFsmTaskEntry_Object = MibTableRow
cfprApSwUtilityDomainFsmTaskEntry = _CfprApSwUtilityDomainFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90, 1)
)
cfprApSwUtilityDomainFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwUtilityDomainFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskEntry.setStatus("current")
_CfprApSwUtilityDomainFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApSwUtilityDomainFsmTaskInstanceId_Object = MibTableColumn
cfprApSwUtilityDomainFsmTaskInstanceId = _CfprApSwUtilityDomainFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90, 1, 1),
    _CfprApSwUtilityDomainFsmTaskInstanceId_Type()
)
cfprApSwUtilityDomainFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskInstanceId.setStatus("current")
_CfprApSwUtilityDomainFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApSwUtilityDomainFsmTaskDn_Object = MibTableColumn
cfprApSwUtilityDomainFsmTaskDn = _CfprApSwUtilityDomainFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90, 1, 2),
    _CfprApSwUtilityDomainFsmTaskDn_Type()
)
cfprApSwUtilityDomainFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskDn.setStatus("current")
_CfprApSwUtilityDomainFsmTaskRn_Type = SnmpAdminString
_CfprApSwUtilityDomainFsmTaskRn_Object = MibTableColumn
cfprApSwUtilityDomainFsmTaskRn = _CfprApSwUtilityDomainFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90, 1, 3),
    _CfprApSwUtilityDomainFsmTaskRn_Type()
)
cfprApSwUtilityDomainFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskRn.setStatus("current")
_CfprApSwUtilityDomainFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApSwUtilityDomainFsmTaskCompletion_Object = MibTableColumn
cfprApSwUtilityDomainFsmTaskCompletion = _CfprApSwUtilityDomainFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90, 1, 4),
    _CfprApSwUtilityDomainFsmTaskCompletion_Type()
)
cfprApSwUtilityDomainFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskCompletion.setStatus("current")
_CfprApSwUtilityDomainFsmTaskFlags_Type = CfprApFsmFlags
_CfprApSwUtilityDomainFsmTaskFlags_Object = MibTableColumn
cfprApSwUtilityDomainFsmTaskFlags = _CfprApSwUtilityDomainFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90, 1, 5),
    _CfprApSwUtilityDomainFsmTaskFlags_Type()
)
cfprApSwUtilityDomainFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskFlags.setStatus("current")
_CfprApSwUtilityDomainFsmTaskItem_Type = CfprApSwUtilityDomainFsmTaskItem
_CfprApSwUtilityDomainFsmTaskItem_Object = MibTableColumn
cfprApSwUtilityDomainFsmTaskItem = _CfprApSwUtilityDomainFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90, 1, 6),
    _CfprApSwUtilityDomainFsmTaskItem_Type()
)
cfprApSwUtilityDomainFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskItem.setStatus("current")
_CfprApSwUtilityDomainFsmTaskSeqId_Type = Gauge32
_CfprApSwUtilityDomainFsmTaskSeqId_Object = MibTableColumn
cfprApSwUtilityDomainFsmTaskSeqId = _CfprApSwUtilityDomainFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 90, 1, 7),
    _CfprApSwUtilityDomainFsmTaskSeqId_Type()
)
cfprApSwUtilityDomainFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwUtilityDomainFsmTaskSeqId.setStatus("current")
_CfprApSwVlanTable_Object = MibTable
cfprApSwVlanTable = _CfprApSwVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92)
)
if mibBuilder.loadTexts:
    cfprApSwVlanTable.setStatus("current")
_CfprApSwVlanEntry_Object = MibTableRow
cfprApSwVlanEntry = _CfprApSwVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1)
)
cfprApSwVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwVlanEntry.setStatus("current")
_CfprApSwVlanInstanceId_Type = CfprApManagedObjectId
_CfprApSwVlanInstanceId_Object = MibTableColumn
cfprApSwVlanInstanceId = _CfprApSwVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 1),
    _CfprApSwVlanInstanceId_Type()
)
cfprApSwVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwVlanInstanceId.setStatus("current")
_CfprApSwVlanDn_Type = CfprApManagedObjectDn
_CfprApSwVlanDn_Object = MibTableColumn
cfprApSwVlanDn = _CfprApSwVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 2),
    _CfprApSwVlanDn_Type()
)
cfprApSwVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanDn.setStatus("current")
_CfprApSwVlanRn_Type = SnmpAdminString
_CfprApSwVlanRn_Object = MibTableColumn
cfprApSwVlanRn = _CfprApSwVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 3),
    _CfprApSwVlanRn_Type()
)
cfprApSwVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanRn.setStatus("current")
_CfprApSwVlanAssocPrimaryVlanState_Type = CfprApFabricVlanAssocPrimaryVlanState
_CfprApSwVlanAssocPrimaryVlanState_Object = MibTableColumn
cfprApSwVlanAssocPrimaryVlanState = _CfprApSwVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 4),
    _CfprApSwVlanAssocPrimaryVlanState_Type()
)
cfprApSwVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanAssocPrimaryVlanState.setStatus("current")
_CfprApSwVlanAssocPrimaryVlanSwitchId_Type = CfprApFabricAVlanAssocPrimaryVlanSwitchId
_CfprApSwVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprApSwVlanAssocPrimaryVlanSwitchId = _CfprApSwVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 5),
    _CfprApSwVlanAssocPrimaryVlanSwitchId_Type()
)
cfprApSwVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprApSwVlanCompressionType_Type = CfprApSwVlanCompType
_CfprApSwVlanCompressionType_Object = MibTableColumn
cfprApSwVlanCompressionType = _CfprApSwVlanCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 6),
    _CfprApSwVlanCompressionType_Type()
)
cfprApSwVlanCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanCompressionType.setStatus("current")
_CfprApSwVlanEpDn_Type = SnmpAdminString
_CfprApSwVlanEpDn_Object = MibTableColumn
cfprApSwVlanEpDn = _CfprApSwVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 7),
    _CfprApSwVlanEpDn_Type()
)
cfprApSwVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanEpDn.setStatus("current")
_CfprApSwVlanId_Type = Gauge32
_CfprApSwVlanId_Object = MibTableColumn
cfprApSwVlanId = _CfprApSwVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 8),
    _CfprApSwVlanId_Type()
)
cfprApSwVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanId.setStatus("current")
_CfprApSwVlanIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApSwVlanIfRole_Object = MibTableColumn
cfprApSwVlanIfRole = _CfprApSwVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 9),
    _CfprApSwVlanIfRole_Type()
)
cfprApSwVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanIfRole.setStatus("current")
_CfprApSwVlanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApSwVlanIfType_Object = MibTableColumn
cfprApSwVlanIfType = _CfprApSwVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 10),
    _CfprApSwVlanIfType_Type()
)
cfprApSwVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanIfType.setStatus("current")
_CfprApSwVlanLc_Type = CfprApSwVlanLc
_CfprApSwVlanLc_Object = MibTableColumn
cfprApSwVlanLc = _CfprApSwVlanLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 11),
    _CfprApSwVlanLc_Type()
)
cfprApSwVlanLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanLc.setStatus("current")
_CfprApSwVlanLocale_Type = CfprApFabricVnetEpLocale
_CfprApSwVlanLocale_Object = MibTableColumn
cfprApSwVlanLocale = _CfprApSwVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 12),
    _CfprApSwVlanLocale_Type()
)
cfprApSwVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanLocale.setStatus("current")
_CfprApSwVlanMonTrafDir_Type = CfprApFabricTrafficDirection
_CfprApSwVlanMonTrafDir_Object = MibTableColumn
cfprApSwVlanMonTrafDir = _CfprApSwVlanMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 13),
    _CfprApSwVlanMonTrafDir_Type()
)
cfprApSwVlanMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanMonTrafDir.setStatus("current")
_CfprApSwVlanName_Type = SnmpAdminString
_CfprApSwVlanName_Object = MibTableColumn
cfprApSwVlanName = _CfprApSwVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 14),
    _CfprApSwVlanName_Type()
)
cfprApSwVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanName.setStatus("current")
_CfprApSwVlanOperState_Type = CfprApFabricVlanOperState
_CfprApSwVlanOperState_Object = MibTableColumn
cfprApSwVlanOperState = _CfprApSwVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 15),
    _CfprApSwVlanOperState_Type()
)
cfprApSwVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanOperState.setStatus("current")
_CfprApSwVlanOverlapStateForA_Type = CfprApFabricVlanOverlapState
_CfprApSwVlanOverlapStateForA_Object = MibTableColumn
cfprApSwVlanOverlapStateForA = _CfprApSwVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 16),
    _CfprApSwVlanOverlapStateForA_Type()
)
cfprApSwVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanOverlapStateForA.setStatus("current")
_CfprApSwVlanOverlapStateForB_Type = CfprApFabricVlanOverlapState
_CfprApSwVlanOverlapStateForB_Object = MibTableColumn
cfprApSwVlanOverlapStateForB = _CfprApSwVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 17),
    _CfprApSwVlanOverlapStateForB_Type()
)
cfprApSwVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanOverlapStateForB.setStatus("current")
_CfprApSwVlanPeerDn_Type = SnmpAdminString
_CfprApSwVlanPeerDn_Object = MibTableColumn
cfprApSwVlanPeerDn = _CfprApSwVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 18),
    _CfprApSwVlanPeerDn_Type()
)
cfprApSwVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPeerDn.setStatus("current")
_CfprApSwVlanPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApSwVlanPolicyOwner_Object = MibTableColumn
cfprApSwVlanPolicyOwner = _CfprApSwVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 19),
    _CfprApSwVlanPolicyOwner_Type()
)
cfprApSwVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPolicyOwner.setStatus("current")
_CfprApSwVlanPubNwDn_Type = SnmpAdminString
_CfprApSwVlanPubNwDn_Object = MibTableColumn
cfprApSwVlanPubNwDn = _CfprApSwVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 20),
    _CfprApSwVlanPubNwDn_Type()
)
cfprApSwVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPubNwDn.setStatus("current")
_CfprApSwVlanPubNwId_Type = Gauge32
_CfprApSwVlanPubNwId_Object = MibTableColumn
cfprApSwVlanPubNwId = _CfprApSwVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 21),
    _CfprApSwVlanPubNwId_Type()
)
cfprApSwVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPubNwId.setStatus("current")
_CfprApSwVlanPubNwName_Type = SnmpAdminString
_CfprApSwVlanPubNwName_Object = MibTableColumn
cfprApSwVlanPubNwName = _CfprApSwVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 22),
    _CfprApSwVlanPubNwName_Type()
)
cfprApSwVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPubNwName.setStatus("current")
_CfprApSwVlanQuerierIpAddrs_Type = InetAddressIPv4
_CfprApSwVlanQuerierIpAddrs_Object = MibTableColumn
cfprApSwVlanQuerierIpAddrs = _CfprApSwVlanQuerierIpAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 23),
    _CfprApSwVlanQuerierIpAddrs_Type()
)
cfprApSwVlanQuerierIpAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanQuerierIpAddrs.setStatus("current")
_CfprApSwVlanSecVlanPerPrimaryVlanCount_Type = Gauge32
_CfprApSwVlanSecVlanPerPrimaryVlanCount_Object = MibTableColumn
cfprApSwVlanSecVlanPerPrimaryVlanCount = _CfprApSwVlanSecVlanPerPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 24),
    _CfprApSwVlanSecVlanPerPrimaryVlanCount_Type()
)
cfprApSwVlanSecVlanPerPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanSecVlanPerPrimaryVlanCount.setStatus("current")
_CfprApSwVlanSecVlanPerPrimaryVlanCountStatus_Type = CfprApNetworkVlanCountStatus
_CfprApSwVlanSecVlanPerPrimaryVlanCountStatus_Object = MibTableColumn
cfprApSwVlanSecVlanPerPrimaryVlanCountStatus = _CfprApSwVlanSecVlanPerPrimaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 25),
    _CfprApSwVlanSecVlanPerPrimaryVlanCountStatus_Type()
)
cfprApSwVlanSecVlanPerPrimaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanSecVlanPerPrimaryVlanCountStatus.setStatus("current")
_CfprApSwVlanSharing_Type = CfprApFabricAVlanSharing
_CfprApSwVlanSharing_Object = MibTableColumn
cfprApSwVlanSharing = _CfprApSwVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 26),
    _CfprApSwVlanSharing_Type()
)
cfprApSwVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanSharing.setStatus("current")
_CfprApSwVlanSnoopingEnabled_Type = TruthValue
_CfprApSwVlanSnoopingEnabled_Object = MibTableColumn
cfprApSwVlanSnoopingEnabled = _CfprApSwVlanSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 27),
    _CfprApSwVlanSnoopingEnabled_Type()
)
cfprApSwVlanSnoopingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanSnoopingEnabled.setStatus("current")
_CfprApSwVlanSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwVlanSwitchId_Object = MibTableColumn
cfprApSwVlanSwitchId = _CfprApSwVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 28),
    _CfprApSwVlanSwitchId_Type()
)
cfprApSwVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanSwitchId.setStatus("current")
_CfprApSwVlanTransport_Type = CfprApFabricAVlanTransport
_CfprApSwVlanTransport_Object = MibTableColumn
cfprApSwVlanTransport = _CfprApSwVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 29),
    _CfprApSwVlanTransport_Type()
)
cfprApSwVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanTransport.setStatus("current")
_CfprApSwVlanType_Type = CfprApFabricAVlanType
_CfprApSwVlanType_Object = MibTableColumn
cfprApSwVlanType = _CfprApSwVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 30),
    _CfprApSwVlanType_Type()
)
cfprApSwVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanType.setStatus("current")
_CfprApSwVlanVlanType_Type = CfprApFabricEpVlanVlanType
_CfprApSwVlanVlanType_Object = MibTableColumn
cfprApSwVlanVlanType = _CfprApSwVlanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 92, 1, 31),
    _CfprApSwVlanVlanType_Type()
)
cfprApSwVlanVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanVlanType.setStatus("current")
_CfprApSwVlanGroupTable_Object = MibTable
cfprApSwVlanGroupTable = _CfprApSwVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93)
)
if mibBuilder.loadTexts:
    cfprApSwVlanGroupTable.setStatus("current")
_CfprApSwVlanGroupEntry_Object = MibTableRow
cfprApSwVlanGroupEntry = _CfprApSwVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93, 1)
)
cfprApSwVlanGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwVlanGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwVlanGroupEntry.setStatus("current")
_CfprApSwVlanGroupInstanceId_Type = CfprApManagedObjectId
_CfprApSwVlanGroupInstanceId_Object = MibTableColumn
cfprApSwVlanGroupInstanceId = _CfprApSwVlanGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93, 1, 1),
    _CfprApSwVlanGroupInstanceId_Type()
)
cfprApSwVlanGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwVlanGroupInstanceId.setStatus("current")
_CfprApSwVlanGroupDn_Type = CfprApManagedObjectDn
_CfprApSwVlanGroupDn_Object = MibTableColumn
cfprApSwVlanGroupDn = _CfprApSwVlanGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93, 1, 2),
    _CfprApSwVlanGroupDn_Type()
)
cfprApSwVlanGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanGroupDn.setStatus("current")
_CfprApSwVlanGroupRn_Type = SnmpAdminString
_CfprApSwVlanGroupRn_Object = MibTableColumn
cfprApSwVlanGroupRn = _CfprApSwVlanGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93, 1, 3),
    _CfprApSwVlanGroupRn_Type()
)
cfprApSwVlanGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanGroupRn.setStatus("current")
_CfprApSwVlanGroupId_Type = Gauge32
_CfprApSwVlanGroupId_Object = MibTableColumn
cfprApSwVlanGroupId = _CfprApSwVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93, 1, 4),
    _CfprApSwVlanGroupId_Type()
)
cfprApSwVlanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanGroupId.setStatus("current")
_CfprApSwVlanGroupPeerDn_Type = SnmpAdminString
_CfprApSwVlanGroupPeerDn_Object = MibTableColumn
cfprApSwVlanGroupPeerDn = _CfprApSwVlanGroupPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93, 1, 5),
    _CfprApSwVlanGroupPeerDn_Type()
)
cfprApSwVlanGroupPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanGroupPeerDn.setStatus("current")
_CfprApSwVlanGroupSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwVlanGroupSwitchId_Object = MibTableColumn
cfprApSwVlanGroupSwitchId = _CfprApSwVlanGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93, 1, 6),
    _CfprApSwVlanGroupSwitchId_Type()
)
cfprApSwVlanGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanGroupSwitchId.setStatus("current")
_CfprApSwVlanGroupType_Type = CfprApSwVlanGroupType
_CfprApSwVlanGroupType_Object = MibTableColumn
cfprApSwVlanGroupType = _CfprApSwVlanGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 93, 1, 7),
    _CfprApSwVlanGroupType_Type()
)
cfprApSwVlanGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanGroupType.setStatus("current")
_CfprApSwVlanPortNsTable_Object = MibTable
cfprApSwVlanPortNsTable = _CfprApSwVlanPortNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94)
)
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsTable.setStatus("current")
_CfprApSwVlanPortNsEntry_Object = MibTableRow
cfprApSwVlanPortNsEntry = _CfprApSwVlanPortNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1)
)
cfprApSwVlanPortNsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwVlanPortNsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsEntry.setStatus("current")
_CfprApSwVlanPortNsInstanceId_Type = CfprApManagedObjectId
_CfprApSwVlanPortNsInstanceId_Object = MibTableColumn
cfprApSwVlanPortNsInstanceId = _CfprApSwVlanPortNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 1),
    _CfprApSwVlanPortNsInstanceId_Type()
)
cfprApSwVlanPortNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsInstanceId.setStatus("current")
_CfprApSwVlanPortNsDn_Type = CfprApManagedObjectDn
_CfprApSwVlanPortNsDn_Object = MibTableColumn
cfprApSwVlanPortNsDn = _CfprApSwVlanPortNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 2),
    _CfprApSwVlanPortNsDn_Type()
)
cfprApSwVlanPortNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsDn.setStatus("current")
_CfprApSwVlanPortNsRn_Type = SnmpAdminString
_CfprApSwVlanPortNsRn_Object = MibTableColumn
cfprApSwVlanPortNsRn = _CfprApSwVlanPortNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 3),
    _CfprApSwVlanPortNsRn_Type()
)
cfprApSwVlanPortNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsRn.setStatus("current")
_CfprApSwVlanPortNsAccessVlanPortCount_Type = Gauge32
_CfprApSwVlanPortNsAccessVlanPortCount_Object = MibTableColumn
cfprApSwVlanPortNsAccessVlanPortCount = _CfprApSwVlanPortNsAccessVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 4),
    _CfprApSwVlanPortNsAccessVlanPortCount_Type()
)
cfprApSwVlanPortNsAccessVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsAccessVlanPortCount.setStatus("current")
_CfprApSwVlanPortNsAllocStatus_Type = CfprApSwVlanPortNsAllocStatus
_CfprApSwVlanPortNsAllocStatus_Object = MibTableColumn
cfprApSwVlanPortNsAllocStatus = _CfprApSwVlanPortNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 5),
    _CfprApSwVlanPortNsAllocStatus_Type()
)
cfprApSwVlanPortNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsAllocStatus.setStatus("current")
_CfprApSwVlanPortNsBorderVlanPortCount_Type = Gauge32
_CfprApSwVlanPortNsBorderVlanPortCount_Object = MibTableColumn
cfprApSwVlanPortNsBorderVlanPortCount = _CfprApSwVlanPortNsBorderVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 6),
    _CfprApSwVlanPortNsBorderVlanPortCount_Type()
)
cfprApSwVlanPortNsBorderVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsBorderVlanPortCount.setStatus("current")
_CfprApSwVlanPortNsConfigStatus_Type = CfprApSwConfigStatus
_CfprApSwVlanPortNsConfigStatus_Object = MibTableColumn
cfprApSwVlanPortNsConfigStatus = _CfprApSwVlanPortNsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 7),
    _CfprApSwVlanPortNsConfigStatus_Type()
)
cfprApSwVlanPortNsConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsConfigStatus.setStatus("current")
_CfprApSwVlanPortNsLimit_Type = Gauge32
_CfprApSwVlanPortNsLimit_Object = MibTableColumn
cfprApSwVlanPortNsLimit = _CfprApSwVlanPortNsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 8),
    _CfprApSwVlanPortNsLimit_Type()
)
cfprApSwVlanPortNsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsLimit.setStatus("current")
_CfprApSwVlanPortNsSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwVlanPortNsSwitchId_Object = MibTableColumn
cfprApSwVlanPortNsSwitchId = _CfprApSwVlanPortNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 9),
    _CfprApSwVlanPortNsSwitchId_Type()
)
cfprApSwVlanPortNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsSwitchId.setStatus("current")
_CfprApSwVlanPortNsTotalVlanPortCount_Type = Gauge32
_CfprApSwVlanPortNsTotalVlanPortCount_Object = MibTableColumn
cfprApSwVlanPortNsTotalVlanPortCount = _CfprApSwVlanPortNsTotalVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 10),
    _CfprApSwVlanPortNsTotalVlanPortCount_Type()
)
cfprApSwVlanPortNsTotalVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsTotalVlanPortCount.setStatus("current")
_CfprApSwVlanPortNsVlanCompOffLimit_Type = Gauge32
_CfprApSwVlanPortNsVlanCompOffLimit_Object = MibTableColumn
cfprApSwVlanPortNsVlanCompOffLimit = _CfprApSwVlanPortNsVlanCompOffLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 11),
    _CfprApSwVlanPortNsVlanCompOffLimit_Type()
)
cfprApSwVlanPortNsVlanCompOffLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsVlanCompOffLimit.setStatus("current")
_CfprApSwVlanPortNsVlanCompOnLimit_Type = Gauge32
_CfprApSwVlanPortNsVlanCompOnLimit_Object = MibTableColumn
cfprApSwVlanPortNsVlanCompOnLimit = _CfprApSwVlanPortNsVlanCompOnLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 94, 1, 12),
    _CfprApSwVlanPortNsVlanCompOnLimit_Type()
)
cfprApSwVlanPortNsVlanCompOnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsVlanCompOnLimit.setStatus("current")
_CfprApSwVlanPortNsOverrideTable_Object = MibTable
cfprApSwVlanPortNsOverrideTable = _CfprApSwVlanPortNsOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 95)
)
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsOverrideTable.setStatus("current")
_CfprApSwVlanPortNsOverrideEntry_Object = MibTableRow
cfprApSwVlanPortNsOverrideEntry = _CfprApSwVlanPortNsOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 95, 1)
)
cfprApSwVlanPortNsOverrideEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwVlanPortNsOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsOverrideEntry.setStatus("current")
_CfprApSwVlanPortNsOverrideInstanceId_Type = CfprApManagedObjectId
_CfprApSwVlanPortNsOverrideInstanceId_Object = MibTableColumn
cfprApSwVlanPortNsOverrideInstanceId = _CfprApSwVlanPortNsOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 95, 1, 1),
    _CfprApSwVlanPortNsOverrideInstanceId_Type()
)
cfprApSwVlanPortNsOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsOverrideInstanceId.setStatus("current")
_CfprApSwVlanPortNsOverrideDn_Type = CfprApManagedObjectDn
_CfprApSwVlanPortNsOverrideDn_Object = MibTableColumn
cfprApSwVlanPortNsOverrideDn = _CfprApSwVlanPortNsOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 95, 1, 2),
    _CfprApSwVlanPortNsOverrideDn_Type()
)
cfprApSwVlanPortNsOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsOverrideDn.setStatus("current")
_CfprApSwVlanPortNsOverrideRn_Type = SnmpAdminString
_CfprApSwVlanPortNsOverrideRn_Object = MibTableColumn
cfprApSwVlanPortNsOverrideRn = _CfprApSwVlanPortNsOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 95, 1, 3),
    _CfprApSwVlanPortNsOverrideRn_Type()
)
cfprApSwVlanPortNsOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsOverrideRn.setStatus("current")
_CfprApSwVlanPortNsOverrideLimit_Type = Gauge32
_CfprApSwVlanPortNsOverrideLimit_Object = MibTableColumn
cfprApSwVlanPortNsOverrideLimit = _CfprApSwVlanPortNsOverrideLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 95, 1, 4),
    _CfprApSwVlanPortNsOverrideLimit_Type()
)
cfprApSwVlanPortNsOverrideLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanPortNsOverrideLimit.setStatus("current")
_CfprApSwVlanRefTable_Object = MibTable
cfprApSwVlanRefTable = _CfprApSwVlanRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96)
)
if mibBuilder.loadTexts:
    cfprApSwVlanRefTable.setStatus("current")
_CfprApSwVlanRefEntry_Object = MibTableRow
cfprApSwVlanRefEntry = _CfprApSwVlanRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96, 1)
)
cfprApSwVlanRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwVlanRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwVlanRefEntry.setStatus("current")
_CfprApSwVlanRefInstanceId_Type = CfprApManagedObjectId
_CfprApSwVlanRefInstanceId_Object = MibTableColumn
cfprApSwVlanRefInstanceId = _CfprApSwVlanRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96, 1, 1),
    _CfprApSwVlanRefInstanceId_Type()
)
cfprApSwVlanRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwVlanRefInstanceId.setStatus("current")
_CfprApSwVlanRefDn_Type = CfprApManagedObjectDn
_CfprApSwVlanRefDn_Object = MibTableColumn
cfprApSwVlanRefDn = _CfprApSwVlanRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96, 1, 2),
    _CfprApSwVlanRefDn_Type()
)
cfprApSwVlanRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanRefDn.setStatus("current")
_CfprApSwVlanRefRn_Type = SnmpAdminString
_CfprApSwVlanRefRn_Object = MibTableColumn
cfprApSwVlanRefRn = _CfprApSwVlanRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96, 1, 3),
    _CfprApSwVlanRefRn_Type()
)
cfprApSwVlanRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanRefRn.setStatus("current")
_CfprApSwVlanRefCompressionType_Type = CfprApSwVlanCompType
_CfprApSwVlanRefCompressionType_Object = MibTableColumn
cfprApSwVlanRefCompressionType = _CfprApSwVlanRefCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96, 1, 4),
    _CfprApSwVlanRefCompressionType_Type()
)
cfprApSwVlanRefCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanRefCompressionType.setStatus("current")
_CfprApSwVlanRefConfigStatus_Type = CfprApSwVlanConfigStatusType
_CfprApSwVlanRefConfigStatus_Object = MibTableColumn
cfprApSwVlanRefConfigStatus = _CfprApSwVlanRefConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96, 1, 5),
    _CfprApSwVlanRefConfigStatus_Type()
)
cfprApSwVlanRefConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanRefConfigStatus.setStatus("current")
_CfprApSwVlanRefId_Type = Gauge32
_CfprApSwVlanRefId_Object = MibTableColumn
cfprApSwVlanRefId = _CfprApSwVlanRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96, 1, 6),
    _CfprApSwVlanRefId_Type()
)
cfprApSwVlanRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanRefId.setStatus("current")
_CfprApSwVlanRefPeerDn_Type = SnmpAdminString
_CfprApSwVlanRefPeerDn_Object = MibTableColumn
cfprApSwVlanRefPeerDn = _CfprApSwVlanRefPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 96, 1, 7),
    _CfprApSwVlanRefPeerDn_Type()
)
cfprApSwVlanRefPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVlanRefPeerDn.setStatus("current")
_CfprApSwVsanTable_Object = MibTable
cfprApSwVsanTable = _CfprApSwVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97)
)
if mibBuilder.loadTexts:
    cfprApSwVsanTable.setStatus("current")
_CfprApSwVsanEntry_Object = MibTableRow
cfprApSwVsanEntry = _CfprApSwVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1)
)
cfprApSwVsanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwVsanEntry.setStatus("current")
_CfprApSwVsanInstanceId_Type = CfprApManagedObjectId
_CfprApSwVsanInstanceId_Object = MibTableColumn
cfprApSwVsanInstanceId = _CfprApSwVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 1),
    _CfprApSwVsanInstanceId_Type()
)
cfprApSwVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwVsanInstanceId.setStatus("current")
_CfprApSwVsanDn_Type = CfprApManagedObjectDn
_CfprApSwVsanDn_Object = MibTableColumn
cfprApSwVsanDn = _CfprApSwVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 2),
    _CfprApSwVsanDn_Type()
)
cfprApSwVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanDn.setStatus("current")
_CfprApSwVsanRn_Type = SnmpAdminString
_CfprApSwVsanRn_Object = MibTableColumn
cfprApSwVsanRn = _CfprApSwVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 3),
    _CfprApSwVsanRn_Type()
)
cfprApSwVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanRn.setStatus("current")
_CfprApSwVsanDefaultZoning_Type = CfprApFabricDefaultZoningState
_CfprApSwVsanDefaultZoning_Object = MibTableColumn
cfprApSwVsanDefaultZoning = _CfprApSwVsanDefaultZoning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 4),
    _CfprApSwVsanDefaultZoning_Type()
)
cfprApSwVsanDefaultZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanDefaultZoning.setStatus("current")
_CfprApSwVsanEpDn_Type = SnmpAdminString
_CfprApSwVsanEpDn_Object = MibTableColumn
cfprApSwVsanEpDn = _CfprApSwVsanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 5),
    _CfprApSwVsanEpDn_Type()
)
cfprApSwVsanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanEpDn.setStatus("current")
_CfprApSwVsanFcZoneSharingMode_Type = CfprApFabricFcZoneSharingMode
_CfprApSwVsanFcZoneSharingMode_Object = MibTableColumn
cfprApSwVsanFcZoneSharingMode = _CfprApSwVsanFcZoneSharingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 6),
    _CfprApSwVsanFcZoneSharingMode_Type()
)
cfprApSwVsanFcZoneSharingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanFcZoneSharingMode.setStatus("current")
_CfprApSwVsanFcoeVlan_Type = Gauge32
_CfprApSwVsanFcoeVlan_Object = MibTableColumn
cfprApSwVsanFcoeVlan = _CfprApSwVsanFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 7),
    _CfprApSwVsanFcoeVlan_Type()
)
cfprApSwVsanFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanFcoeVlan.setStatus("current")
_CfprApSwVsanFltAggr_Type = Unsigned64
_CfprApSwVsanFltAggr_Object = MibTableColumn
cfprApSwVsanFltAggr = _CfprApSwVsanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 8),
    _CfprApSwVsanFltAggr_Type()
)
cfprApSwVsanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanFltAggr.setStatus("current")
_CfprApSwVsanId_Type = Gauge32
_CfprApSwVsanId_Object = MibTableColumn
cfprApSwVsanId = _CfprApSwVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 9),
    _CfprApSwVsanId_Type()
)
cfprApSwVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanId.setStatus("current")
_CfprApSwVsanIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApSwVsanIfRole_Object = MibTableColumn
cfprApSwVsanIfRole = _CfprApSwVsanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 10),
    _CfprApSwVsanIfRole_Type()
)
cfprApSwVsanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanIfRole.setStatus("current")
_CfprApSwVsanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApSwVsanIfType_Object = MibTableColumn
cfprApSwVsanIfType = _CfprApSwVsanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 11),
    _CfprApSwVsanIfType_Type()
)
cfprApSwVsanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanIfType.setStatus("current")
_CfprApSwVsanLc_Type = CfprApFsmLifecycle
_CfprApSwVsanLc_Object = MibTableColumn
cfprApSwVsanLc = _CfprApSwVsanLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 12),
    _CfprApSwVsanLc_Type()
)
cfprApSwVsanLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanLc.setStatus("current")
_CfprApSwVsanLocale_Type = CfprApFabricVnetEpLocale
_CfprApSwVsanLocale_Object = MibTableColumn
cfprApSwVsanLocale = _CfprApSwVsanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 13),
    _CfprApSwVsanLocale_Type()
)
cfprApSwVsanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanLocale.setStatus("current")
_CfprApSwVsanMonTrafDir_Type = CfprApFabricTrafficDirection
_CfprApSwVsanMonTrafDir_Object = MibTableColumn
cfprApSwVsanMonTrafDir = _CfprApSwVsanMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 14),
    _CfprApSwVsanMonTrafDir_Type()
)
cfprApSwVsanMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanMonTrafDir.setStatus("current")
_CfprApSwVsanName_Type = SnmpAdminString
_CfprApSwVsanName_Object = MibTableColumn
cfprApSwVsanName = _CfprApSwVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 15),
    _CfprApSwVsanName_Type()
)
cfprApSwVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanName.setStatus("current")
_CfprApSwVsanOperState_Type = CfprApFabricVsanOperState
_CfprApSwVsanOperState_Object = MibTableColumn
cfprApSwVsanOperState = _CfprApSwVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 16),
    _CfprApSwVsanOperState_Type()
)
cfprApSwVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanOperState.setStatus("current")
_CfprApSwVsanPeerDn_Type = SnmpAdminString
_CfprApSwVsanPeerDn_Object = MibTableColumn
cfprApSwVsanPeerDn = _CfprApSwVsanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 17),
    _CfprApSwVsanPeerDn_Type()
)
cfprApSwVsanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanPeerDn.setStatus("current")
_CfprApSwVsanPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApSwVsanPolicyOwner_Object = MibTableColumn
cfprApSwVsanPolicyOwner = _CfprApSwVsanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 18),
    _CfprApSwVsanPolicyOwner_Type()
)
cfprApSwVsanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanPolicyOwner.setStatus("current")
_CfprApSwVsanSwitchId_Type = CfprApNetworkSwitchId
_CfprApSwVsanSwitchId_Object = MibTableColumn
cfprApSwVsanSwitchId = _CfprApSwVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 19),
    _CfprApSwVsanSwitchId_Type()
)
cfprApSwVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanSwitchId.setStatus("current")
_CfprApSwVsanTransport_Type = CfprApFabricAVsanTransport
_CfprApSwVsanTransport_Object = MibTableColumn
cfprApSwVsanTransport = _CfprApSwVsanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 20),
    _CfprApSwVsanTransport_Type()
)
cfprApSwVsanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanTransport.setStatus("current")
_CfprApSwVsanType_Type = CfprApFabricAVsanType
_CfprApSwVsanType_Object = MibTableColumn
cfprApSwVsanType = _CfprApSwVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 21),
    _CfprApSwVsanType_Type()
)
cfprApSwVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanType.setStatus("current")
_CfprApSwVsanZoningState_Type = CfprApFabricZoningState
_CfprApSwVsanZoningState_Object = MibTableColumn
cfprApSwVsanZoningState = _CfprApSwVsanZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 97, 1, 22),
    _CfprApSwVsanZoningState_Type()
)
cfprApSwVsanZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwVsanZoningState.setStatus("current")
_CfprApSwZoneInitiatorMemberTable_Object = MibTable
cfprApSwZoneInitiatorMemberTable = _CfprApSwZoneInitiatorMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98)
)
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberTable.setStatus("current")
_CfprApSwZoneInitiatorMemberEntry_Object = MibTableRow
cfprApSwZoneInitiatorMemberEntry = _CfprApSwZoneInitiatorMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1)
)
cfprApSwZoneInitiatorMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwZoneInitiatorMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberEntry.setStatus("current")
_CfprApSwZoneInitiatorMemberInstanceId_Type = CfprApManagedObjectId
_CfprApSwZoneInitiatorMemberInstanceId_Object = MibTableColumn
cfprApSwZoneInitiatorMemberInstanceId = _CfprApSwZoneInitiatorMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1, 1),
    _CfprApSwZoneInitiatorMemberInstanceId_Type()
)
cfprApSwZoneInitiatorMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberInstanceId.setStatus("current")
_CfprApSwZoneInitiatorMemberDn_Type = CfprApManagedObjectDn
_CfprApSwZoneInitiatorMemberDn_Object = MibTableColumn
cfprApSwZoneInitiatorMemberDn = _CfprApSwZoneInitiatorMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1, 2),
    _CfprApSwZoneInitiatorMemberDn_Type()
)
cfprApSwZoneInitiatorMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberDn.setStatus("current")
_CfprApSwZoneInitiatorMemberRn_Type = SnmpAdminString
_CfprApSwZoneInitiatorMemberRn_Object = MibTableColumn
cfprApSwZoneInitiatorMemberRn = _CfprApSwZoneInitiatorMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1, 3),
    _CfprApSwZoneInitiatorMemberRn_Type()
)
cfprApSwZoneInitiatorMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberRn.setStatus("current")
_CfprApSwZoneInitiatorMemberEpDn_Type = SnmpAdminString
_CfprApSwZoneInitiatorMemberEpDn_Object = MibTableColumn
cfprApSwZoneInitiatorMemberEpDn = _CfprApSwZoneInitiatorMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1, 4),
    _CfprApSwZoneInitiatorMemberEpDn_Type()
)
cfprApSwZoneInitiatorMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberEpDn.setStatus("current")
_CfprApSwZoneInitiatorMemberLc_Type = CfprApSwFcZoneMemberLc
_CfprApSwZoneInitiatorMemberLc_Object = MibTableColumn
cfprApSwZoneInitiatorMemberLc = _CfprApSwZoneInitiatorMemberLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1, 5),
    _CfprApSwZoneInitiatorMemberLc_Type()
)
cfprApSwZoneInitiatorMemberLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberLc.setStatus("current")
_CfprApSwZoneInitiatorMemberName_Type = SnmpAdminString
_CfprApSwZoneInitiatorMemberName_Object = MibTableColumn
cfprApSwZoneInitiatorMemberName = _CfprApSwZoneInitiatorMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1, 6),
    _CfprApSwZoneInitiatorMemberName_Type()
)
cfprApSwZoneInitiatorMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberName.setStatus("current")
_CfprApSwZoneInitiatorMemberPeerDn_Type = SnmpAdminString
_CfprApSwZoneInitiatorMemberPeerDn_Object = MibTableColumn
cfprApSwZoneInitiatorMemberPeerDn = _CfprApSwZoneInitiatorMemberPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1, 7),
    _CfprApSwZoneInitiatorMemberPeerDn_Type()
)
cfprApSwZoneInitiatorMemberPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberPeerDn.setStatus("current")
_CfprApSwZoneInitiatorMemberWwpn_Type = Unsigned64
_CfprApSwZoneInitiatorMemberWwpn_Object = MibTableColumn
cfprApSwZoneInitiatorMemberWwpn = _CfprApSwZoneInitiatorMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 98, 1, 8),
    _CfprApSwZoneInitiatorMemberWwpn_Type()
)
cfprApSwZoneInitiatorMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneInitiatorMemberWwpn.setStatus("current")
_CfprApSwZoneTargetMemberTable_Object = MibTable
cfprApSwZoneTargetMemberTable = _CfprApSwZoneTargetMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99)
)
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberTable.setStatus("current")
_CfprApSwZoneTargetMemberEntry_Object = MibTableRow
cfprApSwZoneTargetMemberEntry = _CfprApSwZoneTargetMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1)
)
cfprApSwZoneTargetMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SW-MIB", "cfprApSwZoneTargetMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberEntry.setStatus("current")
_CfprApSwZoneTargetMemberInstanceId_Type = CfprApManagedObjectId
_CfprApSwZoneTargetMemberInstanceId_Object = MibTableColumn
cfprApSwZoneTargetMemberInstanceId = _CfprApSwZoneTargetMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1, 1),
    _CfprApSwZoneTargetMemberInstanceId_Type()
)
cfprApSwZoneTargetMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberInstanceId.setStatus("current")
_CfprApSwZoneTargetMemberDn_Type = CfprApManagedObjectDn
_CfprApSwZoneTargetMemberDn_Object = MibTableColumn
cfprApSwZoneTargetMemberDn = _CfprApSwZoneTargetMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1, 2),
    _CfprApSwZoneTargetMemberDn_Type()
)
cfprApSwZoneTargetMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberDn.setStatus("current")
_CfprApSwZoneTargetMemberRn_Type = SnmpAdminString
_CfprApSwZoneTargetMemberRn_Object = MibTableColumn
cfprApSwZoneTargetMemberRn = _CfprApSwZoneTargetMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1, 3),
    _CfprApSwZoneTargetMemberRn_Type()
)
cfprApSwZoneTargetMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberRn.setStatus("current")
_CfprApSwZoneTargetMemberEpDn_Type = SnmpAdminString
_CfprApSwZoneTargetMemberEpDn_Object = MibTableColumn
cfprApSwZoneTargetMemberEpDn = _CfprApSwZoneTargetMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1, 4),
    _CfprApSwZoneTargetMemberEpDn_Type()
)
cfprApSwZoneTargetMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberEpDn.setStatus("current")
_CfprApSwZoneTargetMemberLc_Type = CfprApSwFcZoneMemberLc
_CfprApSwZoneTargetMemberLc_Object = MibTableColumn
cfprApSwZoneTargetMemberLc = _CfprApSwZoneTargetMemberLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1, 5),
    _CfprApSwZoneTargetMemberLc_Type()
)
cfprApSwZoneTargetMemberLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberLc.setStatus("current")
_CfprApSwZoneTargetMemberName_Type = SnmpAdminString
_CfprApSwZoneTargetMemberName_Object = MibTableColumn
cfprApSwZoneTargetMemberName = _CfprApSwZoneTargetMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1, 6),
    _CfprApSwZoneTargetMemberName_Type()
)
cfprApSwZoneTargetMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberName.setStatus("current")
_CfprApSwZoneTargetMemberPeerDn_Type = SnmpAdminString
_CfprApSwZoneTargetMemberPeerDn_Object = MibTableColumn
cfprApSwZoneTargetMemberPeerDn = _CfprApSwZoneTargetMemberPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1, 7),
    _CfprApSwZoneTargetMemberPeerDn_Type()
)
cfprApSwZoneTargetMemberPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberPeerDn.setStatus("current")
_CfprApSwZoneTargetMemberWwpn_Type = Unsigned64
_CfprApSwZoneTargetMemberWwpn_Object = MibTableColumn
cfprApSwZoneTargetMemberWwpn = _CfprApSwZoneTargetMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 75, 99, 1, 8),
    _CfprApSwZoneTargetMemberWwpn_Type()
)
cfprApSwZoneTargetMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSwZoneTargetMemberWwpn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-SW-MIB",
    **{"cfprApSwObjects": cfprApSwObjects,
       "cfprApSwAccessDomainTable": cfprApSwAccessDomainTable,
       "cfprApSwAccessDomainEntry": cfprApSwAccessDomainEntry,
       "cfprApSwAccessDomainInstanceId": cfprApSwAccessDomainInstanceId,
       "cfprApSwAccessDomainDn": cfprApSwAccessDomainDn,
       "cfprApSwAccessDomainRn": cfprApSwAccessDomainRn,
       "cfprApSwAccessDomainFsmDescr": cfprApSwAccessDomainFsmDescr,
       "cfprApSwAccessDomainFsmPrev": cfprApSwAccessDomainFsmPrev,
       "cfprApSwAccessDomainFsmProgr": cfprApSwAccessDomainFsmProgr,
       "cfprApSwAccessDomainFsmRmtInvErrCode": cfprApSwAccessDomainFsmRmtInvErrCode,
       "cfprApSwAccessDomainFsmRmtInvErrDescr": cfprApSwAccessDomainFsmRmtInvErrDescr,
       "cfprApSwAccessDomainFsmRmtInvRslt": cfprApSwAccessDomainFsmRmtInvRslt,
       "cfprApSwAccessDomainFsmStageDescr": cfprApSwAccessDomainFsmStageDescr,
       "cfprApSwAccessDomainFsmStamp": cfprApSwAccessDomainFsmStamp,
       "cfprApSwAccessDomainFsmStatus": cfprApSwAccessDomainFsmStatus,
       "cfprApSwAccessDomainFsmTry": cfprApSwAccessDomainFsmTry,
       "cfprApSwAccessDomainLocale": cfprApSwAccessDomainLocale,
       "cfprApSwAccessDomainName": cfprApSwAccessDomainName,
       "cfprApSwAccessDomainSwitchId": cfprApSwAccessDomainSwitchId,
       "cfprApSwAccessDomainTransport": cfprApSwAccessDomainTransport,
       "cfprApSwAccessDomainType": cfprApSwAccessDomainType,
       "cfprApSwAccessDomainFsmTable": cfprApSwAccessDomainFsmTable,
       "cfprApSwAccessDomainFsmEntry": cfprApSwAccessDomainFsmEntry,
       "cfprApSwAccessDomainFsmInstanceId": cfprApSwAccessDomainFsmInstanceId,
       "cfprApSwAccessDomainFsmDn": cfprApSwAccessDomainFsmDn,
       "cfprApSwAccessDomainFsmRn": cfprApSwAccessDomainFsmRn,
       "cfprApSwAccessDomainFsmCompletionTime": cfprApSwAccessDomainFsmCompletionTime,
       "cfprApSwAccessDomainFsmCurrentFsm": cfprApSwAccessDomainFsmCurrentFsm,
       "cfprApSwAccessDomainFsmDescrData": cfprApSwAccessDomainFsmDescrData,
       "cfprApSwAccessDomainFsmFsmStatus": cfprApSwAccessDomainFsmFsmStatus,
       "cfprApSwAccessDomainFsmProgress": cfprApSwAccessDomainFsmProgress,
       "cfprApSwAccessDomainFsmRmtErrCode": cfprApSwAccessDomainFsmRmtErrCode,
       "cfprApSwAccessDomainFsmRmtErrDescr": cfprApSwAccessDomainFsmRmtErrDescr,
       "cfprApSwAccessDomainFsmRmtRslt": cfprApSwAccessDomainFsmRmtRslt,
       "cfprApSwAccessDomainFsmStageTable": cfprApSwAccessDomainFsmStageTable,
       "cfprApSwAccessDomainFsmStageEntry": cfprApSwAccessDomainFsmStageEntry,
       "cfprApSwAccessDomainFsmStageInstanceId": cfprApSwAccessDomainFsmStageInstanceId,
       "cfprApSwAccessDomainFsmStageDn": cfprApSwAccessDomainFsmStageDn,
       "cfprApSwAccessDomainFsmStageRn": cfprApSwAccessDomainFsmStageRn,
       "cfprApSwAccessDomainFsmStageDescrData": cfprApSwAccessDomainFsmStageDescrData,
       "cfprApSwAccessDomainFsmStageLastUpdateTime": cfprApSwAccessDomainFsmStageLastUpdateTime,
       "cfprApSwAccessDomainFsmStageName": cfprApSwAccessDomainFsmStageName,
       "cfprApSwAccessDomainFsmStageOrder": cfprApSwAccessDomainFsmStageOrder,
       "cfprApSwAccessDomainFsmStageRetry": cfprApSwAccessDomainFsmStageRetry,
       "cfprApSwAccessDomainFsmStageStageStatus": cfprApSwAccessDomainFsmStageStageStatus,
       "cfprApSwAccessDomainFsmTaskTable": cfprApSwAccessDomainFsmTaskTable,
       "cfprApSwAccessDomainFsmTaskEntry": cfprApSwAccessDomainFsmTaskEntry,
       "cfprApSwAccessDomainFsmTaskInstanceId": cfprApSwAccessDomainFsmTaskInstanceId,
       "cfprApSwAccessDomainFsmTaskDn": cfprApSwAccessDomainFsmTaskDn,
       "cfprApSwAccessDomainFsmTaskRn": cfprApSwAccessDomainFsmTaskRn,
       "cfprApSwAccessDomainFsmTaskCompletion": cfprApSwAccessDomainFsmTaskCompletion,
       "cfprApSwAccessDomainFsmTaskFlags": cfprApSwAccessDomainFsmTaskFlags,
       "cfprApSwAccessDomainFsmTaskItem": cfprApSwAccessDomainFsmTaskItem,
       "cfprApSwAccessDomainFsmTaskSeqId": cfprApSwAccessDomainFsmTaskSeqId,
       "cfprApSwAccessEpTable": cfprApSwAccessEpTable,
       "cfprApSwAccessEpEntry": cfprApSwAccessEpEntry,
       "cfprApSwAccessEpInstanceId": cfprApSwAccessEpInstanceId,
       "cfprApSwAccessEpDn": cfprApSwAccessEpDn,
       "cfprApSwAccessEpRn": cfprApSwAccessEpRn,
       "cfprApSwAccessEpAdminState": cfprApSwAccessEpAdminState,
       "cfprApSwAccessEpAggrPortId": cfprApSwAccessEpAggrPortId,
       "cfprApSwAccessEpChassisId": cfprApSwAccessEpChassisId,
       "cfprApSwAccessEpEncap": cfprApSwAccessEpEncap,
       "cfprApSwAccessEpEpDn": cfprApSwAccessEpEpDn,
       "cfprApSwAccessEpIfRole": cfprApSwAccessEpIfRole,
       "cfprApSwAccessEpIfType": cfprApSwAccessEpIfType,
       "cfprApSwAccessEpLc": cfprApSwAccessEpLc,
       "cfprApSwAccessEpLocale": cfprApSwAccessEpLocale,
       "cfprApSwAccessEpName": cfprApSwAccessEpName,
       "cfprApSwAccessEpNsSize": cfprApSwAccessEpNsSize,
       "cfprApSwAccessEpPeerAggrPortId": cfprApSwAccessEpPeerAggrPortId,
       "cfprApSwAccessEpPeerChassisId": cfprApSwAccessEpPeerChassisId,
       "cfprApSwAccessEpPeerDn": cfprApSwAccessEpPeerDn,
       "cfprApSwAccessEpPeerPortId": cfprApSwAccessEpPeerPortId,
       "cfprApSwAccessEpPeerSlotId": cfprApSwAccessEpPeerSlotId,
       "cfprApSwAccessEpPortId": cfprApSwAccessEpPortId,
       "cfprApSwAccessEpSlotId": cfprApSwAccessEpSlotId,
       "cfprApSwAccessEpSwitchId": cfprApSwAccessEpSwitchId,
       "cfprApSwAccessEpTransport": cfprApSwAccessEpTransport,
       "cfprApSwAccessEpType": cfprApSwAccessEpType,
       "cfprApSwCardEnvStatsTable": cfprApSwCardEnvStatsTable,
       "cfprApSwCardEnvStatsEntry": cfprApSwCardEnvStatsEntry,
       "cfprApSwCardEnvStatsInstanceId": cfprApSwCardEnvStatsInstanceId,
       "cfprApSwCardEnvStatsDn": cfprApSwCardEnvStatsDn,
       "cfprApSwCardEnvStatsRn": cfprApSwCardEnvStatsRn,
       "cfprApSwCardEnvStatsSlotOutlet1": cfprApSwCardEnvStatsSlotOutlet1,
       "cfprApSwCardEnvStatsSlotOutlet1Avg": cfprApSwCardEnvStatsSlotOutlet1Avg,
       "cfprApSwCardEnvStatsSlotOutlet1Max": cfprApSwCardEnvStatsSlotOutlet1Max,
       "cfprApSwCardEnvStatsSlotOutlet1Min": cfprApSwCardEnvStatsSlotOutlet1Min,
       "cfprApSwCardEnvStatsSlotOutlet2": cfprApSwCardEnvStatsSlotOutlet2,
       "cfprApSwCardEnvStatsSlotOutlet2Avg": cfprApSwCardEnvStatsSlotOutlet2Avg,
       "cfprApSwCardEnvStatsSlotOutlet2Max": cfprApSwCardEnvStatsSlotOutlet2Max,
       "cfprApSwCardEnvStatsSlotOutlet2Min": cfprApSwCardEnvStatsSlotOutlet2Min,
       "cfprApSwCardEnvStatsSlotOutlet3": cfprApSwCardEnvStatsSlotOutlet3,
       "cfprApSwCardEnvStatsSlotOutlet3Avg": cfprApSwCardEnvStatsSlotOutlet3Avg,
       "cfprApSwCardEnvStatsSlotOutlet3Max": cfprApSwCardEnvStatsSlotOutlet3Max,
       "cfprApSwCardEnvStatsSlotOutlet3Min": cfprApSwCardEnvStatsSlotOutlet3Min,
       "cfprApSwCardEnvStatsIntervals": cfprApSwCardEnvStatsIntervals,
       "cfprApSwCardEnvStatsSuspect": cfprApSwCardEnvStatsSuspect,
       "cfprApSwCardEnvStatsThresholded": cfprApSwCardEnvStatsThresholded,
       "cfprApSwCardEnvStatsTimeCollected": cfprApSwCardEnvStatsTimeCollected,
       "cfprApSwCardEnvStatsUpdate": cfprApSwCardEnvStatsUpdate,
       "cfprApSwCardEnvStatsHistTable": cfprApSwCardEnvStatsHistTable,
       "cfprApSwCardEnvStatsHistEntry": cfprApSwCardEnvStatsHistEntry,
       "cfprApSwCardEnvStatsHistInstanceId": cfprApSwCardEnvStatsHistInstanceId,
       "cfprApSwCardEnvStatsHistDn": cfprApSwCardEnvStatsHistDn,
       "cfprApSwCardEnvStatsHistRn": cfprApSwCardEnvStatsHistRn,
       "cfprApSwCardEnvStatsHistSlotOutlet1": cfprApSwCardEnvStatsHistSlotOutlet1,
       "cfprApSwCardEnvStatsHistSlotOutlet1Avg": cfprApSwCardEnvStatsHistSlotOutlet1Avg,
       "cfprApSwCardEnvStatsHistSlotOutlet1Max": cfprApSwCardEnvStatsHistSlotOutlet1Max,
       "cfprApSwCardEnvStatsHistSlotOutlet1Min": cfprApSwCardEnvStatsHistSlotOutlet1Min,
       "cfprApSwCardEnvStatsHistSlotOutlet2": cfprApSwCardEnvStatsHistSlotOutlet2,
       "cfprApSwCardEnvStatsHistSlotOutlet2Avg": cfprApSwCardEnvStatsHistSlotOutlet2Avg,
       "cfprApSwCardEnvStatsHistSlotOutlet2Max": cfprApSwCardEnvStatsHistSlotOutlet2Max,
       "cfprApSwCardEnvStatsHistSlotOutlet2Min": cfprApSwCardEnvStatsHistSlotOutlet2Min,
       "cfprApSwCardEnvStatsHistSlotOutlet3": cfprApSwCardEnvStatsHistSlotOutlet3,
       "cfprApSwCardEnvStatsHistSlotOutlet3Avg": cfprApSwCardEnvStatsHistSlotOutlet3Avg,
       "cfprApSwCardEnvStatsHistSlotOutlet3Max": cfprApSwCardEnvStatsHistSlotOutlet3Max,
       "cfprApSwCardEnvStatsHistSlotOutlet3Min": cfprApSwCardEnvStatsHistSlotOutlet3Min,
       "cfprApSwCardEnvStatsHistId": cfprApSwCardEnvStatsHistId,
       "cfprApSwCardEnvStatsHistMostRecent": cfprApSwCardEnvStatsHistMostRecent,
       "cfprApSwCardEnvStatsHistSuspect": cfprApSwCardEnvStatsHistSuspect,
       "cfprApSwCardEnvStatsHistThresholded": cfprApSwCardEnvStatsHistThresholded,
       "cfprApSwCardEnvStatsHistTimeCollected": cfprApSwCardEnvStatsHistTimeCollected,
       "cfprApSwCmclanTable": cfprApSwCmclanTable,
       "cfprApSwCmclanEntry": cfprApSwCmclanEntry,
       "cfprApSwCmclanInstanceId": cfprApSwCmclanInstanceId,
       "cfprApSwCmclanDn": cfprApSwCmclanDn,
       "cfprApSwCmclanRn": cfprApSwCmclanRn,
       "cfprApSwCmclanCimcIds": cfprApSwCmclanCimcIds,
       "cfprApSwCmclanEpDn": cfprApSwCmclanEpDn,
       "cfprApSwCmclanId": cfprApSwCmclanId,
       "cfprApSwCmclanIfRole": cfprApSwCmclanIfRole,
       "cfprApSwCmclanIfType": cfprApSwCmclanIfType,
       "cfprApSwCmclanLocale": cfprApSwCmclanLocale,
       "cfprApSwCmclanName": cfprApSwCmclanName,
       "cfprApSwCmclanPeerDn": cfprApSwCmclanPeerDn,
       "cfprApSwCmclanTransport": cfprApSwCmclanTransport,
       "cfprApSwCmclanType": cfprApSwCmclanType,
       "cfprApSwEnvStatsTable": cfprApSwEnvStatsTable,
       "cfprApSwEnvStatsEntry": cfprApSwEnvStatsEntry,
       "cfprApSwEnvStatsInstanceId": cfprApSwEnvStatsInstanceId,
       "cfprApSwEnvStatsDn": cfprApSwEnvStatsDn,
       "cfprApSwEnvStatsRn": cfprApSwEnvStatsRn,
       "cfprApSwEnvStatsFanCtrlrInlet1": cfprApSwEnvStatsFanCtrlrInlet1,
       "cfprApSwEnvStatsFanCtrlrInlet1Avg": cfprApSwEnvStatsFanCtrlrInlet1Avg,
       "cfprApSwEnvStatsFanCtrlrInlet1Max": cfprApSwEnvStatsFanCtrlrInlet1Max,
       "cfprApSwEnvStatsFanCtrlrInlet1Min": cfprApSwEnvStatsFanCtrlrInlet1Min,
       "cfprApSwEnvStatsFanCtrlrInlet2": cfprApSwEnvStatsFanCtrlrInlet2,
       "cfprApSwEnvStatsFanCtrlrInlet2Avg": cfprApSwEnvStatsFanCtrlrInlet2Avg,
       "cfprApSwEnvStatsFanCtrlrInlet2Max": cfprApSwEnvStatsFanCtrlrInlet2Max,
       "cfprApSwEnvStatsFanCtrlrInlet2Min": cfprApSwEnvStatsFanCtrlrInlet2Min,
       "cfprApSwEnvStatsFanCtrlrInlet3": cfprApSwEnvStatsFanCtrlrInlet3,
       "cfprApSwEnvStatsFanCtrlrInlet3Avg": cfprApSwEnvStatsFanCtrlrInlet3Avg,
       "cfprApSwEnvStatsFanCtrlrInlet3Max": cfprApSwEnvStatsFanCtrlrInlet3Max,
       "cfprApSwEnvStatsFanCtrlrInlet3Min": cfprApSwEnvStatsFanCtrlrInlet3Min,
       "cfprApSwEnvStatsFanCtrlrInlet4": cfprApSwEnvStatsFanCtrlrInlet4,
       "cfprApSwEnvStatsFanCtrlrInlet4Avg": cfprApSwEnvStatsFanCtrlrInlet4Avg,
       "cfprApSwEnvStatsFanCtrlrInlet4Max": cfprApSwEnvStatsFanCtrlrInlet4Max,
       "cfprApSwEnvStatsFanCtrlrInlet4Min": cfprApSwEnvStatsFanCtrlrInlet4Min,
       "cfprApSwEnvStatsIntervals": cfprApSwEnvStatsIntervals,
       "cfprApSwEnvStatsMainBoardOutlet1": cfprApSwEnvStatsMainBoardOutlet1,
       "cfprApSwEnvStatsMainBoardOutlet1Avg": cfprApSwEnvStatsMainBoardOutlet1Avg,
       "cfprApSwEnvStatsMainBoardOutlet1Max": cfprApSwEnvStatsMainBoardOutlet1Max,
       "cfprApSwEnvStatsMainBoardOutlet1Min": cfprApSwEnvStatsMainBoardOutlet1Min,
       "cfprApSwEnvStatsMainBoardOutlet2": cfprApSwEnvStatsMainBoardOutlet2,
       "cfprApSwEnvStatsMainBoardOutlet2Avg": cfprApSwEnvStatsMainBoardOutlet2Avg,
       "cfprApSwEnvStatsMainBoardOutlet2Max": cfprApSwEnvStatsMainBoardOutlet2Max,
       "cfprApSwEnvStatsMainBoardOutlet2Min": cfprApSwEnvStatsMainBoardOutlet2Min,
       "cfprApSwEnvStatsPsuCtrlrInlet1": cfprApSwEnvStatsPsuCtrlrInlet1,
       "cfprApSwEnvStatsPsuCtrlrInlet1Avg": cfprApSwEnvStatsPsuCtrlrInlet1Avg,
       "cfprApSwEnvStatsPsuCtrlrInlet1Max": cfprApSwEnvStatsPsuCtrlrInlet1Max,
       "cfprApSwEnvStatsPsuCtrlrInlet1Min": cfprApSwEnvStatsPsuCtrlrInlet1Min,
       "cfprApSwEnvStatsPsuCtrlrInlet2": cfprApSwEnvStatsPsuCtrlrInlet2,
       "cfprApSwEnvStatsPsuCtrlrInlet2Avg": cfprApSwEnvStatsPsuCtrlrInlet2Avg,
       "cfprApSwEnvStatsPsuCtrlrInlet2Max": cfprApSwEnvStatsPsuCtrlrInlet2Max,
       "cfprApSwEnvStatsPsuCtrlrInlet2Min": cfprApSwEnvStatsPsuCtrlrInlet2Min,
       "cfprApSwEnvStatsSuspect": cfprApSwEnvStatsSuspect,
       "cfprApSwEnvStatsThresholded": cfprApSwEnvStatsThresholded,
       "cfprApSwEnvStatsTimeCollected": cfprApSwEnvStatsTimeCollected,
       "cfprApSwEnvStatsUpdate": cfprApSwEnvStatsUpdate,
       "cfprApSwEnvStatsHistTable": cfprApSwEnvStatsHistTable,
       "cfprApSwEnvStatsHistEntry": cfprApSwEnvStatsHistEntry,
       "cfprApSwEnvStatsHistInstanceId": cfprApSwEnvStatsHistInstanceId,
       "cfprApSwEnvStatsHistDn": cfprApSwEnvStatsHistDn,
       "cfprApSwEnvStatsHistRn": cfprApSwEnvStatsHistRn,
       "cfprApSwEnvStatsHistFanCtrlrInlet1": cfprApSwEnvStatsHistFanCtrlrInlet1,
       "cfprApSwEnvStatsHistFanCtrlrInlet1Avg": cfprApSwEnvStatsHistFanCtrlrInlet1Avg,
       "cfprApSwEnvStatsHistFanCtrlrInlet1Max": cfprApSwEnvStatsHistFanCtrlrInlet1Max,
       "cfprApSwEnvStatsHistFanCtrlrInlet1Min": cfprApSwEnvStatsHistFanCtrlrInlet1Min,
       "cfprApSwEnvStatsHistFanCtrlrInlet2": cfprApSwEnvStatsHistFanCtrlrInlet2,
       "cfprApSwEnvStatsHistFanCtrlrInlet2Avg": cfprApSwEnvStatsHistFanCtrlrInlet2Avg,
       "cfprApSwEnvStatsHistFanCtrlrInlet2Max": cfprApSwEnvStatsHistFanCtrlrInlet2Max,
       "cfprApSwEnvStatsHistFanCtrlrInlet2Min": cfprApSwEnvStatsHistFanCtrlrInlet2Min,
       "cfprApSwEnvStatsHistFanCtrlrInlet3": cfprApSwEnvStatsHistFanCtrlrInlet3,
       "cfprApSwEnvStatsHistFanCtrlrInlet3Avg": cfprApSwEnvStatsHistFanCtrlrInlet3Avg,
       "cfprApSwEnvStatsHistFanCtrlrInlet3Max": cfprApSwEnvStatsHistFanCtrlrInlet3Max,
       "cfprApSwEnvStatsHistFanCtrlrInlet3Min": cfprApSwEnvStatsHistFanCtrlrInlet3Min,
       "cfprApSwEnvStatsHistFanCtrlrInlet4": cfprApSwEnvStatsHistFanCtrlrInlet4,
       "cfprApSwEnvStatsHistFanCtrlrInlet4Avg": cfprApSwEnvStatsHistFanCtrlrInlet4Avg,
       "cfprApSwEnvStatsHistFanCtrlrInlet4Max": cfprApSwEnvStatsHistFanCtrlrInlet4Max,
       "cfprApSwEnvStatsHistFanCtrlrInlet4Min": cfprApSwEnvStatsHistFanCtrlrInlet4Min,
       "cfprApSwEnvStatsHistId": cfprApSwEnvStatsHistId,
       "cfprApSwEnvStatsHistMainBoardOutlet1": cfprApSwEnvStatsHistMainBoardOutlet1,
       "cfprApSwEnvStatsHistMainBoardOutlet1Avg": cfprApSwEnvStatsHistMainBoardOutlet1Avg,
       "cfprApSwEnvStatsHistMainBoardOutlet1Max": cfprApSwEnvStatsHistMainBoardOutlet1Max,
       "cfprApSwEnvStatsHistMainBoardOutlet1Min": cfprApSwEnvStatsHistMainBoardOutlet1Min,
       "cfprApSwEnvStatsHistMainBoardOutlet2": cfprApSwEnvStatsHistMainBoardOutlet2,
       "cfprApSwEnvStatsHistMainBoardOutlet2Avg": cfprApSwEnvStatsHistMainBoardOutlet2Avg,
       "cfprApSwEnvStatsHistMainBoardOutlet2Max": cfprApSwEnvStatsHistMainBoardOutlet2Max,
       "cfprApSwEnvStatsHistMainBoardOutlet2Min": cfprApSwEnvStatsHistMainBoardOutlet2Min,
       "cfprApSwEnvStatsHistMostRecent": cfprApSwEnvStatsHistMostRecent,
       "cfprApSwEnvStatsHistPsuCtrlrInlet1": cfprApSwEnvStatsHistPsuCtrlrInlet1,
       "cfprApSwEnvStatsHistPsuCtrlrInlet1Avg": cfprApSwEnvStatsHistPsuCtrlrInlet1Avg,
       "cfprApSwEnvStatsHistPsuCtrlrInlet1Max": cfprApSwEnvStatsHistPsuCtrlrInlet1Max,
       "cfprApSwEnvStatsHistPsuCtrlrInlet1Min": cfprApSwEnvStatsHistPsuCtrlrInlet1Min,
       "cfprApSwEnvStatsHistPsuCtrlrInlet2": cfprApSwEnvStatsHistPsuCtrlrInlet2,
       "cfprApSwEnvStatsHistPsuCtrlrInlet2Avg": cfprApSwEnvStatsHistPsuCtrlrInlet2Avg,
       "cfprApSwEnvStatsHistPsuCtrlrInlet2Max": cfprApSwEnvStatsHistPsuCtrlrInlet2Max,
       "cfprApSwEnvStatsHistPsuCtrlrInlet2Min": cfprApSwEnvStatsHistPsuCtrlrInlet2Min,
       "cfprApSwEnvStatsHistSuspect": cfprApSwEnvStatsHistSuspect,
       "cfprApSwEnvStatsHistThresholded": cfprApSwEnvStatsHistThresholded,
       "cfprApSwEnvStatsHistTimeCollected": cfprApSwEnvStatsHistTimeCollected,
       "cfprApSwEthEstcEpTable": cfprApSwEthEstcEpTable,
       "cfprApSwEthEstcEpEntry": cfprApSwEthEstcEpEntry,
       "cfprApSwEthEstcEpInstanceId": cfprApSwEthEstcEpInstanceId,
       "cfprApSwEthEstcEpDn": cfprApSwEthEstcEpDn,
       "cfprApSwEthEstcEpRn": cfprApSwEthEstcEpRn,
       "cfprApSwEthEstcEpAdminSpeed": cfprApSwEthEstcEpAdminSpeed,
       "cfprApSwEthEstcEpAdminState": cfprApSwEthEstcEpAdminState,
       "cfprApSwEthEstcEpAggrPortId": cfprApSwEthEstcEpAggrPortId,
       "cfprApSwEthEstcEpBorderAggrPortId": cfprApSwEthEstcEpBorderAggrPortId,
       "cfprApSwEthEstcEpBorderPortId": cfprApSwEthEstcEpBorderPortId,
       "cfprApSwEthEstcEpBorderSlotId": cfprApSwEthEstcEpBorderSlotId,
       "cfprApSwEthEstcEpCdp": cfprApSwEthEstcEpCdp,
       "cfprApSwEthEstcEpChassisId": cfprApSwEthEstcEpChassisId,
       "cfprApSwEthEstcEpCosValue": cfprApSwEthEstcEpCosValue,
       "cfprApSwEthEstcEpEpDn": cfprApSwEthEstcEpEpDn,
       "cfprApSwEthEstcEpForgeMac": cfprApSwEthEstcEpForgeMac,
       "cfprApSwEthEstcEpIfRole": cfprApSwEthEstcEpIfRole,
       "cfprApSwEthEstcEpIfType": cfprApSwEthEstcEpIfType,
       "cfprApSwEthEstcEpLc": cfprApSwEthEstcEpLc,
       "cfprApSwEthEstcEpLocale": cfprApSwEthEstcEpLocale,
       "cfprApSwEthEstcEpName": cfprApSwEthEstcEpName,
       "cfprApSwEthEstcEpPcId": cfprApSwEthEstcEpPcId,
       "cfprApSwEthEstcEpPeerAggrPortId": cfprApSwEthEstcEpPeerAggrPortId,
       "cfprApSwEthEstcEpPeerChassisId": cfprApSwEthEstcEpPeerChassisId,
       "cfprApSwEthEstcEpPeerDn": cfprApSwEthEstcEpPeerDn,
       "cfprApSwEthEstcEpPeerPortId": cfprApSwEthEstcEpPeerPortId,
       "cfprApSwEthEstcEpPeerSlotId": cfprApSwEthEstcEpPeerSlotId,
       "cfprApSwEthEstcEpPinGroupName": cfprApSwEthEstcEpPinGroupName,
       "cfprApSwEthEstcEpPortId": cfprApSwEthEstcEpPortId,
       "cfprApSwEthEstcEpPortMode": cfprApSwEthEstcEpPortMode,
       "cfprApSwEthEstcEpPriorityFlowCtrl": cfprApSwEthEstcEpPriorityFlowCtrl,
       "cfprApSwEthEstcEpRecvFlowCtrl": cfprApSwEthEstcEpRecvFlowCtrl,
       "cfprApSwEthEstcEpSendFlowCtrl": cfprApSwEthEstcEpSendFlowCtrl,
       "cfprApSwEthEstcEpSlotId": cfprApSwEthEstcEpSlotId,
       "cfprApSwEthEstcEpSwitchId": cfprApSwEthEstcEpSwitchId,
       "cfprApSwEthEstcEpTransport": cfprApSwEthEstcEpTransport,
       "cfprApSwEthEstcEpType": cfprApSwEthEstcEpType,
       "cfprApSwEthEstcEpUplinkFailAction": cfprApSwEthEstcEpUplinkFailAction,
       "cfprApSwEthEstcPcTable": cfprApSwEthEstcPcTable,
       "cfprApSwEthEstcPcEntry": cfprApSwEthEstcPcEntry,
       "cfprApSwEthEstcPcInstanceId": cfprApSwEthEstcPcInstanceId,
       "cfprApSwEthEstcPcDn": cfprApSwEthEstcPcDn,
       "cfprApSwEthEstcPcRn": cfprApSwEthEstcPcRn,
       "cfprApSwEthEstcPcAdminSpeed": cfprApSwEthEstcPcAdminSpeed,
       "cfprApSwEthEstcPcAdminState": cfprApSwEthEstcPcAdminState,
       "cfprApSwEthEstcPcBorderAggrPortId": cfprApSwEthEstcPcBorderAggrPortId,
       "cfprApSwEthEstcPcBorderPortId": cfprApSwEthEstcPcBorderPortId,
       "cfprApSwEthEstcPcBorderSlotId": cfprApSwEthEstcPcBorderSlotId,
       "cfprApSwEthEstcPcCdp": cfprApSwEthEstcPcCdp,
       "cfprApSwEthEstcPcCosValue": cfprApSwEthEstcPcCosValue,
       "cfprApSwEthEstcPcEpDn": cfprApSwEthEstcPcEpDn,
       "cfprApSwEthEstcPcForgeMac": cfprApSwEthEstcPcForgeMac,
       "cfprApSwEthEstcPcIfRole": cfprApSwEthEstcPcIfRole,
       "cfprApSwEthEstcPcIfType": cfprApSwEthEstcPcIfType,
       "cfprApSwEthEstcPcLacpFastTimer": cfprApSwEthEstcPcLacpFastTimer,
       "cfprApSwEthEstcPcLacpSuspendIndividual": cfprApSwEthEstcPcLacpSuspendIndividual,
       "cfprApSwEthEstcPcLocale": cfprApSwEthEstcPcLocale,
       "cfprApSwEthEstcPcMonTrafDir": cfprApSwEthEstcPcMonTrafDir,
       "cfprApSwEthEstcPcName": cfprApSwEthEstcPcName,
       "cfprApSwEthEstcPcPeerDn": cfprApSwEthEstcPcPeerDn,
       "cfprApSwEthEstcPcPortId": cfprApSwEthEstcPcPortId,
       "cfprApSwEthEstcPcPortMode": cfprApSwEthEstcPcPortMode,
       "cfprApSwEthEstcPcPriorityFlowCtrl": cfprApSwEthEstcPcPriorityFlowCtrl,
       "cfprApSwEthEstcPcProtocol": cfprApSwEthEstcPcProtocol,
       "cfprApSwEthEstcPcRecvFlowCtrl": cfprApSwEthEstcPcRecvFlowCtrl,
       "cfprApSwEthEstcPcSendFlowCtrl": cfprApSwEthEstcPcSendFlowCtrl,
       "cfprApSwEthEstcPcSwitchId": cfprApSwEthEstcPcSwitchId,
       "cfprApSwEthEstcPcTransport": cfprApSwEthEstcPcTransport,
       "cfprApSwEthEstcPcType": cfprApSwEthEstcPcType,
       "cfprApSwEthEstcPcUplinkFailAction": cfprApSwEthEstcPcUplinkFailAction,
       "cfprApSwEthLanBorderTable": cfprApSwEthLanBorderTable,
       "cfprApSwEthLanBorderEntry": cfprApSwEthLanBorderEntry,
       "cfprApSwEthLanBorderInstanceId": cfprApSwEthLanBorderInstanceId,
       "cfprApSwEthLanBorderDn": cfprApSwEthLanBorderDn,
       "cfprApSwEthLanBorderRn": cfprApSwEthLanBorderRn,
       "cfprApSwEthLanBorderDeployFlag": cfprApSwEthLanBorderDeployFlag,
       "cfprApSwEthLanBorderFsmDescr": cfprApSwEthLanBorderFsmDescr,
       "cfprApSwEthLanBorderFsmFlags": cfprApSwEthLanBorderFsmFlags,
       "cfprApSwEthLanBorderFsmPrev": cfprApSwEthLanBorderFsmPrev,
       "cfprApSwEthLanBorderFsmProgr": cfprApSwEthLanBorderFsmProgr,
       "cfprApSwEthLanBorderFsmRmtInvErrCode": cfprApSwEthLanBorderFsmRmtInvErrCode,
       "cfprApSwEthLanBorderFsmRmtInvErrDescr": cfprApSwEthLanBorderFsmRmtInvErrDescr,
       "cfprApSwEthLanBorderFsmRmtInvRslt": cfprApSwEthLanBorderFsmRmtInvRslt,
       "cfprApSwEthLanBorderFsmStageDescr": cfprApSwEthLanBorderFsmStageDescr,
       "cfprApSwEthLanBorderFsmStamp": cfprApSwEthLanBorderFsmStamp,
       "cfprApSwEthLanBorderFsmStatus": cfprApSwEthLanBorderFsmStatus,
       "cfprApSwEthLanBorderFsmTry": cfprApSwEthLanBorderFsmTry,
       "cfprApSwEthLanBorderLocale": cfprApSwEthLanBorderLocale,
       "cfprApSwEthLanBorderName": cfprApSwEthLanBorderName,
       "cfprApSwEthLanBorderSwitchId": cfprApSwEthLanBorderSwitchId,
       "cfprApSwEthLanBorderTransport": cfprApSwEthLanBorderTransport,
       "cfprApSwEthLanBorderType": cfprApSwEthLanBorderType,
       "cfprApSwEthLanBorderUdldMsgInterval": cfprApSwEthLanBorderUdldMsgInterval,
       "cfprApSwEthLanBorderUdldRecoveryAction": cfprApSwEthLanBorderUdldRecoveryAction,
       "cfprApSwEthLanBorderFsmTable": cfprApSwEthLanBorderFsmTable,
       "cfprApSwEthLanBorderFsmEntry": cfprApSwEthLanBorderFsmEntry,
       "cfprApSwEthLanBorderFsmInstanceId": cfprApSwEthLanBorderFsmInstanceId,
       "cfprApSwEthLanBorderFsmDn": cfprApSwEthLanBorderFsmDn,
       "cfprApSwEthLanBorderFsmRn": cfprApSwEthLanBorderFsmRn,
       "cfprApSwEthLanBorderFsmCompletionTime": cfprApSwEthLanBorderFsmCompletionTime,
       "cfprApSwEthLanBorderFsmCurrentFsm": cfprApSwEthLanBorderFsmCurrentFsm,
       "cfprApSwEthLanBorderFsmDescrData": cfprApSwEthLanBorderFsmDescrData,
       "cfprApSwEthLanBorderFsmFsmStatus": cfprApSwEthLanBorderFsmFsmStatus,
       "cfprApSwEthLanBorderFsmProgress": cfprApSwEthLanBorderFsmProgress,
       "cfprApSwEthLanBorderFsmRmtErrCode": cfprApSwEthLanBorderFsmRmtErrCode,
       "cfprApSwEthLanBorderFsmRmtErrDescr": cfprApSwEthLanBorderFsmRmtErrDescr,
       "cfprApSwEthLanBorderFsmRmtRslt": cfprApSwEthLanBorderFsmRmtRslt,
       "cfprApSwEthLanBorderFsmStageTable": cfprApSwEthLanBorderFsmStageTable,
       "cfprApSwEthLanBorderFsmStageEntry": cfprApSwEthLanBorderFsmStageEntry,
       "cfprApSwEthLanBorderFsmStageInstanceId": cfprApSwEthLanBorderFsmStageInstanceId,
       "cfprApSwEthLanBorderFsmStageDn": cfprApSwEthLanBorderFsmStageDn,
       "cfprApSwEthLanBorderFsmStageRn": cfprApSwEthLanBorderFsmStageRn,
       "cfprApSwEthLanBorderFsmStageDescrData": cfprApSwEthLanBorderFsmStageDescrData,
       "cfprApSwEthLanBorderFsmStageLastUpdateTime": cfprApSwEthLanBorderFsmStageLastUpdateTime,
       "cfprApSwEthLanBorderFsmStageName": cfprApSwEthLanBorderFsmStageName,
       "cfprApSwEthLanBorderFsmStageOrder": cfprApSwEthLanBorderFsmStageOrder,
       "cfprApSwEthLanBorderFsmStageRetry": cfprApSwEthLanBorderFsmStageRetry,
       "cfprApSwEthLanBorderFsmStageStageStatus": cfprApSwEthLanBorderFsmStageStageStatus,
       "cfprApSwEthLanBorderFsmTaskTable": cfprApSwEthLanBorderFsmTaskTable,
       "cfprApSwEthLanBorderFsmTaskEntry": cfprApSwEthLanBorderFsmTaskEntry,
       "cfprApSwEthLanBorderFsmTaskInstanceId": cfprApSwEthLanBorderFsmTaskInstanceId,
       "cfprApSwEthLanBorderFsmTaskDn": cfprApSwEthLanBorderFsmTaskDn,
       "cfprApSwEthLanBorderFsmTaskRn": cfprApSwEthLanBorderFsmTaskRn,
       "cfprApSwEthLanBorderFsmTaskCompletion": cfprApSwEthLanBorderFsmTaskCompletion,
       "cfprApSwEthLanBorderFsmTaskFlags": cfprApSwEthLanBorderFsmTaskFlags,
       "cfprApSwEthLanBorderFsmTaskItem": cfprApSwEthLanBorderFsmTaskItem,
       "cfprApSwEthLanBorderFsmTaskSeqId": cfprApSwEthLanBorderFsmTaskSeqId,
       "cfprApSwEthLanEpTable": cfprApSwEthLanEpTable,
       "cfprApSwEthLanEpEntry": cfprApSwEthLanEpEntry,
       "cfprApSwEthLanEpInstanceId": cfprApSwEthLanEpInstanceId,
       "cfprApSwEthLanEpDn": cfprApSwEthLanEpDn,
       "cfprApSwEthLanEpRn": cfprApSwEthLanEpRn,
       "cfprApSwEthLanEpAdminDuplex": cfprApSwEthLanEpAdminDuplex,
       "cfprApSwEthLanEpAdminSpeed": cfprApSwEthLanEpAdminSpeed,
       "cfprApSwEthLanEpAdminState": cfprApSwEthLanEpAdminState,
       "cfprApSwEthLanEpAggrPortId": cfprApSwEthLanEpAggrPortId,
       "cfprApSwEthLanEpAutoNeg": cfprApSwEthLanEpAutoNeg,
       "cfprApSwEthLanEpChassisId": cfprApSwEthLanEpChassisId,
       "cfprApSwEthLanEpDtagVlan": cfprApSwEthLanEpDtagVlan,
       "cfprApSwEthLanEpEpDn": cfprApSwEthLanEpEpDn,
       "cfprApSwEthLanEpFabRole": cfprApSwEthLanEpFabRole,
       "cfprApSwEthLanEpIfRole": cfprApSwEthLanEpIfRole,
       "cfprApSwEthLanEpIfType": cfprApSwEthLanEpIfType,
       "cfprApSwEthLanEpLc": cfprApSwEthLanEpLc,
       "cfprApSwEthLanEpLocale": cfprApSwEthLanEpLocale,
       "cfprApSwEthLanEpMtu": cfprApSwEthLanEpMtu,
       "cfprApSwEthLanEpName": cfprApSwEthLanEpName,
       "cfprApSwEthLanEpPcId": cfprApSwEthLanEpPcId,
       "cfprApSwEthLanEpPeerAggrPortId": cfprApSwEthLanEpPeerAggrPortId,
       "cfprApSwEthLanEpPeerChassisId": cfprApSwEthLanEpPeerChassisId,
       "cfprApSwEthLanEpPeerDn": cfprApSwEthLanEpPeerDn,
       "cfprApSwEthLanEpPeerPortId": cfprApSwEthLanEpPeerPortId,
       "cfprApSwEthLanEpPeerSlotId": cfprApSwEthLanEpPeerSlotId,
       "cfprApSwEthLanEpPortId": cfprApSwEthLanEpPortId,
       "cfprApSwEthLanEpPriorityFlowCtrl": cfprApSwEthLanEpPriorityFlowCtrl,
       "cfprApSwEthLanEpQosPrio": cfprApSwEthLanEpQosPrio,
       "cfprApSwEthLanEpRecvFlowCtrl": cfprApSwEthLanEpRecvFlowCtrl,
       "cfprApSwEthLanEpSendFlowCtrl": cfprApSwEthLanEpSendFlowCtrl,
       "cfprApSwEthLanEpSlotId": cfprApSwEthLanEpSlotId,
       "cfprApSwEthLanEpSwitchId": cfprApSwEthLanEpSwitchId,
       "cfprApSwEthLanEpTransport": cfprApSwEthLanEpTransport,
       "cfprApSwEthLanEpType": cfprApSwEthLanEpType,
       "cfprApSwEthLanEpUdldAdminState": cfprApSwEthLanEpUdldAdminState,
       "cfprApSwEthLanEpUdldMode": cfprApSwEthLanEpUdldMode,
       "cfprApSwEthLanMonTable": cfprApSwEthLanMonTable,
       "cfprApSwEthLanMonEntry": cfprApSwEthLanMonEntry,
       "cfprApSwEthLanMonInstanceId": cfprApSwEthLanMonInstanceId,
       "cfprApSwEthLanMonDn": cfprApSwEthLanMonDn,
       "cfprApSwEthLanMonRn": cfprApSwEthLanMonRn,
       "cfprApSwEthLanMonLocale": cfprApSwEthLanMonLocale,
       "cfprApSwEthLanMonName": cfprApSwEthLanMonName,
       "cfprApSwEthLanMonSwitchId": cfprApSwEthLanMonSwitchId,
       "cfprApSwEthLanMonTransport": cfprApSwEthLanMonTransport,
       "cfprApSwEthLanMonType": cfprApSwEthLanMonType,
       "cfprApSwEthLanPcTable": cfprApSwEthLanPcTable,
       "cfprApSwEthLanPcEntry": cfprApSwEthLanPcEntry,
       "cfprApSwEthLanPcInstanceId": cfprApSwEthLanPcInstanceId,
       "cfprApSwEthLanPcDn": cfprApSwEthLanPcDn,
       "cfprApSwEthLanPcRn": cfprApSwEthLanPcRn,
       "cfprApSwEthLanPcAdminDuplex": cfprApSwEthLanPcAdminDuplex,
       "cfprApSwEthLanPcAdminSpeed": cfprApSwEthLanPcAdminSpeed,
       "cfprApSwEthLanPcAdminState": cfprApSwEthLanPcAdminState,
       "cfprApSwEthLanPcAutoNeg": cfprApSwEthLanPcAutoNeg,
       "cfprApSwEthLanPcCluChassisId": cfprApSwEthLanPcCluChassisId,
       "cfprApSwEthLanPcClusterName": cfprApSwEthLanPcClusterName,
       "cfprApSwEthLanPcDtagVlan": cfprApSwEthLanPcDtagVlan,
       "cfprApSwEthLanPcEpDn": cfprApSwEthLanPcEpDn,
       "cfprApSwEthLanPcFabRole": cfprApSwEthLanPcFabRole,
       "cfprApSwEthLanPcIfRole": cfprApSwEthLanPcIfRole,
       "cfprApSwEthLanPcIfType": cfprApSwEthLanPcIfType,
       "cfprApSwEthLanPcLacpDetach": cfprApSwEthLanPcLacpDetach,
       "cfprApSwEthLanPcLacpFastTimer": cfprApSwEthLanPcLacpFastTimer,
       "cfprApSwEthLanPcLacpMode": cfprApSwEthLanPcLacpMode,
       "cfprApSwEthLanPcLacpSuspendIndividual": cfprApSwEthLanPcLacpSuspendIndividual,
       "cfprApSwEthLanPcLocale": cfprApSwEthLanPcLocale,
       "cfprApSwEthLanPcMonTrafDir": cfprApSwEthLanPcMonTrafDir,
       "cfprApSwEthLanPcMtu": cfprApSwEthLanPcMtu,
       "cfprApSwEthLanPcName": cfprApSwEthLanPcName,
       "cfprApSwEthLanPcPeerDn": cfprApSwEthLanPcPeerDn,
       "cfprApSwEthLanPcPortId": cfprApSwEthLanPcPortId,
       "cfprApSwEthLanPcPriorityFlowCtrl": cfprApSwEthLanPcPriorityFlowCtrl,
       "cfprApSwEthLanPcQosPrio": cfprApSwEthLanPcQosPrio,
       "cfprApSwEthLanPcRecvFlowCtrl": cfprApSwEthLanPcRecvFlowCtrl,
       "cfprApSwEthLanPcSendFlowCtrl": cfprApSwEthLanPcSendFlowCtrl,
       "cfprApSwEthLanPcSpannedCluster": cfprApSwEthLanPcSpannedCluster,
       "cfprApSwEthLanPcSwitchId": cfprApSwEthLanPcSwitchId,
       "cfprApSwEthLanPcTransport": cfprApSwEthLanPcTransport,
       "cfprApSwEthLanPcType": cfprApSwEthLanPcType,
       "cfprApSwEthMonTable": cfprApSwEthMonTable,
       "cfprApSwEthMonEntry": cfprApSwEthMonEntry,
       "cfprApSwEthMonInstanceId": cfprApSwEthMonInstanceId,
       "cfprApSwEthMonDn": cfprApSwEthMonDn,
       "cfprApSwEthMonRn": cfprApSwEthMonRn,
       "cfprApSwEthMonAdminState": cfprApSwEthMonAdminState,
       "cfprApSwEthMonFsmDescr": cfprApSwEthMonFsmDescr,
       "cfprApSwEthMonFsmPrev": cfprApSwEthMonFsmPrev,
       "cfprApSwEthMonFsmProgr": cfprApSwEthMonFsmProgr,
       "cfprApSwEthMonFsmRmtInvErrCode": cfprApSwEthMonFsmRmtInvErrCode,
       "cfprApSwEthMonFsmRmtInvErrDescr": cfprApSwEthMonFsmRmtInvErrDescr,
       "cfprApSwEthMonFsmRmtInvRslt": cfprApSwEthMonFsmRmtInvRslt,
       "cfprApSwEthMonFsmStageDescr": cfprApSwEthMonFsmStageDescr,
       "cfprApSwEthMonFsmStamp": cfprApSwEthMonFsmStamp,
       "cfprApSwEthMonFsmStatus": cfprApSwEthMonFsmStatus,
       "cfprApSwEthMonFsmTry": cfprApSwEthMonFsmTry,
       "cfprApSwEthMonHasLastDest": cfprApSwEthMonHasLastDest,
       "cfprApSwEthMonLifeCycle": cfprApSwEthMonLifeCycle,
       "cfprApSwEthMonName": cfprApSwEthMonName,
       "cfprApSwEthMonPeerDn": cfprApSwEthMonPeerDn,
       "cfprApSwEthMonSession": cfprApSwEthMonSession,
       "cfprApSwEthMonSwitchId": cfprApSwEthMonSwitchId,
       "cfprApSwEthMonTransport": cfprApSwEthMonTransport,
       "cfprApSwEthMonType": cfprApSwEthMonType,
       "cfprApSwEthMonDestEpTable": cfprApSwEthMonDestEpTable,
       "cfprApSwEthMonDestEpEntry": cfprApSwEthMonDestEpEntry,
       "cfprApSwEthMonDestEpInstanceId": cfprApSwEthMonDestEpInstanceId,
       "cfprApSwEthMonDestEpDn": cfprApSwEthMonDestEpDn,
       "cfprApSwEthMonDestEpRn": cfprApSwEthMonDestEpRn,
       "cfprApSwEthMonDestEpAdminSpeed": cfprApSwEthMonDestEpAdminSpeed,
       "cfprApSwEthMonDestEpAdminState": cfprApSwEthMonDestEpAdminState,
       "cfprApSwEthMonDestEpAggrPortId": cfprApSwEthMonDestEpAggrPortId,
       "cfprApSwEthMonDestEpChassisId": cfprApSwEthMonDestEpChassisId,
       "cfprApSwEthMonDestEpEpDn": cfprApSwEthMonDestEpEpDn,
       "cfprApSwEthMonDestEpIfRole": cfprApSwEthMonDestEpIfRole,
       "cfprApSwEthMonDestEpIfType": cfprApSwEthMonDestEpIfType,
       "cfprApSwEthMonDestEpLc": cfprApSwEthMonDestEpLc,
       "cfprApSwEthMonDestEpLocale": cfprApSwEthMonDestEpLocale,
       "cfprApSwEthMonDestEpName": cfprApSwEthMonDestEpName,
       "cfprApSwEthMonDestEpPeerAggrPortId": cfprApSwEthMonDestEpPeerAggrPortId,
       "cfprApSwEthMonDestEpPeerChassisId": cfprApSwEthMonDestEpPeerChassisId,
       "cfprApSwEthMonDestEpPeerDn": cfprApSwEthMonDestEpPeerDn,
       "cfprApSwEthMonDestEpPeerPortId": cfprApSwEthMonDestEpPeerPortId,
       "cfprApSwEthMonDestEpPeerSlotId": cfprApSwEthMonDestEpPeerSlotId,
       "cfprApSwEthMonDestEpPortId": cfprApSwEthMonDestEpPortId,
       "cfprApSwEthMonDestEpSlotId": cfprApSwEthMonDestEpSlotId,
       "cfprApSwEthMonDestEpSwitchId": cfprApSwEthMonDestEpSwitchId,
       "cfprApSwEthMonDestEpTransport": cfprApSwEthMonDestEpTransport,
       "cfprApSwEthMonDestEpType": cfprApSwEthMonDestEpType,
       "cfprApSwEthMonFsmTable": cfprApSwEthMonFsmTable,
       "cfprApSwEthMonFsmEntry": cfprApSwEthMonFsmEntry,
       "cfprApSwEthMonFsmInstanceId": cfprApSwEthMonFsmInstanceId,
       "cfprApSwEthMonFsmDn": cfprApSwEthMonFsmDn,
       "cfprApSwEthMonFsmRn": cfprApSwEthMonFsmRn,
       "cfprApSwEthMonFsmCompletionTime": cfprApSwEthMonFsmCompletionTime,
       "cfprApSwEthMonFsmCurrentFsm": cfprApSwEthMonFsmCurrentFsm,
       "cfprApSwEthMonFsmDescrData": cfprApSwEthMonFsmDescrData,
       "cfprApSwEthMonFsmFsmStatus": cfprApSwEthMonFsmFsmStatus,
       "cfprApSwEthMonFsmProgress": cfprApSwEthMonFsmProgress,
       "cfprApSwEthMonFsmRmtErrCode": cfprApSwEthMonFsmRmtErrCode,
       "cfprApSwEthMonFsmRmtErrDescr": cfprApSwEthMonFsmRmtErrDescr,
       "cfprApSwEthMonFsmRmtRslt": cfprApSwEthMonFsmRmtRslt,
       "cfprApSwEthMonFsmStageTable": cfprApSwEthMonFsmStageTable,
       "cfprApSwEthMonFsmStageEntry": cfprApSwEthMonFsmStageEntry,
       "cfprApSwEthMonFsmStageInstanceId": cfprApSwEthMonFsmStageInstanceId,
       "cfprApSwEthMonFsmStageDn": cfprApSwEthMonFsmStageDn,
       "cfprApSwEthMonFsmStageRn": cfprApSwEthMonFsmStageRn,
       "cfprApSwEthMonFsmStageDescrData": cfprApSwEthMonFsmStageDescrData,
       "cfprApSwEthMonFsmStageLastUpdateTime": cfprApSwEthMonFsmStageLastUpdateTime,
       "cfprApSwEthMonFsmStageName": cfprApSwEthMonFsmStageName,
       "cfprApSwEthMonFsmStageOrder": cfprApSwEthMonFsmStageOrder,
       "cfprApSwEthMonFsmStageRetry": cfprApSwEthMonFsmStageRetry,
       "cfprApSwEthMonFsmStageStageStatus": cfprApSwEthMonFsmStageStageStatus,
       "cfprApSwEthMonFsmTaskTable": cfprApSwEthMonFsmTaskTable,
       "cfprApSwEthMonFsmTaskEntry": cfprApSwEthMonFsmTaskEntry,
       "cfprApSwEthMonFsmTaskInstanceId": cfprApSwEthMonFsmTaskInstanceId,
       "cfprApSwEthMonFsmTaskDn": cfprApSwEthMonFsmTaskDn,
       "cfprApSwEthMonFsmTaskRn": cfprApSwEthMonFsmTaskRn,
       "cfprApSwEthMonFsmTaskCompletion": cfprApSwEthMonFsmTaskCompletion,
       "cfprApSwEthMonFsmTaskFlags": cfprApSwEthMonFsmTaskFlags,
       "cfprApSwEthMonFsmTaskItem": cfprApSwEthMonFsmTaskItem,
       "cfprApSwEthMonFsmTaskSeqId": cfprApSwEthMonFsmTaskSeqId,
       "cfprApSwEthMonSrcEpTable": cfprApSwEthMonSrcEpTable,
       "cfprApSwEthMonSrcEpEntry": cfprApSwEthMonSrcEpEntry,
       "cfprApSwEthMonSrcEpInstanceId": cfprApSwEthMonSrcEpInstanceId,
       "cfprApSwEthMonSrcEpDn": cfprApSwEthMonSrcEpDn,
       "cfprApSwEthMonSrcEpRn": cfprApSwEthMonSrcEpRn,
       "cfprApSwEthMonSrcEpAdminState": cfprApSwEthMonSrcEpAdminState,
       "cfprApSwEthMonSrcEpAggrPortId": cfprApSwEthMonSrcEpAggrPortId,
       "cfprApSwEthMonSrcEpChassisId": cfprApSwEthMonSrcEpChassisId,
       "cfprApSwEthMonSrcEpEpDn": cfprApSwEthMonSrcEpEpDn,
       "cfprApSwEthMonSrcEpIfRole": cfprApSwEthMonSrcEpIfRole,
       "cfprApSwEthMonSrcEpIfType": cfprApSwEthMonSrcEpIfType,
       "cfprApSwEthMonSrcEpLc": cfprApSwEthMonSrcEpLc,
       "cfprApSwEthMonSrcEpLocale": cfprApSwEthMonSrcEpLocale,
       "cfprApSwEthMonSrcEpMonTrafDir": cfprApSwEthMonSrcEpMonTrafDir,
       "cfprApSwEthMonSrcEpName": cfprApSwEthMonSrcEpName,
       "cfprApSwEthMonSrcEpPeerAggrPortId": cfprApSwEthMonSrcEpPeerAggrPortId,
       "cfprApSwEthMonSrcEpPeerChassisId": cfprApSwEthMonSrcEpPeerChassisId,
       "cfprApSwEthMonSrcEpPeerDn": cfprApSwEthMonSrcEpPeerDn,
       "cfprApSwEthMonSrcEpPeerPortId": cfprApSwEthMonSrcEpPeerPortId,
       "cfprApSwEthMonSrcEpPeerSlotId": cfprApSwEthMonSrcEpPeerSlotId,
       "cfprApSwEthMonSrcEpPortId": cfprApSwEthMonSrcEpPortId,
       "cfprApSwEthMonSrcEpSlotId": cfprApSwEthMonSrcEpSlotId,
       "cfprApSwEthMonSrcEpSwitchId": cfprApSwEthMonSrcEpSwitchId,
       "cfprApSwEthMonSrcEpTransport": cfprApSwEthMonSrcEpTransport,
       "cfprApSwEthMonSrcEpType": cfprApSwEthMonSrcEpType,
       "cfprApSwEthTargetEpTable": cfprApSwEthTargetEpTable,
       "cfprApSwEthTargetEpEntry": cfprApSwEthTargetEpEntry,
       "cfprApSwEthTargetEpInstanceId": cfprApSwEthTargetEpInstanceId,
       "cfprApSwEthTargetEpDn": cfprApSwEthTargetEpDn,
       "cfprApSwEthTargetEpRn": cfprApSwEthTargetEpRn,
       "cfprApSwEthTargetEpAdminState": cfprApSwEthTargetEpAdminState,
       "cfprApSwEthTargetEpAggrPortId": cfprApSwEthTargetEpAggrPortId,
       "cfprApSwEthTargetEpChassisId": cfprApSwEthTargetEpChassisId,
       "cfprApSwEthTargetEpEpDn": cfprApSwEthTargetEpEpDn,
       "cfprApSwEthTargetEpFltAggr": cfprApSwEthTargetEpFltAggr,
       "cfprApSwEthTargetEpIfRole": cfprApSwEthTargetEpIfRole,
       "cfprApSwEthTargetEpIfType": cfprApSwEthTargetEpIfType,
       "cfprApSwEthTargetEpLicGP": cfprApSwEthTargetEpLicGP,
       "cfprApSwEthTargetEpLicState": cfprApSwEthTargetEpLicState,
       "cfprApSwEthTargetEpLocale": cfprApSwEthTargetEpLocale,
       "cfprApSwEthTargetEpMacAddress": cfprApSwEthTargetEpMacAddress,
       "cfprApSwEthTargetEpName": cfprApSwEthTargetEpName,
       "cfprApSwEthTargetEpOperState": cfprApSwEthTargetEpOperState,
       "cfprApSwEthTargetEpOperStateReason": cfprApSwEthTargetEpOperStateReason,
       "cfprApSwEthTargetEpPeerAggrPortId": cfprApSwEthTargetEpPeerAggrPortId,
       "cfprApSwEthTargetEpPeerChassisId": cfprApSwEthTargetEpPeerChassisId,
       "cfprApSwEthTargetEpPeerDn": cfprApSwEthTargetEpPeerDn,
       "cfprApSwEthTargetEpPeerPortId": cfprApSwEthTargetEpPeerPortId,
       "cfprApSwEthTargetEpPeerSlotId": cfprApSwEthTargetEpPeerSlotId,
       "cfprApSwEthTargetEpPortId": cfprApSwEthTargetEpPortId,
       "cfprApSwEthTargetEpSlotId": cfprApSwEthTargetEpSlotId,
       "cfprApSwEthTargetEpSwitchId": cfprApSwEthTargetEpSwitchId,
       "cfprApSwEthTargetEpTransport": cfprApSwEthTargetEpTransport,
       "cfprApSwEthTargetEpType": cfprApSwEthTargetEpType,
       "cfprApSwEthTargetEpWarnings": cfprApSwEthTargetEpWarnings,
       "cfprApSwExtUtilityTable": cfprApSwExtUtilityTable,
       "cfprApSwExtUtilityEntry": cfprApSwExtUtilityEntry,
       "cfprApSwExtUtilityInstanceId": cfprApSwExtUtilityInstanceId,
       "cfprApSwExtUtilityDn": cfprApSwExtUtilityDn,
       "cfprApSwExtUtilityRn": cfprApSwExtUtilityRn,
       "cfprApSwExtUtilityConfMode": cfprApSwExtUtilityConfMode,
       "cfprApSwExtUtilityFsmDescr": cfprApSwExtUtilityFsmDescr,
       "cfprApSwExtUtilityFsmPrev": cfprApSwExtUtilityFsmPrev,
       "cfprApSwExtUtilityFsmProgr": cfprApSwExtUtilityFsmProgr,
       "cfprApSwExtUtilityFsmRmtInvErrCode": cfprApSwExtUtilityFsmRmtInvErrCode,
       "cfprApSwExtUtilityFsmRmtInvErrDescr": cfprApSwExtUtilityFsmRmtInvErrDescr,
       "cfprApSwExtUtilityFsmRmtInvRslt": cfprApSwExtUtilityFsmRmtInvRslt,
       "cfprApSwExtUtilityFsmStageDescr": cfprApSwExtUtilityFsmStageDescr,
       "cfprApSwExtUtilityFsmStamp": cfprApSwExtUtilityFsmStamp,
       "cfprApSwExtUtilityFsmStatus": cfprApSwExtUtilityFsmStatus,
       "cfprApSwExtUtilityFsmTry": cfprApSwExtUtilityFsmTry,
       "cfprApSwExtUtilitySwitchId": cfprApSwExtUtilitySwitchId,
       "cfprApSwExtUtilityFsmTable": cfprApSwExtUtilityFsmTable,
       "cfprApSwExtUtilityFsmEntry": cfprApSwExtUtilityFsmEntry,
       "cfprApSwExtUtilityFsmInstanceId": cfprApSwExtUtilityFsmInstanceId,
       "cfprApSwExtUtilityFsmDn": cfprApSwExtUtilityFsmDn,
       "cfprApSwExtUtilityFsmRn": cfprApSwExtUtilityFsmRn,
       "cfprApSwExtUtilityFsmCompletionTime": cfprApSwExtUtilityFsmCompletionTime,
       "cfprApSwExtUtilityFsmCurrentFsm": cfprApSwExtUtilityFsmCurrentFsm,
       "cfprApSwExtUtilityFsmDescrData": cfprApSwExtUtilityFsmDescrData,
       "cfprApSwExtUtilityFsmFsmStatus": cfprApSwExtUtilityFsmFsmStatus,
       "cfprApSwExtUtilityFsmProgress": cfprApSwExtUtilityFsmProgress,
       "cfprApSwExtUtilityFsmRmtErrCode": cfprApSwExtUtilityFsmRmtErrCode,
       "cfprApSwExtUtilityFsmRmtErrDescr": cfprApSwExtUtilityFsmRmtErrDescr,
       "cfprApSwExtUtilityFsmRmtRslt": cfprApSwExtUtilityFsmRmtRslt,
       "cfprApSwExtUtilityFsmStageTable": cfprApSwExtUtilityFsmStageTable,
       "cfprApSwExtUtilityFsmStageEntry": cfprApSwExtUtilityFsmStageEntry,
       "cfprApSwExtUtilityFsmStageInstanceId": cfprApSwExtUtilityFsmStageInstanceId,
       "cfprApSwExtUtilityFsmStageDn": cfprApSwExtUtilityFsmStageDn,
       "cfprApSwExtUtilityFsmStageRn": cfprApSwExtUtilityFsmStageRn,
       "cfprApSwExtUtilityFsmStageDescrData": cfprApSwExtUtilityFsmStageDescrData,
       "cfprApSwExtUtilityFsmStageLastUpdateTime": cfprApSwExtUtilityFsmStageLastUpdateTime,
       "cfprApSwExtUtilityFsmStageName": cfprApSwExtUtilityFsmStageName,
       "cfprApSwExtUtilityFsmStageOrder": cfprApSwExtUtilityFsmStageOrder,
       "cfprApSwExtUtilityFsmStageRetry": cfprApSwExtUtilityFsmStageRetry,
       "cfprApSwExtUtilityFsmStageStageStatus": cfprApSwExtUtilityFsmStageStageStatus,
       "cfprApSwExtUtilityFsmTaskTable": cfprApSwExtUtilityFsmTaskTable,
       "cfprApSwExtUtilityFsmTaskEntry": cfprApSwExtUtilityFsmTaskEntry,
       "cfprApSwExtUtilityFsmTaskInstanceId": cfprApSwExtUtilityFsmTaskInstanceId,
       "cfprApSwExtUtilityFsmTaskDn": cfprApSwExtUtilityFsmTaskDn,
       "cfprApSwExtUtilityFsmTaskRn": cfprApSwExtUtilityFsmTaskRn,
       "cfprApSwExtUtilityFsmTaskCompletion": cfprApSwExtUtilityFsmTaskCompletion,
       "cfprApSwExtUtilityFsmTaskFlags": cfprApSwExtUtilityFsmTaskFlags,
       "cfprApSwExtUtilityFsmTaskItem": cfprApSwExtUtilityFsmTaskItem,
       "cfprApSwExtUtilityFsmTaskSeqId": cfprApSwExtUtilityFsmTaskSeqId,
       "cfprApSwFabricZoneNsTable": cfprApSwFabricZoneNsTable,
       "cfprApSwFabricZoneNsEntry": cfprApSwFabricZoneNsEntry,
       "cfprApSwFabricZoneNsInstanceId": cfprApSwFabricZoneNsInstanceId,
       "cfprApSwFabricZoneNsDn": cfprApSwFabricZoneNsDn,
       "cfprApSwFabricZoneNsRn": cfprApSwFabricZoneNsRn,
       "cfprApSwFabricZoneNsAllocStatus": cfprApSwFabricZoneNsAllocStatus,
       "cfprApSwFabricZoneNsLimit": cfprApSwFabricZoneNsLimit,
       "cfprApSwFabricZoneNsSwitchId": cfprApSwFabricZoneNsSwitchId,
       "cfprApSwFabricZoneNsZoneCount": cfprApSwFabricZoneNsZoneCount,
       "cfprApSwFabricZoneNsOverrideTable": cfprApSwFabricZoneNsOverrideTable,
       "cfprApSwFabricZoneNsOverrideEntry": cfprApSwFabricZoneNsOverrideEntry,
       "cfprApSwFabricZoneNsOverrideInstanceId": cfprApSwFabricZoneNsOverrideInstanceId,
       "cfprApSwFabricZoneNsOverrideDn": cfprApSwFabricZoneNsOverrideDn,
       "cfprApSwFabricZoneNsOverrideRn": cfprApSwFabricZoneNsOverrideRn,
       "cfprApSwFabricZoneNsOverrideLimit": cfprApSwFabricZoneNsOverrideLimit,
       "cfprApSwFcSanBorderTable": cfprApSwFcSanBorderTable,
       "cfprApSwFcSanBorderEntry": cfprApSwFcSanBorderEntry,
       "cfprApSwFcSanBorderInstanceId": cfprApSwFcSanBorderInstanceId,
       "cfprApSwFcSanBorderDn": cfprApSwFcSanBorderDn,
       "cfprApSwFcSanBorderRn": cfprApSwFcSanBorderRn,
       "cfprApSwFcSanBorderFsmDescr": cfprApSwFcSanBorderFsmDescr,
       "cfprApSwFcSanBorderFsmPrev": cfprApSwFcSanBorderFsmPrev,
       "cfprApSwFcSanBorderFsmProgr": cfprApSwFcSanBorderFsmProgr,
       "cfprApSwFcSanBorderFsmRmtInvErrCode": cfprApSwFcSanBorderFsmRmtInvErrCode,
       "cfprApSwFcSanBorderFsmRmtInvErrDescr": cfprApSwFcSanBorderFsmRmtInvErrDescr,
       "cfprApSwFcSanBorderFsmRmtInvRslt": cfprApSwFcSanBorderFsmRmtInvRslt,
       "cfprApSwFcSanBorderFsmStageDescr": cfprApSwFcSanBorderFsmStageDescr,
       "cfprApSwFcSanBorderFsmStamp": cfprApSwFcSanBorderFsmStamp,
       "cfprApSwFcSanBorderFsmStatus": cfprApSwFcSanBorderFsmStatus,
       "cfprApSwFcSanBorderFsmTry": cfprApSwFcSanBorderFsmTry,
       "cfprApSwFcSanBorderLocale": cfprApSwFcSanBorderLocale,
       "cfprApSwFcSanBorderName": cfprApSwFcSanBorderName,
       "cfprApSwFcSanBorderSwitchId": cfprApSwFcSanBorderSwitchId,
       "cfprApSwFcSanBorderTransport": cfprApSwFcSanBorderTransport,
       "cfprApSwFcSanBorderType": cfprApSwFcSanBorderType,
       "cfprApSwFcSanBorderUplinkTrunking": cfprApSwFcSanBorderUplinkTrunking,
       "cfprApSwFcSanBorderFsmTable": cfprApSwFcSanBorderFsmTable,
       "cfprApSwFcSanBorderFsmEntry": cfprApSwFcSanBorderFsmEntry,
       "cfprApSwFcSanBorderFsmInstanceId": cfprApSwFcSanBorderFsmInstanceId,
       "cfprApSwFcSanBorderFsmDn": cfprApSwFcSanBorderFsmDn,
       "cfprApSwFcSanBorderFsmRn": cfprApSwFcSanBorderFsmRn,
       "cfprApSwFcSanBorderFsmCompletionTime": cfprApSwFcSanBorderFsmCompletionTime,
       "cfprApSwFcSanBorderFsmCurrentFsm": cfprApSwFcSanBorderFsmCurrentFsm,
       "cfprApSwFcSanBorderFsmDescrData": cfprApSwFcSanBorderFsmDescrData,
       "cfprApSwFcSanBorderFsmFsmStatus": cfprApSwFcSanBorderFsmFsmStatus,
       "cfprApSwFcSanBorderFsmProgress": cfprApSwFcSanBorderFsmProgress,
       "cfprApSwFcSanBorderFsmRmtErrCode": cfprApSwFcSanBorderFsmRmtErrCode,
       "cfprApSwFcSanBorderFsmRmtErrDescr": cfprApSwFcSanBorderFsmRmtErrDescr,
       "cfprApSwFcSanBorderFsmRmtRslt": cfprApSwFcSanBorderFsmRmtRslt,
       "cfprApSwFcSanBorderFsmStageTable": cfprApSwFcSanBorderFsmStageTable,
       "cfprApSwFcSanBorderFsmStageEntry": cfprApSwFcSanBorderFsmStageEntry,
       "cfprApSwFcSanBorderFsmStageInstanceId": cfprApSwFcSanBorderFsmStageInstanceId,
       "cfprApSwFcSanBorderFsmStageDn": cfprApSwFcSanBorderFsmStageDn,
       "cfprApSwFcSanBorderFsmStageRn": cfprApSwFcSanBorderFsmStageRn,
       "cfprApSwFcSanBorderFsmStageDescrData": cfprApSwFcSanBorderFsmStageDescrData,
       "cfprApSwFcSanBorderFsmStageLastUpdateTime": cfprApSwFcSanBorderFsmStageLastUpdateTime,
       "cfprApSwFcSanBorderFsmStageName": cfprApSwFcSanBorderFsmStageName,
       "cfprApSwFcSanBorderFsmStageOrder": cfprApSwFcSanBorderFsmStageOrder,
       "cfprApSwFcSanBorderFsmStageRetry": cfprApSwFcSanBorderFsmStageRetry,
       "cfprApSwFcSanBorderFsmStageStageStatus": cfprApSwFcSanBorderFsmStageStageStatus,
       "cfprApSwFcSanBorderFsmTaskTable": cfprApSwFcSanBorderFsmTaskTable,
       "cfprApSwFcSanBorderFsmTaskEntry": cfprApSwFcSanBorderFsmTaskEntry,
       "cfprApSwFcSanBorderFsmTaskInstanceId": cfprApSwFcSanBorderFsmTaskInstanceId,
       "cfprApSwFcSanBorderFsmTaskDn": cfprApSwFcSanBorderFsmTaskDn,
       "cfprApSwFcSanBorderFsmTaskRn": cfprApSwFcSanBorderFsmTaskRn,
       "cfprApSwFcSanBorderFsmTaskCompletion": cfprApSwFcSanBorderFsmTaskCompletion,
       "cfprApSwFcSanBorderFsmTaskFlags": cfprApSwFcSanBorderFsmTaskFlags,
       "cfprApSwFcSanBorderFsmTaskItem": cfprApSwFcSanBorderFsmTaskItem,
       "cfprApSwFcSanBorderFsmTaskSeqId": cfprApSwFcSanBorderFsmTaskSeqId,
       "cfprApSwFcSanEpTable": cfprApSwFcSanEpTable,
       "cfprApSwFcSanEpEntry": cfprApSwFcSanEpEntry,
       "cfprApSwFcSanEpInstanceId": cfprApSwFcSanEpInstanceId,
       "cfprApSwFcSanEpDn": cfprApSwFcSanEpDn,
       "cfprApSwFcSanEpRn": cfprApSwFcSanEpRn,
       "cfprApSwFcSanEpAdminSpeed": cfprApSwFcSanEpAdminSpeed,
       "cfprApSwFcSanEpAdminState": cfprApSwFcSanEpAdminState,
       "cfprApSwFcSanEpAggrPortId": cfprApSwFcSanEpAggrPortId,
       "cfprApSwFcSanEpChassisId": cfprApSwFcSanEpChassisId,
       "cfprApSwFcSanEpEpDn": cfprApSwFcSanEpEpDn,
       "cfprApSwFcSanEpFillPattern": cfprApSwFcSanEpFillPattern,
       "cfprApSwFcSanEpIfRole": cfprApSwFcSanEpIfRole,
       "cfprApSwFcSanEpIfType": cfprApSwFcSanEpIfType,
       "cfprApSwFcSanEpLc": cfprApSwFcSanEpLc,
       "cfprApSwFcSanEpLocale": cfprApSwFcSanEpLocale,
       "cfprApSwFcSanEpName": cfprApSwFcSanEpName,
       "cfprApSwFcSanEpPcId": cfprApSwFcSanEpPcId,
       "cfprApSwFcSanEpPeerAggrPortId": cfprApSwFcSanEpPeerAggrPortId,
       "cfprApSwFcSanEpPeerChassisId": cfprApSwFcSanEpPeerChassisId,
       "cfprApSwFcSanEpPeerDn": cfprApSwFcSanEpPeerDn,
       "cfprApSwFcSanEpPeerPortId": cfprApSwFcSanEpPeerPortId,
       "cfprApSwFcSanEpPeerSlotId": cfprApSwFcSanEpPeerSlotId,
       "cfprApSwFcSanEpPortId": cfprApSwFcSanEpPortId,
       "cfprApSwFcSanEpPortVsanId": cfprApSwFcSanEpPortVsanId,
       "cfprApSwFcSanEpSlotId": cfprApSwFcSanEpSlotId,
       "cfprApSwFcSanEpSwitchId": cfprApSwFcSanEpSwitchId,
       "cfprApSwFcSanEpTransport": cfprApSwFcSanEpTransport,
       "cfprApSwFcSanEpType": cfprApSwFcSanEpType,
       "cfprApSwFcSanPcTable": cfprApSwFcSanPcTable,
       "cfprApSwFcSanPcEntry": cfprApSwFcSanPcEntry,
       "cfprApSwFcSanPcInstanceId": cfprApSwFcSanPcInstanceId,
       "cfprApSwFcSanPcDn": cfprApSwFcSanPcDn,
       "cfprApSwFcSanPcRn": cfprApSwFcSanPcRn,
       "cfprApSwFcSanPcAdminSpeed": cfprApSwFcSanPcAdminSpeed,
       "cfprApSwFcSanPcAdminState": cfprApSwFcSanPcAdminState,
       "cfprApSwFcSanPcEpDn": cfprApSwFcSanPcEpDn,
       "cfprApSwFcSanPcIfRole": cfprApSwFcSanPcIfRole,
       "cfprApSwFcSanPcIfType": cfprApSwFcSanPcIfType,
       "cfprApSwFcSanPcLocale": cfprApSwFcSanPcLocale,
       "cfprApSwFcSanPcMonTrafDir": cfprApSwFcSanPcMonTrafDir,
       "cfprApSwFcSanPcName": cfprApSwFcSanPcName,
       "cfprApSwFcSanPcPcId": cfprApSwFcSanPcPcId,
       "cfprApSwFcSanPcPeerDn": cfprApSwFcSanPcPeerDn,
       "cfprApSwFcSanPcPortId": cfprApSwFcSanPcPortId,
       "cfprApSwFcSanPcPortVsanId": cfprApSwFcSanPcPortVsanId,
       "cfprApSwFcSanPcSwitchId": cfprApSwFcSanPcSwitchId,
       "cfprApSwFcSanPcTransport": cfprApSwFcSanPcTransport,
       "cfprApSwFcSanPcType": cfprApSwFcSanPcType,
       "cfprApSwFcServerZoneGroupTable": cfprApSwFcServerZoneGroupTable,
       "cfprApSwFcServerZoneGroupEntry": cfprApSwFcServerZoneGroupEntry,
       "cfprApSwFcServerZoneGroupInstanceId": cfprApSwFcServerZoneGroupInstanceId,
       "cfprApSwFcServerZoneGroupDn": cfprApSwFcServerZoneGroupDn,
       "cfprApSwFcServerZoneGroupRn": cfprApSwFcServerZoneGroupRn,
       "cfprApSwFcServerZoneGroupEpDn": cfprApSwFcServerZoneGroupEpDn,
       "cfprApSwFcServerZoneGroupId": cfprApSwFcServerZoneGroupId,
       "cfprApSwFcServerZoneGroupLc": cfprApSwFcServerZoneGroupLc,
       "cfprApSwFcServerZoneGroupName": cfprApSwFcServerZoneGroupName,
       "cfprApSwFcServerZoneGroupPeerDn": cfprApSwFcServerZoneGroupPeerDn,
       "cfprApSwFcServerZoneGroupServerDn": cfprApSwFcServerZoneGroupServerDn,
       "cfprApSwFcZoneTable": cfprApSwFcZoneTable,
       "cfprApSwFcZoneEntry": cfprApSwFcZoneEntry,
       "cfprApSwFcZoneInstanceId": cfprApSwFcZoneInstanceId,
       "cfprApSwFcZoneDn": cfprApSwFcZoneDn,
       "cfprApSwFcZoneRn": cfprApSwFcZoneRn,
       "cfprApSwFcZoneId": cfprApSwFcZoneId,
       "cfprApSwFcZoneIdentity": cfprApSwFcZoneIdentity,
       "cfprApSwFcZoneLc": cfprApSwFcZoneLc,
       "cfprApSwFcZoneName": cfprApSwFcZoneName,
       "cfprApSwFcZoneOperState": cfprApSwFcZoneOperState,
       "cfprApSwFcZonePeerDn": cfprApSwFcZonePeerDn,
       "cfprApSwFcZoneSetTable": cfprApSwFcZoneSetTable,
       "cfprApSwFcZoneSetEntry": cfprApSwFcZoneSetEntry,
       "cfprApSwFcZoneSetInstanceId": cfprApSwFcZoneSetInstanceId,
       "cfprApSwFcZoneSetDn": cfprApSwFcZoneSetDn,
       "cfprApSwFcZoneSetRn": cfprApSwFcZoneSetRn,
       "cfprApSwFcZoneSetCurrentZonePrefix": cfprApSwFcZoneSetCurrentZonePrefix,
       "cfprApSwFcZoneSetLc": cfprApSwFcZoneSetLc,
       "cfprApSwFcZoneSetName": cfprApSwFcZoneSetName,
       "cfprApSwFcZoneSetOldZonePrefix": cfprApSwFcZoneSetOldZonePrefix,
       "cfprApSwFcoeSanEpTable": cfprApSwFcoeSanEpTable,
       "cfprApSwFcoeSanEpEntry": cfprApSwFcoeSanEpEntry,
       "cfprApSwFcoeSanEpInstanceId": cfprApSwFcoeSanEpInstanceId,
       "cfprApSwFcoeSanEpDn": cfprApSwFcoeSanEpDn,
       "cfprApSwFcoeSanEpRn": cfprApSwFcoeSanEpRn,
       "cfprApSwFcoeSanEpAdminSpeed": cfprApSwFcoeSanEpAdminSpeed,
       "cfprApSwFcoeSanEpAdminState": cfprApSwFcoeSanEpAdminState,
       "cfprApSwFcoeSanEpAggrPortId": cfprApSwFcoeSanEpAggrPortId,
       "cfprApSwFcoeSanEpChassisId": cfprApSwFcoeSanEpChassisId,
       "cfprApSwFcoeSanEpEpDn": cfprApSwFcoeSanEpEpDn,
       "cfprApSwFcoeSanEpIfRole": cfprApSwFcoeSanEpIfRole,
       "cfprApSwFcoeSanEpIfType": cfprApSwFcoeSanEpIfType,
       "cfprApSwFcoeSanEpLc": cfprApSwFcoeSanEpLc,
       "cfprApSwFcoeSanEpLocale": cfprApSwFcoeSanEpLocale,
       "cfprApSwFcoeSanEpName": cfprApSwFcoeSanEpName,
       "cfprApSwFcoeSanEpPcId": cfprApSwFcoeSanEpPcId,
       "cfprApSwFcoeSanEpPeerAggrPortId": cfprApSwFcoeSanEpPeerAggrPortId,
       "cfprApSwFcoeSanEpPeerChassisId": cfprApSwFcoeSanEpPeerChassisId,
       "cfprApSwFcoeSanEpPeerDn": cfprApSwFcoeSanEpPeerDn,
       "cfprApSwFcoeSanEpPeerPortId": cfprApSwFcoeSanEpPeerPortId,
       "cfprApSwFcoeSanEpPeerSlotId": cfprApSwFcoeSanEpPeerSlotId,
       "cfprApSwFcoeSanEpPeerState": cfprApSwFcoeSanEpPeerState,
       "cfprApSwFcoeSanEpPortId": cfprApSwFcoeSanEpPortId,
       "cfprApSwFcoeSanEpPortVsanId": cfprApSwFcoeSanEpPortVsanId,
       "cfprApSwFcoeSanEpSlotId": cfprApSwFcoeSanEpSlotId,
       "cfprApSwFcoeSanEpSwitchId": cfprApSwFcoeSanEpSwitchId,
       "cfprApSwFcoeSanEpTransport": cfprApSwFcoeSanEpTransport,
       "cfprApSwFcoeSanEpType": cfprApSwFcoeSanEpType,
       "cfprApSwFcoeSanEpUdldAdminState": cfprApSwFcoeSanEpUdldAdminState,
       "cfprApSwFcoeSanEpUdldMode": cfprApSwFcoeSanEpUdldMode,
       "cfprApSwFcoeSanPcTable": cfprApSwFcoeSanPcTable,
       "cfprApSwFcoeSanPcEntry": cfprApSwFcoeSanPcEntry,
       "cfprApSwFcoeSanPcInstanceId": cfprApSwFcoeSanPcInstanceId,
       "cfprApSwFcoeSanPcDn": cfprApSwFcoeSanPcDn,
       "cfprApSwFcoeSanPcRn": cfprApSwFcoeSanPcRn,
       "cfprApSwFcoeSanPcAdminState": cfprApSwFcoeSanPcAdminState,
       "cfprApSwFcoeSanPcEpDn": cfprApSwFcoeSanPcEpDn,
       "cfprApSwFcoeSanPcIfRole": cfprApSwFcoeSanPcIfRole,
       "cfprApSwFcoeSanPcIfType": cfprApSwFcoeSanPcIfType,
       "cfprApSwFcoeSanPcLacpFastTimer": cfprApSwFcoeSanPcLacpFastTimer,
       "cfprApSwFcoeSanPcLacpSuspendIndividual": cfprApSwFcoeSanPcLacpSuspendIndividual,
       "cfprApSwFcoeSanPcLocale": cfprApSwFcoeSanPcLocale,
       "cfprApSwFcoeSanPcMonTrafDir": cfprApSwFcoeSanPcMonTrafDir,
       "cfprApSwFcoeSanPcName": cfprApSwFcoeSanPcName,
       "cfprApSwFcoeSanPcPcId": cfprApSwFcoeSanPcPcId,
       "cfprApSwFcoeSanPcPeerDn": cfprApSwFcoeSanPcPeerDn,
       "cfprApSwFcoeSanPcPeerState": cfprApSwFcoeSanPcPeerState,
       "cfprApSwFcoeSanPcPortId": cfprApSwFcoeSanPcPortId,
       "cfprApSwFcoeSanPcPortVsanId": cfprApSwFcoeSanPcPortVsanId,
       "cfprApSwFcoeSanPcSwitchId": cfprApSwFcoeSanPcSwitchId,
       "cfprApSwFcoeSanPcTransport": cfprApSwFcoeSanPcTransport,
       "cfprApSwFcoeSanPcType": cfprApSwFcoeSanPcType,
       "cfprApSwPhysTable": cfprApSwPhysTable,
       "cfprApSwPhysEntry": cfprApSwPhysEntry,
       "cfprApSwPhysInstanceId": cfprApSwPhysInstanceId,
       "cfprApSwPhysDn": cfprApSwPhysDn,
       "cfprApSwPhysRn": cfprApSwPhysRn,
       "cfprApSwPhysConfMode": cfprApSwPhysConfMode,
       "cfprApSwPhysFsmDescr": cfprApSwPhysFsmDescr,
       "cfprApSwPhysFsmPrev": cfprApSwPhysFsmPrev,
       "cfprApSwPhysFsmProgr": cfprApSwPhysFsmProgr,
       "cfprApSwPhysFsmRmtInvErrCode": cfprApSwPhysFsmRmtInvErrCode,
       "cfprApSwPhysFsmRmtInvErrDescr": cfprApSwPhysFsmRmtInvErrDescr,
       "cfprApSwPhysFsmRmtInvRslt": cfprApSwPhysFsmRmtInvRslt,
       "cfprApSwPhysFsmStageDescr": cfprApSwPhysFsmStageDescr,
       "cfprApSwPhysFsmStamp": cfprApSwPhysFsmStamp,
       "cfprApSwPhysFsmStatus": cfprApSwPhysFsmStatus,
       "cfprApSwPhysFsmTry": cfprApSwPhysFsmTry,
       "cfprApSwPhysEtherEpTable": cfprApSwPhysEtherEpTable,
       "cfprApSwPhysEtherEpEntry": cfprApSwPhysEtherEpEntry,
       "cfprApSwPhysEtherEpInstanceId": cfprApSwPhysEtherEpInstanceId,
       "cfprApSwPhysEtherEpDn": cfprApSwPhysEtherEpDn,
       "cfprApSwPhysEtherEpRn": cfprApSwPhysEtherEpRn,
       "cfprApSwPhysEtherEpAdminState": cfprApSwPhysEtherEpAdminState,
       "cfprApSwPhysEtherEpAggrPortId": cfprApSwPhysEtherEpAggrPortId,
       "cfprApSwPhysEtherEpChassisId": cfprApSwPhysEtherEpChassisId,
       "cfprApSwPhysEtherEpEpDn": cfprApSwPhysEtherEpEpDn,
       "cfprApSwPhysEtherEpIfRole": cfprApSwPhysEtherEpIfRole,
       "cfprApSwPhysEtherEpIfType": cfprApSwPhysEtherEpIfType,
       "cfprApSwPhysEtherEpLc": cfprApSwPhysEtherEpLc,
       "cfprApSwPhysEtherEpLocale": cfprApSwPhysEtherEpLocale,
       "cfprApSwPhysEtherEpName": cfprApSwPhysEtherEpName,
       "cfprApSwPhysEtherEpPeerAggrPortId": cfprApSwPhysEtherEpPeerAggrPortId,
       "cfprApSwPhysEtherEpPeerChassisId": cfprApSwPhysEtherEpPeerChassisId,
       "cfprApSwPhysEtherEpPeerDn": cfprApSwPhysEtherEpPeerDn,
       "cfprApSwPhysEtherEpPeerPortId": cfprApSwPhysEtherEpPeerPortId,
       "cfprApSwPhysEtherEpPeerSlotId": cfprApSwPhysEtherEpPeerSlotId,
       "cfprApSwPhysEtherEpPortId": cfprApSwPhysEtherEpPortId,
       "cfprApSwPhysEtherEpSlotId": cfprApSwPhysEtherEpSlotId,
       "cfprApSwPhysEtherEpSwitchId": cfprApSwPhysEtherEpSwitchId,
       "cfprApSwPhysEtherEpTransport": cfprApSwPhysEtherEpTransport,
       "cfprApSwPhysEtherEpType": cfprApSwPhysEtherEpType,
       "cfprApSwPhysFcEpTable": cfprApSwPhysFcEpTable,
       "cfprApSwPhysFcEpEntry": cfprApSwPhysFcEpEntry,
       "cfprApSwPhysFcEpInstanceId": cfprApSwPhysFcEpInstanceId,
       "cfprApSwPhysFcEpDn": cfprApSwPhysFcEpDn,
       "cfprApSwPhysFcEpRn": cfprApSwPhysFcEpRn,
       "cfprApSwPhysFcEpAdminState": cfprApSwPhysFcEpAdminState,
       "cfprApSwPhysFcEpAggrPortId": cfprApSwPhysFcEpAggrPortId,
       "cfprApSwPhysFcEpChassisId": cfprApSwPhysFcEpChassisId,
       "cfprApSwPhysFcEpEpDn": cfprApSwPhysFcEpEpDn,
       "cfprApSwPhysFcEpIfRole": cfprApSwPhysFcEpIfRole,
       "cfprApSwPhysFcEpIfType": cfprApSwPhysFcEpIfType,
       "cfprApSwPhysFcEpLc": cfprApSwPhysFcEpLc,
       "cfprApSwPhysFcEpLocale": cfprApSwPhysFcEpLocale,
       "cfprApSwPhysFcEpName": cfprApSwPhysFcEpName,
       "cfprApSwPhysFcEpPeerAggrPortId": cfprApSwPhysFcEpPeerAggrPortId,
       "cfprApSwPhysFcEpPeerChassisId": cfprApSwPhysFcEpPeerChassisId,
       "cfprApSwPhysFcEpPeerDn": cfprApSwPhysFcEpPeerDn,
       "cfprApSwPhysFcEpPeerPortId": cfprApSwPhysFcEpPeerPortId,
       "cfprApSwPhysFcEpPeerSlotId": cfprApSwPhysFcEpPeerSlotId,
       "cfprApSwPhysFcEpPortId": cfprApSwPhysFcEpPortId,
       "cfprApSwPhysFcEpSlotId": cfprApSwPhysFcEpSlotId,
       "cfprApSwPhysFcEpSwitchId": cfprApSwPhysFcEpSwitchId,
       "cfprApSwPhysFcEpTransport": cfprApSwPhysFcEpTransport,
       "cfprApSwPhysFcEpType": cfprApSwPhysFcEpType,
       "cfprApSwPhysFsmTable": cfprApSwPhysFsmTable,
       "cfprApSwPhysFsmEntry": cfprApSwPhysFsmEntry,
       "cfprApSwPhysFsmInstanceId": cfprApSwPhysFsmInstanceId,
       "cfprApSwPhysFsmDn": cfprApSwPhysFsmDn,
       "cfprApSwPhysFsmRn": cfprApSwPhysFsmRn,
       "cfprApSwPhysFsmCompletionTime": cfprApSwPhysFsmCompletionTime,
       "cfprApSwPhysFsmCurrentFsm": cfprApSwPhysFsmCurrentFsm,
       "cfprApSwPhysFsmDescrData": cfprApSwPhysFsmDescrData,
       "cfprApSwPhysFsmFsmStatus": cfprApSwPhysFsmFsmStatus,
       "cfprApSwPhysFsmProgress": cfprApSwPhysFsmProgress,
       "cfprApSwPhysFsmRmtErrCode": cfprApSwPhysFsmRmtErrCode,
       "cfprApSwPhysFsmRmtErrDescr": cfprApSwPhysFsmRmtErrDescr,
       "cfprApSwPhysFsmRmtRslt": cfprApSwPhysFsmRmtRslt,
       "cfprApSwPhysFsmStageTable": cfprApSwPhysFsmStageTable,
       "cfprApSwPhysFsmStageEntry": cfprApSwPhysFsmStageEntry,
       "cfprApSwPhysFsmStageInstanceId": cfprApSwPhysFsmStageInstanceId,
       "cfprApSwPhysFsmStageDn": cfprApSwPhysFsmStageDn,
       "cfprApSwPhysFsmStageRn": cfprApSwPhysFsmStageRn,
       "cfprApSwPhysFsmStageDescrData": cfprApSwPhysFsmStageDescrData,
       "cfprApSwPhysFsmStageLastUpdateTime": cfprApSwPhysFsmStageLastUpdateTime,
       "cfprApSwPhysFsmStageName": cfprApSwPhysFsmStageName,
       "cfprApSwPhysFsmStageOrder": cfprApSwPhysFsmStageOrder,
       "cfprApSwPhysFsmStageRetry": cfprApSwPhysFsmStageRetry,
       "cfprApSwPhysFsmStageStageStatus": cfprApSwPhysFsmStageStageStatus,
       "cfprApSwPhysFsmTaskTable": cfprApSwPhysFsmTaskTable,
       "cfprApSwPhysFsmTaskEntry": cfprApSwPhysFsmTaskEntry,
       "cfprApSwPhysFsmTaskInstanceId": cfprApSwPhysFsmTaskInstanceId,
       "cfprApSwPhysFsmTaskDn": cfprApSwPhysFsmTaskDn,
       "cfprApSwPhysFsmTaskRn": cfprApSwPhysFsmTaskRn,
       "cfprApSwPhysFsmTaskCompletion": cfprApSwPhysFsmTaskCompletion,
       "cfprApSwPhysFsmTaskFlags": cfprApSwPhysFsmTaskFlags,
       "cfprApSwPhysFsmTaskItem": cfprApSwPhysFsmTaskItem,
       "cfprApSwPhysFsmTaskSeqId": cfprApSwPhysFsmTaskSeqId,
       "cfprApSwPortBreakoutTable": cfprApSwPortBreakoutTable,
       "cfprApSwPortBreakoutEntry": cfprApSwPortBreakoutEntry,
       "cfprApSwPortBreakoutInstanceId": cfprApSwPortBreakoutInstanceId,
       "cfprApSwPortBreakoutDn": cfprApSwPortBreakoutDn,
       "cfprApSwPortBreakoutRn": cfprApSwPortBreakoutRn,
       "cfprApSwPortBreakoutBreakoutType": cfprApSwPortBreakoutBreakoutType,
       "cfprApSwPortBreakoutPortId": cfprApSwPortBreakoutPortId,
       "cfprApSwPortBreakoutSlotId": cfprApSwPortBreakoutSlotId,
       "cfprApSwSspEthLanMonTable": cfprApSwSspEthLanMonTable,
       "cfprApSwSspEthLanMonEntry": cfprApSwSspEthLanMonEntry,
       "cfprApSwSspEthLanMonInstanceId": cfprApSwSspEthLanMonInstanceId,
       "cfprApSwSspEthLanMonDn": cfprApSwSspEthLanMonDn,
       "cfprApSwSspEthLanMonRn": cfprApSwSspEthLanMonRn,
       "cfprApSwSspEthLanMonLocale": cfprApSwSspEthLanMonLocale,
       "cfprApSwSspEthLanMonName": cfprApSwSspEthLanMonName,
       "cfprApSwSspEthLanMonSwitchId": cfprApSwSspEthLanMonSwitchId,
       "cfprApSwSspEthLanMonTransport": cfprApSwSspEthLanMonTransport,
       "cfprApSwSspEthLanMonType": cfprApSwSspEthLanMonType,
       "cfprApSwSspEthMonTable": cfprApSwSspEthMonTable,
       "cfprApSwSspEthMonEntry": cfprApSwSspEthMonEntry,
       "cfprApSwSspEthMonInstanceId": cfprApSwSspEthMonInstanceId,
       "cfprApSwSspEthMonDn": cfprApSwSspEthMonDn,
       "cfprApSwSspEthMonRn": cfprApSwSspEthMonRn,
       "cfprApSwSspEthMonAdminState": cfprApSwSspEthMonAdminState,
       "cfprApSwSspEthMonAppendFlag": cfprApSwSspEthMonAppendFlag,
       "cfprApSwSspEthMonDelPcap": cfprApSwSspEthMonDelPcap,
       "cfprApSwSspEthMonFsmDescr": cfprApSwSspEthMonFsmDescr,
       "cfprApSwSspEthMonFsmPrev": cfprApSwSspEthMonFsmPrev,
       "cfprApSwSspEthMonFsmProgr": cfprApSwSspEthMonFsmProgr,
       "cfprApSwSspEthMonFsmRmtInvErrCode": cfprApSwSspEthMonFsmRmtInvErrCode,
       "cfprApSwSspEthMonFsmRmtInvErrDescr": cfprApSwSspEthMonFsmRmtInvErrDescr,
       "cfprApSwSspEthMonFsmRmtInvRslt": cfprApSwSspEthMonFsmRmtInvRslt,
       "cfprApSwSspEthMonFsmStageDescr": cfprApSwSspEthMonFsmStageDescr,
       "cfprApSwSspEthMonFsmStamp": cfprApSwSspEthMonFsmStamp,
       "cfprApSwSspEthMonFsmStatus": cfprApSwSspEthMonFsmStatus,
       "cfprApSwSspEthMonFsmTry": cfprApSwSspEthMonFsmTry,
       "cfprApSwSspEthMonLifeCycle": cfprApSwSspEthMonLifeCycle,
       "cfprApSwSspEthMonName": cfprApSwSspEthMonName,
       "cfprApSwSspEthMonPeerDn": cfprApSwSspEthMonPeerDn,
       "cfprApSwSspEthMonSession": cfprApSwSspEthMonSession,
       "cfprApSwSspEthMonSessionMemUsage": cfprApSwSspEthMonSessionMemUsage,
       "cfprApSwSspEthMonSwitchId": cfprApSwSspEthMonSwitchId,
       "cfprApSwSspEthMonTransport": cfprApSwSspEthMonTransport,
       "cfprApSwSspEthMonType": cfprApSwSspEthMonType,
       "cfprApSwSspEthMonFilterEpTable": cfprApSwSspEthMonFilterEpTable,
       "cfprApSwSspEthMonFilterEpEntry": cfprApSwSspEthMonFilterEpEntry,
       "cfprApSwSspEthMonFilterEpInstanceId": cfprApSwSspEthMonFilterEpInstanceId,
       "cfprApSwSspEthMonFilterEpDn": cfprApSwSspEthMonFilterEpDn,
       "cfprApSwSspEthMonFilterEpRn": cfprApSwSspEthMonFilterEpRn,
       "cfprApSwSspEthMonFilterEpDestIp": cfprApSwSspEthMonFilterEpDestIp,
       "cfprApSwSspEthMonFilterEpDestMAC": cfprApSwSspEthMonFilterEpDestMAC,
       "cfprApSwSspEthMonFilterEpDestPort": cfprApSwSspEthMonFilterEpDestPort,
       "cfprApSwSspEthMonFilterEpEthertype": cfprApSwSspEthMonFilterEpEthertype,
       "cfprApSwSspEthMonFilterEpFilterFlag": cfprApSwSspEthMonFilterEpFilterFlag,
       "cfprApSwSspEthMonFilterEpIvlan": cfprApSwSspEthMonFilterEpIvlan,
       "cfprApSwSspEthMonFilterEpLifeCycle": cfprApSwSspEthMonFilterEpLifeCycle,
       "cfprApSwSspEthMonFilterEpNameId": cfprApSwSspEthMonFilterEpNameId,
       "cfprApSwSspEthMonFilterEpOvlan": cfprApSwSspEthMonFilterEpOvlan,
       "cfprApSwSspEthMonFilterEpPeerDn": cfprApSwSspEthMonFilterEpPeerDn,
       "cfprApSwSspEthMonFilterEpProtocol": cfprApSwSspEthMonFilterEpProtocol,
       "cfprApSwSspEthMonFilterEpRefCount": cfprApSwSspEthMonFilterEpRefCount,
       "cfprApSwSspEthMonFilterEpSrcIp": cfprApSwSspEthMonFilterEpSrcIp,
       "cfprApSwSspEthMonFilterEpSrcMAC": cfprApSwSspEthMonFilterEpSrcMAC,
       "cfprApSwSspEthMonFilterEpSrcPort": cfprApSwSspEthMonFilterEpSrcPort,
       "cfprApSwSspEthMonFsmTable": cfprApSwSspEthMonFsmTable,
       "cfprApSwSspEthMonFsmEntry": cfprApSwSspEthMonFsmEntry,
       "cfprApSwSspEthMonFsmInstanceId": cfprApSwSspEthMonFsmInstanceId,
       "cfprApSwSspEthMonFsmDn": cfprApSwSspEthMonFsmDn,
       "cfprApSwSspEthMonFsmRn": cfprApSwSspEthMonFsmRn,
       "cfprApSwSspEthMonFsmCompletionTime": cfprApSwSspEthMonFsmCompletionTime,
       "cfprApSwSspEthMonFsmCurrentFsm": cfprApSwSspEthMonFsmCurrentFsm,
       "cfprApSwSspEthMonFsmDescrData": cfprApSwSspEthMonFsmDescrData,
       "cfprApSwSspEthMonFsmFsmStatus": cfprApSwSspEthMonFsmFsmStatus,
       "cfprApSwSspEthMonFsmProgress": cfprApSwSspEthMonFsmProgress,
       "cfprApSwSspEthMonFsmRmtErrCode": cfprApSwSspEthMonFsmRmtErrCode,
       "cfprApSwSspEthMonFsmRmtErrDescr": cfprApSwSspEthMonFsmRmtErrDescr,
       "cfprApSwSspEthMonFsmRmtRslt": cfprApSwSspEthMonFsmRmtRslt,
       "cfprApSwSspEthMonFsmStageTable": cfprApSwSspEthMonFsmStageTable,
       "cfprApSwSspEthMonFsmStageEntry": cfprApSwSspEthMonFsmStageEntry,
       "cfprApSwSspEthMonFsmStageInstanceId": cfprApSwSspEthMonFsmStageInstanceId,
       "cfprApSwSspEthMonFsmStageDn": cfprApSwSspEthMonFsmStageDn,
       "cfprApSwSspEthMonFsmStageRn": cfprApSwSspEthMonFsmStageRn,
       "cfprApSwSspEthMonFsmStageDescrData": cfprApSwSspEthMonFsmStageDescrData,
       "cfprApSwSspEthMonFsmStageLastUpdateTime": cfprApSwSspEthMonFsmStageLastUpdateTime,
       "cfprApSwSspEthMonFsmStageName": cfprApSwSspEthMonFsmStageName,
       "cfprApSwSspEthMonFsmStageOrder": cfprApSwSspEthMonFsmStageOrder,
       "cfprApSwSspEthMonFsmStageRetry": cfprApSwSspEthMonFsmStageRetry,
       "cfprApSwSspEthMonFsmStageStageStatus": cfprApSwSspEthMonFsmStageStageStatus,
       "cfprApSwSspEthMonFsmTaskTable": cfprApSwSspEthMonFsmTaskTable,
       "cfprApSwSspEthMonFsmTaskEntry": cfprApSwSspEthMonFsmTaskEntry,
       "cfprApSwSspEthMonFsmTaskInstanceId": cfprApSwSspEthMonFsmTaskInstanceId,
       "cfprApSwSspEthMonFsmTaskDn": cfprApSwSspEthMonFsmTaskDn,
       "cfprApSwSspEthMonFsmTaskRn": cfprApSwSspEthMonFsmTaskRn,
       "cfprApSwSspEthMonFsmTaskCompletion": cfprApSwSspEthMonFsmTaskCompletion,
       "cfprApSwSspEthMonFsmTaskFlags": cfprApSwSspEthMonFsmTaskFlags,
       "cfprApSwSspEthMonFsmTaskItem": cfprApSwSspEthMonFsmTaskItem,
       "cfprApSwSspEthMonFsmTaskSeqId": cfprApSwSspEthMonFsmTaskSeqId,
       "cfprApSwSspEthMonSrcAppEpTable": cfprApSwSspEthMonSrcAppEpTable,
       "cfprApSwSspEthMonSrcAppEpEntry": cfprApSwSspEthMonSrcAppEpEntry,
       "cfprApSwSspEthMonSrcAppEpInstanceId": cfprApSwSspEthMonSrcAppEpInstanceId,
       "cfprApSwSspEthMonSrcAppEpDn": cfprApSwSspEthMonSrcAppEpDn,
       "cfprApSwSspEthMonSrcAppEpRn": cfprApSwSspEthMonSrcAppEpRn,
       "cfprApSwSspEthMonSrcAppEpAppName": cfprApSwSspEthMonSrcAppEpAppName,
       "cfprApSwSspEthMonSrcAppEpExternalPortDn": cfprApSwSspEthMonSrcAppEpExternalPortDn,
       "cfprApSwSspEthMonSrcAppEpFilter": cfprApSwSspEthMonSrcAppEpFilter,
       "cfprApSwSspEthMonSrcAppEpFilterDn": cfprApSwSspEthMonSrcAppEpFilterDn,
       "cfprApSwSspEthMonSrcAppEpLifeCycle": cfprApSwSspEthMonSrcAppEpLifeCycle,
       "cfprApSwSspEthMonSrcAppEpLinkName": cfprApSwSspEthMonSrcAppEpLinkName,
       "cfprApSwSspEthMonSrcAppEpPcapfile": cfprApSwSspEthMonSrcAppEpPcapfile,
       "cfprApSwSspEthMonSrcAppEpPcapfilename": cfprApSwSspEthMonSrcAppEpPcapfilename,
       "cfprApSwSspEthMonSrcAppEpPcapsize": cfprApSwSspEthMonSrcAppEpPcapsize,
       "cfprApSwSspEthMonSrcAppEpPeerDn": cfprApSwSspEthMonSrcAppEpPeerDn,
       "cfprApSwSspEthMonSrcAppEpPortChannelDn": cfprApSwSspEthMonSrcAppEpPortChannelDn,
       "cfprApSwSspEthMonSrcAppEpPortName": cfprApSwSspEthMonSrcAppEpPortName,
       "cfprApSwSspEthMonSrcAppEpSlotId": cfprApSwSspEthMonSrcAppEpSlotId,
       "cfprApSwSspEthMonSrcAppLinksEpTable": cfprApSwSspEthMonSrcAppLinksEpTable,
       "cfprApSwSspEthMonSrcAppLinksEpEntry": cfprApSwSspEthMonSrcAppLinksEpEntry,
       "cfprApSwSspEthMonSrcAppLinksEpInstanceId": cfprApSwSspEthMonSrcAppLinksEpInstanceId,
       "cfprApSwSspEthMonSrcAppLinksEpDn": cfprApSwSspEthMonSrcAppLinksEpDn,
       "cfprApSwSspEthMonSrcAppLinksEpRn": cfprApSwSspEthMonSrcAppLinksEpRn,
       "cfprApSwSspEthMonSrcAppLinksEpChassisId": cfprApSwSspEthMonSrcAppLinksEpChassisId,
       "cfprApSwSspEthMonSrcAppLinksEpEqAggrPortId": cfprApSwSspEthMonSrcAppLinksEpEqAggrPortId,
       "cfprApSwSspEthMonSrcAppLinksEpEqPortId": cfprApSwSspEthMonSrcAppLinksEpEqPortId,
       "cfprApSwSspEthMonSrcAppLinksEpEqSlotId": cfprApSwSspEthMonSrcAppLinksEpEqSlotId,
       "cfprApSwSspEthMonSrcAppLinksEpFilter": cfprApSwSspEthMonSrcAppLinksEpFilter,
       "cfprApSwSspEthMonSrcAppLinksEpFilterDn": cfprApSwSspEthMonSrcAppLinksEpFilterDn,
       "cfprApSwSspEthMonSrcAppLinksEpLifeCycle": cfprApSwSspEthMonSrcAppLinksEpLifeCycle,
       "cfprApSwSspEthMonSrcAppLinksEpName": cfprApSwSspEthMonSrcAppLinksEpName,
       "cfprApSwSspEthMonSrcAppLinksEpPcapfile": cfprApSwSspEthMonSrcAppLinksEpPcapfile,
       "cfprApSwSspEthMonSrcAppLinksEpPcapfilename": cfprApSwSspEthMonSrcAppLinksEpPcapfilename,
       "cfprApSwSspEthMonSrcAppLinksEpPcapsize": cfprApSwSspEthMonSrcAppLinksEpPcapsize,
       "cfprApSwSspEthMonSrcAppLinksEpSwitchId": cfprApSwSspEthMonSrcAppLinksEpSwitchId,
       "cfprApSwSspEthMonSrcAppLinksEpVlan": cfprApSwSspEthMonSrcAppLinksEpVlan,
       "cfprApSwSspEthMonSrcAppLinksEpVnicName1": cfprApSwSspEthMonSrcAppLinksEpVnicName1,
       "cfprApSwSspEthMonSrcPhyEpTable": cfprApSwSspEthMonSrcPhyEpTable,
       "cfprApSwSspEthMonSrcPhyEpEntry": cfprApSwSspEthMonSrcPhyEpEntry,
       "cfprApSwSspEthMonSrcPhyEpInstanceId": cfprApSwSspEthMonSrcPhyEpInstanceId,
       "cfprApSwSspEthMonSrcPhyEpDn": cfprApSwSspEthMonSrcPhyEpDn,
       "cfprApSwSspEthMonSrcPhyEpRn": cfprApSwSspEthMonSrcPhyEpRn,
       "cfprApSwSspEthMonSrcPhyEpAggrPortId": cfprApSwSspEthMonSrcPhyEpAggrPortId,
       "cfprApSwSspEthMonSrcPhyEpChassisId": cfprApSwSspEthMonSrcPhyEpChassisId,
       "cfprApSwSspEthMonSrcPhyEpFilter": cfprApSwSspEthMonSrcPhyEpFilter,
       "cfprApSwSspEthMonSrcPhyEpFilterDn": cfprApSwSspEthMonSrcPhyEpFilterDn,
       "cfprApSwSspEthMonSrcPhyEpFsmDescr": cfprApSwSspEthMonSrcPhyEpFsmDescr,
       "cfprApSwSspEthMonSrcPhyEpFsmPrev": cfprApSwSspEthMonSrcPhyEpFsmPrev,
       "cfprApSwSspEthMonSrcPhyEpFsmProgr": cfprApSwSspEthMonSrcPhyEpFsmProgr,
       "cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode": cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrCode,
       "cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr": cfprApSwSspEthMonSrcPhyEpFsmRmtInvErrDescr,
       "cfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt": cfprApSwSspEthMonSrcPhyEpFsmRmtInvRslt,
       "cfprApSwSspEthMonSrcPhyEpFsmStageDescr": cfprApSwSspEthMonSrcPhyEpFsmStageDescr,
       "cfprApSwSspEthMonSrcPhyEpFsmStamp": cfprApSwSspEthMonSrcPhyEpFsmStamp,
       "cfprApSwSspEthMonSrcPhyEpFsmStatus": cfprApSwSspEthMonSrcPhyEpFsmStatus,
       "cfprApSwSspEthMonSrcPhyEpFsmTry": cfprApSwSspEthMonSrcPhyEpFsmTry,
       "cfprApSwSspEthMonSrcPhyEpLifeCycle": cfprApSwSspEthMonSrcPhyEpLifeCycle,
       "cfprApSwSspEthMonSrcPhyEpPcapfile": cfprApSwSspEthMonSrcPhyEpPcapfile,
       "cfprApSwSspEthMonSrcPhyEpPcapfilename": cfprApSwSspEthMonSrcPhyEpPcapfilename,
       "cfprApSwSspEthMonSrcPhyEpPcapsize": cfprApSwSspEthMonSrcPhyEpPcapsize,
       "cfprApSwSspEthMonSrcPhyEpPeerDn": cfprApSwSspEthMonSrcPhyEpPeerDn,
       "cfprApSwSspEthMonSrcPhyEpPortId": cfprApSwSspEthMonSrcPhyEpPortId,
       "cfprApSwSspEthMonSrcPhyEpSlotId": cfprApSwSspEthMonSrcPhyEpSlotId,
       "cfprApSwSspEthMonSrcPhyEpSwitchId": cfprApSwSspEthMonSrcPhyEpSwitchId,
       "cfprApSwSspEthMonSrcPhyEpFsmTable": cfprApSwSspEthMonSrcPhyEpFsmTable,
       "cfprApSwSspEthMonSrcPhyEpFsmEntry": cfprApSwSspEthMonSrcPhyEpFsmEntry,
       "cfprApSwSspEthMonSrcPhyEpFsmInstanceId": cfprApSwSspEthMonSrcPhyEpFsmInstanceId,
       "cfprApSwSspEthMonSrcPhyEpFsmDn": cfprApSwSspEthMonSrcPhyEpFsmDn,
       "cfprApSwSspEthMonSrcPhyEpFsmRn": cfprApSwSspEthMonSrcPhyEpFsmRn,
       "cfprApSwSspEthMonSrcPhyEpFsmCompletionTime": cfprApSwSspEthMonSrcPhyEpFsmCompletionTime,
       "cfprApSwSspEthMonSrcPhyEpFsmCurrentFsm": cfprApSwSspEthMonSrcPhyEpFsmCurrentFsm,
       "cfprApSwSspEthMonSrcPhyEpFsmDescrData": cfprApSwSspEthMonSrcPhyEpFsmDescrData,
       "cfprApSwSspEthMonSrcPhyEpFsmFsmStatus": cfprApSwSspEthMonSrcPhyEpFsmFsmStatus,
       "cfprApSwSspEthMonSrcPhyEpFsmProgress": cfprApSwSspEthMonSrcPhyEpFsmProgress,
       "cfprApSwSspEthMonSrcPhyEpFsmRmtErrCode": cfprApSwSspEthMonSrcPhyEpFsmRmtErrCode,
       "cfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr": cfprApSwSspEthMonSrcPhyEpFsmRmtErrDescr,
       "cfprApSwSspEthMonSrcPhyEpFsmRmtRslt": cfprApSwSspEthMonSrcPhyEpFsmRmtRslt,
       "cfprApSwSspEthMonSrcPhyEpFsmStageTable": cfprApSwSspEthMonSrcPhyEpFsmStageTable,
       "cfprApSwSspEthMonSrcPhyEpFsmStageEntry": cfprApSwSspEthMonSrcPhyEpFsmStageEntry,
       "cfprApSwSspEthMonSrcPhyEpFsmStageInstanceId": cfprApSwSspEthMonSrcPhyEpFsmStageInstanceId,
       "cfprApSwSspEthMonSrcPhyEpFsmStageDn": cfprApSwSspEthMonSrcPhyEpFsmStageDn,
       "cfprApSwSspEthMonSrcPhyEpFsmStageRn": cfprApSwSspEthMonSrcPhyEpFsmStageRn,
       "cfprApSwSspEthMonSrcPhyEpFsmStageDescrData": cfprApSwSspEthMonSrcPhyEpFsmStageDescrData,
       "cfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime": cfprApSwSspEthMonSrcPhyEpFsmStageLastUpdateTime,
       "cfprApSwSspEthMonSrcPhyEpFsmStageName": cfprApSwSspEthMonSrcPhyEpFsmStageName,
       "cfprApSwSspEthMonSrcPhyEpFsmStageOrder": cfprApSwSspEthMonSrcPhyEpFsmStageOrder,
       "cfprApSwSspEthMonSrcPhyEpFsmStageRetry": cfprApSwSspEthMonSrcPhyEpFsmStageRetry,
       "cfprApSwSspEthMonSrcPhyEpFsmStageStageStatus": cfprApSwSspEthMonSrcPhyEpFsmStageStageStatus,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskTable": cfprApSwSspEthMonSrcPhyEpFsmTaskTable,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskEntry": cfprApSwSspEthMonSrcPhyEpFsmTaskEntry,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId": cfprApSwSspEthMonSrcPhyEpFsmTaskInstanceId,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskDn": cfprApSwSspEthMonSrcPhyEpFsmTaskDn,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskRn": cfprApSwSspEthMonSrcPhyEpFsmTaskRn,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskCompletion": cfprApSwSspEthMonSrcPhyEpFsmTaskCompletion,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskFlags": cfprApSwSspEthMonSrcPhyEpFsmTaskFlags,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskItem": cfprApSwSspEthMonSrcPhyEpFsmTaskItem,
       "cfprApSwSspEthMonSrcPhyEpFsmTaskSeqId": cfprApSwSspEthMonSrcPhyEpFsmTaskSeqId,
       "cfprApSwSubGroupTable": cfprApSwSubGroupTable,
       "cfprApSwSubGroupEntry": cfprApSwSubGroupEntry,
       "cfprApSwSubGroupInstanceId": cfprApSwSubGroupInstanceId,
       "cfprApSwSubGroupDn": cfprApSwSubGroupDn,
       "cfprApSwSubGroupRn": cfprApSwSubGroupRn,
       "cfprApSwSubGroupAggrPortId": cfprApSwSubGroupAggrPortId,
       "cfprApSwSubGroupLicGP": cfprApSwSubGroupLicGP,
       "cfprApSwSubGroupLicState": cfprApSwSubGroupLicState,
       "cfprApSwSubGroupLocale": cfprApSwSubGroupLocale,
       "cfprApSwSubGroupName": cfprApSwSubGroupName,
       "cfprApSwSubGroupSlotId": cfprApSwSubGroupSlotId,
       "cfprApSwSubGroupSwitchId": cfprApSwSubGroupSwitchId,
       "cfprApSwSubGroupTransport": cfprApSwSubGroupTransport,
       "cfprApSwSubGroupType": cfprApSwSubGroupType,
       "cfprApSwSystemStatsTable": cfprApSwSystemStatsTable,
       "cfprApSwSystemStatsEntry": cfprApSwSystemStatsEntry,
       "cfprApSwSystemStatsInstanceId": cfprApSwSystemStatsInstanceId,
       "cfprApSwSystemStatsDn": cfprApSwSystemStatsDn,
       "cfprApSwSystemStatsRn": cfprApSwSystemStatsRn,
       "cfprApSwSystemStatsIntervals": cfprApSwSystemStatsIntervals,
       "cfprApSwSystemStatsLoad": cfprApSwSystemStatsLoad,
       "cfprApSwSystemStatsLoadAvg": cfprApSwSystemStatsLoadAvg,
       "cfprApSwSystemStatsLoadMax": cfprApSwSystemStatsLoadMax,
       "cfprApSwSystemStatsLoadMin": cfprApSwSystemStatsLoadMin,
       "cfprApSwSystemStatsMemAvailable": cfprApSwSystemStatsMemAvailable,
       "cfprApSwSystemStatsMemAvailableAvg": cfprApSwSystemStatsMemAvailableAvg,
       "cfprApSwSystemStatsMemAvailableMax": cfprApSwSystemStatsMemAvailableMax,
       "cfprApSwSystemStatsMemAvailableMin": cfprApSwSystemStatsMemAvailableMin,
       "cfprApSwSystemStatsMemCached": cfprApSwSystemStatsMemCached,
       "cfprApSwSystemStatsMemCachedAvg": cfprApSwSystemStatsMemCachedAvg,
       "cfprApSwSystemStatsMemCachedMax": cfprApSwSystemStatsMemCachedMax,
       "cfprApSwSystemStatsMemCachedMin": cfprApSwSystemStatsMemCachedMin,
       "cfprApSwSystemStatsSuspect": cfprApSwSystemStatsSuspect,
       "cfprApSwSystemStatsThresholded": cfprApSwSystemStatsThresholded,
       "cfprApSwSystemStatsTimeCollected": cfprApSwSystemStatsTimeCollected,
       "cfprApSwSystemStatsUpdate": cfprApSwSystemStatsUpdate,
       "cfprApSwSystemStatsHistTable": cfprApSwSystemStatsHistTable,
       "cfprApSwSystemStatsHistEntry": cfprApSwSystemStatsHistEntry,
       "cfprApSwSystemStatsHistInstanceId": cfprApSwSystemStatsHistInstanceId,
       "cfprApSwSystemStatsHistDn": cfprApSwSystemStatsHistDn,
       "cfprApSwSystemStatsHistRn": cfprApSwSystemStatsHistRn,
       "cfprApSwSystemStatsHistId": cfprApSwSystemStatsHistId,
       "cfprApSwSystemStatsHistLoad": cfprApSwSystemStatsHistLoad,
       "cfprApSwSystemStatsHistLoadAvg": cfprApSwSystemStatsHistLoadAvg,
       "cfprApSwSystemStatsHistLoadMax": cfprApSwSystemStatsHistLoadMax,
       "cfprApSwSystemStatsHistLoadMin": cfprApSwSystemStatsHistLoadMin,
       "cfprApSwSystemStatsHistMemAvailable": cfprApSwSystemStatsHistMemAvailable,
       "cfprApSwSystemStatsHistMemAvailableAvg": cfprApSwSystemStatsHistMemAvailableAvg,
       "cfprApSwSystemStatsHistMemAvailableMax": cfprApSwSystemStatsHistMemAvailableMax,
       "cfprApSwSystemStatsHistMemAvailableMin": cfprApSwSystemStatsHistMemAvailableMin,
       "cfprApSwSystemStatsHistMemCached": cfprApSwSystemStatsHistMemCached,
       "cfprApSwSystemStatsHistMemCachedAvg": cfprApSwSystemStatsHistMemCachedAvg,
       "cfprApSwSystemStatsHistMemCachedMax": cfprApSwSystemStatsHistMemCachedMax,
       "cfprApSwSystemStatsHistMemCachedMin": cfprApSwSystemStatsHistMemCachedMin,
       "cfprApSwSystemStatsHistMostRecent": cfprApSwSystemStatsHistMostRecent,
       "cfprApSwSystemStatsHistSuspect": cfprApSwSystemStatsHistSuspect,
       "cfprApSwSystemStatsHistThresholded": cfprApSwSystemStatsHistThresholded,
       "cfprApSwSystemStatsHistTimeCollected": cfprApSwSystemStatsHistTimeCollected,
       "cfprApSwUlanTable": cfprApSwUlanTable,
       "cfprApSwUlanEntry": cfprApSwUlanEntry,
       "cfprApSwUlanInstanceId": cfprApSwUlanInstanceId,
       "cfprApSwUlanDn": cfprApSwUlanDn,
       "cfprApSwUlanRn": cfprApSwUlanRn,
       "cfprApSwUlanAssocPrimaryVlanState": cfprApSwUlanAssocPrimaryVlanState,
       "cfprApSwUlanAssocPrimaryVlanSwitchId": cfprApSwUlanAssocPrimaryVlanSwitchId,
       "cfprApSwUlanEpDn": cfprApSwUlanEpDn,
       "cfprApSwUlanId": cfprApSwUlanId,
       "cfprApSwUlanIfRole": cfprApSwUlanIfRole,
       "cfprApSwUlanIfType": cfprApSwUlanIfType,
       "cfprApSwUlanLocale": cfprApSwUlanLocale,
       "cfprApSwUlanName": cfprApSwUlanName,
       "cfprApSwUlanOperState": cfprApSwUlanOperState,
       "cfprApSwUlanOverlapStateForA": cfprApSwUlanOverlapStateForA,
       "cfprApSwUlanOverlapStateForB": cfprApSwUlanOverlapStateForB,
       "cfprApSwUlanPeerDn": cfprApSwUlanPeerDn,
       "cfprApSwUlanPolicyOwner": cfprApSwUlanPolicyOwner,
       "cfprApSwUlanPubNwDn": cfprApSwUlanPubNwDn,
       "cfprApSwUlanPubNwId": cfprApSwUlanPubNwId,
       "cfprApSwUlanPubNwName": cfprApSwUlanPubNwName,
       "cfprApSwUlanPurpose": cfprApSwUlanPurpose,
       "cfprApSwUlanSharing": cfprApSwUlanSharing,
       "cfprApSwUlanSwitchId": cfprApSwUlanSwitchId,
       "cfprApSwUlanTransport": cfprApSwUlanTransport,
       "cfprApSwUlanType": cfprApSwUlanType,
       "cfprApSwUlanVlanType": cfprApSwUlanVlanType,
       "cfprApSwUtilityDomainTable": cfprApSwUtilityDomainTable,
       "cfprApSwUtilityDomainEntry": cfprApSwUtilityDomainEntry,
       "cfprApSwUtilityDomainInstanceId": cfprApSwUtilityDomainInstanceId,
       "cfprApSwUtilityDomainDn": cfprApSwUtilityDomainDn,
       "cfprApSwUtilityDomainRn": cfprApSwUtilityDomainRn,
       "cfprApSwUtilityDomainFsmDescr": cfprApSwUtilityDomainFsmDescr,
       "cfprApSwUtilityDomainFsmPrev": cfprApSwUtilityDomainFsmPrev,
       "cfprApSwUtilityDomainFsmProgr": cfprApSwUtilityDomainFsmProgr,
       "cfprApSwUtilityDomainFsmRmtInvErrCode": cfprApSwUtilityDomainFsmRmtInvErrCode,
       "cfprApSwUtilityDomainFsmRmtInvErrDescr": cfprApSwUtilityDomainFsmRmtInvErrDescr,
       "cfprApSwUtilityDomainFsmRmtInvRslt": cfprApSwUtilityDomainFsmRmtInvRslt,
       "cfprApSwUtilityDomainFsmStageDescr": cfprApSwUtilityDomainFsmStageDescr,
       "cfprApSwUtilityDomainFsmStamp": cfprApSwUtilityDomainFsmStamp,
       "cfprApSwUtilityDomainFsmStatus": cfprApSwUtilityDomainFsmStatus,
       "cfprApSwUtilityDomainFsmTry": cfprApSwUtilityDomainFsmTry,
       "cfprApSwUtilityDomainLocale": cfprApSwUtilityDomainLocale,
       "cfprApSwUtilityDomainName": cfprApSwUtilityDomainName,
       "cfprApSwUtilityDomainSwitchId": cfprApSwUtilityDomainSwitchId,
       "cfprApSwUtilityDomainTransport": cfprApSwUtilityDomainTransport,
       "cfprApSwUtilityDomainType": cfprApSwUtilityDomainType,
       "cfprApSwUtilityDomainFsmTable": cfprApSwUtilityDomainFsmTable,
       "cfprApSwUtilityDomainFsmEntry": cfprApSwUtilityDomainFsmEntry,
       "cfprApSwUtilityDomainFsmInstanceId": cfprApSwUtilityDomainFsmInstanceId,
       "cfprApSwUtilityDomainFsmDn": cfprApSwUtilityDomainFsmDn,
       "cfprApSwUtilityDomainFsmRn": cfprApSwUtilityDomainFsmRn,
       "cfprApSwUtilityDomainFsmCompletionTime": cfprApSwUtilityDomainFsmCompletionTime,
       "cfprApSwUtilityDomainFsmCurrentFsm": cfprApSwUtilityDomainFsmCurrentFsm,
       "cfprApSwUtilityDomainFsmDescrData": cfprApSwUtilityDomainFsmDescrData,
       "cfprApSwUtilityDomainFsmFsmStatus": cfprApSwUtilityDomainFsmFsmStatus,
       "cfprApSwUtilityDomainFsmProgress": cfprApSwUtilityDomainFsmProgress,
       "cfprApSwUtilityDomainFsmRmtErrCode": cfprApSwUtilityDomainFsmRmtErrCode,
       "cfprApSwUtilityDomainFsmRmtErrDescr": cfprApSwUtilityDomainFsmRmtErrDescr,
       "cfprApSwUtilityDomainFsmRmtRslt": cfprApSwUtilityDomainFsmRmtRslt,
       "cfprApSwUtilityDomainFsmStageTable": cfprApSwUtilityDomainFsmStageTable,
       "cfprApSwUtilityDomainFsmStageEntry": cfprApSwUtilityDomainFsmStageEntry,
       "cfprApSwUtilityDomainFsmStageInstanceId": cfprApSwUtilityDomainFsmStageInstanceId,
       "cfprApSwUtilityDomainFsmStageDn": cfprApSwUtilityDomainFsmStageDn,
       "cfprApSwUtilityDomainFsmStageRn": cfprApSwUtilityDomainFsmStageRn,
       "cfprApSwUtilityDomainFsmStageDescrData": cfprApSwUtilityDomainFsmStageDescrData,
       "cfprApSwUtilityDomainFsmStageLastUpdateTime": cfprApSwUtilityDomainFsmStageLastUpdateTime,
       "cfprApSwUtilityDomainFsmStageName": cfprApSwUtilityDomainFsmStageName,
       "cfprApSwUtilityDomainFsmStageOrder": cfprApSwUtilityDomainFsmStageOrder,
       "cfprApSwUtilityDomainFsmStageRetry": cfprApSwUtilityDomainFsmStageRetry,
       "cfprApSwUtilityDomainFsmStageStageStatus": cfprApSwUtilityDomainFsmStageStageStatus,
       "cfprApSwUtilityDomainFsmTaskTable": cfprApSwUtilityDomainFsmTaskTable,
       "cfprApSwUtilityDomainFsmTaskEntry": cfprApSwUtilityDomainFsmTaskEntry,
       "cfprApSwUtilityDomainFsmTaskInstanceId": cfprApSwUtilityDomainFsmTaskInstanceId,
       "cfprApSwUtilityDomainFsmTaskDn": cfprApSwUtilityDomainFsmTaskDn,
       "cfprApSwUtilityDomainFsmTaskRn": cfprApSwUtilityDomainFsmTaskRn,
       "cfprApSwUtilityDomainFsmTaskCompletion": cfprApSwUtilityDomainFsmTaskCompletion,
       "cfprApSwUtilityDomainFsmTaskFlags": cfprApSwUtilityDomainFsmTaskFlags,
       "cfprApSwUtilityDomainFsmTaskItem": cfprApSwUtilityDomainFsmTaskItem,
       "cfprApSwUtilityDomainFsmTaskSeqId": cfprApSwUtilityDomainFsmTaskSeqId,
       "cfprApSwVlanTable": cfprApSwVlanTable,
       "cfprApSwVlanEntry": cfprApSwVlanEntry,
       "cfprApSwVlanInstanceId": cfprApSwVlanInstanceId,
       "cfprApSwVlanDn": cfprApSwVlanDn,
       "cfprApSwVlanRn": cfprApSwVlanRn,
       "cfprApSwVlanAssocPrimaryVlanState": cfprApSwVlanAssocPrimaryVlanState,
       "cfprApSwVlanAssocPrimaryVlanSwitchId": cfprApSwVlanAssocPrimaryVlanSwitchId,
       "cfprApSwVlanCompressionType": cfprApSwVlanCompressionType,
       "cfprApSwVlanEpDn": cfprApSwVlanEpDn,
       "cfprApSwVlanId": cfprApSwVlanId,
       "cfprApSwVlanIfRole": cfprApSwVlanIfRole,
       "cfprApSwVlanIfType": cfprApSwVlanIfType,
       "cfprApSwVlanLc": cfprApSwVlanLc,
       "cfprApSwVlanLocale": cfprApSwVlanLocale,
       "cfprApSwVlanMonTrafDir": cfprApSwVlanMonTrafDir,
       "cfprApSwVlanName": cfprApSwVlanName,
       "cfprApSwVlanOperState": cfprApSwVlanOperState,
       "cfprApSwVlanOverlapStateForA": cfprApSwVlanOverlapStateForA,
       "cfprApSwVlanOverlapStateForB": cfprApSwVlanOverlapStateForB,
       "cfprApSwVlanPeerDn": cfprApSwVlanPeerDn,
       "cfprApSwVlanPolicyOwner": cfprApSwVlanPolicyOwner,
       "cfprApSwVlanPubNwDn": cfprApSwVlanPubNwDn,
       "cfprApSwVlanPubNwId": cfprApSwVlanPubNwId,
       "cfprApSwVlanPubNwName": cfprApSwVlanPubNwName,
       "cfprApSwVlanQuerierIpAddrs": cfprApSwVlanQuerierIpAddrs,
       "cfprApSwVlanSecVlanPerPrimaryVlanCount": cfprApSwVlanSecVlanPerPrimaryVlanCount,
       "cfprApSwVlanSecVlanPerPrimaryVlanCountStatus": cfprApSwVlanSecVlanPerPrimaryVlanCountStatus,
       "cfprApSwVlanSharing": cfprApSwVlanSharing,
       "cfprApSwVlanSnoopingEnabled": cfprApSwVlanSnoopingEnabled,
       "cfprApSwVlanSwitchId": cfprApSwVlanSwitchId,
       "cfprApSwVlanTransport": cfprApSwVlanTransport,
       "cfprApSwVlanType": cfprApSwVlanType,
       "cfprApSwVlanVlanType": cfprApSwVlanVlanType,
       "cfprApSwVlanGroupTable": cfprApSwVlanGroupTable,
       "cfprApSwVlanGroupEntry": cfprApSwVlanGroupEntry,
       "cfprApSwVlanGroupInstanceId": cfprApSwVlanGroupInstanceId,
       "cfprApSwVlanGroupDn": cfprApSwVlanGroupDn,
       "cfprApSwVlanGroupRn": cfprApSwVlanGroupRn,
       "cfprApSwVlanGroupId": cfprApSwVlanGroupId,
       "cfprApSwVlanGroupPeerDn": cfprApSwVlanGroupPeerDn,
       "cfprApSwVlanGroupSwitchId": cfprApSwVlanGroupSwitchId,
       "cfprApSwVlanGroupType": cfprApSwVlanGroupType,
       "cfprApSwVlanPortNsTable": cfprApSwVlanPortNsTable,
       "cfprApSwVlanPortNsEntry": cfprApSwVlanPortNsEntry,
       "cfprApSwVlanPortNsInstanceId": cfprApSwVlanPortNsInstanceId,
       "cfprApSwVlanPortNsDn": cfprApSwVlanPortNsDn,
       "cfprApSwVlanPortNsRn": cfprApSwVlanPortNsRn,
       "cfprApSwVlanPortNsAccessVlanPortCount": cfprApSwVlanPortNsAccessVlanPortCount,
       "cfprApSwVlanPortNsAllocStatus": cfprApSwVlanPortNsAllocStatus,
       "cfprApSwVlanPortNsBorderVlanPortCount": cfprApSwVlanPortNsBorderVlanPortCount,
       "cfprApSwVlanPortNsConfigStatus": cfprApSwVlanPortNsConfigStatus,
       "cfprApSwVlanPortNsLimit": cfprApSwVlanPortNsLimit,
       "cfprApSwVlanPortNsSwitchId": cfprApSwVlanPortNsSwitchId,
       "cfprApSwVlanPortNsTotalVlanPortCount": cfprApSwVlanPortNsTotalVlanPortCount,
       "cfprApSwVlanPortNsVlanCompOffLimit": cfprApSwVlanPortNsVlanCompOffLimit,
       "cfprApSwVlanPortNsVlanCompOnLimit": cfprApSwVlanPortNsVlanCompOnLimit,
       "cfprApSwVlanPortNsOverrideTable": cfprApSwVlanPortNsOverrideTable,
       "cfprApSwVlanPortNsOverrideEntry": cfprApSwVlanPortNsOverrideEntry,
       "cfprApSwVlanPortNsOverrideInstanceId": cfprApSwVlanPortNsOverrideInstanceId,
       "cfprApSwVlanPortNsOverrideDn": cfprApSwVlanPortNsOverrideDn,
       "cfprApSwVlanPortNsOverrideRn": cfprApSwVlanPortNsOverrideRn,
       "cfprApSwVlanPortNsOverrideLimit": cfprApSwVlanPortNsOverrideLimit,
       "cfprApSwVlanRefTable": cfprApSwVlanRefTable,
       "cfprApSwVlanRefEntry": cfprApSwVlanRefEntry,
       "cfprApSwVlanRefInstanceId": cfprApSwVlanRefInstanceId,
       "cfprApSwVlanRefDn": cfprApSwVlanRefDn,
       "cfprApSwVlanRefRn": cfprApSwVlanRefRn,
       "cfprApSwVlanRefCompressionType": cfprApSwVlanRefCompressionType,
       "cfprApSwVlanRefConfigStatus": cfprApSwVlanRefConfigStatus,
       "cfprApSwVlanRefId": cfprApSwVlanRefId,
       "cfprApSwVlanRefPeerDn": cfprApSwVlanRefPeerDn,
       "cfprApSwVsanTable": cfprApSwVsanTable,
       "cfprApSwVsanEntry": cfprApSwVsanEntry,
       "cfprApSwVsanInstanceId": cfprApSwVsanInstanceId,
       "cfprApSwVsanDn": cfprApSwVsanDn,
       "cfprApSwVsanRn": cfprApSwVsanRn,
       "cfprApSwVsanDefaultZoning": cfprApSwVsanDefaultZoning,
       "cfprApSwVsanEpDn": cfprApSwVsanEpDn,
       "cfprApSwVsanFcZoneSharingMode": cfprApSwVsanFcZoneSharingMode,
       "cfprApSwVsanFcoeVlan": cfprApSwVsanFcoeVlan,
       "cfprApSwVsanFltAggr": cfprApSwVsanFltAggr,
       "cfprApSwVsanId": cfprApSwVsanId,
       "cfprApSwVsanIfRole": cfprApSwVsanIfRole,
       "cfprApSwVsanIfType": cfprApSwVsanIfType,
       "cfprApSwVsanLc": cfprApSwVsanLc,
       "cfprApSwVsanLocale": cfprApSwVsanLocale,
       "cfprApSwVsanMonTrafDir": cfprApSwVsanMonTrafDir,
       "cfprApSwVsanName": cfprApSwVsanName,
       "cfprApSwVsanOperState": cfprApSwVsanOperState,
       "cfprApSwVsanPeerDn": cfprApSwVsanPeerDn,
       "cfprApSwVsanPolicyOwner": cfprApSwVsanPolicyOwner,
       "cfprApSwVsanSwitchId": cfprApSwVsanSwitchId,
       "cfprApSwVsanTransport": cfprApSwVsanTransport,
       "cfprApSwVsanType": cfprApSwVsanType,
       "cfprApSwVsanZoningState": cfprApSwVsanZoningState,
       "cfprApSwZoneInitiatorMemberTable": cfprApSwZoneInitiatorMemberTable,
       "cfprApSwZoneInitiatorMemberEntry": cfprApSwZoneInitiatorMemberEntry,
       "cfprApSwZoneInitiatorMemberInstanceId": cfprApSwZoneInitiatorMemberInstanceId,
       "cfprApSwZoneInitiatorMemberDn": cfprApSwZoneInitiatorMemberDn,
       "cfprApSwZoneInitiatorMemberRn": cfprApSwZoneInitiatorMemberRn,
       "cfprApSwZoneInitiatorMemberEpDn": cfprApSwZoneInitiatorMemberEpDn,
       "cfprApSwZoneInitiatorMemberLc": cfprApSwZoneInitiatorMemberLc,
       "cfprApSwZoneInitiatorMemberName": cfprApSwZoneInitiatorMemberName,
       "cfprApSwZoneInitiatorMemberPeerDn": cfprApSwZoneInitiatorMemberPeerDn,
       "cfprApSwZoneInitiatorMemberWwpn": cfprApSwZoneInitiatorMemberWwpn,
       "cfprApSwZoneTargetMemberTable": cfprApSwZoneTargetMemberTable,
       "cfprApSwZoneTargetMemberEntry": cfprApSwZoneTargetMemberEntry,
       "cfprApSwZoneTargetMemberInstanceId": cfprApSwZoneTargetMemberInstanceId,
       "cfprApSwZoneTargetMemberDn": cfprApSwZoneTargetMemberDn,
       "cfprApSwZoneTargetMemberRn": cfprApSwZoneTargetMemberRn,
       "cfprApSwZoneTargetMemberEpDn": cfprApSwZoneTargetMemberEpDn,
       "cfprApSwZoneTargetMemberLc": cfprApSwZoneTargetMemberLc,
       "cfprApSwZoneTargetMemberName": cfprApSwZoneTargetMemberName,
       "cfprApSwZoneTargetMemberPeerDn": cfprApSwZoneTargetMemberPeerDn,
       "cfprApSwZoneTargetMemberWwpn": cfprApSwZoneTargetMemberWwpn}
)
