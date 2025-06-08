# SNMP MIB module (CISCO-FIREPOWER-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-FABRIC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:11 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprComputeDecommissionState,
 CfprComputeDiscovery,
 CfprConditionRemoteInvRslt,
 CfprEquipmentBoardAggregationRole,
 CfprEquipmentConnectionStatus,
 CfprEquipmentEthPortSpeedCap,
 CfprEquipmentFabricEpType,
 CfprEquipmentSlotStatus,
 CfprFabricADceSwSrvEpTransport,
 CfprFabricAEthEstcEpIfRole,
 CfprFabricAEthEstcEpTransport,
 CfprFabricAEthEstcEpType,
 CfprFabricAEthLanEpTransport,
 CfprFabricAFcSanEpTransport,
 CfprFabricAFcoeSanEpTransport,
 CfprFabricAVlanAssocPrimaryVlanSwitchId,
 CfprFabricAVlanSharing,
 CfprFabricAVlanTransport,
 CfprFabricAVlanType,
 CfprFabricAVsanTransport,
 CfprFabricAVsanType,
 CfprFabricAccessType,
 CfprFabricAdminState,
 CfprFabricAllowedVlanType,
 CfprFabricBHVlanSwitchId,
 CfprFabricBladeLifeCycle,
 CfprFabricBreakoutPortId,
 CfprFabricBreakoutSlotId,
 CfprFabricBreakoutType,
 CfprFabricCIoEpAdminState,
 CfprFabricCIoEpIfType,
 CfprFabricCdpLinkPolicyAdminState,
 CfprFabricCloudType,
 CfprFabricComputeEpIfRole,
 CfprFabricComputeEpType,
 CfprFabricComputePhEpAdminState,
 CfprFabricComputeSlotEpFsmCurrentFsm,
 CfprFabricComputeSlotEpFsmStageName,
 CfprFabricComputeSlotEpFsmTaskItem,
 CfprFabricComputeSlotEpSlotId,
 CfprFabricConfMode,
 CfprFabricConfState,
 CfprFabricConfigState,
 CfprFabricDceSwSrvEpPortId,
 CfprFabricDceSwSrvEpSlotId,
 CfprFabricDceSwSrvPcAdminState,
 CfprFabricDceSwSrvPcEpPortId,
 CfprFabricDceSwSrvPcEpSlotId,
 CfprFabricDceSwSrvPcPortId,
 CfprFabricDceSwSrvPcTransport,
 CfprFabricDefaultZoningState,
 CfprFabricEpMgrFsmCurrentFsm,
 CfprFabricEpMgrFsmStageName,
 CfprFabricEpMgrFsmTaskFlags,
 CfprFabricEpMgrFsmTaskItem,
 CfprFabricEstcPcIfRole,
 CfprFabricEstcPcType,
 CfprFabricEthCdpPolicyProtocol,
 CfprFabricEthEstcEpPortId,
 CfprFabricEthEstcEpPrio,
 CfprFabricEthEstcEpSlotId,
 CfprFabricEthEstcEpTransport,
 CfprFabricEthEstcEpType,
 CfprFabricEthEstcOperPortMode,
 CfprFabricEthEstcPcEpPortId,
 CfprFabricEthEstcPcEpSlotId,
 CfprFabricEthEstcPcTransport,
 CfprFabricEthEstcPortMode,
 CfprFabricEthEstcTransport,
 CfprFabricEthEstcType,
 CfprFabricEthLanEpAdminState,
 CfprFabricEthLanEpInlineState,
 CfprFabricEthLanEpServiceState,
 CfprFabricEthLanEpVlanStatus,
 CfprFabricEthLanPcAdminState,
 CfprFabricEthLanPcInlineState,
 CfprFabricEthLanPcLacpDetach,
 CfprFabricEthLanPcServiceState,
 CfprFabricEthLanPcTransport,
 CfprFabricEthLanPcVlanStatus,
 CfprFabricEthLanTransport,
 CfprFabricEthLinkPolicyType,
 CfprFabricEthMonDestEpAdminSpeed,
 CfprFabricEthMonDestEpIfRole,
 CfprFabricEthMonDestEpPortId,
 CfprFabricEthMonDestEpSlotId,
 CfprFabricEthMonDestEpType,
 CfprFabricEthMonFiltEpType,
 CfprFabricEthMonFiltRefType,
 CfprFabricEthMonLanTransport,
 CfprFabricEthMonLanType,
 CfprFabricEthMonSrcEpType,
 CfprFabricEthMonSrcRefType,
 CfprFabricEthMonTransport,
 CfprFabricEthMonType,
 CfprFabricEthPcProtocol,
 CfprFabricEthSourceType,
 CfprFabricEthTargetEpTransport,
 CfprFabricEthUdldPolicyProtocol,
 CfprFabricEthVlanPcTransport,
 CfprFabricExternalEpAdminState,
 CfprFabricExternalEpLocale,
 CfprFabricExternalLocale,
 CfprFabricExternalPcLocale,
 CfprFabricFcSanEpPortId,
 CfprFabricFcSanEpSlotId,
 CfprFabricFcSanPcEpPortId,
 CfprFabricFcSanPcEpSlotId,
 CfprFabricFcSanPcTransport,
 CfprFabricFcSanTransport,
 CfprFabricFcSanUplinkTrunking,
 CfprFabricFcVsanPcTransport,
 CfprFabricFcVsanPortEpPortId,
 CfprFabricFcVsanPortEpSlotId,
 CfprFabricFcZoneSharingMode,
 CfprFabricFcoeSanEpPortId,
 CfprFabricFcoeSanEpSlotId,
 CfprFabricFcoeSanPcEpPortId,
 CfprFabricFcoeSanPcEpSlotId,
 CfprFabricFcoeSanPcTransport,
 CfprFabricFcoeVsanPcTransport,
 CfprFabricFcoeVsanPortEpPortId,
 CfprFabricFcoeVsanPortEpSlotId,
 CfprFabricFillPattern,
 CfprFabricInternalDceSrvTransport,
 CfprFabricInternalDceSrvType,
 CfprFabricInternalEpAdminState,
 CfprFabricInternalEpLocale,
 CfprFabricInternalLocale,
 CfprFabricInternalPcLocale,
 CfprFabricLacpMode,
 CfprFabricLacpRate,
 CfprFabricLacpSuspend,
 CfprFabricLanCloudFsmCurrentFsm,
 CfprFabricLanCloudFsmStageName,
 CfprFabricLanCloudFsmTaskItem,
 CfprFabricLanCloudVlanCompression,
 CfprFabricLanEpIfRole,
 CfprFabricLanEpType,
 CfprFabricLanPcIfRole,
 CfprFabricLanPcType,
 CfprFabricLanType,
 CfprFabricLifeCycle,
 CfprFabricMemberStatus,
 CfprFabricMembershipStatus,
 CfprFabricMonAdminState,
 CfprFabricMonOperState,
 CfprFabricMonOperStateReason,
 CfprFabricNetGroupSwitchId,
 CfprFabricNetGroupType,
 CfprFabricOwner,
 CfprFabricPIoEpIfType,
 CfprFabricPIoEpOperState,
 CfprFabricPIoEpPortId,
 CfprFabricPIoEpSlotId,
 CfprFabricPathEpIfType,
 CfprFabricPathEpLocale,
 CfprFabricPcConfigStatus,
 CfprFabricPcMode,
 CfprFabricPcModeState,
 CfprFabricPktCaptureAppSlotId,
 CfprFabricPoolMemberConfigIssues,
 CfprFabricQosPrio,
 CfprFabricQuerierType,
 CfprFabricRecoveryAction,
 CfprFabricReqIssues,
 CfprFabricSSAPortType,
 CfprFabricSSASubPortType,
 CfprFabricSanCloudFsmCurrentFsm,
 CfprFabricSanCloudFsmStageName,
 CfprFabricSanCloudFsmTaskItem,
 CfprFabricSanEpIfRole,
 CfprFabricSanEpType,
 CfprFabricSanPcIfRole,
 CfprFabricSanPcType,
 CfprFabricSanType,
 CfprFabricSlotAdminState,
 CfprFabricSnoopingType,
 CfprFabricSpannedCluster,
 CfprFabricSspEthMonAppendFlag,
 CfprFabricSspEthMonDelAllSessEnabledState,
 CfprFabricSspLanMonCloudDelAllSess,
 CfprFabricSspMonAdminState,
 CfprFabricSspMonDelPcap,
 CfprFabricSspMonOperState,
 CfprFabricSspMonOperStateReason,
 CfprFabricStatus,
 CfprFabricSubGroupAggrPortId,
 CfprFabricSubGroupConfigState,
 CfprFabricSubGroupSlotId,
 CfprFabricSvcStateDownReason,
 CfprFabricSwChEpIfRole,
 CfprFabricSwChEpType,
 CfprFabricSwChPhEpAdminState,
 CfprFabricSwSrvEpIfRole,
 CfprFabricSwSrvEpType,
 CfprFabricSwSrvPcIfRole,
 CfprFabricSwSrvPcType,
 CfprFabricSwSubGroupAggrPortId,
 CfprFabricSwSubGroupConfigState,
 CfprFabricSwSubGroupSlotId,
 CfprFabricSwitchingMode,
 CfprFabricTargetEpType,
 CfprFabricTargetStatus,
 CfprFabricTrafficDirection,
 CfprFabricUdldLinkPolicyAdminState,
 CfprFabricUdldLinkPolicyMode,
 CfprFabricUdldOperState,
 CfprFabricVConInstType,
 CfprFabricVConMappingScheme,
 CfprFabricVConPlacementPref,
 CfprFabricVConSelectPref,
 CfprFabricVConSharePref,
 CfprFabricVConTransportPref,
 CfprFabricVlanAssocPrimaryVlanState,
 CfprFabricVlanCompType,
 CfprFabricVlanConfigIssues,
 CfprFabricVlanOperState,
 CfprFabricVlanOverlapState,
 CfprFabricVlanSwitchId,
 CfprFabricVnetEpIfRole,
 CfprFabricVnetEpLocale,
 CfprFabricVnetEpPolicyOwner,
 CfprFabricVnetEpSyncEpFsmCurrentFsm,
 CfprFabricVnetEpSyncEpFsmStageName,
 CfprFabricVnetEpSyncEpFsmTaskItem,
 CfprFabricVsanOperState,
 CfprFabricVsanSwitchId,
 CfprFabricWarnings,
 CfprFabricZoningState,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprLicenseState,
 CfprLsOperState,
 CfprNetworkConnectionType,
 CfprNetworkLocale,
 CfprNetworkPortOperState,
 CfprNetworkPortRole,
 CfprNetworkSide,
 CfprNetworkSwitchId,
 CfprNetworkTransport,
 CfprNetworkVnetEpIfType,
 CfprNhTpHashType,
 CfprPolicyPolicyOwner,
 CfprPoolPoolAssignmentOrder,
 CfprPortDuplex,
 CfprPortEthAdminSpeed,
 CfprPortEthSpeed,
 CfprPortSpeed,
 CfprQosPriority,
 CfprSwPktCaptureLifeCycle) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprComputeDecommissionState",
    "CfprComputeDiscovery",
    "CfprConditionRemoteInvRslt",
    "CfprEquipmentBoardAggregationRole",
    "CfprEquipmentConnectionStatus",
    "CfprEquipmentEthPortSpeedCap",
    "CfprEquipmentFabricEpType",
    "CfprEquipmentSlotStatus",
    "CfprFabricADceSwSrvEpTransport",
    "CfprFabricAEthEstcEpIfRole",
    "CfprFabricAEthEstcEpTransport",
    "CfprFabricAEthEstcEpType",
    "CfprFabricAEthLanEpTransport",
    "CfprFabricAFcSanEpTransport",
    "CfprFabricAFcoeSanEpTransport",
    "CfprFabricAVlanAssocPrimaryVlanSwitchId",
    "CfprFabricAVlanSharing",
    "CfprFabricAVlanTransport",
    "CfprFabricAVlanType",
    "CfprFabricAVsanTransport",
    "CfprFabricAVsanType",
    "CfprFabricAccessType",
    "CfprFabricAdminState",
    "CfprFabricAllowedVlanType",
    "CfprFabricBHVlanSwitchId",
    "CfprFabricBladeLifeCycle",
    "CfprFabricBreakoutPortId",
    "CfprFabricBreakoutSlotId",
    "CfprFabricBreakoutType",
    "CfprFabricCIoEpAdminState",
    "CfprFabricCIoEpIfType",
    "CfprFabricCdpLinkPolicyAdminState",
    "CfprFabricCloudType",
    "CfprFabricComputeEpIfRole",
    "CfprFabricComputeEpType",
    "CfprFabricComputePhEpAdminState",
    "CfprFabricComputeSlotEpFsmCurrentFsm",
    "CfprFabricComputeSlotEpFsmStageName",
    "CfprFabricComputeSlotEpFsmTaskItem",
    "CfprFabricComputeSlotEpSlotId",
    "CfprFabricConfMode",
    "CfprFabricConfState",
    "CfprFabricConfigState",
    "CfprFabricDceSwSrvEpPortId",
    "CfprFabricDceSwSrvEpSlotId",
    "CfprFabricDceSwSrvPcAdminState",
    "CfprFabricDceSwSrvPcEpPortId",
    "CfprFabricDceSwSrvPcEpSlotId",
    "CfprFabricDceSwSrvPcPortId",
    "CfprFabricDceSwSrvPcTransport",
    "CfprFabricDefaultZoningState",
    "CfprFabricEpMgrFsmCurrentFsm",
    "CfprFabricEpMgrFsmStageName",
    "CfprFabricEpMgrFsmTaskFlags",
    "CfprFabricEpMgrFsmTaskItem",
    "CfprFabricEstcPcIfRole",
    "CfprFabricEstcPcType",
    "CfprFabricEthCdpPolicyProtocol",
    "CfprFabricEthEstcEpPortId",
    "CfprFabricEthEstcEpPrio",
    "CfprFabricEthEstcEpSlotId",
    "CfprFabricEthEstcEpTransport",
    "CfprFabricEthEstcEpType",
    "CfprFabricEthEstcOperPortMode",
    "CfprFabricEthEstcPcEpPortId",
    "CfprFabricEthEstcPcEpSlotId",
    "CfprFabricEthEstcPcTransport",
    "CfprFabricEthEstcPortMode",
    "CfprFabricEthEstcTransport",
    "CfprFabricEthEstcType",
    "CfprFabricEthLanEpAdminState",
    "CfprFabricEthLanEpInlineState",
    "CfprFabricEthLanEpServiceState",
    "CfprFabricEthLanEpVlanStatus",
    "CfprFabricEthLanPcAdminState",
    "CfprFabricEthLanPcInlineState",
    "CfprFabricEthLanPcLacpDetach",
    "CfprFabricEthLanPcServiceState",
    "CfprFabricEthLanPcTransport",
    "CfprFabricEthLanPcVlanStatus",
    "CfprFabricEthLanTransport",
    "CfprFabricEthLinkPolicyType",
    "CfprFabricEthMonDestEpAdminSpeed",
    "CfprFabricEthMonDestEpIfRole",
    "CfprFabricEthMonDestEpPortId",
    "CfprFabricEthMonDestEpSlotId",
    "CfprFabricEthMonDestEpType",
    "CfprFabricEthMonFiltEpType",
    "CfprFabricEthMonFiltRefType",
    "CfprFabricEthMonLanTransport",
    "CfprFabricEthMonLanType",
    "CfprFabricEthMonSrcEpType",
    "CfprFabricEthMonSrcRefType",
    "CfprFabricEthMonTransport",
    "CfprFabricEthMonType",
    "CfprFabricEthPcProtocol",
    "CfprFabricEthSourceType",
    "CfprFabricEthTargetEpTransport",
    "CfprFabricEthUdldPolicyProtocol",
    "CfprFabricEthVlanPcTransport",
    "CfprFabricExternalEpAdminState",
    "CfprFabricExternalEpLocale",
    "CfprFabricExternalLocale",
    "CfprFabricExternalPcLocale",
    "CfprFabricFcSanEpPortId",
    "CfprFabricFcSanEpSlotId",
    "CfprFabricFcSanPcEpPortId",
    "CfprFabricFcSanPcEpSlotId",
    "CfprFabricFcSanPcTransport",
    "CfprFabricFcSanTransport",
    "CfprFabricFcSanUplinkTrunking",
    "CfprFabricFcVsanPcTransport",
    "CfprFabricFcVsanPortEpPortId",
    "CfprFabricFcVsanPortEpSlotId",
    "CfprFabricFcZoneSharingMode",
    "CfprFabricFcoeSanEpPortId",
    "CfprFabricFcoeSanEpSlotId",
    "CfprFabricFcoeSanPcEpPortId",
    "CfprFabricFcoeSanPcEpSlotId",
    "CfprFabricFcoeSanPcTransport",
    "CfprFabricFcoeVsanPcTransport",
    "CfprFabricFcoeVsanPortEpPortId",
    "CfprFabricFcoeVsanPortEpSlotId",
    "CfprFabricFillPattern",
    "CfprFabricInternalDceSrvTransport",
    "CfprFabricInternalDceSrvType",
    "CfprFabricInternalEpAdminState",
    "CfprFabricInternalEpLocale",
    "CfprFabricInternalLocale",
    "CfprFabricInternalPcLocale",
    "CfprFabricLacpMode",
    "CfprFabricLacpRate",
    "CfprFabricLacpSuspend",
    "CfprFabricLanCloudFsmCurrentFsm",
    "CfprFabricLanCloudFsmStageName",
    "CfprFabricLanCloudFsmTaskItem",
    "CfprFabricLanCloudVlanCompression",
    "CfprFabricLanEpIfRole",
    "CfprFabricLanEpType",
    "CfprFabricLanPcIfRole",
    "CfprFabricLanPcType",
    "CfprFabricLanType",
    "CfprFabricLifeCycle",
    "CfprFabricMemberStatus",
    "CfprFabricMembershipStatus",
    "CfprFabricMonAdminState",
    "CfprFabricMonOperState",
    "CfprFabricMonOperStateReason",
    "CfprFabricNetGroupSwitchId",
    "CfprFabricNetGroupType",
    "CfprFabricOwner",
    "CfprFabricPIoEpIfType",
    "CfprFabricPIoEpOperState",
    "CfprFabricPIoEpPortId",
    "CfprFabricPIoEpSlotId",
    "CfprFabricPathEpIfType",
    "CfprFabricPathEpLocale",
    "CfprFabricPcConfigStatus",
    "CfprFabricPcMode",
    "CfprFabricPcModeState",
    "CfprFabricPktCaptureAppSlotId",
    "CfprFabricPoolMemberConfigIssues",
    "CfprFabricQosPrio",
    "CfprFabricQuerierType",
    "CfprFabricRecoveryAction",
    "CfprFabricReqIssues",
    "CfprFabricSSAPortType",
    "CfprFabricSSASubPortType",
    "CfprFabricSanCloudFsmCurrentFsm",
    "CfprFabricSanCloudFsmStageName",
    "CfprFabricSanCloudFsmTaskItem",
    "CfprFabricSanEpIfRole",
    "CfprFabricSanEpType",
    "CfprFabricSanPcIfRole",
    "CfprFabricSanPcType",
    "CfprFabricSanType",
    "CfprFabricSlotAdminState",
    "CfprFabricSnoopingType",
    "CfprFabricSpannedCluster",
    "CfprFabricSspEthMonAppendFlag",
    "CfprFabricSspEthMonDelAllSessEnabledState",
    "CfprFabricSspLanMonCloudDelAllSess",
    "CfprFabricSspMonAdminState",
    "CfprFabricSspMonDelPcap",
    "CfprFabricSspMonOperState",
    "CfprFabricSspMonOperStateReason",
    "CfprFabricStatus",
    "CfprFabricSubGroupAggrPortId",
    "CfprFabricSubGroupConfigState",
    "CfprFabricSubGroupSlotId",
    "CfprFabricSvcStateDownReason",
    "CfprFabricSwChEpIfRole",
    "CfprFabricSwChEpType",
    "CfprFabricSwChPhEpAdminState",
    "CfprFabricSwSrvEpIfRole",
    "CfprFabricSwSrvEpType",
    "CfprFabricSwSrvPcIfRole",
    "CfprFabricSwSrvPcType",
    "CfprFabricSwSubGroupAggrPortId",
    "CfprFabricSwSubGroupConfigState",
    "CfprFabricSwSubGroupSlotId",
    "CfprFabricSwitchingMode",
    "CfprFabricTargetEpType",
    "CfprFabricTargetStatus",
    "CfprFabricTrafficDirection",
    "CfprFabricUdldLinkPolicyAdminState",
    "CfprFabricUdldLinkPolicyMode",
    "CfprFabricUdldOperState",
    "CfprFabricVConInstType",
    "CfprFabricVConMappingScheme",
    "CfprFabricVConPlacementPref",
    "CfprFabricVConSelectPref",
    "CfprFabricVConSharePref",
    "CfprFabricVConTransportPref",
    "CfprFabricVlanAssocPrimaryVlanState",
    "CfprFabricVlanCompType",
    "CfprFabricVlanConfigIssues",
    "CfprFabricVlanOperState",
    "CfprFabricVlanOverlapState",
    "CfprFabricVlanSwitchId",
    "CfprFabricVnetEpIfRole",
    "CfprFabricVnetEpLocale",
    "CfprFabricVnetEpPolicyOwner",
    "CfprFabricVnetEpSyncEpFsmCurrentFsm",
    "CfprFabricVnetEpSyncEpFsmStageName",
    "CfprFabricVnetEpSyncEpFsmTaskItem",
    "CfprFabricVsanOperState",
    "CfprFabricVsanSwitchId",
    "CfprFabricWarnings",
    "CfprFabricZoningState",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprLicenseState",
    "CfprLsOperState",
    "CfprNetworkConnectionType",
    "CfprNetworkLocale",
    "CfprNetworkPortOperState",
    "CfprNetworkPortRole",
    "CfprNetworkSide",
    "CfprNetworkSwitchId",
    "CfprNetworkTransport",
    "CfprNetworkVnetEpIfType",
    "CfprNhTpHashType",
    "CfprPolicyPolicyOwner",
    "CfprPoolPoolAssignmentOrder",
    "CfprPortDuplex",
    "CfprPortEthAdminSpeed",
    "CfprPortEthSpeed",
    "CfprPortSpeed",
    "CfprQosPriority",
    "CfprSwPktCaptureLifeCycle")

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

cfprFabricObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprFabricBHVlanTable_Object = MibTable
cfprFabricBHVlanTable = _CfprFabricBHVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1)
)
if mibBuilder.loadTexts:
    cfprFabricBHVlanTable.setStatus("current")
_CfprFabricBHVlanEntry_Object = MibTableRow
cfprFabricBHVlanEntry = _CfprFabricBHVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1)
)
cfprFabricBHVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricBHVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricBHVlanEntry.setStatus("current")
_CfprFabricBHVlanInstanceId_Type = CfprManagedObjectId
_CfprFabricBHVlanInstanceId_Object = MibTableColumn
cfprFabricBHVlanInstanceId = _CfprFabricBHVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 1),
    _CfprFabricBHVlanInstanceId_Type()
)
cfprFabricBHVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricBHVlanInstanceId.setStatus("current")
_CfprFabricBHVlanDn_Type = CfprManagedObjectDn
_CfprFabricBHVlanDn_Object = MibTableColumn
cfprFabricBHVlanDn = _CfprFabricBHVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 2),
    _CfprFabricBHVlanDn_Type()
)
cfprFabricBHVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanDn.setStatus("current")
_CfprFabricBHVlanRn_Type = SnmpAdminString
_CfprFabricBHVlanRn_Object = MibTableColumn
cfprFabricBHVlanRn = _CfprFabricBHVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 3),
    _CfprFabricBHVlanRn_Type()
)
cfprFabricBHVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanRn.setStatus("current")
_CfprFabricBHVlanAssocPrimaryVlanState_Type = CfprFabricVlanAssocPrimaryVlanState
_CfprFabricBHVlanAssocPrimaryVlanState_Object = MibTableColumn
cfprFabricBHVlanAssocPrimaryVlanState = _CfprFabricBHVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 4),
    _CfprFabricBHVlanAssocPrimaryVlanState_Type()
)
cfprFabricBHVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanAssocPrimaryVlanState.setStatus("current")
_CfprFabricBHVlanAssocPrimaryVlanSwitchId_Type = CfprFabricAVlanAssocPrimaryVlanSwitchId
_CfprFabricBHVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprFabricBHVlanAssocPrimaryVlanSwitchId = _CfprFabricBHVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 5),
    _CfprFabricBHVlanAssocPrimaryVlanSwitchId_Type()
)
cfprFabricBHVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprFabricBHVlanEpDn_Type = SnmpAdminString
_CfprFabricBHVlanEpDn_Object = MibTableColumn
cfprFabricBHVlanEpDn = _CfprFabricBHVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 6),
    _CfprFabricBHVlanEpDn_Type()
)
cfprFabricBHVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanEpDn.setStatus("current")
_CfprFabricBHVlanId_Type = Gauge32
_CfprFabricBHVlanId_Object = MibTableColumn
cfprFabricBHVlanId = _CfprFabricBHVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 7),
    _CfprFabricBHVlanId_Type()
)
cfprFabricBHVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanId.setStatus("current")
_CfprFabricBHVlanIfRole_Type = CfprFabricVnetEpIfRole
_CfprFabricBHVlanIfRole_Object = MibTableColumn
cfprFabricBHVlanIfRole = _CfprFabricBHVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 8),
    _CfprFabricBHVlanIfRole_Type()
)
cfprFabricBHVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanIfRole.setStatus("current")
_CfprFabricBHVlanIfType_Type = CfprNetworkVnetEpIfType
_CfprFabricBHVlanIfType_Object = MibTableColumn
cfprFabricBHVlanIfType = _CfprFabricBHVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 9),
    _CfprFabricBHVlanIfType_Type()
)
cfprFabricBHVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanIfType.setStatus("current")
_CfprFabricBHVlanLocale_Type = CfprFabricVnetEpLocale
_CfprFabricBHVlanLocale_Object = MibTableColumn
cfprFabricBHVlanLocale = _CfprFabricBHVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 10),
    _CfprFabricBHVlanLocale_Type()
)
cfprFabricBHVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanLocale.setStatus("current")
_CfprFabricBHVlanName_Type = SnmpAdminString
_CfprFabricBHVlanName_Object = MibTableColumn
cfprFabricBHVlanName = _CfprFabricBHVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 11),
    _CfprFabricBHVlanName_Type()
)
cfprFabricBHVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanName.setStatus("current")
_CfprFabricBHVlanOperState_Type = CfprFabricVlanOperState
_CfprFabricBHVlanOperState_Object = MibTableColumn
cfprFabricBHVlanOperState = _CfprFabricBHVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 12),
    _CfprFabricBHVlanOperState_Type()
)
cfprFabricBHVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanOperState.setStatus("current")
_CfprFabricBHVlanOverlapStateForA_Type = CfprFabricVlanOverlapState
_CfprFabricBHVlanOverlapStateForA_Object = MibTableColumn
cfprFabricBHVlanOverlapStateForA = _CfprFabricBHVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 13),
    _CfprFabricBHVlanOverlapStateForA_Type()
)
cfprFabricBHVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanOverlapStateForA.setStatus("current")
_CfprFabricBHVlanOverlapStateForB_Type = CfprFabricVlanOverlapState
_CfprFabricBHVlanOverlapStateForB_Object = MibTableColumn
cfprFabricBHVlanOverlapStateForB = _CfprFabricBHVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 14),
    _CfprFabricBHVlanOverlapStateForB_Type()
)
cfprFabricBHVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanOverlapStateForB.setStatus("current")
_CfprFabricBHVlanPeerDn_Type = SnmpAdminString
_CfprFabricBHVlanPeerDn_Object = MibTableColumn
cfprFabricBHVlanPeerDn = _CfprFabricBHVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 15),
    _CfprFabricBHVlanPeerDn_Type()
)
cfprFabricBHVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanPeerDn.setStatus("current")
_CfprFabricBHVlanPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprFabricBHVlanPolicyOwner_Object = MibTableColumn
cfprFabricBHVlanPolicyOwner = _CfprFabricBHVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 16),
    _CfprFabricBHVlanPolicyOwner_Type()
)
cfprFabricBHVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanPolicyOwner.setStatus("current")
_CfprFabricBHVlanPubNwDn_Type = SnmpAdminString
_CfprFabricBHVlanPubNwDn_Object = MibTableColumn
cfprFabricBHVlanPubNwDn = _CfprFabricBHVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 17),
    _CfprFabricBHVlanPubNwDn_Type()
)
cfprFabricBHVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanPubNwDn.setStatus("current")
_CfprFabricBHVlanPubNwId_Type = Gauge32
_CfprFabricBHVlanPubNwId_Object = MibTableColumn
cfprFabricBHVlanPubNwId = _CfprFabricBHVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 18),
    _CfprFabricBHVlanPubNwId_Type()
)
cfprFabricBHVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanPubNwId.setStatus("current")
_CfprFabricBHVlanPubNwName_Type = SnmpAdminString
_CfprFabricBHVlanPubNwName_Object = MibTableColumn
cfprFabricBHVlanPubNwName = _CfprFabricBHVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 19),
    _CfprFabricBHVlanPubNwName_Type()
)
cfprFabricBHVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanPubNwName.setStatus("current")
_CfprFabricBHVlanSharing_Type = CfprFabricAVlanSharing
_CfprFabricBHVlanSharing_Object = MibTableColumn
cfprFabricBHVlanSharing = _CfprFabricBHVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 20),
    _CfprFabricBHVlanSharing_Type()
)
cfprFabricBHVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanSharing.setStatus("current")
_CfprFabricBHVlanSwitchId_Type = CfprFabricBHVlanSwitchId
_CfprFabricBHVlanSwitchId_Object = MibTableColumn
cfprFabricBHVlanSwitchId = _CfprFabricBHVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 21),
    _CfprFabricBHVlanSwitchId_Type()
)
cfprFabricBHVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanSwitchId.setStatus("current")
_CfprFabricBHVlanTransport_Type = CfprFabricAVlanTransport
_CfprFabricBHVlanTransport_Object = MibTableColumn
cfprFabricBHVlanTransport = _CfprFabricBHVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 22),
    _CfprFabricBHVlanTransport_Type()
)
cfprFabricBHVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanTransport.setStatus("current")
_CfprFabricBHVlanType_Type = CfprFabricAVlanType
_CfprFabricBHVlanType_Object = MibTableColumn
cfprFabricBHVlanType = _CfprFabricBHVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 1, 1, 23),
    _CfprFabricBHVlanType_Type()
)
cfprFabricBHVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBHVlanType.setStatus("current")
_CfprFabricBreakoutTable_Object = MibTable
cfprFabricBreakoutTable = _CfprFabricBreakoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 2)
)
if mibBuilder.loadTexts:
    cfprFabricBreakoutTable.setStatus("current")
_CfprFabricBreakoutEntry_Object = MibTableRow
cfprFabricBreakoutEntry = _CfprFabricBreakoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 2, 1)
)
cfprFabricBreakoutEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricBreakoutInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricBreakoutEntry.setStatus("current")
_CfprFabricBreakoutInstanceId_Type = CfprManagedObjectId
_CfprFabricBreakoutInstanceId_Object = MibTableColumn
cfprFabricBreakoutInstanceId = _CfprFabricBreakoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 2, 1, 1),
    _CfprFabricBreakoutInstanceId_Type()
)
cfprFabricBreakoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricBreakoutInstanceId.setStatus("current")
_CfprFabricBreakoutDn_Type = CfprManagedObjectDn
_CfprFabricBreakoutDn_Object = MibTableColumn
cfprFabricBreakoutDn = _CfprFabricBreakoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 2, 1, 2),
    _CfprFabricBreakoutDn_Type()
)
cfprFabricBreakoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBreakoutDn.setStatus("current")
_CfprFabricBreakoutRn_Type = SnmpAdminString
_CfprFabricBreakoutRn_Object = MibTableColumn
cfprFabricBreakoutRn = _CfprFabricBreakoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 2, 1, 3),
    _CfprFabricBreakoutRn_Type()
)
cfprFabricBreakoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBreakoutRn.setStatus("current")
_CfprFabricBreakoutBreakoutType_Type = CfprFabricBreakoutType
_CfprFabricBreakoutBreakoutType_Object = MibTableColumn
cfprFabricBreakoutBreakoutType = _CfprFabricBreakoutBreakoutType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 2, 1, 4),
    _CfprFabricBreakoutBreakoutType_Type()
)
cfprFabricBreakoutBreakoutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBreakoutBreakoutType.setStatus("current")
_CfprFabricBreakoutPortId_Type = CfprFabricBreakoutPortId
_CfprFabricBreakoutPortId_Object = MibTableColumn
cfprFabricBreakoutPortId = _CfprFabricBreakoutPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 2, 1, 5),
    _CfprFabricBreakoutPortId_Type()
)
cfprFabricBreakoutPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBreakoutPortId.setStatus("current")
_CfprFabricBreakoutSlotId_Type = CfprFabricBreakoutSlotId
_CfprFabricBreakoutSlotId_Object = MibTableColumn
cfprFabricBreakoutSlotId = _CfprFabricBreakoutSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 2, 1, 6),
    _CfprFabricBreakoutSlotId_Type()
)
cfprFabricBreakoutSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricBreakoutSlotId.setStatus("current")
_CfprFabricCablingTable_Object = MibTable
cfprFabricCablingTable = _CfprFabricCablingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 3)
)
if mibBuilder.loadTexts:
    cfprFabricCablingTable.setStatus("current")
_CfprFabricCablingEntry_Object = MibTableRow
cfprFabricCablingEntry = _CfprFabricCablingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 3, 1)
)
cfprFabricCablingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricCablingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricCablingEntry.setStatus("current")
_CfprFabricCablingInstanceId_Type = CfprManagedObjectId
_CfprFabricCablingInstanceId_Object = MibTableColumn
cfprFabricCablingInstanceId = _CfprFabricCablingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 3, 1, 1),
    _CfprFabricCablingInstanceId_Type()
)
cfprFabricCablingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricCablingInstanceId.setStatus("current")
_CfprFabricCablingDn_Type = CfprManagedObjectDn
_CfprFabricCablingDn_Object = MibTableColumn
cfprFabricCablingDn = _CfprFabricCablingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 3, 1, 2),
    _CfprFabricCablingDn_Type()
)
cfprFabricCablingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingDn.setStatus("current")
_CfprFabricCablingRn_Type = SnmpAdminString
_CfprFabricCablingRn_Object = MibTableColumn
cfprFabricCablingRn = _CfprFabricCablingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 3, 1, 3),
    _CfprFabricCablingRn_Type()
)
cfprFabricCablingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingRn.setStatus("current")
_CfprFabricCablingSwTable_Object = MibTable
cfprFabricCablingSwTable = _CfprFabricCablingSwTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4)
)
if mibBuilder.loadTexts:
    cfprFabricCablingSwTable.setStatus("current")
_CfprFabricCablingSwEntry_Object = MibTableRow
cfprFabricCablingSwEntry = _CfprFabricCablingSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1)
)
cfprFabricCablingSwEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricCablingSwInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricCablingSwEntry.setStatus("current")
_CfprFabricCablingSwInstanceId_Type = CfprManagedObjectId
_CfprFabricCablingSwInstanceId_Object = MibTableColumn
cfprFabricCablingSwInstanceId = _CfprFabricCablingSwInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1, 1),
    _CfprFabricCablingSwInstanceId_Type()
)
cfprFabricCablingSwInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricCablingSwInstanceId.setStatus("current")
_CfprFabricCablingSwDn_Type = CfprManagedObjectDn
_CfprFabricCablingSwDn_Object = MibTableColumn
cfprFabricCablingSwDn = _CfprFabricCablingSwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1, 2),
    _CfprFabricCablingSwDn_Type()
)
cfprFabricCablingSwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingSwDn.setStatus("current")
_CfprFabricCablingSwRn_Type = SnmpAdminString
_CfprFabricCablingSwRn_Object = MibTableColumn
cfprFabricCablingSwRn = _CfprFabricCablingSwRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1, 3),
    _CfprFabricCablingSwRn_Type()
)
cfprFabricCablingSwRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingSwRn.setStatus("current")
_CfprFabricCablingSwId_Type = CfprNetworkSwitchId
_CfprFabricCablingSwId_Object = MibTableColumn
cfprFabricCablingSwId = _CfprFabricCablingSwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1, 4),
    _CfprFabricCablingSwId_Type()
)
cfprFabricCablingSwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingSwId.setStatus("current")
_CfprFabricCablingSwLocale_Type = CfprFabricExternalLocale
_CfprFabricCablingSwLocale_Object = MibTableColumn
cfprFabricCablingSwLocale = _CfprFabricCablingSwLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1, 5),
    _CfprFabricCablingSwLocale_Type()
)
cfprFabricCablingSwLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingSwLocale.setStatus("current")
_CfprFabricCablingSwName_Type = SnmpAdminString
_CfprFabricCablingSwName_Object = MibTableColumn
cfprFabricCablingSwName = _CfprFabricCablingSwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1, 6),
    _CfprFabricCablingSwName_Type()
)
cfprFabricCablingSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingSwName.setStatus("current")
_CfprFabricCablingSwTransport_Type = CfprNetworkTransport
_CfprFabricCablingSwTransport_Object = MibTableColumn
cfprFabricCablingSwTransport = _CfprFabricCablingSwTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1, 7),
    _CfprFabricCablingSwTransport_Type()
)
cfprFabricCablingSwTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingSwTransport.setStatus("current")
_CfprFabricCablingSwType_Type = CfprNetworkConnectionType
_CfprFabricCablingSwType_Object = MibTableColumn
cfprFabricCablingSwType = _CfprFabricCablingSwType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 4, 1, 8),
    _CfprFabricCablingSwType_Type()
)
cfprFabricCablingSwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCablingSwType.setStatus("current")
_CfprFabricCdpLinkPolicyTable_Object = MibTable
cfprFabricCdpLinkPolicyTable = _CfprFabricCdpLinkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5)
)
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyTable.setStatus("current")
_CfprFabricCdpLinkPolicyEntry_Object = MibTableRow
cfprFabricCdpLinkPolicyEntry = _CfprFabricCdpLinkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1)
)
cfprFabricCdpLinkPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricCdpLinkPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyEntry.setStatus("current")
_CfprFabricCdpLinkPolicyInstanceId_Type = CfprManagedObjectId
_CfprFabricCdpLinkPolicyInstanceId_Object = MibTableColumn
cfprFabricCdpLinkPolicyInstanceId = _CfprFabricCdpLinkPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 1),
    _CfprFabricCdpLinkPolicyInstanceId_Type()
)
cfprFabricCdpLinkPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyInstanceId.setStatus("current")
_CfprFabricCdpLinkPolicyDn_Type = CfprManagedObjectDn
_CfprFabricCdpLinkPolicyDn_Object = MibTableColumn
cfprFabricCdpLinkPolicyDn = _CfprFabricCdpLinkPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 2),
    _CfprFabricCdpLinkPolicyDn_Type()
)
cfprFabricCdpLinkPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyDn.setStatus("current")
_CfprFabricCdpLinkPolicyRn_Type = SnmpAdminString
_CfprFabricCdpLinkPolicyRn_Object = MibTableColumn
cfprFabricCdpLinkPolicyRn = _CfprFabricCdpLinkPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 3),
    _CfprFabricCdpLinkPolicyRn_Type()
)
cfprFabricCdpLinkPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyRn.setStatus("current")
_CfprFabricCdpLinkPolicyAdminState_Type = CfprFabricCdpLinkPolicyAdminState
_CfprFabricCdpLinkPolicyAdminState_Object = MibTableColumn
cfprFabricCdpLinkPolicyAdminState = _CfprFabricCdpLinkPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 4),
    _CfprFabricCdpLinkPolicyAdminState_Type()
)
cfprFabricCdpLinkPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyAdminState.setStatus("current")
_CfprFabricCdpLinkPolicyDescr_Type = SnmpAdminString
_CfprFabricCdpLinkPolicyDescr_Object = MibTableColumn
cfprFabricCdpLinkPolicyDescr = _CfprFabricCdpLinkPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 5),
    _CfprFabricCdpLinkPolicyDescr_Type()
)
cfprFabricCdpLinkPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyDescr.setStatus("current")
_CfprFabricCdpLinkPolicyIntId_Type = SnmpAdminString
_CfprFabricCdpLinkPolicyIntId_Object = MibTableColumn
cfprFabricCdpLinkPolicyIntId = _CfprFabricCdpLinkPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 6),
    _CfprFabricCdpLinkPolicyIntId_Type()
)
cfprFabricCdpLinkPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyIntId.setStatus("current")
_CfprFabricCdpLinkPolicyName_Type = SnmpAdminString
_CfprFabricCdpLinkPolicyName_Object = MibTableColumn
cfprFabricCdpLinkPolicyName = _CfprFabricCdpLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 7),
    _CfprFabricCdpLinkPolicyName_Type()
)
cfprFabricCdpLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyName.setStatus("current")
_CfprFabricCdpLinkPolicyPolicyLevel_Type = Gauge32
_CfprFabricCdpLinkPolicyPolicyLevel_Object = MibTableColumn
cfprFabricCdpLinkPolicyPolicyLevel = _CfprFabricCdpLinkPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 8),
    _CfprFabricCdpLinkPolicyPolicyLevel_Type()
)
cfprFabricCdpLinkPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyPolicyLevel.setStatus("current")
_CfprFabricCdpLinkPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricCdpLinkPolicyPolicyOwner_Object = MibTableColumn
cfprFabricCdpLinkPolicyPolicyOwner = _CfprFabricCdpLinkPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 9),
    _CfprFabricCdpLinkPolicyPolicyOwner_Type()
)
cfprFabricCdpLinkPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyPolicyOwner.setStatus("current")
_CfprFabricCdpLinkPolicyProtocol_Type = CfprFabricEthCdpPolicyProtocol
_CfprFabricCdpLinkPolicyProtocol_Object = MibTableColumn
cfprFabricCdpLinkPolicyProtocol = _CfprFabricCdpLinkPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 10),
    _CfprFabricCdpLinkPolicyProtocol_Type()
)
cfprFabricCdpLinkPolicyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyProtocol.setStatus("current")
_CfprFabricCdpLinkPolicyType_Type = CfprFabricEthLinkPolicyType
_CfprFabricCdpLinkPolicyType_Object = MibTableColumn
cfprFabricCdpLinkPolicyType = _CfprFabricCdpLinkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 5, 1, 11),
    _CfprFabricCdpLinkPolicyType_Type()
)
cfprFabricCdpLinkPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricCdpLinkPolicyType.setStatus("current")
_CfprFabricChangedObjectRefTable_Object = MibTable
cfprFabricChangedObjectRefTable = _CfprFabricChangedObjectRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6)
)
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefTable.setStatus("current")
_CfprFabricChangedObjectRefEntry_Object = MibTableRow
cfprFabricChangedObjectRefEntry = _CfprFabricChangedObjectRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1)
)
cfprFabricChangedObjectRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricChangedObjectRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefEntry.setStatus("current")
_CfprFabricChangedObjectRefInstanceId_Type = CfprManagedObjectId
_CfprFabricChangedObjectRefInstanceId_Object = MibTableColumn
cfprFabricChangedObjectRefInstanceId = _CfprFabricChangedObjectRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1, 1),
    _CfprFabricChangedObjectRefInstanceId_Type()
)
cfprFabricChangedObjectRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefInstanceId.setStatus("current")
_CfprFabricChangedObjectRefDn_Type = CfprManagedObjectDn
_CfprFabricChangedObjectRefDn_Object = MibTableColumn
cfprFabricChangedObjectRefDn = _CfprFabricChangedObjectRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1, 2),
    _CfprFabricChangedObjectRefDn_Type()
)
cfprFabricChangedObjectRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefDn.setStatus("current")
_CfprFabricChangedObjectRefRn_Type = SnmpAdminString
_CfprFabricChangedObjectRefRn_Object = MibTableColumn
cfprFabricChangedObjectRefRn = _CfprFabricChangedObjectRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1, 3),
    _CfprFabricChangedObjectRefRn_Type()
)
cfprFabricChangedObjectRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefRn.setStatus("current")
_CfprFabricChangedObjectRefCentraleVnetEpDn_Type = SnmpAdminString
_CfprFabricChangedObjectRefCentraleVnetEpDn_Object = MibTableColumn
cfprFabricChangedObjectRefCentraleVnetEpDn = _CfprFabricChangedObjectRefCentraleVnetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1, 4),
    _CfprFabricChangedObjectRefCentraleVnetEpDn_Type()
)
cfprFabricChangedObjectRefCentraleVnetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefCentraleVnetEpDn.setStatus("current")
_CfprFabricChangedObjectRefId_Type = Gauge32
_CfprFabricChangedObjectRefId_Object = MibTableColumn
cfprFabricChangedObjectRefId = _CfprFabricChangedObjectRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1, 5),
    _CfprFabricChangedObjectRefId_Type()
)
cfprFabricChangedObjectRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefId.setStatus("current")
_CfprFabricChangedObjectRefOldCentraleVnetEpDn_Type = SnmpAdminString
_CfprFabricChangedObjectRefOldCentraleVnetEpDn_Object = MibTableColumn
cfprFabricChangedObjectRefOldCentraleVnetEpDn = _CfprFabricChangedObjectRefOldCentraleVnetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1, 6),
    _CfprFabricChangedObjectRefOldCentraleVnetEpDn_Type()
)
cfprFabricChangedObjectRefOldCentraleVnetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefOldCentraleVnetEpDn.setStatus("current")
_CfprFabricChangedObjectRefRefObjStatus_Type = CfprFabricStatus
_CfprFabricChangedObjectRefRefObjStatus_Object = MibTableColumn
cfprFabricChangedObjectRefRefObjStatus = _CfprFabricChangedObjectRefRefObjStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1, 7),
    _CfprFabricChangedObjectRefRefObjStatus_Type()
)
cfprFabricChangedObjectRefRefObjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefRefObjStatus.setStatus("current")
_CfprFabricChangedObjectRefFprmVnetEpDn_Type = SnmpAdminString
_CfprFabricChangedObjectRefFprmVnetEpDn_Object = MibTableColumn
cfprFabricChangedObjectRefFprmVnetEpDn = _CfprFabricChangedObjectRefFprmVnetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 6, 1, 8),
    _CfprFabricChangedObjectRefFprmVnetEpDn_Type()
)
cfprFabricChangedObjectRefFprmVnetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChangedObjectRefFprmVnetEpDn.setStatus("current")
_CfprFabricChassisEpTable_Object = MibTable
cfprFabricChassisEpTable = _CfprFabricChassisEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7)
)
if mibBuilder.loadTexts:
    cfprFabricChassisEpTable.setStatus("current")
_CfprFabricChassisEpEntry_Object = MibTableRow
cfprFabricChassisEpEntry = _CfprFabricChassisEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1)
)
cfprFabricChassisEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricChassisEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricChassisEpEntry.setStatus("current")
_CfprFabricChassisEpInstanceId_Type = CfprManagedObjectId
_CfprFabricChassisEpInstanceId_Object = MibTableColumn
cfprFabricChassisEpInstanceId = _CfprFabricChassisEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 1),
    _CfprFabricChassisEpInstanceId_Type()
)
cfprFabricChassisEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricChassisEpInstanceId.setStatus("current")
_CfprFabricChassisEpDn_Type = CfprManagedObjectDn
_CfprFabricChassisEpDn_Object = MibTableColumn
cfprFabricChassisEpDn = _CfprFabricChassisEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 2),
    _CfprFabricChassisEpDn_Type()
)
cfprFabricChassisEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpDn.setStatus("current")
_CfprFabricChassisEpRn_Type = SnmpAdminString
_CfprFabricChassisEpRn_Object = MibTableColumn
cfprFabricChassisEpRn = _CfprFabricChassisEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 3),
    _CfprFabricChassisEpRn_Type()
)
cfprFabricChassisEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpRn.setStatus("current")
_CfprFabricChassisEpAdminState_Type = CfprFabricInternalEpAdminState
_CfprFabricChassisEpAdminState_Object = MibTableColumn
cfprFabricChassisEpAdminState = _CfprFabricChassisEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 4),
    _CfprFabricChassisEpAdminState_Type()
)
cfprFabricChassisEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpAdminState.setStatus("current")
_CfprFabricChassisEpAggrPortId_Type = Gauge32
_CfprFabricChassisEpAggrPortId_Object = MibTableColumn
cfprFabricChassisEpAggrPortId = _CfprFabricChassisEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 5),
    _CfprFabricChassisEpAggrPortId_Type()
)
cfprFabricChassisEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpAggrPortId.setStatus("current")
_CfprFabricChassisEpChassisDn_Type = SnmpAdminString
_CfprFabricChassisEpChassisDn_Object = MibTableColumn
cfprFabricChassisEpChassisDn = _CfprFabricChassisEpChassisDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 6),
    _CfprFabricChassisEpChassisDn_Type()
)
cfprFabricChassisEpChassisDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpChassisDn.setStatus("current")
_CfprFabricChassisEpChassisId_Type = Gauge32
_CfprFabricChassisEpChassisId_Object = MibTableColumn
cfprFabricChassisEpChassisId = _CfprFabricChassisEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 7),
    _CfprFabricChassisEpChassisId_Type()
)
cfprFabricChassisEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpChassisId.setStatus("current")
_CfprFabricChassisEpEpDn_Type = SnmpAdminString
_CfprFabricChassisEpEpDn_Object = MibTableColumn
cfprFabricChassisEpEpDn = _CfprFabricChassisEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 8),
    _CfprFabricChassisEpEpDn_Type()
)
cfprFabricChassisEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpEpDn.setStatus("current")
_CfprFabricChassisEpFltAggr_Type = Unsigned64
_CfprFabricChassisEpFltAggr_Object = MibTableColumn
cfprFabricChassisEpFltAggr = _CfprFabricChassisEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 9),
    _CfprFabricChassisEpFltAggr_Type()
)
cfprFabricChassisEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpFltAggr.setStatus("current")
_CfprFabricChassisEpIfRole_Type = CfprFabricComputeEpIfRole
_CfprFabricChassisEpIfRole_Object = MibTableColumn
cfprFabricChassisEpIfRole = _CfprFabricChassisEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 10),
    _CfprFabricChassisEpIfRole_Type()
)
cfprFabricChassisEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpIfRole.setStatus("current")
_CfprFabricChassisEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricChassisEpIfType_Object = MibTableColumn
cfprFabricChassisEpIfType = _CfprFabricChassisEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 11),
    _CfprFabricChassisEpIfType_Type()
)
cfprFabricChassisEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpIfType.setStatus("current")
_CfprFabricChassisEpLicGP_Type = Unsigned64
_CfprFabricChassisEpLicGP_Object = MibTableColumn
cfprFabricChassisEpLicGP = _CfprFabricChassisEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 12),
    _CfprFabricChassisEpLicGP_Type()
)
cfprFabricChassisEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpLicGP.setStatus("current")
_CfprFabricChassisEpLicState_Type = CfprLicenseState
_CfprFabricChassisEpLicState_Object = MibTableColumn
cfprFabricChassisEpLicState = _CfprFabricChassisEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 13),
    _CfprFabricChassisEpLicState_Type()
)
cfprFabricChassisEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpLicState.setStatus("current")
_CfprFabricChassisEpLocale_Type = CfprFabricInternalEpLocale
_CfprFabricChassisEpLocale_Object = MibTableColumn
cfprFabricChassisEpLocale = _CfprFabricChassisEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 14),
    _CfprFabricChassisEpLocale_Type()
)
cfprFabricChassisEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpLocale.setStatus("current")
_CfprFabricChassisEpModel_Type = SnmpAdminString
_CfprFabricChassisEpModel_Object = MibTableColumn
cfprFabricChassisEpModel = _CfprFabricChassisEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 15),
    _CfprFabricChassisEpModel_Type()
)
cfprFabricChassisEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpModel.setStatus("current")
_CfprFabricChassisEpName_Type = SnmpAdminString
_CfprFabricChassisEpName_Object = MibTableColumn
cfprFabricChassisEpName = _CfprFabricChassisEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 16),
    _CfprFabricChassisEpName_Type()
)
cfprFabricChassisEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpName.setStatus("current")
_CfprFabricChassisEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricChassisEpOperState_Object = MibTableColumn
cfprFabricChassisEpOperState = _CfprFabricChassisEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 17),
    _CfprFabricChassisEpOperState_Type()
)
cfprFabricChassisEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpOperState.setStatus("current")
_CfprFabricChassisEpOperStateReason_Type = SnmpAdminString
_CfprFabricChassisEpOperStateReason_Object = MibTableColumn
cfprFabricChassisEpOperStateReason = _CfprFabricChassisEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 18),
    _CfprFabricChassisEpOperStateReason_Type()
)
cfprFabricChassisEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpOperStateReason.setStatus("current")
_CfprFabricChassisEpPeerAggrPortId_Type = Gauge32
_CfprFabricChassisEpPeerAggrPortId_Object = MibTableColumn
cfprFabricChassisEpPeerAggrPortId = _CfprFabricChassisEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 19),
    _CfprFabricChassisEpPeerAggrPortId_Type()
)
cfprFabricChassisEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpPeerAggrPortId.setStatus("current")
_CfprFabricChassisEpPeerChassisId_Type = Gauge32
_CfprFabricChassisEpPeerChassisId_Object = MibTableColumn
cfprFabricChassisEpPeerChassisId = _CfprFabricChassisEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 20),
    _CfprFabricChassisEpPeerChassisId_Type()
)
cfprFabricChassisEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpPeerChassisId.setStatus("current")
_CfprFabricChassisEpPeerDn_Type = SnmpAdminString
_CfprFabricChassisEpPeerDn_Object = MibTableColumn
cfprFabricChassisEpPeerDn = _CfprFabricChassisEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 21),
    _CfprFabricChassisEpPeerDn_Type()
)
cfprFabricChassisEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpPeerDn.setStatus("current")
_CfprFabricChassisEpPeerPortId_Type = Gauge32
_CfprFabricChassisEpPeerPortId_Object = MibTableColumn
cfprFabricChassisEpPeerPortId = _CfprFabricChassisEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 22),
    _CfprFabricChassisEpPeerPortId_Type()
)
cfprFabricChassisEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpPeerPortId.setStatus("current")
_CfprFabricChassisEpPeerSlotId_Type = Gauge32
_CfprFabricChassisEpPeerSlotId_Object = MibTableColumn
cfprFabricChassisEpPeerSlotId = _CfprFabricChassisEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 23),
    _CfprFabricChassisEpPeerSlotId_Type()
)
cfprFabricChassisEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpPeerSlotId.setStatus("current")
_CfprFabricChassisEpPortId_Type = CfprFabricPIoEpPortId
_CfprFabricChassisEpPortId_Object = MibTableColumn
cfprFabricChassisEpPortId = _CfprFabricChassisEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 24),
    _CfprFabricChassisEpPortId_Type()
)
cfprFabricChassisEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpPortId.setStatus("current")
_CfprFabricChassisEpRevision_Type = SnmpAdminString
_CfprFabricChassisEpRevision_Object = MibTableColumn
cfprFabricChassisEpRevision = _CfprFabricChassisEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 25),
    _CfprFabricChassisEpRevision_Type()
)
cfprFabricChassisEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpRevision.setStatus("current")
_CfprFabricChassisEpSerial_Type = SnmpAdminString
_CfprFabricChassisEpSerial_Object = MibTableColumn
cfprFabricChassisEpSerial = _CfprFabricChassisEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 26),
    _CfprFabricChassisEpSerial_Type()
)
cfprFabricChassisEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpSerial.setStatus("current")
_CfprFabricChassisEpSlotId_Type = CfprFabricPIoEpSlotId
_CfprFabricChassisEpSlotId_Object = MibTableColumn
cfprFabricChassisEpSlotId = _CfprFabricChassisEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 27),
    _CfprFabricChassisEpSlotId_Type()
)
cfprFabricChassisEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpSlotId.setStatus("current")
_CfprFabricChassisEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricChassisEpSwitchId_Object = MibTableColumn
cfprFabricChassisEpSwitchId = _CfprFabricChassisEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 28),
    _CfprFabricChassisEpSwitchId_Type()
)
cfprFabricChassisEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpSwitchId.setStatus("current")
_CfprFabricChassisEpTransport_Type = CfprNetworkTransport
_CfprFabricChassisEpTransport_Object = MibTableColumn
cfprFabricChassisEpTransport = _CfprFabricChassisEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 29),
    _CfprFabricChassisEpTransport_Type()
)
cfprFabricChassisEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpTransport.setStatus("current")
_CfprFabricChassisEpType_Type = CfprFabricComputeEpType
_CfprFabricChassisEpType_Object = MibTableColumn
cfprFabricChassisEpType = _CfprFabricChassisEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 30),
    _CfprFabricChassisEpType_Type()
)
cfprFabricChassisEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpType.setStatus("current")
_CfprFabricChassisEpVendor_Type = SnmpAdminString
_CfprFabricChassisEpVendor_Object = MibTableColumn
cfprFabricChassisEpVendor = _CfprFabricChassisEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 7, 1, 31),
    _CfprFabricChassisEpVendor_Type()
)
cfprFabricChassisEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricChassisEpVendor.setStatus("current")
_CfprFabricComputePhEpTable_Object = MibTable
cfprFabricComputePhEpTable = _CfprFabricComputePhEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8)
)
if mibBuilder.loadTexts:
    cfprFabricComputePhEpTable.setStatus("current")
_CfprFabricComputePhEpEntry_Object = MibTableRow
cfprFabricComputePhEpEntry = _CfprFabricComputePhEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1)
)
cfprFabricComputePhEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricComputePhEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricComputePhEpEntry.setStatus("current")
_CfprFabricComputePhEpInstanceId_Type = CfprManagedObjectId
_CfprFabricComputePhEpInstanceId_Object = MibTableColumn
cfprFabricComputePhEpInstanceId = _CfprFabricComputePhEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 1),
    _CfprFabricComputePhEpInstanceId_Type()
)
cfprFabricComputePhEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpInstanceId.setStatus("current")
_CfprFabricComputePhEpDn_Type = CfprManagedObjectDn
_CfprFabricComputePhEpDn_Object = MibTableColumn
cfprFabricComputePhEpDn = _CfprFabricComputePhEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 2),
    _CfprFabricComputePhEpDn_Type()
)
cfprFabricComputePhEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpDn.setStatus("current")
_CfprFabricComputePhEpRn_Type = SnmpAdminString
_CfprFabricComputePhEpRn_Object = MibTableColumn
cfprFabricComputePhEpRn = _CfprFabricComputePhEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 3),
    _CfprFabricComputePhEpRn_Type()
)
cfprFabricComputePhEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpRn.setStatus("current")
_CfprFabricComputePhEpAdminState_Type = CfprFabricComputePhEpAdminState
_CfprFabricComputePhEpAdminState_Object = MibTableColumn
cfprFabricComputePhEpAdminState = _CfprFabricComputePhEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 4),
    _CfprFabricComputePhEpAdminState_Type()
)
cfprFabricComputePhEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpAdminState.setStatus("current")
_CfprFabricComputePhEpAggrPortId_Type = Gauge32
_CfprFabricComputePhEpAggrPortId_Object = MibTableColumn
cfprFabricComputePhEpAggrPortId = _CfprFabricComputePhEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 5),
    _CfprFabricComputePhEpAggrPortId_Type()
)
cfprFabricComputePhEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpAggrPortId.setStatus("current")
_CfprFabricComputePhEpBoardAggregationRole_Type = CfprEquipmentBoardAggregationRole
_CfprFabricComputePhEpBoardAggregationRole_Object = MibTableColumn
cfprFabricComputePhEpBoardAggregationRole = _CfprFabricComputePhEpBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 6),
    _CfprFabricComputePhEpBoardAggregationRole_Type()
)
cfprFabricComputePhEpBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpBoardAggregationRole.setStatus("current")
_CfprFabricComputePhEpChassisId_Type = Gauge32
_CfprFabricComputePhEpChassisId_Object = MibTableColumn
cfprFabricComputePhEpChassisId = _CfprFabricComputePhEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 7),
    _CfprFabricComputePhEpChassisId_Type()
)
cfprFabricComputePhEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpChassisId.setStatus("current")
_CfprFabricComputePhEpCheckpointTrigTs_Type = Unsigned64
_CfprFabricComputePhEpCheckpointTrigTs_Object = MibTableColumn
cfprFabricComputePhEpCheckpointTrigTs = _CfprFabricComputePhEpCheckpointTrigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 8),
    _CfprFabricComputePhEpCheckpointTrigTs_Type()
)
cfprFabricComputePhEpCheckpointTrigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpCheckpointTrigTs.setStatus("current")
_CfprFabricComputePhEpDeepCheckpointTrigTs_Type = Unsigned64
_CfprFabricComputePhEpDeepCheckpointTrigTs_Object = MibTableColumn
cfprFabricComputePhEpDeepCheckpointTrigTs = _CfprFabricComputePhEpDeepCheckpointTrigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 9),
    _CfprFabricComputePhEpDeepCheckpointTrigTs_Type()
)
cfprFabricComputePhEpDeepCheckpointTrigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpDeepCheckpointTrigTs.setStatus("current")
_CfprFabricComputePhEpDiscTrigTs_Type = Unsigned64
_CfprFabricComputePhEpDiscTrigTs_Object = MibTableColumn
cfprFabricComputePhEpDiscTrigTs = _CfprFabricComputePhEpDiscTrigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 10),
    _CfprFabricComputePhEpDiscTrigTs_Type()
)
cfprFabricComputePhEpDiscTrigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpDiscTrigTs.setStatus("current")
_CfprFabricComputePhEpEpDn_Type = SnmpAdminString
_CfprFabricComputePhEpEpDn_Object = MibTableColumn
cfprFabricComputePhEpEpDn = _CfprFabricComputePhEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 11),
    _CfprFabricComputePhEpEpDn_Type()
)
cfprFabricComputePhEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpEpDn.setStatus("current")
_CfprFabricComputePhEpEqType_Type = CfprEquipmentFabricEpType
_CfprFabricComputePhEpEqType_Object = MibTableColumn
cfprFabricComputePhEpEqType = _CfprFabricComputePhEpEqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 12),
    _CfprFabricComputePhEpEqType_Type()
)
cfprFabricComputePhEpEqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpEqType.setStatus("current")
_CfprFabricComputePhEpFltAggr_Type = Unsigned64
_CfprFabricComputePhEpFltAggr_Object = MibTableColumn
cfprFabricComputePhEpFltAggr = _CfprFabricComputePhEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 13),
    _CfprFabricComputePhEpFltAggr_Type()
)
cfprFabricComputePhEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpFltAggr.setStatus("current")
_CfprFabricComputePhEpIfRole_Type = CfprFabricComputeEpIfRole
_CfprFabricComputePhEpIfRole_Object = MibTableColumn
cfprFabricComputePhEpIfRole = _CfprFabricComputePhEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 14),
    _CfprFabricComputePhEpIfRole_Type()
)
cfprFabricComputePhEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpIfRole.setStatus("current")
_CfprFabricComputePhEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricComputePhEpIfType_Object = MibTableColumn
cfprFabricComputePhEpIfType = _CfprFabricComputePhEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 15),
    _CfprFabricComputePhEpIfType_Type()
)
cfprFabricComputePhEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpIfType.setStatus("current")
_CfprFabricComputePhEpLc_Type = CfprFabricBladeLifeCycle
_CfprFabricComputePhEpLc_Object = MibTableColumn
cfprFabricComputePhEpLc = _CfprFabricComputePhEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 16),
    _CfprFabricComputePhEpLc_Type()
)
cfprFabricComputePhEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpLc.setStatus("current")
_CfprFabricComputePhEpLicGP_Type = Unsigned64
_CfprFabricComputePhEpLicGP_Object = MibTableColumn
cfprFabricComputePhEpLicGP = _CfprFabricComputePhEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 17),
    _CfprFabricComputePhEpLicGP_Type()
)
cfprFabricComputePhEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpLicGP.setStatus("current")
_CfprFabricComputePhEpLicState_Type = CfprLicenseState
_CfprFabricComputePhEpLicState_Object = MibTableColumn
cfprFabricComputePhEpLicState = _CfprFabricComputePhEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 18),
    _CfprFabricComputePhEpLicState_Type()
)
cfprFabricComputePhEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpLicState.setStatus("current")
_CfprFabricComputePhEpLocale_Type = CfprFabricInternalEpLocale
_CfprFabricComputePhEpLocale_Object = MibTableColumn
cfprFabricComputePhEpLocale = _CfprFabricComputePhEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 19),
    _CfprFabricComputePhEpLocale_Type()
)
cfprFabricComputePhEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpLocale.setStatus("current")
_CfprFabricComputePhEpModel_Type = SnmpAdminString
_CfprFabricComputePhEpModel_Object = MibTableColumn
cfprFabricComputePhEpModel = _CfprFabricComputePhEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 20),
    _CfprFabricComputePhEpModel_Type()
)
cfprFabricComputePhEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpModel.setStatus("current")
_CfprFabricComputePhEpName_Type = SnmpAdminString
_CfprFabricComputePhEpName_Object = MibTableColumn
cfprFabricComputePhEpName = _CfprFabricComputePhEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 21),
    _CfprFabricComputePhEpName_Type()
)
cfprFabricComputePhEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpName.setStatus("current")
_CfprFabricComputePhEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricComputePhEpOperState_Object = MibTableColumn
cfprFabricComputePhEpOperState = _CfprFabricComputePhEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 22),
    _CfprFabricComputePhEpOperState_Type()
)
cfprFabricComputePhEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpOperState.setStatus("current")
_CfprFabricComputePhEpOperStateReason_Type = SnmpAdminString
_CfprFabricComputePhEpOperStateReason_Object = MibTableColumn
cfprFabricComputePhEpOperStateReason = _CfprFabricComputePhEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 23),
    _CfprFabricComputePhEpOperStateReason_Type()
)
cfprFabricComputePhEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpOperStateReason.setStatus("current")
_CfprFabricComputePhEpPeerAggrPortId_Type = Gauge32
_CfprFabricComputePhEpPeerAggrPortId_Object = MibTableColumn
cfprFabricComputePhEpPeerAggrPortId = _CfprFabricComputePhEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 24),
    _CfprFabricComputePhEpPeerAggrPortId_Type()
)
cfprFabricComputePhEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpPeerAggrPortId.setStatus("current")
_CfprFabricComputePhEpPeerChassisId_Type = Gauge32
_CfprFabricComputePhEpPeerChassisId_Object = MibTableColumn
cfprFabricComputePhEpPeerChassisId = _CfprFabricComputePhEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 25),
    _CfprFabricComputePhEpPeerChassisId_Type()
)
cfprFabricComputePhEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpPeerChassisId.setStatus("current")
_CfprFabricComputePhEpPeerDn_Type = SnmpAdminString
_CfprFabricComputePhEpPeerDn_Object = MibTableColumn
cfprFabricComputePhEpPeerDn = _CfprFabricComputePhEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 26),
    _CfprFabricComputePhEpPeerDn_Type()
)
cfprFabricComputePhEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpPeerDn.setStatus("current")
_CfprFabricComputePhEpPeerPortId_Type = Gauge32
_CfprFabricComputePhEpPeerPortId_Object = MibTableColumn
cfprFabricComputePhEpPeerPortId = _CfprFabricComputePhEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 27),
    _CfprFabricComputePhEpPeerPortId_Type()
)
cfprFabricComputePhEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpPeerPortId.setStatus("current")
_CfprFabricComputePhEpPeerSlotId_Type = Gauge32
_CfprFabricComputePhEpPeerSlotId_Object = MibTableColumn
cfprFabricComputePhEpPeerSlotId = _CfprFabricComputePhEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 28),
    _CfprFabricComputePhEpPeerSlotId_Type()
)
cfprFabricComputePhEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpPeerSlotId.setStatus("current")
_CfprFabricComputePhEpPortId_Type = CfprFabricPIoEpPortId
_CfprFabricComputePhEpPortId_Object = MibTableColumn
cfprFabricComputePhEpPortId = _CfprFabricComputePhEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 29),
    _CfprFabricComputePhEpPortId_Type()
)
cfprFabricComputePhEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpPortId.setStatus("current")
_CfprFabricComputePhEpProfileDn_Type = SnmpAdminString
_CfprFabricComputePhEpProfileDn_Object = MibTableColumn
cfprFabricComputePhEpProfileDn = _CfprFabricComputePhEpProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 30),
    _CfprFabricComputePhEpProfileDn_Type()
)
cfprFabricComputePhEpProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpProfileDn.setStatus("current")
_CfprFabricComputePhEpRevision_Type = SnmpAdminString
_CfprFabricComputePhEpRevision_Object = MibTableColumn
cfprFabricComputePhEpRevision = _CfprFabricComputePhEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 31),
    _CfprFabricComputePhEpRevision_Type()
)
cfprFabricComputePhEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpRevision.setStatus("current")
_CfprFabricComputePhEpSerial_Type = SnmpAdminString
_CfprFabricComputePhEpSerial_Object = MibTableColumn
cfprFabricComputePhEpSerial = _CfprFabricComputePhEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 32),
    _CfprFabricComputePhEpSerial_Type()
)
cfprFabricComputePhEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpSerial.setStatus("current")
_CfprFabricComputePhEpSlotId_Type = CfprFabricPIoEpSlotId
_CfprFabricComputePhEpSlotId_Object = MibTableColumn
cfprFabricComputePhEpSlotId = _CfprFabricComputePhEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 33),
    _CfprFabricComputePhEpSlotId_Type()
)
cfprFabricComputePhEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpSlotId.setStatus("current")
_CfprFabricComputePhEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricComputePhEpSwitchId_Object = MibTableColumn
cfprFabricComputePhEpSwitchId = _CfprFabricComputePhEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 34),
    _CfprFabricComputePhEpSwitchId_Type()
)
cfprFabricComputePhEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpSwitchId.setStatus("current")
_CfprFabricComputePhEpTransport_Type = CfprNetworkTransport
_CfprFabricComputePhEpTransport_Object = MibTableColumn
cfprFabricComputePhEpTransport = _CfprFabricComputePhEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 35),
    _CfprFabricComputePhEpTransport_Type()
)
cfprFabricComputePhEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpTransport.setStatus("current")
_CfprFabricComputePhEpType_Type = CfprFabricComputeEpType
_CfprFabricComputePhEpType_Object = MibTableColumn
cfprFabricComputePhEpType = _CfprFabricComputePhEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 36),
    _CfprFabricComputePhEpType_Type()
)
cfprFabricComputePhEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpType.setStatus("current")
_CfprFabricComputePhEpVendor_Type = SnmpAdminString
_CfprFabricComputePhEpVendor_Object = MibTableColumn
cfprFabricComputePhEpVendor = _CfprFabricComputePhEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 8, 1, 37),
    _CfprFabricComputePhEpVendor_Type()
)
cfprFabricComputePhEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputePhEpVendor.setStatus("current")
_CfprFabricComputeSlotEpTable_Object = MibTable
cfprFabricComputeSlotEpTable = _CfprFabricComputeSlotEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9)
)
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpTable.setStatus("current")
_CfprFabricComputeSlotEpEntry_Object = MibTableRow
cfprFabricComputeSlotEpEntry = _CfprFabricComputeSlotEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1)
)
cfprFabricComputeSlotEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricComputeSlotEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpEntry.setStatus("current")
_CfprFabricComputeSlotEpInstanceId_Type = CfprManagedObjectId
_CfprFabricComputeSlotEpInstanceId_Object = MibTableColumn
cfprFabricComputeSlotEpInstanceId = _CfprFabricComputeSlotEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 1),
    _CfprFabricComputeSlotEpInstanceId_Type()
)
cfprFabricComputeSlotEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpInstanceId.setStatus("current")
_CfprFabricComputeSlotEpDn_Type = CfprManagedObjectDn
_CfprFabricComputeSlotEpDn_Object = MibTableColumn
cfprFabricComputeSlotEpDn = _CfprFabricComputeSlotEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 2),
    _CfprFabricComputeSlotEpDn_Type()
)
cfprFabricComputeSlotEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpDn.setStatus("current")
_CfprFabricComputeSlotEpRn_Type = SnmpAdminString
_CfprFabricComputeSlotEpRn_Object = MibTableColumn
cfprFabricComputeSlotEpRn = _CfprFabricComputeSlotEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 3),
    _CfprFabricComputeSlotEpRn_Type()
)
cfprFabricComputeSlotEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpRn.setStatus("current")
_CfprFabricComputeSlotEpAdminState_Type = CfprFabricSlotAdminState
_CfprFabricComputeSlotEpAdminState_Object = MibTableColumn
cfprFabricComputeSlotEpAdminState = _CfprFabricComputeSlotEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 4),
    _CfprFabricComputeSlotEpAdminState_Type()
)
cfprFabricComputeSlotEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpAdminState.setStatus("current")
_CfprFabricComputeSlotEpAggrPortId_Type = Gauge32
_CfprFabricComputeSlotEpAggrPortId_Object = MibTableColumn
cfprFabricComputeSlotEpAggrPortId = _CfprFabricComputeSlotEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 5),
    _CfprFabricComputeSlotEpAggrPortId_Type()
)
cfprFabricComputeSlotEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpAggrPortId.setStatus("current")
_CfprFabricComputeSlotEpBoardAggregationRole_Type = CfprEquipmentBoardAggregationRole
_CfprFabricComputeSlotEpBoardAggregationRole_Object = MibTableColumn
cfprFabricComputeSlotEpBoardAggregationRole = _CfprFabricComputeSlotEpBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 6),
    _CfprFabricComputeSlotEpBoardAggregationRole_Type()
)
cfprFabricComputeSlotEpBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpBoardAggregationRole.setStatus("current")
_CfprFabricComputeSlotEpChassisId_Type = Gauge32
_CfprFabricComputeSlotEpChassisId_Object = MibTableColumn
cfprFabricComputeSlotEpChassisId = _CfprFabricComputeSlotEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 7),
    _CfprFabricComputeSlotEpChassisId_Type()
)
cfprFabricComputeSlotEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpChassisId.setStatus("current")
_CfprFabricComputeSlotEpConnPath_Type = CfprEquipmentConnectionStatus
_CfprFabricComputeSlotEpConnPath_Object = MibTableColumn
cfprFabricComputeSlotEpConnPath = _CfprFabricComputeSlotEpConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 8),
    _CfprFabricComputeSlotEpConnPath_Type()
)
cfprFabricComputeSlotEpConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpConnPath.setStatus("current")
_CfprFabricComputeSlotEpConnStatus_Type = CfprEquipmentConnectionStatus
_CfprFabricComputeSlotEpConnStatus_Object = MibTableColumn
cfprFabricComputeSlotEpConnStatus = _CfprFabricComputeSlotEpConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 9),
    _CfprFabricComputeSlotEpConnStatus_Type()
)
cfprFabricComputeSlotEpConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpConnStatus.setStatus("current")
_CfprFabricComputeSlotEpDiscovery_Type = CfprComputeDiscovery
_CfprFabricComputeSlotEpDiscovery_Object = MibTableColumn
cfprFabricComputeSlotEpDiscovery = _CfprFabricComputeSlotEpDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 10),
    _CfprFabricComputeSlotEpDiscovery_Type()
)
cfprFabricComputeSlotEpDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpDiscovery.setStatus("current")
_CfprFabricComputeSlotEpEpDn_Type = SnmpAdminString
_CfprFabricComputeSlotEpEpDn_Object = MibTableColumn
cfprFabricComputeSlotEpEpDn = _CfprFabricComputeSlotEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 11),
    _CfprFabricComputeSlotEpEpDn_Type()
)
cfprFabricComputeSlotEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpEpDn.setStatus("current")
_CfprFabricComputeSlotEpFactoryResetFlag_Type = TruthValue
_CfprFabricComputeSlotEpFactoryResetFlag_Object = MibTableColumn
cfprFabricComputeSlotEpFactoryResetFlag = _CfprFabricComputeSlotEpFactoryResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 12),
    _CfprFabricComputeSlotEpFactoryResetFlag_Type()
)
cfprFabricComputeSlotEpFactoryResetFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFactoryResetFlag.setStatus("current")
_CfprFabricComputeSlotEpFltAggr_Type = Unsigned64
_CfprFabricComputeSlotEpFltAggr_Object = MibTableColumn
cfprFabricComputeSlotEpFltAggr = _CfprFabricComputeSlotEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 13),
    _CfprFabricComputeSlotEpFltAggr_Type()
)
cfprFabricComputeSlotEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFltAggr.setStatus("current")
_CfprFabricComputeSlotEpFruIdentTrigTs_Type = Unsigned64
_CfprFabricComputeSlotEpFruIdentTrigTs_Object = MibTableColumn
cfprFabricComputeSlotEpFruIdentTrigTs = _CfprFabricComputeSlotEpFruIdentTrigTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 14),
    _CfprFabricComputeSlotEpFruIdentTrigTs_Type()
)
cfprFabricComputeSlotEpFruIdentTrigTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFruIdentTrigTs.setStatus("current")
_CfprFabricComputeSlotEpFsmDescr_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmDescr_Object = MibTableColumn
cfprFabricComputeSlotEpFsmDescr = _CfprFabricComputeSlotEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 15),
    _CfprFabricComputeSlotEpFsmDescr_Type()
)
cfprFabricComputeSlotEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmDescr.setStatus("current")
_CfprFabricComputeSlotEpFsmPrev_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmPrev_Object = MibTableColumn
cfprFabricComputeSlotEpFsmPrev = _CfprFabricComputeSlotEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 16),
    _CfprFabricComputeSlotEpFsmPrev_Type()
)
cfprFabricComputeSlotEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmPrev.setStatus("current")
_CfprFabricComputeSlotEpFsmProgr_Type = Gauge32
_CfprFabricComputeSlotEpFsmProgr_Object = MibTableColumn
cfprFabricComputeSlotEpFsmProgr = _CfprFabricComputeSlotEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 17),
    _CfprFabricComputeSlotEpFsmProgr_Type()
)
cfprFabricComputeSlotEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmProgr.setStatus("current")
_CfprFabricComputeSlotEpFsmRmtInvErrCode_Type = Gauge32
_CfprFabricComputeSlotEpFsmRmtInvErrCode_Object = MibTableColumn
cfprFabricComputeSlotEpFsmRmtInvErrCode = _CfprFabricComputeSlotEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 18),
    _CfprFabricComputeSlotEpFsmRmtInvErrCode_Type()
)
cfprFabricComputeSlotEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmRmtInvErrCode.setStatus("current")
_CfprFabricComputeSlotEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprFabricComputeSlotEpFsmRmtInvErrDescr = _CfprFabricComputeSlotEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 19),
    _CfprFabricComputeSlotEpFsmRmtInvErrDescr_Type()
)
cfprFabricComputeSlotEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmRmtInvErrDescr.setStatus("current")
_CfprFabricComputeSlotEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricComputeSlotEpFsmRmtInvRslt_Object = MibTableColumn
cfprFabricComputeSlotEpFsmRmtInvRslt = _CfprFabricComputeSlotEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 20),
    _CfprFabricComputeSlotEpFsmRmtInvRslt_Type()
)
cfprFabricComputeSlotEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmRmtInvRslt.setStatus("current")
_CfprFabricComputeSlotEpFsmStageDescr_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmStageDescr_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageDescr = _CfprFabricComputeSlotEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 21),
    _CfprFabricComputeSlotEpFsmStageDescr_Type()
)
cfprFabricComputeSlotEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageDescr.setStatus("current")
_CfprFabricComputeSlotEpFsmStamp_Type = DateAndTime
_CfprFabricComputeSlotEpFsmStamp_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStamp = _CfprFabricComputeSlotEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 22),
    _CfprFabricComputeSlotEpFsmStamp_Type()
)
cfprFabricComputeSlotEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStamp.setStatus("current")
_CfprFabricComputeSlotEpFsmStatus_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmStatus_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStatus = _CfprFabricComputeSlotEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 23),
    _CfprFabricComputeSlotEpFsmStatus_Type()
)
cfprFabricComputeSlotEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStatus.setStatus("current")
_CfprFabricComputeSlotEpFsmTry_Type = Gauge32
_CfprFabricComputeSlotEpFsmTry_Object = MibTableColumn
cfprFabricComputeSlotEpFsmTry = _CfprFabricComputeSlotEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 24),
    _CfprFabricComputeSlotEpFsmTry_Type()
)
cfprFabricComputeSlotEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTry.setStatus("current")
_CfprFabricComputeSlotEpIfRole_Type = CfprFabricComputeEpIfRole
_CfprFabricComputeSlotEpIfRole_Object = MibTableColumn
cfprFabricComputeSlotEpIfRole = _CfprFabricComputeSlotEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 25),
    _CfprFabricComputeSlotEpIfRole_Type()
)
cfprFabricComputeSlotEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpIfRole.setStatus("current")
_CfprFabricComputeSlotEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricComputeSlotEpIfType_Object = MibTableColumn
cfprFabricComputeSlotEpIfType = _CfprFabricComputeSlotEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 26),
    _CfprFabricComputeSlotEpIfType_Type()
)
cfprFabricComputeSlotEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpIfType.setStatus("current")
_CfprFabricComputeSlotEpLcTs_Type = DateAndTime
_CfprFabricComputeSlotEpLcTs_Object = MibTableColumn
cfprFabricComputeSlotEpLcTs = _CfprFabricComputeSlotEpLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 27),
    _CfprFabricComputeSlotEpLcTs_Type()
)
cfprFabricComputeSlotEpLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpLcTs.setStatus("current")
_CfprFabricComputeSlotEpLicGP_Type = Unsigned64
_CfprFabricComputeSlotEpLicGP_Object = MibTableColumn
cfprFabricComputeSlotEpLicGP = _CfprFabricComputeSlotEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 28),
    _CfprFabricComputeSlotEpLicGP_Type()
)
cfprFabricComputeSlotEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpLicGP.setStatus("current")
_CfprFabricComputeSlotEpLicState_Type = CfprLicenseState
_CfprFabricComputeSlotEpLicState_Object = MibTableColumn
cfprFabricComputeSlotEpLicState = _CfprFabricComputeSlotEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 29),
    _CfprFabricComputeSlotEpLicState_Type()
)
cfprFabricComputeSlotEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpLicState.setStatus("current")
_CfprFabricComputeSlotEpLocale_Type = CfprFabricInternalEpLocale
_CfprFabricComputeSlotEpLocale_Object = MibTableColumn
cfprFabricComputeSlotEpLocale = _CfprFabricComputeSlotEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 30),
    _CfprFabricComputeSlotEpLocale_Type()
)
cfprFabricComputeSlotEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpLocale.setStatus("current")
_CfprFabricComputeSlotEpManagingInst_Type = CfprNetworkSwitchId
_CfprFabricComputeSlotEpManagingInst_Object = MibTableColumn
cfprFabricComputeSlotEpManagingInst = _CfprFabricComputeSlotEpManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 31),
    _CfprFabricComputeSlotEpManagingInst_Type()
)
cfprFabricComputeSlotEpManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpManagingInst.setStatus("current")
_CfprFabricComputeSlotEpModel_Type = SnmpAdminString
_CfprFabricComputeSlotEpModel_Object = MibTableColumn
cfprFabricComputeSlotEpModel = _CfprFabricComputeSlotEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 32),
    _CfprFabricComputeSlotEpModel_Type()
)
cfprFabricComputeSlotEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpModel.setStatus("current")
_CfprFabricComputeSlotEpName_Type = SnmpAdminString
_CfprFabricComputeSlotEpName_Object = MibTableColumn
cfprFabricComputeSlotEpName = _CfprFabricComputeSlotEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 33),
    _CfprFabricComputeSlotEpName_Type()
)
cfprFabricComputeSlotEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpName.setStatus("current")
_CfprFabricComputeSlotEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricComputeSlotEpOperState_Object = MibTableColumn
cfprFabricComputeSlotEpOperState = _CfprFabricComputeSlotEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 34),
    _CfprFabricComputeSlotEpOperState_Type()
)
cfprFabricComputeSlotEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpOperState.setStatus("current")
_CfprFabricComputeSlotEpOperStateReason_Type = SnmpAdminString
_CfprFabricComputeSlotEpOperStateReason_Object = MibTableColumn
cfprFabricComputeSlotEpOperStateReason = _CfprFabricComputeSlotEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 35),
    _CfprFabricComputeSlotEpOperStateReason_Type()
)
cfprFabricComputeSlotEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpOperStateReason.setStatus("current")
_CfprFabricComputeSlotEpPeerAggrPortId_Type = Gauge32
_CfprFabricComputeSlotEpPeerAggrPortId_Object = MibTableColumn
cfprFabricComputeSlotEpPeerAggrPortId = _CfprFabricComputeSlotEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 36),
    _CfprFabricComputeSlotEpPeerAggrPortId_Type()
)
cfprFabricComputeSlotEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPeerAggrPortId.setStatus("current")
_CfprFabricComputeSlotEpPeerChassisId_Type = Gauge32
_CfprFabricComputeSlotEpPeerChassisId_Object = MibTableColumn
cfprFabricComputeSlotEpPeerChassisId = _CfprFabricComputeSlotEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 37),
    _CfprFabricComputeSlotEpPeerChassisId_Type()
)
cfprFabricComputeSlotEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPeerChassisId.setStatus("current")
_CfprFabricComputeSlotEpPeerDn_Type = SnmpAdminString
_CfprFabricComputeSlotEpPeerDn_Object = MibTableColumn
cfprFabricComputeSlotEpPeerDn = _CfprFabricComputeSlotEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 38),
    _CfprFabricComputeSlotEpPeerDn_Type()
)
cfprFabricComputeSlotEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPeerDn.setStatus("current")
_CfprFabricComputeSlotEpPeerPortId_Type = Gauge32
_CfprFabricComputeSlotEpPeerPortId_Object = MibTableColumn
cfprFabricComputeSlotEpPeerPortId = _CfprFabricComputeSlotEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 39),
    _CfprFabricComputeSlotEpPeerPortId_Type()
)
cfprFabricComputeSlotEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPeerPortId.setStatus("current")
_CfprFabricComputeSlotEpPeerSlotEpDn_Type = SnmpAdminString
_CfprFabricComputeSlotEpPeerSlotEpDn_Object = MibTableColumn
cfprFabricComputeSlotEpPeerSlotEpDn = _CfprFabricComputeSlotEpPeerSlotEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 40),
    _CfprFabricComputeSlotEpPeerSlotEpDn_Type()
)
cfprFabricComputeSlotEpPeerSlotEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPeerSlotEpDn.setStatus("current")
_CfprFabricComputeSlotEpPeerSlotId_Type = Gauge32
_CfprFabricComputeSlotEpPeerSlotId_Object = MibTableColumn
cfprFabricComputeSlotEpPeerSlotId = _CfprFabricComputeSlotEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 41),
    _CfprFabricComputeSlotEpPeerSlotId_Type()
)
cfprFabricComputeSlotEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPeerSlotId.setStatus("current")
_CfprFabricComputeSlotEpPortId_Type = CfprFabricPIoEpPortId
_CfprFabricComputeSlotEpPortId_Object = MibTableColumn
cfprFabricComputeSlotEpPortId = _CfprFabricComputeSlotEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 42),
    _CfprFabricComputeSlotEpPortId_Type()
)
cfprFabricComputeSlotEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPortId.setStatus("current")
_CfprFabricComputeSlotEpPresence_Type = CfprEquipmentSlotStatus
_CfprFabricComputeSlotEpPresence_Object = MibTableColumn
cfprFabricComputeSlotEpPresence = _CfprFabricComputeSlotEpPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 43),
    _CfprFabricComputeSlotEpPresence_Type()
)
cfprFabricComputeSlotEpPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPresence.setStatus("current")
_CfprFabricComputeSlotEpPresencePath_Type = CfprEquipmentConnectionStatus
_CfprFabricComputeSlotEpPresencePath_Object = MibTableColumn
cfprFabricComputeSlotEpPresencePath = _CfprFabricComputeSlotEpPresencePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 44),
    _CfprFabricComputeSlotEpPresencePath_Type()
)
cfprFabricComputeSlotEpPresencePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpPresencePath.setStatus("current")
_CfprFabricComputeSlotEpRevision_Type = SnmpAdminString
_CfprFabricComputeSlotEpRevision_Object = MibTableColumn
cfprFabricComputeSlotEpRevision = _CfprFabricComputeSlotEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 45),
    _CfprFabricComputeSlotEpRevision_Type()
)
cfprFabricComputeSlotEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpRevision.setStatus("current")
_CfprFabricComputeSlotEpSerial_Type = SnmpAdminString
_CfprFabricComputeSlotEpSerial_Object = MibTableColumn
cfprFabricComputeSlotEpSerial = _CfprFabricComputeSlotEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 46),
    _CfprFabricComputeSlotEpSerial_Type()
)
cfprFabricComputeSlotEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpSerial.setStatus("current")
_CfprFabricComputeSlotEpSlotId_Type = CfprFabricComputeSlotEpSlotId
_CfprFabricComputeSlotEpSlotId_Object = MibTableColumn
cfprFabricComputeSlotEpSlotId = _CfprFabricComputeSlotEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 47),
    _CfprFabricComputeSlotEpSlotId_Type()
)
cfprFabricComputeSlotEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpSlotId.setStatus("current")
_CfprFabricComputeSlotEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricComputeSlotEpSwitchId_Object = MibTableColumn
cfprFabricComputeSlotEpSwitchId = _CfprFabricComputeSlotEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 48),
    _CfprFabricComputeSlotEpSwitchId_Type()
)
cfprFabricComputeSlotEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpSwitchId.setStatus("current")
_CfprFabricComputeSlotEpTransport_Type = CfprNetworkTransport
_CfprFabricComputeSlotEpTransport_Object = MibTableColumn
cfprFabricComputeSlotEpTransport = _CfprFabricComputeSlotEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 49),
    _CfprFabricComputeSlotEpTransport_Type()
)
cfprFabricComputeSlotEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpTransport.setStatus("current")
_CfprFabricComputeSlotEpType_Type = CfprFabricComputeEpType
_CfprFabricComputeSlotEpType_Object = MibTableColumn
cfprFabricComputeSlotEpType = _CfprFabricComputeSlotEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 50),
    _CfprFabricComputeSlotEpType_Type()
)
cfprFabricComputeSlotEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpType.setStatus("current")
_CfprFabricComputeSlotEpVendor_Type = SnmpAdminString
_CfprFabricComputeSlotEpVendor_Object = MibTableColumn
cfprFabricComputeSlotEpVendor = _CfprFabricComputeSlotEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 51),
    _CfprFabricComputeSlotEpVendor_Type()
)
cfprFabricComputeSlotEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpVendor.setStatus("current")
_CfprFabricComputeSlotEpBladeState_Type = CfprLsOperState
_CfprFabricComputeSlotEpBladeState_Object = MibTableColumn
cfprFabricComputeSlotEpBladeState = _CfprFabricComputeSlotEpBladeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 52),
    _CfprFabricComputeSlotEpBladeState_Type()
)
cfprFabricComputeSlotEpBladeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpBladeState.setStatus("current")
_CfprFabricComputeSlotEpDecommissionSecure_Type = CfprComputeDecommissionState
_CfprFabricComputeSlotEpDecommissionSecure_Object = MibTableColumn
cfprFabricComputeSlotEpDecommissionSecure = _CfprFabricComputeSlotEpDecommissionSecure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 53),
    _CfprFabricComputeSlotEpDecommissionSecure_Type()
)
cfprFabricComputeSlotEpDecommissionSecure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpDecommissionSecure.setStatus("current")
_CfprFabricComputeSlotEpFailReason_Type = SnmpAdminString
_CfprFabricComputeSlotEpFailReason_Object = MibTableColumn
cfprFabricComputeSlotEpFailReason = _CfprFabricComputeSlotEpFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 9, 1, 54),
    _CfprFabricComputeSlotEpFailReason_Type()
)
cfprFabricComputeSlotEpFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFailReason.setStatus("current")
_CfprFabricComputeSlotEpFsmTable_Object = MibTable
cfprFabricComputeSlotEpFsmTable = _CfprFabricComputeSlotEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10)
)
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTable.setStatus("current")
_CfprFabricComputeSlotEpFsmEntry_Object = MibTableRow
cfprFabricComputeSlotEpFsmEntry = _CfprFabricComputeSlotEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1)
)
cfprFabricComputeSlotEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricComputeSlotEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmEntry.setStatus("current")
_CfprFabricComputeSlotEpFsmInstanceId_Type = CfprManagedObjectId
_CfprFabricComputeSlotEpFsmInstanceId_Object = MibTableColumn
cfprFabricComputeSlotEpFsmInstanceId = _CfprFabricComputeSlotEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 1),
    _CfprFabricComputeSlotEpFsmInstanceId_Type()
)
cfprFabricComputeSlotEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmInstanceId.setStatus("current")
_CfprFabricComputeSlotEpFsmDn_Type = CfprManagedObjectDn
_CfprFabricComputeSlotEpFsmDn_Object = MibTableColumn
cfprFabricComputeSlotEpFsmDn = _CfprFabricComputeSlotEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 2),
    _CfprFabricComputeSlotEpFsmDn_Type()
)
cfprFabricComputeSlotEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmDn.setStatus("current")
_CfprFabricComputeSlotEpFsmRn_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmRn_Object = MibTableColumn
cfprFabricComputeSlotEpFsmRn = _CfprFabricComputeSlotEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 3),
    _CfprFabricComputeSlotEpFsmRn_Type()
)
cfprFabricComputeSlotEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmRn.setStatus("current")
_CfprFabricComputeSlotEpFsmCompletionTime_Type = DateAndTime
_CfprFabricComputeSlotEpFsmCompletionTime_Object = MibTableColumn
cfprFabricComputeSlotEpFsmCompletionTime = _CfprFabricComputeSlotEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 4),
    _CfprFabricComputeSlotEpFsmCompletionTime_Type()
)
cfprFabricComputeSlotEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmCompletionTime.setStatus("current")
_CfprFabricComputeSlotEpFsmCurrentFsm_Type = CfprFabricComputeSlotEpFsmCurrentFsm
_CfprFabricComputeSlotEpFsmCurrentFsm_Object = MibTableColumn
cfprFabricComputeSlotEpFsmCurrentFsm = _CfprFabricComputeSlotEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 5),
    _CfprFabricComputeSlotEpFsmCurrentFsm_Type()
)
cfprFabricComputeSlotEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmCurrentFsm.setStatus("current")
_CfprFabricComputeSlotEpFsmDescrData_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmDescrData_Object = MibTableColumn
cfprFabricComputeSlotEpFsmDescrData = _CfprFabricComputeSlotEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 6),
    _CfprFabricComputeSlotEpFsmDescrData_Type()
)
cfprFabricComputeSlotEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmDescrData.setStatus("current")
_CfprFabricComputeSlotEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFabricComputeSlotEpFsmFsmStatus_Object = MibTableColumn
cfprFabricComputeSlotEpFsmFsmStatus = _CfprFabricComputeSlotEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 7),
    _CfprFabricComputeSlotEpFsmFsmStatus_Type()
)
cfprFabricComputeSlotEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmFsmStatus.setStatus("current")
_CfprFabricComputeSlotEpFsmProgress_Type = Gauge32
_CfprFabricComputeSlotEpFsmProgress_Object = MibTableColumn
cfprFabricComputeSlotEpFsmProgress = _CfprFabricComputeSlotEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 8),
    _CfprFabricComputeSlotEpFsmProgress_Type()
)
cfprFabricComputeSlotEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmProgress.setStatus("current")
_CfprFabricComputeSlotEpFsmRmtErrCode_Type = Gauge32
_CfprFabricComputeSlotEpFsmRmtErrCode_Object = MibTableColumn
cfprFabricComputeSlotEpFsmRmtErrCode = _CfprFabricComputeSlotEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 9),
    _CfprFabricComputeSlotEpFsmRmtErrCode_Type()
)
cfprFabricComputeSlotEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmRmtErrCode.setStatus("current")
_CfprFabricComputeSlotEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmRmtErrDescr_Object = MibTableColumn
cfprFabricComputeSlotEpFsmRmtErrDescr = _CfprFabricComputeSlotEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 10),
    _CfprFabricComputeSlotEpFsmRmtErrDescr_Type()
)
cfprFabricComputeSlotEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmRmtErrDescr.setStatus("current")
_CfprFabricComputeSlotEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricComputeSlotEpFsmRmtRslt_Object = MibTableColumn
cfprFabricComputeSlotEpFsmRmtRslt = _CfprFabricComputeSlotEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 10, 1, 11),
    _CfprFabricComputeSlotEpFsmRmtRslt_Type()
)
cfprFabricComputeSlotEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmRmtRslt.setStatus("current")
_CfprFabricComputeSlotEpFsmStageTable_Object = MibTable
cfprFabricComputeSlotEpFsmStageTable = _CfprFabricComputeSlotEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11)
)
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageTable.setStatus("current")
_CfprFabricComputeSlotEpFsmStageEntry_Object = MibTableRow
cfprFabricComputeSlotEpFsmStageEntry = _CfprFabricComputeSlotEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1)
)
cfprFabricComputeSlotEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricComputeSlotEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageEntry.setStatus("current")
_CfprFabricComputeSlotEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFabricComputeSlotEpFsmStageInstanceId_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageInstanceId = _CfprFabricComputeSlotEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 1),
    _CfprFabricComputeSlotEpFsmStageInstanceId_Type()
)
cfprFabricComputeSlotEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageInstanceId.setStatus("current")
_CfprFabricComputeSlotEpFsmStageDn_Type = CfprManagedObjectDn
_CfprFabricComputeSlotEpFsmStageDn_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageDn = _CfprFabricComputeSlotEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 2),
    _CfprFabricComputeSlotEpFsmStageDn_Type()
)
cfprFabricComputeSlotEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageDn.setStatus("current")
_CfprFabricComputeSlotEpFsmStageRn_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmStageRn_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageRn = _CfprFabricComputeSlotEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 3),
    _CfprFabricComputeSlotEpFsmStageRn_Type()
)
cfprFabricComputeSlotEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageRn.setStatus("current")
_CfprFabricComputeSlotEpFsmStageDescrData_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmStageDescrData_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageDescrData = _CfprFabricComputeSlotEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 4),
    _CfprFabricComputeSlotEpFsmStageDescrData_Type()
)
cfprFabricComputeSlotEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageDescrData.setStatus("current")
_CfprFabricComputeSlotEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprFabricComputeSlotEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageLastUpdateTime = _CfprFabricComputeSlotEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 5),
    _CfprFabricComputeSlotEpFsmStageLastUpdateTime_Type()
)
cfprFabricComputeSlotEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageLastUpdateTime.setStatus("current")
_CfprFabricComputeSlotEpFsmStageName_Type = CfprFabricComputeSlotEpFsmStageName
_CfprFabricComputeSlotEpFsmStageName_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageName = _CfprFabricComputeSlotEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 6),
    _CfprFabricComputeSlotEpFsmStageName_Type()
)
cfprFabricComputeSlotEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageName.setStatus("current")
_CfprFabricComputeSlotEpFsmStageOrder_Type = Gauge32
_CfprFabricComputeSlotEpFsmStageOrder_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageOrder = _CfprFabricComputeSlotEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 7),
    _CfprFabricComputeSlotEpFsmStageOrder_Type()
)
cfprFabricComputeSlotEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageOrder.setStatus("current")
_CfprFabricComputeSlotEpFsmStageRetry_Type = Gauge32
_CfprFabricComputeSlotEpFsmStageRetry_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageRetry = _CfprFabricComputeSlotEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 8),
    _CfprFabricComputeSlotEpFsmStageRetry_Type()
)
cfprFabricComputeSlotEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageRetry.setStatus("current")
_CfprFabricComputeSlotEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFabricComputeSlotEpFsmStageStageStatus_Object = MibTableColumn
cfprFabricComputeSlotEpFsmStageStageStatus = _CfprFabricComputeSlotEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 11, 1, 9),
    _CfprFabricComputeSlotEpFsmStageStageStatus_Type()
)
cfprFabricComputeSlotEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmStageStageStatus.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskTable_Object = MibTable
cfprFabricComputeSlotEpFsmTaskTable = _CfprFabricComputeSlotEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12)
)
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskTable.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskEntry_Object = MibTableRow
cfprFabricComputeSlotEpFsmTaskEntry = _CfprFabricComputeSlotEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12, 1)
)
cfprFabricComputeSlotEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricComputeSlotEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskEntry.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFabricComputeSlotEpFsmTaskInstanceId_Object = MibTableColumn
cfprFabricComputeSlotEpFsmTaskInstanceId = _CfprFabricComputeSlotEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12, 1, 1),
    _CfprFabricComputeSlotEpFsmTaskInstanceId_Type()
)
cfprFabricComputeSlotEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskInstanceId.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprFabricComputeSlotEpFsmTaskDn_Object = MibTableColumn
cfprFabricComputeSlotEpFsmTaskDn = _CfprFabricComputeSlotEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12, 1, 2),
    _CfprFabricComputeSlotEpFsmTaskDn_Type()
)
cfprFabricComputeSlotEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskDn.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskRn_Type = SnmpAdminString
_CfprFabricComputeSlotEpFsmTaskRn_Object = MibTableColumn
cfprFabricComputeSlotEpFsmTaskRn = _CfprFabricComputeSlotEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12, 1, 3),
    _CfprFabricComputeSlotEpFsmTaskRn_Type()
)
cfprFabricComputeSlotEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskRn.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFabricComputeSlotEpFsmTaskCompletion_Object = MibTableColumn
cfprFabricComputeSlotEpFsmTaskCompletion = _CfprFabricComputeSlotEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12, 1, 4),
    _CfprFabricComputeSlotEpFsmTaskCompletion_Type()
)
cfprFabricComputeSlotEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskCompletion.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskFlags_Type = CfprFsmFlags
_CfprFabricComputeSlotEpFsmTaskFlags_Object = MibTableColumn
cfprFabricComputeSlotEpFsmTaskFlags = _CfprFabricComputeSlotEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12, 1, 5),
    _CfprFabricComputeSlotEpFsmTaskFlags_Type()
)
cfprFabricComputeSlotEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskFlags.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskItem_Type = CfprFabricComputeSlotEpFsmTaskItem
_CfprFabricComputeSlotEpFsmTaskItem_Object = MibTableColumn
cfprFabricComputeSlotEpFsmTaskItem = _CfprFabricComputeSlotEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12, 1, 6),
    _CfprFabricComputeSlotEpFsmTaskItem_Type()
)
cfprFabricComputeSlotEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskItem.setStatus("current")
_CfprFabricComputeSlotEpFsmTaskSeqId_Type = Gauge32
_CfprFabricComputeSlotEpFsmTaskSeqId_Object = MibTableColumn
cfprFabricComputeSlotEpFsmTaskSeqId = _CfprFabricComputeSlotEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 12, 1, 7),
    _CfprFabricComputeSlotEpFsmTaskSeqId_Type()
)
cfprFabricComputeSlotEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricComputeSlotEpFsmTaskSeqId.setStatus("current")
_CfprFabricDceSrvTable_Object = MibTable
cfprFabricDceSrvTable = _CfprFabricDceSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13)
)
if mibBuilder.loadTexts:
    cfprFabricDceSrvTable.setStatus("current")
_CfprFabricDceSrvEntry_Object = MibTableRow
cfprFabricDceSrvEntry = _CfprFabricDceSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1)
)
cfprFabricDceSrvEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricDceSrvInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricDceSrvEntry.setStatus("current")
_CfprFabricDceSrvInstanceId_Type = CfprManagedObjectId
_CfprFabricDceSrvInstanceId_Object = MibTableColumn
cfprFabricDceSrvInstanceId = _CfprFabricDceSrvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1, 1),
    _CfprFabricDceSrvInstanceId_Type()
)
cfprFabricDceSrvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricDceSrvInstanceId.setStatus("current")
_CfprFabricDceSrvDn_Type = CfprManagedObjectDn
_CfprFabricDceSrvDn_Object = MibTableColumn
cfprFabricDceSrvDn = _CfprFabricDceSrvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1, 2),
    _CfprFabricDceSrvDn_Type()
)
cfprFabricDceSrvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSrvDn.setStatus("current")
_CfprFabricDceSrvRn_Type = SnmpAdminString
_CfprFabricDceSrvRn_Object = MibTableColumn
cfprFabricDceSrvRn = _CfprFabricDceSrvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1, 3),
    _CfprFabricDceSrvRn_Type()
)
cfprFabricDceSrvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSrvRn.setStatus("current")
_CfprFabricDceSrvId_Type = CfprNetworkSwitchId
_CfprFabricDceSrvId_Object = MibTableColumn
cfprFabricDceSrvId = _CfprFabricDceSrvId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1, 4),
    _CfprFabricDceSrvId_Type()
)
cfprFabricDceSrvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSrvId.setStatus("current")
_CfprFabricDceSrvLocale_Type = CfprFabricInternalLocale
_CfprFabricDceSrvLocale_Object = MibTableColumn
cfprFabricDceSrvLocale = _CfprFabricDceSrvLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1, 5),
    _CfprFabricDceSrvLocale_Type()
)
cfprFabricDceSrvLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSrvLocale.setStatus("current")
_CfprFabricDceSrvName_Type = SnmpAdminString
_CfprFabricDceSrvName_Object = MibTableColumn
cfprFabricDceSrvName = _CfprFabricDceSrvName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1, 6),
    _CfprFabricDceSrvName_Type()
)
cfprFabricDceSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSrvName.setStatus("current")
_CfprFabricDceSrvTransport_Type = CfprFabricInternalDceSrvTransport
_CfprFabricDceSrvTransport_Object = MibTableColumn
cfprFabricDceSrvTransport = _CfprFabricDceSrvTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1, 7),
    _CfprFabricDceSrvTransport_Type()
)
cfprFabricDceSrvTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSrvTransport.setStatus("current")
_CfprFabricDceSrvType_Type = CfprFabricInternalDceSrvType
_CfprFabricDceSrvType_Object = MibTableColumn
cfprFabricDceSrvType = _CfprFabricDceSrvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 13, 1, 8),
    _CfprFabricDceSrvType_Type()
)
cfprFabricDceSrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSrvType.setStatus("current")
_CfprFabricDceSwSrvTable_Object = MibTable
cfprFabricDceSwSrvTable = _CfprFabricDceSwSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14)
)
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvTable.setStatus("current")
_CfprFabricDceSwSrvEntry_Object = MibTableRow
cfprFabricDceSwSrvEntry = _CfprFabricDceSwSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1)
)
cfprFabricDceSwSrvEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricDceSwSrvInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEntry.setStatus("current")
_CfprFabricDceSwSrvInstanceId_Type = CfprManagedObjectId
_CfprFabricDceSwSrvInstanceId_Object = MibTableColumn
cfprFabricDceSwSrvInstanceId = _CfprFabricDceSwSrvInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1, 1),
    _CfprFabricDceSwSrvInstanceId_Type()
)
cfprFabricDceSwSrvInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvInstanceId.setStatus("current")
_CfprFabricDceSwSrvDn_Type = CfprManagedObjectDn
_CfprFabricDceSwSrvDn_Object = MibTableColumn
cfprFabricDceSwSrvDn = _CfprFabricDceSwSrvDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1, 2),
    _CfprFabricDceSwSrvDn_Type()
)
cfprFabricDceSwSrvDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvDn.setStatus("current")
_CfprFabricDceSwSrvRn_Type = SnmpAdminString
_CfprFabricDceSwSrvRn_Object = MibTableColumn
cfprFabricDceSwSrvRn = _CfprFabricDceSwSrvRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1, 3),
    _CfprFabricDceSwSrvRn_Type()
)
cfprFabricDceSwSrvRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvRn.setStatus("current")
_CfprFabricDceSwSrvId_Type = CfprNetworkSwitchId
_CfprFabricDceSwSrvId_Object = MibTableColumn
cfprFabricDceSwSrvId = _CfprFabricDceSwSrvId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1, 4),
    _CfprFabricDceSwSrvId_Type()
)
cfprFabricDceSwSrvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvId.setStatus("current")
_CfprFabricDceSwSrvLocale_Type = CfprFabricInternalLocale
_CfprFabricDceSwSrvLocale_Object = MibTableColumn
cfprFabricDceSwSrvLocale = _CfprFabricDceSwSrvLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1, 5),
    _CfprFabricDceSwSrvLocale_Type()
)
cfprFabricDceSwSrvLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvLocale.setStatus("current")
_CfprFabricDceSwSrvName_Type = SnmpAdminString
_CfprFabricDceSwSrvName_Object = MibTableColumn
cfprFabricDceSwSrvName = _CfprFabricDceSwSrvName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1, 6),
    _CfprFabricDceSwSrvName_Type()
)
cfprFabricDceSwSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvName.setStatus("current")
_CfprFabricDceSwSrvTransport_Type = CfprFabricInternalDceSrvTransport
_CfprFabricDceSwSrvTransport_Object = MibTableColumn
cfprFabricDceSwSrvTransport = _CfprFabricDceSwSrvTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1, 7),
    _CfprFabricDceSwSrvTransport_Type()
)
cfprFabricDceSwSrvTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvTransport.setStatus("current")
_CfprFabricDceSwSrvType_Type = CfprFabricInternalDceSrvType
_CfprFabricDceSwSrvType_Object = MibTableColumn
cfprFabricDceSwSrvType = _CfprFabricDceSwSrvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 14, 1, 8),
    _CfprFabricDceSwSrvType_Type()
)
cfprFabricDceSwSrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvType.setStatus("current")
_CfprFabricDceSwSrvEpTable_Object = MibTable
cfprFabricDceSwSrvEpTable = _CfprFabricDceSwSrvEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15)
)
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpTable.setStatus("current")
_CfprFabricDceSwSrvEpEntry_Object = MibTableRow
cfprFabricDceSwSrvEpEntry = _CfprFabricDceSwSrvEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1)
)
cfprFabricDceSwSrvEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricDceSwSrvEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpEntry.setStatus("current")
_CfprFabricDceSwSrvEpInstanceId_Type = CfprManagedObjectId
_CfprFabricDceSwSrvEpInstanceId_Object = MibTableColumn
cfprFabricDceSwSrvEpInstanceId = _CfprFabricDceSwSrvEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 1),
    _CfprFabricDceSwSrvEpInstanceId_Type()
)
cfprFabricDceSwSrvEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpInstanceId.setStatus("current")
_CfprFabricDceSwSrvEpDn_Type = CfprManagedObjectDn
_CfprFabricDceSwSrvEpDn_Object = MibTableColumn
cfprFabricDceSwSrvEpDn = _CfprFabricDceSwSrvEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 2),
    _CfprFabricDceSwSrvEpDn_Type()
)
cfprFabricDceSwSrvEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpDn.setStatus("current")
_CfprFabricDceSwSrvEpRn_Type = SnmpAdminString
_CfprFabricDceSwSrvEpRn_Object = MibTableColumn
cfprFabricDceSwSrvEpRn = _CfprFabricDceSwSrvEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 3),
    _CfprFabricDceSwSrvEpRn_Type()
)
cfprFabricDceSwSrvEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpRn.setStatus("current")
_CfprFabricDceSwSrvEpAdminState_Type = CfprFabricInternalEpAdminState
_CfprFabricDceSwSrvEpAdminState_Object = MibTableColumn
cfprFabricDceSwSrvEpAdminState = _CfprFabricDceSwSrvEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 4),
    _CfprFabricDceSwSrvEpAdminState_Type()
)
cfprFabricDceSwSrvEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpAdminState.setStatus("current")
_CfprFabricDceSwSrvEpAggrPortId_Type = Gauge32
_CfprFabricDceSwSrvEpAggrPortId_Object = MibTableColumn
cfprFabricDceSwSrvEpAggrPortId = _CfprFabricDceSwSrvEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 5),
    _CfprFabricDceSwSrvEpAggrPortId_Type()
)
cfprFabricDceSwSrvEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpAggrPortId.setStatus("current")
_CfprFabricDceSwSrvEpChassisId_Type = Gauge32
_CfprFabricDceSwSrvEpChassisId_Object = MibTableColumn
cfprFabricDceSwSrvEpChassisId = _CfprFabricDceSwSrvEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 6),
    _CfprFabricDceSwSrvEpChassisId_Type()
)
cfprFabricDceSwSrvEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpChassisId.setStatus("current")
_CfprFabricDceSwSrvEpEpDn_Type = SnmpAdminString
_CfprFabricDceSwSrvEpEpDn_Object = MibTableColumn
cfprFabricDceSwSrvEpEpDn = _CfprFabricDceSwSrvEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 7),
    _CfprFabricDceSwSrvEpEpDn_Type()
)
cfprFabricDceSwSrvEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpEpDn.setStatus("current")
_CfprFabricDceSwSrvEpFltAggr_Type = Unsigned64
_CfprFabricDceSwSrvEpFltAggr_Object = MibTableColumn
cfprFabricDceSwSrvEpFltAggr = _CfprFabricDceSwSrvEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 8),
    _CfprFabricDceSwSrvEpFltAggr_Type()
)
cfprFabricDceSwSrvEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpFltAggr.setStatus("current")
_CfprFabricDceSwSrvEpIfRole_Type = CfprFabricSwSrvEpIfRole
_CfprFabricDceSwSrvEpIfRole_Object = MibTableColumn
cfprFabricDceSwSrvEpIfRole = _CfprFabricDceSwSrvEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 9),
    _CfprFabricDceSwSrvEpIfRole_Type()
)
cfprFabricDceSwSrvEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpIfRole.setStatus("current")
_CfprFabricDceSwSrvEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricDceSwSrvEpIfType_Object = MibTableColumn
cfprFabricDceSwSrvEpIfType = _CfprFabricDceSwSrvEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 10),
    _CfprFabricDceSwSrvEpIfType_Type()
)
cfprFabricDceSwSrvEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpIfType.setStatus("current")
_CfprFabricDceSwSrvEpLicGP_Type = Unsigned64
_CfprFabricDceSwSrvEpLicGP_Object = MibTableColumn
cfprFabricDceSwSrvEpLicGP = _CfprFabricDceSwSrvEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 11),
    _CfprFabricDceSwSrvEpLicGP_Type()
)
cfprFabricDceSwSrvEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpLicGP.setStatus("current")
_CfprFabricDceSwSrvEpLicState_Type = CfprLicenseState
_CfprFabricDceSwSrvEpLicState_Object = MibTableColumn
cfprFabricDceSwSrvEpLicState = _CfprFabricDceSwSrvEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 12),
    _CfprFabricDceSwSrvEpLicState_Type()
)
cfprFabricDceSwSrvEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpLicState.setStatus("current")
_CfprFabricDceSwSrvEpLocale_Type = CfprFabricInternalEpLocale
_CfprFabricDceSwSrvEpLocale_Object = MibTableColumn
cfprFabricDceSwSrvEpLocale = _CfprFabricDceSwSrvEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 13),
    _CfprFabricDceSwSrvEpLocale_Type()
)
cfprFabricDceSwSrvEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpLocale.setStatus("current")
_CfprFabricDceSwSrvEpName_Type = SnmpAdminString
_CfprFabricDceSwSrvEpName_Object = MibTableColumn
cfprFabricDceSwSrvEpName = _CfprFabricDceSwSrvEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 14),
    _CfprFabricDceSwSrvEpName_Type()
)
cfprFabricDceSwSrvEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpName.setStatus("current")
_CfprFabricDceSwSrvEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricDceSwSrvEpOperState_Object = MibTableColumn
cfprFabricDceSwSrvEpOperState = _CfprFabricDceSwSrvEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 15),
    _CfprFabricDceSwSrvEpOperState_Type()
)
cfprFabricDceSwSrvEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpOperState.setStatus("current")
_CfprFabricDceSwSrvEpOperStateReason_Type = SnmpAdminString
_CfprFabricDceSwSrvEpOperStateReason_Object = MibTableColumn
cfprFabricDceSwSrvEpOperStateReason = _CfprFabricDceSwSrvEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 16),
    _CfprFabricDceSwSrvEpOperStateReason_Type()
)
cfprFabricDceSwSrvEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpOperStateReason.setStatus("current")
_CfprFabricDceSwSrvEpPeerAggrPortId_Type = Gauge32
_CfprFabricDceSwSrvEpPeerAggrPortId_Object = MibTableColumn
cfprFabricDceSwSrvEpPeerAggrPortId = _CfprFabricDceSwSrvEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 17),
    _CfprFabricDceSwSrvEpPeerAggrPortId_Type()
)
cfprFabricDceSwSrvEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpPeerAggrPortId.setStatus("current")
_CfprFabricDceSwSrvEpPeerChassisId_Type = Gauge32
_CfprFabricDceSwSrvEpPeerChassisId_Object = MibTableColumn
cfprFabricDceSwSrvEpPeerChassisId = _CfprFabricDceSwSrvEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 18),
    _CfprFabricDceSwSrvEpPeerChassisId_Type()
)
cfprFabricDceSwSrvEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpPeerChassisId.setStatus("current")
_CfprFabricDceSwSrvEpPeerDn_Type = SnmpAdminString
_CfprFabricDceSwSrvEpPeerDn_Object = MibTableColumn
cfprFabricDceSwSrvEpPeerDn = _CfprFabricDceSwSrvEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 19),
    _CfprFabricDceSwSrvEpPeerDn_Type()
)
cfprFabricDceSwSrvEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpPeerDn.setStatus("current")
_CfprFabricDceSwSrvEpPeerPortId_Type = Gauge32
_CfprFabricDceSwSrvEpPeerPortId_Object = MibTableColumn
cfprFabricDceSwSrvEpPeerPortId = _CfprFabricDceSwSrvEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 20),
    _CfprFabricDceSwSrvEpPeerPortId_Type()
)
cfprFabricDceSwSrvEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpPeerPortId.setStatus("current")
_CfprFabricDceSwSrvEpPeerSlotId_Type = Gauge32
_CfprFabricDceSwSrvEpPeerSlotId_Object = MibTableColumn
cfprFabricDceSwSrvEpPeerSlotId = _CfprFabricDceSwSrvEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 21),
    _CfprFabricDceSwSrvEpPeerSlotId_Type()
)
cfprFabricDceSwSrvEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpPeerSlotId.setStatus("current")
_CfprFabricDceSwSrvEpPortId_Type = CfprFabricDceSwSrvEpPortId
_CfprFabricDceSwSrvEpPortId_Object = MibTableColumn
cfprFabricDceSwSrvEpPortId = _CfprFabricDceSwSrvEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 22),
    _CfprFabricDceSwSrvEpPortId_Type()
)
cfprFabricDceSwSrvEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpPortId.setStatus("current")
_CfprFabricDceSwSrvEpSlotId_Type = CfprFabricDceSwSrvEpSlotId
_CfprFabricDceSwSrvEpSlotId_Object = MibTableColumn
cfprFabricDceSwSrvEpSlotId = _CfprFabricDceSwSrvEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 23),
    _CfprFabricDceSwSrvEpSlotId_Type()
)
cfprFabricDceSwSrvEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpSlotId.setStatus("current")
_CfprFabricDceSwSrvEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricDceSwSrvEpSwitchId_Object = MibTableColumn
cfprFabricDceSwSrvEpSwitchId = _CfprFabricDceSwSrvEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 24),
    _CfprFabricDceSwSrvEpSwitchId_Type()
)
cfprFabricDceSwSrvEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpSwitchId.setStatus("current")
_CfprFabricDceSwSrvEpTransport_Type = CfprFabricADceSwSrvEpTransport
_CfprFabricDceSwSrvEpTransport_Object = MibTableColumn
cfprFabricDceSwSrvEpTransport = _CfprFabricDceSwSrvEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 25),
    _CfprFabricDceSwSrvEpTransport_Type()
)
cfprFabricDceSwSrvEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpTransport.setStatus("current")
_CfprFabricDceSwSrvEpType_Type = CfprFabricSwSrvEpType
_CfprFabricDceSwSrvEpType_Object = MibTableColumn
cfprFabricDceSwSrvEpType = _CfprFabricDceSwSrvEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 26),
    _CfprFabricDceSwSrvEpType_Type()
)
cfprFabricDceSwSrvEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpType.setStatus("current")
_CfprFabricDceSwSrvEpUsrLbl_Type = SnmpAdminString
_CfprFabricDceSwSrvEpUsrLbl_Object = MibTableColumn
cfprFabricDceSwSrvEpUsrLbl = _CfprFabricDceSwSrvEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 15, 1, 27),
    _CfprFabricDceSwSrvEpUsrLbl_Type()
)
cfprFabricDceSwSrvEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvEpUsrLbl.setStatus("current")
_CfprFabricDceSwSrvPcTable_Object = MibTable
cfprFabricDceSwSrvPcTable = _CfprFabricDceSwSrvPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16)
)
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcTable.setStatus("current")
_CfprFabricDceSwSrvPcEntry_Object = MibTableRow
cfprFabricDceSwSrvPcEntry = _CfprFabricDceSwSrvPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1)
)
cfprFabricDceSwSrvPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricDceSwSrvPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEntry.setStatus("current")
_CfprFabricDceSwSrvPcInstanceId_Type = CfprManagedObjectId
_CfprFabricDceSwSrvPcInstanceId_Object = MibTableColumn
cfprFabricDceSwSrvPcInstanceId = _CfprFabricDceSwSrvPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 1),
    _CfprFabricDceSwSrvPcInstanceId_Type()
)
cfprFabricDceSwSrvPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcInstanceId.setStatus("current")
_CfprFabricDceSwSrvPcDn_Type = CfprManagedObjectDn
_CfprFabricDceSwSrvPcDn_Object = MibTableColumn
cfprFabricDceSwSrvPcDn = _CfprFabricDceSwSrvPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 2),
    _CfprFabricDceSwSrvPcDn_Type()
)
cfprFabricDceSwSrvPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcDn.setStatus("current")
_CfprFabricDceSwSrvPcRn_Type = SnmpAdminString
_CfprFabricDceSwSrvPcRn_Object = MibTableColumn
cfprFabricDceSwSrvPcRn = _CfprFabricDceSwSrvPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 3),
    _CfprFabricDceSwSrvPcRn_Type()
)
cfprFabricDceSwSrvPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcRn.setStatus("current")
_CfprFabricDceSwSrvPcAdminState_Type = CfprFabricDceSwSrvPcAdminState
_CfprFabricDceSwSrvPcAdminState_Object = MibTableColumn
cfprFabricDceSwSrvPcAdminState = _CfprFabricDceSwSrvPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 4),
    _CfprFabricDceSwSrvPcAdminState_Type()
)
cfprFabricDceSwSrvPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcAdminState.setStatus("current")
_CfprFabricDceSwSrvPcChassisId_Type = Gauge32
_CfprFabricDceSwSrvPcChassisId_Object = MibTableColumn
cfprFabricDceSwSrvPcChassisId = _CfprFabricDceSwSrvPcChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 5),
    _CfprFabricDceSwSrvPcChassisId_Type()
)
cfprFabricDceSwSrvPcChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcChassisId.setStatus("current")
_CfprFabricDceSwSrvPcDescr_Type = SnmpAdminString
_CfprFabricDceSwSrvPcDescr_Object = MibTableColumn
cfprFabricDceSwSrvPcDescr = _CfprFabricDceSwSrvPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 6),
    _CfprFabricDceSwSrvPcDescr_Type()
)
cfprFabricDceSwSrvPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcDescr.setStatus("current")
_CfprFabricDceSwSrvPcEpDn_Type = SnmpAdminString
_CfprFabricDceSwSrvPcEpDn_Object = MibTableColumn
cfprFabricDceSwSrvPcEpDn = _CfprFabricDceSwSrvPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 7),
    _CfprFabricDceSwSrvPcEpDn_Type()
)
cfprFabricDceSwSrvPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpDn.setStatus("current")
_CfprFabricDceSwSrvPcFltAggr_Type = Unsigned64
_CfprFabricDceSwSrvPcFltAggr_Object = MibTableColumn
cfprFabricDceSwSrvPcFltAggr = _CfprFabricDceSwSrvPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 8),
    _CfprFabricDceSwSrvPcFltAggr_Type()
)
cfprFabricDceSwSrvPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcFltAggr.setStatus("current")
_CfprFabricDceSwSrvPcIfRole_Type = CfprFabricSwSrvPcIfRole
_CfprFabricDceSwSrvPcIfRole_Object = MibTableColumn
cfprFabricDceSwSrvPcIfRole = _CfprFabricDceSwSrvPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 9),
    _CfprFabricDceSwSrvPcIfRole_Type()
)
cfprFabricDceSwSrvPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcIfRole.setStatus("current")
_CfprFabricDceSwSrvPcIfType_Type = CfprFabricCIoEpIfType
_CfprFabricDceSwSrvPcIfType_Object = MibTableColumn
cfprFabricDceSwSrvPcIfType = _CfprFabricDceSwSrvPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 10),
    _CfprFabricDceSwSrvPcIfType_Type()
)
cfprFabricDceSwSrvPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcIfType.setStatus("current")
_CfprFabricDceSwSrvPcLocale_Type = CfprFabricInternalPcLocale
_CfprFabricDceSwSrvPcLocale_Object = MibTableColumn
cfprFabricDceSwSrvPcLocale = _CfprFabricDceSwSrvPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 11),
    _CfprFabricDceSwSrvPcLocale_Type()
)
cfprFabricDceSwSrvPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcLocale.setStatus("current")
_CfprFabricDceSwSrvPcName_Type = SnmpAdminString
_CfprFabricDceSwSrvPcName_Object = MibTableColumn
cfprFabricDceSwSrvPcName = _CfprFabricDceSwSrvPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 12),
    _CfprFabricDceSwSrvPcName_Type()
)
cfprFabricDceSwSrvPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcName.setStatus("current")
_CfprFabricDceSwSrvPcOperSpeed_Type = CfprPortEthSpeed
_CfprFabricDceSwSrvPcOperSpeed_Object = MibTableColumn
cfprFabricDceSwSrvPcOperSpeed = _CfprFabricDceSwSrvPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 13),
    _CfprFabricDceSwSrvPcOperSpeed_Type()
)
cfprFabricDceSwSrvPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcOperSpeed.setStatus("current")
_CfprFabricDceSwSrvPcOperState_Type = CfprNetworkPortOperState
_CfprFabricDceSwSrvPcOperState_Object = MibTableColumn
cfprFabricDceSwSrvPcOperState = _CfprFabricDceSwSrvPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 14),
    _CfprFabricDceSwSrvPcOperState_Type()
)
cfprFabricDceSwSrvPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcOperState.setStatus("current")
_CfprFabricDceSwSrvPcPeerDn_Type = SnmpAdminString
_CfprFabricDceSwSrvPcPeerDn_Object = MibTableColumn
cfprFabricDceSwSrvPcPeerDn = _CfprFabricDceSwSrvPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 15),
    _CfprFabricDceSwSrvPcPeerDn_Type()
)
cfprFabricDceSwSrvPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcPeerDn.setStatus("current")
_CfprFabricDceSwSrvPcPortId_Type = CfprFabricDceSwSrvPcPortId
_CfprFabricDceSwSrvPcPortId_Object = MibTableColumn
cfprFabricDceSwSrvPcPortId = _CfprFabricDceSwSrvPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 16),
    _CfprFabricDceSwSrvPcPortId_Type()
)
cfprFabricDceSwSrvPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcPortId.setStatus("current")
_CfprFabricDceSwSrvPcStateQual_Type = SnmpAdminString
_CfprFabricDceSwSrvPcStateQual_Object = MibTableColumn
cfprFabricDceSwSrvPcStateQual = _CfprFabricDceSwSrvPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 17),
    _CfprFabricDceSwSrvPcStateQual_Type()
)
cfprFabricDceSwSrvPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcStateQual.setStatus("current")
_CfprFabricDceSwSrvPcSwitchId_Type = CfprNetworkSwitchId
_CfprFabricDceSwSrvPcSwitchId_Object = MibTableColumn
cfprFabricDceSwSrvPcSwitchId = _CfprFabricDceSwSrvPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 18),
    _CfprFabricDceSwSrvPcSwitchId_Type()
)
cfprFabricDceSwSrvPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcSwitchId.setStatus("current")
_CfprFabricDceSwSrvPcTransport_Type = CfprFabricDceSwSrvPcTransport
_CfprFabricDceSwSrvPcTransport_Object = MibTableColumn
cfprFabricDceSwSrvPcTransport = _CfprFabricDceSwSrvPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 19),
    _CfprFabricDceSwSrvPcTransport_Type()
)
cfprFabricDceSwSrvPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcTransport.setStatus("current")
_CfprFabricDceSwSrvPcType_Type = CfprFabricSwSrvPcType
_CfprFabricDceSwSrvPcType_Object = MibTableColumn
cfprFabricDceSwSrvPcType = _CfprFabricDceSwSrvPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 16, 1, 20),
    _CfprFabricDceSwSrvPcType_Type()
)
cfprFabricDceSwSrvPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcType.setStatus("current")
_CfprFabricDceSwSrvPcEpTable_Object = MibTable
cfprFabricDceSwSrvPcEpTable = _CfprFabricDceSwSrvPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17)
)
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpTable.setStatus("current")
_CfprFabricDceSwSrvPcEpEntry_Object = MibTableRow
cfprFabricDceSwSrvPcEpEntry = _CfprFabricDceSwSrvPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1)
)
cfprFabricDceSwSrvPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricDceSwSrvPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpEntry.setStatus("current")
_CfprFabricDceSwSrvPcEpInstanceId_Type = CfprManagedObjectId
_CfprFabricDceSwSrvPcEpInstanceId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpInstanceId = _CfprFabricDceSwSrvPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 1),
    _CfprFabricDceSwSrvPcEpInstanceId_Type()
)
cfprFabricDceSwSrvPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpInstanceId.setStatus("current")
_CfprFabricDceSwSrvPcEpDnData_Type = CfprManagedObjectDn
_CfprFabricDceSwSrvPcEpDnData_Object = MibTableColumn
cfprFabricDceSwSrvPcEpDnData = _CfprFabricDceSwSrvPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 2),
    _CfprFabricDceSwSrvPcEpDnData_Type()
)
cfprFabricDceSwSrvPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpDnData.setStatus("current")
_CfprFabricDceSwSrvPcEpRn_Type = SnmpAdminString
_CfprFabricDceSwSrvPcEpRn_Object = MibTableColumn
cfprFabricDceSwSrvPcEpRn = _CfprFabricDceSwSrvPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 3),
    _CfprFabricDceSwSrvPcEpRn_Type()
)
cfprFabricDceSwSrvPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpRn.setStatus("current")
_CfprFabricDceSwSrvPcEpAdminState_Type = CfprFabricInternalEpAdminState
_CfprFabricDceSwSrvPcEpAdminState_Object = MibTableColumn
cfprFabricDceSwSrvPcEpAdminState = _CfprFabricDceSwSrvPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 4),
    _CfprFabricDceSwSrvPcEpAdminState_Type()
)
cfprFabricDceSwSrvPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpAdminState.setStatus("current")
_CfprFabricDceSwSrvPcEpAggrPortId_Type = Gauge32
_CfprFabricDceSwSrvPcEpAggrPortId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpAggrPortId = _CfprFabricDceSwSrvPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 5),
    _CfprFabricDceSwSrvPcEpAggrPortId_Type()
)
cfprFabricDceSwSrvPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpAggrPortId.setStatus("current")
_CfprFabricDceSwSrvPcEpChassisId_Type = Gauge32
_CfprFabricDceSwSrvPcEpChassisId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpChassisId = _CfprFabricDceSwSrvPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 6),
    _CfprFabricDceSwSrvPcEpChassisId_Type()
)
cfprFabricDceSwSrvPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpChassisId.setStatus("current")
_CfprFabricDceSwSrvPcEpEpDn_Type = SnmpAdminString
_CfprFabricDceSwSrvPcEpEpDn_Object = MibTableColumn
cfprFabricDceSwSrvPcEpEpDn = _CfprFabricDceSwSrvPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 7),
    _CfprFabricDceSwSrvPcEpEpDn_Type()
)
cfprFabricDceSwSrvPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpEpDn.setStatus("current")
_CfprFabricDceSwSrvPcEpFltAggr_Type = Unsigned64
_CfprFabricDceSwSrvPcEpFltAggr_Object = MibTableColumn
cfprFabricDceSwSrvPcEpFltAggr = _CfprFabricDceSwSrvPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 8),
    _CfprFabricDceSwSrvPcEpFltAggr_Type()
)
cfprFabricDceSwSrvPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpFltAggr.setStatus("current")
_CfprFabricDceSwSrvPcEpIfRole_Type = CfprFabricSwSrvEpIfRole
_CfprFabricDceSwSrvPcEpIfRole_Object = MibTableColumn
cfprFabricDceSwSrvPcEpIfRole = _CfprFabricDceSwSrvPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 9),
    _CfprFabricDceSwSrvPcEpIfRole_Type()
)
cfprFabricDceSwSrvPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpIfRole.setStatus("current")
_CfprFabricDceSwSrvPcEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricDceSwSrvPcEpIfType_Object = MibTableColumn
cfprFabricDceSwSrvPcEpIfType = _CfprFabricDceSwSrvPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 10),
    _CfprFabricDceSwSrvPcEpIfType_Type()
)
cfprFabricDceSwSrvPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpIfType.setStatus("current")
_CfprFabricDceSwSrvPcEpLicGP_Type = Unsigned64
_CfprFabricDceSwSrvPcEpLicGP_Object = MibTableColumn
cfprFabricDceSwSrvPcEpLicGP = _CfprFabricDceSwSrvPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 11),
    _CfprFabricDceSwSrvPcEpLicGP_Type()
)
cfprFabricDceSwSrvPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpLicGP.setStatus("current")
_CfprFabricDceSwSrvPcEpLicState_Type = CfprLicenseState
_CfprFabricDceSwSrvPcEpLicState_Object = MibTableColumn
cfprFabricDceSwSrvPcEpLicState = _CfprFabricDceSwSrvPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 12),
    _CfprFabricDceSwSrvPcEpLicState_Type()
)
cfprFabricDceSwSrvPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpLicState.setStatus("current")
_CfprFabricDceSwSrvPcEpLocale_Type = CfprFabricInternalEpLocale
_CfprFabricDceSwSrvPcEpLocale_Object = MibTableColumn
cfprFabricDceSwSrvPcEpLocale = _CfprFabricDceSwSrvPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 13),
    _CfprFabricDceSwSrvPcEpLocale_Type()
)
cfprFabricDceSwSrvPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpLocale.setStatus("current")
_CfprFabricDceSwSrvPcEpMembership_Type = CfprFabricMembershipStatus
_CfprFabricDceSwSrvPcEpMembership_Object = MibTableColumn
cfprFabricDceSwSrvPcEpMembership = _CfprFabricDceSwSrvPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 14),
    _CfprFabricDceSwSrvPcEpMembership_Type()
)
cfprFabricDceSwSrvPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpMembership.setStatus("current")
_CfprFabricDceSwSrvPcEpName_Type = SnmpAdminString
_CfprFabricDceSwSrvPcEpName_Object = MibTableColumn
cfprFabricDceSwSrvPcEpName = _CfprFabricDceSwSrvPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 15),
    _CfprFabricDceSwSrvPcEpName_Type()
)
cfprFabricDceSwSrvPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpName.setStatus("current")
_CfprFabricDceSwSrvPcEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricDceSwSrvPcEpOperState_Object = MibTableColumn
cfprFabricDceSwSrvPcEpOperState = _CfprFabricDceSwSrvPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 16),
    _CfprFabricDceSwSrvPcEpOperState_Type()
)
cfprFabricDceSwSrvPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpOperState.setStatus("current")
_CfprFabricDceSwSrvPcEpOperStateReason_Type = SnmpAdminString
_CfprFabricDceSwSrvPcEpOperStateReason_Object = MibTableColumn
cfprFabricDceSwSrvPcEpOperStateReason = _CfprFabricDceSwSrvPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 17),
    _CfprFabricDceSwSrvPcEpOperStateReason_Type()
)
cfprFabricDceSwSrvPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpOperStateReason.setStatus("current")
_CfprFabricDceSwSrvPcEpPeerAggrPortId_Type = Gauge32
_CfprFabricDceSwSrvPcEpPeerAggrPortId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpPeerAggrPortId = _CfprFabricDceSwSrvPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 18),
    _CfprFabricDceSwSrvPcEpPeerAggrPortId_Type()
)
cfprFabricDceSwSrvPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpPeerAggrPortId.setStatus("current")
_CfprFabricDceSwSrvPcEpPeerChassisId_Type = Gauge32
_CfprFabricDceSwSrvPcEpPeerChassisId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpPeerChassisId = _CfprFabricDceSwSrvPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 19),
    _CfprFabricDceSwSrvPcEpPeerChassisId_Type()
)
cfprFabricDceSwSrvPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpPeerChassisId.setStatus("current")
_CfprFabricDceSwSrvPcEpPeerDn_Type = SnmpAdminString
_CfprFabricDceSwSrvPcEpPeerDn_Object = MibTableColumn
cfprFabricDceSwSrvPcEpPeerDn = _CfprFabricDceSwSrvPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 20),
    _CfprFabricDceSwSrvPcEpPeerDn_Type()
)
cfprFabricDceSwSrvPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpPeerDn.setStatus("current")
_CfprFabricDceSwSrvPcEpPeerPortId_Type = Gauge32
_CfprFabricDceSwSrvPcEpPeerPortId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpPeerPortId = _CfprFabricDceSwSrvPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 21),
    _CfprFabricDceSwSrvPcEpPeerPortId_Type()
)
cfprFabricDceSwSrvPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpPeerPortId.setStatus("current")
_CfprFabricDceSwSrvPcEpPeerSlotId_Type = Gauge32
_CfprFabricDceSwSrvPcEpPeerSlotId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpPeerSlotId = _CfprFabricDceSwSrvPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 22),
    _CfprFabricDceSwSrvPcEpPeerSlotId_Type()
)
cfprFabricDceSwSrvPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpPeerSlotId.setStatus("current")
_CfprFabricDceSwSrvPcEpPortId_Type = CfprFabricDceSwSrvPcEpPortId
_CfprFabricDceSwSrvPcEpPortId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpPortId = _CfprFabricDceSwSrvPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 23),
    _CfprFabricDceSwSrvPcEpPortId_Type()
)
cfprFabricDceSwSrvPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpPortId.setStatus("current")
_CfprFabricDceSwSrvPcEpSlotId_Type = CfprFabricDceSwSrvPcEpSlotId
_CfprFabricDceSwSrvPcEpSlotId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpSlotId = _CfprFabricDceSwSrvPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 24),
    _CfprFabricDceSwSrvPcEpSlotId_Type()
)
cfprFabricDceSwSrvPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpSlotId.setStatus("current")
_CfprFabricDceSwSrvPcEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricDceSwSrvPcEpSwitchId_Object = MibTableColumn
cfprFabricDceSwSrvPcEpSwitchId = _CfprFabricDceSwSrvPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 25),
    _CfprFabricDceSwSrvPcEpSwitchId_Type()
)
cfprFabricDceSwSrvPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpSwitchId.setStatus("current")
_CfprFabricDceSwSrvPcEpTransport_Type = CfprFabricADceSwSrvEpTransport
_CfprFabricDceSwSrvPcEpTransport_Object = MibTableColumn
cfprFabricDceSwSrvPcEpTransport = _CfprFabricDceSwSrvPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 26),
    _CfprFabricDceSwSrvPcEpTransport_Type()
)
cfprFabricDceSwSrvPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpTransport.setStatus("current")
_CfprFabricDceSwSrvPcEpType_Type = CfprFabricSwSrvEpType
_CfprFabricDceSwSrvPcEpType_Object = MibTableColumn
cfprFabricDceSwSrvPcEpType = _CfprFabricDceSwSrvPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 27),
    _CfprFabricDceSwSrvPcEpType_Type()
)
cfprFabricDceSwSrvPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpType.setStatus("current")
_CfprFabricDceSwSrvPcEpUsrLbl_Type = SnmpAdminString
_CfprFabricDceSwSrvPcEpUsrLbl_Object = MibTableColumn
cfprFabricDceSwSrvPcEpUsrLbl = _CfprFabricDceSwSrvPcEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 17, 1, 28),
    _CfprFabricDceSwSrvPcEpUsrLbl_Type()
)
cfprFabricDceSwSrvPcEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricDceSwSrvPcEpUsrLbl.setStatus("current")
_CfprFabricEpTable_Object = MibTable
cfprFabricEpTable = _CfprFabricEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 18)
)
if mibBuilder.loadTexts:
    cfprFabricEpTable.setStatus("current")
_CfprFabricEpEntry_Object = MibTableRow
cfprFabricEpEntry = _CfprFabricEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 18, 1)
)
cfprFabricEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEpEntry.setStatus("current")
_CfprFabricEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEpInstanceId_Object = MibTableColumn
cfprFabricEpInstanceId = _CfprFabricEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 18, 1, 1),
    _CfprFabricEpInstanceId_Type()
)
cfprFabricEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEpInstanceId.setStatus("current")
_CfprFabricEpDn_Type = CfprManagedObjectDn
_CfprFabricEpDn_Object = MibTableColumn
cfprFabricEpDn = _CfprFabricEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 18, 1, 2),
    _CfprFabricEpDn_Type()
)
cfprFabricEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpDn.setStatus("current")
_CfprFabricEpRn_Type = SnmpAdminString
_CfprFabricEpRn_Object = MibTableColumn
cfprFabricEpRn = _CfprFabricEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 18, 1, 3),
    _CfprFabricEpRn_Type()
)
cfprFabricEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpRn.setStatus("current")
_CfprFabricEpMgrTable_Object = MibTable
cfprFabricEpMgrTable = _CfprFabricEpMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19)
)
if mibBuilder.loadTexts:
    cfprFabricEpMgrTable.setStatus("current")
_CfprFabricEpMgrEntry_Object = MibTableRow
cfprFabricEpMgrEntry = _CfprFabricEpMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1)
)
cfprFabricEpMgrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEpMgrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEpMgrEntry.setStatus("current")
_CfprFabricEpMgrInstanceId_Type = CfprManagedObjectId
_CfprFabricEpMgrInstanceId_Object = MibTableColumn
cfprFabricEpMgrInstanceId = _CfprFabricEpMgrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 1),
    _CfprFabricEpMgrInstanceId_Type()
)
cfprFabricEpMgrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEpMgrInstanceId.setStatus("current")
_CfprFabricEpMgrDn_Type = CfprManagedObjectDn
_CfprFabricEpMgrDn_Object = MibTableColumn
cfprFabricEpMgrDn = _CfprFabricEpMgrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 2),
    _CfprFabricEpMgrDn_Type()
)
cfprFabricEpMgrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrDn.setStatus("current")
_CfprFabricEpMgrRn_Type = SnmpAdminString
_CfprFabricEpMgrRn_Object = MibTableColumn
cfprFabricEpMgrRn = _CfprFabricEpMgrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 3),
    _CfprFabricEpMgrRn_Type()
)
cfprFabricEpMgrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrRn.setStatus("current")
_CfprFabricEpMgrConfMode_Type = CfprFabricConfMode
_CfprFabricEpMgrConfMode_Object = MibTableColumn
cfprFabricEpMgrConfMode = _CfprFabricEpMgrConfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 4),
    _CfprFabricEpMgrConfMode_Type()
)
cfprFabricEpMgrConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrConfMode.setStatus("current")
_CfprFabricEpMgrConfQual_Type = SnmpAdminString
_CfprFabricEpMgrConfQual_Object = MibTableColumn
cfprFabricEpMgrConfQual = _CfprFabricEpMgrConfQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 5),
    _CfprFabricEpMgrConfQual_Type()
)
cfprFabricEpMgrConfQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrConfQual.setStatus("current")
_CfprFabricEpMgrConfState_Type = CfprFabricConfState
_CfprFabricEpMgrConfState_Object = MibTableColumn
cfprFabricEpMgrConfState = _CfprFabricEpMgrConfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 6),
    _CfprFabricEpMgrConfState_Type()
)
cfprFabricEpMgrConfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrConfState.setStatus("current")
_CfprFabricEpMgrFltAggr_Type = Unsigned64
_CfprFabricEpMgrFltAggr_Object = MibTableColumn
cfprFabricEpMgrFltAggr = _CfprFabricEpMgrFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 7),
    _CfprFabricEpMgrFltAggr_Type()
)
cfprFabricEpMgrFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFltAggr.setStatus("current")
_CfprFabricEpMgrFsmDescr_Type = SnmpAdminString
_CfprFabricEpMgrFsmDescr_Object = MibTableColumn
cfprFabricEpMgrFsmDescr = _CfprFabricEpMgrFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 8),
    _CfprFabricEpMgrFsmDescr_Type()
)
cfprFabricEpMgrFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmDescr.setStatus("current")
_CfprFabricEpMgrFsmFlags_Type = SnmpAdminString
_CfprFabricEpMgrFsmFlags_Object = MibTableColumn
cfprFabricEpMgrFsmFlags = _CfprFabricEpMgrFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 9),
    _CfprFabricEpMgrFsmFlags_Type()
)
cfprFabricEpMgrFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmFlags.setStatus("current")
_CfprFabricEpMgrFsmPrev_Type = SnmpAdminString
_CfprFabricEpMgrFsmPrev_Object = MibTableColumn
cfprFabricEpMgrFsmPrev = _CfprFabricEpMgrFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 10),
    _CfprFabricEpMgrFsmPrev_Type()
)
cfprFabricEpMgrFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmPrev.setStatus("current")
_CfprFabricEpMgrFsmProgr_Type = Gauge32
_CfprFabricEpMgrFsmProgr_Object = MibTableColumn
cfprFabricEpMgrFsmProgr = _CfprFabricEpMgrFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 11),
    _CfprFabricEpMgrFsmProgr_Type()
)
cfprFabricEpMgrFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmProgr.setStatus("current")
_CfprFabricEpMgrFsmRmtInvErrCode_Type = Gauge32
_CfprFabricEpMgrFsmRmtInvErrCode_Object = MibTableColumn
cfprFabricEpMgrFsmRmtInvErrCode = _CfprFabricEpMgrFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 12),
    _CfprFabricEpMgrFsmRmtInvErrCode_Type()
)
cfprFabricEpMgrFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmRmtInvErrCode.setStatus("current")
_CfprFabricEpMgrFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFabricEpMgrFsmRmtInvErrDescr_Object = MibTableColumn
cfprFabricEpMgrFsmRmtInvErrDescr = _CfprFabricEpMgrFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 13),
    _CfprFabricEpMgrFsmRmtInvErrDescr_Type()
)
cfprFabricEpMgrFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmRmtInvErrDescr.setStatus("current")
_CfprFabricEpMgrFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricEpMgrFsmRmtInvRslt_Object = MibTableColumn
cfprFabricEpMgrFsmRmtInvRslt = _CfprFabricEpMgrFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 14),
    _CfprFabricEpMgrFsmRmtInvRslt_Type()
)
cfprFabricEpMgrFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmRmtInvRslt.setStatus("current")
_CfprFabricEpMgrFsmStageDescr_Type = SnmpAdminString
_CfprFabricEpMgrFsmStageDescr_Object = MibTableColumn
cfprFabricEpMgrFsmStageDescr = _CfprFabricEpMgrFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 15),
    _CfprFabricEpMgrFsmStageDescr_Type()
)
cfprFabricEpMgrFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageDescr.setStatus("current")
_CfprFabricEpMgrFsmStamp_Type = DateAndTime
_CfprFabricEpMgrFsmStamp_Object = MibTableColumn
cfprFabricEpMgrFsmStamp = _CfprFabricEpMgrFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 16),
    _CfprFabricEpMgrFsmStamp_Type()
)
cfprFabricEpMgrFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStamp.setStatus("current")
_CfprFabricEpMgrFsmStatus_Type = SnmpAdminString
_CfprFabricEpMgrFsmStatus_Object = MibTableColumn
cfprFabricEpMgrFsmStatus = _CfprFabricEpMgrFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 17),
    _CfprFabricEpMgrFsmStatus_Type()
)
cfprFabricEpMgrFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStatus.setStatus("current")
_CfprFabricEpMgrFsmTry_Type = Gauge32
_CfprFabricEpMgrFsmTry_Object = MibTableColumn
cfprFabricEpMgrFsmTry = _CfprFabricEpMgrFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 18),
    _CfprFabricEpMgrFsmTry_Type()
)
cfprFabricEpMgrFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTry.setStatus("current")
_CfprFabricEpMgrId_Type = CfprNetworkSwitchId
_CfprFabricEpMgrId_Object = MibTableColumn
cfprFabricEpMgrId = _CfprFabricEpMgrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 19, 1, 19),
    _CfprFabricEpMgrId_Type()
)
cfprFabricEpMgrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrId.setStatus("current")
_CfprFabricEpMgrFsmTable_Object = MibTable
cfprFabricEpMgrFsmTable = _CfprFabricEpMgrFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20)
)
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTable.setStatus("current")
_CfprFabricEpMgrFsmEntry_Object = MibTableRow
cfprFabricEpMgrFsmEntry = _CfprFabricEpMgrFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1)
)
cfprFabricEpMgrFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEpMgrFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmEntry.setStatus("current")
_CfprFabricEpMgrFsmInstanceId_Type = CfprManagedObjectId
_CfprFabricEpMgrFsmInstanceId_Object = MibTableColumn
cfprFabricEpMgrFsmInstanceId = _CfprFabricEpMgrFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 1),
    _CfprFabricEpMgrFsmInstanceId_Type()
)
cfprFabricEpMgrFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmInstanceId.setStatus("current")
_CfprFabricEpMgrFsmDn_Type = CfprManagedObjectDn
_CfprFabricEpMgrFsmDn_Object = MibTableColumn
cfprFabricEpMgrFsmDn = _CfprFabricEpMgrFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 2),
    _CfprFabricEpMgrFsmDn_Type()
)
cfprFabricEpMgrFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmDn.setStatus("current")
_CfprFabricEpMgrFsmRn_Type = SnmpAdminString
_CfprFabricEpMgrFsmRn_Object = MibTableColumn
cfprFabricEpMgrFsmRn = _CfprFabricEpMgrFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 3),
    _CfprFabricEpMgrFsmRn_Type()
)
cfprFabricEpMgrFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmRn.setStatus("current")
_CfprFabricEpMgrFsmCompletionTime_Type = DateAndTime
_CfprFabricEpMgrFsmCompletionTime_Object = MibTableColumn
cfprFabricEpMgrFsmCompletionTime = _CfprFabricEpMgrFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 4),
    _CfprFabricEpMgrFsmCompletionTime_Type()
)
cfprFabricEpMgrFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmCompletionTime.setStatus("current")
_CfprFabricEpMgrFsmCurrentFsm_Type = CfprFabricEpMgrFsmCurrentFsm
_CfprFabricEpMgrFsmCurrentFsm_Object = MibTableColumn
cfprFabricEpMgrFsmCurrentFsm = _CfprFabricEpMgrFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 5),
    _CfprFabricEpMgrFsmCurrentFsm_Type()
)
cfprFabricEpMgrFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmCurrentFsm.setStatus("current")
_CfprFabricEpMgrFsmDescrData_Type = SnmpAdminString
_CfprFabricEpMgrFsmDescrData_Object = MibTableColumn
cfprFabricEpMgrFsmDescrData = _CfprFabricEpMgrFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 6),
    _CfprFabricEpMgrFsmDescrData_Type()
)
cfprFabricEpMgrFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmDescrData.setStatus("current")
_CfprFabricEpMgrFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFabricEpMgrFsmFsmStatus_Object = MibTableColumn
cfprFabricEpMgrFsmFsmStatus = _CfprFabricEpMgrFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 7),
    _CfprFabricEpMgrFsmFsmStatus_Type()
)
cfprFabricEpMgrFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmFsmStatus.setStatus("current")
_CfprFabricEpMgrFsmProgress_Type = Gauge32
_CfprFabricEpMgrFsmProgress_Object = MibTableColumn
cfprFabricEpMgrFsmProgress = _CfprFabricEpMgrFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 8),
    _CfprFabricEpMgrFsmProgress_Type()
)
cfprFabricEpMgrFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmProgress.setStatus("current")
_CfprFabricEpMgrFsmRmtErrCode_Type = Gauge32
_CfprFabricEpMgrFsmRmtErrCode_Object = MibTableColumn
cfprFabricEpMgrFsmRmtErrCode = _CfprFabricEpMgrFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 9),
    _CfprFabricEpMgrFsmRmtErrCode_Type()
)
cfprFabricEpMgrFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmRmtErrCode.setStatus("current")
_CfprFabricEpMgrFsmRmtErrDescr_Type = SnmpAdminString
_CfprFabricEpMgrFsmRmtErrDescr_Object = MibTableColumn
cfprFabricEpMgrFsmRmtErrDescr = _CfprFabricEpMgrFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 10),
    _CfprFabricEpMgrFsmRmtErrDescr_Type()
)
cfprFabricEpMgrFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmRmtErrDescr.setStatus("current")
_CfprFabricEpMgrFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricEpMgrFsmRmtRslt_Object = MibTableColumn
cfprFabricEpMgrFsmRmtRslt = _CfprFabricEpMgrFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 20, 1, 11),
    _CfprFabricEpMgrFsmRmtRslt_Type()
)
cfprFabricEpMgrFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmRmtRslt.setStatus("current")
_CfprFabricEpMgrFsmStageTable_Object = MibTable
cfprFabricEpMgrFsmStageTable = _CfprFabricEpMgrFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21)
)
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageTable.setStatus("current")
_CfprFabricEpMgrFsmStageEntry_Object = MibTableRow
cfprFabricEpMgrFsmStageEntry = _CfprFabricEpMgrFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1)
)
cfprFabricEpMgrFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEpMgrFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageEntry.setStatus("current")
_CfprFabricEpMgrFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFabricEpMgrFsmStageInstanceId_Object = MibTableColumn
cfprFabricEpMgrFsmStageInstanceId = _CfprFabricEpMgrFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 1),
    _CfprFabricEpMgrFsmStageInstanceId_Type()
)
cfprFabricEpMgrFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageInstanceId.setStatus("current")
_CfprFabricEpMgrFsmStageDn_Type = CfprManagedObjectDn
_CfprFabricEpMgrFsmStageDn_Object = MibTableColumn
cfprFabricEpMgrFsmStageDn = _CfprFabricEpMgrFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 2),
    _CfprFabricEpMgrFsmStageDn_Type()
)
cfprFabricEpMgrFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageDn.setStatus("current")
_CfprFabricEpMgrFsmStageRn_Type = SnmpAdminString
_CfprFabricEpMgrFsmStageRn_Object = MibTableColumn
cfprFabricEpMgrFsmStageRn = _CfprFabricEpMgrFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 3),
    _CfprFabricEpMgrFsmStageRn_Type()
)
cfprFabricEpMgrFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageRn.setStatus("current")
_CfprFabricEpMgrFsmStageDescrData_Type = SnmpAdminString
_CfprFabricEpMgrFsmStageDescrData_Object = MibTableColumn
cfprFabricEpMgrFsmStageDescrData = _CfprFabricEpMgrFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 4),
    _CfprFabricEpMgrFsmStageDescrData_Type()
)
cfprFabricEpMgrFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageDescrData.setStatus("current")
_CfprFabricEpMgrFsmStageLastUpdateTime_Type = DateAndTime
_CfprFabricEpMgrFsmStageLastUpdateTime_Object = MibTableColumn
cfprFabricEpMgrFsmStageLastUpdateTime = _CfprFabricEpMgrFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 5),
    _CfprFabricEpMgrFsmStageLastUpdateTime_Type()
)
cfprFabricEpMgrFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageLastUpdateTime.setStatus("current")
_CfprFabricEpMgrFsmStageName_Type = CfprFabricEpMgrFsmStageName
_CfprFabricEpMgrFsmStageName_Object = MibTableColumn
cfprFabricEpMgrFsmStageName = _CfprFabricEpMgrFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 6),
    _CfprFabricEpMgrFsmStageName_Type()
)
cfprFabricEpMgrFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageName.setStatus("current")
_CfprFabricEpMgrFsmStageOrder_Type = Gauge32
_CfprFabricEpMgrFsmStageOrder_Object = MibTableColumn
cfprFabricEpMgrFsmStageOrder = _CfprFabricEpMgrFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 7),
    _CfprFabricEpMgrFsmStageOrder_Type()
)
cfprFabricEpMgrFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageOrder.setStatus("current")
_CfprFabricEpMgrFsmStageRetry_Type = Gauge32
_CfprFabricEpMgrFsmStageRetry_Object = MibTableColumn
cfprFabricEpMgrFsmStageRetry = _CfprFabricEpMgrFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 8),
    _CfprFabricEpMgrFsmStageRetry_Type()
)
cfprFabricEpMgrFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageRetry.setStatus("current")
_CfprFabricEpMgrFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFabricEpMgrFsmStageStageStatus_Object = MibTableColumn
cfprFabricEpMgrFsmStageStageStatus = _CfprFabricEpMgrFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 21, 1, 9),
    _CfprFabricEpMgrFsmStageStageStatus_Type()
)
cfprFabricEpMgrFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmStageStageStatus.setStatus("current")
_CfprFabricEpMgrFsmTaskTable_Object = MibTable
cfprFabricEpMgrFsmTaskTable = _CfprFabricEpMgrFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22)
)
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskTable.setStatus("current")
_CfprFabricEpMgrFsmTaskEntry_Object = MibTableRow
cfprFabricEpMgrFsmTaskEntry = _CfprFabricEpMgrFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22, 1)
)
cfprFabricEpMgrFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEpMgrFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskEntry.setStatus("current")
_CfprFabricEpMgrFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFabricEpMgrFsmTaskInstanceId_Object = MibTableColumn
cfprFabricEpMgrFsmTaskInstanceId = _CfprFabricEpMgrFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22, 1, 1),
    _CfprFabricEpMgrFsmTaskInstanceId_Type()
)
cfprFabricEpMgrFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskInstanceId.setStatus("current")
_CfprFabricEpMgrFsmTaskDn_Type = CfprManagedObjectDn
_CfprFabricEpMgrFsmTaskDn_Object = MibTableColumn
cfprFabricEpMgrFsmTaskDn = _CfprFabricEpMgrFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22, 1, 2),
    _CfprFabricEpMgrFsmTaskDn_Type()
)
cfprFabricEpMgrFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskDn.setStatus("current")
_CfprFabricEpMgrFsmTaskRn_Type = SnmpAdminString
_CfprFabricEpMgrFsmTaskRn_Object = MibTableColumn
cfprFabricEpMgrFsmTaskRn = _CfprFabricEpMgrFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22, 1, 3),
    _CfprFabricEpMgrFsmTaskRn_Type()
)
cfprFabricEpMgrFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskRn.setStatus("current")
_CfprFabricEpMgrFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFabricEpMgrFsmTaskCompletion_Object = MibTableColumn
cfprFabricEpMgrFsmTaskCompletion = _CfprFabricEpMgrFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22, 1, 4),
    _CfprFabricEpMgrFsmTaskCompletion_Type()
)
cfprFabricEpMgrFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskCompletion.setStatus("current")
_CfprFabricEpMgrFsmTaskFlags_Type = CfprFabricEpMgrFsmTaskFlags
_CfprFabricEpMgrFsmTaskFlags_Object = MibTableColumn
cfprFabricEpMgrFsmTaskFlags = _CfprFabricEpMgrFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22, 1, 5),
    _CfprFabricEpMgrFsmTaskFlags_Type()
)
cfprFabricEpMgrFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskFlags.setStatus("current")
_CfprFabricEpMgrFsmTaskItem_Type = CfprFabricEpMgrFsmTaskItem
_CfprFabricEpMgrFsmTaskItem_Object = MibTableColumn
cfprFabricEpMgrFsmTaskItem = _CfprFabricEpMgrFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22, 1, 6),
    _CfprFabricEpMgrFsmTaskItem_Type()
)
cfprFabricEpMgrFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskItem.setStatus("current")
_CfprFabricEpMgrFsmTaskSeqId_Type = Gauge32
_CfprFabricEpMgrFsmTaskSeqId_Object = MibTableColumn
cfprFabricEpMgrFsmTaskSeqId = _CfprFabricEpMgrFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 22, 1, 7),
    _CfprFabricEpMgrFsmTaskSeqId_Type()
)
cfprFabricEpMgrFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEpMgrFsmTaskSeqId.setStatus("current")
_CfprFabricEthEstcTable_Object = MibTable
cfprFabricEthEstcTable = _CfprFabricEthEstcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23)
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcTable.setStatus("current")
_CfprFabricEthEstcEntry_Object = MibTableRow
cfprFabricEthEstcEntry = _CfprFabricEthEstcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1)
)
cfprFabricEthEstcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthEstcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcEntry.setStatus("current")
_CfprFabricEthEstcInstanceId_Type = CfprManagedObjectId
_CfprFabricEthEstcInstanceId_Object = MibTableColumn
cfprFabricEthEstcInstanceId = _CfprFabricEthEstcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1, 1),
    _CfprFabricEthEstcInstanceId_Type()
)
cfprFabricEthEstcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthEstcInstanceId.setStatus("current")
_CfprFabricEthEstcDn_Type = CfprManagedObjectDn
_CfprFabricEthEstcDn_Object = MibTableColumn
cfprFabricEthEstcDn = _CfprFabricEthEstcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1, 2),
    _CfprFabricEthEstcDn_Type()
)
cfprFabricEthEstcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcDn.setStatus("current")
_CfprFabricEthEstcRn_Type = SnmpAdminString
_CfprFabricEthEstcRn_Object = MibTableColumn
cfprFabricEthEstcRn = _CfprFabricEthEstcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1, 3),
    _CfprFabricEthEstcRn_Type()
)
cfprFabricEthEstcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcRn.setStatus("current")
_CfprFabricEthEstcId_Type = CfprNetworkSwitchId
_CfprFabricEthEstcId_Object = MibTableColumn
cfprFabricEthEstcId = _CfprFabricEthEstcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1, 4),
    _CfprFabricEthEstcId_Type()
)
cfprFabricEthEstcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcId.setStatus("current")
_CfprFabricEthEstcLocale_Type = CfprFabricExternalLocale
_CfprFabricEthEstcLocale_Object = MibTableColumn
cfprFabricEthEstcLocale = _CfprFabricEthEstcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1, 5),
    _CfprFabricEthEstcLocale_Type()
)
cfprFabricEthEstcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcLocale.setStatus("current")
_CfprFabricEthEstcName_Type = SnmpAdminString
_CfprFabricEthEstcName_Object = MibTableColumn
cfprFabricEthEstcName = _CfprFabricEthEstcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1, 6),
    _CfprFabricEthEstcName_Type()
)
cfprFabricEthEstcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcName.setStatus("current")
_CfprFabricEthEstcTransport_Type = CfprFabricEthEstcTransport
_CfprFabricEthEstcTransport_Object = MibTableColumn
cfprFabricEthEstcTransport = _CfprFabricEthEstcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1, 7),
    _CfprFabricEthEstcTransport_Type()
)
cfprFabricEthEstcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcTransport.setStatus("current")
_CfprFabricEthEstcType_Type = CfprFabricEthEstcType
_CfprFabricEthEstcType_Object = MibTableColumn
cfprFabricEthEstcType = _CfprFabricEthEstcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 23, 1, 8),
    _CfprFabricEthEstcType_Type()
)
cfprFabricEthEstcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcType.setStatus("current")
_CfprFabricEthEstcCloudTable_Object = MibTable
cfprFabricEthEstcCloudTable = _CfprFabricEthEstcCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 24)
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcCloudTable.setStatus("current")
_CfprFabricEthEstcCloudEntry_Object = MibTableRow
cfprFabricEthEstcCloudEntry = _CfprFabricEthEstcCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 24, 1)
)
cfprFabricEthEstcCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthEstcCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcCloudEntry.setStatus("current")
_CfprFabricEthEstcCloudInstanceId_Type = CfprManagedObjectId
_CfprFabricEthEstcCloudInstanceId_Object = MibTableColumn
cfprFabricEthEstcCloudInstanceId = _CfprFabricEthEstcCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 24, 1, 1),
    _CfprFabricEthEstcCloudInstanceId_Type()
)
cfprFabricEthEstcCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthEstcCloudInstanceId.setStatus("current")
_CfprFabricEthEstcCloudDn_Type = CfprManagedObjectDn
_CfprFabricEthEstcCloudDn_Object = MibTableColumn
cfprFabricEthEstcCloudDn = _CfprFabricEthEstcCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 24, 1, 2),
    _CfprFabricEthEstcCloudDn_Type()
)
cfprFabricEthEstcCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcCloudDn.setStatus("current")
_CfprFabricEthEstcCloudRn_Type = SnmpAdminString
_CfprFabricEthEstcCloudRn_Object = MibTableColumn
cfprFabricEthEstcCloudRn = _CfprFabricEthEstcCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 24, 1, 3),
    _CfprFabricEthEstcCloudRn_Type()
)
cfprFabricEthEstcCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcCloudRn.setStatus("current")
_CfprFabricEthEstcEpTable_Object = MibTable
cfprFabricEthEstcEpTable = _CfprFabricEthEstcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25)
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpTable.setStatus("current")
_CfprFabricEthEstcEpEntry_Object = MibTableRow
cfprFabricEthEstcEpEntry = _CfprFabricEthEstcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1)
)
cfprFabricEthEstcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthEstcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpEntry.setStatus("current")
_CfprFabricEthEstcEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthEstcEpInstanceId_Object = MibTableColumn
cfprFabricEthEstcEpInstanceId = _CfprFabricEthEstcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 1),
    _CfprFabricEthEstcEpInstanceId_Type()
)
cfprFabricEthEstcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpInstanceId.setStatus("current")
_CfprFabricEthEstcEpDn_Type = CfprManagedObjectDn
_CfprFabricEthEstcEpDn_Object = MibTableColumn
cfprFabricEthEstcEpDn = _CfprFabricEthEstcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 2),
    _CfprFabricEthEstcEpDn_Type()
)
cfprFabricEthEstcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpDn.setStatus("current")
_CfprFabricEthEstcEpRn_Type = SnmpAdminString
_CfprFabricEthEstcEpRn_Object = MibTableColumn
cfprFabricEthEstcEpRn = _CfprFabricEthEstcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 3),
    _CfprFabricEthEstcEpRn_Type()
)
cfprFabricEthEstcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpRn.setStatus("current")
_CfprFabricEthEstcEpAdminSpeed_Type = CfprPortEthSpeed
_CfprFabricEthEstcEpAdminSpeed_Object = MibTableColumn
cfprFabricEthEstcEpAdminSpeed = _CfprFabricEthEstcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 4),
    _CfprFabricEthEstcEpAdminSpeed_Type()
)
cfprFabricEthEstcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpAdminSpeed.setStatus("current")
_CfprFabricEthEstcEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricEthEstcEpAdminState_Object = MibTableColumn
cfprFabricEthEstcEpAdminState = _CfprFabricEthEstcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 5),
    _CfprFabricEthEstcEpAdminState_Type()
)
cfprFabricEthEstcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpAdminState.setStatus("current")
_CfprFabricEthEstcEpAggrPortId_Type = Gauge32
_CfprFabricEthEstcEpAggrPortId_Object = MibTableColumn
cfprFabricEthEstcEpAggrPortId = _CfprFabricEthEstcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 6),
    _CfprFabricEthEstcEpAggrPortId_Type()
)
cfprFabricEthEstcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpAggrPortId.setStatus("current")
_CfprFabricEthEstcEpChassisId_Type = Gauge32
_CfprFabricEthEstcEpChassisId_Object = MibTableColumn
cfprFabricEthEstcEpChassisId = _CfprFabricEthEstcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 7),
    _CfprFabricEthEstcEpChassisId_Type()
)
cfprFabricEthEstcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpChassisId.setStatus("current")
_CfprFabricEthEstcEpConfigState_Type = CfprFabricConfigState
_CfprFabricEthEstcEpConfigState_Object = MibTableColumn
cfprFabricEthEstcEpConfigState = _CfprFabricEthEstcEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 8),
    _CfprFabricEthEstcEpConfigState_Type()
)
cfprFabricEthEstcEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpConfigState.setStatus("current")
_CfprFabricEthEstcEpEpDn_Type = SnmpAdminString
_CfprFabricEthEstcEpEpDn_Object = MibTableColumn
cfprFabricEthEstcEpEpDn = _CfprFabricEthEstcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 9),
    _CfprFabricEthEstcEpEpDn_Type()
)
cfprFabricEthEstcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpEpDn.setStatus("current")
_CfprFabricEthEstcEpFlowCtrlPolicy_Type = SnmpAdminString
_CfprFabricEthEstcEpFlowCtrlPolicy_Object = MibTableColumn
cfprFabricEthEstcEpFlowCtrlPolicy = _CfprFabricEthEstcEpFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 10),
    _CfprFabricEthEstcEpFlowCtrlPolicy_Type()
)
cfprFabricEthEstcEpFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpFlowCtrlPolicy.setStatus("current")
_CfprFabricEthEstcEpFltAggr_Type = Unsigned64
_CfprFabricEthEstcEpFltAggr_Object = MibTableColumn
cfprFabricEthEstcEpFltAggr = _CfprFabricEthEstcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 11),
    _CfprFabricEthEstcEpFltAggr_Type()
)
cfprFabricEthEstcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpFltAggr.setStatus("current")
_CfprFabricEthEstcEpIfRole_Type = CfprFabricAEthEstcEpIfRole
_CfprFabricEthEstcEpIfRole_Object = MibTableColumn
cfprFabricEthEstcEpIfRole = _CfprFabricEthEstcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 12),
    _CfprFabricEthEstcEpIfRole_Type()
)
cfprFabricEthEstcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpIfRole.setStatus("current")
_CfprFabricEthEstcEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricEthEstcEpIfType_Object = MibTableColumn
cfprFabricEthEstcEpIfType = _CfprFabricEthEstcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 13),
    _CfprFabricEthEstcEpIfType_Type()
)
cfprFabricEthEstcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpIfType.setStatus("current")
_CfprFabricEthEstcEpLicGP_Type = Unsigned64
_CfprFabricEthEstcEpLicGP_Object = MibTableColumn
cfprFabricEthEstcEpLicGP = _CfprFabricEthEstcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 14),
    _CfprFabricEthEstcEpLicGP_Type()
)
cfprFabricEthEstcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpLicGP.setStatus("current")
_CfprFabricEthEstcEpLicState_Type = CfprLicenseState
_CfprFabricEthEstcEpLicState_Object = MibTableColumn
cfprFabricEthEstcEpLicState = _CfprFabricEthEstcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 15),
    _CfprFabricEthEstcEpLicState_Type()
)
cfprFabricEthEstcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpLicState.setStatus("current")
_CfprFabricEthEstcEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricEthEstcEpLocale_Object = MibTableColumn
cfprFabricEthEstcEpLocale = _CfprFabricEthEstcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 16),
    _CfprFabricEthEstcEpLocale_Type()
)
cfprFabricEthEstcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpLocale.setStatus("current")
_CfprFabricEthEstcEpName_Type = SnmpAdminString
_CfprFabricEthEstcEpName_Object = MibTableColumn
cfprFabricEthEstcEpName = _CfprFabricEthEstcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 17),
    _CfprFabricEthEstcEpName_Type()
)
cfprFabricEthEstcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpName.setStatus("current")
_CfprFabricEthEstcEpNwCtrlPolicyName_Type = SnmpAdminString
_CfprFabricEthEstcEpNwCtrlPolicyName_Object = MibTableColumn
cfprFabricEthEstcEpNwCtrlPolicyName = _CfprFabricEthEstcEpNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 18),
    _CfprFabricEthEstcEpNwCtrlPolicyName_Type()
)
cfprFabricEthEstcEpNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpNwCtrlPolicyName.setStatus("current")
_CfprFabricEthEstcEpOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprFabricEthEstcEpOperNwCtrlPolicyName_Object = MibTableColumn
cfprFabricEthEstcEpOperNwCtrlPolicyName = _CfprFabricEthEstcEpOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 19),
    _CfprFabricEthEstcEpOperNwCtrlPolicyName_Type()
)
cfprFabricEthEstcEpOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpOperNwCtrlPolicyName.setStatus("current")
_CfprFabricEthEstcEpOperPortMode_Type = CfprFabricEthEstcOperPortMode
_CfprFabricEthEstcEpOperPortMode_Object = MibTableColumn
cfprFabricEthEstcEpOperPortMode = _CfprFabricEthEstcEpOperPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 20),
    _CfprFabricEthEstcEpOperPortMode_Type()
)
cfprFabricEthEstcEpOperPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpOperPortMode.setStatus("current")
_CfprFabricEthEstcEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricEthEstcEpOperState_Object = MibTableColumn
cfprFabricEthEstcEpOperState = _CfprFabricEthEstcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 21),
    _CfprFabricEthEstcEpOperState_Type()
)
cfprFabricEthEstcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpOperState.setStatus("current")
_CfprFabricEthEstcEpOperStateReason_Type = SnmpAdminString
_CfprFabricEthEstcEpOperStateReason_Object = MibTableColumn
cfprFabricEthEstcEpOperStateReason = _CfprFabricEthEstcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 22),
    _CfprFabricEthEstcEpOperStateReason_Type()
)
cfprFabricEthEstcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpOperStateReason.setStatus("current")
_CfprFabricEthEstcEpPeerAggrPortId_Type = Gauge32
_CfprFabricEthEstcEpPeerAggrPortId_Object = MibTableColumn
cfprFabricEthEstcEpPeerAggrPortId = _CfprFabricEthEstcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 23),
    _CfprFabricEthEstcEpPeerAggrPortId_Type()
)
cfprFabricEthEstcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPeerAggrPortId.setStatus("current")
_CfprFabricEthEstcEpPeerChassisId_Type = Gauge32
_CfprFabricEthEstcEpPeerChassisId_Object = MibTableColumn
cfprFabricEthEstcEpPeerChassisId = _CfprFabricEthEstcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 24),
    _CfprFabricEthEstcEpPeerChassisId_Type()
)
cfprFabricEthEstcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPeerChassisId.setStatus("current")
_CfprFabricEthEstcEpPeerDn_Type = SnmpAdminString
_CfprFabricEthEstcEpPeerDn_Object = MibTableColumn
cfprFabricEthEstcEpPeerDn = _CfprFabricEthEstcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 25),
    _CfprFabricEthEstcEpPeerDn_Type()
)
cfprFabricEthEstcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPeerDn.setStatus("current")
_CfprFabricEthEstcEpPeerPortId_Type = Gauge32
_CfprFabricEthEstcEpPeerPortId_Object = MibTableColumn
cfprFabricEthEstcEpPeerPortId = _CfprFabricEthEstcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 26),
    _CfprFabricEthEstcEpPeerPortId_Type()
)
cfprFabricEthEstcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPeerPortId.setStatus("current")
_CfprFabricEthEstcEpPeerSlotId_Type = Gauge32
_CfprFabricEthEstcEpPeerSlotId_Object = MibTableColumn
cfprFabricEthEstcEpPeerSlotId = _CfprFabricEthEstcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 27),
    _CfprFabricEthEstcEpPeerSlotId_Type()
)
cfprFabricEthEstcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPeerSlotId.setStatus("current")
_CfprFabricEthEstcEpPinGroupName_Type = SnmpAdminString
_CfprFabricEthEstcEpPinGroupName_Object = MibTableColumn
cfprFabricEthEstcEpPinGroupName = _CfprFabricEthEstcEpPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 28),
    _CfprFabricEthEstcEpPinGroupName_Type()
)
cfprFabricEthEstcEpPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPinGroupName.setStatus("current")
_CfprFabricEthEstcEpPortId_Type = CfprFabricEthEstcEpPortId
_CfprFabricEthEstcEpPortId_Object = MibTableColumn
cfprFabricEthEstcEpPortId = _CfprFabricEthEstcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 29),
    _CfprFabricEthEstcEpPortId_Type()
)
cfprFabricEthEstcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPortId.setStatus("current")
_CfprFabricEthEstcEpPortMode_Type = CfprFabricEthEstcPortMode
_CfprFabricEthEstcEpPortMode_Object = MibTableColumn
cfprFabricEthEstcEpPortMode = _CfprFabricEthEstcEpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 30),
    _CfprFabricEthEstcEpPortMode_Type()
)
cfprFabricEthEstcEpPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPortMode.setStatus("current")
_CfprFabricEthEstcEpPrio_Type = CfprFabricEthEstcEpPrio
_CfprFabricEthEstcEpPrio_Object = MibTableColumn
cfprFabricEthEstcEpPrio = _CfprFabricEthEstcEpPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 31),
    _CfprFabricEthEstcEpPrio_Type()
)
cfprFabricEthEstcEpPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpPrio.setStatus("current")
_CfprFabricEthEstcEpSlotId_Type = CfprFabricEthEstcEpSlotId
_CfprFabricEthEstcEpSlotId_Object = MibTableColumn
cfprFabricEthEstcEpSlotId = _CfprFabricEthEstcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 32),
    _CfprFabricEthEstcEpSlotId_Type()
)
cfprFabricEthEstcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpSlotId.setStatus("current")
_CfprFabricEthEstcEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthEstcEpSwitchId_Object = MibTableColumn
cfprFabricEthEstcEpSwitchId = _CfprFabricEthEstcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 33),
    _CfprFabricEthEstcEpSwitchId_Type()
)
cfprFabricEthEstcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpSwitchId.setStatus("current")
_CfprFabricEthEstcEpTransport_Type = CfprFabricEthEstcEpTransport
_CfprFabricEthEstcEpTransport_Object = MibTableColumn
cfprFabricEthEstcEpTransport = _CfprFabricEthEstcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 34),
    _CfprFabricEthEstcEpTransport_Type()
)
cfprFabricEthEstcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpTransport.setStatus("current")
_CfprFabricEthEstcEpType_Type = CfprFabricEthEstcEpType
_CfprFabricEthEstcEpType_Object = MibTableColumn
cfprFabricEthEstcEpType = _CfprFabricEthEstcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 35),
    _CfprFabricEthEstcEpType_Type()
)
cfprFabricEthEstcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpType.setStatus("current")
_CfprFabricEthEstcEpUsrLbl_Type = SnmpAdminString
_CfprFabricEthEstcEpUsrLbl_Object = MibTableColumn
cfprFabricEthEstcEpUsrLbl = _CfprFabricEthEstcEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 36),
    _CfprFabricEthEstcEpUsrLbl_Type()
)
cfprFabricEthEstcEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpUsrLbl.setStatus("current")
_CfprFabricEthEstcEpWarnings_Type = CfprFabricWarnings
_CfprFabricEthEstcEpWarnings_Object = MibTableColumn
cfprFabricEthEstcEpWarnings = _CfprFabricEthEstcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 25, 1, 37),
    _CfprFabricEthEstcEpWarnings_Type()
)
cfprFabricEthEstcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcEpWarnings.setStatus("current")
_CfprFabricEthEstcPcTable_Object = MibTable
cfprFabricEthEstcPcTable = _CfprFabricEthEstcPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26)
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcTable.setStatus("current")
_CfprFabricEthEstcPcEntry_Object = MibTableRow
cfprFabricEthEstcPcEntry = _CfprFabricEthEstcPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1)
)
cfprFabricEthEstcPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthEstcPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEntry.setStatus("current")
_CfprFabricEthEstcPcInstanceId_Type = CfprManagedObjectId
_CfprFabricEthEstcPcInstanceId_Object = MibTableColumn
cfprFabricEthEstcPcInstanceId = _CfprFabricEthEstcPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 1),
    _CfprFabricEthEstcPcInstanceId_Type()
)
cfprFabricEthEstcPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcInstanceId.setStatus("current")
_CfprFabricEthEstcPcDn_Type = CfprManagedObjectDn
_CfprFabricEthEstcPcDn_Object = MibTableColumn
cfprFabricEthEstcPcDn = _CfprFabricEthEstcPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 2),
    _CfprFabricEthEstcPcDn_Type()
)
cfprFabricEthEstcPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcDn.setStatus("current")
_CfprFabricEthEstcPcRn_Type = SnmpAdminString
_CfprFabricEthEstcPcRn_Object = MibTableColumn
cfprFabricEthEstcPcRn = _CfprFabricEthEstcPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 3),
    _CfprFabricEthEstcPcRn_Type()
)
cfprFabricEthEstcPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcRn.setStatus("current")
_CfprFabricEthEstcPcAdminSpeed_Type = CfprPortEthAdminSpeed
_CfprFabricEthEstcPcAdminSpeed_Object = MibTableColumn
cfprFabricEthEstcPcAdminSpeed = _CfprFabricEthEstcPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 4),
    _CfprFabricEthEstcPcAdminSpeed_Type()
)
cfprFabricEthEstcPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcAdminSpeed.setStatus("current")
_CfprFabricEthEstcPcAdminState_Type = CfprFabricCIoEpAdminState
_CfprFabricEthEstcPcAdminState_Object = MibTableColumn
cfprFabricEthEstcPcAdminState = _CfprFabricEthEstcPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 5),
    _CfprFabricEthEstcPcAdminState_Type()
)
cfprFabricEthEstcPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcAdminState.setStatus("current")
_CfprFabricEthEstcPcDescr_Type = SnmpAdminString
_CfprFabricEthEstcPcDescr_Object = MibTableColumn
cfprFabricEthEstcPcDescr = _CfprFabricEthEstcPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 6),
    _CfprFabricEthEstcPcDescr_Type()
)
cfprFabricEthEstcPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcDescr.setStatus("current")
_CfprFabricEthEstcPcEpDn_Type = SnmpAdminString
_CfprFabricEthEstcPcEpDn_Object = MibTableColumn
cfprFabricEthEstcPcEpDn = _CfprFabricEthEstcPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 7),
    _CfprFabricEthEstcPcEpDn_Type()
)
cfprFabricEthEstcPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpDn.setStatus("current")
_CfprFabricEthEstcPcFlowCtrlPolicy_Type = SnmpAdminString
_CfprFabricEthEstcPcFlowCtrlPolicy_Object = MibTableColumn
cfprFabricEthEstcPcFlowCtrlPolicy = _CfprFabricEthEstcPcFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 8),
    _CfprFabricEthEstcPcFlowCtrlPolicy_Type()
)
cfprFabricEthEstcPcFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcFlowCtrlPolicy.setStatus("current")
_CfprFabricEthEstcPcFltAggr_Type = Unsigned64
_CfprFabricEthEstcPcFltAggr_Object = MibTableColumn
cfprFabricEthEstcPcFltAggr = _CfprFabricEthEstcPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 9),
    _CfprFabricEthEstcPcFltAggr_Type()
)
cfprFabricEthEstcPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcFltAggr.setStatus("current")
_CfprFabricEthEstcPcIfRole_Type = CfprFabricEstcPcIfRole
_CfprFabricEthEstcPcIfRole_Object = MibTableColumn
cfprFabricEthEstcPcIfRole = _CfprFabricEthEstcPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 10),
    _CfprFabricEthEstcPcIfRole_Type()
)
cfprFabricEthEstcPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcIfRole.setStatus("current")
_CfprFabricEthEstcPcIfType_Type = CfprFabricCIoEpIfType
_CfprFabricEthEstcPcIfType_Object = MibTableColumn
cfprFabricEthEstcPcIfType = _CfprFabricEthEstcPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 11),
    _CfprFabricEthEstcPcIfType_Type()
)
cfprFabricEthEstcPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcIfType.setStatus("current")
_CfprFabricEthEstcPcLacpPolicyName_Type = SnmpAdminString
_CfprFabricEthEstcPcLacpPolicyName_Object = MibTableColumn
cfprFabricEthEstcPcLacpPolicyName = _CfprFabricEthEstcPcLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 12),
    _CfprFabricEthEstcPcLacpPolicyName_Type()
)
cfprFabricEthEstcPcLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcLacpPolicyName.setStatus("current")
_CfprFabricEthEstcPcLocale_Type = CfprFabricExternalPcLocale
_CfprFabricEthEstcPcLocale_Object = MibTableColumn
cfprFabricEthEstcPcLocale = _CfprFabricEthEstcPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 13),
    _CfprFabricEthEstcPcLocale_Type()
)
cfprFabricEthEstcPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcLocale.setStatus("current")
_CfprFabricEthEstcPcName_Type = SnmpAdminString
_CfprFabricEthEstcPcName_Object = MibTableColumn
cfprFabricEthEstcPcName = _CfprFabricEthEstcPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 14),
    _CfprFabricEthEstcPcName_Type()
)
cfprFabricEthEstcPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcName.setStatus("current")
_CfprFabricEthEstcPcNwCtrlPolicyName_Type = SnmpAdminString
_CfprFabricEthEstcPcNwCtrlPolicyName_Object = MibTableColumn
cfprFabricEthEstcPcNwCtrlPolicyName = _CfprFabricEthEstcPcNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 15),
    _CfprFabricEthEstcPcNwCtrlPolicyName_Type()
)
cfprFabricEthEstcPcNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcNwCtrlPolicyName.setStatus("current")
_CfprFabricEthEstcPcOperLacpPolicyName_Type = SnmpAdminString
_CfprFabricEthEstcPcOperLacpPolicyName_Object = MibTableColumn
cfprFabricEthEstcPcOperLacpPolicyName = _CfprFabricEthEstcPcOperLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 16),
    _CfprFabricEthEstcPcOperLacpPolicyName_Type()
)
cfprFabricEthEstcPcOperLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcOperLacpPolicyName.setStatus("current")
_CfprFabricEthEstcPcOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprFabricEthEstcPcOperNwCtrlPolicyName_Object = MibTableColumn
cfprFabricEthEstcPcOperNwCtrlPolicyName = _CfprFabricEthEstcPcOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 17),
    _CfprFabricEthEstcPcOperNwCtrlPolicyName_Type()
)
cfprFabricEthEstcPcOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcOperNwCtrlPolicyName.setStatus("current")
_CfprFabricEthEstcPcOperSpeed_Type = CfprPortEthSpeed
_CfprFabricEthEstcPcOperSpeed_Object = MibTableColumn
cfprFabricEthEstcPcOperSpeed = _CfprFabricEthEstcPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 18),
    _CfprFabricEthEstcPcOperSpeed_Type()
)
cfprFabricEthEstcPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcOperSpeed.setStatus("current")
_CfprFabricEthEstcPcOperState_Type = CfprNetworkPortOperState
_CfprFabricEthEstcPcOperState_Object = MibTableColumn
cfprFabricEthEstcPcOperState = _CfprFabricEthEstcPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 19),
    _CfprFabricEthEstcPcOperState_Type()
)
cfprFabricEthEstcPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcOperState.setStatus("current")
_CfprFabricEthEstcPcPeerDn_Type = SnmpAdminString
_CfprFabricEthEstcPcPeerDn_Object = MibTableColumn
cfprFabricEthEstcPcPeerDn = _CfprFabricEthEstcPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 20),
    _CfprFabricEthEstcPcPeerDn_Type()
)
cfprFabricEthEstcPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcPeerDn.setStatus("current")
_CfprFabricEthEstcPcPinGroupName_Type = SnmpAdminString
_CfprFabricEthEstcPcPinGroupName_Object = MibTableColumn
cfprFabricEthEstcPcPinGroupName = _CfprFabricEthEstcPcPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 21),
    _CfprFabricEthEstcPcPinGroupName_Type()
)
cfprFabricEthEstcPcPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcPinGroupName.setStatus("current")
_CfprFabricEthEstcPcPortId_Type = Gauge32
_CfprFabricEthEstcPcPortId_Object = MibTableColumn
cfprFabricEthEstcPcPortId = _CfprFabricEthEstcPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 22),
    _CfprFabricEthEstcPcPortId_Type()
)
cfprFabricEthEstcPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcPortId.setStatus("current")
_CfprFabricEthEstcPcPortMode_Type = CfprFabricEthEstcPortMode
_CfprFabricEthEstcPcPortMode_Object = MibTableColumn
cfprFabricEthEstcPcPortMode = _CfprFabricEthEstcPcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 23),
    _CfprFabricEthEstcPcPortMode_Type()
)
cfprFabricEthEstcPcPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcPortMode.setStatus("current")
_CfprFabricEthEstcPcPrio_Type = CfprQosPriority
_CfprFabricEthEstcPcPrio_Object = MibTableColumn
cfprFabricEthEstcPcPrio = _CfprFabricEthEstcPcPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 24),
    _CfprFabricEthEstcPcPrio_Type()
)
cfprFabricEthEstcPcPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcPrio.setStatus("current")
_CfprFabricEthEstcPcProtocol_Type = CfprFabricEthPcProtocol
_CfprFabricEthEstcPcProtocol_Object = MibTableColumn
cfprFabricEthEstcPcProtocol = _CfprFabricEthEstcPcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 25),
    _CfprFabricEthEstcPcProtocol_Type()
)
cfprFabricEthEstcPcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcProtocol.setStatus("current")
_CfprFabricEthEstcPcStateQual_Type = SnmpAdminString
_CfprFabricEthEstcPcStateQual_Object = MibTableColumn
cfprFabricEthEstcPcStateQual = _CfprFabricEthEstcPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 26),
    _CfprFabricEthEstcPcStateQual_Type()
)
cfprFabricEthEstcPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcStateQual.setStatus("current")
_CfprFabricEthEstcPcSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthEstcPcSwitchId_Object = MibTableColumn
cfprFabricEthEstcPcSwitchId = _CfprFabricEthEstcPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 27),
    _CfprFabricEthEstcPcSwitchId_Type()
)
cfprFabricEthEstcPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcSwitchId.setStatus("current")
_CfprFabricEthEstcPcTransport_Type = CfprFabricEthEstcPcTransport
_CfprFabricEthEstcPcTransport_Object = MibTableColumn
cfprFabricEthEstcPcTransport = _CfprFabricEthEstcPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 28),
    _CfprFabricEthEstcPcTransport_Type()
)
cfprFabricEthEstcPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcTransport.setStatus("current")
_CfprFabricEthEstcPcType_Type = CfprFabricEstcPcType
_CfprFabricEthEstcPcType_Object = MibTableColumn
cfprFabricEthEstcPcType = _CfprFabricEthEstcPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 29),
    _CfprFabricEthEstcPcType_Type()
)
cfprFabricEthEstcPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcType.setStatus("current")
_CfprFabricEthEstcPcWarnings_Type = CfprFabricWarnings
_CfprFabricEthEstcPcWarnings_Object = MibTableColumn
cfprFabricEthEstcPcWarnings = _CfprFabricEthEstcPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 26, 1, 30),
    _CfprFabricEthEstcPcWarnings_Type()
)
cfprFabricEthEstcPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcWarnings.setStatus("current")
_CfprFabricEthEstcPcEpTable_Object = MibTable
cfprFabricEthEstcPcEpTable = _CfprFabricEthEstcPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27)
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpTable.setStatus("current")
_CfprFabricEthEstcPcEpEntry_Object = MibTableRow
cfprFabricEthEstcPcEpEntry = _CfprFabricEthEstcPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1)
)
cfprFabricEthEstcPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthEstcPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpEntry.setStatus("current")
_CfprFabricEthEstcPcEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthEstcPcEpInstanceId_Object = MibTableColumn
cfprFabricEthEstcPcEpInstanceId = _CfprFabricEthEstcPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 1),
    _CfprFabricEthEstcPcEpInstanceId_Type()
)
cfprFabricEthEstcPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpInstanceId.setStatus("current")
_CfprFabricEthEstcPcEpDnData_Type = CfprManagedObjectDn
_CfprFabricEthEstcPcEpDnData_Object = MibTableColumn
cfprFabricEthEstcPcEpDnData = _CfprFabricEthEstcPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 2),
    _CfprFabricEthEstcPcEpDnData_Type()
)
cfprFabricEthEstcPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpDnData.setStatus("current")
_CfprFabricEthEstcPcEpRn_Type = SnmpAdminString
_CfprFabricEthEstcPcEpRn_Object = MibTableColumn
cfprFabricEthEstcPcEpRn = _CfprFabricEthEstcPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 3),
    _CfprFabricEthEstcPcEpRn_Type()
)
cfprFabricEthEstcPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpRn.setStatus("current")
_CfprFabricEthEstcPcEpAdminSpeed_Type = CfprPortSpeed
_CfprFabricEthEstcPcEpAdminSpeed_Object = MibTableColumn
cfprFabricEthEstcPcEpAdminSpeed = _CfprFabricEthEstcPcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 4),
    _CfprFabricEthEstcPcEpAdminSpeed_Type()
)
cfprFabricEthEstcPcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpAdminSpeed.setStatus("current")
_CfprFabricEthEstcPcEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricEthEstcPcEpAdminState_Object = MibTableColumn
cfprFabricEthEstcPcEpAdminState = _CfprFabricEthEstcPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 5),
    _CfprFabricEthEstcPcEpAdminState_Type()
)
cfprFabricEthEstcPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpAdminState.setStatus("current")
_CfprFabricEthEstcPcEpAggrPortId_Type = Gauge32
_CfprFabricEthEstcPcEpAggrPortId_Object = MibTableColumn
cfprFabricEthEstcPcEpAggrPortId = _CfprFabricEthEstcPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 6),
    _CfprFabricEthEstcPcEpAggrPortId_Type()
)
cfprFabricEthEstcPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpAggrPortId.setStatus("current")
_CfprFabricEthEstcPcEpChassisId_Type = Gauge32
_CfprFabricEthEstcPcEpChassisId_Object = MibTableColumn
cfprFabricEthEstcPcEpChassisId = _CfprFabricEthEstcPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 7),
    _CfprFabricEthEstcPcEpChassisId_Type()
)
cfprFabricEthEstcPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpChassisId.setStatus("current")
_CfprFabricEthEstcPcEpConfigState_Type = CfprFabricConfigState
_CfprFabricEthEstcPcEpConfigState_Object = MibTableColumn
cfprFabricEthEstcPcEpConfigState = _CfprFabricEthEstcPcEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 8),
    _CfprFabricEthEstcPcEpConfigState_Type()
)
cfprFabricEthEstcPcEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpConfigState.setStatus("current")
_CfprFabricEthEstcPcEpEpDn_Type = SnmpAdminString
_CfprFabricEthEstcPcEpEpDn_Object = MibTableColumn
cfprFabricEthEstcPcEpEpDn = _CfprFabricEthEstcPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 9),
    _CfprFabricEthEstcPcEpEpDn_Type()
)
cfprFabricEthEstcPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpEpDn.setStatus("current")
_CfprFabricEthEstcPcEpFltAggr_Type = Unsigned64
_CfprFabricEthEstcPcEpFltAggr_Object = MibTableColumn
cfprFabricEthEstcPcEpFltAggr = _CfprFabricEthEstcPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 10),
    _CfprFabricEthEstcPcEpFltAggr_Type()
)
cfprFabricEthEstcPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpFltAggr.setStatus("current")
_CfprFabricEthEstcPcEpIfRole_Type = CfprFabricAEthEstcEpIfRole
_CfprFabricEthEstcPcEpIfRole_Object = MibTableColumn
cfprFabricEthEstcPcEpIfRole = _CfprFabricEthEstcPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 11),
    _CfprFabricEthEstcPcEpIfRole_Type()
)
cfprFabricEthEstcPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpIfRole.setStatus("current")
_CfprFabricEthEstcPcEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricEthEstcPcEpIfType_Object = MibTableColumn
cfprFabricEthEstcPcEpIfType = _CfprFabricEthEstcPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 12),
    _CfprFabricEthEstcPcEpIfType_Type()
)
cfprFabricEthEstcPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpIfType.setStatus("current")
_CfprFabricEthEstcPcEpLicGP_Type = Unsigned64
_CfprFabricEthEstcPcEpLicGP_Object = MibTableColumn
cfprFabricEthEstcPcEpLicGP = _CfprFabricEthEstcPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 13),
    _CfprFabricEthEstcPcEpLicGP_Type()
)
cfprFabricEthEstcPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpLicGP.setStatus("current")
_CfprFabricEthEstcPcEpLicState_Type = CfprLicenseState
_CfprFabricEthEstcPcEpLicState_Object = MibTableColumn
cfprFabricEthEstcPcEpLicState = _CfprFabricEthEstcPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 14),
    _CfprFabricEthEstcPcEpLicState_Type()
)
cfprFabricEthEstcPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpLicState.setStatus("current")
_CfprFabricEthEstcPcEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricEthEstcPcEpLocale_Object = MibTableColumn
cfprFabricEthEstcPcEpLocale = _CfprFabricEthEstcPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 15),
    _CfprFabricEthEstcPcEpLocale_Type()
)
cfprFabricEthEstcPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpLocale.setStatus("current")
_CfprFabricEthEstcPcEpMembership_Type = CfprFabricMembershipStatus
_CfprFabricEthEstcPcEpMembership_Object = MibTableColumn
cfprFabricEthEstcPcEpMembership = _CfprFabricEthEstcPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 16),
    _CfprFabricEthEstcPcEpMembership_Type()
)
cfprFabricEthEstcPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpMembership.setStatus("current")
_CfprFabricEthEstcPcEpName_Type = SnmpAdminString
_CfprFabricEthEstcPcEpName_Object = MibTableColumn
cfprFabricEthEstcPcEpName = _CfprFabricEthEstcPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 17),
    _CfprFabricEthEstcPcEpName_Type()
)
cfprFabricEthEstcPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpName.setStatus("current")
_CfprFabricEthEstcPcEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricEthEstcPcEpOperState_Object = MibTableColumn
cfprFabricEthEstcPcEpOperState = _CfprFabricEthEstcPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 18),
    _CfprFabricEthEstcPcEpOperState_Type()
)
cfprFabricEthEstcPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpOperState.setStatus("current")
_CfprFabricEthEstcPcEpOperStateReason_Type = SnmpAdminString
_CfprFabricEthEstcPcEpOperStateReason_Object = MibTableColumn
cfprFabricEthEstcPcEpOperStateReason = _CfprFabricEthEstcPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 19),
    _CfprFabricEthEstcPcEpOperStateReason_Type()
)
cfprFabricEthEstcPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpOperStateReason.setStatus("current")
_CfprFabricEthEstcPcEpPeerAggrPortId_Type = Gauge32
_CfprFabricEthEstcPcEpPeerAggrPortId_Object = MibTableColumn
cfprFabricEthEstcPcEpPeerAggrPortId = _CfprFabricEthEstcPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 20),
    _CfprFabricEthEstcPcEpPeerAggrPortId_Type()
)
cfprFabricEthEstcPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpPeerAggrPortId.setStatus("current")
_CfprFabricEthEstcPcEpPeerChassisId_Type = Gauge32
_CfprFabricEthEstcPcEpPeerChassisId_Object = MibTableColumn
cfprFabricEthEstcPcEpPeerChassisId = _CfprFabricEthEstcPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 21),
    _CfprFabricEthEstcPcEpPeerChassisId_Type()
)
cfprFabricEthEstcPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpPeerChassisId.setStatus("current")
_CfprFabricEthEstcPcEpPeerDn_Type = SnmpAdminString
_CfprFabricEthEstcPcEpPeerDn_Object = MibTableColumn
cfprFabricEthEstcPcEpPeerDn = _CfprFabricEthEstcPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 22),
    _CfprFabricEthEstcPcEpPeerDn_Type()
)
cfprFabricEthEstcPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpPeerDn.setStatus("current")
_CfprFabricEthEstcPcEpPeerPortId_Type = Gauge32
_CfprFabricEthEstcPcEpPeerPortId_Object = MibTableColumn
cfprFabricEthEstcPcEpPeerPortId = _CfprFabricEthEstcPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 23),
    _CfprFabricEthEstcPcEpPeerPortId_Type()
)
cfprFabricEthEstcPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpPeerPortId.setStatus("current")
_CfprFabricEthEstcPcEpPeerSlotId_Type = Gauge32
_CfprFabricEthEstcPcEpPeerSlotId_Object = MibTableColumn
cfprFabricEthEstcPcEpPeerSlotId = _CfprFabricEthEstcPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 24),
    _CfprFabricEthEstcPcEpPeerSlotId_Type()
)
cfprFabricEthEstcPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpPeerSlotId.setStatus("current")
_CfprFabricEthEstcPcEpPortId_Type = CfprFabricEthEstcPcEpPortId
_CfprFabricEthEstcPcEpPortId_Object = MibTableColumn
cfprFabricEthEstcPcEpPortId = _CfprFabricEthEstcPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 25),
    _CfprFabricEthEstcPcEpPortId_Type()
)
cfprFabricEthEstcPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpPortId.setStatus("current")
_CfprFabricEthEstcPcEpSlotId_Type = CfprFabricEthEstcPcEpSlotId
_CfprFabricEthEstcPcEpSlotId_Object = MibTableColumn
cfprFabricEthEstcPcEpSlotId = _CfprFabricEthEstcPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 26),
    _CfprFabricEthEstcPcEpSlotId_Type()
)
cfprFabricEthEstcPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpSlotId.setStatus("current")
_CfprFabricEthEstcPcEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthEstcPcEpSwitchId_Object = MibTableColumn
cfprFabricEthEstcPcEpSwitchId = _CfprFabricEthEstcPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 27),
    _CfprFabricEthEstcPcEpSwitchId_Type()
)
cfprFabricEthEstcPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpSwitchId.setStatus("current")
_CfprFabricEthEstcPcEpTransport_Type = CfprFabricAEthEstcEpTransport
_CfprFabricEthEstcPcEpTransport_Object = MibTableColumn
cfprFabricEthEstcPcEpTransport = _CfprFabricEthEstcPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 28),
    _CfprFabricEthEstcPcEpTransport_Type()
)
cfprFabricEthEstcPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpTransport.setStatus("current")
_CfprFabricEthEstcPcEpType_Type = CfprFabricAEthEstcEpType
_CfprFabricEthEstcPcEpType_Object = MibTableColumn
cfprFabricEthEstcPcEpType = _CfprFabricEthEstcPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 29),
    _CfprFabricEthEstcPcEpType_Type()
)
cfprFabricEthEstcPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpType.setStatus("current")
_CfprFabricEthEstcPcEpUsrLbl_Type = SnmpAdminString
_CfprFabricEthEstcPcEpUsrLbl_Object = MibTableColumn
cfprFabricEthEstcPcEpUsrLbl = _CfprFabricEthEstcPcEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 30),
    _CfprFabricEthEstcPcEpUsrLbl_Type()
)
cfprFabricEthEstcPcEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpUsrLbl.setStatus("current")
_CfprFabricEthEstcPcEpWarnings_Type = CfprFabricWarnings
_CfprFabricEthEstcPcEpWarnings_Object = MibTableColumn
cfprFabricEthEstcPcEpWarnings = _CfprFabricEthEstcPcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 27, 1, 31),
    _CfprFabricEthEstcPcEpWarnings_Type()
)
cfprFabricEthEstcPcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthEstcPcEpWarnings.setStatus("current")
_CfprFabricEthLanTable_Object = MibTable
cfprFabricEthLanTable = _CfprFabricEthLanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29)
)
if mibBuilder.loadTexts:
    cfprFabricEthLanTable.setStatus("current")
_CfprFabricEthLanEntry_Object = MibTableRow
cfprFabricEthLanEntry = _CfprFabricEthLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1)
)
cfprFabricEthLanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthLanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthLanEntry.setStatus("current")
_CfprFabricEthLanInstanceId_Type = CfprManagedObjectId
_CfprFabricEthLanInstanceId_Object = MibTableColumn
cfprFabricEthLanInstanceId = _CfprFabricEthLanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1, 1),
    _CfprFabricEthLanInstanceId_Type()
)
cfprFabricEthLanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthLanInstanceId.setStatus("current")
_CfprFabricEthLanDn_Type = CfprManagedObjectDn
_CfprFabricEthLanDn_Object = MibTableColumn
cfprFabricEthLanDn = _CfprFabricEthLanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1, 2),
    _CfprFabricEthLanDn_Type()
)
cfprFabricEthLanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanDn.setStatus("current")
_CfprFabricEthLanRn_Type = SnmpAdminString
_CfprFabricEthLanRn_Object = MibTableColumn
cfprFabricEthLanRn = _CfprFabricEthLanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1, 3),
    _CfprFabricEthLanRn_Type()
)
cfprFabricEthLanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanRn.setStatus("current")
_CfprFabricEthLanId_Type = CfprNetworkSwitchId
_CfprFabricEthLanId_Object = MibTableColumn
cfprFabricEthLanId = _CfprFabricEthLanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1, 4),
    _CfprFabricEthLanId_Type()
)
cfprFabricEthLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanId.setStatus("current")
_CfprFabricEthLanLocale_Type = CfprFabricExternalLocale
_CfprFabricEthLanLocale_Object = MibTableColumn
cfprFabricEthLanLocale = _CfprFabricEthLanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1, 5),
    _CfprFabricEthLanLocale_Type()
)
cfprFabricEthLanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanLocale.setStatus("current")
_CfprFabricEthLanName_Type = SnmpAdminString
_CfprFabricEthLanName_Object = MibTableColumn
cfprFabricEthLanName = _CfprFabricEthLanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1, 6),
    _CfprFabricEthLanName_Type()
)
cfprFabricEthLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanName.setStatus("current")
_CfprFabricEthLanTransport_Type = CfprFabricEthLanTransport
_CfprFabricEthLanTransport_Object = MibTableColumn
cfprFabricEthLanTransport = _CfprFabricEthLanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1, 7),
    _CfprFabricEthLanTransport_Type()
)
cfprFabricEthLanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanTransport.setStatus("current")
_CfprFabricEthLanType_Type = CfprFabricLanType
_CfprFabricEthLanType_Object = MibTableColumn
cfprFabricEthLanType = _CfprFabricEthLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 29, 1, 8),
    _CfprFabricEthLanType_Type()
)
cfprFabricEthLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanType.setStatus("current")
_CfprFabricEthLanEpTable_Object = MibTable
cfprFabricEthLanEpTable = _CfprFabricEthLanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30)
)
if mibBuilder.loadTexts:
    cfprFabricEthLanEpTable.setStatus("current")
_CfprFabricEthLanEpEntry_Object = MibTableRow
cfprFabricEthLanEpEntry = _CfprFabricEthLanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1)
)
cfprFabricEthLanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthLanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthLanEpEntry.setStatus("current")
_CfprFabricEthLanEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthLanEpInstanceId_Object = MibTableColumn
cfprFabricEthLanEpInstanceId = _CfprFabricEthLanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 1),
    _CfprFabricEthLanEpInstanceId_Type()
)
cfprFabricEthLanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpInstanceId.setStatus("current")
_CfprFabricEthLanEpDn_Type = CfprManagedObjectDn
_CfprFabricEthLanEpDn_Object = MibTableColumn
cfprFabricEthLanEpDn = _CfprFabricEthLanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 2),
    _CfprFabricEthLanEpDn_Type()
)
cfprFabricEthLanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpDn.setStatus("current")
_CfprFabricEthLanEpRn_Type = SnmpAdminString
_CfprFabricEthLanEpRn_Object = MibTableColumn
cfprFabricEthLanEpRn = _CfprFabricEthLanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 3),
    _CfprFabricEthLanEpRn_Type()
)
cfprFabricEthLanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpRn.setStatus("current")
_CfprFabricEthLanEpAdminSpeed_Type = CfprPortEthSpeed
_CfprFabricEthLanEpAdminSpeed_Object = MibTableColumn
cfprFabricEthLanEpAdminSpeed = _CfprFabricEthLanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 4),
    _CfprFabricEthLanEpAdminSpeed_Type()
)
cfprFabricEthLanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpAdminSpeed.setStatus("current")
_CfprFabricEthLanEpAdminState_Type = CfprFabricEthLanEpAdminState
_CfprFabricEthLanEpAdminState_Object = MibTableColumn
cfprFabricEthLanEpAdminState = _CfprFabricEthLanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 5),
    _CfprFabricEthLanEpAdminState_Type()
)
cfprFabricEthLanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpAdminState.setStatus("current")
_CfprFabricEthLanEpAggrPortId_Type = Gauge32
_CfprFabricEthLanEpAggrPortId_Object = MibTableColumn
cfprFabricEthLanEpAggrPortId = _CfprFabricEthLanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 6),
    _CfprFabricEthLanEpAggrPortId_Type()
)
cfprFabricEthLanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpAggrPortId.setStatus("current")
_CfprFabricEthLanEpChassisId_Type = Gauge32
_CfprFabricEthLanEpChassisId_Object = MibTableColumn
cfprFabricEthLanEpChassisId = _CfprFabricEthLanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 7),
    _CfprFabricEthLanEpChassisId_Type()
)
cfprFabricEthLanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpChassisId.setStatus("current")
_CfprFabricEthLanEpDtagVlan_Type = Gauge32
_CfprFabricEthLanEpDtagVlan_Object = MibTableColumn
cfprFabricEthLanEpDtagVlan = _CfprFabricEthLanEpDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 8),
    _CfprFabricEthLanEpDtagVlan_Type()
)
cfprFabricEthLanEpDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpDtagVlan.setStatus("current")
_CfprFabricEthLanEpEpDn_Type = SnmpAdminString
_CfprFabricEthLanEpEpDn_Object = MibTableColumn
cfprFabricEthLanEpEpDn = _CfprFabricEthLanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 9),
    _CfprFabricEthLanEpEpDn_Type()
)
cfprFabricEthLanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpEpDn.setStatus("current")
_CfprFabricEthLanEpEthLinkProfileName_Type = SnmpAdminString
_CfprFabricEthLanEpEthLinkProfileName_Object = MibTableColumn
cfprFabricEthLanEpEthLinkProfileName = _CfprFabricEthLanEpEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 10),
    _CfprFabricEthLanEpEthLinkProfileName_Type()
)
cfprFabricEthLanEpEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpEthLinkProfileName.setStatus("current")
_CfprFabricEthLanEpFlowCtrlPolicy_Type = SnmpAdminString
_CfprFabricEthLanEpFlowCtrlPolicy_Object = MibTableColumn
cfprFabricEthLanEpFlowCtrlPolicy = _CfprFabricEthLanEpFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 11),
    _CfprFabricEthLanEpFlowCtrlPolicy_Type()
)
cfprFabricEthLanEpFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpFlowCtrlPolicy.setStatus("current")
_CfprFabricEthLanEpFltAggr_Type = Unsigned64
_CfprFabricEthLanEpFltAggr_Object = MibTableColumn
cfprFabricEthLanEpFltAggr = _CfprFabricEthLanEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 12),
    _CfprFabricEthLanEpFltAggr_Type()
)
cfprFabricEthLanEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpFltAggr.setStatus("current")
_CfprFabricEthLanEpIfRole_Type = CfprFabricLanEpIfRole
_CfprFabricEthLanEpIfRole_Object = MibTableColumn
cfprFabricEthLanEpIfRole = _CfprFabricEthLanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 13),
    _CfprFabricEthLanEpIfRole_Type()
)
cfprFabricEthLanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpIfRole.setStatus("current")
_CfprFabricEthLanEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricEthLanEpIfType_Object = MibTableColumn
cfprFabricEthLanEpIfType = _CfprFabricEthLanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 14),
    _CfprFabricEthLanEpIfType_Type()
)
cfprFabricEthLanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpIfType.setStatus("current")
_CfprFabricEthLanEpLicGP_Type = Unsigned64
_CfprFabricEthLanEpLicGP_Object = MibTableColumn
cfprFabricEthLanEpLicGP = _CfprFabricEthLanEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 15),
    _CfprFabricEthLanEpLicGP_Type()
)
cfprFabricEthLanEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpLicGP.setStatus("current")
_CfprFabricEthLanEpLicState_Type = CfprLicenseState
_CfprFabricEthLanEpLicState_Object = MibTableColumn
cfprFabricEthLanEpLicState = _CfprFabricEthLanEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 16),
    _CfprFabricEthLanEpLicState_Type()
)
cfprFabricEthLanEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpLicState.setStatus("current")
_CfprFabricEthLanEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricEthLanEpLocale_Object = MibTableColumn
cfprFabricEthLanEpLocale = _CfprFabricEthLanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 17),
    _CfprFabricEthLanEpLocale_Type()
)
cfprFabricEthLanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpLocale.setStatus("current")
_CfprFabricEthLanEpName_Type = SnmpAdminString
_CfprFabricEthLanEpName_Object = MibTableColumn
cfprFabricEthLanEpName = _CfprFabricEthLanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 19),
    _CfprFabricEthLanEpName_Type()
)
cfprFabricEthLanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpName.setStatus("current")
_CfprFabricEthLanEpOperEthLinkProfileName_Type = SnmpAdminString
_CfprFabricEthLanEpOperEthLinkProfileName_Object = MibTableColumn
cfprFabricEthLanEpOperEthLinkProfileName = _CfprFabricEthLanEpOperEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 20),
    _CfprFabricEthLanEpOperEthLinkProfileName_Type()
)
cfprFabricEthLanEpOperEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpOperEthLinkProfileName.setStatus("current")
_CfprFabricEthLanEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricEthLanEpOperState_Object = MibTableColumn
cfprFabricEthLanEpOperState = _CfprFabricEthLanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 21),
    _CfprFabricEthLanEpOperState_Type()
)
cfprFabricEthLanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpOperState.setStatus("current")
_CfprFabricEthLanEpOperStateReason_Type = SnmpAdminString
_CfprFabricEthLanEpOperStateReason_Object = MibTableColumn
cfprFabricEthLanEpOperStateReason = _CfprFabricEthLanEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 22),
    _CfprFabricEthLanEpOperStateReason_Type()
)
cfprFabricEthLanEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpOperStateReason.setStatus("current")
_CfprFabricEthLanEpOverlappingVlans_Type = SnmpAdminString
_CfprFabricEthLanEpOverlappingVlans_Object = MibTableColumn
cfprFabricEthLanEpOverlappingVlans = _CfprFabricEthLanEpOverlappingVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 23),
    _CfprFabricEthLanEpOverlappingVlans_Type()
)
cfprFabricEthLanEpOverlappingVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpOverlappingVlans.setStatus("current")
_CfprFabricEthLanEpPeerAggrPortId_Type = Gauge32
_CfprFabricEthLanEpPeerAggrPortId_Object = MibTableColumn
cfprFabricEthLanEpPeerAggrPortId = _CfprFabricEthLanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 24),
    _CfprFabricEthLanEpPeerAggrPortId_Type()
)
cfprFabricEthLanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpPeerAggrPortId.setStatus("current")
_CfprFabricEthLanEpPeerChassisId_Type = Gauge32
_CfprFabricEthLanEpPeerChassisId_Object = MibTableColumn
cfprFabricEthLanEpPeerChassisId = _CfprFabricEthLanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 25),
    _CfprFabricEthLanEpPeerChassisId_Type()
)
cfprFabricEthLanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpPeerChassisId.setStatus("current")
_CfprFabricEthLanEpPeerDn_Type = SnmpAdminString
_CfprFabricEthLanEpPeerDn_Object = MibTableColumn
cfprFabricEthLanEpPeerDn = _CfprFabricEthLanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 26),
    _CfprFabricEthLanEpPeerDn_Type()
)
cfprFabricEthLanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpPeerDn.setStatus("current")
_CfprFabricEthLanEpPeerPortId_Type = Gauge32
_CfprFabricEthLanEpPeerPortId_Object = MibTableColumn
cfprFabricEthLanEpPeerPortId = _CfprFabricEthLanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 27),
    _CfprFabricEthLanEpPeerPortId_Type()
)
cfprFabricEthLanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpPeerPortId.setStatus("current")
_CfprFabricEthLanEpPeerSlotId_Type = Gauge32
_CfprFabricEthLanEpPeerSlotId_Object = MibTableColumn
cfprFabricEthLanEpPeerSlotId = _CfprFabricEthLanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 28),
    _CfprFabricEthLanEpPeerSlotId_Type()
)
cfprFabricEthLanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpPeerSlotId.setStatus("current")
_CfprFabricEthLanEpPortId_Type = Gauge32
_CfprFabricEthLanEpPortId_Object = MibTableColumn
cfprFabricEthLanEpPortId = _CfprFabricEthLanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 29),
    _CfprFabricEthLanEpPortId_Type()
)
cfprFabricEthLanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpPortId.setStatus("current")
_CfprFabricEthLanEpSlotId_Type = Gauge32
_CfprFabricEthLanEpSlotId_Object = MibTableColumn
cfprFabricEthLanEpSlotId = _CfprFabricEthLanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 30),
    _CfprFabricEthLanEpSlotId_Type()
)
cfprFabricEthLanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpSlotId.setStatus("current")
_CfprFabricEthLanEpSsaPortType_Type = CfprFabricSSAPortType
_CfprFabricEthLanEpSsaPortType_Object = MibTableColumn
cfprFabricEthLanEpSsaPortType = _CfprFabricEthLanEpSsaPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 31),
    _CfprFabricEthLanEpSsaPortType_Type()
)
cfprFabricEthLanEpSsaPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpSsaPortType.setStatus("current")
_CfprFabricEthLanEpSsaVlanId_Type = Gauge32
_CfprFabricEthLanEpSsaVlanId_Object = MibTableColumn
cfprFabricEthLanEpSsaVlanId = _CfprFabricEthLanEpSsaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 32),
    _CfprFabricEthLanEpSsaVlanId_Type()
)
cfprFabricEthLanEpSsaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpSsaVlanId.setStatus("current")
_CfprFabricEthLanEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthLanEpSwitchId_Object = MibTableColumn
cfprFabricEthLanEpSwitchId = _CfprFabricEthLanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 33),
    _CfprFabricEthLanEpSwitchId_Type()
)
cfprFabricEthLanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpSwitchId.setStatus("current")
_CfprFabricEthLanEpTransport_Type = CfprFabricAEthLanEpTransport
_CfprFabricEthLanEpTransport_Object = MibTableColumn
cfprFabricEthLanEpTransport = _CfprFabricEthLanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 34),
    _CfprFabricEthLanEpTransport_Type()
)
cfprFabricEthLanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpTransport.setStatus("current")
_CfprFabricEthLanEpType_Type = CfprFabricLanEpType
_CfprFabricEthLanEpType_Object = MibTableColumn
cfprFabricEthLanEpType = _CfprFabricEthLanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 35),
    _CfprFabricEthLanEpType_Type()
)
cfprFabricEthLanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpType.setStatus("current")
_CfprFabricEthLanEpUdldOperState_Type = CfprFabricUdldOperState
_CfprFabricEthLanEpUdldOperState_Object = MibTableColumn
cfprFabricEthLanEpUdldOperState = _CfprFabricEthLanEpUdldOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 36),
    _CfprFabricEthLanEpUdldOperState_Type()
)
cfprFabricEthLanEpUdldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpUdldOperState.setStatus("current")
_CfprFabricEthLanEpUsrLbl_Type = SnmpAdminString
_CfprFabricEthLanEpUsrLbl_Object = MibTableColumn
cfprFabricEthLanEpUsrLbl = _CfprFabricEthLanEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 37),
    _CfprFabricEthLanEpUsrLbl_Type()
)
cfprFabricEthLanEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpUsrLbl.setStatus("current")
_CfprFabricEthLanEpVlanStatus_Type = CfprFabricEthLanEpVlanStatus
_CfprFabricEthLanEpVlanStatus_Object = MibTableColumn
cfprFabricEthLanEpVlanStatus = _CfprFabricEthLanEpVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 38),
    _CfprFabricEthLanEpVlanStatus_Type()
)
cfprFabricEthLanEpVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpVlanStatus.setStatus("current")
_CfprFabricEthLanEpWarnings_Type = CfprFabricWarnings
_CfprFabricEthLanEpWarnings_Object = MibTableColumn
cfprFabricEthLanEpWarnings = _CfprFabricEthLanEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 39),
    _CfprFabricEthLanEpWarnings_Type()
)
cfprFabricEthLanEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpWarnings.setStatus("current")
_CfprFabricEthLanEpAdminDuplex_Type = CfprPortDuplex
_CfprFabricEthLanEpAdminDuplex_Object = MibTableColumn
cfprFabricEthLanEpAdminDuplex = _CfprFabricEthLanEpAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 40),
    _CfprFabricEthLanEpAdminDuplex_Type()
)
cfprFabricEthLanEpAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpAdminDuplex.setStatus("current")
_CfprFabricEthLanEpAllowSharing_Type = TruthValue
_CfprFabricEthLanEpAllowSharing_Object = MibTableColumn
cfprFabricEthLanEpAllowSharing = _CfprFabricEthLanEpAllowSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 41),
    _CfprFabricEthLanEpAllowSharing_Type()
)
cfprFabricEthLanEpAllowSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpAllowSharing.setStatus("current")
_CfprFabricEthLanEpAllowedVlan_Type = CfprFabricAllowedVlanType
_CfprFabricEthLanEpAllowedVlan_Object = MibTableColumn
cfprFabricEthLanEpAllowedVlan = _CfprFabricEthLanEpAllowedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 42),
    _CfprFabricEthLanEpAllowedVlan_Type()
)
cfprFabricEthLanEpAllowedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpAllowedVlan.setStatus("current")
_CfprFabricEthLanEpAutoNeg_Type = TruthValue
_CfprFabricEthLanEpAutoNeg_Object = MibTableColumn
cfprFabricEthLanEpAutoNeg = _CfprFabricEthLanEpAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 43),
    _CfprFabricEthLanEpAutoNeg_Type()
)
cfprFabricEthLanEpAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpAutoNeg.setStatus("current")
_CfprFabricEthLanEpDescr_Type = SnmpAdminString
_CfprFabricEthLanEpDescr_Object = MibTableColumn
cfprFabricEthLanEpDescr = _CfprFabricEthLanEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 44),
    _CfprFabricEthLanEpDescr_Type()
)
cfprFabricEthLanEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpDescr.setStatus("current")
_CfprFabricEthLanEpHashAlg_Type = CfprNhTpHashType
_CfprFabricEthLanEpHashAlg_Object = MibTableColumn
cfprFabricEthLanEpHashAlg = _CfprFabricEthLanEpHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 45),
    _CfprFabricEthLanEpHashAlg_Type()
)
cfprFabricEthLanEpHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpHashAlg.setStatus("current")
_CfprFabricEthLanEpInlinePeerDn_Type = SnmpAdminString
_CfprFabricEthLanEpInlinePeerDn_Object = MibTableColumn
cfprFabricEthLanEpInlinePeerDn = _CfprFabricEthLanEpInlinePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 46),
    _CfprFabricEthLanEpInlinePeerDn_Type()
)
cfprFabricEthLanEpInlinePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpInlinePeerDn.setStatus("current")
_CfprFabricEthLanEpInlinePeerName_Type = SnmpAdminString
_CfprFabricEthLanEpInlinePeerName_Object = MibTableColumn
cfprFabricEthLanEpInlinePeerName = _CfprFabricEthLanEpInlinePeerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 47),
    _CfprFabricEthLanEpInlinePeerName_Type()
)
cfprFabricEthLanEpInlinePeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpInlinePeerName.setStatus("current")
_CfprFabricEthLanEpInlineState_Type = CfprFabricEthLanEpInlineState
_CfprFabricEthLanEpInlineState_Object = MibTableColumn
cfprFabricEthLanEpInlineState = _CfprFabricEthLanEpInlineState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 48),
    _CfprFabricEthLanEpInlineState_Type()
)
cfprFabricEthLanEpInlineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpInlineState.setStatus("current")
_CfprFabricEthLanEpQosPrio_Type = CfprFabricQosPrio
_CfprFabricEthLanEpQosPrio_Object = MibTableColumn
cfprFabricEthLanEpQosPrio = _CfprFabricEthLanEpQosPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 49),
    _CfprFabricEthLanEpQosPrio_Type()
)
cfprFabricEthLanEpQosPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpQosPrio.setStatus("current")
_CfprFabricEthLanEpSpeedCap_Type = CfprEquipmentEthPortSpeedCap
_CfprFabricEthLanEpSpeedCap_Object = MibTableColumn
cfprFabricEthLanEpSpeedCap = _CfprFabricEthLanEpSpeedCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 50),
    _CfprFabricEthLanEpSpeedCap_Type()
)
cfprFabricEthLanEpSpeedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpSpeedCap.setStatus("current")
_CfprFabricEthLanEpNwCtrlPolicyName_Type = SnmpAdminString
_CfprFabricEthLanEpNwCtrlPolicyName_Object = MibTableColumn
cfprFabricEthLanEpNwCtrlPolicyName = _CfprFabricEthLanEpNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 51),
    _CfprFabricEthLanEpNwCtrlPolicyName_Type()
)
cfprFabricEthLanEpNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpNwCtrlPolicyName.setStatus("current")
_CfprFabricEthLanEpOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprFabricEthLanEpOperNwCtrlPolicyName_Object = MibTableColumn
cfprFabricEthLanEpOperNwCtrlPolicyName = _CfprFabricEthLanEpOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 52),
    _CfprFabricEthLanEpOperNwCtrlPolicyName_Type()
)
cfprFabricEthLanEpOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpOperNwCtrlPolicyName.setStatus("current")
_CfprFabricEthLanEpAllowAneg_Type = TruthValue
_CfprFabricEthLanEpAllowAneg_Object = MibTableColumn
cfprFabricEthLanEpAllowAneg = _CfprFabricEthLanEpAllowAneg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 53),
    _CfprFabricEthLanEpAllowAneg_Type()
)
cfprFabricEthLanEpAllowAneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpAllowAneg.setStatus("current")
_CfprFabricEthLanEpDebounceTime_Type = Gauge32
_CfprFabricEthLanEpDebounceTime_Object = MibTableColumn
cfprFabricEthLanEpDebounceTime = _CfprFabricEthLanEpDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 54),
    _CfprFabricEthLanEpDebounceTime_Type()
)
cfprFabricEthLanEpDebounceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpDebounceTime.setStatus("current")
_CfprFabricEthLanEpLastSvcStateDownReason_Type = CfprFabricSvcStateDownReason
_CfprFabricEthLanEpLastSvcStateDownReason_Object = MibTableColumn
cfprFabricEthLanEpLastSvcStateDownReason = _CfprFabricEthLanEpLastSvcStateDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 55),
    _CfprFabricEthLanEpLastSvcStateDownReason_Type()
)
cfprFabricEthLanEpLastSvcStateDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpLastSvcStateDownReason.setStatus("current")
_CfprFabricEthLanEpServiceState_Type = CfprFabricEthLanEpServiceState
_CfprFabricEthLanEpServiceState_Object = MibTableColumn
cfprFabricEthLanEpServiceState = _CfprFabricEthLanEpServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 30, 1, 56),
    _CfprFabricEthLanEpServiceState_Type()
)
cfprFabricEthLanEpServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanEpServiceState.setStatus("current")
_CfprFabricEthLanPcTable_Object = MibTable
cfprFabricEthLanPcTable = _CfprFabricEthLanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32)
)
if mibBuilder.loadTexts:
    cfprFabricEthLanPcTable.setStatus("current")
_CfprFabricEthLanPcEntry_Object = MibTableRow
cfprFabricEthLanPcEntry = _CfprFabricEthLanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1)
)
cfprFabricEthLanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthLanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEntry.setStatus("current")
_CfprFabricEthLanPcInstanceId_Type = CfprManagedObjectId
_CfprFabricEthLanPcInstanceId_Object = MibTableColumn
cfprFabricEthLanPcInstanceId = _CfprFabricEthLanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 1),
    _CfprFabricEthLanPcInstanceId_Type()
)
cfprFabricEthLanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcInstanceId.setStatus("current")
_CfprFabricEthLanPcDn_Type = CfprManagedObjectDn
_CfprFabricEthLanPcDn_Object = MibTableColumn
cfprFabricEthLanPcDn = _CfprFabricEthLanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 2),
    _CfprFabricEthLanPcDn_Type()
)
cfprFabricEthLanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcDn.setStatus("current")
_CfprFabricEthLanPcRn_Type = SnmpAdminString
_CfprFabricEthLanPcRn_Object = MibTableColumn
cfprFabricEthLanPcRn = _CfprFabricEthLanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 3),
    _CfprFabricEthLanPcRn_Type()
)
cfprFabricEthLanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcRn.setStatus("current")
_CfprFabricEthLanPcAdminSpeed_Type = CfprPortEthSpeed
_CfprFabricEthLanPcAdminSpeed_Object = MibTableColumn
cfprFabricEthLanPcAdminSpeed = _CfprFabricEthLanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 4),
    _CfprFabricEthLanPcAdminSpeed_Type()
)
cfprFabricEthLanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcAdminSpeed.setStatus("current")
_CfprFabricEthLanPcAdminState_Type = CfprFabricEthLanPcAdminState
_CfprFabricEthLanPcAdminState_Object = MibTableColumn
cfprFabricEthLanPcAdminState = _CfprFabricEthLanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 5),
    _CfprFabricEthLanPcAdminState_Type()
)
cfprFabricEthLanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcAdminState.setStatus("current")
_CfprFabricEthLanPcBandwidth_Type = Gauge32
_CfprFabricEthLanPcBandwidth_Object = MibTableColumn
cfprFabricEthLanPcBandwidth = _CfprFabricEthLanPcBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 6),
    _CfprFabricEthLanPcBandwidth_Type()
)
cfprFabricEthLanPcBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcBandwidth.setStatus("current")
_CfprFabricEthLanPcClusterName_Type = SnmpAdminString
_CfprFabricEthLanPcClusterName_Object = MibTableColumn
cfprFabricEthLanPcClusterName = _CfprFabricEthLanPcClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 7),
    _CfprFabricEthLanPcClusterName_Type()
)
cfprFabricEthLanPcClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcClusterName.setStatus("current")
_CfprFabricEthLanPcDescr_Type = SnmpAdminString
_CfprFabricEthLanPcDescr_Object = MibTableColumn
cfprFabricEthLanPcDescr = _CfprFabricEthLanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 8),
    _CfprFabricEthLanPcDescr_Type()
)
cfprFabricEthLanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcDescr.setStatus("current")
_CfprFabricEthLanPcDtagVlan_Type = Gauge32
_CfprFabricEthLanPcDtagVlan_Object = MibTableColumn
cfprFabricEthLanPcDtagVlan = _CfprFabricEthLanPcDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 9),
    _CfprFabricEthLanPcDtagVlan_Type()
)
cfprFabricEthLanPcDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcDtagVlan.setStatus("current")
_CfprFabricEthLanPcEpDn_Type = SnmpAdminString
_CfprFabricEthLanPcEpDn_Object = MibTableColumn
cfprFabricEthLanPcEpDn = _CfprFabricEthLanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 10),
    _CfprFabricEthLanPcEpDn_Type()
)
cfprFabricEthLanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpDn.setStatus("current")
_CfprFabricEthLanPcFlowCtrlPolicy_Type = SnmpAdminString
_CfprFabricEthLanPcFlowCtrlPolicy_Object = MibTableColumn
cfprFabricEthLanPcFlowCtrlPolicy = _CfprFabricEthLanPcFlowCtrlPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 11),
    _CfprFabricEthLanPcFlowCtrlPolicy_Type()
)
cfprFabricEthLanPcFlowCtrlPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcFlowCtrlPolicy.setStatus("current")
_CfprFabricEthLanPcFltAggr_Type = Unsigned64
_CfprFabricEthLanPcFltAggr_Object = MibTableColumn
cfprFabricEthLanPcFltAggr = _CfprFabricEthLanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 12),
    _CfprFabricEthLanPcFltAggr_Type()
)
cfprFabricEthLanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcFltAggr.setStatus("current")
_CfprFabricEthLanPcIfRole_Type = CfprFabricLanPcIfRole
_CfprFabricEthLanPcIfRole_Object = MibTableColumn
cfprFabricEthLanPcIfRole = _CfprFabricEthLanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 13),
    _CfprFabricEthLanPcIfRole_Type()
)
cfprFabricEthLanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcIfRole.setStatus("current")
_CfprFabricEthLanPcIfType_Type = CfprFabricCIoEpIfType
_CfprFabricEthLanPcIfType_Object = MibTableColumn
cfprFabricEthLanPcIfType = _CfprFabricEthLanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 14),
    _CfprFabricEthLanPcIfType_Type()
)
cfprFabricEthLanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcIfType.setStatus("current")
_CfprFabricEthLanPcLacpPolicyName_Type = SnmpAdminString
_CfprFabricEthLanPcLacpPolicyName_Object = MibTableColumn
cfprFabricEthLanPcLacpPolicyName = _CfprFabricEthLanPcLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 15),
    _CfprFabricEthLanPcLacpPolicyName_Type()
)
cfprFabricEthLanPcLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcLacpPolicyName.setStatus("current")
_CfprFabricEthLanPcLocale_Type = CfprFabricExternalPcLocale
_CfprFabricEthLanPcLocale_Object = MibTableColumn
cfprFabricEthLanPcLocale = _CfprFabricEthLanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 16),
    _CfprFabricEthLanPcLocale_Type()
)
cfprFabricEthLanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcLocale.setStatus("current")
_CfprFabricEthLanPcName_Type = SnmpAdminString
_CfprFabricEthLanPcName_Object = MibTableColumn
cfprFabricEthLanPcName = _CfprFabricEthLanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 18),
    _CfprFabricEthLanPcName_Type()
)
cfprFabricEthLanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcName.setStatus("current")
_CfprFabricEthLanPcOperLacpPolicyName_Type = SnmpAdminString
_CfprFabricEthLanPcOperLacpPolicyName_Object = MibTableColumn
cfprFabricEthLanPcOperLacpPolicyName = _CfprFabricEthLanPcOperLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 19),
    _CfprFabricEthLanPcOperLacpPolicyName_Type()
)
cfprFabricEthLanPcOperLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcOperLacpPolicyName.setStatus("current")
_CfprFabricEthLanPcOperSpeed_Type = CfprPortEthSpeed
_CfprFabricEthLanPcOperSpeed_Object = MibTableColumn
cfprFabricEthLanPcOperSpeed = _CfprFabricEthLanPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 20),
    _CfprFabricEthLanPcOperSpeed_Type()
)
cfprFabricEthLanPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcOperSpeed.setStatus("current")
_CfprFabricEthLanPcOperState_Type = CfprNetworkPortOperState
_CfprFabricEthLanPcOperState_Object = MibTableColumn
cfprFabricEthLanPcOperState = _CfprFabricEthLanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 21),
    _CfprFabricEthLanPcOperState_Type()
)
cfprFabricEthLanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcOperState.setStatus("current")
_CfprFabricEthLanPcOverlappingVlans_Type = SnmpAdminString
_CfprFabricEthLanPcOverlappingVlans_Object = MibTableColumn
cfprFabricEthLanPcOverlappingVlans = _CfprFabricEthLanPcOverlappingVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 22),
    _CfprFabricEthLanPcOverlappingVlans_Type()
)
cfprFabricEthLanPcOverlappingVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcOverlappingVlans.setStatus("current")
_CfprFabricEthLanPcPeerDn_Type = SnmpAdminString
_CfprFabricEthLanPcPeerDn_Object = MibTableColumn
cfprFabricEthLanPcPeerDn = _CfprFabricEthLanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 23),
    _CfprFabricEthLanPcPeerDn_Type()
)
cfprFabricEthLanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcPeerDn.setStatus("current")
_CfprFabricEthLanPcPortId_Type = Gauge32
_CfprFabricEthLanPcPortId_Object = MibTableColumn
cfprFabricEthLanPcPortId = _CfprFabricEthLanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 24),
    _CfprFabricEthLanPcPortId_Type()
)
cfprFabricEthLanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcPortId.setStatus("current")
_CfprFabricEthLanPcSpannedCluster_Type = CfprFabricSpannedCluster
_CfprFabricEthLanPcSpannedCluster_Object = MibTableColumn
cfprFabricEthLanPcSpannedCluster = _CfprFabricEthLanPcSpannedCluster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 25),
    _CfprFabricEthLanPcSpannedCluster_Type()
)
cfprFabricEthLanPcSpannedCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcSpannedCluster.setStatus("current")
_CfprFabricEthLanPcSsaPortType_Type = CfprFabricSSAPortType
_CfprFabricEthLanPcSsaPortType_Object = MibTableColumn
cfprFabricEthLanPcSsaPortType = _CfprFabricEthLanPcSsaPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 26),
    _CfprFabricEthLanPcSsaPortType_Type()
)
cfprFabricEthLanPcSsaPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcSsaPortType.setStatus("current")
_CfprFabricEthLanPcSsaVlanId_Type = Gauge32
_CfprFabricEthLanPcSsaVlanId_Object = MibTableColumn
cfprFabricEthLanPcSsaVlanId = _CfprFabricEthLanPcSsaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 27),
    _CfprFabricEthLanPcSsaVlanId_Type()
)
cfprFabricEthLanPcSsaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcSsaVlanId.setStatus("current")
_CfprFabricEthLanPcStateQual_Type = SnmpAdminString
_CfprFabricEthLanPcStateQual_Object = MibTableColumn
cfprFabricEthLanPcStateQual = _CfprFabricEthLanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 28),
    _CfprFabricEthLanPcStateQual_Type()
)
cfprFabricEthLanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcStateQual.setStatus("current")
_CfprFabricEthLanPcSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthLanPcSwitchId_Object = MibTableColumn
cfprFabricEthLanPcSwitchId = _CfprFabricEthLanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 29),
    _CfprFabricEthLanPcSwitchId_Type()
)
cfprFabricEthLanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcSwitchId.setStatus("current")
_CfprFabricEthLanPcTransport_Type = CfprFabricEthLanPcTransport
_CfprFabricEthLanPcTransport_Object = MibTableColumn
cfprFabricEthLanPcTransport = _CfprFabricEthLanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 30),
    _CfprFabricEthLanPcTransport_Type()
)
cfprFabricEthLanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcTransport.setStatus("current")
_CfprFabricEthLanPcType_Type = CfprFabricLanPcType
_CfprFabricEthLanPcType_Object = MibTableColumn
cfprFabricEthLanPcType = _CfprFabricEthLanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 31),
    _CfprFabricEthLanPcType_Type()
)
cfprFabricEthLanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcType.setStatus("current")
_CfprFabricEthLanPcVlanStatus_Type = CfprFabricEthLanPcVlanStatus
_CfprFabricEthLanPcVlanStatus_Object = MibTableColumn
cfprFabricEthLanPcVlanStatus = _CfprFabricEthLanPcVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 32),
    _CfprFabricEthLanPcVlanStatus_Type()
)
cfprFabricEthLanPcVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcVlanStatus.setStatus("current")
_CfprFabricEthLanPcWarnings_Type = CfprFabricWarnings
_CfprFabricEthLanPcWarnings_Object = MibTableColumn
cfprFabricEthLanPcWarnings = _CfprFabricEthLanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 33),
    _CfprFabricEthLanPcWarnings_Type()
)
cfprFabricEthLanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcWarnings.setStatus("current")
_CfprFabricEthLanPcCluChassisId_Type = Gauge32
_CfprFabricEthLanPcCluChassisId_Object = MibTableColumn
cfprFabricEthLanPcCluChassisId = _CfprFabricEthLanPcCluChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 34),
    _CfprFabricEthLanPcCluChassisId_Type()
)
cfprFabricEthLanPcCluChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcCluChassisId.setStatus("current")
_CfprFabricEthLanPcLacpDetach_Type = CfprFabricEthLanPcLacpDetach
_CfprFabricEthLanPcLacpDetach_Object = MibTableColumn
cfprFabricEthLanPcLacpDetach = _CfprFabricEthLanPcLacpDetach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 35),
    _CfprFabricEthLanPcLacpDetach_Type()
)
cfprFabricEthLanPcLacpDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcLacpDetach.setStatus("current")
_CfprFabricEthLanPcAdminDuplex_Type = CfprPortDuplex
_CfprFabricEthLanPcAdminDuplex_Object = MibTableColumn
cfprFabricEthLanPcAdminDuplex = _CfprFabricEthLanPcAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 36),
    _CfprFabricEthLanPcAdminDuplex_Type()
)
cfprFabricEthLanPcAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcAdminDuplex.setStatus("current")
_CfprFabricEthLanPcAllowSharing_Type = TruthValue
_CfprFabricEthLanPcAllowSharing_Object = MibTableColumn
cfprFabricEthLanPcAllowSharing = _CfprFabricEthLanPcAllowSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 37),
    _CfprFabricEthLanPcAllowSharing_Type()
)
cfprFabricEthLanPcAllowSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcAllowSharing.setStatus("current")
_CfprFabricEthLanPcAllowedVlan_Type = CfprFabricAllowedVlanType
_CfprFabricEthLanPcAllowedVlan_Object = MibTableColumn
cfprFabricEthLanPcAllowedVlan = _CfprFabricEthLanPcAllowedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 38),
    _CfprFabricEthLanPcAllowedVlan_Type()
)
cfprFabricEthLanPcAllowedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcAllowedVlan.setStatus("current")
_CfprFabricEthLanPcAutoNeg_Type = TruthValue
_CfprFabricEthLanPcAutoNeg_Object = MibTableColumn
cfprFabricEthLanPcAutoNeg = _CfprFabricEthLanPcAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 39),
    _CfprFabricEthLanPcAutoNeg_Type()
)
cfprFabricEthLanPcAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcAutoNeg.setStatus("current")
_CfprFabricEthLanPcHashAlg_Type = CfprNhTpHashType
_CfprFabricEthLanPcHashAlg_Object = MibTableColumn
cfprFabricEthLanPcHashAlg = _CfprFabricEthLanPcHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 40),
    _CfprFabricEthLanPcHashAlg_Type()
)
cfprFabricEthLanPcHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcHashAlg.setStatus("current")
_CfprFabricEthLanPcInlinePeerDn_Type = SnmpAdminString
_CfprFabricEthLanPcInlinePeerDn_Object = MibTableColumn
cfprFabricEthLanPcInlinePeerDn = _CfprFabricEthLanPcInlinePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 41),
    _CfprFabricEthLanPcInlinePeerDn_Type()
)
cfprFabricEthLanPcInlinePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcInlinePeerDn.setStatus("current")
_CfprFabricEthLanPcInlinePeerName_Type = SnmpAdminString
_CfprFabricEthLanPcInlinePeerName_Object = MibTableColumn
cfprFabricEthLanPcInlinePeerName = _CfprFabricEthLanPcInlinePeerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 42),
    _CfprFabricEthLanPcInlinePeerName_Type()
)
cfprFabricEthLanPcInlinePeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcInlinePeerName.setStatus("current")
_CfprFabricEthLanPcInlineState_Type = CfprFabricEthLanPcInlineState
_CfprFabricEthLanPcInlineState_Object = MibTableColumn
cfprFabricEthLanPcInlineState = _CfprFabricEthLanPcInlineState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 43),
    _CfprFabricEthLanPcInlineState_Type()
)
cfprFabricEthLanPcInlineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcInlineState.setStatus("current")
_CfprFabricEthLanPcLacpMode_Type = CfprFabricLacpMode
_CfprFabricEthLanPcLacpMode_Object = MibTableColumn
cfprFabricEthLanPcLacpMode = _CfprFabricEthLanPcLacpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 44),
    _CfprFabricEthLanPcLacpMode_Type()
)
cfprFabricEthLanPcLacpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcLacpMode.setStatus("current")
_CfprFabricEthLanPcPcMode_Type = CfprFabricPcMode
_CfprFabricEthLanPcPcMode_Object = MibTableColumn
cfprFabricEthLanPcPcMode = _CfprFabricEthLanPcPcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 45),
    _CfprFabricEthLanPcPcMode_Type()
)
cfprFabricEthLanPcPcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcPcMode.setStatus("current")
_CfprFabricEthLanPcPcModeState_Type = CfprFabricPcModeState
_CfprFabricEthLanPcPcModeState_Object = MibTableColumn
cfprFabricEthLanPcPcModeState = _CfprFabricEthLanPcPcModeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 46),
    _CfprFabricEthLanPcPcModeState_Type()
)
cfprFabricEthLanPcPcModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcPcModeState.setStatus("current")
_CfprFabricEthLanPcQosPrio_Type = CfprFabricQosPrio
_CfprFabricEthLanPcQosPrio_Object = MibTableColumn
cfprFabricEthLanPcQosPrio = _CfprFabricEthLanPcQosPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 47),
    _CfprFabricEthLanPcQosPrio_Type()
)
cfprFabricEthLanPcQosPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcQosPrio.setStatus("current")
_CfprFabricEthLanPcSpeedCap_Type = CfprEquipmentEthPortSpeedCap
_CfprFabricEthLanPcSpeedCap_Object = MibTableColumn
cfprFabricEthLanPcSpeedCap = _CfprFabricEthLanPcSpeedCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 48),
    _CfprFabricEthLanPcSpeedCap_Type()
)
cfprFabricEthLanPcSpeedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcSpeedCap.setStatus("current")
_CfprFabricEthLanPcNwCtrlPolicyName_Type = SnmpAdminString
_CfprFabricEthLanPcNwCtrlPolicyName_Object = MibTableColumn
cfprFabricEthLanPcNwCtrlPolicyName = _CfprFabricEthLanPcNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 49),
    _CfprFabricEthLanPcNwCtrlPolicyName_Type()
)
cfprFabricEthLanPcNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcNwCtrlPolicyName.setStatus("current")
_CfprFabricEthLanPcOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprFabricEthLanPcOperNwCtrlPolicyName_Object = MibTableColumn
cfprFabricEthLanPcOperNwCtrlPolicyName = _CfprFabricEthLanPcOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 50),
    _CfprFabricEthLanPcOperNwCtrlPolicyName_Type()
)
cfprFabricEthLanPcOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcOperNwCtrlPolicyName.setStatus("current")
_CfprFabricEthLanPcLastSvcStateDownReason_Type = CfprFabricSvcStateDownReason
_CfprFabricEthLanPcLastSvcStateDownReason_Object = MibTableColumn
cfprFabricEthLanPcLastSvcStateDownReason = _CfprFabricEthLanPcLastSvcStateDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 51),
    _CfprFabricEthLanPcLastSvcStateDownReason_Type()
)
cfprFabricEthLanPcLastSvcStateDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcLastSvcStateDownReason.setStatus("current")
_CfprFabricEthLanPcServiceState_Type = CfprFabricEthLanPcServiceState
_CfprFabricEthLanPcServiceState_Object = MibTableColumn
cfprFabricEthLanPcServiceState = _CfprFabricEthLanPcServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 32, 1, 52),
    _CfprFabricEthLanPcServiceState_Type()
)
cfprFabricEthLanPcServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcServiceState.setStatus("current")
_CfprFabricEthLanPcEpTable_Object = MibTable
cfprFabricEthLanPcEpTable = _CfprFabricEthLanPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33)
)
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpTable.setStatus("current")
_CfprFabricEthLanPcEpEntry_Object = MibTableRow
cfprFabricEthLanPcEpEntry = _CfprFabricEthLanPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1)
)
cfprFabricEthLanPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthLanPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpEntry.setStatus("current")
_CfprFabricEthLanPcEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthLanPcEpInstanceId_Object = MibTableColumn
cfprFabricEthLanPcEpInstanceId = _CfprFabricEthLanPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 1),
    _CfprFabricEthLanPcEpInstanceId_Type()
)
cfprFabricEthLanPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpInstanceId.setStatus("current")
_CfprFabricEthLanPcEpDnData_Type = CfprManagedObjectDn
_CfprFabricEthLanPcEpDnData_Object = MibTableColumn
cfprFabricEthLanPcEpDnData = _CfprFabricEthLanPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 2),
    _CfprFabricEthLanPcEpDnData_Type()
)
cfprFabricEthLanPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpDnData.setStatus("current")
_CfprFabricEthLanPcEpRn_Type = SnmpAdminString
_CfprFabricEthLanPcEpRn_Object = MibTableColumn
cfprFabricEthLanPcEpRn = _CfprFabricEthLanPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 3),
    _CfprFabricEthLanPcEpRn_Type()
)
cfprFabricEthLanPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpRn.setStatus("current")
_CfprFabricEthLanPcEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricEthLanPcEpAdminState_Object = MibTableColumn
cfprFabricEthLanPcEpAdminState = _CfprFabricEthLanPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 4),
    _CfprFabricEthLanPcEpAdminState_Type()
)
cfprFabricEthLanPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpAdminState.setStatus("current")
_CfprFabricEthLanPcEpAggrPortId_Type = Gauge32
_CfprFabricEthLanPcEpAggrPortId_Object = MibTableColumn
cfprFabricEthLanPcEpAggrPortId = _CfprFabricEthLanPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 5),
    _CfprFabricEthLanPcEpAggrPortId_Type()
)
cfprFabricEthLanPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpAggrPortId.setStatus("current")
_CfprFabricEthLanPcEpChassisId_Type = Gauge32
_CfprFabricEthLanPcEpChassisId_Object = MibTableColumn
cfprFabricEthLanPcEpChassisId = _CfprFabricEthLanPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 6),
    _CfprFabricEthLanPcEpChassisId_Type()
)
cfprFabricEthLanPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpChassisId.setStatus("current")
_CfprFabricEthLanPcEpEpDn_Type = SnmpAdminString
_CfprFabricEthLanPcEpEpDn_Object = MibTableColumn
cfprFabricEthLanPcEpEpDn = _CfprFabricEthLanPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 7),
    _CfprFabricEthLanPcEpEpDn_Type()
)
cfprFabricEthLanPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpEpDn.setStatus("current")
_CfprFabricEthLanPcEpEthLinkProfileName_Type = SnmpAdminString
_CfprFabricEthLanPcEpEthLinkProfileName_Object = MibTableColumn
cfprFabricEthLanPcEpEthLinkProfileName = _CfprFabricEthLanPcEpEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 8),
    _CfprFabricEthLanPcEpEthLinkProfileName_Type()
)
cfprFabricEthLanPcEpEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpEthLinkProfileName.setStatus("current")
_CfprFabricEthLanPcEpFltAggr_Type = Unsigned64
_CfprFabricEthLanPcEpFltAggr_Object = MibTableColumn
cfprFabricEthLanPcEpFltAggr = _CfprFabricEthLanPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 9),
    _CfprFabricEthLanPcEpFltAggr_Type()
)
cfprFabricEthLanPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpFltAggr.setStatus("current")
_CfprFabricEthLanPcEpIfRole_Type = CfprFabricLanEpIfRole
_CfprFabricEthLanPcEpIfRole_Object = MibTableColumn
cfprFabricEthLanPcEpIfRole = _CfprFabricEthLanPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 10),
    _CfprFabricEthLanPcEpIfRole_Type()
)
cfprFabricEthLanPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpIfRole.setStatus("current")
_CfprFabricEthLanPcEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricEthLanPcEpIfType_Object = MibTableColumn
cfprFabricEthLanPcEpIfType = _CfprFabricEthLanPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 11),
    _CfprFabricEthLanPcEpIfType_Type()
)
cfprFabricEthLanPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpIfType.setStatus("current")
_CfprFabricEthLanPcEpLicGP_Type = Unsigned64
_CfprFabricEthLanPcEpLicGP_Object = MibTableColumn
cfprFabricEthLanPcEpLicGP = _CfprFabricEthLanPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 12),
    _CfprFabricEthLanPcEpLicGP_Type()
)
cfprFabricEthLanPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpLicGP.setStatus("current")
_CfprFabricEthLanPcEpLicState_Type = CfprLicenseState
_CfprFabricEthLanPcEpLicState_Object = MibTableColumn
cfprFabricEthLanPcEpLicState = _CfprFabricEthLanPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 13),
    _CfprFabricEthLanPcEpLicState_Type()
)
cfprFabricEthLanPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpLicState.setStatus("current")
_CfprFabricEthLanPcEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricEthLanPcEpLocale_Object = MibTableColumn
cfprFabricEthLanPcEpLocale = _CfprFabricEthLanPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 14),
    _CfprFabricEthLanPcEpLocale_Type()
)
cfprFabricEthLanPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpLocale.setStatus("current")
_CfprFabricEthLanPcEpMembership_Type = CfprFabricMembershipStatus
_CfprFabricEthLanPcEpMembership_Object = MibTableColumn
cfprFabricEthLanPcEpMembership = _CfprFabricEthLanPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 15),
    _CfprFabricEthLanPcEpMembership_Type()
)
cfprFabricEthLanPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpMembership.setStatus("current")
_CfprFabricEthLanPcEpName_Type = SnmpAdminString
_CfprFabricEthLanPcEpName_Object = MibTableColumn
cfprFabricEthLanPcEpName = _CfprFabricEthLanPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 16),
    _CfprFabricEthLanPcEpName_Type()
)
cfprFabricEthLanPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpName.setStatus("current")
_CfprFabricEthLanPcEpOperEthLinkProfileName_Type = SnmpAdminString
_CfprFabricEthLanPcEpOperEthLinkProfileName_Object = MibTableColumn
cfprFabricEthLanPcEpOperEthLinkProfileName = _CfprFabricEthLanPcEpOperEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 17),
    _CfprFabricEthLanPcEpOperEthLinkProfileName_Type()
)
cfprFabricEthLanPcEpOperEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpOperEthLinkProfileName.setStatus("current")
_CfprFabricEthLanPcEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricEthLanPcEpOperState_Object = MibTableColumn
cfprFabricEthLanPcEpOperState = _CfprFabricEthLanPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 18),
    _CfprFabricEthLanPcEpOperState_Type()
)
cfprFabricEthLanPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpOperState.setStatus("current")
_CfprFabricEthLanPcEpOperStateReason_Type = SnmpAdminString
_CfprFabricEthLanPcEpOperStateReason_Object = MibTableColumn
cfprFabricEthLanPcEpOperStateReason = _CfprFabricEthLanPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 19),
    _CfprFabricEthLanPcEpOperStateReason_Type()
)
cfprFabricEthLanPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpOperStateReason.setStatus("current")
_CfprFabricEthLanPcEpPeerAggrPortId_Type = Gauge32
_CfprFabricEthLanPcEpPeerAggrPortId_Object = MibTableColumn
cfprFabricEthLanPcEpPeerAggrPortId = _CfprFabricEthLanPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 20),
    _CfprFabricEthLanPcEpPeerAggrPortId_Type()
)
cfprFabricEthLanPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpPeerAggrPortId.setStatus("current")
_CfprFabricEthLanPcEpPeerChassisId_Type = Gauge32
_CfprFabricEthLanPcEpPeerChassisId_Object = MibTableColumn
cfprFabricEthLanPcEpPeerChassisId = _CfprFabricEthLanPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 21),
    _CfprFabricEthLanPcEpPeerChassisId_Type()
)
cfprFabricEthLanPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpPeerChassisId.setStatus("current")
_CfprFabricEthLanPcEpPeerDn_Type = SnmpAdminString
_CfprFabricEthLanPcEpPeerDn_Object = MibTableColumn
cfprFabricEthLanPcEpPeerDn = _CfprFabricEthLanPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 22),
    _CfprFabricEthLanPcEpPeerDn_Type()
)
cfprFabricEthLanPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpPeerDn.setStatus("current")
_CfprFabricEthLanPcEpPeerPortId_Type = Gauge32
_CfprFabricEthLanPcEpPeerPortId_Object = MibTableColumn
cfprFabricEthLanPcEpPeerPortId = _CfprFabricEthLanPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 23),
    _CfprFabricEthLanPcEpPeerPortId_Type()
)
cfprFabricEthLanPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpPeerPortId.setStatus("current")
_CfprFabricEthLanPcEpPeerSlotId_Type = Gauge32
_CfprFabricEthLanPcEpPeerSlotId_Object = MibTableColumn
cfprFabricEthLanPcEpPeerSlotId = _CfprFabricEthLanPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 24),
    _CfprFabricEthLanPcEpPeerSlotId_Type()
)
cfprFabricEthLanPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpPeerSlotId.setStatus("current")
_CfprFabricEthLanPcEpPortId_Type = Gauge32
_CfprFabricEthLanPcEpPortId_Object = MibTableColumn
cfprFabricEthLanPcEpPortId = _CfprFabricEthLanPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 25),
    _CfprFabricEthLanPcEpPortId_Type()
)
cfprFabricEthLanPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpPortId.setStatus("current")
_CfprFabricEthLanPcEpSlotId_Type = Gauge32
_CfprFabricEthLanPcEpSlotId_Object = MibTableColumn
cfprFabricEthLanPcEpSlotId = _CfprFabricEthLanPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 26),
    _CfprFabricEthLanPcEpSlotId_Type()
)
cfprFabricEthLanPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpSlotId.setStatus("current")
_CfprFabricEthLanPcEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthLanPcEpSwitchId_Object = MibTableColumn
cfprFabricEthLanPcEpSwitchId = _CfprFabricEthLanPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 27),
    _CfprFabricEthLanPcEpSwitchId_Type()
)
cfprFabricEthLanPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpSwitchId.setStatus("current")
_CfprFabricEthLanPcEpTransport_Type = CfprFabricAEthLanEpTransport
_CfprFabricEthLanPcEpTransport_Object = MibTableColumn
cfprFabricEthLanPcEpTransport = _CfprFabricEthLanPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 28),
    _CfprFabricEthLanPcEpTransport_Type()
)
cfprFabricEthLanPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpTransport.setStatus("current")
_CfprFabricEthLanPcEpType_Type = CfprFabricLanEpType
_CfprFabricEthLanPcEpType_Object = MibTableColumn
cfprFabricEthLanPcEpType = _CfprFabricEthLanPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 29),
    _CfprFabricEthLanPcEpType_Type()
)
cfprFabricEthLanPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpType.setStatus("current")
_CfprFabricEthLanPcEpUdldOperState_Type = CfprFabricUdldOperState
_CfprFabricEthLanPcEpUdldOperState_Object = MibTableColumn
cfprFabricEthLanPcEpUdldOperState = _CfprFabricEthLanPcEpUdldOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 30),
    _CfprFabricEthLanPcEpUdldOperState_Type()
)
cfprFabricEthLanPcEpUdldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpUdldOperState.setStatus("current")
_CfprFabricEthLanPcEpWarnings_Type = CfprFabricWarnings
_CfprFabricEthLanPcEpWarnings_Object = MibTableColumn
cfprFabricEthLanPcEpWarnings = _CfprFabricEthLanPcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 31),
    _CfprFabricEthLanPcEpWarnings_Type()
)
cfprFabricEthLanPcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpWarnings.setStatus("current")
_CfprFabricEthLanPcEpDescr_Type = SnmpAdminString
_CfprFabricEthLanPcEpDescr_Object = MibTableColumn
cfprFabricEthLanPcEpDescr = _CfprFabricEthLanPcEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 32),
    _CfprFabricEthLanPcEpDescr_Type()
)
cfprFabricEthLanPcEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpDescr.setStatus("current")
_CfprFabricEthLanPcEpSpeedCap_Type = CfprEquipmentEthPortSpeedCap
_CfprFabricEthLanPcEpSpeedCap_Object = MibTableColumn
cfprFabricEthLanPcEpSpeedCap = _CfprFabricEthLanPcEpSpeedCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 33, 1, 33),
    _CfprFabricEthLanPcEpSpeedCap_Type()
)
cfprFabricEthLanPcEpSpeedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLanPcEpSpeedCap.setStatus("current")
_CfprFabricEthLinkProfileTable_Object = MibTable
cfprFabricEthLinkProfileTable = _CfprFabricEthLinkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34)
)
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileTable.setStatus("current")
_CfprFabricEthLinkProfileEntry_Object = MibTableRow
cfprFabricEthLinkProfileEntry = _CfprFabricEthLinkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1)
)
cfprFabricEthLinkProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthLinkProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileEntry.setStatus("current")
_CfprFabricEthLinkProfileInstanceId_Type = CfprManagedObjectId
_CfprFabricEthLinkProfileInstanceId_Object = MibTableColumn
cfprFabricEthLinkProfileInstanceId = _CfprFabricEthLinkProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 1),
    _CfprFabricEthLinkProfileInstanceId_Type()
)
cfprFabricEthLinkProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileInstanceId.setStatus("current")
_CfprFabricEthLinkProfileDn_Type = CfprManagedObjectDn
_CfprFabricEthLinkProfileDn_Object = MibTableColumn
cfprFabricEthLinkProfileDn = _CfprFabricEthLinkProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 2),
    _CfprFabricEthLinkProfileDn_Type()
)
cfprFabricEthLinkProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileDn.setStatus("current")
_CfprFabricEthLinkProfileRn_Type = SnmpAdminString
_CfprFabricEthLinkProfileRn_Object = MibTableColumn
cfprFabricEthLinkProfileRn = _CfprFabricEthLinkProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 3),
    _CfprFabricEthLinkProfileRn_Type()
)
cfprFabricEthLinkProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileRn.setStatus("current")
_CfprFabricEthLinkProfileCdpLinkPolicyName_Type = SnmpAdminString
_CfprFabricEthLinkProfileCdpLinkPolicyName_Object = MibTableColumn
cfprFabricEthLinkProfileCdpLinkPolicyName = _CfprFabricEthLinkProfileCdpLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 4),
    _CfprFabricEthLinkProfileCdpLinkPolicyName_Type()
)
cfprFabricEthLinkProfileCdpLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileCdpLinkPolicyName.setStatus("current")
_CfprFabricEthLinkProfileDescr_Type = SnmpAdminString
_CfprFabricEthLinkProfileDescr_Object = MibTableColumn
cfprFabricEthLinkProfileDescr = _CfprFabricEthLinkProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 5),
    _CfprFabricEthLinkProfileDescr_Type()
)
cfprFabricEthLinkProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileDescr.setStatus("current")
_CfprFabricEthLinkProfileIntId_Type = SnmpAdminString
_CfprFabricEthLinkProfileIntId_Object = MibTableColumn
cfprFabricEthLinkProfileIntId = _CfprFabricEthLinkProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 6),
    _CfprFabricEthLinkProfileIntId_Type()
)
cfprFabricEthLinkProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileIntId.setStatus("current")
_CfprFabricEthLinkProfileName_Type = SnmpAdminString
_CfprFabricEthLinkProfileName_Object = MibTableColumn
cfprFabricEthLinkProfileName = _CfprFabricEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 7),
    _CfprFabricEthLinkProfileName_Type()
)
cfprFabricEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileName.setStatus("current")
_CfprFabricEthLinkProfileOperCdpLinkPolicyName_Type = SnmpAdminString
_CfprFabricEthLinkProfileOperCdpLinkPolicyName_Object = MibTableColumn
cfprFabricEthLinkProfileOperCdpLinkPolicyName = _CfprFabricEthLinkProfileOperCdpLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 8),
    _CfprFabricEthLinkProfileOperCdpLinkPolicyName_Type()
)
cfprFabricEthLinkProfileOperCdpLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileOperCdpLinkPolicyName.setStatus("current")
_CfprFabricEthLinkProfileOperUdldLinkPolicyName_Type = SnmpAdminString
_CfprFabricEthLinkProfileOperUdldLinkPolicyName_Object = MibTableColumn
cfprFabricEthLinkProfileOperUdldLinkPolicyName = _CfprFabricEthLinkProfileOperUdldLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 9),
    _CfprFabricEthLinkProfileOperUdldLinkPolicyName_Type()
)
cfprFabricEthLinkProfileOperUdldLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileOperUdldLinkPolicyName.setStatus("current")
_CfprFabricEthLinkProfilePolicyLevel_Type = Gauge32
_CfprFabricEthLinkProfilePolicyLevel_Object = MibTableColumn
cfprFabricEthLinkProfilePolicyLevel = _CfprFabricEthLinkProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 10),
    _CfprFabricEthLinkProfilePolicyLevel_Type()
)
cfprFabricEthLinkProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfilePolicyLevel.setStatus("current")
_CfprFabricEthLinkProfilePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricEthLinkProfilePolicyOwner_Object = MibTableColumn
cfprFabricEthLinkProfilePolicyOwner = _CfprFabricEthLinkProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 11),
    _CfprFabricEthLinkProfilePolicyOwner_Type()
)
cfprFabricEthLinkProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfilePolicyOwner.setStatus("current")
_CfprFabricEthLinkProfileUdldLinkPolicyName_Type = SnmpAdminString
_CfprFabricEthLinkProfileUdldLinkPolicyName_Object = MibTableColumn
cfprFabricEthLinkProfileUdldLinkPolicyName = _CfprFabricEthLinkProfileUdldLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 34, 1, 12),
    _CfprFabricEthLinkProfileUdldLinkPolicyName_Type()
)
cfprFabricEthLinkProfileUdldLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthLinkProfileUdldLinkPolicyName.setStatus("current")
_CfprFabricEthMonTable_Object = MibTable
cfprFabricEthMonTable = _CfprFabricEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35)
)
if mibBuilder.loadTexts:
    cfprFabricEthMonTable.setStatus("current")
_CfprFabricEthMonEntry_Object = MibTableRow
cfprFabricEthMonEntry = _CfprFabricEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1)
)
cfprFabricEthMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthMonEntry.setStatus("current")
_CfprFabricEthMonInstanceId_Type = CfprManagedObjectId
_CfprFabricEthMonInstanceId_Object = MibTableColumn
cfprFabricEthMonInstanceId = _CfprFabricEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 1),
    _CfprFabricEthMonInstanceId_Type()
)
cfprFabricEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthMonInstanceId.setStatus("current")
_CfprFabricEthMonDn_Type = CfprManagedObjectDn
_CfprFabricEthMonDn_Object = MibTableColumn
cfprFabricEthMonDn = _CfprFabricEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 2),
    _CfprFabricEthMonDn_Type()
)
cfprFabricEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDn.setStatus("current")
_CfprFabricEthMonRn_Type = SnmpAdminString
_CfprFabricEthMonRn_Object = MibTableColumn
cfprFabricEthMonRn = _CfprFabricEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 3),
    _CfprFabricEthMonRn_Type()
)
cfprFabricEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonRn.setStatus("current")
_CfprFabricEthMonAdminState_Type = CfprFabricMonAdminState
_CfprFabricEthMonAdminState_Object = MibTableColumn
cfprFabricEthMonAdminState = _CfprFabricEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 4),
    _CfprFabricEthMonAdminState_Type()
)
cfprFabricEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonAdminState.setStatus("current")
_CfprFabricEthMonConfigFailReason_Type = SnmpAdminString
_CfprFabricEthMonConfigFailReason_Object = MibTableColumn
cfprFabricEthMonConfigFailReason = _CfprFabricEthMonConfigFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 5),
    _CfprFabricEthMonConfigFailReason_Type()
)
cfprFabricEthMonConfigFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonConfigFailReason.setStatus("current")
_CfprFabricEthMonId_Type = CfprNetworkSwitchId
_CfprFabricEthMonId_Object = MibTableColumn
cfprFabricEthMonId = _CfprFabricEthMonId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 6),
    _CfprFabricEthMonId_Type()
)
cfprFabricEthMonId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonId.setStatus("current")
_CfprFabricEthMonIsConfigSuccess_Type = TruthValue
_CfprFabricEthMonIsConfigSuccess_Object = MibTableColumn
cfprFabricEthMonIsConfigSuccess = _CfprFabricEthMonIsConfigSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 7),
    _CfprFabricEthMonIsConfigSuccess_Type()
)
cfprFabricEthMonIsConfigSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonIsConfigSuccess.setStatus("current")
_CfprFabricEthMonLocale_Type = CfprFabricExternalLocale
_CfprFabricEthMonLocale_Object = MibTableColumn
cfprFabricEthMonLocale = _CfprFabricEthMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 8),
    _CfprFabricEthMonLocale_Type()
)
cfprFabricEthMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonLocale.setStatus("current")
_CfprFabricEthMonName_Type = SnmpAdminString
_CfprFabricEthMonName_Object = MibTableColumn
cfprFabricEthMonName = _CfprFabricEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 9),
    _CfprFabricEthMonName_Type()
)
cfprFabricEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonName.setStatus("current")
_CfprFabricEthMonOperState_Type = CfprFabricMonOperState
_CfprFabricEthMonOperState_Object = MibTableColumn
cfprFabricEthMonOperState = _CfprFabricEthMonOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 10),
    _CfprFabricEthMonOperState_Type()
)
cfprFabricEthMonOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonOperState.setStatus("current")
_CfprFabricEthMonOperStateReason_Type = CfprFabricMonOperStateReason
_CfprFabricEthMonOperStateReason_Object = MibTableColumn
cfprFabricEthMonOperStateReason = _CfprFabricEthMonOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 11),
    _CfprFabricEthMonOperStateReason_Type()
)
cfprFabricEthMonOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonOperStateReason.setStatus("current")
_CfprFabricEthMonPeerDn_Type = SnmpAdminString
_CfprFabricEthMonPeerDn_Object = MibTableColumn
cfprFabricEthMonPeerDn = _CfprFabricEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 12),
    _CfprFabricEthMonPeerDn_Type()
)
cfprFabricEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonPeerDn.setStatus("current")
_CfprFabricEthMonSession_Type = Gauge32
_CfprFabricEthMonSession_Object = MibTableColumn
cfprFabricEthMonSession = _CfprFabricEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 13),
    _CfprFabricEthMonSession_Type()
)
cfprFabricEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSession.setStatus("current")
_CfprFabricEthMonTransport_Type = CfprFabricEthMonTransport
_CfprFabricEthMonTransport_Object = MibTableColumn
cfprFabricEthMonTransport = _CfprFabricEthMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 14),
    _CfprFabricEthMonTransport_Type()
)
cfprFabricEthMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonTransport.setStatus("current")
_CfprFabricEthMonType_Type = CfprFabricEthMonType
_CfprFabricEthMonType_Object = MibTableColumn
cfprFabricEthMonType = _CfprFabricEthMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 35, 1, 15),
    _CfprFabricEthMonType_Type()
)
cfprFabricEthMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonType.setStatus("current")
_CfprFabricEthMonDestEpTable_Object = MibTable
cfprFabricEthMonDestEpTable = _CfprFabricEthMonDestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36)
)
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpTable.setStatus("current")
_CfprFabricEthMonDestEpEntry_Object = MibTableRow
cfprFabricEthMonDestEpEntry = _CfprFabricEthMonDestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1)
)
cfprFabricEthMonDestEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthMonDestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpEntry.setStatus("current")
_CfprFabricEthMonDestEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthMonDestEpInstanceId_Object = MibTableColumn
cfprFabricEthMonDestEpInstanceId = _CfprFabricEthMonDestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 1),
    _CfprFabricEthMonDestEpInstanceId_Type()
)
cfprFabricEthMonDestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpInstanceId.setStatus("current")
_CfprFabricEthMonDestEpDn_Type = CfprManagedObjectDn
_CfprFabricEthMonDestEpDn_Object = MibTableColumn
cfprFabricEthMonDestEpDn = _CfprFabricEthMonDestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 2),
    _CfprFabricEthMonDestEpDn_Type()
)
cfprFabricEthMonDestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpDn.setStatus("current")
_CfprFabricEthMonDestEpRn_Type = SnmpAdminString
_CfprFabricEthMonDestEpRn_Object = MibTableColumn
cfprFabricEthMonDestEpRn = _CfprFabricEthMonDestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 3),
    _CfprFabricEthMonDestEpRn_Type()
)
cfprFabricEthMonDestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpRn.setStatus("current")
_CfprFabricEthMonDestEpAdminSpeed_Type = CfprFabricEthMonDestEpAdminSpeed
_CfprFabricEthMonDestEpAdminSpeed_Object = MibTableColumn
cfprFabricEthMonDestEpAdminSpeed = _CfprFabricEthMonDestEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 4),
    _CfprFabricEthMonDestEpAdminSpeed_Type()
)
cfprFabricEthMonDestEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpAdminSpeed.setStatus("current")
_CfprFabricEthMonDestEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricEthMonDestEpAdminState_Object = MibTableColumn
cfprFabricEthMonDestEpAdminState = _CfprFabricEthMonDestEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 5),
    _CfprFabricEthMonDestEpAdminState_Type()
)
cfprFabricEthMonDestEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpAdminState.setStatus("current")
_CfprFabricEthMonDestEpAggrPortId_Type = Gauge32
_CfprFabricEthMonDestEpAggrPortId_Object = MibTableColumn
cfprFabricEthMonDestEpAggrPortId = _CfprFabricEthMonDestEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 6),
    _CfprFabricEthMonDestEpAggrPortId_Type()
)
cfprFabricEthMonDestEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpAggrPortId.setStatus("current")
_CfprFabricEthMonDestEpChassisId_Type = Gauge32
_CfprFabricEthMonDestEpChassisId_Object = MibTableColumn
cfprFabricEthMonDestEpChassisId = _CfprFabricEthMonDestEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 7),
    _CfprFabricEthMonDestEpChassisId_Type()
)
cfprFabricEthMonDestEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpChassisId.setStatus("current")
_CfprFabricEthMonDestEpEpDn_Type = SnmpAdminString
_CfprFabricEthMonDestEpEpDn_Object = MibTableColumn
cfprFabricEthMonDestEpEpDn = _CfprFabricEthMonDestEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 8),
    _CfprFabricEthMonDestEpEpDn_Type()
)
cfprFabricEthMonDestEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpEpDn.setStatus("current")
_CfprFabricEthMonDestEpFltAggr_Type = Unsigned64
_CfprFabricEthMonDestEpFltAggr_Object = MibTableColumn
cfprFabricEthMonDestEpFltAggr = _CfprFabricEthMonDestEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 9),
    _CfprFabricEthMonDestEpFltAggr_Type()
)
cfprFabricEthMonDestEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpFltAggr.setStatus("current")
_CfprFabricEthMonDestEpIfRole_Type = CfprFabricEthMonDestEpIfRole
_CfprFabricEthMonDestEpIfRole_Object = MibTableColumn
cfprFabricEthMonDestEpIfRole = _CfprFabricEthMonDestEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 10),
    _CfprFabricEthMonDestEpIfRole_Type()
)
cfprFabricEthMonDestEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpIfRole.setStatus("current")
_CfprFabricEthMonDestEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricEthMonDestEpIfType_Object = MibTableColumn
cfprFabricEthMonDestEpIfType = _CfprFabricEthMonDestEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 11),
    _CfprFabricEthMonDestEpIfType_Type()
)
cfprFabricEthMonDestEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpIfType.setStatus("current")
_CfprFabricEthMonDestEpLicGP_Type = Unsigned64
_CfprFabricEthMonDestEpLicGP_Object = MibTableColumn
cfprFabricEthMonDestEpLicGP = _CfprFabricEthMonDestEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 12),
    _CfprFabricEthMonDestEpLicGP_Type()
)
cfprFabricEthMonDestEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpLicGP.setStatus("current")
_CfprFabricEthMonDestEpLicState_Type = CfprLicenseState
_CfprFabricEthMonDestEpLicState_Object = MibTableColumn
cfprFabricEthMonDestEpLicState = _CfprFabricEthMonDestEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 13),
    _CfprFabricEthMonDestEpLicState_Type()
)
cfprFabricEthMonDestEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpLicState.setStatus("current")
_CfprFabricEthMonDestEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricEthMonDestEpLocale_Object = MibTableColumn
cfprFabricEthMonDestEpLocale = _CfprFabricEthMonDestEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 14),
    _CfprFabricEthMonDestEpLocale_Type()
)
cfprFabricEthMonDestEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpLocale.setStatus("current")
_CfprFabricEthMonDestEpName_Type = SnmpAdminString
_CfprFabricEthMonDestEpName_Object = MibTableColumn
cfprFabricEthMonDestEpName = _CfprFabricEthMonDestEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 15),
    _CfprFabricEthMonDestEpName_Type()
)
cfprFabricEthMonDestEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpName.setStatus("current")
_CfprFabricEthMonDestEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricEthMonDestEpOperState_Object = MibTableColumn
cfprFabricEthMonDestEpOperState = _CfprFabricEthMonDestEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 16),
    _CfprFabricEthMonDestEpOperState_Type()
)
cfprFabricEthMonDestEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpOperState.setStatus("current")
_CfprFabricEthMonDestEpOperStateReason_Type = SnmpAdminString
_CfprFabricEthMonDestEpOperStateReason_Object = MibTableColumn
cfprFabricEthMonDestEpOperStateReason = _CfprFabricEthMonDestEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 17),
    _CfprFabricEthMonDestEpOperStateReason_Type()
)
cfprFabricEthMonDestEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpOperStateReason.setStatus("current")
_CfprFabricEthMonDestEpPeerAggrPortId_Type = Gauge32
_CfprFabricEthMonDestEpPeerAggrPortId_Object = MibTableColumn
cfprFabricEthMonDestEpPeerAggrPortId = _CfprFabricEthMonDestEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 18),
    _CfprFabricEthMonDestEpPeerAggrPortId_Type()
)
cfprFabricEthMonDestEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpPeerAggrPortId.setStatus("current")
_CfprFabricEthMonDestEpPeerChassisId_Type = Gauge32
_CfprFabricEthMonDestEpPeerChassisId_Object = MibTableColumn
cfprFabricEthMonDestEpPeerChassisId = _CfprFabricEthMonDestEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 19),
    _CfprFabricEthMonDestEpPeerChassisId_Type()
)
cfprFabricEthMonDestEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpPeerChassisId.setStatus("current")
_CfprFabricEthMonDestEpPeerDn_Type = SnmpAdminString
_CfprFabricEthMonDestEpPeerDn_Object = MibTableColumn
cfprFabricEthMonDestEpPeerDn = _CfprFabricEthMonDestEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 20),
    _CfprFabricEthMonDestEpPeerDn_Type()
)
cfprFabricEthMonDestEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpPeerDn.setStatus("current")
_CfprFabricEthMonDestEpPeerPortId_Type = Gauge32
_CfprFabricEthMonDestEpPeerPortId_Object = MibTableColumn
cfprFabricEthMonDestEpPeerPortId = _CfprFabricEthMonDestEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 21),
    _CfprFabricEthMonDestEpPeerPortId_Type()
)
cfprFabricEthMonDestEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpPeerPortId.setStatus("current")
_CfprFabricEthMonDestEpPeerSlotId_Type = Gauge32
_CfprFabricEthMonDestEpPeerSlotId_Object = MibTableColumn
cfprFabricEthMonDestEpPeerSlotId = _CfprFabricEthMonDestEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 22),
    _CfprFabricEthMonDestEpPeerSlotId_Type()
)
cfprFabricEthMonDestEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpPeerSlotId.setStatus("current")
_CfprFabricEthMonDestEpPortId_Type = CfprFabricEthMonDestEpPortId
_CfprFabricEthMonDestEpPortId_Object = MibTableColumn
cfprFabricEthMonDestEpPortId = _CfprFabricEthMonDestEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 23),
    _CfprFabricEthMonDestEpPortId_Type()
)
cfprFabricEthMonDestEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpPortId.setStatus("current")
_CfprFabricEthMonDestEpSlotId_Type = CfprFabricEthMonDestEpSlotId
_CfprFabricEthMonDestEpSlotId_Object = MibTableColumn
cfprFabricEthMonDestEpSlotId = _CfprFabricEthMonDestEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 24),
    _CfprFabricEthMonDestEpSlotId_Type()
)
cfprFabricEthMonDestEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpSlotId.setStatus("current")
_CfprFabricEthMonDestEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthMonDestEpSwitchId_Object = MibTableColumn
cfprFabricEthMonDestEpSwitchId = _CfprFabricEthMonDestEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 25),
    _CfprFabricEthMonDestEpSwitchId_Type()
)
cfprFabricEthMonDestEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpSwitchId.setStatus("current")
_CfprFabricEthMonDestEpTransport_Type = CfprNetworkTransport
_CfprFabricEthMonDestEpTransport_Object = MibTableColumn
cfprFabricEthMonDestEpTransport = _CfprFabricEthMonDestEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 26),
    _CfprFabricEthMonDestEpTransport_Type()
)
cfprFabricEthMonDestEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpTransport.setStatus("current")
_CfprFabricEthMonDestEpType_Type = CfprFabricEthMonDestEpType
_CfprFabricEthMonDestEpType_Object = MibTableColumn
cfprFabricEthMonDestEpType = _CfprFabricEthMonDestEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 27),
    _CfprFabricEthMonDestEpType_Type()
)
cfprFabricEthMonDestEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpType.setStatus("current")
_CfprFabricEthMonDestEpWarnings_Type = CfprFabricWarnings
_CfprFabricEthMonDestEpWarnings_Object = MibTableColumn
cfprFabricEthMonDestEpWarnings = _CfprFabricEthMonDestEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 36, 1, 28),
    _CfprFabricEthMonDestEpWarnings_Type()
)
cfprFabricEthMonDestEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonDestEpWarnings.setStatus("current")
_CfprFabricEthMonFiltEpTable_Object = MibTable
cfprFabricEthMonFiltEpTable = _CfprFabricEthMonFiltEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 37)
)
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltEpTable.setStatus("current")
_CfprFabricEthMonFiltEpEntry_Object = MibTableRow
cfprFabricEthMonFiltEpEntry = _CfprFabricEthMonFiltEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 37, 1)
)
cfprFabricEthMonFiltEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthMonFiltEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltEpEntry.setStatus("current")
_CfprFabricEthMonFiltEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthMonFiltEpInstanceId_Object = MibTableColumn
cfprFabricEthMonFiltEpInstanceId = _CfprFabricEthMonFiltEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 37, 1, 1),
    _CfprFabricEthMonFiltEpInstanceId_Type()
)
cfprFabricEthMonFiltEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltEpInstanceId.setStatus("current")
_CfprFabricEthMonFiltEpDn_Type = CfprManagedObjectDn
_CfprFabricEthMonFiltEpDn_Object = MibTableColumn
cfprFabricEthMonFiltEpDn = _CfprFabricEthMonFiltEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 37, 1, 2),
    _CfprFabricEthMonFiltEpDn_Type()
)
cfprFabricEthMonFiltEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltEpDn.setStatus("current")
_CfprFabricEthMonFiltEpRn_Type = SnmpAdminString
_CfprFabricEthMonFiltEpRn_Object = MibTableColumn
cfprFabricEthMonFiltEpRn = _CfprFabricEthMonFiltEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 37, 1, 3),
    _CfprFabricEthMonFiltEpRn_Type()
)
cfprFabricEthMonFiltEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltEpRn.setStatus("current")
_CfprFabricEthMonFiltEpName_Type = SnmpAdminString
_CfprFabricEthMonFiltEpName_Object = MibTableColumn
cfprFabricEthMonFiltEpName = _CfprFabricEthMonFiltEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 37, 1, 4),
    _CfprFabricEthMonFiltEpName_Type()
)
cfprFabricEthMonFiltEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltEpName.setStatus("current")
_CfprFabricEthMonFiltEpSession_Type = Gauge32
_CfprFabricEthMonFiltEpSession_Object = MibTableColumn
cfprFabricEthMonFiltEpSession = _CfprFabricEthMonFiltEpSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 37, 1, 5),
    _CfprFabricEthMonFiltEpSession_Type()
)
cfprFabricEthMonFiltEpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltEpSession.setStatus("current")
_CfprFabricEthMonFiltEpType_Type = CfprFabricEthMonFiltEpType
_CfprFabricEthMonFiltEpType_Object = MibTableColumn
cfprFabricEthMonFiltEpType = _CfprFabricEthMonFiltEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 37, 1, 6),
    _CfprFabricEthMonFiltEpType_Type()
)
cfprFabricEthMonFiltEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltEpType.setStatus("current")
_CfprFabricEthMonFiltRefTable_Object = MibTable
cfprFabricEthMonFiltRefTable = _CfprFabricEthMonFiltRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 38)
)
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltRefTable.setStatus("current")
_CfprFabricEthMonFiltRefEntry_Object = MibTableRow
cfprFabricEthMonFiltRefEntry = _CfprFabricEthMonFiltRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 38, 1)
)
cfprFabricEthMonFiltRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthMonFiltRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltRefEntry.setStatus("current")
_CfprFabricEthMonFiltRefInstanceId_Type = CfprManagedObjectId
_CfprFabricEthMonFiltRefInstanceId_Object = MibTableColumn
cfprFabricEthMonFiltRefInstanceId = _CfprFabricEthMonFiltRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 38, 1, 1),
    _CfprFabricEthMonFiltRefInstanceId_Type()
)
cfprFabricEthMonFiltRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltRefInstanceId.setStatus("current")
_CfprFabricEthMonFiltRefDn_Type = CfprManagedObjectDn
_CfprFabricEthMonFiltRefDn_Object = MibTableColumn
cfprFabricEthMonFiltRefDn = _CfprFabricEthMonFiltRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 38, 1, 2),
    _CfprFabricEthMonFiltRefDn_Type()
)
cfprFabricEthMonFiltRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltRefDn.setStatus("current")
_CfprFabricEthMonFiltRefRn_Type = SnmpAdminString
_CfprFabricEthMonFiltRefRn_Object = MibTableColumn
cfprFabricEthMonFiltRefRn = _CfprFabricEthMonFiltRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 38, 1, 3),
    _CfprFabricEthMonFiltRefRn_Type()
)
cfprFabricEthMonFiltRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltRefRn.setStatus("current")
_CfprFabricEthMonFiltRefSrcFiltDn_Type = SnmpAdminString
_CfprFabricEthMonFiltRefSrcFiltDn_Object = MibTableColumn
cfprFabricEthMonFiltRefSrcFiltDn = _CfprFabricEthMonFiltRefSrcFiltDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 38, 1, 4),
    _CfprFabricEthMonFiltRefSrcFiltDn_Type()
)
cfprFabricEthMonFiltRefSrcFiltDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltRefSrcFiltDn.setStatus("current")
_CfprFabricEthMonFiltRefType_Type = CfprFabricEthMonFiltRefType
_CfprFabricEthMonFiltRefType_Object = MibTableColumn
cfprFabricEthMonFiltRefType = _CfprFabricEthMonFiltRefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 38, 1, 5),
    _CfprFabricEthMonFiltRefType_Type()
)
cfprFabricEthMonFiltRefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonFiltRefType.setStatus("current")
_CfprFabricEthMonLanTable_Object = MibTable
cfprFabricEthMonLanTable = _CfprFabricEthMonLanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39)
)
if mibBuilder.loadTexts:
    cfprFabricEthMonLanTable.setStatus("current")
_CfprFabricEthMonLanEntry_Object = MibTableRow
cfprFabricEthMonLanEntry = _CfprFabricEthMonLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1)
)
cfprFabricEthMonLanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthMonLanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthMonLanEntry.setStatus("current")
_CfprFabricEthMonLanInstanceId_Type = CfprManagedObjectId
_CfprFabricEthMonLanInstanceId_Object = MibTableColumn
cfprFabricEthMonLanInstanceId = _CfprFabricEthMonLanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1, 1),
    _CfprFabricEthMonLanInstanceId_Type()
)
cfprFabricEthMonLanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthMonLanInstanceId.setStatus("current")
_CfprFabricEthMonLanDn_Type = CfprManagedObjectDn
_CfprFabricEthMonLanDn_Object = MibTableColumn
cfprFabricEthMonLanDn = _CfprFabricEthMonLanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1, 2),
    _CfprFabricEthMonLanDn_Type()
)
cfprFabricEthMonLanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonLanDn.setStatus("current")
_CfprFabricEthMonLanRn_Type = SnmpAdminString
_CfprFabricEthMonLanRn_Object = MibTableColumn
cfprFabricEthMonLanRn = _CfprFabricEthMonLanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1, 3),
    _CfprFabricEthMonLanRn_Type()
)
cfprFabricEthMonLanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonLanRn.setStatus("current")
_CfprFabricEthMonLanId_Type = CfprNetworkSwitchId
_CfprFabricEthMonLanId_Object = MibTableColumn
cfprFabricEthMonLanId = _CfprFabricEthMonLanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1, 4),
    _CfprFabricEthMonLanId_Type()
)
cfprFabricEthMonLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonLanId.setStatus("current")
_CfprFabricEthMonLanLocale_Type = CfprFabricExternalLocale
_CfprFabricEthMonLanLocale_Object = MibTableColumn
cfprFabricEthMonLanLocale = _CfprFabricEthMonLanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1, 5),
    _CfprFabricEthMonLanLocale_Type()
)
cfprFabricEthMonLanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonLanLocale.setStatus("current")
_CfprFabricEthMonLanName_Type = SnmpAdminString
_CfprFabricEthMonLanName_Object = MibTableColumn
cfprFabricEthMonLanName = _CfprFabricEthMonLanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1, 6),
    _CfprFabricEthMonLanName_Type()
)
cfprFabricEthMonLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonLanName.setStatus("current")
_CfprFabricEthMonLanTransport_Type = CfprFabricEthMonLanTransport
_CfprFabricEthMonLanTransport_Object = MibTableColumn
cfprFabricEthMonLanTransport = _CfprFabricEthMonLanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1, 7),
    _CfprFabricEthMonLanTransport_Type()
)
cfprFabricEthMonLanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonLanTransport.setStatus("current")
_CfprFabricEthMonLanType_Type = CfprFabricEthMonLanType
_CfprFabricEthMonLanType_Object = MibTableColumn
cfprFabricEthMonLanType = _CfprFabricEthMonLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 39, 1, 8),
    _CfprFabricEthMonLanType_Type()
)
cfprFabricEthMonLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonLanType.setStatus("current")
_CfprFabricEthMonSrcEpTable_Object = MibTable
cfprFabricEthMonSrcEpTable = _CfprFabricEthMonSrcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40)
)
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpTable.setStatus("current")
_CfprFabricEthMonSrcEpEntry_Object = MibTableRow
cfprFabricEthMonSrcEpEntry = _CfprFabricEthMonSrcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1)
)
cfprFabricEthMonSrcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthMonSrcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpEntry.setStatus("current")
_CfprFabricEthMonSrcEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthMonSrcEpInstanceId_Object = MibTableColumn
cfprFabricEthMonSrcEpInstanceId = _CfprFabricEthMonSrcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1, 1),
    _CfprFabricEthMonSrcEpInstanceId_Type()
)
cfprFabricEthMonSrcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpInstanceId.setStatus("current")
_CfprFabricEthMonSrcEpDn_Type = CfprManagedObjectDn
_CfprFabricEthMonSrcEpDn_Object = MibTableColumn
cfprFabricEthMonSrcEpDn = _CfprFabricEthMonSrcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1, 2),
    _CfprFabricEthMonSrcEpDn_Type()
)
cfprFabricEthMonSrcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpDn.setStatus("current")
_CfprFabricEthMonSrcEpRn_Type = SnmpAdminString
_CfprFabricEthMonSrcEpRn_Object = MibTableColumn
cfprFabricEthMonSrcEpRn = _CfprFabricEthMonSrcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1, 3),
    _CfprFabricEthMonSrcEpRn_Type()
)
cfprFabricEthMonSrcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpRn.setStatus("current")
_CfprFabricEthMonSrcEpDirection_Type = CfprFabricTrafficDirection
_CfprFabricEthMonSrcEpDirection_Object = MibTableColumn
cfprFabricEthMonSrcEpDirection = _CfprFabricEthMonSrcEpDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1, 4),
    _CfprFabricEthMonSrcEpDirection_Type()
)
cfprFabricEthMonSrcEpDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpDirection.setStatus("current")
_CfprFabricEthMonSrcEpName_Type = SnmpAdminString
_CfprFabricEthMonSrcEpName_Object = MibTableColumn
cfprFabricEthMonSrcEpName = _CfprFabricEthMonSrcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1, 5),
    _CfprFabricEthMonSrcEpName_Type()
)
cfprFabricEthMonSrcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpName.setStatus("current")
_CfprFabricEthMonSrcEpSession_Type = Gauge32
_CfprFabricEthMonSrcEpSession_Object = MibTableColumn
cfprFabricEthMonSrcEpSession = _CfprFabricEthMonSrcEpSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1, 6),
    _CfprFabricEthMonSrcEpSession_Type()
)
cfprFabricEthMonSrcEpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpSession.setStatus("current")
_CfprFabricEthMonSrcEpTransport_Type = CfprNetworkTransport
_CfprFabricEthMonSrcEpTransport_Object = MibTableColumn
cfprFabricEthMonSrcEpTransport = _CfprFabricEthMonSrcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1, 7),
    _CfprFabricEthMonSrcEpTransport_Type()
)
cfprFabricEthMonSrcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpTransport.setStatus("current")
_CfprFabricEthMonSrcEpType_Type = CfprFabricEthMonSrcEpType
_CfprFabricEthMonSrcEpType_Object = MibTableColumn
cfprFabricEthMonSrcEpType = _CfprFabricEthMonSrcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 40, 1, 8),
    _CfprFabricEthMonSrcEpType_Type()
)
cfprFabricEthMonSrcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcEpType.setStatus("current")
_CfprFabricEthMonSrcRefTable_Object = MibTable
cfprFabricEthMonSrcRefTable = _CfprFabricEthMonSrcRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41)
)
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefTable.setStatus("current")
_CfprFabricEthMonSrcRefEntry_Object = MibTableRow
cfprFabricEthMonSrcRefEntry = _CfprFabricEthMonSrcRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41, 1)
)
cfprFabricEthMonSrcRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthMonSrcRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefEntry.setStatus("current")
_CfprFabricEthMonSrcRefInstanceId_Type = CfprManagedObjectId
_CfprFabricEthMonSrcRefInstanceId_Object = MibTableColumn
cfprFabricEthMonSrcRefInstanceId = _CfprFabricEthMonSrcRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41, 1, 1),
    _CfprFabricEthMonSrcRefInstanceId_Type()
)
cfprFabricEthMonSrcRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefInstanceId.setStatus("current")
_CfprFabricEthMonSrcRefDn_Type = CfprManagedObjectDn
_CfprFabricEthMonSrcRefDn_Object = MibTableColumn
cfprFabricEthMonSrcRefDn = _CfprFabricEthMonSrcRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41, 1, 2),
    _CfprFabricEthMonSrcRefDn_Type()
)
cfprFabricEthMonSrcRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefDn.setStatus("current")
_CfprFabricEthMonSrcRefRn_Type = SnmpAdminString
_CfprFabricEthMonSrcRefRn_Object = MibTableColumn
cfprFabricEthMonSrcRefRn = _CfprFabricEthMonSrcRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41, 1, 3),
    _CfprFabricEthMonSrcRefRn_Type()
)
cfprFabricEthMonSrcRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefRn.setStatus("current")
_CfprFabricEthMonSrcRefId_Type = Unsigned64
_CfprFabricEthMonSrcRefId_Object = MibTableColumn
cfprFabricEthMonSrcRefId = _CfprFabricEthMonSrcRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41, 1, 4),
    _CfprFabricEthMonSrcRefId_Type()
)
cfprFabricEthMonSrcRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefId.setStatus("current")
_CfprFabricEthMonSrcRefSourceDn_Type = SnmpAdminString
_CfprFabricEthMonSrcRefSourceDn_Object = MibTableColumn
cfprFabricEthMonSrcRefSourceDn = _CfprFabricEthMonSrcRefSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41, 1, 5),
    _CfprFabricEthMonSrcRefSourceDn_Type()
)
cfprFabricEthMonSrcRefSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefSourceDn.setStatus("current")
_CfprFabricEthMonSrcRefSourceType_Type = CfprFabricEthSourceType
_CfprFabricEthMonSrcRefSourceType_Object = MibTableColumn
cfprFabricEthMonSrcRefSourceType = _CfprFabricEthMonSrcRefSourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41, 1, 6),
    _CfprFabricEthMonSrcRefSourceType_Type()
)
cfprFabricEthMonSrcRefSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefSourceType.setStatus("current")
_CfprFabricEthMonSrcRefType_Type = CfprFabricEthMonSrcRefType
_CfprFabricEthMonSrcRefType_Object = MibTableColumn
cfprFabricEthMonSrcRefType = _CfprFabricEthMonSrcRefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 41, 1, 7),
    _CfprFabricEthMonSrcRefType_Type()
)
cfprFabricEthMonSrcRefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthMonSrcRefType.setStatus("current")
_CfprFabricEthTargetEpTable_Object = MibTable
cfprFabricEthTargetEpTable = _CfprFabricEthTargetEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42)
)
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpTable.setStatus("current")
_CfprFabricEthTargetEpEntry_Object = MibTableRow
cfprFabricEthTargetEpEntry = _CfprFabricEthTargetEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1)
)
cfprFabricEthTargetEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthTargetEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpEntry.setStatus("current")
_CfprFabricEthTargetEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthTargetEpInstanceId_Object = MibTableColumn
cfprFabricEthTargetEpInstanceId = _CfprFabricEthTargetEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 1),
    _CfprFabricEthTargetEpInstanceId_Type()
)
cfprFabricEthTargetEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpInstanceId.setStatus("current")
_CfprFabricEthTargetEpDn_Type = CfprManagedObjectDn
_CfprFabricEthTargetEpDn_Object = MibTableColumn
cfprFabricEthTargetEpDn = _CfprFabricEthTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 2),
    _CfprFabricEthTargetEpDn_Type()
)
cfprFabricEthTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpDn.setStatus("current")
_CfprFabricEthTargetEpRn_Type = SnmpAdminString
_CfprFabricEthTargetEpRn_Object = MibTableColumn
cfprFabricEthTargetEpRn = _CfprFabricEthTargetEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 3),
    _CfprFabricEthTargetEpRn_Type()
)
cfprFabricEthTargetEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpRn.setStatus("current")
_CfprFabricEthTargetEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricEthTargetEpAdminState_Object = MibTableColumn
cfprFabricEthTargetEpAdminState = _CfprFabricEthTargetEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 4),
    _CfprFabricEthTargetEpAdminState_Type()
)
cfprFabricEthTargetEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpAdminState.setStatus("current")
_CfprFabricEthTargetEpAggrPortId_Type = Gauge32
_CfprFabricEthTargetEpAggrPortId_Object = MibTableColumn
cfprFabricEthTargetEpAggrPortId = _CfprFabricEthTargetEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 5),
    _CfprFabricEthTargetEpAggrPortId_Type()
)
cfprFabricEthTargetEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpAggrPortId.setStatus("current")
_CfprFabricEthTargetEpChassisId_Type = Gauge32
_CfprFabricEthTargetEpChassisId_Object = MibTableColumn
cfprFabricEthTargetEpChassisId = _CfprFabricEthTargetEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 6),
    _CfprFabricEthTargetEpChassisId_Type()
)
cfprFabricEthTargetEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpChassisId.setStatus("current")
_CfprFabricEthTargetEpEpDn_Type = SnmpAdminString
_CfprFabricEthTargetEpEpDn_Object = MibTableColumn
cfprFabricEthTargetEpEpDn = _CfprFabricEthTargetEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 7),
    _CfprFabricEthTargetEpEpDn_Type()
)
cfprFabricEthTargetEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpEpDn.setStatus("current")
_CfprFabricEthTargetEpFltAggr_Type = Unsigned64
_CfprFabricEthTargetEpFltAggr_Object = MibTableColumn
cfprFabricEthTargetEpFltAggr = _CfprFabricEthTargetEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 8),
    _CfprFabricEthTargetEpFltAggr_Type()
)
cfprFabricEthTargetEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpFltAggr.setStatus("current")
_CfprFabricEthTargetEpIfRole_Type = CfprNetworkPortRole
_CfprFabricEthTargetEpIfRole_Object = MibTableColumn
cfprFabricEthTargetEpIfRole = _CfprFabricEthTargetEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 9),
    _CfprFabricEthTargetEpIfRole_Type()
)
cfprFabricEthTargetEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpIfRole.setStatus("current")
_CfprFabricEthTargetEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricEthTargetEpIfType_Object = MibTableColumn
cfprFabricEthTargetEpIfType = _CfprFabricEthTargetEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 10),
    _CfprFabricEthTargetEpIfType_Type()
)
cfprFabricEthTargetEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpIfType.setStatus("current")
_CfprFabricEthTargetEpLicGP_Type = Unsigned64
_CfprFabricEthTargetEpLicGP_Object = MibTableColumn
cfprFabricEthTargetEpLicGP = _CfprFabricEthTargetEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 11),
    _CfprFabricEthTargetEpLicGP_Type()
)
cfprFabricEthTargetEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpLicGP.setStatus("current")
_CfprFabricEthTargetEpLicState_Type = CfprLicenseState
_CfprFabricEthTargetEpLicState_Object = MibTableColumn
cfprFabricEthTargetEpLicState = _CfprFabricEthTargetEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 12),
    _CfprFabricEthTargetEpLicState_Type()
)
cfprFabricEthTargetEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpLicState.setStatus("current")
_CfprFabricEthTargetEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricEthTargetEpLocale_Object = MibTableColumn
cfprFabricEthTargetEpLocale = _CfprFabricEthTargetEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 13),
    _CfprFabricEthTargetEpLocale_Type()
)
cfprFabricEthTargetEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpLocale.setStatus("current")
_CfprFabricEthTargetEpMacAddress_Type = MacAddress
_CfprFabricEthTargetEpMacAddress_Object = MibTableColumn
cfprFabricEthTargetEpMacAddress = _CfprFabricEthTargetEpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 14),
    _CfprFabricEthTargetEpMacAddress_Type()
)
cfprFabricEthTargetEpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpMacAddress.setStatus("current")
_CfprFabricEthTargetEpName_Type = SnmpAdminString
_CfprFabricEthTargetEpName_Object = MibTableColumn
cfprFabricEthTargetEpName = _CfprFabricEthTargetEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 15),
    _CfprFabricEthTargetEpName_Type()
)
cfprFabricEthTargetEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpName.setStatus("current")
_CfprFabricEthTargetEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricEthTargetEpOperState_Object = MibTableColumn
cfprFabricEthTargetEpOperState = _CfprFabricEthTargetEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 16),
    _CfprFabricEthTargetEpOperState_Type()
)
cfprFabricEthTargetEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpOperState.setStatus("current")
_CfprFabricEthTargetEpOperStateReason_Type = SnmpAdminString
_CfprFabricEthTargetEpOperStateReason_Object = MibTableColumn
cfprFabricEthTargetEpOperStateReason = _CfprFabricEthTargetEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 17),
    _CfprFabricEthTargetEpOperStateReason_Type()
)
cfprFabricEthTargetEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpOperStateReason.setStatus("current")
_CfprFabricEthTargetEpPeerAggrPortId_Type = Gauge32
_CfprFabricEthTargetEpPeerAggrPortId_Object = MibTableColumn
cfprFabricEthTargetEpPeerAggrPortId = _CfprFabricEthTargetEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 18),
    _CfprFabricEthTargetEpPeerAggrPortId_Type()
)
cfprFabricEthTargetEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpPeerAggrPortId.setStatus("current")
_CfprFabricEthTargetEpPeerChassisId_Type = Gauge32
_CfprFabricEthTargetEpPeerChassisId_Object = MibTableColumn
cfprFabricEthTargetEpPeerChassisId = _CfprFabricEthTargetEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 19),
    _CfprFabricEthTargetEpPeerChassisId_Type()
)
cfprFabricEthTargetEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpPeerChassisId.setStatus("current")
_CfprFabricEthTargetEpPeerDn_Type = SnmpAdminString
_CfprFabricEthTargetEpPeerDn_Object = MibTableColumn
cfprFabricEthTargetEpPeerDn = _CfprFabricEthTargetEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 20),
    _CfprFabricEthTargetEpPeerDn_Type()
)
cfprFabricEthTargetEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpPeerDn.setStatus("current")
_CfprFabricEthTargetEpPeerPortId_Type = Gauge32
_CfprFabricEthTargetEpPeerPortId_Object = MibTableColumn
cfprFabricEthTargetEpPeerPortId = _CfprFabricEthTargetEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 21),
    _CfprFabricEthTargetEpPeerPortId_Type()
)
cfprFabricEthTargetEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpPeerPortId.setStatus("current")
_CfprFabricEthTargetEpPeerSlotId_Type = Gauge32
_CfprFabricEthTargetEpPeerSlotId_Object = MibTableColumn
cfprFabricEthTargetEpPeerSlotId = _CfprFabricEthTargetEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 22),
    _CfprFabricEthTargetEpPeerSlotId_Type()
)
cfprFabricEthTargetEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpPeerSlotId.setStatus("current")
_CfprFabricEthTargetEpPortId_Type = CfprFabricPIoEpPortId
_CfprFabricEthTargetEpPortId_Object = MibTableColumn
cfprFabricEthTargetEpPortId = _CfprFabricEthTargetEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 23),
    _CfprFabricEthTargetEpPortId_Type()
)
cfprFabricEthTargetEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpPortId.setStatus("current")
_CfprFabricEthTargetEpSlotId_Type = CfprFabricPIoEpSlotId
_CfprFabricEthTargetEpSlotId_Object = MibTableColumn
cfprFabricEthTargetEpSlotId = _CfprFabricEthTargetEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 24),
    _CfprFabricEthTargetEpSlotId_Type()
)
cfprFabricEthTargetEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpSlotId.setStatus("current")
_CfprFabricEthTargetEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthTargetEpSwitchId_Object = MibTableColumn
cfprFabricEthTargetEpSwitchId = _CfprFabricEthTargetEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 25),
    _CfprFabricEthTargetEpSwitchId_Type()
)
cfprFabricEthTargetEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpSwitchId.setStatus("current")
_CfprFabricEthTargetEpTransport_Type = CfprFabricEthTargetEpTransport
_CfprFabricEthTargetEpTransport_Object = MibTableColumn
cfprFabricEthTargetEpTransport = _CfprFabricEthTargetEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 26),
    _CfprFabricEthTargetEpTransport_Type()
)
cfprFabricEthTargetEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpTransport.setStatus("current")
_CfprFabricEthTargetEpType_Type = CfprFabricTargetEpType
_CfprFabricEthTargetEpType_Object = MibTableColumn
cfprFabricEthTargetEpType = _CfprFabricEthTargetEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 27),
    _CfprFabricEthTargetEpType_Type()
)
cfprFabricEthTargetEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpType.setStatus("current")
_CfprFabricEthTargetEpWarnings_Type = CfprFabricWarnings
_CfprFabricEthTargetEpWarnings_Object = MibTableColumn
cfprFabricEthTargetEpWarnings = _CfprFabricEthTargetEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 42, 1, 28),
    _CfprFabricEthTargetEpWarnings_Type()
)
cfprFabricEthTargetEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthTargetEpWarnings.setStatus("current")
_CfprFabricEthVlanPcTable_Object = MibTable
cfprFabricEthVlanPcTable = _CfprFabricEthVlanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43)
)
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcTable.setStatus("current")
_CfprFabricEthVlanPcEntry_Object = MibTableRow
cfprFabricEthVlanPcEntry = _CfprFabricEthVlanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1)
)
cfprFabricEthVlanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthVlanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcEntry.setStatus("current")
_CfprFabricEthVlanPcInstanceId_Type = CfprManagedObjectId
_CfprFabricEthVlanPcInstanceId_Object = MibTableColumn
cfprFabricEthVlanPcInstanceId = _CfprFabricEthVlanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 1),
    _CfprFabricEthVlanPcInstanceId_Type()
)
cfprFabricEthVlanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcInstanceId.setStatus("current")
_CfprFabricEthVlanPcDn_Type = CfprManagedObjectDn
_CfprFabricEthVlanPcDn_Object = MibTableColumn
cfprFabricEthVlanPcDn = _CfprFabricEthVlanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 2),
    _CfprFabricEthVlanPcDn_Type()
)
cfprFabricEthVlanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcDn.setStatus("current")
_CfprFabricEthVlanPcRn_Type = SnmpAdminString
_CfprFabricEthVlanPcRn_Object = MibTableColumn
cfprFabricEthVlanPcRn = _CfprFabricEthVlanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 3),
    _CfprFabricEthVlanPcRn_Type()
)
cfprFabricEthVlanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcRn.setStatus("current")
_CfprFabricEthVlanPcAdminSpeed_Type = CfprPortEthAdminSpeed
_CfprFabricEthVlanPcAdminSpeed_Object = MibTableColumn
cfprFabricEthVlanPcAdminSpeed = _CfprFabricEthVlanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 4),
    _CfprFabricEthVlanPcAdminSpeed_Type()
)
cfprFabricEthVlanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcAdminSpeed.setStatus("current")
_CfprFabricEthVlanPcAdminState_Type = CfprFabricCIoEpAdminState
_CfprFabricEthVlanPcAdminState_Object = MibTableColumn
cfprFabricEthVlanPcAdminState = _CfprFabricEthVlanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 5),
    _CfprFabricEthVlanPcAdminState_Type()
)
cfprFabricEthVlanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcAdminState.setStatus("current")
_CfprFabricEthVlanPcDescr_Type = SnmpAdminString
_CfprFabricEthVlanPcDescr_Object = MibTableColumn
cfprFabricEthVlanPcDescr = _CfprFabricEthVlanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 6),
    _CfprFabricEthVlanPcDescr_Type()
)
cfprFabricEthVlanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcDescr.setStatus("current")
_CfprFabricEthVlanPcEpDn_Type = SnmpAdminString
_CfprFabricEthVlanPcEpDn_Object = MibTableColumn
cfprFabricEthVlanPcEpDn = _CfprFabricEthVlanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 7),
    _CfprFabricEthVlanPcEpDn_Type()
)
cfprFabricEthVlanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcEpDn.setStatus("current")
_CfprFabricEthVlanPcFltAggr_Type = Unsigned64
_CfprFabricEthVlanPcFltAggr_Object = MibTableColumn
cfprFabricEthVlanPcFltAggr = _CfprFabricEthVlanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 8),
    _CfprFabricEthVlanPcFltAggr_Type()
)
cfprFabricEthVlanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcFltAggr.setStatus("current")
_CfprFabricEthVlanPcIfRole_Type = CfprFabricEstcPcIfRole
_CfprFabricEthVlanPcIfRole_Object = MibTableColumn
cfprFabricEthVlanPcIfRole = _CfprFabricEthVlanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 9),
    _CfprFabricEthVlanPcIfRole_Type()
)
cfprFabricEthVlanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcIfRole.setStatus("current")
_CfprFabricEthVlanPcIfType_Type = CfprFabricCIoEpIfType
_CfprFabricEthVlanPcIfType_Object = MibTableColumn
cfprFabricEthVlanPcIfType = _CfprFabricEthVlanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 10),
    _CfprFabricEthVlanPcIfType_Type()
)
cfprFabricEthVlanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcIfType.setStatus("current")
_CfprFabricEthVlanPcIsNative_Type = TruthValue
_CfprFabricEthVlanPcIsNative_Object = MibTableColumn
cfprFabricEthVlanPcIsNative = _CfprFabricEthVlanPcIsNative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 11),
    _CfprFabricEthVlanPcIsNative_Type()
)
cfprFabricEthVlanPcIsNative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcIsNative.setStatus("current")
_CfprFabricEthVlanPcLocale_Type = CfprFabricExternalPcLocale
_CfprFabricEthVlanPcLocale_Object = MibTableColumn
cfprFabricEthVlanPcLocale = _CfprFabricEthVlanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 12),
    _CfprFabricEthVlanPcLocale_Type()
)
cfprFabricEthVlanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcLocale.setStatus("current")
_CfprFabricEthVlanPcName_Type = SnmpAdminString
_CfprFabricEthVlanPcName_Object = MibTableColumn
cfprFabricEthVlanPcName = _CfprFabricEthVlanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 13),
    _CfprFabricEthVlanPcName_Type()
)
cfprFabricEthVlanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcName.setStatus("current")
_CfprFabricEthVlanPcOperSpeed_Type = CfprPortEthSpeed
_CfprFabricEthVlanPcOperSpeed_Object = MibTableColumn
cfprFabricEthVlanPcOperSpeed = _CfprFabricEthVlanPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 14),
    _CfprFabricEthVlanPcOperSpeed_Type()
)
cfprFabricEthVlanPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcOperSpeed.setStatus("current")
_CfprFabricEthVlanPcOperState_Type = CfprNetworkPortOperState
_CfprFabricEthVlanPcOperState_Object = MibTableColumn
cfprFabricEthVlanPcOperState = _CfprFabricEthVlanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 15),
    _CfprFabricEthVlanPcOperState_Type()
)
cfprFabricEthVlanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcOperState.setStatus("current")
_CfprFabricEthVlanPcPeerDn_Type = SnmpAdminString
_CfprFabricEthVlanPcPeerDn_Object = MibTableColumn
cfprFabricEthVlanPcPeerDn = _CfprFabricEthVlanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 16),
    _CfprFabricEthVlanPcPeerDn_Type()
)
cfprFabricEthVlanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcPeerDn.setStatus("current")
_CfprFabricEthVlanPcPortId_Type = Gauge32
_CfprFabricEthVlanPcPortId_Object = MibTableColumn
cfprFabricEthVlanPcPortId = _CfprFabricEthVlanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 17),
    _CfprFabricEthVlanPcPortId_Type()
)
cfprFabricEthVlanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcPortId.setStatus("current")
_CfprFabricEthVlanPcStateQual_Type = SnmpAdminString
_CfprFabricEthVlanPcStateQual_Object = MibTableColumn
cfprFabricEthVlanPcStateQual = _CfprFabricEthVlanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 18),
    _CfprFabricEthVlanPcStateQual_Type()
)
cfprFabricEthVlanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcStateQual.setStatus("current")
_CfprFabricEthVlanPcSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthVlanPcSwitchId_Object = MibTableColumn
cfprFabricEthVlanPcSwitchId = _CfprFabricEthVlanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 19),
    _CfprFabricEthVlanPcSwitchId_Type()
)
cfprFabricEthVlanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcSwitchId.setStatus("current")
_CfprFabricEthVlanPcTransport_Type = CfprFabricEthVlanPcTransport
_CfprFabricEthVlanPcTransport_Object = MibTableColumn
cfprFabricEthVlanPcTransport = _CfprFabricEthVlanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 20),
    _CfprFabricEthVlanPcTransport_Type()
)
cfprFabricEthVlanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcTransport.setStatus("current")
_CfprFabricEthVlanPcType_Type = CfprFabricEstcPcType
_CfprFabricEthVlanPcType_Object = MibTableColumn
cfprFabricEthVlanPcType = _CfprFabricEthVlanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 21),
    _CfprFabricEthVlanPcType_Type()
)
cfprFabricEthVlanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcType.setStatus("current")
_CfprFabricEthVlanPcWarnings_Type = CfprFabricWarnings
_CfprFabricEthVlanPcWarnings_Object = MibTableColumn
cfprFabricEthVlanPcWarnings = _CfprFabricEthVlanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 43, 1, 22),
    _CfprFabricEthVlanPcWarnings_Type()
)
cfprFabricEthVlanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPcWarnings.setStatus("current")
_CfprFabricEthVlanPortEpTable_Object = MibTable
cfprFabricEthVlanPortEpTable = _CfprFabricEthVlanPortEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44)
)
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpTable.setStatus("current")
_CfprFabricEthVlanPortEpEntry_Object = MibTableRow
cfprFabricEthVlanPortEpEntry = _CfprFabricEthVlanPortEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1)
)
cfprFabricEthVlanPortEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricEthVlanPortEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpEntry.setStatus("current")
_CfprFabricEthVlanPortEpInstanceId_Type = CfprManagedObjectId
_CfprFabricEthVlanPortEpInstanceId_Object = MibTableColumn
cfprFabricEthVlanPortEpInstanceId = _CfprFabricEthVlanPortEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 1),
    _CfprFabricEthVlanPortEpInstanceId_Type()
)
cfprFabricEthVlanPortEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpInstanceId.setStatus("current")
_CfprFabricEthVlanPortEpDn_Type = CfprManagedObjectDn
_CfprFabricEthVlanPortEpDn_Object = MibTableColumn
cfprFabricEthVlanPortEpDn = _CfprFabricEthVlanPortEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 2),
    _CfprFabricEthVlanPortEpDn_Type()
)
cfprFabricEthVlanPortEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpDn.setStatus("current")
_CfprFabricEthVlanPortEpRn_Type = SnmpAdminString
_CfprFabricEthVlanPortEpRn_Object = MibTableColumn
cfprFabricEthVlanPortEpRn = _CfprFabricEthVlanPortEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 3),
    _CfprFabricEthVlanPortEpRn_Type()
)
cfprFabricEthVlanPortEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpRn.setStatus("current")
_CfprFabricEthVlanPortEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricEthVlanPortEpAdminState_Object = MibTableColumn
cfprFabricEthVlanPortEpAdminState = _CfprFabricEthVlanPortEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 4),
    _CfprFabricEthVlanPortEpAdminState_Type()
)
cfprFabricEthVlanPortEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpAdminState.setStatus("current")
_CfprFabricEthVlanPortEpAggrPortId_Type = Gauge32
_CfprFabricEthVlanPortEpAggrPortId_Object = MibTableColumn
cfprFabricEthVlanPortEpAggrPortId = _CfprFabricEthVlanPortEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 5),
    _CfprFabricEthVlanPortEpAggrPortId_Type()
)
cfprFabricEthVlanPortEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpAggrPortId.setStatus("current")
_CfprFabricEthVlanPortEpChassisId_Type = Gauge32
_CfprFabricEthVlanPortEpChassisId_Object = MibTableColumn
cfprFabricEthVlanPortEpChassisId = _CfprFabricEthVlanPortEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 6),
    _CfprFabricEthVlanPortEpChassisId_Type()
)
cfprFabricEthVlanPortEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpChassisId.setStatus("current")
_CfprFabricEthVlanPortEpEpDn_Type = SnmpAdminString
_CfprFabricEthVlanPortEpEpDn_Object = MibTableColumn
cfprFabricEthVlanPortEpEpDn = _CfprFabricEthVlanPortEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 7),
    _CfprFabricEthVlanPortEpEpDn_Type()
)
cfprFabricEthVlanPortEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpEpDn.setStatus("current")
_CfprFabricEthVlanPortEpFltAggr_Type = Unsigned64
_CfprFabricEthVlanPortEpFltAggr_Object = MibTableColumn
cfprFabricEthVlanPortEpFltAggr = _CfprFabricEthVlanPortEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 8),
    _CfprFabricEthVlanPortEpFltAggr_Type()
)
cfprFabricEthVlanPortEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpFltAggr.setStatus("current")
_CfprFabricEthVlanPortEpIfRole_Type = CfprFabricLanEpIfRole
_CfprFabricEthVlanPortEpIfRole_Object = MibTableColumn
cfprFabricEthVlanPortEpIfRole = _CfprFabricEthVlanPortEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 9),
    _CfprFabricEthVlanPortEpIfRole_Type()
)
cfprFabricEthVlanPortEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpIfRole.setStatus("current")
_CfprFabricEthVlanPortEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricEthVlanPortEpIfType_Object = MibTableColumn
cfprFabricEthVlanPortEpIfType = _CfprFabricEthVlanPortEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 10),
    _CfprFabricEthVlanPortEpIfType_Type()
)
cfprFabricEthVlanPortEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpIfType.setStatus("current")
_CfprFabricEthVlanPortEpIsNative_Type = TruthValue
_CfprFabricEthVlanPortEpIsNative_Object = MibTableColumn
cfprFabricEthVlanPortEpIsNative = _CfprFabricEthVlanPortEpIsNative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 11),
    _CfprFabricEthVlanPortEpIsNative_Type()
)
cfprFabricEthVlanPortEpIsNative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpIsNative.setStatus("current")
_CfprFabricEthVlanPortEpLicGP_Type = Unsigned64
_CfprFabricEthVlanPortEpLicGP_Object = MibTableColumn
cfprFabricEthVlanPortEpLicGP = _CfprFabricEthVlanPortEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 12),
    _CfprFabricEthVlanPortEpLicGP_Type()
)
cfprFabricEthVlanPortEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpLicGP.setStatus("current")
_CfprFabricEthVlanPortEpLicState_Type = CfprLicenseState
_CfprFabricEthVlanPortEpLicState_Object = MibTableColumn
cfprFabricEthVlanPortEpLicState = _CfprFabricEthVlanPortEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 13),
    _CfprFabricEthVlanPortEpLicState_Type()
)
cfprFabricEthVlanPortEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpLicState.setStatus("current")
_CfprFabricEthVlanPortEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricEthVlanPortEpLocale_Object = MibTableColumn
cfprFabricEthVlanPortEpLocale = _CfprFabricEthVlanPortEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 14),
    _CfprFabricEthVlanPortEpLocale_Type()
)
cfprFabricEthVlanPortEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpLocale.setStatus("current")
_CfprFabricEthVlanPortEpName_Type = SnmpAdminString
_CfprFabricEthVlanPortEpName_Object = MibTableColumn
cfprFabricEthVlanPortEpName = _CfprFabricEthVlanPortEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 15),
    _CfprFabricEthVlanPortEpName_Type()
)
cfprFabricEthVlanPortEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpName.setStatus("current")
_CfprFabricEthVlanPortEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricEthVlanPortEpOperState_Object = MibTableColumn
cfprFabricEthVlanPortEpOperState = _CfprFabricEthVlanPortEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 16),
    _CfprFabricEthVlanPortEpOperState_Type()
)
cfprFabricEthVlanPortEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpOperState.setStatus("current")
_CfprFabricEthVlanPortEpOperStateReason_Type = SnmpAdminString
_CfprFabricEthVlanPortEpOperStateReason_Object = MibTableColumn
cfprFabricEthVlanPortEpOperStateReason = _CfprFabricEthVlanPortEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 17),
    _CfprFabricEthVlanPortEpOperStateReason_Type()
)
cfprFabricEthVlanPortEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpOperStateReason.setStatus("current")
_CfprFabricEthVlanPortEpPeerAggrPortId_Type = Gauge32
_CfprFabricEthVlanPortEpPeerAggrPortId_Object = MibTableColumn
cfprFabricEthVlanPortEpPeerAggrPortId = _CfprFabricEthVlanPortEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 18),
    _CfprFabricEthVlanPortEpPeerAggrPortId_Type()
)
cfprFabricEthVlanPortEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpPeerAggrPortId.setStatus("current")
_CfprFabricEthVlanPortEpPeerChassisId_Type = Gauge32
_CfprFabricEthVlanPortEpPeerChassisId_Object = MibTableColumn
cfprFabricEthVlanPortEpPeerChassisId = _CfprFabricEthVlanPortEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 19),
    _CfprFabricEthVlanPortEpPeerChassisId_Type()
)
cfprFabricEthVlanPortEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpPeerChassisId.setStatus("current")
_CfprFabricEthVlanPortEpPeerDn_Type = SnmpAdminString
_CfprFabricEthVlanPortEpPeerDn_Object = MibTableColumn
cfprFabricEthVlanPortEpPeerDn = _CfprFabricEthVlanPortEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 20),
    _CfprFabricEthVlanPortEpPeerDn_Type()
)
cfprFabricEthVlanPortEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpPeerDn.setStatus("current")
_CfprFabricEthVlanPortEpPeerPortId_Type = Gauge32
_CfprFabricEthVlanPortEpPeerPortId_Object = MibTableColumn
cfprFabricEthVlanPortEpPeerPortId = _CfprFabricEthVlanPortEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 21),
    _CfprFabricEthVlanPortEpPeerPortId_Type()
)
cfprFabricEthVlanPortEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpPeerPortId.setStatus("current")
_CfprFabricEthVlanPortEpPeerSlotId_Type = Gauge32
_CfprFabricEthVlanPortEpPeerSlotId_Object = MibTableColumn
cfprFabricEthVlanPortEpPeerSlotId = _CfprFabricEthVlanPortEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 22),
    _CfprFabricEthVlanPortEpPeerSlotId_Type()
)
cfprFabricEthVlanPortEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpPeerSlotId.setStatus("current")
_CfprFabricEthVlanPortEpPortId_Type = Gauge32
_CfprFabricEthVlanPortEpPortId_Object = MibTableColumn
cfprFabricEthVlanPortEpPortId = _CfprFabricEthVlanPortEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 23),
    _CfprFabricEthVlanPortEpPortId_Type()
)
cfprFabricEthVlanPortEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpPortId.setStatus("current")
_CfprFabricEthVlanPortEpSlotId_Type = Gauge32
_CfprFabricEthVlanPortEpSlotId_Object = MibTableColumn
cfprFabricEthVlanPortEpSlotId = _CfprFabricEthVlanPortEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 24),
    _CfprFabricEthVlanPortEpSlotId_Type()
)
cfprFabricEthVlanPortEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpSlotId.setStatus("current")
_CfprFabricEthVlanPortEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricEthVlanPortEpSwitchId_Object = MibTableColumn
cfprFabricEthVlanPortEpSwitchId = _CfprFabricEthVlanPortEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 25),
    _CfprFabricEthVlanPortEpSwitchId_Type()
)
cfprFabricEthVlanPortEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpSwitchId.setStatus("current")
_CfprFabricEthVlanPortEpTransport_Type = CfprFabricAEthLanEpTransport
_CfprFabricEthVlanPortEpTransport_Object = MibTableColumn
cfprFabricEthVlanPortEpTransport = _CfprFabricEthVlanPortEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 26),
    _CfprFabricEthVlanPortEpTransport_Type()
)
cfprFabricEthVlanPortEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpTransport.setStatus("current")
_CfprFabricEthVlanPortEpType_Type = CfprFabricLanEpType
_CfprFabricEthVlanPortEpType_Object = MibTableColumn
cfprFabricEthVlanPortEpType = _CfprFabricEthVlanPortEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 27),
    _CfprFabricEthVlanPortEpType_Type()
)
cfprFabricEthVlanPortEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpType.setStatus("current")
_CfprFabricEthVlanPortEpWarnings_Type = CfprFabricWarnings
_CfprFabricEthVlanPortEpWarnings_Object = MibTableColumn
cfprFabricEthVlanPortEpWarnings = _CfprFabricEthVlanPortEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 44, 1, 28),
    _CfprFabricEthVlanPortEpWarnings_Type()
)
cfprFabricEthVlanPortEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricEthVlanPortEpWarnings.setStatus("current")
_CfprFabricFcSanTable_Object = MibTable
cfprFabricFcSanTable = _CfprFabricFcSanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55)
)
if mibBuilder.loadTexts:
    cfprFabricFcSanTable.setStatus("current")
_CfprFabricFcSanEntry_Object = MibTableRow
cfprFabricFcSanEntry = _CfprFabricFcSanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1)
)
cfprFabricFcSanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcSanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcSanEntry.setStatus("current")
_CfprFabricFcSanInstanceId_Type = CfprManagedObjectId
_CfprFabricFcSanInstanceId_Object = MibTableColumn
cfprFabricFcSanInstanceId = _CfprFabricFcSanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 1),
    _CfprFabricFcSanInstanceId_Type()
)
cfprFabricFcSanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcSanInstanceId.setStatus("current")
_CfprFabricFcSanDn_Type = CfprManagedObjectDn
_CfprFabricFcSanDn_Object = MibTableColumn
cfprFabricFcSanDn = _CfprFabricFcSanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 2),
    _CfprFabricFcSanDn_Type()
)
cfprFabricFcSanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanDn.setStatus("current")
_CfprFabricFcSanRn_Type = SnmpAdminString
_CfprFabricFcSanRn_Object = MibTableColumn
cfprFabricFcSanRn = _CfprFabricFcSanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 3),
    _CfprFabricFcSanRn_Type()
)
cfprFabricFcSanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanRn.setStatus("current")
_CfprFabricFcSanId_Type = CfprNetworkSwitchId
_CfprFabricFcSanId_Object = MibTableColumn
cfprFabricFcSanId = _CfprFabricFcSanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 4),
    _CfprFabricFcSanId_Type()
)
cfprFabricFcSanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanId.setStatus("current")
_CfprFabricFcSanLocale_Type = CfprFabricExternalLocale
_CfprFabricFcSanLocale_Object = MibTableColumn
cfprFabricFcSanLocale = _CfprFabricFcSanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 5),
    _CfprFabricFcSanLocale_Type()
)
cfprFabricFcSanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanLocale.setStatus("current")
_CfprFabricFcSanName_Type = SnmpAdminString
_CfprFabricFcSanName_Object = MibTableColumn
cfprFabricFcSanName = _CfprFabricFcSanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 6),
    _CfprFabricFcSanName_Type()
)
cfprFabricFcSanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanName.setStatus("current")
_CfprFabricFcSanTransport_Type = CfprFabricFcSanTransport
_CfprFabricFcSanTransport_Object = MibTableColumn
cfprFabricFcSanTransport = _CfprFabricFcSanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 7),
    _CfprFabricFcSanTransport_Type()
)
cfprFabricFcSanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanTransport.setStatus("current")
_CfprFabricFcSanType_Type = CfprFabricSanType
_CfprFabricFcSanType_Object = MibTableColumn
cfprFabricFcSanType = _CfprFabricFcSanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 8),
    _CfprFabricFcSanType_Type()
)
cfprFabricFcSanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanType.setStatus("current")
_CfprFabricFcSanUplinkTrunking_Type = CfprFabricFcSanUplinkTrunking
_CfprFabricFcSanUplinkTrunking_Object = MibTableColumn
cfprFabricFcSanUplinkTrunking = _CfprFabricFcSanUplinkTrunking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 55, 1, 9),
    _CfprFabricFcSanUplinkTrunking_Type()
)
cfprFabricFcSanUplinkTrunking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanUplinkTrunking.setStatus("current")
_CfprFabricFcSanEpTable_Object = MibTable
cfprFabricFcSanEpTable = _CfprFabricFcSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56)
)
if mibBuilder.loadTexts:
    cfprFabricFcSanEpTable.setStatus("current")
_CfprFabricFcSanEpEntry_Object = MibTableRow
cfprFabricFcSanEpEntry = _CfprFabricFcSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1)
)
cfprFabricFcSanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcSanEpEntry.setStatus("current")
_CfprFabricFcSanEpInstanceId_Type = CfprManagedObjectId
_CfprFabricFcSanEpInstanceId_Object = MibTableColumn
cfprFabricFcSanEpInstanceId = _CfprFabricFcSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 1),
    _CfprFabricFcSanEpInstanceId_Type()
)
cfprFabricFcSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpInstanceId.setStatus("current")
_CfprFabricFcSanEpDn_Type = CfprManagedObjectDn
_CfprFabricFcSanEpDn_Object = MibTableColumn
cfprFabricFcSanEpDn = _CfprFabricFcSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 2),
    _CfprFabricFcSanEpDn_Type()
)
cfprFabricFcSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpDn.setStatus("current")
_CfprFabricFcSanEpRn_Type = SnmpAdminString
_CfprFabricFcSanEpRn_Object = MibTableColumn
cfprFabricFcSanEpRn = _CfprFabricFcSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 3),
    _CfprFabricFcSanEpRn_Type()
)
cfprFabricFcSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpRn.setStatus("current")
_CfprFabricFcSanEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricFcSanEpAdminState_Object = MibTableColumn
cfprFabricFcSanEpAdminState = _CfprFabricFcSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 4),
    _CfprFabricFcSanEpAdminState_Type()
)
cfprFabricFcSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpAdminState.setStatus("current")
_CfprFabricFcSanEpAggrPortId_Type = Gauge32
_CfprFabricFcSanEpAggrPortId_Object = MibTableColumn
cfprFabricFcSanEpAggrPortId = _CfprFabricFcSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 5),
    _CfprFabricFcSanEpAggrPortId_Type()
)
cfprFabricFcSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpAggrPortId.setStatus("current")
_CfprFabricFcSanEpChassisId_Type = Gauge32
_CfprFabricFcSanEpChassisId_Object = MibTableColumn
cfprFabricFcSanEpChassisId = _CfprFabricFcSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 6),
    _CfprFabricFcSanEpChassisId_Type()
)
cfprFabricFcSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpChassisId.setStatus("current")
_CfprFabricFcSanEpEpDn_Type = SnmpAdminString
_CfprFabricFcSanEpEpDn_Object = MibTableColumn
cfprFabricFcSanEpEpDn = _CfprFabricFcSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 7),
    _CfprFabricFcSanEpEpDn_Type()
)
cfprFabricFcSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpEpDn.setStatus("current")
_CfprFabricFcSanEpFillPattern_Type = CfprFabricFillPattern
_CfprFabricFcSanEpFillPattern_Object = MibTableColumn
cfprFabricFcSanEpFillPattern = _CfprFabricFcSanEpFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 8),
    _CfprFabricFcSanEpFillPattern_Type()
)
cfprFabricFcSanEpFillPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpFillPattern.setStatus("current")
_CfprFabricFcSanEpFltAggr_Type = Unsigned64
_CfprFabricFcSanEpFltAggr_Object = MibTableColumn
cfprFabricFcSanEpFltAggr = _CfprFabricFcSanEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 9),
    _CfprFabricFcSanEpFltAggr_Type()
)
cfprFabricFcSanEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpFltAggr.setStatus("current")
_CfprFabricFcSanEpIfRole_Type = CfprFabricSanEpIfRole
_CfprFabricFcSanEpIfRole_Object = MibTableColumn
cfprFabricFcSanEpIfRole = _CfprFabricFcSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 10),
    _CfprFabricFcSanEpIfRole_Type()
)
cfprFabricFcSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpIfRole.setStatus("current")
_CfprFabricFcSanEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricFcSanEpIfType_Object = MibTableColumn
cfprFabricFcSanEpIfType = _CfprFabricFcSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 11),
    _CfprFabricFcSanEpIfType_Type()
)
cfprFabricFcSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpIfType.setStatus("current")
_CfprFabricFcSanEpLicGP_Type = Unsigned64
_CfprFabricFcSanEpLicGP_Object = MibTableColumn
cfprFabricFcSanEpLicGP = _CfprFabricFcSanEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 12),
    _CfprFabricFcSanEpLicGP_Type()
)
cfprFabricFcSanEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpLicGP.setStatus("current")
_CfprFabricFcSanEpLicState_Type = CfprLicenseState
_CfprFabricFcSanEpLicState_Object = MibTableColumn
cfprFabricFcSanEpLicState = _CfprFabricFcSanEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 13),
    _CfprFabricFcSanEpLicState_Type()
)
cfprFabricFcSanEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpLicState.setStatus("current")
_CfprFabricFcSanEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricFcSanEpLocale_Object = MibTableColumn
cfprFabricFcSanEpLocale = _CfprFabricFcSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 14),
    _CfprFabricFcSanEpLocale_Type()
)
cfprFabricFcSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpLocale.setStatus("current")
_CfprFabricFcSanEpName_Type = SnmpAdminString
_CfprFabricFcSanEpName_Object = MibTableColumn
cfprFabricFcSanEpName = _CfprFabricFcSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 15),
    _CfprFabricFcSanEpName_Type()
)
cfprFabricFcSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpName.setStatus("current")
_CfprFabricFcSanEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricFcSanEpOperState_Object = MibTableColumn
cfprFabricFcSanEpOperState = _CfprFabricFcSanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 16),
    _CfprFabricFcSanEpOperState_Type()
)
cfprFabricFcSanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpOperState.setStatus("current")
_CfprFabricFcSanEpOperStateReason_Type = SnmpAdminString
_CfprFabricFcSanEpOperStateReason_Object = MibTableColumn
cfprFabricFcSanEpOperStateReason = _CfprFabricFcSanEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 17),
    _CfprFabricFcSanEpOperStateReason_Type()
)
cfprFabricFcSanEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpOperStateReason.setStatus("current")
_CfprFabricFcSanEpPeerAggrPortId_Type = Gauge32
_CfprFabricFcSanEpPeerAggrPortId_Object = MibTableColumn
cfprFabricFcSanEpPeerAggrPortId = _CfprFabricFcSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 18),
    _CfprFabricFcSanEpPeerAggrPortId_Type()
)
cfprFabricFcSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpPeerAggrPortId.setStatus("current")
_CfprFabricFcSanEpPeerChassisId_Type = Gauge32
_CfprFabricFcSanEpPeerChassisId_Object = MibTableColumn
cfprFabricFcSanEpPeerChassisId = _CfprFabricFcSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 19),
    _CfprFabricFcSanEpPeerChassisId_Type()
)
cfprFabricFcSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpPeerChassisId.setStatus("current")
_CfprFabricFcSanEpPeerDn_Type = SnmpAdminString
_CfprFabricFcSanEpPeerDn_Object = MibTableColumn
cfprFabricFcSanEpPeerDn = _CfprFabricFcSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 20),
    _CfprFabricFcSanEpPeerDn_Type()
)
cfprFabricFcSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpPeerDn.setStatus("current")
_CfprFabricFcSanEpPeerPortId_Type = Gauge32
_CfprFabricFcSanEpPeerPortId_Object = MibTableColumn
cfprFabricFcSanEpPeerPortId = _CfprFabricFcSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 21),
    _CfprFabricFcSanEpPeerPortId_Type()
)
cfprFabricFcSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpPeerPortId.setStatus("current")
_CfprFabricFcSanEpPeerSlotId_Type = Gauge32
_CfprFabricFcSanEpPeerSlotId_Object = MibTableColumn
cfprFabricFcSanEpPeerSlotId = _CfprFabricFcSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 22),
    _CfprFabricFcSanEpPeerSlotId_Type()
)
cfprFabricFcSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpPeerSlotId.setStatus("current")
_CfprFabricFcSanEpPortId_Type = CfprFabricFcSanEpPortId
_CfprFabricFcSanEpPortId_Object = MibTableColumn
cfprFabricFcSanEpPortId = _CfprFabricFcSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 23),
    _CfprFabricFcSanEpPortId_Type()
)
cfprFabricFcSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpPortId.setStatus("current")
_CfprFabricFcSanEpSlotId_Type = CfprFabricFcSanEpSlotId
_CfprFabricFcSanEpSlotId_Object = MibTableColumn
cfprFabricFcSanEpSlotId = _CfprFabricFcSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 24),
    _CfprFabricFcSanEpSlotId_Type()
)
cfprFabricFcSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpSlotId.setStatus("current")
_CfprFabricFcSanEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcSanEpSwitchId_Object = MibTableColumn
cfprFabricFcSanEpSwitchId = _CfprFabricFcSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 25),
    _CfprFabricFcSanEpSwitchId_Type()
)
cfprFabricFcSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpSwitchId.setStatus("current")
_CfprFabricFcSanEpTransport_Type = CfprFabricAFcSanEpTransport
_CfprFabricFcSanEpTransport_Object = MibTableColumn
cfprFabricFcSanEpTransport = _CfprFabricFcSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 26),
    _CfprFabricFcSanEpTransport_Type()
)
cfprFabricFcSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpTransport.setStatus("current")
_CfprFabricFcSanEpType_Type = CfprFabricSanEpType
_CfprFabricFcSanEpType_Object = MibTableColumn
cfprFabricFcSanEpType = _CfprFabricFcSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 27),
    _CfprFabricFcSanEpType_Type()
)
cfprFabricFcSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpType.setStatus("current")
_CfprFabricFcSanEpUsrLbl_Type = SnmpAdminString
_CfprFabricFcSanEpUsrLbl_Object = MibTableColumn
cfprFabricFcSanEpUsrLbl = _CfprFabricFcSanEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 28),
    _CfprFabricFcSanEpUsrLbl_Type()
)
cfprFabricFcSanEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpUsrLbl.setStatus("current")
_CfprFabricFcSanEpWarnings_Type = CfprFabricWarnings
_CfprFabricFcSanEpWarnings_Object = MibTableColumn
cfprFabricFcSanEpWarnings = _CfprFabricFcSanEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 56, 1, 29),
    _CfprFabricFcSanEpWarnings_Type()
)
cfprFabricFcSanEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanEpWarnings.setStatus("current")
_CfprFabricFcSanPcTable_Object = MibTable
cfprFabricFcSanPcTable = _CfprFabricFcSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57)
)
if mibBuilder.loadTexts:
    cfprFabricFcSanPcTable.setStatus("current")
_CfprFabricFcSanPcEntry_Object = MibTableRow
cfprFabricFcSanPcEntry = _CfprFabricFcSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1)
)
cfprFabricFcSanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEntry.setStatus("current")
_CfprFabricFcSanPcInstanceId_Type = CfprManagedObjectId
_CfprFabricFcSanPcInstanceId_Object = MibTableColumn
cfprFabricFcSanPcInstanceId = _CfprFabricFcSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 1),
    _CfprFabricFcSanPcInstanceId_Type()
)
cfprFabricFcSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcInstanceId.setStatus("current")
_CfprFabricFcSanPcDn_Type = CfprManagedObjectDn
_CfprFabricFcSanPcDn_Object = MibTableColumn
cfprFabricFcSanPcDn = _CfprFabricFcSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 2),
    _CfprFabricFcSanPcDn_Type()
)
cfprFabricFcSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcDn.setStatus("current")
_CfprFabricFcSanPcRn_Type = SnmpAdminString
_CfprFabricFcSanPcRn_Object = MibTableColumn
cfprFabricFcSanPcRn = _CfprFabricFcSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 3),
    _CfprFabricFcSanPcRn_Type()
)
cfprFabricFcSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcRn.setStatus("current")
_CfprFabricFcSanPcAdminSpeed_Type = CfprPortSpeed
_CfprFabricFcSanPcAdminSpeed_Object = MibTableColumn
cfprFabricFcSanPcAdminSpeed = _CfprFabricFcSanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 4),
    _CfprFabricFcSanPcAdminSpeed_Type()
)
cfprFabricFcSanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcAdminSpeed.setStatus("current")
_CfprFabricFcSanPcAdminState_Type = CfprFabricCIoEpAdminState
_CfprFabricFcSanPcAdminState_Object = MibTableColumn
cfprFabricFcSanPcAdminState = _CfprFabricFcSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 5),
    _CfprFabricFcSanPcAdminState_Type()
)
cfprFabricFcSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcAdminState.setStatus("current")
_CfprFabricFcSanPcConfigState_Type = CfprFabricConfigState
_CfprFabricFcSanPcConfigState_Object = MibTableColumn
cfprFabricFcSanPcConfigState = _CfprFabricFcSanPcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 6),
    _CfprFabricFcSanPcConfigState_Type()
)
cfprFabricFcSanPcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcConfigState.setStatus("current")
_CfprFabricFcSanPcConfigStatus_Type = CfprFabricPcConfigStatus
_CfprFabricFcSanPcConfigStatus_Object = MibTableColumn
cfprFabricFcSanPcConfigStatus = _CfprFabricFcSanPcConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 7),
    _CfprFabricFcSanPcConfigStatus_Type()
)
cfprFabricFcSanPcConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcConfigStatus.setStatus("current")
_CfprFabricFcSanPcDescr_Type = SnmpAdminString
_CfprFabricFcSanPcDescr_Object = MibTableColumn
cfprFabricFcSanPcDescr = _CfprFabricFcSanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 8),
    _CfprFabricFcSanPcDescr_Type()
)
cfprFabricFcSanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcDescr.setStatus("current")
_CfprFabricFcSanPcEpDn_Type = SnmpAdminString
_CfprFabricFcSanPcEpDn_Object = MibTableColumn
cfprFabricFcSanPcEpDn = _CfprFabricFcSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 9),
    _CfprFabricFcSanPcEpDn_Type()
)
cfprFabricFcSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpDn.setStatus("current")
_CfprFabricFcSanPcFltAggr_Type = Unsigned64
_CfprFabricFcSanPcFltAggr_Object = MibTableColumn
cfprFabricFcSanPcFltAggr = _CfprFabricFcSanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 10),
    _CfprFabricFcSanPcFltAggr_Type()
)
cfprFabricFcSanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcFltAggr.setStatus("current")
_CfprFabricFcSanPcIfRole_Type = CfprFabricSanPcIfRole
_CfprFabricFcSanPcIfRole_Object = MibTableColumn
cfprFabricFcSanPcIfRole = _CfprFabricFcSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 11),
    _CfprFabricFcSanPcIfRole_Type()
)
cfprFabricFcSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcIfRole.setStatus("current")
_CfprFabricFcSanPcIfType_Type = CfprFabricCIoEpIfType
_CfprFabricFcSanPcIfType_Object = MibTableColumn
cfprFabricFcSanPcIfType = _CfprFabricFcSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 12),
    _CfprFabricFcSanPcIfType_Type()
)
cfprFabricFcSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcIfType.setStatus("current")
_CfprFabricFcSanPcLocale_Type = CfprFabricExternalPcLocale
_CfprFabricFcSanPcLocale_Object = MibTableColumn
cfprFabricFcSanPcLocale = _CfprFabricFcSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 13),
    _CfprFabricFcSanPcLocale_Type()
)
cfprFabricFcSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcLocale.setStatus("current")
_CfprFabricFcSanPcName_Type = SnmpAdminString
_CfprFabricFcSanPcName_Object = MibTableColumn
cfprFabricFcSanPcName = _CfprFabricFcSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 14),
    _CfprFabricFcSanPcName_Type()
)
cfprFabricFcSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcName.setStatus("current")
_CfprFabricFcSanPcOperSpeed_Type = Gauge32
_CfprFabricFcSanPcOperSpeed_Object = MibTableColumn
cfprFabricFcSanPcOperSpeed = _CfprFabricFcSanPcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 15),
    _CfprFabricFcSanPcOperSpeed_Type()
)
cfprFabricFcSanPcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcOperSpeed.setStatus("current")
_CfprFabricFcSanPcOperState_Type = CfprNetworkPortOperState
_CfprFabricFcSanPcOperState_Object = MibTableColumn
cfprFabricFcSanPcOperState = _CfprFabricFcSanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 16),
    _CfprFabricFcSanPcOperState_Type()
)
cfprFabricFcSanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcOperState.setStatus("current")
_CfprFabricFcSanPcPeerDn_Type = SnmpAdminString
_CfprFabricFcSanPcPeerDn_Object = MibTableColumn
cfprFabricFcSanPcPeerDn = _CfprFabricFcSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 17),
    _CfprFabricFcSanPcPeerDn_Type()
)
cfprFabricFcSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcPeerDn.setStatus("current")
_CfprFabricFcSanPcPortId_Type = Gauge32
_CfprFabricFcSanPcPortId_Object = MibTableColumn
cfprFabricFcSanPcPortId = _CfprFabricFcSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 18),
    _CfprFabricFcSanPcPortId_Type()
)
cfprFabricFcSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcPortId.setStatus("current")
_CfprFabricFcSanPcStateQual_Type = SnmpAdminString
_CfprFabricFcSanPcStateQual_Object = MibTableColumn
cfprFabricFcSanPcStateQual = _CfprFabricFcSanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 19),
    _CfprFabricFcSanPcStateQual_Type()
)
cfprFabricFcSanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcStateQual.setStatus("current")
_CfprFabricFcSanPcSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcSanPcSwitchId_Object = MibTableColumn
cfprFabricFcSanPcSwitchId = _CfprFabricFcSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 20),
    _CfprFabricFcSanPcSwitchId_Type()
)
cfprFabricFcSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcSwitchId.setStatus("current")
_CfprFabricFcSanPcTransport_Type = CfprFabricFcSanPcTransport
_CfprFabricFcSanPcTransport_Object = MibTableColumn
cfprFabricFcSanPcTransport = _CfprFabricFcSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 21),
    _CfprFabricFcSanPcTransport_Type()
)
cfprFabricFcSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcTransport.setStatus("current")
_CfprFabricFcSanPcType_Type = CfprFabricSanPcType
_CfprFabricFcSanPcType_Object = MibTableColumn
cfprFabricFcSanPcType = _CfprFabricFcSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 22),
    _CfprFabricFcSanPcType_Type()
)
cfprFabricFcSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcType.setStatus("current")
_CfprFabricFcSanPcWarnings_Type = CfprFabricWarnings
_CfprFabricFcSanPcWarnings_Object = MibTableColumn
cfprFabricFcSanPcWarnings = _CfprFabricFcSanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 57, 1, 23),
    _CfprFabricFcSanPcWarnings_Type()
)
cfprFabricFcSanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcWarnings.setStatus("current")
_CfprFabricFcSanPcEpTable_Object = MibTable
cfprFabricFcSanPcEpTable = _CfprFabricFcSanPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58)
)
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpTable.setStatus("current")
_CfprFabricFcSanPcEpEntry_Object = MibTableRow
cfprFabricFcSanPcEpEntry = _CfprFabricFcSanPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1)
)
cfprFabricFcSanPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcSanPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpEntry.setStatus("current")
_CfprFabricFcSanPcEpInstanceId_Type = CfprManagedObjectId
_CfprFabricFcSanPcEpInstanceId_Object = MibTableColumn
cfprFabricFcSanPcEpInstanceId = _CfprFabricFcSanPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 1),
    _CfprFabricFcSanPcEpInstanceId_Type()
)
cfprFabricFcSanPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpInstanceId.setStatus("current")
_CfprFabricFcSanPcEpDnData_Type = CfprManagedObjectDn
_CfprFabricFcSanPcEpDnData_Object = MibTableColumn
cfprFabricFcSanPcEpDnData = _CfprFabricFcSanPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 2),
    _CfprFabricFcSanPcEpDnData_Type()
)
cfprFabricFcSanPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpDnData.setStatus("current")
_CfprFabricFcSanPcEpRn_Type = SnmpAdminString
_CfprFabricFcSanPcEpRn_Object = MibTableColumn
cfprFabricFcSanPcEpRn = _CfprFabricFcSanPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 3),
    _CfprFabricFcSanPcEpRn_Type()
)
cfprFabricFcSanPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpRn.setStatus("current")
_CfprFabricFcSanPcEpAdminSpeed_Type = CfprPortSpeed
_CfprFabricFcSanPcEpAdminSpeed_Object = MibTableColumn
cfprFabricFcSanPcEpAdminSpeed = _CfprFabricFcSanPcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 4),
    _CfprFabricFcSanPcEpAdminSpeed_Type()
)
cfprFabricFcSanPcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpAdminSpeed.setStatus("current")
_CfprFabricFcSanPcEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricFcSanPcEpAdminState_Object = MibTableColumn
cfprFabricFcSanPcEpAdminState = _CfprFabricFcSanPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 5),
    _CfprFabricFcSanPcEpAdminState_Type()
)
cfprFabricFcSanPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpAdminState.setStatus("current")
_CfprFabricFcSanPcEpAggrPortId_Type = Gauge32
_CfprFabricFcSanPcEpAggrPortId_Object = MibTableColumn
cfprFabricFcSanPcEpAggrPortId = _CfprFabricFcSanPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 6),
    _CfprFabricFcSanPcEpAggrPortId_Type()
)
cfprFabricFcSanPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpAggrPortId.setStatus("current")
_CfprFabricFcSanPcEpChassisId_Type = Gauge32
_CfprFabricFcSanPcEpChassisId_Object = MibTableColumn
cfprFabricFcSanPcEpChassisId = _CfprFabricFcSanPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 7),
    _CfprFabricFcSanPcEpChassisId_Type()
)
cfprFabricFcSanPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpChassisId.setStatus("current")
_CfprFabricFcSanPcEpEpDn_Type = SnmpAdminString
_CfprFabricFcSanPcEpEpDn_Object = MibTableColumn
cfprFabricFcSanPcEpEpDn = _CfprFabricFcSanPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 8),
    _CfprFabricFcSanPcEpEpDn_Type()
)
cfprFabricFcSanPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpEpDn.setStatus("current")
_CfprFabricFcSanPcEpFillPattern_Type = CfprFabricFillPattern
_CfprFabricFcSanPcEpFillPattern_Object = MibTableColumn
cfprFabricFcSanPcEpFillPattern = _CfprFabricFcSanPcEpFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 9),
    _CfprFabricFcSanPcEpFillPattern_Type()
)
cfprFabricFcSanPcEpFillPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpFillPattern.setStatus("current")
_CfprFabricFcSanPcEpFltAggr_Type = Unsigned64
_CfprFabricFcSanPcEpFltAggr_Object = MibTableColumn
cfprFabricFcSanPcEpFltAggr = _CfprFabricFcSanPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 10),
    _CfprFabricFcSanPcEpFltAggr_Type()
)
cfprFabricFcSanPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpFltAggr.setStatus("current")
_CfprFabricFcSanPcEpIfRole_Type = CfprFabricSanEpIfRole
_CfprFabricFcSanPcEpIfRole_Object = MibTableColumn
cfprFabricFcSanPcEpIfRole = _CfprFabricFcSanPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 11),
    _CfprFabricFcSanPcEpIfRole_Type()
)
cfprFabricFcSanPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpIfRole.setStatus("current")
_CfprFabricFcSanPcEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricFcSanPcEpIfType_Object = MibTableColumn
cfprFabricFcSanPcEpIfType = _CfprFabricFcSanPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 12),
    _CfprFabricFcSanPcEpIfType_Type()
)
cfprFabricFcSanPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpIfType.setStatus("current")
_CfprFabricFcSanPcEpLicGP_Type = Unsigned64
_CfprFabricFcSanPcEpLicGP_Object = MibTableColumn
cfprFabricFcSanPcEpLicGP = _CfprFabricFcSanPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 13),
    _CfprFabricFcSanPcEpLicGP_Type()
)
cfprFabricFcSanPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpLicGP.setStatus("current")
_CfprFabricFcSanPcEpLicState_Type = CfprLicenseState
_CfprFabricFcSanPcEpLicState_Object = MibTableColumn
cfprFabricFcSanPcEpLicState = _CfprFabricFcSanPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 14),
    _CfprFabricFcSanPcEpLicState_Type()
)
cfprFabricFcSanPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpLicState.setStatus("current")
_CfprFabricFcSanPcEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricFcSanPcEpLocale_Object = MibTableColumn
cfprFabricFcSanPcEpLocale = _CfprFabricFcSanPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 15),
    _CfprFabricFcSanPcEpLocale_Type()
)
cfprFabricFcSanPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpLocale.setStatus("current")
_CfprFabricFcSanPcEpMembership_Type = CfprFabricMembershipStatus
_CfprFabricFcSanPcEpMembership_Object = MibTableColumn
cfprFabricFcSanPcEpMembership = _CfprFabricFcSanPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 16),
    _CfprFabricFcSanPcEpMembership_Type()
)
cfprFabricFcSanPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpMembership.setStatus("current")
_CfprFabricFcSanPcEpName_Type = SnmpAdminString
_CfprFabricFcSanPcEpName_Object = MibTableColumn
cfprFabricFcSanPcEpName = _CfprFabricFcSanPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 17),
    _CfprFabricFcSanPcEpName_Type()
)
cfprFabricFcSanPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpName.setStatus("current")
_CfprFabricFcSanPcEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricFcSanPcEpOperState_Object = MibTableColumn
cfprFabricFcSanPcEpOperState = _CfprFabricFcSanPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 18),
    _CfprFabricFcSanPcEpOperState_Type()
)
cfprFabricFcSanPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpOperState.setStatus("current")
_CfprFabricFcSanPcEpOperStateReason_Type = SnmpAdminString
_CfprFabricFcSanPcEpOperStateReason_Object = MibTableColumn
cfprFabricFcSanPcEpOperStateReason = _CfprFabricFcSanPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 19),
    _CfprFabricFcSanPcEpOperStateReason_Type()
)
cfprFabricFcSanPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpOperStateReason.setStatus("current")
_CfprFabricFcSanPcEpPeerAggrPortId_Type = Gauge32
_CfprFabricFcSanPcEpPeerAggrPortId_Object = MibTableColumn
cfprFabricFcSanPcEpPeerAggrPortId = _CfprFabricFcSanPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 20),
    _CfprFabricFcSanPcEpPeerAggrPortId_Type()
)
cfprFabricFcSanPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpPeerAggrPortId.setStatus("current")
_CfprFabricFcSanPcEpPeerChassisId_Type = Gauge32
_CfprFabricFcSanPcEpPeerChassisId_Object = MibTableColumn
cfprFabricFcSanPcEpPeerChassisId = _CfprFabricFcSanPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 21),
    _CfprFabricFcSanPcEpPeerChassisId_Type()
)
cfprFabricFcSanPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpPeerChassisId.setStatus("current")
_CfprFabricFcSanPcEpPeerDn_Type = SnmpAdminString
_CfprFabricFcSanPcEpPeerDn_Object = MibTableColumn
cfprFabricFcSanPcEpPeerDn = _CfprFabricFcSanPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 22),
    _CfprFabricFcSanPcEpPeerDn_Type()
)
cfprFabricFcSanPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpPeerDn.setStatus("current")
_CfprFabricFcSanPcEpPeerPortId_Type = Gauge32
_CfprFabricFcSanPcEpPeerPortId_Object = MibTableColumn
cfprFabricFcSanPcEpPeerPortId = _CfprFabricFcSanPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 23),
    _CfprFabricFcSanPcEpPeerPortId_Type()
)
cfprFabricFcSanPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpPeerPortId.setStatus("current")
_CfprFabricFcSanPcEpPeerSlotId_Type = Gauge32
_CfprFabricFcSanPcEpPeerSlotId_Object = MibTableColumn
cfprFabricFcSanPcEpPeerSlotId = _CfprFabricFcSanPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 24),
    _CfprFabricFcSanPcEpPeerSlotId_Type()
)
cfprFabricFcSanPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpPeerSlotId.setStatus("current")
_CfprFabricFcSanPcEpPortId_Type = CfprFabricFcSanPcEpPortId
_CfprFabricFcSanPcEpPortId_Object = MibTableColumn
cfprFabricFcSanPcEpPortId = _CfprFabricFcSanPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 25),
    _CfprFabricFcSanPcEpPortId_Type()
)
cfprFabricFcSanPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpPortId.setStatus("current")
_CfprFabricFcSanPcEpSlotId_Type = CfprFabricFcSanPcEpSlotId
_CfprFabricFcSanPcEpSlotId_Object = MibTableColumn
cfprFabricFcSanPcEpSlotId = _CfprFabricFcSanPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 26),
    _CfprFabricFcSanPcEpSlotId_Type()
)
cfprFabricFcSanPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpSlotId.setStatus("current")
_CfprFabricFcSanPcEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcSanPcEpSwitchId_Object = MibTableColumn
cfprFabricFcSanPcEpSwitchId = _CfprFabricFcSanPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 27),
    _CfprFabricFcSanPcEpSwitchId_Type()
)
cfprFabricFcSanPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpSwitchId.setStatus("current")
_CfprFabricFcSanPcEpTransport_Type = CfprFabricAFcSanEpTransport
_CfprFabricFcSanPcEpTransport_Object = MibTableColumn
cfprFabricFcSanPcEpTransport = _CfprFabricFcSanPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 28),
    _CfprFabricFcSanPcEpTransport_Type()
)
cfprFabricFcSanPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpTransport.setStatus("current")
_CfprFabricFcSanPcEpType_Type = CfprFabricSanEpType
_CfprFabricFcSanPcEpType_Object = MibTableColumn
cfprFabricFcSanPcEpType = _CfprFabricFcSanPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 29),
    _CfprFabricFcSanPcEpType_Type()
)
cfprFabricFcSanPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpType.setStatus("current")
_CfprFabricFcSanPcEpWarnings_Type = CfprFabricWarnings
_CfprFabricFcSanPcEpWarnings_Object = MibTableColumn
cfprFabricFcSanPcEpWarnings = _CfprFabricFcSanPcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 58, 1, 30),
    _CfprFabricFcSanPcEpWarnings_Type()
)
cfprFabricFcSanPcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcSanPcEpWarnings.setStatus("current")
_CfprFabricFcVsanPcTable_Object = MibTable
cfprFabricFcVsanPcTable = _CfprFabricFcVsanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59)
)
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcTable.setStatus("current")
_CfprFabricFcVsanPcEntry_Object = MibTableRow
cfprFabricFcVsanPcEntry = _CfprFabricFcVsanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1)
)
cfprFabricFcVsanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcVsanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcEntry.setStatus("current")
_CfprFabricFcVsanPcInstanceId_Type = CfprManagedObjectId
_CfprFabricFcVsanPcInstanceId_Object = MibTableColumn
cfprFabricFcVsanPcInstanceId = _CfprFabricFcVsanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 1),
    _CfprFabricFcVsanPcInstanceId_Type()
)
cfprFabricFcVsanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcInstanceId.setStatus("current")
_CfprFabricFcVsanPcDn_Type = CfprManagedObjectDn
_CfprFabricFcVsanPcDn_Object = MibTableColumn
cfprFabricFcVsanPcDn = _CfprFabricFcVsanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 2),
    _CfprFabricFcVsanPcDn_Type()
)
cfprFabricFcVsanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcDn.setStatus("current")
_CfprFabricFcVsanPcRn_Type = SnmpAdminString
_CfprFabricFcVsanPcRn_Object = MibTableColumn
cfprFabricFcVsanPcRn = _CfprFabricFcVsanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 3),
    _CfprFabricFcVsanPcRn_Type()
)
cfprFabricFcVsanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcRn.setStatus("current")
_CfprFabricFcVsanPcAdminState_Type = CfprFabricCIoEpAdminState
_CfprFabricFcVsanPcAdminState_Object = MibTableColumn
cfprFabricFcVsanPcAdminState = _CfprFabricFcVsanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 4),
    _CfprFabricFcVsanPcAdminState_Type()
)
cfprFabricFcVsanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcAdminState.setStatus("current")
_CfprFabricFcVsanPcDescr_Type = SnmpAdminString
_CfprFabricFcVsanPcDescr_Object = MibTableColumn
cfprFabricFcVsanPcDescr = _CfprFabricFcVsanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 5),
    _CfprFabricFcVsanPcDescr_Type()
)
cfprFabricFcVsanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcDescr.setStatus("current")
_CfprFabricFcVsanPcEpDn_Type = SnmpAdminString
_CfprFabricFcVsanPcEpDn_Object = MibTableColumn
cfprFabricFcVsanPcEpDn = _CfprFabricFcVsanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 6),
    _CfprFabricFcVsanPcEpDn_Type()
)
cfprFabricFcVsanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcEpDn.setStatus("current")
_CfprFabricFcVsanPcFltAggr_Type = Unsigned64
_CfprFabricFcVsanPcFltAggr_Object = MibTableColumn
cfprFabricFcVsanPcFltAggr = _CfprFabricFcVsanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 7),
    _CfprFabricFcVsanPcFltAggr_Type()
)
cfprFabricFcVsanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcFltAggr.setStatus("current")
_CfprFabricFcVsanPcIfRole_Type = CfprFabricSanPcIfRole
_CfprFabricFcVsanPcIfRole_Object = MibTableColumn
cfprFabricFcVsanPcIfRole = _CfprFabricFcVsanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 8),
    _CfprFabricFcVsanPcIfRole_Type()
)
cfprFabricFcVsanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcIfRole.setStatus("current")
_CfprFabricFcVsanPcIfType_Type = CfprFabricCIoEpIfType
_CfprFabricFcVsanPcIfType_Object = MibTableColumn
cfprFabricFcVsanPcIfType = _CfprFabricFcVsanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 9),
    _CfprFabricFcVsanPcIfType_Type()
)
cfprFabricFcVsanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcIfType.setStatus("current")
_CfprFabricFcVsanPcLocale_Type = CfprFabricExternalPcLocale
_CfprFabricFcVsanPcLocale_Object = MibTableColumn
cfprFabricFcVsanPcLocale = _CfprFabricFcVsanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 10),
    _CfprFabricFcVsanPcLocale_Type()
)
cfprFabricFcVsanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcLocale.setStatus("current")
_CfprFabricFcVsanPcName_Type = SnmpAdminString
_CfprFabricFcVsanPcName_Object = MibTableColumn
cfprFabricFcVsanPcName = _CfprFabricFcVsanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 11),
    _CfprFabricFcVsanPcName_Type()
)
cfprFabricFcVsanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcName.setStatus("current")
_CfprFabricFcVsanPcOperState_Type = CfprNetworkPortOperState
_CfprFabricFcVsanPcOperState_Object = MibTableColumn
cfprFabricFcVsanPcOperState = _CfprFabricFcVsanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 12),
    _CfprFabricFcVsanPcOperState_Type()
)
cfprFabricFcVsanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcOperState.setStatus("current")
_CfprFabricFcVsanPcPeerDn_Type = SnmpAdminString
_CfprFabricFcVsanPcPeerDn_Object = MibTableColumn
cfprFabricFcVsanPcPeerDn = _CfprFabricFcVsanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 13),
    _CfprFabricFcVsanPcPeerDn_Type()
)
cfprFabricFcVsanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcPeerDn.setStatus("current")
_CfprFabricFcVsanPcPortId_Type = Gauge32
_CfprFabricFcVsanPcPortId_Object = MibTableColumn
cfprFabricFcVsanPcPortId = _CfprFabricFcVsanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 14),
    _CfprFabricFcVsanPcPortId_Type()
)
cfprFabricFcVsanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcPortId.setStatus("current")
_CfprFabricFcVsanPcStateQual_Type = SnmpAdminString
_CfprFabricFcVsanPcStateQual_Object = MibTableColumn
cfprFabricFcVsanPcStateQual = _CfprFabricFcVsanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 15),
    _CfprFabricFcVsanPcStateQual_Type()
)
cfprFabricFcVsanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcStateQual.setStatus("current")
_CfprFabricFcVsanPcSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcVsanPcSwitchId_Object = MibTableColumn
cfprFabricFcVsanPcSwitchId = _CfprFabricFcVsanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 16),
    _CfprFabricFcVsanPcSwitchId_Type()
)
cfprFabricFcVsanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcSwitchId.setStatus("current")
_CfprFabricFcVsanPcTransport_Type = CfprFabricFcVsanPcTransport
_CfprFabricFcVsanPcTransport_Object = MibTableColumn
cfprFabricFcVsanPcTransport = _CfprFabricFcVsanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 17),
    _CfprFabricFcVsanPcTransport_Type()
)
cfprFabricFcVsanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcTransport.setStatus("current")
_CfprFabricFcVsanPcType_Type = CfprFabricSanPcType
_CfprFabricFcVsanPcType_Object = MibTableColumn
cfprFabricFcVsanPcType = _CfprFabricFcVsanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 18),
    _CfprFabricFcVsanPcType_Type()
)
cfprFabricFcVsanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcType.setStatus("current")
_CfprFabricFcVsanPcWarnings_Type = CfprFabricWarnings
_CfprFabricFcVsanPcWarnings_Object = MibTableColumn
cfprFabricFcVsanPcWarnings = _CfprFabricFcVsanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 59, 1, 19),
    _CfprFabricFcVsanPcWarnings_Type()
)
cfprFabricFcVsanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPcWarnings.setStatus("current")
_CfprFabricFcVsanPortEpTable_Object = MibTable
cfprFabricFcVsanPortEpTable = _CfprFabricFcVsanPortEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60)
)
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpTable.setStatus("current")
_CfprFabricFcVsanPortEpEntry_Object = MibTableRow
cfprFabricFcVsanPortEpEntry = _CfprFabricFcVsanPortEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1)
)
cfprFabricFcVsanPortEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcVsanPortEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpEntry.setStatus("current")
_CfprFabricFcVsanPortEpInstanceId_Type = CfprManagedObjectId
_CfprFabricFcVsanPortEpInstanceId_Object = MibTableColumn
cfprFabricFcVsanPortEpInstanceId = _CfprFabricFcVsanPortEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 1),
    _CfprFabricFcVsanPortEpInstanceId_Type()
)
cfprFabricFcVsanPortEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpInstanceId.setStatus("current")
_CfprFabricFcVsanPortEpDn_Type = CfprManagedObjectDn
_CfprFabricFcVsanPortEpDn_Object = MibTableColumn
cfprFabricFcVsanPortEpDn = _CfprFabricFcVsanPortEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 2),
    _CfprFabricFcVsanPortEpDn_Type()
)
cfprFabricFcVsanPortEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpDn.setStatus("current")
_CfprFabricFcVsanPortEpRn_Type = SnmpAdminString
_CfprFabricFcVsanPortEpRn_Object = MibTableColumn
cfprFabricFcVsanPortEpRn = _CfprFabricFcVsanPortEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 3),
    _CfprFabricFcVsanPortEpRn_Type()
)
cfprFabricFcVsanPortEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpRn.setStatus("current")
_CfprFabricFcVsanPortEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricFcVsanPortEpAdminState_Object = MibTableColumn
cfprFabricFcVsanPortEpAdminState = _CfprFabricFcVsanPortEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 4),
    _CfprFabricFcVsanPortEpAdminState_Type()
)
cfprFabricFcVsanPortEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpAdminState.setStatus("current")
_CfprFabricFcVsanPortEpAggrPortId_Type = Gauge32
_CfprFabricFcVsanPortEpAggrPortId_Object = MibTableColumn
cfprFabricFcVsanPortEpAggrPortId = _CfprFabricFcVsanPortEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 5),
    _CfprFabricFcVsanPortEpAggrPortId_Type()
)
cfprFabricFcVsanPortEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpAggrPortId.setStatus("current")
_CfprFabricFcVsanPortEpChassisId_Type = Gauge32
_CfprFabricFcVsanPortEpChassisId_Object = MibTableColumn
cfprFabricFcVsanPortEpChassisId = _CfprFabricFcVsanPortEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 6),
    _CfprFabricFcVsanPortEpChassisId_Type()
)
cfprFabricFcVsanPortEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpChassisId.setStatus("current")
_CfprFabricFcVsanPortEpEpDn_Type = SnmpAdminString
_CfprFabricFcVsanPortEpEpDn_Object = MibTableColumn
cfprFabricFcVsanPortEpEpDn = _CfprFabricFcVsanPortEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 7),
    _CfprFabricFcVsanPortEpEpDn_Type()
)
cfprFabricFcVsanPortEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpEpDn.setStatus("current")
_CfprFabricFcVsanPortEpFltAggr_Type = Unsigned64
_CfprFabricFcVsanPortEpFltAggr_Object = MibTableColumn
cfprFabricFcVsanPortEpFltAggr = _CfprFabricFcVsanPortEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 8),
    _CfprFabricFcVsanPortEpFltAggr_Type()
)
cfprFabricFcVsanPortEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpFltAggr.setStatus("current")
_CfprFabricFcVsanPortEpIfRole_Type = CfprFabricSanEpIfRole
_CfprFabricFcVsanPortEpIfRole_Object = MibTableColumn
cfprFabricFcVsanPortEpIfRole = _CfprFabricFcVsanPortEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 9),
    _CfprFabricFcVsanPortEpIfRole_Type()
)
cfprFabricFcVsanPortEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpIfRole.setStatus("current")
_CfprFabricFcVsanPortEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricFcVsanPortEpIfType_Object = MibTableColumn
cfprFabricFcVsanPortEpIfType = _CfprFabricFcVsanPortEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 10),
    _CfprFabricFcVsanPortEpIfType_Type()
)
cfprFabricFcVsanPortEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpIfType.setStatus("current")
_CfprFabricFcVsanPortEpLicGP_Type = Unsigned64
_CfprFabricFcVsanPortEpLicGP_Object = MibTableColumn
cfprFabricFcVsanPortEpLicGP = _CfprFabricFcVsanPortEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 11),
    _CfprFabricFcVsanPortEpLicGP_Type()
)
cfprFabricFcVsanPortEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpLicGP.setStatus("current")
_CfprFabricFcVsanPortEpLicState_Type = CfprLicenseState
_CfprFabricFcVsanPortEpLicState_Object = MibTableColumn
cfprFabricFcVsanPortEpLicState = _CfprFabricFcVsanPortEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 12),
    _CfprFabricFcVsanPortEpLicState_Type()
)
cfprFabricFcVsanPortEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpLicState.setStatus("current")
_CfprFabricFcVsanPortEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricFcVsanPortEpLocale_Object = MibTableColumn
cfprFabricFcVsanPortEpLocale = _CfprFabricFcVsanPortEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 13),
    _CfprFabricFcVsanPortEpLocale_Type()
)
cfprFabricFcVsanPortEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpLocale.setStatus("current")
_CfprFabricFcVsanPortEpName_Type = SnmpAdminString
_CfprFabricFcVsanPortEpName_Object = MibTableColumn
cfprFabricFcVsanPortEpName = _CfprFabricFcVsanPortEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 14),
    _CfprFabricFcVsanPortEpName_Type()
)
cfprFabricFcVsanPortEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpName.setStatus("current")
_CfprFabricFcVsanPortEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricFcVsanPortEpOperState_Object = MibTableColumn
cfprFabricFcVsanPortEpOperState = _CfprFabricFcVsanPortEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 15),
    _CfprFabricFcVsanPortEpOperState_Type()
)
cfprFabricFcVsanPortEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpOperState.setStatus("current")
_CfprFabricFcVsanPortEpOperStateReason_Type = SnmpAdminString
_CfprFabricFcVsanPortEpOperStateReason_Object = MibTableColumn
cfprFabricFcVsanPortEpOperStateReason = _CfprFabricFcVsanPortEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 16),
    _CfprFabricFcVsanPortEpOperStateReason_Type()
)
cfprFabricFcVsanPortEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpOperStateReason.setStatus("current")
_CfprFabricFcVsanPortEpPeerAggrPortId_Type = Gauge32
_CfprFabricFcVsanPortEpPeerAggrPortId_Object = MibTableColumn
cfprFabricFcVsanPortEpPeerAggrPortId = _CfprFabricFcVsanPortEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 17),
    _CfprFabricFcVsanPortEpPeerAggrPortId_Type()
)
cfprFabricFcVsanPortEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpPeerAggrPortId.setStatus("current")
_CfprFabricFcVsanPortEpPeerChassisId_Type = Gauge32
_CfprFabricFcVsanPortEpPeerChassisId_Object = MibTableColumn
cfprFabricFcVsanPortEpPeerChassisId = _CfprFabricFcVsanPortEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 18),
    _CfprFabricFcVsanPortEpPeerChassisId_Type()
)
cfprFabricFcVsanPortEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpPeerChassisId.setStatus("current")
_CfprFabricFcVsanPortEpPeerDn_Type = SnmpAdminString
_CfprFabricFcVsanPortEpPeerDn_Object = MibTableColumn
cfprFabricFcVsanPortEpPeerDn = _CfprFabricFcVsanPortEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 19),
    _CfprFabricFcVsanPortEpPeerDn_Type()
)
cfprFabricFcVsanPortEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpPeerDn.setStatus("current")
_CfprFabricFcVsanPortEpPeerPortId_Type = Gauge32
_CfprFabricFcVsanPortEpPeerPortId_Object = MibTableColumn
cfprFabricFcVsanPortEpPeerPortId = _CfprFabricFcVsanPortEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 20),
    _CfprFabricFcVsanPortEpPeerPortId_Type()
)
cfprFabricFcVsanPortEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpPeerPortId.setStatus("current")
_CfprFabricFcVsanPortEpPeerSlotId_Type = Gauge32
_CfprFabricFcVsanPortEpPeerSlotId_Object = MibTableColumn
cfprFabricFcVsanPortEpPeerSlotId = _CfprFabricFcVsanPortEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 21),
    _CfprFabricFcVsanPortEpPeerSlotId_Type()
)
cfprFabricFcVsanPortEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpPeerSlotId.setStatus("current")
_CfprFabricFcVsanPortEpPortId_Type = CfprFabricFcVsanPortEpPortId
_CfprFabricFcVsanPortEpPortId_Object = MibTableColumn
cfprFabricFcVsanPortEpPortId = _CfprFabricFcVsanPortEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 22),
    _CfprFabricFcVsanPortEpPortId_Type()
)
cfprFabricFcVsanPortEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpPortId.setStatus("current")
_CfprFabricFcVsanPortEpSlotId_Type = CfprFabricFcVsanPortEpSlotId
_CfprFabricFcVsanPortEpSlotId_Object = MibTableColumn
cfprFabricFcVsanPortEpSlotId = _CfprFabricFcVsanPortEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 23),
    _CfprFabricFcVsanPortEpSlotId_Type()
)
cfprFabricFcVsanPortEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpSlotId.setStatus("current")
_CfprFabricFcVsanPortEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcVsanPortEpSwitchId_Object = MibTableColumn
cfprFabricFcVsanPortEpSwitchId = _CfprFabricFcVsanPortEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 24),
    _CfprFabricFcVsanPortEpSwitchId_Type()
)
cfprFabricFcVsanPortEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpSwitchId.setStatus("current")
_CfprFabricFcVsanPortEpTransport_Type = CfprFabricAFcSanEpTransport
_CfprFabricFcVsanPortEpTransport_Object = MibTableColumn
cfprFabricFcVsanPortEpTransport = _CfprFabricFcVsanPortEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 25),
    _CfprFabricFcVsanPortEpTransport_Type()
)
cfprFabricFcVsanPortEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpTransport.setStatus("current")
_CfprFabricFcVsanPortEpType_Type = CfprFabricSanEpType
_CfprFabricFcVsanPortEpType_Object = MibTableColumn
cfprFabricFcVsanPortEpType = _CfprFabricFcVsanPortEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 26),
    _CfprFabricFcVsanPortEpType_Type()
)
cfprFabricFcVsanPortEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpType.setStatus("current")
_CfprFabricFcVsanPortEpWarnings_Type = CfprFabricWarnings
_CfprFabricFcVsanPortEpWarnings_Object = MibTableColumn
cfprFabricFcVsanPortEpWarnings = _CfprFabricFcVsanPortEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 60, 1, 27),
    _CfprFabricFcVsanPortEpWarnings_Type()
)
cfprFabricFcVsanPortEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcVsanPortEpWarnings.setStatus("current")
_CfprFabricFcoeSanEpTable_Object = MibTable
cfprFabricFcoeSanEpTable = _CfprFabricFcoeSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62)
)
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpTable.setStatus("current")
_CfprFabricFcoeSanEpEntry_Object = MibTableRow
cfprFabricFcoeSanEpEntry = _CfprFabricFcoeSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1)
)
cfprFabricFcoeSanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcoeSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpEntry.setStatus("current")
_CfprFabricFcoeSanEpInstanceId_Type = CfprManagedObjectId
_CfprFabricFcoeSanEpInstanceId_Object = MibTableColumn
cfprFabricFcoeSanEpInstanceId = _CfprFabricFcoeSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 1),
    _CfprFabricFcoeSanEpInstanceId_Type()
)
cfprFabricFcoeSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpInstanceId.setStatus("current")
_CfprFabricFcoeSanEpDn_Type = CfprManagedObjectDn
_CfprFabricFcoeSanEpDn_Object = MibTableColumn
cfprFabricFcoeSanEpDn = _CfprFabricFcoeSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 2),
    _CfprFabricFcoeSanEpDn_Type()
)
cfprFabricFcoeSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpDn.setStatus("current")
_CfprFabricFcoeSanEpRn_Type = SnmpAdminString
_CfprFabricFcoeSanEpRn_Object = MibTableColumn
cfprFabricFcoeSanEpRn = _CfprFabricFcoeSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 3),
    _CfprFabricFcoeSanEpRn_Type()
)
cfprFabricFcoeSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpRn.setStatus("current")
_CfprFabricFcoeSanEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricFcoeSanEpAdminState_Object = MibTableColumn
cfprFabricFcoeSanEpAdminState = _CfprFabricFcoeSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 4),
    _CfprFabricFcoeSanEpAdminState_Type()
)
cfprFabricFcoeSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpAdminState.setStatus("current")
_CfprFabricFcoeSanEpAggrPortId_Type = Gauge32
_CfprFabricFcoeSanEpAggrPortId_Object = MibTableColumn
cfprFabricFcoeSanEpAggrPortId = _CfprFabricFcoeSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 5),
    _CfprFabricFcoeSanEpAggrPortId_Type()
)
cfprFabricFcoeSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpAggrPortId.setStatus("current")
_CfprFabricFcoeSanEpChassisId_Type = Gauge32
_CfprFabricFcoeSanEpChassisId_Object = MibTableColumn
cfprFabricFcoeSanEpChassisId = _CfprFabricFcoeSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 6),
    _CfprFabricFcoeSanEpChassisId_Type()
)
cfprFabricFcoeSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpChassisId.setStatus("current")
_CfprFabricFcoeSanEpConfigState_Type = CfprFabricConfigState
_CfprFabricFcoeSanEpConfigState_Object = MibTableColumn
cfprFabricFcoeSanEpConfigState = _CfprFabricFcoeSanEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 7),
    _CfprFabricFcoeSanEpConfigState_Type()
)
cfprFabricFcoeSanEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpConfigState.setStatus("current")
_CfprFabricFcoeSanEpEpDn_Type = SnmpAdminString
_CfprFabricFcoeSanEpEpDn_Object = MibTableColumn
cfprFabricFcoeSanEpEpDn = _CfprFabricFcoeSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 8),
    _CfprFabricFcoeSanEpEpDn_Type()
)
cfprFabricFcoeSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpEpDn.setStatus("current")
_CfprFabricFcoeSanEpEthLinkProfileName_Type = SnmpAdminString
_CfprFabricFcoeSanEpEthLinkProfileName_Object = MibTableColumn
cfprFabricFcoeSanEpEthLinkProfileName = _CfprFabricFcoeSanEpEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 9),
    _CfprFabricFcoeSanEpEthLinkProfileName_Type()
)
cfprFabricFcoeSanEpEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpEthLinkProfileName.setStatus("current")
_CfprFabricFcoeSanEpFcoeState_Type = CfprNetworkPortOperState
_CfprFabricFcoeSanEpFcoeState_Object = MibTableColumn
cfprFabricFcoeSanEpFcoeState = _CfprFabricFcoeSanEpFcoeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 10),
    _CfprFabricFcoeSanEpFcoeState_Type()
)
cfprFabricFcoeSanEpFcoeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpFcoeState.setStatus("current")
_CfprFabricFcoeSanEpFcoeStateReason_Type = SnmpAdminString
_CfprFabricFcoeSanEpFcoeStateReason_Object = MibTableColumn
cfprFabricFcoeSanEpFcoeStateReason = _CfprFabricFcoeSanEpFcoeStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 11),
    _CfprFabricFcoeSanEpFcoeStateReason_Type()
)
cfprFabricFcoeSanEpFcoeStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpFcoeStateReason.setStatus("current")
_CfprFabricFcoeSanEpFltAggr_Type = Unsigned64
_CfprFabricFcoeSanEpFltAggr_Object = MibTableColumn
cfprFabricFcoeSanEpFltAggr = _CfprFabricFcoeSanEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 12),
    _CfprFabricFcoeSanEpFltAggr_Type()
)
cfprFabricFcoeSanEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpFltAggr.setStatus("current")
_CfprFabricFcoeSanEpIfRole_Type = CfprFabricSanEpIfRole
_CfprFabricFcoeSanEpIfRole_Object = MibTableColumn
cfprFabricFcoeSanEpIfRole = _CfprFabricFcoeSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 13),
    _CfprFabricFcoeSanEpIfRole_Type()
)
cfprFabricFcoeSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpIfRole.setStatus("current")
_CfprFabricFcoeSanEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricFcoeSanEpIfType_Object = MibTableColumn
cfprFabricFcoeSanEpIfType = _CfprFabricFcoeSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 14),
    _CfprFabricFcoeSanEpIfType_Type()
)
cfprFabricFcoeSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpIfType.setStatus("current")
_CfprFabricFcoeSanEpLicGP_Type = Unsigned64
_CfprFabricFcoeSanEpLicGP_Object = MibTableColumn
cfprFabricFcoeSanEpLicGP = _CfprFabricFcoeSanEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 15),
    _CfprFabricFcoeSanEpLicGP_Type()
)
cfprFabricFcoeSanEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpLicGP.setStatus("current")
_CfprFabricFcoeSanEpLicState_Type = CfprLicenseState
_CfprFabricFcoeSanEpLicState_Object = MibTableColumn
cfprFabricFcoeSanEpLicState = _CfprFabricFcoeSanEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 16),
    _CfprFabricFcoeSanEpLicState_Type()
)
cfprFabricFcoeSanEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpLicState.setStatus("current")
_CfprFabricFcoeSanEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricFcoeSanEpLocale_Object = MibTableColumn
cfprFabricFcoeSanEpLocale = _CfprFabricFcoeSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 17),
    _CfprFabricFcoeSanEpLocale_Type()
)
cfprFabricFcoeSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpLocale.setStatus("current")
_CfprFabricFcoeSanEpName_Type = SnmpAdminString
_CfprFabricFcoeSanEpName_Object = MibTableColumn
cfprFabricFcoeSanEpName = _CfprFabricFcoeSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 18),
    _CfprFabricFcoeSanEpName_Type()
)
cfprFabricFcoeSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpName.setStatus("current")
_CfprFabricFcoeSanEpOperEthLinkProfileName_Type = SnmpAdminString
_CfprFabricFcoeSanEpOperEthLinkProfileName_Object = MibTableColumn
cfprFabricFcoeSanEpOperEthLinkProfileName = _CfprFabricFcoeSanEpOperEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 19),
    _CfprFabricFcoeSanEpOperEthLinkProfileName_Type()
)
cfprFabricFcoeSanEpOperEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpOperEthLinkProfileName.setStatus("current")
_CfprFabricFcoeSanEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricFcoeSanEpOperState_Object = MibTableColumn
cfprFabricFcoeSanEpOperState = _CfprFabricFcoeSanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 20),
    _CfprFabricFcoeSanEpOperState_Type()
)
cfprFabricFcoeSanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpOperState.setStatus("current")
_CfprFabricFcoeSanEpOperStateReason_Type = SnmpAdminString
_CfprFabricFcoeSanEpOperStateReason_Object = MibTableColumn
cfprFabricFcoeSanEpOperStateReason = _CfprFabricFcoeSanEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 21),
    _CfprFabricFcoeSanEpOperStateReason_Type()
)
cfprFabricFcoeSanEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpOperStateReason.setStatus("current")
_CfprFabricFcoeSanEpPeerAggrPortId_Type = Gauge32
_CfprFabricFcoeSanEpPeerAggrPortId_Object = MibTableColumn
cfprFabricFcoeSanEpPeerAggrPortId = _CfprFabricFcoeSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 22),
    _CfprFabricFcoeSanEpPeerAggrPortId_Type()
)
cfprFabricFcoeSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpPeerAggrPortId.setStatus("current")
_CfprFabricFcoeSanEpPeerChassisId_Type = Gauge32
_CfprFabricFcoeSanEpPeerChassisId_Object = MibTableColumn
cfprFabricFcoeSanEpPeerChassisId = _CfprFabricFcoeSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 23),
    _CfprFabricFcoeSanEpPeerChassisId_Type()
)
cfprFabricFcoeSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpPeerChassisId.setStatus("current")
_CfprFabricFcoeSanEpPeerDn_Type = SnmpAdminString
_CfprFabricFcoeSanEpPeerDn_Object = MibTableColumn
cfprFabricFcoeSanEpPeerDn = _CfprFabricFcoeSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 24),
    _CfprFabricFcoeSanEpPeerDn_Type()
)
cfprFabricFcoeSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpPeerDn.setStatus("current")
_CfprFabricFcoeSanEpPeerPortId_Type = Gauge32
_CfprFabricFcoeSanEpPeerPortId_Object = MibTableColumn
cfprFabricFcoeSanEpPeerPortId = _CfprFabricFcoeSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 25),
    _CfprFabricFcoeSanEpPeerPortId_Type()
)
cfprFabricFcoeSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpPeerPortId.setStatus("current")
_CfprFabricFcoeSanEpPeerSlotId_Type = Gauge32
_CfprFabricFcoeSanEpPeerSlotId_Object = MibTableColumn
cfprFabricFcoeSanEpPeerSlotId = _CfprFabricFcoeSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 26),
    _CfprFabricFcoeSanEpPeerSlotId_Type()
)
cfprFabricFcoeSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpPeerSlotId.setStatus("current")
_CfprFabricFcoeSanEpPortId_Type = CfprFabricFcoeSanEpPortId
_CfprFabricFcoeSanEpPortId_Object = MibTableColumn
cfprFabricFcoeSanEpPortId = _CfprFabricFcoeSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 27),
    _CfprFabricFcoeSanEpPortId_Type()
)
cfprFabricFcoeSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpPortId.setStatus("current")
_CfprFabricFcoeSanEpSlotId_Type = CfprFabricFcoeSanEpSlotId
_CfprFabricFcoeSanEpSlotId_Object = MibTableColumn
cfprFabricFcoeSanEpSlotId = _CfprFabricFcoeSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 28),
    _CfprFabricFcoeSanEpSlotId_Type()
)
cfprFabricFcoeSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpSlotId.setStatus("current")
_CfprFabricFcoeSanEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcoeSanEpSwitchId_Object = MibTableColumn
cfprFabricFcoeSanEpSwitchId = _CfprFabricFcoeSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 29),
    _CfprFabricFcoeSanEpSwitchId_Type()
)
cfprFabricFcoeSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpSwitchId.setStatus("current")
_CfprFabricFcoeSanEpTransport_Type = CfprFabricAFcoeSanEpTransport
_CfprFabricFcoeSanEpTransport_Object = MibTableColumn
cfprFabricFcoeSanEpTransport = _CfprFabricFcoeSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 30),
    _CfprFabricFcoeSanEpTransport_Type()
)
cfprFabricFcoeSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpTransport.setStatus("current")
_CfprFabricFcoeSanEpType_Type = CfprFabricSanEpType
_CfprFabricFcoeSanEpType_Object = MibTableColumn
cfprFabricFcoeSanEpType = _CfprFabricFcoeSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 31),
    _CfprFabricFcoeSanEpType_Type()
)
cfprFabricFcoeSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpType.setStatus("current")
_CfprFabricFcoeSanEpUdldOperState_Type = CfprFabricUdldOperState
_CfprFabricFcoeSanEpUdldOperState_Object = MibTableColumn
cfprFabricFcoeSanEpUdldOperState = _CfprFabricFcoeSanEpUdldOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 32),
    _CfprFabricFcoeSanEpUdldOperState_Type()
)
cfprFabricFcoeSanEpUdldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpUdldOperState.setStatus("current")
_CfprFabricFcoeSanEpUsrLbl_Type = SnmpAdminString
_CfprFabricFcoeSanEpUsrLbl_Object = MibTableColumn
cfprFabricFcoeSanEpUsrLbl = _CfprFabricFcoeSanEpUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 33),
    _CfprFabricFcoeSanEpUsrLbl_Type()
)
cfprFabricFcoeSanEpUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpUsrLbl.setStatus("current")
_CfprFabricFcoeSanEpWarnings_Type = CfprFabricWarnings
_CfprFabricFcoeSanEpWarnings_Object = MibTableColumn
cfprFabricFcoeSanEpWarnings = _CfprFabricFcoeSanEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 62, 1, 34),
    _CfprFabricFcoeSanEpWarnings_Type()
)
cfprFabricFcoeSanEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanEpWarnings.setStatus("current")
_CfprFabricFcoeSanPcTable_Object = MibTable
cfprFabricFcoeSanPcTable = _CfprFabricFcoeSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63)
)
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcTable.setStatus("current")
_CfprFabricFcoeSanPcEntry_Object = MibTableRow
cfprFabricFcoeSanPcEntry = _CfprFabricFcoeSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1)
)
cfprFabricFcoeSanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcoeSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEntry.setStatus("current")
_CfprFabricFcoeSanPcInstanceId_Type = CfprManagedObjectId
_CfprFabricFcoeSanPcInstanceId_Object = MibTableColumn
cfprFabricFcoeSanPcInstanceId = _CfprFabricFcoeSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 1),
    _CfprFabricFcoeSanPcInstanceId_Type()
)
cfprFabricFcoeSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcInstanceId.setStatus("current")
_CfprFabricFcoeSanPcDn_Type = CfprManagedObjectDn
_CfprFabricFcoeSanPcDn_Object = MibTableColumn
cfprFabricFcoeSanPcDn = _CfprFabricFcoeSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 2),
    _CfprFabricFcoeSanPcDn_Type()
)
cfprFabricFcoeSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcDn.setStatus("current")
_CfprFabricFcoeSanPcRn_Type = SnmpAdminString
_CfprFabricFcoeSanPcRn_Object = MibTableColumn
cfprFabricFcoeSanPcRn = _CfprFabricFcoeSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 3),
    _CfprFabricFcoeSanPcRn_Type()
)
cfprFabricFcoeSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcRn.setStatus("current")
_CfprFabricFcoeSanPcAdminState_Type = CfprFabricCIoEpAdminState
_CfprFabricFcoeSanPcAdminState_Object = MibTableColumn
cfprFabricFcoeSanPcAdminState = _CfprFabricFcoeSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 4),
    _CfprFabricFcoeSanPcAdminState_Type()
)
cfprFabricFcoeSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcAdminState.setStatus("current")
_CfprFabricFcoeSanPcConfigState_Type = CfprFabricConfigState
_CfprFabricFcoeSanPcConfigState_Object = MibTableColumn
cfprFabricFcoeSanPcConfigState = _CfprFabricFcoeSanPcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 5),
    _CfprFabricFcoeSanPcConfigState_Type()
)
cfprFabricFcoeSanPcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcConfigState.setStatus("current")
_CfprFabricFcoeSanPcDescr_Type = SnmpAdminString
_CfprFabricFcoeSanPcDescr_Object = MibTableColumn
cfprFabricFcoeSanPcDescr = _CfprFabricFcoeSanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 6),
    _CfprFabricFcoeSanPcDescr_Type()
)
cfprFabricFcoeSanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcDescr.setStatus("current")
_CfprFabricFcoeSanPcEpDn_Type = SnmpAdminString
_CfprFabricFcoeSanPcEpDn_Object = MibTableColumn
cfprFabricFcoeSanPcEpDn = _CfprFabricFcoeSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 7),
    _CfprFabricFcoeSanPcEpDn_Type()
)
cfprFabricFcoeSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpDn.setStatus("current")
_CfprFabricFcoeSanPcFcoeState_Type = CfprNetworkPortOperState
_CfprFabricFcoeSanPcFcoeState_Object = MibTableColumn
cfprFabricFcoeSanPcFcoeState = _CfprFabricFcoeSanPcFcoeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 8),
    _CfprFabricFcoeSanPcFcoeState_Type()
)
cfprFabricFcoeSanPcFcoeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcFcoeState.setStatus("current")
_CfprFabricFcoeSanPcFcoeStateReason_Type = SnmpAdminString
_CfprFabricFcoeSanPcFcoeStateReason_Object = MibTableColumn
cfprFabricFcoeSanPcFcoeStateReason = _CfprFabricFcoeSanPcFcoeStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 9),
    _CfprFabricFcoeSanPcFcoeStateReason_Type()
)
cfprFabricFcoeSanPcFcoeStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcFcoeStateReason.setStatus("current")
_CfprFabricFcoeSanPcFltAggr_Type = Unsigned64
_CfprFabricFcoeSanPcFltAggr_Object = MibTableColumn
cfprFabricFcoeSanPcFltAggr = _CfprFabricFcoeSanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 10),
    _CfprFabricFcoeSanPcFltAggr_Type()
)
cfprFabricFcoeSanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcFltAggr.setStatus("current")
_CfprFabricFcoeSanPcIfRole_Type = CfprFabricSanPcIfRole
_CfprFabricFcoeSanPcIfRole_Object = MibTableColumn
cfprFabricFcoeSanPcIfRole = _CfprFabricFcoeSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 11),
    _CfprFabricFcoeSanPcIfRole_Type()
)
cfprFabricFcoeSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcIfRole.setStatus("current")
_CfprFabricFcoeSanPcIfType_Type = CfprFabricCIoEpIfType
_CfprFabricFcoeSanPcIfType_Object = MibTableColumn
cfprFabricFcoeSanPcIfType = _CfprFabricFcoeSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 12),
    _CfprFabricFcoeSanPcIfType_Type()
)
cfprFabricFcoeSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcIfType.setStatus("current")
_CfprFabricFcoeSanPcLacpPolicyName_Type = SnmpAdminString
_CfprFabricFcoeSanPcLacpPolicyName_Object = MibTableColumn
cfprFabricFcoeSanPcLacpPolicyName = _CfprFabricFcoeSanPcLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 13),
    _CfprFabricFcoeSanPcLacpPolicyName_Type()
)
cfprFabricFcoeSanPcLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcLacpPolicyName.setStatus("current")
_CfprFabricFcoeSanPcLocale_Type = CfprFabricExternalPcLocale
_CfprFabricFcoeSanPcLocale_Object = MibTableColumn
cfprFabricFcoeSanPcLocale = _CfprFabricFcoeSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 14),
    _CfprFabricFcoeSanPcLocale_Type()
)
cfprFabricFcoeSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcLocale.setStatus("current")
_CfprFabricFcoeSanPcName_Type = SnmpAdminString
_CfprFabricFcoeSanPcName_Object = MibTableColumn
cfprFabricFcoeSanPcName = _CfprFabricFcoeSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 15),
    _CfprFabricFcoeSanPcName_Type()
)
cfprFabricFcoeSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcName.setStatus("current")
_CfprFabricFcoeSanPcOperLacpPolicyName_Type = SnmpAdminString
_CfprFabricFcoeSanPcOperLacpPolicyName_Object = MibTableColumn
cfprFabricFcoeSanPcOperLacpPolicyName = _CfprFabricFcoeSanPcOperLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 16),
    _CfprFabricFcoeSanPcOperLacpPolicyName_Type()
)
cfprFabricFcoeSanPcOperLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcOperLacpPolicyName.setStatus("current")
_CfprFabricFcoeSanPcOperState_Type = CfprNetworkPortOperState
_CfprFabricFcoeSanPcOperState_Object = MibTableColumn
cfprFabricFcoeSanPcOperState = _CfprFabricFcoeSanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 17),
    _CfprFabricFcoeSanPcOperState_Type()
)
cfprFabricFcoeSanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcOperState.setStatus("current")
_CfprFabricFcoeSanPcPeerDn_Type = SnmpAdminString
_CfprFabricFcoeSanPcPeerDn_Object = MibTableColumn
cfprFabricFcoeSanPcPeerDn = _CfprFabricFcoeSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 18),
    _CfprFabricFcoeSanPcPeerDn_Type()
)
cfprFabricFcoeSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcPeerDn.setStatus("current")
_CfprFabricFcoeSanPcPortId_Type = Gauge32
_CfprFabricFcoeSanPcPortId_Object = MibTableColumn
cfprFabricFcoeSanPcPortId = _CfprFabricFcoeSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 19),
    _CfprFabricFcoeSanPcPortId_Type()
)
cfprFabricFcoeSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcPortId.setStatus("current")
_CfprFabricFcoeSanPcStateQual_Type = SnmpAdminString
_CfprFabricFcoeSanPcStateQual_Object = MibTableColumn
cfprFabricFcoeSanPcStateQual = _CfprFabricFcoeSanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 20),
    _CfprFabricFcoeSanPcStateQual_Type()
)
cfprFabricFcoeSanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcStateQual.setStatus("current")
_CfprFabricFcoeSanPcSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcoeSanPcSwitchId_Object = MibTableColumn
cfprFabricFcoeSanPcSwitchId = _CfprFabricFcoeSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 21),
    _CfprFabricFcoeSanPcSwitchId_Type()
)
cfprFabricFcoeSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcSwitchId.setStatus("current")
_CfprFabricFcoeSanPcTransport_Type = CfprFabricFcoeSanPcTransport
_CfprFabricFcoeSanPcTransport_Object = MibTableColumn
cfprFabricFcoeSanPcTransport = _CfprFabricFcoeSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 22),
    _CfprFabricFcoeSanPcTransport_Type()
)
cfprFabricFcoeSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcTransport.setStatus("current")
_CfprFabricFcoeSanPcType_Type = CfprFabricSanPcType
_CfprFabricFcoeSanPcType_Object = MibTableColumn
cfprFabricFcoeSanPcType = _CfprFabricFcoeSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 23),
    _CfprFabricFcoeSanPcType_Type()
)
cfprFabricFcoeSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcType.setStatus("current")
_CfprFabricFcoeSanPcWarnings_Type = CfprFabricWarnings
_CfprFabricFcoeSanPcWarnings_Object = MibTableColumn
cfprFabricFcoeSanPcWarnings = _CfprFabricFcoeSanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 63, 1, 24),
    _CfprFabricFcoeSanPcWarnings_Type()
)
cfprFabricFcoeSanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcWarnings.setStatus("current")
_CfprFabricFcoeSanPcEpTable_Object = MibTable
cfprFabricFcoeSanPcEpTable = _CfprFabricFcoeSanPcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64)
)
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpTable.setStatus("current")
_CfprFabricFcoeSanPcEpEntry_Object = MibTableRow
cfprFabricFcoeSanPcEpEntry = _CfprFabricFcoeSanPcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1)
)
cfprFabricFcoeSanPcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcoeSanPcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpEntry.setStatus("current")
_CfprFabricFcoeSanPcEpInstanceId_Type = CfprManagedObjectId
_CfprFabricFcoeSanPcEpInstanceId_Object = MibTableColumn
cfprFabricFcoeSanPcEpInstanceId = _CfprFabricFcoeSanPcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 1),
    _CfprFabricFcoeSanPcEpInstanceId_Type()
)
cfprFabricFcoeSanPcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpInstanceId.setStatus("current")
_CfprFabricFcoeSanPcEpDnData_Type = CfprManagedObjectDn
_CfprFabricFcoeSanPcEpDnData_Object = MibTableColumn
cfprFabricFcoeSanPcEpDnData = _CfprFabricFcoeSanPcEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 2),
    _CfprFabricFcoeSanPcEpDnData_Type()
)
cfprFabricFcoeSanPcEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpDnData.setStatus("current")
_CfprFabricFcoeSanPcEpRn_Type = SnmpAdminString
_CfprFabricFcoeSanPcEpRn_Object = MibTableColumn
cfprFabricFcoeSanPcEpRn = _CfprFabricFcoeSanPcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 3),
    _CfprFabricFcoeSanPcEpRn_Type()
)
cfprFabricFcoeSanPcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpRn.setStatus("current")
_CfprFabricFcoeSanPcEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricFcoeSanPcEpAdminState_Object = MibTableColumn
cfprFabricFcoeSanPcEpAdminState = _CfprFabricFcoeSanPcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 4),
    _CfprFabricFcoeSanPcEpAdminState_Type()
)
cfprFabricFcoeSanPcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpAdminState.setStatus("current")
_CfprFabricFcoeSanPcEpAggrPortId_Type = Gauge32
_CfprFabricFcoeSanPcEpAggrPortId_Object = MibTableColumn
cfprFabricFcoeSanPcEpAggrPortId = _CfprFabricFcoeSanPcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 5),
    _CfprFabricFcoeSanPcEpAggrPortId_Type()
)
cfprFabricFcoeSanPcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpAggrPortId.setStatus("current")
_CfprFabricFcoeSanPcEpChassisId_Type = Gauge32
_CfprFabricFcoeSanPcEpChassisId_Object = MibTableColumn
cfprFabricFcoeSanPcEpChassisId = _CfprFabricFcoeSanPcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 6),
    _CfprFabricFcoeSanPcEpChassisId_Type()
)
cfprFabricFcoeSanPcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpChassisId.setStatus("current")
_CfprFabricFcoeSanPcEpEpDn_Type = SnmpAdminString
_CfprFabricFcoeSanPcEpEpDn_Object = MibTableColumn
cfprFabricFcoeSanPcEpEpDn = _CfprFabricFcoeSanPcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 7),
    _CfprFabricFcoeSanPcEpEpDn_Type()
)
cfprFabricFcoeSanPcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpEpDn.setStatus("current")
_CfprFabricFcoeSanPcEpEthLinkProfileName_Type = SnmpAdminString
_CfprFabricFcoeSanPcEpEthLinkProfileName_Object = MibTableColumn
cfprFabricFcoeSanPcEpEthLinkProfileName = _CfprFabricFcoeSanPcEpEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 8),
    _CfprFabricFcoeSanPcEpEthLinkProfileName_Type()
)
cfprFabricFcoeSanPcEpEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpEthLinkProfileName.setStatus("current")
_CfprFabricFcoeSanPcEpFltAggr_Type = Unsigned64
_CfprFabricFcoeSanPcEpFltAggr_Object = MibTableColumn
cfprFabricFcoeSanPcEpFltAggr = _CfprFabricFcoeSanPcEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 9),
    _CfprFabricFcoeSanPcEpFltAggr_Type()
)
cfprFabricFcoeSanPcEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpFltAggr.setStatus("current")
_CfprFabricFcoeSanPcEpIfRole_Type = CfprFabricSanEpIfRole
_CfprFabricFcoeSanPcEpIfRole_Object = MibTableColumn
cfprFabricFcoeSanPcEpIfRole = _CfprFabricFcoeSanPcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 10),
    _CfprFabricFcoeSanPcEpIfRole_Type()
)
cfprFabricFcoeSanPcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpIfRole.setStatus("current")
_CfprFabricFcoeSanPcEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricFcoeSanPcEpIfType_Object = MibTableColumn
cfprFabricFcoeSanPcEpIfType = _CfprFabricFcoeSanPcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 11),
    _CfprFabricFcoeSanPcEpIfType_Type()
)
cfprFabricFcoeSanPcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpIfType.setStatus("current")
_CfprFabricFcoeSanPcEpLicGP_Type = Unsigned64
_CfprFabricFcoeSanPcEpLicGP_Object = MibTableColumn
cfprFabricFcoeSanPcEpLicGP = _CfprFabricFcoeSanPcEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 12),
    _CfprFabricFcoeSanPcEpLicGP_Type()
)
cfprFabricFcoeSanPcEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpLicGP.setStatus("current")
_CfprFabricFcoeSanPcEpLicState_Type = CfprLicenseState
_CfprFabricFcoeSanPcEpLicState_Object = MibTableColumn
cfprFabricFcoeSanPcEpLicState = _CfprFabricFcoeSanPcEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 13),
    _CfprFabricFcoeSanPcEpLicState_Type()
)
cfprFabricFcoeSanPcEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpLicState.setStatus("current")
_CfprFabricFcoeSanPcEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricFcoeSanPcEpLocale_Object = MibTableColumn
cfprFabricFcoeSanPcEpLocale = _CfprFabricFcoeSanPcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 14),
    _CfprFabricFcoeSanPcEpLocale_Type()
)
cfprFabricFcoeSanPcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpLocale.setStatus("current")
_CfprFabricFcoeSanPcEpMembership_Type = CfprFabricMembershipStatus
_CfprFabricFcoeSanPcEpMembership_Object = MibTableColumn
cfprFabricFcoeSanPcEpMembership = _CfprFabricFcoeSanPcEpMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 15),
    _CfprFabricFcoeSanPcEpMembership_Type()
)
cfprFabricFcoeSanPcEpMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpMembership.setStatus("current")
_CfprFabricFcoeSanPcEpName_Type = SnmpAdminString
_CfprFabricFcoeSanPcEpName_Object = MibTableColumn
cfprFabricFcoeSanPcEpName = _CfprFabricFcoeSanPcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 16),
    _CfprFabricFcoeSanPcEpName_Type()
)
cfprFabricFcoeSanPcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpName.setStatus("current")
_CfprFabricFcoeSanPcEpOperEthLinkProfileName_Type = SnmpAdminString
_CfprFabricFcoeSanPcEpOperEthLinkProfileName_Object = MibTableColumn
cfprFabricFcoeSanPcEpOperEthLinkProfileName = _CfprFabricFcoeSanPcEpOperEthLinkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 17),
    _CfprFabricFcoeSanPcEpOperEthLinkProfileName_Type()
)
cfprFabricFcoeSanPcEpOperEthLinkProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpOperEthLinkProfileName.setStatus("current")
_CfprFabricFcoeSanPcEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricFcoeSanPcEpOperState_Object = MibTableColumn
cfprFabricFcoeSanPcEpOperState = _CfprFabricFcoeSanPcEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 18),
    _CfprFabricFcoeSanPcEpOperState_Type()
)
cfprFabricFcoeSanPcEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpOperState.setStatus("current")
_CfprFabricFcoeSanPcEpOperStateReason_Type = SnmpAdminString
_CfprFabricFcoeSanPcEpOperStateReason_Object = MibTableColumn
cfprFabricFcoeSanPcEpOperStateReason = _CfprFabricFcoeSanPcEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 19),
    _CfprFabricFcoeSanPcEpOperStateReason_Type()
)
cfprFabricFcoeSanPcEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpOperStateReason.setStatus("current")
_CfprFabricFcoeSanPcEpPeerAggrPortId_Type = Gauge32
_CfprFabricFcoeSanPcEpPeerAggrPortId_Object = MibTableColumn
cfprFabricFcoeSanPcEpPeerAggrPortId = _CfprFabricFcoeSanPcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 20),
    _CfprFabricFcoeSanPcEpPeerAggrPortId_Type()
)
cfprFabricFcoeSanPcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpPeerAggrPortId.setStatus("current")
_CfprFabricFcoeSanPcEpPeerChassisId_Type = Gauge32
_CfprFabricFcoeSanPcEpPeerChassisId_Object = MibTableColumn
cfprFabricFcoeSanPcEpPeerChassisId = _CfprFabricFcoeSanPcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 21),
    _CfprFabricFcoeSanPcEpPeerChassisId_Type()
)
cfprFabricFcoeSanPcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpPeerChassisId.setStatus("current")
_CfprFabricFcoeSanPcEpPeerDn_Type = SnmpAdminString
_CfprFabricFcoeSanPcEpPeerDn_Object = MibTableColumn
cfprFabricFcoeSanPcEpPeerDn = _CfprFabricFcoeSanPcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 22),
    _CfprFabricFcoeSanPcEpPeerDn_Type()
)
cfprFabricFcoeSanPcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpPeerDn.setStatus("current")
_CfprFabricFcoeSanPcEpPeerPortId_Type = Gauge32
_CfprFabricFcoeSanPcEpPeerPortId_Object = MibTableColumn
cfprFabricFcoeSanPcEpPeerPortId = _CfprFabricFcoeSanPcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 23),
    _CfprFabricFcoeSanPcEpPeerPortId_Type()
)
cfprFabricFcoeSanPcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpPeerPortId.setStatus("current")
_CfprFabricFcoeSanPcEpPeerSlotId_Type = Gauge32
_CfprFabricFcoeSanPcEpPeerSlotId_Object = MibTableColumn
cfprFabricFcoeSanPcEpPeerSlotId = _CfprFabricFcoeSanPcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 24),
    _CfprFabricFcoeSanPcEpPeerSlotId_Type()
)
cfprFabricFcoeSanPcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpPeerSlotId.setStatus("current")
_CfprFabricFcoeSanPcEpPortId_Type = CfprFabricFcoeSanPcEpPortId
_CfprFabricFcoeSanPcEpPortId_Object = MibTableColumn
cfprFabricFcoeSanPcEpPortId = _CfprFabricFcoeSanPcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 25),
    _CfprFabricFcoeSanPcEpPortId_Type()
)
cfprFabricFcoeSanPcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpPortId.setStatus("current")
_CfprFabricFcoeSanPcEpSlotId_Type = CfprFabricFcoeSanPcEpSlotId
_CfprFabricFcoeSanPcEpSlotId_Object = MibTableColumn
cfprFabricFcoeSanPcEpSlotId = _CfprFabricFcoeSanPcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 26),
    _CfprFabricFcoeSanPcEpSlotId_Type()
)
cfprFabricFcoeSanPcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpSlotId.setStatus("current")
_CfprFabricFcoeSanPcEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcoeSanPcEpSwitchId_Object = MibTableColumn
cfprFabricFcoeSanPcEpSwitchId = _CfprFabricFcoeSanPcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 27),
    _CfprFabricFcoeSanPcEpSwitchId_Type()
)
cfprFabricFcoeSanPcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpSwitchId.setStatus("current")
_CfprFabricFcoeSanPcEpTransport_Type = CfprFabricAFcoeSanEpTransport
_CfprFabricFcoeSanPcEpTransport_Object = MibTableColumn
cfprFabricFcoeSanPcEpTransport = _CfprFabricFcoeSanPcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 28),
    _CfprFabricFcoeSanPcEpTransport_Type()
)
cfprFabricFcoeSanPcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpTransport.setStatus("current")
_CfprFabricFcoeSanPcEpType_Type = CfprFabricSanEpType
_CfprFabricFcoeSanPcEpType_Object = MibTableColumn
cfprFabricFcoeSanPcEpType = _CfprFabricFcoeSanPcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 29),
    _CfprFabricFcoeSanPcEpType_Type()
)
cfprFabricFcoeSanPcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpType.setStatus("current")
_CfprFabricFcoeSanPcEpUdldOperState_Type = CfprFabricUdldOperState
_CfprFabricFcoeSanPcEpUdldOperState_Object = MibTableColumn
cfprFabricFcoeSanPcEpUdldOperState = _CfprFabricFcoeSanPcEpUdldOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 30),
    _CfprFabricFcoeSanPcEpUdldOperState_Type()
)
cfprFabricFcoeSanPcEpUdldOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpUdldOperState.setStatus("current")
_CfprFabricFcoeSanPcEpWarnings_Type = CfprFabricWarnings
_CfprFabricFcoeSanPcEpWarnings_Object = MibTableColumn
cfprFabricFcoeSanPcEpWarnings = _CfprFabricFcoeSanPcEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 64, 1, 31),
    _CfprFabricFcoeSanPcEpWarnings_Type()
)
cfprFabricFcoeSanPcEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeSanPcEpWarnings.setStatus("current")
_CfprFabricFcoeVsanPcTable_Object = MibTable
cfprFabricFcoeVsanPcTable = _CfprFabricFcoeVsanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65)
)
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcTable.setStatus("current")
_CfprFabricFcoeVsanPcEntry_Object = MibTableRow
cfprFabricFcoeVsanPcEntry = _CfprFabricFcoeVsanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1)
)
cfprFabricFcoeVsanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcoeVsanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcEntry.setStatus("current")
_CfprFabricFcoeVsanPcInstanceId_Type = CfprManagedObjectId
_CfprFabricFcoeVsanPcInstanceId_Object = MibTableColumn
cfprFabricFcoeVsanPcInstanceId = _CfprFabricFcoeVsanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 1),
    _CfprFabricFcoeVsanPcInstanceId_Type()
)
cfprFabricFcoeVsanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcInstanceId.setStatus("current")
_CfprFabricFcoeVsanPcDn_Type = CfprManagedObjectDn
_CfprFabricFcoeVsanPcDn_Object = MibTableColumn
cfprFabricFcoeVsanPcDn = _CfprFabricFcoeVsanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 2),
    _CfprFabricFcoeVsanPcDn_Type()
)
cfprFabricFcoeVsanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcDn.setStatus("current")
_CfprFabricFcoeVsanPcRn_Type = SnmpAdminString
_CfprFabricFcoeVsanPcRn_Object = MibTableColumn
cfprFabricFcoeVsanPcRn = _CfprFabricFcoeVsanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 3),
    _CfprFabricFcoeVsanPcRn_Type()
)
cfprFabricFcoeVsanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcRn.setStatus("current")
_CfprFabricFcoeVsanPcAdminState_Type = CfprFabricCIoEpAdminState
_CfprFabricFcoeVsanPcAdminState_Object = MibTableColumn
cfprFabricFcoeVsanPcAdminState = _CfprFabricFcoeVsanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 4),
    _CfprFabricFcoeVsanPcAdminState_Type()
)
cfprFabricFcoeVsanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcAdminState.setStatus("current")
_CfprFabricFcoeVsanPcDescr_Type = SnmpAdminString
_CfprFabricFcoeVsanPcDescr_Object = MibTableColumn
cfprFabricFcoeVsanPcDescr = _CfprFabricFcoeVsanPcDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 5),
    _CfprFabricFcoeVsanPcDescr_Type()
)
cfprFabricFcoeVsanPcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcDescr.setStatus("current")
_CfprFabricFcoeVsanPcEpDn_Type = SnmpAdminString
_CfprFabricFcoeVsanPcEpDn_Object = MibTableColumn
cfprFabricFcoeVsanPcEpDn = _CfprFabricFcoeVsanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 6),
    _CfprFabricFcoeVsanPcEpDn_Type()
)
cfprFabricFcoeVsanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcEpDn.setStatus("current")
_CfprFabricFcoeVsanPcFltAggr_Type = Unsigned64
_CfprFabricFcoeVsanPcFltAggr_Object = MibTableColumn
cfprFabricFcoeVsanPcFltAggr = _CfprFabricFcoeVsanPcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 7),
    _CfprFabricFcoeVsanPcFltAggr_Type()
)
cfprFabricFcoeVsanPcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcFltAggr.setStatus("current")
_CfprFabricFcoeVsanPcIfRole_Type = CfprFabricSanPcIfRole
_CfprFabricFcoeVsanPcIfRole_Object = MibTableColumn
cfprFabricFcoeVsanPcIfRole = _CfprFabricFcoeVsanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 8),
    _CfprFabricFcoeVsanPcIfRole_Type()
)
cfprFabricFcoeVsanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcIfRole.setStatus("current")
_CfprFabricFcoeVsanPcIfType_Type = CfprFabricCIoEpIfType
_CfprFabricFcoeVsanPcIfType_Object = MibTableColumn
cfprFabricFcoeVsanPcIfType = _CfprFabricFcoeVsanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 9),
    _CfprFabricFcoeVsanPcIfType_Type()
)
cfprFabricFcoeVsanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcIfType.setStatus("current")
_CfprFabricFcoeVsanPcLocale_Type = CfprFabricExternalPcLocale
_CfprFabricFcoeVsanPcLocale_Object = MibTableColumn
cfprFabricFcoeVsanPcLocale = _CfprFabricFcoeVsanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 10),
    _CfprFabricFcoeVsanPcLocale_Type()
)
cfprFabricFcoeVsanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcLocale.setStatus("current")
_CfprFabricFcoeVsanPcName_Type = SnmpAdminString
_CfprFabricFcoeVsanPcName_Object = MibTableColumn
cfprFabricFcoeVsanPcName = _CfprFabricFcoeVsanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 11),
    _CfprFabricFcoeVsanPcName_Type()
)
cfprFabricFcoeVsanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcName.setStatus("current")
_CfprFabricFcoeVsanPcOperState_Type = CfprNetworkPortOperState
_CfprFabricFcoeVsanPcOperState_Object = MibTableColumn
cfprFabricFcoeVsanPcOperState = _CfprFabricFcoeVsanPcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 12),
    _CfprFabricFcoeVsanPcOperState_Type()
)
cfprFabricFcoeVsanPcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcOperState.setStatus("current")
_CfprFabricFcoeVsanPcPeerDn_Type = SnmpAdminString
_CfprFabricFcoeVsanPcPeerDn_Object = MibTableColumn
cfprFabricFcoeVsanPcPeerDn = _CfprFabricFcoeVsanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 13),
    _CfprFabricFcoeVsanPcPeerDn_Type()
)
cfprFabricFcoeVsanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcPeerDn.setStatus("current")
_CfprFabricFcoeVsanPcPortId_Type = Gauge32
_CfprFabricFcoeVsanPcPortId_Object = MibTableColumn
cfprFabricFcoeVsanPcPortId = _CfprFabricFcoeVsanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 14),
    _CfprFabricFcoeVsanPcPortId_Type()
)
cfprFabricFcoeVsanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcPortId.setStatus("current")
_CfprFabricFcoeVsanPcStateQual_Type = SnmpAdminString
_CfprFabricFcoeVsanPcStateQual_Object = MibTableColumn
cfprFabricFcoeVsanPcStateQual = _CfprFabricFcoeVsanPcStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 15),
    _CfprFabricFcoeVsanPcStateQual_Type()
)
cfprFabricFcoeVsanPcStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcStateQual.setStatus("current")
_CfprFabricFcoeVsanPcSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcoeVsanPcSwitchId_Object = MibTableColumn
cfprFabricFcoeVsanPcSwitchId = _CfprFabricFcoeVsanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 16),
    _CfprFabricFcoeVsanPcSwitchId_Type()
)
cfprFabricFcoeVsanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcSwitchId.setStatus("current")
_CfprFabricFcoeVsanPcTransport_Type = CfprFabricFcoeVsanPcTransport
_CfprFabricFcoeVsanPcTransport_Object = MibTableColumn
cfprFabricFcoeVsanPcTransport = _CfprFabricFcoeVsanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 17),
    _CfprFabricFcoeVsanPcTransport_Type()
)
cfprFabricFcoeVsanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcTransport.setStatus("current")
_CfprFabricFcoeVsanPcType_Type = CfprFabricSanPcType
_CfprFabricFcoeVsanPcType_Object = MibTableColumn
cfprFabricFcoeVsanPcType = _CfprFabricFcoeVsanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 18),
    _CfprFabricFcoeVsanPcType_Type()
)
cfprFabricFcoeVsanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcType.setStatus("current")
_CfprFabricFcoeVsanPcWarnings_Type = CfprFabricWarnings
_CfprFabricFcoeVsanPcWarnings_Object = MibTableColumn
cfprFabricFcoeVsanPcWarnings = _CfprFabricFcoeVsanPcWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 65, 1, 19),
    _CfprFabricFcoeVsanPcWarnings_Type()
)
cfprFabricFcoeVsanPcWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPcWarnings.setStatus("current")
_CfprFabricFcoeVsanPortEpTable_Object = MibTable
cfprFabricFcoeVsanPortEpTable = _CfprFabricFcoeVsanPortEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66)
)
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpTable.setStatus("current")
_CfprFabricFcoeVsanPortEpEntry_Object = MibTableRow
cfprFabricFcoeVsanPortEpEntry = _CfprFabricFcoeVsanPortEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1)
)
cfprFabricFcoeVsanPortEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricFcoeVsanPortEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpEntry.setStatus("current")
_CfprFabricFcoeVsanPortEpInstanceId_Type = CfprManagedObjectId
_CfprFabricFcoeVsanPortEpInstanceId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpInstanceId = _CfprFabricFcoeVsanPortEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 1),
    _CfprFabricFcoeVsanPortEpInstanceId_Type()
)
cfprFabricFcoeVsanPortEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpInstanceId.setStatus("current")
_CfprFabricFcoeVsanPortEpDn_Type = CfprManagedObjectDn
_CfprFabricFcoeVsanPortEpDn_Object = MibTableColumn
cfprFabricFcoeVsanPortEpDn = _CfprFabricFcoeVsanPortEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 2),
    _CfprFabricFcoeVsanPortEpDn_Type()
)
cfprFabricFcoeVsanPortEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpDn.setStatus("current")
_CfprFabricFcoeVsanPortEpRn_Type = SnmpAdminString
_CfprFabricFcoeVsanPortEpRn_Object = MibTableColumn
cfprFabricFcoeVsanPortEpRn = _CfprFabricFcoeVsanPortEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 3),
    _CfprFabricFcoeVsanPortEpRn_Type()
)
cfprFabricFcoeVsanPortEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpRn.setStatus("current")
_CfprFabricFcoeVsanPortEpAdminState_Type = CfprFabricExternalEpAdminState
_CfprFabricFcoeVsanPortEpAdminState_Object = MibTableColumn
cfprFabricFcoeVsanPortEpAdminState = _CfprFabricFcoeVsanPortEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 4),
    _CfprFabricFcoeVsanPortEpAdminState_Type()
)
cfprFabricFcoeVsanPortEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpAdminState.setStatus("current")
_CfprFabricFcoeVsanPortEpAggrPortId_Type = Gauge32
_CfprFabricFcoeVsanPortEpAggrPortId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpAggrPortId = _CfprFabricFcoeVsanPortEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 5),
    _CfprFabricFcoeVsanPortEpAggrPortId_Type()
)
cfprFabricFcoeVsanPortEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpAggrPortId.setStatus("current")
_CfprFabricFcoeVsanPortEpChassisId_Type = Gauge32
_CfprFabricFcoeVsanPortEpChassisId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpChassisId = _CfprFabricFcoeVsanPortEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 6),
    _CfprFabricFcoeVsanPortEpChassisId_Type()
)
cfprFabricFcoeVsanPortEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpChassisId.setStatus("current")
_CfprFabricFcoeVsanPortEpEpDn_Type = SnmpAdminString
_CfprFabricFcoeVsanPortEpEpDn_Object = MibTableColumn
cfprFabricFcoeVsanPortEpEpDn = _CfprFabricFcoeVsanPortEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 7),
    _CfprFabricFcoeVsanPortEpEpDn_Type()
)
cfprFabricFcoeVsanPortEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpEpDn.setStatus("current")
_CfprFabricFcoeVsanPortEpFltAggr_Type = Unsigned64
_CfprFabricFcoeVsanPortEpFltAggr_Object = MibTableColumn
cfprFabricFcoeVsanPortEpFltAggr = _CfprFabricFcoeVsanPortEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 8),
    _CfprFabricFcoeVsanPortEpFltAggr_Type()
)
cfprFabricFcoeVsanPortEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpFltAggr.setStatus("current")
_CfprFabricFcoeVsanPortEpIfRole_Type = CfprFabricSanEpIfRole
_CfprFabricFcoeVsanPortEpIfRole_Object = MibTableColumn
cfprFabricFcoeVsanPortEpIfRole = _CfprFabricFcoeVsanPortEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 9),
    _CfprFabricFcoeVsanPortEpIfRole_Type()
)
cfprFabricFcoeVsanPortEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpIfRole.setStatus("current")
_CfprFabricFcoeVsanPortEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricFcoeVsanPortEpIfType_Object = MibTableColumn
cfprFabricFcoeVsanPortEpIfType = _CfprFabricFcoeVsanPortEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 10),
    _CfprFabricFcoeVsanPortEpIfType_Type()
)
cfprFabricFcoeVsanPortEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpIfType.setStatus("current")
_CfprFabricFcoeVsanPortEpLicGP_Type = Unsigned64
_CfprFabricFcoeVsanPortEpLicGP_Object = MibTableColumn
cfprFabricFcoeVsanPortEpLicGP = _CfprFabricFcoeVsanPortEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 11),
    _CfprFabricFcoeVsanPortEpLicGP_Type()
)
cfprFabricFcoeVsanPortEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpLicGP.setStatus("current")
_CfprFabricFcoeVsanPortEpLicState_Type = CfprLicenseState
_CfprFabricFcoeVsanPortEpLicState_Object = MibTableColumn
cfprFabricFcoeVsanPortEpLicState = _CfprFabricFcoeVsanPortEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 12),
    _CfprFabricFcoeVsanPortEpLicState_Type()
)
cfprFabricFcoeVsanPortEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpLicState.setStatus("current")
_CfprFabricFcoeVsanPortEpLocale_Type = CfprFabricExternalEpLocale
_CfprFabricFcoeVsanPortEpLocale_Object = MibTableColumn
cfprFabricFcoeVsanPortEpLocale = _CfprFabricFcoeVsanPortEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 13),
    _CfprFabricFcoeVsanPortEpLocale_Type()
)
cfprFabricFcoeVsanPortEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpLocale.setStatus("current")
_CfprFabricFcoeVsanPortEpName_Type = SnmpAdminString
_CfprFabricFcoeVsanPortEpName_Object = MibTableColumn
cfprFabricFcoeVsanPortEpName = _CfprFabricFcoeVsanPortEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 14),
    _CfprFabricFcoeVsanPortEpName_Type()
)
cfprFabricFcoeVsanPortEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpName.setStatus("current")
_CfprFabricFcoeVsanPortEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricFcoeVsanPortEpOperState_Object = MibTableColumn
cfprFabricFcoeVsanPortEpOperState = _CfprFabricFcoeVsanPortEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 15),
    _CfprFabricFcoeVsanPortEpOperState_Type()
)
cfprFabricFcoeVsanPortEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpOperState.setStatus("current")
_CfprFabricFcoeVsanPortEpOperStateReason_Type = SnmpAdminString
_CfprFabricFcoeVsanPortEpOperStateReason_Object = MibTableColumn
cfprFabricFcoeVsanPortEpOperStateReason = _CfprFabricFcoeVsanPortEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 16),
    _CfprFabricFcoeVsanPortEpOperStateReason_Type()
)
cfprFabricFcoeVsanPortEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpOperStateReason.setStatus("current")
_CfprFabricFcoeVsanPortEpPeerAggrPortId_Type = Gauge32
_CfprFabricFcoeVsanPortEpPeerAggrPortId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpPeerAggrPortId = _CfprFabricFcoeVsanPortEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 17),
    _CfprFabricFcoeVsanPortEpPeerAggrPortId_Type()
)
cfprFabricFcoeVsanPortEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpPeerAggrPortId.setStatus("current")
_CfprFabricFcoeVsanPortEpPeerChassisId_Type = Gauge32
_CfprFabricFcoeVsanPortEpPeerChassisId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpPeerChassisId = _CfprFabricFcoeVsanPortEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 18),
    _CfprFabricFcoeVsanPortEpPeerChassisId_Type()
)
cfprFabricFcoeVsanPortEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpPeerChassisId.setStatus("current")
_CfprFabricFcoeVsanPortEpPeerDn_Type = SnmpAdminString
_CfprFabricFcoeVsanPortEpPeerDn_Object = MibTableColumn
cfprFabricFcoeVsanPortEpPeerDn = _CfprFabricFcoeVsanPortEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 19),
    _CfprFabricFcoeVsanPortEpPeerDn_Type()
)
cfprFabricFcoeVsanPortEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpPeerDn.setStatus("current")
_CfprFabricFcoeVsanPortEpPeerPortId_Type = Gauge32
_CfprFabricFcoeVsanPortEpPeerPortId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpPeerPortId = _CfprFabricFcoeVsanPortEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 20),
    _CfprFabricFcoeVsanPortEpPeerPortId_Type()
)
cfprFabricFcoeVsanPortEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpPeerPortId.setStatus("current")
_CfprFabricFcoeVsanPortEpPeerSlotId_Type = Gauge32
_CfprFabricFcoeVsanPortEpPeerSlotId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpPeerSlotId = _CfprFabricFcoeVsanPortEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 21),
    _CfprFabricFcoeVsanPortEpPeerSlotId_Type()
)
cfprFabricFcoeVsanPortEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpPeerSlotId.setStatus("current")
_CfprFabricFcoeVsanPortEpPortId_Type = CfprFabricFcoeVsanPortEpPortId
_CfprFabricFcoeVsanPortEpPortId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpPortId = _CfprFabricFcoeVsanPortEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 22),
    _CfprFabricFcoeVsanPortEpPortId_Type()
)
cfprFabricFcoeVsanPortEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpPortId.setStatus("current")
_CfprFabricFcoeVsanPortEpSlotId_Type = CfprFabricFcoeVsanPortEpSlotId
_CfprFabricFcoeVsanPortEpSlotId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpSlotId = _CfprFabricFcoeVsanPortEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 23),
    _CfprFabricFcoeVsanPortEpSlotId_Type()
)
cfprFabricFcoeVsanPortEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpSlotId.setStatus("current")
_CfprFabricFcoeVsanPortEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricFcoeVsanPortEpSwitchId_Object = MibTableColumn
cfprFabricFcoeVsanPortEpSwitchId = _CfprFabricFcoeVsanPortEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 24),
    _CfprFabricFcoeVsanPortEpSwitchId_Type()
)
cfprFabricFcoeVsanPortEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpSwitchId.setStatus("current")
_CfprFabricFcoeVsanPortEpTransport_Type = CfprFabricAFcSanEpTransport
_CfprFabricFcoeVsanPortEpTransport_Object = MibTableColumn
cfprFabricFcoeVsanPortEpTransport = _CfprFabricFcoeVsanPortEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 25),
    _CfprFabricFcoeVsanPortEpTransport_Type()
)
cfprFabricFcoeVsanPortEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpTransport.setStatus("current")
_CfprFabricFcoeVsanPortEpType_Type = CfprFabricSanEpType
_CfprFabricFcoeVsanPortEpType_Object = MibTableColumn
cfprFabricFcoeVsanPortEpType = _CfprFabricFcoeVsanPortEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 26),
    _CfprFabricFcoeVsanPortEpType_Type()
)
cfprFabricFcoeVsanPortEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpType.setStatus("current")
_CfprFabricFcoeVsanPortEpWarnings_Type = CfprFabricWarnings
_CfprFabricFcoeVsanPortEpWarnings_Object = MibTableColumn
cfprFabricFcoeVsanPortEpWarnings = _CfprFabricFcoeVsanPortEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 66, 1, 27),
    _CfprFabricFcoeVsanPortEpWarnings_Type()
)
cfprFabricFcoeVsanPortEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricFcoeVsanPortEpWarnings.setStatus("current")
_CfprFabricIfTable_Object = MibTable
cfprFabricIfTable = _CfprFabricIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 69)
)
if mibBuilder.loadTexts:
    cfprFabricIfTable.setStatus("current")
_CfprFabricIfEntry_Object = MibTableRow
cfprFabricIfEntry = _CfprFabricIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 69, 1)
)
cfprFabricIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricIfEntry.setStatus("current")
_CfprFabricIfInstanceId_Type = CfprManagedObjectId
_CfprFabricIfInstanceId_Object = MibTableColumn
cfprFabricIfInstanceId = _CfprFabricIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 69, 1, 1),
    _CfprFabricIfInstanceId_Type()
)
cfprFabricIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricIfInstanceId.setStatus("current")
_CfprFabricIfDn_Type = CfprManagedObjectDn
_CfprFabricIfDn_Object = MibTableColumn
cfprFabricIfDn = _CfprFabricIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 69, 1, 2),
    _CfprFabricIfDn_Type()
)
cfprFabricIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricIfDn.setStatus("current")
_CfprFabricIfRn_Type = SnmpAdminString
_CfprFabricIfRn_Object = MibTableColumn
cfprFabricIfRn = _CfprFabricIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 69, 1, 3),
    _CfprFabricIfRn_Type()
)
cfprFabricIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricIfRn.setStatus("current")
_CfprFabricIfAddr_Type = InetAddressIPv4
_CfprFabricIfAddr_Object = MibTableColumn
cfprFabricIfAddr = _CfprFabricIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 69, 1, 4),
    _CfprFabricIfAddr_Type()
)
cfprFabricIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricIfAddr.setStatus("current")
_CfprFabricIfId_Type = CfprNetworkSwitchId
_CfprFabricIfId_Object = MibTableColumn
cfprFabricIfId = _CfprFabricIfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 69, 1, 5),
    _CfprFabricIfId_Type()
)
cfprFabricIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricIfId.setStatus("current")
_CfprFabricLacpPolicyTable_Object = MibTable
cfprFabricLacpPolicyTable = _CfprFabricLacpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70)
)
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyTable.setStatus("current")
_CfprFabricLacpPolicyEntry_Object = MibTableRow
cfprFabricLacpPolicyEntry = _CfprFabricLacpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1)
)
cfprFabricLacpPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLacpPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyEntry.setStatus("current")
_CfprFabricLacpPolicyInstanceId_Type = CfprManagedObjectId
_CfprFabricLacpPolicyInstanceId_Object = MibTableColumn
cfprFabricLacpPolicyInstanceId = _CfprFabricLacpPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 1),
    _CfprFabricLacpPolicyInstanceId_Type()
)
cfprFabricLacpPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyInstanceId.setStatus("current")
_CfprFabricLacpPolicyDn_Type = CfprManagedObjectDn
_CfprFabricLacpPolicyDn_Object = MibTableColumn
cfprFabricLacpPolicyDn = _CfprFabricLacpPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 2),
    _CfprFabricLacpPolicyDn_Type()
)
cfprFabricLacpPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyDn.setStatus("current")
_CfprFabricLacpPolicyRn_Type = SnmpAdminString
_CfprFabricLacpPolicyRn_Object = MibTableColumn
cfprFabricLacpPolicyRn = _CfprFabricLacpPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 3),
    _CfprFabricLacpPolicyRn_Type()
)
cfprFabricLacpPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyRn.setStatus("current")
_CfprFabricLacpPolicyDescr_Type = SnmpAdminString
_CfprFabricLacpPolicyDescr_Object = MibTableColumn
cfprFabricLacpPolicyDescr = _CfprFabricLacpPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 4),
    _CfprFabricLacpPolicyDescr_Type()
)
cfprFabricLacpPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyDescr.setStatus("current")
_CfprFabricLacpPolicyFastTimer_Type = CfprFabricLacpRate
_CfprFabricLacpPolicyFastTimer_Object = MibTableColumn
cfprFabricLacpPolicyFastTimer = _CfprFabricLacpPolicyFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 5),
    _CfprFabricLacpPolicyFastTimer_Type()
)
cfprFabricLacpPolicyFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyFastTimer.setStatus("current")
_CfprFabricLacpPolicyIntId_Type = SnmpAdminString
_CfprFabricLacpPolicyIntId_Object = MibTableColumn
cfprFabricLacpPolicyIntId = _CfprFabricLacpPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 6),
    _CfprFabricLacpPolicyIntId_Type()
)
cfprFabricLacpPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyIntId.setStatus("current")
_CfprFabricLacpPolicyName_Type = SnmpAdminString
_CfprFabricLacpPolicyName_Object = MibTableColumn
cfprFabricLacpPolicyName = _CfprFabricLacpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 7),
    _CfprFabricLacpPolicyName_Type()
)
cfprFabricLacpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyName.setStatus("current")
_CfprFabricLacpPolicyPolicyLevel_Type = Gauge32
_CfprFabricLacpPolicyPolicyLevel_Object = MibTableColumn
cfprFabricLacpPolicyPolicyLevel = _CfprFabricLacpPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 8),
    _CfprFabricLacpPolicyPolicyLevel_Type()
)
cfprFabricLacpPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyPolicyLevel.setStatus("current")
_CfprFabricLacpPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricLacpPolicyPolicyOwner_Object = MibTableColumn
cfprFabricLacpPolicyPolicyOwner = _CfprFabricLacpPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 9),
    _CfprFabricLacpPolicyPolicyOwner_Type()
)
cfprFabricLacpPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicyPolicyOwner.setStatus("current")
_CfprFabricLacpPolicySuspendIndividual_Type = CfprFabricLacpSuspend
_CfprFabricLacpPolicySuspendIndividual_Object = MibTableColumn
cfprFabricLacpPolicySuspendIndividual = _CfprFabricLacpPolicySuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 70, 1, 10),
    _CfprFabricLacpPolicySuspendIndividual_Type()
)
cfprFabricLacpPolicySuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLacpPolicySuspendIndividual.setStatus("current")
_CfprFabricLanAccessMgrTable_Object = MibTable
cfprFabricLanAccessMgrTable = _CfprFabricLanAccessMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 71)
)
if mibBuilder.loadTexts:
    cfprFabricLanAccessMgrTable.setStatus("current")
_CfprFabricLanAccessMgrEntry_Object = MibTableRow
cfprFabricLanAccessMgrEntry = _CfprFabricLanAccessMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 71, 1)
)
cfprFabricLanAccessMgrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLanAccessMgrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLanAccessMgrEntry.setStatus("current")
_CfprFabricLanAccessMgrInstanceId_Type = CfprManagedObjectId
_CfprFabricLanAccessMgrInstanceId_Object = MibTableColumn
cfprFabricLanAccessMgrInstanceId = _CfprFabricLanAccessMgrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 71, 1, 1),
    _CfprFabricLanAccessMgrInstanceId_Type()
)
cfprFabricLanAccessMgrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLanAccessMgrInstanceId.setStatus("current")
_CfprFabricLanAccessMgrDn_Type = CfprManagedObjectDn
_CfprFabricLanAccessMgrDn_Object = MibTableColumn
cfprFabricLanAccessMgrDn = _CfprFabricLanAccessMgrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 71, 1, 2),
    _CfprFabricLanAccessMgrDn_Type()
)
cfprFabricLanAccessMgrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanAccessMgrDn.setStatus("current")
_CfprFabricLanAccessMgrRn_Type = SnmpAdminString
_CfprFabricLanAccessMgrRn_Object = MibTableColumn
cfprFabricLanAccessMgrRn = _CfprFabricLanAccessMgrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 71, 1, 3),
    _CfprFabricLanAccessMgrRn_Type()
)
cfprFabricLanAccessMgrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanAccessMgrRn.setStatus("current")
_CfprFabricLanCloudTable_Object = MibTable
cfprFabricLanCloudTable = _CfprFabricLanCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72)
)
if mibBuilder.loadTexts:
    cfprFabricLanCloudTable.setStatus("current")
_CfprFabricLanCloudEntry_Object = MibTableRow
cfprFabricLanCloudEntry = _CfprFabricLanCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1)
)
cfprFabricLanCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLanCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLanCloudEntry.setStatus("current")
_CfprFabricLanCloudInstanceId_Type = CfprManagedObjectId
_CfprFabricLanCloudInstanceId_Object = MibTableColumn
cfprFabricLanCloudInstanceId = _CfprFabricLanCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 1),
    _CfprFabricLanCloudInstanceId_Type()
)
cfprFabricLanCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLanCloudInstanceId.setStatus("current")
_CfprFabricLanCloudDn_Type = CfprManagedObjectDn
_CfprFabricLanCloudDn_Object = MibTableColumn
cfprFabricLanCloudDn = _CfprFabricLanCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 2),
    _CfprFabricLanCloudDn_Type()
)
cfprFabricLanCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudDn.setStatus("current")
_CfprFabricLanCloudRn_Type = SnmpAdminString
_CfprFabricLanCloudRn_Object = MibTableColumn
cfprFabricLanCloudRn = _CfprFabricLanCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 3),
    _CfprFabricLanCloudRn_Type()
)
cfprFabricLanCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudRn.setStatus("current")
_CfprFabricLanCloudFsmDescr_Type = SnmpAdminString
_CfprFabricLanCloudFsmDescr_Object = MibTableColumn
cfprFabricLanCloudFsmDescr = _CfprFabricLanCloudFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 4),
    _CfprFabricLanCloudFsmDescr_Type()
)
cfprFabricLanCloudFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmDescr.setStatus("current")
_CfprFabricLanCloudFsmPrev_Type = SnmpAdminString
_CfprFabricLanCloudFsmPrev_Object = MibTableColumn
cfprFabricLanCloudFsmPrev = _CfprFabricLanCloudFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 5),
    _CfprFabricLanCloudFsmPrev_Type()
)
cfprFabricLanCloudFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmPrev.setStatus("current")
_CfprFabricLanCloudFsmProgr_Type = Gauge32
_CfprFabricLanCloudFsmProgr_Object = MibTableColumn
cfprFabricLanCloudFsmProgr = _CfprFabricLanCloudFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 6),
    _CfprFabricLanCloudFsmProgr_Type()
)
cfprFabricLanCloudFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmProgr.setStatus("current")
_CfprFabricLanCloudFsmRmtInvErrCode_Type = Gauge32
_CfprFabricLanCloudFsmRmtInvErrCode_Object = MibTableColumn
cfprFabricLanCloudFsmRmtInvErrCode = _CfprFabricLanCloudFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 7),
    _CfprFabricLanCloudFsmRmtInvErrCode_Type()
)
cfprFabricLanCloudFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmRmtInvErrCode.setStatus("current")
_CfprFabricLanCloudFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFabricLanCloudFsmRmtInvErrDescr_Object = MibTableColumn
cfprFabricLanCloudFsmRmtInvErrDescr = _CfprFabricLanCloudFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 8),
    _CfprFabricLanCloudFsmRmtInvErrDescr_Type()
)
cfprFabricLanCloudFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmRmtInvErrDescr.setStatus("current")
_CfprFabricLanCloudFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricLanCloudFsmRmtInvRslt_Object = MibTableColumn
cfprFabricLanCloudFsmRmtInvRslt = _CfprFabricLanCloudFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 9),
    _CfprFabricLanCloudFsmRmtInvRslt_Type()
)
cfprFabricLanCloudFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmRmtInvRslt.setStatus("current")
_CfprFabricLanCloudFsmStageDescr_Type = SnmpAdminString
_CfprFabricLanCloudFsmStageDescr_Object = MibTableColumn
cfprFabricLanCloudFsmStageDescr = _CfprFabricLanCloudFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 10),
    _CfprFabricLanCloudFsmStageDescr_Type()
)
cfprFabricLanCloudFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageDescr.setStatus("current")
_CfprFabricLanCloudFsmStamp_Type = DateAndTime
_CfprFabricLanCloudFsmStamp_Object = MibTableColumn
cfprFabricLanCloudFsmStamp = _CfprFabricLanCloudFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 11),
    _CfprFabricLanCloudFsmStamp_Type()
)
cfprFabricLanCloudFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStamp.setStatus("current")
_CfprFabricLanCloudFsmStatus_Type = SnmpAdminString
_CfprFabricLanCloudFsmStatus_Object = MibTableColumn
cfprFabricLanCloudFsmStatus = _CfprFabricLanCloudFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 12),
    _CfprFabricLanCloudFsmStatus_Type()
)
cfprFabricLanCloudFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStatus.setStatus("current")
_CfprFabricLanCloudFsmTry_Type = Gauge32
_CfprFabricLanCloudFsmTry_Object = MibTableColumn
cfprFabricLanCloudFsmTry = _CfprFabricLanCloudFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 13),
    _CfprFabricLanCloudFsmTry_Type()
)
cfprFabricLanCloudFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTry.setStatus("current")
_CfprFabricLanCloudMacAging_Type = TimeIntervalSec
_CfprFabricLanCloudMacAging_Object = MibTableColumn
cfprFabricLanCloudMacAging = _CfprFabricLanCloudMacAging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 14),
    _CfprFabricLanCloudMacAging_Type()
)
cfprFabricLanCloudMacAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudMacAging.setStatus("current")
_CfprFabricLanCloudMode_Type = CfprFabricSwitchingMode
_CfprFabricLanCloudMode_Object = MibTableColumn
cfprFabricLanCloudMode = _CfprFabricLanCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 15),
    _CfprFabricLanCloudMode_Type()
)
cfprFabricLanCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudMode.setStatus("current")
_CfprFabricLanCloudVlanCompression_Type = CfprFabricLanCloudVlanCompression
_CfprFabricLanCloudVlanCompression_Object = MibTableColumn
cfprFabricLanCloudVlanCompression = _CfprFabricLanCloudVlanCompression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 72, 1, 16),
    _CfprFabricLanCloudVlanCompression_Type()
)
cfprFabricLanCloudVlanCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudVlanCompression.setStatus("current")
_CfprFabricLanCloudFsmTable_Object = MibTable
cfprFabricLanCloudFsmTable = _CfprFabricLanCloudFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73)
)
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTable.setStatus("current")
_CfprFabricLanCloudFsmEntry_Object = MibTableRow
cfprFabricLanCloudFsmEntry = _CfprFabricLanCloudFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1)
)
cfprFabricLanCloudFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLanCloudFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmEntry.setStatus("current")
_CfprFabricLanCloudFsmInstanceId_Type = CfprManagedObjectId
_CfprFabricLanCloudFsmInstanceId_Object = MibTableColumn
cfprFabricLanCloudFsmInstanceId = _CfprFabricLanCloudFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 1),
    _CfprFabricLanCloudFsmInstanceId_Type()
)
cfprFabricLanCloudFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmInstanceId.setStatus("current")
_CfprFabricLanCloudFsmDn_Type = CfprManagedObjectDn
_CfprFabricLanCloudFsmDn_Object = MibTableColumn
cfprFabricLanCloudFsmDn = _CfprFabricLanCloudFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 2),
    _CfprFabricLanCloudFsmDn_Type()
)
cfprFabricLanCloudFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmDn.setStatus("current")
_CfprFabricLanCloudFsmRn_Type = SnmpAdminString
_CfprFabricLanCloudFsmRn_Object = MibTableColumn
cfprFabricLanCloudFsmRn = _CfprFabricLanCloudFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 3),
    _CfprFabricLanCloudFsmRn_Type()
)
cfprFabricLanCloudFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmRn.setStatus("current")
_CfprFabricLanCloudFsmCompletionTime_Type = DateAndTime
_CfprFabricLanCloudFsmCompletionTime_Object = MibTableColumn
cfprFabricLanCloudFsmCompletionTime = _CfprFabricLanCloudFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 4),
    _CfprFabricLanCloudFsmCompletionTime_Type()
)
cfprFabricLanCloudFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmCompletionTime.setStatus("current")
_CfprFabricLanCloudFsmCurrentFsm_Type = CfprFabricLanCloudFsmCurrentFsm
_CfprFabricLanCloudFsmCurrentFsm_Object = MibTableColumn
cfprFabricLanCloudFsmCurrentFsm = _CfprFabricLanCloudFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 5),
    _CfprFabricLanCloudFsmCurrentFsm_Type()
)
cfprFabricLanCloudFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmCurrentFsm.setStatus("current")
_CfprFabricLanCloudFsmDescrData_Type = SnmpAdminString
_CfprFabricLanCloudFsmDescrData_Object = MibTableColumn
cfprFabricLanCloudFsmDescrData = _CfprFabricLanCloudFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 6),
    _CfprFabricLanCloudFsmDescrData_Type()
)
cfprFabricLanCloudFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmDescrData.setStatus("current")
_CfprFabricLanCloudFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFabricLanCloudFsmFsmStatus_Object = MibTableColumn
cfprFabricLanCloudFsmFsmStatus = _CfprFabricLanCloudFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 7),
    _CfprFabricLanCloudFsmFsmStatus_Type()
)
cfprFabricLanCloudFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmFsmStatus.setStatus("current")
_CfprFabricLanCloudFsmProgress_Type = Gauge32
_CfprFabricLanCloudFsmProgress_Object = MibTableColumn
cfprFabricLanCloudFsmProgress = _CfprFabricLanCloudFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 8),
    _CfprFabricLanCloudFsmProgress_Type()
)
cfprFabricLanCloudFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmProgress.setStatus("current")
_CfprFabricLanCloudFsmRmtErrCode_Type = Gauge32
_CfprFabricLanCloudFsmRmtErrCode_Object = MibTableColumn
cfprFabricLanCloudFsmRmtErrCode = _CfprFabricLanCloudFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 9),
    _CfprFabricLanCloudFsmRmtErrCode_Type()
)
cfprFabricLanCloudFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmRmtErrCode.setStatus("current")
_CfprFabricLanCloudFsmRmtErrDescr_Type = SnmpAdminString
_CfprFabricLanCloudFsmRmtErrDescr_Object = MibTableColumn
cfprFabricLanCloudFsmRmtErrDescr = _CfprFabricLanCloudFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 10),
    _CfprFabricLanCloudFsmRmtErrDescr_Type()
)
cfprFabricLanCloudFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmRmtErrDescr.setStatus("current")
_CfprFabricLanCloudFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricLanCloudFsmRmtRslt_Object = MibTableColumn
cfprFabricLanCloudFsmRmtRslt = _CfprFabricLanCloudFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 73, 1, 11),
    _CfprFabricLanCloudFsmRmtRslt_Type()
)
cfprFabricLanCloudFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmRmtRslt.setStatus("current")
_CfprFabricLanCloudFsmStageTable_Object = MibTable
cfprFabricLanCloudFsmStageTable = _CfprFabricLanCloudFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74)
)
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageTable.setStatus("current")
_CfprFabricLanCloudFsmStageEntry_Object = MibTableRow
cfprFabricLanCloudFsmStageEntry = _CfprFabricLanCloudFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1)
)
cfprFabricLanCloudFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLanCloudFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageEntry.setStatus("current")
_CfprFabricLanCloudFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFabricLanCloudFsmStageInstanceId_Object = MibTableColumn
cfprFabricLanCloudFsmStageInstanceId = _CfprFabricLanCloudFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 1),
    _CfprFabricLanCloudFsmStageInstanceId_Type()
)
cfprFabricLanCloudFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageInstanceId.setStatus("current")
_CfprFabricLanCloudFsmStageDn_Type = CfprManagedObjectDn
_CfprFabricLanCloudFsmStageDn_Object = MibTableColumn
cfprFabricLanCloudFsmStageDn = _CfprFabricLanCloudFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 2),
    _CfprFabricLanCloudFsmStageDn_Type()
)
cfprFabricLanCloudFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageDn.setStatus("current")
_CfprFabricLanCloudFsmStageRn_Type = SnmpAdminString
_CfprFabricLanCloudFsmStageRn_Object = MibTableColumn
cfprFabricLanCloudFsmStageRn = _CfprFabricLanCloudFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 3),
    _CfprFabricLanCloudFsmStageRn_Type()
)
cfprFabricLanCloudFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageRn.setStatus("current")
_CfprFabricLanCloudFsmStageDescrData_Type = SnmpAdminString
_CfprFabricLanCloudFsmStageDescrData_Object = MibTableColumn
cfprFabricLanCloudFsmStageDescrData = _CfprFabricLanCloudFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 4),
    _CfprFabricLanCloudFsmStageDescrData_Type()
)
cfprFabricLanCloudFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageDescrData.setStatus("current")
_CfprFabricLanCloudFsmStageLastUpdateTime_Type = DateAndTime
_CfprFabricLanCloudFsmStageLastUpdateTime_Object = MibTableColumn
cfprFabricLanCloudFsmStageLastUpdateTime = _CfprFabricLanCloudFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 5),
    _CfprFabricLanCloudFsmStageLastUpdateTime_Type()
)
cfprFabricLanCloudFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageLastUpdateTime.setStatus("current")
_CfprFabricLanCloudFsmStageName_Type = CfprFabricLanCloudFsmStageName
_CfprFabricLanCloudFsmStageName_Object = MibTableColumn
cfprFabricLanCloudFsmStageName = _CfprFabricLanCloudFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 6),
    _CfprFabricLanCloudFsmStageName_Type()
)
cfprFabricLanCloudFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageName.setStatus("current")
_CfprFabricLanCloudFsmStageOrder_Type = Gauge32
_CfprFabricLanCloudFsmStageOrder_Object = MibTableColumn
cfprFabricLanCloudFsmStageOrder = _CfprFabricLanCloudFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 7),
    _CfprFabricLanCloudFsmStageOrder_Type()
)
cfprFabricLanCloudFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageOrder.setStatus("current")
_CfprFabricLanCloudFsmStageRetry_Type = Gauge32
_CfprFabricLanCloudFsmStageRetry_Object = MibTableColumn
cfprFabricLanCloudFsmStageRetry = _CfprFabricLanCloudFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 8),
    _CfprFabricLanCloudFsmStageRetry_Type()
)
cfprFabricLanCloudFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageRetry.setStatus("current")
_CfprFabricLanCloudFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFabricLanCloudFsmStageStageStatus_Object = MibTableColumn
cfprFabricLanCloudFsmStageStageStatus = _CfprFabricLanCloudFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 74, 1, 9),
    _CfprFabricLanCloudFsmStageStageStatus_Type()
)
cfprFabricLanCloudFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmStageStageStatus.setStatus("current")
_CfprFabricLanCloudFsmTaskTable_Object = MibTable
cfprFabricLanCloudFsmTaskTable = _CfprFabricLanCloudFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75)
)
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskTable.setStatus("current")
_CfprFabricLanCloudFsmTaskEntry_Object = MibTableRow
cfprFabricLanCloudFsmTaskEntry = _CfprFabricLanCloudFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75, 1)
)
cfprFabricLanCloudFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLanCloudFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskEntry.setStatus("current")
_CfprFabricLanCloudFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFabricLanCloudFsmTaskInstanceId_Object = MibTableColumn
cfprFabricLanCloudFsmTaskInstanceId = _CfprFabricLanCloudFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75, 1, 1),
    _CfprFabricLanCloudFsmTaskInstanceId_Type()
)
cfprFabricLanCloudFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskInstanceId.setStatus("current")
_CfprFabricLanCloudFsmTaskDn_Type = CfprManagedObjectDn
_CfprFabricLanCloudFsmTaskDn_Object = MibTableColumn
cfprFabricLanCloudFsmTaskDn = _CfprFabricLanCloudFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75, 1, 2),
    _CfprFabricLanCloudFsmTaskDn_Type()
)
cfprFabricLanCloudFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskDn.setStatus("current")
_CfprFabricLanCloudFsmTaskRn_Type = SnmpAdminString
_CfprFabricLanCloudFsmTaskRn_Object = MibTableColumn
cfprFabricLanCloudFsmTaskRn = _CfprFabricLanCloudFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75, 1, 3),
    _CfprFabricLanCloudFsmTaskRn_Type()
)
cfprFabricLanCloudFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskRn.setStatus("current")
_CfprFabricLanCloudFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFabricLanCloudFsmTaskCompletion_Object = MibTableColumn
cfprFabricLanCloudFsmTaskCompletion = _CfprFabricLanCloudFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75, 1, 4),
    _CfprFabricLanCloudFsmTaskCompletion_Type()
)
cfprFabricLanCloudFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskCompletion.setStatus("current")
_CfprFabricLanCloudFsmTaskFlags_Type = CfprFsmFlags
_CfprFabricLanCloudFsmTaskFlags_Object = MibTableColumn
cfprFabricLanCloudFsmTaskFlags = _CfprFabricLanCloudFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75, 1, 5),
    _CfprFabricLanCloudFsmTaskFlags_Type()
)
cfprFabricLanCloudFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskFlags.setStatus("current")
_CfprFabricLanCloudFsmTaskItem_Type = CfprFabricLanCloudFsmTaskItem
_CfprFabricLanCloudFsmTaskItem_Object = MibTableColumn
cfprFabricLanCloudFsmTaskItem = _CfprFabricLanCloudFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75, 1, 6),
    _CfprFabricLanCloudFsmTaskItem_Type()
)
cfprFabricLanCloudFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskItem.setStatus("current")
_CfprFabricLanCloudFsmTaskSeqId_Type = Gauge32
_CfprFabricLanCloudFsmTaskSeqId_Object = MibTableColumn
cfprFabricLanCloudFsmTaskSeqId = _CfprFabricLanCloudFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 75, 1, 7),
    _CfprFabricLanCloudFsmTaskSeqId_Type()
)
cfprFabricLanCloudFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanCloudFsmTaskSeqId.setStatus("current")
_CfprFabricLanMonCloudTable_Object = MibTable
cfprFabricLanMonCloudTable = _CfprFabricLanMonCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 76)
)
if mibBuilder.loadTexts:
    cfprFabricLanMonCloudTable.setStatus("current")
_CfprFabricLanMonCloudEntry_Object = MibTableRow
cfprFabricLanMonCloudEntry = _CfprFabricLanMonCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 76, 1)
)
cfprFabricLanMonCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLanMonCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLanMonCloudEntry.setStatus("current")
_CfprFabricLanMonCloudInstanceId_Type = CfprManagedObjectId
_CfprFabricLanMonCloudInstanceId_Object = MibTableColumn
cfprFabricLanMonCloudInstanceId = _CfprFabricLanMonCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 76, 1, 1),
    _CfprFabricLanMonCloudInstanceId_Type()
)
cfprFabricLanMonCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLanMonCloudInstanceId.setStatus("current")
_CfprFabricLanMonCloudDn_Type = CfprManagedObjectDn
_CfprFabricLanMonCloudDn_Object = MibTableColumn
cfprFabricLanMonCloudDn = _CfprFabricLanMonCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 76, 1, 2),
    _CfprFabricLanMonCloudDn_Type()
)
cfprFabricLanMonCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanMonCloudDn.setStatus("current")
_CfprFabricLanMonCloudRn_Type = SnmpAdminString
_CfprFabricLanMonCloudRn_Object = MibTableColumn
cfprFabricLanMonCloudRn = _CfprFabricLanMonCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 76, 1, 3),
    _CfprFabricLanMonCloudRn_Type()
)
cfprFabricLanMonCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanMonCloudRn.setStatus("current")
_CfprFabricLanMonCloudMode_Type = CfprFabricSwitchingMode
_CfprFabricLanMonCloudMode_Object = MibTableColumn
cfprFabricLanMonCloudMode = _CfprFabricLanMonCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 76, 1, 4),
    _CfprFabricLanMonCloudMode_Type()
)
cfprFabricLanMonCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanMonCloudMode.setStatus("current")
_CfprFabricLanPinGroupTable_Object = MibTable
cfprFabricLanPinGroupTable = _CfprFabricLanPinGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77)
)
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupTable.setStatus("current")
_CfprFabricLanPinGroupEntry_Object = MibTableRow
cfprFabricLanPinGroupEntry = _CfprFabricLanPinGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1)
)
cfprFabricLanPinGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLanPinGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupEntry.setStatus("current")
_CfprFabricLanPinGroupInstanceId_Type = CfprManagedObjectId
_CfprFabricLanPinGroupInstanceId_Object = MibTableColumn
cfprFabricLanPinGroupInstanceId = _CfprFabricLanPinGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 1),
    _CfprFabricLanPinGroupInstanceId_Type()
)
cfprFabricLanPinGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupInstanceId.setStatus("current")
_CfprFabricLanPinGroupDn_Type = CfprManagedObjectDn
_CfprFabricLanPinGroupDn_Object = MibTableColumn
cfprFabricLanPinGroupDn = _CfprFabricLanPinGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 2),
    _CfprFabricLanPinGroupDn_Type()
)
cfprFabricLanPinGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupDn.setStatus("current")
_CfprFabricLanPinGroupRn_Type = SnmpAdminString
_CfprFabricLanPinGroupRn_Object = MibTableColumn
cfprFabricLanPinGroupRn = _CfprFabricLanPinGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 3),
    _CfprFabricLanPinGroupRn_Type()
)
cfprFabricLanPinGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupRn.setStatus("current")
_CfprFabricLanPinGroupDescr_Type = SnmpAdminString
_CfprFabricLanPinGroupDescr_Object = MibTableColumn
cfprFabricLanPinGroupDescr = _CfprFabricLanPinGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 4),
    _CfprFabricLanPinGroupDescr_Type()
)
cfprFabricLanPinGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupDescr.setStatus("current")
_CfprFabricLanPinGroupIntId_Type = SnmpAdminString
_CfprFabricLanPinGroupIntId_Object = MibTableColumn
cfprFabricLanPinGroupIntId = _CfprFabricLanPinGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 5),
    _CfprFabricLanPinGroupIntId_Type()
)
cfprFabricLanPinGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupIntId.setStatus("current")
_CfprFabricLanPinGroupName_Type = SnmpAdminString
_CfprFabricLanPinGroupName_Object = MibTableColumn
cfprFabricLanPinGroupName = _CfprFabricLanPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 6),
    _CfprFabricLanPinGroupName_Type()
)
cfprFabricLanPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupName.setStatus("current")
_CfprFabricLanPinGroupPolicyLevel_Type = Gauge32
_CfprFabricLanPinGroupPolicyLevel_Object = MibTableColumn
cfprFabricLanPinGroupPolicyLevel = _CfprFabricLanPinGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 7),
    _CfprFabricLanPinGroupPolicyLevel_Type()
)
cfprFabricLanPinGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupPolicyLevel.setStatus("current")
_CfprFabricLanPinGroupPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricLanPinGroupPolicyOwner_Object = MibTableColumn
cfprFabricLanPinGroupPolicyOwner = _CfprFabricLanPinGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 8),
    _CfprFabricLanPinGroupPolicyOwner_Type()
)
cfprFabricLanPinGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupPolicyOwner.setStatus("current")
_CfprFabricLanPinGroupSize_Type = Gauge32
_CfprFabricLanPinGroupSize_Object = MibTableColumn
cfprFabricLanPinGroupSize = _CfprFabricLanPinGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 77, 1, 9),
    _CfprFabricLanPinGroupSize_Type()
)
cfprFabricLanPinGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinGroupSize.setStatus("current")
_CfprFabricLanPinTargetTable_Object = MibTable
cfprFabricLanPinTargetTable = _CfprFabricLanPinTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 78)
)
if mibBuilder.loadTexts:
    cfprFabricLanPinTargetTable.setStatus("current")
_CfprFabricLanPinTargetEntry_Object = MibTableRow
cfprFabricLanPinTargetEntry = _CfprFabricLanPinTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 78, 1)
)
cfprFabricLanPinTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLanPinTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLanPinTargetEntry.setStatus("current")
_CfprFabricLanPinTargetInstanceId_Type = CfprManagedObjectId
_CfprFabricLanPinTargetInstanceId_Object = MibTableColumn
cfprFabricLanPinTargetInstanceId = _CfprFabricLanPinTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 78, 1, 1),
    _CfprFabricLanPinTargetInstanceId_Type()
)
cfprFabricLanPinTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLanPinTargetInstanceId.setStatus("current")
_CfprFabricLanPinTargetDn_Type = CfprManagedObjectDn
_CfprFabricLanPinTargetDn_Object = MibTableColumn
cfprFabricLanPinTargetDn = _CfprFabricLanPinTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 78, 1, 2),
    _CfprFabricLanPinTargetDn_Type()
)
cfprFabricLanPinTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinTargetDn.setStatus("current")
_CfprFabricLanPinTargetRn_Type = SnmpAdminString
_CfprFabricLanPinTargetRn_Object = MibTableColumn
cfprFabricLanPinTargetRn = _CfprFabricLanPinTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 78, 1, 3),
    _CfprFabricLanPinTargetRn_Type()
)
cfprFabricLanPinTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinTargetRn.setStatus("current")
_CfprFabricLanPinTargetEpDn_Type = SnmpAdminString
_CfprFabricLanPinTargetEpDn_Object = MibTableColumn
cfprFabricLanPinTargetEpDn = _CfprFabricLanPinTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 78, 1, 4),
    _CfprFabricLanPinTargetEpDn_Type()
)
cfprFabricLanPinTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinTargetEpDn.setStatus("current")
_CfprFabricLanPinTargetFabricId_Type = SnmpAdminString
_CfprFabricLanPinTargetFabricId_Object = MibTableColumn
cfprFabricLanPinTargetFabricId = _CfprFabricLanPinTargetFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 78, 1, 5),
    _CfprFabricLanPinTargetFabricId_Type()
)
cfprFabricLanPinTargetFabricId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinTargetFabricId.setStatus("current")
_CfprFabricLanPinTargetTargetStatus_Type = CfprFabricTargetStatus
_CfprFabricLanPinTargetTargetStatus_Object = MibTableColumn
cfprFabricLanPinTargetTargetStatus = _CfprFabricLanPinTargetTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 78, 1, 6),
    _CfprFabricLanPinTargetTargetStatus_Type()
)
cfprFabricLanPinTargetTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLanPinTargetTargetStatus.setStatus("current")
_CfprFabricLastAckedSlotTable_Object = MibTable
cfprFabricLastAckedSlotTable = _CfprFabricLastAckedSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79)
)
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotTable.setStatus("current")
_CfprFabricLastAckedSlotEntry_Object = MibTableRow
cfprFabricLastAckedSlotEntry = _CfprFabricLastAckedSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79, 1)
)
cfprFabricLastAckedSlotEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLastAckedSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotEntry.setStatus("current")
_CfprFabricLastAckedSlotInstanceId_Type = CfprManagedObjectId
_CfprFabricLastAckedSlotInstanceId_Object = MibTableColumn
cfprFabricLastAckedSlotInstanceId = _CfprFabricLastAckedSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79, 1, 1),
    _CfprFabricLastAckedSlotInstanceId_Type()
)
cfprFabricLastAckedSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotInstanceId.setStatus("current")
_CfprFabricLastAckedSlotDn_Type = CfprManagedObjectDn
_CfprFabricLastAckedSlotDn_Object = MibTableColumn
cfprFabricLastAckedSlotDn = _CfprFabricLastAckedSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79, 1, 2),
    _CfprFabricLastAckedSlotDn_Type()
)
cfprFabricLastAckedSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotDn.setStatus("current")
_CfprFabricLastAckedSlotRn_Type = SnmpAdminString
_CfprFabricLastAckedSlotRn_Object = MibTableColumn
cfprFabricLastAckedSlotRn = _CfprFabricLastAckedSlotRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79, 1, 3),
    _CfprFabricLastAckedSlotRn_Type()
)
cfprFabricLastAckedSlotRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotRn.setStatus("current")
_CfprFabricLastAckedSlotBoardAggregationRole_Type = CfprEquipmentBoardAggregationRole
_CfprFabricLastAckedSlotBoardAggregationRole_Object = MibTableColumn
cfprFabricLastAckedSlotBoardAggregationRole = _CfprFabricLastAckedSlotBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79, 1, 4),
    _CfprFabricLastAckedSlotBoardAggregationRole_Type()
)
cfprFabricLastAckedSlotBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotBoardAggregationRole.setStatus("current")
_CfprFabricLastAckedSlotChassisId_Type = Gauge32
_CfprFabricLastAckedSlotChassisId_Object = MibTableColumn
cfprFabricLastAckedSlotChassisId = _CfprFabricLastAckedSlotChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79, 1, 5),
    _CfprFabricLastAckedSlotChassisId_Type()
)
cfprFabricLastAckedSlotChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotChassisId.setStatus("current")
_CfprFabricLastAckedSlotSlotId_Type = Gauge32
_CfprFabricLastAckedSlotSlotId_Object = MibTableColumn
cfprFabricLastAckedSlotSlotId = _CfprFabricLastAckedSlotSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79, 1, 6),
    _CfprFabricLastAckedSlotSlotId_Type()
)
cfprFabricLastAckedSlotSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotSlotId.setStatus("current")
_CfprFabricLastAckedSlotSwitchId_Type = CfprNetworkSwitchId
_CfprFabricLastAckedSlotSwitchId_Object = MibTableColumn
cfprFabricLastAckedSlotSwitchId = _CfprFabricLastAckedSlotSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 79, 1, 7),
    _CfprFabricLastAckedSlotSwitchId_Type()
)
cfprFabricLastAckedSlotSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLastAckedSlotSwitchId.setStatus("current")
_CfprFabricLocaleTable_Object = MibTable
cfprFabricLocaleTable = _CfprFabricLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80)
)
if mibBuilder.loadTexts:
    cfprFabricLocaleTable.setStatus("current")
_CfprFabricLocaleEntry_Object = MibTableRow
cfprFabricLocaleEntry = _CfprFabricLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1)
)
cfprFabricLocaleEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricLocaleEntry.setStatus("current")
_CfprFabricLocaleInstanceId_Type = CfprManagedObjectId
_CfprFabricLocaleInstanceId_Object = MibTableColumn
cfprFabricLocaleInstanceId = _CfprFabricLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 1),
    _CfprFabricLocaleInstanceId_Type()
)
cfprFabricLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricLocaleInstanceId.setStatus("current")
_CfprFabricLocaleDn_Type = CfprManagedObjectDn
_CfprFabricLocaleDn_Object = MibTableColumn
cfprFabricLocaleDn = _CfprFabricLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 2),
    _CfprFabricLocaleDn_Type()
)
cfprFabricLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleDn.setStatus("current")
_CfprFabricLocaleRn_Type = SnmpAdminString
_CfprFabricLocaleRn_Object = MibTableColumn
cfprFabricLocaleRn = _CfprFabricLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 3),
    _CfprFabricLocaleRn_Type()
)
cfprFabricLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleRn.setStatus("current")
_CfprFabricLocaleCType_Type = Gauge32
_CfprFabricLocaleCType_Object = MibTableColumn
cfprFabricLocaleCType = _CfprFabricLocaleCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 4),
    _CfprFabricLocaleCType_Type()
)
cfprFabricLocaleCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleCType.setStatus("current")
_CfprFabricLocaleChassisId_Type = Gauge32
_CfprFabricLocaleChassisId_Object = MibTableColumn
cfprFabricLocaleChassisId = _CfprFabricLocaleChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 5),
    _CfprFabricLocaleChassisId_Type()
)
cfprFabricLocaleChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleChassisId.setStatus("current")
_CfprFabricLocaleLocale_Type = CfprNetworkLocale
_CfprFabricLocaleLocale_Object = MibTableColumn
cfprFabricLocaleLocale = _CfprFabricLocaleLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 6),
    _CfprFabricLocaleLocale_Type()
)
cfprFabricLocaleLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleLocale.setStatus("current")
_CfprFabricLocaleName_Type = SnmpAdminString
_CfprFabricLocaleName_Object = MibTableColumn
cfprFabricLocaleName = _CfprFabricLocaleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 7),
    _CfprFabricLocaleName_Type()
)
cfprFabricLocaleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleName.setStatus("current")
_CfprFabricLocaleSide_Type = CfprNetworkSide
_CfprFabricLocaleSide_Object = MibTableColumn
cfprFabricLocaleSide = _CfprFabricLocaleSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 8),
    _CfprFabricLocaleSide_Type()
)
cfprFabricLocaleSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleSide.setStatus("current")
_CfprFabricLocaleSlotId_Type = Gauge32
_CfprFabricLocaleSlotId_Object = MibTableColumn
cfprFabricLocaleSlotId = _CfprFabricLocaleSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 9),
    _CfprFabricLocaleSlotId_Type()
)
cfprFabricLocaleSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleSlotId.setStatus("current")
_CfprFabricLocaleSwitchId_Type = CfprNetworkSwitchId
_CfprFabricLocaleSwitchId_Object = MibTableColumn
cfprFabricLocaleSwitchId = _CfprFabricLocaleSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 10),
    _CfprFabricLocaleSwitchId_Type()
)
cfprFabricLocaleSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleSwitchId.setStatus("current")
_CfprFabricLocaleTransport_Type = CfprNetworkTransport
_CfprFabricLocaleTransport_Object = MibTableColumn
cfprFabricLocaleTransport = _CfprFabricLocaleTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 11),
    _CfprFabricLocaleTransport_Type()
)
cfprFabricLocaleTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleTransport.setStatus("current")
_CfprFabricLocaleType_Type = CfprNetworkConnectionType
_CfprFabricLocaleType_Object = MibTableColumn
cfprFabricLocaleType = _CfprFabricLocaleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 80, 1, 12),
    _CfprFabricLocaleType_Type()
)
cfprFabricLocaleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricLocaleType.setStatus("current")
_CfprFabricMulticastPolicyTable_Object = MibTable
cfprFabricMulticastPolicyTable = _CfprFabricMulticastPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81)
)
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyTable.setStatus("current")
_CfprFabricMulticastPolicyEntry_Object = MibTableRow
cfprFabricMulticastPolicyEntry = _CfprFabricMulticastPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1)
)
cfprFabricMulticastPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricMulticastPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyEntry.setStatus("current")
_CfprFabricMulticastPolicyInstanceId_Type = CfprManagedObjectId
_CfprFabricMulticastPolicyInstanceId_Object = MibTableColumn
cfprFabricMulticastPolicyInstanceId = _CfprFabricMulticastPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 1),
    _CfprFabricMulticastPolicyInstanceId_Type()
)
cfprFabricMulticastPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyInstanceId.setStatus("current")
_CfprFabricMulticastPolicyDn_Type = CfprManagedObjectDn
_CfprFabricMulticastPolicyDn_Object = MibTableColumn
cfprFabricMulticastPolicyDn = _CfprFabricMulticastPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 2),
    _CfprFabricMulticastPolicyDn_Type()
)
cfprFabricMulticastPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyDn.setStatus("current")
_CfprFabricMulticastPolicyRn_Type = SnmpAdminString
_CfprFabricMulticastPolicyRn_Object = MibTableColumn
cfprFabricMulticastPolicyRn = _CfprFabricMulticastPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 3),
    _CfprFabricMulticastPolicyRn_Type()
)
cfprFabricMulticastPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyRn.setStatus("current")
_CfprFabricMulticastPolicyDescr_Type = SnmpAdminString
_CfprFabricMulticastPolicyDescr_Object = MibTableColumn
cfprFabricMulticastPolicyDescr = _CfprFabricMulticastPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 4),
    _CfprFabricMulticastPolicyDescr_Type()
)
cfprFabricMulticastPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyDescr.setStatus("current")
_CfprFabricMulticastPolicyIntId_Type = SnmpAdminString
_CfprFabricMulticastPolicyIntId_Object = MibTableColumn
cfprFabricMulticastPolicyIntId = _CfprFabricMulticastPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 5),
    _CfprFabricMulticastPolicyIntId_Type()
)
cfprFabricMulticastPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyIntId.setStatus("current")
_CfprFabricMulticastPolicyName_Type = SnmpAdminString
_CfprFabricMulticastPolicyName_Object = MibTableColumn
cfprFabricMulticastPolicyName = _CfprFabricMulticastPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 6),
    _CfprFabricMulticastPolicyName_Type()
)
cfprFabricMulticastPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyName.setStatus("current")
_CfprFabricMulticastPolicyPolicyLevel_Type = Gauge32
_CfprFabricMulticastPolicyPolicyLevel_Object = MibTableColumn
cfprFabricMulticastPolicyPolicyLevel = _CfprFabricMulticastPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 7),
    _CfprFabricMulticastPolicyPolicyLevel_Type()
)
cfprFabricMulticastPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyPolicyLevel.setStatus("current")
_CfprFabricMulticastPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricMulticastPolicyPolicyOwner_Object = MibTableColumn
cfprFabricMulticastPolicyPolicyOwner = _CfprFabricMulticastPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 8),
    _CfprFabricMulticastPolicyPolicyOwner_Type()
)
cfprFabricMulticastPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyPolicyOwner.setStatus("current")
_CfprFabricMulticastPolicyQuerierIpAddr_Type = InetAddressIPv4
_CfprFabricMulticastPolicyQuerierIpAddr_Object = MibTableColumn
cfprFabricMulticastPolicyQuerierIpAddr = _CfprFabricMulticastPolicyQuerierIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 9),
    _CfprFabricMulticastPolicyQuerierIpAddr_Type()
)
cfprFabricMulticastPolicyQuerierIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyQuerierIpAddr.setStatus("current")
_CfprFabricMulticastPolicyQuerierState_Type = CfprFabricQuerierType
_CfprFabricMulticastPolicyQuerierState_Object = MibTableColumn
cfprFabricMulticastPolicyQuerierState = _CfprFabricMulticastPolicyQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 10),
    _CfprFabricMulticastPolicyQuerierState_Type()
)
cfprFabricMulticastPolicyQuerierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicyQuerierState.setStatus("current")
_CfprFabricMulticastPolicySnoopingState_Type = CfprFabricSnoopingType
_CfprFabricMulticastPolicySnoopingState_Object = MibTableColumn
cfprFabricMulticastPolicySnoopingState = _CfprFabricMulticastPolicySnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 81, 1, 11),
    _CfprFabricMulticastPolicySnoopingState_Type()
)
cfprFabricMulticastPolicySnoopingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricMulticastPolicySnoopingState.setStatus("current")
_CfprFabricNetGroupTable_Object = MibTable
cfprFabricNetGroupTable = _CfprFabricNetGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82)
)
if mibBuilder.loadTexts:
    cfprFabricNetGroupTable.setStatus("current")
_CfprFabricNetGroupEntry_Object = MibTableRow
cfprFabricNetGroupEntry = _CfprFabricNetGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1)
)
cfprFabricNetGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricNetGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricNetGroupEntry.setStatus("current")
_CfprFabricNetGroupInstanceId_Type = CfprManagedObjectId
_CfprFabricNetGroupInstanceId_Object = MibTableColumn
cfprFabricNetGroupInstanceId = _CfprFabricNetGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 1),
    _CfprFabricNetGroupInstanceId_Type()
)
cfprFabricNetGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricNetGroupInstanceId.setStatus("current")
_CfprFabricNetGroupDn_Type = CfprManagedObjectDn
_CfprFabricNetGroupDn_Object = MibTableColumn
cfprFabricNetGroupDn = _CfprFabricNetGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 2),
    _CfprFabricNetGroupDn_Type()
)
cfprFabricNetGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupDn.setStatus("current")
_CfprFabricNetGroupRn_Type = SnmpAdminString
_CfprFabricNetGroupRn_Object = MibTableColumn
cfprFabricNetGroupRn = _CfprFabricNetGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 3),
    _CfprFabricNetGroupRn_Type()
)
cfprFabricNetGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupRn.setStatus("current")
_CfprFabricNetGroupAssigned_Type = Gauge32
_CfprFabricNetGroupAssigned_Object = MibTableColumn
cfprFabricNetGroupAssigned = _CfprFabricNetGroupAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 4),
    _CfprFabricNetGroupAssigned_Type()
)
cfprFabricNetGroupAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupAssigned.setStatus("current")
_CfprFabricNetGroupAssignmentOrder_Type = CfprPoolPoolAssignmentOrder
_CfprFabricNetGroupAssignmentOrder_Object = MibTableColumn
cfprFabricNetGroupAssignmentOrder = _CfprFabricNetGroupAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 5),
    _CfprFabricNetGroupAssignmentOrder_Type()
)
cfprFabricNetGroupAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupAssignmentOrder.setStatus("current")
_CfprFabricNetGroupDescr_Type = SnmpAdminString
_CfprFabricNetGroupDescr_Object = MibTableColumn
cfprFabricNetGroupDescr = _CfprFabricNetGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 6),
    _CfprFabricNetGroupDescr_Type()
)
cfprFabricNetGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupDescr.setStatus("current")
_CfprFabricNetGroupId_Type = Gauge32
_CfprFabricNetGroupId_Object = MibTableColumn
cfprFabricNetGroupId = _CfprFabricNetGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 7),
    _CfprFabricNetGroupId_Type()
)
cfprFabricNetGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupId.setStatus("current")
_CfprFabricNetGroupIntId_Type = SnmpAdminString
_CfprFabricNetGroupIntId_Object = MibTableColumn
cfprFabricNetGroupIntId = _CfprFabricNetGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 8),
    _CfprFabricNetGroupIntId_Type()
)
cfprFabricNetGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupIntId.setStatus("current")
_CfprFabricNetGroupName_Type = SnmpAdminString
_CfprFabricNetGroupName_Object = MibTableColumn
cfprFabricNetGroupName = _CfprFabricNetGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 9),
    _CfprFabricNetGroupName_Type()
)
cfprFabricNetGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupName.setStatus("current")
_CfprFabricNetGroupNativeNet_Type = SnmpAdminString
_CfprFabricNetGroupNativeNet_Object = MibTableColumn
cfprFabricNetGroupNativeNet = _CfprFabricNetGroupNativeNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 10),
    _CfprFabricNetGroupNativeNet_Type()
)
cfprFabricNetGroupNativeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupNativeNet.setStatus("current")
_CfprFabricNetGroupNativeNetDn_Type = SnmpAdminString
_CfprFabricNetGroupNativeNetDn_Object = MibTableColumn
cfprFabricNetGroupNativeNetDn = _CfprFabricNetGroupNativeNetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 11),
    _CfprFabricNetGroupNativeNetDn_Type()
)
cfprFabricNetGroupNativeNetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupNativeNetDn.setStatus("current")
_CfprFabricNetGroupOwner_Type = CfprFabricOwner
_CfprFabricNetGroupOwner_Object = MibTableColumn
cfprFabricNetGroupOwner = _CfprFabricNetGroupOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 12),
    _CfprFabricNetGroupOwner_Type()
)
cfprFabricNetGroupOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupOwner.setStatus("current")
_CfprFabricNetGroupPeerDn_Type = SnmpAdminString
_CfprFabricNetGroupPeerDn_Object = MibTableColumn
cfprFabricNetGroupPeerDn = _CfprFabricNetGroupPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 13),
    _CfprFabricNetGroupPeerDn_Type()
)
cfprFabricNetGroupPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupPeerDn.setStatus("current")
_CfprFabricNetGroupPolicyLevel_Type = Gauge32
_CfprFabricNetGroupPolicyLevel_Object = MibTableColumn
cfprFabricNetGroupPolicyLevel = _CfprFabricNetGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 14),
    _CfprFabricNetGroupPolicyLevel_Type()
)
cfprFabricNetGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupPolicyLevel.setStatus("current")
_CfprFabricNetGroupPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricNetGroupPolicyOwner_Object = MibTableColumn
cfprFabricNetGroupPolicyOwner = _CfprFabricNetGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 15),
    _CfprFabricNetGroupPolicyOwner_Type()
)
cfprFabricNetGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupPolicyOwner.setStatus("current")
_CfprFabricNetGroupSize_Type = Gauge32
_CfprFabricNetGroupSize_Object = MibTableColumn
cfprFabricNetGroupSize = _CfprFabricNetGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 16),
    _CfprFabricNetGroupSize_Type()
)
cfprFabricNetGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupSize.setStatus("current")
_CfprFabricNetGroupSwitchId_Type = CfprFabricNetGroupSwitchId
_CfprFabricNetGroupSwitchId_Object = MibTableColumn
cfprFabricNetGroupSwitchId = _CfprFabricNetGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 17),
    _CfprFabricNetGroupSwitchId_Type()
)
cfprFabricNetGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupSwitchId.setStatus("current")
_CfprFabricNetGroupType_Type = CfprFabricNetGroupType
_CfprFabricNetGroupType_Object = MibTableColumn
cfprFabricNetGroupType = _CfprFabricNetGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 82, 1, 18),
    _CfprFabricNetGroupType_Type()
)
cfprFabricNetGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricNetGroupType.setStatus("current")
_CfprFabricOrgVlanPolicyTable_Object = MibTable
cfprFabricOrgVlanPolicyTable = _CfprFabricOrgVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 93)
)
if mibBuilder.loadTexts:
    cfprFabricOrgVlanPolicyTable.setStatus("current")
_CfprFabricOrgVlanPolicyEntry_Object = MibTableRow
cfprFabricOrgVlanPolicyEntry = _CfprFabricOrgVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 93, 1)
)
cfprFabricOrgVlanPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricOrgVlanPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricOrgVlanPolicyEntry.setStatus("current")
_CfprFabricOrgVlanPolicyInstanceId_Type = CfprManagedObjectId
_CfprFabricOrgVlanPolicyInstanceId_Object = MibTableColumn
cfprFabricOrgVlanPolicyInstanceId = _CfprFabricOrgVlanPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 93, 1, 1),
    _CfprFabricOrgVlanPolicyInstanceId_Type()
)
cfprFabricOrgVlanPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricOrgVlanPolicyInstanceId.setStatus("current")
_CfprFabricOrgVlanPolicyDn_Type = CfprManagedObjectDn
_CfprFabricOrgVlanPolicyDn_Object = MibTableColumn
cfprFabricOrgVlanPolicyDn = _CfprFabricOrgVlanPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 93, 1, 2),
    _CfprFabricOrgVlanPolicyDn_Type()
)
cfprFabricOrgVlanPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricOrgVlanPolicyDn.setStatus("current")
_CfprFabricOrgVlanPolicyRn_Type = SnmpAdminString
_CfprFabricOrgVlanPolicyRn_Object = MibTableColumn
cfprFabricOrgVlanPolicyRn = _CfprFabricOrgVlanPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 93, 1, 3),
    _CfprFabricOrgVlanPolicyRn_Type()
)
cfprFabricOrgVlanPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricOrgVlanPolicyRn.setStatus("current")
_CfprFabricOrgVlanPolicyAdminState_Type = CfprFabricAdminState
_CfprFabricOrgVlanPolicyAdminState_Object = MibTableColumn
cfprFabricOrgVlanPolicyAdminState = _CfprFabricOrgVlanPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 93, 1, 4),
    _CfprFabricOrgVlanPolicyAdminState_Type()
)
cfprFabricOrgVlanPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricOrgVlanPolicyAdminState.setStatus("current")
_CfprFabricOrgVlanPolicyName_Type = SnmpAdminString
_CfprFabricOrgVlanPolicyName_Object = MibTableColumn
cfprFabricOrgVlanPolicyName = _CfprFabricOrgVlanPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 93, 1, 5),
    _CfprFabricOrgVlanPolicyName_Type()
)
cfprFabricOrgVlanPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricOrgVlanPolicyName.setStatus("current")
_CfprFabricPathTable_Object = MibTable
cfprFabricPathTable = _CfprFabricPathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94)
)
if mibBuilder.loadTexts:
    cfprFabricPathTable.setStatus("current")
_CfprFabricPathEntry_Object = MibTableRow
cfprFabricPathEntry = _CfprFabricPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1)
)
cfprFabricPathEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricPathInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricPathEntry.setStatus("current")
_CfprFabricPathInstanceId_Type = CfprManagedObjectId
_CfprFabricPathInstanceId_Object = MibTableColumn
cfprFabricPathInstanceId = _CfprFabricPathInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 1),
    _CfprFabricPathInstanceId_Type()
)
cfprFabricPathInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricPathInstanceId.setStatus("current")
_CfprFabricPathDn_Type = CfprManagedObjectDn
_CfprFabricPathDn_Object = MibTableColumn
cfprFabricPathDn = _CfprFabricPathDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 2),
    _CfprFabricPathDn_Type()
)
cfprFabricPathDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathDn.setStatus("current")
_CfprFabricPathRn_Type = SnmpAdminString
_CfprFabricPathRn_Object = MibTableColumn
cfprFabricPathRn = _CfprFabricPathRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 3),
    _CfprFabricPathRn_Type()
)
cfprFabricPathRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathRn.setStatus("current")
_CfprFabricPathCType_Type = Gauge32
_CfprFabricPathCType_Object = MibTableColumn
cfprFabricPathCType = _CfprFabricPathCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 4),
    _CfprFabricPathCType_Type()
)
cfprFabricPathCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathCType.setStatus("current")
_CfprFabricPathChassisId_Type = Gauge32
_CfprFabricPathChassisId_Object = MibTableColumn
cfprFabricPathChassisId = _CfprFabricPathChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 5),
    _CfprFabricPathChassisId_Type()
)
cfprFabricPathChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathChassisId.setStatus("current")
_CfprFabricPathEnacp_Type = Gauge32
_CfprFabricPathEnacp_Object = MibTableColumn
cfprFabricPathEnacp = _CfprFabricPathEnacp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 6),
    _CfprFabricPathEnacp_Type()
)
cfprFabricPathEnacp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEnacp.setStatus("current")
_CfprFabricPathId_Type = Gauge32
_CfprFabricPathId_Object = MibTableColumn
cfprFabricPathId = _CfprFabricPathId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 7),
    _CfprFabricPathId_Type()
)
cfprFabricPathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathId.setStatus("current")
_CfprFabricPathLocale_Type = CfprNetworkLocale
_CfprFabricPathLocale_Object = MibTableColumn
cfprFabricPathLocale = _CfprFabricPathLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 8),
    _CfprFabricPathLocale_Type()
)
cfprFabricPathLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathLocale.setStatus("current")
_CfprFabricPathName_Type = SnmpAdminString
_CfprFabricPathName_Object = MibTableColumn
cfprFabricPathName = _CfprFabricPathName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 9),
    _CfprFabricPathName_Type()
)
cfprFabricPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathName.setStatus("current")
_CfprFabricPathNsSize_Type = Gauge32
_CfprFabricPathNsSize_Object = MibTableColumn
cfprFabricPathNsSize = _CfprFabricPathNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 10),
    _CfprFabricPathNsSize_Type()
)
cfprFabricPathNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathNsSize.setStatus("current")
_CfprFabricPathSide_Type = CfprNetworkSide
_CfprFabricPathSide_Object = MibTableColumn
cfprFabricPathSide = _CfprFabricPathSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 11),
    _CfprFabricPathSide_Type()
)
cfprFabricPathSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathSide.setStatus("current")
_CfprFabricPathSwitchId_Type = CfprNetworkSwitchId
_CfprFabricPathSwitchId_Object = MibTableColumn
cfprFabricPathSwitchId = _CfprFabricPathSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 12),
    _CfprFabricPathSwitchId_Type()
)
cfprFabricPathSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathSwitchId.setStatus("current")
_CfprFabricPathTransport_Type = CfprNetworkTransport
_CfprFabricPathTransport_Object = MibTableColumn
cfprFabricPathTransport = _CfprFabricPathTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 13),
    _CfprFabricPathTransport_Type()
)
cfprFabricPathTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathTransport.setStatus("current")
_CfprFabricPathType_Type = CfprNetworkConnectionType
_CfprFabricPathType_Object = MibTableColumn
cfprFabricPathType = _CfprFabricPathType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 94, 1, 14),
    _CfprFabricPathType_Type()
)
cfprFabricPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathType.setStatus("current")
_CfprFabricPathConnTable_Object = MibTable
cfprFabricPathConnTable = _CfprFabricPathConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95)
)
if mibBuilder.loadTexts:
    cfprFabricPathConnTable.setStatus("current")
_CfprFabricPathConnEntry_Object = MibTableRow
cfprFabricPathConnEntry = _CfprFabricPathConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1)
)
cfprFabricPathConnEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricPathConnInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricPathConnEntry.setStatus("current")
_CfprFabricPathConnInstanceId_Type = CfprManagedObjectId
_CfprFabricPathConnInstanceId_Object = MibTableColumn
cfprFabricPathConnInstanceId = _CfprFabricPathConnInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1, 1),
    _CfprFabricPathConnInstanceId_Type()
)
cfprFabricPathConnInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricPathConnInstanceId.setStatus("current")
_CfprFabricPathConnDn_Type = CfprManagedObjectDn
_CfprFabricPathConnDn_Object = MibTableColumn
cfprFabricPathConnDn = _CfprFabricPathConnDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1, 2),
    _CfprFabricPathConnDn_Type()
)
cfprFabricPathConnDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathConnDn.setStatus("current")
_CfprFabricPathConnRn_Type = SnmpAdminString
_CfprFabricPathConnRn_Object = MibTableColumn
cfprFabricPathConnRn = _CfprFabricPathConnRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1, 3),
    _CfprFabricPathConnRn_Type()
)
cfprFabricPathConnRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathConnRn.setStatus("current")
_CfprFabricPathConnCType_Type = Gauge32
_CfprFabricPathConnCType_Object = MibTableColumn
cfprFabricPathConnCType = _CfprFabricPathConnCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1, 4),
    _CfprFabricPathConnCType_Type()
)
cfprFabricPathConnCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathConnCType.setStatus("current")
_CfprFabricPathConnLocale_Type = CfprNetworkLocale
_CfprFabricPathConnLocale_Object = MibTableColumn
cfprFabricPathConnLocale = _CfprFabricPathConnLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1, 5),
    _CfprFabricPathConnLocale_Type()
)
cfprFabricPathConnLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathConnLocale.setStatus("current")
_CfprFabricPathConnName_Type = SnmpAdminString
_CfprFabricPathConnName_Object = MibTableColumn
cfprFabricPathConnName = _CfprFabricPathConnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1, 6),
    _CfprFabricPathConnName_Type()
)
cfprFabricPathConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathConnName.setStatus("current")
_CfprFabricPathConnTransport_Type = CfprNetworkTransport
_CfprFabricPathConnTransport_Object = MibTableColumn
cfprFabricPathConnTransport = _CfprFabricPathConnTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1, 7),
    _CfprFabricPathConnTransport_Type()
)
cfprFabricPathConnTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathConnTransport.setStatus("current")
_CfprFabricPathConnType_Type = CfprNetworkConnectionType
_CfprFabricPathConnType_Object = MibTableColumn
cfprFabricPathConnType = _CfprFabricPathConnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 95, 1, 8),
    _CfprFabricPathConnType_Type()
)
cfprFabricPathConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathConnType.setStatus("current")
_CfprFabricPathEpTable_Object = MibTable
cfprFabricPathEpTable = _CfprFabricPathEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96)
)
if mibBuilder.loadTexts:
    cfprFabricPathEpTable.setStatus("current")
_CfprFabricPathEpEntry_Object = MibTableRow
cfprFabricPathEpEntry = _CfprFabricPathEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1)
)
cfprFabricPathEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricPathEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricPathEpEntry.setStatus("current")
_CfprFabricPathEpInstanceId_Type = CfprManagedObjectId
_CfprFabricPathEpInstanceId_Object = MibTableColumn
cfprFabricPathEpInstanceId = _CfprFabricPathEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 1),
    _CfprFabricPathEpInstanceId_Type()
)
cfprFabricPathEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricPathEpInstanceId.setStatus("current")
_CfprFabricPathEpDn_Type = CfprManagedObjectDn
_CfprFabricPathEpDn_Object = MibTableColumn
cfprFabricPathEpDn = _CfprFabricPathEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 2),
    _CfprFabricPathEpDn_Type()
)
cfprFabricPathEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpDn.setStatus("current")
_CfprFabricPathEpRn_Type = SnmpAdminString
_CfprFabricPathEpRn_Object = MibTableColumn
cfprFabricPathEpRn = _CfprFabricPathEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 3),
    _CfprFabricPathEpRn_Type()
)
cfprFabricPathEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpRn.setStatus("current")
_CfprFabricPathEpAggrPortId_Type = Gauge32
_CfprFabricPathEpAggrPortId_Object = MibTableColumn
cfprFabricPathEpAggrPortId = _CfprFabricPathEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 4),
    _CfprFabricPathEpAggrPortId_Type()
)
cfprFabricPathEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpAggrPortId.setStatus("current")
_CfprFabricPathEpCType_Type = Gauge32
_CfprFabricPathEpCType_Object = MibTableColumn
cfprFabricPathEpCType = _CfprFabricPathEpCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 5),
    _CfprFabricPathEpCType_Type()
)
cfprFabricPathEpCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpCType.setStatus("current")
_CfprFabricPathEpChassisId_Type = Gauge32
_CfprFabricPathEpChassisId_Object = MibTableColumn
cfprFabricPathEpChassisId = _CfprFabricPathEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 6),
    _CfprFabricPathEpChassisId_Type()
)
cfprFabricPathEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpChassisId.setStatus("current")
_CfprFabricPathEpDiagLldpTransmit_Type = TruthValue
_CfprFabricPathEpDiagLldpTransmit_Object = MibTableColumn
cfprFabricPathEpDiagLldpTransmit = _CfprFabricPathEpDiagLldpTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 7),
    _CfprFabricPathEpDiagLldpTransmit_Type()
)
cfprFabricPathEpDiagLldpTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpDiagLldpTransmit.setStatus("current")
_CfprFabricPathEpEpDn_Type = SnmpAdminString
_CfprFabricPathEpEpDn_Object = MibTableColumn
cfprFabricPathEpEpDn = _CfprFabricPathEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 8),
    _CfprFabricPathEpEpDn_Type()
)
cfprFabricPathEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpEpDn.setStatus("current")
_CfprFabricPathEpIfRole_Type = CfprNetworkPortRole
_CfprFabricPathEpIfRole_Object = MibTableColumn
cfprFabricPathEpIfRole = _CfprFabricPathEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 9),
    _CfprFabricPathEpIfRole_Type()
)
cfprFabricPathEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpIfRole.setStatus("current")
_CfprFabricPathEpIfType_Type = CfprFabricPathEpIfType
_CfprFabricPathEpIfType_Object = MibTableColumn
cfprFabricPathEpIfType = _CfprFabricPathEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 10),
    _CfprFabricPathEpIfType_Type()
)
cfprFabricPathEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpIfType.setStatus("current")
_CfprFabricPathEpLocale_Type = CfprFabricPathEpLocale
_CfprFabricPathEpLocale_Object = MibTableColumn
cfprFabricPathEpLocale = _CfprFabricPathEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 11),
    _CfprFabricPathEpLocale_Type()
)
cfprFabricPathEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpLocale.setStatus("current")
_CfprFabricPathEpName_Type = SnmpAdminString
_CfprFabricPathEpName_Object = MibTableColumn
cfprFabricPathEpName = _CfprFabricPathEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 12),
    _CfprFabricPathEpName_Type()
)
cfprFabricPathEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpName.setStatus("current")
_CfprFabricPathEpPeerAggrPortId_Type = Gauge32
_CfprFabricPathEpPeerAggrPortId_Object = MibTableColumn
cfprFabricPathEpPeerAggrPortId = _CfprFabricPathEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 13),
    _CfprFabricPathEpPeerAggrPortId_Type()
)
cfprFabricPathEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpPeerAggrPortId.setStatus("current")
_CfprFabricPathEpPeerChassisId_Type = Gauge32
_CfprFabricPathEpPeerChassisId_Object = MibTableColumn
cfprFabricPathEpPeerChassisId = _CfprFabricPathEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 14),
    _CfprFabricPathEpPeerChassisId_Type()
)
cfprFabricPathEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpPeerChassisId.setStatus("current")
_CfprFabricPathEpPeerDn_Type = SnmpAdminString
_CfprFabricPathEpPeerDn_Object = MibTableColumn
cfprFabricPathEpPeerDn = _CfprFabricPathEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 15),
    _CfprFabricPathEpPeerDn_Type()
)
cfprFabricPathEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpPeerDn.setStatus("current")
_CfprFabricPathEpPeerMac_Type = MacAddress
_CfprFabricPathEpPeerMac_Object = MibTableColumn
cfprFabricPathEpPeerMac = _CfprFabricPathEpPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 16),
    _CfprFabricPathEpPeerMac_Type()
)
cfprFabricPathEpPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpPeerMac.setStatus("current")
_CfprFabricPathEpPeerPortId_Type = Gauge32
_CfprFabricPathEpPeerPortId_Object = MibTableColumn
cfprFabricPathEpPeerPortId = _CfprFabricPathEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 17),
    _CfprFabricPathEpPeerPortId_Type()
)
cfprFabricPathEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpPeerPortId.setStatus("current")
_CfprFabricPathEpPeerSlotId_Type = Gauge32
_CfprFabricPathEpPeerSlotId_Object = MibTableColumn
cfprFabricPathEpPeerSlotId = _CfprFabricPathEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 18),
    _CfprFabricPathEpPeerSlotId_Type()
)
cfprFabricPathEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpPeerSlotId.setStatus("current")
_CfprFabricPathEpPortId_Type = Gauge32
_CfprFabricPathEpPortId_Object = MibTableColumn
cfprFabricPathEpPortId = _CfprFabricPathEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 19),
    _CfprFabricPathEpPortId_Type()
)
cfprFabricPathEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpPortId.setStatus("current")
_CfprFabricPathEpSide_Type = CfprNetworkSide
_CfprFabricPathEpSide_Object = MibTableColumn
cfprFabricPathEpSide = _CfprFabricPathEpSide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 20),
    _CfprFabricPathEpSide_Type()
)
cfprFabricPathEpSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpSide.setStatus("current")
_CfprFabricPathEpSlotId_Type = Gauge32
_CfprFabricPathEpSlotId_Object = MibTableColumn
cfprFabricPathEpSlotId = _CfprFabricPathEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 21),
    _CfprFabricPathEpSlotId_Type()
)
cfprFabricPathEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpSlotId.setStatus("current")
_CfprFabricPathEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricPathEpSwitchId_Object = MibTableColumn
cfprFabricPathEpSwitchId = _CfprFabricPathEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 22),
    _CfprFabricPathEpSwitchId_Type()
)
cfprFabricPathEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpSwitchId.setStatus("current")
_CfprFabricPathEpTransport_Type = CfprNetworkTransport
_CfprFabricPathEpTransport_Object = MibTableColumn
cfprFabricPathEpTransport = _CfprFabricPathEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 23),
    _CfprFabricPathEpTransport_Type()
)
cfprFabricPathEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpTransport.setStatus("current")
_CfprFabricPathEpType_Type = CfprNetworkConnectionType
_CfprFabricPathEpType_Object = MibTableColumn
cfprFabricPathEpType = _CfprFabricPathEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 96, 1, 24),
    _CfprFabricPathEpType_Type()
)
cfprFabricPathEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPathEpType.setStatus("current")
_CfprFabricPoolableVlanTable_Object = MibTable
cfprFabricPoolableVlanTable = _CfprFabricPoolableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 97)
)
if mibBuilder.loadTexts:
    cfprFabricPoolableVlanTable.setStatus("current")
_CfprFabricPoolableVlanEntry_Object = MibTableRow
cfprFabricPoolableVlanEntry = _CfprFabricPoolableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 97, 1)
)
cfprFabricPoolableVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricPoolableVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricPoolableVlanEntry.setStatus("current")
_CfprFabricPoolableVlanInstanceId_Type = CfprManagedObjectId
_CfprFabricPoolableVlanInstanceId_Object = MibTableColumn
cfprFabricPoolableVlanInstanceId = _CfprFabricPoolableVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 97, 1, 1),
    _CfprFabricPoolableVlanInstanceId_Type()
)
cfprFabricPoolableVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricPoolableVlanInstanceId.setStatus("current")
_CfprFabricPoolableVlanDn_Type = CfprManagedObjectDn
_CfprFabricPoolableVlanDn_Object = MibTableColumn
cfprFabricPoolableVlanDn = _CfprFabricPoolableVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 97, 1, 2),
    _CfprFabricPoolableVlanDn_Type()
)
cfprFabricPoolableVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPoolableVlanDn.setStatus("current")
_CfprFabricPoolableVlanRn_Type = SnmpAdminString
_CfprFabricPoolableVlanRn_Object = MibTableColumn
cfprFabricPoolableVlanRn = _CfprFabricPoolableVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 97, 1, 3),
    _CfprFabricPoolableVlanRn_Type()
)
cfprFabricPoolableVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPoolableVlanRn.setStatus("current")
_CfprFabricPoolableVlanId_Type = Unsigned64
_CfprFabricPoolableVlanId_Object = MibTableColumn
cfprFabricPoolableVlanId = _CfprFabricPoolableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 97, 1, 4),
    _CfprFabricPoolableVlanId_Type()
)
cfprFabricPoolableVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPoolableVlanId.setStatus("current")
_CfprFabricPoolableVlanPoolDn_Type = SnmpAdminString
_CfprFabricPoolableVlanPoolDn_Object = MibTableColumn
cfprFabricPoolableVlanPoolDn = _CfprFabricPoolableVlanPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 97, 1, 5),
    _CfprFabricPoolableVlanPoolDn_Type()
)
cfprFabricPoolableVlanPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPoolableVlanPoolDn.setStatus("current")
_CfprFabricPooledVlanTable_Object = MibTable
cfprFabricPooledVlanTable = _CfprFabricPooledVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98)
)
if mibBuilder.loadTexts:
    cfprFabricPooledVlanTable.setStatus("current")
_CfprFabricPooledVlanEntry_Object = MibTableRow
cfprFabricPooledVlanEntry = _CfprFabricPooledVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1)
)
cfprFabricPooledVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricPooledVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricPooledVlanEntry.setStatus("current")
_CfprFabricPooledVlanInstanceId_Type = CfprManagedObjectId
_CfprFabricPooledVlanInstanceId_Object = MibTableColumn
cfprFabricPooledVlanInstanceId = _CfprFabricPooledVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 1),
    _CfprFabricPooledVlanInstanceId_Type()
)
cfprFabricPooledVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanInstanceId.setStatus("current")
_CfprFabricPooledVlanDn_Type = CfprManagedObjectDn
_CfprFabricPooledVlanDn_Object = MibTableColumn
cfprFabricPooledVlanDn = _CfprFabricPooledVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 2),
    _CfprFabricPooledVlanDn_Type()
)
cfprFabricPooledVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanDn.setStatus("current")
_CfprFabricPooledVlanRn_Type = SnmpAdminString
_CfprFabricPooledVlanRn_Object = MibTableColumn
cfprFabricPooledVlanRn = _CfprFabricPooledVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 3),
    _CfprFabricPooledVlanRn_Type()
)
cfprFabricPooledVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanRn.setStatus("current")
_CfprFabricPooledVlanAssigned_Type = TruthValue
_CfprFabricPooledVlanAssigned_Object = MibTableColumn
cfprFabricPooledVlanAssigned = _CfprFabricPooledVlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 4),
    _CfprFabricPooledVlanAssigned_Type()
)
cfprFabricPooledVlanAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanAssigned.setStatus("current")
_CfprFabricPooledVlanAssignedToDn_Type = SnmpAdminString
_CfprFabricPooledVlanAssignedToDn_Object = MibTableColumn
cfprFabricPooledVlanAssignedToDn = _CfprFabricPooledVlanAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 5),
    _CfprFabricPooledVlanAssignedToDn_Type()
)
cfprFabricPooledVlanAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanAssignedToDn.setStatus("current")
_CfprFabricPooledVlanConfigIssues_Type = CfprFabricPoolMemberConfigIssues
_CfprFabricPooledVlanConfigIssues_Object = MibTableColumn
cfprFabricPooledVlanConfigIssues = _CfprFabricPooledVlanConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 6),
    _CfprFabricPooledVlanConfigIssues_Type()
)
cfprFabricPooledVlanConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanConfigIssues.setStatus("current")
_CfprFabricPooledVlanName_Type = SnmpAdminString
_CfprFabricPooledVlanName_Object = MibTableColumn
cfprFabricPooledVlanName = _CfprFabricPooledVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 7),
    _CfprFabricPooledVlanName_Type()
)
cfprFabricPooledVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanName.setStatus("current")
_CfprFabricPooledVlanPeerDn_Type = SnmpAdminString
_CfprFabricPooledVlanPeerDn_Object = MibTableColumn
cfprFabricPooledVlanPeerDn = _CfprFabricPooledVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 8),
    _CfprFabricPooledVlanPeerDn_Type()
)
cfprFabricPooledVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanPeerDn.setStatus("current")
_CfprFabricPooledVlanPoolableDn_Type = SnmpAdminString
_CfprFabricPooledVlanPoolableDn_Object = MibTableColumn
cfprFabricPooledVlanPoolableDn = _CfprFabricPooledVlanPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 9),
    _CfprFabricPooledVlanPoolableDn_Type()
)
cfprFabricPooledVlanPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanPoolableDn.setStatus("current")
_CfprFabricPooledVlanPrevAssignedToDn_Type = SnmpAdminString
_CfprFabricPooledVlanPrevAssignedToDn_Object = MibTableColumn
cfprFabricPooledVlanPrevAssignedToDn = _CfprFabricPooledVlanPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 98, 1, 10),
    _CfprFabricPooledVlanPrevAssignedToDn_Type()
)
cfprFabricPooledVlanPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricPooledVlanPrevAssignedToDn.setStatus("current")
_CfprFabricSanCloudTable_Object = MibTable
cfprFabricSanCloudTable = _CfprFabricSanCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99)
)
if mibBuilder.loadTexts:
    cfprFabricSanCloudTable.setStatus("current")
_CfprFabricSanCloudEntry_Object = MibTableRow
cfprFabricSanCloudEntry = _CfprFabricSanCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1)
)
cfprFabricSanCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSanCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSanCloudEntry.setStatus("current")
_CfprFabricSanCloudInstanceId_Type = CfprManagedObjectId
_CfprFabricSanCloudInstanceId_Object = MibTableColumn
cfprFabricSanCloudInstanceId = _CfprFabricSanCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 1),
    _CfprFabricSanCloudInstanceId_Type()
)
cfprFabricSanCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSanCloudInstanceId.setStatus("current")
_CfprFabricSanCloudDn_Type = CfprManagedObjectDn
_CfprFabricSanCloudDn_Object = MibTableColumn
cfprFabricSanCloudDn = _CfprFabricSanCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 2),
    _CfprFabricSanCloudDn_Type()
)
cfprFabricSanCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudDn.setStatus("current")
_CfprFabricSanCloudRn_Type = SnmpAdminString
_CfprFabricSanCloudRn_Object = MibTableColumn
cfprFabricSanCloudRn = _CfprFabricSanCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 3),
    _CfprFabricSanCloudRn_Type()
)
cfprFabricSanCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudRn.setStatus("current")
_CfprFabricSanCloudFsmDescr_Type = SnmpAdminString
_CfprFabricSanCloudFsmDescr_Object = MibTableColumn
cfprFabricSanCloudFsmDescr = _CfprFabricSanCloudFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 4),
    _CfprFabricSanCloudFsmDescr_Type()
)
cfprFabricSanCloudFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmDescr.setStatus("current")
_CfprFabricSanCloudFsmPrev_Type = SnmpAdminString
_CfprFabricSanCloudFsmPrev_Object = MibTableColumn
cfprFabricSanCloudFsmPrev = _CfprFabricSanCloudFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 5),
    _CfprFabricSanCloudFsmPrev_Type()
)
cfprFabricSanCloudFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmPrev.setStatus("current")
_CfprFabricSanCloudFsmProgr_Type = Gauge32
_CfprFabricSanCloudFsmProgr_Object = MibTableColumn
cfprFabricSanCloudFsmProgr = _CfprFabricSanCloudFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 6),
    _CfprFabricSanCloudFsmProgr_Type()
)
cfprFabricSanCloudFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmProgr.setStatus("current")
_CfprFabricSanCloudFsmRmtInvErrCode_Type = Gauge32
_CfprFabricSanCloudFsmRmtInvErrCode_Object = MibTableColumn
cfprFabricSanCloudFsmRmtInvErrCode = _CfprFabricSanCloudFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 7),
    _CfprFabricSanCloudFsmRmtInvErrCode_Type()
)
cfprFabricSanCloudFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmRmtInvErrCode.setStatus("current")
_CfprFabricSanCloudFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFabricSanCloudFsmRmtInvErrDescr_Object = MibTableColumn
cfprFabricSanCloudFsmRmtInvErrDescr = _CfprFabricSanCloudFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 8),
    _CfprFabricSanCloudFsmRmtInvErrDescr_Type()
)
cfprFabricSanCloudFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmRmtInvErrDescr.setStatus("current")
_CfprFabricSanCloudFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricSanCloudFsmRmtInvRslt_Object = MibTableColumn
cfprFabricSanCloudFsmRmtInvRslt = _CfprFabricSanCloudFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 9),
    _CfprFabricSanCloudFsmRmtInvRslt_Type()
)
cfprFabricSanCloudFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmRmtInvRslt.setStatus("current")
_CfprFabricSanCloudFsmStageDescr_Type = SnmpAdminString
_CfprFabricSanCloudFsmStageDescr_Object = MibTableColumn
cfprFabricSanCloudFsmStageDescr = _CfprFabricSanCloudFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 10),
    _CfprFabricSanCloudFsmStageDescr_Type()
)
cfprFabricSanCloudFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageDescr.setStatus("current")
_CfprFabricSanCloudFsmStamp_Type = DateAndTime
_CfprFabricSanCloudFsmStamp_Object = MibTableColumn
cfprFabricSanCloudFsmStamp = _CfprFabricSanCloudFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 11),
    _CfprFabricSanCloudFsmStamp_Type()
)
cfprFabricSanCloudFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStamp.setStatus("current")
_CfprFabricSanCloudFsmStatus_Type = SnmpAdminString
_CfprFabricSanCloudFsmStatus_Object = MibTableColumn
cfprFabricSanCloudFsmStatus = _CfprFabricSanCloudFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 12),
    _CfprFabricSanCloudFsmStatus_Type()
)
cfprFabricSanCloudFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStatus.setStatus("current")
_CfprFabricSanCloudFsmTry_Type = Gauge32
_CfprFabricSanCloudFsmTry_Object = MibTableColumn
cfprFabricSanCloudFsmTry = _CfprFabricSanCloudFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 13),
    _CfprFabricSanCloudFsmTry_Type()
)
cfprFabricSanCloudFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTry.setStatus("current")
_CfprFabricSanCloudMode_Type = CfprFabricSwitchingMode
_CfprFabricSanCloudMode_Object = MibTableColumn
cfprFabricSanCloudMode = _CfprFabricSanCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 99, 1, 14),
    _CfprFabricSanCloudMode_Type()
)
cfprFabricSanCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudMode.setStatus("current")
_CfprFabricSanCloudFsmTable_Object = MibTable
cfprFabricSanCloudFsmTable = _CfprFabricSanCloudFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100)
)
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTable.setStatus("current")
_CfprFabricSanCloudFsmEntry_Object = MibTableRow
cfprFabricSanCloudFsmEntry = _CfprFabricSanCloudFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1)
)
cfprFabricSanCloudFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSanCloudFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmEntry.setStatus("current")
_CfprFabricSanCloudFsmInstanceId_Type = CfprManagedObjectId
_CfprFabricSanCloudFsmInstanceId_Object = MibTableColumn
cfprFabricSanCloudFsmInstanceId = _CfprFabricSanCloudFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 1),
    _CfprFabricSanCloudFsmInstanceId_Type()
)
cfprFabricSanCloudFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmInstanceId.setStatus("current")
_CfprFabricSanCloudFsmDn_Type = CfprManagedObjectDn
_CfprFabricSanCloudFsmDn_Object = MibTableColumn
cfprFabricSanCloudFsmDn = _CfprFabricSanCloudFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 2),
    _CfprFabricSanCloudFsmDn_Type()
)
cfprFabricSanCloudFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmDn.setStatus("current")
_CfprFabricSanCloudFsmRn_Type = SnmpAdminString
_CfprFabricSanCloudFsmRn_Object = MibTableColumn
cfprFabricSanCloudFsmRn = _CfprFabricSanCloudFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 3),
    _CfprFabricSanCloudFsmRn_Type()
)
cfprFabricSanCloudFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmRn.setStatus("current")
_CfprFabricSanCloudFsmCompletionTime_Type = DateAndTime
_CfprFabricSanCloudFsmCompletionTime_Object = MibTableColumn
cfprFabricSanCloudFsmCompletionTime = _CfprFabricSanCloudFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 4),
    _CfprFabricSanCloudFsmCompletionTime_Type()
)
cfprFabricSanCloudFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmCompletionTime.setStatus("current")
_CfprFabricSanCloudFsmCurrentFsm_Type = CfprFabricSanCloudFsmCurrentFsm
_CfprFabricSanCloudFsmCurrentFsm_Object = MibTableColumn
cfprFabricSanCloudFsmCurrentFsm = _CfprFabricSanCloudFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 5),
    _CfprFabricSanCloudFsmCurrentFsm_Type()
)
cfprFabricSanCloudFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmCurrentFsm.setStatus("current")
_CfprFabricSanCloudFsmDescrData_Type = SnmpAdminString
_CfprFabricSanCloudFsmDescrData_Object = MibTableColumn
cfprFabricSanCloudFsmDescrData = _CfprFabricSanCloudFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 6),
    _CfprFabricSanCloudFsmDescrData_Type()
)
cfprFabricSanCloudFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmDescrData.setStatus("current")
_CfprFabricSanCloudFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFabricSanCloudFsmFsmStatus_Object = MibTableColumn
cfprFabricSanCloudFsmFsmStatus = _CfprFabricSanCloudFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 7),
    _CfprFabricSanCloudFsmFsmStatus_Type()
)
cfprFabricSanCloudFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmFsmStatus.setStatus("current")
_CfprFabricSanCloudFsmProgress_Type = Gauge32
_CfprFabricSanCloudFsmProgress_Object = MibTableColumn
cfprFabricSanCloudFsmProgress = _CfprFabricSanCloudFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 8),
    _CfprFabricSanCloudFsmProgress_Type()
)
cfprFabricSanCloudFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmProgress.setStatus("current")
_CfprFabricSanCloudFsmRmtErrCode_Type = Gauge32
_CfprFabricSanCloudFsmRmtErrCode_Object = MibTableColumn
cfprFabricSanCloudFsmRmtErrCode = _CfprFabricSanCloudFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 9),
    _CfprFabricSanCloudFsmRmtErrCode_Type()
)
cfprFabricSanCloudFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmRmtErrCode.setStatus("current")
_CfprFabricSanCloudFsmRmtErrDescr_Type = SnmpAdminString
_CfprFabricSanCloudFsmRmtErrDescr_Object = MibTableColumn
cfprFabricSanCloudFsmRmtErrDescr = _CfprFabricSanCloudFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 10),
    _CfprFabricSanCloudFsmRmtErrDescr_Type()
)
cfprFabricSanCloudFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmRmtErrDescr.setStatus("current")
_CfprFabricSanCloudFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricSanCloudFsmRmtRslt_Object = MibTableColumn
cfprFabricSanCloudFsmRmtRslt = _CfprFabricSanCloudFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 100, 1, 11),
    _CfprFabricSanCloudFsmRmtRslt_Type()
)
cfprFabricSanCloudFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmRmtRslt.setStatus("current")
_CfprFabricSanCloudFsmStageTable_Object = MibTable
cfprFabricSanCloudFsmStageTable = _CfprFabricSanCloudFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101)
)
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageTable.setStatus("current")
_CfprFabricSanCloudFsmStageEntry_Object = MibTableRow
cfprFabricSanCloudFsmStageEntry = _CfprFabricSanCloudFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1)
)
cfprFabricSanCloudFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSanCloudFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageEntry.setStatus("current")
_CfprFabricSanCloudFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFabricSanCloudFsmStageInstanceId_Object = MibTableColumn
cfprFabricSanCloudFsmStageInstanceId = _CfprFabricSanCloudFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 1),
    _CfprFabricSanCloudFsmStageInstanceId_Type()
)
cfprFabricSanCloudFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageInstanceId.setStatus("current")
_CfprFabricSanCloudFsmStageDn_Type = CfprManagedObjectDn
_CfprFabricSanCloudFsmStageDn_Object = MibTableColumn
cfprFabricSanCloudFsmStageDn = _CfprFabricSanCloudFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 2),
    _CfprFabricSanCloudFsmStageDn_Type()
)
cfprFabricSanCloudFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageDn.setStatus("current")
_CfprFabricSanCloudFsmStageRn_Type = SnmpAdminString
_CfprFabricSanCloudFsmStageRn_Object = MibTableColumn
cfprFabricSanCloudFsmStageRn = _CfprFabricSanCloudFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 3),
    _CfprFabricSanCloudFsmStageRn_Type()
)
cfprFabricSanCloudFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageRn.setStatus("current")
_CfprFabricSanCloudFsmStageDescrData_Type = SnmpAdminString
_CfprFabricSanCloudFsmStageDescrData_Object = MibTableColumn
cfprFabricSanCloudFsmStageDescrData = _CfprFabricSanCloudFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 4),
    _CfprFabricSanCloudFsmStageDescrData_Type()
)
cfprFabricSanCloudFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageDescrData.setStatus("current")
_CfprFabricSanCloudFsmStageLastUpdateTime_Type = DateAndTime
_CfprFabricSanCloudFsmStageLastUpdateTime_Object = MibTableColumn
cfprFabricSanCloudFsmStageLastUpdateTime = _CfprFabricSanCloudFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 5),
    _CfprFabricSanCloudFsmStageLastUpdateTime_Type()
)
cfprFabricSanCloudFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageLastUpdateTime.setStatus("current")
_CfprFabricSanCloudFsmStageName_Type = CfprFabricSanCloudFsmStageName
_CfprFabricSanCloudFsmStageName_Object = MibTableColumn
cfprFabricSanCloudFsmStageName = _CfprFabricSanCloudFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 6),
    _CfprFabricSanCloudFsmStageName_Type()
)
cfprFabricSanCloudFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageName.setStatus("current")
_CfprFabricSanCloudFsmStageOrder_Type = Gauge32
_CfprFabricSanCloudFsmStageOrder_Object = MibTableColumn
cfprFabricSanCloudFsmStageOrder = _CfprFabricSanCloudFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 7),
    _CfprFabricSanCloudFsmStageOrder_Type()
)
cfprFabricSanCloudFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageOrder.setStatus("current")
_CfprFabricSanCloudFsmStageRetry_Type = Gauge32
_CfprFabricSanCloudFsmStageRetry_Object = MibTableColumn
cfprFabricSanCloudFsmStageRetry = _CfprFabricSanCloudFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 8),
    _CfprFabricSanCloudFsmStageRetry_Type()
)
cfprFabricSanCloudFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageRetry.setStatus("current")
_CfprFabricSanCloudFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFabricSanCloudFsmStageStageStatus_Object = MibTableColumn
cfprFabricSanCloudFsmStageStageStatus = _CfprFabricSanCloudFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 101, 1, 9),
    _CfprFabricSanCloudFsmStageStageStatus_Type()
)
cfprFabricSanCloudFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmStageStageStatus.setStatus("current")
_CfprFabricSanCloudFsmTaskTable_Object = MibTable
cfprFabricSanCloudFsmTaskTable = _CfprFabricSanCloudFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102)
)
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskTable.setStatus("current")
_CfprFabricSanCloudFsmTaskEntry_Object = MibTableRow
cfprFabricSanCloudFsmTaskEntry = _CfprFabricSanCloudFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102, 1)
)
cfprFabricSanCloudFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSanCloudFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskEntry.setStatus("current")
_CfprFabricSanCloudFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFabricSanCloudFsmTaskInstanceId_Object = MibTableColumn
cfprFabricSanCloudFsmTaskInstanceId = _CfprFabricSanCloudFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102, 1, 1),
    _CfprFabricSanCloudFsmTaskInstanceId_Type()
)
cfprFabricSanCloudFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskInstanceId.setStatus("current")
_CfprFabricSanCloudFsmTaskDn_Type = CfprManagedObjectDn
_CfprFabricSanCloudFsmTaskDn_Object = MibTableColumn
cfprFabricSanCloudFsmTaskDn = _CfprFabricSanCloudFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102, 1, 2),
    _CfprFabricSanCloudFsmTaskDn_Type()
)
cfprFabricSanCloudFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskDn.setStatus("current")
_CfprFabricSanCloudFsmTaskRn_Type = SnmpAdminString
_CfprFabricSanCloudFsmTaskRn_Object = MibTableColumn
cfprFabricSanCloudFsmTaskRn = _CfprFabricSanCloudFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102, 1, 3),
    _CfprFabricSanCloudFsmTaskRn_Type()
)
cfprFabricSanCloudFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskRn.setStatus("current")
_CfprFabricSanCloudFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFabricSanCloudFsmTaskCompletion_Object = MibTableColumn
cfprFabricSanCloudFsmTaskCompletion = _CfprFabricSanCloudFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102, 1, 4),
    _CfprFabricSanCloudFsmTaskCompletion_Type()
)
cfprFabricSanCloudFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskCompletion.setStatus("current")
_CfprFabricSanCloudFsmTaskFlags_Type = CfprFsmFlags
_CfprFabricSanCloudFsmTaskFlags_Object = MibTableColumn
cfprFabricSanCloudFsmTaskFlags = _CfprFabricSanCloudFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102, 1, 5),
    _CfprFabricSanCloudFsmTaskFlags_Type()
)
cfprFabricSanCloudFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskFlags.setStatus("current")
_CfprFabricSanCloudFsmTaskItem_Type = CfprFabricSanCloudFsmTaskItem
_CfprFabricSanCloudFsmTaskItem_Object = MibTableColumn
cfprFabricSanCloudFsmTaskItem = _CfprFabricSanCloudFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102, 1, 6),
    _CfprFabricSanCloudFsmTaskItem_Type()
)
cfprFabricSanCloudFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskItem.setStatus("current")
_CfprFabricSanCloudFsmTaskSeqId_Type = Gauge32
_CfprFabricSanCloudFsmTaskSeqId_Object = MibTableColumn
cfprFabricSanCloudFsmTaskSeqId = _CfprFabricSanCloudFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 102, 1, 7),
    _CfprFabricSanCloudFsmTaskSeqId_Type()
)
cfprFabricSanCloudFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanCloudFsmTaskSeqId.setStatus("current")
_CfprFabricSanPinGroupTable_Object = MibTable
cfprFabricSanPinGroupTable = _CfprFabricSanPinGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104)
)
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupTable.setStatus("current")
_CfprFabricSanPinGroupEntry_Object = MibTableRow
cfprFabricSanPinGroupEntry = _CfprFabricSanPinGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1)
)
cfprFabricSanPinGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSanPinGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupEntry.setStatus("current")
_CfprFabricSanPinGroupInstanceId_Type = CfprManagedObjectId
_CfprFabricSanPinGroupInstanceId_Object = MibTableColumn
cfprFabricSanPinGroupInstanceId = _CfprFabricSanPinGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 1),
    _CfprFabricSanPinGroupInstanceId_Type()
)
cfprFabricSanPinGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupInstanceId.setStatus("current")
_CfprFabricSanPinGroupDn_Type = CfprManagedObjectDn
_CfprFabricSanPinGroupDn_Object = MibTableColumn
cfprFabricSanPinGroupDn = _CfprFabricSanPinGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 2),
    _CfprFabricSanPinGroupDn_Type()
)
cfprFabricSanPinGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupDn.setStatus("current")
_CfprFabricSanPinGroupRn_Type = SnmpAdminString
_CfprFabricSanPinGroupRn_Object = MibTableColumn
cfprFabricSanPinGroupRn = _CfprFabricSanPinGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 3),
    _CfprFabricSanPinGroupRn_Type()
)
cfprFabricSanPinGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupRn.setStatus("current")
_CfprFabricSanPinGroupDescr_Type = SnmpAdminString
_CfprFabricSanPinGroupDescr_Object = MibTableColumn
cfprFabricSanPinGroupDescr = _CfprFabricSanPinGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 4),
    _CfprFabricSanPinGroupDescr_Type()
)
cfprFabricSanPinGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupDescr.setStatus("current")
_CfprFabricSanPinGroupIntId_Type = SnmpAdminString
_CfprFabricSanPinGroupIntId_Object = MibTableColumn
cfprFabricSanPinGroupIntId = _CfprFabricSanPinGroupIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 5),
    _CfprFabricSanPinGroupIntId_Type()
)
cfprFabricSanPinGroupIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupIntId.setStatus("current")
_CfprFabricSanPinGroupName_Type = SnmpAdminString
_CfprFabricSanPinGroupName_Object = MibTableColumn
cfprFabricSanPinGroupName = _CfprFabricSanPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 6),
    _CfprFabricSanPinGroupName_Type()
)
cfprFabricSanPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupName.setStatus("current")
_CfprFabricSanPinGroupPolicyLevel_Type = Gauge32
_CfprFabricSanPinGroupPolicyLevel_Object = MibTableColumn
cfprFabricSanPinGroupPolicyLevel = _CfprFabricSanPinGroupPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 7),
    _CfprFabricSanPinGroupPolicyLevel_Type()
)
cfprFabricSanPinGroupPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupPolicyLevel.setStatus("current")
_CfprFabricSanPinGroupPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricSanPinGroupPolicyOwner_Object = MibTableColumn
cfprFabricSanPinGroupPolicyOwner = _CfprFabricSanPinGroupPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 8),
    _CfprFabricSanPinGroupPolicyOwner_Type()
)
cfprFabricSanPinGroupPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupPolicyOwner.setStatus("current")
_CfprFabricSanPinGroupSize_Type = Gauge32
_CfprFabricSanPinGroupSize_Object = MibTableColumn
cfprFabricSanPinGroupSize = _CfprFabricSanPinGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 104, 1, 9),
    _CfprFabricSanPinGroupSize_Type()
)
cfprFabricSanPinGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinGroupSize.setStatus("current")
_CfprFabricSanPinTargetTable_Object = MibTable
cfprFabricSanPinTargetTable = _CfprFabricSanPinTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 105)
)
if mibBuilder.loadTexts:
    cfprFabricSanPinTargetTable.setStatus("current")
_CfprFabricSanPinTargetEntry_Object = MibTableRow
cfprFabricSanPinTargetEntry = _CfprFabricSanPinTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 105, 1)
)
cfprFabricSanPinTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSanPinTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSanPinTargetEntry.setStatus("current")
_CfprFabricSanPinTargetInstanceId_Type = CfprManagedObjectId
_CfprFabricSanPinTargetInstanceId_Object = MibTableColumn
cfprFabricSanPinTargetInstanceId = _CfprFabricSanPinTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 105, 1, 1),
    _CfprFabricSanPinTargetInstanceId_Type()
)
cfprFabricSanPinTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSanPinTargetInstanceId.setStatus("current")
_CfprFabricSanPinTargetDn_Type = CfprManagedObjectDn
_CfprFabricSanPinTargetDn_Object = MibTableColumn
cfprFabricSanPinTargetDn = _CfprFabricSanPinTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 105, 1, 2),
    _CfprFabricSanPinTargetDn_Type()
)
cfprFabricSanPinTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinTargetDn.setStatus("current")
_CfprFabricSanPinTargetRn_Type = SnmpAdminString
_CfprFabricSanPinTargetRn_Object = MibTableColumn
cfprFabricSanPinTargetRn = _CfprFabricSanPinTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 105, 1, 3),
    _CfprFabricSanPinTargetRn_Type()
)
cfprFabricSanPinTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinTargetRn.setStatus("current")
_CfprFabricSanPinTargetEpDn_Type = SnmpAdminString
_CfprFabricSanPinTargetEpDn_Object = MibTableColumn
cfprFabricSanPinTargetEpDn = _CfprFabricSanPinTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 105, 1, 4),
    _CfprFabricSanPinTargetEpDn_Type()
)
cfprFabricSanPinTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinTargetEpDn.setStatus("current")
_CfprFabricSanPinTargetFabricId_Type = SnmpAdminString
_CfprFabricSanPinTargetFabricId_Object = MibTableColumn
cfprFabricSanPinTargetFabricId = _CfprFabricSanPinTargetFabricId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 105, 1, 5),
    _CfprFabricSanPinTargetFabricId_Type()
)
cfprFabricSanPinTargetFabricId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinTargetFabricId.setStatus("current")
_CfprFabricSanPinTargetTargetStatus_Type = CfprFabricTargetStatus
_CfprFabricSanPinTargetTargetStatus_Object = MibTableColumn
cfprFabricSanPinTargetTargetStatus = _CfprFabricSanPinTargetTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 105, 1, 6),
    _CfprFabricSanPinTargetTargetStatus_Type()
)
cfprFabricSanPinTargetTargetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSanPinTargetTargetStatus.setStatus("current")
_CfprFabricSubGroupTable_Object = MibTable
cfprFabricSubGroupTable = _CfprFabricSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106)
)
if mibBuilder.loadTexts:
    cfprFabricSubGroupTable.setStatus("current")
_CfprFabricSubGroupEntry_Object = MibTableRow
cfprFabricSubGroupEntry = _CfprFabricSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1)
)
cfprFabricSubGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSubGroupEntry.setStatus("current")
_CfprFabricSubGroupInstanceId_Type = CfprManagedObjectId
_CfprFabricSubGroupInstanceId_Object = MibTableColumn
cfprFabricSubGroupInstanceId = _CfprFabricSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 1),
    _CfprFabricSubGroupInstanceId_Type()
)
cfprFabricSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSubGroupInstanceId.setStatus("current")
_CfprFabricSubGroupDn_Type = CfprManagedObjectDn
_CfprFabricSubGroupDn_Object = MibTableColumn
cfprFabricSubGroupDn = _CfprFabricSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 2),
    _CfprFabricSubGroupDn_Type()
)
cfprFabricSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupDn.setStatus("current")
_CfprFabricSubGroupRn_Type = SnmpAdminString
_CfprFabricSubGroupRn_Object = MibTableColumn
cfprFabricSubGroupRn = _CfprFabricSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 3),
    _CfprFabricSubGroupRn_Type()
)
cfprFabricSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupRn.setStatus("current")
_CfprFabricSubGroupAggrPortId_Type = CfprFabricSubGroupAggrPortId
_CfprFabricSubGroupAggrPortId_Object = MibTableColumn
cfprFabricSubGroupAggrPortId = _CfprFabricSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 4),
    _CfprFabricSubGroupAggrPortId_Type()
)
cfprFabricSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupAggrPortId.setStatus("current")
_CfprFabricSubGroupConfigState_Type = CfprFabricSubGroupConfigState
_CfprFabricSubGroupConfigState_Object = MibTableColumn
cfprFabricSubGroupConfigState = _CfprFabricSubGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 5),
    _CfprFabricSubGroupConfigState_Type()
)
cfprFabricSubGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupConfigState.setStatus("current")
_CfprFabricSubGroupLicGP_Type = Unsigned64
_CfprFabricSubGroupLicGP_Object = MibTableColumn
cfprFabricSubGroupLicGP = _CfprFabricSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 6),
    _CfprFabricSubGroupLicGP_Type()
)
cfprFabricSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupLicGP.setStatus("current")
_CfprFabricSubGroupLicState_Type = CfprLicenseState
_CfprFabricSubGroupLicState_Object = MibTableColumn
cfprFabricSubGroupLicState = _CfprFabricSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 7),
    _CfprFabricSubGroupLicState_Type()
)
cfprFabricSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupLicState.setStatus("current")
_CfprFabricSubGroupLocale_Type = CfprNetworkLocale
_CfprFabricSubGroupLocale_Object = MibTableColumn
cfprFabricSubGroupLocale = _CfprFabricSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 8),
    _CfprFabricSubGroupLocale_Type()
)
cfprFabricSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupLocale.setStatus("current")
_CfprFabricSubGroupName_Type = SnmpAdminString
_CfprFabricSubGroupName_Object = MibTableColumn
cfprFabricSubGroupName = _CfprFabricSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 9),
    _CfprFabricSubGroupName_Type()
)
cfprFabricSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupName.setStatus("current")
_CfprFabricSubGroupSlotId_Type = CfprFabricSubGroupSlotId
_CfprFabricSubGroupSlotId_Object = MibTableColumn
cfprFabricSubGroupSlotId = _CfprFabricSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 10),
    _CfprFabricSubGroupSlotId_Type()
)
cfprFabricSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupSlotId.setStatus("current")
_CfprFabricSubGroupSwitchId_Type = CfprNetworkSwitchId
_CfprFabricSubGroupSwitchId_Object = MibTableColumn
cfprFabricSubGroupSwitchId = _CfprFabricSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 11),
    _CfprFabricSubGroupSwitchId_Type()
)
cfprFabricSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupSwitchId.setStatus("current")
_CfprFabricSubGroupTransport_Type = CfprNetworkTransport
_CfprFabricSubGroupTransport_Object = MibTableColumn
cfprFabricSubGroupTransport = _CfprFabricSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 12),
    _CfprFabricSubGroupTransport_Type()
)
cfprFabricSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupTransport.setStatus("current")
_CfprFabricSubGroupType_Type = CfprNetworkConnectionType
_CfprFabricSubGroupType_Object = MibTableColumn
cfprFabricSubGroupType = _CfprFabricSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 106, 1, 13),
    _CfprFabricSubGroupType_Type()
)
cfprFabricSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubGroupType.setStatus("current")
_CfprFabricSwChPhEpTable_Object = MibTable
cfprFabricSwChPhEpTable = _CfprFabricSwChPhEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107)
)
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpTable.setStatus("current")
_CfprFabricSwChPhEpEntry_Object = MibTableRow
cfprFabricSwChPhEpEntry = _CfprFabricSwChPhEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1)
)
cfprFabricSwChPhEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSwChPhEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpEntry.setStatus("current")
_CfprFabricSwChPhEpInstanceId_Type = CfprManagedObjectId
_CfprFabricSwChPhEpInstanceId_Object = MibTableColumn
cfprFabricSwChPhEpInstanceId = _CfprFabricSwChPhEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 1),
    _CfprFabricSwChPhEpInstanceId_Type()
)
cfprFabricSwChPhEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpInstanceId.setStatus("current")
_CfprFabricSwChPhEpDn_Type = CfprManagedObjectDn
_CfprFabricSwChPhEpDn_Object = MibTableColumn
cfprFabricSwChPhEpDn = _CfprFabricSwChPhEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 2),
    _CfprFabricSwChPhEpDn_Type()
)
cfprFabricSwChPhEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpDn.setStatus("current")
_CfprFabricSwChPhEpRn_Type = SnmpAdminString
_CfprFabricSwChPhEpRn_Object = MibTableColumn
cfprFabricSwChPhEpRn = _CfprFabricSwChPhEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 3),
    _CfprFabricSwChPhEpRn_Type()
)
cfprFabricSwChPhEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpRn.setStatus("current")
_CfprFabricSwChPhEpAdminState_Type = CfprFabricSwChPhEpAdminState
_CfprFabricSwChPhEpAdminState_Object = MibTableColumn
cfprFabricSwChPhEpAdminState = _CfprFabricSwChPhEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 4),
    _CfprFabricSwChPhEpAdminState_Type()
)
cfprFabricSwChPhEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpAdminState.setStatus("current")
_CfprFabricSwChPhEpAggrPortId_Type = Gauge32
_CfprFabricSwChPhEpAggrPortId_Object = MibTableColumn
cfprFabricSwChPhEpAggrPortId = _CfprFabricSwChPhEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 5),
    _CfprFabricSwChPhEpAggrPortId_Type()
)
cfprFabricSwChPhEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpAggrPortId.setStatus("current")
_CfprFabricSwChPhEpChassisId_Type = Gauge32
_CfprFabricSwChPhEpChassisId_Object = MibTableColumn
cfprFabricSwChPhEpChassisId = _CfprFabricSwChPhEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 6),
    _CfprFabricSwChPhEpChassisId_Type()
)
cfprFabricSwChPhEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpChassisId.setStatus("current")
_CfprFabricSwChPhEpEpDn_Type = SnmpAdminString
_CfprFabricSwChPhEpEpDn_Object = MibTableColumn
cfprFabricSwChPhEpEpDn = _CfprFabricSwChPhEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 7),
    _CfprFabricSwChPhEpEpDn_Type()
)
cfprFabricSwChPhEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpEpDn.setStatus("current")
_CfprFabricSwChPhEpEqType_Type = CfprEquipmentFabricEpType
_CfprFabricSwChPhEpEqType_Object = MibTableColumn
cfprFabricSwChPhEpEqType = _CfprFabricSwChPhEpEqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 8),
    _CfprFabricSwChPhEpEqType_Type()
)
cfprFabricSwChPhEpEqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpEqType.setStatus("current")
_CfprFabricSwChPhEpFltAggr_Type = Unsigned64
_CfprFabricSwChPhEpFltAggr_Object = MibTableColumn
cfprFabricSwChPhEpFltAggr = _CfprFabricSwChPhEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 9),
    _CfprFabricSwChPhEpFltAggr_Type()
)
cfprFabricSwChPhEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpFltAggr.setStatus("current")
_CfprFabricSwChPhEpIfRole_Type = CfprFabricSwChEpIfRole
_CfprFabricSwChPhEpIfRole_Object = MibTableColumn
cfprFabricSwChPhEpIfRole = _CfprFabricSwChPhEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 10),
    _CfprFabricSwChPhEpIfRole_Type()
)
cfprFabricSwChPhEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpIfRole.setStatus("current")
_CfprFabricSwChPhEpIfType_Type = CfprFabricPIoEpIfType
_CfprFabricSwChPhEpIfType_Object = MibTableColumn
cfprFabricSwChPhEpIfType = _CfprFabricSwChPhEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 11),
    _CfprFabricSwChPhEpIfType_Type()
)
cfprFabricSwChPhEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpIfType.setStatus("current")
_CfprFabricSwChPhEpLc_Type = CfprFabricLifeCycle
_CfprFabricSwChPhEpLc_Object = MibTableColumn
cfprFabricSwChPhEpLc = _CfprFabricSwChPhEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 12),
    _CfprFabricSwChPhEpLc_Type()
)
cfprFabricSwChPhEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpLc.setStatus("current")
_CfprFabricSwChPhEpLicGP_Type = Unsigned64
_CfprFabricSwChPhEpLicGP_Object = MibTableColumn
cfprFabricSwChPhEpLicGP = _CfprFabricSwChPhEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 13),
    _CfprFabricSwChPhEpLicGP_Type()
)
cfprFabricSwChPhEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpLicGP.setStatus("current")
_CfprFabricSwChPhEpLicState_Type = CfprLicenseState
_CfprFabricSwChPhEpLicState_Object = MibTableColumn
cfprFabricSwChPhEpLicState = _CfprFabricSwChPhEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 14),
    _CfprFabricSwChPhEpLicState_Type()
)
cfprFabricSwChPhEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpLicState.setStatus("current")
_CfprFabricSwChPhEpLocale_Type = CfprFabricInternalEpLocale
_CfprFabricSwChPhEpLocale_Object = MibTableColumn
cfprFabricSwChPhEpLocale = _CfprFabricSwChPhEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 15),
    _CfprFabricSwChPhEpLocale_Type()
)
cfprFabricSwChPhEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpLocale.setStatus("current")
_CfprFabricSwChPhEpModel_Type = SnmpAdminString
_CfprFabricSwChPhEpModel_Object = MibTableColumn
cfprFabricSwChPhEpModel = _CfprFabricSwChPhEpModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 16),
    _CfprFabricSwChPhEpModel_Type()
)
cfprFabricSwChPhEpModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpModel.setStatus("current")
_CfprFabricSwChPhEpName_Type = SnmpAdminString
_CfprFabricSwChPhEpName_Object = MibTableColumn
cfprFabricSwChPhEpName = _CfprFabricSwChPhEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 17),
    _CfprFabricSwChPhEpName_Type()
)
cfprFabricSwChPhEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpName.setStatus("current")
_CfprFabricSwChPhEpOperState_Type = CfprFabricPIoEpOperState
_CfprFabricSwChPhEpOperState_Object = MibTableColumn
cfprFabricSwChPhEpOperState = _CfprFabricSwChPhEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 18),
    _CfprFabricSwChPhEpOperState_Type()
)
cfprFabricSwChPhEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpOperState.setStatus("current")
_CfprFabricSwChPhEpOperStateReason_Type = SnmpAdminString
_CfprFabricSwChPhEpOperStateReason_Object = MibTableColumn
cfprFabricSwChPhEpOperStateReason = _CfprFabricSwChPhEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 19),
    _CfprFabricSwChPhEpOperStateReason_Type()
)
cfprFabricSwChPhEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpOperStateReason.setStatus("current")
_CfprFabricSwChPhEpPeerAggrPortId_Type = Gauge32
_CfprFabricSwChPhEpPeerAggrPortId_Object = MibTableColumn
cfprFabricSwChPhEpPeerAggrPortId = _CfprFabricSwChPhEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 20),
    _CfprFabricSwChPhEpPeerAggrPortId_Type()
)
cfprFabricSwChPhEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpPeerAggrPortId.setStatus("current")
_CfprFabricSwChPhEpPeerChassisId_Type = Gauge32
_CfprFabricSwChPhEpPeerChassisId_Object = MibTableColumn
cfprFabricSwChPhEpPeerChassisId = _CfprFabricSwChPhEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 21),
    _CfprFabricSwChPhEpPeerChassisId_Type()
)
cfprFabricSwChPhEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpPeerChassisId.setStatus("current")
_CfprFabricSwChPhEpPeerDn_Type = SnmpAdminString
_CfprFabricSwChPhEpPeerDn_Object = MibTableColumn
cfprFabricSwChPhEpPeerDn = _CfprFabricSwChPhEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 22),
    _CfprFabricSwChPhEpPeerDn_Type()
)
cfprFabricSwChPhEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpPeerDn.setStatus("current")
_CfprFabricSwChPhEpPeerPortId_Type = Gauge32
_CfprFabricSwChPhEpPeerPortId_Object = MibTableColumn
cfprFabricSwChPhEpPeerPortId = _CfprFabricSwChPhEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 23),
    _CfprFabricSwChPhEpPeerPortId_Type()
)
cfprFabricSwChPhEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpPeerPortId.setStatus("current")
_CfprFabricSwChPhEpPeerSlotId_Type = Gauge32
_CfprFabricSwChPhEpPeerSlotId_Object = MibTableColumn
cfprFabricSwChPhEpPeerSlotId = _CfprFabricSwChPhEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 24),
    _CfprFabricSwChPhEpPeerSlotId_Type()
)
cfprFabricSwChPhEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpPeerSlotId.setStatus("current")
_CfprFabricSwChPhEpPortId_Type = CfprFabricPIoEpPortId
_CfprFabricSwChPhEpPortId_Object = MibTableColumn
cfprFabricSwChPhEpPortId = _CfprFabricSwChPhEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 25),
    _CfprFabricSwChPhEpPortId_Type()
)
cfprFabricSwChPhEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpPortId.setStatus("current")
_CfprFabricSwChPhEpRevision_Type = SnmpAdminString
_CfprFabricSwChPhEpRevision_Object = MibTableColumn
cfprFabricSwChPhEpRevision = _CfprFabricSwChPhEpRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 26),
    _CfprFabricSwChPhEpRevision_Type()
)
cfprFabricSwChPhEpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpRevision.setStatus("current")
_CfprFabricSwChPhEpSerial_Type = SnmpAdminString
_CfprFabricSwChPhEpSerial_Object = MibTableColumn
cfprFabricSwChPhEpSerial = _CfprFabricSwChPhEpSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 27),
    _CfprFabricSwChPhEpSerial_Type()
)
cfprFabricSwChPhEpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpSerial.setStatus("current")
_CfprFabricSwChPhEpSlotId_Type = CfprFabricPIoEpSlotId
_CfprFabricSwChPhEpSlotId_Object = MibTableColumn
cfprFabricSwChPhEpSlotId = _CfprFabricSwChPhEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 28),
    _CfprFabricSwChPhEpSlotId_Type()
)
cfprFabricSwChPhEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpSlotId.setStatus("current")
_CfprFabricSwChPhEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricSwChPhEpSwitchId_Object = MibTableColumn
cfprFabricSwChPhEpSwitchId = _CfprFabricSwChPhEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 29),
    _CfprFabricSwChPhEpSwitchId_Type()
)
cfprFabricSwChPhEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpSwitchId.setStatus("current")
_CfprFabricSwChPhEpTransport_Type = CfprNetworkTransport
_CfprFabricSwChPhEpTransport_Object = MibTableColumn
cfprFabricSwChPhEpTransport = _CfprFabricSwChPhEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 30),
    _CfprFabricSwChPhEpTransport_Type()
)
cfprFabricSwChPhEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpTransport.setStatus("current")
_CfprFabricSwChPhEpType_Type = CfprFabricSwChEpType
_CfprFabricSwChPhEpType_Object = MibTableColumn
cfprFabricSwChPhEpType = _CfprFabricSwChPhEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 31),
    _CfprFabricSwChPhEpType_Type()
)
cfprFabricSwChPhEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpType.setStatus("current")
_CfprFabricSwChPhEpVendor_Type = SnmpAdminString
_CfprFabricSwChPhEpVendor_Object = MibTableColumn
cfprFabricSwChPhEpVendor = _CfprFabricSwChPhEpVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 107, 1, 32),
    _CfprFabricSwChPhEpVendor_Type()
)
cfprFabricSwChPhEpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwChPhEpVendor.setStatus("current")
_CfprFabricSwSubGroupTable_Object = MibTable
cfprFabricSwSubGroupTable = _CfprFabricSwSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108)
)
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupTable.setStatus("current")
_CfprFabricSwSubGroupEntry_Object = MibTableRow
cfprFabricSwSubGroupEntry = _CfprFabricSwSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1)
)
cfprFabricSwSubGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSwSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupEntry.setStatus("current")
_CfprFabricSwSubGroupInstanceId_Type = CfprManagedObjectId
_CfprFabricSwSubGroupInstanceId_Object = MibTableColumn
cfprFabricSwSubGroupInstanceId = _CfprFabricSwSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 1),
    _CfprFabricSwSubGroupInstanceId_Type()
)
cfprFabricSwSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupInstanceId.setStatus("current")
_CfprFabricSwSubGroupDn_Type = CfprManagedObjectDn
_CfprFabricSwSubGroupDn_Object = MibTableColumn
cfprFabricSwSubGroupDn = _CfprFabricSwSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 2),
    _CfprFabricSwSubGroupDn_Type()
)
cfprFabricSwSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupDn.setStatus("current")
_CfprFabricSwSubGroupRn_Type = SnmpAdminString
_CfprFabricSwSubGroupRn_Object = MibTableColumn
cfprFabricSwSubGroupRn = _CfprFabricSwSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 3),
    _CfprFabricSwSubGroupRn_Type()
)
cfprFabricSwSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupRn.setStatus("current")
_CfprFabricSwSubGroupAggrPortId_Type = CfprFabricSwSubGroupAggrPortId
_CfprFabricSwSubGroupAggrPortId_Object = MibTableColumn
cfprFabricSwSubGroupAggrPortId = _CfprFabricSwSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 4),
    _CfprFabricSwSubGroupAggrPortId_Type()
)
cfprFabricSwSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupAggrPortId.setStatus("current")
_CfprFabricSwSubGroupConfigState_Type = CfprFabricSwSubGroupConfigState
_CfprFabricSwSubGroupConfigState_Object = MibTableColumn
cfprFabricSwSubGroupConfigState = _CfprFabricSwSubGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 5),
    _CfprFabricSwSubGroupConfigState_Type()
)
cfprFabricSwSubGroupConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupConfigState.setStatus("current")
_CfprFabricSwSubGroupLicGP_Type = Unsigned64
_CfprFabricSwSubGroupLicGP_Object = MibTableColumn
cfprFabricSwSubGroupLicGP = _CfprFabricSwSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 6),
    _CfprFabricSwSubGroupLicGP_Type()
)
cfprFabricSwSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupLicGP.setStatus("current")
_CfprFabricSwSubGroupLicState_Type = CfprLicenseState
_CfprFabricSwSubGroupLicState_Object = MibTableColumn
cfprFabricSwSubGroupLicState = _CfprFabricSwSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 7),
    _CfprFabricSwSubGroupLicState_Type()
)
cfprFabricSwSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupLicState.setStatus("current")
_CfprFabricSwSubGroupLocale_Type = CfprNetworkLocale
_CfprFabricSwSubGroupLocale_Object = MibTableColumn
cfprFabricSwSubGroupLocale = _CfprFabricSwSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 8),
    _CfprFabricSwSubGroupLocale_Type()
)
cfprFabricSwSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupLocale.setStatus("current")
_CfprFabricSwSubGroupName_Type = SnmpAdminString
_CfprFabricSwSubGroupName_Object = MibTableColumn
cfprFabricSwSubGroupName = _CfprFabricSwSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 9),
    _CfprFabricSwSubGroupName_Type()
)
cfprFabricSwSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupName.setStatus("current")
_CfprFabricSwSubGroupSlotId_Type = CfprFabricSwSubGroupSlotId
_CfprFabricSwSubGroupSlotId_Object = MibTableColumn
cfprFabricSwSubGroupSlotId = _CfprFabricSwSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 10),
    _CfprFabricSwSubGroupSlotId_Type()
)
cfprFabricSwSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupSlotId.setStatus("current")
_CfprFabricSwSubGroupSwitchId_Type = CfprNetworkSwitchId
_CfprFabricSwSubGroupSwitchId_Object = MibTableColumn
cfprFabricSwSubGroupSwitchId = _CfprFabricSwSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 11),
    _CfprFabricSwSubGroupSwitchId_Type()
)
cfprFabricSwSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupSwitchId.setStatus("current")
_CfprFabricSwSubGroupTransport_Type = CfprNetworkTransport
_CfprFabricSwSubGroupTransport_Object = MibTableColumn
cfprFabricSwSubGroupTransport = _CfprFabricSwSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 12),
    _CfprFabricSwSubGroupTransport_Type()
)
cfprFabricSwSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupTransport.setStatus("current")
_CfprFabricSwSubGroupType_Type = CfprNetworkConnectionType
_CfprFabricSwSubGroupType_Object = MibTableColumn
cfprFabricSwSubGroupType = _CfprFabricSwSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 108, 1, 13),
    _CfprFabricSwSubGroupType_Type()
)
cfprFabricSwSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSwSubGroupType.setStatus("current")
_CfprFabricUdldLinkPolicyTable_Object = MibTable
cfprFabricUdldLinkPolicyTable = _CfprFabricUdldLinkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109)
)
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyTable.setStatus("current")
_CfprFabricUdldLinkPolicyEntry_Object = MibTableRow
cfprFabricUdldLinkPolicyEntry = _CfprFabricUdldLinkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1)
)
cfprFabricUdldLinkPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricUdldLinkPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyEntry.setStatus("current")
_CfprFabricUdldLinkPolicyInstanceId_Type = CfprManagedObjectId
_CfprFabricUdldLinkPolicyInstanceId_Object = MibTableColumn
cfprFabricUdldLinkPolicyInstanceId = _CfprFabricUdldLinkPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 1),
    _CfprFabricUdldLinkPolicyInstanceId_Type()
)
cfprFabricUdldLinkPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyInstanceId.setStatus("current")
_CfprFabricUdldLinkPolicyDn_Type = CfprManagedObjectDn
_CfprFabricUdldLinkPolicyDn_Object = MibTableColumn
cfprFabricUdldLinkPolicyDn = _CfprFabricUdldLinkPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 2),
    _CfprFabricUdldLinkPolicyDn_Type()
)
cfprFabricUdldLinkPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyDn.setStatus("current")
_CfprFabricUdldLinkPolicyRn_Type = SnmpAdminString
_CfprFabricUdldLinkPolicyRn_Object = MibTableColumn
cfprFabricUdldLinkPolicyRn = _CfprFabricUdldLinkPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 3),
    _CfprFabricUdldLinkPolicyRn_Type()
)
cfprFabricUdldLinkPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyRn.setStatus("current")
_CfprFabricUdldLinkPolicyAdminState_Type = CfprFabricUdldLinkPolicyAdminState
_CfprFabricUdldLinkPolicyAdminState_Object = MibTableColumn
cfprFabricUdldLinkPolicyAdminState = _CfprFabricUdldLinkPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 4),
    _CfprFabricUdldLinkPolicyAdminState_Type()
)
cfprFabricUdldLinkPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyAdminState.setStatus("current")
_CfprFabricUdldLinkPolicyDescr_Type = SnmpAdminString
_CfprFabricUdldLinkPolicyDescr_Object = MibTableColumn
cfprFabricUdldLinkPolicyDescr = _CfprFabricUdldLinkPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 5),
    _CfprFabricUdldLinkPolicyDescr_Type()
)
cfprFabricUdldLinkPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyDescr.setStatus("current")
_CfprFabricUdldLinkPolicyIntId_Type = SnmpAdminString
_CfprFabricUdldLinkPolicyIntId_Object = MibTableColumn
cfprFabricUdldLinkPolicyIntId = _CfprFabricUdldLinkPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 6),
    _CfprFabricUdldLinkPolicyIntId_Type()
)
cfprFabricUdldLinkPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyIntId.setStatus("current")
_CfprFabricUdldLinkPolicyMode_Type = CfprFabricUdldLinkPolicyMode
_CfprFabricUdldLinkPolicyMode_Object = MibTableColumn
cfprFabricUdldLinkPolicyMode = _CfprFabricUdldLinkPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 7),
    _CfprFabricUdldLinkPolicyMode_Type()
)
cfprFabricUdldLinkPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyMode.setStatus("current")
_CfprFabricUdldLinkPolicyName_Type = SnmpAdminString
_CfprFabricUdldLinkPolicyName_Object = MibTableColumn
cfprFabricUdldLinkPolicyName = _CfprFabricUdldLinkPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 8),
    _CfprFabricUdldLinkPolicyName_Type()
)
cfprFabricUdldLinkPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyName.setStatus("current")
_CfprFabricUdldLinkPolicyPolicyLevel_Type = Gauge32
_CfprFabricUdldLinkPolicyPolicyLevel_Object = MibTableColumn
cfprFabricUdldLinkPolicyPolicyLevel = _CfprFabricUdldLinkPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 9),
    _CfprFabricUdldLinkPolicyPolicyLevel_Type()
)
cfprFabricUdldLinkPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyPolicyLevel.setStatus("current")
_CfprFabricUdldLinkPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricUdldLinkPolicyPolicyOwner_Object = MibTableColumn
cfprFabricUdldLinkPolicyPolicyOwner = _CfprFabricUdldLinkPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 10),
    _CfprFabricUdldLinkPolicyPolicyOwner_Type()
)
cfprFabricUdldLinkPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyPolicyOwner.setStatus("current")
_CfprFabricUdldLinkPolicyProtocol_Type = CfprFabricEthUdldPolicyProtocol
_CfprFabricUdldLinkPolicyProtocol_Object = MibTableColumn
cfprFabricUdldLinkPolicyProtocol = _CfprFabricUdldLinkPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 11),
    _CfprFabricUdldLinkPolicyProtocol_Type()
)
cfprFabricUdldLinkPolicyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyProtocol.setStatus("current")
_CfprFabricUdldLinkPolicyType_Type = CfprFabricEthLinkPolicyType
_CfprFabricUdldLinkPolicyType_Object = MibTableColumn
cfprFabricUdldLinkPolicyType = _CfprFabricUdldLinkPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 109, 1, 12),
    _CfprFabricUdldLinkPolicyType_Type()
)
cfprFabricUdldLinkPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldLinkPolicyType.setStatus("current")
_CfprFabricUdldPolicyTable_Object = MibTable
cfprFabricUdldPolicyTable = _CfprFabricUdldPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110)
)
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyTable.setStatus("current")
_CfprFabricUdldPolicyEntry_Object = MibTableRow
cfprFabricUdldPolicyEntry = _CfprFabricUdldPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1)
)
cfprFabricUdldPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricUdldPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyEntry.setStatus("current")
_CfprFabricUdldPolicyInstanceId_Type = CfprManagedObjectId
_CfprFabricUdldPolicyInstanceId_Object = MibTableColumn
cfprFabricUdldPolicyInstanceId = _CfprFabricUdldPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 1),
    _CfprFabricUdldPolicyInstanceId_Type()
)
cfprFabricUdldPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyInstanceId.setStatus("current")
_CfprFabricUdldPolicyDn_Type = CfprManagedObjectDn
_CfprFabricUdldPolicyDn_Object = MibTableColumn
cfprFabricUdldPolicyDn = _CfprFabricUdldPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 2),
    _CfprFabricUdldPolicyDn_Type()
)
cfprFabricUdldPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyDn.setStatus("current")
_CfprFabricUdldPolicyRn_Type = SnmpAdminString
_CfprFabricUdldPolicyRn_Object = MibTableColumn
cfprFabricUdldPolicyRn = _CfprFabricUdldPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 3),
    _CfprFabricUdldPolicyRn_Type()
)
cfprFabricUdldPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyRn.setStatus("current")
_CfprFabricUdldPolicyDescr_Type = SnmpAdminString
_CfprFabricUdldPolicyDescr_Object = MibTableColumn
cfprFabricUdldPolicyDescr = _CfprFabricUdldPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 4),
    _CfprFabricUdldPolicyDescr_Type()
)
cfprFabricUdldPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyDescr.setStatus("current")
_CfprFabricUdldPolicyIntId_Type = SnmpAdminString
_CfprFabricUdldPolicyIntId_Object = MibTableColumn
cfprFabricUdldPolicyIntId = _CfprFabricUdldPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 5),
    _CfprFabricUdldPolicyIntId_Type()
)
cfprFabricUdldPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyIntId.setStatus("current")
_CfprFabricUdldPolicyMsgInterval_Type = Gauge32
_CfprFabricUdldPolicyMsgInterval_Object = MibTableColumn
cfprFabricUdldPolicyMsgInterval = _CfprFabricUdldPolicyMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 6),
    _CfprFabricUdldPolicyMsgInterval_Type()
)
cfprFabricUdldPolicyMsgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyMsgInterval.setStatus("current")
_CfprFabricUdldPolicyName_Type = SnmpAdminString
_CfprFabricUdldPolicyName_Object = MibTableColumn
cfprFabricUdldPolicyName = _CfprFabricUdldPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 7),
    _CfprFabricUdldPolicyName_Type()
)
cfprFabricUdldPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyName.setStatus("current")
_CfprFabricUdldPolicyPolicyLevel_Type = Gauge32
_CfprFabricUdldPolicyPolicyLevel_Object = MibTableColumn
cfprFabricUdldPolicyPolicyLevel = _CfprFabricUdldPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 8),
    _CfprFabricUdldPolicyPolicyLevel_Type()
)
cfprFabricUdldPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyPolicyLevel.setStatus("current")
_CfprFabricUdldPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricUdldPolicyPolicyOwner_Object = MibTableColumn
cfprFabricUdldPolicyPolicyOwner = _CfprFabricUdldPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 9),
    _CfprFabricUdldPolicyPolicyOwner_Type()
)
cfprFabricUdldPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyPolicyOwner.setStatus("current")
_CfprFabricUdldPolicyRecoveryAction_Type = CfprFabricRecoveryAction
_CfprFabricUdldPolicyRecoveryAction_Object = MibTableColumn
cfprFabricUdldPolicyRecoveryAction = _CfprFabricUdldPolicyRecoveryAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 110, 1, 10),
    _CfprFabricUdldPolicyRecoveryAction_Type()
)
cfprFabricUdldPolicyRecoveryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricUdldPolicyRecoveryAction.setStatus("current")
_CfprFabricVConTable_Object = MibTable
cfprFabricVConTable = _CfprFabricVConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111)
)
if mibBuilder.loadTexts:
    cfprFabricVConTable.setStatus("current")
_CfprFabricVConEntry_Object = MibTableRow
cfprFabricVConEntry = _CfprFabricVConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1)
)
cfprFabricVConEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVConInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVConEntry.setStatus("current")
_CfprFabricVConInstanceId_Type = CfprManagedObjectId
_CfprFabricVConInstanceId_Object = MibTableColumn
cfprFabricVConInstanceId = _CfprFabricVConInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 1),
    _CfprFabricVConInstanceId_Type()
)
cfprFabricVConInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVConInstanceId.setStatus("current")
_CfprFabricVConDn_Type = CfprManagedObjectDn
_CfprFabricVConDn_Object = MibTableColumn
cfprFabricVConDn = _CfprFabricVConDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 2),
    _CfprFabricVConDn_Type()
)
cfprFabricVConDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConDn.setStatus("current")
_CfprFabricVConRn_Type = SnmpAdminString
_CfprFabricVConRn_Object = MibTableColumn
cfprFabricVConRn = _CfprFabricVConRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 3),
    _CfprFabricVConRn_Type()
)
cfprFabricVConRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConRn.setStatus("current")
_CfprFabricVConEquipmentDn_Type = SnmpAdminString
_CfprFabricVConEquipmentDn_Object = MibTableColumn
cfprFabricVConEquipmentDn = _CfprFabricVConEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 4),
    _CfprFabricVConEquipmentDn_Type()
)
cfprFabricVConEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConEquipmentDn.setStatus("current")
_CfprFabricVConFabric_Type = SnmpAdminString
_CfprFabricVConFabric_Object = MibTableColumn
cfprFabricVConFabric = _CfprFabricVConFabric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 5),
    _CfprFabricVConFabric_Type()
)
cfprFabricVConFabric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConFabric.setStatus("current")
_CfprFabricVConId_Type = SnmpAdminString
_CfprFabricVConId_Object = MibTableColumn
cfprFabricVConId = _CfprFabricVConId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 6),
    _CfprFabricVConId_Type()
)
cfprFabricVConId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConId.setStatus("current")
_CfprFabricVConInstType_Type = CfprFabricVConInstType
_CfprFabricVConInstType_Object = MibTableColumn
cfprFabricVConInstType = _CfprFabricVConInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 7),
    _CfprFabricVConInstType_Type()
)
cfprFabricVConInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConInstType.setStatus("current")
_CfprFabricVConPlacement_Type = CfprFabricVConPlacementPref
_CfprFabricVConPlacement_Object = MibTableColumn
cfprFabricVConPlacement = _CfprFabricVConPlacement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 8),
    _CfprFabricVConPlacement_Type()
)
cfprFabricVConPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConPlacement.setStatus("current")
_CfprFabricVConSelect_Type = CfprFabricVConSelectPref
_CfprFabricVConSelect_Object = MibTableColumn
cfprFabricVConSelect = _CfprFabricVConSelect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 9),
    _CfprFabricVConSelect_Type()
)
cfprFabricVConSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConSelect.setStatus("current")
_CfprFabricVConShare_Type = CfprFabricVConSharePref
_CfprFabricVConShare_Object = MibTableColumn
cfprFabricVConShare = _CfprFabricVConShare_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 10),
    _CfprFabricVConShare_Type()
)
cfprFabricVConShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConShare.setStatus("current")
_CfprFabricVConTransport_Type = CfprFabricVConTransportPref
_CfprFabricVConTransport_Object = MibTableColumn
cfprFabricVConTransport = _CfprFabricVConTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 111, 1, 11),
    _CfprFabricVConTransport_Type()
)
cfprFabricVConTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConTransport.setStatus("current")
_CfprFabricVConProfileTable_Object = MibTable
cfprFabricVConProfileTable = _CfprFabricVConProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112)
)
if mibBuilder.loadTexts:
    cfprFabricVConProfileTable.setStatus("current")
_CfprFabricVConProfileEntry_Object = MibTableRow
cfprFabricVConProfileEntry = _CfprFabricVConProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1)
)
cfprFabricVConProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVConProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVConProfileEntry.setStatus("current")
_CfprFabricVConProfileInstanceId_Type = CfprManagedObjectId
_CfprFabricVConProfileInstanceId_Object = MibTableColumn
cfprFabricVConProfileInstanceId = _CfprFabricVConProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 1),
    _CfprFabricVConProfileInstanceId_Type()
)
cfprFabricVConProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVConProfileInstanceId.setStatus("current")
_CfprFabricVConProfileDn_Type = CfprManagedObjectDn
_CfprFabricVConProfileDn_Object = MibTableColumn
cfprFabricVConProfileDn = _CfprFabricVConProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 2),
    _CfprFabricVConProfileDn_Type()
)
cfprFabricVConProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConProfileDn.setStatus("current")
_CfprFabricVConProfileRn_Type = SnmpAdminString
_CfprFabricVConProfileRn_Object = MibTableColumn
cfprFabricVConProfileRn = _CfprFabricVConProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 3),
    _CfprFabricVConProfileRn_Type()
)
cfprFabricVConProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConProfileRn.setStatus("current")
_CfprFabricVConProfileDescr_Type = SnmpAdminString
_CfprFabricVConProfileDescr_Object = MibTableColumn
cfprFabricVConProfileDescr = _CfprFabricVConProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 4),
    _CfprFabricVConProfileDescr_Type()
)
cfprFabricVConProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConProfileDescr.setStatus("current")
_CfprFabricVConProfileIntId_Type = SnmpAdminString
_CfprFabricVConProfileIntId_Object = MibTableColumn
cfprFabricVConProfileIntId = _CfprFabricVConProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 5),
    _CfprFabricVConProfileIntId_Type()
)
cfprFabricVConProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConProfileIntId.setStatus("current")
_CfprFabricVConProfileMezzMapping_Type = CfprFabricVConMappingScheme
_CfprFabricVConProfileMezzMapping_Object = MibTableColumn
cfprFabricVConProfileMezzMapping = _CfprFabricVConProfileMezzMapping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 6),
    _CfprFabricVConProfileMezzMapping_Type()
)
cfprFabricVConProfileMezzMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConProfileMezzMapping.setStatus("current")
_CfprFabricVConProfileName_Type = SnmpAdminString
_CfprFabricVConProfileName_Object = MibTableColumn
cfprFabricVConProfileName = _CfprFabricVConProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 7),
    _CfprFabricVConProfileName_Type()
)
cfprFabricVConProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConProfileName.setStatus("current")
_CfprFabricVConProfilePolicyLevel_Type = Gauge32
_CfprFabricVConProfilePolicyLevel_Object = MibTableColumn
cfprFabricVConProfilePolicyLevel = _CfprFabricVConProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 8),
    _CfprFabricVConProfilePolicyLevel_Type()
)
cfprFabricVConProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConProfilePolicyLevel.setStatus("current")
_CfprFabricVConProfilePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprFabricVConProfilePolicyOwner_Object = MibTableColumn
cfprFabricVConProfilePolicyOwner = _CfprFabricVConProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 112, 1, 9),
    _CfprFabricVConProfilePolicyOwner_Type()
)
cfprFabricVConProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVConProfilePolicyOwner.setStatus("current")
_CfprFabricVlanTable_Object = MibTable
cfprFabricVlanTable = _CfprFabricVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113)
)
if mibBuilder.loadTexts:
    cfprFabricVlanTable.setStatus("current")
_CfprFabricVlanEntry_Object = MibTableRow
cfprFabricVlanEntry = _CfprFabricVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1)
)
cfprFabricVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVlanEntry.setStatus("current")
_CfprFabricVlanInstanceId_Type = CfprManagedObjectId
_CfprFabricVlanInstanceId_Object = MibTableColumn
cfprFabricVlanInstanceId = _CfprFabricVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 1),
    _CfprFabricVlanInstanceId_Type()
)
cfprFabricVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVlanInstanceId.setStatus("current")
_CfprFabricVlanDn_Type = CfprManagedObjectDn
_CfprFabricVlanDn_Object = MibTableColumn
cfprFabricVlanDn = _CfprFabricVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 2),
    _CfprFabricVlanDn_Type()
)
cfprFabricVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanDn.setStatus("current")
_CfprFabricVlanRn_Type = SnmpAdminString
_CfprFabricVlanRn_Object = MibTableColumn
cfprFabricVlanRn = _CfprFabricVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 3),
    _CfprFabricVlanRn_Type()
)
cfprFabricVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanRn.setStatus("current")
_CfprFabricVlanAssocPrimaryVlanState_Type = CfprFabricVlanAssocPrimaryVlanState
_CfprFabricVlanAssocPrimaryVlanState_Object = MibTableColumn
cfprFabricVlanAssocPrimaryVlanState = _CfprFabricVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 4),
    _CfprFabricVlanAssocPrimaryVlanState_Type()
)
cfprFabricVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanAssocPrimaryVlanState.setStatus("current")
_CfprFabricVlanAssocPrimaryVlanSwitchId_Type = CfprFabricAVlanAssocPrimaryVlanSwitchId
_CfprFabricVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprFabricVlanAssocPrimaryVlanSwitchId = _CfprFabricVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 5),
    _CfprFabricVlanAssocPrimaryVlanSwitchId_Type()
)
cfprFabricVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprFabricVlanCloud_Type = CfprFabricCloudType
_CfprFabricVlanCloud_Object = MibTableColumn
cfprFabricVlanCloud = _CfprFabricVlanCloud_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 6),
    _CfprFabricVlanCloud_Type()
)
cfprFabricVlanCloud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanCloud.setStatus("current")
_CfprFabricVlanCompressionType_Type = CfprFabricVlanCompType
_CfprFabricVlanCompressionType_Object = MibTableColumn
cfprFabricVlanCompressionType = _CfprFabricVlanCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 7),
    _CfprFabricVlanCompressionType_Type()
)
cfprFabricVlanCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanCompressionType.setStatus("current")
_CfprFabricVlanConfigIssues_Type = CfprFabricVlanConfigIssues
_CfprFabricVlanConfigIssues_Object = MibTableColumn
cfprFabricVlanConfigIssues = _CfprFabricVlanConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 8),
    _CfprFabricVlanConfigIssues_Type()
)
cfprFabricVlanConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanConfigIssues.setStatus("current")
_CfprFabricVlanDefaultNet_Type = TruthValue
_CfprFabricVlanDefaultNet_Object = MibTableColumn
cfprFabricVlanDefaultNet = _CfprFabricVlanDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 9),
    _CfprFabricVlanDefaultNet_Type()
)
cfprFabricVlanDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanDefaultNet.setStatus("current")
_CfprFabricVlanEpDn_Type = SnmpAdminString
_CfprFabricVlanEpDn_Object = MibTableColumn
cfprFabricVlanEpDn = _CfprFabricVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 10),
    _CfprFabricVlanEpDn_Type()
)
cfprFabricVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpDn.setStatus("current")
_CfprFabricVlanFltAggr_Type = Unsigned64
_CfprFabricVlanFltAggr_Object = MibTableColumn
cfprFabricVlanFltAggr = _CfprFabricVlanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 11),
    _CfprFabricVlanFltAggr_Type()
)
cfprFabricVlanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanFltAggr.setStatus("current")
_CfprFabricVlanGlobal_Type = Unsigned64
_CfprFabricVlanGlobal_Object = MibTableColumn
cfprFabricVlanGlobal = _CfprFabricVlanGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 12),
    _CfprFabricVlanGlobal_Type()
)
cfprFabricVlanGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanGlobal.setStatus("current")
_CfprFabricVlanId_Type = Gauge32
_CfprFabricVlanId_Object = MibTableColumn
cfprFabricVlanId = _CfprFabricVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 13),
    _CfprFabricVlanId_Type()
)
cfprFabricVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanId.setStatus("current")
_CfprFabricVlanIfRole_Type = CfprFabricVnetEpIfRole
_CfprFabricVlanIfRole_Object = MibTableColumn
cfprFabricVlanIfRole = _CfprFabricVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 14),
    _CfprFabricVlanIfRole_Type()
)
cfprFabricVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanIfRole.setStatus("current")
_CfprFabricVlanIfType_Type = CfprNetworkVnetEpIfType
_CfprFabricVlanIfType_Object = MibTableColumn
cfprFabricVlanIfType = _CfprFabricVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 15),
    _CfprFabricVlanIfType_Type()
)
cfprFabricVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanIfType.setStatus("current")
_CfprFabricVlanLocal_Type = Unsigned64
_CfprFabricVlanLocal_Object = MibTableColumn
cfprFabricVlanLocal = _CfprFabricVlanLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 16),
    _CfprFabricVlanLocal_Type()
)
cfprFabricVlanLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanLocal.setStatus("current")
_CfprFabricVlanLocale_Type = CfprFabricVnetEpLocale
_CfprFabricVlanLocale_Object = MibTableColumn
cfprFabricVlanLocale = _CfprFabricVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 17),
    _CfprFabricVlanLocale_Type()
)
cfprFabricVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanLocale.setStatus("current")
_CfprFabricVlanMcastPolicyName_Type = SnmpAdminString
_CfprFabricVlanMcastPolicyName_Object = MibTableColumn
cfprFabricVlanMcastPolicyName = _CfprFabricVlanMcastPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 18),
    _CfprFabricVlanMcastPolicyName_Type()
)
cfprFabricVlanMcastPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanMcastPolicyName.setStatus("current")
_CfprFabricVlanName_Type = SnmpAdminString
_CfprFabricVlanName_Object = MibTableColumn
cfprFabricVlanName = _CfprFabricVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 19),
    _CfprFabricVlanName_Type()
)
cfprFabricVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanName.setStatus("current")
_CfprFabricVlanOperMcastPolicyName_Type = SnmpAdminString
_CfprFabricVlanOperMcastPolicyName_Object = MibTableColumn
cfprFabricVlanOperMcastPolicyName = _CfprFabricVlanOperMcastPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 20),
    _CfprFabricVlanOperMcastPolicyName_Type()
)
cfprFabricVlanOperMcastPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanOperMcastPolicyName.setStatus("current")
_CfprFabricVlanOperState_Type = CfprFabricVlanOperState
_CfprFabricVlanOperState_Object = MibTableColumn
cfprFabricVlanOperState = _CfprFabricVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 21),
    _CfprFabricVlanOperState_Type()
)
cfprFabricVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanOperState.setStatus("current")
_CfprFabricVlanOverlapStateForA_Type = CfprFabricVlanOverlapState
_CfprFabricVlanOverlapStateForA_Object = MibTableColumn
cfprFabricVlanOverlapStateForA = _CfprFabricVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 22),
    _CfprFabricVlanOverlapStateForA_Type()
)
cfprFabricVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanOverlapStateForA.setStatus("current")
_CfprFabricVlanOverlapStateForB_Type = CfprFabricVlanOverlapState
_CfprFabricVlanOverlapStateForB_Object = MibTableColumn
cfprFabricVlanOverlapStateForB = _CfprFabricVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 23),
    _CfprFabricVlanOverlapStateForB_Type()
)
cfprFabricVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanOverlapStateForB.setStatus("current")
_CfprFabricVlanPeerDn_Type = SnmpAdminString
_CfprFabricVlanPeerDn_Object = MibTableColumn
cfprFabricVlanPeerDn = _CfprFabricVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 24),
    _CfprFabricVlanPeerDn_Type()
)
cfprFabricVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPeerDn.setStatus("current")
_CfprFabricVlanPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprFabricVlanPolicyOwner_Object = MibTableColumn
cfprFabricVlanPolicyOwner = _CfprFabricVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 25),
    _CfprFabricVlanPolicyOwner_Type()
)
cfprFabricVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPolicyOwner.setStatus("current")
_CfprFabricVlanPubNwDn_Type = SnmpAdminString
_CfprFabricVlanPubNwDn_Object = MibTableColumn
cfprFabricVlanPubNwDn = _CfprFabricVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 26),
    _CfprFabricVlanPubNwDn_Type()
)
cfprFabricVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPubNwDn.setStatus("current")
_CfprFabricVlanPubNwId_Type = Gauge32
_CfprFabricVlanPubNwId_Object = MibTableColumn
cfprFabricVlanPubNwId = _CfprFabricVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 27),
    _CfprFabricVlanPubNwId_Type()
)
cfprFabricVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPubNwId.setStatus("current")
_CfprFabricVlanPubNwName_Type = SnmpAdminString
_CfprFabricVlanPubNwName_Object = MibTableColumn
cfprFabricVlanPubNwName = _CfprFabricVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 28),
    _CfprFabricVlanPubNwName_Type()
)
cfprFabricVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPubNwName.setStatus("current")
_CfprFabricVlanSharing_Type = CfprFabricAVlanSharing
_CfprFabricVlanSharing_Object = MibTableColumn
cfprFabricVlanSharing = _CfprFabricVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 29),
    _CfprFabricVlanSharing_Type()
)
cfprFabricVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanSharing.setStatus("current")
_CfprFabricVlanSwitchId_Type = CfprFabricVlanSwitchId
_CfprFabricVlanSwitchId_Object = MibTableColumn
cfprFabricVlanSwitchId = _CfprFabricVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 30),
    _CfprFabricVlanSwitchId_Type()
)
cfprFabricVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanSwitchId.setStatus("current")
_CfprFabricVlanTransport_Type = CfprFabricAVlanTransport
_CfprFabricVlanTransport_Object = MibTableColumn
cfprFabricVlanTransport = _CfprFabricVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 31),
    _CfprFabricVlanTransport_Type()
)
cfprFabricVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanTransport.setStatus("current")
_CfprFabricVlanType_Type = CfprFabricAVlanType
_CfprFabricVlanType_Object = MibTableColumn
cfprFabricVlanType = _CfprFabricVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 113, 1, 32),
    _CfprFabricVlanType_Type()
)
cfprFabricVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanType.setStatus("current")
_CfprFabricVlanEpTable_Object = MibTable
cfprFabricVlanEpTable = _CfprFabricVlanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114)
)
if mibBuilder.loadTexts:
    cfprFabricVlanEpTable.setStatus("current")
_CfprFabricVlanEpEntry_Object = MibTableRow
cfprFabricVlanEpEntry = _CfprFabricVlanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1)
)
cfprFabricVlanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVlanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVlanEpEntry.setStatus("current")
_CfprFabricVlanEpInstanceId_Type = CfprManagedObjectId
_CfprFabricVlanEpInstanceId_Object = MibTableColumn
cfprFabricVlanEpInstanceId = _CfprFabricVlanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 1),
    _CfprFabricVlanEpInstanceId_Type()
)
cfprFabricVlanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVlanEpInstanceId.setStatus("current")
_CfprFabricVlanEpDnData_Type = CfprManagedObjectDn
_CfprFabricVlanEpDnData_Object = MibTableColumn
cfprFabricVlanEpDnData = _CfprFabricVlanEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 2),
    _CfprFabricVlanEpDnData_Type()
)
cfprFabricVlanEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpDnData.setStatus("current")
_CfprFabricVlanEpRn_Type = SnmpAdminString
_CfprFabricVlanEpRn_Object = MibTableColumn
cfprFabricVlanEpRn = _CfprFabricVlanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 3),
    _CfprFabricVlanEpRn_Type()
)
cfprFabricVlanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpRn.setStatus("current")
_CfprFabricVlanEpAssocPrimaryVlanState_Type = CfprFabricVlanAssocPrimaryVlanState
_CfprFabricVlanEpAssocPrimaryVlanState_Object = MibTableColumn
cfprFabricVlanEpAssocPrimaryVlanState = _CfprFabricVlanEpAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 4),
    _CfprFabricVlanEpAssocPrimaryVlanState_Type()
)
cfprFabricVlanEpAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpAssocPrimaryVlanState.setStatus("current")
_CfprFabricVlanEpAssocPrimaryVlanSwitchId_Type = CfprFabricAVlanAssocPrimaryVlanSwitchId
_CfprFabricVlanEpAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprFabricVlanEpAssocPrimaryVlanSwitchId = _CfprFabricVlanEpAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 5),
    _CfprFabricVlanEpAssocPrimaryVlanSwitchId_Type()
)
cfprFabricVlanEpAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpAssocPrimaryVlanSwitchId.setStatus("current")
_CfprFabricVlanEpEpDn_Type = SnmpAdminString
_CfprFabricVlanEpEpDn_Object = MibTableColumn
cfprFabricVlanEpEpDn = _CfprFabricVlanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 6),
    _CfprFabricVlanEpEpDn_Type()
)
cfprFabricVlanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpEpDn.setStatus("current")
_CfprFabricVlanEpId_Type = Gauge32
_CfprFabricVlanEpId_Object = MibTableColumn
cfprFabricVlanEpId = _CfprFabricVlanEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 7),
    _CfprFabricVlanEpId_Type()
)
cfprFabricVlanEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpId.setStatus("current")
_CfprFabricVlanEpIfRole_Type = CfprFabricVnetEpIfRole
_CfprFabricVlanEpIfRole_Object = MibTableColumn
cfprFabricVlanEpIfRole = _CfprFabricVlanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 8),
    _CfprFabricVlanEpIfRole_Type()
)
cfprFabricVlanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpIfRole.setStatus("current")
_CfprFabricVlanEpIfType_Type = CfprNetworkVnetEpIfType
_CfprFabricVlanEpIfType_Object = MibTableColumn
cfprFabricVlanEpIfType = _CfprFabricVlanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 9),
    _CfprFabricVlanEpIfType_Type()
)
cfprFabricVlanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpIfType.setStatus("current")
_CfprFabricVlanEpIsNative_Type = TruthValue
_CfprFabricVlanEpIsNative_Object = MibTableColumn
cfprFabricVlanEpIsNative = _CfprFabricVlanEpIsNative_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 10),
    _CfprFabricVlanEpIsNative_Type()
)
cfprFabricVlanEpIsNative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpIsNative.setStatus("current")
_CfprFabricVlanEpLocale_Type = CfprFabricVnetEpLocale
_CfprFabricVlanEpLocale_Object = MibTableColumn
cfprFabricVlanEpLocale = _CfprFabricVlanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 11),
    _CfprFabricVlanEpLocale_Type()
)
cfprFabricVlanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpLocale.setStatus("current")
_CfprFabricVlanEpName_Type = SnmpAdminString
_CfprFabricVlanEpName_Object = MibTableColumn
cfprFabricVlanEpName = _CfprFabricVlanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 12),
    _CfprFabricVlanEpName_Type()
)
cfprFabricVlanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpName.setStatus("current")
_CfprFabricVlanEpOperState_Type = CfprFabricVlanOperState
_CfprFabricVlanEpOperState_Object = MibTableColumn
cfprFabricVlanEpOperState = _CfprFabricVlanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 13),
    _CfprFabricVlanEpOperState_Type()
)
cfprFabricVlanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpOperState.setStatus("current")
_CfprFabricVlanEpOverlapStateForA_Type = CfprFabricVlanOverlapState
_CfprFabricVlanEpOverlapStateForA_Object = MibTableColumn
cfprFabricVlanEpOverlapStateForA = _CfprFabricVlanEpOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 14),
    _CfprFabricVlanEpOverlapStateForA_Type()
)
cfprFabricVlanEpOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpOverlapStateForA.setStatus("current")
_CfprFabricVlanEpOverlapStateForB_Type = CfprFabricVlanOverlapState
_CfprFabricVlanEpOverlapStateForB_Object = MibTableColumn
cfprFabricVlanEpOverlapStateForB = _CfprFabricVlanEpOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 15),
    _CfprFabricVlanEpOverlapStateForB_Type()
)
cfprFabricVlanEpOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpOverlapStateForB.setStatus("current")
_CfprFabricVlanEpPeerDn_Type = SnmpAdminString
_CfprFabricVlanEpPeerDn_Object = MibTableColumn
cfprFabricVlanEpPeerDn = _CfprFabricVlanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 16),
    _CfprFabricVlanEpPeerDn_Type()
)
cfprFabricVlanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpPeerDn.setStatus("current")
_CfprFabricVlanEpPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprFabricVlanEpPolicyOwner_Object = MibTableColumn
cfprFabricVlanEpPolicyOwner = _CfprFabricVlanEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 17),
    _CfprFabricVlanEpPolicyOwner_Type()
)
cfprFabricVlanEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpPolicyOwner.setStatus("current")
_CfprFabricVlanEpPubNwDn_Type = SnmpAdminString
_CfprFabricVlanEpPubNwDn_Object = MibTableColumn
cfprFabricVlanEpPubNwDn = _CfprFabricVlanEpPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 18),
    _CfprFabricVlanEpPubNwDn_Type()
)
cfprFabricVlanEpPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpPubNwDn.setStatus("current")
_CfprFabricVlanEpPubNwId_Type = Gauge32
_CfprFabricVlanEpPubNwId_Object = MibTableColumn
cfprFabricVlanEpPubNwId = _CfprFabricVlanEpPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 19),
    _CfprFabricVlanEpPubNwId_Type()
)
cfprFabricVlanEpPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpPubNwId.setStatus("current")
_CfprFabricVlanEpPubNwName_Type = SnmpAdminString
_CfprFabricVlanEpPubNwName_Object = MibTableColumn
cfprFabricVlanEpPubNwName = _CfprFabricVlanEpPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 20),
    _CfprFabricVlanEpPubNwName_Type()
)
cfprFabricVlanEpPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpPubNwName.setStatus("current")
_CfprFabricVlanEpSharing_Type = CfprFabricAVlanSharing
_CfprFabricVlanEpSharing_Object = MibTableColumn
cfprFabricVlanEpSharing = _CfprFabricVlanEpSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 21),
    _CfprFabricVlanEpSharing_Type()
)
cfprFabricVlanEpSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpSharing.setStatus("current")
_CfprFabricVlanEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricVlanEpSwitchId_Object = MibTableColumn
cfprFabricVlanEpSwitchId = _CfprFabricVlanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 22),
    _CfprFabricVlanEpSwitchId_Type()
)
cfprFabricVlanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpSwitchId.setStatus("current")
_CfprFabricVlanEpTransport_Type = CfprFabricAVlanTransport
_CfprFabricVlanEpTransport_Object = MibTableColumn
cfprFabricVlanEpTransport = _CfprFabricVlanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 23),
    _CfprFabricVlanEpTransport_Type()
)
cfprFabricVlanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpTransport.setStatus("current")
_CfprFabricVlanEpType_Type = CfprFabricAVlanType
_CfprFabricVlanEpType_Object = MibTableColumn
cfprFabricVlanEpType = _CfprFabricVlanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 114, 1, 24),
    _CfprFabricVlanEpType_Type()
)
cfprFabricVlanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanEpType.setStatus("current")
_CfprFabricVlanGroupReqTable_Object = MibTable
cfprFabricVlanGroupReqTable = _CfprFabricVlanGroupReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 115)
)
if mibBuilder.loadTexts:
    cfprFabricVlanGroupReqTable.setStatus("current")
_CfprFabricVlanGroupReqEntry_Object = MibTableRow
cfprFabricVlanGroupReqEntry = _CfprFabricVlanGroupReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 115, 1)
)
cfprFabricVlanGroupReqEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVlanGroupReqInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVlanGroupReqEntry.setStatus("current")
_CfprFabricVlanGroupReqInstanceId_Type = CfprManagedObjectId
_CfprFabricVlanGroupReqInstanceId_Object = MibTableColumn
cfprFabricVlanGroupReqInstanceId = _CfprFabricVlanGroupReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 115, 1, 1),
    _CfprFabricVlanGroupReqInstanceId_Type()
)
cfprFabricVlanGroupReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVlanGroupReqInstanceId.setStatus("current")
_CfprFabricVlanGroupReqDn_Type = CfprManagedObjectDn
_CfprFabricVlanGroupReqDn_Object = MibTableColumn
cfprFabricVlanGroupReqDn = _CfprFabricVlanGroupReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 115, 1, 2),
    _CfprFabricVlanGroupReqDn_Type()
)
cfprFabricVlanGroupReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanGroupReqDn.setStatus("current")
_CfprFabricVlanGroupReqRn_Type = SnmpAdminString
_CfprFabricVlanGroupReqRn_Object = MibTableColumn
cfprFabricVlanGroupReqRn = _CfprFabricVlanGroupReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 115, 1, 3),
    _CfprFabricVlanGroupReqRn_Type()
)
cfprFabricVlanGroupReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanGroupReqRn.setStatus("current")
_CfprFabricVlanGroupReqConfigIssues_Type = CfprFabricReqIssues
_CfprFabricVlanGroupReqConfigIssues_Object = MibTableColumn
cfprFabricVlanGroupReqConfigIssues = _CfprFabricVlanGroupReqConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 115, 1, 4),
    _CfprFabricVlanGroupReqConfigIssues_Type()
)
cfprFabricVlanGroupReqConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanGroupReqConfigIssues.setStatus("current")
_CfprFabricVlanGroupReqName_Type = SnmpAdminString
_CfprFabricVlanGroupReqName_Object = MibTableColumn
cfprFabricVlanGroupReqName = _CfprFabricVlanGroupReqName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 115, 1, 5),
    _CfprFabricVlanGroupReqName_Type()
)
cfprFabricVlanGroupReqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanGroupReqName.setStatus("current")
_CfprFabricVlanGroupReqType_Type = CfprFabricAccessType
_CfprFabricVlanGroupReqType_Object = MibTableColumn
cfprFabricVlanGroupReqType = _CfprFabricVlanGroupReqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 115, 1, 6),
    _CfprFabricVlanGroupReqType_Type()
)
cfprFabricVlanGroupReqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanGroupReqType.setStatus("current")
_CfprFabricVlanPermitTable_Object = MibTable
cfprFabricVlanPermitTable = _CfprFabricVlanPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 116)
)
if mibBuilder.loadTexts:
    cfprFabricVlanPermitTable.setStatus("current")
_CfprFabricVlanPermitEntry_Object = MibTableRow
cfprFabricVlanPermitEntry = _CfprFabricVlanPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 116, 1)
)
cfprFabricVlanPermitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVlanPermitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVlanPermitEntry.setStatus("current")
_CfprFabricVlanPermitInstanceId_Type = CfprManagedObjectId
_CfprFabricVlanPermitInstanceId_Object = MibTableColumn
cfprFabricVlanPermitInstanceId = _CfprFabricVlanPermitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 116, 1, 1),
    _CfprFabricVlanPermitInstanceId_Type()
)
cfprFabricVlanPermitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVlanPermitInstanceId.setStatus("current")
_CfprFabricVlanPermitDn_Type = CfprManagedObjectDn
_CfprFabricVlanPermitDn_Object = MibTableColumn
cfprFabricVlanPermitDn = _CfprFabricVlanPermitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 116, 1, 2),
    _CfprFabricVlanPermitDn_Type()
)
cfprFabricVlanPermitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPermitDn.setStatus("current")
_CfprFabricVlanPermitRn_Type = SnmpAdminString
_CfprFabricVlanPermitRn_Object = MibTableColumn
cfprFabricVlanPermitRn = _CfprFabricVlanPermitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 116, 1, 3),
    _CfprFabricVlanPermitRn_Type()
)
cfprFabricVlanPermitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPermitRn.setStatus("current")
_CfprFabricVlanPermitCloud_Type = CfprFabricCloudType
_CfprFabricVlanPermitCloud_Object = MibTableColumn
cfprFabricVlanPermitCloud = _CfprFabricVlanPermitCloud_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 116, 1, 4),
    _CfprFabricVlanPermitCloud_Type()
)
cfprFabricVlanPermitCloud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPermitCloud.setStatus("current")
_CfprFabricVlanPermitName_Type = SnmpAdminString
_CfprFabricVlanPermitName_Object = MibTableColumn
cfprFabricVlanPermitName = _CfprFabricVlanPermitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 116, 1, 5),
    _CfprFabricVlanPermitName_Type()
)
cfprFabricVlanPermitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPermitName.setStatus("current")
_CfprFabricVlanPermitSwitchId_Type = SnmpAdminString
_CfprFabricVlanPermitSwitchId_Object = MibTableColumn
cfprFabricVlanPermitSwitchId = _CfprFabricVlanPermitSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 116, 1, 6),
    _CfprFabricVlanPermitSwitchId_Type()
)
cfprFabricVlanPermitSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanPermitSwitchId.setStatus("current")
_CfprFabricVlanReqTable_Object = MibTable
cfprFabricVlanReqTable = _CfprFabricVlanReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 117)
)
if mibBuilder.loadTexts:
    cfprFabricVlanReqTable.setStatus("current")
_CfprFabricVlanReqEntry_Object = MibTableRow
cfprFabricVlanReqEntry = _CfprFabricVlanReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 117, 1)
)
cfprFabricVlanReqEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVlanReqInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVlanReqEntry.setStatus("current")
_CfprFabricVlanReqInstanceId_Type = CfprManagedObjectId
_CfprFabricVlanReqInstanceId_Object = MibTableColumn
cfprFabricVlanReqInstanceId = _CfprFabricVlanReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 117, 1, 1),
    _CfprFabricVlanReqInstanceId_Type()
)
cfprFabricVlanReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVlanReqInstanceId.setStatus("current")
_CfprFabricVlanReqDn_Type = CfprManagedObjectDn
_CfprFabricVlanReqDn_Object = MibTableColumn
cfprFabricVlanReqDn = _CfprFabricVlanReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 117, 1, 2),
    _CfprFabricVlanReqDn_Type()
)
cfprFabricVlanReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanReqDn.setStatus("current")
_CfprFabricVlanReqRn_Type = SnmpAdminString
_CfprFabricVlanReqRn_Object = MibTableColumn
cfprFabricVlanReqRn = _CfprFabricVlanReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 117, 1, 3),
    _CfprFabricVlanReqRn_Type()
)
cfprFabricVlanReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanReqRn.setStatus("current")
_CfprFabricVlanReqConfigIssues_Type = CfprFabricReqIssues
_CfprFabricVlanReqConfigIssues_Object = MibTableColumn
cfprFabricVlanReqConfigIssues = _CfprFabricVlanReqConfigIssues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 117, 1, 4),
    _CfprFabricVlanReqConfigIssues_Type()
)
cfprFabricVlanReqConfigIssues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanReqConfigIssues.setStatus("current")
_CfprFabricVlanReqName_Type = SnmpAdminString
_CfprFabricVlanReqName_Object = MibTableColumn
cfprFabricVlanReqName = _CfprFabricVlanReqName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 117, 1, 5),
    _CfprFabricVlanReqName_Type()
)
cfprFabricVlanReqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanReqName.setStatus("current")
_CfprFabricVlanReqType_Type = CfprFabricAccessType
_CfprFabricVlanReqType_Object = MibTableColumn
cfprFabricVlanReqType = _CfprFabricVlanReqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 117, 1, 6),
    _CfprFabricVlanReqType_Type()
)
cfprFabricVlanReqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVlanReqType.setStatus("current")
_CfprFabricVnetEpSyncEpTable_Object = MibTable
cfprFabricVnetEpSyncEpTable = _CfprFabricVnetEpSyncEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118)
)
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpTable.setStatus("current")
_CfprFabricVnetEpSyncEpEntry_Object = MibTableRow
cfprFabricVnetEpSyncEpEntry = _CfprFabricVnetEpSyncEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1)
)
cfprFabricVnetEpSyncEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVnetEpSyncEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpEntry.setStatus("current")
_CfprFabricVnetEpSyncEpInstanceId_Type = CfprManagedObjectId
_CfprFabricVnetEpSyncEpInstanceId_Object = MibTableColumn
cfprFabricVnetEpSyncEpInstanceId = _CfprFabricVnetEpSyncEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 1),
    _CfprFabricVnetEpSyncEpInstanceId_Type()
)
cfprFabricVnetEpSyncEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpInstanceId.setStatus("current")
_CfprFabricVnetEpSyncEpDn_Type = CfprManagedObjectDn
_CfprFabricVnetEpSyncEpDn_Object = MibTableColumn
cfprFabricVnetEpSyncEpDn = _CfprFabricVnetEpSyncEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 2),
    _CfprFabricVnetEpSyncEpDn_Type()
)
cfprFabricVnetEpSyncEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpDn.setStatus("current")
_CfprFabricVnetEpSyncEpRn_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpRn_Object = MibTableColumn
cfprFabricVnetEpSyncEpRn = _CfprFabricVnetEpSyncEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 3),
    _CfprFabricVnetEpSyncEpRn_Type()
)
cfprFabricVnetEpSyncEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpRn.setStatus("current")
_CfprFabricVnetEpSyncEpFsmDescr_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmDescr_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmDescr = _CfprFabricVnetEpSyncEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 4),
    _CfprFabricVnetEpSyncEpFsmDescr_Type()
)
cfprFabricVnetEpSyncEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmDescr.setStatus("current")
_CfprFabricVnetEpSyncEpFsmPrev_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmPrev_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmPrev = _CfprFabricVnetEpSyncEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 5),
    _CfprFabricVnetEpSyncEpFsmPrev_Type()
)
cfprFabricVnetEpSyncEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmPrev.setStatus("current")
_CfprFabricVnetEpSyncEpFsmProgr_Type = Gauge32
_CfprFabricVnetEpSyncEpFsmProgr_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmProgr = _CfprFabricVnetEpSyncEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 6),
    _CfprFabricVnetEpSyncEpFsmProgr_Type()
)
cfprFabricVnetEpSyncEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmProgr.setStatus("current")
_CfprFabricVnetEpSyncEpFsmRmtInvErrCode_Type = Gauge32
_CfprFabricVnetEpSyncEpFsmRmtInvErrCode_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmRmtInvErrCode = _CfprFabricVnetEpSyncEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 7),
    _CfprFabricVnetEpSyncEpFsmRmtInvErrCode_Type()
)
cfprFabricVnetEpSyncEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmRmtInvErrCode.setStatus("current")
_CfprFabricVnetEpSyncEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmRmtInvErrDescr = _CfprFabricVnetEpSyncEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 8),
    _CfprFabricVnetEpSyncEpFsmRmtInvErrDescr_Type()
)
cfprFabricVnetEpSyncEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmRmtInvErrDescr.setStatus("current")
_CfprFabricVnetEpSyncEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricVnetEpSyncEpFsmRmtInvRslt_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmRmtInvRslt = _CfprFabricVnetEpSyncEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 9),
    _CfprFabricVnetEpSyncEpFsmRmtInvRslt_Type()
)
cfprFabricVnetEpSyncEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmRmtInvRslt.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageDescr_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmStageDescr_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageDescr = _CfprFabricVnetEpSyncEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 10),
    _CfprFabricVnetEpSyncEpFsmStageDescr_Type()
)
cfprFabricVnetEpSyncEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageDescr.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStamp_Type = DateAndTime
_CfprFabricVnetEpSyncEpFsmStamp_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStamp = _CfprFabricVnetEpSyncEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 11),
    _CfprFabricVnetEpSyncEpFsmStamp_Type()
)
cfprFabricVnetEpSyncEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStamp.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStatus_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmStatus_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStatus = _CfprFabricVnetEpSyncEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 12),
    _CfprFabricVnetEpSyncEpFsmStatus_Type()
)
cfprFabricVnetEpSyncEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStatus.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTry_Type = Gauge32
_CfprFabricVnetEpSyncEpFsmTry_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmTry = _CfprFabricVnetEpSyncEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 13),
    _CfprFabricVnetEpSyncEpFsmTry_Type()
)
cfprFabricVnetEpSyncEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTry.setStatus("current")
_CfprFabricVnetEpSyncEpGenNumSync_Type = Gauge32
_CfprFabricVnetEpSyncEpGenNumSync_Object = MibTableColumn
cfprFabricVnetEpSyncEpGenNumSync = _CfprFabricVnetEpSyncEpGenNumSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 14),
    _CfprFabricVnetEpSyncEpGenNumSync_Type()
)
cfprFabricVnetEpSyncEpGenNumSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpGenNumSync.setStatus("current")
_CfprFabricVnetEpSyncEpId_Type = Gauge32
_CfprFabricVnetEpSyncEpId_Object = MibTableColumn
cfprFabricVnetEpSyncEpId = _CfprFabricVnetEpSyncEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 15),
    _CfprFabricVnetEpSyncEpId_Type()
)
cfprFabricVnetEpSyncEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpId.setStatus("current")
_CfprFabricVnetEpSyncEpIsChangedObjectUpdate_Type = TruthValue
_CfprFabricVnetEpSyncEpIsChangedObjectUpdate_Object = MibTableColumn
cfprFabricVnetEpSyncEpIsChangedObjectUpdate = _CfprFabricVnetEpSyncEpIsChangedObjectUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 118, 1, 16),
    _CfprFabricVnetEpSyncEpIsChangedObjectUpdate_Type()
)
cfprFabricVnetEpSyncEpIsChangedObjectUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpIsChangedObjectUpdate.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTable_Object = MibTable
cfprFabricVnetEpSyncEpFsmTable = _CfprFabricVnetEpSyncEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119)
)
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTable.setStatus("current")
_CfprFabricVnetEpSyncEpFsmEntry_Object = MibTableRow
cfprFabricVnetEpSyncEpFsmEntry = _CfprFabricVnetEpSyncEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1)
)
cfprFabricVnetEpSyncEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVnetEpSyncEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmEntry.setStatus("current")
_CfprFabricVnetEpSyncEpFsmInstanceId_Type = CfprManagedObjectId
_CfprFabricVnetEpSyncEpFsmInstanceId_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmInstanceId = _CfprFabricVnetEpSyncEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 1),
    _CfprFabricVnetEpSyncEpFsmInstanceId_Type()
)
cfprFabricVnetEpSyncEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmInstanceId.setStatus("current")
_CfprFabricVnetEpSyncEpFsmDn_Type = CfprManagedObjectDn
_CfprFabricVnetEpSyncEpFsmDn_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmDn = _CfprFabricVnetEpSyncEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 2),
    _CfprFabricVnetEpSyncEpFsmDn_Type()
)
cfprFabricVnetEpSyncEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmDn.setStatus("current")
_CfprFabricVnetEpSyncEpFsmRn_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmRn_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmRn = _CfprFabricVnetEpSyncEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 3),
    _CfprFabricVnetEpSyncEpFsmRn_Type()
)
cfprFabricVnetEpSyncEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmRn.setStatus("current")
_CfprFabricVnetEpSyncEpFsmCompletionTime_Type = DateAndTime
_CfprFabricVnetEpSyncEpFsmCompletionTime_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmCompletionTime = _CfprFabricVnetEpSyncEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 4),
    _CfprFabricVnetEpSyncEpFsmCompletionTime_Type()
)
cfprFabricVnetEpSyncEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmCompletionTime.setStatus("current")
_CfprFabricVnetEpSyncEpFsmCurrentFsm_Type = CfprFabricVnetEpSyncEpFsmCurrentFsm
_CfprFabricVnetEpSyncEpFsmCurrentFsm_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmCurrentFsm = _CfprFabricVnetEpSyncEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 5),
    _CfprFabricVnetEpSyncEpFsmCurrentFsm_Type()
)
cfprFabricVnetEpSyncEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmCurrentFsm.setStatus("current")
_CfprFabricVnetEpSyncEpFsmDescrData_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmDescrData_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmDescrData = _CfprFabricVnetEpSyncEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 6),
    _CfprFabricVnetEpSyncEpFsmDescrData_Type()
)
cfprFabricVnetEpSyncEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmDescrData.setStatus("current")
_CfprFabricVnetEpSyncEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprFabricVnetEpSyncEpFsmFsmStatus_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmFsmStatus = _CfprFabricVnetEpSyncEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 7),
    _CfprFabricVnetEpSyncEpFsmFsmStatus_Type()
)
cfprFabricVnetEpSyncEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmFsmStatus.setStatus("current")
_CfprFabricVnetEpSyncEpFsmProgress_Type = Gauge32
_CfprFabricVnetEpSyncEpFsmProgress_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmProgress = _CfprFabricVnetEpSyncEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 8),
    _CfprFabricVnetEpSyncEpFsmProgress_Type()
)
cfprFabricVnetEpSyncEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmProgress.setStatus("current")
_CfprFabricVnetEpSyncEpFsmRmtErrCode_Type = Gauge32
_CfprFabricVnetEpSyncEpFsmRmtErrCode_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmRmtErrCode = _CfprFabricVnetEpSyncEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 9),
    _CfprFabricVnetEpSyncEpFsmRmtErrCode_Type()
)
cfprFabricVnetEpSyncEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmRmtErrCode.setStatus("current")
_CfprFabricVnetEpSyncEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmRmtErrDescr_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmRmtErrDescr = _CfprFabricVnetEpSyncEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 10),
    _CfprFabricVnetEpSyncEpFsmRmtErrDescr_Type()
)
cfprFabricVnetEpSyncEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmRmtErrDescr.setStatus("current")
_CfprFabricVnetEpSyncEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprFabricVnetEpSyncEpFsmRmtRslt_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmRmtRslt = _CfprFabricVnetEpSyncEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 119, 1, 11),
    _CfprFabricVnetEpSyncEpFsmRmtRslt_Type()
)
cfprFabricVnetEpSyncEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmRmtRslt.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageTable_Object = MibTable
cfprFabricVnetEpSyncEpFsmStageTable = _CfprFabricVnetEpSyncEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120)
)
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageTable.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageEntry_Object = MibTableRow
cfprFabricVnetEpSyncEpFsmStageEntry = _CfprFabricVnetEpSyncEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1)
)
cfprFabricVnetEpSyncEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVnetEpSyncEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageEntry.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprFabricVnetEpSyncEpFsmStageInstanceId_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageInstanceId = _CfprFabricVnetEpSyncEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 1),
    _CfprFabricVnetEpSyncEpFsmStageInstanceId_Type()
)
cfprFabricVnetEpSyncEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageInstanceId.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageDn_Type = CfprManagedObjectDn
_CfprFabricVnetEpSyncEpFsmStageDn_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageDn = _CfprFabricVnetEpSyncEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 2),
    _CfprFabricVnetEpSyncEpFsmStageDn_Type()
)
cfprFabricVnetEpSyncEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageDn.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageRn_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmStageRn_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageRn = _CfprFabricVnetEpSyncEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 3),
    _CfprFabricVnetEpSyncEpFsmStageRn_Type()
)
cfprFabricVnetEpSyncEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageRn.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageDescrData_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmStageDescrData_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageDescrData = _CfprFabricVnetEpSyncEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 4),
    _CfprFabricVnetEpSyncEpFsmStageDescrData_Type()
)
cfprFabricVnetEpSyncEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageDescrData.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprFabricVnetEpSyncEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageLastUpdateTime = _CfprFabricVnetEpSyncEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 5),
    _CfprFabricVnetEpSyncEpFsmStageLastUpdateTime_Type()
)
cfprFabricVnetEpSyncEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageLastUpdateTime.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageName_Type = CfprFabricVnetEpSyncEpFsmStageName
_CfprFabricVnetEpSyncEpFsmStageName_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageName = _CfprFabricVnetEpSyncEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 6),
    _CfprFabricVnetEpSyncEpFsmStageName_Type()
)
cfprFabricVnetEpSyncEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageName.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageOrder_Type = Gauge32
_CfprFabricVnetEpSyncEpFsmStageOrder_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageOrder = _CfprFabricVnetEpSyncEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 7),
    _CfprFabricVnetEpSyncEpFsmStageOrder_Type()
)
cfprFabricVnetEpSyncEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageOrder.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageRetry_Type = Gauge32
_CfprFabricVnetEpSyncEpFsmStageRetry_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageRetry = _CfprFabricVnetEpSyncEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 8),
    _CfprFabricVnetEpSyncEpFsmStageRetry_Type()
)
cfprFabricVnetEpSyncEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageRetry.setStatus("current")
_CfprFabricVnetEpSyncEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprFabricVnetEpSyncEpFsmStageStageStatus_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmStageStageStatus = _CfprFabricVnetEpSyncEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 120, 1, 9),
    _CfprFabricVnetEpSyncEpFsmStageStageStatus_Type()
)
cfprFabricVnetEpSyncEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmStageStageStatus.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskTable_Object = MibTable
cfprFabricVnetEpSyncEpFsmTaskTable = _CfprFabricVnetEpSyncEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121)
)
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskTable.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskEntry_Object = MibTableRow
cfprFabricVnetEpSyncEpFsmTaskEntry = _CfprFabricVnetEpSyncEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121, 1)
)
cfprFabricVnetEpSyncEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVnetEpSyncEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskEntry.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprFabricVnetEpSyncEpFsmTaskInstanceId_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmTaskInstanceId = _CfprFabricVnetEpSyncEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121, 1, 1),
    _CfprFabricVnetEpSyncEpFsmTaskInstanceId_Type()
)
cfprFabricVnetEpSyncEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskInstanceId.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprFabricVnetEpSyncEpFsmTaskDn_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmTaskDn = _CfprFabricVnetEpSyncEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121, 1, 2),
    _CfprFabricVnetEpSyncEpFsmTaskDn_Type()
)
cfprFabricVnetEpSyncEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskDn.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskRn_Type = SnmpAdminString
_CfprFabricVnetEpSyncEpFsmTaskRn_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmTaskRn = _CfprFabricVnetEpSyncEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121, 1, 3),
    _CfprFabricVnetEpSyncEpFsmTaskRn_Type()
)
cfprFabricVnetEpSyncEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskRn.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprFabricVnetEpSyncEpFsmTaskCompletion_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmTaskCompletion = _CfprFabricVnetEpSyncEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121, 1, 4),
    _CfprFabricVnetEpSyncEpFsmTaskCompletion_Type()
)
cfprFabricVnetEpSyncEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskCompletion.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskFlags_Type = CfprFsmFlags
_CfprFabricVnetEpSyncEpFsmTaskFlags_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmTaskFlags = _CfprFabricVnetEpSyncEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121, 1, 5),
    _CfprFabricVnetEpSyncEpFsmTaskFlags_Type()
)
cfprFabricVnetEpSyncEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskFlags.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskItem_Type = CfprFabricVnetEpSyncEpFsmTaskItem
_CfprFabricVnetEpSyncEpFsmTaskItem_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmTaskItem = _CfprFabricVnetEpSyncEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121, 1, 6),
    _CfprFabricVnetEpSyncEpFsmTaskItem_Type()
)
cfprFabricVnetEpSyncEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskItem.setStatus("current")
_CfprFabricVnetEpSyncEpFsmTaskSeqId_Type = Gauge32
_CfprFabricVnetEpSyncEpFsmTaskSeqId_Object = MibTableColumn
cfprFabricVnetEpSyncEpFsmTaskSeqId = _CfprFabricVnetEpSyncEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 121, 1, 7),
    _CfprFabricVnetEpSyncEpFsmTaskSeqId_Type()
)
cfprFabricVnetEpSyncEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVnetEpSyncEpFsmTaskSeqId.setStatus("current")
_CfprFabricVsanTable_Object = MibTable
cfprFabricVsanTable = _CfprFabricVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122)
)
if mibBuilder.loadTexts:
    cfprFabricVsanTable.setStatus("current")
_CfprFabricVsanEntry_Object = MibTableRow
cfprFabricVsanEntry = _CfprFabricVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1)
)
cfprFabricVsanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVsanEntry.setStatus("current")
_CfprFabricVsanInstanceId_Type = CfprManagedObjectId
_CfprFabricVsanInstanceId_Object = MibTableColumn
cfprFabricVsanInstanceId = _CfprFabricVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 1),
    _CfprFabricVsanInstanceId_Type()
)
cfprFabricVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVsanInstanceId.setStatus("current")
_CfprFabricVsanDn_Type = CfprManagedObjectDn
_CfprFabricVsanDn_Object = MibTableColumn
cfprFabricVsanDn = _CfprFabricVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 2),
    _CfprFabricVsanDn_Type()
)
cfprFabricVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanDn.setStatus("current")
_CfprFabricVsanRn_Type = SnmpAdminString
_CfprFabricVsanRn_Object = MibTableColumn
cfprFabricVsanRn = _CfprFabricVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 3),
    _CfprFabricVsanRn_Type()
)
cfprFabricVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanRn.setStatus("current")
_CfprFabricVsanDefaultZoning_Type = CfprFabricDefaultZoningState
_CfprFabricVsanDefaultZoning_Object = MibTableColumn
cfprFabricVsanDefaultZoning = _CfprFabricVsanDefaultZoning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 4),
    _CfprFabricVsanDefaultZoning_Type()
)
cfprFabricVsanDefaultZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanDefaultZoning.setStatus("current")
_CfprFabricVsanEpDn_Type = SnmpAdminString
_CfprFabricVsanEpDn_Object = MibTableColumn
cfprFabricVsanEpDn = _CfprFabricVsanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 5),
    _CfprFabricVsanEpDn_Type()
)
cfprFabricVsanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpDn.setStatus("current")
_CfprFabricVsanFcZoneSharingMode_Type = CfprFabricFcZoneSharingMode
_CfprFabricVsanFcZoneSharingMode_Object = MibTableColumn
cfprFabricVsanFcZoneSharingMode = _CfprFabricVsanFcZoneSharingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 6),
    _CfprFabricVsanFcZoneSharingMode_Type()
)
cfprFabricVsanFcZoneSharingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanFcZoneSharingMode.setStatus("current")
_CfprFabricVsanFcoeVlan_Type = Gauge32
_CfprFabricVsanFcoeVlan_Object = MibTableColumn
cfprFabricVsanFcoeVlan = _CfprFabricVsanFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 7),
    _CfprFabricVsanFcoeVlan_Type()
)
cfprFabricVsanFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanFcoeVlan.setStatus("current")
_CfprFabricVsanFltAggr_Type = Unsigned64
_CfprFabricVsanFltAggr_Object = MibTableColumn
cfprFabricVsanFltAggr = _CfprFabricVsanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 8),
    _CfprFabricVsanFltAggr_Type()
)
cfprFabricVsanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanFltAggr.setStatus("current")
_CfprFabricVsanGlobal_Type = Unsigned64
_CfprFabricVsanGlobal_Object = MibTableColumn
cfprFabricVsanGlobal = _CfprFabricVsanGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 9),
    _CfprFabricVsanGlobal_Type()
)
cfprFabricVsanGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanGlobal.setStatus("current")
_CfprFabricVsanId_Type = Gauge32
_CfprFabricVsanId_Object = MibTableColumn
cfprFabricVsanId = _CfprFabricVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 10),
    _CfprFabricVsanId_Type()
)
cfprFabricVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanId.setStatus("current")
_CfprFabricVsanIfRole_Type = CfprFabricVnetEpIfRole
_CfprFabricVsanIfRole_Object = MibTableColumn
cfprFabricVsanIfRole = _CfprFabricVsanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 11),
    _CfprFabricVsanIfRole_Type()
)
cfprFabricVsanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanIfRole.setStatus("current")
_CfprFabricVsanIfType_Type = CfprNetworkVnetEpIfType
_CfprFabricVsanIfType_Object = MibTableColumn
cfprFabricVsanIfType = _CfprFabricVsanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 12),
    _CfprFabricVsanIfType_Type()
)
cfprFabricVsanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanIfType.setStatus("current")
_CfprFabricVsanLocal_Type = Unsigned64
_CfprFabricVsanLocal_Object = MibTableColumn
cfprFabricVsanLocal = _CfprFabricVsanLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 13),
    _CfprFabricVsanLocal_Type()
)
cfprFabricVsanLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanLocal.setStatus("current")
_CfprFabricVsanLocale_Type = CfprFabricVnetEpLocale
_CfprFabricVsanLocale_Object = MibTableColumn
cfprFabricVsanLocale = _CfprFabricVsanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 14),
    _CfprFabricVsanLocale_Type()
)
cfprFabricVsanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanLocale.setStatus("current")
_CfprFabricVsanName_Type = SnmpAdminString
_CfprFabricVsanName_Object = MibTableColumn
cfprFabricVsanName = _CfprFabricVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 15),
    _CfprFabricVsanName_Type()
)
cfprFabricVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanName.setStatus("current")
_CfprFabricVsanOperState_Type = CfprFabricVsanOperState
_CfprFabricVsanOperState_Object = MibTableColumn
cfprFabricVsanOperState = _CfprFabricVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 16),
    _CfprFabricVsanOperState_Type()
)
cfprFabricVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanOperState.setStatus("current")
_CfprFabricVsanPeerDn_Type = SnmpAdminString
_CfprFabricVsanPeerDn_Object = MibTableColumn
cfprFabricVsanPeerDn = _CfprFabricVsanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 17),
    _CfprFabricVsanPeerDn_Type()
)
cfprFabricVsanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanPeerDn.setStatus("current")
_CfprFabricVsanPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprFabricVsanPolicyOwner_Object = MibTableColumn
cfprFabricVsanPolicyOwner = _CfprFabricVsanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 18),
    _CfprFabricVsanPolicyOwner_Type()
)
cfprFabricVsanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanPolicyOwner.setStatus("current")
_CfprFabricVsanSwitchId_Type = CfprFabricVsanSwitchId
_CfprFabricVsanSwitchId_Object = MibTableColumn
cfprFabricVsanSwitchId = _CfprFabricVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 19),
    _CfprFabricVsanSwitchId_Type()
)
cfprFabricVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanSwitchId.setStatus("current")
_CfprFabricVsanTransport_Type = CfprFabricAVsanTransport
_CfprFabricVsanTransport_Object = MibTableColumn
cfprFabricVsanTransport = _CfprFabricVsanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 20),
    _CfprFabricVsanTransport_Type()
)
cfprFabricVsanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanTransport.setStatus("current")
_CfprFabricVsanType_Type = CfprFabricAVsanType
_CfprFabricVsanType_Object = MibTableColumn
cfprFabricVsanType = _CfprFabricVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 21),
    _CfprFabricVsanType_Type()
)
cfprFabricVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanType.setStatus("current")
_CfprFabricVsanZoningState_Type = CfprFabricZoningState
_CfprFabricVsanZoningState_Object = MibTableColumn
cfprFabricVsanZoningState = _CfprFabricVsanZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 122, 1, 22),
    _CfprFabricVsanZoningState_Type()
)
cfprFabricVsanZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanZoningState.setStatus("current")
_CfprFabricVsanEpTable_Object = MibTable
cfprFabricVsanEpTable = _CfprFabricVsanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123)
)
if mibBuilder.loadTexts:
    cfprFabricVsanEpTable.setStatus("current")
_CfprFabricVsanEpEntry_Object = MibTableRow
cfprFabricVsanEpEntry = _CfprFabricVsanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1)
)
cfprFabricVsanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVsanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVsanEpEntry.setStatus("current")
_CfprFabricVsanEpInstanceId_Type = CfprManagedObjectId
_CfprFabricVsanEpInstanceId_Object = MibTableColumn
cfprFabricVsanEpInstanceId = _CfprFabricVsanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 1),
    _CfprFabricVsanEpInstanceId_Type()
)
cfprFabricVsanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVsanEpInstanceId.setStatus("current")
_CfprFabricVsanEpDnData_Type = CfprManagedObjectDn
_CfprFabricVsanEpDnData_Object = MibTableColumn
cfprFabricVsanEpDnData = _CfprFabricVsanEpDnData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 2),
    _CfprFabricVsanEpDnData_Type()
)
cfprFabricVsanEpDnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpDnData.setStatus("current")
_CfprFabricVsanEpRn_Type = SnmpAdminString
_CfprFabricVsanEpRn_Object = MibTableColumn
cfprFabricVsanEpRn = _CfprFabricVsanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 3),
    _CfprFabricVsanEpRn_Type()
)
cfprFabricVsanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpRn.setStatus("current")
_CfprFabricVsanEpEpDn_Type = SnmpAdminString
_CfprFabricVsanEpEpDn_Object = MibTableColumn
cfprFabricVsanEpEpDn = _CfprFabricVsanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 4),
    _CfprFabricVsanEpEpDn_Type()
)
cfprFabricVsanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpEpDn.setStatus("current")
_CfprFabricVsanEpFcoeVlan_Type = Gauge32
_CfprFabricVsanEpFcoeVlan_Object = MibTableColumn
cfprFabricVsanEpFcoeVlan = _CfprFabricVsanEpFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 5),
    _CfprFabricVsanEpFcoeVlan_Type()
)
cfprFabricVsanEpFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpFcoeVlan.setStatus("current")
_CfprFabricVsanEpId_Type = Gauge32
_CfprFabricVsanEpId_Object = MibTableColumn
cfprFabricVsanEpId = _CfprFabricVsanEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 6),
    _CfprFabricVsanEpId_Type()
)
cfprFabricVsanEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpId.setStatus("current")
_CfprFabricVsanEpIfRole_Type = CfprFabricVnetEpIfRole
_CfprFabricVsanEpIfRole_Object = MibTableColumn
cfprFabricVsanEpIfRole = _CfprFabricVsanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 7),
    _CfprFabricVsanEpIfRole_Type()
)
cfprFabricVsanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpIfRole.setStatus("current")
_CfprFabricVsanEpIfType_Type = CfprNetworkVnetEpIfType
_CfprFabricVsanEpIfType_Object = MibTableColumn
cfprFabricVsanEpIfType = _CfprFabricVsanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 8),
    _CfprFabricVsanEpIfType_Type()
)
cfprFabricVsanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpIfType.setStatus("current")
_CfprFabricVsanEpLocale_Type = CfprFabricVnetEpLocale
_CfprFabricVsanEpLocale_Object = MibTableColumn
cfprFabricVsanEpLocale = _CfprFabricVsanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 9),
    _CfprFabricVsanEpLocale_Type()
)
cfprFabricVsanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpLocale.setStatus("current")
_CfprFabricVsanEpName_Type = SnmpAdminString
_CfprFabricVsanEpName_Object = MibTableColumn
cfprFabricVsanEpName = _CfprFabricVsanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 10),
    _CfprFabricVsanEpName_Type()
)
cfprFabricVsanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpName.setStatus("current")
_CfprFabricVsanEpOperState_Type = CfprFabricVsanOperState
_CfprFabricVsanEpOperState_Object = MibTableColumn
cfprFabricVsanEpOperState = _CfprFabricVsanEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 11),
    _CfprFabricVsanEpOperState_Type()
)
cfprFabricVsanEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpOperState.setStatus("current")
_CfprFabricVsanEpPeerDn_Type = SnmpAdminString
_CfprFabricVsanEpPeerDn_Object = MibTableColumn
cfprFabricVsanEpPeerDn = _CfprFabricVsanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 12),
    _CfprFabricVsanEpPeerDn_Type()
)
cfprFabricVsanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpPeerDn.setStatus("current")
_CfprFabricVsanEpPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprFabricVsanEpPolicyOwner_Object = MibTableColumn
cfprFabricVsanEpPolicyOwner = _CfprFabricVsanEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 13),
    _CfprFabricVsanEpPolicyOwner_Type()
)
cfprFabricVsanEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpPolicyOwner.setStatus("current")
_CfprFabricVsanEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricVsanEpSwitchId_Object = MibTableColumn
cfprFabricVsanEpSwitchId = _CfprFabricVsanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 14),
    _CfprFabricVsanEpSwitchId_Type()
)
cfprFabricVsanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpSwitchId.setStatus("current")
_CfprFabricVsanEpTransport_Type = CfprFabricAVsanTransport
_CfprFabricVsanEpTransport_Object = MibTableColumn
cfprFabricVsanEpTransport = _CfprFabricVsanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 15),
    _CfprFabricVsanEpTransport_Type()
)
cfprFabricVsanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpTransport.setStatus("current")
_CfprFabricVsanEpType_Type = CfprFabricAVsanType
_CfprFabricVsanEpType_Object = MibTableColumn
cfprFabricVsanEpType = _CfprFabricVsanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 16),
    _CfprFabricVsanEpType_Type()
)
cfprFabricVsanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpType.setStatus("current")
_CfprFabricVsanEpZoningState_Type = CfprFabricZoningState
_CfprFabricVsanEpZoningState_Object = MibTableColumn
cfprFabricVsanEpZoningState = _CfprFabricVsanEpZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 123, 1, 17),
    _CfprFabricVsanEpZoningState_Type()
)
cfprFabricVsanEpZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanEpZoningState.setStatus("current")
_CfprFabricVsanMembershipTable_Object = MibTable
cfprFabricVsanMembershipTable = _CfprFabricVsanMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124)
)
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipTable.setStatus("current")
_CfprFabricVsanMembershipEntry_Object = MibTableRow
cfprFabricVsanMembershipEntry = _CfprFabricVsanMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124, 1)
)
cfprFabricVsanMembershipEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricVsanMembershipInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipEntry.setStatus("current")
_CfprFabricVsanMembershipInstanceId_Type = CfprManagedObjectId
_CfprFabricVsanMembershipInstanceId_Object = MibTableColumn
cfprFabricVsanMembershipInstanceId = _CfprFabricVsanMembershipInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124, 1, 1),
    _CfprFabricVsanMembershipInstanceId_Type()
)
cfprFabricVsanMembershipInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipInstanceId.setStatus("current")
_CfprFabricVsanMembershipDn_Type = CfprManagedObjectDn
_CfprFabricVsanMembershipDn_Object = MibTableColumn
cfprFabricVsanMembershipDn = _CfprFabricVsanMembershipDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124, 1, 2),
    _CfprFabricVsanMembershipDn_Type()
)
cfprFabricVsanMembershipDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipDn.setStatus("current")
_CfprFabricVsanMembershipRn_Type = SnmpAdminString
_CfprFabricVsanMembershipRn_Object = MibTableColumn
cfprFabricVsanMembershipRn = _CfprFabricVsanMembershipRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124, 1, 3),
    _CfprFabricVsanMembershipRn_Type()
)
cfprFabricVsanMembershipRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipRn.setStatus("current")
_CfprFabricVsanMembershipMemberStatus_Type = CfprFabricMemberStatus
_CfprFabricVsanMembershipMemberStatus_Object = MibTableColumn
cfprFabricVsanMembershipMemberStatus = _CfprFabricVsanMembershipMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124, 1, 4),
    _CfprFabricVsanMembershipMemberStatus_Type()
)
cfprFabricVsanMembershipMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipMemberStatus.setStatus("current")
_CfprFabricVsanMembershipParentAdminState_Type = CfprFabricAdminState
_CfprFabricVsanMembershipParentAdminState_Object = MibTableColumn
cfprFabricVsanMembershipParentAdminState = _CfprFabricVsanMembershipParentAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124, 1, 5),
    _CfprFabricVsanMembershipParentAdminState_Type()
)
cfprFabricVsanMembershipParentAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipParentAdminState.setStatus("current")
_CfprFabricVsanMembershipStateQual_Type = SnmpAdminString
_CfprFabricVsanMembershipStateQual_Object = MibTableColumn
cfprFabricVsanMembershipStateQual = _CfprFabricVsanMembershipStateQual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124, 1, 6),
    _CfprFabricVsanMembershipStateQual_Type()
)
cfprFabricVsanMembershipStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipStateQual.setStatus("current")
_CfprFabricVsanMembershipVsanId_Type = Gauge32
_CfprFabricVsanMembershipVsanId_Object = MibTableColumn
cfprFabricVsanMembershipVsanId = _CfprFabricVsanMembershipVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 124, 1, 7),
    _CfprFabricVsanMembershipVsanId_Type()
)
cfprFabricVsanMembershipVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricVsanMembershipVsanId.setStatus("current")
_CfprFabricZoneIdUniverseTable_Object = MibTable
cfprFabricZoneIdUniverseTable = _CfprFabricZoneIdUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 125)
)
if mibBuilder.loadTexts:
    cfprFabricZoneIdUniverseTable.setStatus("current")
_CfprFabricZoneIdUniverseEntry_Object = MibTableRow
cfprFabricZoneIdUniverseEntry = _CfprFabricZoneIdUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 125, 1)
)
cfprFabricZoneIdUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricZoneIdUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricZoneIdUniverseEntry.setStatus("current")
_CfprFabricZoneIdUniverseInstanceId_Type = CfprManagedObjectId
_CfprFabricZoneIdUniverseInstanceId_Object = MibTableColumn
cfprFabricZoneIdUniverseInstanceId = _CfprFabricZoneIdUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 125, 1, 1),
    _CfprFabricZoneIdUniverseInstanceId_Type()
)
cfprFabricZoneIdUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricZoneIdUniverseInstanceId.setStatus("current")
_CfprFabricZoneIdUniverseDn_Type = CfprManagedObjectDn
_CfprFabricZoneIdUniverseDn_Object = MibTableColumn
cfprFabricZoneIdUniverseDn = _CfprFabricZoneIdUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 125, 1, 2),
    _CfprFabricZoneIdUniverseDn_Type()
)
cfprFabricZoneIdUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricZoneIdUniverseDn.setStatus("current")
_CfprFabricZoneIdUniverseRn_Type = SnmpAdminString
_CfprFabricZoneIdUniverseRn_Object = MibTableColumn
cfprFabricZoneIdUniverseRn = _CfprFabricZoneIdUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 125, 1, 3),
    _CfprFabricZoneIdUniverseRn_Type()
)
cfprFabricZoneIdUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricZoneIdUniverseRn.setStatus("current")
_CfprFabricSspEthMonTable_Object = MibTable
cfprFabricSspEthMonTable = _CfprFabricSspEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126)
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonTable.setStatus("current")
_CfprFabricSspEthMonEntry_Object = MibTableRow
cfprFabricSspEthMonEntry = _CfprFabricSspEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1)
)
cfprFabricSspEthMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSspEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonEntry.setStatus("current")
_CfprFabricSspEthMonInstanceId_Type = CfprManagedObjectId
_CfprFabricSspEthMonInstanceId_Object = MibTableColumn
cfprFabricSspEthMonInstanceId = _CfprFabricSspEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 1),
    _CfprFabricSspEthMonInstanceId_Type()
)
cfprFabricSspEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonInstanceId.setStatus("current")
_CfprFabricSspEthMonDn_Type = CfprManagedObjectDn
_CfprFabricSspEthMonDn_Object = MibTableColumn
cfprFabricSspEthMonDn = _CfprFabricSspEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 2),
    _CfprFabricSspEthMonDn_Type()
)
cfprFabricSspEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonDn.setStatus("current")
_CfprFabricSspEthMonRn_Type = SnmpAdminString
_CfprFabricSspEthMonRn_Object = MibTableColumn
cfprFabricSspEthMonRn = _CfprFabricSspEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 3),
    _CfprFabricSspEthMonRn_Type()
)
cfprFabricSspEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonRn.setStatus("current")
_CfprFabricSspEthMonAdminState_Type = CfprFabricSspMonAdminState
_CfprFabricSspEthMonAdminState_Object = MibTableColumn
cfprFabricSspEthMonAdminState = _CfprFabricSspEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 4),
    _CfprFabricSspEthMonAdminState_Type()
)
cfprFabricSspEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonAdminState.setStatus("current")
_CfprFabricSspEthMonAppendFlag_Type = CfprFabricSspEthMonAppendFlag
_CfprFabricSspEthMonAppendFlag_Object = MibTableColumn
cfprFabricSspEthMonAppendFlag = _CfprFabricSspEthMonAppendFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 5),
    _CfprFabricSspEthMonAppendFlag_Type()
)
cfprFabricSspEthMonAppendFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonAppendFlag.setStatus("current")
_CfprFabricSspEthMonConfigFailReason_Type = SnmpAdminString
_CfprFabricSspEthMonConfigFailReason_Object = MibTableColumn
cfprFabricSspEthMonConfigFailReason = _CfprFabricSspEthMonConfigFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 6),
    _CfprFabricSspEthMonConfigFailReason_Type()
)
cfprFabricSspEthMonConfigFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonConfigFailReason.setStatus("current")
_CfprFabricSspEthMonDelPcap_Type = CfprFabricSspMonDelPcap
_CfprFabricSspEthMonDelPcap_Object = MibTableColumn
cfprFabricSspEthMonDelPcap = _CfprFabricSspEthMonDelPcap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 7),
    _CfprFabricSspEthMonDelPcap_Type()
)
cfprFabricSspEthMonDelPcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonDelPcap.setStatus("current")
_CfprFabricSspEthMonId_Type = CfprNetworkSwitchId
_CfprFabricSspEthMonId_Object = MibTableColumn
cfprFabricSspEthMonId = _CfprFabricSspEthMonId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 8),
    _CfprFabricSspEthMonId_Type()
)
cfprFabricSspEthMonId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonId.setStatus("current")
_CfprFabricSspEthMonIsConfigSuccess_Type = TruthValue
_CfprFabricSspEthMonIsConfigSuccess_Object = MibTableColumn
cfprFabricSspEthMonIsConfigSuccess = _CfprFabricSspEthMonIsConfigSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 9),
    _CfprFabricSspEthMonIsConfigSuccess_Type()
)
cfprFabricSspEthMonIsConfigSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonIsConfigSuccess.setStatus("current")
_CfprFabricSspEthMonName_Type = SnmpAdminString
_CfprFabricSspEthMonName_Object = MibTableColumn
cfprFabricSspEthMonName = _CfprFabricSspEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 10),
    _CfprFabricSspEthMonName_Type()
)
cfprFabricSspEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonName.setStatus("current")
_CfprFabricSspEthMonOperState_Type = CfprFabricSspMonOperState
_CfprFabricSspEthMonOperState_Object = MibTableColumn
cfprFabricSspEthMonOperState = _CfprFabricSspEthMonOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 11),
    _CfprFabricSspEthMonOperState_Type()
)
cfprFabricSspEthMonOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonOperState.setStatus("current")
_CfprFabricSspEthMonOperStateReason_Type = CfprFabricSspMonOperStateReason
_CfprFabricSspEthMonOperStateReason_Object = MibTableColumn
cfprFabricSspEthMonOperStateReason = _CfprFabricSspEthMonOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 12),
    _CfprFabricSspEthMonOperStateReason_Type()
)
cfprFabricSspEthMonOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonOperStateReason.setStatus("current")
_CfprFabricSspEthMonPeerDn_Type = SnmpAdminString
_CfprFabricSspEthMonPeerDn_Object = MibTableColumn
cfprFabricSspEthMonPeerDn = _CfprFabricSspEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 13),
    _CfprFabricSspEthMonPeerDn_Type()
)
cfprFabricSspEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonPeerDn.setStatus("current")
_CfprFabricSspEthMonSession_Type = Gauge32
_CfprFabricSspEthMonSession_Object = MibTableColumn
cfprFabricSspEthMonSession = _CfprFabricSspEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 14),
    _CfprFabricSspEthMonSession_Type()
)
cfprFabricSspEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSession.setStatus("current")
_CfprFabricSspEthMonSessionMemUsage_Type = Gauge32
_CfprFabricSspEthMonSessionMemUsage_Object = MibTableColumn
cfprFabricSspEthMonSessionMemUsage = _CfprFabricSspEthMonSessionMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 15),
    _CfprFabricSspEthMonSessionMemUsage_Type()
)
cfprFabricSspEthMonSessionMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSessionMemUsage.setStatus("current")
_CfprFabricSspEthMonSourceConfigured_Type = Gauge32
_CfprFabricSspEthMonSourceConfigured_Object = MibTableColumn
cfprFabricSspEthMonSourceConfigured = _CfprFabricSspEthMonSourceConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 16),
    _CfprFabricSspEthMonSourceConfigured_Type()
)
cfprFabricSspEthMonSourceConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSourceConfigured.setStatus("current")
_CfprFabricSspEthMonDelAllSessEnabledState_Type = CfprFabricSspEthMonDelAllSessEnabledState
_CfprFabricSspEthMonDelAllSessEnabledState_Object = MibTableColumn
cfprFabricSspEthMonDelAllSessEnabledState = _CfprFabricSspEthMonDelAllSessEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 17),
    _CfprFabricSspEthMonDelAllSessEnabledState_Type()
)
cfprFabricSspEthMonDelAllSessEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonDelAllSessEnabledState.setStatus("current")
_CfprFabricSspEthMonDropCount_Type = Unsigned64
_CfprFabricSspEthMonDropCount_Object = MibTableColumn
cfprFabricSspEthMonDropCount = _CfprFabricSspEthMonDropCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 18),
    _CfprFabricSspEthMonDropCount_Type()
)
cfprFabricSspEthMonDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonDropCount.setStatus("current")
_CfprFabricSspEthMonErrorCode_Type = SnmpAdminString
_CfprFabricSspEthMonErrorCode_Object = MibTableColumn
cfprFabricSspEthMonErrorCode = _CfprFabricSspEthMonErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 19),
    _CfprFabricSspEthMonErrorCode_Type()
)
cfprFabricSspEthMonErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonErrorCode.setStatus("current")
_CfprFabricSspEthMonIsConfiguredByAG_Type = TruthValue
_CfprFabricSspEthMonIsConfiguredByAG_Object = MibTableColumn
cfprFabricSspEthMonIsConfiguredByAG = _CfprFabricSspEthMonIsConfiguredByAG_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 20),
    _CfprFabricSspEthMonIsConfiguredByAG_Type()
)
cfprFabricSspEthMonIsConfiguredByAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonIsConfiguredByAG.setStatus("current")
_CfprFabricSspEthMonReBoot_Type = SnmpAdminString
_CfprFabricSspEthMonReBoot_Object = MibTableColumn
cfprFabricSspEthMonReBoot = _CfprFabricSspEthMonReBoot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 21),
    _CfprFabricSspEthMonReBoot_Type()
)
cfprFabricSspEthMonReBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonReBoot.setStatus("current")
_CfprFabricSspEthMonSessionPcapSnapLen_Type = Gauge32
_CfprFabricSspEthMonSessionPcapSnapLen_Object = MibTableColumn
cfprFabricSspEthMonSessionPcapSnapLen = _CfprFabricSspEthMonSessionPcapSnapLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 126, 1, 22),
    _CfprFabricSspEthMonSessionPcapSnapLen_Type()
)
cfprFabricSspEthMonSessionPcapSnapLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSessionPcapSnapLen.setStatus("current")
_CfprFabricSspEthMonFilterEpTable_Object = MibTable
cfprFabricSspEthMonFilterEpTable = _CfprFabricSspEthMonFilterEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127)
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpTable.setStatus("current")
_CfprFabricSspEthMonFilterEpEntry_Object = MibTableRow
cfprFabricSspEthMonFilterEpEntry = _CfprFabricSspEthMonFilterEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1)
)
cfprFabricSspEthMonFilterEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSspEthMonFilterEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpEntry.setStatus("current")
_CfprFabricSspEthMonFilterEpInstanceId_Type = CfprManagedObjectId
_CfprFabricSspEthMonFilterEpInstanceId_Object = MibTableColumn
cfprFabricSspEthMonFilterEpInstanceId = _CfprFabricSspEthMonFilterEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 1),
    _CfprFabricSspEthMonFilterEpInstanceId_Type()
)
cfprFabricSspEthMonFilterEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpInstanceId.setStatus("current")
_CfprFabricSspEthMonFilterEpDn_Type = CfprManagedObjectDn
_CfprFabricSspEthMonFilterEpDn_Object = MibTableColumn
cfprFabricSspEthMonFilterEpDn = _CfprFabricSspEthMonFilterEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 2),
    _CfprFabricSspEthMonFilterEpDn_Type()
)
cfprFabricSspEthMonFilterEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpDn.setStatus("current")
_CfprFabricSspEthMonFilterEpRn_Type = SnmpAdminString
_CfprFabricSspEthMonFilterEpRn_Object = MibTableColumn
cfprFabricSspEthMonFilterEpRn = _CfprFabricSspEthMonFilterEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 3),
    _CfprFabricSspEthMonFilterEpRn_Type()
)
cfprFabricSspEthMonFilterEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpRn.setStatus("current")
_CfprFabricSspEthMonFilterEpDestIp_Type = InetAddressIPv4
_CfprFabricSspEthMonFilterEpDestIp_Object = MibTableColumn
cfprFabricSspEthMonFilterEpDestIp = _CfprFabricSspEthMonFilterEpDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 4),
    _CfprFabricSspEthMonFilterEpDestIp_Type()
)
cfprFabricSspEthMonFilterEpDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpDestIp.setStatus("current")
_CfprFabricSspEthMonFilterEpDestMAC_Type = MacAddress
_CfprFabricSspEthMonFilterEpDestMAC_Object = MibTableColumn
cfprFabricSspEthMonFilterEpDestMAC = _CfprFabricSspEthMonFilterEpDestMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 5),
    _CfprFabricSspEthMonFilterEpDestMAC_Type()
)
cfprFabricSspEthMonFilterEpDestMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpDestMAC.setStatus("current")
_CfprFabricSspEthMonFilterEpDestPort_Type = Gauge32
_CfprFabricSspEthMonFilterEpDestPort_Object = MibTableColumn
cfprFabricSspEthMonFilterEpDestPort = _CfprFabricSspEthMonFilterEpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 6),
    _CfprFabricSspEthMonFilterEpDestPort_Type()
)
cfprFabricSspEthMonFilterEpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpDestPort.setStatus("current")
_CfprFabricSspEthMonFilterEpEthertype_Type = Gauge32
_CfprFabricSspEthMonFilterEpEthertype_Object = MibTableColumn
cfprFabricSspEthMonFilterEpEthertype = _CfprFabricSspEthMonFilterEpEthertype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 7),
    _CfprFabricSspEthMonFilterEpEthertype_Type()
)
cfprFabricSspEthMonFilterEpEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpEthertype.setStatus("current")
_CfprFabricSspEthMonFilterEpIvlan_Type = Gauge32
_CfprFabricSspEthMonFilterEpIvlan_Object = MibTableColumn
cfprFabricSspEthMonFilterEpIvlan = _CfprFabricSspEthMonFilterEpIvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 8),
    _CfprFabricSspEthMonFilterEpIvlan_Type()
)
cfprFabricSspEthMonFilterEpIvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpIvlan.setStatus("current")
_CfprFabricSspEthMonFilterEpNameId_Type = SnmpAdminString
_CfprFabricSspEthMonFilterEpNameId_Object = MibTableColumn
cfprFabricSspEthMonFilterEpNameId = _CfprFabricSspEthMonFilterEpNameId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 9),
    _CfprFabricSspEthMonFilterEpNameId_Type()
)
cfprFabricSspEthMonFilterEpNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpNameId.setStatus("current")
_CfprFabricSspEthMonFilterEpOvlan_Type = Gauge32
_CfprFabricSspEthMonFilterEpOvlan_Object = MibTableColumn
cfprFabricSspEthMonFilterEpOvlan = _CfprFabricSspEthMonFilterEpOvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 10),
    _CfprFabricSspEthMonFilterEpOvlan_Type()
)
cfprFabricSspEthMonFilterEpOvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpOvlan.setStatus("current")
_CfprFabricSspEthMonFilterEpProtocol_Type = Gauge32
_CfprFabricSspEthMonFilterEpProtocol_Object = MibTableColumn
cfprFabricSspEthMonFilterEpProtocol = _CfprFabricSspEthMonFilterEpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 11),
    _CfprFabricSspEthMonFilterEpProtocol_Type()
)
cfprFabricSspEthMonFilterEpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpProtocol.setStatus("current")
_CfprFabricSspEthMonFilterEpSrcIp_Type = InetAddressIPv4
_CfprFabricSspEthMonFilterEpSrcIp_Object = MibTableColumn
cfprFabricSspEthMonFilterEpSrcIp = _CfprFabricSspEthMonFilterEpSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 12),
    _CfprFabricSspEthMonFilterEpSrcIp_Type()
)
cfprFabricSspEthMonFilterEpSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpSrcIp.setStatus("current")
_CfprFabricSspEthMonFilterEpSrcMAC_Type = MacAddress
_CfprFabricSspEthMonFilterEpSrcMAC_Object = MibTableColumn
cfprFabricSspEthMonFilterEpSrcMAC = _CfprFabricSspEthMonFilterEpSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 13),
    _CfprFabricSspEthMonFilterEpSrcMAC_Type()
)
cfprFabricSspEthMonFilterEpSrcMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpSrcMAC.setStatus("current")
_CfprFabricSspEthMonFilterEpSrcPort_Type = Gauge32
_CfprFabricSspEthMonFilterEpSrcPort_Object = MibTableColumn
cfprFabricSspEthMonFilterEpSrcPort = _CfprFabricSspEthMonFilterEpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 14),
    _CfprFabricSspEthMonFilterEpSrcPort_Type()
)
cfprFabricSspEthMonFilterEpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpSrcPort.setStatus("current")
_CfprFabricSspEthMonFilterEpDestIpv6_Type = InetAddressIPv6
_CfprFabricSspEthMonFilterEpDestIpv6_Object = MibTableColumn
cfprFabricSspEthMonFilterEpDestIpv6 = _CfprFabricSspEthMonFilterEpDestIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 15),
    _CfprFabricSspEthMonFilterEpDestIpv6_Type()
)
cfprFabricSspEthMonFilterEpDestIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpDestIpv6.setStatus("current")
_CfprFabricSspEthMonFilterEpEcmpId_Type = Gauge32
_CfprFabricSspEthMonFilterEpEcmpId_Object = MibTableColumn
cfprFabricSspEthMonFilterEpEcmpId = _CfprFabricSspEthMonFilterEpEcmpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 16),
    _CfprFabricSspEthMonFilterEpEcmpId_Type()
)
cfprFabricSspEthMonFilterEpEcmpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpEcmpId.setStatus("current")
_CfprFabricSspEthMonFilterEpSrcIpv6_Type = InetAddressIPv6
_CfprFabricSspEthMonFilterEpSrcIpv6_Object = MibTableColumn
cfprFabricSspEthMonFilterEpSrcIpv6 = _CfprFabricSspEthMonFilterEpSrcIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 17),
    _CfprFabricSspEthMonFilterEpSrcIpv6_Type()
)
cfprFabricSspEthMonFilterEpSrcIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpSrcIpv6.setStatus("current")
_CfprFabricSspEthMonFilterEpSubvlan_Type = Gauge32
_CfprFabricSspEthMonFilterEpSubvlan_Object = MibTableColumn
cfprFabricSspEthMonFilterEpSubvlan = _CfprFabricSspEthMonFilterEpSubvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 18),
    _CfprFabricSspEthMonFilterEpSubvlan_Type()
)
cfprFabricSspEthMonFilterEpSubvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpSubvlan.setStatus("current")
_CfprFabricSspEthMonFilterEpVifId_Type = Gauge32
_CfprFabricSspEthMonFilterEpVifId_Object = MibTableColumn
cfprFabricSspEthMonFilterEpVifId = _CfprFabricSspEthMonFilterEpVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 127, 1, 19),
    _CfprFabricSspEthMonFilterEpVifId_Type()
)
cfprFabricSspEthMonFilterEpVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonFilterEpVifId.setStatus("current")
_CfprFabricSspEthMonSrcAppEpTable_Object = MibTable
cfprFabricSspEthMonSrcAppEpTable = _CfprFabricSspEthMonSrcAppEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128)
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpTable.setStatus("current")
_CfprFabricSspEthMonSrcAppEpEntry_Object = MibTableRow
cfprFabricSspEthMonSrcAppEpEntry = _CfprFabricSspEthMonSrcAppEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1)
)
cfprFabricSspEthMonSrcAppEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSspEthMonSrcAppEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpEntry.setStatus("current")
_CfprFabricSspEthMonSrcAppEpInstanceId_Type = CfprManagedObjectId
_CfprFabricSspEthMonSrcAppEpInstanceId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpInstanceId = _CfprFabricSspEthMonSrcAppEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 1),
    _CfprFabricSspEthMonSrcAppEpInstanceId_Type()
)
cfprFabricSspEthMonSrcAppEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpInstanceId.setStatus("current")
_CfprFabricSspEthMonSrcAppEpDn_Type = CfprManagedObjectDn
_CfprFabricSspEthMonSrcAppEpDn_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpDn = _CfprFabricSspEthMonSrcAppEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 2),
    _CfprFabricSspEthMonSrcAppEpDn_Type()
)
cfprFabricSspEthMonSrcAppEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpDn.setStatus("current")
_CfprFabricSspEthMonSrcAppEpRn_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpRn_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpRn = _CfprFabricSspEthMonSrcAppEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 3),
    _CfprFabricSspEthMonSrcAppEpRn_Type()
)
cfprFabricSspEthMonSrcAppEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpRn.setStatus("current")
_CfprFabricSspEthMonSrcAppEpAppName_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpAppName_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpAppName = _CfprFabricSspEthMonSrcAppEpAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 4),
    _CfprFabricSspEthMonSrcAppEpAppName_Type()
)
cfprFabricSspEthMonSrcAppEpAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpAppName.setStatus("current")
_CfprFabricSspEthMonSrcAppEpFilter_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpFilter_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpFilter = _CfprFabricSspEthMonSrcAppEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 5),
    _CfprFabricSspEthMonSrcAppEpFilter_Type()
)
cfprFabricSspEthMonSrcAppEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpFilter.setStatus("current")
_CfprFabricSspEthMonSrcAppEpLinkName_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpLinkName_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpLinkName = _CfprFabricSspEthMonSrcAppEpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 6),
    _CfprFabricSspEthMonSrcAppEpLinkName_Type()
)
cfprFabricSspEthMonSrcAppEpLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpLinkName.setStatus("current")
_CfprFabricSspEthMonSrcAppEpPcapfile_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpPcapfile_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpPcapfile = _CfprFabricSspEthMonSrcAppEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 7),
    _CfprFabricSspEthMonSrcAppEpPcapfile_Type()
)
cfprFabricSspEthMonSrcAppEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpPcapfile.setStatus("current")
_CfprFabricSspEthMonSrcAppEpPcapfilename_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpPcapfilename_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpPcapfilename = _CfprFabricSspEthMonSrcAppEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 8),
    _CfprFabricSspEthMonSrcAppEpPcapfilename_Type()
)
cfprFabricSspEthMonSrcAppEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpPcapfilename.setStatus("current")
_CfprFabricSspEthMonSrcAppEpPcapsize_Type = Gauge32
_CfprFabricSspEthMonSrcAppEpPcapsize_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpPcapsize = _CfprFabricSspEthMonSrcAppEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 9),
    _CfprFabricSspEthMonSrcAppEpPcapsize_Type()
)
cfprFabricSspEthMonSrcAppEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpPcapsize.setStatus("current")
_CfprFabricSspEthMonSrcAppEpPortName_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpPortName_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpPortName = _CfprFabricSspEthMonSrcAppEpPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 10),
    _CfprFabricSspEthMonSrcAppEpPortName_Type()
)
cfprFabricSspEthMonSrcAppEpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpPortName.setStatus("current")
_CfprFabricSspEthMonSrcAppEpSlotId_Type = CfprFabricPktCaptureAppSlotId
_CfprFabricSspEthMonSrcAppEpSlotId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpSlotId = _CfprFabricSspEthMonSrcAppEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 11),
    _CfprFabricSspEthMonSrcAppEpSlotId_Type()
)
cfprFabricSspEthMonSrcAppEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpSlotId.setStatus("current")
_CfprFabricSspEthMonSrcAppEpAppInstance_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpAppInstance_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpAppInstance = _CfprFabricSspEthMonSrcAppEpAppInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 12),
    _CfprFabricSspEthMonSrcAppEpAppInstance_Type()
)
cfprFabricSspEthMonSrcAppEpAppInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpAppInstance.setStatus("current")
_CfprFabricSspEthMonSrcAppEpSubInterface_Type = Gauge32
_CfprFabricSspEthMonSrcAppEpSubInterface_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpSubInterface = _CfprFabricSspEthMonSrcAppEpSubInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 13),
    _CfprFabricSspEthMonSrcAppEpSubInterface_Type()
)
cfprFabricSspEthMonSrcAppEpSubInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpSubInterface.setStatus("current")
_CfprFabricSspEthMonSrcAppEpExternalLduLinkDn_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppEpExternalLduLinkDn_Object = MibTableColumn
cfprFabricSspEthMonSrcAppEpExternalLduLinkDn = _CfprFabricSspEthMonSrcAppEpExternalLduLinkDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 128, 1, 14),
    _CfprFabricSspEthMonSrcAppEpExternalLduLinkDn_Type()
)
cfprFabricSspEthMonSrcAppEpExternalLduLinkDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppEpExternalLduLinkDn.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpTable_Object = MibTable
cfprFabricSspEthMonSrcAppLinksEpTable = _CfprFabricSspEthMonSrcAppLinksEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129)
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpTable.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpEntry_Object = MibTableRow
cfprFabricSspEthMonSrcAppLinksEpEntry = _CfprFabricSspEthMonSrcAppLinksEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1)
)
cfprFabricSspEthMonSrcAppLinksEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSspEthMonSrcAppLinksEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpEntry.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpInstanceId_Type = CfprManagedObjectId
_CfprFabricSspEthMonSrcAppLinksEpInstanceId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpInstanceId = _CfprFabricSspEthMonSrcAppLinksEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 1),
    _CfprFabricSspEthMonSrcAppLinksEpInstanceId_Type()
)
cfprFabricSspEthMonSrcAppLinksEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpInstanceId.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpDn_Type = CfprManagedObjectDn
_CfprFabricSspEthMonSrcAppLinksEpDn_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpDn = _CfprFabricSspEthMonSrcAppLinksEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 2),
    _CfprFabricSspEthMonSrcAppLinksEpDn_Type()
)
cfprFabricSspEthMonSrcAppLinksEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpDn.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpRn_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppLinksEpRn_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpRn = _CfprFabricSspEthMonSrcAppLinksEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 3),
    _CfprFabricSspEthMonSrcAppLinksEpRn_Type()
)
cfprFabricSspEthMonSrcAppLinksEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpRn.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpChassisId_Type = Gauge32
_CfprFabricSspEthMonSrcAppLinksEpChassisId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpChassisId = _CfprFabricSspEthMonSrcAppLinksEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 4),
    _CfprFabricSspEthMonSrcAppLinksEpChassisId_Type()
)
cfprFabricSspEthMonSrcAppLinksEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpChassisId.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpEqAggrPortId_Type = Gauge32
_CfprFabricSspEthMonSrcAppLinksEpEqAggrPortId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpEqAggrPortId = _CfprFabricSspEthMonSrcAppLinksEpEqAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 5),
    _CfprFabricSspEthMonSrcAppLinksEpEqAggrPortId_Type()
)
cfprFabricSspEthMonSrcAppLinksEpEqAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpEqAggrPortId.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpEqPortId_Type = Gauge32
_CfprFabricSspEthMonSrcAppLinksEpEqPortId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpEqPortId = _CfprFabricSspEthMonSrcAppLinksEpEqPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 6),
    _CfprFabricSspEthMonSrcAppLinksEpEqPortId_Type()
)
cfprFabricSspEthMonSrcAppLinksEpEqPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpEqPortId.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpEqSlotId_Type = Gauge32
_CfprFabricSspEthMonSrcAppLinksEpEqSlotId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpEqSlotId = _CfprFabricSspEthMonSrcAppLinksEpEqSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 7),
    _CfprFabricSspEthMonSrcAppLinksEpEqSlotId_Type()
)
cfprFabricSspEthMonSrcAppLinksEpEqSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpEqSlotId.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpFilter_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppLinksEpFilter_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpFilter = _CfprFabricSspEthMonSrcAppLinksEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 8),
    _CfprFabricSspEthMonSrcAppLinksEpFilter_Type()
)
cfprFabricSspEthMonSrcAppLinksEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpFilter.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpFilterDn_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppLinksEpFilterDn_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpFilterDn = _CfprFabricSspEthMonSrcAppLinksEpFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 9),
    _CfprFabricSspEthMonSrcAppLinksEpFilterDn_Type()
)
cfprFabricSspEthMonSrcAppLinksEpFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpFilterDn.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpLifeCycle_Type = CfprSwPktCaptureLifeCycle
_CfprFabricSspEthMonSrcAppLinksEpLifeCycle_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpLifeCycle = _CfprFabricSspEthMonSrcAppLinksEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 10),
    _CfprFabricSspEthMonSrcAppLinksEpLifeCycle_Type()
)
cfprFabricSspEthMonSrcAppLinksEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpLifeCycle.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpName_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppLinksEpName_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpName = _CfprFabricSspEthMonSrcAppLinksEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 11),
    _CfprFabricSspEthMonSrcAppLinksEpName_Type()
)
cfprFabricSspEthMonSrcAppLinksEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpName.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpPcapfile_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppLinksEpPcapfile_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpPcapfile = _CfprFabricSspEthMonSrcAppLinksEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 12),
    _CfprFabricSspEthMonSrcAppLinksEpPcapfile_Type()
)
cfprFabricSspEthMonSrcAppLinksEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpPcapfile.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpPcapfilename_Type = SnmpAdminString
_CfprFabricSspEthMonSrcAppLinksEpPcapfilename_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpPcapfilename = _CfprFabricSspEthMonSrcAppLinksEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 13),
    _CfprFabricSspEthMonSrcAppLinksEpPcapfilename_Type()
)
cfprFabricSspEthMonSrcAppLinksEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpPcapfilename.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpPcapsize_Type = Gauge32
_CfprFabricSspEthMonSrcAppLinksEpPcapsize_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpPcapsize = _CfprFabricSspEthMonSrcAppLinksEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 14),
    _CfprFabricSspEthMonSrcAppLinksEpPcapsize_Type()
)
cfprFabricSspEthMonSrcAppLinksEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpPcapsize.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricSspEthMonSrcAppLinksEpSwitchId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpSwitchId = _CfprFabricSspEthMonSrcAppLinksEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 15),
    _CfprFabricSspEthMonSrcAppLinksEpSwitchId_Type()
)
cfprFabricSspEthMonSrcAppLinksEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpSwitchId.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpVlan_Type = Gauge32
_CfprFabricSspEthMonSrcAppLinksEpVlan_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpVlan = _CfprFabricSspEthMonSrcAppLinksEpVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 16),
    _CfprFabricSspEthMonSrcAppLinksEpVlan_Type()
)
cfprFabricSspEthMonSrcAppLinksEpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpVlan.setStatus("current")
_CfprFabricSspEthMonSrcAppLinksEpVifId_Type = Gauge32
_CfprFabricSspEthMonSrcAppLinksEpVifId_Object = MibTableColumn
cfprFabricSspEthMonSrcAppLinksEpVifId = _CfprFabricSspEthMonSrcAppLinksEpVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 129, 1, 17),
    _CfprFabricSspEthMonSrcAppLinksEpVifId_Type()
)
cfprFabricSspEthMonSrcAppLinksEpVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcAppLinksEpVifId.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpTable_Object = MibTable
cfprFabricSspEthMonSrcPhyAggrEpTable = _CfprFabricSspEthMonSrcPhyAggrEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130)
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpTable.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpEntry_Object = MibTableRow
cfprFabricSspEthMonSrcPhyAggrEpEntry = _CfprFabricSspEthMonSrcPhyAggrEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1)
)
cfprFabricSspEthMonSrcPhyAggrEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSspEthMonSrcPhyAggrEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpEntry.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpInstanceId_Type = CfprManagedObjectId
_CfprFabricSspEthMonSrcPhyAggrEpInstanceId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpInstanceId = _CfprFabricSspEthMonSrcPhyAggrEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 1),
    _CfprFabricSspEthMonSrcPhyAggrEpInstanceId_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpInstanceId.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpDn_Type = CfprManagedObjectDn
_CfprFabricSspEthMonSrcPhyAggrEpDn_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpDn = _CfprFabricSspEthMonSrcPhyAggrEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 2),
    _CfprFabricSspEthMonSrcPhyAggrEpDn_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpDn.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpRn_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyAggrEpRn_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpRn = _CfprFabricSspEthMonSrcPhyAggrEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 3),
    _CfprFabricSspEthMonSrcPhyAggrEpRn_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpRn.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpAggrPortId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyAggrEpAggrPortId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpAggrPortId = _CfprFabricSspEthMonSrcPhyAggrEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 4),
    _CfprFabricSspEthMonSrcPhyAggrEpAggrPortId_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpAggrPortId.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId = _CfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 5),
    _CfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpChassisId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyAggrEpChassisId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpChassisId = _CfprFabricSspEthMonSrcPhyAggrEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 6),
    _CfprFabricSspEthMonSrcPhyAggrEpChassisId_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpChassisId.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpFilter_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyAggrEpFilter_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpFilter = _CfprFabricSspEthMonSrcPhyAggrEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 7),
    _CfprFabricSspEthMonSrcPhyAggrEpFilter_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpFilter.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpPcapfile_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyAggrEpPcapfile_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpPcapfile = _CfprFabricSspEthMonSrcPhyAggrEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 8),
    _CfprFabricSspEthMonSrcPhyAggrEpPcapfile_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpPcapfile.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpPcapfilename_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyAggrEpPcapfilename_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpPcapfilename = _CfprFabricSspEthMonSrcPhyAggrEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 9),
    _CfprFabricSspEthMonSrcPhyAggrEpPcapfilename_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpPcapfilename.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpPcapsize_Type = Gauge32
_CfprFabricSspEthMonSrcPhyAggrEpPcapsize_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpPcapsize = _CfprFabricSspEthMonSrcPhyAggrEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 10),
    _CfprFabricSspEthMonSrcPhyAggrEpPcapsize_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpPcapsize.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpSlotId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyAggrEpSlotId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpSlotId = _CfprFabricSspEthMonSrcPhyAggrEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 11),
    _CfprFabricSspEthMonSrcPhyAggrEpSlotId_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpSlotId.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricSspEthMonSrcPhyAggrEpSwitchId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpSwitchId = _CfprFabricSspEthMonSrcPhyAggrEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 12),
    _CfprFabricSspEthMonSrcPhyAggrEpSwitchId_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpSwitchId.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpAppInstance_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyAggrEpAppInstance_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpAppInstance = _CfprFabricSspEthMonSrcPhyAggrEpAppInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 13),
    _CfprFabricSspEthMonSrcPhyAggrEpAppInstance_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpAppInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpAppInstance.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpAppName_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyAggrEpAppName_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpAppName = _CfprFabricSspEthMonSrcPhyAggrEpAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 14),
    _CfprFabricSspEthMonSrcPhyAggrEpAppName_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpAppName.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpSubInterface_Type = Gauge32
_CfprFabricSspEthMonSrcPhyAggrEpSubInterface_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpSubInterface = _CfprFabricSspEthMonSrcPhyAggrEpSubInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 15),
    _CfprFabricSspEthMonSrcPhyAggrEpSubInterface_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpSubInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpSubInterface.setStatus("current")
_CfprFabricSspEthMonSrcPhyAggrEpEcmpId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyAggrEpEcmpId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyAggrEpEcmpId = _CfprFabricSspEthMonSrcPhyAggrEpEcmpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 130, 1, 16),
    _CfprFabricSspEthMonSrcPhyAggrEpEcmpId_Type()
)
cfprFabricSspEthMonSrcPhyAggrEpEcmpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyAggrEpEcmpId.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpTable_Object = MibTable
cfprFabricSspEthMonSrcPhyEpTable = _CfprFabricSspEthMonSrcPhyEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131)
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpTable.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpEntry_Object = MibTableRow
cfprFabricSspEthMonSrcPhyEpEntry = _CfprFabricSspEthMonSrcPhyEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1)
)
cfprFabricSspEthMonSrcPhyEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSspEthMonSrcPhyEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpEntry.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpInstanceId_Type = CfprManagedObjectId
_CfprFabricSspEthMonSrcPhyEpInstanceId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpInstanceId = _CfprFabricSspEthMonSrcPhyEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 1),
    _CfprFabricSspEthMonSrcPhyEpInstanceId_Type()
)
cfprFabricSspEthMonSrcPhyEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpInstanceId.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpDn_Type = CfprManagedObjectDn
_CfprFabricSspEthMonSrcPhyEpDn_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpDn = _CfprFabricSspEthMonSrcPhyEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 2),
    _CfprFabricSspEthMonSrcPhyEpDn_Type()
)
cfprFabricSspEthMonSrcPhyEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpDn.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpRn_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyEpRn_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpRn = _CfprFabricSspEthMonSrcPhyEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 3),
    _CfprFabricSspEthMonSrcPhyEpRn_Type()
)
cfprFabricSspEthMonSrcPhyEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpRn.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpChassisId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyEpChassisId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpChassisId = _CfprFabricSspEthMonSrcPhyEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 4),
    _CfprFabricSspEthMonSrcPhyEpChassisId_Type()
)
cfprFabricSspEthMonSrcPhyEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpChassisId.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpFilter_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyEpFilter_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpFilter = _CfprFabricSspEthMonSrcPhyEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 5),
    _CfprFabricSspEthMonSrcPhyEpFilter_Type()
)
cfprFabricSspEthMonSrcPhyEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpFilter.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpPcapfile_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyEpPcapfile_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpPcapfile = _CfprFabricSspEthMonSrcPhyEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 6),
    _CfprFabricSspEthMonSrcPhyEpPcapfile_Type()
)
cfprFabricSspEthMonSrcPhyEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpPcapfile.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpPcapfilename_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyEpPcapfilename_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpPcapfilename = _CfprFabricSspEthMonSrcPhyEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 7),
    _CfprFabricSspEthMonSrcPhyEpPcapfilename_Type()
)
cfprFabricSspEthMonSrcPhyEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpPcapfilename.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpPcapsize_Type = Gauge32
_CfprFabricSspEthMonSrcPhyEpPcapsize_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpPcapsize = _CfprFabricSspEthMonSrcPhyEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 8),
    _CfprFabricSspEthMonSrcPhyEpPcapsize_Type()
)
cfprFabricSspEthMonSrcPhyEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpPcapsize.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpPortId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyEpPortId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpPortId = _CfprFabricSspEthMonSrcPhyEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 9),
    _CfprFabricSspEthMonSrcPhyEpPortId_Type()
)
cfprFabricSspEthMonSrcPhyEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpPortId.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpSlotId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyEpSlotId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpSlotId = _CfprFabricSspEthMonSrcPhyEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 10),
    _CfprFabricSspEthMonSrcPhyEpSlotId_Type()
)
cfprFabricSspEthMonSrcPhyEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpSlotId.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpSwitchId_Type = CfprNetworkSwitchId
_CfprFabricSspEthMonSrcPhyEpSwitchId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpSwitchId = _CfprFabricSspEthMonSrcPhyEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 11),
    _CfprFabricSspEthMonSrcPhyEpSwitchId_Type()
)
cfprFabricSspEthMonSrcPhyEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpSwitchId.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpAppInstance_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyEpAppInstance_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpAppInstance = _CfprFabricSspEthMonSrcPhyEpAppInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 12),
    _CfprFabricSspEthMonSrcPhyEpAppInstance_Type()
)
cfprFabricSspEthMonSrcPhyEpAppInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpAppInstance.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpAppName_Type = SnmpAdminString
_CfprFabricSspEthMonSrcPhyEpAppName_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpAppName = _CfprFabricSspEthMonSrcPhyEpAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 13),
    _CfprFabricSspEthMonSrcPhyEpAppName_Type()
)
cfprFabricSspEthMonSrcPhyEpAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpAppName.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpSubInterface_Type = Gauge32
_CfprFabricSspEthMonSrcPhyEpSubInterface_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpSubInterface = _CfprFabricSspEthMonSrcPhyEpSubInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 14),
    _CfprFabricSspEthMonSrcPhyEpSubInterface_Type()
)
cfprFabricSspEthMonSrcPhyEpSubInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpSubInterface.setStatus("current")
_CfprFabricSspEthMonSrcPhyEpEcmpId_Type = Gauge32
_CfprFabricSspEthMonSrcPhyEpEcmpId_Object = MibTableColumn
cfprFabricSspEthMonSrcPhyEpEcmpId = _CfprFabricSspEthMonSrcPhyEpEcmpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 131, 1, 15),
    _CfprFabricSspEthMonSrcPhyEpEcmpId_Type()
)
cfprFabricSspEthMonSrcPhyEpEcmpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspEthMonSrcPhyEpEcmpId.setStatus("current")
_CfprFabricSspLanMonCloudTable_Object = MibTable
cfprFabricSspLanMonCloudTable = _CfprFabricSspLanMonCloudTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 132)
)
if mibBuilder.loadTexts:
    cfprFabricSspLanMonCloudTable.setStatus("current")
_CfprFabricSspLanMonCloudEntry_Object = MibTableRow
cfprFabricSspLanMonCloudEntry = _CfprFabricSspLanMonCloudEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 132, 1)
)
cfprFabricSspLanMonCloudEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSspLanMonCloudInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSspLanMonCloudEntry.setStatus("current")
_CfprFabricSspLanMonCloudInstanceId_Type = CfprManagedObjectId
_CfprFabricSspLanMonCloudInstanceId_Object = MibTableColumn
cfprFabricSspLanMonCloudInstanceId = _CfprFabricSspLanMonCloudInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 132, 1, 1),
    _CfprFabricSspLanMonCloudInstanceId_Type()
)
cfprFabricSspLanMonCloudInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSspLanMonCloudInstanceId.setStatus("current")
_CfprFabricSspLanMonCloudDn_Type = CfprManagedObjectDn
_CfprFabricSspLanMonCloudDn_Object = MibTableColumn
cfprFabricSspLanMonCloudDn = _CfprFabricSspLanMonCloudDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 132, 1, 2),
    _CfprFabricSspLanMonCloudDn_Type()
)
cfprFabricSspLanMonCloudDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspLanMonCloudDn.setStatus("current")
_CfprFabricSspLanMonCloudRn_Type = SnmpAdminString
_CfprFabricSspLanMonCloudRn_Object = MibTableColumn
cfprFabricSspLanMonCloudRn = _CfprFabricSspLanMonCloudRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 132, 1, 3),
    _CfprFabricSspLanMonCloudRn_Type()
)
cfprFabricSspLanMonCloudRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspLanMonCloudRn.setStatus("current")
_CfprFabricSspLanMonCloudMode_Type = CfprFabricSwitchingMode
_CfprFabricSspLanMonCloudMode_Object = MibTableColumn
cfprFabricSspLanMonCloudMode = _CfprFabricSspLanMonCloudMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 132, 1, 4),
    _CfprFabricSspLanMonCloudMode_Type()
)
cfprFabricSspLanMonCloudMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspLanMonCloudMode.setStatus("current")
_CfprFabricSspLanMonCloudDelAllSess_Type = CfprFabricSspLanMonCloudDelAllSess
_CfprFabricSspLanMonCloudDelAllSess_Object = MibTableColumn
cfprFabricSspLanMonCloudDelAllSess = _CfprFabricSspLanMonCloudDelAllSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 132, 1, 5),
    _CfprFabricSspLanMonCloudDelAllSess_Type()
)
cfprFabricSspLanMonCloudDelAllSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSspLanMonCloudDelAllSess.setStatus("current")
_CfprFabricInnerVlanMgrTable_Object = MibTable
cfprFabricInnerVlanMgrTable = _CfprFabricInnerVlanMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 133)
)
if mibBuilder.loadTexts:
    cfprFabricInnerVlanMgrTable.setStatus("current")
_CfprFabricInnerVlanMgrEntry_Object = MibTableRow
cfprFabricInnerVlanMgrEntry = _CfprFabricInnerVlanMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 133, 1)
)
cfprFabricInnerVlanMgrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricInnerVlanMgrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricInnerVlanMgrEntry.setStatus("current")
_CfprFabricInnerVlanMgrInstanceId_Type = CfprManagedObjectId
_CfprFabricInnerVlanMgrInstanceId_Object = MibTableColumn
cfprFabricInnerVlanMgrInstanceId = _CfprFabricInnerVlanMgrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 133, 1, 1),
    _CfprFabricInnerVlanMgrInstanceId_Type()
)
cfprFabricInnerVlanMgrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricInnerVlanMgrInstanceId.setStatus("current")
_CfprFabricInnerVlanMgrDn_Type = CfprManagedObjectDn
_CfprFabricInnerVlanMgrDn_Object = MibTableColumn
cfprFabricInnerVlanMgrDn = _CfprFabricInnerVlanMgrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 133, 1, 2),
    _CfprFabricInnerVlanMgrDn_Type()
)
cfprFabricInnerVlanMgrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricInnerVlanMgrDn.setStatus("current")
_CfprFabricInnerVlanMgrRn_Type = SnmpAdminString
_CfprFabricInnerVlanMgrRn_Object = MibTableColumn
cfprFabricInnerVlanMgrRn = _CfprFabricInnerVlanMgrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 133, 1, 3),
    _CfprFabricInnerVlanMgrRn_Type()
)
cfprFabricInnerVlanMgrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricInnerVlanMgrRn.setStatus("current")
_CfprFabricInnerVlanMgrFltAggr_Type = Unsigned64
_CfprFabricInnerVlanMgrFltAggr_Object = MibTableColumn
cfprFabricInnerVlanMgrFltAggr = _CfprFabricInnerVlanMgrFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 133, 1, 4),
    _CfprFabricInnerVlanMgrFltAggr_Type()
)
cfprFabricInnerVlanMgrFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricInnerVlanMgrFltAggr.setStatus("current")
_CfprFabricInnerVlanMgrId_Type = CfprNetworkSwitchId
_CfprFabricInnerVlanMgrId_Object = MibTableColumn
cfprFabricInnerVlanMgrId = _CfprFabricInnerVlanMgrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 133, 1, 5),
    _CfprFabricInnerVlanMgrId_Type()
)
cfprFabricInnerVlanMgrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricInnerVlanMgrId.setStatus("current")
_CfprFabricSubIfTable_Object = MibTable
cfprFabricSubIfTable = _CfprFabricSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134)
)
if mibBuilder.loadTexts:
    cfprFabricSubIfTable.setStatus("current")
_CfprFabricSubIfEntry_Object = MibTableRow
cfprFabricSubIfEntry = _CfprFabricSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1)
)
cfprFabricSubIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-FABRIC-MIB", "cfprFabricSubIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprFabricSubIfEntry.setStatus("current")
_CfprFabricSubIfInstanceId_Type = CfprManagedObjectId
_CfprFabricSubIfInstanceId_Object = MibTableColumn
cfprFabricSubIfInstanceId = _CfprFabricSubIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 1),
    _CfprFabricSubIfInstanceId_Type()
)
cfprFabricSubIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprFabricSubIfInstanceId.setStatus("current")
_CfprFabricSubIfDn_Type = CfprManagedObjectDn
_CfprFabricSubIfDn_Object = MibTableColumn
cfprFabricSubIfDn = _CfprFabricSubIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 2),
    _CfprFabricSubIfDn_Type()
)
cfprFabricSubIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubIfDn.setStatus("current")
_CfprFabricSubIfRn_Type = SnmpAdminString
_CfprFabricSubIfRn_Object = MibTableColumn
cfprFabricSubIfRn = _CfprFabricSubIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 3),
    _CfprFabricSubIfRn_Type()
)
cfprFabricSubIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubIfRn.setStatus("current")
_CfprFabricSubIfAllowSharing_Type = TruthValue
_CfprFabricSubIfAllowSharing_Object = MibTableColumn
cfprFabricSubIfAllowSharing = _CfprFabricSubIfAllowSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 4),
    _CfprFabricSubIfAllowSharing_Type()
)
cfprFabricSubIfAllowSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubIfAllowSharing.setStatus("current")
_CfprFabricSubIfDescr_Type = SnmpAdminString
_CfprFabricSubIfDescr_Object = MibTableColumn
cfprFabricSubIfDescr = _CfprFabricSubIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 5),
    _CfprFabricSubIfDescr_Type()
)
cfprFabricSubIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubIfDescr.setStatus("current")
_CfprFabricSubIfIfName_Type = SnmpAdminString
_CfprFabricSubIfIfName_Object = MibTableColumn
cfprFabricSubIfIfName = _CfprFabricSubIfIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 6),
    _CfprFabricSubIfIfName_Type()
)
cfprFabricSubIfIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubIfIfName.setStatus("current")
_CfprFabricSubIfSsaPortType_Type = CfprFabricSSASubPortType
_CfprFabricSubIfSsaPortType_Object = MibTableColumn
cfprFabricSubIfSsaPortType = _CfprFabricSubIfSsaPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 7),
    _CfprFabricSubIfSsaPortType_Type()
)
cfprFabricSubIfSsaPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubIfSsaPortType.setStatus("current")
_CfprFabricSubIfSubId_Type = Gauge32
_CfprFabricSubIfSubId_Object = MibTableColumn
cfprFabricSubIfSubId = _CfprFabricSubIfSubId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 8),
    _CfprFabricSubIfSubId_Type()
)
cfprFabricSubIfSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubIfSubId.setStatus("current")
_CfprFabricSubIfVlanId_Type = Integer32
_CfprFabricSubIfVlanId_Object = MibTableColumn
cfprFabricSubIfVlanId = _CfprFabricSubIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 26, 134, 1, 9),
    _CfprFabricSubIfVlanId_Type()
)
cfprFabricSubIfVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprFabricSubIfVlanId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-FABRIC-MIB",
    **{"cfprFabricObjects": cfprFabricObjects,
       "cfprFabricBHVlanTable": cfprFabricBHVlanTable,
       "cfprFabricBHVlanEntry": cfprFabricBHVlanEntry,
       "cfprFabricBHVlanInstanceId": cfprFabricBHVlanInstanceId,
       "cfprFabricBHVlanDn": cfprFabricBHVlanDn,
       "cfprFabricBHVlanRn": cfprFabricBHVlanRn,
       "cfprFabricBHVlanAssocPrimaryVlanState": cfprFabricBHVlanAssocPrimaryVlanState,
       "cfprFabricBHVlanAssocPrimaryVlanSwitchId": cfprFabricBHVlanAssocPrimaryVlanSwitchId,
       "cfprFabricBHVlanEpDn": cfprFabricBHVlanEpDn,
       "cfprFabricBHVlanId": cfprFabricBHVlanId,
       "cfprFabricBHVlanIfRole": cfprFabricBHVlanIfRole,
       "cfprFabricBHVlanIfType": cfprFabricBHVlanIfType,
       "cfprFabricBHVlanLocale": cfprFabricBHVlanLocale,
       "cfprFabricBHVlanName": cfprFabricBHVlanName,
       "cfprFabricBHVlanOperState": cfprFabricBHVlanOperState,
       "cfprFabricBHVlanOverlapStateForA": cfprFabricBHVlanOverlapStateForA,
       "cfprFabricBHVlanOverlapStateForB": cfprFabricBHVlanOverlapStateForB,
       "cfprFabricBHVlanPeerDn": cfprFabricBHVlanPeerDn,
       "cfprFabricBHVlanPolicyOwner": cfprFabricBHVlanPolicyOwner,
       "cfprFabricBHVlanPubNwDn": cfprFabricBHVlanPubNwDn,
       "cfprFabricBHVlanPubNwId": cfprFabricBHVlanPubNwId,
       "cfprFabricBHVlanPubNwName": cfprFabricBHVlanPubNwName,
       "cfprFabricBHVlanSharing": cfprFabricBHVlanSharing,
       "cfprFabricBHVlanSwitchId": cfprFabricBHVlanSwitchId,
       "cfprFabricBHVlanTransport": cfprFabricBHVlanTransport,
       "cfprFabricBHVlanType": cfprFabricBHVlanType,
       "cfprFabricBreakoutTable": cfprFabricBreakoutTable,
       "cfprFabricBreakoutEntry": cfprFabricBreakoutEntry,
       "cfprFabricBreakoutInstanceId": cfprFabricBreakoutInstanceId,
       "cfprFabricBreakoutDn": cfprFabricBreakoutDn,
       "cfprFabricBreakoutRn": cfprFabricBreakoutRn,
       "cfprFabricBreakoutBreakoutType": cfprFabricBreakoutBreakoutType,
       "cfprFabricBreakoutPortId": cfprFabricBreakoutPortId,
       "cfprFabricBreakoutSlotId": cfprFabricBreakoutSlotId,
       "cfprFabricCablingTable": cfprFabricCablingTable,
       "cfprFabricCablingEntry": cfprFabricCablingEntry,
       "cfprFabricCablingInstanceId": cfprFabricCablingInstanceId,
       "cfprFabricCablingDn": cfprFabricCablingDn,
       "cfprFabricCablingRn": cfprFabricCablingRn,
       "cfprFabricCablingSwTable": cfprFabricCablingSwTable,
       "cfprFabricCablingSwEntry": cfprFabricCablingSwEntry,
       "cfprFabricCablingSwInstanceId": cfprFabricCablingSwInstanceId,
       "cfprFabricCablingSwDn": cfprFabricCablingSwDn,
       "cfprFabricCablingSwRn": cfprFabricCablingSwRn,
       "cfprFabricCablingSwId": cfprFabricCablingSwId,
       "cfprFabricCablingSwLocale": cfprFabricCablingSwLocale,
       "cfprFabricCablingSwName": cfprFabricCablingSwName,
       "cfprFabricCablingSwTransport": cfprFabricCablingSwTransport,
       "cfprFabricCablingSwType": cfprFabricCablingSwType,
       "cfprFabricCdpLinkPolicyTable": cfprFabricCdpLinkPolicyTable,
       "cfprFabricCdpLinkPolicyEntry": cfprFabricCdpLinkPolicyEntry,
       "cfprFabricCdpLinkPolicyInstanceId": cfprFabricCdpLinkPolicyInstanceId,
       "cfprFabricCdpLinkPolicyDn": cfprFabricCdpLinkPolicyDn,
       "cfprFabricCdpLinkPolicyRn": cfprFabricCdpLinkPolicyRn,
       "cfprFabricCdpLinkPolicyAdminState": cfprFabricCdpLinkPolicyAdminState,
       "cfprFabricCdpLinkPolicyDescr": cfprFabricCdpLinkPolicyDescr,
       "cfprFabricCdpLinkPolicyIntId": cfprFabricCdpLinkPolicyIntId,
       "cfprFabricCdpLinkPolicyName": cfprFabricCdpLinkPolicyName,
       "cfprFabricCdpLinkPolicyPolicyLevel": cfprFabricCdpLinkPolicyPolicyLevel,
       "cfprFabricCdpLinkPolicyPolicyOwner": cfprFabricCdpLinkPolicyPolicyOwner,
       "cfprFabricCdpLinkPolicyProtocol": cfprFabricCdpLinkPolicyProtocol,
       "cfprFabricCdpLinkPolicyType": cfprFabricCdpLinkPolicyType,
       "cfprFabricChangedObjectRefTable": cfprFabricChangedObjectRefTable,
       "cfprFabricChangedObjectRefEntry": cfprFabricChangedObjectRefEntry,
       "cfprFabricChangedObjectRefInstanceId": cfprFabricChangedObjectRefInstanceId,
       "cfprFabricChangedObjectRefDn": cfprFabricChangedObjectRefDn,
       "cfprFabricChangedObjectRefRn": cfprFabricChangedObjectRefRn,
       "cfprFabricChangedObjectRefCentraleVnetEpDn": cfprFabricChangedObjectRefCentraleVnetEpDn,
       "cfprFabricChangedObjectRefId": cfprFabricChangedObjectRefId,
       "cfprFabricChangedObjectRefOldCentraleVnetEpDn": cfprFabricChangedObjectRefOldCentraleVnetEpDn,
       "cfprFabricChangedObjectRefRefObjStatus": cfprFabricChangedObjectRefRefObjStatus,
       "cfprFabricChangedObjectRefFprmVnetEpDn": cfprFabricChangedObjectRefFprmVnetEpDn,
       "cfprFabricChassisEpTable": cfprFabricChassisEpTable,
       "cfprFabricChassisEpEntry": cfprFabricChassisEpEntry,
       "cfprFabricChassisEpInstanceId": cfprFabricChassisEpInstanceId,
       "cfprFabricChassisEpDn": cfprFabricChassisEpDn,
       "cfprFabricChassisEpRn": cfprFabricChassisEpRn,
       "cfprFabricChassisEpAdminState": cfprFabricChassisEpAdminState,
       "cfprFabricChassisEpAggrPortId": cfprFabricChassisEpAggrPortId,
       "cfprFabricChassisEpChassisDn": cfprFabricChassisEpChassisDn,
       "cfprFabricChassisEpChassisId": cfprFabricChassisEpChassisId,
       "cfprFabricChassisEpEpDn": cfprFabricChassisEpEpDn,
       "cfprFabricChassisEpFltAggr": cfprFabricChassisEpFltAggr,
       "cfprFabricChassisEpIfRole": cfprFabricChassisEpIfRole,
       "cfprFabricChassisEpIfType": cfprFabricChassisEpIfType,
       "cfprFabricChassisEpLicGP": cfprFabricChassisEpLicGP,
       "cfprFabricChassisEpLicState": cfprFabricChassisEpLicState,
       "cfprFabricChassisEpLocale": cfprFabricChassisEpLocale,
       "cfprFabricChassisEpModel": cfprFabricChassisEpModel,
       "cfprFabricChassisEpName": cfprFabricChassisEpName,
       "cfprFabricChassisEpOperState": cfprFabricChassisEpOperState,
       "cfprFabricChassisEpOperStateReason": cfprFabricChassisEpOperStateReason,
       "cfprFabricChassisEpPeerAggrPortId": cfprFabricChassisEpPeerAggrPortId,
       "cfprFabricChassisEpPeerChassisId": cfprFabricChassisEpPeerChassisId,
       "cfprFabricChassisEpPeerDn": cfprFabricChassisEpPeerDn,
       "cfprFabricChassisEpPeerPortId": cfprFabricChassisEpPeerPortId,
       "cfprFabricChassisEpPeerSlotId": cfprFabricChassisEpPeerSlotId,
       "cfprFabricChassisEpPortId": cfprFabricChassisEpPortId,
       "cfprFabricChassisEpRevision": cfprFabricChassisEpRevision,
       "cfprFabricChassisEpSerial": cfprFabricChassisEpSerial,
       "cfprFabricChassisEpSlotId": cfprFabricChassisEpSlotId,
       "cfprFabricChassisEpSwitchId": cfprFabricChassisEpSwitchId,
       "cfprFabricChassisEpTransport": cfprFabricChassisEpTransport,
       "cfprFabricChassisEpType": cfprFabricChassisEpType,
       "cfprFabricChassisEpVendor": cfprFabricChassisEpVendor,
       "cfprFabricComputePhEpTable": cfprFabricComputePhEpTable,
       "cfprFabricComputePhEpEntry": cfprFabricComputePhEpEntry,
       "cfprFabricComputePhEpInstanceId": cfprFabricComputePhEpInstanceId,
       "cfprFabricComputePhEpDn": cfprFabricComputePhEpDn,
       "cfprFabricComputePhEpRn": cfprFabricComputePhEpRn,
       "cfprFabricComputePhEpAdminState": cfprFabricComputePhEpAdminState,
       "cfprFabricComputePhEpAggrPortId": cfprFabricComputePhEpAggrPortId,
       "cfprFabricComputePhEpBoardAggregationRole": cfprFabricComputePhEpBoardAggregationRole,
       "cfprFabricComputePhEpChassisId": cfprFabricComputePhEpChassisId,
       "cfprFabricComputePhEpCheckpointTrigTs": cfprFabricComputePhEpCheckpointTrigTs,
       "cfprFabricComputePhEpDeepCheckpointTrigTs": cfprFabricComputePhEpDeepCheckpointTrigTs,
       "cfprFabricComputePhEpDiscTrigTs": cfprFabricComputePhEpDiscTrigTs,
       "cfprFabricComputePhEpEpDn": cfprFabricComputePhEpEpDn,
       "cfprFabricComputePhEpEqType": cfprFabricComputePhEpEqType,
       "cfprFabricComputePhEpFltAggr": cfprFabricComputePhEpFltAggr,
       "cfprFabricComputePhEpIfRole": cfprFabricComputePhEpIfRole,
       "cfprFabricComputePhEpIfType": cfprFabricComputePhEpIfType,
       "cfprFabricComputePhEpLc": cfprFabricComputePhEpLc,
       "cfprFabricComputePhEpLicGP": cfprFabricComputePhEpLicGP,
       "cfprFabricComputePhEpLicState": cfprFabricComputePhEpLicState,
       "cfprFabricComputePhEpLocale": cfprFabricComputePhEpLocale,
       "cfprFabricComputePhEpModel": cfprFabricComputePhEpModel,
       "cfprFabricComputePhEpName": cfprFabricComputePhEpName,
       "cfprFabricComputePhEpOperState": cfprFabricComputePhEpOperState,
       "cfprFabricComputePhEpOperStateReason": cfprFabricComputePhEpOperStateReason,
       "cfprFabricComputePhEpPeerAggrPortId": cfprFabricComputePhEpPeerAggrPortId,
       "cfprFabricComputePhEpPeerChassisId": cfprFabricComputePhEpPeerChassisId,
       "cfprFabricComputePhEpPeerDn": cfprFabricComputePhEpPeerDn,
       "cfprFabricComputePhEpPeerPortId": cfprFabricComputePhEpPeerPortId,
       "cfprFabricComputePhEpPeerSlotId": cfprFabricComputePhEpPeerSlotId,
       "cfprFabricComputePhEpPortId": cfprFabricComputePhEpPortId,
       "cfprFabricComputePhEpProfileDn": cfprFabricComputePhEpProfileDn,
       "cfprFabricComputePhEpRevision": cfprFabricComputePhEpRevision,
       "cfprFabricComputePhEpSerial": cfprFabricComputePhEpSerial,
       "cfprFabricComputePhEpSlotId": cfprFabricComputePhEpSlotId,
       "cfprFabricComputePhEpSwitchId": cfprFabricComputePhEpSwitchId,
       "cfprFabricComputePhEpTransport": cfprFabricComputePhEpTransport,
       "cfprFabricComputePhEpType": cfprFabricComputePhEpType,
       "cfprFabricComputePhEpVendor": cfprFabricComputePhEpVendor,
       "cfprFabricComputeSlotEpTable": cfprFabricComputeSlotEpTable,
       "cfprFabricComputeSlotEpEntry": cfprFabricComputeSlotEpEntry,
       "cfprFabricComputeSlotEpInstanceId": cfprFabricComputeSlotEpInstanceId,
       "cfprFabricComputeSlotEpDn": cfprFabricComputeSlotEpDn,
       "cfprFabricComputeSlotEpRn": cfprFabricComputeSlotEpRn,
       "cfprFabricComputeSlotEpAdminState": cfprFabricComputeSlotEpAdminState,
       "cfprFabricComputeSlotEpAggrPortId": cfprFabricComputeSlotEpAggrPortId,
       "cfprFabricComputeSlotEpBoardAggregationRole": cfprFabricComputeSlotEpBoardAggregationRole,
       "cfprFabricComputeSlotEpChassisId": cfprFabricComputeSlotEpChassisId,
       "cfprFabricComputeSlotEpConnPath": cfprFabricComputeSlotEpConnPath,
       "cfprFabricComputeSlotEpConnStatus": cfprFabricComputeSlotEpConnStatus,
       "cfprFabricComputeSlotEpDiscovery": cfprFabricComputeSlotEpDiscovery,
       "cfprFabricComputeSlotEpEpDn": cfprFabricComputeSlotEpEpDn,
       "cfprFabricComputeSlotEpFactoryResetFlag": cfprFabricComputeSlotEpFactoryResetFlag,
       "cfprFabricComputeSlotEpFltAggr": cfprFabricComputeSlotEpFltAggr,
       "cfprFabricComputeSlotEpFruIdentTrigTs": cfprFabricComputeSlotEpFruIdentTrigTs,
       "cfprFabricComputeSlotEpFsmDescr": cfprFabricComputeSlotEpFsmDescr,
       "cfprFabricComputeSlotEpFsmPrev": cfprFabricComputeSlotEpFsmPrev,
       "cfprFabricComputeSlotEpFsmProgr": cfprFabricComputeSlotEpFsmProgr,
       "cfprFabricComputeSlotEpFsmRmtInvErrCode": cfprFabricComputeSlotEpFsmRmtInvErrCode,
       "cfprFabricComputeSlotEpFsmRmtInvErrDescr": cfprFabricComputeSlotEpFsmRmtInvErrDescr,
       "cfprFabricComputeSlotEpFsmRmtInvRslt": cfprFabricComputeSlotEpFsmRmtInvRslt,
       "cfprFabricComputeSlotEpFsmStageDescr": cfprFabricComputeSlotEpFsmStageDescr,
       "cfprFabricComputeSlotEpFsmStamp": cfprFabricComputeSlotEpFsmStamp,
       "cfprFabricComputeSlotEpFsmStatus": cfprFabricComputeSlotEpFsmStatus,
       "cfprFabricComputeSlotEpFsmTry": cfprFabricComputeSlotEpFsmTry,
       "cfprFabricComputeSlotEpIfRole": cfprFabricComputeSlotEpIfRole,
       "cfprFabricComputeSlotEpIfType": cfprFabricComputeSlotEpIfType,
       "cfprFabricComputeSlotEpLcTs": cfprFabricComputeSlotEpLcTs,
       "cfprFabricComputeSlotEpLicGP": cfprFabricComputeSlotEpLicGP,
       "cfprFabricComputeSlotEpLicState": cfprFabricComputeSlotEpLicState,
       "cfprFabricComputeSlotEpLocale": cfprFabricComputeSlotEpLocale,
       "cfprFabricComputeSlotEpManagingInst": cfprFabricComputeSlotEpManagingInst,
       "cfprFabricComputeSlotEpModel": cfprFabricComputeSlotEpModel,
       "cfprFabricComputeSlotEpName": cfprFabricComputeSlotEpName,
       "cfprFabricComputeSlotEpOperState": cfprFabricComputeSlotEpOperState,
       "cfprFabricComputeSlotEpOperStateReason": cfprFabricComputeSlotEpOperStateReason,
       "cfprFabricComputeSlotEpPeerAggrPortId": cfprFabricComputeSlotEpPeerAggrPortId,
       "cfprFabricComputeSlotEpPeerChassisId": cfprFabricComputeSlotEpPeerChassisId,
       "cfprFabricComputeSlotEpPeerDn": cfprFabricComputeSlotEpPeerDn,
       "cfprFabricComputeSlotEpPeerPortId": cfprFabricComputeSlotEpPeerPortId,
       "cfprFabricComputeSlotEpPeerSlotEpDn": cfprFabricComputeSlotEpPeerSlotEpDn,
       "cfprFabricComputeSlotEpPeerSlotId": cfprFabricComputeSlotEpPeerSlotId,
       "cfprFabricComputeSlotEpPortId": cfprFabricComputeSlotEpPortId,
       "cfprFabricComputeSlotEpPresence": cfprFabricComputeSlotEpPresence,
       "cfprFabricComputeSlotEpPresencePath": cfprFabricComputeSlotEpPresencePath,
       "cfprFabricComputeSlotEpRevision": cfprFabricComputeSlotEpRevision,
       "cfprFabricComputeSlotEpSerial": cfprFabricComputeSlotEpSerial,
       "cfprFabricComputeSlotEpSlotId": cfprFabricComputeSlotEpSlotId,
       "cfprFabricComputeSlotEpSwitchId": cfprFabricComputeSlotEpSwitchId,
       "cfprFabricComputeSlotEpTransport": cfprFabricComputeSlotEpTransport,
       "cfprFabricComputeSlotEpType": cfprFabricComputeSlotEpType,
       "cfprFabricComputeSlotEpVendor": cfprFabricComputeSlotEpVendor,
       "cfprFabricComputeSlotEpBladeState": cfprFabricComputeSlotEpBladeState,
       "cfprFabricComputeSlotEpDecommissionSecure": cfprFabricComputeSlotEpDecommissionSecure,
       "cfprFabricComputeSlotEpFailReason": cfprFabricComputeSlotEpFailReason,
       "cfprFabricComputeSlotEpFsmTable": cfprFabricComputeSlotEpFsmTable,
       "cfprFabricComputeSlotEpFsmEntry": cfprFabricComputeSlotEpFsmEntry,
       "cfprFabricComputeSlotEpFsmInstanceId": cfprFabricComputeSlotEpFsmInstanceId,
       "cfprFabricComputeSlotEpFsmDn": cfprFabricComputeSlotEpFsmDn,
       "cfprFabricComputeSlotEpFsmRn": cfprFabricComputeSlotEpFsmRn,
       "cfprFabricComputeSlotEpFsmCompletionTime": cfprFabricComputeSlotEpFsmCompletionTime,
       "cfprFabricComputeSlotEpFsmCurrentFsm": cfprFabricComputeSlotEpFsmCurrentFsm,
       "cfprFabricComputeSlotEpFsmDescrData": cfprFabricComputeSlotEpFsmDescrData,
       "cfprFabricComputeSlotEpFsmFsmStatus": cfprFabricComputeSlotEpFsmFsmStatus,
       "cfprFabricComputeSlotEpFsmProgress": cfprFabricComputeSlotEpFsmProgress,
       "cfprFabricComputeSlotEpFsmRmtErrCode": cfprFabricComputeSlotEpFsmRmtErrCode,
       "cfprFabricComputeSlotEpFsmRmtErrDescr": cfprFabricComputeSlotEpFsmRmtErrDescr,
       "cfprFabricComputeSlotEpFsmRmtRslt": cfprFabricComputeSlotEpFsmRmtRslt,
       "cfprFabricComputeSlotEpFsmStageTable": cfprFabricComputeSlotEpFsmStageTable,
       "cfprFabricComputeSlotEpFsmStageEntry": cfprFabricComputeSlotEpFsmStageEntry,
       "cfprFabricComputeSlotEpFsmStageInstanceId": cfprFabricComputeSlotEpFsmStageInstanceId,
       "cfprFabricComputeSlotEpFsmStageDn": cfprFabricComputeSlotEpFsmStageDn,
       "cfprFabricComputeSlotEpFsmStageRn": cfprFabricComputeSlotEpFsmStageRn,
       "cfprFabricComputeSlotEpFsmStageDescrData": cfprFabricComputeSlotEpFsmStageDescrData,
       "cfprFabricComputeSlotEpFsmStageLastUpdateTime": cfprFabricComputeSlotEpFsmStageLastUpdateTime,
       "cfprFabricComputeSlotEpFsmStageName": cfprFabricComputeSlotEpFsmStageName,
       "cfprFabricComputeSlotEpFsmStageOrder": cfprFabricComputeSlotEpFsmStageOrder,
       "cfprFabricComputeSlotEpFsmStageRetry": cfprFabricComputeSlotEpFsmStageRetry,
       "cfprFabricComputeSlotEpFsmStageStageStatus": cfprFabricComputeSlotEpFsmStageStageStatus,
       "cfprFabricComputeSlotEpFsmTaskTable": cfprFabricComputeSlotEpFsmTaskTable,
       "cfprFabricComputeSlotEpFsmTaskEntry": cfprFabricComputeSlotEpFsmTaskEntry,
       "cfprFabricComputeSlotEpFsmTaskInstanceId": cfprFabricComputeSlotEpFsmTaskInstanceId,
       "cfprFabricComputeSlotEpFsmTaskDn": cfprFabricComputeSlotEpFsmTaskDn,
       "cfprFabricComputeSlotEpFsmTaskRn": cfprFabricComputeSlotEpFsmTaskRn,
       "cfprFabricComputeSlotEpFsmTaskCompletion": cfprFabricComputeSlotEpFsmTaskCompletion,
       "cfprFabricComputeSlotEpFsmTaskFlags": cfprFabricComputeSlotEpFsmTaskFlags,
       "cfprFabricComputeSlotEpFsmTaskItem": cfprFabricComputeSlotEpFsmTaskItem,
       "cfprFabricComputeSlotEpFsmTaskSeqId": cfprFabricComputeSlotEpFsmTaskSeqId,
       "cfprFabricDceSrvTable": cfprFabricDceSrvTable,
       "cfprFabricDceSrvEntry": cfprFabricDceSrvEntry,
       "cfprFabricDceSrvInstanceId": cfprFabricDceSrvInstanceId,
       "cfprFabricDceSrvDn": cfprFabricDceSrvDn,
       "cfprFabricDceSrvRn": cfprFabricDceSrvRn,
       "cfprFabricDceSrvId": cfprFabricDceSrvId,
       "cfprFabricDceSrvLocale": cfprFabricDceSrvLocale,
       "cfprFabricDceSrvName": cfprFabricDceSrvName,
       "cfprFabricDceSrvTransport": cfprFabricDceSrvTransport,
       "cfprFabricDceSrvType": cfprFabricDceSrvType,
       "cfprFabricDceSwSrvTable": cfprFabricDceSwSrvTable,
       "cfprFabricDceSwSrvEntry": cfprFabricDceSwSrvEntry,
       "cfprFabricDceSwSrvInstanceId": cfprFabricDceSwSrvInstanceId,
       "cfprFabricDceSwSrvDn": cfprFabricDceSwSrvDn,
       "cfprFabricDceSwSrvRn": cfprFabricDceSwSrvRn,
       "cfprFabricDceSwSrvId": cfprFabricDceSwSrvId,
       "cfprFabricDceSwSrvLocale": cfprFabricDceSwSrvLocale,
       "cfprFabricDceSwSrvName": cfprFabricDceSwSrvName,
       "cfprFabricDceSwSrvTransport": cfprFabricDceSwSrvTransport,
       "cfprFabricDceSwSrvType": cfprFabricDceSwSrvType,
       "cfprFabricDceSwSrvEpTable": cfprFabricDceSwSrvEpTable,
       "cfprFabricDceSwSrvEpEntry": cfprFabricDceSwSrvEpEntry,
       "cfprFabricDceSwSrvEpInstanceId": cfprFabricDceSwSrvEpInstanceId,
       "cfprFabricDceSwSrvEpDn": cfprFabricDceSwSrvEpDn,
       "cfprFabricDceSwSrvEpRn": cfprFabricDceSwSrvEpRn,
       "cfprFabricDceSwSrvEpAdminState": cfprFabricDceSwSrvEpAdminState,
       "cfprFabricDceSwSrvEpAggrPortId": cfprFabricDceSwSrvEpAggrPortId,
       "cfprFabricDceSwSrvEpChassisId": cfprFabricDceSwSrvEpChassisId,
       "cfprFabricDceSwSrvEpEpDn": cfprFabricDceSwSrvEpEpDn,
       "cfprFabricDceSwSrvEpFltAggr": cfprFabricDceSwSrvEpFltAggr,
       "cfprFabricDceSwSrvEpIfRole": cfprFabricDceSwSrvEpIfRole,
       "cfprFabricDceSwSrvEpIfType": cfprFabricDceSwSrvEpIfType,
       "cfprFabricDceSwSrvEpLicGP": cfprFabricDceSwSrvEpLicGP,
       "cfprFabricDceSwSrvEpLicState": cfprFabricDceSwSrvEpLicState,
       "cfprFabricDceSwSrvEpLocale": cfprFabricDceSwSrvEpLocale,
       "cfprFabricDceSwSrvEpName": cfprFabricDceSwSrvEpName,
       "cfprFabricDceSwSrvEpOperState": cfprFabricDceSwSrvEpOperState,
       "cfprFabricDceSwSrvEpOperStateReason": cfprFabricDceSwSrvEpOperStateReason,
       "cfprFabricDceSwSrvEpPeerAggrPortId": cfprFabricDceSwSrvEpPeerAggrPortId,
       "cfprFabricDceSwSrvEpPeerChassisId": cfprFabricDceSwSrvEpPeerChassisId,
       "cfprFabricDceSwSrvEpPeerDn": cfprFabricDceSwSrvEpPeerDn,
       "cfprFabricDceSwSrvEpPeerPortId": cfprFabricDceSwSrvEpPeerPortId,
       "cfprFabricDceSwSrvEpPeerSlotId": cfprFabricDceSwSrvEpPeerSlotId,
       "cfprFabricDceSwSrvEpPortId": cfprFabricDceSwSrvEpPortId,
       "cfprFabricDceSwSrvEpSlotId": cfprFabricDceSwSrvEpSlotId,
       "cfprFabricDceSwSrvEpSwitchId": cfprFabricDceSwSrvEpSwitchId,
       "cfprFabricDceSwSrvEpTransport": cfprFabricDceSwSrvEpTransport,
       "cfprFabricDceSwSrvEpType": cfprFabricDceSwSrvEpType,
       "cfprFabricDceSwSrvEpUsrLbl": cfprFabricDceSwSrvEpUsrLbl,
       "cfprFabricDceSwSrvPcTable": cfprFabricDceSwSrvPcTable,
       "cfprFabricDceSwSrvPcEntry": cfprFabricDceSwSrvPcEntry,
       "cfprFabricDceSwSrvPcInstanceId": cfprFabricDceSwSrvPcInstanceId,
       "cfprFabricDceSwSrvPcDn": cfprFabricDceSwSrvPcDn,
       "cfprFabricDceSwSrvPcRn": cfprFabricDceSwSrvPcRn,
       "cfprFabricDceSwSrvPcAdminState": cfprFabricDceSwSrvPcAdminState,
       "cfprFabricDceSwSrvPcChassisId": cfprFabricDceSwSrvPcChassisId,
       "cfprFabricDceSwSrvPcDescr": cfprFabricDceSwSrvPcDescr,
       "cfprFabricDceSwSrvPcEpDn": cfprFabricDceSwSrvPcEpDn,
       "cfprFabricDceSwSrvPcFltAggr": cfprFabricDceSwSrvPcFltAggr,
       "cfprFabricDceSwSrvPcIfRole": cfprFabricDceSwSrvPcIfRole,
       "cfprFabricDceSwSrvPcIfType": cfprFabricDceSwSrvPcIfType,
       "cfprFabricDceSwSrvPcLocale": cfprFabricDceSwSrvPcLocale,
       "cfprFabricDceSwSrvPcName": cfprFabricDceSwSrvPcName,
       "cfprFabricDceSwSrvPcOperSpeed": cfprFabricDceSwSrvPcOperSpeed,
       "cfprFabricDceSwSrvPcOperState": cfprFabricDceSwSrvPcOperState,
       "cfprFabricDceSwSrvPcPeerDn": cfprFabricDceSwSrvPcPeerDn,
       "cfprFabricDceSwSrvPcPortId": cfprFabricDceSwSrvPcPortId,
       "cfprFabricDceSwSrvPcStateQual": cfprFabricDceSwSrvPcStateQual,
       "cfprFabricDceSwSrvPcSwitchId": cfprFabricDceSwSrvPcSwitchId,
       "cfprFabricDceSwSrvPcTransport": cfprFabricDceSwSrvPcTransport,
       "cfprFabricDceSwSrvPcType": cfprFabricDceSwSrvPcType,
       "cfprFabricDceSwSrvPcEpTable": cfprFabricDceSwSrvPcEpTable,
       "cfprFabricDceSwSrvPcEpEntry": cfprFabricDceSwSrvPcEpEntry,
       "cfprFabricDceSwSrvPcEpInstanceId": cfprFabricDceSwSrvPcEpInstanceId,
       "cfprFabricDceSwSrvPcEpDnData": cfprFabricDceSwSrvPcEpDnData,
       "cfprFabricDceSwSrvPcEpRn": cfprFabricDceSwSrvPcEpRn,
       "cfprFabricDceSwSrvPcEpAdminState": cfprFabricDceSwSrvPcEpAdminState,
       "cfprFabricDceSwSrvPcEpAggrPortId": cfprFabricDceSwSrvPcEpAggrPortId,
       "cfprFabricDceSwSrvPcEpChassisId": cfprFabricDceSwSrvPcEpChassisId,
       "cfprFabricDceSwSrvPcEpEpDn": cfprFabricDceSwSrvPcEpEpDn,
       "cfprFabricDceSwSrvPcEpFltAggr": cfprFabricDceSwSrvPcEpFltAggr,
       "cfprFabricDceSwSrvPcEpIfRole": cfprFabricDceSwSrvPcEpIfRole,
       "cfprFabricDceSwSrvPcEpIfType": cfprFabricDceSwSrvPcEpIfType,
       "cfprFabricDceSwSrvPcEpLicGP": cfprFabricDceSwSrvPcEpLicGP,
       "cfprFabricDceSwSrvPcEpLicState": cfprFabricDceSwSrvPcEpLicState,
       "cfprFabricDceSwSrvPcEpLocale": cfprFabricDceSwSrvPcEpLocale,
       "cfprFabricDceSwSrvPcEpMembership": cfprFabricDceSwSrvPcEpMembership,
       "cfprFabricDceSwSrvPcEpName": cfprFabricDceSwSrvPcEpName,
       "cfprFabricDceSwSrvPcEpOperState": cfprFabricDceSwSrvPcEpOperState,
       "cfprFabricDceSwSrvPcEpOperStateReason": cfprFabricDceSwSrvPcEpOperStateReason,
       "cfprFabricDceSwSrvPcEpPeerAggrPortId": cfprFabricDceSwSrvPcEpPeerAggrPortId,
       "cfprFabricDceSwSrvPcEpPeerChassisId": cfprFabricDceSwSrvPcEpPeerChassisId,
       "cfprFabricDceSwSrvPcEpPeerDn": cfprFabricDceSwSrvPcEpPeerDn,
       "cfprFabricDceSwSrvPcEpPeerPortId": cfprFabricDceSwSrvPcEpPeerPortId,
       "cfprFabricDceSwSrvPcEpPeerSlotId": cfprFabricDceSwSrvPcEpPeerSlotId,
       "cfprFabricDceSwSrvPcEpPortId": cfprFabricDceSwSrvPcEpPortId,
       "cfprFabricDceSwSrvPcEpSlotId": cfprFabricDceSwSrvPcEpSlotId,
       "cfprFabricDceSwSrvPcEpSwitchId": cfprFabricDceSwSrvPcEpSwitchId,
       "cfprFabricDceSwSrvPcEpTransport": cfprFabricDceSwSrvPcEpTransport,
       "cfprFabricDceSwSrvPcEpType": cfprFabricDceSwSrvPcEpType,
       "cfprFabricDceSwSrvPcEpUsrLbl": cfprFabricDceSwSrvPcEpUsrLbl,
       "cfprFabricEpTable": cfprFabricEpTable,
       "cfprFabricEpEntry": cfprFabricEpEntry,
       "cfprFabricEpInstanceId": cfprFabricEpInstanceId,
       "cfprFabricEpDn": cfprFabricEpDn,
       "cfprFabricEpRn": cfprFabricEpRn,
       "cfprFabricEpMgrTable": cfprFabricEpMgrTable,
       "cfprFabricEpMgrEntry": cfprFabricEpMgrEntry,
       "cfprFabricEpMgrInstanceId": cfprFabricEpMgrInstanceId,
       "cfprFabricEpMgrDn": cfprFabricEpMgrDn,
       "cfprFabricEpMgrRn": cfprFabricEpMgrRn,
       "cfprFabricEpMgrConfMode": cfprFabricEpMgrConfMode,
       "cfprFabricEpMgrConfQual": cfprFabricEpMgrConfQual,
       "cfprFabricEpMgrConfState": cfprFabricEpMgrConfState,
       "cfprFabricEpMgrFltAggr": cfprFabricEpMgrFltAggr,
       "cfprFabricEpMgrFsmDescr": cfprFabricEpMgrFsmDescr,
       "cfprFabricEpMgrFsmFlags": cfprFabricEpMgrFsmFlags,
       "cfprFabricEpMgrFsmPrev": cfprFabricEpMgrFsmPrev,
       "cfprFabricEpMgrFsmProgr": cfprFabricEpMgrFsmProgr,
       "cfprFabricEpMgrFsmRmtInvErrCode": cfprFabricEpMgrFsmRmtInvErrCode,
       "cfprFabricEpMgrFsmRmtInvErrDescr": cfprFabricEpMgrFsmRmtInvErrDescr,
       "cfprFabricEpMgrFsmRmtInvRslt": cfprFabricEpMgrFsmRmtInvRslt,
       "cfprFabricEpMgrFsmStageDescr": cfprFabricEpMgrFsmStageDescr,
       "cfprFabricEpMgrFsmStamp": cfprFabricEpMgrFsmStamp,
       "cfprFabricEpMgrFsmStatus": cfprFabricEpMgrFsmStatus,
       "cfprFabricEpMgrFsmTry": cfprFabricEpMgrFsmTry,
       "cfprFabricEpMgrId": cfprFabricEpMgrId,
       "cfprFabricEpMgrFsmTable": cfprFabricEpMgrFsmTable,
       "cfprFabricEpMgrFsmEntry": cfprFabricEpMgrFsmEntry,
       "cfprFabricEpMgrFsmInstanceId": cfprFabricEpMgrFsmInstanceId,
       "cfprFabricEpMgrFsmDn": cfprFabricEpMgrFsmDn,
       "cfprFabricEpMgrFsmRn": cfprFabricEpMgrFsmRn,
       "cfprFabricEpMgrFsmCompletionTime": cfprFabricEpMgrFsmCompletionTime,
       "cfprFabricEpMgrFsmCurrentFsm": cfprFabricEpMgrFsmCurrentFsm,
       "cfprFabricEpMgrFsmDescrData": cfprFabricEpMgrFsmDescrData,
       "cfprFabricEpMgrFsmFsmStatus": cfprFabricEpMgrFsmFsmStatus,
       "cfprFabricEpMgrFsmProgress": cfprFabricEpMgrFsmProgress,
       "cfprFabricEpMgrFsmRmtErrCode": cfprFabricEpMgrFsmRmtErrCode,
       "cfprFabricEpMgrFsmRmtErrDescr": cfprFabricEpMgrFsmRmtErrDescr,
       "cfprFabricEpMgrFsmRmtRslt": cfprFabricEpMgrFsmRmtRslt,
       "cfprFabricEpMgrFsmStageTable": cfprFabricEpMgrFsmStageTable,
       "cfprFabricEpMgrFsmStageEntry": cfprFabricEpMgrFsmStageEntry,
       "cfprFabricEpMgrFsmStageInstanceId": cfprFabricEpMgrFsmStageInstanceId,
       "cfprFabricEpMgrFsmStageDn": cfprFabricEpMgrFsmStageDn,
       "cfprFabricEpMgrFsmStageRn": cfprFabricEpMgrFsmStageRn,
       "cfprFabricEpMgrFsmStageDescrData": cfprFabricEpMgrFsmStageDescrData,
       "cfprFabricEpMgrFsmStageLastUpdateTime": cfprFabricEpMgrFsmStageLastUpdateTime,
       "cfprFabricEpMgrFsmStageName": cfprFabricEpMgrFsmStageName,
       "cfprFabricEpMgrFsmStageOrder": cfprFabricEpMgrFsmStageOrder,
       "cfprFabricEpMgrFsmStageRetry": cfprFabricEpMgrFsmStageRetry,
       "cfprFabricEpMgrFsmStageStageStatus": cfprFabricEpMgrFsmStageStageStatus,
       "cfprFabricEpMgrFsmTaskTable": cfprFabricEpMgrFsmTaskTable,
       "cfprFabricEpMgrFsmTaskEntry": cfprFabricEpMgrFsmTaskEntry,
       "cfprFabricEpMgrFsmTaskInstanceId": cfprFabricEpMgrFsmTaskInstanceId,
       "cfprFabricEpMgrFsmTaskDn": cfprFabricEpMgrFsmTaskDn,
       "cfprFabricEpMgrFsmTaskRn": cfprFabricEpMgrFsmTaskRn,
       "cfprFabricEpMgrFsmTaskCompletion": cfprFabricEpMgrFsmTaskCompletion,
       "cfprFabricEpMgrFsmTaskFlags": cfprFabricEpMgrFsmTaskFlags,
       "cfprFabricEpMgrFsmTaskItem": cfprFabricEpMgrFsmTaskItem,
       "cfprFabricEpMgrFsmTaskSeqId": cfprFabricEpMgrFsmTaskSeqId,
       "cfprFabricEthEstcTable": cfprFabricEthEstcTable,
       "cfprFabricEthEstcEntry": cfprFabricEthEstcEntry,
       "cfprFabricEthEstcInstanceId": cfprFabricEthEstcInstanceId,
       "cfprFabricEthEstcDn": cfprFabricEthEstcDn,
       "cfprFabricEthEstcRn": cfprFabricEthEstcRn,
       "cfprFabricEthEstcId": cfprFabricEthEstcId,
       "cfprFabricEthEstcLocale": cfprFabricEthEstcLocale,
       "cfprFabricEthEstcName": cfprFabricEthEstcName,
       "cfprFabricEthEstcTransport": cfprFabricEthEstcTransport,
       "cfprFabricEthEstcType": cfprFabricEthEstcType,
       "cfprFabricEthEstcCloudTable": cfprFabricEthEstcCloudTable,
       "cfprFabricEthEstcCloudEntry": cfprFabricEthEstcCloudEntry,
       "cfprFabricEthEstcCloudInstanceId": cfprFabricEthEstcCloudInstanceId,
       "cfprFabricEthEstcCloudDn": cfprFabricEthEstcCloudDn,
       "cfprFabricEthEstcCloudRn": cfprFabricEthEstcCloudRn,
       "cfprFabricEthEstcEpTable": cfprFabricEthEstcEpTable,
       "cfprFabricEthEstcEpEntry": cfprFabricEthEstcEpEntry,
       "cfprFabricEthEstcEpInstanceId": cfprFabricEthEstcEpInstanceId,
       "cfprFabricEthEstcEpDn": cfprFabricEthEstcEpDn,
       "cfprFabricEthEstcEpRn": cfprFabricEthEstcEpRn,
       "cfprFabricEthEstcEpAdminSpeed": cfprFabricEthEstcEpAdminSpeed,
       "cfprFabricEthEstcEpAdminState": cfprFabricEthEstcEpAdminState,
       "cfprFabricEthEstcEpAggrPortId": cfprFabricEthEstcEpAggrPortId,
       "cfprFabricEthEstcEpChassisId": cfprFabricEthEstcEpChassisId,
       "cfprFabricEthEstcEpConfigState": cfprFabricEthEstcEpConfigState,
       "cfprFabricEthEstcEpEpDn": cfprFabricEthEstcEpEpDn,
       "cfprFabricEthEstcEpFlowCtrlPolicy": cfprFabricEthEstcEpFlowCtrlPolicy,
       "cfprFabricEthEstcEpFltAggr": cfprFabricEthEstcEpFltAggr,
       "cfprFabricEthEstcEpIfRole": cfprFabricEthEstcEpIfRole,
       "cfprFabricEthEstcEpIfType": cfprFabricEthEstcEpIfType,
       "cfprFabricEthEstcEpLicGP": cfprFabricEthEstcEpLicGP,
       "cfprFabricEthEstcEpLicState": cfprFabricEthEstcEpLicState,
       "cfprFabricEthEstcEpLocale": cfprFabricEthEstcEpLocale,
       "cfprFabricEthEstcEpName": cfprFabricEthEstcEpName,
       "cfprFabricEthEstcEpNwCtrlPolicyName": cfprFabricEthEstcEpNwCtrlPolicyName,
       "cfprFabricEthEstcEpOperNwCtrlPolicyName": cfprFabricEthEstcEpOperNwCtrlPolicyName,
       "cfprFabricEthEstcEpOperPortMode": cfprFabricEthEstcEpOperPortMode,
       "cfprFabricEthEstcEpOperState": cfprFabricEthEstcEpOperState,
       "cfprFabricEthEstcEpOperStateReason": cfprFabricEthEstcEpOperStateReason,
       "cfprFabricEthEstcEpPeerAggrPortId": cfprFabricEthEstcEpPeerAggrPortId,
       "cfprFabricEthEstcEpPeerChassisId": cfprFabricEthEstcEpPeerChassisId,
       "cfprFabricEthEstcEpPeerDn": cfprFabricEthEstcEpPeerDn,
       "cfprFabricEthEstcEpPeerPortId": cfprFabricEthEstcEpPeerPortId,
       "cfprFabricEthEstcEpPeerSlotId": cfprFabricEthEstcEpPeerSlotId,
       "cfprFabricEthEstcEpPinGroupName": cfprFabricEthEstcEpPinGroupName,
       "cfprFabricEthEstcEpPortId": cfprFabricEthEstcEpPortId,
       "cfprFabricEthEstcEpPortMode": cfprFabricEthEstcEpPortMode,
       "cfprFabricEthEstcEpPrio": cfprFabricEthEstcEpPrio,
       "cfprFabricEthEstcEpSlotId": cfprFabricEthEstcEpSlotId,
       "cfprFabricEthEstcEpSwitchId": cfprFabricEthEstcEpSwitchId,
       "cfprFabricEthEstcEpTransport": cfprFabricEthEstcEpTransport,
       "cfprFabricEthEstcEpType": cfprFabricEthEstcEpType,
       "cfprFabricEthEstcEpUsrLbl": cfprFabricEthEstcEpUsrLbl,
       "cfprFabricEthEstcEpWarnings": cfprFabricEthEstcEpWarnings,
       "cfprFabricEthEstcPcTable": cfprFabricEthEstcPcTable,
       "cfprFabricEthEstcPcEntry": cfprFabricEthEstcPcEntry,
       "cfprFabricEthEstcPcInstanceId": cfprFabricEthEstcPcInstanceId,
       "cfprFabricEthEstcPcDn": cfprFabricEthEstcPcDn,
       "cfprFabricEthEstcPcRn": cfprFabricEthEstcPcRn,
       "cfprFabricEthEstcPcAdminSpeed": cfprFabricEthEstcPcAdminSpeed,
       "cfprFabricEthEstcPcAdminState": cfprFabricEthEstcPcAdminState,
       "cfprFabricEthEstcPcDescr": cfprFabricEthEstcPcDescr,
       "cfprFabricEthEstcPcEpDn": cfprFabricEthEstcPcEpDn,
       "cfprFabricEthEstcPcFlowCtrlPolicy": cfprFabricEthEstcPcFlowCtrlPolicy,
       "cfprFabricEthEstcPcFltAggr": cfprFabricEthEstcPcFltAggr,
       "cfprFabricEthEstcPcIfRole": cfprFabricEthEstcPcIfRole,
       "cfprFabricEthEstcPcIfType": cfprFabricEthEstcPcIfType,
       "cfprFabricEthEstcPcLacpPolicyName": cfprFabricEthEstcPcLacpPolicyName,
       "cfprFabricEthEstcPcLocale": cfprFabricEthEstcPcLocale,
       "cfprFabricEthEstcPcName": cfprFabricEthEstcPcName,
       "cfprFabricEthEstcPcNwCtrlPolicyName": cfprFabricEthEstcPcNwCtrlPolicyName,
       "cfprFabricEthEstcPcOperLacpPolicyName": cfprFabricEthEstcPcOperLacpPolicyName,
       "cfprFabricEthEstcPcOperNwCtrlPolicyName": cfprFabricEthEstcPcOperNwCtrlPolicyName,
       "cfprFabricEthEstcPcOperSpeed": cfprFabricEthEstcPcOperSpeed,
       "cfprFabricEthEstcPcOperState": cfprFabricEthEstcPcOperState,
       "cfprFabricEthEstcPcPeerDn": cfprFabricEthEstcPcPeerDn,
       "cfprFabricEthEstcPcPinGroupName": cfprFabricEthEstcPcPinGroupName,
       "cfprFabricEthEstcPcPortId": cfprFabricEthEstcPcPortId,
       "cfprFabricEthEstcPcPortMode": cfprFabricEthEstcPcPortMode,
       "cfprFabricEthEstcPcPrio": cfprFabricEthEstcPcPrio,
       "cfprFabricEthEstcPcProtocol": cfprFabricEthEstcPcProtocol,
       "cfprFabricEthEstcPcStateQual": cfprFabricEthEstcPcStateQual,
       "cfprFabricEthEstcPcSwitchId": cfprFabricEthEstcPcSwitchId,
       "cfprFabricEthEstcPcTransport": cfprFabricEthEstcPcTransport,
       "cfprFabricEthEstcPcType": cfprFabricEthEstcPcType,
       "cfprFabricEthEstcPcWarnings": cfprFabricEthEstcPcWarnings,
       "cfprFabricEthEstcPcEpTable": cfprFabricEthEstcPcEpTable,
       "cfprFabricEthEstcPcEpEntry": cfprFabricEthEstcPcEpEntry,
       "cfprFabricEthEstcPcEpInstanceId": cfprFabricEthEstcPcEpInstanceId,
       "cfprFabricEthEstcPcEpDnData": cfprFabricEthEstcPcEpDnData,
       "cfprFabricEthEstcPcEpRn": cfprFabricEthEstcPcEpRn,
       "cfprFabricEthEstcPcEpAdminSpeed": cfprFabricEthEstcPcEpAdminSpeed,
       "cfprFabricEthEstcPcEpAdminState": cfprFabricEthEstcPcEpAdminState,
       "cfprFabricEthEstcPcEpAggrPortId": cfprFabricEthEstcPcEpAggrPortId,
       "cfprFabricEthEstcPcEpChassisId": cfprFabricEthEstcPcEpChassisId,
       "cfprFabricEthEstcPcEpConfigState": cfprFabricEthEstcPcEpConfigState,
       "cfprFabricEthEstcPcEpEpDn": cfprFabricEthEstcPcEpEpDn,
       "cfprFabricEthEstcPcEpFltAggr": cfprFabricEthEstcPcEpFltAggr,
       "cfprFabricEthEstcPcEpIfRole": cfprFabricEthEstcPcEpIfRole,
       "cfprFabricEthEstcPcEpIfType": cfprFabricEthEstcPcEpIfType,
       "cfprFabricEthEstcPcEpLicGP": cfprFabricEthEstcPcEpLicGP,
       "cfprFabricEthEstcPcEpLicState": cfprFabricEthEstcPcEpLicState,
       "cfprFabricEthEstcPcEpLocale": cfprFabricEthEstcPcEpLocale,
       "cfprFabricEthEstcPcEpMembership": cfprFabricEthEstcPcEpMembership,
       "cfprFabricEthEstcPcEpName": cfprFabricEthEstcPcEpName,
       "cfprFabricEthEstcPcEpOperState": cfprFabricEthEstcPcEpOperState,
       "cfprFabricEthEstcPcEpOperStateReason": cfprFabricEthEstcPcEpOperStateReason,
       "cfprFabricEthEstcPcEpPeerAggrPortId": cfprFabricEthEstcPcEpPeerAggrPortId,
       "cfprFabricEthEstcPcEpPeerChassisId": cfprFabricEthEstcPcEpPeerChassisId,
       "cfprFabricEthEstcPcEpPeerDn": cfprFabricEthEstcPcEpPeerDn,
       "cfprFabricEthEstcPcEpPeerPortId": cfprFabricEthEstcPcEpPeerPortId,
       "cfprFabricEthEstcPcEpPeerSlotId": cfprFabricEthEstcPcEpPeerSlotId,
       "cfprFabricEthEstcPcEpPortId": cfprFabricEthEstcPcEpPortId,
       "cfprFabricEthEstcPcEpSlotId": cfprFabricEthEstcPcEpSlotId,
       "cfprFabricEthEstcPcEpSwitchId": cfprFabricEthEstcPcEpSwitchId,
       "cfprFabricEthEstcPcEpTransport": cfprFabricEthEstcPcEpTransport,
       "cfprFabricEthEstcPcEpType": cfprFabricEthEstcPcEpType,
       "cfprFabricEthEstcPcEpUsrLbl": cfprFabricEthEstcPcEpUsrLbl,
       "cfprFabricEthEstcPcEpWarnings": cfprFabricEthEstcPcEpWarnings,
       "cfprFabricEthLanTable": cfprFabricEthLanTable,
       "cfprFabricEthLanEntry": cfprFabricEthLanEntry,
       "cfprFabricEthLanInstanceId": cfprFabricEthLanInstanceId,
       "cfprFabricEthLanDn": cfprFabricEthLanDn,
       "cfprFabricEthLanRn": cfprFabricEthLanRn,
       "cfprFabricEthLanId": cfprFabricEthLanId,
       "cfprFabricEthLanLocale": cfprFabricEthLanLocale,
       "cfprFabricEthLanName": cfprFabricEthLanName,
       "cfprFabricEthLanTransport": cfprFabricEthLanTransport,
       "cfprFabricEthLanType": cfprFabricEthLanType,
       "cfprFabricEthLanEpTable": cfprFabricEthLanEpTable,
       "cfprFabricEthLanEpEntry": cfprFabricEthLanEpEntry,
       "cfprFabricEthLanEpInstanceId": cfprFabricEthLanEpInstanceId,
       "cfprFabricEthLanEpDn": cfprFabricEthLanEpDn,
       "cfprFabricEthLanEpRn": cfprFabricEthLanEpRn,
       "cfprFabricEthLanEpAdminSpeed": cfprFabricEthLanEpAdminSpeed,
       "cfprFabricEthLanEpAdminState": cfprFabricEthLanEpAdminState,
       "cfprFabricEthLanEpAggrPortId": cfprFabricEthLanEpAggrPortId,
       "cfprFabricEthLanEpChassisId": cfprFabricEthLanEpChassisId,
       "cfprFabricEthLanEpDtagVlan": cfprFabricEthLanEpDtagVlan,
       "cfprFabricEthLanEpEpDn": cfprFabricEthLanEpEpDn,
       "cfprFabricEthLanEpEthLinkProfileName": cfprFabricEthLanEpEthLinkProfileName,
       "cfprFabricEthLanEpFlowCtrlPolicy": cfprFabricEthLanEpFlowCtrlPolicy,
       "cfprFabricEthLanEpFltAggr": cfprFabricEthLanEpFltAggr,
       "cfprFabricEthLanEpIfRole": cfprFabricEthLanEpIfRole,
       "cfprFabricEthLanEpIfType": cfprFabricEthLanEpIfType,
       "cfprFabricEthLanEpLicGP": cfprFabricEthLanEpLicGP,
       "cfprFabricEthLanEpLicState": cfprFabricEthLanEpLicState,
       "cfprFabricEthLanEpLocale": cfprFabricEthLanEpLocale,
       "cfprFabricEthLanEpName": cfprFabricEthLanEpName,
       "cfprFabricEthLanEpOperEthLinkProfileName": cfprFabricEthLanEpOperEthLinkProfileName,
       "cfprFabricEthLanEpOperState": cfprFabricEthLanEpOperState,
       "cfprFabricEthLanEpOperStateReason": cfprFabricEthLanEpOperStateReason,
       "cfprFabricEthLanEpOverlappingVlans": cfprFabricEthLanEpOverlappingVlans,
       "cfprFabricEthLanEpPeerAggrPortId": cfprFabricEthLanEpPeerAggrPortId,
       "cfprFabricEthLanEpPeerChassisId": cfprFabricEthLanEpPeerChassisId,
       "cfprFabricEthLanEpPeerDn": cfprFabricEthLanEpPeerDn,
       "cfprFabricEthLanEpPeerPortId": cfprFabricEthLanEpPeerPortId,
       "cfprFabricEthLanEpPeerSlotId": cfprFabricEthLanEpPeerSlotId,
       "cfprFabricEthLanEpPortId": cfprFabricEthLanEpPortId,
       "cfprFabricEthLanEpSlotId": cfprFabricEthLanEpSlotId,
       "cfprFabricEthLanEpSsaPortType": cfprFabricEthLanEpSsaPortType,
       "cfprFabricEthLanEpSsaVlanId": cfprFabricEthLanEpSsaVlanId,
       "cfprFabricEthLanEpSwitchId": cfprFabricEthLanEpSwitchId,
       "cfprFabricEthLanEpTransport": cfprFabricEthLanEpTransport,
       "cfprFabricEthLanEpType": cfprFabricEthLanEpType,
       "cfprFabricEthLanEpUdldOperState": cfprFabricEthLanEpUdldOperState,
       "cfprFabricEthLanEpUsrLbl": cfprFabricEthLanEpUsrLbl,
       "cfprFabricEthLanEpVlanStatus": cfprFabricEthLanEpVlanStatus,
       "cfprFabricEthLanEpWarnings": cfprFabricEthLanEpWarnings,
       "cfprFabricEthLanEpAdminDuplex": cfprFabricEthLanEpAdminDuplex,
       "cfprFabricEthLanEpAllowSharing": cfprFabricEthLanEpAllowSharing,
       "cfprFabricEthLanEpAllowedVlan": cfprFabricEthLanEpAllowedVlan,
       "cfprFabricEthLanEpAutoNeg": cfprFabricEthLanEpAutoNeg,
       "cfprFabricEthLanEpDescr": cfprFabricEthLanEpDescr,
       "cfprFabricEthLanEpHashAlg": cfprFabricEthLanEpHashAlg,
       "cfprFabricEthLanEpInlinePeerDn": cfprFabricEthLanEpInlinePeerDn,
       "cfprFabricEthLanEpInlinePeerName": cfprFabricEthLanEpInlinePeerName,
       "cfprFabricEthLanEpInlineState": cfprFabricEthLanEpInlineState,
       "cfprFabricEthLanEpQosPrio": cfprFabricEthLanEpQosPrio,
       "cfprFabricEthLanEpSpeedCap": cfprFabricEthLanEpSpeedCap,
       "cfprFabricEthLanEpNwCtrlPolicyName": cfprFabricEthLanEpNwCtrlPolicyName,
       "cfprFabricEthLanEpOperNwCtrlPolicyName": cfprFabricEthLanEpOperNwCtrlPolicyName,
       "cfprFabricEthLanEpAllowAneg": cfprFabricEthLanEpAllowAneg,
       "cfprFabricEthLanEpDebounceTime": cfprFabricEthLanEpDebounceTime,
       "cfprFabricEthLanEpLastSvcStateDownReason": cfprFabricEthLanEpLastSvcStateDownReason,
       "cfprFabricEthLanEpServiceState": cfprFabricEthLanEpServiceState,
       "cfprFabricEthLanPcTable": cfprFabricEthLanPcTable,
       "cfprFabricEthLanPcEntry": cfprFabricEthLanPcEntry,
       "cfprFabricEthLanPcInstanceId": cfprFabricEthLanPcInstanceId,
       "cfprFabricEthLanPcDn": cfprFabricEthLanPcDn,
       "cfprFabricEthLanPcRn": cfprFabricEthLanPcRn,
       "cfprFabricEthLanPcAdminSpeed": cfprFabricEthLanPcAdminSpeed,
       "cfprFabricEthLanPcAdminState": cfprFabricEthLanPcAdminState,
       "cfprFabricEthLanPcBandwidth": cfprFabricEthLanPcBandwidth,
       "cfprFabricEthLanPcClusterName": cfprFabricEthLanPcClusterName,
       "cfprFabricEthLanPcDescr": cfprFabricEthLanPcDescr,
       "cfprFabricEthLanPcDtagVlan": cfprFabricEthLanPcDtagVlan,
       "cfprFabricEthLanPcEpDn": cfprFabricEthLanPcEpDn,
       "cfprFabricEthLanPcFlowCtrlPolicy": cfprFabricEthLanPcFlowCtrlPolicy,
       "cfprFabricEthLanPcFltAggr": cfprFabricEthLanPcFltAggr,
       "cfprFabricEthLanPcIfRole": cfprFabricEthLanPcIfRole,
       "cfprFabricEthLanPcIfType": cfprFabricEthLanPcIfType,
       "cfprFabricEthLanPcLacpPolicyName": cfprFabricEthLanPcLacpPolicyName,
       "cfprFabricEthLanPcLocale": cfprFabricEthLanPcLocale,
       "cfprFabricEthLanPcName": cfprFabricEthLanPcName,
       "cfprFabricEthLanPcOperLacpPolicyName": cfprFabricEthLanPcOperLacpPolicyName,
       "cfprFabricEthLanPcOperSpeed": cfprFabricEthLanPcOperSpeed,
       "cfprFabricEthLanPcOperState": cfprFabricEthLanPcOperState,
       "cfprFabricEthLanPcOverlappingVlans": cfprFabricEthLanPcOverlappingVlans,
       "cfprFabricEthLanPcPeerDn": cfprFabricEthLanPcPeerDn,
       "cfprFabricEthLanPcPortId": cfprFabricEthLanPcPortId,
       "cfprFabricEthLanPcSpannedCluster": cfprFabricEthLanPcSpannedCluster,
       "cfprFabricEthLanPcSsaPortType": cfprFabricEthLanPcSsaPortType,
       "cfprFabricEthLanPcSsaVlanId": cfprFabricEthLanPcSsaVlanId,
       "cfprFabricEthLanPcStateQual": cfprFabricEthLanPcStateQual,
       "cfprFabricEthLanPcSwitchId": cfprFabricEthLanPcSwitchId,
       "cfprFabricEthLanPcTransport": cfprFabricEthLanPcTransport,
       "cfprFabricEthLanPcType": cfprFabricEthLanPcType,
       "cfprFabricEthLanPcVlanStatus": cfprFabricEthLanPcVlanStatus,
       "cfprFabricEthLanPcWarnings": cfprFabricEthLanPcWarnings,
       "cfprFabricEthLanPcCluChassisId": cfprFabricEthLanPcCluChassisId,
       "cfprFabricEthLanPcLacpDetach": cfprFabricEthLanPcLacpDetach,
       "cfprFabricEthLanPcAdminDuplex": cfprFabricEthLanPcAdminDuplex,
       "cfprFabricEthLanPcAllowSharing": cfprFabricEthLanPcAllowSharing,
       "cfprFabricEthLanPcAllowedVlan": cfprFabricEthLanPcAllowedVlan,
       "cfprFabricEthLanPcAutoNeg": cfprFabricEthLanPcAutoNeg,
       "cfprFabricEthLanPcHashAlg": cfprFabricEthLanPcHashAlg,
       "cfprFabricEthLanPcInlinePeerDn": cfprFabricEthLanPcInlinePeerDn,
       "cfprFabricEthLanPcInlinePeerName": cfprFabricEthLanPcInlinePeerName,
       "cfprFabricEthLanPcInlineState": cfprFabricEthLanPcInlineState,
       "cfprFabricEthLanPcLacpMode": cfprFabricEthLanPcLacpMode,
       "cfprFabricEthLanPcPcMode": cfprFabricEthLanPcPcMode,
       "cfprFabricEthLanPcPcModeState": cfprFabricEthLanPcPcModeState,
       "cfprFabricEthLanPcQosPrio": cfprFabricEthLanPcQosPrio,
       "cfprFabricEthLanPcSpeedCap": cfprFabricEthLanPcSpeedCap,
       "cfprFabricEthLanPcNwCtrlPolicyName": cfprFabricEthLanPcNwCtrlPolicyName,
       "cfprFabricEthLanPcOperNwCtrlPolicyName": cfprFabricEthLanPcOperNwCtrlPolicyName,
       "cfprFabricEthLanPcLastSvcStateDownReason": cfprFabricEthLanPcLastSvcStateDownReason,
       "cfprFabricEthLanPcServiceState": cfprFabricEthLanPcServiceState,
       "cfprFabricEthLanPcEpTable": cfprFabricEthLanPcEpTable,
       "cfprFabricEthLanPcEpEntry": cfprFabricEthLanPcEpEntry,
       "cfprFabricEthLanPcEpInstanceId": cfprFabricEthLanPcEpInstanceId,
       "cfprFabricEthLanPcEpDnData": cfprFabricEthLanPcEpDnData,
       "cfprFabricEthLanPcEpRn": cfprFabricEthLanPcEpRn,
       "cfprFabricEthLanPcEpAdminState": cfprFabricEthLanPcEpAdminState,
       "cfprFabricEthLanPcEpAggrPortId": cfprFabricEthLanPcEpAggrPortId,
       "cfprFabricEthLanPcEpChassisId": cfprFabricEthLanPcEpChassisId,
       "cfprFabricEthLanPcEpEpDn": cfprFabricEthLanPcEpEpDn,
       "cfprFabricEthLanPcEpEthLinkProfileName": cfprFabricEthLanPcEpEthLinkProfileName,
       "cfprFabricEthLanPcEpFltAggr": cfprFabricEthLanPcEpFltAggr,
       "cfprFabricEthLanPcEpIfRole": cfprFabricEthLanPcEpIfRole,
       "cfprFabricEthLanPcEpIfType": cfprFabricEthLanPcEpIfType,
       "cfprFabricEthLanPcEpLicGP": cfprFabricEthLanPcEpLicGP,
       "cfprFabricEthLanPcEpLicState": cfprFabricEthLanPcEpLicState,
       "cfprFabricEthLanPcEpLocale": cfprFabricEthLanPcEpLocale,
       "cfprFabricEthLanPcEpMembership": cfprFabricEthLanPcEpMembership,
       "cfprFabricEthLanPcEpName": cfprFabricEthLanPcEpName,
       "cfprFabricEthLanPcEpOperEthLinkProfileName": cfprFabricEthLanPcEpOperEthLinkProfileName,
       "cfprFabricEthLanPcEpOperState": cfprFabricEthLanPcEpOperState,
       "cfprFabricEthLanPcEpOperStateReason": cfprFabricEthLanPcEpOperStateReason,
       "cfprFabricEthLanPcEpPeerAggrPortId": cfprFabricEthLanPcEpPeerAggrPortId,
       "cfprFabricEthLanPcEpPeerChassisId": cfprFabricEthLanPcEpPeerChassisId,
       "cfprFabricEthLanPcEpPeerDn": cfprFabricEthLanPcEpPeerDn,
       "cfprFabricEthLanPcEpPeerPortId": cfprFabricEthLanPcEpPeerPortId,
       "cfprFabricEthLanPcEpPeerSlotId": cfprFabricEthLanPcEpPeerSlotId,
       "cfprFabricEthLanPcEpPortId": cfprFabricEthLanPcEpPortId,
       "cfprFabricEthLanPcEpSlotId": cfprFabricEthLanPcEpSlotId,
       "cfprFabricEthLanPcEpSwitchId": cfprFabricEthLanPcEpSwitchId,
       "cfprFabricEthLanPcEpTransport": cfprFabricEthLanPcEpTransport,
       "cfprFabricEthLanPcEpType": cfprFabricEthLanPcEpType,
       "cfprFabricEthLanPcEpUdldOperState": cfprFabricEthLanPcEpUdldOperState,
       "cfprFabricEthLanPcEpWarnings": cfprFabricEthLanPcEpWarnings,
       "cfprFabricEthLanPcEpDescr": cfprFabricEthLanPcEpDescr,
       "cfprFabricEthLanPcEpSpeedCap": cfprFabricEthLanPcEpSpeedCap,
       "cfprFabricEthLinkProfileTable": cfprFabricEthLinkProfileTable,
       "cfprFabricEthLinkProfileEntry": cfprFabricEthLinkProfileEntry,
       "cfprFabricEthLinkProfileInstanceId": cfprFabricEthLinkProfileInstanceId,
       "cfprFabricEthLinkProfileDn": cfprFabricEthLinkProfileDn,
       "cfprFabricEthLinkProfileRn": cfprFabricEthLinkProfileRn,
       "cfprFabricEthLinkProfileCdpLinkPolicyName": cfprFabricEthLinkProfileCdpLinkPolicyName,
       "cfprFabricEthLinkProfileDescr": cfprFabricEthLinkProfileDescr,
       "cfprFabricEthLinkProfileIntId": cfprFabricEthLinkProfileIntId,
       "cfprFabricEthLinkProfileName": cfprFabricEthLinkProfileName,
       "cfprFabricEthLinkProfileOperCdpLinkPolicyName": cfprFabricEthLinkProfileOperCdpLinkPolicyName,
       "cfprFabricEthLinkProfileOperUdldLinkPolicyName": cfprFabricEthLinkProfileOperUdldLinkPolicyName,
       "cfprFabricEthLinkProfilePolicyLevel": cfprFabricEthLinkProfilePolicyLevel,
       "cfprFabricEthLinkProfilePolicyOwner": cfprFabricEthLinkProfilePolicyOwner,
       "cfprFabricEthLinkProfileUdldLinkPolicyName": cfprFabricEthLinkProfileUdldLinkPolicyName,
       "cfprFabricEthMonTable": cfprFabricEthMonTable,
       "cfprFabricEthMonEntry": cfprFabricEthMonEntry,
       "cfprFabricEthMonInstanceId": cfprFabricEthMonInstanceId,
       "cfprFabricEthMonDn": cfprFabricEthMonDn,
       "cfprFabricEthMonRn": cfprFabricEthMonRn,
       "cfprFabricEthMonAdminState": cfprFabricEthMonAdminState,
       "cfprFabricEthMonConfigFailReason": cfprFabricEthMonConfigFailReason,
       "cfprFabricEthMonId": cfprFabricEthMonId,
       "cfprFabricEthMonIsConfigSuccess": cfprFabricEthMonIsConfigSuccess,
       "cfprFabricEthMonLocale": cfprFabricEthMonLocale,
       "cfprFabricEthMonName": cfprFabricEthMonName,
       "cfprFabricEthMonOperState": cfprFabricEthMonOperState,
       "cfprFabricEthMonOperStateReason": cfprFabricEthMonOperStateReason,
       "cfprFabricEthMonPeerDn": cfprFabricEthMonPeerDn,
       "cfprFabricEthMonSession": cfprFabricEthMonSession,
       "cfprFabricEthMonTransport": cfprFabricEthMonTransport,
       "cfprFabricEthMonType": cfprFabricEthMonType,
       "cfprFabricEthMonDestEpTable": cfprFabricEthMonDestEpTable,
       "cfprFabricEthMonDestEpEntry": cfprFabricEthMonDestEpEntry,
       "cfprFabricEthMonDestEpInstanceId": cfprFabricEthMonDestEpInstanceId,
       "cfprFabricEthMonDestEpDn": cfprFabricEthMonDestEpDn,
       "cfprFabricEthMonDestEpRn": cfprFabricEthMonDestEpRn,
       "cfprFabricEthMonDestEpAdminSpeed": cfprFabricEthMonDestEpAdminSpeed,
       "cfprFabricEthMonDestEpAdminState": cfprFabricEthMonDestEpAdminState,
       "cfprFabricEthMonDestEpAggrPortId": cfprFabricEthMonDestEpAggrPortId,
       "cfprFabricEthMonDestEpChassisId": cfprFabricEthMonDestEpChassisId,
       "cfprFabricEthMonDestEpEpDn": cfprFabricEthMonDestEpEpDn,
       "cfprFabricEthMonDestEpFltAggr": cfprFabricEthMonDestEpFltAggr,
       "cfprFabricEthMonDestEpIfRole": cfprFabricEthMonDestEpIfRole,
       "cfprFabricEthMonDestEpIfType": cfprFabricEthMonDestEpIfType,
       "cfprFabricEthMonDestEpLicGP": cfprFabricEthMonDestEpLicGP,
       "cfprFabricEthMonDestEpLicState": cfprFabricEthMonDestEpLicState,
       "cfprFabricEthMonDestEpLocale": cfprFabricEthMonDestEpLocale,
       "cfprFabricEthMonDestEpName": cfprFabricEthMonDestEpName,
       "cfprFabricEthMonDestEpOperState": cfprFabricEthMonDestEpOperState,
       "cfprFabricEthMonDestEpOperStateReason": cfprFabricEthMonDestEpOperStateReason,
       "cfprFabricEthMonDestEpPeerAggrPortId": cfprFabricEthMonDestEpPeerAggrPortId,
       "cfprFabricEthMonDestEpPeerChassisId": cfprFabricEthMonDestEpPeerChassisId,
       "cfprFabricEthMonDestEpPeerDn": cfprFabricEthMonDestEpPeerDn,
       "cfprFabricEthMonDestEpPeerPortId": cfprFabricEthMonDestEpPeerPortId,
       "cfprFabricEthMonDestEpPeerSlotId": cfprFabricEthMonDestEpPeerSlotId,
       "cfprFabricEthMonDestEpPortId": cfprFabricEthMonDestEpPortId,
       "cfprFabricEthMonDestEpSlotId": cfprFabricEthMonDestEpSlotId,
       "cfprFabricEthMonDestEpSwitchId": cfprFabricEthMonDestEpSwitchId,
       "cfprFabricEthMonDestEpTransport": cfprFabricEthMonDestEpTransport,
       "cfprFabricEthMonDestEpType": cfprFabricEthMonDestEpType,
       "cfprFabricEthMonDestEpWarnings": cfprFabricEthMonDestEpWarnings,
       "cfprFabricEthMonFiltEpTable": cfprFabricEthMonFiltEpTable,
       "cfprFabricEthMonFiltEpEntry": cfprFabricEthMonFiltEpEntry,
       "cfprFabricEthMonFiltEpInstanceId": cfprFabricEthMonFiltEpInstanceId,
       "cfprFabricEthMonFiltEpDn": cfprFabricEthMonFiltEpDn,
       "cfprFabricEthMonFiltEpRn": cfprFabricEthMonFiltEpRn,
       "cfprFabricEthMonFiltEpName": cfprFabricEthMonFiltEpName,
       "cfprFabricEthMonFiltEpSession": cfprFabricEthMonFiltEpSession,
       "cfprFabricEthMonFiltEpType": cfprFabricEthMonFiltEpType,
       "cfprFabricEthMonFiltRefTable": cfprFabricEthMonFiltRefTable,
       "cfprFabricEthMonFiltRefEntry": cfprFabricEthMonFiltRefEntry,
       "cfprFabricEthMonFiltRefInstanceId": cfprFabricEthMonFiltRefInstanceId,
       "cfprFabricEthMonFiltRefDn": cfprFabricEthMonFiltRefDn,
       "cfprFabricEthMonFiltRefRn": cfprFabricEthMonFiltRefRn,
       "cfprFabricEthMonFiltRefSrcFiltDn": cfprFabricEthMonFiltRefSrcFiltDn,
       "cfprFabricEthMonFiltRefType": cfprFabricEthMonFiltRefType,
       "cfprFabricEthMonLanTable": cfprFabricEthMonLanTable,
       "cfprFabricEthMonLanEntry": cfprFabricEthMonLanEntry,
       "cfprFabricEthMonLanInstanceId": cfprFabricEthMonLanInstanceId,
       "cfprFabricEthMonLanDn": cfprFabricEthMonLanDn,
       "cfprFabricEthMonLanRn": cfprFabricEthMonLanRn,
       "cfprFabricEthMonLanId": cfprFabricEthMonLanId,
       "cfprFabricEthMonLanLocale": cfprFabricEthMonLanLocale,
       "cfprFabricEthMonLanName": cfprFabricEthMonLanName,
       "cfprFabricEthMonLanTransport": cfprFabricEthMonLanTransport,
       "cfprFabricEthMonLanType": cfprFabricEthMonLanType,
       "cfprFabricEthMonSrcEpTable": cfprFabricEthMonSrcEpTable,
       "cfprFabricEthMonSrcEpEntry": cfprFabricEthMonSrcEpEntry,
       "cfprFabricEthMonSrcEpInstanceId": cfprFabricEthMonSrcEpInstanceId,
       "cfprFabricEthMonSrcEpDn": cfprFabricEthMonSrcEpDn,
       "cfprFabricEthMonSrcEpRn": cfprFabricEthMonSrcEpRn,
       "cfprFabricEthMonSrcEpDirection": cfprFabricEthMonSrcEpDirection,
       "cfprFabricEthMonSrcEpName": cfprFabricEthMonSrcEpName,
       "cfprFabricEthMonSrcEpSession": cfprFabricEthMonSrcEpSession,
       "cfprFabricEthMonSrcEpTransport": cfprFabricEthMonSrcEpTransport,
       "cfprFabricEthMonSrcEpType": cfprFabricEthMonSrcEpType,
       "cfprFabricEthMonSrcRefTable": cfprFabricEthMonSrcRefTable,
       "cfprFabricEthMonSrcRefEntry": cfprFabricEthMonSrcRefEntry,
       "cfprFabricEthMonSrcRefInstanceId": cfprFabricEthMonSrcRefInstanceId,
       "cfprFabricEthMonSrcRefDn": cfprFabricEthMonSrcRefDn,
       "cfprFabricEthMonSrcRefRn": cfprFabricEthMonSrcRefRn,
       "cfprFabricEthMonSrcRefId": cfprFabricEthMonSrcRefId,
       "cfprFabricEthMonSrcRefSourceDn": cfprFabricEthMonSrcRefSourceDn,
       "cfprFabricEthMonSrcRefSourceType": cfprFabricEthMonSrcRefSourceType,
       "cfprFabricEthMonSrcRefType": cfprFabricEthMonSrcRefType,
       "cfprFabricEthTargetEpTable": cfprFabricEthTargetEpTable,
       "cfprFabricEthTargetEpEntry": cfprFabricEthTargetEpEntry,
       "cfprFabricEthTargetEpInstanceId": cfprFabricEthTargetEpInstanceId,
       "cfprFabricEthTargetEpDn": cfprFabricEthTargetEpDn,
       "cfprFabricEthTargetEpRn": cfprFabricEthTargetEpRn,
       "cfprFabricEthTargetEpAdminState": cfprFabricEthTargetEpAdminState,
       "cfprFabricEthTargetEpAggrPortId": cfprFabricEthTargetEpAggrPortId,
       "cfprFabricEthTargetEpChassisId": cfprFabricEthTargetEpChassisId,
       "cfprFabricEthTargetEpEpDn": cfprFabricEthTargetEpEpDn,
       "cfprFabricEthTargetEpFltAggr": cfprFabricEthTargetEpFltAggr,
       "cfprFabricEthTargetEpIfRole": cfprFabricEthTargetEpIfRole,
       "cfprFabricEthTargetEpIfType": cfprFabricEthTargetEpIfType,
       "cfprFabricEthTargetEpLicGP": cfprFabricEthTargetEpLicGP,
       "cfprFabricEthTargetEpLicState": cfprFabricEthTargetEpLicState,
       "cfprFabricEthTargetEpLocale": cfprFabricEthTargetEpLocale,
       "cfprFabricEthTargetEpMacAddress": cfprFabricEthTargetEpMacAddress,
       "cfprFabricEthTargetEpName": cfprFabricEthTargetEpName,
       "cfprFabricEthTargetEpOperState": cfprFabricEthTargetEpOperState,
       "cfprFabricEthTargetEpOperStateReason": cfprFabricEthTargetEpOperStateReason,
       "cfprFabricEthTargetEpPeerAggrPortId": cfprFabricEthTargetEpPeerAggrPortId,
       "cfprFabricEthTargetEpPeerChassisId": cfprFabricEthTargetEpPeerChassisId,
       "cfprFabricEthTargetEpPeerDn": cfprFabricEthTargetEpPeerDn,
       "cfprFabricEthTargetEpPeerPortId": cfprFabricEthTargetEpPeerPortId,
       "cfprFabricEthTargetEpPeerSlotId": cfprFabricEthTargetEpPeerSlotId,
       "cfprFabricEthTargetEpPortId": cfprFabricEthTargetEpPortId,
       "cfprFabricEthTargetEpSlotId": cfprFabricEthTargetEpSlotId,
       "cfprFabricEthTargetEpSwitchId": cfprFabricEthTargetEpSwitchId,
       "cfprFabricEthTargetEpTransport": cfprFabricEthTargetEpTransport,
       "cfprFabricEthTargetEpType": cfprFabricEthTargetEpType,
       "cfprFabricEthTargetEpWarnings": cfprFabricEthTargetEpWarnings,
       "cfprFabricEthVlanPcTable": cfprFabricEthVlanPcTable,
       "cfprFabricEthVlanPcEntry": cfprFabricEthVlanPcEntry,
       "cfprFabricEthVlanPcInstanceId": cfprFabricEthVlanPcInstanceId,
       "cfprFabricEthVlanPcDn": cfprFabricEthVlanPcDn,
       "cfprFabricEthVlanPcRn": cfprFabricEthVlanPcRn,
       "cfprFabricEthVlanPcAdminSpeed": cfprFabricEthVlanPcAdminSpeed,
       "cfprFabricEthVlanPcAdminState": cfprFabricEthVlanPcAdminState,
       "cfprFabricEthVlanPcDescr": cfprFabricEthVlanPcDescr,
       "cfprFabricEthVlanPcEpDn": cfprFabricEthVlanPcEpDn,
       "cfprFabricEthVlanPcFltAggr": cfprFabricEthVlanPcFltAggr,
       "cfprFabricEthVlanPcIfRole": cfprFabricEthVlanPcIfRole,
       "cfprFabricEthVlanPcIfType": cfprFabricEthVlanPcIfType,
       "cfprFabricEthVlanPcIsNative": cfprFabricEthVlanPcIsNative,
       "cfprFabricEthVlanPcLocale": cfprFabricEthVlanPcLocale,
       "cfprFabricEthVlanPcName": cfprFabricEthVlanPcName,
       "cfprFabricEthVlanPcOperSpeed": cfprFabricEthVlanPcOperSpeed,
       "cfprFabricEthVlanPcOperState": cfprFabricEthVlanPcOperState,
       "cfprFabricEthVlanPcPeerDn": cfprFabricEthVlanPcPeerDn,
       "cfprFabricEthVlanPcPortId": cfprFabricEthVlanPcPortId,
       "cfprFabricEthVlanPcStateQual": cfprFabricEthVlanPcStateQual,
       "cfprFabricEthVlanPcSwitchId": cfprFabricEthVlanPcSwitchId,
       "cfprFabricEthVlanPcTransport": cfprFabricEthVlanPcTransport,
       "cfprFabricEthVlanPcType": cfprFabricEthVlanPcType,
       "cfprFabricEthVlanPcWarnings": cfprFabricEthVlanPcWarnings,
       "cfprFabricEthVlanPortEpTable": cfprFabricEthVlanPortEpTable,
       "cfprFabricEthVlanPortEpEntry": cfprFabricEthVlanPortEpEntry,
       "cfprFabricEthVlanPortEpInstanceId": cfprFabricEthVlanPortEpInstanceId,
       "cfprFabricEthVlanPortEpDn": cfprFabricEthVlanPortEpDn,
       "cfprFabricEthVlanPortEpRn": cfprFabricEthVlanPortEpRn,
       "cfprFabricEthVlanPortEpAdminState": cfprFabricEthVlanPortEpAdminState,
       "cfprFabricEthVlanPortEpAggrPortId": cfprFabricEthVlanPortEpAggrPortId,
       "cfprFabricEthVlanPortEpChassisId": cfprFabricEthVlanPortEpChassisId,
       "cfprFabricEthVlanPortEpEpDn": cfprFabricEthVlanPortEpEpDn,
       "cfprFabricEthVlanPortEpFltAggr": cfprFabricEthVlanPortEpFltAggr,
       "cfprFabricEthVlanPortEpIfRole": cfprFabricEthVlanPortEpIfRole,
       "cfprFabricEthVlanPortEpIfType": cfprFabricEthVlanPortEpIfType,
       "cfprFabricEthVlanPortEpIsNative": cfprFabricEthVlanPortEpIsNative,
       "cfprFabricEthVlanPortEpLicGP": cfprFabricEthVlanPortEpLicGP,
       "cfprFabricEthVlanPortEpLicState": cfprFabricEthVlanPortEpLicState,
       "cfprFabricEthVlanPortEpLocale": cfprFabricEthVlanPortEpLocale,
       "cfprFabricEthVlanPortEpName": cfprFabricEthVlanPortEpName,
       "cfprFabricEthVlanPortEpOperState": cfprFabricEthVlanPortEpOperState,
       "cfprFabricEthVlanPortEpOperStateReason": cfprFabricEthVlanPortEpOperStateReason,
       "cfprFabricEthVlanPortEpPeerAggrPortId": cfprFabricEthVlanPortEpPeerAggrPortId,
       "cfprFabricEthVlanPortEpPeerChassisId": cfprFabricEthVlanPortEpPeerChassisId,
       "cfprFabricEthVlanPortEpPeerDn": cfprFabricEthVlanPortEpPeerDn,
       "cfprFabricEthVlanPortEpPeerPortId": cfprFabricEthVlanPortEpPeerPortId,
       "cfprFabricEthVlanPortEpPeerSlotId": cfprFabricEthVlanPortEpPeerSlotId,
       "cfprFabricEthVlanPortEpPortId": cfprFabricEthVlanPortEpPortId,
       "cfprFabricEthVlanPortEpSlotId": cfprFabricEthVlanPortEpSlotId,
       "cfprFabricEthVlanPortEpSwitchId": cfprFabricEthVlanPortEpSwitchId,
       "cfprFabricEthVlanPortEpTransport": cfprFabricEthVlanPortEpTransport,
       "cfprFabricEthVlanPortEpType": cfprFabricEthVlanPortEpType,
       "cfprFabricEthVlanPortEpWarnings": cfprFabricEthVlanPortEpWarnings,
       "cfprFabricFcSanTable": cfprFabricFcSanTable,
       "cfprFabricFcSanEntry": cfprFabricFcSanEntry,
       "cfprFabricFcSanInstanceId": cfprFabricFcSanInstanceId,
       "cfprFabricFcSanDn": cfprFabricFcSanDn,
       "cfprFabricFcSanRn": cfprFabricFcSanRn,
       "cfprFabricFcSanId": cfprFabricFcSanId,
       "cfprFabricFcSanLocale": cfprFabricFcSanLocale,
       "cfprFabricFcSanName": cfprFabricFcSanName,
       "cfprFabricFcSanTransport": cfprFabricFcSanTransport,
       "cfprFabricFcSanType": cfprFabricFcSanType,
       "cfprFabricFcSanUplinkTrunking": cfprFabricFcSanUplinkTrunking,
       "cfprFabricFcSanEpTable": cfprFabricFcSanEpTable,
       "cfprFabricFcSanEpEntry": cfprFabricFcSanEpEntry,
       "cfprFabricFcSanEpInstanceId": cfprFabricFcSanEpInstanceId,
       "cfprFabricFcSanEpDn": cfprFabricFcSanEpDn,
       "cfprFabricFcSanEpRn": cfprFabricFcSanEpRn,
       "cfprFabricFcSanEpAdminState": cfprFabricFcSanEpAdminState,
       "cfprFabricFcSanEpAggrPortId": cfprFabricFcSanEpAggrPortId,
       "cfprFabricFcSanEpChassisId": cfprFabricFcSanEpChassisId,
       "cfprFabricFcSanEpEpDn": cfprFabricFcSanEpEpDn,
       "cfprFabricFcSanEpFillPattern": cfprFabricFcSanEpFillPattern,
       "cfprFabricFcSanEpFltAggr": cfprFabricFcSanEpFltAggr,
       "cfprFabricFcSanEpIfRole": cfprFabricFcSanEpIfRole,
       "cfprFabricFcSanEpIfType": cfprFabricFcSanEpIfType,
       "cfprFabricFcSanEpLicGP": cfprFabricFcSanEpLicGP,
       "cfprFabricFcSanEpLicState": cfprFabricFcSanEpLicState,
       "cfprFabricFcSanEpLocale": cfprFabricFcSanEpLocale,
       "cfprFabricFcSanEpName": cfprFabricFcSanEpName,
       "cfprFabricFcSanEpOperState": cfprFabricFcSanEpOperState,
       "cfprFabricFcSanEpOperStateReason": cfprFabricFcSanEpOperStateReason,
       "cfprFabricFcSanEpPeerAggrPortId": cfprFabricFcSanEpPeerAggrPortId,
       "cfprFabricFcSanEpPeerChassisId": cfprFabricFcSanEpPeerChassisId,
       "cfprFabricFcSanEpPeerDn": cfprFabricFcSanEpPeerDn,
       "cfprFabricFcSanEpPeerPortId": cfprFabricFcSanEpPeerPortId,
       "cfprFabricFcSanEpPeerSlotId": cfprFabricFcSanEpPeerSlotId,
       "cfprFabricFcSanEpPortId": cfprFabricFcSanEpPortId,
       "cfprFabricFcSanEpSlotId": cfprFabricFcSanEpSlotId,
       "cfprFabricFcSanEpSwitchId": cfprFabricFcSanEpSwitchId,
       "cfprFabricFcSanEpTransport": cfprFabricFcSanEpTransport,
       "cfprFabricFcSanEpType": cfprFabricFcSanEpType,
       "cfprFabricFcSanEpUsrLbl": cfprFabricFcSanEpUsrLbl,
       "cfprFabricFcSanEpWarnings": cfprFabricFcSanEpWarnings,
       "cfprFabricFcSanPcTable": cfprFabricFcSanPcTable,
       "cfprFabricFcSanPcEntry": cfprFabricFcSanPcEntry,
       "cfprFabricFcSanPcInstanceId": cfprFabricFcSanPcInstanceId,
       "cfprFabricFcSanPcDn": cfprFabricFcSanPcDn,
       "cfprFabricFcSanPcRn": cfprFabricFcSanPcRn,
       "cfprFabricFcSanPcAdminSpeed": cfprFabricFcSanPcAdminSpeed,
       "cfprFabricFcSanPcAdminState": cfprFabricFcSanPcAdminState,
       "cfprFabricFcSanPcConfigState": cfprFabricFcSanPcConfigState,
       "cfprFabricFcSanPcConfigStatus": cfprFabricFcSanPcConfigStatus,
       "cfprFabricFcSanPcDescr": cfprFabricFcSanPcDescr,
       "cfprFabricFcSanPcEpDn": cfprFabricFcSanPcEpDn,
       "cfprFabricFcSanPcFltAggr": cfprFabricFcSanPcFltAggr,
       "cfprFabricFcSanPcIfRole": cfprFabricFcSanPcIfRole,
       "cfprFabricFcSanPcIfType": cfprFabricFcSanPcIfType,
       "cfprFabricFcSanPcLocale": cfprFabricFcSanPcLocale,
       "cfprFabricFcSanPcName": cfprFabricFcSanPcName,
       "cfprFabricFcSanPcOperSpeed": cfprFabricFcSanPcOperSpeed,
       "cfprFabricFcSanPcOperState": cfprFabricFcSanPcOperState,
       "cfprFabricFcSanPcPeerDn": cfprFabricFcSanPcPeerDn,
       "cfprFabricFcSanPcPortId": cfprFabricFcSanPcPortId,
       "cfprFabricFcSanPcStateQual": cfprFabricFcSanPcStateQual,
       "cfprFabricFcSanPcSwitchId": cfprFabricFcSanPcSwitchId,
       "cfprFabricFcSanPcTransport": cfprFabricFcSanPcTransport,
       "cfprFabricFcSanPcType": cfprFabricFcSanPcType,
       "cfprFabricFcSanPcWarnings": cfprFabricFcSanPcWarnings,
       "cfprFabricFcSanPcEpTable": cfprFabricFcSanPcEpTable,
       "cfprFabricFcSanPcEpEntry": cfprFabricFcSanPcEpEntry,
       "cfprFabricFcSanPcEpInstanceId": cfprFabricFcSanPcEpInstanceId,
       "cfprFabricFcSanPcEpDnData": cfprFabricFcSanPcEpDnData,
       "cfprFabricFcSanPcEpRn": cfprFabricFcSanPcEpRn,
       "cfprFabricFcSanPcEpAdminSpeed": cfprFabricFcSanPcEpAdminSpeed,
       "cfprFabricFcSanPcEpAdminState": cfprFabricFcSanPcEpAdminState,
       "cfprFabricFcSanPcEpAggrPortId": cfprFabricFcSanPcEpAggrPortId,
       "cfprFabricFcSanPcEpChassisId": cfprFabricFcSanPcEpChassisId,
       "cfprFabricFcSanPcEpEpDn": cfprFabricFcSanPcEpEpDn,
       "cfprFabricFcSanPcEpFillPattern": cfprFabricFcSanPcEpFillPattern,
       "cfprFabricFcSanPcEpFltAggr": cfprFabricFcSanPcEpFltAggr,
       "cfprFabricFcSanPcEpIfRole": cfprFabricFcSanPcEpIfRole,
       "cfprFabricFcSanPcEpIfType": cfprFabricFcSanPcEpIfType,
       "cfprFabricFcSanPcEpLicGP": cfprFabricFcSanPcEpLicGP,
       "cfprFabricFcSanPcEpLicState": cfprFabricFcSanPcEpLicState,
       "cfprFabricFcSanPcEpLocale": cfprFabricFcSanPcEpLocale,
       "cfprFabricFcSanPcEpMembership": cfprFabricFcSanPcEpMembership,
       "cfprFabricFcSanPcEpName": cfprFabricFcSanPcEpName,
       "cfprFabricFcSanPcEpOperState": cfprFabricFcSanPcEpOperState,
       "cfprFabricFcSanPcEpOperStateReason": cfprFabricFcSanPcEpOperStateReason,
       "cfprFabricFcSanPcEpPeerAggrPortId": cfprFabricFcSanPcEpPeerAggrPortId,
       "cfprFabricFcSanPcEpPeerChassisId": cfprFabricFcSanPcEpPeerChassisId,
       "cfprFabricFcSanPcEpPeerDn": cfprFabricFcSanPcEpPeerDn,
       "cfprFabricFcSanPcEpPeerPortId": cfprFabricFcSanPcEpPeerPortId,
       "cfprFabricFcSanPcEpPeerSlotId": cfprFabricFcSanPcEpPeerSlotId,
       "cfprFabricFcSanPcEpPortId": cfprFabricFcSanPcEpPortId,
       "cfprFabricFcSanPcEpSlotId": cfprFabricFcSanPcEpSlotId,
       "cfprFabricFcSanPcEpSwitchId": cfprFabricFcSanPcEpSwitchId,
       "cfprFabricFcSanPcEpTransport": cfprFabricFcSanPcEpTransport,
       "cfprFabricFcSanPcEpType": cfprFabricFcSanPcEpType,
       "cfprFabricFcSanPcEpWarnings": cfprFabricFcSanPcEpWarnings,
       "cfprFabricFcVsanPcTable": cfprFabricFcVsanPcTable,
       "cfprFabricFcVsanPcEntry": cfprFabricFcVsanPcEntry,
       "cfprFabricFcVsanPcInstanceId": cfprFabricFcVsanPcInstanceId,
       "cfprFabricFcVsanPcDn": cfprFabricFcVsanPcDn,
       "cfprFabricFcVsanPcRn": cfprFabricFcVsanPcRn,
       "cfprFabricFcVsanPcAdminState": cfprFabricFcVsanPcAdminState,
       "cfprFabricFcVsanPcDescr": cfprFabricFcVsanPcDescr,
       "cfprFabricFcVsanPcEpDn": cfprFabricFcVsanPcEpDn,
       "cfprFabricFcVsanPcFltAggr": cfprFabricFcVsanPcFltAggr,
       "cfprFabricFcVsanPcIfRole": cfprFabricFcVsanPcIfRole,
       "cfprFabricFcVsanPcIfType": cfprFabricFcVsanPcIfType,
       "cfprFabricFcVsanPcLocale": cfprFabricFcVsanPcLocale,
       "cfprFabricFcVsanPcName": cfprFabricFcVsanPcName,
       "cfprFabricFcVsanPcOperState": cfprFabricFcVsanPcOperState,
       "cfprFabricFcVsanPcPeerDn": cfprFabricFcVsanPcPeerDn,
       "cfprFabricFcVsanPcPortId": cfprFabricFcVsanPcPortId,
       "cfprFabricFcVsanPcStateQual": cfprFabricFcVsanPcStateQual,
       "cfprFabricFcVsanPcSwitchId": cfprFabricFcVsanPcSwitchId,
       "cfprFabricFcVsanPcTransport": cfprFabricFcVsanPcTransport,
       "cfprFabricFcVsanPcType": cfprFabricFcVsanPcType,
       "cfprFabricFcVsanPcWarnings": cfprFabricFcVsanPcWarnings,
       "cfprFabricFcVsanPortEpTable": cfprFabricFcVsanPortEpTable,
       "cfprFabricFcVsanPortEpEntry": cfprFabricFcVsanPortEpEntry,
       "cfprFabricFcVsanPortEpInstanceId": cfprFabricFcVsanPortEpInstanceId,
       "cfprFabricFcVsanPortEpDn": cfprFabricFcVsanPortEpDn,
       "cfprFabricFcVsanPortEpRn": cfprFabricFcVsanPortEpRn,
       "cfprFabricFcVsanPortEpAdminState": cfprFabricFcVsanPortEpAdminState,
       "cfprFabricFcVsanPortEpAggrPortId": cfprFabricFcVsanPortEpAggrPortId,
       "cfprFabricFcVsanPortEpChassisId": cfprFabricFcVsanPortEpChassisId,
       "cfprFabricFcVsanPortEpEpDn": cfprFabricFcVsanPortEpEpDn,
       "cfprFabricFcVsanPortEpFltAggr": cfprFabricFcVsanPortEpFltAggr,
       "cfprFabricFcVsanPortEpIfRole": cfprFabricFcVsanPortEpIfRole,
       "cfprFabricFcVsanPortEpIfType": cfprFabricFcVsanPortEpIfType,
       "cfprFabricFcVsanPortEpLicGP": cfprFabricFcVsanPortEpLicGP,
       "cfprFabricFcVsanPortEpLicState": cfprFabricFcVsanPortEpLicState,
       "cfprFabricFcVsanPortEpLocale": cfprFabricFcVsanPortEpLocale,
       "cfprFabricFcVsanPortEpName": cfprFabricFcVsanPortEpName,
       "cfprFabricFcVsanPortEpOperState": cfprFabricFcVsanPortEpOperState,
       "cfprFabricFcVsanPortEpOperStateReason": cfprFabricFcVsanPortEpOperStateReason,
       "cfprFabricFcVsanPortEpPeerAggrPortId": cfprFabricFcVsanPortEpPeerAggrPortId,
       "cfprFabricFcVsanPortEpPeerChassisId": cfprFabricFcVsanPortEpPeerChassisId,
       "cfprFabricFcVsanPortEpPeerDn": cfprFabricFcVsanPortEpPeerDn,
       "cfprFabricFcVsanPortEpPeerPortId": cfprFabricFcVsanPortEpPeerPortId,
       "cfprFabricFcVsanPortEpPeerSlotId": cfprFabricFcVsanPortEpPeerSlotId,
       "cfprFabricFcVsanPortEpPortId": cfprFabricFcVsanPortEpPortId,
       "cfprFabricFcVsanPortEpSlotId": cfprFabricFcVsanPortEpSlotId,
       "cfprFabricFcVsanPortEpSwitchId": cfprFabricFcVsanPortEpSwitchId,
       "cfprFabricFcVsanPortEpTransport": cfprFabricFcVsanPortEpTransport,
       "cfprFabricFcVsanPortEpType": cfprFabricFcVsanPortEpType,
       "cfprFabricFcVsanPortEpWarnings": cfprFabricFcVsanPortEpWarnings,
       "cfprFabricFcoeSanEpTable": cfprFabricFcoeSanEpTable,
       "cfprFabricFcoeSanEpEntry": cfprFabricFcoeSanEpEntry,
       "cfprFabricFcoeSanEpInstanceId": cfprFabricFcoeSanEpInstanceId,
       "cfprFabricFcoeSanEpDn": cfprFabricFcoeSanEpDn,
       "cfprFabricFcoeSanEpRn": cfprFabricFcoeSanEpRn,
       "cfprFabricFcoeSanEpAdminState": cfprFabricFcoeSanEpAdminState,
       "cfprFabricFcoeSanEpAggrPortId": cfprFabricFcoeSanEpAggrPortId,
       "cfprFabricFcoeSanEpChassisId": cfprFabricFcoeSanEpChassisId,
       "cfprFabricFcoeSanEpConfigState": cfprFabricFcoeSanEpConfigState,
       "cfprFabricFcoeSanEpEpDn": cfprFabricFcoeSanEpEpDn,
       "cfprFabricFcoeSanEpEthLinkProfileName": cfprFabricFcoeSanEpEthLinkProfileName,
       "cfprFabricFcoeSanEpFcoeState": cfprFabricFcoeSanEpFcoeState,
       "cfprFabricFcoeSanEpFcoeStateReason": cfprFabricFcoeSanEpFcoeStateReason,
       "cfprFabricFcoeSanEpFltAggr": cfprFabricFcoeSanEpFltAggr,
       "cfprFabricFcoeSanEpIfRole": cfprFabricFcoeSanEpIfRole,
       "cfprFabricFcoeSanEpIfType": cfprFabricFcoeSanEpIfType,
       "cfprFabricFcoeSanEpLicGP": cfprFabricFcoeSanEpLicGP,
       "cfprFabricFcoeSanEpLicState": cfprFabricFcoeSanEpLicState,
       "cfprFabricFcoeSanEpLocale": cfprFabricFcoeSanEpLocale,
       "cfprFabricFcoeSanEpName": cfprFabricFcoeSanEpName,
       "cfprFabricFcoeSanEpOperEthLinkProfileName": cfprFabricFcoeSanEpOperEthLinkProfileName,
       "cfprFabricFcoeSanEpOperState": cfprFabricFcoeSanEpOperState,
       "cfprFabricFcoeSanEpOperStateReason": cfprFabricFcoeSanEpOperStateReason,
       "cfprFabricFcoeSanEpPeerAggrPortId": cfprFabricFcoeSanEpPeerAggrPortId,
       "cfprFabricFcoeSanEpPeerChassisId": cfprFabricFcoeSanEpPeerChassisId,
       "cfprFabricFcoeSanEpPeerDn": cfprFabricFcoeSanEpPeerDn,
       "cfprFabricFcoeSanEpPeerPortId": cfprFabricFcoeSanEpPeerPortId,
       "cfprFabricFcoeSanEpPeerSlotId": cfprFabricFcoeSanEpPeerSlotId,
       "cfprFabricFcoeSanEpPortId": cfprFabricFcoeSanEpPortId,
       "cfprFabricFcoeSanEpSlotId": cfprFabricFcoeSanEpSlotId,
       "cfprFabricFcoeSanEpSwitchId": cfprFabricFcoeSanEpSwitchId,
       "cfprFabricFcoeSanEpTransport": cfprFabricFcoeSanEpTransport,
       "cfprFabricFcoeSanEpType": cfprFabricFcoeSanEpType,
       "cfprFabricFcoeSanEpUdldOperState": cfprFabricFcoeSanEpUdldOperState,
       "cfprFabricFcoeSanEpUsrLbl": cfprFabricFcoeSanEpUsrLbl,
       "cfprFabricFcoeSanEpWarnings": cfprFabricFcoeSanEpWarnings,
       "cfprFabricFcoeSanPcTable": cfprFabricFcoeSanPcTable,
       "cfprFabricFcoeSanPcEntry": cfprFabricFcoeSanPcEntry,
       "cfprFabricFcoeSanPcInstanceId": cfprFabricFcoeSanPcInstanceId,
       "cfprFabricFcoeSanPcDn": cfprFabricFcoeSanPcDn,
       "cfprFabricFcoeSanPcRn": cfprFabricFcoeSanPcRn,
       "cfprFabricFcoeSanPcAdminState": cfprFabricFcoeSanPcAdminState,
       "cfprFabricFcoeSanPcConfigState": cfprFabricFcoeSanPcConfigState,
       "cfprFabricFcoeSanPcDescr": cfprFabricFcoeSanPcDescr,
       "cfprFabricFcoeSanPcEpDn": cfprFabricFcoeSanPcEpDn,
       "cfprFabricFcoeSanPcFcoeState": cfprFabricFcoeSanPcFcoeState,
       "cfprFabricFcoeSanPcFcoeStateReason": cfprFabricFcoeSanPcFcoeStateReason,
       "cfprFabricFcoeSanPcFltAggr": cfprFabricFcoeSanPcFltAggr,
       "cfprFabricFcoeSanPcIfRole": cfprFabricFcoeSanPcIfRole,
       "cfprFabricFcoeSanPcIfType": cfprFabricFcoeSanPcIfType,
       "cfprFabricFcoeSanPcLacpPolicyName": cfprFabricFcoeSanPcLacpPolicyName,
       "cfprFabricFcoeSanPcLocale": cfprFabricFcoeSanPcLocale,
       "cfprFabricFcoeSanPcName": cfprFabricFcoeSanPcName,
       "cfprFabricFcoeSanPcOperLacpPolicyName": cfprFabricFcoeSanPcOperLacpPolicyName,
       "cfprFabricFcoeSanPcOperState": cfprFabricFcoeSanPcOperState,
       "cfprFabricFcoeSanPcPeerDn": cfprFabricFcoeSanPcPeerDn,
       "cfprFabricFcoeSanPcPortId": cfprFabricFcoeSanPcPortId,
       "cfprFabricFcoeSanPcStateQual": cfprFabricFcoeSanPcStateQual,
       "cfprFabricFcoeSanPcSwitchId": cfprFabricFcoeSanPcSwitchId,
       "cfprFabricFcoeSanPcTransport": cfprFabricFcoeSanPcTransport,
       "cfprFabricFcoeSanPcType": cfprFabricFcoeSanPcType,
       "cfprFabricFcoeSanPcWarnings": cfprFabricFcoeSanPcWarnings,
       "cfprFabricFcoeSanPcEpTable": cfprFabricFcoeSanPcEpTable,
       "cfprFabricFcoeSanPcEpEntry": cfprFabricFcoeSanPcEpEntry,
       "cfprFabricFcoeSanPcEpInstanceId": cfprFabricFcoeSanPcEpInstanceId,
       "cfprFabricFcoeSanPcEpDnData": cfprFabricFcoeSanPcEpDnData,
       "cfprFabricFcoeSanPcEpRn": cfprFabricFcoeSanPcEpRn,
       "cfprFabricFcoeSanPcEpAdminState": cfprFabricFcoeSanPcEpAdminState,
       "cfprFabricFcoeSanPcEpAggrPortId": cfprFabricFcoeSanPcEpAggrPortId,
       "cfprFabricFcoeSanPcEpChassisId": cfprFabricFcoeSanPcEpChassisId,
       "cfprFabricFcoeSanPcEpEpDn": cfprFabricFcoeSanPcEpEpDn,
       "cfprFabricFcoeSanPcEpEthLinkProfileName": cfprFabricFcoeSanPcEpEthLinkProfileName,
       "cfprFabricFcoeSanPcEpFltAggr": cfprFabricFcoeSanPcEpFltAggr,
       "cfprFabricFcoeSanPcEpIfRole": cfprFabricFcoeSanPcEpIfRole,
       "cfprFabricFcoeSanPcEpIfType": cfprFabricFcoeSanPcEpIfType,
       "cfprFabricFcoeSanPcEpLicGP": cfprFabricFcoeSanPcEpLicGP,
       "cfprFabricFcoeSanPcEpLicState": cfprFabricFcoeSanPcEpLicState,
       "cfprFabricFcoeSanPcEpLocale": cfprFabricFcoeSanPcEpLocale,
       "cfprFabricFcoeSanPcEpMembership": cfprFabricFcoeSanPcEpMembership,
       "cfprFabricFcoeSanPcEpName": cfprFabricFcoeSanPcEpName,
       "cfprFabricFcoeSanPcEpOperEthLinkProfileName": cfprFabricFcoeSanPcEpOperEthLinkProfileName,
       "cfprFabricFcoeSanPcEpOperState": cfprFabricFcoeSanPcEpOperState,
       "cfprFabricFcoeSanPcEpOperStateReason": cfprFabricFcoeSanPcEpOperStateReason,
       "cfprFabricFcoeSanPcEpPeerAggrPortId": cfprFabricFcoeSanPcEpPeerAggrPortId,
       "cfprFabricFcoeSanPcEpPeerChassisId": cfprFabricFcoeSanPcEpPeerChassisId,
       "cfprFabricFcoeSanPcEpPeerDn": cfprFabricFcoeSanPcEpPeerDn,
       "cfprFabricFcoeSanPcEpPeerPortId": cfprFabricFcoeSanPcEpPeerPortId,
       "cfprFabricFcoeSanPcEpPeerSlotId": cfprFabricFcoeSanPcEpPeerSlotId,
       "cfprFabricFcoeSanPcEpPortId": cfprFabricFcoeSanPcEpPortId,
       "cfprFabricFcoeSanPcEpSlotId": cfprFabricFcoeSanPcEpSlotId,
       "cfprFabricFcoeSanPcEpSwitchId": cfprFabricFcoeSanPcEpSwitchId,
       "cfprFabricFcoeSanPcEpTransport": cfprFabricFcoeSanPcEpTransport,
       "cfprFabricFcoeSanPcEpType": cfprFabricFcoeSanPcEpType,
       "cfprFabricFcoeSanPcEpUdldOperState": cfprFabricFcoeSanPcEpUdldOperState,
       "cfprFabricFcoeSanPcEpWarnings": cfprFabricFcoeSanPcEpWarnings,
       "cfprFabricFcoeVsanPcTable": cfprFabricFcoeVsanPcTable,
       "cfprFabricFcoeVsanPcEntry": cfprFabricFcoeVsanPcEntry,
       "cfprFabricFcoeVsanPcInstanceId": cfprFabricFcoeVsanPcInstanceId,
       "cfprFabricFcoeVsanPcDn": cfprFabricFcoeVsanPcDn,
       "cfprFabricFcoeVsanPcRn": cfprFabricFcoeVsanPcRn,
       "cfprFabricFcoeVsanPcAdminState": cfprFabricFcoeVsanPcAdminState,
       "cfprFabricFcoeVsanPcDescr": cfprFabricFcoeVsanPcDescr,
       "cfprFabricFcoeVsanPcEpDn": cfprFabricFcoeVsanPcEpDn,
       "cfprFabricFcoeVsanPcFltAggr": cfprFabricFcoeVsanPcFltAggr,
       "cfprFabricFcoeVsanPcIfRole": cfprFabricFcoeVsanPcIfRole,
       "cfprFabricFcoeVsanPcIfType": cfprFabricFcoeVsanPcIfType,
       "cfprFabricFcoeVsanPcLocale": cfprFabricFcoeVsanPcLocale,
       "cfprFabricFcoeVsanPcName": cfprFabricFcoeVsanPcName,
       "cfprFabricFcoeVsanPcOperState": cfprFabricFcoeVsanPcOperState,
       "cfprFabricFcoeVsanPcPeerDn": cfprFabricFcoeVsanPcPeerDn,
       "cfprFabricFcoeVsanPcPortId": cfprFabricFcoeVsanPcPortId,
       "cfprFabricFcoeVsanPcStateQual": cfprFabricFcoeVsanPcStateQual,
       "cfprFabricFcoeVsanPcSwitchId": cfprFabricFcoeVsanPcSwitchId,
       "cfprFabricFcoeVsanPcTransport": cfprFabricFcoeVsanPcTransport,
       "cfprFabricFcoeVsanPcType": cfprFabricFcoeVsanPcType,
       "cfprFabricFcoeVsanPcWarnings": cfprFabricFcoeVsanPcWarnings,
       "cfprFabricFcoeVsanPortEpTable": cfprFabricFcoeVsanPortEpTable,
       "cfprFabricFcoeVsanPortEpEntry": cfprFabricFcoeVsanPortEpEntry,
       "cfprFabricFcoeVsanPortEpInstanceId": cfprFabricFcoeVsanPortEpInstanceId,
       "cfprFabricFcoeVsanPortEpDn": cfprFabricFcoeVsanPortEpDn,
       "cfprFabricFcoeVsanPortEpRn": cfprFabricFcoeVsanPortEpRn,
       "cfprFabricFcoeVsanPortEpAdminState": cfprFabricFcoeVsanPortEpAdminState,
       "cfprFabricFcoeVsanPortEpAggrPortId": cfprFabricFcoeVsanPortEpAggrPortId,
       "cfprFabricFcoeVsanPortEpChassisId": cfprFabricFcoeVsanPortEpChassisId,
       "cfprFabricFcoeVsanPortEpEpDn": cfprFabricFcoeVsanPortEpEpDn,
       "cfprFabricFcoeVsanPortEpFltAggr": cfprFabricFcoeVsanPortEpFltAggr,
       "cfprFabricFcoeVsanPortEpIfRole": cfprFabricFcoeVsanPortEpIfRole,
       "cfprFabricFcoeVsanPortEpIfType": cfprFabricFcoeVsanPortEpIfType,
       "cfprFabricFcoeVsanPortEpLicGP": cfprFabricFcoeVsanPortEpLicGP,
       "cfprFabricFcoeVsanPortEpLicState": cfprFabricFcoeVsanPortEpLicState,
       "cfprFabricFcoeVsanPortEpLocale": cfprFabricFcoeVsanPortEpLocale,
       "cfprFabricFcoeVsanPortEpName": cfprFabricFcoeVsanPortEpName,
       "cfprFabricFcoeVsanPortEpOperState": cfprFabricFcoeVsanPortEpOperState,
       "cfprFabricFcoeVsanPortEpOperStateReason": cfprFabricFcoeVsanPortEpOperStateReason,
       "cfprFabricFcoeVsanPortEpPeerAggrPortId": cfprFabricFcoeVsanPortEpPeerAggrPortId,
       "cfprFabricFcoeVsanPortEpPeerChassisId": cfprFabricFcoeVsanPortEpPeerChassisId,
       "cfprFabricFcoeVsanPortEpPeerDn": cfprFabricFcoeVsanPortEpPeerDn,
       "cfprFabricFcoeVsanPortEpPeerPortId": cfprFabricFcoeVsanPortEpPeerPortId,
       "cfprFabricFcoeVsanPortEpPeerSlotId": cfprFabricFcoeVsanPortEpPeerSlotId,
       "cfprFabricFcoeVsanPortEpPortId": cfprFabricFcoeVsanPortEpPortId,
       "cfprFabricFcoeVsanPortEpSlotId": cfprFabricFcoeVsanPortEpSlotId,
       "cfprFabricFcoeVsanPortEpSwitchId": cfprFabricFcoeVsanPortEpSwitchId,
       "cfprFabricFcoeVsanPortEpTransport": cfprFabricFcoeVsanPortEpTransport,
       "cfprFabricFcoeVsanPortEpType": cfprFabricFcoeVsanPortEpType,
       "cfprFabricFcoeVsanPortEpWarnings": cfprFabricFcoeVsanPortEpWarnings,
       "cfprFabricIfTable": cfprFabricIfTable,
       "cfprFabricIfEntry": cfprFabricIfEntry,
       "cfprFabricIfInstanceId": cfprFabricIfInstanceId,
       "cfprFabricIfDn": cfprFabricIfDn,
       "cfprFabricIfRn": cfprFabricIfRn,
       "cfprFabricIfAddr": cfprFabricIfAddr,
       "cfprFabricIfId": cfprFabricIfId,
       "cfprFabricLacpPolicyTable": cfprFabricLacpPolicyTable,
       "cfprFabricLacpPolicyEntry": cfprFabricLacpPolicyEntry,
       "cfprFabricLacpPolicyInstanceId": cfprFabricLacpPolicyInstanceId,
       "cfprFabricLacpPolicyDn": cfprFabricLacpPolicyDn,
       "cfprFabricLacpPolicyRn": cfprFabricLacpPolicyRn,
       "cfprFabricLacpPolicyDescr": cfprFabricLacpPolicyDescr,
       "cfprFabricLacpPolicyFastTimer": cfprFabricLacpPolicyFastTimer,
       "cfprFabricLacpPolicyIntId": cfprFabricLacpPolicyIntId,
       "cfprFabricLacpPolicyName": cfprFabricLacpPolicyName,
       "cfprFabricLacpPolicyPolicyLevel": cfprFabricLacpPolicyPolicyLevel,
       "cfprFabricLacpPolicyPolicyOwner": cfprFabricLacpPolicyPolicyOwner,
       "cfprFabricLacpPolicySuspendIndividual": cfprFabricLacpPolicySuspendIndividual,
       "cfprFabricLanAccessMgrTable": cfprFabricLanAccessMgrTable,
       "cfprFabricLanAccessMgrEntry": cfprFabricLanAccessMgrEntry,
       "cfprFabricLanAccessMgrInstanceId": cfprFabricLanAccessMgrInstanceId,
       "cfprFabricLanAccessMgrDn": cfprFabricLanAccessMgrDn,
       "cfprFabricLanAccessMgrRn": cfprFabricLanAccessMgrRn,
       "cfprFabricLanCloudTable": cfprFabricLanCloudTable,
       "cfprFabricLanCloudEntry": cfprFabricLanCloudEntry,
       "cfprFabricLanCloudInstanceId": cfprFabricLanCloudInstanceId,
       "cfprFabricLanCloudDn": cfprFabricLanCloudDn,
       "cfprFabricLanCloudRn": cfprFabricLanCloudRn,
       "cfprFabricLanCloudFsmDescr": cfprFabricLanCloudFsmDescr,
       "cfprFabricLanCloudFsmPrev": cfprFabricLanCloudFsmPrev,
       "cfprFabricLanCloudFsmProgr": cfprFabricLanCloudFsmProgr,
       "cfprFabricLanCloudFsmRmtInvErrCode": cfprFabricLanCloudFsmRmtInvErrCode,
       "cfprFabricLanCloudFsmRmtInvErrDescr": cfprFabricLanCloudFsmRmtInvErrDescr,
       "cfprFabricLanCloudFsmRmtInvRslt": cfprFabricLanCloudFsmRmtInvRslt,
       "cfprFabricLanCloudFsmStageDescr": cfprFabricLanCloudFsmStageDescr,
       "cfprFabricLanCloudFsmStamp": cfprFabricLanCloudFsmStamp,
       "cfprFabricLanCloudFsmStatus": cfprFabricLanCloudFsmStatus,
       "cfprFabricLanCloudFsmTry": cfprFabricLanCloudFsmTry,
       "cfprFabricLanCloudMacAging": cfprFabricLanCloudMacAging,
       "cfprFabricLanCloudMode": cfprFabricLanCloudMode,
       "cfprFabricLanCloudVlanCompression": cfprFabricLanCloudVlanCompression,
       "cfprFabricLanCloudFsmTable": cfprFabricLanCloudFsmTable,
       "cfprFabricLanCloudFsmEntry": cfprFabricLanCloudFsmEntry,
       "cfprFabricLanCloudFsmInstanceId": cfprFabricLanCloudFsmInstanceId,
       "cfprFabricLanCloudFsmDn": cfprFabricLanCloudFsmDn,
       "cfprFabricLanCloudFsmRn": cfprFabricLanCloudFsmRn,
       "cfprFabricLanCloudFsmCompletionTime": cfprFabricLanCloudFsmCompletionTime,
       "cfprFabricLanCloudFsmCurrentFsm": cfprFabricLanCloudFsmCurrentFsm,
       "cfprFabricLanCloudFsmDescrData": cfprFabricLanCloudFsmDescrData,
       "cfprFabricLanCloudFsmFsmStatus": cfprFabricLanCloudFsmFsmStatus,
       "cfprFabricLanCloudFsmProgress": cfprFabricLanCloudFsmProgress,
       "cfprFabricLanCloudFsmRmtErrCode": cfprFabricLanCloudFsmRmtErrCode,
       "cfprFabricLanCloudFsmRmtErrDescr": cfprFabricLanCloudFsmRmtErrDescr,
       "cfprFabricLanCloudFsmRmtRslt": cfprFabricLanCloudFsmRmtRslt,
       "cfprFabricLanCloudFsmStageTable": cfprFabricLanCloudFsmStageTable,
       "cfprFabricLanCloudFsmStageEntry": cfprFabricLanCloudFsmStageEntry,
       "cfprFabricLanCloudFsmStageInstanceId": cfprFabricLanCloudFsmStageInstanceId,
       "cfprFabricLanCloudFsmStageDn": cfprFabricLanCloudFsmStageDn,
       "cfprFabricLanCloudFsmStageRn": cfprFabricLanCloudFsmStageRn,
       "cfprFabricLanCloudFsmStageDescrData": cfprFabricLanCloudFsmStageDescrData,
       "cfprFabricLanCloudFsmStageLastUpdateTime": cfprFabricLanCloudFsmStageLastUpdateTime,
       "cfprFabricLanCloudFsmStageName": cfprFabricLanCloudFsmStageName,
       "cfprFabricLanCloudFsmStageOrder": cfprFabricLanCloudFsmStageOrder,
       "cfprFabricLanCloudFsmStageRetry": cfprFabricLanCloudFsmStageRetry,
       "cfprFabricLanCloudFsmStageStageStatus": cfprFabricLanCloudFsmStageStageStatus,
       "cfprFabricLanCloudFsmTaskTable": cfprFabricLanCloudFsmTaskTable,
       "cfprFabricLanCloudFsmTaskEntry": cfprFabricLanCloudFsmTaskEntry,
       "cfprFabricLanCloudFsmTaskInstanceId": cfprFabricLanCloudFsmTaskInstanceId,
       "cfprFabricLanCloudFsmTaskDn": cfprFabricLanCloudFsmTaskDn,
       "cfprFabricLanCloudFsmTaskRn": cfprFabricLanCloudFsmTaskRn,
       "cfprFabricLanCloudFsmTaskCompletion": cfprFabricLanCloudFsmTaskCompletion,
       "cfprFabricLanCloudFsmTaskFlags": cfprFabricLanCloudFsmTaskFlags,
       "cfprFabricLanCloudFsmTaskItem": cfprFabricLanCloudFsmTaskItem,
       "cfprFabricLanCloudFsmTaskSeqId": cfprFabricLanCloudFsmTaskSeqId,
       "cfprFabricLanMonCloudTable": cfprFabricLanMonCloudTable,
       "cfprFabricLanMonCloudEntry": cfprFabricLanMonCloudEntry,
       "cfprFabricLanMonCloudInstanceId": cfprFabricLanMonCloudInstanceId,
       "cfprFabricLanMonCloudDn": cfprFabricLanMonCloudDn,
       "cfprFabricLanMonCloudRn": cfprFabricLanMonCloudRn,
       "cfprFabricLanMonCloudMode": cfprFabricLanMonCloudMode,
       "cfprFabricLanPinGroupTable": cfprFabricLanPinGroupTable,
       "cfprFabricLanPinGroupEntry": cfprFabricLanPinGroupEntry,
       "cfprFabricLanPinGroupInstanceId": cfprFabricLanPinGroupInstanceId,
       "cfprFabricLanPinGroupDn": cfprFabricLanPinGroupDn,
       "cfprFabricLanPinGroupRn": cfprFabricLanPinGroupRn,
       "cfprFabricLanPinGroupDescr": cfprFabricLanPinGroupDescr,
       "cfprFabricLanPinGroupIntId": cfprFabricLanPinGroupIntId,
       "cfprFabricLanPinGroupName": cfprFabricLanPinGroupName,
       "cfprFabricLanPinGroupPolicyLevel": cfprFabricLanPinGroupPolicyLevel,
       "cfprFabricLanPinGroupPolicyOwner": cfprFabricLanPinGroupPolicyOwner,
       "cfprFabricLanPinGroupSize": cfprFabricLanPinGroupSize,
       "cfprFabricLanPinTargetTable": cfprFabricLanPinTargetTable,
       "cfprFabricLanPinTargetEntry": cfprFabricLanPinTargetEntry,
       "cfprFabricLanPinTargetInstanceId": cfprFabricLanPinTargetInstanceId,
       "cfprFabricLanPinTargetDn": cfprFabricLanPinTargetDn,
       "cfprFabricLanPinTargetRn": cfprFabricLanPinTargetRn,
       "cfprFabricLanPinTargetEpDn": cfprFabricLanPinTargetEpDn,
       "cfprFabricLanPinTargetFabricId": cfprFabricLanPinTargetFabricId,
       "cfprFabricLanPinTargetTargetStatus": cfprFabricLanPinTargetTargetStatus,
       "cfprFabricLastAckedSlotTable": cfprFabricLastAckedSlotTable,
       "cfprFabricLastAckedSlotEntry": cfprFabricLastAckedSlotEntry,
       "cfprFabricLastAckedSlotInstanceId": cfprFabricLastAckedSlotInstanceId,
       "cfprFabricLastAckedSlotDn": cfprFabricLastAckedSlotDn,
       "cfprFabricLastAckedSlotRn": cfprFabricLastAckedSlotRn,
       "cfprFabricLastAckedSlotBoardAggregationRole": cfprFabricLastAckedSlotBoardAggregationRole,
       "cfprFabricLastAckedSlotChassisId": cfprFabricLastAckedSlotChassisId,
       "cfprFabricLastAckedSlotSlotId": cfprFabricLastAckedSlotSlotId,
       "cfprFabricLastAckedSlotSwitchId": cfprFabricLastAckedSlotSwitchId,
       "cfprFabricLocaleTable": cfprFabricLocaleTable,
       "cfprFabricLocaleEntry": cfprFabricLocaleEntry,
       "cfprFabricLocaleInstanceId": cfprFabricLocaleInstanceId,
       "cfprFabricLocaleDn": cfprFabricLocaleDn,
       "cfprFabricLocaleRn": cfprFabricLocaleRn,
       "cfprFabricLocaleCType": cfprFabricLocaleCType,
       "cfprFabricLocaleChassisId": cfprFabricLocaleChassisId,
       "cfprFabricLocaleLocale": cfprFabricLocaleLocale,
       "cfprFabricLocaleName": cfprFabricLocaleName,
       "cfprFabricLocaleSide": cfprFabricLocaleSide,
       "cfprFabricLocaleSlotId": cfprFabricLocaleSlotId,
       "cfprFabricLocaleSwitchId": cfprFabricLocaleSwitchId,
       "cfprFabricLocaleTransport": cfprFabricLocaleTransport,
       "cfprFabricLocaleType": cfprFabricLocaleType,
       "cfprFabricMulticastPolicyTable": cfprFabricMulticastPolicyTable,
       "cfprFabricMulticastPolicyEntry": cfprFabricMulticastPolicyEntry,
       "cfprFabricMulticastPolicyInstanceId": cfprFabricMulticastPolicyInstanceId,
       "cfprFabricMulticastPolicyDn": cfprFabricMulticastPolicyDn,
       "cfprFabricMulticastPolicyRn": cfprFabricMulticastPolicyRn,
       "cfprFabricMulticastPolicyDescr": cfprFabricMulticastPolicyDescr,
       "cfprFabricMulticastPolicyIntId": cfprFabricMulticastPolicyIntId,
       "cfprFabricMulticastPolicyName": cfprFabricMulticastPolicyName,
       "cfprFabricMulticastPolicyPolicyLevel": cfprFabricMulticastPolicyPolicyLevel,
       "cfprFabricMulticastPolicyPolicyOwner": cfprFabricMulticastPolicyPolicyOwner,
       "cfprFabricMulticastPolicyQuerierIpAddr": cfprFabricMulticastPolicyQuerierIpAddr,
       "cfprFabricMulticastPolicyQuerierState": cfprFabricMulticastPolicyQuerierState,
       "cfprFabricMulticastPolicySnoopingState": cfprFabricMulticastPolicySnoopingState,
       "cfprFabricNetGroupTable": cfprFabricNetGroupTable,
       "cfprFabricNetGroupEntry": cfprFabricNetGroupEntry,
       "cfprFabricNetGroupInstanceId": cfprFabricNetGroupInstanceId,
       "cfprFabricNetGroupDn": cfprFabricNetGroupDn,
       "cfprFabricNetGroupRn": cfprFabricNetGroupRn,
       "cfprFabricNetGroupAssigned": cfprFabricNetGroupAssigned,
       "cfprFabricNetGroupAssignmentOrder": cfprFabricNetGroupAssignmentOrder,
       "cfprFabricNetGroupDescr": cfprFabricNetGroupDescr,
       "cfprFabricNetGroupId": cfprFabricNetGroupId,
       "cfprFabricNetGroupIntId": cfprFabricNetGroupIntId,
       "cfprFabricNetGroupName": cfprFabricNetGroupName,
       "cfprFabricNetGroupNativeNet": cfprFabricNetGroupNativeNet,
       "cfprFabricNetGroupNativeNetDn": cfprFabricNetGroupNativeNetDn,
       "cfprFabricNetGroupOwner": cfprFabricNetGroupOwner,
       "cfprFabricNetGroupPeerDn": cfprFabricNetGroupPeerDn,
       "cfprFabricNetGroupPolicyLevel": cfprFabricNetGroupPolicyLevel,
       "cfprFabricNetGroupPolicyOwner": cfprFabricNetGroupPolicyOwner,
       "cfprFabricNetGroupSize": cfprFabricNetGroupSize,
       "cfprFabricNetGroupSwitchId": cfprFabricNetGroupSwitchId,
       "cfprFabricNetGroupType": cfprFabricNetGroupType,
       "cfprFabricOrgVlanPolicyTable": cfprFabricOrgVlanPolicyTable,
       "cfprFabricOrgVlanPolicyEntry": cfprFabricOrgVlanPolicyEntry,
       "cfprFabricOrgVlanPolicyInstanceId": cfprFabricOrgVlanPolicyInstanceId,
       "cfprFabricOrgVlanPolicyDn": cfprFabricOrgVlanPolicyDn,
       "cfprFabricOrgVlanPolicyRn": cfprFabricOrgVlanPolicyRn,
       "cfprFabricOrgVlanPolicyAdminState": cfprFabricOrgVlanPolicyAdminState,
       "cfprFabricOrgVlanPolicyName": cfprFabricOrgVlanPolicyName,
       "cfprFabricPathTable": cfprFabricPathTable,
       "cfprFabricPathEntry": cfprFabricPathEntry,
       "cfprFabricPathInstanceId": cfprFabricPathInstanceId,
       "cfprFabricPathDn": cfprFabricPathDn,
       "cfprFabricPathRn": cfprFabricPathRn,
       "cfprFabricPathCType": cfprFabricPathCType,
       "cfprFabricPathChassisId": cfprFabricPathChassisId,
       "cfprFabricPathEnacp": cfprFabricPathEnacp,
       "cfprFabricPathId": cfprFabricPathId,
       "cfprFabricPathLocale": cfprFabricPathLocale,
       "cfprFabricPathName": cfprFabricPathName,
       "cfprFabricPathNsSize": cfprFabricPathNsSize,
       "cfprFabricPathSide": cfprFabricPathSide,
       "cfprFabricPathSwitchId": cfprFabricPathSwitchId,
       "cfprFabricPathTransport": cfprFabricPathTransport,
       "cfprFabricPathType": cfprFabricPathType,
       "cfprFabricPathConnTable": cfprFabricPathConnTable,
       "cfprFabricPathConnEntry": cfprFabricPathConnEntry,
       "cfprFabricPathConnInstanceId": cfprFabricPathConnInstanceId,
       "cfprFabricPathConnDn": cfprFabricPathConnDn,
       "cfprFabricPathConnRn": cfprFabricPathConnRn,
       "cfprFabricPathConnCType": cfprFabricPathConnCType,
       "cfprFabricPathConnLocale": cfprFabricPathConnLocale,
       "cfprFabricPathConnName": cfprFabricPathConnName,
       "cfprFabricPathConnTransport": cfprFabricPathConnTransport,
       "cfprFabricPathConnType": cfprFabricPathConnType,
       "cfprFabricPathEpTable": cfprFabricPathEpTable,
       "cfprFabricPathEpEntry": cfprFabricPathEpEntry,
       "cfprFabricPathEpInstanceId": cfprFabricPathEpInstanceId,
       "cfprFabricPathEpDn": cfprFabricPathEpDn,
       "cfprFabricPathEpRn": cfprFabricPathEpRn,
       "cfprFabricPathEpAggrPortId": cfprFabricPathEpAggrPortId,
       "cfprFabricPathEpCType": cfprFabricPathEpCType,
       "cfprFabricPathEpChassisId": cfprFabricPathEpChassisId,
       "cfprFabricPathEpDiagLldpTransmit": cfprFabricPathEpDiagLldpTransmit,
       "cfprFabricPathEpEpDn": cfprFabricPathEpEpDn,
       "cfprFabricPathEpIfRole": cfprFabricPathEpIfRole,
       "cfprFabricPathEpIfType": cfprFabricPathEpIfType,
       "cfprFabricPathEpLocale": cfprFabricPathEpLocale,
       "cfprFabricPathEpName": cfprFabricPathEpName,
       "cfprFabricPathEpPeerAggrPortId": cfprFabricPathEpPeerAggrPortId,
       "cfprFabricPathEpPeerChassisId": cfprFabricPathEpPeerChassisId,
       "cfprFabricPathEpPeerDn": cfprFabricPathEpPeerDn,
       "cfprFabricPathEpPeerMac": cfprFabricPathEpPeerMac,
       "cfprFabricPathEpPeerPortId": cfprFabricPathEpPeerPortId,
       "cfprFabricPathEpPeerSlotId": cfprFabricPathEpPeerSlotId,
       "cfprFabricPathEpPortId": cfprFabricPathEpPortId,
       "cfprFabricPathEpSide": cfprFabricPathEpSide,
       "cfprFabricPathEpSlotId": cfprFabricPathEpSlotId,
       "cfprFabricPathEpSwitchId": cfprFabricPathEpSwitchId,
       "cfprFabricPathEpTransport": cfprFabricPathEpTransport,
       "cfprFabricPathEpType": cfprFabricPathEpType,
       "cfprFabricPoolableVlanTable": cfprFabricPoolableVlanTable,
       "cfprFabricPoolableVlanEntry": cfprFabricPoolableVlanEntry,
       "cfprFabricPoolableVlanInstanceId": cfprFabricPoolableVlanInstanceId,
       "cfprFabricPoolableVlanDn": cfprFabricPoolableVlanDn,
       "cfprFabricPoolableVlanRn": cfprFabricPoolableVlanRn,
       "cfprFabricPoolableVlanId": cfprFabricPoolableVlanId,
       "cfprFabricPoolableVlanPoolDn": cfprFabricPoolableVlanPoolDn,
       "cfprFabricPooledVlanTable": cfprFabricPooledVlanTable,
       "cfprFabricPooledVlanEntry": cfprFabricPooledVlanEntry,
       "cfprFabricPooledVlanInstanceId": cfprFabricPooledVlanInstanceId,
       "cfprFabricPooledVlanDn": cfprFabricPooledVlanDn,
       "cfprFabricPooledVlanRn": cfprFabricPooledVlanRn,
       "cfprFabricPooledVlanAssigned": cfprFabricPooledVlanAssigned,
       "cfprFabricPooledVlanAssignedToDn": cfprFabricPooledVlanAssignedToDn,
       "cfprFabricPooledVlanConfigIssues": cfprFabricPooledVlanConfigIssues,
       "cfprFabricPooledVlanName": cfprFabricPooledVlanName,
       "cfprFabricPooledVlanPeerDn": cfprFabricPooledVlanPeerDn,
       "cfprFabricPooledVlanPoolableDn": cfprFabricPooledVlanPoolableDn,
       "cfprFabricPooledVlanPrevAssignedToDn": cfprFabricPooledVlanPrevAssignedToDn,
       "cfprFabricSanCloudTable": cfprFabricSanCloudTable,
       "cfprFabricSanCloudEntry": cfprFabricSanCloudEntry,
       "cfprFabricSanCloudInstanceId": cfprFabricSanCloudInstanceId,
       "cfprFabricSanCloudDn": cfprFabricSanCloudDn,
       "cfprFabricSanCloudRn": cfprFabricSanCloudRn,
       "cfprFabricSanCloudFsmDescr": cfprFabricSanCloudFsmDescr,
       "cfprFabricSanCloudFsmPrev": cfprFabricSanCloudFsmPrev,
       "cfprFabricSanCloudFsmProgr": cfprFabricSanCloudFsmProgr,
       "cfprFabricSanCloudFsmRmtInvErrCode": cfprFabricSanCloudFsmRmtInvErrCode,
       "cfprFabricSanCloudFsmRmtInvErrDescr": cfprFabricSanCloudFsmRmtInvErrDescr,
       "cfprFabricSanCloudFsmRmtInvRslt": cfprFabricSanCloudFsmRmtInvRslt,
       "cfprFabricSanCloudFsmStageDescr": cfprFabricSanCloudFsmStageDescr,
       "cfprFabricSanCloudFsmStamp": cfprFabricSanCloudFsmStamp,
       "cfprFabricSanCloudFsmStatus": cfprFabricSanCloudFsmStatus,
       "cfprFabricSanCloudFsmTry": cfprFabricSanCloudFsmTry,
       "cfprFabricSanCloudMode": cfprFabricSanCloudMode,
       "cfprFabricSanCloudFsmTable": cfprFabricSanCloudFsmTable,
       "cfprFabricSanCloudFsmEntry": cfprFabricSanCloudFsmEntry,
       "cfprFabricSanCloudFsmInstanceId": cfprFabricSanCloudFsmInstanceId,
       "cfprFabricSanCloudFsmDn": cfprFabricSanCloudFsmDn,
       "cfprFabricSanCloudFsmRn": cfprFabricSanCloudFsmRn,
       "cfprFabricSanCloudFsmCompletionTime": cfprFabricSanCloudFsmCompletionTime,
       "cfprFabricSanCloudFsmCurrentFsm": cfprFabricSanCloudFsmCurrentFsm,
       "cfprFabricSanCloudFsmDescrData": cfprFabricSanCloudFsmDescrData,
       "cfprFabricSanCloudFsmFsmStatus": cfprFabricSanCloudFsmFsmStatus,
       "cfprFabricSanCloudFsmProgress": cfprFabricSanCloudFsmProgress,
       "cfprFabricSanCloudFsmRmtErrCode": cfprFabricSanCloudFsmRmtErrCode,
       "cfprFabricSanCloudFsmRmtErrDescr": cfprFabricSanCloudFsmRmtErrDescr,
       "cfprFabricSanCloudFsmRmtRslt": cfprFabricSanCloudFsmRmtRslt,
       "cfprFabricSanCloudFsmStageTable": cfprFabricSanCloudFsmStageTable,
       "cfprFabricSanCloudFsmStageEntry": cfprFabricSanCloudFsmStageEntry,
       "cfprFabricSanCloudFsmStageInstanceId": cfprFabricSanCloudFsmStageInstanceId,
       "cfprFabricSanCloudFsmStageDn": cfprFabricSanCloudFsmStageDn,
       "cfprFabricSanCloudFsmStageRn": cfprFabricSanCloudFsmStageRn,
       "cfprFabricSanCloudFsmStageDescrData": cfprFabricSanCloudFsmStageDescrData,
       "cfprFabricSanCloudFsmStageLastUpdateTime": cfprFabricSanCloudFsmStageLastUpdateTime,
       "cfprFabricSanCloudFsmStageName": cfprFabricSanCloudFsmStageName,
       "cfprFabricSanCloudFsmStageOrder": cfprFabricSanCloudFsmStageOrder,
       "cfprFabricSanCloudFsmStageRetry": cfprFabricSanCloudFsmStageRetry,
       "cfprFabricSanCloudFsmStageStageStatus": cfprFabricSanCloudFsmStageStageStatus,
       "cfprFabricSanCloudFsmTaskTable": cfprFabricSanCloudFsmTaskTable,
       "cfprFabricSanCloudFsmTaskEntry": cfprFabricSanCloudFsmTaskEntry,
       "cfprFabricSanCloudFsmTaskInstanceId": cfprFabricSanCloudFsmTaskInstanceId,
       "cfprFabricSanCloudFsmTaskDn": cfprFabricSanCloudFsmTaskDn,
       "cfprFabricSanCloudFsmTaskRn": cfprFabricSanCloudFsmTaskRn,
       "cfprFabricSanCloudFsmTaskCompletion": cfprFabricSanCloudFsmTaskCompletion,
       "cfprFabricSanCloudFsmTaskFlags": cfprFabricSanCloudFsmTaskFlags,
       "cfprFabricSanCloudFsmTaskItem": cfprFabricSanCloudFsmTaskItem,
       "cfprFabricSanCloudFsmTaskSeqId": cfprFabricSanCloudFsmTaskSeqId,
       "cfprFabricSanPinGroupTable": cfprFabricSanPinGroupTable,
       "cfprFabricSanPinGroupEntry": cfprFabricSanPinGroupEntry,
       "cfprFabricSanPinGroupInstanceId": cfprFabricSanPinGroupInstanceId,
       "cfprFabricSanPinGroupDn": cfprFabricSanPinGroupDn,
       "cfprFabricSanPinGroupRn": cfprFabricSanPinGroupRn,
       "cfprFabricSanPinGroupDescr": cfprFabricSanPinGroupDescr,
       "cfprFabricSanPinGroupIntId": cfprFabricSanPinGroupIntId,
       "cfprFabricSanPinGroupName": cfprFabricSanPinGroupName,
       "cfprFabricSanPinGroupPolicyLevel": cfprFabricSanPinGroupPolicyLevel,
       "cfprFabricSanPinGroupPolicyOwner": cfprFabricSanPinGroupPolicyOwner,
       "cfprFabricSanPinGroupSize": cfprFabricSanPinGroupSize,
       "cfprFabricSanPinTargetTable": cfprFabricSanPinTargetTable,
       "cfprFabricSanPinTargetEntry": cfprFabricSanPinTargetEntry,
       "cfprFabricSanPinTargetInstanceId": cfprFabricSanPinTargetInstanceId,
       "cfprFabricSanPinTargetDn": cfprFabricSanPinTargetDn,
       "cfprFabricSanPinTargetRn": cfprFabricSanPinTargetRn,
       "cfprFabricSanPinTargetEpDn": cfprFabricSanPinTargetEpDn,
       "cfprFabricSanPinTargetFabricId": cfprFabricSanPinTargetFabricId,
       "cfprFabricSanPinTargetTargetStatus": cfprFabricSanPinTargetTargetStatus,
       "cfprFabricSubGroupTable": cfprFabricSubGroupTable,
       "cfprFabricSubGroupEntry": cfprFabricSubGroupEntry,
       "cfprFabricSubGroupInstanceId": cfprFabricSubGroupInstanceId,
       "cfprFabricSubGroupDn": cfprFabricSubGroupDn,
       "cfprFabricSubGroupRn": cfprFabricSubGroupRn,
       "cfprFabricSubGroupAggrPortId": cfprFabricSubGroupAggrPortId,
       "cfprFabricSubGroupConfigState": cfprFabricSubGroupConfigState,
       "cfprFabricSubGroupLicGP": cfprFabricSubGroupLicGP,
       "cfprFabricSubGroupLicState": cfprFabricSubGroupLicState,
       "cfprFabricSubGroupLocale": cfprFabricSubGroupLocale,
       "cfprFabricSubGroupName": cfprFabricSubGroupName,
       "cfprFabricSubGroupSlotId": cfprFabricSubGroupSlotId,
       "cfprFabricSubGroupSwitchId": cfprFabricSubGroupSwitchId,
       "cfprFabricSubGroupTransport": cfprFabricSubGroupTransport,
       "cfprFabricSubGroupType": cfprFabricSubGroupType,
       "cfprFabricSwChPhEpTable": cfprFabricSwChPhEpTable,
       "cfprFabricSwChPhEpEntry": cfprFabricSwChPhEpEntry,
       "cfprFabricSwChPhEpInstanceId": cfprFabricSwChPhEpInstanceId,
       "cfprFabricSwChPhEpDn": cfprFabricSwChPhEpDn,
       "cfprFabricSwChPhEpRn": cfprFabricSwChPhEpRn,
       "cfprFabricSwChPhEpAdminState": cfprFabricSwChPhEpAdminState,
       "cfprFabricSwChPhEpAggrPortId": cfprFabricSwChPhEpAggrPortId,
       "cfprFabricSwChPhEpChassisId": cfprFabricSwChPhEpChassisId,
       "cfprFabricSwChPhEpEpDn": cfprFabricSwChPhEpEpDn,
       "cfprFabricSwChPhEpEqType": cfprFabricSwChPhEpEqType,
       "cfprFabricSwChPhEpFltAggr": cfprFabricSwChPhEpFltAggr,
       "cfprFabricSwChPhEpIfRole": cfprFabricSwChPhEpIfRole,
       "cfprFabricSwChPhEpIfType": cfprFabricSwChPhEpIfType,
       "cfprFabricSwChPhEpLc": cfprFabricSwChPhEpLc,
       "cfprFabricSwChPhEpLicGP": cfprFabricSwChPhEpLicGP,
       "cfprFabricSwChPhEpLicState": cfprFabricSwChPhEpLicState,
       "cfprFabricSwChPhEpLocale": cfprFabricSwChPhEpLocale,
       "cfprFabricSwChPhEpModel": cfprFabricSwChPhEpModel,
       "cfprFabricSwChPhEpName": cfprFabricSwChPhEpName,
       "cfprFabricSwChPhEpOperState": cfprFabricSwChPhEpOperState,
       "cfprFabricSwChPhEpOperStateReason": cfprFabricSwChPhEpOperStateReason,
       "cfprFabricSwChPhEpPeerAggrPortId": cfprFabricSwChPhEpPeerAggrPortId,
       "cfprFabricSwChPhEpPeerChassisId": cfprFabricSwChPhEpPeerChassisId,
       "cfprFabricSwChPhEpPeerDn": cfprFabricSwChPhEpPeerDn,
       "cfprFabricSwChPhEpPeerPortId": cfprFabricSwChPhEpPeerPortId,
       "cfprFabricSwChPhEpPeerSlotId": cfprFabricSwChPhEpPeerSlotId,
       "cfprFabricSwChPhEpPortId": cfprFabricSwChPhEpPortId,
       "cfprFabricSwChPhEpRevision": cfprFabricSwChPhEpRevision,
       "cfprFabricSwChPhEpSerial": cfprFabricSwChPhEpSerial,
       "cfprFabricSwChPhEpSlotId": cfprFabricSwChPhEpSlotId,
       "cfprFabricSwChPhEpSwitchId": cfprFabricSwChPhEpSwitchId,
       "cfprFabricSwChPhEpTransport": cfprFabricSwChPhEpTransport,
       "cfprFabricSwChPhEpType": cfprFabricSwChPhEpType,
       "cfprFabricSwChPhEpVendor": cfprFabricSwChPhEpVendor,
       "cfprFabricSwSubGroupTable": cfprFabricSwSubGroupTable,
       "cfprFabricSwSubGroupEntry": cfprFabricSwSubGroupEntry,
       "cfprFabricSwSubGroupInstanceId": cfprFabricSwSubGroupInstanceId,
       "cfprFabricSwSubGroupDn": cfprFabricSwSubGroupDn,
       "cfprFabricSwSubGroupRn": cfprFabricSwSubGroupRn,
       "cfprFabricSwSubGroupAggrPortId": cfprFabricSwSubGroupAggrPortId,
       "cfprFabricSwSubGroupConfigState": cfprFabricSwSubGroupConfigState,
       "cfprFabricSwSubGroupLicGP": cfprFabricSwSubGroupLicGP,
       "cfprFabricSwSubGroupLicState": cfprFabricSwSubGroupLicState,
       "cfprFabricSwSubGroupLocale": cfprFabricSwSubGroupLocale,
       "cfprFabricSwSubGroupName": cfprFabricSwSubGroupName,
       "cfprFabricSwSubGroupSlotId": cfprFabricSwSubGroupSlotId,
       "cfprFabricSwSubGroupSwitchId": cfprFabricSwSubGroupSwitchId,
       "cfprFabricSwSubGroupTransport": cfprFabricSwSubGroupTransport,
       "cfprFabricSwSubGroupType": cfprFabricSwSubGroupType,
       "cfprFabricUdldLinkPolicyTable": cfprFabricUdldLinkPolicyTable,
       "cfprFabricUdldLinkPolicyEntry": cfprFabricUdldLinkPolicyEntry,
       "cfprFabricUdldLinkPolicyInstanceId": cfprFabricUdldLinkPolicyInstanceId,
       "cfprFabricUdldLinkPolicyDn": cfprFabricUdldLinkPolicyDn,
       "cfprFabricUdldLinkPolicyRn": cfprFabricUdldLinkPolicyRn,
       "cfprFabricUdldLinkPolicyAdminState": cfprFabricUdldLinkPolicyAdminState,
       "cfprFabricUdldLinkPolicyDescr": cfprFabricUdldLinkPolicyDescr,
       "cfprFabricUdldLinkPolicyIntId": cfprFabricUdldLinkPolicyIntId,
       "cfprFabricUdldLinkPolicyMode": cfprFabricUdldLinkPolicyMode,
       "cfprFabricUdldLinkPolicyName": cfprFabricUdldLinkPolicyName,
       "cfprFabricUdldLinkPolicyPolicyLevel": cfprFabricUdldLinkPolicyPolicyLevel,
       "cfprFabricUdldLinkPolicyPolicyOwner": cfprFabricUdldLinkPolicyPolicyOwner,
       "cfprFabricUdldLinkPolicyProtocol": cfprFabricUdldLinkPolicyProtocol,
       "cfprFabricUdldLinkPolicyType": cfprFabricUdldLinkPolicyType,
       "cfprFabricUdldPolicyTable": cfprFabricUdldPolicyTable,
       "cfprFabricUdldPolicyEntry": cfprFabricUdldPolicyEntry,
       "cfprFabricUdldPolicyInstanceId": cfprFabricUdldPolicyInstanceId,
       "cfprFabricUdldPolicyDn": cfprFabricUdldPolicyDn,
       "cfprFabricUdldPolicyRn": cfprFabricUdldPolicyRn,
       "cfprFabricUdldPolicyDescr": cfprFabricUdldPolicyDescr,
       "cfprFabricUdldPolicyIntId": cfprFabricUdldPolicyIntId,
       "cfprFabricUdldPolicyMsgInterval": cfprFabricUdldPolicyMsgInterval,
       "cfprFabricUdldPolicyName": cfprFabricUdldPolicyName,
       "cfprFabricUdldPolicyPolicyLevel": cfprFabricUdldPolicyPolicyLevel,
       "cfprFabricUdldPolicyPolicyOwner": cfprFabricUdldPolicyPolicyOwner,
       "cfprFabricUdldPolicyRecoveryAction": cfprFabricUdldPolicyRecoveryAction,
       "cfprFabricVConTable": cfprFabricVConTable,
       "cfprFabricVConEntry": cfprFabricVConEntry,
       "cfprFabricVConInstanceId": cfprFabricVConInstanceId,
       "cfprFabricVConDn": cfprFabricVConDn,
       "cfprFabricVConRn": cfprFabricVConRn,
       "cfprFabricVConEquipmentDn": cfprFabricVConEquipmentDn,
       "cfprFabricVConFabric": cfprFabricVConFabric,
       "cfprFabricVConId": cfprFabricVConId,
       "cfprFabricVConInstType": cfprFabricVConInstType,
       "cfprFabricVConPlacement": cfprFabricVConPlacement,
       "cfprFabricVConSelect": cfprFabricVConSelect,
       "cfprFabricVConShare": cfprFabricVConShare,
       "cfprFabricVConTransport": cfprFabricVConTransport,
       "cfprFabricVConProfileTable": cfprFabricVConProfileTable,
       "cfprFabricVConProfileEntry": cfprFabricVConProfileEntry,
       "cfprFabricVConProfileInstanceId": cfprFabricVConProfileInstanceId,
       "cfprFabricVConProfileDn": cfprFabricVConProfileDn,
       "cfprFabricVConProfileRn": cfprFabricVConProfileRn,
       "cfprFabricVConProfileDescr": cfprFabricVConProfileDescr,
       "cfprFabricVConProfileIntId": cfprFabricVConProfileIntId,
       "cfprFabricVConProfileMezzMapping": cfprFabricVConProfileMezzMapping,
       "cfprFabricVConProfileName": cfprFabricVConProfileName,
       "cfprFabricVConProfilePolicyLevel": cfprFabricVConProfilePolicyLevel,
       "cfprFabricVConProfilePolicyOwner": cfprFabricVConProfilePolicyOwner,
       "cfprFabricVlanTable": cfprFabricVlanTable,
       "cfprFabricVlanEntry": cfprFabricVlanEntry,
       "cfprFabricVlanInstanceId": cfprFabricVlanInstanceId,
       "cfprFabricVlanDn": cfprFabricVlanDn,
       "cfprFabricVlanRn": cfprFabricVlanRn,
       "cfprFabricVlanAssocPrimaryVlanState": cfprFabricVlanAssocPrimaryVlanState,
       "cfprFabricVlanAssocPrimaryVlanSwitchId": cfprFabricVlanAssocPrimaryVlanSwitchId,
       "cfprFabricVlanCloud": cfprFabricVlanCloud,
       "cfprFabricVlanCompressionType": cfprFabricVlanCompressionType,
       "cfprFabricVlanConfigIssues": cfprFabricVlanConfigIssues,
       "cfprFabricVlanDefaultNet": cfprFabricVlanDefaultNet,
       "cfprFabricVlanEpDn": cfprFabricVlanEpDn,
       "cfprFabricVlanFltAggr": cfprFabricVlanFltAggr,
       "cfprFabricVlanGlobal": cfprFabricVlanGlobal,
       "cfprFabricVlanId": cfprFabricVlanId,
       "cfprFabricVlanIfRole": cfprFabricVlanIfRole,
       "cfprFabricVlanIfType": cfprFabricVlanIfType,
       "cfprFabricVlanLocal": cfprFabricVlanLocal,
       "cfprFabricVlanLocale": cfprFabricVlanLocale,
       "cfprFabricVlanMcastPolicyName": cfprFabricVlanMcastPolicyName,
       "cfprFabricVlanName": cfprFabricVlanName,
       "cfprFabricVlanOperMcastPolicyName": cfprFabricVlanOperMcastPolicyName,
       "cfprFabricVlanOperState": cfprFabricVlanOperState,
       "cfprFabricVlanOverlapStateForA": cfprFabricVlanOverlapStateForA,
       "cfprFabricVlanOverlapStateForB": cfprFabricVlanOverlapStateForB,
       "cfprFabricVlanPeerDn": cfprFabricVlanPeerDn,
       "cfprFabricVlanPolicyOwner": cfprFabricVlanPolicyOwner,
       "cfprFabricVlanPubNwDn": cfprFabricVlanPubNwDn,
       "cfprFabricVlanPubNwId": cfprFabricVlanPubNwId,
       "cfprFabricVlanPubNwName": cfprFabricVlanPubNwName,
       "cfprFabricVlanSharing": cfprFabricVlanSharing,
       "cfprFabricVlanSwitchId": cfprFabricVlanSwitchId,
       "cfprFabricVlanTransport": cfprFabricVlanTransport,
       "cfprFabricVlanType": cfprFabricVlanType,
       "cfprFabricVlanEpTable": cfprFabricVlanEpTable,
       "cfprFabricVlanEpEntry": cfprFabricVlanEpEntry,
       "cfprFabricVlanEpInstanceId": cfprFabricVlanEpInstanceId,
       "cfprFabricVlanEpDnData": cfprFabricVlanEpDnData,
       "cfprFabricVlanEpRn": cfprFabricVlanEpRn,
       "cfprFabricVlanEpAssocPrimaryVlanState": cfprFabricVlanEpAssocPrimaryVlanState,
       "cfprFabricVlanEpAssocPrimaryVlanSwitchId": cfprFabricVlanEpAssocPrimaryVlanSwitchId,
       "cfprFabricVlanEpEpDn": cfprFabricVlanEpEpDn,
       "cfprFabricVlanEpId": cfprFabricVlanEpId,
       "cfprFabricVlanEpIfRole": cfprFabricVlanEpIfRole,
       "cfprFabricVlanEpIfType": cfprFabricVlanEpIfType,
       "cfprFabricVlanEpIsNative": cfprFabricVlanEpIsNative,
       "cfprFabricVlanEpLocale": cfprFabricVlanEpLocale,
       "cfprFabricVlanEpName": cfprFabricVlanEpName,
       "cfprFabricVlanEpOperState": cfprFabricVlanEpOperState,
       "cfprFabricVlanEpOverlapStateForA": cfprFabricVlanEpOverlapStateForA,
       "cfprFabricVlanEpOverlapStateForB": cfprFabricVlanEpOverlapStateForB,
       "cfprFabricVlanEpPeerDn": cfprFabricVlanEpPeerDn,
       "cfprFabricVlanEpPolicyOwner": cfprFabricVlanEpPolicyOwner,
       "cfprFabricVlanEpPubNwDn": cfprFabricVlanEpPubNwDn,
       "cfprFabricVlanEpPubNwId": cfprFabricVlanEpPubNwId,
       "cfprFabricVlanEpPubNwName": cfprFabricVlanEpPubNwName,
       "cfprFabricVlanEpSharing": cfprFabricVlanEpSharing,
       "cfprFabricVlanEpSwitchId": cfprFabricVlanEpSwitchId,
       "cfprFabricVlanEpTransport": cfprFabricVlanEpTransport,
       "cfprFabricVlanEpType": cfprFabricVlanEpType,
       "cfprFabricVlanGroupReqTable": cfprFabricVlanGroupReqTable,
       "cfprFabricVlanGroupReqEntry": cfprFabricVlanGroupReqEntry,
       "cfprFabricVlanGroupReqInstanceId": cfprFabricVlanGroupReqInstanceId,
       "cfprFabricVlanGroupReqDn": cfprFabricVlanGroupReqDn,
       "cfprFabricVlanGroupReqRn": cfprFabricVlanGroupReqRn,
       "cfprFabricVlanGroupReqConfigIssues": cfprFabricVlanGroupReqConfigIssues,
       "cfprFabricVlanGroupReqName": cfprFabricVlanGroupReqName,
       "cfprFabricVlanGroupReqType": cfprFabricVlanGroupReqType,
       "cfprFabricVlanPermitTable": cfprFabricVlanPermitTable,
       "cfprFabricVlanPermitEntry": cfprFabricVlanPermitEntry,
       "cfprFabricVlanPermitInstanceId": cfprFabricVlanPermitInstanceId,
       "cfprFabricVlanPermitDn": cfprFabricVlanPermitDn,
       "cfprFabricVlanPermitRn": cfprFabricVlanPermitRn,
       "cfprFabricVlanPermitCloud": cfprFabricVlanPermitCloud,
       "cfprFabricVlanPermitName": cfprFabricVlanPermitName,
       "cfprFabricVlanPermitSwitchId": cfprFabricVlanPermitSwitchId,
       "cfprFabricVlanReqTable": cfprFabricVlanReqTable,
       "cfprFabricVlanReqEntry": cfprFabricVlanReqEntry,
       "cfprFabricVlanReqInstanceId": cfprFabricVlanReqInstanceId,
       "cfprFabricVlanReqDn": cfprFabricVlanReqDn,
       "cfprFabricVlanReqRn": cfprFabricVlanReqRn,
       "cfprFabricVlanReqConfigIssues": cfprFabricVlanReqConfigIssues,
       "cfprFabricVlanReqName": cfprFabricVlanReqName,
       "cfprFabricVlanReqType": cfprFabricVlanReqType,
       "cfprFabricVnetEpSyncEpTable": cfprFabricVnetEpSyncEpTable,
       "cfprFabricVnetEpSyncEpEntry": cfprFabricVnetEpSyncEpEntry,
       "cfprFabricVnetEpSyncEpInstanceId": cfprFabricVnetEpSyncEpInstanceId,
       "cfprFabricVnetEpSyncEpDn": cfprFabricVnetEpSyncEpDn,
       "cfprFabricVnetEpSyncEpRn": cfprFabricVnetEpSyncEpRn,
       "cfprFabricVnetEpSyncEpFsmDescr": cfprFabricVnetEpSyncEpFsmDescr,
       "cfprFabricVnetEpSyncEpFsmPrev": cfprFabricVnetEpSyncEpFsmPrev,
       "cfprFabricVnetEpSyncEpFsmProgr": cfprFabricVnetEpSyncEpFsmProgr,
       "cfprFabricVnetEpSyncEpFsmRmtInvErrCode": cfprFabricVnetEpSyncEpFsmRmtInvErrCode,
       "cfprFabricVnetEpSyncEpFsmRmtInvErrDescr": cfprFabricVnetEpSyncEpFsmRmtInvErrDescr,
       "cfprFabricVnetEpSyncEpFsmRmtInvRslt": cfprFabricVnetEpSyncEpFsmRmtInvRslt,
       "cfprFabricVnetEpSyncEpFsmStageDescr": cfprFabricVnetEpSyncEpFsmStageDescr,
       "cfprFabricVnetEpSyncEpFsmStamp": cfprFabricVnetEpSyncEpFsmStamp,
       "cfprFabricVnetEpSyncEpFsmStatus": cfprFabricVnetEpSyncEpFsmStatus,
       "cfprFabricVnetEpSyncEpFsmTry": cfprFabricVnetEpSyncEpFsmTry,
       "cfprFabricVnetEpSyncEpGenNumSync": cfprFabricVnetEpSyncEpGenNumSync,
       "cfprFabricVnetEpSyncEpId": cfprFabricVnetEpSyncEpId,
       "cfprFabricVnetEpSyncEpIsChangedObjectUpdate": cfprFabricVnetEpSyncEpIsChangedObjectUpdate,
       "cfprFabricVnetEpSyncEpFsmTable": cfprFabricVnetEpSyncEpFsmTable,
       "cfprFabricVnetEpSyncEpFsmEntry": cfprFabricVnetEpSyncEpFsmEntry,
       "cfprFabricVnetEpSyncEpFsmInstanceId": cfprFabricVnetEpSyncEpFsmInstanceId,
       "cfprFabricVnetEpSyncEpFsmDn": cfprFabricVnetEpSyncEpFsmDn,
       "cfprFabricVnetEpSyncEpFsmRn": cfprFabricVnetEpSyncEpFsmRn,
       "cfprFabricVnetEpSyncEpFsmCompletionTime": cfprFabricVnetEpSyncEpFsmCompletionTime,
       "cfprFabricVnetEpSyncEpFsmCurrentFsm": cfprFabricVnetEpSyncEpFsmCurrentFsm,
       "cfprFabricVnetEpSyncEpFsmDescrData": cfprFabricVnetEpSyncEpFsmDescrData,
       "cfprFabricVnetEpSyncEpFsmFsmStatus": cfprFabricVnetEpSyncEpFsmFsmStatus,
       "cfprFabricVnetEpSyncEpFsmProgress": cfprFabricVnetEpSyncEpFsmProgress,
       "cfprFabricVnetEpSyncEpFsmRmtErrCode": cfprFabricVnetEpSyncEpFsmRmtErrCode,
       "cfprFabricVnetEpSyncEpFsmRmtErrDescr": cfprFabricVnetEpSyncEpFsmRmtErrDescr,
       "cfprFabricVnetEpSyncEpFsmRmtRslt": cfprFabricVnetEpSyncEpFsmRmtRslt,
       "cfprFabricVnetEpSyncEpFsmStageTable": cfprFabricVnetEpSyncEpFsmStageTable,
       "cfprFabricVnetEpSyncEpFsmStageEntry": cfprFabricVnetEpSyncEpFsmStageEntry,
       "cfprFabricVnetEpSyncEpFsmStageInstanceId": cfprFabricVnetEpSyncEpFsmStageInstanceId,
       "cfprFabricVnetEpSyncEpFsmStageDn": cfprFabricVnetEpSyncEpFsmStageDn,
       "cfprFabricVnetEpSyncEpFsmStageRn": cfprFabricVnetEpSyncEpFsmStageRn,
       "cfprFabricVnetEpSyncEpFsmStageDescrData": cfprFabricVnetEpSyncEpFsmStageDescrData,
       "cfprFabricVnetEpSyncEpFsmStageLastUpdateTime": cfprFabricVnetEpSyncEpFsmStageLastUpdateTime,
       "cfprFabricVnetEpSyncEpFsmStageName": cfprFabricVnetEpSyncEpFsmStageName,
       "cfprFabricVnetEpSyncEpFsmStageOrder": cfprFabricVnetEpSyncEpFsmStageOrder,
       "cfprFabricVnetEpSyncEpFsmStageRetry": cfprFabricVnetEpSyncEpFsmStageRetry,
       "cfprFabricVnetEpSyncEpFsmStageStageStatus": cfprFabricVnetEpSyncEpFsmStageStageStatus,
       "cfprFabricVnetEpSyncEpFsmTaskTable": cfprFabricVnetEpSyncEpFsmTaskTable,
       "cfprFabricVnetEpSyncEpFsmTaskEntry": cfprFabricVnetEpSyncEpFsmTaskEntry,
       "cfprFabricVnetEpSyncEpFsmTaskInstanceId": cfprFabricVnetEpSyncEpFsmTaskInstanceId,
       "cfprFabricVnetEpSyncEpFsmTaskDn": cfprFabricVnetEpSyncEpFsmTaskDn,
       "cfprFabricVnetEpSyncEpFsmTaskRn": cfprFabricVnetEpSyncEpFsmTaskRn,
       "cfprFabricVnetEpSyncEpFsmTaskCompletion": cfprFabricVnetEpSyncEpFsmTaskCompletion,
       "cfprFabricVnetEpSyncEpFsmTaskFlags": cfprFabricVnetEpSyncEpFsmTaskFlags,
       "cfprFabricVnetEpSyncEpFsmTaskItem": cfprFabricVnetEpSyncEpFsmTaskItem,
       "cfprFabricVnetEpSyncEpFsmTaskSeqId": cfprFabricVnetEpSyncEpFsmTaskSeqId,
       "cfprFabricVsanTable": cfprFabricVsanTable,
       "cfprFabricVsanEntry": cfprFabricVsanEntry,
       "cfprFabricVsanInstanceId": cfprFabricVsanInstanceId,
       "cfprFabricVsanDn": cfprFabricVsanDn,
       "cfprFabricVsanRn": cfprFabricVsanRn,
       "cfprFabricVsanDefaultZoning": cfprFabricVsanDefaultZoning,
       "cfprFabricVsanEpDn": cfprFabricVsanEpDn,
       "cfprFabricVsanFcZoneSharingMode": cfprFabricVsanFcZoneSharingMode,
       "cfprFabricVsanFcoeVlan": cfprFabricVsanFcoeVlan,
       "cfprFabricVsanFltAggr": cfprFabricVsanFltAggr,
       "cfprFabricVsanGlobal": cfprFabricVsanGlobal,
       "cfprFabricVsanId": cfprFabricVsanId,
       "cfprFabricVsanIfRole": cfprFabricVsanIfRole,
       "cfprFabricVsanIfType": cfprFabricVsanIfType,
       "cfprFabricVsanLocal": cfprFabricVsanLocal,
       "cfprFabricVsanLocale": cfprFabricVsanLocale,
       "cfprFabricVsanName": cfprFabricVsanName,
       "cfprFabricVsanOperState": cfprFabricVsanOperState,
       "cfprFabricVsanPeerDn": cfprFabricVsanPeerDn,
       "cfprFabricVsanPolicyOwner": cfprFabricVsanPolicyOwner,
       "cfprFabricVsanSwitchId": cfprFabricVsanSwitchId,
       "cfprFabricVsanTransport": cfprFabricVsanTransport,
       "cfprFabricVsanType": cfprFabricVsanType,
       "cfprFabricVsanZoningState": cfprFabricVsanZoningState,
       "cfprFabricVsanEpTable": cfprFabricVsanEpTable,
       "cfprFabricVsanEpEntry": cfprFabricVsanEpEntry,
       "cfprFabricVsanEpInstanceId": cfprFabricVsanEpInstanceId,
       "cfprFabricVsanEpDnData": cfprFabricVsanEpDnData,
       "cfprFabricVsanEpRn": cfprFabricVsanEpRn,
       "cfprFabricVsanEpEpDn": cfprFabricVsanEpEpDn,
       "cfprFabricVsanEpFcoeVlan": cfprFabricVsanEpFcoeVlan,
       "cfprFabricVsanEpId": cfprFabricVsanEpId,
       "cfprFabricVsanEpIfRole": cfprFabricVsanEpIfRole,
       "cfprFabricVsanEpIfType": cfprFabricVsanEpIfType,
       "cfprFabricVsanEpLocale": cfprFabricVsanEpLocale,
       "cfprFabricVsanEpName": cfprFabricVsanEpName,
       "cfprFabricVsanEpOperState": cfprFabricVsanEpOperState,
       "cfprFabricVsanEpPeerDn": cfprFabricVsanEpPeerDn,
       "cfprFabricVsanEpPolicyOwner": cfprFabricVsanEpPolicyOwner,
       "cfprFabricVsanEpSwitchId": cfprFabricVsanEpSwitchId,
       "cfprFabricVsanEpTransport": cfprFabricVsanEpTransport,
       "cfprFabricVsanEpType": cfprFabricVsanEpType,
       "cfprFabricVsanEpZoningState": cfprFabricVsanEpZoningState,
       "cfprFabricVsanMembershipTable": cfprFabricVsanMembershipTable,
       "cfprFabricVsanMembershipEntry": cfprFabricVsanMembershipEntry,
       "cfprFabricVsanMembershipInstanceId": cfprFabricVsanMembershipInstanceId,
       "cfprFabricVsanMembershipDn": cfprFabricVsanMembershipDn,
       "cfprFabricVsanMembershipRn": cfprFabricVsanMembershipRn,
       "cfprFabricVsanMembershipMemberStatus": cfprFabricVsanMembershipMemberStatus,
       "cfprFabricVsanMembershipParentAdminState": cfprFabricVsanMembershipParentAdminState,
       "cfprFabricVsanMembershipStateQual": cfprFabricVsanMembershipStateQual,
       "cfprFabricVsanMembershipVsanId": cfprFabricVsanMembershipVsanId,
       "cfprFabricZoneIdUniverseTable": cfprFabricZoneIdUniverseTable,
       "cfprFabricZoneIdUniverseEntry": cfprFabricZoneIdUniverseEntry,
       "cfprFabricZoneIdUniverseInstanceId": cfprFabricZoneIdUniverseInstanceId,
       "cfprFabricZoneIdUniverseDn": cfprFabricZoneIdUniverseDn,
       "cfprFabricZoneIdUniverseRn": cfprFabricZoneIdUniverseRn,
       "cfprFabricSspEthMonTable": cfprFabricSspEthMonTable,
       "cfprFabricSspEthMonEntry": cfprFabricSspEthMonEntry,
       "cfprFabricSspEthMonInstanceId": cfprFabricSspEthMonInstanceId,
       "cfprFabricSspEthMonDn": cfprFabricSspEthMonDn,
       "cfprFabricSspEthMonRn": cfprFabricSspEthMonRn,
       "cfprFabricSspEthMonAdminState": cfprFabricSspEthMonAdminState,
       "cfprFabricSspEthMonAppendFlag": cfprFabricSspEthMonAppendFlag,
       "cfprFabricSspEthMonConfigFailReason": cfprFabricSspEthMonConfigFailReason,
       "cfprFabricSspEthMonDelPcap": cfprFabricSspEthMonDelPcap,
       "cfprFabricSspEthMonId": cfprFabricSspEthMonId,
       "cfprFabricSspEthMonIsConfigSuccess": cfprFabricSspEthMonIsConfigSuccess,
       "cfprFabricSspEthMonName": cfprFabricSspEthMonName,
       "cfprFabricSspEthMonOperState": cfprFabricSspEthMonOperState,
       "cfprFabricSspEthMonOperStateReason": cfprFabricSspEthMonOperStateReason,
       "cfprFabricSspEthMonPeerDn": cfprFabricSspEthMonPeerDn,
       "cfprFabricSspEthMonSession": cfprFabricSspEthMonSession,
       "cfprFabricSspEthMonSessionMemUsage": cfprFabricSspEthMonSessionMemUsage,
       "cfprFabricSspEthMonSourceConfigured": cfprFabricSspEthMonSourceConfigured,
       "cfprFabricSspEthMonDelAllSessEnabledState": cfprFabricSspEthMonDelAllSessEnabledState,
       "cfprFabricSspEthMonDropCount": cfprFabricSspEthMonDropCount,
       "cfprFabricSspEthMonErrorCode": cfprFabricSspEthMonErrorCode,
       "cfprFabricSspEthMonIsConfiguredByAG": cfprFabricSspEthMonIsConfiguredByAG,
       "cfprFabricSspEthMonReBoot": cfprFabricSspEthMonReBoot,
       "cfprFabricSspEthMonSessionPcapSnapLen": cfprFabricSspEthMonSessionPcapSnapLen,
       "cfprFabricSspEthMonFilterEpTable": cfprFabricSspEthMonFilterEpTable,
       "cfprFabricSspEthMonFilterEpEntry": cfprFabricSspEthMonFilterEpEntry,
       "cfprFabricSspEthMonFilterEpInstanceId": cfprFabricSspEthMonFilterEpInstanceId,
       "cfprFabricSspEthMonFilterEpDn": cfprFabricSspEthMonFilterEpDn,
       "cfprFabricSspEthMonFilterEpRn": cfprFabricSspEthMonFilterEpRn,
       "cfprFabricSspEthMonFilterEpDestIp": cfprFabricSspEthMonFilterEpDestIp,
       "cfprFabricSspEthMonFilterEpDestMAC": cfprFabricSspEthMonFilterEpDestMAC,
       "cfprFabricSspEthMonFilterEpDestPort": cfprFabricSspEthMonFilterEpDestPort,
       "cfprFabricSspEthMonFilterEpEthertype": cfprFabricSspEthMonFilterEpEthertype,
       "cfprFabricSspEthMonFilterEpIvlan": cfprFabricSspEthMonFilterEpIvlan,
       "cfprFabricSspEthMonFilterEpNameId": cfprFabricSspEthMonFilterEpNameId,
       "cfprFabricSspEthMonFilterEpOvlan": cfprFabricSspEthMonFilterEpOvlan,
       "cfprFabricSspEthMonFilterEpProtocol": cfprFabricSspEthMonFilterEpProtocol,
       "cfprFabricSspEthMonFilterEpSrcIp": cfprFabricSspEthMonFilterEpSrcIp,
       "cfprFabricSspEthMonFilterEpSrcMAC": cfprFabricSspEthMonFilterEpSrcMAC,
       "cfprFabricSspEthMonFilterEpSrcPort": cfprFabricSspEthMonFilterEpSrcPort,
       "cfprFabricSspEthMonFilterEpDestIpv6": cfprFabricSspEthMonFilterEpDestIpv6,
       "cfprFabricSspEthMonFilterEpEcmpId": cfprFabricSspEthMonFilterEpEcmpId,
       "cfprFabricSspEthMonFilterEpSrcIpv6": cfprFabricSspEthMonFilterEpSrcIpv6,
       "cfprFabricSspEthMonFilterEpSubvlan": cfprFabricSspEthMonFilterEpSubvlan,
       "cfprFabricSspEthMonFilterEpVifId": cfprFabricSspEthMonFilterEpVifId,
       "cfprFabricSspEthMonSrcAppEpTable": cfprFabricSspEthMonSrcAppEpTable,
       "cfprFabricSspEthMonSrcAppEpEntry": cfprFabricSspEthMonSrcAppEpEntry,
       "cfprFabricSspEthMonSrcAppEpInstanceId": cfprFabricSspEthMonSrcAppEpInstanceId,
       "cfprFabricSspEthMonSrcAppEpDn": cfprFabricSspEthMonSrcAppEpDn,
       "cfprFabricSspEthMonSrcAppEpRn": cfprFabricSspEthMonSrcAppEpRn,
       "cfprFabricSspEthMonSrcAppEpAppName": cfprFabricSspEthMonSrcAppEpAppName,
       "cfprFabricSspEthMonSrcAppEpFilter": cfprFabricSspEthMonSrcAppEpFilter,
       "cfprFabricSspEthMonSrcAppEpLinkName": cfprFabricSspEthMonSrcAppEpLinkName,
       "cfprFabricSspEthMonSrcAppEpPcapfile": cfprFabricSspEthMonSrcAppEpPcapfile,
       "cfprFabricSspEthMonSrcAppEpPcapfilename": cfprFabricSspEthMonSrcAppEpPcapfilename,
       "cfprFabricSspEthMonSrcAppEpPcapsize": cfprFabricSspEthMonSrcAppEpPcapsize,
       "cfprFabricSspEthMonSrcAppEpPortName": cfprFabricSspEthMonSrcAppEpPortName,
       "cfprFabricSspEthMonSrcAppEpSlotId": cfprFabricSspEthMonSrcAppEpSlotId,
       "cfprFabricSspEthMonSrcAppEpAppInstance": cfprFabricSspEthMonSrcAppEpAppInstance,
       "cfprFabricSspEthMonSrcAppEpSubInterface": cfprFabricSspEthMonSrcAppEpSubInterface,
       "cfprFabricSspEthMonSrcAppEpExternalLduLinkDn": cfprFabricSspEthMonSrcAppEpExternalLduLinkDn,
       "cfprFabricSspEthMonSrcAppLinksEpTable": cfprFabricSspEthMonSrcAppLinksEpTable,
       "cfprFabricSspEthMonSrcAppLinksEpEntry": cfprFabricSspEthMonSrcAppLinksEpEntry,
       "cfprFabricSspEthMonSrcAppLinksEpInstanceId": cfprFabricSspEthMonSrcAppLinksEpInstanceId,
       "cfprFabricSspEthMonSrcAppLinksEpDn": cfprFabricSspEthMonSrcAppLinksEpDn,
       "cfprFabricSspEthMonSrcAppLinksEpRn": cfprFabricSspEthMonSrcAppLinksEpRn,
       "cfprFabricSspEthMonSrcAppLinksEpChassisId": cfprFabricSspEthMonSrcAppLinksEpChassisId,
       "cfprFabricSspEthMonSrcAppLinksEpEqAggrPortId": cfprFabricSspEthMonSrcAppLinksEpEqAggrPortId,
       "cfprFabricSspEthMonSrcAppLinksEpEqPortId": cfprFabricSspEthMonSrcAppLinksEpEqPortId,
       "cfprFabricSspEthMonSrcAppLinksEpEqSlotId": cfprFabricSspEthMonSrcAppLinksEpEqSlotId,
       "cfprFabricSspEthMonSrcAppLinksEpFilter": cfprFabricSspEthMonSrcAppLinksEpFilter,
       "cfprFabricSspEthMonSrcAppLinksEpFilterDn": cfprFabricSspEthMonSrcAppLinksEpFilterDn,
       "cfprFabricSspEthMonSrcAppLinksEpLifeCycle": cfprFabricSspEthMonSrcAppLinksEpLifeCycle,
       "cfprFabricSspEthMonSrcAppLinksEpName": cfprFabricSspEthMonSrcAppLinksEpName,
       "cfprFabricSspEthMonSrcAppLinksEpPcapfile": cfprFabricSspEthMonSrcAppLinksEpPcapfile,
       "cfprFabricSspEthMonSrcAppLinksEpPcapfilename": cfprFabricSspEthMonSrcAppLinksEpPcapfilename,
       "cfprFabricSspEthMonSrcAppLinksEpPcapsize": cfprFabricSspEthMonSrcAppLinksEpPcapsize,
       "cfprFabricSspEthMonSrcAppLinksEpSwitchId": cfprFabricSspEthMonSrcAppLinksEpSwitchId,
       "cfprFabricSspEthMonSrcAppLinksEpVlan": cfprFabricSspEthMonSrcAppLinksEpVlan,
       "cfprFabricSspEthMonSrcAppLinksEpVifId": cfprFabricSspEthMonSrcAppLinksEpVifId,
       "cfprFabricSspEthMonSrcPhyAggrEpTable": cfprFabricSspEthMonSrcPhyAggrEpTable,
       "cfprFabricSspEthMonSrcPhyAggrEpEntry": cfprFabricSspEthMonSrcPhyAggrEpEntry,
       "cfprFabricSspEthMonSrcPhyAggrEpInstanceId": cfprFabricSspEthMonSrcPhyAggrEpInstanceId,
       "cfprFabricSspEthMonSrcPhyAggrEpDn": cfprFabricSspEthMonSrcPhyAggrEpDn,
       "cfprFabricSspEthMonSrcPhyAggrEpRn": cfprFabricSspEthMonSrcPhyAggrEpRn,
       "cfprFabricSspEthMonSrcPhyAggrEpAggrPortId": cfprFabricSspEthMonSrcPhyAggrEpAggrPortId,
       "cfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId": cfprFabricSspEthMonSrcPhyAggrEpBreakoutPortId,
       "cfprFabricSspEthMonSrcPhyAggrEpChassisId": cfprFabricSspEthMonSrcPhyAggrEpChassisId,
       "cfprFabricSspEthMonSrcPhyAggrEpFilter": cfprFabricSspEthMonSrcPhyAggrEpFilter,
       "cfprFabricSspEthMonSrcPhyAggrEpPcapfile": cfprFabricSspEthMonSrcPhyAggrEpPcapfile,
       "cfprFabricSspEthMonSrcPhyAggrEpPcapfilename": cfprFabricSspEthMonSrcPhyAggrEpPcapfilename,
       "cfprFabricSspEthMonSrcPhyAggrEpPcapsize": cfprFabricSspEthMonSrcPhyAggrEpPcapsize,
       "cfprFabricSspEthMonSrcPhyAggrEpSlotId": cfprFabricSspEthMonSrcPhyAggrEpSlotId,
       "cfprFabricSspEthMonSrcPhyAggrEpSwitchId": cfprFabricSspEthMonSrcPhyAggrEpSwitchId,
       "cfprFabricSspEthMonSrcPhyAggrEpAppInstance": cfprFabricSspEthMonSrcPhyAggrEpAppInstance,
       "cfprFabricSspEthMonSrcPhyAggrEpAppName": cfprFabricSspEthMonSrcPhyAggrEpAppName,
       "cfprFabricSspEthMonSrcPhyAggrEpSubInterface": cfprFabricSspEthMonSrcPhyAggrEpSubInterface,
       "cfprFabricSspEthMonSrcPhyAggrEpEcmpId": cfprFabricSspEthMonSrcPhyAggrEpEcmpId,
       "cfprFabricSspEthMonSrcPhyEpTable": cfprFabricSspEthMonSrcPhyEpTable,
       "cfprFabricSspEthMonSrcPhyEpEntry": cfprFabricSspEthMonSrcPhyEpEntry,
       "cfprFabricSspEthMonSrcPhyEpInstanceId": cfprFabricSspEthMonSrcPhyEpInstanceId,
       "cfprFabricSspEthMonSrcPhyEpDn": cfprFabricSspEthMonSrcPhyEpDn,
       "cfprFabricSspEthMonSrcPhyEpRn": cfprFabricSspEthMonSrcPhyEpRn,
       "cfprFabricSspEthMonSrcPhyEpChassisId": cfprFabricSspEthMonSrcPhyEpChassisId,
       "cfprFabricSspEthMonSrcPhyEpFilter": cfprFabricSspEthMonSrcPhyEpFilter,
       "cfprFabricSspEthMonSrcPhyEpPcapfile": cfprFabricSspEthMonSrcPhyEpPcapfile,
       "cfprFabricSspEthMonSrcPhyEpPcapfilename": cfprFabricSspEthMonSrcPhyEpPcapfilename,
       "cfprFabricSspEthMonSrcPhyEpPcapsize": cfprFabricSspEthMonSrcPhyEpPcapsize,
       "cfprFabricSspEthMonSrcPhyEpPortId": cfprFabricSspEthMonSrcPhyEpPortId,
       "cfprFabricSspEthMonSrcPhyEpSlotId": cfprFabricSspEthMonSrcPhyEpSlotId,
       "cfprFabricSspEthMonSrcPhyEpSwitchId": cfprFabricSspEthMonSrcPhyEpSwitchId,
       "cfprFabricSspEthMonSrcPhyEpAppInstance": cfprFabricSspEthMonSrcPhyEpAppInstance,
       "cfprFabricSspEthMonSrcPhyEpAppName": cfprFabricSspEthMonSrcPhyEpAppName,
       "cfprFabricSspEthMonSrcPhyEpSubInterface": cfprFabricSspEthMonSrcPhyEpSubInterface,
       "cfprFabricSspEthMonSrcPhyEpEcmpId": cfprFabricSspEthMonSrcPhyEpEcmpId,
       "cfprFabricSspLanMonCloudTable": cfprFabricSspLanMonCloudTable,
       "cfprFabricSspLanMonCloudEntry": cfprFabricSspLanMonCloudEntry,
       "cfprFabricSspLanMonCloudInstanceId": cfprFabricSspLanMonCloudInstanceId,
       "cfprFabricSspLanMonCloudDn": cfprFabricSspLanMonCloudDn,
       "cfprFabricSspLanMonCloudRn": cfprFabricSspLanMonCloudRn,
       "cfprFabricSspLanMonCloudMode": cfprFabricSspLanMonCloudMode,
       "cfprFabricSspLanMonCloudDelAllSess": cfprFabricSspLanMonCloudDelAllSess,
       "cfprFabricInnerVlanMgrTable": cfprFabricInnerVlanMgrTable,
       "cfprFabricInnerVlanMgrEntry": cfprFabricInnerVlanMgrEntry,
       "cfprFabricInnerVlanMgrInstanceId": cfprFabricInnerVlanMgrInstanceId,
       "cfprFabricInnerVlanMgrDn": cfprFabricInnerVlanMgrDn,
       "cfprFabricInnerVlanMgrRn": cfprFabricInnerVlanMgrRn,
       "cfprFabricInnerVlanMgrFltAggr": cfprFabricInnerVlanMgrFltAggr,
       "cfprFabricInnerVlanMgrId": cfprFabricInnerVlanMgrId,
       "cfprFabricSubIfTable": cfprFabricSubIfTable,
       "cfprFabricSubIfEntry": cfprFabricSubIfEntry,
       "cfprFabricSubIfInstanceId": cfprFabricSubIfInstanceId,
       "cfprFabricSubIfDn": cfprFabricSubIfDn,
       "cfprFabricSubIfRn": cfprFabricSubIfRn,
       "cfprFabricSubIfAllowSharing": cfprFabricSubIfAllowSharing,
       "cfprFabricSubIfDescr": cfprFabricSubIfDescr,
       "cfprFabricSubIfIfName": cfprFabricSubIfIfName,
       "cfprFabricSubIfSsaPortType": cfprFabricSubIfSsaPortType,
       "cfprFabricSubIfSubId": cfprFabricSubIfSubId,
       "cfprFabricSubIfVlanId": cfprFabricSubIfVlanId}
)
