# SNMP MIB module (CISCO-FIREPOWER-SW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-SW-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:12 2025
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

(CfprConditionRemoteInvRslt,
 CfprDpsecForgedTransmit,
 CfprFabricAVlanAssocPrimaryVlanSwitchId,
 CfprFabricAVlanSharing,
 CfprFabricAVlanTransport,
 CfprFabricAVlanType,
 CfprFabricAVsanTransport,
 CfprFabricAVsanType,
 CfprFabricAdminState,
 CfprFabricDefaultZoningState,
 CfprFabricEpVlanVlanType,
 CfprFabricEthEstcPortMode,
 CfprFabricEthPcProtocol,
 CfprFabricExternalEpLocale,
 CfprFabricFcZoneSharingMode,
 CfprFabricFillPattern,
 CfprFabricPIoEpIfType,
 CfprFabricPIoEpOperState,
 CfprFabricPIoEpPortId,
 CfprFabricPIoEpSlotId,
 CfprFabricPktCaptureAppendFlag,
 CfprFabricPort,
 CfprFabricQosPrio,
 CfprFabricRecoveryAction,
 CfprFabricSpannedCluster,
 CfprFabricTrafficDirection,
 CfprFabricVlanAssocPrimaryVlanState,
 CfprFabricVlanOperState,
 CfprFabricVlanOverlapState,
 CfprFabricVnetEpIfRole,
 CfprFabricVnetEpLocale,
 CfprFabricVnetEpPolicyOwner,
 CfprFabricVsanOperState,
 CfprFabricWarnings,
 CfprFabricZoningState,
 CfprFlowctrlFlowControlRx,
 CfprFlowctrlFlowControlTx,
 CfprFlowctrlPriorityPause,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprFsmLifecycle,
 CfprLicenseState,
 CfprLsFcZoneState,
 CfprNetworkConnectionType,
 CfprNetworkLocale,
 CfprNetworkPortRole,
 CfprNetworkSwitchId,
 CfprNetworkTransport,
 CfprNetworkVlanCountStatus,
 CfprNetworkVnetEpIfType,
 CfprNhTpHashType,
 CfprNwctrlAdminState,
 CfprNwctrlLinkFailAction,
 CfprNwctrlLldpAdminStateBitmask,
 CfprPortDuplex,
 CfprPortEthSpeed,
 CfprPortSpeed,
 CfprSwAccessDomainFsmCurrentFsm,
 CfprSwAccessDomainFsmStageName,
 CfprSwAccessDomainFsmTaskItem,
 CfprSwAccessDomainLocale,
 CfprSwAccessDomainType,
 CfprSwAccessEpLocale,
 CfprSwAccessEpTransport,
 CfprSwAdminState,
 CfprSwBorderDomainLocale,
 CfprSwBorderEpLocale,
 CfprSwBorderPcLocale,
 CfprSwBreakoutType,
 CfprSwCIoEpIfType,
 CfprSwCardEnvStatsHistThresholded,
 CfprSwCardEnvStatsThresholded,
 CfprSwCimcId,
 CfprSwConfMode,
 CfprSwConfigStatus,
 CfprSwEnvStatsHistThresholded,
 CfprSwEnvStatsThresholded,
 CfprSwEstcEpLocale,
 CfprSwEthEstcEpTransport,
 CfprSwEthEstcPcTransport,
 CfprSwEthLanBorderFsmCurrentFsm,
 CfprSwEthLanBorderFsmStageName,
 CfprSwEthLanBorderFsmTaskFlags,
 CfprSwEthLanBorderFsmTaskItem,
 CfprSwEthLanBorderTransport,
 CfprSwEthLanEpInlineState,
 CfprSwEthLanEpServiceState,
 CfprSwEthLanEpTransport,
 CfprSwEthLanEpUdldAdminState,
 CfprSwEthLanEpUdldMode,
 CfprSwEthLanMonTransport,
 CfprSwEthLanPcInlineState,
 CfprSwEthLanPcServiceState,
 CfprSwEthLanPcTransport,
 CfprSwEthMonDestEpTransport,
 CfprSwEthMonFsmCurrentFsm,
 CfprSwEthMonFsmStageName,
 CfprSwEthMonFsmTaskItem,
 CfprSwEthMonSrcEpTransport,
 CfprSwEthMonTransport,
 CfprSwEthMonType,
 CfprSwEthTargetEpAdminState,
 CfprSwEthTargetEpTransport,
 CfprSwExtUtilityFsmCurrentFsm,
 CfprSwExtUtilityFsmStageName,
 CfprSwExtUtilityFsmTaskItem,
 CfprSwFabricZoneNsAllocStatus,
 CfprSwFcSanBorderFsmCurrentFsm,
 CfprSwFcSanBorderFsmStageName,
 CfprSwFcSanBorderFsmTaskItem,
 CfprSwFcSanBorderTransport,
 CfprSwFcSanBorderUplinkTrunking,
 CfprSwFcSanEpTransport,
 CfprSwFcSanPcTransport,
 CfprSwFcServerZoneGroupLc,
 CfprSwFcZoneLc,
 CfprSwFcZoneMemberLc,
 CfprSwFcZoneSetLc,
 CfprSwFcoeSanEpTransport,
 CfprSwFcoeSanEpUdldAdminState,
 CfprSwFcoeSanEpUdldMode,
 CfprSwFcoeSanPcTransport,
 CfprSwLanBorderType,
 CfprSwLanEpIfRole,
 CfprSwLanEpType,
 CfprSwLanMonType,
 CfprSwLanPcIfRole,
 CfprSwLanPcType,
 CfprSwMonAdminState,
 CfprSwMonDomainLocale,
 CfprSwMonLifeCycle,
 CfprSwMonSrcEpLocale,
 CfprSwPIoEpIfType,
 CfprSwPIoEpLc,
 CfprSwPcMode,
 CfprSwPcModeState,
 CfprSwPeerStatus,
 CfprSwPhysFsmCurrentFsm,
 CfprSwPhysFsmStageName,
 CfprSwPhysFsmTaskItem,
 CfprSwPktCaptureLifeCycle,
 CfprSwPortBreakoutPortId,
 CfprSwPortBreakoutSlotId,
 CfprSwSanBorderType,
 CfprSwSanEpIfRole,
 CfprSwSanEpType,
 CfprSwSanPcIfRole,
 CfprSwSanPcType,
 CfprSwSspEthLanMonTransport,
 CfprSwSspEthMonFsmCurrentFsm,
 CfprSwSspEthMonFsmStageName,
 CfprSwSspEthMonFsmTaskFlags,
 CfprSwSspEthMonFsmTaskItem,
 CfprSwSspEthMonSrcPhyEpFsmCurrentFsm,
 CfprSwSspEthMonSrcPhyEpFsmStageName,
 CfprSwSspEthMonSrcPhyEpFsmTaskItem,
 CfprSwSspEthMonTransport,
 CfprSwSspEthMonType,
 CfprSwSspLanMonType,
 CfprSwSspMonAdminState,
 CfprSwSspMonDelPcap,
 CfprSwSspMonDomainLocale,
 CfprSwSubGroupAggrPortId,
 CfprSwSubGroupSlotId,
 CfprSwSystemStatsHistThresholded,
 CfprSwSystemStatsThresholded,
 CfprSwTargetEpType,
 CfprSwUlanPurpose,
 CfprSwUtilityDomainFsmCurrentFsm,
 CfprSwUtilityDomainFsmStageName,
 CfprSwUtilityDomainFsmTaskItem,
 CfprSwUtilityDomainLocale,
 CfprSwUtilityDomainType,
 CfprSwVlanCompType,
 CfprSwVlanConfigStatusType,
 CfprSwVlanGroupType,
 CfprSwVlanLc,
 CfprSwVlanPortNsAllocStatus) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprDpsecForgedTransmit",
    "CfprFabricAVlanAssocPrimaryVlanSwitchId",
    "CfprFabricAVlanSharing",
    "CfprFabricAVlanTransport",
    "CfprFabricAVlanType",
    "CfprFabricAVsanTransport",
    "CfprFabricAVsanType",
    "CfprFabricAdminState",
    "CfprFabricDefaultZoningState",
    "CfprFabricEpVlanVlanType",
    "CfprFabricEthEstcPortMode",
    "CfprFabricEthPcProtocol",
    "CfprFabricExternalEpLocale",
    "CfprFabricFcZoneSharingMode",
    "CfprFabricFillPattern",
    "CfprFabricPIoEpIfType",
    "CfprFabricPIoEpOperState",
    "CfprFabricPIoEpPortId",
    "CfprFabricPIoEpSlotId",
    "CfprFabricPktCaptureAppendFlag",
    "CfprFabricPort",
    "CfprFabricQosPrio",
    "CfprFabricRecoveryAction",
    "CfprFabricSpannedCluster",
    "CfprFabricTrafficDirection",
    "CfprFabricVlanAssocPrimaryVlanState",
    "CfprFabricVlanOperState",
    "CfprFabricVlanOverlapState",
    "CfprFabricVnetEpIfRole",
    "CfprFabricVnetEpLocale",
    "CfprFabricVnetEpPolicyOwner",
    "CfprFabricVsanOperState",
    "CfprFabricWarnings",
    "CfprFabricZoningState",
    "CfprFlowctrlFlowControlRx",
    "CfprFlowctrlFlowControlTx",
    "CfprFlowctrlPriorityPause",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprFsmLifecycle",
    "CfprLicenseState",
    "CfprLsFcZoneState",
    "CfprNetworkConnectionType",
    "CfprNetworkLocale",
    "CfprNetworkPortRole",
    "CfprNetworkSwitchId",
    "CfprNetworkTransport",
    "CfprNetworkVlanCountStatus",
    "CfprNetworkVnetEpIfType",
    "CfprNhTpHashType",
    "CfprNwctrlAdminState",
    "CfprNwctrlLinkFailAction",
    "CfprNwctrlLldpAdminStateBitmask",
    "CfprPortDuplex",
    "CfprPortEthSpeed",
    "CfprPortSpeed",
    "CfprSwAccessDomainFsmCurrentFsm",
    "CfprSwAccessDomainFsmStageName",
    "CfprSwAccessDomainFsmTaskItem",
    "CfprSwAccessDomainLocale",
    "CfprSwAccessDomainType",
    "CfprSwAccessEpLocale",
    "CfprSwAccessEpTransport",
    "CfprSwAdminState",
    "CfprSwBorderDomainLocale",
    "CfprSwBorderEpLocale",
    "CfprSwBorderPcLocale",
    "CfprSwBreakoutType",
    "CfprSwCIoEpIfType",
    "CfprSwCardEnvStatsHistThresholded",
    "CfprSwCardEnvStatsThresholded",
    "CfprSwCimcId",
    "CfprSwConfMode",
    "CfprSwConfigStatus",
    "CfprSwEnvStatsHistThresholded",
    "CfprSwEnvStatsThresholded",
    "CfprSwEstcEpLocale",
    "CfprSwEthEstcEpTransport",
    "CfprSwEthEstcPcTransport",
    "CfprSwEthLanBorderFsmCurrentFsm",
    "CfprSwEthLanBorderFsmStageName",
    "CfprSwEthLanBorderFsmTaskFlags",
    "CfprSwEthLanBorderFsmTaskItem",
    "CfprSwEthLanBorderTransport",
    "CfprSwEthLanEpInlineState",
    "CfprSwEthLanEpServiceState",
    "CfprSwEthLanEpTransport",
    "CfprSwEthLanEpUdldAdminState",
    "CfprSwEthLanEpUdldMode",
    "CfprSwEthLanMonTransport",
    "CfprSwEthLanPcInlineState",
    "CfprSwEthLanPcServiceState",
    "CfprSwEthLanPcTransport",
    "CfprSwEthMonDestEpTransport",
    "CfprSwEthMonFsmCurrentFsm",
    "CfprSwEthMonFsmStageName",
    "CfprSwEthMonFsmTaskItem",
    "CfprSwEthMonSrcEpTransport",
    "CfprSwEthMonTransport",
    "CfprSwEthMonType",
    "CfprSwEthTargetEpAdminState",
    "CfprSwEthTargetEpTransport",
    "CfprSwExtUtilityFsmCurrentFsm",
    "CfprSwExtUtilityFsmStageName",
    "CfprSwExtUtilityFsmTaskItem",
    "CfprSwFabricZoneNsAllocStatus",
    "CfprSwFcSanBorderFsmCurrentFsm",
    "CfprSwFcSanBorderFsmStageName",
    "CfprSwFcSanBorderFsmTaskItem",
    "CfprSwFcSanBorderTransport",
    "CfprSwFcSanBorderUplinkTrunking",
    "CfprSwFcSanEpTransport",
    "CfprSwFcSanPcTransport",
    "CfprSwFcServerZoneGroupLc",
    "CfprSwFcZoneLc",
    "CfprSwFcZoneMemberLc",
    "CfprSwFcZoneSetLc",
    "CfprSwFcoeSanEpTransport",
    "CfprSwFcoeSanEpUdldAdminState",
    "CfprSwFcoeSanEpUdldMode",
    "CfprSwFcoeSanPcTransport",
    "CfprSwLanBorderType",
    "CfprSwLanEpIfRole",
    "CfprSwLanEpType",
    "CfprSwLanMonType",
    "CfprSwLanPcIfRole",
    "CfprSwLanPcType",
    "CfprSwMonAdminState",
    "CfprSwMonDomainLocale",
    "CfprSwMonLifeCycle",
    "CfprSwMonSrcEpLocale",
    "CfprSwPIoEpIfType",
    "CfprSwPIoEpLc",
    "CfprSwPcMode",
    "CfprSwPcModeState",
    "CfprSwPeerStatus",
    "CfprSwPhysFsmCurrentFsm",
    "CfprSwPhysFsmStageName",
    "CfprSwPhysFsmTaskItem",
    "CfprSwPktCaptureLifeCycle",
    "CfprSwPortBreakoutPortId",
    "CfprSwPortBreakoutSlotId",
    "CfprSwSanBorderType",
    "CfprSwSanEpIfRole",
    "CfprSwSanEpType",
    "CfprSwSanPcIfRole",
    "CfprSwSanPcType",
    "CfprSwSspEthLanMonTransport",
    "CfprSwSspEthMonFsmCurrentFsm",
    "CfprSwSspEthMonFsmStageName",
    "CfprSwSspEthMonFsmTaskFlags",
    "CfprSwSspEthMonFsmTaskItem",
    "CfprSwSspEthMonSrcPhyEpFsmCurrentFsm",
    "CfprSwSspEthMonSrcPhyEpFsmStageName",
    "CfprSwSspEthMonSrcPhyEpFsmTaskItem",
    "CfprSwSspEthMonTransport",
    "CfprSwSspEthMonType",
    "CfprSwSspLanMonType",
    "CfprSwSspMonAdminState",
    "CfprSwSspMonDelPcap",
    "CfprSwSspMonDomainLocale",
    "CfprSwSubGroupAggrPortId",
    "CfprSwSubGroupSlotId",
    "CfprSwSystemStatsHistThresholded",
    "CfprSwSystemStatsThresholded",
    "CfprSwTargetEpType",
    "CfprSwUlanPurpose",
    "CfprSwUtilityDomainFsmCurrentFsm",
    "CfprSwUtilityDomainFsmStageName",
    "CfprSwUtilityDomainFsmTaskItem",
    "CfprSwUtilityDomainLocale",
    "CfprSwUtilityDomainType",
    "CfprSwVlanCompType",
    "CfprSwVlanConfigStatusType",
    "CfprSwVlanGroupType",
    "CfprSwVlanLc",
    "CfprSwVlanPortNsAllocStatus")

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

cfprSwObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprSwAccessDomainTable_Object = MibTable
cfprSwAccessDomainTable = _CfprSwAccessDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1)
)
if mibBuilder.loadTexts:
    cfprSwAccessDomainTable.setStatus("current")
_CfprSwAccessDomainEntry_Object = MibTableRow
cfprSwAccessDomainEntry = _CfprSwAccessDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1)
)
cfprSwAccessDomainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwAccessDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwAccessDomainEntry.setStatus("current")
_CfprSwAccessDomainInstanceId_Type = CfprManagedObjectId
_CfprSwAccessDomainInstanceId_Object = MibTableColumn
cfprSwAccessDomainInstanceId = _CfprSwAccessDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 1),
    _CfprSwAccessDomainInstanceId_Type()
)
cfprSwAccessDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwAccessDomainInstanceId.setStatus("current")
_CfprSwAccessDomainDn_Type = CfprManagedObjectDn
_CfprSwAccessDomainDn_Object = MibTableColumn
cfprSwAccessDomainDn = _CfprSwAccessDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 2),
    _CfprSwAccessDomainDn_Type()
)
cfprSwAccessDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainDn.setStatus("current")
_CfprSwAccessDomainRn_Type = SnmpAdminString
_CfprSwAccessDomainRn_Object = MibTableColumn
cfprSwAccessDomainRn = _CfprSwAccessDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 3),
    _CfprSwAccessDomainRn_Type()
)
cfprSwAccessDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainRn.setStatus("current")
_CfprSwAccessDomainFsmDescr_Type = SnmpAdminString
_CfprSwAccessDomainFsmDescr_Object = MibTableColumn
cfprSwAccessDomainFsmDescr = _CfprSwAccessDomainFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 4),
    _CfprSwAccessDomainFsmDescr_Type()
)
cfprSwAccessDomainFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmDescr.setStatus("current")
_CfprSwAccessDomainFsmPrev_Type = SnmpAdminString
_CfprSwAccessDomainFsmPrev_Object = MibTableColumn
cfprSwAccessDomainFsmPrev = _CfprSwAccessDomainFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 5),
    _CfprSwAccessDomainFsmPrev_Type()
)
cfprSwAccessDomainFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmPrev.setStatus("current")
_CfprSwAccessDomainFsmProgr_Type = Gauge32
_CfprSwAccessDomainFsmProgr_Object = MibTableColumn
cfprSwAccessDomainFsmProgr = _CfprSwAccessDomainFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 6),
    _CfprSwAccessDomainFsmProgr_Type()
)
cfprSwAccessDomainFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmProgr.setStatus("current")
_CfprSwAccessDomainFsmRmtInvErrCode_Type = Gauge32
_CfprSwAccessDomainFsmRmtInvErrCode_Object = MibTableColumn
cfprSwAccessDomainFsmRmtInvErrCode = _CfprSwAccessDomainFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 7),
    _CfprSwAccessDomainFsmRmtInvErrCode_Type()
)
cfprSwAccessDomainFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmRmtInvErrCode.setStatus("current")
_CfprSwAccessDomainFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwAccessDomainFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwAccessDomainFsmRmtInvErrDescr = _CfprSwAccessDomainFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 8),
    _CfprSwAccessDomainFsmRmtInvErrDescr_Type()
)
cfprSwAccessDomainFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmRmtInvErrDescr.setStatus("current")
_CfprSwAccessDomainFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwAccessDomainFsmRmtInvRslt_Object = MibTableColumn
cfprSwAccessDomainFsmRmtInvRslt = _CfprSwAccessDomainFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 9),
    _CfprSwAccessDomainFsmRmtInvRslt_Type()
)
cfprSwAccessDomainFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmRmtInvRslt.setStatus("current")
_CfprSwAccessDomainFsmStageDescr_Type = SnmpAdminString
_CfprSwAccessDomainFsmStageDescr_Object = MibTableColumn
cfprSwAccessDomainFsmStageDescr = _CfprSwAccessDomainFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 10),
    _CfprSwAccessDomainFsmStageDescr_Type()
)
cfprSwAccessDomainFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageDescr.setStatus("current")
_CfprSwAccessDomainFsmStamp_Type = DateAndTime
_CfprSwAccessDomainFsmStamp_Object = MibTableColumn
cfprSwAccessDomainFsmStamp = _CfprSwAccessDomainFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 11),
    _CfprSwAccessDomainFsmStamp_Type()
)
cfprSwAccessDomainFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStamp.setStatus("current")
_CfprSwAccessDomainFsmStatus_Type = SnmpAdminString
_CfprSwAccessDomainFsmStatus_Object = MibTableColumn
cfprSwAccessDomainFsmStatus = _CfprSwAccessDomainFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 12),
    _CfprSwAccessDomainFsmStatus_Type()
)
cfprSwAccessDomainFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStatus.setStatus("current")
_CfprSwAccessDomainFsmTry_Type = Gauge32
_CfprSwAccessDomainFsmTry_Object = MibTableColumn
cfprSwAccessDomainFsmTry = _CfprSwAccessDomainFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 13),
    _CfprSwAccessDomainFsmTry_Type()
)
cfprSwAccessDomainFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTry.setStatus("current")
_CfprSwAccessDomainLocale_Type = CfprSwAccessDomainLocale
_CfprSwAccessDomainLocale_Object = MibTableColumn
cfprSwAccessDomainLocale = _CfprSwAccessDomainLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 14),
    _CfprSwAccessDomainLocale_Type()
)
cfprSwAccessDomainLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainLocale.setStatus("current")
_CfprSwAccessDomainName_Type = SnmpAdminString
_CfprSwAccessDomainName_Object = MibTableColumn
cfprSwAccessDomainName = _CfprSwAccessDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 15),
    _CfprSwAccessDomainName_Type()
)
cfprSwAccessDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainName.setStatus("current")
_CfprSwAccessDomainSwitchId_Type = CfprNetworkSwitchId
_CfprSwAccessDomainSwitchId_Object = MibTableColumn
cfprSwAccessDomainSwitchId = _CfprSwAccessDomainSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 16),
    _CfprSwAccessDomainSwitchId_Type()
)
cfprSwAccessDomainSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainSwitchId.setStatus("current")
_CfprSwAccessDomainTransport_Type = CfprNetworkTransport
_CfprSwAccessDomainTransport_Object = MibTableColumn
cfprSwAccessDomainTransport = _CfprSwAccessDomainTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 17),
    _CfprSwAccessDomainTransport_Type()
)
cfprSwAccessDomainTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainTransport.setStatus("current")
_CfprSwAccessDomainType_Type = CfprSwAccessDomainType
_CfprSwAccessDomainType_Object = MibTableColumn
cfprSwAccessDomainType = _CfprSwAccessDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 1, 1, 18),
    _CfprSwAccessDomainType_Type()
)
cfprSwAccessDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainType.setStatus("current")
_CfprSwAccessDomainFsmTable_Object = MibTable
cfprSwAccessDomainFsmTable = _CfprSwAccessDomainFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2)
)
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTable.setStatus("current")
_CfprSwAccessDomainFsmEntry_Object = MibTableRow
cfprSwAccessDomainFsmEntry = _CfprSwAccessDomainFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1)
)
cfprSwAccessDomainFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwAccessDomainFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmEntry.setStatus("current")
_CfprSwAccessDomainFsmInstanceId_Type = CfprManagedObjectId
_CfprSwAccessDomainFsmInstanceId_Object = MibTableColumn
cfprSwAccessDomainFsmInstanceId = _CfprSwAccessDomainFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 1),
    _CfprSwAccessDomainFsmInstanceId_Type()
)
cfprSwAccessDomainFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmInstanceId.setStatus("current")
_CfprSwAccessDomainFsmDn_Type = CfprManagedObjectDn
_CfprSwAccessDomainFsmDn_Object = MibTableColumn
cfprSwAccessDomainFsmDn = _CfprSwAccessDomainFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 2),
    _CfprSwAccessDomainFsmDn_Type()
)
cfprSwAccessDomainFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmDn.setStatus("current")
_CfprSwAccessDomainFsmRn_Type = SnmpAdminString
_CfprSwAccessDomainFsmRn_Object = MibTableColumn
cfprSwAccessDomainFsmRn = _CfprSwAccessDomainFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 3),
    _CfprSwAccessDomainFsmRn_Type()
)
cfprSwAccessDomainFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmRn.setStatus("current")
_CfprSwAccessDomainFsmCompletionTime_Type = DateAndTime
_CfprSwAccessDomainFsmCompletionTime_Object = MibTableColumn
cfprSwAccessDomainFsmCompletionTime = _CfprSwAccessDomainFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 4),
    _CfprSwAccessDomainFsmCompletionTime_Type()
)
cfprSwAccessDomainFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmCompletionTime.setStatus("current")
_CfprSwAccessDomainFsmCurrentFsm_Type = CfprSwAccessDomainFsmCurrentFsm
_CfprSwAccessDomainFsmCurrentFsm_Object = MibTableColumn
cfprSwAccessDomainFsmCurrentFsm = _CfprSwAccessDomainFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 5),
    _CfprSwAccessDomainFsmCurrentFsm_Type()
)
cfprSwAccessDomainFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmCurrentFsm.setStatus("current")
_CfprSwAccessDomainFsmDescrData_Type = SnmpAdminString
_CfprSwAccessDomainFsmDescrData_Object = MibTableColumn
cfprSwAccessDomainFsmDescrData = _CfprSwAccessDomainFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 6),
    _CfprSwAccessDomainFsmDescrData_Type()
)
cfprSwAccessDomainFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmDescrData.setStatus("current")
_CfprSwAccessDomainFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwAccessDomainFsmFsmStatus_Object = MibTableColumn
cfprSwAccessDomainFsmFsmStatus = _CfprSwAccessDomainFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 7),
    _CfprSwAccessDomainFsmFsmStatus_Type()
)
cfprSwAccessDomainFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmFsmStatus.setStatus("current")
_CfprSwAccessDomainFsmProgress_Type = Gauge32
_CfprSwAccessDomainFsmProgress_Object = MibTableColumn
cfprSwAccessDomainFsmProgress = _CfprSwAccessDomainFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 8),
    _CfprSwAccessDomainFsmProgress_Type()
)
cfprSwAccessDomainFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmProgress.setStatus("current")
_CfprSwAccessDomainFsmRmtErrCode_Type = Gauge32
_CfprSwAccessDomainFsmRmtErrCode_Object = MibTableColumn
cfprSwAccessDomainFsmRmtErrCode = _CfprSwAccessDomainFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 9),
    _CfprSwAccessDomainFsmRmtErrCode_Type()
)
cfprSwAccessDomainFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmRmtErrCode.setStatus("current")
_CfprSwAccessDomainFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwAccessDomainFsmRmtErrDescr_Object = MibTableColumn
cfprSwAccessDomainFsmRmtErrDescr = _CfprSwAccessDomainFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 10),
    _CfprSwAccessDomainFsmRmtErrDescr_Type()
)
cfprSwAccessDomainFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmRmtErrDescr.setStatus("current")
_CfprSwAccessDomainFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwAccessDomainFsmRmtRslt_Object = MibTableColumn
cfprSwAccessDomainFsmRmtRslt = _CfprSwAccessDomainFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 2, 1, 11),
    _CfprSwAccessDomainFsmRmtRslt_Type()
)
cfprSwAccessDomainFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmRmtRslt.setStatus("current")
_CfprSwAccessDomainFsmStageTable_Object = MibTable
cfprSwAccessDomainFsmStageTable = _CfprSwAccessDomainFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3)
)
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageTable.setStatus("current")
_CfprSwAccessDomainFsmStageEntry_Object = MibTableRow
cfprSwAccessDomainFsmStageEntry = _CfprSwAccessDomainFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1)
)
cfprSwAccessDomainFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwAccessDomainFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageEntry.setStatus("current")
_CfprSwAccessDomainFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwAccessDomainFsmStageInstanceId_Object = MibTableColumn
cfprSwAccessDomainFsmStageInstanceId = _CfprSwAccessDomainFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 1),
    _CfprSwAccessDomainFsmStageInstanceId_Type()
)
cfprSwAccessDomainFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageInstanceId.setStatus("current")
_CfprSwAccessDomainFsmStageDn_Type = CfprManagedObjectDn
_CfprSwAccessDomainFsmStageDn_Object = MibTableColumn
cfprSwAccessDomainFsmStageDn = _CfprSwAccessDomainFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 2),
    _CfprSwAccessDomainFsmStageDn_Type()
)
cfprSwAccessDomainFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageDn.setStatus("current")
_CfprSwAccessDomainFsmStageRn_Type = SnmpAdminString
_CfprSwAccessDomainFsmStageRn_Object = MibTableColumn
cfprSwAccessDomainFsmStageRn = _CfprSwAccessDomainFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 3),
    _CfprSwAccessDomainFsmStageRn_Type()
)
cfprSwAccessDomainFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageRn.setStatus("current")
_CfprSwAccessDomainFsmStageDescrData_Type = SnmpAdminString
_CfprSwAccessDomainFsmStageDescrData_Object = MibTableColumn
cfprSwAccessDomainFsmStageDescrData = _CfprSwAccessDomainFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 4),
    _CfprSwAccessDomainFsmStageDescrData_Type()
)
cfprSwAccessDomainFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageDescrData.setStatus("current")
_CfprSwAccessDomainFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwAccessDomainFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwAccessDomainFsmStageLastUpdateTime = _CfprSwAccessDomainFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 5),
    _CfprSwAccessDomainFsmStageLastUpdateTime_Type()
)
cfprSwAccessDomainFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageLastUpdateTime.setStatus("current")
_CfprSwAccessDomainFsmStageName_Type = CfprSwAccessDomainFsmStageName
_CfprSwAccessDomainFsmStageName_Object = MibTableColumn
cfprSwAccessDomainFsmStageName = _CfprSwAccessDomainFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 6),
    _CfprSwAccessDomainFsmStageName_Type()
)
cfprSwAccessDomainFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageName.setStatus("current")
_CfprSwAccessDomainFsmStageOrder_Type = Gauge32
_CfprSwAccessDomainFsmStageOrder_Object = MibTableColumn
cfprSwAccessDomainFsmStageOrder = _CfprSwAccessDomainFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 7),
    _CfprSwAccessDomainFsmStageOrder_Type()
)
cfprSwAccessDomainFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageOrder.setStatus("current")
_CfprSwAccessDomainFsmStageRetry_Type = Gauge32
_CfprSwAccessDomainFsmStageRetry_Object = MibTableColumn
cfprSwAccessDomainFsmStageRetry = _CfprSwAccessDomainFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 8),
    _CfprSwAccessDomainFsmStageRetry_Type()
)
cfprSwAccessDomainFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageRetry.setStatus("current")
_CfprSwAccessDomainFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwAccessDomainFsmStageStageStatus_Object = MibTableColumn
cfprSwAccessDomainFsmStageStageStatus = _CfprSwAccessDomainFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 3, 1, 9),
    _CfprSwAccessDomainFsmStageStageStatus_Type()
)
cfprSwAccessDomainFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmStageStageStatus.setStatus("current")
_CfprSwAccessDomainFsmTaskTable_Object = MibTable
cfprSwAccessDomainFsmTaskTable = _CfprSwAccessDomainFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4)
)
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskTable.setStatus("current")
_CfprSwAccessDomainFsmTaskEntry_Object = MibTableRow
cfprSwAccessDomainFsmTaskEntry = _CfprSwAccessDomainFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4, 1)
)
cfprSwAccessDomainFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwAccessDomainFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskEntry.setStatus("current")
_CfprSwAccessDomainFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwAccessDomainFsmTaskInstanceId_Object = MibTableColumn
cfprSwAccessDomainFsmTaskInstanceId = _CfprSwAccessDomainFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4, 1, 1),
    _CfprSwAccessDomainFsmTaskInstanceId_Type()
)
cfprSwAccessDomainFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskInstanceId.setStatus("current")
_CfprSwAccessDomainFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwAccessDomainFsmTaskDn_Object = MibTableColumn
cfprSwAccessDomainFsmTaskDn = _CfprSwAccessDomainFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4, 1, 2),
    _CfprSwAccessDomainFsmTaskDn_Type()
)
cfprSwAccessDomainFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskDn.setStatus("current")
_CfprSwAccessDomainFsmTaskRn_Type = SnmpAdminString
_CfprSwAccessDomainFsmTaskRn_Object = MibTableColumn
cfprSwAccessDomainFsmTaskRn = _CfprSwAccessDomainFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4, 1, 3),
    _CfprSwAccessDomainFsmTaskRn_Type()
)
cfprSwAccessDomainFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskRn.setStatus("current")
_CfprSwAccessDomainFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwAccessDomainFsmTaskCompletion_Object = MibTableColumn
cfprSwAccessDomainFsmTaskCompletion = _CfprSwAccessDomainFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4, 1, 4),
    _CfprSwAccessDomainFsmTaskCompletion_Type()
)
cfprSwAccessDomainFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskCompletion.setStatus("current")
_CfprSwAccessDomainFsmTaskFlags_Type = CfprFsmFlags
_CfprSwAccessDomainFsmTaskFlags_Object = MibTableColumn
cfprSwAccessDomainFsmTaskFlags = _CfprSwAccessDomainFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4, 1, 5),
    _CfprSwAccessDomainFsmTaskFlags_Type()
)
cfprSwAccessDomainFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskFlags.setStatus("current")
_CfprSwAccessDomainFsmTaskItem_Type = CfprSwAccessDomainFsmTaskItem
_CfprSwAccessDomainFsmTaskItem_Object = MibTableColumn
cfprSwAccessDomainFsmTaskItem = _CfprSwAccessDomainFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4, 1, 6),
    _CfprSwAccessDomainFsmTaskItem_Type()
)
cfprSwAccessDomainFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskItem.setStatus("current")
_CfprSwAccessDomainFsmTaskSeqId_Type = Gauge32
_CfprSwAccessDomainFsmTaskSeqId_Object = MibTableColumn
cfprSwAccessDomainFsmTaskSeqId = _CfprSwAccessDomainFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 4, 1, 7),
    _CfprSwAccessDomainFsmTaskSeqId_Type()
)
cfprSwAccessDomainFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessDomainFsmTaskSeqId.setStatus("current")
_CfprSwAccessEpTable_Object = MibTable
cfprSwAccessEpTable = _CfprSwAccessEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5)
)
if mibBuilder.loadTexts:
    cfprSwAccessEpTable.setStatus("current")
_CfprSwAccessEpEntry_Object = MibTableRow
cfprSwAccessEpEntry = _CfprSwAccessEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1)
)
cfprSwAccessEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwAccessEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwAccessEpEntry.setStatus("current")
_CfprSwAccessEpInstanceId_Type = CfprManagedObjectId
_CfprSwAccessEpInstanceId_Object = MibTableColumn
cfprSwAccessEpInstanceId = _CfprSwAccessEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 1),
    _CfprSwAccessEpInstanceId_Type()
)
cfprSwAccessEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwAccessEpInstanceId.setStatus("current")
_CfprSwAccessEpDn_Type = CfprManagedObjectDn
_CfprSwAccessEpDn_Object = MibTableColumn
cfprSwAccessEpDn = _CfprSwAccessEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 2),
    _CfprSwAccessEpDn_Type()
)
cfprSwAccessEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpDn.setStatus("current")
_CfprSwAccessEpRn_Type = SnmpAdminString
_CfprSwAccessEpRn_Object = MibTableColumn
cfprSwAccessEpRn = _CfprSwAccessEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 3),
    _CfprSwAccessEpRn_Type()
)
cfprSwAccessEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpRn.setStatus("current")
_CfprSwAccessEpAdminState_Type = CfprFabricAdminState
_CfprSwAccessEpAdminState_Object = MibTableColumn
cfprSwAccessEpAdminState = _CfprSwAccessEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 4),
    _CfprSwAccessEpAdminState_Type()
)
cfprSwAccessEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpAdminState.setStatus("current")
_CfprSwAccessEpAggrPortId_Type = Gauge32
_CfprSwAccessEpAggrPortId_Object = MibTableColumn
cfprSwAccessEpAggrPortId = _CfprSwAccessEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 5),
    _CfprSwAccessEpAggrPortId_Type()
)
cfprSwAccessEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpAggrPortId.setStatus("current")
_CfprSwAccessEpChassisId_Type = Gauge32
_CfprSwAccessEpChassisId_Object = MibTableColumn
cfprSwAccessEpChassisId = _CfprSwAccessEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 6),
    _CfprSwAccessEpChassisId_Type()
)
cfprSwAccessEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpChassisId.setStatus("current")
_CfprSwAccessEpEncap_Type = Gauge32
_CfprSwAccessEpEncap_Object = MibTableColumn
cfprSwAccessEpEncap = _CfprSwAccessEpEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 7),
    _CfprSwAccessEpEncap_Type()
)
cfprSwAccessEpEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpEncap.setStatus("current")
_CfprSwAccessEpEpDn_Type = SnmpAdminString
_CfprSwAccessEpEpDn_Object = MibTableColumn
cfprSwAccessEpEpDn = _CfprSwAccessEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 8),
    _CfprSwAccessEpEpDn_Type()
)
cfprSwAccessEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpEpDn.setStatus("current")
_CfprSwAccessEpIfRole_Type = CfprNetworkPortRole
_CfprSwAccessEpIfRole_Object = MibTableColumn
cfprSwAccessEpIfRole = _CfprSwAccessEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 9),
    _CfprSwAccessEpIfRole_Type()
)
cfprSwAccessEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpIfRole.setStatus("current")
_CfprSwAccessEpIfType_Type = CfprSwPIoEpIfType
_CfprSwAccessEpIfType_Object = MibTableColumn
cfprSwAccessEpIfType = _CfprSwAccessEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 10),
    _CfprSwAccessEpIfType_Type()
)
cfprSwAccessEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpIfType.setStatus("current")
_CfprSwAccessEpLc_Type = CfprSwPIoEpLc
_CfprSwAccessEpLc_Object = MibTableColumn
cfprSwAccessEpLc = _CfprSwAccessEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 11),
    _CfprSwAccessEpLc_Type()
)
cfprSwAccessEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpLc.setStatus("current")
_CfprSwAccessEpLocale_Type = CfprSwAccessEpLocale
_CfprSwAccessEpLocale_Object = MibTableColumn
cfprSwAccessEpLocale = _CfprSwAccessEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 12),
    _CfprSwAccessEpLocale_Type()
)
cfprSwAccessEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpLocale.setStatus("current")
_CfprSwAccessEpName_Type = SnmpAdminString
_CfprSwAccessEpName_Object = MibTableColumn
cfprSwAccessEpName = _CfprSwAccessEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 13),
    _CfprSwAccessEpName_Type()
)
cfprSwAccessEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpName.setStatus("current")
_CfprSwAccessEpNsSize_Type = Gauge32
_CfprSwAccessEpNsSize_Object = MibTableColumn
cfprSwAccessEpNsSize = _CfprSwAccessEpNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 14),
    _CfprSwAccessEpNsSize_Type()
)
cfprSwAccessEpNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpNsSize.setStatus("current")
_CfprSwAccessEpPeerAggrPortId_Type = Gauge32
_CfprSwAccessEpPeerAggrPortId_Object = MibTableColumn
cfprSwAccessEpPeerAggrPortId = _CfprSwAccessEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 15),
    _CfprSwAccessEpPeerAggrPortId_Type()
)
cfprSwAccessEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpPeerAggrPortId.setStatus("current")
_CfprSwAccessEpPeerChassisId_Type = Gauge32
_CfprSwAccessEpPeerChassisId_Object = MibTableColumn
cfprSwAccessEpPeerChassisId = _CfprSwAccessEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 16),
    _CfprSwAccessEpPeerChassisId_Type()
)
cfprSwAccessEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpPeerChassisId.setStatus("current")
_CfprSwAccessEpPeerDn_Type = SnmpAdminString
_CfprSwAccessEpPeerDn_Object = MibTableColumn
cfprSwAccessEpPeerDn = _CfprSwAccessEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 17),
    _CfprSwAccessEpPeerDn_Type()
)
cfprSwAccessEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpPeerDn.setStatus("current")
_CfprSwAccessEpPeerPortId_Type = Gauge32
_CfprSwAccessEpPeerPortId_Object = MibTableColumn
cfprSwAccessEpPeerPortId = _CfprSwAccessEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 18),
    _CfprSwAccessEpPeerPortId_Type()
)
cfprSwAccessEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpPeerPortId.setStatus("current")
_CfprSwAccessEpPeerSlotId_Type = Gauge32
_CfprSwAccessEpPeerSlotId_Object = MibTableColumn
cfprSwAccessEpPeerSlotId = _CfprSwAccessEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 19),
    _CfprSwAccessEpPeerSlotId_Type()
)
cfprSwAccessEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpPeerSlotId.setStatus("current")
_CfprSwAccessEpPortId_Type = Gauge32
_CfprSwAccessEpPortId_Object = MibTableColumn
cfprSwAccessEpPortId = _CfprSwAccessEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 20),
    _CfprSwAccessEpPortId_Type()
)
cfprSwAccessEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpPortId.setStatus("current")
_CfprSwAccessEpSlotId_Type = Gauge32
_CfprSwAccessEpSlotId_Object = MibTableColumn
cfprSwAccessEpSlotId = _CfprSwAccessEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 21),
    _CfprSwAccessEpSlotId_Type()
)
cfprSwAccessEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpSlotId.setStatus("current")
_CfprSwAccessEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwAccessEpSwitchId_Object = MibTableColumn
cfprSwAccessEpSwitchId = _CfprSwAccessEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 22),
    _CfprSwAccessEpSwitchId_Type()
)
cfprSwAccessEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpSwitchId.setStatus("current")
_CfprSwAccessEpTransport_Type = CfprSwAccessEpTransport
_CfprSwAccessEpTransport_Object = MibTableColumn
cfprSwAccessEpTransport = _CfprSwAccessEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 23),
    _CfprSwAccessEpTransport_Type()
)
cfprSwAccessEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpTransport.setStatus("current")
_CfprSwAccessEpType_Type = CfprNetworkConnectionType
_CfprSwAccessEpType_Object = MibTableColumn
cfprSwAccessEpType = _CfprSwAccessEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 5, 1, 24),
    _CfprSwAccessEpType_Type()
)
cfprSwAccessEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwAccessEpType.setStatus("current")
_CfprSwCardEnvStatsTable_Object = MibTable
cfprSwCardEnvStatsTable = _CfprSwCardEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6)
)
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsTable.setStatus("current")
_CfprSwCardEnvStatsEntry_Object = MibTableRow
cfprSwCardEnvStatsEntry = _CfprSwCardEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1)
)
cfprSwCardEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwCardEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsEntry.setStatus("current")
_CfprSwCardEnvStatsInstanceId_Type = CfprManagedObjectId
_CfprSwCardEnvStatsInstanceId_Object = MibTableColumn
cfprSwCardEnvStatsInstanceId = _CfprSwCardEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 1),
    _CfprSwCardEnvStatsInstanceId_Type()
)
cfprSwCardEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsInstanceId.setStatus("current")
_CfprSwCardEnvStatsDn_Type = CfprManagedObjectDn
_CfprSwCardEnvStatsDn_Object = MibTableColumn
cfprSwCardEnvStatsDn = _CfprSwCardEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 2),
    _CfprSwCardEnvStatsDn_Type()
)
cfprSwCardEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsDn.setStatus("current")
_CfprSwCardEnvStatsRn_Type = SnmpAdminString
_CfprSwCardEnvStatsRn_Object = MibTableColumn
cfprSwCardEnvStatsRn = _CfprSwCardEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 3),
    _CfprSwCardEnvStatsRn_Type()
)
cfprSwCardEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsRn.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet1_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet1_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet1 = _CfprSwCardEnvStatsSlotOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 4),
    _CfprSwCardEnvStatsSlotOutlet1_Type()
)
cfprSwCardEnvStatsSlotOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet1.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet1Avg_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet1Avg_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet1Avg = _CfprSwCardEnvStatsSlotOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 5),
    _CfprSwCardEnvStatsSlotOutlet1Avg_Type()
)
cfprSwCardEnvStatsSlotOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet1Avg.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet1Max_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet1Max_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet1Max = _CfprSwCardEnvStatsSlotOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 6),
    _CfprSwCardEnvStatsSlotOutlet1Max_Type()
)
cfprSwCardEnvStatsSlotOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet1Max.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet1Min_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet1Min_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet1Min = _CfprSwCardEnvStatsSlotOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 7),
    _CfprSwCardEnvStatsSlotOutlet1Min_Type()
)
cfprSwCardEnvStatsSlotOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet1Min.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet2_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet2_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet2 = _CfprSwCardEnvStatsSlotOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 8),
    _CfprSwCardEnvStatsSlotOutlet2_Type()
)
cfprSwCardEnvStatsSlotOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet2.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet2Avg_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet2Avg_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet2Avg = _CfprSwCardEnvStatsSlotOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 9),
    _CfprSwCardEnvStatsSlotOutlet2Avg_Type()
)
cfprSwCardEnvStatsSlotOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet2Avg.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet2Max_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet2Max_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet2Max = _CfprSwCardEnvStatsSlotOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 10),
    _CfprSwCardEnvStatsSlotOutlet2Max_Type()
)
cfprSwCardEnvStatsSlotOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet2Max.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet2Min_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet2Min_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet2Min = _CfprSwCardEnvStatsSlotOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 11),
    _CfprSwCardEnvStatsSlotOutlet2Min_Type()
)
cfprSwCardEnvStatsSlotOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet2Min.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet3_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet3_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet3 = _CfprSwCardEnvStatsSlotOutlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 12),
    _CfprSwCardEnvStatsSlotOutlet3_Type()
)
cfprSwCardEnvStatsSlotOutlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet3.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet3Avg_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet3Avg_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet3Avg = _CfprSwCardEnvStatsSlotOutlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 13),
    _CfprSwCardEnvStatsSlotOutlet3Avg_Type()
)
cfprSwCardEnvStatsSlotOutlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet3Avg.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet3Max_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet3Max_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet3Max = _CfprSwCardEnvStatsSlotOutlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 14),
    _CfprSwCardEnvStatsSlotOutlet3Max_Type()
)
cfprSwCardEnvStatsSlotOutlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet3Max.setStatus("current")
_CfprSwCardEnvStatsSlotOutlet3Min_Type = Integer32
_CfprSwCardEnvStatsSlotOutlet3Min_Object = MibTableColumn
cfprSwCardEnvStatsSlotOutlet3Min = _CfprSwCardEnvStatsSlotOutlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 15),
    _CfprSwCardEnvStatsSlotOutlet3Min_Type()
)
cfprSwCardEnvStatsSlotOutlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSlotOutlet3Min.setStatus("current")
_CfprSwCardEnvStatsIntervals_Type = Gauge32
_CfprSwCardEnvStatsIntervals_Object = MibTableColumn
cfprSwCardEnvStatsIntervals = _CfprSwCardEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 16),
    _CfprSwCardEnvStatsIntervals_Type()
)
cfprSwCardEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsIntervals.setStatus("current")
_CfprSwCardEnvStatsSuspect_Type = TruthValue
_CfprSwCardEnvStatsSuspect_Object = MibTableColumn
cfprSwCardEnvStatsSuspect = _CfprSwCardEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 17),
    _CfprSwCardEnvStatsSuspect_Type()
)
cfprSwCardEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsSuspect.setStatus("current")
_CfprSwCardEnvStatsThresholded_Type = CfprSwCardEnvStatsThresholded
_CfprSwCardEnvStatsThresholded_Object = MibTableColumn
cfprSwCardEnvStatsThresholded = _CfprSwCardEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 18),
    _CfprSwCardEnvStatsThresholded_Type()
)
cfprSwCardEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsThresholded.setStatus("current")
_CfprSwCardEnvStatsTimeCollected_Type = DateAndTime
_CfprSwCardEnvStatsTimeCollected_Object = MibTableColumn
cfprSwCardEnvStatsTimeCollected = _CfprSwCardEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 19),
    _CfprSwCardEnvStatsTimeCollected_Type()
)
cfprSwCardEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsTimeCollected.setStatus("current")
_CfprSwCardEnvStatsUpdate_Type = Gauge32
_CfprSwCardEnvStatsUpdate_Object = MibTableColumn
cfprSwCardEnvStatsUpdate = _CfprSwCardEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 6, 1, 20),
    _CfprSwCardEnvStatsUpdate_Type()
)
cfprSwCardEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsUpdate.setStatus("current")
_CfprSwCardEnvStatsHistTable_Object = MibTable
cfprSwCardEnvStatsHistTable = _CfprSwCardEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7)
)
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistTable.setStatus("current")
_CfprSwCardEnvStatsHistEntry_Object = MibTableRow
cfprSwCardEnvStatsHistEntry = _CfprSwCardEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1)
)
cfprSwCardEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwCardEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistEntry.setStatus("current")
_CfprSwCardEnvStatsHistInstanceId_Type = CfprManagedObjectId
_CfprSwCardEnvStatsHistInstanceId_Object = MibTableColumn
cfprSwCardEnvStatsHistInstanceId = _CfprSwCardEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 1),
    _CfprSwCardEnvStatsHistInstanceId_Type()
)
cfprSwCardEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistInstanceId.setStatus("current")
_CfprSwCardEnvStatsHistDn_Type = CfprManagedObjectDn
_CfprSwCardEnvStatsHistDn_Object = MibTableColumn
cfprSwCardEnvStatsHistDn = _CfprSwCardEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 2),
    _CfprSwCardEnvStatsHistDn_Type()
)
cfprSwCardEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistDn.setStatus("current")
_CfprSwCardEnvStatsHistRn_Type = SnmpAdminString
_CfprSwCardEnvStatsHistRn_Object = MibTableColumn
cfprSwCardEnvStatsHistRn = _CfprSwCardEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 3),
    _CfprSwCardEnvStatsHistRn_Type()
)
cfprSwCardEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistRn.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet1_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet1_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet1 = _CfprSwCardEnvStatsHistSlotOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 4),
    _CfprSwCardEnvStatsHistSlotOutlet1_Type()
)
cfprSwCardEnvStatsHistSlotOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet1.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet1Avg_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet1Avg_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet1Avg = _CfprSwCardEnvStatsHistSlotOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 5),
    _CfprSwCardEnvStatsHistSlotOutlet1Avg_Type()
)
cfprSwCardEnvStatsHistSlotOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet1Avg.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet1Max_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet1Max_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet1Max = _CfprSwCardEnvStatsHistSlotOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 6),
    _CfprSwCardEnvStatsHistSlotOutlet1Max_Type()
)
cfprSwCardEnvStatsHistSlotOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet1Max.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet1Min_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet1Min_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet1Min = _CfprSwCardEnvStatsHistSlotOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 7),
    _CfprSwCardEnvStatsHistSlotOutlet1Min_Type()
)
cfprSwCardEnvStatsHistSlotOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet1Min.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet2_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet2_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet2 = _CfprSwCardEnvStatsHistSlotOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 8),
    _CfprSwCardEnvStatsHistSlotOutlet2_Type()
)
cfprSwCardEnvStatsHistSlotOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet2.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet2Avg_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet2Avg_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet2Avg = _CfprSwCardEnvStatsHistSlotOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 9),
    _CfprSwCardEnvStatsHistSlotOutlet2Avg_Type()
)
cfprSwCardEnvStatsHistSlotOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet2Avg.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet2Max_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet2Max_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet2Max = _CfprSwCardEnvStatsHistSlotOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 10),
    _CfprSwCardEnvStatsHistSlotOutlet2Max_Type()
)
cfprSwCardEnvStatsHistSlotOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet2Max.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet2Min_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet2Min_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet2Min = _CfprSwCardEnvStatsHistSlotOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 11),
    _CfprSwCardEnvStatsHistSlotOutlet2Min_Type()
)
cfprSwCardEnvStatsHistSlotOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet2Min.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet3_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet3_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet3 = _CfprSwCardEnvStatsHistSlotOutlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 12),
    _CfprSwCardEnvStatsHistSlotOutlet3_Type()
)
cfprSwCardEnvStatsHistSlotOutlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet3.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet3Avg_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet3Avg_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet3Avg = _CfprSwCardEnvStatsHistSlotOutlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 13),
    _CfprSwCardEnvStatsHistSlotOutlet3Avg_Type()
)
cfprSwCardEnvStatsHistSlotOutlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet3Avg.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet3Max_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet3Max_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet3Max = _CfprSwCardEnvStatsHistSlotOutlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 14),
    _CfprSwCardEnvStatsHistSlotOutlet3Max_Type()
)
cfprSwCardEnvStatsHistSlotOutlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet3Max.setStatus("current")
_CfprSwCardEnvStatsHistSlotOutlet3Min_Type = Integer32
_CfprSwCardEnvStatsHistSlotOutlet3Min_Object = MibTableColumn
cfprSwCardEnvStatsHistSlotOutlet3Min = _CfprSwCardEnvStatsHistSlotOutlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 15),
    _CfprSwCardEnvStatsHistSlotOutlet3Min_Type()
)
cfprSwCardEnvStatsHistSlotOutlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSlotOutlet3Min.setStatus("current")
_CfprSwCardEnvStatsHistId_Type = Unsigned64
_CfprSwCardEnvStatsHistId_Object = MibTableColumn
cfprSwCardEnvStatsHistId = _CfprSwCardEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 16),
    _CfprSwCardEnvStatsHistId_Type()
)
cfprSwCardEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistId.setStatus("current")
_CfprSwCardEnvStatsHistMostRecent_Type = TruthValue
_CfprSwCardEnvStatsHistMostRecent_Object = MibTableColumn
cfprSwCardEnvStatsHistMostRecent = _CfprSwCardEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 17),
    _CfprSwCardEnvStatsHistMostRecent_Type()
)
cfprSwCardEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistMostRecent.setStatus("current")
_CfprSwCardEnvStatsHistSuspect_Type = TruthValue
_CfprSwCardEnvStatsHistSuspect_Object = MibTableColumn
cfprSwCardEnvStatsHistSuspect = _CfprSwCardEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 18),
    _CfprSwCardEnvStatsHistSuspect_Type()
)
cfprSwCardEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistSuspect.setStatus("current")
_CfprSwCardEnvStatsHistThresholded_Type = CfprSwCardEnvStatsHistThresholded
_CfprSwCardEnvStatsHistThresholded_Object = MibTableColumn
cfprSwCardEnvStatsHistThresholded = _CfprSwCardEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 19),
    _CfprSwCardEnvStatsHistThresholded_Type()
)
cfprSwCardEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistThresholded.setStatus("current")
_CfprSwCardEnvStatsHistTimeCollected_Type = DateAndTime
_CfprSwCardEnvStatsHistTimeCollected_Object = MibTableColumn
cfprSwCardEnvStatsHistTimeCollected = _CfprSwCardEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 7, 1, 20),
    _CfprSwCardEnvStatsHistTimeCollected_Type()
)
cfprSwCardEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCardEnvStatsHistTimeCollected.setStatus("current")
_CfprSwCmclanTable_Object = MibTable
cfprSwCmclanTable = _CfprSwCmclanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8)
)
if mibBuilder.loadTexts:
    cfprSwCmclanTable.setStatus("current")
_CfprSwCmclanEntry_Object = MibTableRow
cfprSwCmclanEntry = _CfprSwCmclanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1)
)
cfprSwCmclanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwCmclanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwCmclanEntry.setStatus("current")
_CfprSwCmclanInstanceId_Type = CfprManagedObjectId
_CfprSwCmclanInstanceId_Object = MibTableColumn
cfprSwCmclanInstanceId = _CfprSwCmclanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 1),
    _CfprSwCmclanInstanceId_Type()
)
cfprSwCmclanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwCmclanInstanceId.setStatus("current")
_CfprSwCmclanDn_Type = CfprManagedObjectDn
_CfprSwCmclanDn_Object = MibTableColumn
cfprSwCmclanDn = _CfprSwCmclanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 2),
    _CfprSwCmclanDn_Type()
)
cfprSwCmclanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanDn.setStatus("current")
_CfprSwCmclanRn_Type = SnmpAdminString
_CfprSwCmclanRn_Object = MibTableColumn
cfprSwCmclanRn = _CfprSwCmclanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 3),
    _CfprSwCmclanRn_Type()
)
cfprSwCmclanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanRn.setStatus("current")
_CfprSwCmclanCimcIds_Type = CfprSwCimcId
_CfprSwCmclanCimcIds_Object = MibTableColumn
cfprSwCmclanCimcIds = _CfprSwCmclanCimcIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 4),
    _CfprSwCmclanCimcIds_Type()
)
cfprSwCmclanCimcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanCimcIds.setStatus("current")
_CfprSwCmclanEpDn_Type = SnmpAdminString
_CfprSwCmclanEpDn_Object = MibTableColumn
cfprSwCmclanEpDn = _CfprSwCmclanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 5),
    _CfprSwCmclanEpDn_Type()
)
cfprSwCmclanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanEpDn.setStatus("current")
_CfprSwCmclanId_Type = Gauge32
_CfprSwCmclanId_Object = MibTableColumn
cfprSwCmclanId = _CfprSwCmclanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 6),
    _CfprSwCmclanId_Type()
)
cfprSwCmclanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanId.setStatus("current")
_CfprSwCmclanIfRole_Type = CfprNetworkPortRole
_CfprSwCmclanIfRole_Object = MibTableColumn
cfprSwCmclanIfRole = _CfprSwCmclanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 7),
    _CfprSwCmclanIfRole_Type()
)
cfprSwCmclanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanIfRole.setStatus("current")
_CfprSwCmclanIfType_Type = CfprNetworkVnetEpIfType
_CfprSwCmclanIfType_Object = MibTableColumn
cfprSwCmclanIfType = _CfprSwCmclanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 8),
    _CfprSwCmclanIfType_Type()
)
cfprSwCmclanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanIfType.setStatus("current")
_CfprSwCmclanLocale_Type = CfprNetworkLocale
_CfprSwCmclanLocale_Object = MibTableColumn
cfprSwCmclanLocale = _CfprSwCmclanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 9),
    _CfprSwCmclanLocale_Type()
)
cfprSwCmclanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanLocale.setStatus("current")
_CfprSwCmclanName_Type = SnmpAdminString
_CfprSwCmclanName_Object = MibTableColumn
cfprSwCmclanName = _CfprSwCmclanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 10),
    _CfprSwCmclanName_Type()
)
cfprSwCmclanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanName.setStatus("current")
_CfprSwCmclanPeerDn_Type = SnmpAdminString
_CfprSwCmclanPeerDn_Object = MibTableColumn
cfprSwCmclanPeerDn = _CfprSwCmclanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 11),
    _CfprSwCmclanPeerDn_Type()
)
cfprSwCmclanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanPeerDn.setStatus("current")
_CfprSwCmclanTransport_Type = CfprNetworkTransport
_CfprSwCmclanTransport_Object = MibTableColumn
cfprSwCmclanTransport = _CfprSwCmclanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 12),
    _CfprSwCmclanTransport_Type()
)
cfprSwCmclanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanTransport.setStatus("current")
_CfprSwCmclanType_Type = CfprNetworkConnectionType
_CfprSwCmclanType_Object = MibTableColumn
cfprSwCmclanType = _CfprSwCmclanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 8, 1, 13),
    _CfprSwCmclanType_Type()
)
cfprSwCmclanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwCmclanType.setStatus("current")
_CfprSwEnvStatsTable_Object = MibTable
cfprSwEnvStatsTable = _CfprSwEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9)
)
if mibBuilder.loadTexts:
    cfprSwEnvStatsTable.setStatus("current")
_CfprSwEnvStatsEntry_Object = MibTableRow
cfprSwEnvStatsEntry = _CfprSwEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1)
)
cfprSwEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEnvStatsEntry.setStatus("current")
_CfprSwEnvStatsInstanceId_Type = CfprManagedObjectId
_CfprSwEnvStatsInstanceId_Object = MibTableColumn
cfprSwEnvStatsInstanceId = _CfprSwEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 1),
    _CfprSwEnvStatsInstanceId_Type()
)
cfprSwEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEnvStatsInstanceId.setStatus("current")
_CfprSwEnvStatsDn_Type = CfprManagedObjectDn
_CfprSwEnvStatsDn_Object = MibTableColumn
cfprSwEnvStatsDn = _CfprSwEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 2),
    _CfprSwEnvStatsDn_Type()
)
cfprSwEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsDn.setStatus("current")
_CfprSwEnvStatsRn_Type = SnmpAdminString
_CfprSwEnvStatsRn_Object = MibTableColumn
cfprSwEnvStatsRn = _CfprSwEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 3),
    _CfprSwEnvStatsRn_Type()
)
cfprSwEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsRn.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet1_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet1_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet1 = _CfprSwEnvStatsFanCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 4),
    _CfprSwEnvStatsFanCtrlrInlet1_Type()
)
cfprSwEnvStatsFanCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet1.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet1Avg_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet1Avg_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet1Avg = _CfprSwEnvStatsFanCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 5),
    _CfprSwEnvStatsFanCtrlrInlet1Avg_Type()
)
cfprSwEnvStatsFanCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet1Avg.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet1Max_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet1Max_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet1Max = _CfprSwEnvStatsFanCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 6),
    _CfprSwEnvStatsFanCtrlrInlet1Max_Type()
)
cfprSwEnvStatsFanCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet1Max.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet1Min_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet1Min_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet1Min = _CfprSwEnvStatsFanCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 7),
    _CfprSwEnvStatsFanCtrlrInlet1Min_Type()
)
cfprSwEnvStatsFanCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet1Min.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet2_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet2_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet2 = _CfprSwEnvStatsFanCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 8),
    _CfprSwEnvStatsFanCtrlrInlet2_Type()
)
cfprSwEnvStatsFanCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet2.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet2Avg_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet2Avg_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet2Avg = _CfprSwEnvStatsFanCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 9),
    _CfprSwEnvStatsFanCtrlrInlet2Avg_Type()
)
cfprSwEnvStatsFanCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet2Avg.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet2Max_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet2Max_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet2Max = _CfprSwEnvStatsFanCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 10),
    _CfprSwEnvStatsFanCtrlrInlet2Max_Type()
)
cfprSwEnvStatsFanCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet2Max.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet2Min_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet2Min_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet2Min = _CfprSwEnvStatsFanCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 11),
    _CfprSwEnvStatsFanCtrlrInlet2Min_Type()
)
cfprSwEnvStatsFanCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet2Min.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet3_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet3_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet3 = _CfprSwEnvStatsFanCtrlrInlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 12),
    _CfprSwEnvStatsFanCtrlrInlet3_Type()
)
cfprSwEnvStatsFanCtrlrInlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet3.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet3Avg_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet3Avg_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet3Avg = _CfprSwEnvStatsFanCtrlrInlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 13),
    _CfprSwEnvStatsFanCtrlrInlet3Avg_Type()
)
cfprSwEnvStatsFanCtrlrInlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet3Avg.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet3Max_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet3Max_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet3Max = _CfprSwEnvStatsFanCtrlrInlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 14),
    _CfprSwEnvStatsFanCtrlrInlet3Max_Type()
)
cfprSwEnvStatsFanCtrlrInlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet3Max.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet3Min_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet3Min_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet3Min = _CfprSwEnvStatsFanCtrlrInlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 15),
    _CfprSwEnvStatsFanCtrlrInlet3Min_Type()
)
cfprSwEnvStatsFanCtrlrInlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet3Min.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet4_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet4_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet4 = _CfprSwEnvStatsFanCtrlrInlet4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 16),
    _CfprSwEnvStatsFanCtrlrInlet4_Type()
)
cfprSwEnvStatsFanCtrlrInlet4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet4.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet4Avg_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet4Avg_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet4Avg = _CfprSwEnvStatsFanCtrlrInlet4Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 17),
    _CfprSwEnvStatsFanCtrlrInlet4Avg_Type()
)
cfprSwEnvStatsFanCtrlrInlet4Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet4Avg.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet4Max_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet4Max_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet4Max = _CfprSwEnvStatsFanCtrlrInlet4Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 18),
    _CfprSwEnvStatsFanCtrlrInlet4Max_Type()
)
cfprSwEnvStatsFanCtrlrInlet4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet4Max.setStatus("current")
_CfprSwEnvStatsFanCtrlrInlet4Min_Type = Integer32
_CfprSwEnvStatsFanCtrlrInlet4Min_Object = MibTableColumn
cfprSwEnvStatsFanCtrlrInlet4Min = _CfprSwEnvStatsFanCtrlrInlet4Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 19),
    _CfprSwEnvStatsFanCtrlrInlet4Min_Type()
)
cfprSwEnvStatsFanCtrlrInlet4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsFanCtrlrInlet4Min.setStatus("current")
_CfprSwEnvStatsIntervals_Type = Gauge32
_CfprSwEnvStatsIntervals_Object = MibTableColumn
cfprSwEnvStatsIntervals = _CfprSwEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 20),
    _CfprSwEnvStatsIntervals_Type()
)
cfprSwEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsIntervals.setStatus("current")
_CfprSwEnvStatsMainBoardOutlet1_Type = Integer32
_CfprSwEnvStatsMainBoardOutlet1_Object = MibTableColumn
cfprSwEnvStatsMainBoardOutlet1 = _CfprSwEnvStatsMainBoardOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 21),
    _CfprSwEnvStatsMainBoardOutlet1_Type()
)
cfprSwEnvStatsMainBoardOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsMainBoardOutlet1.setStatus("current")
_CfprSwEnvStatsMainBoardOutlet1Avg_Type = Integer32
_CfprSwEnvStatsMainBoardOutlet1Avg_Object = MibTableColumn
cfprSwEnvStatsMainBoardOutlet1Avg = _CfprSwEnvStatsMainBoardOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 22),
    _CfprSwEnvStatsMainBoardOutlet1Avg_Type()
)
cfprSwEnvStatsMainBoardOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsMainBoardOutlet1Avg.setStatus("current")
_CfprSwEnvStatsMainBoardOutlet1Max_Type = Integer32
_CfprSwEnvStatsMainBoardOutlet1Max_Object = MibTableColumn
cfprSwEnvStatsMainBoardOutlet1Max = _CfprSwEnvStatsMainBoardOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 23),
    _CfprSwEnvStatsMainBoardOutlet1Max_Type()
)
cfprSwEnvStatsMainBoardOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsMainBoardOutlet1Max.setStatus("current")
_CfprSwEnvStatsMainBoardOutlet1Min_Type = Integer32
_CfprSwEnvStatsMainBoardOutlet1Min_Object = MibTableColumn
cfprSwEnvStatsMainBoardOutlet1Min = _CfprSwEnvStatsMainBoardOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 24),
    _CfprSwEnvStatsMainBoardOutlet1Min_Type()
)
cfprSwEnvStatsMainBoardOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsMainBoardOutlet1Min.setStatus("current")
_CfprSwEnvStatsMainBoardOutlet2_Type = Integer32
_CfprSwEnvStatsMainBoardOutlet2_Object = MibTableColumn
cfprSwEnvStatsMainBoardOutlet2 = _CfprSwEnvStatsMainBoardOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 25),
    _CfprSwEnvStatsMainBoardOutlet2_Type()
)
cfprSwEnvStatsMainBoardOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsMainBoardOutlet2.setStatus("current")
_CfprSwEnvStatsMainBoardOutlet2Avg_Type = Integer32
_CfprSwEnvStatsMainBoardOutlet2Avg_Object = MibTableColumn
cfprSwEnvStatsMainBoardOutlet2Avg = _CfprSwEnvStatsMainBoardOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 26),
    _CfprSwEnvStatsMainBoardOutlet2Avg_Type()
)
cfprSwEnvStatsMainBoardOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsMainBoardOutlet2Avg.setStatus("current")
_CfprSwEnvStatsMainBoardOutlet2Max_Type = Integer32
_CfprSwEnvStatsMainBoardOutlet2Max_Object = MibTableColumn
cfprSwEnvStatsMainBoardOutlet2Max = _CfprSwEnvStatsMainBoardOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 27),
    _CfprSwEnvStatsMainBoardOutlet2Max_Type()
)
cfprSwEnvStatsMainBoardOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsMainBoardOutlet2Max.setStatus("current")
_CfprSwEnvStatsMainBoardOutlet2Min_Type = Integer32
_CfprSwEnvStatsMainBoardOutlet2Min_Object = MibTableColumn
cfprSwEnvStatsMainBoardOutlet2Min = _CfprSwEnvStatsMainBoardOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 28),
    _CfprSwEnvStatsMainBoardOutlet2Min_Type()
)
cfprSwEnvStatsMainBoardOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsMainBoardOutlet2Min.setStatus("current")
_CfprSwEnvStatsPsuCtrlrInlet1_Type = Integer32
_CfprSwEnvStatsPsuCtrlrInlet1_Object = MibTableColumn
cfprSwEnvStatsPsuCtrlrInlet1 = _CfprSwEnvStatsPsuCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 29),
    _CfprSwEnvStatsPsuCtrlrInlet1_Type()
)
cfprSwEnvStatsPsuCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsPsuCtrlrInlet1.setStatus("current")
_CfprSwEnvStatsPsuCtrlrInlet1Avg_Type = Integer32
_CfprSwEnvStatsPsuCtrlrInlet1Avg_Object = MibTableColumn
cfprSwEnvStatsPsuCtrlrInlet1Avg = _CfprSwEnvStatsPsuCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 30),
    _CfprSwEnvStatsPsuCtrlrInlet1Avg_Type()
)
cfprSwEnvStatsPsuCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsPsuCtrlrInlet1Avg.setStatus("current")
_CfprSwEnvStatsPsuCtrlrInlet1Max_Type = Integer32
_CfprSwEnvStatsPsuCtrlrInlet1Max_Object = MibTableColumn
cfprSwEnvStatsPsuCtrlrInlet1Max = _CfprSwEnvStatsPsuCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 31),
    _CfprSwEnvStatsPsuCtrlrInlet1Max_Type()
)
cfprSwEnvStatsPsuCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsPsuCtrlrInlet1Max.setStatus("current")
_CfprSwEnvStatsPsuCtrlrInlet1Min_Type = Integer32
_CfprSwEnvStatsPsuCtrlrInlet1Min_Object = MibTableColumn
cfprSwEnvStatsPsuCtrlrInlet1Min = _CfprSwEnvStatsPsuCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 32),
    _CfprSwEnvStatsPsuCtrlrInlet1Min_Type()
)
cfprSwEnvStatsPsuCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsPsuCtrlrInlet1Min.setStatus("current")
_CfprSwEnvStatsPsuCtrlrInlet2_Type = Integer32
_CfprSwEnvStatsPsuCtrlrInlet2_Object = MibTableColumn
cfprSwEnvStatsPsuCtrlrInlet2 = _CfprSwEnvStatsPsuCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 33),
    _CfprSwEnvStatsPsuCtrlrInlet2_Type()
)
cfprSwEnvStatsPsuCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsPsuCtrlrInlet2.setStatus("current")
_CfprSwEnvStatsPsuCtrlrInlet2Avg_Type = Integer32
_CfprSwEnvStatsPsuCtrlrInlet2Avg_Object = MibTableColumn
cfprSwEnvStatsPsuCtrlrInlet2Avg = _CfprSwEnvStatsPsuCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 34),
    _CfprSwEnvStatsPsuCtrlrInlet2Avg_Type()
)
cfprSwEnvStatsPsuCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsPsuCtrlrInlet2Avg.setStatus("current")
_CfprSwEnvStatsPsuCtrlrInlet2Max_Type = Integer32
_CfprSwEnvStatsPsuCtrlrInlet2Max_Object = MibTableColumn
cfprSwEnvStatsPsuCtrlrInlet2Max = _CfprSwEnvStatsPsuCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 35),
    _CfprSwEnvStatsPsuCtrlrInlet2Max_Type()
)
cfprSwEnvStatsPsuCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsPsuCtrlrInlet2Max.setStatus("current")
_CfprSwEnvStatsPsuCtrlrInlet2Min_Type = Integer32
_CfprSwEnvStatsPsuCtrlrInlet2Min_Object = MibTableColumn
cfprSwEnvStatsPsuCtrlrInlet2Min = _CfprSwEnvStatsPsuCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 36),
    _CfprSwEnvStatsPsuCtrlrInlet2Min_Type()
)
cfprSwEnvStatsPsuCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsPsuCtrlrInlet2Min.setStatus("current")
_CfprSwEnvStatsSuspect_Type = TruthValue
_CfprSwEnvStatsSuspect_Object = MibTableColumn
cfprSwEnvStatsSuspect = _CfprSwEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 37),
    _CfprSwEnvStatsSuspect_Type()
)
cfprSwEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsSuspect.setStatus("current")
_CfprSwEnvStatsThresholded_Type = CfprSwEnvStatsThresholded
_CfprSwEnvStatsThresholded_Object = MibTableColumn
cfprSwEnvStatsThresholded = _CfprSwEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 38),
    _CfprSwEnvStatsThresholded_Type()
)
cfprSwEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsThresholded.setStatus("current")
_CfprSwEnvStatsTimeCollected_Type = DateAndTime
_CfprSwEnvStatsTimeCollected_Object = MibTableColumn
cfprSwEnvStatsTimeCollected = _CfprSwEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 39),
    _CfprSwEnvStatsTimeCollected_Type()
)
cfprSwEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsTimeCollected.setStatus("current")
_CfprSwEnvStatsUpdate_Type = Gauge32
_CfprSwEnvStatsUpdate_Object = MibTableColumn
cfprSwEnvStatsUpdate = _CfprSwEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 9, 1, 40),
    _CfprSwEnvStatsUpdate_Type()
)
cfprSwEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsUpdate.setStatus("current")
_CfprSwEnvStatsHistTable_Object = MibTable
cfprSwEnvStatsHistTable = _CfprSwEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10)
)
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistTable.setStatus("current")
_CfprSwEnvStatsHistEntry_Object = MibTableRow
cfprSwEnvStatsHistEntry = _CfprSwEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1)
)
cfprSwEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistEntry.setStatus("current")
_CfprSwEnvStatsHistInstanceId_Type = CfprManagedObjectId
_CfprSwEnvStatsHistInstanceId_Object = MibTableColumn
cfprSwEnvStatsHistInstanceId = _CfprSwEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 1),
    _CfprSwEnvStatsHistInstanceId_Type()
)
cfprSwEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistInstanceId.setStatus("current")
_CfprSwEnvStatsHistDn_Type = CfprManagedObjectDn
_CfprSwEnvStatsHistDn_Object = MibTableColumn
cfprSwEnvStatsHistDn = _CfprSwEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 2),
    _CfprSwEnvStatsHistDn_Type()
)
cfprSwEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistDn.setStatus("current")
_CfprSwEnvStatsHistRn_Type = SnmpAdminString
_CfprSwEnvStatsHistRn_Object = MibTableColumn
cfprSwEnvStatsHistRn = _CfprSwEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 3),
    _CfprSwEnvStatsHistRn_Type()
)
cfprSwEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistRn.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet1_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet1_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet1 = _CfprSwEnvStatsHistFanCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 4),
    _CfprSwEnvStatsHistFanCtrlrInlet1_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet1.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet1Avg_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet1Avg_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet1Avg = _CfprSwEnvStatsHistFanCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 5),
    _CfprSwEnvStatsHistFanCtrlrInlet1Avg_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet1Avg.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet1Max_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet1Max_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet1Max = _CfprSwEnvStatsHistFanCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 6),
    _CfprSwEnvStatsHistFanCtrlrInlet1Max_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet1Max.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet1Min_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet1Min_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet1Min = _CfprSwEnvStatsHistFanCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 7),
    _CfprSwEnvStatsHistFanCtrlrInlet1Min_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet1Min.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet2_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet2_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet2 = _CfprSwEnvStatsHistFanCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 8),
    _CfprSwEnvStatsHistFanCtrlrInlet2_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet2.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet2Avg_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet2Avg_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet2Avg = _CfprSwEnvStatsHistFanCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 9),
    _CfprSwEnvStatsHistFanCtrlrInlet2Avg_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet2Avg.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet2Max_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet2Max_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet2Max = _CfprSwEnvStatsHistFanCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 10),
    _CfprSwEnvStatsHistFanCtrlrInlet2Max_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet2Max.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet2Min_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet2Min_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet2Min = _CfprSwEnvStatsHistFanCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 11),
    _CfprSwEnvStatsHistFanCtrlrInlet2Min_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet2Min.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet3_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet3_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet3 = _CfprSwEnvStatsHistFanCtrlrInlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 12),
    _CfprSwEnvStatsHistFanCtrlrInlet3_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet3.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet3Avg_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet3Avg_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet3Avg = _CfprSwEnvStatsHistFanCtrlrInlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 13),
    _CfprSwEnvStatsHistFanCtrlrInlet3Avg_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet3Avg.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet3Max_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet3Max_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet3Max = _CfprSwEnvStatsHistFanCtrlrInlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 14),
    _CfprSwEnvStatsHistFanCtrlrInlet3Max_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet3Max.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet3Min_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet3Min_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet3Min = _CfprSwEnvStatsHistFanCtrlrInlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 15),
    _CfprSwEnvStatsHistFanCtrlrInlet3Min_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet3Min.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet4_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet4_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet4 = _CfprSwEnvStatsHistFanCtrlrInlet4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 16),
    _CfprSwEnvStatsHistFanCtrlrInlet4_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet4.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet4Avg_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet4Avg_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet4Avg = _CfprSwEnvStatsHistFanCtrlrInlet4Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 17),
    _CfprSwEnvStatsHistFanCtrlrInlet4Avg_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet4Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet4Avg.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet4Max_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet4Max_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet4Max = _CfprSwEnvStatsHistFanCtrlrInlet4Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 18),
    _CfprSwEnvStatsHistFanCtrlrInlet4Max_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet4Max.setStatus("current")
_CfprSwEnvStatsHistFanCtrlrInlet4Min_Type = Integer32
_CfprSwEnvStatsHistFanCtrlrInlet4Min_Object = MibTableColumn
cfprSwEnvStatsHistFanCtrlrInlet4Min = _CfprSwEnvStatsHistFanCtrlrInlet4Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 19),
    _CfprSwEnvStatsHistFanCtrlrInlet4Min_Type()
)
cfprSwEnvStatsHistFanCtrlrInlet4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistFanCtrlrInlet4Min.setStatus("current")
_CfprSwEnvStatsHistId_Type = Unsigned64
_CfprSwEnvStatsHistId_Object = MibTableColumn
cfprSwEnvStatsHistId = _CfprSwEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 20),
    _CfprSwEnvStatsHistId_Type()
)
cfprSwEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistId.setStatus("current")
_CfprSwEnvStatsHistMainBoardOutlet1_Type = Integer32
_CfprSwEnvStatsHistMainBoardOutlet1_Object = MibTableColumn
cfprSwEnvStatsHistMainBoardOutlet1 = _CfprSwEnvStatsHistMainBoardOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 21),
    _CfprSwEnvStatsHistMainBoardOutlet1_Type()
)
cfprSwEnvStatsHistMainBoardOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMainBoardOutlet1.setStatus("current")
_CfprSwEnvStatsHistMainBoardOutlet1Avg_Type = Integer32
_CfprSwEnvStatsHistMainBoardOutlet1Avg_Object = MibTableColumn
cfprSwEnvStatsHistMainBoardOutlet1Avg = _CfprSwEnvStatsHistMainBoardOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 22),
    _CfprSwEnvStatsHistMainBoardOutlet1Avg_Type()
)
cfprSwEnvStatsHistMainBoardOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMainBoardOutlet1Avg.setStatus("current")
_CfprSwEnvStatsHistMainBoardOutlet1Max_Type = Integer32
_CfprSwEnvStatsHistMainBoardOutlet1Max_Object = MibTableColumn
cfprSwEnvStatsHistMainBoardOutlet1Max = _CfprSwEnvStatsHistMainBoardOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 23),
    _CfprSwEnvStatsHistMainBoardOutlet1Max_Type()
)
cfprSwEnvStatsHistMainBoardOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMainBoardOutlet1Max.setStatus("current")
_CfprSwEnvStatsHistMainBoardOutlet1Min_Type = Integer32
_CfprSwEnvStatsHistMainBoardOutlet1Min_Object = MibTableColumn
cfprSwEnvStatsHistMainBoardOutlet1Min = _CfprSwEnvStatsHistMainBoardOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 24),
    _CfprSwEnvStatsHistMainBoardOutlet1Min_Type()
)
cfprSwEnvStatsHistMainBoardOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMainBoardOutlet1Min.setStatus("current")
_CfprSwEnvStatsHistMainBoardOutlet2_Type = Integer32
_CfprSwEnvStatsHistMainBoardOutlet2_Object = MibTableColumn
cfprSwEnvStatsHistMainBoardOutlet2 = _CfprSwEnvStatsHistMainBoardOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 25),
    _CfprSwEnvStatsHistMainBoardOutlet2_Type()
)
cfprSwEnvStatsHistMainBoardOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMainBoardOutlet2.setStatus("current")
_CfprSwEnvStatsHistMainBoardOutlet2Avg_Type = Integer32
_CfprSwEnvStatsHistMainBoardOutlet2Avg_Object = MibTableColumn
cfprSwEnvStatsHistMainBoardOutlet2Avg = _CfprSwEnvStatsHistMainBoardOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 26),
    _CfprSwEnvStatsHistMainBoardOutlet2Avg_Type()
)
cfprSwEnvStatsHistMainBoardOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMainBoardOutlet2Avg.setStatus("current")
_CfprSwEnvStatsHistMainBoardOutlet2Max_Type = Integer32
_CfprSwEnvStatsHistMainBoardOutlet2Max_Object = MibTableColumn
cfprSwEnvStatsHistMainBoardOutlet2Max = _CfprSwEnvStatsHistMainBoardOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 27),
    _CfprSwEnvStatsHistMainBoardOutlet2Max_Type()
)
cfprSwEnvStatsHistMainBoardOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMainBoardOutlet2Max.setStatus("current")
_CfprSwEnvStatsHistMainBoardOutlet2Min_Type = Integer32
_CfprSwEnvStatsHistMainBoardOutlet2Min_Object = MibTableColumn
cfprSwEnvStatsHistMainBoardOutlet2Min = _CfprSwEnvStatsHistMainBoardOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 28),
    _CfprSwEnvStatsHistMainBoardOutlet2Min_Type()
)
cfprSwEnvStatsHistMainBoardOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMainBoardOutlet2Min.setStatus("current")
_CfprSwEnvStatsHistMostRecent_Type = TruthValue
_CfprSwEnvStatsHistMostRecent_Object = MibTableColumn
cfprSwEnvStatsHistMostRecent = _CfprSwEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 29),
    _CfprSwEnvStatsHistMostRecent_Type()
)
cfprSwEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistMostRecent.setStatus("current")
_CfprSwEnvStatsHistPsuCtrlrInlet1_Type = Integer32
_CfprSwEnvStatsHistPsuCtrlrInlet1_Object = MibTableColumn
cfprSwEnvStatsHistPsuCtrlrInlet1 = _CfprSwEnvStatsHistPsuCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 30),
    _CfprSwEnvStatsHistPsuCtrlrInlet1_Type()
)
cfprSwEnvStatsHistPsuCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistPsuCtrlrInlet1.setStatus("current")
_CfprSwEnvStatsHistPsuCtrlrInlet1Avg_Type = Integer32
_CfprSwEnvStatsHistPsuCtrlrInlet1Avg_Object = MibTableColumn
cfprSwEnvStatsHistPsuCtrlrInlet1Avg = _CfprSwEnvStatsHistPsuCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 31),
    _CfprSwEnvStatsHistPsuCtrlrInlet1Avg_Type()
)
cfprSwEnvStatsHistPsuCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistPsuCtrlrInlet1Avg.setStatus("current")
_CfprSwEnvStatsHistPsuCtrlrInlet1Max_Type = Integer32
_CfprSwEnvStatsHistPsuCtrlrInlet1Max_Object = MibTableColumn
cfprSwEnvStatsHistPsuCtrlrInlet1Max = _CfprSwEnvStatsHistPsuCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 32),
    _CfprSwEnvStatsHistPsuCtrlrInlet1Max_Type()
)
cfprSwEnvStatsHistPsuCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistPsuCtrlrInlet1Max.setStatus("current")
_CfprSwEnvStatsHistPsuCtrlrInlet1Min_Type = Integer32
_CfprSwEnvStatsHistPsuCtrlrInlet1Min_Object = MibTableColumn
cfprSwEnvStatsHistPsuCtrlrInlet1Min = _CfprSwEnvStatsHistPsuCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 33),
    _CfprSwEnvStatsHistPsuCtrlrInlet1Min_Type()
)
cfprSwEnvStatsHistPsuCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistPsuCtrlrInlet1Min.setStatus("current")
_CfprSwEnvStatsHistPsuCtrlrInlet2_Type = Integer32
_CfprSwEnvStatsHistPsuCtrlrInlet2_Object = MibTableColumn
cfprSwEnvStatsHistPsuCtrlrInlet2 = _CfprSwEnvStatsHistPsuCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 34),
    _CfprSwEnvStatsHistPsuCtrlrInlet2_Type()
)
cfprSwEnvStatsHistPsuCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistPsuCtrlrInlet2.setStatus("current")
_CfprSwEnvStatsHistPsuCtrlrInlet2Avg_Type = Integer32
_CfprSwEnvStatsHistPsuCtrlrInlet2Avg_Object = MibTableColumn
cfprSwEnvStatsHistPsuCtrlrInlet2Avg = _CfprSwEnvStatsHistPsuCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 35),
    _CfprSwEnvStatsHistPsuCtrlrInlet2Avg_Type()
)
cfprSwEnvStatsHistPsuCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistPsuCtrlrInlet2Avg.setStatus("current")
_CfprSwEnvStatsHistPsuCtrlrInlet2Max_Type = Integer32
_CfprSwEnvStatsHistPsuCtrlrInlet2Max_Object = MibTableColumn
cfprSwEnvStatsHistPsuCtrlrInlet2Max = _CfprSwEnvStatsHistPsuCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 36),
    _CfprSwEnvStatsHistPsuCtrlrInlet2Max_Type()
)
cfprSwEnvStatsHistPsuCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistPsuCtrlrInlet2Max.setStatus("current")
_CfprSwEnvStatsHistPsuCtrlrInlet2Min_Type = Integer32
_CfprSwEnvStatsHistPsuCtrlrInlet2Min_Object = MibTableColumn
cfprSwEnvStatsHistPsuCtrlrInlet2Min = _CfprSwEnvStatsHistPsuCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 37),
    _CfprSwEnvStatsHistPsuCtrlrInlet2Min_Type()
)
cfprSwEnvStatsHistPsuCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistPsuCtrlrInlet2Min.setStatus("current")
_CfprSwEnvStatsHistSuspect_Type = TruthValue
_CfprSwEnvStatsHistSuspect_Object = MibTableColumn
cfprSwEnvStatsHistSuspect = _CfprSwEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 38),
    _CfprSwEnvStatsHistSuspect_Type()
)
cfprSwEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistSuspect.setStatus("current")
_CfprSwEnvStatsHistThresholded_Type = CfprSwEnvStatsHistThresholded
_CfprSwEnvStatsHistThresholded_Object = MibTableColumn
cfprSwEnvStatsHistThresholded = _CfprSwEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 39),
    _CfprSwEnvStatsHistThresholded_Type()
)
cfprSwEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistThresholded.setStatus("current")
_CfprSwEnvStatsHistTimeCollected_Type = DateAndTime
_CfprSwEnvStatsHistTimeCollected_Object = MibTableColumn
cfprSwEnvStatsHistTimeCollected = _CfprSwEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 10, 1, 40),
    _CfprSwEnvStatsHistTimeCollected_Type()
)
cfprSwEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEnvStatsHistTimeCollected.setStatus("current")
_CfprSwEthEstcEpTable_Object = MibTable
cfprSwEthEstcEpTable = _CfprSwEthEstcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11)
)
if mibBuilder.loadTexts:
    cfprSwEthEstcEpTable.setStatus("current")
_CfprSwEthEstcEpEntry_Object = MibTableRow
cfprSwEthEstcEpEntry = _CfprSwEthEstcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1)
)
cfprSwEthEstcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthEstcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthEstcEpEntry.setStatus("current")
_CfprSwEthEstcEpInstanceId_Type = CfprManagedObjectId
_CfprSwEthEstcEpInstanceId_Object = MibTableColumn
cfprSwEthEstcEpInstanceId = _CfprSwEthEstcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 1),
    _CfprSwEthEstcEpInstanceId_Type()
)
cfprSwEthEstcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpInstanceId.setStatus("current")
_CfprSwEthEstcEpDn_Type = CfprManagedObjectDn
_CfprSwEthEstcEpDn_Object = MibTableColumn
cfprSwEthEstcEpDn = _CfprSwEthEstcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 2),
    _CfprSwEthEstcEpDn_Type()
)
cfprSwEthEstcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpDn.setStatus("current")
_CfprSwEthEstcEpRn_Type = SnmpAdminString
_CfprSwEthEstcEpRn_Object = MibTableColumn
cfprSwEthEstcEpRn = _CfprSwEthEstcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 3),
    _CfprSwEthEstcEpRn_Type()
)
cfprSwEthEstcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpRn.setStatus("current")
_CfprSwEthEstcEpAdminSpeed_Type = CfprPortEthSpeed
_CfprSwEthEstcEpAdminSpeed_Object = MibTableColumn
cfprSwEthEstcEpAdminSpeed = _CfprSwEthEstcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 4),
    _CfprSwEthEstcEpAdminSpeed_Type()
)
cfprSwEthEstcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpAdminSpeed.setStatus("current")
_CfprSwEthEstcEpAdminState_Type = CfprFabricAdminState
_CfprSwEthEstcEpAdminState_Object = MibTableColumn
cfprSwEthEstcEpAdminState = _CfprSwEthEstcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 5),
    _CfprSwEthEstcEpAdminState_Type()
)
cfprSwEthEstcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpAdminState.setStatus("current")
_CfprSwEthEstcEpAggrPortId_Type = Gauge32
_CfprSwEthEstcEpAggrPortId_Object = MibTableColumn
cfprSwEthEstcEpAggrPortId = _CfprSwEthEstcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 6),
    _CfprSwEthEstcEpAggrPortId_Type()
)
cfprSwEthEstcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpAggrPortId.setStatus("current")
_CfprSwEthEstcEpBorderAggrPortId_Type = Gauge32
_CfprSwEthEstcEpBorderAggrPortId_Object = MibTableColumn
cfprSwEthEstcEpBorderAggrPortId = _CfprSwEthEstcEpBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 7),
    _CfprSwEthEstcEpBorderAggrPortId_Type()
)
cfprSwEthEstcEpBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpBorderAggrPortId.setStatus("current")
_CfprSwEthEstcEpBorderPortId_Type = Gauge32
_CfprSwEthEstcEpBorderPortId_Object = MibTableColumn
cfprSwEthEstcEpBorderPortId = _CfprSwEthEstcEpBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 8),
    _CfprSwEthEstcEpBorderPortId_Type()
)
cfprSwEthEstcEpBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpBorderPortId.setStatus("current")
_CfprSwEthEstcEpBorderSlotId_Type = Gauge32
_CfprSwEthEstcEpBorderSlotId_Object = MibTableColumn
cfprSwEthEstcEpBorderSlotId = _CfprSwEthEstcEpBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 9),
    _CfprSwEthEstcEpBorderSlotId_Type()
)
cfprSwEthEstcEpBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpBorderSlotId.setStatus("current")
_CfprSwEthEstcEpCdp_Type = CfprNwctrlAdminState
_CfprSwEthEstcEpCdp_Object = MibTableColumn
cfprSwEthEstcEpCdp = _CfprSwEthEstcEpCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 10),
    _CfprSwEthEstcEpCdp_Type()
)
cfprSwEthEstcEpCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpCdp.setStatus("current")
_CfprSwEthEstcEpChassisId_Type = Gauge32
_CfprSwEthEstcEpChassisId_Object = MibTableColumn
cfprSwEthEstcEpChassisId = _CfprSwEthEstcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 11),
    _CfprSwEthEstcEpChassisId_Type()
)
cfprSwEthEstcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpChassisId.setStatus("current")
_CfprSwEthEstcEpCosValue_Type = Gauge32
_CfprSwEthEstcEpCosValue_Object = MibTableColumn
cfprSwEthEstcEpCosValue = _CfprSwEthEstcEpCosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 12),
    _CfprSwEthEstcEpCosValue_Type()
)
cfprSwEthEstcEpCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpCosValue.setStatus("current")
_CfprSwEthEstcEpEpDn_Type = SnmpAdminString
_CfprSwEthEstcEpEpDn_Object = MibTableColumn
cfprSwEthEstcEpEpDn = _CfprSwEthEstcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 13),
    _CfprSwEthEstcEpEpDn_Type()
)
cfprSwEthEstcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpEpDn.setStatus("current")
_CfprSwEthEstcEpForgeMac_Type = CfprDpsecForgedTransmit
_CfprSwEthEstcEpForgeMac_Object = MibTableColumn
cfprSwEthEstcEpForgeMac = _CfprSwEthEstcEpForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 14),
    _CfprSwEthEstcEpForgeMac_Type()
)
cfprSwEthEstcEpForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpForgeMac.setStatus("current")
_CfprSwEthEstcEpIfRole_Type = CfprNetworkPortRole
_CfprSwEthEstcEpIfRole_Object = MibTableColumn
cfprSwEthEstcEpIfRole = _CfprSwEthEstcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 15),
    _CfprSwEthEstcEpIfRole_Type()
)
cfprSwEthEstcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpIfRole.setStatus("current")
_CfprSwEthEstcEpIfType_Type = CfprSwPIoEpIfType
_CfprSwEthEstcEpIfType_Object = MibTableColumn
cfprSwEthEstcEpIfType = _CfprSwEthEstcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 16),
    _CfprSwEthEstcEpIfType_Type()
)
cfprSwEthEstcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpIfType.setStatus("current")
_CfprSwEthEstcEpLc_Type = CfprSwPIoEpLc
_CfprSwEthEstcEpLc_Object = MibTableColumn
cfprSwEthEstcEpLc = _CfprSwEthEstcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 17),
    _CfprSwEthEstcEpLc_Type()
)
cfprSwEthEstcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpLc.setStatus("current")
_CfprSwEthEstcEpLocale_Type = CfprSwEstcEpLocale
_CfprSwEthEstcEpLocale_Object = MibTableColumn
cfprSwEthEstcEpLocale = _CfprSwEthEstcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 18),
    _CfprSwEthEstcEpLocale_Type()
)
cfprSwEthEstcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpLocale.setStatus("current")
_CfprSwEthEstcEpName_Type = SnmpAdminString
_CfprSwEthEstcEpName_Object = MibTableColumn
cfprSwEthEstcEpName = _CfprSwEthEstcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 19),
    _CfprSwEthEstcEpName_Type()
)
cfprSwEthEstcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpName.setStatus("current")
_CfprSwEthEstcEpPcId_Type = Gauge32
_CfprSwEthEstcEpPcId_Object = MibTableColumn
cfprSwEthEstcEpPcId = _CfprSwEthEstcEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 20),
    _CfprSwEthEstcEpPcId_Type()
)
cfprSwEthEstcEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPcId.setStatus("current")
_CfprSwEthEstcEpPeerAggrPortId_Type = Gauge32
_CfprSwEthEstcEpPeerAggrPortId_Object = MibTableColumn
cfprSwEthEstcEpPeerAggrPortId = _CfprSwEthEstcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 21),
    _CfprSwEthEstcEpPeerAggrPortId_Type()
)
cfprSwEthEstcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPeerAggrPortId.setStatus("current")
_CfprSwEthEstcEpPeerChassisId_Type = Gauge32
_CfprSwEthEstcEpPeerChassisId_Object = MibTableColumn
cfprSwEthEstcEpPeerChassisId = _CfprSwEthEstcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 22),
    _CfprSwEthEstcEpPeerChassisId_Type()
)
cfprSwEthEstcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPeerChassisId.setStatus("current")
_CfprSwEthEstcEpPeerDn_Type = SnmpAdminString
_CfprSwEthEstcEpPeerDn_Object = MibTableColumn
cfprSwEthEstcEpPeerDn = _CfprSwEthEstcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 23),
    _CfprSwEthEstcEpPeerDn_Type()
)
cfprSwEthEstcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPeerDn.setStatus("current")
_CfprSwEthEstcEpPeerPortId_Type = Gauge32
_CfprSwEthEstcEpPeerPortId_Object = MibTableColumn
cfprSwEthEstcEpPeerPortId = _CfprSwEthEstcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 24),
    _CfprSwEthEstcEpPeerPortId_Type()
)
cfprSwEthEstcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPeerPortId.setStatus("current")
_CfprSwEthEstcEpPeerSlotId_Type = Gauge32
_CfprSwEthEstcEpPeerSlotId_Object = MibTableColumn
cfprSwEthEstcEpPeerSlotId = _CfprSwEthEstcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 25),
    _CfprSwEthEstcEpPeerSlotId_Type()
)
cfprSwEthEstcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPeerSlotId.setStatus("current")
_CfprSwEthEstcEpPinGroupName_Type = SnmpAdminString
_CfprSwEthEstcEpPinGroupName_Object = MibTableColumn
cfprSwEthEstcEpPinGroupName = _CfprSwEthEstcEpPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 26),
    _CfprSwEthEstcEpPinGroupName_Type()
)
cfprSwEthEstcEpPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPinGroupName.setStatus("current")
_CfprSwEthEstcEpPortId_Type = Gauge32
_CfprSwEthEstcEpPortId_Object = MibTableColumn
cfprSwEthEstcEpPortId = _CfprSwEthEstcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 27),
    _CfprSwEthEstcEpPortId_Type()
)
cfprSwEthEstcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPortId.setStatus("current")
_CfprSwEthEstcEpPortMode_Type = CfprFabricEthEstcPortMode
_CfprSwEthEstcEpPortMode_Object = MibTableColumn
cfprSwEthEstcEpPortMode = _CfprSwEthEstcEpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 28),
    _CfprSwEthEstcEpPortMode_Type()
)
cfprSwEthEstcEpPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPortMode.setStatus("current")
_CfprSwEthEstcEpPriorityFlowCtrl_Type = CfprFlowctrlPriorityPause
_CfprSwEthEstcEpPriorityFlowCtrl_Object = MibTableColumn
cfprSwEthEstcEpPriorityFlowCtrl = _CfprSwEthEstcEpPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 29),
    _CfprSwEthEstcEpPriorityFlowCtrl_Type()
)
cfprSwEthEstcEpPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpPriorityFlowCtrl.setStatus("current")
_CfprSwEthEstcEpRecvFlowCtrl_Type = CfprFlowctrlFlowControlRx
_CfprSwEthEstcEpRecvFlowCtrl_Object = MibTableColumn
cfprSwEthEstcEpRecvFlowCtrl = _CfprSwEthEstcEpRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 30),
    _CfprSwEthEstcEpRecvFlowCtrl_Type()
)
cfprSwEthEstcEpRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpRecvFlowCtrl.setStatus("current")
_CfprSwEthEstcEpSendFlowCtrl_Type = CfprFlowctrlFlowControlTx
_CfprSwEthEstcEpSendFlowCtrl_Object = MibTableColumn
cfprSwEthEstcEpSendFlowCtrl = _CfprSwEthEstcEpSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 31),
    _CfprSwEthEstcEpSendFlowCtrl_Type()
)
cfprSwEthEstcEpSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpSendFlowCtrl.setStatus("current")
_CfprSwEthEstcEpSlotId_Type = Gauge32
_CfprSwEthEstcEpSlotId_Object = MibTableColumn
cfprSwEthEstcEpSlotId = _CfprSwEthEstcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 32),
    _CfprSwEthEstcEpSlotId_Type()
)
cfprSwEthEstcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpSlotId.setStatus("current")
_CfprSwEthEstcEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthEstcEpSwitchId_Object = MibTableColumn
cfprSwEthEstcEpSwitchId = _CfprSwEthEstcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 33),
    _CfprSwEthEstcEpSwitchId_Type()
)
cfprSwEthEstcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpSwitchId.setStatus("current")
_CfprSwEthEstcEpTransport_Type = CfprSwEthEstcEpTransport
_CfprSwEthEstcEpTransport_Object = MibTableColumn
cfprSwEthEstcEpTransport = _CfprSwEthEstcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 34),
    _CfprSwEthEstcEpTransport_Type()
)
cfprSwEthEstcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpTransport.setStatus("current")
_CfprSwEthEstcEpType_Type = CfprNetworkConnectionType
_CfprSwEthEstcEpType_Object = MibTableColumn
cfprSwEthEstcEpType = _CfprSwEthEstcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 35),
    _CfprSwEthEstcEpType_Type()
)
cfprSwEthEstcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpType.setStatus("current")
_CfprSwEthEstcEpUplinkFailAction_Type = CfprNwctrlLinkFailAction
_CfprSwEthEstcEpUplinkFailAction_Object = MibTableColumn
cfprSwEthEstcEpUplinkFailAction = _CfprSwEthEstcEpUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 11, 1, 36),
    _CfprSwEthEstcEpUplinkFailAction_Type()
)
cfprSwEthEstcEpUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcEpUplinkFailAction.setStatus("current")
_CfprSwEthEstcPcTable_Object = MibTable
cfprSwEthEstcPcTable = _CfprSwEthEstcPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12)
)
if mibBuilder.loadTexts:
    cfprSwEthEstcPcTable.setStatus("current")
_CfprSwEthEstcPcEntry_Object = MibTableRow
cfprSwEthEstcPcEntry = _CfprSwEthEstcPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1)
)
cfprSwEthEstcPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthEstcPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthEstcPcEntry.setStatus("current")
_CfprSwEthEstcPcInstanceId_Type = CfprManagedObjectId
_CfprSwEthEstcPcInstanceId_Object = MibTableColumn
cfprSwEthEstcPcInstanceId = _CfprSwEthEstcPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 1),
    _CfprSwEthEstcPcInstanceId_Type()
)
cfprSwEthEstcPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcInstanceId.setStatus("current")
_CfprSwEthEstcPcDn_Type = CfprManagedObjectDn
_CfprSwEthEstcPcDn_Object = MibTableColumn
cfprSwEthEstcPcDn = _CfprSwEthEstcPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 2),
    _CfprSwEthEstcPcDn_Type()
)
cfprSwEthEstcPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcDn.setStatus("current")
_CfprSwEthEstcPcRn_Type = SnmpAdminString
_CfprSwEthEstcPcRn_Object = MibTableColumn
cfprSwEthEstcPcRn = _CfprSwEthEstcPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 3),
    _CfprSwEthEstcPcRn_Type()
)
cfprSwEthEstcPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcRn.setStatus("current")
_CfprSwEthEstcPcAdminSpeed_Type = CfprPortEthSpeed
_CfprSwEthEstcPcAdminSpeed_Object = MibTableColumn
cfprSwEthEstcPcAdminSpeed = _CfprSwEthEstcPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 4),
    _CfprSwEthEstcPcAdminSpeed_Type()
)
cfprSwEthEstcPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcAdminSpeed.setStatus("current")
_CfprSwEthEstcPcAdminState_Type = CfprFabricAdminState
_CfprSwEthEstcPcAdminState_Object = MibTableColumn
cfprSwEthEstcPcAdminState = _CfprSwEthEstcPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 5),
    _CfprSwEthEstcPcAdminState_Type()
)
cfprSwEthEstcPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcAdminState.setStatus("current")
_CfprSwEthEstcPcBorderAggrPortId_Type = Gauge32
_CfprSwEthEstcPcBorderAggrPortId_Object = MibTableColumn
cfprSwEthEstcPcBorderAggrPortId = _CfprSwEthEstcPcBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 6),
    _CfprSwEthEstcPcBorderAggrPortId_Type()
)
cfprSwEthEstcPcBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcBorderAggrPortId.setStatus("current")
_CfprSwEthEstcPcBorderPortId_Type = Gauge32
_CfprSwEthEstcPcBorderPortId_Object = MibTableColumn
cfprSwEthEstcPcBorderPortId = _CfprSwEthEstcPcBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 7),
    _CfprSwEthEstcPcBorderPortId_Type()
)
cfprSwEthEstcPcBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcBorderPortId.setStatus("current")
_CfprSwEthEstcPcBorderSlotId_Type = Gauge32
_CfprSwEthEstcPcBorderSlotId_Object = MibTableColumn
cfprSwEthEstcPcBorderSlotId = _CfprSwEthEstcPcBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 8),
    _CfprSwEthEstcPcBorderSlotId_Type()
)
cfprSwEthEstcPcBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcBorderSlotId.setStatus("current")
_CfprSwEthEstcPcCdp_Type = CfprNwctrlAdminState
_CfprSwEthEstcPcCdp_Object = MibTableColumn
cfprSwEthEstcPcCdp = _CfprSwEthEstcPcCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 9),
    _CfprSwEthEstcPcCdp_Type()
)
cfprSwEthEstcPcCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcCdp.setStatus("current")
_CfprSwEthEstcPcCosValue_Type = Gauge32
_CfprSwEthEstcPcCosValue_Object = MibTableColumn
cfprSwEthEstcPcCosValue = _CfprSwEthEstcPcCosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 10),
    _CfprSwEthEstcPcCosValue_Type()
)
cfprSwEthEstcPcCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcCosValue.setStatus("current")
_CfprSwEthEstcPcEpDn_Type = SnmpAdminString
_CfprSwEthEstcPcEpDn_Object = MibTableColumn
cfprSwEthEstcPcEpDn = _CfprSwEthEstcPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 11),
    _CfprSwEthEstcPcEpDn_Type()
)
cfprSwEthEstcPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcEpDn.setStatus("current")
_CfprSwEthEstcPcForgeMac_Type = CfprDpsecForgedTransmit
_CfprSwEthEstcPcForgeMac_Object = MibTableColumn
cfprSwEthEstcPcForgeMac = _CfprSwEthEstcPcForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 12),
    _CfprSwEthEstcPcForgeMac_Type()
)
cfprSwEthEstcPcForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcForgeMac.setStatus("current")
_CfprSwEthEstcPcIfRole_Type = CfprSwLanPcIfRole
_CfprSwEthEstcPcIfRole_Object = MibTableColumn
cfprSwEthEstcPcIfRole = _CfprSwEthEstcPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 13),
    _CfprSwEthEstcPcIfRole_Type()
)
cfprSwEthEstcPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcIfRole.setStatus("current")
_CfprSwEthEstcPcIfType_Type = CfprSwCIoEpIfType
_CfprSwEthEstcPcIfType_Object = MibTableColumn
cfprSwEthEstcPcIfType = _CfprSwEthEstcPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 14),
    _CfprSwEthEstcPcIfType_Type()
)
cfprSwEthEstcPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcIfType.setStatus("current")
_CfprSwEthEstcPcLacpFastTimer_Type = TruthValue
_CfprSwEthEstcPcLacpFastTimer_Object = MibTableColumn
cfprSwEthEstcPcLacpFastTimer = _CfprSwEthEstcPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 15),
    _CfprSwEthEstcPcLacpFastTimer_Type()
)
cfprSwEthEstcPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcLacpFastTimer.setStatus("current")
_CfprSwEthEstcPcLacpSuspendIndividual_Type = TruthValue
_CfprSwEthEstcPcLacpSuspendIndividual_Object = MibTableColumn
cfprSwEthEstcPcLacpSuspendIndividual = _CfprSwEthEstcPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 16),
    _CfprSwEthEstcPcLacpSuspendIndividual_Type()
)
cfprSwEthEstcPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcLacpSuspendIndividual.setStatus("current")
_CfprSwEthEstcPcLocale_Type = CfprSwBorderPcLocale
_CfprSwEthEstcPcLocale_Object = MibTableColumn
cfprSwEthEstcPcLocale = _CfprSwEthEstcPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 17),
    _CfprSwEthEstcPcLocale_Type()
)
cfprSwEthEstcPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcLocale.setStatus("current")
_CfprSwEthEstcPcMonTrafDir_Type = CfprFabricTrafficDirection
_CfprSwEthEstcPcMonTrafDir_Object = MibTableColumn
cfprSwEthEstcPcMonTrafDir = _CfprSwEthEstcPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 18),
    _CfprSwEthEstcPcMonTrafDir_Type()
)
cfprSwEthEstcPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcMonTrafDir.setStatus("current")
_CfprSwEthEstcPcName_Type = SnmpAdminString
_CfprSwEthEstcPcName_Object = MibTableColumn
cfprSwEthEstcPcName = _CfprSwEthEstcPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 19),
    _CfprSwEthEstcPcName_Type()
)
cfprSwEthEstcPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcName.setStatus("current")
_CfprSwEthEstcPcPeerDn_Type = SnmpAdminString
_CfprSwEthEstcPcPeerDn_Object = MibTableColumn
cfprSwEthEstcPcPeerDn = _CfprSwEthEstcPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 20),
    _CfprSwEthEstcPcPeerDn_Type()
)
cfprSwEthEstcPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcPeerDn.setStatus("current")
_CfprSwEthEstcPcPortId_Type = Gauge32
_CfprSwEthEstcPcPortId_Object = MibTableColumn
cfprSwEthEstcPcPortId = _CfprSwEthEstcPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 21),
    _CfprSwEthEstcPcPortId_Type()
)
cfprSwEthEstcPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcPortId.setStatus("current")
_CfprSwEthEstcPcPortMode_Type = CfprFabricEthEstcPortMode
_CfprSwEthEstcPcPortMode_Object = MibTableColumn
cfprSwEthEstcPcPortMode = _CfprSwEthEstcPcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 22),
    _CfprSwEthEstcPcPortMode_Type()
)
cfprSwEthEstcPcPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcPortMode.setStatus("current")
_CfprSwEthEstcPcPriorityFlowCtrl_Type = CfprFlowctrlPriorityPause
_CfprSwEthEstcPcPriorityFlowCtrl_Object = MibTableColumn
cfprSwEthEstcPcPriorityFlowCtrl = _CfprSwEthEstcPcPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 23),
    _CfprSwEthEstcPcPriorityFlowCtrl_Type()
)
cfprSwEthEstcPcPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcPriorityFlowCtrl.setStatus("current")
_CfprSwEthEstcPcProtocol_Type = CfprFabricEthPcProtocol
_CfprSwEthEstcPcProtocol_Object = MibTableColumn
cfprSwEthEstcPcProtocol = _CfprSwEthEstcPcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 24),
    _CfprSwEthEstcPcProtocol_Type()
)
cfprSwEthEstcPcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcProtocol.setStatus("current")
_CfprSwEthEstcPcRecvFlowCtrl_Type = CfprFlowctrlFlowControlRx
_CfprSwEthEstcPcRecvFlowCtrl_Object = MibTableColumn
cfprSwEthEstcPcRecvFlowCtrl = _CfprSwEthEstcPcRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 25),
    _CfprSwEthEstcPcRecvFlowCtrl_Type()
)
cfprSwEthEstcPcRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcRecvFlowCtrl.setStatus("current")
_CfprSwEthEstcPcSendFlowCtrl_Type = CfprFlowctrlFlowControlTx
_CfprSwEthEstcPcSendFlowCtrl_Object = MibTableColumn
cfprSwEthEstcPcSendFlowCtrl = _CfprSwEthEstcPcSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 26),
    _CfprSwEthEstcPcSendFlowCtrl_Type()
)
cfprSwEthEstcPcSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcSendFlowCtrl.setStatus("current")
_CfprSwEthEstcPcSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthEstcPcSwitchId_Object = MibTableColumn
cfprSwEthEstcPcSwitchId = _CfprSwEthEstcPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 27),
    _CfprSwEthEstcPcSwitchId_Type()
)
cfprSwEthEstcPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcSwitchId.setStatus("current")
_CfprSwEthEstcPcTransport_Type = CfprSwEthEstcPcTransport
_CfprSwEthEstcPcTransport_Object = MibTableColumn
cfprSwEthEstcPcTransport = _CfprSwEthEstcPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 28),
    _CfprSwEthEstcPcTransport_Type()
)
cfprSwEthEstcPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcTransport.setStatus("current")
_CfprSwEthEstcPcType_Type = CfprSwLanPcType
_CfprSwEthEstcPcType_Object = MibTableColumn
cfprSwEthEstcPcType = _CfprSwEthEstcPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 29),
    _CfprSwEthEstcPcType_Type()
)
cfprSwEthEstcPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcType.setStatus("current")
_CfprSwEthEstcPcUplinkFailAction_Type = CfprNwctrlLinkFailAction
_CfprSwEthEstcPcUplinkFailAction_Object = MibTableColumn
cfprSwEthEstcPcUplinkFailAction = _CfprSwEthEstcPcUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 12, 1, 30),
    _CfprSwEthEstcPcUplinkFailAction_Type()
)
cfprSwEthEstcPcUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthEstcPcUplinkFailAction.setStatus("current")
_CfprSwEthLanBorderTable_Object = MibTable
cfprSwEthLanBorderTable = _CfprSwEthLanBorderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13)
)
if mibBuilder.loadTexts:
    cfprSwEthLanBorderTable.setStatus("current")
_CfprSwEthLanBorderEntry_Object = MibTableRow
cfprSwEthLanBorderEntry = _CfprSwEthLanBorderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1)
)
cfprSwEthLanBorderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthLanBorderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthLanBorderEntry.setStatus("current")
_CfprSwEthLanBorderInstanceId_Type = CfprManagedObjectId
_CfprSwEthLanBorderInstanceId_Object = MibTableColumn
cfprSwEthLanBorderInstanceId = _CfprSwEthLanBorderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 1),
    _CfprSwEthLanBorderInstanceId_Type()
)
cfprSwEthLanBorderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderInstanceId.setStatus("current")
_CfprSwEthLanBorderDn_Type = CfprManagedObjectDn
_CfprSwEthLanBorderDn_Object = MibTableColumn
cfprSwEthLanBorderDn = _CfprSwEthLanBorderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 2),
    _CfprSwEthLanBorderDn_Type()
)
cfprSwEthLanBorderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderDn.setStatus("current")
_CfprSwEthLanBorderRn_Type = SnmpAdminString
_CfprSwEthLanBorderRn_Object = MibTableColumn
cfprSwEthLanBorderRn = _CfprSwEthLanBorderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 3),
    _CfprSwEthLanBorderRn_Type()
)
cfprSwEthLanBorderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderRn.setStatus("current")
_CfprSwEthLanBorderDeployFlag_Type = Integer32
_CfprSwEthLanBorderDeployFlag_Object = MibTableColumn
cfprSwEthLanBorderDeployFlag = _CfprSwEthLanBorderDeployFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 4),
    _CfprSwEthLanBorderDeployFlag_Type()
)
cfprSwEthLanBorderDeployFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderDeployFlag.setStatus("current")
_CfprSwEthLanBorderFsmDescr_Type = SnmpAdminString
_CfprSwEthLanBorderFsmDescr_Object = MibTableColumn
cfprSwEthLanBorderFsmDescr = _CfprSwEthLanBorderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 5),
    _CfprSwEthLanBorderFsmDescr_Type()
)
cfprSwEthLanBorderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmDescr.setStatus("current")
_CfprSwEthLanBorderFsmFlags_Type = SnmpAdminString
_CfprSwEthLanBorderFsmFlags_Object = MibTableColumn
cfprSwEthLanBorderFsmFlags = _CfprSwEthLanBorderFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 6),
    _CfprSwEthLanBorderFsmFlags_Type()
)
cfprSwEthLanBorderFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmFlags.setStatus("current")
_CfprSwEthLanBorderFsmPrev_Type = SnmpAdminString
_CfprSwEthLanBorderFsmPrev_Object = MibTableColumn
cfprSwEthLanBorderFsmPrev = _CfprSwEthLanBorderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 7),
    _CfprSwEthLanBorderFsmPrev_Type()
)
cfprSwEthLanBorderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmPrev.setStatus("current")
_CfprSwEthLanBorderFsmProgr_Type = Gauge32
_CfprSwEthLanBorderFsmProgr_Object = MibTableColumn
cfprSwEthLanBorderFsmProgr = _CfprSwEthLanBorderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 8),
    _CfprSwEthLanBorderFsmProgr_Type()
)
cfprSwEthLanBorderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmProgr.setStatus("current")
_CfprSwEthLanBorderFsmRmtInvErrCode_Type = Gauge32
_CfprSwEthLanBorderFsmRmtInvErrCode_Object = MibTableColumn
cfprSwEthLanBorderFsmRmtInvErrCode = _CfprSwEthLanBorderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 9),
    _CfprSwEthLanBorderFsmRmtInvErrCode_Type()
)
cfprSwEthLanBorderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmRmtInvErrCode.setStatus("current")
_CfprSwEthLanBorderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwEthLanBorderFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwEthLanBorderFsmRmtInvErrDescr = _CfprSwEthLanBorderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 10),
    _CfprSwEthLanBorderFsmRmtInvErrDescr_Type()
)
cfprSwEthLanBorderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmRmtInvErrDescr.setStatus("current")
_CfprSwEthLanBorderFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwEthLanBorderFsmRmtInvRslt_Object = MibTableColumn
cfprSwEthLanBorderFsmRmtInvRslt = _CfprSwEthLanBorderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 11),
    _CfprSwEthLanBorderFsmRmtInvRslt_Type()
)
cfprSwEthLanBorderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmRmtInvRslt.setStatus("current")
_CfprSwEthLanBorderFsmStageDescr_Type = SnmpAdminString
_CfprSwEthLanBorderFsmStageDescr_Object = MibTableColumn
cfprSwEthLanBorderFsmStageDescr = _CfprSwEthLanBorderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 12),
    _CfprSwEthLanBorderFsmStageDescr_Type()
)
cfprSwEthLanBorderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageDescr.setStatus("current")
_CfprSwEthLanBorderFsmStamp_Type = DateAndTime
_CfprSwEthLanBorderFsmStamp_Object = MibTableColumn
cfprSwEthLanBorderFsmStamp = _CfprSwEthLanBorderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 13),
    _CfprSwEthLanBorderFsmStamp_Type()
)
cfprSwEthLanBorderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStamp.setStatus("current")
_CfprSwEthLanBorderFsmStatus_Type = SnmpAdminString
_CfprSwEthLanBorderFsmStatus_Object = MibTableColumn
cfprSwEthLanBorderFsmStatus = _CfprSwEthLanBorderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 14),
    _CfprSwEthLanBorderFsmStatus_Type()
)
cfprSwEthLanBorderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStatus.setStatus("current")
_CfprSwEthLanBorderFsmTry_Type = Gauge32
_CfprSwEthLanBorderFsmTry_Object = MibTableColumn
cfprSwEthLanBorderFsmTry = _CfprSwEthLanBorderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 15),
    _CfprSwEthLanBorderFsmTry_Type()
)
cfprSwEthLanBorderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTry.setStatus("current")
_CfprSwEthLanBorderLocale_Type = CfprSwBorderDomainLocale
_CfprSwEthLanBorderLocale_Object = MibTableColumn
cfprSwEthLanBorderLocale = _CfprSwEthLanBorderLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 16),
    _CfprSwEthLanBorderLocale_Type()
)
cfprSwEthLanBorderLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderLocale.setStatus("current")
_CfprSwEthLanBorderName_Type = SnmpAdminString
_CfprSwEthLanBorderName_Object = MibTableColumn
cfprSwEthLanBorderName = _CfprSwEthLanBorderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 17),
    _CfprSwEthLanBorderName_Type()
)
cfprSwEthLanBorderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderName.setStatus("current")
_CfprSwEthLanBorderSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthLanBorderSwitchId_Object = MibTableColumn
cfprSwEthLanBorderSwitchId = _CfprSwEthLanBorderSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 18),
    _CfprSwEthLanBorderSwitchId_Type()
)
cfprSwEthLanBorderSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderSwitchId.setStatus("current")
_CfprSwEthLanBorderTransport_Type = CfprSwEthLanBorderTransport
_CfprSwEthLanBorderTransport_Object = MibTableColumn
cfprSwEthLanBorderTransport = _CfprSwEthLanBorderTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 19),
    _CfprSwEthLanBorderTransport_Type()
)
cfprSwEthLanBorderTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderTransport.setStatus("current")
_CfprSwEthLanBorderType_Type = CfprSwLanBorderType
_CfprSwEthLanBorderType_Object = MibTableColumn
cfprSwEthLanBorderType = _CfprSwEthLanBorderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 20),
    _CfprSwEthLanBorderType_Type()
)
cfprSwEthLanBorderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderType.setStatus("current")
_CfprSwEthLanBorderUdldMsgInterval_Type = Gauge32
_CfprSwEthLanBorderUdldMsgInterval_Object = MibTableColumn
cfprSwEthLanBorderUdldMsgInterval = _CfprSwEthLanBorderUdldMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 21),
    _CfprSwEthLanBorderUdldMsgInterval_Type()
)
cfprSwEthLanBorderUdldMsgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderUdldMsgInterval.setStatus("current")
_CfprSwEthLanBorderUdldRecoveryAction_Type = CfprFabricRecoveryAction
_CfprSwEthLanBorderUdldRecoveryAction_Object = MibTableColumn
cfprSwEthLanBorderUdldRecoveryAction = _CfprSwEthLanBorderUdldRecoveryAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 13, 1, 22),
    _CfprSwEthLanBorderUdldRecoveryAction_Type()
)
cfprSwEthLanBorderUdldRecoveryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderUdldRecoveryAction.setStatus("current")
_CfprSwEthLanBorderFsmTable_Object = MibTable
cfprSwEthLanBorderFsmTable = _CfprSwEthLanBorderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14)
)
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTable.setStatus("current")
_CfprSwEthLanBorderFsmEntry_Object = MibTableRow
cfprSwEthLanBorderFsmEntry = _CfprSwEthLanBorderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1)
)
cfprSwEthLanBorderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthLanBorderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmEntry.setStatus("current")
_CfprSwEthLanBorderFsmInstanceId_Type = CfprManagedObjectId
_CfprSwEthLanBorderFsmInstanceId_Object = MibTableColumn
cfprSwEthLanBorderFsmInstanceId = _CfprSwEthLanBorderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 1),
    _CfprSwEthLanBorderFsmInstanceId_Type()
)
cfprSwEthLanBorderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmInstanceId.setStatus("current")
_CfprSwEthLanBorderFsmDn_Type = CfprManagedObjectDn
_CfprSwEthLanBorderFsmDn_Object = MibTableColumn
cfprSwEthLanBorderFsmDn = _CfprSwEthLanBorderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 2),
    _CfprSwEthLanBorderFsmDn_Type()
)
cfprSwEthLanBorderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmDn.setStatus("current")
_CfprSwEthLanBorderFsmRn_Type = SnmpAdminString
_CfprSwEthLanBorderFsmRn_Object = MibTableColumn
cfprSwEthLanBorderFsmRn = _CfprSwEthLanBorderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 3),
    _CfprSwEthLanBorderFsmRn_Type()
)
cfprSwEthLanBorderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmRn.setStatus("current")
_CfprSwEthLanBorderFsmCompletionTime_Type = DateAndTime
_CfprSwEthLanBorderFsmCompletionTime_Object = MibTableColumn
cfprSwEthLanBorderFsmCompletionTime = _CfprSwEthLanBorderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 4),
    _CfprSwEthLanBorderFsmCompletionTime_Type()
)
cfprSwEthLanBorderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmCompletionTime.setStatus("current")
_CfprSwEthLanBorderFsmCurrentFsm_Type = CfprSwEthLanBorderFsmCurrentFsm
_CfprSwEthLanBorderFsmCurrentFsm_Object = MibTableColumn
cfprSwEthLanBorderFsmCurrentFsm = _CfprSwEthLanBorderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 5),
    _CfprSwEthLanBorderFsmCurrentFsm_Type()
)
cfprSwEthLanBorderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmCurrentFsm.setStatus("current")
_CfprSwEthLanBorderFsmDescrData_Type = SnmpAdminString
_CfprSwEthLanBorderFsmDescrData_Object = MibTableColumn
cfprSwEthLanBorderFsmDescrData = _CfprSwEthLanBorderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 6),
    _CfprSwEthLanBorderFsmDescrData_Type()
)
cfprSwEthLanBorderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmDescrData.setStatus("current")
_CfprSwEthLanBorderFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwEthLanBorderFsmFsmStatus_Object = MibTableColumn
cfprSwEthLanBorderFsmFsmStatus = _CfprSwEthLanBorderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 7),
    _CfprSwEthLanBorderFsmFsmStatus_Type()
)
cfprSwEthLanBorderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmFsmStatus.setStatus("current")
_CfprSwEthLanBorderFsmProgress_Type = Gauge32
_CfprSwEthLanBorderFsmProgress_Object = MibTableColumn
cfprSwEthLanBorderFsmProgress = _CfprSwEthLanBorderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 8),
    _CfprSwEthLanBorderFsmProgress_Type()
)
cfprSwEthLanBorderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmProgress.setStatus("current")
_CfprSwEthLanBorderFsmRmtErrCode_Type = Gauge32
_CfprSwEthLanBorderFsmRmtErrCode_Object = MibTableColumn
cfprSwEthLanBorderFsmRmtErrCode = _CfprSwEthLanBorderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 9),
    _CfprSwEthLanBorderFsmRmtErrCode_Type()
)
cfprSwEthLanBorderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmRmtErrCode.setStatus("current")
_CfprSwEthLanBorderFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwEthLanBorderFsmRmtErrDescr_Object = MibTableColumn
cfprSwEthLanBorderFsmRmtErrDescr = _CfprSwEthLanBorderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 10),
    _CfprSwEthLanBorderFsmRmtErrDescr_Type()
)
cfprSwEthLanBorderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmRmtErrDescr.setStatus("current")
_CfprSwEthLanBorderFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwEthLanBorderFsmRmtRslt_Object = MibTableColumn
cfprSwEthLanBorderFsmRmtRslt = _CfprSwEthLanBorderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 14, 1, 11),
    _CfprSwEthLanBorderFsmRmtRslt_Type()
)
cfprSwEthLanBorderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmRmtRslt.setStatus("current")
_CfprSwEthLanBorderFsmStageTable_Object = MibTable
cfprSwEthLanBorderFsmStageTable = _CfprSwEthLanBorderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15)
)
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageTable.setStatus("current")
_CfprSwEthLanBorderFsmStageEntry_Object = MibTableRow
cfprSwEthLanBorderFsmStageEntry = _CfprSwEthLanBorderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1)
)
cfprSwEthLanBorderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthLanBorderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageEntry.setStatus("current")
_CfprSwEthLanBorderFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwEthLanBorderFsmStageInstanceId_Object = MibTableColumn
cfprSwEthLanBorderFsmStageInstanceId = _CfprSwEthLanBorderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 1),
    _CfprSwEthLanBorderFsmStageInstanceId_Type()
)
cfprSwEthLanBorderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageInstanceId.setStatus("current")
_CfprSwEthLanBorderFsmStageDn_Type = CfprManagedObjectDn
_CfprSwEthLanBorderFsmStageDn_Object = MibTableColumn
cfprSwEthLanBorderFsmStageDn = _CfprSwEthLanBorderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 2),
    _CfprSwEthLanBorderFsmStageDn_Type()
)
cfprSwEthLanBorderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageDn.setStatus("current")
_CfprSwEthLanBorderFsmStageRn_Type = SnmpAdminString
_CfprSwEthLanBorderFsmStageRn_Object = MibTableColumn
cfprSwEthLanBorderFsmStageRn = _CfprSwEthLanBorderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 3),
    _CfprSwEthLanBorderFsmStageRn_Type()
)
cfprSwEthLanBorderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageRn.setStatus("current")
_CfprSwEthLanBorderFsmStageDescrData_Type = SnmpAdminString
_CfprSwEthLanBorderFsmStageDescrData_Object = MibTableColumn
cfprSwEthLanBorderFsmStageDescrData = _CfprSwEthLanBorderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 4),
    _CfprSwEthLanBorderFsmStageDescrData_Type()
)
cfprSwEthLanBorderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageDescrData.setStatus("current")
_CfprSwEthLanBorderFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwEthLanBorderFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwEthLanBorderFsmStageLastUpdateTime = _CfprSwEthLanBorderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 5),
    _CfprSwEthLanBorderFsmStageLastUpdateTime_Type()
)
cfprSwEthLanBorderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageLastUpdateTime.setStatus("current")
_CfprSwEthLanBorderFsmStageName_Type = CfprSwEthLanBorderFsmStageName
_CfprSwEthLanBorderFsmStageName_Object = MibTableColumn
cfprSwEthLanBorderFsmStageName = _CfprSwEthLanBorderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 6),
    _CfprSwEthLanBorderFsmStageName_Type()
)
cfprSwEthLanBorderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageName.setStatus("current")
_CfprSwEthLanBorderFsmStageOrder_Type = Gauge32
_CfprSwEthLanBorderFsmStageOrder_Object = MibTableColumn
cfprSwEthLanBorderFsmStageOrder = _CfprSwEthLanBorderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 7),
    _CfprSwEthLanBorderFsmStageOrder_Type()
)
cfprSwEthLanBorderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageOrder.setStatus("current")
_CfprSwEthLanBorderFsmStageRetry_Type = Gauge32
_CfprSwEthLanBorderFsmStageRetry_Object = MibTableColumn
cfprSwEthLanBorderFsmStageRetry = _CfprSwEthLanBorderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 8),
    _CfprSwEthLanBorderFsmStageRetry_Type()
)
cfprSwEthLanBorderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageRetry.setStatus("current")
_CfprSwEthLanBorderFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwEthLanBorderFsmStageStageStatus_Object = MibTableColumn
cfprSwEthLanBorderFsmStageStageStatus = _CfprSwEthLanBorderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 15, 1, 9),
    _CfprSwEthLanBorderFsmStageStageStatus_Type()
)
cfprSwEthLanBorderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmStageStageStatus.setStatus("current")
_CfprSwEthLanBorderFsmTaskTable_Object = MibTable
cfprSwEthLanBorderFsmTaskTable = _CfprSwEthLanBorderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16)
)
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskTable.setStatus("current")
_CfprSwEthLanBorderFsmTaskEntry_Object = MibTableRow
cfprSwEthLanBorderFsmTaskEntry = _CfprSwEthLanBorderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16, 1)
)
cfprSwEthLanBorderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthLanBorderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskEntry.setStatus("current")
_CfprSwEthLanBorderFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwEthLanBorderFsmTaskInstanceId_Object = MibTableColumn
cfprSwEthLanBorderFsmTaskInstanceId = _CfprSwEthLanBorderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16, 1, 1),
    _CfprSwEthLanBorderFsmTaskInstanceId_Type()
)
cfprSwEthLanBorderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskInstanceId.setStatus("current")
_CfprSwEthLanBorderFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwEthLanBorderFsmTaskDn_Object = MibTableColumn
cfprSwEthLanBorderFsmTaskDn = _CfprSwEthLanBorderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16, 1, 2),
    _CfprSwEthLanBorderFsmTaskDn_Type()
)
cfprSwEthLanBorderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskDn.setStatus("current")
_CfprSwEthLanBorderFsmTaskRn_Type = SnmpAdminString
_CfprSwEthLanBorderFsmTaskRn_Object = MibTableColumn
cfprSwEthLanBorderFsmTaskRn = _CfprSwEthLanBorderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16, 1, 3),
    _CfprSwEthLanBorderFsmTaskRn_Type()
)
cfprSwEthLanBorderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskRn.setStatus("current")
_CfprSwEthLanBorderFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwEthLanBorderFsmTaskCompletion_Object = MibTableColumn
cfprSwEthLanBorderFsmTaskCompletion = _CfprSwEthLanBorderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16, 1, 4),
    _CfprSwEthLanBorderFsmTaskCompletion_Type()
)
cfprSwEthLanBorderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskCompletion.setStatus("current")
_CfprSwEthLanBorderFsmTaskFlags_Type = CfprSwEthLanBorderFsmTaskFlags
_CfprSwEthLanBorderFsmTaskFlags_Object = MibTableColumn
cfprSwEthLanBorderFsmTaskFlags = _CfprSwEthLanBorderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16, 1, 5),
    _CfprSwEthLanBorderFsmTaskFlags_Type()
)
cfprSwEthLanBorderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskFlags.setStatus("current")
_CfprSwEthLanBorderFsmTaskItem_Type = CfprSwEthLanBorderFsmTaskItem
_CfprSwEthLanBorderFsmTaskItem_Object = MibTableColumn
cfprSwEthLanBorderFsmTaskItem = _CfprSwEthLanBorderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16, 1, 6),
    _CfprSwEthLanBorderFsmTaskItem_Type()
)
cfprSwEthLanBorderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskItem.setStatus("current")
_CfprSwEthLanBorderFsmTaskSeqId_Type = Gauge32
_CfprSwEthLanBorderFsmTaskSeqId_Object = MibTableColumn
cfprSwEthLanBorderFsmTaskSeqId = _CfprSwEthLanBorderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 16, 1, 7),
    _CfprSwEthLanBorderFsmTaskSeqId_Type()
)
cfprSwEthLanBorderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanBorderFsmTaskSeqId.setStatus("current")
_CfprSwEthLanEpTable_Object = MibTable
cfprSwEthLanEpTable = _CfprSwEthLanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17)
)
if mibBuilder.loadTexts:
    cfprSwEthLanEpTable.setStatus("current")
_CfprSwEthLanEpEntry_Object = MibTableRow
cfprSwEthLanEpEntry = _CfprSwEthLanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1)
)
cfprSwEthLanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthLanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthLanEpEntry.setStatus("current")
_CfprSwEthLanEpInstanceId_Type = CfprManagedObjectId
_CfprSwEthLanEpInstanceId_Object = MibTableColumn
cfprSwEthLanEpInstanceId = _CfprSwEthLanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 1),
    _CfprSwEthLanEpInstanceId_Type()
)
cfprSwEthLanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthLanEpInstanceId.setStatus("current")
_CfprSwEthLanEpDn_Type = CfprManagedObjectDn
_CfprSwEthLanEpDn_Object = MibTableColumn
cfprSwEthLanEpDn = _CfprSwEthLanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 2),
    _CfprSwEthLanEpDn_Type()
)
cfprSwEthLanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpDn.setStatus("current")
_CfprSwEthLanEpRn_Type = SnmpAdminString
_CfprSwEthLanEpRn_Object = MibTableColumn
cfprSwEthLanEpRn = _CfprSwEthLanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 3),
    _CfprSwEthLanEpRn_Type()
)
cfprSwEthLanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpRn.setStatus("current")
_CfprSwEthLanEpAdminSpeed_Type = CfprPortEthSpeed
_CfprSwEthLanEpAdminSpeed_Object = MibTableColumn
cfprSwEthLanEpAdminSpeed = _CfprSwEthLanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 4),
    _CfprSwEthLanEpAdminSpeed_Type()
)
cfprSwEthLanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpAdminSpeed.setStatus("current")
_CfprSwEthLanEpAdminState_Type = CfprFabricAdminState
_CfprSwEthLanEpAdminState_Object = MibTableColumn
cfprSwEthLanEpAdminState = _CfprSwEthLanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 5),
    _CfprSwEthLanEpAdminState_Type()
)
cfprSwEthLanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpAdminState.setStatus("current")
_CfprSwEthLanEpAggrPortId_Type = Gauge32
_CfprSwEthLanEpAggrPortId_Object = MibTableColumn
cfprSwEthLanEpAggrPortId = _CfprSwEthLanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 6),
    _CfprSwEthLanEpAggrPortId_Type()
)
cfprSwEthLanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpAggrPortId.setStatus("current")
_CfprSwEthLanEpChassisId_Type = Gauge32
_CfprSwEthLanEpChassisId_Object = MibTableColumn
cfprSwEthLanEpChassisId = _CfprSwEthLanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 7),
    _CfprSwEthLanEpChassisId_Type()
)
cfprSwEthLanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpChassisId.setStatus("current")
_CfprSwEthLanEpDtagVlan_Type = Gauge32
_CfprSwEthLanEpDtagVlan_Object = MibTableColumn
cfprSwEthLanEpDtagVlan = _CfprSwEthLanEpDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 8),
    _CfprSwEthLanEpDtagVlan_Type()
)
cfprSwEthLanEpDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpDtagVlan.setStatus("current")
_CfprSwEthLanEpEpDn_Type = SnmpAdminString
_CfprSwEthLanEpEpDn_Object = MibTableColumn
cfprSwEthLanEpEpDn = _CfprSwEthLanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 9),
    _CfprSwEthLanEpEpDn_Type()
)
cfprSwEthLanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpEpDn.setStatus("current")
_CfprSwEthLanEpIfRole_Type = CfprSwLanEpIfRole
_CfprSwEthLanEpIfRole_Object = MibTableColumn
cfprSwEthLanEpIfRole = _CfprSwEthLanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 10),
    _CfprSwEthLanEpIfRole_Type()
)
cfprSwEthLanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpIfRole.setStatus("current")
_CfprSwEthLanEpIfType_Type = CfprSwPIoEpIfType
_CfprSwEthLanEpIfType_Object = MibTableColumn
cfprSwEthLanEpIfType = _CfprSwEthLanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 11),
    _CfprSwEthLanEpIfType_Type()
)
cfprSwEthLanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpIfType.setStatus("current")
_CfprSwEthLanEpLc_Type = CfprSwPIoEpLc
_CfprSwEthLanEpLc_Object = MibTableColumn
cfprSwEthLanEpLc = _CfprSwEthLanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 12),
    _CfprSwEthLanEpLc_Type()
)
cfprSwEthLanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpLc.setStatus("current")
_CfprSwEthLanEpLocale_Type = CfprSwBorderEpLocale
_CfprSwEthLanEpLocale_Object = MibTableColumn
cfprSwEthLanEpLocale = _CfprSwEthLanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 13),
    _CfprSwEthLanEpLocale_Type()
)
cfprSwEthLanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpLocale.setStatus("current")
_CfprSwEthLanEpName_Type = SnmpAdminString
_CfprSwEthLanEpName_Object = MibTableColumn
cfprSwEthLanEpName = _CfprSwEthLanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 15),
    _CfprSwEthLanEpName_Type()
)
cfprSwEthLanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpName.setStatus("current")
_CfprSwEthLanEpPcId_Type = Gauge32
_CfprSwEthLanEpPcId_Object = MibTableColumn
cfprSwEthLanEpPcId = _CfprSwEthLanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 16),
    _CfprSwEthLanEpPcId_Type()
)
cfprSwEthLanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPcId.setStatus("current")
_CfprSwEthLanEpPeerAggrPortId_Type = Gauge32
_CfprSwEthLanEpPeerAggrPortId_Object = MibTableColumn
cfprSwEthLanEpPeerAggrPortId = _CfprSwEthLanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 17),
    _CfprSwEthLanEpPeerAggrPortId_Type()
)
cfprSwEthLanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPeerAggrPortId.setStatus("current")
_CfprSwEthLanEpPeerChassisId_Type = Gauge32
_CfprSwEthLanEpPeerChassisId_Object = MibTableColumn
cfprSwEthLanEpPeerChassisId = _CfprSwEthLanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 18),
    _CfprSwEthLanEpPeerChassisId_Type()
)
cfprSwEthLanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPeerChassisId.setStatus("current")
_CfprSwEthLanEpPeerDn_Type = SnmpAdminString
_CfprSwEthLanEpPeerDn_Object = MibTableColumn
cfprSwEthLanEpPeerDn = _CfprSwEthLanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 19),
    _CfprSwEthLanEpPeerDn_Type()
)
cfprSwEthLanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPeerDn.setStatus("current")
_CfprSwEthLanEpPeerPortId_Type = Gauge32
_CfprSwEthLanEpPeerPortId_Object = MibTableColumn
cfprSwEthLanEpPeerPortId = _CfprSwEthLanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 20),
    _CfprSwEthLanEpPeerPortId_Type()
)
cfprSwEthLanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPeerPortId.setStatus("current")
_CfprSwEthLanEpPeerSlotId_Type = Gauge32
_CfprSwEthLanEpPeerSlotId_Object = MibTableColumn
cfprSwEthLanEpPeerSlotId = _CfprSwEthLanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 21),
    _CfprSwEthLanEpPeerSlotId_Type()
)
cfprSwEthLanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPeerSlotId.setStatus("current")
_CfprSwEthLanEpPortId_Type = Gauge32
_CfprSwEthLanEpPortId_Object = MibTableColumn
cfprSwEthLanEpPortId = _CfprSwEthLanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 22),
    _CfprSwEthLanEpPortId_Type()
)
cfprSwEthLanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPortId.setStatus("current")
_CfprSwEthLanEpPriorityFlowCtrl_Type = CfprFlowctrlPriorityPause
_CfprSwEthLanEpPriorityFlowCtrl_Object = MibTableColumn
cfprSwEthLanEpPriorityFlowCtrl = _CfprSwEthLanEpPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 23),
    _CfprSwEthLanEpPriorityFlowCtrl_Type()
)
cfprSwEthLanEpPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPriorityFlowCtrl.setStatus("current")
_CfprSwEthLanEpRecvFlowCtrl_Type = CfprFlowctrlFlowControlRx
_CfprSwEthLanEpRecvFlowCtrl_Object = MibTableColumn
cfprSwEthLanEpRecvFlowCtrl = _CfprSwEthLanEpRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 24),
    _CfprSwEthLanEpRecvFlowCtrl_Type()
)
cfprSwEthLanEpRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpRecvFlowCtrl.setStatus("current")
_CfprSwEthLanEpSendFlowCtrl_Type = CfprFlowctrlFlowControlTx
_CfprSwEthLanEpSendFlowCtrl_Object = MibTableColumn
cfprSwEthLanEpSendFlowCtrl = _CfprSwEthLanEpSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 25),
    _CfprSwEthLanEpSendFlowCtrl_Type()
)
cfprSwEthLanEpSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpSendFlowCtrl.setStatus("current")
_CfprSwEthLanEpSlotId_Type = Gauge32
_CfprSwEthLanEpSlotId_Object = MibTableColumn
cfprSwEthLanEpSlotId = _CfprSwEthLanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 26),
    _CfprSwEthLanEpSlotId_Type()
)
cfprSwEthLanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpSlotId.setStatus("current")
_CfprSwEthLanEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthLanEpSwitchId_Object = MibTableColumn
cfprSwEthLanEpSwitchId = _CfprSwEthLanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 27),
    _CfprSwEthLanEpSwitchId_Type()
)
cfprSwEthLanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpSwitchId.setStatus("current")
_CfprSwEthLanEpTransport_Type = CfprSwEthLanEpTransport
_CfprSwEthLanEpTransport_Object = MibTableColumn
cfprSwEthLanEpTransport = _CfprSwEthLanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 28),
    _CfprSwEthLanEpTransport_Type()
)
cfprSwEthLanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpTransport.setStatus("current")
_CfprSwEthLanEpType_Type = CfprSwLanEpType
_CfprSwEthLanEpType_Object = MibTableColumn
cfprSwEthLanEpType = _CfprSwEthLanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 29),
    _CfprSwEthLanEpType_Type()
)
cfprSwEthLanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpType.setStatus("current")
_CfprSwEthLanEpUdldAdminState_Type = CfprSwEthLanEpUdldAdminState
_CfprSwEthLanEpUdldAdminState_Object = MibTableColumn
cfprSwEthLanEpUdldAdminState = _CfprSwEthLanEpUdldAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 30),
    _CfprSwEthLanEpUdldAdminState_Type()
)
cfprSwEthLanEpUdldAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpUdldAdminState.setStatus("current")
_CfprSwEthLanEpUdldMode_Type = CfprSwEthLanEpUdldMode
_CfprSwEthLanEpUdldMode_Object = MibTableColumn
cfprSwEthLanEpUdldMode = _CfprSwEthLanEpUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 31),
    _CfprSwEthLanEpUdldMode_Type()
)
cfprSwEthLanEpUdldMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpUdldMode.setStatus("current")
_CfprSwEthLanEpAdminDuplex_Type = CfprPortDuplex
_CfprSwEthLanEpAdminDuplex_Object = MibTableColumn
cfprSwEthLanEpAdminDuplex = _CfprSwEthLanEpAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 32),
    _CfprSwEthLanEpAdminDuplex_Type()
)
cfprSwEthLanEpAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpAdminDuplex.setStatus("current")
_CfprSwEthLanEpAutoNeg_Type = TruthValue
_CfprSwEthLanEpAutoNeg_Object = MibTableColumn
cfprSwEthLanEpAutoNeg = _CfprSwEthLanEpAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 33),
    _CfprSwEthLanEpAutoNeg_Type()
)
cfprSwEthLanEpAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpAutoNeg.setStatus("current")
_CfprSwEthLanEpHashAlg_Type = CfprNhTpHashType
_CfprSwEthLanEpHashAlg_Object = MibTableColumn
cfprSwEthLanEpHashAlg = _CfprSwEthLanEpHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 34),
    _CfprSwEthLanEpHashAlg_Type()
)
cfprSwEthLanEpHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpHashAlg.setStatus("current")
_CfprSwEthLanEpInlineState_Type = CfprSwEthLanEpInlineState
_CfprSwEthLanEpInlineState_Object = MibTableColumn
cfprSwEthLanEpInlineState = _CfprSwEthLanEpInlineState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 35),
    _CfprSwEthLanEpInlineState_Type()
)
cfprSwEthLanEpInlineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpInlineState.setStatus("current")
_CfprSwEthLanEpPcMode_Type = CfprSwPcMode
_CfprSwEthLanEpPcMode_Object = MibTableColumn
cfprSwEthLanEpPcMode = _CfprSwEthLanEpPcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 36),
    _CfprSwEthLanEpPcMode_Type()
)
cfprSwEthLanEpPcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPcMode.setStatus("current")
_CfprSwEthLanEpPcModeState_Type = CfprSwPcModeState
_CfprSwEthLanEpPcModeState_Object = MibTableColumn
cfprSwEthLanEpPcModeState = _CfprSwEthLanEpPcModeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 37),
    _CfprSwEthLanEpPcModeState_Type()
)
cfprSwEthLanEpPcModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpPcModeState.setStatus("current")
_CfprSwEthLanEpQosPrio_Type = CfprFabricQosPrio
_CfprSwEthLanEpQosPrio_Object = MibTableColumn
cfprSwEthLanEpQosPrio = _CfprSwEthLanEpQosPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 38),
    _CfprSwEthLanEpQosPrio_Type()
)
cfprSwEthLanEpQosPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpQosPrio.setStatus("current")
_CfprSwEthLanEpLldp_Type = CfprNwctrlLldpAdminStateBitmask
_CfprSwEthLanEpLldp_Object = MibTableColumn
cfprSwEthLanEpLldp = _CfprSwEthLanEpLldp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 39),
    _CfprSwEthLanEpLldp_Type()
)
cfprSwEthLanEpLldp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpLldp.setStatus("current")
_CfprSwEthLanEpAllowAneg_Type = TruthValue
_CfprSwEthLanEpAllowAneg_Object = MibTableColumn
cfprSwEthLanEpAllowAneg = _CfprSwEthLanEpAllowAneg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 40),
    _CfprSwEthLanEpAllowAneg_Type()
)
cfprSwEthLanEpAllowAneg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpAllowAneg.setStatus("current")
_CfprSwEthLanEpDebounceTime_Type = Gauge32
_CfprSwEthLanEpDebounceTime_Object = MibTableColumn
cfprSwEthLanEpDebounceTime = _CfprSwEthLanEpDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 41),
    _CfprSwEthLanEpDebounceTime_Type()
)
cfprSwEthLanEpDebounceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpDebounceTime.setStatus("current")
_CfprSwEthLanEpServiceState_Type = CfprSwEthLanEpServiceState
_CfprSwEthLanEpServiceState_Object = MibTableColumn
cfprSwEthLanEpServiceState = _CfprSwEthLanEpServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 17, 1, 42),
    _CfprSwEthLanEpServiceState_Type()
)
cfprSwEthLanEpServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanEpServiceState.setStatus("current")
_CfprSwEthLanMonTable_Object = MibTable
cfprSwEthLanMonTable = _CfprSwEthLanMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22)
)
if mibBuilder.loadTexts:
    cfprSwEthLanMonTable.setStatus("current")
_CfprSwEthLanMonEntry_Object = MibTableRow
cfprSwEthLanMonEntry = _CfprSwEthLanMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1)
)
cfprSwEthLanMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthLanMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthLanMonEntry.setStatus("current")
_CfprSwEthLanMonInstanceId_Type = CfprManagedObjectId
_CfprSwEthLanMonInstanceId_Object = MibTableColumn
cfprSwEthLanMonInstanceId = _CfprSwEthLanMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1, 1),
    _CfprSwEthLanMonInstanceId_Type()
)
cfprSwEthLanMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthLanMonInstanceId.setStatus("current")
_CfprSwEthLanMonDn_Type = CfprManagedObjectDn
_CfprSwEthLanMonDn_Object = MibTableColumn
cfprSwEthLanMonDn = _CfprSwEthLanMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1, 2),
    _CfprSwEthLanMonDn_Type()
)
cfprSwEthLanMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanMonDn.setStatus("current")
_CfprSwEthLanMonRn_Type = SnmpAdminString
_CfprSwEthLanMonRn_Object = MibTableColumn
cfprSwEthLanMonRn = _CfprSwEthLanMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1, 3),
    _CfprSwEthLanMonRn_Type()
)
cfprSwEthLanMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanMonRn.setStatus("current")
_CfprSwEthLanMonLocale_Type = CfprSwMonDomainLocale
_CfprSwEthLanMonLocale_Object = MibTableColumn
cfprSwEthLanMonLocale = _CfprSwEthLanMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1, 4),
    _CfprSwEthLanMonLocale_Type()
)
cfprSwEthLanMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanMonLocale.setStatus("current")
_CfprSwEthLanMonName_Type = SnmpAdminString
_CfprSwEthLanMonName_Object = MibTableColumn
cfprSwEthLanMonName = _CfprSwEthLanMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1, 5),
    _CfprSwEthLanMonName_Type()
)
cfprSwEthLanMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanMonName.setStatus("current")
_CfprSwEthLanMonSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthLanMonSwitchId_Object = MibTableColumn
cfprSwEthLanMonSwitchId = _CfprSwEthLanMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1, 6),
    _CfprSwEthLanMonSwitchId_Type()
)
cfprSwEthLanMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanMonSwitchId.setStatus("current")
_CfprSwEthLanMonTransport_Type = CfprSwEthLanMonTransport
_CfprSwEthLanMonTransport_Object = MibTableColumn
cfprSwEthLanMonTransport = _CfprSwEthLanMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1, 7),
    _CfprSwEthLanMonTransport_Type()
)
cfprSwEthLanMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanMonTransport.setStatus("current")
_CfprSwEthLanMonType_Type = CfprSwLanMonType
_CfprSwEthLanMonType_Object = MibTableColumn
cfprSwEthLanMonType = _CfprSwEthLanMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 22, 1, 8),
    _CfprSwEthLanMonType_Type()
)
cfprSwEthLanMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanMonType.setStatus("current")
_CfprSwEthLanPcTable_Object = MibTable
cfprSwEthLanPcTable = _CfprSwEthLanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23)
)
if mibBuilder.loadTexts:
    cfprSwEthLanPcTable.setStatus("current")
_CfprSwEthLanPcEntry_Object = MibTableRow
cfprSwEthLanPcEntry = _CfprSwEthLanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1)
)
cfprSwEthLanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthLanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthLanPcEntry.setStatus("current")
_CfprSwEthLanPcInstanceId_Type = CfprManagedObjectId
_CfprSwEthLanPcInstanceId_Object = MibTableColumn
cfprSwEthLanPcInstanceId = _CfprSwEthLanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 1),
    _CfprSwEthLanPcInstanceId_Type()
)
cfprSwEthLanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthLanPcInstanceId.setStatus("current")
_CfprSwEthLanPcDn_Type = CfprManagedObjectDn
_CfprSwEthLanPcDn_Object = MibTableColumn
cfprSwEthLanPcDn = _CfprSwEthLanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 2),
    _CfprSwEthLanPcDn_Type()
)
cfprSwEthLanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcDn.setStatus("current")
_CfprSwEthLanPcRn_Type = SnmpAdminString
_CfprSwEthLanPcRn_Object = MibTableColumn
cfprSwEthLanPcRn = _CfprSwEthLanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 3),
    _CfprSwEthLanPcRn_Type()
)
cfprSwEthLanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcRn.setStatus("current")
_CfprSwEthLanPcAdminSpeed_Type = CfprPortEthSpeed
_CfprSwEthLanPcAdminSpeed_Object = MibTableColumn
cfprSwEthLanPcAdminSpeed = _CfprSwEthLanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 4),
    _CfprSwEthLanPcAdminSpeed_Type()
)
cfprSwEthLanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcAdminSpeed.setStatus("current")
_CfprSwEthLanPcAdminState_Type = CfprFabricAdminState
_CfprSwEthLanPcAdminState_Object = MibTableColumn
cfprSwEthLanPcAdminState = _CfprSwEthLanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 5),
    _CfprSwEthLanPcAdminState_Type()
)
cfprSwEthLanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcAdminState.setStatus("current")
_CfprSwEthLanPcClusterName_Type = SnmpAdminString
_CfprSwEthLanPcClusterName_Object = MibTableColumn
cfprSwEthLanPcClusterName = _CfprSwEthLanPcClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 6),
    _CfprSwEthLanPcClusterName_Type()
)
cfprSwEthLanPcClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcClusterName.setStatus("current")
_CfprSwEthLanPcDtagVlan_Type = Gauge32
_CfprSwEthLanPcDtagVlan_Object = MibTableColumn
cfprSwEthLanPcDtagVlan = _CfprSwEthLanPcDtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 7),
    _CfprSwEthLanPcDtagVlan_Type()
)
cfprSwEthLanPcDtagVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcDtagVlan.setStatus("current")
_CfprSwEthLanPcEpDn_Type = SnmpAdminString
_CfprSwEthLanPcEpDn_Object = MibTableColumn
cfprSwEthLanPcEpDn = _CfprSwEthLanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 8),
    _CfprSwEthLanPcEpDn_Type()
)
cfprSwEthLanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcEpDn.setStatus("current")
_CfprSwEthLanPcIfRole_Type = CfprSwLanPcIfRole
_CfprSwEthLanPcIfRole_Object = MibTableColumn
cfprSwEthLanPcIfRole = _CfprSwEthLanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 9),
    _CfprSwEthLanPcIfRole_Type()
)
cfprSwEthLanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcIfRole.setStatus("current")
_CfprSwEthLanPcIfType_Type = CfprSwCIoEpIfType
_CfprSwEthLanPcIfType_Object = MibTableColumn
cfprSwEthLanPcIfType = _CfprSwEthLanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 10),
    _CfprSwEthLanPcIfType_Type()
)
cfprSwEthLanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcIfType.setStatus("current")
_CfprSwEthLanPcLacpFastTimer_Type = TruthValue
_CfprSwEthLanPcLacpFastTimer_Object = MibTableColumn
cfprSwEthLanPcLacpFastTimer = _CfprSwEthLanPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 11),
    _CfprSwEthLanPcLacpFastTimer_Type()
)
cfprSwEthLanPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcLacpFastTimer.setStatus("current")
_CfprSwEthLanPcLacpSuspendIndividual_Type = TruthValue
_CfprSwEthLanPcLacpSuspendIndividual_Object = MibTableColumn
cfprSwEthLanPcLacpSuspendIndividual = _CfprSwEthLanPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 12),
    _CfprSwEthLanPcLacpSuspendIndividual_Type()
)
cfprSwEthLanPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcLacpSuspendIndividual.setStatus("current")
_CfprSwEthLanPcLocale_Type = CfprSwBorderPcLocale
_CfprSwEthLanPcLocale_Object = MibTableColumn
cfprSwEthLanPcLocale = _CfprSwEthLanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 13),
    _CfprSwEthLanPcLocale_Type()
)
cfprSwEthLanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcLocale.setStatus("current")
_CfprSwEthLanPcMonTrafDir_Type = CfprFabricTrafficDirection
_CfprSwEthLanPcMonTrafDir_Object = MibTableColumn
cfprSwEthLanPcMonTrafDir = _CfprSwEthLanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 14),
    _CfprSwEthLanPcMonTrafDir_Type()
)
cfprSwEthLanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcMonTrafDir.setStatus("current")
_CfprSwEthLanPcName_Type = SnmpAdminString
_CfprSwEthLanPcName_Object = MibTableColumn
cfprSwEthLanPcName = _CfprSwEthLanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 16),
    _CfprSwEthLanPcName_Type()
)
cfprSwEthLanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcName.setStatus("current")
_CfprSwEthLanPcPeerDn_Type = SnmpAdminString
_CfprSwEthLanPcPeerDn_Object = MibTableColumn
cfprSwEthLanPcPeerDn = _CfprSwEthLanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 17),
    _CfprSwEthLanPcPeerDn_Type()
)
cfprSwEthLanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcPeerDn.setStatus("current")
_CfprSwEthLanPcPortId_Type = Gauge32
_CfprSwEthLanPcPortId_Object = MibTableColumn
cfprSwEthLanPcPortId = _CfprSwEthLanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 18),
    _CfprSwEthLanPcPortId_Type()
)
cfprSwEthLanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcPortId.setStatus("current")
_CfprSwEthLanPcPriorityFlowCtrl_Type = CfprFlowctrlPriorityPause
_CfprSwEthLanPcPriorityFlowCtrl_Object = MibTableColumn
cfprSwEthLanPcPriorityFlowCtrl = _CfprSwEthLanPcPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 19),
    _CfprSwEthLanPcPriorityFlowCtrl_Type()
)
cfprSwEthLanPcPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcPriorityFlowCtrl.setStatus("current")
_CfprSwEthLanPcRecvFlowCtrl_Type = CfprFlowctrlFlowControlRx
_CfprSwEthLanPcRecvFlowCtrl_Object = MibTableColumn
cfprSwEthLanPcRecvFlowCtrl = _CfprSwEthLanPcRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 20),
    _CfprSwEthLanPcRecvFlowCtrl_Type()
)
cfprSwEthLanPcRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcRecvFlowCtrl.setStatus("current")
_CfprSwEthLanPcSendFlowCtrl_Type = CfprFlowctrlFlowControlTx
_CfprSwEthLanPcSendFlowCtrl_Object = MibTableColumn
cfprSwEthLanPcSendFlowCtrl = _CfprSwEthLanPcSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 21),
    _CfprSwEthLanPcSendFlowCtrl_Type()
)
cfprSwEthLanPcSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcSendFlowCtrl.setStatus("current")
_CfprSwEthLanPcSpannedCluster_Type = CfprFabricSpannedCluster
_CfprSwEthLanPcSpannedCluster_Object = MibTableColumn
cfprSwEthLanPcSpannedCluster = _CfprSwEthLanPcSpannedCluster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 22),
    _CfprSwEthLanPcSpannedCluster_Type()
)
cfprSwEthLanPcSpannedCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcSpannedCluster.setStatus("current")
_CfprSwEthLanPcSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthLanPcSwitchId_Object = MibTableColumn
cfprSwEthLanPcSwitchId = _CfprSwEthLanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 23),
    _CfprSwEthLanPcSwitchId_Type()
)
cfprSwEthLanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcSwitchId.setStatus("current")
_CfprSwEthLanPcTransport_Type = CfprSwEthLanPcTransport
_CfprSwEthLanPcTransport_Object = MibTableColumn
cfprSwEthLanPcTransport = _CfprSwEthLanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 24),
    _CfprSwEthLanPcTransport_Type()
)
cfprSwEthLanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcTransport.setStatus("current")
_CfprSwEthLanPcType_Type = CfprSwLanPcType
_CfprSwEthLanPcType_Object = MibTableColumn
cfprSwEthLanPcType = _CfprSwEthLanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 25),
    _CfprSwEthLanPcType_Type()
)
cfprSwEthLanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcType.setStatus("current")
_CfprSwEthLanPcCluChassisId_Type = Gauge32
_CfprSwEthLanPcCluChassisId_Object = MibTableColumn
cfprSwEthLanPcCluChassisId = _CfprSwEthLanPcCluChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 26),
    _CfprSwEthLanPcCluChassisId_Type()
)
cfprSwEthLanPcCluChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcCluChassisId.setStatus("current")
_CfprSwEthLanPcLacpDetach_Type = CfprSwAdminState
_CfprSwEthLanPcLacpDetach_Object = MibTableColumn
cfprSwEthLanPcLacpDetach = _CfprSwEthLanPcLacpDetach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 27),
    _CfprSwEthLanPcLacpDetach_Type()
)
cfprSwEthLanPcLacpDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcLacpDetach.setStatus("current")
_CfprSwEthLanPcAdminDuplex_Type = CfprPortDuplex
_CfprSwEthLanPcAdminDuplex_Object = MibTableColumn
cfprSwEthLanPcAdminDuplex = _CfprSwEthLanPcAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 28),
    _CfprSwEthLanPcAdminDuplex_Type()
)
cfprSwEthLanPcAdminDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcAdminDuplex.setStatus("current")
_CfprSwEthLanPcAutoNeg_Type = TruthValue
_CfprSwEthLanPcAutoNeg_Object = MibTableColumn
cfprSwEthLanPcAutoNeg = _CfprSwEthLanPcAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 29),
    _CfprSwEthLanPcAutoNeg_Type()
)
cfprSwEthLanPcAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcAutoNeg.setStatus("current")
_CfprSwEthLanPcHashAlg_Type = CfprNhTpHashType
_CfprSwEthLanPcHashAlg_Object = MibTableColumn
cfprSwEthLanPcHashAlg = _CfprSwEthLanPcHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 30),
    _CfprSwEthLanPcHashAlg_Type()
)
cfprSwEthLanPcHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcHashAlg.setStatus("current")
_CfprSwEthLanPcInlineState_Type = CfprSwEthLanPcInlineState
_CfprSwEthLanPcInlineState_Object = MibTableColumn
cfprSwEthLanPcInlineState = _CfprSwEthLanPcInlineState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 31),
    _CfprSwEthLanPcInlineState_Type()
)
cfprSwEthLanPcInlineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcInlineState.setStatus("current")
_CfprSwEthLanPcPcMode_Type = CfprSwPcMode
_CfprSwEthLanPcPcMode_Object = MibTableColumn
cfprSwEthLanPcPcMode = _CfprSwEthLanPcPcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 32),
    _CfprSwEthLanPcPcMode_Type()
)
cfprSwEthLanPcPcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcPcMode.setStatus("current")
_CfprSwEthLanPcPcModeState_Type = CfprSwPcModeState
_CfprSwEthLanPcPcModeState_Object = MibTableColumn
cfprSwEthLanPcPcModeState = _CfprSwEthLanPcPcModeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 33),
    _CfprSwEthLanPcPcModeState_Type()
)
cfprSwEthLanPcPcModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcPcModeState.setStatus("current")
_CfprSwEthLanPcQosPrio_Type = CfprFabricQosPrio
_CfprSwEthLanPcQosPrio_Object = MibTableColumn
cfprSwEthLanPcQosPrio = _CfprSwEthLanPcQosPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 34),
    _CfprSwEthLanPcQosPrio_Type()
)
cfprSwEthLanPcQosPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcQosPrio.setStatus("current")
_CfprSwEthLanPcLldp_Type = CfprNwctrlLldpAdminStateBitmask
_CfprSwEthLanPcLldp_Object = MibTableColumn
cfprSwEthLanPcLldp = _CfprSwEthLanPcLldp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 35),
    _CfprSwEthLanPcLldp_Type()
)
cfprSwEthLanPcLldp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcLldp.setStatus("current")
_CfprSwEthLanPcServiceState_Type = CfprSwEthLanPcServiceState
_CfprSwEthLanPcServiceState_Object = MibTableColumn
cfprSwEthLanPcServiceState = _CfprSwEthLanPcServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 23, 1, 36),
    _CfprSwEthLanPcServiceState_Type()
)
cfprSwEthLanPcServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthLanPcServiceState.setStatus("current")
_CfprSwEthMonTable_Object = MibTable
cfprSwEthMonTable = _CfprSwEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24)
)
if mibBuilder.loadTexts:
    cfprSwEthMonTable.setStatus("current")
_CfprSwEthMonEntry_Object = MibTableRow
cfprSwEthMonEntry = _CfprSwEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1)
)
cfprSwEthMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthMonEntry.setStatus("current")
_CfprSwEthMonInstanceId_Type = CfprManagedObjectId
_CfprSwEthMonInstanceId_Object = MibTableColumn
cfprSwEthMonInstanceId = _CfprSwEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 1),
    _CfprSwEthMonInstanceId_Type()
)
cfprSwEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthMonInstanceId.setStatus("current")
_CfprSwEthMonDn_Type = CfprManagedObjectDn
_CfprSwEthMonDn_Object = MibTableColumn
cfprSwEthMonDn = _CfprSwEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 2),
    _CfprSwEthMonDn_Type()
)
cfprSwEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDn.setStatus("current")
_CfprSwEthMonRn_Type = SnmpAdminString
_CfprSwEthMonRn_Object = MibTableColumn
cfprSwEthMonRn = _CfprSwEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 3),
    _CfprSwEthMonRn_Type()
)
cfprSwEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonRn.setStatus("current")
_CfprSwEthMonAdminState_Type = CfprSwMonAdminState
_CfprSwEthMonAdminState_Object = MibTableColumn
cfprSwEthMonAdminState = _CfprSwEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 4),
    _CfprSwEthMonAdminState_Type()
)
cfprSwEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonAdminState.setStatus("current")
_CfprSwEthMonFsmDescr_Type = SnmpAdminString
_CfprSwEthMonFsmDescr_Object = MibTableColumn
cfprSwEthMonFsmDescr = _CfprSwEthMonFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 5),
    _CfprSwEthMonFsmDescr_Type()
)
cfprSwEthMonFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmDescr.setStatus("current")
_CfprSwEthMonFsmPrev_Type = SnmpAdminString
_CfprSwEthMonFsmPrev_Object = MibTableColumn
cfprSwEthMonFsmPrev = _CfprSwEthMonFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 6),
    _CfprSwEthMonFsmPrev_Type()
)
cfprSwEthMonFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmPrev.setStatus("current")
_CfprSwEthMonFsmProgr_Type = Gauge32
_CfprSwEthMonFsmProgr_Object = MibTableColumn
cfprSwEthMonFsmProgr = _CfprSwEthMonFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 7),
    _CfprSwEthMonFsmProgr_Type()
)
cfprSwEthMonFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmProgr.setStatus("current")
_CfprSwEthMonFsmRmtInvErrCode_Type = Gauge32
_CfprSwEthMonFsmRmtInvErrCode_Object = MibTableColumn
cfprSwEthMonFsmRmtInvErrCode = _CfprSwEthMonFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 8),
    _CfprSwEthMonFsmRmtInvErrCode_Type()
)
cfprSwEthMonFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmRmtInvErrCode.setStatus("current")
_CfprSwEthMonFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwEthMonFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwEthMonFsmRmtInvErrDescr = _CfprSwEthMonFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 9),
    _CfprSwEthMonFsmRmtInvErrDescr_Type()
)
cfprSwEthMonFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmRmtInvErrDescr.setStatus("current")
_CfprSwEthMonFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwEthMonFsmRmtInvRslt_Object = MibTableColumn
cfprSwEthMonFsmRmtInvRslt = _CfprSwEthMonFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 10),
    _CfprSwEthMonFsmRmtInvRslt_Type()
)
cfprSwEthMonFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmRmtInvRslt.setStatus("current")
_CfprSwEthMonFsmStageDescr_Type = SnmpAdminString
_CfprSwEthMonFsmStageDescr_Object = MibTableColumn
cfprSwEthMonFsmStageDescr = _CfprSwEthMonFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 11),
    _CfprSwEthMonFsmStageDescr_Type()
)
cfprSwEthMonFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageDescr.setStatus("current")
_CfprSwEthMonFsmStamp_Type = DateAndTime
_CfprSwEthMonFsmStamp_Object = MibTableColumn
cfprSwEthMonFsmStamp = _CfprSwEthMonFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 12),
    _CfprSwEthMonFsmStamp_Type()
)
cfprSwEthMonFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStamp.setStatus("current")
_CfprSwEthMonFsmStatus_Type = SnmpAdminString
_CfprSwEthMonFsmStatus_Object = MibTableColumn
cfprSwEthMonFsmStatus = _CfprSwEthMonFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 13),
    _CfprSwEthMonFsmStatus_Type()
)
cfprSwEthMonFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStatus.setStatus("current")
_CfprSwEthMonFsmTry_Type = Gauge32
_CfprSwEthMonFsmTry_Object = MibTableColumn
cfprSwEthMonFsmTry = _CfprSwEthMonFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 14),
    _CfprSwEthMonFsmTry_Type()
)
cfprSwEthMonFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTry.setStatus("current")
_CfprSwEthMonHasLastDest_Type = TruthValue
_CfprSwEthMonHasLastDest_Object = MibTableColumn
cfprSwEthMonHasLastDest = _CfprSwEthMonHasLastDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 15),
    _CfprSwEthMonHasLastDest_Type()
)
cfprSwEthMonHasLastDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonHasLastDest.setStatus("current")
_CfprSwEthMonLifeCycle_Type = CfprSwMonLifeCycle
_CfprSwEthMonLifeCycle_Object = MibTableColumn
cfprSwEthMonLifeCycle = _CfprSwEthMonLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 16),
    _CfprSwEthMonLifeCycle_Type()
)
cfprSwEthMonLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonLifeCycle.setStatus("current")
_CfprSwEthMonName_Type = SnmpAdminString
_CfprSwEthMonName_Object = MibTableColumn
cfprSwEthMonName = _CfprSwEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 17),
    _CfprSwEthMonName_Type()
)
cfprSwEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonName.setStatus("current")
_CfprSwEthMonPeerDn_Type = SnmpAdminString
_CfprSwEthMonPeerDn_Object = MibTableColumn
cfprSwEthMonPeerDn = _CfprSwEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 18),
    _CfprSwEthMonPeerDn_Type()
)
cfprSwEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonPeerDn.setStatus("current")
_CfprSwEthMonSession_Type = Gauge32
_CfprSwEthMonSession_Object = MibTableColumn
cfprSwEthMonSession = _CfprSwEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 19),
    _CfprSwEthMonSession_Type()
)
cfprSwEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSession.setStatus("current")
_CfprSwEthMonSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthMonSwitchId_Object = MibTableColumn
cfprSwEthMonSwitchId = _CfprSwEthMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 20),
    _CfprSwEthMonSwitchId_Type()
)
cfprSwEthMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSwitchId.setStatus("current")
_CfprSwEthMonTransport_Type = CfprSwEthMonTransport
_CfprSwEthMonTransport_Object = MibTableColumn
cfprSwEthMonTransport = _CfprSwEthMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 21),
    _CfprSwEthMonTransport_Type()
)
cfprSwEthMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonTransport.setStatus("current")
_CfprSwEthMonType_Type = CfprSwEthMonType
_CfprSwEthMonType_Object = MibTableColumn
cfprSwEthMonType = _CfprSwEthMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 24, 1, 22),
    _CfprSwEthMonType_Type()
)
cfprSwEthMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonType.setStatus("current")
_CfprSwEthMonDestEpTable_Object = MibTable
cfprSwEthMonDestEpTable = _CfprSwEthMonDestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25)
)
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpTable.setStatus("current")
_CfprSwEthMonDestEpEntry_Object = MibTableRow
cfprSwEthMonDestEpEntry = _CfprSwEthMonDestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1)
)
cfprSwEthMonDestEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthMonDestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpEntry.setStatus("current")
_CfprSwEthMonDestEpInstanceId_Type = CfprManagedObjectId
_CfprSwEthMonDestEpInstanceId_Object = MibTableColumn
cfprSwEthMonDestEpInstanceId = _CfprSwEthMonDestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 1),
    _CfprSwEthMonDestEpInstanceId_Type()
)
cfprSwEthMonDestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpInstanceId.setStatus("current")
_CfprSwEthMonDestEpDn_Type = CfprManagedObjectDn
_CfprSwEthMonDestEpDn_Object = MibTableColumn
cfprSwEthMonDestEpDn = _CfprSwEthMonDestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 2),
    _CfprSwEthMonDestEpDn_Type()
)
cfprSwEthMonDestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpDn.setStatus("current")
_CfprSwEthMonDestEpRn_Type = SnmpAdminString
_CfprSwEthMonDestEpRn_Object = MibTableColumn
cfprSwEthMonDestEpRn = _CfprSwEthMonDestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 3),
    _CfprSwEthMonDestEpRn_Type()
)
cfprSwEthMonDestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpRn.setStatus("current")
_CfprSwEthMonDestEpAdminSpeed_Type = CfprPortEthSpeed
_CfprSwEthMonDestEpAdminSpeed_Object = MibTableColumn
cfprSwEthMonDestEpAdminSpeed = _CfprSwEthMonDestEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 4),
    _CfprSwEthMonDestEpAdminSpeed_Type()
)
cfprSwEthMonDestEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpAdminSpeed.setStatus("current")
_CfprSwEthMonDestEpAdminState_Type = CfprFabricAdminState
_CfprSwEthMonDestEpAdminState_Object = MibTableColumn
cfprSwEthMonDestEpAdminState = _CfprSwEthMonDestEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 5),
    _CfprSwEthMonDestEpAdminState_Type()
)
cfprSwEthMonDestEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpAdminState.setStatus("current")
_CfprSwEthMonDestEpAggrPortId_Type = Gauge32
_CfprSwEthMonDestEpAggrPortId_Object = MibTableColumn
cfprSwEthMonDestEpAggrPortId = _CfprSwEthMonDestEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 6),
    _CfprSwEthMonDestEpAggrPortId_Type()
)
cfprSwEthMonDestEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpAggrPortId.setStatus("current")
_CfprSwEthMonDestEpChassisId_Type = Gauge32
_CfprSwEthMonDestEpChassisId_Object = MibTableColumn
cfprSwEthMonDestEpChassisId = _CfprSwEthMonDestEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 7),
    _CfprSwEthMonDestEpChassisId_Type()
)
cfprSwEthMonDestEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpChassisId.setStatus("current")
_CfprSwEthMonDestEpEpDn_Type = SnmpAdminString
_CfprSwEthMonDestEpEpDn_Object = MibTableColumn
cfprSwEthMonDestEpEpDn = _CfprSwEthMonDestEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 8),
    _CfprSwEthMonDestEpEpDn_Type()
)
cfprSwEthMonDestEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpEpDn.setStatus("current")
_CfprSwEthMonDestEpIfRole_Type = CfprNetworkPortRole
_CfprSwEthMonDestEpIfRole_Object = MibTableColumn
cfprSwEthMonDestEpIfRole = _CfprSwEthMonDestEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 9),
    _CfprSwEthMonDestEpIfRole_Type()
)
cfprSwEthMonDestEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpIfRole.setStatus("current")
_CfprSwEthMonDestEpIfType_Type = CfprSwPIoEpIfType
_CfprSwEthMonDestEpIfType_Object = MibTableColumn
cfprSwEthMonDestEpIfType = _CfprSwEthMonDestEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 10),
    _CfprSwEthMonDestEpIfType_Type()
)
cfprSwEthMonDestEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpIfType.setStatus("current")
_CfprSwEthMonDestEpLc_Type = CfprSwPIoEpLc
_CfprSwEthMonDestEpLc_Object = MibTableColumn
cfprSwEthMonDestEpLc = _CfprSwEthMonDestEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 11),
    _CfprSwEthMonDestEpLc_Type()
)
cfprSwEthMonDestEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpLc.setStatus("current")
_CfprSwEthMonDestEpLocale_Type = CfprNetworkLocale
_CfprSwEthMonDestEpLocale_Object = MibTableColumn
cfprSwEthMonDestEpLocale = _CfprSwEthMonDestEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 12),
    _CfprSwEthMonDestEpLocale_Type()
)
cfprSwEthMonDestEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpLocale.setStatus("current")
_CfprSwEthMonDestEpName_Type = SnmpAdminString
_CfprSwEthMonDestEpName_Object = MibTableColumn
cfprSwEthMonDestEpName = _CfprSwEthMonDestEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 13),
    _CfprSwEthMonDestEpName_Type()
)
cfprSwEthMonDestEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpName.setStatus("current")
_CfprSwEthMonDestEpPeerAggrPortId_Type = Gauge32
_CfprSwEthMonDestEpPeerAggrPortId_Object = MibTableColumn
cfprSwEthMonDestEpPeerAggrPortId = _CfprSwEthMonDestEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 14),
    _CfprSwEthMonDestEpPeerAggrPortId_Type()
)
cfprSwEthMonDestEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpPeerAggrPortId.setStatus("current")
_CfprSwEthMonDestEpPeerChassisId_Type = Gauge32
_CfprSwEthMonDestEpPeerChassisId_Object = MibTableColumn
cfprSwEthMonDestEpPeerChassisId = _CfprSwEthMonDestEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 15),
    _CfprSwEthMonDestEpPeerChassisId_Type()
)
cfprSwEthMonDestEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpPeerChassisId.setStatus("current")
_CfprSwEthMonDestEpPeerDn_Type = SnmpAdminString
_CfprSwEthMonDestEpPeerDn_Object = MibTableColumn
cfprSwEthMonDestEpPeerDn = _CfprSwEthMonDestEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 16),
    _CfprSwEthMonDestEpPeerDn_Type()
)
cfprSwEthMonDestEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpPeerDn.setStatus("current")
_CfprSwEthMonDestEpPeerPortId_Type = Gauge32
_CfprSwEthMonDestEpPeerPortId_Object = MibTableColumn
cfprSwEthMonDestEpPeerPortId = _CfprSwEthMonDestEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 17),
    _CfprSwEthMonDestEpPeerPortId_Type()
)
cfprSwEthMonDestEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpPeerPortId.setStatus("current")
_CfprSwEthMonDestEpPeerSlotId_Type = Gauge32
_CfprSwEthMonDestEpPeerSlotId_Object = MibTableColumn
cfprSwEthMonDestEpPeerSlotId = _CfprSwEthMonDestEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 18),
    _CfprSwEthMonDestEpPeerSlotId_Type()
)
cfprSwEthMonDestEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpPeerSlotId.setStatus("current")
_CfprSwEthMonDestEpPortId_Type = Gauge32
_CfprSwEthMonDestEpPortId_Object = MibTableColumn
cfprSwEthMonDestEpPortId = _CfprSwEthMonDestEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 19),
    _CfprSwEthMonDestEpPortId_Type()
)
cfprSwEthMonDestEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpPortId.setStatus("current")
_CfprSwEthMonDestEpSlotId_Type = Gauge32
_CfprSwEthMonDestEpSlotId_Object = MibTableColumn
cfprSwEthMonDestEpSlotId = _CfprSwEthMonDestEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 20),
    _CfprSwEthMonDestEpSlotId_Type()
)
cfprSwEthMonDestEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpSlotId.setStatus("current")
_CfprSwEthMonDestEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthMonDestEpSwitchId_Object = MibTableColumn
cfprSwEthMonDestEpSwitchId = _CfprSwEthMonDestEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 21),
    _CfprSwEthMonDestEpSwitchId_Type()
)
cfprSwEthMonDestEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpSwitchId.setStatus("current")
_CfprSwEthMonDestEpTransport_Type = CfprSwEthMonDestEpTransport
_CfprSwEthMonDestEpTransport_Object = MibTableColumn
cfprSwEthMonDestEpTransport = _CfprSwEthMonDestEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 22),
    _CfprSwEthMonDestEpTransport_Type()
)
cfprSwEthMonDestEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpTransport.setStatus("current")
_CfprSwEthMonDestEpType_Type = CfprNetworkConnectionType
_CfprSwEthMonDestEpType_Object = MibTableColumn
cfprSwEthMonDestEpType = _CfprSwEthMonDestEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 25, 1, 23),
    _CfprSwEthMonDestEpType_Type()
)
cfprSwEthMonDestEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonDestEpType.setStatus("current")
_CfprSwEthMonFsmTable_Object = MibTable
cfprSwEthMonFsmTable = _CfprSwEthMonFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26)
)
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTable.setStatus("current")
_CfprSwEthMonFsmEntry_Object = MibTableRow
cfprSwEthMonFsmEntry = _CfprSwEthMonFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1)
)
cfprSwEthMonFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthMonFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthMonFsmEntry.setStatus("current")
_CfprSwEthMonFsmInstanceId_Type = CfprManagedObjectId
_CfprSwEthMonFsmInstanceId_Object = MibTableColumn
cfprSwEthMonFsmInstanceId = _CfprSwEthMonFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 1),
    _CfprSwEthMonFsmInstanceId_Type()
)
cfprSwEthMonFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmInstanceId.setStatus("current")
_CfprSwEthMonFsmDn_Type = CfprManagedObjectDn
_CfprSwEthMonFsmDn_Object = MibTableColumn
cfprSwEthMonFsmDn = _CfprSwEthMonFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 2),
    _CfprSwEthMonFsmDn_Type()
)
cfprSwEthMonFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmDn.setStatus("current")
_CfprSwEthMonFsmRn_Type = SnmpAdminString
_CfprSwEthMonFsmRn_Object = MibTableColumn
cfprSwEthMonFsmRn = _CfprSwEthMonFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 3),
    _CfprSwEthMonFsmRn_Type()
)
cfprSwEthMonFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmRn.setStatus("current")
_CfprSwEthMonFsmCompletionTime_Type = DateAndTime
_CfprSwEthMonFsmCompletionTime_Object = MibTableColumn
cfprSwEthMonFsmCompletionTime = _CfprSwEthMonFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 4),
    _CfprSwEthMonFsmCompletionTime_Type()
)
cfprSwEthMonFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmCompletionTime.setStatus("current")
_CfprSwEthMonFsmCurrentFsm_Type = CfprSwEthMonFsmCurrentFsm
_CfprSwEthMonFsmCurrentFsm_Object = MibTableColumn
cfprSwEthMonFsmCurrentFsm = _CfprSwEthMonFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 5),
    _CfprSwEthMonFsmCurrentFsm_Type()
)
cfprSwEthMonFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmCurrentFsm.setStatus("current")
_CfprSwEthMonFsmDescrData_Type = SnmpAdminString
_CfprSwEthMonFsmDescrData_Object = MibTableColumn
cfprSwEthMonFsmDescrData = _CfprSwEthMonFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 6),
    _CfprSwEthMonFsmDescrData_Type()
)
cfprSwEthMonFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmDescrData.setStatus("current")
_CfprSwEthMonFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwEthMonFsmFsmStatus_Object = MibTableColumn
cfprSwEthMonFsmFsmStatus = _CfprSwEthMonFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 7),
    _CfprSwEthMonFsmFsmStatus_Type()
)
cfprSwEthMonFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmFsmStatus.setStatus("current")
_CfprSwEthMonFsmProgress_Type = Gauge32
_CfprSwEthMonFsmProgress_Object = MibTableColumn
cfprSwEthMonFsmProgress = _CfprSwEthMonFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 8),
    _CfprSwEthMonFsmProgress_Type()
)
cfprSwEthMonFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmProgress.setStatus("current")
_CfprSwEthMonFsmRmtErrCode_Type = Gauge32
_CfprSwEthMonFsmRmtErrCode_Object = MibTableColumn
cfprSwEthMonFsmRmtErrCode = _CfprSwEthMonFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 9),
    _CfprSwEthMonFsmRmtErrCode_Type()
)
cfprSwEthMonFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmRmtErrCode.setStatus("current")
_CfprSwEthMonFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwEthMonFsmRmtErrDescr_Object = MibTableColumn
cfprSwEthMonFsmRmtErrDescr = _CfprSwEthMonFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 10),
    _CfprSwEthMonFsmRmtErrDescr_Type()
)
cfprSwEthMonFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmRmtErrDescr.setStatus("current")
_CfprSwEthMonFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwEthMonFsmRmtRslt_Object = MibTableColumn
cfprSwEthMonFsmRmtRslt = _CfprSwEthMonFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 26, 1, 11),
    _CfprSwEthMonFsmRmtRslt_Type()
)
cfprSwEthMonFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmRmtRslt.setStatus("current")
_CfprSwEthMonFsmStageTable_Object = MibTable
cfprSwEthMonFsmStageTable = _CfprSwEthMonFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27)
)
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageTable.setStatus("current")
_CfprSwEthMonFsmStageEntry_Object = MibTableRow
cfprSwEthMonFsmStageEntry = _CfprSwEthMonFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1)
)
cfprSwEthMonFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthMonFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageEntry.setStatus("current")
_CfprSwEthMonFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwEthMonFsmStageInstanceId_Object = MibTableColumn
cfprSwEthMonFsmStageInstanceId = _CfprSwEthMonFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 1),
    _CfprSwEthMonFsmStageInstanceId_Type()
)
cfprSwEthMonFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageInstanceId.setStatus("current")
_CfprSwEthMonFsmStageDn_Type = CfprManagedObjectDn
_CfprSwEthMonFsmStageDn_Object = MibTableColumn
cfprSwEthMonFsmStageDn = _CfprSwEthMonFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 2),
    _CfprSwEthMonFsmStageDn_Type()
)
cfprSwEthMonFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageDn.setStatus("current")
_CfprSwEthMonFsmStageRn_Type = SnmpAdminString
_CfprSwEthMonFsmStageRn_Object = MibTableColumn
cfprSwEthMonFsmStageRn = _CfprSwEthMonFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 3),
    _CfprSwEthMonFsmStageRn_Type()
)
cfprSwEthMonFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageRn.setStatus("current")
_CfprSwEthMonFsmStageDescrData_Type = SnmpAdminString
_CfprSwEthMonFsmStageDescrData_Object = MibTableColumn
cfprSwEthMonFsmStageDescrData = _CfprSwEthMonFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 4),
    _CfprSwEthMonFsmStageDescrData_Type()
)
cfprSwEthMonFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageDescrData.setStatus("current")
_CfprSwEthMonFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwEthMonFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwEthMonFsmStageLastUpdateTime = _CfprSwEthMonFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 5),
    _CfprSwEthMonFsmStageLastUpdateTime_Type()
)
cfprSwEthMonFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageLastUpdateTime.setStatus("current")
_CfprSwEthMonFsmStageName_Type = CfprSwEthMonFsmStageName
_CfprSwEthMonFsmStageName_Object = MibTableColumn
cfprSwEthMonFsmStageName = _CfprSwEthMonFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 6),
    _CfprSwEthMonFsmStageName_Type()
)
cfprSwEthMonFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageName.setStatus("current")
_CfprSwEthMonFsmStageOrder_Type = Gauge32
_CfprSwEthMonFsmStageOrder_Object = MibTableColumn
cfprSwEthMonFsmStageOrder = _CfprSwEthMonFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 7),
    _CfprSwEthMonFsmStageOrder_Type()
)
cfprSwEthMonFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageOrder.setStatus("current")
_CfprSwEthMonFsmStageRetry_Type = Gauge32
_CfprSwEthMonFsmStageRetry_Object = MibTableColumn
cfprSwEthMonFsmStageRetry = _CfprSwEthMonFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 8),
    _CfprSwEthMonFsmStageRetry_Type()
)
cfprSwEthMonFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageRetry.setStatus("current")
_CfprSwEthMonFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwEthMonFsmStageStageStatus_Object = MibTableColumn
cfprSwEthMonFsmStageStageStatus = _CfprSwEthMonFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 27, 1, 9),
    _CfprSwEthMonFsmStageStageStatus_Type()
)
cfprSwEthMonFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmStageStageStatus.setStatus("current")
_CfprSwEthMonFsmTaskTable_Object = MibTable
cfprSwEthMonFsmTaskTable = _CfprSwEthMonFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28)
)
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskTable.setStatus("current")
_CfprSwEthMonFsmTaskEntry_Object = MibTableRow
cfprSwEthMonFsmTaskEntry = _CfprSwEthMonFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28, 1)
)
cfprSwEthMonFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthMonFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskEntry.setStatus("current")
_CfprSwEthMonFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwEthMonFsmTaskInstanceId_Object = MibTableColumn
cfprSwEthMonFsmTaskInstanceId = _CfprSwEthMonFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28, 1, 1),
    _CfprSwEthMonFsmTaskInstanceId_Type()
)
cfprSwEthMonFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskInstanceId.setStatus("current")
_CfprSwEthMonFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwEthMonFsmTaskDn_Object = MibTableColumn
cfprSwEthMonFsmTaskDn = _CfprSwEthMonFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28, 1, 2),
    _CfprSwEthMonFsmTaskDn_Type()
)
cfprSwEthMonFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskDn.setStatus("current")
_CfprSwEthMonFsmTaskRn_Type = SnmpAdminString
_CfprSwEthMonFsmTaskRn_Object = MibTableColumn
cfprSwEthMonFsmTaskRn = _CfprSwEthMonFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28, 1, 3),
    _CfprSwEthMonFsmTaskRn_Type()
)
cfprSwEthMonFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskRn.setStatus("current")
_CfprSwEthMonFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwEthMonFsmTaskCompletion_Object = MibTableColumn
cfprSwEthMonFsmTaskCompletion = _CfprSwEthMonFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28, 1, 4),
    _CfprSwEthMonFsmTaskCompletion_Type()
)
cfprSwEthMonFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskCompletion.setStatus("current")
_CfprSwEthMonFsmTaskFlags_Type = CfprFsmFlags
_CfprSwEthMonFsmTaskFlags_Object = MibTableColumn
cfprSwEthMonFsmTaskFlags = _CfprSwEthMonFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28, 1, 5),
    _CfprSwEthMonFsmTaskFlags_Type()
)
cfprSwEthMonFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskFlags.setStatus("current")
_CfprSwEthMonFsmTaskItem_Type = CfprSwEthMonFsmTaskItem
_CfprSwEthMonFsmTaskItem_Object = MibTableColumn
cfprSwEthMonFsmTaskItem = _CfprSwEthMonFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28, 1, 6),
    _CfprSwEthMonFsmTaskItem_Type()
)
cfprSwEthMonFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskItem.setStatus("current")
_CfprSwEthMonFsmTaskSeqId_Type = Gauge32
_CfprSwEthMonFsmTaskSeqId_Object = MibTableColumn
cfprSwEthMonFsmTaskSeqId = _CfprSwEthMonFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 28, 1, 7),
    _CfprSwEthMonFsmTaskSeqId_Type()
)
cfprSwEthMonFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonFsmTaskSeqId.setStatus("current")
_CfprSwEthMonSrcEpTable_Object = MibTable
cfprSwEthMonSrcEpTable = _CfprSwEthMonSrcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29)
)
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpTable.setStatus("current")
_CfprSwEthMonSrcEpEntry_Object = MibTableRow
cfprSwEthMonSrcEpEntry = _CfprSwEthMonSrcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1)
)
cfprSwEthMonSrcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthMonSrcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpEntry.setStatus("current")
_CfprSwEthMonSrcEpInstanceId_Type = CfprManagedObjectId
_CfprSwEthMonSrcEpInstanceId_Object = MibTableColumn
cfprSwEthMonSrcEpInstanceId = _CfprSwEthMonSrcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 1),
    _CfprSwEthMonSrcEpInstanceId_Type()
)
cfprSwEthMonSrcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpInstanceId.setStatus("current")
_CfprSwEthMonSrcEpDn_Type = CfprManagedObjectDn
_CfprSwEthMonSrcEpDn_Object = MibTableColumn
cfprSwEthMonSrcEpDn = _CfprSwEthMonSrcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 2),
    _CfprSwEthMonSrcEpDn_Type()
)
cfprSwEthMonSrcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpDn.setStatus("current")
_CfprSwEthMonSrcEpRn_Type = SnmpAdminString
_CfprSwEthMonSrcEpRn_Object = MibTableColumn
cfprSwEthMonSrcEpRn = _CfprSwEthMonSrcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 3),
    _CfprSwEthMonSrcEpRn_Type()
)
cfprSwEthMonSrcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpRn.setStatus("current")
_CfprSwEthMonSrcEpAdminState_Type = CfprFabricAdminState
_CfprSwEthMonSrcEpAdminState_Object = MibTableColumn
cfprSwEthMonSrcEpAdminState = _CfprSwEthMonSrcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 4),
    _CfprSwEthMonSrcEpAdminState_Type()
)
cfprSwEthMonSrcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpAdminState.setStatus("current")
_CfprSwEthMonSrcEpAggrPortId_Type = Gauge32
_CfprSwEthMonSrcEpAggrPortId_Object = MibTableColumn
cfprSwEthMonSrcEpAggrPortId = _CfprSwEthMonSrcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 5),
    _CfprSwEthMonSrcEpAggrPortId_Type()
)
cfprSwEthMonSrcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpAggrPortId.setStatus("current")
_CfprSwEthMonSrcEpChassisId_Type = Gauge32
_CfprSwEthMonSrcEpChassisId_Object = MibTableColumn
cfprSwEthMonSrcEpChassisId = _CfprSwEthMonSrcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 6),
    _CfprSwEthMonSrcEpChassisId_Type()
)
cfprSwEthMonSrcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpChassisId.setStatus("current")
_CfprSwEthMonSrcEpEpDn_Type = SnmpAdminString
_CfprSwEthMonSrcEpEpDn_Object = MibTableColumn
cfprSwEthMonSrcEpEpDn = _CfprSwEthMonSrcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 7),
    _CfprSwEthMonSrcEpEpDn_Type()
)
cfprSwEthMonSrcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpEpDn.setStatus("current")
_CfprSwEthMonSrcEpIfRole_Type = CfprNetworkPortRole
_CfprSwEthMonSrcEpIfRole_Object = MibTableColumn
cfprSwEthMonSrcEpIfRole = _CfprSwEthMonSrcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 8),
    _CfprSwEthMonSrcEpIfRole_Type()
)
cfprSwEthMonSrcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpIfRole.setStatus("current")
_CfprSwEthMonSrcEpIfType_Type = CfprSwPIoEpIfType
_CfprSwEthMonSrcEpIfType_Object = MibTableColumn
cfprSwEthMonSrcEpIfType = _CfprSwEthMonSrcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 9),
    _CfprSwEthMonSrcEpIfType_Type()
)
cfprSwEthMonSrcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpIfType.setStatus("current")
_CfprSwEthMonSrcEpLc_Type = CfprSwPIoEpLc
_CfprSwEthMonSrcEpLc_Object = MibTableColumn
cfprSwEthMonSrcEpLc = _CfprSwEthMonSrcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 10),
    _CfprSwEthMonSrcEpLc_Type()
)
cfprSwEthMonSrcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpLc.setStatus("current")
_CfprSwEthMonSrcEpLocale_Type = CfprSwMonSrcEpLocale
_CfprSwEthMonSrcEpLocale_Object = MibTableColumn
cfprSwEthMonSrcEpLocale = _CfprSwEthMonSrcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 11),
    _CfprSwEthMonSrcEpLocale_Type()
)
cfprSwEthMonSrcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpLocale.setStatus("current")
_CfprSwEthMonSrcEpMonTrafDir_Type = CfprFabricTrafficDirection
_CfprSwEthMonSrcEpMonTrafDir_Object = MibTableColumn
cfprSwEthMonSrcEpMonTrafDir = _CfprSwEthMonSrcEpMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 12),
    _CfprSwEthMonSrcEpMonTrafDir_Type()
)
cfprSwEthMonSrcEpMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpMonTrafDir.setStatus("current")
_CfprSwEthMonSrcEpName_Type = SnmpAdminString
_CfprSwEthMonSrcEpName_Object = MibTableColumn
cfprSwEthMonSrcEpName = _CfprSwEthMonSrcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 13),
    _CfprSwEthMonSrcEpName_Type()
)
cfprSwEthMonSrcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpName.setStatus("current")
_CfprSwEthMonSrcEpPeerAggrPortId_Type = Gauge32
_CfprSwEthMonSrcEpPeerAggrPortId_Object = MibTableColumn
cfprSwEthMonSrcEpPeerAggrPortId = _CfprSwEthMonSrcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 14),
    _CfprSwEthMonSrcEpPeerAggrPortId_Type()
)
cfprSwEthMonSrcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpPeerAggrPortId.setStatus("current")
_CfprSwEthMonSrcEpPeerChassisId_Type = Gauge32
_CfprSwEthMonSrcEpPeerChassisId_Object = MibTableColumn
cfprSwEthMonSrcEpPeerChassisId = _CfprSwEthMonSrcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 15),
    _CfprSwEthMonSrcEpPeerChassisId_Type()
)
cfprSwEthMonSrcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpPeerChassisId.setStatus("current")
_CfprSwEthMonSrcEpPeerDn_Type = SnmpAdminString
_CfprSwEthMonSrcEpPeerDn_Object = MibTableColumn
cfprSwEthMonSrcEpPeerDn = _CfprSwEthMonSrcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 16),
    _CfprSwEthMonSrcEpPeerDn_Type()
)
cfprSwEthMonSrcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpPeerDn.setStatus("current")
_CfprSwEthMonSrcEpPeerPortId_Type = Gauge32
_CfprSwEthMonSrcEpPeerPortId_Object = MibTableColumn
cfprSwEthMonSrcEpPeerPortId = _CfprSwEthMonSrcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 17),
    _CfprSwEthMonSrcEpPeerPortId_Type()
)
cfprSwEthMonSrcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpPeerPortId.setStatus("current")
_CfprSwEthMonSrcEpPeerSlotId_Type = Gauge32
_CfprSwEthMonSrcEpPeerSlotId_Object = MibTableColumn
cfprSwEthMonSrcEpPeerSlotId = _CfprSwEthMonSrcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 18),
    _CfprSwEthMonSrcEpPeerSlotId_Type()
)
cfprSwEthMonSrcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpPeerSlotId.setStatus("current")
_CfprSwEthMonSrcEpPortId_Type = Gauge32
_CfprSwEthMonSrcEpPortId_Object = MibTableColumn
cfprSwEthMonSrcEpPortId = _CfprSwEthMonSrcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 19),
    _CfprSwEthMonSrcEpPortId_Type()
)
cfprSwEthMonSrcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpPortId.setStatus("current")
_CfprSwEthMonSrcEpSlotId_Type = Gauge32
_CfprSwEthMonSrcEpSlotId_Object = MibTableColumn
cfprSwEthMonSrcEpSlotId = _CfprSwEthMonSrcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 20),
    _CfprSwEthMonSrcEpSlotId_Type()
)
cfprSwEthMonSrcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpSlotId.setStatus("current")
_CfprSwEthMonSrcEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthMonSrcEpSwitchId_Object = MibTableColumn
cfprSwEthMonSrcEpSwitchId = _CfprSwEthMonSrcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 21),
    _CfprSwEthMonSrcEpSwitchId_Type()
)
cfprSwEthMonSrcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpSwitchId.setStatus("current")
_CfprSwEthMonSrcEpTransport_Type = CfprSwEthMonSrcEpTransport
_CfprSwEthMonSrcEpTransport_Object = MibTableColumn
cfprSwEthMonSrcEpTransport = _CfprSwEthMonSrcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 22),
    _CfprSwEthMonSrcEpTransport_Type()
)
cfprSwEthMonSrcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpTransport.setStatus("current")
_CfprSwEthMonSrcEpType_Type = CfprNetworkConnectionType
_CfprSwEthMonSrcEpType_Object = MibTableColumn
cfprSwEthMonSrcEpType = _CfprSwEthMonSrcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 29, 1, 23),
    _CfprSwEthMonSrcEpType_Type()
)
cfprSwEthMonSrcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthMonSrcEpType.setStatus("current")
_CfprSwEthTargetEpTable_Object = MibTable
cfprSwEthTargetEpTable = _CfprSwEthTargetEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30)
)
if mibBuilder.loadTexts:
    cfprSwEthTargetEpTable.setStatus("current")
_CfprSwEthTargetEpEntry_Object = MibTableRow
cfprSwEthTargetEpEntry = _CfprSwEthTargetEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1)
)
cfprSwEthTargetEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwEthTargetEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwEthTargetEpEntry.setStatus("current")
_CfprSwEthTargetEpInstanceId_Type = CfprManagedObjectId
_CfprSwEthTargetEpInstanceId_Object = MibTableColumn
cfprSwEthTargetEpInstanceId = _CfprSwEthTargetEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 1),
    _CfprSwEthTargetEpInstanceId_Type()
)
cfprSwEthTargetEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpInstanceId.setStatus("current")
_CfprSwEthTargetEpDn_Type = CfprManagedObjectDn
_CfprSwEthTargetEpDn_Object = MibTableColumn
cfprSwEthTargetEpDn = _CfprSwEthTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 2),
    _CfprSwEthTargetEpDn_Type()
)
cfprSwEthTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpDn.setStatus("current")
_CfprSwEthTargetEpRn_Type = SnmpAdminString
_CfprSwEthTargetEpRn_Object = MibTableColumn
cfprSwEthTargetEpRn = _CfprSwEthTargetEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 3),
    _CfprSwEthTargetEpRn_Type()
)
cfprSwEthTargetEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpRn.setStatus("current")
_CfprSwEthTargetEpAdminState_Type = CfprSwEthTargetEpAdminState
_CfprSwEthTargetEpAdminState_Object = MibTableColumn
cfprSwEthTargetEpAdminState = _CfprSwEthTargetEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 4),
    _CfprSwEthTargetEpAdminState_Type()
)
cfprSwEthTargetEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpAdminState.setStatus("current")
_CfprSwEthTargetEpAggrPortId_Type = Gauge32
_CfprSwEthTargetEpAggrPortId_Object = MibTableColumn
cfprSwEthTargetEpAggrPortId = _CfprSwEthTargetEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 5),
    _CfprSwEthTargetEpAggrPortId_Type()
)
cfprSwEthTargetEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpAggrPortId.setStatus("current")
_CfprSwEthTargetEpChassisId_Type = Gauge32
_CfprSwEthTargetEpChassisId_Object = MibTableColumn
cfprSwEthTargetEpChassisId = _CfprSwEthTargetEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 6),
    _CfprSwEthTargetEpChassisId_Type()
)
cfprSwEthTargetEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpChassisId.setStatus("current")
_CfprSwEthTargetEpEpDn_Type = SnmpAdminString
_CfprSwEthTargetEpEpDn_Object = MibTableColumn
cfprSwEthTargetEpEpDn = _CfprSwEthTargetEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 7),
    _CfprSwEthTargetEpEpDn_Type()
)
cfprSwEthTargetEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpEpDn.setStatus("current")
_CfprSwEthTargetEpFltAggr_Type = Unsigned64
_CfprSwEthTargetEpFltAggr_Object = MibTableColumn
cfprSwEthTargetEpFltAggr = _CfprSwEthTargetEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 8),
    _CfprSwEthTargetEpFltAggr_Type()
)
cfprSwEthTargetEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpFltAggr.setStatus("current")
_CfprSwEthTargetEpIfRole_Type = CfprNetworkPortRole
_CfprSwEthTargetEpIfRole_Object = MibTableColumn
cfprSwEthTargetEpIfRole = _CfprSwEthTargetEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 9),
    _CfprSwEthTargetEpIfRole_Type()
)
cfprSwEthTargetEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpIfRole.setStatus("current")
_CfprSwEthTargetEpIfType_Type = CfprFabricPIoEpIfType
_CfprSwEthTargetEpIfType_Object = MibTableColumn
cfprSwEthTargetEpIfType = _CfprSwEthTargetEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 10),
    _CfprSwEthTargetEpIfType_Type()
)
cfprSwEthTargetEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpIfType.setStatus("current")
_CfprSwEthTargetEpLicGP_Type = Unsigned64
_CfprSwEthTargetEpLicGP_Object = MibTableColumn
cfprSwEthTargetEpLicGP = _CfprSwEthTargetEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 11),
    _CfprSwEthTargetEpLicGP_Type()
)
cfprSwEthTargetEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpLicGP.setStatus("current")
_CfprSwEthTargetEpLicState_Type = CfprLicenseState
_CfprSwEthTargetEpLicState_Object = MibTableColumn
cfprSwEthTargetEpLicState = _CfprSwEthTargetEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 12),
    _CfprSwEthTargetEpLicState_Type()
)
cfprSwEthTargetEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpLicState.setStatus("current")
_CfprSwEthTargetEpLocale_Type = CfprFabricExternalEpLocale
_CfprSwEthTargetEpLocale_Object = MibTableColumn
cfprSwEthTargetEpLocale = _CfprSwEthTargetEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 13),
    _CfprSwEthTargetEpLocale_Type()
)
cfprSwEthTargetEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpLocale.setStatus("current")
_CfprSwEthTargetEpMacAddress_Type = MacAddress
_CfprSwEthTargetEpMacAddress_Object = MibTableColumn
cfprSwEthTargetEpMacAddress = _CfprSwEthTargetEpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 14),
    _CfprSwEthTargetEpMacAddress_Type()
)
cfprSwEthTargetEpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpMacAddress.setStatus("current")
_CfprSwEthTargetEpName_Type = SnmpAdminString
_CfprSwEthTargetEpName_Object = MibTableColumn
cfprSwEthTargetEpName = _CfprSwEthTargetEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 15),
    _CfprSwEthTargetEpName_Type()
)
cfprSwEthTargetEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpName.setStatus("current")
_CfprSwEthTargetEpOperState_Type = CfprFabricPIoEpOperState
_CfprSwEthTargetEpOperState_Object = MibTableColumn
cfprSwEthTargetEpOperState = _CfprSwEthTargetEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 16),
    _CfprSwEthTargetEpOperState_Type()
)
cfprSwEthTargetEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpOperState.setStatus("current")
_CfprSwEthTargetEpOperStateReason_Type = SnmpAdminString
_CfprSwEthTargetEpOperStateReason_Object = MibTableColumn
cfprSwEthTargetEpOperStateReason = _CfprSwEthTargetEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 17),
    _CfprSwEthTargetEpOperStateReason_Type()
)
cfprSwEthTargetEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpOperStateReason.setStatus("current")
_CfprSwEthTargetEpPeerAggrPortId_Type = Gauge32
_CfprSwEthTargetEpPeerAggrPortId_Object = MibTableColumn
cfprSwEthTargetEpPeerAggrPortId = _CfprSwEthTargetEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 18),
    _CfprSwEthTargetEpPeerAggrPortId_Type()
)
cfprSwEthTargetEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpPeerAggrPortId.setStatus("current")
_CfprSwEthTargetEpPeerChassisId_Type = Gauge32
_CfprSwEthTargetEpPeerChassisId_Object = MibTableColumn
cfprSwEthTargetEpPeerChassisId = _CfprSwEthTargetEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 19),
    _CfprSwEthTargetEpPeerChassisId_Type()
)
cfprSwEthTargetEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpPeerChassisId.setStatus("current")
_CfprSwEthTargetEpPeerDn_Type = SnmpAdminString
_CfprSwEthTargetEpPeerDn_Object = MibTableColumn
cfprSwEthTargetEpPeerDn = _CfprSwEthTargetEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 20),
    _CfprSwEthTargetEpPeerDn_Type()
)
cfprSwEthTargetEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpPeerDn.setStatus("current")
_CfprSwEthTargetEpPeerPortId_Type = Gauge32
_CfprSwEthTargetEpPeerPortId_Object = MibTableColumn
cfprSwEthTargetEpPeerPortId = _CfprSwEthTargetEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 21),
    _CfprSwEthTargetEpPeerPortId_Type()
)
cfprSwEthTargetEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpPeerPortId.setStatus("current")
_CfprSwEthTargetEpPeerSlotId_Type = Gauge32
_CfprSwEthTargetEpPeerSlotId_Object = MibTableColumn
cfprSwEthTargetEpPeerSlotId = _CfprSwEthTargetEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 22),
    _CfprSwEthTargetEpPeerSlotId_Type()
)
cfprSwEthTargetEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpPeerSlotId.setStatus("current")
_CfprSwEthTargetEpPortId_Type = CfprFabricPIoEpPortId
_CfprSwEthTargetEpPortId_Object = MibTableColumn
cfprSwEthTargetEpPortId = _CfprSwEthTargetEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 23),
    _CfprSwEthTargetEpPortId_Type()
)
cfprSwEthTargetEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpPortId.setStatus("current")
_CfprSwEthTargetEpSlotId_Type = CfprFabricPIoEpSlotId
_CfprSwEthTargetEpSlotId_Object = MibTableColumn
cfprSwEthTargetEpSlotId = _CfprSwEthTargetEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 24),
    _CfprSwEthTargetEpSlotId_Type()
)
cfprSwEthTargetEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpSlotId.setStatus("current")
_CfprSwEthTargetEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwEthTargetEpSwitchId_Object = MibTableColumn
cfprSwEthTargetEpSwitchId = _CfprSwEthTargetEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 25),
    _CfprSwEthTargetEpSwitchId_Type()
)
cfprSwEthTargetEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpSwitchId.setStatus("current")
_CfprSwEthTargetEpTransport_Type = CfprSwEthTargetEpTransport
_CfprSwEthTargetEpTransport_Object = MibTableColumn
cfprSwEthTargetEpTransport = _CfprSwEthTargetEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 26),
    _CfprSwEthTargetEpTransport_Type()
)
cfprSwEthTargetEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpTransport.setStatus("current")
_CfprSwEthTargetEpType_Type = CfprSwTargetEpType
_CfprSwEthTargetEpType_Object = MibTableColumn
cfprSwEthTargetEpType = _CfprSwEthTargetEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 27),
    _CfprSwEthTargetEpType_Type()
)
cfprSwEthTargetEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpType.setStatus("current")
_CfprSwEthTargetEpWarnings_Type = CfprFabricWarnings
_CfprSwEthTargetEpWarnings_Object = MibTableColumn
cfprSwEthTargetEpWarnings = _CfprSwEthTargetEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 30, 1, 28),
    _CfprSwEthTargetEpWarnings_Type()
)
cfprSwEthTargetEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwEthTargetEpWarnings.setStatus("current")
_CfprSwExtUtilityTable_Object = MibTable
cfprSwExtUtilityTable = _CfprSwExtUtilityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31)
)
if mibBuilder.loadTexts:
    cfprSwExtUtilityTable.setStatus("current")
_CfprSwExtUtilityEntry_Object = MibTableRow
cfprSwExtUtilityEntry = _CfprSwExtUtilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1)
)
cfprSwExtUtilityEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwExtUtilityInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwExtUtilityEntry.setStatus("current")
_CfprSwExtUtilityInstanceId_Type = CfprManagedObjectId
_CfprSwExtUtilityInstanceId_Object = MibTableColumn
cfprSwExtUtilityInstanceId = _CfprSwExtUtilityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 1),
    _CfprSwExtUtilityInstanceId_Type()
)
cfprSwExtUtilityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwExtUtilityInstanceId.setStatus("current")
_CfprSwExtUtilityDn_Type = CfprManagedObjectDn
_CfprSwExtUtilityDn_Object = MibTableColumn
cfprSwExtUtilityDn = _CfprSwExtUtilityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 2),
    _CfprSwExtUtilityDn_Type()
)
cfprSwExtUtilityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityDn.setStatus("current")
_CfprSwExtUtilityRn_Type = SnmpAdminString
_CfprSwExtUtilityRn_Object = MibTableColumn
cfprSwExtUtilityRn = _CfprSwExtUtilityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 3),
    _CfprSwExtUtilityRn_Type()
)
cfprSwExtUtilityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityRn.setStatus("current")
_CfprSwExtUtilityConfMode_Type = CfprSwConfMode
_CfprSwExtUtilityConfMode_Object = MibTableColumn
cfprSwExtUtilityConfMode = _CfprSwExtUtilityConfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 4),
    _CfprSwExtUtilityConfMode_Type()
)
cfprSwExtUtilityConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityConfMode.setStatus("current")
_CfprSwExtUtilityFsmDescr_Type = SnmpAdminString
_CfprSwExtUtilityFsmDescr_Object = MibTableColumn
cfprSwExtUtilityFsmDescr = _CfprSwExtUtilityFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 5),
    _CfprSwExtUtilityFsmDescr_Type()
)
cfprSwExtUtilityFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmDescr.setStatus("current")
_CfprSwExtUtilityFsmPrev_Type = SnmpAdminString
_CfprSwExtUtilityFsmPrev_Object = MibTableColumn
cfprSwExtUtilityFsmPrev = _CfprSwExtUtilityFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 6),
    _CfprSwExtUtilityFsmPrev_Type()
)
cfprSwExtUtilityFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmPrev.setStatus("current")
_CfprSwExtUtilityFsmProgr_Type = Gauge32
_CfprSwExtUtilityFsmProgr_Object = MibTableColumn
cfprSwExtUtilityFsmProgr = _CfprSwExtUtilityFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 7),
    _CfprSwExtUtilityFsmProgr_Type()
)
cfprSwExtUtilityFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmProgr.setStatus("current")
_CfprSwExtUtilityFsmRmtInvErrCode_Type = Gauge32
_CfprSwExtUtilityFsmRmtInvErrCode_Object = MibTableColumn
cfprSwExtUtilityFsmRmtInvErrCode = _CfprSwExtUtilityFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 8),
    _CfprSwExtUtilityFsmRmtInvErrCode_Type()
)
cfprSwExtUtilityFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmRmtInvErrCode.setStatus("current")
_CfprSwExtUtilityFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwExtUtilityFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwExtUtilityFsmRmtInvErrDescr = _CfprSwExtUtilityFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 9),
    _CfprSwExtUtilityFsmRmtInvErrDescr_Type()
)
cfprSwExtUtilityFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmRmtInvErrDescr.setStatus("current")
_CfprSwExtUtilityFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwExtUtilityFsmRmtInvRslt_Object = MibTableColumn
cfprSwExtUtilityFsmRmtInvRslt = _CfprSwExtUtilityFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 10),
    _CfprSwExtUtilityFsmRmtInvRslt_Type()
)
cfprSwExtUtilityFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmRmtInvRslt.setStatus("current")
_CfprSwExtUtilityFsmStageDescr_Type = SnmpAdminString
_CfprSwExtUtilityFsmStageDescr_Object = MibTableColumn
cfprSwExtUtilityFsmStageDescr = _CfprSwExtUtilityFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 11),
    _CfprSwExtUtilityFsmStageDescr_Type()
)
cfprSwExtUtilityFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageDescr.setStatus("current")
_CfprSwExtUtilityFsmStamp_Type = DateAndTime
_CfprSwExtUtilityFsmStamp_Object = MibTableColumn
cfprSwExtUtilityFsmStamp = _CfprSwExtUtilityFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 12),
    _CfprSwExtUtilityFsmStamp_Type()
)
cfprSwExtUtilityFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStamp.setStatus("current")
_CfprSwExtUtilityFsmStatus_Type = SnmpAdminString
_CfprSwExtUtilityFsmStatus_Object = MibTableColumn
cfprSwExtUtilityFsmStatus = _CfprSwExtUtilityFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 13),
    _CfprSwExtUtilityFsmStatus_Type()
)
cfprSwExtUtilityFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStatus.setStatus("current")
_CfprSwExtUtilityFsmTry_Type = Gauge32
_CfprSwExtUtilityFsmTry_Object = MibTableColumn
cfprSwExtUtilityFsmTry = _CfprSwExtUtilityFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 14),
    _CfprSwExtUtilityFsmTry_Type()
)
cfprSwExtUtilityFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTry.setStatus("current")
_CfprSwExtUtilitySwitchId_Type = CfprNetworkSwitchId
_CfprSwExtUtilitySwitchId_Object = MibTableColumn
cfprSwExtUtilitySwitchId = _CfprSwExtUtilitySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 31, 1, 15),
    _CfprSwExtUtilitySwitchId_Type()
)
cfprSwExtUtilitySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilitySwitchId.setStatus("current")
_CfprSwExtUtilityFsmTable_Object = MibTable
cfprSwExtUtilityFsmTable = _CfprSwExtUtilityFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32)
)
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTable.setStatus("current")
_CfprSwExtUtilityFsmEntry_Object = MibTableRow
cfprSwExtUtilityFsmEntry = _CfprSwExtUtilityFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1)
)
cfprSwExtUtilityFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwExtUtilityFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmEntry.setStatus("current")
_CfprSwExtUtilityFsmInstanceId_Type = CfprManagedObjectId
_CfprSwExtUtilityFsmInstanceId_Object = MibTableColumn
cfprSwExtUtilityFsmInstanceId = _CfprSwExtUtilityFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 1),
    _CfprSwExtUtilityFsmInstanceId_Type()
)
cfprSwExtUtilityFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmInstanceId.setStatus("current")
_CfprSwExtUtilityFsmDn_Type = CfprManagedObjectDn
_CfprSwExtUtilityFsmDn_Object = MibTableColumn
cfprSwExtUtilityFsmDn = _CfprSwExtUtilityFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 2),
    _CfprSwExtUtilityFsmDn_Type()
)
cfprSwExtUtilityFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmDn.setStatus("current")
_CfprSwExtUtilityFsmRn_Type = SnmpAdminString
_CfprSwExtUtilityFsmRn_Object = MibTableColumn
cfprSwExtUtilityFsmRn = _CfprSwExtUtilityFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 3),
    _CfprSwExtUtilityFsmRn_Type()
)
cfprSwExtUtilityFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmRn.setStatus("current")
_CfprSwExtUtilityFsmCompletionTime_Type = DateAndTime
_CfprSwExtUtilityFsmCompletionTime_Object = MibTableColumn
cfprSwExtUtilityFsmCompletionTime = _CfprSwExtUtilityFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 4),
    _CfprSwExtUtilityFsmCompletionTime_Type()
)
cfprSwExtUtilityFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmCompletionTime.setStatus("current")
_CfprSwExtUtilityFsmCurrentFsm_Type = CfprSwExtUtilityFsmCurrentFsm
_CfprSwExtUtilityFsmCurrentFsm_Object = MibTableColumn
cfprSwExtUtilityFsmCurrentFsm = _CfprSwExtUtilityFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 5),
    _CfprSwExtUtilityFsmCurrentFsm_Type()
)
cfprSwExtUtilityFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmCurrentFsm.setStatus("current")
_CfprSwExtUtilityFsmDescrData_Type = SnmpAdminString
_CfprSwExtUtilityFsmDescrData_Object = MibTableColumn
cfprSwExtUtilityFsmDescrData = _CfprSwExtUtilityFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 6),
    _CfprSwExtUtilityFsmDescrData_Type()
)
cfprSwExtUtilityFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmDescrData.setStatus("current")
_CfprSwExtUtilityFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwExtUtilityFsmFsmStatus_Object = MibTableColumn
cfprSwExtUtilityFsmFsmStatus = _CfprSwExtUtilityFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 7),
    _CfprSwExtUtilityFsmFsmStatus_Type()
)
cfprSwExtUtilityFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmFsmStatus.setStatus("current")
_CfprSwExtUtilityFsmProgress_Type = Gauge32
_CfprSwExtUtilityFsmProgress_Object = MibTableColumn
cfprSwExtUtilityFsmProgress = _CfprSwExtUtilityFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 8),
    _CfprSwExtUtilityFsmProgress_Type()
)
cfprSwExtUtilityFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmProgress.setStatus("current")
_CfprSwExtUtilityFsmRmtErrCode_Type = Gauge32
_CfprSwExtUtilityFsmRmtErrCode_Object = MibTableColumn
cfprSwExtUtilityFsmRmtErrCode = _CfprSwExtUtilityFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 9),
    _CfprSwExtUtilityFsmRmtErrCode_Type()
)
cfprSwExtUtilityFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmRmtErrCode.setStatus("current")
_CfprSwExtUtilityFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwExtUtilityFsmRmtErrDescr_Object = MibTableColumn
cfprSwExtUtilityFsmRmtErrDescr = _CfprSwExtUtilityFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 10),
    _CfprSwExtUtilityFsmRmtErrDescr_Type()
)
cfprSwExtUtilityFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmRmtErrDescr.setStatus("current")
_CfprSwExtUtilityFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwExtUtilityFsmRmtRslt_Object = MibTableColumn
cfprSwExtUtilityFsmRmtRslt = _CfprSwExtUtilityFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 32, 1, 11),
    _CfprSwExtUtilityFsmRmtRslt_Type()
)
cfprSwExtUtilityFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmRmtRslt.setStatus("current")
_CfprSwExtUtilityFsmStageTable_Object = MibTable
cfprSwExtUtilityFsmStageTable = _CfprSwExtUtilityFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33)
)
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageTable.setStatus("current")
_CfprSwExtUtilityFsmStageEntry_Object = MibTableRow
cfprSwExtUtilityFsmStageEntry = _CfprSwExtUtilityFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1)
)
cfprSwExtUtilityFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwExtUtilityFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageEntry.setStatus("current")
_CfprSwExtUtilityFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwExtUtilityFsmStageInstanceId_Object = MibTableColumn
cfprSwExtUtilityFsmStageInstanceId = _CfprSwExtUtilityFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 1),
    _CfprSwExtUtilityFsmStageInstanceId_Type()
)
cfprSwExtUtilityFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageInstanceId.setStatus("current")
_CfprSwExtUtilityFsmStageDn_Type = CfprManagedObjectDn
_CfprSwExtUtilityFsmStageDn_Object = MibTableColumn
cfprSwExtUtilityFsmStageDn = _CfprSwExtUtilityFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 2),
    _CfprSwExtUtilityFsmStageDn_Type()
)
cfprSwExtUtilityFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageDn.setStatus("current")
_CfprSwExtUtilityFsmStageRn_Type = SnmpAdminString
_CfprSwExtUtilityFsmStageRn_Object = MibTableColumn
cfprSwExtUtilityFsmStageRn = _CfprSwExtUtilityFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 3),
    _CfprSwExtUtilityFsmStageRn_Type()
)
cfprSwExtUtilityFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageRn.setStatus("current")
_CfprSwExtUtilityFsmStageDescrData_Type = SnmpAdminString
_CfprSwExtUtilityFsmStageDescrData_Object = MibTableColumn
cfprSwExtUtilityFsmStageDescrData = _CfprSwExtUtilityFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 4),
    _CfprSwExtUtilityFsmStageDescrData_Type()
)
cfprSwExtUtilityFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageDescrData.setStatus("current")
_CfprSwExtUtilityFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwExtUtilityFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwExtUtilityFsmStageLastUpdateTime = _CfprSwExtUtilityFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 5),
    _CfprSwExtUtilityFsmStageLastUpdateTime_Type()
)
cfprSwExtUtilityFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageLastUpdateTime.setStatus("current")
_CfprSwExtUtilityFsmStageName_Type = CfprSwExtUtilityFsmStageName
_CfprSwExtUtilityFsmStageName_Object = MibTableColumn
cfprSwExtUtilityFsmStageName = _CfprSwExtUtilityFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 6),
    _CfprSwExtUtilityFsmStageName_Type()
)
cfprSwExtUtilityFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageName.setStatus("current")
_CfprSwExtUtilityFsmStageOrder_Type = Gauge32
_CfprSwExtUtilityFsmStageOrder_Object = MibTableColumn
cfprSwExtUtilityFsmStageOrder = _CfprSwExtUtilityFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 7),
    _CfprSwExtUtilityFsmStageOrder_Type()
)
cfprSwExtUtilityFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageOrder.setStatus("current")
_CfprSwExtUtilityFsmStageRetry_Type = Gauge32
_CfprSwExtUtilityFsmStageRetry_Object = MibTableColumn
cfprSwExtUtilityFsmStageRetry = _CfprSwExtUtilityFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 8),
    _CfprSwExtUtilityFsmStageRetry_Type()
)
cfprSwExtUtilityFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageRetry.setStatus("current")
_CfprSwExtUtilityFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwExtUtilityFsmStageStageStatus_Object = MibTableColumn
cfprSwExtUtilityFsmStageStageStatus = _CfprSwExtUtilityFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 33, 1, 9),
    _CfprSwExtUtilityFsmStageStageStatus_Type()
)
cfprSwExtUtilityFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmStageStageStatus.setStatus("current")
_CfprSwExtUtilityFsmTaskTable_Object = MibTable
cfprSwExtUtilityFsmTaskTable = _CfprSwExtUtilityFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34)
)
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskTable.setStatus("current")
_CfprSwExtUtilityFsmTaskEntry_Object = MibTableRow
cfprSwExtUtilityFsmTaskEntry = _CfprSwExtUtilityFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34, 1)
)
cfprSwExtUtilityFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwExtUtilityFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskEntry.setStatus("current")
_CfprSwExtUtilityFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwExtUtilityFsmTaskInstanceId_Object = MibTableColumn
cfprSwExtUtilityFsmTaskInstanceId = _CfprSwExtUtilityFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34, 1, 1),
    _CfprSwExtUtilityFsmTaskInstanceId_Type()
)
cfprSwExtUtilityFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskInstanceId.setStatus("current")
_CfprSwExtUtilityFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwExtUtilityFsmTaskDn_Object = MibTableColumn
cfprSwExtUtilityFsmTaskDn = _CfprSwExtUtilityFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34, 1, 2),
    _CfprSwExtUtilityFsmTaskDn_Type()
)
cfprSwExtUtilityFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskDn.setStatus("current")
_CfprSwExtUtilityFsmTaskRn_Type = SnmpAdminString
_CfprSwExtUtilityFsmTaskRn_Object = MibTableColumn
cfprSwExtUtilityFsmTaskRn = _CfprSwExtUtilityFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34, 1, 3),
    _CfprSwExtUtilityFsmTaskRn_Type()
)
cfprSwExtUtilityFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskRn.setStatus("current")
_CfprSwExtUtilityFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwExtUtilityFsmTaskCompletion_Object = MibTableColumn
cfprSwExtUtilityFsmTaskCompletion = _CfprSwExtUtilityFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34, 1, 4),
    _CfprSwExtUtilityFsmTaskCompletion_Type()
)
cfprSwExtUtilityFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskCompletion.setStatus("current")
_CfprSwExtUtilityFsmTaskFlags_Type = CfprFsmFlags
_CfprSwExtUtilityFsmTaskFlags_Object = MibTableColumn
cfprSwExtUtilityFsmTaskFlags = _CfprSwExtUtilityFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34, 1, 5),
    _CfprSwExtUtilityFsmTaskFlags_Type()
)
cfprSwExtUtilityFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskFlags.setStatus("current")
_CfprSwExtUtilityFsmTaskItem_Type = CfprSwExtUtilityFsmTaskItem
_CfprSwExtUtilityFsmTaskItem_Object = MibTableColumn
cfprSwExtUtilityFsmTaskItem = _CfprSwExtUtilityFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34, 1, 6),
    _CfprSwExtUtilityFsmTaskItem_Type()
)
cfprSwExtUtilityFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskItem.setStatus("current")
_CfprSwExtUtilityFsmTaskSeqId_Type = Gauge32
_CfprSwExtUtilityFsmTaskSeqId_Object = MibTableColumn
cfprSwExtUtilityFsmTaskSeqId = _CfprSwExtUtilityFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 34, 1, 7),
    _CfprSwExtUtilityFsmTaskSeqId_Type()
)
cfprSwExtUtilityFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwExtUtilityFsmTaskSeqId.setStatus("current")
_CfprSwFabricZoneNsTable_Object = MibTable
cfprSwFabricZoneNsTable = _CfprSwFabricZoneNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35)
)
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsTable.setStatus("current")
_CfprSwFabricZoneNsEntry_Object = MibTableRow
cfprSwFabricZoneNsEntry = _CfprSwFabricZoneNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35, 1)
)
cfprSwFabricZoneNsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFabricZoneNsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsEntry.setStatus("current")
_CfprSwFabricZoneNsInstanceId_Type = CfprManagedObjectId
_CfprSwFabricZoneNsInstanceId_Object = MibTableColumn
cfprSwFabricZoneNsInstanceId = _CfprSwFabricZoneNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35, 1, 1),
    _CfprSwFabricZoneNsInstanceId_Type()
)
cfprSwFabricZoneNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsInstanceId.setStatus("current")
_CfprSwFabricZoneNsDn_Type = CfprManagedObjectDn
_CfprSwFabricZoneNsDn_Object = MibTableColumn
cfprSwFabricZoneNsDn = _CfprSwFabricZoneNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35, 1, 2),
    _CfprSwFabricZoneNsDn_Type()
)
cfprSwFabricZoneNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsDn.setStatus("current")
_CfprSwFabricZoneNsRn_Type = SnmpAdminString
_CfprSwFabricZoneNsRn_Object = MibTableColumn
cfprSwFabricZoneNsRn = _CfprSwFabricZoneNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35, 1, 3),
    _CfprSwFabricZoneNsRn_Type()
)
cfprSwFabricZoneNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsRn.setStatus("current")
_CfprSwFabricZoneNsAllocStatus_Type = CfprSwFabricZoneNsAllocStatus
_CfprSwFabricZoneNsAllocStatus_Object = MibTableColumn
cfprSwFabricZoneNsAllocStatus = _CfprSwFabricZoneNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35, 1, 4),
    _CfprSwFabricZoneNsAllocStatus_Type()
)
cfprSwFabricZoneNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsAllocStatus.setStatus("current")
_CfprSwFabricZoneNsLimit_Type = Gauge32
_CfprSwFabricZoneNsLimit_Object = MibTableColumn
cfprSwFabricZoneNsLimit = _CfprSwFabricZoneNsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35, 1, 5),
    _CfprSwFabricZoneNsLimit_Type()
)
cfprSwFabricZoneNsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsLimit.setStatus("current")
_CfprSwFabricZoneNsSwitchId_Type = CfprNetworkSwitchId
_CfprSwFabricZoneNsSwitchId_Object = MibTableColumn
cfprSwFabricZoneNsSwitchId = _CfprSwFabricZoneNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35, 1, 6),
    _CfprSwFabricZoneNsSwitchId_Type()
)
cfprSwFabricZoneNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsSwitchId.setStatus("current")
_CfprSwFabricZoneNsZoneCount_Type = Gauge32
_CfprSwFabricZoneNsZoneCount_Object = MibTableColumn
cfprSwFabricZoneNsZoneCount = _CfprSwFabricZoneNsZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 35, 1, 7),
    _CfprSwFabricZoneNsZoneCount_Type()
)
cfprSwFabricZoneNsZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsZoneCount.setStatus("current")
_CfprSwFabricZoneNsOverrideTable_Object = MibTable
cfprSwFabricZoneNsOverrideTable = _CfprSwFabricZoneNsOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 36)
)
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsOverrideTable.setStatus("current")
_CfprSwFabricZoneNsOverrideEntry_Object = MibTableRow
cfprSwFabricZoneNsOverrideEntry = _CfprSwFabricZoneNsOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 36, 1)
)
cfprSwFabricZoneNsOverrideEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFabricZoneNsOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsOverrideEntry.setStatus("current")
_CfprSwFabricZoneNsOverrideInstanceId_Type = CfprManagedObjectId
_CfprSwFabricZoneNsOverrideInstanceId_Object = MibTableColumn
cfprSwFabricZoneNsOverrideInstanceId = _CfprSwFabricZoneNsOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 36, 1, 1),
    _CfprSwFabricZoneNsOverrideInstanceId_Type()
)
cfprSwFabricZoneNsOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsOverrideInstanceId.setStatus("current")
_CfprSwFabricZoneNsOverrideDn_Type = CfprManagedObjectDn
_CfprSwFabricZoneNsOverrideDn_Object = MibTableColumn
cfprSwFabricZoneNsOverrideDn = _CfprSwFabricZoneNsOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 36, 1, 2),
    _CfprSwFabricZoneNsOverrideDn_Type()
)
cfprSwFabricZoneNsOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsOverrideDn.setStatus("current")
_CfprSwFabricZoneNsOverrideRn_Type = SnmpAdminString
_CfprSwFabricZoneNsOverrideRn_Object = MibTableColumn
cfprSwFabricZoneNsOverrideRn = _CfprSwFabricZoneNsOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 36, 1, 3),
    _CfprSwFabricZoneNsOverrideRn_Type()
)
cfprSwFabricZoneNsOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsOverrideRn.setStatus("current")
_CfprSwFabricZoneNsOverrideLimit_Type = Gauge32
_CfprSwFabricZoneNsOverrideLimit_Object = MibTableColumn
cfprSwFabricZoneNsOverrideLimit = _CfprSwFabricZoneNsOverrideLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 36, 1, 4),
    _CfprSwFabricZoneNsOverrideLimit_Type()
)
cfprSwFabricZoneNsOverrideLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFabricZoneNsOverrideLimit.setStatus("current")
_CfprSwFcSanBorderTable_Object = MibTable
cfprSwFcSanBorderTable = _CfprSwFcSanBorderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44)
)
if mibBuilder.loadTexts:
    cfprSwFcSanBorderTable.setStatus("current")
_CfprSwFcSanBorderEntry_Object = MibTableRow
cfprSwFcSanBorderEntry = _CfprSwFcSanBorderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1)
)
cfprSwFcSanBorderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcSanBorderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcSanBorderEntry.setStatus("current")
_CfprSwFcSanBorderInstanceId_Type = CfprManagedObjectId
_CfprSwFcSanBorderInstanceId_Object = MibTableColumn
cfprSwFcSanBorderInstanceId = _CfprSwFcSanBorderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 1),
    _CfprSwFcSanBorderInstanceId_Type()
)
cfprSwFcSanBorderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderInstanceId.setStatus("current")
_CfprSwFcSanBorderDn_Type = CfprManagedObjectDn
_CfprSwFcSanBorderDn_Object = MibTableColumn
cfprSwFcSanBorderDn = _CfprSwFcSanBorderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 2),
    _CfprSwFcSanBorderDn_Type()
)
cfprSwFcSanBorderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderDn.setStatus("current")
_CfprSwFcSanBorderRn_Type = SnmpAdminString
_CfprSwFcSanBorderRn_Object = MibTableColumn
cfprSwFcSanBorderRn = _CfprSwFcSanBorderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 3),
    _CfprSwFcSanBorderRn_Type()
)
cfprSwFcSanBorderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderRn.setStatus("current")
_CfprSwFcSanBorderFsmDescr_Type = SnmpAdminString
_CfprSwFcSanBorderFsmDescr_Object = MibTableColumn
cfprSwFcSanBorderFsmDescr = _CfprSwFcSanBorderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 4),
    _CfprSwFcSanBorderFsmDescr_Type()
)
cfprSwFcSanBorderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmDescr.setStatus("current")
_CfprSwFcSanBorderFsmPrev_Type = SnmpAdminString
_CfprSwFcSanBorderFsmPrev_Object = MibTableColumn
cfprSwFcSanBorderFsmPrev = _CfprSwFcSanBorderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 5),
    _CfprSwFcSanBorderFsmPrev_Type()
)
cfprSwFcSanBorderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmPrev.setStatus("current")
_CfprSwFcSanBorderFsmProgr_Type = Gauge32
_CfprSwFcSanBorderFsmProgr_Object = MibTableColumn
cfprSwFcSanBorderFsmProgr = _CfprSwFcSanBorderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 6),
    _CfprSwFcSanBorderFsmProgr_Type()
)
cfprSwFcSanBorderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmProgr.setStatus("current")
_CfprSwFcSanBorderFsmRmtInvErrCode_Type = Gauge32
_CfprSwFcSanBorderFsmRmtInvErrCode_Object = MibTableColumn
cfprSwFcSanBorderFsmRmtInvErrCode = _CfprSwFcSanBorderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 7),
    _CfprSwFcSanBorderFsmRmtInvErrCode_Type()
)
cfprSwFcSanBorderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmRmtInvErrCode.setStatus("current")
_CfprSwFcSanBorderFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwFcSanBorderFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwFcSanBorderFsmRmtInvErrDescr = _CfprSwFcSanBorderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 8),
    _CfprSwFcSanBorderFsmRmtInvErrDescr_Type()
)
cfprSwFcSanBorderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmRmtInvErrDescr.setStatus("current")
_CfprSwFcSanBorderFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwFcSanBorderFsmRmtInvRslt_Object = MibTableColumn
cfprSwFcSanBorderFsmRmtInvRslt = _CfprSwFcSanBorderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 9),
    _CfprSwFcSanBorderFsmRmtInvRslt_Type()
)
cfprSwFcSanBorderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmRmtInvRslt.setStatus("current")
_CfprSwFcSanBorderFsmStageDescr_Type = SnmpAdminString
_CfprSwFcSanBorderFsmStageDescr_Object = MibTableColumn
cfprSwFcSanBorderFsmStageDescr = _CfprSwFcSanBorderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 10),
    _CfprSwFcSanBorderFsmStageDescr_Type()
)
cfprSwFcSanBorderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageDescr.setStatus("current")
_CfprSwFcSanBorderFsmStamp_Type = DateAndTime
_CfprSwFcSanBorderFsmStamp_Object = MibTableColumn
cfprSwFcSanBorderFsmStamp = _CfprSwFcSanBorderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 11),
    _CfprSwFcSanBorderFsmStamp_Type()
)
cfprSwFcSanBorderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStamp.setStatus("current")
_CfprSwFcSanBorderFsmStatus_Type = SnmpAdminString
_CfprSwFcSanBorderFsmStatus_Object = MibTableColumn
cfprSwFcSanBorderFsmStatus = _CfprSwFcSanBorderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 12),
    _CfprSwFcSanBorderFsmStatus_Type()
)
cfprSwFcSanBorderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStatus.setStatus("current")
_CfprSwFcSanBorderFsmTry_Type = Gauge32
_CfprSwFcSanBorderFsmTry_Object = MibTableColumn
cfprSwFcSanBorderFsmTry = _CfprSwFcSanBorderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 13),
    _CfprSwFcSanBorderFsmTry_Type()
)
cfprSwFcSanBorderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTry.setStatus("current")
_CfprSwFcSanBorderLocale_Type = CfprSwBorderDomainLocale
_CfprSwFcSanBorderLocale_Object = MibTableColumn
cfprSwFcSanBorderLocale = _CfprSwFcSanBorderLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 14),
    _CfprSwFcSanBorderLocale_Type()
)
cfprSwFcSanBorderLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderLocale.setStatus("current")
_CfprSwFcSanBorderName_Type = SnmpAdminString
_CfprSwFcSanBorderName_Object = MibTableColumn
cfprSwFcSanBorderName = _CfprSwFcSanBorderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 15),
    _CfprSwFcSanBorderName_Type()
)
cfprSwFcSanBorderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderName.setStatus("current")
_CfprSwFcSanBorderSwitchId_Type = CfprNetworkSwitchId
_CfprSwFcSanBorderSwitchId_Object = MibTableColumn
cfprSwFcSanBorderSwitchId = _CfprSwFcSanBorderSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 16),
    _CfprSwFcSanBorderSwitchId_Type()
)
cfprSwFcSanBorderSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderSwitchId.setStatus("current")
_CfprSwFcSanBorderTransport_Type = CfprSwFcSanBorderTransport
_CfprSwFcSanBorderTransport_Object = MibTableColumn
cfprSwFcSanBorderTransport = _CfprSwFcSanBorderTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 17),
    _CfprSwFcSanBorderTransport_Type()
)
cfprSwFcSanBorderTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderTransport.setStatus("current")
_CfprSwFcSanBorderType_Type = CfprSwSanBorderType
_CfprSwFcSanBorderType_Object = MibTableColumn
cfprSwFcSanBorderType = _CfprSwFcSanBorderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 18),
    _CfprSwFcSanBorderType_Type()
)
cfprSwFcSanBorderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderType.setStatus("current")
_CfprSwFcSanBorderUplinkTrunking_Type = CfprSwFcSanBorderUplinkTrunking
_CfprSwFcSanBorderUplinkTrunking_Object = MibTableColumn
cfprSwFcSanBorderUplinkTrunking = _CfprSwFcSanBorderUplinkTrunking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 44, 1, 19),
    _CfprSwFcSanBorderUplinkTrunking_Type()
)
cfprSwFcSanBorderUplinkTrunking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderUplinkTrunking.setStatus("current")
_CfprSwFcSanBorderFsmTable_Object = MibTable
cfprSwFcSanBorderFsmTable = _CfprSwFcSanBorderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45)
)
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTable.setStatus("current")
_CfprSwFcSanBorderFsmEntry_Object = MibTableRow
cfprSwFcSanBorderFsmEntry = _CfprSwFcSanBorderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1)
)
cfprSwFcSanBorderFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcSanBorderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmEntry.setStatus("current")
_CfprSwFcSanBorderFsmInstanceId_Type = CfprManagedObjectId
_CfprSwFcSanBorderFsmInstanceId_Object = MibTableColumn
cfprSwFcSanBorderFsmInstanceId = _CfprSwFcSanBorderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 1),
    _CfprSwFcSanBorderFsmInstanceId_Type()
)
cfprSwFcSanBorderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmInstanceId.setStatus("current")
_CfprSwFcSanBorderFsmDn_Type = CfprManagedObjectDn
_CfprSwFcSanBorderFsmDn_Object = MibTableColumn
cfprSwFcSanBorderFsmDn = _CfprSwFcSanBorderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 2),
    _CfprSwFcSanBorderFsmDn_Type()
)
cfprSwFcSanBorderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmDn.setStatus("current")
_CfprSwFcSanBorderFsmRn_Type = SnmpAdminString
_CfprSwFcSanBorderFsmRn_Object = MibTableColumn
cfprSwFcSanBorderFsmRn = _CfprSwFcSanBorderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 3),
    _CfprSwFcSanBorderFsmRn_Type()
)
cfprSwFcSanBorderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmRn.setStatus("current")
_CfprSwFcSanBorderFsmCompletionTime_Type = DateAndTime
_CfprSwFcSanBorderFsmCompletionTime_Object = MibTableColumn
cfprSwFcSanBorderFsmCompletionTime = _CfprSwFcSanBorderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 4),
    _CfprSwFcSanBorderFsmCompletionTime_Type()
)
cfprSwFcSanBorderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmCompletionTime.setStatus("current")
_CfprSwFcSanBorderFsmCurrentFsm_Type = CfprSwFcSanBorderFsmCurrentFsm
_CfprSwFcSanBorderFsmCurrentFsm_Object = MibTableColumn
cfprSwFcSanBorderFsmCurrentFsm = _CfprSwFcSanBorderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 5),
    _CfprSwFcSanBorderFsmCurrentFsm_Type()
)
cfprSwFcSanBorderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmCurrentFsm.setStatus("current")
_CfprSwFcSanBorderFsmDescrData_Type = SnmpAdminString
_CfprSwFcSanBorderFsmDescrData_Object = MibTableColumn
cfprSwFcSanBorderFsmDescrData = _CfprSwFcSanBorderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 6),
    _CfprSwFcSanBorderFsmDescrData_Type()
)
cfprSwFcSanBorderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmDescrData.setStatus("current")
_CfprSwFcSanBorderFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwFcSanBorderFsmFsmStatus_Object = MibTableColumn
cfprSwFcSanBorderFsmFsmStatus = _CfprSwFcSanBorderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 7),
    _CfprSwFcSanBorderFsmFsmStatus_Type()
)
cfprSwFcSanBorderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmFsmStatus.setStatus("current")
_CfprSwFcSanBorderFsmProgress_Type = Gauge32
_CfprSwFcSanBorderFsmProgress_Object = MibTableColumn
cfprSwFcSanBorderFsmProgress = _CfprSwFcSanBorderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 8),
    _CfprSwFcSanBorderFsmProgress_Type()
)
cfprSwFcSanBorderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmProgress.setStatus("current")
_CfprSwFcSanBorderFsmRmtErrCode_Type = Gauge32
_CfprSwFcSanBorderFsmRmtErrCode_Object = MibTableColumn
cfprSwFcSanBorderFsmRmtErrCode = _CfprSwFcSanBorderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 9),
    _CfprSwFcSanBorderFsmRmtErrCode_Type()
)
cfprSwFcSanBorderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmRmtErrCode.setStatus("current")
_CfprSwFcSanBorderFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwFcSanBorderFsmRmtErrDescr_Object = MibTableColumn
cfprSwFcSanBorderFsmRmtErrDescr = _CfprSwFcSanBorderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 10),
    _CfprSwFcSanBorderFsmRmtErrDescr_Type()
)
cfprSwFcSanBorderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmRmtErrDescr.setStatus("current")
_CfprSwFcSanBorderFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwFcSanBorderFsmRmtRslt_Object = MibTableColumn
cfprSwFcSanBorderFsmRmtRslt = _CfprSwFcSanBorderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 45, 1, 11),
    _CfprSwFcSanBorderFsmRmtRslt_Type()
)
cfprSwFcSanBorderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmRmtRslt.setStatus("current")
_CfprSwFcSanBorderFsmStageTable_Object = MibTable
cfprSwFcSanBorderFsmStageTable = _CfprSwFcSanBorderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46)
)
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageTable.setStatus("current")
_CfprSwFcSanBorderFsmStageEntry_Object = MibTableRow
cfprSwFcSanBorderFsmStageEntry = _CfprSwFcSanBorderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1)
)
cfprSwFcSanBorderFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcSanBorderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageEntry.setStatus("current")
_CfprSwFcSanBorderFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwFcSanBorderFsmStageInstanceId_Object = MibTableColumn
cfprSwFcSanBorderFsmStageInstanceId = _CfprSwFcSanBorderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 1),
    _CfprSwFcSanBorderFsmStageInstanceId_Type()
)
cfprSwFcSanBorderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageInstanceId.setStatus("current")
_CfprSwFcSanBorderFsmStageDn_Type = CfprManagedObjectDn
_CfprSwFcSanBorderFsmStageDn_Object = MibTableColumn
cfprSwFcSanBorderFsmStageDn = _CfprSwFcSanBorderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 2),
    _CfprSwFcSanBorderFsmStageDn_Type()
)
cfprSwFcSanBorderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageDn.setStatus("current")
_CfprSwFcSanBorderFsmStageRn_Type = SnmpAdminString
_CfprSwFcSanBorderFsmStageRn_Object = MibTableColumn
cfprSwFcSanBorderFsmStageRn = _CfprSwFcSanBorderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 3),
    _CfprSwFcSanBorderFsmStageRn_Type()
)
cfprSwFcSanBorderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageRn.setStatus("current")
_CfprSwFcSanBorderFsmStageDescrData_Type = SnmpAdminString
_CfprSwFcSanBorderFsmStageDescrData_Object = MibTableColumn
cfprSwFcSanBorderFsmStageDescrData = _CfprSwFcSanBorderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 4),
    _CfprSwFcSanBorderFsmStageDescrData_Type()
)
cfprSwFcSanBorderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageDescrData.setStatus("current")
_CfprSwFcSanBorderFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwFcSanBorderFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwFcSanBorderFsmStageLastUpdateTime = _CfprSwFcSanBorderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 5),
    _CfprSwFcSanBorderFsmStageLastUpdateTime_Type()
)
cfprSwFcSanBorderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageLastUpdateTime.setStatus("current")
_CfprSwFcSanBorderFsmStageName_Type = CfprSwFcSanBorderFsmStageName
_CfprSwFcSanBorderFsmStageName_Object = MibTableColumn
cfprSwFcSanBorderFsmStageName = _CfprSwFcSanBorderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 6),
    _CfprSwFcSanBorderFsmStageName_Type()
)
cfprSwFcSanBorderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageName.setStatus("current")
_CfprSwFcSanBorderFsmStageOrder_Type = Gauge32
_CfprSwFcSanBorderFsmStageOrder_Object = MibTableColumn
cfprSwFcSanBorderFsmStageOrder = _CfprSwFcSanBorderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 7),
    _CfprSwFcSanBorderFsmStageOrder_Type()
)
cfprSwFcSanBorderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageOrder.setStatus("current")
_CfprSwFcSanBorderFsmStageRetry_Type = Gauge32
_CfprSwFcSanBorderFsmStageRetry_Object = MibTableColumn
cfprSwFcSanBorderFsmStageRetry = _CfprSwFcSanBorderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 8),
    _CfprSwFcSanBorderFsmStageRetry_Type()
)
cfprSwFcSanBorderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageRetry.setStatus("current")
_CfprSwFcSanBorderFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwFcSanBorderFsmStageStageStatus_Object = MibTableColumn
cfprSwFcSanBorderFsmStageStageStatus = _CfprSwFcSanBorderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 46, 1, 9),
    _CfprSwFcSanBorderFsmStageStageStatus_Type()
)
cfprSwFcSanBorderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmStageStageStatus.setStatus("current")
_CfprSwFcSanBorderFsmTaskTable_Object = MibTable
cfprSwFcSanBorderFsmTaskTable = _CfprSwFcSanBorderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47)
)
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskTable.setStatus("current")
_CfprSwFcSanBorderFsmTaskEntry_Object = MibTableRow
cfprSwFcSanBorderFsmTaskEntry = _CfprSwFcSanBorderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47, 1)
)
cfprSwFcSanBorderFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcSanBorderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskEntry.setStatus("current")
_CfprSwFcSanBorderFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwFcSanBorderFsmTaskInstanceId_Object = MibTableColumn
cfprSwFcSanBorderFsmTaskInstanceId = _CfprSwFcSanBorderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47, 1, 1),
    _CfprSwFcSanBorderFsmTaskInstanceId_Type()
)
cfprSwFcSanBorderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskInstanceId.setStatus("current")
_CfprSwFcSanBorderFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwFcSanBorderFsmTaskDn_Object = MibTableColumn
cfprSwFcSanBorderFsmTaskDn = _CfprSwFcSanBorderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47, 1, 2),
    _CfprSwFcSanBorderFsmTaskDn_Type()
)
cfprSwFcSanBorderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskDn.setStatus("current")
_CfprSwFcSanBorderFsmTaskRn_Type = SnmpAdminString
_CfprSwFcSanBorderFsmTaskRn_Object = MibTableColumn
cfprSwFcSanBorderFsmTaskRn = _CfprSwFcSanBorderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47, 1, 3),
    _CfprSwFcSanBorderFsmTaskRn_Type()
)
cfprSwFcSanBorderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskRn.setStatus("current")
_CfprSwFcSanBorderFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwFcSanBorderFsmTaskCompletion_Object = MibTableColumn
cfprSwFcSanBorderFsmTaskCompletion = _CfprSwFcSanBorderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47, 1, 4),
    _CfprSwFcSanBorderFsmTaskCompletion_Type()
)
cfprSwFcSanBorderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskCompletion.setStatus("current")
_CfprSwFcSanBorderFsmTaskFlags_Type = CfprFsmFlags
_CfprSwFcSanBorderFsmTaskFlags_Object = MibTableColumn
cfprSwFcSanBorderFsmTaskFlags = _CfprSwFcSanBorderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47, 1, 5),
    _CfprSwFcSanBorderFsmTaskFlags_Type()
)
cfprSwFcSanBorderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskFlags.setStatus("current")
_CfprSwFcSanBorderFsmTaskItem_Type = CfprSwFcSanBorderFsmTaskItem
_CfprSwFcSanBorderFsmTaskItem_Object = MibTableColumn
cfprSwFcSanBorderFsmTaskItem = _CfprSwFcSanBorderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47, 1, 6),
    _CfprSwFcSanBorderFsmTaskItem_Type()
)
cfprSwFcSanBorderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskItem.setStatus("current")
_CfprSwFcSanBorderFsmTaskSeqId_Type = Gauge32
_CfprSwFcSanBorderFsmTaskSeqId_Object = MibTableColumn
cfprSwFcSanBorderFsmTaskSeqId = _CfprSwFcSanBorderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 47, 1, 7),
    _CfprSwFcSanBorderFsmTaskSeqId_Type()
)
cfprSwFcSanBorderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanBorderFsmTaskSeqId.setStatus("current")
_CfprSwFcSanEpTable_Object = MibTable
cfprSwFcSanEpTable = _CfprSwFcSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48)
)
if mibBuilder.loadTexts:
    cfprSwFcSanEpTable.setStatus("current")
_CfprSwFcSanEpEntry_Object = MibTableRow
cfprSwFcSanEpEntry = _CfprSwFcSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1)
)
cfprSwFcSanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcSanEpEntry.setStatus("current")
_CfprSwFcSanEpInstanceId_Type = CfprManagedObjectId
_CfprSwFcSanEpInstanceId_Object = MibTableColumn
cfprSwFcSanEpInstanceId = _CfprSwFcSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 1),
    _CfprSwFcSanEpInstanceId_Type()
)
cfprSwFcSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcSanEpInstanceId.setStatus("current")
_CfprSwFcSanEpDn_Type = CfprManagedObjectDn
_CfprSwFcSanEpDn_Object = MibTableColumn
cfprSwFcSanEpDn = _CfprSwFcSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 2),
    _CfprSwFcSanEpDn_Type()
)
cfprSwFcSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpDn.setStatus("current")
_CfprSwFcSanEpRn_Type = SnmpAdminString
_CfprSwFcSanEpRn_Object = MibTableColumn
cfprSwFcSanEpRn = _CfprSwFcSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 3),
    _CfprSwFcSanEpRn_Type()
)
cfprSwFcSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpRn.setStatus("current")
_CfprSwFcSanEpAdminSpeed_Type = CfprPortSpeed
_CfprSwFcSanEpAdminSpeed_Object = MibTableColumn
cfprSwFcSanEpAdminSpeed = _CfprSwFcSanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 4),
    _CfprSwFcSanEpAdminSpeed_Type()
)
cfprSwFcSanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpAdminSpeed.setStatus("current")
_CfprSwFcSanEpAdminState_Type = CfprFabricAdminState
_CfprSwFcSanEpAdminState_Object = MibTableColumn
cfprSwFcSanEpAdminState = _CfprSwFcSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 5),
    _CfprSwFcSanEpAdminState_Type()
)
cfprSwFcSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpAdminState.setStatus("current")
_CfprSwFcSanEpAggrPortId_Type = Gauge32
_CfprSwFcSanEpAggrPortId_Object = MibTableColumn
cfprSwFcSanEpAggrPortId = _CfprSwFcSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 6),
    _CfprSwFcSanEpAggrPortId_Type()
)
cfprSwFcSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpAggrPortId.setStatus("current")
_CfprSwFcSanEpChassisId_Type = Gauge32
_CfprSwFcSanEpChassisId_Object = MibTableColumn
cfprSwFcSanEpChassisId = _CfprSwFcSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 7),
    _CfprSwFcSanEpChassisId_Type()
)
cfprSwFcSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpChassisId.setStatus("current")
_CfprSwFcSanEpEpDn_Type = SnmpAdminString
_CfprSwFcSanEpEpDn_Object = MibTableColumn
cfprSwFcSanEpEpDn = _CfprSwFcSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 8),
    _CfprSwFcSanEpEpDn_Type()
)
cfprSwFcSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpEpDn.setStatus("current")
_CfprSwFcSanEpFillPattern_Type = CfprFabricFillPattern
_CfprSwFcSanEpFillPattern_Object = MibTableColumn
cfprSwFcSanEpFillPattern = _CfprSwFcSanEpFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 9),
    _CfprSwFcSanEpFillPattern_Type()
)
cfprSwFcSanEpFillPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpFillPattern.setStatus("current")
_CfprSwFcSanEpIfRole_Type = CfprSwSanEpIfRole
_CfprSwFcSanEpIfRole_Object = MibTableColumn
cfprSwFcSanEpIfRole = _CfprSwFcSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 10),
    _CfprSwFcSanEpIfRole_Type()
)
cfprSwFcSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpIfRole.setStatus("current")
_CfprSwFcSanEpIfType_Type = CfprSwPIoEpIfType
_CfprSwFcSanEpIfType_Object = MibTableColumn
cfprSwFcSanEpIfType = _CfprSwFcSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 11),
    _CfprSwFcSanEpIfType_Type()
)
cfprSwFcSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpIfType.setStatus("current")
_CfprSwFcSanEpLc_Type = CfprSwPIoEpLc
_CfprSwFcSanEpLc_Object = MibTableColumn
cfprSwFcSanEpLc = _CfprSwFcSanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 12),
    _CfprSwFcSanEpLc_Type()
)
cfprSwFcSanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpLc.setStatus("current")
_CfprSwFcSanEpLocale_Type = CfprSwBorderEpLocale
_CfprSwFcSanEpLocale_Object = MibTableColumn
cfprSwFcSanEpLocale = _CfprSwFcSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 13),
    _CfprSwFcSanEpLocale_Type()
)
cfprSwFcSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpLocale.setStatus("current")
_CfprSwFcSanEpName_Type = SnmpAdminString
_CfprSwFcSanEpName_Object = MibTableColumn
cfprSwFcSanEpName = _CfprSwFcSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 14),
    _CfprSwFcSanEpName_Type()
)
cfprSwFcSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpName.setStatus("current")
_CfprSwFcSanEpPcId_Type = Gauge32
_CfprSwFcSanEpPcId_Object = MibTableColumn
cfprSwFcSanEpPcId = _CfprSwFcSanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 15),
    _CfprSwFcSanEpPcId_Type()
)
cfprSwFcSanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpPcId.setStatus("current")
_CfprSwFcSanEpPeerAggrPortId_Type = Gauge32
_CfprSwFcSanEpPeerAggrPortId_Object = MibTableColumn
cfprSwFcSanEpPeerAggrPortId = _CfprSwFcSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 16),
    _CfprSwFcSanEpPeerAggrPortId_Type()
)
cfprSwFcSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpPeerAggrPortId.setStatus("current")
_CfprSwFcSanEpPeerChassisId_Type = Gauge32
_CfprSwFcSanEpPeerChassisId_Object = MibTableColumn
cfprSwFcSanEpPeerChassisId = _CfprSwFcSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 17),
    _CfprSwFcSanEpPeerChassisId_Type()
)
cfprSwFcSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpPeerChassisId.setStatus("current")
_CfprSwFcSanEpPeerDn_Type = SnmpAdminString
_CfprSwFcSanEpPeerDn_Object = MibTableColumn
cfprSwFcSanEpPeerDn = _CfprSwFcSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 18),
    _CfprSwFcSanEpPeerDn_Type()
)
cfprSwFcSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpPeerDn.setStatus("current")
_CfprSwFcSanEpPeerPortId_Type = Gauge32
_CfprSwFcSanEpPeerPortId_Object = MibTableColumn
cfprSwFcSanEpPeerPortId = _CfprSwFcSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 19),
    _CfprSwFcSanEpPeerPortId_Type()
)
cfprSwFcSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpPeerPortId.setStatus("current")
_CfprSwFcSanEpPeerSlotId_Type = Gauge32
_CfprSwFcSanEpPeerSlotId_Object = MibTableColumn
cfprSwFcSanEpPeerSlotId = _CfprSwFcSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 20),
    _CfprSwFcSanEpPeerSlotId_Type()
)
cfprSwFcSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpPeerSlotId.setStatus("current")
_CfprSwFcSanEpPortId_Type = Gauge32
_CfprSwFcSanEpPortId_Object = MibTableColumn
cfprSwFcSanEpPortId = _CfprSwFcSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 21),
    _CfprSwFcSanEpPortId_Type()
)
cfprSwFcSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpPortId.setStatus("current")
_CfprSwFcSanEpPortVsanId_Type = Gauge32
_CfprSwFcSanEpPortVsanId_Object = MibTableColumn
cfprSwFcSanEpPortVsanId = _CfprSwFcSanEpPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 22),
    _CfprSwFcSanEpPortVsanId_Type()
)
cfprSwFcSanEpPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpPortVsanId.setStatus("current")
_CfprSwFcSanEpSlotId_Type = Gauge32
_CfprSwFcSanEpSlotId_Object = MibTableColumn
cfprSwFcSanEpSlotId = _CfprSwFcSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 23),
    _CfprSwFcSanEpSlotId_Type()
)
cfprSwFcSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpSlotId.setStatus("current")
_CfprSwFcSanEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwFcSanEpSwitchId_Object = MibTableColumn
cfprSwFcSanEpSwitchId = _CfprSwFcSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 24),
    _CfprSwFcSanEpSwitchId_Type()
)
cfprSwFcSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpSwitchId.setStatus("current")
_CfprSwFcSanEpTransport_Type = CfprSwFcSanEpTransport
_CfprSwFcSanEpTransport_Object = MibTableColumn
cfprSwFcSanEpTransport = _CfprSwFcSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 25),
    _CfprSwFcSanEpTransport_Type()
)
cfprSwFcSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpTransport.setStatus("current")
_CfprSwFcSanEpType_Type = CfprSwSanEpType
_CfprSwFcSanEpType_Object = MibTableColumn
cfprSwFcSanEpType = _CfprSwFcSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 48, 1, 26),
    _CfprSwFcSanEpType_Type()
)
cfprSwFcSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanEpType.setStatus("current")
_CfprSwFcSanPcTable_Object = MibTable
cfprSwFcSanPcTable = _CfprSwFcSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50)
)
if mibBuilder.loadTexts:
    cfprSwFcSanPcTable.setStatus("current")
_CfprSwFcSanPcEntry_Object = MibTableRow
cfprSwFcSanPcEntry = _CfprSwFcSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1)
)
cfprSwFcSanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcSanPcEntry.setStatus("current")
_CfprSwFcSanPcInstanceId_Type = CfprManagedObjectId
_CfprSwFcSanPcInstanceId_Object = MibTableColumn
cfprSwFcSanPcInstanceId = _CfprSwFcSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 1),
    _CfprSwFcSanPcInstanceId_Type()
)
cfprSwFcSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcSanPcInstanceId.setStatus("current")
_CfprSwFcSanPcDn_Type = CfprManagedObjectDn
_CfprSwFcSanPcDn_Object = MibTableColumn
cfprSwFcSanPcDn = _CfprSwFcSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 2),
    _CfprSwFcSanPcDn_Type()
)
cfprSwFcSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcDn.setStatus("current")
_CfprSwFcSanPcRn_Type = SnmpAdminString
_CfprSwFcSanPcRn_Object = MibTableColumn
cfprSwFcSanPcRn = _CfprSwFcSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 3),
    _CfprSwFcSanPcRn_Type()
)
cfprSwFcSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcRn.setStatus("current")
_CfprSwFcSanPcAdminSpeed_Type = CfprPortSpeed
_CfprSwFcSanPcAdminSpeed_Object = MibTableColumn
cfprSwFcSanPcAdminSpeed = _CfprSwFcSanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 4),
    _CfprSwFcSanPcAdminSpeed_Type()
)
cfprSwFcSanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcAdminSpeed.setStatus("current")
_CfprSwFcSanPcAdminState_Type = CfprFabricAdminState
_CfprSwFcSanPcAdminState_Object = MibTableColumn
cfprSwFcSanPcAdminState = _CfprSwFcSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 5),
    _CfprSwFcSanPcAdminState_Type()
)
cfprSwFcSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcAdminState.setStatus("current")
_CfprSwFcSanPcEpDn_Type = SnmpAdminString
_CfprSwFcSanPcEpDn_Object = MibTableColumn
cfprSwFcSanPcEpDn = _CfprSwFcSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 6),
    _CfprSwFcSanPcEpDn_Type()
)
cfprSwFcSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcEpDn.setStatus("current")
_CfprSwFcSanPcIfRole_Type = CfprSwSanPcIfRole
_CfprSwFcSanPcIfRole_Object = MibTableColumn
cfprSwFcSanPcIfRole = _CfprSwFcSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 7),
    _CfprSwFcSanPcIfRole_Type()
)
cfprSwFcSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcIfRole.setStatus("current")
_CfprSwFcSanPcIfType_Type = CfprSwCIoEpIfType
_CfprSwFcSanPcIfType_Object = MibTableColumn
cfprSwFcSanPcIfType = _CfprSwFcSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 8),
    _CfprSwFcSanPcIfType_Type()
)
cfprSwFcSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcIfType.setStatus("current")
_CfprSwFcSanPcLocale_Type = CfprSwBorderPcLocale
_CfprSwFcSanPcLocale_Object = MibTableColumn
cfprSwFcSanPcLocale = _CfprSwFcSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 9),
    _CfprSwFcSanPcLocale_Type()
)
cfprSwFcSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcLocale.setStatus("current")
_CfprSwFcSanPcMonTrafDir_Type = CfprFabricTrafficDirection
_CfprSwFcSanPcMonTrafDir_Object = MibTableColumn
cfprSwFcSanPcMonTrafDir = _CfprSwFcSanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 10),
    _CfprSwFcSanPcMonTrafDir_Type()
)
cfprSwFcSanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcMonTrafDir.setStatus("current")
_CfprSwFcSanPcName_Type = SnmpAdminString
_CfprSwFcSanPcName_Object = MibTableColumn
cfprSwFcSanPcName = _CfprSwFcSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 11),
    _CfprSwFcSanPcName_Type()
)
cfprSwFcSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcName.setStatus("current")
_CfprSwFcSanPcPcId_Type = Gauge32
_CfprSwFcSanPcPcId_Object = MibTableColumn
cfprSwFcSanPcPcId = _CfprSwFcSanPcPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 12),
    _CfprSwFcSanPcPcId_Type()
)
cfprSwFcSanPcPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcPcId.setStatus("current")
_CfprSwFcSanPcPeerDn_Type = SnmpAdminString
_CfprSwFcSanPcPeerDn_Object = MibTableColumn
cfprSwFcSanPcPeerDn = _CfprSwFcSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 13),
    _CfprSwFcSanPcPeerDn_Type()
)
cfprSwFcSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcPeerDn.setStatus("current")
_CfprSwFcSanPcPortId_Type = Gauge32
_CfprSwFcSanPcPortId_Object = MibTableColumn
cfprSwFcSanPcPortId = _CfprSwFcSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 14),
    _CfprSwFcSanPcPortId_Type()
)
cfprSwFcSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcPortId.setStatus("current")
_CfprSwFcSanPcPortVsanId_Type = Gauge32
_CfprSwFcSanPcPortVsanId_Object = MibTableColumn
cfprSwFcSanPcPortVsanId = _CfprSwFcSanPcPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 15),
    _CfprSwFcSanPcPortVsanId_Type()
)
cfprSwFcSanPcPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcPortVsanId.setStatus("current")
_CfprSwFcSanPcSwitchId_Type = CfprNetworkSwitchId
_CfprSwFcSanPcSwitchId_Object = MibTableColumn
cfprSwFcSanPcSwitchId = _CfprSwFcSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 16),
    _CfprSwFcSanPcSwitchId_Type()
)
cfprSwFcSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcSwitchId.setStatus("current")
_CfprSwFcSanPcTransport_Type = CfprSwFcSanPcTransport
_CfprSwFcSanPcTransport_Object = MibTableColumn
cfprSwFcSanPcTransport = _CfprSwFcSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 17),
    _CfprSwFcSanPcTransport_Type()
)
cfprSwFcSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcTransport.setStatus("current")
_CfprSwFcSanPcType_Type = CfprSwSanPcType
_CfprSwFcSanPcType_Object = MibTableColumn
cfprSwFcSanPcType = _CfprSwFcSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 50, 1, 18),
    _CfprSwFcSanPcType_Type()
)
cfprSwFcSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcSanPcType.setStatus("current")
_CfprSwFcServerZoneGroupTable_Object = MibTable
cfprSwFcServerZoneGroupTable = _CfprSwFcServerZoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51)
)
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupTable.setStatus("current")
_CfprSwFcServerZoneGroupEntry_Object = MibTableRow
cfprSwFcServerZoneGroupEntry = _CfprSwFcServerZoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1)
)
cfprSwFcServerZoneGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcServerZoneGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupEntry.setStatus("current")
_CfprSwFcServerZoneGroupInstanceId_Type = CfprManagedObjectId
_CfprSwFcServerZoneGroupInstanceId_Object = MibTableColumn
cfprSwFcServerZoneGroupInstanceId = _CfprSwFcServerZoneGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 1),
    _CfprSwFcServerZoneGroupInstanceId_Type()
)
cfprSwFcServerZoneGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupInstanceId.setStatus("current")
_CfprSwFcServerZoneGroupDn_Type = CfprManagedObjectDn
_CfprSwFcServerZoneGroupDn_Object = MibTableColumn
cfprSwFcServerZoneGroupDn = _CfprSwFcServerZoneGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 2),
    _CfprSwFcServerZoneGroupDn_Type()
)
cfprSwFcServerZoneGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupDn.setStatus("current")
_CfprSwFcServerZoneGroupRn_Type = SnmpAdminString
_CfprSwFcServerZoneGroupRn_Object = MibTableColumn
cfprSwFcServerZoneGroupRn = _CfprSwFcServerZoneGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 3),
    _CfprSwFcServerZoneGroupRn_Type()
)
cfprSwFcServerZoneGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupRn.setStatus("current")
_CfprSwFcServerZoneGroupEpDn_Type = SnmpAdminString
_CfprSwFcServerZoneGroupEpDn_Object = MibTableColumn
cfprSwFcServerZoneGroupEpDn = _CfprSwFcServerZoneGroupEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 4),
    _CfprSwFcServerZoneGroupEpDn_Type()
)
cfprSwFcServerZoneGroupEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupEpDn.setStatus("current")
_CfprSwFcServerZoneGroupId_Type = Gauge32
_CfprSwFcServerZoneGroupId_Object = MibTableColumn
cfprSwFcServerZoneGroupId = _CfprSwFcServerZoneGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 5),
    _CfprSwFcServerZoneGroupId_Type()
)
cfprSwFcServerZoneGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupId.setStatus("current")
_CfprSwFcServerZoneGroupLc_Type = CfprSwFcServerZoneGroupLc
_CfprSwFcServerZoneGroupLc_Object = MibTableColumn
cfprSwFcServerZoneGroupLc = _CfprSwFcServerZoneGroupLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 6),
    _CfprSwFcServerZoneGroupLc_Type()
)
cfprSwFcServerZoneGroupLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupLc.setStatus("current")
_CfprSwFcServerZoneGroupName_Type = SnmpAdminString
_CfprSwFcServerZoneGroupName_Object = MibTableColumn
cfprSwFcServerZoneGroupName = _CfprSwFcServerZoneGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 7),
    _CfprSwFcServerZoneGroupName_Type()
)
cfprSwFcServerZoneGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupName.setStatus("current")
_CfprSwFcServerZoneGroupPeerDn_Type = SnmpAdminString
_CfprSwFcServerZoneGroupPeerDn_Object = MibTableColumn
cfprSwFcServerZoneGroupPeerDn = _CfprSwFcServerZoneGroupPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 8),
    _CfprSwFcServerZoneGroupPeerDn_Type()
)
cfprSwFcServerZoneGroupPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupPeerDn.setStatus("current")
_CfprSwFcServerZoneGroupServerDn_Type = SnmpAdminString
_CfprSwFcServerZoneGroupServerDn_Object = MibTableColumn
cfprSwFcServerZoneGroupServerDn = _CfprSwFcServerZoneGroupServerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 51, 1, 9),
    _CfprSwFcServerZoneGroupServerDn_Type()
)
cfprSwFcServerZoneGroupServerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcServerZoneGroupServerDn.setStatus("current")
_CfprSwFcZoneTable_Object = MibTable
cfprSwFcZoneTable = _CfprSwFcZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52)
)
if mibBuilder.loadTexts:
    cfprSwFcZoneTable.setStatus("current")
_CfprSwFcZoneEntry_Object = MibTableRow
cfprSwFcZoneEntry = _CfprSwFcZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1)
)
cfprSwFcZoneEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcZoneInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcZoneEntry.setStatus("current")
_CfprSwFcZoneInstanceId_Type = CfprManagedObjectId
_CfprSwFcZoneInstanceId_Object = MibTableColumn
cfprSwFcZoneInstanceId = _CfprSwFcZoneInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 1),
    _CfprSwFcZoneInstanceId_Type()
)
cfprSwFcZoneInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcZoneInstanceId.setStatus("current")
_CfprSwFcZoneDn_Type = CfprManagedObjectDn
_CfprSwFcZoneDn_Object = MibTableColumn
cfprSwFcZoneDn = _CfprSwFcZoneDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 2),
    _CfprSwFcZoneDn_Type()
)
cfprSwFcZoneDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneDn.setStatus("current")
_CfprSwFcZoneRn_Type = SnmpAdminString
_CfprSwFcZoneRn_Object = MibTableColumn
cfprSwFcZoneRn = _CfprSwFcZoneRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 3),
    _CfprSwFcZoneRn_Type()
)
cfprSwFcZoneRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneRn.setStatus("current")
_CfprSwFcZoneId_Type = Gauge32
_CfprSwFcZoneId_Object = MibTableColumn
cfprSwFcZoneId = _CfprSwFcZoneId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 4),
    _CfprSwFcZoneId_Type()
)
cfprSwFcZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneId.setStatus("current")
_CfprSwFcZoneIdentity_Type = SnmpAdminString
_CfprSwFcZoneIdentity_Object = MibTableColumn
cfprSwFcZoneIdentity = _CfprSwFcZoneIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 5),
    _CfprSwFcZoneIdentity_Type()
)
cfprSwFcZoneIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneIdentity.setStatus("current")
_CfprSwFcZoneLc_Type = CfprSwFcZoneLc
_CfprSwFcZoneLc_Object = MibTableColumn
cfprSwFcZoneLc = _CfprSwFcZoneLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 6),
    _CfprSwFcZoneLc_Type()
)
cfprSwFcZoneLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneLc.setStatus("current")
_CfprSwFcZoneName_Type = SnmpAdminString
_CfprSwFcZoneName_Object = MibTableColumn
cfprSwFcZoneName = _CfprSwFcZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 7),
    _CfprSwFcZoneName_Type()
)
cfprSwFcZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneName.setStatus("current")
_CfprSwFcZoneOperState_Type = CfprLsFcZoneState
_CfprSwFcZoneOperState_Object = MibTableColumn
cfprSwFcZoneOperState = _CfprSwFcZoneOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 8),
    _CfprSwFcZoneOperState_Type()
)
cfprSwFcZoneOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneOperState.setStatus("current")
_CfprSwFcZonePeerDn_Type = SnmpAdminString
_CfprSwFcZonePeerDn_Object = MibTableColumn
cfprSwFcZonePeerDn = _CfprSwFcZonePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 52, 1, 9),
    _CfprSwFcZonePeerDn_Type()
)
cfprSwFcZonePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZonePeerDn.setStatus("current")
_CfprSwFcZoneSetTable_Object = MibTable
cfprSwFcZoneSetTable = _CfprSwFcZoneSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53)
)
if mibBuilder.loadTexts:
    cfprSwFcZoneSetTable.setStatus("current")
_CfprSwFcZoneSetEntry_Object = MibTableRow
cfprSwFcZoneSetEntry = _CfprSwFcZoneSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53, 1)
)
cfprSwFcZoneSetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcZoneSetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcZoneSetEntry.setStatus("current")
_CfprSwFcZoneSetInstanceId_Type = CfprManagedObjectId
_CfprSwFcZoneSetInstanceId_Object = MibTableColumn
cfprSwFcZoneSetInstanceId = _CfprSwFcZoneSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53, 1, 1),
    _CfprSwFcZoneSetInstanceId_Type()
)
cfprSwFcZoneSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcZoneSetInstanceId.setStatus("current")
_CfprSwFcZoneSetDn_Type = CfprManagedObjectDn
_CfprSwFcZoneSetDn_Object = MibTableColumn
cfprSwFcZoneSetDn = _CfprSwFcZoneSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53, 1, 2),
    _CfprSwFcZoneSetDn_Type()
)
cfprSwFcZoneSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneSetDn.setStatus("current")
_CfprSwFcZoneSetRn_Type = SnmpAdminString
_CfprSwFcZoneSetRn_Object = MibTableColumn
cfprSwFcZoneSetRn = _CfprSwFcZoneSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53, 1, 3),
    _CfprSwFcZoneSetRn_Type()
)
cfprSwFcZoneSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneSetRn.setStatus("current")
_CfprSwFcZoneSetCurrentZonePrefix_Type = SnmpAdminString
_CfprSwFcZoneSetCurrentZonePrefix_Object = MibTableColumn
cfprSwFcZoneSetCurrentZonePrefix = _CfprSwFcZoneSetCurrentZonePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53, 1, 4),
    _CfprSwFcZoneSetCurrentZonePrefix_Type()
)
cfprSwFcZoneSetCurrentZonePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneSetCurrentZonePrefix.setStatus("current")
_CfprSwFcZoneSetLc_Type = CfprSwFcZoneSetLc
_CfprSwFcZoneSetLc_Object = MibTableColumn
cfprSwFcZoneSetLc = _CfprSwFcZoneSetLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53, 1, 5),
    _CfprSwFcZoneSetLc_Type()
)
cfprSwFcZoneSetLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneSetLc.setStatus("current")
_CfprSwFcZoneSetName_Type = SnmpAdminString
_CfprSwFcZoneSetName_Object = MibTableColumn
cfprSwFcZoneSetName = _CfprSwFcZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53, 1, 6),
    _CfprSwFcZoneSetName_Type()
)
cfprSwFcZoneSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneSetName.setStatus("current")
_CfprSwFcZoneSetOldZonePrefix_Type = SnmpAdminString
_CfprSwFcZoneSetOldZonePrefix_Object = MibTableColumn
cfprSwFcZoneSetOldZonePrefix = _CfprSwFcZoneSetOldZonePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 53, 1, 7),
    _CfprSwFcZoneSetOldZonePrefix_Type()
)
cfprSwFcZoneSetOldZonePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcZoneSetOldZonePrefix.setStatus("current")
_CfprSwFcoeSanEpTable_Object = MibTable
cfprSwFcoeSanEpTable = _CfprSwFcoeSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55)
)
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpTable.setStatus("current")
_CfprSwFcoeSanEpEntry_Object = MibTableRow
cfprSwFcoeSanEpEntry = _CfprSwFcoeSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1)
)
cfprSwFcoeSanEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcoeSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpEntry.setStatus("current")
_CfprSwFcoeSanEpInstanceId_Type = CfprManagedObjectId
_CfprSwFcoeSanEpInstanceId_Object = MibTableColumn
cfprSwFcoeSanEpInstanceId = _CfprSwFcoeSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 1),
    _CfprSwFcoeSanEpInstanceId_Type()
)
cfprSwFcoeSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpInstanceId.setStatus("current")
_CfprSwFcoeSanEpDn_Type = CfprManagedObjectDn
_CfprSwFcoeSanEpDn_Object = MibTableColumn
cfprSwFcoeSanEpDn = _CfprSwFcoeSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 2),
    _CfprSwFcoeSanEpDn_Type()
)
cfprSwFcoeSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpDn.setStatus("current")
_CfprSwFcoeSanEpRn_Type = SnmpAdminString
_CfprSwFcoeSanEpRn_Object = MibTableColumn
cfprSwFcoeSanEpRn = _CfprSwFcoeSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 3),
    _CfprSwFcoeSanEpRn_Type()
)
cfprSwFcoeSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpRn.setStatus("current")
_CfprSwFcoeSanEpAdminSpeed_Type = CfprPortSpeed
_CfprSwFcoeSanEpAdminSpeed_Object = MibTableColumn
cfprSwFcoeSanEpAdminSpeed = _CfprSwFcoeSanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 4),
    _CfprSwFcoeSanEpAdminSpeed_Type()
)
cfprSwFcoeSanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpAdminSpeed.setStatus("current")
_CfprSwFcoeSanEpAdminState_Type = CfprFabricAdminState
_CfprSwFcoeSanEpAdminState_Object = MibTableColumn
cfprSwFcoeSanEpAdminState = _CfprSwFcoeSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 5),
    _CfprSwFcoeSanEpAdminState_Type()
)
cfprSwFcoeSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpAdminState.setStatus("current")
_CfprSwFcoeSanEpAggrPortId_Type = Gauge32
_CfprSwFcoeSanEpAggrPortId_Object = MibTableColumn
cfprSwFcoeSanEpAggrPortId = _CfprSwFcoeSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 6),
    _CfprSwFcoeSanEpAggrPortId_Type()
)
cfprSwFcoeSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpAggrPortId.setStatus("current")
_CfprSwFcoeSanEpChassisId_Type = Gauge32
_CfprSwFcoeSanEpChassisId_Object = MibTableColumn
cfprSwFcoeSanEpChassisId = _CfprSwFcoeSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 7),
    _CfprSwFcoeSanEpChassisId_Type()
)
cfprSwFcoeSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpChassisId.setStatus("current")
_CfprSwFcoeSanEpEpDn_Type = SnmpAdminString
_CfprSwFcoeSanEpEpDn_Object = MibTableColumn
cfprSwFcoeSanEpEpDn = _CfprSwFcoeSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 8),
    _CfprSwFcoeSanEpEpDn_Type()
)
cfprSwFcoeSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpEpDn.setStatus("current")
_CfprSwFcoeSanEpIfRole_Type = CfprSwSanEpIfRole
_CfprSwFcoeSanEpIfRole_Object = MibTableColumn
cfprSwFcoeSanEpIfRole = _CfprSwFcoeSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 9),
    _CfprSwFcoeSanEpIfRole_Type()
)
cfprSwFcoeSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpIfRole.setStatus("current")
_CfprSwFcoeSanEpIfType_Type = CfprSwPIoEpIfType
_CfprSwFcoeSanEpIfType_Object = MibTableColumn
cfprSwFcoeSanEpIfType = _CfprSwFcoeSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 10),
    _CfprSwFcoeSanEpIfType_Type()
)
cfprSwFcoeSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpIfType.setStatus("current")
_CfprSwFcoeSanEpLc_Type = CfprSwPIoEpLc
_CfprSwFcoeSanEpLc_Object = MibTableColumn
cfprSwFcoeSanEpLc = _CfprSwFcoeSanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 11),
    _CfprSwFcoeSanEpLc_Type()
)
cfprSwFcoeSanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpLc.setStatus("current")
_CfprSwFcoeSanEpLocale_Type = CfprSwBorderEpLocale
_CfprSwFcoeSanEpLocale_Object = MibTableColumn
cfprSwFcoeSanEpLocale = _CfprSwFcoeSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 12),
    _CfprSwFcoeSanEpLocale_Type()
)
cfprSwFcoeSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpLocale.setStatus("current")
_CfprSwFcoeSanEpName_Type = SnmpAdminString
_CfprSwFcoeSanEpName_Object = MibTableColumn
cfprSwFcoeSanEpName = _CfprSwFcoeSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 13),
    _CfprSwFcoeSanEpName_Type()
)
cfprSwFcoeSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpName.setStatus("current")
_CfprSwFcoeSanEpPcId_Type = Gauge32
_CfprSwFcoeSanEpPcId_Object = MibTableColumn
cfprSwFcoeSanEpPcId = _CfprSwFcoeSanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 14),
    _CfprSwFcoeSanEpPcId_Type()
)
cfprSwFcoeSanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPcId.setStatus("current")
_CfprSwFcoeSanEpPeerAggrPortId_Type = Gauge32
_CfprSwFcoeSanEpPeerAggrPortId_Object = MibTableColumn
cfprSwFcoeSanEpPeerAggrPortId = _CfprSwFcoeSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 15),
    _CfprSwFcoeSanEpPeerAggrPortId_Type()
)
cfprSwFcoeSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPeerAggrPortId.setStatus("current")
_CfprSwFcoeSanEpPeerChassisId_Type = Gauge32
_CfprSwFcoeSanEpPeerChassisId_Object = MibTableColumn
cfprSwFcoeSanEpPeerChassisId = _CfprSwFcoeSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 16),
    _CfprSwFcoeSanEpPeerChassisId_Type()
)
cfprSwFcoeSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPeerChassisId.setStatus("current")
_CfprSwFcoeSanEpPeerDn_Type = SnmpAdminString
_CfprSwFcoeSanEpPeerDn_Object = MibTableColumn
cfprSwFcoeSanEpPeerDn = _CfprSwFcoeSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 17),
    _CfprSwFcoeSanEpPeerDn_Type()
)
cfprSwFcoeSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPeerDn.setStatus("current")
_CfprSwFcoeSanEpPeerPortId_Type = Gauge32
_CfprSwFcoeSanEpPeerPortId_Object = MibTableColumn
cfprSwFcoeSanEpPeerPortId = _CfprSwFcoeSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 18),
    _CfprSwFcoeSanEpPeerPortId_Type()
)
cfprSwFcoeSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPeerPortId.setStatus("current")
_CfprSwFcoeSanEpPeerSlotId_Type = Gauge32
_CfprSwFcoeSanEpPeerSlotId_Object = MibTableColumn
cfprSwFcoeSanEpPeerSlotId = _CfprSwFcoeSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 19),
    _CfprSwFcoeSanEpPeerSlotId_Type()
)
cfprSwFcoeSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPeerSlotId.setStatus("current")
_CfprSwFcoeSanEpPeerState_Type = CfprSwPeerStatus
_CfprSwFcoeSanEpPeerState_Object = MibTableColumn
cfprSwFcoeSanEpPeerState = _CfprSwFcoeSanEpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 20),
    _CfprSwFcoeSanEpPeerState_Type()
)
cfprSwFcoeSanEpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPeerState.setStatus("current")
_CfprSwFcoeSanEpPortId_Type = Gauge32
_CfprSwFcoeSanEpPortId_Object = MibTableColumn
cfprSwFcoeSanEpPortId = _CfprSwFcoeSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 21),
    _CfprSwFcoeSanEpPortId_Type()
)
cfprSwFcoeSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPortId.setStatus("current")
_CfprSwFcoeSanEpPortVsanId_Type = Gauge32
_CfprSwFcoeSanEpPortVsanId_Object = MibTableColumn
cfprSwFcoeSanEpPortVsanId = _CfprSwFcoeSanEpPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 22),
    _CfprSwFcoeSanEpPortVsanId_Type()
)
cfprSwFcoeSanEpPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpPortVsanId.setStatus("current")
_CfprSwFcoeSanEpSlotId_Type = Gauge32
_CfprSwFcoeSanEpSlotId_Object = MibTableColumn
cfprSwFcoeSanEpSlotId = _CfprSwFcoeSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 23),
    _CfprSwFcoeSanEpSlotId_Type()
)
cfprSwFcoeSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpSlotId.setStatus("current")
_CfprSwFcoeSanEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwFcoeSanEpSwitchId_Object = MibTableColumn
cfprSwFcoeSanEpSwitchId = _CfprSwFcoeSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 24),
    _CfprSwFcoeSanEpSwitchId_Type()
)
cfprSwFcoeSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpSwitchId.setStatus("current")
_CfprSwFcoeSanEpTransport_Type = CfprSwFcoeSanEpTransport
_CfprSwFcoeSanEpTransport_Object = MibTableColumn
cfprSwFcoeSanEpTransport = _CfprSwFcoeSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 25),
    _CfprSwFcoeSanEpTransport_Type()
)
cfprSwFcoeSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpTransport.setStatus("current")
_CfprSwFcoeSanEpType_Type = CfprSwSanEpType
_CfprSwFcoeSanEpType_Object = MibTableColumn
cfprSwFcoeSanEpType = _CfprSwFcoeSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 26),
    _CfprSwFcoeSanEpType_Type()
)
cfprSwFcoeSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpType.setStatus("current")
_CfprSwFcoeSanEpUdldAdminState_Type = CfprSwFcoeSanEpUdldAdminState
_CfprSwFcoeSanEpUdldAdminState_Object = MibTableColumn
cfprSwFcoeSanEpUdldAdminState = _CfprSwFcoeSanEpUdldAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 27),
    _CfprSwFcoeSanEpUdldAdminState_Type()
)
cfprSwFcoeSanEpUdldAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpUdldAdminState.setStatus("current")
_CfprSwFcoeSanEpUdldMode_Type = CfprSwFcoeSanEpUdldMode
_CfprSwFcoeSanEpUdldMode_Object = MibTableColumn
cfprSwFcoeSanEpUdldMode = _CfprSwFcoeSanEpUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 55, 1, 28),
    _CfprSwFcoeSanEpUdldMode_Type()
)
cfprSwFcoeSanEpUdldMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanEpUdldMode.setStatus("current")
_CfprSwFcoeSanPcTable_Object = MibTable
cfprSwFcoeSanPcTable = _CfprSwFcoeSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56)
)
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcTable.setStatus("current")
_CfprSwFcoeSanPcEntry_Object = MibTableRow
cfprSwFcoeSanPcEntry = _CfprSwFcoeSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1)
)
cfprSwFcoeSanPcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwFcoeSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcEntry.setStatus("current")
_CfprSwFcoeSanPcInstanceId_Type = CfprManagedObjectId
_CfprSwFcoeSanPcInstanceId_Object = MibTableColumn
cfprSwFcoeSanPcInstanceId = _CfprSwFcoeSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 1),
    _CfprSwFcoeSanPcInstanceId_Type()
)
cfprSwFcoeSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcInstanceId.setStatus("current")
_CfprSwFcoeSanPcDn_Type = CfprManagedObjectDn
_CfprSwFcoeSanPcDn_Object = MibTableColumn
cfprSwFcoeSanPcDn = _CfprSwFcoeSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 2),
    _CfprSwFcoeSanPcDn_Type()
)
cfprSwFcoeSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcDn.setStatus("current")
_CfprSwFcoeSanPcRn_Type = SnmpAdminString
_CfprSwFcoeSanPcRn_Object = MibTableColumn
cfprSwFcoeSanPcRn = _CfprSwFcoeSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 3),
    _CfprSwFcoeSanPcRn_Type()
)
cfprSwFcoeSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcRn.setStatus("current")
_CfprSwFcoeSanPcAdminState_Type = CfprFabricAdminState
_CfprSwFcoeSanPcAdminState_Object = MibTableColumn
cfprSwFcoeSanPcAdminState = _CfprSwFcoeSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 4),
    _CfprSwFcoeSanPcAdminState_Type()
)
cfprSwFcoeSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcAdminState.setStatus("current")
_CfprSwFcoeSanPcEpDn_Type = SnmpAdminString
_CfprSwFcoeSanPcEpDn_Object = MibTableColumn
cfprSwFcoeSanPcEpDn = _CfprSwFcoeSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 5),
    _CfprSwFcoeSanPcEpDn_Type()
)
cfprSwFcoeSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcEpDn.setStatus("current")
_CfprSwFcoeSanPcIfRole_Type = CfprSwSanPcIfRole
_CfprSwFcoeSanPcIfRole_Object = MibTableColumn
cfprSwFcoeSanPcIfRole = _CfprSwFcoeSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 6),
    _CfprSwFcoeSanPcIfRole_Type()
)
cfprSwFcoeSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcIfRole.setStatus("current")
_CfprSwFcoeSanPcIfType_Type = CfprSwCIoEpIfType
_CfprSwFcoeSanPcIfType_Object = MibTableColumn
cfprSwFcoeSanPcIfType = _CfprSwFcoeSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 7),
    _CfprSwFcoeSanPcIfType_Type()
)
cfprSwFcoeSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcIfType.setStatus("current")
_CfprSwFcoeSanPcLacpFastTimer_Type = TruthValue
_CfprSwFcoeSanPcLacpFastTimer_Object = MibTableColumn
cfprSwFcoeSanPcLacpFastTimer = _CfprSwFcoeSanPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 8),
    _CfprSwFcoeSanPcLacpFastTimer_Type()
)
cfprSwFcoeSanPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcLacpFastTimer.setStatus("current")
_CfprSwFcoeSanPcLacpSuspendIndividual_Type = TruthValue
_CfprSwFcoeSanPcLacpSuspendIndividual_Object = MibTableColumn
cfprSwFcoeSanPcLacpSuspendIndividual = _CfprSwFcoeSanPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 9),
    _CfprSwFcoeSanPcLacpSuspendIndividual_Type()
)
cfprSwFcoeSanPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcLacpSuspendIndividual.setStatus("current")
_CfprSwFcoeSanPcLocale_Type = CfprSwBorderPcLocale
_CfprSwFcoeSanPcLocale_Object = MibTableColumn
cfprSwFcoeSanPcLocale = _CfprSwFcoeSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 10),
    _CfprSwFcoeSanPcLocale_Type()
)
cfprSwFcoeSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcLocale.setStatus("current")
_CfprSwFcoeSanPcMonTrafDir_Type = CfprFabricTrafficDirection
_CfprSwFcoeSanPcMonTrafDir_Object = MibTableColumn
cfprSwFcoeSanPcMonTrafDir = _CfprSwFcoeSanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 11),
    _CfprSwFcoeSanPcMonTrafDir_Type()
)
cfprSwFcoeSanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcMonTrafDir.setStatus("current")
_CfprSwFcoeSanPcName_Type = SnmpAdminString
_CfprSwFcoeSanPcName_Object = MibTableColumn
cfprSwFcoeSanPcName = _CfprSwFcoeSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 12),
    _CfprSwFcoeSanPcName_Type()
)
cfprSwFcoeSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcName.setStatus("current")
_CfprSwFcoeSanPcPcId_Type = Gauge32
_CfprSwFcoeSanPcPcId_Object = MibTableColumn
cfprSwFcoeSanPcPcId = _CfprSwFcoeSanPcPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 13),
    _CfprSwFcoeSanPcPcId_Type()
)
cfprSwFcoeSanPcPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcPcId.setStatus("current")
_CfprSwFcoeSanPcPeerDn_Type = SnmpAdminString
_CfprSwFcoeSanPcPeerDn_Object = MibTableColumn
cfprSwFcoeSanPcPeerDn = _CfprSwFcoeSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 14),
    _CfprSwFcoeSanPcPeerDn_Type()
)
cfprSwFcoeSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcPeerDn.setStatus("current")
_CfprSwFcoeSanPcPeerState_Type = CfprSwPeerStatus
_CfprSwFcoeSanPcPeerState_Object = MibTableColumn
cfprSwFcoeSanPcPeerState = _CfprSwFcoeSanPcPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 15),
    _CfprSwFcoeSanPcPeerState_Type()
)
cfprSwFcoeSanPcPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcPeerState.setStatus("current")
_CfprSwFcoeSanPcPortId_Type = Gauge32
_CfprSwFcoeSanPcPortId_Object = MibTableColumn
cfprSwFcoeSanPcPortId = _CfprSwFcoeSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 16),
    _CfprSwFcoeSanPcPortId_Type()
)
cfprSwFcoeSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcPortId.setStatus("current")
_CfprSwFcoeSanPcPortVsanId_Type = Gauge32
_CfprSwFcoeSanPcPortVsanId_Object = MibTableColumn
cfprSwFcoeSanPcPortVsanId = _CfprSwFcoeSanPcPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 17),
    _CfprSwFcoeSanPcPortVsanId_Type()
)
cfprSwFcoeSanPcPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcPortVsanId.setStatus("current")
_CfprSwFcoeSanPcSwitchId_Type = CfprNetworkSwitchId
_CfprSwFcoeSanPcSwitchId_Object = MibTableColumn
cfprSwFcoeSanPcSwitchId = _CfprSwFcoeSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 18),
    _CfprSwFcoeSanPcSwitchId_Type()
)
cfprSwFcoeSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcSwitchId.setStatus("current")
_CfprSwFcoeSanPcTransport_Type = CfprSwFcoeSanPcTransport
_CfprSwFcoeSanPcTransport_Object = MibTableColumn
cfprSwFcoeSanPcTransport = _CfprSwFcoeSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 19),
    _CfprSwFcoeSanPcTransport_Type()
)
cfprSwFcoeSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcTransport.setStatus("current")
_CfprSwFcoeSanPcType_Type = CfprSwSanPcType
_CfprSwFcoeSanPcType_Object = MibTableColumn
cfprSwFcoeSanPcType = _CfprSwFcoeSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 56, 1, 20),
    _CfprSwFcoeSanPcType_Type()
)
cfprSwFcoeSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwFcoeSanPcType.setStatus("current")
_CfprSwPhysTable_Object = MibTable
cfprSwPhysTable = _CfprSwPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64)
)
if mibBuilder.loadTexts:
    cfprSwPhysTable.setStatus("current")
_CfprSwPhysEntry_Object = MibTableRow
cfprSwPhysEntry = _CfprSwPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1)
)
cfprSwPhysEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwPhysInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwPhysEntry.setStatus("current")
_CfprSwPhysInstanceId_Type = CfprManagedObjectId
_CfprSwPhysInstanceId_Object = MibTableColumn
cfprSwPhysInstanceId = _CfprSwPhysInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 1),
    _CfprSwPhysInstanceId_Type()
)
cfprSwPhysInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwPhysInstanceId.setStatus("current")
_CfprSwPhysDn_Type = CfprManagedObjectDn
_CfprSwPhysDn_Object = MibTableColumn
cfprSwPhysDn = _CfprSwPhysDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 2),
    _CfprSwPhysDn_Type()
)
cfprSwPhysDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysDn.setStatus("current")
_CfprSwPhysRn_Type = SnmpAdminString
_CfprSwPhysRn_Object = MibTableColumn
cfprSwPhysRn = _CfprSwPhysRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 3),
    _CfprSwPhysRn_Type()
)
cfprSwPhysRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysRn.setStatus("current")
_CfprSwPhysConfMode_Type = CfprSwConfMode
_CfprSwPhysConfMode_Object = MibTableColumn
cfprSwPhysConfMode = _CfprSwPhysConfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 4),
    _CfprSwPhysConfMode_Type()
)
cfprSwPhysConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysConfMode.setStatus("current")
_CfprSwPhysFsmDescr_Type = SnmpAdminString
_CfprSwPhysFsmDescr_Object = MibTableColumn
cfprSwPhysFsmDescr = _CfprSwPhysFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 5),
    _CfprSwPhysFsmDescr_Type()
)
cfprSwPhysFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmDescr.setStatus("current")
_CfprSwPhysFsmPrev_Type = SnmpAdminString
_CfprSwPhysFsmPrev_Object = MibTableColumn
cfprSwPhysFsmPrev = _CfprSwPhysFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 6),
    _CfprSwPhysFsmPrev_Type()
)
cfprSwPhysFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmPrev.setStatus("current")
_CfprSwPhysFsmProgr_Type = Gauge32
_CfprSwPhysFsmProgr_Object = MibTableColumn
cfprSwPhysFsmProgr = _CfprSwPhysFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 7),
    _CfprSwPhysFsmProgr_Type()
)
cfprSwPhysFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmProgr.setStatus("current")
_CfprSwPhysFsmRmtInvErrCode_Type = Gauge32
_CfprSwPhysFsmRmtInvErrCode_Object = MibTableColumn
cfprSwPhysFsmRmtInvErrCode = _CfprSwPhysFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 8),
    _CfprSwPhysFsmRmtInvErrCode_Type()
)
cfprSwPhysFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmRmtInvErrCode.setStatus("current")
_CfprSwPhysFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwPhysFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwPhysFsmRmtInvErrDescr = _CfprSwPhysFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 9),
    _CfprSwPhysFsmRmtInvErrDescr_Type()
)
cfprSwPhysFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmRmtInvErrDescr.setStatus("current")
_CfprSwPhysFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwPhysFsmRmtInvRslt_Object = MibTableColumn
cfprSwPhysFsmRmtInvRslt = _CfprSwPhysFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 10),
    _CfprSwPhysFsmRmtInvRslt_Type()
)
cfprSwPhysFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmRmtInvRslt.setStatus("current")
_CfprSwPhysFsmStageDescr_Type = SnmpAdminString
_CfprSwPhysFsmStageDescr_Object = MibTableColumn
cfprSwPhysFsmStageDescr = _CfprSwPhysFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 11),
    _CfprSwPhysFsmStageDescr_Type()
)
cfprSwPhysFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageDescr.setStatus("current")
_CfprSwPhysFsmStamp_Type = DateAndTime
_CfprSwPhysFsmStamp_Object = MibTableColumn
cfprSwPhysFsmStamp = _CfprSwPhysFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 12),
    _CfprSwPhysFsmStamp_Type()
)
cfprSwPhysFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStamp.setStatus("current")
_CfprSwPhysFsmStatus_Type = SnmpAdminString
_CfprSwPhysFsmStatus_Object = MibTableColumn
cfprSwPhysFsmStatus = _CfprSwPhysFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 13),
    _CfprSwPhysFsmStatus_Type()
)
cfprSwPhysFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStatus.setStatus("current")
_CfprSwPhysFsmTry_Type = Gauge32
_CfprSwPhysFsmTry_Object = MibTableColumn
cfprSwPhysFsmTry = _CfprSwPhysFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 64, 1, 14),
    _CfprSwPhysFsmTry_Type()
)
cfprSwPhysFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmTry.setStatus("current")
_CfprSwPhysEtherEpTable_Object = MibTable
cfprSwPhysEtherEpTable = _CfprSwPhysEtherEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65)
)
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpTable.setStatus("current")
_CfprSwPhysEtherEpEntry_Object = MibTableRow
cfprSwPhysEtherEpEntry = _CfprSwPhysEtherEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1)
)
cfprSwPhysEtherEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwPhysEtherEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpEntry.setStatus("current")
_CfprSwPhysEtherEpInstanceId_Type = CfprManagedObjectId
_CfprSwPhysEtherEpInstanceId_Object = MibTableColumn
cfprSwPhysEtherEpInstanceId = _CfprSwPhysEtherEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 1),
    _CfprSwPhysEtherEpInstanceId_Type()
)
cfprSwPhysEtherEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpInstanceId.setStatus("current")
_CfprSwPhysEtherEpDn_Type = CfprManagedObjectDn
_CfprSwPhysEtherEpDn_Object = MibTableColumn
cfprSwPhysEtherEpDn = _CfprSwPhysEtherEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 2),
    _CfprSwPhysEtherEpDn_Type()
)
cfprSwPhysEtherEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpDn.setStatus("current")
_CfprSwPhysEtherEpRn_Type = SnmpAdminString
_CfprSwPhysEtherEpRn_Object = MibTableColumn
cfprSwPhysEtherEpRn = _CfprSwPhysEtherEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 3),
    _CfprSwPhysEtherEpRn_Type()
)
cfprSwPhysEtherEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpRn.setStatus("current")
_CfprSwPhysEtherEpAdminState_Type = CfprFabricAdminState
_CfprSwPhysEtherEpAdminState_Object = MibTableColumn
cfprSwPhysEtherEpAdminState = _CfprSwPhysEtherEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 4),
    _CfprSwPhysEtherEpAdminState_Type()
)
cfprSwPhysEtherEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpAdminState.setStatus("current")
_CfprSwPhysEtherEpAggrPortId_Type = Gauge32
_CfprSwPhysEtherEpAggrPortId_Object = MibTableColumn
cfprSwPhysEtherEpAggrPortId = _CfprSwPhysEtherEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 5),
    _CfprSwPhysEtherEpAggrPortId_Type()
)
cfprSwPhysEtherEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpAggrPortId.setStatus("current")
_CfprSwPhysEtherEpChassisId_Type = Gauge32
_CfprSwPhysEtherEpChassisId_Object = MibTableColumn
cfprSwPhysEtherEpChassisId = _CfprSwPhysEtherEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 6),
    _CfprSwPhysEtherEpChassisId_Type()
)
cfprSwPhysEtherEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpChassisId.setStatus("current")
_CfprSwPhysEtherEpEpDn_Type = SnmpAdminString
_CfprSwPhysEtherEpEpDn_Object = MibTableColumn
cfprSwPhysEtherEpEpDn = _CfprSwPhysEtherEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 7),
    _CfprSwPhysEtherEpEpDn_Type()
)
cfprSwPhysEtherEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpEpDn.setStatus("current")
_CfprSwPhysEtherEpIfRole_Type = CfprNetworkPortRole
_CfprSwPhysEtherEpIfRole_Object = MibTableColumn
cfprSwPhysEtherEpIfRole = _CfprSwPhysEtherEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 8),
    _CfprSwPhysEtherEpIfRole_Type()
)
cfprSwPhysEtherEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpIfRole.setStatus("current")
_CfprSwPhysEtherEpIfType_Type = CfprSwPIoEpIfType
_CfprSwPhysEtherEpIfType_Object = MibTableColumn
cfprSwPhysEtherEpIfType = _CfprSwPhysEtherEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 9),
    _CfprSwPhysEtherEpIfType_Type()
)
cfprSwPhysEtherEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpIfType.setStatus("current")
_CfprSwPhysEtherEpLc_Type = CfprSwPIoEpLc
_CfprSwPhysEtherEpLc_Object = MibTableColumn
cfprSwPhysEtherEpLc = _CfprSwPhysEtherEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 10),
    _CfprSwPhysEtherEpLc_Type()
)
cfprSwPhysEtherEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpLc.setStatus("current")
_CfprSwPhysEtherEpLocale_Type = CfprNetworkLocale
_CfprSwPhysEtherEpLocale_Object = MibTableColumn
cfprSwPhysEtherEpLocale = _CfprSwPhysEtherEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 11),
    _CfprSwPhysEtherEpLocale_Type()
)
cfprSwPhysEtherEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpLocale.setStatus("current")
_CfprSwPhysEtherEpName_Type = SnmpAdminString
_CfprSwPhysEtherEpName_Object = MibTableColumn
cfprSwPhysEtherEpName = _CfprSwPhysEtherEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 12),
    _CfprSwPhysEtherEpName_Type()
)
cfprSwPhysEtherEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpName.setStatus("current")
_CfprSwPhysEtherEpPeerAggrPortId_Type = Gauge32
_CfprSwPhysEtherEpPeerAggrPortId_Object = MibTableColumn
cfprSwPhysEtherEpPeerAggrPortId = _CfprSwPhysEtherEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 13),
    _CfprSwPhysEtherEpPeerAggrPortId_Type()
)
cfprSwPhysEtherEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpPeerAggrPortId.setStatus("current")
_CfprSwPhysEtherEpPeerChassisId_Type = Gauge32
_CfprSwPhysEtherEpPeerChassisId_Object = MibTableColumn
cfprSwPhysEtherEpPeerChassisId = _CfprSwPhysEtherEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 14),
    _CfprSwPhysEtherEpPeerChassisId_Type()
)
cfprSwPhysEtherEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpPeerChassisId.setStatus("current")
_CfprSwPhysEtherEpPeerDn_Type = SnmpAdminString
_CfprSwPhysEtherEpPeerDn_Object = MibTableColumn
cfprSwPhysEtherEpPeerDn = _CfprSwPhysEtherEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 15),
    _CfprSwPhysEtherEpPeerDn_Type()
)
cfprSwPhysEtherEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpPeerDn.setStatus("current")
_CfprSwPhysEtherEpPeerPortId_Type = Gauge32
_CfprSwPhysEtherEpPeerPortId_Object = MibTableColumn
cfprSwPhysEtherEpPeerPortId = _CfprSwPhysEtherEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 16),
    _CfprSwPhysEtherEpPeerPortId_Type()
)
cfprSwPhysEtherEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpPeerPortId.setStatus("current")
_CfprSwPhysEtherEpPeerSlotId_Type = Gauge32
_CfprSwPhysEtherEpPeerSlotId_Object = MibTableColumn
cfprSwPhysEtherEpPeerSlotId = _CfprSwPhysEtherEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 17),
    _CfprSwPhysEtherEpPeerSlotId_Type()
)
cfprSwPhysEtherEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpPeerSlotId.setStatus("current")
_CfprSwPhysEtherEpPortId_Type = Gauge32
_CfprSwPhysEtherEpPortId_Object = MibTableColumn
cfprSwPhysEtherEpPortId = _CfprSwPhysEtherEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 18),
    _CfprSwPhysEtherEpPortId_Type()
)
cfprSwPhysEtherEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpPortId.setStatus("current")
_CfprSwPhysEtherEpSlotId_Type = Gauge32
_CfprSwPhysEtherEpSlotId_Object = MibTableColumn
cfprSwPhysEtherEpSlotId = _CfprSwPhysEtherEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 19),
    _CfprSwPhysEtherEpSlotId_Type()
)
cfprSwPhysEtherEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpSlotId.setStatus("current")
_CfprSwPhysEtherEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwPhysEtherEpSwitchId_Object = MibTableColumn
cfprSwPhysEtherEpSwitchId = _CfprSwPhysEtherEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 20),
    _CfprSwPhysEtherEpSwitchId_Type()
)
cfprSwPhysEtherEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpSwitchId.setStatus("current")
_CfprSwPhysEtherEpTransport_Type = CfprNetworkTransport
_CfprSwPhysEtherEpTransport_Object = MibTableColumn
cfprSwPhysEtherEpTransport = _CfprSwPhysEtherEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 21),
    _CfprSwPhysEtherEpTransport_Type()
)
cfprSwPhysEtherEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpTransport.setStatus("current")
_CfprSwPhysEtherEpType_Type = CfprNetworkConnectionType
_CfprSwPhysEtherEpType_Object = MibTableColumn
cfprSwPhysEtherEpType = _CfprSwPhysEtherEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 65, 1, 22),
    _CfprSwPhysEtherEpType_Type()
)
cfprSwPhysEtherEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysEtherEpType.setStatus("current")
_CfprSwPhysFcEpTable_Object = MibTable
cfprSwPhysFcEpTable = _CfprSwPhysFcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66)
)
if mibBuilder.loadTexts:
    cfprSwPhysFcEpTable.setStatus("current")
_CfprSwPhysFcEpEntry_Object = MibTableRow
cfprSwPhysFcEpEntry = _CfprSwPhysFcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1)
)
cfprSwPhysFcEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwPhysFcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwPhysFcEpEntry.setStatus("current")
_CfprSwPhysFcEpInstanceId_Type = CfprManagedObjectId
_CfprSwPhysFcEpInstanceId_Object = MibTableColumn
cfprSwPhysFcEpInstanceId = _CfprSwPhysFcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 1),
    _CfprSwPhysFcEpInstanceId_Type()
)
cfprSwPhysFcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpInstanceId.setStatus("current")
_CfprSwPhysFcEpDn_Type = CfprManagedObjectDn
_CfprSwPhysFcEpDn_Object = MibTableColumn
cfprSwPhysFcEpDn = _CfprSwPhysFcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 2),
    _CfprSwPhysFcEpDn_Type()
)
cfprSwPhysFcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpDn.setStatus("current")
_CfprSwPhysFcEpRn_Type = SnmpAdminString
_CfprSwPhysFcEpRn_Object = MibTableColumn
cfprSwPhysFcEpRn = _CfprSwPhysFcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 3),
    _CfprSwPhysFcEpRn_Type()
)
cfprSwPhysFcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpRn.setStatus("current")
_CfprSwPhysFcEpAdminState_Type = CfprFabricAdminState
_CfprSwPhysFcEpAdminState_Object = MibTableColumn
cfprSwPhysFcEpAdminState = _CfprSwPhysFcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 4),
    _CfprSwPhysFcEpAdminState_Type()
)
cfprSwPhysFcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpAdminState.setStatus("current")
_CfprSwPhysFcEpAggrPortId_Type = Gauge32
_CfprSwPhysFcEpAggrPortId_Object = MibTableColumn
cfprSwPhysFcEpAggrPortId = _CfprSwPhysFcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 5),
    _CfprSwPhysFcEpAggrPortId_Type()
)
cfprSwPhysFcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpAggrPortId.setStatus("current")
_CfprSwPhysFcEpChassisId_Type = Gauge32
_CfprSwPhysFcEpChassisId_Object = MibTableColumn
cfprSwPhysFcEpChassisId = _CfprSwPhysFcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 6),
    _CfprSwPhysFcEpChassisId_Type()
)
cfprSwPhysFcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpChassisId.setStatus("current")
_CfprSwPhysFcEpEpDn_Type = SnmpAdminString
_CfprSwPhysFcEpEpDn_Object = MibTableColumn
cfprSwPhysFcEpEpDn = _CfprSwPhysFcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 7),
    _CfprSwPhysFcEpEpDn_Type()
)
cfprSwPhysFcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpEpDn.setStatus("current")
_CfprSwPhysFcEpIfRole_Type = CfprNetworkPortRole
_CfprSwPhysFcEpIfRole_Object = MibTableColumn
cfprSwPhysFcEpIfRole = _CfprSwPhysFcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 8),
    _CfprSwPhysFcEpIfRole_Type()
)
cfprSwPhysFcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpIfRole.setStatus("current")
_CfprSwPhysFcEpIfType_Type = CfprSwPIoEpIfType
_CfprSwPhysFcEpIfType_Object = MibTableColumn
cfprSwPhysFcEpIfType = _CfprSwPhysFcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 9),
    _CfprSwPhysFcEpIfType_Type()
)
cfprSwPhysFcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpIfType.setStatus("current")
_CfprSwPhysFcEpLc_Type = CfprSwPIoEpLc
_CfprSwPhysFcEpLc_Object = MibTableColumn
cfprSwPhysFcEpLc = _CfprSwPhysFcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 10),
    _CfprSwPhysFcEpLc_Type()
)
cfprSwPhysFcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpLc.setStatus("current")
_CfprSwPhysFcEpLocale_Type = CfprNetworkLocale
_CfprSwPhysFcEpLocale_Object = MibTableColumn
cfprSwPhysFcEpLocale = _CfprSwPhysFcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 11),
    _CfprSwPhysFcEpLocale_Type()
)
cfprSwPhysFcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpLocale.setStatus("current")
_CfprSwPhysFcEpName_Type = SnmpAdminString
_CfprSwPhysFcEpName_Object = MibTableColumn
cfprSwPhysFcEpName = _CfprSwPhysFcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 12),
    _CfprSwPhysFcEpName_Type()
)
cfprSwPhysFcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpName.setStatus("current")
_CfprSwPhysFcEpPeerAggrPortId_Type = Gauge32
_CfprSwPhysFcEpPeerAggrPortId_Object = MibTableColumn
cfprSwPhysFcEpPeerAggrPortId = _CfprSwPhysFcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 13),
    _CfprSwPhysFcEpPeerAggrPortId_Type()
)
cfprSwPhysFcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpPeerAggrPortId.setStatus("current")
_CfprSwPhysFcEpPeerChassisId_Type = Gauge32
_CfprSwPhysFcEpPeerChassisId_Object = MibTableColumn
cfprSwPhysFcEpPeerChassisId = _CfprSwPhysFcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 14),
    _CfprSwPhysFcEpPeerChassisId_Type()
)
cfprSwPhysFcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpPeerChassisId.setStatus("current")
_CfprSwPhysFcEpPeerDn_Type = SnmpAdminString
_CfprSwPhysFcEpPeerDn_Object = MibTableColumn
cfprSwPhysFcEpPeerDn = _CfprSwPhysFcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 15),
    _CfprSwPhysFcEpPeerDn_Type()
)
cfprSwPhysFcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpPeerDn.setStatus("current")
_CfprSwPhysFcEpPeerPortId_Type = Gauge32
_CfprSwPhysFcEpPeerPortId_Object = MibTableColumn
cfprSwPhysFcEpPeerPortId = _CfprSwPhysFcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 16),
    _CfprSwPhysFcEpPeerPortId_Type()
)
cfprSwPhysFcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpPeerPortId.setStatus("current")
_CfprSwPhysFcEpPeerSlotId_Type = Gauge32
_CfprSwPhysFcEpPeerSlotId_Object = MibTableColumn
cfprSwPhysFcEpPeerSlotId = _CfprSwPhysFcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 17),
    _CfprSwPhysFcEpPeerSlotId_Type()
)
cfprSwPhysFcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpPeerSlotId.setStatus("current")
_CfprSwPhysFcEpPortId_Type = Gauge32
_CfprSwPhysFcEpPortId_Object = MibTableColumn
cfprSwPhysFcEpPortId = _CfprSwPhysFcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 18),
    _CfprSwPhysFcEpPortId_Type()
)
cfprSwPhysFcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpPortId.setStatus("current")
_CfprSwPhysFcEpSlotId_Type = Gauge32
_CfprSwPhysFcEpSlotId_Object = MibTableColumn
cfprSwPhysFcEpSlotId = _CfprSwPhysFcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 19),
    _CfprSwPhysFcEpSlotId_Type()
)
cfprSwPhysFcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpSlotId.setStatus("current")
_CfprSwPhysFcEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwPhysFcEpSwitchId_Object = MibTableColumn
cfprSwPhysFcEpSwitchId = _CfprSwPhysFcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 20),
    _CfprSwPhysFcEpSwitchId_Type()
)
cfprSwPhysFcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpSwitchId.setStatus("current")
_CfprSwPhysFcEpTransport_Type = CfprNetworkTransport
_CfprSwPhysFcEpTransport_Object = MibTableColumn
cfprSwPhysFcEpTransport = _CfprSwPhysFcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 21),
    _CfprSwPhysFcEpTransport_Type()
)
cfprSwPhysFcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpTransport.setStatus("current")
_CfprSwPhysFcEpType_Type = CfprNetworkConnectionType
_CfprSwPhysFcEpType_Object = MibTableColumn
cfprSwPhysFcEpType = _CfprSwPhysFcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 66, 1, 22),
    _CfprSwPhysFcEpType_Type()
)
cfprSwPhysFcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFcEpType.setStatus("current")
_CfprSwPhysFsmTable_Object = MibTable
cfprSwPhysFsmTable = _CfprSwPhysFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67)
)
if mibBuilder.loadTexts:
    cfprSwPhysFsmTable.setStatus("current")
_CfprSwPhysFsmEntry_Object = MibTableRow
cfprSwPhysFsmEntry = _CfprSwPhysFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1)
)
cfprSwPhysFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwPhysFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwPhysFsmEntry.setStatus("current")
_CfprSwPhysFsmInstanceId_Type = CfprManagedObjectId
_CfprSwPhysFsmInstanceId_Object = MibTableColumn
cfprSwPhysFsmInstanceId = _CfprSwPhysFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 1),
    _CfprSwPhysFsmInstanceId_Type()
)
cfprSwPhysFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwPhysFsmInstanceId.setStatus("current")
_CfprSwPhysFsmDn_Type = CfprManagedObjectDn
_CfprSwPhysFsmDn_Object = MibTableColumn
cfprSwPhysFsmDn = _CfprSwPhysFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 2),
    _CfprSwPhysFsmDn_Type()
)
cfprSwPhysFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmDn.setStatus("current")
_CfprSwPhysFsmRn_Type = SnmpAdminString
_CfprSwPhysFsmRn_Object = MibTableColumn
cfprSwPhysFsmRn = _CfprSwPhysFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 3),
    _CfprSwPhysFsmRn_Type()
)
cfprSwPhysFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmRn.setStatus("current")
_CfprSwPhysFsmCompletionTime_Type = DateAndTime
_CfprSwPhysFsmCompletionTime_Object = MibTableColumn
cfprSwPhysFsmCompletionTime = _CfprSwPhysFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 4),
    _CfprSwPhysFsmCompletionTime_Type()
)
cfprSwPhysFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmCompletionTime.setStatus("current")
_CfprSwPhysFsmCurrentFsm_Type = CfprSwPhysFsmCurrentFsm
_CfprSwPhysFsmCurrentFsm_Object = MibTableColumn
cfprSwPhysFsmCurrentFsm = _CfprSwPhysFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 5),
    _CfprSwPhysFsmCurrentFsm_Type()
)
cfprSwPhysFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmCurrentFsm.setStatus("current")
_CfprSwPhysFsmDescrData_Type = SnmpAdminString
_CfprSwPhysFsmDescrData_Object = MibTableColumn
cfprSwPhysFsmDescrData = _CfprSwPhysFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 6),
    _CfprSwPhysFsmDescrData_Type()
)
cfprSwPhysFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmDescrData.setStatus("current")
_CfprSwPhysFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwPhysFsmFsmStatus_Object = MibTableColumn
cfprSwPhysFsmFsmStatus = _CfprSwPhysFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 7),
    _CfprSwPhysFsmFsmStatus_Type()
)
cfprSwPhysFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmFsmStatus.setStatus("current")
_CfprSwPhysFsmProgress_Type = Gauge32
_CfprSwPhysFsmProgress_Object = MibTableColumn
cfprSwPhysFsmProgress = _CfprSwPhysFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 8),
    _CfprSwPhysFsmProgress_Type()
)
cfprSwPhysFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmProgress.setStatus("current")
_CfprSwPhysFsmRmtErrCode_Type = Gauge32
_CfprSwPhysFsmRmtErrCode_Object = MibTableColumn
cfprSwPhysFsmRmtErrCode = _CfprSwPhysFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 9),
    _CfprSwPhysFsmRmtErrCode_Type()
)
cfprSwPhysFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmRmtErrCode.setStatus("current")
_CfprSwPhysFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwPhysFsmRmtErrDescr_Object = MibTableColumn
cfprSwPhysFsmRmtErrDescr = _CfprSwPhysFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 10),
    _CfprSwPhysFsmRmtErrDescr_Type()
)
cfprSwPhysFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmRmtErrDescr.setStatus("current")
_CfprSwPhysFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwPhysFsmRmtRslt_Object = MibTableColumn
cfprSwPhysFsmRmtRslt = _CfprSwPhysFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 67, 1, 11),
    _CfprSwPhysFsmRmtRslt_Type()
)
cfprSwPhysFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmRmtRslt.setStatus("current")
_CfprSwPhysFsmStageTable_Object = MibTable
cfprSwPhysFsmStageTable = _CfprSwPhysFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68)
)
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageTable.setStatus("current")
_CfprSwPhysFsmStageEntry_Object = MibTableRow
cfprSwPhysFsmStageEntry = _CfprSwPhysFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1)
)
cfprSwPhysFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwPhysFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageEntry.setStatus("current")
_CfprSwPhysFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwPhysFsmStageInstanceId_Object = MibTableColumn
cfprSwPhysFsmStageInstanceId = _CfprSwPhysFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 1),
    _CfprSwPhysFsmStageInstanceId_Type()
)
cfprSwPhysFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageInstanceId.setStatus("current")
_CfprSwPhysFsmStageDn_Type = CfprManagedObjectDn
_CfprSwPhysFsmStageDn_Object = MibTableColumn
cfprSwPhysFsmStageDn = _CfprSwPhysFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 2),
    _CfprSwPhysFsmStageDn_Type()
)
cfprSwPhysFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageDn.setStatus("current")
_CfprSwPhysFsmStageRn_Type = SnmpAdminString
_CfprSwPhysFsmStageRn_Object = MibTableColumn
cfprSwPhysFsmStageRn = _CfprSwPhysFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 3),
    _CfprSwPhysFsmStageRn_Type()
)
cfprSwPhysFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageRn.setStatus("current")
_CfprSwPhysFsmStageDescrData_Type = SnmpAdminString
_CfprSwPhysFsmStageDescrData_Object = MibTableColumn
cfprSwPhysFsmStageDescrData = _CfprSwPhysFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 4),
    _CfprSwPhysFsmStageDescrData_Type()
)
cfprSwPhysFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageDescrData.setStatus("current")
_CfprSwPhysFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwPhysFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwPhysFsmStageLastUpdateTime = _CfprSwPhysFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 5),
    _CfprSwPhysFsmStageLastUpdateTime_Type()
)
cfprSwPhysFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageLastUpdateTime.setStatus("current")
_CfprSwPhysFsmStageName_Type = CfprSwPhysFsmStageName
_CfprSwPhysFsmStageName_Object = MibTableColumn
cfprSwPhysFsmStageName = _CfprSwPhysFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 6),
    _CfprSwPhysFsmStageName_Type()
)
cfprSwPhysFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageName.setStatus("current")
_CfprSwPhysFsmStageOrder_Type = Gauge32
_CfprSwPhysFsmStageOrder_Object = MibTableColumn
cfprSwPhysFsmStageOrder = _CfprSwPhysFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 7),
    _CfprSwPhysFsmStageOrder_Type()
)
cfprSwPhysFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageOrder.setStatus("current")
_CfprSwPhysFsmStageRetry_Type = Gauge32
_CfprSwPhysFsmStageRetry_Object = MibTableColumn
cfprSwPhysFsmStageRetry = _CfprSwPhysFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 8),
    _CfprSwPhysFsmStageRetry_Type()
)
cfprSwPhysFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageRetry.setStatus("current")
_CfprSwPhysFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwPhysFsmStageStageStatus_Object = MibTableColumn
cfprSwPhysFsmStageStageStatus = _CfprSwPhysFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 68, 1, 9),
    _CfprSwPhysFsmStageStageStatus_Type()
)
cfprSwPhysFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmStageStageStatus.setStatus("current")
_CfprSwPhysFsmTaskTable_Object = MibTable
cfprSwPhysFsmTaskTable = _CfprSwPhysFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69)
)
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskTable.setStatus("current")
_CfprSwPhysFsmTaskEntry_Object = MibTableRow
cfprSwPhysFsmTaskEntry = _CfprSwPhysFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69, 1)
)
cfprSwPhysFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwPhysFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskEntry.setStatus("current")
_CfprSwPhysFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwPhysFsmTaskInstanceId_Object = MibTableColumn
cfprSwPhysFsmTaskInstanceId = _CfprSwPhysFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69, 1, 1),
    _CfprSwPhysFsmTaskInstanceId_Type()
)
cfprSwPhysFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskInstanceId.setStatus("current")
_CfprSwPhysFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwPhysFsmTaskDn_Object = MibTableColumn
cfprSwPhysFsmTaskDn = _CfprSwPhysFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69, 1, 2),
    _CfprSwPhysFsmTaskDn_Type()
)
cfprSwPhysFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskDn.setStatus("current")
_CfprSwPhysFsmTaskRn_Type = SnmpAdminString
_CfprSwPhysFsmTaskRn_Object = MibTableColumn
cfprSwPhysFsmTaskRn = _CfprSwPhysFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69, 1, 3),
    _CfprSwPhysFsmTaskRn_Type()
)
cfprSwPhysFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskRn.setStatus("current")
_CfprSwPhysFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwPhysFsmTaskCompletion_Object = MibTableColumn
cfprSwPhysFsmTaskCompletion = _CfprSwPhysFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69, 1, 4),
    _CfprSwPhysFsmTaskCompletion_Type()
)
cfprSwPhysFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskCompletion.setStatus("current")
_CfprSwPhysFsmTaskFlags_Type = CfprFsmFlags
_CfprSwPhysFsmTaskFlags_Object = MibTableColumn
cfprSwPhysFsmTaskFlags = _CfprSwPhysFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69, 1, 5),
    _CfprSwPhysFsmTaskFlags_Type()
)
cfprSwPhysFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskFlags.setStatus("current")
_CfprSwPhysFsmTaskItem_Type = CfprSwPhysFsmTaskItem
_CfprSwPhysFsmTaskItem_Object = MibTableColumn
cfprSwPhysFsmTaskItem = _CfprSwPhysFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69, 1, 6),
    _CfprSwPhysFsmTaskItem_Type()
)
cfprSwPhysFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskItem.setStatus("current")
_CfprSwPhysFsmTaskSeqId_Type = Gauge32
_CfprSwPhysFsmTaskSeqId_Object = MibTableColumn
cfprSwPhysFsmTaskSeqId = _CfprSwPhysFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 69, 1, 7),
    _CfprSwPhysFsmTaskSeqId_Type()
)
cfprSwPhysFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPhysFsmTaskSeqId.setStatus("current")
_CfprSwPortBreakoutTable_Object = MibTable
cfprSwPortBreakoutTable = _CfprSwPortBreakoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 70)
)
if mibBuilder.loadTexts:
    cfprSwPortBreakoutTable.setStatus("current")
_CfprSwPortBreakoutEntry_Object = MibTableRow
cfprSwPortBreakoutEntry = _CfprSwPortBreakoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 70, 1)
)
cfprSwPortBreakoutEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwPortBreakoutInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwPortBreakoutEntry.setStatus("current")
_CfprSwPortBreakoutInstanceId_Type = CfprManagedObjectId
_CfprSwPortBreakoutInstanceId_Object = MibTableColumn
cfprSwPortBreakoutInstanceId = _CfprSwPortBreakoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 70, 1, 1),
    _CfprSwPortBreakoutInstanceId_Type()
)
cfprSwPortBreakoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwPortBreakoutInstanceId.setStatus("current")
_CfprSwPortBreakoutDn_Type = CfprManagedObjectDn
_CfprSwPortBreakoutDn_Object = MibTableColumn
cfprSwPortBreakoutDn = _CfprSwPortBreakoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 70, 1, 2),
    _CfprSwPortBreakoutDn_Type()
)
cfprSwPortBreakoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPortBreakoutDn.setStatus("current")
_CfprSwPortBreakoutRn_Type = SnmpAdminString
_CfprSwPortBreakoutRn_Object = MibTableColumn
cfprSwPortBreakoutRn = _CfprSwPortBreakoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 70, 1, 3),
    _CfprSwPortBreakoutRn_Type()
)
cfprSwPortBreakoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPortBreakoutRn.setStatus("current")
_CfprSwPortBreakoutBreakoutType_Type = CfprSwBreakoutType
_CfprSwPortBreakoutBreakoutType_Object = MibTableColumn
cfprSwPortBreakoutBreakoutType = _CfprSwPortBreakoutBreakoutType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 70, 1, 4),
    _CfprSwPortBreakoutBreakoutType_Type()
)
cfprSwPortBreakoutBreakoutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPortBreakoutBreakoutType.setStatus("current")
_CfprSwPortBreakoutPortId_Type = CfprSwPortBreakoutPortId
_CfprSwPortBreakoutPortId_Object = MibTableColumn
cfprSwPortBreakoutPortId = _CfprSwPortBreakoutPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 70, 1, 5),
    _CfprSwPortBreakoutPortId_Type()
)
cfprSwPortBreakoutPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPortBreakoutPortId.setStatus("current")
_CfprSwPortBreakoutSlotId_Type = CfprSwPortBreakoutSlotId
_CfprSwPortBreakoutSlotId_Object = MibTableColumn
cfprSwPortBreakoutSlotId = _CfprSwPortBreakoutSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 70, 1, 6),
    _CfprSwPortBreakoutSlotId_Type()
)
cfprSwPortBreakoutSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwPortBreakoutSlotId.setStatus("current")
_CfprSwSubGroupTable_Object = MibTable
cfprSwSubGroupTable = _CfprSwSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71)
)
if mibBuilder.loadTexts:
    cfprSwSubGroupTable.setStatus("current")
_CfprSwSubGroupEntry_Object = MibTableRow
cfprSwSubGroupEntry = _CfprSwSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1)
)
cfprSwSubGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSubGroupEntry.setStatus("current")
_CfprSwSubGroupInstanceId_Type = CfprManagedObjectId
_CfprSwSubGroupInstanceId_Object = MibTableColumn
cfprSwSubGroupInstanceId = _CfprSwSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 1),
    _CfprSwSubGroupInstanceId_Type()
)
cfprSwSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSubGroupInstanceId.setStatus("current")
_CfprSwSubGroupDn_Type = CfprManagedObjectDn
_CfprSwSubGroupDn_Object = MibTableColumn
cfprSwSubGroupDn = _CfprSwSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 2),
    _CfprSwSubGroupDn_Type()
)
cfprSwSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupDn.setStatus("current")
_CfprSwSubGroupRn_Type = SnmpAdminString
_CfprSwSubGroupRn_Object = MibTableColumn
cfprSwSubGroupRn = _CfprSwSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 3),
    _CfprSwSubGroupRn_Type()
)
cfprSwSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupRn.setStatus("current")
_CfprSwSubGroupAggrPortId_Type = CfprSwSubGroupAggrPortId
_CfprSwSubGroupAggrPortId_Object = MibTableColumn
cfprSwSubGroupAggrPortId = _CfprSwSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 4),
    _CfprSwSubGroupAggrPortId_Type()
)
cfprSwSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupAggrPortId.setStatus("current")
_CfprSwSubGroupLicGP_Type = Unsigned64
_CfprSwSubGroupLicGP_Object = MibTableColumn
cfprSwSubGroupLicGP = _CfprSwSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 5),
    _CfprSwSubGroupLicGP_Type()
)
cfprSwSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupLicGP.setStatus("current")
_CfprSwSubGroupLicState_Type = CfprLicenseState
_CfprSwSubGroupLicState_Object = MibTableColumn
cfprSwSubGroupLicState = _CfprSwSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 6),
    _CfprSwSubGroupLicState_Type()
)
cfprSwSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupLicState.setStatus("current")
_CfprSwSubGroupLocale_Type = CfprNetworkLocale
_CfprSwSubGroupLocale_Object = MibTableColumn
cfprSwSubGroupLocale = _CfprSwSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 7),
    _CfprSwSubGroupLocale_Type()
)
cfprSwSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupLocale.setStatus("current")
_CfprSwSubGroupName_Type = SnmpAdminString
_CfprSwSubGroupName_Object = MibTableColumn
cfprSwSubGroupName = _CfprSwSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 8),
    _CfprSwSubGroupName_Type()
)
cfprSwSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupName.setStatus("current")
_CfprSwSubGroupSlotId_Type = CfprSwSubGroupSlotId
_CfprSwSubGroupSlotId_Object = MibTableColumn
cfprSwSubGroupSlotId = _CfprSwSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 9),
    _CfprSwSubGroupSlotId_Type()
)
cfprSwSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupSlotId.setStatus("current")
_CfprSwSubGroupSwitchId_Type = CfprNetworkSwitchId
_CfprSwSubGroupSwitchId_Object = MibTableColumn
cfprSwSubGroupSwitchId = _CfprSwSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 10),
    _CfprSwSubGroupSwitchId_Type()
)
cfprSwSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupSwitchId.setStatus("current")
_CfprSwSubGroupTransport_Type = CfprNetworkTransport
_CfprSwSubGroupTransport_Object = MibTableColumn
cfprSwSubGroupTransport = _CfprSwSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 11),
    _CfprSwSubGroupTransport_Type()
)
cfprSwSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupTransport.setStatus("current")
_CfprSwSubGroupType_Type = CfprNetworkConnectionType
_CfprSwSubGroupType_Object = MibTableColumn
cfprSwSubGroupType = _CfprSwSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 71, 1, 12),
    _CfprSwSubGroupType_Type()
)
cfprSwSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSubGroupType.setStatus("current")
_CfprSwSystemStatsTable_Object = MibTable
cfprSwSystemStatsTable = _CfprSwSystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72)
)
if mibBuilder.loadTexts:
    cfprSwSystemStatsTable.setStatus("current")
_CfprSwSystemStatsEntry_Object = MibTableRow
cfprSwSystemStatsEntry = _CfprSwSystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1)
)
cfprSwSystemStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSystemStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSystemStatsEntry.setStatus("current")
_CfprSwSystemStatsInstanceId_Type = CfprManagedObjectId
_CfprSwSystemStatsInstanceId_Object = MibTableColumn
cfprSwSystemStatsInstanceId = _CfprSwSystemStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 1),
    _CfprSwSystemStatsInstanceId_Type()
)
cfprSwSystemStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSystemStatsInstanceId.setStatus("current")
_CfprSwSystemStatsDn_Type = CfprManagedObjectDn
_CfprSwSystemStatsDn_Object = MibTableColumn
cfprSwSystemStatsDn = _CfprSwSystemStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 2),
    _CfprSwSystemStatsDn_Type()
)
cfprSwSystemStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsDn.setStatus("current")
_CfprSwSystemStatsRn_Type = SnmpAdminString
_CfprSwSystemStatsRn_Object = MibTableColumn
cfprSwSystemStatsRn = _CfprSwSystemStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 3),
    _CfprSwSystemStatsRn_Type()
)
cfprSwSystemStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsRn.setStatus("current")
_CfprSwSystemStatsIntervals_Type = Gauge32
_CfprSwSystemStatsIntervals_Object = MibTableColumn
cfprSwSystemStatsIntervals = _CfprSwSystemStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 4),
    _CfprSwSystemStatsIntervals_Type()
)
cfprSwSystemStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsIntervals.setStatus("current")
_CfprSwSystemStatsLoad_Type = Integer32
_CfprSwSystemStatsLoad_Object = MibTableColumn
cfprSwSystemStatsLoad = _CfprSwSystemStatsLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 5),
    _CfprSwSystemStatsLoad_Type()
)
cfprSwSystemStatsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsLoad.setStatus("current")
_CfprSwSystemStatsLoadAvg_Type = Integer32
_CfprSwSystemStatsLoadAvg_Object = MibTableColumn
cfprSwSystemStatsLoadAvg = _CfprSwSystemStatsLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 6),
    _CfprSwSystemStatsLoadAvg_Type()
)
cfprSwSystemStatsLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsLoadAvg.setStatus("current")
_CfprSwSystemStatsLoadMax_Type = Integer32
_CfprSwSystemStatsLoadMax_Object = MibTableColumn
cfprSwSystemStatsLoadMax = _CfprSwSystemStatsLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 7),
    _CfprSwSystemStatsLoadMax_Type()
)
cfprSwSystemStatsLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsLoadMax.setStatus("current")
_CfprSwSystemStatsLoadMin_Type = Integer32
_CfprSwSystemStatsLoadMin_Object = MibTableColumn
cfprSwSystemStatsLoadMin = _CfprSwSystemStatsLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 8),
    _CfprSwSystemStatsLoadMin_Type()
)
cfprSwSystemStatsLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsLoadMin.setStatus("current")
_CfprSwSystemStatsMemAvailable_Type = Gauge32
_CfprSwSystemStatsMemAvailable_Object = MibTableColumn
cfprSwSystemStatsMemAvailable = _CfprSwSystemStatsMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 9),
    _CfprSwSystemStatsMemAvailable_Type()
)
cfprSwSystemStatsMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsMemAvailable.setStatus("current")
_CfprSwSystemStatsMemAvailableAvg_Type = Gauge32
_CfprSwSystemStatsMemAvailableAvg_Object = MibTableColumn
cfprSwSystemStatsMemAvailableAvg = _CfprSwSystemStatsMemAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 10),
    _CfprSwSystemStatsMemAvailableAvg_Type()
)
cfprSwSystemStatsMemAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsMemAvailableAvg.setStatus("current")
_CfprSwSystemStatsMemAvailableMax_Type = Gauge32
_CfprSwSystemStatsMemAvailableMax_Object = MibTableColumn
cfprSwSystemStatsMemAvailableMax = _CfprSwSystemStatsMemAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 11),
    _CfprSwSystemStatsMemAvailableMax_Type()
)
cfprSwSystemStatsMemAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsMemAvailableMax.setStatus("current")
_CfprSwSystemStatsMemAvailableMin_Type = Gauge32
_CfprSwSystemStatsMemAvailableMin_Object = MibTableColumn
cfprSwSystemStatsMemAvailableMin = _CfprSwSystemStatsMemAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 12),
    _CfprSwSystemStatsMemAvailableMin_Type()
)
cfprSwSystemStatsMemAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsMemAvailableMin.setStatus("current")
_CfprSwSystemStatsMemCached_Type = Gauge32
_CfprSwSystemStatsMemCached_Object = MibTableColumn
cfprSwSystemStatsMemCached = _CfprSwSystemStatsMemCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 13),
    _CfprSwSystemStatsMemCached_Type()
)
cfprSwSystemStatsMemCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsMemCached.setStatus("current")
_CfprSwSystemStatsMemCachedAvg_Type = Gauge32
_CfprSwSystemStatsMemCachedAvg_Object = MibTableColumn
cfprSwSystemStatsMemCachedAvg = _CfprSwSystemStatsMemCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 14),
    _CfprSwSystemStatsMemCachedAvg_Type()
)
cfprSwSystemStatsMemCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsMemCachedAvg.setStatus("current")
_CfprSwSystemStatsMemCachedMax_Type = Gauge32
_CfprSwSystemStatsMemCachedMax_Object = MibTableColumn
cfprSwSystemStatsMemCachedMax = _CfprSwSystemStatsMemCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 15),
    _CfprSwSystemStatsMemCachedMax_Type()
)
cfprSwSystemStatsMemCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsMemCachedMax.setStatus("current")
_CfprSwSystemStatsMemCachedMin_Type = Gauge32
_CfprSwSystemStatsMemCachedMin_Object = MibTableColumn
cfprSwSystemStatsMemCachedMin = _CfprSwSystemStatsMemCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 16),
    _CfprSwSystemStatsMemCachedMin_Type()
)
cfprSwSystemStatsMemCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsMemCachedMin.setStatus("current")
_CfprSwSystemStatsSuspect_Type = TruthValue
_CfprSwSystemStatsSuspect_Object = MibTableColumn
cfprSwSystemStatsSuspect = _CfprSwSystemStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 17),
    _CfprSwSystemStatsSuspect_Type()
)
cfprSwSystemStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsSuspect.setStatus("current")
_CfprSwSystemStatsThresholded_Type = CfprSwSystemStatsThresholded
_CfprSwSystemStatsThresholded_Object = MibTableColumn
cfprSwSystemStatsThresholded = _CfprSwSystemStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 18),
    _CfprSwSystemStatsThresholded_Type()
)
cfprSwSystemStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsThresholded.setStatus("current")
_CfprSwSystemStatsTimeCollected_Type = DateAndTime
_CfprSwSystemStatsTimeCollected_Object = MibTableColumn
cfprSwSystemStatsTimeCollected = _CfprSwSystemStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 19),
    _CfprSwSystemStatsTimeCollected_Type()
)
cfprSwSystemStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsTimeCollected.setStatus("current")
_CfprSwSystemStatsUpdate_Type = Gauge32
_CfprSwSystemStatsUpdate_Object = MibTableColumn
cfprSwSystemStatsUpdate = _CfprSwSystemStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 72, 1, 20),
    _CfprSwSystemStatsUpdate_Type()
)
cfprSwSystemStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsUpdate.setStatus("current")
_CfprSwSystemStatsHistTable_Object = MibTable
cfprSwSystemStatsHistTable = _CfprSwSystemStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73)
)
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistTable.setStatus("current")
_CfprSwSystemStatsHistEntry_Object = MibTableRow
cfprSwSystemStatsHistEntry = _CfprSwSystemStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1)
)
cfprSwSystemStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSystemStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistEntry.setStatus("current")
_CfprSwSystemStatsHistInstanceId_Type = CfprManagedObjectId
_CfprSwSystemStatsHistInstanceId_Object = MibTableColumn
cfprSwSystemStatsHistInstanceId = _CfprSwSystemStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 1),
    _CfprSwSystemStatsHistInstanceId_Type()
)
cfprSwSystemStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistInstanceId.setStatus("current")
_CfprSwSystemStatsHistDn_Type = CfprManagedObjectDn
_CfprSwSystemStatsHistDn_Object = MibTableColumn
cfprSwSystemStatsHistDn = _CfprSwSystemStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 2),
    _CfprSwSystemStatsHistDn_Type()
)
cfprSwSystemStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistDn.setStatus("current")
_CfprSwSystemStatsHistRn_Type = SnmpAdminString
_CfprSwSystemStatsHistRn_Object = MibTableColumn
cfprSwSystemStatsHistRn = _CfprSwSystemStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 3),
    _CfprSwSystemStatsHistRn_Type()
)
cfprSwSystemStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistRn.setStatus("current")
_CfprSwSystemStatsHistId_Type = Unsigned64
_CfprSwSystemStatsHistId_Object = MibTableColumn
cfprSwSystemStatsHistId = _CfprSwSystemStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 4),
    _CfprSwSystemStatsHistId_Type()
)
cfprSwSystemStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistId.setStatus("current")
_CfprSwSystemStatsHistLoad_Type = Integer32
_CfprSwSystemStatsHistLoad_Object = MibTableColumn
cfprSwSystemStatsHistLoad = _CfprSwSystemStatsHistLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 5),
    _CfprSwSystemStatsHistLoad_Type()
)
cfprSwSystemStatsHistLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistLoad.setStatus("current")
_CfprSwSystemStatsHistLoadAvg_Type = Integer32
_CfprSwSystemStatsHistLoadAvg_Object = MibTableColumn
cfprSwSystemStatsHistLoadAvg = _CfprSwSystemStatsHistLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 6),
    _CfprSwSystemStatsHistLoadAvg_Type()
)
cfprSwSystemStatsHistLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistLoadAvg.setStatus("current")
_CfprSwSystemStatsHistLoadMax_Type = Integer32
_CfprSwSystemStatsHistLoadMax_Object = MibTableColumn
cfprSwSystemStatsHistLoadMax = _CfprSwSystemStatsHistLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 7),
    _CfprSwSystemStatsHistLoadMax_Type()
)
cfprSwSystemStatsHistLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistLoadMax.setStatus("current")
_CfprSwSystemStatsHistLoadMin_Type = Integer32
_CfprSwSystemStatsHistLoadMin_Object = MibTableColumn
cfprSwSystemStatsHistLoadMin = _CfprSwSystemStatsHistLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 8),
    _CfprSwSystemStatsHistLoadMin_Type()
)
cfprSwSystemStatsHistLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistLoadMin.setStatus("current")
_CfprSwSystemStatsHistMemAvailable_Type = Gauge32
_CfprSwSystemStatsHistMemAvailable_Object = MibTableColumn
cfprSwSystemStatsHistMemAvailable = _CfprSwSystemStatsHistMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 9),
    _CfprSwSystemStatsHistMemAvailable_Type()
)
cfprSwSystemStatsHistMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMemAvailable.setStatus("current")
_CfprSwSystemStatsHistMemAvailableAvg_Type = Gauge32
_CfprSwSystemStatsHistMemAvailableAvg_Object = MibTableColumn
cfprSwSystemStatsHistMemAvailableAvg = _CfprSwSystemStatsHistMemAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 10),
    _CfprSwSystemStatsHistMemAvailableAvg_Type()
)
cfprSwSystemStatsHistMemAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMemAvailableAvg.setStatus("current")
_CfprSwSystemStatsHistMemAvailableMax_Type = Gauge32
_CfprSwSystemStatsHistMemAvailableMax_Object = MibTableColumn
cfprSwSystemStatsHistMemAvailableMax = _CfprSwSystemStatsHistMemAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 11),
    _CfprSwSystemStatsHistMemAvailableMax_Type()
)
cfprSwSystemStatsHistMemAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMemAvailableMax.setStatus("current")
_CfprSwSystemStatsHistMemAvailableMin_Type = Gauge32
_CfprSwSystemStatsHistMemAvailableMin_Object = MibTableColumn
cfprSwSystemStatsHistMemAvailableMin = _CfprSwSystemStatsHistMemAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 12),
    _CfprSwSystemStatsHistMemAvailableMin_Type()
)
cfprSwSystemStatsHistMemAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMemAvailableMin.setStatus("current")
_CfprSwSystemStatsHistMemCached_Type = Gauge32
_CfprSwSystemStatsHistMemCached_Object = MibTableColumn
cfprSwSystemStatsHistMemCached = _CfprSwSystemStatsHistMemCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 13),
    _CfprSwSystemStatsHistMemCached_Type()
)
cfprSwSystemStatsHistMemCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMemCached.setStatus("current")
_CfprSwSystemStatsHistMemCachedAvg_Type = Gauge32
_CfprSwSystemStatsHistMemCachedAvg_Object = MibTableColumn
cfprSwSystemStatsHistMemCachedAvg = _CfprSwSystemStatsHistMemCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 14),
    _CfprSwSystemStatsHistMemCachedAvg_Type()
)
cfprSwSystemStatsHistMemCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMemCachedAvg.setStatus("current")
_CfprSwSystemStatsHistMemCachedMax_Type = Gauge32
_CfprSwSystemStatsHistMemCachedMax_Object = MibTableColumn
cfprSwSystemStatsHistMemCachedMax = _CfprSwSystemStatsHistMemCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 15),
    _CfprSwSystemStatsHistMemCachedMax_Type()
)
cfprSwSystemStatsHistMemCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMemCachedMax.setStatus("current")
_CfprSwSystemStatsHistMemCachedMin_Type = Gauge32
_CfprSwSystemStatsHistMemCachedMin_Object = MibTableColumn
cfprSwSystemStatsHistMemCachedMin = _CfprSwSystemStatsHistMemCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 16),
    _CfprSwSystemStatsHistMemCachedMin_Type()
)
cfprSwSystemStatsHistMemCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMemCachedMin.setStatus("current")
_CfprSwSystemStatsHistMostRecent_Type = TruthValue
_CfprSwSystemStatsHistMostRecent_Object = MibTableColumn
cfprSwSystemStatsHistMostRecent = _CfprSwSystemStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 17),
    _CfprSwSystemStatsHistMostRecent_Type()
)
cfprSwSystemStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistMostRecent.setStatus("current")
_CfprSwSystemStatsHistSuspect_Type = TruthValue
_CfprSwSystemStatsHistSuspect_Object = MibTableColumn
cfprSwSystemStatsHistSuspect = _CfprSwSystemStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 18),
    _CfprSwSystemStatsHistSuspect_Type()
)
cfprSwSystemStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistSuspect.setStatus("current")
_CfprSwSystemStatsHistThresholded_Type = CfprSwSystemStatsHistThresholded
_CfprSwSystemStatsHistThresholded_Object = MibTableColumn
cfprSwSystemStatsHistThresholded = _CfprSwSystemStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 19),
    _CfprSwSystemStatsHistThresholded_Type()
)
cfprSwSystemStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistThresholded.setStatus("current")
_CfprSwSystemStatsHistTimeCollected_Type = DateAndTime
_CfprSwSystemStatsHistTimeCollected_Object = MibTableColumn
cfprSwSystemStatsHistTimeCollected = _CfprSwSystemStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 73, 1, 20),
    _CfprSwSystemStatsHistTimeCollected_Type()
)
cfprSwSystemStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSystemStatsHistTimeCollected.setStatus("current")
_CfprSwUlanTable_Object = MibTable
cfprSwUlanTable = _CfprSwUlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74)
)
if mibBuilder.loadTexts:
    cfprSwUlanTable.setStatus("current")
_CfprSwUlanEntry_Object = MibTableRow
cfprSwUlanEntry = _CfprSwUlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1)
)
cfprSwUlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwUlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwUlanEntry.setStatus("current")
_CfprSwUlanInstanceId_Type = CfprManagedObjectId
_CfprSwUlanInstanceId_Object = MibTableColumn
cfprSwUlanInstanceId = _CfprSwUlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 1),
    _CfprSwUlanInstanceId_Type()
)
cfprSwUlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwUlanInstanceId.setStatus("current")
_CfprSwUlanDn_Type = CfprManagedObjectDn
_CfprSwUlanDn_Object = MibTableColumn
cfprSwUlanDn = _CfprSwUlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 2),
    _CfprSwUlanDn_Type()
)
cfprSwUlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanDn.setStatus("current")
_CfprSwUlanRn_Type = SnmpAdminString
_CfprSwUlanRn_Object = MibTableColumn
cfprSwUlanRn = _CfprSwUlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 3),
    _CfprSwUlanRn_Type()
)
cfprSwUlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanRn.setStatus("current")
_CfprSwUlanAssocPrimaryVlanState_Type = CfprFabricVlanAssocPrimaryVlanState
_CfprSwUlanAssocPrimaryVlanState_Object = MibTableColumn
cfprSwUlanAssocPrimaryVlanState = _CfprSwUlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 4),
    _CfprSwUlanAssocPrimaryVlanState_Type()
)
cfprSwUlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanAssocPrimaryVlanState.setStatus("current")
_CfprSwUlanAssocPrimaryVlanSwitchId_Type = CfprFabricAVlanAssocPrimaryVlanSwitchId
_CfprSwUlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprSwUlanAssocPrimaryVlanSwitchId = _CfprSwUlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 5),
    _CfprSwUlanAssocPrimaryVlanSwitchId_Type()
)
cfprSwUlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprSwUlanEpDn_Type = SnmpAdminString
_CfprSwUlanEpDn_Object = MibTableColumn
cfprSwUlanEpDn = _CfprSwUlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 6),
    _CfprSwUlanEpDn_Type()
)
cfprSwUlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanEpDn.setStatus("current")
_CfprSwUlanId_Type = Gauge32
_CfprSwUlanId_Object = MibTableColumn
cfprSwUlanId = _CfprSwUlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 7),
    _CfprSwUlanId_Type()
)
cfprSwUlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanId.setStatus("current")
_CfprSwUlanIfRole_Type = CfprFabricVnetEpIfRole
_CfprSwUlanIfRole_Object = MibTableColumn
cfprSwUlanIfRole = _CfprSwUlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 8),
    _CfprSwUlanIfRole_Type()
)
cfprSwUlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanIfRole.setStatus("current")
_CfprSwUlanIfType_Type = CfprNetworkVnetEpIfType
_CfprSwUlanIfType_Object = MibTableColumn
cfprSwUlanIfType = _CfprSwUlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 9),
    _CfprSwUlanIfType_Type()
)
cfprSwUlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanIfType.setStatus("current")
_CfprSwUlanLocale_Type = CfprFabricVnetEpLocale
_CfprSwUlanLocale_Object = MibTableColumn
cfprSwUlanLocale = _CfprSwUlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 10),
    _CfprSwUlanLocale_Type()
)
cfprSwUlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanLocale.setStatus("current")
_CfprSwUlanName_Type = SnmpAdminString
_CfprSwUlanName_Object = MibTableColumn
cfprSwUlanName = _CfprSwUlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 11),
    _CfprSwUlanName_Type()
)
cfprSwUlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanName.setStatus("current")
_CfprSwUlanOperState_Type = CfprFabricVlanOperState
_CfprSwUlanOperState_Object = MibTableColumn
cfprSwUlanOperState = _CfprSwUlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 12),
    _CfprSwUlanOperState_Type()
)
cfprSwUlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanOperState.setStatus("current")
_CfprSwUlanOverlapStateForA_Type = CfprFabricVlanOverlapState
_CfprSwUlanOverlapStateForA_Object = MibTableColumn
cfprSwUlanOverlapStateForA = _CfprSwUlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 13),
    _CfprSwUlanOverlapStateForA_Type()
)
cfprSwUlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanOverlapStateForA.setStatus("current")
_CfprSwUlanOverlapStateForB_Type = CfprFabricVlanOverlapState
_CfprSwUlanOverlapStateForB_Object = MibTableColumn
cfprSwUlanOverlapStateForB = _CfprSwUlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 14),
    _CfprSwUlanOverlapStateForB_Type()
)
cfprSwUlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanOverlapStateForB.setStatus("current")
_CfprSwUlanPeerDn_Type = SnmpAdminString
_CfprSwUlanPeerDn_Object = MibTableColumn
cfprSwUlanPeerDn = _CfprSwUlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 15),
    _CfprSwUlanPeerDn_Type()
)
cfprSwUlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanPeerDn.setStatus("current")
_CfprSwUlanPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprSwUlanPolicyOwner_Object = MibTableColumn
cfprSwUlanPolicyOwner = _CfprSwUlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 16),
    _CfprSwUlanPolicyOwner_Type()
)
cfprSwUlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanPolicyOwner.setStatus("current")
_CfprSwUlanPubNwDn_Type = SnmpAdminString
_CfprSwUlanPubNwDn_Object = MibTableColumn
cfprSwUlanPubNwDn = _CfprSwUlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 17),
    _CfprSwUlanPubNwDn_Type()
)
cfprSwUlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanPubNwDn.setStatus("current")
_CfprSwUlanPubNwId_Type = Gauge32
_CfprSwUlanPubNwId_Object = MibTableColumn
cfprSwUlanPubNwId = _CfprSwUlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 18),
    _CfprSwUlanPubNwId_Type()
)
cfprSwUlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanPubNwId.setStatus("current")
_CfprSwUlanPubNwName_Type = SnmpAdminString
_CfprSwUlanPubNwName_Object = MibTableColumn
cfprSwUlanPubNwName = _CfprSwUlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 19),
    _CfprSwUlanPubNwName_Type()
)
cfprSwUlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanPubNwName.setStatus("current")
_CfprSwUlanPurpose_Type = CfprSwUlanPurpose
_CfprSwUlanPurpose_Object = MibTableColumn
cfprSwUlanPurpose = _CfprSwUlanPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 20),
    _CfprSwUlanPurpose_Type()
)
cfprSwUlanPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanPurpose.setStatus("current")
_CfprSwUlanSharing_Type = CfprFabricAVlanSharing
_CfprSwUlanSharing_Object = MibTableColumn
cfprSwUlanSharing = _CfprSwUlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 21),
    _CfprSwUlanSharing_Type()
)
cfprSwUlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanSharing.setStatus("current")
_CfprSwUlanSwitchId_Type = CfprNetworkSwitchId
_CfprSwUlanSwitchId_Object = MibTableColumn
cfprSwUlanSwitchId = _CfprSwUlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 22),
    _CfprSwUlanSwitchId_Type()
)
cfprSwUlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanSwitchId.setStatus("current")
_CfprSwUlanTransport_Type = CfprFabricAVlanTransport
_CfprSwUlanTransport_Object = MibTableColumn
cfprSwUlanTransport = _CfprSwUlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 23),
    _CfprSwUlanTransport_Type()
)
cfprSwUlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanTransport.setStatus("current")
_CfprSwUlanType_Type = CfprFabricAVlanType
_CfprSwUlanType_Object = MibTableColumn
cfprSwUlanType = _CfprSwUlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 24),
    _CfprSwUlanType_Type()
)
cfprSwUlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanType.setStatus("current")
_CfprSwUlanVlanType_Type = CfprFabricEpVlanVlanType
_CfprSwUlanVlanType_Object = MibTableColumn
cfprSwUlanVlanType = _CfprSwUlanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 74, 1, 25),
    _CfprSwUlanVlanType_Type()
)
cfprSwUlanVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUlanVlanType.setStatus("current")
_CfprSwUtilityDomainTable_Object = MibTable
cfprSwUtilityDomainTable = _CfprSwUtilityDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75)
)
if mibBuilder.loadTexts:
    cfprSwUtilityDomainTable.setStatus("current")
_CfprSwUtilityDomainEntry_Object = MibTableRow
cfprSwUtilityDomainEntry = _CfprSwUtilityDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1)
)
cfprSwUtilityDomainEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwUtilityDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwUtilityDomainEntry.setStatus("current")
_CfprSwUtilityDomainInstanceId_Type = CfprManagedObjectId
_CfprSwUtilityDomainInstanceId_Object = MibTableColumn
cfprSwUtilityDomainInstanceId = _CfprSwUtilityDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 1),
    _CfprSwUtilityDomainInstanceId_Type()
)
cfprSwUtilityDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainInstanceId.setStatus("current")
_CfprSwUtilityDomainDn_Type = CfprManagedObjectDn
_CfprSwUtilityDomainDn_Object = MibTableColumn
cfprSwUtilityDomainDn = _CfprSwUtilityDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 2),
    _CfprSwUtilityDomainDn_Type()
)
cfprSwUtilityDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainDn.setStatus("current")
_CfprSwUtilityDomainRn_Type = SnmpAdminString
_CfprSwUtilityDomainRn_Object = MibTableColumn
cfprSwUtilityDomainRn = _CfprSwUtilityDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 3),
    _CfprSwUtilityDomainRn_Type()
)
cfprSwUtilityDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainRn.setStatus("current")
_CfprSwUtilityDomainFsmDescr_Type = SnmpAdminString
_CfprSwUtilityDomainFsmDescr_Object = MibTableColumn
cfprSwUtilityDomainFsmDescr = _CfprSwUtilityDomainFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 4),
    _CfprSwUtilityDomainFsmDescr_Type()
)
cfprSwUtilityDomainFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmDescr.setStatus("current")
_CfprSwUtilityDomainFsmPrev_Type = SnmpAdminString
_CfprSwUtilityDomainFsmPrev_Object = MibTableColumn
cfprSwUtilityDomainFsmPrev = _CfprSwUtilityDomainFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 5),
    _CfprSwUtilityDomainFsmPrev_Type()
)
cfprSwUtilityDomainFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmPrev.setStatus("current")
_CfprSwUtilityDomainFsmProgr_Type = Gauge32
_CfprSwUtilityDomainFsmProgr_Object = MibTableColumn
cfprSwUtilityDomainFsmProgr = _CfprSwUtilityDomainFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 6),
    _CfprSwUtilityDomainFsmProgr_Type()
)
cfprSwUtilityDomainFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmProgr.setStatus("current")
_CfprSwUtilityDomainFsmRmtInvErrCode_Type = Gauge32
_CfprSwUtilityDomainFsmRmtInvErrCode_Object = MibTableColumn
cfprSwUtilityDomainFsmRmtInvErrCode = _CfprSwUtilityDomainFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 7),
    _CfprSwUtilityDomainFsmRmtInvErrCode_Type()
)
cfprSwUtilityDomainFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmRmtInvErrCode.setStatus("current")
_CfprSwUtilityDomainFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwUtilityDomainFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwUtilityDomainFsmRmtInvErrDescr = _CfprSwUtilityDomainFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 8),
    _CfprSwUtilityDomainFsmRmtInvErrDescr_Type()
)
cfprSwUtilityDomainFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmRmtInvErrDescr.setStatus("current")
_CfprSwUtilityDomainFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwUtilityDomainFsmRmtInvRslt_Object = MibTableColumn
cfprSwUtilityDomainFsmRmtInvRslt = _CfprSwUtilityDomainFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 9),
    _CfprSwUtilityDomainFsmRmtInvRslt_Type()
)
cfprSwUtilityDomainFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmRmtInvRslt.setStatus("current")
_CfprSwUtilityDomainFsmStageDescr_Type = SnmpAdminString
_CfprSwUtilityDomainFsmStageDescr_Object = MibTableColumn
cfprSwUtilityDomainFsmStageDescr = _CfprSwUtilityDomainFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 10),
    _CfprSwUtilityDomainFsmStageDescr_Type()
)
cfprSwUtilityDomainFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageDescr.setStatus("current")
_CfprSwUtilityDomainFsmStamp_Type = DateAndTime
_CfprSwUtilityDomainFsmStamp_Object = MibTableColumn
cfprSwUtilityDomainFsmStamp = _CfprSwUtilityDomainFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 11),
    _CfprSwUtilityDomainFsmStamp_Type()
)
cfprSwUtilityDomainFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStamp.setStatus("current")
_CfprSwUtilityDomainFsmStatus_Type = SnmpAdminString
_CfprSwUtilityDomainFsmStatus_Object = MibTableColumn
cfprSwUtilityDomainFsmStatus = _CfprSwUtilityDomainFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 12),
    _CfprSwUtilityDomainFsmStatus_Type()
)
cfprSwUtilityDomainFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStatus.setStatus("current")
_CfprSwUtilityDomainFsmTry_Type = Gauge32
_CfprSwUtilityDomainFsmTry_Object = MibTableColumn
cfprSwUtilityDomainFsmTry = _CfprSwUtilityDomainFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 13),
    _CfprSwUtilityDomainFsmTry_Type()
)
cfprSwUtilityDomainFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTry.setStatus("current")
_CfprSwUtilityDomainLocale_Type = CfprSwUtilityDomainLocale
_CfprSwUtilityDomainLocale_Object = MibTableColumn
cfprSwUtilityDomainLocale = _CfprSwUtilityDomainLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 14),
    _CfprSwUtilityDomainLocale_Type()
)
cfprSwUtilityDomainLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainLocale.setStatus("current")
_CfprSwUtilityDomainName_Type = SnmpAdminString
_CfprSwUtilityDomainName_Object = MibTableColumn
cfprSwUtilityDomainName = _CfprSwUtilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 15),
    _CfprSwUtilityDomainName_Type()
)
cfprSwUtilityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainName.setStatus("current")
_CfprSwUtilityDomainSwitchId_Type = CfprNetworkSwitchId
_CfprSwUtilityDomainSwitchId_Object = MibTableColumn
cfprSwUtilityDomainSwitchId = _CfprSwUtilityDomainSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 16),
    _CfprSwUtilityDomainSwitchId_Type()
)
cfprSwUtilityDomainSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainSwitchId.setStatus("current")
_CfprSwUtilityDomainTransport_Type = CfprNetworkTransport
_CfprSwUtilityDomainTransport_Object = MibTableColumn
cfprSwUtilityDomainTransport = _CfprSwUtilityDomainTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 17),
    _CfprSwUtilityDomainTransport_Type()
)
cfprSwUtilityDomainTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainTransport.setStatus("current")
_CfprSwUtilityDomainType_Type = CfprSwUtilityDomainType
_CfprSwUtilityDomainType_Object = MibTableColumn
cfprSwUtilityDomainType = _CfprSwUtilityDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 75, 1, 18),
    _CfprSwUtilityDomainType_Type()
)
cfprSwUtilityDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainType.setStatus("current")
_CfprSwUtilityDomainFsmTable_Object = MibTable
cfprSwUtilityDomainFsmTable = _CfprSwUtilityDomainFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76)
)
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTable.setStatus("current")
_CfprSwUtilityDomainFsmEntry_Object = MibTableRow
cfprSwUtilityDomainFsmEntry = _CfprSwUtilityDomainFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1)
)
cfprSwUtilityDomainFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwUtilityDomainFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmEntry.setStatus("current")
_CfprSwUtilityDomainFsmInstanceId_Type = CfprManagedObjectId
_CfprSwUtilityDomainFsmInstanceId_Object = MibTableColumn
cfprSwUtilityDomainFsmInstanceId = _CfprSwUtilityDomainFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 1),
    _CfprSwUtilityDomainFsmInstanceId_Type()
)
cfprSwUtilityDomainFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmInstanceId.setStatus("current")
_CfprSwUtilityDomainFsmDn_Type = CfprManagedObjectDn
_CfprSwUtilityDomainFsmDn_Object = MibTableColumn
cfprSwUtilityDomainFsmDn = _CfprSwUtilityDomainFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 2),
    _CfprSwUtilityDomainFsmDn_Type()
)
cfprSwUtilityDomainFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmDn.setStatus("current")
_CfprSwUtilityDomainFsmRn_Type = SnmpAdminString
_CfprSwUtilityDomainFsmRn_Object = MibTableColumn
cfprSwUtilityDomainFsmRn = _CfprSwUtilityDomainFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 3),
    _CfprSwUtilityDomainFsmRn_Type()
)
cfprSwUtilityDomainFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmRn.setStatus("current")
_CfprSwUtilityDomainFsmCompletionTime_Type = DateAndTime
_CfprSwUtilityDomainFsmCompletionTime_Object = MibTableColumn
cfprSwUtilityDomainFsmCompletionTime = _CfprSwUtilityDomainFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 4),
    _CfprSwUtilityDomainFsmCompletionTime_Type()
)
cfprSwUtilityDomainFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmCompletionTime.setStatus("current")
_CfprSwUtilityDomainFsmCurrentFsm_Type = CfprSwUtilityDomainFsmCurrentFsm
_CfprSwUtilityDomainFsmCurrentFsm_Object = MibTableColumn
cfprSwUtilityDomainFsmCurrentFsm = _CfprSwUtilityDomainFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 5),
    _CfprSwUtilityDomainFsmCurrentFsm_Type()
)
cfprSwUtilityDomainFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmCurrentFsm.setStatus("current")
_CfprSwUtilityDomainFsmDescrData_Type = SnmpAdminString
_CfprSwUtilityDomainFsmDescrData_Object = MibTableColumn
cfprSwUtilityDomainFsmDescrData = _CfprSwUtilityDomainFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 6),
    _CfprSwUtilityDomainFsmDescrData_Type()
)
cfprSwUtilityDomainFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmDescrData.setStatus("current")
_CfprSwUtilityDomainFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwUtilityDomainFsmFsmStatus_Object = MibTableColumn
cfprSwUtilityDomainFsmFsmStatus = _CfprSwUtilityDomainFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 7),
    _CfprSwUtilityDomainFsmFsmStatus_Type()
)
cfprSwUtilityDomainFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmFsmStatus.setStatus("current")
_CfprSwUtilityDomainFsmProgress_Type = Gauge32
_CfprSwUtilityDomainFsmProgress_Object = MibTableColumn
cfprSwUtilityDomainFsmProgress = _CfprSwUtilityDomainFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 8),
    _CfprSwUtilityDomainFsmProgress_Type()
)
cfprSwUtilityDomainFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmProgress.setStatus("current")
_CfprSwUtilityDomainFsmRmtErrCode_Type = Gauge32
_CfprSwUtilityDomainFsmRmtErrCode_Object = MibTableColumn
cfprSwUtilityDomainFsmRmtErrCode = _CfprSwUtilityDomainFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 9),
    _CfprSwUtilityDomainFsmRmtErrCode_Type()
)
cfprSwUtilityDomainFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmRmtErrCode.setStatus("current")
_CfprSwUtilityDomainFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwUtilityDomainFsmRmtErrDescr_Object = MibTableColumn
cfprSwUtilityDomainFsmRmtErrDescr = _CfprSwUtilityDomainFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 10),
    _CfprSwUtilityDomainFsmRmtErrDescr_Type()
)
cfprSwUtilityDomainFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmRmtErrDescr.setStatus("current")
_CfprSwUtilityDomainFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwUtilityDomainFsmRmtRslt_Object = MibTableColumn
cfprSwUtilityDomainFsmRmtRslt = _CfprSwUtilityDomainFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 76, 1, 11),
    _CfprSwUtilityDomainFsmRmtRslt_Type()
)
cfprSwUtilityDomainFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmRmtRslt.setStatus("current")
_CfprSwUtilityDomainFsmStageTable_Object = MibTable
cfprSwUtilityDomainFsmStageTable = _CfprSwUtilityDomainFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77)
)
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageTable.setStatus("current")
_CfprSwUtilityDomainFsmStageEntry_Object = MibTableRow
cfprSwUtilityDomainFsmStageEntry = _CfprSwUtilityDomainFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1)
)
cfprSwUtilityDomainFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwUtilityDomainFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageEntry.setStatus("current")
_CfprSwUtilityDomainFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwUtilityDomainFsmStageInstanceId_Object = MibTableColumn
cfprSwUtilityDomainFsmStageInstanceId = _CfprSwUtilityDomainFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 1),
    _CfprSwUtilityDomainFsmStageInstanceId_Type()
)
cfprSwUtilityDomainFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageInstanceId.setStatus("current")
_CfprSwUtilityDomainFsmStageDn_Type = CfprManagedObjectDn
_CfprSwUtilityDomainFsmStageDn_Object = MibTableColumn
cfprSwUtilityDomainFsmStageDn = _CfprSwUtilityDomainFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 2),
    _CfprSwUtilityDomainFsmStageDn_Type()
)
cfprSwUtilityDomainFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageDn.setStatus("current")
_CfprSwUtilityDomainFsmStageRn_Type = SnmpAdminString
_CfprSwUtilityDomainFsmStageRn_Object = MibTableColumn
cfprSwUtilityDomainFsmStageRn = _CfprSwUtilityDomainFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 3),
    _CfprSwUtilityDomainFsmStageRn_Type()
)
cfprSwUtilityDomainFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageRn.setStatus("current")
_CfprSwUtilityDomainFsmStageDescrData_Type = SnmpAdminString
_CfprSwUtilityDomainFsmStageDescrData_Object = MibTableColumn
cfprSwUtilityDomainFsmStageDescrData = _CfprSwUtilityDomainFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 4),
    _CfprSwUtilityDomainFsmStageDescrData_Type()
)
cfprSwUtilityDomainFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageDescrData.setStatus("current")
_CfprSwUtilityDomainFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwUtilityDomainFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwUtilityDomainFsmStageLastUpdateTime = _CfprSwUtilityDomainFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 5),
    _CfprSwUtilityDomainFsmStageLastUpdateTime_Type()
)
cfprSwUtilityDomainFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageLastUpdateTime.setStatus("current")
_CfprSwUtilityDomainFsmStageName_Type = CfprSwUtilityDomainFsmStageName
_CfprSwUtilityDomainFsmStageName_Object = MibTableColumn
cfprSwUtilityDomainFsmStageName = _CfprSwUtilityDomainFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 6),
    _CfprSwUtilityDomainFsmStageName_Type()
)
cfprSwUtilityDomainFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageName.setStatus("current")
_CfprSwUtilityDomainFsmStageOrder_Type = Gauge32
_CfprSwUtilityDomainFsmStageOrder_Object = MibTableColumn
cfprSwUtilityDomainFsmStageOrder = _CfprSwUtilityDomainFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 7),
    _CfprSwUtilityDomainFsmStageOrder_Type()
)
cfprSwUtilityDomainFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageOrder.setStatus("current")
_CfprSwUtilityDomainFsmStageRetry_Type = Gauge32
_CfprSwUtilityDomainFsmStageRetry_Object = MibTableColumn
cfprSwUtilityDomainFsmStageRetry = _CfprSwUtilityDomainFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 8),
    _CfprSwUtilityDomainFsmStageRetry_Type()
)
cfprSwUtilityDomainFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageRetry.setStatus("current")
_CfprSwUtilityDomainFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwUtilityDomainFsmStageStageStatus_Object = MibTableColumn
cfprSwUtilityDomainFsmStageStageStatus = _CfprSwUtilityDomainFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 77, 1, 9),
    _CfprSwUtilityDomainFsmStageStageStatus_Type()
)
cfprSwUtilityDomainFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmStageStageStatus.setStatus("current")
_CfprSwUtilityDomainFsmTaskTable_Object = MibTable
cfprSwUtilityDomainFsmTaskTable = _CfprSwUtilityDomainFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78)
)
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskTable.setStatus("current")
_CfprSwUtilityDomainFsmTaskEntry_Object = MibTableRow
cfprSwUtilityDomainFsmTaskEntry = _CfprSwUtilityDomainFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78, 1)
)
cfprSwUtilityDomainFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwUtilityDomainFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskEntry.setStatus("current")
_CfprSwUtilityDomainFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwUtilityDomainFsmTaskInstanceId_Object = MibTableColumn
cfprSwUtilityDomainFsmTaskInstanceId = _CfprSwUtilityDomainFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78, 1, 1),
    _CfprSwUtilityDomainFsmTaskInstanceId_Type()
)
cfprSwUtilityDomainFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskInstanceId.setStatus("current")
_CfprSwUtilityDomainFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwUtilityDomainFsmTaskDn_Object = MibTableColumn
cfprSwUtilityDomainFsmTaskDn = _CfprSwUtilityDomainFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78, 1, 2),
    _CfprSwUtilityDomainFsmTaskDn_Type()
)
cfprSwUtilityDomainFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskDn.setStatus("current")
_CfprSwUtilityDomainFsmTaskRn_Type = SnmpAdminString
_CfprSwUtilityDomainFsmTaskRn_Object = MibTableColumn
cfprSwUtilityDomainFsmTaskRn = _CfprSwUtilityDomainFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78, 1, 3),
    _CfprSwUtilityDomainFsmTaskRn_Type()
)
cfprSwUtilityDomainFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskRn.setStatus("current")
_CfprSwUtilityDomainFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwUtilityDomainFsmTaskCompletion_Object = MibTableColumn
cfprSwUtilityDomainFsmTaskCompletion = _CfprSwUtilityDomainFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78, 1, 4),
    _CfprSwUtilityDomainFsmTaskCompletion_Type()
)
cfprSwUtilityDomainFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskCompletion.setStatus("current")
_CfprSwUtilityDomainFsmTaskFlags_Type = CfprFsmFlags
_CfprSwUtilityDomainFsmTaskFlags_Object = MibTableColumn
cfprSwUtilityDomainFsmTaskFlags = _CfprSwUtilityDomainFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78, 1, 5),
    _CfprSwUtilityDomainFsmTaskFlags_Type()
)
cfprSwUtilityDomainFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskFlags.setStatus("current")
_CfprSwUtilityDomainFsmTaskItem_Type = CfprSwUtilityDomainFsmTaskItem
_CfprSwUtilityDomainFsmTaskItem_Object = MibTableColumn
cfprSwUtilityDomainFsmTaskItem = _CfprSwUtilityDomainFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78, 1, 6),
    _CfprSwUtilityDomainFsmTaskItem_Type()
)
cfprSwUtilityDomainFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskItem.setStatus("current")
_CfprSwUtilityDomainFsmTaskSeqId_Type = Gauge32
_CfprSwUtilityDomainFsmTaskSeqId_Object = MibTableColumn
cfprSwUtilityDomainFsmTaskSeqId = _CfprSwUtilityDomainFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 78, 1, 7),
    _CfprSwUtilityDomainFsmTaskSeqId_Type()
)
cfprSwUtilityDomainFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwUtilityDomainFsmTaskSeqId.setStatus("current")
_CfprSwVlanTable_Object = MibTable
cfprSwVlanTable = _CfprSwVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80)
)
if mibBuilder.loadTexts:
    cfprSwVlanTable.setStatus("current")
_CfprSwVlanEntry_Object = MibTableRow
cfprSwVlanEntry = _CfprSwVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1)
)
cfprSwVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwVlanEntry.setStatus("current")
_CfprSwVlanInstanceId_Type = CfprManagedObjectId
_CfprSwVlanInstanceId_Object = MibTableColumn
cfprSwVlanInstanceId = _CfprSwVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 1),
    _CfprSwVlanInstanceId_Type()
)
cfprSwVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwVlanInstanceId.setStatus("current")
_CfprSwVlanDn_Type = CfprManagedObjectDn
_CfprSwVlanDn_Object = MibTableColumn
cfprSwVlanDn = _CfprSwVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 2),
    _CfprSwVlanDn_Type()
)
cfprSwVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanDn.setStatus("current")
_CfprSwVlanRn_Type = SnmpAdminString
_CfprSwVlanRn_Object = MibTableColumn
cfprSwVlanRn = _CfprSwVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 3),
    _CfprSwVlanRn_Type()
)
cfprSwVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanRn.setStatus("current")
_CfprSwVlanAssocPrimaryVlanState_Type = CfprFabricVlanAssocPrimaryVlanState
_CfprSwVlanAssocPrimaryVlanState_Object = MibTableColumn
cfprSwVlanAssocPrimaryVlanState = _CfprSwVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 4),
    _CfprSwVlanAssocPrimaryVlanState_Type()
)
cfprSwVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanAssocPrimaryVlanState.setStatus("current")
_CfprSwVlanAssocPrimaryVlanSwitchId_Type = CfprFabricAVlanAssocPrimaryVlanSwitchId
_CfprSwVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cfprSwVlanAssocPrimaryVlanSwitchId = _CfprSwVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 5),
    _CfprSwVlanAssocPrimaryVlanSwitchId_Type()
)
cfprSwVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CfprSwVlanCompressionType_Type = CfprSwVlanCompType
_CfprSwVlanCompressionType_Object = MibTableColumn
cfprSwVlanCompressionType = _CfprSwVlanCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 6),
    _CfprSwVlanCompressionType_Type()
)
cfprSwVlanCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanCompressionType.setStatus("current")
_CfprSwVlanEpDn_Type = SnmpAdminString
_CfprSwVlanEpDn_Object = MibTableColumn
cfprSwVlanEpDn = _CfprSwVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 7),
    _CfprSwVlanEpDn_Type()
)
cfprSwVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanEpDn.setStatus("current")
_CfprSwVlanId_Type = Gauge32
_CfprSwVlanId_Object = MibTableColumn
cfprSwVlanId = _CfprSwVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 8),
    _CfprSwVlanId_Type()
)
cfprSwVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanId.setStatus("current")
_CfprSwVlanIfRole_Type = CfprFabricVnetEpIfRole
_CfprSwVlanIfRole_Object = MibTableColumn
cfprSwVlanIfRole = _CfprSwVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 9),
    _CfprSwVlanIfRole_Type()
)
cfprSwVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanIfRole.setStatus("current")
_CfprSwVlanIfType_Type = CfprNetworkVnetEpIfType
_CfprSwVlanIfType_Object = MibTableColumn
cfprSwVlanIfType = _CfprSwVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 10),
    _CfprSwVlanIfType_Type()
)
cfprSwVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanIfType.setStatus("current")
_CfprSwVlanLc_Type = CfprSwVlanLc
_CfprSwVlanLc_Object = MibTableColumn
cfprSwVlanLc = _CfprSwVlanLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 11),
    _CfprSwVlanLc_Type()
)
cfprSwVlanLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanLc.setStatus("current")
_CfprSwVlanLocale_Type = CfprFabricVnetEpLocale
_CfprSwVlanLocale_Object = MibTableColumn
cfprSwVlanLocale = _CfprSwVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 12),
    _CfprSwVlanLocale_Type()
)
cfprSwVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanLocale.setStatus("current")
_CfprSwVlanMonTrafDir_Type = CfprFabricTrafficDirection
_CfprSwVlanMonTrafDir_Object = MibTableColumn
cfprSwVlanMonTrafDir = _CfprSwVlanMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 13),
    _CfprSwVlanMonTrafDir_Type()
)
cfprSwVlanMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanMonTrafDir.setStatus("current")
_CfprSwVlanName_Type = SnmpAdminString
_CfprSwVlanName_Object = MibTableColumn
cfprSwVlanName = _CfprSwVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 14),
    _CfprSwVlanName_Type()
)
cfprSwVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanName.setStatus("current")
_CfprSwVlanOperState_Type = CfprFabricVlanOperState
_CfprSwVlanOperState_Object = MibTableColumn
cfprSwVlanOperState = _CfprSwVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 15),
    _CfprSwVlanOperState_Type()
)
cfprSwVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanOperState.setStatus("current")
_CfprSwVlanOverlapStateForA_Type = CfprFabricVlanOverlapState
_CfprSwVlanOverlapStateForA_Object = MibTableColumn
cfprSwVlanOverlapStateForA = _CfprSwVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 16),
    _CfprSwVlanOverlapStateForA_Type()
)
cfprSwVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanOverlapStateForA.setStatus("current")
_CfprSwVlanOverlapStateForB_Type = CfprFabricVlanOverlapState
_CfprSwVlanOverlapStateForB_Object = MibTableColumn
cfprSwVlanOverlapStateForB = _CfprSwVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 17),
    _CfprSwVlanOverlapStateForB_Type()
)
cfprSwVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanOverlapStateForB.setStatus("current")
_CfprSwVlanPeerDn_Type = SnmpAdminString
_CfprSwVlanPeerDn_Object = MibTableColumn
cfprSwVlanPeerDn = _CfprSwVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 18),
    _CfprSwVlanPeerDn_Type()
)
cfprSwVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPeerDn.setStatus("current")
_CfprSwVlanPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprSwVlanPolicyOwner_Object = MibTableColumn
cfprSwVlanPolicyOwner = _CfprSwVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 19),
    _CfprSwVlanPolicyOwner_Type()
)
cfprSwVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPolicyOwner.setStatus("current")
_CfprSwVlanPubNwDn_Type = SnmpAdminString
_CfprSwVlanPubNwDn_Object = MibTableColumn
cfprSwVlanPubNwDn = _CfprSwVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 20),
    _CfprSwVlanPubNwDn_Type()
)
cfprSwVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPubNwDn.setStatus("current")
_CfprSwVlanPubNwId_Type = Gauge32
_CfprSwVlanPubNwId_Object = MibTableColumn
cfprSwVlanPubNwId = _CfprSwVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 21),
    _CfprSwVlanPubNwId_Type()
)
cfprSwVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPubNwId.setStatus("current")
_CfprSwVlanPubNwName_Type = SnmpAdminString
_CfprSwVlanPubNwName_Object = MibTableColumn
cfprSwVlanPubNwName = _CfprSwVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 22),
    _CfprSwVlanPubNwName_Type()
)
cfprSwVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPubNwName.setStatus("current")
_CfprSwVlanQuerierIpAddrs_Type = InetAddressIPv4
_CfprSwVlanQuerierIpAddrs_Object = MibTableColumn
cfprSwVlanQuerierIpAddrs = _CfprSwVlanQuerierIpAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 23),
    _CfprSwVlanQuerierIpAddrs_Type()
)
cfprSwVlanQuerierIpAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanQuerierIpAddrs.setStatus("current")
_CfprSwVlanSecVlanPerPrimaryVlanCount_Type = Gauge32
_CfprSwVlanSecVlanPerPrimaryVlanCount_Object = MibTableColumn
cfprSwVlanSecVlanPerPrimaryVlanCount = _CfprSwVlanSecVlanPerPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 24),
    _CfprSwVlanSecVlanPerPrimaryVlanCount_Type()
)
cfprSwVlanSecVlanPerPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanSecVlanPerPrimaryVlanCount.setStatus("current")
_CfprSwVlanSecVlanPerPrimaryVlanCountStatus_Type = CfprNetworkVlanCountStatus
_CfprSwVlanSecVlanPerPrimaryVlanCountStatus_Object = MibTableColumn
cfprSwVlanSecVlanPerPrimaryVlanCountStatus = _CfprSwVlanSecVlanPerPrimaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 25),
    _CfprSwVlanSecVlanPerPrimaryVlanCountStatus_Type()
)
cfprSwVlanSecVlanPerPrimaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanSecVlanPerPrimaryVlanCountStatus.setStatus("current")
_CfprSwVlanSharing_Type = CfprFabricAVlanSharing
_CfprSwVlanSharing_Object = MibTableColumn
cfprSwVlanSharing = _CfprSwVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 26),
    _CfprSwVlanSharing_Type()
)
cfprSwVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanSharing.setStatus("current")
_CfprSwVlanSnoopingEnabled_Type = TruthValue
_CfprSwVlanSnoopingEnabled_Object = MibTableColumn
cfprSwVlanSnoopingEnabled = _CfprSwVlanSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 27),
    _CfprSwVlanSnoopingEnabled_Type()
)
cfprSwVlanSnoopingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanSnoopingEnabled.setStatus("current")
_CfprSwVlanSwitchId_Type = CfprNetworkSwitchId
_CfprSwVlanSwitchId_Object = MibTableColumn
cfprSwVlanSwitchId = _CfprSwVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 28),
    _CfprSwVlanSwitchId_Type()
)
cfprSwVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanSwitchId.setStatus("current")
_CfprSwVlanTransport_Type = CfprFabricAVlanTransport
_CfprSwVlanTransport_Object = MibTableColumn
cfprSwVlanTransport = _CfprSwVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 29),
    _CfprSwVlanTransport_Type()
)
cfprSwVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanTransport.setStatus("current")
_CfprSwVlanType_Type = CfprFabricAVlanType
_CfprSwVlanType_Object = MibTableColumn
cfprSwVlanType = _CfprSwVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 30),
    _CfprSwVlanType_Type()
)
cfprSwVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanType.setStatus("current")
_CfprSwVlanVlanType_Type = CfprFabricEpVlanVlanType
_CfprSwVlanVlanType_Object = MibTableColumn
cfprSwVlanVlanType = _CfprSwVlanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 80, 1, 31),
    _CfprSwVlanVlanType_Type()
)
cfprSwVlanVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanVlanType.setStatus("current")
_CfprSwVlanGroupTable_Object = MibTable
cfprSwVlanGroupTable = _CfprSwVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81)
)
if mibBuilder.loadTexts:
    cfprSwVlanGroupTable.setStatus("current")
_CfprSwVlanGroupEntry_Object = MibTableRow
cfprSwVlanGroupEntry = _CfprSwVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81, 1)
)
cfprSwVlanGroupEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwVlanGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwVlanGroupEntry.setStatus("current")
_CfprSwVlanGroupInstanceId_Type = CfprManagedObjectId
_CfprSwVlanGroupInstanceId_Object = MibTableColumn
cfprSwVlanGroupInstanceId = _CfprSwVlanGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81, 1, 1),
    _CfprSwVlanGroupInstanceId_Type()
)
cfprSwVlanGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwVlanGroupInstanceId.setStatus("current")
_CfprSwVlanGroupDn_Type = CfprManagedObjectDn
_CfprSwVlanGroupDn_Object = MibTableColumn
cfprSwVlanGroupDn = _CfprSwVlanGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81, 1, 2),
    _CfprSwVlanGroupDn_Type()
)
cfprSwVlanGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanGroupDn.setStatus("current")
_CfprSwVlanGroupRn_Type = SnmpAdminString
_CfprSwVlanGroupRn_Object = MibTableColumn
cfprSwVlanGroupRn = _CfprSwVlanGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81, 1, 3),
    _CfprSwVlanGroupRn_Type()
)
cfprSwVlanGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanGroupRn.setStatus("current")
_CfprSwVlanGroupId_Type = Gauge32
_CfprSwVlanGroupId_Object = MibTableColumn
cfprSwVlanGroupId = _CfprSwVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81, 1, 4),
    _CfprSwVlanGroupId_Type()
)
cfprSwVlanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanGroupId.setStatus("current")
_CfprSwVlanGroupPeerDn_Type = SnmpAdminString
_CfprSwVlanGroupPeerDn_Object = MibTableColumn
cfprSwVlanGroupPeerDn = _CfprSwVlanGroupPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81, 1, 5),
    _CfprSwVlanGroupPeerDn_Type()
)
cfprSwVlanGroupPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanGroupPeerDn.setStatus("current")
_CfprSwVlanGroupSwitchId_Type = CfprNetworkSwitchId
_CfprSwVlanGroupSwitchId_Object = MibTableColumn
cfprSwVlanGroupSwitchId = _CfprSwVlanGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81, 1, 6),
    _CfprSwVlanGroupSwitchId_Type()
)
cfprSwVlanGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanGroupSwitchId.setStatus("current")
_CfprSwVlanGroupType_Type = CfprSwVlanGroupType
_CfprSwVlanGroupType_Object = MibTableColumn
cfprSwVlanGroupType = _CfprSwVlanGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 81, 1, 7),
    _CfprSwVlanGroupType_Type()
)
cfprSwVlanGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanGroupType.setStatus("current")
_CfprSwVlanPortNsTable_Object = MibTable
cfprSwVlanPortNsTable = _CfprSwVlanPortNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82)
)
if mibBuilder.loadTexts:
    cfprSwVlanPortNsTable.setStatus("current")
_CfprSwVlanPortNsEntry_Object = MibTableRow
cfprSwVlanPortNsEntry = _CfprSwVlanPortNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1)
)
cfprSwVlanPortNsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwVlanPortNsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwVlanPortNsEntry.setStatus("current")
_CfprSwVlanPortNsInstanceId_Type = CfprManagedObjectId
_CfprSwVlanPortNsInstanceId_Object = MibTableColumn
cfprSwVlanPortNsInstanceId = _CfprSwVlanPortNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 1),
    _CfprSwVlanPortNsInstanceId_Type()
)
cfprSwVlanPortNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsInstanceId.setStatus("current")
_CfprSwVlanPortNsDn_Type = CfprManagedObjectDn
_CfprSwVlanPortNsDn_Object = MibTableColumn
cfprSwVlanPortNsDn = _CfprSwVlanPortNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 2),
    _CfprSwVlanPortNsDn_Type()
)
cfprSwVlanPortNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsDn.setStatus("current")
_CfprSwVlanPortNsRn_Type = SnmpAdminString
_CfprSwVlanPortNsRn_Object = MibTableColumn
cfprSwVlanPortNsRn = _CfprSwVlanPortNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 3),
    _CfprSwVlanPortNsRn_Type()
)
cfprSwVlanPortNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsRn.setStatus("current")
_CfprSwVlanPortNsAccessVlanPortCount_Type = Gauge32
_CfprSwVlanPortNsAccessVlanPortCount_Object = MibTableColumn
cfprSwVlanPortNsAccessVlanPortCount = _CfprSwVlanPortNsAccessVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 4),
    _CfprSwVlanPortNsAccessVlanPortCount_Type()
)
cfprSwVlanPortNsAccessVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsAccessVlanPortCount.setStatus("current")
_CfprSwVlanPortNsAllocStatus_Type = CfprSwVlanPortNsAllocStatus
_CfprSwVlanPortNsAllocStatus_Object = MibTableColumn
cfprSwVlanPortNsAllocStatus = _CfprSwVlanPortNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 5),
    _CfprSwVlanPortNsAllocStatus_Type()
)
cfprSwVlanPortNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsAllocStatus.setStatus("current")
_CfprSwVlanPortNsBorderVlanPortCount_Type = Gauge32
_CfprSwVlanPortNsBorderVlanPortCount_Object = MibTableColumn
cfprSwVlanPortNsBorderVlanPortCount = _CfprSwVlanPortNsBorderVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 6),
    _CfprSwVlanPortNsBorderVlanPortCount_Type()
)
cfprSwVlanPortNsBorderVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsBorderVlanPortCount.setStatus("current")
_CfprSwVlanPortNsConfigStatus_Type = CfprSwConfigStatus
_CfprSwVlanPortNsConfigStatus_Object = MibTableColumn
cfprSwVlanPortNsConfigStatus = _CfprSwVlanPortNsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 7),
    _CfprSwVlanPortNsConfigStatus_Type()
)
cfprSwVlanPortNsConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsConfigStatus.setStatus("current")
_CfprSwVlanPortNsLimit_Type = Gauge32
_CfprSwVlanPortNsLimit_Object = MibTableColumn
cfprSwVlanPortNsLimit = _CfprSwVlanPortNsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 8),
    _CfprSwVlanPortNsLimit_Type()
)
cfprSwVlanPortNsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsLimit.setStatus("current")
_CfprSwVlanPortNsSwitchId_Type = CfprNetworkSwitchId
_CfprSwVlanPortNsSwitchId_Object = MibTableColumn
cfprSwVlanPortNsSwitchId = _CfprSwVlanPortNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 9),
    _CfprSwVlanPortNsSwitchId_Type()
)
cfprSwVlanPortNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsSwitchId.setStatus("current")
_CfprSwVlanPortNsTotalVlanPortCount_Type = Gauge32
_CfprSwVlanPortNsTotalVlanPortCount_Object = MibTableColumn
cfprSwVlanPortNsTotalVlanPortCount = _CfprSwVlanPortNsTotalVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 10),
    _CfprSwVlanPortNsTotalVlanPortCount_Type()
)
cfprSwVlanPortNsTotalVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsTotalVlanPortCount.setStatus("current")
_CfprSwVlanPortNsVlanCompOffLimit_Type = Gauge32
_CfprSwVlanPortNsVlanCompOffLimit_Object = MibTableColumn
cfprSwVlanPortNsVlanCompOffLimit = _CfprSwVlanPortNsVlanCompOffLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 11),
    _CfprSwVlanPortNsVlanCompOffLimit_Type()
)
cfprSwVlanPortNsVlanCompOffLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsVlanCompOffLimit.setStatus("current")
_CfprSwVlanPortNsVlanCompOnLimit_Type = Gauge32
_CfprSwVlanPortNsVlanCompOnLimit_Object = MibTableColumn
cfprSwVlanPortNsVlanCompOnLimit = _CfprSwVlanPortNsVlanCompOnLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 82, 1, 12),
    _CfprSwVlanPortNsVlanCompOnLimit_Type()
)
cfprSwVlanPortNsVlanCompOnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsVlanCompOnLimit.setStatus("current")
_CfprSwVlanPortNsOverrideTable_Object = MibTable
cfprSwVlanPortNsOverrideTable = _CfprSwVlanPortNsOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 83)
)
if mibBuilder.loadTexts:
    cfprSwVlanPortNsOverrideTable.setStatus("current")
_CfprSwVlanPortNsOverrideEntry_Object = MibTableRow
cfprSwVlanPortNsOverrideEntry = _CfprSwVlanPortNsOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 83, 1)
)
cfprSwVlanPortNsOverrideEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwVlanPortNsOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwVlanPortNsOverrideEntry.setStatus("current")
_CfprSwVlanPortNsOverrideInstanceId_Type = CfprManagedObjectId
_CfprSwVlanPortNsOverrideInstanceId_Object = MibTableColumn
cfprSwVlanPortNsOverrideInstanceId = _CfprSwVlanPortNsOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 83, 1, 1),
    _CfprSwVlanPortNsOverrideInstanceId_Type()
)
cfprSwVlanPortNsOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsOverrideInstanceId.setStatus("current")
_CfprSwVlanPortNsOverrideDn_Type = CfprManagedObjectDn
_CfprSwVlanPortNsOverrideDn_Object = MibTableColumn
cfprSwVlanPortNsOverrideDn = _CfprSwVlanPortNsOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 83, 1, 2),
    _CfprSwVlanPortNsOverrideDn_Type()
)
cfprSwVlanPortNsOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsOverrideDn.setStatus("current")
_CfprSwVlanPortNsOverrideRn_Type = SnmpAdminString
_CfprSwVlanPortNsOverrideRn_Object = MibTableColumn
cfprSwVlanPortNsOverrideRn = _CfprSwVlanPortNsOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 83, 1, 3),
    _CfprSwVlanPortNsOverrideRn_Type()
)
cfprSwVlanPortNsOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsOverrideRn.setStatus("current")
_CfprSwVlanPortNsOverrideLimit_Type = Gauge32
_CfprSwVlanPortNsOverrideLimit_Object = MibTableColumn
cfprSwVlanPortNsOverrideLimit = _CfprSwVlanPortNsOverrideLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 83, 1, 4),
    _CfprSwVlanPortNsOverrideLimit_Type()
)
cfprSwVlanPortNsOverrideLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanPortNsOverrideLimit.setStatus("current")
_CfprSwVlanRefTable_Object = MibTable
cfprSwVlanRefTable = _CfprSwVlanRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84)
)
if mibBuilder.loadTexts:
    cfprSwVlanRefTable.setStatus("current")
_CfprSwVlanRefEntry_Object = MibTableRow
cfprSwVlanRefEntry = _CfprSwVlanRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84, 1)
)
cfprSwVlanRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwVlanRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwVlanRefEntry.setStatus("current")
_CfprSwVlanRefInstanceId_Type = CfprManagedObjectId
_CfprSwVlanRefInstanceId_Object = MibTableColumn
cfprSwVlanRefInstanceId = _CfprSwVlanRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84, 1, 1),
    _CfprSwVlanRefInstanceId_Type()
)
cfprSwVlanRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwVlanRefInstanceId.setStatus("current")
_CfprSwVlanRefDn_Type = CfprManagedObjectDn
_CfprSwVlanRefDn_Object = MibTableColumn
cfprSwVlanRefDn = _CfprSwVlanRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84, 1, 2),
    _CfprSwVlanRefDn_Type()
)
cfprSwVlanRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanRefDn.setStatus("current")
_CfprSwVlanRefRn_Type = SnmpAdminString
_CfprSwVlanRefRn_Object = MibTableColumn
cfprSwVlanRefRn = _CfprSwVlanRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84, 1, 3),
    _CfprSwVlanRefRn_Type()
)
cfprSwVlanRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanRefRn.setStatus("current")
_CfprSwVlanRefCompressionType_Type = CfprSwVlanCompType
_CfprSwVlanRefCompressionType_Object = MibTableColumn
cfprSwVlanRefCompressionType = _CfprSwVlanRefCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84, 1, 4),
    _CfprSwVlanRefCompressionType_Type()
)
cfprSwVlanRefCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanRefCompressionType.setStatus("current")
_CfprSwVlanRefConfigStatus_Type = CfprSwVlanConfigStatusType
_CfprSwVlanRefConfigStatus_Object = MibTableColumn
cfprSwVlanRefConfigStatus = _CfprSwVlanRefConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84, 1, 5),
    _CfprSwVlanRefConfigStatus_Type()
)
cfprSwVlanRefConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanRefConfigStatus.setStatus("current")
_CfprSwVlanRefId_Type = Gauge32
_CfprSwVlanRefId_Object = MibTableColumn
cfprSwVlanRefId = _CfprSwVlanRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84, 1, 6),
    _CfprSwVlanRefId_Type()
)
cfprSwVlanRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanRefId.setStatus("current")
_CfprSwVlanRefPeerDn_Type = SnmpAdminString
_CfprSwVlanRefPeerDn_Object = MibTableColumn
cfprSwVlanRefPeerDn = _CfprSwVlanRefPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 84, 1, 7),
    _CfprSwVlanRefPeerDn_Type()
)
cfprSwVlanRefPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVlanRefPeerDn.setStatus("current")
_CfprSwVsanTable_Object = MibTable
cfprSwVsanTable = _CfprSwVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85)
)
if mibBuilder.loadTexts:
    cfprSwVsanTable.setStatus("current")
_CfprSwVsanEntry_Object = MibTableRow
cfprSwVsanEntry = _CfprSwVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1)
)
cfprSwVsanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwVsanEntry.setStatus("current")
_CfprSwVsanInstanceId_Type = CfprManagedObjectId
_CfprSwVsanInstanceId_Object = MibTableColumn
cfprSwVsanInstanceId = _CfprSwVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 1),
    _CfprSwVsanInstanceId_Type()
)
cfprSwVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwVsanInstanceId.setStatus("current")
_CfprSwVsanDn_Type = CfprManagedObjectDn
_CfprSwVsanDn_Object = MibTableColumn
cfprSwVsanDn = _CfprSwVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 2),
    _CfprSwVsanDn_Type()
)
cfprSwVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanDn.setStatus("current")
_CfprSwVsanRn_Type = SnmpAdminString
_CfprSwVsanRn_Object = MibTableColumn
cfprSwVsanRn = _CfprSwVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 3),
    _CfprSwVsanRn_Type()
)
cfprSwVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanRn.setStatus("current")
_CfprSwVsanDefaultZoning_Type = CfprFabricDefaultZoningState
_CfprSwVsanDefaultZoning_Object = MibTableColumn
cfprSwVsanDefaultZoning = _CfprSwVsanDefaultZoning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 4),
    _CfprSwVsanDefaultZoning_Type()
)
cfprSwVsanDefaultZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanDefaultZoning.setStatus("current")
_CfprSwVsanEpDn_Type = SnmpAdminString
_CfprSwVsanEpDn_Object = MibTableColumn
cfprSwVsanEpDn = _CfprSwVsanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 5),
    _CfprSwVsanEpDn_Type()
)
cfprSwVsanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanEpDn.setStatus("current")
_CfprSwVsanFcZoneSharingMode_Type = CfprFabricFcZoneSharingMode
_CfprSwVsanFcZoneSharingMode_Object = MibTableColumn
cfprSwVsanFcZoneSharingMode = _CfprSwVsanFcZoneSharingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 6),
    _CfprSwVsanFcZoneSharingMode_Type()
)
cfprSwVsanFcZoneSharingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanFcZoneSharingMode.setStatus("current")
_CfprSwVsanFcoeVlan_Type = Gauge32
_CfprSwVsanFcoeVlan_Object = MibTableColumn
cfprSwVsanFcoeVlan = _CfprSwVsanFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 7),
    _CfprSwVsanFcoeVlan_Type()
)
cfprSwVsanFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanFcoeVlan.setStatus("current")
_CfprSwVsanFltAggr_Type = Unsigned64
_CfprSwVsanFltAggr_Object = MibTableColumn
cfprSwVsanFltAggr = _CfprSwVsanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 8),
    _CfprSwVsanFltAggr_Type()
)
cfprSwVsanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanFltAggr.setStatus("current")
_CfprSwVsanId_Type = Gauge32
_CfprSwVsanId_Object = MibTableColumn
cfprSwVsanId = _CfprSwVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 9),
    _CfprSwVsanId_Type()
)
cfprSwVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanId.setStatus("current")
_CfprSwVsanIfRole_Type = CfprFabricVnetEpIfRole
_CfprSwVsanIfRole_Object = MibTableColumn
cfprSwVsanIfRole = _CfprSwVsanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 10),
    _CfprSwVsanIfRole_Type()
)
cfprSwVsanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanIfRole.setStatus("current")
_CfprSwVsanIfType_Type = CfprNetworkVnetEpIfType
_CfprSwVsanIfType_Object = MibTableColumn
cfprSwVsanIfType = _CfprSwVsanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 11),
    _CfprSwVsanIfType_Type()
)
cfprSwVsanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanIfType.setStatus("current")
_CfprSwVsanLc_Type = CfprFsmLifecycle
_CfprSwVsanLc_Object = MibTableColumn
cfprSwVsanLc = _CfprSwVsanLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 12),
    _CfprSwVsanLc_Type()
)
cfprSwVsanLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanLc.setStatus("current")
_CfprSwVsanLocale_Type = CfprFabricVnetEpLocale
_CfprSwVsanLocale_Object = MibTableColumn
cfprSwVsanLocale = _CfprSwVsanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 13),
    _CfprSwVsanLocale_Type()
)
cfprSwVsanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanLocale.setStatus("current")
_CfprSwVsanMonTrafDir_Type = CfprFabricTrafficDirection
_CfprSwVsanMonTrafDir_Object = MibTableColumn
cfprSwVsanMonTrafDir = _CfprSwVsanMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 14),
    _CfprSwVsanMonTrafDir_Type()
)
cfprSwVsanMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanMonTrafDir.setStatus("current")
_CfprSwVsanName_Type = SnmpAdminString
_CfprSwVsanName_Object = MibTableColumn
cfprSwVsanName = _CfprSwVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 15),
    _CfprSwVsanName_Type()
)
cfprSwVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanName.setStatus("current")
_CfprSwVsanOperState_Type = CfprFabricVsanOperState
_CfprSwVsanOperState_Object = MibTableColumn
cfprSwVsanOperState = _CfprSwVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 16),
    _CfprSwVsanOperState_Type()
)
cfprSwVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanOperState.setStatus("current")
_CfprSwVsanPeerDn_Type = SnmpAdminString
_CfprSwVsanPeerDn_Object = MibTableColumn
cfprSwVsanPeerDn = _CfprSwVsanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 17),
    _CfprSwVsanPeerDn_Type()
)
cfprSwVsanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanPeerDn.setStatus("current")
_CfprSwVsanPolicyOwner_Type = CfprFabricVnetEpPolicyOwner
_CfprSwVsanPolicyOwner_Object = MibTableColumn
cfprSwVsanPolicyOwner = _CfprSwVsanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 18),
    _CfprSwVsanPolicyOwner_Type()
)
cfprSwVsanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanPolicyOwner.setStatus("current")
_CfprSwVsanSwitchId_Type = CfprNetworkSwitchId
_CfprSwVsanSwitchId_Object = MibTableColumn
cfprSwVsanSwitchId = _CfprSwVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 19),
    _CfprSwVsanSwitchId_Type()
)
cfprSwVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanSwitchId.setStatus("current")
_CfprSwVsanTransport_Type = CfprFabricAVsanTransport
_CfprSwVsanTransport_Object = MibTableColumn
cfprSwVsanTransport = _CfprSwVsanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 20),
    _CfprSwVsanTransport_Type()
)
cfprSwVsanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanTransport.setStatus("current")
_CfprSwVsanType_Type = CfprFabricAVsanType
_CfprSwVsanType_Object = MibTableColumn
cfprSwVsanType = _CfprSwVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 21),
    _CfprSwVsanType_Type()
)
cfprSwVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanType.setStatus("current")
_CfprSwVsanZoningState_Type = CfprFabricZoningState
_CfprSwVsanZoningState_Object = MibTableColumn
cfprSwVsanZoningState = _CfprSwVsanZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 85, 1, 22),
    _CfprSwVsanZoningState_Type()
)
cfprSwVsanZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwVsanZoningState.setStatus("current")
_CfprSwZoneInitiatorMemberTable_Object = MibTable
cfprSwZoneInitiatorMemberTable = _CfprSwZoneInitiatorMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86)
)
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberTable.setStatus("current")
_CfprSwZoneInitiatorMemberEntry_Object = MibTableRow
cfprSwZoneInitiatorMemberEntry = _CfprSwZoneInitiatorMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1)
)
cfprSwZoneInitiatorMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwZoneInitiatorMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberEntry.setStatus("current")
_CfprSwZoneInitiatorMemberInstanceId_Type = CfprManagedObjectId
_CfprSwZoneInitiatorMemberInstanceId_Object = MibTableColumn
cfprSwZoneInitiatorMemberInstanceId = _CfprSwZoneInitiatorMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1, 1),
    _CfprSwZoneInitiatorMemberInstanceId_Type()
)
cfprSwZoneInitiatorMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberInstanceId.setStatus("current")
_CfprSwZoneInitiatorMemberDn_Type = CfprManagedObjectDn
_CfprSwZoneInitiatorMemberDn_Object = MibTableColumn
cfprSwZoneInitiatorMemberDn = _CfprSwZoneInitiatorMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1, 2),
    _CfprSwZoneInitiatorMemberDn_Type()
)
cfprSwZoneInitiatorMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberDn.setStatus("current")
_CfprSwZoneInitiatorMemberRn_Type = SnmpAdminString
_CfprSwZoneInitiatorMemberRn_Object = MibTableColumn
cfprSwZoneInitiatorMemberRn = _CfprSwZoneInitiatorMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1, 3),
    _CfprSwZoneInitiatorMemberRn_Type()
)
cfprSwZoneInitiatorMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberRn.setStatus("current")
_CfprSwZoneInitiatorMemberEpDn_Type = SnmpAdminString
_CfprSwZoneInitiatorMemberEpDn_Object = MibTableColumn
cfprSwZoneInitiatorMemberEpDn = _CfprSwZoneInitiatorMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1, 4),
    _CfprSwZoneInitiatorMemberEpDn_Type()
)
cfprSwZoneInitiatorMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberEpDn.setStatus("current")
_CfprSwZoneInitiatorMemberLc_Type = CfprSwFcZoneMemberLc
_CfprSwZoneInitiatorMemberLc_Object = MibTableColumn
cfprSwZoneInitiatorMemberLc = _CfprSwZoneInitiatorMemberLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1, 5),
    _CfprSwZoneInitiatorMemberLc_Type()
)
cfprSwZoneInitiatorMemberLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberLc.setStatus("current")
_CfprSwZoneInitiatorMemberName_Type = SnmpAdminString
_CfprSwZoneInitiatorMemberName_Object = MibTableColumn
cfprSwZoneInitiatorMemberName = _CfprSwZoneInitiatorMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1, 6),
    _CfprSwZoneInitiatorMemberName_Type()
)
cfprSwZoneInitiatorMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberName.setStatus("current")
_CfprSwZoneInitiatorMemberPeerDn_Type = SnmpAdminString
_CfprSwZoneInitiatorMemberPeerDn_Object = MibTableColumn
cfprSwZoneInitiatorMemberPeerDn = _CfprSwZoneInitiatorMemberPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1, 7),
    _CfprSwZoneInitiatorMemberPeerDn_Type()
)
cfprSwZoneInitiatorMemberPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberPeerDn.setStatus("current")
_CfprSwZoneInitiatorMemberWwpn_Type = Unsigned64
_CfprSwZoneInitiatorMemberWwpn_Object = MibTableColumn
cfprSwZoneInitiatorMemberWwpn = _CfprSwZoneInitiatorMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 86, 1, 8),
    _CfprSwZoneInitiatorMemberWwpn_Type()
)
cfprSwZoneInitiatorMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneInitiatorMemberWwpn.setStatus("current")
_CfprSwZoneTargetMemberTable_Object = MibTable
cfprSwZoneTargetMemberTable = _CfprSwZoneTargetMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87)
)
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberTable.setStatus("current")
_CfprSwZoneTargetMemberEntry_Object = MibTableRow
cfprSwZoneTargetMemberEntry = _CfprSwZoneTargetMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1)
)
cfprSwZoneTargetMemberEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwZoneTargetMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberEntry.setStatus("current")
_CfprSwZoneTargetMemberInstanceId_Type = CfprManagedObjectId
_CfprSwZoneTargetMemberInstanceId_Object = MibTableColumn
cfprSwZoneTargetMemberInstanceId = _CfprSwZoneTargetMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1, 1),
    _CfprSwZoneTargetMemberInstanceId_Type()
)
cfprSwZoneTargetMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberInstanceId.setStatus("current")
_CfprSwZoneTargetMemberDn_Type = CfprManagedObjectDn
_CfprSwZoneTargetMemberDn_Object = MibTableColumn
cfprSwZoneTargetMemberDn = _CfprSwZoneTargetMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1, 2),
    _CfprSwZoneTargetMemberDn_Type()
)
cfprSwZoneTargetMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberDn.setStatus("current")
_CfprSwZoneTargetMemberRn_Type = SnmpAdminString
_CfprSwZoneTargetMemberRn_Object = MibTableColumn
cfprSwZoneTargetMemberRn = _CfprSwZoneTargetMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1, 3),
    _CfprSwZoneTargetMemberRn_Type()
)
cfprSwZoneTargetMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberRn.setStatus("current")
_CfprSwZoneTargetMemberEpDn_Type = SnmpAdminString
_CfprSwZoneTargetMemberEpDn_Object = MibTableColumn
cfprSwZoneTargetMemberEpDn = _CfprSwZoneTargetMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1, 4),
    _CfprSwZoneTargetMemberEpDn_Type()
)
cfprSwZoneTargetMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberEpDn.setStatus("current")
_CfprSwZoneTargetMemberLc_Type = CfprSwFcZoneMemberLc
_CfprSwZoneTargetMemberLc_Object = MibTableColumn
cfprSwZoneTargetMemberLc = _CfprSwZoneTargetMemberLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1, 5),
    _CfprSwZoneTargetMemberLc_Type()
)
cfprSwZoneTargetMemberLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberLc.setStatus("current")
_CfprSwZoneTargetMemberName_Type = SnmpAdminString
_CfprSwZoneTargetMemberName_Object = MibTableColumn
cfprSwZoneTargetMemberName = _CfprSwZoneTargetMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1, 6),
    _CfprSwZoneTargetMemberName_Type()
)
cfprSwZoneTargetMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberName.setStatus("current")
_CfprSwZoneTargetMemberPeerDn_Type = SnmpAdminString
_CfprSwZoneTargetMemberPeerDn_Object = MibTableColumn
cfprSwZoneTargetMemberPeerDn = _CfprSwZoneTargetMemberPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1, 7),
    _CfprSwZoneTargetMemberPeerDn_Type()
)
cfprSwZoneTargetMemberPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberPeerDn.setStatus("current")
_CfprSwZoneTargetMemberWwpn_Type = Unsigned64
_CfprSwZoneTargetMemberWwpn_Object = MibTableColumn
cfprSwZoneTargetMemberWwpn = _CfprSwZoneTargetMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 87, 1, 8),
    _CfprSwZoneTargetMemberWwpn_Type()
)
cfprSwZoneTargetMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwZoneTargetMemberWwpn.setStatus("current")
_CfprSwSspEthLanMonTable_Object = MibTable
cfprSwSspEthLanMonTable = _CfprSwSspEthLanMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88)
)
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonTable.setStatus("current")
_CfprSwSspEthLanMonEntry_Object = MibTableRow
cfprSwSspEthLanMonEntry = _CfprSwSspEthLanMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1)
)
cfprSwSspEthLanMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthLanMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonEntry.setStatus("current")
_CfprSwSspEthLanMonInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthLanMonInstanceId_Object = MibTableColumn
cfprSwSspEthLanMonInstanceId = _CfprSwSspEthLanMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1, 1),
    _CfprSwSspEthLanMonInstanceId_Type()
)
cfprSwSspEthLanMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonInstanceId.setStatus("current")
_CfprSwSspEthLanMonDn_Type = CfprManagedObjectDn
_CfprSwSspEthLanMonDn_Object = MibTableColumn
cfprSwSspEthLanMonDn = _CfprSwSspEthLanMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1, 2),
    _CfprSwSspEthLanMonDn_Type()
)
cfprSwSspEthLanMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonDn.setStatus("current")
_CfprSwSspEthLanMonRn_Type = SnmpAdminString
_CfprSwSspEthLanMonRn_Object = MibTableColumn
cfprSwSspEthLanMonRn = _CfprSwSspEthLanMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1, 3),
    _CfprSwSspEthLanMonRn_Type()
)
cfprSwSspEthLanMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonRn.setStatus("current")
_CfprSwSspEthLanMonLocale_Type = CfprSwSspMonDomainLocale
_CfprSwSspEthLanMonLocale_Object = MibTableColumn
cfprSwSspEthLanMonLocale = _CfprSwSspEthLanMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1, 4),
    _CfprSwSspEthLanMonLocale_Type()
)
cfprSwSspEthLanMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonLocale.setStatus("current")
_CfprSwSspEthLanMonName_Type = SnmpAdminString
_CfprSwSspEthLanMonName_Object = MibTableColumn
cfprSwSspEthLanMonName = _CfprSwSspEthLanMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1, 5),
    _CfprSwSspEthLanMonName_Type()
)
cfprSwSspEthLanMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonName.setStatus("current")
_CfprSwSspEthLanMonSwitchId_Type = CfprNetworkSwitchId
_CfprSwSspEthLanMonSwitchId_Object = MibTableColumn
cfprSwSspEthLanMonSwitchId = _CfprSwSspEthLanMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1, 6),
    _CfprSwSspEthLanMonSwitchId_Type()
)
cfprSwSspEthLanMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonSwitchId.setStatus("current")
_CfprSwSspEthLanMonTransport_Type = CfprSwSspEthLanMonTransport
_CfprSwSspEthLanMonTransport_Object = MibTableColumn
cfprSwSspEthLanMonTransport = _CfprSwSspEthLanMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1, 7),
    _CfprSwSspEthLanMonTransport_Type()
)
cfprSwSspEthLanMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonTransport.setStatus("current")
_CfprSwSspEthLanMonType_Type = CfprSwSspLanMonType
_CfprSwSspEthLanMonType_Object = MibTableColumn
cfprSwSspEthLanMonType = _CfprSwSspEthLanMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 88, 1, 8),
    _CfprSwSspEthLanMonType_Type()
)
cfprSwSspEthLanMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthLanMonType.setStatus("current")
_CfprSwSspEthMonTable_Object = MibTable
cfprSwSspEthMonTable = _CfprSwSspEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonTable.setStatus("current")
_CfprSwSspEthMonEntry_Object = MibTableRow
cfprSwSspEthMonEntry = _CfprSwSspEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1)
)
cfprSwSspEthMonEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonEntry.setStatus("current")
_CfprSwSspEthMonInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonInstanceId_Object = MibTableColumn
cfprSwSspEthMonInstanceId = _CfprSwSspEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 1),
    _CfprSwSspEthMonInstanceId_Type()
)
cfprSwSspEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonInstanceId.setStatus("current")
_CfprSwSspEthMonDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonDn_Object = MibTableColumn
cfprSwSspEthMonDn = _CfprSwSspEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 2),
    _CfprSwSspEthMonDn_Type()
)
cfprSwSspEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonDn.setStatus("current")
_CfprSwSspEthMonRn_Type = SnmpAdminString
_CfprSwSspEthMonRn_Object = MibTableColumn
cfprSwSspEthMonRn = _CfprSwSspEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 3),
    _CfprSwSspEthMonRn_Type()
)
cfprSwSspEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonRn.setStatus("current")
_CfprSwSspEthMonAdminState_Type = CfprSwSspMonAdminState
_CfprSwSspEthMonAdminState_Object = MibTableColumn
cfprSwSspEthMonAdminState = _CfprSwSspEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 4),
    _CfprSwSspEthMonAdminState_Type()
)
cfprSwSspEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonAdminState.setStatus("current")
_CfprSwSspEthMonAppendFlag_Type = CfprFabricPktCaptureAppendFlag
_CfprSwSspEthMonAppendFlag_Object = MibTableColumn
cfprSwSspEthMonAppendFlag = _CfprSwSspEthMonAppendFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 5),
    _CfprSwSspEthMonAppendFlag_Type()
)
cfprSwSspEthMonAppendFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonAppendFlag.setStatus("current")
_CfprSwSspEthMonDelPcap_Type = CfprSwSspMonDelPcap
_CfprSwSspEthMonDelPcap_Object = MibTableColumn
cfprSwSspEthMonDelPcap = _CfprSwSspEthMonDelPcap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 6),
    _CfprSwSspEthMonDelPcap_Type()
)
cfprSwSspEthMonDelPcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonDelPcap.setStatus("current")
_CfprSwSspEthMonFsmDescr_Type = SnmpAdminString
_CfprSwSspEthMonFsmDescr_Object = MibTableColumn
cfprSwSspEthMonFsmDescr = _CfprSwSspEthMonFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 7),
    _CfprSwSspEthMonFsmDescr_Type()
)
cfprSwSspEthMonFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmDescr.setStatus("current")
_CfprSwSspEthMonFsmPrev_Type = SnmpAdminString
_CfprSwSspEthMonFsmPrev_Object = MibTableColumn
cfprSwSspEthMonFsmPrev = _CfprSwSspEthMonFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 8),
    _CfprSwSspEthMonFsmPrev_Type()
)
cfprSwSspEthMonFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmPrev.setStatus("current")
_CfprSwSspEthMonFsmProgr_Type = Gauge32
_CfprSwSspEthMonFsmProgr_Object = MibTableColumn
cfprSwSspEthMonFsmProgr = _CfprSwSspEthMonFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 9),
    _CfprSwSspEthMonFsmProgr_Type()
)
cfprSwSspEthMonFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmProgr.setStatus("current")
_CfprSwSspEthMonFsmRmtInvErrCode_Type = Gauge32
_CfprSwSspEthMonFsmRmtInvErrCode_Object = MibTableColumn
cfprSwSspEthMonFsmRmtInvErrCode = _CfprSwSspEthMonFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 10),
    _CfprSwSspEthMonFsmRmtInvErrCode_Type()
)
cfprSwSspEthMonFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmRmtInvErrCode.setStatus("current")
_CfprSwSspEthMonFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwSspEthMonFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwSspEthMonFsmRmtInvErrDescr = _CfprSwSspEthMonFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 11),
    _CfprSwSspEthMonFsmRmtInvErrDescr_Type()
)
cfprSwSspEthMonFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmRmtInvErrDescr.setStatus("current")
_CfprSwSspEthMonFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwSspEthMonFsmRmtInvRslt_Object = MibTableColumn
cfprSwSspEthMonFsmRmtInvRslt = _CfprSwSspEthMonFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 12),
    _CfprSwSspEthMonFsmRmtInvRslt_Type()
)
cfprSwSspEthMonFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmRmtInvRslt.setStatus("current")
_CfprSwSspEthMonFsmStageDescr_Type = SnmpAdminString
_CfprSwSspEthMonFsmStageDescr_Object = MibTableColumn
cfprSwSspEthMonFsmStageDescr = _CfprSwSspEthMonFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 13),
    _CfprSwSspEthMonFsmStageDescr_Type()
)
cfprSwSspEthMonFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageDescr.setStatus("current")
_CfprSwSspEthMonFsmStamp_Type = DateAndTime
_CfprSwSspEthMonFsmStamp_Object = MibTableColumn
cfprSwSspEthMonFsmStamp = _CfprSwSspEthMonFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 14),
    _CfprSwSspEthMonFsmStamp_Type()
)
cfprSwSspEthMonFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStamp.setStatus("current")
_CfprSwSspEthMonFsmStatus_Type = SnmpAdminString
_CfprSwSspEthMonFsmStatus_Object = MibTableColumn
cfprSwSspEthMonFsmStatus = _CfprSwSspEthMonFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 15),
    _CfprSwSspEthMonFsmStatus_Type()
)
cfprSwSspEthMonFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStatus.setStatus("current")
_CfprSwSspEthMonFsmTry_Type = Gauge32
_CfprSwSspEthMonFsmTry_Object = MibTableColumn
cfprSwSspEthMonFsmTry = _CfprSwSspEthMonFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 16),
    _CfprSwSspEthMonFsmTry_Type()
)
cfprSwSspEthMonFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTry.setStatus("current")
_CfprSwSspEthMonLifeCycle_Type = CfprSwPktCaptureLifeCycle
_CfprSwSspEthMonLifeCycle_Object = MibTableColumn
cfprSwSspEthMonLifeCycle = _CfprSwSspEthMonLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 17),
    _CfprSwSspEthMonLifeCycle_Type()
)
cfprSwSspEthMonLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonLifeCycle.setStatus("current")
_CfprSwSspEthMonName_Type = SnmpAdminString
_CfprSwSspEthMonName_Object = MibTableColumn
cfprSwSspEthMonName = _CfprSwSspEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 18),
    _CfprSwSspEthMonName_Type()
)
cfprSwSspEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonName.setStatus("current")
_CfprSwSspEthMonPeerDn_Type = SnmpAdminString
_CfprSwSspEthMonPeerDn_Object = MibTableColumn
cfprSwSspEthMonPeerDn = _CfprSwSspEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 19),
    _CfprSwSspEthMonPeerDn_Type()
)
cfprSwSspEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonPeerDn.setStatus("current")
_CfprSwSspEthMonSession_Type = Gauge32
_CfprSwSspEthMonSession_Object = MibTableColumn
cfprSwSspEthMonSession = _CfprSwSspEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 20),
    _CfprSwSspEthMonSession_Type()
)
cfprSwSspEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSession.setStatus("current")
_CfprSwSspEthMonSessionMemUsage_Type = Unsigned64
_CfprSwSspEthMonSessionMemUsage_Object = MibTableColumn
cfprSwSspEthMonSessionMemUsage = _CfprSwSspEthMonSessionMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 21),
    _CfprSwSspEthMonSessionMemUsage_Type()
)
cfprSwSspEthMonSessionMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSessionMemUsage.setStatus("current")
_CfprSwSspEthMonSwitchId_Type = CfprNetworkSwitchId
_CfprSwSspEthMonSwitchId_Object = MibTableColumn
cfprSwSspEthMonSwitchId = _CfprSwSspEthMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 22),
    _CfprSwSspEthMonSwitchId_Type()
)
cfprSwSspEthMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSwitchId.setStatus("current")
_CfprSwSspEthMonTransport_Type = CfprSwSspEthMonTransport
_CfprSwSspEthMonTransport_Object = MibTableColumn
cfprSwSspEthMonTransport = _CfprSwSspEthMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 23),
    _CfprSwSspEthMonTransport_Type()
)
cfprSwSspEthMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonTransport.setStatus("current")
_CfprSwSspEthMonType_Type = CfprSwSspEthMonType
_CfprSwSspEthMonType_Object = MibTableColumn
cfprSwSspEthMonType = _CfprSwSspEthMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 24),
    _CfprSwSspEthMonType_Type()
)
cfprSwSspEthMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonType.setStatus("current")
_CfprSwSspEthMonSessionPcapSnapLen_Type = Gauge32
_CfprSwSspEthMonSessionPcapSnapLen_Object = MibTableColumn
cfprSwSspEthMonSessionPcapSnapLen = _CfprSwSspEthMonSessionPcapSnapLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 25),
    _CfprSwSspEthMonSessionPcapSnapLen_Type()
)
cfprSwSspEthMonSessionPcapSnapLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSessionPcapSnapLen.setStatus("current")
_CfprSwSspEthMonFsmFlags_Type = SnmpAdminString
_CfprSwSspEthMonFsmFlags_Object = MibTableColumn
cfprSwSspEthMonFsmFlags = _CfprSwSspEthMonFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 89, 1, 26),
    _CfprSwSspEthMonFsmFlags_Type()
)
cfprSwSspEthMonFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmFlags.setStatus("current")
_CfprSwSspEthMonFilterEpTable_Object = MibTable
cfprSwSspEthMonFilterEpTable = _CfprSwSspEthMonFilterEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpTable.setStatus("current")
_CfprSwSspEthMonFilterEpEntry_Object = MibTableRow
cfprSwSspEthMonFilterEpEntry = _CfprSwSspEthMonFilterEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1)
)
cfprSwSspEthMonFilterEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonFilterEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpEntry.setStatus("current")
_CfprSwSspEthMonFilterEpInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonFilterEpInstanceId_Object = MibTableColumn
cfprSwSspEthMonFilterEpInstanceId = _CfprSwSspEthMonFilterEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 1),
    _CfprSwSspEthMonFilterEpInstanceId_Type()
)
cfprSwSspEthMonFilterEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpInstanceId.setStatus("current")
_CfprSwSspEthMonFilterEpDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonFilterEpDn_Object = MibTableColumn
cfprSwSspEthMonFilterEpDn = _CfprSwSspEthMonFilterEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 2),
    _CfprSwSspEthMonFilterEpDn_Type()
)
cfprSwSspEthMonFilterEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpDn.setStatus("current")
_CfprSwSspEthMonFilterEpRn_Type = SnmpAdminString
_CfprSwSspEthMonFilterEpRn_Object = MibTableColumn
cfprSwSspEthMonFilterEpRn = _CfprSwSspEthMonFilterEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 3),
    _CfprSwSspEthMonFilterEpRn_Type()
)
cfprSwSspEthMonFilterEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpRn.setStatus("current")
_CfprSwSspEthMonFilterEpDestIp_Type = InetAddressIPv4
_CfprSwSspEthMonFilterEpDestIp_Object = MibTableColumn
cfprSwSspEthMonFilterEpDestIp = _CfprSwSspEthMonFilterEpDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 4),
    _CfprSwSspEthMonFilterEpDestIp_Type()
)
cfprSwSspEthMonFilterEpDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpDestIp.setStatus("current")
_CfprSwSspEthMonFilterEpDestMAC_Type = MacAddress
_CfprSwSspEthMonFilterEpDestMAC_Object = MibTableColumn
cfprSwSspEthMonFilterEpDestMAC = _CfprSwSspEthMonFilterEpDestMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 5),
    _CfprSwSspEthMonFilterEpDestMAC_Type()
)
cfprSwSspEthMonFilterEpDestMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpDestMAC.setStatus("current")
_CfprSwSspEthMonFilterEpDestPort_Type = CfprFabricPort
_CfprSwSspEthMonFilterEpDestPort_Object = MibTableColumn
cfprSwSspEthMonFilterEpDestPort = _CfprSwSspEthMonFilterEpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 6),
    _CfprSwSspEthMonFilterEpDestPort_Type()
)
cfprSwSspEthMonFilterEpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpDestPort.setStatus("current")
_CfprSwSspEthMonFilterEpEthertype_Type = Gauge32
_CfprSwSspEthMonFilterEpEthertype_Object = MibTableColumn
cfprSwSspEthMonFilterEpEthertype = _CfprSwSspEthMonFilterEpEthertype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 7),
    _CfprSwSspEthMonFilterEpEthertype_Type()
)
cfprSwSspEthMonFilterEpEthertype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpEthertype.setStatus("current")
_CfprSwSspEthMonFilterEpFilterFlag_Type = Gauge32
_CfprSwSspEthMonFilterEpFilterFlag_Object = MibTableColumn
cfprSwSspEthMonFilterEpFilterFlag = _CfprSwSspEthMonFilterEpFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 8),
    _CfprSwSspEthMonFilterEpFilterFlag_Type()
)
cfprSwSspEthMonFilterEpFilterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpFilterFlag.setStatus("current")
_CfprSwSspEthMonFilterEpIvlan_Type = Gauge32
_CfprSwSspEthMonFilterEpIvlan_Object = MibTableColumn
cfprSwSspEthMonFilterEpIvlan = _CfprSwSspEthMonFilterEpIvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 9),
    _CfprSwSspEthMonFilterEpIvlan_Type()
)
cfprSwSspEthMonFilterEpIvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpIvlan.setStatus("current")
_CfprSwSspEthMonFilterEpLifeCycle_Type = CfprSwPktCaptureLifeCycle
_CfprSwSspEthMonFilterEpLifeCycle_Object = MibTableColumn
cfprSwSspEthMonFilterEpLifeCycle = _CfprSwSspEthMonFilterEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 10),
    _CfprSwSspEthMonFilterEpLifeCycle_Type()
)
cfprSwSspEthMonFilterEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpLifeCycle.setStatus("current")
_CfprSwSspEthMonFilterEpNameId_Type = SnmpAdminString
_CfprSwSspEthMonFilterEpNameId_Object = MibTableColumn
cfprSwSspEthMonFilterEpNameId = _CfprSwSspEthMonFilterEpNameId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 11),
    _CfprSwSspEthMonFilterEpNameId_Type()
)
cfprSwSspEthMonFilterEpNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpNameId.setStatus("current")
_CfprSwSspEthMonFilterEpOvlan_Type = Gauge32
_CfprSwSspEthMonFilterEpOvlan_Object = MibTableColumn
cfprSwSspEthMonFilterEpOvlan = _CfprSwSspEthMonFilterEpOvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 12),
    _CfprSwSspEthMonFilterEpOvlan_Type()
)
cfprSwSspEthMonFilterEpOvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpOvlan.setStatus("current")
_CfprSwSspEthMonFilterEpPeerDn_Type = SnmpAdminString
_CfprSwSspEthMonFilterEpPeerDn_Object = MibTableColumn
cfprSwSspEthMonFilterEpPeerDn = _CfprSwSspEthMonFilterEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 13),
    _CfprSwSspEthMonFilterEpPeerDn_Type()
)
cfprSwSspEthMonFilterEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpPeerDn.setStatus("current")
_CfprSwSspEthMonFilterEpProtocol_Type = Gauge32
_CfprSwSspEthMonFilterEpProtocol_Object = MibTableColumn
cfprSwSspEthMonFilterEpProtocol = _CfprSwSspEthMonFilterEpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 14),
    _CfprSwSspEthMonFilterEpProtocol_Type()
)
cfprSwSspEthMonFilterEpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpProtocol.setStatus("current")
_CfprSwSspEthMonFilterEpRefCount_Type = Gauge32
_CfprSwSspEthMonFilterEpRefCount_Object = MibTableColumn
cfprSwSspEthMonFilterEpRefCount = _CfprSwSspEthMonFilterEpRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 15),
    _CfprSwSspEthMonFilterEpRefCount_Type()
)
cfprSwSspEthMonFilterEpRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpRefCount.setStatus("current")
_CfprSwSspEthMonFilterEpSrcIp_Type = InetAddressIPv4
_CfprSwSspEthMonFilterEpSrcIp_Object = MibTableColumn
cfprSwSspEthMonFilterEpSrcIp = _CfprSwSspEthMonFilterEpSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 16),
    _CfprSwSspEthMonFilterEpSrcIp_Type()
)
cfprSwSspEthMonFilterEpSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpSrcIp.setStatus("current")
_CfprSwSspEthMonFilterEpSrcMAC_Type = MacAddress
_CfprSwSspEthMonFilterEpSrcMAC_Object = MibTableColumn
cfprSwSspEthMonFilterEpSrcMAC = _CfprSwSspEthMonFilterEpSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 17),
    _CfprSwSspEthMonFilterEpSrcMAC_Type()
)
cfprSwSspEthMonFilterEpSrcMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpSrcMAC.setStatus("current")
_CfprSwSspEthMonFilterEpSrcPort_Type = CfprFabricPort
_CfprSwSspEthMonFilterEpSrcPort_Object = MibTableColumn
cfprSwSspEthMonFilterEpSrcPort = _CfprSwSspEthMonFilterEpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 18),
    _CfprSwSspEthMonFilterEpSrcPort_Type()
)
cfprSwSspEthMonFilterEpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpSrcPort.setStatus("current")
_CfprSwSspEthMonFilterEpDestIpv6_Type = InetAddressIPv6
_CfprSwSspEthMonFilterEpDestIpv6_Object = MibTableColumn
cfprSwSspEthMonFilterEpDestIpv6 = _CfprSwSspEthMonFilterEpDestIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 19),
    _CfprSwSspEthMonFilterEpDestIpv6_Type()
)
cfprSwSspEthMonFilterEpDestIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpDestIpv6.setStatus("current")
_CfprSwSspEthMonFilterEpEcmpId_Type = Gauge32
_CfprSwSspEthMonFilterEpEcmpId_Object = MibTableColumn
cfprSwSspEthMonFilterEpEcmpId = _CfprSwSspEthMonFilterEpEcmpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 20),
    _CfprSwSspEthMonFilterEpEcmpId_Type()
)
cfprSwSspEthMonFilterEpEcmpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpEcmpId.setStatus("current")
_CfprSwSspEthMonFilterEpSrcIpv6_Type = InetAddressIPv6
_CfprSwSspEthMonFilterEpSrcIpv6_Object = MibTableColumn
cfprSwSspEthMonFilterEpSrcIpv6 = _CfprSwSspEthMonFilterEpSrcIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 21),
    _CfprSwSspEthMonFilterEpSrcIpv6_Type()
)
cfprSwSspEthMonFilterEpSrcIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpSrcIpv6.setStatus("current")
_CfprSwSspEthMonFilterEpSubvlan_Type = Gauge32
_CfprSwSspEthMonFilterEpSubvlan_Object = MibTableColumn
cfprSwSspEthMonFilterEpSubvlan = _CfprSwSspEthMonFilterEpSubvlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 22),
    _CfprSwSspEthMonFilterEpSubvlan_Type()
)
cfprSwSspEthMonFilterEpSubvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpSubvlan.setStatus("current")
_CfprSwSspEthMonFilterEpVifId_Type = Gauge32
_CfprSwSspEthMonFilterEpVifId_Object = MibTableColumn
cfprSwSspEthMonFilterEpVifId = _CfprSwSspEthMonFilterEpVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 90, 1, 23),
    _CfprSwSspEthMonFilterEpVifId_Type()
)
cfprSwSspEthMonFilterEpVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFilterEpVifId.setStatus("current")
_CfprSwSspEthMonFsmTable_Object = MibTable
cfprSwSspEthMonFsmTable = _CfprSwSspEthMonFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTable.setStatus("current")
_CfprSwSspEthMonFsmEntry_Object = MibTableRow
cfprSwSspEthMonFsmEntry = _CfprSwSspEthMonFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1)
)
cfprSwSspEthMonFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmEntry.setStatus("current")
_CfprSwSspEthMonFsmInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonFsmInstanceId_Object = MibTableColumn
cfprSwSspEthMonFsmInstanceId = _CfprSwSspEthMonFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 1),
    _CfprSwSspEthMonFsmInstanceId_Type()
)
cfprSwSspEthMonFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmInstanceId.setStatus("current")
_CfprSwSspEthMonFsmDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonFsmDn_Object = MibTableColumn
cfprSwSspEthMonFsmDn = _CfprSwSspEthMonFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 2),
    _CfprSwSspEthMonFsmDn_Type()
)
cfprSwSspEthMonFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmDn.setStatus("current")
_CfprSwSspEthMonFsmRn_Type = SnmpAdminString
_CfprSwSspEthMonFsmRn_Object = MibTableColumn
cfprSwSspEthMonFsmRn = _CfprSwSspEthMonFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 3),
    _CfprSwSspEthMonFsmRn_Type()
)
cfprSwSspEthMonFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmRn.setStatus("current")
_CfprSwSspEthMonFsmCompletionTime_Type = DateAndTime
_CfprSwSspEthMonFsmCompletionTime_Object = MibTableColumn
cfprSwSspEthMonFsmCompletionTime = _CfprSwSspEthMonFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 4),
    _CfprSwSspEthMonFsmCompletionTime_Type()
)
cfprSwSspEthMonFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmCompletionTime.setStatus("current")
_CfprSwSspEthMonFsmCurrentFsm_Type = CfprSwSspEthMonFsmCurrentFsm
_CfprSwSspEthMonFsmCurrentFsm_Object = MibTableColumn
cfprSwSspEthMonFsmCurrentFsm = _CfprSwSspEthMonFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 5),
    _CfprSwSspEthMonFsmCurrentFsm_Type()
)
cfprSwSspEthMonFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmCurrentFsm.setStatus("current")
_CfprSwSspEthMonFsmDescrData_Type = SnmpAdminString
_CfprSwSspEthMonFsmDescrData_Object = MibTableColumn
cfprSwSspEthMonFsmDescrData = _CfprSwSspEthMonFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 6),
    _CfprSwSspEthMonFsmDescrData_Type()
)
cfprSwSspEthMonFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmDescrData.setStatus("current")
_CfprSwSspEthMonFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwSspEthMonFsmFsmStatus_Object = MibTableColumn
cfprSwSspEthMonFsmFsmStatus = _CfprSwSspEthMonFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 7),
    _CfprSwSspEthMonFsmFsmStatus_Type()
)
cfprSwSspEthMonFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmFsmStatus.setStatus("current")
_CfprSwSspEthMonFsmProgress_Type = Gauge32
_CfprSwSspEthMonFsmProgress_Object = MibTableColumn
cfprSwSspEthMonFsmProgress = _CfprSwSspEthMonFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 8),
    _CfprSwSspEthMonFsmProgress_Type()
)
cfprSwSspEthMonFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmProgress.setStatus("current")
_CfprSwSspEthMonFsmRmtErrCode_Type = Gauge32
_CfprSwSspEthMonFsmRmtErrCode_Object = MibTableColumn
cfprSwSspEthMonFsmRmtErrCode = _CfprSwSspEthMonFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 9),
    _CfprSwSspEthMonFsmRmtErrCode_Type()
)
cfprSwSspEthMonFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmRmtErrCode.setStatus("current")
_CfprSwSspEthMonFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwSspEthMonFsmRmtErrDescr_Object = MibTableColumn
cfprSwSspEthMonFsmRmtErrDescr = _CfprSwSspEthMonFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 10),
    _CfprSwSspEthMonFsmRmtErrDescr_Type()
)
cfprSwSspEthMonFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmRmtErrDescr.setStatus("current")
_CfprSwSspEthMonFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwSspEthMonFsmRmtRslt_Object = MibTableColumn
cfprSwSspEthMonFsmRmtRslt = _CfprSwSspEthMonFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 91, 1, 11),
    _CfprSwSspEthMonFsmRmtRslt_Type()
)
cfprSwSspEthMonFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmRmtRslt.setStatus("current")
_CfprSwSspEthMonFsmStageTable_Object = MibTable
cfprSwSspEthMonFsmStageTable = _CfprSwSspEthMonFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageTable.setStatus("current")
_CfprSwSspEthMonFsmStageEntry_Object = MibTableRow
cfprSwSspEthMonFsmStageEntry = _CfprSwSspEthMonFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1)
)
cfprSwSspEthMonFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageEntry.setStatus("current")
_CfprSwSspEthMonFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonFsmStageInstanceId_Object = MibTableColumn
cfprSwSspEthMonFsmStageInstanceId = _CfprSwSspEthMonFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 1),
    _CfprSwSspEthMonFsmStageInstanceId_Type()
)
cfprSwSspEthMonFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageInstanceId.setStatus("current")
_CfprSwSspEthMonFsmStageDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonFsmStageDn_Object = MibTableColumn
cfprSwSspEthMonFsmStageDn = _CfprSwSspEthMonFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 2),
    _CfprSwSspEthMonFsmStageDn_Type()
)
cfprSwSspEthMonFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageDn.setStatus("current")
_CfprSwSspEthMonFsmStageRn_Type = SnmpAdminString
_CfprSwSspEthMonFsmStageRn_Object = MibTableColumn
cfprSwSspEthMonFsmStageRn = _CfprSwSspEthMonFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 3),
    _CfprSwSspEthMonFsmStageRn_Type()
)
cfprSwSspEthMonFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageRn.setStatus("current")
_CfprSwSspEthMonFsmStageDescrData_Type = SnmpAdminString
_CfprSwSspEthMonFsmStageDescrData_Object = MibTableColumn
cfprSwSspEthMonFsmStageDescrData = _CfprSwSspEthMonFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 4),
    _CfprSwSspEthMonFsmStageDescrData_Type()
)
cfprSwSspEthMonFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageDescrData.setStatus("current")
_CfprSwSspEthMonFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwSspEthMonFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwSspEthMonFsmStageLastUpdateTime = _CfprSwSspEthMonFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 5),
    _CfprSwSspEthMonFsmStageLastUpdateTime_Type()
)
cfprSwSspEthMonFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageLastUpdateTime.setStatus("current")
_CfprSwSspEthMonFsmStageName_Type = CfprSwSspEthMonFsmStageName
_CfprSwSspEthMonFsmStageName_Object = MibTableColumn
cfprSwSspEthMonFsmStageName = _CfprSwSspEthMonFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 6),
    _CfprSwSspEthMonFsmStageName_Type()
)
cfprSwSspEthMonFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageName.setStatus("current")
_CfprSwSspEthMonFsmStageOrder_Type = Gauge32
_CfprSwSspEthMonFsmStageOrder_Object = MibTableColumn
cfprSwSspEthMonFsmStageOrder = _CfprSwSspEthMonFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 7),
    _CfprSwSspEthMonFsmStageOrder_Type()
)
cfprSwSspEthMonFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageOrder.setStatus("current")
_CfprSwSspEthMonFsmStageRetry_Type = Gauge32
_CfprSwSspEthMonFsmStageRetry_Object = MibTableColumn
cfprSwSspEthMonFsmStageRetry = _CfprSwSspEthMonFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 8),
    _CfprSwSspEthMonFsmStageRetry_Type()
)
cfprSwSspEthMonFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageRetry.setStatus("current")
_CfprSwSspEthMonFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwSspEthMonFsmStageStageStatus_Object = MibTableColumn
cfprSwSspEthMonFsmStageStageStatus = _CfprSwSspEthMonFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 92, 1, 9),
    _CfprSwSspEthMonFsmStageStageStatus_Type()
)
cfprSwSspEthMonFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmStageStageStatus.setStatus("current")
_CfprSwSspEthMonFsmTaskTable_Object = MibTable
cfprSwSspEthMonFsmTaskTable = _CfprSwSspEthMonFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskTable.setStatus("current")
_CfprSwSspEthMonFsmTaskEntry_Object = MibTableRow
cfprSwSspEthMonFsmTaskEntry = _CfprSwSspEthMonFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93, 1)
)
cfprSwSspEthMonFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskEntry.setStatus("current")
_CfprSwSspEthMonFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonFsmTaskInstanceId_Object = MibTableColumn
cfprSwSspEthMonFsmTaskInstanceId = _CfprSwSspEthMonFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93, 1, 1),
    _CfprSwSspEthMonFsmTaskInstanceId_Type()
)
cfprSwSspEthMonFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskInstanceId.setStatus("current")
_CfprSwSspEthMonFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonFsmTaskDn_Object = MibTableColumn
cfprSwSspEthMonFsmTaskDn = _CfprSwSspEthMonFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93, 1, 2),
    _CfprSwSspEthMonFsmTaskDn_Type()
)
cfprSwSspEthMonFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskDn.setStatus("current")
_CfprSwSspEthMonFsmTaskRn_Type = SnmpAdminString
_CfprSwSspEthMonFsmTaskRn_Object = MibTableColumn
cfprSwSspEthMonFsmTaskRn = _CfprSwSspEthMonFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93, 1, 3),
    _CfprSwSspEthMonFsmTaskRn_Type()
)
cfprSwSspEthMonFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskRn.setStatus("current")
_CfprSwSspEthMonFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwSspEthMonFsmTaskCompletion_Object = MibTableColumn
cfprSwSspEthMonFsmTaskCompletion = _CfprSwSspEthMonFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93, 1, 4),
    _CfprSwSspEthMonFsmTaskCompletion_Type()
)
cfprSwSspEthMonFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskCompletion.setStatus("current")
_CfprSwSspEthMonFsmTaskFlags_Type = CfprSwSspEthMonFsmTaskFlags
_CfprSwSspEthMonFsmTaskFlags_Object = MibTableColumn
cfprSwSspEthMonFsmTaskFlags = _CfprSwSspEthMonFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93, 1, 5),
    _CfprSwSspEthMonFsmTaskFlags_Type()
)
cfprSwSspEthMonFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskFlags.setStatus("current")
_CfprSwSspEthMonFsmTaskItem_Type = CfprSwSspEthMonFsmTaskItem
_CfprSwSspEthMonFsmTaskItem_Object = MibTableColumn
cfprSwSspEthMonFsmTaskItem = _CfprSwSspEthMonFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93, 1, 6),
    _CfprSwSspEthMonFsmTaskItem_Type()
)
cfprSwSspEthMonFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskItem.setStatus("current")
_CfprSwSspEthMonFsmTaskSeqId_Type = Gauge32
_CfprSwSspEthMonFsmTaskSeqId_Object = MibTableColumn
cfprSwSspEthMonFsmTaskSeqId = _CfprSwSspEthMonFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 93, 1, 7),
    _CfprSwSspEthMonFsmTaskSeqId_Type()
)
cfprSwSspEthMonFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonFsmTaskSeqId.setStatus("current")
_CfprSwSspEthMonSrcAppEpTable_Object = MibTable
cfprSwSspEthMonSrcAppEpTable = _CfprSwSspEthMonSrcAppEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpTable.setStatus("current")
_CfprSwSspEthMonSrcAppEpEntry_Object = MibTableRow
cfprSwSspEthMonSrcAppEpEntry = _CfprSwSspEthMonSrcAppEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1)
)
cfprSwSspEthMonSrcAppEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonSrcAppEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpEntry.setStatus("current")
_CfprSwSspEthMonSrcAppEpInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonSrcAppEpInstanceId_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpInstanceId = _CfprSwSspEthMonSrcAppEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 1),
    _CfprSwSspEthMonSrcAppEpInstanceId_Type()
)
cfprSwSspEthMonSrcAppEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpInstanceId.setStatus("current")
_CfprSwSspEthMonSrcAppEpDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonSrcAppEpDn_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpDn = _CfprSwSspEthMonSrcAppEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 2),
    _CfprSwSspEthMonSrcAppEpDn_Type()
)
cfprSwSspEthMonSrcAppEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpDn.setStatus("current")
_CfprSwSspEthMonSrcAppEpRn_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpRn_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpRn = _CfprSwSspEthMonSrcAppEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 3),
    _CfprSwSspEthMonSrcAppEpRn_Type()
)
cfprSwSspEthMonSrcAppEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpRn.setStatus("current")
_CfprSwSspEthMonSrcAppEpAppName_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpAppName_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpAppName = _CfprSwSspEthMonSrcAppEpAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 4),
    _CfprSwSspEthMonSrcAppEpAppName_Type()
)
cfprSwSspEthMonSrcAppEpAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpAppName.setStatus("current")
_CfprSwSspEthMonSrcAppEpExternalPortDn_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpExternalPortDn_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpExternalPortDn = _CfprSwSspEthMonSrcAppEpExternalPortDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 5),
    _CfprSwSspEthMonSrcAppEpExternalPortDn_Type()
)
cfprSwSspEthMonSrcAppEpExternalPortDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpExternalPortDn.setStatus("current")
_CfprSwSspEthMonSrcAppEpFilter_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpFilter_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpFilter = _CfprSwSspEthMonSrcAppEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 6),
    _CfprSwSspEthMonSrcAppEpFilter_Type()
)
cfprSwSspEthMonSrcAppEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpFilter.setStatus("current")
_CfprSwSspEthMonSrcAppEpFilterDn_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpFilterDn_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpFilterDn = _CfprSwSspEthMonSrcAppEpFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 7),
    _CfprSwSspEthMonSrcAppEpFilterDn_Type()
)
cfprSwSspEthMonSrcAppEpFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpFilterDn.setStatus("current")
_CfprSwSspEthMonSrcAppEpLifeCycle_Type = CfprSwPktCaptureLifeCycle
_CfprSwSspEthMonSrcAppEpLifeCycle_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpLifeCycle = _CfprSwSspEthMonSrcAppEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 8),
    _CfprSwSspEthMonSrcAppEpLifeCycle_Type()
)
cfprSwSspEthMonSrcAppEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpLifeCycle.setStatus("current")
_CfprSwSspEthMonSrcAppEpLinkName_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpLinkName_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpLinkName = _CfprSwSspEthMonSrcAppEpLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 9),
    _CfprSwSspEthMonSrcAppEpLinkName_Type()
)
cfprSwSspEthMonSrcAppEpLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpLinkName.setStatus("current")
_CfprSwSspEthMonSrcAppEpPcapfile_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpPcapfile_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpPcapfile = _CfprSwSspEthMonSrcAppEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 10),
    _CfprSwSspEthMonSrcAppEpPcapfile_Type()
)
cfprSwSspEthMonSrcAppEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpPcapfile.setStatus("current")
_CfprSwSspEthMonSrcAppEpPcapfilename_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpPcapfilename_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpPcapfilename = _CfprSwSspEthMonSrcAppEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 11),
    _CfprSwSspEthMonSrcAppEpPcapfilename_Type()
)
cfprSwSspEthMonSrcAppEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpPcapfilename.setStatus("current")
_CfprSwSspEthMonSrcAppEpPcapsize_Type = Gauge32
_CfprSwSspEthMonSrcAppEpPcapsize_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpPcapsize = _CfprSwSspEthMonSrcAppEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 12),
    _CfprSwSspEthMonSrcAppEpPcapsize_Type()
)
cfprSwSspEthMonSrcAppEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpPcapsize.setStatus("current")
_CfprSwSspEthMonSrcAppEpPortChannelDn_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpPortChannelDn_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpPortChannelDn = _CfprSwSspEthMonSrcAppEpPortChannelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 13),
    _CfprSwSspEthMonSrcAppEpPortChannelDn_Type()
)
cfprSwSspEthMonSrcAppEpPortChannelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpPortChannelDn.setStatus("current")
_CfprSwSspEthMonSrcAppEpPortName_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpPortName_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpPortName = _CfprSwSspEthMonSrcAppEpPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 14),
    _CfprSwSspEthMonSrcAppEpPortName_Type()
)
cfprSwSspEthMonSrcAppEpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpPortName.setStatus("current")
_CfprSwSspEthMonSrcAppEpSlotId_Type = Gauge32
_CfprSwSspEthMonSrcAppEpSlotId_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpSlotId = _CfprSwSspEthMonSrcAppEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 15),
    _CfprSwSspEthMonSrcAppEpSlotId_Type()
)
cfprSwSspEthMonSrcAppEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpSlotId.setStatus("current")
_CfprSwSspEthMonSrcAppEpPeerDn_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppEpPeerDn_Object = MibTableColumn
cfprSwSspEthMonSrcAppEpPeerDn = _CfprSwSspEthMonSrcAppEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 94, 1, 16),
    _CfprSwSspEthMonSrcAppEpPeerDn_Type()
)
cfprSwSspEthMonSrcAppEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppEpPeerDn.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpTable_Object = MibTable
cfprSwSspEthMonSrcAppLinksEpTable = _CfprSwSspEthMonSrcAppLinksEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpTable.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpEntry_Object = MibTableRow
cfprSwSspEthMonSrcAppLinksEpEntry = _CfprSwSspEthMonSrcAppLinksEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1)
)
cfprSwSspEthMonSrcAppLinksEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonSrcAppLinksEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpEntry.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonSrcAppLinksEpInstanceId_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpInstanceId = _CfprSwSspEthMonSrcAppLinksEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 1),
    _CfprSwSspEthMonSrcAppLinksEpInstanceId_Type()
)
cfprSwSspEthMonSrcAppLinksEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpInstanceId.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonSrcAppLinksEpDn_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpDn = _CfprSwSspEthMonSrcAppLinksEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 2),
    _CfprSwSspEthMonSrcAppLinksEpDn_Type()
)
cfprSwSspEthMonSrcAppLinksEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpDn.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpRn_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppLinksEpRn_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpRn = _CfprSwSspEthMonSrcAppLinksEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 3),
    _CfprSwSspEthMonSrcAppLinksEpRn_Type()
)
cfprSwSspEthMonSrcAppLinksEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpRn.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpChassisId_Type = Gauge32
_CfprSwSspEthMonSrcAppLinksEpChassisId_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpChassisId = _CfprSwSspEthMonSrcAppLinksEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 4),
    _CfprSwSspEthMonSrcAppLinksEpChassisId_Type()
)
cfprSwSspEthMonSrcAppLinksEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpChassisId.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpEqAggrPortId_Type = Gauge32
_CfprSwSspEthMonSrcAppLinksEpEqAggrPortId_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpEqAggrPortId = _CfprSwSspEthMonSrcAppLinksEpEqAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 5),
    _CfprSwSspEthMonSrcAppLinksEpEqAggrPortId_Type()
)
cfprSwSspEthMonSrcAppLinksEpEqAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpEqAggrPortId.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpEqPortId_Type = Gauge32
_CfprSwSspEthMonSrcAppLinksEpEqPortId_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpEqPortId = _CfprSwSspEthMonSrcAppLinksEpEqPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 6),
    _CfprSwSspEthMonSrcAppLinksEpEqPortId_Type()
)
cfprSwSspEthMonSrcAppLinksEpEqPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpEqPortId.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpEqSlotId_Type = Gauge32
_CfprSwSspEthMonSrcAppLinksEpEqSlotId_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpEqSlotId = _CfprSwSspEthMonSrcAppLinksEpEqSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 7),
    _CfprSwSspEthMonSrcAppLinksEpEqSlotId_Type()
)
cfprSwSspEthMonSrcAppLinksEpEqSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpEqSlotId.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpFilter_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppLinksEpFilter_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpFilter = _CfprSwSspEthMonSrcAppLinksEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 8),
    _CfprSwSspEthMonSrcAppLinksEpFilter_Type()
)
cfprSwSspEthMonSrcAppLinksEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpFilter.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpFilterDn_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppLinksEpFilterDn_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpFilterDn = _CfprSwSspEthMonSrcAppLinksEpFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 9),
    _CfprSwSspEthMonSrcAppLinksEpFilterDn_Type()
)
cfprSwSspEthMonSrcAppLinksEpFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpFilterDn.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpLifeCycle_Type = CfprSwPktCaptureLifeCycle
_CfprSwSspEthMonSrcAppLinksEpLifeCycle_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpLifeCycle = _CfprSwSspEthMonSrcAppLinksEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 10),
    _CfprSwSspEthMonSrcAppLinksEpLifeCycle_Type()
)
cfprSwSspEthMonSrcAppLinksEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpLifeCycle.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpName_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppLinksEpName_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpName = _CfprSwSspEthMonSrcAppLinksEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 11),
    _CfprSwSspEthMonSrcAppLinksEpName_Type()
)
cfprSwSspEthMonSrcAppLinksEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpName.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpPcapfile_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppLinksEpPcapfile_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpPcapfile = _CfprSwSspEthMonSrcAppLinksEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 12),
    _CfprSwSspEthMonSrcAppLinksEpPcapfile_Type()
)
cfprSwSspEthMonSrcAppLinksEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpPcapfile.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpPcapfilename_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppLinksEpPcapfilename_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpPcapfilename = _CfprSwSspEthMonSrcAppLinksEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 13),
    _CfprSwSspEthMonSrcAppLinksEpPcapfilename_Type()
)
cfprSwSspEthMonSrcAppLinksEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpPcapfilename.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpPcapsize_Type = Gauge32
_CfprSwSspEthMonSrcAppLinksEpPcapsize_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpPcapsize = _CfprSwSspEthMonSrcAppLinksEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 14),
    _CfprSwSspEthMonSrcAppLinksEpPcapsize_Type()
)
cfprSwSspEthMonSrcAppLinksEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpPcapsize.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwSspEthMonSrcAppLinksEpSwitchId_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpSwitchId = _CfprSwSspEthMonSrcAppLinksEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 15),
    _CfprSwSspEthMonSrcAppLinksEpSwitchId_Type()
)
cfprSwSspEthMonSrcAppLinksEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpSwitchId.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpVlan_Type = Gauge32
_CfprSwSspEthMonSrcAppLinksEpVlan_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpVlan = _CfprSwSspEthMonSrcAppLinksEpVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 16),
    _CfprSwSspEthMonSrcAppLinksEpVlan_Type()
)
cfprSwSspEthMonSrcAppLinksEpVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpVlan.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpVnicName1_Type = SnmpAdminString
_CfprSwSspEthMonSrcAppLinksEpVnicName1_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpVnicName1 = _CfprSwSspEthMonSrcAppLinksEpVnicName1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 17),
    _CfprSwSspEthMonSrcAppLinksEpVnicName1_Type()
)
cfprSwSspEthMonSrcAppLinksEpVnicName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpVnicName1.setStatus("current")
_CfprSwSspEthMonSrcAppLinksEpVifId_Type = Gauge32
_CfprSwSspEthMonSrcAppLinksEpVifId_Object = MibTableColumn
cfprSwSspEthMonSrcAppLinksEpVifId = _CfprSwSspEthMonSrcAppLinksEpVifId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 95, 1, 18),
    _CfprSwSspEthMonSrcAppLinksEpVifId_Type()
)
cfprSwSspEthMonSrcAppLinksEpVifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcAppLinksEpVifId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpTable_Object = MibTable
cfprSwSspEthMonSrcPhyEpTable = _CfprSwSspEthMonSrcPhyEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpTable.setStatus("current")
_CfprSwSspEthMonSrcPhyEpEntry_Object = MibTableRow
cfprSwSspEthMonSrcPhyEpEntry = _CfprSwSspEthMonSrcPhyEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1)
)
cfprSwSspEthMonSrcPhyEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonSrcPhyEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpEntry.setStatus("current")
_CfprSwSspEthMonSrcPhyEpInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonSrcPhyEpInstanceId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpInstanceId = _CfprSwSspEthMonSrcPhyEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 1),
    _CfprSwSspEthMonSrcPhyEpInstanceId_Type()
)
cfprSwSspEthMonSrcPhyEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpInstanceId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonSrcPhyEpDn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpDn = _CfprSwSspEthMonSrcPhyEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 2),
    _CfprSwSspEthMonSrcPhyEpDn_Type()
)
cfprSwSspEthMonSrcPhyEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpDn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpRn_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpRn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpRn = _CfprSwSspEthMonSrcPhyEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 3),
    _CfprSwSspEthMonSrcPhyEpRn_Type()
)
cfprSwSspEthMonSrcPhyEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpRn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpAggrPortId_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpAggrPortId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpAggrPortId = _CfprSwSspEthMonSrcPhyEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 4),
    _CfprSwSspEthMonSrcPhyEpAggrPortId_Type()
)
cfprSwSspEthMonSrcPhyEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpAggrPortId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpChassisId_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpChassisId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpChassisId = _CfprSwSspEthMonSrcPhyEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 5),
    _CfprSwSspEthMonSrcPhyEpChassisId_Type()
)
cfprSwSspEthMonSrcPhyEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpChassisId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFilter_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFilter_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFilter = _CfprSwSspEthMonSrcPhyEpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 6),
    _CfprSwSspEthMonSrcPhyEpFilter_Type()
)
cfprSwSspEthMonSrcPhyEpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFilter.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFilterDn_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFilterDn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFilterDn = _CfprSwSspEthMonSrcPhyEpFilterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 7),
    _CfprSwSspEthMonSrcPhyEpFilterDn_Type()
)
cfprSwSspEthMonSrcPhyEpFilterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFilterDn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpLifeCycle_Type = CfprSwPktCaptureLifeCycle
_CfprSwSspEthMonSrcPhyEpLifeCycle_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpLifeCycle = _CfprSwSspEthMonSrcPhyEpLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 8),
    _CfprSwSspEthMonSrcPhyEpLifeCycle_Type()
)
cfprSwSspEthMonSrcPhyEpLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpLifeCycle.setStatus("current")
_CfprSwSspEthMonSrcPhyEpPcapfile_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpPcapfile_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpPcapfile = _CfprSwSspEthMonSrcPhyEpPcapfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 9),
    _CfprSwSspEthMonSrcPhyEpPcapfile_Type()
)
cfprSwSspEthMonSrcPhyEpPcapfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpPcapfile.setStatus("current")
_CfprSwSspEthMonSrcPhyEpPcapfilename_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpPcapfilename_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpPcapfilename = _CfprSwSspEthMonSrcPhyEpPcapfilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 10),
    _CfprSwSspEthMonSrcPhyEpPcapfilename_Type()
)
cfprSwSspEthMonSrcPhyEpPcapfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpPcapfilename.setStatus("current")
_CfprSwSspEthMonSrcPhyEpPcapsize_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpPcapsize_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpPcapsize = _CfprSwSspEthMonSrcPhyEpPcapsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 11),
    _CfprSwSspEthMonSrcPhyEpPcapsize_Type()
)
cfprSwSspEthMonSrcPhyEpPcapsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpPcapsize.setStatus("current")
_CfprSwSspEthMonSrcPhyEpPortId_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpPortId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpPortId = _CfprSwSspEthMonSrcPhyEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 12),
    _CfprSwSspEthMonSrcPhyEpPortId_Type()
)
cfprSwSspEthMonSrcPhyEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpPortId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpSlotId_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpSlotId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpSlotId = _CfprSwSspEthMonSrcPhyEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 13),
    _CfprSwSspEthMonSrcPhyEpSlotId_Type()
)
cfprSwSspEthMonSrcPhyEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpSlotId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpSwitchId_Type = CfprNetworkSwitchId
_CfprSwSspEthMonSrcPhyEpSwitchId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpSwitchId = _CfprSwSspEthMonSrcPhyEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 14),
    _CfprSwSspEthMonSrcPhyEpSwitchId_Type()
)
cfprSwSspEthMonSrcPhyEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpSwitchId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmDescr_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmDescr_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmDescr = _CfprSwSspEthMonSrcPhyEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 15),
    _CfprSwSspEthMonSrcPhyEpFsmDescr_Type()
)
cfprSwSspEthMonSrcPhyEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmDescr.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmPrev_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmPrev_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmPrev = _CfprSwSspEthMonSrcPhyEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 16),
    _CfprSwSspEthMonSrcPhyEpFsmPrev_Type()
)
cfprSwSspEthMonSrcPhyEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmPrev.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmProgr_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpFsmProgr_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmProgr = _CfprSwSspEthMonSrcPhyEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 17),
    _CfprSwSspEthMonSrcPhyEpFsmProgr_Type()
)
cfprSwSspEthMonSrcPhyEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmProgr.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode = _CfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 18),
    _CfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode_Type()
)
cfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr = _CfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 19),
    _CfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr_Type()
)
cfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprSwSspEthMonSrcPhyEpFsmRmtInvRslt_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmRmtInvRslt = _CfprSwSspEthMonSrcPhyEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 20),
    _CfprSwSspEthMonSrcPhyEpFsmRmtInvRslt_Type()
)
cfprSwSspEthMonSrcPhyEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmRmtInvRslt.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageDescr_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmStageDescr_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageDescr = _CfprSwSspEthMonSrcPhyEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 21),
    _CfprSwSspEthMonSrcPhyEpFsmStageDescr_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageDescr.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStamp_Type = DateAndTime
_CfprSwSspEthMonSrcPhyEpFsmStamp_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStamp = _CfprSwSspEthMonSrcPhyEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 22),
    _CfprSwSspEthMonSrcPhyEpFsmStamp_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStamp.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStatus_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmStatus_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStatus = _CfprSwSspEthMonSrcPhyEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 23),
    _CfprSwSspEthMonSrcPhyEpFsmStatus_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStatus.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTry_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpFsmTry_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmTry = _CfprSwSspEthMonSrcPhyEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 24),
    _CfprSwSspEthMonSrcPhyEpFsmTry_Type()
)
cfprSwSspEthMonSrcPhyEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTry.setStatus("current")
_CfprSwSspEthMonSrcPhyEpPeerDn_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpPeerDn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpPeerDn = _CfprSwSspEthMonSrcPhyEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 25),
    _CfprSwSspEthMonSrcPhyEpPeerDn_Type()
)
cfprSwSspEthMonSrcPhyEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpPeerDn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpEcmpId_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpEcmpId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpEcmpId = _CfprSwSspEthMonSrcPhyEpEcmpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 26),
    _CfprSwSspEthMonSrcPhyEpEcmpId_Type()
)
cfprSwSspEthMonSrcPhyEpEcmpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpEcmpId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpSubIfVlan_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpSubIfVlan_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpSubIfVlan = _CfprSwSspEthMonSrcPhyEpSubIfVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 96, 1, 27),
    _CfprSwSspEthMonSrcPhyEpSubIfVlan_Type()
)
cfprSwSspEthMonSrcPhyEpSubIfVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpSubIfVlan.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTable_Object = MibTable
cfprSwSspEthMonSrcPhyEpFsmTable = _CfprSwSspEthMonSrcPhyEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTable.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmEntry_Object = MibTableRow
cfprSwSspEthMonSrcPhyEpFsmEntry = _CfprSwSspEthMonSrcPhyEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1)
)
cfprSwSspEthMonSrcPhyEpFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonSrcPhyEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmEntry.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonSrcPhyEpFsmInstanceId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmInstanceId = _CfprSwSspEthMonSrcPhyEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 1),
    _CfprSwSspEthMonSrcPhyEpFsmInstanceId_Type()
)
cfprSwSspEthMonSrcPhyEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmInstanceId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonSrcPhyEpFsmDn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmDn = _CfprSwSspEthMonSrcPhyEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 2),
    _CfprSwSspEthMonSrcPhyEpFsmDn_Type()
)
cfprSwSspEthMonSrcPhyEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmDn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmRn_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmRn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmRn = _CfprSwSspEthMonSrcPhyEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 3),
    _CfprSwSspEthMonSrcPhyEpFsmRn_Type()
)
cfprSwSspEthMonSrcPhyEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmRn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmCompletionTime_Type = DateAndTime
_CfprSwSspEthMonSrcPhyEpFsmCompletionTime_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmCompletionTime = _CfprSwSspEthMonSrcPhyEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 4),
    _CfprSwSspEthMonSrcPhyEpFsmCompletionTime_Type()
)
cfprSwSspEthMonSrcPhyEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmCompletionTime.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmCurrentFsm_Type = CfprSwSspEthMonSrcPhyEpFsmCurrentFsm
_CfprSwSspEthMonSrcPhyEpFsmCurrentFsm_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmCurrentFsm = _CfprSwSspEthMonSrcPhyEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 5),
    _CfprSwSspEthMonSrcPhyEpFsmCurrentFsm_Type()
)
cfprSwSspEthMonSrcPhyEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmCurrentFsm.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmDescrData_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmDescrData_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmDescrData = _CfprSwSspEthMonSrcPhyEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 6),
    _CfprSwSspEthMonSrcPhyEpFsmDescrData_Type()
)
cfprSwSspEthMonSrcPhyEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmDescrData.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprSwSspEthMonSrcPhyEpFsmFsmStatus_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmFsmStatus = _CfprSwSspEthMonSrcPhyEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 7),
    _CfprSwSspEthMonSrcPhyEpFsmFsmStatus_Type()
)
cfprSwSspEthMonSrcPhyEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmFsmStatus.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmProgress_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpFsmProgress_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmProgress = _CfprSwSspEthMonSrcPhyEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 8),
    _CfprSwSspEthMonSrcPhyEpFsmProgress_Type()
)
cfprSwSspEthMonSrcPhyEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmProgress.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmRmtErrCode_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpFsmRmtErrCode_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmRmtErrCode = _CfprSwSspEthMonSrcPhyEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 9),
    _CfprSwSspEthMonSrcPhyEpFsmRmtErrCode_Type()
)
cfprSwSspEthMonSrcPhyEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmRmtErrCode.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmRmtErrDescr_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmRmtErrDescr_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmRmtErrDescr = _CfprSwSspEthMonSrcPhyEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 10),
    _CfprSwSspEthMonSrcPhyEpFsmRmtErrDescr_Type()
)
cfprSwSspEthMonSrcPhyEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmRmtErrDescr.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprSwSspEthMonSrcPhyEpFsmRmtRslt_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmRmtRslt = _CfprSwSspEthMonSrcPhyEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 97, 1, 11),
    _CfprSwSspEthMonSrcPhyEpFsmRmtRslt_Type()
)
cfprSwSspEthMonSrcPhyEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmRmtRslt.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageTable_Object = MibTable
cfprSwSspEthMonSrcPhyEpFsmStageTable = _CfprSwSspEthMonSrcPhyEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageTable.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageEntry_Object = MibTableRow
cfprSwSspEthMonSrcPhyEpFsmStageEntry = _CfprSwSspEthMonSrcPhyEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1)
)
cfprSwSspEthMonSrcPhyEpFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonSrcPhyEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageEntry.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonSrcPhyEpFsmStageInstanceId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageInstanceId = _CfprSwSspEthMonSrcPhyEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 1),
    _CfprSwSspEthMonSrcPhyEpFsmStageInstanceId_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageInstanceId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonSrcPhyEpFsmStageDn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageDn = _CfprSwSspEthMonSrcPhyEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 2),
    _CfprSwSspEthMonSrcPhyEpFsmStageDn_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageDn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageRn_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmStageRn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageRn = _CfprSwSspEthMonSrcPhyEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 3),
    _CfprSwSspEthMonSrcPhyEpFsmStageRn_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageRn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageDescrData_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmStageDescrData_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageDescrData = _CfprSwSspEthMonSrcPhyEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 4),
    _CfprSwSspEthMonSrcPhyEpFsmStageDescrData_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageDescrData.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime_Type = DateAndTime
_CfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime = _CfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 5),
    _CfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageName_Type = CfprSwSspEthMonSrcPhyEpFsmStageName
_CfprSwSspEthMonSrcPhyEpFsmStageName_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageName = _CfprSwSspEthMonSrcPhyEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 6),
    _CfprSwSspEthMonSrcPhyEpFsmStageName_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageName.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageOrder_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpFsmStageOrder_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageOrder = _CfprSwSspEthMonSrcPhyEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 7),
    _CfprSwSspEthMonSrcPhyEpFsmStageOrder_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageOrder.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageRetry_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpFsmStageRetry_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageRetry = _CfprSwSspEthMonSrcPhyEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 8),
    _CfprSwSspEthMonSrcPhyEpFsmStageRetry_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageRetry.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprSwSspEthMonSrcPhyEpFsmStageStageStatus_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmStageStageStatus = _CfprSwSspEthMonSrcPhyEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 98, 1, 9),
    _CfprSwSspEthMonSrcPhyEpFsmStageStageStatus_Type()
)
cfprSwSspEthMonSrcPhyEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmStageStageStatus.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskTable_Object = MibTable
cfprSwSspEthMonSrcPhyEpFsmTaskTable = _CfprSwSspEthMonSrcPhyEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99)
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskTable.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskEntry_Object = MibTableRow
cfprSwSspEthMonSrcPhyEpFsmTaskEntry = _CfprSwSspEthMonSrcPhyEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99, 1)
)
cfprSwSspEthMonSrcPhyEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SW-MIB", "cfprSwSspEthMonSrcPhyEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskEntry.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprSwSspEthMonSrcPhyEpFsmTaskInstanceId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmTaskInstanceId = _CfprSwSspEthMonSrcPhyEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99, 1, 1),
    _CfprSwSspEthMonSrcPhyEpFsmTaskInstanceId_Type()
)
cfprSwSspEthMonSrcPhyEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskInstanceId.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskDn_Type = CfprManagedObjectDn
_CfprSwSspEthMonSrcPhyEpFsmTaskDn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmTaskDn = _CfprSwSspEthMonSrcPhyEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99, 1, 2),
    _CfprSwSspEthMonSrcPhyEpFsmTaskDn_Type()
)
cfprSwSspEthMonSrcPhyEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskDn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskRn_Type = SnmpAdminString
_CfprSwSspEthMonSrcPhyEpFsmTaskRn_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmTaskRn = _CfprSwSspEthMonSrcPhyEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99, 1, 3),
    _CfprSwSspEthMonSrcPhyEpFsmTaskRn_Type()
)
cfprSwSspEthMonSrcPhyEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskRn.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskCompletion_Type = CfprFsmCompletion
_CfprSwSspEthMonSrcPhyEpFsmTaskCompletion_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmTaskCompletion = _CfprSwSspEthMonSrcPhyEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99, 1, 4),
    _CfprSwSspEthMonSrcPhyEpFsmTaskCompletion_Type()
)
cfprSwSspEthMonSrcPhyEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskCompletion.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskFlags_Type = CfprFsmFlags
_CfprSwSspEthMonSrcPhyEpFsmTaskFlags_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmTaskFlags = _CfprSwSspEthMonSrcPhyEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99, 1, 5),
    _CfprSwSspEthMonSrcPhyEpFsmTaskFlags_Type()
)
cfprSwSspEthMonSrcPhyEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskFlags.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskItem_Type = CfprSwSspEthMonSrcPhyEpFsmTaskItem
_CfprSwSspEthMonSrcPhyEpFsmTaskItem_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmTaskItem = _CfprSwSspEthMonSrcPhyEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99, 1, 6),
    _CfprSwSspEthMonSrcPhyEpFsmTaskItem_Type()
)
cfprSwSspEthMonSrcPhyEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskItem.setStatus("current")
_CfprSwSspEthMonSrcPhyEpFsmTaskSeqId_Type = Gauge32
_CfprSwSspEthMonSrcPhyEpFsmTaskSeqId_Object = MibTableColumn
cfprSwSspEthMonSrcPhyEpFsmTaskSeqId = _CfprSwSspEthMonSrcPhyEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 75, 99, 1, 7),
    _CfprSwSspEthMonSrcPhyEpFsmTaskSeqId_Type()
)
cfprSwSspEthMonSrcPhyEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSwSspEthMonSrcPhyEpFsmTaskSeqId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-SW-MIB",
    **{"cfprSwObjects": cfprSwObjects,
       "cfprSwAccessDomainTable": cfprSwAccessDomainTable,
       "cfprSwAccessDomainEntry": cfprSwAccessDomainEntry,
       "cfprSwAccessDomainInstanceId": cfprSwAccessDomainInstanceId,
       "cfprSwAccessDomainDn": cfprSwAccessDomainDn,
       "cfprSwAccessDomainRn": cfprSwAccessDomainRn,
       "cfprSwAccessDomainFsmDescr": cfprSwAccessDomainFsmDescr,
       "cfprSwAccessDomainFsmPrev": cfprSwAccessDomainFsmPrev,
       "cfprSwAccessDomainFsmProgr": cfprSwAccessDomainFsmProgr,
       "cfprSwAccessDomainFsmRmtInvErrCode": cfprSwAccessDomainFsmRmtInvErrCode,
       "cfprSwAccessDomainFsmRmtInvErrDescr": cfprSwAccessDomainFsmRmtInvErrDescr,
       "cfprSwAccessDomainFsmRmtInvRslt": cfprSwAccessDomainFsmRmtInvRslt,
       "cfprSwAccessDomainFsmStageDescr": cfprSwAccessDomainFsmStageDescr,
       "cfprSwAccessDomainFsmStamp": cfprSwAccessDomainFsmStamp,
       "cfprSwAccessDomainFsmStatus": cfprSwAccessDomainFsmStatus,
       "cfprSwAccessDomainFsmTry": cfprSwAccessDomainFsmTry,
       "cfprSwAccessDomainLocale": cfprSwAccessDomainLocale,
       "cfprSwAccessDomainName": cfprSwAccessDomainName,
       "cfprSwAccessDomainSwitchId": cfprSwAccessDomainSwitchId,
       "cfprSwAccessDomainTransport": cfprSwAccessDomainTransport,
       "cfprSwAccessDomainType": cfprSwAccessDomainType,
       "cfprSwAccessDomainFsmTable": cfprSwAccessDomainFsmTable,
       "cfprSwAccessDomainFsmEntry": cfprSwAccessDomainFsmEntry,
       "cfprSwAccessDomainFsmInstanceId": cfprSwAccessDomainFsmInstanceId,
       "cfprSwAccessDomainFsmDn": cfprSwAccessDomainFsmDn,
       "cfprSwAccessDomainFsmRn": cfprSwAccessDomainFsmRn,
       "cfprSwAccessDomainFsmCompletionTime": cfprSwAccessDomainFsmCompletionTime,
       "cfprSwAccessDomainFsmCurrentFsm": cfprSwAccessDomainFsmCurrentFsm,
       "cfprSwAccessDomainFsmDescrData": cfprSwAccessDomainFsmDescrData,
       "cfprSwAccessDomainFsmFsmStatus": cfprSwAccessDomainFsmFsmStatus,
       "cfprSwAccessDomainFsmProgress": cfprSwAccessDomainFsmProgress,
       "cfprSwAccessDomainFsmRmtErrCode": cfprSwAccessDomainFsmRmtErrCode,
       "cfprSwAccessDomainFsmRmtErrDescr": cfprSwAccessDomainFsmRmtErrDescr,
       "cfprSwAccessDomainFsmRmtRslt": cfprSwAccessDomainFsmRmtRslt,
       "cfprSwAccessDomainFsmStageTable": cfprSwAccessDomainFsmStageTable,
       "cfprSwAccessDomainFsmStageEntry": cfprSwAccessDomainFsmStageEntry,
       "cfprSwAccessDomainFsmStageInstanceId": cfprSwAccessDomainFsmStageInstanceId,
       "cfprSwAccessDomainFsmStageDn": cfprSwAccessDomainFsmStageDn,
       "cfprSwAccessDomainFsmStageRn": cfprSwAccessDomainFsmStageRn,
       "cfprSwAccessDomainFsmStageDescrData": cfprSwAccessDomainFsmStageDescrData,
       "cfprSwAccessDomainFsmStageLastUpdateTime": cfprSwAccessDomainFsmStageLastUpdateTime,
       "cfprSwAccessDomainFsmStageName": cfprSwAccessDomainFsmStageName,
       "cfprSwAccessDomainFsmStageOrder": cfprSwAccessDomainFsmStageOrder,
       "cfprSwAccessDomainFsmStageRetry": cfprSwAccessDomainFsmStageRetry,
       "cfprSwAccessDomainFsmStageStageStatus": cfprSwAccessDomainFsmStageStageStatus,
       "cfprSwAccessDomainFsmTaskTable": cfprSwAccessDomainFsmTaskTable,
       "cfprSwAccessDomainFsmTaskEntry": cfprSwAccessDomainFsmTaskEntry,
       "cfprSwAccessDomainFsmTaskInstanceId": cfprSwAccessDomainFsmTaskInstanceId,
       "cfprSwAccessDomainFsmTaskDn": cfprSwAccessDomainFsmTaskDn,
       "cfprSwAccessDomainFsmTaskRn": cfprSwAccessDomainFsmTaskRn,
       "cfprSwAccessDomainFsmTaskCompletion": cfprSwAccessDomainFsmTaskCompletion,
       "cfprSwAccessDomainFsmTaskFlags": cfprSwAccessDomainFsmTaskFlags,
       "cfprSwAccessDomainFsmTaskItem": cfprSwAccessDomainFsmTaskItem,
       "cfprSwAccessDomainFsmTaskSeqId": cfprSwAccessDomainFsmTaskSeqId,
       "cfprSwAccessEpTable": cfprSwAccessEpTable,
       "cfprSwAccessEpEntry": cfprSwAccessEpEntry,
       "cfprSwAccessEpInstanceId": cfprSwAccessEpInstanceId,
       "cfprSwAccessEpDn": cfprSwAccessEpDn,
       "cfprSwAccessEpRn": cfprSwAccessEpRn,
       "cfprSwAccessEpAdminState": cfprSwAccessEpAdminState,
       "cfprSwAccessEpAggrPortId": cfprSwAccessEpAggrPortId,
       "cfprSwAccessEpChassisId": cfprSwAccessEpChassisId,
       "cfprSwAccessEpEncap": cfprSwAccessEpEncap,
       "cfprSwAccessEpEpDn": cfprSwAccessEpEpDn,
       "cfprSwAccessEpIfRole": cfprSwAccessEpIfRole,
       "cfprSwAccessEpIfType": cfprSwAccessEpIfType,
       "cfprSwAccessEpLc": cfprSwAccessEpLc,
       "cfprSwAccessEpLocale": cfprSwAccessEpLocale,
       "cfprSwAccessEpName": cfprSwAccessEpName,
       "cfprSwAccessEpNsSize": cfprSwAccessEpNsSize,
       "cfprSwAccessEpPeerAggrPortId": cfprSwAccessEpPeerAggrPortId,
       "cfprSwAccessEpPeerChassisId": cfprSwAccessEpPeerChassisId,
       "cfprSwAccessEpPeerDn": cfprSwAccessEpPeerDn,
       "cfprSwAccessEpPeerPortId": cfprSwAccessEpPeerPortId,
       "cfprSwAccessEpPeerSlotId": cfprSwAccessEpPeerSlotId,
       "cfprSwAccessEpPortId": cfprSwAccessEpPortId,
       "cfprSwAccessEpSlotId": cfprSwAccessEpSlotId,
       "cfprSwAccessEpSwitchId": cfprSwAccessEpSwitchId,
       "cfprSwAccessEpTransport": cfprSwAccessEpTransport,
       "cfprSwAccessEpType": cfprSwAccessEpType,
       "cfprSwCardEnvStatsTable": cfprSwCardEnvStatsTable,
       "cfprSwCardEnvStatsEntry": cfprSwCardEnvStatsEntry,
       "cfprSwCardEnvStatsInstanceId": cfprSwCardEnvStatsInstanceId,
       "cfprSwCardEnvStatsDn": cfprSwCardEnvStatsDn,
       "cfprSwCardEnvStatsRn": cfprSwCardEnvStatsRn,
       "cfprSwCardEnvStatsSlotOutlet1": cfprSwCardEnvStatsSlotOutlet1,
       "cfprSwCardEnvStatsSlotOutlet1Avg": cfprSwCardEnvStatsSlotOutlet1Avg,
       "cfprSwCardEnvStatsSlotOutlet1Max": cfprSwCardEnvStatsSlotOutlet1Max,
       "cfprSwCardEnvStatsSlotOutlet1Min": cfprSwCardEnvStatsSlotOutlet1Min,
       "cfprSwCardEnvStatsSlotOutlet2": cfprSwCardEnvStatsSlotOutlet2,
       "cfprSwCardEnvStatsSlotOutlet2Avg": cfprSwCardEnvStatsSlotOutlet2Avg,
       "cfprSwCardEnvStatsSlotOutlet2Max": cfprSwCardEnvStatsSlotOutlet2Max,
       "cfprSwCardEnvStatsSlotOutlet2Min": cfprSwCardEnvStatsSlotOutlet2Min,
       "cfprSwCardEnvStatsSlotOutlet3": cfprSwCardEnvStatsSlotOutlet3,
       "cfprSwCardEnvStatsSlotOutlet3Avg": cfprSwCardEnvStatsSlotOutlet3Avg,
       "cfprSwCardEnvStatsSlotOutlet3Max": cfprSwCardEnvStatsSlotOutlet3Max,
       "cfprSwCardEnvStatsSlotOutlet3Min": cfprSwCardEnvStatsSlotOutlet3Min,
       "cfprSwCardEnvStatsIntervals": cfprSwCardEnvStatsIntervals,
       "cfprSwCardEnvStatsSuspect": cfprSwCardEnvStatsSuspect,
       "cfprSwCardEnvStatsThresholded": cfprSwCardEnvStatsThresholded,
       "cfprSwCardEnvStatsTimeCollected": cfprSwCardEnvStatsTimeCollected,
       "cfprSwCardEnvStatsUpdate": cfprSwCardEnvStatsUpdate,
       "cfprSwCardEnvStatsHistTable": cfprSwCardEnvStatsHistTable,
       "cfprSwCardEnvStatsHistEntry": cfprSwCardEnvStatsHistEntry,
       "cfprSwCardEnvStatsHistInstanceId": cfprSwCardEnvStatsHistInstanceId,
       "cfprSwCardEnvStatsHistDn": cfprSwCardEnvStatsHistDn,
       "cfprSwCardEnvStatsHistRn": cfprSwCardEnvStatsHistRn,
       "cfprSwCardEnvStatsHistSlotOutlet1": cfprSwCardEnvStatsHistSlotOutlet1,
       "cfprSwCardEnvStatsHistSlotOutlet1Avg": cfprSwCardEnvStatsHistSlotOutlet1Avg,
       "cfprSwCardEnvStatsHistSlotOutlet1Max": cfprSwCardEnvStatsHistSlotOutlet1Max,
       "cfprSwCardEnvStatsHistSlotOutlet1Min": cfprSwCardEnvStatsHistSlotOutlet1Min,
       "cfprSwCardEnvStatsHistSlotOutlet2": cfprSwCardEnvStatsHistSlotOutlet2,
       "cfprSwCardEnvStatsHistSlotOutlet2Avg": cfprSwCardEnvStatsHistSlotOutlet2Avg,
       "cfprSwCardEnvStatsHistSlotOutlet2Max": cfprSwCardEnvStatsHistSlotOutlet2Max,
       "cfprSwCardEnvStatsHistSlotOutlet2Min": cfprSwCardEnvStatsHistSlotOutlet2Min,
       "cfprSwCardEnvStatsHistSlotOutlet3": cfprSwCardEnvStatsHistSlotOutlet3,
       "cfprSwCardEnvStatsHistSlotOutlet3Avg": cfprSwCardEnvStatsHistSlotOutlet3Avg,
       "cfprSwCardEnvStatsHistSlotOutlet3Max": cfprSwCardEnvStatsHistSlotOutlet3Max,
       "cfprSwCardEnvStatsHistSlotOutlet3Min": cfprSwCardEnvStatsHistSlotOutlet3Min,
       "cfprSwCardEnvStatsHistId": cfprSwCardEnvStatsHistId,
       "cfprSwCardEnvStatsHistMostRecent": cfprSwCardEnvStatsHistMostRecent,
       "cfprSwCardEnvStatsHistSuspect": cfprSwCardEnvStatsHistSuspect,
       "cfprSwCardEnvStatsHistThresholded": cfprSwCardEnvStatsHistThresholded,
       "cfprSwCardEnvStatsHistTimeCollected": cfprSwCardEnvStatsHistTimeCollected,
       "cfprSwCmclanTable": cfprSwCmclanTable,
       "cfprSwCmclanEntry": cfprSwCmclanEntry,
       "cfprSwCmclanInstanceId": cfprSwCmclanInstanceId,
       "cfprSwCmclanDn": cfprSwCmclanDn,
       "cfprSwCmclanRn": cfprSwCmclanRn,
       "cfprSwCmclanCimcIds": cfprSwCmclanCimcIds,
       "cfprSwCmclanEpDn": cfprSwCmclanEpDn,
       "cfprSwCmclanId": cfprSwCmclanId,
       "cfprSwCmclanIfRole": cfprSwCmclanIfRole,
       "cfprSwCmclanIfType": cfprSwCmclanIfType,
       "cfprSwCmclanLocale": cfprSwCmclanLocale,
       "cfprSwCmclanName": cfprSwCmclanName,
       "cfprSwCmclanPeerDn": cfprSwCmclanPeerDn,
       "cfprSwCmclanTransport": cfprSwCmclanTransport,
       "cfprSwCmclanType": cfprSwCmclanType,
       "cfprSwEnvStatsTable": cfprSwEnvStatsTable,
       "cfprSwEnvStatsEntry": cfprSwEnvStatsEntry,
       "cfprSwEnvStatsInstanceId": cfprSwEnvStatsInstanceId,
       "cfprSwEnvStatsDn": cfprSwEnvStatsDn,
       "cfprSwEnvStatsRn": cfprSwEnvStatsRn,
       "cfprSwEnvStatsFanCtrlrInlet1": cfprSwEnvStatsFanCtrlrInlet1,
       "cfprSwEnvStatsFanCtrlrInlet1Avg": cfprSwEnvStatsFanCtrlrInlet1Avg,
       "cfprSwEnvStatsFanCtrlrInlet1Max": cfprSwEnvStatsFanCtrlrInlet1Max,
       "cfprSwEnvStatsFanCtrlrInlet1Min": cfprSwEnvStatsFanCtrlrInlet1Min,
       "cfprSwEnvStatsFanCtrlrInlet2": cfprSwEnvStatsFanCtrlrInlet2,
       "cfprSwEnvStatsFanCtrlrInlet2Avg": cfprSwEnvStatsFanCtrlrInlet2Avg,
       "cfprSwEnvStatsFanCtrlrInlet2Max": cfprSwEnvStatsFanCtrlrInlet2Max,
       "cfprSwEnvStatsFanCtrlrInlet2Min": cfprSwEnvStatsFanCtrlrInlet2Min,
       "cfprSwEnvStatsFanCtrlrInlet3": cfprSwEnvStatsFanCtrlrInlet3,
       "cfprSwEnvStatsFanCtrlrInlet3Avg": cfprSwEnvStatsFanCtrlrInlet3Avg,
       "cfprSwEnvStatsFanCtrlrInlet3Max": cfprSwEnvStatsFanCtrlrInlet3Max,
       "cfprSwEnvStatsFanCtrlrInlet3Min": cfprSwEnvStatsFanCtrlrInlet3Min,
       "cfprSwEnvStatsFanCtrlrInlet4": cfprSwEnvStatsFanCtrlrInlet4,
       "cfprSwEnvStatsFanCtrlrInlet4Avg": cfprSwEnvStatsFanCtrlrInlet4Avg,
       "cfprSwEnvStatsFanCtrlrInlet4Max": cfprSwEnvStatsFanCtrlrInlet4Max,
       "cfprSwEnvStatsFanCtrlrInlet4Min": cfprSwEnvStatsFanCtrlrInlet4Min,
       "cfprSwEnvStatsIntervals": cfprSwEnvStatsIntervals,
       "cfprSwEnvStatsMainBoardOutlet1": cfprSwEnvStatsMainBoardOutlet1,
       "cfprSwEnvStatsMainBoardOutlet1Avg": cfprSwEnvStatsMainBoardOutlet1Avg,
       "cfprSwEnvStatsMainBoardOutlet1Max": cfprSwEnvStatsMainBoardOutlet1Max,
       "cfprSwEnvStatsMainBoardOutlet1Min": cfprSwEnvStatsMainBoardOutlet1Min,
       "cfprSwEnvStatsMainBoardOutlet2": cfprSwEnvStatsMainBoardOutlet2,
       "cfprSwEnvStatsMainBoardOutlet2Avg": cfprSwEnvStatsMainBoardOutlet2Avg,
       "cfprSwEnvStatsMainBoardOutlet2Max": cfprSwEnvStatsMainBoardOutlet2Max,
       "cfprSwEnvStatsMainBoardOutlet2Min": cfprSwEnvStatsMainBoardOutlet2Min,
       "cfprSwEnvStatsPsuCtrlrInlet1": cfprSwEnvStatsPsuCtrlrInlet1,
       "cfprSwEnvStatsPsuCtrlrInlet1Avg": cfprSwEnvStatsPsuCtrlrInlet1Avg,
       "cfprSwEnvStatsPsuCtrlrInlet1Max": cfprSwEnvStatsPsuCtrlrInlet1Max,
       "cfprSwEnvStatsPsuCtrlrInlet1Min": cfprSwEnvStatsPsuCtrlrInlet1Min,
       "cfprSwEnvStatsPsuCtrlrInlet2": cfprSwEnvStatsPsuCtrlrInlet2,
       "cfprSwEnvStatsPsuCtrlrInlet2Avg": cfprSwEnvStatsPsuCtrlrInlet2Avg,
       "cfprSwEnvStatsPsuCtrlrInlet2Max": cfprSwEnvStatsPsuCtrlrInlet2Max,
       "cfprSwEnvStatsPsuCtrlrInlet2Min": cfprSwEnvStatsPsuCtrlrInlet2Min,
       "cfprSwEnvStatsSuspect": cfprSwEnvStatsSuspect,
       "cfprSwEnvStatsThresholded": cfprSwEnvStatsThresholded,
       "cfprSwEnvStatsTimeCollected": cfprSwEnvStatsTimeCollected,
       "cfprSwEnvStatsUpdate": cfprSwEnvStatsUpdate,
       "cfprSwEnvStatsHistTable": cfprSwEnvStatsHistTable,
       "cfprSwEnvStatsHistEntry": cfprSwEnvStatsHistEntry,
       "cfprSwEnvStatsHistInstanceId": cfprSwEnvStatsHistInstanceId,
       "cfprSwEnvStatsHistDn": cfprSwEnvStatsHistDn,
       "cfprSwEnvStatsHistRn": cfprSwEnvStatsHistRn,
       "cfprSwEnvStatsHistFanCtrlrInlet1": cfprSwEnvStatsHistFanCtrlrInlet1,
       "cfprSwEnvStatsHistFanCtrlrInlet1Avg": cfprSwEnvStatsHistFanCtrlrInlet1Avg,
       "cfprSwEnvStatsHistFanCtrlrInlet1Max": cfprSwEnvStatsHistFanCtrlrInlet1Max,
       "cfprSwEnvStatsHistFanCtrlrInlet1Min": cfprSwEnvStatsHistFanCtrlrInlet1Min,
       "cfprSwEnvStatsHistFanCtrlrInlet2": cfprSwEnvStatsHistFanCtrlrInlet2,
       "cfprSwEnvStatsHistFanCtrlrInlet2Avg": cfprSwEnvStatsHistFanCtrlrInlet2Avg,
       "cfprSwEnvStatsHistFanCtrlrInlet2Max": cfprSwEnvStatsHistFanCtrlrInlet2Max,
       "cfprSwEnvStatsHistFanCtrlrInlet2Min": cfprSwEnvStatsHistFanCtrlrInlet2Min,
       "cfprSwEnvStatsHistFanCtrlrInlet3": cfprSwEnvStatsHistFanCtrlrInlet3,
       "cfprSwEnvStatsHistFanCtrlrInlet3Avg": cfprSwEnvStatsHistFanCtrlrInlet3Avg,
       "cfprSwEnvStatsHistFanCtrlrInlet3Max": cfprSwEnvStatsHistFanCtrlrInlet3Max,
       "cfprSwEnvStatsHistFanCtrlrInlet3Min": cfprSwEnvStatsHistFanCtrlrInlet3Min,
       "cfprSwEnvStatsHistFanCtrlrInlet4": cfprSwEnvStatsHistFanCtrlrInlet4,
       "cfprSwEnvStatsHistFanCtrlrInlet4Avg": cfprSwEnvStatsHistFanCtrlrInlet4Avg,
       "cfprSwEnvStatsHistFanCtrlrInlet4Max": cfprSwEnvStatsHistFanCtrlrInlet4Max,
       "cfprSwEnvStatsHistFanCtrlrInlet4Min": cfprSwEnvStatsHistFanCtrlrInlet4Min,
       "cfprSwEnvStatsHistId": cfprSwEnvStatsHistId,
       "cfprSwEnvStatsHistMainBoardOutlet1": cfprSwEnvStatsHistMainBoardOutlet1,
       "cfprSwEnvStatsHistMainBoardOutlet1Avg": cfprSwEnvStatsHistMainBoardOutlet1Avg,
       "cfprSwEnvStatsHistMainBoardOutlet1Max": cfprSwEnvStatsHistMainBoardOutlet1Max,
       "cfprSwEnvStatsHistMainBoardOutlet1Min": cfprSwEnvStatsHistMainBoardOutlet1Min,
       "cfprSwEnvStatsHistMainBoardOutlet2": cfprSwEnvStatsHistMainBoardOutlet2,
       "cfprSwEnvStatsHistMainBoardOutlet2Avg": cfprSwEnvStatsHistMainBoardOutlet2Avg,
       "cfprSwEnvStatsHistMainBoardOutlet2Max": cfprSwEnvStatsHistMainBoardOutlet2Max,
       "cfprSwEnvStatsHistMainBoardOutlet2Min": cfprSwEnvStatsHistMainBoardOutlet2Min,
       "cfprSwEnvStatsHistMostRecent": cfprSwEnvStatsHistMostRecent,
       "cfprSwEnvStatsHistPsuCtrlrInlet1": cfprSwEnvStatsHistPsuCtrlrInlet1,
       "cfprSwEnvStatsHistPsuCtrlrInlet1Avg": cfprSwEnvStatsHistPsuCtrlrInlet1Avg,
       "cfprSwEnvStatsHistPsuCtrlrInlet1Max": cfprSwEnvStatsHistPsuCtrlrInlet1Max,
       "cfprSwEnvStatsHistPsuCtrlrInlet1Min": cfprSwEnvStatsHistPsuCtrlrInlet1Min,
       "cfprSwEnvStatsHistPsuCtrlrInlet2": cfprSwEnvStatsHistPsuCtrlrInlet2,
       "cfprSwEnvStatsHistPsuCtrlrInlet2Avg": cfprSwEnvStatsHistPsuCtrlrInlet2Avg,
       "cfprSwEnvStatsHistPsuCtrlrInlet2Max": cfprSwEnvStatsHistPsuCtrlrInlet2Max,
       "cfprSwEnvStatsHistPsuCtrlrInlet2Min": cfprSwEnvStatsHistPsuCtrlrInlet2Min,
       "cfprSwEnvStatsHistSuspect": cfprSwEnvStatsHistSuspect,
       "cfprSwEnvStatsHistThresholded": cfprSwEnvStatsHistThresholded,
       "cfprSwEnvStatsHistTimeCollected": cfprSwEnvStatsHistTimeCollected,
       "cfprSwEthEstcEpTable": cfprSwEthEstcEpTable,
       "cfprSwEthEstcEpEntry": cfprSwEthEstcEpEntry,
       "cfprSwEthEstcEpInstanceId": cfprSwEthEstcEpInstanceId,
       "cfprSwEthEstcEpDn": cfprSwEthEstcEpDn,
       "cfprSwEthEstcEpRn": cfprSwEthEstcEpRn,
       "cfprSwEthEstcEpAdminSpeed": cfprSwEthEstcEpAdminSpeed,
       "cfprSwEthEstcEpAdminState": cfprSwEthEstcEpAdminState,
       "cfprSwEthEstcEpAggrPortId": cfprSwEthEstcEpAggrPortId,
       "cfprSwEthEstcEpBorderAggrPortId": cfprSwEthEstcEpBorderAggrPortId,
       "cfprSwEthEstcEpBorderPortId": cfprSwEthEstcEpBorderPortId,
       "cfprSwEthEstcEpBorderSlotId": cfprSwEthEstcEpBorderSlotId,
       "cfprSwEthEstcEpCdp": cfprSwEthEstcEpCdp,
       "cfprSwEthEstcEpChassisId": cfprSwEthEstcEpChassisId,
       "cfprSwEthEstcEpCosValue": cfprSwEthEstcEpCosValue,
       "cfprSwEthEstcEpEpDn": cfprSwEthEstcEpEpDn,
       "cfprSwEthEstcEpForgeMac": cfprSwEthEstcEpForgeMac,
       "cfprSwEthEstcEpIfRole": cfprSwEthEstcEpIfRole,
       "cfprSwEthEstcEpIfType": cfprSwEthEstcEpIfType,
       "cfprSwEthEstcEpLc": cfprSwEthEstcEpLc,
       "cfprSwEthEstcEpLocale": cfprSwEthEstcEpLocale,
       "cfprSwEthEstcEpName": cfprSwEthEstcEpName,
       "cfprSwEthEstcEpPcId": cfprSwEthEstcEpPcId,
       "cfprSwEthEstcEpPeerAggrPortId": cfprSwEthEstcEpPeerAggrPortId,
       "cfprSwEthEstcEpPeerChassisId": cfprSwEthEstcEpPeerChassisId,
       "cfprSwEthEstcEpPeerDn": cfprSwEthEstcEpPeerDn,
       "cfprSwEthEstcEpPeerPortId": cfprSwEthEstcEpPeerPortId,
       "cfprSwEthEstcEpPeerSlotId": cfprSwEthEstcEpPeerSlotId,
       "cfprSwEthEstcEpPinGroupName": cfprSwEthEstcEpPinGroupName,
       "cfprSwEthEstcEpPortId": cfprSwEthEstcEpPortId,
       "cfprSwEthEstcEpPortMode": cfprSwEthEstcEpPortMode,
       "cfprSwEthEstcEpPriorityFlowCtrl": cfprSwEthEstcEpPriorityFlowCtrl,
       "cfprSwEthEstcEpRecvFlowCtrl": cfprSwEthEstcEpRecvFlowCtrl,
       "cfprSwEthEstcEpSendFlowCtrl": cfprSwEthEstcEpSendFlowCtrl,
       "cfprSwEthEstcEpSlotId": cfprSwEthEstcEpSlotId,
       "cfprSwEthEstcEpSwitchId": cfprSwEthEstcEpSwitchId,
       "cfprSwEthEstcEpTransport": cfprSwEthEstcEpTransport,
       "cfprSwEthEstcEpType": cfprSwEthEstcEpType,
       "cfprSwEthEstcEpUplinkFailAction": cfprSwEthEstcEpUplinkFailAction,
       "cfprSwEthEstcPcTable": cfprSwEthEstcPcTable,
       "cfprSwEthEstcPcEntry": cfprSwEthEstcPcEntry,
       "cfprSwEthEstcPcInstanceId": cfprSwEthEstcPcInstanceId,
       "cfprSwEthEstcPcDn": cfprSwEthEstcPcDn,
       "cfprSwEthEstcPcRn": cfprSwEthEstcPcRn,
       "cfprSwEthEstcPcAdminSpeed": cfprSwEthEstcPcAdminSpeed,
       "cfprSwEthEstcPcAdminState": cfprSwEthEstcPcAdminState,
       "cfprSwEthEstcPcBorderAggrPortId": cfprSwEthEstcPcBorderAggrPortId,
       "cfprSwEthEstcPcBorderPortId": cfprSwEthEstcPcBorderPortId,
       "cfprSwEthEstcPcBorderSlotId": cfprSwEthEstcPcBorderSlotId,
       "cfprSwEthEstcPcCdp": cfprSwEthEstcPcCdp,
       "cfprSwEthEstcPcCosValue": cfprSwEthEstcPcCosValue,
       "cfprSwEthEstcPcEpDn": cfprSwEthEstcPcEpDn,
       "cfprSwEthEstcPcForgeMac": cfprSwEthEstcPcForgeMac,
       "cfprSwEthEstcPcIfRole": cfprSwEthEstcPcIfRole,
       "cfprSwEthEstcPcIfType": cfprSwEthEstcPcIfType,
       "cfprSwEthEstcPcLacpFastTimer": cfprSwEthEstcPcLacpFastTimer,
       "cfprSwEthEstcPcLacpSuspendIndividual": cfprSwEthEstcPcLacpSuspendIndividual,
       "cfprSwEthEstcPcLocale": cfprSwEthEstcPcLocale,
       "cfprSwEthEstcPcMonTrafDir": cfprSwEthEstcPcMonTrafDir,
       "cfprSwEthEstcPcName": cfprSwEthEstcPcName,
       "cfprSwEthEstcPcPeerDn": cfprSwEthEstcPcPeerDn,
       "cfprSwEthEstcPcPortId": cfprSwEthEstcPcPortId,
       "cfprSwEthEstcPcPortMode": cfprSwEthEstcPcPortMode,
       "cfprSwEthEstcPcPriorityFlowCtrl": cfprSwEthEstcPcPriorityFlowCtrl,
       "cfprSwEthEstcPcProtocol": cfprSwEthEstcPcProtocol,
       "cfprSwEthEstcPcRecvFlowCtrl": cfprSwEthEstcPcRecvFlowCtrl,
       "cfprSwEthEstcPcSendFlowCtrl": cfprSwEthEstcPcSendFlowCtrl,
       "cfprSwEthEstcPcSwitchId": cfprSwEthEstcPcSwitchId,
       "cfprSwEthEstcPcTransport": cfprSwEthEstcPcTransport,
       "cfprSwEthEstcPcType": cfprSwEthEstcPcType,
       "cfprSwEthEstcPcUplinkFailAction": cfprSwEthEstcPcUplinkFailAction,
       "cfprSwEthLanBorderTable": cfprSwEthLanBorderTable,
       "cfprSwEthLanBorderEntry": cfprSwEthLanBorderEntry,
       "cfprSwEthLanBorderInstanceId": cfprSwEthLanBorderInstanceId,
       "cfprSwEthLanBorderDn": cfprSwEthLanBorderDn,
       "cfprSwEthLanBorderRn": cfprSwEthLanBorderRn,
       "cfprSwEthLanBorderDeployFlag": cfprSwEthLanBorderDeployFlag,
       "cfprSwEthLanBorderFsmDescr": cfprSwEthLanBorderFsmDescr,
       "cfprSwEthLanBorderFsmFlags": cfprSwEthLanBorderFsmFlags,
       "cfprSwEthLanBorderFsmPrev": cfprSwEthLanBorderFsmPrev,
       "cfprSwEthLanBorderFsmProgr": cfprSwEthLanBorderFsmProgr,
       "cfprSwEthLanBorderFsmRmtInvErrCode": cfprSwEthLanBorderFsmRmtInvErrCode,
       "cfprSwEthLanBorderFsmRmtInvErrDescr": cfprSwEthLanBorderFsmRmtInvErrDescr,
       "cfprSwEthLanBorderFsmRmtInvRslt": cfprSwEthLanBorderFsmRmtInvRslt,
       "cfprSwEthLanBorderFsmStageDescr": cfprSwEthLanBorderFsmStageDescr,
       "cfprSwEthLanBorderFsmStamp": cfprSwEthLanBorderFsmStamp,
       "cfprSwEthLanBorderFsmStatus": cfprSwEthLanBorderFsmStatus,
       "cfprSwEthLanBorderFsmTry": cfprSwEthLanBorderFsmTry,
       "cfprSwEthLanBorderLocale": cfprSwEthLanBorderLocale,
       "cfprSwEthLanBorderName": cfprSwEthLanBorderName,
       "cfprSwEthLanBorderSwitchId": cfprSwEthLanBorderSwitchId,
       "cfprSwEthLanBorderTransport": cfprSwEthLanBorderTransport,
       "cfprSwEthLanBorderType": cfprSwEthLanBorderType,
       "cfprSwEthLanBorderUdldMsgInterval": cfprSwEthLanBorderUdldMsgInterval,
       "cfprSwEthLanBorderUdldRecoveryAction": cfprSwEthLanBorderUdldRecoveryAction,
       "cfprSwEthLanBorderFsmTable": cfprSwEthLanBorderFsmTable,
       "cfprSwEthLanBorderFsmEntry": cfprSwEthLanBorderFsmEntry,
       "cfprSwEthLanBorderFsmInstanceId": cfprSwEthLanBorderFsmInstanceId,
       "cfprSwEthLanBorderFsmDn": cfprSwEthLanBorderFsmDn,
       "cfprSwEthLanBorderFsmRn": cfprSwEthLanBorderFsmRn,
       "cfprSwEthLanBorderFsmCompletionTime": cfprSwEthLanBorderFsmCompletionTime,
       "cfprSwEthLanBorderFsmCurrentFsm": cfprSwEthLanBorderFsmCurrentFsm,
       "cfprSwEthLanBorderFsmDescrData": cfprSwEthLanBorderFsmDescrData,
       "cfprSwEthLanBorderFsmFsmStatus": cfprSwEthLanBorderFsmFsmStatus,
       "cfprSwEthLanBorderFsmProgress": cfprSwEthLanBorderFsmProgress,
       "cfprSwEthLanBorderFsmRmtErrCode": cfprSwEthLanBorderFsmRmtErrCode,
       "cfprSwEthLanBorderFsmRmtErrDescr": cfprSwEthLanBorderFsmRmtErrDescr,
       "cfprSwEthLanBorderFsmRmtRslt": cfprSwEthLanBorderFsmRmtRslt,
       "cfprSwEthLanBorderFsmStageTable": cfprSwEthLanBorderFsmStageTable,
       "cfprSwEthLanBorderFsmStageEntry": cfprSwEthLanBorderFsmStageEntry,
       "cfprSwEthLanBorderFsmStageInstanceId": cfprSwEthLanBorderFsmStageInstanceId,
       "cfprSwEthLanBorderFsmStageDn": cfprSwEthLanBorderFsmStageDn,
       "cfprSwEthLanBorderFsmStageRn": cfprSwEthLanBorderFsmStageRn,
       "cfprSwEthLanBorderFsmStageDescrData": cfprSwEthLanBorderFsmStageDescrData,
       "cfprSwEthLanBorderFsmStageLastUpdateTime": cfprSwEthLanBorderFsmStageLastUpdateTime,
       "cfprSwEthLanBorderFsmStageName": cfprSwEthLanBorderFsmStageName,
       "cfprSwEthLanBorderFsmStageOrder": cfprSwEthLanBorderFsmStageOrder,
       "cfprSwEthLanBorderFsmStageRetry": cfprSwEthLanBorderFsmStageRetry,
       "cfprSwEthLanBorderFsmStageStageStatus": cfprSwEthLanBorderFsmStageStageStatus,
       "cfprSwEthLanBorderFsmTaskTable": cfprSwEthLanBorderFsmTaskTable,
       "cfprSwEthLanBorderFsmTaskEntry": cfprSwEthLanBorderFsmTaskEntry,
       "cfprSwEthLanBorderFsmTaskInstanceId": cfprSwEthLanBorderFsmTaskInstanceId,
       "cfprSwEthLanBorderFsmTaskDn": cfprSwEthLanBorderFsmTaskDn,
       "cfprSwEthLanBorderFsmTaskRn": cfprSwEthLanBorderFsmTaskRn,
       "cfprSwEthLanBorderFsmTaskCompletion": cfprSwEthLanBorderFsmTaskCompletion,
       "cfprSwEthLanBorderFsmTaskFlags": cfprSwEthLanBorderFsmTaskFlags,
       "cfprSwEthLanBorderFsmTaskItem": cfprSwEthLanBorderFsmTaskItem,
       "cfprSwEthLanBorderFsmTaskSeqId": cfprSwEthLanBorderFsmTaskSeqId,
       "cfprSwEthLanEpTable": cfprSwEthLanEpTable,
       "cfprSwEthLanEpEntry": cfprSwEthLanEpEntry,
       "cfprSwEthLanEpInstanceId": cfprSwEthLanEpInstanceId,
       "cfprSwEthLanEpDn": cfprSwEthLanEpDn,
       "cfprSwEthLanEpRn": cfprSwEthLanEpRn,
       "cfprSwEthLanEpAdminSpeed": cfprSwEthLanEpAdminSpeed,
       "cfprSwEthLanEpAdminState": cfprSwEthLanEpAdminState,
       "cfprSwEthLanEpAggrPortId": cfprSwEthLanEpAggrPortId,
       "cfprSwEthLanEpChassisId": cfprSwEthLanEpChassisId,
       "cfprSwEthLanEpDtagVlan": cfprSwEthLanEpDtagVlan,
       "cfprSwEthLanEpEpDn": cfprSwEthLanEpEpDn,
       "cfprSwEthLanEpIfRole": cfprSwEthLanEpIfRole,
       "cfprSwEthLanEpIfType": cfprSwEthLanEpIfType,
       "cfprSwEthLanEpLc": cfprSwEthLanEpLc,
       "cfprSwEthLanEpLocale": cfprSwEthLanEpLocale,
       "cfprSwEthLanEpName": cfprSwEthLanEpName,
       "cfprSwEthLanEpPcId": cfprSwEthLanEpPcId,
       "cfprSwEthLanEpPeerAggrPortId": cfprSwEthLanEpPeerAggrPortId,
       "cfprSwEthLanEpPeerChassisId": cfprSwEthLanEpPeerChassisId,
       "cfprSwEthLanEpPeerDn": cfprSwEthLanEpPeerDn,
       "cfprSwEthLanEpPeerPortId": cfprSwEthLanEpPeerPortId,
       "cfprSwEthLanEpPeerSlotId": cfprSwEthLanEpPeerSlotId,
       "cfprSwEthLanEpPortId": cfprSwEthLanEpPortId,
       "cfprSwEthLanEpPriorityFlowCtrl": cfprSwEthLanEpPriorityFlowCtrl,
       "cfprSwEthLanEpRecvFlowCtrl": cfprSwEthLanEpRecvFlowCtrl,
       "cfprSwEthLanEpSendFlowCtrl": cfprSwEthLanEpSendFlowCtrl,
       "cfprSwEthLanEpSlotId": cfprSwEthLanEpSlotId,
       "cfprSwEthLanEpSwitchId": cfprSwEthLanEpSwitchId,
       "cfprSwEthLanEpTransport": cfprSwEthLanEpTransport,
       "cfprSwEthLanEpType": cfprSwEthLanEpType,
       "cfprSwEthLanEpUdldAdminState": cfprSwEthLanEpUdldAdminState,
       "cfprSwEthLanEpUdldMode": cfprSwEthLanEpUdldMode,
       "cfprSwEthLanEpAdminDuplex": cfprSwEthLanEpAdminDuplex,
       "cfprSwEthLanEpAutoNeg": cfprSwEthLanEpAutoNeg,
       "cfprSwEthLanEpHashAlg": cfprSwEthLanEpHashAlg,
       "cfprSwEthLanEpInlineState": cfprSwEthLanEpInlineState,
       "cfprSwEthLanEpPcMode": cfprSwEthLanEpPcMode,
       "cfprSwEthLanEpPcModeState": cfprSwEthLanEpPcModeState,
       "cfprSwEthLanEpQosPrio": cfprSwEthLanEpQosPrio,
       "cfprSwEthLanEpLldp": cfprSwEthLanEpLldp,
       "cfprSwEthLanEpAllowAneg": cfprSwEthLanEpAllowAneg,
       "cfprSwEthLanEpDebounceTime": cfprSwEthLanEpDebounceTime,
       "cfprSwEthLanEpServiceState": cfprSwEthLanEpServiceState,
       "cfprSwEthLanMonTable": cfprSwEthLanMonTable,
       "cfprSwEthLanMonEntry": cfprSwEthLanMonEntry,
       "cfprSwEthLanMonInstanceId": cfprSwEthLanMonInstanceId,
       "cfprSwEthLanMonDn": cfprSwEthLanMonDn,
       "cfprSwEthLanMonRn": cfprSwEthLanMonRn,
       "cfprSwEthLanMonLocale": cfprSwEthLanMonLocale,
       "cfprSwEthLanMonName": cfprSwEthLanMonName,
       "cfprSwEthLanMonSwitchId": cfprSwEthLanMonSwitchId,
       "cfprSwEthLanMonTransport": cfprSwEthLanMonTransport,
       "cfprSwEthLanMonType": cfprSwEthLanMonType,
       "cfprSwEthLanPcTable": cfprSwEthLanPcTable,
       "cfprSwEthLanPcEntry": cfprSwEthLanPcEntry,
       "cfprSwEthLanPcInstanceId": cfprSwEthLanPcInstanceId,
       "cfprSwEthLanPcDn": cfprSwEthLanPcDn,
       "cfprSwEthLanPcRn": cfprSwEthLanPcRn,
       "cfprSwEthLanPcAdminSpeed": cfprSwEthLanPcAdminSpeed,
       "cfprSwEthLanPcAdminState": cfprSwEthLanPcAdminState,
       "cfprSwEthLanPcClusterName": cfprSwEthLanPcClusterName,
       "cfprSwEthLanPcDtagVlan": cfprSwEthLanPcDtagVlan,
       "cfprSwEthLanPcEpDn": cfprSwEthLanPcEpDn,
       "cfprSwEthLanPcIfRole": cfprSwEthLanPcIfRole,
       "cfprSwEthLanPcIfType": cfprSwEthLanPcIfType,
       "cfprSwEthLanPcLacpFastTimer": cfprSwEthLanPcLacpFastTimer,
       "cfprSwEthLanPcLacpSuspendIndividual": cfprSwEthLanPcLacpSuspendIndividual,
       "cfprSwEthLanPcLocale": cfprSwEthLanPcLocale,
       "cfprSwEthLanPcMonTrafDir": cfprSwEthLanPcMonTrafDir,
       "cfprSwEthLanPcName": cfprSwEthLanPcName,
       "cfprSwEthLanPcPeerDn": cfprSwEthLanPcPeerDn,
       "cfprSwEthLanPcPortId": cfprSwEthLanPcPortId,
       "cfprSwEthLanPcPriorityFlowCtrl": cfprSwEthLanPcPriorityFlowCtrl,
       "cfprSwEthLanPcRecvFlowCtrl": cfprSwEthLanPcRecvFlowCtrl,
       "cfprSwEthLanPcSendFlowCtrl": cfprSwEthLanPcSendFlowCtrl,
       "cfprSwEthLanPcSpannedCluster": cfprSwEthLanPcSpannedCluster,
       "cfprSwEthLanPcSwitchId": cfprSwEthLanPcSwitchId,
       "cfprSwEthLanPcTransport": cfprSwEthLanPcTransport,
       "cfprSwEthLanPcType": cfprSwEthLanPcType,
       "cfprSwEthLanPcCluChassisId": cfprSwEthLanPcCluChassisId,
       "cfprSwEthLanPcLacpDetach": cfprSwEthLanPcLacpDetach,
       "cfprSwEthLanPcAdminDuplex": cfprSwEthLanPcAdminDuplex,
       "cfprSwEthLanPcAutoNeg": cfprSwEthLanPcAutoNeg,
       "cfprSwEthLanPcHashAlg": cfprSwEthLanPcHashAlg,
       "cfprSwEthLanPcInlineState": cfprSwEthLanPcInlineState,
       "cfprSwEthLanPcPcMode": cfprSwEthLanPcPcMode,
       "cfprSwEthLanPcPcModeState": cfprSwEthLanPcPcModeState,
       "cfprSwEthLanPcQosPrio": cfprSwEthLanPcQosPrio,
       "cfprSwEthLanPcLldp": cfprSwEthLanPcLldp,
       "cfprSwEthLanPcServiceState": cfprSwEthLanPcServiceState,
       "cfprSwEthMonTable": cfprSwEthMonTable,
       "cfprSwEthMonEntry": cfprSwEthMonEntry,
       "cfprSwEthMonInstanceId": cfprSwEthMonInstanceId,
       "cfprSwEthMonDn": cfprSwEthMonDn,
       "cfprSwEthMonRn": cfprSwEthMonRn,
       "cfprSwEthMonAdminState": cfprSwEthMonAdminState,
       "cfprSwEthMonFsmDescr": cfprSwEthMonFsmDescr,
       "cfprSwEthMonFsmPrev": cfprSwEthMonFsmPrev,
       "cfprSwEthMonFsmProgr": cfprSwEthMonFsmProgr,
       "cfprSwEthMonFsmRmtInvErrCode": cfprSwEthMonFsmRmtInvErrCode,
       "cfprSwEthMonFsmRmtInvErrDescr": cfprSwEthMonFsmRmtInvErrDescr,
       "cfprSwEthMonFsmRmtInvRslt": cfprSwEthMonFsmRmtInvRslt,
       "cfprSwEthMonFsmStageDescr": cfprSwEthMonFsmStageDescr,
       "cfprSwEthMonFsmStamp": cfprSwEthMonFsmStamp,
       "cfprSwEthMonFsmStatus": cfprSwEthMonFsmStatus,
       "cfprSwEthMonFsmTry": cfprSwEthMonFsmTry,
       "cfprSwEthMonHasLastDest": cfprSwEthMonHasLastDest,
       "cfprSwEthMonLifeCycle": cfprSwEthMonLifeCycle,
       "cfprSwEthMonName": cfprSwEthMonName,
       "cfprSwEthMonPeerDn": cfprSwEthMonPeerDn,
       "cfprSwEthMonSession": cfprSwEthMonSession,
       "cfprSwEthMonSwitchId": cfprSwEthMonSwitchId,
       "cfprSwEthMonTransport": cfprSwEthMonTransport,
       "cfprSwEthMonType": cfprSwEthMonType,
       "cfprSwEthMonDestEpTable": cfprSwEthMonDestEpTable,
       "cfprSwEthMonDestEpEntry": cfprSwEthMonDestEpEntry,
       "cfprSwEthMonDestEpInstanceId": cfprSwEthMonDestEpInstanceId,
       "cfprSwEthMonDestEpDn": cfprSwEthMonDestEpDn,
       "cfprSwEthMonDestEpRn": cfprSwEthMonDestEpRn,
       "cfprSwEthMonDestEpAdminSpeed": cfprSwEthMonDestEpAdminSpeed,
       "cfprSwEthMonDestEpAdminState": cfprSwEthMonDestEpAdminState,
       "cfprSwEthMonDestEpAggrPortId": cfprSwEthMonDestEpAggrPortId,
       "cfprSwEthMonDestEpChassisId": cfprSwEthMonDestEpChassisId,
       "cfprSwEthMonDestEpEpDn": cfprSwEthMonDestEpEpDn,
       "cfprSwEthMonDestEpIfRole": cfprSwEthMonDestEpIfRole,
       "cfprSwEthMonDestEpIfType": cfprSwEthMonDestEpIfType,
       "cfprSwEthMonDestEpLc": cfprSwEthMonDestEpLc,
       "cfprSwEthMonDestEpLocale": cfprSwEthMonDestEpLocale,
       "cfprSwEthMonDestEpName": cfprSwEthMonDestEpName,
       "cfprSwEthMonDestEpPeerAggrPortId": cfprSwEthMonDestEpPeerAggrPortId,
       "cfprSwEthMonDestEpPeerChassisId": cfprSwEthMonDestEpPeerChassisId,
       "cfprSwEthMonDestEpPeerDn": cfprSwEthMonDestEpPeerDn,
       "cfprSwEthMonDestEpPeerPortId": cfprSwEthMonDestEpPeerPortId,
       "cfprSwEthMonDestEpPeerSlotId": cfprSwEthMonDestEpPeerSlotId,
       "cfprSwEthMonDestEpPortId": cfprSwEthMonDestEpPortId,
       "cfprSwEthMonDestEpSlotId": cfprSwEthMonDestEpSlotId,
       "cfprSwEthMonDestEpSwitchId": cfprSwEthMonDestEpSwitchId,
       "cfprSwEthMonDestEpTransport": cfprSwEthMonDestEpTransport,
       "cfprSwEthMonDestEpType": cfprSwEthMonDestEpType,
       "cfprSwEthMonFsmTable": cfprSwEthMonFsmTable,
       "cfprSwEthMonFsmEntry": cfprSwEthMonFsmEntry,
       "cfprSwEthMonFsmInstanceId": cfprSwEthMonFsmInstanceId,
       "cfprSwEthMonFsmDn": cfprSwEthMonFsmDn,
       "cfprSwEthMonFsmRn": cfprSwEthMonFsmRn,
       "cfprSwEthMonFsmCompletionTime": cfprSwEthMonFsmCompletionTime,
       "cfprSwEthMonFsmCurrentFsm": cfprSwEthMonFsmCurrentFsm,
       "cfprSwEthMonFsmDescrData": cfprSwEthMonFsmDescrData,
       "cfprSwEthMonFsmFsmStatus": cfprSwEthMonFsmFsmStatus,
       "cfprSwEthMonFsmProgress": cfprSwEthMonFsmProgress,
       "cfprSwEthMonFsmRmtErrCode": cfprSwEthMonFsmRmtErrCode,
       "cfprSwEthMonFsmRmtErrDescr": cfprSwEthMonFsmRmtErrDescr,
       "cfprSwEthMonFsmRmtRslt": cfprSwEthMonFsmRmtRslt,
       "cfprSwEthMonFsmStageTable": cfprSwEthMonFsmStageTable,
       "cfprSwEthMonFsmStageEntry": cfprSwEthMonFsmStageEntry,
       "cfprSwEthMonFsmStageInstanceId": cfprSwEthMonFsmStageInstanceId,
       "cfprSwEthMonFsmStageDn": cfprSwEthMonFsmStageDn,
       "cfprSwEthMonFsmStageRn": cfprSwEthMonFsmStageRn,
       "cfprSwEthMonFsmStageDescrData": cfprSwEthMonFsmStageDescrData,
       "cfprSwEthMonFsmStageLastUpdateTime": cfprSwEthMonFsmStageLastUpdateTime,
       "cfprSwEthMonFsmStageName": cfprSwEthMonFsmStageName,
       "cfprSwEthMonFsmStageOrder": cfprSwEthMonFsmStageOrder,
       "cfprSwEthMonFsmStageRetry": cfprSwEthMonFsmStageRetry,
       "cfprSwEthMonFsmStageStageStatus": cfprSwEthMonFsmStageStageStatus,
       "cfprSwEthMonFsmTaskTable": cfprSwEthMonFsmTaskTable,
       "cfprSwEthMonFsmTaskEntry": cfprSwEthMonFsmTaskEntry,
       "cfprSwEthMonFsmTaskInstanceId": cfprSwEthMonFsmTaskInstanceId,
       "cfprSwEthMonFsmTaskDn": cfprSwEthMonFsmTaskDn,
       "cfprSwEthMonFsmTaskRn": cfprSwEthMonFsmTaskRn,
       "cfprSwEthMonFsmTaskCompletion": cfprSwEthMonFsmTaskCompletion,
       "cfprSwEthMonFsmTaskFlags": cfprSwEthMonFsmTaskFlags,
       "cfprSwEthMonFsmTaskItem": cfprSwEthMonFsmTaskItem,
       "cfprSwEthMonFsmTaskSeqId": cfprSwEthMonFsmTaskSeqId,
       "cfprSwEthMonSrcEpTable": cfprSwEthMonSrcEpTable,
       "cfprSwEthMonSrcEpEntry": cfprSwEthMonSrcEpEntry,
       "cfprSwEthMonSrcEpInstanceId": cfprSwEthMonSrcEpInstanceId,
       "cfprSwEthMonSrcEpDn": cfprSwEthMonSrcEpDn,
       "cfprSwEthMonSrcEpRn": cfprSwEthMonSrcEpRn,
       "cfprSwEthMonSrcEpAdminState": cfprSwEthMonSrcEpAdminState,
       "cfprSwEthMonSrcEpAggrPortId": cfprSwEthMonSrcEpAggrPortId,
       "cfprSwEthMonSrcEpChassisId": cfprSwEthMonSrcEpChassisId,
       "cfprSwEthMonSrcEpEpDn": cfprSwEthMonSrcEpEpDn,
       "cfprSwEthMonSrcEpIfRole": cfprSwEthMonSrcEpIfRole,
       "cfprSwEthMonSrcEpIfType": cfprSwEthMonSrcEpIfType,
       "cfprSwEthMonSrcEpLc": cfprSwEthMonSrcEpLc,
       "cfprSwEthMonSrcEpLocale": cfprSwEthMonSrcEpLocale,
       "cfprSwEthMonSrcEpMonTrafDir": cfprSwEthMonSrcEpMonTrafDir,
       "cfprSwEthMonSrcEpName": cfprSwEthMonSrcEpName,
       "cfprSwEthMonSrcEpPeerAggrPortId": cfprSwEthMonSrcEpPeerAggrPortId,
       "cfprSwEthMonSrcEpPeerChassisId": cfprSwEthMonSrcEpPeerChassisId,
       "cfprSwEthMonSrcEpPeerDn": cfprSwEthMonSrcEpPeerDn,
       "cfprSwEthMonSrcEpPeerPortId": cfprSwEthMonSrcEpPeerPortId,
       "cfprSwEthMonSrcEpPeerSlotId": cfprSwEthMonSrcEpPeerSlotId,
       "cfprSwEthMonSrcEpPortId": cfprSwEthMonSrcEpPortId,
       "cfprSwEthMonSrcEpSlotId": cfprSwEthMonSrcEpSlotId,
       "cfprSwEthMonSrcEpSwitchId": cfprSwEthMonSrcEpSwitchId,
       "cfprSwEthMonSrcEpTransport": cfprSwEthMonSrcEpTransport,
       "cfprSwEthMonSrcEpType": cfprSwEthMonSrcEpType,
       "cfprSwEthTargetEpTable": cfprSwEthTargetEpTable,
       "cfprSwEthTargetEpEntry": cfprSwEthTargetEpEntry,
       "cfprSwEthTargetEpInstanceId": cfprSwEthTargetEpInstanceId,
       "cfprSwEthTargetEpDn": cfprSwEthTargetEpDn,
       "cfprSwEthTargetEpRn": cfprSwEthTargetEpRn,
       "cfprSwEthTargetEpAdminState": cfprSwEthTargetEpAdminState,
       "cfprSwEthTargetEpAggrPortId": cfprSwEthTargetEpAggrPortId,
       "cfprSwEthTargetEpChassisId": cfprSwEthTargetEpChassisId,
       "cfprSwEthTargetEpEpDn": cfprSwEthTargetEpEpDn,
       "cfprSwEthTargetEpFltAggr": cfprSwEthTargetEpFltAggr,
       "cfprSwEthTargetEpIfRole": cfprSwEthTargetEpIfRole,
       "cfprSwEthTargetEpIfType": cfprSwEthTargetEpIfType,
       "cfprSwEthTargetEpLicGP": cfprSwEthTargetEpLicGP,
       "cfprSwEthTargetEpLicState": cfprSwEthTargetEpLicState,
       "cfprSwEthTargetEpLocale": cfprSwEthTargetEpLocale,
       "cfprSwEthTargetEpMacAddress": cfprSwEthTargetEpMacAddress,
       "cfprSwEthTargetEpName": cfprSwEthTargetEpName,
       "cfprSwEthTargetEpOperState": cfprSwEthTargetEpOperState,
       "cfprSwEthTargetEpOperStateReason": cfprSwEthTargetEpOperStateReason,
       "cfprSwEthTargetEpPeerAggrPortId": cfprSwEthTargetEpPeerAggrPortId,
       "cfprSwEthTargetEpPeerChassisId": cfprSwEthTargetEpPeerChassisId,
       "cfprSwEthTargetEpPeerDn": cfprSwEthTargetEpPeerDn,
       "cfprSwEthTargetEpPeerPortId": cfprSwEthTargetEpPeerPortId,
       "cfprSwEthTargetEpPeerSlotId": cfprSwEthTargetEpPeerSlotId,
       "cfprSwEthTargetEpPortId": cfprSwEthTargetEpPortId,
       "cfprSwEthTargetEpSlotId": cfprSwEthTargetEpSlotId,
       "cfprSwEthTargetEpSwitchId": cfprSwEthTargetEpSwitchId,
       "cfprSwEthTargetEpTransport": cfprSwEthTargetEpTransport,
       "cfprSwEthTargetEpType": cfprSwEthTargetEpType,
       "cfprSwEthTargetEpWarnings": cfprSwEthTargetEpWarnings,
       "cfprSwExtUtilityTable": cfprSwExtUtilityTable,
       "cfprSwExtUtilityEntry": cfprSwExtUtilityEntry,
       "cfprSwExtUtilityInstanceId": cfprSwExtUtilityInstanceId,
       "cfprSwExtUtilityDn": cfprSwExtUtilityDn,
       "cfprSwExtUtilityRn": cfprSwExtUtilityRn,
       "cfprSwExtUtilityConfMode": cfprSwExtUtilityConfMode,
       "cfprSwExtUtilityFsmDescr": cfprSwExtUtilityFsmDescr,
       "cfprSwExtUtilityFsmPrev": cfprSwExtUtilityFsmPrev,
       "cfprSwExtUtilityFsmProgr": cfprSwExtUtilityFsmProgr,
       "cfprSwExtUtilityFsmRmtInvErrCode": cfprSwExtUtilityFsmRmtInvErrCode,
       "cfprSwExtUtilityFsmRmtInvErrDescr": cfprSwExtUtilityFsmRmtInvErrDescr,
       "cfprSwExtUtilityFsmRmtInvRslt": cfprSwExtUtilityFsmRmtInvRslt,
       "cfprSwExtUtilityFsmStageDescr": cfprSwExtUtilityFsmStageDescr,
       "cfprSwExtUtilityFsmStamp": cfprSwExtUtilityFsmStamp,
       "cfprSwExtUtilityFsmStatus": cfprSwExtUtilityFsmStatus,
       "cfprSwExtUtilityFsmTry": cfprSwExtUtilityFsmTry,
       "cfprSwExtUtilitySwitchId": cfprSwExtUtilitySwitchId,
       "cfprSwExtUtilityFsmTable": cfprSwExtUtilityFsmTable,
       "cfprSwExtUtilityFsmEntry": cfprSwExtUtilityFsmEntry,
       "cfprSwExtUtilityFsmInstanceId": cfprSwExtUtilityFsmInstanceId,
       "cfprSwExtUtilityFsmDn": cfprSwExtUtilityFsmDn,
       "cfprSwExtUtilityFsmRn": cfprSwExtUtilityFsmRn,
       "cfprSwExtUtilityFsmCompletionTime": cfprSwExtUtilityFsmCompletionTime,
       "cfprSwExtUtilityFsmCurrentFsm": cfprSwExtUtilityFsmCurrentFsm,
       "cfprSwExtUtilityFsmDescrData": cfprSwExtUtilityFsmDescrData,
       "cfprSwExtUtilityFsmFsmStatus": cfprSwExtUtilityFsmFsmStatus,
       "cfprSwExtUtilityFsmProgress": cfprSwExtUtilityFsmProgress,
       "cfprSwExtUtilityFsmRmtErrCode": cfprSwExtUtilityFsmRmtErrCode,
       "cfprSwExtUtilityFsmRmtErrDescr": cfprSwExtUtilityFsmRmtErrDescr,
       "cfprSwExtUtilityFsmRmtRslt": cfprSwExtUtilityFsmRmtRslt,
       "cfprSwExtUtilityFsmStageTable": cfprSwExtUtilityFsmStageTable,
       "cfprSwExtUtilityFsmStageEntry": cfprSwExtUtilityFsmStageEntry,
       "cfprSwExtUtilityFsmStageInstanceId": cfprSwExtUtilityFsmStageInstanceId,
       "cfprSwExtUtilityFsmStageDn": cfprSwExtUtilityFsmStageDn,
       "cfprSwExtUtilityFsmStageRn": cfprSwExtUtilityFsmStageRn,
       "cfprSwExtUtilityFsmStageDescrData": cfprSwExtUtilityFsmStageDescrData,
       "cfprSwExtUtilityFsmStageLastUpdateTime": cfprSwExtUtilityFsmStageLastUpdateTime,
       "cfprSwExtUtilityFsmStageName": cfprSwExtUtilityFsmStageName,
       "cfprSwExtUtilityFsmStageOrder": cfprSwExtUtilityFsmStageOrder,
       "cfprSwExtUtilityFsmStageRetry": cfprSwExtUtilityFsmStageRetry,
       "cfprSwExtUtilityFsmStageStageStatus": cfprSwExtUtilityFsmStageStageStatus,
       "cfprSwExtUtilityFsmTaskTable": cfprSwExtUtilityFsmTaskTable,
       "cfprSwExtUtilityFsmTaskEntry": cfprSwExtUtilityFsmTaskEntry,
       "cfprSwExtUtilityFsmTaskInstanceId": cfprSwExtUtilityFsmTaskInstanceId,
       "cfprSwExtUtilityFsmTaskDn": cfprSwExtUtilityFsmTaskDn,
       "cfprSwExtUtilityFsmTaskRn": cfprSwExtUtilityFsmTaskRn,
       "cfprSwExtUtilityFsmTaskCompletion": cfprSwExtUtilityFsmTaskCompletion,
       "cfprSwExtUtilityFsmTaskFlags": cfprSwExtUtilityFsmTaskFlags,
       "cfprSwExtUtilityFsmTaskItem": cfprSwExtUtilityFsmTaskItem,
       "cfprSwExtUtilityFsmTaskSeqId": cfprSwExtUtilityFsmTaskSeqId,
       "cfprSwFabricZoneNsTable": cfprSwFabricZoneNsTable,
       "cfprSwFabricZoneNsEntry": cfprSwFabricZoneNsEntry,
       "cfprSwFabricZoneNsInstanceId": cfprSwFabricZoneNsInstanceId,
       "cfprSwFabricZoneNsDn": cfprSwFabricZoneNsDn,
       "cfprSwFabricZoneNsRn": cfprSwFabricZoneNsRn,
       "cfprSwFabricZoneNsAllocStatus": cfprSwFabricZoneNsAllocStatus,
       "cfprSwFabricZoneNsLimit": cfprSwFabricZoneNsLimit,
       "cfprSwFabricZoneNsSwitchId": cfprSwFabricZoneNsSwitchId,
       "cfprSwFabricZoneNsZoneCount": cfprSwFabricZoneNsZoneCount,
       "cfprSwFabricZoneNsOverrideTable": cfprSwFabricZoneNsOverrideTable,
       "cfprSwFabricZoneNsOverrideEntry": cfprSwFabricZoneNsOverrideEntry,
       "cfprSwFabricZoneNsOverrideInstanceId": cfprSwFabricZoneNsOverrideInstanceId,
       "cfprSwFabricZoneNsOverrideDn": cfprSwFabricZoneNsOverrideDn,
       "cfprSwFabricZoneNsOverrideRn": cfprSwFabricZoneNsOverrideRn,
       "cfprSwFabricZoneNsOverrideLimit": cfprSwFabricZoneNsOverrideLimit,
       "cfprSwFcSanBorderTable": cfprSwFcSanBorderTable,
       "cfprSwFcSanBorderEntry": cfprSwFcSanBorderEntry,
       "cfprSwFcSanBorderInstanceId": cfprSwFcSanBorderInstanceId,
       "cfprSwFcSanBorderDn": cfprSwFcSanBorderDn,
       "cfprSwFcSanBorderRn": cfprSwFcSanBorderRn,
       "cfprSwFcSanBorderFsmDescr": cfprSwFcSanBorderFsmDescr,
       "cfprSwFcSanBorderFsmPrev": cfprSwFcSanBorderFsmPrev,
       "cfprSwFcSanBorderFsmProgr": cfprSwFcSanBorderFsmProgr,
       "cfprSwFcSanBorderFsmRmtInvErrCode": cfprSwFcSanBorderFsmRmtInvErrCode,
       "cfprSwFcSanBorderFsmRmtInvErrDescr": cfprSwFcSanBorderFsmRmtInvErrDescr,
       "cfprSwFcSanBorderFsmRmtInvRslt": cfprSwFcSanBorderFsmRmtInvRslt,
       "cfprSwFcSanBorderFsmStageDescr": cfprSwFcSanBorderFsmStageDescr,
       "cfprSwFcSanBorderFsmStamp": cfprSwFcSanBorderFsmStamp,
       "cfprSwFcSanBorderFsmStatus": cfprSwFcSanBorderFsmStatus,
       "cfprSwFcSanBorderFsmTry": cfprSwFcSanBorderFsmTry,
       "cfprSwFcSanBorderLocale": cfprSwFcSanBorderLocale,
       "cfprSwFcSanBorderName": cfprSwFcSanBorderName,
       "cfprSwFcSanBorderSwitchId": cfprSwFcSanBorderSwitchId,
       "cfprSwFcSanBorderTransport": cfprSwFcSanBorderTransport,
       "cfprSwFcSanBorderType": cfprSwFcSanBorderType,
       "cfprSwFcSanBorderUplinkTrunking": cfprSwFcSanBorderUplinkTrunking,
       "cfprSwFcSanBorderFsmTable": cfprSwFcSanBorderFsmTable,
       "cfprSwFcSanBorderFsmEntry": cfprSwFcSanBorderFsmEntry,
       "cfprSwFcSanBorderFsmInstanceId": cfprSwFcSanBorderFsmInstanceId,
       "cfprSwFcSanBorderFsmDn": cfprSwFcSanBorderFsmDn,
       "cfprSwFcSanBorderFsmRn": cfprSwFcSanBorderFsmRn,
       "cfprSwFcSanBorderFsmCompletionTime": cfprSwFcSanBorderFsmCompletionTime,
       "cfprSwFcSanBorderFsmCurrentFsm": cfprSwFcSanBorderFsmCurrentFsm,
       "cfprSwFcSanBorderFsmDescrData": cfprSwFcSanBorderFsmDescrData,
       "cfprSwFcSanBorderFsmFsmStatus": cfprSwFcSanBorderFsmFsmStatus,
       "cfprSwFcSanBorderFsmProgress": cfprSwFcSanBorderFsmProgress,
       "cfprSwFcSanBorderFsmRmtErrCode": cfprSwFcSanBorderFsmRmtErrCode,
       "cfprSwFcSanBorderFsmRmtErrDescr": cfprSwFcSanBorderFsmRmtErrDescr,
       "cfprSwFcSanBorderFsmRmtRslt": cfprSwFcSanBorderFsmRmtRslt,
       "cfprSwFcSanBorderFsmStageTable": cfprSwFcSanBorderFsmStageTable,
       "cfprSwFcSanBorderFsmStageEntry": cfprSwFcSanBorderFsmStageEntry,
       "cfprSwFcSanBorderFsmStageInstanceId": cfprSwFcSanBorderFsmStageInstanceId,
       "cfprSwFcSanBorderFsmStageDn": cfprSwFcSanBorderFsmStageDn,
       "cfprSwFcSanBorderFsmStageRn": cfprSwFcSanBorderFsmStageRn,
       "cfprSwFcSanBorderFsmStageDescrData": cfprSwFcSanBorderFsmStageDescrData,
       "cfprSwFcSanBorderFsmStageLastUpdateTime": cfprSwFcSanBorderFsmStageLastUpdateTime,
       "cfprSwFcSanBorderFsmStageName": cfprSwFcSanBorderFsmStageName,
       "cfprSwFcSanBorderFsmStageOrder": cfprSwFcSanBorderFsmStageOrder,
       "cfprSwFcSanBorderFsmStageRetry": cfprSwFcSanBorderFsmStageRetry,
       "cfprSwFcSanBorderFsmStageStageStatus": cfprSwFcSanBorderFsmStageStageStatus,
       "cfprSwFcSanBorderFsmTaskTable": cfprSwFcSanBorderFsmTaskTable,
       "cfprSwFcSanBorderFsmTaskEntry": cfprSwFcSanBorderFsmTaskEntry,
       "cfprSwFcSanBorderFsmTaskInstanceId": cfprSwFcSanBorderFsmTaskInstanceId,
       "cfprSwFcSanBorderFsmTaskDn": cfprSwFcSanBorderFsmTaskDn,
       "cfprSwFcSanBorderFsmTaskRn": cfprSwFcSanBorderFsmTaskRn,
       "cfprSwFcSanBorderFsmTaskCompletion": cfprSwFcSanBorderFsmTaskCompletion,
       "cfprSwFcSanBorderFsmTaskFlags": cfprSwFcSanBorderFsmTaskFlags,
       "cfprSwFcSanBorderFsmTaskItem": cfprSwFcSanBorderFsmTaskItem,
       "cfprSwFcSanBorderFsmTaskSeqId": cfprSwFcSanBorderFsmTaskSeqId,
       "cfprSwFcSanEpTable": cfprSwFcSanEpTable,
       "cfprSwFcSanEpEntry": cfprSwFcSanEpEntry,
       "cfprSwFcSanEpInstanceId": cfprSwFcSanEpInstanceId,
       "cfprSwFcSanEpDn": cfprSwFcSanEpDn,
       "cfprSwFcSanEpRn": cfprSwFcSanEpRn,
       "cfprSwFcSanEpAdminSpeed": cfprSwFcSanEpAdminSpeed,
       "cfprSwFcSanEpAdminState": cfprSwFcSanEpAdminState,
       "cfprSwFcSanEpAggrPortId": cfprSwFcSanEpAggrPortId,
       "cfprSwFcSanEpChassisId": cfprSwFcSanEpChassisId,
       "cfprSwFcSanEpEpDn": cfprSwFcSanEpEpDn,
       "cfprSwFcSanEpFillPattern": cfprSwFcSanEpFillPattern,
       "cfprSwFcSanEpIfRole": cfprSwFcSanEpIfRole,
       "cfprSwFcSanEpIfType": cfprSwFcSanEpIfType,
       "cfprSwFcSanEpLc": cfprSwFcSanEpLc,
       "cfprSwFcSanEpLocale": cfprSwFcSanEpLocale,
       "cfprSwFcSanEpName": cfprSwFcSanEpName,
       "cfprSwFcSanEpPcId": cfprSwFcSanEpPcId,
       "cfprSwFcSanEpPeerAggrPortId": cfprSwFcSanEpPeerAggrPortId,
       "cfprSwFcSanEpPeerChassisId": cfprSwFcSanEpPeerChassisId,
       "cfprSwFcSanEpPeerDn": cfprSwFcSanEpPeerDn,
       "cfprSwFcSanEpPeerPortId": cfprSwFcSanEpPeerPortId,
       "cfprSwFcSanEpPeerSlotId": cfprSwFcSanEpPeerSlotId,
       "cfprSwFcSanEpPortId": cfprSwFcSanEpPortId,
       "cfprSwFcSanEpPortVsanId": cfprSwFcSanEpPortVsanId,
       "cfprSwFcSanEpSlotId": cfprSwFcSanEpSlotId,
       "cfprSwFcSanEpSwitchId": cfprSwFcSanEpSwitchId,
       "cfprSwFcSanEpTransport": cfprSwFcSanEpTransport,
       "cfprSwFcSanEpType": cfprSwFcSanEpType,
       "cfprSwFcSanPcTable": cfprSwFcSanPcTable,
       "cfprSwFcSanPcEntry": cfprSwFcSanPcEntry,
       "cfprSwFcSanPcInstanceId": cfprSwFcSanPcInstanceId,
       "cfprSwFcSanPcDn": cfprSwFcSanPcDn,
       "cfprSwFcSanPcRn": cfprSwFcSanPcRn,
       "cfprSwFcSanPcAdminSpeed": cfprSwFcSanPcAdminSpeed,
       "cfprSwFcSanPcAdminState": cfprSwFcSanPcAdminState,
       "cfprSwFcSanPcEpDn": cfprSwFcSanPcEpDn,
       "cfprSwFcSanPcIfRole": cfprSwFcSanPcIfRole,
       "cfprSwFcSanPcIfType": cfprSwFcSanPcIfType,
       "cfprSwFcSanPcLocale": cfprSwFcSanPcLocale,
       "cfprSwFcSanPcMonTrafDir": cfprSwFcSanPcMonTrafDir,
       "cfprSwFcSanPcName": cfprSwFcSanPcName,
       "cfprSwFcSanPcPcId": cfprSwFcSanPcPcId,
       "cfprSwFcSanPcPeerDn": cfprSwFcSanPcPeerDn,
       "cfprSwFcSanPcPortId": cfprSwFcSanPcPortId,
       "cfprSwFcSanPcPortVsanId": cfprSwFcSanPcPortVsanId,
       "cfprSwFcSanPcSwitchId": cfprSwFcSanPcSwitchId,
       "cfprSwFcSanPcTransport": cfprSwFcSanPcTransport,
       "cfprSwFcSanPcType": cfprSwFcSanPcType,
       "cfprSwFcServerZoneGroupTable": cfprSwFcServerZoneGroupTable,
       "cfprSwFcServerZoneGroupEntry": cfprSwFcServerZoneGroupEntry,
       "cfprSwFcServerZoneGroupInstanceId": cfprSwFcServerZoneGroupInstanceId,
       "cfprSwFcServerZoneGroupDn": cfprSwFcServerZoneGroupDn,
       "cfprSwFcServerZoneGroupRn": cfprSwFcServerZoneGroupRn,
       "cfprSwFcServerZoneGroupEpDn": cfprSwFcServerZoneGroupEpDn,
       "cfprSwFcServerZoneGroupId": cfprSwFcServerZoneGroupId,
       "cfprSwFcServerZoneGroupLc": cfprSwFcServerZoneGroupLc,
       "cfprSwFcServerZoneGroupName": cfprSwFcServerZoneGroupName,
       "cfprSwFcServerZoneGroupPeerDn": cfprSwFcServerZoneGroupPeerDn,
       "cfprSwFcServerZoneGroupServerDn": cfprSwFcServerZoneGroupServerDn,
       "cfprSwFcZoneTable": cfprSwFcZoneTable,
       "cfprSwFcZoneEntry": cfprSwFcZoneEntry,
       "cfprSwFcZoneInstanceId": cfprSwFcZoneInstanceId,
       "cfprSwFcZoneDn": cfprSwFcZoneDn,
       "cfprSwFcZoneRn": cfprSwFcZoneRn,
       "cfprSwFcZoneId": cfprSwFcZoneId,
       "cfprSwFcZoneIdentity": cfprSwFcZoneIdentity,
       "cfprSwFcZoneLc": cfprSwFcZoneLc,
       "cfprSwFcZoneName": cfprSwFcZoneName,
       "cfprSwFcZoneOperState": cfprSwFcZoneOperState,
       "cfprSwFcZonePeerDn": cfprSwFcZonePeerDn,
       "cfprSwFcZoneSetTable": cfprSwFcZoneSetTable,
       "cfprSwFcZoneSetEntry": cfprSwFcZoneSetEntry,
       "cfprSwFcZoneSetInstanceId": cfprSwFcZoneSetInstanceId,
       "cfprSwFcZoneSetDn": cfprSwFcZoneSetDn,
       "cfprSwFcZoneSetRn": cfprSwFcZoneSetRn,
       "cfprSwFcZoneSetCurrentZonePrefix": cfprSwFcZoneSetCurrentZonePrefix,
       "cfprSwFcZoneSetLc": cfprSwFcZoneSetLc,
       "cfprSwFcZoneSetName": cfprSwFcZoneSetName,
       "cfprSwFcZoneSetOldZonePrefix": cfprSwFcZoneSetOldZonePrefix,
       "cfprSwFcoeSanEpTable": cfprSwFcoeSanEpTable,
       "cfprSwFcoeSanEpEntry": cfprSwFcoeSanEpEntry,
       "cfprSwFcoeSanEpInstanceId": cfprSwFcoeSanEpInstanceId,
       "cfprSwFcoeSanEpDn": cfprSwFcoeSanEpDn,
       "cfprSwFcoeSanEpRn": cfprSwFcoeSanEpRn,
       "cfprSwFcoeSanEpAdminSpeed": cfprSwFcoeSanEpAdminSpeed,
       "cfprSwFcoeSanEpAdminState": cfprSwFcoeSanEpAdminState,
       "cfprSwFcoeSanEpAggrPortId": cfprSwFcoeSanEpAggrPortId,
       "cfprSwFcoeSanEpChassisId": cfprSwFcoeSanEpChassisId,
       "cfprSwFcoeSanEpEpDn": cfprSwFcoeSanEpEpDn,
       "cfprSwFcoeSanEpIfRole": cfprSwFcoeSanEpIfRole,
       "cfprSwFcoeSanEpIfType": cfprSwFcoeSanEpIfType,
       "cfprSwFcoeSanEpLc": cfprSwFcoeSanEpLc,
       "cfprSwFcoeSanEpLocale": cfprSwFcoeSanEpLocale,
       "cfprSwFcoeSanEpName": cfprSwFcoeSanEpName,
       "cfprSwFcoeSanEpPcId": cfprSwFcoeSanEpPcId,
       "cfprSwFcoeSanEpPeerAggrPortId": cfprSwFcoeSanEpPeerAggrPortId,
       "cfprSwFcoeSanEpPeerChassisId": cfprSwFcoeSanEpPeerChassisId,
       "cfprSwFcoeSanEpPeerDn": cfprSwFcoeSanEpPeerDn,
       "cfprSwFcoeSanEpPeerPortId": cfprSwFcoeSanEpPeerPortId,
       "cfprSwFcoeSanEpPeerSlotId": cfprSwFcoeSanEpPeerSlotId,
       "cfprSwFcoeSanEpPeerState": cfprSwFcoeSanEpPeerState,
       "cfprSwFcoeSanEpPortId": cfprSwFcoeSanEpPortId,
       "cfprSwFcoeSanEpPortVsanId": cfprSwFcoeSanEpPortVsanId,
       "cfprSwFcoeSanEpSlotId": cfprSwFcoeSanEpSlotId,
       "cfprSwFcoeSanEpSwitchId": cfprSwFcoeSanEpSwitchId,
       "cfprSwFcoeSanEpTransport": cfprSwFcoeSanEpTransport,
       "cfprSwFcoeSanEpType": cfprSwFcoeSanEpType,
       "cfprSwFcoeSanEpUdldAdminState": cfprSwFcoeSanEpUdldAdminState,
       "cfprSwFcoeSanEpUdldMode": cfprSwFcoeSanEpUdldMode,
       "cfprSwFcoeSanPcTable": cfprSwFcoeSanPcTable,
       "cfprSwFcoeSanPcEntry": cfprSwFcoeSanPcEntry,
       "cfprSwFcoeSanPcInstanceId": cfprSwFcoeSanPcInstanceId,
       "cfprSwFcoeSanPcDn": cfprSwFcoeSanPcDn,
       "cfprSwFcoeSanPcRn": cfprSwFcoeSanPcRn,
       "cfprSwFcoeSanPcAdminState": cfprSwFcoeSanPcAdminState,
       "cfprSwFcoeSanPcEpDn": cfprSwFcoeSanPcEpDn,
       "cfprSwFcoeSanPcIfRole": cfprSwFcoeSanPcIfRole,
       "cfprSwFcoeSanPcIfType": cfprSwFcoeSanPcIfType,
       "cfprSwFcoeSanPcLacpFastTimer": cfprSwFcoeSanPcLacpFastTimer,
       "cfprSwFcoeSanPcLacpSuspendIndividual": cfprSwFcoeSanPcLacpSuspendIndividual,
       "cfprSwFcoeSanPcLocale": cfprSwFcoeSanPcLocale,
       "cfprSwFcoeSanPcMonTrafDir": cfprSwFcoeSanPcMonTrafDir,
       "cfprSwFcoeSanPcName": cfprSwFcoeSanPcName,
       "cfprSwFcoeSanPcPcId": cfprSwFcoeSanPcPcId,
       "cfprSwFcoeSanPcPeerDn": cfprSwFcoeSanPcPeerDn,
       "cfprSwFcoeSanPcPeerState": cfprSwFcoeSanPcPeerState,
       "cfprSwFcoeSanPcPortId": cfprSwFcoeSanPcPortId,
       "cfprSwFcoeSanPcPortVsanId": cfprSwFcoeSanPcPortVsanId,
       "cfprSwFcoeSanPcSwitchId": cfprSwFcoeSanPcSwitchId,
       "cfprSwFcoeSanPcTransport": cfprSwFcoeSanPcTransport,
       "cfprSwFcoeSanPcType": cfprSwFcoeSanPcType,
       "cfprSwPhysTable": cfprSwPhysTable,
       "cfprSwPhysEntry": cfprSwPhysEntry,
       "cfprSwPhysInstanceId": cfprSwPhysInstanceId,
       "cfprSwPhysDn": cfprSwPhysDn,
       "cfprSwPhysRn": cfprSwPhysRn,
       "cfprSwPhysConfMode": cfprSwPhysConfMode,
       "cfprSwPhysFsmDescr": cfprSwPhysFsmDescr,
       "cfprSwPhysFsmPrev": cfprSwPhysFsmPrev,
       "cfprSwPhysFsmProgr": cfprSwPhysFsmProgr,
       "cfprSwPhysFsmRmtInvErrCode": cfprSwPhysFsmRmtInvErrCode,
       "cfprSwPhysFsmRmtInvErrDescr": cfprSwPhysFsmRmtInvErrDescr,
       "cfprSwPhysFsmRmtInvRslt": cfprSwPhysFsmRmtInvRslt,
       "cfprSwPhysFsmStageDescr": cfprSwPhysFsmStageDescr,
       "cfprSwPhysFsmStamp": cfprSwPhysFsmStamp,
       "cfprSwPhysFsmStatus": cfprSwPhysFsmStatus,
       "cfprSwPhysFsmTry": cfprSwPhysFsmTry,
       "cfprSwPhysEtherEpTable": cfprSwPhysEtherEpTable,
       "cfprSwPhysEtherEpEntry": cfprSwPhysEtherEpEntry,
       "cfprSwPhysEtherEpInstanceId": cfprSwPhysEtherEpInstanceId,
       "cfprSwPhysEtherEpDn": cfprSwPhysEtherEpDn,
       "cfprSwPhysEtherEpRn": cfprSwPhysEtherEpRn,
       "cfprSwPhysEtherEpAdminState": cfprSwPhysEtherEpAdminState,
       "cfprSwPhysEtherEpAggrPortId": cfprSwPhysEtherEpAggrPortId,
       "cfprSwPhysEtherEpChassisId": cfprSwPhysEtherEpChassisId,
       "cfprSwPhysEtherEpEpDn": cfprSwPhysEtherEpEpDn,
       "cfprSwPhysEtherEpIfRole": cfprSwPhysEtherEpIfRole,
       "cfprSwPhysEtherEpIfType": cfprSwPhysEtherEpIfType,
       "cfprSwPhysEtherEpLc": cfprSwPhysEtherEpLc,
       "cfprSwPhysEtherEpLocale": cfprSwPhysEtherEpLocale,
       "cfprSwPhysEtherEpName": cfprSwPhysEtherEpName,
       "cfprSwPhysEtherEpPeerAggrPortId": cfprSwPhysEtherEpPeerAggrPortId,
       "cfprSwPhysEtherEpPeerChassisId": cfprSwPhysEtherEpPeerChassisId,
       "cfprSwPhysEtherEpPeerDn": cfprSwPhysEtherEpPeerDn,
       "cfprSwPhysEtherEpPeerPortId": cfprSwPhysEtherEpPeerPortId,
       "cfprSwPhysEtherEpPeerSlotId": cfprSwPhysEtherEpPeerSlotId,
       "cfprSwPhysEtherEpPortId": cfprSwPhysEtherEpPortId,
       "cfprSwPhysEtherEpSlotId": cfprSwPhysEtherEpSlotId,
       "cfprSwPhysEtherEpSwitchId": cfprSwPhysEtherEpSwitchId,
       "cfprSwPhysEtherEpTransport": cfprSwPhysEtherEpTransport,
       "cfprSwPhysEtherEpType": cfprSwPhysEtherEpType,
       "cfprSwPhysFcEpTable": cfprSwPhysFcEpTable,
       "cfprSwPhysFcEpEntry": cfprSwPhysFcEpEntry,
       "cfprSwPhysFcEpInstanceId": cfprSwPhysFcEpInstanceId,
       "cfprSwPhysFcEpDn": cfprSwPhysFcEpDn,
       "cfprSwPhysFcEpRn": cfprSwPhysFcEpRn,
       "cfprSwPhysFcEpAdminState": cfprSwPhysFcEpAdminState,
       "cfprSwPhysFcEpAggrPortId": cfprSwPhysFcEpAggrPortId,
       "cfprSwPhysFcEpChassisId": cfprSwPhysFcEpChassisId,
       "cfprSwPhysFcEpEpDn": cfprSwPhysFcEpEpDn,
       "cfprSwPhysFcEpIfRole": cfprSwPhysFcEpIfRole,
       "cfprSwPhysFcEpIfType": cfprSwPhysFcEpIfType,
       "cfprSwPhysFcEpLc": cfprSwPhysFcEpLc,
       "cfprSwPhysFcEpLocale": cfprSwPhysFcEpLocale,
       "cfprSwPhysFcEpName": cfprSwPhysFcEpName,
       "cfprSwPhysFcEpPeerAggrPortId": cfprSwPhysFcEpPeerAggrPortId,
       "cfprSwPhysFcEpPeerChassisId": cfprSwPhysFcEpPeerChassisId,
       "cfprSwPhysFcEpPeerDn": cfprSwPhysFcEpPeerDn,
       "cfprSwPhysFcEpPeerPortId": cfprSwPhysFcEpPeerPortId,
       "cfprSwPhysFcEpPeerSlotId": cfprSwPhysFcEpPeerSlotId,
       "cfprSwPhysFcEpPortId": cfprSwPhysFcEpPortId,
       "cfprSwPhysFcEpSlotId": cfprSwPhysFcEpSlotId,
       "cfprSwPhysFcEpSwitchId": cfprSwPhysFcEpSwitchId,
       "cfprSwPhysFcEpTransport": cfprSwPhysFcEpTransport,
       "cfprSwPhysFcEpType": cfprSwPhysFcEpType,
       "cfprSwPhysFsmTable": cfprSwPhysFsmTable,
       "cfprSwPhysFsmEntry": cfprSwPhysFsmEntry,
       "cfprSwPhysFsmInstanceId": cfprSwPhysFsmInstanceId,
       "cfprSwPhysFsmDn": cfprSwPhysFsmDn,
       "cfprSwPhysFsmRn": cfprSwPhysFsmRn,
       "cfprSwPhysFsmCompletionTime": cfprSwPhysFsmCompletionTime,
       "cfprSwPhysFsmCurrentFsm": cfprSwPhysFsmCurrentFsm,
       "cfprSwPhysFsmDescrData": cfprSwPhysFsmDescrData,
       "cfprSwPhysFsmFsmStatus": cfprSwPhysFsmFsmStatus,
       "cfprSwPhysFsmProgress": cfprSwPhysFsmProgress,
       "cfprSwPhysFsmRmtErrCode": cfprSwPhysFsmRmtErrCode,
       "cfprSwPhysFsmRmtErrDescr": cfprSwPhysFsmRmtErrDescr,
       "cfprSwPhysFsmRmtRslt": cfprSwPhysFsmRmtRslt,
       "cfprSwPhysFsmStageTable": cfprSwPhysFsmStageTable,
       "cfprSwPhysFsmStageEntry": cfprSwPhysFsmStageEntry,
       "cfprSwPhysFsmStageInstanceId": cfprSwPhysFsmStageInstanceId,
       "cfprSwPhysFsmStageDn": cfprSwPhysFsmStageDn,
       "cfprSwPhysFsmStageRn": cfprSwPhysFsmStageRn,
       "cfprSwPhysFsmStageDescrData": cfprSwPhysFsmStageDescrData,
       "cfprSwPhysFsmStageLastUpdateTime": cfprSwPhysFsmStageLastUpdateTime,
       "cfprSwPhysFsmStageName": cfprSwPhysFsmStageName,
       "cfprSwPhysFsmStageOrder": cfprSwPhysFsmStageOrder,
       "cfprSwPhysFsmStageRetry": cfprSwPhysFsmStageRetry,
       "cfprSwPhysFsmStageStageStatus": cfprSwPhysFsmStageStageStatus,
       "cfprSwPhysFsmTaskTable": cfprSwPhysFsmTaskTable,
       "cfprSwPhysFsmTaskEntry": cfprSwPhysFsmTaskEntry,
       "cfprSwPhysFsmTaskInstanceId": cfprSwPhysFsmTaskInstanceId,
       "cfprSwPhysFsmTaskDn": cfprSwPhysFsmTaskDn,
       "cfprSwPhysFsmTaskRn": cfprSwPhysFsmTaskRn,
       "cfprSwPhysFsmTaskCompletion": cfprSwPhysFsmTaskCompletion,
       "cfprSwPhysFsmTaskFlags": cfprSwPhysFsmTaskFlags,
       "cfprSwPhysFsmTaskItem": cfprSwPhysFsmTaskItem,
       "cfprSwPhysFsmTaskSeqId": cfprSwPhysFsmTaskSeqId,
       "cfprSwPortBreakoutTable": cfprSwPortBreakoutTable,
       "cfprSwPortBreakoutEntry": cfprSwPortBreakoutEntry,
       "cfprSwPortBreakoutInstanceId": cfprSwPortBreakoutInstanceId,
       "cfprSwPortBreakoutDn": cfprSwPortBreakoutDn,
       "cfprSwPortBreakoutRn": cfprSwPortBreakoutRn,
       "cfprSwPortBreakoutBreakoutType": cfprSwPortBreakoutBreakoutType,
       "cfprSwPortBreakoutPortId": cfprSwPortBreakoutPortId,
       "cfprSwPortBreakoutSlotId": cfprSwPortBreakoutSlotId,
       "cfprSwSubGroupTable": cfprSwSubGroupTable,
       "cfprSwSubGroupEntry": cfprSwSubGroupEntry,
       "cfprSwSubGroupInstanceId": cfprSwSubGroupInstanceId,
       "cfprSwSubGroupDn": cfprSwSubGroupDn,
       "cfprSwSubGroupRn": cfprSwSubGroupRn,
       "cfprSwSubGroupAggrPortId": cfprSwSubGroupAggrPortId,
       "cfprSwSubGroupLicGP": cfprSwSubGroupLicGP,
       "cfprSwSubGroupLicState": cfprSwSubGroupLicState,
       "cfprSwSubGroupLocale": cfprSwSubGroupLocale,
       "cfprSwSubGroupName": cfprSwSubGroupName,
       "cfprSwSubGroupSlotId": cfprSwSubGroupSlotId,
       "cfprSwSubGroupSwitchId": cfprSwSubGroupSwitchId,
       "cfprSwSubGroupTransport": cfprSwSubGroupTransport,
       "cfprSwSubGroupType": cfprSwSubGroupType,
       "cfprSwSystemStatsTable": cfprSwSystemStatsTable,
       "cfprSwSystemStatsEntry": cfprSwSystemStatsEntry,
       "cfprSwSystemStatsInstanceId": cfprSwSystemStatsInstanceId,
       "cfprSwSystemStatsDn": cfprSwSystemStatsDn,
       "cfprSwSystemStatsRn": cfprSwSystemStatsRn,
       "cfprSwSystemStatsIntervals": cfprSwSystemStatsIntervals,
       "cfprSwSystemStatsLoad": cfprSwSystemStatsLoad,
       "cfprSwSystemStatsLoadAvg": cfprSwSystemStatsLoadAvg,
       "cfprSwSystemStatsLoadMax": cfprSwSystemStatsLoadMax,
       "cfprSwSystemStatsLoadMin": cfprSwSystemStatsLoadMin,
       "cfprSwSystemStatsMemAvailable": cfprSwSystemStatsMemAvailable,
       "cfprSwSystemStatsMemAvailableAvg": cfprSwSystemStatsMemAvailableAvg,
       "cfprSwSystemStatsMemAvailableMax": cfprSwSystemStatsMemAvailableMax,
       "cfprSwSystemStatsMemAvailableMin": cfprSwSystemStatsMemAvailableMin,
       "cfprSwSystemStatsMemCached": cfprSwSystemStatsMemCached,
       "cfprSwSystemStatsMemCachedAvg": cfprSwSystemStatsMemCachedAvg,
       "cfprSwSystemStatsMemCachedMax": cfprSwSystemStatsMemCachedMax,
       "cfprSwSystemStatsMemCachedMin": cfprSwSystemStatsMemCachedMin,
       "cfprSwSystemStatsSuspect": cfprSwSystemStatsSuspect,
       "cfprSwSystemStatsThresholded": cfprSwSystemStatsThresholded,
       "cfprSwSystemStatsTimeCollected": cfprSwSystemStatsTimeCollected,
       "cfprSwSystemStatsUpdate": cfprSwSystemStatsUpdate,
       "cfprSwSystemStatsHistTable": cfprSwSystemStatsHistTable,
       "cfprSwSystemStatsHistEntry": cfprSwSystemStatsHistEntry,
       "cfprSwSystemStatsHistInstanceId": cfprSwSystemStatsHistInstanceId,
       "cfprSwSystemStatsHistDn": cfprSwSystemStatsHistDn,
       "cfprSwSystemStatsHistRn": cfprSwSystemStatsHistRn,
       "cfprSwSystemStatsHistId": cfprSwSystemStatsHistId,
       "cfprSwSystemStatsHistLoad": cfprSwSystemStatsHistLoad,
       "cfprSwSystemStatsHistLoadAvg": cfprSwSystemStatsHistLoadAvg,
       "cfprSwSystemStatsHistLoadMax": cfprSwSystemStatsHistLoadMax,
       "cfprSwSystemStatsHistLoadMin": cfprSwSystemStatsHistLoadMin,
       "cfprSwSystemStatsHistMemAvailable": cfprSwSystemStatsHistMemAvailable,
       "cfprSwSystemStatsHistMemAvailableAvg": cfprSwSystemStatsHistMemAvailableAvg,
       "cfprSwSystemStatsHistMemAvailableMax": cfprSwSystemStatsHistMemAvailableMax,
       "cfprSwSystemStatsHistMemAvailableMin": cfprSwSystemStatsHistMemAvailableMin,
       "cfprSwSystemStatsHistMemCached": cfprSwSystemStatsHistMemCached,
       "cfprSwSystemStatsHistMemCachedAvg": cfprSwSystemStatsHistMemCachedAvg,
       "cfprSwSystemStatsHistMemCachedMax": cfprSwSystemStatsHistMemCachedMax,
       "cfprSwSystemStatsHistMemCachedMin": cfprSwSystemStatsHistMemCachedMin,
       "cfprSwSystemStatsHistMostRecent": cfprSwSystemStatsHistMostRecent,
       "cfprSwSystemStatsHistSuspect": cfprSwSystemStatsHistSuspect,
       "cfprSwSystemStatsHistThresholded": cfprSwSystemStatsHistThresholded,
       "cfprSwSystemStatsHistTimeCollected": cfprSwSystemStatsHistTimeCollected,
       "cfprSwUlanTable": cfprSwUlanTable,
       "cfprSwUlanEntry": cfprSwUlanEntry,
       "cfprSwUlanInstanceId": cfprSwUlanInstanceId,
       "cfprSwUlanDn": cfprSwUlanDn,
       "cfprSwUlanRn": cfprSwUlanRn,
       "cfprSwUlanAssocPrimaryVlanState": cfprSwUlanAssocPrimaryVlanState,
       "cfprSwUlanAssocPrimaryVlanSwitchId": cfprSwUlanAssocPrimaryVlanSwitchId,
       "cfprSwUlanEpDn": cfprSwUlanEpDn,
       "cfprSwUlanId": cfprSwUlanId,
       "cfprSwUlanIfRole": cfprSwUlanIfRole,
       "cfprSwUlanIfType": cfprSwUlanIfType,
       "cfprSwUlanLocale": cfprSwUlanLocale,
       "cfprSwUlanName": cfprSwUlanName,
       "cfprSwUlanOperState": cfprSwUlanOperState,
       "cfprSwUlanOverlapStateForA": cfprSwUlanOverlapStateForA,
       "cfprSwUlanOverlapStateForB": cfprSwUlanOverlapStateForB,
       "cfprSwUlanPeerDn": cfprSwUlanPeerDn,
       "cfprSwUlanPolicyOwner": cfprSwUlanPolicyOwner,
       "cfprSwUlanPubNwDn": cfprSwUlanPubNwDn,
       "cfprSwUlanPubNwId": cfprSwUlanPubNwId,
       "cfprSwUlanPubNwName": cfprSwUlanPubNwName,
       "cfprSwUlanPurpose": cfprSwUlanPurpose,
       "cfprSwUlanSharing": cfprSwUlanSharing,
       "cfprSwUlanSwitchId": cfprSwUlanSwitchId,
       "cfprSwUlanTransport": cfprSwUlanTransport,
       "cfprSwUlanType": cfprSwUlanType,
       "cfprSwUlanVlanType": cfprSwUlanVlanType,
       "cfprSwUtilityDomainTable": cfprSwUtilityDomainTable,
       "cfprSwUtilityDomainEntry": cfprSwUtilityDomainEntry,
       "cfprSwUtilityDomainInstanceId": cfprSwUtilityDomainInstanceId,
       "cfprSwUtilityDomainDn": cfprSwUtilityDomainDn,
       "cfprSwUtilityDomainRn": cfprSwUtilityDomainRn,
       "cfprSwUtilityDomainFsmDescr": cfprSwUtilityDomainFsmDescr,
       "cfprSwUtilityDomainFsmPrev": cfprSwUtilityDomainFsmPrev,
       "cfprSwUtilityDomainFsmProgr": cfprSwUtilityDomainFsmProgr,
       "cfprSwUtilityDomainFsmRmtInvErrCode": cfprSwUtilityDomainFsmRmtInvErrCode,
       "cfprSwUtilityDomainFsmRmtInvErrDescr": cfprSwUtilityDomainFsmRmtInvErrDescr,
       "cfprSwUtilityDomainFsmRmtInvRslt": cfprSwUtilityDomainFsmRmtInvRslt,
       "cfprSwUtilityDomainFsmStageDescr": cfprSwUtilityDomainFsmStageDescr,
       "cfprSwUtilityDomainFsmStamp": cfprSwUtilityDomainFsmStamp,
       "cfprSwUtilityDomainFsmStatus": cfprSwUtilityDomainFsmStatus,
       "cfprSwUtilityDomainFsmTry": cfprSwUtilityDomainFsmTry,
       "cfprSwUtilityDomainLocale": cfprSwUtilityDomainLocale,
       "cfprSwUtilityDomainName": cfprSwUtilityDomainName,
       "cfprSwUtilityDomainSwitchId": cfprSwUtilityDomainSwitchId,
       "cfprSwUtilityDomainTransport": cfprSwUtilityDomainTransport,
       "cfprSwUtilityDomainType": cfprSwUtilityDomainType,
       "cfprSwUtilityDomainFsmTable": cfprSwUtilityDomainFsmTable,
       "cfprSwUtilityDomainFsmEntry": cfprSwUtilityDomainFsmEntry,
       "cfprSwUtilityDomainFsmInstanceId": cfprSwUtilityDomainFsmInstanceId,
       "cfprSwUtilityDomainFsmDn": cfprSwUtilityDomainFsmDn,
       "cfprSwUtilityDomainFsmRn": cfprSwUtilityDomainFsmRn,
       "cfprSwUtilityDomainFsmCompletionTime": cfprSwUtilityDomainFsmCompletionTime,
       "cfprSwUtilityDomainFsmCurrentFsm": cfprSwUtilityDomainFsmCurrentFsm,
       "cfprSwUtilityDomainFsmDescrData": cfprSwUtilityDomainFsmDescrData,
       "cfprSwUtilityDomainFsmFsmStatus": cfprSwUtilityDomainFsmFsmStatus,
       "cfprSwUtilityDomainFsmProgress": cfprSwUtilityDomainFsmProgress,
       "cfprSwUtilityDomainFsmRmtErrCode": cfprSwUtilityDomainFsmRmtErrCode,
       "cfprSwUtilityDomainFsmRmtErrDescr": cfprSwUtilityDomainFsmRmtErrDescr,
       "cfprSwUtilityDomainFsmRmtRslt": cfprSwUtilityDomainFsmRmtRslt,
       "cfprSwUtilityDomainFsmStageTable": cfprSwUtilityDomainFsmStageTable,
       "cfprSwUtilityDomainFsmStageEntry": cfprSwUtilityDomainFsmStageEntry,
       "cfprSwUtilityDomainFsmStageInstanceId": cfprSwUtilityDomainFsmStageInstanceId,
       "cfprSwUtilityDomainFsmStageDn": cfprSwUtilityDomainFsmStageDn,
       "cfprSwUtilityDomainFsmStageRn": cfprSwUtilityDomainFsmStageRn,
       "cfprSwUtilityDomainFsmStageDescrData": cfprSwUtilityDomainFsmStageDescrData,
       "cfprSwUtilityDomainFsmStageLastUpdateTime": cfprSwUtilityDomainFsmStageLastUpdateTime,
       "cfprSwUtilityDomainFsmStageName": cfprSwUtilityDomainFsmStageName,
       "cfprSwUtilityDomainFsmStageOrder": cfprSwUtilityDomainFsmStageOrder,
       "cfprSwUtilityDomainFsmStageRetry": cfprSwUtilityDomainFsmStageRetry,
       "cfprSwUtilityDomainFsmStageStageStatus": cfprSwUtilityDomainFsmStageStageStatus,
       "cfprSwUtilityDomainFsmTaskTable": cfprSwUtilityDomainFsmTaskTable,
       "cfprSwUtilityDomainFsmTaskEntry": cfprSwUtilityDomainFsmTaskEntry,
       "cfprSwUtilityDomainFsmTaskInstanceId": cfprSwUtilityDomainFsmTaskInstanceId,
       "cfprSwUtilityDomainFsmTaskDn": cfprSwUtilityDomainFsmTaskDn,
       "cfprSwUtilityDomainFsmTaskRn": cfprSwUtilityDomainFsmTaskRn,
       "cfprSwUtilityDomainFsmTaskCompletion": cfprSwUtilityDomainFsmTaskCompletion,
       "cfprSwUtilityDomainFsmTaskFlags": cfprSwUtilityDomainFsmTaskFlags,
       "cfprSwUtilityDomainFsmTaskItem": cfprSwUtilityDomainFsmTaskItem,
       "cfprSwUtilityDomainFsmTaskSeqId": cfprSwUtilityDomainFsmTaskSeqId,
       "cfprSwVlanTable": cfprSwVlanTable,
       "cfprSwVlanEntry": cfprSwVlanEntry,
       "cfprSwVlanInstanceId": cfprSwVlanInstanceId,
       "cfprSwVlanDn": cfprSwVlanDn,
       "cfprSwVlanRn": cfprSwVlanRn,
       "cfprSwVlanAssocPrimaryVlanState": cfprSwVlanAssocPrimaryVlanState,
       "cfprSwVlanAssocPrimaryVlanSwitchId": cfprSwVlanAssocPrimaryVlanSwitchId,
       "cfprSwVlanCompressionType": cfprSwVlanCompressionType,
       "cfprSwVlanEpDn": cfprSwVlanEpDn,
       "cfprSwVlanId": cfprSwVlanId,
       "cfprSwVlanIfRole": cfprSwVlanIfRole,
       "cfprSwVlanIfType": cfprSwVlanIfType,
       "cfprSwVlanLc": cfprSwVlanLc,
       "cfprSwVlanLocale": cfprSwVlanLocale,
       "cfprSwVlanMonTrafDir": cfprSwVlanMonTrafDir,
       "cfprSwVlanName": cfprSwVlanName,
       "cfprSwVlanOperState": cfprSwVlanOperState,
       "cfprSwVlanOverlapStateForA": cfprSwVlanOverlapStateForA,
       "cfprSwVlanOverlapStateForB": cfprSwVlanOverlapStateForB,
       "cfprSwVlanPeerDn": cfprSwVlanPeerDn,
       "cfprSwVlanPolicyOwner": cfprSwVlanPolicyOwner,
       "cfprSwVlanPubNwDn": cfprSwVlanPubNwDn,
       "cfprSwVlanPubNwId": cfprSwVlanPubNwId,
       "cfprSwVlanPubNwName": cfprSwVlanPubNwName,
       "cfprSwVlanQuerierIpAddrs": cfprSwVlanQuerierIpAddrs,
       "cfprSwVlanSecVlanPerPrimaryVlanCount": cfprSwVlanSecVlanPerPrimaryVlanCount,
       "cfprSwVlanSecVlanPerPrimaryVlanCountStatus": cfprSwVlanSecVlanPerPrimaryVlanCountStatus,
       "cfprSwVlanSharing": cfprSwVlanSharing,
       "cfprSwVlanSnoopingEnabled": cfprSwVlanSnoopingEnabled,
       "cfprSwVlanSwitchId": cfprSwVlanSwitchId,
       "cfprSwVlanTransport": cfprSwVlanTransport,
       "cfprSwVlanType": cfprSwVlanType,
       "cfprSwVlanVlanType": cfprSwVlanVlanType,
       "cfprSwVlanGroupTable": cfprSwVlanGroupTable,
       "cfprSwVlanGroupEntry": cfprSwVlanGroupEntry,
       "cfprSwVlanGroupInstanceId": cfprSwVlanGroupInstanceId,
       "cfprSwVlanGroupDn": cfprSwVlanGroupDn,
       "cfprSwVlanGroupRn": cfprSwVlanGroupRn,
       "cfprSwVlanGroupId": cfprSwVlanGroupId,
       "cfprSwVlanGroupPeerDn": cfprSwVlanGroupPeerDn,
       "cfprSwVlanGroupSwitchId": cfprSwVlanGroupSwitchId,
       "cfprSwVlanGroupType": cfprSwVlanGroupType,
       "cfprSwVlanPortNsTable": cfprSwVlanPortNsTable,
       "cfprSwVlanPortNsEntry": cfprSwVlanPortNsEntry,
       "cfprSwVlanPortNsInstanceId": cfprSwVlanPortNsInstanceId,
       "cfprSwVlanPortNsDn": cfprSwVlanPortNsDn,
       "cfprSwVlanPortNsRn": cfprSwVlanPortNsRn,
       "cfprSwVlanPortNsAccessVlanPortCount": cfprSwVlanPortNsAccessVlanPortCount,
       "cfprSwVlanPortNsAllocStatus": cfprSwVlanPortNsAllocStatus,
       "cfprSwVlanPortNsBorderVlanPortCount": cfprSwVlanPortNsBorderVlanPortCount,
       "cfprSwVlanPortNsConfigStatus": cfprSwVlanPortNsConfigStatus,
       "cfprSwVlanPortNsLimit": cfprSwVlanPortNsLimit,
       "cfprSwVlanPortNsSwitchId": cfprSwVlanPortNsSwitchId,
       "cfprSwVlanPortNsTotalVlanPortCount": cfprSwVlanPortNsTotalVlanPortCount,
       "cfprSwVlanPortNsVlanCompOffLimit": cfprSwVlanPortNsVlanCompOffLimit,
       "cfprSwVlanPortNsVlanCompOnLimit": cfprSwVlanPortNsVlanCompOnLimit,
       "cfprSwVlanPortNsOverrideTable": cfprSwVlanPortNsOverrideTable,
       "cfprSwVlanPortNsOverrideEntry": cfprSwVlanPortNsOverrideEntry,
       "cfprSwVlanPortNsOverrideInstanceId": cfprSwVlanPortNsOverrideInstanceId,
       "cfprSwVlanPortNsOverrideDn": cfprSwVlanPortNsOverrideDn,
       "cfprSwVlanPortNsOverrideRn": cfprSwVlanPortNsOverrideRn,
       "cfprSwVlanPortNsOverrideLimit": cfprSwVlanPortNsOverrideLimit,
       "cfprSwVlanRefTable": cfprSwVlanRefTable,
       "cfprSwVlanRefEntry": cfprSwVlanRefEntry,
       "cfprSwVlanRefInstanceId": cfprSwVlanRefInstanceId,
       "cfprSwVlanRefDn": cfprSwVlanRefDn,
       "cfprSwVlanRefRn": cfprSwVlanRefRn,
       "cfprSwVlanRefCompressionType": cfprSwVlanRefCompressionType,
       "cfprSwVlanRefConfigStatus": cfprSwVlanRefConfigStatus,
       "cfprSwVlanRefId": cfprSwVlanRefId,
       "cfprSwVlanRefPeerDn": cfprSwVlanRefPeerDn,
       "cfprSwVsanTable": cfprSwVsanTable,
       "cfprSwVsanEntry": cfprSwVsanEntry,
       "cfprSwVsanInstanceId": cfprSwVsanInstanceId,
       "cfprSwVsanDn": cfprSwVsanDn,
       "cfprSwVsanRn": cfprSwVsanRn,
       "cfprSwVsanDefaultZoning": cfprSwVsanDefaultZoning,
       "cfprSwVsanEpDn": cfprSwVsanEpDn,
       "cfprSwVsanFcZoneSharingMode": cfprSwVsanFcZoneSharingMode,
       "cfprSwVsanFcoeVlan": cfprSwVsanFcoeVlan,
       "cfprSwVsanFltAggr": cfprSwVsanFltAggr,
       "cfprSwVsanId": cfprSwVsanId,
       "cfprSwVsanIfRole": cfprSwVsanIfRole,
       "cfprSwVsanIfType": cfprSwVsanIfType,
       "cfprSwVsanLc": cfprSwVsanLc,
       "cfprSwVsanLocale": cfprSwVsanLocale,
       "cfprSwVsanMonTrafDir": cfprSwVsanMonTrafDir,
       "cfprSwVsanName": cfprSwVsanName,
       "cfprSwVsanOperState": cfprSwVsanOperState,
       "cfprSwVsanPeerDn": cfprSwVsanPeerDn,
       "cfprSwVsanPolicyOwner": cfprSwVsanPolicyOwner,
       "cfprSwVsanSwitchId": cfprSwVsanSwitchId,
       "cfprSwVsanTransport": cfprSwVsanTransport,
       "cfprSwVsanType": cfprSwVsanType,
       "cfprSwVsanZoningState": cfprSwVsanZoningState,
       "cfprSwZoneInitiatorMemberTable": cfprSwZoneInitiatorMemberTable,
       "cfprSwZoneInitiatorMemberEntry": cfprSwZoneInitiatorMemberEntry,
       "cfprSwZoneInitiatorMemberInstanceId": cfprSwZoneInitiatorMemberInstanceId,
       "cfprSwZoneInitiatorMemberDn": cfprSwZoneInitiatorMemberDn,
       "cfprSwZoneInitiatorMemberRn": cfprSwZoneInitiatorMemberRn,
       "cfprSwZoneInitiatorMemberEpDn": cfprSwZoneInitiatorMemberEpDn,
       "cfprSwZoneInitiatorMemberLc": cfprSwZoneInitiatorMemberLc,
       "cfprSwZoneInitiatorMemberName": cfprSwZoneInitiatorMemberName,
       "cfprSwZoneInitiatorMemberPeerDn": cfprSwZoneInitiatorMemberPeerDn,
       "cfprSwZoneInitiatorMemberWwpn": cfprSwZoneInitiatorMemberWwpn,
       "cfprSwZoneTargetMemberTable": cfprSwZoneTargetMemberTable,
       "cfprSwZoneTargetMemberEntry": cfprSwZoneTargetMemberEntry,
       "cfprSwZoneTargetMemberInstanceId": cfprSwZoneTargetMemberInstanceId,
       "cfprSwZoneTargetMemberDn": cfprSwZoneTargetMemberDn,
       "cfprSwZoneTargetMemberRn": cfprSwZoneTargetMemberRn,
       "cfprSwZoneTargetMemberEpDn": cfprSwZoneTargetMemberEpDn,
       "cfprSwZoneTargetMemberLc": cfprSwZoneTargetMemberLc,
       "cfprSwZoneTargetMemberName": cfprSwZoneTargetMemberName,
       "cfprSwZoneTargetMemberPeerDn": cfprSwZoneTargetMemberPeerDn,
       "cfprSwZoneTargetMemberWwpn": cfprSwZoneTargetMemberWwpn,
       "cfprSwSspEthLanMonTable": cfprSwSspEthLanMonTable,
       "cfprSwSspEthLanMonEntry": cfprSwSspEthLanMonEntry,
       "cfprSwSspEthLanMonInstanceId": cfprSwSspEthLanMonInstanceId,
       "cfprSwSspEthLanMonDn": cfprSwSspEthLanMonDn,
       "cfprSwSspEthLanMonRn": cfprSwSspEthLanMonRn,
       "cfprSwSspEthLanMonLocale": cfprSwSspEthLanMonLocale,
       "cfprSwSspEthLanMonName": cfprSwSspEthLanMonName,
       "cfprSwSspEthLanMonSwitchId": cfprSwSspEthLanMonSwitchId,
       "cfprSwSspEthLanMonTransport": cfprSwSspEthLanMonTransport,
       "cfprSwSspEthLanMonType": cfprSwSspEthLanMonType,
       "cfprSwSspEthMonTable": cfprSwSspEthMonTable,
       "cfprSwSspEthMonEntry": cfprSwSspEthMonEntry,
       "cfprSwSspEthMonInstanceId": cfprSwSspEthMonInstanceId,
       "cfprSwSspEthMonDn": cfprSwSspEthMonDn,
       "cfprSwSspEthMonRn": cfprSwSspEthMonRn,
       "cfprSwSspEthMonAdminState": cfprSwSspEthMonAdminState,
       "cfprSwSspEthMonAppendFlag": cfprSwSspEthMonAppendFlag,
       "cfprSwSspEthMonDelPcap": cfprSwSspEthMonDelPcap,
       "cfprSwSspEthMonFsmDescr": cfprSwSspEthMonFsmDescr,
       "cfprSwSspEthMonFsmPrev": cfprSwSspEthMonFsmPrev,
       "cfprSwSspEthMonFsmProgr": cfprSwSspEthMonFsmProgr,
       "cfprSwSspEthMonFsmRmtInvErrCode": cfprSwSspEthMonFsmRmtInvErrCode,
       "cfprSwSspEthMonFsmRmtInvErrDescr": cfprSwSspEthMonFsmRmtInvErrDescr,
       "cfprSwSspEthMonFsmRmtInvRslt": cfprSwSspEthMonFsmRmtInvRslt,
       "cfprSwSspEthMonFsmStageDescr": cfprSwSspEthMonFsmStageDescr,
       "cfprSwSspEthMonFsmStamp": cfprSwSspEthMonFsmStamp,
       "cfprSwSspEthMonFsmStatus": cfprSwSspEthMonFsmStatus,
       "cfprSwSspEthMonFsmTry": cfprSwSspEthMonFsmTry,
       "cfprSwSspEthMonLifeCycle": cfprSwSspEthMonLifeCycle,
       "cfprSwSspEthMonName": cfprSwSspEthMonName,
       "cfprSwSspEthMonPeerDn": cfprSwSspEthMonPeerDn,
       "cfprSwSspEthMonSession": cfprSwSspEthMonSession,
       "cfprSwSspEthMonSessionMemUsage": cfprSwSspEthMonSessionMemUsage,
       "cfprSwSspEthMonSwitchId": cfprSwSspEthMonSwitchId,
       "cfprSwSspEthMonTransport": cfprSwSspEthMonTransport,
       "cfprSwSspEthMonType": cfprSwSspEthMonType,
       "cfprSwSspEthMonSessionPcapSnapLen": cfprSwSspEthMonSessionPcapSnapLen,
       "cfprSwSspEthMonFsmFlags": cfprSwSspEthMonFsmFlags,
       "cfprSwSspEthMonFilterEpTable": cfprSwSspEthMonFilterEpTable,
       "cfprSwSspEthMonFilterEpEntry": cfprSwSspEthMonFilterEpEntry,
       "cfprSwSspEthMonFilterEpInstanceId": cfprSwSspEthMonFilterEpInstanceId,
       "cfprSwSspEthMonFilterEpDn": cfprSwSspEthMonFilterEpDn,
       "cfprSwSspEthMonFilterEpRn": cfprSwSspEthMonFilterEpRn,
       "cfprSwSspEthMonFilterEpDestIp": cfprSwSspEthMonFilterEpDestIp,
       "cfprSwSspEthMonFilterEpDestMAC": cfprSwSspEthMonFilterEpDestMAC,
       "cfprSwSspEthMonFilterEpDestPort": cfprSwSspEthMonFilterEpDestPort,
       "cfprSwSspEthMonFilterEpEthertype": cfprSwSspEthMonFilterEpEthertype,
       "cfprSwSspEthMonFilterEpFilterFlag": cfprSwSspEthMonFilterEpFilterFlag,
       "cfprSwSspEthMonFilterEpIvlan": cfprSwSspEthMonFilterEpIvlan,
       "cfprSwSspEthMonFilterEpLifeCycle": cfprSwSspEthMonFilterEpLifeCycle,
       "cfprSwSspEthMonFilterEpNameId": cfprSwSspEthMonFilterEpNameId,
       "cfprSwSspEthMonFilterEpOvlan": cfprSwSspEthMonFilterEpOvlan,
       "cfprSwSspEthMonFilterEpPeerDn": cfprSwSspEthMonFilterEpPeerDn,
       "cfprSwSspEthMonFilterEpProtocol": cfprSwSspEthMonFilterEpProtocol,
       "cfprSwSspEthMonFilterEpRefCount": cfprSwSspEthMonFilterEpRefCount,
       "cfprSwSspEthMonFilterEpSrcIp": cfprSwSspEthMonFilterEpSrcIp,
       "cfprSwSspEthMonFilterEpSrcMAC": cfprSwSspEthMonFilterEpSrcMAC,
       "cfprSwSspEthMonFilterEpSrcPort": cfprSwSspEthMonFilterEpSrcPort,
       "cfprSwSspEthMonFilterEpDestIpv6": cfprSwSspEthMonFilterEpDestIpv6,
       "cfprSwSspEthMonFilterEpEcmpId": cfprSwSspEthMonFilterEpEcmpId,
       "cfprSwSspEthMonFilterEpSrcIpv6": cfprSwSspEthMonFilterEpSrcIpv6,
       "cfprSwSspEthMonFilterEpSubvlan": cfprSwSspEthMonFilterEpSubvlan,
       "cfprSwSspEthMonFilterEpVifId": cfprSwSspEthMonFilterEpVifId,
       "cfprSwSspEthMonFsmTable": cfprSwSspEthMonFsmTable,
       "cfprSwSspEthMonFsmEntry": cfprSwSspEthMonFsmEntry,
       "cfprSwSspEthMonFsmInstanceId": cfprSwSspEthMonFsmInstanceId,
       "cfprSwSspEthMonFsmDn": cfprSwSspEthMonFsmDn,
       "cfprSwSspEthMonFsmRn": cfprSwSspEthMonFsmRn,
       "cfprSwSspEthMonFsmCompletionTime": cfprSwSspEthMonFsmCompletionTime,
       "cfprSwSspEthMonFsmCurrentFsm": cfprSwSspEthMonFsmCurrentFsm,
       "cfprSwSspEthMonFsmDescrData": cfprSwSspEthMonFsmDescrData,
       "cfprSwSspEthMonFsmFsmStatus": cfprSwSspEthMonFsmFsmStatus,
       "cfprSwSspEthMonFsmProgress": cfprSwSspEthMonFsmProgress,
       "cfprSwSspEthMonFsmRmtErrCode": cfprSwSspEthMonFsmRmtErrCode,
       "cfprSwSspEthMonFsmRmtErrDescr": cfprSwSspEthMonFsmRmtErrDescr,
       "cfprSwSspEthMonFsmRmtRslt": cfprSwSspEthMonFsmRmtRslt,
       "cfprSwSspEthMonFsmStageTable": cfprSwSspEthMonFsmStageTable,
       "cfprSwSspEthMonFsmStageEntry": cfprSwSspEthMonFsmStageEntry,
       "cfprSwSspEthMonFsmStageInstanceId": cfprSwSspEthMonFsmStageInstanceId,
       "cfprSwSspEthMonFsmStageDn": cfprSwSspEthMonFsmStageDn,
       "cfprSwSspEthMonFsmStageRn": cfprSwSspEthMonFsmStageRn,
       "cfprSwSspEthMonFsmStageDescrData": cfprSwSspEthMonFsmStageDescrData,
       "cfprSwSspEthMonFsmStageLastUpdateTime": cfprSwSspEthMonFsmStageLastUpdateTime,
       "cfprSwSspEthMonFsmStageName": cfprSwSspEthMonFsmStageName,
       "cfprSwSspEthMonFsmStageOrder": cfprSwSspEthMonFsmStageOrder,
       "cfprSwSspEthMonFsmStageRetry": cfprSwSspEthMonFsmStageRetry,
       "cfprSwSspEthMonFsmStageStageStatus": cfprSwSspEthMonFsmStageStageStatus,
       "cfprSwSspEthMonFsmTaskTable": cfprSwSspEthMonFsmTaskTable,
       "cfprSwSspEthMonFsmTaskEntry": cfprSwSspEthMonFsmTaskEntry,
       "cfprSwSspEthMonFsmTaskInstanceId": cfprSwSspEthMonFsmTaskInstanceId,
       "cfprSwSspEthMonFsmTaskDn": cfprSwSspEthMonFsmTaskDn,
       "cfprSwSspEthMonFsmTaskRn": cfprSwSspEthMonFsmTaskRn,
       "cfprSwSspEthMonFsmTaskCompletion": cfprSwSspEthMonFsmTaskCompletion,
       "cfprSwSspEthMonFsmTaskFlags": cfprSwSspEthMonFsmTaskFlags,
       "cfprSwSspEthMonFsmTaskItem": cfprSwSspEthMonFsmTaskItem,
       "cfprSwSspEthMonFsmTaskSeqId": cfprSwSspEthMonFsmTaskSeqId,
       "cfprSwSspEthMonSrcAppEpTable": cfprSwSspEthMonSrcAppEpTable,
       "cfprSwSspEthMonSrcAppEpEntry": cfprSwSspEthMonSrcAppEpEntry,
       "cfprSwSspEthMonSrcAppEpInstanceId": cfprSwSspEthMonSrcAppEpInstanceId,
       "cfprSwSspEthMonSrcAppEpDn": cfprSwSspEthMonSrcAppEpDn,
       "cfprSwSspEthMonSrcAppEpRn": cfprSwSspEthMonSrcAppEpRn,
       "cfprSwSspEthMonSrcAppEpAppName": cfprSwSspEthMonSrcAppEpAppName,
       "cfprSwSspEthMonSrcAppEpExternalPortDn": cfprSwSspEthMonSrcAppEpExternalPortDn,
       "cfprSwSspEthMonSrcAppEpFilter": cfprSwSspEthMonSrcAppEpFilter,
       "cfprSwSspEthMonSrcAppEpFilterDn": cfprSwSspEthMonSrcAppEpFilterDn,
       "cfprSwSspEthMonSrcAppEpLifeCycle": cfprSwSspEthMonSrcAppEpLifeCycle,
       "cfprSwSspEthMonSrcAppEpLinkName": cfprSwSspEthMonSrcAppEpLinkName,
       "cfprSwSspEthMonSrcAppEpPcapfile": cfprSwSspEthMonSrcAppEpPcapfile,
       "cfprSwSspEthMonSrcAppEpPcapfilename": cfprSwSspEthMonSrcAppEpPcapfilename,
       "cfprSwSspEthMonSrcAppEpPcapsize": cfprSwSspEthMonSrcAppEpPcapsize,
       "cfprSwSspEthMonSrcAppEpPortChannelDn": cfprSwSspEthMonSrcAppEpPortChannelDn,
       "cfprSwSspEthMonSrcAppEpPortName": cfprSwSspEthMonSrcAppEpPortName,
       "cfprSwSspEthMonSrcAppEpSlotId": cfprSwSspEthMonSrcAppEpSlotId,
       "cfprSwSspEthMonSrcAppEpPeerDn": cfprSwSspEthMonSrcAppEpPeerDn,
       "cfprSwSspEthMonSrcAppLinksEpTable": cfprSwSspEthMonSrcAppLinksEpTable,
       "cfprSwSspEthMonSrcAppLinksEpEntry": cfprSwSspEthMonSrcAppLinksEpEntry,
       "cfprSwSspEthMonSrcAppLinksEpInstanceId": cfprSwSspEthMonSrcAppLinksEpInstanceId,
       "cfprSwSspEthMonSrcAppLinksEpDn": cfprSwSspEthMonSrcAppLinksEpDn,
       "cfprSwSspEthMonSrcAppLinksEpRn": cfprSwSspEthMonSrcAppLinksEpRn,
       "cfprSwSspEthMonSrcAppLinksEpChassisId": cfprSwSspEthMonSrcAppLinksEpChassisId,
       "cfprSwSspEthMonSrcAppLinksEpEqAggrPortId": cfprSwSspEthMonSrcAppLinksEpEqAggrPortId,
       "cfprSwSspEthMonSrcAppLinksEpEqPortId": cfprSwSspEthMonSrcAppLinksEpEqPortId,
       "cfprSwSspEthMonSrcAppLinksEpEqSlotId": cfprSwSspEthMonSrcAppLinksEpEqSlotId,
       "cfprSwSspEthMonSrcAppLinksEpFilter": cfprSwSspEthMonSrcAppLinksEpFilter,
       "cfprSwSspEthMonSrcAppLinksEpFilterDn": cfprSwSspEthMonSrcAppLinksEpFilterDn,
       "cfprSwSspEthMonSrcAppLinksEpLifeCycle": cfprSwSspEthMonSrcAppLinksEpLifeCycle,
       "cfprSwSspEthMonSrcAppLinksEpName": cfprSwSspEthMonSrcAppLinksEpName,
       "cfprSwSspEthMonSrcAppLinksEpPcapfile": cfprSwSspEthMonSrcAppLinksEpPcapfile,
       "cfprSwSspEthMonSrcAppLinksEpPcapfilename": cfprSwSspEthMonSrcAppLinksEpPcapfilename,
       "cfprSwSspEthMonSrcAppLinksEpPcapsize": cfprSwSspEthMonSrcAppLinksEpPcapsize,
       "cfprSwSspEthMonSrcAppLinksEpSwitchId": cfprSwSspEthMonSrcAppLinksEpSwitchId,
       "cfprSwSspEthMonSrcAppLinksEpVlan": cfprSwSspEthMonSrcAppLinksEpVlan,
       "cfprSwSspEthMonSrcAppLinksEpVnicName1": cfprSwSspEthMonSrcAppLinksEpVnicName1,
       "cfprSwSspEthMonSrcAppLinksEpVifId": cfprSwSspEthMonSrcAppLinksEpVifId,
       "cfprSwSspEthMonSrcPhyEpTable": cfprSwSspEthMonSrcPhyEpTable,
       "cfprSwSspEthMonSrcPhyEpEntry": cfprSwSspEthMonSrcPhyEpEntry,
       "cfprSwSspEthMonSrcPhyEpInstanceId": cfprSwSspEthMonSrcPhyEpInstanceId,
       "cfprSwSspEthMonSrcPhyEpDn": cfprSwSspEthMonSrcPhyEpDn,
       "cfprSwSspEthMonSrcPhyEpRn": cfprSwSspEthMonSrcPhyEpRn,
       "cfprSwSspEthMonSrcPhyEpAggrPortId": cfprSwSspEthMonSrcPhyEpAggrPortId,
       "cfprSwSspEthMonSrcPhyEpChassisId": cfprSwSspEthMonSrcPhyEpChassisId,
       "cfprSwSspEthMonSrcPhyEpFilter": cfprSwSspEthMonSrcPhyEpFilter,
       "cfprSwSspEthMonSrcPhyEpFilterDn": cfprSwSspEthMonSrcPhyEpFilterDn,
       "cfprSwSspEthMonSrcPhyEpLifeCycle": cfprSwSspEthMonSrcPhyEpLifeCycle,
       "cfprSwSspEthMonSrcPhyEpPcapfile": cfprSwSspEthMonSrcPhyEpPcapfile,
       "cfprSwSspEthMonSrcPhyEpPcapfilename": cfprSwSspEthMonSrcPhyEpPcapfilename,
       "cfprSwSspEthMonSrcPhyEpPcapsize": cfprSwSspEthMonSrcPhyEpPcapsize,
       "cfprSwSspEthMonSrcPhyEpPortId": cfprSwSspEthMonSrcPhyEpPortId,
       "cfprSwSspEthMonSrcPhyEpSlotId": cfprSwSspEthMonSrcPhyEpSlotId,
       "cfprSwSspEthMonSrcPhyEpSwitchId": cfprSwSspEthMonSrcPhyEpSwitchId,
       "cfprSwSspEthMonSrcPhyEpFsmDescr": cfprSwSspEthMonSrcPhyEpFsmDescr,
       "cfprSwSspEthMonSrcPhyEpFsmPrev": cfprSwSspEthMonSrcPhyEpFsmPrev,
       "cfprSwSspEthMonSrcPhyEpFsmProgr": cfprSwSspEthMonSrcPhyEpFsmProgr,
       "cfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode": cfprSwSspEthMonSrcPhyEpFsmRmtInvErrCode,
       "cfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr": cfprSwSspEthMonSrcPhyEpFsmRmtInvErrDescr,
       "cfprSwSspEthMonSrcPhyEpFsmRmtInvRslt": cfprSwSspEthMonSrcPhyEpFsmRmtInvRslt,
       "cfprSwSspEthMonSrcPhyEpFsmStageDescr": cfprSwSspEthMonSrcPhyEpFsmStageDescr,
       "cfprSwSspEthMonSrcPhyEpFsmStamp": cfprSwSspEthMonSrcPhyEpFsmStamp,
       "cfprSwSspEthMonSrcPhyEpFsmStatus": cfprSwSspEthMonSrcPhyEpFsmStatus,
       "cfprSwSspEthMonSrcPhyEpFsmTry": cfprSwSspEthMonSrcPhyEpFsmTry,
       "cfprSwSspEthMonSrcPhyEpPeerDn": cfprSwSspEthMonSrcPhyEpPeerDn,
       "cfprSwSspEthMonSrcPhyEpEcmpId": cfprSwSspEthMonSrcPhyEpEcmpId,
       "cfprSwSspEthMonSrcPhyEpSubIfVlan": cfprSwSspEthMonSrcPhyEpSubIfVlan,
       "cfprSwSspEthMonSrcPhyEpFsmTable": cfprSwSspEthMonSrcPhyEpFsmTable,
       "cfprSwSspEthMonSrcPhyEpFsmEntry": cfprSwSspEthMonSrcPhyEpFsmEntry,
       "cfprSwSspEthMonSrcPhyEpFsmInstanceId": cfprSwSspEthMonSrcPhyEpFsmInstanceId,
       "cfprSwSspEthMonSrcPhyEpFsmDn": cfprSwSspEthMonSrcPhyEpFsmDn,
       "cfprSwSspEthMonSrcPhyEpFsmRn": cfprSwSspEthMonSrcPhyEpFsmRn,
       "cfprSwSspEthMonSrcPhyEpFsmCompletionTime": cfprSwSspEthMonSrcPhyEpFsmCompletionTime,
       "cfprSwSspEthMonSrcPhyEpFsmCurrentFsm": cfprSwSspEthMonSrcPhyEpFsmCurrentFsm,
       "cfprSwSspEthMonSrcPhyEpFsmDescrData": cfprSwSspEthMonSrcPhyEpFsmDescrData,
       "cfprSwSspEthMonSrcPhyEpFsmFsmStatus": cfprSwSspEthMonSrcPhyEpFsmFsmStatus,
       "cfprSwSspEthMonSrcPhyEpFsmProgress": cfprSwSspEthMonSrcPhyEpFsmProgress,
       "cfprSwSspEthMonSrcPhyEpFsmRmtErrCode": cfprSwSspEthMonSrcPhyEpFsmRmtErrCode,
       "cfprSwSspEthMonSrcPhyEpFsmRmtErrDescr": cfprSwSspEthMonSrcPhyEpFsmRmtErrDescr,
       "cfprSwSspEthMonSrcPhyEpFsmRmtRslt": cfprSwSspEthMonSrcPhyEpFsmRmtRslt,
       "cfprSwSspEthMonSrcPhyEpFsmStageTable": cfprSwSspEthMonSrcPhyEpFsmStageTable,
       "cfprSwSspEthMonSrcPhyEpFsmStageEntry": cfprSwSspEthMonSrcPhyEpFsmStageEntry,
       "cfprSwSspEthMonSrcPhyEpFsmStageInstanceId": cfprSwSspEthMonSrcPhyEpFsmStageInstanceId,
       "cfprSwSspEthMonSrcPhyEpFsmStageDn": cfprSwSspEthMonSrcPhyEpFsmStageDn,
       "cfprSwSspEthMonSrcPhyEpFsmStageRn": cfprSwSspEthMonSrcPhyEpFsmStageRn,
       "cfprSwSspEthMonSrcPhyEpFsmStageDescrData": cfprSwSspEthMonSrcPhyEpFsmStageDescrData,
       "cfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime": cfprSwSspEthMonSrcPhyEpFsmStageLastUpdateTime,
       "cfprSwSspEthMonSrcPhyEpFsmStageName": cfprSwSspEthMonSrcPhyEpFsmStageName,
       "cfprSwSspEthMonSrcPhyEpFsmStageOrder": cfprSwSspEthMonSrcPhyEpFsmStageOrder,
       "cfprSwSspEthMonSrcPhyEpFsmStageRetry": cfprSwSspEthMonSrcPhyEpFsmStageRetry,
       "cfprSwSspEthMonSrcPhyEpFsmStageStageStatus": cfprSwSspEthMonSrcPhyEpFsmStageStageStatus,
       "cfprSwSspEthMonSrcPhyEpFsmTaskTable": cfprSwSspEthMonSrcPhyEpFsmTaskTable,
       "cfprSwSspEthMonSrcPhyEpFsmTaskEntry": cfprSwSspEthMonSrcPhyEpFsmTaskEntry,
       "cfprSwSspEthMonSrcPhyEpFsmTaskInstanceId": cfprSwSspEthMonSrcPhyEpFsmTaskInstanceId,
       "cfprSwSspEthMonSrcPhyEpFsmTaskDn": cfprSwSspEthMonSrcPhyEpFsmTaskDn,
       "cfprSwSspEthMonSrcPhyEpFsmTaskRn": cfprSwSspEthMonSrcPhyEpFsmTaskRn,
       "cfprSwSspEthMonSrcPhyEpFsmTaskCompletion": cfprSwSspEthMonSrcPhyEpFsmTaskCompletion,
       "cfprSwSspEthMonSrcPhyEpFsmTaskFlags": cfprSwSspEthMonSrcPhyEpFsmTaskFlags,
       "cfprSwSspEthMonSrcPhyEpFsmTaskItem": cfprSwSspEthMonSrcPhyEpFsmTaskItem,
       "cfprSwSspEthMonSrcPhyEpFsmTaskSeqId": cfprSwSspEthMonSrcPhyEpFsmTaskSeqId}
)
