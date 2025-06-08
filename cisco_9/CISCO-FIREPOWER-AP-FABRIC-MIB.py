# SNMP MIB module (CISCO-FIREPOWER-AP-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-FABRIC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:53 2025
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

(CfprApComputeDiscovery,
 CfprApConditionRemoteInvRslt,
 CfprApEquipmentBoardAggregationRole,
 CfprApEquipmentConnectionStatus,
 CfprApEquipmentFabricEpType,
 CfprApEquipmentSlotStatus,
 CfprApFabricADceSwSrvEpTransport,
 CfprApFabricAEthEstcEpIfRole,
 CfprApFabricAEthEstcEpTransport,
 CfprApFabricAEthEstcEpType,
 CfprApFabricAEthLanEpTransport,
 CfprApFabricAFcSanEpTransport,
 CfprApFabricAFcoeSanEpTransport,
 CfprApFabricAVlanAssocPrimaryVlanSwitchId,
 CfprApFabricAVlanSharing,
 CfprApFabricAVlanTransport,
 CfprApFabricAVlanType,
 CfprApFabricAVsanTransport,
 CfprApFabricAVsanType,
 CfprApFabricAccessType,
 CfprApFabricAdminState,
 CfprApFabricBHVlanSwitchId,
 CfprApFabricBladeLifeCycle,
 CfprApFabricBreakoutPortId,
 CfprApFabricBreakoutSlotId,
 CfprApFabricBreakoutType,
 CfprApFabricCIoEpAdminState,
 CfprApFabricCIoEpIfType,
 CfprApFabricCdpLinkPolicyAdminState,
 CfprApFabricCloudType,
 CfprApFabricComputeEpIfRole,
 CfprApFabricComputeEpType,
 CfprApFabricComputePhEpAdminState,
 CfprApFabricComputeSlotEpSlotId,
 CfprApFabricConfMode,
 CfprApFabricConfState,
 CfprApFabricConfigState,
 CfprApFabricDceSwSrvEpPortId,
 CfprApFabricDceSwSrvEpSlotId,
 CfprApFabricDceSwSrvPcAdminState,
 CfprApFabricDceSwSrvPcEpPortId,
 CfprApFabricDceSwSrvPcEpSlotId,
 CfprApFabricDceSwSrvPcPortId,
 CfprApFabricDceSwSrvPcTransport,
 CfprApFabricDefaultZoningState,
 CfprApFabricEpMgrFsmCurrentFsm,
 CfprApFabricEpMgrFsmStageName,
 CfprApFabricEpMgrFsmTaskFlags,
 CfprApFabricEpMgrFsmTaskItem,
 CfprApFabricEstcPcIfRole,
 CfprApFabricEstcPcType,
 CfprApFabricEthCdpPolicyProtocol,
 CfprApFabricEthEstcEpPortId,
 CfprApFabricEthEstcEpPrio,
 CfprApFabricEthEstcEpSlotId,
 CfprApFabricEthEstcEpTransport,
 CfprApFabricEthEstcEpType,
 CfprApFabricEthEstcOperPortMode,
 CfprApFabricEthEstcPcEpPortId,
 CfprApFabricEthEstcPcEpSlotId,
 CfprApFabricEthEstcPcTransport,
 CfprApFabricEthEstcPortMode,
 CfprApFabricEthEstcTransport,
 CfprApFabricEthEstcType,
 CfprApFabricEthLanEpAdminState,
 CfprApFabricEthLanEpSpeedCap,
 CfprApFabricEthLanEpVlanStatus,
 CfprApFabricEthLanPcAdminState,
 CfprApFabricEthLanPcLacpDetach,
 CfprApFabricEthLanPcSpeedCap,
 CfprApFabricEthLanPcTransport,
 CfprApFabricEthLanPcVlanStatus,
 CfprApFabricEthLanTransport,
 CfprApFabricEthLinkPolicyType,
 CfprApFabricEthMonDestEpAdminSpeed,
 CfprApFabricEthMonDestEpIfRole,
 CfprApFabricEthMonDestEpPortId,
 CfprApFabricEthMonDestEpSlotId,
 CfprApFabricEthMonDestEpType,
 CfprApFabricEthMonFiltEpType,
 CfprApFabricEthMonFiltRefType,
 CfprApFabricEthMonLanTransport,
 CfprApFabricEthMonLanType,
 CfprApFabricEthMonSrcEpType,
 CfprApFabricEthMonSrcRefType,
 CfprApFabricEthMonTransport,
 CfprApFabricEthMonType,
 CfprApFabricEthPcProtocol,
 CfprApFabricEthSourceType,
 CfprApFabricEthTargetEpTransport,
 CfprApFabricEthUdldPolicyProtocol,
 CfprApFabricEthVlanPcTransport,
 CfprApFabricExternalEpAdminState,
 CfprApFabricExternalEpLocale,
 CfprApFabricExternalLocale,
 CfprApFabricExternalPcLocale,
 CfprApFabricFcSanEpPortId,
 CfprApFabricFcSanEpSlotId,
 CfprApFabricFcSanPcEpPortId,
 CfprApFabricFcSanPcEpSlotId,
 CfprApFabricFcSanPcTransport,
 CfprApFabricFcSanTransport,
 CfprApFabricFcSanUplinkTrunking,
 CfprApFabricFcVsanPcTransport,
 CfprApFabricFcVsanPortEpPortId,
 CfprApFabricFcVsanPortEpSlotId,
 CfprApFabricFcZoneSharingMode,
 CfprApFabricFcoeSanEpPortId,
 CfprApFabricFcoeSanEpSlotId,
 CfprApFabricFcoeSanPcEpPortId,
 CfprApFabricFcoeSanPcEpSlotId,
 CfprApFabricFcoeSanPcTransport,
 CfprApFabricFcoeVsanPcTransport,
 CfprApFabricFcoeVsanPortEpPortId,
 CfprApFabricFcoeVsanPortEpSlotId,
 CfprApFabricFillPattern,
 CfprApFabricInternalDceSrvTransport,
 CfprApFabricInternalDceSrvType,
 CfprApFabricInternalEpAdminState,
 CfprApFabricInternalEpLocale,
 CfprApFabricInternalLocale,
 CfprApFabricInternalPcLocale,
 CfprApFabricLacpMode,
 CfprApFabricLacpRate,
 CfprApFabricLacpSuspend,
 CfprApFabricLanCloudFsmCurrentFsm,
 CfprApFabricLanCloudFsmStageName,
 CfprApFabricLanCloudFsmTaskItem,
 CfprApFabricLanCloudVlanCompression,
 CfprApFabricLanEpIfRole,
 CfprApFabricLanEpType,
 CfprApFabricLanPcIfRole,
 CfprApFabricLanPcType,
 CfprApFabricLanType,
 CfprApFabricLifeCycle,
 CfprApFabricMemberStatus,
 CfprApFabricMembershipStatus,
 CfprApFabricMonAdminState,
 CfprApFabricMonOperState,
 CfprApFabricMonOperStateReason,
 CfprApFabricNetGroupSwitchId,
 CfprApFabricNetGroupType,
 CfprApFabricOwner,
 CfprApFabricPIoEpIfType,
 CfprApFabricPIoEpOperState,
 CfprApFabricPIoEpPortId,
 CfprApFabricPIoEpSlotId,
 CfprApFabricPathEpIfType,
 CfprApFabricPathEpLocale,
 CfprApFabricPcConfigStatus,
 CfprApFabricPktCaptureAppSlotId,
 CfprApFabricPoolMemberConfigIssues,
 CfprApFabricQosPrio,
 CfprApFabricQuerierType,
 CfprApFabricRecoveryAction,
 CfprApFabricReqIssues,
 CfprApFabricSSAPortType,
 CfprApFabricSanCloudFsmCurrentFsm,
 CfprApFabricSanCloudFsmStageName,
 CfprApFabricSanCloudFsmTaskItem,
 CfprApFabricSanEpIfRole,
 CfprApFabricSanEpType,
 CfprApFabricSanPcIfRole,
 CfprApFabricSanPcType,
 CfprApFabricSanType,
 CfprApFabricSlotAdminState,
 CfprApFabricSnoopingType,
 CfprApFabricSpannedCluster,
 CfprApFabricSspEthMonAppendFlag,
 CfprApFabricSspMonAdminState,
 CfprApFabricSspMonDelPcap,
 CfprApFabricSspMonOperState,
 CfprApFabricSspMonOperStateReason,
 CfprApFabricStatus,
 CfprApFabricSubGroupAggrPortId,
 CfprApFabricSubGroupConfigState,
 CfprApFabricSubGroupSlotId,
 CfprApFabricSwChEpIfRole,
 CfprApFabricSwChEpType,
 CfprApFabricSwChPhEpAdminState,
 CfprApFabricSwSrvEpIfRole,
 CfprApFabricSwSrvEpType,
 CfprApFabricSwSrvPcIfRole,
 CfprApFabricSwSrvPcType,
 CfprApFabricSwSubGroupAggrPortId,
 CfprApFabricSwSubGroupConfigState,
 CfprApFabricSwSubGroupSlotId,
 CfprApFabricSwitchingMode,
 CfprApFabricTargetEpType,
 CfprApFabricTargetStatus,
 CfprApFabricTrafficDirection,
 CfprApFabricUdldLinkPolicyAdminState,
 CfprApFabricUdldLinkPolicyMode,
 CfprApFabricUdldOperState,
 CfprApFabricVConInstType,
 CfprApFabricVConMappingScheme,
 CfprApFabricVConPlacementPref,
 CfprApFabricVConSelectPref,
 CfprApFabricVConSharePref,
 CfprApFabricVConTransportPref,
 CfprApFabricVlanAssocPrimaryVlanState,
 CfprApFabricVlanCompType,
 CfprApFabricVlanConfigIssues,
 CfprApFabricVlanOperState,
 CfprApFabricVlanOverlapState,
 CfprApFabricVlanSwitchId,
 CfprApFabricVnetEpIfRole,
 CfprApFabricVnetEpLocale,
 CfprApFabricVnetEpPolicyOwner,
 CfprApFabricVnetEpSyncEpFsmCurrentFsm,
 CfprApFabricVnetEpSyncEpFsmStageName,
 CfprApFabricVnetEpSyncEpFsmTaskItem,
 CfprApFabricVsanOperState,
 CfprApFabricVsanSwitchId,
 CfprApFabricWarnings,
 CfprApFabricZoningState,
 CfprApFsmCompletion,
 CfprApFsmFlags,
 CfprApFsmFsmStageStatus,
 CfprApLicenseState,
 CfprApNetworkConnectionType,
 CfprApNetworkLocale,
 CfprApNetworkPortOperState,
 CfprApNetworkPortRole,
 CfprApNetworkSide,
 CfprApNetworkSwitchId,
 CfprApNetworkTransport,
 CfprApNetworkVnetEpIfType,
 CfprApNhTpHashType,
 CfprApPolicyPolicyOwner,
 CfprApPoolPoolAssignmentOrder,
 CfprApPortDuplex,
 CfprApPortEthAdminSpeed,
 CfprApPortEthSpeed,
 CfprApPortSpeed,
 CfprApQosPriority,
 CfprApSwPktCaptureLifeCycle) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApComputeDiscovery",
    "CfprApConditionRemoteInvRslt",
    "CfprApEquipmentBoardAggregationRole",
    "CfprApEquipmentConnectionStatus",
    "CfprApEquipmentFabricEpType",
    "CfprApEquipmentSlotStatus",
    "CfprApFabricADceSwSrvEpTransport",
    "CfprApFabricAEthEstcEpIfRole",
    "CfprApFabricAEthEstcEpTransport",
    "CfprApFabricAEthEstcEpType",
    "CfprApFabricAEthLanEpTransport",
    "CfprApFabricAFcSanEpTransport",
    "CfprApFabricAFcoeSanEpTransport",
    "CfprApFabricAVlanAssocPrimaryVlanSwitchId",
    "CfprApFabricAVlanSharing",
    "CfprApFabricAVlanTransport",
    "CfprApFabricAVlanType",
    "CfprApFabricAVsanTransport",
    "CfprApFabricAVsanType",
    "CfprApFabricAccessType",
    "CfprApFabricAdminState",
    "CfprApFabricBHVlanSwitchId",
    "CfprApFabricBladeLifeCycle",
    "CfprApFabricBreakoutPortId",
    "CfprApFabricBreakoutSlotId",
    "CfprApFabricBreakoutType",
    "CfprApFabricCIoEpAdminState",
    "CfprApFabricCIoEpIfType",
    "CfprApFabricCdpLinkPolicyAdminState",
    "CfprApFabricCloudType",
    "CfprApFabricComputeEpIfRole",
    "CfprApFabricComputeEpType",
    "CfprApFabricComputePhEpAdminState",
    "CfprApFabricComputeSlotEpSlotId",
    "CfprApFabricConfMode",
    "CfprApFabricConfState",
    "CfprApFabricConfigState",
    "CfprApFabricDceSwSrvEpPortId",
    "CfprApFabricDceSwSrvEpSlotId",
    "CfprApFabricDceSwSrvPcAdminState",
    "CfprApFabricDceSwSrvPcEpPortId",
    "CfprApFabricDceSwSrvPcEpSlotId",
    "CfprApFabricDceSwSrvPcPortId",
    "CfprApFabricDceSwSrvPcTransport",
    "CfprApFabricDefaultZoningState",
    "CfprApFabricEpMgrFsmCurrentFsm",
    "CfprApFabricEpMgrFsmStageName",
    "CfprApFabricEpMgrFsmTaskFlags",
    "CfprApFabricEpMgrFsmTaskItem",
    "CfprApFabricEstcPcIfRole",
    "CfprApFabricEstcPcType",
    "CfprApFabricEthCdpPolicyProtocol",
    "CfprApFabricEthEstcEpPortId",
    "CfprApFabricEthEstcEpPrio",
    "CfprApFabricEthEstcEpSlotId",
    "CfprApFabricEthEstcEpTransport",
    "CfprApFabricEthEstcEpType",
    "CfprApFabricEthEstcOperPortMode",
    "CfprApFabricEthEstcPcEpPortId",
    "CfprApFabricEthEstcPcEpSlotId",
    "CfprApFabricEthEstcPcTransport",
    "CfprApFabricEthEstcPortMode",
    "CfprApFabricEthEstcTransport",
    "CfprApFabricEthEstcType",
    "CfprApFabricEthLanEpAdminState",
    "CfprApFabricEthLanEpSpeedCap",
    "CfprApFabricEthLanEpVlanStatus",
    "CfprApFabricEthLanPcAdminState",
    "CfprApFabricEthLanPcLacpDetach",
    "CfprApFabricEthLanPcSpeedCap",
    "CfprApFabricEthLanPcTransport",
    "CfprApFabricEthLanPcVlanStatus",
    "CfprApFabricEthLanTransport",
    "CfprApFabricEthLinkPolicyType",
    "CfprApFabricEthMonDestEpAdminSpeed",
    "CfprApFabricEthMonDestEpIfRole",
    "CfprApFabricEthMonDestEpPortId",
    "CfprApFabricEthMonDestEpSlotId",
    "CfprApFabricEthMonDestEpType",
    "CfprApFabricEthMonFiltEpType",
    "CfprApFabricEthMonFiltRefType",
    "CfprApFabricEthMonLanTransport",
    "CfprApFabricEthMonLanType",
    "CfprApFabricEthMonSrcEpType",
    "CfprApFabricEthMonSrcRefType",
    "CfprApFabricEthMonTransport",
    "CfprApFabricEthMonType",
    "CfprApFabricEthPcProtocol",
    "CfprApFabricEthSourceType",
    "CfprApFabricEthTargetEpTransport",
    "CfprApFabricEthUdldPolicyProtocol",
    "CfprApFabricEthVlanPcTransport",
    "CfprApFabricExternalEpAdminState",
    "CfprApFabricExternalEpLocale",
    "CfprApFabricExternalLocale",
    "CfprApFabricExternalPcLocale",
    "CfprApFabricFcSanEpPortId",
    "CfprApFabricFcSanEpSlotId",
    "CfprApFabricFcSanPcEpPortId",
    "CfprApFabricFcSanPcEpSlotId",
    "CfprApFabricFcSanPcTransport",
    "CfprApFabricFcSanTransport",
    "CfprApFabricFcSanUplinkTrunking",
    "CfprApFabricFcVsanPcTransport",
    "CfprApFabricFcVsanPortEpPortId",
    "CfprApFabricFcVsanPortEpSlotId",
    "CfprApFabricFcZoneSharingMode",
    "CfprApFabricFcoeSanEpPortId",
    "CfprApFabricFcoeSanEpSlotId",
    "CfprApFabricFcoeSanPcEpPortId",
    "CfprApFabricFcoeSanPcEpSlotId",
    "CfprApFabricFcoeSanPcTransport",
    "CfprApFabricFcoeVsanPcTransport",
    "CfprApFabricFcoeVsanPortEpPortId",
    "CfprApFabricFcoeVsanPortEpSlotId",
    "CfprApFabricFillPattern",
    "CfprApFabricInternalDceSrvTransport",
    "CfprApFabricInternalDceSrvType",
    "CfprApFabricInternalEpAdminState",
    "CfprApFabricInternalEpLocale",
    "CfprApFabricInternalLocale",
    "CfprApFabricInternalPcLocale",
    "CfprApFabricLacpMode",
    "CfprApFabricLacpRate",
    "CfprApFabricLacpSuspend",
    "CfprApFabricLanCloudFsmCurrentFsm",
    "CfprApFabricLanCloudFsmStageName",
    "CfprApFabricLanCloudFsmTaskItem",
    "CfprApFabricLanCloudVlanCompression",
    "CfprApFabricLanEpIfRole",
    "CfprApFabricLanEpType",
    "CfprApFabricLanPcIfRole",
    "CfprApFabricLanPcType",
    "CfprApFabricLanType",
    "CfprApFabricLifeCycle",
    "CfprApFabricMemberStatus",
    "CfprApFabricMembershipStatus",
    "CfprApFabricMonAdminState",
    "CfprApFabricMonOperState",
    "CfprApFabricMonOperStateReason",
    "CfprApFabricNetGroupSwitchId",
    "CfprApFabricNetGroupType",
    "CfprApFabricOwner",
    "CfprApFabricPIoEpIfType",
    "CfprApFabricPIoEpOperState",
    "CfprApFabricPIoEpPortId",
    "CfprApFabricPIoEpSlotId",
    "CfprApFabricPathEpIfType",
    "CfprApFabricPathEpLocale",
    "CfprApFabricPcConfigStatus",
    "CfprApFabricPktCaptureAppSlotId",
    "CfprApFabricPoolMemberConfigIssues",
    "CfprApFabricQosPrio",
    "CfprApFabricQuerierType",
    "CfprApFabricRecoveryAction",
    "CfprApFabricReqIssues",
    "CfprApFabricSSAPortType",
    "CfprApFabricSanCloudFsmCurrentFsm",
    "CfprApFabricSanCloudFsmStageName",
    "CfprApFabricSanCloudFsmTaskItem",
    "CfprApFabricSanEpIfRole",
    "CfprApFabricSanEpType",
    "CfprApFabricSanPcIfRole",
    "CfprApFabricSanPcType",
    "CfprApFabricSanType",
    "CfprApFabricSlotAdminState",
    "CfprApFabricSnoopingType",
    "CfprApFabricSpannedCluster",
    "CfprApFabricSspEthMonAppendFlag",
    "CfprApFabricSspMonAdminState",
    "CfprApFabricSspMonDelPcap",
    "CfprApFabricSspMonOperState",
    "CfprApFabricSspMonOperStateReason",
    "CfprApFabricStatus",
    "CfprApFabricSubGroupAggrPortId",
    "CfprApFabricSubGroupConfigState",
    "CfprApFabricSubGroupSlotId",
    "CfprApFabricSwChEpIfRole",
    "CfprApFabricSwChEpType",
    "CfprApFabricSwChPhEpAdminState",
    "CfprApFabricSwSrvEpIfRole",
    "CfprApFabricSwSrvEpType",
    "CfprApFabricSwSrvPcIfRole",
    "CfprApFabricSwSrvPcType",
    "CfprApFabricSwSubGroupAggrPortId",
    "CfprApFabricSwSubGroupConfigState",
    "CfprApFabricSwSubGroupSlotId",
    "CfprApFabricSwitchingMode",
    "CfprApFabricTargetEpType",
    "CfprApFabricTargetStatus",
    "CfprApFabricTrafficDirection",
    "CfprApFabricUdldLinkPolicyAdminState",
    "CfprApFabricUdldLinkPolicyMode",
    "CfprApFabricUdldOperState",
    "CfprApFabricVConInstType",
    "CfprApFabricVConMappingScheme",
    "CfprApFabricVConPlacementPref",
    "CfprApFabricVConSelectPref",
    "CfprApFabricVConSharePref",
    "CfprApFabricVConTransportPref",
    "CfprApFabricVlanAssocPrimaryVlanState",
    "CfprApFabricVlanCompType",
    "CfprApFabricVlanConfigIssues",
    "CfprApFabricVlanOperState",
    "CfprApFabricVlanOverlapState",
    "CfprApFabricVlanSwitchId",
    "CfprApFabricVnetEpIfRole",
    "CfprApFabricVnetEpLocale",
    "CfprApFabricVnetEpPolicyOwner",
    "CfprApFabricVnetEpSyncEpFsmCurrentFsm",
    "CfprApFabricVnetEpSyncEpFsmStageName",
    "CfprApFabricVnetEpSyncEpFsmTaskItem",
    "CfprApFabricVsanOperState",
    "CfprApFabricVsanSwitchId",
    "CfprApFabricWarnings",
    "CfprApFabricZoningState",
    "CfprApFsmCompletion",
    "CfprApFsmFlags",
    "CfprApFsmFsmStageStatus",
    "CfprApLicenseState",
    "CfprApNetworkConnectionType",
    "CfprApNetworkLocale",
    "CfprApNetworkPortOperState",
    "CfprApNetworkPortRole",
    "CfprApNetworkSide",
    "CfprApNetworkSwitchId",
    "CfprApNetworkTransport",
    "CfprApNetworkVnetEpIfType",
    "CfprApNhTpHashType",
    "CfprApPolicyPolicyOwner",
    "CfprApPoolPoolAssignmentOrder",
    "CfprApPortDuplex",
    "CfprApPortEthAdminSpeed",
    "CfprApPortEthSpeed",
    "CfprApPortSpeed",
    "CfprApQosPriority",
    "CfprApSwPktCaptureLifeCycle")

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

cfprApFabricObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApFabricBHVlanTable_Object = MibTable
cfprApFabricBHVlanTable = _CfprApFabricBHVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1)
)
if mibBuilder.loadTexts:
    cfprApFabricBHVlanTable.setStatus("current")
_CfprApFabricBHVlanEntry_Object = MibTableRow
cfprApFabricBHVlanEntry = _CfprApFabricBHVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1)
)
cfprApFabricBHVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricBHVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricBHVlanEntry.setStatus("current")
_CfprApFabricBHVlanInstanceId_Type = CfprApManagedObjectId
_CfprApFabricBHVlanInstanceId_Object = MibTableColumn
cfprApFabricBHVlanInstanceId = _CfprApFabricBHVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 1),
    _CfprApFabricBHVlanInstanceId_Type()
)
cfprApFabricBHVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanInstanceId.setStatus("current")
_CfprApFabricBHVlanDn_Type = CfprApManagedObjectDn
_CfprApFabricBHVlanDn_Object = MibTableColumn
cfprApFabricBHVlanDn = _CfprApFabricBHVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 2),
    _CfprApFabricBHVlanDn_Type()
)
cfprApFabricBHVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanDn.setStatus("current")
_CfprApFabricBHVlanRn_Type = SnmpAdminString
_CfprApFabricBHVlanRn_Object = MibTableColumn
cfprApFabricBHVlanRn = _CfprApFabricBHVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 3),
    _CfprApFabricBHVlanRn_Type()
)
cfprApFabricBHVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanRn.setStatus("current")
_CfprApFabricBHVlanAssocPrimaryVlanState_Type = CfprApFabricVlanAssocPrimaryVlanState
_CfprApFabricBHVlanAssocPrimaryVlanState_Object = MibTableColumn
cfprApFabricBHVlanAssocPrimaryVlanState = _CfprApFabricBHVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 4),
    _CfprApFabricBHVlanAssocPrimaryVlanState_Type()
)
cfprApFabricBHVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanAssocPrimaryVlanState.setStatus("current")
_CfprApFabricBHVlanAssocPrimaryVlanSwitchId_Type = CfprApFabricAVlanAssocPrimaryVlanSwitchId
_CfprApFabricBHVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprApFabricBHVlanAssocPrimaryVlanSwitchId = _CfprApFabricBHVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 5),
    _CfprApFabricBHVlanAssocPrimaryVlanSwitchId_Type()
)
cfprApFabricBHVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprApFabricBHVlanEpDn_Type = SnmpAdminString
_CfprApFabricBHVlanEpDn_Object = MibTableColumn
cfprApFabricBHVlanEpDn = _CfprApFabricBHVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 6),
    _CfprApFabricBHVlanEpDn_Type()
)
cfprApFabricBHVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanEpDn.setStatus("current")
_CfprApFabricBHVlanId_Type = Gauge32
_CfprApFabricBHVlanId_Object = MibTableColumn
cfprApFabricBHVlanId = _CfprApFabricBHVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 7),
    _CfprApFabricBHVlanId_Type()
)
cfprApFabricBHVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanId.setStatus("current")
_CfprApFabricBHVlanIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApFabricBHVlanIfRole_Object = MibTableColumn
cfprApFabricBHVlanIfRole = _CfprApFabricBHVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 8),
    _CfprApFabricBHVlanIfRole_Type()
)
cfprApFabricBHVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanIfRole.setStatus("current")
_CfprApFabricBHVlanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApFabricBHVlanIfType_Object = MibTableColumn
cfprApFabricBHVlanIfType = _CfprApFabricBHVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 9),
    _CfprApFabricBHVlanIfType_Type()
)
cfprApFabricBHVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanIfType.setStatus("current")
_CfprApFabricBHVlanLocale_Type = CfprApFabricVnetEpLocale
_CfprApFabricBHVlanLocale_Object = MibTableColumn
cfprApFabricBHVlanLocale = _CfprApFabricBHVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 10),
    _CfprApFabricBHVlanLocale_Type()
)
cfprApFabricBHVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanLocale.setStatus("current")
_CfprApFabricBHVlanName_Type = SnmpAdminString
_CfprApFabricBHVlanName_Object = MibTableColumn
cfprApFabricBHVlanName = _CfprApFabricBHVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 11),
    _CfprApFabricBHVlanName_Type()
)
cfprApFabricBHVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanName.setStatus("current")
_CfprApFabricBHVlanOperState_Type = CfprApFabricVlanOperState
_CfprApFabricBHVlanOperState_Object = MibTableColumn
cfprApFabricBHVlanOperState = _CfprApFabricBHVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 12),
    _CfprApFabricBHVlanOperState_Type()
)
cfprApFabricBHVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanOperState.setStatus("current")
_CfprApFabricBHVlanOverlapStateForA_Type = CfprApFabricVlanOverlapState
_CfprApFabricBHVlanOverlapStateForA_Object = MibTableColumn
cfprApFabricBHVlanOverlapStateForA = _CfprApFabricBHVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 13),
    _CfprApFabricBHVlanOverlapStateForA_Type()
)
cfprApFabricBHVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanOverlapStateForA.setStatus("current")
_CfprApFabricBHVlanOverlapStateForB_Type = CfprApFabricVlanOverlapState
_CfprApFabricBHVlanOverlapStateForB_Object = MibTableColumn
cfprApFabricBHVlanOverlapStateForB = _CfprApFabricBHVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 14),
    _CfprApFabricBHVlanOverlapStateForB_Type()
)
cfprApFabricBHVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanOverlapStateForB.setStatus("current")
_CfprApFabricBHVlanPeerDn_Type = SnmpAdminString
_CfprApFabricBHVlanPeerDn_Object = MibTableColumn
cfprApFabricBHVlanPeerDn = _CfprApFabricBHVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 15),
    _CfprApFabricBHVlanPeerDn_Type()
)
cfprApFabricBHVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanPeerDn.setStatus("current")
_CfprApFabricBHVlanPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApFabricBHVlanPolicyOwner_Object = MibTableColumn
cfprApFabricBHVlanPolicyOwner = _CfprApFabricBHVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 16),
    _CfprApFabricBHVlanPolicyOwner_Type()
)
cfprApFabricBHVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanPolicyOwner.setStatus("current")
_CfprApFabricBHVlanPubNwDn_Type = SnmpAdminString
_CfprApFabricBHVlanPubNwDn_Object = MibTableColumn
cfprApFabricBHVlanPubNwDn = _CfprApFabricBHVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 17),
    _CfprApFabricBHVlanPubNwDn_Type()
)
cfprApFabricBHVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanPubNwDn.setStatus("current")
_CfprApFabricBHVlanPubNwId_Type = Gauge32
_CfprApFabricBHVlanPubNwId_Object = MibTableColumn
cfprApFabricBHVlanPubNwId = _CfprApFabricBHVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 18),
    _CfprApFabricBHVlanPubNwId_Type()
)
cfprApFabricBHVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanPubNwId.setStatus("current")
_CfprApFabricBHVlanPubNwName_Type = SnmpAdminString
_CfprApFabricBHVlanPubNwName_Object = MibTableColumn
cfprApFabricBHVlanPubNwName = _CfprApFabricBHVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 19),
    _CfprApFabricBHVlanPubNwName_Type()
)
cfprApFabricBHVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanPubNwName.setStatus("current")
_CfprApFabricBHVlanSharing_Type = CfprApFabricAVlanSharing
_CfprApFabricBHVlanSharing_Object = MibTableColumn
cfprApFabricBHVlanSharing = _CfprApFabricBHVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 20),
    _CfprApFabricBHVlanSharing_Type()
)
cfprApFabricBHVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanSharing.setStatus("current")
_CfprApFabricBHVlanSwitchId_Type = CfprApFabricBHVlanSwitchId
_CfprApFabricBHVlanSwitchId_Object = MibTableColumn
cfprApFabricBHVlanSwitchId = _CfprApFabricBHVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 21),
    _CfprApFabricBHVlanSwitchId_Type()
)
cfprApFabricBHVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanSwitchId.setStatus("current")
_CfprApFabricBHVlanTransport_Type = CfprApFabricAVlanTransport
_CfprApFabricBHVlanTransport_Object = MibTableColumn
cfprApFabricBHVlanTransport = _CfprApFabricBHVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 22),
    _CfprApFabricBHVlanTransport_Type()
)
cfprApFabricBHVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanTransport.setStatus("current")
_CfprApFabricBHVlanType_Type = CfprApFabricAVlanType
_CfprApFabricBHVlanType_Object = MibTableColumn
cfprApFabricBHVlanType = _CfprApFabricBHVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 1, 1, 23),
    _CfprApFabricBHVlanType_Type()
)
cfprApFabricBHVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBHVlanType.setStatus("current")
_CfprApFabricBreakoutTable_Object = MibTable
cfprApFabricBreakoutTable = _CfprApFabricBreakoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 2)
)
if mibBuilder.loadTexts:
    cfprApFabricBreakoutTable.setStatus("current")
_CfprApFabricBreakoutEntry_Object = MibTableRow
cfprApFabricBreakoutEntry = _CfprApFabricBreakoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 2, 1)
)
cfprApFabricBreakoutEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricBreakoutInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricBreakoutEntry.setStatus("current")
_CfprApFabricBreakoutInstanceId_Type = CfprApManagedObjectId
_CfprApFabricBreakoutInstanceId_Object = MibTableColumn
cfprApFabricBreakoutInstanceId = _CfprApFabricBreakoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 2, 1, 1),
    _CfprApFabricBreakoutInstanceId_Type()
)
cfprApFabricBreakoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricBreakoutInstanceId.setStatus("current")
_CfprApFabricBreakoutDn_Type = CfprApManagedObjectDn
_CfprApFabricBreakoutDn_Object = MibTableColumn
cfprApFabricBreakoutDn = _CfprApFabricBreakoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 2, 1, 2),
    _CfprApFabricBreakoutDn_Type()
)
cfprApFabricBreakoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBreakoutDn.setStatus("current")
_CfprApFabricBreakoutRn_Type = SnmpAdminString
_CfprApFabricBreakoutRn_Object = MibTableColumn
cfprApFabricBreakoutRn = _CfprApFabricBreakoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 2, 1, 3),
    _CfprApFabricBreakoutRn_Type()
)
cfprApFabricBreakoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBreakoutRn.setStatus("current")
_CfprApFabricBreakoutBreakoutType_Type = CfprApFabricBreakoutType
_CfprApFabricBreakoutBreakoutType_Object = MibTableColumn
cfprApFabricBreakoutBreakoutType = _CfprApFabricBreakoutBreakoutType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 2, 1, 4),
    _CfprApFabricBreakoutBreakoutType_Type()
)
cfprApFabricBreakoutBreakoutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBreakoutBreakoutType.setStatus("current")
_CfprApFabricBreakoutPortId_Type = CfprApFabricBreakoutPortId
_CfprApFabricBreakoutPortId_Object = MibTableColumn
cfprApFabricBreakoutPortId = _CfprApFabricBreakoutPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 2, 1, 5),
    _CfprApFabricBreakoutPortId_Type()
)
cfprApFabricBreakoutPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBreakoutPortId.setStatus("current")
_CfprApFabricBreakoutSlotId_Type = CfprApFabricBreakoutSlotId
_CfprApFabricBreakoutSlotId_Object = MibTableColumn
cfprApFabricBreakoutSlotId = _CfprApFabricBreakoutSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 2, 1, 6),
    _CfprApFabricBreakoutSlotId_Type()
)
cfprApFabricBreakoutSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricBreakoutSlotId.setStatus("current")
_CfprApFabricCablingSwTable_Object = MibTable
cfprApFabricCablingSwTable = _CfprApFabricCablingSwTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4)
)
if mibBuilder.loadTexts:
    cfprApFabricCablingSwTable.setStatus("current")
_CfprApFabricCablingSwEntry_Object = MibTableRow
cfprApFabricCablingSwEntry = _CfprApFabricCablingSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1)
)
cfprApFabricCablingSwEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricCablingSwInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricCablingSwEntry.setStatus("current")
_CfprApFabricCablingSwInstanceId_Type = CfprApManagedObjectId
_CfprApFabricCablingSwInstanceId_Object = MibTableColumn
cfprApFabricCablingSwInstanceId = _CfprApFabricCablingSwInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1, 1),
    _CfprApFabricCablingSwInstanceId_Type()
)
cfprApFabricCablingSwInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricCablingSwInstanceId.setStatus("current")
_CfprApFabricCablingSwDn_Type = CfprApManagedObjectDn
_CfprApFabricCablingSwDn_Object = MibTableColumn
cfprApFabricCablingSwDn = _CfprApFabricCablingSwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1, 2),
    _CfprApFabricCablingSwDn_Type()
)
cfprApFabricCablingSwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCablingSwDn.setStatus("current")
_CfprApFabricCablingSwRn_Type = SnmpAdminString
_CfprApFabricCablingSwRn_Object = MibTableColumn
cfprApFabricCablingSwRn = _CfprApFabricCablingSwRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1, 3),
    _CfprApFabricCablingSwRn_Type()
)
cfprApFabricCablingSwRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCablingSwRn.setStatus("current")
_CfprApFabricCablingSwId_Type = CfprApNetworkSwitchId
_CfprApFabricCablingSwId_Object = MibTableColumn
cfprApFabricCablingSwId = _CfprApFabricCablingSwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1, 4),
    _CfprApFabricCablingSwId_Type()
)
cfprApFabricCablingSwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCablingSwId.setStatus("current")
_CfprApFabricCablingSwLocale_Type = CfprApFabricExternalLocale
_CfprApFabricCablingSwLocale_Object = MibTableColumn
cfprApFabricCablingSwLocale = _CfprApFabricCablingSwLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1, 5),
    _CfprApFabricCablingSwLocale_Type()
)
cfprApFabricCablingSwLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCablingSwLocale.setStatus("current")
_CfprApFabricCablingSwName_Type = SnmpAdminString
_CfprApFabricCablingSwName_Object = MibTableColumn
cfprApFabricCablingSwName = _CfprApFabricCablingSwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1, 6),
    _CfprApFabricCablingSwName_Type()
)
cfprApFabricCablingSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCablingSwName.setStatus("current")
_CfprApFabricCablingSwTransport_Type = CfprApNetworkTransport
_CfprApFabricCablingSwTransport_Object = MibTableColumn
cfprApFabricCablingSwTransport = _CfprApFabricCablingSwTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1, 7),
    _CfprApFabricCablingSwTransport_Type()
)
cfprApFabricCablingSwTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCablingSwTransport.setStatus("current")
_CfprApFabricCablingSwType_Type = CfprApNetworkConnectionType
_CfprApFabricCablingSwType_Object = MibTableColumn
cfprApFabricCablingSwType = _CfprApFabricCablingSwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 4, 1, 8),
    _CfprApFabricCablingSwType_Type()
)
cfprApFabricCablingSwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCablingSwType.setStatus("current")
_CfprApFabricCdpLinkPolicyTable_Object = MibTable
cfprApFabricCdpLinkPolicyTable = _CfprApFabricCdpLinkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5)
)
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyTable.setStatus("current")
_CfprApFabricCdpLinkPolicyEntry_Object = MibTableRow
cfprApFabricCdpLinkPolicyEntry = _CfprApFabricCdpLinkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1)
)
cfprApFabricCdpLinkPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricCdpLinkPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyEntry.setStatus("current")
_CfprApFabricCdpLinkPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFabricCdpLinkPolicyInstanceId_Object = MibTableColumn
cfprApFabricCdpLinkPolicyInstanceId = _CfprApFabricCdpLinkPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 1),
    _CfprApFabricCdpLinkPolicyInstanceId_Type()
)
cfprApFabricCdpLinkPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyInstanceId.setStatus("current")
_CfprApFabricCdpLinkPolicyDn_Type = CfprApManagedObjectDn
_CfprApFabricCdpLinkPolicyDn_Object = MibTableColumn
cfprApFabricCdpLinkPolicyDn = _CfprApFabricCdpLinkPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 2),
    _CfprApFabricCdpLinkPolicyDn_Type()
)
cfprApFabricCdpLinkPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyDn.setStatus("current")
_CfprApFabricCdpLinkPolicyRn_Type = SnmpAdminString
_CfprApFabricCdpLinkPolicyRn_Object = MibTableColumn
cfprApFabricCdpLinkPolicyRn = _CfprApFabricCdpLinkPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 3),
    _CfprApFabricCdpLinkPolicyRn_Type()
)
cfprApFabricCdpLinkPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyRn.setStatus("current")
_CfprApFabricCdpLinkPolicyAdminState_Type = CfprApFabricCdpLinkPolicyAdminState
_CfprApFabricCdpLinkPolicyAdminState_Object = MibTableColumn
cfprApFabricCdpLinkPolicyAdminState = _CfprApFabricCdpLinkPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 4),
    _CfprApFabricCdpLinkPolicyAdminState_Type()
)
cfprApFabricCdpLinkPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyAdminState.setStatus("current")
_CfprApFabricCdpLinkPolicyDescr_Type = SnmpAdminString
_CfprApFabricCdpLinkPolicyDescr_Object = MibTableColumn
cfprApFabricCdpLinkPolicyDescr = _CfprApFabricCdpLinkPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 5),
    _CfprApFabricCdpLinkPolicyDescr_Type()
)
cfprApFabricCdpLinkPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyDescr.setStatus("current")
_CfprApFabricCdpLinkPolicyIntId_Type = SnmpAdminString
_CfprApFabricCdpLinkPolicyIntId_Object = MibTableColumn
cfprApFabricCdpLinkPolicyIntId = _CfprApFabricCdpLinkPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 6),
    _CfprApFabricCdpLinkPolicyIntId_Type()
)
cfprApFabricCdpLinkPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyIntId.setStatus("current")
_CfprApFabricCdpLinkPolicyName_Type = SnmpAdminString
_CfprApFabricCdpLinkPolicyName_Object = MibTableColumn
cfprApFabricCdpLinkPolicyName = _CfprApFabricCdpLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 7),
    _CfprApFabricCdpLinkPolicyName_Type()
)
cfprApFabricCdpLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyName.setStatus("current")
_CfprApFabricCdpLinkPolicyPolicyLevel_Type = Gauge32
_CfprApFabricCdpLinkPolicyPolicyLevel_Object = MibTableColumn
cfprApFabricCdpLinkPolicyPolicyLevel = _CfprApFabricCdpLinkPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 8),
    _CfprApFabricCdpLinkPolicyPolicyLevel_Type()
)
cfprApFabricCdpLinkPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyPolicyLevel.setStatus("current")
_CfprApFabricCdpLinkPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricCdpLinkPolicyPolicyOwner_Object = MibTableColumn
cfprApFabricCdpLinkPolicyPolicyOwner = _CfprApFabricCdpLinkPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 9),
    _CfprApFabricCdpLinkPolicyPolicyOwner_Type()
)
cfprApFabricCdpLinkPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyPolicyOwner.setStatus("current")
_CfprApFabricCdpLinkPolicyProtocol_Type = CfprApFabricEthCdpPolicyProtocol
_CfprApFabricCdpLinkPolicyProtocol_Object = MibTableColumn
cfprApFabricCdpLinkPolicyProtocol = _CfprApFabricCdpLinkPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 10),
    _CfprApFabricCdpLinkPolicyProtocol_Type()
)
cfprApFabricCdpLinkPolicyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyProtocol.setStatus("current")
_CfprApFabricCdpLinkPolicyType_Type = CfprApFabricEthLinkPolicyType
_CfprApFabricCdpLinkPolicyType_Object = MibTableColumn
cfprApFabricCdpLinkPolicyType = _CfprApFabricCdpLinkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 5, 1, 11),
    _CfprApFabricCdpLinkPolicyType_Type()
)
cfprApFabricCdpLinkPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricCdpLinkPolicyType.setStatus("current")
_CfprApFabricChangedObjectRefTable_Object = MibTable
cfprApFabricChangedObjectRefTable = _CfprApFabricChangedObjectRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6)
)
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefTable.setStatus("current")
_CfprApFabricChangedObjectRefEntry_Object = MibTableRow
cfprApFabricChangedObjectRefEntry = _CfprApFabricChangedObjectRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1)
)
cfprApFabricChangedObjectRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricChangedObjectRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefEntry.setStatus("current")
_CfprApFabricChangedObjectRefInstanceId_Type = CfprApManagedObjectId
_CfprApFabricChangedObjectRefInstanceId_Object = MibTableColumn
cfprApFabricChangedObjectRefInstanceId = _CfprApFabricChangedObjectRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1, 1),
    _CfprApFabricChangedObjectRefInstanceId_Type()
)
cfprApFabricChangedObjectRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefInstanceId.setStatus("current")
_CfprApFabricChangedObjectRefDn_Type = CfprApManagedObjectDn
_CfprApFabricChangedObjectRefDn_Object = MibTableColumn
cfprApFabricChangedObjectRefDn = _CfprApFabricChangedObjectRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1, 2),
    _CfprApFabricChangedObjectRefDn_Type()
)
cfprApFabricChangedObjectRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefDn.setStatus("current")
_CfprApFabricChangedObjectRefRn_Type = SnmpAdminString
_CfprApFabricChangedObjectRefRn_Object = MibTableColumn
cfprApFabricChangedObjectRefRn = _CfprApFabricChangedObjectRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1, 3),
    _CfprApFabricChangedObjectRefRn_Type()
)
cfprApFabricChangedObjectRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefRn.setStatus("current")
_CfprApFabricChangedObjectRefCentraleVnetEpDn_Type = SnmpAdminString
_CfprApFabricChangedObjectRefCentraleVnetEpDn_Object = MibTableColumn
cfprApFabricChangedObjectRefCentraleVnetEpDn = _CfprApFabricChangedObjectRefCentraleVnetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1, 4),
    _CfprApFabricChangedObjectRefCentraleVnetEpDn_Type()
)
cfprApFabricChangedObjectRefCentraleVnetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefCentraleVnetEpDn.setStatus("current")
_CfprApFabricChangedObjectRefId_Type = Gauge32
_CfprApFabricChangedObjectRefId_Object = MibTableColumn
cfprApFabricChangedObjectRefId = _CfprApFabricChangedObjectRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1, 5),
    _CfprApFabricChangedObjectRefId_Type()
)
cfprApFabricChangedObjectRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefId.setStatus("current")
_CfprApFabricChangedObjectRefOldCentraleVnetEpDn_Type = SnmpAdminString
_CfprApFabricChangedObjectRefOldCentraleVnetEpDn_Object = MibTableColumn
cfprApFabricChangedObjectRefOldCentraleVnetEpDn = _CfprApFabricChangedObjectRefOldCentraleVnetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1, 6),
    _CfprApFabricChangedObjectRefOldCentraleVnetEpDn_Type()
)
cfprApFabricChangedObjectRefOldCentraleVnetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefOldCentraleVnetEpDn.setStatus("current")
_CfprApFabricChangedObjectRefRefObjStatus_Type = CfprApFabricStatus
_CfprApFabricChangedObjectRefRefObjStatus_Object = MibTableColumn
cfprApFabricChangedObjectRefRefObjStatus = _CfprApFabricChangedObjectRefRefObjStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1, 7),
    _CfprApFabricChangedObjectRefRefObjStatus_Type()
)
cfprApFabricChangedObjectRefRefObjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefRefObjStatus.setStatus("current")
_CfprApFabricChangedObjectRefUcsmVnetEpDn_Type = SnmpAdminString
_CfprApFabricChangedObjectRefUcsmVnetEpDn_Object = MibTableColumn
cfprApFabricChangedObjectRefUcsmVnetEpDn = _CfprApFabricChangedObjectRefUcsmVnetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 6, 1, 8),
    _CfprApFabricChangedObjectRefUcsmVnetEpDn_Type()
)
cfprApFabricChangedObjectRefUcsmVnetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChangedObjectRefUcsmVnetEpDn.setStatus("current")
_CfprApFabricChassisEpTable_Object = MibTable
cfprApFabricChassisEpTable = _CfprApFabricChassisEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7)
)
if mibBuilder.loadTexts:
    cfprApFabricChassisEpTable.setStatus("current")
_CfprApFabricChassisEpEntry_Object = MibTableRow
cfprApFabricChassisEpEntry = _CfprApFabricChassisEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1)
)
cfprApFabricChassisEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricChassisEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricChassisEpEntry.setStatus("current")
_CfprApFabricChassisEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricChassisEpInstanceId_Object = MibTableColumn
cfprApFabricChassisEpInstanceId = _CfprApFabricChassisEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 1),
    _CfprApFabricChassisEpInstanceId_Type()
)
cfprApFabricChassisEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpInstanceId.setStatus("current")
_CfprApFabricChassisEpDn_Type = CfprApManagedObjectDn
_CfprApFabricChassisEpDn_Object = MibTableColumn
cfprApFabricChassisEpDn = _CfprApFabricChassisEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 2),
    _CfprApFabricChassisEpDn_Type()
)
cfprApFabricChassisEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpDn.setStatus("current")
_CfprApFabricChassisEpRn_Type = SnmpAdminString
_CfprApFabricChassisEpRn_Object = MibTableColumn
cfprApFabricChassisEpRn = _CfprApFabricChassisEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 3),
    _CfprApFabricChassisEpRn_Type()
)
cfprApFabricChassisEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpRn.setStatus("current")
_CfprApFabricChassisEpAdminState_Type = CfprApFabricInternalEpAdminState
_CfprApFabricChassisEpAdminState_Object = MibTableColumn
cfprApFabricChassisEpAdminState = _CfprApFabricChassisEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 4),
    _CfprApFabricChassisEpAdminState_Type()
)
cfprApFabricChassisEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpAdminState.setStatus("current")
_CfprApFabricChassisEpAggrPortId_Type = Gauge32
_CfprApFabricChassisEpAggrPortId_Object = MibTableColumn
cfprApFabricChassisEpAggrPortId = _CfprApFabricChassisEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 5),
    _CfprApFabricChassisEpAggrPortId_Type()
)
cfprApFabricChassisEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpAggrPortId.setStatus("current")
_CfprApFabricChassisEpChassisDn_Type = SnmpAdminString
_CfprApFabricChassisEpChassisDn_Object = MibTableColumn
cfprApFabricChassisEpChassisDn = _CfprApFabricChassisEpChassisDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 6),
    _CfprApFabricChassisEpChassisDn_Type()
)
cfprApFabricChassisEpChassisDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpChassisDn.setStatus("current")
_CfprApFabricChassisEpChassisId_Type = Gauge32
_CfprApFabricChassisEpChassisId_Object = MibTableColumn
cfprApFabricChassisEpChassisId = _CfprApFabricChassisEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 7),
    _CfprApFabricChassisEpChassisId_Type()
)
cfprApFabricChassisEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpChassisId.setStatus("current")
_CfprApFabricChassisEpEpDn_Type = SnmpAdminString
_CfprApFabricChassisEpEpDn_Object = MibTableColumn
cfprApFabricChassisEpEpDn = _CfprApFabricChassisEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 8),
    _CfprApFabricChassisEpEpDn_Type()
)
cfprApFabricChassisEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpEpDn.setStatus("current")
_CfprApFabricChassisEpFltAggr_Type = Unsigned64
_CfprApFabricChassisEpFltAggr_Object = MibTableColumn
cfprApFabricChassisEpFltAggr = _CfprApFabricChassisEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 9),
    _CfprApFabricChassisEpFltAggr_Type()
)
cfprApFabricChassisEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpFltAggr.setStatus("current")
_CfprApFabricChassisEpIfRole_Type = CfprApFabricComputeEpIfRole
_CfprApFabricChassisEpIfRole_Object = MibTableColumn
cfprApFabricChassisEpIfRole = _CfprApFabricChassisEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 10),
    _CfprApFabricChassisEpIfRole_Type()
)
cfprApFabricChassisEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpIfRole.setStatus("current")
_CfprApFabricChassisEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricChassisEpIfType_Object = MibTableColumn
cfprApFabricChassisEpIfType = _CfprApFabricChassisEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 11),
    _CfprApFabricChassisEpIfType_Type()
)
cfprApFabricChassisEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpIfType.setStatus("current")
_CfprApFabricChassisEpLicGP_Type = Unsigned64
_CfprApFabricChassisEpLicGP_Object = MibTableColumn
cfprApFabricChassisEpLicGP = _CfprApFabricChassisEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 12),
    _CfprApFabricChassisEpLicGP_Type()
)
cfprApFabricChassisEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpLicGP.setStatus("current")
_CfprApFabricChassisEpLicState_Type = CfprApLicenseState
_CfprApFabricChassisEpLicState_Object = MibTableColumn
cfprApFabricChassisEpLicState = _CfprApFabricChassisEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 13),
    _CfprApFabricChassisEpLicState_Type()
)
cfprApFabricChassisEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpLicState.setStatus("current")
_CfprApFabricChassisEpLocale_Type = CfprApFabricInternalEpLocale
_CfprApFabricChassisEpLocale_Object = MibTableColumn
cfprApFabricChassisEpLocale = _CfprApFabricChassisEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 14),
    _CfprApFabricChassisEpLocale_Type()
)
cfprApFabricChassisEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpLocale.setStatus("current")
_CfprApFabricChassisEpModel_Type = SnmpAdminString
_CfprApFabricChassisEpModel_Object = MibTableColumn
cfprApFabricChassisEpModel = _CfprApFabricChassisEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 15),
    _CfprApFabricChassisEpModel_Type()
)
cfprApFabricChassisEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpModel.setStatus("current")
_CfprApFabricChassisEpName_Type = SnmpAdminString
_CfprApFabricChassisEpName_Object = MibTableColumn
cfprApFabricChassisEpName = _CfprApFabricChassisEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 16),
    _CfprApFabricChassisEpName_Type()
)
cfprApFabricChassisEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpName.setStatus("current")
_CfprApFabricChassisEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricChassisEpOperState_Object = MibTableColumn
cfprApFabricChassisEpOperState = _CfprApFabricChassisEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 17),
    _CfprApFabricChassisEpOperState_Type()
)
cfprApFabricChassisEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpOperState.setStatus("current")
_CfprApFabricChassisEpOperStateReason_Type = SnmpAdminString
_CfprApFabricChassisEpOperStateReason_Object = MibTableColumn
cfprApFabricChassisEpOperStateReason = _CfprApFabricChassisEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 18),
    _CfprApFabricChassisEpOperStateReason_Type()
)
cfprApFabricChassisEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpOperStateReason.setStatus("current")
_CfprApFabricChassisEpPeerAggrPortId_Type = Gauge32
_CfprApFabricChassisEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricChassisEpPeerAggrPortId = _CfprApFabricChassisEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 19),
    _CfprApFabricChassisEpPeerAggrPortId_Type()
)
cfprApFabricChassisEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpPeerAggrPortId.setStatus("current")
_CfprApFabricChassisEpPeerChassisId_Type = Gauge32
_CfprApFabricChassisEpPeerChassisId_Object = MibTableColumn
cfprApFabricChassisEpPeerChassisId = _CfprApFabricChassisEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 20),
    _CfprApFabricChassisEpPeerChassisId_Type()
)
cfprApFabricChassisEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpPeerChassisId.setStatus("current")
_CfprApFabricChassisEpPeerDn_Type = SnmpAdminString
_CfprApFabricChassisEpPeerDn_Object = MibTableColumn
cfprApFabricChassisEpPeerDn = _CfprApFabricChassisEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 21),
    _CfprApFabricChassisEpPeerDn_Type()
)
cfprApFabricChassisEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpPeerDn.setStatus("current")
_CfprApFabricChassisEpPeerPortId_Type = Gauge32
_CfprApFabricChassisEpPeerPortId_Object = MibTableColumn
cfprApFabricChassisEpPeerPortId = _CfprApFabricChassisEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 22),
    _CfprApFabricChassisEpPeerPortId_Type()
)
cfprApFabricChassisEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpPeerPortId.setStatus("current")
_CfprApFabricChassisEpPeerSlotId_Type = Gauge32
_CfprApFabricChassisEpPeerSlotId_Object = MibTableColumn
cfprApFabricChassisEpPeerSlotId = _CfprApFabricChassisEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 23),
    _CfprApFabricChassisEpPeerSlotId_Type()
)
cfprApFabricChassisEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpPeerSlotId.setStatus("current")
_CfprApFabricChassisEpPortId_Type = CfprApFabricPIoEpPortId
_CfprApFabricChassisEpPortId_Object = MibTableColumn
cfprApFabricChassisEpPortId = _CfprApFabricChassisEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 24),
    _CfprApFabricChassisEpPortId_Type()
)
cfprApFabricChassisEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpPortId.setStatus("current")
_CfprApFabricChassisEpRevision_Type = SnmpAdminString
_CfprApFabricChassisEpRevision_Object = MibTableColumn
cfprApFabricChassisEpRevision = _CfprApFabricChassisEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 25),
    _CfprApFabricChassisEpRevision_Type()
)
cfprApFabricChassisEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpRevision.setStatus("current")
_CfprApFabricChassisEpSerial_Type = SnmpAdminString
_CfprApFabricChassisEpSerial_Object = MibTableColumn
cfprApFabricChassisEpSerial = _CfprApFabricChassisEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 26),
    _CfprApFabricChassisEpSerial_Type()
)
cfprApFabricChassisEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpSerial.setStatus("current")
_CfprApFabricChassisEpSlotId_Type = CfprApFabricPIoEpSlotId
_CfprApFabricChassisEpSlotId_Object = MibTableColumn
cfprApFabricChassisEpSlotId = _CfprApFabricChassisEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 27),
    _CfprApFabricChassisEpSlotId_Type()
)
cfprApFabricChassisEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpSlotId.setStatus("current")
_CfprApFabricChassisEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricChassisEpSwitchId_Object = MibTableColumn
cfprApFabricChassisEpSwitchId = _CfprApFabricChassisEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 28),
    _CfprApFabricChassisEpSwitchId_Type()
)
cfprApFabricChassisEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpSwitchId.setStatus("current")
_CfprApFabricChassisEpTransport_Type = CfprApNetworkTransport
_CfprApFabricChassisEpTransport_Object = MibTableColumn
cfprApFabricChassisEpTransport = _CfprApFabricChassisEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 29),
    _CfprApFabricChassisEpTransport_Type()
)
cfprApFabricChassisEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpTransport.setStatus("current")
_CfprApFabricChassisEpType_Type = CfprApFabricComputeEpType
_CfprApFabricChassisEpType_Object = MibTableColumn
cfprApFabricChassisEpType = _CfprApFabricChassisEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 30),
    _CfprApFabricChassisEpType_Type()
)
cfprApFabricChassisEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpType.setStatus("current")
_CfprApFabricChassisEpVendor_Type = SnmpAdminString
_CfprApFabricChassisEpVendor_Object = MibTableColumn
cfprApFabricChassisEpVendor = _CfprApFabricChassisEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 7, 1, 31),
    _CfprApFabricChassisEpVendor_Type()
)
cfprApFabricChassisEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricChassisEpVendor.setStatus("current")
_CfprApFabricComputePhEpTable_Object = MibTable
cfprApFabricComputePhEpTable = _CfprApFabricComputePhEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8)
)
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpTable.setStatus("current")
_CfprApFabricComputePhEpEntry_Object = MibTableRow
cfprApFabricComputePhEpEntry = _CfprApFabricComputePhEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1)
)
cfprApFabricComputePhEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricComputePhEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpEntry.setStatus("current")
_CfprApFabricComputePhEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricComputePhEpInstanceId_Object = MibTableColumn
cfprApFabricComputePhEpInstanceId = _CfprApFabricComputePhEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 1),
    _CfprApFabricComputePhEpInstanceId_Type()
)
cfprApFabricComputePhEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpInstanceId.setStatus("current")
_CfprApFabricComputePhEpDn_Type = CfprApManagedObjectDn
_CfprApFabricComputePhEpDn_Object = MibTableColumn
cfprApFabricComputePhEpDn = _CfprApFabricComputePhEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 2),
    _CfprApFabricComputePhEpDn_Type()
)
cfprApFabricComputePhEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpDn.setStatus("current")
_CfprApFabricComputePhEpRn_Type = SnmpAdminString
_CfprApFabricComputePhEpRn_Object = MibTableColumn
cfprApFabricComputePhEpRn = _CfprApFabricComputePhEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 3),
    _CfprApFabricComputePhEpRn_Type()
)
cfprApFabricComputePhEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpRn.setStatus("current")
_CfprApFabricComputePhEpAdminState_Type = CfprApFabricComputePhEpAdminState
_CfprApFabricComputePhEpAdminState_Object = MibTableColumn
cfprApFabricComputePhEpAdminState = _CfprApFabricComputePhEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 4),
    _CfprApFabricComputePhEpAdminState_Type()
)
cfprApFabricComputePhEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpAdminState.setStatus("current")
_CfprApFabricComputePhEpAggrPortId_Type = Gauge32
_CfprApFabricComputePhEpAggrPortId_Object = MibTableColumn
cfprApFabricComputePhEpAggrPortId = _CfprApFabricComputePhEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 5),
    _CfprApFabricComputePhEpAggrPortId_Type()
)
cfprApFabricComputePhEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpAggrPortId.setStatus("current")
_CfprApFabricComputePhEpBoardAggregationRole_Type = CfprApEquipmentBoardAggregationRole
_CfprApFabricComputePhEpBoardAggregationRole_Object = MibTableColumn
cfprApFabricComputePhEpBoardAggregationRole = _CfprApFabricComputePhEpBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 6),
    _CfprApFabricComputePhEpBoardAggregationRole_Type()
)
cfprApFabricComputePhEpBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpBoardAggregationRole.setStatus("current")
_CfprApFabricComputePhEpChassisId_Type = Gauge32
_CfprApFabricComputePhEpChassisId_Object = MibTableColumn
cfprApFabricComputePhEpChassisId = _CfprApFabricComputePhEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 7),
    _CfprApFabricComputePhEpChassisId_Type()
)
cfprApFabricComputePhEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpChassisId.setStatus("current")
_CfprApFabricComputePhEpCheckpointTrigTs_Type = Unsigned64
_CfprApFabricComputePhEpCheckpointTrigTs_Object = MibTableColumn
cfprApFabricComputePhEpCheckpointTrigTs = _CfprApFabricComputePhEpCheckpointTrigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 8),
    _CfprApFabricComputePhEpCheckpointTrigTs_Type()
)
cfprApFabricComputePhEpCheckpointTrigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpCheckpointTrigTs.setStatus("current")
_CfprApFabricComputePhEpDeepCheckpointTrigTs_Type = Unsigned64
_CfprApFabricComputePhEpDeepCheckpointTrigTs_Object = MibTableColumn
cfprApFabricComputePhEpDeepCheckpointTrigTs = _CfprApFabricComputePhEpDeepCheckpointTrigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 9),
    _CfprApFabricComputePhEpDeepCheckpointTrigTs_Type()
)
cfprApFabricComputePhEpDeepCheckpointTrigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpDeepCheckpointTrigTs.setStatus("current")
_CfprApFabricComputePhEpDiscTrigTs_Type = Unsigned64
_CfprApFabricComputePhEpDiscTrigTs_Object = MibTableColumn
cfprApFabricComputePhEpDiscTrigTs = _CfprApFabricComputePhEpDiscTrigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 10),
    _CfprApFabricComputePhEpDiscTrigTs_Type()
)
cfprApFabricComputePhEpDiscTrigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpDiscTrigTs.setStatus("current")
_CfprApFabricComputePhEpEpDn_Type = SnmpAdminString
_CfprApFabricComputePhEpEpDn_Object = MibTableColumn
cfprApFabricComputePhEpEpDn = _CfprApFabricComputePhEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 11),
    _CfprApFabricComputePhEpEpDn_Type()
)
cfprApFabricComputePhEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpEpDn.setStatus("current")
_CfprApFabricComputePhEpEqType_Type = CfprApEquipmentFabricEpType
_CfprApFabricComputePhEpEqType_Object = MibTableColumn
cfprApFabricComputePhEpEqType = _CfprApFabricComputePhEpEqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 12),
    _CfprApFabricComputePhEpEqType_Type()
)
cfprApFabricComputePhEpEqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpEqType.setStatus("current")
_CfprApFabricComputePhEpFltAggr_Type = Unsigned64
_CfprApFabricComputePhEpFltAggr_Object = MibTableColumn
cfprApFabricComputePhEpFltAggr = _CfprApFabricComputePhEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 13),
    _CfprApFabricComputePhEpFltAggr_Type()
)
cfprApFabricComputePhEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpFltAggr.setStatus("current")
_CfprApFabricComputePhEpIfRole_Type = CfprApFabricComputeEpIfRole
_CfprApFabricComputePhEpIfRole_Object = MibTableColumn
cfprApFabricComputePhEpIfRole = _CfprApFabricComputePhEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 14),
    _CfprApFabricComputePhEpIfRole_Type()
)
cfprApFabricComputePhEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpIfRole.setStatus("current")
_CfprApFabricComputePhEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricComputePhEpIfType_Object = MibTableColumn
cfprApFabricComputePhEpIfType = _CfprApFabricComputePhEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 15),
    _CfprApFabricComputePhEpIfType_Type()
)
cfprApFabricComputePhEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpIfType.setStatus("current")
_CfprApFabricComputePhEpLc_Type = CfprApFabricBladeLifeCycle
_CfprApFabricComputePhEpLc_Object = MibTableColumn
cfprApFabricComputePhEpLc = _CfprApFabricComputePhEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 16),
    _CfprApFabricComputePhEpLc_Type()
)
cfprApFabricComputePhEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpLc.setStatus("current")
_CfprApFabricComputePhEpLicGP_Type = Unsigned64
_CfprApFabricComputePhEpLicGP_Object = MibTableColumn
cfprApFabricComputePhEpLicGP = _CfprApFabricComputePhEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 17),
    _CfprApFabricComputePhEpLicGP_Type()
)
cfprApFabricComputePhEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpLicGP.setStatus("current")
_CfprApFabricComputePhEpLicState_Type = CfprApLicenseState
_CfprApFabricComputePhEpLicState_Object = MibTableColumn
cfprApFabricComputePhEpLicState = _CfprApFabricComputePhEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 18),
    _CfprApFabricComputePhEpLicState_Type()
)
cfprApFabricComputePhEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpLicState.setStatus("current")
_CfprApFabricComputePhEpLocale_Type = CfprApFabricInternalEpLocale
_CfprApFabricComputePhEpLocale_Object = MibTableColumn
cfprApFabricComputePhEpLocale = _CfprApFabricComputePhEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 19),
    _CfprApFabricComputePhEpLocale_Type()
)
cfprApFabricComputePhEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpLocale.setStatus("current")
_CfprApFabricComputePhEpModel_Type = SnmpAdminString
_CfprApFabricComputePhEpModel_Object = MibTableColumn
cfprApFabricComputePhEpModel = _CfprApFabricComputePhEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 20),
    _CfprApFabricComputePhEpModel_Type()
)
cfprApFabricComputePhEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpModel.setStatus("current")
_CfprApFabricComputePhEpName_Type = SnmpAdminString
_CfprApFabricComputePhEpName_Object = MibTableColumn
cfprApFabricComputePhEpName = _CfprApFabricComputePhEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 21),
    _CfprApFabricComputePhEpName_Type()
)
cfprApFabricComputePhEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpName.setStatus("current")
_CfprApFabricComputePhEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricComputePhEpOperState_Object = MibTableColumn
cfprApFabricComputePhEpOperState = _CfprApFabricComputePhEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 22),
    _CfprApFabricComputePhEpOperState_Type()
)
cfprApFabricComputePhEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpOperState.setStatus("current")
_CfprApFabricComputePhEpOperStateReason_Type = SnmpAdminString
_CfprApFabricComputePhEpOperStateReason_Object = MibTableColumn
cfprApFabricComputePhEpOperStateReason = _CfprApFabricComputePhEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 23),
    _CfprApFabricComputePhEpOperStateReason_Type()
)
cfprApFabricComputePhEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpOperStateReason.setStatus("current")
_CfprApFabricComputePhEpPeerAggrPortId_Type = Gauge32
_CfprApFabricComputePhEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricComputePhEpPeerAggrPortId = _CfprApFabricComputePhEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 24),
    _CfprApFabricComputePhEpPeerAggrPortId_Type()
)
cfprApFabricComputePhEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpPeerAggrPortId.setStatus("current")
_CfprApFabricComputePhEpPeerChassisId_Type = Gauge32
_CfprApFabricComputePhEpPeerChassisId_Object = MibTableColumn
cfprApFabricComputePhEpPeerChassisId = _CfprApFabricComputePhEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 25),
    _CfprApFabricComputePhEpPeerChassisId_Type()
)
cfprApFabricComputePhEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpPeerChassisId.setStatus("current")
_CfprApFabricComputePhEpPeerDn_Type = SnmpAdminString
_CfprApFabricComputePhEpPeerDn_Object = MibTableColumn
cfprApFabricComputePhEpPeerDn = _CfprApFabricComputePhEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 26),
    _CfprApFabricComputePhEpPeerDn_Type()
)
cfprApFabricComputePhEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpPeerDn.setStatus("current")
_CfprApFabricComputePhEpPeerPortId_Type = Gauge32
_CfprApFabricComputePhEpPeerPortId_Object = MibTableColumn
cfprApFabricComputePhEpPeerPortId = _CfprApFabricComputePhEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 27),
    _CfprApFabricComputePhEpPeerPortId_Type()
)
cfprApFabricComputePhEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpPeerPortId.setStatus("current")
_CfprApFabricComputePhEpPeerSlotId_Type = Gauge32
_CfprApFabricComputePhEpPeerSlotId_Object = MibTableColumn
cfprApFabricComputePhEpPeerSlotId = _CfprApFabricComputePhEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 28),
    _CfprApFabricComputePhEpPeerSlotId_Type()
)
cfprApFabricComputePhEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpPeerSlotId.setStatus("current")
_CfprApFabricComputePhEpPortId_Type = CfprApFabricPIoEpPortId
_CfprApFabricComputePhEpPortId_Object = MibTableColumn
cfprApFabricComputePhEpPortId = _CfprApFabricComputePhEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 29),
    _CfprApFabricComputePhEpPortId_Type()
)
cfprApFabricComputePhEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpPortId.setStatus("current")
_CfprApFabricComputePhEpProfileDn_Type = SnmpAdminString
_CfprApFabricComputePhEpProfileDn_Object = MibTableColumn
cfprApFabricComputePhEpProfileDn = _CfprApFabricComputePhEpProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 30),
    _CfprApFabricComputePhEpProfileDn_Type()
)
cfprApFabricComputePhEpProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpProfileDn.setStatus("current")
_CfprApFabricComputePhEpRevision_Type = SnmpAdminString
_CfprApFabricComputePhEpRevision_Object = MibTableColumn
cfprApFabricComputePhEpRevision = _CfprApFabricComputePhEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 31),
    _CfprApFabricComputePhEpRevision_Type()
)
cfprApFabricComputePhEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpRevision.setStatus("current")
_CfprApFabricComputePhEpSerial_Type = SnmpAdminString
_CfprApFabricComputePhEpSerial_Object = MibTableColumn
cfprApFabricComputePhEpSerial = _CfprApFabricComputePhEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 32),
    _CfprApFabricComputePhEpSerial_Type()
)
cfprApFabricComputePhEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpSerial.setStatus("current")
_CfprApFabricComputePhEpSlotId_Type = CfprApFabricPIoEpSlotId
_CfprApFabricComputePhEpSlotId_Object = MibTableColumn
cfprApFabricComputePhEpSlotId = _CfprApFabricComputePhEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 33),
    _CfprApFabricComputePhEpSlotId_Type()
)
cfprApFabricComputePhEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpSlotId.setStatus("current")
_CfprApFabricComputePhEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricComputePhEpSwitchId_Object = MibTableColumn
cfprApFabricComputePhEpSwitchId = _CfprApFabricComputePhEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 34),
    _CfprApFabricComputePhEpSwitchId_Type()
)
cfprApFabricComputePhEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpSwitchId.setStatus("current")
_CfprApFabricComputePhEpTransport_Type = CfprApNetworkTransport
_CfprApFabricComputePhEpTransport_Object = MibTableColumn
cfprApFabricComputePhEpTransport = _CfprApFabricComputePhEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 35),
    _CfprApFabricComputePhEpTransport_Type()
)
cfprApFabricComputePhEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpTransport.setStatus("current")
_CfprApFabricComputePhEpType_Type = CfprApFabricComputeEpType
_CfprApFabricComputePhEpType_Object = MibTableColumn
cfprApFabricComputePhEpType = _CfprApFabricComputePhEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 36),
    _CfprApFabricComputePhEpType_Type()
)
cfprApFabricComputePhEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpType.setStatus("current")
_CfprApFabricComputePhEpVendor_Type = SnmpAdminString
_CfprApFabricComputePhEpVendor_Object = MibTableColumn
cfprApFabricComputePhEpVendor = _CfprApFabricComputePhEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 8, 1, 37),
    _CfprApFabricComputePhEpVendor_Type()
)
cfprApFabricComputePhEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputePhEpVendor.setStatus("current")
_CfprApFabricComputeSlotEpTable_Object = MibTable
cfprApFabricComputeSlotEpTable = _CfprApFabricComputeSlotEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9)
)
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpTable.setStatus("current")
_CfprApFabricComputeSlotEpEntry_Object = MibTableRow
cfprApFabricComputeSlotEpEntry = _CfprApFabricComputeSlotEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1)
)
cfprApFabricComputeSlotEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricComputeSlotEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpEntry.setStatus("current")
_CfprApFabricComputeSlotEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricComputeSlotEpInstanceId_Object = MibTableColumn
cfprApFabricComputeSlotEpInstanceId = _CfprApFabricComputeSlotEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 1),
    _CfprApFabricComputeSlotEpInstanceId_Type()
)
cfprApFabricComputeSlotEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpInstanceId.setStatus("current")
_CfprApFabricComputeSlotEpDn_Type = CfprApManagedObjectDn
_CfprApFabricComputeSlotEpDn_Object = MibTableColumn
cfprApFabricComputeSlotEpDn = _CfprApFabricComputeSlotEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 2),
    _CfprApFabricComputeSlotEpDn_Type()
)
cfprApFabricComputeSlotEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpDn.setStatus("current")
_CfprApFabricComputeSlotEpRn_Type = SnmpAdminString
_CfprApFabricComputeSlotEpRn_Object = MibTableColumn
cfprApFabricComputeSlotEpRn = _CfprApFabricComputeSlotEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 3),
    _CfprApFabricComputeSlotEpRn_Type()
)
cfprApFabricComputeSlotEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpRn.setStatus("current")
_CfprApFabricComputeSlotEpAdminState_Type = CfprApFabricSlotAdminState
_CfprApFabricComputeSlotEpAdminState_Object = MibTableColumn
cfprApFabricComputeSlotEpAdminState = _CfprApFabricComputeSlotEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 4),
    _CfprApFabricComputeSlotEpAdminState_Type()
)
cfprApFabricComputeSlotEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpAdminState.setStatus("current")
_CfprApFabricComputeSlotEpAggrPortId_Type = Gauge32
_CfprApFabricComputeSlotEpAggrPortId_Object = MibTableColumn
cfprApFabricComputeSlotEpAggrPortId = _CfprApFabricComputeSlotEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 5),
    _CfprApFabricComputeSlotEpAggrPortId_Type()
)
cfprApFabricComputeSlotEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpAggrPortId.setStatus("current")
_CfprApFabricComputeSlotEpBoardAggregationRole_Type = CfprApEquipmentBoardAggregationRole
_CfprApFabricComputeSlotEpBoardAggregationRole_Object = MibTableColumn
cfprApFabricComputeSlotEpBoardAggregationRole = _CfprApFabricComputeSlotEpBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 6),
    _CfprApFabricComputeSlotEpBoardAggregationRole_Type()
)
cfprApFabricComputeSlotEpBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpBoardAggregationRole.setStatus("current")
_CfprApFabricComputeSlotEpChassisId_Type = Gauge32
_CfprApFabricComputeSlotEpChassisId_Object = MibTableColumn
cfprApFabricComputeSlotEpChassisId = _CfprApFabricComputeSlotEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 7),
    _CfprApFabricComputeSlotEpChassisId_Type()
)
cfprApFabricComputeSlotEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpChassisId.setStatus("current")
_CfprApFabricComputeSlotEpConnPath_Type = CfprApEquipmentConnectionStatus
_CfprApFabricComputeSlotEpConnPath_Object = MibTableColumn
cfprApFabricComputeSlotEpConnPath = _CfprApFabricComputeSlotEpConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 8),
    _CfprApFabricComputeSlotEpConnPath_Type()
)
cfprApFabricComputeSlotEpConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpConnPath.setStatus("current")
_CfprApFabricComputeSlotEpConnStatus_Type = CfprApEquipmentConnectionStatus
_CfprApFabricComputeSlotEpConnStatus_Object = MibTableColumn
cfprApFabricComputeSlotEpConnStatus = _CfprApFabricComputeSlotEpConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 9),
    _CfprApFabricComputeSlotEpConnStatus_Type()
)
cfprApFabricComputeSlotEpConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpConnStatus.setStatus("current")
_CfprApFabricComputeSlotEpDiscovery_Type = CfprApComputeDiscovery
_CfprApFabricComputeSlotEpDiscovery_Object = MibTableColumn
cfprApFabricComputeSlotEpDiscovery = _CfprApFabricComputeSlotEpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 10),
    _CfprApFabricComputeSlotEpDiscovery_Type()
)
cfprApFabricComputeSlotEpDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpDiscovery.setStatus("current")
_CfprApFabricComputeSlotEpEpDn_Type = SnmpAdminString
_CfprApFabricComputeSlotEpEpDn_Object = MibTableColumn
cfprApFabricComputeSlotEpEpDn = _CfprApFabricComputeSlotEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 11),
    _CfprApFabricComputeSlotEpEpDn_Type()
)
cfprApFabricComputeSlotEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpEpDn.setStatus("current")
_CfprApFabricComputeSlotEpFactoryResetFlag_Type = TruthValue
_CfprApFabricComputeSlotEpFactoryResetFlag_Object = MibTableColumn
cfprApFabricComputeSlotEpFactoryResetFlag = _CfprApFabricComputeSlotEpFactoryResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 12),
    _CfprApFabricComputeSlotEpFactoryResetFlag_Type()
)
cfprApFabricComputeSlotEpFactoryResetFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpFactoryResetFlag.setStatus("current")
_CfprApFabricComputeSlotEpFltAggr_Type = Unsigned64
_CfprApFabricComputeSlotEpFltAggr_Object = MibTableColumn
cfprApFabricComputeSlotEpFltAggr = _CfprApFabricComputeSlotEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 13),
    _CfprApFabricComputeSlotEpFltAggr_Type()
)
cfprApFabricComputeSlotEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpFltAggr.setStatus("current")
_CfprApFabricComputeSlotEpFruIdentTrigTs_Type = Unsigned64
_CfprApFabricComputeSlotEpFruIdentTrigTs_Object = MibTableColumn
cfprApFabricComputeSlotEpFruIdentTrigTs = _CfprApFabricComputeSlotEpFruIdentTrigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 14),
    _CfprApFabricComputeSlotEpFruIdentTrigTs_Type()
)
cfprApFabricComputeSlotEpFruIdentTrigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpFruIdentTrigTs.setStatus("current")
_CfprApFabricComputeSlotEpIfRole_Type = CfprApFabricComputeEpIfRole
_CfprApFabricComputeSlotEpIfRole_Object = MibTableColumn
cfprApFabricComputeSlotEpIfRole = _CfprApFabricComputeSlotEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 15),
    _CfprApFabricComputeSlotEpIfRole_Type()
)
cfprApFabricComputeSlotEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpIfRole.setStatus("current")
_CfprApFabricComputeSlotEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricComputeSlotEpIfType_Object = MibTableColumn
cfprApFabricComputeSlotEpIfType = _CfprApFabricComputeSlotEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 16),
    _CfprApFabricComputeSlotEpIfType_Type()
)
cfprApFabricComputeSlotEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpIfType.setStatus("current")
_CfprApFabricComputeSlotEpLcTs_Type = DateAndTime
_CfprApFabricComputeSlotEpLcTs_Object = MibTableColumn
cfprApFabricComputeSlotEpLcTs = _CfprApFabricComputeSlotEpLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 17),
    _CfprApFabricComputeSlotEpLcTs_Type()
)
cfprApFabricComputeSlotEpLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpLcTs.setStatus("current")
_CfprApFabricComputeSlotEpLicGP_Type = Unsigned64
_CfprApFabricComputeSlotEpLicGP_Object = MibTableColumn
cfprApFabricComputeSlotEpLicGP = _CfprApFabricComputeSlotEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 18),
    _CfprApFabricComputeSlotEpLicGP_Type()
)
cfprApFabricComputeSlotEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpLicGP.setStatus("current")
_CfprApFabricComputeSlotEpLicState_Type = CfprApLicenseState
_CfprApFabricComputeSlotEpLicState_Object = MibTableColumn
cfprApFabricComputeSlotEpLicState = _CfprApFabricComputeSlotEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 19),
    _CfprApFabricComputeSlotEpLicState_Type()
)
cfprApFabricComputeSlotEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpLicState.setStatus("current")
_CfprApFabricComputeSlotEpLocale_Type = CfprApFabricInternalEpLocale
_CfprApFabricComputeSlotEpLocale_Object = MibTableColumn
cfprApFabricComputeSlotEpLocale = _CfprApFabricComputeSlotEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 20),
    _CfprApFabricComputeSlotEpLocale_Type()
)
cfprApFabricComputeSlotEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpLocale.setStatus("current")
_CfprApFabricComputeSlotEpManagingInst_Type = CfprApNetworkSwitchId
_CfprApFabricComputeSlotEpManagingInst_Object = MibTableColumn
cfprApFabricComputeSlotEpManagingInst = _CfprApFabricComputeSlotEpManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 21),
    _CfprApFabricComputeSlotEpManagingInst_Type()
)
cfprApFabricComputeSlotEpManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpManagingInst.setStatus("current")
_CfprApFabricComputeSlotEpModel_Type = SnmpAdminString
_CfprApFabricComputeSlotEpModel_Object = MibTableColumn
cfprApFabricComputeSlotEpModel = _CfprApFabricComputeSlotEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 22),
    _CfprApFabricComputeSlotEpModel_Type()
)
cfprApFabricComputeSlotEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpModel.setStatus("current")
_CfprApFabricComputeSlotEpName_Type = SnmpAdminString
_CfprApFabricComputeSlotEpName_Object = MibTableColumn
cfprApFabricComputeSlotEpName = _CfprApFabricComputeSlotEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 23),
    _CfprApFabricComputeSlotEpName_Type()
)
cfprApFabricComputeSlotEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpName.setStatus("current")
_CfprApFabricComputeSlotEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricComputeSlotEpOperState_Object = MibTableColumn
cfprApFabricComputeSlotEpOperState = _CfprApFabricComputeSlotEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 24),
    _CfprApFabricComputeSlotEpOperState_Type()
)
cfprApFabricComputeSlotEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpOperState.setStatus("current")
_CfprApFabricComputeSlotEpOperStateReason_Type = SnmpAdminString
_CfprApFabricComputeSlotEpOperStateReason_Object = MibTableColumn
cfprApFabricComputeSlotEpOperStateReason = _CfprApFabricComputeSlotEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 25),
    _CfprApFabricComputeSlotEpOperStateReason_Type()
)
cfprApFabricComputeSlotEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpOperStateReason.setStatus("current")
_CfprApFabricComputeSlotEpPeerAggrPortId_Type = Gauge32
_CfprApFabricComputeSlotEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricComputeSlotEpPeerAggrPortId = _CfprApFabricComputeSlotEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 26),
    _CfprApFabricComputeSlotEpPeerAggrPortId_Type()
)
cfprApFabricComputeSlotEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPeerAggrPortId.setStatus("current")
_CfprApFabricComputeSlotEpPeerChassisId_Type = Gauge32
_CfprApFabricComputeSlotEpPeerChassisId_Object = MibTableColumn
cfprApFabricComputeSlotEpPeerChassisId = _CfprApFabricComputeSlotEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 27),
    _CfprApFabricComputeSlotEpPeerChassisId_Type()
)
cfprApFabricComputeSlotEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPeerChassisId.setStatus("current")
_CfprApFabricComputeSlotEpPeerDn_Type = SnmpAdminString
_CfprApFabricComputeSlotEpPeerDn_Object = MibTableColumn
cfprApFabricComputeSlotEpPeerDn = _CfprApFabricComputeSlotEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 28),
    _CfprApFabricComputeSlotEpPeerDn_Type()
)
cfprApFabricComputeSlotEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPeerDn.setStatus("current")
_CfprApFabricComputeSlotEpPeerPortId_Type = Gauge32
_CfprApFabricComputeSlotEpPeerPortId_Object = MibTableColumn
cfprApFabricComputeSlotEpPeerPortId = _CfprApFabricComputeSlotEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 29),
    _CfprApFabricComputeSlotEpPeerPortId_Type()
)
cfprApFabricComputeSlotEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPeerPortId.setStatus("current")
_CfprApFabricComputeSlotEpPeerSlotEpDn_Type = SnmpAdminString
_CfprApFabricComputeSlotEpPeerSlotEpDn_Object = MibTableColumn
cfprApFabricComputeSlotEpPeerSlotEpDn = _CfprApFabricComputeSlotEpPeerSlotEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 30),
    _CfprApFabricComputeSlotEpPeerSlotEpDn_Type()
)
cfprApFabricComputeSlotEpPeerSlotEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPeerSlotEpDn.setStatus("current")
_CfprApFabricComputeSlotEpPeerSlotId_Type = Gauge32
_CfprApFabricComputeSlotEpPeerSlotId_Object = MibTableColumn
cfprApFabricComputeSlotEpPeerSlotId = _CfprApFabricComputeSlotEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 31),
    _CfprApFabricComputeSlotEpPeerSlotId_Type()
)
cfprApFabricComputeSlotEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPeerSlotId.setStatus("current")
_CfprApFabricComputeSlotEpPortId_Type = CfprApFabricPIoEpPortId
_CfprApFabricComputeSlotEpPortId_Object = MibTableColumn
cfprApFabricComputeSlotEpPortId = _CfprApFabricComputeSlotEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 32),
    _CfprApFabricComputeSlotEpPortId_Type()
)
cfprApFabricComputeSlotEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPortId.setStatus("current")
_CfprApFabricComputeSlotEpPresence_Type = CfprApEquipmentSlotStatus
_CfprApFabricComputeSlotEpPresence_Object = MibTableColumn
cfprApFabricComputeSlotEpPresence = _CfprApFabricComputeSlotEpPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 33),
    _CfprApFabricComputeSlotEpPresence_Type()
)
cfprApFabricComputeSlotEpPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPresence.setStatus("current")
_CfprApFabricComputeSlotEpPresencePath_Type = CfprApEquipmentConnectionStatus
_CfprApFabricComputeSlotEpPresencePath_Object = MibTableColumn
cfprApFabricComputeSlotEpPresencePath = _CfprApFabricComputeSlotEpPresencePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 34),
    _CfprApFabricComputeSlotEpPresencePath_Type()
)
cfprApFabricComputeSlotEpPresencePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpPresencePath.setStatus("current")
_CfprApFabricComputeSlotEpRevision_Type = SnmpAdminString
_CfprApFabricComputeSlotEpRevision_Object = MibTableColumn
cfprApFabricComputeSlotEpRevision = _CfprApFabricComputeSlotEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 35),
    _CfprApFabricComputeSlotEpRevision_Type()
)
cfprApFabricComputeSlotEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpRevision.setStatus("current")
_CfprApFabricComputeSlotEpSerial_Type = SnmpAdminString
_CfprApFabricComputeSlotEpSerial_Object = MibTableColumn
cfprApFabricComputeSlotEpSerial = _CfprApFabricComputeSlotEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 36),
    _CfprApFabricComputeSlotEpSerial_Type()
)
cfprApFabricComputeSlotEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpSerial.setStatus("current")
_CfprApFabricComputeSlotEpSlotId_Type = CfprApFabricComputeSlotEpSlotId
_CfprApFabricComputeSlotEpSlotId_Object = MibTableColumn
cfprApFabricComputeSlotEpSlotId = _CfprApFabricComputeSlotEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 37),
    _CfprApFabricComputeSlotEpSlotId_Type()
)
cfprApFabricComputeSlotEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpSlotId.setStatus("current")
_CfprApFabricComputeSlotEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricComputeSlotEpSwitchId_Object = MibTableColumn
cfprApFabricComputeSlotEpSwitchId = _CfprApFabricComputeSlotEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 38),
    _CfprApFabricComputeSlotEpSwitchId_Type()
)
cfprApFabricComputeSlotEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpSwitchId.setStatus("current")
_CfprApFabricComputeSlotEpTransport_Type = CfprApNetworkTransport
_CfprApFabricComputeSlotEpTransport_Object = MibTableColumn
cfprApFabricComputeSlotEpTransport = _CfprApFabricComputeSlotEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 39),
    _CfprApFabricComputeSlotEpTransport_Type()
)
cfprApFabricComputeSlotEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpTransport.setStatus("current")
_CfprApFabricComputeSlotEpType_Type = CfprApFabricComputeEpType
_CfprApFabricComputeSlotEpType_Object = MibTableColumn
cfprApFabricComputeSlotEpType = _CfprApFabricComputeSlotEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 40),
    _CfprApFabricComputeSlotEpType_Type()
)
cfprApFabricComputeSlotEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpType.setStatus("current")
_CfprApFabricComputeSlotEpVendor_Type = SnmpAdminString
_CfprApFabricComputeSlotEpVendor_Object = MibTableColumn
cfprApFabricComputeSlotEpVendor = _CfprApFabricComputeSlotEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 9, 1, 41),
    _CfprApFabricComputeSlotEpVendor_Type()
)
cfprApFabricComputeSlotEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricComputeSlotEpVendor.setStatus("current")
_CfprApFabricDceSrvTable_Object = MibTable
cfprApFabricDceSrvTable = _CfprApFabricDceSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10)
)
if mibBuilder.loadTexts:
    cfprApFabricDceSrvTable.setStatus("current")
_CfprApFabricDceSrvEntry_Object = MibTableRow
cfprApFabricDceSrvEntry = _CfprApFabricDceSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1)
)
cfprApFabricDceSrvEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricDceSrvInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricDceSrvEntry.setStatus("current")
_CfprApFabricDceSrvInstanceId_Type = CfprApManagedObjectId
_CfprApFabricDceSrvInstanceId_Object = MibTableColumn
cfprApFabricDceSrvInstanceId = _CfprApFabricDceSrvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1, 1),
    _CfprApFabricDceSrvInstanceId_Type()
)
cfprApFabricDceSrvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricDceSrvInstanceId.setStatus("current")
_CfprApFabricDceSrvDn_Type = CfprApManagedObjectDn
_CfprApFabricDceSrvDn_Object = MibTableColumn
cfprApFabricDceSrvDn = _CfprApFabricDceSrvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1, 2),
    _CfprApFabricDceSrvDn_Type()
)
cfprApFabricDceSrvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSrvDn.setStatus("current")
_CfprApFabricDceSrvRn_Type = SnmpAdminString
_CfprApFabricDceSrvRn_Object = MibTableColumn
cfprApFabricDceSrvRn = _CfprApFabricDceSrvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1, 3),
    _CfprApFabricDceSrvRn_Type()
)
cfprApFabricDceSrvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSrvRn.setStatus("current")
_CfprApFabricDceSrvId_Type = CfprApNetworkSwitchId
_CfprApFabricDceSrvId_Object = MibTableColumn
cfprApFabricDceSrvId = _CfprApFabricDceSrvId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1, 4),
    _CfprApFabricDceSrvId_Type()
)
cfprApFabricDceSrvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSrvId.setStatus("current")
_CfprApFabricDceSrvLocale_Type = CfprApFabricInternalLocale
_CfprApFabricDceSrvLocale_Object = MibTableColumn
cfprApFabricDceSrvLocale = _CfprApFabricDceSrvLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1, 5),
    _CfprApFabricDceSrvLocale_Type()
)
cfprApFabricDceSrvLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSrvLocale.setStatus("current")
_CfprApFabricDceSrvName_Type = SnmpAdminString
_CfprApFabricDceSrvName_Object = MibTableColumn
cfprApFabricDceSrvName = _CfprApFabricDceSrvName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1, 6),
    _CfprApFabricDceSrvName_Type()
)
cfprApFabricDceSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSrvName.setStatus("current")
_CfprApFabricDceSrvTransport_Type = CfprApFabricInternalDceSrvTransport
_CfprApFabricDceSrvTransport_Object = MibTableColumn
cfprApFabricDceSrvTransport = _CfprApFabricDceSrvTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1, 7),
    _CfprApFabricDceSrvTransport_Type()
)
cfprApFabricDceSrvTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSrvTransport.setStatus("current")
_CfprApFabricDceSrvType_Type = CfprApFabricInternalDceSrvType
_CfprApFabricDceSrvType_Object = MibTableColumn
cfprApFabricDceSrvType = _CfprApFabricDceSrvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 10, 1, 8),
    _CfprApFabricDceSrvType_Type()
)
cfprApFabricDceSrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSrvType.setStatus("current")
_CfprApFabricDceSwSrvTable_Object = MibTable
cfprApFabricDceSwSrvTable = _CfprApFabricDceSwSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11)
)
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvTable.setStatus("current")
_CfprApFabricDceSwSrvEntry_Object = MibTableRow
cfprApFabricDceSwSrvEntry = _CfprApFabricDceSwSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1)
)
cfprApFabricDceSwSrvEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricDceSwSrvInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEntry.setStatus("current")
_CfprApFabricDceSwSrvInstanceId_Type = CfprApManagedObjectId
_CfprApFabricDceSwSrvInstanceId_Object = MibTableColumn
cfprApFabricDceSwSrvInstanceId = _CfprApFabricDceSwSrvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1, 1),
    _CfprApFabricDceSwSrvInstanceId_Type()
)
cfprApFabricDceSwSrvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvInstanceId.setStatus("current")
_CfprApFabricDceSwSrvDn_Type = CfprApManagedObjectDn
_CfprApFabricDceSwSrvDn_Object = MibTableColumn
cfprApFabricDceSwSrvDn = _CfprApFabricDceSwSrvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1, 2),
    _CfprApFabricDceSwSrvDn_Type()
)
cfprApFabricDceSwSrvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvDn.setStatus("current")
_CfprApFabricDceSwSrvRn_Type = SnmpAdminString
_CfprApFabricDceSwSrvRn_Object = MibTableColumn
cfprApFabricDceSwSrvRn = _CfprApFabricDceSwSrvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1, 3),
    _CfprApFabricDceSwSrvRn_Type()
)
cfprApFabricDceSwSrvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvRn.setStatus("current")
_CfprApFabricDceSwSrvId_Type = CfprApNetworkSwitchId
_CfprApFabricDceSwSrvId_Object = MibTableColumn
cfprApFabricDceSwSrvId = _CfprApFabricDceSwSrvId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1, 4),
    _CfprApFabricDceSwSrvId_Type()
)
cfprApFabricDceSwSrvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvId.setStatus("current")
_CfprApFabricDceSwSrvLocale_Type = CfprApFabricInternalLocale
_CfprApFabricDceSwSrvLocale_Object = MibTableColumn
cfprApFabricDceSwSrvLocale = _CfprApFabricDceSwSrvLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1, 5),
    _CfprApFabricDceSwSrvLocale_Type()
)
cfprApFabricDceSwSrvLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvLocale.setStatus("current")
_CfprApFabricDceSwSrvName_Type = SnmpAdminString
_CfprApFabricDceSwSrvName_Object = MibTableColumn
cfprApFabricDceSwSrvName = _CfprApFabricDceSwSrvName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1, 6),
    _CfprApFabricDceSwSrvName_Type()
)
cfprApFabricDceSwSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvName.setStatus("current")
_CfprApFabricDceSwSrvTransport_Type = CfprApFabricInternalDceSrvTransport
_CfprApFabricDceSwSrvTransport_Object = MibTableColumn
cfprApFabricDceSwSrvTransport = _CfprApFabricDceSwSrvTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1, 7),
    _CfprApFabricDceSwSrvTransport_Type()
)
cfprApFabricDceSwSrvTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvTransport.setStatus("current")
_CfprApFabricDceSwSrvType_Type = CfprApFabricInternalDceSrvType
_CfprApFabricDceSwSrvType_Object = MibTableColumn
cfprApFabricDceSwSrvType = _CfprApFabricDceSwSrvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 11, 1, 8),
    _CfprApFabricDceSwSrvType_Type()
)
cfprApFabricDceSwSrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvType.setStatus("current")
_CfprApFabricDceSwSrvEpTable_Object = MibTable
cfprApFabricDceSwSrvEpTable = _CfprApFabricDceSwSrvEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12)
)
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpTable.setStatus("current")
_CfprApFabricDceSwSrvEpEntry_Object = MibTableRow
cfprApFabricDceSwSrvEpEntry = _CfprApFabricDceSwSrvEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1)
)
cfprApFabricDceSwSrvEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricDceSwSrvEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpEntry.setStatus("current")
_CfprApFabricDceSwSrvEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricDceSwSrvEpInstanceId_Object = MibTableColumn
cfprApFabricDceSwSrvEpInstanceId = _CfprApFabricDceSwSrvEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 1),
    _CfprApFabricDceSwSrvEpInstanceId_Type()
)
cfprApFabricDceSwSrvEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpInstanceId.setStatus("current")
_CfprApFabricDceSwSrvEpDn_Type = CfprApManagedObjectDn
_CfprApFabricDceSwSrvEpDn_Object = MibTableColumn
cfprApFabricDceSwSrvEpDn = _CfprApFabricDceSwSrvEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 2),
    _CfprApFabricDceSwSrvEpDn_Type()
)
cfprApFabricDceSwSrvEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpDn.setStatus("current")
_CfprApFabricDceSwSrvEpRn_Type = SnmpAdminString
_CfprApFabricDceSwSrvEpRn_Object = MibTableColumn
cfprApFabricDceSwSrvEpRn = _CfprApFabricDceSwSrvEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 3),
    _CfprApFabricDceSwSrvEpRn_Type()
)
cfprApFabricDceSwSrvEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpRn.setStatus("current")
_CfprApFabricDceSwSrvEpAdminState_Type = CfprApFabricInternalEpAdminState
_CfprApFabricDceSwSrvEpAdminState_Object = MibTableColumn
cfprApFabricDceSwSrvEpAdminState = _CfprApFabricDceSwSrvEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 4),
    _CfprApFabricDceSwSrvEpAdminState_Type()
)
cfprApFabricDceSwSrvEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpAdminState.setStatus("current")
_CfprApFabricDceSwSrvEpAggrPortId_Type = Gauge32
_CfprApFabricDceSwSrvEpAggrPortId_Object = MibTableColumn
cfprApFabricDceSwSrvEpAggrPortId = _CfprApFabricDceSwSrvEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 5),
    _CfprApFabricDceSwSrvEpAggrPortId_Type()
)
cfprApFabricDceSwSrvEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpAggrPortId.setStatus("current")
_CfprApFabricDceSwSrvEpChassisId_Type = Gauge32
_CfprApFabricDceSwSrvEpChassisId_Object = MibTableColumn
cfprApFabricDceSwSrvEpChassisId = _CfprApFabricDceSwSrvEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 6),
    _CfprApFabricDceSwSrvEpChassisId_Type()
)
cfprApFabricDceSwSrvEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpChassisId.setStatus("current")
_CfprApFabricDceSwSrvEpEpDn_Type = SnmpAdminString
_CfprApFabricDceSwSrvEpEpDn_Object = MibTableColumn
cfprApFabricDceSwSrvEpEpDn = _CfprApFabricDceSwSrvEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 7),
    _CfprApFabricDceSwSrvEpEpDn_Type()
)
cfprApFabricDceSwSrvEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpEpDn.setStatus("current")
_CfprApFabricDceSwSrvEpFltAggr_Type = Unsigned64
_CfprApFabricDceSwSrvEpFltAggr_Object = MibTableColumn
cfprApFabricDceSwSrvEpFltAggr = _CfprApFabricDceSwSrvEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 8),
    _CfprApFabricDceSwSrvEpFltAggr_Type()
)
cfprApFabricDceSwSrvEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpFltAggr.setStatus("current")
_CfprApFabricDceSwSrvEpIfRole_Type = CfprApFabricSwSrvEpIfRole
_CfprApFabricDceSwSrvEpIfRole_Object = MibTableColumn
cfprApFabricDceSwSrvEpIfRole = _CfprApFabricDceSwSrvEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 9),
    _CfprApFabricDceSwSrvEpIfRole_Type()
)
cfprApFabricDceSwSrvEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpIfRole.setStatus("current")
_CfprApFabricDceSwSrvEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricDceSwSrvEpIfType_Object = MibTableColumn
cfprApFabricDceSwSrvEpIfType = _CfprApFabricDceSwSrvEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 10),
    _CfprApFabricDceSwSrvEpIfType_Type()
)
cfprApFabricDceSwSrvEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpIfType.setStatus("current")
_CfprApFabricDceSwSrvEpLicGP_Type = Unsigned64
_CfprApFabricDceSwSrvEpLicGP_Object = MibTableColumn
cfprApFabricDceSwSrvEpLicGP = _CfprApFabricDceSwSrvEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 11),
    _CfprApFabricDceSwSrvEpLicGP_Type()
)
cfprApFabricDceSwSrvEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpLicGP.setStatus("current")
_CfprApFabricDceSwSrvEpLicState_Type = CfprApLicenseState
_CfprApFabricDceSwSrvEpLicState_Object = MibTableColumn
cfprApFabricDceSwSrvEpLicState = _CfprApFabricDceSwSrvEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 12),
    _CfprApFabricDceSwSrvEpLicState_Type()
)
cfprApFabricDceSwSrvEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpLicState.setStatus("current")
_CfprApFabricDceSwSrvEpLocale_Type = CfprApFabricInternalEpLocale
_CfprApFabricDceSwSrvEpLocale_Object = MibTableColumn
cfprApFabricDceSwSrvEpLocale = _CfprApFabricDceSwSrvEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 13),
    _CfprApFabricDceSwSrvEpLocale_Type()
)
cfprApFabricDceSwSrvEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpLocale.setStatus("current")
_CfprApFabricDceSwSrvEpName_Type = SnmpAdminString
_CfprApFabricDceSwSrvEpName_Object = MibTableColumn
cfprApFabricDceSwSrvEpName = _CfprApFabricDceSwSrvEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 14),
    _CfprApFabricDceSwSrvEpName_Type()
)
cfprApFabricDceSwSrvEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpName.setStatus("current")
_CfprApFabricDceSwSrvEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricDceSwSrvEpOperState_Object = MibTableColumn
cfprApFabricDceSwSrvEpOperState = _CfprApFabricDceSwSrvEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 15),
    _CfprApFabricDceSwSrvEpOperState_Type()
)
cfprApFabricDceSwSrvEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpOperState.setStatus("current")
_CfprApFabricDceSwSrvEpOperStateReason_Type = SnmpAdminString
_CfprApFabricDceSwSrvEpOperStateReason_Object = MibTableColumn
cfprApFabricDceSwSrvEpOperStateReason = _CfprApFabricDceSwSrvEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 16),
    _CfprApFabricDceSwSrvEpOperStateReason_Type()
)
cfprApFabricDceSwSrvEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpOperStateReason.setStatus("current")
_CfprApFabricDceSwSrvEpPeerAggrPortId_Type = Gauge32
_CfprApFabricDceSwSrvEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricDceSwSrvEpPeerAggrPortId = _CfprApFabricDceSwSrvEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 17),
    _CfprApFabricDceSwSrvEpPeerAggrPortId_Type()
)
cfprApFabricDceSwSrvEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpPeerAggrPortId.setStatus("current")
_CfprApFabricDceSwSrvEpPeerChassisId_Type = Gauge32
_CfprApFabricDceSwSrvEpPeerChassisId_Object = MibTableColumn
cfprApFabricDceSwSrvEpPeerChassisId = _CfprApFabricDceSwSrvEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 18),
    _CfprApFabricDceSwSrvEpPeerChassisId_Type()
)
cfprApFabricDceSwSrvEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpPeerChassisId.setStatus("current")
_CfprApFabricDceSwSrvEpPeerDn_Type = SnmpAdminString
_CfprApFabricDceSwSrvEpPeerDn_Object = MibTableColumn
cfprApFabricDceSwSrvEpPeerDn = _CfprApFabricDceSwSrvEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 19),
    _CfprApFabricDceSwSrvEpPeerDn_Type()
)
cfprApFabricDceSwSrvEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpPeerDn.setStatus("current")
_CfprApFabricDceSwSrvEpPeerPortId_Type = Gauge32
_CfprApFabricDceSwSrvEpPeerPortId_Object = MibTableColumn
cfprApFabricDceSwSrvEpPeerPortId = _CfprApFabricDceSwSrvEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 20),
    _CfprApFabricDceSwSrvEpPeerPortId_Type()
)
cfprApFabricDceSwSrvEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpPeerPortId.setStatus("current")
_CfprApFabricDceSwSrvEpPeerSlotId_Type = Gauge32
_CfprApFabricDceSwSrvEpPeerSlotId_Object = MibTableColumn
cfprApFabricDceSwSrvEpPeerSlotId = _CfprApFabricDceSwSrvEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 21),
    _CfprApFabricDceSwSrvEpPeerSlotId_Type()
)
cfprApFabricDceSwSrvEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpPeerSlotId.setStatus("current")
_CfprApFabricDceSwSrvEpPortId_Type = CfprApFabricDceSwSrvEpPortId
_CfprApFabricDceSwSrvEpPortId_Object = MibTableColumn
cfprApFabricDceSwSrvEpPortId = _CfprApFabricDceSwSrvEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 22),
    _CfprApFabricDceSwSrvEpPortId_Type()
)
cfprApFabricDceSwSrvEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpPortId.setStatus("current")
_CfprApFabricDceSwSrvEpSlotId_Type = CfprApFabricDceSwSrvEpSlotId
_CfprApFabricDceSwSrvEpSlotId_Object = MibTableColumn
cfprApFabricDceSwSrvEpSlotId = _CfprApFabricDceSwSrvEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 23),
    _CfprApFabricDceSwSrvEpSlotId_Type()
)
cfprApFabricDceSwSrvEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpSlotId.setStatus("current")
_CfprApFabricDceSwSrvEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricDceSwSrvEpSwitchId_Object = MibTableColumn
cfprApFabricDceSwSrvEpSwitchId = _CfprApFabricDceSwSrvEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 24),
    _CfprApFabricDceSwSrvEpSwitchId_Type()
)
cfprApFabricDceSwSrvEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpSwitchId.setStatus("current")
_CfprApFabricDceSwSrvEpTransport_Type = CfprApFabricADceSwSrvEpTransport
_CfprApFabricDceSwSrvEpTransport_Object = MibTableColumn
cfprApFabricDceSwSrvEpTransport = _CfprApFabricDceSwSrvEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 25),
    _CfprApFabricDceSwSrvEpTransport_Type()
)
cfprApFabricDceSwSrvEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpTransport.setStatus("current")
_CfprApFabricDceSwSrvEpType_Type = CfprApFabricSwSrvEpType
_CfprApFabricDceSwSrvEpType_Object = MibTableColumn
cfprApFabricDceSwSrvEpType = _CfprApFabricDceSwSrvEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 26),
    _CfprApFabricDceSwSrvEpType_Type()
)
cfprApFabricDceSwSrvEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpType.setStatus("current")
_CfprApFabricDceSwSrvEpUsrLbl_Type = SnmpAdminString
_CfprApFabricDceSwSrvEpUsrLbl_Object = MibTableColumn
cfprApFabricDceSwSrvEpUsrLbl = _CfprApFabricDceSwSrvEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 12, 1, 27),
    _CfprApFabricDceSwSrvEpUsrLbl_Type()
)
cfprApFabricDceSwSrvEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvEpUsrLbl.setStatus("current")
_CfprApFabricDceSwSrvPcTable_Object = MibTable
cfprApFabricDceSwSrvPcTable = _CfprApFabricDceSwSrvPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13)
)
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcTable.setStatus("current")
_CfprApFabricDceSwSrvPcEntry_Object = MibTableRow
cfprApFabricDceSwSrvPcEntry = _CfprApFabricDceSwSrvPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1)
)
cfprApFabricDceSwSrvPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricDceSwSrvPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEntry.setStatus("current")
_CfprApFabricDceSwSrvPcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricDceSwSrvPcInstanceId_Object = MibTableColumn
cfprApFabricDceSwSrvPcInstanceId = _CfprApFabricDceSwSrvPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 1),
    _CfprApFabricDceSwSrvPcInstanceId_Type()
)
cfprApFabricDceSwSrvPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcInstanceId.setStatus("current")
_CfprApFabricDceSwSrvPcDn_Type = CfprApManagedObjectDn
_CfprApFabricDceSwSrvPcDn_Object = MibTableColumn
cfprApFabricDceSwSrvPcDn = _CfprApFabricDceSwSrvPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 2),
    _CfprApFabricDceSwSrvPcDn_Type()
)
cfprApFabricDceSwSrvPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcDn.setStatus("current")
_CfprApFabricDceSwSrvPcRn_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcRn_Object = MibTableColumn
cfprApFabricDceSwSrvPcRn = _CfprApFabricDceSwSrvPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 3),
    _CfprApFabricDceSwSrvPcRn_Type()
)
cfprApFabricDceSwSrvPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcRn.setStatus("current")
_CfprApFabricDceSwSrvPcAdminState_Type = CfprApFabricDceSwSrvPcAdminState
_CfprApFabricDceSwSrvPcAdminState_Object = MibTableColumn
cfprApFabricDceSwSrvPcAdminState = _CfprApFabricDceSwSrvPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 4),
    _CfprApFabricDceSwSrvPcAdminState_Type()
)
cfprApFabricDceSwSrvPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcAdminState.setStatus("current")
_CfprApFabricDceSwSrvPcChassisId_Type = Gauge32
_CfprApFabricDceSwSrvPcChassisId_Object = MibTableColumn
cfprApFabricDceSwSrvPcChassisId = _CfprApFabricDceSwSrvPcChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 5),
    _CfprApFabricDceSwSrvPcChassisId_Type()
)
cfprApFabricDceSwSrvPcChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcChassisId.setStatus("current")
_CfprApFabricDceSwSrvPcDescr_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcDescr_Object = MibTableColumn
cfprApFabricDceSwSrvPcDescr = _CfprApFabricDceSwSrvPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 6),
    _CfprApFabricDceSwSrvPcDescr_Type()
)
cfprApFabricDceSwSrvPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcDescr.setStatus("current")
_CfprApFabricDceSwSrvPcEpDn_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcEpDn_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpDn = _CfprApFabricDceSwSrvPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 7),
    _CfprApFabricDceSwSrvPcEpDn_Type()
)
cfprApFabricDceSwSrvPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpDn.setStatus("current")
_CfprApFabricDceSwSrvPcFltAggr_Type = Unsigned64
_CfprApFabricDceSwSrvPcFltAggr_Object = MibTableColumn
cfprApFabricDceSwSrvPcFltAggr = _CfprApFabricDceSwSrvPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 8),
    _CfprApFabricDceSwSrvPcFltAggr_Type()
)
cfprApFabricDceSwSrvPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcFltAggr.setStatus("current")
_CfprApFabricDceSwSrvPcIfRole_Type = CfprApFabricSwSrvPcIfRole
_CfprApFabricDceSwSrvPcIfRole_Object = MibTableColumn
cfprApFabricDceSwSrvPcIfRole = _CfprApFabricDceSwSrvPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 9),
    _CfprApFabricDceSwSrvPcIfRole_Type()
)
cfprApFabricDceSwSrvPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcIfRole.setStatus("current")
_CfprApFabricDceSwSrvPcIfType_Type = CfprApFabricCIoEpIfType
_CfprApFabricDceSwSrvPcIfType_Object = MibTableColumn
cfprApFabricDceSwSrvPcIfType = _CfprApFabricDceSwSrvPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 10),
    _CfprApFabricDceSwSrvPcIfType_Type()
)
cfprApFabricDceSwSrvPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcIfType.setStatus("current")
_CfprApFabricDceSwSrvPcLocale_Type = CfprApFabricInternalPcLocale
_CfprApFabricDceSwSrvPcLocale_Object = MibTableColumn
cfprApFabricDceSwSrvPcLocale = _CfprApFabricDceSwSrvPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 11),
    _CfprApFabricDceSwSrvPcLocale_Type()
)
cfprApFabricDceSwSrvPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcLocale.setStatus("current")
_CfprApFabricDceSwSrvPcName_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcName_Object = MibTableColumn
cfprApFabricDceSwSrvPcName = _CfprApFabricDceSwSrvPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 12),
    _CfprApFabricDceSwSrvPcName_Type()
)
cfprApFabricDceSwSrvPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcName.setStatus("current")
_CfprApFabricDceSwSrvPcOperSpeed_Type = CfprApPortEthSpeed
_CfprApFabricDceSwSrvPcOperSpeed_Object = MibTableColumn
cfprApFabricDceSwSrvPcOperSpeed = _CfprApFabricDceSwSrvPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 13),
    _CfprApFabricDceSwSrvPcOperSpeed_Type()
)
cfprApFabricDceSwSrvPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcOperSpeed.setStatus("current")
_CfprApFabricDceSwSrvPcOperState_Type = CfprApNetworkPortOperState
_CfprApFabricDceSwSrvPcOperState_Object = MibTableColumn
cfprApFabricDceSwSrvPcOperState = _CfprApFabricDceSwSrvPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 14),
    _CfprApFabricDceSwSrvPcOperState_Type()
)
cfprApFabricDceSwSrvPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcOperState.setStatus("current")
_CfprApFabricDceSwSrvPcPeerDn_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcPeerDn_Object = MibTableColumn
cfprApFabricDceSwSrvPcPeerDn = _CfprApFabricDceSwSrvPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 15),
    _CfprApFabricDceSwSrvPcPeerDn_Type()
)
cfprApFabricDceSwSrvPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcPeerDn.setStatus("current")
_CfprApFabricDceSwSrvPcPortId_Type = CfprApFabricDceSwSrvPcPortId
_CfprApFabricDceSwSrvPcPortId_Object = MibTableColumn
cfprApFabricDceSwSrvPcPortId = _CfprApFabricDceSwSrvPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 16),
    _CfprApFabricDceSwSrvPcPortId_Type()
)
cfprApFabricDceSwSrvPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcPortId.setStatus("current")
_CfprApFabricDceSwSrvPcStateQual_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcStateQual_Object = MibTableColumn
cfprApFabricDceSwSrvPcStateQual = _CfprApFabricDceSwSrvPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 17),
    _CfprApFabricDceSwSrvPcStateQual_Type()
)
cfprApFabricDceSwSrvPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcStateQual.setStatus("current")
_CfprApFabricDceSwSrvPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricDceSwSrvPcSwitchId_Object = MibTableColumn
cfprApFabricDceSwSrvPcSwitchId = _CfprApFabricDceSwSrvPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 18),
    _CfprApFabricDceSwSrvPcSwitchId_Type()
)
cfprApFabricDceSwSrvPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcSwitchId.setStatus("current")
_CfprApFabricDceSwSrvPcTransport_Type = CfprApFabricDceSwSrvPcTransport
_CfprApFabricDceSwSrvPcTransport_Object = MibTableColumn
cfprApFabricDceSwSrvPcTransport = _CfprApFabricDceSwSrvPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 19),
    _CfprApFabricDceSwSrvPcTransport_Type()
)
cfprApFabricDceSwSrvPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcTransport.setStatus("current")
_CfprApFabricDceSwSrvPcType_Type = CfprApFabricSwSrvPcType
_CfprApFabricDceSwSrvPcType_Object = MibTableColumn
cfprApFabricDceSwSrvPcType = _CfprApFabricDceSwSrvPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 13, 1, 20),
    _CfprApFabricDceSwSrvPcType_Type()
)
cfprApFabricDceSwSrvPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcType.setStatus("current")
_CfprApFabricDceSwSrvPcEpTable_Object = MibTable
cfprApFabricDceSwSrvPcEpTable = _CfprApFabricDceSwSrvPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14)
)
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpTable.setStatus("current")
_CfprApFabricDceSwSrvPcEpEntry_Object = MibTableRow
cfprApFabricDceSwSrvPcEpEntry = _CfprApFabricDceSwSrvPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1)
)
cfprApFabricDceSwSrvPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricDceSwSrvPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpEntry.setStatus("current")
_CfprApFabricDceSwSrvPcEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricDceSwSrvPcEpInstanceId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpInstanceId = _CfprApFabricDceSwSrvPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 1),
    _CfprApFabricDceSwSrvPcEpInstanceId_Type()
)
cfprApFabricDceSwSrvPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpInstanceId.setStatus("current")
_CfprApFabricDceSwSrvPcEpDnData_Type = CfprApManagedObjectDn
_CfprApFabricDceSwSrvPcEpDnData_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpDnData = _CfprApFabricDceSwSrvPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 2),
    _CfprApFabricDceSwSrvPcEpDnData_Type()
)
cfprApFabricDceSwSrvPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpDnData.setStatus("current")
_CfprApFabricDceSwSrvPcEpRn_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcEpRn_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpRn = _CfprApFabricDceSwSrvPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 3),
    _CfprApFabricDceSwSrvPcEpRn_Type()
)
cfprApFabricDceSwSrvPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpRn.setStatus("current")
_CfprApFabricDceSwSrvPcEpAdminState_Type = CfprApFabricInternalEpAdminState
_CfprApFabricDceSwSrvPcEpAdminState_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpAdminState = _CfprApFabricDceSwSrvPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 4),
    _CfprApFabricDceSwSrvPcEpAdminState_Type()
)
cfprApFabricDceSwSrvPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpAdminState.setStatus("current")
_CfprApFabricDceSwSrvPcEpAggrPortId_Type = Gauge32
_CfprApFabricDceSwSrvPcEpAggrPortId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpAggrPortId = _CfprApFabricDceSwSrvPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 5),
    _CfprApFabricDceSwSrvPcEpAggrPortId_Type()
)
cfprApFabricDceSwSrvPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpAggrPortId.setStatus("current")
_CfprApFabricDceSwSrvPcEpChassisId_Type = Gauge32
_CfprApFabricDceSwSrvPcEpChassisId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpChassisId = _CfprApFabricDceSwSrvPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 6),
    _CfprApFabricDceSwSrvPcEpChassisId_Type()
)
cfprApFabricDceSwSrvPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpChassisId.setStatus("current")
_CfprApFabricDceSwSrvPcEpEpDn_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcEpEpDn_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpEpDn = _CfprApFabricDceSwSrvPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 7),
    _CfprApFabricDceSwSrvPcEpEpDn_Type()
)
cfprApFabricDceSwSrvPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpEpDn.setStatus("current")
_CfprApFabricDceSwSrvPcEpFltAggr_Type = Unsigned64
_CfprApFabricDceSwSrvPcEpFltAggr_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpFltAggr = _CfprApFabricDceSwSrvPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 8),
    _CfprApFabricDceSwSrvPcEpFltAggr_Type()
)
cfprApFabricDceSwSrvPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpFltAggr.setStatus("current")
_CfprApFabricDceSwSrvPcEpIfRole_Type = CfprApFabricSwSrvEpIfRole
_CfprApFabricDceSwSrvPcEpIfRole_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpIfRole = _CfprApFabricDceSwSrvPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 9),
    _CfprApFabricDceSwSrvPcEpIfRole_Type()
)
cfprApFabricDceSwSrvPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpIfRole.setStatus("current")
_CfprApFabricDceSwSrvPcEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricDceSwSrvPcEpIfType_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpIfType = _CfprApFabricDceSwSrvPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 10),
    _CfprApFabricDceSwSrvPcEpIfType_Type()
)
cfprApFabricDceSwSrvPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpIfType.setStatus("current")
_CfprApFabricDceSwSrvPcEpLicGP_Type = Unsigned64
_CfprApFabricDceSwSrvPcEpLicGP_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpLicGP = _CfprApFabricDceSwSrvPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 11),
    _CfprApFabricDceSwSrvPcEpLicGP_Type()
)
cfprApFabricDceSwSrvPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpLicGP.setStatus("current")
_CfprApFabricDceSwSrvPcEpLicState_Type = CfprApLicenseState
_CfprApFabricDceSwSrvPcEpLicState_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpLicState = _CfprApFabricDceSwSrvPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 12),
    _CfprApFabricDceSwSrvPcEpLicState_Type()
)
cfprApFabricDceSwSrvPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpLicState.setStatus("current")
_CfprApFabricDceSwSrvPcEpLocale_Type = CfprApFabricInternalEpLocale
_CfprApFabricDceSwSrvPcEpLocale_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpLocale = _CfprApFabricDceSwSrvPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 13),
    _CfprApFabricDceSwSrvPcEpLocale_Type()
)
cfprApFabricDceSwSrvPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpLocale.setStatus("current")
_CfprApFabricDceSwSrvPcEpMembership_Type = CfprApFabricMembershipStatus
_CfprApFabricDceSwSrvPcEpMembership_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpMembership = _CfprApFabricDceSwSrvPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 14),
    _CfprApFabricDceSwSrvPcEpMembership_Type()
)
cfprApFabricDceSwSrvPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpMembership.setStatus("current")
_CfprApFabricDceSwSrvPcEpName_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcEpName_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpName = _CfprApFabricDceSwSrvPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 15),
    _CfprApFabricDceSwSrvPcEpName_Type()
)
cfprApFabricDceSwSrvPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpName.setStatus("current")
_CfprApFabricDceSwSrvPcEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricDceSwSrvPcEpOperState_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpOperState = _CfprApFabricDceSwSrvPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 16),
    _CfprApFabricDceSwSrvPcEpOperState_Type()
)
cfprApFabricDceSwSrvPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpOperState.setStatus("current")
_CfprApFabricDceSwSrvPcEpOperStateReason_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcEpOperStateReason_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpOperStateReason = _CfprApFabricDceSwSrvPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 17),
    _CfprApFabricDceSwSrvPcEpOperStateReason_Type()
)
cfprApFabricDceSwSrvPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpOperStateReason.setStatus("current")
_CfprApFabricDceSwSrvPcEpPeerAggrPortId_Type = Gauge32
_CfprApFabricDceSwSrvPcEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpPeerAggrPortId = _CfprApFabricDceSwSrvPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 18),
    _CfprApFabricDceSwSrvPcEpPeerAggrPortId_Type()
)
cfprApFabricDceSwSrvPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpPeerAggrPortId.setStatus("current")
_CfprApFabricDceSwSrvPcEpPeerChassisId_Type = Gauge32
_CfprApFabricDceSwSrvPcEpPeerChassisId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpPeerChassisId = _CfprApFabricDceSwSrvPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 19),
    _CfprApFabricDceSwSrvPcEpPeerChassisId_Type()
)
cfprApFabricDceSwSrvPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpPeerChassisId.setStatus("current")
_CfprApFabricDceSwSrvPcEpPeerDn_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcEpPeerDn_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpPeerDn = _CfprApFabricDceSwSrvPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 20),
    _CfprApFabricDceSwSrvPcEpPeerDn_Type()
)
cfprApFabricDceSwSrvPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpPeerDn.setStatus("current")
_CfprApFabricDceSwSrvPcEpPeerPortId_Type = Gauge32
_CfprApFabricDceSwSrvPcEpPeerPortId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpPeerPortId = _CfprApFabricDceSwSrvPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 21),
    _CfprApFabricDceSwSrvPcEpPeerPortId_Type()
)
cfprApFabricDceSwSrvPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpPeerPortId.setStatus("current")
_CfprApFabricDceSwSrvPcEpPeerSlotId_Type = Gauge32
_CfprApFabricDceSwSrvPcEpPeerSlotId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpPeerSlotId = _CfprApFabricDceSwSrvPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 22),
    _CfprApFabricDceSwSrvPcEpPeerSlotId_Type()
)
cfprApFabricDceSwSrvPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpPeerSlotId.setStatus("current")
_CfprApFabricDceSwSrvPcEpPortId_Type = CfprApFabricDceSwSrvPcEpPortId
_CfprApFabricDceSwSrvPcEpPortId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpPortId = _CfprApFabricDceSwSrvPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 23),
    _CfprApFabricDceSwSrvPcEpPortId_Type()
)
cfprApFabricDceSwSrvPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpPortId.setStatus("current")
_CfprApFabricDceSwSrvPcEpSlotId_Type = CfprApFabricDceSwSrvPcEpSlotId
_CfprApFabricDceSwSrvPcEpSlotId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpSlotId = _CfprApFabricDceSwSrvPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 24),
    _CfprApFabricDceSwSrvPcEpSlotId_Type()
)
cfprApFabricDceSwSrvPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpSlotId.setStatus("current")
_CfprApFabricDceSwSrvPcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricDceSwSrvPcEpSwitchId_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpSwitchId = _CfprApFabricDceSwSrvPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 25),
    _CfprApFabricDceSwSrvPcEpSwitchId_Type()
)
cfprApFabricDceSwSrvPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpSwitchId.setStatus("current")
_CfprApFabricDceSwSrvPcEpTransport_Type = CfprApFabricADceSwSrvEpTransport
_CfprApFabricDceSwSrvPcEpTransport_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpTransport = _CfprApFabricDceSwSrvPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 26),
    _CfprApFabricDceSwSrvPcEpTransport_Type()
)
cfprApFabricDceSwSrvPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpTransport.setStatus("current")
_CfprApFabricDceSwSrvPcEpType_Type = CfprApFabricSwSrvEpType
_CfprApFabricDceSwSrvPcEpType_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpType = _CfprApFabricDceSwSrvPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 27),
    _CfprApFabricDceSwSrvPcEpType_Type()
)
cfprApFabricDceSwSrvPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpType.setStatus("current")
_CfprApFabricDceSwSrvPcEpUsrLbl_Type = SnmpAdminString
_CfprApFabricDceSwSrvPcEpUsrLbl_Object = MibTableColumn
cfprApFabricDceSwSrvPcEpUsrLbl = _CfprApFabricDceSwSrvPcEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 14, 1, 28),
    _CfprApFabricDceSwSrvPcEpUsrLbl_Type()
)
cfprApFabricDceSwSrvPcEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricDceSwSrvPcEpUsrLbl.setStatus("current")
_CfprApFabricEpTable_Object = MibTable
cfprApFabricEpTable = _CfprApFabricEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 15)
)
if mibBuilder.loadTexts:
    cfprApFabricEpTable.setStatus("current")
_CfprApFabricEpEntry_Object = MibTableRow
cfprApFabricEpEntry = _CfprApFabricEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 15, 1)
)
cfprApFabricEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEpEntry.setStatus("current")
_CfprApFabricEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEpInstanceId_Object = MibTableColumn
cfprApFabricEpInstanceId = _CfprApFabricEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 15, 1, 1),
    _CfprApFabricEpInstanceId_Type()
)
cfprApFabricEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEpInstanceId.setStatus("current")
_CfprApFabricEpDn_Type = CfprApManagedObjectDn
_CfprApFabricEpDn_Object = MibTableColumn
cfprApFabricEpDn = _CfprApFabricEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 15, 1, 2),
    _CfprApFabricEpDn_Type()
)
cfprApFabricEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpDn.setStatus("current")
_CfprApFabricEpRn_Type = SnmpAdminString
_CfprApFabricEpRn_Object = MibTableColumn
cfprApFabricEpRn = _CfprApFabricEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 15, 1, 3),
    _CfprApFabricEpRn_Type()
)
cfprApFabricEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpRn.setStatus("current")
_CfprApFabricEpMgrTable_Object = MibTable
cfprApFabricEpMgrTable = _CfprApFabricEpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16)
)
if mibBuilder.loadTexts:
    cfprApFabricEpMgrTable.setStatus("current")
_CfprApFabricEpMgrEntry_Object = MibTableRow
cfprApFabricEpMgrEntry = _CfprApFabricEpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1)
)
cfprApFabricEpMgrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEpMgrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEpMgrEntry.setStatus("current")
_CfprApFabricEpMgrInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEpMgrInstanceId_Object = MibTableColumn
cfprApFabricEpMgrInstanceId = _CfprApFabricEpMgrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 1),
    _CfprApFabricEpMgrInstanceId_Type()
)
cfprApFabricEpMgrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrInstanceId.setStatus("current")
_CfprApFabricEpMgrDn_Type = CfprApManagedObjectDn
_CfprApFabricEpMgrDn_Object = MibTableColumn
cfprApFabricEpMgrDn = _CfprApFabricEpMgrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 2),
    _CfprApFabricEpMgrDn_Type()
)
cfprApFabricEpMgrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrDn.setStatus("current")
_CfprApFabricEpMgrRn_Type = SnmpAdminString
_CfprApFabricEpMgrRn_Object = MibTableColumn
cfprApFabricEpMgrRn = _CfprApFabricEpMgrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 3),
    _CfprApFabricEpMgrRn_Type()
)
cfprApFabricEpMgrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrRn.setStatus("current")
_CfprApFabricEpMgrConfMode_Type = CfprApFabricConfMode
_CfprApFabricEpMgrConfMode_Object = MibTableColumn
cfprApFabricEpMgrConfMode = _CfprApFabricEpMgrConfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 4),
    _CfprApFabricEpMgrConfMode_Type()
)
cfprApFabricEpMgrConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrConfMode.setStatus("current")
_CfprApFabricEpMgrConfQual_Type = SnmpAdminString
_CfprApFabricEpMgrConfQual_Object = MibTableColumn
cfprApFabricEpMgrConfQual = _CfprApFabricEpMgrConfQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 5),
    _CfprApFabricEpMgrConfQual_Type()
)
cfprApFabricEpMgrConfQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrConfQual.setStatus("current")
_CfprApFabricEpMgrConfState_Type = CfprApFabricConfState
_CfprApFabricEpMgrConfState_Object = MibTableColumn
cfprApFabricEpMgrConfState = _CfprApFabricEpMgrConfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 6),
    _CfprApFabricEpMgrConfState_Type()
)
cfprApFabricEpMgrConfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrConfState.setStatus("current")
_CfprApFabricEpMgrFltAggr_Type = Unsigned64
_CfprApFabricEpMgrFltAggr_Object = MibTableColumn
cfprApFabricEpMgrFltAggr = _CfprApFabricEpMgrFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 7),
    _CfprApFabricEpMgrFltAggr_Type()
)
cfprApFabricEpMgrFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFltAggr.setStatus("current")
_CfprApFabricEpMgrFsmDescr_Type = SnmpAdminString
_CfprApFabricEpMgrFsmDescr_Object = MibTableColumn
cfprApFabricEpMgrFsmDescr = _CfprApFabricEpMgrFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 8),
    _CfprApFabricEpMgrFsmDescr_Type()
)
cfprApFabricEpMgrFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmDescr.setStatus("current")
_CfprApFabricEpMgrFsmFlags_Type = SnmpAdminString
_CfprApFabricEpMgrFsmFlags_Object = MibTableColumn
cfprApFabricEpMgrFsmFlags = _CfprApFabricEpMgrFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 9),
    _CfprApFabricEpMgrFsmFlags_Type()
)
cfprApFabricEpMgrFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmFlags.setStatus("current")
_CfprApFabricEpMgrFsmPrev_Type = SnmpAdminString
_CfprApFabricEpMgrFsmPrev_Object = MibTableColumn
cfprApFabricEpMgrFsmPrev = _CfprApFabricEpMgrFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 10),
    _CfprApFabricEpMgrFsmPrev_Type()
)
cfprApFabricEpMgrFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmPrev.setStatus("current")
_CfprApFabricEpMgrFsmProgr_Type = Gauge32
_CfprApFabricEpMgrFsmProgr_Object = MibTableColumn
cfprApFabricEpMgrFsmProgr = _CfprApFabricEpMgrFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 11),
    _CfprApFabricEpMgrFsmProgr_Type()
)
cfprApFabricEpMgrFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmProgr.setStatus("current")
_CfprApFabricEpMgrFsmRmtInvErrCode_Type = Gauge32
_CfprApFabricEpMgrFsmRmtInvErrCode_Object = MibTableColumn
cfprApFabricEpMgrFsmRmtInvErrCode = _CfprApFabricEpMgrFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 12),
    _CfprApFabricEpMgrFsmRmtInvErrCode_Type()
)
cfprApFabricEpMgrFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmRmtInvErrCode.setStatus("current")
_CfprApFabricEpMgrFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFabricEpMgrFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFabricEpMgrFsmRmtInvErrDescr = _CfprApFabricEpMgrFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 13),
    _CfprApFabricEpMgrFsmRmtInvErrDescr_Type()
)
cfprApFabricEpMgrFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmRmtInvErrDescr.setStatus("current")
_CfprApFabricEpMgrFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFabricEpMgrFsmRmtInvRslt_Object = MibTableColumn
cfprApFabricEpMgrFsmRmtInvRslt = _CfprApFabricEpMgrFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 14),
    _CfprApFabricEpMgrFsmRmtInvRslt_Type()
)
cfprApFabricEpMgrFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmRmtInvRslt.setStatus("current")
_CfprApFabricEpMgrFsmStageDescr_Type = SnmpAdminString
_CfprApFabricEpMgrFsmStageDescr_Object = MibTableColumn
cfprApFabricEpMgrFsmStageDescr = _CfprApFabricEpMgrFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 15),
    _CfprApFabricEpMgrFsmStageDescr_Type()
)
cfprApFabricEpMgrFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageDescr.setStatus("current")
_CfprApFabricEpMgrFsmStamp_Type = DateAndTime
_CfprApFabricEpMgrFsmStamp_Object = MibTableColumn
cfprApFabricEpMgrFsmStamp = _CfprApFabricEpMgrFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 16),
    _CfprApFabricEpMgrFsmStamp_Type()
)
cfprApFabricEpMgrFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStamp.setStatus("current")
_CfprApFabricEpMgrFsmStatus_Type = SnmpAdminString
_CfprApFabricEpMgrFsmStatus_Object = MibTableColumn
cfprApFabricEpMgrFsmStatus = _CfprApFabricEpMgrFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 17),
    _CfprApFabricEpMgrFsmStatus_Type()
)
cfprApFabricEpMgrFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStatus.setStatus("current")
_CfprApFabricEpMgrFsmTry_Type = Gauge32
_CfprApFabricEpMgrFsmTry_Object = MibTableColumn
cfprApFabricEpMgrFsmTry = _CfprApFabricEpMgrFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 18),
    _CfprApFabricEpMgrFsmTry_Type()
)
cfprApFabricEpMgrFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTry.setStatus("current")
_CfprApFabricEpMgrId_Type = CfprApNetworkSwitchId
_CfprApFabricEpMgrId_Object = MibTableColumn
cfprApFabricEpMgrId = _CfprApFabricEpMgrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 16, 1, 19),
    _CfprApFabricEpMgrId_Type()
)
cfprApFabricEpMgrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrId.setStatus("current")
_CfprApFabricEpMgrFsmTable_Object = MibTable
cfprApFabricEpMgrFsmTable = _CfprApFabricEpMgrFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17)
)
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTable.setStatus("current")
_CfprApFabricEpMgrFsmEntry_Object = MibTableRow
cfprApFabricEpMgrFsmEntry = _CfprApFabricEpMgrFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1)
)
cfprApFabricEpMgrFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEpMgrFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmEntry.setStatus("current")
_CfprApFabricEpMgrFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEpMgrFsmInstanceId_Object = MibTableColumn
cfprApFabricEpMgrFsmInstanceId = _CfprApFabricEpMgrFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 1),
    _CfprApFabricEpMgrFsmInstanceId_Type()
)
cfprApFabricEpMgrFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmInstanceId.setStatus("current")
_CfprApFabricEpMgrFsmDn_Type = CfprApManagedObjectDn
_CfprApFabricEpMgrFsmDn_Object = MibTableColumn
cfprApFabricEpMgrFsmDn = _CfprApFabricEpMgrFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 2),
    _CfprApFabricEpMgrFsmDn_Type()
)
cfprApFabricEpMgrFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmDn.setStatus("current")
_CfprApFabricEpMgrFsmRn_Type = SnmpAdminString
_CfprApFabricEpMgrFsmRn_Object = MibTableColumn
cfprApFabricEpMgrFsmRn = _CfprApFabricEpMgrFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 3),
    _CfprApFabricEpMgrFsmRn_Type()
)
cfprApFabricEpMgrFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmRn.setStatus("current")
_CfprApFabricEpMgrFsmCompletionTime_Type = DateAndTime
_CfprApFabricEpMgrFsmCompletionTime_Object = MibTableColumn
cfprApFabricEpMgrFsmCompletionTime = _CfprApFabricEpMgrFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 4),
    _CfprApFabricEpMgrFsmCompletionTime_Type()
)
cfprApFabricEpMgrFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmCompletionTime.setStatus("current")
_CfprApFabricEpMgrFsmCurrentFsm_Type = CfprApFabricEpMgrFsmCurrentFsm
_CfprApFabricEpMgrFsmCurrentFsm_Object = MibTableColumn
cfprApFabricEpMgrFsmCurrentFsm = _CfprApFabricEpMgrFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 5),
    _CfprApFabricEpMgrFsmCurrentFsm_Type()
)
cfprApFabricEpMgrFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmCurrentFsm.setStatus("current")
_CfprApFabricEpMgrFsmDescrData_Type = SnmpAdminString
_CfprApFabricEpMgrFsmDescrData_Object = MibTableColumn
cfprApFabricEpMgrFsmDescrData = _CfprApFabricEpMgrFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 6),
    _CfprApFabricEpMgrFsmDescrData_Type()
)
cfprApFabricEpMgrFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmDescrData.setStatus("current")
_CfprApFabricEpMgrFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFabricEpMgrFsmFsmStatus_Object = MibTableColumn
cfprApFabricEpMgrFsmFsmStatus = _CfprApFabricEpMgrFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 7),
    _CfprApFabricEpMgrFsmFsmStatus_Type()
)
cfprApFabricEpMgrFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmFsmStatus.setStatus("current")
_CfprApFabricEpMgrFsmProgress_Type = Gauge32
_CfprApFabricEpMgrFsmProgress_Object = MibTableColumn
cfprApFabricEpMgrFsmProgress = _CfprApFabricEpMgrFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 8),
    _CfprApFabricEpMgrFsmProgress_Type()
)
cfprApFabricEpMgrFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmProgress.setStatus("current")
_CfprApFabricEpMgrFsmRmtErrCode_Type = Gauge32
_CfprApFabricEpMgrFsmRmtErrCode_Object = MibTableColumn
cfprApFabricEpMgrFsmRmtErrCode = _CfprApFabricEpMgrFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 9),
    _CfprApFabricEpMgrFsmRmtErrCode_Type()
)
cfprApFabricEpMgrFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmRmtErrCode.setStatus("current")
_CfprApFabricEpMgrFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFabricEpMgrFsmRmtErrDescr_Object = MibTableColumn
cfprApFabricEpMgrFsmRmtErrDescr = _CfprApFabricEpMgrFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 10),
    _CfprApFabricEpMgrFsmRmtErrDescr_Type()
)
cfprApFabricEpMgrFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmRmtErrDescr.setStatus("current")
_CfprApFabricEpMgrFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFabricEpMgrFsmRmtRslt_Object = MibTableColumn
cfprApFabricEpMgrFsmRmtRslt = _CfprApFabricEpMgrFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 17, 1, 11),
    _CfprApFabricEpMgrFsmRmtRslt_Type()
)
cfprApFabricEpMgrFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmRmtRslt.setStatus("current")
_CfprApFabricEpMgrFsmStageTable_Object = MibTable
cfprApFabricEpMgrFsmStageTable = _CfprApFabricEpMgrFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18)
)
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageTable.setStatus("current")
_CfprApFabricEpMgrFsmStageEntry_Object = MibTableRow
cfprApFabricEpMgrFsmStageEntry = _CfprApFabricEpMgrFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1)
)
cfprApFabricEpMgrFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEpMgrFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageEntry.setStatus("current")
_CfprApFabricEpMgrFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEpMgrFsmStageInstanceId_Object = MibTableColumn
cfprApFabricEpMgrFsmStageInstanceId = _CfprApFabricEpMgrFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 1),
    _CfprApFabricEpMgrFsmStageInstanceId_Type()
)
cfprApFabricEpMgrFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageInstanceId.setStatus("current")
_CfprApFabricEpMgrFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFabricEpMgrFsmStageDn_Object = MibTableColumn
cfprApFabricEpMgrFsmStageDn = _CfprApFabricEpMgrFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 2),
    _CfprApFabricEpMgrFsmStageDn_Type()
)
cfprApFabricEpMgrFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageDn.setStatus("current")
_CfprApFabricEpMgrFsmStageRn_Type = SnmpAdminString
_CfprApFabricEpMgrFsmStageRn_Object = MibTableColumn
cfprApFabricEpMgrFsmStageRn = _CfprApFabricEpMgrFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 3),
    _CfprApFabricEpMgrFsmStageRn_Type()
)
cfprApFabricEpMgrFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageRn.setStatus("current")
_CfprApFabricEpMgrFsmStageDescrData_Type = SnmpAdminString
_CfprApFabricEpMgrFsmStageDescrData_Object = MibTableColumn
cfprApFabricEpMgrFsmStageDescrData = _CfprApFabricEpMgrFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 4),
    _CfprApFabricEpMgrFsmStageDescrData_Type()
)
cfprApFabricEpMgrFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageDescrData.setStatus("current")
_CfprApFabricEpMgrFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFabricEpMgrFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFabricEpMgrFsmStageLastUpdateTime = _CfprApFabricEpMgrFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 5),
    _CfprApFabricEpMgrFsmStageLastUpdateTime_Type()
)
cfprApFabricEpMgrFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageLastUpdateTime.setStatus("current")
_CfprApFabricEpMgrFsmStageName_Type = CfprApFabricEpMgrFsmStageName
_CfprApFabricEpMgrFsmStageName_Object = MibTableColumn
cfprApFabricEpMgrFsmStageName = _CfprApFabricEpMgrFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 6),
    _CfprApFabricEpMgrFsmStageName_Type()
)
cfprApFabricEpMgrFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageName.setStatus("current")
_CfprApFabricEpMgrFsmStageOrder_Type = Gauge32
_CfprApFabricEpMgrFsmStageOrder_Object = MibTableColumn
cfprApFabricEpMgrFsmStageOrder = _CfprApFabricEpMgrFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 7),
    _CfprApFabricEpMgrFsmStageOrder_Type()
)
cfprApFabricEpMgrFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageOrder.setStatus("current")
_CfprApFabricEpMgrFsmStageRetry_Type = Gauge32
_CfprApFabricEpMgrFsmStageRetry_Object = MibTableColumn
cfprApFabricEpMgrFsmStageRetry = _CfprApFabricEpMgrFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 8),
    _CfprApFabricEpMgrFsmStageRetry_Type()
)
cfprApFabricEpMgrFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageRetry.setStatus("current")
_CfprApFabricEpMgrFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFabricEpMgrFsmStageStageStatus_Object = MibTableColumn
cfprApFabricEpMgrFsmStageStageStatus = _CfprApFabricEpMgrFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 18, 1, 9),
    _CfprApFabricEpMgrFsmStageStageStatus_Type()
)
cfprApFabricEpMgrFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmStageStageStatus.setStatus("current")
_CfprApFabricEpMgrFsmTaskTable_Object = MibTable
cfprApFabricEpMgrFsmTaskTable = _CfprApFabricEpMgrFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19)
)
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskTable.setStatus("current")
_CfprApFabricEpMgrFsmTaskEntry_Object = MibTableRow
cfprApFabricEpMgrFsmTaskEntry = _CfprApFabricEpMgrFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19, 1)
)
cfprApFabricEpMgrFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEpMgrFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskEntry.setStatus("current")
_CfprApFabricEpMgrFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEpMgrFsmTaskInstanceId_Object = MibTableColumn
cfprApFabricEpMgrFsmTaskInstanceId = _CfprApFabricEpMgrFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19, 1, 1),
    _CfprApFabricEpMgrFsmTaskInstanceId_Type()
)
cfprApFabricEpMgrFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskInstanceId.setStatus("current")
_CfprApFabricEpMgrFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFabricEpMgrFsmTaskDn_Object = MibTableColumn
cfprApFabricEpMgrFsmTaskDn = _CfprApFabricEpMgrFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19, 1, 2),
    _CfprApFabricEpMgrFsmTaskDn_Type()
)
cfprApFabricEpMgrFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskDn.setStatus("current")
_CfprApFabricEpMgrFsmTaskRn_Type = SnmpAdminString
_CfprApFabricEpMgrFsmTaskRn_Object = MibTableColumn
cfprApFabricEpMgrFsmTaskRn = _CfprApFabricEpMgrFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19, 1, 3),
    _CfprApFabricEpMgrFsmTaskRn_Type()
)
cfprApFabricEpMgrFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskRn.setStatus("current")
_CfprApFabricEpMgrFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFabricEpMgrFsmTaskCompletion_Object = MibTableColumn
cfprApFabricEpMgrFsmTaskCompletion = _CfprApFabricEpMgrFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19, 1, 4),
    _CfprApFabricEpMgrFsmTaskCompletion_Type()
)
cfprApFabricEpMgrFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskCompletion.setStatus("current")
_CfprApFabricEpMgrFsmTaskFlags_Type = CfprApFabricEpMgrFsmTaskFlags
_CfprApFabricEpMgrFsmTaskFlags_Object = MibTableColumn
cfprApFabricEpMgrFsmTaskFlags = _CfprApFabricEpMgrFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19, 1, 5),
    _CfprApFabricEpMgrFsmTaskFlags_Type()
)
cfprApFabricEpMgrFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskFlags.setStatus("current")
_CfprApFabricEpMgrFsmTaskItem_Type = CfprApFabricEpMgrFsmTaskItem
_CfprApFabricEpMgrFsmTaskItem_Object = MibTableColumn
cfprApFabricEpMgrFsmTaskItem = _CfprApFabricEpMgrFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19, 1, 6),
    _CfprApFabricEpMgrFsmTaskItem_Type()
)
cfprApFabricEpMgrFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskItem.setStatus("current")
_CfprApFabricEpMgrFsmTaskSeqId_Type = Gauge32
_CfprApFabricEpMgrFsmTaskSeqId_Object = MibTableColumn
cfprApFabricEpMgrFsmTaskSeqId = _CfprApFabricEpMgrFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 19, 1, 7),
    _CfprApFabricEpMgrFsmTaskSeqId_Type()
)
cfprApFabricEpMgrFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEpMgrFsmTaskSeqId.setStatus("current")
_CfprApFabricEthEstcTable_Object = MibTable
cfprApFabricEthEstcTable = _CfprApFabricEthEstcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20)
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcTable.setStatus("current")
_CfprApFabricEthEstcEntry_Object = MibTableRow
cfprApFabricEthEstcEntry = _CfprApFabricEthEstcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1)
)
cfprApFabricEthEstcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthEstcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEntry.setStatus("current")
_CfprApFabricEthEstcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthEstcInstanceId_Object = MibTableColumn
cfprApFabricEthEstcInstanceId = _CfprApFabricEthEstcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1, 1),
    _CfprApFabricEthEstcInstanceId_Type()
)
cfprApFabricEthEstcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcInstanceId.setStatus("current")
_CfprApFabricEthEstcDn_Type = CfprApManagedObjectDn
_CfprApFabricEthEstcDn_Object = MibTableColumn
cfprApFabricEthEstcDn = _CfprApFabricEthEstcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1, 2),
    _CfprApFabricEthEstcDn_Type()
)
cfprApFabricEthEstcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcDn.setStatus("current")
_CfprApFabricEthEstcRn_Type = SnmpAdminString
_CfprApFabricEthEstcRn_Object = MibTableColumn
cfprApFabricEthEstcRn = _CfprApFabricEthEstcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1, 3),
    _CfprApFabricEthEstcRn_Type()
)
cfprApFabricEthEstcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcRn.setStatus("current")
_CfprApFabricEthEstcId_Type = CfprApNetworkSwitchId
_CfprApFabricEthEstcId_Object = MibTableColumn
cfprApFabricEthEstcId = _CfprApFabricEthEstcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1, 4),
    _CfprApFabricEthEstcId_Type()
)
cfprApFabricEthEstcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcId.setStatus("current")
_CfprApFabricEthEstcLocale_Type = CfprApFabricExternalLocale
_CfprApFabricEthEstcLocale_Object = MibTableColumn
cfprApFabricEthEstcLocale = _CfprApFabricEthEstcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1, 5),
    _CfprApFabricEthEstcLocale_Type()
)
cfprApFabricEthEstcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcLocale.setStatus("current")
_CfprApFabricEthEstcName_Type = SnmpAdminString
_CfprApFabricEthEstcName_Object = MibTableColumn
cfprApFabricEthEstcName = _CfprApFabricEthEstcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1, 6),
    _CfprApFabricEthEstcName_Type()
)
cfprApFabricEthEstcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcName.setStatus("current")
_CfprApFabricEthEstcTransport_Type = CfprApFabricEthEstcTransport
_CfprApFabricEthEstcTransport_Object = MibTableColumn
cfprApFabricEthEstcTransport = _CfprApFabricEthEstcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1, 7),
    _CfprApFabricEthEstcTransport_Type()
)
cfprApFabricEthEstcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcTransport.setStatus("current")
_CfprApFabricEthEstcType_Type = CfprApFabricEthEstcType
_CfprApFabricEthEstcType_Object = MibTableColumn
cfprApFabricEthEstcType = _CfprApFabricEthEstcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 20, 1, 8),
    _CfprApFabricEthEstcType_Type()
)
cfprApFabricEthEstcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcType.setStatus("current")
_CfprApFabricEthEstcCloudTable_Object = MibTable
cfprApFabricEthEstcCloudTable = _CfprApFabricEthEstcCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 21)
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcCloudTable.setStatus("current")
_CfprApFabricEthEstcCloudEntry_Object = MibTableRow
cfprApFabricEthEstcCloudEntry = _CfprApFabricEthEstcCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 21, 1)
)
cfprApFabricEthEstcCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthEstcCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcCloudEntry.setStatus("current")
_CfprApFabricEthEstcCloudInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthEstcCloudInstanceId_Object = MibTableColumn
cfprApFabricEthEstcCloudInstanceId = _CfprApFabricEthEstcCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 21, 1, 1),
    _CfprApFabricEthEstcCloudInstanceId_Type()
)
cfprApFabricEthEstcCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcCloudInstanceId.setStatus("current")
_CfprApFabricEthEstcCloudDn_Type = CfprApManagedObjectDn
_CfprApFabricEthEstcCloudDn_Object = MibTableColumn
cfprApFabricEthEstcCloudDn = _CfprApFabricEthEstcCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 21, 1, 2),
    _CfprApFabricEthEstcCloudDn_Type()
)
cfprApFabricEthEstcCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcCloudDn.setStatus("current")
_CfprApFabricEthEstcCloudRn_Type = SnmpAdminString
_CfprApFabricEthEstcCloudRn_Object = MibTableColumn
cfprApFabricEthEstcCloudRn = _CfprApFabricEthEstcCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 21, 1, 3),
    _CfprApFabricEthEstcCloudRn_Type()
)
cfprApFabricEthEstcCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcCloudRn.setStatus("current")
_CfprApFabricEthEstcEpTable_Object = MibTable
cfprApFabricEthEstcEpTable = _CfprApFabricEthEstcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22)
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpTable.setStatus("current")
_CfprApFabricEthEstcEpEntry_Object = MibTableRow
cfprApFabricEthEstcEpEntry = _CfprApFabricEthEstcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1)
)
cfprApFabricEthEstcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthEstcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpEntry.setStatus("current")
_CfprApFabricEthEstcEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthEstcEpInstanceId_Object = MibTableColumn
cfprApFabricEthEstcEpInstanceId = _CfprApFabricEthEstcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 1),
    _CfprApFabricEthEstcEpInstanceId_Type()
)
cfprApFabricEthEstcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpInstanceId.setStatus("current")
_CfprApFabricEthEstcEpDn_Type = CfprApManagedObjectDn
_CfprApFabricEthEstcEpDn_Object = MibTableColumn
cfprApFabricEthEstcEpDn = _CfprApFabricEthEstcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 2),
    _CfprApFabricEthEstcEpDn_Type()
)
cfprApFabricEthEstcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpDn.setStatus("current")
_CfprApFabricEthEstcEpRn_Type = SnmpAdminString
_CfprApFabricEthEstcEpRn_Object = MibTableColumn
cfprApFabricEthEstcEpRn = _CfprApFabricEthEstcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 3),
    _CfprApFabricEthEstcEpRn_Type()
)
cfprApFabricEthEstcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpRn.setStatus("current")
_CfprApFabricEthEstcEpAdminSpeed_Type = CfprApPortEthSpeed
_CfprApFabricEthEstcEpAdminSpeed_Object = MibTableColumn
cfprApFabricEthEstcEpAdminSpeed = _CfprApFabricEthEstcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 4),
    _CfprApFabricEthEstcEpAdminSpeed_Type()
)
cfprApFabricEthEstcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpAdminSpeed.setStatus("current")
_CfprApFabricEthEstcEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricEthEstcEpAdminState_Object = MibTableColumn
cfprApFabricEthEstcEpAdminState = _CfprApFabricEthEstcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 5),
    _CfprApFabricEthEstcEpAdminState_Type()
)
cfprApFabricEthEstcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpAdminState.setStatus("current")
_CfprApFabricEthEstcEpAggrPortId_Type = Gauge32
_CfprApFabricEthEstcEpAggrPortId_Object = MibTableColumn
cfprApFabricEthEstcEpAggrPortId = _CfprApFabricEthEstcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 6),
    _CfprApFabricEthEstcEpAggrPortId_Type()
)
cfprApFabricEthEstcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpAggrPortId.setStatus("current")
_CfprApFabricEthEstcEpChassisId_Type = Gauge32
_CfprApFabricEthEstcEpChassisId_Object = MibTableColumn
cfprApFabricEthEstcEpChassisId = _CfprApFabricEthEstcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 7),
    _CfprApFabricEthEstcEpChassisId_Type()
)
cfprApFabricEthEstcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpChassisId.setStatus("current")
_CfprApFabricEthEstcEpConfigState_Type = CfprApFabricConfigState
_CfprApFabricEthEstcEpConfigState_Object = MibTableColumn
cfprApFabricEthEstcEpConfigState = _CfprApFabricEthEstcEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 8),
    _CfprApFabricEthEstcEpConfigState_Type()
)
cfprApFabricEthEstcEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpConfigState.setStatus("current")
_CfprApFabricEthEstcEpEpDn_Type = SnmpAdminString
_CfprApFabricEthEstcEpEpDn_Object = MibTableColumn
cfprApFabricEthEstcEpEpDn = _CfprApFabricEthEstcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 9),
    _CfprApFabricEthEstcEpEpDn_Type()
)
cfprApFabricEthEstcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpEpDn.setStatus("current")
_CfprApFabricEthEstcEpFlowCtrlPolicy_Type = SnmpAdminString
_CfprApFabricEthEstcEpFlowCtrlPolicy_Object = MibTableColumn
cfprApFabricEthEstcEpFlowCtrlPolicy = _CfprApFabricEthEstcEpFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 10),
    _CfprApFabricEthEstcEpFlowCtrlPolicy_Type()
)
cfprApFabricEthEstcEpFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpFlowCtrlPolicy.setStatus("current")
_CfprApFabricEthEstcEpFltAggr_Type = Unsigned64
_CfprApFabricEthEstcEpFltAggr_Object = MibTableColumn
cfprApFabricEthEstcEpFltAggr = _CfprApFabricEthEstcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 11),
    _CfprApFabricEthEstcEpFltAggr_Type()
)
cfprApFabricEthEstcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpFltAggr.setStatus("current")
_CfprApFabricEthEstcEpIfRole_Type = CfprApFabricAEthEstcEpIfRole
_CfprApFabricEthEstcEpIfRole_Object = MibTableColumn
cfprApFabricEthEstcEpIfRole = _CfprApFabricEthEstcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 12),
    _CfprApFabricEthEstcEpIfRole_Type()
)
cfprApFabricEthEstcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpIfRole.setStatus("current")
_CfprApFabricEthEstcEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricEthEstcEpIfType_Object = MibTableColumn
cfprApFabricEthEstcEpIfType = _CfprApFabricEthEstcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 13),
    _CfprApFabricEthEstcEpIfType_Type()
)
cfprApFabricEthEstcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpIfType.setStatus("current")
_CfprApFabricEthEstcEpLicGP_Type = Unsigned64
_CfprApFabricEthEstcEpLicGP_Object = MibTableColumn
cfprApFabricEthEstcEpLicGP = _CfprApFabricEthEstcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 14),
    _CfprApFabricEthEstcEpLicGP_Type()
)
cfprApFabricEthEstcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpLicGP.setStatus("current")
_CfprApFabricEthEstcEpLicState_Type = CfprApLicenseState
_CfprApFabricEthEstcEpLicState_Object = MibTableColumn
cfprApFabricEthEstcEpLicState = _CfprApFabricEthEstcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 15),
    _CfprApFabricEthEstcEpLicState_Type()
)
cfprApFabricEthEstcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpLicState.setStatus("current")
_CfprApFabricEthEstcEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricEthEstcEpLocale_Object = MibTableColumn
cfprApFabricEthEstcEpLocale = _CfprApFabricEthEstcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 16),
    _CfprApFabricEthEstcEpLocale_Type()
)
cfprApFabricEthEstcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpLocale.setStatus("current")
_CfprApFabricEthEstcEpName_Type = SnmpAdminString
_CfprApFabricEthEstcEpName_Object = MibTableColumn
cfprApFabricEthEstcEpName = _CfprApFabricEthEstcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 17),
    _CfprApFabricEthEstcEpName_Type()
)
cfprApFabricEthEstcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpName.setStatus("current")
_CfprApFabricEthEstcEpNwCtrlPolicyName_Type = SnmpAdminString
_CfprApFabricEthEstcEpNwCtrlPolicyName_Object = MibTableColumn
cfprApFabricEthEstcEpNwCtrlPolicyName = _CfprApFabricEthEstcEpNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 18),
    _CfprApFabricEthEstcEpNwCtrlPolicyName_Type()
)
cfprApFabricEthEstcEpNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpNwCtrlPolicyName.setStatus("current")
_CfprApFabricEthEstcEpOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprApFabricEthEstcEpOperNwCtrlPolicyName_Object = MibTableColumn
cfprApFabricEthEstcEpOperNwCtrlPolicyName = _CfprApFabricEthEstcEpOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 19),
    _CfprApFabricEthEstcEpOperNwCtrlPolicyName_Type()
)
cfprApFabricEthEstcEpOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpOperNwCtrlPolicyName.setStatus("current")
_CfprApFabricEthEstcEpOperPortMode_Type = CfprApFabricEthEstcOperPortMode
_CfprApFabricEthEstcEpOperPortMode_Object = MibTableColumn
cfprApFabricEthEstcEpOperPortMode = _CfprApFabricEthEstcEpOperPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 20),
    _CfprApFabricEthEstcEpOperPortMode_Type()
)
cfprApFabricEthEstcEpOperPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpOperPortMode.setStatus("current")
_CfprApFabricEthEstcEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricEthEstcEpOperState_Object = MibTableColumn
cfprApFabricEthEstcEpOperState = _CfprApFabricEthEstcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 21),
    _CfprApFabricEthEstcEpOperState_Type()
)
cfprApFabricEthEstcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpOperState.setStatus("current")
_CfprApFabricEthEstcEpOperStateReason_Type = SnmpAdminString
_CfprApFabricEthEstcEpOperStateReason_Object = MibTableColumn
cfprApFabricEthEstcEpOperStateReason = _CfprApFabricEthEstcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 22),
    _CfprApFabricEthEstcEpOperStateReason_Type()
)
cfprApFabricEthEstcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpOperStateReason.setStatus("current")
_CfprApFabricEthEstcEpPeerAggrPortId_Type = Gauge32
_CfprApFabricEthEstcEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricEthEstcEpPeerAggrPortId = _CfprApFabricEthEstcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 23),
    _CfprApFabricEthEstcEpPeerAggrPortId_Type()
)
cfprApFabricEthEstcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPeerAggrPortId.setStatus("current")
_CfprApFabricEthEstcEpPeerChassisId_Type = Gauge32
_CfprApFabricEthEstcEpPeerChassisId_Object = MibTableColumn
cfprApFabricEthEstcEpPeerChassisId = _CfprApFabricEthEstcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 24),
    _CfprApFabricEthEstcEpPeerChassisId_Type()
)
cfprApFabricEthEstcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPeerChassisId.setStatus("current")
_CfprApFabricEthEstcEpPeerDn_Type = SnmpAdminString
_CfprApFabricEthEstcEpPeerDn_Object = MibTableColumn
cfprApFabricEthEstcEpPeerDn = _CfprApFabricEthEstcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 25),
    _CfprApFabricEthEstcEpPeerDn_Type()
)
cfprApFabricEthEstcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPeerDn.setStatus("current")
_CfprApFabricEthEstcEpPeerPortId_Type = Gauge32
_CfprApFabricEthEstcEpPeerPortId_Object = MibTableColumn
cfprApFabricEthEstcEpPeerPortId = _CfprApFabricEthEstcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 26),
    _CfprApFabricEthEstcEpPeerPortId_Type()
)
cfprApFabricEthEstcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPeerPortId.setStatus("current")
_CfprApFabricEthEstcEpPeerSlotId_Type = Gauge32
_CfprApFabricEthEstcEpPeerSlotId_Object = MibTableColumn
cfprApFabricEthEstcEpPeerSlotId = _CfprApFabricEthEstcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 27),
    _CfprApFabricEthEstcEpPeerSlotId_Type()
)
cfprApFabricEthEstcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPeerSlotId.setStatus("current")
_CfprApFabricEthEstcEpPinGroupName_Type = SnmpAdminString
_CfprApFabricEthEstcEpPinGroupName_Object = MibTableColumn
cfprApFabricEthEstcEpPinGroupName = _CfprApFabricEthEstcEpPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 28),
    _CfprApFabricEthEstcEpPinGroupName_Type()
)
cfprApFabricEthEstcEpPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPinGroupName.setStatus("current")
_CfprApFabricEthEstcEpPortId_Type = CfprApFabricEthEstcEpPortId
_CfprApFabricEthEstcEpPortId_Object = MibTableColumn
cfprApFabricEthEstcEpPortId = _CfprApFabricEthEstcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 29),
    _CfprApFabricEthEstcEpPortId_Type()
)
cfprApFabricEthEstcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPortId.setStatus("current")
_CfprApFabricEthEstcEpPortMode_Type = CfprApFabricEthEstcPortMode
_CfprApFabricEthEstcEpPortMode_Object = MibTableColumn
cfprApFabricEthEstcEpPortMode = _CfprApFabricEthEstcEpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 30),
    _CfprApFabricEthEstcEpPortMode_Type()
)
cfprApFabricEthEstcEpPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPortMode.setStatus("current")
_CfprApFabricEthEstcEpPrio_Type = CfprApFabricEthEstcEpPrio
_CfprApFabricEthEstcEpPrio_Object = MibTableColumn
cfprApFabricEthEstcEpPrio = _CfprApFabricEthEstcEpPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 31),
    _CfprApFabricEthEstcEpPrio_Type()
)
cfprApFabricEthEstcEpPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpPrio.setStatus("current")
_CfprApFabricEthEstcEpSlotId_Type = CfprApFabricEthEstcEpSlotId
_CfprApFabricEthEstcEpSlotId_Object = MibTableColumn
cfprApFabricEthEstcEpSlotId = _CfprApFabricEthEstcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 32),
    _CfprApFabricEthEstcEpSlotId_Type()
)
cfprApFabricEthEstcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpSlotId.setStatus("current")
_CfprApFabricEthEstcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthEstcEpSwitchId_Object = MibTableColumn
cfprApFabricEthEstcEpSwitchId = _CfprApFabricEthEstcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 33),
    _CfprApFabricEthEstcEpSwitchId_Type()
)
cfprApFabricEthEstcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpSwitchId.setStatus("current")
_CfprApFabricEthEstcEpTransport_Type = CfprApFabricEthEstcEpTransport
_CfprApFabricEthEstcEpTransport_Object = MibTableColumn
cfprApFabricEthEstcEpTransport = _CfprApFabricEthEstcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 34),
    _CfprApFabricEthEstcEpTransport_Type()
)
cfprApFabricEthEstcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpTransport.setStatus("current")
_CfprApFabricEthEstcEpType_Type = CfprApFabricEthEstcEpType
_CfprApFabricEthEstcEpType_Object = MibTableColumn
cfprApFabricEthEstcEpType = _CfprApFabricEthEstcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 35),
    _CfprApFabricEthEstcEpType_Type()
)
cfprApFabricEthEstcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpType.setStatus("current")
_CfprApFabricEthEstcEpUsrLbl_Type = SnmpAdminString
_CfprApFabricEthEstcEpUsrLbl_Object = MibTableColumn
cfprApFabricEthEstcEpUsrLbl = _CfprApFabricEthEstcEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 36),
    _CfprApFabricEthEstcEpUsrLbl_Type()
)
cfprApFabricEthEstcEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpUsrLbl.setStatus("current")
_CfprApFabricEthEstcEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthEstcEpWarnings_Object = MibTableColumn
cfprApFabricEthEstcEpWarnings = _CfprApFabricEthEstcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 22, 1, 37),
    _CfprApFabricEthEstcEpWarnings_Type()
)
cfprApFabricEthEstcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcEpWarnings.setStatus("current")
_CfprApFabricEthEstcPcTable_Object = MibTable
cfprApFabricEthEstcPcTable = _CfprApFabricEthEstcPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23)
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcTable.setStatus("current")
_CfprApFabricEthEstcPcEntry_Object = MibTableRow
cfprApFabricEthEstcPcEntry = _CfprApFabricEthEstcPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1)
)
cfprApFabricEthEstcPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthEstcPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEntry.setStatus("current")
_CfprApFabricEthEstcPcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthEstcPcInstanceId_Object = MibTableColumn
cfprApFabricEthEstcPcInstanceId = _CfprApFabricEthEstcPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 1),
    _CfprApFabricEthEstcPcInstanceId_Type()
)
cfprApFabricEthEstcPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcInstanceId.setStatus("current")
_CfprApFabricEthEstcPcDn_Type = CfprApManagedObjectDn
_CfprApFabricEthEstcPcDn_Object = MibTableColumn
cfprApFabricEthEstcPcDn = _CfprApFabricEthEstcPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 2),
    _CfprApFabricEthEstcPcDn_Type()
)
cfprApFabricEthEstcPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcDn.setStatus("current")
_CfprApFabricEthEstcPcRn_Type = SnmpAdminString
_CfprApFabricEthEstcPcRn_Object = MibTableColumn
cfprApFabricEthEstcPcRn = _CfprApFabricEthEstcPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 3),
    _CfprApFabricEthEstcPcRn_Type()
)
cfprApFabricEthEstcPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcRn.setStatus("current")
_CfprApFabricEthEstcPcAdminSpeed_Type = CfprApPortEthAdminSpeed
_CfprApFabricEthEstcPcAdminSpeed_Object = MibTableColumn
cfprApFabricEthEstcPcAdminSpeed = _CfprApFabricEthEstcPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 4),
    _CfprApFabricEthEstcPcAdminSpeed_Type()
)
cfprApFabricEthEstcPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcAdminSpeed.setStatus("current")
_CfprApFabricEthEstcPcAdminState_Type = CfprApFabricCIoEpAdminState
_CfprApFabricEthEstcPcAdminState_Object = MibTableColumn
cfprApFabricEthEstcPcAdminState = _CfprApFabricEthEstcPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 5),
    _CfprApFabricEthEstcPcAdminState_Type()
)
cfprApFabricEthEstcPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcAdminState.setStatus("current")
_CfprApFabricEthEstcPcDescr_Type = SnmpAdminString
_CfprApFabricEthEstcPcDescr_Object = MibTableColumn
cfprApFabricEthEstcPcDescr = _CfprApFabricEthEstcPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 6),
    _CfprApFabricEthEstcPcDescr_Type()
)
cfprApFabricEthEstcPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcDescr.setStatus("current")
_CfprApFabricEthEstcPcEpDn_Type = SnmpAdminString
_CfprApFabricEthEstcPcEpDn_Object = MibTableColumn
cfprApFabricEthEstcPcEpDn = _CfprApFabricEthEstcPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 7),
    _CfprApFabricEthEstcPcEpDn_Type()
)
cfprApFabricEthEstcPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpDn.setStatus("current")
_CfprApFabricEthEstcPcFlowCtrlPolicy_Type = SnmpAdminString
_CfprApFabricEthEstcPcFlowCtrlPolicy_Object = MibTableColumn
cfprApFabricEthEstcPcFlowCtrlPolicy = _CfprApFabricEthEstcPcFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 8),
    _CfprApFabricEthEstcPcFlowCtrlPolicy_Type()
)
cfprApFabricEthEstcPcFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcFlowCtrlPolicy.setStatus("current")
_CfprApFabricEthEstcPcFltAggr_Type = Unsigned64
_CfprApFabricEthEstcPcFltAggr_Object = MibTableColumn
cfprApFabricEthEstcPcFltAggr = _CfprApFabricEthEstcPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 9),
    _CfprApFabricEthEstcPcFltAggr_Type()
)
cfprApFabricEthEstcPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcFltAggr.setStatus("current")
_CfprApFabricEthEstcPcIfRole_Type = CfprApFabricEstcPcIfRole
_CfprApFabricEthEstcPcIfRole_Object = MibTableColumn
cfprApFabricEthEstcPcIfRole = _CfprApFabricEthEstcPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 10),
    _CfprApFabricEthEstcPcIfRole_Type()
)
cfprApFabricEthEstcPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcIfRole.setStatus("current")
_CfprApFabricEthEstcPcIfType_Type = CfprApFabricCIoEpIfType
_CfprApFabricEthEstcPcIfType_Object = MibTableColumn
cfprApFabricEthEstcPcIfType = _CfprApFabricEthEstcPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 11),
    _CfprApFabricEthEstcPcIfType_Type()
)
cfprApFabricEthEstcPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcIfType.setStatus("current")
_CfprApFabricEthEstcPcLacpPolicyName_Type = SnmpAdminString
_CfprApFabricEthEstcPcLacpPolicyName_Object = MibTableColumn
cfprApFabricEthEstcPcLacpPolicyName = _CfprApFabricEthEstcPcLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 12),
    _CfprApFabricEthEstcPcLacpPolicyName_Type()
)
cfprApFabricEthEstcPcLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcLacpPolicyName.setStatus("current")
_CfprApFabricEthEstcPcLocale_Type = CfprApFabricExternalPcLocale
_CfprApFabricEthEstcPcLocale_Object = MibTableColumn
cfprApFabricEthEstcPcLocale = _CfprApFabricEthEstcPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 13),
    _CfprApFabricEthEstcPcLocale_Type()
)
cfprApFabricEthEstcPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcLocale.setStatus("current")
_CfprApFabricEthEstcPcName_Type = SnmpAdminString
_CfprApFabricEthEstcPcName_Object = MibTableColumn
cfprApFabricEthEstcPcName = _CfprApFabricEthEstcPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 14),
    _CfprApFabricEthEstcPcName_Type()
)
cfprApFabricEthEstcPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcName.setStatus("current")
_CfprApFabricEthEstcPcNwCtrlPolicyName_Type = SnmpAdminString
_CfprApFabricEthEstcPcNwCtrlPolicyName_Object = MibTableColumn
cfprApFabricEthEstcPcNwCtrlPolicyName = _CfprApFabricEthEstcPcNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 15),
    _CfprApFabricEthEstcPcNwCtrlPolicyName_Type()
)
cfprApFabricEthEstcPcNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcNwCtrlPolicyName.setStatus("current")
_CfprApFabricEthEstcPcOperLacpPolicyName_Type = SnmpAdminString
_CfprApFabricEthEstcPcOperLacpPolicyName_Object = MibTableColumn
cfprApFabricEthEstcPcOperLacpPolicyName = _CfprApFabricEthEstcPcOperLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 16),
    _CfprApFabricEthEstcPcOperLacpPolicyName_Type()
)
cfprApFabricEthEstcPcOperLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcOperLacpPolicyName.setStatus("current")
_CfprApFabricEthEstcPcOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprApFabricEthEstcPcOperNwCtrlPolicyName_Object = MibTableColumn
cfprApFabricEthEstcPcOperNwCtrlPolicyName = _CfprApFabricEthEstcPcOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 17),
    _CfprApFabricEthEstcPcOperNwCtrlPolicyName_Type()
)
cfprApFabricEthEstcPcOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcOperNwCtrlPolicyName.setStatus("current")
_CfprApFabricEthEstcPcOperSpeed_Type = CfprApPortEthSpeed
_CfprApFabricEthEstcPcOperSpeed_Object = MibTableColumn
cfprApFabricEthEstcPcOperSpeed = _CfprApFabricEthEstcPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 18),
    _CfprApFabricEthEstcPcOperSpeed_Type()
)
cfprApFabricEthEstcPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcOperSpeed.setStatus("current")
_CfprApFabricEthEstcPcOperState_Type = CfprApNetworkPortOperState
_CfprApFabricEthEstcPcOperState_Object = MibTableColumn
cfprApFabricEthEstcPcOperState = _CfprApFabricEthEstcPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 19),
    _CfprApFabricEthEstcPcOperState_Type()
)
cfprApFabricEthEstcPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcOperState.setStatus("current")
_CfprApFabricEthEstcPcPeerDn_Type = SnmpAdminString
_CfprApFabricEthEstcPcPeerDn_Object = MibTableColumn
cfprApFabricEthEstcPcPeerDn = _CfprApFabricEthEstcPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 20),
    _CfprApFabricEthEstcPcPeerDn_Type()
)
cfprApFabricEthEstcPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcPeerDn.setStatus("current")
_CfprApFabricEthEstcPcPinGroupName_Type = SnmpAdminString
_CfprApFabricEthEstcPcPinGroupName_Object = MibTableColumn
cfprApFabricEthEstcPcPinGroupName = _CfprApFabricEthEstcPcPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 21),
    _CfprApFabricEthEstcPcPinGroupName_Type()
)
cfprApFabricEthEstcPcPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcPinGroupName.setStatus("current")
_CfprApFabricEthEstcPcPortId_Type = Gauge32
_CfprApFabricEthEstcPcPortId_Object = MibTableColumn
cfprApFabricEthEstcPcPortId = _CfprApFabricEthEstcPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 22),
    _CfprApFabricEthEstcPcPortId_Type()
)
cfprApFabricEthEstcPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcPortId.setStatus("current")
_CfprApFabricEthEstcPcPortMode_Type = CfprApFabricEthEstcPortMode
_CfprApFabricEthEstcPcPortMode_Object = MibTableColumn
cfprApFabricEthEstcPcPortMode = _CfprApFabricEthEstcPcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 23),
    _CfprApFabricEthEstcPcPortMode_Type()
)
cfprApFabricEthEstcPcPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcPortMode.setStatus("current")
_CfprApFabricEthEstcPcPrio_Type = CfprApQosPriority
_CfprApFabricEthEstcPcPrio_Object = MibTableColumn
cfprApFabricEthEstcPcPrio = _CfprApFabricEthEstcPcPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 24),
    _CfprApFabricEthEstcPcPrio_Type()
)
cfprApFabricEthEstcPcPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcPrio.setStatus("current")
_CfprApFabricEthEstcPcProtocol_Type = CfprApFabricEthPcProtocol
_CfprApFabricEthEstcPcProtocol_Object = MibTableColumn
cfprApFabricEthEstcPcProtocol = _CfprApFabricEthEstcPcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 25),
    _CfprApFabricEthEstcPcProtocol_Type()
)
cfprApFabricEthEstcPcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcProtocol.setStatus("current")
_CfprApFabricEthEstcPcStateQual_Type = SnmpAdminString
_CfprApFabricEthEstcPcStateQual_Object = MibTableColumn
cfprApFabricEthEstcPcStateQual = _CfprApFabricEthEstcPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 26),
    _CfprApFabricEthEstcPcStateQual_Type()
)
cfprApFabricEthEstcPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcStateQual.setStatus("current")
_CfprApFabricEthEstcPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthEstcPcSwitchId_Object = MibTableColumn
cfprApFabricEthEstcPcSwitchId = _CfprApFabricEthEstcPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 27),
    _CfprApFabricEthEstcPcSwitchId_Type()
)
cfprApFabricEthEstcPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcSwitchId.setStatus("current")
_CfprApFabricEthEstcPcTransport_Type = CfprApFabricEthEstcPcTransport
_CfprApFabricEthEstcPcTransport_Object = MibTableColumn
cfprApFabricEthEstcPcTransport = _CfprApFabricEthEstcPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 28),
    _CfprApFabricEthEstcPcTransport_Type()
)
cfprApFabricEthEstcPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcTransport.setStatus("current")
_CfprApFabricEthEstcPcType_Type = CfprApFabricEstcPcType
_CfprApFabricEthEstcPcType_Object = MibTableColumn
cfprApFabricEthEstcPcType = _CfprApFabricEthEstcPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 29),
    _CfprApFabricEthEstcPcType_Type()
)
cfprApFabricEthEstcPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcType.setStatus("current")
_CfprApFabricEthEstcPcWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthEstcPcWarnings_Object = MibTableColumn
cfprApFabricEthEstcPcWarnings = _CfprApFabricEthEstcPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 23, 1, 30),
    _CfprApFabricEthEstcPcWarnings_Type()
)
cfprApFabricEthEstcPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcWarnings.setStatus("current")
_CfprApFabricEthEstcPcEpTable_Object = MibTable
cfprApFabricEthEstcPcEpTable = _CfprApFabricEthEstcPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24)
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpTable.setStatus("current")
_CfprApFabricEthEstcPcEpEntry_Object = MibTableRow
cfprApFabricEthEstcPcEpEntry = _CfprApFabricEthEstcPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1)
)
cfprApFabricEthEstcPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthEstcPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpEntry.setStatus("current")
_CfprApFabricEthEstcPcEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthEstcPcEpInstanceId_Object = MibTableColumn
cfprApFabricEthEstcPcEpInstanceId = _CfprApFabricEthEstcPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 1),
    _CfprApFabricEthEstcPcEpInstanceId_Type()
)
cfprApFabricEthEstcPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpInstanceId.setStatus("current")
_CfprApFabricEthEstcPcEpDnData_Type = CfprApManagedObjectDn
_CfprApFabricEthEstcPcEpDnData_Object = MibTableColumn
cfprApFabricEthEstcPcEpDnData = _CfprApFabricEthEstcPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 2),
    _CfprApFabricEthEstcPcEpDnData_Type()
)
cfprApFabricEthEstcPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpDnData.setStatus("current")
_CfprApFabricEthEstcPcEpRn_Type = SnmpAdminString
_CfprApFabricEthEstcPcEpRn_Object = MibTableColumn
cfprApFabricEthEstcPcEpRn = _CfprApFabricEthEstcPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 3),
    _CfprApFabricEthEstcPcEpRn_Type()
)
cfprApFabricEthEstcPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpRn.setStatus("current")
_CfprApFabricEthEstcPcEpAdminSpeed_Type = CfprApPortSpeed
_CfprApFabricEthEstcPcEpAdminSpeed_Object = MibTableColumn
cfprApFabricEthEstcPcEpAdminSpeed = _CfprApFabricEthEstcPcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 4),
    _CfprApFabricEthEstcPcEpAdminSpeed_Type()
)
cfprApFabricEthEstcPcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpAdminSpeed.setStatus("current")
_CfprApFabricEthEstcPcEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricEthEstcPcEpAdminState_Object = MibTableColumn
cfprApFabricEthEstcPcEpAdminState = _CfprApFabricEthEstcPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 5),
    _CfprApFabricEthEstcPcEpAdminState_Type()
)
cfprApFabricEthEstcPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpAdminState.setStatus("current")
_CfprApFabricEthEstcPcEpAggrPortId_Type = Gauge32
_CfprApFabricEthEstcPcEpAggrPortId_Object = MibTableColumn
cfprApFabricEthEstcPcEpAggrPortId = _CfprApFabricEthEstcPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 6),
    _CfprApFabricEthEstcPcEpAggrPortId_Type()
)
cfprApFabricEthEstcPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpAggrPortId.setStatus("current")
_CfprApFabricEthEstcPcEpChassisId_Type = Gauge32
_CfprApFabricEthEstcPcEpChassisId_Object = MibTableColumn
cfprApFabricEthEstcPcEpChassisId = _CfprApFabricEthEstcPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 7),
    _CfprApFabricEthEstcPcEpChassisId_Type()
)
cfprApFabricEthEstcPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpChassisId.setStatus("current")
_CfprApFabricEthEstcPcEpConfigState_Type = CfprApFabricConfigState
_CfprApFabricEthEstcPcEpConfigState_Object = MibTableColumn
cfprApFabricEthEstcPcEpConfigState = _CfprApFabricEthEstcPcEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 8),
    _CfprApFabricEthEstcPcEpConfigState_Type()
)
cfprApFabricEthEstcPcEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpConfigState.setStatus("current")
_CfprApFabricEthEstcPcEpEpDn_Type = SnmpAdminString
_CfprApFabricEthEstcPcEpEpDn_Object = MibTableColumn
cfprApFabricEthEstcPcEpEpDn = _CfprApFabricEthEstcPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 9),
    _CfprApFabricEthEstcPcEpEpDn_Type()
)
cfprApFabricEthEstcPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpEpDn.setStatus("current")
_CfprApFabricEthEstcPcEpFltAggr_Type = Unsigned64
_CfprApFabricEthEstcPcEpFltAggr_Object = MibTableColumn
cfprApFabricEthEstcPcEpFltAggr = _CfprApFabricEthEstcPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 10),
    _CfprApFabricEthEstcPcEpFltAggr_Type()
)
cfprApFabricEthEstcPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpFltAggr.setStatus("current")
_CfprApFabricEthEstcPcEpIfRole_Type = CfprApFabricAEthEstcEpIfRole
_CfprApFabricEthEstcPcEpIfRole_Object = MibTableColumn
cfprApFabricEthEstcPcEpIfRole = _CfprApFabricEthEstcPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 11),
    _CfprApFabricEthEstcPcEpIfRole_Type()
)
cfprApFabricEthEstcPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpIfRole.setStatus("current")
_CfprApFabricEthEstcPcEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricEthEstcPcEpIfType_Object = MibTableColumn
cfprApFabricEthEstcPcEpIfType = _CfprApFabricEthEstcPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 12),
    _CfprApFabricEthEstcPcEpIfType_Type()
)
cfprApFabricEthEstcPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpIfType.setStatus("current")
_CfprApFabricEthEstcPcEpLicGP_Type = Unsigned64
_CfprApFabricEthEstcPcEpLicGP_Object = MibTableColumn
cfprApFabricEthEstcPcEpLicGP = _CfprApFabricEthEstcPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 13),
    _CfprApFabricEthEstcPcEpLicGP_Type()
)
cfprApFabricEthEstcPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpLicGP.setStatus("current")
_CfprApFabricEthEstcPcEpLicState_Type = CfprApLicenseState
_CfprApFabricEthEstcPcEpLicState_Object = MibTableColumn
cfprApFabricEthEstcPcEpLicState = _CfprApFabricEthEstcPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 14),
    _CfprApFabricEthEstcPcEpLicState_Type()
)
cfprApFabricEthEstcPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpLicState.setStatus("current")
_CfprApFabricEthEstcPcEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricEthEstcPcEpLocale_Object = MibTableColumn
cfprApFabricEthEstcPcEpLocale = _CfprApFabricEthEstcPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 15),
    _CfprApFabricEthEstcPcEpLocale_Type()
)
cfprApFabricEthEstcPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpLocale.setStatus("current")
_CfprApFabricEthEstcPcEpMembership_Type = CfprApFabricMembershipStatus
_CfprApFabricEthEstcPcEpMembership_Object = MibTableColumn
cfprApFabricEthEstcPcEpMembership = _CfprApFabricEthEstcPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 16),
    _CfprApFabricEthEstcPcEpMembership_Type()
)
cfprApFabricEthEstcPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpMembership.setStatus("current")
_CfprApFabricEthEstcPcEpName_Type = SnmpAdminString
_CfprApFabricEthEstcPcEpName_Object = MibTableColumn
cfprApFabricEthEstcPcEpName = _CfprApFabricEthEstcPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 17),
    _CfprApFabricEthEstcPcEpName_Type()
)
cfprApFabricEthEstcPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpName.setStatus("current")
_CfprApFabricEthEstcPcEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricEthEstcPcEpOperState_Object = MibTableColumn
cfprApFabricEthEstcPcEpOperState = _CfprApFabricEthEstcPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 18),
    _CfprApFabricEthEstcPcEpOperState_Type()
)
cfprApFabricEthEstcPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpOperState.setStatus("current")
_CfprApFabricEthEstcPcEpOperStateReason_Type = SnmpAdminString
_CfprApFabricEthEstcPcEpOperStateReason_Object = MibTableColumn
cfprApFabricEthEstcPcEpOperStateReason = _CfprApFabricEthEstcPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 19),
    _CfprApFabricEthEstcPcEpOperStateReason_Type()
)
cfprApFabricEthEstcPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpOperStateReason.setStatus("current")
_CfprApFabricEthEstcPcEpPeerAggrPortId_Type = Gauge32
_CfprApFabricEthEstcPcEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricEthEstcPcEpPeerAggrPortId = _CfprApFabricEthEstcPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 20),
    _CfprApFabricEthEstcPcEpPeerAggrPortId_Type()
)
cfprApFabricEthEstcPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpPeerAggrPortId.setStatus("current")
_CfprApFabricEthEstcPcEpPeerChassisId_Type = Gauge32
_CfprApFabricEthEstcPcEpPeerChassisId_Object = MibTableColumn
cfprApFabricEthEstcPcEpPeerChassisId = _CfprApFabricEthEstcPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 21),
    _CfprApFabricEthEstcPcEpPeerChassisId_Type()
)
cfprApFabricEthEstcPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpPeerChassisId.setStatus("current")
_CfprApFabricEthEstcPcEpPeerDn_Type = SnmpAdminString
_CfprApFabricEthEstcPcEpPeerDn_Object = MibTableColumn
cfprApFabricEthEstcPcEpPeerDn = _CfprApFabricEthEstcPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 22),
    _CfprApFabricEthEstcPcEpPeerDn_Type()
)
cfprApFabricEthEstcPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpPeerDn.setStatus("current")
_CfprApFabricEthEstcPcEpPeerPortId_Type = Gauge32
_CfprApFabricEthEstcPcEpPeerPortId_Object = MibTableColumn
cfprApFabricEthEstcPcEpPeerPortId = _CfprApFabricEthEstcPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 23),
    _CfprApFabricEthEstcPcEpPeerPortId_Type()
)
cfprApFabricEthEstcPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpPeerPortId.setStatus("current")
_CfprApFabricEthEstcPcEpPeerSlotId_Type = Gauge32
_CfprApFabricEthEstcPcEpPeerSlotId_Object = MibTableColumn
cfprApFabricEthEstcPcEpPeerSlotId = _CfprApFabricEthEstcPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 24),
    _CfprApFabricEthEstcPcEpPeerSlotId_Type()
)
cfprApFabricEthEstcPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpPeerSlotId.setStatus("current")
_CfprApFabricEthEstcPcEpPortId_Type = CfprApFabricEthEstcPcEpPortId
_CfprApFabricEthEstcPcEpPortId_Object = MibTableColumn
cfprApFabricEthEstcPcEpPortId = _CfprApFabricEthEstcPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 25),
    _CfprApFabricEthEstcPcEpPortId_Type()
)
cfprApFabricEthEstcPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpPortId.setStatus("current")
_CfprApFabricEthEstcPcEpSlotId_Type = CfprApFabricEthEstcPcEpSlotId
_CfprApFabricEthEstcPcEpSlotId_Object = MibTableColumn
cfprApFabricEthEstcPcEpSlotId = _CfprApFabricEthEstcPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 26),
    _CfprApFabricEthEstcPcEpSlotId_Type()
)
cfprApFabricEthEstcPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpSlotId.setStatus("current")
_CfprApFabricEthEstcPcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthEstcPcEpSwitchId_Object = MibTableColumn
cfprApFabricEthEstcPcEpSwitchId = _CfprApFabricEthEstcPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 27),
    _CfprApFabricEthEstcPcEpSwitchId_Type()
)
cfprApFabricEthEstcPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpSwitchId.setStatus("current")
_CfprApFabricEthEstcPcEpTransport_Type = CfprApFabricAEthEstcEpTransport
_CfprApFabricEthEstcPcEpTransport_Object = MibTableColumn
cfprApFabricEthEstcPcEpTransport = _CfprApFabricEthEstcPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 28),
    _CfprApFabricEthEstcPcEpTransport_Type()
)
cfprApFabricEthEstcPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpTransport.setStatus("current")
_CfprApFabricEthEstcPcEpType_Type = CfprApFabricAEthEstcEpType
_CfprApFabricEthEstcPcEpType_Object = MibTableColumn
cfprApFabricEthEstcPcEpType = _CfprApFabricEthEstcPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 29),
    _CfprApFabricEthEstcPcEpType_Type()
)
cfprApFabricEthEstcPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpType.setStatus("current")
_CfprApFabricEthEstcPcEpUsrLbl_Type = SnmpAdminString
_CfprApFabricEthEstcPcEpUsrLbl_Object = MibTableColumn
cfprApFabricEthEstcPcEpUsrLbl = _CfprApFabricEthEstcPcEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 30),
    _CfprApFabricEthEstcPcEpUsrLbl_Type()
)
cfprApFabricEthEstcPcEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpUsrLbl.setStatus("current")
_CfprApFabricEthEstcPcEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthEstcPcEpWarnings_Object = MibTableColumn
cfprApFabricEthEstcPcEpWarnings = _CfprApFabricEthEstcPcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 24, 1, 31),
    _CfprApFabricEthEstcPcEpWarnings_Type()
)
cfprApFabricEthEstcPcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthEstcPcEpWarnings.setStatus("current")
_CfprApFabricEthLanTable_Object = MibTable
cfprApFabricEthLanTable = _CfprApFabricEthLanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26)
)
if mibBuilder.loadTexts:
    cfprApFabricEthLanTable.setStatus("current")
_CfprApFabricEthLanEntry_Object = MibTableRow
cfprApFabricEthLanEntry = _CfprApFabricEthLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1)
)
cfprApFabricEthLanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthLanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthLanEntry.setStatus("current")
_CfprApFabricEthLanInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthLanInstanceId_Object = MibTableColumn
cfprApFabricEthLanInstanceId = _CfprApFabricEthLanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1, 1),
    _CfprApFabricEthLanInstanceId_Type()
)
cfprApFabricEthLanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthLanInstanceId.setStatus("current")
_CfprApFabricEthLanDn_Type = CfprApManagedObjectDn
_CfprApFabricEthLanDn_Object = MibTableColumn
cfprApFabricEthLanDn = _CfprApFabricEthLanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1, 2),
    _CfprApFabricEthLanDn_Type()
)
cfprApFabricEthLanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanDn.setStatus("current")
_CfprApFabricEthLanRn_Type = SnmpAdminString
_CfprApFabricEthLanRn_Object = MibTableColumn
cfprApFabricEthLanRn = _CfprApFabricEthLanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1, 3),
    _CfprApFabricEthLanRn_Type()
)
cfprApFabricEthLanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanRn.setStatus("current")
_CfprApFabricEthLanId_Type = CfprApNetworkSwitchId
_CfprApFabricEthLanId_Object = MibTableColumn
cfprApFabricEthLanId = _CfprApFabricEthLanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1, 4),
    _CfprApFabricEthLanId_Type()
)
cfprApFabricEthLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanId.setStatus("current")
_CfprApFabricEthLanLocale_Type = CfprApFabricExternalLocale
_CfprApFabricEthLanLocale_Object = MibTableColumn
cfprApFabricEthLanLocale = _CfprApFabricEthLanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1, 5),
    _CfprApFabricEthLanLocale_Type()
)
cfprApFabricEthLanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanLocale.setStatus("current")
_CfprApFabricEthLanName_Type = SnmpAdminString
_CfprApFabricEthLanName_Object = MibTableColumn
cfprApFabricEthLanName = _CfprApFabricEthLanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1, 6),
    _CfprApFabricEthLanName_Type()
)
cfprApFabricEthLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanName.setStatus("current")
_CfprApFabricEthLanTransport_Type = CfprApFabricEthLanTransport
_CfprApFabricEthLanTransport_Object = MibTableColumn
cfprApFabricEthLanTransport = _CfprApFabricEthLanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1, 7),
    _CfprApFabricEthLanTransport_Type()
)
cfprApFabricEthLanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanTransport.setStatus("current")
_CfprApFabricEthLanType_Type = CfprApFabricLanType
_CfprApFabricEthLanType_Object = MibTableColumn
cfprApFabricEthLanType = _CfprApFabricEthLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 26, 1, 8),
    _CfprApFabricEthLanType_Type()
)
cfprApFabricEthLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanType.setStatus("current")
_CfprApFabricEthLanEpTable_Object = MibTable
cfprApFabricEthLanEpTable = _CfprApFabricEthLanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27)
)
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpTable.setStatus("current")
_CfprApFabricEthLanEpEntry_Object = MibTableRow
cfprApFabricEthLanEpEntry = _CfprApFabricEthLanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1)
)
cfprApFabricEthLanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthLanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpEntry.setStatus("current")
_CfprApFabricEthLanEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthLanEpInstanceId_Object = MibTableColumn
cfprApFabricEthLanEpInstanceId = _CfprApFabricEthLanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 1),
    _CfprApFabricEthLanEpInstanceId_Type()
)
cfprApFabricEthLanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpInstanceId.setStatus("current")
_CfprApFabricEthLanEpDn_Type = CfprApManagedObjectDn
_CfprApFabricEthLanEpDn_Object = MibTableColumn
cfprApFabricEthLanEpDn = _CfprApFabricEthLanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 2),
    _CfprApFabricEthLanEpDn_Type()
)
cfprApFabricEthLanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpDn.setStatus("current")
_CfprApFabricEthLanEpRn_Type = SnmpAdminString
_CfprApFabricEthLanEpRn_Object = MibTableColumn
cfprApFabricEthLanEpRn = _CfprApFabricEthLanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 3),
    _CfprApFabricEthLanEpRn_Type()
)
cfprApFabricEthLanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpRn.setStatus("current")
_CfprApFabricEthLanEpAdminDuplex_Type = CfprApPortDuplex
_CfprApFabricEthLanEpAdminDuplex_Object = MibTableColumn
cfprApFabricEthLanEpAdminDuplex = _CfprApFabricEthLanEpAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 4),
    _CfprApFabricEthLanEpAdminDuplex_Type()
)
cfprApFabricEthLanEpAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpAdminDuplex.setStatus("current")
_CfprApFabricEthLanEpAdminSpeed_Type = CfprApPortEthSpeed
_CfprApFabricEthLanEpAdminSpeed_Object = MibTableColumn
cfprApFabricEthLanEpAdminSpeed = _CfprApFabricEthLanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 5),
    _CfprApFabricEthLanEpAdminSpeed_Type()
)
cfprApFabricEthLanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpAdminSpeed.setStatus("current")
_CfprApFabricEthLanEpAdminState_Type = CfprApFabricEthLanEpAdminState
_CfprApFabricEthLanEpAdminState_Object = MibTableColumn
cfprApFabricEthLanEpAdminState = _CfprApFabricEthLanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 6),
    _CfprApFabricEthLanEpAdminState_Type()
)
cfprApFabricEthLanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpAdminState.setStatus("current")
_CfprApFabricEthLanEpAggrPortId_Type = Gauge32
_CfprApFabricEthLanEpAggrPortId_Object = MibTableColumn
cfprApFabricEthLanEpAggrPortId = _CfprApFabricEthLanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 7),
    _CfprApFabricEthLanEpAggrPortId_Type()
)
cfprApFabricEthLanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpAggrPortId.setStatus("current")
_CfprApFabricEthLanEpAutoNeg_Type = TruthValue
_CfprApFabricEthLanEpAutoNeg_Object = MibTableColumn
cfprApFabricEthLanEpAutoNeg = _CfprApFabricEthLanEpAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 8),
    _CfprApFabricEthLanEpAutoNeg_Type()
)
cfprApFabricEthLanEpAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpAutoNeg.setStatus("current")
_CfprApFabricEthLanEpChassisId_Type = Gauge32
_CfprApFabricEthLanEpChassisId_Object = MibTableColumn
cfprApFabricEthLanEpChassisId = _CfprApFabricEthLanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 9),
    _CfprApFabricEthLanEpChassisId_Type()
)
cfprApFabricEthLanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpChassisId.setStatus("current")
_CfprApFabricEthLanEpDtagVlan_Type = Gauge32
_CfprApFabricEthLanEpDtagVlan_Object = MibTableColumn
cfprApFabricEthLanEpDtagVlan = _CfprApFabricEthLanEpDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 10),
    _CfprApFabricEthLanEpDtagVlan_Type()
)
cfprApFabricEthLanEpDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpDtagVlan.setStatus("current")
_CfprApFabricEthLanEpEpDn_Type = SnmpAdminString
_CfprApFabricEthLanEpEpDn_Object = MibTableColumn
cfprApFabricEthLanEpEpDn = _CfprApFabricEthLanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 11),
    _CfprApFabricEthLanEpEpDn_Type()
)
cfprApFabricEthLanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpEpDn.setStatus("current")
_CfprApFabricEthLanEpEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricEthLanEpEthLinkProfileName_Object = MibTableColumn
cfprApFabricEthLanEpEthLinkProfileName = _CfprApFabricEthLanEpEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 12),
    _CfprApFabricEthLanEpEthLinkProfileName_Type()
)
cfprApFabricEthLanEpEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpEthLinkProfileName.setStatus("current")
_CfprApFabricEthLanEpFlowCtrlPolicy_Type = SnmpAdminString
_CfprApFabricEthLanEpFlowCtrlPolicy_Object = MibTableColumn
cfprApFabricEthLanEpFlowCtrlPolicy = _CfprApFabricEthLanEpFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 13),
    _CfprApFabricEthLanEpFlowCtrlPolicy_Type()
)
cfprApFabricEthLanEpFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpFlowCtrlPolicy.setStatus("current")
_CfprApFabricEthLanEpFltAggr_Type = Unsigned64
_CfprApFabricEthLanEpFltAggr_Object = MibTableColumn
cfprApFabricEthLanEpFltAggr = _CfprApFabricEthLanEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 14),
    _CfprApFabricEthLanEpFltAggr_Type()
)
cfprApFabricEthLanEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpFltAggr.setStatus("current")
_CfprApFabricEthLanEpHashAlg_Type = CfprApNhTpHashType
_CfprApFabricEthLanEpHashAlg_Object = MibTableColumn
cfprApFabricEthLanEpHashAlg = _CfprApFabricEthLanEpHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 15),
    _CfprApFabricEthLanEpHashAlg_Type()
)
cfprApFabricEthLanEpHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpHashAlg.setStatus("current")
_CfprApFabricEthLanEpIfRole_Type = CfprApFabricLanEpIfRole
_CfprApFabricEthLanEpIfRole_Object = MibTableColumn
cfprApFabricEthLanEpIfRole = _CfprApFabricEthLanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 16),
    _CfprApFabricEthLanEpIfRole_Type()
)
cfprApFabricEthLanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpIfRole.setStatus("current")
_CfprApFabricEthLanEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricEthLanEpIfType_Object = MibTableColumn
cfprApFabricEthLanEpIfType = _CfprApFabricEthLanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 17),
    _CfprApFabricEthLanEpIfType_Type()
)
cfprApFabricEthLanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpIfType.setStatus("current")
_CfprApFabricEthLanEpLicGP_Type = Unsigned64
_CfprApFabricEthLanEpLicGP_Object = MibTableColumn
cfprApFabricEthLanEpLicGP = _CfprApFabricEthLanEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 18),
    _CfprApFabricEthLanEpLicGP_Type()
)
cfprApFabricEthLanEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpLicGP.setStatus("current")
_CfprApFabricEthLanEpLicState_Type = CfprApLicenseState
_CfprApFabricEthLanEpLicState_Object = MibTableColumn
cfprApFabricEthLanEpLicState = _CfprApFabricEthLanEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 19),
    _CfprApFabricEthLanEpLicState_Type()
)
cfprApFabricEthLanEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpLicState.setStatus("current")
_CfprApFabricEthLanEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricEthLanEpLocale_Object = MibTableColumn
cfprApFabricEthLanEpLocale = _CfprApFabricEthLanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 20),
    _CfprApFabricEthLanEpLocale_Type()
)
cfprApFabricEthLanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpLocale.setStatus("current")
_CfprApFabricEthLanEpName_Type = SnmpAdminString
_CfprApFabricEthLanEpName_Object = MibTableColumn
cfprApFabricEthLanEpName = _CfprApFabricEthLanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 21),
    _CfprApFabricEthLanEpName_Type()
)
cfprApFabricEthLanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpName.setStatus("current")
_CfprApFabricEthLanEpOperEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricEthLanEpOperEthLinkProfileName_Object = MibTableColumn
cfprApFabricEthLanEpOperEthLinkProfileName = _CfprApFabricEthLanEpOperEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 22),
    _CfprApFabricEthLanEpOperEthLinkProfileName_Type()
)
cfprApFabricEthLanEpOperEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpOperEthLinkProfileName.setStatus("current")
_CfprApFabricEthLanEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricEthLanEpOperState_Object = MibTableColumn
cfprApFabricEthLanEpOperState = _CfprApFabricEthLanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 23),
    _CfprApFabricEthLanEpOperState_Type()
)
cfprApFabricEthLanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpOperState.setStatus("current")
_CfprApFabricEthLanEpOperStateReason_Type = SnmpAdminString
_CfprApFabricEthLanEpOperStateReason_Object = MibTableColumn
cfprApFabricEthLanEpOperStateReason = _CfprApFabricEthLanEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 24),
    _CfprApFabricEthLanEpOperStateReason_Type()
)
cfprApFabricEthLanEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpOperStateReason.setStatus("current")
_CfprApFabricEthLanEpOverlappingVlans_Type = SnmpAdminString
_CfprApFabricEthLanEpOverlappingVlans_Object = MibTableColumn
cfprApFabricEthLanEpOverlappingVlans = _CfprApFabricEthLanEpOverlappingVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 25),
    _CfprApFabricEthLanEpOverlappingVlans_Type()
)
cfprApFabricEthLanEpOverlappingVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpOverlappingVlans.setStatus("current")
_CfprApFabricEthLanEpPeerAggrPortId_Type = Gauge32
_CfprApFabricEthLanEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricEthLanEpPeerAggrPortId = _CfprApFabricEthLanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 26),
    _CfprApFabricEthLanEpPeerAggrPortId_Type()
)
cfprApFabricEthLanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpPeerAggrPortId.setStatus("current")
_CfprApFabricEthLanEpPeerChassisId_Type = Gauge32
_CfprApFabricEthLanEpPeerChassisId_Object = MibTableColumn
cfprApFabricEthLanEpPeerChassisId = _CfprApFabricEthLanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 27),
    _CfprApFabricEthLanEpPeerChassisId_Type()
)
cfprApFabricEthLanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpPeerChassisId.setStatus("current")
_CfprApFabricEthLanEpPeerDn_Type = SnmpAdminString
_CfprApFabricEthLanEpPeerDn_Object = MibTableColumn
cfprApFabricEthLanEpPeerDn = _CfprApFabricEthLanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 28),
    _CfprApFabricEthLanEpPeerDn_Type()
)
cfprApFabricEthLanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpPeerDn.setStatus("current")
_CfprApFabricEthLanEpPeerPortId_Type = Gauge32
_CfprApFabricEthLanEpPeerPortId_Object = MibTableColumn
cfprApFabricEthLanEpPeerPortId = _CfprApFabricEthLanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 29),
    _CfprApFabricEthLanEpPeerPortId_Type()
)
cfprApFabricEthLanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpPeerPortId.setStatus("current")
_CfprApFabricEthLanEpPeerSlotId_Type = Gauge32
_CfprApFabricEthLanEpPeerSlotId_Object = MibTableColumn
cfprApFabricEthLanEpPeerSlotId = _CfprApFabricEthLanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 30),
    _CfprApFabricEthLanEpPeerSlotId_Type()
)
cfprApFabricEthLanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpPeerSlotId.setStatus("current")
_CfprApFabricEthLanEpPortId_Type = Gauge32
_CfprApFabricEthLanEpPortId_Object = MibTableColumn
cfprApFabricEthLanEpPortId = _CfprApFabricEthLanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 31),
    _CfprApFabricEthLanEpPortId_Type()
)
cfprApFabricEthLanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpPortId.setStatus("current")
_CfprApFabricEthLanEpQosPrio_Type = CfprApFabricQosPrio
_CfprApFabricEthLanEpQosPrio_Object = MibTableColumn
cfprApFabricEthLanEpQosPrio = _CfprApFabricEthLanEpQosPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 32),
    _CfprApFabricEthLanEpQosPrio_Type()
)
cfprApFabricEthLanEpQosPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpQosPrio.setStatus("current")
_CfprApFabricEthLanEpSlotId_Type = Gauge32
_CfprApFabricEthLanEpSlotId_Object = MibTableColumn
cfprApFabricEthLanEpSlotId = _CfprApFabricEthLanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 33),
    _CfprApFabricEthLanEpSlotId_Type()
)
cfprApFabricEthLanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpSlotId.setStatus("current")
_CfprApFabricEthLanEpSpeedCap_Type = CfprApFabricEthLanEpSpeedCap
_CfprApFabricEthLanEpSpeedCap_Object = MibTableColumn
cfprApFabricEthLanEpSpeedCap = _CfprApFabricEthLanEpSpeedCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 34),
    _CfprApFabricEthLanEpSpeedCap_Type()
)
cfprApFabricEthLanEpSpeedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpSpeedCap.setStatus("current")
_CfprApFabricEthLanEpSsaPortType_Type = CfprApFabricSSAPortType
_CfprApFabricEthLanEpSsaPortType_Object = MibTableColumn
cfprApFabricEthLanEpSsaPortType = _CfprApFabricEthLanEpSsaPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 35),
    _CfprApFabricEthLanEpSsaPortType_Type()
)
cfprApFabricEthLanEpSsaPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpSsaPortType.setStatus("current")
_CfprApFabricEthLanEpSsaVlanId_Type = Gauge32
_CfprApFabricEthLanEpSsaVlanId_Object = MibTableColumn
cfprApFabricEthLanEpSsaVlanId = _CfprApFabricEthLanEpSsaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 36),
    _CfprApFabricEthLanEpSsaVlanId_Type()
)
cfprApFabricEthLanEpSsaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpSsaVlanId.setStatus("current")
_CfprApFabricEthLanEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthLanEpSwitchId_Object = MibTableColumn
cfprApFabricEthLanEpSwitchId = _CfprApFabricEthLanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 37),
    _CfprApFabricEthLanEpSwitchId_Type()
)
cfprApFabricEthLanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpSwitchId.setStatus("current")
_CfprApFabricEthLanEpTransport_Type = CfprApFabricAEthLanEpTransport
_CfprApFabricEthLanEpTransport_Object = MibTableColumn
cfprApFabricEthLanEpTransport = _CfprApFabricEthLanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 38),
    _CfprApFabricEthLanEpTransport_Type()
)
cfprApFabricEthLanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpTransport.setStatus("current")
_CfprApFabricEthLanEpType_Type = CfprApFabricLanEpType
_CfprApFabricEthLanEpType_Object = MibTableColumn
cfprApFabricEthLanEpType = _CfprApFabricEthLanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 39),
    _CfprApFabricEthLanEpType_Type()
)
cfprApFabricEthLanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpType.setStatus("current")
_CfprApFabricEthLanEpUdldOperState_Type = CfprApFabricUdldOperState
_CfprApFabricEthLanEpUdldOperState_Object = MibTableColumn
cfprApFabricEthLanEpUdldOperState = _CfprApFabricEthLanEpUdldOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 40),
    _CfprApFabricEthLanEpUdldOperState_Type()
)
cfprApFabricEthLanEpUdldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpUdldOperState.setStatus("current")
_CfprApFabricEthLanEpUsrLbl_Type = SnmpAdminString
_CfprApFabricEthLanEpUsrLbl_Object = MibTableColumn
cfprApFabricEthLanEpUsrLbl = _CfprApFabricEthLanEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 41),
    _CfprApFabricEthLanEpUsrLbl_Type()
)
cfprApFabricEthLanEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpUsrLbl.setStatus("current")
_CfprApFabricEthLanEpVlanStatus_Type = CfprApFabricEthLanEpVlanStatus
_CfprApFabricEthLanEpVlanStatus_Object = MibTableColumn
cfprApFabricEthLanEpVlanStatus = _CfprApFabricEthLanEpVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 42),
    _CfprApFabricEthLanEpVlanStatus_Type()
)
cfprApFabricEthLanEpVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpVlanStatus.setStatus("current")
_CfprApFabricEthLanEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthLanEpWarnings_Object = MibTableColumn
cfprApFabricEthLanEpWarnings = _CfprApFabricEthLanEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 27, 1, 43),
    _CfprApFabricEthLanEpWarnings_Type()
)
cfprApFabricEthLanEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanEpWarnings.setStatus("current")
_CfprApFabricEthLanPcTable_Object = MibTable
cfprApFabricEthLanPcTable = _CfprApFabricEthLanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29)
)
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcTable.setStatus("current")
_CfprApFabricEthLanPcEntry_Object = MibTableRow
cfprApFabricEthLanPcEntry = _CfprApFabricEthLanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1)
)
cfprApFabricEthLanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthLanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEntry.setStatus("current")
_CfprApFabricEthLanPcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthLanPcInstanceId_Object = MibTableColumn
cfprApFabricEthLanPcInstanceId = _CfprApFabricEthLanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 1),
    _CfprApFabricEthLanPcInstanceId_Type()
)
cfprApFabricEthLanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcInstanceId.setStatus("current")
_CfprApFabricEthLanPcDn_Type = CfprApManagedObjectDn
_CfprApFabricEthLanPcDn_Object = MibTableColumn
cfprApFabricEthLanPcDn = _CfprApFabricEthLanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 2),
    _CfprApFabricEthLanPcDn_Type()
)
cfprApFabricEthLanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcDn.setStatus("current")
_CfprApFabricEthLanPcRn_Type = SnmpAdminString
_CfprApFabricEthLanPcRn_Object = MibTableColumn
cfprApFabricEthLanPcRn = _CfprApFabricEthLanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 3),
    _CfprApFabricEthLanPcRn_Type()
)
cfprApFabricEthLanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcRn.setStatus("current")
_CfprApFabricEthLanPcAdminDuplex_Type = CfprApPortDuplex
_CfprApFabricEthLanPcAdminDuplex_Object = MibTableColumn
cfprApFabricEthLanPcAdminDuplex = _CfprApFabricEthLanPcAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 4),
    _CfprApFabricEthLanPcAdminDuplex_Type()
)
cfprApFabricEthLanPcAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcAdminDuplex.setStatus("current")
_CfprApFabricEthLanPcAdminSpeed_Type = CfprApPortEthSpeed
_CfprApFabricEthLanPcAdminSpeed_Object = MibTableColumn
cfprApFabricEthLanPcAdminSpeed = _CfprApFabricEthLanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 5),
    _CfprApFabricEthLanPcAdminSpeed_Type()
)
cfprApFabricEthLanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcAdminSpeed.setStatus("current")
_CfprApFabricEthLanPcAdminState_Type = CfprApFabricEthLanPcAdminState
_CfprApFabricEthLanPcAdminState_Object = MibTableColumn
cfprApFabricEthLanPcAdminState = _CfprApFabricEthLanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 6),
    _CfprApFabricEthLanPcAdminState_Type()
)
cfprApFabricEthLanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcAdminState.setStatus("current")
_CfprApFabricEthLanPcAutoNeg_Type = TruthValue
_CfprApFabricEthLanPcAutoNeg_Object = MibTableColumn
cfprApFabricEthLanPcAutoNeg = _CfprApFabricEthLanPcAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 7),
    _CfprApFabricEthLanPcAutoNeg_Type()
)
cfprApFabricEthLanPcAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcAutoNeg.setStatus("current")
_CfprApFabricEthLanPcBandwidth_Type = Gauge32
_CfprApFabricEthLanPcBandwidth_Object = MibTableColumn
cfprApFabricEthLanPcBandwidth = _CfprApFabricEthLanPcBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 8),
    _CfprApFabricEthLanPcBandwidth_Type()
)
cfprApFabricEthLanPcBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcBandwidth.setStatus("current")
_CfprApFabricEthLanPcCluChassisId_Type = Gauge32
_CfprApFabricEthLanPcCluChassisId_Object = MibTableColumn
cfprApFabricEthLanPcCluChassisId = _CfprApFabricEthLanPcCluChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 9),
    _CfprApFabricEthLanPcCluChassisId_Type()
)
cfprApFabricEthLanPcCluChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcCluChassisId.setStatus("current")
_CfprApFabricEthLanPcClusterName_Type = SnmpAdminString
_CfprApFabricEthLanPcClusterName_Object = MibTableColumn
cfprApFabricEthLanPcClusterName = _CfprApFabricEthLanPcClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 10),
    _CfprApFabricEthLanPcClusterName_Type()
)
cfprApFabricEthLanPcClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcClusterName.setStatus("current")
_CfprApFabricEthLanPcDescr_Type = SnmpAdminString
_CfprApFabricEthLanPcDescr_Object = MibTableColumn
cfprApFabricEthLanPcDescr = _CfprApFabricEthLanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 11),
    _CfprApFabricEthLanPcDescr_Type()
)
cfprApFabricEthLanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcDescr.setStatus("current")
_CfprApFabricEthLanPcDtagVlan_Type = Gauge32
_CfprApFabricEthLanPcDtagVlan_Object = MibTableColumn
cfprApFabricEthLanPcDtagVlan = _CfprApFabricEthLanPcDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 12),
    _CfprApFabricEthLanPcDtagVlan_Type()
)
cfprApFabricEthLanPcDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcDtagVlan.setStatus("current")
_CfprApFabricEthLanPcEpDn_Type = SnmpAdminString
_CfprApFabricEthLanPcEpDn_Object = MibTableColumn
cfprApFabricEthLanPcEpDn = _CfprApFabricEthLanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 13),
    _CfprApFabricEthLanPcEpDn_Type()
)
cfprApFabricEthLanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpDn.setStatus("current")
_CfprApFabricEthLanPcFlowCtrlPolicy_Type = SnmpAdminString
_CfprApFabricEthLanPcFlowCtrlPolicy_Object = MibTableColumn
cfprApFabricEthLanPcFlowCtrlPolicy = _CfprApFabricEthLanPcFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 14),
    _CfprApFabricEthLanPcFlowCtrlPolicy_Type()
)
cfprApFabricEthLanPcFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcFlowCtrlPolicy.setStatus("current")
_CfprApFabricEthLanPcFltAggr_Type = Unsigned64
_CfprApFabricEthLanPcFltAggr_Object = MibTableColumn
cfprApFabricEthLanPcFltAggr = _CfprApFabricEthLanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 15),
    _CfprApFabricEthLanPcFltAggr_Type()
)
cfprApFabricEthLanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcFltAggr.setStatus("current")
_CfprApFabricEthLanPcHashAlg_Type = CfprApNhTpHashType
_CfprApFabricEthLanPcHashAlg_Object = MibTableColumn
cfprApFabricEthLanPcHashAlg = _CfprApFabricEthLanPcHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 16),
    _CfprApFabricEthLanPcHashAlg_Type()
)
cfprApFabricEthLanPcHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcHashAlg.setStatus("current")
_CfprApFabricEthLanPcIfRole_Type = CfprApFabricLanPcIfRole
_CfprApFabricEthLanPcIfRole_Object = MibTableColumn
cfprApFabricEthLanPcIfRole = _CfprApFabricEthLanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 17),
    _CfprApFabricEthLanPcIfRole_Type()
)
cfprApFabricEthLanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcIfRole.setStatus("current")
_CfprApFabricEthLanPcIfType_Type = CfprApFabricCIoEpIfType
_CfprApFabricEthLanPcIfType_Object = MibTableColumn
cfprApFabricEthLanPcIfType = _CfprApFabricEthLanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 18),
    _CfprApFabricEthLanPcIfType_Type()
)
cfprApFabricEthLanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcIfType.setStatus("current")
_CfprApFabricEthLanPcLacpDetach_Type = CfprApFabricEthLanPcLacpDetach
_CfprApFabricEthLanPcLacpDetach_Object = MibTableColumn
cfprApFabricEthLanPcLacpDetach = _CfprApFabricEthLanPcLacpDetach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 19),
    _CfprApFabricEthLanPcLacpDetach_Type()
)
cfprApFabricEthLanPcLacpDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcLacpDetach.setStatus("current")
_CfprApFabricEthLanPcLacpMode_Type = CfprApFabricLacpMode
_CfprApFabricEthLanPcLacpMode_Object = MibTableColumn
cfprApFabricEthLanPcLacpMode = _CfprApFabricEthLanPcLacpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 20),
    _CfprApFabricEthLanPcLacpMode_Type()
)
cfprApFabricEthLanPcLacpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcLacpMode.setStatus("current")
_CfprApFabricEthLanPcLacpPolicyName_Type = SnmpAdminString
_CfprApFabricEthLanPcLacpPolicyName_Object = MibTableColumn
cfprApFabricEthLanPcLacpPolicyName = _CfprApFabricEthLanPcLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 21),
    _CfprApFabricEthLanPcLacpPolicyName_Type()
)
cfprApFabricEthLanPcLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcLacpPolicyName.setStatus("current")
_CfprApFabricEthLanPcLocale_Type = CfprApFabricExternalPcLocale
_CfprApFabricEthLanPcLocale_Object = MibTableColumn
cfprApFabricEthLanPcLocale = _CfprApFabricEthLanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 22),
    _CfprApFabricEthLanPcLocale_Type()
)
cfprApFabricEthLanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcLocale.setStatus("current")
_CfprApFabricEthLanPcName_Type = SnmpAdminString
_CfprApFabricEthLanPcName_Object = MibTableColumn
cfprApFabricEthLanPcName = _CfprApFabricEthLanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 23),
    _CfprApFabricEthLanPcName_Type()
)
cfprApFabricEthLanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcName.setStatus("current")
_CfprApFabricEthLanPcOperLacpPolicyName_Type = SnmpAdminString
_CfprApFabricEthLanPcOperLacpPolicyName_Object = MibTableColumn
cfprApFabricEthLanPcOperLacpPolicyName = _CfprApFabricEthLanPcOperLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 24),
    _CfprApFabricEthLanPcOperLacpPolicyName_Type()
)
cfprApFabricEthLanPcOperLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcOperLacpPolicyName.setStatus("current")
_CfprApFabricEthLanPcOperSpeed_Type = CfprApPortEthSpeed
_CfprApFabricEthLanPcOperSpeed_Object = MibTableColumn
cfprApFabricEthLanPcOperSpeed = _CfprApFabricEthLanPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 25),
    _CfprApFabricEthLanPcOperSpeed_Type()
)
cfprApFabricEthLanPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcOperSpeed.setStatus("current")
_CfprApFabricEthLanPcOperState_Type = CfprApNetworkPortOperState
_CfprApFabricEthLanPcOperState_Object = MibTableColumn
cfprApFabricEthLanPcOperState = _CfprApFabricEthLanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 26),
    _CfprApFabricEthLanPcOperState_Type()
)
cfprApFabricEthLanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcOperState.setStatus("current")
_CfprApFabricEthLanPcOverlappingVlans_Type = SnmpAdminString
_CfprApFabricEthLanPcOverlappingVlans_Object = MibTableColumn
cfprApFabricEthLanPcOverlappingVlans = _CfprApFabricEthLanPcOverlappingVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 27),
    _CfprApFabricEthLanPcOverlappingVlans_Type()
)
cfprApFabricEthLanPcOverlappingVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcOverlappingVlans.setStatus("current")
_CfprApFabricEthLanPcPeerDn_Type = SnmpAdminString
_CfprApFabricEthLanPcPeerDn_Object = MibTableColumn
cfprApFabricEthLanPcPeerDn = _CfprApFabricEthLanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 28),
    _CfprApFabricEthLanPcPeerDn_Type()
)
cfprApFabricEthLanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcPeerDn.setStatus("current")
_CfprApFabricEthLanPcPortId_Type = Gauge32
_CfprApFabricEthLanPcPortId_Object = MibTableColumn
cfprApFabricEthLanPcPortId = _CfprApFabricEthLanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 29),
    _CfprApFabricEthLanPcPortId_Type()
)
cfprApFabricEthLanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcPortId.setStatus("current")
_CfprApFabricEthLanPcQosPrio_Type = CfprApFabricQosPrio
_CfprApFabricEthLanPcQosPrio_Object = MibTableColumn
cfprApFabricEthLanPcQosPrio = _CfprApFabricEthLanPcQosPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 30),
    _CfprApFabricEthLanPcQosPrio_Type()
)
cfprApFabricEthLanPcQosPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcQosPrio.setStatus("current")
_CfprApFabricEthLanPcSpannedCluster_Type = CfprApFabricSpannedCluster
_CfprApFabricEthLanPcSpannedCluster_Object = MibTableColumn
cfprApFabricEthLanPcSpannedCluster = _CfprApFabricEthLanPcSpannedCluster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 31),
    _CfprApFabricEthLanPcSpannedCluster_Type()
)
cfprApFabricEthLanPcSpannedCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcSpannedCluster.setStatus("current")
_CfprApFabricEthLanPcSpeedCap_Type = CfprApFabricEthLanPcSpeedCap
_CfprApFabricEthLanPcSpeedCap_Object = MibTableColumn
cfprApFabricEthLanPcSpeedCap = _CfprApFabricEthLanPcSpeedCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 32),
    _CfprApFabricEthLanPcSpeedCap_Type()
)
cfprApFabricEthLanPcSpeedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcSpeedCap.setStatus("current")
_CfprApFabricEthLanPcSsaPortType_Type = CfprApFabricSSAPortType
_CfprApFabricEthLanPcSsaPortType_Object = MibTableColumn
cfprApFabricEthLanPcSsaPortType = _CfprApFabricEthLanPcSsaPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 33),
    _CfprApFabricEthLanPcSsaPortType_Type()
)
cfprApFabricEthLanPcSsaPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcSsaPortType.setStatus("current")
_CfprApFabricEthLanPcSsaVlanId_Type = Gauge32
_CfprApFabricEthLanPcSsaVlanId_Object = MibTableColumn
cfprApFabricEthLanPcSsaVlanId = _CfprApFabricEthLanPcSsaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 34),
    _CfprApFabricEthLanPcSsaVlanId_Type()
)
cfprApFabricEthLanPcSsaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcSsaVlanId.setStatus("current")
_CfprApFabricEthLanPcStateQual_Type = SnmpAdminString
_CfprApFabricEthLanPcStateQual_Object = MibTableColumn
cfprApFabricEthLanPcStateQual = _CfprApFabricEthLanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 35),
    _CfprApFabricEthLanPcStateQual_Type()
)
cfprApFabricEthLanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcStateQual.setStatus("current")
_CfprApFabricEthLanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthLanPcSwitchId_Object = MibTableColumn
cfprApFabricEthLanPcSwitchId = _CfprApFabricEthLanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 36),
    _CfprApFabricEthLanPcSwitchId_Type()
)
cfprApFabricEthLanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcSwitchId.setStatus("current")
_CfprApFabricEthLanPcTransport_Type = CfprApFabricEthLanPcTransport
_CfprApFabricEthLanPcTransport_Object = MibTableColumn
cfprApFabricEthLanPcTransport = _CfprApFabricEthLanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 37),
    _CfprApFabricEthLanPcTransport_Type()
)
cfprApFabricEthLanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcTransport.setStatus("current")
_CfprApFabricEthLanPcType_Type = CfprApFabricLanPcType
_CfprApFabricEthLanPcType_Object = MibTableColumn
cfprApFabricEthLanPcType = _CfprApFabricEthLanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 38),
    _CfprApFabricEthLanPcType_Type()
)
cfprApFabricEthLanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcType.setStatus("current")
_CfprApFabricEthLanPcVlanStatus_Type = CfprApFabricEthLanPcVlanStatus
_CfprApFabricEthLanPcVlanStatus_Object = MibTableColumn
cfprApFabricEthLanPcVlanStatus = _CfprApFabricEthLanPcVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 39),
    _CfprApFabricEthLanPcVlanStatus_Type()
)
cfprApFabricEthLanPcVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcVlanStatus.setStatus("current")
_CfprApFabricEthLanPcWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthLanPcWarnings_Object = MibTableColumn
cfprApFabricEthLanPcWarnings = _CfprApFabricEthLanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 29, 1, 40),
    _CfprApFabricEthLanPcWarnings_Type()
)
cfprApFabricEthLanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcWarnings.setStatus("current")
_CfprApFabricEthLanPcEpTable_Object = MibTable
cfprApFabricEthLanPcEpTable = _CfprApFabricEthLanPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30)
)
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpTable.setStatus("current")
_CfprApFabricEthLanPcEpEntry_Object = MibTableRow
cfprApFabricEthLanPcEpEntry = _CfprApFabricEthLanPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1)
)
cfprApFabricEthLanPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthLanPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpEntry.setStatus("current")
_CfprApFabricEthLanPcEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthLanPcEpInstanceId_Object = MibTableColumn
cfprApFabricEthLanPcEpInstanceId = _CfprApFabricEthLanPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 1),
    _CfprApFabricEthLanPcEpInstanceId_Type()
)
cfprApFabricEthLanPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpInstanceId.setStatus("current")
_CfprApFabricEthLanPcEpDnData_Type = CfprApManagedObjectDn
_CfprApFabricEthLanPcEpDnData_Object = MibTableColumn
cfprApFabricEthLanPcEpDnData = _CfprApFabricEthLanPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 2),
    _CfprApFabricEthLanPcEpDnData_Type()
)
cfprApFabricEthLanPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpDnData.setStatus("current")
_CfprApFabricEthLanPcEpRn_Type = SnmpAdminString
_CfprApFabricEthLanPcEpRn_Object = MibTableColumn
cfprApFabricEthLanPcEpRn = _CfprApFabricEthLanPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 3),
    _CfprApFabricEthLanPcEpRn_Type()
)
cfprApFabricEthLanPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpRn.setStatus("current")
_CfprApFabricEthLanPcEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricEthLanPcEpAdminState_Object = MibTableColumn
cfprApFabricEthLanPcEpAdminState = _CfprApFabricEthLanPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 4),
    _CfprApFabricEthLanPcEpAdminState_Type()
)
cfprApFabricEthLanPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpAdminState.setStatus("current")
_CfprApFabricEthLanPcEpAggrPortId_Type = Gauge32
_CfprApFabricEthLanPcEpAggrPortId_Object = MibTableColumn
cfprApFabricEthLanPcEpAggrPortId = _CfprApFabricEthLanPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 5),
    _CfprApFabricEthLanPcEpAggrPortId_Type()
)
cfprApFabricEthLanPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpAggrPortId.setStatus("current")
_CfprApFabricEthLanPcEpChassisId_Type = Gauge32
_CfprApFabricEthLanPcEpChassisId_Object = MibTableColumn
cfprApFabricEthLanPcEpChassisId = _CfprApFabricEthLanPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 6),
    _CfprApFabricEthLanPcEpChassisId_Type()
)
cfprApFabricEthLanPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpChassisId.setStatus("current")
_CfprApFabricEthLanPcEpEpDn_Type = SnmpAdminString
_CfprApFabricEthLanPcEpEpDn_Object = MibTableColumn
cfprApFabricEthLanPcEpEpDn = _CfprApFabricEthLanPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 7),
    _CfprApFabricEthLanPcEpEpDn_Type()
)
cfprApFabricEthLanPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpEpDn.setStatus("current")
_CfprApFabricEthLanPcEpEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricEthLanPcEpEthLinkProfileName_Object = MibTableColumn
cfprApFabricEthLanPcEpEthLinkProfileName = _CfprApFabricEthLanPcEpEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 8),
    _CfprApFabricEthLanPcEpEthLinkProfileName_Type()
)
cfprApFabricEthLanPcEpEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpEthLinkProfileName.setStatus("current")
_CfprApFabricEthLanPcEpFltAggr_Type = Unsigned64
_CfprApFabricEthLanPcEpFltAggr_Object = MibTableColumn
cfprApFabricEthLanPcEpFltAggr = _CfprApFabricEthLanPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 9),
    _CfprApFabricEthLanPcEpFltAggr_Type()
)
cfprApFabricEthLanPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpFltAggr.setStatus("current")
_CfprApFabricEthLanPcEpIfRole_Type = CfprApFabricLanEpIfRole
_CfprApFabricEthLanPcEpIfRole_Object = MibTableColumn
cfprApFabricEthLanPcEpIfRole = _CfprApFabricEthLanPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 10),
    _CfprApFabricEthLanPcEpIfRole_Type()
)
cfprApFabricEthLanPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpIfRole.setStatus("current")
_CfprApFabricEthLanPcEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricEthLanPcEpIfType_Object = MibTableColumn
cfprApFabricEthLanPcEpIfType = _CfprApFabricEthLanPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 11),
    _CfprApFabricEthLanPcEpIfType_Type()
)
cfprApFabricEthLanPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpIfType.setStatus("current")
_CfprApFabricEthLanPcEpLicGP_Type = Unsigned64
_CfprApFabricEthLanPcEpLicGP_Object = MibTableColumn
cfprApFabricEthLanPcEpLicGP = _CfprApFabricEthLanPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 12),
    _CfprApFabricEthLanPcEpLicGP_Type()
)
cfprApFabricEthLanPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpLicGP.setStatus("current")
_CfprApFabricEthLanPcEpLicState_Type = CfprApLicenseState
_CfprApFabricEthLanPcEpLicState_Object = MibTableColumn
cfprApFabricEthLanPcEpLicState = _CfprApFabricEthLanPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 13),
    _CfprApFabricEthLanPcEpLicState_Type()
)
cfprApFabricEthLanPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpLicState.setStatus("current")
_CfprApFabricEthLanPcEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricEthLanPcEpLocale_Object = MibTableColumn
cfprApFabricEthLanPcEpLocale = _CfprApFabricEthLanPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 14),
    _CfprApFabricEthLanPcEpLocale_Type()
)
cfprApFabricEthLanPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpLocale.setStatus("current")
_CfprApFabricEthLanPcEpMembership_Type = CfprApFabricMembershipStatus
_CfprApFabricEthLanPcEpMembership_Object = MibTableColumn
cfprApFabricEthLanPcEpMembership = _CfprApFabricEthLanPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 15),
    _CfprApFabricEthLanPcEpMembership_Type()
)
cfprApFabricEthLanPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpMembership.setStatus("current")
_CfprApFabricEthLanPcEpName_Type = SnmpAdminString
_CfprApFabricEthLanPcEpName_Object = MibTableColumn
cfprApFabricEthLanPcEpName = _CfprApFabricEthLanPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 16),
    _CfprApFabricEthLanPcEpName_Type()
)
cfprApFabricEthLanPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpName.setStatus("current")
_CfprApFabricEthLanPcEpOperEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricEthLanPcEpOperEthLinkProfileName_Object = MibTableColumn
cfprApFabricEthLanPcEpOperEthLinkProfileName = _CfprApFabricEthLanPcEpOperEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 17),
    _CfprApFabricEthLanPcEpOperEthLinkProfileName_Type()
)
cfprApFabricEthLanPcEpOperEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpOperEthLinkProfileName.setStatus("current")
_CfprApFabricEthLanPcEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricEthLanPcEpOperState_Object = MibTableColumn
cfprApFabricEthLanPcEpOperState = _CfprApFabricEthLanPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 18),
    _CfprApFabricEthLanPcEpOperState_Type()
)
cfprApFabricEthLanPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpOperState.setStatus("current")
_CfprApFabricEthLanPcEpOperStateReason_Type = SnmpAdminString
_CfprApFabricEthLanPcEpOperStateReason_Object = MibTableColumn
cfprApFabricEthLanPcEpOperStateReason = _CfprApFabricEthLanPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 19),
    _CfprApFabricEthLanPcEpOperStateReason_Type()
)
cfprApFabricEthLanPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpOperStateReason.setStatus("current")
_CfprApFabricEthLanPcEpPeerAggrPortId_Type = Gauge32
_CfprApFabricEthLanPcEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricEthLanPcEpPeerAggrPortId = _CfprApFabricEthLanPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 20),
    _CfprApFabricEthLanPcEpPeerAggrPortId_Type()
)
cfprApFabricEthLanPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpPeerAggrPortId.setStatus("current")
_CfprApFabricEthLanPcEpPeerChassisId_Type = Gauge32
_CfprApFabricEthLanPcEpPeerChassisId_Object = MibTableColumn
cfprApFabricEthLanPcEpPeerChassisId = _CfprApFabricEthLanPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 21),
    _CfprApFabricEthLanPcEpPeerChassisId_Type()
)
cfprApFabricEthLanPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpPeerChassisId.setStatus("current")
_CfprApFabricEthLanPcEpPeerDn_Type = SnmpAdminString
_CfprApFabricEthLanPcEpPeerDn_Object = MibTableColumn
cfprApFabricEthLanPcEpPeerDn = _CfprApFabricEthLanPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 22),
    _CfprApFabricEthLanPcEpPeerDn_Type()
)
cfprApFabricEthLanPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpPeerDn.setStatus("current")
_CfprApFabricEthLanPcEpPeerPortId_Type = Gauge32
_CfprApFabricEthLanPcEpPeerPortId_Object = MibTableColumn
cfprApFabricEthLanPcEpPeerPortId = _CfprApFabricEthLanPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 23),
    _CfprApFabricEthLanPcEpPeerPortId_Type()
)
cfprApFabricEthLanPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpPeerPortId.setStatus("current")
_CfprApFabricEthLanPcEpPeerSlotId_Type = Gauge32
_CfprApFabricEthLanPcEpPeerSlotId_Object = MibTableColumn
cfprApFabricEthLanPcEpPeerSlotId = _CfprApFabricEthLanPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 24),
    _CfprApFabricEthLanPcEpPeerSlotId_Type()
)
cfprApFabricEthLanPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpPeerSlotId.setStatus("current")
_CfprApFabricEthLanPcEpPortId_Type = Gauge32
_CfprApFabricEthLanPcEpPortId_Object = MibTableColumn
cfprApFabricEthLanPcEpPortId = _CfprApFabricEthLanPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 25),
    _CfprApFabricEthLanPcEpPortId_Type()
)
cfprApFabricEthLanPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpPortId.setStatus("current")
_CfprApFabricEthLanPcEpSlotId_Type = Gauge32
_CfprApFabricEthLanPcEpSlotId_Object = MibTableColumn
cfprApFabricEthLanPcEpSlotId = _CfprApFabricEthLanPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 26),
    _CfprApFabricEthLanPcEpSlotId_Type()
)
cfprApFabricEthLanPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpSlotId.setStatus("current")
_CfprApFabricEthLanPcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthLanPcEpSwitchId_Object = MibTableColumn
cfprApFabricEthLanPcEpSwitchId = _CfprApFabricEthLanPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 27),
    _CfprApFabricEthLanPcEpSwitchId_Type()
)
cfprApFabricEthLanPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpSwitchId.setStatus("current")
_CfprApFabricEthLanPcEpTransport_Type = CfprApFabricAEthLanEpTransport
_CfprApFabricEthLanPcEpTransport_Object = MibTableColumn
cfprApFabricEthLanPcEpTransport = _CfprApFabricEthLanPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 28),
    _CfprApFabricEthLanPcEpTransport_Type()
)
cfprApFabricEthLanPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpTransport.setStatus("current")
_CfprApFabricEthLanPcEpType_Type = CfprApFabricLanEpType
_CfprApFabricEthLanPcEpType_Object = MibTableColumn
cfprApFabricEthLanPcEpType = _CfprApFabricEthLanPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 29),
    _CfprApFabricEthLanPcEpType_Type()
)
cfprApFabricEthLanPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpType.setStatus("current")
_CfprApFabricEthLanPcEpUdldOperState_Type = CfprApFabricUdldOperState
_CfprApFabricEthLanPcEpUdldOperState_Object = MibTableColumn
cfprApFabricEthLanPcEpUdldOperState = _CfprApFabricEthLanPcEpUdldOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 30),
    _CfprApFabricEthLanPcEpUdldOperState_Type()
)
cfprApFabricEthLanPcEpUdldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpUdldOperState.setStatus("current")
_CfprApFabricEthLanPcEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthLanPcEpWarnings_Object = MibTableColumn
cfprApFabricEthLanPcEpWarnings = _CfprApFabricEthLanPcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 30, 1, 31),
    _CfprApFabricEthLanPcEpWarnings_Type()
)
cfprApFabricEthLanPcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLanPcEpWarnings.setStatus("current")
_CfprApFabricEthLinkProfileTable_Object = MibTable
cfprApFabricEthLinkProfileTable = _CfprApFabricEthLinkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31)
)
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileTable.setStatus("current")
_CfprApFabricEthLinkProfileEntry_Object = MibTableRow
cfprApFabricEthLinkProfileEntry = _CfprApFabricEthLinkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1)
)
cfprApFabricEthLinkProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthLinkProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileEntry.setStatus("current")
_CfprApFabricEthLinkProfileInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthLinkProfileInstanceId_Object = MibTableColumn
cfprApFabricEthLinkProfileInstanceId = _CfprApFabricEthLinkProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 1),
    _CfprApFabricEthLinkProfileInstanceId_Type()
)
cfprApFabricEthLinkProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileInstanceId.setStatus("current")
_CfprApFabricEthLinkProfileDn_Type = CfprApManagedObjectDn
_CfprApFabricEthLinkProfileDn_Object = MibTableColumn
cfprApFabricEthLinkProfileDn = _CfprApFabricEthLinkProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 2),
    _CfprApFabricEthLinkProfileDn_Type()
)
cfprApFabricEthLinkProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileDn.setStatus("current")
_CfprApFabricEthLinkProfileRn_Type = SnmpAdminString
_CfprApFabricEthLinkProfileRn_Object = MibTableColumn
cfprApFabricEthLinkProfileRn = _CfprApFabricEthLinkProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 3),
    _CfprApFabricEthLinkProfileRn_Type()
)
cfprApFabricEthLinkProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileRn.setStatus("current")
_CfprApFabricEthLinkProfileCdpLinkPolicyName_Type = SnmpAdminString
_CfprApFabricEthLinkProfileCdpLinkPolicyName_Object = MibTableColumn
cfprApFabricEthLinkProfileCdpLinkPolicyName = _CfprApFabricEthLinkProfileCdpLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 4),
    _CfprApFabricEthLinkProfileCdpLinkPolicyName_Type()
)
cfprApFabricEthLinkProfileCdpLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileCdpLinkPolicyName.setStatus("current")
_CfprApFabricEthLinkProfileDescr_Type = SnmpAdminString
_CfprApFabricEthLinkProfileDescr_Object = MibTableColumn
cfprApFabricEthLinkProfileDescr = _CfprApFabricEthLinkProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 5),
    _CfprApFabricEthLinkProfileDescr_Type()
)
cfprApFabricEthLinkProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileDescr.setStatus("current")
_CfprApFabricEthLinkProfileIntId_Type = SnmpAdminString
_CfprApFabricEthLinkProfileIntId_Object = MibTableColumn
cfprApFabricEthLinkProfileIntId = _CfprApFabricEthLinkProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 6),
    _CfprApFabricEthLinkProfileIntId_Type()
)
cfprApFabricEthLinkProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileIntId.setStatus("current")
_CfprApFabricEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricEthLinkProfileName_Object = MibTableColumn
cfprApFabricEthLinkProfileName = _CfprApFabricEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 7),
    _CfprApFabricEthLinkProfileName_Type()
)
cfprApFabricEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileName.setStatus("current")
_CfprApFabricEthLinkProfileOperCdpLinkPolicyName_Type = SnmpAdminString
_CfprApFabricEthLinkProfileOperCdpLinkPolicyName_Object = MibTableColumn
cfprApFabricEthLinkProfileOperCdpLinkPolicyName = _CfprApFabricEthLinkProfileOperCdpLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 8),
    _CfprApFabricEthLinkProfileOperCdpLinkPolicyName_Type()
)
cfprApFabricEthLinkProfileOperCdpLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileOperCdpLinkPolicyName.setStatus("current")
_CfprApFabricEthLinkProfileOperUdldLinkPolicyName_Type = SnmpAdminString
_CfprApFabricEthLinkProfileOperUdldLinkPolicyName_Object = MibTableColumn
cfprApFabricEthLinkProfileOperUdldLinkPolicyName = _CfprApFabricEthLinkProfileOperUdldLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 9),
    _CfprApFabricEthLinkProfileOperUdldLinkPolicyName_Type()
)
cfprApFabricEthLinkProfileOperUdldLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileOperUdldLinkPolicyName.setStatus("current")
_CfprApFabricEthLinkProfilePolicyLevel_Type = Gauge32
_CfprApFabricEthLinkProfilePolicyLevel_Object = MibTableColumn
cfprApFabricEthLinkProfilePolicyLevel = _CfprApFabricEthLinkProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 10),
    _CfprApFabricEthLinkProfilePolicyLevel_Type()
)
cfprApFabricEthLinkProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfilePolicyLevel.setStatus("current")
_CfprApFabricEthLinkProfilePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricEthLinkProfilePolicyOwner_Object = MibTableColumn
cfprApFabricEthLinkProfilePolicyOwner = _CfprApFabricEthLinkProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 11),
    _CfprApFabricEthLinkProfilePolicyOwner_Type()
)
cfprApFabricEthLinkProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfilePolicyOwner.setStatus("current")
_CfprApFabricEthLinkProfileUdldLinkPolicyName_Type = SnmpAdminString
_CfprApFabricEthLinkProfileUdldLinkPolicyName_Object = MibTableColumn
cfprApFabricEthLinkProfileUdldLinkPolicyName = _CfprApFabricEthLinkProfileUdldLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 31, 1, 12),
    _CfprApFabricEthLinkProfileUdldLinkPolicyName_Type()
)
cfprApFabricEthLinkProfileUdldLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthLinkProfileUdldLinkPolicyName.setStatus("current")
_CfprApFabricEthMonTable_Object = MibTable
cfprApFabricEthMonTable = _CfprApFabricEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32)
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonTable.setStatus("current")
_CfprApFabricEthMonEntry_Object = MibTableRow
cfprApFabricEthMonEntry = _CfprApFabricEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1)
)
cfprApFabricEthMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonEntry.setStatus("current")
_CfprApFabricEthMonInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthMonInstanceId_Object = MibTableColumn
cfprApFabricEthMonInstanceId = _CfprApFabricEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 1),
    _CfprApFabricEthMonInstanceId_Type()
)
cfprApFabricEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthMonInstanceId.setStatus("current")
_CfprApFabricEthMonDn_Type = CfprApManagedObjectDn
_CfprApFabricEthMonDn_Object = MibTableColumn
cfprApFabricEthMonDn = _CfprApFabricEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 2),
    _CfprApFabricEthMonDn_Type()
)
cfprApFabricEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDn.setStatus("current")
_CfprApFabricEthMonRn_Type = SnmpAdminString
_CfprApFabricEthMonRn_Object = MibTableColumn
cfprApFabricEthMonRn = _CfprApFabricEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 3),
    _CfprApFabricEthMonRn_Type()
)
cfprApFabricEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonRn.setStatus("current")
_CfprApFabricEthMonAdminState_Type = CfprApFabricMonAdminState
_CfprApFabricEthMonAdminState_Object = MibTableColumn
cfprApFabricEthMonAdminState = _CfprApFabricEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 4),
    _CfprApFabricEthMonAdminState_Type()
)
cfprApFabricEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonAdminState.setStatus("current")
_CfprApFabricEthMonConfigFailReason_Type = SnmpAdminString
_CfprApFabricEthMonConfigFailReason_Object = MibTableColumn
cfprApFabricEthMonConfigFailReason = _CfprApFabricEthMonConfigFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 5),
    _CfprApFabricEthMonConfigFailReason_Type()
)
cfprApFabricEthMonConfigFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonConfigFailReason.setStatus("current")
_CfprApFabricEthMonId_Type = CfprApNetworkSwitchId
_CfprApFabricEthMonId_Object = MibTableColumn
cfprApFabricEthMonId = _CfprApFabricEthMonId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 6),
    _CfprApFabricEthMonId_Type()
)
cfprApFabricEthMonId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonId.setStatus("current")
_CfprApFabricEthMonIsConfigSuccess_Type = TruthValue
_CfprApFabricEthMonIsConfigSuccess_Object = MibTableColumn
cfprApFabricEthMonIsConfigSuccess = _CfprApFabricEthMonIsConfigSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 7),
    _CfprApFabricEthMonIsConfigSuccess_Type()
)
cfprApFabricEthMonIsConfigSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonIsConfigSuccess.setStatus("current")
_CfprApFabricEthMonLocale_Type = CfprApFabricExternalLocale
_CfprApFabricEthMonLocale_Object = MibTableColumn
cfprApFabricEthMonLocale = _CfprApFabricEthMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 8),
    _CfprApFabricEthMonLocale_Type()
)
cfprApFabricEthMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLocale.setStatus("current")
_CfprApFabricEthMonName_Type = SnmpAdminString
_CfprApFabricEthMonName_Object = MibTableColumn
cfprApFabricEthMonName = _CfprApFabricEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 9),
    _CfprApFabricEthMonName_Type()
)
cfprApFabricEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonName.setStatus("current")
_CfprApFabricEthMonOperState_Type = CfprApFabricMonOperState
_CfprApFabricEthMonOperState_Object = MibTableColumn
cfprApFabricEthMonOperState = _CfprApFabricEthMonOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 10),
    _CfprApFabricEthMonOperState_Type()
)
cfprApFabricEthMonOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonOperState.setStatus("current")
_CfprApFabricEthMonOperStateReason_Type = CfprApFabricMonOperStateReason
_CfprApFabricEthMonOperStateReason_Object = MibTableColumn
cfprApFabricEthMonOperStateReason = _CfprApFabricEthMonOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 11),
    _CfprApFabricEthMonOperStateReason_Type()
)
cfprApFabricEthMonOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonOperStateReason.setStatus("current")
_CfprApFabricEthMonPeerDn_Type = SnmpAdminString
_CfprApFabricEthMonPeerDn_Object = MibTableColumn
cfprApFabricEthMonPeerDn = _CfprApFabricEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 12),
    _CfprApFabricEthMonPeerDn_Type()
)
cfprApFabricEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonPeerDn.setStatus("current")
_CfprApFabricEthMonSession_Type = Gauge32
_CfprApFabricEthMonSession_Object = MibTableColumn
cfprApFabricEthMonSession = _CfprApFabricEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 13),
    _CfprApFabricEthMonSession_Type()
)
cfprApFabricEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSession.setStatus("current")
_CfprApFabricEthMonTransport_Type = CfprApFabricEthMonTransport
_CfprApFabricEthMonTransport_Object = MibTableColumn
cfprApFabricEthMonTransport = _CfprApFabricEthMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 14),
    _CfprApFabricEthMonTransport_Type()
)
cfprApFabricEthMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonTransport.setStatus("current")
_CfprApFabricEthMonType_Type = CfprApFabricEthMonType
_CfprApFabricEthMonType_Object = MibTableColumn
cfprApFabricEthMonType = _CfprApFabricEthMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 32, 1, 15),
    _CfprApFabricEthMonType_Type()
)
cfprApFabricEthMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonType.setStatus("current")
_CfprApFabricEthMonDestEpTable_Object = MibTable
cfprApFabricEthMonDestEpTable = _CfprApFabricEthMonDestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33)
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpTable.setStatus("current")
_CfprApFabricEthMonDestEpEntry_Object = MibTableRow
cfprApFabricEthMonDestEpEntry = _CfprApFabricEthMonDestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1)
)
cfprApFabricEthMonDestEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthMonDestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpEntry.setStatus("current")
_CfprApFabricEthMonDestEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthMonDestEpInstanceId_Object = MibTableColumn
cfprApFabricEthMonDestEpInstanceId = _CfprApFabricEthMonDestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 1),
    _CfprApFabricEthMonDestEpInstanceId_Type()
)
cfprApFabricEthMonDestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpInstanceId.setStatus("current")
_CfprApFabricEthMonDestEpDn_Type = CfprApManagedObjectDn
_CfprApFabricEthMonDestEpDn_Object = MibTableColumn
cfprApFabricEthMonDestEpDn = _CfprApFabricEthMonDestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 2),
    _CfprApFabricEthMonDestEpDn_Type()
)
cfprApFabricEthMonDestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpDn.setStatus("current")
_CfprApFabricEthMonDestEpRn_Type = SnmpAdminString
_CfprApFabricEthMonDestEpRn_Object = MibTableColumn
cfprApFabricEthMonDestEpRn = _CfprApFabricEthMonDestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 3),
    _CfprApFabricEthMonDestEpRn_Type()
)
cfprApFabricEthMonDestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpRn.setStatus("current")
_CfprApFabricEthMonDestEpAdminSpeed_Type = CfprApFabricEthMonDestEpAdminSpeed
_CfprApFabricEthMonDestEpAdminSpeed_Object = MibTableColumn
cfprApFabricEthMonDestEpAdminSpeed = _CfprApFabricEthMonDestEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 4),
    _CfprApFabricEthMonDestEpAdminSpeed_Type()
)
cfprApFabricEthMonDestEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpAdminSpeed.setStatus("current")
_CfprApFabricEthMonDestEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricEthMonDestEpAdminState_Object = MibTableColumn
cfprApFabricEthMonDestEpAdminState = _CfprApFabricEthMonDestEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 5),
    _CfprApFabricEthMonDestEpAdminState_Type()
)
cfprApFabricEthMonDestEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpAdminState.setStatus("current")
_CfprApFabricEthMonDestEpAggrPortId_Type = Gauge32
_CfprApFabricEthMonDestEpAggrPortId_Object = MibTableColumn
cfprApFabricEthMonDestEpAggrPortId = _CfprApFabricEthMonDestEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 6),
    _CfprApFabricEthMonDestEpAggrPortId_Type()
)
cfprApFabricEthMonDestEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpAggrPortId.setStatus("current")
_CfprApFabricEthMonDestEpChassisId_Type = Gauge32
_CfprApFabricEthMonDestEpChassisId_Object = MibTableColumn
cfprApFabricEthMonDestEpChassisId = _CfprApFabricEthMonDestEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 7),
    _CfprApFabricEthMonDestEpChassisId_Type()
)
cfprApFabricEthMonDestEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpChassisId.setStatus("current")
_CfprApFabricEthMonDestEpEpDn_Type = SnmpAdminString
_CfprApFabricEthMonDestEpEpDn_Object = MibTableColumn
cfprApFabricEthMonDestEpEpDn = _CfprApFabricEthMonDestEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 8),
    _CfprApFabricEthMonDestEpEpDn_Type()
)
cfprApFabricEthMonDestEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpEpDn.setStatus("current")
_CfprApFabricEthMonDestEpFltAggr_Type = Unsigned64
_CfprApFabricEthMonDestEpFltAggr_Object = MibTableColumn
cfprApFabricEthMonDestEpFltAggr = _CfprApFabricEthMonDestEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 9),
    _CfprApFabricEthMonDestEpFltAggr_Type()
)
cfprApFabricEthMonDestEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpFltAggr.setStatus("current")
_CfprApFabricEthMonDestEpIfRole_Type = CfprApFabricEthMonDestEpIfRole
_CfprApFabricEthMonDestEpIfRole_Object = MibTableColumn
cfprApFabricEthMonDestEpIfRole = _CfprApFabricEthMonDestEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 10),
    _CfprApFabricEthMonDestEpIfRole_Type()
)
cfprApFabricEthMonDestEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpIfRole.setStatus("current")
_CfprApFabricEthMonDestEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricEthMonDestEpIfType_Object = MibTableColumn
cfprApFabricEthMonDestEpIfType = _CfprApFabricEthMonDestEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 11),
    _CfprApFabricEthMonDestEpIfType_Type()
)
cfprApFabricEthMonDestEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpIfType.setStatus("current")
_CfprApFabricEthMonDestEpLicGP_Type = Unsigned64
_CfprApFabricEthMonDestEpLicGP_Object = MibTableColumn
cfprApFabricEthMonDestEpLicGP = _CfprApFabricEthMonDestEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 12),
    _CfprApFabricEthMonDestEpLicGP_Type()
)
cfprApFabricEthMonDestEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpLicGP.setStatus("current")
_CfprApFabricEthMonDestEpLicState_Type = CfprApLicenseState
_CfprApFabricEthMonDestEpLicState_Object = MibTableColumn
cfprApFabricEthMonDestEpLicState = _CfprApFabricEthMonDestEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 13),
    _CfprApFabricEthMonDestEpLicState_Type()
)
cfprApFabricEthMonDestEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpLicState.setStatus("current")
_CfprApFabricEthMonDestEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricEthMonDestEpLocale_Object = MibTableColumn
cfprApFabricEthMonDestEpLocale = _CfprApFabricEthMonDestEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 14),
    _CfprApFabricEthMonDestEpLocale_Type()
)
cfprApFabricEthMonDestEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpLocale.setStatus("current")
_CfprApFabricEthMonDestEpName_Type = SnmpAdminString
_CfprApFabricEthMonDestEpName_Object = MibTableColumn
cfprApFabricEthMonDestEpName = _CfprApFabricEthMonDestEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 15),
    _CfprApFabricEthMonDestEpName_Type()
)
cfprApFabricEthMonDestEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpName.setStatus("current")
_CfprApFabricEthMonDestEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricEthMonDestEpOperState_Object = MibTableColumn
cfprApFabricEthMonDestEpOperState = _CfprApFabricEthMonDestEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 16),
    _CfprApFabricEthMonDestEpOperState_Type()
)
cfprApFabricEthMonDestEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpOperState.setStatus("current")
_CfprApFabricEthMonDestEpOperStateReason_Type = SnmpAdminString
_CfprApFabricEthMonDestEpOperStateReason_Object = MibTableColumn
cfprApFabricEthMonDestEpOperStateReason = _CfprApFabricEthMonDestEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 17),
    _CfprApFabricEthMonDestEpOperStateReason_Type()
)
cfprApFabricEthMonDestEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpOperStateReason.setStatus("current")
_CfprApFabricEthMonDestEpPeerAggrPortId_Type = Gauge32
_CfprApFabricEthMonDestEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricEthMonDestEpPeerAggrPortId = _CfprApFabricEthMonDestEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 18),
    _CfprApFabricEthMonDestEpPeerAggrPortId_Type()
)
cfprApFabricEthMonDestEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpPeerAggrPortId.setStatus("current")
_CfprApFabricEthMonDestEpPeerChassisId_Type = Gauge32
_CfprApFabricEthMonDestEpPeerChassisId_Object = MibTableColumn
cfprApFabricEthMonDestEpPeerChassisId = _CfprApFabricEthMonDestEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 19),
    _CfprApFabricEthMonDestEpPeerChassisId_Type()
)
cfprApFabricEthMonDestEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpPeerChassisId.setStatus("current")
_CfprApFabricEthMonDestEpPeerDn_Type = SnmpAdminString
_CfprApFabricEthMonDestEpPeerDn_Object = MibTableColumn
cfprApFabricEthMonDestEpPeerDn = _CfprApFabricEthMonDestEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 20),
    _CfprApFabricEthMonDestEpPeerDn_Type()
)
cfprApFabricEthMonDestEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpPeerDn.setStatus("current")
_CfprApFabricEthMonDestEpPeerPortId_Type = Gauge32
_CfprApFabricEthMonDestEpPeerPortId_Object = MibTableColumn
cfprApFabricEthMonDestEpPeerPortId = _CfprApFabricEthMonDestEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 21),
    _CfprApFabricEthMonDestEpPeerPortId_Type()
)
cfprApFabricEthMonDestEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpPeerPortId.setStatus("current")
_CfprApFabricEthMonDestEpPeerSlotId_Type = Gauge32
_CfprApFabricEthMonDestEpPeerSlotId_Object = MibTableColumn
cfprApFabricEthMonDestEpPeerSlotId = _CfprApFabricEthMonDestEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 22),
    _CfprApFabricEthMonDestEpPeerSlotId_Type()
)
cfprApFabricEthMonDestEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpPeerSlotId.setStatus("current")
_CfprApFabricEthMonDestEpPortId_Type = CfprApFabricEthMonDestEpPortId
_CfprApFabricEthMonDestEpPortId_Object = MibTableColumn
cfprApFabricEthMonDestEpPortId = _CfprApFabricEthMonDestEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 23),
    _CfprApFabricEthMonDestEpPortId_Type()
)
cfprApFabricEthMonDestEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpPortId.setStatus("current")
_CfprApFabricEthMonDestEpSlotId_Type = CfprApFabricEthMonDestEpSlotId
_CfprApFabricEthMonDestEpSlotId_Object = MibTableColumn
cfprApFabricEthMonDestEpSlotId = _CfprApFabricEthMonDestEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 24),
    _CfprApFabricEthMonDestEpSlotId_Type()
)
cfprApFabricEthMonDestEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpSlotId.setStatus("current")
_CfprApFabricEthMonDestEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthMonDestEpSwitchId_Object = MibTableColumn
cfprApFabricEthMonDestEpSwitchId = _CfprApFabricEthMonDestEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 25),
    _CfprApFabricEthMonDestEpSwitchId_Type()
)
cfprApFabricEthMonDestEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpSwitchId.setStatus("current")
_CfprApFabricEthMonDestEpTransport_Type = CfprApNetworkTransport
_CfprApFabricEthMonDestEpTransport_Object = MibTableColumn
cfprApFabricEthMonDestEpTransport = _CfprApFabricEthMonDestEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 26),
    _CfprApFabricEthMonDestEpTransport_Type()
)
cfprApFabricEthMonDestEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpTransport.setStatus("current")
_CfprApFabricEthMonDestEpType_Type = CfprApFabricEthMonDestEpType
_CfprApFabricEthMonDestEpType_Object = MibTableColumn
cfprApFabricEthMonDestEpType = _CfprApFabricEthMonDestEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 27),
    _CfprApFabricEthMonDestEpType_Type()
)
cfprApFabricEthMonDestEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpType.setStatus("current")
_CfprApFabricEthMonDestEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthMonDestEpWarnings_Object = MibTableColumn
cfprApFabricEthMonDestEpWarnings = _CfprApFabricEthMonDestEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 33, 1, 28),
    _CfprApFabricEthMonDestEpWarnings_Type()
)
cfprApFabricEthMonDestEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonDestEpWarnings.setStatus("current")
_CfprApFabricEthMonFiltEpTable_Object = MibTable
cfprApFabricEthMonFiltEpTable = _CfprApFabricEthMonFiltEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 34)
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltEpTable.setStatus("current")
_CfprApFabricEthMonFiltEpEntry_Object = MibTableRow
cfprApFabricEthMonFiltEpEntry = _CfprApFabricEthMonFiltEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 34, 1)
)
cfprApFabricEthMonFiltEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthMonFiltEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltEpEntry.setStatus("current")
_CfprApFabricEthMonFiltEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthMonFiltEpInstanceId_Object = MibTableColumn
cfprApFabricEthMonFiltEpInstanceId = _CfprApFabricEthMonFiltEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 34, 1, 1),
    _CfprApFabricEthMonFiltEpInstanceId_Type()
)
cfprApFabricEthMonFiltEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltEpInstanceId.setStatus("current")
_CfprApFabricEthMonFiltEpDn_Type = CfprApManagedObjectDn
_CfprApFabricEthMonFiltEpDn_Object = MibTableColumn
cfprApFabricEthMonFiltEpDn = _CfprApFabricEthMonFiltEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 34, 1, 2),
    _CfprApFabricEthMonFiltEpDn_Type()
)
cfprApFabricEthMonFiltEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltEpDn.setStatus("current")
_CfprApFabricEthMonFiltEpRn_Type = SnmpAdminString
_CfprApFabricEthMonFiltEpRn_Object = MibTableColumn
cfprApFabricEthMonFiltEpRn = _CfprApFabricEthMonFiltEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 34, 1, 3),
    _CfprApFabricEthMonFiltEpRn_Type()
)
cfprApFabricEthMonFiltEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltEpRn.setStatus("current")
_CfprApFabricEthMonFiltEpName_Type = SnmpAdminString
_CfprApFabricEthMonFiltEpName_Object = MibTableColumn
cfprApFabricEthMonFiltEpName = _CfprApFabricEthMonFiltEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 34, 1, 4),
    _CfprApFabricEthMonFiltEpName_Type()
)
cfprApFabricEthMonFiltEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltEpName.setStatus("current")
_CfprApFabricEthMonFiltEpSession_Type = Gauge32
_CfprApFabricEthMonFiltEpSession_Object = MibTableColumn
cfprApFabricEthMonFiltEpSession = _CfprApFabricEthMonFiltEpSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 34, 1, 5),
    _CfprApFabricEthMonFiltEpSession_Type()
)
cfprApFabricEthMonFiltEpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltEpSession.setStatus("current")
_CfprApFabricEthMonFiltEpType_Type = CfprApFabricEthMonFiltEpType
_CfprApFabricEthMonFiltEpType_Object = MibTableColumn
cfprApFabricEthMonFiltEpType = _CfprApFabricEthMonFiltEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 34, 1, 6),
    _CfprApFabricEthMonFiltEpType_Type()
)
cfprApFabricEthMonFiltEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltEpType.setStatus("current")
_CfprApFabricEthMonFiltRefTable_Object = MibTable
cfprApFabricEthMonFiltRefTable = _CfprApFabricEthMonFiltRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 35)
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltRefTable.setStatus("current")
_CfprApFabricEthMonFiltRefEntry_Object = MibTableRow
cfprApFabricEthMonFiltRefEntry = _CfprApFabricEthMonFiltRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 35, 1)
)
cfprApFabricEthMonFiltRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthMonFiltRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltRefEntry.setStatus("current")
_CfprApFabricEthMonFiltRefInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthMonFiltRefInstanceId_Object = MibTableColumn
cfprApFabricEthMonFiltRefInstanceId = _CfprApFabricEthMonFiltRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 35, 1, 1),
    _CfprApFabricEthMonFiltRefInstanceId_Type()
)
cfprApFabricEthMonFiltRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltRefInstanceId.setStatus("current")
_CfprApFabricEthMonFiltRefDn_Type = CfprApManagedObjectDn
_CfprApFabricEthMonFiltRefDn_Object = MibTableColumn
cfprApFabricEthMonFiltRefDn = _CfprApFabricEthMonFiltRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 35, 1, 2),
    _CfprApFabricEthMonFiltRefDn_Type()
)
cfprApFabricEthMonFiltRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltRefDn.setStatus("current")
_CfprApFabricEthMonFiltRefRn_Type = SnmpAdminString
_CfprApFabricEthMonFiltRefRn_Object = MibTableColumn
cfprApFabricEthMonFiltRefRn = _CfprApFabricEthMonFiltRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 35, 1, 3),
    _CfprApFabricEthMonFiltRefRn_Type()
)
cfprApFabricEthMonFiltRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltRefRn.setStatus("current")
_CfprApFabricEthMonFiltRefSrcFiltDn_Type = SnmpAdminString
_CfprApFabricEthMonFiltRefSrcFiltDn_Object = MibTableColumn
cfprApFabricEthMonFiltRefSrcFiltDn = _CfprApFabricEthMonFiltRefSrcFiltDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 35, 1, 4),
    _CfprApFabricEthMonFiltRefSrcFiltDn_Type()
)
cfprApFabricEthMonFiltRefSrcFiltDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltRefSrcFiltDn.setStatus("current")
_CfprApFabricEthMonFiltRefType_Type = CfprApFabricEthMonFiltRefType
_CfprApFabricEthMonFiltRefType_Object = MibTableColumn
cfprApFabricEthMonFiltRefType = _CfprApFabricEthMonFiltRefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 35, 1, 5),
    _CfprApFabricEthMonFiltRefType_Type()
)
cfprApFabricEthMonFiltRefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonFiltRefType.setStatus("current")
_CfprApFabricEthMonLanTable_Object = MibTable
cfprApFabricEthMonLanTable = _CfprApFabricEthMonLanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36)
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanTable.setStatus("current")
_CfprApFabricEthMonLanEntry_Object = MibTableRow
cfprApFabricEthMonLanEntry = _CfprApFabricEthMonLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1)
)
cfprApFabricEthMonLanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthMonLanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanEntry.setStatus("current")
_CfprApFabricEthMonLanInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthMonLanInstanceId_Object = MibTableColumn
cfprApFabricEthMonLanInstanceId = _CfprApFabricEthMonLanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1, 1),
    _CfprApFabricEthMonLanInstanceId_Type()
)
cfprApFabricEthMonLanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanInstanceId.setStatus("current")
_CfprApFabricEthMonLanDn_Type = CfprApManagedObjectDn
_CfprApFabricEthMonLanDn_Object = MibTableColumn
cfprApFabricEthMonLanDn = _CfprApFabricEthMonLanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1, 2),
    _CfprApFabricEthMonLanDn_Type()
)
cfprApFabricEthMonLanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanDn.setStatus("current")
_CfprApFabricEthMonLanRn_Type = SnmpAdminString
_CfprApFabricEthMonLanRn_Object = MibTableColumn
cfprApFabricEthMonLanRn = _CfprApFabricEthMonLanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1, 3),
    _CfprApFabricEthMonLanRn_Type()
)
cfprApFabricEthMonLanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanRn.setStatus("current")
_CfprApFabricEthMonLanId_Type = CfprApNetworkSwitchId
_CfprApFabricEthMonLanId_Object = MibTableColumn
cfprApFabricEthMonLanId = _CfprApFabricEthMonLanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1, 4),
    _CfprApFabricEthMonLanId_Type()
)
cfprApFabricEthMonLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanId.setStatus("current")
_CfprApFabricEthMonLanLocale_Type = CfprApFabricExternalLocale
_CfprApFabricEthMonLanLocale_Object = MibTableColumn
cfprApFabricEthMonLanLocale = _CfprApFabricEthMonLanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1, 5),
    _CfprApFabricEthMonLanLocale_Type()
)
cfprApFabricEthMonLanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanLocale.setStatus("current")
_CfprApFabricEthMonLanName_Type = SnmpAdminString
_CfprApFabricEthMonLanName_Object = MibTableColumn
cfprApFabricEthMonLanName = _CfprApFabricEthMonLanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1, 6),
    _CfprApFabricEthMonLanName_Type()
)
cfprApFabricEthMonLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanName.setStatus("current")
_CfprApFabricEthMonLanTransport_Type = CfprApFabricEthMonLanTransport
_CfprApFabricEthMonLanTransport_Object = MibTableColumn
cfprApFabricEthMonLanTransport = _CfprApFabricEthMonLanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1, 7),
    _CfprApFabricEthMonLanTransport_Type()
)
cfprApFabricEthMonLanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanTransport.setStatus("current")
_CfprApFabricEthMonLanType_Type = CfprApFabricEthMonLanType
_CfprApFabricEthMonLanType_Object = MibTableColumn
cfprApFabricEthMonLanType = _CfprApFabricEthMonLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 36, 1, 8),
    _CfprApFabricEthMonLanType_Type()
)
cfprApFabricEthMonLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonLanType.setStatus("current")
_CfprApFabricEthMonSrcEpTable_Object = MibTable
cfprApFabricEthMonSrcEpTable = _CfprApFabricEthMonSrcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37)
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpTable.setStatus("current")
_CfprApFabricEthMonSrcEpEntry_Object = MibTableRow
cfprApFabricEthMonSrcEpEntry = _CfprApFabricEthMonSrcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1)
)
cfprApFabricEthMonSrcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthMonSrcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpEntry.setStatus("current")
_CfprApFabricEthMonSrcEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthMonSrcEpInstanceId_Object = MibTableColumn
cfprApFabricEthMonSrcEpInstanceId = _CfprApFabricEthMonSrcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1, 1),
    _CfprApFabricEthMonSrcEpInstanceId_Type()
)
cfprApFabricEthMonSrcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpInstanceId.setStatus("current")
_CfprApFabricEthMonSrcEpDn_Type = CfprApManagedObjectDn
_CfprApFabricEthMonSrcEpDn_Object = MibTableColumn
cfprApFabricEthMonSrcEpDn = _CfprApFabricEthMonSrcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1, 2),
    _CfprApFabricEthMonSrcEpDn_Type()
)
cfprApFabricEthMonSrcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpDn.setStatus("current")
_CfprApFabricEthMonSrcEpRn_Type = SnmpAdminString
_CfprApFabricEthMonSrcEpRn_Object = MibTableColumn
cfprApFabricEthMonSrcEpRn = _CfprApFabricEthMonSrcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1, 3),
    _CfprApFabricEthMonSrcEpRn_Type()
)
cfprApFabricEthMonSrcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpRn.setStatus("current")
_CfprApFabricEthMonSrcEpDirection_Type = CfprApFabricTrafficDirection
_CfprApFabricEthMonSrcEpDirection_Object = MibTableColumn
cfprApFabricEthMonSrcEpDirection = _CfprApFabricEthMonSrcEpDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1, 4),
    _CfprApFabricEthMonSrcEpDirection_Type()
)
cfprApFabricEthMonSrcEpDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpDirection.setStatus("current")
_CfprApFabricEthMonSrcEpName_Type = SnmpAdminString
_CfprApFabricEthMonSrcEpName_Object = MibTableColumn
cfprApFabricEthMonSrcEpName = _CfprApFabricEthMonSrcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1, 5),
    _CfprApFabricEthMonSrcEpName_Type()
)
cfprApFabricEthMonSrcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpName.setStatus("current")
_CfprApFabricEthMonSrcEpSession_Type = Gauge32
_CfprApFabricEthMonSrcEpSession_Object = MibTableColumn
cfprApFabricEthMonSrcEpSession = _CfprApFabricEthMonSrcEpSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1, 6),
    _CfprApFabricEthMonSrcEpSession_Type()
)
cfprApFabricEthMonSrcEpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpSession.setStatus("current")
_CfprApFabricEthMonSrcEpTransport_Type = CfprApNetworkTransport
_CfprApFabricEthMonSrcEpTransport_Object = MibTableColumn
cfprApFabricEthMonSrcEpTransport = _CfprApFabricEthMonSrcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1, 7),
    _CfprApFabricEthMonSrcEpTransport_Type()
)
cfprApFabricEthMonSrcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpTransport.setStatus("current")
_CfprApFabricEthMonSrcEpType_Type = CfprApFabricEthMonSrcEpType
_CfprApFabricEthMonSrcEpType_Object = MibTableColumn
cfprApFabricEthMonSrcEpType = _CfprApFabricEthMonSrcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 37, 1, 8),
    _CfprApFabricEthMonSrcEpType_Type()
)
cfprApFabricEthMonSrcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcEpType.setStatus("current")
_CfprApFabricEthMonSrcRefTable_Object = MibTable
cfprApFabricEthMonSrcRefTable = _CfprApFabricEthMonSrcRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38)
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefTable.setStatus("current")
_CfprApFabricEthMonSrcRefEntry_Object = MibTableRow
cfprApFabricEthMonSrcRefEntry = _CfprApFabricEthMonSrcRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38, 1)
)
cfprApFabricEthMonSrcRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthMonSrcRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefEntry.setStatus("current")
_CfprApFabricEthMonSrcRefInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthMonSrcRefInstanceId_Object = MibTableColumn
cfprApFabricEthMonSrcRefInstanceId = _CfprApFabricEthMonSrcRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38, 1, 1),
    _CfprApFabricEthMonSrcRefInstanceId_Type()
)
cfprApFabricEthMonSrcRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefInstanceId.setStatus("current")
_CfprApFabricEthMonSrcRefDn_Type = CfprApManagedObjectDn
_CfprApFabricEthMonSrcRefDn_Object = MibTableColumn
cfprApFabricEthMonSrcRefDn = _CfprApFabricEthMonSrcRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38, 1, 2),
    _CfprApFabricEthMonSrcRefDn_Type()
)
cfprApFabricEthMonSrcRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefDn.setStatus("current")
_CfprApFabricEthMonSrcRefRn_Type = SnmpAdminString
_CfprApFabricEthMonSrcRefRn_Object = MibTableColumn
cfprApFabricEthMonSrcRefRn = _CfprApFabricEthMonSrcRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38, 1, 3),
    _CfprApFabricEthMonSrcRefRn_Type()
)
cfprApFabricEthMonSrcRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefRn.setStatus("current")
_CfprApFabricEthMonSrcRefId_Type = Unsigned64
_CfprApFabricEthMonSrcRefId_Object = MibTableColumn
cfprApFabricEthMonSrcRefId = _CfprApFabricEthMonSrcRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38, 1, 4),
    _CfprApFabricEthMonSrcRefId_Type()
)
cfprApFabricEthMonSrcRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefId.setStatus("current")
_CfprApFabricEthMonSrcRefSourceDn_Type = SnmpAdminString
_CfprApFabricEthMonSrcRefSourceDn_Object = MibTableColumn
cfprApFabricEthMonSrcRefSourceDn = _CfprApFabricEthMonSrcRefSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38, 1, 5),
    _CfprApFabricEthMonSrcRefSourceDn_Type()
)
cfprApFabricEthMonSrcRefSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefSourceDn.setStatus("current")
_CfprApFabricEthMonSrcRefSourceType_Type = CfprApFabricEthSourceType
_CfprApFabricEthMonSrcRefSourceType_Object = MibTableColumn
cfprApFabricEthMonSrcRefSourceType = _CfprApFabricEthMonSrcRefSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38, 1, 6),
    _CfprApFabricEthMonSrcRefSourceType_Type()
)
cfprApFabricEthMonSrcRefSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefSourceType.setStatus("current")
_CfprApFabricEthMonSrcRefType_Type = CfprApFabricEthMonSrcRefType
_CfprApFabricEthMonSrcRefType_Object = MibTableColumn
cfprApFabricEthMonSrcRefType = _CfprApFabricEthMonSrcRefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 38, 1, 7),
    _CfprApFabricEthMonSrcRefType_Type()
)
cfprApFabricEthMonSrcRefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthMonSrcRefType.setStatus("current")
_CfprApFabricEthTargetEpTable_Object = MibTable
cfprApFabricEthTargetEpTable = _CfprApFabricEthTargetEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39)
)
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpTable.setStatus("current")
_CfprApFabricEthTargetEpEntry_Object = MibTableRow
cfprApFabricEthTargetEpEntry = _CfprApFabricEthTargetEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1)
)
cfprApFabricEthTargetEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthTargetEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpEntry.setStatus("current")
_CfprApFabricEthTargetEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthTargetEpInstanceId_Object = MibTableColumn
cfprApFabricEthTargetEpInstanceId = _CfprApFabricEthTargetEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 1),
    _CfprApFabricEthTargetEpInstanceId_Type()
)
cfprApFabricEthTargetEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpInstanceId.setStatus("current")
_CfprApFabricEthTargetEpDn_Type = CfprApManagedObjectDn
_CfprApFabricEthTargetEpDn_Object = MibTableColumn
cfprApFabricEthTargetEpDn = _CfprApFabricEthTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 2),
    _CfprApFabricEthTargetEpDn_Type()
)
cfprApFabricEthTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpDn.setStatus("current")
_CfprApFabricEthTargetEpRn_Type = SnmpAdminString
_CfprApFabricEthTargetEpRn_Object = MibTableColumn
cfprApFabricEthTargetEpRn = _CfprApFabricEthTargetEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 3),
    _CfprApFabricEthTargetEpRn_Type()
)
cfprApFabricEthTargetEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpRn.setStatus("current")
_CfprApFabricEthTargetEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricEthTargetEpAdminState_Object = MibTableColumn
cfprApFabricEthTargetEpAdminState = _CfprApFabricEthTargetEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 4),
    _CfprApFabricEthTargetEpAdminState_Type()
)
cfprApFabricEthTargetEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpAdminState.setStatus("current")
_CfprApFabricEthTargetEpAggrPortId_Type = Gauge32
_CfprApFabricEthTargetEpAggrPortId_Object = MibTableColumn
cfprApFabricEthTargetEpAggrPortId = _CfprApFabricEthTargetEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 5),
    _CfprApFabricEthTargetEpAggrPortId_Type()
)
cfprApFabricEthTargetEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpAggrPortId.setStatus("current")
_CfprApFabricEthTargetEpChassisId_Type = Gauge32
_CfprApFabricEthTargetEpChassisId_Object = MibTableColumn
cfprApFabricEthTargetEpChassisId = _CfprApFabricEthTargetEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 6),
    _CfprApFabricEthTargetEpChassisId_Type()
)
cfprApFabricEthTargetEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpChassisId.setStatus("current")
_CfprApFabricEthTargetEpEpDn_Type = SnmpAdminString
_CfprApFabricEthTargetEpEpDn_Object = MibTableColumn
cfprApFabricEthTargetEpEpDn = _CfprApFabricEthTargetEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 7),
    _CfprApFabricEthTargetEpEpDn_Type()
)
cfprApFabricEthTargetEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpEpDn.setStatus("current")
_CfprApFabricEthTargetEpFltAggr_Type = Unsigned64
_CfprApFabricEthTargetEpFltAggr_Object = MibTableColumn
cfprApFabricEthTargetEpFltAggr = _CfprApFabricEthTargetEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 8),
    _CfprApFabricEthTargetEpFltAggr_Type()
)
cfprApFabricEthTargetEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpFltAggr.setStatus("current")
_CfprApFabricEthTargetEpIfRole_Type = CfprApNetworkPortRole
_CfprApFabricEthTargetEpIfRole_Object = MibTableColumn
cfprApFabricEthTargetEpIfRole = _CfprApFabricEthTargetEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 9),
    _CfprApFabricEthTargetEpIfRole_Type()
)
cfprApFabricEthTargetEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpIfRole.setStatus("current")
_CfprApFabricEthTargetEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricEthTargetEpIfType_Object = MibTableColumn
cfprApFabricEthTargetEpIfType = _CfprApFabricEthTargetEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 10),
    _CfprApFabricEthTargetEpIfType_Type()
)
cfprApFabricEthTargetEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpIfType.setStatus("current")
_CfprApFabricEthTargetEpLicGP_Type = Unsigned64
_CfprApFabricEthTargetEpLicGP_Object = MibTableColumn
cfprApFabricEthTargetEpLicGP = _CfprApFabricEthTargetEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 11),
    _CfprApFabricEthTargetEpLicGP_Type()
)
cfprApFabricEthTargetEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpLicGP.setStatus("current")
_CfprApFabricEthTargetEpLicState_Type = CfprApLicenseState
_CfprApFabricEthTargetEpLicState_Object = MibTableColumn
cfprApFabricEthTargetEpLicState = _CfprApFabricEthTargetEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 12),
    _CfprApFabricEthTargetEpLicState_Type()
)
cfprApFabricEthTargetEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpLicState.setStatus("current")
_CfprApFabricEthTargetEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricEthTargetEpLocale_Object = MibTableColumn
cfprApFabricEthTargetEpLocale = _CfprApFabricEthTargetEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 13),
    _CfprApFabricEthTargetEpLocale_Type()
)
cfprApFabricEthTargetEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpLocale.setStatus("current")
_CfprApFabricEthTargetEpMacAddress_Type = MacAddress
_CfprApFabricEthTargetEpMacAddress_Object = MibTableColumn
cfprApFabricEthTargetEpMacAddress = _CfprApFabricEthTargetEpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 14),
    _CfprApFabricEthTargetEpMacAddress_Type()
)
cfprApFabricEthTargetEpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpMacAddress.setStatus("current")
_CfprApFabricEthTargetEpName_Type = SnmpAdminString
_CfprApFabricEthTargetEpName_Object = MibTableColumn
cfprApFabricEthTargetEpName = _CfprApFabricEthTargetEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 15),
    _CfprApFabricEthTargetEpName_Type()
)
cfprApFabricEthTargetEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpName.setStatus("current")
_CfprApFabricEthTargetEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricEthTargetEpOperState_Object = MibTableColumn
cfprApFabricEthTargetEpOperState = _CfprApFabricEthTargetEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 16),
    _CfprApFabricEthTargetEpOperState_Type()
)
cfprApFabricEthTargetEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpOperState.setStatus("current")
_CfprApFabricEthTargetEpOperStateReason_Type = SnmpAdminString
_CfprApFabricEthTargetEpOperStateReason_Object = MibTableColumn
cfprApFabricEthTargetEpOperStateReason = _CfprApFabricEthTargetEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 17),
    _CfprApFabricEthTargetEpOperStateReason_Type()
)
cfprApFabricEthTargetEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpOperStateReason.setStatus("current")
_CfprApFabricEthTargetEpPeerAggrPortId_Type = Gauge32
_CfprApFabricEthTargetEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricEthTargetEpPeerAggrPortId = _CfprApFabricEthTargetEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 18),
    _CfprApFabricEthTargetEpPeerAggrPortId_Type()
)
cfprApFabricEthTargetEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpPeerAggrPortId.setStatus("current")
_CfprApFabricEthTargetEpPeerChassisId_Type = Gauge32
_CfprApFabricEthTargetEpPeerChassisId_Object = MibTableColumn
cfprApFabricEthTargetEpPeerChassisId = _CfprApFabricEthTargetEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 19),
    _CfprApFabricEthTargetEpPeerChassisId_Type()
)
cfprApFabricEthTargetEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpPeerChassisId.setStatus("current")
_CfprApFabricEthTargetEpPeerDn_Type = SnmpAdminString
_CfprApFabricEthTargetEpPeerDn_Object = MibTableColumn
cfprApFabricEthTargetEpPeerDn = _CfprApFabricEthTargetEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 20),
    _CfprApFabricEthTargetEpPeerDn_Type()
)
cfprApFabricEthTargetEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpPeerDn.setStatus("current")
_CfprApFabricEthTargetEpPeerPortId_Type = Gauge32
_CfprApFabricEthTargetEpPeerPortId_Object = MibTableColumn
cfprApFabricEthTargetEpPeerPortId = _CfprApFabricEthTargetEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 21),
    _CfprApFabricEthTargetEpPeerPortId_Type()
)
cfprApFabricEthTargetEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpPeerPortId.setStatus("current")
_CfprApFabricEthTargetEpPeerSlotId_Type = Gauge32
_CfprApFabricEthTargetEpPeerSlotId_Object = MibTableColumn
cfprApFabricEthTargetEpPeerSlotId = _CfprApFabricEthTargetEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 22),
    _CfprApFabricEthTargetEpPeerSlotId_Type()
)
cfprApFabricEthTargetEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpPeerSlotId.setStatus("current")
_CfprApFabricEthTargetEpPortId_Type = CfprApFabricPIoEpPortId
_CfprApFabricEthTargetEpPortId_Object = MibTableColumn
cfprApFabricEthTargetEpPortId = _CfprApFabricEthTargetEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 23),
    _CfprApFabricEthTargetEpPortId_Type()
)
cfprApFabricEthTargetEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpPortId.setStatus("current")
_CfprApFabricEthTargetEpSlotId_Type = CfprApFabricPIoEpSlotId
_CfprApFabricEthTargetEpSlotId_Object = MibTableColumn
cfprApFabricEthTargetEpSlotId = _CfprApFabricEthTargetEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 24),
    _CfprApFabricEthTargetEpSlotId_Type()
)
cfprApFabricEthTargetEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpSlotId.setStatus("current")
_CfprApFabricEthTargetEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthTargetEpSwitchId_Object = MibTableColumn
cfprApFabricEthTargetEpSwitchId = _CfprApFabricEthTargetEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 25),
    _CfprApFabricEthTargetEpSwitchId_Type()
)
cfprApFabricEthTargetEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpSwitchId.setStatus("current")
_CfprApFabricEthTargetEpTransport_Type = CfprApFabricEthTargetEpTransport
_CfprApFabricEthTargetEpTransport_Object = MibTableColumn
cfprApFabricEthTargetEpTransport = _CfprApFabricEthTargetEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 26),
    _CfprApFabricEthTargetEpTransport_Type()
)
cfprApFabricEthTargetEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpTransport.setStatus("current")
_CfprApFabricEthTargetEpType_Type = CfprApFabricTargetEpType
_CfprApFabricEthTargetEpType_Object = MibTableColumn
cfprApFabricEthTargetEpType = _CfprApFabricEthTargetEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 27),
    _CfprApFabricEthTargetEpType_Type()
)
cfprApFabricEthTargetEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpType.setStatus("current")
_CfprApFabricEthTargetEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthTargetEpWarnings_Object = MibTableColumn
cfprApFabricEthTargetEpWarnings = _CfprApFabricEthTargetEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 39, 1, 28),
    _CfprApFabricEthTargetEpWarnings_Type()
)
cfprApFabricEthTargetEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthTargetEpWarnings.setStatus("current")
_CfprApFabricEthVlanPcTable_Object = MibTable
cfprApFabricEthVlanPcTable = _CfprApFabricEthVlanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40)
)
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcTable.setStatus("current")
_CfprApFabricEthVlanPcEntry_Object = MibTableRow
cfprApFabricEthVlanPcEntry = _CfprApFabricEthVlanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1)
)
cfprApFabricEthVlanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthVlanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcEntry.setStatus("current")
_CfprApFabricEthVlanPcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthVlanPcInstanceId_Object = MibTableColumn
cfprApFabricEthVlanPcInstanceId = _CfprApFabricEthVlanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 1),
    _CfprApFabricEthVlanPcInstanceId_Type()
)
cfprApFabricEthVlanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcInstanceId.setStatus("current")
_CfprApFabricEthVlanPcDn_Type = CfprApManagedObjectDn
_CfprApFabricEthVlanPcDn_Object = MibTableColumn
cfprApFabricEthVlanPcDn = _CfprApFabricEthVlanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 2),
    _CfprApFabricEthVlanPcDn_Type()
)
cfprApFabricEthVlanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcDn.setStatus("current")
_CfprApFabricEthVlanPcRn_Type = SnmpAdminString
_CfprApFabricEthVlanPcRn_Object = MibTableColumn
cfprApFabricEthVlanPcRn = _CfprApFabricEthVlanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 3),
    _CfprApFabricEthVlanPcRn_Type()
)
cfprApFabricEthVlanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcRn.setStatus("current")
_CfprApFabricEthVlanPcAdminSpeed_Type = CfprApPortEthAdminSpeed
_CfprApFabricEthVlanPcAdminSpeed_Object = MibTableColumn
cfprApFabricEthVlanPcAdminSpeed = _CfprApFabricEthVlanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 4),
    _CfprApFabricEthVlanPcAdminSpeed_Type()
)
cfprApFabricEthVlanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcAdminSpeed.setStatus("current")
_CfprApFabricEthVlanPcAdminState_Type = CfprApFabricCIoEpAdminState
_CfprApFabricEthVlanPcAdminState_Object = MibTableColumn
cfprApFabricEthVlanPcAdminState = _CfprApFabricEthVlanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 5),
    _CfprApFabricEthVlanPcAdminState_Type()
)
cfprApFabricEthVlanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcAdminState.setStatus("current")
_CfprApFabricEthVlanPcDescr_Type = SnmpAdminString
_CfprApFabricEthVlanPcDescr_Object = MibTableColumn
cfprApFabricEthVlanPcDescr = _CfprApFabricEthVlanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 6),
    _CfprApFabricEthVlanPcDescr_Type()
)
cfprApFabricEthVlanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcDescr.setStatus("current")
_CfprApFabricEthVlanPcEpDn_Type = SnmpAdminString
_CfprApFabricEthVlanPcEpDn_Object = MibTableColumn
cfprApFabricEthVlanPcEpDn = _CfprApFabricEthVlanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 7),
    _CfprApFabricEthVlanPcEpDn_Type()
)
cfprApFabricEthVlanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcEpDn.setStatus("current")
_CfprApFabricEthVlanPcFltAggr_Type = Unsigned64
_CfprApFabricEthVlanPcFltAggr_Object = MibTableColumn
cfprApFabricEthVlanPcFltAggr = _CfprApFabricEthVlanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 8),
    _CfprApFabricEthVlanPcFltAggr_Type()
)
cfprApFabricEthVlanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcFltAggr.setStatus("current")
_CfprApFabricEthVlanPcIfRole_Type = CfprApFabricEstcPcIfRole
_CfprApFabricEthVlanPcIfRole_Object = MibTableColumn
cfprApFabricEthVlanPcIfRole = _CfprApFabricEthVlanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 9),
    _CfprApFabricEthVlanPcIfRole_Type()
)
cfprApFabricEthVlanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcIfRole.setStatus("current")
_CfprApFabricEthVlanPcIfType_Type = CfprApFabricCIoEpIfType
_CfprApFabricEthVlanPcIfType_Object = MibTableColumn
cfprApFabricEthVlanPcIfType = _CfprApFabricEthVlanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 10),
    _CfprApFabricEthVlanPcIfType_Type()
)
cfprApFabricEthVlanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcIfType.setStatus("current")
_CfprApFabricEthVlanPcIsNative_Type = TruthValue
_CfprApFabricEthVlanPcIsNative_Object = MibTableColumn
cfprApFabricEthVlanPcIsNative = _CfprApFabricEthVlanPcIsNative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 11),
    _CfprApFabricEthVlanPcIsNative_Type()
)
cfprApFabricEthVlanPcIsNative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcIsNative.setStatus("current")
_CfprApFabricEthVlanPcLocale_Type = CfprApFabricExternalPcLocale
_CfprApFabricEthVlanPcLocale_Object = MibTableColumn
cfprApFabricEthVlanPcLocale = _CfprApFabricEthVlanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 12),
    _CfprApFabricEthVlanPcLocale_Type()
)
cfprApFabricEthVlanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcLocale.setStatus("current")
_CfprApFabricEthVlanPcName_Type = SnmpAdminString
_CfprApFabricEthVlanPcName_Object = MibTableColumn
cfprApFabricEthVlanPcName = _CfprApFabricEthVlanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 13),
    _CfprApFabricEthVlanPcName_Type()
)
cfprApFabricEthVlanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcName.setStatus("current")
_CfprApFabricEthVlanPcOperSpeed_Type = CfprApPortEthSpeed
_CfprApFabricEthVlanPcOperSpeed_Object = MibTableColumn
cfprApFabricEthVlanPcOperSpeed = _CfprApFabricEthVlanPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 14),
    _CfprApFabricEthVlanPcOperSpeed_Type()
)
cfprApFabricEthVlanPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcOperSpeed.setStatus("current")
_CfprApFabricEthVlanPcOperState_Type = CfprApNetworkPortOperState
_CfprApFabricEthVlanPcOperState_Object = MibTableColumn
cfprApFabricEthVlanPcOperState = _CfprApFabricEthVlanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 15),
    _CfprApFabricEthVlanPcOperState_Type()
)
cfprApFabricEthVlanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcOperState.setStatus("current")
_CfprApFabricEthVlanPcPeerDn_Type = SnmpAdminString
_CfprApFabricEthVlanPcPeerDn_Object = MibTableColumn
cfprApFabricEthVlanPcPeerDn = _CfprApFabricEthVlanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 16),
    _CfprApFabricEthVlanPcPeerDn_Type()
)
cfprApFabricEthVlanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcPeerDn.setStatus("current")
_CfprApFabricEthVlanPcPortId_Type = Gauge32
_CfprApFabricEthVlanPcPortId_Object = MibTableColumn
cfprApFabricEthVlanPcPortId = _CfprApFabricEthVlanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 17),
    _CfprApFabricEthVlanPcPortId_Type()
)
cfprApFabricEthVlanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcPortId.setStatus("current")
_CfprApFabricEthVlanPcStateQual_Type = SnmpAdminString
_CfprApFabricEthVlanPcStateQual_Object = MibTableColumn
cfprApFabricEthVlanPcStateQual = _CfprApFabricEthVlanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 18),
    _CfprApFabricEthVlanPcStateQual_Type()
)
cfprApFabricEthVlanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcStateQual.setStatus("current")
_CfprApFabricEthVlanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthVlanPcSwitchId_Object = MibTableColumn
cfprApFabricEthVlanPcSwitchId = _CfprApFabricEthVlanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 19),
    _CfprApFabricEthVlanPcSwitchId_Type()
)
cfprApFabricEthVlanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcSwitchId.setStatus("current")
_CfprApFabricEthVlanPcTransport_Type = CfprApFabricEthVlanPcTransport
_CfprApFabricEthVlanPcTransport_Object = MibTableColumn
cfprApFabricEthVlanPcTransport = _CfprApFabricEthVlanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 20),
    _CfprApFabricEthVlanPcTransport_Type()
)
cfprApFabricEthVlanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcTransport.setStatus("current")
_CfprApFabricEthVlanPcType_Type = CfprApFabricEstcPcType
_CfprApFabricEthVlanPcType_Object = MibTableColumn
cfprApFabricEthVlanPcType = _CfprApFabricEthVlanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 21),
    _CfprApFabricEthVlanPcType_Type()
)
cfprApFabricEthVlanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcType.setStatus("current")
_CfprApFabricEthVlanPcWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthVlanPcWarnings_Object = MibTableColumn
cfprApFabricEthVlanPcWarnings = _CfprApFabricEthVlanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 40, 1, 22),
    _CfprApFabricEthVlanPcWarnings_Type()
)
cfprApFabricEthVlanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPcWarnings.setStatus("current")
_CfprApFabricEthVlanPortEpTable_Object = MibTable
cfprApFabricEthVlanPortEpTable = _CfprApFabricEthVlanPortEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41)
)
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpTable.setStatus("current")
_CfprApFabricEthVlanPortEpEntry_Object = MibTableRow
cfprApFabricEthVlanPortEpEntry = _CfprApFabricEthVlanPortEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1)
)
cfprApFabricEthVlanPortEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricEthVlanPortEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpEntry.setStatus("current")
_CfprApFabricEthVlanPortEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricEthVlanPortEpInstanceId_Object = MibTableColumn
cfprApFabricEthVlanPortEpInstanceId = _CfprApFabricEthVlanPortEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 1),
    _CfprApFabricEthVlanPortEpInstanceId_Type()
)
cfprApFabricEthVlanPortEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpInstanceId.setStatus("current")
_CfprApFabricEthVlanPortEpDn_Type = CfprApManagedObjectDn
_CfprApFabricEthVlanPortEpDn_Object = MibTableColumn
cfprApFabricEthVlanPortEpDn = _CfprApFabricEthVlanPortEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 2),
    _CfprApFabricEthVlanPortEpDn_Type()
)
cfprApFabricEthVlanPortEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpDn.setStatus("current")
_CfprApFabricEthVlanPortEpRn_Type = SnmpAdminString
_CfprApFabricEthVlanPortEpRn_Object = MibTableColumn
cfprApFabricEthVlanPortEpRn = _CfprApFabricEthVlanPortEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 3),
    _CfprApFabricEthVlanPortEpRn_Type()
)
cfprApFabricEthVlanPortEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpRn.setStatus("current")
_CfprApFabricEthVlanPortEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricEthVlanPortEpAdminState_Object = MibTableColumn
cfprApFabricEthVlanPortEpAdminState = _CfprApFabricEthVlanPortEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 4),
    _CfprApFabricEthVlanPortEpAdminState_Type()
)
cfprApFabricEthVlanPortEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpAdminState.setStatus("current")
_CfprApFabricEthVlanPortEpAggrPortId_Type = Gauge32
_CfprApFabricEthVlanPortEpAggrPortId_Object = MibTableColumn
cfprApFabricEthVlanPortEpAggrPortId = _CfprApFabricEthVlanPortEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 5),
    _CfprApFabricEthVlanPortEpAggrPortId_Type()
)
cfprApFabricEthVlanPortEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpAggrPortId.setStatus("current")
_CfprApFabricEthVlanPortEpChassisId_Type = Gauge32
_CfprApFabricEthVlanPortEpChassisId_Object = MibTableColumn
cfprApFabricEthVlanPortEpChassisId = _CfprApFabricEthVlanPortEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 6),
    _CfprApFabricEthVlanPortEpChassisId_Type()
)
cfprApFabricEthVlanPortEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpChassisId.setStatus("current")
_CfprApFabricEthVlanPortEpEpDn_Type = SnmpAdminString
_CfprApFabricEthVlanPortEpEpDn_Object = MibTableColumn
cfprApFabricEthVlanPortEpEpDn = _CfprApFabricEthVlanPortEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 7),
    _CfprApFabricEthVlanPortEpEpDn_Type()
)
cfprApFabricEthVlanPortEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpEpDn.setStatus("current")
_CfprApFabricEthVlanPortEpFltAggr_Type = Unsigned64
_CfprApFabricEthVlanPortEpFltAggr_Object = MibTableColumn
cfprApFabricEthVlanPortEpFltAggr = _CfprApFabricEthVlanPortEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 8),
    _CfprApFabricEthVlanPortEpFltAggr_Type()
)
cfprApFabricEthVlanPortEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpFltAggr.setStatus("current")
_CfprApFabricEthVlanPortEpIfRole_Type = CfprApFabricLanEpIfRole
_CfprApFabricEthVlanPortEpIfRole_Object = MibTableColumn
cfprApFabricEthVlanPortEpIfRole = _CfprApFabricEthVlanPortEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 9),
    _CfprApFabricEthVlanPortEpIfRole_Type()
)
cfprApFabricEthVlanPortEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpIfRole.setStatus("current")
_CfprApFabricEthVlanPortEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricEthVlanPortEpIfType_Object = MibTableColumn
cfprApFabricEthVlanPortEpIfType = _CfprApFabricEthVlanPortEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 10),
    _CfprApFabricEthVlanPortEpIfType_Type()
)
cfprApFabricEthVlanPortEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpIfType.setStatus("current")
_CfprApFabricEthVlanPortEpIsNative_Type = TruthValue
_CfprApFabricEthVlanPortEpIsNative_Object = MibTableColumn
cfprApFabricEthVlanPortEpIsNative = _CfprApFabricEthVlanPortEpIsNative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 11),
    _CfprApFabricEthVlanPortEpIsNative_Type()
)
cfprApFabricEthVlanPortEpIsNative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpIsNative.setStatus("current")
_CfprApFabricEthVlanPortEpLicGP_Type = Unsigned64
_CfprApFabricEthVlanPortEpLicGP_Object = MibTableColumn
cfprApFabricEthVlanPortEpLicGP = _CfprApFabricEthVlanPortEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 12),
    _CfprApFabricEthVlanPortEpLicGP_Type()
)
cfprApFabricEthVlanPortEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpLicGP.setStatus("current")
_CfprApFabricEthVlanPortEpLicState_Type = CfprApLicenseState
_CfprApFabricEthVlanPortEpLicState_Object = MibTableColumn
cfprApFabricEthVlanPortEpLicState = _CfprApFabricEthVlanPortEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 13),
    _CfprApFabricEthVlanPortEpLicState_Type()
)
cfprApFabricEthVlanPortEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpLicState.setStatus("current")
_CfprApFabricEthVlanPortEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricEthVlanPortEpLocale_Object = MibTableColumn
cfprApFabricEthVlanPortEpLocale = _CfprApFabricEthVlanPortEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 14),
    _CfprApFabricEthVlanPortEpLocale_Type()
)
cfprApFabricEthVlanPortEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpLocale.setStatus("current")
_CfprApFabricEthVlanPortEpName_Type = SnmpAdminString
_CfprApFabricEthVlanPortEpName_Object = MibTableColumn
cfprApFabricEthVlanPortEpName = _CfprApFabricEthVlanPortEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 15),
    _CfprApFabricEthVlanPortEpName_Type()
)
cfprApFabricEthVlanPortEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpName.setStatus("current")
_CfprApFabricEthVlanPortEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricEthVlanPortEpOperState_Object = MibTableColumn
cfprApFabricEthVlanPortEpOperState = _CfprApFabricEthVlanPortEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 16),
    _CfprApFabricEthVlanPortEpOperState_Type()
)
cfprApFabricEthVlanPortEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpOperState.setStatus("current")
_CfprApFabricEthVlanPortEpOperStateReason_Type = SnmpAdminString
_CfprApFabricEthVlanPortEpOperStateReason_Object = MibTableColumn
cfprApFabricEthVlanPortEpOperStateReason = _CfprApFabricEthVlanPortEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 17),
    _CfprApFabricEthVlanPortEpOperStateReason_Type()
)
cfprApFabricEthVlanPortEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpOperStateReason.setStatus("current")
_CfprApFabricEthVlanPortEpPeerAggrPortId_Type = Gauge32
_CfprApFabricEthVlanPortEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricEthVlanPortEpPeerAggrPortId = _CfprApFabricEthVlanPortEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 18),
    _CfprApFabricEthVlanPortEpPeerAggrPortId_Type()
)
cfprApFabricEthVlanPortEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpPeerAggrPortId.setStatus("current")
_CfprApFabricEthVlanPortEpPeerChassisId_Type = Gauge32
_CfprApFabricEthVlanPortEpPeerChassisId_Object = MibTableColumn
cfprApFabricEthVlanPortEpPeerChassisId = _CfprApFabricEthVlanPortEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 19),
    _CfprApFabricEthVlanPortEpPeerChassisId_Type()
)
cfprApFabricEthVlanPortEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpPeerChassisId.setStatus("current")
_CfprApFabricEthVlanPortEpPeerDn_Type = SnmpAdminString
_CfprApFabricEthVlanPortEpPeerDn_Object = MibTableColumn
cfprApFabricEthVlanPortEpPeerDn = _CfprApFabricEthVlanPortEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 20),
    _CfprApFabricEthVlanPortEpPeerDn_Type()
)
cfprApFabricEthVlanPortEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpPeerDn.setStatus("current")
_CfprApFabricEthVlanPortEpPeerPortId_Type = Gauge32
_CfprApFabricEthVlanPortEpPeerPortId_Object = MibTableColumn
cfprApFabricEthVlanPortEpPeerPortId = _CfprApFabricEthVlanPortEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 21),
    _CfprApFabricEthVlanPortEpPeerPortId_Type()
)
cfprApFabricEthVlanPortEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpPeerPortId.setStatus("current")
_CfprApFabricEthVlanPortEpPeerSlotId_Type = Gauge32
_CfprApFabricEthVlanPortEpPeerSlotId_Object = MibTableColumn
cfprApFabricEthVlanPortEpPeerSlotId = _CfprApFabricEthVlanPortEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 22),
    _CfprApFabricEthVlanPortEpPeerSlotId_Type()
)
cfprApFabricEthVlanPortEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpPeerSlotId.setStatus("current")
_CfprApFabricEthVlanPortEpPortId_Type = Gauge32
_CfprApFabricEthVlanPortEpPortId_Object = MibTableColumn
cfprApFabricEthVlanPortEpPortId = _CfprApFabricEthVlanPortEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 23),
    _CfprApFabricEthVlanPortEpPortId_Type()
)
cfprApFabricEthVlanPortEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpPortId.setStatus("current")
_CfprApFabricEthVlanPortEpSlotId_Type = Gauge32
_CfprApFabricEthVlanPortEpSlotId_Object = MibTableColumn
cfprApFabricEthVlanPortEpSlotId = _CfprApFabricEthVlanPortEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 24),
    _CfprApFabricEthVlanPortEpSlotId_Type()
)
cfprApFabricEthVlanPortEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpSlotId.setStatus("current")
_CfprApFabricEthVlanPortEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricEthVlanPortEpSwitchId_Object = MibTableColumn
cfprApFabricEthVlanPortEpSwitchId = _CfprApFabricEthVlanPortEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 25),
    _CfprApFabricEthVlanPortEpSwitchId_Type()
)
cfprApFabricEthVlanPortEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpSwitchId.setStatus("current")
_CfprApFabricEthVlanPortEpTransport_Type = CfprApFabricAEthLanEpTransport
_CfprApFabricEthVlanPortEpTransport_Object = MibTableColumn
cfprApFabricEthVlanPortEpTransport = _CfprApFabricEthVlanPortEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 26),
    _CfprApFabricEthVlanPortEpTransport_Type()
)
cfprApFabricEthVlanPortEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpTransport.setStatus("current")
_CfprApFabricEthVlanPortEpType_Type = CfprApFabricLanEpType
_CfprApFabricEthVlanPortEpType_Object = MibTableColumn
cfprApFabricEthVlanPortEpType = _CfprApFabricEthVlanPortEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 27),
    _CfprApFabricEthVlanPortEpType_Type()
)
cfprApFabricEthVlanPortEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpType.setStatus("current")
_CfprApFabricEthVlanPortEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricEthVlanPortEpWarnings_Object = MibTableColumn
cfprApFabricEthVlanPortEpWarnings = _CfprApFabricEthVlanPortEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 41, 1, 28),
    _CfprApFabricEthVlanPortEpWarnings_Type()
)
cfprApFabricEthVlanPortEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricEthVlanPortEpWarnings.setStatus("current")
_CfprApFabricFcSanTable_Object = MibTable
cfprApFabricFcSanTable = _CfprApFabricFcSanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52)
)
if mibBuilder.loadTexts:
    cfprApFabricFcSanTable.setStatus("current")
_CfprApFabricFcSanEntry_Object = MibTableRow
cfprApFabricFcSanEntry = _CfprApFabricFcSanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1)
)
cfprApFabricFcSanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcSanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcSanEntry.setStatus("current")
_CfprApFabricFcSanInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcSanInstanceId_Object = MibTableColumn
cfprApFabricFcSanInstanceId = _CfprApFabricFcSanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 1),
    _CfprApFabricFcSanInstanceId_Type()
)
cfprApFabricFcSanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcSanInstanceId.setStatus("current")
_CfprApFabricFcSanDn_Type = CfprApManagedObjectDn
_CfprApFabricFcSanDn_Object = MibTableColumn
cfprApFabricFcSanDn = _CfprApFabricFcSanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 2),
    _CfprApFabricFcSanDn_Type()
)
cfprApFabricFcSanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanDn.setStatus("current")
_CfprApFabricFcSanRn_Type = SnmpAdminString
_CfprApFabricFcSanRn_Object = MibTableColumn
cfprApFabricFcSanRn = _CfprApFabricFcSanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 3),
    _CfprApFabricFcSanRn_Type()
)
cfprApFabricFcSanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanRn.setStatus("current")
_CfprApFabricFcSanId_Type = CfprApNetworkSwitchId
_CfprApFabricFcSanId_Object = MibTableColumn
cfprApFabricFcSanId = _CfprApFabricFcSanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 4),
    _CfprApFabricFcSanId_Type()
)
cfprApFabricFcSanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanId.setStatus("current")
_CfprApFabricFcSanLocale_Type = CfprApFabricExternalLocale
_CfprApFabricFcSanLocale_Object = MibTableColumn
cfprApFabricFcSanLocale = _CfprApFabricFcSanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 5),
    _CfprApFabricFcSanLocale_Type()
)
cfprApFabricFcSanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanLocale.setStatus("current")
_CfprApFabricFcSanName_Type = SnmpAdminString
_CfprApFabricFcSanName_Object = MibTableColumn
cfprApFabricFcSanName = _CfprApFabricFcSanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 6),
    _CfprApFabricFcSanName_Type()
)
cfprApFabricFcSanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanName.setStatus("current")
_CfprApFabricFcSanTransport_Type = CfprApFabricFcSanTransport
_CfprApFabricFcSanTransport_Object = MibTableColumn
cfprApFabricFcSanTransport = _CfprApFabricFcSanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 7),
    _CfprApFabricFcSanTransport_Type()
)
cfprApFabricFcSanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanTransport.setStatus("current")
_CfprApFabricFcSanType_Type = CfprApFabricSanType
_CfprApFabricFcSanType_Object = MibTableColumn
cfprApFabricFcSanType = _CfprApFabricFcSanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 8),
    _CfprApFabricFcSanType_Type()
)
cfprApFabricFcSanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanType.setStatus("current")
_CfprApFabricFcSanUplinkTrunking_Type = CfprApFabricFcSanUplinkTrunking
_CfprApFabricFcSanUplinkTrunking_Object = MibTableColumn
cfprApFabricFcSanUplinkTrunking = _CfprApFabricFcSanUplinkTrunking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 52, 1, 9),
    _CfprApFabricFcSanUplinkTrunking_Type()
)
cfprApFabricFcSanUplinkTrunking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanUplinkTrunking.setStatus("current")
_CfprApFabricFcSanEpTable_Object = MibTable
cfprApFabricFcSanEpTable = _CfprApFabricFcSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53)
)
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpTable.setStatus("current")
_CfprApFabricFcSanEpEntry_Object = MibTableRow
cfprApFabricFcSanEpEntry = _CfprApFabricFcSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1)
)
cfprApFabricFcSanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpEntry.setStatus("current")
_CfprApFabricFcSanEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcSanEpInstanceId_Object = MibTableColumn
cfprApFabricFcSanEpInstanceId = _CfprApFabricFcSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 1),
    _CfprApFabricFcSanEpInstanceId_Type()
)
cfprApFabricFcSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpInstanceId.setStatus("current")
_CfprApFabricFcSanEpDn_Type = CfprApManagedObjectDn
_CfprApFabricFcSanEpDn_Object = MibTableColumn
cfprApFabricFcSanEpDn = _CfprApFabricFcSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 2),
    _CfprApFabricFcSanEpDn_Type()
)
cfprApFabricFcSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpDn.setStatus("current")
_CfprApFabricFcSanEpRn_Type = SnmpAdminString
_CfprApFabricFcSanEpRn_Object = MibTableColumn
cfprApFabricFcSanEpRn = _CfprApFabricFcSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 3),
    _CfprApFabricFcSanEpRn_Type()
)
cfprApFabricFcSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpRn.setStatus("current")
_CfprApFabricFcSanEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricFcSanEpAdminState_Object = MibTableColumn
cfprApFabricFcSanEpAdminState = _CfprApFabricFcSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 4),
    _CfprApFabricFcSanEpAdminState_Type()
)
cfprApFabricFcSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpAdminState.setStatus("current")
_CfprApFabricFcSanEpAggrPortId_Type = Gauge32
_CfprApFabricFcSanEpAggrPortId_Object = MibTableColumn
cfprApFabricFcSanEpAggrPortId = _CfprApFabricFcSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 5),
    _CfprApFabricFcSanEpAggrPortId_Type()
)
cfprApFabricFcSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpAggrPortId.setStatus("current")
_CfprApFabricFcSanEpChassisId_Type = Gauge32
_CfprApFabricFcSanEpChassisId_Object = MibTableColumn
cfprApFabricFcSanEpChassisId = _CfprApFabricFcSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 6),
    _CfprApFabricFcSanEpChassisId_Type()
)
cfprApFabricFcSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpChassisId.setStatus("current")
_CfprApFabricFcSanEpEpDn_Type = SnmpAdminString
_CfprApFabricFcSanEpEpDn_Object = MibTableColumn
cfprApFabricFcSanEpEpDn = _CfprApFabricFcSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 7),
    _CfprApFabricFcSanEpEpDn_Type()
)
cfprApFabricFcSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpEpDn.setStatus("current")
_CfprApFabricFcSanEpFillPattern_Type = CfprApFabricFillPattern
_CfprApFabricFcSanEpFillPattern_Object = MibTableColumn
cfprApFabricFcSanEpFillPattern = _CfprApFabricFcSanEpFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 8),
    _CfprApFabricFcSanEpFillPattern_Type()
)
cfprApFabricFcSanEpFillPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpFillPattern.setStatus("current")
_CfprApFabricFcSanEpFltAggr_Type = Unsigned64
_CfprApFabricFcSanEpFltAggr_Object = MibTableColumn
cfprApFabricFcSanEpFltAggr = _CfprApFabricFcSanEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 9),
    _CfprApFabricFcSanEpFltAggr_Type()
)
cfprApFabricFcSanEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpFltAggr.setStatus("current")
_CfprApFabricFcSanEpIfRole_Type = CfprApFabricSanEpIfRole
_CfprApFabricFcSanEpIfRole_Object = MibTableColumn
cfprApFabricFcSanEpIfRole = _CfprApFabricFcSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 10),
    _CfprApFabricFcSanEpIfRole_Type()
)
cfprApFabricFcSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpIfRole.setStatus("current")
_CfprApFabricFcSanEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricFcSanEpIfType_Object = MibTableColumn
cfprApFabricFcSanEpIfType = _CfprApFabricFcSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 11),
    _CfprApFabricFcSanEpIfType_Type()
)
cfprApFabricFcSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpIfType.setStatus("current")
_CfprApFabricFcSanEpLicGP_Type = Unsigned64
_CfprApFabricFcSanEpLicGP_Object = MibTableColumn
cfprApFabricFcSanEpLicGP = _CfprApFabricFcSanEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 12),
    _CfprApFabricFcSanEpLicGP_Type()
)
cfprApFabricFcSanEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpLicGP.setStatus("current")
_CfprApFabricFcSanEpLicState_Type = CfprApLicenseState
_CfprApFabricFcSanEpLicState_Object = MibTableColumn
cfprApFabricFcSanEpLicState = _CfprApFabricFcSanEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 13),
    _CfprApFabricFcSanEpLicState_Type()
)
cfprApFabricFcSanEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpLicState.setStatus("current")
_CfprApFabricFcSanEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricFcSanEpLocale_Object = MibTableColumn
cfprApFabricFcSanEpLocale = _CfprApFabricFcSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 14),
    _CfprApFabricFcSanEpLocale_Type()
)
cfprApFabricFcSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpLocale.setStatus("current")
_CfprApFabricFcSanEpName_Type = SnmpAdminString
_CfprApFabricFcSanEpName_Object = MibTableColumn
cfprApFabricFcSanEpName = _CfprApFabricFcSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 15),
    _CfprApFabricFcSanEpName_Type()
)
cfprApFabricFcSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpName.setStatus("current")
_CfprApFabricFcSanEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricFcSanEpOperState_Object = MibTableColumn
cfprApFabricFcSanEpOperState = _CfprApFabricFcSanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 16),
    _CfprApFabricFcSanEpOperState_Type()
)
cfprApFabricFcSanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpOperState.setStatus("current")
_CfprApFabricFcSanEpOperStateReason_Type = SnmpAdminString
_CfprApFabricFcSanEpOperStateReason_Object = MibTableColumn
cfprApFabricFcSanEpOperStateReason = _CfprApFabricFcSanEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 17),
    _CfprApFabricFcSanEpOperStateReason_Type()
)
cfprApFabricFcSanEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpOperStateReason.setStatus("current")
_CfprApFabricFcSanEpPeerAggrPortId_Type = Gauge32
_CfprApFabricFcSanEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricFcSanEpPeerAggrPortId = _CfprApFabricFcSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 18),
    _CfprApFabricFcSanEpPeerAggrPortId_Type()
)
cfprApFabricFcSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpPeerAggrPortId.setStatus("current")
_CfprApFabricFcSanEpPeerChassisId_Type = Gauge32
_CfprApFabricFcSanEpPeerChassisId_Object = MibTableColumn
cfprApFabricFcSanEpPeerChassisId = _CfprApFabricFcSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 19),
    _CfprApFabricFcSanEpPeerChassisId_Type()
)
cfprApFabricFcSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpPeerChassisId.setStatus("current")
_CfprApFabricFcSanEpPeerDn_Type = SnmpAdminString
_CfprApFabricFcSanEpPeerDn_Object = MibTableColumn
cfprApFabricFcSanEpPeerDn = _CfprApFabricFcSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 20),
    _CfprApFabricFcSanEpPeerDn_Type()
)
cfprApFabricFcSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpPeerDn.setStatus("current")
_CfprApFabricFcSanEpPeerPortId_Type = Gauge32
_CfprApFabricFcSanEpPeerPortId_Object = MibTableColumn
cfprApFabricFcSanEpPeerPortId = _CfprApFabricFcSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 21),
    _CfprApFabricFcSanEpPeerPortId_Type()
)
cfprApFabricFcSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpPeerPortId.setStatus("current")
_CfprApFabricFcSanEpPeerSlotId_Type = Gauge32
_CfprApFabricFcSanEpPeerSlotId_Object = MibTableColumn
cfprApFabricFcSanEpPeerSlotId = _CfprApFabricFcSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 22),
    _CfprApFabricFcSanEpPeerSlotId_Type()
)
cfprApFabricFcSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpPeerSlotId.setStatus("current")
_CfprApFabricFcSanEpPortId_Type = CfprApFabricFcSanEpPortId
_CfprApFabricFcSanEpPortId_Object = MibTableColumn
cfprApFabricFcSanEpPortId = _CfprApFabricFcSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 23),
    _CfprApFabricFcSanEpPortId_Type()
)
cfprApFabricFcSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpPortId.setStatus("current")
_CfprApFabricFcSanEpSlotId_Type = CfprApFabricFcSanEpSlotId
_CfprApFabricFcSanEpSlotId_Object = MibTableColumn
cfprApFabricFcSanEpSlotId = _CfprApFabricFcSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 24),
    _CfprApFabricFcSanEpSlotId_Type()
)
cfprApFabricFcSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpSlotId.setStatus("current")
_CfprApFabricFcSanEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcSanEpSwitchId_Object = MibTableColumn
cfprApFabricFcSanEpSwitchId = _CfprApFabricFcSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 25),
    _CfprApFabricFcSanEpSwitchId_Type()
)
cfprApFabricFcSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpSwitchId.setStatus("current")
_CfprApFabricFcSanEpTransport_Type = CfprApFabricAFcSanEpTransport
_CfprApFabricFcSanEpTransport_Object = MibTableColumn
cfprApFabricFcSanEpTransport = _CfprApFabricFcSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 26),
    _CfprApFabricFcSanEpTransport_Type()
)
cfprApFabricFcSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpTransport.setStatus("current")
_CfprApFabricFcSanEpType_Type = CfprApFabricSanEpType
_CfprApFabricFcSanEpType_Object = MibTableColumn
cfprApFabricFcSanEpType = _CfprApFabricFcSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 27),
    _CfprApFabricFcSanEpType_Type()
)
cfprApFabricFcSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpType.setStatus("current")
_CfprApFabricFcSanEpUsrLbl_Type = SnmpAdminString
_CfprApFabricFcSanEpUsrLbl_Object = MibTableColumn
cfprApFabricFcSanEpUsrLbl = _CfprApFabricFcSanEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 28),
    _CfprApFabricFcSanEpUsrLbl_Type()
)
cfprApFabricFcSanEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpUsrLbl.setStatus("current")
_CfprApFabricFcSanEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcSanEpWarnings_Object = MibTableColumn
cfprApFabricFcSanEpWarnings = _CfprApFabricFcSanEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 53, 1, 29),
    _CfprApFabricFcSanEpWarnings_Type()
)
cfprApFabricFcSanEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanEpWarnings.setStatus("current")
_CfprApFabricFcSanPcTable_Object = MibTable
cfprApFabricFcSanPcTable = _CfprApFabricFcSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54)
)
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcTable.setStatus("current")
_CfprApFabricFcSanPcEntry_Object = MibTableRow
cfprApFabricFcSanPcEntry = _CfprApFabricFcSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1)
)
cfprApFabricFcSanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEntry.setStatus("current")
_CfprApFabricFcSanPcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcSanPcInstanceId_Object = MibTableColumn
cfprApFabricFcSanPcInstanceId = _CfprApFabricFcSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 1),
    _CfprApFabricFcSanPcInstanceId_Type()
)
cfprApFabricFcSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcInstanceId.setStatus("current")
_CfprApFabricFcSanPcDn_Type = CfprApManagedObjectDn
_CfprApFabricFcSanPcDn_Object = MibTableColumn
cfprApFabricFcSanPcDn = _CfprApFabricFcSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 2),
    _CfprApFabricFcSanPcDn_Type()
)
cfprApFabricFcSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcDn.setStatus("current")
_CfprApFabricFcSanPcRn_Type = SnmpAdminString
_CfprApFabricFcSanPcRn_Object = MibTableColumn
cfprApFabricFcSanPcRn = _CfprApFabricFcSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 3),
    _CfprApFabricFcSanPcRn_Type()
)
cfprApFabricFcSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcRn.setStatus("current")
_CfprApFabricFcSanPcAdminSpeed_Type = CfprApPortSpeed
_CfprApFabricFcSanPcAdminSpeed_Object = MibTableColumn
cfprApFabricFcSanPcAdminSpeed = _CfprApFabricFcSanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 4),
    _CfprApFabricFcSanPcAdminSpeed_Type()
)
cfprApFabricFcSanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcAdminSpeed.setStatus("current")
_CfprApFabricFcSanPcAdminState_Type = CfprApFabricCIoEpAdminState
_CfprApFabricFcSanPcAdminState_Object = MibTableColumn
cfprApFabricFcSanPcAdminState = _CfprApFabricFcSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 5),
    _CfprApFabricFcSanPcAdminState_Type()
)
cfprApFabricFcSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcAdminState.setStatus("current")
_CfprApFabricFcSanPcConfigState_Type = CfprApFabricConfigState
_CfprApFabricFcSanPcConfigState_Object = MibTableColumn
cfprApFabricFcSanPcConfigState = _CfprApFabricFcSanPcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 6),
    _CfprApFabricFcSanPcConfigState_Type()
)
cfprApFabricFcSanPcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcConfigState.setStatus("current")
_CfprApFabricFcSanPcConfigStatus_Type = CfprApFabricPcConfigStatus
_CfprApFabricFcSanPcConfigStatus_Object = MibTableColumn
cfprApFabricFcSanPcConfigStatus = _CfprApFabricFcSanPcConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 7),
    _CfprApFabricFcSanPcConfigStatus_Type()
)
cfprApFabricFcSanPcConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcConfigStatus.setStatus("current")
_CfprApFabricFcSanPcDescr_Type = SnmpAdminString
_CfprApFabricFcSanPcDescr_Object = MibTableColumn
cfprApFabricFcSanPcDescr = _CfprApFabricFcSanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 8),
    _CfprApFabricFcSanPcDescr_Type()
)
cfprApFabricFcSanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcDescr.setStatus("current")
_CfprApFabricFcSanPcEpDn_Type = SnmpAdminString
_CfprApFabricFcSanPcEpDn_Object = MibTableColumn
cfprApFabricFcSanPcEpDn = _CfprApFabricFcSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 9),
    _CfprApFabricFcSanPcEpDn_Type()
)
cfprApFabricFcSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpDn.setStatus("current")
_CfprApFabricFcSanPcFltAggr_Type = Unsigned64
_CfprApFabricFcSanPcFltAggr_Object = MibTableColumn
cfprApFabricFcSanPcFltAggr = _CfprApFabricFcSanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 10),
    _CfprApFabricFcSanPcFltAggr_Type()
)
cfprApFabricFcSanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcFltAggr.setStatus("current")
_CfprApFabricFcSanPcIfRole_Type = CfprApFabricSanPcIfRole
_CfprApFabricFcSanPcIfRole_Object = MibTableColumn
cfprApFabricFcSanPcIfRole = _CfprApFabricFcSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 11),
    _CfprApFabricFcSanPcIfRole_Type()
)
cfprApFabricFcSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcIfRole.setStatus("current")
_CfprApFabricFcSanPcIfType_Type = CfprApFabricCIoEpIfType
_CfprApFabricFcSanPcIfType_Object = MibTableColumn
cfprApFabricFcSanPcIfType = _CfprApFabricFcSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 12),
    _CfprApFabricFcSanPcIfType_Type()
)
cfprApFabricFcSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcIfType.setStatus("current")
_CfprApFabricFcSanPcLocale_Type = CfprApFabricExternalPcLocale
_CfprApFabricFcSanPcLocale_Object = MibTableColumn
cfprApFabricFcSanPcLocale = _CfprApFabricFcSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 13),
    _CfprApFabricFcSanPcLocale_Type()
)
cfprApFabricFcSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcLocale.setStatus("current")
_CfprApFabricFcSanPcName_Type = SnmpAdminString
_CfprApFabricFcSanPcName_Object = MibTableColumn
cfprApFabricFcSanPcName = _CfprApFabricFcSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 14),
    _CfprApFabricFcSanPcName_Type()
)
cfprApFabricFcSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcName.setStatus("current")
_CfprApFabricFcSanPcOperSpeed_Type = Gauge32
_CfprApFabricFcSanPcOperSpeed_Object = MibTableColumn
cfprApFabricFcSanPcOperSpeed = _CfprApFabricFcSanPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 15),
    _CfprApFabricFcSanPcOperSpeed_Type()
)
cfprApFabricFcSanPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcOperSpeed.setStatus("current")
_CfprApFabricFcSanPcOperState_Type = CfprApNetworkPortOperState
_CfprApFabricFcSanPcOperState_Object = MibTableColumn
cfprApFabricFcSanPcOperState = _CfprApFabricFcSanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 16),
    _CfprApFabricFcSanPcOperState_Type()
)
cfprApFabricFcSanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcOperState.setStatus("current")
_CfprApFabricFcSanPcPeerDn_Type = SnmpAdminString
_CfprApFabricFcSanPcPeerDn_Object = MibTableColumn
cfprApFabricFcSanPcPeerDn = _CfprApFabricFcSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 17),
    _CfprApFabricFcSanPcPeerDn_Type()
)
cfprApFabricFcSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcPeerDn.setStatus("current")
_CfprApFabricFcSanPcPortId_Type = Gauge32
_CfprApFabricFcSanPcPortId_Object = MibTableColumn
cfprApFabricFcSanPcPortId = _CfprApFabricFcSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 18),
    _CfprApFabricFcSanPcPortId_Type()
)
cfprApFabricFcSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcPortId.setStatus("current")
_CfprApFabricFcSanPcStateQual_Type = SnmpAdminString
_CfprApFabricFcSanPcStateQual_Object = MibTableColumn
cfprApFabricFcSanPcStateQual = _CfprApFabricFcSanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 19),
    _CfprApFabricFcSanPcStateQual_Type()
)
cfprApFabricFcSanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcStateQual.setStatus("current")
_CfprApFabricFcSanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcSanPcSwitchId_Object = MibTableColumn
cfprApFabricFcSanPcSwitchId = _CfprApFabricFcSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 20),
    _CfprApFabricFcSanPcSwitchId_Type()
)
cfprApFabricFcSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcSwitchId.setStatus("current")
_CfprApFabricFcSanPcTransport_Type = CfprApFabricFcSanPcTransport
_CfprApFabricFcSanPcTransport_Object = MibTableColumn
cfprApFabricFcSanPcTransport = _CfprApFabricFcSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 21),
    _CfprApFabricFcSanPcTransport_Type()
)
cfprApFabricFcSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcTransport.setStatus("current")
_CfprApFabricFcSanPcType_Type = CfprApFabricSanPcType
_CfprApFabricFcSanPcType_Object = MibTableColumn
cfprApFabricFcSanPcType = _CfprApFabricFcSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 22),
    _CfprApFabricFcSanPcType_Type()
)
cfprApFabricFcSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcType.setStatus("current")
_CfprApFabricFcSanPcWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcSanPcWarnings_Object = MibTableColumn
cfprApFabricFcSanPcWarnings = _CfprApFabricFcSanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 54, 1, 23),
    _CfprApFabricFcSanPcWarnings_Type()
)
cfprApFabricFcSanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcWarnings.setStatus("current")
_CfprApFabricFcSanPcEpTable_Object = MibTable
cfprApFabricFcSanPcEpTable = _CfprApFabricFcSanPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55)
)
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpTable.setStatus("current")
_CfprApFabricFcSanPcEpEntry_Object = MibTableRow
cfprApFabricFcSanPcEpEntry = _CfprApFabricFcSanPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1)
)
cfprApFabricFcSanPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcSanPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpEntry.setStatus("current")
_CfprApFabricFcSanPcEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcSanPcEpInstanceId_Object = MibTableColumn
cfprApFabricFcSanPcEpInstanceId = _CfprApFabricFcSanPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 1),
    _CfprApFabricFcSanPcEpInstanceId_Type()
)
cfprApFabricFcSanPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpInstanceId.setStatus("current")
_CfprApFabricFcSanPcEpDnData_Type = CfprApManagedObjectDn
_CfprApFabricFcSanPcEpDnData_Object = MibTableColumn
cfprApFabricFcSanPcEpDnData = _CfprApFabricFcSanPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 2),
    _CfprApFabricFcSanPcEpDnData_Type()
)
cfprApFabricFcSanPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpDnData.setStatus("current")
_CfprApFabricFcSanPcEpRn_Type = SnmpAdminString
_CfprApFabricFcSanPcEpRn_Object = MibTableColumn
cfprApFabricFcSanPcEpRn = _CfprApFabricFcSanPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 3),
    _CfprApFabricFcSanPcEpRn_Type()
)
cfprApFabricFcSanPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpRn.setStatus("current")
_CfprApFabricFcSanPcEpAdminSpeed_Type = CfprApPortSpeed
_CfprApFabricFcSanPcEpAdminSpeed_Object = MibTableColumn
cfprApFabricFcSanPcEpAdminSpeed = _CfprApFabricFcSanPcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 4),
    _CfprApFabricFcSanPcEpAdminSpeed_Type()
)
cfprApFabricFcSanPcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpAdminSpeed.setStatus("current")
_CfprApFabricFcSanPcEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricFcSanPcEpAdminState_Object = MibTableColumn
cfprApFabricFcSanPcEpAdminState = _CfprApFabricFcSanPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 5),
    _CfprApFabricFcSanPcEpAdminState_Type()
)
cfprApFabricFcSanPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpAdminState.setStatus("current")
_CfprApFabricFcSanPcEpAggrPortId_Type = Gauge32
_CfprApFabricFcSanPcEpAggrPortId_Object = MibTableColumn
cfprApFabricFcSanPcEpAggrPortId = _CfprApFabricFcSanPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 6),
    _CfprApFabricFcSanPcEpAggrPortId_Type()
)
cfprApFabricFcSanPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpAggrPortId.setStatus("current")
_CfprApFabricFcSanPcEpChassisId_Type = Gauge32
_CfprApFabricFcSanPcEpChassisId_Object = MibTableColumn
cfprApFabricFcSanPcEpChassisId = _CfprApFabricFcSanPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 7),
    _CfprApFabricFcSanPcEpChassisId_Type()
)
cfprApFabricFcSanPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpChassisId.setStatus("current")
_CfprApFabricFcSanPcEpEpDn_Type = SnmpAdminString
_CfprApFabricFcSanPcEpEpDn_Object = MibTableColumn
cfprApFabricFcSanPcEpEpDn = _CfprApFabricFcSanPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 8),
    _CfprApFabricFcSanPcEpEpDn_Type()
)
cfprApFabricFcSanPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpEpDn.setStatus("current")
_CfprApFabricFcSanPcEpFillPattern_Type = CfprApFabricFillPattern
_CfprApFabricFcSanPcEpFillPattern_Object = MibTableColumn
cfprApFabricFcSanPcEpFillPattern = _CfprApFabricFcSanPcEpFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 9),
    _CfprApFabricFcSanPcEpFillPattern_Type()
)
cfprApFabricFcSanPcEpFillPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpFillPattern.setStatus("current")
_CfprApFabricFcSanPcEpFltAggr_Type = Unsigned64
_CfprApFabricFcSanPcEpFltAggr_Object = MibTableColumn
cfprApFabricFcSanPcEpFltAggr = _CfprApFabricFcSanPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 10),
    _CfprApFabricFcSanPcEpFltAggr_Type()
)
cfprApFabricFcSanPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpFltAggr.setStatus("current")
_CfprApFabricFcSanPcEpIfRole_Type = CfprApFabricSanEpIfRole
_CfprApFabricFcSanPcEpIfRole_Object = MibTableColumn
cfprApFabricFcSanPcEpIfRole = _CfprApFabricFcSanPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 11),
    _CfprApFabricFcSanPcEpIfRole_Type()
)
cfprApFabricFcSanPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpIfRole.setStatus("current")
_CfprApFabricFcSanPcEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricFcSanPcEpIfType_Object = MibTableColumn
cfprApFabricFcSanPcEpIfType = _CfprApFabricFcSanPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 12),
    _CfprApFabricFcSanPcEpIfType_Type()
)
cfprApFabricFcSanPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpIfType.setStatus("current")
_CfprApFabricFcSanPcEpLicGP_Type = Unsigned64
_CfprApFabricFcSanPcEpLicGP_Object = MibTableColumn
cfprApFabricFcSanPcEpLicGP = _CfprApFabricFcSanPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 13),
    _CfprApFabricFcSanPcEpLicGP_Type()
)
cfprApFabricFcSanPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpLicGP.setStatus("current")
_CfprApFabricFcSanPcEpLicState_Type = CfprApLicenseState
_CfprApFabricFcSanPcEpLicState_Object = MibTableColumn
cfprApFabricFcSanPcEpLicState = _CfprApFabricFcSanPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 14),
    _CfprApFabricFcSanPcEpLicState_Type()
)
cfprApFabricFcSanPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpLicState.setStatus("current")
_CfprApFabricFcSanPcEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricFcSanPcEpLocale_Object = MibTableColumn
cfprApFabricFcSanPcEpLocale = _CfprApFabricFcSanPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 15),
    _CfprApFabricFcSanPcEpLocale_Type()
)
cfprApFabricFcSanPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpLocale.setStatus("current")
_CfprApFabricFcSanPcEpMembership_Type = CfprApFabricMembershipStatus
_CfprApFabricFcSanPcEpMembership_Object = MibTableColumn
cfprApFabricFcSanPcEpMembership = _CfprApFabricFcSanPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 16),
    _CfprApFabricFcSanPcEpMembership_Type()
)
cfprApFabricFcSanPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpMembership.setStatus("current")
_CfprApFabricFcSanPcEpName_Type = SnmpAdminString
_CfprApFabricFcSanPcEpName_Object = MibTableColumn
cfprApFabricFcSanPcEpName = _CfprApFabricFcSanPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 17),
    _CfprApFabricFcSanPcEpName_Type()
)
cfprApFabricFcSanPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpName.setStatus("current")
_CfprApFabricFcSanPcEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricFcSanPcEpOperState_Object = MibTableColumn
cfprApFabricFcSanPcEpOperState = _CfprApFabricFcSanPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 18),
    _CfprApFabricFcSanPcEpOperState_Type()
)
cfprApFabricFcSanPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpOperState.setStatus("current")
_CfprApFabricFcSanPcEpOperStateReason_Type = SnmpAdminString
_CfprApFabricFcSanPcEpOperStateReason_Object = MibTableColumn
cfprApFabricFcSanPcEpOperStateReason = _CfprApFabricFcSanPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 19),
    _CfprApFabricFcSanPcEpOperStateReason_Type()
)
cfprApFabricFcSanPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpOperStateReason.setStatus("current")
_CfprApFabricFcSanPcEpPeerAggrPortId_Type = Gauge32
_CfprApFabricFcSanPcEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricFcSanPcEpPeerAggrPortId = _CfprApFabricFcSanPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 20),
    _CfprApFabricFcSanPcEpPeerAggrPortId_Type()
)
cfprApFabricFcSanPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpPeerAggrPortId.setStatus("current")
_CfprApFabricFcSanPcEpPeerChassisId_Type = Gauge32
_CfprApFabricFcSanPcEpPeerChassisId_Object = MibTableColumn
cfprApFabricFcSanPcEpPeerChassisId = _CfprApFabricFcSanPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 21),
    _CfprApFabricFcSanPcEpPeerChassisId_Type()
)
cfprApFabricFcSanPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpPeerChassisId.setStatus("current")
_CfprApFabricFcSanPcEpPeerDn_Type = SnmpAdminString
_CfprApFabricFcSanPcEpPeerDn_Object = MibTableColumn
cfprApFabricFcSanPcEpPeerDn = _CfprApFabricFcSanPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 22),
    _CfprApFabricFcSanPcEpPeerDn_Type()
)
cfprApFabricFcSanPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpPeerDn.setStatus("current")
_CfprApFabricFcSanPcEpPeerPortId_Type = Gauge32
_CfprApFabricFcSanPcEpPeerPortId_Object = MibTableColumn
cfprApFabricFcSanPcEpPeerPortId = _CfprApFabricFcSanPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 23),
    _CfprApFabricFcSanPcEpPeerPortId_Type()
)
cfprApFabricFcSanPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpPeerPortId.setStatus("current")
_CfprApFabricFcSanPcEpPeerSlotId_Type = Gauge32
_CfprApFabricFcSanPcEpPeerSlotId_Object = MibTableColumn
cfprApFabricFcSanPcEpPeerSlotId = _CfprApFabricFcSanPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 24),
    _CfprApFabricFcSanPcEpPeerSlotId_Type()
)
cfprApFabricFcSanPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpPeerSlotId.setStatus("current")
_CfprApFabricFcSanPcEpPortId_Type = CfprApFabricFcSanPcEpPortId
_CfprApFabricFcSanPcEpPortId_Object = MibTableColumn
cfprApFabricFcSanPcEpPortId = _CfprApFabricFcSanPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 25),
    _CfprApFabricFcSanPcEpPortId_Type()
)
cfprApFabricFcSanPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpPortId.setStatus("current")
_CfprApFabricFcSanPcEpSlotId_Type = CfprApFabricFcSanPcEpSlotId
_CfprApFabricFcSanPcEpSlotId_Object = MibTableColumn
cfprApFabricFcSanPcEpSlotId = _CfprApFabricFcSanPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 26),
    _CfprApFabricFcSanPcEpSlotId_Type()
)
cfprApFabricFcSanPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpSlotId.setStatus("current")
_CfprApFabricFcSanPcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcSanPcEpSwitchId_Object = MibTableColumn
cfprApFabricFcSanPcEpSwitchId = _CfprApFabricFcSanPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 27),
    _CfprApFabricFcSanPcEpSwitchId_Type()
)
cfprApFabricFcSanPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpSwitchId.setStatus("current")
_CfprApFabricFcSanPcEpTransport_Type = CfprApFabricAFcSanEpTransport
_CfprApFabricFcSanPcEpTransport_Object = MibTableColumn
cfprApFabricFcSanPcEpTransport = _CfprApFabricFcSanPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 28),
    _CfprApFabricFcSanPcEpTransport_Type()
)
cfprApFabricFcSanPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpTransport.setStatus("current")
_CfprApFabricFcSanPcEpType_Type = CfprApFabricSanEpType
_CfprApFabricFcSanPcEpType_Object = MibTableColumn
cfprApFabricFcSanPcEpType = _CfprApFabricFcSanPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 29),
    _CfprApFabricFcSanPcEpType_Type()
)
cfprApFabricFcSanPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpType.setStatus("current")
_CfprApFabricFcSanPcEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcSanPcEpWarnings_Object = MibTableColumn
cfprApFabricFcSanPcEpWarnings = _CfprApFabricFcSanPcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 55, 1, 30),
    _CfprApFabricFcSanPcEpWarnings_Type()
)
cfprApFabricFcSanPcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcSanPcEpWarnings.setStatus("current")
_CfprApFabricFcVsanPcTable_Object = MibTable
cfprApFabricFcVsanPcTable = _CfprApFabricFcVsanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56)
)
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcTable.setStatus("current")
_CfprApFabricFcVsanPcEntry_Object = MibTableRow
cfprApFabricFcVsanPcEntry = _CfprApFabricFcVsanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1)
)
cfprApFabricFcVsanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcVsanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcEntry.setStatus("current")
_CfprApFabricFcVsanPcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcVsanPcInstanceId_Object = MibTableColumn
cfprApFabricFcVsanPcInstanceId = _CfprApFabricFcVsanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 1),
    _CfprApFabricFcVsanPcInstanceId_Type()
)
cfprApFabricFcVsanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcInstanceId.setStatus("current")
_CfprApFabricFcVsanPcDn_Type = CfprApManagedObjectDn
_CfprApFabricFcVsanPcDn_Object = MibTableColumn
cfprApFabricFcVsanPcDn = _CfprApFabricFcVsanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 2),
    _CfprApFabricFcVsanPcDn_Type()
)
cfprApFabricFcVsanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcDn.setStatus("current")
_CfprApFabricFcVsanPcRn_Type = SnmpAdminString
_CfprApFabricFcVsanPcRn_Object = MibTableColumn
cfprApFabricFcVsanPcRn = _CfprApFabricFcVsanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 3),
    _CfprApFabricFcVsanPcRn_Type()
)
cfprApFabricFcVsanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcRn.setStatus("current")
_CfprApFabricFcVsanPcAdminState_Type = CfprApFabricCIoEpAdminState
_CfprApFabricFcVsanPcAdminState_Object = MibTableColumn
cfprApFabricFcVsanPcAdminState = _CfprApFabricFcVsanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 4),
    _CfprApFabricFcVsanPcAdminState_Type()
)
cfprApFabricFcVsanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcAdminState.setStatus("current")
_CfprApFabricFcVsanPcDescr_Type = SnmpAdminString
_CfprApFabricFcVsanPcDescr_Object = MibTableColumn
cfprApFabricFcVsanPcDescr = _CfprApFabricFcVsanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 5),
    _CfprApFabricFcVsanPcDescr_Type()
)
cfprApFabricFcVsanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcDescr.setStatus("current")
_CfprApFabricFcVsanPcEpDn_Type = SnmpAdminString
_CfprApFabricFcVsanPcEpDn_Object = MibTableColumn
cfprApFabricFcVsanPcEpDn = _CfprApFabricFcVsanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 6),
    _CfprApFabricFcVsanPcEpDn_Type()
)
cfprApFabricFcVsanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcEpDn.setStatus("current")
_CfprApFabricFcVsanPcFltAggr_Type = Unsigned64
_CfprApFabricFcVsanPcFltAggr_Object = MibTableColumn
cfprApFabricFcVsanPcFltAggr = _CfprApFabricFcVsanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 7),
    _CfprApFabricFcVsanPcFltAggr_Type()
)
cfprApFabricFcVsanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcFltAggr.setStatus("current")
_CfprApFabricFcVsanPcIfRole_Type = CfprApFabricSanPcIfRole
_CfprApFabricFcVsanPcIfRole_Object = MibTableColumn
cfprApFabricFcVsanPcIfRole = _CfprApFabricFcVsanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 8),
    _CfprApFabricFcVsanPcIfRole_Type()
)
cfprApFabricFcVsanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcIfRole.setStatus("current")
_CfprApFabricFcVsanPcIfType_Type = CfprApFabricCIoEpIfType
_CfprApFabricFcVsanPcIfType_Object = MibTableColumn
cfprApFabricFcVsanPcIfType = _CfprApFabricFcVsanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 9),
    _CfprApFabricFcVsanPcIfType_Type()
)
cfprApFabricFcVsanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcIfType.setStatus("current")
_CfprApFabricFcVsanPcLocale_Type = CfprApFabricExternalPcLocale
_CfprApFabricFcVsanPcLocale_Object = MibTableColumn
cfprApFabricFcVsanPcLocale = _CfprApFabricFcVsanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 10),
    _CfprApFabricFcVsanPcLocale_Type()
)
cfprApFabricFcVsanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcLocale.setStatus("current")
_CfprApFabricFcVsanPcName_Type = SnmpAdminString
_CfprApFabricFcVsanPcName_Object = MibTableColumn
cfprApFabricFcVsanPcName = _CfprApFabricFcVsanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 11),
    _CfprApFabricFcVsanPcName_Type()
)
cfprApFabricFcVsanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcName.setStatus("current")
_CfprApFabricFcVsanPcOperState_Type = CfprApNetworkPortOperState
_CfprApFabricFcVsanPcOperState_Object = MibTableColumn
cfprApFabricFcVsanPcOperState = _CfprApFabricFcVsanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 12),
    _CfprApFabricFcVsanPcOperState_Type()
)
cfprApFabricFcVsanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcOperState.setStatus("current")
_CfprApFabricFcVsanPcPeerDn_Type = SnmpAdminString
_CfprApFabricFcVsanPcPeerDn_Object = MibTableColumn
cfprApFabricFcVsanPcPeerDn = _CfprApFabricFcVsanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 13),
    _CfprApFabricFcVsanPcPeerDn_Type()
)
cfprApFabricFcVsanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcPeerDn.setStatus("current")
_CfprApFabricFcVsanPcPortId_Type = Gauge32
_CfprApFabricFcVsanPcPortId_Object = MibTableColumn
cfprApFabricFcVsanPcPortId = _CfprApFabricFcVsanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 14),
    _CfprApFabricFcVsanPcPortId_Type()
)
cfprApFabricFcVsanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcPortId.setStatus("current")
_CfprApFabricFcVsanPcStateQual_Type = SnmpAdminString
_CfprApFabricFcVsanPcStateQual_Object = MibTableColumn
cfprApFabricFcVsanPcStateQual = _CfprApFabricFcVsanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 15),
    _CfprApFabricFcVsanPcStateQual_Type()
)
cfprApFabricFcVsanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcStateQual.setStatus("current")
_CfprApFabricFcVsanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcVsanPcSwitchId_Object = MibTableColumn
cfprApFabricFcVsanPcSwitchId = _CfprApFabricFcVsanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 16),
    _CfprApFabricFcVsanPcSwitchId_Type()
)
cfprApFabricFcVsanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcSwitchId.setStatus("current")
_CfprApFabricFcVsanPcTransport_Type = CfprApFabricFcVsanPcTransport
_CfprApFabricFcVsanPcTransport_Object = MibTableColumn
cfprApFabricFcVsanPcTransport = _CfprApFabricFcVsanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 17),
    _CfprApFabricFcVsanPcTransport_Type()
)
cfprApFabricFcVsanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcTransport.setStatus("current")
_CfprApFabricFcVsanPcType_Type = CfprApFabricSanPcType
_CfprApFabricFcVsanPcType_Object = MibTableColumn
cfprApFabricFcVsanPcType = _CfprApFabricFcVsanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 18),
    _CfprApFabricFcVsanPcType_Type()
)
cfprApFabricFcVsanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcType.setStatus("current")
_CfprApFabricFcVsanPcWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcVsanPcWarnings_Object = MibTableColumn
cfprApFabricFcVsanPcWarnings = _CfprApFabricFcVsanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 56, 1, 19),
    _CfprApFabricFcVsanPcWarnings_Type()
)
cfprApFabricFcVsanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPcWarnings.setStatus("current")
_CfprApFabricFcVsanPortEpTable_Object = MibTable
cfprApFabricFcVsanPortEpTable = _CfprApFabricFcVsanPortEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57)
)
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpTable.setStatus("current")
_CfprApFabricFcVsanPortEpEntry_Object = MibTableRow
cfprApFabricFcVsanPortEpEntry = _CfprApFabricFcVsanPortEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1)
)
cfprApFabricFcVsanPortEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcVsanPortEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpEntry.setStatus("current")
_CfprApFabricFcVsanPortEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcVsanPortEpInstanceId_Object = MibTableColumn
cfprApFabricFcVsanPortEpInstanceId = _CfprApFabricFcVsanPortEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 1),
    _CfprApFabricFcVsanPortEpInstanceId_Type()
)
cfprApFabricFcVsanPortEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpInstanceId.setStatus("current")
_CfprApFabricFcVsanPortEpDn_Type = CfprApManagedObjectDn
_CfprApFabricFcVsanPortEpDn_Object = MibTableColumn
cfprApFabricFcVsanPortEpDn = _CfprApFabricFcVsanPortEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 2),
    _CfprApFabricFcVsanPortEpDn_Type()
)
cfprApFabricFcVsanPortEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpDn.setStatus("current")
_CfprApFabricFcVsanPortEpRn_Type = SnmpAdminString
_CfprApFabricFcVsanPortEpRn_Object = MibTableColumn
cfprApFabricFcVsanPortEpRn = _CfprApFabricFcVsanPortEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 3),
    _CfprApFabricFcVsanPortEpRn_Type()
)
cfprApFabricFcVsanPortEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpRn.setStatus("current")
_CfprApFabricFcVsanPortEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricFcVsanPortEpAdminState_Object = MibTableColumn
cfprApFabricFcVsanPortEpAdminState = _CfprApFabricFcVsanPortEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 4),
    _CfprApFabricFcVsanPortEpAdminState_Type()
)
cfprApFabricFcVsanPortEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpAdminState.setStatus("current")
_CfprApFabricFcVsanPortEpAggrPortId_Type = Gauge32
_CfprApFabricFcVsanPortEpAggrPortId_Object = MibTableColumn
cfprApFabricFcVsanPortEpAggrPortId = _CfprApFabricFcVsanPortEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 5),
    _CfprApFabricFcVsanPortEpAggrPortId_Type()
)
cfprApFabricFcVsanPortEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpAggrPortId.setStatus("current")
_CfprApFabricFcVsanPortEpChassisId_Type = Gauge32
_CfprApFabricFcVsanPortEpChassisId_Object = MibTableColumn
cfprApFabricFcVsanPortEpChassisId = _CfprApFabricFcVsanPortEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 6),
    _CfprApFabricFcVsanPortEpChassisId_Type()
)
cfprApFabricFcVsanPortEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpChassisId.setStatus("current")
_CfprApFabricFcVsanPortEpEpDn_Type = SnmpAdminString
_CfprApFabricFcVsanPortEpEpDn_Object = MibTableColumn
cfprApFabricFcVsanPortEpEpDn = _CfprApFabricFcVsanPortEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 7),
    _CfprApFabricFcVsanPortEpEpDn_Type()
)
cfprApFabricFcVsanPortEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpEpDn.setStatus("current")
_CfprApFabricFcVsanPortEpFltAggr_Type = Unsigned64
_CfprApFabricFcVsanPortEpFltAggr_Object = MibTableColumn
cfprApFabricFcVsanPortEpFltAggr = _CfprApFabricFcVsanPortEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 8),
    _CfprApFabricFcVsanPortEpFltAggr_Type()
)
cfprApFabricFcVsanPortEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpFltAggr.setStatus("current")
_CfprApFabricFcVsanPortEpIfRole_Type = CfprApFabricSanEpIfRole
_CfprApFabricFcVsanPortEpIfRole_Object = MibTableColumn
cfprApFabricFcVsanPortEpIfRole = _CfprApFabricFcVsanPortEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 9),
    _CfprApFabricFcVsanPortEpIfRole_Type()
)
cfprApFabricFcVsanPortEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpIfRole.setStatus("current")
_CfprApFabricFcVsanPortEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricFcVsanPortEpIfType_Object = MibTableColumn
cfprApFabricFcVsanPortEpIfType = _CfprApFabricFcVsanPortEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 10),
    _CfprApFabricFcVsanPortEpIfType_Type()
)
cfprApFabricFcVsanPortEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpIfType.setStatus("current")
_CfprApFabricFcVsanPortEpLicGP_Type = Unsigned64
_CfprApFabricFcVsanPortEpLicGP_Object = MibTableColumn
cfprApFabricFcVsanPortEpLicGP = _CfprApFabricFcVsanPortEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 11),
    _CfprApFabricFcVsanPortEpLicGP_Type()
)
cfprApFabricFcVsanPortEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpLicGP.setStatus("current")
_CfprApFabricFcVsanPortEpLicState_Type = CfprApLicenseState
_CfprApFabricFcVsanPortEpLicState_Object = MibTableColumn
cfprApFabricFcVsanPortEpLicState = _CfprApFabricFcVsanPortEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 12),
    _CfprApFabricFcVsanPortEpLicState_Type()
)
cfprApFabricFcVsanPortEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpLicState.setStatus("current")
_CfprApFabricFcVsanPortEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricFcVsanPortEpLocale_Object = MibTableColumn
cfprApFabricFcVsanPortEpLocale = _CfprApFabricFcVsanPortEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 13),
    _CfprApFabricFcVsanPortEpLocale_Type()
)
cfprApFabricFcVsanPortEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpLocale.setStatus("current")
_CfprApFabricFcVsanPortEpName_Type = SnmpAdminString
_CfprApFabricFcVsanPortEpName_Object = MibTableColumn
cfprApFabricFcVsanPortEpName = _CfprApFabricFcVsanPortEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 14),
    _CfprApFabricFcVsanPortEpName_Type()
)
cfprApFabricFcVsanPortEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpName.setStatus("current")
_CfprApFabricFcVsanPortEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricFcVsanPortEpOperState_Object = MibTableColumn
cfprApFabricFcVsanPortEpOperState = _CfprApFabricFcVsanPortEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 15),
    _CfprApFabricFcVsanPortEpOperState_Type()
)
cfprApFabricFcVsanPortEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpOperState.setStatus("current")
_CfprApFabricFcVsanPortEpOperStateReason_Type = SnmpAdminString
_CfprApFabricFcVsanPortEpOperStateReason_Object = MibTableColumn
cfprApFabricFcVsanPortEpOperStateReason = _CfprApFabricFcVsanPortEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 16),
    _CfprApFabricFcVsanPortEpOperStateReason_Type()
)
cfprApFabricFcVsanPortEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpOperStateReason.setStatus("current")
_CfprApFabricFcVsanPortEpPeerAggrPortId_Type = Gauge32
_CfprApFabricFcVsanPortEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricFcVsanPortEpPeerAggrPortId = _CfprApFabricFcVsanPortEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 17),
    _CfprApFabricFcVsanPortEpPeerAggrPortId_Type()
)
cfprApFabricFcVsanPortEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpPeerAggrPortId.setStatus("current")
_CfprApFabricFcVsanPortEpPeerChassisId_Type = Gauge32
_CfprApFabricFcVsanPortEpPeerChassisId_Object = MibTableColumn
cfprApFabricFcVsanPortEpPeerChassisId = _CfprApFabricFcVsanPortEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 18),
    _CfprApFabricFcVsanPortEpPeerChassisId_Type()
)
cfprApFabricFcVsanPortEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpPeerChassisId.setStatus("current")
_CfprApFabricFcVsanPortEpPeerDn_Type = SnmpAdminString
_CfprApFabricFcVsanPortEpPeerDn_Object = MibTableColumn
cfprApFabricFcVsanPortEpPeerDn = _CfprApFabricFcVsanPortEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 19),
    _CfprApFabricFcVsanPortEpPeerDn_Type()
)
cfprApFabricFcVsanPortEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpPeerDn.setStatus("current")
_CfprApFabricFcVsanPortEpPeerPortId_Type = Gauge32
_CfprApFabricFcVsanPortEpPeerPortId_Object = MibTableColumn
cfprApFabricFcVsanPortEpPeerPortId = _CfprApFabricFcVsanPortEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 20),
    _CfprApFabricFcVsanPortEpPeerPortId_Type()
)
cfprApFabricFcVsanPortEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpPeerPortId.setStatus("current")
_CfprApFabricFcVsanPortEpPeerSlotId_Type = Gauge32
_CfprApFabricFcVsanPortEpPeerSlotId_Object = MibTableColumn
cfprApFabricFcVsanPortEpPeerSlotId = _CfprApFabricFcVsanPortEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 21),
    _CfprApFabricFcVsanPortEpPeerSlotId_Type()
)
cfprApFabricFcVsanPortEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpPeerSlotId.setStatus("current")
_CfprApFabricFcVsanPortEpPortId_Type = CfprApFabricFcVsanPortEpPortId
_CfprApFabricFcVsanPortEpPortId_Object = MibTableColumn
cfprApFabricFcVsanPortEpPortId = _CfprApFabricFcVsanPortEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 22),
    _CfprApFabricFcVsanPortEpPortId_Type()
)
cfprApFabricFcVsanPortEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpPortId.setStatus("current")
_CfprApFabricFcVsanPortEpSlotId_Type = CfprApFabricFcVsanPortEpSlotId
_CfprApFabricFcVsanPortEpSlotId_Object = MibTableColumn
cfprApFabricFcVsanPortEpSlotId = _CfprApFabricFcVsanPortEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 23),
    _CfprApFabricFcVsanPortEpSlotId_Type()
)
cfprApFabricFcVsanPortEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpSlotId.setStatus("current")
_CfprApFabricFcVsanPortEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcVsanPortEpSwitchId_Object = MibTableColumn
cfprApFabricFcVsanPortEpSwitchId = _CfprApFabricFcVsanPortEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 24),
    _CfprApFabricFcVsanPortEpSwitchId_Type()
)
cfprApFabricFcVsanPortEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpSwitchId.setStatus("current")
_CfprApFabricFcVsanPortEpTransport_Type = CfprApFabricAFcSanEpTransport
_CfprApFabricFcVsanPortEpTransport_Object = MibTableColumn
cfprApFabricFcVsanPortEpTransport = _CfprApFabricFcVsanPortEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 25),
    _CfprApFabricFcVsanPortEpTransport_Type()
)
cfprApFabricFcVsanPortEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpTransport.setStatus("current")
_CfprApFabricFcVsanPortEpType_Type = CfprApFabricSanEpType
_CfprApFabricFcVsanPortEpType_Object = MibTableColumn
cfprApFabricFcVsanPortEpType = _CfprApFabricFcVsanPortEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 26),
    _CfprApFabricFcVsanPortEpType_Type()
)
cfprApFabricFcVsanPortEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpType.setStatus("current")
_CfprApFabricFcVsanPortEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcVsanPortEpWarnings_Object = MibTableColumn
cfprApFabricFcVsanPortEpWarnings = _CfprApFabricFcVsanPortEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 57, 1, 27),
    _CfprApFabricFcVsanPortEpWarnings_Type()
)
cfprApFabricFcVsanPortEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcVsanPortEpWarnings.setStatus("current")
_CfprApFabricFcoeSanEpTable_Object = MibTable
cfprApFabricFcoeSanEpTable = _CfprApFabricFcoeSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59)
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpTable.setStatus("current")
_CfprApFabricFcoeSanEpEntry_Object = MibTableRow
cfprApFabricFcoeSanEpEntry = _CfprApFabricFcoeSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1)
)
cfprApFabricFcoeSanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcoeSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpEntry.setStatus("current")
_CfprApFabricFcoeSanEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcoeSanEpInstanceId_Object = MibTableColumn
cfprApFabricFcoeSanEpInstanceId = _CfprApFabricFcoeSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 1),
    _CfprApFabricFcoeSanEpInstanceId_Type()
)
cfprApFabricFcoeSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpInstanceId.setStatus("current")
_CfprApFabricFcoeSanEpDn_Type = CfprApManagedObjectDn
_CfprApFabricFcoeSanEpDn_Object = MibTableColumn
cfprApFabricFcoeSanEpDn = _CfprApFabricFcoeSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 2),
    _CfprApFabricFcoeSanEpDn_Type()
)
cfprApFabricFcoeSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpDn.setStatus("current")
_CfprApFabricFcoeSanEpRn_Type = SnmpAdminString
_CfprApFabricFcoeSanEpRn_Object = MibTableColumn
cfprApFabricFcoeSanEpRn = _CfprApFabricFcoeSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 3),
    _CfprApFabricFcoeSanEpRn_Type()
)
cfprApFabricFcoeSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpRn.setStatus("current")
_CfprApFabricFcoeSanEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricFcoeSanEpAdminState_Object = MibTableColumn
cfprApFabricFcoeSanEpAdminState = _CfprApFabricFcoeSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 4),
    _CfprApFabricFcoeSanEpAdminState_Type()
)
cfprApFabricFcoeSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpAdminState.setStatus("current")
_CfprApFabricFcoeSanEpAggrPortId_Type = Gauge32
_CfprApFabricFcoeSanEpAggrPortId_Object = MibTableColumn
cfprApFabricFcoeSanEpAggrPortId = _CfprApFabricFcoeSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 5),
    _CfprApFabricFcoeSanEpAggrPortId_Type()
)
cfprApFabricFcoeSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpAggrPortId.setStatus("current")
_CfprApFabricFcoeSanEpChassisId_Type = Gauge32
_CfprApFabricFcoeSanEpChassisId_Object = MibTableColumn
cfprApFabricFcoeSanEpChassisId = _CfprApFabricFcoeSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 6),
    _CfprApFabricFcoeSanEpChassisId_Type()
)
cfprApFabricFcoeSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpChassisId.setStatus("current")
_CfprApFabricFcoeSanEpConfigState_Type = CfprApFabricConfigState
_CfprApFabricFcoeSanEpConfigState_Object = MibTableColumn
cfprApFabricFcoeSanEpConfigState = _CfprApFabricFcoeSanEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 7),
    _CfprApFabricFcoeSanEpConfigState_Type()
)
cfprApFabricFcoeSanEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpConfigState.setStatus("current")
_CfprApFabricFcoeSanEpEpDn_Type = SnmpAdminString
_CfprApFabricFcoeSanEpEpDn_Object = MibTableColumn
cfprApFabricFcoeSanEpEpDn = _CfprApFabricFcoeSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 8),
    _CfprApFabricFcoeSanEpEpDn_Type()
)
cfprApFabricFcoeSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpEpDn.setStatus("current")
_CfprApFabricFcoeSanEpEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricFcoeSanEpEthLinkProfileName_Object = MibTableColumn
cfprApFabricFcoeSanEpEthLinkProfileName = _CfprApFabricFcoeSanEpEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 9),
    _CfprApFabricFcoeSanEpEthLinkProfileName_Type()
)
cfprApFabricFcoeSanEpEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpEthLinkProfileName.setStatus("current")
_CfprApFabricFcoeSanEpFcoeState_Type = CfprApNetworkPortOperState
_CfprApFabricFcoeSanEpFcoeState_Object = MibTableColumn
cfprApFabricFcoeSanEpFcoeState = _CfprApFabricFcoeSanEpFcoeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 10),
    _CfprApFabricFcoeSanEpFcoeState_Type()
)
cfprApFabricFcoeSanEpFcoeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpFcoeState.setStatus("current")
_CfprApFabricFcoeSanEpFcoeStateReason_Type = SnmpAdminString
_CfprApFabricFcoeSanEpFcoeStateReason_Object = MibTableColumn
cfprApFabricFcoeSanEpFcoeStateReason = _CfprApFabricFcoeSanEpFcoeStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 11),
    _CfprApFabricFcoeSanEpFcoeStateReason_Type()
)
cfprApFabricFcoeSanEpFcoeStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpFcoeStateReason.setStatus("current")
_CfprApFabricFcoeSanEpFltAggr_Type = Unsigned64
_CfprApFabricFcoeSanEpFltAggr_Object = MibTableColumn
cfprApFabricFcoeSanEpFltAggr = _CfprApFabricFcoeSanEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 12),
    _CfprApFabricFcoeSanEpFltAggr_Type()
)
cfprApFabricFcoeSanEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpFltAggr.setStatus("current")
_CfprApFabricFcoeSanEpIfRole_Type = CfprApFabricSanEpIfRole
_CfprApFabricFcoeSanEpIfRole_Object = MibTableColumn
cfprApFabricFcoeSanEpIfRole = _CfprApFabricFcoeSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 13),
    _CfprApFabricFcoeSanEpIfRole_Type()
)
cfprApFabricFcoeSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpIfRole.setStatus("current")
_CfprApFabricFcoeSanEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricFcoeSanEpIfType_Object = MibTableColumn
cfprApFabricFcoeSanEpIfType = _CfprApFabricFcoeSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 14),
    _CfprApFabricFcoeSanEpIfType_Type()
)
cfprApFabricFcoeSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpIfType.setStatus("current")
_CfprApFabricFcoeSanEpLicGP_Type = Unsigned64
_CfprApFabricFcoeSanEpLicGP_Object = MibTableColumn
cfprApFabricFcoeSanEpLicGP = _CfprApFabricFcoeSanEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 15),
    _CfprApFabricFcoeSanEpLicGP_Type()
)
cfprApFabricFcoeSanEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpLicGP.setStatus("current")
_CfprApFabricFcoeSanEpLicState_Type = CfprApLicenseState
_CfprApFabricFcoeSanEpLicState_Object = MibTableColumn
cfprApFabricFcoeSanEpLicState = _CfprApFabricFcoeSanEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 16),
    _CfprApFabricFcoeSanEpLicState_Type()
)
cfprApFabricFcoeSanEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpLicState.setStatus("current")
_CfprApFabricFcoeSanEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricFcoeSanEpLocale_Object = MibTableColumn
cfprApFabricFcoeSanEpLocale = _CfprApFabricFcoeSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 17),
    _CfprApFabricFcoeSanEpLocale_Type()
)
cfprApFabricFcoeSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpLocale.setStatus("current")
_CfprApFabricFcoeSanEpName_Type = SnmpAdminString
_CfprApFabricFcoeSanEpName_Object = MibTableColumn
cfprApFabricFcoeSanEpName = _CfprApFabricFcoeSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 18),
    _CfprApFabricFcoeSanEpName_Type()
)
cfprApFabricFcoeSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpName.setStatus("current")
_CfprApFabricFcoeSanEpOperEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricFcoeSanEpOperEthLinkProfileName_Object = MibTableColumn
cfprApFabricFcoeSanEpOperEthLinkProfileName = _CfprApFabricFcoeSanEpOperEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 19),
    _CfprApFabricFcoeSanEpOperEthLinkProfileName_Type()
)
cfprApFabricFcoeSanEpOperEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpOperEthLinkProfileName.setStatus("current")
_CfprApFabricFcoeSanEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricFcoeSanEpOperState_Object = MibTableColumn
cfprApFabricFcoeSanEpOperState = _CfprApFabricFcoeSanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 20),
    _CfprApFabricFcoeSanEpOperState_Type()
)
cfprApFabricFcoeSanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpOperState.setStatus("current")
_CfprApFabricFcoeSanEpOperStateReason_Type = SnmpAdminString
_CfprApFabricFcoeSanEpOperStateReason_Object = MibTableColumn
cfprApFabricFcoeSanEpOperStateReason = _CfprApFabricFcoeSanEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 21),
    _CfprApFabricFcoeSanEpOperStateReason_Type()
)
cfprApFabricFcoeSanEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpOperStateReason.setStatus("current")
_CfprApFabricFcoeSanEpPeerAggrPortId_Type = Gauge32
_CfprApFabricFcoeSanEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricFcoeSanEpPeerAggrPortId = _CfprApFabricFcoeSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 22),
    _CfprApFabricFcoeSanEpPeerAggrPortId_Type()
)
cfprApFabricFcoeSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpPeerAggrPortId.setStatus("current")
_CfprApFabricFcoeSanEpPeerChassisId_Type = Gauge32
_CfprApFabricFcoeSanEpPeerChassisId_Object = MibTableColumn
cfprApFabricFcoeSanEpPeerChassisId = _CfprApFabricFcoeSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 23),
    _CfprApFabricFcoeSanEpPeerChassisId_Type()
)
cfprApFabricFcoeSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpPeerChassisId.setStatus("current")
_CfprApFabricFcoeSanEpPeerDn_Type = SnmpAdminString
_CfprApFabricFcoeSanEpPeerDn_Object = MibTableColumn
cfprApFabricFcoeSanEpPeerDn = _CfprApFabricFcoeSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 24),
    _CfprApFabricFcoeSanEpPeerDn_Type()
)
cfprApFabricFcoeSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpPeerDn.setStatus("current")
_CfprApFabricFcoeSanEpPeerPortId_Type = Gauge32
_CfprApFabricFcoeSanEpPeerPortId_Object = MibTableColumn
cfprApFabricFcoeSanEpPeerPortId = _CfprApFabricFcoeSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 25),
    _CfprApFabricFcoeSanEpPeerPortId_Type()
)
cfprApFabricFcoeSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpPeerPortId.setStatus("current")
_CfprApFabricFcoeSanEpPeerSlotId_Type = Gauge32
_CfprApFabricFcoeSanEpPeerSlotId_Object = MibTableColumn
cfprApFabricFcoeSanEpPeerSlotId = _CfprApFabricFcoeSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 26),
    _CfprApFabricFcoeSanEpPeerSlotId_Type()
)
cfprApFabricFcoeSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpPeerSlotId.setStatus("current")
_CfprApFabricFcoeSanEpPortId_Type = CfprApFabricFcoeSanEpPortId
_CfprApFabricFcoeSanEpPortId_Object = MibTableColumn
cfprApFabricFcoeSanEpPortId = _CfprApFabricFcoeSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 27),
    _CfprApFabricFcoeSanEpPortId_Type()
)
cfprApFabricFcoeSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpPortId.setStatus("current")
_CfprApFabricFcoeSanEpSlotId_Type = CfprApFabricFcoeSanEpSlotId
_CfprApFabricFcoeSanEpSlotId_Object = MibTableColumn
cfprApFabricFcoeSanEpSlotId = _CfprApFabricFcoeSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 28),
    _CfprApFabricFcoeSanEpSlotId_Type()
)
cfprApFabricFcoeSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpSlotId.setStatus("current")
_CfprApFabricFcoeSanEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcoeSanEpSwitchId_Object = MibTableColumn
cfprApFabricFcoeSanEpSwitchId = _CfprApFabricFcoeSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 29),
    _CfprApFabricFcoeSanEpSwitchId_Type()
)
cfprApFabricFcoeSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpSwitchId.setStatus("current")
_CfprApFabricFcoeSanEpTransport_Type = CfprApFabricAFcoeSanEpTransport
_CfprApFabricFcoeSanEpTransport_Object = MibTableColumn
cfprApFabricFcoeSanEpTransport = _CfprApFabricFcoeSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 30),
    _CfprApFabricFcoeSanEpTransport_Type()
)
cfprApFabricFcoeSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpTransport.setStatus("current")
_CfprApFabricFcoeSanEpType_Type = CfprApFabricSanEpType
_CfprApFabricFcoeSanEpType_Object = MibTableColumn
cfprApFabricFcoeSanEpType = _CfprApFabricFcoeSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 31),
    _CfprApFabricFcoeSanEpType_Type()
)
cfprApFabricFcoeSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpType.setStatus("current")
_CfprApFabricFcoeSanEpUdldOperState_Type = CfprApFabricUdldOperState
_CfprApFabricFcoeSanEpUdldOperState_Object = MibTableColumn
cfprApFabricFcoeSanEpUdldOperState = _CfprApFabricFcoeSanEpUdldOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 32),
    _CfprApFabricFcoeSanEpUdldOperState_Type()
)
cfprApFabricFcoeSanEpUdldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpUdldOperState.setStatus("current")
_CfprApFabricFcoeSanEpUsrLbl_Type = SnmpAdminString
_CfprApFabricFcoeSanEpUsrLbl_Object = MibTableColumn
cfprApFabricFcoeSanEpUsrLbl = _CfprApFabricFcoeSanEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 33),
    _CfprApFabricFcoeSanEpUsrLbl_Type()
)
cfprApFabricFcoeSanEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpUsrLbl.setStatus("current")
_CfprApFabricFcoeSanEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcoeSanEpWarnings_Object = MibTableColumn
cfprApFabricFcoeSanEpWarnings = _CfprApFabricFcoeSanEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 59, 1, 34),
    _CfprApFabricFcoeSanEpWarnings_Type()
)
cfprApFabricFcoeSanEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanEpWarnings.setStatus("current")
_CfprApFabricFcoeSanPcTable_Object = MibTable
cfprApFabricFcoeSanPcTable = _CfprApFabricFcoeSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60)
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcTable.setStatus("current")
_CfprApFabricFcoeSanPcEntry_Object = MibTableRow
cfprApFabricFcoeSanPcEntry = _CfprApFabricFcoeSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1)
)
cfprApFabricFcoeSanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcoeSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEntry.setStatus("current")
_CfprApFabricFcoeSanPcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcoeSanPcInstanceId_Object = MibTableColumn
cfprApFabricFcoeSanPcInstanceId = _CfprApFabricFcoeSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 1),
    _CfprApFabricFcoeSanPcInstanceId_Type()
)
cfprApFabricFcoeSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcInstanceId.setStatus("current")
_CfprApFabricFcoeSanPcDn_Type = CfprApManagedObjectDn
_CfprApFabricFcoeSanPcDn_Object = MibTableColumn
cfprApFabricFcoeSanPcDn = _CfprApFabricFcoeSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 2),
    _CfprApFabricFcoeSanPcDn_Type()
)
cfprApFabricFcoeSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcDn.setStatus("current")
_CfprApFabricFcoeSanPcRn_Type = SnmpAdminString
_CfprApFabricFcoeSanPcRn_Object = MibTableColumn
cfprApFabricFcoeSanPcRn = _CfprApFabricFcoeSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 3),
    _CfprApFabricFcoeSanPcRn_Type()
)
cfprApFabricFcoeSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcRn.setStatus("current")
_CfprApFabricFcoeSanPcAdminState_Type = CfprApFabricCIoEpAdminState
_CfprApFabricFcoeSanPcAdminState_Object = MibTableColumn
cfprApFabricFcoeSanPcAdminState = _CfprApFabricFcoeSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 4),
    _CfprApFabricFcoeSanPcAdminState_Type()
)
cfprApFabricFcoeSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcAdminState.setStatus("current")
_CfprApFabricFcoeSanPcConfigState_Type = CfprApFabricConfigState
_CfprApFabricFcoeSanPcConfigState_Object = MibTableColumn
cfprApFabricFcoeSanPcConfigState = _CfprApFabricFcoeSanPcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 5),
    _CfprApFabricFcoeSanPcConfigState_Type()
)
cfprApFabricFcoeSanPcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcConfigState.setStatus("current")
_CfprApFabricFcoeSanPcDescr_Type = SnmpAdminString
_CfprApFabricFcoeSanPcDescr_Object = MibTableColumn
cfprApFabricFcoeSanPcDescr = _CfprApFabricFcoeSanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 6),
    _CfprApFabricFcoeSanPcDescr_Type()
)
cfprApFabricFcoeSanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcDescr.setStatus("current")
_CfprApFabricFcoeSanPcEpDn_Type = SnmpAdminString
_CfprApFabricFcoeSanPcEpDn_Object = MibTableColumn
cfprApFabricFcoeSanPcEpDn = _CfprApFabricFcoeSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 7),
    _CfprApFabricFcoeSanPcEpDn_Type()
)
cfprApFabricFcoeSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpDn.setStatus("current")
_CfprApFabricFcoeSanPcFcoeState_Type = CfprApNetworkPortOperState
_CfprApFabricFcoeSanPcFcoeState_Object = MibTableColumn
cfprApFabricFcoeSanPcFcoeState = _CfprApFabricFcoeSanPcFcoeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 8),
    _CfprApFabricFcoeSanPcFcoeState_Type()
)
cfprApFabricFcoeSanPcFcoeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcFcoeState.setStatus("current")
_CfprApFabricFcoeSanPcFcoeStateReason_Type = SnmpAdminString
_CfprApFabricFcoeSanPcFcoeStateReason_Object = MibTableColumn
cfprApFabricFcoeSanPcFcoeStateReason = _CfprApFabricFcoeSanPcFcoeStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 9),
    _CfprApFabricFcoeSanPcFcoeStateReason_Type()
)
cfprApFabricFcoeSanPcFcoeStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcFcoeStateReason.setStatus("current")
_CfprApFabricFcoeSanPcFltAggr_Type = Unsigned64
_CfprApFabricFcoeSanPcFltAggr_Object = MibTableColumn
cfprApFabricFcoeSanPcFltAggr = _CfprApFabricFcoeSanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 10),
    _CfprApFabricFcoeSanPcFltAggr_Type()
)
cfprApFabricFcoeSanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcFltAggr.setStatus("current")
_CfprApFabricFcoeSanPcIfRole_Type = CfprApFabricSanPcIfRole
_CfprApFabricFcoeSanPcIfRole_Object = MibTableColumn
cfprApFabricFcoeSanPcIfRole = _CfprApFabricFcoeSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 11),
    _CfprApFabricFcoeSanPcIfRole_Type()
)
cfprApFabricFcoeSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcIfRole.setStatus("current")
_CfprApFabricFcoeSanPcIfType_Type = CfprApFabricCIoEpIfType
_CfprApFabricFcoeSanPcIfType_Object = MibTableColumn
cfprApFabricFcoeSanPcIfType = _CfprApFabricFcoeSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 12),
    _CfprApFabricFcoeSanPcIfType_Type()
)
cfprApFabricFcoeSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcIfType.setStatus("current")
_CfprApFabricFcoeSanPcLacpPolicyName_Type = SnmpAdminString
_CfprApFabricFcoeSanPcLacpPolicyName_Object = MibTableColumn
cfprApFabricFcoeSanPcLacpPolicyName = _CfprApFabricFcoeSanPcLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 13),
    _CfprApFabricFcoeSanPcLacpPolicyName_Type()
)
cfprApFabricFcoeSanPcLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcLacpPolicyName.setStatus("current")
_CfprApFabricFcoeSanPcLocale_Type = CfprApFabricExternalPcLocale
_CfprApFabricFcoeSanPcLocale_Object = MibTableColumn
cfprApFabricFcoeSanPcLocale = _CfprApFabricFcoeSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 14),
    _CfprApFabricFcoeSanPcLocale_Type()
)
cfprApFabricFcoeSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcLocale.setStatus("current")
_CfprApFabricFcoeSanPcName_Type = SnmpAdminString
_CfprApFabricFcoeSanPcName_Object = MibTableColumn
cfprApFabricFcoeSanPcName = _CfprApFabricFcoeSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 15),
    _CfprApFabricFcoeSanPcName_Type()
)
cfprApFabricFcoeSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcName.setStatus("current")
_CfprApFabricFcoeSanPcOperLacpPolicyName_Type = SnmpAdminString
_CfprApFabricFcoeSanPcOperLacpPolicyName_Object = MibTableColumn
cfprApFabricFcoeSanPcOperLacpPolicyName = _CfprApFabricFcoeSanPcOperLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 16),
    _CfprApFabricFcoeSanPcOperLacpPolicyName_Type()
)
cfprApFabricFcoeSanPcOperLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcOperLacpPolicyName.setStatus("current")
_CfprApFabricFcoeSanPcOperState_Type = CfprApNetworkPortOperState
_CfprApFabricFcoeSanPcOperState_Object = MibTableColumn
cfprApFabricFcoeSanPcOperState = _CfprApFabricFcoeSanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 17),
    _CfprApFabricFcoeSanPcOperState_Type()
)
cfprApFabricFcoeSanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcOperState.setStatus("current")
_CfprApFabricFcoeSanPcPeerDn_Type = SnmpAdminString
_CfprApFabricFcoeSanPcPeerDn_Object = MibTableColumn
cfprApFabricFcoeSanPcPeerDn = _CfprApFabricFcoeSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 18),
    _CfprApFabricFcoeSanPcPeerDn_Type()
)
cfprApFabricFcoeSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcPeerDn.setStatus("current")
_CfprApFabricFcoeSanPcPortId_Type = Gauge32
_CfprApFabricFcoeSanPcPortId_Object = MibTableColumn
cfprApFabricFcoeSanPcPortId = _CfprApFabricFcoeSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 19),
    _CfprApFabricFcoeSanPcPortId_Type()
)
cfprApFabricFcoeSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcPortId.setStatus("current")
_CfprApFabricFcoeSanPcStateQual_Type = SnmpAdminString
_CfprApFabricFcoeSanPcStateQual_Object = MibTableColumn
cfprApFabricFcoeSanPcStateQual = _CfprApFabricFcoeSanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 20),
    _CfprApFabricFcoeSanPcStateQual_Type()
)
cfprApFabricFcoeSanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcStateQual.setStatus("current")
_CfprApFabricFcoeSanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcoeSanPcSwitchId_Object = MibTableColumn
cfprApFabricFcoeSanPcSwitchId = _CfprApFabricFcoeSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 21),
    _CfprApFabricFcoeSanPcSwitchId_Type()
)
cfprApFabricFcoeSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcSwitchId.setStatus("current")
_CfprApFabricFcoeSanPcTransport_Type = CfprApFabricFcoeSanPcTransport
_CfprApFabricFcoeSanPcTransport_Object = MibTableColumn
cfprApFabricFcoeSanPcTransport = _CfprApFabricFcoeSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 22),
    _CfprApFabricFcoeSanPcTransport_Type()
)
cfprApFabricFcoeSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcTransport.setStatus("current")
_CfprApFabricFcoeSanPcType_Type = CfprApFabricSanPcType
_CfprApFabricFcoeSanPcType_Object = MibTableColumn
cfprApFabricFcoeSanPcType = _CfprApFabricFcoeSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 23),
    _CfprApFabricFcoeSanPcType_Type()
)
cfprApFabricFcoeSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcType.setStatus("current")
_CfprApFabricFcoeSanPcWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcoeSanPcWarnings_Object = MibTableColumn
cfprApFabricFcoeSanPcWarnings = _CfprApFabricFcoeSanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 60, 1, 24),
    _CfprApFabricFcoeSanPcWarnings_Type()
)
cfprApFabricFcoeSanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcWarnings.setStatus("current")
_CfprApFabricFcoeSanPcEpTable_Object = MibTable
cfprApFabricFcoeSanPcEpTable = _CfprApFabricFcoeSanPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61)
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpTable.setStatus("current")
_CfprApFabricFcoeSanPcEpEntry_Object = MibTableRow
cfprApFabricFcoeSanPcEpEntry = _CfprApFabricFcoeSanPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1)
)
cfprApFabricFcoeSanPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcoeSanPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpEntry.setStatus("current")
_CfprApFabricFcoeSanPcEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcoeSanPcEpInstanceId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpInstanceId = _CfprApFabricFcoeSanPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 1),
    _CfprApFabricFcoeSanPcEpInstanceId_Type()
)
cfprApFabricFcoeSanPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpInstanceId.setStatus("current")
_CfprApFabricFcoeSanPcEpDnData_Type = CfprApManagedObjectDn
_CfprApFabricFcoeSanPcEpDnData_Object = MibTableColumn
cfprApFabricFcoeSanPcEpDnData = _CfprApFabricFcoeSanPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 2),
    _CfprApFabricFcoeSanPcEpDnData_Type()
)
cfprApFabricFcoeSanPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpDnData.setStatus("current")
_CfprApFabricFcoeSanPcEpRn_Type = SnmpAdminString
_CfprApFabricFcoeSanPcEpRn_Object = MibTableColumn
cfprApFabricFcoeSanPcEpRn = _CfprApFabricFcoeSanPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 3),
    _CfprApFabricFcoeSanPcEpRn_Type()
)
cfprApFabricFcoeSanPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpRn.setStatus("current")
_CfprApFabricFcoeSanPcEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricFcoeSanPcEpAdminState_Object = MibTableColumn
cfprApFabricFcoeSanPcEpAdminState = _CfprApFabricFcoeSanPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 4),
    _CfprApFabricFcoeSanPcEpAdminState_Type()
)
cfprApFabricFcoeSanPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpAdminState.setStatus("current")
_CfprApFabricFcoeSanPcEpAggrPortId_Type = Gauge32
_CfprApFabricFcoeSanPcEpAggrPortId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpAggrPortId = _CfprApFabricFcoeSanPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 5),
    _CfprApFabricFcoeSanPcEpAggrPortId_Type()
)
cfprApFabricFcoeSanPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpAggrPortId.setStatus("current")
_CfprApFabricFcoeSanPcEpChassisId_Type = Gauge32
_CfprApFabricFcoeSanPcEpChassisId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpChassisId = _CfprApFabricFcoeSanPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 6),
    _CfprApFabricFcoeSanPcEpChassisId_Type()
)
cfprApFabricFcoeSanPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpChassisId.setStatus("current")
_CfprApFabricFcoeSanPcEpEpDn_Type = SnmpAdminString
_CfprApFabricFcoeSanPcEpEpDn_Object = MibTableColumn
cfprApFabricFcoeSanPcEpEpDn = _CfprApFabricFcoeSanPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 7),
    _CfprApFabricFcoeSanPcEpEpDn_Type()
)
cfprApFabricFcoeSanPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpEpDn.setStatus("current")
_CfprApFabricFcoeSanPcEpEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricFcoeSanPcEpEthLinkProfileName_Object = MibTableColumn
cfprApFabricFcoeSanPcEpEthLinkProfileName = _CfprApFabricFcoeSanPcEpEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 8),
    _CfprApFabricFcoeSanPcEpEthLinkProfileName_Type()
)
cfprApFabricFcoeSanPcEpEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpEthLinkProfileName.setStatus("current")
_CfprApFabricFcoeSanPcEpFltAggr_Type = Unsigned64
_CfprApFabricFcoeSanPcEpFltAggr_Object = MibTableColumn
cfprApFabricFcoeSanPcEpFltAggr = _CfprApFabricFcoeSanPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 9),
    _CfprApFabricFcoeSanPcEpFltAggr_Type()
)
cfprApFabricFcoeSanPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpFltAggr.setStatus("current")
_CfprApFabricFcoeSanPcEpIfRole_Type = CfprApFabricSanEpIfRole
_CfprApFabricFcoeSanPcEpIfRole_Object = MibTableColumn
cfprApFabricFcoeSanPcEpIfRole = _CfprApFabricFcoeSanPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 10),
    _CfprApFabricFcoeSanPcEpIfRole_Type()
)
cfprApFabricFcoeSanPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpIfRole.setStatus("current")
_CfprApFabricFcoeSanPcEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricFcoeSanPcEpIfType_Object = MibTableColumn
cfprApFabricFcoeSanPcEpIfType = _CfprApFabricFcoeSanPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 11),
    _CfprApFabricFcoeSanPcEpIfType_Type()
)
cfprApFabricFcoeSanPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpIfType.setStatus("current")
_CfprApFabricFcoeSanPcEpLicGP_Type = Unsigned64
_CfprApFabricFcoeSanPcEpLicGP_Object = MibTableColumn
cfprApFabricFcoeSanPcEpLicGP = _CfprApFabricFcoeSanPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 12),
    _CfprApFabricFcoeSanPcEpLicGP_Type()
)
cfprApFabricFcoeSanPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpLicGP.setStatus("current")
_CfprApFabricFcoeSanPcEpLicState_Type = CfprApLicenseState
_CfprApFabricFcoeSanPcEpLicState_Object = MibTableColumn
cfprApFabricFcoeSanPcEpLicState = _CfprApFabricFcoeSanPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 13),
    _CfprApFabricFcoeSanPcEpLicState_Type()
)
cfprApFabricFcoeSanPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpLicState.setStatus("current")
_CfprApFabricFcoeSanPcEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricFcoeSanPcEpLocale_Object = MibTableColumn
cfprApFabricFcoeSanPcEpLocale = _CfprApFabricFcoeSanPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 14),
    _CfprApFabricFcoeSanPcEpLocale_Type()
)
cfprApFabricFcoeSanPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpLocale.setStatus("current")
_CfprApFabricFcoeSanPcEpMembership_Type = CfprApFabricMembershipStatus
_CfprApFabricFcoeSanPcEpMembership_Object = MibTableColumn
cfprApFabricFcoeSanPcEpMembership = _CfprApFabricFcoeSanPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 15),
    _CfprApFabricFcoeSanPcEpMembership_Type()
)
cfprApFabricFcoeSanPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpMembership.setStatus("current")
_CfprApFabricFcoeSanPcEpName_Type = SnmpAdminString
_CfprApFabricFcoeSanPcEpName_Object = MibTableColumn
cfprApFabricFcoeSanPcEpName = _CfprApFabricFcoeSanPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 16),
    _CfprApFabricFcoeSanPcEpName_Type()
)
cfprApFabricFcoeSanPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpName.setStatus("current")
_CfprApFabricFcoeSanPcEpOperEthLinkProfileName_Type = SnmpAdminString
_CfprApFabricFcoeSanPcEpOperEthLinkProfileName_Object = MibTableColumn
cfprApFabricFcoeSanPcEpOperEthLinkProfileName = _CfprApFabricFcoeSanPcEpOperEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 17),
    _CfprApFabricFcoeSanPcEpOperEthLinkProfileName_Type()
)
cfprApFabricFcoeSanPcEpOperEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpOperEthLinkProfileName.setStatus("current")
_CfprApFabricFcoeSanPcEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricFcoeSanPcEpOperState_Object = MibTableColumn
cfprApFabricFcoeSanPcEpOperState = _CfprApFabricFcoeSanPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 18),
    _CfprApFabricFcoeSanPcEpOperState_Type()
)
cfprApFabricFcoeSanPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpOperState.setStatus("current")
_CfprApFabricFcoeSanPcEpOperStateReason_Type = SnmpAdminString
_CfprApFabricFcoeSanPcEpOperStateReason_Object = MibTableColumn
cfprApFabricFcoeSanPcEpOperStateReason = _CfprApFabricFcoeSanPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 19),
    _CfprApFabricFcoeSanPcEpOperStateReason_Type()
)
cfprApFabricFcoeSanPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpOperStateReason.setStatus("current")
_CfprApFabricFcoeSanPcEpPeerAggrPortId_Type = Gauge32
_CfprApFabricFcoeSanPcEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpPeerAggrPortId = _CfprApFabricFcoeSanPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 20),
    _CfprApFabricFcoeSanPcEpPeerAggrPortId_Type()
)
cfprApFabricFcoeSanPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpPeerAggrPortId.setStatus("current")
_CfprApFabricFcoeSanPcEpPeerChassisId_Type = Gauge32
_CfprApFabricFcoeSanPcEpPeerChassisId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpPeerChassisId = _CfprApFabricFcoeSanPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 21),
    _CfprApFabricFcoeSanPcEpPeerChassisId_Type()
)
cfprApFabricFcoeSanPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpPeerChassisId.setStatus("current")
_CfprApFabricFcoeSanPcEpPeerDn_Type = SnmpAdminString
_CfprApFabricFcoeSanPcEpPeerDn_Object = MibTableColumn
cfprApFabricFcoeSanPcEpPeerDn = _CfprApFabricFcoeSanPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 22),
    _CfprApFabricFcoeSanPcEpPeerDn_Type()
)
cfprApFabricFcoeSanPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpPeerDn.setStatus("current")
_CfprApFabricFcoeSanPcEpPeerPortId_Type = Gauge32
_CfprApFabricFcoeSanPcEpPeerPortId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpPeerPortId = _CfprApFabricFcoeSanPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 23),
    _CfprApFabricFcoeSanPcEpPeerPortId_Type()
)
cfprApFabricFcoeSanPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpPeerPortId.setStatus("current")
_CfprApFabricFcoeSanPcEpPeerSlotId_Type = Gauge32
_CfprApFabricFcoeSanPcEpPeerSlotId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpPeerSlotId = _CfprApFabricFcoeSanPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 24),
    _CfprApFabricFcoeSanPcEpPeerSlotId_Type()
)
cfprApFabricFcoeSanPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpPeerSlotId.setStatus("current")
_CfprApFabricFcoeSanPcEpPortId_Type = CfprApFabricFcoeSanPcEpPortId
_CfprApFabricFcoeSanPcEpPortId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpPortId = _CfprApFabricFcoeSanPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 25),
    _CfprApFabricFcoeSanPcEpPortId_Type()
)
cfprApFabricFcoeSanPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpPortId.setStatus("current")
_CfprApFabricFcoeSanPcEpSlotId_Type = CfprApFabricFcoeSanPcEpSlotId
_CfprApFabricFcoeSanPcEpSlotId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpSlotId = _CfprApFabricFcoeSanPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 26),
    _CfprApFabricFcoeSanPcEpSlotId_Type()
)
cfprApFabricFcoeSanPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpSlotId.setStatus("current")
_CfprApFabricFcoeSanPcEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcoeSanPcEpSwitchId_Object = MibTableColumn
cfprApFabricFcoeSanPcEpSwitchId = _CfprApFabricFcoeSanPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 27),
    _CfprApFabricFcoeSanPcEpSwitchId_Type()
)
cfprApFabricFcoeSanPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpSwitchId.setStatus("current")
_CfprApFabricFcoeSanPcEpTransport_Type = CfprApFabricAFcoeSanEpTransport
_CfprApFabricFcoeSanPcEpTransport_Object = MibTableColumn
cfprApFabricFcoeSanPcEpTransport = _CfprApFabricFcoeSanPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 28),
    _CfprApFabricFcoeSanPcEpTransport_Type()
)
cfprApFabricFcoeSanPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpTransport.setStatus("current")
_CfprApFabricFcoeSanPcEpType_Type = CfprApFabricSanEpType
_CfprApFabricFcoeSanPcEpType_Object = MibTableColumn
cfprApFabricFcoeSanPcEpType = _CfprApFabricFcoeSanPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 29),
    _CfprApFabricFcoeSanPcEpType_Type()
)
cfprApFabricFcoeSanPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpType.setStatus("current")
_CfprApFabricFcoeSanPcEpUdldOperState_Type = CfprApFabricUdldOperState
_CfprApFabricFcoeSanPcEpUdldOperState_Object = MibTableColumn
cfprApFabricFcoeSanPcEpUdldOperState = _CfprApFabricFcoeSanPcEpUdldOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 30),
    _CfprApFabricFcoeSanPcEpUdldOperState_Type()
)
cfprApFabricFcoeSanPcEpUdldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpUdldOperState.setStatus("current")
_CfprApFabricFcoeSanPcEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcoeSanPcEpWarnings_Object = MibTableColumn
cfprApFabricFcoeSanPcEpWarnings = _CfprApFabricFcoeSanPcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 61, 1, 31),
    _CfprApFabricFcoeSanPcEpWarnings_Type()
)
cfprApFabricFcoeSanPcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeSanPcEpWarnings.setStatus("current")
_CfprApFabricFcoeVsanPcTable_Object = MibTable
cfprApFabricFcoeVsanPcTable = _CfprApFabricFcoeVsanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62)
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcTable.setStatus("current")
_CfprApFabricFcoeVsanPcEntry_Object = MibTableRow
cfprApFabricFcoeVsanPcEntry = _CfprApFabricFcoeVsanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1)
)
cfprApFabricFcoeVsanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcoeVsanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcEntry.setStatus("current")
_CfprApFabricFcoeVsanPcInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcoeVsanPcInstanceId_Object = MibTableColumn
cfprApFabricFcoeVsanPcInstanceId = _CfprApFabricFcoeVsanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 1),
    _CfprApFabricFcoeVsanPcInstanceId_Type()
)
cfprApFabricFcoeVsanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcInstanceId.setStatus("current")
_CfprApFabricFcoeVsanPcDn_Type = CfprApManagedObjectDn
_CfprApFabricFcoeVsanPcDn_Object = MibTableColumn
cfprApFabricFcoeVsanPcDn = _CfprApFabricFcoeVsanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 2),
    _CfprApFabricFcoeVsanPcDn_Type()
)
cfprApFabricFcoeVsanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcDn.setStatus("current")
_CfprApFabricFcoeVsanPcRn_Type = SnmpAdminString
_CfprApFabricFcoeVsanPcRn_Object = MibTableColumn
cfprApFabricFcoeVsanPcRn = _CfprApFabricFcoeVsanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 3),
    _CfprApFabricFcoeVsanPcRn_Type()
)
cfprApFabricFcoeVsanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcRn.setStatus("current")
_CfprApFabricFcoeVsanPcAdminState_Type = CfprApFabricCIoEpAdminState
_CfprApFabricFcoeVsanPcAdminState_Object = MibTableColumn
cfprApFabricFcoeVsanPcAdminState = _CfprApFabricFcoeVsanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 4),
    _CfprApFabricFcoeVsanPcAdminState_Type()
)
cfprApFabricFcoeVsanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcAdminState.setStatus("current")
_CfprApFabricFcoeVsanPcDescr_Type = SnmpAdminString
_CfprApFabricFcoeVsanPcDescr_Object = MibTableColumn
cfprApFabricFcoeVsanPcDescr = _CfprApFabricFcoeVsanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 5),
    _CfprApFabricFcoeVsanPcDescr_Type()
)
cfprApFabricFcoeVsanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcDescr.setStatus("current")
_CfprApFabricFcoeVsanPcEpDn_Type = SnmpAdminString
_CfprApFabricFcoeVsanPcEpDn_Object = MibTableColumn
cfprApFabricFcoeVsanPcEpDn = _CfprApFabricFcoeVsanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 6),
    _CfprApFabricFcoeVsanPcEpDn_Type()
)
cfprApFabricFcoeVsanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcEpDn.setStatus("current")
_CfprApFabricFcoeVsanPcFltAggr_Type = Unsigned64
_CfprApFabricFcoeVsanPcFltAggr_Object = MibTableColumn
cfprApFabricFcoeVsanPcFltAggr = _CfprApFabricFcoeVsanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 7),
    _CfprApFabricFcoeVsanPcFltAggr_Type()
)
cfprApFabricFcoeVsanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcFltAggr.setStatus("current")
_CfprApFabricFcoeVsanPcIfRole_Type = CfprApFabricSanPcIfRole
_CfprApFabricFcoeVsanPcIfRole_Object = MibTableColumn
cfprApFabricFcoeVsanPcIfRole = _CfprApFabricFcoeVsanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 8),
    _CfprApFabricFcoeVsanPcIfRole_Type()
)
cfprApFabricFcoeVsanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcIfRole.setStatus("current")
_CfprApFabricFcoeVsanPcIfType_Type = CfprApFabricCIoEpIfType
_CfprApFabricFcoeVsanPcIfType_Object = MibTableColumn
cfprApFabricFcoeVsanPcIfType = _CfprApFabricFcoeVsanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 9),
    _CfprApFabricFcoeVsanPcIfType_Type()
)
cfprApFabricFcoeVsanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcIfType.setStatus("current")
_CfprApFabricFcoeVsanPcLocale_Type = CfprApFabricExternalPcLocale
_CfprApFabricFcoeVsanPcLocale_Object = MibTableColumn
cfprApFabricFcoeVsanPcLocale = _CfprApFabricFcoeVsanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 10),
    _CfprApFabricFcoeVsanPcLocale_Type()
)
cfprApFabricFcoeVsanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcLocale.setStatus("current")
_CfprApFabricFcoeVsanPcName_Type = SnmpAdminString
_CfprApFabricFcoeVsanPcName_Object = MibTableColumn
cfprApFabricFcoeVsanPcName = _CfprApFabricFcoeVsanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 11),
    _CfprApFabricFcoeVsanPcName_Type()
)
cfprApFabricFcoeVsanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcName.setStatus("current")
_CfprApFabricFcoeVsanPcOperState_Type = CfprApNetworkPortOperState
_CfprApFabricFcoeVsanPcOperState_Object = MibTableColumn
cfprApFabricFcoeVsanPcOperState = _CfprApFabricFcoeVsanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 12),
    _CfprApFabricFcoeVsanPcOperState_Type()
)
cfprApFabricFcoeVsanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcOperState.setStatus("current")
_CfprApFabricFcoeVsanPcPeerDn_Type = SnmpAdminString
_CfprApFabricFcoeVsanPcPeerDn_Object = MibTableColumn
cfprApFabricFcoeVsanPcPeerDn = _CfprApFabricFcoeVsanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 13),
    _CfprApFabricFcoeVsanPcPeerDn_Type()
)
cfprApFabricFcoeVsanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcPeerDn.setStatus("current")
_CfprApFabricFcoeVsanPcPortId_Type = Gauge32
_CfprApFabricFcoeVsanPcPortId_Object = MibTableColumn
cfprApFabricFcoeVsanPcPortId = _CfprApFabricFcoeVsanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 14),
    _CfprApFabricFcoeVsanPcPortId_Type()
)
cfprApFabricFcoeVsanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcPortId.setStatus("current")
_CfprApFabricFcoeVsanPcStateQual_Type = SnmpAdminString
_CfprApFabricFcoeVsanPcStateQual_Object = MibTableColumn
cfprApFabricFcoeVsanPcStateQual = _CfprApFabricFcoeVsanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 15),
    _CfprApFabricFcoeVsanPcStateQual_Type()
)
cfprApFabricFcoeVsanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcStateQual.setStatus("current")
_CfprApFabricFcoeVsanPcSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcoeVsanPcSwitchId_Object = MibTableColumn
cfprApFabricFcoeVsanPcSwitchId = _CfprApFabricFcoeVsanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 16),
    _CfprApFabricFcoeVsanPcSwitchId_Type()
)
cfprApFabricFcoeVsanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcSwitchId.setStatus("current")
_CfprApFabricFcoeVsanPcTransport_Type = CfprApFabricFcoeVsanPcTransport
_CfprApFabricFcoeVsanPcTransport_Object = MibTableColumn
cfprApFabricFcoeVsanPcTransport = _CfprApFabricFcoeVsanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 17),
    _CfprApFabricFcoeVsanPcTransport_Type()
)
cfprApFabricFcoeVsanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcTransport.setStatus("current")
_CfprApFabricFcoeVsanPcType_Type = CfprApFabricSanPcType
_CfprApFabricFcoeVsanPcType_Object = MibTableColumn
cfprApFabricFcoeVsanPcType = _CfprApFabricFcoeVsanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 18),
    _CfprApFabricFcoeVsanPcType_Type()
)
cfprApFabricFcoeVsanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcType.setStatus("current")
_CfprApFabricFcoeVsanPcWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcoeVsanPcWarnings_Object = MibTableColumn
cfprApFabricFcoeVsanPcWarnings = _CfprApFabricFcoeVsanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 62, 1, 19),
    _CfprApFabricFcoeVsanPcWarnings_Type()
)
cfprApFabricFcoeVsanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPcWarnings.setStatus("current")
_CfprApFabricFcoeVsanPortEpTable_Object = MibTable
cfprApFabricFcoeVsanPortEpTable = _CfprApFabricFcoeVsanPortEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63)
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpTable.setStatus("current")
_CfprApFabricFcoeVsanPortEpEntry_Object = MibTableRow
cfprApFabricFcoeVsanPortEpEntry = _CfprApFabricFcoeVsanPortEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1)
)
cfprApFabricFcoeVsanPortEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricFcoeVsanPortEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpEntry.setStatus("current")
_CfprApFabricFcoeVsanPortEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricFcoeVsanPortEpInstanceId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpInstanceId = _CfprApFabricFcoeVsanPortEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 1),
    _CfprApFabricFcoeVsanPortEpInstanceId_Type()
)
cfprApFabricFcoeVsanPortEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpInstanceId.setStatus("current")
_CfprApFabricFcoeVsanPortEpDn_Type = CfprApManagedObjectDn
_CfprApFabricFcoeVsanPortEpDn_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpDn = _CfprApFabricFcoeVsanPortEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 2),
    _CfprApFabricFcoeVsanPortEpDn_Type()
)
cfprApFabricFcoeVsanPortEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpDn.setStatus("current")
_CfprApFabricFcoeVsanPortEpRn_Type = SnmpAdminString
_CfprApFabricFcoeVsanPortEpRn_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpRn = _CfprApFabricFcoeVsanPortEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 3),
    _CfprApFabricFcoeVsanPortEpRn_Type()
)
cfprApFabricFcoeVsanPortEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpRn.setStatus("current")
_CfprApFabricFcoeVsanPortEpAdminState_Type = CfprApFabricExternalEpAdminState
_CfprApFabricFcoeVsanPortEpAdminState_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpAdminState = _CfprApFabricFcoeVsanPortEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 4),
    _CfprApFabricFcoeVsanPortEpAdminState_Type()
)
cfprApFabricFcoeVsanPortEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpAdminState.setStatus("current")
_CfprApFabricFcoeVsanPortEpAggrPortId_Type = Gauge32
_CfprApFabricFcoeVsanPortEpAggrPortId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpAggrPortId = _CfprApFabricFcoeVsanPortEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 5),
    _CfprApFabricFcoeVsanPortEpAggrPortId_Type()
)
cfprApFabricFcoeVsanPortEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpAggrPortId.setStatus("current")
_CfprApFabricFcoeVsanPortEpChassisId_Type = Gauge32
_CfprApFabricFcoeVsanPortEpChassisId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpChassisId = _CfprApFabricFcoeVsanPortEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 6),
    _CfprApFabricFcoeVsanPortEpChassisId_Type()
)
cfprApFabricFcoeVsanPortEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpChassisId.setStatus("current")
_CfprApFabricFcoeVsanPortEpEpDn_Type = SnmpAdminString
_CfprApFabricFcoeVsanPortEpEpDn_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpEpDn = _CfprApFabricFcoeVsanPortEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 7),
    _CfprApFabricFcoeVsanPortEpEpDn_Type()
)
cfprApFabricFcoeVsanPortEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpEpDn.setStatus("current")
_CfprApFabricFcoeVsanPortEpFltAggr_Type = Unsigned64
_CfprApFabricFcoeVsanPortEpFltAggr_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpFltAggr = _CfprApFabricFcoeVsanPortEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 8),
    _CfprApFabricFcoeVsanPortEpFltAggr_Type()
)
cfprApFabricFcoeVsanPortEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpFltAggr.setStatus("current")
_CfprApFabricFcoeVsanPortEpIfRole_Type = CfprApFabricSanEpIfRole
_CfprApFabricFcoeVsanPortEpIfRole_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpIfRole = _CfprApFabricFcoeVsanPortEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 9),
    _CfprApFabricFcoeVsanPortEpIfRole_Type()
)
cfprApFabricFcoeVsanPortEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpIfRole.setStatus("current")
_CfprApFabricFcoeVsanPortEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricFcoeVsanPortEpIfType_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpIfType = _CfprApFabricFcoeVsanPortEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 10),
    _CfprApFabricFcoeVsanPortEpIfType_Type()
)
cfprApFabricFcoeVsanPortEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpIfType.setStatus("current")
_CfprApFabricFcoeVsanPortEpLicGP_Type = Unsigned64
_CfprApFabricFcoeVsanPortEpLicGP_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpLicGP = _CfprApFabricFcoeVsanPortEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 11),
    _CfprApFabricFcoeVsanPortEpLicGP_Type()
)
cfprApFabricFcoeVsanPortEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpLicGP.setStatus("current")
_CfprApFabricFcoeVsanPortEpLicState_Type = CfprApLicenseState
_CfprApFabricFcoeVsanPortEpLicState_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpLicState = _CfprApFabricFcoeVsanPortEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 12),
    _CfprApFabricFcoeVsanPortEpLicState_Type()
)
cfprApFabricFcoeVsanPortEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpLicState.setStatus("current")
_CfprApFabricFcoeVsanPortEpLocale_Type = CfprApFabricExternalEpLocale
_CfprApFabricFcoeVsanPortEpLocale_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpLocale = _CfprApFabricFcoeVsanPortEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 13),
    _CfprApFabricFcoeVsanPortEpLocale_Type()
)
cfprApFabricFcoeVsanPortEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpLocale.setStatus("current")
_CfprApFabricFcoeVsanPortEpName_Type = SnmpAdminString
_CfprApFabricFcoeVsanPortEpName_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpName = _CfprApFabricFcoeVsanPortEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 14),
    _CfprApFabricFcoeVsanPortEpName_Type()
)
cfprApFabricFcoeVsanPortEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpName.setStatus("current")
_CfprApFabricFcoeVsanPortEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricFcoeVsanPortEpOperState_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpOperState = _CfprApFabricFcoeVsanPortEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 15),
    _CfprApFabricFcoeVsanPortEpOperState_Type()
)
cfprApFabricFcoeVsanPortEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpOperState.setStatus("current")
_CfprApFabricFcoeVsanPortEpOperStateReason_Type = SnmpAdminString
_CfprApFabricFcoeVsanPortEpOperStateReason_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpOperStateReason = _CfprApFabricFcoeVsanPortEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 16),
    _CfprApFabricFcoeVsanPortEpOperStateReason_Type()
)
cfprApFabricFcoeVsanPortEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpOperStateReason.setStatus("current")
_CfprApFabricFcoeVsanPortEpPeerAggrPortId_Type = Gauge32
_CfprApFabricFcoeVsanPortEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpPeerAggrPortId = _CfprApFabricFcoeVsanPortEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 17),
    _CfprApFabricFcoeVsanPortEpPeerAggrPortId_Type()
)
cfprApFabricFcoeVsanPortEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpPeerAggrPortId.setStatus("current")
_CfprApFabricFcoeVsanPortEpPeerChassisId_Type = Gauge32
_CfprApFabricFcoeVsanPortEpPeerChassisId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpPeerChassisId = _CfprApFabricFcoeVsanPortEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 18),
    _CfprApFabricFcoeVsanPortEpPeerChassisId_Type()
)
cfprApFabricFcoeVsanPortEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpPeerChassisId.setStatus("current")
_CfprApFabricFcoeVsanPortEpPeerDn_Type = SnmpAdminString
_CfprApFabricFcoeVsanPortEpPeerDn_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpPeerDn = _CfprApFabricFcoeVsanPortEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 19),
    _CfprApFabricFcoeVsanPortEpPeerDn_Type()
)
cfprApFabricFcoeVsanPortEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpPeerDn.setStatus("current")
_CfprApFabricFcoeVsanPortEpPeerPortId_Type = Gauge32
_CfprApFabricFcoeVsanPortEpPeerPortId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpPeerPortId = _CfprApFabricFcoeVsanPortEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 20),
    _CfprApFabricFcoeVsanPortEpPeerPortId_Type()
)
cfprApFabricFcoeVsanPortEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpPeerPortId.setStatus("current")
_CfprApFabricFcoeVsanPortEpPeerSlotId_Type = Gauge32
_CfprApFabricFcoeVsanPortEpPeerSlotId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpPeerSlotId = _CfprApFabricFcoeVsanPortEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 21),
    _CfprApFabricFcoeVsanPortEpPeerSlotId_Type()
)
cfprApFabricFcoeVsanPortEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpPeerSlotId.setStatus("current")
_CfprApFabricFcoeVsanPortEpPortId_Type = CfprApFabricFcoeVsanPortEpPortId
_CfprApFabricFcoeVsanPortEpPortId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpPortId = _CfprApFabricFcoeVsanPortEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 22),
    _CfprApFabricFcoeVsanPortEpPortId_Type()
)
cfprApFabricFcoeVsanPortEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpPortId.setStatus("current")
_CfprApFabricFcoeVsanPortEpSlotId_Type = CfprApFabricFcoeVsanPortEpSlotId
_CfprApFabricFcoeVsanPortEpSlotId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpSlotId = _CfprApFabricFcoeVsanPortEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 23),
    _CfprApFabricFcoeVsanPortEpSlotId_Type()
)
cfprApFabricFcoeVsanPortEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpSlotId.setStatus("current")
_CfprApFabricFcoeVsanPortEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricFcoeVsanPortEpSwitchId_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpSwitchId = _CfprApFabricFcoeVsanPortEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 24),
    _CfprApFabricFcoeVsanPortEpSwitchId_Type()
)
cfprApFabricFcoeVsanPortEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpSwitchId.setStatus("current")
_CfprApFabricFcoeVsanPortEpTransport_Type = CfprApFabricAFcSanEpTransport
_CfprApFabricFcoeVsanPortEpTransport_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpTransport = _CfprApFabricFcoeVsanPortEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 25),
    _CfprApFabricFcoeVsanPortEpTransport_Type()
)
cfprApFabricFcoeVsanPortEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpTransport.setStatus("current")
_CfprApFabricFcoeVsanPortEpType_Type = CfprApFabricSanEpType
_CfprApFabricFcoeVsanPortEpType_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpType = _CfprApFabricFcoeVsanPortEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 26),
    _CfprApFabricFcoeVsanPortEpType_Type()
)
cfprApFabricFcoeVsanPortEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpType.setStatus("current")
_CfprApFabricFcoeVsanPortEpWarnings_Type = CfprApFabricWarnings
_CfprApFabricFcoeVsanPortEpWarnings_Object = MibTableColumn
cfprApFabricFcoeVsanPortEpWarnings = _CfprApFabricFcoeVsanPortEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 63, 1, 27),
    _CfprApFabricFcoeVsanPortEpWarnings_Type()
)
cfprApFabricFcoeVsanPortEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricFcoeVsanPortEpWarnings.setStatus("current")
_CfprApFabricIfTable_Object = MibTable
cfprApFabricIfTable = _CfprApFabricIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 66)
)
if mibBuilder.loadTexts:
    cfprApFabricIfTable.setStatus("current")
_CfprApFabricIfEntry_Object = MibTableRow
cfprApFabricIfEntry = _CfprApFabricIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 66, 1)
)
cfprApFabricIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricIfEntry.setStatus("current")
_CfprApFabricIfInstanceId_Type = CfprApManagedObjectId
_CfprApFabricIfInstanceId_Object = MibTableColumn
cfprApFabricIfInstanceId = _CfprApFabricIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 66, 1, 1),
    _CfprApFabricIfInstanceId_Type()
)
cfprApFabricIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricIfInstanceId.setStatus("current")
_CfprApFabricIfDn_Type = CfprApManagedObjectDn
_CfprApFabricIfDn_Object = MibTableColumn
cfprApFabricIfDn = _CfprApFabricIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 66, 1, 2),
    _CfprApFabricIfDn_Type()
)
cfprApFabricIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricIfDn.setStatus("current")
_CfprApFabricIfRn_Type = SnmpAdminString
_CfprApFabricIfRn_Object = MibTableColumn
cfprApFabricIfRn = _CfprApFabricIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 66, 1, 3),
    _CfprApFabricIfRn_Type()
)
cfprApFabricIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricIfRn.setStatus("current")
_CfprApFabricIfAddr_Type = InetAddressIPv4
_CfprApFabricIfAddr_Object = MibTableColumn
cfprApFabricIfAddr = _CfprApFabricIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 66, 1, 4),
    _CfprApFabricIfAddr_Type()
)
cfprApFabricIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricIfAddr.setStatus("current")
_CfprApFabricIfId_Type = CfprApNetworkSwitchId
_CfprApFabricIfId_Object = MibTableColumn
cfprApFabricIfId = _CfprApFabricIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 66, 1, 5),
    _CfprApFabricIfId_Type()
)
cfprApFabricIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricIfId.setStatus("current")
_CfprApFabricLacpPolicyTable_Object = MibTable
cfprApFabricLacpPolicyTable = _CfprApFabricLacpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67)
)
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyTable.setStatus("current")
_CfprApFabricLacpPolicyEntry_Object = MibTableRow
cfprApFabricLacpPolicyEntry = _CfprApFabricLacpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1)
)
cfprApFabricLacpPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLacpPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyEntry.setStatus("current")
_CfprApFabricLacpPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLacpPolicyInstanceId_Object = MibTableColumn
cfprApFabricLacpPolicyInstanceId = _CfprApFabricLacpPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 1),
    _CfprApFabricLacpPolicyInstanceId_Type()
)
cfprApFabricLacpPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyInstanceId.setStatus("current")
_CfprApFabricLacpPolicyDn_Type = CfprApManagedObjectDn
_CfprApFabricLacpPolicyDn_Object = MibTableColumn
cfprApFabricLacpPolicyDn = _CfprApFabricLacpPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 2),
    _CfprApFabricLacpPolicyDn_Type()
)
cfprApFabricLacpPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyDn.setStatus("current")
_CfprApFabricLacpPolicyRn_Type = SnmpAdminString
_CfprApFabricLacpPolicyRn_Object = MibTableColumn
cfprApFabricLacpPolicyRn = _CfprApFabricLacpPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 3),
    _CfprApFabricLacpPolicyRn_Type()
)
cfprApFabricLacpPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyRn.setStatus("current")
_CfprApFabricLacpPolicyDescr_Type = SnmpAdminString
_CfprApFabricLacpPolicyDescr_Object = MibTableColumn
cfprApFabricLacpPolicyDescr = _CfprApFabricLacpPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 4),
    _CfprApFabricLacpPolicyDescr_Type()
)
cfprApFabricLacpPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyDescr.setStatus("current")
_CfprApFabricLacpPolicyFastTimer_Type = CfprApFabricLacpRate
_CfprApFabricLacpPolicyFastTimer_Object = MibTableColumn
cfprApFabricLacpPolicyFastTimer = _CfprApFabricLacpPolicyFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 5),
    _CfprApFabricLacpPolicyFastTimer_Type()
)
cfprApFabricLacpPolicyFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyFastTimer.setStatus("current")
_CfprApFabricLacpPolicyIntId_Type = SnmpAdminString
_CfprApFabricLacpPolicyIntId_Object = MibTableColumn
cfprApFabricLacpPolicyIntId = _CfprApFabricLacpPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 6),
    _CfprApFabricLacpPolicyIntId_Type()
)
cfprApFabricLacpPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyIntId.setStatus("current")
_CfprApFabricLacpPolicyName_Type = SnmpAdminString
_CfprApFabricLacpPolicyName_Object = MibTableColumn
cfprApFabricLacpPolicyName = _CfprApFabricLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 7),
    _CfprApFabricLacpPolicyName_Type()
)
cfprApFabricLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyName.setStatus("current")
_CfprApFabricLacpPolicyPolicyLevel_Type = Gauge32
_CfprApFabricLacpPolicyPolicyLevel_Object = MibTableColumn
cfprApFabricLacpPolicyPolicyLevel = _CfprApFabricLacpPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 8),
    _CfprApFabricLacpPolicyPolicyLevel_Type()
)
cfprApFabricLacpPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyPolicyLevel.setStatus("current")
_CfprApFabricLacpPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricLacpPolicyPolicyOwner_Object = MibTableColumn
cfprApFabricLacpPolicyPolicyOwner = _CfprApFabricLacpPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 9),
    _CfprApFabricLacpPolicyPolicyOwner_Type()
)
cfprApFabricLacpPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicyPolicyOwner.setStatus("current")
_CfprApFabricLacpPolicySuspendIndividual_Type = CfprApFabricLacpSuspend
_CfprApFabricLacpPolicySuspendIndividual_Object = MibTableColumn
cfprApFabricLacpPolicySuspendIndividual = _CfprApFabricLacpPolicySuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 67, 1, 10),
    _CfprApFabricLacpPolicySuspendIndividual_Type()
)
cfprApFabricLacpPolicySuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLacpPolicySuspendIndividual.setStatus("current")
_CfprApFabricLanAccessMgrTable_Object = MibTable
cfprApFabricLanAccessMgrTable = _CfprApFabricLanAccessMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 68)
)
if mibBuilder.loadTexts:
    cfprApFabricLanAccessMgrTable.setStatus("current")
_CfprApFabricLanAccessMgrEntry_Object = MibTableRow
cfprApFabricLanAccessMgrEntry = _CfprApFabricLanAccessMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 68, 1)
)
cfprApFabricLanAccessMgrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLanAccessMgrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLanAccessMgrEntry.setStatus("current")
_CfprApFabricLanAccessMgrInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLanAccessMgrInstanceId_Object = MibTableColumn
cfprApFabricLanAccessMgrInstanceId = _CfprApFabricLanAccessMgrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 68, 1, 1),
    _CfprApFabricLanAccessMgrInstanceId_Type()
)
cfprApFabricLanAccessMgrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLanAccessMgrInstanceId.setStatus("current")
_CfprApFabricLanAccessMgrDn_Type = CfprApManagedObjectDn
_CfprApFabricLanAccessMgrDn_Object = MibTableColumn
cfprApFabricLanAccessMgrDn = _CfprApFabricLanAccessMgrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 68, 1, 2),
    _CfprApFabricLanAccessMgrDn_Type()
)
cfprApFabricLanAccessMgrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanAccessMgrDn.setStatus("current")
_CfprApFabricLanAccessMgrRn_Type = SnmpAdminString
_CfprApFabricLanAccessMgrRn_Object = MibTableColumn
cfprApFabricLanAccessMgrRn = _CfprApFabricLanAccessMgrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 68, 1, 3),
    _CfprApFabricLanAccessMgrRn_Type()
)
cfprApFabricLanAccessMgrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanAccessMgrRn.setStatus("current")
_CfprApFabricLanCloudTable_Object = MibTable
cfprApFabricLanCloudTable = _CfprApFabricLanCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69)
)
if mibBuilder.loadTexts:
    cfprApFabricLanCloudTable.setStatus("current")
_CfprApFabricLanCloudEntry_Object = MibTableRow
cfprApFabricLanCloudEntry = _CfprApFabricLanCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1)
)
cfprApFabricLanCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLanCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLanCloudEntry.setStatus("current")
_CfprApFabricLanCloudInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLanCloudInstanceId_Object = MibTableColumn
cfprApFabricLanCloudInstanceId = _CfprApFabricLanCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 1),
    _CfprApFabricLanCloudInstanceId_Type()
)
cfprApFabricLanCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudInstanceId.setStatus("current")
_CfprApFabricLanCloudDn_Type = CfprApManagedObjectDn
_CfprApFabricLanCloudDn_Object = MibTableColumn
cfprApFabricLanCloudDn = _CfprApFabricLanCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 2),
    _CfprApFabricLanCloudDn_Type()
)
cfprApFabricLanCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudDn.setStatus("current")
_CfprApFabricLanCloudRn_Type = SnmpAdminString
_CfprApFabricLanCloudRn_Object = MibTableColumn
cfprApFabricLanCloudRn = _CfprApFabricLanCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 3),
    _CfprApFabricLanCloudRn_Type()
)
cfprApFabricLanCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudRn.setStatus("current")
_CfprApFabricLanCloudFsmDescr_Type = SnmpAdminString
_CfprApFabricLanCloudFsmDescr_Object = MibTableColumn
cfprApFabricLanCloudFsmDescr = _CfprApFabricLanCloudFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 4),
    _CfprApFabricLanCloudFsmDescr_Type()
)
cfprApFabricLanCloudFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmDescr.setStatus("current")
_CfprApFabricLanCloudFsmPrev_Type = SnmpAdminString
_CfprApFabricLanCloudFsmPrev_Object = MibTableColumn
cfprApFabricLanCloudFsmPrev = _CfprApFabricLanCloudFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 5),
    _CfprApFabricLanCloudFsmPrev_Type()
)
cfprApFabricLanCloudFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmPrev.setStatus("current")
_CfprApFabricLanCloudFsmProgr_Type = Gauge32
_CfprApFabricLanCloudFsmProgr_Object = MibTableColumn
cfprApFabricLanCloudFsmProgr = _CfprApFabricLanCloudFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 6),
    _CfprApFabricLanCloudFsmProgr_Type()
)
cfprApFabricLanCloudFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmProgr.setStatus("current")
_CfprApFabricLanCloudFsmRmtInvErrCode_Type = Gauge32
_CfprApFabricLanCloudFsmRmtInvErrCode_Object = MibTableColumn
cfprApFabricLanCloudFsmRmtInvErrCode = _CfprApFabricLanCloudFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 7),
    _CfprApFabricLanCloudFsmRmtInvErrCode_Type()
)
cfprApFabricLanCloudFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmRmtInvErrCode.setStatus("current")
_CfprApFabricLanCloudFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFabricLanCloudFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFabricLanCloudFsmRmtInvErrDescr = _CfprApFabricLanCloudFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 8),
    _CfprApFabricLanCloudFsmRmtInvErrDescr_Type()
)
cfprApFabricLanCloudFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmRmtInvErrDescr.setStatus("current")
_CfprApFabricLanCloudFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFabricLanCloudFsmRmtInvRslt_Object = MibTableColumn
cfprApFabricLanCloudFsmRmtInvRslt = _CfprApFabricLanCloudFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 9),
    _CfprApFabricLanCloudFsmRmtInvRslt_Type()
)
cfprApFabricLanCloudFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmRmtInvRslt.setStatus("current")
_CfprApFabricLanCloudFsmStageDescr_Type = SnmpAdminString
_CfprApFabricLanCloudFsmStageDescr_Object = MibTableColumn
cfprApFabricLanCloudFsmStageDescr = _CfprApFabricLanCloudFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 10),
    _CfprApFabricLanCloudFsmStageDescr_Type()
)
cfprApFabricLanCloudFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageDescr.setStatus("current")
_CfprApFabricLanCloudFsmStamp_Type = DateAndTime
_CfprApFabricLanCloudFsmStamp_Object = MibTableColumn
cfprApFabricLanCloudFsmStamp = _CfprApFabricLanCloudFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 11),
    _CfprApFabricLanCloudFsmStamp_Type()
)
cfprApFabricLanCloudFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStamp.setStatus("current")
_CfprApFabricLanCloudFsmStatus_Type = SnmpAdminString
_CfprApFabricLanCloudFsmStatus_Object = MibTableColumn
cfprApFabricLanCloudFsmStatus = _CfprApFabricLanCloudFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 12),
    _CfprApFabricLanCloudFsmStatus_Type()
)
cfprApFabricLanCloudFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStatus.setStatus("current")
_CfprApFabricLanCloudFsmTry_Type = Gauge32
_CfprApFabricLanCloudFsmTry_Object = MibTableColumn
cfprApFabricLanCloudFsmTry = _CfprApFabricLanCloudFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 13),
    _CfprApFabricLanCloudFsmTry_Type()
)
cfprApFabricLanCloudFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTry.setStatus("current")
_CfprApFabricLanCloudMacAging_Type = TimeIntervalSec
_CfprApFabricLanCloudMacAging_Object = MibTableColumn
cfprApFabricLanCloudMacAging = _CfprApFabricLanCloudMacAging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 14),
    _CfprApFabricLanCloudMacAging_Type()
)
cfprApFabricLanCloudMacAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudMacAging.setStatus("current")
_CfprApFabricLanCloudMode_Type = CfprApFabricSwitchingMode
_CfprApFabricLanCloudMode_Object = MibTableColumn
cfprApFabricLanCloudMode = _CfprApFabricLanCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 15),
    _CfprApFabricLanCloudMode_Type()
)
cfprApFabricLanCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudMode.setStatus("current")
_CfprApFabricLanCloudVlanCompression_Type = CfprApFabricLanCloudVlanCompression
_CfprApFabricLanCloudVlanCompression_Object = MibTableColumn
cfprApFabricLanCloudVlanCompression = _CfprApFabricLanCloudVlanCompression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 69, 1, 16),
    _CfprApFabricLanCloudVlanCompression_Type()
)
cfprApFabricLanCloudVlanCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudVlanCompression.setStatus("current")
_CfprApFabricLanCloudFsmTable_Object = MibTable
cfprApFabricLanCloudFsmTable = _CfprApFabricLanCloudFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70)
)
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTable.setStatus("current")
_CfprApFabricLanCloudFsmEntry_Object = MibTableRow
cfprApFabricLanCloudFsmEntry = _CfprApFabricLanCloudFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1)
)
cfprApFabricLanCloudFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLanCloudFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmEntry.setStatus("current")
_CfprApFabricLanCloudFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLanCloudFsmInstanceId_Object = MibTableColumn
cfprApFabricLanCloudFsmInstanceId = _CfprApFabricLanCloudFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 1),
    _CfprApFabricLanCloudFsmInstanceId_Type()
)
cfprApFabricLanCloudFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmInstanceId.setStatus("current")
_CfprApFabricLanCloudFsmDn_Type = CfprApManagedObjectDn
_CfprApFabricLanCloudFsmDn_Object = MibTableColumn
cfprApFabricLanCloudFsmDn = _CfprApFabricLanCloudFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 2),
    _CfprApFabricLanCloudFsmDn_Type()
)
cfprApFabricLanCloudFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmDn.setStatus("current")
_CfprApFabricLanCloudFsmRn_Type = SnmpAdminString
_CfprApFabricLanCloudFsmRn_Object = MibTableColumn
cfprApFabricLanCloudFsmRn = _CfprApFabricLanCloudFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 3),
    _CfprApFabricLanCloudFsmRn_Type()
)
cfprApFabricLanCloudFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmRn.setStatus("current")
_CfprApFabricLanCloudFsmCompletionTime_Type = DateAndTime
_CfprApFabricLanCloudFsmCompletionTime_Object = MibTableColumn
cfprApFabricLanCloudFsmCompletionTime = _CfprApFabricLanCloudFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 4),
    _CfprApFabricLanCloudFsmCompletionTime_Type()
)
cfprApFabricLanCloudFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmCompletionTime.setStatus("current")
_CfprApFabricLanCloudFsmCurrentFsm_Type = CfprApFabricLanCloudFsmCurrentFsm
_CfprApFabricLanCloudFsmCurrentFsm_Object = MibTableColumn
cfprApFabricLanCloudFsmCurrentFsm = _CfprApFabricLanCloudFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 5),
    _CfprApFabricLanCloudFsmCurrentFsm_Type()
)
cfprApFabricLanCloudFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmCurrentFsm.setStatus("current")
_CfprApFabricLanCloudFsmDescrData_Type = SnmpAdminString
_CfprApFabricLanCloudFsmDescrData_Object = MibTableColumn
cfprApFabricLanCloudFsmDescrData = _CfprApFabricLanCloudFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 6),
    _CfprApFabricLanCloudFsmDescrData_Type()
)
cfprApFabricLanCloudFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmDescrData.setStatus("current")
_CfprApFabricLanCloudFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFabricLanCloudFsmFsmStatus_Object = MibTableColumn
cfprApFabricLanCloudFsmFsmStatus = _CfprApFabricLanCloudFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 7),
    _CfprApFabricLanCloudFsmFsmStatus_Type()
)
cfprApFabricLanCloudFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmFsmStatus.setStatus("current")
_CfprApFabricLanCloudFsmProgress_Type = Gauge32
_CfprApFabricLanCloudFsmProgress_Object = MibTableColumn
cfprApFabricLanCloudFsmProgress = _CfprApFabricLanCloudFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 8),
    _CfprApFabricLanCloudFsmProgress_Type()
)
cfprApFabricLanCloudFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmProgress.setStatus("current")
_CfprApFabricLanCloudFsmRmtErrCode_Type = Gauge32
_CfprApFabricLanCloudFsmRmtErrCode_Object = MibTableColumn
cfprApFabricLanCloudFsmRmtErrCode = _CfprApFabricLanCloudFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 9),
    _CfprApFabricLanCloudFsmRmtErrCode_Type()
)
cfprApFabricLanCloudFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmRmtErrCode.setStatus("current")
_CfprApFabricLanCloudFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFabricLanCloudFsmRmtErrDescr_Object = MibTableColumn
cfprApFabricLanCloudFsmRmtErrDescr = _CfprApFabricLanCloudFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 10),
    _CfprApFabricLanCloudFsmRmtErrDescr_Type()
)
cfprApFabricLanCloudFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmRmtErrDescr.setStatus("current")
_CfprApFabricLanCloudFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFabricLanCloudFsmRmtRslt_Object = MibTableColumn
cfprApFabricLanCloudFsmRmtRslt = _CfprApFabricLanCloudFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 70, 1, 11),
    _CfprApFabricLanCloudFsmRmtRslt_Type()
)
cfprApFabricLanCloudFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmRmtRslt.setStatus("current")
_CfprApFabricLanCloudFsmStageTable_Object = MibTable
cfprApFabricLanCloudFsmStageTable = _CfprApFabricLanCloudFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71)
)
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageTable.setStatus("current")
_CfprApFabricLanCloudFsmStageEntry_Object = MibTableRow
cfprApFabricLanCloudFsmStageEntry = _CfprApFabricLanCloudFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1)
)
cfprApFabricLanCloudFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLanCloudFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageEntry.setStatus("current")
_CfprApFabricLanCloudFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLanCloudFsmStageInstanceId_Object = MibTableColumn
cfprApFabricLanCloudFsmStageInstanceId = _CfprApFabricLanCloudFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 1),
    _CfprApFabricLanCloudFsmStageInstanceId_Type()
)
cfprApFabricLanCloudFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageInstanceId.setStatus("current")
_CfprApFabricLanCloudFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFabricLanCloudFsmStageDn_Object = MibTableColumn
cfprApFabricLanCloudFsmStageDn = _CfprApFabricLanCloudFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 2),
    _CfprApFabricLanCloudFsmStageDn_Type()
)
cfprApFabricLanCloudFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageDn.setStatus("current")
_CfprApFabricLanCloudFsmStageRn_Type = SnmpAdminString
_CfprApFabricLanCloudFsmStageRn_Object = MibTableColumn
cfprApFabricLanCloudFsmStageRn = _CfprApFabricLanCloudFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 3),
    _CfprApFabricLanCloudFsmStageRn_Type()
)
cfprApFabricLanCloudFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageRn.setStatus("current")
_CfprApFabricLanCloudFsmStageDescrData_Type = SnmpAdminString
_CfprApFabricLanCloudFsmStageDescrData_Object = MibTableColumn
cfprApFabricLanCloudFsmStageDescrData = _CfprApFabricLanCloudFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 4),
    _CfprApFabricLanCloudFsmStageDescrData_Type()
)
cfprApFabricLanCloudFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageDescrData.setStatus("current")
_CfprApFabricLanCloudFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFabricLanCloudFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFabricLanCloudFsmStageLastUpdateTime = _CfprApFabricLanCloudFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 5),
    _CfprApFabricLanCloudFsmStageLastUpdateTime_Type()
)
cfprApFabricLanCloudFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageLastUpdateTime.setStatus("current")
_CfprApFabricLanCloudFsmStageName_Type = CfprApFabricLanCloudFsmStageName
_CfprApFabricLanCloudFsmStageName_Object = MibTableColumn
cfprApFabricLanCloudFsmStageName = _CfprApFabricLanCloudFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 6),
    _CfprApFabricLanCloudFsmStageName_Type()
)
cfprApFabricLanCloudFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageName.setStatus("current")
_CfprApFabricLanCloudFsmStageOrder_Type = Gauge32
_CfprApFabricLanCloudFsmStageOrder_Object = MibTableColumn
cfprApFabricLanCloudFsmStageOrder = _CfprApFabricLanCloudFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 7),
    _CfprApFabricLanCloudFsmStageOrder_Type()
)
cfprApFabricLanCloudFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageOrder.setStatus("current")
_CfprApFabricLanCloudFsmStageRetry_Type = Gauge32
_CfprApFabricLanCloudFsmStageRetry_Object = MibTableColumn
cfprApFabricLanCloudFsmStageRetry = _CfprApFabricLanCloudFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 8),
    _CfprApFabricLanCloudFsmStageRetry_Type()
)
cfprApFabricLanCloudFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageRetry.setStatus("current")
_CfprApFabricLanCloudFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFabricLanCloudFsmStageStageStatus_Object = MibTableColumn
cfprApFabricLanCloudFsmStageStageStatus = _CfprApFabricLanCloudFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 71, 1, 9),
    _CfprApFabricLanCloudFsmStageStageStatus_Type()
)
cfprApFabricLanCloudFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmStageStageStatus.setStatus("current")
_CfprApFabricLanCloudFsmTaskTable_Object = MibTable
cfprApFabricLanCloudFsmTaskTable = _CfprApFabricLanCloudFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72)
)
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskTable.setStatus("current")
_CfprApFabricLanCloudFsmTaskEntry_Object = MibTableRow
cfprApFabricLanCloudFsmTaskEntry = _CfprApFabricLanCloudFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72, 1)
)
cfprApFabricLanCloudFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLanCloudFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskEntry.setStatus("current")
_CfprApFabricLanCloudFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLanCloudFsmTaskInstanceId_Object = MibTableColumn
cfprApFabricLanCloudFsmTaskInstanceId = _CfprApFabricLanCloudFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72, 1, 1),
    _CfprApFabricLanCloudFsmTaskInstanceId_Type()
)
cfprApFabricLanCloudFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskInstanceId.setStatus("current")
_CfprApFabricLanCloudFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFabricLanCloudFsmTaskDn_Object = MibTableColumn
cfprApFabricLanCloudFsmTaskDn = _CfprApFabricLanCloudFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72, 1, 2),
    _CfprApFabricLanCloudFsmTaskDn_Type()
)
cfprApFabricLanCloudFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskDn.setStatus("current")
_CfprApFabricLanCloudFsmTaskRn_Type = SnmpAdminString
_CfprApFabricLanCloudFsmTaskRn_Object = MibTableColumn
cfprApFabricLanCloudFsmTaskRn = _CfprApFabricLanCloudFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72, 1, 3),
    _CfprApFabricLanCloudFsmTaskRn_Type()
)
cfprApFabricLanCloudFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskRn.setStatus("current")
_CfprApFabricLanCloudFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFabricLanCloudFsmTaskCompletion_Object = MibTableColumn
cfprApFabricLanCloudFsmTaskCompletion = _CfprApFabricLanCloudFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72, 1, 4),
    _CfprApFabricLanCloudFsmTaskCompletion_Type()
)
cfprApFabricLanCloudFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskCompletion.setStatus("current")
_CfprApFabricLanCloudFsmTaskFlags_Type = CfprApFsmFlags
_CfprApFabricLanCloudFsmTaskFlags_Object = MibTableColumn
cfprApFabricLanCloudFsmTaskFlags = _CfprApFabricLanCloudFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72, 1, 5),
    _CfprApFabricLanCloudFsmTaskFlags_Type()
)
cfprApFabricLanCloudFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskFlags.setStatus("current")
_CfprApFabricLanCloudFsmTaskItem_Type = CfprApFabricLanCloudFsmTaskItem
_CfprApFabricLanCloudFsmTaskItem_Object = MibTableColumn
cfprApFabricLanCloudFsmTaskItem = _CfprApFabricLanCloudFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72, 1, 6),
    _CfprApFabricLanCloudFsmTaskItem_Type()
)
cfprApFabricLanCloudFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskItem.setStatus("current")
_CfprApFabricLanCloudFsmTaskSeqId_Type = Gauge32
_CfprApFabricLanCloudFsmTaskSeqId_Object = MibTableColumn
cfprApFabricLanCloudFsmTaskSeqId = _CfprApFabricLanCloudFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 72, 1, 7),
    _CfprApFabricLanCloudFsmTaskSeqId_Type()
)
cfprApFabricLanCloudFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanCloudFsmTaskSeqId.setStatus("current")
_CfprApFabricLanMonCloudTable_Object = MibTable
cfprApFabricLanMonCloudTable = _CfprApFabricLanMonCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 73)
)
if mibBuilder.loadTexts:
    cfprApFabricLanMonCloudTable.setStatus("current")
_CfprApFabricLanMonCloudEntry_Object = MibTableRow
cfprApFabricLanMonCloudEntry = _CfprApFabricLanMonCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 73, 1)
)
cfprApFabricLanMonCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLanMonCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLanMonCloudEntry.setStatus("current")
_CfprApFabricLanMonCloudInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLanMonCloudInstanceId_Object = MibTableColumn
cfprApFabricLanMonCloudInstanceId = _CfprApFabricLanMonCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 73, 1, 1),
    _CfprApFabricLanMonCloudInstanceId_Type()
)
cfprApFabricLanMonCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLanMonCloudInstanceId.setStatus("current")
_CfprApFabricLanMonCloudDn_Type = CfprApManagedObjectDn
_CfprApFabricLanMonCloudDn_Object = MibTableColumn
cfprApFabricLanMonCloudDn = _CfprApFabricLanMonCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 73, 1, 2),
    _CfprApFabricLanMonCloudDn_Type()
)
cfprApFabricLanMonCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanMonCloudDn.setStatus("current")
_CfprApFabricLanMonCloudRn_Type = SnmpAdminString
_CfprApFabricLanMonCloudRn_Object = MibTableColumn
cfprApFabricLanMonCloudRn = _CfprApFabricLanMonCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 73, 1, 3),
    _CfprApFabricLanMonCloudRn_Type()
)
cfprApFabricLanMonCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanMonCloudRn.setStatus("current")
_CfprApFabricLanMonCloudMode_Type = CfprApFabricSwitchingMode
_CfprApFabricLanMonCloudMode_Object = MibTableColumn
cfprApFabricLanMonCloudMode = _CfprApFabricLanMonCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 73, 1, 4),
    _CfprApFabricLanMonCloudMode_Type()
)
cfprApFabricLanMonCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanMonCloudMode.setStatus("current")
_CfprApFabricLanPinGroupTable_Object = MibTable
cfprApFabricLanPinGroupTable = _CfprApFabricLanPinGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74)
)
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupTable.setStatus("current")
_CfprApFabricLanPinGroupEntry_Object = MibTableRow
cfprApFabricLanPinGroupEntry = _CfprApFabricLanPinGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1)
)
cfprApFabricLanPinGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLanPinGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupEntry.setStatus("current")
_CfprApFabricLanPinGroupInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLanPinGroupInstanceId_Object = MibTableColumn
cfprApFabricLanPinGroupInstanceId = _CfprApFabricLanPinGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 1),
    _CfprApFabricLanPinGroupInstanceId_Type()
)
cfprApFabricLanPinGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupInstanceId.setStatus("current")
_CfprApFabricLanPinGroupDn_Type = CfprApManagedObjectDn
_CfprApFabricLanPinGroupDn_Object = MibTableColumn
cfprApFabricLanPinGroupDn = _CfprApFabricLanPinGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 2),
    _CfprApFabricLanPinGroupDn_Type()
)
cfprApFabricLanPinGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupDn.setStatus("current")
_CfprApFabricLanPinGroupRn_Type = SnmpAdminString
_CfprApFabricLanPinGroupRn_Object = MibTableColumn
cfprApFabricLanPinGroupRn = _CfprApFabricLanPinGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 3),
    _CfprApFabricLanPinGroupRn_Type()
)
cfprApFabricLanPinGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupRn.setStatus("current")
_CfprApFabricLanPinGroupDescr_Type = SnmpAdminString
_CfprApFabricLanPinGroupDescr_Object = MibTableColumn
cfprApFabricLanPinGroupDescr = _CfprApFabricLanPinGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 4),
    _CfprApFabricLanPinGroupDescr_Type()
)
cfprApFabricLanPinGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupDescr.setStatus("current")
_CfprApFabricLanPinGroupIntId_Type = SnmpAdminString
_CfprApFabricLanPinGroupIntId_Object = MibTableColumn
cfprApFabricLanPinGroupIntId = _CfprApFabricLanPinGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 5),
    _CfprApFabricLanPinGroupIntId_Type()
)
cfprApFabricLanPinGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupIntId.setStatus("current")
_CfprApFabricLanPinGroupName_Type = SnmpAdminString
_CfprApFabricLanPinGroupName_Object = MibTableColumn
cfprApFabricLanPinGroupName = _CfprApFabricLanPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 6),
    _CfprApFabricLanPinGroupName_Type()
)
cfprApFabricLanPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupName.setStatus("current")
_CfprApFabricLanPinGroupPolicyLevel_Type = Gauge32
_CfprApFabricLanPinGroupPolicyLevel_Object = MibTableColumn
cfprApFabricLanPinGroupPolicyLevel = _CfprApFabricLanPinGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 7),
    _CfprApFabricLanPinGroupPolicyLevel_Type()
)
cfprApFabricLanPinGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupPolicyLevel.setStatus("current")
_CfprApFabricLanPinGroupPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricLanPinGroupPolicyOwner_Object = MibTableColumn
cfprApFabricLanPinGroupPolicyOwner = _CfprApFabricLanPinGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 8),
    _CfprApFabricLanPinGroupPolicyOwner_Type()
)
cfprApFabricLanPinGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupPolicyOwner.setStatus("current")
_CfprApFabricLanPinGroupSize_Type = Gauge32
_CfprApFabricLanPinGroupSize_Object = MibTableColumn
cfprApFabricLanPinGroupSize = _CfprApFabricLanPinGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 74, 1, 9),
    _CfprApFabricLanPinGroupSize_Type()
)
cfprApFabricLanPinGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinGroupSize.setStatus("current")
_CfprApFabricLanPinTargetTable_Object = MibTable
cfprApFabricLanPinTargetTable = _CfprApFabricLanPinTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 75)
)
if mibBuilder.loadTexts:
    cfprApFabricLanPinTargetTable.setStatus("current")
_CfprApFabricLanPinTargetEntry_Object = MibTableRow
cfprApFabricLanPinTargetEntry = _CfprApFabricLanPinTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 75, 1)
)
cfprApFabricLanPinTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLanPinTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLanPinTargetEntry.setStatus("current")
_CfprApFabricLanPinTargetInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLanPinTargetInstanceId_Object = MibTableColumn
cfprApFabricLanPinTargetInstanceId = _CfprApFabricLanPinTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 75, 1, 1),
    _CfprApFabricLanPinTargetInstanceId_Type()
)
cfprApFabricLanPinTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLanPinTargetInstanceId.setStatus("current")
_CfprApFabricLanPinTargetDn_Type = CfprApManagedObjectDn
_CfprApFabricLanPinTargetDn_Object = MibTableColumn
cfprApFabricLanPinTargetDn = _CfprApFabricLanPinTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 75, 1, 2),
    _CfprApFabricLanPinTargetDn_Type()
)
cfprApFabricLanPinTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinTargetDn.setStatus("current")
_CfprApFabricLanPinTargetRn_Type = SnmpAdminString
_CfprApFabricLanPinTargetRn_Object = MibTableColumn
cfprApFabricLanPinTargetRn = _CfprApFabricLanPinTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 75, 1, 3),
    _CfprApFabricLanPinTargetRn_Type()
)
cfprApFabricLanPinTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinTargetRn.setStatus("current")
_CfprApFabricLanPinTargetEpDn_Type = SnmpAdminString
_CfprApFabricLanPinTargetEpDn_Object = MibTableColumn
cfprApFabricLanPinTargetEpDn = _CfprApFabricLanPinTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 75, 1, 4),
    _CfprApFabricLanPinTargetEpDn_Type()
)
cfprApFabricLanPinTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinTargetEpDn.setStatus("current")
_CfprApFabricLanPinTargetFabricId_Type = SnmpAdminString
_CfprApFabricLanPinTargetFabricId_Object = MibTableColumn
cfprApFabricLanPinTargetFabricId = _CfprApFabricLanPinTargetFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 75, 1, 5),
    _CfprApFabricLanPinTargetFabricId_Type()
)
cfprApFabricLanPinTargetFabricId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinTargetFabricId.setStatus("current")
_CfprApFabricLanPinTargetTargetStatus_Type = CfprApFabricTargetStatus
_CfprApFabricLanPinTargetTargetStatus_Object = MibTableColumn
cfprApFabricLanPinTargetTargetStatus = _CfprApFabricLanPinTargetTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 75, 1, 6),
    _CfprApFabricLanPinTargetTargetStatus_Type()
)
cfprApFabricLanPinTargetTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLanPinTargetTargetStatus.setStatus("current")
_CfprApFabricLastAckedSlotTable_Object = MibTable
cfprApFabricLastAckedSlotTable = _CfprApFabricLastAckedSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76)
)
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotTable.setStatus("current")
_CfprApFabricLastAckedSlotEntry_Object = MibTableRow
cfprApFabricLastAckedSlotEntry = _CfprApFabricLastAckedSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76, 1)
)
cfprApFabricLastAckedSlotEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLastAckedSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotEntry.setStatus("current")
_CfprApFabricLastAckedSlotInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLastAckedSlotInstanceId_Object = MibTableColumn
cfprApFabricLastAckedSlotInstanceId = _CfprApFabricLastAckedSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76, 1, 1),
    _CfprApFabricLastAckedSlotInstanceId_Type()
)
cfprApFabricLastAckedSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotInstanceId.setStatus("current")
_CfprApFabricLastAckedSlotDn_Type = CfprApManagedObjectDn
_CfprApFabricLastAckedSlotDn_Object = MibTableColumn
cfprApFabricLastAckedSlotDn = _CfprApFabricLastAckedSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76, 1, 2),
    _CfprApFabricLastAckedSlotDn_Type()
)
cfprApFabricLastAckedSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotDn.setStatus("current")
_CfprApFabricLastAckedSlotRn_Type = SnmpAdminString
_CfprApFabricLastAckedSlotRn_Object = MibTableColumn
cfprApFabricLastAckedSlotRn = _CfprApFabricLastAckedSlotRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76, 1, 3),
    _CfprApFabricLastAckedSlotRn_Type()
)
cfprApFabricLastAckedSlotRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotRn.setStatus("current")
_CfprApFabricLastAckedSlotBoardAggregationRole_Type = CfprApEquipmentBoardAggregationRole
_CfprApFabricLastAckedSlotBoardAggregationRole_Object = MibTableColumn
cfprApFabricLastAckedSlotBoardAggregationRole = _CfprApFabricLastAckedSlotBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76, 1, 4),
    _CfprApFabricLastAckedSlotBoardAggregationRole_Type()
)
cfprApFabricLastAckedSlotBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotBoardAggregationRole.setStatus("current")
_CfprApFabricLastAckedSlotChassisId_Type = Gauge32
_CfprApFabricLastAckedSlotChassisId_Object = MibTableColumn
cfprApFabricLastAckedSlotChassisId = _CfprApFabricLastAckedSlotChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76, 1, 5),
    _CfprApFabricLastAckedSlotChassisId_Type()
)
cfprApFabricLastAckedSlotChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotChassisId.setStatus("current")
_CfprApFabricLastAckedSlotSlotId_Type = Gauge32
_CfprApFabricLastAckedSlotSlotId_Object = MibTableColumn
cfprApFabricLastAckedSlotSlotId = _CfprApFabricLastAckedSlotSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76, 1, 6),
    _CfprApFabricLastAckedSlotSlotId_Type()
)
cfprApFabricLastAckedSlotSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotSlotId.setStatus("current")
_CfprApFabricLastAckedSlotSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricLastAckedSlotSwitchId_Object = MibTableColumn
cfprApFabricLastAckedSlotSwitchId = _CfprApFabricLastAckedSlotSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 76, 1, 7),
    _CfprApFabricLastAckedSlotSwitchId_Type()
)
cfprApFabricLastAckedSlotSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLastAckedSlotSwitchId.setStatus("current")
_CfprApFabricLocaleTable_Object = MibTable
cfprApFabricLocaleTable = _CfprApFabricLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77)
)
if mibBuilder.loadTexts:
    cfprApFabricLocaleTable.setStatus("current")
_CfprApFabricLocaleEntry_Object = MibTableRow
cfprApFabricLocaleEntry = _CfprApFabricLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1)
)
cfprApFabricLocaleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricLocaleEntry.setStatus("current")
_CfprApFabricLocaleInstanceId_Type = CfprApManagedObjectId
_CfprApFabricLocaleInstanceId_Object = MibTableColumn
cfprApFabricLocaleInstanceId = _CfprApFabricLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 1),
    _CfprApFabricLocaleInstanceId_Type()
)
cfprApFabricLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricLocaleInstanceId.setStatus("current")
_CfprApFabricLocaleDn_Type = CfprApManagedObjectDn
_CfprApFabricLocaleDn_Object = MibTableColumn
cfprApFabricLocaleDn = _CfprApFabricLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 2),
    _CfprApFabricLocaleDn_Type()
)
cfprApFabricLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleDn.setStatus("current")
_CfprApFabricLocaleRn_Type = SnmpAdminString
_CfprApFabricLocaleRn_Object = MibTableColumn
cfprApFabricLocaleRn = _CfprApFabricLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 3),
    _CfprApFabricLocaleRn_Type()
)
cfprApFabricLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleRn.setStatus("current")
_CfprApFabricLocaleCType_Type = Gauge32
_CfprApFabricLocaleCType_Object = MibTableColumn
cfprApFabricLocaleCType = _CfprApFabricLocaleCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 4),
    _CfprApFabricLocaleCType_Type()
)
cfprApFabricLocaleCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleCType.setStatus("current")
_CfprApFabricLocaleChassisId_Type = Gauge32
_CfprApFabricLocaleChassisId_Object = MibTableColumn
cfprApFabricLocaleChassisId = _CfprApFabricLocaleChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 5),
    _CfprApFabricLocaleChassisId_Type()
)
cfprApFabricLocaleChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleChassisId.setStatus("current")
_CfprApFabricLocaleLocale_Type = CfprApNetworkLocale
_CfprApFabricLocaleLocale_Object = MibTableColumn
cfprApFabricLocaleLocale = _CfprApFabricLocaleLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 6),
    _CfprApFabricLocaleLocale_Type()
)
cfprApFabricLocaleLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleLocale.setStatus("current")
_CfprApFabricLocaleName_Type = SnmpAdminString
_CfprApFabricLocaleName_Object = MibTableColumn
cfprApFabricLocaleName = _CfprApFabricLocaleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 7),
    _CfprApFabricLocaleName_Type()
)
cfprApFabricLocaleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleName.setStatus("current")
_CfprApFabricLocaleSide_Type = CfprApNetworkSide
_CfprApFabricLocaleSide_Object = MibTableColumn
cfprApFabricLocaleSide = _CfprApFabricLocaleSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 8),
    _CfprApFabricLocaleSide_Type()
)
cfprApFabricLocaleSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleSide.setStatus("current")
_CfprApFabricLocaleSlotId_Type = Gauge32
_CfprApFabricLocaleSlotId_Object = MibTableColumn
cfprApFabricLocaleSlotId = _CfprApFabricLocaleSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 9),
    _CfprApFabricLocaleSlotId_Type()
)
cfprApFabricLocaleSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleSlotId.setStatus("current")
_CfprApFabricLocaleSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricLocaleSwitchId_Object = MibTableColumn
cfprApFabricLocaleSwitchId = _CfprApFabricLocaleSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 10),
    _CfprApFabricLocaleSwitchId_Type()
)
cfprApFabricLocaleSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleSwitchId.setStatus("current")
_CfprApFabricLocaleTransport_Type = CfprApNetworkTransport
_CfprApFabricLocaleTransport_Object = MibTableColumn
cfprApFabricLocaleTransport = _CfprApFabricLocaleTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 11),
    _CfprApFabricLocaleTransport_Type()
)
cfprApFabricLocaleTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleTransport.setStatus("current")
_CfprApFabricLocaleType_Type = CfprApNetworkConnectionType
_CfprApFabricLocaleType_Object = MibTableColumn
cfprApFabricLocaleType = _CfprApFabricLocaleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 77, 1, 12),
    _CfprApFabricLocaleType_Type()
)
cfprApFabricLocaleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricLocaleType.setStatus("current")
_CfprApFabricMulticastPolicyTable_Object = MibTable
cfprApFabricMulticastPolicyTable = _CfprApFabricMulticastPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78)
)
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyTable.setStatus("current")
_CfprApFabricMulticastPolicyEntry_Object = MibTableRow
cfprApFabricMulticastPolicyEntry = _CfprApFabricMulticastPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1)
)
cfprApFabricMulticastPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricMulticastPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyEntry.setStatus("current")
_CfprApFabricMulticastPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFabricMulticastPolicyInstanceId_Object = MibTableColumn
cfprApFabricMulticastPolicyInstanceId = _CfprApFabricMulticastPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 1),
    _CfprApFabricMulticastPolicyInstanceId_Type()
)
cfprApFabricMulticastPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyInstanceId.setStatus("current")
_CfprApFabricMulticastPolicyDn_Type = CfprApManagedObjectDn
_CfprApFabricMulticastPolicyDn_Object = MibTableColumn
cfprApFabricMulticastPolicyDn = _CfprApFabricMulticastPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 2),
    _CfprApFabricMulticastPolicyDn_Type()
)
cfprApFabricMulticastPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyDn.setStatus("current")
_CfprApFabricMulticastPolicyRn_Type = SnmpAdminString
_CfprApFabricMulticastPolicyRn_Object = MibTableColumn
cfprApFabricMulticastPolicyRn = _CfprApFabricMulticastPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 3),
    _CfprApFabricMulticastPolicyRn_Type()
)
cfprApFabricMulticastPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyRn.setStatus("current")
_CfprApFabricMulticastPolicyDescr_Type = SnmpAdminString
_CfprApFabricMulticastPolicyDescr_Object = MibTableColumn
cfprApFabricMulticastPolicyDescr = _CfprApFabricMulticastPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 4),
    _CfprApFabricMulticastPolicyDescr_Type()
)
cfprApFabricMulticastPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyDescr.setStatus("current")
_CfprApFabricMulticastPolicyIntId_Type = SnmpAdminString
_CfprApFabricMulticastPolicyIntId_Object = MibTableColumn
cfprApFabricMulticastPolicyIntId = _CfprApFabricMulticastPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 5),
    _CfprApFabricMulticastPolicyIntId_Type()
)
cfprApFabricMulticastPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyIntId.setStatus("current")
_CfprApFabricMulticastPolicyName_Type = SnmpAdminString
_CfprApFabricMulticastPolicyName_Object = MibTableColumn
cfprApFabricMulticastPolicyName = _CfprApFabricMulticastPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 6),
    _CfprApFabricMulticastPolicyName_Type()
)
cfprApFabricMulticastPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyName.setStatus("current")
_CfprApFabricMulticastPolicyPolicyLevel_Type = Gauge32
_CfprApFabricMulticastPolicyPolicyLevel_Object = MibTableColumn
cfprApFabricMulticastPolicyPolicyLevel = _CfprApFabricMulticastPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 7),
    _CfprApFabricMulticastPolicyPolicyLevel_Type()
)
cfprApFabricMulticastPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyPolicyLevel.setStatus("current")
_CfprApFabricMulticastPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricMulticastPolicyPolicyOwner_Object = MibTableColumn
cfprApFabricMulticastPolicyPolicyOwner = _CfprApFabricMulticastPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 8),
    _CfprApFabricMulticastPolicyPolicyOwner_Type()
)
cfprApFabricMulticastPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyPolicyOwner.setStatus("current")
_CfprApFabricMulticastPolicyQuerierIpAddr_Type = InetAddressIPv4
_CfprApFabricMulticastPolicyQuerierIpAddr_Object = MibTableColumn
cfprApFabricMulticastPolicyQuerierIpAddr = _CfprApFabricMulticastPolicyQuerierIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 9),
    _CfprApFabricMulticastPolicyQuerierIpAddr_Type()
)
cfprApFabricMulticastPolicyQuerierIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyQuerierIpAddr.setStatus("current")
_CfprApFabricMulticastPolicyQuerierState_Type = CfprApFabricQuerierType
_CfprApFabricMulticastPolicyQuerierState_Object = MibTableColumn
cfprApFabricMulticastPolicyQuerierState = _CfprApFabricMulticastPolicyQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 10),
    _CfprApFabricMulticastPolicyQuerierState_Type()
)
cfprApFabricMulticastPolicyQuerierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicyQuerierState.setStatus("current")
_CfprApFabricMulticastPolicySnoopingState_Type = CfprApFabricSnoopingType
_CfprApFabricMulticastPolicySnoopingState_Object = MibTableColumn
cfprApFabricMulticastPolicySnoopingState = _CfprApFabricMulticastPolicySnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 78, 1, 11),
    _CfprApFabricMulticastPolicySnoopingState_Type()
)
cfprApFabricMulticastPolicySnoopingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricMulticastPolicySnoopingState.setStatus("current")
_CfprApFabricNetGroupTable_Object = MibTable
cfprApFabricNetGroupTable = _CfprApFabricNetGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79)
)
if mibBuilder.loadTexts:
    cfprApFabricNetGroupTable.setStatus("current")
_CfprApFabricNetGroupEntry_Object = MibTableRow
cfprApFabricNetGroupEntry = _CfprApFabricNetGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1)
)
cfprApFabricNetGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricNetGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricNetGroupEntry.setStatus("current")
_CfprApFabricNetGroupInstanceId_Type = CfprApManagedObjectId
_CfprApFabricNetGroupInstanceId_Object = MibTableColumn
cfprApFabricNetGroupInstanceId = _CfprApFabricNetGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 1),
    _CfprApFabricNetGroupInstanceId_Type()
)
cfprApFabricNetGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupInstanceId.setStatus("current")
_CfprApFabricNetGroupDn_Type = CfprApManagedObjectDn
_CfprApFabricNetGroupDn_Object = MibTableColumn
cfprApFabricNetGroupDn = _CfprApFabricNetGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 2),
    _CfprApFabricNetGroupDn_Type()
)
cfprApFabricNetGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupDn.setStatus("current")
_CfprApFabricNetGroupRn_Type = SnmpAdminString
_CfprApFabricNetGroupRn_Object = MibTableColumn
cfprApFabricNetGroupRn = _CfprApFabricNetGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 3),
    _CfprApFabricNetGroupRn_Type()
)
cfprApFabricNetGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupRn.setStatus("current")
_CfprApFabricNetGroupAssigned_Type = Gauge32
_CfprApFabricNetGroupAssigned_Object = MibTableColumn
cfprApFabricNetGroupAssigned = _CfprApFabricNetGroupAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 4),
    _CfprApFabricNetGroupAssigned_Type()
)
cfprApFabricNetGroupAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupAssigned.setStatus("current")
_CfprApFabricNetGroupAssignmentOrder_Type = CfprApPoolPoolAssignmentOrder
_CfprApFabricNetGroupAssignmentOrder_Object = MibTableColumn
cfprApFabricNetGroupAssignmentOrder = _CfprApFabricNetGroupAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 5),
    _CfprApFabricNetGroupAssignmentOrder_Type()
)
cfprApFabricNetGroupAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupAssignmentOrder.setStatus("current")
_CfprApFabricNetGroupDescr_Type = SnmpAdminString
_CfprApFabricNetGroupDescr_Object = MibTableColumn
cfprApFabricNetGroupDescr = _CfprApFabricNetGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 6),
    _CfprApFabricNetGroupDescr_Type()
)
cfprApFabricNetGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupDescr.setStatus("current")
_CfprApFabricNetGroupId_Type = Gauge32
_CfprApFabricNetGroupId_Object = MibTableColumn
cfprApFabricNetGroupId = _CfprApFabricNetGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 7),
    _CfprApFabricNetGroupId_Type()
)
cfprApFabricNetGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupId.setStatus("current")
_CfprApFabricNetGroupIntId_Type = SnmpAdminString
_CfprApFabricNetGroupIntId_Object = MibTableColumn
cfprApFabricNetGroupIntId = _CfprApFabricNetGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 8),
    _CfprApFabricNetGroupIntId_Type()
)
cfprApFabricNetGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupIntId.setStatus("current")
_CfprApFabricNetGroupName_Type = SnmpAdminString
_CfprApFabricNetGroupName_Object = MibTableColumn
cfprApFabricNetGroupName = _CfprApFabricNetGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 9),
    _CfprApFabricNetGroupName_Type()
)
cfprApFabricNetGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupName.setStatus("current")
_CfprApFabricNetGroupNativeNet_Type = SnmpAdminString
_CfprApFabricNetGroupNativeNet_Object = MibTableColumn
cfprApFabricNetGroupNativeNet = _CfprApFabricNetGroupNativeNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 10),
    _CfprApFabricNetGroupNativeNet_Type()
)
cfprApFabricNetGroupNativeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupNativeNet.setStatus("current")
_CfprApFabricNetGroupNativeNetDn_Type = SnmpAdminString
_CfprApFabricNetGroupNativeNetDn_Object = MibTableColumn
cfprApFabricNetGroupNativeNetDn = _CfprApFabricNetGroupNativeNetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 11),
    _CfprApFabricNetGroupNativeNetDn_Type()
)
cfprApFabricNetGroupNativeNetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupNativeNetDn.setStatus("current")
_CfprApFabricNetGroupOwner_Type = CfprApFabricOwner
_CfprApFabricNetGroupOwner_Object = MibTableColumn
cfprApFabricNetGroupOwner = _CfprApFabricNetGroupOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 12),
    _CfprApFabricNetGroupOwner_Type()
)
cfprApFabricNetGroupOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupOwner.setStatus("current")
_CfprApFabricNetGroupPeerDn_Type = SnmpAdminString
_CfprApFabricNetGroupPeerDn_Object = MibTableColumn
cfprApFabricNetGroupPeerDn = _CfprApFabricNetGroupPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 13),
    _CfprApFabricNetGroupPeerDn_Type()
)
cfprApFabricNetGroupPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupPeerDn.setStatus("current")
_CfprApFabricNetGroupPolicyLevel_Type = Gauge32
_CfprApFabricNetGroupPolicyLevel_Object = MibTableColumn
cfprApFabricNetGroupPolicyLevel = _CfprApFabricNetGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 14),
    _CfprApFabricNetGroupPolicyLevel_Type()
)
cfprApFabricNetGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupPolicyLevel.setStatus("current")
_CfprApFabricNetGroupPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricNetGroupPolicyOwner_Object = MibTableColumn
cfprApFabricNetGroupPolicyOwner = _CfprApFabricNetGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 15),
    _CfprApFabricNetGroupPolicyOwner_Type()
)
cfprApFabricNetGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupPolicyOwner.setStatus("current")
_CfprApFabricNetGroupSize_Type = Gauge32
_CfprApFabricNetGroupSize_Object = MibTableColumn
cfprApFabricNetGroupSize = _CfprApFabricNetGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 16),
    _CfprApFabricNetGroupSize_Type()
)
cfprApFabricNetGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupSize.setStatus("current")
_CfprApFabricNetGroupSwitchId_Type = CfprApFabricNetGroupSwitchId
_CfprApFabricNetGroupSwitchId_Object = MibTableColumn
cfprApFabricNetGroupSwitchId = _CfprApFabricNetGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 17),
    _CfprApFabricNetGroupSwitchId_Type()
)
cfprApFabricNetGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupSwitchId.setStatus("current")
_CfprApFabricNetGroupType_Type = CfprApFabricNetGroupType
_CfprApFabricNetGroupType_Object = MibTableColumn
cfprApFabricNetGroupType = _CfprApFabricNetGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 79, 1, 18),
    _CfprApFabricNetGroupType_Type()
)
cfprApFabricNetGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricNetGroupType.setStatus("current")
_CfprApFabricOrgVlanPolicyTable_Object = MibTable
cfprApFabricOrgVlanPolicyTable = _CfprApFabricOrgVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 90)
)
if mibBuilder.loadTexts:
    cfprApFabricOrgVlanPolicyTable.setStatus("current")
_CfprApFabricOrgVlanPolicyEntry_Object = MibTableRow
cfprApFabricOrgVlanPolicyEntry = _CfprApFabricOrgVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 90, 1)
)
cfprApFabricOrgVlanPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricOrgVlanPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricOrgVlanPolicyEntry.setStatus("current")
_CfprApFabricOrgVlanPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFabricOrgVlanPolicyInstanceId_Object = MibTableColumn
cfprApFabricOrgVlanPolicyInstanceId = _CfprApFabricOrgVlanPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 90, 1, 1),
    _CfprApFabricOrgVlanPolicyInstanceId_Type()
)
cfprApFabricOrgVlanPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricOrgVlanPolicyInstanceId.setStatus("current")
_CfprApFabricOrgVlanPolicyDn_Type = CfprApManagedObjectDn
_CfprApFabricOrgVlanPolicyDn_Object = MibTableColumn
cfprApFabricOrgVlanPolicyDn = _CfprApFabricOrgVlanPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 90, 1, 2),
    _CfprApFabricOrgVlanPolicyDn_Type()
)
cfprApFabricOrgVlanPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricOrgVlanPolicyDn.setStatus("current")
_CfprApFabricOrgVlanPolicyRn_Type = SnmpAdminString
_CfprApFabricOrgVlanPolicyRn_Object = MibTableColumn
cfprApFabricOrgVlanPolicyRn = _CfprApFabricOrgVlanPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 90, 1, 3),
    _CfprApFabricOrgVlanPolicyRn_Type()
)
cfprApFabricOrgVlanPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricOrgVlanPolicyRn.setStatus("current")
_CfprApFabricOrgVlanPolicyAdminState_Type = CfprApFabricAdminState
_CfprApFabricOrgVlanPolicyAdminState_Object = MibTableColumn
cfprApFabricOrgVlanPolicyAdminState = _CfprApFabricOrgVlanPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 90, 1, 4),
    _CfprApFabricOrgVlanPolicyAdminState_Type()
)
cfprApFabricOrgVlanPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricOrgVlanPolicyAdminState.setStatus("current")
_CfprApFabricOrgVlanPolicyName_Type = SnmpAdminString
_CfprApFabricOrgVlanPolicyName_Object = MibTableColumn
cfprApFabricOrgVlanPolicyName = _CfprApFabricOrgVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 90, 1, 5),
    _CfprApFabricOrgVlanPolicyName_Type()
)
cfprApFabricOrgVlanPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricOrgVlanPolicyName.setStatus("current")
_CfprApFabricPathTable_Object = MibTable
cfprApFabricPathTable = _CfprApFabricPathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91)
)
if mibBuilder.loadTexts:
    cfprApFabricPathTable.setStatus("current")
_CfprApFabricPathEntry_Object = MibTableRow
cfprApFabricPathEntry = _CfprApFabricPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1)
)
cfprApFabricPathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricPathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricPathEntry.setStatus("current")
_CfprApFabricPathInstanceId_Type = CfprApManagedObjectId
_CfprApFabricPathInstanceId_Object = MibTableColumn
cfprApFabricPathInstanceId = _CfprApFabricPathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 1),
    _CfprApFabricPathInstanceId_Type()
)
cfprApFabricPathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricPathInstanceId.setStatus("current")
_CfprApFabricPathDn_Type = CfprApManagedObjectDn
_CfprApFabricPathDn_Object = MibTableColumn
cfprApFabricPathDn = _CfprApFabricPathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 2),
    _CfprApFabricPathDn_Type()
)
cfprApFabricPathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathDn.setStatus("current")
_CfprApFabricPathRn_Type = SnmpAdminString
_CfprApFabricPathRn_Object = MibTableColumn
cfprApFabricPathRn = _CfprApFabricPathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 3),
    _CfprApFabricPathRn_Type()
)
cfprApFabricPathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathRn.setStatus("current")
_CfprApFabricPathCType_Type = Gauge32
_CfprApFabricPathCType_Object = MibTableColumn
cfprApFabricPathCType = _CfprApFabricPathCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 4),
    _CfprApFabricPathCType_Type()
)
cfprApFabricPathCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathCType.setStatus("current")
_CfprApFabricPathChassisId_Type = Gauge32
_CfprApFabricPathChassisId_Object = MibTableColumn
cfprApFabricPathChassisId = _CfprApFabricPathChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 5),
    _CfprApFabricPathChassisId_Type()
)
cfprApFabricPathChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathChassisId.setStatus("current")
_CfprApFabricPathEnacp_Type = Gauge32
_CfprApFabricPathEnacp_Object = MibTableColumn
cfprApFabricPathEnacp = _CfprApFabricPathEnacp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 6),
    _CfprApFabricPathEnacp_Type()
)
cfprApFabricPathEnacp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEnacp.setStatus("current")
_CfprApFabricPathId_Type = Gauge32
_CfprApFabricPathId_Object = MibTableColumn
cfprApFabricPathId = _CfprApFabricPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 7),
    _CfprApFabricPathId_Type()
)
cfprApFabricPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathId.setStatus("current")
_CfprApFabricPathLocale_Type = CfprApNetworkLocale
_CfprApFabricPathLocale_Object = MibTableColumn
cfprApFabricPathLocale = _CfprApFabricPathLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 8),
    _CfprApFabricPathLocale_Type()
)
cfprApFabricPathLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathLocale.setStatus("current")
_CfprApFabricPathName_Type = SnmpAdminString
_CfprApFabricPathName_Object = MibTableColumn
cfprApFabricPathName = _CfprApFabricPathName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 9),
    _CfprApFabricPathName_Type()
)
cfprApFabricPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathName.setStatus("current")
_CfprApFabricPathNsSize_Type = Gauge32
_CfprApFabricPathNsSize_Object = MibTableColumn
cfprApFabricPathNsSize = _CfprApFabricPathNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 10),
    _CfprApFabricPathNsSize_Type()
)
cfprApFabricPathNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathNsSize.setStatus("current")
_CfprApFabricPathSide_Type = CfprApNetworkSide
_CfprApFabricPathSide_Object = MibTableColumn
cfprApFabricPathSide = _CfprApFabricPathSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 11),
    _CfprApFabricPathSide_Type()
)
cfprApFabricPathSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathSide.setStatus("current")
_CfprApFabricPathSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricPathSwitchId_Object = MibTableColumn
cfprApFabricPathSwitchId = _CfprApFabricPathSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 12),
    _CfprApFabricPathSwitchId_Type()
)
cfprApFabricPathSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathSwitchId.setStatus("current")
_CfprApFabricPathTransport_Type = CfprApNetworkTransport
_CfprApFabricPathTransport_Object = MibTableColumn
cfprApFabricPathTransport = _CfprApFabricPathTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 13),
    _CfprApFabricPathTransport_Type()
)
cfprApFabricPathTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathTransport.setStatus("current")
_CfprApFabricPathType_Type = CfprApNetworkConnectionType
_CfprApFabricPathType_Object = MibTableColumn
cfprApFabricPathType = _CfprApFabricPathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 91, 1, 14),
    _CfprApFabricPathType_Type()
)
cfprApFabricPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathType.setStatus("current")
_CfprApFabricPathConnTable_Object = MibTable
cfprApFabricPathConnTable = _CfprApFabricPathConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92)
)
if mibBuilder.loadTexts:
    cfprApFabricPathConnTable.setStatus("current")
_CfprApFabricPathConnEntry_Object = MibTableRow
cfprApFabricPathConnEntry = _CfprApFabricPathConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1)
)
cfprApFabricPathConnEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricPathConnInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricPathConnEntry.setStatus("current")
_CfprApFabricPathConnInstanceId_Type = CfprApManagedObjectId
_CfprApFabricPathConnInstanceId_Object = MibTableColumn
cfprApFabricPathConnInstanceId = _CfprApFabricPathConnInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1, 1),
    _CfprApFabricPathConnInstanceId_Type()
)
cfprApFabricPathConnInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricPathConnInstanceId.setStatus("current")
_CfprApFabricPathConnDn_Type = CfprApManagedObjectDn
_CfprApFabricPathConnDn_Object = MibTableColumn
cfprApFabricPathConnDn = _CfprApFabricPathConnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1, 2),
    _CfprApFabricPathConnDn_Type()
)
cfprApFabricPathConnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathConnDn.setStatus("current")
_CfprApFabricPathConnRn_Type = SnmpAdminString
_CfprApFabricPathConnRn_Object = MibTableColumn
cfprApFabricPathConnRn = _CfprApFabricPathConnRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1, 3),
    _CfprApFabricPathConnRn_Type()
)
cfprApFabricPathConnRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathConnRn.setStatus("current")
_CfprApFabricPathConnCType_Type = Gauge32
_CfprApFabricPathConnCType_Object = MibTableColumn
cfprApFabricPathConnCType = _CfprApFabricPathConnCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1, 4),
    _CfprApFabricPathConnCType_Type()
)
cfprApFabricPathConnCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathConnCType.setStatus("current")
_CfprApFabricPathConnLocale_Type = CfprApNetworkLocale
_CfprApFabricPathConnLocale_Object = MibTableColumn
cfprApFabricPathConnLocale = _CfprApFabricPathConnLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1, 5),
    _CfprApFabricPathConnLocale_Type()
)
cfprApFabricPathConnLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathConnLocale.setStatus("current")
_CfprApFabricPathConnName_Type = SnmpAdminString
_CfprApFabricPathConnName_Object = MibTableColumn
cfprApFabricPathConnName = _CfprApFabricPathConnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1, 6),
    _CfprApFabricPathConnName_Type()
)
cfprApFabricPathConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathConnName.setStatus("current")
_CfprApFabricPathConnTransport_Type = CfprApNetworkTransport
_CfprApFabricPathConnTransport_Object = MibTableColumn
cfprApFabricPathConnTransport = _CfprApFabricPathConnTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1, 7),
    _CfprApFabricPathConnTransport_Type()
)
cfprApFabricPathConnTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathConnTransport.setStatus("current")
_CfprApFabricPathConnType_Type = CfprApNetworkConnectionType
_CfprApFabricPathConnType_Object = MibTableColumn
cfprApFabricPathConnType = _CfprApFabricPathConnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 92, 1, 8),
    _CfprApFabricPathConnType_Type()
)
cfprApFabricPathConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathConnType.setStatus("current")
_CfprApFabricPathEpTable_Object = MibTable
cfprApFabricPathEpTable = _CfprApFabricPathEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93)
)
if mibBuilder.loadTexts:
    cfprApFabricPathEpTable.setStatus("current")
_CfprApFabricPathEpEntry_Object = MibTableRow
cfprApFabricPathEpEntry = _CfprApFabricPathEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1)
)
cfprApFabricPathEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricPathEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricPathEpEntry.setStatus("current")
_CfprApFabricPathEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricPathEpInstanceId_Object = MibTableColumn
cfprApFabricPathEpInstanceId = _CfprApFabricPathEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 1),
    _CfprApFabricPathEpInstanceId_Type()
)
cfprApFabricPathEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricPathEpInstanceId.setStatus("current")
_CfprApFabricPathEpDn_Type = CfprApManagedObjectDn
_CfprApFabricPathEpDn_Object = MibTableColumn
cfprApFabricPathEpDn = _CfprApFabricPathEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 2),
    _CfprApFabricPathEpDn_Type()
)
cfprApFabricPathEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpDn.setStatus("current")
_CfprApFabricPathEpRn_Type = SnmpAdminString
_CfprApFabricPathEpRn_Object = MibTableColumn
cfprApFabricPathEpRn = _CfprApFabricPathEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 3),
    _CfprApFabricPathEpRn_Type()
)
cfprApFabricPathEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpRn.setStatus("current")
_CfprApFabricPathEpAggrPortId_Type = Gauge32
_CfprApFabricPathEpAggrPortId_Object = MibTableColumn
cfprApFabricPathEpAggrPortId = _CfprApFabricPathEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 4),
    _CfprApFabricPathEpAggrPortId_Type()
)
cfprApFabricPathEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpAggrPortId.setStatus("current")
_CfprApFabricPathEpCType_Type = Gauge32
_CfprApFabricPathEpCType_Object = MibTableColumn
cfprApFabricPathEpCType = _CfprApFabricPathEpCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 5),
    _CfprApFabricPathEpCType_Type()
)
cfprApFabricPathEpCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpCType.setStatus("current")
_CfprApFabricPathEpChassisId_Type = Gauge32
_CfprApFabricPathEpChassisId_Object = MibTableColumn
cfprApFabricPathEpChassisId = _CfprApFabricPathEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 6),
    _CfprApFabricPathEpChassisId_Type()
)
cfprApFabricPathEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpChassisId.setStatus("current")
_CfprApFabricPathEpDiagLldpTransmit_Type = TruthValue
_CfprApFabricPathEpDiagLldpTransmit_Object = MibTableColumn
cfprApFabricPathEpDiagLldpTransmit = _CfprApFabricPathEpDiagLldpTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 7),
    _CfprApFabricPathEpDiagLldpTransmit_Type()
)
cfprApFabricPathEpDiagLldpTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpDiagLldpTransmit.setStatus("current")
_CfprApFabricPathEpEpDn_Type = SnmpAdminString
_CfprApFabricPathEpEpDn_Object = MibTableColumn
cfprApFabricPathEpEpDn = _CfprApFabricPathEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 8),
    _CfprApFabricPathEpEpDn_Type()
)
cfprApFabricPathEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpEpDn.setStatus("current")
_CfprApFabricPathEpIfRole_Type = CfprApNetworkPortRole
_CfprApFabricPathEpIfRole_Object = MibTableColumn
cfprApFabricPathEpIfRole = _CfprApFabricPathEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 9),
    _CfprApFabricPathEpIfRole_Type()
)
cfprApFabricPathEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpIfRole.setStatus("current")
_CfprApFabricPathEpIfType_Type = CfprApFabricPathEpIfType
_CfprApFabricPathEpIfType_Object = MibTableColumn
cfprApFabricPathEpIfType = _CfprApFabricPathEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 10),
    _CfprApFabricPathEpIfType_Type()
)
cfprApFabricPathEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpIfType.setStatus("current")
_CfprApFabricPathEpLocale_Type = CfprApFabricPathEpLocale
_CfprApFabricPathEpLocale_Object = MibTableColumn
cfprApFabricPathEpLocale = _CfprApFabricPathEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 11),
    _CfprApFabricPathEpLocale_Type()
)
cfprApFabricPathEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpLocale.setStatus("current")
_CfprApFabricPathEpName_Type = SnmpAdminString
_CfprApFabricPathEpName_Object = MibTableColumn
cfprApFabricPathEpName = _CfprApFabricPathEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 12),
    _CfprApFabricPathEpName_Type()
)
cfprApFabricPathEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpName.setStatus("current")
_CfprApFabricPathEpPeerAggrPortId_Type = Gauge32
_CfprApFabricPathEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricPathEpPeerAggrPortId = _CfprApFabricPathEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 13),
    _CfprApFabricPathEpPeerAggrPortId_Type()
)
cfprApFabricPathEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpPeerAggrPortId.setStatus("current")
_CfprApFabricPathEpPeerChassisId_Type = Gauge32
_CfprApFabricPathEpPeerChassisId_Object = MibTableColumn
cfprApFabricPathEpPeerChassisId = _CfprApFabricPathEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 14),
    _CfprApFabricPathEpPeerChassisId_Type()
)
cfprApFabricPathEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpPeerChassisId.setStatus("current")
_CfprApFabricPathEpPeerDn_Type = SnmpAdminString
_CfprApFabricPathEpPeerDn_Object = MibTableColumn
cfprApFabricPathEpPeerDn = _CfprApFabricPathEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 15),
    _CfprApFabricPathEpPeerDn_Type()
)
cfprApFabricPathEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpPeerDn.setStatus("current")
_CfprApFabricPathEpPeerMac_Type = MacAddress
_CfprApFabricPathEpPeerMac_Object = MibTableColumn
cfprApFabricPathEpPeerMac = _CfprApFabricPathEpPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 16),
    _CfprApFabricPathEpPeerMac_Type()
)
cfprApFabricPathEpPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpPeerMac.setStatus("current")
_CfprApFabricPathEpPeerPortId_Type = Gauge32
_CfprApFabricPathEpPeerPortId_Object = MibTableColumn
cfprApFabricPathEpPeerPortId = _CfprApFabricPathEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 17),
    _CfprApFabricPathEpPeerPortId_Type()
)
cfprApFabricPathEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpPeerPortId.setStatus("current")
_CfprApFabricPathEpPeerSlotId_Type = Gauge32
_CfprApFabricPathEpPeerSlotId_Object = MibTableColumn
cfprApFabricPathEpPeerSlotId = _CfprApFabricPathEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 18),
    _CfprApFabricPathEpPeerSlotId_Type()
)
cfprApFabricPathEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpPeerSlotId.setStatus("current")
_CfprApFabricPathEpPortId_Type = Gauge32
_CfprApFabricPathEpPortId_Object = MibTableColumn
cfprApFabricPathEpPortId = _CfprApFabricPathEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 19),
    _CfprApFabricPathEpPortId_Type()
)
cfprApFabricPathEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpPortId.setStatus("current")
_CfprApFabricPathEpSide_Type = CfprApNetworkSide
_CfprApFabricPathEpSide_Object = MibTableColumn
cfprApFabricPathEpSide = _CfprApFabricPathEpSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 20),
    _CfprApFabricPathEpSide_Type()
)
cfprApFabricPathEpSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpSide.setStatus("current")
_CfprApFabricPathEpSlotId_Type = Gauge32
_CfprApFabricPathEpSlotId_Object = MibTableColumn
cfprApFabricPathEpSlotId = _CfprApFabricPathEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 21),
    _CfprApFabricPathEpSlotId_Type()
)
cfprApFabricPathEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpSlotId.setStatus("current")
_CfprApFabricPathEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricPathEpSwitchId_Object = MibTableColumn
cfprApFabricPathEpSwitchId = _CfprApFabricPathEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 22),
    _CfprApFabricPathEpSwitchId_Type()
)
cfprApFabricPathEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpSwitchId.setStatus("current")
_CfprApFabricPathEpTransport_Type = CfprApNetworkTransport
_CfprApFabricPathEpTransport_Object = MibTableColumn
cfprApFabricPathEpTransport = _CfprApFabricPathEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 23),
    _CfprApFabricPathEpTransport_Type()
)
cfprApFabricPathEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpTransport.setStatus("current")
_CfprApFabricPathEpType_Type = CfprApNetworkConnectionType
_CfprApFabricPathEpType_Object = MibTableColumn
cfprApFabricPathEpType = _CfprApFabricPathEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 93, 1, 24),
    _CfprApFabricPathEpType_Type()
)
cfprApFabricPathEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPathEpType.setStatus("current")
_CfprApFabricPoolableVlanTable_Object = MibTable
cfprApFabricPoolableVlanTable = _CfprApFabricPoolableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 94)
)
if mibBuilder.loadTexts:
    cfprApFabricPoolableVlanTable.setStatus("current")
_CfprApFabricPoolableVlanEntry_Object = MibTableRow
cfprApFabricPoolableVlanEntry = _CfprApFabricPoolableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 94, 1)
)
cfprApFabricPoolableVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricPoolableVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricPoolableVlanEntry.setStatus("current")
_CfprApFabricPoolableVlanInstanceId_Type = CfprApManagedObjectId
_CfprApFabricPoolableVlanInstanceId_Object = MibTableColumn
cfprApFabricPoolableVlanInstanceId = _CfprApFabricPoolableVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 94, 1, 1),
    _CfprApFabricPoolableVlanInstanceId_Type()
)
cfprApFabricPoolableVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricPoolableVlanInstanceId.setStatus("current")
_CfprApFabricPoolableVlanDn_Type = CfprApManagedObjectDn
_CfprApFabricPoolableVlanDn_Object = MibTableColumn
cfprApFabricPoolableVlanDn = _CfprApFabricPoolableVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 94, 1, 2),
    _CfprApFabricPoolableVlanDn_Type()
)
cfprApFabricPoolableVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPoolableVlanDn.setStatus("current")
_CfprApFabricPoolableVlanRn_Type = SnmpAdminString
_CfprApFabricPoolableVlanRn_Object = MibTableColumn
cfprApFabricPoolableVlanRn = _CfprApFabricPoolableVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 94, 1, 3),
    _CfprApFabricPoolableVlanRn_Type()
)
cfprApFabricPoolableVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPoolableVlanRn.setStatus("current")
_CfprApFabricPoolableVlanId_Type = Unsigned64
_CfprApFabricPoolableVlanId_Object = MibTableColumn
cfprApFabricPoolableVlanId = _CfprApFabricPoolableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 94, 1, 4),
    _CfprApFabricPoolableVlanId_Type()
)
cfprApFabricPoolableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPoolableVlanId.setStatus("current")
_CfprApFabricPoolableVlanPoolDn_Type = SnmpAdminString
_CfprApFabricPoolableVlanPoolDn_Object = MibTableColumn
cfprApFabricPoolableVlanPoolDn = _CfprApFabricPoolableVlanPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 94, 1, 5),
    _CfprApFabricPoolableVlanPoolDn_Type()
)
cfprApFabricPoolableVlanPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPoolableVlanPoolDn.setStatus("current")
_CfprApFabricPooledVlanTable_Object = MibTable
cfprApFabricPooledVlanTable = _CfprApFabricPooledVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95)
)
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanTable.setStatus("current")
_CfprApFabricPooledVlanEntry_Object = MibTableRow
cfprApFabricPooledVlanEntry = _CfprApFabricPooledVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1)
)
cfprApFabricPooledVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricPooledVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanEntry.setStatus("current")
_CfprApFabricPooledVlanInstanceId_Type = CfprApManagedObjectId
_CfprApFabricPooledVlanInstanceId_Object = MibTableColumn
cfprApFabricPooledVlanInstanceId = _CfprApFabricPooledVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 1),
    _CfprApFabricPooledVlanInstanceId_Type()
)
cfprApFabricPooledVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanInstanceId.setStatus("current")
_CfprApFabricPooledVlanDn_Type = CfprApManagedObjectDn
_CfprApFabricPooledVlanDn_Object = MibTableColumn
cfprApFabricPooledVlanDn = _CfprApFabricPooledVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 2),
    _CfprApFabricPooledVlanDn_Type()
)
cfprApFabricPooledVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanDn.setStatus("current")
_CfprApFabricPooledVlanRn_Type = SnmpAdminString
_CfprApFabricPooledVlanRn_Object = MibTableColumn
cfprApFabricPooledVlanRn = _CfprApFabricPooledVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 3),
    _CfprApFabricPooledVlanRn_Type()
)
cfprApFabricPooledVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanRn.setStatus("current")
_CfprApFabricPooledVlanAssigned_Type = TruthValue
_CfprApFabricPooledVlanAssigned_Object = MibTableColumn
cfprApFabricPooledVlanAssigned = _CfprApFabricPooledVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 4),
    _CfprApFabricPooledVlanAssigned_Type()
)
cfprApFabricPooledVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanAssigned.setStatus("current")
_CfprApFabricPooledVlanAssignedToDn_Type = SnmpAdminString
_CfprApFabricPooledVlanAssignedToDn_Object = MibTableColumn
cfprApFabricPooledVlanAssignedToDn = _CfprApFabricPooledVlanAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 5),
    _CfprApFabricPooledVlanAssignedToDn_Type()
)
cfprApFabricPooledVlanAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanAssignedToDn.setStatus("current")
_CfprApFabricPooledVlanConfigIssues_Type = CfprApFabricPoolMemberConfigIssues
_CfprApFabricPooledVlanConfigIssues_Object = MibTableColumn
cfprApFabricPooledVlanConfigIssues = _CfprApFabricPooledVlanConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 6),
    _CfprApFabricPooledVlanConfigIssues_Type()
)
cfprApFabricPooledVlanConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanConfigIssues.setStatus("current")
_CfprApFabricPooledVlanName_Type = SnmpAdminString
_CfprApFabricPooledVlanName_Object = MibTableColumn
cfprApFabricPooledVlanName = _CfprApFabricPooledVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 7),
    _CfprApFabricPooledVlanName_Type()
)
cfprApFabricPooledVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanName.setStatus("current")
_CfprApFabricPooledVlanPeerDn_Type = SnmpAdminString
_CfprApFabricPooledVlanPeerDn_Object = MibTableColumn
cfprApFabricPooledVlanPeerDn = _CfprApFabricPooledVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 8),
    _CfprApFabricPooledVlanPeerDn_Type()
)
cfprApFabricPooledVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanPeerDn.setStatus("current")
_CfprApFabricPooledVlanPoolableDn_Type = SnmpAdminString
_CfprApFabricPooledVlanPoolableDn_Object = MibTableColumn
cfprApFabricPooledVlanPoolableDn = _CfprApFabricPooledVlanPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 9),
    _CfprApFabricPooledVlanPoolableDn_Type()
)
cfprApFabricPooledVlanPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanPoolableDn.setStatus("current")
_CfprApFabricPooledVlanPrevAssignedToDn_Type = SnmpAdminString
_CfprApFabricPooledVlanPrevAssignedToDn_Object = MibTableColumn
cfprApFabricPooledVlanPrevAssignedToDn = _CfprApFabricPooledVlanPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 95, 1, 10),
    _CfprApFabricPooledVlanPrevAssignedToDn_Type()
)
cfprApFabricPooledVlanPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricPooledVlanPrevAssignedToDn.setStatus("current")
_CfprApFabricSanCloudTable_Object = MibTable
cfprApFabricSanCloudTable = _CfprApFabricSanCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96)
)
if mibBuilder.loadTexts:
    cfprApFabricSanCloudTable.setStatus("current")
_CfprApFabricSanCloudEntry_Object = MibTableRow
cfprApFabricSanCloudEntry = _CfprApFabricSanCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1)
)
cfprApFabricSanCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSanCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSanCloudEntry.setStatus("current")
_CfprApFabricSanCloudInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSanCloudInstanceId_Object = MibTableColumn
cfprApFabricSanCloudInstanceId = _CfprApFabricSanCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 1),
    _CfprApFabricSanCloudInstanceId_Type()
)
cfprApFabricSanCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudInstanceId.setStatus("current")
_CfprApFabricSanCloudDn_Type = CfprApManagedObjectDn
_CfprApFabricSanCloudDn_Object = MibTableColumn
cfprApFabricSanCloudDn = _CfprApFabricSanCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 2),
    _CfprApFabricSanCloudDn_Type()
)
cfprApFabricSanCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudDn.setStatus("current")
_CfprApFabricSanCloudRn_Type = SnmpAdminString
_CfprApFabricSanCloudRn_Object = MibTableColumn
cfprApFabricSanCloudRn = _CfprApFabricSanCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 3),
    _CfprApFabricSanCloudRn_Type()
)
cfprApFabricSanCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudRn.setStatus("current")
_CfprApFabricSanCloudFsmDescr_Type = SnmpAdminString
_CfprApFabricSanCloudFsmDescr_Object = MibTableColumn
cfprApFabricSanCloudFsmDescr = _CfprApFabricSanCloudFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 4),
    _CfprApFabricSanCloudFsmDescr_Type()
)
cfprApFabricSanCloudFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmDescr.setStatus("current")
_CfprApFabricSanCloudFsmPrev_Type = SnmpAdminString
_CfprApFabricSanCloudFsmPrev_Object = MibTableColumn
cfprApFabricSanCloudFsmPrev = _CfprApFabricSanCloudFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 5),
    _CfprApFabricSanCloudFsmPrev_Type()
)
cfprApFabricSanCloudFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmPrev.setStatus("current")
_CfprApFabricSanCloudFsmProgr_Type = Gauge32
_CfprApFabricSanCloudFsmProgr_Object = MibTableColumn
cfprApFabricSanCloudFsmProgr = _CfprApFabricSanCloudFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 6),
    _CfprApFabricSanCloudFsmProgr_Type()
)
cfprApFabricSanCloudFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmProgr.setStatus("current")
_CfprApFabricSanCloudFsmRmtInvErrCode_Type = Gauge32
_CfprApFabricSanCloudFsmRmtInvErrCode_Object = MibTableColumn
cfprApFabricSanCloudFsmRmtInvErrCode = _CfprApFabricSanCloudFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 7),
    _CfprApFabricSanCloudFsmRmtInvErrCode_Type()
)
cfprApFabricSanCloudFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmRmtInvErrCode.setStatus("current")
_CfprApFabricSanCloudFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFabricSanCloudFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFabricSanCloudFsmRmtInvErrDescr = _CfprApFabricSanCloudFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 8),
    _CfprApFabricSanCloudFsmRmtInvErrDescr_Type()
)
cfprApFabricSanCloudFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmRmtInvErrDescr.setStatus("current")
_CfprApFabricSanCloudFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFabricSanCloudFsmRmtInvRslt_Object = MibTableColumn
cfprApFabricSanCloudFsmRmtInvRslt = _CfprApFabricSanCloudFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 9),
    _CfprApFabricSanCloudFsmRmtInvRslt_Type()
)
cfprApFabricSanCloudFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmRmtInvRslt.setStatus("current")
_CfprApFabricSanCloudFsmStageDescr_Type = SnmpAdminString
_CfprApFabricSanCloudFsmStageDescr_Object = MibTableColumn
cfprApFabricSanCloudFsmStageDescr = _CfprApFabricSanCloudFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 10),
    _CfprApFabricSanCloudFsmStageDescr_Type()
)
cfprApFabricSanCloudFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageDescr.setStatus("current")
_CfprApFabricSanCloudFsmStamp_Type = DateAndTime
_CfprApFabricSanCloudFsmStamp_Object = MibTableColumn
cfprApFabricSanCloudFsmStamp = _CfprApFabricSanCloudFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 11),
    _CfprApFabricSanCloudFsmStamp_Type()
)
cfprApFabricSanCloudFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStamp.setStatus("current")
_CfprApFabricSanCloudFsmStatus_Type = SnmpAdminString
_CfprApFabricSanCloudFsmStatus_Object = MibTableColumn
cfprApFabricSanCloudFsmStatus = _CfprApFabricSanCloudFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 12),
    _CfprApFabricSanCloudFsmStatus_Type()
)
cfprApFabricSanCloudFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStatus.setStatus("current")
_CfprApFabricSanCloudFsmTry_Type = Gauge32
_CfprApFabricSanCloudFsmTry_Object = MibTableColumn
cfprApFabricSanCloudFsmTry = _CfprApFabricSanCloudFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 13),
    _CfprApFabricSanCloudFsmTry_Type()
)
cfprApFabricSanCloudFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTry.setStatus("current")
_CfprApFabricSanCloudMode_Type = CfprApFabricSwitchingMode
_CfprApFabricSanCloudMode_Object = MibTableColumn
cfprApFabricSanCloudMode = _CfprApFabricSanCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 96, 1, 14),
    _CfprApFabricSanCloudMode_Type()
)
cfprApFabricSanCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudMode.setStatus("current")
_CfprApFabricSanCloudFsmTable_Object = MibTable
cfprApFabricSanCloudFsmTable = _CfprApFabricSanCloudFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97)
)
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTable.setStatus("current")
_CfprApFabricSanCloudFsmEntry_Object = MibTableRow
cfprApFabricSanCloudFsmEntry = _CfprApFabricSanCloudFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1)
)
cfprApFabricSanCloudFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSanCloudFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmEntry.setStatus("current")
_CfprApFabricSanCloudFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSanCloudFsmInstanceId_Object = MibTableColumn
cfprApFabricSanCloudFsmInstanceId = _CfprApFabricSanCloudFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 1),
    _CfprApFabricSanCloudFsmInstanceId_Type()
)
cfprApFabricSanCloudFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmInstanceId.setStatus("current")
_CfprApFabricSanCloudFsmDn_Type = CfprApManagedObjectDn
_CfprApFabricSanCloudFsmDn_Object = MibTableColumn
cfprApFabricSanCloudFsmDn = _CfprApFabricSanCloudFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 2),
    _CfprApFabricSanCloudFsmDn_Type()
)
cfprApFabricSanCloudFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmDn.setStatus("current")
_CfprApFabricSanCloudFsmRn_Type = SnmpAdminString
_CfprApFabricSanCloudFsmRn_Object = MibTableColumn
cfprApFabricSanCloudFsmRn = _CfprApFabricSanCloudFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 3),
    _CfprApFabricSanCloudFsmRn_Type()
)
cfprApFabricSanCloudFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmRn.setStatus("current")
_CfprApFabricSanCloudFsmCompletionTime_Type = DateAndTime
_CfprApFabricSanCloudFsmCompletionTime_Object = MibTableColumn
cfprApFabricSanCloudFsmCompletionTime = _CfprApFabricSanCloudFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 4),
    _CfprApFabricSanCloudFsmCompletionTime_Type()
)
cfprApFabricSanCloudFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmCompletionTime.setStatus("current")
_CfprApFabricSanCloudFsmCurrentFsm_Type = CfprApFabricSanCloudFsmCurrentFsm
_CfprApFabricSanCloudFsmCurrentFsm_Object = MibTableColumn
cfprApFabricSanCloudFsmCurrentFsm = _CfprApFabricSanCloudFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 5),
    _CfprApFabricSanCloudFsmCurrentFsm_Type()
)
cfprApFabricSanCloudFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmCurrentFsm.setStatus("current")
_CfprApFabricSanCloudFsmDescrData_Type = SnmpAdminString
_CfprApFabricSanCloudFsmDescrData_Object = MibTableColumn
cfprApFabricSanCloudFsmDescrData = _CfprApFabricSanCloudFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 6),
    _CfprApFabricSanCloudFsmDescrData_Type()
)
cfprApFabricSanCloudFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmDescrData.setStatus("current")
_CfprApFabricSanCloudFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFabricSanCloudFsmFsmStatus_Object = MibTableColumn
cfprApFabricSanCloudFsmFsmStatus = _CfprApFabricSanCloudFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 7),
    _CfprApFabricSanCloudFsmFsmStatus_Type()
)
cfprApFabricSanCloudFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmFsmStatus.setStatus("current")
_CfprApFabricSanCloudFsmProgress_Type = Gauge32
_CfprApFabricSanCloudFsmProgress_Object = MibTableColumn
cfprApFabricSanCloudFsmProgress = _CfprApFabricSanCloudFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 8),
    _CfprApFabricSanCloudFsmProgress_Type()
)
cfprApFabricSanCloudFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmProgress.setStatus("current")
_CfprApFabricSanCloudFsmRmtErrCode_Type = Gauge32
_CfprApFabricSanCloudFsmRmtErrCode_Object = MibTableColumn
cfprApFabricSanCloudFsmRmtErrCode = _CfprApFabricSanCloudFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 9),
    _CfprApFabricSanCloudFsmRmtErrCode_Type()
)
cfprApFabricSanCloudFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmRmtErrCode.setStatus("current")
_CfprApFabricSanCloudFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFabricSanCloudFsmRmtErrDescr_Object = MibTableColumn
cfprApFabricSanCloudFsmRmtErrDescr = _CfprApFabricSanCloudFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 10),
    _CfprApFabricSanCloudFsmRmtErrDescr_Type()
)
cfprApFabricSanCloudFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmRmtErrDescr.setStatus("current")
_CfprApFabricSanCloudFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFabricSanCloudFsmRmtRslt_Object = MibTableColumn
cfprApFabricSanCloudFsmRmtRslt = _CfprApFabricSanCloudFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 97, 1, 11),
    _CfprApFabricSanCloudFsmRmtRslt_Type()
)
cfprApFabricSanCloudFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmRmtRslt.setStatus("current")
_CfprApFabricSanCloudFsmStageTable_Object = MibTable
cfprApFabricSanCloudFsmStageTable = _CfprApFabricSanCloudFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98)
)
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageTable.setStatus("current")
_CfprApFabricSanCloudFsmStageEntry_Object = MibTableRow
cfprApFabricSanCloudFsmStageEntry = _CfprApFabricSanCloudFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1)
)
cfprApFabricSanCloudFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSanCloudFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageEntry.setStatus("current")
_CfprApFabricSanCloudFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSanCloudFsmStageInstanceId_Object = MibTableColumn
cfprApFabricSanCloudFsmStageInstanceId = _CfprApFabricSanCloudFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 1),
    _CfprApFabricSanCloudFsmStageInstanceId_Type()
)
cfprApFabricSanCloudFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageInstanceId.setStatus("current")
_CfprApFabricSanCloudFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFabricSanCloudFsmStageDn_Object = MibTableColumn
cfprApFabricSanCloudFsmStageDn = _CfprApFabricSanCloudFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 2),
    _CfprApFabricSanCloudFsmStageDn_Type()
)
cfprApFabricSanCloudFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageDn.setStatus("current")
_CfprApFabricSanCloudFsmStageRn_Type = SnmpAdminString
_CfprApFabricSanCloudFsmStageRn_Object = MibTableColumn
cfprApFabricSanCloudFsmStageRn = _CfprApFabricSanCloudFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 3),
    _CfprApFabricSanCloudFsmStageRn_Type()
)
cfprApFabricSanCloudFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageRn.setStatus("current")
_CfprApFabricSanCloudFsmStageDescrData_Type = SnmpAdminString
_CfprApFabricSanCloudFsmStageDescrData_Object = MibTableColumn
cfprApFabricSanCloudFsmStageDescrData = _CfprApFabricSanCloudFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 4),
    _CfprApFabricSanCloudFsmStageDescrData_Type()
)
cfprApFabricSanCloudFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageDescrData.setStatus("current")
_CfprApFabricSanCloudFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFabricSanCloudFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFabricSanCloudFsmStageLastUpdateTime = _CfprApFabricSanCloudFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 5),
    _CfprApFabricSanCloudFsmStageLastUpdateTime_Type()
)
cfprApFabricSanCloudFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageLastUpdateTime.setStatus("current")
_CfprApFabricSanCloudFsmStageName_Type = CfprApFabricSanCloudFsmStageName
_CfprApFabricSanCloudFsmStageName_Object = MibTableColumn
cfprApFabricSanCloudFsmStageName = _CfprApFabricSanCloudFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 6),
    _CfprApFabricSanCloudFsmStageName_Type()
)
cfprApFabricSanCloudFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageName.setStatus("current")
_CfprApFabricSanCloudFsmStageOrder_Type = Gauge32
_CfprApFabricSanCloudFsmStageOrder_Object = MibTableColumn
cfprApFabricSanCloudFsmStageOrder = _CfprApFabricSanCloudFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 7),
    _CfprApFabricSanCloudFsmStageOrder_Type()
)
cfprApFabricSanCloudFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageOrder.setStatus("current")
_CfprApFabricSanCloudFsmStageRetry_Type = Gauge32
_CfprApFabricSanCloudFsmStageRetry_Object = MibTableColumn
cfprApFabricSanCloudFsmStageRetry = _CfprApFabricSanCloudFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 8),
    _CfprApFabricSanCloudFsmStageRetry_Type()
)
cfprApFabricSanCloudFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageRetry.setStatus("current")
_CfprApFabricSanCloudFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFabricSanCloudFsmStageStageStatus_Object = MibTableColumn
cfprApFabricSanCloudFsmStageStageStatus = _CfprApFabricSanCloudFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 98, 1, 9),
    _CfprApFabricSanCloudFsmStageStageStatus_Type()
)
cfprApFabricSanCloudFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmStageStageStatus.setStatus("current")
_CfprApFabricSanCloudFsmTaskTable_Object = MibTable
cfprApFabricSanCloudFsmTaskTable = _CfprApFabricSanCloudFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99)
)
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskTable.setStatus("current")
_CfprApFabricSanCloudFsmTaskEntry_Object = MibTableRow
cfprApFabricSanCloudFsmTaskEntry = _CfprApFabricSanCloudFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99, 1)
)
cfprApFabricSanCloudFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSanCloudFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskEntry.setStatus("current")
_CfprApFabricSanCloudFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSanCloudFsmTaskInstanceId_Object = MibTableColumn
cfprApFabricSanCloudFsmTaskInstanceId = _CfprApFabricSanCloudFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99, 1, 1),
    _CfprApFabricSanCloudFsmTaskInstanceId_Type()
)
cfprApFabricSanCloudFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskInstanceId.setStatus("current")
_CfprApFabricSanCloudFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFabricSanCloudFsmTaskDn_Object = MibTableColumn
cfprApFabricSanCloudFsmTaskDn = _CfprApFabricSanCloudFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99, 1, 2),
    _CfprApFabricSanCloudFsmTaskDn_Type()
)
cfprApFabricSanCloudFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskDn.setStatus("current")
_CfprApFabricSanCloudFsmTaskRn_Type = SnmpAdminString
_CfprApFabricSanCloudFsmTaskRn_Object = MibTableColumn
cfprApFabricSanCloudFsmTaskRn = _CfprApFabricSanCloudFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99, 1, 3),
    _CfprApFabricSanCloudFsmTaskRn_Type()
)
cfprApFabricSanCloudFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskRn.setStatus("current")
_CfprApFabricSanCloudFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFabricSanCloudFsmTaskCompletion_Object = MibTableColumn
cfprApFabricSanCloudFsmTaskCompletion = _CfprApFabricSanCloudFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99, 1, 4),
    _CfprApFabricSanCloudFsmTaskCompletion_Type()
)
cfprApFabricSanCloudFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskCompletion.setStatus("current")
_CfprApFabricSanCloudFsmTaskFlags_Type = CfprApFsmFlags
_CfprApFabricSanCloudFsmTaskFlags_Object = MibTableColumn
cfprApFabricSanCloudFsmTaskFlags = _CfprApFabricSanCloudFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99, 1, 5),
    _CfprApFabricSanCloudFsmTaskFlags_Type()
)
cfprApFabricSanCloudFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskFlags.setStatus("current")
_CfprApFabricSanCloudFsmTaskItem_Type = CfprApFabricSanCloudFsmTaskItem
_CfprApFabricSanCloudFsmTaskItem_Object = MibTableColumn
cfprApFabricSanCloudFsmTaskItem = _CfprApFabricSanCloudFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99, 1, 6),
    _CfprApFabricSanCloudFsmTaskItem_Type()
)
cfprApFabricSanCloudFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskItem.setStatus("current")
_CfprApFabricSanCloudFsmTaskSeqId_Type = Gauge32
_CfprApFabricSanCloudFsmTaskSeqId_Object = MibTableColumn
cfprApFabricSanCloudFsmTaskSeqId = _CfprApFabricSanCloudFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 99, 1, 7),
    _CfprApFabricSanCloudFsmTaskSeqId_Type()
)
cfprApFabricSanCloudFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanCloudFsmTaskSeqId.setStatus("current")
_CfprApFabricSanPinGroupTable_Object = MibTable
cfprApFabricSanPinGroupTable = _CfprApFabricSanPinGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101)
)
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupTable.setStatus("current")
_CfprApFabricSanPinGroupEntry_Object = MibTableRow
cfprApFabricSanPinGroupEntry = _CfprApFabricSanPinGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1)
)
cfprApFabricSanPinGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSanPinGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupEntry.setStatus("current")
_CfprApFabricSanPinGroupInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSanPinGroupInstanceId_Object = MibTableColumn
cfprApFabricSanPinGroupInstanceId = _CfprApFabricSanPinGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 1),
    _CfprApFabricSanPinGroupInstanceId_Type()
)
cfprApFabricSanPinGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupInstanceId.setStatus("current")
_CfprApFabricSanPinGroupDn_Type = CfprApManagedObjectDn
_CfprApFabricSanPinGroupDn_Object = MibTableColumn
cfprApFabricSanPinGroupDn = _CfprApFabricSanPinGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 2),
    _CfprApFabricSanPinGroupDn_Type()
)
cfprApFabricSanPinGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupDn.setStatus("current")
_CfprApFabricSanPinGroupRn_Type = SnmpAdminString
_CfprApFabricSanPinGroupRn_Object = MibTableColumn
cfprApFabricSanPinGroupRn = _CfprApFabricSanPinGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 3),
    _CfprApFabricSanPinGroupRn_Type()
)
cfprApFabricSanPinGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupRn.setStatus("current")
_CfprApFabricSanPinGroupDescr_Type = SnmpAdminString
_CfprApFabricSanPinGroupDescr_Object = MibTableColumn
cfprApFabricSanPinGroupDescr = _CfprApFabricSanPinGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 4),
    _CfprApFabricSanPinGroupDescr_Type()
)
cfprApFabricSanPinGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupDescr.setStatus("current")
_CfprApFabricSanPinGroupIntId_Type = SnmpAdminString
_CfprApFabricSanPinGroupIntId_Object = MibTableColumn
cfprApFabricSanPinGroupIntId = _CfprApFabricSanPinGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 5),
    _CfprApFabricSanPinGroupIntId_Type()
)
cfprApFabricSanPinGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupIntId.setStatus("current")
_CfprApFabricSanPinGroupName_Type = SnmpAdminString
_CfprApFabricSanPinGroupName_Object = MibTableColumn
cfprApFabricSanPinGroupName = _CfprApFabricSanPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 6),
    _CfprApFabricSanPinGroupName_Type()
)
cfprApFabricSanPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupName.setStatus("current")
_CfprApFabricSanPinGroupPolicyLevel_Type = Gauge32
_CfprApFabricSanPinGroupPolicyLevel_Object = MibTableColumn
cfprApFabricSanPinGroupPolicyLevel = _CfprApFabricSanPinGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 7),
    _CfprApFabricSanPinGroupPolicyLevel_Type()
)
cfprApFabricSanPinGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupPolicyLevel.setStatus("current")
_CfprApFabricSanPinGroupPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricSanPinGroupPolicyOwner_Object = MibTableColumn
cfprApFabricSanPinGroupPolicyOwner = _CfprApFabricSanPinGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 8),
    _CfprApFabricSanPinGroupPolicyOwner_Type()
)
cfprApFabricSanPinGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupPolicyOwner.setStatus("current")
_CfprApFabricSanPinGroupSize_Type = Gauge32
_CfprApFabricSanPinGroupSize_Object = MibTableColumn
cfprApFabricSanPinGroupSize = _CfprApFabricSanPinGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 101, 1, 9),
    _CfprApFabricSanPinGroupSize_Type()
)
cfprApFabricSanPinGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinGroupSize.setStatus("current")
_CfprApFabricSanPinTargetTable_Object = MibTable
cfprApFabricSanPinTargetTable = _CfprApFabricSanPinTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 102)
)
if mibBuilder.loadTexts:
    cfprApFabricSanPinTargetTable.setStatus("current")
_CfprApFabricSanPinTargetEntry_Object = MibTableRow
cfprApFabricSanPinTargetEntry = _CfprApFabricSanPinTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 102, 1)
)
cfprApFabricSanPinTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSanPinTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSanPinTargetEntry.setStatus("current")
_CfprApFabricSanPinTargetInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSanPinTargetInstanceId_Object = MibTableColumn
cfprApFabricSanPinTargetInstanceId = _CfprApFabricSanPinTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 102, 1, 1),
    _CfprApFabricSanPinTargetInstanceId_Type()
)
cfprApFabricSanPinTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSanPinTargetInstanceId.setStatus("current")
_CfprApFabricSanPinTargetDn_Type = CfprApManagedObjectDn
_CfprApFabricSanPinTargetDn_Object = MibTableColumn
cfprApFabricSanPinTargetDn = _CfprApFabricSanPinTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 102, 1, 2),
    _CfprApFabricSanPinTargetDn_Type()
)
cfprApFabricSanPinTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinTargetDn.setStatus("current")
_CfprApFabricSanPinTargetRn_Type = SnmpAdminString
_CfprApFabricSanPinTargetRn_Object = MibTableColumn
cfprApFabricSanPinTargetRn = _CfprApFabricSanPinTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 102, 1, 3),
    _CfprApFabricSanPinTargetRn_Type()
)
cfprApFabricSanPinTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinTargetRn.setStatus("current")
_CfprApFabricSanPinTargetEpDn_Type = SnmpAdminString
_CfprApFabricSanPinTargetEpDn_Object = MibTableColumn
cfprApFabricSanPinTargetEpDn = _CfprApFabricSanPinTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 102, 1, 4),
    _CfprApFabricSanPinTargetEpDn_Type()
)
cfprApFabricSanPinTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinTargetEpDn.setStatus("current")
_CfprApFabricSanPinTargetFabricId_Type = SnmpAdminString
_CfprApFabricSanPinTargetFabricId_Object = MibTableColumn
cfprApFabricSanPinTargetFabricId = _CfprApFabricSanPinTargetFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 102, 1, 5),
    _CfprApFabricSanPinTargetFabricId_Type()
)
cfprApFabricSanPinTargetFabricId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinTargetFabricId.setStatus("current")
_CfprApFabricSanPinTargetTargetStatus_Type = CfprApFabricTargetStatus
_CfprApFabricSanPinTargetTargetStatus_Object = MibTableColumn
cfprApFabricSanPinTargetTargetStatus = _CfprApFabricSanPinTargetTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 102, 1, 6),
    _CfprApFabricSanPinTargetTargetStatus_Type()
)
cfprApFabricSanPinTargetTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSanPinTargetTargetStatus.setStatus("current")
_CfprApFabricSspEthMonTable_Object = MibTable
cfprApFabricSspEthMonTable = _CfprApFabricSspEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103)
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonTable.setStatus("current")
_CfprApFabricSspEthMonEntry_Object = MibTableRow
cfprApFabricSspEthMonEntry = _CfprApFabricSspEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1)
)
cfprApFabricSspEthMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSspEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonEntry.setStatus("current")
_CfprApFabricSspEthMonInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSspEthMonInstanceId_Object = MibTableColumn
cfprApFabricSspEthMonInstanceId = _CfprApFabricSspEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 1),
    _CfprApFabricSspEthMonInstanceId_Type()
)
cfprApFabricSspEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonInstanceId.setStatus("current")
_CfprApFabricSspEthMonDn_Type = CfprApManagedObjectDn
_CfprApFabricSspEthMonDn_Object = MibTableColumn
cfprApFabricSspEthMonDn = _CfprApFabricSspEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 2),
    _CfprApFabricSspEthMonDn_Type()
)
cfprApFabricSspEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonDn.setStatus("current")
_CfprApFabricSspEthMonRn_Type = SnmpAdminString
_CfprApFabricSspEthMonRn_Object = MibTableColumn
cfprApFabricSspEthMonRn = _CfprApFabricSspEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 3),
    _CfprApFabricSspEthMonRn_Type()
)
cfprApFabricSspEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonRn.setStatus("current")
_CfprApFabricSspEthMonAdminState_Type = CfprApFabricSspMonAdminState
_CfprApFabricSspEthMonAdminState_Object = MibTableColumn
cfprApFabricSspEthMonAdminState = _CfprApFabricSspEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 4),
    _CfprApFabricSspEthMonAdminState_Type()
)
cfprApFabricSspEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonAdminState.setStatus("current")
_CfprApFabricSspEthMonAppendFlag_Type = CfprApFabricSspEthMonAppendFlag
_CfprApFabricSspEthMonAppendFlag_Object = MibTableColumn
cfprApFabricSspEthMonAppendFlag = _CfprApFabricSspEthMonAppendFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 5),
    _CfprApFabricSspEthMonAppendFlag_Type()
)
cfprApFabricSspEthMonAppendFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonAppendFlag.setStatus("current")
_CfprApFabricSspEthMonConfigFailReason_Type = SnmpAdminString
_CfprApFabricSspEthMonConfigFailReason_Object = MibTableColumn
cfprApFabricSspEthMonConfigFailReason = _CfprApFabricSspEthMonConfigFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 6),
    _CfprApFabricSspEthMonConfigFailReason_Type()
)
cfprApFabricSspEthMonConfigFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonConfigFailReason.setStatus("current")
_CfprApFabricSspEthMonDelPcap_Type = CfprApFabricSspMonDelPcap
_CfprApFabricSspEthMonDelPcap_Object = MibTableColumn
cfprApFabricSspEthMonDelPcap = _CfprApFabricSspEthMonDelPcap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 7),
    _CfprApFabricSspEthMonDelPcap_Type()
)
cfprApFabricSspEthMonDelPcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonDelPcap.setStatus("current")
_CfprApFabricSspEthMonDropCount_Type = Unsigned64
_CfprApFabricSspEthMonDropCount_Object = MibTableColumn
cfprApFabricSspEthMonDropCount = _CfprApFabricSspEthMonDropCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 8),
    _CfprApFabricSspEthMonDropCount_Type()
)
cfprApFabricSspEthMonDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonDropCount.setStatus("current")
_CfprApFabricSspEthMonErrorCode_Type = SnmpAdminString
_CfprApFabricSspEthMonErrorCode_Object = MibTableColumn
cfprApFabricSspEthMonErrorCode = _CfprApFabricSspEthMonErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 9),
    _CfprApFabricSspEthMonErrorCode_Type()
)
cfprApFabricSspEthMonErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonErrorCode.setStatus("current")
_CfprApFabricSspEthMonId_Type = CfprApNetworkSwitchId
_CfprApFabricSspEthMonId_Object = MibTableColumn
cfprApFabricSspEthMonId = _CfprApFabricSspEthMonId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 10),
    _CfprApFabricSspEthMonId_Type()
)
cfprApFabricSspEthMonId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonId.setStatus("current")
_CfprApFabricSspEthMonIsConfigSuccess_Type = TruthValue
_CfprApFabricSspEthMonIsConfigSuccess_Object = MibTableColumn
cfprApFabricSspEthMonIsConfigSuccess = _CfprApFabricSspEthMonIsConfigSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 11),
    _CfprApFabricSspEthMonIsConfigSuccess_Type()
)
cfprApFabricSspEthMonIsConfigSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonIsConfigSuccess.setStatus("current")
_CfprApFabricSspEthMonIsConfiguredByAG_Type = TruthValue
_CfprApFabricSspEthMonIsConfiguredByAG_Object = MibTableColumn
cfprApFabricSspEthMonIsConfiguredByAG = _CfprApFabricSspEthMonIsConfiguredByAG_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 12),
    _CfprApFabricSspEthMonIsConfiguredByAG_Type()
)
cfprApFabricSspEthMonIsConfiguredByAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonIsConfiguredByAG.setStatus("current")
_CfprApFabricSspEthMonName_Type = SnmpAdminString
_CfprApFabricSspEthMonName_Object = MibTableColumn
cfprApFabricSspEthMonName = _CfprApFabricSspEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 13),
    _CfprApFabricSspEthMonName_Type()
)
cfprApFabricSspEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonName.setStatus("current")
_CfprApFabricSspEthMonOperState_Type = CfprApFabricSspMonOperState
_CfprApFabricSspEthMonOperState_Object = MibTableColumn
cfprApFabricSspEthMonOperState = _CfprApFabricSspEthMonOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 14),
    _CfprApFabricSspEthMonOperState_Type()
)
cfprApFabricSspEthMonOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonOperState.setStatus("current")
_CfprApFabricSspEthMonOperStateReason_Type = CfprApFabricSspMonOperStateReason
_CfprApFabricSspEthMonOperStateReason_Object = MibTableColumn
cfprApFabricSspEthMonOperStateReason = _CfprApFabricSspEthMonOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 15),
    _CfprApFabricSspEthMonOperStateReason_Type()
)
cfprApFabricSspEthMonOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonOperStateReason.setStatus("current")
_CfprApFabricSspEthMonPeerDn_Type = SnmpAdminString
_CfprApFabricSspEthMonPeerDn_Object = MibTableColumn
cfprApFabricSspEthMonPeerDn = _CfprApFabricSspEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 16),
    _CfprApFabricSspEthMonPeerDn_Type()
)
cfprApFabricSspEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonPeerDn.setStatus("current")
_CfprApFabricSspEthMonReBoot_Type = SnmpAdminString
_CfprApFabricSspEthMonReBoot_Object = MibTableColumn
cfprApFabricSspEthMonReBoot = _CfprApFabricSspEthMonReBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 17),
    _CfprApFabricSspEthMonReBoot_Type()
)
cfprApFabricSspEthMonReBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonReBoot.setStatus("current")
_CfprApFabricSspEthMonSession_Type = Gauge32
_CfprApFabricSspEthMonSession_Object = MibTableColumn
cfprApFabricSspEthMonSession = _CfprApFabricSspEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 18),
    _CfprApFabricSspEthMonSession_Type()
)
cfprApFabricSspEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSession.setStatus("current")
_CfprApFabricSspEthMonSessionMemUsage_Type = Gauge32
_CfprApFabricSspEthMonSessionMemUsage_Object = MibTableColumn
cfprApFabricSspEthMonSessionMemUsage = _CfprApFabricSspEthMonSessionMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 19),
    _CfprApFabricSspEthMonSessionMemUsage_Type()
)
cfprApFabricSspEthMonSessionMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSessionMemUsage.setStatus("current")
_CfprApFabricSspEthMonSourceConfigured_Type = Gauge32
_CfprApFabricSspEthMonSourceConfigured_Object = MibTableColumn
cfprApFabricSspEthMonSourceConfigured = _CfprApFabricSspEthMonSourceConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 103, 1, 20),
    _CfprApFabricSspEthMonSourceConfigured_Type()
)
cfprApFabricSspEthMonSourceConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSourceConfigured.setStatus("current")
_CfprApFabricSspEthMonFilterEpTable_Object = MibTable
cfprApFabricSspEthMonFilterEpTable = _CfprApFabricSspEthMonFilterEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104)
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpTable.setStatus("current")
_CfprApFabricSspEthMonFilterEpEntry_Object = MibTableRow
cfprApFabricSspEthMonFilterEpEntry = _CfprApFabricSspEthMonFilterEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1)
)
cfprApFabricSspEthMonFilterEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSspEthMonFilterEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpEntry.setStatus("current")
_CfprApFabricSspEthMonFilterEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSspEthMonFilterEpInstanceId_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpInstanceId = _CfprApFabricSspEthMonFilterEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 1),
    _CfprApFabricSspEthMonFilterEpInstanceId_Type()
)
cfprApFabricSspEthMonFilterEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpInstanceId.setStatus("current")
_CfprApFabricSspEthMonFilterEpDn_Type = CfprApManagedObjectDn
_CfprApFabricSspEthMonFilterEpDn_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpDn = _CfprApFabricSspEthMonFilterEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 2),
    _CfprApFabricSspEthMonFilterEpDn_Type()
)
cfprApFabricSspEthMonFilterEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpDn.setStatus("current")
_CfprApFabricSspEthMonFilterEpRn_Type = SnmpAdminString
_CfprApFabricSspEthMonFilterEpRn_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpRn = _CfprApFabricSspEthMonFilterEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 3),
    _CfprApFabricSspEthMonFilterEpRn_Type()
)
cfprApFabricSspEthMonFilterEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpRn.setStatus("current")
_CfprApFabricSspEthMonFilterEpDestIp_Type = InetAddressIPv4
_CfprApFabricSspEthMonFilterEpDestIp_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpDestIp = _CfprApFabricSspEthMonFilterEpDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 4),
    _CfprApFabricSspEthMonFilterEpDestIp_Type()
)
cfprApFabricSspEthMonFilterEpDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpDestIp.setStatus("current")
_CfprApFabricSspEthMonFilterEpDestMAC_Type = MacAddress
_CfprApFabricSspEthMonFilterEpDestMAC_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpDestMAC = _CfprApFabricSspEthMonFilterEpDestMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 5),
    _CfprApFabricSspEthMonFilterEpDestMAC_Type()
)
cfprApFabricSspEthMonFilterEpDestMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpDestMAC.setStatus("current")
_CfprApFabricSspEthMonFilterEpDestPort_Type = Gauge32
_CfprApFabricSspEthMonFilterEpDestPort_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpDestPort = _CfprApFabricSspEthMonFilterEpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 6),
    _CfprApFabricSspEthMonFilterEpDestPort_Type()
)
cfprApFabricSspEthMonFilterEpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpDestPort.setStatus("current")
_CfprApFabricSspEthMonFilterEpEthertype_Type = Gauge32
_CfprApFabricSspEthMonFilterEpEthertype_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpEthertype = _CfprApFabricSspEthMonFilterEpEthertype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 7),
    _CfprApFabricSspEthMonFilterEpEthertype_Type()
)
cfprApFabricSspEthMonFilterEpEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpEthertype.setStatus("current")
_CfprApFabricSspEthMonFilterEpIvlan_Type = Gauge32
_CfprApFabricSspEthMonFilterEpIvlan_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpIvlan = _CfprApFabricSspEthMonFilterEpIvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 8),
    _CfprApFabricSspEthMonFilterEpIvlan_Type()
)
cfprApFabricSspEthMonFilterEpIvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpIvlan.setStatus("current")
_CfprApFabricSspEthMonFilterEpNameId_Type = SnmpAdminString
_CfprApFabricSspEthMonFilterEpNameId_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpNameId = _CfprApFabricSspEthMonFilterEpNameId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 9),
    _CfprApFabricSspEthMonFilterEpNameId_Type()
)
cfprApFabricSspEthMonFilterEpNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpNameId.setStatus("current")
_CfprApFabricSspEthMonFilterEpOvlan_Type = Gauge32
_CfprApFabricSspEthMonFilterEpOvlan_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpOvlan = _CfprApFabricSspEthMonFilterEpOvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 10),
    _CfprApFabricSspEthMonFilterEpOvlan_Type()
)
cfprApFabricSspEthMonFilterEpOvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpOvlan.setStatus("current")
_CfprApFabricSspEthMonFilterEpProtocol_Type = Gauge32
_CfprApFabricSspEthMonFilterEpProtocol_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpProtocol = _CfprApFabricSspEthMonFilterEpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 11),
    _CfprApFabricSspEthMonFilterEpProtocol_Type()
)
cfprApFabricSspEthMonFilterEpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpProtocol.setStatus("current")
_CfprApFabricSspEthMonFilterEpSrcIp_Type = InetAddressIPv4
_CfprApFabricSspEthMonFilterEpSrcIp_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpSrcIp = _CfprApFabricSspEthMonFilterEpSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 12),
    _CfprApFabricSspEthMonFilterEpSrcIp_Type()
)
cfprApFabricSspEthMonFilterEpSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpSrcIp.setStatus("current")
_CfprApFabricSspEthMonFilterEpSrcMAC_Type = MacAddress
_CfprApFabricSspEthMonFilterEpSrcMAC_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpSrcMAC = _CfprApFabricSspEthMonFilterEpSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 13),
    _CfprApFabricSspEthMonFilterEpSrcMAC_Type()
)
cfprApFabricSspEthMonFilterEpSrcMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpSrcMAC.setStatus("current")
_CfprApFabricSspEthMonFilterEpSrcPort_Type = Gauge32
_CfprApFabricSspEthMonFilterEpSrcPort_Object = MibTableColumn
cfprApFabricSspEthMonFilterEpSrcPort = _CfprApFabricSspEthMonFilterEpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 104, 1, 14),
    _CfprApFabricSspEthMonFilterEpSrcPort_Type()
)
cfprApFabricSspEthMonFilterEpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonFilterEpSrcPort.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpTable_Object = MibTable
cfprApFabricSspEthMonSrcAppEpTable = _CfprApFabricSspEthMonSrcAppEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105)
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpTable.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpEntry_Object = MibTableRow
cfprApFabricSspEthMonSrcAppEpEntry = _CfprApFabricSspEthMonSrcAppEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1)
)
cfprApFabricSspEthMonSrcAppEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSspEthMonSrcAppEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpEntry.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSspEthMonSrcAppEpInstanceId_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpInstanceId = _CfprApFabricSspEthMonSrcAppEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 1),
    _CfprApFabricSspEthMonSrcAppEpInstanceId_Type()
)
cfprApFabricSspEthMonSrcAppEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpInstanceId.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpDn_Type = CfprApManagedObjectDn
_CfprApFabricSspEthMonSrcAppEpDn_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpDn = _CfprApFabricSspEthMonSrcAppEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 2),
    _CfprApFabricSspEthMonSrcAppEpDn_Type()
)
cfprApFabricSspEthMonSrcAppEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpDn.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpRn_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppEpRn_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpRn = _CfprApFabricSspEthMonSrcAppEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 3),
    _CfprApFabricSspEthMonSrcAppEpRn_Type()
)
cfprApFabricSspEthMonSrcAppEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpRn.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpAppName_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppEpAppName_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpAppName = _CfprApFabricSspEthMonSrcAppEpAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 4),
    _CfprApFabricSspEthMonSrcAppEpAppName_Type()
)
cfprApFabricSspEthMonSrcAppEpAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpAppName.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpFilter_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppEpFilter_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpFilter = _CfprApFabricSspEthMonSrcAppEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 5),
    _CfprApFabricSspEthMonSrcAppEpFilter_Type()
)
cfprApFabricSspEthMonSrcAppEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpFilter.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpLinkName_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppEpLinkName_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpLinkName = _CfprApFabricSspEthMonSrcAppEpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 6),
    _CfprApFabricSspEthMonSrcAppEpLinkName_Type()
)
cfprApFabricSspEthMonSrcAppEpLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpLinkName.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpPcapfile_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppEpPcapfile_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpPcapfile = _CfprApFabricSspEthMonSrcAppEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 7),
    _CfprApFabricSspEthMonSrcAppEpPcapfile_Type()
)
cfprApFabricSspEthMonSrcAppEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpPcapfile.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpPcapfilename_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppEpPcapfilename_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpPcapfilename = _CfprApFabricSspEthMonSrcAppEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 8),
    _CfprApFabricSspEthMonSrcAppEpPcapfilename_Type()
)
cfprApFabricSspEthMonSrcAppEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpPcapfilename.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpPcapsize_Type = Gauge32
_CfprApFabricSspEthMonSrcAppEpPcapsize_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpPcapsize = _CfprApFabricSspEthMonSrcAppEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 9),
    _CfprApFabricSspEthMonSrcAppEpPcapsize_Type()
)
cfprApFabricSspEthMonSrcAppEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpPcapsize.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpPortName_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppEpPortName_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpPortName = _CfprApFabricSspEthMonSrcAppEpPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 10),
    _CfprApFabricSspEthMonSrcAppEpPortName_Type()
)
cfprApFabricSspEthMonSrcAppEpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpPortName.setStatus("current")
_CfprApFabricSspEthMonSrcAppEpSlotId_Type = CfprApFabricPktCaptureAppSlotId
_CfprApFabricSspEthMonSrcAppEpSlotId_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppEpSlotId = _CfprApFabricSspEthMonSrcAppEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 105, 1, 11),
    _CfprApFabricSspEthMonSrcAppEpSlotId_Type()
)
cfprApFabricSspEthMonSrcAppEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppEpSlotId.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpTable_Object = MibTable
cfprApFabricSspEthMonSrcAppLinksEpTable = _CfprApFabricSspEthMonSrcAppLinksEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106)
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpTable.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpEntry_Object = MibTableRow
cfprApFabricSspEthMonSrcAppLinksEpEntry = _CfprApFabricSspEthMonSrcAppLinksEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1)
)
cfprApFabricSspEthMonSrcAppLinksEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSspEthMonSrcAppLinksEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpEntry.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSspEthMonSrcAppLinksEpInstanceId_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpInstanceId = _CfprApFabricSspEthMonSrcAppLinksEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 1),
    _CfprApFabricSspEthMonSrcAppLinksEpInstanceId_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpInstanceId.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpDn_Type = CfprApManagedObjectDn
_CfprApFabricSspEthMonSrcAppLinksEpDn_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpDn = _CfprApFabricSspEthMonSrcAppLinksEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 2),
    _CfprApFabricSspEthMonSrcAppLinksEpDn_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpDn.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpRn_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppLinksEpRn_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpRn = _CfprApFabricSspEthMonSrcAppLinksEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 3),
    _CfprApFabricSspEthMonSrcAppLinksEpRn_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpRn.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpChassisId_Type = Gauge32
_CfprApFabricSspEthMonSrcAppLinksEpChassisId_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpChassisId = _CfprApFabricSspEthMonSrcAppLinksEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 4),
    _CfprApFabricSspEthMonSrcAppLinksEpChassisId_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpChassisId.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId_Type = Gauge32
_CfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId = _CfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 5),
    _CfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpEqPortId_Type = Gauge32
_CfprApFabricSspEthMonSrcAppLinksEpEqPortId_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpEqPortId = _CfprApFabricSspEthMonSrcAppLinksEpEqPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 6),
    _CfprApFabricSspEthMonSrcAppLinksEpEqPortId_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpEqPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpEqPortId.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpEqSlotId_Type = Gauge32
_CfprApFabricSspEthMonSrcAppLinksEpEqSlotId_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpEqSlotId = _CfprApFabricSspEthMonSrcAppLinksEpEqSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 7),
    _CfprApFabricSspEthMonSrcAppLinksEpEqSlotId_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpEqSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpEqSlotId.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpFilter_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppLinksEpFilter_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpFilter = _CfprApFabricSspEthMonSrcAppLinksEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 8),
    _CfprApFabricSspEthMonSrcAppLinksEpFilter_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpFilter.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpFilterDn_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppLinksEpFilterDn_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpFilterDn = _CfprApFabricSspEthMonSrcAppLinksEpFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 9),
    _CfprApFabricSspEthMonSrcAppLinksEpFilterDn_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpFilterDn.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpLifeCycle_Type = CfprApSwPktCaptureLifeCycle
_CfprApFabricSspEthMonSrcAppLinksEpLifeCycle_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpLifeCycle = _CfprApFabricSspEthMonSrcAppLinksEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 10),
    _CfprApFabricSspEthMonSrcAppLinksEpLifeCycle_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpLifeCycle.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpName_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppLinksEpName_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpName = _CfprApFabricSspEthMonSrcAppLinksEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 11),
    _CfprApFabricSspEthMonSrcAppLinksEpName_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpName.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpPcapfile_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppLinksEpPcapfile_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpPcapfile = _CfprApFabricSspEthMonSrcAppLinksEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 12),
    _CfprApFabricSspEthMonSrcAppLinksEpPcapfile_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpPcapfile.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpPcapfilename_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcAppLinksEpPcapfilename_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpPcapfilename = _CfprApFabricSspEthMonSrcAppLinksEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 13),
    _CfprApFabricSspEthMonSrcAppLinksEpPcapfilename_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpPcapfilename.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpPcapsize_Type = Gauge32
_CfprApFabricSspEthMonSrcAppLinksEpPcapsize_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpPcapsize = _CfprApFabricSspEthMonSrcAppLinksEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 14),
    _CfprApFabricSspEthMonSrcAppLinksEpPcapsize_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpPcapsize.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricSspEthMonSrcAppLinksEpSwitchId_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpSwitchId = _CfprApFabricSspEthMonSrcAppLinksEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 15),
    _CfprApFabricSspEthMonSrcAppLinksEpSwitchId_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpSwitchId.setStatus("current")
_CfprApFabricSspEthMonSrcAppLinksEpVlan_Type = Gauge32
_CfprApFabricSspEthMonSrcAppLinksEpVlan_Object = MibTableColumn
cfprApFabricSspEthMonSrcAppLinksEpVlan = _CfprApFabricSspEthMonSrcAppLinksEpVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 106, 1, 16),
    _CfprApFabricSspEthMonSrcAppLinksEpVlan_Type()
)
cfprApFabricSspEthMonSrcAppLinksEpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcAppLinksEpVlan.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpTable_Object = MibTable
cfprApFabricSspEthMonSrcPhyAggrEpTable = _CfprApFabricSspEthMonSrcPhyAggrEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107)
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpTable.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpEntry_Object = MibTableRow
cfprApFabricSspEthMonSrcPhyAggrEpEntry = _CfprApFabricSspEthMonSrcPhyAggrEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1)
)
cfprApFabricSspEthMonSrcPhyAggrEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSspEthMonSrcPhyAggrEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpEntry.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSspEthMonSrcPhyAggrEpInstanceId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpInstanceId = _CfprApFabricSspEthMonSrcPhyAggrEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 1),
    _CfprApFabricSspEthMonSrcPhyAggrEpInstanceId_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpInstanceId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpDn_Type = CfprApManagedObjectDn
_CfprApFabricSspEthMonSrcPhyAggrEpDn_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpDn = _CfprApFabricSspEthMonSrcPhyAggrEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 2),
    _CfprApFabricSspEthMonSrcPhyAggrEpDn_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpDn.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpRn_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcPhyAggrEpRn_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpRn = _CfprApFabricSspEthMonSrcPhyAggrEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 3),
    _CfprApFabricSspEthMonSrcPhyAggrEpRn_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpRn.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpAggrPortId_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyAggrEpAggrPortId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpAggrPortId = _CfprApFabricSspEthMonSrcPhyAggrEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 4),
    _CfprApFabricSspEthMonSrcPhyAggrEpAggrPortId_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpAggrPortId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId = _CfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 5),
    _CfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpChassisId_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyAggrEpChassisId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpChassisId = _CfprApFabricSspEthMonSrcPhyAggrEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 6),
    _CfprApFabricSspEthMonSrcPhyAggrEpChassisId_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpChassisId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpFilter_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcPhyAggrEpFilter_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpFilter = _CfprApFabricSspEthMonSrcPhyAggrEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 7),
    _CfprApFabricSspEthMonSrcPhyAggrEpFilter_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpFilter.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpPcapfile_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcPhyAggrEpPcapfile_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpPcapfile = _CfprApFabricSspEthMonSrcPhyAggrEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 8),
    _CfprApFabricSspEthMonSrcPhyAggrEpPcapfile_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpPcapfile.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpPcapfilename_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcPhyAggrEpPcapfilename_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpPcapfilename = _CfprApFabricSspEthMonSrcPhyAggrEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 9),
    _CfprApFabricSspEthMonSrcPhyAggrEpPcapfilename_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpPcapfilename.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpPcapsize_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyAggrEpPcapsize_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpPcapsize = _CfprApFabricSspEthMonSrcPhyAggrEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 10),
    _CfprApFabricSspEthMonSrcPhyAggrEpPcapsize_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpPcapsize.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpSlotId_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyAggrEpSlotId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpSlotId = _CfprApFabricSspEthMonSrcPhyAggrEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 11),
    _CfprApFabricSspEthMonSrcPhyAggrEpSlotId_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpSlotId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyAggrEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricSspEthMonSrcPhyAggrEpSwitchId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyAggrEpSwitchId = _CfprApFabricSspEthMonSrcPhyAggrEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 107, 1, 12),
    _CfprApFabricSspEthMonSrcPhyAggrEpSwitchId_Type()
)
cfprApFabricSspEthMonSrcPhyAggrEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyAggrEpSwitchId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpTable_Object = MibTable
cfprApFabricSspEthMonSrcPhyEpTable = _CfprApFabricSspEthMonSrcPhyEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108)
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpTable.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpEntry_Object = MibTableRow
cfprApFabricSspEthMonSrcPhyEpEntry = _CfprApFabricSspEthMonSrcPhyEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1)
)
cfprApFabricSspEthMonSrcPhyEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSspEthMonSrcPhyEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpEntry.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSspEthMonSrcPhyEpInstanceId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpInstanceId = _CfprApFabricSspEthMonSrcPhyEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 1),
    _CfprApFabricSspEthMonSrcPhyEpInstanceId_Type()
)
cfprApFabricSspEthMonSrcPhyEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpInstanceId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpDn_Type = CfprApManagedObjectDn
_CfprApFabricSspEthMonSrcPhyEpDn_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpDn = _CfprApFabricSspEthMonSrcPhyEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 2),
    _CfprApFabricSspEthMonSrcPhyEpDn_Type()
)
cfprApFabricSspEthMonSrcPhyEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpDn.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpRn_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcPhyEpRn_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpRn = _CfprApFabricSspEthMonSrcPhyEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 3),
    _CfprApFabricSspEthMonSrcPhyEpRn_Type()
)
cfprApFabricSspEthMonSrcPhyEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpRn.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpChassisId_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyEpChassisId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpChassisId = _CfprApFabricSspEthMonSrcPhyEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 4),
    _CfprApFabricSspEthMonSrcPhyEpChassisId_Type()
)
cfprApFabricSspEthMonSrcPhyEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpChassisId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpFilter_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcPhyEpFilter_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpFilter = _CfprApFabricSspEthMonSrcPhyEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 5),
    _CfprApFabricSspEthMonSrcPhyEpFilter_Type()
)
cfprApFabricSspEthMonSrcPhyEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpFilter.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpPcapfile_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcPhyEpPcapfile_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpPcapfile = _CfprApFabricSspEthMonSrcPhyEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 6),
    _CfprApFabricSspEthMonSrcPhyEpPcapfile_Type()
)
cfprApFabricSspEthMonSrcPhyEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpPcapfile.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpPcapfilename_Type = SnmpAdminString
_CfprApFabricSspEthMonSrcPhyEpPcapfilename_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpPcapfilename = _CfprApFabricSspEthMonSrcPhyEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 7),
    _CfprApFabricSspEthMonSrcPhyEpPcapfilename_Type()
)
cfprApFabricSspEthMonSrcPhyEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpPcapfilename.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpPcapsize_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyEpPcapsize_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpPcapsize = _CfprApFabricSspEthMonSrcPhyEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 8),
    _CfprApFabricSspEthMonSrcPhyEpPcapsize_Type()
)
cfprApFabricSspEthMonSrcPhyEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpPcapsize.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpPortId_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyEpPortId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpPortId = _CfprApFabricSspEthMonSrcPhyEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 9),
    _CfprApFabricSspEthMonSrcPhyEpPortId_Type()
)
cfprApFabricSspEthMonSrcPhyEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpPortId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpSlotId_Type = Gauge32
_CfprApFabricSspEthMonSrcPhyEpSlotId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpSlotId = _CfprApFabricSspEthMonSrcPhyEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 10),
    _CfprApFabricSspEthMonSrcPhyEpSlotId_Type()
)
cfprApFabricSspEthMonSrcPhyEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpSlotId.setStatus("current")
_CfprApFabricSspEthMonSrcPhyEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricSspEthMonSrcPhyEpSwitchId_Object = MibTableColumn
cfprApFabricSspEthMonSrcPhyEpSwitchId = _CfprApFabricSspEthMonSrcPhyEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 108, 1, 11),
    _CfprApFabricSspEthMonSrcPhyEpSwitchId_Type()
)
cfprApFabricSspEthMonSrcPhyEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspEthMonSrcPhyEpSwitchId.setStatus("current")
_CfprApFabricSspLanMonCloudTable_Object = MibTable
cfprApFabricSspLanMonCloudTable = _CfprApFabricSspLanMonCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 109)
)
if mibBuilder.loadTexts:
    cfprApFabricSspLanMonCloudTable.setStatus("current")
_CfprApFabricSspLanMonCloudEntry_Object = MibTableRow
cfprApFabricSspLanMonCloudEntry = _CfprApFabricSspLanMonCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 109, 1)
)
cfprApFabricSspLanMonCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSspLanMonCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSspLanMonCloudEntry.setStatus("current")
_CfprApFabricSspLanMonCloudInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSspLanMonCloudInstanceId_Object = MibTableColumn
cfprApFabricSspLanMonCloudInstanceId = _CfprApFabricSspLanMonCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 109, 1, 1),
    _CfprApFabricSspLanMonCloudInstanceId_Type()
)
cfprApFabricSspLanMonCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSspLanMonCloudInstanceId.setStatus("current")
_CfprApFabricSspLanMonCloudDn_Type = CfprApManagedObjectDn
_CfprApFabricSspLanMonCloudDn_Object = MibTableColumn
cfprApFabricSspLanMonCloudDn = _CfprApFabricSspLanMonCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 109, 1, 2),
    _CfprApFabricSspLanMonCloudDn_Type()
)
cfprApFabricSspLanMonCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspLanMonCloudDn.setStatus("current")
_CfprApFabricSspLanMonCloudRn_Type = SnmpAdminString
_CfprApFabricSspLanMonCloudRn_Object = MibTableColumn
cfprApFabricSspLanMonCloudRn = _CfprApFabricSspLanMonCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 109, 1, 3),
    _CfprApFabricSspLanMonCloudRn_Type()
)
cfprApFabricSspLanMonCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspLanMonCloudRn.setStatus("current")
_CfprApFabricSspLanMonCloudMode_Type = CfprApFabricSwitchingMode
_CfprApFabricSspLanMonCloudMode_Object = MibTableColumn
cfprApFabricSspLanMonCloudMode = _CfprApFabricSspLanMonCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 109, 1, 4),
    _CfprApFabricSspLanMonCloudMode_Type()
)
cfprApFabricSspLanMonCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSspLanMonCloudMode.setStatus("current")
_CfprApFabricSubGroupTable_Object = MibTable
cfprApFabricSubGroupTable = _CfprApFabricSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110)
)
if mibBuilder.loadTexts:
    cfprApFabricSubGroupTable.setStatus("current")
_CfprApFabricSubGroupEntry_Object = MibTableRow
cfprApFabricSubGroupEntry = _CfprApFabricSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1)
)
cfprApFabricSubGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSubGroupEntry.setStatus("current")
_CfprApFabricSubGroupInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSubGroupInstanceId_Object = MibTableColumn
cfprApFabricSubGroupInstanceId = _CfprApFabricSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 1),
    _CfprApFabricSubGroupInstanceId_Type()
)
cfprApFabricSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupInstanceId.setStatus("current")
_CfprApFabricSubGroupDn_Type = CfprApManagedObjectDn
_CfprApFabricSubGroupDn_Object = MibTableColumn
cfprApFabricSubGroupDn = _CfprApFabricSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 2),
    _CfprApFabricSubGroupDn_Type()
)
cfprApFabricSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupDn.setStatus("current")
_CfprApFabricSubGroupRn_Type = SnmpAdminString
_CfprApFabricSubGroupRn_Object = MibTableColumn
cfprApFabricSubGroupRn = _CfprApFabricSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 3),
    _CfprApFabricSubGroupRn_Type()
)
cfprApFabricSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupRn.setStatus("current")
_CfprApFabricSubGroupAggrPortId_Type = CfprApFabricSubGroupAggrPortId
_CfprApFabricSubGroupAggrPortId_Object = MibTableColumn
cfprApFabricSubGroupAggrPortId = _CfprApFabricSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 4),
    _CfprApFabricSubGroupAggrPortId_Type()
)
cfprApFabricSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupAggrPortId.setStatus("current")
_CfprApFabricSubGroupConfigState_Type = CfprApFabricSubGroupConfigState
_CfprApFabricSubGroupConfigState_Object = MibTableColumn
cfprApFabricSubGroupConfigState = _CfprApFabricSubGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 5),
    _CfprApFabricSubGroupConfigState_Type()
)
cfprApFabricSubGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupConfigState.setStatus("current")
_CfprApFabricSubGroupLicGP_Type = Unsigned64
_CfprApFabricSubGroupLicGP_Object = MibTableColumn
cfprApFabricSubGroupLicGP = _CfprApFabricSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 6),
    _CfprApFabricSubGroupLicGP_Type()
)
cfprApFabricSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupLicGP.setStatus("current")
_CfprApFabricSubGroupLicState_Type = CfprApLicenseState
_CfprApFabricSubGroupLicState_Object = MibTableColumn
cfprApFabricSubGroupLicState = _CfprApFabricSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 7),
    _CfprApFabricSubGroupLicState_Type()
)
cfprApFabricSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupLicState.setStatus("current")
_CfprApFabricSubGroupLocale_Type = CfprApNetworkLocale
_CfprApFabricSubGroupLocale_Object = MibTableColumn
cfprApFabricSubGroupLocale = _CfprApFabricSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 8),
    _CfprApFabricSubGroupLocale_Type()
)
cfprApFabricSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupLocale.setStatus("current")
_CfprApFabricSubGroupName_Type = SnmpAdminString
_CfprApFabricSubGroupName_Object = MibTableColumn
cfprApFabricSubGroupName = _CfprApFabricSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 9),
    _CfprApFabricSubGroupName_Type()
)
cfprApFabricSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupName.setStatus("current")
_CfprApFabricSubGroupSlotId_Type = CfprApFabricSubGroupSlotId
_CfprApFabricSubGroupSlotId_Object = MibTableColumn
cfprApFabricSubGroupSlotId = _CfprApFabricSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 10),
    _CfprApFabricSubGroupSlotId_Type()
)
cfprApFabricSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupSlotId.setStatus("current")
_CfprApFabricSubGroupSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricSubGroupSwitchId_Object = MibTableColumn
cfprApFabricSubGroupSwitchId = _CfprApFabricSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 11),
    _CfprApFabricSubGroupSwitchId_Type()
)
cfprApFabricSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupSwitchId.setStatus("current")
_CfprApFabricSubGroupTransport_Type = CfprApNetworkTransport
_CfprApFabricSubGroupTransport_Object = MibTableColumn
cfprApFabricSubGroupTransport = _CfprApFabricSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 12),
    _CfprApFabricSubGroupTransport_Type()
)
cfprApFabricSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupTransport.setStatus("current")
_CfprApFabricSubGroupType_Type = CfprApNetworkConnectionType
_CfprApFabricSubGroupType_Object = MibTableColumn
cfprApFabricSubGroupType = _CfprApFabricSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 110, 1, 13),
    _CfprApFabricSubGroupType_Type()
)
cfprApFabricSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSubGroupType.setStatus("current")
_CfprApFabricSwChPhEpTable_Object = MibTable
cfprApFabricSwChPhEpTable = _CfprApFabricSwChPhEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111)
)
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpTable.setStatus("current")
_CfprApFabricSwChPhEpEntry_Object = MibTableRow
cfprApFabricSwChPhEpEntry = _CfprApFabricSwChPhEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1)
)
cfprApFabricSwChPhEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSwChPhEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpEntry.setStatus("current")
_CfprApFabricSwChPhEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSwChPhEpInstanceId_Object = MibTableColumn
cfprApFabricSwChPhEpInstanceId = _CfprApFabricSwChPhEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 1),
    _CfprApFabricSwChPhEpInstanceId_Type()
)
cfprApFabricSwChPhEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpInstanceId.setStatus("current")
_CfprApFabricSwChPhEpDn_Type = CfprApManagedObjectDn
_CfprApFabricSwChPhEpDn_Object = MibTableColumn
cfprApFabricSwChPhEpDn = _CfprApFabricSwChPhEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 2),
    _CfprApFabricSwChPhEpDn_Type()
)
cfprApFabricSwChPhEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpDn.setStatus("current")
_CfprApFabricSwChPhEpRn_Type = SnmpAdminString
_CfprApFabricSwChPhEpRn_Object = MibTableColumn
cfprApFabricSwChPhEpRn = _CfprApFabricSwChPhEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 3),
    _CfprApFabricSwChPhEpRn_Type()
)
cfprApFabricSwChPhEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpRn.setStatus("current")
_CfprApFabricSwChPhEpAdminState_Type = CfprApFabricSwChPhEpAdminState
_CfprApFabricSwChPhEpAdminState_Object = MibTableColumn
cfprApFabricSwChPhEpAdminState = _CfprApFabricSwChPhEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 4),
    _CfprApFabricSwChPhEpAdminState_Type()
)
cfprApFabricSwChPhEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpAdminState.setStatus("current")
_CfprApFabricSwChPhEpAggrPortId_Type = Gauge32
_CfprApFabricSwChPhEpAggrPortId_Object = MibTableColumn
cfprApFabricSwChPhEpAggrPortId = _CfprApFabricSwChPhEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 5),
    _CfprApFabricSwChPhEpAggrPortId_Type()
)
cfprApFabricSwChPhEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpAggrPortId.setStatus("current")
_CfprApFabricSwChPhEpChassisId_Type = Gauge32
_CfprApFabricSwChPhEpChassisId_Object = MibTableColumn
cfprApFabricSwChPhEpChassisId = _CfprApFabricSwChPhEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 6),
    _CfprApFabricSwChPhEpChassisId_Type()
)
cfprApFabricSwChPhEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpChassisId.setStatus("current")
_CfprApFabricSwChPhEpEpDn_Type = SnmpAdminString
_CfprApFabricSwChPhEpEpDn_Object = MibTableColumn
cfprApFabricSwChPhEpEpDn = _CfprApFabricSwChPhEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 7),
    _CfprApFabricSwChPhEpEpDn_Type()
)
cfprApFabricSwChPhEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpEpDn.setStatus("current")
_CfprApFabricSwChPhEpEqType_Type = CfprApEquipmentFabricEpType
_CfprApFabricSwChPhEpEqType_Object = MibTableColumn
cfprApFabricSwChPhEpEqType = _CfprApFabricSwChPhEpEqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 8),
    _CfprApFabricSwChPhEpEqType_Type()
)
cfprApFabricSwChPhEpEqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpEqType.setStatus("current")
_CfprApFabricSwChPhEpFltAggr_Type = Unsigned64
_CfprApFabricSwChPhEpFltAggr_Object = MibTableColumn
cfprApFabricSwChPhEpFltAggr = _CfprApFabricSwChPhEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 9),
    _CfprApFabricSwChPhEpFltAggr_Type()
)
cfprApFabricSwChPhEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpFltAggr.setStatus("current")
_CfprApFabricSwChPhEpIfRole_Type = CfprApFabricSwChEpIfRole
_CfprApFabricSwChPhEpIfRole_Object = MibTableColumn
cfprApFabricSwChPhEpIfRole = _CfprApFabricSwChPhEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 10),
    _CfprApFabricSwChPhEpIfRole_Type()
)
cfprApFabricSwChPhEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpIfRole.setStatus("current")
_CfprApFabricSwChPhEpIfType_Type = CfprApFabricPIoEpIfType
_CfprApFabricSwChPhEpIfType_Object = MibTableColumn
cfprApFabricSwChPhEpIfType = _CfprApFabricSwChPhEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 11),
    _CfprApFabricSwChPhEpIfType_Type()
)
cfprApFabricSwChPhEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpIfType.setStatus("current")
_CfprApFabricSwChPhEpLc_Type = CfprApFabricLifeCycle
_CfprApFabricSwChPhEpLc_Object = MibTableColumn
cfprApFabricSwChPhEpLc = _CfprApFabricSwChPhEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 12),
    _CfprApFabricSwChPhEpLc_Type()
)
cfprApFabricSwChPhEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpLc.setStatus("current")
_CfprApFabricSwChPhEpLicGP_Type = Unsigned64
_CfprApFabricSwChPhEpLicGP_Object = MibTableColumn
cfprApFabricSwChPhEpLicGP = _CfprApFabricSwChPhEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 13),
    _CfprApFabricSwChPhEpLicGP_Type()
)
cfprApFabricSwChPhEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpLicGP.setStatus("current")
_CfprApFabricSwChPhEpLicState_Type = CfprApLicenseState
_CfprApFabricSwChPhEpLicState_Object = MibTableColumn
cfprApFabricSwChPhEpLicState = _CfprApFabricSwChPhEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 14),
    _CfprApFabricSwChPhEpLicState_Type()
)
cfprApFabricSwChPhEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpLicState.setStatus("current")
_CfprApFabricSwChPhEpLocale_Type = CfprApFabricInternalEpLocale
_CfprApFabricSwChPhEpLocale_Object = MibTableColumn
cfprApFabricSwChPhEpLocale = _CfprApFabricSwChPhEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 15),
    _CfprApFabricSwChPhEpLocale_Type()
)
cfprApFabricSwChPhEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpLocale.setStatus("current")
_CfprApFabricSwChPhEpModel_Type = SnmpAdminString
_CfprApFabricSwChPhEpModel_Object = MibTableColumn
cfprApFabricSwChPhEpModel = _CfprApFabricSwChPhEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 16),
    _CfprApFabricSwChPhEpModel_Type()
)
cfprApFabricSwChPhEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpModel.setStatus("current")
_CfprApFabricSwChPhEpName_Type = SnmpAdminString
_CfprApFabricSwChPhEpName_Object = MibTableColumn
cfprApFabricSwChPhEpName = _CfprApFabricSwChPhEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 17),
    _CfprApFabricSwChPhEpName_Type()
)
cfprApFabricSwChPhEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpName.setStatus("current")
_CfprApFabricSwChPhEpOperState_Type = CfprApFabricPIoEpOperState
_CfprApFabricSwChPhEpOperState_Object = MibTableColumn
cfprApFabricSwChPhEpOperState = _CfprApFabricSwChPhEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 18),
    _CfprApFabricSwChPhEpOperState_Type()
)
cfprApFabricSwChPhEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpOperState.setStatus("current")
_CfprApFabricSwChPhEpOperStateReason_Type = SnmpAdminString
_CfprApFabricSwChPhEpOperStateReason_Object = MibTableColumn
cfprApFabricSwChPhEpOperStateReason = _CfprApFabricSwChPhEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 19),
    _CfprApFabricSwChPhEpOperStateReason_Type()
)
cfprApFabricSwChPhEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpOperStateReason.setStatus("current")
_CfprApFabricSwChPhEpPeerAggrPortId_Type = Gauge32
_CfprApFabricSwChPhEpPeerAggrPortId_Object = MibTableColumn
cfprApFabricSwChPhEpPeerAggrPortId = _CfprApFabricSwChPhEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 20),
    _CfprApFabricSwChPhEpPeerAggrPortId_Type()
)
cfprApFabricSwChPhEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpPeerAggrPortId.setStatus("current")
_CfprApFabricSwChPhEpPeerChassisId_Type = Gauge32
_CfprApFabricSwChPhEpPeerChassisId_Object = MibTableColumn
cfprApFabricSwChPhEpPeerChassisId = _CfprApFabricSwChPhEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 21),
    _CfprApFabricSwChPhEpPeerChassisId_Type()
)
cfprApFabricSwChPhEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpPeerChassisId.setStatus("current")
_CfprApFabricSwChPhEpPeerDn_Type = SnmpAdminString
_CfprApFabricSwChPhEpPeerDn_Object = MibTableColumn
cfprApFabricSwChPhEpPeerDn = _CfprApFabricSwChPhEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 22),
    _CfprApFabricSwChPhEpPeerDn_Type()
)
cfprApFabricSwChPhEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpPeerDn.setStatus("current")
_CfprApFabricSwChPhEpPeerPortId_Type = Gauge32
_CfprApFabricSwChPhEpPeerPortId_Object = MibTableColumn
cfprApFabricSwChPhEpPeerPortId = _CfprApFabricSwChPhEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 23),
    _CfprApFabricSwChPhEpPeerPortId_Type()
)
cfprApFabricSwChPhEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpPeerPortId.setStatus("current")
_CfprApFabricSwChPhEpPeerSlotId_Type = Gauge32
_CfprApFabricSwChPhEpPeerSlotId_Object = MibTableColumn
cfprApFabricSwChPhEpPeerSlotId = _CfprApFabricSwChPhEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 24),
    _CfprApFabricSwChPhEpPeerSlotId_Type()
)
cfprApFabricSwChPhEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpPeerSlotId.setStatus("current")
_CfprApFabricSwChPhEpPortId_Type = CfprApFabricPIoEpPortId
_CfprApFabricSwChPhEpPortId_Object = MibTableColumn
cfprApFabricSwChPhEpPortId = _CfprApFabricSwChPhEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 25),
    _CfprApFabricSwChPhEpPortId_Type()
)
cfprApFabricSwChPhEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpPortId.setStatus("current")
_CfprApFabricSwChPhEpRevision_Type = SnmpAdminString
_CfprApFabricSwChPhEpRevision_Object = MibTableColumn
cfprApFabricSwChPhEpRevision = _CfprApFabricSwChPhEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 26),
    _CfprApFabricSwChPhEpRevision_Type()
)
cfprApFabricSwChPhEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpRevision.setStatus("current")
_CfprApFabricSwChPhEpSerial_Type = SnmpAdminString
_CfprApFabricSwChPhEpSerial_Object = MibTableColumn
cfprApFabricSwChPhEpSerial = _CfprApFabricSwChPhEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 27),
    _CfprApFabricSwChPhEpSerial_Type()
)
cfprApFabricSwChPhEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpSerial.setStatus("current")
_CfprApFabricSwChPhEpSlotId_Type = CfprApFabricPIoEpSlotId
_CfprApFabricSwChPhEpSlotId_Object = MibTableColumn
cfprApFabricSwChPhEpSlotId = _CfprApFabricSwChPhEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 28),
    _CfprApFabricSwChPhEpSlotId_Type()
)
cfprApFabricSwChPhEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpSlotId.setStatus("current")
_CfprApFabricSwChPhEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricSwChPhEpSwitchId_Object = MibTableColumn
cfprApFabricSwChPhEpSwitchId = _CfprApFabricSwChPhEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 29),
    _CfprApFabricSwChPhEpSwitchId_Type()
)
cfprApFabricSwChPhEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpSwitchId.setStatus("current")
_CfprApFabricSwChPhEpTransport_Type = CfprApNetworkTransport
_CfprApFabricSwChPhEpTransport_Object = MibTableColumn
cfprApFabricSwChPhEpTransport = _CfprApFabricSwChPhEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 30),
    _CfprApFabricSwChPhEpTransport_Type()
)
cfprApFabricSwChPhEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpTransport.setStatus("current")
_CfprApFabricSwChPhEpType_Type = CfprApFabricSwChEpType
_CfprApFabricSwChPhEpType_Object = MibTableColumn
cfprApFabricSwChPhEpType = _CfprApFabricSwChPhEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 31),
    _CfprApFabricSwChPhEpType_Type()
)
cfprApFabricSwChPhEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpType.setStatus("current")
_CfprApFabricSwChPhEpVendor_Type = SnmpAdminString
_CfprApFabricSwChPhEpVendor_Object = MibTableColumn
cfprApFabricSwChPhEpVendor = _CfprApFabricSwChPhEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 111, 1, 32),
    _CfprApFabricSwChPhEpVendor_Type()
)
cfprApFabricSwChPhEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwChPhEpVendor.setStatus("current")
_CfprApFabricSwSubGroupTable_Object = MibTable
cfprApFabricSwSubGroupTable = _CfprApFabricSwSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112)
)
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupTable.setStatus("current")
_CfprApFabricSwSubGroupEntry_Object = MibTableRow
cfprApFabricSwSubGroupEntry = _CfprApFabricSwSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1)
)
cfprApFabricSwSubGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricSwSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupEntry.setStatus("current")
_CfprApFabricSwSubGroupInstanceId_Type = CfprApManagedObjectId
_CfprApFabricSwSubGroupInstanceId_Object = MibTableColumn
cfprApFabricSwSubGroupInstanceId = _CfprApFabricSwSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 1),
    _CfprApFabricSwSubGroupInstanceId_Type()
)
cfprApFabricSwSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupInstanceId.setStatus("current")
_CfprApFabricSwSubGroupDn_Type = CfprApManagedObjectDn
_CfprApFabricSwSubGroupDn_Object = MibTableColumn
cfprApFabricSwSubGroupDn = _CfprApFabricSwSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 2),
    _CfprApFabricSwSubGroupDn_Type()
)
cfprApFabricSwSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupDn.setStatus("current")
_CfprApFabricSwSubGroupRn_Type = SnmpAdminString
_CfprApFabricSwSubGroupRn_Object = MibTableColumn
cfprApFabricSwSubGroupRn = _CfprApFabricSwSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 3),
    _CfprApFabricSwSubGroupRn_Type()
)
cfprApFabricSwSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupRn.setStatus("current")
_CfprApFabricSwSubGroupAggrPortId_Type = CfprApFabricSwSubGroupAggrPortId
_CfprApFabricSwSubGroupAggrPortId_Object = MibTableColumn
cfprApFabricSwSubGroupAggrPortId = _CfprApFabricSwSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 4),
    _CfprApFabricSwSubGroupAggrPortId_Type()
)
cfprApFabricSwSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupAggrPortId.setStatus("current")
_CfprApFabricSwSubGroupConfigState_Type = CfprApFabricSwSubGroupConfigState
_CfprApFabricSwSubGroupConfigState_Object = MibTableColumn
cfprApFabricSwSubGroupConfigState = _CfprApFabricSwSubGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 5),
    _CfprApFabricSwSubGroupConfigState_Type()
)
cfprApFabricSwSubGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupConfigState.setStatus("current")
_CfprApFabricSwSubGroupLicGP_Type = Unsigned64
_CfprApFabricSwSubGroupLicGP_Object = MibTableColumn
cfprApFabricSwSubGroupLicGP = _CfprApFabricSwSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 6),
    _CfprApFabricSwSubGroupLicGP_Type()
)
cfprApFabricSwSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupLicGP.setStatus("current")
_CfprApFabricSwSubGroupLicState_Type = CfprApLicenseState
_CfprApFabricSwSubGroupLicState_Object = MibTableColumn
cfprApFabricSwSubGroupLicState = _CfprApFabricSwSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 7),
    _CfprApFabricSwSubGroupLicState_Type()
)
cfprApFabricSwSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupLicState.setStatus("current")
_CfprApFabricSwSubGroupLocale_Type = CfprApNetworkLocale
_CfprApFabricSwSubGroupLocale_Object = MibTableColumn
cfprApFabricSwSubGroupLocale = _CfprApFabricSwSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 8),
    _CfprApFabricSwSubGroupLocale_Type()
)
cfprApFabricSwSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupLocale.setStatus("current")
_CfprApFabricSwSubGroupName_Type = SnmpAdminString
_CfprApFabricSwSubGroupName_Object = MibTableColumn
cfprApFabricSwSubGroupName = _CfprApFabricSwSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 9),
    _CfprApFabricSwSubGroupName_Type()
)
cfprApFabricSwSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupName.setStatus("current")
_CfprApFabricSwSubGroupSlotId_Type = CfprApFabricSwSubGroupSlotId
_CfprApFabricSwSubGroupSlotId_Object = MibTableColumn
cfprApFabricSwSubGroupSlotId = _CfprApFabricSwSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 10),
    _CfprApFabricSwSubGroupSlotId_Type()
)
cfprApFabricSwSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupSlotId.setStatus("current")
_CfprApFabricSwSubGroupSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricSwSubGroupSwitchId_Object = MibTableColumn
cfprApFabricSwSubGroupSwitchId = _CfprApFabricSwSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 11),
    _CfprApFabricSwSubGroupSwitchId_Type()
)
cfprApFabricSwSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupSwitchId.setStatus("current")
_CfprApFabricSwSubGroupTransport_Type = CfprApNetworkTransport
_CfprApFabricSwSubGroupTransport_Object = MibTableColumn
cfprApFabricSwSubGroupTransport = _CfprApFabricSwSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 12),
    _CfprApFabricSwSubGroupTransport_Type()
)
cfprApFabricSwSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupTransport.setStatus("current")
_CfprApFabricSwSubGroupType_Type = CfprApNetworkConnectionType
_CfprApFabricSwSubGroupType_Object = MibTableColumn
cfprApFabricSwSubGroupType = _CfprApFabricSwSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 112, 1, 13),
    _CfprApFabricSwSubGroupType_Type()
)
cfprApFabricSwSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricSwSubGroupType.setStatus("current")
_CfprApFabricUdldLinkPolicyTable_Object = MibTable
cfprApFabricUdldLinkPolicyTable = _CfprApFabricUdldLinkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113)
)
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyTable.setStatus("current")
_CfprApFabricUdldLinkPolicyEntry_Object = MibTableRow
cfprApFabricUdldLinkPolicyEntry = _CfprApFabricUdldLinkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1)
)
cfprApFabricUdldLinkPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricUdldLinkPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyEntry.setStatus("current")
_CfprApFabricUdldLinkPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFabricUdldLinkPolicyInstanceId_Object = MibTableColumn
cfprApFabricUdldLinkPolicyInstanceId = _CfprApFabricUdldLinkPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 1),
    _CfprApFabricUdldLinkPolicyInstanceId_Type()
)
cfprApFabricUdldLinkPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyInstanceId.setStatus("current")
_CfprApFabricUdldLinkPolicyDn_Type = CfprApManagedObjectDn
_CfprApFabricUdldLinkPolicyDn_Object = MibTableColumn
cfprApFabricUdldLinkPolicyDn = _CfprApFabricUdldLinkPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 2),
    _CfprApFabricUdldLinkPolicyDn_Type()
)
cfprApFabricUdldLinkPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyDn.setStatus("current")
_CfprApFabricUdldLinkPolicyRn_Type = SnmpAdminString
_CfprApFabricUdldLinkPolicyRn_Object = MibTableColumn
cfprApFabricUdldLinkPolicyRn = _CfprApFabricUdldLinkPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 3),
    _CfprApFabricUdldLinkPolicyRn_Type()
)
cfprApFabricUdldLinkPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyRn.setStatus("current")
_CfprApFabricUdldLinkPolicyAdminState_Type = CfprApFabricUdldLinkPolicyAdminState
_CfprApFabricUdldLinkPolicyAdminState_Object = MibTableColumn
cfprApFabricUdldLinkPolicyAdminState = _CfprApFabricUdldLinkPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 4),
    _CfprApFabricUdldLinkPolicyAdminState_Type()
)
cfprApFabricUdldLinkPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyAdminState.setStatus("current")
_CfprApFabricUdldLinkPolicyDescr_Type = SnmpAdminString
_CfprApFabricUdldLinkPolicyDescr_Object = MibTableColumn
cfprApFabricUdldLinkPolicyDescr = _CfprApFabricUdldLinkPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 5),
    _CfprApFabricUdldLinkPolicyDescr_Type()
)
cfprApFabricUdldLinkPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyDescr.setStatus("current")
_CfprApFabricUdldLinkPolicyIntId_Type = SnmpAdminString
_CfprApFabricUdldLinkPolicyIntId_Object = MibTableColumn
cfprApFabricUdldLinkPolicyIntId = _CfprApFabricUdldLinkPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 6),
    _CfprApFabricUdldLinkPolicyIntId_Type()
)
cfprApFabricUdldLinkPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyIntId.setStatus("current")
_CfprApFabricUdldLinkPolicyMode_Type = CfprApFabricUdldLinkPolicyMode
_CfprApFabricUdldLinkPolicyMode_Object = MibTableColumn
cfprApFabricUdldLinkPolicyMode = _CfprApFabricUdldLinkPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 7),
    _CfprApFabricUdldLinkPolicyMode_Type()
)
cfprApFabricUdldLinkPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyMode.setStatus("current")
_CfprApFabricUdldLinkPolicyName_Type = SnmpAdminString
_CfprApFabricUdldLinkPolicyName_Object = MibTableColumn
cfprApFabricUdldLinkPolicyName = _CfprApFabricUdldLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 8),
    _CfprApFabricUdldLinkPolicyName_Type()
)
cfprApFabricUdldLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyName.setStatus("current")
_CfprApFabricUdldLinkPolicyPolicyLevel_Type = Gauge32
_CfprApFabricUdldLinkPolicyPolicyLevel_Object = MibTableColumn
cfprApFabricUdldLinkPolicyPolicyLevel = _CfprApFabricUdldLinkPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 9),
    _CfprApFabricUdldLinkPolicyPolicyLevel_Type()
)
cfprApFabricUdldLinkPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyPolicyLevel.setStatus("current")
_CfprApFabricUdldLinkPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricUdldLinkPolicyPolicyOwner_Object = MibTableColumn
cfprApFabricUdldLinkPolicyPolicyOwner = _CfprApFabricUdldLinkPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 10),
    _CfprApFabricUdldLinkPolicyPolicyOwner_Type()
)
cfprApFabricUdldLinkPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyPolicyOwner.setStatus("current")
_CfprApFabricUdldLinkPolicyProtocol_Type = CfprApFabricEthUdldPolicyProtocol
_CfprApFabricUdldLinkPolicyProtocol_Object = MibTableColumn
cfprApFabricUdldLinkPolicyProtocol = _CfprApFabricUdldLinkPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 11),
    _CfprApFabricUdldLinkPolicyProtocol_Type()
)
cfprApFabricUdldLinkPolicyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyProtocol.setStatus("current")
_CfprApFabricUdldLinkPolicyType_Type = CfprApFabricEthLinkPolicyType
_CfprApFabricUdldLinkPolicyType_Object = MibTableColumn
cfprApFabricUdldLinkPolicyType = _CfprApFabricUdldLinkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 113, 1, 12),
    _CfprApFabricUdldLinkPolicyType_Type()
)
cfprApFabricUdldLinkPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldLinkPolicyType.setStatus("current")
_CfprApFabricUdldPolicyTable_Object = MibTable
cfprApFabricUdldPolicyTable = _CfprApFabricUdldPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114)
)
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyTable.setStatus("current")
_CfprApFabricUdldPolicyEntry_Object = MibTableRow
cfprApFabricUdldPolicyEntry = _CfprApFabricUdldPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1)
)
cfprApFabricUdldPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricUdldPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyEntry.setStatus("current")
_CfprApFabricUdldPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApFabricUdldPolicyInstanceId_Object = MibTableColumn
cfprApFabricUdldPolicyInstanceId = _CfprApFabricUdldPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 1),
    _CfprApFabricUdldPolicyInstanceId_Type()
)
cfprApFabricUdldPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyInstanceId.setStatus("current")
_CfprApFabricUdldPolicyDn_Type = CfprApManagedObjectDn
_CfprApFabricUdldPolicyDn_Object = MibTableColumn
cfprApFabricUdldPolicyDn = _CfprApFabricUdldPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 2),
    _CfprApFabricUdldPolicyDn_Type()
)
cfprApFabricUdldPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyDn.setStatus("current")
_CfprApFabricUdldPolicyRn_Type = SnmpAdminString
_CfprApFabricUdldPolicyRn_Object = MibTableColumn
cfprApFabricUdldPolicyRn = _CfprApFabricUdldPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 3),
    _CfprApFabricUdldPolicyRn_Type()
)
cfprApFabricUdldPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyRn.setStatus("current")
_CfprApFabricUdldPolicyDescr_Type = SnmpAdminString
_CfprApFabricUdldPolicyDescr_Object = MibTableColumn
cfprApFabricUdldPolicyDescr = _CfprApFabricUdldPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 4),
    _CfprApFabricUdldPolicyDescr_Type()
)
cfprApFabricUdldPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyDescr.setStatus("current")
_CfprApFabricUdldPolicyIntId_Type = SnmpAdminString
_CfprApFabricUdldPolicyIntId_Object = MibTableColumn
cfprApFabricUdldPolicyIntId = _CfprApFabricUdldPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 5),
    _CfprApFabricUdldPolicyIntId_Type()
)
cfprApFabricUdldPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyIntId.setStatus("current")
_CfprApFabricUdldPolicyMsgInterval_Type = Gauge32
_CfprApFabricUdldPolicyMsgInterval_Object = MibTableColumn
cfprApFabricUdldPolicyMsgInterval = _CfprApFabricUdldPolicyMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 6),
    _CfprApFabricUdldPolicyMsgInterval_Type()
)
cfprApFabricUdldPolicyMsgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyMsgInterval.setStatus("current")
_CfprApFabricUdldPolicyName_Type = SnmpAdminString
_CfprApFabricUdldPolicyName_Object = MibTableColumn
cfprApFabricUdldPolicyName = _CfprApFabricUdldPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 7),
    _CfprApFabricUdldPolicyName_Type()
)
cfprApFabricUdldPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyName.setStatus("current")
_CfprApFabricUdldPolicyPolicyLevel_Type = Gauge32
_CfprApFabricUdldPolicyPolicyLevel_Object = MibTableColumn
cfprApFabricUdldPolicyPolicyLevel = _CfprApFabricUdldPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 8),
    _CfprApFabricUdldPolicyPolicyLevel_Type()
)
cfprApFabricUdldPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyPolicyLevel.setStatus("current")
_CfprApFabricUdldPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricUdldPolicyPolicyOwner_Object = MibTableColumn
cfprApFabricUdldPolicyPolicyOwner = _CfprApFabricUdldPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 9),
    _CfprApFabricUdldPolicyPolicyOwner_Type()
)
cfprApFabricUdldPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyPolicyOwner.setStatus("current")
_CfprApFabricUdldPolicyRecoveryAction_Type = CfprApFabricRecoveryAction
_CfprApFabricUdldPolicyRecoveryAction_Object = MibTableColumn
cfprApFabricUdldPolicyRecoveryAction = _CfprApFabricUdldPolicyRecoveryAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 114, 1, 10),
    _CfprApFabricUdldPolicyRecoveryAction_Type()
)
cfprApFabricUdldPolicyRecoveryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricUdldPolicyRecoveryAction.setStatus("current")
_CfprApFabricVConTable_Object = MibTable
cfprApFabricVConTable = _CfprApFabricVConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115)
)
if mibBuilder.loadTexts:
    cfprApFabricVConTable.setStatus("current")
_CfprApFabricVConEntry_Object = MibTableRow
cfprApFabricVConEntry = _CfprApFabricVConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1)
)
cfprApFabricVConEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVConInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVConEntry.setStatus("current")
_CfprApFabricVConInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVConInstanceId_Object = MibTableColumn
cfprApFabricVConInstanceId = _CfprApFabricVConInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 1),
    _CfprApFabricVConInstanceId_Type()
)
cfprApFabricVConInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVConInstanceId.setStatus("current")
_CfprApFabricVConDn_Type = CfprApManagedObjectDn
_CfprApFabricVConDn_Object = MibTableColumn
cfprApFabricVConDn = _CfprApFabricVConDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 2),
    _CfprApFabricVConDn_Type()
)
cfprApFabricVConDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConDn.setStatus("current")
_CfprApFabricVConRn_Type = SnmpAdminString
_CfprApFabricVConRn_Object = MibTableColumn
cfprApFabricVConRn = _CfprApFabricVConRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 3),
    _CfprApFabricVConRn_Type()
)
cfprApFabricVConRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConRn.setStatus("current")
_CfprApFabricVConEquipmentDn_Type = SnmpAdminString
_CfprApFabricVConEquipmentDn_Object = MibTableColumn
cfprApFabricVConEquipmentDn = _CfprApFabricVConEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 4),
    _CfprApFabricVConEquipmentDn_Type()
)
cfprApFabricVConEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConEquipmentDn.setStatus("current")
_CfprApFabricVConFabric_Type = SnmpAdminString
_CfprApFabricVConFabric_Object = MibTableColumn
cfprApFabricVConFabric = _CfprApFabricVConFabric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 5),
    _CfprApFabricVConFabric_Type()
)
cfprApFabricVConFabric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConFabric.setStatus("current")
_CfprApFabricVConId_Type = SnmpAdminString
_CfprApFabricVConId_Object = MibTableColumn
cfprApFabricVConId = _CfprApFabricVConId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 6),
    _CfprApFabricVConId_Type()
)
cfprApFabricVConId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConId.setStatus("current")
_CfprApFabricVConInstType_Type = CfprApFabricVConInstType
_CfprApFabricVConInstType_Object = MibTableColumn
cfprApFabricVConInstType = _CfprApFabricVConInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 7),
    _CfprApFabricVConInstType_Type()
)
cfprApFabricVConInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConInstType.setStatus("current")
_CfprApFabricVConPlacement_Type = CfprApFabricVConPlacementPref
_CfprApFabricVConPlacement_Object = MibTableColumn
cfprApFabricVConPlacement = _CfprApFabricVConPlacement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 8),
    _CfprApFabricVConPlacement_Type()
)
cfprApFabricVConPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConPlacement.setStatus("current")
_CfprApFabricVConSelect_Type = CfprApFabricVConSelectPref
_CfprApFabricVConSelect_Object = MibTableColumn
cfprApFabricVConSelect = _CfprApFabricVConSelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 9),
    _CfprApFabricVConSelect_Type()
)
cfprApFabricVConSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConSelect.setStatus("current")
_CfprApFabricVConShare_Type = CfprApFabricVConSharePref
_CfprApFabricVConShare_Object = MibTableColumn
cfprApFabricVConShare = _CfprApFabricVConShare_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 10),
    _CfprApFabricVConShare_Type()
)
cfprApFabricVConShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConShare.setStatus("current")
_CfprApFabricVConTransport_Type = CfprApFabricVConTransportPref
_CfprApFabricVConTransport_Object = MibTableColumn
cfprApFabricVConTransport = _CfprApFabricVConTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 115, 1, 11),
    _CfprApFabricVConTransport_Type()
)
cfprApFabricVConTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConTransport.setStatus("current")
_CfprApFabricVConProfileTable_Object = MibTable
cfprApFabricVConProfileTable = _CfprApFabricVConProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116)
)
if mibBuilder.loadTexts:
    cfprApFabricVConProfileTable.setStatus("current")
_CfprApFabricVConProfileEntry_Object = MibTableRow
cfprApFabricVConProfileEntry = _CfprApFabricVConProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1)
)
cfprApFabricVConProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVConProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVConProfileEntry.setStatus("current")
_CfprApFabricVConProfileInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVConProfileInstanceId_Object = MibTableColumn
cfprApFabricVConProfileInstanceId = _CfprApFabricVConProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 1),
    _CfprApFabricVConProfileInstanceId_Type()
)
cfprApFabricVConProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVConProfileInstanceId.setStatus("current")
_CfprApFabricVConProfileDn_Type = CfprApManagedObjectDn
_CfprApFabricVConProfileDn_Object = MibTableColumn
cfprApFabricVConProfileDn = _CfprApFabricVConProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 2),
    _CfprApFabricVConProfileDn_Type()
)
cfprApFabricVConProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConProfileDn.setStatus("current")
_CfprApFabricVConProfileRn_Type = SnmpAdminString
_CfprApFabricVConProfileRn_Object = MibTableColumn
cfprApFabricVConProfileRn = _CfprApFabricVConProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 3),
    _CfprApFabricVConProfileRn_Type()
)
cfprApFabricVConProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConProfileRn.setStatus("current")
_CfprApFabricVConProfileDescr_Type = SnmpAdminString
_CfprApFabricVConProfileDescr_Object = MibTableColumn
cfprApFabricVConProfileDescr = _CfprApFabricVConProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 4),
    _CfprApFabricVConProfileDescr_Type()
)
cfprApFabricVConProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConProfileDescr.setStatus("current")
_CfprApFabricVConProfileIntId_Type = SnmpAdminString
_CfprApFabricVConProfileIntId_Object = MibTableColumn
cfprApFabricVConProfileIntId = _CfprApFabricVConProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 5),
    _CfprApFabricVConProfileIntId_Type()
)
cfprApFabricVConProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConProfileIntId.setStatus("current")
_CfprApFabricVConProfileMezzMapping_Type = CfprApFabricVConMappingScheme
_CfprApFabricVConProfileMezzMapping_Object = MibTableColumn
cfprApFabricVConProfileMezzMapping = _CfprApFabricVConProfileMezzMapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 6),
    _CfprApFabricVConProfileMezzMapping_Type()
)
cfprApFabricVConProfileMezzMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConProfileMezzMapping.setStatus("current")
_CfprApFabricVConProfileName_Type = SnmpAdminString
_CfprApFabricVConProfileName_Object = MibTableColumn
cfprApFabricVConProfileName = _CfprApFabricVConProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 7),
    _CfprApFabricVConProfileName_Type()
)
cfprApFabricVConProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConProfileName.setStatus("current")
_CfprApFabricVConProfilePolicyLevel_Type = Gauge32
_CfprApFabricVConProfilePolicyLevel_Object = MibTableColumn
cfprApFabricVConProfilePolicyLevel = _CfprApFabricVConProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 8),
    _CfprApFabricVConProfilePolicyLevel_Type()
)
cfprApFabricVConProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConProfilePolicyLevel.setStatus("current")
_CfprApFabricVConProfilePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApFabricVConProfilePolicyOwner_Object = MibTableColumn
cfprApFabricVConProfilePolicyOwner = _CfprApFabricVConProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 116, 1, 9),
    _CfprApFabricVConProfilePolicyOwner_Type()
)
cfprApFabricVConProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVConProfilePolicyOwner.setStatus("current")
_CfprApFabricVlanTable_Object = MibTable
cfprApFabricVlanTable = _CfprApFabricVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117)
)
if mibBuilder.loadTexts:
    cfprApFabricVlanTable.setStatus("current")
_CfprApFabricVlanEntry_Object = MibTableRow
cfprApFabricVlanEntry = _CfprApFabricVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1)
)
cfprApFabricVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVlanEntry.setStatus("current")
_CfprApFabricVlanInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVlanInstanceId_Object = MibTableColumn
cfprApFabricVlanInstanceId = _CfprApFabricVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 1),
    _CfprApFabricVlanInstanceId_Type()
)
cfprApFabricVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVlanInstanceId.setStatus("current")
_CfprApFabricVlanDn_Type = CfprApManagedObjectDn
_CfprApFabricVlanDn_Object = MibTableColumn
cfprApFabricVlanDn = _CfprApFabricVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 2),
    _CfprApFabricVlanDn_Type()
)
cfprApFabricVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanDn.setStatus("current")
_CfprApFabricVlanRn_Type = SnmpAdminString
_CfprApFabricVlanRn_Object = MibTableColumn
cfprApFabricVlanRn = _CfprApFabricVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 3),
    _CfprApFabricVlanRn_Type()
)
cfprApFabricVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanRn.setStatus("current")
_CfprApFabricVlanAssocPrimaryVlanState_Type = CfprApFabricVlanAssocPrimaryVlanState
_CfprApFabricVlanAssocPrimaryVlanState_Object = MibTableColumn
cfprApFabricVlanAssocPrimaryVlanState = _CfprApFabricVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 4),
    _CfprApFabricVlanAssocPrimaryVlanState_Type()
)
cfprApFabricVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanAssocPrimaryVlanState.setStatus("current")
_CfprApFabricVlanAssocPrimaryVlanSwitchId_Type = CfprApFabricAVlanAssocPrimaryVlanSwitchId
_CfprApFabricVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprApFabricVlanAssocPrimaryVlanSwitchId = _CfprApFabricVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 5),
    _CfprApFabricVlanAssocPrimaryVlanSwitchId_Type()
)
cfprApFabricVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprApFabricVlanCloud_Type = CfprApFabricCloudType
_CfprApFabricVlanCloud_Object = MibTableColumn
cfprApFabricVlanCloud = _CfprApFabricVlanCloud_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 6),
    _CfprApFabricVlanCloud_Type()
)
cfprApFabricVlanCloud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanCloud.setStatus("current")
_CfprApFabricVlanCompressionType_Type = CfprApFabricVlanCompType
_CfprApFabricVlanCompressionType_Object = MibTableColumn
cfprApFabricVlanCompressionType = _CfprApFabricVlanCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 7),
    _CfprApFabricVlanCompressionType_Type()
)
cfprApFabricVlanCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanCompressionType.setStatus("current")
_CfprApFabricVlanConfigIssues_Type = CfprApFabricVlanConfigIssues
_CfprApFabricVlanConfigIssues_Object = MibTableColumn
cfprApFabricVlanConfigIssues = _CfprApFabricVlanConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 8),
    _CfprApFabricVlanConfigIssues_Type()
)
cfprApFabricVlanConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanConfigIssues.setStatus("current")
_CfprApFabricVlanDefaultNet_Type = TruthValue
_CfprApFabricVlanDefaultNet_Object = MibTableColumn
cfprApFabricVlanDefaultNet = _CfprApFabricVlanDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 9),
    _CfprApFabricVlanDefaultNet_Type()
)
cfprApFabricVlanDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanDefaultNet.setStatus("current")
_CfprApFabricVlanEpDn_Type = SnmpAdminString
_CfprApFabricVlanEpDn_Object = MibTableColumn
cfprApFabricVlanEpDn = _CfprApFabricVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 10),
    _CfprApFabricVlanEpDn_Type()
)
cfprApFabricVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpDn.setStatus("current")
_CfprApFabricVlanFltAggr_Type = Unsigned64
_CfprApFabricVlanFltAggr_Object = MibTableColumn
cfprApFabricVlanFltAggr = _CfprApFabricVlanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 11),
    _CfprApFabricVlanFltAggr_Type()
)
cfprApFabricVlanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanFltAggr.setStatus("current")
_CfprApFabricVlanGlobal_Type = Unsigned64
_CfprApFabricVlanGlobal_Object = MibTableColumn
cfprApFabricVlanGlobal = _CfprApFabricVlanGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 12),
    _CfprApFabricVlanGlobal_Type()
)
cfprApFabricVlanGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanGlobal.setStatus("current")
_CfprApFabricVlanId_Type = Gauge32
_CfprApFabricVlanId_Object = MibTableColumn
cfprApFabricVlanId = _CfprApFabricVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 13),
    _CfprApFabricVlanId_Type()
)
cfprApFabricVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanId.setStatus("current")
_CfprApFabricVlanIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApFabricVlanIfRole_Object = MibTableColumn
cfprApFabricVlanIfRole = _CfprApFabricVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 14),
    _CfprApFabricVlanIfRole_Type()
)
cfprApFabricVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanIfRole.setStatus("current")
_CfprApFabricVlanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApFabricVlanIfType_Object = MibTableColumn
cfprApFabricVlanIfType = _CfprApFabricVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 15),
    _CfprApFabricVlanIfType_Type()
)
cfprApFabricVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanIfType.setStatus("current")
_CfprApFabricVlanLocal_Type = Unsigned64
_CfprApFabricVlanLocal_Object = MibTableColumn
cfprApFabricVlanLocal = _CfprApFabricVlanLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 16),
    _CfprApFabricVlanLocal_Type()
)
cfprApFabricVlanLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanLocal.setStatus("current")
_CfprApFabricVlanLocale_Type = CfprApFabricVnetEpLocale
_CfprApFabricVlanLocale_Object = MibTableColumn
cfprApFabricVlanLocale = _CfprApFabricVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 17),
    _CfprApFabricVlanLocale_Type()
)
cfprApFabricVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanLocale.setStatus("current")
_CfprApFabricVlanMcastPolicyName_Type = SnmpAdminString
_CfprApFabricVlanMcastPolicyName_Object = MibTableColumn
cfprApFabricVlanMcastPolicyName = _CfprApFabricVlanMcastPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 18),
    _CfprApFabricVlanMcastPolicyName_Type()
)
cfprApFabricVlanMcastPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanMcastPolicyName.setStatus("current")
_CfprApFabricVlanName_Type = SnmpAdminString
_CfprApFabricVlanName_Object = MibTableColumn
cfprApFabricVlanName = _CfprApFabricVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 19),
    _CfprApFabricVlanName_Type()
)
cfprApFabricVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanName.setStatus("current")
_CfprApFabricVlanOperMcastPolicyName_Type = SnmpAdminString
_CfprApFabricVlanOperMcastPolicyName_Object = MibTableColumn
cfprApFabricVlanOperMcastPolicyName = _CfprApFabricVlanOperMcastPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 20),
    _CfprApFabricVlanOperMcastPolicyName_Type()
)
cfprApFabricVlanOperMcastPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanOperMcastPolicyName.setStatus("current")
_CfprApFabricVlanOperState_Type = CfprApFabricVlanOperState
_CfprApFabricVlanOperState_Object = MibTableColumn
cfprApFabricVlanOperState = _CfprApFabricVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 21),
    _CfprApFabricVlanOperState_Type()
)
cfprApFabricVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanOperState.setStatus("current")
_CfprApFabricVlanOverlapStateForA_Type = CfprApFabricVlanOverlapState
_CfprApFabricVlanOverlapStateForA_Object = MibTableColumn
cfprApFabricVlanOverlapStateForA = _CfprApFabricVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 22),
    _CfprApFabricVlanOverlapStateForA_Type()
)
cfprApFabricVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanOverlapStateForA.setStatus("current")
_CfprApFabricVlanOverlapStateForB_Type = CfprApFabricVlanOverlapState
_CfprApFabricVlanOverlapStateForB_Object = MibTableColumn
cfprApFabricVlanOverlapStateForB = _CfprApFabricVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 23),
    _CfprApFabricVlanOverlapStateForB_Type()
)
cfprApFabricVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanOverlapStateForB.setStatus("current")
_CfprApFabricVlanPeerDn_Type = SnmpAdminString
_CfprApFabricVlanPeerDn_Object = MibTableColumn
cfprApFabricVlanPeerDn = _CfprApFabricVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 24),
    _CfprApFabricVlanPeerDn_Type()
)
cfprApFabricVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPeerDn.setStatus("current")
_CfprApFabricVlanPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApFabricVlanPolicyOwner_Object = MibTableColumn
cfprApFabricVlanPolicyOwner = _CfprApFabricVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 25),
    _CfprApFabricVlanPolicyOwner_Type()
)
cfprApFabricVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPolicyOwner.setStatus("current")
_CfprApFabricVlanPubNwDn_Type = SnmpAdminString
_CfprApFabricVlanPubNwDn_Object = MibTableColumn
cfprApFabricVlanPubNwDn = _CfprApFabricVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 26),
    _CfprApFabricVlanPubNwDn_Type()
)
cfprApFabricVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPubNwDn.setStatus("current")
_CfprApFabricVlanPubNwId_Type = Gauge32
_CfprApFabricVlanPubNwId_Object = MibTableColumn
cfprApFabricVlanPubNwId = _CfprApFabricVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 27),
    _CfprApFabricVlanPubNwId_Type()
)
cfprApFabricVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPubNwId.setStatus("current")
_CfprApFabricVlanPubNwName_Type = SnmpAdminString
_CfprApFabricVlanPubNwName_Object = MibTableColumn
cfprApFabricVlanPubNwName = _CfprApFabricVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 28),
    _CfprApFabricVlanPubNwName_Type()
)
cfprApFabricVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPubNwName.setStatus("current")
_CfprApFabricVlanSharing_Type = CfprApFabricAVlanSharing
_CfprApFabricVlanSharing_Object = MibTableColumn
cfprApFabricVlanSharing = _CfprApFabricVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 29),
    _CfprApFabricVlanSharing_Type()
)
cfprApFabricVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanSharing.setStatus("current")
_CfprApFabricVlanSwitchId_Type = CfprApFabricVlanSwitchId
_CfprApFabricVlanSwitchId_Object = MibTableColumn
cfprApFabricVlanSwitchId = _CfprApFabricVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 30),
    _CfprApFabricVlanSwitchId_Type()
)
cfprApFabricVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanSwitchId.setStatus("current")
_CfprApFabricVlanTransport_Type = CfprApFabricAVlanTransport
_CfprApFabricVlanTransport_Object = MibTableColumn
cfprApFabricVlanTransport = _CfprApFabricVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 31),
    _CfprApFabricVlanTransport_Type()
)
cfprApFabricVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanTransport.setStatus("current")
_CfprApFabricVlanType_Type = CfprApFabricAVlanType
_CfprApFabricVlanType_Object = MibTableColumn
cfprApFabricVlanType = _CfprApFabricVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 117, 1, 32),
    _CfprApFabricVlanType_Type()
)
cfprApFabricVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanType.setStatus("current")
_CfprApFabricVlanEpTable_Object = MibTable
cfprApFabricVlanEpTable = _CfprApFabricVlanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118)
)
if mibBuilder.loadTexts:
    cfprApFabricVlanEpTable.setStatus("current")
_CfprApFabricVlanEpEntry_Object = MibTableRow
cfprApFabricVlanEpEntry = _CfprApFabricVlanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1)
)
cfprApFabricVlanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVlanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVlanEpEntry.setStatus("current")
_CfprApFabricVlanEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVlanEpInstanceId_Object = MibTableColumn
cfprApFabricVlanEpInstanceId = _CfprApFabricVlanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 1),
    _CfprApFabricVlanEpInstanceId_Type()
)
cfprApFabricVlanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpInstanceId.setStatus("current")
_CfprApFabricVlanEpDnData_Type = CfprApManagedObjectDn
_CfprApFabricVlanEpDnData_Object = MibTableColumn
cfprApFabricVlanEpDnData = _CfprApFabricVlanEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 2),
    _CfprApFabricVlanEpDnData_Type()
)
cfprApFabricVlanEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpDnData.setStatus("current")
_CfprApFabricVlanEpRn_Type = SnmpAdminString
_CfprApFabricVlanEpRn_Object = MibTableColumn
cfprApFabricVlanEpRn = _CfprApFabricVlanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 3),
    _CfprApFabricVlanEpRn_Type()
)
cfprApFabricVlanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpRn.setStatus("current")
_CfprApFabricVlanEpAssocPrimaryVlanState_Type = CfprApFabricVlanAssocPrimaryVlanState
_CfprApFabricVlanEpAssocPrimaryVlanState_Object = MibTableColumn
cfprApFabricVlanEpAssocPrimaryVlanState = _CfprApFabricVlanEpAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 4),
    _CfprApFabricVlanEpAssocPrimaryVlanState_Type()
)
cfprApFabricVlanEpAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpAssocPrimaryVlanState.setStatus("current")
_CfprApFabricVlanEpAssocPrimaryVlanSwitchId_Type = CfprApFabricAVlanAssocPrimaryVlanSwitchId
_CfprApFabricVlanEpAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprApFabricVlanEpAssocPrimaryVlanSwitchId = _CfprApFabricVlanEpAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 5),
    _CfprApFabricVlanEpAssocPrimaryVlanSwitchId_Type()
)
cfprApFabricVlanEpAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpAssocPrimaryVlanSwitchId.setStatus("current")
_CfprApFabricVlanEpEpDn_Type = SnmpAdminString
_CfprApFabricVlanEpEpDn_Object = MibTableColumn
cfprApFabricVlanEpEpDn = _CfprApFabricVlanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 6),
    _CfprApFabricVlanEpEpDn_Type()
)
cfprApFabricVlanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpEpDn.setStatus("current")
_CfprApFabricVlanEpId_Type = Gauge32
_CfprApFabricVlanEpId_Object = MibTableColumn
cfprApFabricVlanEpId = _CfprApFabricVlanEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 7),
    _CfprApFabricVlanEpId_Type()
)
cfprApFabricVlanEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpId.setStatus("current")
_CfprApFabricVlanEpIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApFabricVlanEpIfRole_Object = MibTableColumn
cfprApFabricVlanEpIfRole = _CfprApFabricVlanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 8),
    _CfprApFabricVlanEpIfRole_Type()
)
cfprApFabricVlanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpIfRole.setStatus("current")
_CfprApFabricVlanEpIfType_Type = CfprApNetworkVnetEpIfType
_CfprApFabricVlanEpIfType_Object = MibTableColumn
cfprApFabricVlanEpIfType = _CfprApFabricVlanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 9),
    _CfprApFabricVlanEpIfType_Type()
)
cfprApFabricVlanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpIfType.setStatus("current")
_CfprApFabricVlanEpIsNative_Type = TruthValue
_CfprApFabricVlanEpIsNative_Object = MibTableColumn
cfprApFabricVlanEpIsNative = _CfprApFabricVlanEpIsNative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 10),
    _CfprApFabricVlanEpIsNative_Type()
)
cfprApFabricVlanEpIsNative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpIsNative.setStatus("current")
_CfprApFabricVlanEpLocale_Type = CfprApFabricVnetEpLocale
_CfprApFabricVlanEpLocale_Object = MibTableColumn
cfprApFabricVlanEpLocale = _CfprApFabricVlanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 11),
    _CfprApFabricVlanEpLocale_Type()
)
cfprApFabricVlanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpLocale.setStatus("current")
_CfprApFabricVlanEpName_Type = SnmpAdminString
_CfprApFabricVlanEpName_Object = MibTableColumn
cfprApFabricVlanEpName = _CfprApFabricVlanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 12),
    _CfprApFabricVlanEpName_Type()
)
cfprApFabricVlanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpName.setStatus("current")
_CfprApFabricVlanEpOperState_Type = CfprApFabricVlanOperState
_CfprApFabricVlanEpOperState_Object = MibTableColumn
cfprApFabricVlanEpOperState = _CfprApFabricVlanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 13),
    _CfprApFabricVlanEpOperState_Type()
)
cfprApFabricVlanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpOperState.setStatus("current")
_CfprApFabricVlanEpOverlapStateForA_Type = CfprApFabricVlanOverlapState
_CfprApFabricVlanEpOverlapStateForA_Object = MibTableColumn
cfprApFabricVlanEpOverlapStateForA = _CfprApFabricVlanEpOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 14),
    _CfprApFabricVlanEpOverlapStateForA_Type()
)
cfprApFabricVlanEpOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpOverlapStateForA.setStatus("current")
_CfprApFabricVlanEpOverlapStateForB_Type = CfprApFabricVlanOverlapState
_CfprApFabricVlanEpOverlapStateForB_Object = MibTableColumn
cfprApFabricVlanEpOverlapStateForB = _CfprApFabricVlanEpOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 15),
    _CfprApFabricVlanEpOverlapStateForB_Type()
)
cfprApFabricVlanEpOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpOverlapStateForB.setStatus("current")
_CfprApFabricVlanEpPeerDn_Type = SnmpAdminString
_CfprApFabricVlanEpPeerDn_Object = MibTableColumn
cfprApFabricVlanEpPeerDn = _CfprApFabricVlanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 16),
    _CfprApFabricVlanEpPeerDn_Type()
)
cfprApFabricVlanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpPeerDn.setStatus("current")
_CfprApFabricVlanEpPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApFabricVlanEpPolicyOwner_Object = MibTableColumn
cfprApFabricVlanEpPolicyOwner = _CfprApFabricVlanEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 17),
    _CfprApFabricVlanEpPolicyOwner_Type()
)
cfprApFabricVlanEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpPolicyOwner.setStatus("current")
_CfprApFabricVlanEpPubNwDn_Type = SnmpAdminString
_CfprApFabricVlanEpPubNwDn_Object = MibTableColumn
cfprApFabricVlanEpPubNwDn = _CfprApFabricVlanEpPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 18),
    _CfprApFabricVlanEpPubNwDn_Type()
)
cfprApFabricVlanEpPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpPubNwDn.setStatus("current")
_CfprApFabricVlanEpPubNwId_Type = Gauge32
_CfprApFabricVlanEpPubNwId_Object = MibTableColumn
cfprApFabricVlanEpPubNwId = _CfprApFabricVlanEpPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 19),
    _CfprApFabricVlanEpPubNwId_Type()
)
cfprApFabricVlanEpPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpPubNwId.setStatus("current")
_CfprApFabricVlanEpPubNwName_Type = SnmpAdminString
_CfprApFabricVlanEpPubNwName_Object = MibTableColumn
cfprApFabricVlanEpPubNwName = _CfprApFabricVlanEpPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 20),
    _CfprApFabricVlanEpPubNwName_Type()
)
cfprApFabricVlanEpPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpPubNwName.setStatus("current")
_CfprApFabricVlanEpSharing_Type = CfprApFabricAVlanSharing
_CfprApFabricVlanEpSharing_Object = MibTableColumn
cfprApFabricVlanEpSharing = _CfprApFabricVlanEpSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 21),
    _CfprApFabricVlanEpSharing_Type()
)
cfprApFabricVlanEpSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpSharing.setStatus("current")
_CfprApFabricVlanEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricVlanEpSwitchId_Object = MibTableColumn
cfprApFabricVlanEpSwitchId = _CfprApFabricVlanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 22),
    _CfprApFabricVlanEpSwitchId_Type()
)
cfprApFabricVlanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpSwitchId.setStatus("current")
_CfprApFabricVlanEpTransport_Type = CfprApFabricAVlanTransport
_CfprApFabricVlanEpTransport_Object = MibTableColumn
cfprApFabricVlanEpTransport = _CfprApFabricVlanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 23),
    _CfprApFabricVlanEpTransport_Type()
)
cfprApFabricVlanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpTransport.setStatus("current")
_CfprApFabricVlanEpType_Type = CfprApFabricAVlanType
_CfprApFabricVlanEpType_Object = MibTableColumn
cfprApFabricVlanEpType = _CfprApFabricVlanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 118, 1, 24),
    _CfprApFabricVlanEpType_Type()
)
cfprApFabricVlanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanEpType.setStatus("current")
_CfprApFabricVlanGroupReqTable_Object = MibTable
cfprApFabricVlanGroupReqTable = _CfprApFabricVlanGroupReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 119)
)
if mibBuilder.loadTexts:
    cfprApFabricVlanGroupReqTable.setStatus("current")
_CfprApFabricVlanGroupReqEntry_Object = MibTableRow
cfprApFabricVlanGroupReqEntry = _CfprApFabricVlanGroupReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 119, 1)
)
cfprApFabricVlanGroupReqEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVlanGroupReqInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVlanGroupReqEntry.setStatus("current")
_CfprApFabricVlanGroupReqInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVlanGroupReqInstanceId_Object = MibTableColumn
cfprApFabricVlanGroupReqInstanceId = _CfprApFabricVlanGroupReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 119, 1, 1),
    _CfprApFabricVlanGroupReqInstanceId_Type()
)
cfprApFabricVlanGroupReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVlanGroupReqInstanceId.setStatus("current")
_CfprApFabricVlanGroupReqDn_Type = CfprApManagedObjectDn
_CfprApFabricVlanGroupReqDn_Object = MibTableColumn
cfprApFabricVlanGroupReqDn = _CfprApFabricVlanGroupReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 119, 1, 2),
    _CfprApFabricVlanGroupReqDn_Type()
)
cfprApFabricVlanGroupReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanGroupReqDn.setStatus("current")
_CfprApFabricVlanGroupReqRn_Type = SnmpAdminString
_CfprApFabricVlanGroupReqRn_Object = MibTableColumn
cfprApFabricVlanGroupReqRn = _CfprApFabricVlanGroupReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 119, 1, 3),
    _CfprApFabricVlanGroupReqRn_Type()
)
cfprApFabricVlanGroupReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanGroupReqRn.setStatus("current")
_CfprApFabricVlanGroupReqConfigIssues_Type = CfprApFabricReqIssues
_CfprApFabricVlanGroupReqConfigIssues_Object = MibTableColumn
cfprApFabricVlanGroupReqConfigIssues = _CfprApFabricVlanGroupReqConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 119, 1, 4),
    _CfprApFabricVlanGroupReqConfigIssues_Type()
)
cfprApFabricVlanGroupReqConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanGroupReqConfigIssues.setStatus("current")
_CfprApFabricVlanGroupReqName_Type = SnmpAdminString
_CfprApFabricVlanGroupReqName_Object = MibTableColumn
cfprApFabricVlanGroupReqName = _CfprApFabricVlanGroupReqName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 119, 1, 5),
    _CfprApFabricVlanGroupReqName_Type()
)
cfprApFabricVlanGroupReqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanGroupReqName.setStatus("current")
_CfprApFabricVlanGroupReqType_Type = CfprApFabricAccessType
_CfprApFabricVlanGroupReqType_Object = MibTableColumn
cfprApFabricVlanGroupReqType = _CfprApFabricVlanGroupReqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 119, 1, 6),
    _CfprApFabricVlanGroupReqType_Type()
)
cfprApFabricVlanGroupReqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanGroupReqType.setStatus("current")
_CfprApFabricVlanPermitTable_Object = MibTable
cfprApFabricVlanPermitTable = _CfprApFabricVlanPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 120)
)
if mibBuilder.loadTexts:
    cfprApFabricVlanPermitTable.setStatus("current")
_CfprApFabricVlanPermitEntry_Object = MibTableRow
cfprApFabricVlanPermitEntry = _CfprApFabricVlanPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 120, 1)
)
cfprApFabricVlanPermitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVlanPermitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVlanPermitEntry.setStatus("current")
_CfprApFabricVlanPermitInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVlanPermitInstanceId_Object = MibTableColumn
cfprApFabricVlanPermitInstanceId = _CfprApFabricVlanPermitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 120, 1, 1),
    _CfprApFabricVlanPermitInstanceId_Type()
)
cfprApFabricVlanPermitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVlanPermitInstanceId.setStatus("current")
_CfprApFabricVlanPermitDn_Type = CfprApManagedObjectDn
_CfprApFabricVlanPermitDn_Object = MibTableColumn
cfprApFabricVlanPermitDn = _CfprApFabricVlanPermitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 120, 1, 2),
    _CfprApFabricVlanPermitDn_Type()
)
cfprApFabricVlanPermitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPermitDn.setStatus("current")
_CfprApFabricVlanPermitRn_Type = SnmpAdminString
_CfprApFabricVlanPermitRn_Object = MibTableColumn
cfprApFabricVlanPermitRn = _CfprApFabricVlanPermitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 120, 1, 3),
    _CfprApFabricVlanPermitRn_Type()
)
cfprApFabricVlanPermitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPermitRn.setStatus("current")
_CfprApFabricVlanPermitCloud_Type = CfprApFabricCloudType
_CfprApFabricVlanPermitCloud_Object = MibTableColumn
cfprApFabricVlanPermitCloud = _CfprApFabricVlanPermitCloud_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 120, 1, 4),
    _CfprApFabricVlanPermitCloud_Type()
)
cfprApFabricVlanPermitCloud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPermitCloud.setStatus("current")
_CfprApFabricVlanPermitName_Type = SnmpAdminString
_CfprApFabricVlanPermitName_Object = MibTableColumn
cfprApFabricVlanPermitName = _CfprApFabricVlanPermitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 120, 1, 5),
    _CfprApFabricVlanPermitName_Type()
)
cfprApFabricVlanPermitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPermitName.setStatus("current")
_CfprApFabricVlanPermitSwitchId_Type = SnmpAdminString
_CfprApFabricVlanPermitSwitchId_Object = MibTableColumn
cfprApFabricVlanPermitSwitchId = _CfprApFabricVlanPermitSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 120, 1, 6),
    _CfprApFabricVlanPermitSwitchId_Type()
)
cfprApFabricVlanPermitSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanPermitSwitchId.setStatus("current")
_CfprApFabricVlanReqTable_Object = MibTable
cfprApFabricVlanReqTable = _CfprApFabricVlanReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 121)
)
if mibBuilder.loadTexts:
    cfprApFabricVlanReqTable.setStatus("current")
_CfprApFabricVlanReqEntry_Object = MibTableRow
cfprApFabricVlanReqEntry = _CfprApFabricVlanReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 121, 1)
)
cfprApFabricVlanReqEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVlanReqInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVlanReqEntry.setStatus("current")
_CfprApFabricVlanReqInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVlanReqInstanceId_Object = MibTableColumn
cfprApFabricVlanReqInstanceId = _CfprApFabricVlanReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 121, 1, 1),
    _CfprApFabricVlanReqInstanceId_Type()
)
cfprApFabricVlanReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVlanReqInstanceId.setStatus("current")
_CfprApFabricVlanReqDn_Type = CfprApManagedObjectDn
_CfprApFabricVlanReqDn_Object = MibTableColumn
cfprApFabricVlanReqDn = _CfprApFabricVlanReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 121, 1, 2),
    _CfprApFabricVlanReqDn_Type()
)
cfprApFabricVlanReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanReqDn.setStatus("current")
_CfprApFabricVlanReqRn_Type = SnmpAdminString
_CfprApFabricVlanReqRn_Object = MibTableColumn
cfprApFabricVlanReqRn = _CfprApFabricVlanReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 121, 1, 3),
    _CfprApFabricVlanReqRn_Type()
)
cfprApFabricVlanReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanReqRn.setStatus("current")
_CfprApFabricVlanReqConfigIssues_Type = CfprApFabricReqIssues
_CfprApFabricVlanReqConfigIssues_Object = MibTableColumn
cfprApFabricVlanReqConfigIssues = _CfprApFabricVlanReqConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 121, 1, 4),
    _CfprApFabricVlanReqConfigIssues_Type()
)
cfprApFabricVlanReqConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanReqConfigIssues.setStatus("current")
_CfprApFabricVlanReqName_Type = SnmpAdminString
_CfprApFabricVlanReqName_Object = MibTableColumn
cfprApFabricVlanReqName = _CfprApFabricVlanReqName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 121, 1, 5),
    _CfprApFabricVlanReqName_Type()
)
cfprApFabricVlanReqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanReqName.setStatus("current")
_CfprApFabricVlanReqType_Type = CfprApFabricAccessType
_CfprApFabricVlanReqType_Object = MibTableColumn
cfprApFabricVlanReqType = _CfprApFabricVlanReqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 121, 1, 6),
    _CfprApFabricVlanReqType_Type()
)
cfprApFabricVlanReqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVlanReqType.setStatus("current")
_CfprApFabricVnetEpSyncEpTable_Object = MibTable
cfprApFabricVnetEpSyncEpTable = _CfprApFabricVnetEpSyncEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122)
)
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpTable.setStatus("current")
_CfprApFabricVnetEpSyncEpEntry_Object = MibTableRow
cfprApFabricVnetEpSyncEpEntry = _CfprApFabricVnetEpSyncEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1)
)
cfprApFabricVnetEpSyncEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVnetEpSyncEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpEntry.setStatus("current")
_CfprApFabricVnetEpSyncEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVnetEpSyncEpInstanceId_Object = MibTableColumn
cfprApFabricVnetEpSyncEpInstanceId = _CfprApFabricVnetEpSyncEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 1),
    _CfprApFabricVnetEpSyncEpInstanceId_Type()
)
cfprApFabricVnetEpSyncEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpInstanceId.setStatus("current")
_CfprApFabricVnetEpSyncEpDn_Type = CfprApManagedObjectDn
_CfprApFabricVnetEpSyncEpDn_Object = MibTableColumn
cfprApFabricVnetEpSyncEpDn = _CfprApFabricVnetEpSyncEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 2),
    _CfprApFabricVnetEpSyncEpDn_Type()
)
cfprApFabricVnetEpSyncEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpDn.setStatus("current")
_CfprApFabricVnetEpSyncEpRn_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpRn_Object = MibTableColumn
cfprApFabricVnetEpSyncEpRn = _CfprApFabricVnetEpSyncEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 3),
    _CfprApFabricVnetEpSyncEpRn_Type()
)
cfprApFabricVnetEpSyncEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpRn.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmDescr_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmDescr_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmDescr = _CfprApFabricVnetEpSyncEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 4),
    _CfprApFabricVnetEpSyncEpFsmDescr_Type()
)
cfprApFabricVnetEpSyncEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmDescr.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmPrev_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmPrev_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmPrev = _CfprApFabricVnetEpSyncEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 5),
    _CfprApFabricVnetEpSyncEpFsmPrev_Type()
)
cfprApFabricVnetEpSyncEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmPrev.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmProgr_Type = Gauge32
_CfprApFabricVnetEpSyncEpFsmProgr_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmProgr = _CfprApFabricVnetEpSyncEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 6),
    _CfprApFabricVnetEpSyncEpFsmProgr_Type()
)
cfprApFabricVnetEpSyncEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmProgr.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmRmtInvErrCode_Type = Gauge32
_CfprApFabricVnetEpSyncEpFsmRmtInvErrCode_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmRmtInvErrCode = _CfprApFabricVnetEpSyncEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 7),
    _CfprApFabricVnetEpSyncEpFsmRmtInvErrCode_Type()
)
cfprApFabricVnetEpSyncEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmRmtInvErrCode.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmRmtInvErrDescr = _CfprApFabricVnetEpSyncEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 8),
    _CfprApFabricVnetEpSyncEpFsmRmtInvErrDescr_Type()
)
cfprApFabricVnetEpSyncEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmRmtInvErrDescr.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmRmtInvRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFabricVnetEpSyncEpFsmRmtInvRslt_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmRmtInvRslt = _CfprApFabricVnetEpSyncEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 9),
    _CfprApFabricVnetEpSyncEpFsmRmtInvRslt_Type()
)
cfprApFabricVnetEpSyncEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmRmtInvRslt.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageDescr_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmStageDescr_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageDescr = _CfprApFabricVnetEpSyncEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 10),
    _CfprApFabricVnetEpSyncEpFsmStageDescr_Type()
)
cfprApFabricVnetEpSyncEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageDescr.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStamp_Type = DateAndTime
_CfprApFabricVnetEpSyncEpFsmStamp_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStamp = _CfprApFabricVnetEpSyncEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 11),
    _CfprApFabricVnetEpSyncEpFsmStamp_Type()
)
cfprApFabricVnetEpSyncEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStamp.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStatus_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmStatus_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStatus = _CfprApFabricVnetEpSyncEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 12),
    _CfprApFabricVnetEpSyncEpFsmStatus_Type()
)
cfprApFabricVnetEpSyncEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStatus.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTry_Type = Gauge32
_CfprApFabricVnetEpSyncEpFsmTry_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmTry = _CfprApFabricVnetEpSyncEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 13),
    _CfprApFabricVnetEpSyncEpFsmTry_Type()
)
cfprApFabricVnetEpSyncEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTry.setStatus("current")
_CfprApFabricVnetEpSyncEpGenNumSync_Type = Gauge32
_CfprApFabricVnetEpSyncEpGenNumSync_Object = MibTableColumn
cfprApFabricVnetEpSyncEpGenNumSync = _CfprApFabricVnetEpSyncEpGenNumSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 14),
    _CfprApFabricVnetEpSyncEpGenNumSync_Type()
)
cfprApFabricVnetEpSyncEpGenNumSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpGenNumSync.setStatus("current")
_CfprApFabricVnetEpSyncEpId_Type = Gauge32
_CfprApFabricVnetEpSyncEpId_Object = MibTableColumn
cfprApFabricVnetEpSyncEpId = _CfprApFabricVnetEpSyncEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 15),
    _CfprApFabricVnetEpSyncEpId_Type()
)
cfprApFabricVnetEpSyncEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpId.setStatus("current")
_CfprApFabricVnetEpSyncEpIsChangedObjectUpdate_Type = TruthValue
_CfprApFabricVnetEpSyncEpIsChangedObjectUpdate_Object = MibTableColumn
cfprApFabricVnetEpSyncEpIsChangedObjectUpdate = _CfprApFabricVnetEpSyncEpIsChangedObjectUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 122, 1, 16),
    _CfprApFabricVnetEpSyncEpIsChangedObjectUpdate_Type()
)
cfprApFabricVnetEpSyncEpIsChangedObjectUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpIsChangedObjectUpdate.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTable_Object = MibTable
cfprApFabricVnetEpSyncEpFsmTable = _CfprApFabricVnetEpSyncEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123)
)
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTable.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmEntry_Object = MibTableRow
cfprApFabricVnetEpSyncEpFsmEntry = _CfprApFabricVnetEpSyncEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1)
)
cfprApFabricVnetEpSyncEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVnetEpSyncEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmEntry.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVnetEpSyncEpFsmInstanceId_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmInstanceId = _CfprApFabricVnetEpSyncEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 1),
    _CfprApFabricVnetEpSyncEpFsmInstanceId_Type()
)
cfprApFabricVnetEpSyncEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmInstanceId.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmDn_Type = CfprApManagedObjectDn
_CfprApFabricVnetEpSyncEpFsmDn_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmDn = _CfprApFabricVnetEpSyncEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 2),
    _CfprApFabricVnetEpSyncEpFsmDn_Type()
)
cfprApFabricVnetEpSyncEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmDn.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmRn_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmRn_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmRn = _CfprApFabricVnetEpSyncEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 3),
    _CfprApFabricVnetEpSyncEpFsmRn_Type()
)
cfprApFabricVnetEpSyncEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmRn.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmCompletionTime_Type = DateAndTime
_CfprApFabricVnetEpSyncEpFsmCompletionTime_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmCompletionTime = _CfprApFabricVnetEpSyncEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 4),
    _CfprApFabricVnetEpSyncEpFsmCompletionTime_Type()
)
cfprApFabricVnetEpSyncEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmCompletionTime.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmCurrentFsm_Type = CfprApFabricVnetEpSyncEpFsmCurrentFsm
_CfprApFabricVnetEpSyncEpFsmCurrentFsm_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmCurrentFsm = _CfprApFabricVnetEpSyncEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 5),
    _CfprApFabricVnetEpSyncEpFsmCurrentFsm_Type()
)
cfprApFabricVnetEpSyncEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmCurrentFsm.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmDescrData_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmDescrData_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmDescrData = _CfprApFabricVnetEpSyncEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 6),
    _CfprApFabricVnetEpSyncEpFsmDescrData_Type()
)
cfprApFabricVnetEpSyncEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmDescrData.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmFsmStatus_Type = CfprApFsmFsmStageStatus
_CfprApFabricVnetEpSyncEpFsmFsmStatus_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmFsmStatus = _CfprApFabricVnetEpSyncEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 7),
    _CfprApFabricVnetEpSyncEpFsmFsmStatus_Type()
)
cfprApFabricVnetEpSyncEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmFsmStatus.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmProgress_Type = Gauge32
_CfprApFabricVnetEpSyncEpFsmProgress_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmProgress = _CfprApFabricVnetEpSyncEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 8),
    _CfprApFabricVnetEpSyncEpFsmProgress_Type()
)
cfprApFabricVnetEpSyncEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmProgress.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmRmtErrCode_Type = Gauge32
_CfprApFabricVnetEpSyncEpFsmRmtErrCode_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmRmtErrCode = _CfprApFabricVnetEpSyncEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 9),
    _CfprApFabricVnetEpSyncEpFsmRmtErrCode_Type()
)
cfprApFabricVnetEpSyncEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmRmtErrCode.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmRmtErrDescr_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmRmtErrDescr = _CfprApFabricVnetEpSyncEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 10),
    _CfprApFabricVnetEpSyncEpFsmRmtErrDescr_Type()
)
cfprApFabricVnetEpSyncEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmRmtErrDescr.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmRmtRslt_Type = CfprApConditionRemoteInvRslt
_CfprApFabricVnetEpSyncEpFsmRmtRslt_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmRmtRslt = _CfprApFabricVnetEpSyncEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 123, 1, 11),
    _CfprApFabricVnetEpSyncEpFsmRmtRslt_Type()
)
cfprApFabricVnetEpSyncEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmRmtRslt.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageTable_Object = MibTable
cfprApFabricVnetEpSyncEpFsmStageTable = _CfprApFabricVnetEpSyncEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124)
)
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageTable.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageEntry_Object = MibTableRow
cfprApFabricVnetEpSyncEpFsmStageEntry = _CfprApFabricVnetEpSyncEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1)
)
cfprApFabricVnetEpSyncEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVnetEpSyncEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageEntry.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVnetEpSyncEpFsmStageInstanceId_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageInstanceId = _CfprApFabricVnetEpSyncEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 1),
    _CfprApFabricVnetEpSyncEpFsmStageInstanceId_Type()
)
cfprApFabricVnetEpSyncEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageInstanceId.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageDn_Type = CfprApManagedObjectDn
_CfprApFabricVnetEpSyncEpFsmStageDn_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageDn = _CfprApFabricVnetEpSyncEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 2),
    _CfprApFabricVnetEpSyncEpFsmStageDn_Type()
)
cfprApFabricVnetEpSyncEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageDn.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageRn_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmStageRn_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageRn = _CfprApFabricVnetEpSyncEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 3),
    _CfprApFabricVnetEpSyncEpFsmStageRn_Type()
)
cfprApFabricVnetEpSyncEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageRn.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageDescrData_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmStageDescrData_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageDescrData = _CfprApFabricVnetEpSyncEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 4),
    _CfprApFabricVnetEpSyncEpFsmStageDescrData_Type()
)
cfprApFabricVnetEpSyncEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageDescrData.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprApFabricVnetEpSyncEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageLastUpdateTime = _CfprApFabricVnetEpSyncEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 5),
    _CfprApFabricVnetEpSyncEpFsmStageLastUpdateTime_Type()
)
cfprApFabricVnetEpSyncEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageLastUpdateTime.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageName_Type = CfprApFabricVnetEpSyncEpFsmStageName
_CfprApFabricVnetEpSyncEpFsmStageName_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageName = _CfprApFabricVnetEpSyncEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 6),
    _CfprApFabricVnetEpSyncEpFsmStageName_Type()
)
cfprApFabricVnetEpSyncEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageName.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageOrder_Type = Gauge32
_CfprApFabricVnetEpSyncEpFsmStageOrder_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageOrder = _CfprApFabricVnetEpSyncEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 7),
    _CfprApFabricVnetEpSyncEpFsmStageOrder_Type()
)
cfprApFabricVnetEpSyncEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageOrder.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageRetry_Type = Gauge32
_CfprApFabricVnetEpSyncEpFsmStageRetry_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageRetry = _CfprApFabricVnetEpSyncEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 8),
    _CfprApFabricVnetEpSyncEpFsmStageRetry_Type()
)
cfprApFabricVnetEpSyncEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageRetry.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmStageStageStatus_Type = CfprApFsmFsmStageStatus
_CfprApFabricVnetEpSyncEpFsmStageStageStatus_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmStageStageStatus = _CfprApFabricVnetEpSyncEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 124, 1, 9),
    _CfprApFabricVnetEpSyncEpFsmStageStageStatus_Type()
)
cfprApFabricVnetEpSyncEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmStageStageStatus.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskTable_Object = MibTable
cfprApFabricVnetEpSyncEpFsmTaskTable = _CfprApFabricVnetEpSyncEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125)
)
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskTable.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskEntry_Object = MibTableRow
cfprApFabricVnetEpSyncEpFsmTaskEntry = _CfprApFabricVnetEpSyncEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125, 1)
)
cfprApFabricVnetEpSyncEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVnetEpSyncEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskEntry.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVnetEpSyncEpFsmTaskInstanceId_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmTaskInstanceId = _CfprApFabricVnetEpSyncEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125, 1, 1),
    _CfprApFabricVnetEpSyncEpFsmTaskInstanceId_Type()
)
cfprApFabricVnetEpSyncEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskInstanceId.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskDn_Type = CfprApManagedObjectDn
_CfprApFabricVnetEpSyncEpFsmTaskDn_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmTaskDn = _CfprApFabricVnetEpSyncEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125, 1, 2),
    _CfprApFabricVnetEpSyncEpFsmTaskDn_Type()
)
cfprApFabricVnetEpSyncEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskDn.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskRn_Type = SnmpAdminString
_CfprApFabricVnetEpSyncEpFsmTaskRn_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmTaskRn = _CfprApFabricVnetEpSyncEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125, 1, 3),
    _CfprApFabricVnetEpSyncEpFsmTaskRn_Type()
)
cfprApFabricVnetEpSyncEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskRn.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskCompletion_Type = CfprApFsmCompletion
_CfprApFabricVnetEpSyncEpFsmTaskCompletion_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmTaskCompletion = _CfprApFabricVnetEpSyncEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125, 1, 4),
    _CfprApFabricVnetEpSyncEpFsmTaskCompletion_Type()
)
cfprApFabricVnetEpSyncEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskCompletion.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskFlags_Type = CfprApFsmFlags
_CfprApFabricVnetEpSyncEpFsmTaskFlags_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmTaskFlags = _CfprApFabricVnetEpSyncEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125, 1, 5),
    _CfprApFabricVnetEpSyncEpFsmTaskFlags_Type()
)
cfprApFabricVnetEpSyncEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskFlags.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskItem_Type = CfprApFabricVnetEpSyncEpFsmTaskItem
_CfprApFabricVnetEpSyncEpFsmTaskItem_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmTaskItem = _CfprApFabricVnetEpSyncEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125, 1, 6),
    _CfprApFabricVnetEpSyncEpFsmTaskItem_Type()
)
cfprApFabricVnetEpSyncEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskItem.setStatus("current")
_CfprApFabricVnetEpSyncEpFsmTaskSeqId_Type = Gauge32
_CfprApFabricVnetEpSyncEpFsmTaskSeqId_Object = MibTableColumn
cfprApFabricVnetEpSyncEpFsmTaskSeqId = _CfprApFabricVnetEpSyncEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 125, 1, 7),
    _CfprApFabricVnetEpSyncEpFsmTaskSeqId_Type()
)
cfprApFabricVnetEpSyncEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVnetEpSyncEpFsmTaskSeqId.setStatus("current")
_CfprApFabricVsanTable_Object = MibTable
cfprApFabricVsanTable = _CfprApFabricVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126)
)
if mibBuilder.loadTexts:
    cfprApFabricVsanTable.setStatus("current")
_CfprApFabricVsanEntry_Object = MibTableRow
cfprApFabricVsanEntry = _CfprApFabricVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1)
)
cfprApFabricVsanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVsanEntry.setStatus("current")
_CfprApFabricVsanInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVsanInstanceId_Object = MibTableColumn
cfprApFabricVsanInstanceId = _CfprApFabricVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 1),
    _CfprApFabricVsanInstanceId_Type()
)
cfprApFabricVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVsanInstanceId.setStatus("current")
_CfprApFabricVsanDn_Type = CfprApManagedObjectDn
_CfprApFabricVsanDn_Object = MibTableColumn
cfprApFabricVsanDn = _CfprApFabricVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 2),
    _CfprApFabricVsanDn_Type()
)
cfprApFabricVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanDn.setStatus("current")
_CfprApFabricVsanRn_Type = SnmpAdminString
_CfprApFabricVsanRn_Object = MibTableColumn
cfprApFabricVsanRn = _CfprApFabricVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 3),
    _CfprApFabricVsanRn_Type()
)
cfprApFabricVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanRn.setStatus("current")
_CfprApFabricVsanDefaultZoning_Type = CfprApFabricDefaultZoningState
_CfprApFabricVsanDefaultZoning_Object = MibTableColumn
cfprApFabricVsanDefaultZoning = _CfprApFabricVsanDefaultZoning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 4),
    _CfprApFabricVsanDefaultZoning_Type()
)
cfprApFabricVsanDefaultZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanDefaultZoning.setStatus("current")
_CfprApFabricVsanEpDn_Type = SnmpAdminString
_CfprApFabricVsanEpDn_Object = MibTableColumn
cfprApFabricVsanEpDn = _CfprApFabricVsanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 5),
    _CfprApFabricVsanEpDn_Type()
)
cfprApFabricVsanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpDn.setStatus("current")
_CfprApFabricVsanFcZoneSharingMode_Type = CfprApFabricFcZoneSharingMode
_CfprApFabricVsanFcZoneSharingMode_Object = MibTableColumn
cfprApFabricVsanFcZoneSharingMode = _CfprApFabricVsanFcZoneSharingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 6),
    _CfprApFabricVsanFcZoneSharingMode_Type()
)
cfprApFabricVsanFcZoneSharingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanFcZoneSharingMode.setStatus("current")
_CfprApFabricVsanFcoeVlan_Type = Gauge32
_CfprApFabricVsanFcoeVlan_Object = MibTableColumn
cfprApFabricVsanFcoeVlan = _CfprApFabricVsanFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 7),
    _CfprApFabricVsanFcoeVlan_Type()
)
cfprApFabricVsanFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanFcoeVlan.setStatus("current")
_CfprApFabricVsanFltAggr_Type = Unsigned64
_CfprApFabricVsanFltAggr_Object = MibTableColumn
cfprApFabricVsanFltAggr = _CfprApFabricVsanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 8),
    _CfprApFabricVsanFltAggr_Type()
)
cfprApFabricVsanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanFltAggr.setStatus("current")
_CfprApFabricVsanGlobal_Type = Unsigned64
_CfprApFabricVsanGlobal_Object = MibTableColumn
cfprApFabricVsanGlobal = _CfprApFabricVsanGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 9),
    _CfprApFabricVsanGlobal_Type()
)
cfprApFabricVsanGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanGlobal.setStatus("current")
_CfprApFabricVsanId_Type = Gauge32
_CfprApFabricVsanId_Object = MibTableColumn
cfprApFabricVsanId = _CfprApFabricVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 10),
    _CfprApFabricVsanId_Type()
)
cfprApFabricVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanId.setStatus("current")
_CfprApFabricVsanIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApFabricVsanIfRole_Object = MibTableColumn
cfprApFabricVsanIfRole = _CfprApFabricVsanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 11),
    _CfprApFabricVsanIfRole_Type()
)
cfprApFabricVsanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanIfRole.setStatus("current")
_CfprApFabricVsanIfType_Type = CfprApNetworkVnetEpIfType
_CfprApFabricVsanIfType_Object = MibTableColumn
cfprApFabricVsanIfType = _CfprApFabricVsanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 12),
    _CfprApFabricVsanIfType_Type()
)
cfprApFabricVsanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanIfType.setStatus("current")
_CfprApFabricVsanLocal_Type = Unsigned64
_CfprApFabricVsanLocal_Object = MibTableColumn
cfprApFabricVsanLocal = _CfprApFabricVsanLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 13),
    _CfprApFabricVsanLocal_Type()
)
cfprApFabricVsanLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanLocal.setStatus("current")
_CfprApFabricVsanLocale_Type = CfprApFabricVnetEpLocale
_CfprApFabricVsanLocale_Object = MibTableColumn
cfprApFabricVsanLocale = _CfprApFabricVsanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 14),
    _CfprApFabricVsanLocale_Type()
)
cfprApFabricVsanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanLocale.setStatus("current")
_CfprApFabricVsanName_Type = SnmpAdminString
_CfprApFabricVsanName_Object = MibTableColumn
cfprApFabricVsanName = _CfprApFabricVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 15),
    _CfprApFabricVsanName_Type()
)
cfprApFabricVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanName.setStatus("current")
_CfprApFabricVsanOperState_Type = CfprApFabricVsanOperState
_CfprApFabricVsanOperState_Object = MibTableColumn
cfprApFabricVsanOperState = _CfprApFabricVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 16),
    _CfprApFabricVsanOperState_Type()
)
cfprApFabricVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanOperState.setStatus("current")
_CfprApFabricVsanPeerDn_Type = SnmpAdminString
_CfprApFabricVsanPeerDn_Object = MibTableColumn
cfprApFabricVsanPeerDn = _CfprApFabricVsanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 17),
    _CfprApFabricVsanPeerDn_Type()
)
cfprApFabricVsanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanPeerDn.setStatus("current")
_CfprApFabricVsanPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApFabricVsanPolicyOwner_Object = MibTableColumn
cfprApFabricVsanPolicyOwner = _CfprApFabricVsanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 18),
    _CfprApFabricVsanPolicyOwner_Type()
)
cfprApFabricVsanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanPolicyOwner.setStatus("current")
_CfprApFabricVsanSwitchId_Type = CfprApFabricVsanSwitchId
_CfprApFabricVsanSwitchId_Object = MibTableColumn
cfprApFabricVsanSwitchId = _CfprApFabricVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 19),
    _CfprApFabricVsanSwitchId_Type()
)
cfprApFabricVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanSwitchId.setStatus("current")
_CfprApFabricVsanTransport_Type = CfprApFabricAVsanTransport
_CfprApFabricVsanTransport_Object = MibTableColumn
cfprApFabricVsanTransport = _CfprApFabricVsanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 20),
    _CfprApFabricVsanTransport_Type()
)
cfprApFabricVsanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanTransport.setStatus("current")
_CfprApFabricVsanType_Type = CfprApFabricAVsanType
_CfprApFabricVsanType_Object = MibTableColumn
cfprApFabricVsanType = _CfprApFabricVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 21),
    _CfprApFabricVsanType_Type()
)
cfprApFabricVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanType.setStatus("current")
_CfprApFabricVsanZoningState_Type = CfprApFabricZoningState
_CfprApFabricVsanZoningState_Object = MibTableColumn
cfprApFabricVsanZoningState = _CfprApFabricVsanZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 126, 1, 22),
    _CfprApFabricVsanZoningState_Type()
)
cfprApFabricVsanZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanZoningState.setStatus("current")
_CfprApFabricVsanEpTable_Object = MibTable
cfprApFabricVsanEpTable = _CfprApFabricVsanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127)
)
if mibBuilder.loadTexts:
    cfprApFabricVsanEpTable.setStatus("current")
_CfprApFabricVsanEpEntry_Object = MibTableRow
cfprApFabricVsanEpEntry = _CfprApFabricVsanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1)
)
cfprApFabricVsanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVsanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVsanEpEntry.setStatus("current")
_CfprApFabricVsanEpInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVsanEpInstanceId_Object = MibTableColumn
cfprApFabricVsanEpInstanceId = _CfprApFabricVsanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 1),
    _CfprApFabricVsanEpInstanceId_Type()
)
cfprApFabricVsanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpInstanceId.setStatus("current")
_CfprApFabricVsanEpDnData_Type = CfprApManagedObjectDn
_CfprApFabricVsanEpDnData_Object = MibTableColumn
cfprApFabricVsanEpDnData = _CfprApFabricVsanEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 2),
    _CfprApFabricVsanEpDnData_Type()
)
cfprApFabricVsanEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpDnData.setStatus("current")
_CfprApFabricVsanEpRn_Type = SnmpAdminString
_CfprApFabricVsanEpRn_Object = MibTableColumn
cfprApFabricVsanEpRn = _CfprApFabricVsanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 3),
    _CfprApFabricVsanEpRn_Type()
)
cfprApFabricVsanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpRn.setStatus("current")
_CfprApFabricVsanEpEpDn_Type = SnmpAdminString
_CfprApFabricVsanEpEpDn_Object = MibTableColumn
cfprApFabricVsanEpEpDn = _CfprApFabricVsanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 4),
    _CfprApFabricVsanEpEpDn_Type()
)
cfprApFabricVsanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpEpDn.setStatus("current")
_CfprApFabricVsanEpFcoeVlan_Type = Gauge32
_CfprApFabricVsanEpFcoeVlan_Object = MibTableColumn
cfprApFabricVsanEpFcoeVlan = _CfprApFabricVsanEpFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 5),
    _CfprApFabricVsanEpFcoeVlan_Type()
)
cfprApFabricVsanEpFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpFcoeVlan.setStatus("current")
_CfprApFabricVsanEpId_Type = Gauge32
_CfprApFabricVsanEpId_Object = MibTableColumn
cfprApFabricVsanEpId = _CfprApFabricVsanEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 6),
    _CfprApFabricVsanEpId_Type()
)
cfprApFabricVsanEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpId.setStatus("current")
_CfprApFabricVsanEpIfRole_Type = CfprApFabricVnetEpIfRole
_CfprApFabricVsanEpIfRole_Object = MibTableColumn
cfprApFabricVsanEpIfRole = _CfprApFabricVsanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 7),
    _CfprApFabricVsanEpIfRole_Type()
)
cfprApFabricVsanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpIfRole.setStatus("current")
_CfprApFabricVsanEpIfType_Type = CfprApNetworkVnetEpIfType
_CfprApFabricVsanEpIfType_Object = MibTableColumn
cfprApFabricVsanEpIfType = _CfprApFabricVsanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 8),
    _CfprApFabricVsanEpIfType_Type()
)
cfprApFabricVsanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpIfType.setStatus("current")
_CfprApFabricVsanEpLocale_Type = CfprApFabricVnetEpLocale
_CfprApFabricVsanEpLocale_Object = MibTableColumn
cfprApFabricVsanEpLocale = _CfprApFabricVsanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 9),
    _CfprApFabricVsanEpLocale_Type()
)
cfprApFabricVsanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpLocale.setStatus("current")
_CfprApFabricVsanEpName_Type = SnmpAdminString
_CfprApFabricVsanEpName_Object = MibTableColumn
cfprApFabricVsanEpName = _CfprApFabricVsanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 10),
    _CfprApFabricVsanEpName_Type()
)
cfprApFabricVsanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpName.setStatus("current")
_CfprApFabricVsanEpOperState_Type = CfprApFabricVsanOperState
_CfprApFabricVsanEpOperState_Object = MibTableColumn
cfprApFabricVsanEpOperState = _CfprApFabricVsanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 11),
    _CfprApFabricVsanEpOperState_Type()
)
cfprApFabricVsanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpOperState.setStatus("current")
_CfprApFabricVsanEpPeerDn_Type = SnmpAdminString
_CfprApFabricVsanEpPeerDn_Object = MibTableColumn
cfprApFabricVsanEpPeerDn = _CfprApFabricVsanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 12),
    _CfprApFabricVsanEpPeerDn_Type()
)
cfprApFabricVsanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpPeerDn.setStatus("current")
_CfprApFabricVsanEpPolicyOwner_Type = CfprApFabricVnetEpPolicyOwner
_CfprApFabricVsanEpPolicyOwner_Object = MibTableColumn
cfprApFabricVsanEpPolicyOwner = _CfprApFabricVsanEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 13),
    _CfprApFabricVsanEpPolicyOwner_Type()
)
cfprApFabricVsanEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpPolicyOwner.setStatus("current")
_CfprApFabricVsanEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApFabricVsanEpSwitchId_Object = MibTableColumn
cfprApFabricVsanEpSwitchId = _CfprApFabricVsanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 14),
    _CfprApFabricVsanEpSwitchId_Type()
)
cfprApFabricVsanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpSwitchId.setStatus("current")
_CfprApFabricVsanEpTransport_Type = CfprApFabricAVsanTransport
_CfprApFabricVsanEpTransport_Object = MibTableColumn
cfprApFabricVsanEpTransport = _CfprApFabricVsanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 15),
    _CfprApFabricVsanEpTransport_Type()
)
cfprApFabricVsanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpTransport.setStatus("current")
_CfprApFabricVsanEpType_Type = CfprApFabricAVsanType
_CfprApFabricVsanEpType_Object = MibTableColumn
cfprApFabricVsanEpType = _CfprApFabricVsanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 16),
    _CfprApFabricVsanEpType_Type()
)
cfprApFabricVsanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpType.setStatus("current")
_CfprApFabricVsanEpZoningState_Type = CfprApFabricZoningState
_CfprApFabricVsanEpZoningState_Object = MibTableColumn
cfprApFabricVsanEpZoningState = _CfprApFabricVsanEpZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 127, 1, 17),
    _CfprApFabricVsanEpZoningState_Type()
)
cfprApFabricVsanEpZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanEpZoningState.setStatus("current")
_CfprApFabricVsanMembershipTable_Object = MibTable
cfprApFabricVsanMembershipTable = _CfprApFabricVsanMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128)
)
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipTable.setStatus("current")
_CfprApFabricVsanMembershipEntry_Object = MibTableRow
cfprApFabricVsanMembershipEntry = _CfprApFabricVsanMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128, 1)
)
cfprApFabricVsanMembershipEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricVsanMembershipInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipEntry.setStatus("current")
_CfprApFabricVsanMembershipInstanceId_Type = CfprApManagedObjectId
_CfprApFabricVsanMembershipInstanceId_Object = MibTableColumn
cfprApFabricVsanMembershipInstanceId = _CfprApFabricVsanMembershipInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128, 1, 1),
    _CfprApFabricVsanMembershipInstanceId_Type()
)
cfprApFabricVsanMembershipInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipInstanceId.setStatus("current")
_CfprApFabricVsanMembershipDn_Type = CfprApManagedObjectDn
_CfprApFabricVsanMembershipDn_Object = MibTableColumn
cfprApFabricVsanMembershipDn = _CfprApFabricVsanMembershipDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128, 1, 2),
    _CfprApFabricVsanMembershipDn_Type()
)
cfprApFabricVsanMembershipDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipDn.setStatus("current")
_CfprApFabricVsanMembershipRn_Type = SnmpAdminString
_CfprApFabricVsanMembershipRn_Object = MibTableColumn
cfprApFabricVsanMembershipRn = _CfprApFabricVsanMembershipRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128, 1, 3),
    _CfprApFabricVsanMembershipRn_Type()
)
cfprApFabricVsanMembershipRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipRn.setStatus("current")
_CfprApFabricVsanMembershipMemberStatus_Type = CfprApFabricMemberStatus
_CfprApFabricVsanMembershipMemberStatus_Object = MibTableColumn
cfprApFabricVsanMembershipMemberStatus = _CfprApFabricVsanMembershipMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128, 1, 4),
    _CfprApFabricVsanMembershipMemberStatus_Type()
)
cfprApFabricVsanMembershipMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipMemberStatus.setStatus("current")
_CfprApFabricVsanMembershipParentAdminState_Type = CfprApFabricAdminState
_CfprApFabricVsanMembershipParentAdminState_Object = MibTableColumn
cfprApFabricVsanMembershipParentAdminState = _CfprApFabricVsanMembershipParentAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128, 1, 5),
    _CfprApFabricVsanMembershipParentAdminState_Type()
)
cfprApFabricVsanMembershipParentAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipParentAdminState.setStatus("current")
_CfprApFabricVsanMembershipStateQual_Type = SnmpAdminString
_CfprApFabricVsanMembershipStateQual_Object = MibTableColumn
cfprApFabricVsanMembershipStateQual = _CfprApFabricVsanMembershipStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128, 1, 6),
    _CfprApFabricVsanMembershipStateQual_Type()
)
cfprApFabricVsanMembershipStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipStateQual.setStatus("current")
_CfprApFabricVsanMembershipVsanId_Type = Gauge32
_CfprApFabricVsanMembershipVsanId_Object = MibTableColumn
cfprApFabricVsanMembershipVsanId = _CfprApFabricVsanMembershipVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 128, 1, 7),
    _CfprApFabricVsanMembershipVsanId_Type()
)
cfprApFabricVsanMembershipVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricVsanMembershipVsanId.setStatus("current")
_CfprApFabricZoneIdUniverseTable_Object = MibTable
cfprApFabricZoneIdUniverseTable = _CfprApFabricZoneIdUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 129)
)
if mibBuilder.loadTexts:
    cfprApFabricZoneIdUniverseTable.setStatus("current")
_CfprApFabricZoneIdUniverseEntry_Object = MibTableRow
cfprApFabricZoneIdUniverseEntry = _CfprApFabricZoneIdUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 129, 1)
)
cfprApFabricZoneIdUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-FABRIC-MIB", "cfprApFabricZoneIdUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApFabricZoneIdUniverseEntry.setStatus("current")
_CfprApFabricZoneIdUniverseInstanceId_Type = CfprApManagedObjectId
_CfprApFabricZoneIdUniverseInstanceId_Object = MibTableColumn
cfprApFabricZoneIdUniverseInstanceId = _CfprApFabricZoneIdUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 129, 1, 1),
    _CfprApFabricZoneIdUniverseInstanceId_Type()
)
cfprApFabricZoneIdUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApFabricZoneIdUniverseInstanceId.setStatus("current")
_CfprApFabricZoneIdUniverseDn_Type = CfprApManagedObjectDn
_CfprApFabricZoneIdUniverseDn_Object = MibTableColumn
cfprApFabricZoneIdUniverseDn = _CfprApFabricZoneIdUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 129, 1, 2),
    _CfprApFabricZoneIdUniverseDn_Type()
)
cfprApFabricZoneIdUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricZoneIdUniverseDn.setStatus("current")
_CfprApFabricZoneIdUniverseRn_Type = SnmpAdminString
_CfprApFabricZoneIdUniverseRn_Object = MibTableColumn
cfprApFabricZoneIdUniverseRn = _CfprApFabricZoneIdUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 26, 129, 1, 3),
    _CfprApFabricZoneIdUniverseRn_Type()
)
cfprApFabricZoneIdUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApFabricZoneIdUniverseRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-FABRIC-MIB",
    **{"cfprApFabricObjects": cfprApFabricObjects,
       "cfprApFabricBHVlanTable": cfprApFabricBHVlanTable,
       "cfprApFabricBHVlanEntry": cfprApFabricBHVlanEntry,
       "cfprApFabricBHVlanInstanceId": cfprApFabricBHVlanInstanceId,
       "cfprApFabricBHVlanDn": cfprApFabricBHVlanDn,
       "cfprApFabricBHVlanRn": cfprApFabricBHVlanRn,
       "cfprApFabricBHVlanAssocPrimaryVlanState": cfprApFabricBHVlanAssocPrimaryVlanState,
       "cfprApFabricBHVlanAssocPrimaryVlanSwitchId": cfprApFabricBHVlanAssocPrimaryVlanSwitchId,
       "cfprApFabricBHVlanEpDn": cfprApFabricBHVlanEpDn,
       "cfprApFabricBHVlanId": cfprApFabricBHVlanId,
       "cfprApFabricBHVlanIfRole": cfprApFabricBHVlanIfRole,
       "cfprApFabricBHVlanIfType": cfprApFabricBHVlanIfType,
       "cfprApFabricBHVlanLocale": cfprApFabricBHVlanLocale,
       "cfprApFabricBHVlanName": cfprApFabricBHVlanName,
       "cfprApFabricBHVlanOperState": cfprApFabricBHVlanOperState,
       "cfprApFabricBHVlanOverlapStateForA": cfprApFabricBHVlanOverlapStateForA,
       "cfprApFabricBHVlanOverlapStateForB": cfprApFabricBHVlanOverlapStateForB,
       "cfprApFabricBHVlanPeerDn": cfprApFabricBHVlanPeerDn,
       "cfprApFabricBHVlanPolicyOwner": cfprApFabricBHVlanPolicyOwner,
       "cfprApFabricBHVlanPubNwDn": cfprApFabricBHVlanPubNwDn,
       "cfprApFabricBHVlanPubNwId": cfprApFabricBHVlanPubNwId,
       "cfprApFabricBHVlanPubNwName": cfprApFabricBHVlanPubNwName,
       "cfprApFabricBHVlanSharing": cfprApFabricBHVlanSharing,
       "cfprApFabricBHVlanSwitchId": cfprApFabricBHVlanSwitchId,
       "cfprApFabricBHVlanTransport": cfprApFabricBHVlanTransport,
       "cfprApFabricBHVlanType": cfprApFabricBHVlanType,
       "cfprApFabricBreakoutTable": cfprApFabricBreakoutTable,
       "cfprApFabricBreakoutEntry": cfprApFabricBreakoutEntry,
       "cfprApFabricBreakoutInstanceId": cfprApFabricBreakoutInstanceId,
       "cfprApFabricBreakoutDn": cfprApFabricBreakoutDn,
       "cfprApFabricBreakoutRn": cfprApFabricBreakoutRn,
       "cfprApFabricBreakoutBreakoutType": cfprApFabricBreakoutBreakoutType,
       "cfprApFabricBreakoutPortId": cfprApFabricBreakoutPortId,
       "cfprApFabricBreakoutSlotId": cfprApFabricBreakoutSlotId,
       "cfprApFabricCablingSwTable": cfprApFabricCablingSwTable,
       "cfprApFabricCablingSwEntry": cfprApFabricCablingSwEntry,
       "cfprApFabricCablingSwInstanceId": cfprApFabricCablingSwInstanceId,
       "cfprApFabricCablingSwDn": cfprApFabricCablingSwDn,
       "cfprApFabricCablingSwRn": cfprApFabricCablingSwRn,
       "cfprApFabricCablingSwId": cfprApFabricCablingSwId,
       "cfprApFabricCablingSwLocale": cfprApFabricCablingSwLocale,
       "cfprApFabricCablingSwName": cfprApFabricCablingSwName,
       "cfprApFabricCablingSwTransport": cfprApFabricCablingSwTransport,
       "cfprApFabricCablingSwType": cfprApFabricCablingSwType,
       "cfprApFabricCdpLinkPolicyTable": cfprApFabricCdpLinkPolicyTable,
       "cfprApFabricCdpLinkPolicyEntry": cfprApFabricCdpLinkPolicyEntry,
       "cfprApFabricCdpLinkPolicyInstanceId": cfprApFabricCdpLinkPolicyInstanceId,
       "cfprApFabricCdpLinkPolicyDn": cfprApFabricCdpLinkPolicyDn,
       "cfprApFabricCdpLinkPolicyRn": cfprApFabricCdpLinkPolicyRn,
       "cfprApFabricCdpLinkPolicyAdminState": cfprApFabricCdpLinkPolicyAdminState,
       "cfprApFabricCdpLinkPolicyDescr": cfprApFabricCdpLinkPolicyDescr,
       "cfprApFabricCdpLinkPolicyIntId": cfprApFabricCdpLinkPolicyIntId,
       "cfprApFabricCdpLinkPolicyName": cfprApFabricCdpLinkPolicyName,
       "cfprApFabricCdpLinkPolicyPolicyLevel": cfprApFabricCdpLinkPolicyPolicyLevel,
       "cfprApFabricCdpLinkPolicyPolicyOwner": cfprApFabricCdpLinkPolicyPolicyOwner,
       "cfprApFabricCdpLinkPolicyProtocol": cfprApFabricCdpLinkPolicyProtocol,
       "cfprApFabricCdpLinkPolicyType": cfprApFabricCdpLinkPolicyType,
       "cfprApFabricChangedObjectRefTable": cfprApFabricChangedObjectRefTable,
       "cfprApFabricChangedObjectRefEntry": cfprApFabricChangedObjectRefEntry,
       "cfprApFabricChangedObjectRefInstanceId": cfprApFabricChangedObjectRefInstanceId,
       "cfprApFabricChangedObjectRefDn": cfprApFabricChangedObjectRefDn,
       "cfprApFabricChangedObjectRefRn": cfprApFabricChangedObjectRefRn,
       "cfprApFabricChangedObjectRefCentraleVnetEpDn": cfprApFabricChangedObjectRefCentraleVnetEpDn,
       "cfprApFabricChangedObjectRefId": cfprApFabricChangedObjectRefId,
       "cfprApFabricChangedObjectRefOldCentraleVnetEpDn": cfprApFabricChangedObjectRefOldCentraleVnetEpDn,
       "cfprApFabricChangedObjectRefRefObjStatus": cfprApFabricChangedObjectRefRefObjStatus,
       "cfprApFabricChangedObjectRefUcsmVnetEpDn": cfprApFabricChangedObjectRefUcsmVnetEpDn,
       "cfprApFabricChassisEpTable": cfprApFabricChassisEpTable,
       "cfprApFabricChassisEpEntry": cfprApFabricChassisEpEntry,
       "cfprApFabricChassisEpInstanceId": cfprApFabricChassisEpInstanceId,
       "cfprApFabricChassisEpDn": cfprApFabricChassisEpDn,
       "cfprApFabricChassisEpRn": cfprApFabricChassisEpRn,
       "cfprApFabricChassisEpAdminState": cfprApFabricChassisEpAdminState,
       "cfprApFabricChassisEpAggrPortId": cfprApFabricChassisEpAggrPortId,
       "cfprApFabricChassisEpChassisDn": cfprApFabricChassisEpChassisDn,
       "cfprApFabricChassisEpChassisId": cfprApFabricChassisEpChassisId,
       "cfprApFabricChassisEpEpDn": cfprApFabricChassisEpEpDn,
       "cfprApFabricChassisEpFltAggr": cfprApFabricChassisEpFltAggr,
       "cfprApFabricChassisEpIfRole": cfprApFabricChassisEpIfRole,
       "cfprApFabricChassisEpIfType": cfprApFabricChassisEpIfType,
       "cfprApFabricChassisEpLicGP": cfprApFabricChassisEpLicGP,
       "cfprApFabricChassisEpLicState": cfprApFabricChassisEpLicState,
       "cfprApFabricChassisEpLocale": cfprApFabricChassisEpLocale,
       "cfprApFabricChassisEpModel": cfprApFabricChassisEpModel,
       "cfprApFabricChassisEpName": cfprApFabricChassisEpName,
       "cfprApFabricChassisEpOperState": cfprApFabricChassisEpOperState,
       "cfprApFabricChassisEpOperStateReason": cfprApFabricChassisEpOperStateReason,
       "cfprApFabricChassisEpPeerAggrPortId": cfprApFabricChassisEpPeerAggrPortId,
       "cfprApFabricChassisEpPeerChassisId": cfprApFabricChassisEpPeerChassisId,
       "cfprApFabricChassisEpPeerDn": cfprApFabricChassisEpPeerDn,
       "cfprApFabricChassisEpPeerPortId": cfprApFabricChassisEpPeerPortId,
       "cfprApFabricChassisEpPeerSlotId": cfprApFabricChassisEpPeerSlotId,
       "cfprApFabricChassisEpPortId": cfprApFabricChassisEpPortId,
       "cfprApFabricChassisEpRevision": cfprApFabricChassisEpRevision,
       "cfprApFabricChassisEpSerial": cfprApFabricChassisEpSerial,
       "cfprApFabricChassisEpSlotId": cfprApFabricChassisEpSlotId,
       "cfprApFabricChassisEpSwitchId": cfprApFabricChassisEpSwitchId,
       "cfprApFabricChassisEpTransport": cfprApFabricChassisEpTransport,
       "cfprApFabricChassisEpType": cfprApFabricChassisEpType,
       "cfprApFabricChassisEpVendor": cfprApFabricChassisEpVendor,
       "cfprApFabricComputePhEpTable": cfprApFabricComputePhEpTable,
       "cfprApFabricComputePhEpEntry": cfprApFabricComputePhEpEntry,
       "cfprApFabricComputePhEpInstanceId": cfprApFabricComputePhEpInstanceId,
       "cfprApFabricComputePhEpDn": cfprApFabricComputePhEpDn,
       "cfprApFabricComputePhEpRn": cfprApFabricComputePhEpRn,
       "cfprApFabricComputePhEpAdminState": cfprApFabricComputePhEpAdminState,
       "cfprApFabricComputePhEpAggrPortId": cfprApFabricComputePhEpAggrPortId,
       "cfprApFabricComputePhEpBoardAggregationRole": cfprApFabricComputePhEpBoardAggregationRole,
       "cfprApFabricComputePhEpChassisId": cfprApFabricComputePhEpChassisId,
       "cfprApFabricComputePhEpCheckpointTrigTs": cfprApFabricComputePhEpCheckpointTrigTs,
       "cfprApFabricComputePhEpDeepCheckpointTrigTs": cfprApFabricComputePhEpDeepCheckpointTrigTs,
       "cfprApFabricComputePhEpDiscTrigTs": cfprApFabricComputePhEpDiscTrigTs,
       "cfprApFabricComputePhEpEpDn": cfprApFabricComputePhEpEpDn,
       "cfprApFabricComputePhEpEqType": cfprApFabricComputePhEpEqType,
       "cfprApFabricComputePhEpFltAggr": cfprApFabricComputePhEpFltAggr,
       "cfprApFabricComputePhEpIfRole": cfprApFabricComputePhEpIfRole,
       "cfprApFabricComputePhEpIfType": cfprApFabricComputePhEpIfType,
       "cfprApFabricComputePhEpLc": cfprApFabricComputePhEpLc,
       "cfprApFabricComputePhEpLicGP": cfprApFabricComputePhEpLicGP,
       "cfprApFabricComputePhEpLicState": cfprApFabricComputePhEpLicState,
       "cfprApFabricComputePhEpLocale": cfprApFabricComputePhEpLocale,
       "cfprApFabricComputePhEpModel": cfprApFabricComputePhEpModel,
       "cfprApFabricComputePhEpName": cfprApFabricComputePhEpName,
       "cfprApFabricComputePhEpOperState": cfprApFabricComputePhEpOperState,
       "cfprApFabricComputePhEpOperStateReason": cfprApFabricComputePhEpOperStateReason,
       "cfprApFabricComputePhEpPeerAggrPortId": cfprApFabricComputePhEpPeerAggrPortId,
       "cfprApFabricComputePhEpPeerChassisId": cfprApFabricComputePhEpPeerChassisId,
       "cfprApFabricComputePhEpPeerDn": cfprApFabricComputePhEpPeerDn,
       "cfprApFabricComputePhEpPeerPortId": cfprApFabricComputePhEpPeerPortId,
       "cfprApFabricComputePhEpPeerSlotId": cfprApFabricComputePhEpPeerSlotId,
       "cfprApFabricComputePhEpPortId": cfprApFabricComputePhEpPortId,
       "cfprApFabricComputePhEpProfileDn": cfprApFabricComputePhEpProfileDn,
       "cfprApFabricComputePhEpRevision": cfprApFabricComputePhEpRevision,
       "cfprApFabricComputePhEpSerial": cfprApFabricComputePhEpSerial,
       "cfprApFabricComputePhEpSlotId": cfprApFabricComputePhEpSlotId,
       "cfprApFabricComputePhEpSwitchId": cfprApFabricComputePhEpSwitchId,
       "cfprApFabricComputePhEpTransport": cfprApFabricComputePhEpTransport,
       "cfprApFabricComputePhEpType": cfprApFabricComputePhEpType,
       "cfprApFabricComputePhEpVendor": cfprApFabricComputePhEpVendor,
       "cfprApFabricComputeSlotEpTable": cfprApFabricComputeSlotEpTable,
       "cfprApFabricComputeSlotEpEntry": cfprApFabricComputeSlotEpEntry,
       "cfprApFabricComputeSlotEpInstanceId": cfprApFabricComputeSlotEpInstanceId,
       "cfprApFabricComputeSlotEpDn": cfprApFabricComputeSlotEpDn,
       "cfprApFabricComputeSlotEpRn": cfprApFabricComputeSlotEpRn,
       "cfprApFabricComputeSlotEpAdminState": cfprApFabricComputeSlotEpAdminState,
       "cfprApFabricComputeSlotEpAggrPortId": cfprApFabricComputeSlotEpAggrPortId,
       "cfprApFabricComputeSlotEpBoardAggregationRole": cfprApFabricComputeSlotEpBoardAggregationRole,
       "cfprApFabricComputeSlotEpChassisId": cfprApFabricComputeSlotEpChassisId,
       "cfprApFabricComputeSlotEpConnPath": cfprApFabricComputeSlotEpConnPath,
       "cfprApFabricComputeSlotEpConnStatus": cfprApFabricComputeSlotEpConnStatus,
       "cfprApFabricComputeSlotEpDiscovery": cfprApFabricComputeSlotEpDiscovery,
       "cfprApFabricComputeSlotEpEpDn": cfprApFabricComputeSlotEpEpDn,
       "cfprApFabricComputeSlotEpFactoryResetFlag": cfprApFabricComputeSlotEpFactoryResetFlag,
       "cfprApFabricComputeSlotEpFltAggr": cfprApFabricComputeSlotEpFltAggr,
       "cfprApFabricComputeSlotEpFruIdentTrigTs": cfprApFabricComputeSlotEpFruIdentTrigTs,
       "cfprApFabricComputeSlotEpIfRole": cfprApFabricComputeSlotEpIfRole,
       "cfprApFabricComputeSlotEpIfType": cfprApFabricComputeSlotEpIfType,
       "cfprApFabricComputeSlotEpLcTs": cfprApFabricComputeSlotEpLcTs,
       "cfprApFabricComputeSlotEpLicGP": cfprApFabricComputeSlotEpLicGP,
       "cfprApFabricComputeSlotEpLicState": cfprApFabricComputeSlotEpLicState,
       "cfprApFabricComputeSlotEpLocale": cfprApFabricComputeSlotEpLocale,
       "cfprApFabricComputeSlotEpManagingInst": cfprApFabricComputeSlotEpManagingInst,
       "cfprApFabricComputeSlotEpModel": cfprApFabricComputeSlotEpModel,
       "cfprApFabricComputeSlotEpName": cfprApFabricComputeSlotEpName,
       "cfprApFabricComputeSlotEpOperState": cfprApFabricComputeSlotEpOperState,
       "cfprApFabricComputeSlotEpOperStateReason": cfprApFabricComputeSlotEpOperStateReason,
       "cfprApFabricComputeSlotEpPeerAggrPortId": cfprApFabricComputeSlotEpPeerAggrPortId,
       "cfprApFabricComputeSlotEpPeerChassisId": cfprApFabricComputeSlotEpPeerChassisId,
       "cfprApFabricComputeSlotEpPeerDn": cfprApFabricComputeSlotEpPeerDn,
       "cfprApFabricComputeSlotEpPeerPortId": cfprApFabricComputeSlotEpPeerPortId,
       "cfprApFabricComputeSlotEpPeerSlotEpDn": cfprApFabricComputeSlotEpPeerSlotEpDn,
       "cfprApFabricComputeSlotEpPeerSlotId": cfprApFabricComputeSlotEpPeerSlotId,
       "cfprApFabricComputeSlotEpPortId": cfprApFabricComputeSlotEpPortId,
       "cfprApFabricComputeSlotEpPresence": cfprApFabricComputeSlotEpPresence,
       "cfprApFabricComputeSlotEpPresencePath": cfprApFabricComputeSlotEpPresencePath,
       "cfprApFabricComputeSlotEpRevision": cfprApFabricComputeSlotEpRevision,
       "cfprApFabricComputeSlotEpSerial": cfprApFabricComputeSlotEpSerial,
       "cfprApFabricComputeSlotEpSlotId": cfprApFabricComputeSlotEpSlotId,
       "cfprApFabricComputeSlotEpSwitchId": cfprApFabricComputeSlotEpSwitchId,
       "cfprApFabricComputeSlotEpTransport": cfprApFabricComputeSlotEpTransport,
       "cfprApFabricComputeSlotEpType": cfprApFabricComputeSlotEpType,
       "cfprApFabricComputeSlotEpVendor": cfprApFabricComputeSlotEpVendor,
       "cfprApFabricDceSrvTable": cfprApFabricDceSrvTable,
       "cfprApFabricDceSrvEntry": cfprApFabricDceSrvEntry,
       "cfprApFabricDceSrvInstanceId": cfprApFabricDceSrvInstanceId,
       "cfprApFabricDceSrvDn": cfprApFabricDceSrvDn,
       "cfprApFabricDceSrvRn": cfprApFabricDceSrvRn,
       "cfprApFabricDceSrvId": cfprApFabricDceSrvId,
       "cfprApFabricDceSrvLocale": cfprApFabricDceSrvLocale,
       "cfprApFabricDceSrvName": cfprApFabricDceSrvName,
       "cfprApFabricDceSrvTransport": cfprApFabricDceSrvTransport,
       "cfprApFabricDceSrvType": cfprApFabricDceSrvType,
       "cfprApFabricDceSwSrvTable": cfprApFabricDceSwSrvTable,
       "cfprApFabricDceSwSrvEntry": cfprApFabricDceSwSrvEntry,
       "cfprApFabricDceSwSrvInstanceId": cfprApFabricDceSwSrvInstanceId,
       "cfprApFabricDceSwSrvDn": cfprApFabricDceSwSrvDn,
       "cfprApFabricDceSwSrvRn": cfprApFabricDceSwSrvRn,
       "cfprApFabricDceSwSrvId": cfprApFabricDceSwSrvId,
       "cfprApFabricDceSwSrvLocale": cfprApFabricDceSwSrvLocale,
       "cfprApFabricDceSwSrvName": cfprApFabricDceSwSrvName,
       "cfprApFabricDceSwSrvTransport": cfprApFabricDceSwSrvTransport,
       "cfprApFabricDceSwSrvType": cfprApFabricDceSwSrvType,
       "cfprApFabricDceSwSrvEpTable": cfprApFabricDceSwSrvEpTable,
       "cfprApFabricDceSwSrvEpEntry": cfprApFabricDceSwSrvEpEntry,
       "cfprApFabricDceSwSrvEpInstanceId": cfprApFabricDceSwSrvEpInstanceId,
       "cfprApFabricDceSwSrvEpDn": cfprApFabricDceSwSrvEpDn,
       "cfprApFabricDceSwSrvEpRn": cfprApFabricDceSwSrvEpRn,
       "cfprApFabricDceSwSrvEpAdminState": cfprApFabricDceSwSrvEpAdminState,
       "cfprApFabricDceSwSrvEpAggrPortId": cfprApFabricDceSwSrvEpAggrPortId,
       "cfprApFabricDceSwSrvEpChassisId": cfprApFabricDceSwSrvEpChassisId,
       "cfprApFabricDceSwSrvEpEpDn": cfprApFabricDceSwSrvEpEpDn,
       "cfprApFabricDceSwSrvEpFltAggr": cfprApFabricDceSwSrvEpFltAggr,
       "cfprApFabricDceSwSrvEpIfRole": cfprApFabricDceSwSrvEpIfRole,
       "cfprApFabricDceSwSrvEpIfType": cfprApFabricDceSwSrvEpIfType,
       "cfprApFabricDceSwSrvEpLicGP": cfprApFabricDceSwSrvEpLicGP,
       "cfprApFabricDceSwSrvEpLicState": cfprApFabricDceSwSrvEpLicState,
       "cfprApFabricDceSwSrvEpLocale": cfprApFabricDceSwSrvEpLocale,
       "cfprApFabricDceSwSrvEpName": cfprApFabricDceSwSrvEpName,
       "cfprApFabricDceSwSrvEpOperState": cfprApFabricDceSwSrvEpOperState,
       "cfprApFabricDceSwSrvEpOperStateReason": cfprApFabricDceSwSrvEpOperStateReason,
       "cfprApFabricDceSwSrvEpPeerAggrPortId": cfprApFabricDceSwSrvEpPeerAggrPortId,
       "cfprApFabricDceSwSrvEpPeerChassisId": cfprApFabricDceSwSrvEpPeerChassisId,
       "cfprApFabricDceSwSrvEpPeerDn": cfprApFabricDceSwSrvEpPeerDn,
       "cfprApFabricDceSwSrvEpPeerPortId": cfprApFabricDceSwSrvEpPeerPortId,
       "cfprApFabricDceSwSrvEpPeerSlotId": cfprApFabricDceSwSrvEpPeerSlotId,
       "cfprApFabricDceSwSrvEpPortId": cfprApFabricDceSwSrvEpPortId,
       "cfprApFabricDceSwSrvEpSlotId": cfprApFabricDceSwSrvEpSlotId,
       "cfprApFabricDceSwSrvEpSwitchId": cfprApFabricDceSwSrvEpSwitchId,
       "cfprApFabricDceSwSrvEpTransport": cfprApFabricDceSwSrvEpTransport,
       "cfprApFabricDceSwSrvEpType": cfprApFabricDceSwSrvEpType,
       "cfprApFabricDceSwSrvEpUsrLbl": cfprApFabricDceSwSrvEpUsrLbl,
       "cfprApFabricDceSwSrvPcTable": cfprApFabricDceSwSrvPcTable,
       "cfprApFabricDceSwSrvPcEntry": cfprApFabricDceSwSrvPcEntry,
       "cfprApFabricDceSwSrvPcInstanceId": cfprApFabricDceSwSrvPcInstanceId,
       "cfprApFabricDceSwSrvPcDn": cfprApFabricDceSwSrvPcDn,
       "cfprApFabricDceSwSrvPcRn": cfprApFabricDceSwSrvPcRn,
       "cfprApFabricDceSwSrvPcAdminState": cfprApFabricDceSwSrvPcAdminState,
       "cfprApFabricDceSwSrvPcChassisId": cfprApFabricDceSwSrvPcChassisId,
       "cfprApFabricDceSwSrvPcDescr": cfprApFabricDceSwSrvPcDescr,
       "cfprApFabricDceSwSrvPcEpDn": cfprApFabricDceSwSrvPcEpDn,
       "cfprApFabricDceSwSrvPcFltAggr": cfprApFabricDceSwSrvPcFltAggr,
       "cfprApFabricDceSwSrvPcIfRole": cfprApFabricDceSwSrvPcIfRole,
       "cfprApFabricDceSwSrvPcIfType": cfprApFabricDceSwSrvPcIfType,
       "cfprApFabricDceSwSrvPcLocale": cfprApFabricDceSwSrvPcLocale,
       "cfprApFabricDceSwSrvPcName": cfprApFabricDceSwSrvPcName,
       "cfprApFabricDceSwSrvPcOperSpeed": cfprApFabricDceSwSrvPcOperSpeed,
       "cfprApFabricDceSwSrvPcOperState": cfprApFabricDceSwSrvPcOperState,
       "cfprApFabricDceSwSrvPcPeerDn": cfprApFabricDceSwSrvPcPeerDn,
       "cfprApFabricDceSwSrvPcPortId": cfprApFabricDceSwSrvPcPortId,
       "cfprApFabricDceSwSrvPcStateQual": cfprApFabricDceSwSrvPcStateQual,
       "cfprApFabricDceSwSrvPcSwitchId": cfprApFabricDceSwSrvPcSwitchId,
       "cfprApFabricDceSwSrvPcTransport": cfprApFabricDceSwSrvPcTransport,
       "cfprApFabricDceSwSrvPcType": cfprApFabricDceSwSrvPcType,
       "cfprApFabricDceSwSrvPcEpTable": cfprApFabricDceSwSrvPcEpTable,
       "cfprApFabricDceSwSrvPcEpEntry": cfprApFabricDceSwSrvPcEpEntry,
       "cfprApFabricDceSwSrvPcEpInstanceId": cfprApFabricDceSwSrvPcEpInstanceId,
       "cfprApFabricDceSwSrvPcEpDnData": cfprApFabricDceSwSrvPcEpDnData,
       "cfprApFabricDceSwSrvPcEpRn": cfprApFabricDceSwSrvPcEpRn,
       "cfprApFabricDceSwSrvPcEpAdminState": cfprApFabricDceSwSrvPcEpAdminState,
       "cfprApFabricDceSwSrvPcEpAggrPortId": cfprApFabricDceSwSrvPcEpAggrPortId,
       "cfprApFabricDceSwSrvPcEpChassisId": cfprApFabricDceSwSrvPcEpChassisId,
       "cfprApFabricDceSwSrvPcEpEpDn": cfprApFabricDceSwSrvPcEpEpDn,
       "cfprApFabricDceSwSrvPcEpFltAggr": cfprApFabricDceSwSrvPcEpFltAggr,
       "cfprApFabricDceSwSrvPcEpIfRole": cfprApFabricDceSwSrvPcEpIfRole,
       "cfprApFabricDceSwSrvPcEpIfType": cfprApFabricDceSwSrvPcEpIfType,
       "cfprApFabricDceSwSrvPcEpLicGP": cfprApFabricDceSwSrvPcEpLicGP,
       "cfprApFabricDceSwSrvPcEpLicState": cfprApFabricDceSwSrvPcEpLicState,
       "cfprApFabricDceSwSrvPcEpLocale": cfprApFabricDceSwSrvPcEpLocale,
       "cfprApFabricDceSwSrvPcEpMembership": cfprApFabricDceSwSrvPcEpMembership,
       "cfprApFabricDceSwSrvPcEpName": cfprApFabricDceSwSrvPcEpName,
       "cfprApFabricDceSwSrvPcEpOperState": cfprApFabricDceSwSrvPcEpOperState,
       "cfprApFabricDceSwSrvPcEpOperStateReason": cfprApFabricDceSwSrvPcEpOperStateReason,
       "cfprApFabricDceSwSrvPcEpPeerAggrPortId": cfprApFabricDceSwSrvPcEpPeerAggrPortId,
       "cfprApFabricDceSwSrvPcEpPeerChassisId": cfprApFabricDceSwSrvPcEpPeerChassisId,
       "cfprApFabricDceSwSrvPcEpPeerDn": cfprApFabricDceSwSrvPcEpPeerDn,
       "cfprApFabricDceSwSrvPcEpPeerPortId": cfprApFabricDceSwSrvPcEpPeerPortId,
       "cfprApFabricDceSwSrvPcEpPeerSlotId": cfprApFabricDceSwSrvPcEpPeerSlotId,
       "cfprApFabricDceSwSrvPcEpPortId": cfprApFabricDceSwSrvPcEpPortId,
       "cfprApFabricDceSwSrvPcEpSlotId": cfprApFabricDceSwSrvPcEpSlotId,
       "cfprApFabricDceSwSrvPcEpSwitchId": cfprApFabricDceSwSrvPcEpSwitchId,
       "cfprApFabricDceSwSrvPcEpTransport": cfprApFabricDceSwSrvPcEpTransport,
       "cfprApFabricDceSwSrvPcEpType": cfprApFabricDceSwSrvPcEpType,
       "cfprApFabricDceSwSrvPcEpUsrLbl": cfprApFabricDceSwSrvPcEpUsrLbl,
       "cfprApFabricEpTable": cfprApFabricEpTable,
       "cfprApFabricEpEntry": cfprApFabricEpEntry,
       "cfprApFabricEpInstanceId": cfprApFabricEpInstanceId,
       "cfprApFabricEpDn": cfprApFabricEpDn,
       "cfprApFabricEpRn": cfprApFabricEpRn,
       "cfprApFabricEpMgrTable": cfprApFabricEpMgrTable,
       "cfprApFabricEpMgrEntry": cfprApFabricEpMgrEntry,
       "cfprApFabricEpMgrInstanceId": cfprApFabricEpMgrInstanceId,
       "cfprApFabricEpMgrDn": cfprApFabricEpMgrDn,
       "cfprApFabricEpMgrRn": cfprApFabricEpMgrRn,
       "cfprApFabricEpMgrConfMode": cfprApFabricEpMgrConfMode,
       "cfprApFabricEpMgrConfQual": cfprApFabricEpMgrConfQual,
       "cfprApFabricEpMgrConfState": cfprApFabricEpMgrConfState,
       "cfprApFabricEpMgrFltAggr": cfprApFabricEpMgrFltAggr,
       "cfprApFabricEpMgrFsmDescr": cfprApFabricEpMgrFsmDescr,
       "cfprApFabricEpMgrFsmFlags": cfprApFabricEpMgrFsmFlags,
       "cfprApFabricEpMgrFsmPrev": cfprApFabricEpMgrFsmPrev,
       "cfprApFabricEpMgrFsmProgr": cfprApFabricEpMgrFsmProgr,
       "cfprApFabricEpMgrFsmRmtInvErrCode": cfprApFabricEpMgrFsmRmtInvErrCode,
       "cfprApFabricEpMgrFsmRmtInvErrDescr": cfprApFabricEpMgrFsmRmtInvErrDescr,
       "cfprApFabricEpMgrFsmRmtInvRslt": cfprApFabricEpMgrFsmRmtInvRslt,
       "cfprApFabricEpMgrFsmStageDescr": cfprApFabricEpMgrFsmStageDescr,
       "cfprApFabricEpMgrFsmStamp": cfprApFabricEpMgrFsmStamp,
       "cfprApFabricEpMgrFsmStatus": cfprApFabricEpMgrFsmStatus,
       "cfprApFabricEpMgrFsmTry": cfprApFabricEpMgrFsmTry,
       "cfprApFabricEpMgrId": cfprApFabricEpMgrId,
       "cfprApFabricEpMgrFsmTable": cfprApFabricEpMgrFsmTable,
       "cfprApFabricEpMgrFsmEntry": cfprApFabricEpMgrFsmEntry,
       "cfprApFabricEpMgrFsmInstanceId": cfprApFabricEpMgrFsmInstanceId,
       "cfprApFabricEpMgrFsmDn": cfprApFabricEpMgrFsmDn,
       "cfprApFabricEpMgrFsmRn": cfprApFabricEpMgrFsmRn,
       "cfprApFabricEpMgrFsmCompletionTime": cfprApFabricEpMgrFsmCompletionTime,
       "cfprApFabricEpMgrFsmCurrentFsm": cfprApFabricEpMgrFsmCurrentFsm,
       "cfprApFabricEpMgrFsmDescrData": cfprApFabricEpMgrFsmDescrData,
       "cfprApFabricEpMgrFsmFsmStatus": cfprApFabricEpMgrFsmFsmStatus,
       "cfprApFabricEpMgrFsmProgress": cfprApFabricEpMgrFsmProgress,
       "cfprApFabricEpMgrFsmRmtErrCode": cfprApFabricEpMgrFsmRmtErrCode,
       "cfprApFabricEpMgrFsmRmtErrDescr": cfprApFabricEpMgrFsmRmtErrDescr,
       "cfprApFabricEpMgrFsmRmtRslt": cfprApFabricEpMgrFsmRmtRslt,
       "cfprApFabricEpMgrFsmStageTable": cfprApFabricEpMgrFsmStageTable,
       "cfprApFabricEpMgrFsmStageEntry": cfprApFabricEpMgrFsmStageEntry,
       "cfprApFabricEpMgrFsmStageInstanceId": cfprApFabricEpMgrFsmStageInstanceId,
       "cfprApFabricEpMgrFsmStageDn": cfprApFabricEpMgrFsmStageDn,
       "cfprApFabricEpMgrFsmStageRn": cfprApFabricEpMgrFsmStageRn,
       "cfprApFabricEpMgrFsmStageDescrData": cfprApFabricEpMgrFsmStageDescrData,
       "cfprApFabricEpMgrFsmStageLastUpdateTime": cfprApFabricEpMgrFsmStageLastUpdateTime,
       "cfprApFabricEpMgrFsmStageName": cfprApFabricEpMgrFsmStageName,
       "cfprApFabricEpMgrFsmStageOrder": cfprApFabricEpMgrFsmStageOrder,
       "cfprApFabricEpMgrFsmStageRetry": cfprApFabricEpMgrFsmStageRetry,
       "cfprApFabricEpMgrFsmStageStageStatus": cfprApFabricEpMgrFsmStageStageStatus,
       "cfprApFabricEpMgrFsmTaskTable": cfprApFabricEpMgrFsmTaskTable,
       "cfprApFabricEpMgrFsmTaskEntry": cfprApFabricEpMgrFsmTaskEntry,
       "cfprApFabricEpMgrFsmTaskInstanceId": cfprApFabricEpMgrFsmTaskInstanceId,
       "cfprApFabricEpMgrFsmTaskDn": cfprApFabricEpMgrFsmTaskDn,
       "cfprApFabricEpMgrFsmTaskRn": cfprApFabricEpMgrFsmTaskRn,
       "cfprApFabricEpMgrFsmTaskCompletion": cfprApFabricEpMgrFsmTaskCompletion,
       "cfprApFabricEpMgrFsmTaskFlags": cfprApFabricEpMgrFsmTaskFlags,
       "cfprApFabricEpMgrFsmTaskItem": cfprApFabricEpMgrFsmTaskItem,
       "cfprApFabricEpMgrFsmTaskSeqId": cfprApFabricEpMgrFsmTaskSeqId,
       "cfprApFabricEthEstcTable": cfprApFabricEthEstcTable,
       "cfprApFabricEthEstcEntry": cfprApFabricEthEstcEntry,
       "cfprApFabricEthEstcInstanceId": cfprApFabricEthEstcInstanceId,
       "cfprApFabricEthEstcDn": cfprApFabricEthEstcDn,
       "cfprApFabricEthEstcRn": cfprApFabricEthEstcRn,
       "cfprApFabricEthEstcId": cfprApFabricEthEstcId,
       "cfprApFabricEthEstcLocale": cfprApFabricEthEstcLocale,
       "cfprApFabricEthEstcName": cfprApFabricEthEstcName,
       "cfprApFabricEthEstcTransport": cfprApFabricEthEstcTransport,
       "cfprApFabricEthEstcType": cfprApFabricEthEstcType,
       "cfprApFabricEthEstcCloudTable": cfprApFabricEthEstcCloudTable,
       "cfprApFabricEthEstcCloudEntry": cfprApFabricEthEstcCloudEntry,
       "cfprApFabricEthEstcCloudInstanceId": cfprApFabricEthEstcCloudInstanceId,
       "cfprApFabricEthEstcCloudDn": cfprApFabricEthEstcCloudDn,
       "cfprApFabricEthEstcCloudRn": cfprApFabricEthEstcCloudRn,
       "cfprApFabricEthEstcEpTable": cfprApFabricEthEstcEpTable,
       "cfprApFabricEthEstcEpEntry": cfprApFabricEthEstcEpEntry,
       "cfprApFabricEthEstcEpInstanceId": cfprApFabricEthEstcEpInstanceId,
       "cfprApFabricEthEstcEpDn": cfprApFabricEthEstcEpDn,
       "cfprApFabricEthEstcEpRn": cfprApFabricEthEstcEpRn,
       "cfprApFabricEthEstcEpAdminSpeed": cfprApFabricEthEstcEpAdminSpeed,
       "cfprApFabricEthEstcEpAdminState": cfprApFabricEthEstcEpAdminState,
       "cfprApFabricEthEstcEpAggrPortId": cfprApFabricEthEstcEpAggrPortId,
       "cfprApFabricEthEstcEpChassisId": cfprApFabricEthEstcEpChassisId,
       "cfprApFabricEthEstcEpConfigState": cfprApFabricEthEstcEpConfigState,
       "cfprApFabricEthEstcEpEpDn": cfprApFabricEthEstcEpEpDn,
       "cfprApFabricEthEstcEpFlowCtrlPolicy": cfprApFabricEthEstcEpFlowCtrlPolicy,
       "cfprApFabricEthEstcEpFltAggr": cfprApFabricEthEstcEpFltAggr,
       "cfprApFabricEthEstcEpIfRole": cfprApFabricEthEstcEpIfRole,
       "cfprApFabricEthEstcEpIfType": cfprApFabricEthEstcEpIfType,
       "cfprApFabricEthEstcEpLicGP": cfprApFabricEthEstcEpLicGP,
       "cfprApFabricEthEstcEpLicState": cfprApFabricEthEstcEpLicState,
       "cfprApFabricEthEstcEpLocale": cfprApFabricEthEstcEpLocale,
       "cfprApFabricEthEstcEpName": cfprApFabricEthEstcEpName,
       "cfprApFabricEthEstcEpNwCtrlPolicyName": cfprApFabricEthEstcEpNwCtrlPolicyName,
       "cfprApFabricEthEstcEpOperNwCtrlPolicyName": cfprApFabricEthEstcEpOperNwCtrlPolicyName,
       "cfprApFabricEthEstcEpOperPortMode": cfprApFabricEthEstcEpOperPortMode,
       "cfprApFabricEthEstcEpOperState": cfprApFabricEthEstcEpOperState,
       "cfprApFabricEthEstcEpOperStateReason": cfprApFabricEthEstcEpOperStateReason,
       "cfprApFabricEthEstcEpPeerAggrPortId": cfprApFabricEthEstcEpPeerAggrPortId,
       "cfprApFabricEthEstcEpPeerChassisId": cfprApFabricEthEstcEpPeerChassisId,
       "cfprApFabricEthEstcEpPeerDn": cfprApFabricEthEstcEpPeerDn,
       "cfprApFabricEthEstcEpPeerPortId": cfprApFabricEthEstcEpPeerPortId,
       "cfprApFabricEthEstcEpPeerSlotId": cfprApFabricEthEstcEpPeerSlotId,
       "cfprApFabricEthEstcEpPinGroupName": cfprApFabricEthEstcEpPinGroupName,
       "cfprApFabricEthEstcEpPortId": cfprApFabricEthEstcEpPortId,
       "cfprApFabricEthEstcEpPortMode": cfprApFabricEthEstcEpPortMode,
       "cfprApFabricEthEstcEpPrio": cfprApFabricEthEstcEpPrio,
       "cfprApFabricEthEstcEpSlotId": cfprApFabricEthEstcEpSlotId,
       "cfprApFabricEthEstcEpSwitchId": cfprApFabricEthEstcEpSwitchId,
       "cfprApFabricEthEstcEpTransport": cfprApFabricEthEstcEpTransport,
       "cfprApFabricEthEstcEpType": cfprApFabricEthEstcEpType,
       "cfprApFabricEthEstcEpUsrLbl": cfprApFabricEthEstcEpUsrLbl,
       "cfprApFabricEthEstcEpWarnings": cfprApFabricEthEstcEpWarnings,
       "cfprApFabricEthEstcPcTable": cfprApFabricEthEstcPcTable,
       "cfprApFabricEthEstcPcEntry": cfprApFabricEthEstcPcEntry,
       "cfprApFabricEthEstcPcInstanceId": cfprApFabricEthEstcPcInstanceId,
       "cfprApFabricEthEstcPcDn": cfprApFabricEthEstcPcDn,
       "cfprApFabricEthEstcPcRn": cfprApFabricEthEstcPcRn,
       "cfprApFabricEthEstcPcAdminSpeed": cfprApFabricEthEstcPcAdminSpeed,
       "cfprApFabricEthEstcPcAdminState": cfprApFabricEthEstcPcAdminState,
       "cfprApFabricEthEstcPcDescr": cfprApFabricEthEstcPcDescr,
       "cfprApFabricEthEstcPcEpDn": cfprApFabricEthEstcPcEpDn,
       "cfprApFabricEthEstcPcFlowCtrlPolicy": cfprApFabricEthEstcPcFlowCtrlPolicy,
       "cfprApFabricEthEstcPcFltAggr": cfprApFabricEthEstcPcFltAggr,
       "cfprApFabricEthEstcPcIfRole": cfprApFabricEthEstcPcIfRole,
       "cfprApFabricEthEstcPcIfType": cfprApFabricEthEstcPcIfType,
       "cfprApFabricEthEstcPcLacpPolicyName": cfprApFabricEthEstcPcLacpPolicyName,
       "cfprApFabricEthEstcPcLocale": cfprApFabricEthEstcPcLocale,
       "cfprApFabricEthEstcPcName": cfprApFabricEthEstcPcName,
       "cfprApFabricEthEstcPcNwCtrlPolicyName": cfprApFabricEthEstcPcNwCtrlPolicyName,
       "cfprApFabricEthEstcPcOperLacpPolicyName": cfprApFabricEthEstcPcOperLacpPolicyName,
       "cfprApFabricEthEstcPcOperNwCtrlPolicyName": cfprApFabricEthEstcPcOperNwCtrlPolicyName,
       "cfprApFabricEthEstcPcOperSpeed": cfprApFabricEthEstcPcOperSpeed,
       "cfprApFabricEthEstcPcOperState": cfprApFabricEthEstcPcOperState,
       "cfprApFabricEthEstcPcPeerDn": cfprApFabricEthEstcPcPeerDn,
       "cfprApFabricEthEstcPcPinGroupName": cfprApFabricEthEstcPcPinGroupName,
       "cfprApFabricEthEstcPcPortId": cfprApFabricEthEstcPcPortId,
       "cfprApFabricEthEstcPcPortMode": cfprApFabricEthEstcPcPortMode,
       "cfprApFabricEthEstcPcPrio": cfprApFabricEthEstcPcPrio,
       "cfprApFabricEthEstcPcProtocol": cfprApFabricEthEstcPcProtocol,
       "cfprApFabricEthEstcPcStateQual": cfprApFabricEthEstcPcStateQual,
       "cfprApFabricEthEstcPcSwitchId": cfprApFabricEthEstcPcSwitchId,
       "cfprApFabricEthEstcPcTransport": cfprApFabricEthEstcPcTransport,
       "cfprApFabricEthEstcPcType": cfprApFabricEthEstcPcType,
       "cfprApFabricEthEstcPcWarnings": cfprApFabricEthEstcPcWarnings,
       "cfprApFabricEthEstcPcEpTable": cfprApFabricEthEstcPcEpTable,
       "cfprApFabricEthEstcPcEpEntry": cfprApFabricEthEstcPcEpEntry,
       "cfprApFabricEthEstcPcEpInstanceId": cfprApFabricEthEstcPcEpInstanceId,
       "cfprApFabricEthEstcPcEpDnData": cfprApFabricEthEstcPcEpDnData,
       "cfprApFabricEthEstcPcEpRn": cfprApFabricEthEstcPcEpRn,
       "cfprApFabricEthEstcPcEpAdminSpeed": cfprApFabricEthEstcPcEpAdminSpeed,
       "cfprApFabricEthEstcPcEpAdminState": cfprApFabricEthEstcPcEpAdminState,
       "cfprApFabricEthEstcPcEpAggrPortId": cfprApFabricEthEstcPcEpAggrPortId,
       "cfprApFabricEthEstcPcEpChassisId": cfprApFabricEthEstcPcEpChassisId,
       "cfprApFabricEthEstcPcEpConfigState": cfprApFabricEthEstcPcEpConfigState,
       "cfprApFabricEthEstcPcEpEpDn": cfprApFabricEthEstcPcEpEpDn,
       "cfprApFabricEthEstcPcEpFltAggr": cfprApFabricEthEstcPcEpFltAggr,
       "cfprApFabricEthEstcPcEpIfRole": cfprApFabricEthEstcPcEpIfRole,
       "cfprApFabricEthEstcPcEpIfType": cfprApFabricEthEstcPcEpIfType,
       "cfprApFabricEthEstcPcEpLicGP": cfprApFabricEthEstcPcEpLicGP,
       "cfprApFabricEthEstcPcEpLicState": cfprApFabricEthEstcPcEpLicState,
       "cfprApFabricEthEstcPcEpLocale": cfprApFabricEthEstcPcEpLocale,
       "cfprApFabricEthEstcPcEpMembership": cfprApFabricEthEstcPcEpMembership,
       "cfprApFabricEthEstcPcEpName": cfprApFabricEthEstcPcEpName,
       "cfprApFabricEthEstcPcEpOperState": cfprApFabricEthEstcPcEpOperState,
       "cfprApFabricEthEstcPcEpOperStateReason": cfprApFabricEthEstcPcEpOperStateReason,
       "cfprApFabricEthEstcPcEpPeerAggrPortId": cfprApFabricEthEstcPcEpPeerAggrPortId,
       "cfprApFabricEthEstcPcEpPeerChassisId": cfprApFabricEthEstcPcEpPeerChassisId,
       "cfprApFabricEthEstcPcEpPeerDn": cfprApFabricEthEstcPcEpPeerDn,
       "cfprApFabricEthEstcPcEpPeerPortId": cfprApFabricEthEstcPcEpPeerPortId,
       "cfprApFabricEthEstcPcEpPeerSlotId": cfprApFabricEthEstcPcEpPeerSlotId,
       "cfprApFabricEthEstcPcEpPortId": cfprApFabricEthEstcPcEpPortId,
       "cfprApFabricEthEstcPcEpSlotId": cfprApFabricEthEstcPcEpSlotId,
       "cfprApFabricEthEstcPcEpSwitchId": cfprApFabricEthEstcPcEpSwitchId,
       "cfprApFabricEthEstcPcEpTransport": cfprApFabricEthEstcPcEpTransport,
       "cfprApFabricEthEstcPcEpType": cfprApFabricEthEstcPcEpType,
       "cfprApFabricEthEstcPcEpUsrLbl": cfprApFabricEthEstcPcEpUsrLbl,
       "cfprApFabricEthEstcPcEpWarnings": cfprApFabricEthEstcPcEpWarnings,
       "cfprApFabricEthLanTable": cfprApFabricEthLanTable,
       "cfprApFabricEthLanEntry": cfprApFabricEthLanEntry,
       "cfprApFabricEthLanInstanceId": cfprApFabricEthLanInstanceId,
       "cfprApFabricEthLanDn": cfprApFabricEthLanDn,
       "cfprApFabricEthLanRn": cfprApFabricEthLanRn,
       "cfprApFabricEthLanId": cfprApFabricEthLanId,
       "cfprApFabricEthLanLocale": cfprApFabricEthLanLocale,
       "cfprApFabricEthLanName": cfprApFabricEthLanName,
       "cfprApFabricEthLanTransport": cfprApFabricEthLanTransport,
       "cfprApFabricEthLanType": cfprApFabricEthLanType,
       "cfprApFabricEthLanEpTable": cfprApFabricEthLanEpTable,
       "cfprApFabricEthLanEpEntry": cfprApFabricEthLanEpEntry,
       "cfprApFabricEthLanEpInstanceId": cfprApFabricEthLanEpInstanceId,
       "cfprApFabricEthLanEpDn": cfprApFabricEthLanEpDn,
       "cfprApFabricEthLanEpRn": cfprApFabricEthLanEpRn,
       "cfprApFabricEthLanEpAdminDuplex": cfprApFabricEthLanEpAdminDuplex,
       "cfprApFabricEthLanEpAdminSpeed": cfprApFabricEthLanEpAdminSpeed,
       "cfprApFabricEthLanEpAdminState": cfprApFabricEthLanEpAdminState,
       "cfprApFabricEthLanEpAggrPortId": cfprApFabricEthLanEpAggrPortId,
       "cfprApFabricEthLanEpAutoNeg": cfprApFabricEthLanEpAutoNeg,
       "cfprApFabricEthLanEpChassisId": cfprApFabricEthLanEpChassisId,
       "cfprApFabricEthLanEpDtagVlan": cfprApFabricEthLanEpDtagVlan,
       "cfprApFabricEthLanEpEpDn": cfprApFabricEthLanEpEpDn,
       "cfprApFabricEthLanEpEthLinkProfileName": cfprApFabricEthLanEpEthLinkProfileName,
       "cfprApFabricEthLanEpFlowCtrlPolicy": cfprApFabricEthLanEpFlowCtrlPolicy,
       "cfprApFabricEthLanEpFltAggr": cfprApFabricEthLanEpFltAggr,
       "cfprApFabricEthLanEpHashAlg": cfprApFabricEthLanEpHashAlg,
       "cfprApFabricEthLanEpIfRole": cfprApFabricEthLanEpIfRole,
       "cfprApFabricEthLanEpIfType": cfprApFabricEthLanEpIfType,
       "cfprApFabricEthLanEpLicGP": cfprApFabricEthLanEpLicGP,
       "cfprApFabricEthLanEpLicState": cfprApFabricEthLanEpLicState,
       "cfprApFabricEthLanEpLocale": cfprApFabricEthLanEpLocale,
       "cfprApFabricEthLanEpName": cfprApFabricEthLanEpName,
       "cfprApFabricEthLanEpOperEthLinkProfileName": cfprApFabricEthLanEpOperEthLinkProfileName,
       "cfprApFabricEthLanEpOperState": cfprApFabricEthLanEpOperState,
       "cfprApFabricEthLanEpOperStateReason": cfprApFabricEthLanEpOperStateReason,
       "cfprApFabricEthLanEpOverlappingVlans": cfprApFabricEthLanEpOverlappingVlans,
       "cfprApFabricEthLanEpPeerAggrPortId": cfprApFabricEthLanEpPeerAggrPortId,
       "cfprApFabricEthLanEpPeerChassisId": cfprApFabricEthLanEpPeerChassisId,
       "cfprApFabricEthLanEpPeerDn": cfprApFabricEthLanEpPeerDn,
       "cfprApFabricEthLanEpPeerPortId": cfprApFabricEthLanEpPeerPortId,
       "cfprApFabricEthLanEpPeerSlotId": cfprApFabricEthLanEpPeerSlotId,
       "cfprApFabricEthLanEpPortId": cfprApFabricEthLanEpPortId,
       "cfprApFabricEthLanEpQosPrio": cfprApFabricEthLanEpQosPrio,
       "cfprApFabricEthLanEpSlotId": cfprApFabricEthLanEpSlotId,
       "cfprApFabricEthLanEpSpeedCap": cfprApFabricEthLanEpSpeedCap,
       "cfprApFabricEthLanEpSsaPortType": cfprApFabricEthLanEpSsaPortType,
       "cfprApFabricEthLanEpSsaVlanId": cfprApFabricEthLanEpSsaVlanId,
       "cfprApFabricEthLanEpSwitchId": cfprApFabricEthLanEpSwitchId,
       "cfprApFabricEthLanEpTransport": cfprApFabricEthLanEpTransport,
       "cfprApFabricEthLanEpType": cfprApFabricEthLanEpType,
       "cfprApFabricEthLanEpUdldOperState": cfprApFabricEthLanEpUdldOperState,
       "cfprApFabricEthLanEpUsrLbl": cfprApFabricEthLanEpUsrLbl,
       "cfprApFabricEthLanEpVlanStatus": cfprApFabricEthLanEpVlanStatus,
       "cfprApFabricEthLanEpWarnings": cfprApFabricEthLanEpWarnings,
       "cfprApFabricEthLanPcTable": cfprApFabricEthLanPcTable,
       "cfprApFabricEthLanPcEntry": cfprApFabricEthLanPcEntry,
       "cfprApFabricEthLanPcInstanceId": cfprApFabricEthLanPcInstanceId,
       "cfprApFabricEthLanPcDn": cfprApFabricEthLanPcDn,
       "cfprApFabricEthLanPcRn": cfprApFabricEthLanPcRn,
       "cfprApFabricEthLanPcAdminDuplex": cfprApFabricEthLanPcAdminDuplex,
       "cfprApFabricEthLanPcAdminSpeed": cfprApFabricEthLanPcAdminSpeed,
       "cfprApFabricEthLanPcAdminState": cfprApFabricEthLanPcAdminState,
       "cfprApFabricEthLanPcAutoNeg": cfprApFabricEthLanPcAutoNeg,
       "cfprApFabricEthLanPcBandwidth": cfprApFabricEthLanPcBandwidth,
       "cfprApFabricEthLanPcCluChassisId": cfprApFabricEthLanPcCluChassisId,
       "cfprApFabricEthLanPcClusterName": cfprApFabricEthLanPcClusterName,
       "cfprApFabricEthLanPcDescr": cfprApFabricEthLanPcDescr,
       "cfprApFabricEthLanPcDtagVlan": cfprApFabricEthLanPcDtagVlan,
       "cfprApFabricEthLanPcEpDn": cfprApFabricEthLanPcEpDn,
       "cfprApFabricEthLanPcFlowCtrlPolicy": cfprApFabricEthLanPcFlowCtrlPolicy,
       "cfprApFabricEthLanPcFltAggr": cfprApFabricEthLanPcFltAggr,
       "cfprApFabricEthLanPcHashAlg": cfprApFabricEthLanPcHashAlg,
       "cfprApFabricEthLanPcIfRole": cfprApFabricEthLanPcIfRole,
       "cfprApFabricEthLanPcIfType": cfprApFabricEthLanPcIfType,
       "cfprApFabricEthLanPcLacpDetach": cfprApFabricEthLanPcLacpDetach,
       "cfprApFabricEthLanPcLacpMode": cfprApFabricEthLanPcLacpMode,
       "cfprApFabricEthLanPcLacpPolicyName": cfprApFabricEthLanPcLacpPolicyName,
       "cfprApFabricEthLanPcLocale": cfprApFabricEthLanPcLocale,
       "cfprApFabricEthLanPcName": cfprApFabricEthLanPcName,
       "cfprApFabricEthLanPcOperLacpPolicyName": cfprApFabricEthLanPcOperLacpPolicyName,
       "cfprApFabricEthLanPcOperSpeed": cfprApFabricEthLanPcOperSpeed,
       "cfprApFabricEthLanPcOperState": cfprApFabricEthLanPcOperState,
       "cfprApFabricEthLanPcOverlappingVlans": cfprApFabricEthLanPcOverlappingVlans,
       "cfprApFabricEthLanPcPeerDn": cfprApFabricEthLanPcPeerDn,
       "cfprApFabricEthLanPcPortId": cfprApFabricEthLanPcPortId,
       "cfprApFabricEthLanPcQosPrio": cfprApFabricEthLanPcQosPrio,
       "cfprApFabricEthLanPcSpannedCluster": cfprApFabricEthLanPcSpannedCluster,
       "cfprApFabricEthLanPcSpeedCap": cfprApFabricEthLanPcSpeedCap,
       "cfprApFabricEthLanPcSsaPortType": cfprApFabricEthLanPcSsaPortType,
       "cfprApFabricEthLanPcSsaVlanId": cfprApFabricEthLanPcSsaVlanId,
       "cfprApFabricEthLanPcStateQual": cfprApFabricEthLanPcStateQual,
       "cfprApFabricEthLanPcSwitchId": cfprApFabricEthLanPcSwitchId,
       "cfprApFabricEthLanPcTransport": cfprApFabricEthLanPcTransport,
       "cfprApFabricEthLanPcType": cfprApFabricEthLanPcType,
       "cfprApFabricEthLanPcVlanStatus": cfprApFabricEthLanPcVlanStatus,
       "cfprApFabricEthLanPcWarnings": cfprApFabricEthLanPcWarnings,
       "cfprApFabricEthLanPcEpTable": cfprApFabricEthLanPcEpTable,
       "cfprApFabricEthLanPcEpEntry": cfprApFabricEthLanPcEpEntry,
       "cfprApFabricEthLanPcEpInstanceId": cfprApFabricEthLanPcEpInstanceId,
       "cfprApFabricEthLanPcEpDnData": cfprApFabricEthLanPcEpDnData,
       "cfprApFabricEthLanPcEpRn": cfprApFabricEthLanPcEpRn,
       "cfprApFabricEthLanPcEpAdminState": cfprApFabricEthLanPcEpAdminState,
       "cfprApFabricEthLanPcEpAggrPortId": cfprApFabricEthLanPcEpAggrPortId,
       "cfprApFabricEthLanPcEpChassisId": cfprApFabricEthLanPcEpChassisId,
       "cfprApFabricEthLanPcEpEpDn": cfprApFabricEthLanPcEpEpDn,
       "cfprApFabricEthLanPcEpEthLinkProfileName": cfprApFabricEthLanPcEpEthLinkProfileName,
       "cfprApFabricEthLanPcEpFltAggr": cfprApFabricEthLanPcEpFltAggr,
       "cfprApFabricEthLanPcEpIfRole": cfprApFabricEthLanPcEpIfRole,
       "cfprApFabricEthLanPcEpIfType": cfprApFabricEthLanPcEpIfType,
       "cfprApFabricEthLanPcEpLicGP": cfprApFabricEthLanPcEpLicGP,
       "cfprApFabricEthLanPcEpLicState": cfprApFabricEthLanPcEpLicState,
       "cfprApFabricEthLanPcEpLocale": cfprApFabricEthLanPcEpLocale,
       "cfprApFabricEthLanPcEpMembership": cfprApFabricEthLanPcEpMembership,
       "cfprApFabricEthLanPcEpName": cfprApFabricEthLanPcEpName,
       "cfprApFabricEthLanPcEpOperEthLinkProfileName": cfprApFabricEthLanPcEpOperEthLinkProfileName,
       "cfprApFabricEthLanPcEpOperState": cfprApFabricEthLanPcEpOperState,
       "cfprApFabricEthLanPcEpOperStateReason": cfprApFabricEthLanPcEpOperStateReason,
       "cfprApFabricEthLanPcEpPeerAggrPortId": cfprApFabricEthLanPcEpPeerAggrPortId,
       "cfprApFabricEthLanPcEpPeerChassisId": cfprApFabricEthLanPcEpPeerChassisId,
       "cfprApFabricEthLanPcEpPeerDn": cfprApFabricEthLanPcEpPeerDn,
       "cfprApFabricEthLanPcEpPeerPortId": cfprApFabricEthLanPcEpPeerPortId,
       "cfprApFabricEthLanPcEpPeerSlotId": cfprApFabricEthLanPcEpPeerSlotId,
       "cfprApFabricEthLanPcEpPortId": cfprApFabricEthLanPcEpPortId,
       "cfprApFabricEthLanPcEpSlotId": cfprApFabricEthLanPcEpSlotId,
       "cfprApFabricEthLanPcEpSwitchId": cfprApFabricEthLanPcEpSwitchId,
       "cfprApFabricEthLanPcEpTransport": cfprApFabricEthLanPcEpTransport,
       "cfprApFabricEthLanPcEpType": cfprApFabricEthLanPcEpType,
       "cfprApFabricEthLanPcEpUdldOperState": cfprApFabricEthLanPcEpUdldOperState,
       "cfprApFabricEthLanPcEpWarnings": cfprApFabricEthLanPcEpWarnings,
       "cfprApFabricEthLinkProfileTable": cfprApFabricEthLinkProfileTable,
       "cfprApFabricEthLinkProfileEntry": cfprApFabricEthLinkProfileEntry,
       "cfprApFabricEthLinkProfileInstanceId": cfprApFabricEthLinkProfileInstanceId,
       "cfprApFabricEthLinkProfileDn": cfprApFabricEthLinkProfileDn,
       "cfprApFabricEthLinkProfileRn": cfprApFabricEthLinkProfileRn,
       "cfprApFabricEthLinkProfileCdpLinkPolicyName": cfprApFabricEthLinkProfileCdpLinkPolicyName,
       "cfprApFabricEthLinkProfileDescr": cfprApFabricEthLinkProfileDescr,
       "cfprApFabricEthLinkProfileIntId": cfprApFabricEthLinkProfileIntId,
       "cfprApFabricEthLinkProfileName": cfprApFabricEthLinkProfileName,
       "cfprApFabricEthLinkProfileOperCdpLinkPolicyName": cfprApFabricEthLinkProfileOperCdpLinkPolicyName,
       "cfprApFabricEthLinkProfileOperUdldLinkPolicyName": cfprApFabricEthLinkProfileOperUdldLinkPolicyName,
       "cfprApFabricEthLinkProfilePolicyLevel": cfprApFabricEthLinkProfilePolicyLevel,
       "cfprApFabricEthLinkProfilePolicyOwner": cfprApFabricEthLinkProfilePolicyOwner,
       "cfprApFabricEthLinkProfileUdldLinkPolicyName": cfprApFabricEthLinkProfileUdldLinkPolicyName,
       "cfprApFabricEthMonTable": cfprApFabricEthMonTable,
       "cfprApFabricEthMonEntry": cfprApFabricEthMonEntry,
       "cfprApFabricEthMonInstanceId": cfprApFabricEthMonInstanceId,
       "cfprApFabricEthMonDn": cfprApFabricEthMonDn,
       "cfprApFabricEthMonRn": cfprApFabricEthMonRn,
       "cfprApFabricEthMonAdminState": cfprApFabricEthMonAdminState,
       "cfprApFabricEthMonConfigFailReason": cfprApFabricEthMonConfigFailReason,
       "cfprApFabricEthMonId": cfprApFabricEthMonId,
       "cfprApFabricEthMonIsConfigSuccess": cfprApFabricEthMonIsConfigSuccess,
       "cfprApFabricEthMonLocale": cfprApFabricEthMonLocale,
       "cfprApFabricEthMonName": cfprApFabricEthMonName,
       "cfprApFabricEthMonOperState": cfprApFabricEthMonOperState,
       "cfprApFabricEthMonOperStateReason": cfprApFabricEthMonOperStateReason,
       "cfprApFabricEthMonPeerDn": cfprApFabricEthMonPeerDn,
       "cfprApFabricEthMonSession": cfprApFabricEthMonSession,
       "cfprApFabricEthMonTransport": cfprApFabricEthMonTransport,
       "cfprApFabricEthMonType": cfprApFabricEthMonType,
       "cfprApFabricEthMonDestEpTable": cfprApFabricEthMonDestEpTable,
       "cfprApFabricEthMonDestEpEntry": cfprApFabricEthMonDestEpEntry,
       "cfprApFabricEthMonDestEpInstanceId": cfprApFabricEthMonDestEpInstanceId,
       "cfprApFabricEthMonDestEpDn": cfprApFabricEthMonDestEpDn,
       "cfprApFabricEthMonDestEpRn": cfprApFabricEthMonDestEpRn,
       "cfprApFabricEthMonDestEpAdminSpeed": cfprApFabricEthMonDestEpAdminSpeed,
       "cfprApFabricEthMonDestEpAdminState": cfprApFabricEthMonDestEpAdminState,
       "cfprApFabricEthMonDestEpAggrPortId": cfprApFabricEthMonDestEpAggrPortId,
       "cfprApFabricEthMonDestEpChassisId": cfprApFabricEthMonDestEpChassisId,
       "cfprApFabricEthMonDestEpEpDn": cfprApFabricEthMonDestEpEpDn,
       "cfprApFabricEthMonDestEpFltAggr": cfprApFabricEthMonDestEpFltAggr,
       "cfprApFabricEthMonDestEpIfRole": cfprApFabricEthMonDestEpIfRole,
       "cfprApFabricEthMonDestEpIfType": cfprApFabricEthMonDestEpIfType,
       "cfprApFabricEthMonDestEpLicGP": cfprApFabricEthMonDestEpLicGP,
       "cfprApFabricEthMonDestEpLicState": cfprApFabricEthMonDestEpLicState,
       "cfprApFabricEthMonDestEpLocale": cfprApFabricEthMonDestEpLocale,
       "cfprApFabricEthMonDestEpName": cfprApFabricEthMonDestEpName,
       "cfprApFabricEthMonDestEpOperState": cfprApFabricEthMonDestEpOperState,
       "cfprApFabricEthMonDestEpOperStateReason": cfprApFabricEthMonDestEpOperStateReason,
       "cfprApFabricEthMonDestEpPeerAggrPortId": cfprApFabricEthMonDestEpPeerAggrPortId,
       "cfprApFabricEthMonDestEpPeerChassisId": cfprApFabricEthMonDestEpPeerChassisId,
       "cfprApFabricEthMonDestEpPeerDn": cfprApFabricEthMonDestEpPeerDn,
       "cfprApFabricEthMonDestEpPeerPortId": cfprApFabricEthMonDestEpPeerPortId,
       "cfprApFabricEthMonDestEpPeerSlotId": cfprApFabricEthMonDestEpPeerSlotId,
       "cfprApFabricEthMonDestEpPortId": cfprApFabricEthMonDestEpPortId,
       "cfprApFabricEthMonDestEpSlotId": cfprApFabricEthMonDestEpSlotId,
       "cfprApFabricEthMonDestEpSwitchId": cfprApFabricEthMonDestEpSwitchId,
       "cfprApFabricEthMonDestEpTransport": cfprApFabricEthMonDestEpTransport,
       "cfprApFabricEthMonDestEpType": cfprApFabricEthMonDestEpType,
       "cfprApFabricEthMonDestEpWarnings": cfprApFabricEthMonDestEpWarnings,
       "cfprApFabricEthMonFiltEpTable": cfprApFabricEthMonFiltEpTable,
       "cfprApFabricEthMonFiltEpEntry": cfprApFabricEthMonFiltEpEntry,
       "cfprApFabricEthMonFiltEpInstanceId": cfprApFabricEthMonFiltEpInstanceId,
       "cfprApFabricEthMonFiltEpDn": cfprApFabricEthMonFiltEpDn,
       "cfprApFabricEthMonFiltEpRn": cfprApFabricEthMonFiltEpRn,
       "cfprApFabricEthMonFiltEpName": cfprApFabricEthMonFiltEpName,
       "cfprApFabricEthMonFiltEpSession": cfprApFabricEthMonFiltEpSession,
       "cfprApFabricEthMonFiltEpType": cfprApFabricEthMonFiltEpType,
       "cfprApFabricEthMonFiltRefTable": cfprApFabricEthMonFiltRefTable,
       "cfprApFabricEthMonFiltRefEntry": cfprApFabricEthMonFiltRefEntry,
       "cfprApFabricEthMonFiltRefInstanceId": cfprApFabricEthMonFiltRefInstanceId,
       "cfprApFabricEthMonFiltRefDn": cfprApFabricEthMonFiltRefDn,
       "cfprApFabricEthMonFiltRefRn": cfprApFabricEthMonFiltRefRn,
       "cfprApFabricEthMonFiltRefSrcFiltDn": cfprApFabricEthMonFiltRefSrcFiltDn,
       "cfprApFabricEthMonFiltRefType": cfprApFabricEthMonFiltRefType,
       "cfprApFabricEthMonLanTable": cfprApFabricEthMonLanTable,
       "cfprApFabricEthMonLanEntry": cfprApFabricEthMonLanEntry,
       "cfprApFabricEthMonLanInstanceId": cfprApFabricEthMonLanInstanceId,
       "cfprApFabricEthMonLanDn": cfprApFabricEthMonLanDn,
       "cfprApFabricEthMonLanRn": cfprApFabricEthMonLanRn,
       "cfprApFabricEthMonLanId": cfprApFabricEthMonLanId,
       "cfprApFabricEthMonLanLocale": cfprApFabricEthMonLanLocale,
       "cfprApFabricEthMonLanName": cfprApFabricEthMonLanName,
       "cfprApFabricEthMonLanTransport": cfprApFabricEthMonLanTransport,
       "cfprApFabricEthMonLanType": cfprApFabricEthMonLanType,
       "cfprApFabricEthMonSrcEpTable": cfprApFabricEthMonSrcEpTable,
       "cfprApFabricEthMonSrcEpEntry": cfprApFabricEthMonSrcEpEntry,
       "cfprApFabricEthMonSrcEpInstanceId": cfprApFabricEthMonSrcEpInstanceId,
       "cfprApFabricEthMonSrcEpDn": cfprApFabricEthMonSrcEpDn,
       "cfprApFabricEthMonSrcEpRn": cfprApFabricEthMonSrcEpRn,
       "cfprApFabricEthMonSrcEpDirection": cfprApFabricEthMonSrcEpDirection,
       "cfprApFabricEthMonSrcEpName": cfprApFabricEthMonSrcEpName,
       "cfprApFabricEthMonSrcEpSession": cfprApFabricEthMonSrcEpSession,
       "cfprApFabricEthMonSrcEpTransport": cfprApFabricEthMonSrcEpTransport,
       "cfprApFabricEthMonSrcEpType": cfprApFabricEthMonSrcEpType,
       "cfprApFabricEthMonSrcRefTable": cfprApFabricEthMonSrcRefTable,
       "cfprApFabricEthMonSrcRefEntry": cfprApFabricEthMonSrcRefEntry,
       "cfprApFabricEthMonSrcRefInstanceId": cfprApFabricEthMonSrcRefInstanceId,
       "cfprApFabricEthMonSrcRefDn": cfprApFabricEthMonSrcRefDn,
       "cfprApFabricEthMonSrcRefRn": cfprApFabricEthMonSrcRefRn,
       "cfprApFabricEthMonSrcRefId": cfprApFabricEthMonSrcRefId,
       "cfprApFabricEthMonSrcRefSourceDn": cfprApFabricEthMonSrcRefSourceDn,
       "cfprApFabricEthMonSrcRefSourceType": cfprApFabricEthMonSrcRefSourceType,
       "cfprApFabricEthMonSrcRefType": cfprApFabricEthMonSrcRefType,
       "cfprApFabricEthTargetEpTable": cfprApFabricEthTargetEpTable,
       "cfprApFabricEthTargetEpEntry": cfprApFabricEthTargetEpEntry,
       "cfprApFabricEthTargetEpInstanceId": cfprApFabricEthTargetEpInstanceId,
       "cfprApFabricEthTargetEpDn": cfprApFabricEthTargetEpDn,
       "cfprApFabricEthTargetEpRn": cfprApFabricEthTargetEpRn,
       "cfprApFabricEthTargetEpAdminState": cfprApFabricEthTargetEpAdminState,
       "cfprApFabricEthTargetEpAggrPortId": cfprApFabricEthTargetEpAggrPortId,
       "cfprApFabricEthTargetEpChassisId": cfprApFabricEthTargetEpChassisId,
       "cfprApFabricEthTargetEpEpDn": cfprApFabricEthTargetEpEpDn,
       "cfprApFabricEthTargetEpFltAggr": cfprApFabricEthTargetEpFltAggr,
       "cfprApFabricEthTargetEpIfRole": cfprApFabricEthTargetEpIfRole,
       "cfprApFabricEthTargetEpIfType": cfprApFabricEthTargetEpIfType,
       "cfprApFabricEthTargetEpLicGP": cfprApFabricEthTargetEpLicGP,
       "cfprApFabricEthTargetEpLicState": cfprApFabricEthTargetEpLicState,
       "cfprApFabricEthTargetEpLocale": cfprApFabricEthTargetEpLocale,
       "cfprApFabricEthTargetEpMacAddress": cfprApFabricEthTargetEpMacAddress,
       "cfprApFabricEthTargetEpName": cfprApFabricEthTargetEpName,
       "cfprApFabricEthTargetEpOperState": cfprApFabricEthTargetEpOperState,
       "cfprApFabricEthTargetEpOperStateReason": cfprApFabricEthTargetEpOperStateReason,
       "cfprApFabricEthTargetEpPeerAggrPortId": cfprApFabricEthTargetEpPeerAggrPortId,
       "cfprApFabricEthTargetEpPeerChassisId": cfprApFabricEthTargetEpPeerChassisId,
       "cfprApFabricEthTargetEpPeerDn": cfprApFabricEthTargetEpPeerDn,
       "cfprApFabricEthTargetEpPeerPortId": cfprApFabricEthTargetEpPeerPortId,
       "cfprApFabricEthTargetEpPeerSlotId": cfprApFabricEthTargetEpPeerSlotId,
       "cfprApFabricEthTargetEpPortId": cfprApFabricEthTargetEpPortId,
       "cfprApFabricEthTargetEpSlotId": cfprApFabricEthTargetEpSlotId,
       "cfprApFabricEthTargetEpSwitchId": cfprApFabricEthTargetEpSwitchId,
       "cfprApFabricEthTargetEpTransport": cfprApFabricEthTargetEpTransport,
       "cfprApFabricEthTargetEpType": cfprApFabricEthTargetEpType,
       "cfprApFabricEthTargetEpWarnings": cfprApFabricEthTargetEpWarnings,
       "cfprApFabricEthVlanPcTable": cfprApFabricEthVlanPcTable,
       "cfprApFabricEthVlanPcEntry": cfprApFabricEthVlanPcEntry,
       "cfprApFabricEthVlanPcInstanceId": cfprApFabricEthVlanPcInstanceId,
       "cfprApFabricEthVlanPcDn": cfprApFabricEthVlanPcDn,
       "cfprApFabricEthVlanPcRn": cfprApFabricEthVlanPcRn,
       "cfprApFabricEthVlanPcAdminSpeed": cfprApFabricEthVlanPcAdminSpeed,
       "cfprApFabricEthVlanPcAdminState": cfprApFabricEthVlanPcAdminState,
       "cfprApFabricEthVlanPcDescr": cfprApFabricEthVlanPcDescr,
       "cfprApFabricEthVlanPcEpDn": cfprApFabricEthVlanPcEpDn,
       "cfprApFabricEthVlanPcFltAggr": cfprApFabricEthVlanPcFltAggr,
       "cfprApFabricEthVlanPcIfRole": cfprApFabricEthVlanPcIfRole,
       "cfprApFabricEthVlanPcIfType": cfprApFabricEthVlanPcIfType,
       "cfprApFabricEthVlanPcIsNative": cfprApFabricEthVlanPcIsNative,
       "cfprApFabricEthVlanPcLocale": cfprApFabricEthVlanPcLocale,
       "cfprApFabricEthVlanPcName": cfprApFabricEthVlanPcName,
       "cfprApFabricEthVlanPcOperSpeed": cfprApFabricEthVlanPcOperSpeed,
       "cfprApFabricEthVlanPcOperState": cfprApFabricEthVlanPcOperState,
       "cfprApFabricEthVlanPcPeerDn": cfprApFabricEthVlanPcPeerDn,
       "cfprApFabricEthVlanPcPortId": cfprApFabricEthVlanPcPortId,
       "cfprApFabricEthVlanPcStateQual": cfprApFabricEthVlanPcStateQual,
       "cfprApFabricEthVlanPcSwitchId": cfprApFabricEthVlanPcSwitchId,
       "cfprApFabricEthVlanPcTransport": cfprApFabricEthVlanPcTransport,
       "cfprApFabricEthVlanPcType": cfprApFabricEthVlanPcType,
       "cfprApFabricEthVlanPcWarnings": cfprApFabricEthVlanPcWarnings,
       "cfprApFabricEthVlanPortEpTable": cfprApFabricEthVlanPortEpTable,
       "cfprApFabricEthVlanPortEpEntry": cfprApFabricEthVlanPortEpEntry,
       "cfprApFabricEthVlanPortEpInstanceId": cfprApFabricEthVlanPortEpInstanceId,
       "cfprApFabricEthVlanPortEpDn": cfprApFabricEthVlanPortEpDn,
       "cfprApFabricEthVlanPortEpRn": cfprApFabricEthVlanPortEpRn,
       "cfprApFabricEthVlanPortEpAdminState": cfprApFabricEthVlanPortEpAdminState,
       "cfprApFabricEthVlanPortEpAggrPortId": cfprApFabricEthVlanPortEpAggrPortId,
       "cfprApFabricEthVlanPortEpChassisId": cfprApFabricEthVlanPortEpChassisId,
       "cfprApFabricEthVlanPortEpEpDn": cfprApFabricEthVlanPortEpEpDn,
       "cfprApFabricEthVlanPortEpFltAggr": cfprApFabricEthVlanPortEpFltAggr,
       "cfprApFabricEthVlanPortEpIfRole": cfprApFabricEthVlanPortEpIfRole,
       "cfprApFabricEthVlanPortEpIfType": cfprApFabricEthVlanPortEpIfType,
       "cfprApFabricEthVlanPortEpIsNative": cfprApFabricEthVlanPortEpIsNative,
       "cfprApFabricEthVlanPortEpLicGP": cfprApFabricEthVlanPortEpLicGP,
       "cfprApFabricEthVlanPortEpLicState": cfprApFabricEthVlanPortEpLicState,
       "cfprApFabricEthVlanPortEpLocale": cfprApFabricEthVlanPortEpLocale,
       "cfprApFabricEthVlanPortEpName": cfprApFabricEthVlanPortEpName,
       "cfprApFabricEthVlanPortEpOperState": cfprApFabricEthVlanPortEpOperState,
       "cfprApFabricEthVlanPortEpOperStateReason": cfprApFabricEthVlanPortEpOperStateReason,
       "cfprApFabricEthVlanPortEpPeerAggrPortId": cfprApFabricEthVlanPortEpPeerAggrPortId,
       "cfprApFabricEthVlanPortEpPeerChassisId": cfprApFabricEthVlanPortEpPeerChassisId,
       "cfprApFabricEthVlanPortEpPeerDn": cfprApFabricEthVlanPortEpPeerDn,
       "cfprApFabricEthVlanPortEpPeerPortId": cfprApFabricEthVlanPortEpPeerPortId,
       "cfprApFabricEthVlanPortEpPeerSlotId": cfprApFabricEthVlanPortEpPeerSlotId,
       "cfprApFabricEthVlanPortEpPortId": cfprApFabricEthVlanPortEpPortId,
       "cfprApFabricEthVlanPortEpSlotId": cfprApFabricEthVlanPortEpSlotId,
       "cfprApFabricEthVlanPortEpSwitchId": cfprApFabricEthVlanPortEpSwitchId,
       "cfprApFabricEthVlanPortEpTransport": cfprApFabricEthVlanPortEpTransport,
       "cfprApFabricEthVlanPortEpType": cfprApFabricEthVlanPortEpType,
       "cfprApFabricEthVlanPortEpWarnings": cfprApFabricEthVlanPortEpWarnings,
       "cfprApFabricFcSanTable": cfprApFabricFcSanTable,
       "cfprApFabricFcSanEntry": cfprApFabricFcSanEntry,
       "cfprApFabricFcSanInstanceId": cfprApFabricFcSanInstanceId,
       "cfprApFabricFcSanDn": cfprApFabricFcSanDn,
       "cfprApFabricFcSanRn": cfprApFabricFcSanRn,
       "cfprApFabricFcSanId": cfprApFabricFcSanId,
       "cfprApFabricFcSanLocale": cfprApFabricFcSanLocale,
       "cfprApFabricFcSanName": cfprApFabricFcSanName,
       "cfprApFabricFcSanTransport": cfprApFabricFcSanTransport,
       "cfprApFabricFcSanType": cfprApFabricFcSanType,
       "cfprApFabricFcSanUplinkTrunking": cfprApFabricFcSanUplinkTrunking,
       "cfprApFabricFcSanEpTable": cfprApFabricFcSanEpTable,
       "cfprApFabricFcSanEpEntry": cfprApFabricFcSanEpEntry,
       "cfprApFabricFcSanEpInstanceId": cfprApFabricFcSanEpInstanceId,
       "cfprApFabricFcSanEpDn": cfprApFabricFcSanEpDn,
       "cfprApFabricFcSanEpRn": cfprApFabricFcSanEpRn,
       "cfprApFabricFcSanEpAdminState": cfprApFabricFcSanEpAdminState,
       "cfprApFabricFcSanEpAggrPortId": cfprApFabricFcSanEpAggrPortId,
       "cfprApFabricFcSanEpChassisId": cfprApFabricFcSanEpChassisId,
       "cfprApFabricFcSanEpEpDn": cfprApFabricFcSanEpEpDn,
       "cfprApFabricFcSanEpFillPattern": cfprApFabricFcSanEpFillPattern,
       "cfprApFabricFcSanEpFltAggr": cfprApFabricFcSanEpFltAggr,
       "cfprApFabricFcSanEpIfRole": cfprApFabricFcSanEpIfRole,
       "cfprApFabricFcSanEpIfType": cfprApFabricFcSanEpIfType,
       "cfprApFabricFcSanEpLicGP": cfprApFabricFcSanEpLicGP,
       "cfprApFabricFcSanEpLicState": cfprApFabricFcSanEpLicState,
       "cfprApFabricFcSanEpLocale": cfprApFabricFcSanEpLocale,
       "cfprApFabricFcSanEpName": cfprApFabricFcSanEpName,
       "cfprApFabricFcSanEpOperState": cfprApFabricFcSanEpOperState,
       "cfprApFabricFcSanEpOperStateReason": cfprApFabricFcSanEpOperStateReason,
       "cfprApFabricFcSanEpPeerAggrPortId": cfprApFabricFcSanEpPeerAggrPortId,
       "cfprApFabricFcSanEpPeerChassisId": cfprApFabricFcSanEpPeerChassisId,
       "cfprApFabricFcSanEpPeerDn": cfprApFabricFcSanEpPeerDn,
       "cfprApFabricFcSanEpPeerPortId": cfprApFabricFcSanEpPeerPortId,
       "cfprApFabricFcSanEpPeerSlotId": cfprApFabricFcSanEpPeerSlotId,
       "cfprApFabricFcSanEpPortId": cfprApFabricFcSanEpPortId,
       "cfprApFabricFcSanEpSlotId": cfprApFabricFcSanEpSlotId,
       "cfprApFabricFcSanEpSwitchId": cfprApFabricFcSanEpSwitchId,
       "cfprApFabricFcSanEpTransport": cfprApFabricFcSanEpTransport,
       "cfprApFabricFcSanEpType": cfprApFabricFcSanEpType,
       "cfprApFabricFcSanEpUsrLbl": cfprApFabricFcSanEpUsrLbl,
       "cfprApFabricFcSanEpWarnings": cfprApFabricFcSanEpWarnings,
       "cfprApFabricFcSanPcTable": cfprApFabricFcSanPcTable,
       "cfprApFabricFcSanPcEntry": cfprApFabricFcSanPcEntry,
       "cfprApFabricFcSanPcInstanceId": cfprApFabricFcSanPcInstanceId,
       "cfprApFabricFcSanPcDn": cfprApFabricFcSanPcDn,
       "cfprApFabricFcSanPcRn": cfprApFabricFcSanPcRn,
       "cfprApFabricFcSanPcAdminSpeed": cfprApFabricFcSanPcAdminSpeed,
       "cfprApFabricFcSanPcAdminState": cfprApFabricFcSanPcAdminState,
       "cfprApFabricFcSanPcConfigState": cfprApFabricFcSanPcConfigState,
       "cfprApFabricFcSanPcConfigStatus": cfprApFabricFcSanPcConfigStatus,
       "cfprApFabricFcSanPcDescr": cfprApFabricFcSanPcDescr,
       "cfprApFabricFcSanPcEpDn": cfprApFabricFcSanPcEpDn,
       "cfprApFabricFcSanPcFltAggr": cfprApFabricFcSanPcFltAggr,
       "cfprApFabricFcSanPcIfRole": cfprApFabricFcSanPcIfRole,
       "cfprApFabricFcSanPcIfType": cfprApFabricFcSanPcIfType,
       "cfprApFabricFcSanPcLocale": cfprApFabricFcSanPcLocale,
       "cfprApFabricFcSanPcName": cfprApFabricFcSanPcName,
       "cfprApFabricFcSanPcOperSpeed": cfprApFabricFcSanPcOperSpeed,
       "cfprApFabricFcSanPcOperState": cfprApFabricFcSanPcOperState,
       "cfprApFabricFcSanPcPeerDn": cfprApFabricFcSanPcPeerDn,
       "cfprApFabricFcSanPcPortId": cfprApFabricFcSanPcPortId,
       "cfprApFabricFcSanPcStateQual": cfprApFabricFcSanPcStateQual,
       "cfprApFabricFcSanPcSwitchId": cfprApFabricFcSanPcSwitchId,
       "cfprApFabricFcSanPcTransport": cfprApFabricFcSanPcTransport,
       "cfprApFabricFcSanPcType": cfprApFabricFcSanPcType,
       "cfprApFabricFcSanPcWarnings": cfprApFabricFcSanPcWarnings,
       "cfprApFabricFcSanPcEpTable": cfprApFabricFcSanPcEpTable,
       "cfprApFabricFcSanPcEpEntry": cfprApFabricFcSanPcEpEntry,
       "cfprApFabricFcSanPcEpInstanceId": cfprApFabricFcSanPcEpInstanceId,
       "cfprApFabricFcSanPcEpDnData": cfprApFabricFcSanPcEpDnData,
       "cfprApFabricFcSanPcEpRn": cfprApFabricFcSanPcEpRn,
       "cfprApFabricFcSanPcEpAdminSpeed": cfprApFabricFcSanPcEpAdminSpeed,
       "cfprApFabricFcSanPcEpAdminState": cfprApFabricFcSanPcEpAdminState,
       "cfprApFabricFcSanPcEpAggrPortId": cfprApFabricFcSanPcEpAggrPortId,
       "cfprApFabricFcSanPcEpChassisId": cfprApFabricFcSanPcEpChassisId,
       "cfprApFabricFcSanPcEpEpDn": cfprApFabricFcSanPcEpEpDn,
       "cfprApFabricFcSanPcEpFillPattern": cfprApFabricFcSanPcEpFillPattern,
       "cfprApFabricFcSanPcEpFltAggr": cfprApFabricFcSanPcEpFltAggr,
       "cfprApFabricFcSanPcEpIfRole": cfprApFabricFcSanPcEpIfRole,
       "cfprApFabricFcSanPcEpIfType": cfprApFabricFcSanPcEpIfType,
       "cfprApFabricFcSanPcEpLicGP": cfprApFabricFcSanPcEpLicGP,
       "cfprApFabricFcSanPcEpLicState": cfprApFabricFcSanPcEpLicState,
       "cfprApFabricFcSanPcEpLocale": cfprApFabricFcSanPcEpLocale,
       "cfprApFabricFcSanPcEpMembership": cfprApFabricFcSanPcEpMembership,
       "cfprApFabricFcSanPcEpName": cfprApFabricFcSanPcEpName,
       "cfprApFabricFcSanPcEpOperState": cfprApFabricFcSanPcEpOperState,
       "cfprApFabricFcSanPcEpOperStateReason": cfprApFabricFcSanPcEpOperStateReason,
       "cfprApFabricFcSanPcEpPeerAggrPortId": cfprApFabricFcSanPcEpPeerAggrPortId,
       "cfprApFabricFcSanPcEpPeerChassisId": cfprApFabricFcSanPcEpPeerChassisId,
       "cfprApFabricFcSanPcEpPeerDn": cfprApFabricFcSanPcEpPeerDn,
       "cfprApFabricFcSanPcEpPeerPortId": cfprApFabricFcSanPcEpPeerPortId,
       "cfprApFabricFcSanPcEpPeerSlotId": cfprApFabricFcSanPcEpPeerSlotId,
       "cfprApFabricFcSanPcEpPortId": cfprApFabricFcSanPcEpPortId,
       "cfprApFabricFcSanPcEpSlotId": cfprApFabricFcSanPcEpSlotId,
       "cfprApFabricFcSanPcEpSwitchId": cfprApFabricFcSanPcEpSwitchId,
       "cfprApFabricFcSanPcEpTransport": cfprApFabricFcSanPcEpTransport,
       "cfprApFabricFcSanPcEpType": cfprApFabricFcSanPcEpType,
       "cfprApFabricFcSanPcEpWarnings": cfprApFabricFcSanPcEpWarnings,
       "cfprApFabricFcVsanPcTable": cfprApFabricFcVsanPcTable,
       "cfprApFabricFcVsanPcEntry": cfprApFabricFcVsanPcEntry,
       "cfprApFabricFcVsanPcInstanceId": cfprApFabricFcVsanPcInstanceId,
       "cfprApFabricFcVsanPcDn": cfprApFabricFcVsanPcDn,
       "cfprApFabricFcVsanPcRn": cfprApFabricFcVsanPcRn,
       "cfprApFabricFcVsanPcAdminState": cfprApFabricFcVsanPcAdminState,
       "cfprApFabricFcVsanPcDescr": cfprApFabricFcVsanPcDescr,
       "cfprApFabricFcVsanPcEpDn": cfprApFabricFcVsanPcEpDn,
       "cfprApFabricFcVsanPcFltAggr": cfprApFabricFcVsanPcFltAggr,
       "cfprApFabricFcVsanPcIfRole": cfprApFabricFcVsanPcIfRole,
       "cfprApFabricFcVsanPcIfType": cfprApFabricFcVsanPcIfType,
       "cfprApFabricFcVsanPcLocale": cfprApFabricFcVsanPcLocale,
       "cfprApFabricFcVsanPcName": cfprApFabricFcVsanPcName,
       "cfprApFabricFcVsanPcOperState": cfprApFabricFcVsanPcOperState,
       "cfprApFabricFcVsanPcPeerDn": cfprApFabricFcVsanPcPeerDn,
       "cfprApFabricFcVsanPcPortId": cfprApFabricFcVsanPcPortId,
       "cfprApFabricFcVsanPcStateQual": cfprApFabricFcVsanPcStateQual,
       "cfprApFabricFcVsanPcSwitchId": cfprApFabricFcVsanPcSwitchId,
       "cfprApFabricFcVsanPcTransport": cfprApFabricFcVsanPcTransport,
       "cfprApFabricFcVsanPcType": cfprApFabricFcVsanPcType,
       "cfprApFabricFcVsanPcWarnings": cfprApFabricFcVsanPcWarnings,
       "cfprApFabricFcVsanPortEpTable": cfprApFabricFcVsanPortEpTable,
       "cfprApFabricFcVsanPortEpEntry": cfprApFabricFcVsanPortEpEntry,
       "cfprApFabricFcVsanPortEpInstanceId": cfprApFabricFcVsanPortEpInstanceId,
       "cfprApFabricFcVsanPortEpDn": cfprApFabricFcVsanPortEpDn,
       "cfprApFabricFcVsanPortEpRn": cfprApFabricFcVsanPortEpRn,
       "cfprApFabricFcVsanPortEpAdminState": cfprApFabricFcVsanPortEpAdminState,
       "cfprApFabricFcVsanPortEpAggrPortId": cfprApFabricFcVsanPortEpAggrPortId,
       "cfprApFabricFcVsanPortEpChassisId": cfprApFabricFcVsanPortEpChassisId,
       "cfprApFabricFcVsanPortEpEpDn": cfprApFabricFcVsanPortEpEpDn,
       "cfprApFabricFcVsanPortEpFltAggr": cfprApFabricFcVsanPortEpFltAggr,
       "cfprApFabricFcVsanPortEpIfRole": cfprApFabricFcVsanPortEpIfRole,
       "cfprApFabricFcVsanPortEpIfType": cfprApFabricFcVsanPortEpIfType,
       "cfprApFabricFcVsanPortEpLicGP": cfprApFabricFcVsanPortEpLicGP,
       "cfprApFabricFcVsanPortEpLicState": cfprApFabricFcVsanPortEpLicState,
       "cfprApFabricFcVsanPortEpLocale": cfprApFabricFcVsanPortEpLocale,
       "cfprApFabricFcVsanPortEpName": cfprApFabricFcVsanPortEpName,
       "cfprApFabricFcVsanPortEpOperState": cfprApFabricFcVsanPortEpOperState,
       "cfprApFabricFcVsanPortEpOperStateReason": cfprApFabricFcVsanPortEpOperStateReason,
       "cfprApFabricFcVsanPortEpPeerAggrPortId": cfprApFabricFcVsanPortEpPeerAggrPortId,
       "cfprApFabricFcVsanPortEpPeerChassisId": cfprApFabricFcVsanPortEpPeerChassisId,
       "cfprApFabricFcVsanPortEpPeerDn": cfprApFabricFcVsanPortEpPeerDn,
       "cfprApFabricFcVsanPortEpPeerPortId": cfprApFabricFcVsanPortEpPeerPortId,
       "cfprApFabricFcVsanPortEpPeerSlotId": cfprApFabricFcVsanPortEpPeerSlotId,
       "cfprApFabricFcVsanPortEpPortId": cfprApFabricFcVsanPortEpPortId,
       "cfprApFabricFcVsanPortEpSlotId": cfprApFabricFcVsanPortEpSlotId,
       "cfprApFabricFcVsanPortEpSwitchId": cfprApFabricFcVsanPortEpSwitchId,
       "cfprApFabricFcVsanPortEpTransport": cfprApFabricFcVsanPortEpTransport,
       "cfprApFabricFcVsanPortEpType": cfprApFabricFcVsanPortEpType,
       "cfprApFabricFcVsanPortEpWarnings": cfprApFabricFcVsanPortEpWarnings,
       "cfprApFabricFcoeSanEpTable": cfprApFabricFcoeSanEpTable,
       "cfprApFabricFcoeSanEpEntry": cfprApFabricFcoeSanEpEntry,
       "cfprApFabricFcoeSanEpInstanceId": cfprApFabricFcoeSanEpInstanceId,
       "cfprApFabricFcoeSanEpDn": cfprApFabricFcoeSanEpDn,
       "cfprApFabricFcoeSanEpRn": cfprApFabricFcoeSanEpRn,
       "cfprApFabricFcoeSanEpAdminState": cfprApFabricFcoeSanEpAdminState,
       "cfprApFabricFcoeSanEpAggrPortId": cfprApFabricFcoeSanEpAggrPortId,
       "cfprApFabricFcoeSanEpChassisId": cfprApFabricFcoeSanEpChassisId,
       "cfprApFabricFcoeSanEpConfigState": cfprApFabricFcoeSanEpConfigState,
       "cfprApFabricFcoeSanEpEpDn": cfprApFabricFcoeSanEpEpDn,
       "cfprApFabricFcoeSanEpEthLinkProfileName": cfprApFabricFcoeSanEpEthLinkProfileName,
       "cfprApFabricFcoeSanEpFcoeState": cfprApFabricFcoeSanEpFcoeState,
       "cfprApFabricFcoeSanEpFcoeStateReason": cfprApFabricFcoeSanEpFcoeStateReason,
       "cfprApFabricFcoeSanEpFltAggr": cfprApFabricFcoeSanEpFltAggr,
       "cfprApFabricFcoeSanEpIfRole": cfprApFabricFcoeSanEpIfRole,
       "cfprApFabricFcoeSanEpIfType": cfprApFabricFcoeSanEpIfType,
       "cfprApFabricFcoeSanEpLicGP": cfprApFabricFcoeSanEpLicGP,
       "cfprApFabricFcoeSanEpLicState": cfprApFabricFcoeSanEpLicState,
       "cfprApFabricFcoeSanEpLocale": cfprApFabricFcoeSanEpLocale,
       "cfprApFabricFcoeSanEpName": cfprApFabricFcoeSanEpName,
       "cfprApFabricFcoeSanEpOperEthLinkProfileName": cfprApFabricFcoeSanEpOperEthLinkProfileName,
       "cfprApFabricFcoeSanEpOperState": cfprApFabricFcoeSanEpOperState,
       "cfprApFabricFcoeSanEpOperStateReason": cfprApFabricFcoeSanEpOperStateReason,
       "cfprApFabricFcoeSanEpPeerAggrPortId": cfprApFabricFcoeSanEpPeerAggrPortId,
       "cfprApFabricFcoeSanEpPeerChassisId": cfprApFabricFcoeSanEpPeerChassisId,
       "cfprApFabricFcoeSanEpPeerDn": cfprApFabricFcoeSanEpPeerDn,
       "cfprApFabricFcoeSanEpPeerPortId": cfprApFabricFcoeSanEpPeerPortId,
       "cfprApFabricFcoeSanEpPeerSlotId": cfprApFabricFcoeSanEpPeerSlotId,
       "cfprApFabricFcoeSanEpPortId": cfprApFabricFcoeSanEpPortId,
       "cfprApFabricFcoeSanEpSlotId": cfprApFabricFcoeSanEpSlotId,
       "cfprApFabricFcoeSanEpSwitchId": cfprApFabricFcoeSanEpSwitchId,
       "cfprApFabricFcoeSanEpTransport": cfprApFabricFcoeSanEpTransport,
       "cfprApFabricFcoeSanEpType": cfprApFabricFcoeSanEpType,
       "cfprApFabricFcoeSanEpUdldOperState": cfprApFabricFcoeSanEpUdldOperState,
       "cfprApFabricFcoeSanEpUsrLbl": cfprApFabricFcoeSanEpUsrLbl,
       "cfprApFabricFcoeSanEpWarnings": cfprApFabricFcoeSanEpWarnings,
       "cfprApFabricFcoeSanPcTable": cfprApFabricFcoeSanPcTable,
       "cfprApFabricFcoeSanPcEntry": cfprApFabricFcoeSanPcEntry,
       "cfprApFabricFcoeSanPcInstanceId": cfprApFabricFcoeSanPcInstanceId,
       "cfprApFabricFcoeSanPcDn": cfprApFabricFcoeSanPcDn,
       "cfprApFabricFcoeSanPcRn": cfprApFabricFcoeSanPcRn,
       "cfprApFabricFcoeSanPcAdminState": cfprApFabricFcoeSanPcAdminState,
       "cfprApFabricFcoeSanPcConfigState": cfprApFabricFcoeSanPcConfigState,
       "cfprApFabricFcoeSanPcDescr": cfprApFabricFcoeSanPcDescr,
       "cfprApFabricFcoeSanPcEpDn": cfprApFabricFcoeSanPcEpDn,
       "cfprApFabricFcoeSanPcFcoeState": cfprApFabricFcoeSanPcFcoeState,
       "cfprApFabricFcoeSanPcFcoeStateReason": cfprApFabricFcoeSanPcFcoeStateReason,
       "cfprApFabricFcoeSanPcFltAggr": cfprApFabricFcoeSanPcFltAggr,
       "cfprApFabricFcoeSanPcIfRole": cfprApFabricFcoeSanPcIfRole,
       "cfprApFabricFcoeSanPcIfType": cfprApFabricFcoeSanPcIfType,
       "cfprApFabricFcoeSanPcLacpPolicyName": cfprApFabricFcoeSanPcLacpPolicyName,
       "cfprApFabricFcoeSanPcLocale": cfprApFabricFcoeSanPcLocale,
       "cfprApFabricFcoeSanPcName": cfprApFabricFcoeSanPcName,
       "cfprApFabricFcoeSanPcOperLacpPolicyName": cfprApFabricFcoeSanPcOperLacpPolicyName,
       "cfprApFabricFcoeSanPcOperState": cfprApFabricFcoeSanPcOperState,
       "cfprApFabricFcoeSanPcPeerDn": cfprApFabricFcoeSanPcPeerDn,
       "cfprApFabricFcoeSanPcPortId": cfprApFabricFcoeSanPcPortId,
       "cfprApFabricFcoeSanPcStateQual": cfprApFabricFcoeSanPcStateQual,
       "cfprApFabricFcoeSanPcSwitchId": cfprApFabricFcoeSanPcSwitchId,
       "cfprApFabricFcoeSanPcTransport": cfprApFabricFcoeSanPcTransport,
       "cfprApFabricFcoeSanPcType": cfprApFabricFcoeSanPcType,
       "cfprApFabricFcoeSanPcWarnings": cfprApFabricFcoeSanPcWarnings,
       "cfprApFabricFcoeSanPcEpTable": cfprApFabricFcoeSanPcEpTable,
       "cfprApFabricFcoeSanPcEpEntry": cfprApFabricFcoeSanPcEpEntry,
       "cfprApFabricFcoeSanPcEpInstanceId": cfprApFabricFcoeSanPcEpInstanceId,
       "cfprApFabricFcoeSanPcEpDnData": cfprApFabricFcoeSanPcEpDnData,
       "cfprApFabricFcoeSanPcEpRn": cfprApFabricFcoeSanPcEpRn,
       "cfprApFabricFcoeSanPcEpAdminState": cfprApFabricFcoeSanPcEpAdminState,
       "cfprApFabricFcoeSanPcEpAggrPortId": cfprApFabricFcoeSanPcEpAggrPortId,
       "cfprApFabricFcoeSanPcEpChassisId": cfprApFabricFcoeSanPcEpChassisId,
       "cfprApFabricFcoeSanPcEpEpDn": cfprApFabricFcoeSanPcEpEpDn,
       "cfprApFabricFcoeSanPcEpEthLinkProfileName": cfprApFabricFcoeSanPcEpEthLinkProfileName,
       "cfprApFabricFcoeSanPcEpFltAggr": cfprApFabricFcoeSanPcEpFltAggr,
       "cfprApFabricFcoeSanPcEpIfRole": cfprApFabricFcoeSanPcEpIfRole,
       "cfprApFabricFcoeSanPcEpIfType": cfprApFabricFcoeSanPcEpIfType,
       "cfprApFabricFcoeSanPcEpLicGP": cfprApFabricFcoeSanPcEpLicGP,
       "cfprApFabricFcoeSanPcEpLicState": cfprApFabricFcoeSanPcEpLicState,
       "cfprApFabricFcoeSanPcEpLocale": cfprApFabricFcoeSanPcEpLocale,
       "cfprApFabricFcoeSanPcEpMembership": cfprApFabricFcoeSanPcEpMembership,
       "cfprApFabricFcoeSanPcEpName": cfprApFabricFcoeSanPcEpName,
       "cfprApFabricFcoeSanPcEpOperEthLinkProfileName": cfprApFabricFcoeSanPcEpOperEthLinkProfileName,
       "cfprApFabricFcoeSanPcEpOperState": cfprApFabricFcoeSanPcEpOperState,
       "cfprApFabricFcoeSanPcEpOperStateReason": cfprApFabricFcoeSanPcEpOperStateReason,
       "cfprApFabricFcoeSanPcEpPeerAggrPortId": cfprApFabricFcoeSanPcEpPeerAggrPortId,
       "cfprApFabricFcoeSanPcEpPeerChassisId": cfprApFabricFcoeSanPcEpPeerChassisId,
       "cfprApFabricFcoeSanPcEpPeerDn": cfprApFabricFcoeSanPcEpPeerDn,
       "cfprApFabricFcoeSanPcEpPeerPortId": cfprApFabricFcoeSanPcEpPeerPortId,
       "cfprApFabricFcoeSanPcEpPeerSlotId": cfprApFabricFcoeSanPcEpPeerSlotId,
       "cfprApFabricFcoeSanPcEpPortId": cfprApFabricFcoeSanPcEpPortId,
       "cfprApFabricFcoeSanPcEpSlotId": cfprApFabricFcoeSanPcEpSlotId,
       "cfprApFabricFcoeSanPcEpSwitchId": cfprApFabricFcoeSanPcEpSwitchId,
       "cfprApFabricFcoeSanPcEpTransport": cfprApFabricFcoeSanPcEpTransport,
       "cfprApFabricFcoeSanPcEpType": cfprApFabricFcoeSanPcEpType,
       "cfprApFabricFcoeSanPcEpUdldOperState": cfprApFabricFcoeSanPcEpUdldOperState,
       "cfprApFabricFcoeSanPcEpWarnings": cfprApFabricFcoeSanPcEpWarnings,
       "cfprApFabricFcoeVsanPcTable": cfprApFabricFcoeVsanPcTable,
       "cfprApFabricFcoeVsanPcEntry": cfprApFabricFcoeVsanPcEntry,
       "cfprApFabricFcoeVsanPcInstanceId": cfprApFabricFcoeVsanPcInstanceId,
       "cfprApFabricFcoeVsanPcDn": cfprApFabricFcoeVsanPcDn,
       "cfprApFabricFcoeVsanPcRn": cfprApFabricFcoeVsanPcRn,
       "cfprApFabricFcoeVsanPcAdminState": cfprApFabricFcoeVsanPcAdminState,
       "cfprApFabricFcoeVsanPcDescr": cfprApFabricFcoeVsanPcDescr,
       "cfprApFabricFcoeVsanPcEpDn": cfprApFabricFcoeVsanPcEpDn,
       "cfprApFabricFcoeVsanPcFltAggr": cfprApFabricFcoeVsanPcFltAggr,
       "cfprApFabricFcoeVsanPcIfRole": cfprApFabricFcoeVsanPcIfRole,
       "cfprApFabricFcoeVsanPcIfType": cfprApFabricFcoeVsanPcIfType,
       "cfprApFabricFcoeVsanPcLocale": cfprApFabricFcoeVsanPcLocale,
       "cfprApFabricFcoeVsanPcName": cfprApFabricFcoeVsanPcName,
       "cfprApFabricFcoeVsanPcOperState": cfprApFabricFcoeVsanPcOperState,
       "cfprApFabricFcoeVsanPcPeerDn": cfprApFabricFcoeVsanPcPeerDn,
       "cfprApFabricFcoeVsanPcPortId": cfprApFabricFcoeVsanPcPortId,
       "cfprApFabricFcoeVsanPcStateQual": cfprApFabricFcoeVsanPcStateQual,
       "cfprApFabricFcoeVsanPcSwitchId": cfprApFabricFcoeVsanPcSwitchId,
       "cfprApFabricFcoeVsanPcTransport": cfprApFabricFcoeVsanPcTransport,
       "cfprApFabricFcoeVsanPcType": cfprApFabricFcoeVsanPcType,
       "cfprApFabricFcoeVsanPcWarnings": cfprApFabricFcoeVsanPcWarnings,
       "cfprApFabricFcoeVsanPortEpTable": cfprApFabricFcoeVsanPortEpTable,
       "cfprApFabricFcoeVsanPortEpEntry": cfprApFabricFcoeVsanPortEpEntry,
       "cfprApFabricFcoeVsanPortEpInstanceId": cfprApFabricFcoeVsanPortEpInstanceId,
       "cfprApFabricFcoeVsanPortEpDn": cfprApFabricFcoeVsanPortEpDn,
       "cfprApFabricFcoeVsanPortEpRn": cfprApFabricFcoeVsanPortEpRn,
       "cfprApFabricFcoeVsanPortEpAdminState": cfprApFabricFcoeVsanPortEpAdminState,
       "cfprApFabricFcoeVsanPortEpAggrPortId": cfprApFabricFcoeVsanPortEpAggrPortId,
       "cfprApFabricFcoeVsanPortEpChassisId": cfprApFabricFcoeVsanPortEpChassisId,
       "cfprApFabricFcoeVsanPortEpEpDn": cfprApFabricFcoeVsanPortEpEpDn,
       "cfprApFabricFcoeVsanPortEpFltAggr": cfprApFabricFcoeVsanPortEpFltAggr,
       "cfprApFabricFcoeVsanPortEpIfRole": cfprApFabricFcoeVsanPortEpIfRole,
       "cfprApFabricFcoeVsanPortEpIfType": cfprApFabricFcoeVsanPortEpIfType,
       "cfprApFabricFcoeVsanPortEpLicGP": cfprApFabricFcoeVsanPortEpLicGP,
       "cfprApFabricFcoeVsanPortEpLicState": cfprApFabricFcoeVsanPortEpLicState,
       "cfprApFabricFcoeVsanPortEpLocale": cfprApFabricFcoeVsanPortEpLocale,
       "cfprApFabricFcoeVsanPortEpName": cfprApFabricFcoeVsanPortEpName,
       "cfprApFabricFcoeVsanPortEpOperState": cfprApFabricFcoeVsanPortEpOperState,
       "cfprApFabricFcoeVsanPortEpOperStateReason": cfprApFabricFcoeVsanPortEpOperStateReason,
       "cfprApFabricFcoeVsanPortEpPeerAggrPortId": cfprApFabricFcoeVsanPortEpPeerAggrPortId,
       "cfprApFabricFcoeVsanPortEpPeerChassisId": cfprApFabricFcoeVsanPortEpPeerChassisId,
       "cfprApFabricFcoeVsanPortEpPeerDn": cfprApFabricFcoeVsanPortEpPeerDn,
       "cfprApFabricFcoeVsanPortEpPeerPortId": cfprApFabricFcoeVsanPortEpPeerPortId,
       "cfprApFabricFcoeVsanPortEpPeerSlotId": cfprApFabricFcoeVsanPortEpPeerSlotId,
       "cfprApFabricFcoeVsanPortEpPortId": cfprApFabricFcoeVsanPortEpPortId,
       "cfprApFabricFcoeVsanPortEpSlotId": cfprApFabricFcoeVsanPortEpSlotId,
       "cfprApFabricFcoeVsanPortEpSwitchId": cfprApFabricFcoeVsanPortEpSwitchId,
       "cfprApFabricFcoeVsanPortEpTransport": cfprApFabricFcoeVsanPortEpTransport,
       "cfprApFabricFcoeVsanPortEpType": cfprApFabricFcoeVsanPortEpType,
       "cfprApFabricFcoeVsanPortEpWarnings": cfprApFabricFcoeVsanPortEpWarnings,
       "cfprApFabricIfTable": cfprApFabricIfTable,
       "cfprApFabricIfEntry": cfprApFabricIfEntry,
       "cfprApFabricIfInstanceId": cfprApFabricIfInstanceId,
       "cfprApFabricIfDn": cfprApFabricIfDn,
       "cfprApFabricIfRn": cfprApFabricIfRn,
       "cfprApFabricIfAddr": cfprApFabricIfAddr,
       "cfprApFabricIfId": cfprApFabricIfId,
       "cfprApFabricLacpPolicyTable": cfprApFabricLacpPolicyTable,
       "cfprApFabricLacpPolicyEntry": cfprApFabricLacpPolicyEntry,
       "cfprApFabricLacpPolicyInstanceId": cfprApFabricLacpPolicyInstanceId,
       "cfprApFabricLacpPolicyDn": cfprApFabricLacpPolicyDn,
       "cfprApFabricLacpPolicyRn": cfprApFabricLacpPolicyRn,
       "cfprApFabricLacpPolicyDescr": cfprApFabricLacpPolicyDescr,
       "cfprApFabricLacpPolicyFastTimer": cfprApFabricLacpPolicyFastTimer,
       "cfprApFabricLacpPolicyIntId": cfprApFabricLacpPolicyIntId,
       "cfprApFabricLacpPolicyName": cfprApFabricLacpPolicyName,
       "cfprApFabricLacpPolicyPolicyLevel": cfprApFabricLacpPolicyPolicyLevel,
       "cfprApFabricLacpPolicyPolicyOwner": cfprApFabricLacpPolicyPolicyOwner,
       "cfprApFabricLacpPolicySuspendIndividual": cfprApFabricLacpPolicySuspendIndividual,
       "cfprApFabricLanAccessMgrTable": cfprApFabricLanAccessMgrTable,
       "cfprApFabricLanAccessMgrEntry": cfprApFabricLanAccessMgrEntry,
       "cfprApFabricLanAccessMgrInstanceId": cfprApFabricLanAccessMgrInstanceId,
       "cfprApFabricLanAccessMgrDn": cfprApFabricLanAccessMgrDn,
       "cfprApFabricLanAccessMgrRn": cfprApFabricLanAccessMgrRn,
       "cfprApFabricLanCloudTable": cfprApFabricLanCloudTable,
       "cfprApFabricLanCloudEntry": cfprApFabricLanCloudEntry,
       "cfprApFabricLanCloudInstanceId": cfprApFabricLanCloudInstanceId,
       "cfprApFabricLanCloudDn": cfprApFabricLanCloudDn,
       "cfprApFabricLanCloudRn": cfprApFabricLanCloudRn,
       "cfprApFabricLanCloudFsmDescr": cfprApFabricLanCloudFsmDescr,
       "cfprApFabricLanCloudFsmPrev": cfprApFabricLanCloudFsmPrev,
       "cfprApFabricLanCloudFsmProgr": cfprApFabricLanCloudFsmProgr,
       "cfprApFabricLanCloudFsmRmtInvErrCode": cfprApFabricLanCloudFsmRmtInvErrCode,
       "cfprApFabricLanCloudFsmRmtInvErrDescr": cfprApFabricLanCloudFsmRmtInvErrDescr,
       "cfprApFabricLanCloudFsmRmtInvRslt": cfprApFabricLanCloudFsmRmtInvRslt,
       "cfprApFabricLanCloudFsmStageDescr": cfprApFabricLanCloudFsmStageDescr,
       "cfprApFabricLanCloudFsmStamp": cfprApFabricLanCloudFsmStamp,
       "cfprApFabricLanCloudFsmStatus": cfprApFabricLanCloudFsmStatus,
       "cfprApFabricLanCloudFsmTry": cfprApFabricLanCloudFsmTry,
       "cfprApFabricLanCloudMacAging": cfprApFabricLanCloudMacAging,
       "cfprApFabricLanCloudMode": cfprApFabricLanCloudMode,
       "cfprApFabricLanCloudVlanCompression": cfprApFabricLanCloudVlanCompression,
       "cfprApFabricLanCloudFsmTable": cfprApFabricLanCloudFsmTable,
       "cfprApFabricLanCloudFsmEntry": cfprApFabricLanCloudFsmEntry,
       "cfprApFabricLanCloudFsmInstanceId": cfprApFabricLanCloudFsmInstanceId,
       "cfprApFabricLanCloudFsmDn": cfprApFabricLanCloudFsmDn,
       "cfprApFabricLanCloudFsmRn": cfprApFabricLanCloudFsmRn,
       "cfprApFabricLanCloudFsmCompletionTime": cfprApFabricLanCloudFsmCompletionTime,
       "cfprApFabricLanCloudFsmCurrentFsm": cfprApFabricLanCloudFsmCurrentFsm,
       "cfprApFabricLanCloudFsmDescrData": cfprApFabricLanCloudFsmDescrData,
       "cfprApFabricLanCloudFsmFsmStatus": cfprApFabricLanCloudFsmFsmStatus,
       "cfprApFabricLanCloudFsmProgress": cfprApFabricLanCloudFsmProgress,
       "cfprApFabricLanCloudFsmRmtErrCode": cfprApFabricLanCloudFsmRmtErrCode,
       "cfprApFabricLanCloudFsmRmtErrDescr": cfprApFabricLanCloudFsmRmtErrDescr,
       "cfprApFabricLanCloudFsmRmtRslt": cfprApFabricLanCloudFsmRmtRslt,
       "cfprApFabricLanCloudFsmStageTable": cfprApFabricLanCloudFsmStageTable,
       "cfprApFabricLanCloudFsmStageEntry": cfprApFabricLanCloudFsmStageEntry,
       "cfprApFabricLanCloudFsmStageInstanceId": cfprApFabricLanCloudFsmStageInstanceId,
       "cfprApFabricLanCloudFsmStageDn": cfprApFabricLanCloudFsmStageDn,
       "cfprApFabricLanCloudFsmStageRn": cfprApFabricLanCloudFsmStageRn,
       "cfprApFabricLanCloudFsmStageDescrData": cfprApFabricLanCloudFsmStageDescrData,
       "cfprApFabricLanCloudFsmStageLastUpdateTime": cfprApFabricLanCloudFsmStageLastUpdateTime,
       "cfprApFabricLanCloudFsmStageName": cfprApFabricLanCloudFsmStageName,
       "cfprApFabricLanCloudFsmStageOrder": cfprApFabricLanCloudFsmStageOrder,
       "cfprApFabricLanCloudFsmStageRetry": cfprApFabricLanCloudFsmStageRetry,
       "cfprApFabricLanCloudFsmStageStageStatus": cfprApFabricLanCloudFsmStageStageStatus,
       "cfprApFabricLanCloudFsmTaskTable": cfprApFabricLanCloudFsmTaskTable,
       "cfprApFabricLanCloudFsmTaskEntry": cfprApFabricLanCloudFsmTaskEntry,
       "cfprApFabricLanCloudFsmTaskInstanceId": cfprApFabricLanCloudFsmTaskInstanceId,
       "cfprApFabricLanCloudFsmTaskDn": cfprApFabricLanCloudFsmTaskDn,
       "cfprApFabricLanCloudFsmTaskRn": cfprApFabricLanCloudFsmTaskRn,
       "cfprApFabricLanCloudFsmTaskCompletion": cfprApFabricLanCloudFsmTaskCompletion,
       "cfprApFabricLanCloudFsmTaskFlags": cfprApFabricLanCloudFsmTaskFlags,
       "cfprApFabricLanCloudFsmTaskItem": cfprApFabricLanCloudFsmTaskItem,
       "cfprApFabricLanCloudFsmTaskSeqId": cfprApFabricLanCloudFsmTaskSeqId,
       "cfprApFabricLanMonCloudTable": cfprApFabricLanMonCloudTable,
       "cfprApFabricLanMonCloudEntry": cfprApFabricLanMonCloudEntry,
       "cfprApFabricLanMonCloudInstanceId": cfprApFabricLanMonCloudInstanceId,
       "cfprApFabricLanMonCloudDn": cfprApFabricLanMonCloudDn,
       "cfprApFabricLanMonCloudRn": cfprApFabricLanMonCloudRn,
       "cfprApFabricLanMonCloudMode": cfprApFabricLanMonCloudMode,
       "cfprApFabricLanPinGroupTable": cfprApFabricLanPinGroupTable,
       "cfprApFabricLanPinGroupEntry": cfprApFabricLanPinGroupEntry,
       "cfprApFabricLanPinGroupInstanceId": cfprApFabricLanPinGroupInstanceId,
       "cfprApFabricLanPinGroupDn": cfprApFabricLanPinGroupDn,
       "cfprApFabricLanPinGroupRn": cfprApFabricLanPinGroupRn,
       "cfprApFabricLanPinGroupDescr": cfprApFabricLanPinGroupDescr,
       "cfprApFabricLanPinGroupIntId": cfprApFabricLanPinGroupIntId,
       "cfprApFabricLanPinGroupName": cfprApFabricLanPinGroupName,
       "cfprApFabricLanPinGroupPolicyLevel": cfprApFabricLanPinGroupPolicyLevel,
       "cfprApFabricLanPinGroupPolicyOwner": cfprApFabricLanPinGroupPolicyOwner,
       "cfprApFabricLanPinGroupSize": cfprApFabricLanPinGroupSize,
       "cfprApFabricLanPinTargetTable": cfprApFabricLanPinTargetTable,
       "cfprApFabricLanPinTargetEntry": cfprApFabricLanPinTargetEntry,
       "cfprApFabricLanPinTargetInstanceId": cfprApFabricLanPinTargetInstanceId,
       "cfprApFabricLanPinTargetDn": cfprApFabricLanPinTargetDn,
       "cfprApFabricLanPinTargetRn": cfprApFabricLanPinTargetRn,
       "cfprApFabricLanPinTargetEpDn": cfprApFabricLanPinTargetEpDn,
       "cfprApFabricLanPinTargetFabricId": cfprApFabricLanPinTargetFabricId,
       "cfprApFabricLanPinTargetTargetStatus": cfprApFabricLanPinTargetTargetStatus,
       "cfprApFabricLastAckedSlotTable": cfprApFabricLastAckedSlotTable,
       "cfprApFabricLastAckedSlotEntry": cfprApFabricLastAckedSlotEntry,
       "cfprApFabricLastAckedSlotInstanceId": cfprApFabricLastAckedSlotInstanceId,
       "cfprApFabricLastAckedSlotDn": cfprApFabricLastAckedSlotDn,
       "cfprApFabricLastAckedSlotRn": cfprApFabricLastAckedSlotRn,
       "cfprApFabricLastAckedSlotBoardAggregationRole": cfprApFabricLastAckedSlotBoardAggregationRole,
       "cfprApFabricLastAckedSlotChassisId": cfprApFabricLastAckedSlotChassisId,
       "cfprApFabricLastAckedSlotSlotId": cfprApFabricLastAckedSlotSlotId,
       "cfprApFabricLastAckedSlotSwitchId": cfprApFabricLastAckedSlotSwitchId,
       "cfprApFabricLocaleTable": cfprApFabricLocaleTable,
       "cfprApFabricLocaleEntry": cfprApFabricLocaleEntry,
       "cfprApFabricLocaleInstanceId": cfprApFabricLocaleInstanceId,
       "cfprApFabricLocaleDn": cfprApFabricLocaleDn,
       "cfprApFabricLocaleRn": cfprApFabricLocaleRn,
       "cfprApFabricLocaleCType": cfprApFabricLocaleCType,
       "cfprApFabricLocaleChassisId": cfprApFabricLocaleChassisId,
       "cfprApFabricLocaleLocale": cfprApFabricLocaleLocale,
       "cfprApFabricLocaleName": cfprApFabricLocaleName,
       "cfprApFabricLocaleSide": cfprApFabricLocaleSide,
       "cfprApFabricLocaleSlotId": cfprApFabricLocaleSlotId,
       "cfprApFabricLocaleSwitchId": cfprApFabricLocaleSwitchId,
       "cfprApFabricLocaleTransport": cfprApFabricLocaleTransport,
       "cfprApFabricLocaleType": cfprApFabricLocaleType,
       "cfprApFabricMulticastPolicyTable": cfprApFabricMulticastPolicyTable,
       "cfprApFabricMulticastPolicyEntry": cfprApFabricMulticastPolicyEntry,
       "cfprApFabricMulticastPolicyInstanceId": cfprApFabricMulticastPolicyInstanceId,
       "cfprApFabricMulticastPolicyDn": cfprApFabricMulticastPolicyDn,
       "cfprApFabricMulticastPolicyRn": cfprApFabricMulticastPolicyRn,
       "cfprApFabricMulticastPolicyDescr": cfprApFabricMulticastPolicyDescr,
       "cfprApFabricMulticastPolicyIntId": cfprApFabricMulticastPolicyIntId,
       "cfprApFabricMulticastPolicyName": cfprApFabricMulticastPolicyName,
       "cfprApFabricMulticastPolicyPolicyLevel": cfprApFabricMulticastPolicyPolicyLevel,
       "cfprApFabricMulticastPolicyPolicyOwner": cfprApFabricMulticastPolicyPolicyOwner,
       "cfprApFabricMulticastPolicyQuerierIpAddr": cfprApFabricMulticastPolicyQuerierIpAddr,
       "cfprApFabricMulticastPolicyQuerierState": cfprApFabricMulticastPolicyQuerierState,
       "cfprApFabricMulticastPolicySnoopingState": cfprApFabricMulticastPolicySnoopingState,
       "cfprApFabricNetGroupTable": cfprApFabricNetGroupTable,
       "cfprApFabricNetGroupEntry": cfprApFabricNetGroupEntry,
       "cfprApFabricNetGroupInstanceId": cfprApFabricNetGroupInstanceId,
       "cfprApFabricNetGroupDn": cfprApFabricNetGroupDn,
       "cfprApFabricNetGroupRn": cfprApFabricNetGroupRn,
       "cfprApFabricNetGroupAssigned": cfprApFabricNetGroupAssigned,
       "cfprApFabricNetGroupAssignmentOrder": cfprApFabricNetGroupAssignmentOrder,
       "cfprApFabricNetGroupDescr": cfprApFabricNetGroupDescr,
       "cfprApFabricNetGroupId": cfprApFabricNetGroupId,
       "cfprApFabricNetGroupIntId": cfprApFabricNetGroupIntId,
       "cfprApFabricNetGroupName": cfprApFabricNetGroupName,
       "cfprApFabricNetGroupNativeNet": cfprApFabricNetGroupNativeNet,
       "cfprApFabricNetGroupNativeNetDn": cfprApFabricNetGroupNativeNetDn,
       "cfprApFabricNetGroupOwner": cfprApFabricNetGroupOwner,
       "cfprApFabricNetGroupPeerDn": cfprApFabricNetGroupPeerDn,
       "cfprApFabricNetGroupPolicyLevel": cfprApFabricNetGroupPolicyLevel,
       "cfprApFabricNetGroupPolicyOwner": cfprApFabricNetGroupPolicyOwner,
       "cfprApFabricNetGroupSize": cfprApFabricNetGroupSize,
       "cfprApFabricNetGroupSwitchId": cfprApFabricNetGroupSwitchId,
       "cfprApFabricNetGroupType": cfprApFabricNetGroupType,
       "cfprApFabricOrgVlanPolicyTable": cfprApFabricOrgVlanPolicyTable,
       "cfprApFabricOrgVlanPolicyEntry": cfprApFabricOrgVlanPolicyEntry,
       "cfprApFabricOrgVlanPolicyInstanceId": cfprApFabricOrgVlanPolicyInstanceId,
       "cfprApFabricOrgVlanPolicyDn": cfprApFabricOrgVlanPolicyDn,
       "cfprApFabricOrgVlanPolicyRn": cfprApFabricOrgVlanPolicyRn,
       "cfprApFabricOrgVlanPolicyAdminState": cfprApFabricOrgVlanPolicyAdminState,
       "cfprApFabricOrgVlanPolicyName": cfprApFabricOrgVlanPolicyName,
       "cfprApFabricPathTable": cfprApFabricPathTable,
       "cfprApFabricPathEntry": cfprApFabricPathEntry,
       "cfprApFabricPathInstanceId": cfprApFabricPathInstanceId,
       "cfprApFabricPathDn": cfprApFabricPathDn,
       "cfprApFabricPathRn": cfprApFabricPathRn,
       "cfprApFabricPathCType": cfprApFabricPathCType,
       "cfprApFabricPathChassisId": cfprApFabricPathChassisId,
       "cfprApFabricPathEnacp": cfprApFabricPathEnacp,
       "cfprApFabricPathId": cfprApFabricPathId,
       "cfprApFabricPathLocale": cfprApFabricPathLocale,
       "cfprApFabricPathName": cfprApFabricPathName,
       "cfprApFabricPathNsSize": cfprApFabricPathNsSize,
       "cfprApFabricPathSide": cfprApFabricPathSide,
       "cfprApFabricPathSwitchId": cfprApFabricPathSwitchId,
       "cfprApFabricPathTransport": cfprApFabricPathTransport,
       "cfprApFabricPathType": cfprApFabricPathType,
       "cfprApFabricPathConnTable": cfprApFabricPathConnTable,
       "cfprApFabricPathConnEntry": cfprApFabricPathConnEntry,
       "cfprApFabricPathConnInstanceId": cfprApFabricPathConnInstanceId,
       "cfprApFabricPathConnDn": cfprApFabricPathConnDn,
       "cfprApFabricPathConnRn": cfprApFabricPathConnRn,
       "cfprApFabricPathConnCType": cfprApFabricPathConnCType,
       "cfprApFabricPathConnLocale": cfprApFabricPathConnLocale,
       "cfprApFabricPathConnName": cfprApFabricPathConnName,
       "cfprApFabricPathConnTransport": cfprApFabricPathConnTransport,
       "cfprApFabricPathConnType": cfprApFabricPathConnType,
       "cfprApFabricPathEpTable": cfprApFabricPathEpTable,
       "cfprApFabricPathEpEntry": cfprApFabricPathEpEntry,
       "cfprApFabricPathEpInstanceId": cfprApFabricPathEpInstanceId,
       "cfprApFabricPathEpDn": cfprApFabricPathEpDn,
       "cfprApFabricPathEpRn": cfprApFabricPathEpRn,
       "cfprApFabricPathEpAggrPortId": cfprApFabricPathEpAggrPortId,
       "cfprApFabricPathEpCType": cfprApFabricPathEpCType,
       "cfprApFabricPathEpChassisId": cfprApFabricPathEpChassisId,
       "cfprApFabricPathEpDiagLldpTransmit": cfprApFabricPathEpDiagLldpTransmit,
       "cfprApFabricPathEpEpDn": cfprApFabricPathEpEpDn,
       "cfprApFabricPathEpIfRole": cfprApFabricPathEpIfRole,
       "cfprApFabricPathEpIfType": cfprApFabricPathEpIfType,
       "cfprApFabricPathEpLocale": cfprApFabricPathEpLocale,
       "cfprApFabricPathEpName": cfprApFabricPathEpName,
       "cfprApFabricPathEpPeerAggrPortId": cfprApFabricPathEpPeerAggrPortId,
       "cfprApFabricPathEpPeerChassisId": cfprApFabricPathEpPeerChassisId,
       "cfprApFabricPathEpPeerDn": cfprApFabricPathEpPeerDn,
       "cfprApFabricPathEpPeerMac": cfprApFabricPathEpPeerMac,
       "cfprApFabricPathEpPeerPortId": cfprApFabricPathEpPeerPortId,
       "cfprApFabricPathEpPeerSlotId": cfprApFabricPathEpPeerSlotId,
       "cfprApFabricPathEpPortId": cfprApFabricPathEpPortId,
       "cfprApFabricPathEpSide": cfprApFabricPathEpSide,
       "cfprApFabricPathEpSlotId": cfprApFabricPathEpSlotId,
       "cfprApFabricPathEpSwitchId": cfprApFabricPathEpSwitchId,
       "cfprApFabricPathEpTransport": cfprApFabricPathEpTransport,
       "cfprApFabricPathEpType": cfprApFabricPathEpType,
       "cfprApFabricPoolableVlanTable": cfprApFabricPoolableVlanTable,
       "cfprApFabricPoolableVlanEntry": cfprApFabricPoolableVlanEntry,
       "cfprApFabricPoolableVlanInstanceId": cfprApFabricPoolableVlanInstanceId,
       "cfprApFabricPoolableVlanDn": cfprApFabricPoolableVlanDn,
       "cfprApFabricPoolableVlanRn": cfprApFabricPoolableVlanRn,
       "cfprApFabricPoolableVlanId": cfprApFabricPoolableVlanId,
       "cfprApFabricPoolableVlanPoolDn": cfprApFabricPoolableVlanPoolDn,
       "cfprApFabricPooledVlanTable": cfprApFabricPooledVlanTable,
       "cfprApFabricPooledVlanEntry": cfprApFabricPooledVlanEntry,
       "cfprApFabricPooledVlanInstanceId": cfprApFabricPooledVlanInstanceId,
       "cfprApFabricPooledVlanDn": cfprApFabricPooledVlanDn,
       "cfprApFabricPooledVlanRn": cfprApFabricPooledVlanRn,
       "cfprApFabricPooledVlanAssigned": cfprApFabricPooledVlanAssigned,
       "cfprApFabricPooledVlanAssignedToDn": cfprApFabricPooledVlanAssignedToDn,
       "cfprApFabricPooledVlanConfigIssues": cfprApFabricPooledVlanConfigIssues,
       "cfprApFabricPooledVlanName": cfprApFabricPooledVlanName,
       "cfprApFabricPooledVlanPeerDn": cfprApFabricPooledVlanPeerDn,
       "cfprApFabricPooledVlanPoolableDn": cfprApFabricPooledVlanPoolableDn,
       "cfprApFabricPooledVlanPrevAssignedToDn": cfprApFabricPooledVlanPrevAssignedToDn,
       "cfprApFabricSanCloudTable": cfprApFabricSanCloudTable,
       "cfprApFabricSanCloudEntry": cfprApFabricSanCloudEntry,
       "cfprApFabricSanCloudInstanceId": cfprApFabricSanCloudInstanceId,
       "cfprApFabricSanCloudDn": cfprApFabricSanCloudDn,
       "cfprApFabricSanCloudRn": cfprApFabricSanCloudRn,
       "cfprApFabricSanCloudFsmDescr": cfprApFabricSanCloudFsmDescr,
       "cfprApFabricSanCloudFsmPrev": cfprApFabricSanCloudFsmPrev,
       "cfprApFabricSanCloudFsmProgr": cfprApFabricSanCloudFsmProgr,
       "cfprApFabricSanCloudFsmRmtInvErrCode": cfprApFabricSanCloudFsmRmtInvErrCode,
       "cfprApFabricSanCloudFsmRmtInvErrDescr": cfprApFabricSanCloudFsmRmtInvErrDescr,
       "cfprApFabricSanCloudFsmRmtInvRslt": cfprApFabricSanCloudFsmRmtInvRslt,
       "cfprApFabricSanCloudFsmStageDescr": cfprApFabricSanCloudFsmStageDescr,
       "cfprApFabricSanCloudFsmStamp": cfprApFabricSanCloudFsmStamp,
       "cfprApFabricSanCloudFsmStatus": cfprApFabricSanCloudFsmStatus,
       "cfprApFabricSanCloudFsmTry": cfprApFabricSanCloudFsmTry,
       "cfprApFabricSanCloudMode": cfprApFabricSanCloudMode,
       "cfprApFabricSanCloudFsmTable": cfprApFabricSanCloudFsmTable,
       "cfprApFabricSanCloudFsmEntry": cfprApFabricSanCloudFsmEntry,
       "cfprApFabricSanCloudFsmInstanceId": cfprApFabricSanCloudFsmInstanceId,
       "cfprApFabricSanCloudFsmDn": cfprApFabricSanCloudFsmDn,
       "cfprApFabricSanCloudFsmRn": cfprApFabricSanCloudFsmRn,
       "cfprApFabricSanCloudFsmCompletionTime": cfprApFabricSanCloudFsmCompletionTime,
       "cfprApFabricSanCloudFsmCurrentFsm": cfprApFabricSanCloudFsmCurrentFsm,
       "cfprApFabricSanCloudFsmDescrData": cfprApFabricSanCloudFsmDescrData,
       "cfprApFabricSanCloudFsmFsmStatus": cfprApFabricSanCloudFsmFsmStatus,
       "cfprApFabricSanCloudFsmProgress": cfprApFabricSanCloudFsmProgress,
       "cfprApFabricSanCloudFsmRmtErrCode": cfprApFabricSanCloudFsmRmtErrCode,
       "cfprApFabricSanCloudFsmRmtErrDescr": cfprApFabricSanCloudFsmRmtErrDescr,
       "cfprApFabricSanCloudFsmRmtRslt": cfprApFabricSanCloudFsmRmtRslt,
       "cfprApFabricSanCloudFsmStageTable": cfprApFabricSanCloudFsmStageTable,
       "cfprApFabricSanCloudFsmStageEntry": cfprApFabricSanCloudFsmStageEntry,
       "cfprApFabricSanCloudFsmStageInstanceId": cfprApFabricSanCloudFsmStageInstanceId,
       "cfprApFabricSanCloudFsmStageDn": cfprApFabricSanCloudFsmStageDn,
       "cfprApFabricSanCloudFsmStageRn": cfprApFabricSanCloudFsmStageRn,
       "cfprApFabricSanCloudFsmStageDescrData": cfprApFabricSanCloudFsmStageDescrData,
       "cfprApFabricSanCloudFsmStageLastUpdateTime": cfprApFabricSanCloudFsmStageLastUpdateTime,
       "cfprApFabricSanCloudFsmStageName": cfprApFabricSanCloudFsmStageName,
       "cfprApFabricSanCloudFsmStageOrder": cfprApFabricSanCloudFsmStageOrder,
       "cfprApFabricSanCloudFsmStageRetry": cfprApFabricSanCloudFsmStageRetry,
       "cfprApFabricSanCloudFsmStageStageStatus": cfprApFabricSanCloudFsmStageStageStatus,
       "cfprApFabricSanCloudFsmTaskTable": cfprApFabricSanCloudFsmTaskTable,
       "cfprApFabricSanCloudFsmTaskEntry": cfprApFabricSanCloudFsmTaskEntry,
       "cfprApFabricSanCloudFsmTaskInstanceId": cfprApFabricSanCloudFsmTaskInstanceId,
       "cfprApFabricSanCloudFsmTaskDn": cfprApFabricSanCloudFsmTaskDn,
       "cfprApFabricSanCloudFsmTaskRn": cfprApFabricSanCloudFsmTaskRn,
       "cfprApFabricSanCloudFsmTaskCompletion": cfprApFabricSanCloudFsmTaskCompletion,
       "cfprApFabricSanCloudFsmTaskFlags": cfprApFabricSanCloudFsmTaskFlags,
       "cfprApFabricSanCloudFsmTaskItem": cfprApFabricSanCloudFsmTaskItem,
       "cfprApFabricSanCloudFsmTaskSeqId": cfprApFabricSanCloudFsmTaskSeqId,
       "cfprApFabricSanPinGroupTable": cfprApFabricSanPinGroupTable,
       "cfprApFabricSanPinGroupEntry": cfprApFabricSanPinGroupEntry,
       "cfprApFabricSanPinGroupInstanceId": cfprApFabricSanPinGroupInstanceId,
       "cfprApFabricSanPinGroupDn": cfprApFabricSanPinGroupDn,
       "cfprApFabricSanPinGroupRn": cfprApFabricSanPinGroupRn,
       "cfprApFabricSanPinGroupDescr": cfprApFabricSanPinGroupDescr,
       "cfprApFabricSanPinGroupIntId": cfprApFabricSanPinGroupIntId,
       "cfprApFabricSanPinGroupName": cfprApFabricSanPinGroupName,
       "cfprApFabricSanPinGroupPolicyLevel": cfprApFabricSanPinGroupPolicyLevel,
       "cfprApFabricSanPinGroupPolicyOwner": cfprApFabricSanPinGroupPolicyOwner,
       "cfprApFabricSanPinGroupSize": cfprApFabricSanPinGroupSize,
       "cfprApFabricSanPinTargetTable": cfprApFabricSanPinTargetTable,
       "cfprApFabricSanPinTargetEntry": cfprApFabricSanPinTargetEntry,
       "cfprApFabricSanPinTargetInstanceId": cfprApFabricSanPinTargetInstanceId,
       "cfprApFabricSanPinTargetDn": cfprApFabricSanPinTargetDn,
       "cfprApFabricSanPinTargetRn": cfprApFabricSanPinTargetRn,
       "cfprApFabricSanPinTargetEpDn": cfprApFabricSanPinTargetEpDn,
       "cfprApFabricSanPinTargetFabricId": cfprApFabricSanPinTargetFabricId,
       "cfprApFabricSanPinTargetTargetStatus": cfprApFabricSanPinTargetTargetStatus,
       "cfprApFabricSspEthMonTable": cfprApFabricSspEthMonTable,
       "cfprApFabricSspEthMonEntry": cfprApFabricSspEthMonEntry,
       "cfprApFabricSspEthMonInstanceId": cfprApFabricSspEthMonInstanceId,
       "cfprApFabricSspEthMonDn": cfprApFabricSspEthMonDn,
       "cfprApFabricSspEthMonRn": cfprApFabricSspEthMonRn,
       "cfprApFabricSspEthMonAdminState": cfprApFabricSspEthMonAdminState,
       "cfprApFabricSspEthMonAppendFlag": cfprApFabricSspEthMonAppendFlag,
       "cfprApFabricSspEthMonConfigFailReason": cfprApFabricSspEthMonConfigFailReason,
       "cfprApFabricSspEthMonDelPcap": cfprApFabricSspEthMonDelPcap,
       "cfprApFabricSspEthMonDropCount": cfprApFabricSspEthMonDropCount,
       "cfprApFabricSspEthMonErrorCode": cfprApFabricSspEthMonErrorCode,
       "cfprApFabricSspEthMonId": cfprApFabricSspEthMonId,
       "cfprApFabricSspEthMonIsConfigSuccess": cfprApFabricSspEthMonIsConfigSuccess,
       "cfprApFabricSspEthMonIsConfiguredByAG": cfprApFabricSspEthMonIsConfiguredByAG,
       "cfprApFabricSspEthMonName": cfprApFabricSspEthMonName,
       "cfprApFabricSspEthMonOperState": cfprApFabricSspEthMonOperState,
       "cfprApFabricSspEthMonOperStateReason": cfprApFabricSspEthMonOperStateReason,
       "cfprApFabricSspEthMonPeerDn": cfprApFabricSspEthMonPeerDn,
       "cfprApFabricSspEthMonReBoot": cfprApFabricSspEthMonReBoot,
       "cfprApFabricSspEthMonSession": cfprApFabricSspEthMonSession,
       "cfprApFabricSspEthMonSessionMemUsage": cfprApFabricSspEthMonSessionMemUsage,
       "cfprApFabricSspEthMonSourceConfigured": cfprApFabricSspEthMonSourceConfigured,
       "cfprApFabricSspEthMonFilterEpTable": cfprApFabricSspEthMonFilterEpTable,
       "cfprApFabricSspEthMonFilterEpEntry": cfprApFabricSspEthMonFilterEpEntry,
       "cfprApFabricSspEthMonFilterEpInstanceId": cfprApFabricSspEthMonFilterEpInstanceId,
       "cfprApFabricSspEthMonFilterEpDn": cfprApFabricSspEthMonFilterEpDn,
       "cfprApFabricSspEthMonFilterEpRn": cfprApFabricSspEthMonFilterEpRn,
       "cfprApFabricSspEthMonFilterEpDestIp": cfprApFabricSspEthMonFilterEpDestIp,
       "cfprApFabricSspEthMonFilterEpDestMAC": cfprApFabricSspEthMonFilterEpDestMAC,
       "cfprApFabricSspEthMonFilterEpDestPort": cfprApFabricSspEthMonFilterEpDestPort,
       "cfprApFabricSspEthMonFilterEpEthertype": cfprApFabricSspEthMonFilterEpEthertype,
       "cfprApFabricSspEthMonFilterEpIvlan": cfprApFabricSspEthMonFilterEpIvlan,
       "cfprApFabricSspEthMonFilterEpNameId": cfprApFabricSspEthMonFilterEpNameId,
       "cfprApFabricSspEthMonFilterEpOvlan": cfprApFabricSspEthMonFilterEpOvlan,
       "cfprApFabricSspEthMonFilterEpProtocol": cfprApFabricSspEthMonFilterEpProtocol,
       "cfprApFabricSspEthMonFilterEpSrcIp": cfprApFabricSspEthMonFilterEpSrcIp,
       "cfprApFabricSspEthMonFilterEpSrcMAC": cfprApFabricSspEthMonFilterEpSrcMAC,
       "cfprApFabricSspEthMonFilterEpSrcPort": cfprApFabricSspEthMonFilterEpSrcPort,
       "cfprApFabricSspEthMonSrcAppEpTable": cfprApFabricSspEthMonSrcAppEpTable,
       "cfprApFabricSspEthMonSrcAppEpEntry": cfprApFabricSspEthMonSrcAppEpEntry,
       "cfprApFabricSspEthMonSrcAppEpInstanceId": cfprApFabricSspEthMonSrcAppEpInstanceId,
       "cfprApFabricSspEthMonSrcAppEpDn": cfprApFabricSspEthMonSrcAppEpDn,
       "cfprApFabricSspEthMonSrcAppEpRn": cfprApFabricSspEthMonSrcAppEpRn,
       "cfprApFabricSspEthMonSrcAppEpAppName": cfprApFabricSspEthMonSrcAppEpAppName,
       "cfprApFabricSspEthMonSrcAppEpFilter": cfprApFabricSspEthMonSrcAppEpFilter,
       "cfprApFabricSspEthMonSrcAppEpLinkName": cfprApFabricSspEthMonSrcAppEpLinkName,
       "cfprApFabricSspEthMonSrcAppEpPcapfile": cfprApFabricSspEthMonSrcAppEpPcapfile,
       "cfprApFabricSspEthMonSrcAppEpPcapfilename": cfprApFabricSspEthMonSrcAppEpPcapfilename,
       "cfprApFabricSspEthMonSrcAppEpPcapsize": cfprApFabricSspEthMonSrcAppEpPcapsize,
       "cfprApFabricSspEthMonSrcAppEpPortName": cfprApFabricSspEthMonSrcAppEpPortName,
       "cfprApFabricSspEthMonSrcAppEpSlotId": cfprApFabricSspEthMonSrcAppEpSlotId,
       "cfprApFabricSspEthMonSrcAppLinksEpTable": cfprApFabricSspEthMonSrcAppLinksEpTable,
       "cfprApFabricSspEthMonSrcAppLinksEpEntry": cfprApFabricSspEthMonSrcAppLinksEpEntry,
       "cfprApFabricSspEthMonSrcAppLinksEpInstanceId": cfprApFabricSspEthMonSrcAppLinksEpInstanceId,
       "cfprApFabricSspEthMonSrcAppLinksEpDn": cfprApFabricSspEthMonSrcAppLinksEpDn,
       "cfprApFabricSspEthMonSrcAppLinksEpRn": cfprApFabricSspEthMonSrcAppLinksEpRn,
       "cfprApFabricSspEthMonSrcAppLinksEpChassisId": cfprApFabricSspEthMonSrcAppLinksEpChassisId,
       "cfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId": cfprApFabricSspEthMonSrcAppLinksEpEqAggrPortId,
       "cfprApFabricSspEthMonSrcAppLinksEpEqPortId": cfprApFabricSspEthMonSrcAppLinksEpEqPortId,
       "cfprApFabricSspEthMonSrcAppLinksEpEqSlotId": cfprApFabricSspEthMonSrcAppLinksEpEqSlotId,
       "cfprApFabricSspEthMonSrcAppLinksEpFilter": cfprApFabricSspEthMonSrcAppLinksEpFilter,
       "cfprApFabricSspEthMonSrcAppLinksEpFilterDn": cfprApFabricSspEthMonSrcAppLinksEpFilterDn,
       "cfprApFabricSspEthMonSrcAppLinksEpLifeCycle": cfprApFabricSspEthMonSrcAppLinksEpLifeCycle,
       "cfprApFabricSspEthMonSrcAppLinksEpName": cfprApFabricSspEthMonSrcAppLinksEpName,
       "cfprApFabricSspEthMonSrcAppLinksEpPcapfile": cfprApFabricSspEthMonSrcAppLinksEpPcapfile,
       "cfprApFabricSspEthMonSrcAppLinksEpPcapfilename": cfprApFabricSspEthMonSrcAppLinksEpPcapfilename,
       "cfprApFabricSspEthMonSrcAppLinksEpPcapsize": cfprApFabricSspEthMonSrcAppLinksEpPcapsize,
       "cfprApFabricSspEthMonSrcAppLinksEpSwitchId": cfprApFabricSspEthMonSrcAppLinksEpSwitchId,
       "cfprApFabricSspEthMonSrcAppLinksEpVlan": cfprApFabricSspEthMonSrcAppLinksEpVlan,
       "cfprApFabricSspEthMonSrcPhyAggrEpTable": cfprApFabricSspEthMonSrcPhyAggrEpTable,
       "cfprApFabricSspEthMonSrcPhyAggrEpEntry": cfprApFabricSspEthMonSrcPhyAggrEpEntry,
       "cfprApFabricSspEthMonSrcPhyAggrEpInstanceId": cfprApFabricSspEthMonSrcPhyAggrEpInstanceId,
       "cfprApFabricSspEthMonSrcPhyAggrEpDn": cfprApFabricSspEthMonSrcPhyAggrEpDn,
       "cfprApFabricSspEthMonSrcPhyAggrEpRn": cfprApFabricSspEthMonSrcPhyAggrEpRn,
       "cfprApFabricSspEthMonSrcPhyAggrEpAggrPortId": cfprApFabricSspEthMonSrcPhyAggrEpAggrPortId,
       "cfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId": cfprApFabricSspEthMonSrcPhyAggrEpBreakoutPortId,
       "cfprApFabricSspEthMonSrcPhyAggrEpChassisId": cfprApFabricSspEthMonSrcPhyAggrEpChassisId,
       "cfprApFabricSspEthMonSrcPhyAggrEpFilter": cfprApFabricSspEthMonSrcPhyAggrEpFilter,
       "cfprApFabricSspEthMonSrcPhyAggrEpPcapfile": cfprApFabricSspEthMonSrcPhyAggrEpPcapfile,
       "cfprApFabricSspEthMonSrcPhyAggrEpPcapfilename": cfprApFabricSspEthMonSrcPhyAggrEpPcapfilename,
       "cfprApFabricSspEthMonSrcPhyAggrEpPcapsize": cfprApFabricSspEthMonSrcPhyAggrEpPcapsize,
       "cfprApFabricSspEthMonSrcPhyAggrEpSlotId": cfprApFabricSspEthMonSrcPhyAggrEpSlotId,
       "cfprApFabricSspEthMonSrcPhyAggrEpSwitchId": cfprApFabricSspEthMonSrcPhyAggrEpSwitchId,
       "cfprApFabricSspEthMonSrcPhyEpTable": cfprApFabricSspEthMonSrcPhyEpTable,
       "cfprApFabricSspEthMonSrcPhyEpEntry": cfprApFabricSspEthMonSrcPhyEpEntry,
       "cfprApFabricSspEthMonSrcPhyEpInstanceId": cfprApFabricSspEthMonSrcPhyEpInstanceId,
       "cfprApFabricSspEthMonSrcPhyEpDn": cfprApFabricSspEthMonSrcPhyEpDn,
       "cfprApFabricSspEthMonSrcPhyEpRn": cfprApFabricSspEthMonSrcPhyEpRn,
       "cfprApFabricSspEthMonSrcPhyEpChassisId": cfprApFabricSspEthMonSrcPhyEpChassisId,
       "cfprApFabricSspEthMonSrcPhyEpFilter": cfprApFabricSspEthMonSrcPhyEpFilter,
       "cfprApFabricSspEthMonSrcPhyEpPcapfile": cfprApFabricSspEthMonSrcPhyEpPcapfile,
       "cfprApFabricSspEthMonSrcPhyEpPcapfilename": cfprApFabricSspEthMonSrcPhyEpPcapfilename,
       "cfprApFabricSspEthMonSrcPhyEpPcapsize": cfprApFabricSspEthMonSrcPhyEpPcapsize,
       "cfprApFabricSspEthMonSrcPhyEpPortId": cfprApFabricSspEthMonSrcPhyEpPortId,
       "cfprApFabricSspEthMonSrcPhyEpSlotId": cfprApFabricSspEthMonSrcPhyEpSlotId,
       "cfprApFabricSspEthMonSrcPhyEpSwitchId": cfprApFabricSspEthMonSrcPhyEpSwitchId,
       "cfprApFabricSspLanMonCloudTable": cfprApFabricSspLanMonCloudTable,
       "cfprApFabricSspLanMonCloudEntry": cfprApFabricSspLanMonCloudEntry,
       "cfprApFabricSspLanMonCloudInstanceId": cfprApFabricSspLanMonCloudInstanceId,
       "cfprApFabricSspLanMonCloudDn": cfprApFabricSspLanMonCloudDn,
       "cfprApFabricSspLanMonCloudRn": cfprApFabricSspLanMonCloudRn,
       "cfprApFabricSspLanMonCloudMode": cfprApFabricSspLanMonCloudMode,
       "cfprApFabricSubGroupTable": cfprApFabricSubGroupTable,
       "cfprApFabricSubGroupEntry": cfprApFabricSubGroupEntry,
       "cfprApFabricSubGroupInstanceId": cfprApFabricSubGroupInstanceId,
       "cfprApFabricSubGroupDn": cfprApFabricSubGroupDn,
       "cfprApFabricSubGroupRn": cfprApFabricSubGroupRn,
       "cfprApFabricSubGroupAggrPortId": cfprApFabricSubGroupAggrPortId,
       "cfprApFabricSubGroupConfigState": cfprApFabricSubGroupConfigState,
       "cfprApFabricSubGroupLicGP": cfprApFabricSubGroupLicGP,
       "cfprApFabricSubGroupLicState": cfprApFabricSubGroupLicState,
       "cfprApFabricSubGroupLocale": cfprApFabricSubGroupLocale,
       "cfprApFabricSubGroupName": cfprApFabricSubGroupName,
       "cfprApFabricSubGroupSlotId": cfprApFabricSubGroupSlotId,
       "cfprApFabricSubGroupSwitchId": cfprApFabricSubGroupSwitchId,
       "cfprApFabricSubGroupTransport": cfprApFabricSubGroupTransport,
       "cfprApFabricSubGroupType": cfprApFabricSubGroupType,
       "cfprApFabricSwChPhEpTable": cfprApFabricSwChPhEpTable,
       "cfprApFabricSwChPhEpEntry": cfprApFabricSwChPhEpEntry,
       "cfprApFabricSwChPhEpInstanceId": cfprApFabricSwChPhEpInstanceId,
       "cfprApFabricSwChPhEpDn": cfprApFabricSwChPhEpDn,
       "cfprApFabricSwChPhEpRn": cfprApFabricSwChPhEpRn,
       "cfprApFabricSwChPhEpAdminState": cfprApFabricSwChPhEpAdminState,
       "cfprApFabricSwChPhEpAggrPortId": cfprApFabricSwChPhEpAggrPortId,
       "cfprApFabricSwChPhEpChassisId": cfprApFabricSwChPhEpChassisId,
       "cfprApFabricSwChPhEpEpDn": cfprApFabricSwChPhEpEpDn,
       "cfprApFabricSwChPhEpEqType": cfprApFabricSwChPhEpEqType,
       "cfprApFabricSwChPhEpFltAggr": cfprApFabricSwChPhEpFltAggr,
       "cfprApFabricSwChPhEpIfRole": cfprApFabricSwChPhEpIfRole,
       "cfprApFabricSwChPhEpIfType": cfprApFabricSwChPhEpIfType,
       "cfprApFabricSwChPhEpLc": cfprApFabricSwChPhEpLc,
       "cfprApFabricSwChPhEpLicGP": cfprApFabricSwChPhEpLicGP,
       "cfprApFabricSwChPhEpLicState": cfprApFabricSwChPhEpLicState,
       "cfprApFabricSwChPhEpLocale": cfprApFabricSwChPhEpLocale,
       "cfprApFabricSwChPhEpModel": cfprApFabricSwChPhEpModel,
       "cfprApFabricSwChPhEpName": cfprApFabricSwChPhEpName,
       "cfprApFabricSwChPhEpOperState": cfprApFabricSwChPhEpOperState,
       "cfprApFabricSwChPhEpOperStateReason": cfprApFabricSwChPhEpOperStateReason,
       "cfprApFabricSwChPhEpPeerAggrPortId": cfprApFabricSwChPhEpPeerAggrPortId,
       "cfprApFabricSwChPhEpPeerChassisId": cfprApFabricSwChPhEpPeerChassisId,
       "cfprApFabricSwChPhEpPeerDn": cfprApFabricSwChPhEpPeerDn,
       "cfprApFabricSwChPhEpPeerPortId": cfprApFabricSwChPhEpPeerPortId,
       "cfprApFabricSwChPhEpPeerSlotId": cfprApFabricSwChPhEpPeerSlotId,
       "cfprApFabricSwChPhEpPortId": cfprApFabricSwChPhEpPortId,
       "cfprApFabricSwChPhEpRevision": cfprApFabricSwChPhEpRevision,
       "cfprApFabricSwChPhEpSerial": cfprApFabricSwChPhEpSerial,
       "cfprApFabricSwChPhEpSlotId": cfprApFabricSwChPhEpSlotId,
       "cfprApFabricSwChPhEpSwitchId": cfprApFabricSwChPhEpSwitchId,
       "cfprApFabricSwChPhEpTransport": cfprApFabricSwChPhEpTransport,
       "cfprApFabricSwChPhEpType": cfprApFabricSwChPhEpType,
       "cfprApFabricSwChPhEpVendor": cfprApFabricSwChPhEpVendor,
       "cfprApFabricSwSubGroupTable": cfprApFabricSwSubGroupTable,
       "cfprApFabricSwSubGroupEntry": cfprApFabricSwSubGroupEntry,
       "cfprApFabricSwSubGroupInstanceId": cfprApFabricSwSubGroupInstanceId,
       "cfprApFabricSwSubGroupDn": cfprApFabricSwSubGroupDn,
       "cfprApFabricSwSubGroupRn": cfprApFabricSwSubGroupRn,
       "cfprApFabricSwSubGroupAggrPortId": cfprApFabricSwSubGroupAggrPortId,
       "cfprApFabricSwSubGroupConfigState": cfprApFabricSwSubGroupConfigState,
       "cfprApFabricSwSubGroupLicGP": cfprApFabricSwSubGroupLicGP,
       "cfprApFabricSwSubGroupLicState": cfprApFabricSwSubGroupLicState,
       "cfprApFabricSwSubGroupLocale": cfprApFabricSwSubGroupLocale,
       "cfprApFabricSwSubGroupName": cfprApFabricSwSubGroupName,
       "cfprApFabricSwSubGroupSlotId": cfprApFabricSwSubGroupSlotId,
       "cfprApFabricSwSubGroupSwitchId": cfprApFabricSwSubGroupSwitchId,
       "cfprApFabricSwSubGroupTransport": cfprApFabricSwSubGroupTransport,
       "cfprApFabricSwSubGroupType": cfprApFabricSwSubGroupType,
       "cfprApFabricUdldLinkPolicyTable": cfprApFabricUdldLinkPolicyTable,
       "cfprApFabricUdldLinkPolicyEntry": cfprApFabricUdldLinkPolicyEntry,
       "cfprApFabricUdldLinkPolicyInstanceId": cfprApFabricUdldLinkPolicyInstanceId,
       "cfprApFabricUdldLinkPolicyDn": cfprApFabricUdldLinkPolicyDn,
       "cfprApFabricUdldLinkPolicyRn": cfprApFabricUdldLinkPolicyRn,
       "cfprApFabricUdldLinkPolicyAdminState": cfprApFabricUdldLinkPolicyAdminState,
       "cfprApFabricUdldLinkPolicyDescr": cfprApFabricUdldLinkPolicyDescr,
       "cfprApFabricUdldLinkPolicyIntId": cfprApFabricUdldLinkPolicyIntId,
       "cfprApFabricUdldLinkPolicyMode": cfprApFabricUdldLinkPolicyMode,
       "cfprApFabricUdldLinkPolicyName": cfprApFabricUdldLinkPolicyName,
       "cfprApFabricUdldLinkPolicyPolicyLevel": cfprApFabricUdldLinkPolicyPolicyLevel,
       "cfprApFabricUdldLinkPolicyPolicyOwner": cfprApFabricUdldLinkPolicyPolicyOwner,
       "cfprApFabricUdldLinkPolicyProtocol": cfprApFabricUdldLinkPolicyProtocol,
       "cfprApFabricUdldLinkPolicyType": cfprApFabricUdldLinkPolicyType,
       "cfprApFabricUdldPolicyTable": cfprApFabricUdldPolicyTable,
       "cfprApFabricUdldPolicyEntry": cfprApFabricUdldPolicyEntry,
       "cfprApFabricUdldPolicyInstanceId": cfprApFabricUdldPolicyInstanceId,
       "cfprApFabricUdldPolicyDn": cfprApFabricUdldPolicyDn,
       "cfprApFabricUdldPolicyRn": cfprApFabricUdldPolicyRn,
       "cfprApFabricUdldPolicyDescr": cfprApFabricUdldPolicyDescr,
       "cfprApFabricUdldPolicyIntId": cfprApFabricUdldPolicyIntId,
       "cfprApFabricUdldPolicyMsgInterval": cfprApFabricUdldPolicyMsgInterval,
       "cfprApFabricUdldPolicyName": cfprApFabricUdldPolicyName,
       "cfprApFabricUdldPolicyPolicyLevel": cfprApFabricUdldPolicyPolicyLevel,
       "cfprApFabricUdldPolicyPolicyOwner": cfprApFabricUdldPolicyPolicyOwner,
       "cfprApFabricUdldPolicyRecoveryAction": cfprApFabricUdldPolicyRecoveryAction,
       "cfprApFabricVConTable": cfprApFabricVConTable,
       "cfprApFabricVConEntry": cfprApFabricVConEntry,
       "cfprApFabricVConInstanceId": cfprApFabricVConInstanceId,
       "cfprApFabricVConDn": cfprApFabricVConDn,
       "cfprApFabricVConRn": cfprApFabricVConRn,
       "cfprApFabricVConEquipmentDn": cfprApFabricVConEquipmentDn,
       "cfprApFabricVConFabric": cfprApFabricVConFabric,
       "cfprApFabricVConId": cfprApFabricVConId,
       "cfprApFabricVConInstType": cfprApFabricVConInstType,
       "cfprApFabricVConPlacement": cfprApFabricVConPlacement,
       "cfprApFabricVConSelect": cfprApFabricVConSelect,
       "cfprApFabricVConShare": cfprApFabricVConShare,
       "cfprApFabricVConTransport": cfprApFabricVConTransport,
       "cfprApFabricVConProfileTable": cfprApFabricVConProfileTable,
       "cfprApFabricVConProfileEntry": cfprApFabricVConProfileEntry,
       "cfprApFabricVConProfileInstanceId": cfprApFabricVConProfileInstanceId,
       "cfprApFabricVConProfileDn": cfprApFabricVConProfileDn,
       "cfprApFabricVConProfileRn": cfprApFabricVConProfileRn,
       "cfprApFabricVConProfileDescr": cfprApFabricVConProfileDescr,
       "cfprApFabricVConProfileIntId": cfprApFabricVConProfileIntId,
       "cfprApFabricVConProfileMezzMapping": cfprApFabricVConProfileMezzMapping,
       "cfprApFabricVConProfileName": cfprApFabricVConProfileName,
       "cfprApFabricVConProfilePolicyLevel": cfprApFabricVConProfilePolicyLevel,
       "cfprApFabricVConProfilePolicyOwner": cfprApFabricVConProfilePolicyOwner,
       "cfprApFabricVlanTable": cfprApFabricVlanTable,
       "cfprApFabricVlanEntry": cfprApFabricVlanEntry,
       "cfprApFabricVlanInstanceId": cfprApFabricVlanInstanceId,
       "cfprApFabricVlanDn": cfprApFabricVlanDn,
       "cfprApFabricVlanRn": cfprApFabricVlanRn,
       "cfprApFabricVlanAssocPrimaryVlanState": cfprApFabricVlanAssocPrimaryVlanState,
       "cfprApFabricVlanAssocPrimaryVlanSwitchId": cfprApFabricVlanAssocPrimaryVlanSwitchId,
       "cfprApFabricVlanCloud": cfprApFabricVlanCloud,
       "cfprApFabricVlanCompressionType": cfprApFabricVlanCompressionType,
       "cfprApFabricVlanConfigIssues": cfprApFabricVlanConfigIssues,
       "cfprApFabricVlanDefaultNet": cfprApFabricVlanDefaultNet,
       "cfprApFabricVlanEpDn": cfprApFabricVlanEpDn,
       "cfprApFabricVlanFltAggr": cfprApFabricVlanFltAggr,
       "cfprApFabricVlanGlobal": cfprApFabricVlanGlobal,
       "cfprApFabricVlanId": cfprApFabricVlanId,
       "cfprApFabricVlanIfRole": cfprApFabricVlanIfRole,
       "cfprApFabricVlanIfType": cfprApFabricVlanIfType,
       "cfprApFabricVlanLocal": cfprApFabricVlanLocal,
       "cfprApFabricVlanLocale": cfprApFabricVlanLocale,
       "cfprApFabricVlanMcastPolicyName": cfprApFabricVlanMcastPolicyName,
       "cfprApFabricVlanName": cfprApFabricVlanName,
       "cfprApFabricVlanOperMcastPolicyName": cfprApFabricVlanOperMcastPolicyName,
       "cfprApFabricVlanOperState": cfprApFabricVlanOperState,
       "cfprApFabricVlanOverlapStateForA": cfprApFabricVlanOverlapStateForA,
       "cfprApFabricVlanOverlapStateForB": cfprApFabricVlanOverlapStateForB,
       "cfprApFabricVlanPeerDn": cfprApFabricVlanPeerDn,
       "cfprApFabricVlanPolicyOwner": cfprApFabricVlanPolicyOwner,
       "cfprApFabricVlanPubNwDn": cfprApFabricVlanPubNwDn,
       "cfprApFabricVlanPubNwId": cfprApFabricVlanPubNwId,
       "cfprApFabricVlanPubNwName": cfprApFabricVlanPubNwName,
       "cfprApFabricVlanSharing": cfprApFabricVlanSharing,
       "cfprApFabricVlanSwitchId": cfprApFabricVlanSwitchId,
       "cfprApFabricVlanTransport": cfprApFabricVlanTransport,
       "cfprApFabricVlanType": cfprApFabricVlanType,
       "cfprApFabricVlanEpTable": cfprApFabricVlanEpTable,
       "cfprApFabricVlanEpEntry": cfprApFabricVlanEpEntry,
       "cfprApFabricVlanEpInstanceId": cfprApFabricVlanEpInstanceId,
       "cfprApFabricVlanEpDnData": cfprApFabricVlanEpDnData,
       "cfprApFabricVlanEpRn": cfprApFabricVlanEpRn,
       "cfprApFabricVlanEpAssocPrimaryVlanState": cfprApFabricVlanEpAssocPrimaryVlanState,
       "cfprApFabricVlanEpAssocPrimaryVlanSwitchId": cfprApFabricVlanEpAssocPrimaryVlanSwitchId,
       "cfprApFabricVlanEpEpDn": cfprApFabricVlanEpEpDn,
       "cfprApFabricVlanEpId": cfprApFabricVlanEpId,
       "cfprApFabricVlanEpIfRole": cfprApFabricVlanEpIfRole,
       "cfprApFabricVlanEpIfType": cfprApFabricVlanEpIfType,
       "cfprApFabricVlanEpIsNative": cfprApFabricVlanEpIsNative,
       "cfprApFabricVlanEpLocale": cfprApFabricVlanEpLocale,
       "cfprApFabricVlanEpName": cfprApFabricVlanEpName,
       "cfprApFabricVlanEpOperState": cfprApFabricVlanEpOperState,
       "cfprApFabricVlanEpOverlapStateForA": cfprApFabricVlanEpOverlapStateForA,
       "cfprApFabricVlanEpOverlapStateForB": cfprApFabricVlanEpOverlapStateForB,
       "cfprApFabricVlanEpPeerDn": cfprApFabricVlanEpPeerDn,
       "cfprApFabricVlanEpPolicyOwner": cfprApFabricVlanEpPolicyOwner,
       "cfprApFabricVlanEpPubNwDn": cfprApFabricVlanEpPubNwDn,
       "cfprApFabricVlanEpPubNwId": cfprApFabricVlanEpPubNwId,
       "cfprApFabricVlanEpPubNwName": cfprApFabricVlanEpPubNwName,
       "cfprApFabricVlanEpSharing": cfprApFabricVlanEpSharing,
       "cfprApFabricVlanEpSwitchId": cfprApFabricVlanEpSwitchId,
       "cfprApFabricVlanEpTransport": cfprApFabricVlanEpTransport,
       "cfprApFabricVlanEpType": cfprApFabricVlanEpType,
       "cfprApFabricVlanGroupReqTable": cfprApFabricVlanGroupReqTable,
       "cfprApFabricVlanGroupReqEntry": cfprApFabricVlanGroupReqEntry,
       "cfprApFabricVlanGroupReqInstanceId": cfprApFabricVlanGroupReqInstanceId,
       "cfprApFabricVlanGroupReqDn": cfprApFabricVlanGroupReqDn,
       "cfprApFabricVlanGroupReqRn": cfprApFabricVlanGroupReqRn,
       "cfprApFabricVlanGroupReqConfigIssues": cfprApFabricVlanGroupReqConfigIssues,
       "cfprApFabricVlanGroupReqName": cfprApFabricVlanGroupReqName,
       "cfprApFabricVlanGroupReqType": cfprApFabricVlanGroupReqType,
       "cfprApFabricVlanPermitTable": cfprApFabricVlanPermitTable,
       "cfprApFabricVlanPermitEntry": cfprApFabricVlanPermitEntry,
       "cfprApFabricVlanPermitInstanceId": cfprApFabricVlanPermitInstanceId,
       "cfprApFabricVlanPermitDn": cfprApFabricVlanPermitDn,
       "cfprApFabricVlanPermitRn": cfprApFabricVlanPermitRn,
       "cfprApFabricVlanPermitCloud": cfprApFabricVlanPermitCloud,
       "cfprApFabricVlanPermitName": cfprApFabricVlanPermitName,
       "cfprApFabricVlanPermitSwitchId": cfprApFabricVlanPermitSwitchId,
       "cfprApFabricVlanReqTable": cfprApFabricVlanReqTable,
       "cfprApFabricVlanReqEntry": cfprApFabricVlanReqEntry,
       "cfprApFabricVlanReqInstanceId": cfprApFabricVlanReqInstanceId,
       "cfprApFabricVlanReqDn": cfprApFabricVlanReqDn,
       "cfprApFabricVlanReqRn": cfprApFabricVlanReqRn,
       "cfprApFabricVlanReqConfigIssues": cfprApFabricVlanReqConfigIssues,
       "cfprApFabricVlanReqName": cfprApFabricVlanReqName,
       "cfprApFabricVlanReqType": cfprApFabricVlanReqType,
       "cfprApFabricVnetEpSyncEpTable": cfprApFabricVnetEpSyncEpTable,
       "cfprApFabricVnetEpSyncEpEntry": cfprApFabricVnetEpSyncEpEntry,
       "cfprApFabricVnetEpSyncEpInstanceId": cfprApFabricVnetEpSyncEpInstanceId,
       "cfprApFabricVnetEpSyncEpDn": cfprApFabricVnetEpSyncEpDn,
       "cfprApFabricVnetEpSyncEpRn": cfprApFabricVnetEpSyncEpRn,
       "cfprApFabricVnetEpSyncEpFsmDescr": cfprApFabricVnetEpSyncEpFsmDescr,
       "cfprApFabricVnetEpSyncEpFsmPrev": cfprApFabricVnetEpSyncEpFsmPrev,
       "cfprApFabricVnetEpSyncEpFsmProgr": cfprApFabricVnetEpSyncEpFsmProgr,
       "cfprApFabricVnetEpSyncEpFsmRmtInvErrCode": cfprApFabricVnetEpSyncEpFsmRmtInvErrCode,
       "cfprApFabricVnetEpSyncEpFsmRmtInvErrDescr": cfprApFabricVnetEpSyncEpFsmRmtInvErrDescr,
       "cfprApFabricVnetEpSyncEpFsmRmtInvRslt": cfprApFabricVnetEpSyncEpFsmRmtInvRslt,
       "cfprApFabricVnetEpSyncEpFsmStageDescr": cfprApFabricVnetEpSyncEpFsmStageDescr,
       "cfprApFabricVnetEpSyncEpFsmStamp": cfprApFabricVnetEpSyncEpFsmStamp,
       "cfprApFabricVnetEpSyncEpFsmStatus": cfprApFabricVnetEpSyncEpFsmStatus,
       "cfprApFabricVnetEpSyncEpFsmTry": cfprApFabricVnetEpSyncEpFsmTry,
       "cfprApFabricVnetEpSyncEpGenNumSync": cfprApFabricVnetEpSyncEpGenNumSync,
       "cfprApFabricVnetEpSyncEpId": cfprApFabricVnetEpSyncEpId,
       "cfprApFabricVnetEpSyncEpIsChangedObjectUpdate": cfprApFabricVnetEpSyncEpIsChangedObjectUpdate,
       "cfprApFabricVnetEpSyncEpFsmTable": cfprApFabricVnetEpSyncEpFsmTable,
       "cfprApFabricVnetEpSyncEpFsmEntry": cfprApFabricVnetEpSyncEpFsmEntry,
       "cfprApFabricVnetEpSyncEpFsmInstanceId": cfprApFabricVnetEpSyncEpFsmInstanceId,
       "cfprApFabricVnetEpSyncEpFsmDn": cfprApFabricVnetEpSyncEpFsmDn,
       "cfprApFabricVnetEpSyncEpFsmRn": cfprApFabricVnetEpSyncEpFsmRn,
       "cfprApFabricVnetEpSyncEpFsmCompletionTime": cfprApFabricVnetEpSyncEpFsmCompletionTime,
       "cfprApFabricVnetEpSyncEpFsmCurrentFsm": cfprApFabricVnetEpSyncEpFsmCurrentFsm,
       "cfprApFabricVnetEpSyncEpFsmDescrData": cfprApFabricVnetEpSyncEpFsmDescrData,
       "cfprApFabricVnetEpSyncEpFsmFsmStatus": cfprApFabricVnetEpSyncEpFsmFsmStatus,
       "cfprApFabricVnetEpSyncEpFsmProgress": cfprApFabricVnetEpSyncEpFsmProgress,
       "cfprApFabricVnetEpSyncEpFsmRmtErrCode": cfprApFabricVnetEpSyncEpFsmRmtErrCode,
       "cfprApFabricVnetEpSyncEpFsmRmtErrDescr": cfprApFabricVnetEpSyncEpFsmRmtErrDescr,
       "cfprApFabricVnetEpSyncEpFsmRmtRslt": cfprApFabricVnetEpSyncEpFsmRmtRslt,
       "cfprApFabricVnetEpSyncEpFsmStageTable": cfprApFabricVnetEpSyncEpFsmStageTable,
       "cfprApFabricVnetEpSyncEpFsmStageEntry": cfprApFabricVnetEpSyncEpFsmStageEntry,
       "cfprApFabricVnetEpSyncEpFsmStageInstanceId": cfprApFabricVnetEpSyncEpFsmStageInstanceId,
       "cfprApFabricVnetEpSyncEpFsmStageDn": cfprApFabricVnetEpSyncEpFsmStageDn,
       "cfprApFabricVnetEpSyncEpFsmStageRn": cfprApFabricVnetEpSyncEpFsmStageRn,
       "cfprApFabricVnetEpSyncEpFsmStageDescrData": cfprApFabricVnetEpSyncEpFsmStageDescrData,
       "cfprApFabricVnetEpSyncEpFsmStageLastUpdateTime": cfprApFabricVnetEpSyncEpFsmStageLastUpdateTime,
       "cfprApFabricVnetEpSyncEpFsmStageName": cfprApFabricVnetEpSyncEpFsmStageName,
       "cfprApFabricVnetEpSyncEpFsmStageOrder": cfprApFabricVnetEpSyncEpFsmStageOrder,
       "cfprApFabricVnetEpSyncEpFsmStageRetry": cfprApFabricVnetEpSyncEpFsmStageRetry,
       "cfprApFabricVnetEpSyncEpFsmStageStageStatus": cfprApFabricVnetEpSyncEpFsmStageStageStatus,
       "cfprApFabricVnetEpSyncEpFsmTaskTable": cfprApFabricVnetEpSyncEpFsmTaskTable,
       "cfprApFabricVnetEpSyncEpFsmTaskEntry": cfprApFabricVnetEpSyncEpFsmTaskEntry,
       "cfprApFabricVnetEpSyncEpFsmTaskInstanceId": cfprApFabricVnetEpSyncEpFsmTaskInstanceId,
       "cfprApFabricVnetEpSyncEpFsmTaskDn": cfprApFabricVnetEpSyncEpFsmTaskDn,
       "cfprApFabricVnetEpSyncEpFsmTaskRn": cfprApFabricVnetEpSyncEpFsmTaskRn,
       "cfprApFabricVnetEpSyncEpFsmTaskCompletion": cfprApFabricVnetEpSyncEpFsmTaskCompletion,
       "cfprApFabricVnetEpSyncEpFsmTaskFlags": cfprApFabricVnetEpSyncEpFsmTaskFlags,
       "cfprApFabricVnetEpSyncEpFsmTaskItem": cfprApFabricVnetEpSyncEpFsmTaskItem,
       "cfprApFabricVnetEpSyncEpFsmTaskSeqId": cfprApFabricVnetEpSyncEpFsmTaskSeqId,
       "cfprApFabricVsanTable": cfprApFabricVsanTable,
       "cfprApFabricVsanEntry": cfprApFabricVsanEntry,
       "cfprApFabricVsanInstanceId": cfprApFabricVsanInstanceId,
       "cfprApFabricVsanDn": cfprApFabricVsanDn,
       "cfprApFabricVsanRn": cfprApFabricVsanRn,
       "cfprApFabricVsanDefaultZoning": cfprApFabricVsanDefaultZoning,
       "cfprApFabricVsanEpDn": cfprApFabricVsanEpDn,
       "cfprApFabricVsanFcZoneSharingMode": cfprApFabricVsanFcZoneSharingMode,
       "cfprApFabricVsanFcoeVlan": cfprApFabricVsanFcoeVlan,
       "cfprApFabricVsanFltAggr": cfprApFabricVsanFltAggr,
       "cfprApFabricVsanGlobal": cfprApFabricVsanGlobal,
       "cfprApFabricVsanId": cfprApFabricVsanId,
       "cfprApFabricVsanIfRole": cfprApFabricVsanIfRole,
       "cfprApFabricVsanIfType": cfprApFabricVsanIfType,
       "cfprApFabricVsanLocal": cfprApFabricVsanLocal,
       "cfprApFabricVsanLocale": cfprApFabricVsanLocale,
       "cfprApFabricVsanName": cfprApFabricVsanName,
       "cfprApFabricVsanOperState": cfprApFabricVsanOperState,
       "cfprApFabricVsanPeerDn": cfprApFabricVsanPeerDn,
       "cfprApFabricVsanPolicyOwner": cfprApFabricVsanPolicyOwner,
       "cfprApFabricVsanSwitchId": cfprApFabricVsanSwitchId,
       "cfprApFabricVsanTransport": cfprApFabricVsanTransport,
       "cfprApFabricVsanType": cfprApFabricVsanType,
       "cfprApFabricVsanZoningState": cfprApFabricVsanZoningState,
       "cfprApFabricVsanEpTable": cfprApFabricVsanEpTable,
       "cfprApFabricVsanEpEntry": cfprApFabricVsanEpEntry,
       "cfprApFabricVsanEpInstanceId": cfprApFabricVsanEpInstanceId,
       "cfprApFabricVsanEpDnData": cfprApFabricVsanEpDnData,
       "cfprApFabricVsanEpRn": cfprApFabricVsanEpRn,
       "cfprApFabricVsanEpEpDn": cfprApFabricVsanEpEpDn,
       "cfprApFabricVsanEpFcoeVlan": cfprApFabricVsanEpFcoeVlan,
       "cfprApFabricVsanEpId": cfprApFabricVsanEpId,
       "cfprApFabricVsanEpIfRole": cfprApFabricVsanEpIfRole,
       "cfprApFabricVsanEpIfType": cfprApFabricVsanEpIfType,
       "cfprApFabricVsanEpLocale": cfprApFabricVsanEpLocale,
       "cfprApFabricVsanEpName": cfprApFabricVsanEpName,
       "cfprApFabricVsanEpOperState": cfprApFabricVsanEpOperState,
       "cfprApFabricVsanEpPeerDn": cfprApFabricVsanEpPeerDn,
       "cfprApFabricVsanEpPolicyOwner": cfprApFabricVsanEpPolicyOwner,
       "cfprApFabricVsanEpSwitchId": cfprApFabricVsanEpSwitchId,
       "cfprApFabricVsanEpTransport": cfprApFabricVsanEpTransport,
       "cfprApFabricVsanEpType": cfprApFabricVsanEpType,
       "cfprApFabricVsanEpZoningState": cfprApFabricVsanEpZoningState,
       "cfprApFabricVsanMembershipTable": cfprApFabricVsanMembershipTable,
       "cfprApFabricVsanMembershipEntry": cfprApFabricVsanMembershipEntry,
       "cfprApFabricVsanMembershipInstanceId": cfprApFabricVsanMembershipInstanceId,
       "cfprApFabricVsanMembershipDn": cfprApFabricVsanMembershipDn,
       "cfprApFabricVsanMembershipRn": cfprApFabricVsanMembershipRn,
       "cfprApFabricVsanMembershipMemberStatus": cfprApFabricVsanMembershipMemberStatus,
       "cfprApFabricVsanMembershipParentAdminState": cfprApFabricVsanMembershipParentAdminState,
       "cfprApFabricVsanMembershipStateQual": cfprApFabricVsanMembershipStateQual,
       "cfprApFabricVsanMembershipVsanId": cfprApFabricVsanMembershipVsanId,
       "cfprApFabricZoneIdUniverseTable": cfprApFabricZoneIdUniverseTable,
       "cfprApFabricZoneIdUniverseEntry": cfprApFabricZoneIdUniverseEntry,
       "cfprApFabricZoneIdUniverseInstanceId": cfprApFabricZoneIdUniverseInstanceId,
       "cfprApFabricZoneIdUniverseDn": cfprApFabricZoneIdUniverseDn,
       "cfprApFabricZoneIdUniverseRn": cfprApFabricZoneIdUniverseRn}
)
