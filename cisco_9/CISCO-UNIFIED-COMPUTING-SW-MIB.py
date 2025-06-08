# SNMP MIB module (CISCO-UNIFIED-COMPUTING-SW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UNIFIED-COMPUTING-SW-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:39 2025
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

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsConditionRemoteInvRslt,
 CucsDpsecForgedTransmit,
 CucsFabricAVlanAssocPrimaryVlanSwitchId,
 CucsFabricAVlanSharing,
 CucsFabricAVlanTransport,
 CucsFabricAVlanType,
 CucsFabricAVsanTransport,
 CucsFabricAVsanType,
 CucsFabricAdminState,
 CucsFabricDefaultZoningState,
 CucsFabricDirection,
 CucsFabricEpVlanVlanType,
 CucsFabricEthEstcPortMode,
 CucsFabricEthPcProtocol,
 CucsFabricExternalEpLocale,
 CucsFabricFcZoneSharingMode,
 CucsFabricFillPattern,
 CucsFabricFlowMonIpv4Keys,
 CucsFabricFlowMonIpv6Keys,
 CucsFabricFlowMonKeyType,
 CucsFabricFlowMonL2Keys,
 CucsFabricFlowMonNonKeys,
 CucsFabricNFExporterVersion,
 CucsFabricNFTransport,
 CucsFabricPIoEpIfType,
 CucsFabricPIoEpOperState,
 CucsFabricPIoEpPortId,
 CucsFabricPIoEpSlotId,
 CucsFabricRecoveryAction,
 CucsFabricTrafficDirection,
 CucsFabricVlanAssocPrimaryVlanState,
 CucsFabricVlanOperState,
 CucsFabricVlanOverlapState,
 CucsFabricVnetEpIfRole,
 CucsFabricVnetEpLocale,
 CucsFabricVnetEpPolicyOwner,
 CucsFabricVsanOperState,
 CucsFabricWarnings,
 CucsFabricZoningState,
 CucsFlowctrlFlowControl,
 CucsFlowctrlPriorityPause,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsFsmLifecycle,
 CucsLicenseState,
 CucsLsFcZoneState,
 CucsNetworkConnectionType,
 CucsNetworkLocale,
 CucsNetworkPortRole,
 CucsNetworkSwitchId,
 CucsNetworkTransport,
 CucsNetworkVlanCountStatus,
 CucsNetworkVnetEpIfType,
 CucsNwctrlAdminState,
 CucsNwctrlLinkFailAction,
 CucsPortEthAdminSpeed,
 CucsPortEthSpeed,
 CucsPortSpeed,
 CucsSwAccessDomainFsmCurrentFsm,
 CucsSwAccessDomainFsmStageName,
 CucsSwAccessDomainFsmTaskItem,
 CucsSwAccessDomainLocale,
 CucsSwAccessDomainType,
 CucsSwAccessEpLocale,
 CucsSwAccessEpTransport,
 CucsSwAutoNegMode,
 CucsSwBorderDomainLocale,
 CucsSwBorderEpLocale,
 CucsSwBorderPcLocale,
 CucsSwBreakoutType,
 CucsSwCIoEpIfType,
 CucsSwCardEnvStatsHistThresholded,
 CucsSwCardEnvStatsThresholded,
 CucsSwCimcId,
 CucsSwConfMode,
 CucsSwConfigStatus,
 CucsSwEnvStatsHistThresholded,
 CucsSwEnvStatsThresholded,
 CucsSwEstcEpLocale,
 CucsSwEthEstcEpTransport,
 CucsSwEthEstcPcTransport,
 CucsSwEthFlowMonSessionTransport,
 CucsSwEthFlowMonSessionType,
 CucsSwEthLanBorderFsmCurrentFsm,
 CucsSwEthLanBorderFsmStageName,
 CucsSwEthLanBorderFsmTaskFlags,
 CucsSwEthLanBorderFsmTaskItem,
 CucsSwEthLanBorderTransport,
 CucsSwEthLanEpTransport,
 CucsSwEthLanEpUdldAdminState,
 CucsSwEthLanEpUdldMode,
 CucsSwEthLanFlowMonExporterTransport,
 CucsSwEthLanFlowMonExporterType,
 CucsSwEthLanFlowMonFsmCurrentFsm,
 CucsSwEthLanFlowMonFsmStageName,
 CucsSwEthLanFlowMonFsmTaskItem,
 CucsSwEthLanFlowMonTransport,
 CucsSwEthLanFlowMonitorTransport,
 CucsSwEthLanFlowMonitorType,
 CucsSwEthLanFlowRecordDefTransport,
 CucsSwEthLanFlowRecordDefType,
 CucsSwEthLanMonTransport,
 CucsSwEthLanPcTransport,
 CucsSwEthMonDestEpTransport,
 CucsSwEthMonFsmCurrentFsm,
 CucsSwEthMonFsmStageName,
 CucsSwEthMonFsmTaskItem,
 CucsSwEthMonSrcEpTransport,
 CucsSwEthMonTransport,
 CucsSwEthMonType,
 CucsSwEthTargetEpAdminState,
 CucsSwEthTargetEpTransport,
 CucsSwExtUtilityFsmCurrentFsm,
 CucsSwExtUtilityFsmStageName,
 CucsSwExtUtilityFsmTaskItem,
 CucsSwFabricZoneNsAllocStatus,
 CucsSwFcEstcEpTransport,
 CucsSwFcMonDestEpTransport,
 CucsSwFcMonFsmCurrentFsm,
 CucsSwFcMonFsmStageName,
 CucsSwFcMonFsmTaskItem,
 CucsSwFcMonSrcEpTransport,
 CucsSwFcMonTransport,
 CucsSwFcMonType,
 CucsSwFcSanBorderFsmCurrentFsm,
 CucsSwFcSanBorderFsmStageName,
 CucsSwFcSanBorderFsmTaskItem,
 CucsSwFcSanBorderTransport,
 CucsSwFcSanBorderUplinkTrunking,
 CucsSwFcSanEpTransport,
 CucsSwFcSanMonTransport,
 CucsSwFcSanPcTransport,
 CucsSwFcServerZoneGroupLc,
 CucsSwFcZoneLc,
 CucsSwFcZoneMemberLc,
 CucsSwFcZoneSetLc,
 CucsSwFcoeEstcEpTransport,
 CucsSwFcoeSanEpTransport,
 CucsSwFcoeSanEpUdldAdminState,
 CucsSwFcoeSanEpUdldMode,
 CucsSwFcoeSanPcTransport,
 CucsSwFlowMonitorAdminState,
 CucsSwLanBorderType,
 CucsSwLanEpIfRole,
 CucsSwLanEpType,
 CucsSwLanMonType,
 CucsSwLanPcIfRole,
 CucsSwLanPcType,
 CucsSwMonAdminState,
 CucsSwMonDomainLocale,
 CucsSwMonLifeCycle,
 CucsSwMonSrcEpLocale,
 CucsSwNFConfigStatus,
 CucsSwNetflowExporterProtocol,
 CucsSwNetflowMonSessionProtocol,
 CucsSwNetflowMonitorProtocol,
 CucsSwNetflowRecordDefProtocol,
 CucsSwPIoEpIfType,
 CucsSwPIoEpLc,
 CucsSwPeerStatus,
 CucsSwPhysFsmCurrentFsm,
 CucsSwPhysFsmStageName,
 CucsSwPhysFsmTaskItem,
 CucsSwPortBreakoutPortId,
 CucsSwPortBreakoutSlotId,
 CucsSwSanBorderType,
 CucsSwSanEpIfRole,
 CucsSwSanEpType,
 CucsSwSanMonType,
 CucsSwSanPcIfRole,
 CucsSwSanPcType,
 CucsSwSubGroupAggrPortId,
 CucsSwSubGroupSlotId,
 CucsSwSystemStatsHistThresholded,
 CucsSwSystemStatsThresholded,
 CucsSwTargetEpType,
 CucsSwUlanPurpose,
 CucsSwUtilityDomainFsmCurrentFsm,
 CucsSwUtilityDomainFsmStageName,
 CucsSwUtilityDomainFsmTaskItem,
 CucsSwUtilityDomainLocale,
 CucsSwUtilityDomainType,
 CucsSwVlanCompType,
 CucsSwVlanConfigStatusType,
 CucsSwVlanGroupType,
 CucsSwVlanLc,
 CucsSwVlanPortNsAllocStatus) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsConditionRemoteInvRslt",
    "CucsDpsecForgedTransmit",
    "CucsFabricAVlanAssocPrimaryVlanSwitchId",
    "CucsFabricAVlanSharing",
    "CucsFabricAVlanTransport",
    "CucsFabricAVlanType",
    "CucsFabricAVsanTransport",
    "CucsFabricAVsanType",
    "CucsFabricAdminState",
    "CucsFabricDefaultZoningState",
    "CucsFabricDirection",
    "CucsFabricEpVlanVlanType",
    "CucsFabricEthEstcPortMode",
    "CucsFabricEthPcProtocol",
    "CucsFabricExternalEpLocale",
    "CucsFabricFcZoneSharingMode",
    "CucsFabricFillPattern",
    "CucsFabricFlowMonIpv4Keys",
    "CucsFabricFlowMonIpv6Keys",
    "CucsFabricFlowMonKeyType",
    "CucsFabricFlowMonL2Keys",
    "CucsFabricFlowMonNonKeys",
    "CucsFabricNFExporterVersion",
    "CucsFabricNFTransport",
    "CucsFabricPIoEpIfType",
    "CucsFabricPIoEpOperState",
    "CucsFabricPIoEpPortId",
    "CucsFabricPIoEpSlotId",
    "CucsFabricRecoveryAction",
    "CucsFabricTrafficDirection",
    "CucsFabricVlanAssocPrimaryVlanState",
    "CucsFabricVlanOperState",
    "CucsFabricVlanOverlapState",
    "CucsFabricVnetEpIfRole",
    "CucsFabricVnetEpLocale",
    "CucsFabricVnetEpPolicyOwner",
    "CucsFabricVsanOperState",
    "CucsFabricWarnings",
    "CucsFabricZoningState",
    "CucsFlowctrlFlowControl",
    "CucsFlowctrlPriorityPause",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsFsmLifecycle",
    "CucsLicenseState",
    "CucsLsFcZoneState",
    "CucsNetworkConnectionType",
    "CucsNetworkLocale",
    "CucsNetworkPortRole",
    "CucsNetworkSwitchId",
    "CucsNetworkTransport",
    "CucsNetworkVlanCountStatus",
    "CucsNetworkVnetEpIfType",
    "CucsNwctrlAdminState",
    "CucsNwctrlLinkFailAction",
    "CucsPortEthAdminSpeed",
    "CucsPortEthSpeed",
    "CucsPortSpeed",
    "CucsSwAccessDomainFsmCurrentFsm",
    "CucsSwAccessDomainFsmStageName",
    "CucsSwAccessDomainFsmTaskItem",
    "CucsSwAccessDomainLocale",
    "CucsSwAccessDomainType",
    "CucsSwAccessEpLocale",
    "CucsSwAccessEpTransport",
    "CucsSwAutoNegMode",
    "CucsSwBorderDomainLocale",
    "CucsSwBorderEpLocale",
    "CucsSwBorderPcLocale",
    "CucsSwBreakoutType",
    "CucsSwCIoEpIfType",
    "CucsSwCardEnvStatsHistThresholded",
    "CucsSwCardEnvStatsThresholded",
    "CucsSwCimcId",
    "CucsSwConfMode",
    "CucsSwConfigStatus",
    "CucsSwEnvStatsHistThresholded",
    "CucsSwEnvStatsThresholded",
    "CucsSwEstcEpLocale",
    "CucsSwEthEstcEpTransport",
    "CucsSwEthEstcPcTransport",
    "CucsSwEthFlowMonSessionTransport",
    "CucsSwEthFlowMonSessionType",
    "CucsSwEthLanBorderFsmCurrentFsm",
    "CucsSwEthLanBorderFsmStageName",
    "CucsSwEthLanBorderFsmTaskFlags",
    "CucsSwEthLanBorderFsmTaskItem",
    "CucsSwEthLanBorderTransport",
    "CucsSwEthLanEpTransport",
    "CucsSwEthLanEpUdldAdminState",
    "CucsSwEthLanEpUdldMode",
    "CucsSwEthLanFlowMonExporterTransport",
    "CucsSwEthLanFlowMonExporterType",
    "CucsSwEthLanFlowMonFsmCurrentFsm",
    "CucsSwEthLanFlowMonFsmStageName",
    "CucsSwEthLanFlowMonFsmTaskItem",
    "CucsSwEthLanFlowMonTransport",
    "CucsSwEthLanFlowMonitorTransport",
    "CucsSwEthLanFlowMonitorType",
    "CucsSwEthLanFlowRecordDefTransport",
    "CucsSwEthLanFlowRecordDefType",
    "CucsSwEthLanMonTransport",
    "CucsSwEthLanPcTransport",
    "CucsSwEthMonDestEpTransport",
    "CucsSwEthMonFsmCurrentFsm",
    "CucsSwEthMonFsmStageName",
    "CucsSwEthMonFsmTaskItem",
    "CucsSwEthMonSrcEpTransport",
    "CucsSwEthMonTransport",
    "CucsSwEthMonType",
    "CucsSwEthTargetEpAdminState",
    "CucsSwEthTargetEpTransport",
    "CucsSwExtUtilityFsmCurrentFsm",
    "CucsSwExtUtilityFsmStageName",
    "CucsSwExtUtilityFsmTaskItem",
    "CucsSwFabricZoneNsAllocStatus",
    "CucsSwFcEstcEpTransport",
    "CucsSwFcMonDestEpTransport",
    "CucsSwFcMonFsmCurrentFsm",
    "CucsSwFcMonFsmStageName",
    "CucsSwFcMonFsmTaskItem",
    "CucsSwFcMonSrcEpTransport",
    "CucsSwFcMonTransport",
    "CucsSwFcMonType",
    "CucsSwFcSanBorderFsmCurrentFsm",
    "CucsSwFcSanBorderFsmStageName",
    "CucsSwFcSanBorderFsmTaskItem",
    "CucsSwFcSanBorderTransport",
    "CucsSwFcSanBorderUplinkTrunking",
    "CucsSwFcSanEpTransport",
    "CucsSwFcSanMonTransport",
    "CucsSwFcSanPcTransport",
    "CucsSwFcServerZoneGroupLc",
    "CucsSwFcZoneLc",
    "CucsSwFcZoneMemberLc",
    "CucsSwFcZoneSetLc",
    "CucsSwFcoeEstcEpTransport",
    "CucsSwFcoeSanEpTransport",
    "CucsSwFcoeSanEpUdldAdminState",
    "CucsSwFcoeSanEpUdldMode",
    "CucsSwFcoeSanPcTransport",
    "CucsSwFlowMonitorAdminState",
    "CucsSwLanBorderType",
    "CucsSwLanEpIfRole",
    "CucsSwLanEpType",
    "CucsSwLanMonType",
    "CucsSwLanPcIfRole",
    "CucsSwLanPcType",
    "CucsSwMonAdminState",
    "CucsSwMonDomainLocale",
    "CucsSwMonLifeCycle",
    "CucsSwMonSrcEpLocale",
    "CucsSwNFConfigStatus",
    "CucsSwNetflowExporterProtocol",
    "CucsSwNetflowMonSessionProtocol",
    "CucsSwNetflowMonitorProtocol",
    "CucsSwNetflowRecordDefProtocol",
    "CucsSwPIoEpIfType",
    "CucsSwPIoEpLc",
    "CucsSwPeerStatus",
    "CucsSwPhysFsmCurrentFsm",
    "CucsSwPhysFsmStageName",
    "CucsSwPhysFsmTaskItem",
    "CucsSwPortBreakoutPortId",
    "CucsSwPortBreakoutSlotId",
    "CucsSwSanBorderType",
    "CucsSwSanEpIfRole",
    "CucsSwSanEpType",
    "CucsSwSanMonType",
    "CucsSwSanPcIfRole",
    "CucsSwSanPcType",
    "CucsSwSubGroupAggrPortId",
    "CucsSwSubGroupSlotId",
    "CucsSwSystemStatsHistThresholded",
    "CucsSwSystemStatsThresholded",
    "CucsSwTargetEpType",
    "CucsSwUlanPurpose",
    "CucsSwUtilityDomainFsmCurrentFsm",
    "CucsSwUtilityDomainFsmStageName",
    "CucsSwUtilityDomainFsmTaskItem",
    "CucsSwUtilityDomainLocale",
    "CucsSwUtilityDomainType",
    "CucsSwVlanCompType",
    "CucsSwVlanConfigStatusType",
    "CucsSwVlanGroupType",
    "CucsSwVlanLc",
    "CucsSwVlanPortNsAllocStatus")

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

cucsSwObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsSwAccessDomainTable_Object = MibTable
cucsSwAccessDomainTable = _CucsSwAccessDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1)
)
if mibBuilder.loadTexts:
    cucsSwAccessDomainTable.setStatus("current")
_CucsSwAccessDomainEntry_Object = MibTableRow
cucsSwAccessDomainEntry = _CucsSwAccessDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1)
)
cucsSwAccessDomainEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwAccessDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwAccessDomainEntry.setStatus("current")
_CucsSwAccessDomainInstanceId_Type = CucsManagedObjectId
_CucsSwAccessDomainInstanceId_Object = MibTableColumn
cucsSwAccessDomainInstanceId = _CucsSwAccessDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 1),
    _CucsSwAccessDomainInstanceId_Type()
)
cucsSwAccessDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwAccessDomainInstanceId.setStatus("current")
_CucsSwAccessDomainDn_Type = CucsManagedObjectDn
_CucsSwAccessDomainDn_Object = MibTableColumn
cucsSwAccessDomainDn = _CucsSwAccessDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 2),
    _CucsSwAccessDomainDn_Type()
)
cucsSwAccessDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainDn.setStatus("current")
_CucsSwAccessDomainRn_Type = SnmpAdminString
_CucsSwAccessDomainRn_Object = MibTableColumn
cucsSwAccessDomainRn = _CucsSwAccessDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 3),
    _CucsSwAccessDomainRn_Type()
)
cucsSwAccessDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainRn.setStatus("current")
_CucsSwAccessDomainFsmDescr_Type = SnmpAdminString
_CucsSwAccessDomainFsmDescr_Object = MibTableColumn
cucsSwAccessDomainFsmDescr = _CucsSwAccessDomainFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 4),
    _CucsSwAccessDomainFsmDescr_Type()
)
cucsSwAccessDomainFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmDescr.setStatus("current")
_CucsSwAccessDomainFsmPrev_Type = SnmpAdminString
_CucsSwAccessDomainFsmPrev_Object = MibTableColumn
cucsSwAccessDomainFsmPrev = _CucsSwAccessDomainFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 5),
    _CucsSwAccessDomainFsmPrev_Type()
)
cucsSwAccessDomainFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmPrev.setStatus("current")
_CucsSwAccessDomainFsmProgr_Type = Gauge32
_CucsSwAccessDomainFsmProgr_Object = MibTableColumn
cucsSwAccessDomainFsmProgr = _CucsSwAccessDomainFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 6),
    _CucsSwAccessDomainFsmProgr_Type()
)
cucsSwAccessDomainFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmProgr.setStatus("current")
_CucsSwAccessDomainFsmRmtInvErrCode_Type = Gauge32
_CucsSwAccessDomainFsmRmtInvErrCode_Object = MibTableColumn
cucsSwAccessDomainFsmRmtInvErrCode = _CucsSwAccessDomainFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 7),
    _CucsSwAccessDomainFsmRmtInvErrCode_Type()
)
cucsSwAccessDomainFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmRmtInvErrCode.setStatus("current")
_CucsSwAccessDomainFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwAccessDomainFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwAccessDomainFsmRmtInvErrDescr = _CucsSwAccessDomainFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 8),
    _CucsSwAccessDomainFsmRmtInvErrDescr_Type()
)
cucsSwAccessDomainFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmRmtInvErrDescr.setStatus("current")
_CucsSwAccessDomainFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwAccessDomainFsmRmtInvRslt_Object = MibTableColumn
cucsSwAccessDomainFsmRmtInvRslt = _CucsSwAccessDomainFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 9),
    _CucsSwAccessDomainFsmRmtInvRslt_Type()
)
cucsSwAccessDomainFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmRmtInvRslt.setStatus("current")
_CucsSwAccessDomainFsmStageDescr_Type = SnmpAdminString
_CucsSwAccessDomainFsmStageDescr_Object = MibTableColumn
cucsSwAccessDomainFsmStageDescr = _CucsSwAccessDomainFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 10),
    _CucsSwAccessDomainFsmStageDescr_Type()
)
cucsSwAccessDomainFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageDescr.setStatus("current")
_CucsSwAccessDomainFsmStamp_Type = DateAndTime
_CucsSwAccessDomainFsmStamp_Object = MibTableColumn
cucsSwAccessDomainFsmStamp = _CucsSwAccessDomainFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 11),
    _CucsSwAccessDomainFsmStamp_Type()
)
cucsSwAccessDomainFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStamp.setStatus("current")
_CucsSwAccessDomainFsmStatus_Type = SnmpAdminString
_CucsSwAccessDomainFsmStatus_Object = MibTableColumn
cucsSwAccessDomainFsmStatus = _CucsSwAccessDomainFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 12),
    _CucsSwAccessDomainFsmStatus_Type()
)
cucsSwAccessDomainFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStatus.setStatus("current")
_CucsSwAccessDomainFsmTry_Type = Gauge32
_CucsSwAccessDomainFsmTry_Object = MibTableColumn
cucsSwAccessDomainFsmTry = _CucsSwAccessDomainFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 13),
    _CucsSwAccessDomainFsmTry_Type()
)
cucsSwAccessDomainFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTry.setStatus("current")
_CucsSwAccessDomainLocale_Type = CucsSwAccessDomainLocale
_CucsSwAccessDomainLocale_Object = MibTableColumn
cucsSwAccessDomainLocale = _CucsSwAccessDomainLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 14),
    _CucsSwAccessDomainLocale_Type()
)
cucsSwAccessDomainLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainLocale.setStatus("current")
_CucsSwAccessDomainName_Type = SnmpAdminString
_CucsSwAccessDomainName_Object = MibTableColumn
cucsSwAccessDomainName = _CucsSwAccessDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 15),
    _CucsSwAccessDomainName_Type()
)
cucsSwAccessDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainName.setStatus("current")
_CucsSwAccessDomainSwitchId_Type = CucsNetworkSwitchId
_CucsSwAccessDomainSwitchId_Object = MibTableColumn
cucsSwAccessDomainSwitchId = _CucsSwAccessDomainSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 16),
    _CucsSwAccessDomainSwitchId_Type()
)
cucsSwAccessDomainSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainSwitchId.setStatus("current")
_CucsSwAccessDomainTransport_Type = CucsNetworkTransport
_CucsSwAccessDomainTransport_Object = MibTableColumn
cucsSwAccessDomainTransport = _CucsSwAccessDomainTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 17),
    _CucsSwAccessDomainTransport_Type()
)
cucsSwAccessDomainTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainTransport.setStatus("current")
_CucsSwAccessDomainType_Type = CucsSwAccessDomainType
_CucsSwAccessDomainType_Object = MibTableColumn
cucsSwAccessDomainType = _CucsSwAccessDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 1, 1, 18),
    _CucsSwAccessDomainType_Type()
)
cucsSwAccessDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainType.setStatus("current")
_CucsSwAccessDomainFsmTaskTable_Object = MibTable
cucsSwAccessDomainFsmTaskTable = _CucsSwAccessDomainFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2)
)
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskTable.setStatus("current")
_CucsSwAccessDomainFsmTaskEntry_Object = MibTableRow
cucsSwAccessDomainFsmTaskEntry = _CucsSwAccessDomainFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2, 1)
)
cucsSwAccessDomainFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwAccessDomainFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskEntry.setStatus("current")
_CucsSwAccessDomainFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwAccessDomainFsmTaskInstanceId_Object = MibTableColumn
cucsSwAccessDomainFsmTaskInstanceId = _CucsSwAccessDomainFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2, 1, 1),
    _CucsSwAccessDomainFsmTaskInstanceId_Type()
)
cucsSwAccessDomainFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskInstanceId.setStatus("current")
_CucsSwAccessDomainFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwAccessDomainFsmTaskDn_Object = MibTableColumn
cucsSwAccessDomainFsmTaskDn = _CucsSwAccessDomainFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2, 1, 2),
    _CucsSwAccessDomainFsmTaskDn_Type()
)
cucsSwAccessDomainFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskDn.setStatus("current")
_CucsSwAccessDomainFsmTaskRn_Type = SnmpAdminString
_CucsSwAccessDomainFsmTaskRn_Object = MibTableColumn
cucsSwAccessDomainFsmTaskRn = _CucsSwAccessDomainFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2, 1, 3),
    _CucsSwAccessDomainFsmTaskRn_Type()
)
cucsSwAccessDomainFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskRn.setStatus("current")
_CucsSwAccessDomainFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwAccessDomainFsmTaskCompletion_Object = MibTableColumn
cucsSwAccessDomainFsmTaskCompletion = _CucsSwAccessDomainFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2, 1, 4),
    _CucsSwAccessDomainFsmTaskCompletion_Type()
)
cucsSwAccessDomainFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskCompletion.setStatus("current")
_CucsSwAccessDomainFsmTaskFlags_Type = CucsFsmFlags
_CucsSwAccessDomainFsmTaskFlags_Object = MibTableColumn
cucsSwAccessDomainFsmTaskFlags = _CucsSwAccessDomainFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2, 1, 5),
    _CucsSwAccessDomainFsmTaskFlags_Type()
)
cucsSwAccessDomainFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskFlags.setStatus("current")
_CucsSwAccessDomainFsmTaskItem_Type = CucsSwAccessDomainFsmTaskItem
_CucsSwAccessDomainFsmTaskItem_Object = MibTableColumn
cucsSwAccessDomainFsmTaskItem = _CucsSwAccessDomainFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2, 1, 6),
    _CucsSwAccessDomainFsmTaskItem_Type()
)
cucsSwAccessDomainFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskItem.setStatus("current")
_CucsSwAccessDomainFsmTaskSeqId_Type = Gauge32
_CucsSwAccessDomainFsmTaskSeqId_Object = MibTableColumn
cucsSwAccessDomainFsmTaskSeqId = _CucsSwAccessDomainFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 2, 1, 7),
    _CucsSwAccessDomainFsmTaskSeqId_Type()
)
cucsSwAccessDomainFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTaskSeqId.setStatus("current")
_CucsSwAccessEpTable_Object = MibTable
cucsSwAccessEpTable = _CucsSwAccessEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3)
)
if mibBuilder.loadTexts:
    cucsSwAccessEpTable.setStatus("current")
_CucsSwAccessEpEntry_Object = MibTableRow
cucsSwAccessEpEntry = _CucsSwAccessEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1)
)
cucsSwAccessEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwAccessEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwAccessEpEntry.setStatus("current")
_CucsSwAccessEpInstanceId_Type = CucsManagedObjectId
_CucsSwAccessEpInstanceId_Object = MibTableColumn
cucsSwAccessEpInstanceId = _CucsSwAccessEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 1),
    _CucsSwAccessEpInstanceId_Type()
)
cucsSwAccessEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwAccessEpInstanceId.setStatus("current")
_CucsSwAccessEpDn_Type = CucsManagedObjectDn
_CucsSwAccessEpDn_Object = MibTableColumn
cucsSwAccessEpDn = _CucsSwAccessEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 2),
    _CucsSwAccessEpDn_Type()
)
cucsSwAccessEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpDn.setStatus("current")
_CucsSwAccessEpRn_Type = SnmpAdminString
_CucsSwAccessEpRn_Object = MibTableColumn
cucsSwAccessEpRn = _CucsSwAccessEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 3),
    _CucsSwAccessEpRn_Type()
)
cucsSwAccessEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpRn.setStatus("current")
_CucsSwAccessEpAdminState_Type = CucsFabricAdminState
_CucsSwAccessEpAdminState_Object = MibTableColumn
cucsSwAccessEpAdminState = _CucsSwAccessEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 4),
    _CucsSwAccessEpAdminState_Type()
)
cucsSwAccessEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpAdminState.setStatus("current")
_CucsSwAccessEpChassisId_Type = Gauge32
_CucsSwAccessEpChassisId_Object = MibTableColumn
cucsSwAccessEpChassisId = _CucsSwAccessEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 5),
    _CucsSwAccessEpChassisId_Type()
)
cucsSwAccessEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpChassisId.setStatus("current")
_CucsSwAccessEpEpDn_Type = SnmpAdminString
_CucsSwAccessEpEpDn_Object = MibTableColumn
cucsSwAccessEpEpDn = _CucsSwAccessEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 6),
    _CucsSwAccessEpEpDn_Type()
)
cucsSwAccessEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpEpDn.setStatus("current")
_CucsSwAccessEpIfRole_Type = CucsNetworkPortRole
_CucsSwAccessEpIfRole_Object = MibTableColumn
cucsSwAccessEpIfRole = _CucsSwAccessEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 7),
    _CucsSwAccessEpIfRole_Type()
)
cucsSwAccessEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpIfRole.setStatus("current")
_CucsSwAccessEpIfType_Type = CucsSwPIoEpIfType
_CucsSwAccessEpIfType_Object = MibTableColumn
cucsSwAccessEpIfType = _CucsSwAccessEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 8),
    _CucsSwAccessEpIfType_Type()
)
cucsSwAccessEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpIfType.setStatus("current")
_CucsSwAccessEpLocale_Type = CucsSwAccessEpLocale
_CucsSwAccessEpLocale_Object = MibTableColumn
cucsSwAccessEpLocale = _CucsSwAccessEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 9),
    _CucsSwAccessEpLocale_Type()
)
cucsSwAccessEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpLocale.setStatus("current")
_CucsSwAccessEpName_Type = SnmpAdminString
_CucsSwAccessEpName_Object = MibTableColumn
cucsSwAccessEpName = _CucsSwAccessEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 10),
    _CucsSwAccessEpName_Type()
)
cucsSwAccessEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpName.setStatus("current")
_CucsSwAccessEpPeerDn_Type = SnmpAdminString
_CucsSwAccessEpPeerDn_Object = MibTableColumn
cucsSwAccessEpPeerDn = _CucsSwAccessEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 11),
    _CucsSwAccessEpPeerDn_Type()
)
cucsSwAccessEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpPeerDn.setStatus("current")
_CucsSwAccessEpPeerPortId_Type = Gauge32
_CucsSwAccessEpPeerPortId_Object = MibTableColumn
cucsSwAccessEpPeerPortId = _CucsSwAccessEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 12),
    _CucsSwAccessEpPeerPortId_Type()
)
cucsSwAccessEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpPeerPortId.setStatus("current")
_CucsSwAccessEpPeerSlotId_Type = Gauge32
_CucsSwAccessEpPeerSlotId_Object = MibTableColumn
cucsSwAccessEpPeerSlotId = _CucsSwAccessEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 13),
    _CucsSwAccessEpPeerSlotId_Type()
)
cucsSwAccessEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpPeerSlotId.setStatus("current")
_CucsSwAccessEpPortId_Type = Gauge32
_CucsSwAccessEpPortId_Object = MibTableColumn
cucsSwAccessEpPortId = _CucsSwAccessEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 14),
    _CucsSwAccessEpPortId_Type()
)
cucsSwAccessEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpPortId.setStatus("current")
_CucsSwAccessEpSlotId_Type = Gauge32
_CucsSwAccessEpSlotId_Object = MibTableColumn
cucsSwAccessEpSlotId = _CucsSwAccessEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 15),
    _CucsSwAccessEpSlotId_Type()
)
cucsSwAccessEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpSlotId.setStatus("current")
_CucsSwAccessEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwAccessEpSwitchId_Object = MibTableColumn
cucsSwAccessEpSwitchId = _CucsSwAccessEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 16),
    _CucsSwAccessEpSwitchId_Type()
)
cucsSwAccessEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpSwitchId.setStatus("current")
_CucsSwAccessEpTransport_Type = CucsSwAccessEpTransport
_CucsSwAccessEpTransport_Object = MibTableColumn
cucsSwAccessEpTransport = _CucsSwAccessEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 17),
    _CucsSwAccessEpTransport_Type()
)
cucsSwAccessEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpTransport.setStatus("current")
_CucsSwAccessEpType_Type = CucsNetworkConnectionType
_CucsSwAccessEpType_Object = MibTableColumn
cucsSwAccessEpType = _CucsSwAccessEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 18),
    _CucsSwAccessEpType_Type()
)
cucsSwAccessEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpType.setStatus("current")
_CucsSwAccessEpEncap_Type = Gauge32
_CucsSwAccessEpEncap_Object = MibTableColumn
cucsSwAccessEpEncap = _CucsSwAccessEpEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 19),
    _CucsSwAccessEpEncap_Type()
)
cucsSwAccessEpEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpEncap.setStatus("current")
_CucsSwAccessEpNsSize_Type = Gauge32
_CucsSwAccessEpNsSize_Object = MibTableColumn
cucsSwAccessEpNsSize = _CucsSwAccessEpNsSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 20),
    _CucsSwAccessEpNsSize_Type()
)
cucsSwAccessEpNsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpNsSize.setStatus("current")
_CucsSwAccessEpPeerChassisId_Type = Gauge32
_CucsSwAccessEpPeerChassisId_Object = MibTableColumn
cucsSwAccessEpPeerChassisId = _CucsSwAccessEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 21),
    _CucsSwAccessEpPeerChassisId_Type()
)
cucsSwAccessEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpPeerChassisId.setStatus("current")
_CucsSwAccessEpLc_Type = CucsSwPIoEpLc
_CucsSwAccessEpLc_Object = MibTableColumn
cucsSwAccessEpLc = _CucsSwAccessEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 22),
    _CucsSwAccessEpLc_Type()
)
cucsSwAccessEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpLc.setStatus("current")
_CucsSwAccessEpAggrPortId_Type = Gauge32
_CucsSwAccessEpAggrPortId_Object = MibTableColumn
cucsSwAccessEpAggrPortId = _CucsSwAccessEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 23),
    _CucsSwAccessEpAggrPortId_Type()
)
cucsSwAccessEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpAggrPortId.setStatus("current")
_CucsSwAccessEpPeerAggrPortId_Type = Gauge32
_CucsSwAccessEpPeerAggrPortId_Object = MibTableColumn
cucsSwAccessEpPeerAggrPortId = _CucsSwAccessEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 24),
    _CucsSwAccessEpPeerAggrPortId_Type()
)
cucsSwAccessEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpPeerAggrPortId.setStatus("current")
_CucsSwAccessEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwAccessEpAutoNegotiate_Object = MibTableColumn
cucsSwAccessEpAutoNegotiate = _CucsSwAccessEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 3, 1, 25),
    _CucsSwAccessEpAutoNegotiate_Type()
)
cucsSwAccessEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessEpAutoNegotiate.setStatus("current")
_CucsSwEnvStatsTable_Object = MibTable
cucsSwEnvStatsTable = _CucsSwEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4)
)
if mibBuilder.loadTexts:
    cucsSwEnvStatsTable.setStatus("current")
_CucsSwEnvStatsEntry_Object = MibTableRow
cucsSwEnvStatsEntry = _CucsSwEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1)
)
cucsSwEnvStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEnvStatsEntry.setStatus("current")
_CucsSwEnvStatsInstanceId_Type = CucsManagedObjectId
_CucsSwEnvStatsInstanceId_Object = MibTableColumn
cucsSwEnvStatsInstanceId = _CucsSwEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 1),
    _CucsSwEnvStatsInstanceId_Type()
)
cucsSwEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEnvStatsInstanceId.setStatus("current")
_CucsSwEnvStatsDn_Type = CucsManagedObjectDn
_CucsSwEnvStatsDn_Object = MibTableColumn
cucsSwEnvStatsDn = _CucsSwEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 2),
    _CucsSwEnvStatsDn_Type()
)
cucsSwEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsDn.setStatus("current")
_CucsSwEnvStatsRn_Type = SnmpAdminString
_CucsSwEnvStatsRn_Object = MibTableColumn
cucsSwEnvStatsRn = _CucsSwEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 3),
    _CucsSwEnvStatsRn_Type()
)
cucsSwEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsRn.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet1_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet1_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet1 = _CucsSwEnvStatsFanCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 4),
    _CucsSwEnvStatsFanCtrlrInlet1_Type()
)
cucsSwEnvStatsFanCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet1.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet1Avg_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet1Avg_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet1Avg = _CucsSwEnvStatsFanCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 5),
    _CucsSwEnvStatsFanCtrlrInlet1Avg_Type()
)
cucsSwEnvStatsFanCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet1Avg.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet1Max_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet1Max_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet1Max = _CucsSwEnvStatsFanCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 6),
    _CucsSwEnvStatsFanCtrlrInlet1Max_Type()
)
cucsSwEnvStatsFanCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet1Max.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet1Min_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet1Min_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet1Min = _CucsSwEnvStatsFanCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 7),
    _CucsSwEnvStatsFanCtrlrInlet1Min_Type()
)
cucsSwEnvStatsFanCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet1Min.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet2_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet2_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet2 = _CucsSwEnvStatsFanCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 8),
    _CucsSwEnvStatsFanCtrlrInlet2_Type()
)
cucsSwEnvStatsFanCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet2.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet2Avg_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet2Avg_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet2Avg = _CucsSwEnvStatsFanCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 9),
    _CucsSwEnvStatsFanCtrlrInlet2Avg_Type()
)
cucsSwEnvStatsFanCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet2Avg.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet2Max_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet2Max_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet2Max = _CucsSwEnvStatsFanCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 10),
    _CucsSwEnvStatsFanCtrlrInlet2Max_Type()
)
cucsSwEnvStatsFanCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet2Max.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet2Min_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet2Min_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet2Min = _CucsSwEnvStatsFanCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 11),
    _CucsSwEnvStatsFanCtrlrInlet2Min_Type()
)
cucsSwEnvStatsFanCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet2Min.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet3_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet3_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet3 = _CucsSwEnvStatsFanCtrlrInlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 12),
    _CucsSwEnvStatsFanCtrlrInlet3_Type()
)
cucsSwEnvStatsFanCtrlrInlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet3.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet3Avg_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet3Avg_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet3Avg = _CucsSwEnvStatsFanCtrlrInlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 13),
    _CucsSwEnvStatsFanCtrlrInlet3Avg_Type()
)
cucsSwEnvStatsFanCtrlrInlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet3Avg.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet3Max_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet3Max_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet3Max = _CucsSwEnvStatsFanCtrlrInlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 14),
    _CucsSwEnvStatsFanCtrlrInlet3Max_Type()
)
cucsSwEnvStatsFanCtrlrInlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet3Max.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet3Min_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet3Min_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet3Min = _CucsSwEnvStatsFanCtrlrInlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 15),
    _CucsSwEnvStatsFanCtrlrInlet3Min_Type()
)
cucsSwEnvStatsFanCtrlrInlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet3Min.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet4_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet4_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet4 = _CucsSwEnvStatsFanCtrlrInlet4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 16),
    _CucsSwEnvStatsFanCtrlrInlet4_Type()
)
cucsSwEnvStatsFanCtrlrInlet4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet4.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet4Avg_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet4Avg_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet4Avg = _CucsSwEnvStatsFanCtrlrInlet4Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 17),
    _CucsSwEnvStatsFanCtrlrInlet4Avg_Type()
)
cucsSwEnvStatsFanCtrlrInlet4Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet4Avg.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet4Max_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet4Max_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet4Max = _CucsSwEnvStatsFanCtrlrInlet4Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 18),
    _CucsSwEnvStatsFanCtrlrInlet4Max_Type()
)
cucsSwEnvStatsFanCtrlrInlet4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet4Max.setStatus("current")
_CucsSwEnvStatsFanCtrlrInlet4Min_Type = Integer32
_CucsSwEnvStatsFanCtrlrInlet4Min_Object = MibTableColumn
cucsSwEnvStatsFanCtrlrInlet4Min = _CucsSwEnvStatsFanCtrlrInlet4Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 19),
    _CucsSwEnvStatsFanCtrlrInlet4Min_Type()
)
cucsSwEnvStatsFanCtrlrInlet4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsFanCtrlrInlet4Min.setStatus("current")
_CucsSwEnvStatsIntervals_Type = Gauge32
_CucsSwEnvStatsIntervals_Object = MibTableColumn
cucsSwEnvStatsIntervals = _CucsSwEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 20),
    _CucsSwEnvStatsIntervals_Type()
)
cucsSwEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsIntervals.setStatus("current")
_CucsSwEnvStatsMainBoardOutlet1_Type = Integer32
_CucsSwEnvStatsMainBoardOutlet1_Object = MibTableColumn
cucsSwEnvStatsMainBoardOutlet1 = _CucsSwEnvStatsMainBoardOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 21),
    _CucsSwEnvStatsMainBoardOutlet1_Type()
)
cucsSwEnvStatsMainBoardOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsMainBoardOutlet1.setStatus("current")
_CucsSwEnvStatsMainBoardOutlet1Avg_Type = Integer32
_CucsSwEnvStatsMainBoardOutlet1Avg_Object = MibTableColumn
cucsSwEnvStatsMainBoardOutlet1Avg = _CucsSwEnvStatsMainBoardOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 22),
    _CucsSwEnvStatsMainBoardOutlet1Avg_Type()
)
cucsSwEnvStatsMainBoardOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsMainBoardOutlet1Avg.setStatus("current")
_CucsSwEnvStatsMainBoardOutlet1Max_Type = Integer32
_CucsSwEnvStatsMainBoardOutlet1Max_Object = MibTableColumn
cucsSwEnvStatsMainBoardOutlet1Max = _CucsSwEnvStatsMainBoardOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 23),
    _CucsSwEnvStatsMainBoardOutlet1Max_Type()
)
cucsSwEnvStatsMainBoardOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsMainBoardOutlet1Max.setStatus("current")
_CucsSwEnvStatsMainBoardOutlet1Min_Type = Integer32
_CucsSwEnvStatsMainBoardOutlet1Min_Object = MibTableColumn
cucsSwEnvStatsMainBoardOutlet1Min = _CucsSwEnvStatsMainBoardOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 24),
    _CucsSwEnvStatsMainBoardOutlet1Min_Type()
)
cucsSwEnvStatsMainBoardOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsMainBoardOutlet1Min.setStatus("current")
_CucsSwEnvStatsMainBoardOutlet2_Type = Integer32
_CucsSwEnvStatsMainBoardOutlet2_Object = MibTableColumn
cucsSwEnvStatsMainBoardOutlet2 = _CucsSwEnvStatsMainBoardOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 25),
    _CucsSwEnvStatsMainBoardOutlet2_Type()
)
cucsSwEnvStatsMainBoardOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsMainBoardOutlet2.setStatus("current")
_CucsSwEnvStatsMainBoardOutlet2Avg_Type = Integer32
_CucsSwEnvStatsMainBoardOutlet2Avg_Object = MibTableColumn
cucsSwEnvStatsMainBoardOutlet2Avg = _CucsSwEnvStatsMainBoardOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 26),
    _CucsSwEnvStatsMainBoardOutlet2Avg_Type()
)
cucsSwEnvStatsMainBoardOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsMainBoardOutlet2Avg.setStatus("current")
_CucsSwEnvStatsMainBoardOutlet2Max_Type = Integer32
_CucsSwEnvStatsMainBoardOutlet2Max_Object = MibTableColumn
cucsSwEnvStatsMainBoardOutlet2Max = _CucsSwEnvStatsMainBoardOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 27),
    _CucsSwEnvStatsMainBoardOutlet2Max_Type()
)
cucsSwEnvStatsMainBoardOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsMainBoardOutlet2Max.setStatus("current")
_CucsSwEnvStatsMainBoardOutlet2Min_Type = Integer32
_CucsSwEnvStatsMainBoardOutlet2Min_Object = MibTableColumn
cucsSwEnvStatsMainBoardOutlet2Min = _CucsSwEnvStatsMainBoardOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 28),
    _CucsSwEnvStatsMainBoardOutlet2Min_Type()
)
cucsSwEnvStatsMainBoardOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsMainBoardOutlet2Min.setStatus("current")
_CucsSwEnvStatsPsuCtrlrInlet1_Type = Integer32
_CucsSwEnvStatsPsuCtrlrInlet1_Object = MibTableColumn
cucsSwEnvStatsPsuCtrlrInlet1 = _CucsSwEnvStatsPsuCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 29),
    _CucsSwEnvStatsPsuCtrlrInlet1_Type()
)
cucsSwEnvStatsPsuCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsPsuCtrlrInlet1.setStatus("current")
_CucsSwEnvStatsPsuCtrlrInlet1Avg_Type = Integer32
_CucsSwEnvStatsPsuCtrlrInlet1Avg_Object = MibTableColumn
cucsSwEnvStatsPsuCtrlrInlet1Avg = _CucsSwEnvStatsPsuCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 30),
    _CucsSwEnvStatsPsuCtrlrInlet1Avg_Type()
)
cucsSwEnvStatsPsuCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsPsuCtrlrInlet1Avg.setStatus("current")
_CucsSwEnvStatsPsuCtrlrInlet1Max_Type = Integer32
_CucsSwEnvStatsPsuCtrlrInlet1Max_Object = MibTableColumn
cucsSwEnvStatsPsuCtrlrInlet1Max = _CucsSwEnvStatsPsuCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 31),
    _CucsSwEnvStatsPsuCtrlrInlet1Max_Type()
)
cucsSwEnvStatsPsuCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsPsuCtrlrInlet1Max.setStatus("current")
_CucsSwEnvStatsPsuCtrlrInlet1Min_Type = Integer32
_CucsSwEnvStatsPsuCtrlrInlet1Min_Object = MibTableColumn
cucsSwEnvStatsPsuCtrlrInlet1Min = _CucsSwEnvStatsPsuCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 32),
    _CucsSwEnvStatsPsuCtrlrInlet1Min_Type()
)
cucsSwEnvStatsPsuCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsPsuCtrlrInlet1Min.setStatus("current")
_CucsSwEnvStatsPsuCtrlrInlet2_Type = Integer32
_CucsSwEnvStatsPsuCtrlrInlet2_Object = MibTableColumn
cucsSwEnvStatsPsuCtrlrInlet2 = _CucsSwEnvStatsPsuCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 33),
    _CucsSwEnvStatsPsuCtrlrInlet2_Type()
)
cucsSwEnvStatsPsuCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsPsuCtrlrInlet2.setStatus("current")
_CucsSwEnvStatsPsuCtrlrInlet2Avg_Type = Integer32
_CucsSwEnvStatsPsuCtrlrInlet2Avg_Object = MibTableColumn
cucsSwEnvStatsPsuCtrlrInlet2Avg = _CucsSwEnvStatsPsuCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 34),
    _CucsSwEnvStatsPsuCtrlrInlet2Avg_Type()
)
cucsSwEnvStatsPsuCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsPsuCtrlrInlet2Avg.setStatus("current")
_CucsSwEnvStatsPsuCtrlrInlet2Max_Type = Integer32
_CucsSwEnvStatsPsuCtrlrInlet2Max_Object = MibTableColumn
cucsSwEnvStatsPsuCtrlrInlet2Max = _CucsSwEnvStatsPsuCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 35),
    _CucsSwEnvStatsPsuCtrlrInlet2Max_Type()
)
cucsSwEnvStatsPsuCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsPsuCtrlrInlet2Max.setStatus("current")
_CucsSwEnvStatsPsuCtrlrInlet2Min_Type = Integer32
_CucsSwEnvStatsPsuCtrlrInlet2Min_Object = MibTableColumn
cucsSwEnvStatsPsuCtrlrInlet2Min = _CucsSwEnvStatsPsuCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 36),
    _CucsSwEnvStatsPsuCtrlrInlet2Min_Type()
)
cucsSwEnvStatsPsuCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsPsuCtrlrInlet2Min.setStatus("current")
_CucsSwEnvStatsSuspect_Type = TruthValue
_CucsSwEnvStatsSuspect_Object = MibTableColumn
cucsSwEnvStatsSuspect = _CucsSwEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 37),
    _CucsSwEnvStatsSuspect_Type()
)
cucsSwEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsSuspect.setStatus("current")
_CucsSwEnvStatsThresholded_Type = CucsSwEnvStatsThresholded
_CucsSwEnvStatsThresholded_Object = MibTableColumn
cucsSwEnvStatsThresholded = _CucsSwEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 38),
    _CucsSwEnvStatsThresholded_Type()
)
cucsSwEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsThresholded.setStatus("current")
_CucsSwEnvStatsTimeCollected_Type = DateAndTime
_CucsSwEnvStatsTimeCollected_Object = MibTableColumn
cucsSwEnvStatsTimeCollected = _CucsSwEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 39),
    _CucsSwEnvStatsTimeCollected_Type()
)
cucsSwEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTimeCollected.setStatus("current")
_CucsSwEnvStatsUpdate_Type = Gauge32
_CucsSwEnvStatsUpdate_Object = MibTableColumn
cucsSwEnvStatsUpdate = _CucsSwEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 40),
    _CucsSwEnvStatsUpdate_Type()
)
cucsSwEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsUpdate.setStatus("current")
_CucsSwEnvStatsDonner_Type = Integer32
_CucsSwEnvStatsDonner_Object = MibTableColumn
cucsSwEnvStatsDonner = _CucsSwEnvStatsDonner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 43),
    _CucsSwEnvStatsDonner_Type()
)
cucsSwEnvStatsDonner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsDonner.setStatus("current")
_CucsSwEnvStatsDonnerAvg_Type = Integer32
_CucsSwEnvStatsDonnerAvg_Object = MibTableColumn
cucsSwEnvStatsDonnerAvg = _CucsSwEnvStatsDonnerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 44),
    _CucsSwEnvStatsDonnerAvg_Type()
)
cucsSwEnvStatsDonnerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsDonnerAvg.setStatus("current")
_CucsSwEnvStatsDonnerMax_Type = Integer32
_CucsSwEnvStatsDonnerMax_Object = MibTableColumn
cucsSwEnvStatsDonnerMax = _CucsSwEnvStatsDonnerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 45),
    _CucsSwEnvStatsDonnerMax_Type()
)
cucsSwEnvStatsDonnerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsDonnerMax.setStatus("current")
_CucsSwEnvStatsDonnerMin_Type = Integer32
_CucsSwEnvStatsDonnerMin_Object = MibTableColumn
cucsSwEnvStatsDonnerMin = _CucsSwEnvStatsDonnerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 46),
    _CucsSwEnvStatsDonnerMin_Type()
)
cucsSwEnvStatsDonnerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsDonnerMin.setStatus("current")
_CucsSwEnvStatsTd2_Type = Integer32
_CucsSwEnvStatsTd2_Object = MibTableColumn
cucsSwEnvStatsTd2 = _CucsSwEnvStatsTd2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 47),
    _CucsSwEnvStatsTd2_Type()
)
cucsSwEnvStatsTd2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTd2.setStatus("current")
_CucsSwEnvStatsTd2Avg_Type = Integer32
_CucsSwEnvStatsTd2Avg_Object = MibTableColumn
cucsSwEnvStatsTd2Avg = _CucsSwEnvStatsTd2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 48),
    _CucsSwEnvStatsTd2Avg_Type()
)
cucsSwEnvStatsTd2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTd2Avg.setStatus("current")
_CucsSwEnvStatsTd2Max_Type = Integer32
_CucsSwEnvStatsTd2Max_Object = MibTableColumn
cucsSwEnvStatsTd2Max = _CucsSwEnvStatsTd2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 49),
    _CucsSwEnvStatsTd2Max_Type()
)
cucsSwEnvStatsTd2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTd2Max.setStatus("current")
_CucsSwEnvStatsTd2Min_Type = Integer32
_CucsSwEnvStatsTd2Min_Object = MibTableColumn
cucsSwEnvStatsTd2Min = _CucsSwEnvStatsTd2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 50),
    _CucsSwEnvStatsTd2Min_Type()
)
cucsSwEnvStatsTd2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTd2Min.setStatus("current")
_CucsSwEnvStatsTiburon_Type = Integer32
_CucsSwEnvStatsTiburon_Object = MibTableColumn
cucsSwEnvStatsTiburon = _CucsSwEnvStatsTiburon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 51),
    _CucsSwEnvStatsTiburon_Type()
)
cucsSwEnvStatsTiburon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTiburon.setStatus("current")
_CucsSwEnvStatsTiburonAvg_Type = Integer32
_CucsSwEnvStatsTiburonAvg_Object = MibTableColumn
cucsSwEnvStatsTiburonAvg = _CucsSwEnvStatsTiburonAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 52),
    _CucsSwEnvStatsTiburonAvg_Type()
)
cucsSwEnvStatsTiburonAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTiburonAvg.setStatus("current")
_CucsSwEnvStatsTiburonMax_Type = Integer32
_CucsSwEnvStatsTiburonMax_Object = MibTableColumn
cucsSwEnvStatsTiburonMax = _CucsSwEnvStatsTiburonMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 53),
    _CucsSwEnvStatsTiburonMax_Type()
)
cucsSwEnvStatsTiburonMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTiburonMax.setStatus("current")
_CucsSwEnvStatsTiburonMin_Type = Integer32
_CucsSwEnvStatsTiburonMin_Object = MibTableColumn
cucsSwEnvStatsTiburonMin = _CucsSwEnvStatsTiburonMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 4, 1, 54),
    _CucsSwEnvStatsTiburonMin_Type()
)
cucsSwEnvStatsTiburonMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsTiburonMin.setStatus("current")
_CucsSwEnvStatsHistTable_Object = MibTable
cucsSwEnvStatsHistTable = _CucsSwEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5)
)
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTable.setStatus("current")
_CucsSwEnvStatsHistEntry_Object = MibTableRow
cucsSwEnvStatsHistEntry = _CucsSwEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1)
)
cucsSwEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistEntry.setStatus("current")
_CucsSwEnvStatsHistInstanceId_Type = CucsManagedObjectId
_CucsSwEnvStatsHistInstanceId_Object = MibTableColumn
cucsSwEnvStatsHistInstanceId = _CucsSwEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 1),
    _CucsSwEnvStatsHistInstanceId_Type()
)
cucsSwEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistInstanceId.setStatus("current")
_CucsSwEnvStatsHistDn_Type = CucsManagedObjectDn
_CucsSwEnvStatsHistDn_Object = MibTableColumn
cucsSwEnvStatsHistDn = _CucsSwEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 2),
    _CucsSwEnvStatsHistDn_Type()
)
cucsSwEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistDn.setStatus("current")
_CucsSwEnvStatsHistRn_Type = SnmpAdminString
_CucsSwEnvStatsHistRn_Object = MibTableColumn
cucsSwEnvStatsHistRn = _CucsSwEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 3),
    _CucsSwEnvStatsHistRn_Type()
)
cucsSwEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistRn.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet1_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet1_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet1 = _CucsSwEnvStatsHistFanCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 4),
    _CucsSwEnvStatsHistFanCtrlrInlet1_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet1.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet1Avg_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet1Avg_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet1Avg = _CucsSwEnvStatsHistFanCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 5),
    _CucsSwEnvStatsHistFanCtrlrInlet1Avg_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet1Avg.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet1Max_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet1Max_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet1Max = _CucsSwEnvStatsHistFanCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 6),
    _CucsSwEnvStatsHistFanCtrlrInlet1Max_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet1Max.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet1Min_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet1Min_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet1Min = _CucsSwEnvStatsHistFanCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 7),
    _CucsSwEnvStatsHistFanCtrlrInlet1Min_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet1Min.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet2_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet2_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet2 = _CucsSwEnvStatsHistFanCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 8),
    _CucsSwEnvStatsHistFanCtrlrInlet2_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet2.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet2Avg_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet2Avg_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet2Avg = _CucsSwEnvStatsHistFanCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 9),
    _CucsSwEnvStatsHistFanCtrlrInlet2Avg_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet2Avg.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet2Max_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet2Max_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet2Max = _CucsSwEnvStatsHistFanCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 10),
    _CucsSwEnvStatsHistFanCtrlrInlet2Max_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet2Max.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet2Min_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet2Min_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet2Min = _CucsSwEnvStatsHistFanCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 11),
    _CucsSwEnvStatsHistFanCtrlrInlet2Min_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet2Min.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet3_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet3_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet3 = _CucsSwEnvStatsHistFanCtrlrInlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 12),
    _CucsSwEnvStatsHistFanCtrlrInlet3_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet3.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet3Avg_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet3Avg_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet3Avg = _CucsSwEnvStatsHistFanCtrlrInlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 13),
    _CucsSwEnvStatsHistFanCtrlrInlet3Avg_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet3Avg.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet3Max_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet3Max_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet3Max = _CucsSwEnvStatsHistFanCtrlrInlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 14),
    _CucsSwEnvStatsHistFanCtrlrInlet3Max_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet3Max.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet3Min_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet3Min_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet3Min = _CucsSwEnvStatsHistFanCtrlrInlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 15),
    _CucsSwEnvStatsHistFanCtrlrInlet3Min_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet3Min.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet4_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet4_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet4 = _CucsSwEnvStatsHistFanCtrlrInlet4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 16),
    _CucsSwEnvStatsHistFanCtrlrInlet4_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet4.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet4Avg_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet4Avg_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet4Avg = _CucsSwEnvStatsHistFanCtrlrInlet4Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 17),
    _CucsSwEnvStatsHistFanCtrlrInlet4Avg_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet4Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet4Avg.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet4Max_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet4Max_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet4Max = _CucsSwEnvStatsHistFanCtrlrInlet4Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 18),
    _CucsSwEnvStatsHistFanCtrlrInlet4Max_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet4Max.setStatus("current")
_CucsSwEnvStatsHistFanCtrlrInlet4Min_Type = Integer32
_CucsSwEnvStatsHistFanCtrlrInlet4Min_Object = MibTableColumn
cucsSwEnvStatsHistFanCtrlrInlet4Min = _CucsSwEnvStatsHistFanCtrlrInlet4Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 19),
    _CucsSwEnvStatsHistFanCtrlrInlet4Min_Type()
)
cucsSwEnvStatsHistFanCtrlrInlet4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistFanCtrlrInlet4Min.setStatus("current")
_CucsSwEnvStatsHistId_Type = Unsigned64
_CucsSwEnvStatsHistId_Object = MibTableColumn
cucsSwEnvStatsHistId = _CucsSwEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 20),
    _CucsSwEnvStatsHistId_Type()
)
cucsSwEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistId.setStatus("current")
_CucsSwEnvStatsHistMainBoardOutlet1_Type = Integer32
_CucsSwEnvStatsHistMainBoardOutlet1_Object = MibTableColumn
cucsSwEnvStatsHistMainBoardOutlet1 = _CucsSwEnvStatsHistMainBoardOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 21),
    _CucsSwEnvStatsHistMainBoardOutlet1_Type()
)
cucsSwEnvStatsHistMainBoardOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMainBoardOutlet1.setStatus("current")
_CucsSwEnvStatsHistMainBoardOutlet1Avg_Type = Integer32
_CucsSwEnvStatsHistMainBoardOutlet1Avg_Object = MibTableColumn
cucsSwEnvStatsHistMainBoardOutlet1Avg = _CucsSwEnvStatsHistMainBoardOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 22),
    _CucsSwEnvStatsHistMainBoardOutlet1Avg_Type()
)
cucsSwEnvStatsHistMainBoardOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMainBoardOutlet1Avg.setStatus("current")
_CucsSwEnvStatsHistMainBoardOutlet1Max_Type = Integer32
_CucsSwEnvStatsHistMainBoardOutlet1Max_Object = MibTableColumn
cucsSwEnvStatsHistMainBoardOutlet1Max = _CucsSwEnvStatsHistMainBoardOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 23),
    _CucsSwEnvStatsHistMainBoardOutlet1Max_Type()
)
cucsSwEnvStatsHistMainBoardOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMainBoardOutlet1Max.setStatus("current")
_CucsSwEnvStatsHistMainBoardOutlet1Min_Type = Integer32
_CucsSwEnvStatsHistMainBoardOutlet1Min_Object = MibTableColumn
cucsSwEnvStatsHistMainBoardOutlet1Min = _CucsSwEnvStatsHistMainBoardOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 24),
    _CucsSwEnvStatsHistMainBoardOutlet1Min_Type()
)
cucsSwEnvStatsHistMainBoardOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMainBoardOutlet1Min.setStatus("current")
_CucsSwEnvStatsHistMainBoardOutlet2_Type = Integer32
_CucsSwEnvStatsHistMainBoardOutlet2_Object = MibTableColumn
cucsSwEnvStatsHistMainBoardOutlet2 = _CucsSwEnvStatsHistMainBoardOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 25),
    _CucsSwEnvStatsHistMainBoardOutlet2_Type()
)
cucsSwEnvStatsHistMainBoardOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMainBoardOutlet2.setStatus("current")
_CucsSwEnvStatsHistMainBoardOutlet2Avg_Type = Integer32
_CucsSwEnvStatsHistMainBoardOutlet2Avg_Object = MibTableColumn
cucsSwEnvStatsHistMainBoardOutlet2Avg = _CucsSwEnvStatsHistMainBoardOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 26),
    _CucsSwEnvStatsHistMainBoardOutlet2Avg_Type()
)
cucsSwEnvStatsHistMainBoardOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMainBoardOutlet2Avg.setStatus("current")
_CucsSwEnvStatsHistMainBoardOutlet2Max_Type = Integer32
_CucsSwEnvStatsHistMainBoardOutlet2Max_Object = MibTableColumn
cucsSwEnvStatsHistMainBoardOutlet2Max = _CucsSwEnvStatsHistMainBoardOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 27),
    _CucsSwEnvStatsHistMainBoardOutlet2Max_Type()
)
cucsSwEnvStatsHistMainBoardOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMainBoardOutlet2Max.setStatus("current")
_CucsSwEnvStatsHistMainBoardOutlet2Min_Type = Integer32
_CucsSwEnvStatsHistMainBoardOutlet2Min_Object = MibTableColumn
cucsSwEnvStatsHistMainBoardOutlet2Min = _CucsSwEnvStatsHistMainBoardOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 28),
    _CucsSwEnvStatsHistMainBoardOutlet2Min_Type()
)
cucsSwEnvStatsHistMainBoardOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMainBoardOutlet2Min.setStatus("current")
_CucsSwEnvStatsHistMostRecent_Type = TruthValue
_CucsSwEnvStatsHistMostRecent_Object = MibTableColumn
cucsSwEnvStatsHistMostRecent = _CucsSwEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 29),
    _CucsSwEnvStatsHistMostRecent_Type()
)
cucsSwEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistMostRecent.setStatus("current")
_CucsSwEnvStatsHistPsuCtrlrInlet1_Type = Integer32
_CucsSwEnvStatsHistPsuCtrlrInlet1_Object = MibTableColumn
cucsSwEnvStatsHistPsuCtrlrInlet1 = _CucsSwEnvStatsHistPsuCtrlrInlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 30),
    _CucsSwEnvStatsHistPsuCtrlrInlet1_Type()
)
cucsSwEnvStatsHistPsuCtrlrInlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistPsuCtrlrInlet1.setStatus("current")
_CucsSwEnvStatsHistPsuCtrlrInlet1Avg_Type = Integer32
_CucsSwEnvStatsHistPsuCtrlrInlet1Avg_Object = MibTableColumn
cucsSwEnvStatsHistPsuCtrlrInlet1Avg = _CucsSwEnvStatsHistPsuCtrlrInlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 31),
    _CucsSwEnvStatsHistPsuCtrlrInlet1Avg_Type()
)
cucsSwEnvStatsHistPsuCtrlrInlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistPsuCtrlrInlet1Avg.setStatus("current")
_CucsSwEnvStatsHistPsuCtrlrInlet1Max_Type = Integer32
_CucsSwEnvStatsHistPsuCtrlrInlet1Max_Object = MibTableColumn
cucsSwEnvStatsHistPsuCtrlrInlet1Max = _CucsSwEnvStatsHistPsuCtrlrInlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 32),
    _CucsSwEnvStatsHistPsuCtrlrInlet1Max_Type()
)
cucsSwEnvStatsHistPsuCtrlrInlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistPsuCtrlrInlet1Max.setStatus("current")
_CucsSwEnvStatsHistPsuCtrlrInlet1Min_Type = Integer32
_CucsSwEnvStatsHistPsuCtrlrInlet1Min_Object = MibTableColumn
cucsSwEnvStatsHistPsuCtrlrInlet1Min = _CucsSwEnvStatsHistPsuCtrlrInlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 33),
    _CucsSwEnvStatsHistPsuCtrlrInlet1Min_Type()
)
cucsSwEnvStatsHistPsuCtrlrInlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistPsuCtrlrInlet1Min.setStatus("current")
_CucsSwEnvStatsHistPsuCtrlrInlet2_Type = Integer32
_CucsSwEnvStatsHistPsuCtrlrInlet2_Object = MibTableColumn
cucsSwEnvStatsHistPsuCtrlrInlet2 = _CucsSwEnvStatsHistPsuCtrlrInlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 34),
    _CucsSwEnvStatsHistPsuCtrlrInlet2_Type()
)
cucsSwEnvStatsHistPsuCtrlrInlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistPsuCtrlrInlet2.setStatus("current")
_CucsSwEnvStatsHistPsuCtrlrInlet2Avg_Type = Integer32
_CucsSwEnvStatsHistPsuCtrlrInlet2Avg_Object = MibTableColumn
cucsSwEnvStatsHistPsuCtrlrInlet2Avg = _CucsSwEnvStatsHistPsuCtrlrInlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 35),
    _CucsSwEnvStatsHistPsuCtrlrInlet2Avg_Type()
)
cucsSwEnvStatsHistPsuCtrlrInlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistPsuCtrlrInlet2Avg.setStatus("current")
_CucsSwEnvStatsHistPsuCtrlrInlet2Max_Type = Integer32
_CucsSwEnvStatsHistPsuCtrlrInlet2Max_Object = MibTableColumn
cucsSwEnvStatsHistPsuCtrlrInlet2Max = _CucsSwEnvStatsHistPsuCtrlrInlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 36),
    _CucsSwEnvStatsHistPsuCtrlrInlet2Max_Type()
)
cucsSwEnvStatsHistPsuCtrlrInlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistPsuCtrlrInlet2Max.setStatus("current")
_CucsSwEnvStatsHistPsuCtrlrInlet2Min_Type = Integer32
_CucsSwEnvStatsHistPsuCtrlrInlet2Min_Object = MibTableColumn
cucsSwEnvStatsHistPsuCtrlrInlet2Min = _CucsSwEnvStatsHistPsuCtrlrInlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 37),
    _CucsSwEnvStatsHistPsuCtrlrInlet2Min_Type()
)
cucsSwEnvStatsHistPsuCtrlrInlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistPsuCtrlrInlet2Min.setStatus("current")
_CucsSwEnvStatsHistSuspect_Type = TruthValue
_CucsSwEnvStatsHistSuspect_Object = MibTableColumn
cucsSwEnvStatsHistSuspect = _CucsSwEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 38),
    _CucsSwEnvStatsHistSuspect_Type()
)
cucsSwEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistSuspect.setStatus("current")
_CucsSwEnvStatsHistThresholded_Type = CucsSwEnvStatsHistThresholded
_CucsSwEnvStatsHistThresholded_Object = MibTableColumn
cucsSwEnvStatsHistThresholded = _CucsSwEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 39),
    _CucsSwEnvStatsHistThresholded_Type()
)
cucsSwEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistThresholded.setStatus("current")
_CucsSwEnvStatsHistTimeCollected_Type = DateAndTime
_CucsSwEnvStatsHistTimeCollected_Object = MibTableColumn
cucsSwEnvStatsHistTimeCollected = _CucsSwEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 40),
    _CucsSwEnvStatsHistTimeCollected_Type()
)
cucsSwEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTimeCollected.setStatus("current")
_CucsSwEnvStatsHistDonner_Type = Integer32
_CucsSwEnvStatsHistDonner_Object = MibTableColumn
cucsSwEnvStatsHistDonner = _CucsSwEnvStatsHistDonner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 41),
    _CucsSwEnvStatsHistDonner_Type()
)
cucsSwEnvStatsHistDonner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistDonner.setStatus("current")
_CucsSwEnvStatsHistDonnerAvg_Type = Integer32
_CucsSwEnvStatsHistDonnerAvg_Object = MibTableColumn
cucsSwEnvStatsHistDonnerAvg = _CucsSwEnvStatsHistDonnerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 42),
    _CucsSwEnvStatsHistDonnerAvg_Type()
)
cucsSwEnvStatsHistDonnerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistDonnerAvg.setStatus("current")
_CucsSwEnvStatsHistDonnerMax_Type = Integer32
_CucsSwEnvStatsHistDonnerMax_Object = MibTableColumn
cucsSwEnvStatsHistDonnerMax = _CucsSwEnvStatsHistDonnerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 43),
    _CucsSwEnvStatsHistDonnerMax_Type()
)
cucsSwEnvStatsHistDonnerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistDonnerMax.setStatus("current")
_CucsSwEnvStatsHistDonnerMin_Type = Integer32
_CucsSwEnvStatsHistDonnerMin_Object = MibTableColumn
cucsSwEnvStatsHistDonnerMin = _CucsSwEnvStatsHistDonnerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 44),
    _CucsSwEnvStatsHistDonnerMin_Type()
)
cucsSwEnvStatsHistDonnerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistDonnerMin.setStatus("current")
_CucsSwEnvStatsHistTd2_Type = Integer32
_CucsSwEnvStatsHistTd2_Object = MibTableColumn
cucsSwEnvStatsHistTd2 = _CucsSwEnvStatsHistTd2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 45),
    _CucsSwEnvStatsHistTd2_Type()
)
cucsSwEnvStatsHistTd2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTd2.setStatus("current")
_CucsSwEnvStatsHistTd2Avg_Type = Integer32
_CucsSwEnvStatsHistTd2Avg_Object = MibTableColumn
cucsSwEnvStatsHistTd2Avg = _CucsSwEnvStatsHistTd2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 46),
    _CucsSwEnvStatsHistTd2Avg_Type()
)
cucsSwEnvStatsHistTd2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTd2Avg.setStatus("current")
_CucsSwEnvStatsHistTd2Max_Type = Integer32
_CucsSwEnvStatsHistTd2Max_Object = MibTableColumn
cucsSwEnvStatsHistTd2Max = _CucsSwEnvStatsHistTd2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 47),
    _CucsSwEnvStatsHistTd2Max_Type()
)
cucsSwEnvStatsHistTd2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTd2Max.setStatus("current")
_CucsSwEnvStatsHistTd2Min_Type = Integer32
_CucsSwEnvStatsHistTd2Min_Object = MibTableColumn
cucsSwEnvStatsHistTd2Min = _CucsSwEnvStatsHistTd2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 48),
    _CucsSwEnvStatsHistTd2Min_Type()
)
cucsSwEnvStatsHistTd2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTd2Min.setStatus("current")
_CucsSwEnvStatsHistTiburon_Type = Integer32
_CucsSwEnvStatsHistTiburon_Object = MibTableColumn
cucsSwEnvStatsHistTiburon = _CucsSwEnvStatsHistTiburon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 49),
    _CucsSwEnvStatsHistTiburon_Type()
)
cucsSwEnvStatsHistTiburon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTiburon.setStatus("current")
_CucsSwEnvStatsHistTiburonAvg_Type = Integer32
_CucsSwEnvStatsHistTiburonAvg_Object = MibTableColumn
cucsSwEnvStatsHistTiburonAvg = _CucsSwEnvStatsHistTiburonAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 50),
    _CucsSwEnvStatsHistTiburonAvg_Type()
)
cucsSwEnvStatsHistTiburonAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTiburonAvg.setStatus("current")
_CucsSwEnvStatsHistTiburonMax_Type = Integer32
_CucsSwEnvStatsHistTiburonMax_Object = MibTableColumn
cucsSwEnvStatsHistTiburonMax = _CucsSwEnvStatsHistTiburonMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 51),
    _CucsSwEnvStatsHistTiburonMax_Type()
)
cucsSwEnvStatsHistTiburonMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTiburonMax.setStatus("current")
_CucsSwEnvStatsHistTiburonMin_Type = Integer32
_CucsSwEnvStatsHistTiburonMin_Object = MibTableColumn
cucsSwEnvStatsHistTiburonMin = _CucsSwEnvStatsHistTiburonMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 5, 1, 52),
    _CucsSwEnvStatsHistTiburonMin_Type()
)
cucsSwEnvStatsHistTiburonMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEnvStatsHistTiburonMin.setStatus("current")
_CucsSwEthEstcEpTable_Object = MibTable
cucsSwEthEstcEpTable = _CucsSwEthEstcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6)
)
if mibBuilder.loadTexts:
    cucsSwEthEstcEpTable.setStatus("current")
_CucsSwEthEstcEpEntry_Object = MibTableRow
cucsSwEthEstcEpEntry = _CucsSwEthEstcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1)
)
cucsSwEthEstcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthEstcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthEstcEpEntry.setStatus("current")
_CucsSwEthEstcEpInstanceId_Type = CucsManagedObjectId
_CucsSwEthEstcEpInstanceId_Object = MibTableColumn
cucsSwEthEstcEpInstanceId = _CucsSwEthEstcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 1),
    _CucsSwEthEstcEpInstanceId_Type()
)
cucsSwEthEstcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpInstanceId.setStatus("current")
_CucsSwEthEstcEpDn_Type = CucsManagedObjectDn
_CucsSwEthEstcEpDn_Object = MibTableColumn
cucsSwEthEstcEpDn = _CucsSwEthEstcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 2),
    _CucsSwEthEstcEpDn_Type()
)
cucsSwEthEstcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpDn.setStatus("current")
_CucsSwEthEstcEpRn_Type = SnmpAdminString
_CucsSwEthEstcEpRn_Object = MibTableColumn
cucsSwEthEstcEpRn = _CucsSwEthEstcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 3),
    _CucsSwEthEstcEpRn_Type()
)
cucsSwEthEstcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpRn.setStatus("current")
_CucsSwEthEstcEpAdminState_Type = CucsFabricAdminState
_CucsSwEthEstcEpAdminState_Object = MibTableColumn
cucsSwEthEstcEpAdminState = _CucsSwEthEstcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 4),
    _CucsSwEthEstcEpAdminState_Type()
)
cucsSwEthEstcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpAdminState.setStatus("current")
_CucsSwEthEstcEpBorderPortId_Type = Gauge32
_CucsSwEthEstcEpBorderPortId_Object = MibTableColumn
cucsSwEthEstcEpBorderPortId = _CucsSwEthEstcEpBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 5),
    _CucsSwEthEstcEpBorderPortId_Type()
)
cucsSwEthEstcEpBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpBorderPortId.setStatus("current")
_CucsSwEthEstcEpBorderSlotId_Type = Gauge32
_CucsSwEthEstcEpBorderSlotId_Object = MibTableColumn
cucsSwEthEstcEpBorderSlotId = _CucsSwEthEstcEpBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 6),
    _CucsSwEthEstcEpBorderSlotId_Type()
)
cucsSwEthEstcEpBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpBorderSlotId.setStatus("current")
_CucsSwEthEstcEpChassisId_Type = Gauge32
_CucsSwEthEstcEpChassisId_Object = MibTableColumn
cucsSwEthEstcEpChassisId = _CucsSwEthEstcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 7),
    _CucsSwEthEstcEpChassisId_Type()
)
cucsSwEthEstcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpChassisId.setStatus("current")
_CucsSwEthEstcEpCosValue_Type = Gauge32
_CucsSwEthEstcEpCosValue_Object = MibTableColumn
cucsSwEthEstcEpCosValue = _CucsSwEthEstcEpCosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 8),
    _CucsSwEthEstcEpCosValue_Type()
)
cucsSwEthEstcEpCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpCosValue.setStatus("current")
_CucsSwEthEstcEpEpDn_Type = SnmpAdminString
_CucsSwEthEstcEpEpDn_Object = MibTableColumn
cucsSwEthEstcEpEpDn = _CucsSwEthEstcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 9),
    _CucsSwEthEstcEpEpDn_Type()
)
cucsSwEthEstcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpEpDn.setStatus("current")
_CucsSwEthEstcEpIfRole_Type = CucsNetworkPortRole
_CucsSwEthEstcEpIfRole_Object = MibTableColumn
cucsSwEthEstcEpIfRole = _CucsSwEthEstcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 10),
    _CucsSwEthEstcEpIfRole_Type()
)
cucsSwEthEstcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpIfRole.setStatus("current")
_CucsSwEthEstcEpIfType_Type = CucsSwPIoEpIfType
_CucsSwEthEstcEpIfType_Object = MibTableColumn
cucsSwEthEstcEpIfType = _CucsSwEthEstcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 11),
    _CucsSwEthEstcEpIfType_Type()
)
cucsSwEthEstcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpIfType.setStatus("current")
_CucsSwEthEstcEpLocale_Type = CucsSwEstcEpLocale
_CucsSwEthEstcEpLocale_Object = MibTableColumn
cucsSwEthEstcEpLocale = _CucsSwEthEstcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 12),
    _CucsSwEthEstcEpLocale_Type()
)
cucsSwEthEstcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpLocale.setStatus("current")
_CucsSwEthEstcEpName_Type = SnmpAdminString
_CucsSwEthEstcEpName_Object = MibTableColumn
cucsSwEthEstcEpName = _CucsSwEthEstcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 13),
    _CucsSwEthEstcEpName_Type()
)
cucsSwEthEstcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpName.setStatus("current")
_CucsSwEthEstcEpPeerDn_Type = SnmpAdminString
_CucsSwEthEstcEpPeerDn_Object = MibTableColumn
cucsSwEthEstcEpPeerDn = _CucsSwEthEstcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 14),
    _CucsSwEthEstcEpPeerDn_Type()
)
cucsSwEthEstcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPeerDn.setStatus("current")
_CucsSwEthEstcEpPeerPortId_Type = Gauge32
_CucsSwEthEstcEpPeerPortId_Object = MibTableColumn
cucsSwEthEstcEpPeerPortId = _CucsSwEthEstcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 15),
    _CucsSwEthEstcEpPeerPortId_Type()
)
cucsSwEthEstcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPeerPortId.setStatus("current")
_CucsSwEthEstcEpPeerSlotId_Type = Gauge32
_CucsSwEthEstcEpPeerSlotId_Object = MibTableColumn
cucsSwEthEstcEpPeerSlotId = _CucsSwEthEstcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 16),
    _CucsSwEthEstcEpPeerSlotId_Type()
)
cucsSwEthEstcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPeerSlotId.setStatus("current")
_CucsSwEthEstcEpPinGroupName_Type = SnmpAdminString
_CucsSwEthEstcEpPinGroupName_Object = MibTableColumn
cucsSwEthEstcEpPinGroupName = _CucsSwEthEstcEpPinGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 17),
    _CucsSwEthEstcEpPinGroupName_Type()
)
cucsSwEthEstcEpPinGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPinGroupName.setStatus("current")
_CucsSwEthEstcEpPortId_Type = Gauge32
_CucsSwEthEstcEpPortId_Object = MibTableColumn
cucsSwEthEstcEpPortId = _CucsSwEthEstcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 18),
    _CucsSwEthEstcEpPortId_Type()
)
cucsSwEthEstcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPortId.setStatus("current")
_CucsSwEthEstcEpPortMode_Type = CucsFabricEthEstcPortMode
_CucsSwEthEstcEpPortMode_Object = MibTableColumn
cucsSwEthEstcEpPortMode = _CucsSwEthEstcEpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 19),
    _CucsSwEthEstcEpPortMode_Type()
)
cucsSwEthEstcEpPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPortMode.setStatus("current")
_CucsSwEthEstcEpSlotId_Type = Gauge32
_CucsSwEthEstcEpSlotId_Object = MibTableColumn
cucsSwEthEstcEpSlotId = _CucsSwEthEstcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 20),
    _CucsSwEthEstcEpSlotId_Type()
)
cucsSwEthEstcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpSlotId.setStatus("current")
_CucsSwEthEstcEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthEstcEpSwitchId_Object = MibTableColumn
cucsSwEthEstcEpSwitchId = _CucsSwEthEstcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 21),
    _CucsSwEthEstcEpSwitchId_Type()
)
cucsSwEthEstcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpSwitchId.setStatus("current")
_CucsSwEthEstcEpTransport_Type = CucsSwEthEstcEpTransport
_CucsSwEthEstcEpTransport_Object = MibTableColumn
cucsSwEthEstcEpTransport = _CucsSwEthEstcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 22),
    _CucsSwEthEstcEpTransport_Type()
)
cucsSwEthEstcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpTransport.setStatus("current")
_CucsSwEthEstcEpType_Type = CucsNetworkConnectionType
_CucsSwEthEstcEpType_Object = MibTableColumn
cucsSwEthEstcEpType = _CucsSwEthEstcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 23),
    _CucsSwEthEstcEpType_Type()
)
cucsSwEthEstcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpType.setStatus("current")
_CucsSwEthEstcEpAdminSpeed_Type = CucsPortEthSpeed
_CucsSwEthEstcEpAdminSpeed_Object = MibTableColumn
cucsSwEthEstcEpAdminSpeed = _CucsSwEthEstcEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 24),
    _CucsSwEthEstcEpAdminSpeed_Type()
)
cucsSwEthEstcEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpAdminSpeed.setStatus("current")
_CucsSwEthEstcEpPcId_Type = Gauge32
_CucsSwEthEstcEpPcId_Object = MibTableColumn
cucsSwEthEstcEpPcId = _CucsSwEthEstcEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 25),
    _CucsSwEthEstcEpPcId_Type()
)
cucsSwEthEstcEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPcId.setStatus("current")
_CucsSwEthEstcEpPeerChassisId_Type = Gauge32
_CucsSwEthEstcEpPeerChassisId_Object = MibTableColumn
cucsSwEthEstcEpPeerChassisId = _CucsSwEthEstcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 26),
    _CucsSwEthEstcEpPeerChassisId_Type()
)
cucsSwEthEstcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPeerChassisId.setStatus("current")
_CucsSwEthEstcEpCdp_Type = CucsNwctrlAdminState
_CucsSwEthEstcEpCdp_Object = MibTableColumn
cucsSwEthEstcEpCdp = _CucsSwEthEstcEpCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 27),
    _CucsSwEthEstcEpCdp_Type()
)
cucsSwEthEstcEpCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpCdp.setStatus("current")
_CucsSwEthEstcEpForgeMac_Type = CucsDpsecForgedTransmit
_CucsSwEthEstcEpForgeMac_Object = MibTableColumn
cucsSwEthEstcEpForgeMac = _CucsSwEthEstcEpForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 28),
    _CucsSwEthEstcEpForgeMac_Type()
)
cucsSwEthEstcEpForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpForgeMac.setStatus("current")
_CucsSwEthEstcEpUplinkFailAction_Type = CucsNwctrlLinkFailAction
_CucsSwEthEstcEpUplinkFailAction_Object = MibTableColumn
cucsSwEthEstcEpUplinkFailAction = _CucsSwEthEstcEpUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 29),
    _CucsSwEthEstcEpUplinkFailAction_Type()
)
cucsSwEthEstcEpUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpUplinkFailAction.setStatus("current")
_CucsSwEthEstcEpLc_Type = CucsSwPIoEpLc
_CucsSwEthEstcEpLc_Object = MibTableColumn
cucsSwEthEstcEpLc = _CucsSwEthEstcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 30),
    _CucsSwEthEstcEpLc_Type()
)
cucsSwEthEstcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpLc.setStatus("current")
_CucsSwEthEstcEpPriorityFlowCtrl_Type = CucsFlowctrlPriorityPause
_CucsSwEthEstcEpPriorityFlowCtrl_Object = MibTableColumn
cucsSwEthEstcEpPriorityFlowCtrl = _CucsSwEthEstcEpPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 31),
    _CucsSwEthEstcEpPriorityFlowCtrl_Type()
)
cucsSwEthEstcEpPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPriorityFlowCtrl.setStatus("current")
_CucsSwEthEstcEpRecvFlowCtrl_Type = CucsFlowctrlFlowControl
_CucsSwEthEstcEpRecvFlowCtrl_Object = MibTableColumn
cucsSwEthEstcEpRecvFlowCtrl = _CucsSwEthEstcEpRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 32),
    _CucsSwEthEstcEpRecvFlowCtrl_Type()
)
cucsSwEthEstcEpRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpRecvFlowCtrl.setStatus("current")
_CucsSwEthEstcEpSendFlowCtrl_Type = CucsFlowctrlFlowControl
_CucsSwEthEstcEpSendFlowCtrl_Object = MibTableColumn
cucsSwEthEstcEpSendFlowCtrl = _CucsSwEthEstcEpSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 33),
    _CucsSwEthEstcEpSendFlowCtrl_Type()
)
cucsSwEthEstcEpSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpSendFlowCtrl.setStatus("current")
_CucsSwEthEstcEpAggrPortId_Type = Gauge32
_CucsSwEthEstcEpAggrPortId_Object = MibTableColumn
cucsSwEthEstcEpAggrPortId = _CucsSwEthEstcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 34),
    _CucsSwEthEstcEpAggrPortId_Type()
)
cucsSwEthEstcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpAggrPortId.setStatus("current")
_CucsSwEthEstcEpBorderAggrPortId_Type = Gauge32
_CucsSwEthEstcEpBorderAggrPortId_Object = MibTableColumn
cucsSwEthEstcEpBorderAggrPortId = _CucsSwEthEstcEpBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 35),
    _CucsSwEthEstcEpBorderAggrPortId_Type()
)
cucsSwEthEstcEpBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpBorderAggrPortId.setStatus("current")
_CucsSwEthEstcEpPeerAggrPortId_Type = Gauge32
_CucsSwEthEstcEpPeerAggrPortId_Object = MibTableColumn
cucsSwEthEstcEpPeerAggrPortId = _CucsSwEthEstcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 36),
    _CucsSwEthEstcEpPeerAggrPortId_Type()
)
cucsSwEthEstcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpPeerAggrPortId.setStatus("current")
_CucsSwEthEstcEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwEthEstcEpAutoNegotiate_Object = MibTableColumn
cucsSwEthEstcEpAutoNegotiate = _CucsSwEthEstcEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 6, 1, 37),
    _CucsSwEthEstcEpAutoNegotiate_Type()
)
cucsSwEthEstcEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcEpAutoNegotiate.setStatus("current")
_CucsSwEthLanBorderTable_Object = MibTable
cucsSwEthLanBorderTable = _CucsSwEthLanBorderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7)
)
if mibBuilder.loadTexts:
    cucsSwEthLanBorderTable.setStatus("current")
_CucsSwEthLanBorderEntry_Object = MibTableRow
cucsSwEthLanBorderEntry = _CucsSwEthLanBorderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1)
)
cucsSwEthLanBorderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanBorderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanBorderEntry.setStatus("current")
_CucsSwEthLanBorderInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanBorderInstanceId_Object = MibTableColumn
cucsSwEthLanBorderInstanceId = _CucsSwEthLanBorderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 1),
    _CucsSwEthLanBorderInstanceId_Type()
)
cucsSwEthLanBorderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderInstanceId.setStatus("current")
_CucsSwEthLanBorderDn_Type = CucsManagedObjectDn
_CucsSwEthLanBorderDn_Object = MibTableColumn
cucsSwEthLanBorderDn = _CucsSwEthLanBorderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 2),
    _CucsSwEthLanBorderDn_Type()
)
cucsSwEthLanBorderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderDn.setStatus("current")
_CucsSwEthLanBorderRn_Type = SnmpAdminString
_CucsSwEthLanBorderRn_Object = MibTableColumn
cucsSwEthLanBorderRn = _CucsSwEthLanBorderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 3),
    _CucsSwEthLanBorderRn_Type()
)
cucsSwEthLanBorderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderRn.setStatus("current")
_CucsSwEthLanBorderFsmDescr_Type = SnmpAdminString
_CucsSwEthLanBorderFsmDescr_Object = MibTableColumn
cucsSwEthLanBorderFsmDescr = _CucsSwEthLanBorderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 4),
    _CucsSwEthLanBorderFsmDescr_Type()
)
cucsSwEthLanBorderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmDescr.setStatus("current")
_CucsSwEthLanBorderFsmPrev_Type = SnmpAdminString
_CucsSwEthLanBorderFsmPrev_Object = MibTableColumn
cucsSwEthLanBorderFsmPrev = _CucsSwEthLanBorderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 5),
    _CucsSwEthLanBorderFsmPrev_Type()
)
cucsSwEthLanBorderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmPrev.setStatus("current")
_CucsSwEthLanBorderFsmProgr_Type = Gauge32
_CucsSwEthLanBorderFsmProgr_Object = MibTableColumn
cucsSwEthLanBorderFsmProgr = _CucsSwEthLanBorderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 6),
    _CucsSwEthLanBorderFsmProgr_Type()
)
cucsSwEthLanBorderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmProgr.setStatus("current")
_CucsSwEthLanBorderFsmRmtInvErrCode_Type = Gauge32
_CucsSwEthLanBorderFsmRmtInvErrCode_Object = MibTableColumn
cucsSwEthLanBorderFsmRmtInvErrCode = _CucsSwEthLanBorderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 7),
    _CucsSwEthLanBorderFsmRmtInvErrCode_Type()
)
cucsSwEthLanBorderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmRmtInvErrCode.setStatus("current")
_CucsSwEthLanBorderFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwEthLanBorderFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwEthLanBorderFsmRmtInvErrDescr = _CucsSwEthLanBorderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 8),
    _CucsSwEthLanBorderFsmRmtInvErrDescr_Type()
)
cucsSwEthLanBorderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmRmtInvErrDescr.setStatus("current")
_CucsSwEthLanBorderFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwEthLanBorderFsmRmtInvRslt_Object = MibTableColumn
cucsSwEthLanBorderFsmRmtInvRslt = _CucsSwEthLanBorderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 9),
    _CucsSwEthLanBorderFsmRmtInvRslt_Type()
)
cucsSwEthLanBorderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmRmtInvRslt.setStatus("current")
_CucsSwEthLanBorderFsmStageDescr_Type = SnmpAdminString
_CucsSwEthLanBorderFsmStageDescr_Object = MibTableColumn
cucsSwEthLanBorderFsmStageDescr = _CucsSwEthLanBorderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 10),
    _CucsSwEthLanBorderFsmStageDescr_Type()
)
cucsSwEthLanBorderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageDescr.setStatus("current")
_CucsSwEthLanBorderFsmStamp_Type = DateAndTime
_CucsSwEthLanBorderFsmStamp_Object = MibTableColumn
cucsSwEthLanBorderFsmStamp = _CucsSwEthLanBorderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 11),
    _CucsSwEthLanBorderFsmStamp_Type()
)
cucsSwEthLanBorderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStamp.setStatus("current")
_CucsSwEthLanBorderFsmStatus_Type = SnmpAdminString
_CucsSwEthLanBorderFsmStatus_Object = MibTableColumn
cucsSwEthLanBorderFsmStatus = _CucsSwEthLanBorderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 12),
    _CucsSwEthLanBorderFsmStatus_Type()
)
cucsSwEthLanBorderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStatus.setStatus("current")
_CucsSwEthLanBorderFsmTry_Type = Gauge32
_CucsSwEthLanBorderFsmTry_Object = MibTableColumn
cucsSwEthLanBorderFsmTry = _CucsSwEthLanBorderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 13),
    _CucsSwEthLanBorderFsmTry_Type()
)
cucsSwEthLanBorderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTry.setStatus("current")
_CucsSwEthLanBorderLocale_Type = CucsSwBorderDomainLocale
_CucsSwEthLanBorderLocale_Object = MibTableColumn
cucsSwEthLanBorderLocale = _CucsSwEthLanBorderLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 14),
    _CucsSwEthLanBorderLocale_Type()
)
cucsSwEthLanBorderLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderLocale.setStatus("current")
_CucsSwEthLanBorderName_Type = SnmpAdminString
_CucsSwEthLanBorderName_Object = MibTableColumn
cucsSwEthLanBorderName = _CucsSwEthLanBorderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 15),
    _CucsSwEthLanBorderName_Type()
)
cucsSwEthLanBorderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderName.setStatus("current")
_CucsSwEthLanBorderSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthLanBorderSwitchId_Object = MibTableColumn
cucsSwEthLanBorderSwitchId = _CucsSwEthLanBorderSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 16),
    _CucsSwEthLanBorderSwitchId_Type()
)
cucsSwEthLanBorderSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderSwitchId.setStatus("current")
_CucsSwEthLanBorderTransport_Type = CucsSwEthLanBorderTransport
_CucsSwEthLanBorderTransport_Object = MibTableColumn
cucsSwEthLanBorderTransport = _CucsSwEthLanBorderTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 17),
    _CucsSwEthLanBorderTransport_Type()
)
cucsSwEthLanBorderTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderTransport.setStatus("current")
_CucsSwEthLanBorderType_Type = CucsSwLanBorderType
_CucsSwEthLanBorderType_Object = MibTableColumn
cucsSwEthLanBorderType = _CucsSwEthLanBorderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 18),
    _CucsSwEthLanBorderType_Type()
)
cucsSwEthLanBorderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderType.setStatus("current")
_CucsSwEthLanBorderDeployFlag_Type = Integer32
_CucsSwEthLanBorderDeployFlag_Object = MibTableColumn
cucsSwEthLanBorderDeployFlag = _CucsSwEthLanBorderDeployFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 19),
    _CucsSwEthLanBorderDeployFlag_Type()
)
cucsSwEthLanBorderDeployFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderDeployFlag.setStatus("current")
_CucsSwEthLanBorderFsmFlags_Type = SnmpAdminString
_CucsSwEthLanBorderFsmFlags_Object = MibTableColumn
cucsSwEthLanBorderFsmFlags = _CucsSwEthLanBorderFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 20),
    _CucsSwEthLanBorderFsmFlags_Type()
)
cucsSwEthLanBorderFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmFlags.setStatus("current")
_CucsSwEthLanBorderUdldMsgInterval_Type = Gauge32
_CucsSwEthLanBorderUdldMsgInterval_Object = MibTableColumn
cucsSwEthLanBorderUdldMsgInterval = _CucsSwEthLanBorderUdldMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 21),
    _CucsSwEthLanBorderUdldMsgInterval_Type()
)
cucsSwEthLanBorderUdldMsgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderUdldMsgInterval.setStatus("current")
_CucsSwEthLanBorderUdldRecoveryAction_Type = CucsFabricRecoveryAction
_CucsSwEthLanBorderUdldRecoveryAction_Object = MibTableColumn
cucsSwEthLanBorderUdldRecoveryAction = _CucsSwEthLanBorderUdldRecoveryAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 22),
    _CucsSwEthLanBorderUdldRecoveryAction_Type()
)
cucsSwEthLanBorderUdldRecoveryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderUdldRecoveryAction.setStatus("current")
_CucsSwEthLanBorderLastVlanGrpComputeTime_Type = DateAndTime
_CucsSwEthLanBorderLastVlanGrpComputeTime_Object = MibTableColumn
cucsSwEthLanBorderLastVlanGrpComputeTime = _CucsSwEthLanBorderLastVlanGrpComputeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 7, 1, 23),
    _CucsSwEthLanBorderLastVlanGrpComputeTime_Type()
)
cucsSwEthLanBorderLastVlanGrpComputeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderLastVlanGrpComputeTime.setStatus("current")
_CucsSwEthLanBorderFsmTaskTable_Object = MibTable
cucsSwEthLanBorderFsmTaskTable = _CucsSwEthLanBorderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8)
)
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskTable.setStatus("current")
_CucsSwEthLanBorderFsmTaskEntry_Object = MibTableRow
cucsSwEthLanBorderFsmTaskEntry = _CucsSwEthLanBorderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8, 1)
)
cucsSwEthLanBorderFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanBorderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskEntry.setStatus("current")
_CucsSwEthLanBorderFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanBorderFsmTaskInstanceId_Object = MibTableColumn
cucsSwEthLanBorderFsmTaskInstanceId = _CucsSwEthLanBorderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8, 1, 1),
    _CucsSwEthLanBorderFsmTaskInstanceId_Type()
)
cucsSwEthLanBorderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskInstanceId.setStatus("current")
_CucsSwEthLanBorderFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwEthLanBorderFsmTaskDn_Object = MibTableColumn
cucsSwEthLanBorderFsmTaskDn = _CucsSwEthLanBorderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8, 1, 2),
    _CucsSwEthLanBorderFsmTaskDn_Type()
)
cucsSwEthLanBorderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskDn.setStatus("current")
_CucsSwEthLanBorderFsmTaskRn_Type = SnmpAdminString
_CucsSwEthLanBorderFsmTaskRn_Object = MibTableColumn
cucsSwEthLanBorderFsmTaskRn = _CucsSwEthLanBorderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8, 1, 3),
    _CucsSwEthLanBorderFsmTaskRn_Type()
)
cucsSwEthLanBorderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskRn.setStatus("current")
_CucsSwEthLanBorderFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwEthLanBorderFsmTaskCompletion_Object = MibTableColumn
cucsSwEthLanBorderFsmTaskCompletion = _CucsSwEthLanBorderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8, 1, 4),
    _CucsSwEthLanBorderFsmTaskCompletion_Type()
)
cucsSwEthLanBorderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskCompletion.setStatus("current")
_CucsSwEthLanBorderFsmTaskFlags_Type = CucsSwEthLanBorderFsmTaskFlags
_CucsSwEthLanBorderFsmTaskFlags_Object = MibTableColumn
cucsSwEthLanBorderFsmTaskFlags = _CucsSwEthLanBorderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8, 1, 5),
    _CucsSwEthLanBorderFsmTaskFlags_Type()
)
cucsSwEthLanBorderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskFlags.setStatus("current")
_CucsSwEthLanBorderFsmTaskItem_Type = CucsSwEthLanBorderFsmTaskItem
_CucsSwEthLanBorderFsmTaskItem_Object = MibTableColumn
cucsSwEthLanBorderFsmTaskItem = _CucsSwEthLanBorderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8, 1, 6),
    _CucsSwEthLanBorderFsmTaskItem_Type()
)
cucsSwEthLanBorderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskItem.setStatus("current")
_CucsSwEthLanBorderFsmTaskSeqId_Type = Gauge32
_CucsSwEthLanBorderFsmTaskSeqId_Object = MibTableColumn
cucsSwEthLanBorderFsmTaskSeqId = _CucsSwEthLanBorderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 8, 1, 7),
    _CucsSwEthLanBorderFsmTaskSeqId_Type()
)
cucsSwEthLanBorderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTaskSeqId.setStatus("current")
_CucsSwEthLanEpTable_Object = MibTable
cucsSwEthLanEpTable = _CucsSwEthLanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9)
)
if mibBuilder.loadTexts:
    cucsSwEthLanEpTable.setStatus("current")
_CucsSwEthLanEpEntry_Object = MibTableRow
cucsSwEthLanEpEntry = _CucsSwEthLanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1)
)
cucsSwEthLanEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanEpEntry.setStatus("current")
_CucsSwEthLanEpInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanEpInstanceId_Object = MibTableColumn
cucsSwEthLanEpInstanceId = _CucsSwEthLanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 1),
    _CucsSwEthLanEpInstanceId_Type()
)
cucsSwEthLanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanEpInstanceId.setStatus("current")
_CucsSwEthLanEpDn_Type = CucsManagedObjectDn
_CucsSwEthLanEpDn_Object = MibTableColumn
cucsSwEthLanEpDn = _CucsSwEthLanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 2),
    _CucsSwEthLanEpDn_Type()
)
cucsSwEthLanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpDn.setStatus("current")
_CucsSwEthLanEpRn_Type = SnmpAdminString
_CucsSwEthLanEpRn_Object = MibTableColumn
cucsSwEthLanEpRn = _CucsSwEthLanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 3),
    _CucsSwEthLanEpRn_Type()
)
cucsSwEthLanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpRn.setStatus("current")
_CucsSwEthLanEpAdminSpeed_Type = CucsPortEthSpeed
_CucsSwEthLanEpAdminSpeed_Object = MibTableColumn
cucsSwEthLanEpAdminSpeed = _CucsSwEthLanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 4),
    _CucsSwEthLanEpAdminSpeed_Type()
)
cucsSwEthLanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpAdminSpeed.setStatus("current")
_CucsSwEthLanEpAdminState_Type = CucsFabricAdminState
_CucsSwEthLanEpAdminState_Object = MibTableColumn
cucsSwEthLanEpAdminState = _CucsSwEthLanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 5),
    _CucsSwEthLanEpAdminState_Type()
)
cucsSwEthLanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpAdminState.setStatus("current")
_CucsSwEthLanEpChassisId_Type = Gauge32
_CucsSwEthLanEpChassisId_Object = MibTableColumn
cucsSwEthLanEpChassisId = _CucsSwEthLanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 6),
    _CucsSwEthLanEpChassisId_Type()
)
cucsSwEthLanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpChassisId.setStatus("current")
_CucsSwEthLanEpEpDn_Type = SnmpAdminString
_CucsSwEthLanEpEpDn_Object = MibTableColumn
cucsSwEthLanEpEpDn = _CucsSwEthLanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 7),
    _CucsSwEthLanEpEpDn_Type()
)
cucsSwEthLanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpEpDn.setStatus("current")
_CucsSwEthLanEpIfRole_Type = CucsSwLanEpIfRole
_CucsSwEthLanEpIfRole_Object = MibTableColumn
cucsSwEthLanEpIfRole = _CucsSwEthLanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 8),
    _CucsSwEthLanEpIfRole_Type()
)
cucsSwEthLanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpIfRole.setStatus("current")
_CucsSwEthLanEpIfType_Type = CucsSwPIoEpIfType
_CucsSwEthLanEpIfType_Object = MibTableColumn
cucsSwEthLanEpIfType = _CucsSwEthLanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 9),
    _CucsSwEthLanEpIfType_Type()
)
cucsSwEthLanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpIfType.setStatus("current")
_CucsSwEthLanEpLocale_Type = CucsSwBorderEpLocale
_CucsSwEthLanEpLocale_Object = MibTableColumn
cucsSwEthLanEpLocale = _CucsSwEthLanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 10),
    _CucsSwEthLanEpLocale_Type()
)
cucsSwEthLanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpLocale.setStatus("current")
_CucsSwEthLanEpName_Type = SnmpAdminString
_CucsSwEthLanEpName_Object = MibTableColumn
cucsSwEthLanEpName = _CucsSwEthLanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 11),
    _CucsSwEthLanEpName_Type()
)
cucsSwEthLanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpName.setStatus("current")
_CucsSwEthLanEpPcId_Type = Gauge32
_CucsSwEthLanEpPcId_Object = MibTableColumn
cucsSwEthLanEpPcId = _CucsSwEthLanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 12),
    _CucsSwEthLanEpPcId_Type()
)
cucsSwEthLanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpPcId.setStatus("current")
_CucsSwEthLanEpPeerDn_Type = SnmpAdminString
_CucsSwEthLanEpPeerDn_Object = MibTableColumn
cucsSwEthLanEpPeerDn = _CucsSwEthLanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 13),
    _CucsSwEthLanEpPeerDn_Type()
)
cucsSwEthLanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpPeerDn.setStatus("current")
_CucsSwEthLanEpPeerPortId_Type = Gauge32
_CucsSwEthLanEpPeerPortId_Object = MibTableColumn
cucsSwEthLanEpPeerPortId = _CucsSwEthLanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 14),
    _CucsSwEthLanEpPeerPortId_Type()
)
cucsSwEthLanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpPeerPortId.setStatus("current")
_CucsSwEthLanEpPeerSlotId_Type = Gauge32
_CucsSwEthLanEpPeerSlotId_Object = MibTableColumn
cucsSwEthLanEpPeerSlotId = _CucsSwEthLanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 15),
    _CucsSwEthLanEpPeerSlotId_Type()
)
cucsSwEthLanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpPeerSlotId.setStatus("current")
_CucsSwEthLanEpPortId_Type = Gauge32
_CucsSwEthLanEpPortId_Object = MibTableColumn
cucsSwEthLanEpPortId = _CucsSwEthLanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 16),
    _CucsSwEthLanEpPortId_Type()
)
cucsSwEthLanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpPortId.setStatus("current")
_CucsSwEthLanEpPriorityFlowCtrl_Type = CucsFlowctrlPriorityPause
_CucsSwEthLanEpPriorityFlowCtrl_Object = MibTableColumn
cucsSwEthLanEpPriorityFlowCtrl = _CucsSwEthLanEpPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 17),
    _CucsSwEthLanEpPriorityFlowCtrl_Type()
)
cucsSwEthLanEpPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpPriorityFlowCtrl.setStatus("current")
_CucsSwEthLanEpRecvFlowCtrl_Type = CucsFlowctrlFlowControl
_CucsSwEthLanEpRecvFlowCtrl_Object = MibTableColumn
cucsSwEthLanEpRecvFlowCtrl = _CucsSwEthLanEpRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 18),
    _CucsSwEthLanEpRecvFlowCtrl_Type()
)
cucsSwEthLanEpRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpRecvFlowCtrl.setStatus("current")
_CucsSwEthLanEpSendFlowCtrl_Type = CucsFlowctrlFlowControl
_CucsSwEthLanEpSendFlowCtrl_Object = MibTableColumn
cucsSwEthLanEpSendFlowCtrl = _CucsSwEthLanEpSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 19),
    _CucsSwEthLanEpSendFlowCtrl_Type()
)
cucsSwEthLanEpSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpSendFlowCtrl.setStatus("current")
_CucsSwEthLanEpSlotId_Type = Gauge32
_CucsSwEthLanEpSlotId_Object = MibTableColumn
cucsSwEthLanEpSlotId = _CucsSwEthLanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 20),
    _CucsSwEthLanEpSlotId_Type()
)
cucsSwEthLanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpSlotId.setStatus("current")
_CucsSwEthLanEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthLanEpSwitchId_Object = MibTableColumn
cucsSwEthLanEpSwitchId = _CucsSwEthLanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 21),
    _CucsSwEthLanEpSwitchId_Type()
)
cucsSwEthLanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpSwitchId.setStatus("current")
_CucsSwEthLanEpTransport_Type = CucsSwEthLanEpTransport
_CucsSwEthLanEpTransport_Object = MibTableColumn
cucsSwEthLanEpTransport = _CucsSwEthLanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 22),
    _CucsSwEthLanEpTransport_Type()
)
cucsSwEthLanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpTransport.setStatus("current")
_CucsSwEthLanEpType_Type = CucsSwLanEpType
_CucsSwEthLanEpType_Object = MibTableColumn
cucsSwEthLanEpType = _CucsSwEthLanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 23),
    _CucsSwEthLanEpType_Type()
)
cucsSwEthLanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpType.setStatus("current")
_CucsSwEthLanEpPeerChassisId_Type = Gauge32
_CucsSwEthLanEpPeerChassisId_Object = MibTableColumn
cucsSwEthLanEpPeerChassisId = _CucsSwEthLanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 24),
    _CucsSwEthLanEpPeerChassisId_Type()
)
cucsSwEthLanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpPeerChassisId.setStatus("current")
_CucsSwEthLanEpLc_Type = CucsSwPIoEpLc
_CucsSwEthLanEpLc_Object = MibTableColumn
cucsSwEthLanEpLc = _CucsSwEthLanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 25),
    _CucsSwEthLanEpLc_Type()
)
cucsSwEthLanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpLc.setStatus("current")
_CucsSwEthLanEpUdldAdminState_Type = CucsSwEthLanEpUdldAdminState
_CucsSwEthLanEpUdldAdminState_Object = MibTableColumn
cucsSwEthLanEpUdldAdminState = _CucsSwEthLanEpUdldAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 27),
    _CucsSwEthLanEpUdldAdminState_Type()
)
cucsSwEthLanEpUdldAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpUdldAdminState.setStatus("current")
_CucsSwEthLanEpUdldMode_Type = CucsSwEthLanEpUdldMode
_CucsSwEthLanEpUdldMode_Object = MibTableColumn
cucsSwEthLanEpUdldMode = _CucsSwEthLanEpUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 28),
    _CucsSwEthLanEpUdldMode_Type()
)
cucsSwEthLanEpUdldMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpUdldMode.setStatus("current")
_CucsSwEthLanEpAggrPortId_Type = Gauge32
_CucsSwEthLanEpAggrPortId_Object = MibTableColumn
cucsSwEthLanEpAggrPortId = _CucsSwEthLanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 29),
    _CucsSwEthLanEpAggrPortId_Type()
)
cucsSwEthLanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpAggrPortId.setStatus("current")
_CucsSwEthLanEpPeerAggrPortId_Type = Gauge32
_CucsSwEthLanEpPeerAggrPortId_Object = MibTableColumn
cucsSwEthLanEpPeerAggrPortId = _CucsSwEthLanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 30),
    _CucsSwEthLanEpPeerAggrPortId_Type()
)
cucsSwEthLanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpPeerAggrPortId.setStatus("current")
_CucsSwEthLanEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwEthLanEpAutoNegotiate_Object = MibTableColumn
cucsSwEthLanEpAutoNegotiate = _CucsSwEthLanEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 9, 1, 31),
    _CucsSwEthLanEpAutoNegotiate_Type()
)
cucsSwEthLanEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanEpAutoNegotiate.setStatus("current")
_CucsSwEthLanMonTable_Object = MibTable
cucsSwEthLanMonTable = _CucsSwEthLanMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10)
)
if mibBuilder.loadTexts:
    cucsSwEthLanMonTable.setStatus("current")
_CucsSwEthLanMonEntry_Object = MibTableRow
cucsSwEthLanMonEntry = _CucsSwEthLanMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1)
)
cucsSwEthLanMonEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanMonInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanMonEntry.setStatus("current")
_CucsSwEthLanMonInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanMonInstanceId_Object = MibTableColumn
cucsSwEthLanMonInstanceId = _CucsSwEthLanMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1, 1),
    _CucsSwEthLanMonInstanceId_Type()
)
cucsSwEthLanMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanMonInstanceId.setStatus("current")
_CucsSwEthLanMonDn_Type = CucsManagedObjectDn
_CucsSwEthLanMonDn_Object = MibTableColumn
cucsSwEthLanMonDn = _CucsSwEthLanMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1, 2),
    _CucsSwEthLanMonDn_Type()
)
cucsSwEthLanMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanMonDn.setStatus("current")
_CucsSwEthLanMonRn_Type = SnmpAdminString
_CucsSwEthLanMonRn_Object = MibTableColumn
cucsSwEthLanMonRn = _CucsSwEthLanMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1, 3),
    _CucsSwEthLanMonRn_Type()
)
cucsSwEthLanMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanMonRn.setStatus("current")
_CucsSwEthLanMonLocale_Type = CucsSwMonDomainLocale
_CucsSwEthLanMonLocale_Object = MibTableColumn
cucsSwEthLanMonLocale = _CucsSwEthLanMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1, 4),
    _CucsSwEthLanMonLocale_Type()
)
cucsSwEthLanMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanMonLocale.setStatus("current")
_CucsSwEthLanMonName_Type = SnmpAdminString
_CucsSwEthLanMonName_Object = MibTableColumn
cucsSwEthLanMonName = _CucsSwEthLanMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1, 5),
    _CucsSwEthLanMonName_Type()
)
cucsSwEthLanMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanMonName.setStatus("current")
_CucsSwEthLanMonSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthLanMonSwitchId_Object = MibTableColumn
cucsSwEthLanMonSwitchId = _CucsSwEthLanMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1, 6),
    _CucsSwEthLanMonSwitchId_Type()
)
cucsSwEthLanMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanMonSwitchId.setStatus("current")
_CucsSwEthLanMonTransport_Type = CucsSwEthLanMonTransport
_CucsSwEthLanMonTransport_Object = MibTableColumn
cucsSwEthLanMonTransport = _CucsSwEthLanMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1, 7),
    _CucsSwEthLanMonTransport_Type()
)
cucsSwEthLanMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanMonTransport.setStatus("current")
_CucsSwEthLanMonType_Type = CucsSwLanMonType
_CucsSwEthLanMonType_Object = MibTableColumn
cucsSwEthLanMonType = _CucsSwEthLanMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 10, 1, 8),
    _CucsSwEthLanMonType_Type()
)
cucsSwEthLanMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanMonType.setStatus("current")
_CucsSwEthLanPcTable_Object = MibTable
cucsSwEthLanPcTable = _CucsSwEthLanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11)
)
if mibBuilder.loadTexts:
    cucsSwEthLanPcTable.setStatus("current")
_CucsSwEthLanPcEntry_Object = MibTableRow
cucsSwEthLanPcEntry = _CucsSwEthLanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1)
)
cucsSwEthLanPcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanPcEntry.setStatus("current")
_CucsSwEthLanPcInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanPcInstanceId_Object = MibTableColumn
cucsSwEthLanPcInstanceId = _CucsSwEthLanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 1),
    _CucsSwEthLanPcInstanceId_Type()
)
cucsSwEthLanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanPcInstanceId.setStatus("current")
_CucsSwEthLanPcDn_Type = CucsManagedObjectDn
_CucsSwEthLanPcDn_Object = MibTableColumn
cucsSwEthLanPcDn = _CucsSwEthLanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 2),
    _CucsSwEthLanPcDn_Type()
)
cucsSwEthLanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcDn.setStatus("current")
_CucsSwEthLanPcRn_Type = SnmpAdminString
_CucsSwEthLanPcRn_Object = MibTableColumn
cucsSwEthLanPcRn = _CucsSwEthLanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 3),
    _CucsSwEthLanPcRn_Type()
)
cucsSwEthLanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcRn.setStatus("current")
_CucsSwEthLanPcAdminSpeed_Type = CucsPortEthSpeed
_CucsSwEthLanPcAdminSpeed_Object = MibTableColumn
cucsSwEthLanPcAdminSpeed = _CucsSwEthLanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 4),
    _CucsSwEthLanPcAdminSpeed_Type()
)
cucsSwEthLanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcAdminSpeed.setStatus("current")
_CucsSwEthLanPcAdminState_Type = CucsFabricAdminState
_CucsSwEthLanPcAdminState_Object = MibTableColumn
cucsSwEthLanPcAdminState = _CucsSwEthLanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 5),
    _CucsSwEthLanPcAdminState_Type()
)
cucsSwEthLanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcAdminState.setStatus("current")
_CucsSwEthLanPcEpDn_Type = SnmpAdminString
_CucsSwEthLanPcEpDn_Object = MibTableColumn
cucsSwEthLanPcEpDn = _CucsSwEthLanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 6),
    _CucsSwEthLanPcEpDn_Type()
)
cucsSwEthLanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcEpDn.setStatus("current")
_CucsSwEthLanPcIfRole_Type = CucsSwLanPcIfRole
_CucsSwEthLanPcIfRole_Object = MibTableColumn
cucsSwEthLanPcIfRole = _CucsSwEthLanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 7),
    _CucsSwEthLanPcIfRole_Type()
)
cucsSwEthLanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcIfRole.setStatus("current")
_CucsSwEthLanPcIfType_Type = CucsSwCIoEpIfType
_CucsSwEthLanPcIfType_Object = MibTableColumn
cucsSwEthLanPcIfType = _CucsSwEthLanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 8),
    _CucsSwEthLanPcIfType_Type()
)
cucsSwEthLanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcIfType.setStatus("current")
_CucsSwEthLanPcLocale_Type = CucsSwBorderPcLocale
_CucsSwEthLanPcLocale_Object = MibTableColumn
cucsSwEthLanPcLocale = _CucsSwEthLanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 9),
    _CucsSwEthLanPcLocale_Type()
)
cucsSwEthLanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcLocale.setStatus("current")
_CucsSwEthLanPcName_Type = SnmpAdminString
_CucsSwEthLanPcName_Object = MibTableColumn
cucsSwEthLanPcName = _CucsSwEthLanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 10),
    _CucsSwEthLanPcName_Type()
)
cucsSwEthLanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcName.setStatus("current")
_CucsSwEthLanPcPeerDn_Type = SnmpAdminString
_CucsSwEthLanPcPeerDn_Object = MibTableColumn
cucsSwEthLanPcPeerDn = _CucsSwEthLanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 11),
    _CucsSwEthLanPcPeerDn_Type()
)
cucsSwEthLanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcPeerDn.setStatus("current")
_CucsSwEthLanPcPortId_Type = Gauge32
_CucsSwEthLanPcPortId_Object = MibTableColumn
cucsSwEthLanPcPortId = _CucsSwEthLanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 12),
    _CucsSwEthLanPcPortId_Type()
)
cucsSwEthLanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcPortId.setStatus("current")
_CucsSwEthLanPcPriorityFlowCtrl_Type = CucsFlowctrlPriorityPause
_CucsSwEthLanPcPriorityFlowCtrl_Object = MibTableColumn
cucsSwEthLanPcPriorityFlowCtrl = _CucsSwEthLanPcPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 13),
    _CucsSwEthLanPcPriorityFlowCtrl_Type()
)
cucsSwEthLanPcPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcPriorityFlowCtrl.setStatus("current")
_CucsSwEthLanPcRecvFlowCtrl_Type = CucsFlowctrlFlowControl
_CucsSwEthLanPcRecvFlowCtrl_Object = MibTableColumn
cucsSwEthLanPcRecvFlowCtrl = _CucsSwEthLanPcRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 14),
    _CucsSwEthLanPcRecvFlowCtrl_Type()
)
cucsSwEthLanPcRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcRecvFlowCtrl.setStatus("current")
_CucsSwEthLanPcSendFlowCtrl_Type = CucsFlowctrlFlowControl
_CucsSwEthLanPcSendFlowCtrl_Object = MibTableColumn
cucsSwEthLanPcSendFlowCtrl = _CucsSwEthLanPcSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 15),
    _CucsSwEthLanPcSendFlowCtrl_Type()
)
cucsSwEthLanPcSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcSendFlowCtrl.setStatus("current")
_CucsSwEthLanPcSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthLanPcSwitchId_Object = MibTableColumn
cucsSwEthLanPcSwitchId = _CucsSwEthLanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 16),
    _CucsSwEthLanPcSwitchId_Type()
)
cucsSwEthLanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcSwitchId.setStatus("current")
_CucsSwEthLanPcTransport_Type = CucsSwEthLanPcTransport
_CucsSwEthLanPcTransport_Object = MibTableColumn
cucsSwEthLanPcTransport = _CucsSwEthLanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 17),
    _CucsSwEthLanPcTransport_Type()
)
cucsSwEthLanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcTransport.setStatus("current")
_CucsSwEthLanPcType_Type = CucsSwLanPcType
_CucsSwEthLanPcType_Object = MibTableColumn
cucsSwEthLanPcType = _CucsSwEthLanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 18),
    _CucsSwEthLanPcType_Type()
)
cucsSwEthLanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcType.setStatus("current")
_CucsSwEthLanPcMonTrafDir_Type = CucsFabricTrafficDirection
_CucsSwEthLanPcMonTrafDir_Object = MibTableColumn
cucsSwEthLanPcMonTrafDir = _CucsSwEthLanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 19),
    _CucsSwEthLanPcMonTrafDir_Type()
)
cucsSwEthLanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcMonTrafDir.setStatus("current")
_CucsSwEthLanPcLacpFastTimer_Type = TruthValue
_CucsSwEthLanPcLacpFastTimer_Object = MibTableColumn
cucsSwEthLanPcLacpFastTimer = _CucsSwEthLanPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 21),
    _CucsSwEthLanPcLacpFastTimer_Type()
)
cucsSwEthLanPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcLacpFastTimer.setStatus("current")
_CucsSwEthLanPcLacpSuspendIndividual_Type = TruthValue
_CucsSwEthLanPcLacpSuspendIndividual_Object = MibTableColumn
cucsSwEthLanPcLacpSuspendIndividual = _CucsSwEthLanPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 22),
    _CucsSwEthLanPcLacpSuspendIndividual_Type()
)
cucsSwEthLanPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcLacpSuspendIndividual.setStatus("current")
_CucsSwEthLanPcAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwEthLanPcAutoNegotiate_Object = MibTableColumn
cucsSwEthLanPcAutoNegotiate = _CucsSwEthLanPcAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 11, 1, 23),
    _CucsSwEthLanPcAutoNegotiate_Type()
)
cucsSwEthLanPcAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanPcAutoNegotiate.setStatus("current")
_CucsSwEthMonTable_Object = MibTable
cucsSwEthMonTable = _CucsSwEthMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12)
)
if mibBuilder.loadTexts:
    cucsSwEthMonTable.setStatus("current")
_CucsSwEthMonEntry_Object = MibTableRow
cucsSwEthMonEntry = _CucsSwEthMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1)
)
cucsSwEthMonEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthMonInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthMonEntry.setStatus("current")
_CucsSwEthMonInstanceId_Type = CucsManagedObjectId
_CucsSwEthMonInstanceId_Object = MibTableColumn
cucsSwEthMonInstanceId = _CucsSwEthMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 1),
    _CucsSwEthMonInstanceId_Type()
)
cucsSwEthMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthMonInstanceId.setStatus("current")
_CucsSwEthMonDn_Type = CucsManagedObjectDn
_CucsSwEthMonDn_Object = MibTableColumn
cucsSwEthMonDn = _CucsSwEthMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 2),
    _CucsSwEthMonDn_Type()
)
cucsSwEthMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDn.setStatus("current")
_CucsSwEthMonRn_Type = SnmpAdminString
_CucsSwEthMonRn_Object = MibTableColumn
cucsSwEthMonRn = _CucsSwEthMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 3),
    _CucsSwEthMonRn_Type()
)
cucsSwEthMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonRn.setStatus("current")
_CucsSwEthMonAdminState_Type = CucsSwMonAdminState
_CucsSwEthMonAdminState_Object = MibTableColumn
cucsSwEthMonAdminState = _CucsSwEthMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 4),
    _CucsSwEthMonAdminState_Type()
)
cucsSwEthMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonAdminState.setStatus("current")
_CucsSwEthMonFsmDescr_Type = SnmpAdminString
_CucsSwEthMonFsmDescr_Object = MibTableColumn
cucsSwEthMonFsmDescr = _CucsSwEthMonFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 5),
    _CucsSwEthMonFsmDescr_Type()
)
cucsSwEthMonFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmDescr.setStatus("current")
_CucsSwEthMonFsmPrev_Type = SnmpAdminString
_CucsSwEthMonFsmPrev_Object = MibTableColumn
cucsSwEthMonFsmPrev = _CucsSwEthMonFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 6),
    _CucsSwEthMonFsmPrev_Type()
)
cucsSwEthMonFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmPrev.setStatus("current")
_CucsSwEthMonFsmProgr_Type = Gauge32
_CucsSwEthMonFsmProgr_Object = MibTableColumn
cucsSwEthMonFsmProgr = _CucsSwEthMonFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 7),
    _CucsSwEthMonFsmProgr_Type()
)
cucsSwEthMonFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmProgr.setStatus("current")
_CucsSwEthMonFsmRmtInvErrCode_Type = Gauge32
_CucsSwEthMonFsmRmtInvErrCode_Object = MibTableColumn
cucsSwEthMonFsmRmtInvErrCode = _CucsSwEthMonFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 8),
    _CucsSwEthMonFsmRmtInvErrCode_Type()
)
cucsSwEthMonFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmRmtInvErrCode.setStatus("current")
_CucsSwEthMonFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwEthMonFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwEthMonFsmRmtInvErrDescr = _CucsSwEthMonFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 9),
    _CucsSwEthMonFsmRmtInvErrDescr_Type()
)
cucsSwEthMonFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmRmtInvErrDescr.setStatus("current")
_CucsSwEthMonFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwEthMonFsmRmtInvRslt_Object = MibTableColumn
cucsSwEthMonFsmRmtInvRslt = _CucsSwEthMonFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 10),
    _CucsSwEthMonFsmRmtInvRslt_Type()
)
cucsSwEthMonFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmRmtInvRslt.setStatus("current")
_CucsSwEthMonFsmStageDescr_Type = SnmpAdminString
_CucsSwEthMonFsmStageDescr_Object = MibTableColumn
cucsSwEthMonFsmStageDescr = _CucsSwEthMonFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 11),
    _CucsSwEthMonFsmStageDescr_Type()
)
cucsSwEthMonFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageDescr.setStatus("current")
_CucsSwEthMonFsmStamp_Type = DateAndTime
_CucsSwEthMonFsmStamp_Object = MibTableColumn
cucsSwEthMonFsmStamp = _CucsSwEthMonFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 12),
    _CucsSwEthMonFsmStamp_Type()
)
cucsSwEthMonFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStamp.setStatus("current")
_CucsSwEthMonFsmStatus_Type = SnmpAdminString
_CucsSwEthMonFsmStatus_Object = MibTableColumn
cucsSwEthMonFsmStatus = _CucsSwEthMonFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 13),
    _CucsSwEthMonFsmStatus_Type()
)
cucsSwEthMonFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStatus.setStatus("current")
_CucsSwEthMonFsmTry_Type = Gauge32
_CucsSwEthMonFsmTry_Object = MibTableColumn
cucsSwEthMonFsmTry = _CucsSwEthMonFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 14),
    _CucsSwEthMonFsmTry_Type()
)
cucsSwEthMonFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTry.setStatus("current")
_CucsSwEthMonLifeCycle_Type = CucsSwMonLifeCycle
_CucsSwEthMonLifeCycle_Object = MibTableColumn
cucsSwEthMonLifeCycle = _CucsSwEthMonLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 15),
    _CucsSwEthMonLifeCycle_Type()
)
cucsSwEthMonLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonLifeCycle.setStatus("current")
_CucsSwEthMonName_Type = SnmpAdminString
_CucsSwEthMonName_Object = MibTableColumn
cucsSwEthMonName = _CucsSwEthMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 16),
    _CucsSwEthMonName_Type()
)
cucsSwEthMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonName.setStatus("current")
_CucsSwEthMonSession_Type = Gauge32
_CucsSwEthMonSession_Object = MibTableColumn
cucsSwEthMonSession = _CucsSwEthMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 17),
    _CucsSwEthMonSession_Type()
)
cucsSwEthMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSession.setStatus("current")
_CucsSwEthMonSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthMonSwitchId_Object = MibTableColumn
cucsSwEthMonSwitchId = _CucsSwEthMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 18),
    _CucsSwEthMonSwitchId_Type()
)
cucsSwEthMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSwitchId.setStatus("current")
_CucsSwEthMonTransport_Type = CucsSwEthMonTransport
_CucsSwEthMonTransport_Object = MibTableColumn
cucsSwEthMonTransport = _CucsSwEthMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 19),
    _CucsSwEthMonTransport_Type()
)
cucsSwEthMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonTransport.setStatus("current")
_CucsSwEthMonType_Type = CucsSwEthMonType
_CucsSwEthMonType_Object = MibTableColumn
cucsSwEthMonType = _CucsSwEthMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 20),
    _CucsSwEthMonType_Type()
)
cucsSwEthMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonType.setStatus("current")
_CucsSwEthMonHasLastDest_Type = TruthValue
_CucsSwEthMonHasLastDest_Object = MibTableColumn
cucsSwEthMonHasLastDest = _CucsSwEthMonHasLastDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 21),
    _CucsSwEthMonHasLastDest_Type()
)
cucsSwEthMonHasLastDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonHasLastDest.setStatus("current")
_CucsSwEthMonPeerDn_Type = SnmpAdminString
_CucsSwEthMonPeerDn_Object = MibTableColumn
cucsSwEthMonPeerDn = _CucsSwEthMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 12, 1, 22),
    _CucsSwEthMonPeerDn_Type()
)
cucsSwEthMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonPeerDn.setStatus("current")
_CucsSwEthMonDestEpTable_Object = MibTable
cucsSwEthMonDestEpTable = _CucsSwEthMonDestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13)
)
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpTable.setStatus("current")
_CucsSwEthMonDestEpEntry_Object = MibTableRow
cucsSwEthMonDestEpEntry = _CucsSwEthMonDestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1)
)
cucsSwEthMonDestEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthMonDestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpEntry.setStatus("current")
_CucsSwEthMonDestEpInstanceId_Type = CucsManagedObjectId
_CucsSwEthMonDestEpInstanceId_Object = MibTableColumn
cucsSwEthMonDestEpInstanceId = _CucsSwEthMonDestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 1),
    _CucsSwEthMonDestEpInstanceId_Type()
)
cucsSwEthMonDestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpInstanceId.setStatus("current")
_CucsSwEthMonDestEpDn_Type = CucsManagedObjectDn
_CucsSwEthMonDestEpDn_Object = MibTableColumn
cucsSwEthMonDestEpDn = _CucsSwEthMonDestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 2),
    _CucsSwEthMonDestEpDn_Type()
)
cucsSwEthMonDestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpDn.setStatus("current")
_CucsSwEthMonDestEpRn_Type = SnmpAdminString
_CucsSwEthMonDestEpRn_Object = MibTableColumn
cucsSwEthMonDestEpRn = _CucsSwEthMonDestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 3),
    _CucsSwEthMonDestEpRn_Type()
)
cucsSwEthMonDestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpRn.setStatus("current")
_CucsSwEthMonDestEpAdminState_Type = CucsFabricAdminState
_CucsSwEthMonDestEpAdminState_Object = MibTableColumn
cucsSwEthMonDestEpAdminState = _CucsSwEthMonDestEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 4),
    _CucsSwEthMonDestEpAdminState_Type()
)
cucsSwEthMonDestEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpAdminState.setStatus("current")
_CucsSwEthMonDestEpChassisId_Type = Gauge32
_CucsSwEthMonDestEpChassisId_Object = MibTableColumn
cucsSwEthMonDestEpChassisId = _CucsSwEthMonDestEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 5),
    _CucsSwEthMonDestEpChassisId_Type()
)
cucsSwEthMonDestEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpChassisId.setStatus("current")
_CucsSwEthMonDestEpEpDn_Type = SnmpAdminString
_CucsSwEthMonDestEpEpDn_Object = MibTableColumn
cucsSwEthMonDestEpEpDn = _CucsSwEthMonDestEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 6),
    _CucsSwEthMonDestEpEpDn_Type()
)
cucsSwEthMonDestEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpEpDn.setStatus("current")
_CucsSwEthMonDestEpIfRole_Type = CucsNetworkPortRole
_CucsSwEthMonDestEpIfRole_Object = MibTableColumn
cucsSwEthMonDestEpIfRole = _CucsSwEthMonDestEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 7),
    _CucsSwEthMonDestEpIfRole_Type()
)
cucsSwEthMonDestEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpIfRole.setStatus("current")
_CucsSwEthMonDestEpIfType_Type = CucsSwPIoEpIfType
_CucsSwEthMonDestEpIfType_Object = MibTableColumn
cucsSwEthMonDestEpIfType = _CucsSwEthMonDestEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 8),
    _CucsSwEthMonDestEpIfType_Type()
)
cucsSwEthMonDestEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpIfType.setStatus("current")
_CucsSwEthMonDestEpLocale_Type = CucsNetworkLocale
_CucsSwEthMonDestEpLocale_Object = MibTableColumn
cucsSwEthMonDestEpLocale = _CucsSwEthMonDestEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 9),
    _CucsSwEthMonDestEpLocale_Type()
)
cucsSwEthMonDestEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpLocale.setStatus("current")
_CucsSwEthMonDestEpName_Type = SnmpAdminString
_CucsSwEthMonDestEpName_Object = MibTableColumn
cucsSwEthMonDestEpName = _CucsSwEthMonDestEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 10),
    _CucsSwEthMonDestEpName_Type()
)
cucsSwEthMonDestEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpName.setStatus("current")
_CucsSwEthMonDestEpPeerDn_Type = SnmpAdminString
_CucsSwEthMonDestEpPeerDn_Object = MibTableColumn
cucsSwEthMonDestEpPeerDn = _CucsSwEthMonDestEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 11),
    _CucsSwEthMonDestEpPeerDn_Type()
)
cucsSwEthMonDestEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpPeerDn.setStatus("current")
_CucsSwEthMonDestEpPeerPortId_Type = Gauge32
_CucsSwEthMonDestEpPeerPortId_Object = MibTableColumn
cucsSwEthMonDestEpPeerPortId = _CucsSwEthMonDestEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 12),
    _CucsSwEthMonDestEpPeerPortId_Type()
)
cucsSwEthMonDestEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpPeerPortId.setStatus("current")
_CucsSwEthMonDestEpPeerSlotId_Type = Gauge32
_CucsSwEthMonDestEpPeerSlotId_Object = MibTableColumn
cucsSwEthMonDestEpPeerSlotId = _CucsSwEthMonDestEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 13),
    _CucsSwEthMonDestEpPeerSlotId_Type()
)
cucsSwEthMonDestEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpPeerSlotId.setStatus("current")
_CucsSwEthMonDestEpPortId_Type = Gauge32
_CucsSwEthMonDestEpPortId_Object = MibTableColumn
cucsSwEthMonDestEpPortId = _CucsSwEthMonDestEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 14),
    _CucsSwEthMonDestEpPortId_Type()
)
cucsSwEthMonDestEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpPortId.setStatus("current")
_CucsSwEthMonDestEpSlotId_Type = Gauge32
_CucsSwEthMonDestEpSlotId_Object = MibTableColumn
cucsSwEthMonDestEpSlotId = _CucsSwEthMonDestEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 15),
    _CucsSwEthMonDestEpSlotId_Type()
)
cucsSwEthMonDestEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpSlotId.setStatus("current")
_CucsSwEthMonDestEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthMonDestEpSwitchId_Object = MibTableColumn
cucsSwEthMonDestEpSwitchId = _CucsSwEthMonDestEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 16),
    _CucsSwEthMonDestEpSwitchId_Type()
)
cucsSwEthMonDestEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpSwitchId.setStatus("current")
_CucsSwEthMonDestEpTransport_Type = CucsSwEthMonDestEpTransport
_CucsSwEthMonDestEpTransport_Object = MibTableColumn
cucsSwEthMonDestEpTransport = _CucsSwEthMonDestEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 17),
    _CucsSwEthMonDestEpTransport_Type()
)
cucsSwEthMonDestEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpTransport.setStatus("current")
_CucsSwEthMonDestEpType_Type = CucsNetworkConnectionType
_CucsSwEthMonDestEpType_Object = MibTableColumn
cucsSwEthMonDestEpType = _CucsSwEthMonDestEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 18),
    _CucsSwEthMonDestEpType_Type()
)
cucsSwEthMonDestEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpType.setStatus("current")
_CucsSwEthMonDestEpPeerChassisId_Type = Gauge32
_CucsSwEthMonDestEpPeerChassisId_Object = MibTableColumn
cucsSwEthMonDestEpPeerChassisId = _CucsSwEthMonDestEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 19),
    _CucsSwEthMonDestEpPeerChassisId_Type()
)
cucsSwEthMonDestEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpPeerChassisId.setStatus("current")
_CucsSwEthMonDestEpLc_Type = CucsSwPIoEpLc
_CucsSwEthMonDestEpLc_Object = MibTableColumn
cucsSwEthMonDestEpLc = _CucsSwEthMonDestEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 20),
    _CucsSwEthMonDestEpLc_Type()
)
cucsSwEthMonDestEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpLc.setStatus("current")
_CucsSwEthMonDestEpAdminSpeed_Type = CucsPortEthSpeed
_CucsSwEthMonDestEpAdminSpeed_Object = MibTableColumn
cucsSwEthMonDestEpAdminSpeed = _CucsSwEthMonDestEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 21),
    _CucsSwEthMonDestEpAdminSpeed_Type()
)
cucsSwEthMonDestEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpAdminSpeed.setStatus("current")
_CucsSwEthMonDestEpAggrPortId_Type = Gauge32
_CucsSwEthMonDestEpAggrPortId_Object = MibTableColumn
cucsSwEthMonDestEpAggrPortId = _CucsSwEthMonDestEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 22),
    _CucsSwEthMonDestEpAggrPortId_Type()
)
cucsSwEthMonDestEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpAggrPortId.setStatus("current")
_CucsSwEthMonDestEpPeerAggrPortId_Type = Gauge32
_CucsSwEthMonDestEpPeerAggrPortId_Object = MibTableColumn
cucsSwEthMonDestEpPeerAggrPortId = _CucsSwEthMonDestEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 23),
    _CucsSwEthMonDestEpPeerAggrPortId_Type()
)
cucsSwEthMonDestEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpPeerAggrPortId.setStatus("current")
_CucsSwEthMonDestEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwEthMonDestEpAutoNegotiate_Object = MibTableColumn
cucsSwEthMonDestEpAutoNegotiate = _CucsSwEthMonDestEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 13, 1, 24),
    _CucsSwEthMonDestEpAutoNegotiate_Type()
)
cucsSwEthMonDestEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonDestEpAutoNegotiate.setStatus("current")
_CucsSwEthMonFsmTaskTable_Object = MibTable
cucsSwEthMonFsmTaskTable = _CucsSwEthMonFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14)
)
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskTable.setStatus("current")
_CucsSwEthMonFsmTaskEntry_Object = MibTableRow
cucsSwEthMonFsmTaskEntry = _CucsSwEthMonFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14, 1)
)
cucsSwEthMonFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthMonFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskEntry.setStatus("current")
_CucsSwEthMonFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwEthMonFsmTaskInstanceId_Object = MibTableColumn
cucsSwEthMonFsmTaskInstanceId = _CucsSwEthMonFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14, 1, 1),
    _CucsSwEthMonFsmTaskInstanceId_Type()
)
cucsSwEthMonFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskInstanceId.setStatus("current")
_CucsSwEthMonFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwEthMonFsmTaskDn_Object = MibTableColumn
cucsSwEthMonFsmTaskDn = _CucsSwEthMonFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14, 1, 2),
    _CucsSwEthMonFsmTaskDn_Type()
)
cucsSwEthMonFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskDn.setStatus("current")
_CucsSwEthMonFsmTaskRn_Type = SnmpAdminString
_CucsSwEthMonFsmTaskRn_Object = MibTableColumn
cucsSwEthMonFsmTaskRn = _CucsSwEthMonFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14, 1, 3),
    _CucsSwEthMonFsmTaskRn_Type()
)
cucsSwEthMonFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskRn.setStatus("current")
_CucsSwEthMonFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwEthMonFsmTaskCompletion_Object = MibTableColumn
cucsSwEthMonFsmTaskCompletion = _CucsSwEthMonFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14, 1, 4),
    _CucsSwEthMonFsmTaskCompletion_Type()
)
cucsSwEthMonFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskCompletion.setStatus("current")
_CucsSwEthMonFsmTaskFlags_Type = CucsFsmFlags
_CucsSwEthMonFsmTaskFlags_Object = MibTableColumn
cucsSwEthMonFsmTaskFlags = _CucsSwEthMonFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14, 1, 5),
    _CucsSwEthMonFsmTaskFlags_Type()
)
cucsSwEthMonFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskFlags.setStatus("current")
_CucsSwEthMonFsmTaskItem_Type = CucsSwEthMonFsmTaskItem
_CucsSwEthMonFsmTaskItem_Object = MibTableColumn
cucsSwEthMonFsmTaskItem = _CucsSwEthMonFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14, 1, 6),
    _CucsSwEthMonFsmTaskItem_Type()
)
cucsSwEthMonFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskItem.setStatus("current")
_CucsSwEthMonFsmTaskSeqId_Type = Gauge32
_CucsSwEthMonFsmTaskSeqId_Object = MibTableColumn
cucsSwEthMonFsmTaskSeqId = _CucsSwEthMonFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 14, 1, 7),
    _CucsSwEthMonFsmTaskSeqId_Type()
)
cucsSwEthMonFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTaskSeqId.setStatus("current")
_CucsSwEthMonSrcEpTable_Object = MibTable
cucsSwEthMonSrcEpTable = _CucsSwEthMonSrcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15)
)
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpTable.setStatus("current")
_CucsSwEthMonSrcEpEntry_Object = MibTableRow
cucsSwEthMonSrcEpEntry = _CucsSwEthMonSrcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1)
)
cucsSwEthMonSrcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthMonSrcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpEntry.setStatus("current")
_CucsSwEthMonSrcEpInstanceId_Type = CucsManagedObjectId
_CucsSwEthMonSrcEpInstanceId_Object = MibTableColumn
cucsSwEthMonSrcEpInstanceId = _CucsSwEthMonSrcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 1),
    _CucsSwEthMonSrcEpInstanceId_Type()
)
cucsSwEthMonSrcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpInstanceId.setStatus("current")
_CucsSwEthMonSrcEpDn_Type = CucsManagedObjectDn
_CucsSwEthMonSrcEpDn_Object = MibTableColumn
cucsSwEthMonSrcEpDn = _CucsSwEthMonSrcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 2),
    _CucsSwEthMonSrcEpDn_Type()
)
cucsSwEthMonSrcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpDn.setStatus("current")
_CucsSwEthMonSrcEpRn_Type = SnmpAdminString
_CucsSwEthMonSrcEpRn_Object = MibTableColumn
cucsSwEthMonSrcEpRn = _CucsSwEthMonSrcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 3),
    _CucsSwEthMonSrcEpRn_Type()
)
cucsSwEthMonSrcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpRn.setStatus("current")
_CucsSwEthMonSrcEpAdminState_Type = CucsFabricAdminState
_CucsSwEthMonSrcEpAdminState_Object = MibTableColumn
cucsSwEthMonSrcEpAdminState = _CucsSwEthMonSrcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 4),
    _CucsSwEthMonSrcEpAdminState_Type()
)
cucsSwEthMonSrcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpAdminState.setStatus("current")
_CucsSwEthMonSrcEpChassisId_Type = Gauge32
_CucsSwEthMonSrcEpChassisId_Object = MibTableColumn
cucsSwEthMonSrcEpChassisId = _CucsSwEthMonSrcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 5),
    _CucsSwEthMonSrcEpChassisId_Type()
)
cucsSwEthMonSrcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpChassisId.setStatus("current")
_CucsSwEthMonSrcEpEpDn_Type = SnmpAdminString
_CucsSwEthMonSrcEpEpDn_Object = MibTableColumn
cucsSwEthMonSrcEpEpDn = _CucsSwEthMonSrcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 6),
    _CucsSwEthMonSrcEpEpDn_Type()
)
cucsSwEthMonSrcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpEpDn.setStatus("current")
_CucsSwEthMonSrcEpIfRole_Type = CucsNetworkPortRole
_CucsSwEthMonSrcEpIfRole_Object = MibTableColumn
cucsSwEthMonSrcEpIfRole = _CucsSwEthMonSrcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 7),
    _CucsSwEthMonSrcEpIfRole_Type()
)
cucsSwEthMonSrcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpIfRole.setStatus("current")
_CucsSwEthMonSrcEpIfType_Type = CucsSwPIoEpIfType
_CucsSwEthMonSrcEpIfType_Object = MibTableColumn
cucsSwEthMonSrcEpIfType = _CucsSwEthMonSrcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 8),
    _CucsSwEthMonSrcEpIfType_Type()
)
cucsSwEthMonSrcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpIfType.setStatus("current")
_CucsSwEthMonSrcEpLocale_Type = CucsSwMonSrcEpLocale
_CucsSwEthMonSrcEpLocale_Object = MibTableColumn
cucsSwEthMonSrcEpLocale = _CucsSwEthMonSrcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 9),
    _CucsSwEthMonSrcEpLocale_Type()
)
cucsSwEthMonSrcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpLocale.setStatus("current")
_CucsSwEthMonSrcEpMonTrafDir_Type = CucsFabricTrafficDirection
_CucsSwEthMonSrcEpMonTrafDir_Object = MibTableColumn
cucsSwEthMonSrcEpMonTrafDir = _CucsSwEthMonSrcEpMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 10),
    _CucsSwEthMonSrcEpMonTrafDir_Type()
)
cucsSwEthMonSrcEpMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpMonTrafDir.setStatus("current")
_CucsSwEthMonSrcEpName_Type = SnmpAdminString
_CucsSwEthMonSrcEpName_Object = MibTableColumn
cucsSwEthMonSrcEpName = _CucsSwEthMonSrcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 11),
    _CucsSwEthMonSrcEpName_Type()
)
cucsSwEthMonSrcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpName.setStatus("current")
_CucsSwEthMonSrcEpPeerDn_Type = SnmpAdminString
_CucsSwEthMonSrcEpPeerDn_Object = MibTableColumn
cucsSwEthMonSrcEpPeerDn = _CucsSwEthMonSrcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 12),
    _CucsSwEthMonSrcEpPeerDn_Type()
)
cucsSwEthMonSrcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpPeerDn.setStatus("current")
_CucsSwEthMonSrcEpPeerPortId_Type = Gauge32
_CucsSwEthMonSrcEpPeerPortId_Object = MibTableColumn
cucsSwEthMonSrcEpPeerPortId = _CucsSwEthMonSrcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 13),
    _CucsSwEthMonSrcEpPeerPortId_Type()
)
cucsSwEthMonSrcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpPeerPortId.setStatus("current")
_CucsSwEthMonSrcEpPeerSlotId_Type = Gauge32
_CucsSwEthMonSrcEpPeerSlotId_Object = MibTableColumn
cucsSwEthMonSrcEpPeerSlotId = _CucsSwEthMonSrcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 14),
    _CucsSwEthMonSrcEpPeerSlotId_Type()
)
cucsSwEthMonSrcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpPeerSlotId.setStatus("current")
_CucsSwEthMonSrcEpPortId_Type = Gauge32
_CucsSwEthMonSrcEpPortId_Object = MibTableColumn
cucsSwEthMonSrcEpPortId = _CucsSwEthMonSrcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 15),
    _CucsSwEthMonSrcEpPortId_Type()
)
cucsSwEthMonSrcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpPortId.setStatus("current")
_CucsSwEthMonSrcEpSlotId_Type = Gauge32
_CucsSwEthMonSrcEpSlotId_Object = MibTableColumn
cucsSwEthMonSrcEpSlotId = _CucsSwEthMonSrcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 16),
    _CucsSwEthMonSrcEpSlotId_Type()
)
cucsSwEthMonSrcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpSlotId.setStatus("current")
_CucsSwEthMonSrcEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthMonSrcEpSwitchId_Object = MibTableColumn
cucsSwEthMonSrcEpSwitchId = _CucsSwEthMonSrcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 17),
    _CucsSwEthMonSrcEpSwitchId_Type()
)
cucsSwEthMonSrcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpSwitchId.setStatus("current")
_CucsSwEthMonSrcEpTransport_Type = CucsSwEthMonSrcEpTransport
_CucsSwEthMonSrcEpTransport_Object = MibTableColumn
cucsSwEthMonSrcEpTransport = _CucsSwEthMonSrcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 18),
    _CucsSwEthMonSrcEpTransport_Type()
)
cucsSwEthMonSrcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpTransport.setStatus("current")
_CucsSwEthMonSrcEpType_Type = CucsNetworkConnectionType
_CucsSwEthMonSrcEpType_Object = MibTableColumn
cucsSwEthMonSrcEpType = _CucsSwEthMonSrcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 19),
    _CucsSwEthMonSrcEpType_Type()
)
cucsSwEthMonSrcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpType.setStatus("current")
_CucsSwEthMonSrcEpPeerChassisId_Type = Gauge32
_CucsSwEthMonSrcEpPeerChassisId_Object = MibTableColumn
cucsSwEthMonSrcEpPeerChassisId = _CucsSwEthMonSrcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 20),
    _CucsSwEthMonSrcEpPeerChassisId_Type()
)
cucsSwEthMonSrcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpPeerChassisId.setStatus("current")
_CucsSwEthMonSrcEpLc_Type = CucsSwPIoEpLc
_CucsSwEthMonSrcEpLc_Object = MibTableColumn
cucsSwEthMonSrcEpLc = _CucsSwEthMonSrcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 21),
    _CucsSwEthMonSrcEpLc_Type()
)
cucsSwEthMonSrcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpLc.setStatus("current")
_CucsSwEthMonSrcEpAggrPortId_Type = Gauge32
_CucsSwEthMonSrcEpAggrPortId_Object = MibTableColumn
cucsSwEthMonSrcEpAggrPortId = _CucsSwEthMonSrcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 22),
    _CucsSwEthMonSrcEpAggrPortId_Type()
)
cucsSwEthMonSrcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpAggrPortId.setStatus("current")
_CucsSwEthMonSrcEpPeerAggrPortId_Type = Gauge32
_CucsSwEthMonSrcEpPeerAggrPortId_Object = MibTableColumn
cucsSwEthMonSrcEpPeerAggrPortId = _CucsSwEthMonSrcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 23),
    _CucsSwEthMonSrcEpPeerAggrPortId_Type()
)
cucsSwEthMonSrcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpPeerAggrPortId.setStatus("current")
_CucsSwEthMonSrcEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwEthMonSrcEpAutoNegotiate_Object = MibTableColumn
cucsSwEthMonSrcEpAutoNegotiate = _CucsSwEthMonSrcEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 15, 1, 24),
    _CucsSwEthMonSrcEpAutoNegotiate_Type()
)
cucsSwEthMonSrcEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonSrcEpAutoNegotiate.setStatus("current")
_CucsSwEthTargetEpTable_Object = MibTable
cucsSwEthTargetEpTable = _CucsSwEthTargetEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16)
)
if mibBuilder.loadTexts:
    cucsSwEthTargetEpTable.setStatus("current")
_CucsSwEthTargetEpEntry_Object = MibTableRow
cucsSwEthTargetEpEntry = _CucsSwEthTargetEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1)
)
cucsSwEthTargetEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthTargetEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthTargetEpEntry.setStatus("current")
_CucsSwEthTargetEpInstanceId_Type = CucsManagedObjectId
_CucsSwEthTargetEpInstanceId_Object = MibTableColumn
cucsSwEthTargetEpInstanceId = _CucsSwEthTargetEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 1),
    _CucsSwEthTargetEpInstanceId_Type()
)
cucsSwEthTargetEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpInstanceId.setStatus("current")
_CucsSwEthTargetEpDn_Type = CucsManagedObjectDn
_CucsSwEthTargetEpDn_Object = MibTableColumn
cucsSwEthTargetEpDn = _CucsSwEthTargetEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 2),
    _CucsSwEthTargetEpDn_Type()
)
cucsSwEthTargetEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpDn.setStatus("current")
_CucsSwEthTargetEpRn_Type = SnmpAdminString
_CucsSwEthTargetEpRn_Object = MibTableColumn
cucsSwEthTargetEpRn = _CucsSwEthTargetEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 3),
    _CucsSwEthTargetEpRn_Type()
)
cucsSwEthTargetEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpRn.setStatus("current")
_CucsSwEthTargetEpAdminState_Type = CucsSwEthTargetEpAdminState
_CucsSwEthTargetEpAdminState_Object = MibTableColumn
cucsSwEthTargetEpAdminState = _CucsSwEthTargetEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 4),
    _CucsSwEthTargetEpAdminState_Type()
)
cucsSwEthTargetEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpAdminState.setStatus("current")
_CucsSwEthTargetEpChassisId_Type = Gauge32
_CucsSwEthTargetEpChassisId_Object = MibTableColumn
cucsSwEthTargetEpChassisId = _CucsSwEthTargetEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 5),
    _CucsSwEthTargetEpChassisId_Type()
)
cucsSwEthTargetEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpChassisId.setStatus("current")
_CucsSwEthTargetEpEpDn_Type = SnmpAdminString
_CucsSwEthTargetEpEpDn_Object = MibTableColumn
cucsSwEthTargetEpEpDn = _CucsSwEthTargetEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 6),
    _CucsSwEthTargetEpEpDn_Type()
)
cucsSwEthTargetEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpEpDn.setStatus("current")
_CucsSwEthTargetEpIfRole_Type = CucsNetworkPortRole
_CucsSwEthTargetEpIfRole_Object = MibTableColumn
cucsSwEthTargetEpIfRole = _CucsSwEthTargetEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 7),
    _CucsSwEthTargetEpIfRole_Type()
)
cucsSwEthTargetEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpIfRole.setStatus("current")
_CucsSwEthTargetEpIfType_Type = CucsFabricPIoEpIfType
_CucsSwEthTargetEpIfType_Object = MibTableColumn
cucsSwEthTargetEpIfType = _CucsSwEthTargetEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 8),
    _CucsSwEthTargetEpIfType_Type()
)
cucsSwEthTargetEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpIfType.setStatus("current")
_CucsSwEthTargetEpLicGP_Type = Unsigned64
_CucsSwEthTargetEpLicGP_Object = MibTableColumn
cucsSwEthTargetEpLicGP = _CucsSwEthTargetEpLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 9),
    _CucsSwEthTargetEpLicGP_Type()
)
cucsSwEthTargetEpLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpLicGP.setStatus("current")
_CucsSwEthTargetEpLicState_Type = CucsLicenseState
_CucsSwEthTargetEpLicState_Object = MibTableColumn
cucsSwEthTargetEpLicState = _CucsSwEthTargetEpLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 10),
    _CucsSwEthTargetEpLicState_Type()
)
cucsSwEthTargetEpLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpLicState.setStatus("current")
_CucsSwEthTargetEpLocale_Type = CucsFabricExternalEpLocale
_CucsSwEthTargetEpLocale_Object = MibTableColumn
cucsSwEthTargetEpLocale = _CucsSwEthTargetEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 11),
    _CucsSwEthTargetEpLocale_Type()
)
cucsSwEthTargetEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpLocale.setStatus("current")
_CucsSwEthTargetEpMacAddress_Type = MacAddress
_CucsSwEthTargetEpMacAddress_Object = MibTableColumn
cucsSwEthTargetEpMacAddress = _CucsSwEthTargetEpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 12),
    _CucsSwEthTargetEpMacAddress_Type()
)
cucsSwEthTargetEpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpMacAddress.setStatus("current")
_CucsSwEthTargetEpName_Type = SnmpAdminString
_CucsSwEthTargetEpName_Object = MibTableColumn
cucsSwEthTargetEpName = _CucsSwEthTargetEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 13),
    _CucsSwEthTargetEpName_Type()
)
cucsSwEthTargetEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpName.setStatus("current")
_CucsSwEthTargetEpPeerDn_Type = SnmpAdminString
_CucsSwEthTargetEpPeerDn_Object = MibTableColumn
cucsSwEthTargetEpPeerDn = _CucsSwEthTargetEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 14),
    _CucsSwEthTargetEpPeerDn_Type()
)
cucsSwEthTargetEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpPeerDn.setStatus("current")
_CucsSwEthTargetEpPeerPortId_Type = Gauge32
_CucsSwEthTargetEpPeerPortId_Object = MibTableColumn
cucsSwEthTargetEpPeerPortId = _CucsSwEthTargetEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 15),
    _CucsSwEthTargetEpPeerPortId_Type()
)
cucsSwEthTargetEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpPeerPortId.setStatus("current")
_CucsSwEthTargetEpPeerSlotId_Type = Gauge32
_CucsSwEthTargetEpPeerSlotId_Object = MibTableColumn
cucsSwEthTargetEpPeerSlotId = _CucsSwEthTargetEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 16),
    _CucsSwEthTargetEpPeerSlotId_Type()
)
cucsSwEthTargetEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpPeerSlotId.setStatus("current")
_CucsSwEthTargetEpPortId_Type = CucsFabricPIoEpPortId
_CucsSwEthTargetEpPortId_Object = MibTableColumn
cucsSwEthTargetEpPortId = _CucsSwEthTargetEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 17),
    _CucsSwEthTargetEpPortId_Type()
)
cucsSwEthTargetEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpPortId.setStatus("current")
_CucsSwEthTargetEpSlotId_Type = CucsFabricPIoEpSlotId
_CucsSwEthTargetEpSlotId_Object = MibTableColumn
cucsSwEthTargetEpSlotId = _CucsSwEthTargetEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 18),
    _CucsSwEthTargetEpSlotId_Type()
)
cucsSwEthTargetEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpSlotId.setStatus("current")
_CucsSwEthTargetEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthTargetEpSwitchId_Object = MibTableColumn
cucsSwEthTargetEpSwitchId = _CucsSwEthTargetEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 19),
    _CucsSwEthTargetEpSwitchId_Type()
)
cucsSwEthTargetEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpSwitchId.setStatus("current")
_CucsSwEthTargetEpTransport_Type = CucsSwEthTargetEpTransport
_CucsSwEthTargetEpTransport_Object = MibTableColumn
cucsSwEthTargetEpTransport = _CucsSwEthTargetEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 20),
    _CucsSwEthTargetEpTransport_Type()
)
cucsSwEthTargetEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpTransport.setStatus("current")
_CucsSwEthTargetEpType_Type = CucsSwTargetEpType
_CucsSwEthTargetEpType_Object = MibTableColumn
cucsSwEthTargetEpType = _CucsSwEthTargetEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 21),
    _CucsSwEthTargetEpType_Type()
)
cucsSwEthTargetEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpType.setStatus("current")
_CucsSwEthTargetEpPeerChassisId_Type = Gauge32
_CucsSwEthTargetEpPeerChassisId_Object = MibTableColumn
cucsSwEthTargetEpPeerChassisId = _CucsSwEthTargetEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 22),
    _CucsSwEthTargetEpPeerChassisId_Type()
)
cucsSwEthTargetEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpPeerChassisId.setStatus("current")
_CucsSwEthTargetEpFltAggr_Type = Unsigned64
_CucsSwEthTargetEpFltAggr_Object = MibTableColumn
cucsSwEthTargetEpFltAggr = _CucsSwEthTargetEpFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 23),
    _CucsSwEthTargetEpFltAggr_Type()
)
cucsSwEthTargetEpFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpFltAggr.setStatus("current")
_CucsSwEthTargetEpOperState_Type = CucsFabricPIoEpOperState
_CucsSwEthTargetEpOperState_Object = MibTableColumn
cucsSwEthTargetEpOperState = _CucsSwEthTargetEpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 24),
    _CucsSwEthTargetEpOperState_Type()
)
cucsSwEthTargetEpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpOperState.setStatus("current")
_CucsSwEthTargetEpOperStateReason_Type = SnmpAdminString
_CucsSwEthTargetEpOperStateReason_Object = MibTableColumn
cucsSwEthTargetEpOperStateReason = _CucsSwEthTargetEpOperStateReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 25),
    _CucsSwEthTargetEpOperStateReason_Type()
)
cucsSwEthTargetEpOperStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpOperStateReason.setStatus("current")
_CucsSwEthTargetEpWarnings_Type = CucsFabricWarnings
_CucsSwEthTargetEpWarnings_Object = MibTableColumn
cucsSwEthTargetEpWarnings = _CucsSwEthTargetEpWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 26),
    _CucsSwEthTargetEpWarnings_Type()
)
cucsSwEthTargetEpWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpWarnings.setStatus("current")
_CucsSwEthTargetEpAggrPortId_Type = Gauge32
_CucsSwEthTargetEpAggrPortId_Object = MibTableColumn
cucsSwEthTargetEpAggrPortId = _CucsSwEthTargetEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 27),
    _CucsSwEthTargetEpAggrPortId_Type()
)
cucsSwEthTargetEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpAggrPortId.setStatus("current")
_CucsSwEthTargetEpPeerAggrPortId_Type = Gauge32
_CucsSwEthTargetEpPeerAggrPortId_Object = MibTableColumn
cucsSwEthTargetEpPeerAggrPortId = _CucsSwEthTargetEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 28),
    _CucsSwEthTargetEpPeerAggrPortId_Type()
)
cucsSwEthTargetEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpPeerAggrPortId.setStatus("current")
_CucsSwEthTargetEpAutoNegotiate_Type = TruthValue
_CucsSwEthTargetEpAutoNegotiate_Object = MibTableColumn
cucsSwEthTargetEpAutoNegotiate = _CucsSwEthTargetEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 16, 1, 29),
    _CucsSwEthTargetEpAutoNegotiate_Type()
)
cucsSwEthTargetEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthTargetEpAutoNegotiate.setStatus("current")
_CucsSwFcEstcEpTable_Object = MibTable
cucsSwFcEstcEpTable = _CucsSwFcEstcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17)
)
if mibBuilder.loadTexts:
    cucsSwFcEstcEpTable.setStatus("current")
_CucsSwFcEstcEpEntry_Object = MibTableRow
cucsSwFcEstcEpEntry = _CucsSwFcEstcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1)
)
cucsSwFcEstcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcEstcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcEstcEpEntry.setStatus("current")
_CucsSwFcEstcEpInstanceId_Type = CucsManagedObjectId
_CucsSwFcEstcEpInstanceId_Object = MibTableColumn
cucsSwFcEstcEpInstanceId = _CucsSwFcEstcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 1),
    _CucsSwFcEstcEpInstanceId_Type()
)
cucsSwFcEstcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpInstanceId.setStatus("current")
_CucsSwFcEstcEpDn_Type = CucsManagedObjectDn
_CucsSwFcEstcEpDn_Object = MibTableColumn
cucsSwFcEstcEpDn = _CucsSwFcEstcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 2),
    _CucsSwFcEstcEpDn_Type()
)
cucsSwFcEstcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpDn.setStatus("current")
_CucsSwFcEstcEpRn_Type = SnmpAdminString
_CucsSwFcEstcEpRn_Object = MibTableColumn
cucsSwFcEstcEpRn = _CucsSwFcEstcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 3),
    _CucsSwFcEstcEpRn_Type()
)
cucsSwFcEstcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpRn.setStatus("current")
_CucsSwFcEstcEpAdminState_Type = CucsFabricAdminState
_CucsSwFcEstcEpAdminState_Object = MibTableColumn
cucsSwFcEstcEpAdminState = _CucsSwFcEstcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 4),
    _CucsSwFcEstcEpAdminState_Type()
)
cucsSwFcEstcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpAdminState.setStatus("current")
_CucsSwFcEstcEpChassisId_Type = Gauge32
_CucsSwFcEstcEpChassisId_Object = MibTableColumn
cucsSwFcEstcEpChassisId = _CucsSwFcEstcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 5),
    _CucsSwFcEstcEpChassisId_Type()
)
cucsSwFcEstcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpChassisId.setStatus("current")
_CucsSwFcEstcEpEpDn_Type = SnmpAdminString
_CucsSwFcEstcEpEpDn_Object = MibTableColumn
cucsSwFcEstcEpEpDn = _CucsSwFcEstcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 6),
    _CucsSwFcEstcEpEpDn_Type()
)
cucsSwFcEstcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpEpDn.setStatus("current")
_CucsSwFcEstcEpIfRole_Type = CucsNetworkPortRole
_CucsSwFcEstcEpIfRole_Object = MibTableColumn
cucsSwFcEstcEpIfRole = _CucsSwFcEstcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 7),
    _CucsSwFcEstcEpIfRole_Type()
)
cucsSwFcEstcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpIfRole.setStatus("current")
_CucsSwFcEstcEpIfType_Type = CucsSwPIoEpIfType
_CucsSwFcEstcEpIfType_Object = MibTableColumn
cucsSwFcEstcEpIfType = _CucsSwFcEstcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 8),
    _CucsSwFcEstcEpIfType_Type()
)
cucsSwFcEstcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpIfType.setStatus("current")
_CucsSwFcEstcEpLocale_Type = CucsSwEstcEpLocale
_CucsSwFcEstcEpLocale_Object = MibTableColumn
cucsSwFcEstcEpLocale = _CucsSwFcEstcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 9),
    _CucsSwFcEstcEpLocale_Type()
)
cucsSwFcEstcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpLocale.setStatus("current")
_CucsSwFcEstcEpName_Type = SnmpAdminString
_CucsSwFcEstcEpName_Object = MibTableColumn
cucsSwFcEstcEpName = _CucsSwFcEstcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 10),
    _CucsSwFcEstcEpName_Type()
)
cucsSwFcEstcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpName.setStatus("current")
_CucsSwFcEstcEpPeerDn_Type = SnmpAdminString
_CucsSwFcEstcEpPeerDn_Object = MibTableColumn
cucsSwFcEstcEpPeerDn = _CucsSwFcEstcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 11),
    _CucsSwFcEstcEpPeerDn_Type()
)
cucsSwFcEstcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpPeerDn.setStatus("current")
_CucsSwFcEstcEpPeerPortId_Type = Gauge32
_CucsSwFcEstcEpPeerPortId_Object = MibTableColumn
cucsSwFcEstcEpPeerPortId = _CucsSwFcEstcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 12),
    _CucsSwFcEstcEpPeerPortId_Type()
)
cucsSwFcEstcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpPeerPortId.setStatus("current")
_CucsSwFcEstcEpPeerSlotId_Type = Gauge32
_CucsSwFcEstcEpPeerSlotId_Object = MibTableColumn
cucsSwFcEstcEpPeerSlotId = _CucsSwFcEstcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 13),
    _CucsSwFcEstcEpPeerSlotId_Type()
)
cucsSwFcEstcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpPeerSlotId.setStatus("current")
_CucsSwFcEstcEpPortId_Type = Gauge32
_CucsSwFcEstcEpPortId_Object = MibTableColumn
cucsSwFcEstcEpPortId = _CucsSwFcEstcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 14),
    _CucsSwFcEstcEpPortId_Type()
)
cucsSwFcEstcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpPortId.setStatus("current")
_CucsSwFcEstcEpPortVsanId_Type = Gauge32
_CucsSwFcEstcEpPortVsanId_Object = MibTableColumn
cucsSwFcEstcEpPortVsanId = _CucsSwFcEstcEpPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 15),
    _CucsSwFcEstcEpPortVsanId_Type()
)
cucsSwFcEstcEpPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpPortVsanId.setStatus("current")
_CucsSwFcEstcEpSlotId_Type = Gauge32
_CucsSwFcEstcEpSlotId_Object = MibTableColumn
cucsSwFcEstcEpSlotId = _CucsSwFcEstcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 16),
    _CucsSwFcEstcEpSlotId_Type()
)
cucsSwFcEstcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpSlotId.setStatus("current")
_CucsSwFcEstcEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcEstcEpSwitchId_Object = MibTableColumn
cucsSwFcEstcEpSwitchId = _CucsSwFcEstcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 17),
    _CucsSwFcEstcEpSwitchId_Type()
)
cucsSwFcEstcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpSwitchId.setStatus("current")
_CucsSwFcEstcEpTransport_Type = CucsSwFcEstcEpTransport
_CucsSwFcEstcEpTransport_Object = MibTableColumn
cucsSwFcEstcEpTransport = _CucsSwFcEstcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 18),
    _CucsSwFcEstcEpTransport_Type()
)
cucsSwFcEstcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpTransport.setStatus("current")
_CucsSwFcEstcEpType_Type = CucsNetworkConnectionType
_CucsSwFcEstcEpType_Object = MibTableColumn
cucsSwFcEstcEpType = _CucsSwFcEstcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 19),
    _CucsSwFcEstcEpType_Type()
)
cucsSwFcEstcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpType.setStatus("current")
_CucsSwFcEstcEpPeerChassisId_Type = Gauge32
_CucsSwFcEstcEpPeerChassisId_Object = MibTableColumn
cucsSwFcEstcEpPeerChassisId = _CucsSwFcEstcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 20),
    _CucsSwFcEstcEpPeerChassisId_Type()
)
cucsSwFcEstcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpPeerChassisId.setStatus("current")
_CucsSwFcEstcEpLc_Type = CucsSwPIoEpLc
_CucsSwFcEstcEpLc_Object = MibTableColumn
cucsSwFcEstcEpLc = _CucsSwFcEstcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 21),
    _CucsSwFcEstcEpLc_Type()
)
cucsSwFcEstcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpLc.setStatus("current")
_CucsSwFcEstcEpFillPattern_Type = CucsFabricFillPattern
_CucsSwFcEstcEpFillPattern_Object = MibTableColumn
cucsSwFcEstcEpFillPattern = _CucsSwFcEstcEpFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 22),
    _CucsSwFcEstcEpFillPattern_Type()
)
cucsSwFcEstcEpFillPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpFillPattern.setStatus("current")
_CucsSwFcEstcEpAggrPortId_Type = Gauge32
_CucsSwFcEstcEpAggrPortId_Object = MibTableColumn
cucsSwFcEstcEpAggrPortId = _CucsSwFcEstcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 23),
    _CucsSwFcEstcEpAggrPortId_Type()
)
cucsSwFcEstcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpAggrPortId.setStatus("current")
_CucsSwFcEstcEpPeerAggrPortId_Type = Gauge32
_CucsSwFcEstcEpPeerAggrPortId_Object = MibTableColumn
cucsSwFcEstcEpPeerAggrPortId = _CucsSwFcEstcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 24),
    _CucsSwFcEstcEpPeerAggrPortId_Type()
)
cucsSwFcEstcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpPeerAggrPortId.setStatus("current")
_CucsSwFcEstcEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwFcEstcEpAutoNegotiate_Object = MibTableColumn
cucsSwFcEstcEpAutoNegotiate = _CucsSwFcEstcEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 17, 1, 25),
    _CucsSwFcEstcEpAutoNegotiate_Type()
)
cucsSwFcEstcEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcEstcEpAutoNegotiate.setStatus("current")
_CucsSwFcMonTable_Object = MibTable
cucsSwFcMonTable = _CucsSwFcMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18)
)
if mibBuilder.loadTexts:
    cucsSwFcMonTable.setStatus("current")
_CucsSwFcMonEntry_Object = MibTableRow
cucsSwFcMonEntry = _CucsSwFcMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1)
)
cucsSwFcMonEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcMonInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcMonEntry.setStatus("current")
_CucsSwFcMonInstanceId_Type = CucsManagedObjectId
_CucsSwFcMonInstanceId_Object = MibTableColumn
cucsSwFcMonInstanceId = _CucsSwFcMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 1),
    _CucsSwFcMonInstanceId_Type()
)
cucsSwFcMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcMonInstanceId.setStatus("current")
_CucsSwFcMonDn_Type = CucsManagedObjectDn
_CucsSwFcMonDn_Object = MibTableColumn
cucsSwFcMonDn = _CucsSwFcMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 2),
    _CucsSwFcMonDn_Type()
)
cucsSwFcMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDn.setStatus("current")
_CucsSwFcMonRn_Type = SnmpAdminString
_CucsSwFcMonRn_Object = MibTableColumn
cucsSwFcMonRn = _CucsSwFcMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 3),
    _CucsSwFcMonRn_Type()
)
cucsSwFcMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonRn.setStatus("current")
_CucsSwFcMonAdminState_Type = CucsSwMonAdminState
_CucsSwFcMonAdminState_Object = MibTableColumn
cucsSwFcMonAdminState = _CucsSwFcMonAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 4),
    _CucsSwFcMonAdminState_Type()
)
cucsSwFcMonAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonAdminState.setStatus("current")
_CucsSwFcMonFsmDescr_Type = SnmpAdminString
_CucsSwFcMonFsmDescr_Object = MibTableColumn
cucsSwFcMonFsmDescr = _CucsSwFcMonFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 5),
    _CucsSwFcMonFsmDescr_Type()
)
cucsSwFcMonFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmDescr.setStatus("current")
_CucsSwFcMonFsmPrev_Type = SnmpAdminString
_CucsSwFcMonFsmPrev_Object = MibTableColumn
cucsSwFcMonFsmPrev = _CucsSwFcMonFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 6),
    _CucsSwFcMonFsmPrev_Type()
)
cucsSwFcMonFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmPrev.setStatus("current")
_CucsSwFcMonFsmProgr_Type = Gauge32
_CucsSwFcMonFsmProgr_Object = MibTableColumn
cucsSwFcMonFsmProgr = _CucsSwFcMonFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 7),
    _CucsSwFcMonFsmProgr_Type()
)
cucsSwFcMonFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmProgr.setStatus("current")
_CucsSwFcMonFsmRmtInvErrCode_Type = Gauge32
_CucsSwFcMonFsmRmtInvErrCode_Object = MibTableColumn
cucsSwFcMonFsmRmtInvErrCode = _CucsSwFcMonFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 8),
    _CucsSwFcMonFsmRmtInvErrCode_Type()
)
cucsSwFcMonFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmRmtInvErrCode.setStatus("current")
_CucsSwFcMonFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwFcMonFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwFcMonFsmRmtInvErrDescr = _CucsSwFcMonFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 9),
    _CucsSwFcMonFsmRmtInvErrDescr_Type()
)
cucsSwFcMonFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmRmtInvErrDescr.setStatus("current")
_CucsSwFcMonFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwFcMonFsmRmtInvRslt_Object = MibTableColumn
cucsSwFcMonFsmRmtInvRslt = _CucsSwFcMonFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 10),
    _CucsSwFcMonFsmRmtInvRslt_Type()
)
cucsSwFcMonFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmRmtInvRslt.setStatus("current")
_CucsSwFcMonFsmStageDescr_Type = SnmpAdminString
_CucsSwFcMonFsmStageDescr_Object = MibTableColumn
cucsSwFcMonFsmStageDescr = _CucsSwFcMonFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 11),
    _CucsSwFcMonFsmStageDescr_Type()
)
cucsSwFcMonFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageDescr.setStatus("current")
_CucsSwFcMonFsmStamp_Type = DateAndTime
_CucsSwFcMonFsmStamp_Object = MibTableColumn
cucsSwFcMonFsmStamp = _CucsSwFcMonFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 12),
    _CucsSwFcMonFsmStamp_Type()
)
cucsSwFcMonFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStamp.setStatus("current")
_CucsSwFcMonFsmStatus_Type = SnmpAdminString
_CucsSwFcMonFsmStatus_Object = MibTableColumn
cucsSwFcMonFsmStatus = _CucsSwFcMonFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 13),
    _CucsSwFcMonFsmStatus_Type()
)
cucsSwFcMonFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStatus.setStatus("current")
_CucsSwFcMonFsmTry_Type = Gauge32
_CucsSwFcMonFsmTry_Object = MibTableColumn
cucsSwFcMonFsmTry = _CucsSwFcMonFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 14),
    _CucsSwFcMonFsmTry_Type()
)
cucsSwFcMonFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTry.setStatus("current")
_CucsSwFcMonLifeCycle_Type = CucsSwMonLifeCycle
_CucsSwFcMonLifeCycle_Object = MibTableColumn
cucsSwFcMonLifeCycle = _CucsSwFcMonLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 15),
    _CucsSwFcMonLifeCycle_Type()
)
cucsSwFcMonLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonLifeCycle.setStatus("current")
_CucsSwFcMonName_Type = SnmpAdminString
_CucsSwFcMonName_Object = MibTableColumn
cucsSwFcMonName = _CucsSwFcMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 16),
    _CucsSwFcMonName_Type()
)
cucsSwFcMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonName.setStatus("current")
_CucsSwFcMonSession_Type = Gauge32
_CucsSwFcMonSession_Object = MibTableColumn
cucsSwFcMonSession = _CucsSwFcMonSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 17),
    _CucsSwFcMonSession_Type()
)
cucsSwFcMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSession.setStatus("current")
_CucsSwFcMonSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcMonSwitchId_Object = MibTableColumn
cucsSwFcMonSwitchId = _CucsSwFcMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 18),
    _CucsSwFcMonSwitchId_Type()
)
cucsSwFcMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSwitchId.setStatus("current")
_CucsSwFcMonTransport_Type = CucsSwFcMonTransport
_CucsSwFcMonTransport_Object = MibTableColumn
cucsSwFcMonTransport = _CucsSwFcMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 19),
    _CucsSwFcMonTransport_Type()
)
cucsSwFcMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonTransport.setStatus("current")
_CucsSwFcMonType_Type = CucsSwFcMonType
_CucsSwFcMonType_Object = MibTableColumn
cucsSwFcMonType = _CucsSwFcMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 20),
    _CucsSwFcMonType_Type()
)
cucsSwFcMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonType.setStatus("current")
_CucsSwFcMonHasLastDest_Type = TruthValue
_CucsSwFcMonHasLastDest_Object = MibTableColumn
cucsSwFcMonHasLastDest = _CucsSwFcMonHasLastDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 21),
    _CucsSwFcMonHasLastDest_Type()
)
cucsSwFcMonHasLastDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonHasLastDest.setStatus("current")
_CucsSwFcMonPeerDn_Type = SnmpAdminString
_CucsSwFcMonPeerDn_Object = MibTableColumn
cucsSwFcMonPeerDn = _CucsSwFcMonPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 18, 1, 22),
    _CucsSwFcMonPeerDn_Type()
)
cucsSwFcMonPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonPeerDn.setStatus("current")
_CucsSwFcMonDestEpTable_Object = MibTable
cucsSwFcMonDestEpTable = _CucsSwFcMonDestEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19)
)
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpTable.setStatus("current")
_CucsSwFcMonDestEpEntry_Object = MibTableRow
cucsSwFcMonDestEpEntry = _CucsSwFcMonDestEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1)
)
cucsSwFcMonDestEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcMonDestEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpEntry.setStatus("current")
_CucsSwFcMonDestEpInstanceId_Type = CucsManagedObjectId
_CucsSwFcMonDestEpInstanceId_Object = MibTableColumn
cucsSwFcMonDestEpInstanceId = _CucsSwFcMonDestEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 1),
    _CucsSwFcMonDestEpInstanceId_Type()
)
cucsSwFcMonDestEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpInstanceId.setStatus("current")
_CucsSwFcMonDestEpDn_Type = CucsManagedObjectDn
_CucsSwFcMonDestEpDn_Object = MibTableColumn
cucsSwFcMonDestEpDn = _CucsSwFcMonDestEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 2),
    _CucsSwFcMonDestEpDn_Type()
)
cucsSwFcMonDestEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpDn.setStatus("current")
_CucsSwFcMonDestEpRn_Type = SnmpAdminString
_CucsSwFcMonDestEpRn_Object = MibTableColumn
cucsSwFcMonDestEpRn = _CucsSwFcMonDestEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 3),
    _CucsSwFcMonDestEpRn_Type()
)
cucsSwFcMonDestEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpRn.setStatus("current")
_CucsSwFcMonDestEpAdminState_Type = CucsFabricAdminState
_CucsSwFcMonDestEpAdminState_Object = MibTableColumn
cucsSwFcMonDestEpAdminState = _CucsSwFcMonDestEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 4),
    _CucsSwFcMonDestEpAdminState_Type()
)
cucsSwFcMonDestEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpAdminState.setStatus("current")
_CucsSwFcMonDestEpChassisId_Type = Gauge32
_CucsSwFcMonDestEpChassisId_Object = MibTableColumn
cucsSwFcMonDestEpChassisId = _CucsSwFcMonDestEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 5),
    _CucsSwFcMonDestEpChassisId_Type()
)
cucsSwFcMonDestEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpChassisId.setStatus("current")
_CucsSwFcMonDestEpEpDn_Type = SnmpAdminString
_CucsSwFcMonDestEpEpDn_Object = MibTableColumn
cucsSwFcMonDestEpEpDn = _CucsSwFcMonDestEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 6),
    _CucsSwFcMonDestEpEpDn_Type()
)
cucsSwFcMonDestEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpEpDn.setStatus("current")
_CucsSwFcMonDestEpIfRole_Type = CucsNetworkPortRole
_CucsSwFcMonDestEpIfRole_Object = MibTableColumn
cucsSwFcMonDestEpIfRole = _CucsSwFcMonDestEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 7),
    _CucsSwFcMonDestEpIfRole_Type()
)
cucsSwFcMonDestEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpIfRole.setStatus("current")
_CucsSwFcMonDestEpIfType_Type = CucsSwPIoEpIfType
_CucsSwFcMonDestEpIfType_Object = MibTableColumn
cucsSwFcMonDestEpIfType = _CucsSwFcMonDestEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 8),
    _CucsSwFcMonDestEpIfType_Type()
)
cucsSwFcMonDestEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpIfType.setStatus("current")
_CucsSwFcMonDestEpLocale_Type = CucsNetworkLocale
_CucsSwFcMonDestEpLocale_Object = MibTableColumn
cucsSwFcMonDestEpLocale = _CucsSwFcMonDestEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 9),
    _CucsSwFcMonDestEpLocale_Type()
)
cucsSwFcMonDestEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpLocale.setStatus("current")
_CucsSwFcMonDestEpName_Type = SnmpAdminString
_CucsSwFcMonDestEpName_Object = MibTableColumn
cucsSwFcMonDestEpName = _CucsSwFcMonDestEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 10),
    _CucsSwFcMonDestEpName_Type()
)
cucsSwFcMonDestEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpName.setStatus("current")
_CucsSwFcMonDestEpPeerDn_Type = SnmpAdminString
_CucsSwFcMonDestEpPeerDn_Object = MibTableColumn
cucsSwFcMonDestEpPeerDn = _CucsSwFcMonDestEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 11),
    _CucsSwFcMonDestEpPeerDn_Type()
)
cucsSwFcMonDestEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpPeerDn.setStatus("current")
_CucsSwFcMonDestEpPeerPortId_Type = Gauge32
_CucsSwFcMonDestEpPeerPortId_Object = MibTableColumn
cucsSwFcMonDestEpPeerPortId = _CucsSwFcMonDestEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 12),
    _CucsSwFcMonDestEpPeerPortId_Type()
)
cucsSwFcMonDestEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpPeerPortId.setStatus("current")
_CucsSwFcMonDestEpPeerSlotId_Type = Gauge32
_CucsSwFcMonDestEpPeerSlotId_Object = MibTableColumn
cucsSwFcMonDestEpPeerSlotId = _CucsSwFcMonDestEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 13),
    _CucsSwFcMonDestEpPeerSlotId_Type()
)
cucsSwFcMonDestEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpPeerSlotId.setStatus("current")
_CucsSwFcMonDestEpPortId_Type = Gauge32
_CucsSwFcMonDestEpPortId_Object = MibTableColumn
cucsSwFcMonDestEpPortId = _CucsSwFcMonDestEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 14),
    _CucsSwFcMonDestEpPortId_Type()
)
cucsSwFcMonDestEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpPortId.setStatus("current")
_CucsSwFcMonDestEpSlotId_Type = Gauge32
_CucsSwFcMonDestEpSlotId_Object = MibTableColumn
cucsSwFcMonDestEpSlotId = _CucsSwFcMonDestEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 15),
    _CucsSwFcMonDestEpSlotId_Type()
)
cucsSwFcMonDestEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpSlotId.setStatus("current")
_CucsSwFcMonDestEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcMonDestEpSwitchId_Object = MibTableColumn
cucsSwFcMonDestEpSwitchId = _CucsSwFcMonDestEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 16),
    _CucsSwFcMonDestEpSwitchId_Type()
)
cucsSwFcMonDestEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpSwitchId.setStatus("current")
_CucsSwFcMonDestEpTransport_Type = CucsSwFcMonDestEpTransport
_CucsSwFcMonDestEpTransport_Object = MibTableColumn
cucsSwFcMonDestEpTransport = _CucsSwFcMonDestEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 17),
    _CucsSwFcMonDestEpTransport_Type()
)
cucsSwFcMonDestEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpTransport.setStatus("current")
_CucsSwFcMonDestEpType_Type = CucsNetworkConnectionType
_CucsSwFcMonDestEpType_Object = MibTableColumn
cucsSwFcMonDestEpType = _CucsSwFcMonDestEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 18),
    _CucsSwFcMonDestEpType_Type()
)
cucsSwFcMonDestEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpType.setStatus("current")
_CucsSwFcMonDestEpPeerChassisId_Type = Gauge32
_CucsSwFcMonDestEpPeerChassisId_Object = MibTableColumn
cucsSwFcMonDestEpPeerChassisId = _CucsSwFcMonDestEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 19),
    _CucsSwFcMonDestEpPeerChassisId_Type()
)
cucsSwFcMonDestEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpPeerChassisId.setStatus("current")
_CucsSwFcMonDestEpLc_Type = CucsSwPIoEpLc
_CucsSwFcMonDestEpLc_Object = MibTableColumn
cucsSwFcMonDestEpLc = _CucsSwFcMonDestEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 20),
    _CucsSwFcMonDestEpLc_Type()
)
cucsSwFcMonDestEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpLc.setStatus("current")
_CucsSwFcMonDestEpAdminSpeed_Type = CucsPortSpeed
_CucsSwFcMonDestEpAdminSpeed_Object = MibTableColumn
cucsSwFcMonDestEpAdminSpeed = _CucsSwFcMonDestEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 21),
    _CucsSwFcMonDestEpAdminSpeed_Type()
)
cucsSwFcMonDestEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpAdminSpeed.setStatus("current")
_CucsSwFcMonDestEpAggrPortId_Type = Gauge32
_CucsSwFcMonDestEpAggrPortId_Object = MibTableColumn
cucsSwFcMonDestEpAggrPortId = _CucsSwFcMonDestEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 22),
    _CucsSwFcMonDestEpAggrPortId_Type()
)
cucsSwFcMonDestEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpAggrPortId.setStatus("current")
_CucsSwFcMonDestEpPeerAggrPortId_Type = Gauge32
_CucsSwFcMonDestEpPeerAggrPortId_Object = MibTableColumn
cucsSwFcMonDestEpPeerAggrPortId = _CucsSwFcMonDestEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 23),
    _CucsSwFcMonDestEpPeerAggrPortId_Type()
)
cucsSwFcMonDestEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpPeerAggrPortId.setStatus("current")
_CucsSwFcMonDestEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwFcMonDestEpAutoNegotiate_Object = MibTableColumn
cucsSwFcMonDestEpAutoNegotiate = _CucsSwFcMonDestEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 19, 1, 24),
    _CucsSwFcMonDestEpAutoNegotiate_Type()
)
cucsSwFcMonDestEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonDestEpAutoNegotiate.setStatus("current")
_CucsSwFcMonFsmTaskTable_Object = MibTable
cucsSwFcMonFsmTaskTable = _CucsSwFcMonFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20)
)
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskTable.setStatus("current")
_CucsSwFcMonFsmTaskEntry_Object = MibTableRow
cucsSwFcMonFsmTaskEntry = _CucsSwFcMonFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20, 1)
)
cucsSwFcMonFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcMonFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskEntry.setStatus("current")
_CucsSwFcMonFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwFcMonFsmTaskInstanceId_Object = MibTableColumn
cucsSwFcMonFsmTaskInstanceId = _CucsSwFcMonFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20, 1, 1),
    _CucsSwFcMonFsmTaskInstanceId_Type()
)
cucsSwFcMonFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskInstanceId.setStatus("current")
_CucsSwFcMonFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwFcMonFsmTaskDn_Object = MibTableColumn
cucsSwFcMonFsmTaskDn = _CucsSwFcMonFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20, 1, 2),
    _CucsSwFcMonFsmTaskDn_Type()
)
cucsSwFcMonFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskDn.setStatus("current")
_CucsSwFcMonFsmTaskRn_Type = SnmpAdminString
_CucsSwFcMonFsmTaskRn_Object = MibTableColumn
cucsSwFcMonFsmTaskRn = _CucsSwFcMonFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20, 1, 3),
    _CucsSwFcMonFsmTaskRn_Type()
)
cucsSwFcMonFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskRn.setStatus("current")
_CucsSwFcMonFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwFcMonFsmTaskCompletion_Object = MibTableColumn
cucsSwFcMonFsmTaskCompletion = _CucsSwFcMonFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20, 1, 4),
    _CucsSwFcMonFsmTaskCompletion_Type()
)
cucsSwFcMonFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskCompletion.setStatus("current")
_CucsSwFcMonFsmTaskFlags_Type = CucsFsmFlags
_CucsSwFcMonFsmTaskFlags_Object = MibTableColumn
cucsSwFcMonFsmTaskFlags = _CucsSwFcMonFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20, 1, 5),
    _CucsSwFcMonFsmTaskFlags_Type()
)
cucsSwFcMonFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskFlags.setStatus("current")
_CucsSwFcMonFsmTaskItem_Type = CucsSwFcMonFsmTaskItem
_CucsSwFcMonFsmTaskItem_Object = MibTableColumn
cucsSwFcMonFsmTaskItem = _CucsSwFcMonFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20, 1, 6),
    _CucsSwFcMonFsmTaskItem_Type()
)
cucsSwFcMonFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskItem.setStatus("current")
_CucsSwFcMonFsmTaskSeqId_Type = Gauge32
_CucsSwFcMonFsmTaskSeqId_Object = MibTableColumn
cucsSwFcMonFsmTaskSeqId = _CucsSwFcMonFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 20, 1, 7),
    _CucsSwFcMonFsmTaskSeqId_Type()
)
cucsSwFcMonFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTaskSeqId.setStatus("current")
_CucsSwFcMonSrcEpTable_Object = MibTable
cucsSwFcMonSrcEpTable = _CucsSwFcMonSrcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21)
)
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpTable.setStatus("current")
_CucsSwFcMonSrcEpEntry_Object = MibTableRow
cucsSwFcMonSrcEpEntry = _CucsSwFcMonSrcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1)
)
cucsSwFcMonSrcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcMonSrcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpEntry.setStatus("current")
_CucsSwFcMonSrcEpInstanceId_Type = CucsManagedObjectId
_CucsSwFcMonSrcEpInstanceId_Object = MibTableColumn
cucsSwFcMonSrcEpInstanceId = _CucsSwFcMonSrcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 1),
    _CucsSwFcMonSrcEpInstanceId_Type()
)
cucsSwFcMonSrcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpInstanceId.setStatus("current")
_CucsSwFcMonSrcEpDn_Type = CucsManagedObjectDn
_CucsSwFcMonSrcEpDn_Object = MibTableColumn
cucsSwFcMonSrcEpDn = _CucsSwFcMonSrcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 2),
    _CucsSwFcMonSrcEpDn_Type()
)
cucsSwFcMonSrcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpDn.setStatus("current")
_CucsSwFcMonSrcEpRn_Type = SnmpAdminString
_CucsSwFcMonSrcEpRn_Object = MibTableColumn
cucsSwFcMonSrcEpRn = _CucsSwFcMonSrcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 3),
    _CucsSwFcMonSrcEpRn_Type()
)
cucsSwFcMonSrcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpRn.setStatus("current")
_CucsSwFcMonSrcEpAdminState_Type = CucsFabricAdminState
_CucsSwFcMonSrcEpAdminState_Object = MibTableColumn
cucsSwFcMonSrcEpAdminState = _CucsSwFcMonSrcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 4),
    _CucsSwFcMonSrcEpAdminState_Type()
)
cucsSwFcMonSrcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpAdminState.setStatus("current")
_CucsSwFcMonSrcEpChassisId_Type = Gauge32
_CucsSwFcMonSrcEpChassisId_Object = MibTableColumn
cucsSwFcMonSrcEpChassisId = _CucsSwFcMonSrcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 5),
    _CucsSwFcMonSrcEpChassisId_Type()
)
cucsSwFcMonSrcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpChassisId.setStatus("current")
_CucsSwFcMonSrcEpEpDn_Type = SnmpAdminString
_CucsSwFcMonSrcEpEpDn_Object = MibTableColumn
cucsSwFcMonSrcEpEpDn = _CucsSwFcMonSrcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 6),
    _CucsSwFcMonSrcEpEpDn_Type()
)
cucsSwFcMonSrcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpEpDn.setStatus("current")
_CucsSwFcMonSrcEpIfRole_Type = CucsNetworkPortRole
_CucsSwFcMonSrcEpIfRole_Object = MibTableColumn
cucsSwFcMonSrcEpIfRole = _CucsSwFcMonSrcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 7),
    _CucsSwFcMonSrcEpIfRole_Type()
)
cucsSwFcMonSrcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpIfRole.setStatus("current")
_CucsSwFcMonSrcEpIfType_Type = CucsSwPIoEpIfType
_CucsSwFcMonSrcEpIfType_Object = MibTableColumn
cucsSwFcMonSrcEpIfType = _CucsSwFcMonSrcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 8),
    _CucsSwFcMonSrcEpIfType_Type()
)
cucsSwFcMonSrcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpIfType.setStatus("current")
_CucsSwFcMonSrcEpLocale_Type = CucsSwMonSrcEpLocale
_CucsSwFcMonSrcEpLocale_Object = MibTableColumn
cucsSwFcMonSrcEpLocale = _CucsSwFcMonSrcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 9),
    _CucsSwFcMonSrcEpLocale_Type()
)
cucsSwFcMonSrcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpLocale.setStatus("current")
_CucsSwFcMonSrcEpMonTrafDir_Type = CucsFabricTrafficDirection
_CucsSwFcMonSrcEpMonTrafDir_Object = MibTableColumn
cucsSwFcMonSrcEpMonTrafDir = _CucsSwFcMonSrcEpMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 10),
    _CucsSwFcMonSrcEpMonTrafDir_Type()
)
cucsSwFcMonSrcEpMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpMonTrafDir.setStatus("current")
_CucsSwFcMonSrcEpName_Type = SnmpAdminString
_CucsSwFcMonSrcEpName_Object = MibTableColumn
cucsSwFcMonSrcEpName = _CucsSwFcMonSrcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 11),
    _CucsSwFcMonSrcEpName_Type()
)
cucsSwFcMonSrcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpName.setStatus("current")
_CucsSwFcMonSrcEpPeerDn_Type = SnmpAdminString
_CucsSwFcMonSrcEpPeerDn_Object = MibTableColumn
cucsSwFcMonSrcEpPeerDn = _CucsSwFcMonSrcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 12),
    _CucsSwFcMonSrcEpPeerDn_Type()
)
cucsSwFcMonSrcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpPeerDn.setStatus("current")
_CucsSwFcMonSrcEpPeerPortId_Type = Gauge32
_CucsSwFcMonSrcEpPeerPortId_Object = MibTableColumn
cucsSwFcMonSrcEpPeerPortId = _CucsSwFcMonSrcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 13),
    _CucsSwFcMonSrcEpPeerPortId_Type()
)
cucsSwFcMonSrcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpPeerPortId.setStatus("current")
_CucsSwFcMonSrcEpPeerSlotId_Type = Gauge32
_CucsSwFcMonSrcEpPeerSlotId_Object = MibTableColumn
cucsSwFcMonSrcEpPeerSlotId = _CucsSwFcMonSrcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 14),
    _CucsSwFcMonSrcEpPeerSlotId_Type()
)
cucsSwFcMonSrcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpPeerSlotId.setStatus("current")
_CucsSwFcMonSrcEpPortId_Type = Gauge32
_CucsSwFcMonSrcEpPortId_Object = MibTableColumn
cucsSwFcMonSrcEpPortId = _CucsSwFcMonSrcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 15),
    _CucsSwFcMonSrcEpPortId_Type()
)
cucsSwFcMonSrcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpPortId.setStatus("current")
_CucsSwFcMonSrcEpSlotId_Type = Gauge32
_CucsSwFcMonSrcEpSlotId_Object = MibTableColumn
cucsSwFcMonSrcEpSlotId = _CucsSwFcMonSrcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 16),
    _CucsSwFcMonSrcEpSlotId_Type()
)
cucsSwFcMonSrcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpSlotId.setStatus("current")
_CucsSwFcMonSrcEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcMonSrcEpSwitchId_Object = MibTableColumn
cucsSwFcMonSrcEpSwitchId = _CucsSwFcMonSrcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 17),
    _CucsSwFcMonSrcEpSwitchId_Type()
)
cucsSwFcMonSrcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpSwitchId.setStatus("current")
_CucsSwFcMonSrcEpTransport_Type = CucsSwFcMonSrcEpTransport
_CucsSwFcMonSrcEpTransport_Object = MibTableColumn
cucsSwFcMonSrcEpTransport = _CucsSwFcMonSrcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 18),
    _CucsSwFcMonSrcEpTransport_Type()
)
cucsSwFcMonSrcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpTransport.setStatus("current")
_CucsSwFcMonSrcEpType_Type = CucsNetworkConnectionType
_CucsSwFcMonSrcEpType_Object = MibTableColumn
cucsSwFcMonSrcEpType = _CucsSwFcMonSrcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 19),
    _CucsSwFcMonSrcEpType_Type()
)
cucsSwFcMonSrcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpType.setStatus("current")
_CucsSwFcMonSrcEpPeerChassisId_Type = Gauge32
_CucsSwFcMonSrcEpPeerChassisId_Object = MibTableColumn
cucsSwFcMonSrcEpPeerChassisId = _CucsSwFcMonSrcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 20),
    _CucsSwFcMonSrcEpPeerChassisId_Type()
)
cucsSwFcMonSrcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpPeerChassisId.setStatus("current")
_CucsSwFcMonSrcEpLc_Type = CucsSwPIoEpLc
_CucsSwFcMonSrcEpLc_Object = MibTableColumn
cucsSwFcMonSrcEpLc = _CucsSwFcMonSrcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 21),
    _CucsSwFcMonSrcEpLc_Type()
)
cucsSwFcMonSrcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpLc.setStatus("current")
_CucsSwFcMonSrcEpAggrPortId_Type = Gauge32
_CucsSwFcMonSrcEpAggrPortId_Object = MibTableColumn
cucsSwFcMonSrcEpAggrPortId = _CucsSwFcMonSrcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 22),
    _CucsSwFcMonSrcEpAggrPortId_Type()
)
cucsSwFcMonSrcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpAggrPortId.setStatus("current")
_CucsSwFcMonSrcEpPeerAggrPortId_Type = Gauge32
_CucsSwFcMonSrcEpPeerAggrPortId_Object = MibTableColumn
cucsSwFcMonSrcEpPeerAggrPortId = _CucsSwFcMonSrcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 23),
    _CucsSwFcMonSrcEpPeerAggrPortId_Type()
)
cucsSwFcMonSrcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpPeerAggrPortId.setStatus("current")
_CucsSwFcMonSrcEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwFcMonSrcEpAutoNegotiate_Object = MibTableColumn
cucsSwFcMonSrcEpAutoNegotiate = _CucsSwFcMonSrcEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 21, 1, 24),
    _CucsSwFcMonSrcEpAutoNegotiate_Type()
)
cucsSwFcMonSrcEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonSrcEpAutoNegotiate.setStatus("current")
_CucsSwFcSanBorderTable_Object = MibTable
cucsSwFcSanBorderTable = _CucsSwFcSanBorderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22)
)
if mibBuilder.loadTexts:
    cucsSwFcSanBorderTable.setStatus("current")
_CucsSwFcSanBorderEntry_Object = MibTableRow
cucsSwFcSanBorderEntry = _CucsSwFcSanBorderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1)
)
cucsSwFcSanBorderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcSanBorderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcSanBorderEntry.setStatus("current")
_CucsSwFcSanBorderInstanceId_Type = CucsManagedObjectId
_CucsSwFcSanBorderInstanceId_Object = MibTableColumn
cucsSwFcSanBorderInstanceId = _CucsSwFcSanBorderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 1),
    _CucsSwFcSanBorderInstanceId_Type()
)
cucsSwFcSanBorderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderInstanceId.setStatus("current")
_CucsSwFcSanBorderDn_Type = CucsManagedObjectDn
_CucsSwFcSanBorderDn_Object = MibTableColumn
cucsSwFcSanBorderDn = _CucsSwFcSanBorderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 2),
    _CucsSwFcSanBorderDn_Type()
)
cucsSwFcSanBorderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderDn.setStatus("current")
_CucsSwFcSanBorderRn_Type = SnmpAdminString
_CucsSwFcSanBorderRn_Object = MibTableColumn
cucsSwFcSanBorderRn = _CucsSwFcSanBorderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 3),
    _CucsSwFcSanBorderRn_Type()
)
cucsSwFcSanBorderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderRn.setStatus("current")
_CucsSwFcSanBorderFsmDescr_Type = SnmpAdminString
_CucsSwFcSanBorderFsmDescr_Object = MibTableColumn
cucsSwFcSanBorderFsmDescr = _CucsSwFcSanBorderFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 4),
    _CucsSwFcSanBorderFsmDescr_Type()
)
cucsSwFcSanBorderFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmDescr.setStatus("current")
_CucsSwFcSanBorderFsmPrev_Type = SnmpAdminString
_CucsSwFcSanBorderFsmPrev_Object = MibTableColumn
cucsSwFcSanBorderFsmPrev = _CucsSwFcSanBorderFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 5),
    _CucsSwFcSanBorderFsmPrev_Type()
)
cucsSwFcSanBorderFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmPrev.setStatus("current")
_CucsSwFcSanBorderFsmProgr_Type = Gauge32
_CucsSwFcSanBorderFsmProgr_Object = MibTableColumn
cucsSwFcSanBorderFsmProgr = _CucsSwFcSanBorderFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 6),
    _CucsSwFcSanBorderFsmProgr_Type()
)
cucsSwFcSanBorderFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmProgr.setStatus("current")
_CucsSwFcSanBorderFsmRmtInvErrCode_Type = Gauge32
_CucsSwFcSanBorderFsmRmtInvErrCode_Object = MibTableColumn
cucsSwFcSanBorderFsmRmtInvErrCode = _CucsSwFcSanBorderFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 7),
    _CucsSwFcSanBorderFsmRmtInvErrCode_Type()
)
cucsSwFcSanBorderFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmRmtInvErrCode.setStatus("current")
_CucsSwFcSanBorderFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwFcSanBorderFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwFcSanBorderFsmRmtInvErrDescr = _CucsSwFcSanBorderFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 8),
    _CucsSwFcSanBorderFsmRmtInvErrDescr_Type()
)
cucsSwFcSanBorderFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmRmtInvErrDescr.setStatus("current")
_CucsSwFcSanBorderFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwFcSanBorderFsmRmtInvRslt_Object = MibTableColumn
cucsSwFcSanBorderFsmRmtInvRslt = _CucsSwFcSanBorderFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 9),
    _CucsSwFcSanBorderFsmRmtInvRslt_Type()
)
cucsSwFcSanBorderFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmRmtInvRslt.setStatus("current")
_CucsSwFcSanBorderFsmStageDescr_Type = SnmpAdminString
_CucsSwFcSanBorderFsmStageDescr_Object = MibTableColumn
cucsSwFcSanBorderFsmStageDescr = _CucsSwFcSanBorderFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 10),
    _CucsSwFcSanBorderFsmStageDescr_Type()
)
cucsSwFcSanBorderFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageDescr.setStatus("current")
_CucsSwFcSanBorderFsmStamp_Type = DateAndTime
_CucsSwFcSanBorderFsmStamp_Object = MibTableColumn
cucsSwFcSanBorderFsmStamp = _CucsSwFcSanBorderFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 11),
    _CucsSwFcSanBorderFsmStamp_Type()
)
cucsSwFcSanBorderFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStamp.setStatus("current")
_CucsSwFcSanBorderFsmStatus_Type = SnmpAdminString
_CucsSwFcSanBorderFsmStatus_Object = MibTableColumn
cucsSwFcSanBorderFsmStatus = _CucsSwFcSanBorderFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 12),
    _CucsSwFcSanBorderFsmStatus_Type()
)
cucsSwFcSanBorderFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStatus.setStatus("current")
_CucsSwFcSanBorderFsmTry_Type = Gauge32
_CucsSwFcSanBorderFsmTry_Object = MibTableColumn
cucsSwFcSanBorderFsmTry = _CucsSwFcSanBorderFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 13),
    _CucsSwFcSanBorderFsmTry_Type()
)
cucsSwFcSanBorderFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTry.setStatus("current")
_CucsSwFcSanBorderLocale_Type = CucsSwBorderDomainLocale
_CucsSwFcSanBorderLocale_Object = MibTableColumn
cucsSwFcSanBorderLocale = _CucsSwFcSanBorderLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 14),
    _CucsSwFcSanBorderLocale_Type()
)
cucsSwFcSanBorderLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderLocale.setStatus("current")
_CucsSwFcSanBorderName_Type = SnmpAdminString
_CucsSwFcSanBorderName_Object = MibTableColumn
cucsSwFcSanBorderName = _CucsSwFcSanBorderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 15),
    _CucsSwFcSanBorderName_Type()
)
cucsSwFcSanBorderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderName.setStatus("current")
_CucsSwFcSanBorderSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcSanBorderSwitchId_Object = MibTableColumn
cucsSwFcSanBorderSwitchId = _CucsSwFcSanBorderSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 16),
    _CucsSwFcSanBorderSwitchId_Type()
)
cucsSwFcSanBorderSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderSwitchId.setStatus("current")
_CucsSwFcSanBorderTransport_Type = CucsSwFcSanBorderTransport
_CucsSwFcSanBorderTransport_Object = MibTableColumn
cucsSwFcSanBorderTransport = _CucsSwFcSanBorderTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 17),
    _CucsSwFcSanBorderTransport_Type()
)
cucsSwFcSanBorderTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderTransport.setStatus("current")
_CucsSwFcSanBorderType_Type = CucsSwSanBorderType
_CucsSwFcSanBorderType_Object = MibTableColumn
cucsSwFcSanBorderType = _CucsSwFcSanBorderType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 18),
    _CucsSwFcSanBorderType_Type()
)
cucsSwFcSanBorderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderType.setStatus("current")
_CucsSwFcSanBorderUplinkTrunking_Type = CucsSwFcSanBorderUplinkTrunking
_CucsSwFcSanBorderUplinkTrunking_Object = MibTableColumn
cucsSwFcSanBorderUplinkTrunking = _CucsSwFcSanBorderUplinkTrunking_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 22, 1, 19),
    _CucsSwFcSanBorderUplinkTrunking_Type()
)
cucsSwFcSanBorderUplinkTrunking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderUplinkTrunking.setStatus("current")
_CucsSwFcSanBorderFsmTaskTable_Object = MibTable
cucsSwFcSanBorderFsmTaskTable = _CucsSwFcSanBorderFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23)
)
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskTable.setStatus("current")
_CucsSwFcSanBorderFsmTaskEntry_Object = MibTableRow
cucsSwFcSanBorderFsmTaskEntry = _CucsSwFcSanBorderFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23, 1)
)
cucsSwFcSanBorderFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcSanBorderFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskEntry.setStatus("current")
_CucsSwFcSanBorderFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwFcSanBorderFsmTaskInstanceId_Object = MibTableColumn
cucsSwFcSanBorderFsmTaskInstanceId = _CucsSwFcSanBorderFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23, 1, 1),
    _CucsSwFcSanBorderFsmTaskInstanceId_Type()
)
cucsSwFcSanBorderFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskInstanceId.setStatus("current")
_CucsSwFcSanBorderFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwFcSanBorderFsmTaskDn_Object = MibTableColumn
cucsSwFcSanBorderFsmTaskDn = _CucsSwFcSanBorderFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23, 1, 2),
    _CucsSwFcSanBorderFsmTaskDn_Type()
)
cucsSwFcSanBorderFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskDn.setStatus("current")
_CucsSwFcSanBorderFsmTaskRn_Type = SnmpAdminString
_CucsSwFcSanBorderFsmTaskRn_Object = MibTableColumn
cucsSwFcSanBorderFsmTaskRn = _CucsSwFcSanBorderFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23, 1, 3),
    _CucsSwFcSanBorderFsmTaskRn_Type()
)
cucsSwFcSanBorderFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskRn.setStatus("current")
_CucsSwFcSanBorderFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwFcSanBorderFsmTaskCompletion_Object = MibTableColumn
cucsSwFcSanBorderFsmTaskCompletion = _CucsSwFcSanBorderFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23, 1, 4),
    _CucsSwFcSanBorderFsmTaskCompletion_Type()
)
cucsSwFcSanBorderFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskCompletion.setStatus("current")
_CucsSwFcSanBorderFsmTaskFlags_Type = CucsFsmFlags
_CucsSwFcSanBorderFsmTaskFlags_Object = MibTableColumn
cucsSwFcSanBorderFsmTaskFlags = _CucsSwFcSanBorderFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23, 1, 5),
    _CucsSwFcSanBorderFsmTaskFlags_Type()
)
cucsSwFcSanBorderFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskFlags.setStatus("current")
_CucsSwFcSanBorderFsmTaskItem_Type = CucsSwFcSanBorderFsmTaskItem
_CucsSwFcSanBorderFsmTaskItem_Object = MibTableColumn
cucsSwFcSanBorderFsmTaskItem = _CucsSwFcSanBorderFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23, 1, 6),
    _CucsSwFcSanBorderFsmTaskItem_Type()
)
cucsSwFcSanBorderFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskItem.setStatus("current")
_CucsSwFcSanBorderFsmTaskSeqId_Type = Gauge32
_CucsSwFcSanBorderFsmTaskSeqId_Object = MibTableColumn
cucsSwFcSanBorderFsmTaskSeqId = _CucsSwFcSanBorderFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 23, 1, 7),
    _CucsSwFcSanBorderFsmTaskSeqId_Type()
)
cucsSwFcSanBorderFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTaskSeqId.setStatus("current")
_CucsSwFcSanEpTable_Object = MibTable
cucsSwFcSanEpTable = _CucsSwFcSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24)
)
if mibBuilder.loadTexts:
    cucsSwFcSanEpTable.setStatus("current")
_CucsSwFcSanEpEntry_Object = MibTableRow
cucsSwFcSanEpEntry = _CucsSwFcSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1)
)
cucsSwFcSanEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcSanEpEntry.setStatus("current")
_CucsSwFcSanEpInstanceId_Type = CucsManagedObjectId
_CucsSwFcSanEpInstanceId_Object = MibTableColumn
cucsSwFcSanEpInstanceId = _CucsSwFcSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 1),
    _CucsSwFcSanEpInstanceId_Type()
)
cucsSwFcSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcSanEpInstanceId.setStatus("current")
_CucsSwFcSanEpDn_Type = CucsManagedObjectDn
_CucsSwFcSanEpDn_Object = MibTableColumn
cucsSwFcSanEpDn = _CucsSwFcSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 2),
    _CucsSwFcSanEpDn_Type()
)
cucsSwFcSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpDn.setStatus("current")
_CucsSwFcSanEpRn_Type = SnmpAdminString
_CucsSwFcSanEpRn_Object = MibTableColumn
cucsSwFcSanEpRn = _CucsSwFcSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 3),
    _CucsSwFcSanEpRn_Type()
)
cucsSwFcSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpRn.setStatus("current")
_CucsSwFcSanEpAdminState_Type = CucsFabricAdminState
_CucsSwFcSanEpAdminState_Object = MibTableColumn
cucsSwFcSanEpAdminState = _CucsSwFcSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 4),
    _CucsSwFcSanEpAdminState_Type()
)
cucsSwFcSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpAdminState.setStatus("current")
_CucsSwFcSanEpChassisId_Type = Gauge32
_CucsSwFcSanEpChassisId_Object = MibTableColumn
cucsSwFcSanEpChassisId = _CucsSwFcSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 5),
    _CucsSwFcSanEpChassisId_Type()
)
cucsSwFcSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpChassisId.setStatus("current")
_CucsSwFcSanEpEpDn_Type = SnmpAdminString
_CucsSwFcSanEpEpDn_Object = MibTableColumn
cucsSwFcSanEpEpDn = _CucsSwFcSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 6),
    _CucsSwFcSanEpEpDn_Type()
)
cucsSwFcSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpEpDn.setStatus("current")
_CucsSwFcSanEpIfRole_Type = CucsSwSanEpIfRole
_CucsSwFcSanEpIfRole_Object = MibTableColumn
cucsSwFcSanEpIfRole = _CucsSwFcSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 7),
    _CucsSwFcSanEpIfRole_Type()
)
cucsSwFcSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpIfRole.setStatus("current")
_CucsSwFcSanEpIfType_Type = CucsSwPIoEpIfType
_CucsSwFcSanEpIfType_Object = MibTableColumn
cucsSwFcSanEpIfType = _CucsSwFcSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 8),
    _CucsSwFcSanEpIfType_Type()
)
cucsSwFcSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpIfType.setStatus("current")
_CucsSwFcSanEpLocale_Type = CucsSwBorderEpLocale
_CucsSwFcSanEpLocale_Object = MibTableColumn
cucsSwFcSanEpLocale = _CucsSwFcSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 9),
    _CucsSwFcSanEpLocale_Type()
)
cucsSwFcSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpLocale.setStatus("current")
_CucsSwFcSanEpName_Type = SnmpAdminString
_CucsSwFcSanEpName_Object = MibTableColumn
cucsSwFcSanEpName = _CucsSwFcSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 10),
    _CucsSwFcSanEpName_Type()
)
cucsSwFcSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpName.setStatus("current")
_CucsSwFcSanEpPcId_Type = Gauge32
_CucsSwFcSanEpPcId_Object = MibTableColumn
cucsSwFcSanEpPcId = _CucsSwFcSanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 11),
    _CucsSwFcSanEpPcId_Type()
)
cucsSwFcSanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpPcId.setStatus("current")
_CucsSwFcSanEpPeerDn_Type = SnmpAdminString
_CucsSwFcSanEpPeerDn_Object = MibTableColumn
cucsSwFcSanEpPeerDn = _CucsSwFcSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 12),
    _CucsSwFcSanEpPeerDn_Type()
)
cucsSwFcSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpPeerDn.setStatus("current")
_CucsSwFcSanEpPeerPortId_Type = Gauge32
_CucsSwFcSanEpPeerPortId_Object = MibTableColumn
cucsSwFcSanEpPeerPortId = _CucsSwFcSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 13),
    _CucsSwFcSanEpPeerPortId_Type()
)
cucsSwFcSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpPeerPortId.setStatus("current")
_CucsSwFcSanEpPeerSlotId_Type = Gauge32
_CucsSwFcSanEpPeerSlotId_Object = MibTableColumn
cucsSwFcSanEpPeerSlotId = _CucsSwFcSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 14),
    _CucsSwFcSanEpPeerSlotId_Type()
)
cucsSwFcSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpPeerSlotId.setStatus("current")
_CucsSwFcSanEpPortId_Type = Gauge32
_CucsSwFcSanEpPortId_Object = MibTableColumn
cucsSwFcSanEpPortId = _CucsSwFcSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 15),
    _CucsSwFcSanEpPortId_Type()
)
cucsSwFcSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpPortId.setStatus("current")
_CucsSwFcSanEpPortVsanId_Type = Gauge32
_CucsSwFcSanEpPortVsanId_Object = MibTableColumn
cucsSwFcSanEpPortVsanId = _CucsSwFcSanEpPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 16),
    _CucsSwFcSanEpPortVsanId_Type()
)
cucsSwFcSanEpPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpPortVsanId.setStatus("current")
_CucsSwFcSanEpSlotId_Type = Gauge32
_CucsSwFcSanEpSlotId_Object = MibTableColumn
cucsSwFcSanEpSlotId = _CucsSwFcSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 17),
    _CucsSwFcSanEpSlotId_Type()
)
cucsSwFcSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpSlotId.setStatus("current")
_CucsSwFcSanEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcSanEpSwitchId_Object = MibTableColumn
cucsSwFcSanEpSwitchId = _CucsSwFcSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 18),
    _CucsSwFcSanEpSwitchId_Type()
)
cucsSwFcSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpSwitchId.setStatus("current")
_CucsSwFcSanEpTransport_Type = CucsSwFcSanEpTransport
_CucsSwFcSanEpTransport_Object = MibTableColumn
cucsSwFcSanEpTransport = _CucsSwFcSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 19),
    _CucsSwFcSanEpTransport_Type()
)
cucsSwFcSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpTransport.setStatus("current")
_CucsSwFcSanEpType_Type = CucsSwSanEpType
_CucsSwFcSanEpType_Object = MibTableColumn
cucsSwFcSanEpType = _CucsSwFcSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 20),
    _CucsSwFcSanEpType_Type()
)
cucsSwFcSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpType.setStatus("current")
_CucsSwFcSanEpAdminSpeed_Type = CucsPortSpeed
_CucsSwFcSanEpAdminSpeed_Object = MibTableColumn
cucsSwFcSanEpAdminSpeed = _CucsSwFcSanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 21),
    _CucsSwFcSanEpAdminSpeed_Type()
)
cucsSwFcSanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpAdminSpeed.setStatus("current")
_CucsSwFcSanEpPeerChassisId_Type = Gauge32
_CucsSwFcSanEpPeerChassisId_Object = MibTableColumn
cucsSwFcSanEpPeerChassisId = _CucsSwFcSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 22),
    _CucsSwFcSanEpPeerChassisId_Type()
)
cucsSwFcSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpPeerChassisId.setStatus("current")
_CucsSwFcSanEpLc_Type = CucsSwPIoEpLc
_CucsSwFcSanEpLc_Object = MibTableColumn
cucsSwFcSanEpLc = _CucsSwFcSanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 23),
    _CucsSwFcSanEpLc_Type()
)
cucsSwFcSanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpLc.setStatus("current")
_CucsSwFcSanEpFillPattern_Type = CucsFabricFillPattern
_CucsSwFcSanEpFillPattern_Object = MibTableColumn
cucsSwFcSanEpFillPattern = _CucsSwFcSanEpFillPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 24),
    _CucsSwFcSanEpFillPattern_Type()
)
cucsSwFcSanEpFillPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpFillPattern.setStatus("current")
_CucsSwFcSanEpAggrPortId_Type = Gauge32
_CucsSwFcSanEpAggrPortId_Object = MibTableColumn
cucsSwFcSanEpAggrPortId = _CucsSwFcSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 25),
    _CucsSwFcSanEpAggrPortId_Type()
)
cucsSwFcSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpAggrPortId.setStatus("current")
_CucsSwFcSanEpPeerAggrPortId_Type = Gauge32
_CucsSwFcSanEpPeerAggrPortId_Object = MibTableColumn
cucsSwFcSanEpPeerAggrPortId = _CucsSwFcSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 26),
    _CucsSwFcSanEpPeerAggrPortId_Type()
)
cucsSwFcSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpPeerAggrPortId.setStatus("current")
_CucsSwFcSanEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwFcSanEpAutoNegotiate_Object = MibTableColumn
cucsSwFcSanEpAutoNegotiate = _CucsSwFcSanEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 24, 1, 27),
    _CucsSwFcSanEpAutoNegotiate_Type()
)
cucsSwFcSanEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanEpAutoNegotiate.setStatus("current")
_CucsSwFcSanMonTable_Object = MibTable
cucsSwFcSanMonTable = _CucsSwFcSanMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25)
)
if mibBuilder.loadTexts:
    cucsSwFcSanMonTable.setStatus("current")
_CucsSwFcSanMonEntry_Object = MibTableRow
cucsSwFcSanMonEntry = _CucsSwFcSanMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1)
)
cucsSwFcSanMonEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcSanMonInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcSanMonEntry.setStatus("current")
_CucsSwFcSanMonInstanceId_Type = CucsManagedObjectId
_CucsSwFcSanMonInstanceId_Object = MibTableColumn
cucsSwFcSanMonInstanceId = _CucsSwFcSanMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1, 1),
    _CucsSwFcSanMonInstanceId_Type()
)
cucsSwFcSanMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcSanMonInstanceId.setStatus("current")
_CucsSwFcSanMonDn_Type = CucsManagedObjectDn
_CucsSwFcSanMonDn_Object = MibTableColumn
cucsSwFcSanMonDn = _CucsSwFcSanMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1, 2),
    _CucsSwFcSanMonDn_Type()
)
cucsSwFcSanMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanMonDn.setStatus("current")
_CucsSwFcSanMonRn_Type = SnmpAdminString
_CucsSwFcSanMonRn_Object = MibTableColumn
cucsSwFcSanMonRn = _CucsSwFcSanMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1, 3),
    _CucsSwFcSanMonRn_Type()
)
cucsSwFcSanMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanMonRn.setStatus("current")
_CucsSwFcSanMonLocale_Type = CucsSwMonDomainLocale
_CucsSwFcSanMonLocale_Object = MibTableColumn
cucsSwFcSanMonLocale = _CucsSwFcSanMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1, 4),
    _CucsSwFcSanMonLocale_Type()
)
cucsSwFcSanMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanMonLocale.setStatus("current")
_CucsSwFcSanMonName_Type = SnmpAdminString
_CucsSwFcSanMonName_Object = MibTableColumn
cucsSwFcSanMonName = _CucsSwFcSanMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1, 5),
    _CucsSwFcSanMonName_Type()
)
cucsSwFcSanMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanMonName.setStatus("current")
_CucsSwFcSanMonSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcSanMonSwitchId_Object = MibTableColumn
cucsSwFcSanMonSwitchId = _CucsSwFcSanMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1, 6),
    _CucsSwFcSanMonSwitchId_Type()
)
cucsSwFcSanMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanMonSwitchId.setStatus("current")
_CucsSwFcSanMonTransport_Type = CucsSwFcSanMonTransport
_CucsSwFcSanMonTransport_Object = MibTableColumn
cucsSwFcSanMonTransport = _CucsSwFcSanMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1, 7),
    _CucsSwFcSanMonTransport_Type()
)
cucsSwFcSanMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanMonTransport.setStatus("current")
_CucsSwFcSanMonType_Type = CucsSwSanMonType
_CucsSwFcSanMonType_Object = MibTableColumn
cucsSwFcSanMonType = _CucsSwFcSanMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 25, 1, 8),
    _CucsSwFcSanMonType_Type()
)
cucsSwFcSanMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanMonType.setStatus("current")
_CucsSwFcSanPcTable_Object = MibTable
cucsSwFcSanPcTable = _CucsSwFcSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26)
)
if mibBuilder.loadTexts:
    cucsSwFcSanPcTable.setStatus("current")
_CucsSwFcSanPcEntry_Object = MibTableRow
cucsSwFcSanPcEntry = _CucsSwFcSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1)
)
cucsSwFcSanPcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcSanPcEntry.setStatus("current")
_CucsSwFcSanPcInstanceId_Type = CucsManagedObjectId
_CucsSwFcSanPcInstanceId_Object = MibTableColumn
cucsSwFcSanPcInstanceId = _CucsSwFcSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 1),
    _CucsSwFcSanPcInstanceId_Type()
)
cucsSwFcSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcSanPcInstanceId.setStatus("current")
_CucsSwFcSanPcDn_Type = CucsManagedObjectDn
_CucsSwFcSanPcDn_Object = MibTableColumn
cucsSwFcSanPcDn = _CucsSwFcSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 2),
    _CucsSwFcSanPcDn_Type()
)
cucsSwFcSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcDn.setStatus("current")
_CucsSwFcSanPcRn_Type = SnmpAdminString
_CucsSwFcSanPcRn_Object = MibTableColumn
cucsSwFcSanPcRn = _CucsSwFcSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 3),
    _CucsSwFcSanPcRn_Type()
)
cucsSwFcSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcRn.setStatus("current")
_CucsSwFcSanPcAdminState_Type = CucsFabricAdminState
_CucsSwFcSanPcAdminState_Object = MibTableColumn
cucsSwFcSanPcAdminState = _CucsSwFcSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 4),
    _CucsSwFcSanPcAdminState_Type()
)
cucsSwFcSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcAdminState.setStatus("current")
_CucsSwFcSanPcEpDn_Type = SnmpAdminString
_CucsSwFcSanPcEpDn_Object = MibTableColumn
cucsSwFcSanPcEpDn = _CucsSwFcSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 5),
    _CucsSwFcSanPcEpDn_Type()
)
cucsSwFcSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcEpDn.setStatus("current")
_CucsSwFcSanPcIfRole_Type = CucsSwSanPcIfRole
_CucsSwFcSanPcIfRole_Object = MibTableColumn
cucsSwFcSanPcIfRole = _CucsSwFcSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 6),
    _CucsSwFcSanPcIfRole_Type()
)
cucsSwFcSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcIfRole.setStatus("current")
_CucsSwFcSanPcIfType_Type = CucsSwCIoEpIfType
_CucsSwFcSanPcIfType_Object = MibTableColumn
cucsSwFcSanPcIfType = _CucsSwFcSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 7),
    _CucsSwFcSanPcIfType_Type()
)
cucsSwFcSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcIfType.setStatus("current")
_CucsSwFcSanPcLocale_Type = CucsSwBorderPcLocale
_CucsSwFcSanPcLocale_Object = MibTableColumn
cucsSwFcSanPcLocale = _CucsSwFcSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 8),
    _CucsSwFcSanPcLocale_Type()
)
cucsSwFcSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcLocale.setStatus("current")
_CucsSwFcSanPcName_Type = SnmpAdminString
_CucsSwFcSanPcName_Object = MibTableColumn
cucsSwFcSanPcName = _CucsSwFcSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 9),
    _CucsSwFcSanPcName_Type()
)
cucsSwFcSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcName.setStatus("current")
_CucsSwFcSanPcPcId_Type = Gauge32
_CucsSwFcSanPcPcId_Object = MibTableColumn
cucsSwFcSanPcPcId = _CucsSwFcSanPcPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 10),
    _CucsSwFcSanPcPcId_Type()
)
cucsSwFcSanPcPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcPcId.setStatus("current")
_CucsSwFcSanPcPeerDn_Type = SnmpAdminString
_CucsSwFcSanPcPeerDn_Object = MibTableColumn
cucsSwFcSanPcPeerDn = _CucsSwFcSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 11),
    _CucsSwFcSanPcPeerDn_Type()
)
cucsSwFcSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcPeerDn.setStatus("current")
_CucsSwFcSanPcPortId_Type = Gauge32
_CucsSwFcSanPcPortId_Object = MibTableColumn
cucsSwFcSanPcPortId = _CucsSwFcSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 12),
    _CucsSwFcSanPcPortId_Type()
)
cucsSwFcSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcPortId.setStatus("current")
_CucsSwFcSanPcPortVsanId_Type = Gauge32
_CucsSwFcSanPcPortVsanId_Object = MibTableColumn
cucsSwFcSanPcPortVsanId = _CucsSwFcSanPcPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 13),
    _CucsSwFcSanPcPortVsanId_Type()
)
cucsSwFcSanPcPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcPortVsanId.setStatus("current")
_CucsSwFcSanPcSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcSanPcSwitchId_Object = MibTableColumn
cucsSwFcSanPcSwitchId = _CucsSwFcSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 14),
    _CucsSwFcSanPcSwitchId_Type()
)
cucsSwFcSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcSwitchId.setStatus("current")
_CucsSwFcSanPcTransport_Type = CucsSwFcSanPcTransport
_CucsSwFcSanPcTransport_Object = MibTableColumn
cucsSwFcSanPcTransport = _CucsSwFcSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 15),
    _CucsSwFcSanPcTransport_Type()
)
cucsSwFcSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcTransport.setStatus("current")
_CucsSwFcSanPcType_Type = CucsSwSanPcType
_CucsSwFcSanPcType_Object = MibTableColumn
cucsSwFcSanPcType = _CucsSwFcSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 16),
    _CucsSwFcSanPcType_Type()
)
cucsSwFcSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcType.setStatus("current")
_CucsSwFcSanPcMonTrafDir_Type = CucsFabricTrafficDirection
_CucsSwFcSanPcMonTrafDir_Object = MibTableColumn
cucsSwFcSanPcMonTrafDir = _CucsSwFcSanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 17),
    _CucsSwFcSanPcMonTrafDir_Type()
)
cucsSwFcSanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcMonTrafDir.setStatus("current")
_CucsSwFcSanPcAdminSpeed_Type = CucsPortSpeed
_CucsSwFcSanPcAdminSpeed_Object = MibTableColumn
cucsSwFcSanPcAdminSpeed = _CucsSwFcSanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 26, 1, 18),
    _CucsSwFcSanPcAdminSpeed_Type()
)
cucsSwFcSanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanPcAdminSpeed.setStatus("current")
_CucsSwFcoeEstcEpTable_Object = MibTable
cucsSwFcoeEstcEpTable = _CucsSwFcoeEstcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27)
)
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpTable.setStatus("current")
_CucsSwFcoeEstcEpEntry_Object = MibTableRow
cucsSwFcoeEstcEpEntry = _CucsSwFcoeEstcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1)
)
cucsSwFcoeEstcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcoeEstcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpEntry.setStatus("current")
_CucsSwFcoeEstcEpInstanceId_Type = CucsManagedObjectId
_CucsSwFcoeEstcEpInstanceId_Object = MibTableColumn
cucsSwFcoeEstcEpInstanceId = _CucsSwFcoeEstcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 1),
    _CucsSwFcoeEstcEpInstanceId_Type()
)
cucsSwFcoeEstcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpInstanceId.setStatus("current")
_CucsSwFcoeEstcEpDn_Type = CucsManagedObjectDn
_CucsSwFcoeEstcEpDn_Object = MibTableColumn
cucsSwFcoeEstcEpDn = _CucsSwFcoeEstcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 2),
    _CucsSwFcoeEstcEpDn_Type()
)
cucsSwFcoeEstcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpDn.setStatus("current")
_CucsSwFcoeEstcEpRn_Type = SnmpAdminString
_CucsSwFcoeEstcEpRn_Object = MibTableColumn
cucsSwFcoeEstcEpRn = _CucsSwFcoeEstcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 3),
    _CucsSwFcoeEstcEpRn_Type()
)
cucsSwFcoeEstcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpRn.setStatus("current")
_CucsSwFcoeEstcEpAdminState_Type = CucsFabricAdminState
_CucsSwFcoeEstcEpAdminState_Object = MibTableColumn
cucsSwFcoeEstcEpAdminState = _CucsSwFcoeEstcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 4),
    _CucsSwFcoeEstcEpAdminState_Type()
)
cucsSwFcoeEstcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpAdminState.setStatus("current")
_CucsSwFcoeEstcEpChassisId_Type = Gauge32
_CucsSwFcoeEstcEpChassisId_Object = MibTableColumn
cucsSwFcoeEstcEpChassisId = _CucsSwFcoeEstcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 5),
    _CucsSwFcoeEstcEpChassisId_Type()
)
cucsSwFcoeEstcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpChassisId.setStatus("current")
_CucsSwFcoeEstcEpEpDn_Type = SnmpAdminString
_CucsSwFcoeEstcEpEpDn_Object = MibTableColumn
cucsSwFcoeEstcEpEpDn = _CucsSwFcoeEstcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 6),
    _CucsSwFcoeEstcEpEpDn_Type()
)
cucsSwFcoeEstcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpEpDn.setStatus("current")
_CucsSwFcoeEstcEpIfRole_Type = CucsNetworkPortRole
_CucsSwFcoeEstcEpIfRole_Object = MibTableColumn
cucsSwFcoeEstcEpIfRole = _CucsSwFcoeEstcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 7),
    _CucsSwFcoeEstcEpIfRole_Type()
)
cucsSwFcoeEstcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpIfRole.setStatus("current")
_CucsSwFcoeEstcEpIfType_Type = CucsSwPIoEpIfType
_CucsSwFcoeEstcEpIfType_Object = MibTableColumn
cucsSwFcoeEstcEpIfType = _CucsSwFcoeEstcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 8),
    _CucsSwFcoeEstcEpIfType_Type()
)
cucsSwFcoeEstcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpIfType.setStatus("current")
_CucsSwFcoeEstcEpLocale_Type = CucsSwEstcEpLocale
_CucsSwFcoeEstcEpLocale_Object = MibTableColumn
cucsSwFcoeEstcEpLocale = _CucsSwFcoeEstcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 9),
    _CucsSwFcoeEstcEpLocale_Type()
)
cucsSwFcoeEstcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpLocale.setStatus("current")
_CucsSwFcoeEstcEpName_Type = SnmpAdminString
_CucsSwFcoeEstcEpName_Object = MibTableColumn
cucsSwFcoeEstcEpName = _CucsSwFcoeEstcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 10),
    _CucsSwFcoeEstcEpName_Type()
)
cucsSwFcoeEstcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpName.setStatus("current")
_CucsSwFcoeEstcEpPeerDn_Type = SnmpAdminString
_CucsSwFcoeEstcEpPeerDn_Object = MibTableColumn
cucsSwFcoeEstcEpPeerDn = _CucsSwFcoeEstcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 11),
    _CucsSwFcoeEstcEpPeerDn_Type()
)
cucsSwFcoeEstcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpPeerDn.setStatus("current")
_CucsSwFcoeEstcEpPeerPortId_Type = Gauge32
_CucsSwFcoeEstcEpPeerPortId_Object = MibTableColumn
cucsSwFcoeEstcEpPeerPortId = _CucsSwFcoeEstcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 12),
    _CucsSwFcoeEstcEpPeerPortId_Type()
)
cucsSwFcoeEstcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpPeerPortId.setStatus("current")
_CucsSwFcoeEstcEpPeerSlotId_Type = Gauge32
_CucsSwFcoeEstcEpPeerSlotId_Object = MibTableColumn
cucsSwFcoeEstcEpPeerSlotId = _CucsSwFcoeEstcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 13),
    _CucsSwFcoeEstcEpPeerSlotId_Type()
)
cucsSwFcoeEstcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpPeerSlotId.setStatus("current")
_CucsSwFcoeEstcEpPortId_Type = Gauge32
_CucsSwFcoeEstcEpPortId_Object = MibTableColumn
cucsSwFcoeEstcEpPortId = _CucsSwFcoeEstcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 14),
    _CucsSwFcoeEstcEpPortId_Type()
)
cucsSwFcoeEstcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpPortId.setStatus("current")
_CucsSwFcoeEstcEpSlotId_Type = Gauge32
_CucsSwFcoeEstcEpSlotId_Object = MibTableColumn
cucsSwFcoeEstcEpSlotId = _CucsSwFcoeEstcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 15),
    _CucsSwFcoeEstcEpSlotId_Type()
)
cucsSwFcoeEstcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpSlotId.setStatus("current")
_CucsSwFcoeEstcEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcoeEstcEpSwitchId_Object = MibTableColumn
cucsSwFcoeEstcEpSwitchId = _CucsSwFcoeEstcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 16),
    _CucsSwFcoeEstcEpSwitchId_Type()
)
cucsSwFcoeEstcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpSwitchId.setStatus("current")
_CucsSwFcoeEstcEpTransport_Type = CucsSwFcoeEstcEpTransport
_CucsSwFcoeEstcEpTransport_Object = MibTableColumn
cucsSwFcoeEstcEpTransport = _CucsSwFcoeEstcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 17),
    _CucsSwFcoeEstcEpTransport_Type()
)
cucsSwFcoeEstcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpTransport.setStatus("current")
_CucsSwFcoeEstcEpType_Type = CucsNetworkConnectionType
_CucsSwFcoeEstcEpType_Object = MibTableColumn
cucsSwFcoeEstcEpType = _CucsSwFcoeEstcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 18),
    _CucsSwFcoeEstcEpType_Type()
)
cucsSwFcoeEstcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpType.setStatus("current")
_CucsSwFcoeEstcEpPeerChassisId_Type = Gauge32
_CucsSwFcoeEstcEpPeerChassisId_Object = MibTableColumn
cucsSwFcoeEstcEpPeerChassisId = _CucsSwFcoeEstcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 19),
    _CucsSwFcoeEstcEpPeerChassisId_Type()
)
cucsSwFcoeEstcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpPeerChassisId.setStatus("current")
_CucsSwFcoeEstcEpLc_Type = CucsSwPIoEpLc
_CucsSwFcoeEstcEpLc_Object = MibTableColumn
cucsSwFcoeEstcEpLc = _CucsSwFcoeEstcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 20),
    _CucsSwFcoeEstcEpLc_Type()
)
cucsSwFcoeEstcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpLc.setStatus("current")
_CucsSwFcoeEstcEpPeerState_Type = CucsSwPeerStatus
_CucsSwFcoeEstcEpPeerState_Object = MibTableColumn
cucsSwFcoeEstcEpPeerState = _CucsSwFcoeEstcEpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 21),
    _CucsSwFcoeEstcEpPeerState_Type()
)
cucsSwFcoeEstcEpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpPeerState.setStatus("current")
_CucsSwFcoeEstcEpAggrPortId_Type = Gauge32
_CucsSwFcoeEstcEpAggrPortId_Object = MibTableColumn
cucsSwFcoeEstcEpAggrPortId = _CucsSwFcoeEstcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 22),
    _CucsSwFcoeEstcEpAggrPortId_Type()
)
cucsSwFcoeEstcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpAggrPortId.setStatus("current")
_CucsSwFcoeEstcEpPeerAggrPortId_Type = Gauge32
_CucsSwFcoeEstcEpPeerAggrPortId_Object = MibTableColumn
cucsSwFcoeEstcEpPeerAggrPortId = _CucsSwFcoeEstcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 23),
    _CucsSwFcoeEstcEpPeerAggrPortId_Type()
)
cucsSwFcoeEstcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpPeerAggrPortId.setStatus("current")
_CucsSwFcoeEstcEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwFcoeEstcEpAutoNegotiate_Object = MibTableColumn
cucsSwFcoeEstcEpAutoNegotiate = _CucsSwFcoeEstcEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 27, 1, 24),
    _CucsSwFcoeEstcEpAutoNegotiate_Type()
)
cucsSwFcoeEstcEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeEstcEpAutoNegotiate.setStatus("current")
_CucsSwSystemStatsTable_Object = MibTable
cucsSwSystemStatsTable = _CucsSwSystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28)
)
if mibBuilder.loadTexts:
    cucsSwSystemStatsTable.setStatus("current")
_CucsSwSystemStatsEntry_Object = MibTableRow
cucsSwSystemStatsEntry = _CucsSwSystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1)
)
cucsSwSystemStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwSystemStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwSystemStatsEntry.setStatus("current")
_CucsSwSystemStatsInstanceId_Type = CucsManagedObjectId
_CucsSwSystemStatsInstanceId_Object = MibTableColumn
cucsSwSystemStatsInstanceId = _CucsSwSystemStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 1),
    _CucsSwSystemStatsInstanceId_Type()
)
cucsSwSystemStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwSystemStatsInstanceId.setStatus("current")
_CucsSwSystemStatsDn_Type = CucsManagedObjectDn
_CucsSwSystemStatsDn_Object = MibTableColumn
cucsSwSystemStatsDn = _CucsSwSystemStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 2),
    _CucsSwSystemStatsDn_Type()
)
cucsSwSystemStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsDn.setStatus("current")
_CucsSwSystemStatsRn_Type = SnmpAdminString
_CucsSwSystemStatsRn_Object = MibTableColumn
cucsSwSystemStatsRn = _CucsSwSystemStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 3),
    _CucsSwSystemStatsRn_Type()
)
cucsSwSystemStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsRn.setStatus("current")
_CucsSwSystemStatsIntervals_Type = Gauge32
_CucsSwSystemStatsIntervals_Object = MibTableColumn
cucsSwSystemStatsIntervals = _CucsSwSystemStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 4),
    _CucsSwSystemStatsIntervals_Type()
)
cucsSwSystemStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsIntervals.setStatus("current")
_CucsSwSystemStatsLoad_Type = Integer32
_CucsSwSystemStatsLoad_Object = MibTableColumn
cucsSwSystemStatsLoad = _CucsSwSystemStatsLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 5),
    _CucsSwSystemStatsLoad_Type()
)
cucsSwSystemStatsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsLoad.setStatus("current")
_CucsSwSystemStatsLoadAvg_Type = Integer32
_CucsSwSystemStatsLoadAvg_Object = MibTableColumn
cucsSwSystemStatsLoadAvg = _CucsSwSystemStatsLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 6),
    _CucsSwSystemStatsLoadAvg_Type()
)
cucsSwSystemStatsLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsLoadAvg.setStatus("current")
_CucsSwSystemStatsLoadMax_Type = Integer32
_CucsSwSystemStatsLoadMax_Object = MibTableColumn
cucsSwSystemStatsLoadMax = _CucsSwSystemStatsLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 7),
    _CucsSwSystemStatsLoadMax_Type()
)
cucsSwSystemStatsLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsLoadMax.setStatus("current")
_CucsSwSystemStatsLoadMin_Type = Integer32
_CucsSwSystemStatsLoadMin_Object = MibTableColumn
cucsSwSystemStatsLoadMin = _CucsSwSystemStatsLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 8),
    _CucsSwSystemStatsLoadMin_Type()
)
cucsSwSystemStatsLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsLoadMin.setStatus("current")
_CucsSwSystemStatsMemAvailable_Type = Gauge32
_CucsSwSystemStatsMemAvailable_Object = MibTableColumn
cucsSwSystemStatsMemAvailable = _CucsSwSystemStatsMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 9),
    _CucsSwSystemStatsMemAvailable_Type()
)
cucsSwSystemStatsMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsMemAvailable.setStatus("current")
_CucsSwSystemStatsMemAvailableAvg_Type = Gauge32
_CucsSwSystemStatsMemAvailableAvg_Object = MibTableColumn
cucsSwSystemStatsMemAvailableAvg = _CucsSwSystemStatsMemAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 10),
    _CucsSwSystemStatsMemAvailableAvg_Type()
)
cucsSwSystemStatsMemAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsMemAvailableAvg.setStatus("current")
_CucsSwSystemStatsMemAvailableMax_Type = Gauge32
_CucsSwSystemStatsMemAvailableMax_Object = MibTableColumn
cucsSwSystemStatsMemAvailableMax = _CucsSwSystemStatsMemAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 11),
    _CucsSwSystemStatsMemAvailableMax_Type()
)
cucsSwSystemStatsMemAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsMemAvailableMax.setStatus("current")
_CucsSwSystemStatsMemAvailableMin_Type = Gauge32
_CucsSwSystemStatsMemAvailableMin_Object = MibTableColumn
cucsSwSystemStatsMemAvailableMin = _CucsSwSystemStatsMemAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 12),
    _CucsSwSystemStatsMemAvailableMin_Type()
)
cucsSwSystemStatsMemAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsMemAvailableMin.setStatus("current")
_CucsSwSystemStatsMemCached_Type = Gauge32
_CucsSwSystemStatsMemCached_Object = MibTableColumn
cucsSwSystemStatsMemCached = _CucsSwSystemStatsMemCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 13),
    _CucsSwSystemStatsMemCached_Type()
)
cucsSwSystemStatsMemCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsMemCached.setStatus("current")
_CucsSwSystemStatsMemCachedAvg_Type = Gauge32
_CucsSwSystemStatsMemCachedAvg_Object = MibTableColumn
cucsSwSystemStatsMemCachedAvg = _CucsSwSystemStatsMemCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 14),
    _CucsSwSystemStatsMemCachedAvg_Type()
)
cucsSwSystemStatsMemCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsMemCachedAvg.setStatus("current")
_CucsSwSystemStatsMemCachedMax_Type = Gauge32
_CucsSwSystemStatsMemCachedMax_Object = MibTableColumn
cucsSwSystemStatsMemCachedMax = _CucsSwSystemStatsMemCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 15),
    _CucsSwSystemStatsMemCachedMax_Type()
)
cucsSwSystemStatsMemCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsMemCachedMax.setStatus("current")
_CucsSwSystemStatsMemCachedMin_Type = Gauge32
_CucsSwSystemStatsMemCachedMin_Object = MibTableColumn
cucsSwSystemStatsMemCachedMin = _CucsSwSystemStatsMemCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 16),
    _CucsSwSystemStatsMemCachedMin_Type()
)
cucsSwSystemStatsMemCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsMemCachedMin.setStatus("current")
_CucsSwSystemStatsSuspect_Type = TruthValue
_CucsSwSystemStatsSuspect_Object = MibTableColumn
cucsSwSystemStatsSuspect = _CucsSwSystemStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 17),
    _CucsSwSystemStatsSuspect_Type()
)
cucsSwSystemStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsSuspect.setStatus("current")
_CucsSwSystemStatsThresholded_Type = CucsSwSystemStatsThresholded
_CucsSwSystemStatsThresholded_Object = MibTableColumn
cucsSwSystemStatsThresholded = _CucsSwSystemStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 18),
    _CucsSwSystemStatsThresholded_Type()
)
cucsSwSystemStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsThresholded.setStatus("current")
_CucsSwSystemStatsTimeCollected_Type = DateAndTime
_CucsSwSystemStatsTimeCollected_Object = MibTableColumn
cucsSwSystemStatsTimeCollected = _CucsSwSystemStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 19),
    _CucsSwSystemStatsTimeCollected_Type()
)
cucsSwSystemStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsTimeCollected.setStatus("current")
_CucsSwSystemStatsUpdate_Type = Gauge32
_CucsSwSystemStatsUpdate_Object = MibTableColumn
cucsSwSystemStatsUpdate = _CucsSwSystemStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 20),
    _CucsSwSystemStatsUpdate_Type()
)
cucsSwSystemStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsUpdate.setStatus("current")
_CucsSwSystemStatsCorrectableParityError_Type = Gauge32
_CucsSwSystemStatsCorrectableParityError_Object = MibTableColumn
cucsSwSystemStatsCorrectableParityError = _CucsSwSystemStatsCorrectableParityError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 23),
    _CucsSwSystemStatsCorrectableParityError_Type()
)
cucsSwSystemStatsCorrectableParityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsCorrectableParityError.setStatus("current")
_CucsSwSystemStatsCorrectableParityErrorAvg_Type = Gauge32
_CucsSwSystemStatsCorrectableParityErrorAvg_Object = MibTableColumn
cucsSwSystemStatsCorrectableParityErrorAvg = _CucsSwSystemStatsCorrectableParityErrorAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 24),
    _CucsSwSystemStatsCorrectableParityErrorAvg_Type()
)
cucsSwSystemStatsCorrectableParityErrorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsCorrectableParityErrorAvg.setStatus("current")
_CucsSwSystemStatsCorrectableParityErrorMax_Type = Gauge32
_CucsSwSystemStatsCorrectableParityErrorMax_Object = MibTableColumn
cucsSwSystemStatsCorrectableParityErrorMax = _CucsSwSystemStatsCorrectableParityErrorMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 25),
    _CucsSwSystemStatsCorrectableParityErrorMax_Type()
)
cucsSwSystemStatsCorrectableParityErrorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsCorrectableParityErrorMax.setStatus("current")
_CucsSwSystemStatsCorrectableParityErrorMin_Type = Gauge32
_CucsSwSystemStatsCorrectableParityErrorMin_Object = MibTableColumn
cucsSwSystemStatsCorrectableParityErrorMin = _CucsSwSystemStatsCorrectableParityErrorMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 26),
    _CucsSwSystemStatsCorrectableParityErrorMin_Type()
)
cucsSwSystemStatsCorrectableParityErrorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsCorrectableParityErrorMin.setStatus("current")
_CucsSwSystemStatsKernelMemFree_Type = Gauge32
_CucsSwSystemStatsKernelMemFree_Object = MibTableColumn
cucsSwSystemStatsKernelMemFree = _CucsSwSystemStatsKernelMemFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 27),
    _CucsSwSystemStatsKernelMemFree_Type()
)
cucsSwSystemStatsKernelMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsKernelMemFree.setStatus("current")
_CucsSwSystemStatsKernelMemFreeAvg_Type = Gauge32
_CucsSwSystemStatsKernelMemFreeAvg_Object = MibTableColumn
cucsSwSystemStatsKernelMemFreeAvg = _CucsSwSystemStatsKernelMemFreeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 28),
    _CucsSwSystemStatsKernelMemFreeAvg_Type()
)
cucsSwSystemStatsKernelMemFreeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsKernelMemFreeAvg.setStatus("current")
_CucsSwSystemStatsKernelMemFreeMax_Type = Gauge32
_CucsSwSystemStatsKernelMemFreeMax_Object = MibTableColumn
cucsSwSystemStatsKernelMemFreeMax = _CucsSwSystemStatsKernelMemFreeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 29),
    _CucsSwSystemStatsKernelMemFreeMax_Type()
)
cucsSwSystemStatsKernelMemFreeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsKernelMemFreeMax.setStatus("current")
_CucsSwSystemStatsKernelMemFreeMin_Type = Gauge32
_CucsSwSystemStatsKernelMemFreeMin_Object = MibTableColumn
cucsSwSystemStatsKernelMemFreeMin = _CucsSwSystemStatsKernelMemFreeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 30),
    _CucsSwSystemStatsKernelMemFreeMin_Type()
)
cucsSwSystemStatsKernelMemFreeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsKernelMemFreeMin.setStatus("current")
_CucsSwSystemStatsKernelMemTotal_Type = Gauge32
_CucsSwSystemStatsKernelMemTotal_Object = MibTableColumn
cucsSwSystemStatsKernelMemTotal = _CucsSwSystemStatsKernelMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 31),
    _CucsSwSystemStatsKernelMemTotal_Type()
)
cucsSwSystemStatsKernelMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsKernelMemTotal.setStatus("current")
_CucsSwSystemStatsKernelMemTotalAvg_Type = Gauge32
_CucsSwSystemStatsKernelMemTotalAvg_Object = MibTableColumn
cucsSwSystemStatsKernelMemTotalAvg = _CucsSwSystemStatsKernelMemTotalAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 32),
    _CucsSwSystemStatsKernelMemTotalAvg_Type()
)
cucsSwSystemStatsKernelMemTotalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsKernelMemTotalAvg.setStatus("current")
_CucsSwSystemStatsKernelMemTotalMax_Type = Gauge32
_CucsSwSystemStatsKernelMemTotalMax_Object = MibTableColumn
cucsSwSystemStatsKernelMemTotalMax = _CucsSwSystemStatsKernelMemTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 33),
    _CucsSwSystemStatsKernelMemTotalMax_Type()
)
cucsSwSystemStatsKernelMemTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsKernelMemTotalMax.setStatus("current")
_CucsSwSystemStatsKernelMemTotalMin_Type = Gauge32
_CucsSwSystemStatsKernelMemTotalMin_Object = MibTableColumn
cucsSwSystemStatsKernelMemTotalMin = _CucsSwSystemStatsKernelMemTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 28, 1, 34),
    _CucsSwSystemStatsKernelMemTotalMin_Type()
)
cucsSwSystemStatsKernelMemTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsKernelMemTotalMin.setStatus("current")
_CucsSwSystemStatsHistTable_Object = MibTable
cucsSwSystemStatsHistTable = _CucsSwSystemStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29)
)
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistTable.setStatus("current")
_CucsSwSystemStatsHistEntry_Object = MibTableRow
cucsSwSystemStatsHistEntry = _CucsSwSystemStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1)
)
cucsSwSystemStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwSystemStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistEntry.setStatus("current")
_CucsSwSystemStatsHistInstanceId_Type = CucsManagedObjectId
_CucsSwSystemStatsHistInstanceId_Object = MibTableColumn
cucsSwSystemStatsHistInstanceId = _CucsSwSystemStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 1),
    _CucsSwSystemStatsHistInstanceId_Type()
)
cucsSwSystemStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistInstanceId.setStatus("current")
_CucsSwSystemStatsHistDn_Type = CucsManagedObjectDn
_CucsSwSystemStatsHistDn_Object = MibTableColumn
cucsSwSystemStatsHistDn = _CucsSwSystemStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 2),
    _CucsSwSystemStatsHistDn_Type()
)
cucsSwSystemStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistDn.setStatus("current")
_CucsSwSystemStatsHistRn_Type = SnmpAdminString
_CucsSwSystemStatsHistRn_Object = MibTableColumn
cucsSwSystemStatsHistRn = _CucsSwSystemStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 3),
    _CucsSwSystemStatsHistRn_Type()
)
cucsSwSystemStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistRn.setStatus("current")
_CucsSwSystemStatsHistId_Type = Unsigned64
_CucsSwSystemStatsHistId_Object = MibTableColumn
cucsSwSystemStatsHistId = _CucsSwSystemStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 4),
    _CucsSwSystemStatsHistId_Type()
)
cucsSwSystemStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistId.setStatus("current")
_CucsSwSystemStatsHistLoad_Type = Integer32
_CucsSwSystemStatsHistLoad_Object = MibTableColumn
cucsSwSystemStatsHistLoad = _CucsSwSystemStatsHistLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 5),
    _CucsSwSystemStatsHistLoad_Type()
)
cucsSwSystemStatsHistLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistLoad.setStatus("current")
_CucsSwSystemStatsHistLoadAvg_Type = Integer32
_CucsSwSystemStatsHistLoadAvg_Object = MibTableColumn
cucsSwSystemStatsHistLoadAvg = _CucsSwSystemStatsHistLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 6),
    _CucsSwSystemStatsHistLoadAvg_Type()
)
cucsSwSystemStatsHistLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistLoadAvg.setStatus("current")
_CucsSwSystemStatsHistLoadMax_Type = Integer32
_CucsSwSystemStatsHistLoadMax_Object = MibTableColumn
cucsSwSystemStatsHistLoadMax = _CucsSwSystemStatsHistLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 7),
    _CucsSwSystemStatsHistLoadMax_Type()
)
cucsSwSystemStatsHistLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistLoadMax.setStatus("current")
_CucsSwSystemStatsHistLoadMin_Type = Integer32
_CucsSwSystemStatsHistLoadMin_Object = MibTableColumn
cucsSwSystemStatsHistLoadMin = _CucsSwSystemStatsHistLoadMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 8),
    _CucsSwSystemStatsHistLoadMin_Type()
)
cucsSwSystemStatsHistLoadMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistLoadMin.setStatus("current")
_CucsSwSystemStatsHistMemAvailable_Type = Gauge32
_CucsSwSystemStatsHistMemAvailable_Object = MibTableColumn
cucsSwSystemStatsHistMemAvailable = _CucsSwSystemStatsHistMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 9),
    _CucsSwSystemStatsHistMemAvailable_Type()
)
cucsSwSystemStatsHistMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMemAvailable.setStatus("current")
_CucsSwSystemStatsHistMemAvailableAvg_Type = Gauge32
_CucsSwSystemStatsHistMemAvailableAvg_Object = MibTableColumn
cucsSwSystemStatsHistMemAvailableAvg = _CucsSwSystemStatsHistMemAvailableAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 10),
    _CucsSwSystemStatsHistMemAvailableAvg_Type()
)
cucsSwSystemStatsHistMemAvailableAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMemAvailableAvg.setStatus("current")
_CucsSwSystemStatsHistMemAvailableMax_Type = Gauge32
_CucsSwSystemStatsHistMemAvailableMax_Object = MibTableColumn
cucsSwSystemStatsHistMemAvailableMax = _CucsSwSystemStatsHistMemAvailableMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 11),
    _CucsSwSystemStatsHistMemAvailableMax_Type()
)
cucsSwSystemStatsHistMemAvailableMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMemAvailableMax.setStatus("current")
_CucsSwSystemStatsHistMemAvailableMin_Type = Gauge32
_CucsSwSystemStatsHistMemAvailableMin_Object = MibTableColumn
cucsSwSystemStatsHistMemAvailableMin = _CucsSwSystemStatsHistMemAvailableMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 12),
    _CucsSwSystemStatsHistMemAvailableMin_Type()
)
cucsSwSystemStatsHistMemAvailableMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMemAvailableMin.setStatus("current")
_CucsSwSystemStatsHistMemCached_Type = Gauge32
_CucsSwSystemStatsHistMemCached_Object = MibTableColumn
cucsSwSystemStatsHistMemCached = _CucsSwSystemStatsHistMemCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 13),
    _CucsSwSystemStatsHistMemCached_Type()
)
cucsSwSystemStatsHistMemCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMemCached.setStatus("current")
_CucsSwSystemStatsHistMemCachedAvg_Type = Gauge32
_CucsSwSystemStatsHistMemCachedAvg_Object = MibTableColumn
cucsSwSystemStatsHistMemCachedAvg = _CucsSwSystemStatsHistMemCachedAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 14),
    _CucsSwSystemStatsHistMemCachedAvg_Type()
)
cucsSwSystemStatsHistMemCachedAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMemCachedAvg.setStatus("current")
_CucsSwSystemStatsHistMemCachedMax_Type = Gauge32
_CucsSwSystemStatsHistMemCachedMax_Object = MibTableColumn
cucsSwSystemStatsHistMemCachedMax = _CucsSwSystemStatsHistMemCachedMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 15),
    _CucsSwSystemStatsHistMemCachedMax_Type()
)
cucsSwSystemStatsHistMemCachedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMemCachedMax.setStatus("current")
_CucsSwSystemStatsHistMemCachedMin_Type = Gauge32
_CucsSwSystemStatsHistMemCachedMin_Object = MibTableColumn
cucsSwSystemStatsHistMemCachedMin = _CucsSwSystemStatsHistMemCachedMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 16),
    _CucsSwSystemStatsHistMemCachedMin_Type()
)
cucsSwSystemStatsHistMemCachedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMemCachedMin.setStatus("current")
_CucsSwSystemStatsHistMostRecent_Type = TruthValue
_CucsSwSystemStatsHistMostRecent_Object = MibTableColumn
cucsSwSystemStatsHistMostRecent = _CucsSwSystemStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 17),
    _CucsSwSystemStatsHistMostRecent_Type()
)
cucsSwSystemStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistMostRecent.setStatus("current")
_CucsSwSystemStatsHistSuspect_Type = TruthValue
_CucsSwSystemStatsHistSuspect_Object = MibTableColumn
cucsSwSystemStatsHistSuspect = _CucsSwSystemStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 18),
    _CucsSwSystemStatsHistSuspect_Type()
)
cucsSwSystemStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistSuspect.setStatus("current")
_CucsSwSystemStatsHistThresholded_Type = CucsSwSystemStatsHistThresholded
_CucsSwSystemStatsHistThresholded_Object = MibTableColumn
cucsSwSystemStatsHistThresholded = _CucsSwSystemStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 19),
    _CucsSwSystemStatsHistThresholded_Type()
)
cucsSwSystemStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistThresholded.setStatus("current")
_CucsSwSystemStatsHistTimeCollected_Type = DateAndTime
_CucsSwSystemStatsHistTimeCollected_Object = MibTableColumn
cucsSwSystemStatsHistTimeCollected = _CucsSwSystemStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 20),
    _CucsSwSystemStatsHistTimeCollected_Type()
)
cucsSwSystemStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistTimeCollected.setStatus("current")
_CucsSwSystemStatsHistCorrectableParityError_Type = Gauge32
_CucsSwSystemStatsHistCorrectableParityError_Object = MibTableColumn
cucsSwSystemStatsHistCorrectableParityError = _CucsSwSystemStatsHistCorrectableParityError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 21),
    _CucsSwSystemStatsHistCorrectableParityError_Type()
)
cucsSwSystemStatsHistCorrectableParityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistCorrectableParityError.setStatus("current")
_CucsSwSystemStatsHistCorrectableParityErrorAvg_Type = Gauge32
_CucsSwSystemStatsHistCorrectableParityErrorAvg_Object = MibTableColumn
cucsSwSystemStatsHistCorrectableParityErrorAvg = _CucsSwSystemStatsHistCorrectableParityErrorAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 22),
    _CucsSwSystemStatsHistCorrectableParityErrorAvg_Type()
)
cucsSwSystemStatsHistCorrectableParityErrorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistCorrectableParityErrorAvg.setStatus("current")
_CucsSwSystemStatsHistCorrectableParityErrorMax_Type = Gauge32
_CucsSwSystemStatsHistCorrectableParityErrorMax_Object = MibTableColumn
cucsSwSystemStatsHistCorrectableParityErrorMax = _CucsSwSystemStatsHistCorrectableParityErrorMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 23),
    _CucsSwSystemStatsHistCorrectableParityErrorMax_Type()
)
cucsSwSystemStatsHistCorrectableParityErrorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistCorrectableParityErrorMax.setStatus("current")
_CucsSwSystemStatsHistCorrectableParityErrorMin_Type = Gauge32
_CucsSwSystemStatsHistCorrectableParityErrorMin_Object = MibTableColumn
cucsSwSystemStatsHistCorrectableParityErrorMin = _CucsSwSystemStatsHistCorrectableParityErrorMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 24),
    _CucsSwSystemStatsHistCorrectableParityErrorMin_Type()
)
cucsSwSystemStatsHistCorrectableParityErrorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistCorrectableParityErrorMin.setStatus("current")
_CucsSwSystemStatsHistKernelMemFree_Type = Gauge32
_CucsSwSystemStatsHistKernelMemFree_Object = MibTableColumn
cucsSwSystemStatsHistKernelMemFree = _CucsSwSystemStatsHistKernelMemFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 25),
    _CucsSwSystemStatsHistKernelMemFree_Type()
)
cucsSwSystemStatsHistKernelMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistKernelMemFree.setStatus("current")
_CucsSwSystemStatsHistKernelMemFreeAvg_Type = Gauge32
_CucsSwSystemStatsHistKernelMemFreeAvg_Object = MibTableColumn
cucsSwSystemStatsHistKernelMemFreeAvg = _CucsSwSystemStatsHistKernelMemFreeAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 26),
    _CucsSwSystemStatsHistKernelMemFreeAvg_Type()
)
cucsSwSystemStatsHistKernelMemFreeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistKernelMemFreeAvg.setStatus("current")
_CucsSwSystemStatsHistKernelMemFreeMax_Type = Gauge32
_CucsSwSystemStatsHistKernelMemFreeMax_Object = MibTableColumn
cucsSwSystemStatsHistKernelMemFreeMax = _CucsSwSystemStatsHistKernelMemFreeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 27),
    _CucsSwSystemStatsHistKernelMemFreeMax_Type()
)
cucsSwSystemStatsHistKernelMemFreeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistKernelMemFreeMax.setStatus("current")
_CucsSwSystemStatsHistKernelMemFreeMin_Type = Gauge32
_CucsSwSystemStatsHistKernelMemFreeMin_Object = MibTableColumn
cucsSwSystemStatsHistKernelMemFreeMin = _CucsSwSystemStatsHistKernelMemFreeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 28),
    _CucsSwSystemStatsHistKernelMemFreeMin_Type()
)
cucsSwSystemStatsHistKernelMemFreeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistKernelMemFreeMin.setStatus("current")
_CucsSwSystemStatsHistKernelMemTotal_Type = Gauge32
_CucsSwSystemStatsHistKernelMemTotal_Object = MibTableColumn
cucsSwSystemStatsHistKernelMemTotal = _CucsSwSystemStatsHistKernelMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 29),
    _CucsSwSystemStatsHistKernelMemTotal_Type()
)
cucsSwSystemStatsHistKernelMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistKernelMemTotal.setStatus("current")
_CucsSwSystemStatsHistKernelMemTotalAvg_Type = Gauge32
_CucsSwSystemStatsHistKernelMemTotalAvg_Object = MibTableColumn
cucsSwSystemStatsHistKernelMemTotalAvg = _CucsSwSystemStatsHistKernelMemTotalAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 30),
    _CucsSwSystemStatsHistKernelMemTotalAvg_Type()
)
cucsSwSystemStatsHistKernelMemTotalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistKernelMemTotalAvg.setStatus("current")
_CucsSwSystemStatsHistKernelMemTotalMax_Type = Gauge32
_CucsSwSystemStatsHistKernelMemTotalMax_Object = MibTableColumn
cucsSwSystemStatsHistKernelMemTotalMax = _CucsSwSystemStatsHistKernelMemTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 31),
    _CucsSwSystemStatsHistKernelMemTotalMax_Type()
)
cucsSwSystemStatsHistKernelMemTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistKernelMemTotalMax.setStatus("current")
_CucsSwSystemStatsHistKernelMemTotalMin_Type = Gauge32
_CucsSwSystemStatsHistKernelMemTotalMin_Object = MibTableColumn
cucsSwSystemStatsHistKernelMemTotalMin = _CucsSwSystemStatsHistKernelMemTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 29, 1, 32),
    _CucsSwSystemStatsHistKernelMemTotalMin_Type()
)
cucsSwSystemStatsHistKernelMemTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSystemStatsHistKernelMemTotalMin.setStatus("current")
_CucsSwUlanTable_Object = MibTable
cucsSwUlanTable = _CucsSwUlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30)
)
if mibBuilder.loadTexts:
    cucsSwUlanTable.setStatus("current")
_CucsSwUlanEntry_Object = MibTableRow
cucsSwUlanEntry = _CucsSwUlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1)
)
cucsSwUlanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwUlanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwUlanEntry.setStatus("current")
_CucsSwUlanInstanceId_Type = CucsManagedObjectId
_CucsSwUlanInstanceId_Object = MibTableColumn
cucsSwUlanInstanceId = _CucsSwUlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 1),
    _CucsSwUlanInstanceId_Type()
)
cucsSwUlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwUlanInstanceId.setStatus("current")
_CucsSwUlanDn_Type = CucsManagedObjectDn
_CucsSwUlanDn_Object = MibTableColumn
cucsSwUlanDn = _CucsSwUlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 2),
    _CucsSwUlanDn_Type()
)
cucsSwUlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanDn.setStatus("current")
_CucsSwUlanRn_Type = SnmpAdminString
_CucsSwUlanRn_Object = MibTableColumn
cucsSwUlanRn = _CucsSwUlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 3),
    _CucsSwUlanRn_Type()
)
cucsSwUlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanRn.setStatus("current")
_CucsSwUlanEpDn_Type = SnmpAdminString
_CucsSwUlanEpDn_Object = MibTableColumn
cucsSwUlanEpDn = _CucsSwUlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 4),
    _CucsSwUlanEpDn_Type()
)
cucsSwUlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanEpDn.setStatus("current")
_CucsSwUlanId_Type = Gauge32
_CucsSwUlanId_Object = MibTableColumn
cucsSwUlanId = _CucsSwUlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 5),
    _CucsSwUlanId_Type()
)
cucsSwUlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanId.setStatus("current")
_CucsSwUlanIfRole_Type = CucsFabricVnetEpIfRole
_CucsSwUlanIfRole_Object = MibTableColumn
cucsSwUlanIfRole = _CucsSwUlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 6),
    _CucsSwUlanIfRole_Type()
)
cucsSwUlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanIfRole.setStatus("current")
_CucsSwUlanIfType_Type = CucsNetworkVnetEpIfType
_CucsSwUlanIfType_Object = MibTableColumn
cucsSwUlanIfType = _CucsSwUlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 7),
    _CucsSwUlanIfType_Type()
)
cucsSwUlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanIfType.setStatus("current")
_CucsSwUlanLocale_Type = CucsFabricVnetEpLocale
_CucsSwUlanLocale_Object = MibTableColumn
cucsSwUlanLocale = _CucsSwUlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 8),
    _CucsSwUlanLocale_Type()
)
cucsSwUlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanLocale.setStatus("current")
_CucsSwUlanName_Type = SnmpAdminString
_CucsSwUlanName_Object = MibTableColumn
cucsSwUlanName = _CucsSwUlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 9),
    _CucsSwUlanName_Type()
)
cucsSwUlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanName.setStatus("current")
_CucsSwUlanPeerDn_Type = SnmpAdminString
_CucsSwUlanPeerDn_Object = MibTableColumn
cucsSwUlanPeerDn = _CucsSwUlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 10),
    _CucsSwUlanPeerDn_Type()
)
cucsSwUlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanPeerDn.setStatus("current")
_CucsSwUlanPubNwDn_Type = SnmpAdminString
_CucsSwUlanPubNwDn_Object = MibTableColumn
cucsSwUlanPubNwDn = _CucsSwUlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 11),
    _CucsSwUlanPubNwDn_Type()
)
cucsSwUlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanPubNwDn.setStatus("current")
_CucsSwUlanPubNwId_Type = Gauge32
_CucsSwUlanPubNwId_Object = MibTableColumn
cucsSwUlanPubNwId = _CucsSwUlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 12),
    _CucsSwUlanPubNwId_Type()
)
cucsSwUlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanPubNwId.setStatus("current")
_CucsSwUlanPubNwName_Type = SnmpAdminString
_CucsSwUlanPubNwName_Object = MibTableColumn
cucsSwUlanPubNwName = _CucsSwUlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 13),
    _CucsSwUlanPubNwName_Type()
)
cucsSwUlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanPubNwName.setStatus("current")
_CucsSwUlanPurpose_Type = CucsSwUlanPurpose
_CucsSwUlanPurpose_Object = MibTableColumn
cucsSwUlanPurpose = _CucsSwUlanPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 14),
    _CucsSwUlanPurpose_Type()
)
cucsSwUlanPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanPurpose.setStatus("current")
_CucsSwUlanSharing_Type = CucsFabricAVlanSharing
_CucsSwUlanSharing_Object = MibTableColumn
cucsSwUlanSharing = _CucsSwUlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 15),
    _CucsSwUlanSharing_Type()
)
cucsSwUlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanSharing.setStatus("current")
_CucsSwUlanSwitchId_Type = CucsNetworkSwitchId
_CucsSwUlanSwitchId_Object = MibTableColumn
cucsSwUlanSwitchId = _CucsSwUlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 16),
    _CucsSwUlanSwitchId_Type()
)
cucsSwUlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanSwitchId.setStatus("current")
_CucsSwUlanTransport_Type = CucsFabricAVlanTransport
_CucsSwUlanTransport_Object = MibTableColumn
cucsSwUlanTransport = _CucsSwUlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 17),
    _CucsSwUlanTransport_Type()
)
cucsSwUlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanTransport.setStatus("current")
_CucsSwUlanType_Type = CucsFabricAVlanType
_CucsSwUlanType_Object = MibTableColumn
cucsSwUlanType = _CucsSwUlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 18),
    _CucsSwUlanType_Type()
)
cucsSwUlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanType.setStatus("current")
_CucsSwUlanVlanType_Type = CucsFabricEpVlanVlanType
_CucsSwUlanVlanType_Object = MibTableColumn
cucsSwUlanVlanType = _CucsSwUlanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 19),
    _CucsSwUlanVlanType_Type()
)
cucsSwUlanVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanVlanType.setStatus("current")
_CucsSwUlanOperState_Type = CucsFabricVlanOperState
_CucsSwUlanOperState_Object = MibTableColumn
cucsSwUlanOperState = _CucsSwUlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 20),
    _CucsSwUlanOperState_Type()
)
cucsSwUlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanOperState.setStatus("current")
_CucsSwUlanPolicyOwner_Type = CucsFabricVnetEpPolicyOwner
_CucsSwUlanPolicyOwner_Object = MibTableColumn
cucsSwUlanPolicyOwner = _CucsSwUlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 22),
    _CucsSwUlanPolicyOwner_Type()
)
cucsSwUlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanPolicyOwner.setStatus("current")
_CucsSwUlanAssocPrimaryVlanState_Type = CucsFabricVlanAssocPrimaryVlanState
_CucsSwUlanAssocPrimaryVlanState_Object = MibTableColumn
cucsSwUlanAssocPrimaryVlanState = _CucsSwUlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 23),
    _CucsSwUlanAssocPrimaryVlanState_Type()
)
cucsSwUlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanAssocPrimaryVlanState.setStatus("current")
_CucsSwUlanAssocPrimaryVlanSwitchId_Type = CucsFabricAVlanAssocPrimaryVlanSwitchId
_CucsSwUlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cucsSwUlanAssocPrimaryVlanSwitchId = _CucsSwUlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 24),
    _CucsSwUlanAssocPrimaryVlanSwitchId_Type()
)
cucsSwUlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanAssocPrimaryVlanSwitchId.setStatus("current")
_CucsSwUlanOverlapStateForA_Type = CucsFabricVlanOverlapState
_CucsSwUlanOverlapStateForA_Object = MibTableColumn
cucsSwUlanOverlapStateForA = _CucsSwUlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 25),
    _CucsSwUlanOverlapStateForA_Type()
)
cucsSwUlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanOverlapStateForA.setStatus("current")
_CucsSwUlanOverlapStateForB_Type = CucsFabricVlanOverlapState
_CucsSwUlanOverlapStateForB_Object = MibTableColumn
cucsSwUlanOverlapStateForB = _CucsSwUlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 30, 1, 26),
    _CucsSwUlanOverlapStateForB_Type()
)
cucsSwUlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUlanOverlapStateForB.setStatus("current")
_CucsSwUtilityDomainTable_Object = MibTable
cucsSwUtilityDomainTable = _CucsSwUtilityDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31)
)
if mibBuilder.loadTexts:
    cucsSwUtilityDomainTable.setStatus("current")
_CucsSwUtilityDomainEntry_Object = MibTableRow
cucsSwUtilityDomainEntry = _CucsSwUtilityDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1)
)
cucsSwUtilityDomainEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwUtilityDomainInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwUtilityDomainEntry.setStatus("current")
_CucsSwUtilityDomainInstanceId_Type = CucsManagedObjectId
_CucsSwUtilityDomainInstanceId_Object = MibTableColumn
cucsSwUtilityDomainInstanceId = _CucsSwUtilityDomainInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 1),
    _CucsSwUtilityDomainInstanceId_Type()
)
cucsSwUtilityDomainInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainInstanceId.setStatus("current")
_CucsSwUtilityDomainDn_Type = CucsManagedObjectDn
_CucsSwUtilityDomainDn_Object = MibTableColumn
cucsSwUtilityDomainDn = _CucsSwUtilityDomainDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 2),
    _CucsSwUtilityDomainDn_Type()
)
cucsSwUtilityDomainDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainDn.setStatus("current")
_CucsSwUtilityDomainRn_Type = SnmpAdminString
_CucsSwUtilityDomainRn_Object = MibTableColumn
cucsSwUtilityDomainRn = _CucsSwUtilityDomainRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 3),
    _CucsSwUtilityDomainRn_Type()
)
cucsSwUtilityDomainRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainRn.setStatus("current")
_CucsSwUtilityDomainFsmDescr_Type = SnmpAdminString
_CucsSwUtilityDomainFsmDescr_Object = MibTableColumn
cucsSwUtilityDomainFsmDescr = _CucsSwUtilityDomainFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 4),
    _CucsSwUtilityDomainFsmDescr_Type()
)
cucsSwUtilityDomainFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmDescr.setStatus("current")
_CucsSwUtilityDomainFsmPrev_Type = SnmpAdminString
_CucsSwUtilityDomainFsmPrev_Object = MibTableColumn
cucsSwUtilityDomainFsmPrev = _CucsSwUtilityDomainFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 5),
    _CucsSwUtilityDomainFsmPrev_Type()
)
cucsSwUtilityDomainFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmPrev.setStatus("current")
_CucsSwUtilityDomainFsmProgr_Type = Gauge32
_CucsSwUtilityDomainFsmProgr_Object = MibTableColumn
cucsSwUtilityDomainFsmProgr = _CucsSwUtilityDomainFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 6),
    _CucsSwUtilityDomainFsmProgr_Type()
)
cucsSwUtilityDomainFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmProgr.setStatus("current")
_CucsSwUtilityDomainFsmRmtInvErrCode_Type = Gauge32
_CucsSwUtilityDomainFsmRmtInvErrCode_Object = MibTableColumn
cucsSwUtilityDomainFsmRmtInvErrCode = _CucsSwUtilityDomainFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 7),
    _CucsSwUtilityDomainFsmRmtInvErrCode_Type()
)
cucsSwUtilityDomainFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmRmtInvErrCode.setStatus("current")
_CucsSwUtilityDomainFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwUtilityDomainFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwUtilityDomainFsmRmtInvErrDescr = _CucsSwUtilityDomainFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 8),
    _CucsSwUtilityDomainFsmRmtInvErrDescr_Type()
)
cucsSwUtilityDomainFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmRmtInvErrDescr.setStatus("current")
_CucsSwUtilityDomainFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwUtilityDomainFsmRmtInvRslt_Object = MibTableColumn
cucsSwUtilityDomainFsmRmtInvRslt = _CucsSwUtilityDomainFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 9),
    _CucsSwUtilityDomainFsmRmtInvRslt_Type()
)
cucsSwUtilityDomainFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmRmtInvRslt.setStatus("current")
_CucsSwUtilityDomainFsmStageDescr_Type = SnmpAdminString
_CucsSwUtilityDomainFsmStageDescr_Object = MibTableColumn
cucsSwUtilityDomainFsmStageDescr = _CucsSwUtilityDomainFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 10),
    _CucsSwUtilityDomainFsmStageDescr_Type()
)
cucsSwUtilityDomainFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageDescr.setStatus("current")
_CucsSwUtilityDomainFsmStamp_Type = DateAndTime
_CucsSwUtilityDomainFsmStamp_Object = MibTableColumn
cucsSwUtilityDomainFsmStamp = _CucsSwUtilityDomainFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 11),
    _CucsSwUtilityDomainFsmStamp_Type()
)
cucsSwUtilityDomainFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStamp.setStatus("current")
_CucsSwUtilityDomainFsmStatus_Type = SnmpAdminString
_CucsSwUtilityDomainFsmStatus_Object = MibTableColumn
cucsSwUtilityDomainFsmStatus = _CucsSwUtilityDomainFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 12),
    _CucsSwUtilityDomainFsmStatus_Type()
)
cucsSwUtilityDomainFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStatus.setStatus("current")
_CucsSwUtilityDomainFsmTry_Type = Gauge32
_CucsSwUtilityDomainFsmTry_Object = MibTableColumn
cucsSwUtilityDomainFsmTry = _CucsSwUtilityDomainFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 13),
    _CucsSwUtilityDomainFsmTry_Type()
)
cucsSwUtilityDomainFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTry.setStatus("current")
_CucsSwUtilityDomainLocale_Type = CucsSwUtilityDomainLocale
_CucsSwUtilityDomainLocale_Object = MibTableColumn
cucsSwUtilityDomainLocale = _CucsSwUtilityDomainLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 14),
    _CucsSwUtilityDomainLocale_Type()
)
cucsSwUtilityDomainLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainLocale.setStatus("current")
_CucsSwUtilityDomainName_Type = SnmpAdminString
_CucsSwUtilityDomainName_Object = MibTableColumn
cucsSwUtilityDomainName = _CucsSwUtilityDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 15),
    _CucsSwUtilityDomainName_Type()
)
cucsSwUtilityDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainName.setStatus("current")
_CucsSwUtilityDomainSwitchId_Type = CucsNetworkSwitchId
_CucsSwUtilityDomainSwitchId_Object = MibTableColumn
cucsSwUtilityDomainSwitchId = _CucsSwUtilityDomainSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 16),
    _CucsSwUtilityDomainSwitchId_Type()
)
cucsSwUtilityDomainSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainSwitchId.setStatus("current")
_CucsSwUtilityDomainTransport_Type = CucsNetworkTransport
_CucsSwUtilityDomainTransport_Object = MibTableColumn
cucsSwUtilityDomainTransport = _CucsSwUtilityDomainTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 17),
    _CucsSwUtilityDomainTransport_Type()
)
cucsSwUtilityDomainTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainTransport.setStatus("current")
_CucsSwUtilityDomainType_Type = CucsSwUtilityDomainType
_CucsSwUtilityDomainType_Object = MibTableColumn
cucsSwUtilityDomainType = _CucsSwUtilityDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 31, 1, 18),
    _CucsSwUtilityDomainType_Type()
)
cucsSwUtilityDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainType.setStatus("current")
_CucsSwUtilityDomainFsmTaskTable_Object = MibTable
cucsSwUtilityDomainFsmTaskTable = _CucsSwUtilityDomainFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32)
)
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskTable.setStatus("current")
_CucsSwUtilityDomainFsmTaskEntry_Object = MibTableRow
cucsSwUtilityDomainFsmTaskEntry = _CucsSwUtilityDomainFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32, 1)
)
cucsSwUtilityDomainFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwUtilityDomainFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskEntry.setStatus("current")
_CucsSwUtilityDomainFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwUtilityDomainFsmTaskInstanceId_Object = MibTableColumn
cucsSwUtilityDomainFsmTaskInstanceId = _CucsSwUtilityDomainFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32, 1, 1),
    _CucsSwUtilityDomainFsmTaskInstanceId_Type()
)
cucsSwUtilityDomainFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskInstanceId.setStatus("current")
_CucsSwUtilityDomainFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwUtilityDomainFsmTaskDn_Object = MibTableColumn
cucsSwUtilityDomainFsmTaskDn = _CucsSwUtilityDomainFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32, 1, 2),
    _CucsSwUtilityDomainFsmTaskDn_Type()
)
cucsSwUtilityDomainFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskDn.setStatus("current")
_CucsSwUtilityDomainFsmTaskRn_Type = SnmpAdminString
_CucsSwUtilityDomainFsmTaskRn_Object = MibTableColumn
cucsSwUtilityDomainFsmTaskRn = _CucsSwUtilityDomainFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32, 1, 3),
    _CucsSwUtilityDomainFsmTaskRn_Type()
)
cucsSwUtilityDomainFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskRn.setStatus("current")
_CucsSwUtilityDomainFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwUtilityDomainFsmTaskCompletion_Object = MibTableColumn
cucsSwUtilityDomainFsmTaskCompletion = _CucsSwUtilityDomainFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32, 1, 4),
    _CucsSwUtilityDomainFsmTaskCompletion_Type()
)
cucsSwUtilityDomainFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskCompletion.setStatus("current")
_CucsSwUtilityDomainFsmTaskFlags_Type = CucsFsmFlags
_CucsSwUtilityDomainFsmTaskFlags_Object = MibTableColumn
cucsSwUtilityDomainFsmTaskFlags = _CucsSwUtilityDomainFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32, 1, 5),
    _CucsSwUtilityDomainFsmTaskFlags_Type()
)
cucsSwUtilityDomainFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskFlags.setStatus("current")
_CucsSwUtilityDomainFsmTaskItem_Type = CucsSwUtilityDomainFsmTaskItem
_CucsSwUtilityDomainFsmTaskItem_Object = MibTableColumn
cucsSwUtilityDomainFsmTaskItem = _CucsSwUtilityDomainFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32, 1, 6),
    _CucsSwUtilityDomainFsmTaskItem_Type()
)
cucsSwUtilityDomainFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskItem.setStatus("current")
_CucsSwUtilityDomainFsmTaskSeqId_Type = Gauge32
_CucsSwUtilityDomainFsmTaskSeqId_Object = MibTableColumn
cucsSwUtilityDomainFsmTaskSeqId = _CucsSwUtilityDomainFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 32, 1, 7),
    _CucsSwUtilityDomainFsmTaskSeqId_Type()
)
cucsSwUtilityDomainFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTaskSeqId.setStatus("current")
_CucsSwVlanTable_Object = MibTable
cucsSwVlanTable = _CucsSwVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33)
)
if mibBuilder.loadTexts:
    cucsSwVlanTable.setStatus("current")
_CucsSwVlanEntry_Object = MibTableRow
cucsSwVlanEntry = _CucsSwVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1)
)
cucsSwVlanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwVlanEntry.setStatus("current")
_CucsSwVlanInstanceId_Type = CucsManagedObjectId
_CucsSwVlanInstanceId_Object = MibTableColumn
cucsSwVlanInstanceId = _CucsSwVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 1),
    _CucsSwVlanInstanceId_Type()
)
cucsSwVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwVlanInstanceId.setStatus("current")
_CucsSwVlanDn_Type = CucsManagedObjectDn
_CucsSwVlanDn_Object = MibTableColumn
cucsSwVlanDn = _CucsSwVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 2),
    _CucsSwVlanDn_Type()
)
cucsSwVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanDn.setStatus("current")
_CucsSwVlanRn_Type = SnmpAdminString
_CucsSwVlanRn_Object = MibTableColumn
cucsSwVlanRn = _CucsSwVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 3),
    _CucsSwVlanRn_Type()
)
cucsSwVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanRn.setStatus("current")
_CucsSwVlanEpDn_Type = SnmpAdminString
_CucsSwVlanEpDn_Object = MibTableColumn
cucsSwVlanEpDn = _CucsSwVlanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 4),
    _CucsSwVlanEpDn_Type()
)
cucsSwVlanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanEpDn.setStatus("current")
_CucsSwVlanId_Type = Gauge32
_CucsSwVlanId_Object = MibTableColumn
cucsSwVlanId = _CucsSwVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 5),
    _CucsSwVlanId_Type()
)
cucsSwVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanId.setStatus("current")
_CucsSwVlanIfRole_Type = CucsFabricVnetEpIfRole
_CucsSwVlanIfRole_Object = MibTableColumn
cucsSwVlanIfRole = _CucsSwVlanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 6),
    _CucsSwVlanIfRole_Type()
)
cucsSwVlanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanIfRole.setStatus("current")
_CucsSwVlanIfType_Type = CucsNetworkVnetEpIfType
_CucsSwVlanIfType_Object = MibTableColumn
cucsSwVlanIfType = _CucsSwVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 7),
    _CucsSwVlanIfType_Type()
)
cucsSwVlanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanIfType.setStatus("current")
_CucsSwVlanLc_Type = CucsSwVlanLc
_CucsSwVlanLc_Object = MibTableColumn
cucsSwVlanLc = _CucsSwVlanLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 8),
    _CucsSwVlanLc_Type()
)
cucsSwVlanLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanLc.setStatus("current")
_CucsSwVlanLocale_Type = CucsFabricVnetEpLocale
_CucsSwVlanLocale_Object = MibTableColumn
cucsSwVlanLocale = _CucsSwVlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 9),
    _CucsSwVlanLocale_Type()
)
cucsSwVlanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanLocale.setStatus("current")
_CucsSwVlanMonTrafDir_Type = CucsFabricTrafficDirection
_CucsSwVlanMonTrafDir_Object = MibTableColumn
cucsSwVlanMonTrafDir = _CucsSwVlanMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 10),
    _CucsSwVlanMonTrafDir_Type()
)
cucsSwVlanMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanMonTrafDir.setStatus("current")
_CucsSwVlanName_Type = SnmpAdminString
_CucsSwVlanName_Object = MibTableColumn
cucsSwVlanName = _CucsSwVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 11),
    _CucsSwVlanName_Type()
)
cucsSwVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanName.setStatus("current")
_CucsSwVlanPeerDn_Type = SnmpAdminString
_CucsSwVlanPeerDn_Object = MibTableColumn
cucsSwVlanPeerDn = _CucsSwVlanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 12),
    _CucsSwVlanPeerDn_Type()
)
cucsSwVlanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPeerDn.setStatus("current")
_CucsSwVlanPubNwDn_Type = SnmpAdminString
_CucsSwVlanPubNwDn_Object = MibTableColumn
cucsSwVlanPubNwDn = _CucsSwVlanPubNwDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 13),
    _CucsSwVlanPubNwDn_Type()
)
cucsSwVlanPubNwDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPubNwDn.setStatus("current")
_CucsSwVlanPubNwId_Type = Gauge32
_CucsSwVlanPubNwId_Object = MibTableColumn
cucsSwVlanPubNwId = _CucsSwVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 14),
    _CucsSwVlanPubNwId_Type()
)
cucsSwVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPubNwId.setStatus("current")
_CucsSwVlanPubNwName_Type = SnmpAdminString
_CucsSwVlanPubNwName_Object = MibTableColumn
cucsSwVlanPubNwName = _CucsSwVlanPubNwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 15),
    _CucsSwVlanPubNwName_Type()
)
cucsSwVlanPubNwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPubNwName.setStatus("current")
_CucsSwVlanSharing_Type = CucsFabricAVlanSharing
_CucsSwVlanSharing_Object = MibTableColumn
cucsSwVlanSharing = _CucsSwVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 16),
    _CucsSwVlanSharing_Type()
)
cucsSwVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanSharing.setStatus("current")
_CucsSwVlanSwitchId_Type = CucsNetworkSwitchId
_CucsSwVlanSwitchId_Object = MibTableColumn
cucsSwVlanSwitchId = _CucsSwVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 17),
    _CucsSwVlanSwitchId_Type()
)
cucsSwVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanSwitchId.setStatus("current")
_CucsSwVlanTransport_Type = CucsFabricAVlanTransport
_CucsSwVlanTransport_Object = MibTableColumn
cucsSwVlanTransport = _CucsSwVlanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 18),
    _CucsSwVlanTransport_Type()
)
cucsSwVlanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanTransport.setStatus("current")
_CucsSwVlanType_Type = CucsFabricAVlanType
_CucsSwVlanType_Object = MibTableColumn
cucsSwVlanType = _CucsSwVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 19),
    _CucsSwVlanType_Type()
)
cucsSwVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanType.setStatus("current")
_CucsSwVlanVlanType_Type = CucsFabricEpVlanVlanType
_CucsSwVlanVlanType_Object = MibTableColumn
cucsSwVlanVlanType = _CucsSwVlanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 20),
    _CucsSwVlanVlanType_Type()
)
cucsSwVlanVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanVlanType.setStatus("current")
_CucsSwVlanOperState_Type = CucsFabricVlanOperState
_CucsSwVlanOperState_Object = MibTableColumn
cucsSwVlanOperState = _CucsSwVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 21),
    _CucsSwVlanOperState_Type()
)
cucsSwVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanOperState.setStatus("current")
_CucsSwVlanCompressionType_Type = CucsSwVlanCompType
_CucsSwVlanCompressionType_Object = MibTableColumn
cucsSwVlanCompressionType = _CucsSwVlanCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 22),
    _CucsSwVlanCompressionType_Type()
)
cucsSwVlanCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanCompressionType.setStatus("current")
_CucsSwVlanQuerierIpAddrs_Type = InetAddressIPv4
_CucsSwVlanQuerierIpAddrs_Object = MibTableColumn
cucsSwVlanQuerierIpAddrs = _CucsSwVlanQuerierIpAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 23),
    _CucsSwVlanQuerierIpAddrs_Type()
)
cucsSwVlanQuerierIpAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanQuerierIpAddrs.setStatus("current")
_CucsSwVlanSnoopingEnabled_Type = TruthValue
_CucsSwVlanSnoopingEnabled_Object = MibTableColumn
cucsSwVlanSnoopingEnabled = _CucsSwVlanSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 24),
    _CucsSwVlanSnoopingEnabled_Type()
)
cucsSwVlanSnoopingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanSnoopingEnabled.setStatus("current")
_CucsSwVlanPolicyOwner_Type = CucsFabricVnetEpPolicyOwner
_CucsSwVlanPolicyOwner_Object = MibTableColumn
cucsSwVlanPolicyOwner = _CucsSwVlanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 26),
    _CucsSwVlanPolicyOwner_Type()
)
cucsSwVlanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPolicyOwner.setStatus("current")
_CucsSwVlanAssocPrimaryVlanState_Type = CucsFabricVlanAssocPrimaryVlanState
_CucsSwVlanAssocPrimaryVlanState_Object = MibTableColumn
cucsSwVlanAssocPrimaryVlanState = _CucsSwVlanAssocPrimaryVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 27),
    _CucsSwVlanAssocPrimaryVlanState_Type()
)
cucsSwVlanAssocPrimaryVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanAssocPrimaryVlanState.setStatus("current")
_CucsSwVlanAssocPrimaryVlanSwitchId_Type = CucsFabricAVlanAssocPrimaryVlanSwitchId
_CucsSwVlanAssocPrimaryVlanSwitchId_Object = MibTableColumn
cucsSwVlanAssocPrimaryVlanSwitchId = _CucsSwVlanAssocPrimaryVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 28),
    _CucsSwVlanAssocPrimaryVlanSwitchId_Type()
)
cucsSwVlanAssocPrimaryVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanAssocPrimaryVlanSwitchId.setStatus("current")
_CucsSwVlanOverlapStateForA_Type = CucsFabricVlanOverlapState
_CucsSwVlanOverlapStateForA_Object = MibTableColumn
cucsSwVlanOverlapStateForA = _CucsSwVlanOverlapStateForA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 29),
    _CucsSwVlanOverlapStateForA_Type()
)
cucsSwVlanOverlapStateForA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanOverlapStateForA.setStatus("current")
_CucsSwVlanOverlapStateForB_Type = CucsFabricVlanOverlapState
_CucsSwVlanOverlapStateForB_Object = MibTableColumn
cucsSwVlanOverlapStateForB = _CucsSwVlanOverlapStateForB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 30),
    _CucsSwVlanOverlapStateForB_Type()
)
cucsSwVlanOverlapStateForB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanOverlapStateForB.setStatus("current")
_CucsSwVlanSecVlanPerPrimaryVlanCount_Type = Gauge32
_CucsSwVlanSecVlanPerPrimaryVlanCount_Object = MibTableColumn
cucsSwVlanSecVlanPerPrimaryVlanCount = _CucsSwVlanSecVlanPerPrimaryVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 31),
    _CucsSwVlanSecVlanPerPrimaryVlanCount_Type()
)
cucsSwVlanSecVlanPerPrimaryVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanSecVlanPerPrimaryVlanCount.setStatus("current")
_CucsSwVlanSecVlanPerPrimaryVlanCountStatus_Type = CucsNetworkVlanCountStatus
_CucsSwVlanSecVlanPerPrimaryVlanCountStatus_Object = MibTableColumn
cucsSwVlanSecVlanPerPrimaryVlanCountStatus = _CucsSwVlanSecVlanPerPrimaryVlanCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 33, 1, 32),
    _CucsSwVlanSecVlanPerPrimaryVlanCountStatus_Type()
)
cucsSwVlanSecVlanPerPrimaryVlanCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanSecVlanPerPrimaryVlanCountStatus.setStatus("current")
_CucsSwVlanPortNsTable_Object = MibTable
cucsSwVlanPortNsTable = _CucsSwVlanPortNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34)
)
if mibBuilder.loadTexts:
    cucsSwVlanPortNsTable.setStatus("current")
_CucsSwVlanPortNsEntry_Object = MibTableRow
cucsSwVlanPortNsEntry = _CucsSwVlanPortNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1)
)
cucsSwVlanPortNsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwVlanPortNsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwVlanPortNsEntry.setStatus("current")
_CucsSwVlanPortNsInstanceId_Type = CucsManagedObjectId
_CucsSwVlanPortNsInstanceId_Object = MibTableColumn
cucsSwVlanPortNsInstanceId = _CucsSwVlanPortNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 1),
    _CucsSwVlanPortNsInstanceId_Type()
)
cucsSwVlanPortNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsInstanceId.setStatus("current")
_CucsSwVlanPortNsDn_Type = CucsManagedObjectDn
_CucsSwVlanPortNsDn_Object = MibTableColumn
cucsSwVlanPortNsDn = _CucsSwVlanPortNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 2),
    _CucsSwVlanPortNsDn_Type()
)
cucsSwVlanPortNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsDn.setStatus("current")
_CucsSwVlanPortNsRn_Type = SnmpAdminString
_CucsSwVlanPortNsRn_Object = MibTableColumn
cucsSwVlanPortNsRn = _CucsSwVlanPortNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 3),
    _CucsSwVlanPortNsRn_Type()
)
cucsSwVlanPortNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsRn.setStatus("current")
_CucsSwVlanPortNsAccessVlanPortCount_Type = Gauge32
_CucsSwVlanPortNsAccessVlanPortCount_Object = MibTableColumn
cucsSwVlanPortNsAccessVlanPortCount = _CucsSwVlanPortNsAccessVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 4),
    _CucsSwVlanPortNsAccessVlanPortCount_Type()
)
cucsSwVlanPortNsAccessVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsAccessVlanPortCount.setStatus("current")
_CucsSwVlanPortNsAllocStatus_Type = CucsSwVlanPortNsAllocStatus
_CucsSwVlanPortNsAllocStatus_Object = MibTableColumn
cucsSwVlanPortNsAllocStatus = _CucsSwVlanPortNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 5),
    _CucsSwVlanPortNsAllocStatus_Type()
)
cucsSwVlanPortNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsAllocStatus.setStatus("current")
_CucsSwVlanPortNsBorderVlanPortCount_Type = Gauge32
_CucsSwVlanPortNsBorderVlanPortCount_Object = MibTableColumn
cucsSwVlanPortNsBorderVlanPortCount = _CucsSwVlanPortNsBorderVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 6),
    _CucsSwVlanPortNsBorderVlanPortCount_Type()
)
cucsSwVlanPortNsBorderVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsBorderVlanPortCount.setStatus("current")
_CucsSwVlanPortNsLimit_Type = Gauge32
_CucsSwVlanPortNsLimit_Object = MibTableColumn
cucsSwVlanPortNsLimit = _CucsSwVlanPortNsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 7),
    _CucsSwVlanPortNsLimit_Type()
)
cucsSwVlanPortNsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsLimit.setStatus("current")
_CucsSwVlanPortNsSwitchId_Type = CucsNetworkSwitchId
_CucsSwVlanPortNsSwitchId_Object = MibTableColumn
cucsSwVlanPortNsSwitchId = _CucsSwVlanPortNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 8),
    _CucsSwVlanPortNsSwitchId_Type()
)
cucsSwVlanPortNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsSwitchId.setStatus("current")
_CucsSwVlanPortNsConfigStatus_Type = CucsSwConfigStatus
_CucsSwVlanPortNsConfigStatus_Object = MibTableColumn
cucsSwVlanPortNsConfigStatus = _CucsSwVlanPortNsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 9),
    _CucsSwVlanPortNsConfigStatus_Type()
)
cucsSwVlanPortNsConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsConfigStatus.setStatus("current")
_CucsSwVlanPortNsVlanCompOffLimit_Type = Gauge32
_CucsSwVlanPortNsVlanCompOffLimit_Object = MibTableColumn
cucsSwVlanPortNsVlanCompOffLimit = _CucsSwVlanPortNsVlanCompOffLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 10),
    _CucsSwVlanPortNsVlanCompOffLimit_Type()
)
cucsSwVlanPortNsVlanCompOffLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsVlanCompOffLimit.setStatus("current")
_CucsSwVlanPortNsVlanCompOnLimit_Type = Gauge32
_CucsSwVlanPortNsVlanCompOnLimit_Object = MibTableColumn
cucsSwVlanPortNsVlanCompOnLimit = _CucsSwVlanPortNsVlanCompOnLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 11),
    _CucsSwVlanPortNsVlanCompOnLimit_Type()
)
cucsSwVlanPortNsVlanCompOnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsVlanCompOnLimit.setStatus("current")
_CucsSwVlanPortNsTotalVlanPortCount_Type = Gauge32
_CucsSwVlanPortNsTotalVlanPortCount_Object = MibTableColumn
cucsSwVlanPortNsTotalVlanPortCount = _CucsSwVlanPortNsTotalVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 12),
    _CucsSwVlanPortNsTotalVlanPortCount_Type()
)
cucsSwVlanPortNsTotalVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsTotalVlanPortCount.setStatus("current")
_CucsSwVlanPortNsCompressedOptimizationSets_Type = Gauge32
_CucsSwVlanPortNsCompressedOptimizationSets_Object = MibTableColumn
cucsSwVlanPortNsCompressedOptimizationSets = _CucsSwVlanPortNsCompressedOptimizationSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 13),
    _CucsSwVlanPortNsCompressedOptimizationSets_Type()
)
cucsSwVlanPortNsCompressedOptimizationSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsCompressedOptimizationSets.setStatus("current")
_CucsSwVlanPortNsCompressedVlanPortCount_Type = Gauge32
_CucsSwVlanPortNsCompressedVlanPortCount_Object = MibTableColumn
cucsSwVlanPortNsCompressedVlanPortCount = _CucsSwVlanPortNsCompressedVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 14),
    _CucsSwVlanPortNsCompressedVlanPortCount_Type()
)
cucsSwVlanPortNsCompressedVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsCompressedVlanPortCount.setStatus("current")
_CucsSwVlanPortNsTotalOptimizationSets_Type = Gauge32
_CucsSwVlanPortNsTotalOptimizationSets_Object = MibTableColumn
cucsSwVlanPortNsTotalOptimizationSets = _CucsSwVlanPortNsTotalOptimizationSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 15),
    _CucsSwVlanPortNsTotalOptimizationSets_Type()
)
cucsSwVlanPortNsTotalOptimizationSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsTotalOptimizationSets.setStatus("current")
_CucsSwVlanPortNsUncompressedVlanPortCount_Type = Gauge32
_CucsSwVlanPortNsUncompressedVlanPortCount_Object = MibTableColumn
cucsSwVlanPortNsUncompressedVlanPortCount = _CucsSwVlanPortNsUncompressedVlanPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 34, 1, 16),
    _CucsSwVlanPortNsUncompressedVlanPortCount_Type()
)
cucsSwVlanPortNsUncompressedVlanPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsUncompressedVlanPortCount.setStatus("current")
_CucsSwVsanTable_Object = MibTable
cucsSwVsanTable = _CucsSwVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35)
)
if mibBuilder.loadTexts:
    cucsSwVsanTable.setStatus("current")
_CucsSwVsanEntry_Object = MibTableRow
cucsSwVsanEntry = _CucsSwVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1)
)
cucsSwVsanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwVsanEntry.setStatus("current")
_CucsSwVsanInstanceId_Type = CucsManagedObjectId
_CucsSwVsanInstanceId_Object = MibTableColumn
cucsSwVsanInstanceId = _CucsSwVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 1),
    _CucsSwVsanInstanceId_Type()
)
cucsSwVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwVsanInstanceId.setStatus("current")
_CucsSwVsanDn_Type = CucsManagedObjectDn
_CucsSwVsanDn_Object = MibTableColumn
cucsSwVsanDn = _CucsSwVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 2),
    _CucsSwVsanDn_Type()
)
cucsSwVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanDn.setStatus("current")
_CucsSwVsanRn_Type = SnmpAdminString
_CucsSwVsanRn_Object = MibTableColumn
cucsSwVsanRn = _CucsSwVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 3),
    _CucsSwVsanRn_Type()
)
cucsSwVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanRn.setStatus("current")
_CucsSwVsanEpDn_Type = SnmpAdminString
_CucsSwVsanEpDn_Object = MibTableColumn
cucsSwVsanEpDn = _CucsSwVsanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 4),
    _CucsSwVsanEpDn_Type()
)
cucsSwVsanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanEpDn.setStatus("current")
_CucsSwVsanFcoeVlan_Type = Gauge32
_CucsSwVsanFcoeVlan_Object = MibTableColumn
cucsSwVsanFcoeVlan = _CucsSwVsanFcoeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 5),
    _CucsSwVsanFcoeVlan_Type()
)
cucsSwVsanFcoeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanFcoeVlan.setStatus("current")
_CucsSwVsanId_Type = Gauge32
_CucsSwVsanId_Object = MibTableColumn
cucsSwVsanId = _CucsSwVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 6),
    _CucsSwVsanId_Type()
)
cucsSwVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanId.setStatus("current")
_CucsSwVsanIfRole_Type = CucsFabricVnetEpIfRole
_CucsSwVsanIfRole_Object = MibTableColumn
cucsSwVsanIfRole = _CucsSwVsanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 7),
    _CucsSwVsanIfRole_Type()
)
cucsSwVsanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanIfRole.setStatus("current")
_CucsSwVsanIfType_Type = CucsNetworkVnetEpIfType
_CucsSwVsanIfType_Object = MibTableColumn
cucsSwVsanIfType = _CucsSwVsanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 8),
    _CucsSwVsanIfType_Type()
)
cucsSwVsanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanIfType.setStatus("current")
_CucsSwVsanLc_Type = CucsFsmLifecycle
_CucsSwVsanLc_Object = MibTableColumn
cucsSwVsanLc = _CucsSwVsanLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 9),
    _CucsSwVsanLc_Type()
)
cucsSwVsanLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanLc.setStatus("current")
_CucsSwVsanLocale_Type = CucsFabricVnetEpLocale
_CucsSwVsanLocale_Object = MibTableColumn
cucsSwVsanLocale = _CucsSwVsanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 10),
    _CucsSwVsanLocale_Type()
)
cucsSwVsanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanLocale.setStatus("current")
_CucsSwVsanMonTrafDir_Type = CucsFabricTrafficDirection
_CucsSwVsanMonTrafDir_Object = MibTableColumn
cucsSwVsanMonTrafDir = _CucsSwVsanMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 11),
    _CucsSwVsanMonTrafDir_Type()
)
cucsSwVsanMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanMonTrafDir.setStatus("current")
_CucsSwVsanName_Type = SnmpAdminString
_CucsSwVsanName_Object = MibTableColumn
cucsSwVsanName = _CucsSwVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 12),
    _CucsSwVsanName_Type()
)
cucsSwVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanName.setStatus("current")
_CucsSwVsanPeerDn_Type = SnmpAdminString
_CucsSwVsanPeerDn_Object = MibTableColumn
cucsSwVsanPeerDn = _CucsSwVsanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 13),
    _CucsSwVsanPeerDn_Type()
)
cucsSwVsanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanPeerDn.setStatus("current")
_CucsSwVsanSwitchId_Type = CucsNetworkSwitchId
_CucsSwVsanSwitchId_Object = MibTableColumn
cucsSwVsanSwitchId = _CucsSwVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 14),
    _CucsSwVsanSwitchId_Type()
)
cucsSwVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanSwitchId.setStatus("current")
_CucsSwVsanTransport_Type = CucsFabricAVsanTransport
_CucsSwVsanTransport_Object = MibTableColumn
cucsSwVsanTransport = _CucsSwVsanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 15),
    _CucsSwVsanTransport_Type()
)
cucsSwVsanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanTransport.setStatus("current")
_CucsSwVsanType_Type = CucsFabricAVsanType
_CucsSwVsanType_Object = MibTableColumn
cucsSwVsanType = _CucsSwVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 16),
    _CucsSwVsanType_Type()
)
cucsSwVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanType.setStatus("current")
_CucsSwVsanDefaultZoning_Type = CucsFabricDefaultZoningState
_CucsSwVsanDefaultZoning_Object = MibTableColumn
cucsSwVsanDefaultZoning = _CucsSwVsanDefaultZoning_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 17),
    _CucsSwVsanDefaultZoning_Type()
)
cucsSwVsanDefaultZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanDefaultZoning.setStatus("current")
_CucsSwVsanOperState_Type = CucsFabricVsanOperState
_CucsSwVsanOperState_Object = MibTableColumn
cucsSwVsanOperState = _CucsSwVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 18),
    _CucsSwVsanOperState_Type()
)
cucsSwVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanOperState.setStatus("current")
_CucsSwVsanFcZoneSharingMode_Type = CucsFabricFcZoneSharingMode
_CucsSwVsanFcZoneSharingMode_Object = MibTableColumn
cucsSwVsanFcZoneSharingMode = _CucsSwVsanFcZoneSharingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 19),
    _CucsSwVsanFcZoneSharingMode_Type()
)
cucsSwVsanFcZoneSharingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanFcZoneSharingMode.setStatus("current")
_CucsSwVsanFltAggr_Type = Unsigned64
_CucsSwVsanFltAggr_Object = MibTableColumn
cucsSwVsanFltAggr = _CucsSwVsanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 20),
    _CucsSwVsanFltAggr_Type()
)
cucsSwVsanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanFltAggr.setStatus("current")
_CucsSwVsanZoningState_Type = CucsFabricZoningState
_CucsSwVsanZoningState_Object = MibTableColumn
cucsSwVsanZoningState = _CucsSwVsanZoningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 21),
    _CucsSwVsanZoningState_Type()
)
cucsSwVsanZoningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanZoningState.setStatus("current")
_CucsSwVsanPolicyOwner_Type = CucsFabricVnetEpPolicyOwner
_CucsSwVsanPolicyOwner_Object = MibTableColumn
cucsSwVsanPolicyOwner = _CucsSwVsanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 35, 1, 23),
    _CucsSwVsanPolicyOwner_Type()
)
cucsSwVsanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVsanPolicyOwner.setStatus("current")
_CucsSwEthEstcPcTable_Object = MibTable
cucsSwEthEstcPcTable = _CucsSwEthEstcPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36)
)
if mibBuilder.loadTexts:
    cucsSwEthEstcPcTable.setStatus("current")
_CucsSwEthEstcPcEntry_Object = MibTableRow
cucsSwEthEstcPcEntry = _CucsSwEthEstcPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1)
)
cucsSwEthEstcPcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthEstcPcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthEstcPcEntry.setStatus("current")
_CucsSwEthEstcPcInstanceId_Type = CucsManagedObjectId
_CucsSwEthEstcPcInstanceId_Object = MibTableColumn
cucsSwEthEstcPcInstanceId = _CucsSwEthEstcPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 1),
    _CucsSwEthEstcPcInstanceId_Type()
)
cucsSwEthEstcPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcInstanceId.setStatus("current")
_CucsSwEthEstcPcDn_Type = CucsManagedObjectDn
_CucsSwEthEstcPcDn_Object = MibTableColumn
cucsSwEthEstcPcDn = _CucsSwEthEstcPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 2),
    _CucsSwEthEstcPcDn_Type()
)
cucsSwEthEstcPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcDn.setStatus("current")
_CucsSwEthEstcPcRn_Type = SnmpAdminString
_CucsSwEthEstcPcRn_Object = MibTableColumn
cucsSwEthEstcPcRn = _CucsSwEthEstcPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 3),
    _CucsSwEthEstcPcRn_Type()
)
cucsSwEthEstcPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcRn.setStatus("current")
_CucsSwEthEstcPcAdminSpeed_Type = CucsPortEthSpeed
_CucsSwEthEstcPcAdminSpeed_Object = MibTableColumn
cucsSwEthEstcPcAdminSpeed = _CucsSwEthEstcPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 4),
    _CucsSwEthEstcPcAdminSpeed_Type()
)
cucsSwEthEstcPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcAdminSpeed.setStatus("current")
_CucsSwEthEstcPcAdminState_Type = CucsFabricAdminState
_CucsSwEthEstcPcAdminState_Object = MibTableColumn
cucsSwEthEstcPcAdminState = _CucsSwEthEstcPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 5),
    _CucsSwEthEstcPcAdminState_Type()
)
cucsSwEthEstcPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcAdminState.setStatus("current")
_CucsSwEthEstcPcBorderPortId_Type = Gauge32
_CucsSwEthEstcPcBorderPortId_Object = MibTableColumn
cucsSwEthEstcPcBorderPortId = _CucsSwEthEstcPcBorderPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 6),
    _CucsSwEthEstcPcBorderPortId_Type()
)
cucsSwEthEstcPcBorderPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcBorderPortId.setStatus("current")
_CucsSwEthEstcPcBorderSlotId_Type = Gauge32
_CucsSwEthEstcPcBorderSlotId_Object = MibTableColumn
cucsSwEthEstcPcBorderSlotId = _CucsSwEthEstcPcBorderSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 7),
    _CucsSwEthEstcPcBorderSlotId_Type()
)
cucsSwEthEstcPcBorderSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcBorderSlotId.setStatus("current")
_CucsSwEthEstcPcCosValue_Type = Gauge32
_CucsSwEthEstcPcCosValue_Object = MibTableColumn
cucsSwEthEstcPcCosValue = _CucsSwEthEstcPcCosValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 8),
    _CucsSwEthEstcPcCosValue_Type()
)
cucsSwEthEstcPcCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcCosValue.setStatus("current")
_CucsSwEthEstcPcEpDn_Type = SnmpAdminString
_CucsSwEthEstcPcEpDn_Object = MibTableColumn
cucsSwEthEstcPcEpDn = _CucsSwEthEstcPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 9),
    _CucsSwEthEstcPcEpDn_Type()
)
cucsSwEthEstcPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcEpDn.setStatus("current")
_CucsSwEthEstcPcIfRole_Type = CucsSwLanPcIfRole
_CucsSwEthEstcPcIfRole_Object = MibTableColumn
cucsSwEthEstcPcIfRole = _CucsSwEthEstcPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 10),
    _CucsSwEthEstcPcIfRole_Type()
)
cucsSwEthEstcPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcIfRole.setStatus("current")
_CucsSwEthEstcPcIfType_Type = CucsSwCIoEpIfType
_CucsSwEthEstcPcIfType_Object = MibTableColumn
cucsSwEthEstcPcIfType = _CucsSwEthEstcPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 11),
    _CucsSwEthEstcPcIfType_Type()
)
cucsSwEthEstcPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcIfType.setStatus("current")
_CucsSwEthEstcPcLocale_Type = CucsSwBorderPcLocale
_CucsSwEthEstcPcLocale_Object = MibTableColumn
cucsSwEthEstcPcLocale = _CucsSwEthEstcPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 12),
    _CucsSwEthEstcPcLocale_Type()
)
cucsSwEthEstcPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcLocale.setStatus("current")
_CucsSwEthEstcPcMonTrafDir_Type = CucsFabricTrafficDirection
_CucsSwEthEstcPcMonTrafDir_Object = MibTableColumn
cucsSwEthEstcPcMonTrafDir = _CucsSwEthEstcPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 13),
    _CucsSwEthEstcPcMonTrafDir_Type()
)
cucsSwEthEstcPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcMonTrafDir.setStatus("current")
_CucsSwEthEstcPcName_Type = SnmpAdminString
_CucsSwEthEstcPcName_Object = MibTableColumn
cucsSwEthEstcPcName = _CucsSwEthEstcPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 14),
    _CucsSwEthEstcPcName_Type()
)
cucsSwEthEstcPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcName.setStatus("current")
_CucsSwEthEstcPcPeerDn_Type = SnmpAdminString
_CucsSwEthEstcPcPeerDn_Object = MibTableColumn
cucsSwEthEstcPcPeerDn = _CucsSwEthEstcPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 15),
    _CucsSwEthEstcPcPeerDn_Type()
)
cucsSwEthEstcPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcPeerDn.setStatus("current")
_CucsSwEthEstcPcPortId_Type = Gauge32
_CucsSwEthEstcPcPortId_Object = MibTableColumn
cucsSwEthEstcPcPortId = _CucsSwEthEstcPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 16),
    _CucsSwEthEstcPcPortId_Type()
)
cucsSwEthEstcPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcPortId.setStatus("current")
_CucsSwEthEstcPcPortMode_Type = CucsFabricEthEstcPortMode
_CucsSwEthEstcPcPortMode_Object = MibTableColumn
cucsSwEthEstcPcPortMode = _CucsSwEthEstcPcPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 17),
    _CucsSwEthEstcPcPortMode_Type()
)
cucsSwEthEstcPcPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcPortMode.setStatus("current")
_CucsSwEthEstcPcSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthEstcPcSwitchId_Object = MibTableColumn
cucsSwEthEstcPcSwitchId = _CucsSwEthEstcPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 18),
    _CucsSwEthEstcPcSwitchId_Type()
)
cucsSwEthEstcPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcSwitchId.setStatus("current")
_CucsSwEthEstcPcTransport_Type = CucsSwEthEstcPcTransport
_CucsSwEthEstcPcTransport_Object = MibTableColumn
cucsSwEthEstcPcTransport = _CucsSwEthEstcPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 19),
    _CucsSwEthEstcPcTransport_Type()
)
cucsSwEthEstcPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcTransport.setStatus("current")
_CucsSwEthEstcPcType_Type = CucsSwLanPcType
_CucsSwEthEstcPcType_Object = MibTableColumn
cucsSwEthEstcPcType = _CucsSwEthEstcPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 20),
    _CucsSwEthEstcPcType_Type()
)
cucsSwEthEstcPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcType.setStatus("current")
_CucsSwEthEstcPcCdp_Type = CucsNwctrlAdminState
_CucsSwEthEstcPcCdp_Object = MibTableColumn
cucsSwEthEstcPcCdp = _CucsSwEthEstcPcCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 21),
    _CucsSwEthEstcPcCdp_Type()
)
cucsSwEthEstcPcCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcCdp.setStatus("current")
_CucsSwEthEstcPcForgeMac_Type = CucsDpsecForgedTransmit
_CucsSwEthEstcPcForgeMac_Object = MibTableColumn
cucsSwEthEstcPcForgeMac = _CucsSwEthEstcPcForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 22),
    _CucsSwEthEstcPcForgeMac_Type()
)
cucsSwEthEstcPcForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcForgeMac.setStatus("current")
_CucsSwEthEstcPcProtocol_Type = CucsFabricEthPcProtocol
_CucsSwEthEstcPcProtocol_Object = MibTableColumn
cucsSwEthEstcPcProtocol = _CucsSwEthEstcPcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 23),
    _CucsSwEthEstcPcProtocol_Type()
)
cucsSwEthEstcPcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcProtocol.setStatus("current")
_CucsSwEthEstcPcUplinkFailAction_Type = CucsNwctrlLinkFailAction
_CucsSwEthEstcPcUplinkFailAction_Object = MibTableColumn
cucsSwEthEstcPcUplinkFailAction = _CucsSwEthEstcPcUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 24),
    _CucsSwEthEstcPcUplinkFailAction_Type()
)
cucsSwEthEstcPcUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcUplinkFailAction.setStatus("current")
_CucsSwEthEstcPcPriorityFlowCtrl_Type = CucsFlowctrlPriorityPause
_CucsSwEthEstcPcPriorityFlowCtrl_Object = MibTableColumn
cucsSwEthEstcPcPriorityFlowCtrl = _CucsSwEthEstcPcPriorityFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 25),
    _CucsSwEthEstcPcPriorityFlowCtrl_Type()
)
cucsSwEthEstcPcPriorityFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcPriorityFlowCtrl.setStatus("current")
_CucsSwEthEstcPcRecvFlowCtrl_Type = CucsFlowctrlFlowControl
_CucsSwEthEstcPcRecvFlowCtrl_Object = MibTableColumn
cucsSwEthEstcPcRecvFlowCtrl = _CucsSwEthEstcPcRecvFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 26),
    _CucsSwEthEstcPcRecvFlowCtrl_Type()
)
cucsSwEthEstcPcRecvFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcRecvFlowCtrl.setStatus("current")
_CucsSwEthEstcPcSendFlowCtrl_Type = CucsFlowctrlFlowControl
_CucsSwEthEstcPcSendFlowCtrl_Object = MibTableColumn
cucsSwEthEstcPcSendFlowCtrl = _CucsSwEthEstcPcSendFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 27),
    _CucsSwEthEstcPcSendFlowCtrl_Type()
)
cucsSwEthEstcPcSendFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcSendFlowCtrl.setStatus("current")
_CucsSwEthEstcPcLacpFastTimer_Type = TruthValue
_CucsSwEthEstcPcLacpFastTimer_Object = MibTableColumn
cucsSwEthEstcPcLacpFastTimer = _CucsSwEthEstcPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 28),
    _CucsSwEthEstcPcLacpFastTimer_Type()
)
cucsSwEthEstcPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcLacpFastTimer.setStatus("current")
_CucsSwEthEstcPcLacpSuspendIndividual_Type = TruthValue
_CucsSwEthEstcPcLacpSuspendIndividual_Object = MibTableColumn
cucsSwEthEstcPcLacpSuspendIndividual = _CucsSwEthEstcPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 29),
    _CucsSwEthEstcPcLacpSuspendIndividual_Type()
)
cucsSwEthEstcPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcLacpSuspendIndividual.setStatus("current")
_CucsSwEthEstcPcBorderAggrPortId_Type = Gauge32
_CucsSwEthEstcPcBorderAggrPortId_Object = MibTableColumn
cucsSwEthEstcPcBorderAggrPortId = _CucsSwEthEstcPcBorderAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 36, 1, 30),
    _CucsSwEthEstcPcBorderAggrPortId_Type()
)
cucsSwEthEstcPcBorderAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthEstcPcBorderAggrPortId.setStatus("current")
_CucsSwVlanPortNsOverrideTable_Object = MibTable
cucsSwVlanPortNsOverrideTable = _CucsSwVlanPortNsOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 37)
)
if mibBuilder.loadTexts:
    cucsSwVlanPortNsOverrideTable.setStatus("current")
_CucsSwVlanPortNsOverrideEntry_Object = MibTableRow
cucsSwVlanPortNsOverrideEntry = _CucsSwVlanPortNsOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 37, 1)
)
cucsSwVlanPortNsOverrideEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwVlanPortNsOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwVlanPortNsOverrideEntry.setStatus("current")
_CucsSwVlanPortNsOverrideInstanceId_Type = CucsManagedObjectId
_CucsSwVlanPortNsOverrideInstanceId_Object = MibTableColumn
cucsSwVlanPortNsOverrideInstanceId = _CucsSwVlanPortNsOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 37, 1, 1),
    _CucsSwVlanPortNsOverrideInstanceId_Type()
)
cucsSwVlanPortNsOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsOverrideInstanceId.setStatus("current")
_CucsSwVlanPortNsOverrideDn_Type = CucsManagedObjectDn
_CucsSwVlanPortNsOverrideDn_Object = MibTableColumn
cucsSwVlanPortNsOverrideDn = _CucsSwVlanPortNsOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 37, 1, 2),
    _CucsSwVlanPortNsOverrideDn_Type()
)
cucsSwVlanPortNsOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsOverrideDn.setStatus("current")
_CucsSwVlanPortNsOverrideRn_Type = SnmpAdminString
_CucsSwVlanPortNsOverrideRn_Object = MibTableColumn
cucsSwVlanPortNsOverrideRn = _CucsSwVlanPortNsOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 37, 1, 3),
    _CucsSwVlanPortNsOverrideRn_Type()
)
cucsSwVlanPortNsOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsOverrideRn.setStatus("current")
_CucsSwVlanPortNsOverrideLimit_Type = Gauge32
_CucsSwVlanPortNsOverrideLimit_Object = MibTableColumn
cucsSwVlanPortNsOverrideLimit = _CucsSwVlanPortNsOverrideLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 37, 1, 4),
    _CucsSwVlanPortNsOverrideLimit_Type()
)
cucsSwVlanPortNsOverrideLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanPortNsOverrideLimit.setStatus("current")
_CucsSwPhysTable_Object = MibTable
cucsSwPhysTable = _CucsSwPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38)
)
if mibBuilder.loadTexts:
    cucsSwPhysTable.setStatus("current")
_CucsSwPhysEntry_Object = MibTableRow
cucsSwPhysEntry = _CucsSwPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1)
)
cucsSwPhysEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwPhysInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwPhysEntry.setStatus("current")
_CucsSwPhysInstanceId_Type = CucsManagedObjectId
_CucsSwPhysInstanceId_Object = MibTableColumn
cucsSwPhysInstanceId = _CucsSwPhysInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 1),
    _CucsSwPhysInstanceId_Type()
)
cucsSwPhysInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwPhysInstanceId.setStatus("current")
_CucsSwPhysDn_Type = CucsManagedObjectDn
_CucsSwPhysDn_Object = MibTableColumn
cucsSwPhysDn = _CucsSwPhysDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 2),
    _CucsSwPhysDn_Type()
)
cucsSwPhysDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysDn.setStatus("current")
_CucsSwPhysRn_Type = SnmpAdminString
_CucsSwPhysRn_Object = MibTableColumn
cucsSwPhysRn = _CucsSwPhysRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 3),
    _CucsSwPhysRn_Type()
)
cucsSwPhysRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysRn.setStatus("current")
_CucsSwPhysConfMode_Type = CucsSwConfMode
_CucsSwPhysConfMode_Object = MibTableColumn
cucsSwPhysConfMode = _CucsSwPhysConfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 4),
    _CucsSwPhysConfMode_Type()
)
cucsSwPhysConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysConfMode.setStatus("current")
_CucsSwPhysFsmDescr_Type = SnmpAdminString
_CucsSwPhysFsmDescr_Object = MibTableColumn
cucsSwPhysFsmDescr = _CucsSwPhysFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 5),
    _CucsSwPhysFsmDescr_Type()
)
cucsSwPhysFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmDescr.setStatus("current")
_CucsSwPhysFsmPrev_Type = SnmpAdminString
_CucsSwPhysFsmPrev_Object = MibTableColumn
cucsSwPhysFsmPrev = _CucsSwPhysFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 6),
    _CucsSwPhysFsmPrev_Type()
)
cucsSwPhysFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmPrev.setStatus("current")
_CucsSwPhysFsmProgr_Type = Gauge32
_CucsSwPhysFsmProgr_Object = MibTableColumn
cucsSwPhysFsmProgr = _CucsSwPhysFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 7),
    _CucsSwPhysFsmProgr_Type()
)
cucsSwPhysFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmProgr.setStatus("current")
_CucsSwPhysFsmRmtInvErrCode_Type = Gauge32
_CucsSwPhysFsmRmtInvErrCode_Object = MibTableColumn
cucsSwPhysFsmRmtInvErrCode = _CucsSwPhysFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 8),
    _CucsSwPhysFsmRmtInvErrCode_Type()
)
cucsSwPhysFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmRmtInvErrCode.setStatus("current")
_CucsSwPhysFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwPhysFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwPhysFsmRmtInvErrDescr = _CucsSwPhysFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 9),
    _CucsSwPhysFsmRmtInvErrDescr_Type()
)
cucsSwPhysFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmRmtInvErrDescr.setStatus("current")
_CucsSwPhysFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwPhysFsmRmtInvRslt_Object = MibTableColumn
cucsSwPhysFsmRmtInvRslt = _CucsSwPhysFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 10),
    _CucsSwPhysFsmRmtInvRslt_Type()
)
cucsSwPhysFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmRmtInvRslt.setStatus("current")
_CucsSwPhysFsmStageDescr_Type = SnmpAdminString
_CucsSwPhysFsmStageDescr_Object = MibTableColumn
cucsSwPhysFsmStageDescr = _CucsSwPhysFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 11),
    _CucsSwPhysFsmStageDescr_Type()
)
cucsSwPhysFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageDescr.setStatus("current")
_CucsSwPhysFsmStamp_Type = DateAndTime
_CucsSwPhysFsmStamp_Object = MibTableColumn
cucsSwPhysFsmStamp = _CucsSwPhysFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 12),
    _CucsSwPhysFsmStamp_Type()
)
cucsSwPhysFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStamp.setStatus("current")
_CucsSwPhysFsmStatus_Type = SnmpAdminString
_CucsSwPhysFsmStatus_Object = MibTableColumn
cucsSwPhysFsmStatus = _CucsSwPhysFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 13),
    _CucsSwPhysFsmStatus_Type()
)
cucsSwPhysFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStatus.setStatus("current")
_CucsSwPhysFsmTry_Type = Gauge32
_CucsSwPhysFsmTry_Object = MibTableColumn
cucsSwPhysFsmTry = _CucsSwPhysFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 38, 1, 14),
    _CucsSwPhysFsmTry_Type()
)
cucsSwPhysFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmTry.setStatus("current")
_CucsSwPhysEtherEpTable_Object = MibTable
cucsSwPhysEtherEpTable = _CucsSwPhysEtherEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39)
)
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpTable.setStatus("current")
_CucsSwPhysEtherEpEntry_Object = MibTableRow
cucsSwPhysEtherEpEntry = _CucsSwPhysEtherEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1)
)
cucsSwPhysEtherEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwPhysEtherEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpEntry.setStatus("current")
_CucsSwPhysEtherEpInstanceId_Type = CucsManagedObjectId
_CucsSwPhysEtherEpInstanceId_Object = MibTableColumn
cucsSwPhysEtherEpInstanceId = _CucsSwPhysEtherEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 1),
    _CucsSwPhysEtherEpInstanceId_Type()
)
cucsSwPhysEtherEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpInstanceId.setStatus("current")
_CucsSwPhysEtherEpDn_Type = CucsManagedObjectDn
_CucsSwPhysEtherEpDn_Object = MibTableColumn
cucsSwPhysEtherEpDn = _CucsSwPhysEtherEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 2),
    _CucsSwPhysEtherEpDn_Type()
)
cucsSwPhysEtherEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpDn.setStatus("current")
_CucsSwPhysEtherEpRn_Type = SnmpAdminString
_CucsSwPhysEtherEpRn_Object = MibTableColumn
cucsSwPhysEtherEpRn = _CucsSwPhysEtherEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 3),
    _CucsSwPhysEtherEpRn_Type()
)
cucsSwPhysEtherEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpRn.setStatus("current")
_CucsSwPhysEtherEpAdminState_Type = CucsFabricAdminState
_CucsSwPhysEtherEpAdminState_Object = MibTableColumn
cucsSwPhysEtherEpAdminState = _CucsSwPhysEtherEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 4),
    _CucsSwPhysEtherEpAdminState_Type()
)
cucsSwPhysEtherEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpAdminState.setStatus("current")
_CucsSwPhysEtherEpChassisId_Type = Gauge32
_CucsSwPhysEtherEpChassisId_Object = MibTableColumn
cucsSwPhysEtherEpChassisId = _CucsSwPhysEtherEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 5),
    _CucsSwPhysEtherEpChassisId_Type()
)
cucsSwPhysEtherEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpChassisId.setStatus("current")
_CucsSwPhysEtherEpEpDn_Type = SnmpAdminString
_CucsSwPhysEtherEpEpDn_Object = MibTableColumn
cucsSwPhysEtherEpEpDn = _CucsSwPhysEtherEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 6),
    _CucsSwPhysEtherEpEpDn_Type()
)
cucsSwPhysEtherEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpEpDn.setStatus("current")
_CucsSwPhysEtherEpIfRole_Type = CucsNetworkPortRole
_CucsSwPhysEtherEpIfRole_Object = MibTableColumn
cucsSwPhysEtherEpIfRole = _CucsSwPhysEtherEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 7),
    _CucsSwPhysEtherEpIfRole_Type()
)
cucsSwPhysEtherEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpIfRole.setStatus("current")
_CucsSwPhysEtherEpIfType_Type = CucsSwPIoEpIfType
_CucsSwPhysEtherEpIfType_Object = MibTableColumn
cucsSwPhysEtherEpIfType = _CucsSwPhysEtherEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 8),
    _CucsSwPhysEtherEpIfType_Type()
)
cucsSwPhysEtherEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpIfType.setStatus("current")
_CucsSwPhysEtherEpLc_Type = CucsSwPIoEpLc
_CucsSwPhysEtherEpLc_Object = MibTableColumn
cucsSwPhysEtherEpLc = _CucsSwPhysEtherEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 9),
    _CucsSwPhysEtherEpLc_Type()
)
cucsSwPhysEtherEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpLc.setStatus("current")
_CucsSwPhysEtherEpLocale_Type = CucsNetworkLocale
_CucsSwPhysEtherEpLocale_Object = MibTableColumn
cucsSwPhysEtherEpLocale = _CucsSwPhysEtherEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 10),
    _CucsSwPhysEtherEpLocale_Type()
)
cucsSwPhysEtherEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpLocale.setStatus("current")
_CucsSwPhysEtherEpName_Type = SnmpAdminString
_CucsSwPhysEtherEpName_Object = MibTableColumn
cucsSwPhysEtherEpName = _CucsSwPhysEtherEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 11),
    _CucsSwPhysEtherEpName_Type()
)
cucsSwPhysEtherEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpName.setStatus("current")
_CucsSwPhysEtherEpPeerChassisId_Type = Gauge32
_CucsSwPhysEtherEpPeerChassisId_Object = MibTableColumn
cucsSwPhysEtherEpPeerChassisId = _CucsSwPhysEtherEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 12),
    _CucsSwPhysEtherEpPeerChassisId_Type()
)
cucsSwPhysEtherEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpPeerChassisId.setStatus("current")
_CucsSwPhysEtherEpPeerDn_Type = SnmpAdminString
_CucsSwPhysEtherEpPeerDn_Object = MibTableColumn
cucsSwPhysEtherEpPeerDn = _CucsSwPhysEtherEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 13),
    _CucsSwPhysEtherEpPeerDn_Type()
)
cucsSwPhysEtherEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpPeerDn.setStatus("current")
_CucsSwPhysEtherEpPeerPortId_Type = Gauge32
_CucsSwPhysEtherEpPeerPortId_Object = MibTableColumn
cucsSwPhysEtherEpPeerPortId = _CucsSwPhysEtherEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 14),
    _CucsSwPhysEtherEpPeerPortId_Type()
)
cucsSwPhysEtherEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpPeerPortId.setStatus("current")
_CucsSwPhysEtherEpPeerSlotId_Type = Gauge32
_CucsSwPhysEtherEpPeerSlotId_Object = MibTableColumn
cucsSwPhysEtherEpPeerSlotId = _CucsSwPhysEtherEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 15),
    _CucsSwPhysEtherEpPeerSlotId_Type()
)
cucsSwPhysEtherEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpPeerSlotId.setStatus("current")
_CucsSwPhysEtherEpPortId_Type = Gauge32
_CucsSwPhysEtherEpPortId_Object = MibTableColumn
cucsSwPhysEtherEpPortId = _CucsSwPhysEtherEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 16),
    _CucsSwPhysEtherEpPortId_Type()
)
cucsSwPhysEtherEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpPortId.setStatus("current")
_CucsSwPhysEtherEpSlotId_Type = Gauge32
_CucsSwPhysEtherEpSlotId_Object = MibTableColumn
cucsSwPhysEtherEpSlotId = _CucsSwPhysEtherEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 17),
    _CucsSwPhysEtherEpSlotId_Type()
)
cucsSwPhysEtherEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpSlotId.setStatus("current")
_CucsSwPhysEtherEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwPhysEtherEpSwitchId_Object = MibTableColumn
cucsSwPhysEtherEpSwitchId = _CucsSwPhysEtherEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 18),
    _CucsSwPhysEtherEpSwitchId_Type()
)
cucsSwPhysEtherEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpSwitchId.setStatus("current")
_CucsSwPhysEtherEpTransport_Type = CucsNetworkTransport
_CucsSwPhysEtherEpTransport_Object = MibTableColumn
cucsSwPhysEtherEpTransport = _CucsSwPhysEtherEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 19),
    _CucsSwPhysEtherEpTransport_Type()
)
cucsSwPhysEtherEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpTransport.setStatus("current")
_CucsSwPhysEtherEpType_Type = CucsNetworkConnectionType
_CucsSwPhysEtherEpType_Object = MibTableColumn
cucsSwPhysEtherEpType = _CucsSwPhysEtherEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 20),
    _CucsSwPhysEtherEpType_Type()
)
cucsSwPhysEtherEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpType.setStatus("current")
_CucsSwPhysEtherEpAggrPortId_Type = Gauge32
_CucsSwPhysEtherEpAggrPortId_Object = MibTableColumn
cucsSwPhysEtherEpAggrPortId = _CucsSwPhysEtherEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 21),
    _CucsSwPhysEtherEpAggrPortId_Type()
)
cucsSwPhysEtherEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpAggrPortId.setStatus("current")
_CucsSwPhysEtherEpPeerAggrPortId_Type = Gauge32
_CucsSwPhysEtherEpPeerAggrPortId_Object = MibTableColumn
cucsSwPhysEtherEpPeerAggrPortId = _CucsSwPhysEtherEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 22),
    _CucsSwPhysEtherEpPeerAggrPortId_Type()
)
cucsSwPhysEtherEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpPeerAggrPortId.setStatus("current")
_CucsSwPhysEtherEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwPhysEtherEpAutoNegotiate_Object = MibTableColumn
cucsSwPhysEtherEpAutoNegotiate = _CucsSwPhysEtherEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 39, 1, 23),
    _CucsSwPhysEtherEpAutoNegotiate_Type()
)
cucsSwPhysEtherEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysEtherEpAutoNegotiate.setStatus("current")
_CucsSwPhysFcEpTable_Object = MibTable
cucsSwPhysFcEpTable = _CucsSwPhysFcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40)
)
if mibBuilder.loadTexts:
    cucsSwPhysFcEpTable.setStatus("current")
_CucsSwPhysFcEpEntry_Object = MibTableRow
cucsSwPhysFcEpEntry = _CucsSwPhysFcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1)
)
cucsSwPhysFcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwPhysFcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwPhysFcEpEntry.setStatus("current")
_CucsSwPhysFcEpInstanceId_Type = CucsManagedObjectId
_CucsSwPhysFcEpInstanceId_Object = MibTableColumn
cucsSwPhysFcEpInstanceId = _CucsSwPhysFcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 1),
    _CucsSwPhysFcEpInstanceId_Type()
)
cucsSwPhysFcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpInstanceId.setStatus("current")
_CucsSwPhysFcEpDn_Type = CucsManagedObjectDn
_CucsSwPhysFcEpDn_Object = MibTableColumn
cucsSwPhysFcEpDn = _CucsSwPhysFcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 2),
    _CucsSwPhysFcEpDn_Type()
)
cucsSwPhysFcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpDn.setStatus("current")
_CucsSwPhysFcEpRn_Type = SnmpAdminString
_CucsSwPhysFcEpRn_Object = MibTableColumn
cucsSwPhysFcEpRn = _CucsSwPhysFcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 3),
    _CucsSwPhysFcEpRn_Type()
)
cucsSwPhysFcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpRn.setStatus("current")
_CucsSwPhysFcEpAdminState_Type = CucsFabricAdminState
_CucsSwPhysFcEpAdminState_Object = MibTableColumn
cucsSwPhysFcEpAdminState = _CucsSwPhysFcEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 4),
    _CucsSwPhysFcEpAdminState_Type()
)
cucsSwPhysFcEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpAdminState.setStatus("current")
_CucsSwPhysFcEpChassisId_Type = Gauge32
_CucsSwPhysFcEpChassisId_Object = MibTableColumn
cucsSwPhysFcEpChassisId = _CucsSwPhysFcEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 5),
    _CucsSwPhysFcEpChassisId_Type()
)
cucsSwPhysFcEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpChassisId.setStatus("current")
_CucsSwPhysFcEpEpDn_Type = SnmpAdminString
_CucsSwPhysFcEpEpDn_Object = MibTableColumn
cucsSwPhysFcEpEpDn = _CucsSwPhysFcEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 6),
    _CucsSwPhysFcEpEpDn_Type()
)
cucsSwPhysFcEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpEpDn.setStatus("current")
_CucsSwPhysFcEpIfRole_Type = CucsNetworkPortRole
_CucsSwPhysFcEpIfRole_Object = MibTableColumn
cucsSwPhysFcEpIfRole = _CucsSwPhysFcEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 7),
    _CucsSwPhysFcEpIfRole_Type()
)
cucsSwPhysFcEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpIfRole.setStatus("current")
_CucsSwPhysFcEpIfType_Type = CucsSwPIoEpIfType
_CucsSwPhysFcEpIfType_Object = MibTableColumn
cucsSwPhysFcEpIfType = _CucsSwPhysFcEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 8),
    _CucsSwPhysFcEpIfType_Type()
)
cucsSwPhysFcEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpIfType.setStatus("current")
_CucsSwPhysFcEpLc_Type = CucsSwPIoEpLc
_CucsSwPhysFcEpLc_Object = MibTableColumn
cucsSwPhysFcEpLc = _CucsSwPhysFcEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 9),
    _CucsSwPhysFcEpLc_Type()
)
cucsSwPhysFcEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpLc.setStatus("current")
_CucsSwPhysFcEpLocale_Type = CucsNetworkLocale
_CucsSwPhysFcEpLocale_Object = MibTableColumn
cucsSwPhysFcEpLocale = _CucsSwPhysFcEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 10),
    _CucsSwPhysFcEpLocale_Type()
)
cucsSwPhysFcEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpLocale.setStatus("current")
_CucsSwPhysFcEpName_Type = SnmpAdminString
_CucsSwPhysFcEpName_Object = MibTableColumn
cucsSwPhysFcEpName = _CucsSwPhysFcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 11),
    _CucsSwPhysFcEpName_Type()
)
cucsSwPhysFcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpName.setStatus("current")
_CucsSwPhysFcEpPeerChassisId_Type = Gauge32
_CucsSwPhysFcEpPeerChassisId_Object = MibTableColumn
cucsSwPhysFcEpPeerChassisId = _CucsSwPhysFcEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 12),
    _CucsSwPhysFcEpPeerChassisId_Type()
)
cucsSwPhysFcEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpPeerChassisId.setStatus("current")
_CucsSwPhysFcEpPeerDn_Type = SnmpAdminString
_CucsSwPhysFcEpPeerDn_Object = MibTableColumn
cucsSwPhysFcEpPeerDn = _CucsSwPhysFcEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 13),
    _CucsSwPhysFcEpPeerDn_Type()
)
cucsSwPhysFcEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpPeerDn.setStatus("current")
_CucsSwPhysFcEpPeerPortId_Type = Gauge32
_CucsSwPhysFcEpPeerPortId_Object = MibTableColumn
cucsSwPhysFcEpPeerPortId = _CucsSwPhysFcEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 14),
    _CucsSwPhysFcEpPeerPortId_Type()
)
cucsSwPhysFcEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpPeerPortId.setStatus("current")
_CucsSwPhysFcEpPeerSlotId_Type = Gauge32
_CucsSwPhysFcEpPeerSlotId_Object = MibTableColumn
cucsSwPhysFcEpPeerSlotId = _CucsSwPhysFcEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 15),
    _CucsSwPhysFcEpPeerSlotId_Type()
)
cucsSwPhysFcEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpPeerSlotId.setStatus("current")
_CucsSwPhysFcEpPortId_Type = Gauge32
_CucsSwPhysFcEpPortId_Object = MibTableColumn
cucsSwPhysFcEpPortId = _CucsSwPhysFcEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 16),
    _CucsSwPhysFcEpPortId_Type()
)
cucsSwPhysFcEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpPortId.setStatus("current")
_CucsSwPhysFcEpSlotId_Type = Gauge32
_CucsSwPhysFcEpSlotId_Object = MibTableColumn
cucsSwPhysFcEpSlotId = _CucsSwPhysFcEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 17),
    _CucsSwPhysFcEpSlotId_Type()
)
cucsSwPhysFcEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpSlotId.setStatus("current")
_CucsSwPhysFcEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwPhysFcEpSwitchId_Object = MibTableColumn
cucsSwPhysFcEpSwitchId = _CucsSwPhysFcEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 18),
    _CucsSwPhysFcEpSwitchId_Type()
)
cucsSwPhysFcEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpSwitchId.setStatus("current")
_CucsSwPhysFcEpTransport_Type = CucsNetworkTransport
_CucsSwPhysFcEpTransport_Object = MibTableColumn
cucsSwPhysFcEpTransport = _CucsSwPhysFcEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 19),
    _CucsSwPhysFcEpTransport_Type()
)
cucsSwPhysFcEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpTransport.setStatus("current")
_CucsSwPhysFcEpType_Type = CucsNetworkConnectionType
_CucsSwPhysFcEpType_Object = MibTableColumn
cucsSwPhysFcEpType = _CucsSwPhysFcEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 20),
    _CucsSwPhysFcEpType_Type()
)
cucsSwPhysFcEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpType.setStatus("current")
_CucsSwPhysFcEpAggrPortId_Type = Gauge32
_CucsSwPhysFcEpAggrPortId_Object = MibTableColumn
cucsSwPhysFcEpAggrPortId = _CucsSwPhysFcEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 21),
    _CucsSwPhysFcEpAggrPortId_Type()
)
cucsSwPhysFcEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpAggrPortId.setStatus("current")
_CucsSwPhysFcEpPeerAggrPortId_Type = Gauge32
_CucsSwPhysFcEpPeerAggrPortId_Object = MibTableColumn
cucsSwPhysFcEpPeerAggrPortId = _CucsSwPhysFcEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 22),
    _CucsSwPhysFcEpPeerAggrPortId_Type()
)
cucsSwPhysFcEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpPeerAggrPortId.setStatus("current")
_CucsSwPhysFcEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwPhysFcEpAutoNegotiate_Object = MibTableColumn
cucsSwPhysFcEpAutoNegotiate = _CucsSwPhysFcEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 40, 1, 23),
    _CucsSwPhysFcEpAutoNegotiate_Type()
)
cucsSwPhysFcEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFcEpAutoNegotiate.setStatus("current")
_CucsSwPhysFsmTaskTable_Object = MibTable
cucsSwPhysFsmTaskTable = _CucsSwPhysFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41)
)
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskTable.setStatus("current")
_CucsSwPhysFsmTaskEntry_Object = MibTableRow
cucsSwPhysFsmTaskEntry = _CucsSwPhysFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41, 1)
)
cucsSwPhysFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwPhysFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskEntry.setStatus("current")
_CucsSwPhysFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwPhysFsmTaskInstanceId_Object = MibTableColumn
cucsSwPhysFsmTaskInstanceId = _CucsSwPhysFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41, 1, 1),
    _CucsSwPhysFsmTaskInstanceId_Type()
)
cucsSwPhysFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskInstanceId.setStatus("current")
_CucsSwPhysFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwPhysFsmTaskDn_Object = MibTableColumn
cucsSwPhysFsmTaskDn = _CucsSwPhysFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41, 1, 2),
    _CucsSwPhysFsmTaskDn_Type()
)
cucsSwPhysFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskDn.setStatus("current")
_CucsSwPhysFsmTaskRn_Type = SnmpAdminString
_CucsSwPhysFsmTaskRn_Object = MibTableColumn
cucsSwPhysFsmTaskRn = _CucsSwPhysFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41, 1, 3),
    _CucsSwPhysFsmTaskRn_Type()
)
cucsSwPhysFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskRn.setStatus("current")
_CucsSwPhysFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwPhysFsmTaskCompletion_Object = MibTableColumn
cucsSwPhysFsmTaskCompletion = _CucsSwPhysFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41, 1, 4),
    _CucsSwPhysFsmTaskCompletion_Type()
)
cucsSwPhysFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskCompletion.setStatus("current")
_CucsSwPhysFsmTaskFlags_Type = CucsFsmFlags
_CucsSwPhysFsmTaskFlags_Object = MibTableColumn
cucsSwPhysFsmTaskFlags = _CucsSwPhysFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41, 1, 5),
    _CucsSwPhysFsmTaskFlags_Type()
)
cucsSwPhysFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskFlags.setStatus("current")
_CucsSwPhysFsmTaskItem_Type = CucsSwPhysFsmTaskItem
_CucsSwPhysFsmTaskItem_Object = MibTableColumn
cucsSwPhysFsmTaskItem = _CucsSwPhysFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41, 1, 6),
    _CucsSwPhysFsmTaskItem_Type()
)
cucsSwPhysFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskItem.setStatus("current")
_CucsSwPhysFsmTaskSeqId_Type = Gauge32
_CucsSwPhysFsmTaskSeqId_Object = MibTableColumn
cucsSwPhysFsmTaskSeqId = _CucsSwPhysFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 41, 1, 7),
    _CucsSwPhysFsmTaskSeqId_Type()
)
cucsSwPhysFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmTaskSeqId.setStatus("current")
_CucsSwAccessDomainFsmTable_Object = MibTable
cucsSwAccessDomainFsmTable = _CucsSwAccessDomainFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42)
)
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmTable.setStatus("current")
_CucsSwAccessDomainFsmEntry_Object = MibTableRow
cucsSwAccessDomainFsmEntry = _CucsSwAccessDomainFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1)
)
cucsSwAccessDomainFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwAccessDomainFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmEntry.setStatus("current")
_CucsSwAccessDomainFsmInstanceId_Type = CucsManagedObjectId
_CucsSwAccessDomainFsmInstanceId_Object = MibTableColumn
cucsSwAccessDomainFsmInstanceId = _CucsSwAccessDomainFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 1),
    _CucsSwAccessDomainFsmInstanceId_Type()
)
cucsSwAccessDomainFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmInstanceId.setStatus("current")
_CucsSwAccessDomainFsmDn_Type = CucsManagedObjectDn
_CucsSwAccessDomainFsmDn_Object = MibTableColumn
cucsSwAccessDomainFsmDn = _CucsSwAccessDomainFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 2),
    _CucsSwAccessDomainFsmDn_Type()
)
cucsSwAccessDomainFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmDn.setStatus("current")
_CucsSwAccessDomainFsmRn_Type = SnmpAdminString
_CucsSwAccessDomainFsmRn_Object = MibTableColumn
cucsSwAccessDomainFsmRn = _CucsSwAccessDomainFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 3),
    _CucsSwAccessDomainFsmRn_Type()
)
cucsSwAccessDomainFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmRn.setStatus("current")
_CucsSwAccessDomainFsmCompletionTime_Type = DateAndTime
_CucsSwAccessDomainFsmCompletionTime_Object = MibTableColumn
cucsSwAccessDomainFsmCompletionTime = _CucsSwAccessDomainFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 4),
    _CucsSwAccessDomainFsmCompletionTime_Type()
)
cucsSwAccessDomainFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmCompletionTime.setStatus("current")
_CucsSwAccessDomainFsmCurrentFsm_Type = CucsSwAccessDomainFsmCurrentFsm
_CucsSwAccessDomainFsmCurrentFsm_Object = MibTableColumn
cucsSwAccessDomainFsmCurrentFsm = _CucsSwAccessDomainFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 5),
    _CucsSwAccessDomainFsmCurrentFsm_Type()
)
cucsSwAccessDomainFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmCurrentFsm.setStatus("current")
_CucsSwAccessDomainFsmDescrData_Type = SnmpAdminString
_CucsSwAccessDomainFsmDescrData_Object = MibTableColumn
cucsSwAccessDomainFsmDescrData = _CucsSwAccessDomainFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 6),
    _CucsSwAccessDomainFsmDescrData_Type()
)
cucsSwAccessDomainFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmDescrData.setStatus("current")
_CucsSwAccessDomainFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwAccessDomainFsmFsmStatus_Object = MibTableColumn
cucsSwAccessDomainFsmFsmStatus = _CucsSwAccessDomainFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 7),
    _CucsSwAccessDomainFsmFsmStatus_Type()
)
cucsSwAccessDomainFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmFsmStatus.setStatus("current")
_CucsSwAccessDomainFsmProgress_Type = Gauge32
_CucsSwAccessDomainFsmProgress_Object = MibTableColumn
cucsSwAccessDomainFsmProgress = _CucsSwAccessDomainFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 8),
    _CucsSwAccessDomainFsmProgress_Type()
)
cucsSwAccessDomainFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmProgress.setStatus("current")
_CucsSwAccessDomainFsmRmtErrCode_Type = Gauge32
_CucsSwAccessDomainFsmRmtErrCode_Object = MibTableColumn
cucsSwAccessDomainFsmRmtErrCode = _CucsSwAccessDomainFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 9),
    _CucsSwAccessDomainFsmRmtErrCode_Type()
)
cucsSwAccessDomainFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmRmtErrCode.setStatus("current")
_CucsSwAccessDomainFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwAccessDomainFsmRmtErrDescr_Object = MibTableColumn
cucsSwAccessDomainFsmRmtErrDescr = _CucsSwAccessDomainFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 10),
    _CucsSwAccessDomainFsmRmtErrDescr_Type()
)
cucsSwAccessDomainFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmRmtErrDescr.setStatus("current")
_CucsSwAccessDomainFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwAccessDomainFsmRmtRslt_Object = MibTableColumn
cucsSwAccessDomainFsmRmtRslt = _CucsSwAccessDomainFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 42, 1, 11),
    _CucsSwAccessDomainFsmRmtRslt_Type()
)
cucsSwAccessDomainFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmRmtRslt.setStatus("current")
_CucsSwAccessDomainFsmStageTable_Object = MibTable
cucsSwAccessDomainFsmStageTable = _CucsSwAccessDomainFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43)
)
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageTable.setStatus("current")
_CucsSwAccessDomainFsmStageEntry_Object = MibTableRow
cucsSwAccessDomainFsmStageEntry = _CucsSwAccessDomainFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1)
)
cucsSwAccessDomainFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwAccessDomainFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageEntry.setStatus("current")
_CucsSwAccessDomainFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwAccessDomainFsmStageInstanceId_Object = MibTableColumn
cucsSwAccessDomainFsmStageInstanceId = _CucsSwAccessDomainFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 1),
    _CucsSwAccessDomainFsmStageInstanceId_Type()
)
cucsSwAccessDomainFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageInstanceId.setStatus("current")
_CucsSwAccessDomainFsmStageDn_Type = CucsManagedObjectDn
_CucsSwAccessDomainFsmStageDn_Object = MibTableColumn
cucsSwAccessDomainFsmStageDn = _CucsSwAccessDomainFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 2),
    _CucsSwAccessDomainFsmStageDn_Type()
)
cucsSwAccessDomainFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageDn.setStatus("current")
_CucsSwAccessDomainFsmStageRn_Type = SnmpAdminString
_CucsSwAccessDomainFsmStageRn_Object = MibTableColumn
cucsSwAccessDomainFsmStageRn = _CucsSwAccessDomainFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 3),
    _CucsSwAccessDomainFsmStageRn_Type()
)
cucsSwAccessDomainFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageRn.setStatus("current")
_CucsSwAccessDomainFsmStageDescrData_Type = SnmpAdminString
_CucsSwAccessDomainFsmStageDescrData_Object = MibTableColumn
cucsSwAccessDomainFsmStageDescrData = _CucsSwAccessDomainFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 4),
    _CucsSwAccessDomainFsmStageDescrData_Type()
)
cucsSwAccessDomainFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageDescrData.setStatus("current")
_CucsSwAccessDomainFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwAccessDomainFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwAccessDomainFsmStageLastUpdateTime = _CucsSwAccessDomainFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 5),
    _CucsSwAccessDomainFsmStageLastUpdateTime_Type()
)
cucsSwAccessDomainFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageLastUpdateTime.setStatus("current")
_CucsSwAccessDomainFsmStageName_Type = CucsSwAccessDomainFsmStageName
_CucsSwAccessDomainFsmStageName_Object = MibTableColumn
cucsSwAccessDomainFsmStageName = _CucsSwAccessDomainFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 6),
    _CucsSwAccessDomainFsmStageName_Type()
)
cucsSwAccessDomainFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageName.setStatus("current")
_CucsSwAccessDomainFsmStageOrder_Type = Gauge32
_CucsSwAccessDomainFsmStageOrder_Object = MibTableColumn
cucsSwAccessDomainFsmStageOrder = _CucsSwAccessDomainFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 7),
    _CucsSwAccessDomainFsmStageOrder_Type()
)
cucsSwAccessDomainFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageOrder.setStatus("current")
_CucsSwAccessDomainFsmStageRetry_Type = Gauge32
_CucsSwAccessDomainFsmStageRetry_Object = MibTableColumn
cucsSwAccessDomainFsmStageRetry = _CucsSwAccessDomainFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 8),
    _CucsSwAccessDomainFsmStageRetry_Type()
)
cucsSwAccessDomainFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageRetry.setStatus("current")
_CucsSwAccessDomainFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwAccessDomainFsmStageStageStatus_Object = MibTableColumn
cucsSwAccessDomainFsmStageStageStatus = _CucsSwAccessDomainFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 43, 1, 9),
    _CucsSwAccessDomainFsmStageStageStatus_Type()
)
cucsSwAccessDomainFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwAccessDomainFsmStageStageStatus.setStatus("current")
_CucsSwCardEnvStatsTable_Object = MibTable
cucsSwCardEnvStatsTable = _CucsSwCardEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44)
)
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsTable.setStatus("current")
_CucsSwCardEnvStatsEntry_Object = MibTableRow
cucsSwCardEnvStatsEntry = _CucsSwCardEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1)
)
cucsSwCardEnvStatsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwCardEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsEntry.setStatus("current")
_CucsSwCardEnvStatsInstanceId_Type = CucsManagedObjectId
_CucsSwCardEnvStatsInstanceId_Object = MibTableColumn
cucsSwCardEnvStatsInstanceId = _CucsSwCardEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 1),
    _CucsSwCardEnvStatsInstanceId_Type()
)
cucsSwCardEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsInstanceId.setStatus("current")
_CucsSwCardEnvStatsDn_Type = CucsManagedObjectDn
_CucsSwCardEnvStatsDn_Object = MibTableColumn
cucsSwCardEnvStatsDn = _CucsSwCardEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 2),
    _CucsSwCardEnvStatsDn_Type()
)
cucsSwCardEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsDn.setStatus("current")
_CucsSwCardEnvStatsRn_Type = SnmpAdminString
_CucsSwCardEnvStatsRn_Object = MibTableColumn
cucsSwCardEnvStatsRn = _CucsSwCardEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 3),
    _CucsSwCardEnvStatsRn_Type()
)
cucsSwCardEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsRn.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet1_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet1_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet1 = _CucsSwCardEnvStatsSlotOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 4),
    _CucsSwCardEnvStatsSlotOutlet1_Type()
)
cucsSwCardEnvStatsSlotOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet1.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet1Avg_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet1Avg_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet1Avg = _CucsSwCardEnvStatsSlotOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 5),
    _CucsSwCardEnvStatsSlotOutlet1Avg_Type()
)
cucsSwCardEnvStatsSlotOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet1Avg.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet1Max_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet1Max_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet1Max = _CucsSwCardEnvStatsSlotOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 6),
    _CucsSwCardEnvStatsSlotOutlet1Max_Type()
)
cucsSwCardEnvStatsSlotOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet1Max.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet1Min_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet1Min_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet1Min = _CucsSwCardEnvStatsSlotOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 7),
    _CucsSwCardEnvStatsSlotOutlet1Min_Type()
)
cucsSwCardEnvStatsSlotOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet1Min.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet2_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet2_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet2 = _CucsSwCardEnvStatsSlotOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 8),
    _CucsSwCardEnvStatsSlotOutlet2_Type()
)
cucsSwCardEnvStatsSlotOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet2.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet2Avg_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet2Avg_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet2Avg = _CucsSwCardEnvStatsSlotOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 9),
    _CucsSwCardEnvStatsSlotOutlet2Avg_Type()
)
cucsSwCardEnvStatsSlotOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet2Avg.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet2Max_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet2Max_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet2Max = _CucsSwCardEnvStatsSlotOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 10),
    _CucsSwCardEnvStatsSlotOutlet2Max_Type()
)
cucsSwCardEnvStatsSlotOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet2Max.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet2Min_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet2Min_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet2Min = _CucsSwCardEnvStatsSlotOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 11),
    _CucsSwCardEnvStatsSlotOutlet2Min_Type()
)
cucsSwCardEnvStatsSlotOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet2Min.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet3_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet3_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet3 = _CucsSwCardEnvStatsSlotOutlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 12),
    _CucsSwCardEnvStatsSlotOutlet3_Type()
)
cucsSwCardEnvStatsSlotOutlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet3.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet3Avg_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet3Avg_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet3Avg = _CucsSwCardEnvStatsSlotOutlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 13),
    _CucsSwCardEnvStatsSlotOutlet3Avg_Type()
)
cucsSwCardEnvStatsSlotOutlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet3Avg.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet3Max_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet3Max_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet3Max = _CucsSwCardEnvStatsSlotOutlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 14),
    _CucsSwCardEnvStatsSlotOutlet3Max_Type()
)
cucsSwCardEnvStatsSlotOutlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet3Max.setStatus("current")
_CucsSwCardEnvStatsSlotOutlet3Min_Type = Integer32
_CucsSwCardEnvStatsSlotOutlet3Min_Object = MibTableColumn
cucsSwCardEnvStatsSlotOutlet3Min = _CucsSwCardEnvStatsSlotOutlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 15),
    _CucsSwCardEnvStatsSlotOutlet3Min_Type()
)
cucsSwCardEnvStatsSlotOutlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSlotOutlet3Min.setStatus("current")
_CucsSwCardEnvStatsIntervals_Type = Gauge32
_CucsSwCardEnvStatsIntervals_Object = MibTableColumn
cucsSwCardEnvStatsIntervals = _CucsSwCardEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 16),
    _CucsSwCardEnvStatsIntervals_Type()
)
cucsSwCardEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsIntervals.setStatus("current")
_CucsSwCardEnvStatsSuspect_Type = TruthValue
_CucsSwCardEnvStatsSuspect_Object = MibTableColumn
cucsSwCardEnvStatsSuspect = _CucsSwCardEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 17),
    _CucsSwCardEnvStatsSuspect_Type()
)
cucsSwCardEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsSuspect.setStatus("current")
_CucsSwCardEnvStatsThresholded_Type = CucsSwCardEnvStatsThresholded
_CucsSwCardEnvStatsThresholded_Object = MibTableColumn
cucsSwCardEnvStatsThresholded = _CucsSwCardEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 18),
    _CucsSwCardEnvStatsThresholded_Type()
)
cucsSwCardEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsThresholded.setStatus("current")
_CucsSwCardEnvStatsTimeCollected_Type = DateAndTime
_CucsSwCardEnvStatsTimeCollected_Object = MibTableColumn
cucsSwCardEnvStatsTimeCollected = _CucsSwCardEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 19),
    _CucsSwCardEnvStatsTimeCollected_Type()
)
cucsSwCardEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsTimeCollected.setStatus("current")
_CucsSwCardEnvStatsUpdate_Type = Gauge32
_CucsSwCardEnvStatsUpdate_Object = MibTableColumn
cucsSwCardEnvStatsUpdate = _CucsSwCardEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 44, 1, 20),
    _CucsSwCardEnvStatsUpdate_Type()
)
cucsSwCardEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsUpdate.setStatus("current")
_CucsSwCardEnvStatsHistTable_Object = MibTable
cucsSwCardEnvStatsHistTable = _CucsSwCardEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45)
)
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistTable.setStatus("current")
_CucsSwCardEnvStatsHistEntry_Object = MibTableRow
cucsSwCardEnvStatsHistEntry = _CucsSwCardEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1)
)
cucsSwCardEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwCardEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistEntry.setStatus("current")
_CucsSwCardEnvStatsHistInstanceId_Type = CucsManagedObjectId
_CucsSwCardEnvStatsHistInstanceId_Object = MibTableColumn
cucsSwCardEnvStatsHistInstanceId = _CucsSwCardEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 1),
    _CucsSwCardEnvStatsHistInstanceId_Type()
)
cucsSwCardEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistInstanceId.setStatus("current")
_CucsSwCardEnvStatsHistDn_Type = CucsManagedObjectDn
_CucsSwCardEnvStatsHistDn_Object = MibTableColumn
cucsSwCardEnvStatsHistDn = _CucsSwCardEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 2),
    _CucsSwCardEnvStatsHistDn_Type()
)
cucsSwCardEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistDn.setStatus("current")
_CucsSwCardEnvStatsHistRn_Type = SnmpAdminString
_CucsSwCardEnvStatsHistRn_Object = MibTableColumn
cucsSwCardEnvStatsHistRn = _CucsSwCardEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 3),
    _CucsSwCardEnvStatsHistRn_Type()
)
cucsSwCardEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistRn.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet1_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet1_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet1 = _CucsSwCardEnvStatsHistSlotOutlet1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 4),
    _CucsSwCardEnvStatsHistSlotOutlet1_Type()
)
cucsSwCardEnvStatsHistSlotOutlet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet1.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet1Avg_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet1Avg_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet1Avg = _CucsSwCardEnvStatsHistSlotOutlet1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 5),
    _CucsSwCardEnvStatsHistSlotOutlet1Avg_Type()
)
cucsSwCardEnvStatsHistSlotOutlet1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet1Avg.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet1Max_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet1Max_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet1Max = _CucsSwCardEnvStatsHistSlotOutlet1Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 6),
    _CucsSwCardEnvStatsHistSlotOutlet1Max_Type()
)
cucsSwCardEnvStatsHistSlotOutlet1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet1Max.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet1Min_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet1Min_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet1Min = _CucsSwCardEnvStatsHistSlotOutlet1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 7),
    _CucsSwCardEnvStatsHistSlotOutlet1Min_Type()
)
cucsSwCardEnvStatsHistSlotOutlet1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet1Min.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet2_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet2_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet2 = _CucsSwCardEnvStatsHistSlotOutlet2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 8),
    _CucsSwCardEnvStatsHistSlotOutlet2_Type()
)
cucsSwCardEnvStatsHistSlotOutlet2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet2.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet2Avg_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet2Avg_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet2Avg = _CucsSwCardEnvStatsHistSlotOutlet2Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 9),
    _CucsSwCardEnvStatsHistSlotOutlet2Avg_Type()
)
cucsSwCardEnvStatsHistSlotOutlet2Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet2Avg.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet2Max_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet2Max_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet2Max = _CucsSwCardEnvStatsHistSlotOutlet2Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 10),
    _CucsSwCardEnvStatsHistSlotOutlet2Max_Type()
)
cucsSwCardEnvStatsHistSlotOutlet2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet2Max.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet2Min_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet2Min_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet2Min = _CucsSwCardEnvStatsHistSlotOutlet2Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 11),
    _CucsSwCardEnvStatsHistSlotOutlet2Min_Type()
)
cucsSwCardEnvStatsHistSlotOutlet2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet2Min.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet3_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet3_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet3 = _CucsSwCardEnvStatsHistSlotOutlet3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 12),
    _CucsSwCardEnvStatsHistSlotOutlet3_Type()
)
cucsSwCardEnvStatsHistSlotOutlet3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet3.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet3Avg_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet3Avg_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet3Avg = _CucsSwCardEnvStatsHistSlotOutlet3Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 13),
    _CucsSwCardEnvStatsHistSlotOutlet3Avg_Type()
)
cucsSwCardEnvStatsHistSlotOutlet3Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet3Avg.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet3Max_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet3Max_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet3Max = _CucsSwCardEnvStatsHistSlotOutlet3Max_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 14),
    _CucsSwCardEnvStatsHistSlotOutlet3Max_Type()
)
cucsSwCardEnvStatsHistSlotOutlet3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet3Max.setStatus("current")
_CucsSwCardEnvStatsHistSlotOutlet3Min_Type = Integer32
_CucsSwCardEnvStatsHistSlotOutlet3Min_Object = MibTableColumn
cucsSwCardEnvStatsHistSlotOutlet3Min = _CucsSwCardEnvStatsHistSlotOutlet3Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 15),
    _CucsSwCardEnvStatsHistSlotOutlet3Min_Type()
)
cucsSwCardEnvStatsHistSlotOutlet3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSlotOutlet3Min.setStatus("current")
_CucsSwCardEnvStatsHistId_Type = Unsigned64
_CucsSwCardEnvStatsHistId_Object = MibTableColumn
cucsSwCardEnvStatsHistId = _CucsSwCardEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 16),
    _CucsSwCardEnvStatsHistId_Type()
)
cucsSwCardEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistId.setStatus("current")
_CucsSwCardEnvStatsHistMostRecent_Type = TruthValue
_CucsSwCardEnvStatsHistMostRecent_Object = MibTableColumn
cucsSwCardEnvStatsHistMostRecent = _CucsSwCardEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 17),
    _CucsSwCardEnvStatsHistMostRecent_Type()
)
cucsSwCardEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistMostRecent.setStatus("current")
_CucsSwCardEnvStatsHistSuspect_Type = TruthValue
_CucsSwCardEnvStatsHistSuspect_Object = MibTableColumn
cucsSwCardEnvStatsHistSuspect = _CucsSwCardEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 18),
    _CucsSwCardEnvStatsHistSuspect_Type()
)
cucsSwCardEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistSuspect.setStatus("current")
_CucsSwCardEnvStatsHistThresholded_Type = CucsSwCardEnvStatsHistThresholded
_CucsSwCardEnvStatsHistThresholded_Object = MibTableColumn
cucsSwCardEnvStatsHistThresholded = _CucsSwCardEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 19),
    _CucsSwCardEnvStatsHistThresholded_Type()
)
cucsSwCardEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistThresholded.setStatus("current")
_CucsSwCardEnvStatsHistTimeCollected_Type = DateAndTime
_CucsSwCardEnvStatsHistTimeCollected_Object = MibTableColumn
cucsSwCardEnvStatsHistTimeCollected = _CucsSwCardEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 45, 1, 20),
    _CucsSwCardEnvStatsHistTimeCollected_Type()
)
cucsSwCardEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCardEnvStatsHistTimeCollected.setStatus("current")
_CucsSwEthLanBorderFsmTable_Object = MibTable
cucsSwEthLanBorderFsmTable = _CucsSwEthLanBorderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46)
)
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmTable.setStatus("current")
_CucsSwEthLanBorderFsmEntry_Object = MibTableRow
cucsSwEthLanBorderFsmEntry = _CucsSwEthLanBorderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1)
)
cucsSwEthLanBorderFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanBorderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmEntry.setStatus("current")
_CucsSwEthLanBorderFsmInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanBorderFsmInstanceId_Object = MibTableColumn
cucsSwEthLanBorderFsmInstanceId = _CucsSwEthLanBorderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 1),
    _CucsSwEthLanBorderFsmInstanceId_Type()
)
cucsSwEthLanBorderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmInstanceId.setStatus("current")
_CucsSwEthLanBorderFsmDn_Type = CucsManagedObjectDn
_CucsSwEthLanBorderFsmDn_Object = MibTableColumn
cucsSwEthLanBorderFsmDn = _CucsSwEthLanBorderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 2),
    _CucsSwEthLanBorderFsmDn_Type()
)
cucsSwEthLanBorderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmDn.setStatus("current")
_CucsSwEthLanBorderFsmRn_Type = SnmpAdminString
_CucsSwEthLanBorderFsmRn_Object = MibTableColumn
cucsSwEthLanBorderFsmRn = _CucsSwEthLanBorderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 3),
    _CucsSwEthLanBorderFsmRn_Type()
)
cucsSwEthLanBorderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmRn.setStatus("current")
_CucsSwEthLanBorderFsmCompletionTime_Type = DateAndTime
_CucsSwEthLanBorderFsmCompletionTime_Object = MibTableColumn
cucsSwEthLanBorderFsmCompletionTime = _CucsSwEthLanBorderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 4),
    _CucsSwEthLanBorderFsmCompletionTime_Type()
)
cucsSwEthLanBorderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmCompletionTime.setStatus("current")
_CucsSwEthLanBorderFsmCurrentFsm_Type = CucsSwEthLanBorderFsmCurrentFsm
_CucsSwEthLanBorderFsmCurrentFsm_Object = MibTableColumn
cucsSwEthLanBorderFsmCurrentFsm = _CucsSwEthLanBorderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 5),
    _CucsSwEthLanBorderFsmCurrentFsm_Type()
)
cucsSwEthLanBorderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmCurrentFsm.setStatus("current")
_CucsSwEthLanBorderFsmDescrData_Type = SnmpAdminString
_CucsSwEthLanBorderFsmDescrData_Object = MibTableColumn
cucsSwEthLanBorderFsmDescrData = _CucsSwEthLanBorderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 6),
    _CucsSwEthLanBorderFsmDescrData_Type()
)
cucsSwEthLanBorderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmDescrData.setStatus("current")
_CucsSwEthLanBorderFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwEthLanBorderFsmFsmStatus_Object = MibTableColumn
cucsSwEthLanBorderFsmFsmStatus = _CucsSwEthLanBorderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 7),
    _CucsSwEthLanBorderFsmFsmStatus_Type()
)
cucsSwEthLanBorderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmFsmStatus.setStatus("current")
_CucsSwEthLanBorderFsmProgress_Type = Gauge32
_CucsSwEthLanBorderFsmProgress_Object = MibTableColumn
cucsSwEthLanBorderFsmProgress = _CucsSwEthLanBorderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 8),
    _CucsSwEthLanBorderFsmProgress_Type()
)
cucsSwEthLanBorderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmProgress.setStatus("current")
_CucsSwEthLanBorderFsmRmtErrCode_Type = Gauge32
_CucsSwEthLanBorderFsmRmtErrCode_Object = MibTableColumn
cucsSwEthLanBorderFsmRmtErrCode = _CucsSwEthLanBorderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 9),
    _CucsSwEthLanBorderFsmRmtErrCode_Type()
)
cucsSwEthLanBorderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmRmtErrCode.setStatus("current")
_CucsSwEthLanBorderFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwEthLanBorderFsmRmtErrDescr_Object = MibTableColumn
cucsSwEthLanBorderFsmRmtErrDescr = _CucsSwEthLanBorderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 10),
    _CucsSwEthLanBorderFsmRmtErrDescr_Type()
)
cucsSwEthLanBorderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmRmtErrDescr.setStatus("current")
_CucsSwEthLanBorderFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwEthLanBorderFsmRmtRslt_Object = MibTableColumn
cucsSwEthLanBorderFsmRmtRslt = _CucsSwEthLanBorderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 46, 1, 11),
    _CucsSwEthLanBorderFsmRmtRslt_Type()
)
cucsSwEthLanBorderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmRmtRslt.setStatus("current")
_CucsSwEthLanBorderFsmStageTable_Object = MibTable
cucsSwEthLanBorderFsmStageTable = _CucsSwEthLanBorderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47)
)
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageTable.setStatus("current")
_CucsSwEthLanBorderFsmStageEntry_Object = MibTableRow
cucsSwEthLanBorderFsmStageEntry = _CucsSwEthLanBorderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1)
)
cucsSwEthLanBorderFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanBorderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageEntry.setStatus("current")
_CucsSwEthLanBorderFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanBorderFsmStageInstanceId_Object = MibTableColumn
cucsSwEthLanBorderFsmStageInstanceId = _CucsSwEthLanBorderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 1),
    _CucsSwEthLanBorderFsmStageInstanceId_Type()
)
cucsSwEthLanBorderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageInstanceId.setStatus("current")
_CucsSwEthLanBorderFsmStageDn_Type = CucsManagedObjectDn
_CucsSwEthLanBorderFsmStageDn_Object = MibTableColumn
cucsSwEthLanBorderFsmStageDn = _CucsSwEthLanBorderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 2),
    _CucsSwEthLanBorderFsmStageDn_Type()
)
cucsSwEthLanBorderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageDn.setStatus("current")
_CucsSwEthLanBorderFsmStageRn_Type = SnmpAdminString
_CucsSwEthLanBorderFsmStageRn_Object = MibTableColumn
cucsSwEthLanBorderFsmStageRn = _CucsSwEthLanBorderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 3),
    _CucsSwEthLanBorderFsmStageRn_Type()
)
cucsSwEthLanBorderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageRn.setStatus("current")
_CucsSwEthLanBorderFsmStageDescrData_Type = SnmpAdminString
_CucsSwEthLanBorderFsmStageDescrData_Object = MibTableColumn
cucsSwEthLanBorderFsmStageDescrData = _CucsSwEthLanBorderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 4),
    _CucsSwEthLanBorderFsmStageDescrData_Type()
)
cucsSwEthLanBorderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageDescrData.setStatus("current")
_CucsSwEthLanBorderFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwEthLanBorderFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwEthLanBorderFsmStageLastUpdateTime = _CucsSwEthLanBorderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 5),
    _CucsSwEthLanBorderFsmStageLastUpdateTime_Type()
)
cucsSwEthLanBorderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageLastUpdateTime.setStatus("current")
_CucsSwEthLanBorderFsmStageName_Type = CucsSwEthLanBorderFsmStageName
_CucsSwEthLanBorderFsmStageName_Object = MibTableColumn
cucsSwEthLanBorderFsmStageName = _CucsSwEthLanBorderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 6),
    _CucsSwEthLanBorderFsmStageName_Type()
)
cucsSwEthLanBorderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageName.setStatus("current")
_CucsSwEthLanBorderFsmStageOrder_Type = Gauge32
_CucsSwEthLanBorderFsmStageOrder_Object = MibTableColumn
cucsSwEthLanBorderFsmStageOrder = _CucsSwEthLanBorderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 7),
    _CucsSwEthLanBorderFsmStageOrder_Type()
)
cucsSwEthLanBorderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageOrder.setStatus("current")
_CucsSwEthLanBorderFsmStageRetry_Type = Gauge32
_CucsSwEthLanBorderFsmStageRetry_Object = MibTableColumn
cucsSwEthLanBorderFsmStageRetry = _CucsSwEthLanBorderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 8),
    _CucsSwEthLanBorderFsmStageRetry_Type()
)
cucsSwEthLanBorderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageRetry.setStatus("current")
_CucsSwEthLanBorderFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwEthLanBorderFsmStageStageStatus_Object = MibTableColumn
cucsSwEthLanBorderFsmStageStageStatus = _CucsSwEthLanBorderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 47, 1, 9),
    _CucsSwEthLanBorderFsmStageStageStatus_Type()
)
cucsSwEthLanBorderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanBorderFsmStageStageStatus.setStatus("current")
_CucsSwEthMonFsmTable_Object = MibTable
cucsSwEthMonFsmTable = _CucsSwEthMonFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48)
)
if mibBuilder.loadTexts:
    cucsSwEthMonFsmTable.setStatus("current")
_CucsSwEthMonFsmEntry_Object = MibTableRow
cucsSwEthMonFsmEntry = _CucsSwEthMonFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1)
)
cucsSwEthMonFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthMonFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthMonFsmEntry.setStatus("current")
_CucsSwEthMonFsmInstanceId_Type = CucsManagedObjectId
_CucsSwEthMonFsmInstanceId_Object = MibTableColumn
cucsSwEthMonFsmInstanceId = _CucsSwEthMonFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 1),
    _CucsSwEthMonFsmInstanceId_Type()
)
cucsSwEthMonFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmInstanceId.setStatus("current")
_CucsSwEthMonFsmDn_Type = CucsManagedObjectDn
_CucsSwEthMonFsmDn_Object = MibTableColumn
cucsSwEthMonFsmDn = _CucsSwEthMonFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 2),
    _CucsSwEthMonFsmDn_Type()
)
cucsSwEthMonFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmDn.setStatus("current")
_CucsSwEthMonFsmRn_Type = SnmpAdminString
_CucsSwEthMonFsmRn_Object = MibTableColumn
cucsSwEthMonFsmRn = _CucsSwEthMonFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 3),
    _CucsSwEthMonFsmRn_Type()
)
cucsSwEthMonFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmRn.setStatus("current")
_CucsSwEthMonFsmCompletionTime_Type = DateAndTime
_CucsSwEthMonFsmCompletionTime_Object = MibTableColumn
cucsSwEthMonFsmCompletionTime = _CucsSwEthMonFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 4),
    _CucsSwEthMonFsmCompletionTime_Type()
)
cucsSwEthMonFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmCompletionTime.setStatus("current")
_CucsSwEthMonFsmCurrentFsm_Type = CucsSwEthMonFsmCurrentFsm
_CucsSwEthMonFsmCurrentFsm_Object = MibTableColumn
cucsSwEthMonFsmCurrentFsm = _CucsSwEthMonFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 5),
    _CucsSwEthMonFsmCurrentFsm_Type()
)
cucsSwEthMonFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmCurrentFsm.setStatus("current")
_CucsSwEthMonFsmDescrData_Type = SnmpAdminString
_CucsSwEthMonFsmDescrData_Object = MibTableColumn
cucsSwEthMonFsmDescrData = _CucsSwEthMonFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 6),
    _CucsSwEthMonFsmDescrData_Type()
)
cucsSwEthMonFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmDescrData.setStatus("current")
_CucsSwEthMonFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwEthMonFsmFsmStatus_Object = MibTableColumn
cucsSwEthMonFsmFsmStatus = _CucsSwEthMonFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 7),
    _CucsSwEthMonFsmFsmStatus_Type()
)
cucsSwEthMonFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmFsmStatus.setStatus("current")
_CucsSwEthMonFsmProgress_Type = Gauge32
_CucsSwEthMonFsmProgress_Object = MibTableColumn
cucsSwEthMonFsmProgress = _CucsSwEthMonFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 8),
    _CucsSwEthMonFsmProgress_Type()
)
cucsSwEthMonFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmProgress.setStatus("current")
_CucsSwEthMonFsmRmtErrCode_Type = Gauge32
_CucsSwEthMonFsmRmtErrCode_Object = MibTableColumn
cucsSwEthMonFsmRmtErrCode = _CucsSwEthMonFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 9),
    _CucsSwEthMonFsmRmtErrCode_Type()
)
cucsSwEthMonFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmRmtErrCode.setStatus("current")
_CucsSwEthMonFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwEthMonFsmRmtErrDescr_Object = MibTableColumn
cucsSwEthMonFsmRmtErrDescr = _CucsSwEthMonFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 10),
    _CucsSwEthMonFsmRmtErrDescr_Type()
)
cucsSwEthMonFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmRmtErrDescr.setStatus("current")
_CucsSwEthMonFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwEthMonFsmRmtRslt_Object = MibTableColumn
cucsSwEthMonFsmRmtRslt = _CucsSwEthMonFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 48, 1, 11),
    _CucsSwEthMonFsmRmtRslt_Type()
)
cucsSwEthMonFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmRmtRslt.setStatus("current")
_CucsSwEthMonFsmStageTable_Object = MibTable
cucsSwEthMonFsmStageTable = _CucsSwEthMonFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49)
)
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageTable.setStatus("current")
_CucsSwEthMonFsmStageEntry_Object = MibTableRow
cucsSwEthMonFsmStageEntry = _CucsSwEthMonFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1)
)
cucsSwEthMonFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthMonFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageEntry.setStatus("current")
_CucsSwEthMonFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwEthMonFsmStageInstanceId_Object = MibTableColumn
cucsSwEthMonFsmStageInstanceId = _CucsSwEthMonFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 1),
    _CucsSwEthMonFsmStageInstanceId_Type()
)
cucsSwEthMonFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageInstanceId.setStatus("current")
_CucsSwEthMonFsmStageDn_Type = CucsManagedObjectDn
_CucsSwEthMonFsmStageDn_Object = MibTableColumn
cucsSwEthMonFsmStageDn = _CucsSwEthMonFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 2),
    _CucsSwEthMonFsmStageDn_Type()
)
cucsSwEthMonFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageDn.setStatus("current")
_CucsSwEthMonFsmStageRn_Type = SnmpAdminString
_CucsSwEthMonFsmStageRn_Object = MibTableColumn
cucsSwEthMonFsmStageRn = _CucsSwEthMonFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 3),
    _CucsSwEthMonFsmStageRn_Type()
)
cucsSwEthMonFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageRn.setStatus("current")
_CucsSwEthMonFsmStageDescrData_Type = SnmpAdminString
_CucsSwEthMonFsmStageDescrData_Object = MibTableColumn
cucsSwEthMonFsmStageDescrData = _CucsSwEthMonFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 4),
    _CucsSwEthMonFsmStageDescrData_Type()
)
cucsSwEthMonFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageDescrData.setStatus("current")
_CucsSwEthMonFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwEthMonFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwEthMonFsmStageLastUpdateTime = _CucsSwEthMonFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 5),
    _CucsSwEthMonFsmStageLastUpdateTime_Type()
)
cucsSwEthMonFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageLastUpdateTime.setStatus("current")
_CucsSwEthMonFsmStageName_Type = CucsSwEthMonFsmStageName
_CucsSwEthMonFsmStageName_Object = MibTableColumn
cucsSwEthMonFsmStageName = _CucsSwEthMonFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 6),
    _CucsSwEthMonFsmStageName_Type()
)
cucsSwEthMonFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageName.setStatus("current")
_CucsSwEthMonFsmStageOrder_Type = Gauge32
_CucsSwEthMonFsmStageOrder_Object = MibTableColumn
cucsSwEthMonFsmStageOrder = _CucsSwEthMonFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 7),
    _CucsSwEthMonFsmStageOrder_Type()
)
cucsSwEthMonFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageOrder.setStatus("current")
_CucsSwEthMonFsmStageRetry_Type = Gauge32
_CucsSwEthMonFsmStageRetry_Object = MibTableColumn
cucsSwEthMonFsmStageRetry = _CucsSwEthMonFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 8),
    _CucsSwEthMonFsmStageRetry_Type()
)
cucsSwEthMonFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageRetry.setStatus("current")
_CucsSwEthMonFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwEthMonFsmStageStageStatus_Object = MibTableColumn
cucsSwEthMonFsmStageStageStatus = _CucsSwEthMonFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 49, 1, 9),
    _CucsSwEthMonFsmStageStageStatus_Type()
)
cucsSwEthMonFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthMonFsmStageStageStatus.setStatus("current")
_CucsSwFabricZoneNsTable_Object = MibTable
cucsSwFabricZoneNsTable = _CucsSwFabricZoneNsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50)
)
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsTable.setStatus("current")
_CucsSwFabricZoneNsEntry_Object = MibTableRow
cucsSwFabricZoneNsEntry = _CucsSwFabricZoneNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50, 1)
)
cucsSwFabricZoneNsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFabricZoneNsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsEntry.setStatus("current")
_CucsSwFabricZoneNsInstanceId_Type = CucsManagedObjectId
_CucsSwFabricZoneNsInstanceId_Object = MibTableColumn
cucsSwFabricZoneNsInstanceId = _CucsSwFabricZoneNsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50, 1, 1),
    _CucsSwFabricZoneNsInstanceId_Type()
)
cucsSwFabricZoneNsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsInstanceId.setStatus("current")
_CucsSwFabricZoneNsDn_Type = CucsManagedObjectDn
_CucsSwFabricZoneNsDn_Object = MibTableColumn
cucsSwFabricZoneNsDn = _CucsSwFabricZoneNsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50, 1, 2),
    _CucsSwFabricZoneNsDn_Type()
)
cucsSwFabricZoneNsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsDn.setStatus("current")
_CucsSwFabricZoneNsRn_Type = SnmpAdminString
_CucsSwFabricZoneNsRn_Object = MibTableColumn
cucsSwFabricZoneNsRn = _CucsSwFabricZoneNsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50, 1, 3),
    _CucsSwFabricZoneNsRn_Type()
)
cucsSwFabricZoneNsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsRn.setStatus("current")
_CucsSwFabricZoneNsAllocStatus_Type = CucsSwFabricZoneNsAllocStatus
_CucsSwFabricZoneNsAllocStatus_Object = MibTableColumn
cucsSwFabricZoneNsAllocStatus = _CucsSwFabricZoneNsAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50, 1, 4),
    _CucsSwFabricZoneNsAllocStatus_Type()
)
cucsSwFabricZoneNsAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsAllocStatus.setStatus("current")
_CucsSwFabricZoneNsLimit_Type = Gauge32
_CucsSwFabricZoneNsLimit_Object = MibTableColumn
cucsSwFabricZoneNsLimit = _CucsSwFabricZoneNsLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50, 1, 5),
    _CucsSwFabricZoneNsLimit_Type()
)
cucsSwFabricZoneNsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsLimit.setStatus("current")
_CucsSwFabricZoneNsSwitchId_Type = CucsNetworkSwitchId
_CucsSwFabricZoneNsSwitchId_Object = MibTableColumn
cucsSwFabricZoneNsSwitchId = _CucsSwFabricZoneNsSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50, 1, 6),
    _CucsSwFabricZoneNsSwitchId_Type()
)
cucsSwFabricZoneNsSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsSwitchId.setStatus("current")
_CucsSwFabricZoneNsZoneCount_Type = Gauge32
_CucsSwFabricZoneNsZoneCount_Object = MibTableColumn
cucsSwFabricZoneNsZoneCount = _CucsSwFabricZoneNsZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 50, 1, 7),
    _CucsSwFabricZoneNsZoneCount_Type()
)
cucsSwFabricZoneNsZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsZoneCount.setStatus("current")
_CucsSwFabricZoneNsOverrideTable_Object = MibTable
cucsSwFabricZoneNsOverrideTable = _CucsSwFabricZoneNsOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 51)
)
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsOverrideTable.setStatus("current")
_CucsSwFabricZoneNsOverrideEntry_Object = MibTableRow
cucsSwFabricZoneNsOverrideEntry = _CucsSwFabricZoneNsOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 51, 1)
)
cucsSwFabricZoneNsOverrideEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFabricZoneNsOverrideInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsOverrideEntry.setStatus("current")
_CucsSwFabricZoneNsOverrideInstanceId_Type = CucsManagedObjectId
_CucsSwFabricZoneNsOverrideInstanceId_Object = MibTableColumn
cucsSwFabricZoneNsOverrideInstanceId = _CucsSwFabricZoneNsOverrideInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 51, 1, 1),
    _CucsSwFabricZoneNsOverrideInstanceId_Type()
)
cucsSwFabricZoneNsOverrideInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsOverrideInstanceId.setStatus("current")
_CucsSwFabricZoneNsOverrideDn_Type = CucsManagedObjectDn
_CucsSwFabricZoneNsOverrideDn_Object = MibTableColumn
cucsSwFabricZoneNsOverrideDn = _CucsSwFabricZoneNsOverrideDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 51, 1, 2),
    _CucsSwFabricZoneNsOverrideDn_Type()
)
cucsSwFabricZoneNsOverrideDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsOverrideDn.setStatus("current")
_CucsSwFabricZoneNsOverrideRn_Type = SnmpAdminString
_CucsSwFabricZoneNsOverrideRn_Object = MibTableColumn
cucsSwFabricZoneNsOverrideRn = _CucsSwFabricZoneNsOverrideRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 51, 1, 3),
    _CucsSwFabricZoneNsOverrideRn_Type()
)
cucsSwFabricZoneNsOverrideRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsOverrideRn.setStatus("current")
_CucsSwFabricZoneNsOverrideLimit_Type = Gauge32
_CucsSwFabricZoneNsOverrideLimit_Object = MibTableColumn
cucsSwFabricZoneNsOverrideLimit = _CucsSwFabricZoneNsOverrideLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 51, 1, 4),
    _CucsSwFabricZoneNsOverrideLimit_Type()
)
cucsSwFabricZoneNsOverrideLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFabricZoneNsOverrideLimit.setStatus("current")
_CucsSwFcMonFsmTable_Object = MibTable
cucsSwFcMonFsmTable = _CucsSwFcMonFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52)
)
if mibBuilder.loadTexts:
    cucsSwFcMonFsmTable.setStatus("current")
_CucsSwFcMonFsmEntry_Object = MibTableRow
cucsSwFcMonFsmEntry = _CucsSwFcMonFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1)
)
cucsSwFcMonFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcMonFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcMonFsmEntry.setStatus("current")
_CucsSwFcMonFsmInstanceId_Type = CucsManagedObjectId
_CucsSwFcMonFsmInstanceId_Object = MibTableColumn
cucsSwFcMonFsmInstanceId = _CucsSwFcMonFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 1),
    _CucsSwFcMonFsmInstanceId_Type()
)
cucsSwFcMonFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmInstanceId.setStatus("current")
_CucsSwFcMonFsmDn_Type = CucsManagedObjectDn
_CucsSwFcMonFsmDn_Object = MibTableColumn
cucsSwFcMonFsmDn = _CucsSwFcMonFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 2),
    _CucsSwFcMonFsmDn_Type()
)
cucsSwFcMonFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmDn.setStatus("current")
_CucsSwFcMonFsmRn_Type = SnmpAdminString
_CucsSwFcMonFsmRn_Object = MibTableColumn
cucsSwFcMonFsmRn = _CucsSwFcMonFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 3),
    _CucsSwFcMonFsmRn_Type()
)
cucsSwFcMonFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmRn.setStatus("current")
_CucsSwFcMonFsmCompletionTime_Type = DateAndTime
_CucsSwFcMonFsmCompletionTime_Object = MibTableColumn
cucsSwFcMonFsmCompletionTime = _CucsSwFcMonFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 4),
    _CucsSwFcMonFsmCompletionTime_Type()
)
cucsSwFcMonFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmCompletionTime.setStatus("current")
_CucsSwFcMonFsmCurrentFsm_Type = CucsSwFcMonFsmCurrentFsm
_CucsSwFcMonFsmCurrentFsm_Object = MibTableColumn
cucsSwFcMonFsmCurrentFsm = _CucsSwFcMonFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 5),
    _CucsSwFcMonFsmCurrentFsm_Type()
)
cucsSwFcMonFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmCurrentFsm.setStatus("current")
_CucsSwFcMonFsmDescrData_Type = SnmpAdminString
_CucsSwFcMonFsmDescrData_Object = MibTableColumn
cucsSwFcMonFsmDescrData = _CucsSwFcMonFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 6),
    _CucsSwFcMonFsmDescrData_Type()
)
cucsSwFcMonFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmDescrData.setStatus("current")
_CucsSwFcMonFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwFcMonFsmFsmStatus_Object = MibTableColumn
cucsSwFcMonFsmFsmStatus = _CucsSwFcMonFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 7),
    _CucsSwFcMonFsmFsmStatus_Type()
)
cucsSwFcMonFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmFsmStatus.setStatus("current")
_CucsSwFcMonFsmProgress_Type = Gauge32
_CucsSwFcMonFsmProgress_Object = MibTableColumn
cucsSwFcMonFsmProgress = _CucsSwFcMonFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 8),
    _CucsSwFcMonFsmProgress_Type()
)
cucsSwFcMonFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmProgress.setStatus("current")
_CucsSwFcMonFsmRmtErrCode_Type = Gauge32
_CucsSwFcMonFsmRmtErrCode_Object = MibTableColumn
cucsSwFcMonFsmRmtErrCode = _CucsSwFcMonFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 9),
    _CucsSwFcMonFsmRmtErrCode_Type()
)
cucsSwFcMonFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmRmtErrCode.setStatus("current")
_CucsSwFcMonFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwFcMonFsmRmtErrDescr_Object = MibTableColumn
cucsSwFcMonFsmRmtErrDescr = _CucsSwFcMonFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 10),
    _CucsSwFcMonFsmRmtErrDescr_Type()
)
cucsSwFcMonFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmRmtErrDescr.setStatus("current")
_CucsSwFcMonFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwFcMonFsmRmtRslt_Object = MibTableColumn
cucsSwFcMonFsmRmtRslt = _CucsSwFcMonFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 52, 1, 11),
    _CucsSwFcMonFsmRmtRslt_Type()
)
cucsSwFcMonFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmRmtRslt.setStatus("current")
_CucsSwFcMonFsmStageTable_Object = MibTable
cucsSwFcMonFsmStageTable = _CucsSwFcMonFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53)
)
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageTable.setStatus("current")
_CucsSwFcMonFsmStageEntry_Object = MibTableRow
cucsSwFcMonFsmStageEntry = _CucsSwFcMonFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1)
)
cucsSwFcMonFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcMonFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageEntry.setStatus("current")
_CucsSwFcMonFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwFcMonFsmStageInstanceId_Object = MibTableColumn
cucsSwFcMonFsmStageInstanceId = _CucsSwFcMonFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 1),
    _CucsSwFcMonFsmStageInstanceId_Type()
)
cucsSwFcMonFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageInstanceId.setStatus("current")
_CucsSwFcMonFsmStageDn_Type = CucsManagedObjectDn
_CucsSwFcMonFsmStageDn_Object = MibTableColumn
cucsSwFcMonFsmStageDn = _CucsSwFcMonFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 2),
    _CucsSwFcMonFsmStageDn_Type()
)
cucsSwFcMonFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageDn.setStatus("current")
_CucsSwFcMonFsmStageRn_Type = SnmpAdminString
_CucsSwFcMonFsmStageRn_Object = MibTableColumn
cucsSwFcMonFsmStageRn = _CucsSwFcMonFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 3),
    _CucsSwFcMonFsmStageRn_Type()
)
cucsSwFcMonFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageRn.setStatus("current")
_CucsSwFcMonFsmStageDescrData_Type = SnmpAdminString
_CucsSwFcMonFsmStageDescrData_Object = MibTableColumn
cucsSwFcMonFsmStageDescrData = _CucsSwFcMonFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 4),
    _CucsSwFcMonFsmStageDescrData_Type()
)
cucsSwFcMonFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageDescrData.setStatus("current")
_CucsSwFcMonFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwFcMonFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwFcMonFsmStageLastUpdateTime = _CucsSwFcMonFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 5),
    _CucsSwFcMonFsmStageLastUpdateTime_Type()
)
cucsSwFcMonFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageLastUpdateTime.setStatus("current")
_CucsSwFcMonFsmStageName_Type = CucsSwFcMonFsmStageName
_CucsSwFcMonFsmStageName_Object = MibTableColumn
cucsSwFcMonFsmStageName = _CucsSwFcMonFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 6),
    _CucsSwFcMonFsmStageName_Type()
)
cucsSwFcMonFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageName.setStatus("current")
_CucsSwFcMonFsmStageOrder_Type = Gauge32
_CucsSwFcMonFsmStageOrder_Object = MibTableColumn
cucsSwFcMonFsmStageOrder = _CucsSwFcMonFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 7),
    _CucsSwFcMonFsmStageOrder_Type()
)
cucsSwFcMonFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageOrder.setStatus("current")
_CucsSwFcMonFsmStageRetry_Type = Gauge32
_CucsSwFcMonFsmStageRetry_Object = MibTableColumn
cucsSwFcMonFsmStageRetry = _CucsSwFcMonFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 8),
    _CucsSwFcMonFsmStageRetry_Type()
)
cucsSwFcMonFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageRetry.setStatus("current")
_CucsSwFcMonFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwFcMonFsmStageStageStatus_Object = MibTableColumn
cucsSwFcMonFsmStageStageStatus = _CucsSwFcMonFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 53, 1, 9),
    _CucsSwFcMonFsmStageStageStatus_Type()
)
cucsSwFcMonFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcMonFsmStageStageStatus.setStatus("current")
_CucsSwFcSanBorderFsmTable_Object = MibTable
cucsSwFcSanBorderFsmTable = _CucsSwFcSanBorderFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54)
)
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmTable.setStatus("current")
_CucsSwFcSanBorderFsmEntry_Object = MibTableRow
cucsSwFcSanBorderFsmEntry = _CucsSwFcSanBorderFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1)
)
cucsSwFcSanBorderFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcSanBorderFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmEntry.setStatus("current")
_CucsSwFcSanBorderFsmInstanceId_Type = CucsManagedObjectId
_CucsSwFcSanBorderFsmInstanceId_Object = MibTableColumn
cucsSwFcSanBorderFsmInstanceId = _CucsSwFcSanBorderFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 1),
    _CucsSwFcSanBorderFsmInstanceId_Type()
)
cucsSwFcSanBorderFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmInstanceId.setStatus("current")
_CucsSwFcSanBorderFsmDn_Type = CucsManagedObjectDn
_CucsSwFcSanBorderFsmDn_Object = MibTableColumn
cucsSwFcSanBorderFsmDn = _CucsSwFcSanBorderFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 2),
    _CucsSwFcSanBorderFsmDn_Type()
)
cucsSwFcSanBorderFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmDn.setStatus("current")
_CucsSwFcSanBorderFsmRn_Type = SnmpAdminString
_CucsSwFcSanBorderFsmRn_Object = MibTableColumn
cucsSwFcSanBorderFsmRn = _CucsSwFcSanBorderFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 3),
    _CucsSwFcSanBorderFsmRn_Type()
)
cucsSwFcSanBorderFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmRn.setStatus("current")
_CucsSwFcSanBorderFsmCompletionTime_Type = DateAndTime
_CucsSwFcSanBorderFsmCompletionTime_Object = MibTableColumn
cucsSwFcSanBorderFsmCompletionTime = _CucsSwFcSanBorderFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 4),
    _CucsSwFcSanBorderFsmCompletionTime_Type()
)
cucsSwFcSanBorderFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmCompletionTime.setStatus("current")
_CucsSwFcSanBorderFsmCurrentFsm_Type = CucsSwFcSanBorderFsmCurrentFsm
_CucsSwFcSanBorderFsmCurrentFsm_Object = MibTableColumn
cucsSwFcSanBorderFsmCurrentFsm = _CucsSwFcSanBorderFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 5),
    _CucsSwFcSanBorderFsmCurrentFsm_Type()
)
cucsSwFcSanBorderFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmCurrentFsm.setStatus("current")
_CucsSwFcSanBorderFsmDescrData_Type = SnmpAdminString
_CucsSwFcSanBorderFsmDescrData_Object = MibTableColumn
cucsSwFcSanBorderFsmDescrData = _CucsSwFcSanBorderFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 6),
    _CucsSwFcSanBorderFsmDescrData_Type()
)
cucsSwFcSanBorderFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmDescrData.setStatus("current")
_CucsSwFcSanBorderFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwFcSanBorderFsmFsmStatus_Object = MibTableColumn
cucsSwFcSanBorderFsmFsmStatus = _CucsSwFcSanBorderFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 7),
    _CucsSwFcSanBorderFsmFsmStatus_Type()
)
cucsSwFcSanBorderFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmFsmStatus.setStatus("current")
_CucsSwFcSanBorderFsmProgress_Type = Gauge32
_CucsSwFcSanBorderFsmProgress_Object = MibTableColumn
cucsSwFcSanBorderFsmProgress = _CucsSwFcSanBorderFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 8),
    _CucsSwFcSanBorderFsmProgress_Type()
)
cucsSwFcSanBorderFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmProgress.setStatus("current")
_CucsSwFcSanBorderFsmRmtErrCode_Type = Gauge32
_CucsSwFcSanBorderFsmRmtErrCode_Object = MibTableColumn
cucsSwFcSanBorderFsmRmtErrCode = _CucsSwFcSanBorderFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 9),
    _CucsSwFcSanBorderFsmRmtErrCode_Type()
)
cucsSwFcSanBorderFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmRmtErrCode.setStatus("current")
_CucsSwFcSanBorderFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwFcSanBorderFsmRmtErrDescr_Object = MibTableColumn
cucsSwFcSanBorderFsmRmtErrDescr = _CucsSwFcSanBorderFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 10),
    _CucsSwFcSanBorderFsmRmtErrDescr_Type()
)
cucsSwFcSanBorderFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmRmtErrDescr.setStatus("current")
_CucsSwFcSanBorderFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwFcSanBorderFsmRmtRslt_Object = MibTableColumn
cucsSwFcSanBorderFsmRmtRslt = _CucsSwFcSanBorderFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 54, 1, 11),
    _CucsSwFcSanBorderFsmRmtRslt_Type()
)
cucsSwFcSanBorderFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmRmtRslt.setStatus("current")
_CucsSwFcSanBorderFsmStageTable_Object = MibTable
cucsSwFcSanBorderFsmStageTable = _CucsSwFcSanBorderFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55)
)
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageTable.setStatus("current")
_CucsSwFcSanBorderFsmStageEntry_Object = MibTableRow
cucsSwFcSanBorderFsmStageEntry = _CucsSwFcSanBorderFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1)
)
cucsSwFcSanBorderFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcSanBorderFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageEntry.setStatus("current")
_CucsSwFcSanBorderFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwFcSanBorderFsmStageInstanceId_Object = MibTableColumn
cucsSwFcSanBorderFsmStageInstanceId = _CucsSwFcSanBorderFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 1),
    _CucsSwFcSanBorderFsmStageInstanceId_Type()
)
cucsSwFcSanBorderFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageInstanceId.setStatus("current")
_CucsSwFcSanBorderFsmStageDn_Type = CucsManagedObjectDn
_CucsSwFcSanBorderFsmStageDn_Object = MibTableColumn
cucsSwFcSanBorderFsmStageDn = _CucsSwFcSanBorderFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 2),
    _CucsSwFcSanBorderFsmStageDn_Type()
)
cucsSwFcSanBorderFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageDn.setStatus("current")
_CucsSwFcSanBorderFsmStageRn_Type = SnmpAdminString
_CucsSwFcSanBorderFsmStageRn_Object = MibTableColumn
cucsSwFcSanBorderFsmStageRn = _CucsSwFcSanBorderFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 3),
    _CucsSwFcSanBorderFsmStageRn_Type()
)
cucsSwFcSanBorderFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageRn.setStatus("current")
_CucsSwFcSanBorderFsmStageDescrData_Type = SnmpAdminString
_CucsSwFcSanBorderFsmStageDescrData_Object = MibTableColumn
cucsSwFcSanBorderFsmStageDescrData = _CucsSwFcSanBorderFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 4),
    _CucsSwFcSanBorderFsmStageDescrData_Type()
)
cucsSwFcSanBorderFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageDescrData.setStatus("current")
_CucsSwFcSanBorderFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwFcSanBorderFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwFcSanBorderFsmStageLastUpdateTime = _CucsSwFcSanBorderFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 5),
    _CucsSwFcSanBorderFsmStageLastUpdateTime_Type()
)
cucsSwFcSanBorderFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageLastUpdateTime.setStatus("current")
_CucsSwFcSanBorderFsmStageName_Type = CucsSwFcSanBorderFsmStageName
_CucsSwFcSanBorderFsmStageName_Object = MibTableColumn
cucsSwFcSanBorderFsmStageName = _CucsSwFcSanBorderFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 6),
    _CucsSwFcSanBorderFsmStageName_Type()
)
cucsSwFcSanBorderFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageName.setStatus("current")
_CucsSwFcSanBorderFsmStageOrder_Type = Gauge32
_CucsSwFcSanBorderFsmStageOrder_Object = MibTableColumn
cucsSwFcSanBorderFsmStageOrder = _CucsSwFcSanBorderFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 7),
    _CucsSwFcSanBorderFsmStageOrder_Type()
)
cucsSwFcSanBorderFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageOrder.setStatus("current")
_CucsSwFcSanBorderFsmStageRetry_Type = Gauge32
_CucsSwFcSanBorderFsmStageRetry_Object = MibTableColumn
cucsSwFcSanBorderFsmStageRetry = _CucsSwFcSanBorderFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 8),
    _CucsSwFcSanBorderFsmStageRetry_Type()
)
cucsSwFcSanBorderFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageRetry.setStatus("current")
_CucsSwFcSanBorderFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwFcSanBorderFsmStageStageStatus_Object = MibTableColumn
cucsSwFcSanBorderFsmStageStageStatus = _CucsSwFcSanBorderFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 55, 1, 9),
    _CucsSwFcSanBorderFsmStageStageStatus_Type()
)
cucsSwFcSanBorderFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcSanBorderFsmStageStageStatus.setStatus("current")
_CucsSwFcServerZoneGroupTable_Object = MibTable
cucsSwFcServerZoneGroupTable = _CucsSwFcServerZoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56)
)
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupTable.setStatus("current")
_CucsSwFcServerZoneGroupEntry_Object = MibTableRow
cucsSwFcServerZoneGroupEntry = _CucsSwFcServerZoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1)
)
cucsSwFcServerZoneGroupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcServerZoneGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupEntry.setStatus("current")
_CucsSwFcServerZoneGroupInstanceId_Type = CucsManagedObjectId
_CucsSwFcServerZoneGroupInstanceId_Object = MibTableColumn
cucsSwFcServerZoneGroupInstanceId = _CucsSwFcServerZoneGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 1),
    _CucsSwFcServerZoneGroupInstanceId_Type()
)
cucsSwFcServerZoneGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupInstanceId.setStatus("current")
_CucsSwFcServerZoneGroupDn_Type = CucsManagedObjectDn
_CucsSwFcServerZoneGroupDn_Object = MibTableColumn
cucsSwFcServerZoneGroupDn = _CucsSwFcServerZoneGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 2),
    _CucsSwFcServerZoneGroupDn_Type()
)
cucsSwFcServerZoneGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupDn.setStatus("current")
_CucsSwFcServerZoneGroupRn_Type = SnmpAdminString
_CucsSwFcServerZoneGroupRn_Object = MibTableColumn
cucsSwFcServerZoneGroupRn = _CucsSwFcServerZoneGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 3),
    _CucsSwFcServerZoneGroupRn_Type()
)
cucsSwFcServerZoneGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupRn.setStatus("current")
_CucsSwFcServerZoneGroupEpDn_Type = SnmpAdminString
_CucsSwFcServerZoneGroupEpDn_Object = MibTableColumn
cucsSwFcServerZoneGroupEpDn = _CucsSwFcServerZoneGroupEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 4),
    _CucsSwFcServerZoneGroupEpDn_Type()
)
cucsSwFcServerZoneGroupEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupEpDn.setStatus("current")
_CucsSwFcServerZoneGroupId_Type = Gauge32
_CucsSwFcServerZoneGroupId_Object = MibTableColumn
cucsSwFcServerZoneGroupId = _CucsSwFcServerZoneGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 5),
    _CucsSwFcServerZoneGroupId_Type()
)
cucsSwFcServerZoneGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupId.setStatus("current")
_CucsSwFcServerZoneGroupLc_Type = CucsSwFcServerZoneGroupLc
_CucsSwFcServerZoneGroupLc_Object = MibTableColumn
cucsSwFcServerZoneGroupLc = _CucsSwFcServerZoneGroupLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 6),
    _CucsSwFcServerZoneGroupLc_Type()
)
cucsSwFcServerZoneGroupLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupLc.setStatus("current")
_CucsSwFcServerZoneGroupName_Type = SnmpAdminString
_CucsSwFcServerZoneGroupName_Object = MibTableColumn
cucsSwFcServerZoneGroupName = _CucsSwFcServerZoneGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 7),
    _CucsSwFcServerZoneGroupName_Type()
)
cucsSwFcServerZoneGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupName.setStatus("current")
_CucsSwFcServerZoneGroupPeerDn_Type = SnmpAdminString
_CucsSwFcServerZoneGroupPeerDn_Object = MibTableColumn
cucsSwFcServerZoneGroupPeerDn = _CucsSwFcServerZoneGroupPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 8),
    _CucsSwFcServerZoneGroupPeerDn_Type()
)
cucsSwFcServerZoneGroupPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupPeerDn.setStatus("current")
_CucsSwFcServerZoneGroupServerDn_Type = SnmpAdminString
_CucsSwFcServerZoneGroupServerDn_Object = MibTableColumn
cucsSwFcServerZoneGroupServerDn = _CucsSwFcServerZoneGroupServerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 56, 1, 9),
    _CucsSwFcServerZoneGroupServerDn_Type()
)
cucsSwFcServerZoneGroupServerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcServerZoneGroupServerDn.setStatus("current")
_CucsSwFcZoneTable_Object = MibTable
cucsSwFcZoneTable = _CucsSwFcZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57)
)
if mibBuilder.loadTexts:
    cucsSwFcZoneTable.setStatus("current")
_CucsSwFcZoneEntry_Object = MibTableRow
cucsSwFcZoneEntry = _CucsSwFcZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1)
)
cucsSwFcZoneEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcZoneInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcZoneEntry.setStatus("current")
_CucsSwFcZoneInstanceId_Type = CucsManagedObjectId
_CucsSwFcZoneInstanceId_Object = MibTableColumn
cucsSwFcZoneInstanceId = _CucsSwFcZoneInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 1),
    _CucsSwFcZoneInstanceId_Type()
)
cucsSwFcZoneInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcZoneInstanceId.setStatus("current")
_CucsSwFcZoneDn_Type = CucsManagedObjectDn
_CucsSwFcZoneDn_Object = MibTableColumn
cucsSwFcZoneDn = _CucsSwFcZoneDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 2),
    _CucsSwFcZoneDn_Type()
)
cucsSwFcZoneDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneDn.setStatus("current")
_CucsSwFcZoneRn_Type = SnmpAdminString
_CucsSwFcZoneRn_Object = MibTableColumn
cucsSwFcZoneRn = _CucsSwFcZoneRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 3),
    _CucsSwFcZoneRn_Type()
)
cucsSwFcZoneRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneRn.setStatus("current")
_CucsSwFcZoneId_Type = Gauge32
_CucsSwFcZoneId_Object = MibTableColumn
cucsSwFcZoneId = _CucsSwFcZoneId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 4),
    _CucsSwFcZoneId_Type()
)
cucsSwFcZoneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneId.setStatus("current")
_CucsSwFcZoneIdentity_Type = SnmpAdminString
_CucsSwFcZoneIdentity_Object = MibTableColumn
cucsSwFcZoneIdentity = _CucsSwFcZoneIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 5),
    _CucsSwFcZoneIdentity_Type()
)
cucsSwFcZoneIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneIdentity.setStatus("current")
_CucsSwFcZoneLc_Type = CucsSwFcZoneLc
_CucsSwFcZoneLc_Object = MibTableColumn
cucsSwFcZoneLc = _CucsSwFcZoneLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 6),
    _CucsSwFcZoneLc_Type()
)
cucsSwFcZoneLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneLc.setStatus("current")
_CucsSwFcZoneName_Type = SnmpAdminString
_CucsSwFcZoneName_Object = MibTableColumn
cucsSwFcZoneName = _CucsSwFcZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 7),
    _CucsSwFcZoneName_Type()
)
cucsSwFcZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneName.setStatus("current")
_CucsSwFcZoneOperState_Type = CucsLsFcZoneState
_CucsSwFcZoneOperState_Object = MibTableColumn
cucsSwFcZoneOperState = _CucsSwFcZoneOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 8),
    _CucsSwFcZoneOperState_Type()
)
cucsSwFcZoneOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneOperState.setStatus("current")
_CucsSwFcZonePeerDn_Type = SnmpAdminString
_CucsSwFcZonePeerDn_Object = MibTableColumn
cucsSwFcZonePeerDn = _CucsSwFcZonePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 57, 1, 9),
    _CucsSwFcZonePeerDn_Type()
)
cucsSwFcZonePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZonePeerDn.setStatus("current")
_CucsSwFcZoneSetTable_Object = MibTable
cucsSwFcZoneSetTable = _CucsSwFcZoneSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58)
)
if mibBuilder.loadTexts:
    cucsSwFcZoneSetTable.setStatus("current")
_CucsSwFcZoneSetEntry_Object = MibTableRow
cucsSwFcZoneSetEntry = _CucsSwFcZoneSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58, 1)
)
cucsSwFcZoneSetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcZoneSetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcZoneSetEntry.setStatus("current")
_CucsSwFcZoneSetInstanceId_Type = CucsManagedObjectId
_CucsSwFcZoneSetInstanceId_Object = MibTableColumn
cucsSwFcZoneSetInstanceId = _CucsSwFcZoneSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58, 1, 1),
    _CucsSwFcZoneSetInstanceId_Type()
)
cucsSwFcZoneSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcZoneSetInstanceId.setStatus("current")
_CucsSwFcZoneSetDn_Type = CucsManagedObjectDn
_CucsSwFcZoneSetDn_Object = MibTableColumn
cucsSwFcZoneSetDn = _CucsSwFcZoneSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58, 1, 2),
    _CucsSwFcZoneSetDn_Type()
)
cucsSwFcZoneSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneSetDn.setStatus("current")
_CucsSwFcZoneSetRn_Type = SnmpAdminString
_CucsSwFcZoneSetRn_Object = MibTableColumn
cucsSwFcZoneSetRn = _CucsSwFcZoneSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58, 1, 3),
    _CucsSwFcZoneSetRn_Type()
)
cucsSwFcZoneSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneSetRn.setStatus("current")
_CucsSwFcZoneSetCurrentZonePrefix_Type = SnmpAdminString
_CucsSwFcZoneSetCurrentZonePrefix_Object = MibTableColumn
cucsSwFcZoneSetCurrentZonePrefix = _CucsSwFcZoneSetCurrentZonePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58, 1, 4),
    _CucsSwFcZoneSetCurrentZonePrefix_Type()
)
cucsSwFcZoneSetCurrentZonePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneSetCurrentZonePrefix.setStatus("current")
_CucsSwFcZoneSetLc_Type = CucsSwFcZoneSetLc
_CucsSwFcZoneSetLc_Object = MibTableColumn
cucsSwFcZoneSetLc = _CucsSwFcZoneSetLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58, 1, 5),
    _CucsSwFcZoneSetLc_Type()
)
cucsSwFcZoneSetLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneSetLc.setStatus("current")
_CucsSwFcZoneSetName_Type = SnmpAdminString
_CucsSwFcZoneSetName_Object = MibTableColumn
cucsSwFcZoneSetName = _CucsSwFcZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58, 1, 6),
    _CucsSwFcZoneSetName_Type()
)
cucsSwFcZoneSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneSetName.setStatus("current")
_CucsSwFcZoneSetOldZonePrefix_Type = SnmpAdminString
_CucsSwFcZoneSetOldZonePrefix_Object = MibTableColumn
cucsSwFcZoneSetOldZonePrefix = _CucsSwFcZoneSetOldZonePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 58, 1, 7),
    _CucsSwFcZoneSetOldZonePrefix_Type()
)
cucsSwFcZoneSetOldZonePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcZoneSetOldZonePrefix.setStatus("current")
_CucsSwFcoeSanEpTable_Object = MibTable
cucsSwFcoeSanEpTable = _CucsSwFcoeSanEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59)
)
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpTable.setStatus("current")
_CucsSwFcoeSanEpEntry_Object = MibTableRow
cucsSwFcoeSanEpEntry = _CucsSwFcoeSanEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1)
)
cucsSwFcoeSanEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcoeSanEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpEntry.setStatus("current")
_CucsSwFcoeSanEpInstanceId_Type = CucsManagedObjectId
_CucsSwFcoeSanEpInstanceId_Object = MibTableColumn
cucsSwFcoeSanEpInstanceId = _CucsSwFcoeSanEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 1),
    _CucsSwFcoeSanEpInstanceId_Type()
)
cucsSwFcoeSanEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpInstanceId.setStatus("current")
_CucsSwFcoeSanEpDn_Type = CucsManagedObjectDn
_CucsSwFcoeSanEpDn_Object = MibTableColumn
cucsSwFcoeSanEpDn = _CucsSwFcoeSanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 2),
    _CucsSwFcoeSanEpDn_Type()
)
cucsSwFcoeSanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpDn.setStatus("current")
_CucsSwFcoeSanEpRn_Type = SnmpAdminString
_CucsSwFcoeSanEpRn_Object = MibTableColumn
cucsSwFcoeSanEpRn = _CucsSwFcoeSanEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 3),
    _CucsSwFcoeSanEpRn_Type()
)
cucsSwFcoeSanEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpRn.setStatus("current")
_CucsSwFcoeSanEpAdminSpeed_Type = CucsPortEthAdminSpeed
_CucsSwFcoeSanEpAdminSpeed_Object = MibTableColumn
cucsSwFcoeSanEpAdminSpeed = _CucsSwFcoeSanEpAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 4),
    _CucsSwFcoeSanEpAdminSpeed_Type()
)
cucsSwFcoeSanEpAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpAdminSpeed.setStatus("current")
_CucsSwFcoeSanEpAdminState_Type = CucsFabricAdminState
_CucsSwFcoeSanEpAdminState_Object = MibTableColumn
cucsSwFcoeSanEpAdminState = _CucsSwFcoeSanEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 5),
    _CucsSwFcoeSanEpAdminState_Type()
)
cucsSwFcoeSanEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpAdminState.setStatus("current")
_CucsSwFcoeSanEpChassisId_Type = Gauge32
_CucsSwFcoeSanEpChassisId_Object = MibTableColumn
cucsSwFcoeSanEpChassisId = _CucsSwFcoeSanEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 6),
    _CucsSwFcoeSanEpChassisId_Type()
)
cucsSwFcoeSanEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpChassisId.setStatus("current")
_CucsSwFcoeSanEpEpDn_Type = SnmpAdminString
_CucsSwFcoeSanEpEpDn_Object = MibTableColumn
cucsSwFcoeSanEpEpDn = _CucsSwFcoeSanEpEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 7),
    _CucsSwFcoeSanEpEpDn_Type()
)
cucsSwFcoeSanEpEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpEpDn.setStatus("current")
_CucsSwFcoeSanEpIfRole_Type = CucsSwSanEpIfRole
_CucsSwFcoeSanEpIfRole_Object = MibTableColumn
cucsSwFcoeSanEpIfRole = _CucsSwFcoeSanEpIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 8),
    _CucsSwFcoeSanEpIfRole_Type()
)
cucsSwFcoeSanEpIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpIfRole.setStatus("current")
_CucsSwFcoeSanEpIfType_Type = CucsSwPIoEpIfType
_CucsSwFcoeSanEpIfType_Object = MibTableColumn
cucsSwFcoeSanEpIfType = _CucsSwFcoeSanEpIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 9),
    _CucsSwFcoeSanEpIfType_Type()
)
cucsSwFcoeSanEpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpIfType.setStatus("current")
_CucsSwFcoeSanEpLc_Type = CucsSwPIoEpLc
_CucsSwFcoeSanEpLc_Object = MibTableColumn
cucsSwFcoeSanEpLc = _CucsSwFcoeSanEpLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 10),
    _CucsSwFcoeSanEpLc_Type()
)
cucsSwFcoeSanEpLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpLc.setStatus("current")
_CucsSwFcoeSanEpLocale_Type = CucsSwBorderEpLocale
_CucsSwFcoeSanEpLocale_Object = MibTableColumn
cucsSwFcoeSanEpLocale = _CucsSwFcoeSanEpLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 11),
    _CucsSwFcoeSanEpLocale_Type()
)
cucsSwFcoeSanEpLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpLocale.setStatus("current")
_CucsSwFcoeSanEpName_Type = SnmpAdminString
_CucsSwFcoeSanEpName_Object = MibTableColumn
cucsSwFcoeSanEpName = _CucsSwFcoeSanEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 12),
    _CucsSwFcoeSanEpName_Type()
)
cucsSwFcoeSanEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpName.setStatus("current")
_CucsSwFcoeSanEpPcId_Type = Gauge32
_CucsSwFcoeSanEpPcId_Object = MibTableColumn
cucsSwFcoeSanEpPcId = _CucsSwFcoeSanEpPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 13),
    _CucsSwFcoeSanEpPcId_Type()
)
cucsSwFcoeSanEpPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPcId.setStatus("current")
_CucsSwFcoeSanEpPeerChassisId_Type = Gauge32
_CucsSwFcoeSanEpPeerChassisId_Object = MibTableColumn
cucsSwFcoeSanEpPeerChassisId = _CucsSwFcoeSanEpPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 14),
    _CucsSwFcoeSanEpPeerChassisId_Type()
)
cucsSwFcoeSanEpPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPeerChassisId.setStatus("current")
_CucsSwFcoeSanEpPeerDn_Type = SnmpAdminString
_CucsSwFcoeSanEpPeerDn_Object = MibTableColumn
cucsSwFcoeSanEpPeerDn = _CucsSwFcoeSanEpPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 15),
    _CucsSwFcoeSanEpPeerDn_Type()
)
cucsSwFcoeSanEpPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPeerDn.setStatus("current")
_CucsSwFcoeSanEpPeerPortId_Type = Gauge32
_CucsSwFcoeSanEpPeerPortId_Object = MibTableColumn
cucsSwFcoeSanEpPeerPortId = _CucsSwFcoeSanEpPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 16),
    _CucsSwFcoeSanEpPeerPortId_Type()
)
cucsSwFcoeSanEpPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPeerPortId.setStatus("current")
_CucsSwFcoeSanEpPeerSlotId_Type = Gauge32
_CucsSwFcoeSanEpPeerSlotId_Object = MibTableColumn
cucsSwFcoeSanEpPeerSlotId = _CucsSwFcoeSanEpPeerSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 17),
    _CucsSwFcoeSanEpPeerSlotId_Type()
)
cucsSwFcoeSanEpPeerSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPeerSlotId.setStatus("current")
_CucsSwFcoeSanEpPeerState_Type = CucsSwPeerStatus
_CucsSwFcoeSanEpPeerState_Object = MibTableColumn
cucsSwFcoeSanEpPeerState = _CucsSwFcoeSanEpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 18),
    _CucsSwFcoeSanEpPeerState_Type()
)
cucsSwFcoeSanEpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPeerState.setStatus("current")
_CucsSwFcoeSanEpPortId_Type = Gauge32
_CucsSwFcoeSanEpPortId_Object = MibTableColumn
cucsSwFcoeSanEpPortId = _CucsSwFcoeSanEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 19),
    _CucsSwFcoeSanEpPortId_Type()
)
cucsSwFcoeSanEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPortId.setStatus("current")
_CucsSwFcoeSanEpPortVsanId_Type = Gauge32
_CucsSwFcoeSanEpPortVsanId_Object = MibTableColumn
cucsSwFcoeSanEpPortVsanId = _CucsSwFcoeSanEpPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 20),
    _CucsSwFcoeSanEpPortVsanId_Type()
)
cucsSwFcoeSanEpPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPortVsanId.setStatus("current")
_CucsSwFcoeSanEpSlotId_Type = Gauge32
_CucsSwFcoeSanEpSlotId_Object = MibTableColumn
cucsSwFcoeSanEpSlotId = _CucsSwFcoeSanEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 21),
    _CucsSwFcoeSanEpSlotId_Type()
)
cucsSwFcoeSanEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpSlotId.setStatus("current")
_CucsSwFcoeSanEpSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcoeSanEpSwitchId_Object = MibTableColumn
cucsSwFcoeSanEpSwitchId = _CucsSwFcoeSanEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 22),
    _CucsSwFcoeSanEpSwitchId_Type()
)
cucsSwFcoeSanEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpSwitchId.setStatus("current")
_CucsSwFcoeSanEpTransport_Type = CucsSwFcoeSanEpTransport
_CucsSwFcoeSanEpTransport_Object = MibTableColumn
cucsSwFcoeSanEpTransport = _CucsSwFcoeSanEpTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 23),
    _CucsSwFcoeSanEpTransport_Type()
)
cucsSwFcoeSanEpTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpTransport.setStatus("current")
_CucsSwFcoeSanEpType_Type = CucsSwSanEpType
_CucsSwFcoeSanEpType_Object = MibTableColumn
cucsSwFcoeSanEpType = _CucsSwFcoeSanEpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 24),
    _CucsSwFcoeSanEpType_Type()
)
cucsSwFcoeSanEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpType.setStatus("current")
_CucsSwFcoeSanEpUdldAdminState_Type = CucsSwFcoeSanEpUdldAdminState
_CucsSwFcoeSanEpUdldAdminState_Object = MibTableColumn
cucsSwFcoeSanEpUdldAdminState = _CucsSwFcoeSanEpUdldAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 25),
    _CucsSwFcoeSanEpUdldAdminState_Type()
)
cucsSwFcoeSanEpUdldAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpUdldAdminState.setStatus("current")
_CucsSwFcoeSanEpUdldMode_Type = CucsSwFcoeSanEpUdldMode
_CucsSwFcoeSanEpUdldMode_Object = MibTableColumn
cucsSwFcoeSanEpUdldMode = _CucsSwFcoeSanEpUdldMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 26),
    _CucsSwFcoeSanEpUdldMode_Type()
)
cucsSwFcoeSanEpUdldMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpUdldMode.setStatus("current")
_CucsSwFcoeSanEpAggrPortId_Type = Gauge32
_CucsSwFcoeSanEpAggrPortId_Object = MibTableColumn
cucsSwFcoeSanEpAggrPortId = _CucsSwFcoeSanEpAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 27),
    _CucsSwFcoeSanEpAggrPortId_Type()
)
cucsSwFcoeSanEpAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpAggrPortId.setStatus("current")
_CucsSwFcoeSanEpPeerAggrPortId_Type = Gauge32
_CucsSwFcoeSanEpPeerAggrPortId_Object = MibTableColumn
cucsSwFcoeSanEpPeerAggrPortId = _CucsSwFcoeSanEpPeerAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 28),
    _CucsSwFcoeSanEpPeerAggrPortId_Type()
)
cucsSwFcoeSanEpPeerAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpPeerAggrPortId.setStatus("current")
_CucsSwFcoeSanEpAutoNegotiate_Type = CucsSwAutoNegMode
_CucsSwFcoeSanEpAutoNegotiate_Object = MibTableColumn
cucsSwFcoeSanEpAutoNegotiate = _CucsSwFcoeSanEpAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 59, 1, 29),
    _CucsSwFcoeSanEpAutoNegotiate_Type()
)
cucsSwFcoeSanEpAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanEpAutoNegotiate.setStatus("current")
_CucsSwFcoeSanPcTable_Object = MibTable
cucsSwFcoeSanPcTable = _CucsSwFcoeSanPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60)
)
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcTable.setStatus("current")
_CucsSwFcoeSanPcEntry_Object = MibTableRow
cucsSwFcoeSanPcEntry = _CucsSwFcoeSanPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1)
)
cucsSwFcoeSanPcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwFcoeSanPcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcEntry.setStatus("current")
_CucsSwFcoeSanPcInstanceId_Type = CucsManagedObjectId
_CucsSwFcoeSanPcInstanceId_Object = MibTableColumn
cucsSwFcoeSanPcInstanceId = _CucsSwFcoeSanPcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 1),
    _CucsSwFcoeSanPcInstanceId_Type()
)
cucsSwFcoeSanPcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcInstanceId.setStatus("current")
_CucsSwFcoeSanPcDn_Type = CucsManagedObjectDn
_CucsSwFcoeSanPcDn_Object = MibTableColumn
cucsSwFcoeSanPcDn = _CucsSwFcoeSanPcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 2),
    _CucsSwFcoeSanPcDn_Type()
)
cucsSwFcoeSanPcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcDn.setStatus("current")
_CucsSwFcoeSanPcRn_Type = SnmpAdminString
_CucsSwFcoeSanPcRn_Object = MibTableColumn
cucsSwFcoeSanPcRn = _CucsSwFcoeSanPcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 3),
    _CucsSwFcoeSanPcRn_Type()
)
cucsSwFcoeSanPcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcRn.setStatus("current")
_CucsSwFcoeSanPcAdminState_Type = CucsFabricAdminState
_CucsSwFcoeSanPcAdminState_Object = MibTableColumn
cucsSwFcoeSanPcAdminState = _CucsSwFcoeSanPcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 4),
    _CucsSwFcoeSanPcAdminState_Type()
)
cucsSwFcoeSanPcAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcAdminState.setStatus("current")
_CucsSwFcoeSanPcEpDn_Type = SnmpAdminString
_CucsSwFcoeSanPcEpDn_Object = MibTableColumn
cucsSwFcoeSanPcEpDn = _CucsSwFcoeSanPcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 5),
    _CucsSwFcoeSanPcEpDn_Type()
)
cucsSwFcoeSanPcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcEpDn.setStatus("current")
_CucsSwFcoeSanPcIfRole_Type = CucsSwSanPcIfRole
_CucsSwFcoeSanPcIfRole_Object = MibTableColumn
cucsSwFcoeSanPcIfRole = _CucsSwFcoeSanPcIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 6),
    _CucsSwFcoeSanPcIfRole_Type()
)
cucsSwFcoeSanPcIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcIfRole.setStatus("current")
_CucsSwFcoeSanPcIfType_Type = CucsSwCIoEpIfType
_CucsSwFcoeSanPcIfType_Object = MibTableColumn
cucsSwFcoeSanPcIfType = _CucsSwFcoeSanPcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 7),
    _CucsSwFcoeSanPcIfType_Type()
)
cucsSwFcoeSanPcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcIfType.setStatus("current")
_CucsSwFcoeSanPcLocale_Type = CucsSwBorderPcLocale
_CucsSwFcoeSanPcLocale_Object = MibTableColumn
cucsSwFcoeSanPcLocale = _CucsSwFcoeSanPcLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 8),
    _CucsSwFcoeSanPcLocale_Type()
)
cucsSwFcoeSanPcLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcLocale.setStatus("current")
_CucsSwFcoeSanPcMonTrafDir_Type = CucsFabricTrafficDirection
_CucsSwFcoeSanPcMonTrafDir_Object = MibTableColumn
cucsSwFcoeSanPcMonTrafDir = _CucsSwFcoeSanPcMonTrafDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 9),
    _CucsSwFcoeSanPcMonTrafDir_Type()
)
cucsSwFcoeSanPcMonTrafDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcMonTrafDir.setStatus("current")
_CucsSwFcoeSanPcName_Type = SnmpAdminString
_CucsSwFcoeSanPcName_Object = MibTableColumn
cucsSwFcoeSanPcName = _CucsSwFcoeSanPcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 10),
    _CucsSwFcoeSanPcName_Type()
)
cucsSwFcoeSanPcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcName.setStatus("current")
_CucsSwFcoeSanPcPcId_Type = Gauge32
_CucsSwFcoeSanPcPcId_Object = MibTableColumn
cucsSwFcoeSanPcPcId = _CucsSwFcoeSanPcPcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 11),
    _CucsSwFcoeSanPcPcId_Type()
)
cucsSwFcoeSanPcPcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcPcId.setStatus("current")
_CucsSwFcoeSanPcPeerDn_Type = SnmpAdminString
_CucsSwFcoeSanPcPeerDn_Object = MibTableColumn
cucsSwFcoeSanPcPeerDn = _CucsSwFcoeSanPcPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 12),
    _CucsSwFcoeSanPcPeerDn_Type()
)
cucsSwFcoeSanPcPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcPeerDn.setStatus("current")
_CucsSwFcoeSanPcPeerState_Type = CucsSwPeerStatus
_CucsSwFcoeSanPcPeerState_Object = MibTableColumn
cucsSwFcoeSanPcPeerState = _CucsSwFcoeSanPcPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 13),
    _CucsSwFcoeSanPcPeerState_Type()
)
cucsSwFcoeSanPcPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcPeerState.setStatus("current")
_CucsSwFcoeSanPcPortId_Type = Gauge32
_CucsSwFcoeSanPcPortId_Object = MibTableColumn
cucsSwFcoeSanPcPortId = _CucsSwFcoeSanPcPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 14),
    _CucsSwFcoeSanPcPortId_Type()
)
cucsSwFcoeSanPcPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcPortId.setStatus("current")
_CucsSwFcoeSanPcPortVsanId_Type = Gauge32
_CucsSwFcoeSanPcPortVsanId_Object = MibTableColumn
cucsSwFcoeSanPcPortVsanId = _CucsSwFcoeSanPcPortVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 15),
    _CucsSwFcoeSanPcPortVsanId_Type()
)
cucsSwFcoeSanPcPortVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcPortVsanId.setStatus("current")
_CucsSwFcoeSanPcSwitchId_Type = CucsNetworkSwitchId
_CucsSwFcoeSanPcSwitchId_Object = MibTableColumn
cucsSwFcoeSanPcSwitchId = _CucsSwFcoeSanPcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 16),
    _CucsSwFcoeSanPcSwitchId_Type()
)
cucsSwFcoeSanPcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcSwitchId.setStatus("current")
_CucsSwFcoeSanPcTransport_Type = CucsSwFcoeSanPcTransport
_CucsSwFcoeSanPcTransport_Object = MibTableColumn
cucsSwFcoeSanPcTransport = _CucsSwFcoeSanPcTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 17),
    _CucsSwFcoeSanPcTransport_Type()
)
cucsSwFcoeSanPcTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcTransport.setStatus("current")
_CucsSwFcoeSanPcType_Type = CucsSwSanPcType
_CucsSwFcoeSanPcType_Object = MibTableColumn
cucsSwFcoeSanPcType = _CucsSwFcoeSanPcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 18),
    _CucsSwFcoeSanPcType_Type()
)
cucsSwFcoeSanPcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcType.setStatus("current")
_CucsSwFcoeSanPcLacpFastTimer_Type = TruthValue
_CucsSwFcoeSanPcLacpFastTimer_Object = MibTableColumn
cucsSwFcoeSanPcLacpFastTimer = _CucsSwFcoeSanPcLacpFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 19),
    _CucsSwFcoeSanPcLacpFastTimer_Type()
)
cucsSwFcoeSanPcLacpFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcLacpFastTimer.setStatus("current")
_CucsSwFcoeSanPcLacpSuspendIndividual_Type = TruthValue
_CucsSwFcoeSanPcLacpSuspendIndividual_Object = MibTableColumn
cucsSwFcoeSanPcLacpSuspendIndividual = _CucsSwFcoeSanPcLacpSuspendIndividual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 20),
    _CucsSwFcoeSanPcLacpSuspendIndividual_Type()
)
cucsSwFcoeSanPcLacpSuspendIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcLacpSuspendIndividual.setStatus("current")
_CucsSwFcoeSanPcAdminSpeed_Type = CucsPortEthAdminSpeed
_CucsSwFcoeSanPcAdminSpeed_Object = MibTableColumn
cucsSwFcoeSanPcAdminSpeed = _CucsSwFcoeSanPcAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 60, 1, 21),
    _CucsSwFcoeSanPcAdminSpeed_Type()
)
cucsSwFcoeSanPcAdminSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwFcoeSanPcAdminSpeed.setStatus("current")
_CucsSwPhysFsmTable_Object = MibTable
cucsSwPhysFsmTable = _CucsSwPhysFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61)
)
if mibBuilder.loadTexts:
    cucsSwPhysFsmTable.setStatus("current")
_CucsSwPhysFsmEntry_Object = MibTableRow
cucsSwPhysFsmEntry = _CucsSwPhysFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1)
)
cucsSwPhysFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwPhysFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwPhysFsmEntry.setStatus("current")
_CucsSwPhysFsmInstanceId_Type = CucsManagedObjectId
_CucsSwPhysFsmInstanceId_Object = MibTableColumn
cucsSwPhysFsmInstanceId = _CucsSwPhysFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 1),
    _CucsSwPhysFsmInstanceId_Type()
)
cucsSwPhysFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwPhysFsmInstanceId.setStatus("current")
_CucsSwPhysFsmDn_Type = CucsManagedObjectDn
_CucsSwPhysFsmDn_Object = MibTableColumn
cucsSwPhysFsmDn = _CucsSwPhysFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 2),
    _CucsSwPhysFsmDn_Type()
)
cucsSwPhysFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmDn.setStatus("current")
_CucsSwPhysFsmRn_Type = SnmpAdminString
_CucsSwPhysFsmRn_Object = MibTableColumn
cucsSwPhysFsmRn = _CucsSwPhysFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 3),
    _CucsSwPhysFsmRn_Type()
)
cucsSwPhysFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmRn.setStatus("current")
_CucsSwPhysFsmCompletionTime_Type = DateAndTime
_CucsSwPhysFsmCompletionTime_Object = MibTableColumn
cucsSwPhysFsmCompletionTime = _CucsSwPhysFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 4),
    _CucsSwPhysFsmCompletionTime_Type()
)
cucsSwPhysFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmCompletionTime.setStatus("current")
_CucsSwPhysFsmCurrentFsm_Type = CucsSwPhysFsmCurrentFsm
_CucsSwPhysFsmCurrentFsm_Object = MibTableColumn
cucsSwPhysFsmCurrentFsm = _CucsSwPhysFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 5),
    _CucsSwPhysFsmCurrentFsm_Type()
)
cucsSwPhysFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmCurrentFsm.setStatus("current")
_CucsSwPhysFsmDescrData_Type = SnmpAdminString
_CucsSwPhysFsmDescrData_Object = MibTableColumn
cucsSwPhysFsmDescrData = _CucsSwPhysFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 6),
    _CucsSwPhysFsmDescrData_Type()
)
cucsSwPhysFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmDescrData.setStatus("current")
_CucsSwPhysFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwPhysFsmFsmStatus_Object = MibTableColumn
cucsSwPhysFsmFsmStatus = _CucsSwPhysFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 7),
    _CucsSwPhysFsmFsmStatus_Type()
)
cucsSwPhysFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmFsmStatus.setStatus("current")
_CucsSwPhysFsmProgress_Type = Gauge32
_CucsSwPhysFsmProgress_Object = MibTableColumn
cucsSwPhysFsmProgress = _CucsSwPhysFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 8),
    _CucsSwPhysFsmProgress_Type()
)
cucsSwPhysFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmProgress.setStatus("current")
_CucsSwPhysFsmRmtErrCode_Type = Gauge32
_CucsSwPhysFsmRmtErrCode_Object = MibTableColumn
cucsSwPhysFsmRmtErrCode = _CucsSwPhysFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 9),
    _CucsSwPhysFsmRmtErrCode_Type()
)
cucsSwPhysFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmRmtErrCode.setStatus("current")
_CucsSwPhysFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwPhysFsmRmtErrDescr_Object = MibTableColumn
cucsSwPhysFsmRmtErrDescr = _CucsSwPhysFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 10),
    _CucsSwPhysFsmRmtErrDescr_Type()
)
cucsSwPhysFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmRmtErrDescr.setStatus("current")
_CucsSwPhysFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwPhysFsmRmtRslt_Object = MibTableColumn
cucsSwPhysFsmRmtRslt = _CucsSwPhysFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 61, 1, 11),
    _CucsSwPhysFsmRmtRslt_Type()
)
cucsSwPhysFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmRmtRslt.setStatus("current")
_CucsSwPhysFsmStageTable_Object = MibTable
cucsSwPhysFsmStageTable = _CucsSwPhysFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62)
)
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageTable.setStatus("current")
_CucsSwPhysFsmStageEntry_Object = MibTableRow
cucsSwPhysFsmStageEntry = _CucsSwPhysFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1)
)
cucsSwPhysFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwPhysFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageEntry.setStatus("current")
_CucsSwPhysFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwPhysFsmStageInstanceId_Object = MibTableColumn
cucsSwPhysFsmStageInstanceId = _CucsSwPhysFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 1),
    _CucsSwPhysFsmStageInstanceId_Type()
)
cucsSwPhysFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageInstanceId.setStatus("current")
_CucsSwPhysFsmStageDn_Type = CucsManagedObjectDn
_CucsSwPhysFsmStageDn_Object = MibTableColumn
cucsSwPhysFsmStageDn = _CucsSwPhysFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 2),
    _CucsSwPhysFsmStageDn_Type()
)
cucsSwPhysFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageDn.setStatus("current")
_CucsSwPhysFsmStageRn_Type = SnmpAdminString
_CucsSwPhysFsmStageRn_Object = MibTableColumn
cucsSwPhysFsmStageRn = _CucsSwPhysFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 3),
    _CucsSwPhysFsmStageRn_Type()
)
cucsSwPhysFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageRn.setStatus("current")
_CucsSwPhysFsmStageDescrData_Type = SnmpAdminString
_CucsSwPhysFsmStageDescrData_Object = MibTableColumn
cucsSwPhysFsmStageDescrData = _CucsSwPhysFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 4),
    _CucsSwPhysFsmStageDescrData_Type()
)
cucsSwPhysFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageDescrData.setStatus("current")
_CucsSwPhysFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwPhysFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwPhysFsmStageLastUpdateTime = _CucsSwPhysFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 5),
    _CucsSwPhysFsmStageLastUpdateTime_Type()
)
cucsSwPhysFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageLastUpdateTime.setStatus("current")
_CucsSwPhysFsmStageName_Type = CucsSwPhysFsmStageName
_CucsSwPhysFsmStageName_Object = MibTableColumn
cucsSwPhysFsmStageName = _CucsSwPhysFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 6),
    _CucsSwPhysFsmStageName_Type()
)
cucsSwPhysFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageName.setStatus("current")
_CucsSwPhysFsmStageOrder_Type = Gauge32
_CucsSwPhysFsmStageOrder_Object = MibTableColumn
cucsSwPhysFsmStageOrder = _CucsSwPhysFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 7),
    _CucsSwPhysFsmStageOrder_Type()
)
cucsSwPhysFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageOrder.setStatus("current")
_CucsSwPhysFsmStageRetry_Type = Gauge32
_CucsSwPhysFsmStageRetry_Object = MibTableColumn
cucsSwPhysFsmStageRetry = _CucsSwPhysFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 8),
    _CucsSwPhysFsmStageRetry_Type()
)
cucsSwPhysFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageRetry.setStatus("current")
_CucsSwPhysFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwPhysFsmStageStageStatus_Object = MibTableColumn
cucsSwPhysFsmStageStageStatus = _CucsSwPhysFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 62, 1, 9),
    _CucsSwPhysFsmStageStageStatus_Type()
)
cucsSwPhysFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPhysFsmStageStageStatus.setStatus("current")
_CucsSwUtilityDomainFsmTable_Object = MibTable
cucsSwUtilityDomainFsmTable = _CucsSwUtilityDomainFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63)
)
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmTable.setStatus("current")
_CucsSwUtilityDomainFsmEntry_Object = MibTableRow
cucsSwUtilityDomainFsmEntry = _CucsSwUtilityDomainFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1)
)
cucsSwUtilityDomainFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwUtilityDomainFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmEntry.setStatus("current")
_CucsSwUtilityDomainFsmInstanceId_Type = CucsManagedObjectId
_CucsSwUtilityDomainFsmInstanceId_Object = MibTableColumn
cucsSwUtilityDomainFsmInstanceId = _CucsSwUtilityDomainFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 1),
    _CucsSwUtilityDomainFsmInstanceId_Type()
)
cucsSwUtilityDomainFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmInstanceId.setStatus("current")
_CucsSwUtilityDomainFsmDn_Type = CucsManagedObjectDn
_CucsSwUtilityDomainFsmDn_Object = MibTableColumn
cucsSwUtilityDomainFsmDn = _CucsSwUtilityDomainFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 2),
    _CucsSwUtilityDomainFsmDn_Type()
)
cucsSwUtilityDomainFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmDn.setStatus("current")
_CucsSwUtilityDomainFsmRn_Type = SnmpAdminString
_CucsSwUtilityDomainFsmRn_Object = MibTableColumn
cucsSwUtilityDomainFsmRn = _CucsSwUtilityDomainFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 3),
    _CucsSwUtilityDomainFsmRn_Type()
)
cucsSwUtilityDomainFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmRn.setStatus("current")
_CucsSwUtilityDomainFsmCompletionTime_Type = DateAndTime
_CucsSwUtilityDomainFsmCompletionTime_Object = MibTableColumn
cucsSwUtilityDomainFsmCompletionTime = _CucsSwUtilityDomainFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 4),
    _CucsSwUtilityDomainFsmCompletionTime_Type()
)
cucsSwUtilityDomainFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmCompletionTime.setStatus("current")
_CucsSwUtilityDomainFsmCurrentFsm_Type = CucsSwUtilityDomainFsmCurrentFsm
_CucsSwUtilityDomainFsmCurrentFsm_Object = MibTableColumn
cucsSwUtilityDomainFsmCurrentFsm = _CucsSwUtilityDomainFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 5),
    _CucsSwUtilityDomainFsmCurrentFsm_Type()
)
cucsSwUtilityDomainFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmCurrentFsm.setStatus("current")
_CucsSwUtilityDomainFsmDescrData_Type = SnmpAdminString
_CucsSwUtilityDomainFsmDescrData_Object = MibTableColumn
cucsSwUtilityDomainFsmDescrData = _CucsSwUtilityDomainFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 6),
    _CucsSwUtilityDomainFsmDescrData_Type()
)
cucsSwUtilityDomainFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmDescrData.setStatus("current")
_CucsSwUtilityDomainFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwUtilityDomainFsmFsmStatus_Object = MibTableColumn
cucsSwUtilityDomainFsmFsmStatus = _CucsSwUtilityDomainFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 7),
    _CucsSwUtilityDomainFsmFsmStatus_Type()
)
cucsSwUtilityDomainFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmFsmStatus.setStatus("current")
_CucsSwUtilityDomainFsmProgress_Type = Gauge32
_CucsSwUtilityDomainFsmProgress_Object = MibTableColumn
cucsSwUtilityDomainFsmProgress = _CucsSwUtilityDomainFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 8),
    _CucsSwUtilityDomainFsmProgress_Type()
)
cucsSwUtilityDomainFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmProgress.setStatus("current")
_CucsSwUtilityDomainFsmRmtErrCode_Type = Gauge32
_CucsSwUtilityDomainFsmRmtErrCode_Object = MibTableColumn
cucsSwUtilityDomainFsmRmtErrCode = _CucsSwUtilityDomainFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 9),
    _CucsSwUtilityDomainFsmRmtErrCode_Type()
)
cucsSwUtilityDomainFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmRmtErrCode.setStatus("current")
_CucsSwUtilityDomainFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwUtilityDomainFsmRmtErrDescr_Object = MibTableColumn
cucsSwUtilityDomainFsmRmtErrDescr = _CucsSwUtilityDomainFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 10),
    _CucsSwUtilityDomainFsmRmtErrDescr_Type()
)
cucsSwUtilityDomainFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmRmtErrDescr.setStatus("current")
_CucsSwUtilityDomainFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwUtilityDomainFsmRmtRslt_Object = MibTableColumn
cucsSwUtilityDomainFsmRmtRslt = _CucsSwUtilityDomainFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 63, 1, 11),
    _CucsSwUtilityDomainFsmRmtRslt_Type()
)
cucsSwUtilityDomainFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmRmtRslt.setStatus("current")
_CucsSwUtilityDomainFsmStageTable_Object = MibTable
cucsSwUtilityDomainFsmStageTable = _CucsSwUtilityDomainFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64)
)
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageTable.setStatus("current")
_CucsSwUtilityDomainFsmStageEntry_Object = MibTableRow
cucsSwUtilityDomainFsmStageEntry = _CucsSwUtilityDomainFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1)
)
cucsSwUtilityDomainFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwUtilityDomainFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageEntry.setStatus("current")
_CucsSwUtilityDomainFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwUtilityDomainFsmStageInstanceId_Object = MibTableColumn
cucsSwUtilityDomainFsmStageInstanceId = _CucsSwUtilityDomainFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 1),
    _CucsSwUtilityDomainFsmStageInstanceId_Type()
)
cucsSwUtilityDomainFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageInstanceId.setStatus("current")
_CucsSwUtilityDomainFsmStageDn_Type = CucsManagedObjectDn
_CucsSwUtilityDomainFsmStageDn_Object = MibTableColumn
cucsSwUtilityDomainFsmStageDn = _CucsSwUtilityDomainFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 2),
    _CucsSwUtilityDomainFsmStageDn_Type()
)
cucsSwUtilityDomainFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageDn.setStatus("current")
_CucsSwUtilityDomainFsmStageRn_Type = SnmpAdminString
_CucsSwUtilityDomainFsmStageRn_Object = MibTableColumn
cucsSwUtilityDomainFsmStageRn = _CucsSwUtilityDomainFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 3),
    _CucsSwUtilityDomainFsmStageRn_Type()
)
cucsSwUtilityDomainFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageRn.setStatus("current")
_CucsSwUtilityDomainFsmStageDescrData_Type = SnmpAdminString
_CucsSwUtilityDomainFsmStageDescrData_Object = MibTableColumn
cucsSwUtilityDomainFsmStageDescrData = _CucsSwUtilityDomainFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 4),
    _CucsSwUtilityDomainFsmStageDescrData_Type()
)
cucsSwUtilityDomainFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageDescrData.setStatus("current")
_CucsSwUtilityDomainFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwUtilityDomainFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwUtilityDomainFsmStageLastUpdateTime = _CucsSwUtilityDomainFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 5),
    _CucsSwUtilityDomainFsmStageLastUpdateTime_Type()
)
cucsSwUtilityDomainFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageLastUpdateTime.setStatus("current")
_CucsSwUtilityDomainFsmStageName_Type = CucsSwUtilityDomainFsmStageName
_CucsSwUtilityDomainFsmStageName_Object = MibTableColumn
cucsSwUtilityDomainFsmStageName = _CucsSwUtilityDomainFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 6),
    _CucsSwUtilityDomainFsmStageName_Type()
)
cucsSwUtilityDomainFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageName.setStatus("current")
_CucsSwUtilityDomainFsmStageOrder_Type = Gauge32
_CucsSwUtilityDomainFsmStageOrder_Object = MibTableColumn
cucsSwUtilityDomainFsmStageOrder = _CucsSwUtilityDomainFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 7),
    _CucsSwUtilityDomainFsmStageOrder_Type()
)
cucsSwUtilityDomainFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageOrder.setStatus("current")
_CucsSwUtilityDomainFsmStageRetry_Type = Gauge32
_CucsSwUtilityDomainFsmStageRetry_Object = MibTableColumn
cucsSwUtilityDomainFsmStageRetry = _CucsSwUtilityDomainFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 8),
    _CucsSwUtilityDomainFsmStageRetry_Type()
)
cucsSwUtilityDomainFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageRetry.setStatus("current")
_CucsSwUtilityDomainFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwUtilityDomainFsmStageStageStatus_Object = MibTableColumn
cucsSwUtilityDomainFsmStageStageStatus = _CucsSwUtilityDomainFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 64, 1, 9),
    _CucsSwUtilityDomainFsmStageStageStatus_Type()
)
cucsSwUtilityDomainFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwUtilityDomainFsmStageStageStatus.setStatus("current")
_CucsSwVlanGroupTable_Object = MibTable
cucsSwVlanGroupTable = _CucsSwVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65)
)
if mibBuilder.loadTexts:
    cucsSwVlanGroupTable.setStatus("current")
_CucsSwVlanGroupEntry_Object = MibTableRow
cucsSwVlanGroupEntry = _CucsSwVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1)
)
cucsSwVlanGroupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwVlanGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwVlanGroupEntry.setStatus("current")
_CucsSwVlanGroupInstanceId_Type = CucsManagedObjectId
_CucsSwVlanGroupInstanceId_Object = MibTableColumn
cucsSwVlanGroupInstanceId = _CucsSwVlanGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1, 1),
    _CucsSwVlanGroupInstanceId_Type()
)
cucsSwVlanGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwVlanGroupInstanceId.setStatus("current")
_CucsSwVlanGroupDn_Type = CucsManagedObjectDn
_CucsSwVlanGroupDn_Object = MibTableColumn
cucsSwVlanGroupDn = _CucsSwVlanGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1, 2),
    _CucsSwVlanGroupDn_Type()
)
cucsSwVlanGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanGroupDn.setStatus("current")
_CucsSwVlanGroupRn_Type = SnmpAdminString
_CucsSwVlanGroupRn_Object = MibTableColumn
cucsSwVlanGroupRn = _CucsSwVlanGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1, 3),
    _CucsSwVlanGroupRn_Type()
)
cucsSwVlanGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanGroupRn.setStatus("current")
_CucsSwVlanGroupId_Type = Gauge32
_CucsSwVlanGroupId_Object = MibTableColumn
cucsSwVlanGroupId = _CucsSwVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1, 4),
    _CucsSwVlanGroupId_Type()
)
cucsSwVlanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanGroupId.setStatus("current")
_CucsSwVlanGroupPeerDn_Type = SnmpAdminString
_CucsSwVlanGroupPeerDn_Object = MibTableColumn
cucsSwVlanGroupPeerDn = _CucsSwVlanGroupPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1, 5),
    _CucsSwVlanGroupPeerDn_Type()
)
cucsSwVlanGroupPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanGroupPeerDn.setStatus("current")
_CucsSwVlanGroupSwitchId_Type = CucsNetworkSwitchId
_CucsSwVlanGroupSwitchId_Object = MibTableColumn
cucsSwVlanGroupSwitchId = _CucsSwVlanGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1, 6),
    _CucsSwVlanGroupSwitchId_Type()
)
cucsSwVlanGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanGroupSwitchId.setStatus("current")
_CucsSwVlanGroupType_Type = CucsSwVlanGroupType
_CucsSwVlanGroupType_Object = MibTableColumn
cucsSwVlanGroupType = _CucsSwVlanGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1, 7),
    _CucsSwVlanGroupType_Type()
)
cucsSwVlanGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanGroupType.setStatus("current")
_CucsSwVlanGroupPvScore_Type = Gauge32
_CucsSwVlanGroupPvScore_Object = MibTableColumn
cucsSwVlanGroupPvScore = _CucsSwVlanGroupPvScore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 65, 1, 8),
    _CucsSwVlanGroupPvScore_Type()
)
cucsSwVlanGroupPvScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanGroupPvScore.setStatus("current")
_CucsSwVlanRefTable_Object = MibTable
cucsSwVlanRefTable = _CucsSwVlanRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66)
)
if mibBuilder.loadTexts:
    cucsSwVlanRefTable.setStatus("current")
_CucsSwVlanRefEntry_Object = MibTableRow
cucsSwVlanRefEntry = _CucsSwVlanRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66, 1)
)
cucsSwVlanRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwVlanRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwVlanRefEntry.setStatus("current")
_CucsSwVlanRefInstanceId_Type = CucsManagedObjectId
_CucsSwVlanRefInstanceId_Object = MibTableColumn
cucsSwVlanRefInstanceId = _CucsSwVlanRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66, 1, 1),
    _CucsSwVlanRefInstanceId_Type()
)
cucsSwVlanRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwVlanRefInstanceId.setStatus("current")
_CucsSwVlanRefDn_Type = CucsManagedObjectDn
_CucsSwVlanRefDn_Object = MibTableColumn
cucsSwVlanRefDn = _CucsSwVlanRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66, 1, 2),
    _CucsSwVlanRefDn_Type()
)
cucsSwVlanRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanRefDn.setStatus("current")
_CucsSwVlanRefRn_Type = SnmpAdminString
_CucsSwVlanRefRn_Object = MibTableColumn
cucsSwVlanRefRn = _CucsSwVlanRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66, 1, 3),
    _CucsSwVlanRefRn_Type()
)
cucsSwVlanRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanRefRn.setStatus("current")
_CucsSwVlanRefCompressionType_Type = CucsSwVlanCompType
_CucsSwVlanRefCompressionType_Object = MibTableColumn
cucsSwVlanRefCompressionType = _CucsSwVlanRefCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66, 1, 4),
    _CucsSwVlanRefCompressionType_Type()
)
cucsSwVlanRefCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanRefCompressionType.setStatus("current")
_CucsSwVlanRefConfigStatus_Type = CucsSwVlanConfigStatusType
_CucsSwVlanRefConfigStatus_Object = MibTableColumn
cucsSwVlanRefConfigStatus = _CucsSwVlanRefConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66, 1, 5),
    _CucsSwVlanRefConfigStatus_Type()
)
cucsSwVlanRefConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanRefConfigStatus.setStatus("current")
_CucsSwVlanRefId_Type = Gauge32
_CucsSwVlanRefId_Object = MibTableColumn
cucsSwVlanRefId = _CucsSwVlanRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66, 1, 6),
    _CucsSwVlanRefId_Type()
)
cucsSwVlanRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanRefId.setStatus("current")
_CucsSwVlanRefPeerDn_Type = SnmpAdminString
_CucsSwVlanRefPeerDn_Object = MibTableColumn
cucsSwVlanRefPeerDn = _CucsSwVlanRefPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 66, 1, 7),
    _CucsSwVlanRefPeerDn_Type()
)
cucsSwVlanRefPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVlanRefPeerDn.setStatus("current")
_CucsSwZoneInitiatorMemberTable_Object = MibTable
cucsSwZoneInitiatorMemberTable = _CucsSwZoneInitiatorMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67)
)
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberTable.setStatus("current")
_CucsSwZoneInitiatorMemberEntry_Object = MibTableRow
cucsSwZoneInitiatorMemberEntry = _CucsSwZoneInitiatorMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1)
)
cucsSwZoneInitiatorMemberEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwZoneInitiatorMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberEntry.setStatus("current")
_CucsSwZoneInitiatorMemberInstanceId_Type = CucsManagedObjectId
_CucsSwZoneInitiatorMemberInstanceId_Object = MibTableColumn
cucsSwZoneInitiatorMemberInstanceId = _CucsSwZoneInitiatorMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1, 1),
    _CucsSwZoneInitiatorMemberInstanceId_Type()
)
cucsSwZoneInitiatorMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberInstanceId.setStatus("current")
_CucsSwZoneInitiatorMemberDn_Type = CucsManagedObjectDn
_CucsSwZoneInitiatorMemberDn_Object = MibTableColumn
cucsSwZoneInitiatorMemberDn = _CucsSwZoneInitiatorMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1, 2),
    _CucsSwZoneInitiatorMemberDn_Type()
)
cucsSwZoneInitiatorMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberDn.setStatus("current")
_CucsSwZoneInitiatorMemberRn_Type = SnmpAdminString
_CucsSwZoneInitiatorMemberRn_Object = MibTableColumn
cucsSwZoneInitiatorMemberRn = _CucsSwZoneInitiatorMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1, 3),
    _CucsSwZoneInitiatorMemberRn_Type()
)
cucsSwZoneInitiatorMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberRn.setStatus("current")
_CucsSwZoneInitiatorMemberEpDn_Type = SnmpAdminString
_CucsSwZoneInitiatorMemberEpDn_Object = MibTableColumn
cucsSwZoneInitiatorMemberEpDn = _CucsSwZoneInitiatorMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1, 4),
    _CucsSwZoneInitiatorMemberEpDn_Type()
)
cucsSwZoneInitiatorMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberEpDn.setStatus("current")
_CucsSwZoneInitiatorMemberLc_Type = CucsSwFcZoneMemberLc
_CucsSwZoneInitiatorMemberLc_Object = MibTableColumn
cucsSwZoneInitiatorMemberLc = _CucsSwZoneInitiatorMemberLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1, 5),
    _CucsSwZoneInitiatorMemberLc_Type()
)
cucsSwZoneInitiatorMemberLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberLc.setStatus("current")
_CucsSwZoneInitiatorMemberName_Type = SnmpAdminString
_CucsSwZoneInitiatorMemberName_Object = MibTableColumn
cucsSwZoneInitiatorMemberName = _CucsSwZoneInitiatorMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1, 6),
    _CucsSwZoneInitiatorMemberName_Type()
)
cucsSwZoneInitiatorMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberName.setStatus("current")
_CucsSwZoneInitiatorMemberPeerDn_Type = SnmpAdminString
_CucsSwZoneInitiatorMemberPeerDn_Object = MibTableColumn
cucsSwZoneInitiatorMemberPeerDn = _CucsSwZoneInitiatorMemberPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1, 7),
    _CucsSwZoneInitiatorMemberPeerDn_Type()
)
cucsSwZoneInitiatorMemberPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberPeerDn.setStatus("current")
_CucsSwZoneInitiatorMemberWwpn_Type = Unsigned64
_CucsSwZoneInitiatorMemberWwpn_Object = MibTableColumn
cucsSwZoneInitiatorMemberWwpn = _CucsSwZoneInitiatorMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 67, 1, 8),
    _CucsSwZoneInitiatorMemberWwpn_Type()
)
cucsSwZoneInitiatorMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneInitiatorMemberWwpn.setStatus("current")
_CucsSwZoneTargetMemberTable_Object = MibTable
cucsSwZoneTargetMemberTable = _CucsSwZoneTargetMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68)
)
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberTable.setStatus("current")
_CucsSwZoneTargetMemberEntry_Object = MibTableRow
cucsSwZoneTargetMemberEntry = _CucsSwZoneTargetMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1)
)
cucsSwZoneTargetMemberEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwZoneTargetMemberInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberEntry.setStatus("current")
_CucsSwZoneTargetMemberInstanceId_Type = CucsManagedObjectId
_CucsSwZoneTargetMemberInstanceId_Object = MibTableColumn
cucsSwZoneTargetMemberInstanceId = _CucsSwZoneTargetMemberInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1, 1),
    _CucsSwZoneTargetMemberInstanceId_Type()
)
cucsSwZoneTargetMemberInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberInstanceId.setStatus("current")
_CucsSwZoneTargetMemberDn_Type = CucsManagedObjectDn
_CucsSwZoneTargetMemberDn_Object = MibTableColumn
cucsSwZoneTargetMemberDn = _CucsSwZoneTargetMemberDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1, 2),
    _CucsSwZoneTargetMemberDn_Type()
)
cucsSwZoneTargetMemberDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberDn.setStatus("current")
_CucsSwZoneTargetMemberRn_Type = SnmpAdminString
_CucsSwZoneTargetMemberRn_Object = MibTableColumn
cucsSwZoneTargetMemberRn = _CucsSwZoneTargetMemberRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1, 3),
    _CucsSwZoneTargetMemberRn_Type()
)
cucsSwZoneTargetMemberRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberRn.setStatus("current")
_CucsSwZoneTargetMemberEpDn_Type = SnmpAdminString
_CucsSwZoneTargetMemberEpDn_Object = MibTableColumn
cucsSwZoneTargetMemberEpDn = _CucsSwZoneTargetMemberEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1, 4),
    _CucsSwZoneTargetMemberEpDn_Type()
)
cucsSwZoneTargetMemberEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberEpDn.setStatus("current")
_CucsSwZoneTargetMemberLc_Type = CucsSwFcZoneMemberLc
_CucsSwZoneTargetMemberLc_Object = MibTableColumn
cucsSwZoneTargetMemberLc = _CucsSwZoneTargetMemberLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1, 5),
    _CucsSwZoneTargetMemberLc_Type()
)
cucsSwZoneTargetMemberLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberLc.setStatus("current")
_CucsSwZoneTargetMemberName_Type = SnmpAdminString
_CucsSwZoneTargetMemberName_Object = MibTableColumn
cucsSwZoneTargetMemberName = _CucsSwZoneTargetMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1, 6),
    _CucsSwZoneTargetMemberName_Type()
)
cucsSwZoneTargetMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberName.setStatus("current")
_CucsSwZoneTargetMemberPeerDn_Type = SnmpAdminString
_CucsSwZoneTargetMemberPeerDn_Object = MibTableColumn
cucsSwZoneTargetMemberPeerDn = _CucsSwZoneTargetMemberPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1, 7),
    _CucsSwZoneTargetMemberPeerDn_Type()
)
cucsSwZoneTargetMemberPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberPeerDn.setStatus("current")
_CucsSwZoneTargetMemberWwpn_Type = Unsigned64
_CucsSwZoneTargetMemberWwpn_Object = MibTableColumn
cucsSwZoneTargetMemberWwpn = _CucsSwZoneTargetMemberWwpn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 68, 1, 8),
    _CucsSwZoneTargetMemberWwpn_Type()
)
cucsSwZoneTargetMemberWwpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwZoneTargetMemberWwpn.setStatus("current")
_CucsSwCmclanTable_Object = MibTable
cucsSwCmclanTable = _CucsSwCmclanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69)
)
if mibBuilder.loadTexts:
    cucsSwCmclanTable.setStatus("current")
_CucsSwCmclanEntry_Object = MibTableRow
cucsSwCmclanEntry = _CucsSwCmclanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1)
)
cucsSwCmclanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwCmclanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwCmclanEntry.setStatus("current")
_CucsSwCmclanInstanceId_Type = CucsManagedObjectId
_CucsSwCmclanInstanceId_Object = MibTableColumn
cucsSwCmclanInstanceId = _CucsSwCmclanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 1),
    _CucsSwCmclanInstanceId_Type()
)
cucsSwCmclanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwCmclanInstanceId.setStatus("current")
_CucsSwCmclanDn_Type = CucsManagedObjectDn
_CucsSwCmclanDn_Object = MibTableColumn
cucsSwCmclanDn = _CucsSwCmclanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 2),
    _CucsSwCmclanDn_Type()
)
cucsSwCmclanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanDn.setStatus("current")
_CucsSwCmclanRn_Type = SnmpAdminString
_CucsSwCmclanRn_Object = MibTableColumn
cucsSwCmclanRn = _CucsSwCmclanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 3),
    _CucsSwCmclanRn_Type()
)
cucsSwCmclanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanRn.setStatus("current")
_CucsSwCmclanCimcIds_Type = CucsSwCimcId
_CucsSwCmclanCimcIds_Object = MibTableColumn
cucsSwCmclanCimcIds = _CucsSwCmclanCimcIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 4),
    _CucsSwCmclanCimcIds_Type()
)
cucsSwCmclanCimcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanCimcIds.setStatus("current")
_CucsSwCmclanEpDn_Type = SnmpAdminString
_CucsSwCmclanEpDn_Object = MibTableColumn
cucsSwCmclanEpDn = _CucsSwCmclanEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 5),
    _CucsSwCmclanEpDn_Type()
)
cucsSwCmclanEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanEpDn.setStatus("current")
_CucsSwCmclanId_Type = Gauge32
_CucsSwCmclanId_Object = MibTableColumn
cucsSwCmclanId = _CucsSwCmclanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 6),
    _CucsSwCmclanId_Type()
)
cucsSwCmclanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanId.setStatus("current")
_CucsSwCmclanIfRole_Type = CucsNetworkPortRole
_CucsSwCmclanIfRole_Object = MibTableColumn
cucsSwCmclanIfRole = _CucsSwCmclanIfRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 7),
    _CucsSwCmclanIfRole_Type()
)
cucsSwCmclanIfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanIfRole.setStatus("current")
_CucsSwCmclanIfType_Type = CucsNetworkVnetEpIfType
_CucsSwCmclanIfType_Object = MibTableColumn
cucsSwCmclanIfType = _CucsSwCmclanIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 8),
    _CucsSwCmclanIfType_Type()
)
cucsSwCmclanIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanIfType.setStatus("current")
_CucsSwCmclanLocale_Type = CucsNetworkLocale
_CucsSwCmclanLocale_Object = MibTableColumn
cucsSwCmclanLocale = _CucsSwCmclanLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 9),
    _CucsSwCmclanLocale_Type()
)
cucsSwCmclanLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanLocale.setStatus("current")
_CucsSwCmclanName_Type = SnmpAdminString
_CucsSwCmclanName_Object = MibTableColumn
cucsSwCmclanName = _CucsSwCmclanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 10),
    _CucsSwCmclanName_Type()
)
cucsSwCmclanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanName.setStatus("current")
_CucsSwCmclanPeerDn_Type = SnmpAdminString
_CucsSwCmclanPeerDn_Object = MibTableColumn
cucsSwCmclanPeerDn = _CucsSwCmclanPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 11),
    _CucsSwCmclanPeerDn_Type()
)
cucsSwCmclanPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanPeerDn.setStatus("current")
_CucsSwCmclanTransport_Type = CucsNetworkTransport
_CucsSwCmclanTransport_Object = MibTableColumn
cucsSwCmclanTransport = _CucsSwCmclanTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 12),
    _CucsSwCmclanTransport_Type()
)
cucsSwCmclanTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanTransport.setStatus("current")
_CucsSwCmclanType_Type = CucsNetworkConnectionType
_CucsSwCmclanType_Object = MibTableColumn
cucsSwCmclanType = _CucsSwCmclanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 69, 1, 13),
    _CucsSwCmclanType_Type()
)
cucsSwCmclanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwCmclanType.setStatus("current")
_CucsSwEthLanFlowMonTable_Object = MibTable
cucsSwEthLanFlowMonTable = _CucsSwEthLanFlowMonTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70)
)
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonTable.setStatus("current")
_CucsSwEthLanFlowMonEntry_Object = MibTableRow
cucsSwEthLanFlowMonEntry = _CucsSwEthLanFlowMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1)
)
cucsSwEthLanFlowMonEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanFlowMonInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonEntry.setStatus("current")
_CucsSwEthLanFlowMonInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanFlowMonInstanceId_Object = MibTableColumn
cucsSwEthLanFlowMonInstanceId = _CucsSwEthLanFlowMonInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 1),
    _CucsSwEthLanFlowMonInstanceId_Type()
)
cucsSwEthLanFlowMonInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonInstanceId.setStatus("current")
_CucsSwEthLanFlowMonDn_Type = CucsManagedObjectDn
_CucsSwEthLanFlowMonDn_Object = MibTableColumn
cucsSwEthLanFlowMonDn = _CucsSwEthLanFlowMonDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 2),
    _CucsSwEthLanFlowMonDn_Type()
)
cucsSwEthLanFlowMonDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonDn.setStatus("current")
_CucsSwEthLanFlowMonRn_Type = SnmpAdminString
_CucsSwEthLanFlowMonRn_Object = MibTableColumn
cucsSwEthLanFlowMonRn = _CucsSwEthLanFlowMonRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 3),
    _CucsSwEthLanFlowMonRn_Type()
)
cucsSwEthLanFlowMonRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonRn.setStatus("current")
_CucsSwEthLanFlowMonFsmDescr_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmDescr_Object = MibTableColumn
cucsSwEthLanFlowMonFsmDescr = _CucsSwEthLanFlowMonFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 4),
    _CucsSwEthLanFlowMonFsmDescr_Type()
)
cucsSwEthLanFlowMonFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmDescr.setStatus("current")
_CucsSwEthLanFlowMonFsmPrev_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmPrev_Object = MibTableColumn
cucsSwEthLanFlowMonFsmPrev = _CucsSwEthLanFlowMonFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 5),
    _CucsSwEthLanFlowMonFsmPrev_Type()
)
cucsSwEthLanFlowMonFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmPrev.setStatus("current")
_CucsSwEthLanFlowMonFsmProgr_Type = Gauge32
_CucsSwEthLanFlowMonFsmProgr_Object = MibTableColumn
cucsSwEthLanFlowMonFsmProgr = _CucsSwEthLanFlowMonFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 6),
    _CucsSwEthLanFlowMonFsmProgr_Type()
)
cucsSwEthLanFlowMonFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmProgr.setStatus("current")
_CucsSwEthLanFlowMonFsmRmtInvErrCode_Type = Gauge32
_CucsSwEthLanFlowMonFsmRmtInvErrCode_Object = MibTableColumn
cucsSwEthLanFlowMonFsmRmtInvErrCode = _CucsSwEthLanFlowMonFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 7),
    _CucsSwEthLanFlowMonFsmRmtInvErrCode_Type()
)
cucsSwEthLanFlowMonFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmRmtInvErrCode.setStatus("current")
_CucsSwEthLanFlowMonFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwEthLanFlowMonFsmRmtInvErrDescr = _CucsSwEthLanFlowMonFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 8),
    _CucsSwEthLanFlowMonFsmRmtInvErrDescr_Type()
)
cucsSwEthLanFlowMonFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmRmtInvErrDescr.setStatus("current")
_CucsSwEthLanFlowMonFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwEthLanFlowMonFsmRmtInvRslt_Object = MibTableColumn
cucsSwEthLanFlowMonFsmRmtInvRslt = _CucsSwEthLanFlowMonFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 9),
    _CucsSwEthLanFlowMonFsmRmtInvRslt_Type()
)
cucsSwEthLanFlowMonFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmRmtInvRslt.setStatus("current")
_CucsSwEthLanFlowMonFsmStageDescr_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmStageDescr_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageDescr = _CucsSwEthLanFlowMonFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 10),
    _CucsSwEthLanFlowMonFsmStageDescr_Type()
)
cucsSwEthLanFlowMonFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageDescr.setStatus("current")
_CucsSwEthLanFlowMonFsmStamp_Type = DateAndTime
_CucsSwEthLanFlowMonFsmStamp_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStamp = _CucsSwEthLanFlowMonFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 11),
    _CucsSwEthLanFlowMonFsmStamp_Type()
)
cucsSwEthLanFlowMonFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStamp.setStatus("current")
_CucsSwEthLanFlowMonFsmStatus_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmStatus_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStatus = _CucsSwEthLanFlowMonFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 12),
    _CucsSwEthLanFlowMonFsmStatus_Type()
)
cucsSwEthLanFlowMonFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStatus.setStatus("current")
_CucsSwEthLanFlowMonFsmTry_Type = Gauge32
_CucsSwEthLanFlowMonFsmTry_Object = MibTableColumn
cucsSwEthLanFlowMonFsmTry = _CucsSwEthLanFlowMonFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 13),
    _CucsSwEthLanFlowMonFsmTry_Type()
)
cucsSwEthLanFlowMonFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTry.setStatus("current")
_CucsSwEthLanFlowMonLocale_Type = CucsSwMonDomainLocale
_CucsSwEthLanFlowMonLocale_Object = MibTableColumn
cucsSwEthLanFlowMonLocale = _CucsSwEthLanFlowMonLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 14),
    _CucsSwEthLanFlowMonLocale_Type()
)
cucsSwEthLanFlowMonLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonLocale.setStatus("current")
_CucsSwEthLanFlowMonName_Type = SnmpAdminString
_CucsSwEthLanFlowMonName_Object = MibTableColumn
cucsSwEthLanFlowMonName = _CucsSwEthLanFlowMonName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 15),
    _CucsSwEthLanFlowMonName_Type()
)
cucsSwEthLanFlowMonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonName.setStatus("current")
_CucsSwEthLanFlowMonNetflowActiveTimeout_Type = Gauge32
_CucsSwEthLanFlowMonNetflowActiveTimeout_Object = MibTableColumn
cucsSwEthLanFlowMonNetflowActiveTimeout = _CucsSwEthLanFlowMonNetflowActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 16),
    _CucsSwEthLanFlowMonNetflowActiveTimeout_Type()
)
cucsSwEthLanFlowMonNetflowActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonNetflowActiveTimeout.setStatus("current")
_CucsSwEthLanFlowMonNetflowInactiveTimeout_Type = Gauge32
_CucsSwEthLanFlowMonNetflowInactiveTimeout_Object = MibTableColumn
cucsSwEthLanFlowMonNetflowInactiveTimeout = _CucsSwEthLanFlowMonNetflowInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 17),
    _CucsSwEthLanFlowMonNetflowInactiveTimeout_Type()
)
cucsSwEthLanFlowMonNetflowInactiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonNetflowInactiveTimeout.setStatus("current")
_CucsSwEthLanFlowMonSwitchId_Type = CucsNetworkSwitchId
_CucsSwEthLanFlowMonSwitchId_Object = MibTableColumn
cucsSwEthLanFlowMonSwitchId = _CucsSwEthLanFlowMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 18),
    _CucsSwEthLanFlowMonSwitchId_Type()
)
cucsSwEthLanFlowMonSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonSwitchId.setStatus("current")
_CucsSwEthLanFlowMonTransport_Type = CucsSwEthLanFlowMonTransport
_CucsSwEthLanFlowMonTransport_Object = MibTableColumn
cucsSwEthLanFlowMonTransport = _CucsSwEthLanFlowMonTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 19),
    _CucsSwEthLanFlowMonTransport_Type()
)
cucsSwEthLanFlowMonTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonTransport.setStatus("current")
_CucsSwEthLanFlowMonType_Type = CucsSwLanMonType
_CucsSwEthLanFlowMonType_Object = MibTableColumn
cucsSwEthLanFlowMonType = _CucsSwEthLanFlowMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 70, 1, 20),
    _CucsSwEthLanFlowMonType_Type()
)
cucsSwEthLanFlowMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonType.setStatus("current")
_CucsSwEthLanFlowMonFsmTable_Object = MibTable
cucsSwEthLanFlowMonFsmTable = _CucsSwEthLanFlowMonFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71)
)
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTable.setStatus("current")
_CucsSwEthLanFlowMonFsmEntry_Object = MibTableRow
cucsSwEthLanFlowMonFsmEntry = _CucsSwEthLanFlowMonFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1)
)
cucsSwEthLanFlowMonFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanFlowMonFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmEntry.setStatus("current")
_CucsSwEthLanFlowMonFsmInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanFlowMonFsmInstanceId_Object = MibTableColumn
cucsSwEthLanFlowMonFsmInstanceId = _CucsSwEthLanFlowMonFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 1),
    _CucsSwEthLanFlowMonFsmInstanceId_Type()
)
cucsSwEthLanFlowMonFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmInstanceId.setStatus("current")
_CucsSwEthLanFlowMonFsmDn_Type = CucsManagedObjectDn
_CucsSwEthLanFlowMonFsmDn_Object = MibTableColumn
cucsSwEthLanFlowMonFsmDn = _CucsSwEthLanFlowMonFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 2),
    _CucsSwEthLanFlowMonFsmDn_Type()
)
cucsSwEthLanFlowMonFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmDn.setStatus("current")
_CucsSwEthLanFlowMonFsmRn_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmRn_Object = MibTableColumn
cucsSwEthLanFlowMonFsmRn = _CucsSwEthLanFlowMonFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 3),
    _CucsSwEthLanFlowMonFsmRn_Type()
)
cucsSwEthLanFlowMonFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmRn.setStatus("current")
_CucsSwEthLanFlowMonFsmCompletionTime_Type = DateAndTime
_CucsSwEthLanFlowMonFsmCompletionTime_Object = MibTableColumn
cucsSwEthLanFlowMonFsmCompletionTime = _CucsSwEthLanFlowMonFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 4),
    _CucsSwEthLanFlowMonFsmCompletionTime_Type()
)
cucsSwEthLanFlowMonFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmCompletionTime.setStatus("current")
_CucsSwEthLanFlowMonFsmCurrentFsm_Type = CucsSwEthLanFlowMonFsmCurrentFsm
_CucsSwEthLanFlowMonFsmCurrentFsm_Object = MibTableColumn
cucsSwEthLanFlowMonFsmCurrentFsm = _CucsSwEthLanFlowMonFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 5),
    _CucsSwEthLanFlowMonFsmCurrentFsm_Type()
)
cucsSwEthLanFlowMonFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmCurrentFsm.setStatus("current")
_CucsSwEthLanFlowMonFsmDescrData_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmDescrData_Object = MibTableColumn
cucsSwEthLanFlowMonFsmDescrData = _CucsSwEthLanFlowMonFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 6),
    _CucsSwEthLanFlowMonFsmDescrData_Type()
)
cucsSwEthLanFlowMonFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmDescrData.setStatus("current")
_CucsSwEthLanFlowMonFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwEthLanFlowMonFsmFsmStatus_Object = MibTableColumn
cucsSwEthLanFlowMonFsmFsmStatus = _CucsSwEthLanFlowMonFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 7),
    _CucsSwEthLanFlowMonFsmFsmStatus_Type()
)
cucsSwEthLanFlowMonFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmFsmStatus.setStatus("current")
_CucsSwEthLanFlowMonFsmProgress_Type = Gauge32
_CucsSwEthLanFlowMonFsmProgress_Object = MibTableColumn
cucsSwEthLanFlowMonFsmProgress = _CucsSwEthLanFlowMonFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 8),
    _CucsSwEthLanFlowMonFsmProgress_Type()
)
cucsSwEthLanFlowMonFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmProgress.setStatus("current")
_CucsSwEthLanFlowMonFsmRmtErrCode_Type = Gauge32
_CucsSwEthLanFlowMonFsmRmtErrCode_Object = MibTableColumn
cucsSwEthLanFlowMonFsmRmtErrCode = _CucsSwEthLanFlowMonFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 9),
    _CucsSwEthLanFlowMonFsmRmtErrCode_Type()
)
cucsSwEthLanFlowMonFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmRmtErrCode.setStatus("current")
_CucsSwEthLanFlowMonFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmRmtErrDescr_Object = MibTableColumn
cucsSwEthLanFlowMonFsmRmtErrDescr = _CucsSwEthLanFlowMonFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 10),
    _CucsSwEthLanFlowMonFsmRmtErrDescr_Type()
)
cucsSwEthLanFlowMonFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmRmtErrDescr.setStatus("current")
_CucsSwEthLanFlowMonFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwEthLanFlowMonFsmRmtRslt_Object = MibTableColumn
cucsSwEthLanFlowMonFsmRmtRslt = _CucsSwEthLanFlowMonFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 71, 1, 11),
    _CucsSwEthLanFlowMonFsmRmtRslt_Type()
)
cucsSwEthLanFlowMonFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmRmtRslt.setStatus("current")
_CucsSwEthLanFlowMonFsmStageTable_Object = MibTable
cucsSwEthLanFlowMonFsmStageTable = _CucsSwEthLanFlowMonFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72)
)
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageTable.setStatus("current")
_CucsSwEthLanFlowMonFsmStageEntry_Object = MibTableRow
cucsSwEthLanFlowMonFsmStageEntry = _CucsSwEthLanFlowMonFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1)
)
cucsSwEthLanFlowMonFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanFlowMonFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageEntry.setStatus("current")
_CucsSwEthLanFlowMonFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanFlowMonFsmStageInstanceId_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageInstanceId = _CucsSwEthLanFlowMonFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 1),
    _CucsSwEthLanFlowMonFsmStageInstanceId_Type()
)
cucsSwEthLanFlowMonFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageInstanceId.setStatus("current")
_CucsSwEthLanFlowMonFsmStageDn_Type = CucsManagedObjectDn
_CucsSwEthLanFlowMonFsmStageDn_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageDn = _CucsSwEthLanFlowMonFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 2),
    _CucsSwEthLanFlowMonFsmStageDn_Type()
)
cucsSwEthLanFlowMonFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageDn.setStatus("current")
_CucsSwEthLanFlowMonFsmStageRn_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmStageRn_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageRn = _CucsSwEthLanFlowMonFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 3),
    _CucsSwEthLanFlowMonFsmStageRn_Type()
)
cucsSwEthLanFlowMonFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageRn.setStatus("current")
_CucsSwEthLanFlowMonFsmStageDescrData_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmStageDescrData_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageDescrData = _CucsSwEthLanFlowMonFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 4),
    _CucsSwEthLanFlowMonFsmStageDescrData_Type()
)
cucsSwEthLanFlowMonFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageDescrData.setStatus("current")
_CucsSwEthLanFlowMonFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwEthLanFlowMonFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageLastUpdateTime = _CucsSwEthLanFlowMonFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 5),
    _CucsSwEthLanFlowMonFsmStageLastUpdateTime_Type()
)
cucsSwEthLanFlowMonFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageLastUpdateTime.setStatus("current")
_CucsSwEthLanFlowMonFsmStageName_Type = CucsSwEthLanFlowMonFsmStageName
_CucsSwEthLanFlowMonFsmStageName_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageName = _CucsSwEthLanFlowMonFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 6),
    _CucsSwEthLanFlowMonFsmStageName_Type()
)
cucsSwEthLanFlowMonFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageName.setStatus("current")
_CucsSwEthLanFlowMonFsmStageOrder_Type = Gauge32
_CucsSwEthLanFlowMonFsmStageOrder_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageOrder = _CucsSwEthLanFlowMonFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 7),
    _CucsSwEthLanFlowMonFsmStageOrder_Type()
)
cucsSwEthLanFlowMonFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageOrder.setStatus("current")
_CucsSwEthLanFlowMonFsmStageRetry_Type = Gauge32
_CucsSwEthLanFlowMonFsmStageRetry_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageRetry = _CucsSwEthLanFlowMonFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 8),
    _CucsSwEthLanFlowMonFsmStageRetry_Type()
)
cucsSwEthLanFlowMonFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageRetry.setStatus("current")
_CucsSwEthLanFlowMonFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwEthLanFlowMonFsmStageStageStatus_Object = MibTableColumn
cucsSwEthLanFlowMonFsmStageStageStatus = _CucsSwEthLanFlowMonFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 72, 1, 9),
    _CucsSwEthLanFlowMonFsmStageStageStatus_Type()
)
cucsSwEthLanFlowMonFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmStageStageStatus.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskTable_Object = MibTable
cucsSwEthLanFlowMonFsmTaskTable = _CucsSwEthLanFlowMonFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73)
)
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskTable.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskEntry_Object = MibTableRow
cucsSwEthLanFlowMonFsmTaskEntry = _CucsSwEthLanFlowMonFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73, 1)
)
cucsSwEthLanFlowMonFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwEthLanFlowMonFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskEntry.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwEthLanFlowMonFsmTaskInstanceId_Object = MibTableColumn
cucsSwEthLanFlowMonFsmTaskInstanceId = _CucsSwEthLanFlowMonFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73, 1, 1),
    _CucsSwEthLanFlowMonFsmTaskInstanceId_Type()
)
cucsSwEthLanFlowMonFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskInstanceId.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwEthLanFlowMonFsmTaskDn_Object = MibTableColumn
cucsSwEthLanFlowMonFsmTaskDn = _CucsSwEthLanFlowMonFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73, 1, 2),
    _CucsSwEthLanFlowMonFsmTaskDn_Type()
)
cucsSwEthLanFlowMonFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskDn.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskRn_Type = SnmpAdminString
_CucsSwEthLanFlowMonFsmTaskRn_Object = MibTableColumn
cucsSwEthLanFlowMonFsmTaskRn = _CucsSwEthLanFlowMonFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73, 1, 3),
    _CucsSwEthLanFlowMonFsmTaskRn_Type()
)
cucsSwEthLanFlowMonFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskRn.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwEthLanFlowMonFsmTaskCompletion_Object = MibTableColumn
cucsSwEthLanFlowMonFsmTaskCompletion = _CucsSwEthLanFlowMonFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73, 1, 4),
    _CucsSwEthLanFlowMonFsmTaskCompletion_Type()
)
cucsSwEthLanFlowMonFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskCompletion.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskFlags_Type = CucsFsmFlags
_CucsSwEthLanFlowMonFsmTaskFlags_Object = MibTableColumn
cucsSwEthLanFlowMonFsmTaskFlags = _CucsSwEthLanFlowMonFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73, 1, 5),
    _CucsSwEthLanFlowMonFsmTaskFlags_Type()
)
cucsSwEthLanFlowMonFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskFlags.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskItem_Type = CucsSwEthLanFlowMonFsmTaskItem
_CucsSwEthLanFlowMonFsmTaskItem_Object = MibTableColumn
cucsSwEthLanFlowMonFsmTaskItem = _CucsSwEthLanFlowMonFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73, 1, 6),
    _CucsSwEthLanFlowMonFsmTaskItem_Type()
)
cucsSwEthLanFlowMonFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskItem.setStatus("current")
_CucsSwEthLanFlowMonFsmTaskSeqId_Type = Gauge32
_CucsSwEthLanFlowMonFsmTaskSeqId_Object = MibTableColumn
cucsSwEthLanFlowMonFsmTaskSeqId = _CucsSwEthLanFlowMonFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 73, 1, 7),
    _CucsSwEthLanFlowMonFsmTaskSeqId_Type()
)
cucsSwEthLanFlowMonFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwEthLanFlowMonFsmTaskSeqId.setStatus("current")
_CucsSwIpRouteTable_Object = MibTable
cucsSwIpRouteTable = _CucsSwIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74)
)
if mibBuilder.loadTexts:
    cucsSwIpRouteTable.setStatus("current")
_CucsSwIpRouteEntry_Object = MibTableRow
cucsSwIpRouteEntry = _CucsSwIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1)
)
cucsSwIpRouteEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwIpRouteInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwIpRouteEntry.setStatus("current")
_CucsSwIpRouteInstanceId_Type = CucsManagedObjectId
_CucsSwIpRouteInstanceId_Object = MibTableColumn
cucsSwIpRouteInstanceId = _CucsSwIpRouteInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 1),
    _CucsSwIpRouteInstanceId_Type()
)
cucsSwIpRouteInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwIpRouteInstanceId.setStatus("current")
_CucsSwIpRouteDn_Type = CucsManagedObjectDn
_CucsSwIpRouteDn_Object = MibTableColumn
cucsSwIpRouteDn = _CucsSwIpRouteDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 2),
    _CucsSwIpRouteDn_Type()
)
cucsSwIpRouteDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRouteDn.setStatus("current")
_CucsSwIpRouteRn_Type = SnmpAdminString
_CucsSwIpRouteRn_Object = MibTableColumn
cucsSwIpRouteRn = _CucsSwIpRouteRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 3),
    _CucsSwIpRouteRn_Type()
)
cucsSwIpRouteRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRouteRn.setStatus("current")
_CucsSwIpRouteDestinationIp_Type = InetAddressIPv4
_CucsSwIpRouteDestinationIp_Object = MibTableColumn
cucsSwIpRouteDestinationIp = _CucsSwIpRouteDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 4),
    _CucsSwIpRouteDestinationIp_Type()
)
cucsSwIpRouteDestinationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRouteDestinationIp.setStatus("current")
_CucsSwIpRouteDestinationNetmask_Type = InetAddressIPv4
_CucsSwIpRouteDestinationNetmask_Object = MibTableColumn
cucsSwIpRouteDestinationNetmask = _CucsSwIpRouteDestinationNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 5),
    _CucsSwIpRouteDestinationNetmask_Type()
)
cucsSwIpRouteDestinationNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRouteDestinationNetmask.setStatus("current")
_CucsSwIpRouteName_Type = SnmpAdminString
_CucsSwIpRouteName_Object = MibTableColumn
cucsSwIpRouteName = _CucsSwIpRouteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 6),
    _CucsSwIpRouteName_Type()
)
cucsSwIpRouteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRouteName.setStatus("current")
_CucsSwIpRoutePeerDn_Type = SnmpAdminString
_CucsSwIpRoutePeerDn_Object = MibTableColumn
cucsSwIpRoutePeerDn = _CucsSwIpRoutePeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 7),
    _CucsSwIpRoutePeerDn_Type()
)
cucsSwIpRoutePeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRoutePeerDn.setStatus("current")
_CucsSwIpRoutePrefix_Type = Gauge32
_CucsSwIpRoutePrefix_Object = MibTableColumn
cucsSwIpRoutePrefix = _CucsSwIpRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 8),
    _CucsSwIpRoutePrefix_Type()
)
cucsSwIpRoutePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRoutePrefix.setStatus("current")
_CucsSwIpRouteRouteIP_Type = InetAddressIPv4
_CucsSwIpRouteRouteIP_Object = MibTableColumn
cucsSwIpRouteRouteIP = _CucsSwIpRouteRouteIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 9),
    _CucsSwIpRouteRouteIP_Type()
)
cucsSwIpRouteRouteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRouteRouteIP.setStatus("current")
_CucsSwIpRouteSwitchId_Type = CucsNetworkSwitchId
_CucsSwIpRouteSwitchId_Object = MibTableColumn
cucsSwIpRouteSwitchId = _CucsSwIpRouteSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 74, 1, 10),
    _CucsSwIpRouteSwitchId_Type()
)
cucsSwIpRouteSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwIpRouteSwitchId.setStatus("current")
_CucsSwNFExporterRefTable_Object = MibTable
cucsSwNFExporterRefTable = _CucsSwNFExporterRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 75)
)
if mibBuilder.loadTexts:
    cucsSwNFExporterRefTable.setStatus("current")
_CucsSwNFExporterRefEntry_Object = MibTableRow
cucsSwNFExporterRefEntry = _CucsSwNFExporterRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 75, 1)
)
cucsSwNFExporterRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwNFExporterRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwNFExporterRefEntry.setStatus("current")
_CucsSwNFExporterRefInstanceId_Type = CucsManagedObjectId
_CucsSwNFExporterRefInstanceId_Object = MibTableColumn
cucsSwNFExporterRefInstanceId = _CucsSwNFExporterRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 75, 1, 1),
    _CucsSwNFExporterRefInstanceId_Type()
)
cucsSwNFExporterRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwNFExporterRefInstanceId.setStatus("current")
_CucsSwNFExporterRefDn_Type = CucsManagedObjectDn
_CucsSwNFExporterRefDn_Object = MibTableColumn
cucsSwNFExporterRefDn = _CucsSwNFExporterRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 75, 1, 2),
    _CucsSwNFExporterRefDn_Type()
)
cucsSwNFExporterRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNFExporterRefDn.setStatus("current")
_CucsSwNFExporterRefRn_Type = SnmpAdminString
_CucsSwNFExporterRefRn_Object = MibTableColumn
cucsSwNFExporterRefRn = _CucsSwNFExporterRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 75, 1, 3),
    _CucsSwNFExporterRefRn_Type()
)
cucsSwNFExporterRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNFExporterRefRn.setStatus("current")
_CucsSwNFExporterRefName_Type = SnmpAdminString
_CucsSwNFExporterRefName_Object = MibTableColumn
cucsSwNFExporterRefName = _CucsSwNFExporterRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 75, 1, 4),
    _CucsSwNFExporterRefName_Type()
)
cucsSwNFExporterRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNFExporterRefName.setStatus("current")
_CucsSwNFExporterRefPeerDn_Type = SnmpAdminString
_CucsSwNFExporterRefPeerDn_Object = MibTableColumn
cucsSwNFExporterRefPeerDn = _CucsSwNFExporterRefPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 75, 1, 5),
    _CucsSwNFExporterRefPeerDn_Type()
)
cucsSwNFExporterRefPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNFExporterRefPeerDn.setStatus("current")
_CucsSwNetflowExporterTable_Object = MibTable
cucsSwNetflowExporterTable = _CucsSwNetflowExporterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76)
)
if mibBuilder.loadTexts:
    cucsSwNetflowExporterTable.setStatus("current")
_CucsSwNetflowExporterEntry_Object = MibTableRow
cucsSwNetflowExporterEntry = _CucsSwNetflowExporterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1)
)
cucsSwNetflowExporterEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwNetflowExporterInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwNetflowExporterEntry.setStatus("current")
_CucsSwNetflowExporterInstanceId_Type = CucsManagedObjectId
_CucsSwNetflowExporterInstanceId_Object = MibTableColumn
cucsSwNetflowExporterInstanceId = _CucsSwNetflowExporterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 1),
    _CucsSwNetflowExporterInstanceId_Type()
)
cucsSwNetflowExporterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterInstanceId.setStatus("current")
_CucsSwNetflowExporterDn_Type = CucsManagedObjectDn
_CucsSwNetflowExporterDn_Object = MibTableColumn
cucsSwNetflowExporterDn = _CucsSwNetflowExporterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 2),
    _CucsSwNetflowExporterDn_Type()
)
cucsSwNetflowExporterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterDn.setStatus("current")
_CucsSwNetflowExporterRn_Type = SnmpAdminString
_CucsSwNetflowExporterRn_Object = MibTableColumn
cucsSwNetflowExporterRn = _CucsSwNetflowExporterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 3),
    _CucsSwNetflowExporterRn_Type()
)
cucsSwNetflowExporterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterRn.setStatus("current")
_CucsSwNetflowExporterDestinationIpAddress_Type = InetAddressIPv4
_CucsSwNetflowExporterDestinationIpAddress_Object = MibTableColumn
cucsSwNetflowExporterDestinationIpAddress = _CucsSwNetflowExporterDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 4),
    _CucsSwNetflowExporterDestinationIpAddress_Type()
)
cucsSwNetflowExporterDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterDestinationIpAddress.setStatus("current")
_CucsSwNetflowExporterDestinationPort_Type = Gauge32
_CucsSwNetflowExporterDestinationPort_Object = MibTableColumn
cucsSwNetflowExporterDestinationPort = _CucsSwNetflowExporterDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 5),
    _CucsSwNetflowExporterDestinationPort_Type()
)
cucsSwNetflowExporterDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterDestinationPort.setStatus("current")
_CucsSwNetflowExporterDscp_Type = Gauge32
_CucsSwNetflowExporterDscp_Object = MibTableColumn
cucsSwNetflowExporterDscp = _CucsSwNetflowExporterDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 6),
    _CucsSwNetflowExporterDscp_Type()
)
cucsSwNetflowExporterDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterDscp.setStatus("current")
_CucsSwNetflowExporterExportInternal_Type = Gauge32
_CucsSwNetflowExporterExportInternal_Object = MibTableColumn
cucsSwNetflowExporterExportInternal = _CucsSwNetflowExporterExportInternal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 7),
    _CucsSwNetflowExporterExportInternal_Type()
)
cucsSwNetflowExporterExportInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterExportInternal.setStatus("current")
_CucsSwNetflowExporterExporterStatsTimeout_Type = Gauge32
_CucsSwNetflowExporterExporterStatsTimeout_Object = MibTableColumn
cucsSwNetflowExporterExporterStatsTimeout = _CucsSwNetflowExporterExporterStatsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 8),
    _CucsSwNetflowExporterExporterStatsTimeout_Type()
)
cucsSwNetflowExporterExporterStatsTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterExporterStatsTimeout.setStatus("current")
_CucsSwNetflowExporterInterfaceTableTimeout_Type = Gauge32
_CucsSwNetflowExporterInterfaceTableTimeout_Object = MibTableColumn
cucsSwNetflowExporterInterfaceTableTimeout = _CucsSwNetflowExporterInterfaceTableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 9),
    _CucsSwNetflowExporterInterfaceTableTimeout_Type()
)
cucsSwNetflowExporterInterfaceTableTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterInterfaceTableTimeout.setStatus("current")
_CucsSwNetflowExporterIsValidConfig_Type = CucsSwNFConfigStatus
_CucsSwNetflowExporterIsValidConfig_Object = MibTableColumn
cucsSwNetflowExporterIsValidConfig = _CucsSwNetflowExporterIsValidConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 10),
    _CucsSwNetflowExporterIsValidConfig_Type()
)
cucsSwNetflowExporterIsValidConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterIsValidConfig.setStatus("current")
_CucsSwNetflowExporterLifeCycle_Type = CucsSwMonLifeCycle
_CucsSwNetflowExporterLifeCycle_Object = MibTableColumn
cucsSwNetflowExporterLifeCycle = _CucsSwNetflowExporterLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 11),
    _CucsSwNetflowExporterLifeCycle_Type()
)
cucsSwNetflowExporterLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterLifeCycle.setStatus("current")
_CucsSwNetflowExporterName_Type = SnmpAdminString
_CucsSwNetflowExporterName_Object = MibTableColumn
cucsSwNetflowExporterName = _CucsSwNetflowExporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 12),
    _CucsSwNetflowExporterName_Type()
)
cucsSwNetflowExporterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterName.setStatus("current")
_CucsSwNetflowExporterPeerDn_Type = SnmpAdminString
_CucsSwNetflowExporterPeerDn_Object = MibTableColumn
cucsSwNetflowExporterPeerDn = _CucsSwNetflowExporterPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 13),
    _CucsSwNetflowExporterPeerDn_Type()
)
cucsSwNetflowExporterPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterPeerDn.setStatus("current")
_CucsSwNetflowExporterProtocol_Type = CucsSwNetflowExporterProtocol
_CucsSwNetflowExporterProtocol_Object = MibTableColumn
cucsSwNetflowExporterProtocol = _CucsSwNetflowExporterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 14),
    _CucsSwNetflowExporterProtocol_Type()
)
cucsSwNetflowExporterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterProtocol.setStatus("current")
_CucsSwNetflowExporterSourceVlan_Type = Gauge32
_CucsSwNetflowExporterSourceVlan_Object = MibTableColumn
cucsSwNetflowExporterSourceVlan = _CucsSwNetflowExporterSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 15),
    _CucsSwNetflowExporterSourceVlan_Type()
)
cucsSwNetflowExporterSourceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterSourceVlan.setStatus("current")
_CucsSwNetflowExporterSwitchId_Type = CucsNetworkSwitchId
_CucsSwNetflowExporterSwitchId_Object = MibTableColumn
cucsSwNetflowExporterSwitchId = _CucsSwNetflowExporterSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 16),
    _CucsSwNetflowExporterSwitchId_Type()
)
cucsSwNetflowExporterSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterSwitchId.setStatus("current")
_CucsSwNetflowExporterTemplateDataTimeout_Type = Gauge32
_CucsSwNetflowExporterTemplateDataTimeout_Object = MibTableColumn
cucsSwNetflowExporterTemplateDataTimeout = _CucsSwNetflowExporterTemplateDataTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 17),
    _CucsSwNetflowExporterTemplateDataTimeout_Type()
)
cucsSwNetflowExporterTemplateDataTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterTemplateDataTimeout.setStatus("current")
_CucsSwNetflowExporterTransport_Type = CucsSwEthLanFlowMonExporterTransport
_CucsSwNetflowExporterTransport_Object = MibTableColumn
cucsSwNetflowExporterTransport = _CucsSwNetflowExporterTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 18),
    _CucsSwNetflowExporterTransport_Type()
)
cucsSwNetflowExporterTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterTransport.setStatus("current")
_CucsSwNetflowExporterTransportProtocol_Type = CucsFabricNFTransport
_CucsSwNetflowExporterTransportProtocol_Object = MibTableColumn
cucsSwNetflowExporterTransportProtocol = _CucsSwNetflowExporterTransportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 19),
    _CucsSwNetflowExporterTransportProtocol_Type()
)
cucsSwNetflowExporterTransportProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterTransportProtocol.setStatus("current")
_CucsSwNetflowExporterType_Type = CucsSwEthLanFlowMonExporterType
_CucsSwNetflowExporterType_Object = MibTableColumn
cucsSwNetflowExporterType = _CucsSwNetflowExporterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 20),
    _CucsSwNetflowExporterType_Type()
)
cucsSwNetflowExporterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterType.setStatus("current")
_CucsSwNetflowExporterVersion_Type = CucsFabricNFExporterVersion
_CucsSwNetflowExporterVersion_Object = MibTableColumn
cucsSwNetflowExporterVersion = _CucsSwNetflowExporterVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 76, 1, 21),
    _CucsSwNetflowExporterVersion_Type()
)
cucsSwNetflowExporterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowExporterVersion.setStatus("current")
_CucsSwNetflowMonSessionTable_Object = MibTable
cucsSwNetflowMonSessionTable = _CucsSwNetflowMonSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77)
)
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionTable.setStatus("current")
_CucsSwNetflowMonSessionEntry_Object = MibTableRow
cucsSwNetflowMonSessionEntry = _CucsSwNetflowMonSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1)
)
cucsSwNetflowMonSessionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwNetflowMonSessionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionEntry.setStatus("current")
_CucsSwNetflowMonSessionInstanceId_Type = CucsManagedObjectId
_CucsSwNetflowMonSessionInstanceId_Object = MibTableColumn
cucsSwNetflowMonSessionInstanceId = _CucsSwNetflowMonSessionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 1),
    _CucsSwNetflowMonSessionInstanceId_Type()
)
cucsSwNetflowMonSessionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionInstanceId.setStatus("current")
_CucsSwNetflowMonSessionDn_Type = CucsManagedObjectDn
_CucsSwNetflowMonSessionDn_Object = MibTableColumn
cucsSwNetflowMonSessionDn = _CucsSwNetflowMonSessionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 2),
    _CucsSwNetflowMonSessionDn_Type()
)
cucsSwNetflowMonSessionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionDn.setStatus("current")
_CucsSwNetflowMonSessionRn_Type = SnmpAdminString
_CucsSwNetflowMonSessionRn_Object = MibTableColumn
cucsSwNetflowMonSessionRn = _CucsSwNetflowMonSessionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 3),
    _CucsSwNetflowMonSessionRn_Type()
)
cucsSwNetflowMonSessionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionRn.setStatus("current")
_CucsSwNetflowMonSessionAdminState_Type = CucsSwMonAdminState
_CucsSwNetflowMonSessionAdminState_Object = MibTableColumn
cucsSwNetflowMonSessionAdminState = _CucsSwNetflowMonSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 4),
    _CucsSwNetflowMonSessionAdminState_Type()
)
cucsSwNetflowMonSessionAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionAdminState.setStatus("current")
_CucsSwNetflowMonSessionHasLastDest_Type = TruthValue
_CucsSwNetflowMonSessionHasLastDest_Object = MibTableColumn
cucsSwNetflowMonSessionHasLastDest = _CucsSwNetflowMonSessionHasLastDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 5),
    _CucsSwNetflowMonSessionHasLastDest_Type()
)
cucsSwNetflowMonSessionHasLastDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionHasLastDest.setStatus("current")
_CucsSwNetflowMonSessionLifeCycle_Type = CucsSwMonLifeCycle
_CucsSwNetflowMonSessionLifeCycle_Object = MibTableColumn
cucsSwNetflowMonSessionLifeCycle = _CucsSwNetflowMonSessionLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 6),
    _CucsSwNetflowMonSessionLifeCycle_Type()
)
cucsSwNetflowMonSessionLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionLifeCycle.setStatus("current")
_CucsSwNetflowMonSessionName_Type = SnmpAdminString
_CucsSwNetflowMonSessionName_Object = MibTableColumn
cucsSwNetflowMonSessionName = _CucsSwNetflowMonSessionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 7),
    _CucsSwNetflowMonSessionName_Type()
)
cucsSwNetflowMonSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionName.setStatus("current")
_CucsSwNetflowMonSessionPeerDn_Type = SnmpAdminString
_CucsSwNetflowMonSessionPeerDn_Object = MibTableColumn
cucsSwNetflowMonSessionPeerDn = _CucsSwNetflowMonSessionPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 8),
    _CucsSwNetflowMonSessionPeerDn_Type()
)
cucsSwNetflowMonSessionPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionPeerDn.setStatus("current")
_CucsSwNetflowMonSessionProtocol_Type = CucsSwNetflowMonSessionProtocol
_CucsSwNetflowMonSessionProtocol_Object = MibTableColumn
cucsSwNetflowMonSessionProtocol = _CucsSwNetflowMonSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 9),
    _CucsSwNetflowMonSessionProtocol_Type()
)
cucsSwNetflowMonSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionProtocol.setStatus("current")
_CucsSwNetflowMonSessionSession_Type = Gauge32
_CucsSwNetflowMonSessionSession_Object = MibTableColumn
cucsSwNetflowMonSessionSession = _CucsSwNetflowMonSessionSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 10),
    _CucsSwNetflowMonSessionSession_Type()
)
cucsSwNetflowMonSessionSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionSession.setStatus("current")
_CucsSwNetflowMonSessionSwitchId_Type = CucsNetworkSwitchId
_CucsSwNetflowMonSessionSwitchId_Object = MibTableColumn
cucsSwNetflowMonSessionSwitchId = _CucsSwNetflowMonSessionSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 11),
    _CucsSwNetflowMonSessionSwitchId_Type()
)
cucsSwNetflowMonSessionSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionSwitchId.setStatus("current")
_CucsSwNetflowMonSessionTransport_Type = CucsSwEthFlowMonSessionTransport
_CucsSwNetflowMonSessionTransport_Object = MibTableColumn
cucsSwNetflowMonSessionTransport = _CucsSwNetflowMonSessionTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 12),
    _CucsSwNetflowMonSessionTransport_Type()
)
cucsSwNetflowMonSessionTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionTransport.setStatus("current")
_CucsSwNetflowMonSessionType_Type = CucsSwEthFlowMonSessionType
_CucsSwNetflowMonSessionType_Object = MibTableColumn
cucsSwNetflowMonSessionType = _CucsSwNetflowMonSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 77, 1, 13),
    _CucsSwNetflowMonSessionType_Type()
)
cucsSwNetflowMonSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonSessionType.setStatus("current")
_CucsSwNetflowMonitorTable_Object = MibTable
cucsSwNetflowMonitorTable = _CucsSwNetflowMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78)
)
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorTable.setStatus("current")
_CucsSwNetflowMonitorEntry_Object = MibTableRow
cucsSwNetflowMonitorEntry = _CucsSwNetflowMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1)
)
cucsSwNetflowMonitorEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwNetflowMonitorInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorEntry.setStatus("current")
_CucsSwNetflowMonitorInstanceId_Type = CucsManagedObjectId
_CucsSwNetflowMonitorInstanceId_Object = MibTableColumn
cucsSwNetflowMonitorInstanceId = _CucsSwNetflowMonitorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 1),
    _CucsSwNetflowMonitorInstanceId_Type()
)
cucsSwNetflowMonitorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorInstanceId.setStatus("current")
_CucsSwNetflowMonitorDn_Type = CucsManagedObjectDn
_CucsSwNetflowMonitorDn_Object = MibTableColumn
cucsSwNetflowMonitorDn = _CucsSwNetflowMonitorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 2),
    _CucsSwNetflowMonitorDn_Type()
)
cucsSwNetflowMonitorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorDn.setStatus("current")
_CucsSwNetflowMonitorRn_Type = SnmpAdminString
_CucsSwNetflowMonitorRn_Object = MibTableColumn
cucsSwNetflowMonitorRn = _CucsSwNetflowMonitorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 3),
    _CucsSwNetflowMonitorRn_Type()
)
cucsSwNetflowMonitorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRn.setStatus("current")
_CucsSwNetflowMonitorActiveTimeout_Type = Gauge32
_CucsSwNetflowMonitorActiveTimeout_Object = MibTableColumn
cucsSwNetflowMonitorActiveTimeout = _CucsSwNetflowMonitorActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 4),
    _CucsSwNetflowMonitorActiveTimeout_Type()
)
cucsSwNetflowMonitorActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorActiveTimeout.setStatus("current")
_CucsSwNetflowMonitorAdminState_Type = CucsSwFlowMonitorAdminState
_CucsSwNetflowMonitorAdminState_Object = MibTableColumn
cucsSwNetflowMonitorAdminState = _CucsSwNetflowMonitorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 5),
    _CucsSwNetflowMonitorAdminState_Type()
)
cucsSwNetflowMonitorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorAdminState.setStatus("current")
_CucsSwNetflowMonitorFlowRecordDefName_Type = SnmpAdminString
_CucsSwNetflowMonitorFlowRecordDefName_Object = MibTableColumn
cucsSwNetflowMonitorFlowRecordDefName = _CucsSwNetflowMonitorFlowRecordDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 6),
    _CucsSwNetflowMonitorFlowRecordDefName_Type()
)
cucsSwNetflowMonitorFlowRecordDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorFlowRecordDefName.setStatus("current")
_CucsSwNetflowMonitorInactiveTimeout_Type = Gauge32
_CucsSwNetflowMonitorInactiveTimeout_Object = MibTableColumn
cucsSwNetflowMonitorInactiveTimeout = _CucsSwNetflowMonitorInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 7),
    _CucsSwNetflowMonitorInactiveTimeout_Type()
)
cucsSwNetflowMonitorInactiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorInactiveTimeout.setStatus("current")
_CucsSwNetflowMonitorIsValidConfig_Type = CucsSwNFConfigStatus
_CucsSwNetflowMonitorIsValidConfig_Object = MibTableColumn
cucsSwNetflowMonitorIsValidConfig = _CucsSwNetflowMonitorIsValidConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 8),
    _CucsSwNetflowMonitorIsValidConfig_Type()
)
cucsSwNetflowMonitorIsValidConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorIsValidConfig.setStatus("current")
_CucsSwNetflowMonitorLifeCycle_Type = CucsSwMonLifeCycle
_CucsSwNetflowMonitorLifeCycle_Object = MibTableColumn
cucsSwNetflowMonitorLifeCycle = _CucsSwNetflowMonitorLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 9),
    _CucsSwNetflowMonitorLifeCycle_Type()
)
cucsSwNetflowMonitorLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorLifeCycle.setStatus("current")
_CucsSwNetflowMonitorName_Type = SnmpAdminString
_CucsSwNetflowMonitorName_Object = MibTableColumn
cucsSwNetflowMonitorName = _CucsSwNetflowMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 10),
    _CucsSwNetflowMonitorName_Type()
)
cucsSwNetflowMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorName.setStatus("current")
_CucsSwNetflowMonitorPeerDn_Type = SnmpAdminString
_CucsSwNetflowMonitorPeerDn_Object = MibTableColumn
cucsSwNetflowMonitorPeerDn = _CucsSwNetflowMonitorPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 11),
    _CucsSwNetflowMonitorPeerDn_Type()
)
cucsSwNetflowMonitorPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorPeerDn.setStatus("current")
_CucsSwNetflowMonitorProtocol_Type = CucsSwNetflowMonitorProtocol
_CucsSwNetflowMonitorProtocol_Object = MibTableColumn
cucsSwNetflowMonitorProtocol = _CucsSwNetflowMonitorProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 12),
    _CucsSwNetflowMonitorProtocol_Type()
)
cucsSwNetflowMonitorProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorProtocol.setStatus("current")
_CucsSwNetflowMonitorSwitchId_Type = CucsNetworkSwitchId
_CucsSwNetflowMonitorSwitchId_Object = MibTableColumn
cucsSwNetflowMonitorSwitchId = _CucsSwNetflowMonitorSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 13),
    _CucsSwNetflowMonitorSwitchId_Type()
)
cucsSwNetflowMonitorSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorSwitchId.setStatus("current")
_CucsSwNetflowMonitorTransport_Type = CucsSwEthLanFlowMonitorTransport
_CucsSwNetflowMonitorTransport_Object = MibTableColumn
cucsSwNetflowMonitorTransport = _CucsSwNetflowMonitorTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 14),
    _CucsSwNetflowMonitorTransport_Type()
)
cucsSwNetflowMonitorTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorTransport.setStatus("current")
_CucsSwNetflowMonitorType_Type = CucsSwEthLanFlowMonitorType
_CucsSwNetflowMonitorType_Object = MibTableColumn
cucsSwNetflowMonitorType = _CucsSwNetflowMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 78, 1, 15),
    _CucsSwNetflowMonitorType_Type()
)
cucsSwNetflowMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorType.setStatus("current")
_CucsSwNetflowMonitorRefTable_Object = MibTable
cucsSwNetflowMonitorRefTable = _CucsSwNetflowMonitorRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79)
)
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefTable.setStatus("current")
_CucsSwNetflowMonitorRefEntry_Object = MibTableRow
cucsSwNetflowMonitorRefEntry = _CucsSwNetflowMonitorRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79, 1)
)
cucsSwNetflowMonitorRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwNetflowMonitorRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefEntry.setStatus("current")
_CucsSwNetflowMonitorRefInstanceId_Type = CucsManagedObjectId
_CucsSwNetflowMonitorRefInstanceId_Object = MibTableColumn
cucsSwNetflowMonitorRefInstanceId = _CucsSwNetflowMonitorRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79, 1, 1),
    _CucsSwNetflowMonitorRefInstanceId_Type()
)
cucsSwNetflowMonitorRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefInstanceId.setStatus("current")
_CucsSwNetflowMonitorRefDn_Type = CucsManagedObjectDn
_CucsSwNetflowMonitorRefDn_Object = MibTableColumn
cucsSwNetflowMonitorRefDn = _CucsSwNetflowMonitorRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79, 1, 2),
    _CucsSwNetflowMonitorRefDn_Type()
)
cucsSwNetflowMonitorRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefDn.setStatus("current")
_CucsSwNetflowMonitorRefRn_Type = SnmpAdminString
_CucsSwNetflowMonitorRefRn_Object = MibTableColumn
cucsSwNetflowMonitorRefRn = _CucsSwNetflowMonitorRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79, 1, 3),
    _CucsSwNetflowMonitorRefRn_Type()
)
cucsSwNetflowMonitorRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefRn.setStatus("current")
_CucsSwNetflowMonitorRefDirection_Type = CucsFabricDirection
_CucsSwNetflowMonitorRefDirection_Object = MibTableColumn
cucsSwNetflowMonitorRefDirection = _CucsSwNetflowMonitorRefDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79, 1, 4),
    _CucsSwNetflowMonitorRefDirection_Type()
)
cucsSwNetflowMonitorRefDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefDirection.setStatus("current")
_CucsSwNetflowMonitorRefKeyType_Type = CucsFabricFlowMonKeyType
_CucsSwNetflowMonitorRefKeyType_Object = MibTableColumn
cucsSwNetflowMonitorRefKeyType = _CucsSwNetflowMonitorRefKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79, 1, 5),
    _CucsSwNetflowMonitorRefKeyType_Type()
)
cucsSwNetflowMonitorRefKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefKeyType.setStatus("current")
_CucsSwNetflowMonitorRefName_Type = SnmpAdminString
_CucsSwNetflowMonitorRefName_Object = MibTableColumn
cucsSwNetflowMonitorRefName = _CucsSwNetflowMonitorRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79, 1, 6),
    _CucsSwNetflowMonitorRefName_Type()
)
cucsSwNetflowMonitorRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefName.setStatus("current")
_CucsSwNetflowMonitorRefSourceDn_Type = SnmpAdminString
_CucsSwNetflowMonitorRefSourceDn_Object = MibTableColumn
cucsSwNetflowMonitorRefSourceDn = _CucsSwNetflowMonitorRefSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 79, 1, 7),
    _CucsSwNetflowMonitorRefSourceDn_Type()
)
cucsSwNetflowMonitorRefSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowMonitorRefSourceDn.setStatus("current")
_CucsSwNetflowRecordDefTable_Object = MibTable
cucsSwNetflowRecordDefTable = _CucsSwNetflowRecordDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80)
)
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefTable.setStatus("current")
_CucsSwNetflowRecordDefEntry_Object = MibTableRow
cucsSwNetflowRecordDefEntry = _CucsSwNetflowRecordDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1)
)
cucsSwNetflowRecordDefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwNetflowRecordDefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefEntry.setStatus("current")
_CucsSwNetflowRecordDefInstanceId_Type = CucsManagedObjectId
_CucsSwNetflowRecordDefInstanceId_Object = MibTableColumn
cucsSwNetflowRecordDefInstanceId = _CucsSwNetflowRecordDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 1),
    _CucsSwNetflowRecordDefInstanceId_Type()
)
cucsSwNetflowRecordDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefInstanceId.setStatus("current")
_CucsSwNetflowRecordDefDn_Type = CucsManagedObjectDn
_CucsSwNetflowRecordDefDn_Object = MibTableColumn
cucsSwNetflowRecordDefDn = _CucsSwNetflowRecordDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 2),
    _CucsSwNetflowRecordDefDn_Type()
)
cucsSwNetflowRecordDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefDn.setStatus("current")
_CucsSwNetflowRecordDefRn_Type = SnmpAdminString
_CucsSwNetflowRecordDefRn_Object = MibTableColumn
cucsSwNetflowRecordDefRn = _CucsSwNetflowRecordDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 3),
    _CucsSwNetflowRecordDefRn_Type()
)
cucsSwNetflowRecordDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefRn.setStatus("current")
_CucsSwNetflowRecordDefIpv4keys_Type = CucsFabricFlowMonIpv4Keys
_CucsSwNetflowRecordDefIpv4keys_Object = MibTableColumn
cucsSwNetflowRecordDefIpv4keys = _CucsSwNetflowRecordDefIpv4keys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 4),
    _CucsSwNetflowRecordDefIpv4keys_Type()
)
cucsSwNetflowRecordDefIpv4keys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefIpv4keys.setStatus("current")
_CucsSwNetflowRecordDefIpv6keys_Type = CucsFabricFlowMonIpv6Keys
_CucsSwNetflowRecordDefIpv6keys_Object = MibTableColumn
cucsSwNetflowRecordDefIpv6keys = _CucsSwNetflowRecordDefIpv6keys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 5),
    _CucsSwNetflowRecordDefIpv6keys_Type()
)
cucsSwNetflowRecordDefIpv6keys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefIpv6keys.setStatus("current")
_CucsSwNetflowRecordDefKeyType_Type = CucsFabricFlowMonKeyType
_CucsSwNetflowRecordDefKeyType_Object = MibTableColumn
cucsSwNetflowRecordDefKeyType = _CucsSwNetflowRecordDefKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 6),
    _CucsSwNetflowRecordDefKeyType_Type()
)
cucsSwNetflowRecordDefKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefKeyType.setStatus("current")
_CucsSwNetflowRecordDefL2keys_Type = CucsFabricFlowMonL2Keys
_CucsSwNetflowRecordDefL2keys_Object = MibTableColumn
cucsSwNetflowRecordDefL2keys = _CucsSwNetflowRecordDefL2keys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 7),
    _CucsSwNetflowRecordDefL2keys_Type()
)
cucsSwNetflowRecordDefL2keys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefL2keys.setStatus("current")
_CucsSwNetflowRecordDefLifeCycle_Type = CucsSwMonLifeCycle
_CucsSwNetflowRecordDefLifeCycle_Object = MibTableColumn
cucsSwNetflowRecordDefLifeCycle = _CucsSwNetflowRecordDefLifeCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 8),
    _CucsSwNetflowRecordDefLifeCycle_Type()
)
cucsSwNetflowRecordDefLifeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefLifeCycle.setStatus("current")
_CucsSwNetflowRecordDefName_Type = SnmpAdminString
_CucsSwNetflowRecordDefName_Object = MibTableColumn
cucsSwNetflowRecordDefName = _CucsSwNetflowRecordDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 9),
    _CucsSwNetflowRecordDefName_Type()
)
cucsSwNetflowRecordDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefName.setStatus("current")
_CucsSwNetflowRecordDefNonkeys_Type = CucsFabricFlowMonNonKeys
_CucsSwNetflowRecordDefNonkeys_Object = MibTableColumn
cucsSwNetflowRecordDefNonkeys = _CucsSwNetflowRecordDefNonkeys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 10),
    _CucsSwNetflowRecordDefNonkeys_Type()
)
cucsSwNetflowRecordDefNonkeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefNonkeys.setStatus("current")
_CucsSwNetflowRecordDefPeerDn_Type = SnmpAdminString
_CucsSwNetflowRecordDefPeerDn_Object = MibTableColumn
cucsSwNetflowRecordDefPeerDn = _CucsSwNetflowRecordDefPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 11),
    _CucsSwNetflowRecordDefPeerDn_Type()
)
cucsSwNetflowRecordDefPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefPeerDn.setStatus("current")
_CucsSwNetflowRecordDefProtocol_Type = CucsSwNetflowRecordDefProtocol
_CucsSwNetflowRecordDefProtocol_Object = MibTableColumn
cucsSwNetflowRecordDefProtocol = _CucsSwNetflowRecordDefProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 12),
    _CucsSwNetflowRecordDefProtocol_Type()
)
cucsSwNetflowRecordDefProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefProtocol.setStatus("current")
_CucsSwNetflowRecordDefSwitchId_Type = CucsNetworkSwitchId
_CucsSwNetflowRecordDefSwitchId_Object = MibTableColumn
cucsSwNetflowRecordDefSwitchId = _CucsSwNetflowRecordDefSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 13),
    _CucsSwNetflowRecordDefSwitchId_Type()
)
cucsSwNetflowRecordDefSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefSwitchId.setStatus("current")
_CucsSwNetflowRecordDefTransport_Type = CucsSwEthLanFlowRecordDefTransport
_CucsSwNetflowRecordDefTransport_Object = MibTableColumn
cucsSwNetflowRecordDefTransport = _CucsSwNetflowRecordDefTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 14),
    _CucsSwNetflowRecordDefTransport_Type()
)
cucsSwNetflowRecordDefTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefTransport.setStatus("current")
_CucsSwNetflowRecordDefType_Type = CucsSwEthLanFlowRecordDefType
_CucsSwNetflowRecordDefType_Object = MibTableColumn
cucsSwNetflowRecordDefType = _CucsSwNetflowRecordDefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 80, 1, 15),
    _CucsSwNetflowRecordDefType_Type()
)
cucsSwNetflowRecordDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwNetflowRecordDefType.setStatus("current")
_CucsSwVirtL3IntfTable_Object = MibTable
cucsSwVirtL3IntfTable = _CucsSwVirtL3IntfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81)
)
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfTable.setStatus("current")
_CucsSwVirtL3IntfEntry_Object = MibTableRow
cucsSwVirtL3IntfEntry = _CucsSwVirtL3IntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81, 1)
)
cucsSwVirtL3IntfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwVirtL3IntfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfEntry.setStatus("current")
_CucsSwVirtL3IntfInstanceId_Type = CucsManagedObjectId
_CucsSwVirtL3IntfInstanceId_Object = MibTableColumn
cucsSwVirtL3IntfInstanceId = _CucsSwVirtL3IntfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81, 1, 1),
    _CucsSwVirtL3IntfInstanceId_Type()
)
cucsSwVirtL3IntfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfInstanceId.setStatus("current")
_CucsSwVirtL3IntfDn_Type = CucsManagedObjectDn
_CucsSwVirtL3IntfDn_Object = MibTableColumn
cucsSwVirtL3IntfDn = _CucsSwVirtL3IntfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81, 1, 2),
    _CucsSwVirtL3IntfDn_Type()
)
cucsSwVirtL3IntfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfDn.setStatus("current")
_CucsSwVirtL3IntfRn_Type = SnmpAdminString
_CucsSwVirtL3IntfRn_Object = MibTableColumn
cucsSwVirtL3IntfRn = _CucsSwVirtL3IntfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81, 1, 3),
    _CucsSwVirtL3IntfRn_Type()
)
cucsSwVirtL3IntfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfRn.setStatus("current")
_CucsSwVirtL3IntfIpAddress_Type = InetAddressIPv4
_CucsSwVirtL3IntfIpAddress_Object = MibTableColumn
cucsSwVirtL3IntfIpAddress = _CucsSwVirtL3IntfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81, 1, 4),
    _CucsSwVirtL3IntfIpAddress_Type()
)
cucsSwVirtL3IntfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfIpAddress.setStatus("current")
_CucsSwVirtL3IntfName_Type = SnmpAdminString
_CucsSwVirtL3IntfName_Object = MibTableColumn
cucsSwVirtL3IntfName = _CucsSwVirtL3IntfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81, 1, 5),
    _CucsSwVirtL3IntfName_Type()
)
cucsSwVirtL3IntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfName.setStatus("current")
_CucsSwVirtL3IntfNetmask_Type = InetAddressIPv4
_CucsSwVirtL3IntfNetmask_Object = MibTableColumn
cucsSwVirtL3IntfNetmask = _CucsSwVirtL3IntfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81, 1, 6),
    _CucsSwVirtL3IntfNetmask_Type()
)
cucsSwVirtL3IntfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfNetmask.setStatus("current")
_CucsSwVirtL3IntfVlanId_Type = Gauge32
_CucsSwVirtL3IntfVlanId_Object = MibTableColumn
cucsSwVirtL3IntfVlanId = _CucsSwVirtL3IntfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 81, 1, 7),
    _CucsSwVirtL3IntfVlanId_Type()
)
cucsSwVirtL3IntfVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVirtL3IntfVlanId.setStatus("current")
_CucsSwSubGroupTable_Object = MibTable
cucsSwSubGroupTable = _CucsSwSubGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82)
)
if mibBuilder.loadTexts:
    cucsSwSubGroupTable.setStatus("current")
_CucsSwSubGroupEntry_Object = MibTableRow
cucsSwSubGroupEntry = _CucsSwSubGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1)
)
cucsSwSubGroupEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwSubGroupInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwSubGroupEntry.setStatus("current")
_CucsSwSubGroupInstanceId_Type = CucsManagedObjectId
_CucsSwSubGroupInstanceId_Object = MibTableColumn
cucsSwSubGroupInstanceId = _CucsSwSubGroupInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 1),
    _CucsSwSubGroupInstanceId_Type()
)
cucsSwSubGroupInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwSubGroupInstanceId.setStatus("current")
_CucsSwSubGroupDn_Type = CucsManagedObjectDn
_CucsSwSubGroupDn_Object = MibTableColumn
cucsSwSubGroupDn = _CucsSwSubGroupDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 2),
    _CucsSwSubGroupDn_Type()
)
cucsSwSubGroupDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupDn.setStatus("current")
_CucsSwSubGroupRn_Type = SnmpAdminString
_CucsSwSubGroupRn_Object = MibTableColumn
cucsSwSubGroupRn = _CucsSwSubGroupRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 3),
    _CucsSwSubGroupRn_Type()
)
cucsSwSubGroupRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupRn.setStatus("current")
_CucsSwSubGroupAggrPortId_Type = CucsSwSubGroupAggrPortId
_CucsSwSubGroupAggrPortId_Object = MibTableColumn
cucsSwSubGroupAggrPortId = _CucsSwSubGroupAggrPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 4),
    _CucsSwSubGroupAggrPortId_Type()
)
cucsSwSubGroupAggrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupAggrPortId.setStatus("current")
_CucsSwSubGroupLicGP_Type = Unsigned64
_CucsSwSubGroupLicGP_Object = MibTableColumn
cucsSwSubGroupLicGP = _CucsSwSubGroupLicGP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 5),
    _CucsSwSubGroupLicGP_Type()
)
cucsSwSubGroupLicGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupLicGP.setStatus("current")
_CucsSwSubGroupLicState_Type = CucsLicenseState
_CucsSwSubGroupLicState_Object = MibTableColumn
cucsSwSubGroupLicState = _CucsSwSubGroupLicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 6),
    _CucsSwSubGroupLicState_Type()
)
cucsSwSubGroupLicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupLicState.setStatus("current")
_CucsSwSubGroupLocale_Type = CucsNetworkLocale
_CucsSwSubGroupLocale_Object = MibTableColumn
cucsSwSubGroupLocale = _CucsSwSubGroupLocale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 7),
    _CucsSwSubGroupLocale_Type()
)
cucsSwSubGroupLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupLocale.setStatus("current")
_CucsSwSubGroupName_Type = SnmpAdminString
_CucsSwSubGroupName_Object = MibTableColumn
cucsSwSubGroupName = _CucsSwSubGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 8),
    _CucsSwSubGroupName_Type()
)
cucsSwSubGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupName.setStatus("current")
_CucsSwSubGroupSlotId_Type = CucsSwSubGroupSlotId
_CucsSwSubGroupSlotId_Object = MibTableColumn
cucsSwSubGroupSlotId = _CucsSwSubGroupSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 9),
    _CucsSwSubGroupSlotId_Type()
)
cucsSwSubGroupSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupSlotId.setStatus("current")
_CucsSwSubGroupSwitchId_Type = CucsNetworkSwitchId
_CucsSwSubGroupSwitchId_Object = MibTableColumn
cucsSwSubGroupSwitchId = _CucsSwSubGroupSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 10),
    _CucsSwSubGroupSwitchId_Type()
)
cucsSwSubGroupSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupSwitchId.setStatus("current")
_CucsSwSubGroupTransport_Type = CucsNetworkTransport
_CucsSwSubGroupTransport_Object = MibTableColumn
cucsSwSubGroupTransport = _CucsSwSubGroupTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 11),
    _CucsSwSubGroupTransport_Type()
)
cucsSwSubGroupTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupTransport.setStatus("current")
_CucsSwSubGroupType_Type = CucsNetworkConnectionType
_CucsSwSubGroupType_Object = MibTableColumn
cucsSwSubGroupType = _CucsSwSubGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 82, 1, 12),
    _CucsSwSubGroupType_Type()
)
cucsSwSubGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwSubGroupType.setStatus("current")
_CucsSwExtUtilityTable_Object = MibTable
cucsSwExtUtilityTable = _CucsSwExtUtilityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83)
)
if mibBuilder.loadTexts:
    cucsSwExtUtilityTable.setStatus("current")
_CucsSwExtUtilityEntry_Object = MibTableRow
cucsSwExtUtilityEntry = _CucsSwExtUtilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1)
)
cucsSwExtUtilityEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwExtUtilityInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwExtUtilityEntry.setStatus("current")
_CucsSwExtUtilityInstanceId_Type = CucsManagedObjectId
_CucsSwExtUtilityInstanceId_Object = MibTableColumn
cucsSwExtUtilityInstanceId = _CucsSwExtUtilityInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 1),
    _CucsSwExtUtilityInstanceId_Type()
)
cucsSwExtUtilityInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwExtUtilityInstanceId.setStatus("current")
_CucsSwExtUtilityDn_Type = CucsManagedObjectDn
_CucsSwExtUtilityDn_Object = MibTableColumn
cucsSwExtUtilityDn = _CucsSwExtUtilityDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 2),
    _CucsSwExtUtilityDn_Type()
)
cucsSwExtUtilityDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityDn.setStatus("current")
_CucsSwExtUtilityRn_Type = SnmpAdminString
_CucsSwExtUtilityRn_Object = MibTableColumn
cucsSwExtUtilityRn = _CucsSwExtUtilityRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 3),
    _CucsSwExtUtilityRn_Type()
)
cucsSwExtUtilityRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityRn.setStatus("current")
_CucsSwExtUtilityConfMode_Type = CucsSwConfMode
_CucsSwExtUtilityConfMode_Object = MibTableColumn
cucsSwExtUtilityConfMode = _CucsSwExtUtilityConfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 4),
    _CucsSwExtUtilityConfMode_Type()
)
cucsSwExtUtilityConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityConfMode.setStatus("current")
_CucsSwExtUtilityFsmDescr_Type = SnmpAdminString
_CucsSwExtUtilityFsmDescr_Object = MibTableColumn
cucsSwExtUtilityFsmDescr = _CucsSwExtUtilityFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 5),
    _CucsSwExtUtilityFsmDescr_Type()
)
cucsSwExtUtilityFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmDescr.setStatus("current")
_CucsSwExtUtilityFsmPrev_Type = SnmpAdminString
_CucsSwExtUtilityFsmPrev_Object = MibTableColumn
cucsSwExtUtilityFsmPrev = _CucsSwExtUtilityFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 6),
    _CucsSwExtUtilityFsmPrev_Type()
)
cucsSwExtUtilityFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmPrev.setStatus("current")
_CucsSwExtUtilityFsmProgr_Type = Gauge32
_CucsSwExtUtilityFsmProgr_Object = MibTableColumn
cucsSwExtUtilityFsmProgr = _CucsSwExtUtilityFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 7),
    _CucsSwExtUtilityFsmProgr_Type()
)
cucsSwExtUtilityFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmProgr.setStatus("current")
_CucsSwExtUtilityFsmRmtInvErrCode_Type = Gauge32
_CucsSwExtUtilityFsmRmtInvErrCode_Object = MibTableColumn
cucsSwExtUtilityFsmRmtInvErrCode = _CucsSwExtUtilityFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 8),
    _CucsSwExtUtilityFsmRmtInvErrCode_Type()
)
cucsSwExtUtilityFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmRmtInvErrCode.setStatus("current")
_CucsSwExtUtilityFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsSwExtUtilityFsmRmtInvErrDescr_Object = MibTableColumn
cucsSwExtUtilityFsmRmtInvErrDescr = _CucsSwExtUtilityFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 9),
    _CucsSwExtUtilityFsmRmtInvErrDescr_Type()
)
cucsSwExtUtilityFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmRmtInvErrDescr.setStatus("current")
_CucsSwExtUtilityFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsSwExtUtilityFsmRmtInvRslt_Object = MibTableColumn
cucsSwExtUtilityFsmRmtInvRslt = _CucsSwExtUtilityFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 10),
    _CucsSwExtUtilityFsmRmtInvRslt_Type()
)
cucsSwExtUtilityFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmRmtInvRslt.setStatus("current")
_CucsSwExtUtilityFsmStageDescr_Type = SnmpAdminString
_CucsSwExtUtilityFsmStageDescr_Object = MibTableColumn
cucsSwExtUtilityFsmStageDescr = _CucsSwExtUtilityFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 11),
    _CucsSwExtUtilityFsmStageDescr_Type()
)
cucsSwExtUtilityFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageDescr.setStatus("current")
_CucsSwExtUtilityFsmStamp_Type = DateAndTime
_CucsSwExtUtilityFsmStamp_Object = MibTableColumn
cucsSwExtUtilityFsmStamp = _CucsSwExtUtilityFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 12),
    _CucsSwExtUtilityFsmStamp_Type()
)
cucsSwExtUtilityFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStamp.setStatus("current")
_CucsSwExtUtilityFsmStatus_Type = SnmpAdminString
_CucsSwExtUtilityFsmStatus_Object = MibTableColumn
cucsSwExtUtilityFsmStatus = _CucsSwExtUtilityFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 13),
    _CucsSwExtUtilityFsmStatus_Type()
)
cucsSwExtUtilityFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStatus.setStatus("current")
_CucsSwExtUtilityFsmTry_Type = Gauge32
_CucsSwExtUtilityFsmTry_Object = MibTableColumn
cucsSwExtUtilityFsmTry = _CucsSwExtUtilityFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 14),
    _CucsSwExtUtilityFsmTry_Type()
)
cucsSwExtUtilityFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTry.setStatus("current")
_CucsSwExtUtilitySwitchId_Type = CucsNetworkSwitchId
_CucsSwExtUtilitySwitchId_Object = MibTableColumn
cucsSwExtUtilitySwitchId = _CucsSwExtUtilitySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 83, 1, 15),
    _CucsSwExtUtilitySwitchId_Type()
)
cucsSwExtUtilitySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilitySwitchId.setStatus("current")
_CucsSwExtUtilityFsmTable_Object = MibTable
cucsSwExtUtilityFsmTable = _CucsSwExtUtilityFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84)
)
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTable.setStatus("current")
_CucsSwExtUtilityFsmEntry_Object = MibTableRow
cucsSwExtUtilityFsmEntry = _CucsSwExtUtilityFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1)
)
cucsSwExtUtilityFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwExtUtilityFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmEntry.setStatus("current")
_CucsSwExtUtilityFsmInstanceId_Type = CucsManagedObjectId
_CucsSwExtUtilityFsmInstanceId_Object = MibTableColumn
cucsSwExtUtilityFsmInstanceId = _CucsSwExtUtilityFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 1),
    _CucsSwExtUtilityFsmInstanceId_Type()
)
cucsSwExtUtilityFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmInstanceId.setStatus("current")
_CucsSwExtUtilityFsmDn_Type = CucsManagedObjectDn
_CucsSwExtUtilityFsmDn_Object = MibTableColumn
cucsSwExtUtilityFsmDn = _CucsSwExtUtilityFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 2),
    _CucsSwExtUtilityFsmDn_Type()
)
cucsSwExtUtilityFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmDn.setStatus("current")
_CucsSwExtUtilityFsmRn_Type = SnmpAdminString
_CucsSwExtUtilityFsmRn_Object = MibTableColumn
cucsSwExtUtilityFsmRn = _CucsSwExtUtilityFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 3),
    _CucsSwExtUtilityFsmRn_Type()
)
cucsSwExtUtilityFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmRn.setStatus("current")
_CucsSwExtUtilityFsmCompletionTime_Type = DateAndTime
_CucsSwExtUtilityFsmCompletionTime_Object = MibTableColumn
cucsSwExtUtilityFsmCompletionTime = _CucsSwExtUtilityFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 4),
    _CucsSwExtUtilityFsmCompletionTime_Type()
)
cucsSwExtUtilityFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmCompletionTime.setStatus("current")
_CucsSwExtUtilityFsmCurrentFsm_Type = CucsSwExtUtilityFsmCurrentFsm
_CucsSwExtUtilityFsmCurrentFsm_Object = MibTableColumn
cucsSwExtUtilityFsmCurrentFsm = _CucsSwExtUtilityFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 5),
    _CucsSwExtUtilityFsmCurrentFsm_Type()
)
cucsSwExtUtilityFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmCurrentFsm.setStatus("current")
_CucsSwExtUtilityFsmDescrData_Type = SnmpAdminString
_CucsSwExtUtilityFsmDescrData_Object = MibTableColumn
cucsSwExtUtilityFsmDescrData = _CucsSwExtUtilityFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 6),
    _CucsSwExtUtilityFsmDescrData_Type()
)
cucsSwExtUtilityFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmDescrData.setStatus("current")
_CucsSwExtUtilityFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsSwExtUtilityFsmFsmStatus_Object = MibTableColumn
cucsSwExtUtilityFsmFsmStatus = _CucsSwExtUtilityFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 7),
    _CucsSwExtUtilityFsmFsmStatus_Type()
)
cucsSwExtUtilityFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmFsmStatus.setStatus("current")
_CucsSwExtUtilityFsmProgress_Type = Gauge32
_CucsSwExtUtilityFsmProgress_Object = MibTableColumn
cucsSwExtUtilityFsmProgress = _CucsSwExtUtilityFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 8),
    _CucsSwExtUtilityFsmProgress_Type()
)
cucsSwExtUtilityFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmProgress.setStatus("current")
_CucsSwExtUtilityFsmRmtErrCode_Type = Gauge32
_CucsSwExtUtilityFsmRmtErrCode_Object = MibTableColumn
cucsSwExtUtilityFsmRmtErrCode = _CucsSwExtUtilityFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 9),
    _CucsSwExtUtilityFsmRmtErrCode_Type()
)
cucsSwExtUtilityFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmRmtErrCode.setStatus("current")
_CucsSwExtUtilityFsmRmtErrDescr_Type = SnmpAdminString
_CucsSwExtUtilityFsmRmtErrDescr_Object = MibTableColumn
cucsSwExtUtilityFsmRmtErrDescr = _CucsSwExtUtilityFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 10),
    _CucsSwExtUtilityFsmRmtErrDescr_Type()
)
cucsSwExtUtilityFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmRmtErrDescr.setStatus("current")
_CucsSwExtUtilityFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsSwExtUtilityFsmRmtRslt_Object = MibTableColumn
cucsSwExtUtilityFsmRmtRslt = _CucsSwExtUtilityFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 84, 1, 11),
    _CucsSwExtUtilityFsmRmtRslt_Type()
)
cucsSwExtUtilityFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmRmtRslt.setStatus("current")
_CucsSwExtUtilityFsmStageTable_Object = MibTable
cucsSwExtUtilityFsmStageTable = _CucsSwExtUtilityFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85)
)
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageTable.setStatus("current")
_CucsSwExtUtilityFsmStageEntry_Object = MibTableRow
cucsSwExtUtilityFsmStageEntry = _CucsSwExtUtilityFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1)
)
cucsSwExtUtilityFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwExtUtilityFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageEntry.setStatus("current")
_CucsSwExtUtilityFsmStageInstanceId_Type = CucsManagedObjectId
_CucsSwExtUtilityFsmStageInstanceId_Object = MibTableColumn
cucsSwExtUtilityFsmStageInstanceId = _CucsSwExtUtilityFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 1),
    _CucsSwExtUtilityFsmStageInstanceId_Type()
)
cucsSwExtUtilityFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageInstanceId.setStatus("current")
_CucsSwExtUtilityFsmStageDn_Type = CucsManagedObjectDn
_CucsSwExtUtilityFsmStageDn_Object = MibTableColumn
cucsSwExtUtilityFsmStageDn = _CucsSwExtUtilityFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 2),
    _CucsSwExtUtilityFsmStageDn_Type()
)
cucsSwExtUtilityFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageDn.setStatus("current")
_CucsSwExtUtilityFsmStageRn_Type = SnmpAdminString
_CucsSwExtUtilityFsmStageRn_Object = MibTableColumn
cucsSwExtUtilityFsmStageRn = _CucsSwExtUtilityFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 3),
    _CucsSwExtUtilityFsmStageRn_Type()
)
cucsSwExtUtilityFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageRn.setStatus("current")
_CucsSwExtUtilityFsmStageDescrData_Type = SnmpAdminString
_CucsSwExtUtilityFsmStageDescrData_Object = MibTableColumn
cucsSwExtUtilityFsmStageDescrData = _CucsSwExtUtilityFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 4),
    _CucsSwExtUtilityFsmStageDescrData_Type()
)
cucsSwExtUtilityFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageDescrData.setStatus("current")
_CucsSwExtUtilityFsmStageLastUpdateTime_Type = DateAndTime
_CucsSwExtUtilityFsmStageLastUpdateTime_Object = MibTableColumn
cucsSwExtUtilityFsmStageLastUpdateTime = _CucsSwExtUtilityFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 5),
    _CucsSwExtUtilityFsmStageLastUpdateTime_Type()
)
cucsSwExtUtilityFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageLastUpdateTime.setStatus("current")
_CucsSwExtUtilityFsmStageName_Type = CucsSwExtUtilityFsmStageName
_CucsSwExtUtilityFsmStageName_Object = MibTableColumn
cucsSwExtUtilityFsmStageName = _CucsSwExtUtilityFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 6),
    _CucsSwExtUtilityFsmStageName_Type()
)
cucsSwExtUtilityFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageName.setStatus("current")
_CucsSwExtUtilityFsmStageOrder_Type = Gauge32
_CucsSwExtUtilityFsmStageOrder_Object = MibTableColumn
cucsSwExtUtilityFsmStageOrder = _CucsSwExtUtilityFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 7),
    _CucsSwExtUtilityFsmStageOrder_Type()
)
cucsSwExtUtilityFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageOrder.setStatus("current")
_CucsSwExtUtilityFsmStageRetry_Type = Gauge32
_CucsSwExtUtilityFsmStageRetry_Object = MibTableColumn
cucsSwExtUtilityFsmStageRetry = _CucsSwExtUtilityFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 8),
    _CucsSwExtUtilityFsmStageRetry_Type()
)
cucsSwExtUtilityFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageRetry.setStatus("current")
_CucsSwExtUtilityFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsSwExtUtilityFsmStageStageStatus_Object = MibTableColumn
cucsSwExtUtilityFsmStageStageStatus = _CucsSwExtUtilityFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 85, 1, 9),
    _CucsSwExtUtilityFsmStageStageStatus_Type()
)
cucsSwExtUtilityFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmStageStageStatus.setStatus("current")
_CucsSwExtUtilityFsmTaskTable_Object = MibTable
cucsSwExtUtilityFsmTaskTable = _CucsSwExtUtilityFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86)
)
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskTable.setStatus("current")
_CucsSwExtUtilityFsmTaskEntry_Object = MibTableRow
cucsSwExtUtilityFsmTaskEntry = _CucsSwExtUtilityFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86, 1)
)
cucsSwExtUtilityFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwExtUtilityFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskEntry.setStatus("current")
_CucsSwExtUtilityFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsSwExtUtilityFsmTaskInstanceId_Object = MibTableColumn
cucsSwExtUtilityFsmTaskInstanceId = _CucsSwExtUtilityFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86, 1, 1),
    _CucsSwExtUtilityFsmTaskInstanceId_Type()
)
cucsSwExtUtilityFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskInstanceId.setStatus("current")
_CucsSwExtUtilityFsmTaskDn_Type = CucsManagedObjectDn
_CucsSwExtUtilityFsmTaskDn_Object = MibTableColumn
cucsSwExtUtilityFsmTaskDn = _CucsSwExtUtilityFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86, 1, 2),
    _CucsSwExtUtilityFsmTaskDn_Type()
)
cucsSwExtUtilityFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskDn.setStatus("current")
_CucsSwExtUtilityFsmTaskRn_Type = SnmpAdminString
_CucsSwExtUtilityFsmTaskRn_Object = MibTableColumn
cucsSwExtUtilityFsmTaskRn = _CucsSwExtUtilityFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86, 1, 3),
    _CucsSwExtUtilityFsmTaskRn_Type()
)
cucsSwExtUtilityFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskRn.setStatus("current")
_CucsSwExtUtilityFsmTaskCompletion_Type = CucsFsmCompletion
_CucsSwExtUtilityFsmTaskCompletion_Object = MibTableColumn
cucsSwExtUtilityFsmTaskCompletion = _CucsSwExtUtilityFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86, 1, 4),
    _CucsSwExtUtilityFsmTaskCompletion_Type()
)
cucsSwExtUtilityFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskCompletion.setStatus("current")
_CucsSwExtUtilityFsmTaskFlags_Type = CucsFsmFlags
_CucsSwExtUtilityFsmTaskFlags_Object = MibTableColumn
cucsSwExtUtilityFsmTaskFlags = _CucsSwExtUtilityFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86, 1, 5),
    _CucsSwExtUtilityFsmTaskFlags_Type()
)
cucsSwExtUtilityFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskFlags.setStatus("current")
_CucsSwExtUtilityFsmTaskItem_Type = CucsSwExtUtilityFsmTaskItem
_CucsSwExtUtilityFsmTaskItem_Object = MibTableColumn
cucsSwExtUtilityFsmTaskItem = _CucsSwExtUtilityFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86, 1, 6),
    _CucsSwExtUtilityFsmTaskItem_Type()
)
cucsSwExtUtilityFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskItem.setStatus("current")
_CucsSwExtUtilityFsmTaskSeqId_Type = Gauge32
_CucsSwExtUtilityFsmTaskSeqId_Object = MibTableColumn
cucsSwExtUtilityFsmTaskSeqId = _CucsSwExtUtilityFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 86, 1, 7),
    _CucsSwExtUtilityFsmTaskSeqId_Type()
)
cucsSwExtUtilityFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwExtUtilityFsmTaskSeqId.setStatus("current")
_CucsSwPortBreakoutTable_Object = MibTable
cucsSwPortBreakoutTable = _CucsSwPortBreakoutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 87)
)
if mibBuilder.loadTexts:
    cucsSwPortBreakoutTable.setStatus("current")
_CucsSwPortBreakoutEntry_Object = MibTableRow
cucsSwPortBreakoutEntry = _CucsSwPortBreakoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 87, 1)
)
cucsSwPortBreakoutEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwPortBreakoutInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwPortBreakoutEntry.setStatus("current")
_CucsSwPortBreakoutInstanceId_Type = CucsManagedObjectId
_CucsSwPortBreakoutInstanceId_Object = MibTableColumn
cucsSwPortBreakoutInstanceId = _CucsSwPortBreakoutInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 87, 1, 1),
    _CucsSwPortBreakoutInstanceId_Type()
)
cucsSwPortBreakoutInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwPortBreakoutInstanceId.setStatus("current")
_CucsSwPortBreakoutDn_Type = CucsManagedObjectDn
_CucsSwPortBreakoutDn_Object = MibTableColumn
cucsSwPortBreakoutDn = _CucsSwPortBreakoutDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 87, 1, 2),
    _CucsSwPortBreakoutDn_Type()
)
cucsSwPortBreakoutDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPortBreakoutDn.setStatus("current")
_CucsSwPortBreakoutRn_Type = SnmpAdminString
_CucsSwPortBreakoutRn_Object = MibTableColumn
cucsSwPortBreakoutRn = _CucsSwPortBreakoutRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 87, 1, 3),
    _CucsSwPortBreakoutRn_Type()
)
cucsSwPortBreakoutRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPortBreakoutRn.setStatus("current")
_CucsSwPortBreakoutBreakoutType_Type = CucsSwBreakoutType
_CucsSwPortBreakoutBreakoutType_Object = MibTableColumn
cucsSwPortBreakoutBreakoutType = _CucsSwPortBreakoutBreakoutType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 87, 1, 4),
    _CucsSwPortBreakoutBreakoutType_Type()
)
cucsSwPortBreakoutBreakoutType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPortBreakoutBreakoutType.setStatus("current")
_CucsSwPortBreakoutPortId_Type = CucsSwPortBreakoutPortId
_CucsSwPortBreakoutPortId_Object = MibTableColumn
cucsSwPortBreakoutPortId = _CucsSwPortBreakoutPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 87, 1, 5),
    _CucsSwPortBreakoutPortId_Type()
)
cucsSwPortBreakoutPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPortBreakoutPortId.setStatus("current")
_CucsSwPortBreakoutSlotId_Type = CucsSwPortBreakoutSlotId
_CucsSwPortBreakoutSlotId_Object = MibTableColumn
cucsSwPortBreakoutSlotId = _CucsSwPortBreakoutSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 87, 1, 6),
    _CucsSwPortBreakoutSlotId_Type()
)
cucsSwPortBreakoutSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwPortBreakoutSlotId.setStatus("current")
_CucsSwVIFRefTable_Object = MibTable
cucsSwVIFRefTable = _CucsSwVIFRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 88)
)
if mibBuilder.loadTexts:
    cucsSwVIFRefTable.setStatus("current")
_CucsSwVIFRefEntry_Object = MibTableRow
cucsSwVIFRefEntry = _CucsSwVIFRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 88, 1)
)
cucsSwVIFRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SW-MIB", "cucsSwVIFRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSwVIFRefEntry.setStatus("current")
_CucsSwVIFRefInstanceId_Type = CucsManagedObjectId
_CucsSwVIFRefInstanceId_Object = MibTableColumn
cucsSwVIFRefInstanceId = _CucsSwVIFRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 88, 1, 1),
    _CucsSwVIFRefInstanceId_Type()
)
cucsSwVIFRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSwVIFRefInstanceId.setStatus("current")
_CucsSwVIFRefDn_Type = CucsManagedObjectDn
_CucsSwVIFRefDn_Object = MibTableColumn
cucsSwVIFRefDn = _CucsSwVIFRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 88, 1, 2),
    _CucsSwVIFRefDn_Type()
)
cucsSwVIFRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVIFRefDn.setStatus("current")
_CucsSwVIFRefRn_Type = SnmpAdminString
_CucsSwVIFRefRn_Object = MibTableColumn
cucsSwVIFRefRn = _CucsSwVIFRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 88, 1, 3),
    _CucsSwVIFRefRn_Type()
)
cucsSwVIFRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVIFRefRn.setStatus("current")
_CucsSwVIFRefId_Type = Gauge32
_CucsSwVIFRefId_Object = MibTableColumn
cucsSwVIFRefId = _CucsSwVIFRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 88, 1, 4),
    _CucsSwVIFRefId_Type()
)
cucsSwVIFRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVIFRefId.setStatus("current")
_CucsSwVIFRefPeerDn_Type = SnmpAdminString
_CucsSwVIFRefPeerDn_Object = MibTableColumn
cucsSwVIFRefPeerDn = _CucsSwVIFRefPeerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 46, 88, 1, 5),
    _CucsSwVIFRefPeerDn_Type()
)
cucsSwVIFRefPeerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSwVIFRefPeerDn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-SW-MIB",
    **{"cucsSwObjects": cucsSwObjects,
       "cucsSwAccessDomainTable": cucsSwAccessDomainTable,
       "cucsSwAccessDomainEntry": cucsSwAccessDomainEntry,
       "cucsSwAccessDomainInstanceId": cucsSwAccessDomainInstanceId,
       "cucsSwAccessDomainDn": cucsSwAccessDomainDn,
       "cucsSwAccessDomainRn": cucsSwAccessDomainRn,
       "cucsSwAccessDomainFsmDescr": cucsSwAccessDomainFsmDescr,
       "cucsSwAccessDomainFsmPrev": cucsSwAccessDomainFsmPrev,
       "cucsSwAccessDomainFsmProgr": cucsSwAccessDomainFsmProgr,
       "cucsSwAccessDomainFsmRmtInvErrCode": cucsSwAccessDomainFsmRmtInvErrCode,
       "cucsSwAccessDomainFsmRmtInvErrDescr": cucsSwAccessDomainFsmRmtInvErrDescr,
       "cucsSwAccessDomainFsmRmtInvRslt": cucsSwAccessDomainFsmRmtInvRslt,
       "cucsSwAccessDomainFsmStageDescr": cucsSwAccessDomainFsmStageDescr,
       "cucsSwAccessDomainFsmStamp": cucsSwAccessDomainFsmStamp,
       "cucsSwAccessDomainFsmStatus": cucsSwAccessDomainFsmStatus,
       "cucsSwAccessDomainFsmTry": cucsSwAccessDomainFsmTry,
       "cucsSwAccessDomainLocale": cucsSwAccessDomainLocale,
       "cucsSwAccessDomainName": cucsSwAccessDomainName,
       "cucsSwAccessDomainSwitchId": cucsSwAccessDomainSwitchId,
       "cucsSwAccessDomainTransport": cucsSwAccessDomainTransport,
       "cucsSwAccessDomainType": cucsSwAccessDomainType,
       "cucsSwAccessDomainFsmTaskTable": cucsSwAccessDomainFsmTaskTable,
       "cucsSwAccessDomainFsmTaskEntry": cucsSwAccessDomainFsmTaskEntry,
       "cucsSwAccessDomainFsmTaskInstanceId": cucsSwAccessDomainFsmTaskInstanceId,
       "cucsSwAccessDomainFsmTaskDn": cucsSwAccessDomainFsmTaskDn,
       "cucsSwAccessDomainFsmTaskRn": cucsSwAccessDomainFsmTaskRn,
       "cucsSwAccessDomainFsmTaskCompletion": cucsSwAccessDomainFsmTaskCompletion,
       "cucsSwAccessDomainFsmTaskFlags": cucsSwAccessDomainFsmTaskFlags,
       "cucsSwAccessDomainFsmTaskItem": cucsSwAccessDomainFsmTaskItem,
       "cucsSwAccessDomainFsmTaskSeqId": cucsSwAccessDomainFsmTaskSeqId,
       "cucsSwAccessEpTable": cucsSwAccessEpTable,
       "cucsSwAccessEpEntry": cucsSwAccessEpEntry,
       "cucsSwAccessEpInstanceId": cucsSwAccessEpInstanceId,
       "cucsSwAccessEpDn": cucsSwAccessEpDn,
       "cucsSwAccessEpRn": cucsSwAccessEpRn,
       "cucsSwAccessEpAdminState": cucsSwAccessEpAdminState,
       "cucsSwAccessEpChassisId": cucsSwAccessEpChassisId,
       "cucsSwAccessEpEpDn": cucsSwAccessEpEpDn,
       "cucsSwAccessEpIfRole": cucsSwAccessEpIfRole,
       "cucsSwAccessEpIfType": cucsSwAccessEpIfType,
       "cucsSwAccessEpLocale": cucsSwAccessEpLocale,
       "cucsSwAccessEpName": cucsSwAccessEpName,
       "cucsSwAccessEpPeerDn": cucsSwAccessEpPeerDn,
       "cucsSwAccessEpPeerPortId": cucsSwAccessEpPeerPortId,
       "cucsSwAccessEpPeerSlotId": cucsSwAccessEpPeerSlotId,
       "cucsSwAccessEpPortId": cucsSwAccessEpPortId,
       "cucsSwAccessEpSlotId": cucsSwAccessEpSlotId,
       "cucsSwAccessEpSwitchId": cucsSwAccessEpSwitchId,
       "cucsSwAccessEpTransport": cucsSwAccessEpTransport,
       "cucsSwAccessEpType": cucsSwAccessEpType,
       "cucsSwAccessEpEncap": cucsSwAccessEpEncap,
       "cucsSwAccessEpNsSize": cucsSwAccessEpNsSize,
       "cucsSwAccessEpPeerChassisId": cucsSwAccessEpPeerChassisId,
       "cucsSwAccessEpLc": cucsSwAccessEpLc,
       "cucsSwAccessEpAggrPortId": cucsSwAccessEpAggrPortId,
       "cucsSwAccessEpPeerAggrPortId": cucsSwAccessEpPeerAggrPortId,
       "cucsSwAccessEpAutoNegotiate": cucsSwAccessEpAutoNegotiate,
       "cucsSwEnvStatsTable": cucsSwEnvStatsTable,
       "cucsSwEnvStatsEntry": cucsSwEnvStatsEntry,
       "cucsSwEnvStatsInstanceId": cucsSwEnvStatsInstanceId,
       "cucsSwEnvStatsDn": cucsSwEnvStatsDn,
       "cucsSwEnvStatsRn": cucsSwEnvStatsRn,
       "cucsSwEnvStatsFanCtrlrInlet1": cucsSwEnvStatsFanCtrlrInlet1,
       "cucsSwEnvStatsFanCtrlrInlet1Avg": cucsSwEnvStatsFanCtrlrInlet1Avg,
       "cucsSwEnvStatsFanCtrlrInlet1Max": cucsSwEnvStatsFanCtrlrInlet1Max,
       "cucsSwEnvStatsFanCtrlrInlet1Min": cucsSwEnvStatsFanCtrlrInlet1Min,
       "cucsSwEnvStatsFanCtrlrInlet2": cucsSwEnvStatsFanCtrlrInlet2,
       "cucsSwEnvStatsFanCtrlrInlet2Avg": cucsSwEnvStatsFanCtrlrInlet2Avg,
       "cucsSwEnvStatsFanCtrlrInlet2Max": cucsSwEnvStatsFanCtrlrInlet2Max,
       "cucsSwEnvStatsFanCtrlrInlet2Min": cucsSwEnvStatsFanCtrlrInlet2Min,
       "cucsSwEnvStatsFanCtrlrInlet3": cucsSwEnvStatsFanCtrlrInlet3,
       "cucsSwEnvStatsFanCtrlrInlet3Avg": cucsSwEnvStatsFanCtrlrInlet3Avg,
       "cucsSwEnvStatsFanCtrlrInlet3Max": cucsSwEnvStatsFanCtrlrInlet3Max,
       "cucsSwEnvStatsFanCtrlrInlet3Min": cucsSwEnvStatsFanCtrlrInlet3Min,
       "cucsSwEnvStatsFanCtrlrInlet4": cucsSwEnvStatsFanCtrlrInlet4,
       "cucsSwEnvStatsFanCtrlrInlet4Avg": cucsSwEnvStatsFanCtrlrInlet4Avg,
       "cucsSwEnvStatsFanCtrlrInlet4Max": cucsSwEnvStatsFanCtrlrInlet4Max,
       "cucsSwEnvStatsFanCtrlrInlet4Min": cucsSwEnvStatsFanCtrlrInlet4Min,
       "cucsSwEnvStatsIntervals": cucsSwEnvStatsIntervals,
       "cucsSwEnvStatsMainBoardOutlet1": cucsSwEnvStatsMainBoardOutlet1,
       "cucsSwEnvStatsMainBoardOutlet1Avg": cucsSwEnvStatsMainBoardOutlet1Avg,
       "cucsSwEnvStatsMainBoardOutlet1Max": cucsSwEnvStatsMainBoardOutlet1Max,
       "cucsSwEnvStatsMainBoardOutlet1Min": cucsSwEnvStatsMainBoardOutlet1Min,
       "cucsSwEnvStatsMainBoardOutlet2": cucsSwEnvStatsMainBoardOutlet2,
       "cucsSwEnvStatsMainBoardOutlet2Avg": cucsSwEnvStatsMainBoardOutlet2Avg,
       "cucsSwEnvStatsMainBoardOutlet2Max": cucsSwEnvStatsMainBoardOutlet2Max,
       "cucsSwEnvStatsMainBoardOutlet2Min": cucsSwEnvStatsMainBoardOutlet2Min,
       "cucsSwEnvStatsPsuCtrlrInlet1": cucsSwEnvStatsPsuCtrlrInlet1,
       "cucsSwEnvStatsPsuCtrlrInlet1Avg": cucsSwEnvStatsPsuCtrlrInlet1Avg,
       "cucsSwEnvStatsPsuCtrlrInlet1Max": cucsSwEnvStatsPsuCtrlrInlet1Max,
       "cucsSwEnvStatsPsuCtrlrInlet1Min": cucsSwEnvStatsPsuCtrlrInlet1Min,
       "cucsSwEnvStatsPsuCtrlrInlet2": cucsSwEnvStatsPsuCtrlrInlet2,
       "cucsSwEnvStatsPsuCtrlrInlet2Avg": cucsSwEnvStatsPsuCtrlrInlet2Avg,
       "cucsSwEnvStatsPsuCtrlrInlet2Max": cucsSwEnvStatsPsuCtrlrInlet2Max,
       "cucsSwEnvStatsPsuCtrlrInlet2Min": cucsSwEnvStatsPsuCtrlrInlet2Min,
       "cucsSwEnvStatsSuspect": cucsSwEnvStatsSuspect,
       "cucsSwEnvStatsThresholded": cucsSwEnvStatsThresholded,
       "cucsSwEnvStatsTimeCollected": cucsSwEnvStatsTimeCollected,
       "cucsSwEnvStatsUpdate": cucsSwEnvStatsUpdate,
       "cucsSwEnvStatsDonner": cucsSwEnvStatsDonner,
       "cucsSwEnvStatsDonnerAvg": cucsSwEnvStatsDonnerAvg,
       "cucsSwEnvStatsDonnerMax": cucsSwEnvStatsDonnerMax,
       "cucsSwEnvStatsDonnerMin": cucsSwEnvStatsDonnerMin,
       "cucsSwEnvStatsTd2": cucsSwEnvStatsTd2,
       "cucsSwEnvStatsTd2Avg": cucsSwEnvStatsTd2Avg,
       "cucsSwEnvStatsTd2Max": cucsSwEnvStatsTd2Max,
       "cucsSwEnvStatsTd2Min": cucsSwEnvStatsTd2Min,
       "cucsSwEnvStatsTiburon": cucsSwEnvStatsTiburon,
       "cucsSwEnvStatsTiburonAvg": cucsSwEnvStatsTiburonAvg,
       "cucsSwEnvStatsTiburonMax": cucsSwEnvStatsTiburonMax,
       "cucsSwEnvStatsTiburonMin": cucsSwEnvStatsTiburonMin,
       "cucsSwEnvStatsHistTable": cucsSwEnvStatsHistTable,
       "cucsSwEnvStatsHistEntry": cucsSwEnvStatsHistEntry,
       "cucsSwEnvStatsHistInstanceId": cucsSwEnvStatsHistInstanceId,
       "cucsSwEnvStatsHistDn": cucsSwEnvStatsHistDn,
       "cucsSwEnvStatsHistRn": cucsSwEnvStatsHistRn,
       "cucsSwEnvStatsHistFanCtrlrInlet1": cucsSwEnvStatsHistFanCtrlrInlet1,
       "cucsSwEnvStatsHistFanCtrlrInlet1Avg": cucsSwEnvStatsHistFanCtrlrInlet1Avg,
       "cucsSwEnvStatsHistFanCtrlrInlet1Max": cucsSwEnvStatsHistFanCtrlrInlet1Max,
       "cucsSwEnvStatsHistFanCtrlrInlet1Min": cucsSwEnvStatsHistFanCtrlrInlet1Min,
       "cucsSwEnvStatsHistFanCtrlrInlet2": cucsSwEnvStatsHistFanCtrlrInlet2,
       "cucsSwEnvStatsHistFanCtrlrInlet2Avg": cucsSwEnvStatsHistFanCtrlrInlet2Avg,
       "cucsSwEnvStatsHistFanCtrlrInlet2Max": cucsSwEnvStatsHistFanCtrlrInlet2Max,
       "cucsSwEnvStatsHistFanCtrlrInlet2Min": cucsSwEnvStatsHistFanCtrlrInlet2Min,
       "cucsSwEnvStatsHistFanCtrlrInlet3": cucsSwEnvStatsHistFanCtrlrInlet3,
       "cucsSwEnvStatsHistFanCtrlrInlet3Avg": cucsSwEnvStatsHistFanCtrlrInlet3Avg,
       "cucsSwEnvStatsHistFanCtrlrInlet3Max": cucsSwEnvStatsHistFanCtrlrInlet3Max,
       "cucsSwEnvStatsHistFanCtrlrInlet3Min": cucsSwEnvStatsHistFanCtrlrInlet3Min,
       "cucsSwEnvStatsHistFanCtrlrInlet4": cucsSwEnvStatsHistFanCtrlrInlet4,
       "cucsSwEnvStatsHistFanCtrlrInlet4Avg": cucsSwEnvStatsHistFanCtrlrInlet4Avg,
       "cucsSwEnvStatsHistFanCtrlrInlet4Max": cucsSwEnvStatsHistFanCtrlrInlet4Max,
       "cucsSwEnvStatsHistFanCtrlrInlet4Min": cucsSwEnvStatsHistFanCtrlrInlet4Min,
       "cucsSwEnvStatsHistId": cucsSwEnvStatsHistId,
       "cucsSwEnvStatsHistMainBoardOutlet1": cucsSwEnvStatsHistMainBoardOutlet1,
       "cucsSwEnvStatsHistMainBoardOutlet1Avg": cucsSwEnvStatsHistMainBoardOutlet1Avg,
       "cucsSwEnvStatsHistMainBoardOutlet1Max": cucsSwEnvStatsHistMainBoardOutlet1Max,
       "cucsSwEnvStatsHistMainBoardOutlet1Min": cucsSwEnvStatsHistMainBoardOutlet1Min,
       "cucsSwEnvStatsHistMainBoardOutlet2": cucsSwEnvStatsHistMainBoardOutlet2,
       "cucsSwEnvStatsHistMainBoardOutlet2Avg": cucsSwEnvStatsHistMainBoardOutlet2Avg,
       "cucsSwEnvStatsHistMainBoardOutlet2Max": cucsSwEnvStatsHistMainBoardOutlet2Max,
       "cucsSwEnvStatsHistMainBoardOutlet2Min": cucsSwEnvStatsHistMainBoardOutlet2Min,
       "cucsSwEnvStatsHistMostRecent": cucsSwEnvStatsHistMostRecent,
       "cucsSwEnvStatsHistPsuCtrlrInlet1": cucsSwEnvStatsHistPsuCtrlrInlet1,
       "cucsSwEnvStatsHistPsuCtrlrInlet1Avg": cucsSwEnvStatsHistPsuCtrlrInlet1Avg,
       "cucsSwEnvStatsHistPsuCtrlrInlet1Max": cucsSwEnvStatsHistPsuCtrlrInlet1Max,
       "cucsSwEnvStatsHistPsuCtrlrInlet1Min": cucsSwEnvStatsHistPsuCtrlrInlet1Min,
       "cucsSwEnvStatsHistPsuCtrlrInlet2": cucsSwEnvStatsHistPsuCtrlrInlet2,
       "cucsSwEnvStatsHistPsuCtrlrInlet2Avg": cucsSwEnvStatsHistPsuCtrlrInlet2Avg,
       "cucsSwEnvStatsHistPsuCtrlrInlet2Max": cucsSwEnvStatsHistPsuCtrlrInlet2Max,
       "cucsSwEnvStatsHistPsuCtrlrInlet2Min": cucsSwEnvStatsHistPsuCtrlrInlet2Min,
       "cucsSwEnvStatsHistSuspect": cucsSwEnvStatsHistSuspect,
       "cucsSwEnvStatsHistThresholded": cucsSwEnvStatsHistThresholded,
       "cucsSwEnvStatsHistTimeCollected": cucsSwEnvStatsHistTimeCollected,
       "cucsSwEnvStatsHistDonner": cucsSwEnvStatsHistDonner,
       "cucsSwEnvStatsHistDonnerAvg": cucsSwEnvStatsHistDonnerAvg,
       "cucsSwEnvStatsHistDonnerMax": cucsSwEnvStatsHistDonnerMax,
       "cucsSwEnvStatsHistDonnerMin": cucsSwEnvStatsHistDonnerMin,
       "cucsSwEnvStatsHistTd2": cucsSwEnvStatsHistTd2,
       "cucsSwEnvStatsHistTd2Avg": cucsSwEnvStatsHistTd2Avg,
       "cucsSwEnvStatsHistTd2Max": cucsSwEnvStatsHistTd2Max,
       "cucsSwEnvStatsHistTd2Min": cucsSwEnvStatsHistTd2Min,
       "cucsSwEnvStatsHistTiburon": cucsSwEnvStatsHistTiburon,
       "cucsSwEnvStatsHistTiburonAvg": cucsSwEnvStatsHistTiburonAvg,
       "cucsSwEnvStatsHistTiburonMax": cucsSwEnvStatsHistTiburonMax,
       "cucsSwEnvStatsHistTiburonMin": cucsSwEnvStatsHistTiburonMin,
       "cucsSwEthEstcEpTable": cucsSwEthEstcEpTable,
       "cucsSwEthEstcEpEntry": cucsSwEthEstcEpEntry,
       "cucsSwEthEstcEpInstanceId": cucsSwEthEstcEpInstanceId,
       "cucsSwEthEstcEpDn": cucsSwEthEstcEpDn,
       "cucsSwEthEstcEpRn": cucsSwEthEstcEpRn,
       "cucsSwEthEstcEpAdminState": cucsSwEthEstcEpAdminState,
       "cucsSwEthEstcEpBorderPortId": cucsSwEthEstcEpBorderPortId,
       "cucsSwEthEstcEpBorderSlotId": cucsSwEthEstcEpBorderSlotId,
       "cucsSwEthEstcEpChassisId": cucsSwEthEstcEpChassisId,
       "cucsSwEthEstcEpCosValue": cucsSwEthEstcEpCosValue,
       "cucsSwEthEstcEpEpDn": cucsSwEthEstcEpEpDn,
       "cucsSwEthEstcEpIfRole": cucsSwEthEstcEpIfRole,
       "cucsSwEthEstcEpIfType": cucsSwEthEstcEpIfType,
       "cucsSwEthEstcEpLocale": cucsSwEthEstcEpLocale,
       "cucsSwEthEstcEpName": cucsSwEthEstcEpName,
       "cucsSwEthEstcEpPeerDn": cucsSwEthEstcEpPeerDn,
       "cucsSwEthEstcEpPeerPortId": cucsSwEthEstcEpPeerPortId,
       "cucsSwEthEstcEpPeerSlotId": cucsSwEthEstcEpPeerSlotId,
       "cucsSwEthEstcEpPinGroupName": cucsSwEthEstcEpPinGroupName,
       "cucsSwEthEstcEpPortId": cucsSwEthEstcEpPortId,
       "cucsSwEthEstcEpPortMode": cucsSwEthEstcEpPortMode,
       "cucsSwEthEstcEpSlotId": cucsSwEthEstcEpSlotId,
       "cucsSwEthEstcEpSwitchId": cucsSwEthEstcEpSwitchId,
       "cucsSwEthEstcEpTransport": cucsSwEthEstcEpTransport,
       "cucsSwEthEstcEpType": cucsSwEthEstcEpType,
       "cucsSwEthEstcEpAdminSpeed": cucsSwEthEstcEpAdminSpeed,
       "cucsSwEthEstcEpPcId": cucsSwEthEstcEpPcId,
       "cucsSwEthEstcEpPeerChassisId": cucsSwEthEstcEpPeerChassisId,
       "cucsSwEthEstcEpCdp": cucsSwEthEstcEpCdp,
       "cucsSwEthEstcEpForgeMac": cucsSwEthEstcEpForgeMac,
       "cucsSwEthEstcEpUplinkFailAction": cucsSwEthEstcEpUplinkFailAction,
       "cucsSwEthEstcEpLc": cucsSwEthEstcEpLc,
       "cucsSwEthEstcEpPriorityFlowCtrl": cucsSwEthEstcEpPriorityFlowCtrl,
       "cucsSwEthEstcEpRecvFlowCtrl": cucsSwEthEstcEpRecvFlowCtrl,
       "cucsSwEthEstcEpSendFlowCtrl": cucsSwEthEstcEpSendFlowCtrl,
       "cucsSwEthEstcEpAggrPortId": cucsSwEthEstcEpAggrPortId,
       "cucsSwEthEstcEpBorderAggrPortId": cucsSwEthEstcEpBorderAggrPortId,
       "cucsSwEthEstcEpPeerAggrPortId": cucsSwEthEstcEpPeerAggrPortId,
       "cucsSwEthEstcEpAutoNegotiate": cucsSwEthEstcEpAutoNegotiate,
       "cucsSwEthLanBorderTable": cucsSwEthLanBorderTable,
       "cucsSwEthLanBorderEntry": cucsSwEthLanBorderEntry,
       "cucsSwEthLanBorderInstanceId": cucsSwEthLanBorderInstanceId,
       "cucsSwEthLanBorderDn": cucsSwEthLanBorderDn,
       "cucsSwEthLanBorderRn": cucsSwEthLanBorderRn,
       "cucsSwEthLanBorderFsmDescr": cucsSwEthLanBorderFsmDescr,
       "cucsSwEthLanBorderFsmPrev": cucsSwEthLanBorderFsmPrev,
       "cucsSwEthLanBorderFsmProgr": cucsSwEthLanBorderFsmProgr,
       "cucsSwEthLanBorderFsmRmtInvErrCode": cucsSwEthLanBorderFsmRmtInvErrCode,
       "cucsSwEthLanBorderFsmRmtInvErrDescr": cucsSwEthLanBorderFsmRmtInvErrDescr,
       "cucsSwEthLanBorderFsmRmtInvRslt": cucsSwEthLanBorderFsmRmtInvRslt,
       "cucsSwEthLanBorderFsmStageDescr": cucsSwEthLanBorderFsmStageDescr,
       "cucsSwEthLanBorderFsmStamp": cucsSwEthLanBorderFsmStamp,
       "cucsSwEthLanBorderFsmStatus": cucsSwEthLanBorderFsmStatus,
       "cucsSwEthLanBorderFsmTry": cucsSwEthLanBorderFsmTry,
       "cucsSwEthLanBorderLocale": cucsSwEthLanBorderLocale,
       "cucsSwEthLanBorderName": cucsSwEthLanBorderName,
       "cucsSwEthLanBorderSwitchId": cucsSwEthLanBorderSwitchId,
       "cucsSwEthLanBorderTransport": cucsSwEthLanBorderTransport,
       "cucsSwEthLanBorderType": cucsSwEthLanBorderType,
       "cucsSwEthLanBorderDeployFlag": cucsSwEthLanBorderDeployFlag,
       "cucsSwEthLanBorderFsmFlags": cucsSwEthLanBorderFsmFlags,
       "cucsSwEthLanBorderUdldMsgInterval": cucsSwEthLanBorderUdldMsgInterval,
       "cucsSwEthLanBorderUdldRecoveryAction": cucsSwEthLanBorderUdldRecoveryAction,
       "cucsSwEthLanBorderLastVlanGrpComputeTime": cucsSwEthLanBorderLastVlanGrpComputeTime,
       "cucsSwEthLanBorderFsmTaskTable": cucsSwEthLanBorderFsmTaskTable,
       "cucsSwEthLanBorderFsmTaskEntry": cucsSwEthLanBorderFsmTaskEntry,
       "cucsSwEthLanBorderFsmTaskInstanceId": cucsSwEthLanBorderFsmTaskInstanceId,
       "cucsSwEthLanBorderFsmTaskDn": cucsSwEthLanBorderFsmTaskDn,
       "cucsSwEthLanBorderFsmTaskRn": cucsSwEthLanBorderFsmTaskRn,
       "cucsSwEthLanBorderFsmTaskCompletion": cucsSwEthLanBorderFsmTaskCompletion,
       "cucsSwEthLanBorderFsmTaskFlags": cucsSwEthLanBorderFsmTaskFlags,
       "cucsSwEthLanBorderFsmTaskItem": cucsSwEthLanBorderFsmTaskItem,
       "cucsSwEthLanBorderFsmTaskSeqId": cucsSwEthLanBorderFsmTaskSeqId,
       "cucsSwEthLanEpTable": cucsSwEthLanEpTable,
       "cucsSwEthLanEpEntry": cucsSwEthLanEpEntry,
       "cucsSwEthLanEpInstanceId": cucsSwEthLanEpInstanceId,
       "cucsSwEthLanEpDn": cucsSwEthLanEpDn,
       "cucsSwEthLanEpRn": cucsSwEthLanEpRn,
       "cucsSwEthLanEpAdminSpeed": cucsSwEthLanEpAdminSpeed,
       "cucsSwEthLanEpAdminState": cucsSwEthLanEpAdminState,
       "cucsSwEthLanEpChassisId": cucsSwEthLanEpChassisId,
       "cucsSwEthLanEpEpDn": cucsSwEthLanEpEpDn,
       "cucsSwEthLanEpIfRole": cucsSwEthLanEpIfRole,
       "cucsSwEthLanEpIfType": cucsSwEthLanEpIfType,
       "cucsSwEthLanEpLocale": cucsSwEthLanEpLocale,
       "cucsSwEthLanEpName": cucsSwEthLanEpName,
       "cucsSwEthLanEpPcId": cucsSwEthLanEpPcId,
       "cucsSwEthLanEpPeerDn": cucsSwEthLanEpPeerDn,
       "cucsSwEthLanEpPeerPortId": cucsSwEthLanEpPeerPortId,
       "cucsSwEthLanEpPeerSlotId": cucsSwEthLanEpPeerSlotId,
       "cucsSwEthLanEpPortId": cucsSwEthLanEpPortId,
       "cucsSwEthLanEpPriorityFlowCtrl": cucsSwEthLanEpPriorityFlowCtrl,
       "cucsSwEthLanEpRecvFlowCtrl": cucsSwEthLanEpRecvFlowCtrl,
       "cucsSwEthLanEpSendFlowCtrl": cucsSwEthLanEpSendFlowCtrl,
       "cucsSwEthLanEpSlotId": cucsSwEthLanEpSlotId,
       "cucsSwEthLanEpSwitchId": cucsSwEthLanEpSwitchId,
       "cucsSwEthLanEpTransport": cucsSwEthLanEpTransport,
       "cucsSwEthLanEpType": cucsSwEthLanEpType,
       "cucsSwEthLanEpPeerChassisId": cucsSwEthLanEpPeerChassisId,
       "cucsSwEthLanEpLc": cucsSwEthLanEpLc,
       "cucsSwEthLanEpUdldAdminState": cucsSwEthLanEpUdldAdminState,
       "cucsSwEthLanEpUdldMode": cucsSwEthLanEpUdldMode,
       "cucsSwEthLanEpAggrPortId": cucsSwEthLanEpAggrPortId,
       "cucsSwEthLanEpPeerAggrPortId": cucsSwEthLanEpPeerAggrPortId,
       "cucsSwEthLanEpAutoNegotiate": cucsSwEthLanEpAutoNegotiate,
       "cucsSwEthLanMonTable": cucsSwEthLanMonTable,
       "cucsSwEthLanMonEntry": cucsSwEthLanMonEntry,
       "cucsSwEthLanMonInstanceId": cucsSwEthLanMonInstanceId,
       "cucsSwEthLanMonDn": cucsSwEthLanMonDn,
       "cucsSwEthLanMonRn": cucsSwEthLanMonRn,
       "cucsSwEthLanMonLocale": cucsSwEthLanMonLocale,
       "cucsSwEthLanMonName": cucsSwEthLanMonName,
       "cucsSwEthLanMonSwitchId": cucsSwEthLanMonSwitchId,
       "cucsSwEthLanMonTransport": cucsSwEthLanMonTransport,
       "cucsSwEthLanMonType": cucsSwEthLanMonType,
       "cucsSwEthLanPcTable": cucsSwEthLanPcTable,
       "cucsSwEthLanPcEntry": cucsSwEthLanPcEntry,
       "cucsSwEthLanPcInstanceId": cucsSwEthLanPcInstanceId,
       "cucsSwEthLanPcDn": cucsSwEthLanPcDn,
       "cucsSwEthLanPcRn": cucsSwEthLanPcRn,
       "cucsSwEthLanPcAdminSpeed": cucsSwEthLanPcAdminSpeed,
       "cucsSwEthLanPcAdminState": cucsSwEthLanPcAdminState,
       "cucsSwEthLanPcEpDn": cucsSwEthLanPcEpDn,
       "cucsSwEthLanPcIfRole": cucsSwEthLanPcIfRole,
       "cucsSwEthLanPcIfType": cucsSwEthLanPcIfType,
       "cucsSwEthLanPcLocale": cucsSwEthLanPcLocale,
       "cucsSwEthLanPcName": cucsSwEthLanPcName,
       "cucsSwEthLanPcPeerDn": cucsSwEthLanPcPeerDn,
       "cucsSwEthLanPcPortId": cucsSwEthLanPcPortId,
       "cucsSwEthLanPcPriorityFlowCtrl": cucsSwEthLanPcPriorityFlowCtrl,
       "cucsSwEthLanPcRecvFlowCtrl": cucsSwEthLanPcRecvFlowCtrl,
       "cucsSwEthLanPcSendFlowCtrl": cucsSwEthLanPcSendFlowCtrl,
       "cucsSwEthLanPcSwitchId": cucsSwEthLanPcSwitchId,
       "cucsSwEthLanPcTransport": cucsSwEthLanPcTransport,
       "cucsSwEthLanPcType": cucsSwEthLanPcType,
       "cucsSwEthLanPcMonTrafDir": cucsSwEthLanPcMonTrafDir,
       "cucsSwEthLanPcLacpFastTimer": cucsSwEthLanPcLacpFastTimer,
       "cucsSwEthLanPcLacpSuspendIndividual": cucsSwEthLanPcLacpSuspendIndividual,
       "cucsSwEthLanPcAutoNegotiate": cucsSwEthLanPcAutoNegotiate,
       "cucsSwEthMonTable": cucsSwEthMonTable,
       "cucsSwEthMonEntry": cucsSwEthMonEntry,
       "cucsSwEthMonInstanceId": cucsSwEthMonInstanceId,
       "cucsSwEthMonDn": cucsSwEthMonDn,
       "cucsSwEthMonRn": cucsSwEthMonRn,
       "cucsSwEthMonAdminState": cucsSwEthMonAdminState,
       "cucsSwEthMonFsmDescr": cucsSwEthMonFsmDescr,
       "cucsSwEthMonFsmPrev": cucsSwEthMonFsmPrev,
       "cucsSwEthMonFsmProgr": cucsSwEthMonFsmProgr,
       "cucsSwEthMonFsmRmtInvErrCode": cucsSwEthMonFsmRmtInvErrCode,
       "cucsSwEthMonFsmRmtInvErrDescr": cucsSwEthMonFsmRmtInvErrDescr,
       "cucsSwEthMonFsmRmtInvRslt": cucsSwEthMonFsmRmtInvRslt,
       "cucsSwEthMonFsmStageDescr": cucsSwEthMonFsmStageDescr,
       "cucsSwEthMonFsmStamp": cucsSwEthMonFsmStamp,
       "cucsSwEthMonFsmStatus": cucsSwEthMonFsmStatus,
       "cucsSwEthMonFsmTry": cucsSwEthMonFsmTry,
       "cucsSwEthMonLifeCycle": cucsSwEthMonLifeCycle,
       "cucsSwEthMonName": cucsSwEthMonName,
       "cucsSwEthMonSession": cucsSwEthMonSession,
       "cucsSwEthMonSwitchId": cucsSwEthMonSwitchId,
       "cucsSwEthMonTransport": cucsSwEthMonTransport,
       "cucsSwEthMonType": cucsSwEthMonType,
       "cucsSwEthMonHasLastDest": cucsSwEthMonHasLastDest,
       "cucsSwEthMonPeerDn": cucsSwEthMonPeerDn,
       "cucsSwEthMonDestEpTable": cucsSwEthMonDestEpTable,
       "cucsSwEthMonDestEpEntry": cucsSwEthMonDestEpEntry,
       "cucsSwEthMonDestEpInstanceId": cucsSwEthMonDestEpInstanceId,
       "cucsSwEthMonDestEpDn": cucsSwEthMonDestEpDn,
       "cucsSwEthMonDestEpRn": cucsSwEthMonDestEpRn,
       "cucsSwEthMonDestEpAdminState": cucsSwEthMonDestEpAdminState,
       "cucsSwEthMonDestEpChassisId": cucsSwEthMonDestEpChassisId,
       "cucsSwEthMonDestEpEpDn": cucsSwEthMonDestEpEpDn,
       "cucsSwEthMonDestEpIfRole": cucsSwEthMonDestEpIfRole,
       "cucsSwEthMonDestEpIfType": cucsSwEthMonDestEpIfType,
       "cucsSwEthMonDestEpLocale": cucsSwEthMonDestEpLocale,
       "cucsSwEthMonDestEpName": cucsSwEthMonDestEpName,
       "cucsSwEthMonDestEpPeerDn": cucsSwEthMonDestEpPeerDn,
       "cucsSwEthMonDestEpPeerPortId": cucsSwEthMonDestEpPeerPortId,
       "cucsSwEthMonDestEpPeerSlotId": cucsSwEthMonDestEpPeerSlotId,
       "cucsSwEthMonDestEpPortId": cucsSwEthMonDestEpPortId,
       "cucsSwEthMonDestEpSlotId": cucsSwEthMonDestEpSlotId,
       "cucsSwEthMonDestEpSwitchId": cucsSwEthMonDestEpSwitchId,
       "cucsSwEthMonDestEpTransport": cucsSwEthMonDestEpTransport,
       "cucsSwEthMonDestEpType": cucsSwEthMonDestEpType,
       "cucsSwEthMonDestEpPeerChassisId": cucsSwEthMonDestEpPeerChassisId,
       "cucsSwEthMonDestEpLc": cucsSwEthMonDestEpLc,
       "cucsSwEthMonDestEpAdminSpeed": cucsSwEthMonDestEpAdminSpeed,
       "cucsSwEthMonDestEpAggrPortId": cucsSwEthMonDestEpAggrPortId,
       "cucsSwEthMonDestEpPeerAggrPortId": cucsSwEthMonDestEpPeerAggrPortId,
       "cucsSwEthMonDestEpAutoNegotiate": cucsSwEthMonDestEpAutoNegotiate,
       "cucsSwEthMonFsmTaskTable": cucsSwEthMonFsmTaskTable,
       "cucsSwEthMonFsmTaskEntry": cucsSwEthMonFsmTaskEntry,
       "cucsSwEthMonFsmTaskInstanceId": cucsSwEthMonFsmTaskInstanceId,
       "cucsSwEthMonFsmTaskDn": cucsSwEthMonFsmTaskDn,
       "cucsSwEthMonFsmTaskRn": cucsSwEthMonFsmTaskRn,
       "cucsSwEthMonFsmTaskCompletion": cucsSwEthMonFsmTaskCompletion,
       "cucsSwEthMonFsmTaskFlags": cucsSwEthMonFsmTaskFlags,
       "cucsSwEthMonFsmTaskItem": cucsSwEthMonFsmTaskItem,
       "cucsSwEthMonFsmTaskSeqId": cucsSwEthMonFsmTaskSeqId,
       "cucsSwEthMonSrcEpTable": cucsSwEthMonSrcEpTable,
       "cucsSwEthMonSrcEpEntry": cucsSwEthMonSrcEpEntry,
       "cucsSwEthMonSrcEpInstanceId": cucsSwEthMonSrcEpInstanceId,
       "cucsSwEthMonSrcEpDn": cucsSwEthMonSrcEpDn,
       "cucsSwEthMonSrcEpRn": cucsSwEthMonSrcEpRn,
       "cucsSwEthMonSrcEpAdminState": cucsSwEthMonSrcEpAdminState,
       "cucsSwEthMonSrcEpChassisId": cucsSwEthMonSrcEpChassisId,
       "cucsSwEthMonSrcEpEpDn": cucsSwEthMonSrcEpEpDn,
       "cucsSwEthMonSrcEpIfRole": cucsSwEthMonSrcEpIfRole,
       "cucsSwEthMonSrcEpIfType": cucsSwEthMonSrcEpIfType,
       "cucsSwEthMonSrcEpLocale": cucsSwEthMonSrcEpLocale,
       "cucsSwEthMonSrcEpMonTrafDir": cucsSwEthMonSrcEpMonTrafDir,
       "cucsSwEthMonSrcEpName": cucsSwEthMonSrcEpName,
       "cucsSwEthMonSrcEpPeerDn": cucsSwEthMonSrcEpPeerDn,
       "cucsSwEthMonSrcEpPeerPortId": cucsSwEthMonSrcEpPeerPortId,
       "cucsSwEthMonSrcEpPeerSlotId": cucsSwEthMonSrcEpPeerSlotId,
       "cucsSwEthMonSrcEpPortId": cucsSwEthMonSrcEpPortId,
       "cucsSwEthMonSrcEpSlotId": cucsSwEthMonSrcEpSlotId,
       "cucsSwEthMonSrcEpSwitchId": cucsSwEthMonSrcEpSwitchId,
       "cucsSwEthMonSrcEpTransport": cucsSwEthMonSrcEpTransport,
       "cucsSwEthMonSrcEpType": cucsSwEthMonSrcEpType,
       "cucsSwEthMonSrcEpPeerChassisId": cucsSwEthMonSrcEpPeerChassisId,
       "cucsSwEthMonSrcEpLc": cucsSwEthMonSrcEpLc,
       "cucsSwEthMonSrcEpAggrPortId": cucsSwEthMonSrcEpAggrPortId,
       "cucsSwEthMonSrcEpPeerAggrPortId": cucsSwEthMonSrcEpPeerAggrPortId,
       "cucsSwEthMonSrcEpAutoNegotiate": cucsSwEthMonSrcEpAutoNegotiate,
       "cucsSwEthTargetEpTable": cucsSwEthTargetEpTable,
       "cucsSwEthTargetEpEntry": cucsSwEthTargetEpEntry,
       "cucsSwEthTargetEpInstanceId": cucsSwEthTargetEpInstanceId,
       "cucsSwEthTargetEpDn": cucsSwEthTargetEpDn,
       "cucsSwEthTargetEpRn": cucsSwEthTargetEpRn,
       "cucsSwEthTargetEpAdminState": cucsSwEthTargetEpAdminState,
       "cucsSwEthTargetEpChassisId": cucsSwEthTargetEpChassisId,
       "cucsSwEthTargetEpEpDn": cucsSwEthTargetEpEpDn,
       "cucsSwEthTargetEpIfRole": cucsSwEthTargetEpIfRole,
       "cucsSwEthTargetEpIfType": cucsSwEthTargetEpIfType,
       "cucsSwEthTargetEpLicGP": cucsSwEthTargetEpLicGP,
       "cucsSwEthTargetEpLicState": cucsSwEthTargetEpLicState,
       "cucsSwEthTargetEpLocale": cucsSwEthTargetEpLocale,
       "cucsSwEthTargetEpMacAddress": cucsSwEthTargetEpMacAddress,
       "cucsSwEthTargetEpName": cucsSwEthTargetEpName,
       "cucsSwEthTargetEpPeerDn": cucsSwEthTargetEpPeerDn,
       "cucsSwEthTargetEpPeerPortId": cucsSwEthTargetEpPeerPortId,
       "cucsSwEthTargetEpPeerSlotId": cucsSwEthTargetEpPeerSlotId,
       "cucsSwEthTargetEpPortId": cucsSwEthTargetEpPortId,
       "cucsSwEthTargetEpSlotId": cucsSwEthTargetEpSlotId,
       "cucsSwEthTargetEpSwitchId": cucsSwEthTargetEpSwitchId,
       "cucsSwEthTargetEpTransport": cucsSwEthTargetEpTransport,
       "cucsSwEthTargetEpType": cucsSwEthTargetEpType,
       "cucsSwEthTargetEpPeerChassisId": cucsSwEthTargetEpPeerChassisId,
       "cucsSwEthTargetEpFltAggr": cucsSwEthTargetEpFltAggr,
       "cucsSwEthTargetEpOperState": cucsSwEthTargetEpOperState,
       "cucsSwEthTargetEpOperStateReason": cucsSwEthTargetEpOperStateReason,
       "cucsSwEthTargetEpWarnings": cucsSwEthTargetEpWarnings,
       "cucsSwEthTargetEpAggrPortId": cucsSwEthTargetEpAggrPortId,
       "cucsSwEthTargetEpPeerAggrPortId": cucsSwEthTargetEpPeerAggrPortId,
       "cucsSwEthTargetEpAutoNegotiate": cucsSwEthTargetEpAutoNegotiate,
       "cucsSwFcEstcEpTable": cucsSwFcEstcEpTable,
       "cucsSwFcEstcEpEntry": cucsSwFcEstcEpEntry,
       "cucsSwFcEstcEpInstanceId": cucsSwFcEstcEpInstanceId,
       "cucsSwFcEstcEpDn": cucsSwFcEstcEpDn,
       "cucsSwFcEstcEpRn": cucsSwFcEstcEpRn,
       "cucsSwFcEstcEpAdminState": cucsSwFcEstcEpAdminState,
       "cucsSwFcEstcEpChassisId": cucsSwFcEstcEpChassisId,
       "cucsSwFcEstcEpEpDn": cucsSwFcEstcEpEpDn,
       "cucsSwFcEstcEpIfRole": cucsSwFcEstcEpIfRole,
       "cucsSwFcEstcEpIfType": cucsSwFcEstcEpIfType,
       "cucsSwFcEstcEpLocale": cucsSwFcEstcEpLocale,
       "cucsSwFcEstcEpName": cucsSwFcEstcEpName,
       "cucsSwFcEstcEpPeerDn": cucsSwFcEstcEpPeerDn,
       "cucsSwFcEstcEpPeerPortId": cucsSwFcEstcEpPeerPortId,
       "cucsSwFcEstcEpPeerSlotId": cucsSwFcEstcEpPeerSlotId,
       "cucsSwFcEstcEpPortId": cucsSwFcEstcEpPortId,
       "cucsSwFcEstcEpPortVsanId": cucsSwFcEstcEpPortVsanId,
       "cucsSwFcEstcEpSlotId": cucsSwFcEstcEpSlotId,
       "cucsSwFcEstcEpSwitchId": cucsSwFcEstcEpSwitchId,
       "cucsSwFcEstcEpTransport": cucsSwFcEstcEpTransport,
       "cucsSwFcEstcEpType": cucsSwFcEstcEpType,
       "cucsSwFcEstcEpPeerChassisId": cucsSwFcEstcEpPeerChassisId,
       "cucsSwFcEstcEpLc": cucsSwFcEstcEpLc,
       "cucsSwFcEstcEpFillPattern": cucsSwFcEstcEpFillPattern,
       "cucsSwFcEstcEpAggrPortId": cucsSwFcEstcEpAggrPortId,
       "cucsSwFcEstcEpPeerAggrPortId": cucsSwFcEstcEpPeerAggrPortId,
       "cucsSwFcEstcEpAutoNegotiate": cucsSwFcEstcEpAutoNegotiate,
       "cucsSwFcMonTable": cucsSwFcMonTable,
       "cucsSwFcMonEntry": cucsSwFcMonEntry,
       "cucsSwFcMonInstanceId": cucsSwFcMonInstanceId,
       "cucsSwFcMonDn": cucsSwFcMonDn,
       "cucsSwFcMonRn": cucsSwFcMonRn,
       "cucsSwFcMonAdminState": cucsSwFcMonAdminState,
       "cucsSwFcMonFsmDescr": cucsSwFcMonFsmDescr,
       "cucsSwFcMonFsmPrev": cucsSwFcMonFsmPrev,
       "cucsSwFcMonFsmProgr": cucsSwFcMonFsmProgr,
       "cucsSwFcMonFsmRmtInvErrCode": cucsSwFcMonFsmRmtInvErrCode,
       "cucsSwFcMonFsmRmtInvErrDescr": cucsSwFcMonFsmRmtInvErrDescr,
       "cucsSwFcMonFsmRmtInvRslt": cucsSwFcMonFsmRmtInvRslt,
       "cucsSwFcMonFsmStageDescr": cucsSwFcMonFsmStageDescr,
       "cucsSwFcMonFsmStamp": cucsSwFcMonFsmStamp,
       "cucsSwFcMonFsmStatus": cucsSwFcMonFsmStatus,
       "cucsSwFcMonFsmTry": cucsSwFcMonFsmTry,
       "cucsSwFcMonLifeCycle": cucsSwFcMonLifeCycle,
       "cucsSwFcMonName": cucsSwFcMonName,
       "cucsSwFcMonSession": cucsSwFcMonSession,
       "cucsSwFcMonSwitchId": cucsSwFcMonSwitchId,
       "cucsSwFcMonTransport": cucsSwFcMonTransport,
       "cucsSwFcMonType": cucsSwFcMonType,
       "cucsSwFcMonHasLastDest": cucsSwFcMonHasLastDest,
       "cucsSwFcMonPeerDn": cucsSwFcMonPeerDn,
       "cucsSwFcMonDestEpTable": cucsSwFcMonDestEpTable,
       "cucsSwFcMonDestEpEntry": cucsSwFcMonDestEpEntry,
       "cucsSwFcMonDestEpInstanceId": cucsSwFcMonDestEpInstanceId,
       "cucsSwFcMonDestEpDn": cucsSwFcMonDestEpDn,
       "cucsSwFcMonDestEpRn": cucsSwFcMonDestEpRn,
       "cucsSwFcMonDestEpAdminState": cucsSwFcMonDestEpAdminState,
       "cucsSwFcMonDestEpChassisId": cucsSwFcMonDestEpChassisId,
       "cucsSwFcMonDestEpEpDn": cucsSwFcMonDestEpEpDn,
       "cucsSwFcMonDestEpIfRole": cucsSwFcMonDestEpIfRole,
       "cucsSwFcMonDestEpIfType": cucsSwFcMonDestEpIfType,
       "cucsSwFcMonDestEpLocale": cucsSwFcMonDestEpLocale,
       "cucsSwFcMonDestEpName": cucsSwFcMonDestEpName,
       "cucsSwFcMonDestEpPeerDn": cucsSwFcMonDestEpPeerDn,
       "cucsSwFcMonDestEpPeerPortId": cucsSwFcMonDestEpPeerPortId,
       "cucsSwFcMonDestEpPeerSlotId": cucsSwFcMonDestEpPeerSlotId,
       "cucsSwFcMonDestEpPortId": cucsSwFcMonDestEpPortId,
       "cucsSwFcMonDestEpSlotId": cucsSwFcMonDestEpSlotId,
       "cucsSwFcMonDestEpSwitchId": cucsSwFcMonDestEpSwitchId,
       "cucsSwFcMonDestEpTransport": cucsSwFcMonDestEpTransport,
       "cucsSwFcMonDestEpType": cucsSwFcMonDestEpType,
       "cucsSwFcMonDestEpPeerChassisId": cucsSwFcMonDestEpPeerChassisId,
       "cucsSwFcMonDestEpLc": cucsSwFcMonDestEpLc,
       "cucsSwFcMonDestEpAdminSpeed": cucsSwFcMonDestEpAdminSpeed,
       "cucsSwFcMonDestEpAggrPortId": cucsSwFcMonDestEpAggrPortId,
       "cucsSwFcMonDestEpPeerAggrPortId": cucsSwFcMonDestEpPeerAggrPortId,
       "cucsSwFcMonDestEpAutoNegotiate": cucsSwFcMonDestEpAutoNegotiate,
       "cucsSwFcMonFsmTaskTable": cucsSwFcMonFsmTaskTable,
       "cucsSwFcMonFsmTaskEntry": cucsSwFcMonFsmTaskEntry,
       "cucsSwFcMonFsmTaskInstanceId": cucsSwFcMonFsmTaskInstanceId,
       "cucsSwFcMonFsmTaskDn": cucsSwFcMonFsmTaskDn,
       "cucsSwFcMonFsmTaskRn": cucsSwFcMonFsmTaskRn,
       "cucsSwFcMonFsmTaskCompletion": cucsSwFcMonFsmTaskCompletion,
       "cucsSwFcMonFsmTaskFlags": cucsSwFcMonFsmTaskFlags,
       "cucsSwFcMonFsmTaskItem": cucsSwFcMonFsmTaskItem,
       "cucsSwFcMonFsmTaskSeqId": cucsSwFcMonFsmTaskSeqId,
       "cucsSwFcMonSrcEpTable": cucsSwFcMonSrcEpTable,
       "cucsSwFcMonSrcEpEntry": cucsSwFcMonSrcEpEntry,
       "cucsSwFcMonSrcEpInstanceId": cucsSwFcMonSrcEpInstanceId,
       "cucsSwFcMonSrcEpDn": cucsSwFcMonSrcEpDn,
       "cucsSwFcMonSrcEpRn": cucsSwFcMonSrcEpRn,
       "cucsSwFcMonSrcEpAdminState": cucsSwFcMonSrcEpAdminState,
       "cucsSwFcMonSrcEpChassisId": cucsSwFcMonSrcEpChassisId,
       "cucsSwFcMonSrcEpEpDn": cucsSwFcMonSrcEpEpDn,
       "cucsSwFcMonSrcEpIfRole": cucsSwFcMonSrcEpIfRole,
       "cucsSwFcMonSrcEpIfType": cucsSwFcMonSrcEpIfType,
       "cucsSwFcMonSrcEpLocale": cucsSwFcMonSrcEpLocale,
       "cucsSwFcMonSrcEpMonTrafDir": cucsSwFcMonSrcEpMonTrafDir,
       "cucsSwFcMonSrcEpName": cucsSwFcMonSrcEpName,
       "cucsSwFcMonSrcEpPeerDn": cucsSwFcMonSrcEpPeerDn,
       "cucsSwFcMonSrcEpPeerPortId": cucsSwFcMonSrcEpPeerPortId,
       "cucsSwFcMonSrcEpPeerSlotId": cucsSwFcMonSrcEpPeerSlotId,
       "cucsSwFcMonSrcEpPortId": cucsSwFcMonSrcEpPortId,
       "cucsSwFcMonSrcEpSlotId": cucsSwFcMonSrcEpSlotId,
       "cucsSwFcMonSrcEpSwitchId": cucsSwFcMonSrcEpSwitchId,
       "cucsSwFcMonSrcEpTransport": cucsSwFcMonSrcEpTransport,
       "cucsSwFcMonSrcEpType": cucsSwFcMonSrcEpType,
       "cucsSwFcMonSrcEpPeerChassisId": cucsSwFcMonSrcEpPeerChassisId,
       "cucsSwFcMonSrcEpLc": cucsSwFcMonSrcEpLc,
       "cucsSwFcMonSrcEpAggrPortId": cucsSwFcMonSrcEpAggrPortId,
       "cucsSwFcMonSrcEpPeerAggrPortId": cucsSwFcMonSrcEpPeerAggrPortId,
       "cucsSwFcMonSrcEpAutoNegotiate": cucsSwFcMonSrcEpAutoNegotiate,
       "cucsSwFcSanBorderTable": cucsSwFcSanBorderTable,
       "cucsSwFcSanBorderEntry": cucsSwFcSanBorderEntry,
       "cucsSwFcSanBorderInstanceId": cucsSwFcSanBorderInstanceId,
       "cucsSwFcSanBorderDn": cucsSwFcSanBorderDn,
       "cucsSwFcSanBorderRn": cucsSwFcSanBorderRn,
       "cucsSwFcSanBorderFsmDescr": cucsSwFcSanBorderFsmDescr,
       "cucsSwFcSanBorderFsmPrev": cucsSwFcSanBorderFsmPrev,
       "cucsSwFcSanBorderFsmProgr": cucsSwFcSanBorderFsmProgr,
       "cucsSwFcSanBorderFsmRmtInvErrCode": cucsSwFcSanBorderFsmRmtInvErrCode,
       "cucsSwFcSanBorderFsmRmtInvErrDescr": cucsSwFcSanBorderFsmRmtInvErrDescr,
       "cucsSwFcSanBorderFsmRmtInvRslt": cucsSwFcSanBorderFsmRmtInvRslt,
       "cucsSwFcSanBorderFsmStageDescr": cucsSwFcSanBorderFsmStageDescr,
       "cucsSwFcSanBorderFsmStamp": cucsSwFcSanBorderFsmStamp,
       "cucsSwFcSanBorderFsmStatus": cucsSwFcSanBorderFsmStatus,
       "cucsSwFcSanBorderFsmTry": cucsSwFcSanBorderFsmTry,
       "cucsSwFcSanBorderLocale": cucsSwFcSanBorderLocale,
       "cucsSwFcSanBorderName": cucsSwFcSanBorderName,
       "cucsSwFcSanBorderSwitchId": cucsSwFcSanBorderSwitchId,
       "cucsSwFcSanBorderTransport": cucsSwFcSanBorderTransport,
       "cucsSwFcSanBorderType": cucsSwFcSanBorderType,
       "cucsSwFcSanBorderUplinkTrunking": cucsSwFcSanBorderUplinkTrunking,
       "cucsSwFcSanBorderFsmTaskTable": cucsSwFcSanBorderFsmTaskTable,
       "cucsSwFcSanBorderFsmTaskEntry": cucsSwFcSanBorderFsmTaskEntry,
       "cucsSwFcSanBorderFsmTaskInstanceId": cucsSwFcSanBorderFsmTaskInstanceId,
       "cucsSwFcSanBorderFsmTaskDn": cucsSwFcSanBorderFsmTaskDn,
       "cucsSwFcSanBorderFsmTaskRn": cucsSwFcSanBorderFsmTaskRn,
       "cucsSwFcSanBorderFsmTaskCompletion": cucsSwFcSanBorderFsmTaskCompletion,
       "cucsSwFcSanBorderFsmTaskFlags": cucsSwFcSanBorderFsmTaskFlags,
       "cucsSwFcSanBorderFsmTaskItem": cucsSwFcSanBorderFsmTaskItem,
       "cucsSwFcSanBorderFsmTaskSeqId": cucsSwFcSanBorderFsmTaskSeqId,
       "cucsSwFcSanEpTable": cucsSwFcSanEpTable,
       "cucsSwFcSanEpEntry": cucsSwFcSanEpEntry,
       "cucsSwFcSanEpInstanceId": cucsSwFcSanEpInstanceId,
       "cucsSwFcSanEpDn": cucsSwFcSanEpDn,
       "cucsSwFcSanEpRn": cucsSwFcSanEpRn,
       "cucsSwFcSanEpAdminState": cucsSwFcSanEpAdminState,
       "cucsSwFcSanEpChassisId": cucsSwFcSanEpChassisId,
       "cucsSwFcSanEpEpDn": cucsSwFcSanEpEpDn,
       "cucsSwFcSanEpIfRole": cucsSwFcSanEpIfRole,
       "cucsSwFcSanEpIfType": cucsSwFcSanEpIfType,
       "cucsSwFcSanEpLocale": cucsSwFcSanEpLocale,
       "cucsSwFcSanEpName": cucsSwFcSanEpName,
       "cucsSwFcSanEpPcId": cucsSwFcSanEpPcId,
       "cucsSwFcSanEpPeerDn": cucsSwFcSanEpPeerDn,
       "cucsSwFcSanEpPeerPortId": cucsSwFcSanEpPeerPortId,
       "cucsSwFcSanEpPeerSlotId": cucsSwFcSanEpPeerSlotId,
       "cucsSwFcSanEpPortId": cucsSwFcSanEpPortId,
       "cucsSwFcSanEpPortVsanId": cucsSwFcSanEpPortVsanId,
       "cucsSwFcSanEpSlotId": cucsSwFcSanEpSlotId,
       "cucsSwFcSanEpSwitchId": cucsSwFcSanEpSwitchId,
       "cucsSwFcSanEpTransport": cucsSwFcSanEpTransport,
       "cucsSwFcSanEpType": cucsSwFcSanEpType,
       "cucsSwFcSanEpAdminSpeed": cucsSwFcSanEpAdminSpeed,
       "cucsSwFcSanEpPeerChassisId": cucsSwFcSanEpPeerChassisId,
       "cucsSwFcSanEpLc": cucsSwFcSanEpLc,
       "cucsSwFcSanEpFillPattern": cucsSwFcSanEpFillPattern,
       "cucsSwFcSanEpAggrPortId": cucsSwFcSanEpAggrPortId,
       "cucsSwFcSanEpPeerAggrPortId": cucsSwFcSanEpPeerAggrPortId,
       "cucsSwFcSanEpAutoNegotiate": cucsSwFcSanEpAutoNegotiate,
       "cucsSwFcSanMonTable": cucsSwFcSanMonTable,
       "cucsSwFcSanMonEntry": cucsSwFcSanMonEntry,
       "cucsSwFcSanMonInstanceId": cucsSwFcSanMonInstanceId,
       "cucsSwFcSanMonDn": cucsSwFcSanMonDn,
       "cucsSwFcSanMonRn": cucsSwFcSanMonRn,
       "cucsSwFcSanMonLocale": cucsSwFcSanMonLocale,
       "cucsSwFcSanMonName": cucsSwFcSanMonName,
       "cucsSwFcSanMonSwitchId": cucsSwFcSanMonSwitchId,
       "cucsSwFcSanMonTransport": cucsSwFcSanMonTransport,
       "cucsSwFcSanMonType": cucsSwFcSanMonType,
       "cucsSwFcSanPcTable": cucsSwFcSanPcTable,
       "cucsSwFcSanPcEntry": cucsSwFcSanPcEntry,
       "cucsSwFcSanPcInstanceId": cucsSwFcSanPcInstanceId,
       "cucsSwFcSanPcDn": cucsSwFcSanPcDn,
       "cucsSwFcSanPcRn": cucsSwFcSanPcRn,
       "cucsSwFcSanPcAdminState": cucsSwFcSanPcAdminState,
       "cucsSwFcSanPcEpDn": cucsSwFcSanPcEpDn,
       "cucsSwFcSanPcIfRole": cucsSwFcSanPcIfRole,
       "cucsSwFcSanPcIfType": cucsSwFcSanPcIfType,
       "cucsSwFcSanPcLocale": cucsSwFcSanPcLocale,
       "cucsSwFcSanPcName": cucsSwFcSanPcName,
       "cucsSwFcSanPcPcId": cucsSwFcSanPcPcId,
       "cucsSwFcSanPcPeerDn": cucsSwFcSanPcPeerDn,
       "cucsSwFcSanPcPortId": cucsSwFcSanPcPortId,
       "cucsSwFcSanPcPortVsanId": cucsSwFcSanPcPortVsanId,
       "cucsSwFcSanPcSwitchId": cucsSwFcSanPcSwitchId,
       "cucsSwFcSanPcTransport": cucsSwFcSanPcTransport,
       "cucsSwFcSanPcType": cucsSwFcSanPcType,
       "cucsSwFcSanPcMonTrafDir": cucsSwFcSanPcMonTrafDir,
       "cucsSwFcSanPcAdminSpeed": cucsSwFcSanPcAdminSpeed,
       "cucsSwFcoeEstcEpTable": cucsSwFcoeEstcEpTable,
       "cucsSwFcoeEstcEpEntry": cucsSwFcoeEstcEpEntry,
       "cucsSwFcoeEstcEpInstanceId": cucsSwFcoeEstcEpInstanceId,
       "cucsSwFcoeEstcEpDn": cucsSwFcoeEstcEpDn,
       "cucsSwFcoeEstcEpRn": cucsSwFcoeEstcEpRn,
       "cucsSwFcoeEstcEpAdminState": cucsSwFcoeEstcEpAdminState,
       "cucsSwFcoeEstcEpChassisId": cucsSwFcoeEstcEpChassisId,
       "cucsSwFcoeEstcEpEpDn": cucsSwFcoeEstcEpEpDn,
       "cucsSwFcoeEstcEpIfRole": cucsSwFcoeEstcEpIfRole,
       "cucsSwFcoeEstcEpIfType": cucsSwFcoeEstcEpIfType,
       "cucsSwFcoeEstcEpLocale": cucsSwFcoeEstcEpLocale,
       "cucsSwFcoeEstcEpName": cucsSwFcoeEstcEpName,
       "cucsSwFcoeEstcEpPeerDn": cucsSwFcoeEstcEpPeerDn,
       "cucsSwFcoeEstcEpPeerPortId": cucsSwFcoeEstcEpPeerPortId,
       "cucsSwFcoeEstcEpPeerSlotId": cucsSwFcoeEstcEpPeerSlotId,
       "cucsSwFcoeEstcEpPortId": cucsSwFcoeEstcEpPortId,
       "cucsSwFcoeEstcEpSlotId": cucsSwFcoeEstcEpSlotId,
       "cucsSwFcoeEstcEpSwitchId": cucsSwFcoeEstcEpSwitchId,
       "cucsSwFcoeEstcEpTransport": cucsSwFcoeEstcEpTransport,
       "cucsSwFcoeEstcEpType": cucsSwFcoeEstcEpType,
       "cucsSwFcoeEstcEpPeerChassisId": cucsSwFcoeEstcEpPeerChassisId,
       "cucsSwFcoeEstcEpLc": cucsSwFcoeEstcEpLc,
       "cucsSwFcoeEstcEpPeerState": cucsSwFcoeEstcEpPeerState,
       "cucsSwFcoeEstcEpAggrPortId": cucsSwFcoeEstcEpAggrPortId,
       "cucsSwFcoeEstcEpPeerAggrPortId": cucsSwFcoeEstcEpPeerAggrPortId,
       "cucsSwFcoeEstcEpAutoNegotiate": cucsSwFcoeEstcEpAutoNegotiate,
       "cucsSwSystemStatsTable": cucsSwSystemStatsTable,
       "cucsSwSystemStatsEntry": cucsSwSystemStatsEntry,
       "cucsSwSystemStatsInstanceId": cucsSwSystemStatsInstanceId,
       "cucsSwSystemStatsDn": cucsSwSystemStatsDn,
       "cucsSwSystemStatsRn": cucsSwSystemStatsRn,
       "cucsSwSystemStatsIntervals": cucsSwSystemStatsIntervals,
       "cucsSwSystemStatsLoad": cucsSwSystemStatsLoad,
       "cucsSwSystemStatsLoadAvg": cucsSwSystemStatsLoadAvg,
       "cucsSwSystemStatsLoadMax": cucsSwSystemStatsLoadMax,
       "cucsSwSystemStatsLoadMin": cucsSwSystemStatsLoadMin,
       "cucsSwSystemStatsMemAvailable": cucsSwSystemStatsMemAvailable,
       "cucsSwSystemStatsMemAvailableAvg": cucsSwSystemStatsMemAvailableAvg,
       "cucsSwSystemStatsMemAvailableMax": cucsSwSystemStatsMemAvailableMax,
       "cucsSwSystemStatsMemAvailableMin": cucsSwSystemStatsMemAvailableMin,
       "cucsSwSystemStatsMemCached": cucsSwSystemStatsMemCached,
       "cucsSwSystemStatsMemCachedAvg": cucsSwSystemStatsMemCachedAvg,
       "cucsSwSystemStatsMemCachedMax": cucsSwSystemStatsMemCachedMax,
       "cucsSwSystemStatsMemCachedMin": cucsSwSystemStatsMemCachedMin,
       "cucsSwSystemStatsSuspect": cucsSwSystemStatsSuspect,
       "cucsSwSystemStatsThresholded": cucsSwSystemStatsThresholded,
       "cucsSwSystemStatsTimeCollected": cucsSwSystemStatsTimeCollected,
       "cucsSwSystemStatsUpdate": cucsSwSystemStatsUpdate,
       "cucsSwSystemStatsCorrectableParityError": cucsSwSystemStatsCorrectableParityError,
       "cucsSwSystemStatsCorrectableParityErrorAvg": cucsSwSystemStatsCorrectableParityErrorAvg,
       "cucsSwSystemStatsCorrectableParityErrorMax": cucsSwSystemStatsCorrectableParityErrorMax,
       "cucsSwSystemStatsCorrectableParityErrorMin": cucsSwSystemStatsCorrectableParityErrorMin,
       "cucsSwSystemStatsKernelMemFree": cucsSwSystemStatsKernelMemFree,
       "cucsSwSystemStatsKernelMemFreeAvg": cucsSwSystemStatsKernelMemFreeAvg,
       "cucsSwSystemStatsKernelMemFreeMax": cucsSwSystemStatsKernelMemFreeMax,
       "cucsSwSystemStatsKernelMemFreeMin": cucsSwSystemStatsKernelMemFreeMin,
       "cucsSwSystemStatsKernelMemTotal": cucsSwSystemStatsKernelMemTotal,
       "cucsSwSystemStatsKernelMemTotalAvg": cucsSwSystemStatsKernelMemTotalAvg,
       "cucsSwSystemStatsKernelMemTotalMax": cucsSwSystemStatsKernelMemTotalMax,
       "cucsSwSystemStatsKernelMemTotalMin": cucsSwSystemStatsKernelMemTotalMin,
       "cucsSwSystemStatsHistTable": cucsSwSystemStatsHistTable,
       "cucsSwSystemStatsHistEntry": cucsSwSystemStatsHistEntry,
       "cucsSwSystemStatsHistInstanceId": cucsSwSystemStatsHistInstanceId,
       "cucsSwSystemStatsHistDn": cucsSwSystemStatsHistDn,
       "cucsSwSystemStatsHistRn": cucsSwSystemStatsHistRn,
       "cucsSwSystemStatsHistId": cucsSwSystemStatsHistId,
       "cucsSwSystemStatsHistLoad": cucsSwSystemStatsHistLoad,
       "cucsSwSystemStatsHistLoadAvg": cucsSwSystemStatsHistLoadAvg,
       "cucsSwSystemStatsHistLoadMax": cucsSwSystemStatsHistLoadMax,
       "cucsSwSystemStatsHistLoadMin": cucsSwSystemStatsHistLoadMin,
       "cucsSwSystemStatsHistMemAvailable": cucsSwSystemStatsHistMemAvailable,
       "cucsSwSystemStatsHistMemAvailableAvg": cucsSwSystemStatsHistMemAvailableAvg,
       "cucsSwSystemStatsHistMemAvailableMax": cucsSwSystemStatsHistMemAvailableMax,
       "cucsSwSystemStatsHistMemAvailableMin": cucsSwSystemStatsHistMemAvailableMin,
       "cucsSwSystemStatsHistMemCached": cucsSwSystemStatsHistMemCached,
       "cucsSwSystemStatsHistMemCachedAvg": cucsSwSystemStatsHistMemCachedAvg,
       "cucsSwSystemStatsHistMemCachedMax": cucsSwSystemStatsHistMemCachedMax,
       "cucsSwSystemStatsHistMemCachedMin": cucsSwSystemStatsHistMemCachedMin,
       "cucsSwSystemStatsHistMostRecent": cucsSwSystemStatsHistMostRecent,
       "cucsSwSystemStatsHistSuspect": cucsSwSystemStatsHistSuspect,
       "cucsSwSystemStatsHistThresholded": cucsSwSystemStatsHistThresholded,
       "cucsSwSystemStatsHistTimeCollected": cucsSwSystemStatsHistTimeCollected,
       "cucsSwSystemStatsHistCorrectableParityError": cucsSwSystemStatsHistCorrectableParityError,
       "cucsSwSystemStatsHistCorrectableParityErrorAvg": cucsSwSystemStatsHistCorrectableParityErrorAvg,
       "cucsSwSystemStatsHistCorrectableParityErrorMax": cucsSwSystemStatsHistCorrectableParityErrorMax,
       "cucsSwSystemStatsHistCorrectableParityErrorMin": cucsSwSystemStatsHistCorrectableParityErrorMin,
       "cucsSwSystemStatsHistKernelMemFree": cucsSwSystemStatsHistKernelMemFree,
       "cucsSwSystemStatsHistKernelMemFreeAvg": cucsSwSystemStatsHistKernelMemFreeAvg,
       "cucsSwSystemStatsHistKernelMemFreeMax": cucsSwSystemStatsHistKernelMemFreeMax,
       "cucsSwSystemStatsHistKernelMemFreeMin": cucsSwSystemStatsHistKernelMemFreeMin,
       "cucsSwSystemStatsHistKernelMemTotal": cucsSwSystemStatsHistKernelMemTotal,
       "cucsSwSystemStatsHistKernelMemTotalAvg": cucsSwSystemStatsHistKernelMemTotalAvg,
       "cucsSwSystemStatsHistKernelMemTotalMax": cucsSwSystemStatsHistKernelMemTotalMax,
       "cucsSwSystemStatsHistKernelMemTotalMin": cucsSwSystemStatsHistKernelMemTotalMin,
       "cucsSwUlanTable": cucsSwUlanTable,
       "cucsSwUlanEntry": cucsSwUlanEntry,
       "cucsSwUlanInstanceId": cucsSwUlanInstanceId,
       "cucsSwUlanDn": cucsSwUlanDn,
       "cucsSwUlanRn": cucsSwUlanRn,
       "cucsSwUlanEpDn": cucsSwUlanEpDn,
       "cucsSwUlanId": cucsSwUlanId,
       "cucsSwUlanIfRole": cucsSwUlanIfRole,
       "cucsSwUlanIfType": cucsSwUlanIfType,
       "cucsSwUlanLocale": cucsSwUlanLocale,
       "cucsSwUlanName": cucsSwUlanName,
       "cucsSwUlanPeerDn": cucsSwUlanPeerDn,
       "cucsSwUlanPubNwDn": cucsSwUlanPubNwDn,
       "cucsSwUlanPubNwId": cucsSwUlanPubNwId,
       "cucsSwUlanPubNwName": cucsSwUlanPubNwName,
       "cucsSwUlanPurpose": cucsSwUlanPurpose,
       "cucsSwUlanSharing": cucsSwUlanSharing,
       "cucsSwUlanSwitchId": cucsSwUlanSwitchId,
       "cucsSwUlanTransport": cucsSwUlanTransport,
       "cucsSwUlanType": cucsSwUlanType,
       "cucsSwUlanVlanType": cucsSwUlanVlanType,
       "cucsSwUlanOperState": cucsSwUlanOperState,
       "cucsSwUlanPolicyOwner": cucsSwUlanPolicyOwner,
       "cucsSwUlanAssocPrimaryVlanState": cucsSwUlanAssocPrimaryVlanState,
       "cucsSwUlanAssocPrimaryVlanSwitchId": cucsSwUlanAssocPrimaryVlanSwitchId,
       "cucsSwUlanOverlapStateForA": cucsSwUlanOverlapStateForA,
       "cucsSwUlanOverlapStateForB": cucsSwUlanOverlapStateForB,
       "cucsSwUtilityDomainTable": cucsSwUtilityDomainTable,
       "cucsSwUtilityDomainEntry": cucsSwUtilityDomainEntry,
       "cucsSwUtilityDomainInstanceId": cucsSwUtilityDomainInstanceId,
       "cucsSwUtilityDomainDn": cucsSwUtilityDomainDn,
       "cucsSwUtilityDomainRn": cucsSwUtilityDomainRn,
       "cucsSwUtilityDomainFsmDescr": cucsSwUtilityDomainFsmDescr,
       "cucsSwUtilityDomainFsmPrev": cucsSwUtilityDomainFsmPrev,
       "cucsSwUtilityDomainFsmProgr": cucsSwUtilityDomainFsmProgr,
       "cucsSwUtilityDomainFsmRmtInvErrCode": cucsSwUtilityDomainFsmRmtInvErrCode,
       "cucsSwUtilityDomainFsmRmtInvErrDescr": cucsSwUtilityDomainFsmRmtInvErrDescr,
       "cucsSwUtilityDomainFsmRmtInvRslt": cucsSwUtilityDomainFsmRmtInvRslt,
       "cucsSwUtilityDomainFsmStageDescr": cucsSwUtilityDomainFsmStageDescr,
       "cucsSwUtilityDomainFsmStamp": cucsSwUtilityDomainFsmStamp,
       "cucsSwUtilityDomainFsmStatus": cucsSwUtilityDomainFsmStatus,
       "cucsSwUtilityDomainFsmTry": cucsSwUtilityDomainFsmTry,
       "cucsSwUtilityDomainLocale": cucsSwUtilityDomainLocale,
       "cucsSwUtilityDomainName": cucsSwUtilityDomainName,
       "cucsSwUtilityDomainSwitchId": cucsSwUtilityDomainSwitchId,
       "cucsSwUtilityDomainTransport": cucsSwUtilityDomainTransport,
       "cucsSwUtilityDomainType": cucsSwUtilityDomainType,
       "cucsSwUtilityDomainFsmTaskTable": cucsSwUtilityDomainFsmTaskTable,
       "cucsSwUtilityDomainFsmTaskEntry": cucsSwUtilityDomainFsmTaskEntry,
       "cucsSwUtilityDomainFsmTaskInstanceId": cucsSwUtilityDomainFsmTaskInstanceId,
       "cucsSwUtilityDomainFsmTaskDn": cucsSwUtilityDomainFsmTaskDn,
       "cucsSwUtilityDomainFsmTaskRn": cucsSwUtilityDomainFsmTaskRn,
       "cucsSwUtilityDomainFsmTaskCompletion": cucsSwUtilityDomainFsmTaskCompletion,
       "cucsSwUtilityDomainFsmTaskFlags": cucsSwUtilityDomainFsmTaskFlags,
       "cucsSwUtilityDomainFsmTaskItem": cucsSwUtilityDomainFsmTaskItem,
       "cucsSwUtilityDomainFsmTaskSeqId": cucsSwUtilityDomainFsmTaskSeqId,
       "cucsSwVlanTable": cucsSwVlanTable,
       "cucsSwVlanEntry": cucsSwVlanEntry,
       "cucsSwVlanInstanceId": cucsSwVlanInstanceId,
       "cucsSwVlanDn": cucsSwVlanDn,
       "cucsSwVlanRn": cucsSwVlanRn,
       "cucsSwVlanEpDn": cucsSwVlanEpDn,
       "cucsSwVlanId": cucsSwVlanId,
       "cucsSwVlanIfRole": cucsSwVlanIfRole,
       "cucsSwVlanIfType": cucsSwVlanIfType,
       "cucsSwVlanLc": cucsSwVlanLc,
       "cucsSwVlanLocale": cucsSwVlanLocale,
       "cucsSwVlanMonTrafDir": cucsSwVlanMonTrafDir,
       "cucsSwVlanName": cucsSwVlanName,
       "cucsSwVlanPeerDn": cucsSwVlanPeerDn,
       "cucsSwVlanPubNwDn": cucsSwVlanPubNwDn,
       "cucsSwVlanPubNwId": cucsSwVlanPubNwId,
       "cucsSwVlanPubNwName": cucsSwVlanPubNwName,
       "cucsSwVlanSharing": cucsSwVlanSharing,
       "cucsSwVlanSwitchId": cucsSwVlanSwitchId,
       "cucsSwVlanTransport": cucsSwVlanTransport,
       "cucsSwVlanType": cucsSwVlanType,
       "cucsSwVlanVlanType": cucsSwVlanVlanType,
       "cucsSwVlanOperState": cucsSwVlanOperState,
       "cucsSwVlanCompressionType": cucsSwVlanCompressionType,
       "cucsSwVlanQuerierIpAddrs": cucsSwVlanQuerierIpAddrs,
       "cucsSwVlanSnoopingEnabled": cucsSwVlanSnoopingEnabled,
       "cucsSwVlanPolicyOwner": cucsSwVlanPolicyOwner,
       "cucsSwVlanAssocPrimaryVlanState": cucsSwVlanAssocPrimaryVlanState,
       "cucsSwVlanAssocPrimaryVlanSwitchId": cucsSwVlanAssocPrimaryVlanSwitchId,
       "cucsSwVlanOverlapStateForA": cucsSwVlanOverlapStateForA,
       "cucsSwVlanOverlapStateForB": cucsSwVlanOverlapStateForB,
       "cucsSwVlanSecVlanPerPrimaryVlanCount": cucsSwVlanSecVlanPerPrimaryVlanCount,
       "cucsSwVlanSecVlanPerPrimaryVlanCountStatus": cucsSwVlanSecVlanPerPrimaryVlanCountStatus,
       "cucsSwVlanPortNsTable": cucsSwVlanPortNsTable,
       "cucsSwVlanPortNsEntry": cucsSwVlanPortNsEntry,
       "cucsSwVlanPortNsInstanceId": cucsSwVlanPortNsInstanceId,
       "cucsSwVlanPortNsDn": cucsSwVlanPortNsDn,
       "cucsSwVlanPortNsRn": cucsSwVlanPortNsRn,
       "cucsSwVlanPortNsAccessVlanPortCount": cucsSwVlanPortNsAccessVlanPortCount,
       "cucsSwVlanPortNsAllocStatus": cucsSwVlanPortNsAllocStatus,
       "cucsSwVlanPortNsBorderVlanPortCount": cucsSwVlanPortNsBorderVlanPortCount,
       "cucsSwVlanPortNsLimit": cucsSwVlanPortNsLimit,
       "cucsSwVlanPortNsSwitchId": cucsSwVlanPortNsSwitchId,
       "cucsSwVlanPortNsConfigStatus": cucsSwVlanPortNsConfigStatus,
       "cucsSwVlanPortNsVlanCompOffLimit": cucsSwVlanPortNsVlanCompOffLimit,
       "cucsSwVlanPortNsVlanCompOnLimit": cucsSwVlanPortNsVlanCompOnLimit,
       "cucsSwVlanPortNsTotalVlanPortCount": cucsSwVlanPortNsTotalVlanPortCount,
       "cucsSwVlanPortNsCompressedOptimizationSets": cucsSwVlanPortNsCompressedOptimizationSets,
       "cucsSwVlanPortNsCompressedVlanPortCount": cucsSwVlanPortNsCompressedVlanPortCount,
       "cucsSwVlanPortNsTotalOptimizationSets": cucsSwVlanPortNsTotalOptimizationSets,
       "cucsSwVlanPortNsUncompressedVlanPortCount": cucsSwVlanPortNsUncompressedVlanPortCount,
       "cucsSwVsanTable": cucsSwVsanTable,
       "cucsSwVsanEntry": cucsSwVsanEntry,
       "cucsSwVsanInstanceId": cucsSwVsanInstanceId,
       "cucsSwVsanDn": cucsSwVsanDn,
       "cucsSwVsanRn": cucsSwVsanRn,
       "cucsSwVsanEpDn": cucsSwVsanEpDn,
       "cucsSwVsanFcoeVlan": cucsSwVsanFcoeVlan,
       "cucsSwVsanId": cucsSwVsanId,
       "cucsSwVsanIfRole": cucsSwVsanIfRole,
       "cucsSwVsanIfType": cucsSwVsanIfType,
       "cucsSwVsanLc": cucsSwVsanLc,
       "cucsSwVsanLocale": cucsSwVsanLocale,
       "cucsSwVsanMonTrafDir": cucsSwVsanMonTrafDir,
       "cucsSwVsanName": cucsSwVsanName,
       "cucsSwVsanPeerDn": cucsSwVsanPeerDn,
       "cucsSwVsanSwitchId": cucsSwVsanSwitchId,
       "cucsSwVsanTransport": cucsSwVsanTransport,
       "cucsSwVsanType": cucsSwVsanType,
       "cucsSwVsanDefaultZoning": cucsSwVsanDefaultZoning,
       "cucsSwVsanOperState": cucsSwVsanOperState,
       "cucsSwVsanFcZoneSharingMode": cucsSwVsanFcZoneSharingMode,
       "cucsSwVsanFltAggr": cucsSwVsanFltAggr,
       "cucsSwVsanZoningState": cucsSwVsanZoningState,
       "cucsSwVsanPolicyOwner": cucsSwVsanPolicyOwner,
       "cucsSwEthEstcPcTable": cucsSwEthEstcPcTable,
       "cucsSwEthEstcPcEntry": cucsSwEthEstcPcEntry,
       "cucsSwEthEstcPcInstanceId": cucsSwEthEstcPcInstanceId,
       "cucsSwEthEstcPcDn": cucsSwEthEstcPcDn,
       "cucsSwEthEstcPcRn": cucsSwEthEstcPcRn,
       "cucsSwEthEstcPcAdminSpeed": cucsSwEthEstcPcAdminSpeed,
       "cucsSwEthEstcPcAdminState": cucsSwEthEstcPcAdminState,
       "cucsSwEthEstcPcBorderPortId": cucsSwEthEstcPcBorderPortId,
       "cucsSwEthEstcPcBorderSlotId": cucsSwEthEstcPcBorderSlotId,
       "cucsSwEthEstcPcCosValue": cucsSwEthEstcPcCosValue,
       "cucsSwEthEstcPcEpDn": cucsSwEthEstcPcEpDn,
       "cucsSwEthEstcPcIfRole": cucsSwEthEstcPcIfRole,
       "cucsSwEthEstcPcIfType": cucsSwEthEstcPcIfType,
       "cucsSwEthEstcPcLocale": cucsSwEthEstcPcLocale,
       "cucsSwEthEstcPcMonTrafDir": cucsSwEthEstcPcMonTrafDir,
       "cucsSwEthEstcPcName": cucsSwEthEstcPcName,
       "cucsSwEthEstcPcPeerDn": cucsSwEthEstcPcPeerDn,
       "cucsSwEthEstcPcPortId": cucsSwEthEstcPcPortId,
       "cucsSwEthEstcPcPortMode": cucsSwEthEstcPcPortMode,
       "cucsSwEthEstcPcSwitchId": cucsSwEthEstcPcSwitchId,
       "cucsSwEthEstcPcTransport": cucsSwEthEstcPcTransport,
       "cucsSwEthEstcPcType": cucsSwEthEstcPcType,
       "cucsSwEthEstcPcCdp": cucsSwEthEstcPcCdp,
       "cucsSwEthEstcPcForgeMac": cucsSwEthEstcPcForgeMac,
       "cucsSwEthEstcPcProtocol": cucsSwEthEstcPcProtocol,
       "cucsSwEthEstcPcUplinkFailAction": cucsSwEthEstcPcUplinkFailAction,
       "cucsSwEthEstcPcPriorityFlowCtrl": cucsSwEthEstcPcPriorityFlowCtrl,
       "cucsSwEthEstcPcRecvFlowCtrl": cucsSwEthEstcPcRecvFlowCtrl,
       "cucsSwEthEstcPcSendFlowCtrl": cucsSwEthEstcPcSendFlowCtrl,
       "cucsSwEthEstcPcLacpFastTimer": cucsSwEthEstcPcLacpFastTimer,
       "cucsSwEthEstcPcLacpSuspendIndividual": cucsSwEthEstcPcLacpSuspendIndividual,
       "cucsSwEthEstcPcBorderAggrPortId": cucsSwEthEstcPcBorderAggrPortId,
       "cucsSwVlanPortNsOverrideTable": cucsSwVlanPortNsOverrideTable,
       "cucsSwVlanPortNsOverrideEntry": cucsSwVlanPortNsOverrideEntry,
       "cucsSwVlanPortNsOverrideInstanceId": cucsSwVlanPortNsOverrideInstanceId,
       "cucsSwVlanPortNsOverrideDn": cucsSwVlanPortNsOverrideDn,
       "cucsSwVlanPortNsOverrideRn": cucsSwVlanPortNsOverrideRn,
       "cucsSwVlanPortNsOverrideLimit": cucsSwVlanPortNsOverrideLimit,
       "cucsSwPhysTable": cucsSwPhysTable,
       "cucsSwPhysEntry": cucsSwPhysEntry,
       "cucsSwPhysInstanceId": cucsSwPhysInstanceId,
       "cucsSwPhysDn": cucsSwPhysDn,
       "cucsSwPhysRn": cucsSwPhysRn,
       "cucsSwPhysConfMode": cucsSwPhysConfMode,
       "cucsSwPhysFsmDescr": cucsSwPhysFsmDescr,
       "cucsSwPhysFsmPrev": cucsSwPhysFsmPrev,
       "cucsSwPhysFsmProgr": cucsSwPhysFsmProgr,
       "cucsSwPhysFsmRmtInvErrCode": cucsSwPhysFsmRmtInvErrCode,
       "cucsSwPhysFsmRmtInvErrDescr": cucsSwPhysFsmRmtInvErrDescr,
       "cucsSwPhysFsmRmtInvRslt": cucsSwPhysFsmRmtInvRslt,
       "cucsSwPhysFsmStageDescr": cucsSwPhysFsmStageDescr,
       "cucsSwPhysFsmStamp": cucsSwPhysFsmStamp,
       "cucsSwPhysFsmStatus": cucsSwPhysFsmStatus,
       "cucsSwPhysFsmTry": cucsSwPhysFsmTry,
       "cucsSwPhysEtherEpTable": cucsSwPhysEtherEpTable,
       "cucsSwPhysEtherEpEntry": cucsSwPhysEtherEpEntry,
       "cucsSwPhysEtherEpInstanceId": cucsSwPhysEtherEpInstanceId,
       "cucsSwPhysEtherEpDn": cucsSwPhysEtherEpDn,
       "cucsSwPhysEtherEpRn": cucsSwPhysEtherEpRn,
       "cucsSwPhysEtherEpAdminState": cucsSwPhysEtherEpAdminState,
       "cucsSwPhysEtherEpChassisId": cucsSwPhysEtherEpChassisId,
       "cucsSwPhysEtherEpEpDn": cucsSwPhysEtherEpEpDn,
       "cucsSwPhysEtherEpIfRole": cucsSwPhysEtherEpIfRole,
       "cucsSwPhysEtherEpIfType": cucsSwPhysEtherEpIfType,
       "cucsSwPhysEtherEpLc": cucsSwPhysEtherEpLc,
       "cucsSwPhysEtherEpLocale": cucsSwPhysEtherEpLocale,
       "cucsSwPhysEtherEpName": cucsSwPhysEtherEpName,
       "cucsSwPhysEtherEpPeerChassisId": cucsSwPhysEtherEpPeerChassisId,
       "cucsSwPhysEtherEpPeerDn": cucsSwPhysEtherEpPeerDn,
       "cucsSwPhysEtherEpPeerPortId": cucsSwPhysEtherEpPeerPortId,
       "cucsSwPhysEtherEpPeerSlotId": cucsSwPhysEtherEpPeerSlotId,
       "cucsSwPhysEtherEpPortId": cucsSwPhysEtherEpPortId,
       "cucsSwPhysEtherEpSlotId": cucsSwPhysEtherEpSlotId,
       "cucsSwPhysEtherEpSwitchId": cucsSwPhysEtherEpSwitchId,
       "cucsSwPhysEtherEpTransport": cucsSwPhysEtherEpTransport,
       "cucsSwPhysEtherEpType": cucsSwPhysEtherEpType,
       "cucsSwPhysEtherEpAggrPortId": cucsSwPhysEtherEpAggrPortId,
       "cucsSwPhysEtherEpPeerAggrPortId": cucsSwPhysEtherEpPeerAggrPortId,
       "cucsSwPhysEtherEpAutoNegotiate": cucsSwPhysEtherEpAutoNegotiate,
       "cucsSwPhysFcEpTable": cucsSwPhysFcEpTable,
       "cucsSwPhysFcEpEntry": cucsSwPhysFcEpEntry,
       "cucsSwPhysFcEpInstanceId": cucsSwPhysFcEpInstanceId,
       "cucsSwPhysFcEpDn": cucsSwPhysFcEpDn,
       "cucsSwPhysFcEpRn": cucsSwPhysFcEpRn,
       "cucsSwPhysFcEpAdminState": cucsSwPhysFcEpAdminState,
       "cucsSwPhysFcEpChassisId": cucsSwPhysFcEpChassisId,
       "cucsSwPhysFcEpEpDn": cucsSwPhysFcEpEpDn,
       "cucsSwPhysFcEpIfRole": cucsSwPhysFcEpIfRole,
       "cucsSwPhysFcEpIfType": cucsSwPhysFcEpIfType,
       "cucsSwPhysFcEpLc": cucsSwPhysFcEpLc,
       "cucsSwPhysFcEpLocale": cucsSwPhysFcEpLocale,
       "cucsSwPhysFcEpName": cucsSwPhysFcEpName,
       "cucsSwPhysFcEpPeerChassisId": cucsSwPhysFcEpPeerChassisId,
       "cucsSwPhysFcEpPeerDn": cucsSwPhysFcEpPeerDn,
       "cucsSwPhysFcEpPeerPortId": cucsSwPhysFcEpPeerPortId,
       "cucsSwPhysFcEpPeerSlotId": cucsSwPhysFcEpPeerSlotId,
       "cucsSwPhysFcEpPortId": cucsSwPhysFcEpPortId,
       "cucsSwPhysFcEpSlotId": cucsSwPhysFcEpSlotId,
       "cucsSwPhysFcEpSwitchId": cucsSwPhysFcEpSwitchId,
       "cucsSwPhysFcEpTransport": cucsSwPhysFcEpTransport,
       "cucsSwPhysFcEpType": cucsSwPhysFcEpType,
       "cucsSwPhysFcEpAggrPortId": cucsSwPhysFcEpAggrPortId,
       "cucsSwPhysFcEpPeerAggrPortId": cucsSwPhysFcEpPeerAggrPortId,
       "cucsSwPhysFcEpAutoNegotiate": cucsSwPhysFcEpAutoNegotiate,
       "cucsSwPhysFsmTaskTable": cucsSwPhysFsmTaskTable,
       "cucsSwPhysFsmTaskEntry": cucsSwPhysFsmTaskEntry,
       "cucsSwPhysFsmTaskInstanceId": cucsSwPhysFsmTaskInstanceId,
       "cucsSwPhysFsmTaskDn": cucsSwPhysFsmTaskDn,
       "cucsSwPhysFsmTaskRn": cucsSwPhysFsmTaskRn,
       "cucsSwPhysFsmTaskCompletion": cucsSwPhysFsmTaskCompletion,
       "cucsSwPhysFsmTaskFlags": cucsSwPhysFsmTaskFlags,
       "cucsSwPhysFsmTaskItem": cucsSwPhysFsmTaskItem,
       "cucsSwPhysFsmTaskSeqId": cucsSwPhysFsmTaskSeqId,
       "cucsSwAccessDomainFsmTable": cucsSwAccessDomainFsmTable,
       "cucsSwAccessDomainFsmEntry": cucsSwAccessDomainFsmEntry,
       "cucsSwAccessDomainFsmInstanceId": cucsSwAccessDomainFsmInstanceId,
       "cucsSwAccessDomainFsmDn": cucsSwAccessDomainFsmDn,
       "cucsSwAccessDomainFsmRn": cucsSwAccessDomainFsmRn,
       "cucsSwAccessDomainFsmCompletionTime": cucsSwAccessDomainFsmCompletionTime,
       "cucsSwAccessDomainFsmCurrentFsm": cucsSwAccessDomainFsmCurrentFsm,
       "cucsSwAccessDomainFsmDescrData": cucsSwAccessDomainFsmDescrData,
       "cucsSwAccessDomainFsmFsmStatus": cucsSwAccessDomainFsmFsmStatus,
       "cucsSwAccessDomainFsmProgress": cucsSwAccessDomainFsmProgress,
       "cucsSwAccessDomainFsmRmtErrCode": cucsSwAccessDomainFsmRmtErrCode,
       "cucsSwAccessDomainFsmRmtErrDescr": cucsSwAccessDomainFsmRmtErrDescr,
       "cucsSwAccessDomainFsmRmtRslt": cucsSwAccessDomainFsmRmtRslt,
       "cucsSwAccessDomainFsmStageTable": cucsSwAccessDomainFsmStageTable,
       "cucsSwAccessDomainFsmStageEntry": cucsSwAccessDomainFsmStageEntry,
       "cucsSwAccessDomainFsmStageInstanceId": cucsSwAccessDomainFsmStageInstanceId,
       "cucsSwAccessDomainFsmStageDn": cucsSwAccessDomainFsmStageDn,
       "cucsSwAccessDomainFsmStageRn": cucsSwAccessDomainFsmStageRn,
       "cucsSwAccessDomainFsmStageDescrData": cucsSwAccessDomainFsmStageDescrData,
       "cucsSwAccessDomainFsmStageLastUpdateTime": cucsSwAccessDomainFsmStageLastUpdateTime,
       "cucsSwAccessDomainFsmStageName": cucsSwAccessDomainFsmStageName,
       "cucsSwAccessDomainFsmStageOrder": cucsSwAccessDomainFsmStageOrder,
       "cucsSwAccessDomainFsmStageRetry": cucsSwAccessDomainFsmStageRetry,
       "cucsSwAccessDomainFsmStageStageStatus": cucsSwAccessDomainFsmStageStageStatus,
       "cucsSwCardEnvStatsTable": cucsSwCardEnvStatsTable,
       "cucsSwCardEnvStatsEntry": cucsSwCardEnvStatsEntry,
       "cucsSwCardEnvStatsInstanceId": cucsSwCardEnvStatsInstanceId,
       "cucsSwCardEnvStatsDn": cucsSwCardEnvStatsDn,
       "cucsSwCardEnvStatsRn": cucsSwCardEnvStatsRn,
       "cucsSwCardEnvStatsSlotOutlet1": cucsSwCardEnvStatsSlotOutlet1,
       "cucsSwCardEnvStatsSlotOutlet1Avg": cucsSwCardEnvStatsSlotOutlet1Avg,
       "cucsSwCardEnvStatsSlotOutlet1Max": cucsSwCardEnvStatsSlotOutlet1Max,
       "cucsSwCardEnvStatsSlotOutlet1Min": cucsSwCardEnvStatsSlotOutlet1Min,
       "cucsSwCardEnvStatsSlotOutlet2": cucsSwCardEnvStatsSlotOutlet2,
       "cucsSwCardEnvStatsSlotOutlet2Avg": cucsSwCardEnvStatsSlotOutlet2Avg,
       "cucsSwCardEnvStatsSlotOutlet2Max": cucsSwCardEnvStatsSlotOutlet2Max,
       "cucsSwCardEnvStatsSlotOutlet2Min": cucsSwCardEnvStatsSlotOutlet2Min,
       "cucsSwCardEnvStatsSlotOutlet3": cucsSwCardEnvStatsSlotOutlet3,
       "cucsSwCardEnvStatsSlotOutlet3Avg": cucsSwCardEnvStatsSlotOutlet3Avg,
       "cucsSwCardEnvStatsSlotOutlet3Max": cucsSwCardEnvStatsSlotOutlet3Max,
       "cucsSwCardEnvStatsSlotOutlet3Min": cucsSwCardEnvStatsSlotOutlet3Min,
       "cucsSwCardEnvStatsIntervals": cucsSwCardEnvStatsIntervals,
       "cucsSwCardEnvStatsSuspect": cucsSwCardEnvStatsSuspect,
       "cucsSwCardEnvStatsThresholded": cucsSwCardEnvStatsThresholded,
       "cucsSwCardEnvStatsTimeCollected": cucsSwCardEnvStatsTimeCollected,
       "cucsSwCardEnvStatsUpdate": cucsSwCardEnvStatsUpdate,
       "cucsSwCardEnvStatsHistTable": cucsSwCardEnvStatsHistTable,
       "cucsSwCardEnvStatsHistEntry": cucsSwCardEnvStatsHistEntry,
       "cucsSwCardEnvStatsHistInstanceId": cucsSwCardEnvStatsHistInstanceId,
       "cucsSwCardEnvStatsHistDn": cucsSwCardEnvStatsHistDn,
       "cucsSwCardEnvStatsHistRn": cucsSwCardEnvStatsHistRn,
       "cucsSwCardEnvStatsHistSlotOutlet1": cucsSwCardEnvStatsHistSlotOutlet1,
       "cucsSwCardEnvStatsHistSlotOutlet1Avg": cucsSwCardEnvStatsHistSlotOutlet1Avg,
       "cucsSwCardEnvStatsHistSlotOutlet1Max": cucsSwCardEnvStatsHistSlotOutlet1Max,
       "cucsSwCardEnvStatsHistSlotOutlet1Min": cucsSwCardEnvStatsHistSlotOutlet1Min,
       "cucsSwCardEnvStatsHistSlotOutlet2": cucsSwCardEnvStatsHistSlotOutlet2,
       "cucsSwCardEnvStatsHistSlotOutlet2Avg": cucsSwCardEnvStatsHistSlotOutlet2Avg,
       "cucsSwCardEnvStatsHistSlotOutlet2Max": cucsSwCardEnvStatsHistSlotOutlet2Max,
       "cucsSwCardEnvStatsHistSlotOutlet2Min": cucsSwCardEnvStatsHistSlotOutlet2Min,
       "cucsSwCardEnvStatsHistSlotOutlet3": cucsSwCardEnvStatsHistSlotOutlet3,
       "cucsSwCardEnvStatsHistSlotOutlet3Avg": cucsSwCardEnvStatsHistSlotOutlet3Avg,
       "cucsSwCardEnvStatsHistSlotOutlet3Max": cucsSwCardEnvStatsHistSlotOutlet3Max,
       "cucsSwCardEnvStatsHistSlotOutlet3Min": cucsSwCardEnvStatsHistSlotOutlet3Min,
       "cucsSwCardEnvStatsHistId": cucsSwCardEnvStatsHistId,
       "cucsSwCardEnvStatsHistMostRecent": cucsSwCardEnvStatsHistMostRecent,
       "cucsSwCardEnvStatsHistSuspect": cucsSwCardEnvStatsHistSuspect,
       "cucsSwCardEnvStatsHistThresholded": cucsSwCardEnvStatsHistThresholded,
       "cucsSwCardEnvStatsHistTimeCollected": cucsSwCardEnvStatsHistTimeCollected,
       "cucsSwEthLanBorderFsmTable": cucsSwEthLanBorderFsmTable,
       "cucsSwEthLanBorderFsmEntry": cucsSwEthLanBorderFsmEntry,
       "cucsSwEthLanBorderFsmInstanceId": cucsSwEthLanBorderFsmInstanceId,
       "cucsSwEthLanBorderFsmDn": cucsSwEthLanBorderFsmDn,
       "cucsSwEthLanBorderFsmRn": cucsSwEthLanBorderFsmRn,
       "cucsSwEthLanBorderFsmCompletionTime": cucsSwEthLanBorderFsmCompletionTime,
       "cucsSwEthLanBorderFsmCurrentFsm": cucsSwEthLanBorderFsmCurrentFsm,
       "cucsSwEthLanBorderFsmDescrData": cucsSwEthLanBorderFsmDescrData,
       "cucsSwEthLanBorderFsmFsmStatus": cucsSwEthLanBorderFsmFsmStatus,
       "cucsSwEthLanBorderFsmProgress": cucsSwEthLanBorderFsmProgress,
       "cucsSwEthLanBorderFsmRmtErrCode": cucsSwEthLanBorderFsmRmtErrCode,
       "cucsSwEthLanBorderFsmRmtErrDescr": cucsSwEthLanBorderFsmRmtErrDescr,
       "cucsSwEthLanBorderFsmRmtRslt": cucsSwEthLanBorderFsmRmtRslt,
       "cucsSwEthLanBorderFsmStageTable": cucsSwEthLanBorderFsmStageTable,
       "cucsSwEthLanBorderFsmStageEntry": cucsSwEthLanBorderFsmStageEntry,
       "cucsSwEthLanBorderFsmStageInstanceId": cucsSwEthLanBorderFsmStageInstanceId,
       "cucsSwEthLanBorderFsmStageDn": cucsSwEthLanBorderFsmStageDn,
       "cucsSwEthLanBorderFsmStageRn": cucsSwEthLanBorderFsmStageRn,
       "cucsSwEthLanBorderFsmStageDescrData": cucsSwEthLanBorderFsmStageDescrData,
       "cucsSwEthLanBorderFsmStageLastUpdateTime": cucsSwEthLanBorderFsmStageLastUpdateTime,
       "cucsSwEthLanBorderFsmStageName": cucsSwEthLanBorderFsmStageName,
       "cucsSwEthLanBorderFsmStageOrder": cucsSwEthLanBorderFsmStageOrder,
       "cucsSwEthLanBorderFsmStageRetry": cucsSwEthLanBorderFsmStageRetry,
       "cucsSwEthLanBorderFsmStageStageStatus": cucsSwEthLanBorderFsmStageStageStatus,
       "cucsSwEthMonFsmTable": cucsSwEthMonFsmTable,
       "cucsSwEthMonFsmEntry": cucsSwEthMonFsmEntry,
       "cucsSwEthMonFsmInstanceId": cucsSwEthMonFsmInstanceId,
       "cucsSwEthMonFsmDn": cucsSwEthMonFsmDn,
       "cucsSwEthMonFsmRn": cucsSwEthMonFsmRn,
       "cucsSwEthMonFsmCompletionTime": cucsSwEthMonFsmCompletionTime,
       "cucsSwEthMonFsmCurrentFsm": cucsSwEthMonFsmCurrentFsm,
       "cucsSwEthMonFsmDescrData": cucsSwEthMonFsmDescrData,
       "cucsSwEthMonFsmFsmStatus": cucsSwEthMonFsmFsmStatus,
       "cucsSwEthMonFsmProgress": cucsSwEthMonFsmProgress,
       "cucsSwEthMonFsmRmtErrCode": cucsSwEthMonFsmRmtErrCode,
       "cucsSwEthMonFsmRmtErrDescr": cucsSwEthMonFsmRmtErrDescr,
       "cucsSwEthMonFsmRmtRslt": cucsSwEthMonFsmRmtRslt,
       "cucsSwEthMonFsmStageTable": cucsSwEthMonFsmStageTable,
       "cucsSwEthMonFsmStageEntry": cucsSwEthMonFsmStageEntry,
       "cucsSwEthMonFsmStageInstanceId": cucsSwEthMonFsmStageInstanceId,
       "cucsSwEthMonFsmStageDn": cucsSwEthMonFsmStageDn,
       "cucsSwEthMonFsmStageRn": cucsSwEthMonFsmStageRn,
       "cucsSwEthMonFsmStageDescrData": cucsSwEthMonFsmStageDescrData,
       "cucsSwEthMonFsmStageLastUpdateTime": cucsSwEthMonFsmStageLastUpdateTime,
       "cucsSwEthMonFsmStageName": cucsSwEthMonFsmStageName,
       "cucsSwEthMonFsmStageOrder": cucsSwEthMonFsmStageOrder,
       "cucsSwEthMonFsmStageRetry": cucsSwEthMonFsmStageRetry,
       "cucsSwEthMonFsmStageStageStatus": cucsSwEthMonFsmStageStageStatus,
       "cucsSwFabricZoneNsTable": cucsSwFabricZoneNsTable,
       "cucsSwFabricZoneNsEntry": cucsSwFabricZoneNsEntry,
       "cucsSwFabricZoneNsInstanceId": cucsSwFabricZoneNsInstanceId,
       "cucsSwFabricZoneNsDn": cucsSwFabricZoneNsDn,
       "cucsSwFabricZoneNsRn": cucsSwFabricZoneNsRn,
       "cucsSwFabricZoneNsAllocStatus": cucsSwFabricZoneNsAllocStatus,
       "cucsSwFabricZoneNsLimit": cucsSwFabricZoneNsLimit,
       "cucsSwFabricZoneNsSwitchId": cucsSwFabricZoneNsSwitchId,
       "cucsSwFabricZoneNsZoneCount": cucsSwFabricZoneNsZoneCount,
       "cucsSwFabricZoneNsOverrideTable": cucsSwFabricZoneNsOverrideTable,
       "cucsSwFabricZoneNsOverrideEntry": cucsSwFabricZoneNsOverrideEntry,
       "cucsSwFabricZoneNsOverrideInstanceId": cucsSwFabricZoneNsOverrideInstanceId,
       "cucsSwFabricZoneNsOverrideDn": cucsSwFabricZoneNsOverrideDn,
       "cucsSwFabricZoneNsOverrideRn": cucsSwFabricZoneNsOverrideRn,
       "cucsSwFabricZoneNsOverrideLimit": cucsSwFabricZoneNsOverrideLimit,
       "cucsSwFcMonFsmTable": cucsSwFcMonFsmTable,
       "cucsSwFcMonFsmEntry": cucsSwFcMonFsmEntry,
       "cucsSwFcMonFsmInstanceId": cucsSwFcMonFsmInstanceId,
       "cucsSwFcMonFsmDn": cucsSwFcMonFsmDn,
       "cucsSwFcMonFsmRn": cucsSwFcMonFsmRn,
       "cucsSwFcMonFsmCompletionTime": cucsSwFcMonFsmCompletionTime,
       "cucsSwFcMonFsmCurrentFsm": cucsSwFcMonFsmCurrentFsm,
       "cucsSwFcMonFsmDescrData": cucsSwFcMonFsmDescrData,
       "cucsSwFcMonFsmFsmStatus": cucsSwFcMonFsmFsmStatus,
       "cucsSwFcMonFsmProgress": cucsSwFcMonFsmProgress,
       "cucsSwFcMonFsmRmtErrCode": cucsSwFcMonFsmRmtErrCode,
       "cucsSwFcMonFsmRmtErrDescr": cucsSwFcMonFsmRmtErrDescr,
       "cucsSwFcMonFsmRmtRslt": cucsSwFcMonFsmRmtRslt,
       "cucsSwFcMonFsmStageTable": cucsSwFcMonFsmStageTable,
       "cucsSwFcMonFsmStageEntry": cucsSwFcMonFsmStageEntry,
       "cucsSwFcMonFsmStageInstanceId": cucsSwFcMonFsmStageInstanceId,
       "cucsSwFcMonFsmStageDn": cucsSwFcMonFsmStageDn,
       "cucsSwFcMonFsmStageRn": cucsSwFcMonFsmStageRn,
       "cucsSwFcMonFsmStageDescrData": cucsSwFcMonFsmStageDescrData,
       "cucsSwFcMonFsmStageLastUpdateTime": cucsSwFcMonFsmStageLastUpdateTime,
       "cucsSwFcMonFsmStageName": cucsSwFcMonFsmStageName,
       "cucsSwFcMonFsmStageOrder": cucsSwFcMonFsmStageOrder,
       "cucsSwFcMonFsmStageRetry": cucsSwFcMonFsmStageRetry,
       "cucsSwFcMonFsmStageStageStatus": cucsSwFcMonFsmStageStageStatus,
       "cucsSwFcSanBorderFsmTable": cucsSwFcSanBorderFsmTable,
       "cucsSwFcSanBorderFsmEntry": cucsSwFcSanBorderFsmEntry,
       "cucsSwFcSanBorderFsmInstanceId": cucsSwFcSanBorderFsmInstanceId,
       "cucsSwFcSanBorderFsmDn": cucsSwFcSanBorderFsmDn,
       "cucsSwFcSanBorderFsmRn": cucsSwFcSanBorderFsmRn,
       "cucsSwFcSanBorderFsmCompletionTime": cucsSwFcSanBorderFsmCompletionTime,
       "cucsSwFcSanBorderFsmCurrentFsm": cucsSwFcSanBorderFsmCurrentFsm,
       "cucsSwFcSanBorderFsmDescrData": cucsSwFcSanBorderFsmDescrData,
       "cucsSwFcSanBorderFsmFsmStatus": cucsSwFcSanBorderFsmFsmStatus,
       "cucsSwFcSanBorderFsmProgress": cucsSwFcSanBorderFsmProgress,
       "cucsSwFcSanBorderFsmRmtErrCode": cucsSwFcSanBorderFsmRmtErrCode,
       "cucsSwFcSanBorderFsmRmtErrDescr": cucsSwFcSanBorderFsmRmtErrDescr,
       "cucsSwFcSanBorderFsmRmtRslt": cucsSwFcSanBorderFsmRmtRslt,
       "cucsSwFcSanBorderFsmStageTable": cucsSwFcSanBorderFsmStageTable,
       "cucsSwFcSanBorderFsmStageEntry": cucsSwFcSanBorderFsmStageEntry,
       "cucsSwFcSanBorderFsmStageInstanceId": cucsSwFcSanBorderFsmStageInstanceId,
       "cucsSwFcSanBorderFsmStageDn": cucsSwFcSanBorderFsmStageDn,
       "cucsSwFcSanBorderFsmStageRn": cucsSwFcSanBorderFsmStageRn,
       "cucsSwFcSanBorderFsmStageDescrData": cucsSwFcSanBorderFsmStageDescrData,
       "cucsSwFcSanBorderFsmStageLastUpdateTime": cucsSwFcSanBorderFsmStageLastUpdateTime,
       "cucsSwFcSanBorderFsmStageName": cucsSwFcSanBorderFsmStageName,
       "cucsSwFcSanBorderFsmStageOrder": cucsSwFcSanBorderFsmStageOrder,
       "cucsSwFcSanBorderFsmStageRetry": cucsSwFcSanBorderFsmStageRetry,
       "cucsSwFcSanBorderFsmStageStageStatus": cucsSwFcSanBorderFsmStageStageStatus,
       "cucsSwFcServerZoneGroupTable": cucsSwFcServerZoneGroupTable,
       "cucsSwFcServerZoneGroupEntry": cucsSwFcServerZoneGroupEntry,
       "cucsSwFcServerZoneGroupInstanceId": cucsSwFcServerZoneGroupInstanceId,
       "cucsSwFcServerZoneGroupDn": cucsSwFcServerZoneGroupDn,
       "cucsSwFcServerZoneGroupRn": cucsSwFcServerZoneGroupRn,
       "cucsSwFcServerZoneGroupEpDn": cucsSwFcServerZoneGroupEpDn,
       "cucsSwFcServerZoneGroupId": cucsSwFcServerZoneGroupId,
       "cucsSwFcServerZoneGroupLc": cucsSwFcServerZoneGroupLc,
       "cucsSwFcServerZoneGroupName": cucsSwFcServerZoneGroupName,
       "cucsSwFcServerZoneGroupPeerDn": cucsSwFcServerZoneGroupPeerDn,
       "cucsSwFcServerZoneGroupServerDn": cucsSwFcServerZoneGroupServerDn,
       "cucsSwFcZoneTable": cucsSwFcZoneTable,
       "cucsSwFcZoneEntry": cucsSwFcZoneEntry,
       "cucsSwFcZoneInstanceId": cucsSwFcZoneInstanceId,
       "cucsSwFcZoneDn": cucsSwFcZoneDn,
       "cucsSwFcZoneRn": cucsSwFcZoneRn,
       "cucsSwFcZoneId": cucsSwFcZoneId,
       "cucsSwFcZoneIdentity": cucsSwFcZoneIdentity,
       "cucsSwFcZoneLc": cucsSwFcZoneLc,
       "cucsSwFcZoneName": cucsSwFcZoneName,
       "cucsSwFcZoneOperState": cucsSwFcZoneOperState,
       "cucsSwFcZonePeerDn": cucsSwFcZonePeerDn,
       "cucsSwFcZoneSetTable": cucsSwFcZoneSetTable,
       "cucsSwFcZoneSetEntry": cucsSwFcZoneSetEntry,
       "cucsSwFcZoneSetInstanceId": cucsSwFcZoneSetInstanceId,
       "cucsSwFcZoneSetDn": cucsSwFcZoneSetDn,
       "cucsSwFcZoneSetRn": cucsSwFcZoneSetRn,
       "cucsSwFcZoneSetCurrentZonePrefix": cucsSwFcZoneSetCurrentZonePrefix,
       "cucsSwFcZoneSetLc": cucsSwFcZoneSetLc,
       "cucsSwFcZoneSetName": cucsSwFcZoneSetName,
       "cucsSwFcZoneSetOldZonePrefix": cucsSwFcZoneSetOldZonePrefix,
       "cucsSwFcoeSanEpTable": cucsSwFcoeSanEpTable,
       "cucsSwFcoeSanEpEntry": cucsSwFcoeSanEpEntry,
       "cucsSwFcoeSanEpInstanceId": cucsSwFcoeSanEpInstanceId,
       "cucsSwFcoeSanEpDn": cucsSwFcoeSanEpDn,
       "cucsSwFcoeSanEpRn": cucsSwFcoeSanEpRn,
       "cucsSwFcoeSanEpAdminSpeed": cucsSwFcoeSanEpAdminSpeed,
       "cucsSwFcoeSanEpAdminState": cucsSwFcoeSanEpAdminState,
       "cucsSwFcoeSanEpChassisId": cucsSwFcoeSanEpChassisId,
       "cucsSwFcoeSanEpEpDn": cucsSwFcoeSanEpEpDn,
       "cucsSwFcoeSanEpIfRole": cucsSwFcoeSanEpIfRole,
       "cucsSwFcoeSanEpIfType": cucsSwFcoeSanEpIfType,
       "cucsSwFcoeSanEpLc": cucsSwFcoeSanEpLc,
       "cucsSwFcoeSanEpLocale": cucsSwFcoeSanEpLocale,
       "cucsSwFcoeSanEpName": cucsSwFcoeSanEpName,
       "cucsSwFcoeSanEpPcId": cucsSwFcoeSanEpPcId,
       "cucsSwFcoeSanEpPeerChassisId": cucsSwFcoeSanEpPeerChassisId,
       "cucsSwFcoeSanEpPeerDn": cucsSwFcoeSanEpPeerDn,
       "cucsSwFcoeSanEpPeerPortId": cucsSwFcoeSanEpPeerPortId,
       "cucsSwFcoeSanEpPeerSlotId": cucsSwFcoeSanEpPeerSlotId,
       "cucsSwFcoeSanEpPeerState": cucsSwFcoeSanEpPeerState,
       "cucsSwFcoeSanEpPortId": cucsSwFcoeSanEpPortId,
       "cucsSwFcoeSanEpPortVsanId": cucsSwFcoeSanEpPortVsanId,
       "cucsSwFcoeSanEpSlotId": cucsSwFcoeSanEpSlotId,
       "cucsSwFcoeSanEpSwitchId": cucsSwFcoeSanEpSwitchId,
       "cucsSwFcoeSanEpTransport": cucsSwFcoeSanEpTransport,
       "cucsSwFcoeSanEpType": cucsSwFcoeSanEpType,
       "cucsSwFcoeSanEpUdldAdminState": cucsSwFcoeSanEpUdldAdminState,
       "cucsSwFcoeSanEpUdldMode": cucsSwFcoeSanEpUdldMode,
       "cucsSwFcoeSanEpAggrPortId": cucsSwFcoeSanEpAggrPortId,
       "cucsSwFcoeSanEpPeerAggrPortId": cucsSwFcoeSanEpPeerAggrPortId,
       "cucsSwFcoeSanEpAutoNegotiate": cucsSwFcoeSanEpAutoNegotiate,
       "cucsSwFcoeSanPcTable": cucsSwFcoeSanPcTable,
       "cucsSwFcoeSanPcEntry": cucsSwFcoeSanPcEntry,
       "cucsSwFcoeSanPcInstanceId": cucsSwFcoeSanPcInstanceId,
       "cucsSwFcoeSanPcDn": cucsSwFcoeSanPcDn,
       "cucsSwFcoeSanPcRn": cucsSwFcoeSanPcRn,
       "cucsSwFcoeSanPcAdminState": cucsSwFcoeSanPcAdminState,
       "cucsSwFcoeSanPcEpDn": cucsSwFcoeSanPcEpDn,
       "cucsSwFcoeSanPcIfRole": cucsSwFcoeSanPcIfRole,
       "cucsSwFcoeSanPcIfType": cucsSwFcoeSanPcIfType,
       "cucsSwFcoeSanPcLocale": cucsSwFcoeSanPcLocale,
       "cucsSwFcoeSanPcMonTrafDir": cucsSwFcoeSanPcMonTrafDir,
       "cucsSwFcoeSanPcName": cucsSwFcoeSanPcName,
       "cucsSwFcoeSanPcPcId": cucsSwFcoeSanPcPcId,
       "cucsSwFcoeSanPcPeerDn": cucsSwFcoeSanPcPeerDn,
       "cucsSwFcoeSanPcPeerState": cucsSwFcoeSanPcPeerState,
       "cucsSwFcoeSanPcPortId": cucsSwFcoeSanPcPortId,
       "cucsSwFcoeSanPcPortVsanId": cucsSwFcoeSanPcPortVsanId,
       "cucsSwFcoeSanPcSwitchId": cucsSwFcoeSanPcSwitchId,
       "cucsSwFcoeSanPcTransport": cucsSwFcoeSanPcTransport,
       "cucsSwFcoeSanPcType": cucsSwFcoeSanPcType,
       "cucsSwFcoeSanPcLacpFastTimer": cucsSwFcoeSanPcLacpFastTimer,
       "cucsSwFcoeSanPcLacpSuspendIndividual": cucsSwFcoeSanPcLacpSuspendIndividual,
       "cucsSwFcoeSanPcAdminSpeed": cucsSwFcoeSanPcAdminSpeed,
       "cucsSwPhysFsmTable": cucsSwPhysFsmTable,
       "cucsSwPhysFsmEntry": cucsSwPhysFsmEntry,
       "cucsSwPhysFsmInstanceId": cucsSwPhysFsmInstanceId,
       "cucsSwPhysFsmDn": cucsSwPhysFsmDn,
       "cucsSwPhysFsmRn": cucsSwPhysFsmRn,
       "cucsSwPhysFsmCompletionTime": cucsSwPhysFsmCompletionTime,
       "cucsSwPhysFsmCurrentFsm": cucsSwPhysFsmCurrentFsm,
       "cucsSwPhysFsmDescrData": cucsSwPhysFsmDescrData,
       "cucsSwPhysFsmFsmStatus": cucsSwPhysFsmFsmStatus,
       "cucsSwPhysFsmProgress": cucsSwPhysFsmProgress,
       "cucsSwPhysFsmRmtErrCode": cucsSwPhysFsmRmtErrCode,
       "cucsSwPhysFsmRmtErrDescr": cucsSwPhysFsmRmtErrDescr,
       "cucsSwPhysFsmRmtRslt": cucsSwPhysFsmRmtRslt,
       "cucsSwPhysFsmStageTable": cucsSwPhysFsmStageTable,
       "cucsSwPhysFsmStageEntry": cucsSwPhysFsmStageEntry,
       "cucsSwPhysFsmStageInstanceId": cucsSwPhysFsmStageInstanceId,
       "cucsSwPhysFsmStageDn": cucsSwPhysFsmStageDn,
       "cucsSwPhysFsmStageRn": cucsSwPhysFsmStageRn,
       "cucsSwPhysFsmStageDescrData": cucsSwPhysFsmStageDescrData,
       "cucsSwPhysFsmStageLastUpdateTime": cucsSwPhysFsmStageLastUpdateTime,
       "cucsSwPhysFsmStageName": cucsSwPhysFsmStageName,
       "cucsSwPhysFsmStageOrder": cucsSwPhysFsmStageOrder,
       "cucsSwPhysFsmStageRetry": cucsSwPhysFsmStageRetry,
       "cucsSwPhysFsmStageStageStatus": cucsSwPhysFsmStageStageStatus,
       "cucsSwUtilityDomainFsmTable": cucsSwUtilityDomainFsmTable,
       "cucsSwUtilityDomainFsmEntry": cucsSwUtilityDomainFsmEntry,
       "cucsSwUtilityDomainFsmInstanceId": cucsSwUtilityDomainFsmInstanceId,
       "cucsSwUtilityDomainFsmDn": cucsSwUtilityDomainFsmDn,
       "cucsSwUtilityDomainFsmRn": cucsSwUtilityDomainFsmRn,
       "cucsSwUtilityDomainFsmCompletionTime": cucsSwUtilityDomainFsmCompletionTime,
       "cucsSwUtilityDomainFsmCurrentFsm": cucsSwUtilityDomainFsmCurrentFsm,
       "cucsSwUtilityDomainFsmDescrData": cucsSwUtilityDomainFsmDescrData,
       "cucsSwUtilityDomainFsmFsmStatus": cucsSwUtilityDomainFsmFsmStatus,
       "cucsSwUtilityDomainFsmProgress": cucsSwUtilityDomainFsmProgress,
       "cucsSwUtilityDomainFsmRmtErrCode": cucsSwUtilityDomainFsmRmtErrCode,
       "cucsSwUtilityDomainFsmRmtErrDescr": cucsSwUtilityDomainFsmRmtErrDescr,
       "cucsSwUtilityDomainFsmRmtRslt": cucsSwUtilityDomainFsmRmtRslt,
       "cucsSwUtilityDomainFsmStageTable": cucsSwUtilityDomainFsmStageTable,
       "cucsSwUtilityDomainFsmStageEntry": cucsSwUtilityDomainFsmStageEntry,
       "cucsSwUtilityDomainFsmStageInstanceId": cucsSwUtilityDomainFsmStageInstanceId,
       "cucsSwUtilityDomainFsmStageDn": cucsSwUtilityDomainFsmStageDn,
       "cucsSwUtilityDomainFsmStageRn": cucsSwUtilityDomainFsmStageRn,
       "cucsSwUtilityDomainFsmStageDescrData": cucsSwUtilityDomainFsmStageDescrData,
       "cucsSwUtilityDomainFsmStageLastUpdateTime": cucsSwUtilityDomainFsmStageLastUpdateTime,
       "cucsSwUtilityDomainFsmStageName": cucsSwUtilityDomainFsmStageName,
       "cucsSwUtilityDomainFsmStageOrder": cucsSwUtilityDomainFsmStageOrder,
       "cucsSwUtilityDomainFsmStageRetry": cucsSwUtilityDomainFsmStageRetry,
       "cucsSwUtilityDomainFsmStageStageStatus": cucsSwUtilityDomainFsmStageStageStatus,
       "cucsSwVlanGroupTable": cucsSwVlanGroupTable,
       "cucsSwVlanGroupEntry": cucsSwVlanGroupEntry,
       "cucsSwVlanGroupInstanceId": cucsSwVlanGroupInstanceId,
       "cucsSwVlanGroupDn": cucsSwVlanGroupDn,
       "cucsSwVlanGroupRn": cucsSwVlanGroupRn,
       "cucsSwVlanGroupId": cucsSwVlanGroupId,
       "cucsSwVlanGroupPeerDn": cucsSwVlanGroupPeerDn,
       "cucsSwVlanGroupSwitchId": cucsSwVlanGroupSwitchId,
       "cucsSwVlanGroupType": cucsSwVlanGroupType,
       "cucsSwVlanGroupPvScore": cucsSwVlanGroupPvScore,
       "cucsSwVlanRefTable": cucsSwVlanRefTable,
       "cucsSwVlanRefEntry": cucsSwVlanRefEntry,
       "cucsSwVlanRefInstanceId": cucsSwVlanRefInstanceId,
       "cucsSwVlanRefDn": cucsSwVlanRefDn,
       "cucsSwVlanRefRn": cucsSwVlanRefRn,
       "cucsSwVlanRefCompressionType": cucsSwVlanRefCompressionType,
       "cucsSwVlanRefConfigStatus": cucsSwVlanRefConfigStatus,
       "cucsSwVlanRefId": cucsSwVlanRefId,
       "cucsSwVlanRefPeerDn": cucsSwVlanRefPeerDn,
       "cucsSwZoneInitiatorMemberTable": cucsSwZoneInitiatorMemberTable,
       "cucsSwZoneInitiatorMemberEntry": cucsSwZoneInitiatorMemberEntry,
       "cucsSwZoneInitiatorMemberInstanceId": cucsSwZoneInitiatorMemberInstanceId,
       "cucsSwZoneInitiatorMemberDn": cucsSwZoneInitiatorMemberDn,
       "cucsSwZoneInitiatorMemberRn": cucsSwZoneInitiatorMemberRn,
       "cucsSwZoneInitiatorMemberEpDn": cucsSwZoneInitiatorMemberEpDn,
       "cucsSwZoneInitiatorMemberLc": cucsSwZoneInitiatorMemberLc,
       "cucsSwZoneInitiatorMemberName": cucsSwZoneInitiatorMemberName,
       "cucsSwZoneInitiatorMemberPeerDn": cucsSwZoneInitiatorMemberPeerDn,
       "cucsSwZoneInitiatorMemberWwpn": cucsSwZoneInitiatorMemberWwpn,
       "cucsSwZoneTargetMemberTable": cucsSwZoneTargetMemberTable,
       "cucsSwZoneTargetMemberEntry": cucsSwZoneTargetMemberEntry,
       "cucsSwZoneTargetMemberInstanceId": cucsSwZoneTargetMemberInstanceId,
       "cucsSwZoneTargetMemberDn": cucsSwZoneTargetMemberDn,
       "cucsSwZoneTargetMemberRn": cucsSwZoneTargetMemberRn,
       "cucsSwZoneTargetMemberEpDn": cucsSwZoneTargetMemberEpDn,
       "cucsSwZoneTargetMemberLc": cucsSwZoneTargetMemberLc,
       "cucsSwZoneTargetMemberName": cucsSwZoneTargetMemberName,
       "cucsSwZoneTargetMemberPeerDn": cucsSwZoneTargetMemberPeerDn,
       "cucsSwZoneTargetMemberWwpn": cucsSwZoneTargetMemberWwpn,
       "cucsSwCmclanTable": cucsSwCmclanTable,
       "cucsSwCmclanEntry": cucsSwCmclanEntry,
       "cucsSwCmclanInstanceId": cucsSwCmclanInstanceId,
       "cucsSwCmclanDn": cucsSwCmclanDn,
       "cucsSwCmclanRn": cucsSwCmclanRn,
       "cucsSwCmclanCimcIds": cucsSwCmclanCimcIds,
       "cucsSwCmclanEpDn": cucsSwCmclanEpDn,
       "cucsSwCmclanId": cucsSwCmclanId,
       "cucsSwCmclanIfRole": cucsSwCmclanIfRole,
       "cucsSwCmclanIfType": cucsSwCmclanIfType,
       "cucsSwCmclanLocale": cucsSwCmclanLocale,
       "cucsSwCmclanName": cucsSwCmclanName,
       "cucsSwCmclanPeerDn": cucsSwCmclanPeerDn,
       "cucsSwCmclanTransport": cucsSwCmclanTransport,
       "cucsSwCmclanType": cucsSwCmclanType,
       "cucsSwEthLanFlowMonTable": cucsSwEthLanFlowMonTable,
       "cucsSwEthLanFlowMonEntry": cucsSwEthLanFlowMonEntry,
       "cucsSwEthLanFlowMonInstanceId": cucsSwEthLanFlowMonInstanceId,
       "cucsSwEthLanFlowMonDn": cucsSwEthLanFlowMonDn,
       "cucsSwEthLanFlowMonRn": cucsSwEthLanFlowMonRn,
       "cucsSwEthLanFlowMonFsmDescr": cucsSwEthLanFlowMonFsmDescr,
       "cucsSwEthLanFlowMonFsmPrev": cucsSwEthLanFlowMonFsmPrev,
       "cucsSwEthLanFlowMonFsmProgr": cucsSwEthLanFlowMonFsmProgr,
       "cucsSwEthLanFlowMonFsmRmtInvErrCode": cucsSwEthLanFlowMonFsmRmtInvErrCode,
       "cucsSwEthLanFlowMonFsmRmtInvErrDescr": cucsSwEthLanFlowMonFsmRmtInvErrDescr,
       "cucsSwEthLanFlowMonFsmRmtInvRslt": cucsSwEthLanFlowMonFsmRmtInvRslt,
       "cucsSwEthLanFlowMonFsmStageDescr": cucsSwEthLanFlowMonFsmStageDescr,
       "cucsSwEthLanFlowMonFsmStamp": cucsSwEthLanFlowMonFsmStamp,
       "cucsSwEthLanFlowMonFsmStatus": cucsSwEthLanFlowMonFsmStatus,
       "cucsSwEthLanFlowMonFsmTry": cucsSwEthLanFlowMonFsmTry,
       "cucsSwEthLanFlowMonLocale": cucsSwEthLanFlowMonLocale,
       "cucsSwEthLanFlowMonName": cucsSwEthLanFlowMonName,
       "cucsSwEthLanFlowMonNetflowActiveTimeout": cucsSwEthLanFlowMonNetflowActiveTimeout,
       "cucsSwEthLanFlowMonNetflowInactiveTimeout": cucsSwEthLanFlowMonNetflowInactiveTimeout,
       "cucsSwEthLanFlowMonSwitchId": cucsSwEthLanFlowMonSwitchId,
       "cucsSwEthLanFlowMonTransport": cucsSwEthLanFlowMonTransport,
       "cucsSwEthLanFlowMonType": cucsSwEthLanFlowMonType,
       "cucsSwEthLanFlowMonFsmTable": cucsSwEthLanFlowMonFsmTable,
       "cucsSwEthLanFlowMonFsmEntry": cucsSwEthLanFlowMonFsmEntry,
       "cucsSwEthLanFlowMonFsmInstanceId": cucsSwEthLanFlowMonFsmInstanceId,
       "cucsSwEthLanFlowMonFsmDn": cucsSwEthLanFlowMonFsmDn,
       "cucsSwEthLanFlowMonFsmRn": cucsSwEthLanFlowMonFsmRn,
       "cucsSwEthLanFlowMonFsmCompletionTime": cucsSwEthLanFlowMonFsmCompletionTime,
       "cucsSwEthLanFlowMonFsmCurrentFsm": cucsSwEthLanFlowMonFsmCurrentFsm,
       "cucsSwEthLanFlowMonFsmDescrData": cucsSwEthLanFlowMonFsmDescrData,
       "cucsSwEthLanFlowMonFsmFsmStatus": cucsSwEthLanFlowMonFsmFsmStatus,
       "cucsSwEthLanFlowMonFsmProgress": cucsSwEthLanFlowMonFsmProgress,
       "cucsSwEthLanFlowMonFsmRmtErrCode": cucsSwEthLanFlowMonFsmRmtErrCode,
       "cucsSwEthLanFlowMonFsmRmtErrDescr": cucsSwEthLanFlowMonFsmRmtErrDescr,
       "cucsSwEthLanFlowMonFsmRmtRslt": cucsSwEthLanFlowMonFsmRmtRslt,
       "cucsSwEthLanFlowMonFsmStageTable": cucsSwEthLanFlowMonFsmStageTable,
       "cucsSwEthLanFlowMonFsmStageEntry": cucsSwEthLanFlowMonFsmStageEntry,
       "cucsSwEthLanFlowMonFsmStageInstanceId": cucsSwEthLanFlowMonFsmStageInstanceId,
       "cucsSwEthLanFlowMonFsmStageDn": cucsSwEthLanFlowMonFsmStageDn,
       "cucsSwEthLanFlowMonFsmStageRn": cucsSwEthLanFlowMonFsmStageRn,
       "cucsSwEthLanFlowMonFsmStageDescrData": cucsSwEthLanFlowMonFsmStageDescrData,
       "cucsSwEthLanFlowMonFsmStageLastUpdateTime": cucsSwEthLanFlowMonFsmStageLastUpdateTime,
       "cucsSwEthLanFlowMonFsmStageName": cucsSwEthLanFlowMonFsmStageName,
       "cucsSwEthLanFlowMonFsmStageOrder": cucsSwEthLanFlowMonFsmStageOrder,
       "cucsSwEthLanFlowMonFsmStageRetry": cucsSwEthLanFlowMonFsmStageRetry,
       "cucsSwEthLanFlowMonFsmStageStageStatus": cucsSwEthLanFlowMonFsmStageStageStatus,
       "cucsSwEthLanFlowMonFsmTaskTable": cucsSwEthLanFlowMonFsmTaskTable,
       "cucsSwEthLanFlowMonFsmTaskEntry": cucsSwEthLanFlowMonFsmTaskEntry,
       "cucsSwEthLanFlowMonFsmTaskInstanceId": cucsSwEthLanFlowMonFsmTaskInstanceId,
       "cucsSwEthLanFlowMonFsmTaskDn": cucsSwEthLanFlowMonFsmTaskDn,
       "cucsSwEthLanFlowMonFsmTaskRn": cucsSwEthLanFlowMonFsmTaskRn,
       "cucsSwEthLanFlowMonFsmTaskCompletion": cucsSwEthLanFlowMonFsmTaskCompletion,
       "cucsSwEthLanFlowMonFsmTaskFlags": cucsSwEthLanFlowMonFsmTaskFlags,
       "cucsSwEthLanFlowMonFsmTaskItem": cucsSwEthLanFlowMonFsmTaskItem,
       "cucsSwEthLanFlowMonFsmTaskSeqId": cucsSwEthLanFlowMonFsmTaskSeqId,
       "cucsSwIpRouteTable": cucsSwIpRouteTable,
       "cucsSwIpRouteEntry": cucsSwIpRouteEntry,
       "cucsSwIpRouteInstanceId": cucsSwIpRouteInstanceId,
       "cucsSwIpRouteDn": cucsSwIpRouteDn,
       "cucsSwIpRouteRn": cucsSwIpRouteRn,
       "cucsSwIpRouteDestinationIp": cucsSwIpRouteDestinationIp,
       "cucsSwIpRouteDestinationNetmask": cucsSwIpRouteDestinationNetmask,
       "cucsSwIpRouteName": cucsSwIpRouteName,
       "cucsSwIpRoutePeerDn": cucsSwIpRoutePeerDn,
       "cucsSwIpRoutePrefix": cucsSwIpRoutePrefix,
       "cucsSwIpRouteRouteIP": cucsSwIpRouteRouteIP,
       "cucsSwIpRouteSwitchId": cucsSwIpRouteSwitchId,
       "cucsSwNFExporterRefTable": cucsSwNFExporterRefTable,
       "cucsSwNFExporterRefEntry": cucsSwNFExporterRefEntry,
       "cucsSwNFExporterRefInstanceId": cucsSwNFExporterRefInstanceId,
       "cucsSwNFExporterRefDn": cucsSwNFExporterRefDn,
       "cucsSwNFExporterRefRn": cucsSwNFExporterRefRn,
       "cucsSwNFExporterRefName": cucsSwNFExporterRefName,
       "cucsSwNFExporterRefPeerDn": cucsSwNFExporterRefPeerDn,
       "cucsSwNetflowExporterTable": cucsSwNetflowExporterTable,
       "cucsSwNetflowExporterEntry": cucsSwNetflowExporterEntry,
       "cucsSwNetflowExporterInstanceId": cucsSwNetflowExporterInstanceId,
       "cucsSwNetflowExporterDn": cucsSwNetflowExporterDn,
       "cucsSwNetflowExporterRn": cucsSwNetflowExporterRn,
       "cucsSwNetflowExporterDestinationIpAddress": cucsSwNetflowExporterDestinationIpAddress,
       "cucsSwNetflowExporterDestinationPort": cucsSwNetflowExporterDestinationPort,
       "cucsSwNetflowExporterDscp": cucsSwNetflowExporterDscp,
       "cucsSwNetflowExporterExportInternal": cucsSwNetflowExporterExportInternal,
       "cucsSwNetflowExporterExporterStatsTimeout": cucsSwNetflowExporterExporterStatsTimeout,
       "cucsSwNetflowExporterInterfaceTableTimeout": cucsSwNetflowExporterInterfaceTableTimeout,
       "cucsSwNetflowExporterIsValidConfig": cucsSwNetflowExporterIsValidConfig,
       "cucsSwNetflowExporterLifeCycle": cucsSwNetflowExporterLifeCycle,
       "cucsSwNetflowExporterName": cucsSwNetflowExporterName,
       "cucsSwNetflowExporterPeerDn": cucsSwNetflowExporterPeerDn,
       "cucsSwNetflowExporterProtocol": cucsSwNetflowExporterProtocol,
       "cucsSwNetflowExporterSourceVlan": cucsSwNetflowExporterSourceVlan,
       "cucsSwNetflowExporterSwitchId": cucsSwNetflowExporterSwitchId,
       "cucsSwNetflowExporterTemplateDataTimeout": cucsSwNetflowExporterTemplateDataTimeout,
       "cucsSwNetflowExporterTransport": cucsSwNetflowExporterTransport,
       "cucsSwNetflowExporterTransportProtocol": cucsSwNetflowExporterTransportProtocol,
       "cucsSwNetflowExporterType": cucsSwNetflowExporterType,
       "cucsSwNetflowExporterVersion": cucsSwNetflowExporterVersion,
       "cucsSwNetflowMonSessionTable": cucsSwNetflowMonSessionTable,
       "cucsSwNetflowMonSessionEntry": cucsSwNetflowMonSessionEntry,
       "cucsSwNetflowMonSessionInstanceId": cucsSwNetflowMonSessionInstanceId,
       "cucsSwNetflowMonSessionDn": cucsSwNetflowMonSessionDn,
       "cucsSwNetflowMonSessionRn": cucsSwNetflowMonSessionRn,
       "cucsSwNetflowMonSessionAdminState": cucsSwNetflowMonSessionAdminState,
       "cucsSwNetflowMonSessionHasLastDest": cucsSwNetflowMonSessionHasLastDest,
       "cucsSwNetflowMonSessionLifeCycle": cucsSwNetflowMonSessionLifeCycle,
       "cucsSwNetflowMonSessionName": cucsSwNetflowMonSessionName,
       "cucsSwNetflowMonSessionPeerDn": cucsSwNetflowMonSessionPeerDn,
       "cucsSwNetflowMonSessionProtocol": cucsSwNetflowMonSessionProtocol,
       "cucsSwNetflowMonSessionSession": cucsSwNetflowMonSessionSession,
       "cucsSwNetflowMonSessionSwitchId": cucsSwNetflowMonSessionSwitchId,
       "cucsSwNetflowMonSessionTransport": cucsSwNetflowMonSessionTransport,
       "cucsSwNetflowMonSessionType": cucsSwNetflowMonSessionType,
       "cucsSwNetflowMonitorTable": cucsSwNetflowMonitorTable,
       "cucsSwNetflowMonitorEntry": cucsSwNetflowMonitorEntry,
       "cucsSwNetflowMonitorInstanceId": cucsSwNetflowMonitorInstanceId,
       "cucsSwNetflowMonitorDn": cucsSwNetflowMonitorDn,
       "cucsSwNetflowMonitorRn": cucsSwNetflowMonitorRn,
       "cucsSwNetflowMonitorActiveTimeout": cucsSwNetflowMonitorActiveTimeout,
       "cucsSwNetflowMonitorAdminState": cucsSwNetflowMonitorAdminState,
       "cucsSwNetflowMonitorFlowRecordDefName": cucsSwNetflowMonitorFlowRecordDefName,
       "cucsSwNetflowMonitorInactiveTimeout": cucsSwNetflowMonitorInactiveTimeout,
       "cucsSwNetflowMonitorIsValidConfig": cucsSwNetflowMonitorIsValidConfig,
       "cucsSwNetflowMonitorLifeCycle": cucsSwNetflowMonitorLifeCycle,
       "cucsSwNetflowMonitorName": cucsSwNetflowMonitorName,
       "cucsSwNetflowMonitorPeerDn": cucsSwNetflowMonitorPeerDn,
       "cucsSwNetflowMonitorProtocol": cucsSwNetflowMonitorProtocol,
       "cucsSwNetflowMonitorSwitchId": cucsSwNetflowMonitorSwitchId,
       "cucsSwNetflowMonitorTransport": cucsSwNetflowMonitorTransport,
       "cucsSwNetflowMonitorType": cucsSwNetflowMonitorType,
       "cucsSwNetflowMonitorRefTable": cucsSwNetflowMonitorRefTable,
       "cucsSwNetflowMonitorRefEntry": cucsSwNetflowMonitorRefEntry,
       "cucsSwNetflowMonitorRefInstanceId": cucsSwNetflowMonitorRefInstanceId,
       "cucsSwNetflowMonitorRefDn": cucsSwNetflowMonitorRefDn,
       "cucsSwNetflowMonitorRefRn": cucsSwNetflowMonitorRefRn,
       "cucsSwNetflowMonitorRefDirection": cucsSwNetflowMonitorRefDirection,
       "cucsSwNetflowMonitorRefKeyType": cucsSwNetflowMonitorRefKeyType,
       "cucsSwNetflowMonitorRefName": cucsSwNetflowMonitorRefName,
       "cucsSwNetflowMonitorRefSourceDn": cucsSwNetflowMonitorRefSourceDn,
       "cucsSwNetflowRecordDefTable": cucsSwNetflowRecordDefTable,
       "cucsSwNetflowRecordDefEntry": cucsSwNetflowRecordDefEntry,
       "cucsSwNetflowRecordDefInstanceId": cucsSwNetflowRecordDefInstanceId,
       "cucsSwNetflowRecordDefDn": cucsSwNetflowRecordDefDn,
       "cucsSwNetflowRecordDefRn": cucsSwNetflowRecordDefRn,
       "cucsSwNetflowRecordDefIpv4keys": cucsSwNetflowRecordDefIpv4keys,
       "cucsSwNetflowRecordDefIpv6keys": cucsSwNetflowRecordDefIpv6keys,
       "cucsSwNetflowRecordDefKeyType": cucsSwNetflowRecordDefKeyType,
       "cucsSwNetflowRecordDefL2keys": cucsSwNetflowRecordDefL2keys,
       "cucsSwNetflowRecordDefLifeCycle": cucsSwNetflowRecordDefLifeCycle,
       "cucsSwNetflowRecordDefName": cucsSwNetflowRecordDefName,
       "cucsSwNetflowRecordDefNonkeys": cucsSwNetflowRecordDefNonkeys,
       "cucsSwNetflowRecordDefPeerDn": cucsSwNetflowRecordDefPeerDn,
       "cucsSwNetflowRecordDefProtocol": cucsSwNetflowRecordDefProtocol,
       "cucsSwNetflowRecordDefSwitchId": cucsSwNetflowRecordDefSwitchId,
       "cucsSwNetflowRecordDefTransport": cucsSwNetflowRecordDefTransport,
       "cucsSwNetflowRecordDefType": cucsSwNetflowRecordDefType,
       "cucsSwVirtL3IntfTable": cucsSwVirtL3IntfTable,
       "cucsSwVirtL3IntfEntry": cucsSwVirtL3IntfEntry,
       "cucsSwVirtL3IntfInstanceId": cucsSwVirtL3IntfInstanceId,
       "cucsSwVirtL3IntfDn": cucsSwVirtL3IntfDn,
       "cucsSwVirtL3IntfRn": cucsSwVirtL3IntfRn,
       "cucsSwVirtL3IntfIpAddress": cucsSwVirtL3IntfIpAddress,
       "cucsSwVirtL3IntfName": cucsSwVirtL3IntfName,
       "cucsSwVirtL3IntfNetmask": cucsSwVirtL3IntfNetmask,
       "cucsSwVirtL3IntfVlanId": cucsSwVirtL3IntfVlanId,
       "cucsSwSubGroupTable": cucsSwSubGroupTable,
       "cucsSwSubGroupEntry": cucsSwSubGroupEntry,
       "cucsSwSubGroupInstanceId": cucsSwSubGroupInstanceId,
       "cucsSwSubGroupDn": cucsSwSubGroupDn,
       "cucsSwSubGroupRn": cucsSwSubGroupRn,
       "cucsSwSubGroupAggrPortId": cucsSwSubGroupAggrPortId,
       "cucsSwSubGroupLicGP": cucsSwSubGroupLicGP,
       "cucsSwSubGroupLicState": cucsSwSubGroupLicState,
       "cucsSwSubGroupLocale": cucsSwSubGroupLocale,
       "cucsSwSubGroupName": cucsSwSubGroupName,
       "cucsSwSubGroupSlotId": cucsSwSubGroupSlotId,
       "cucsSwSubGroupSwitchId": cucsSwSubGroupSwitchId,
       "cucsSwSubGroupTransport": cucsSwSubGroupTransport,
       "cucsSwSubGroupType": cucsSwSubGroupType,
       "cucsSwExtUtilityTable": cucsSwExtUtilityTable,
       "cucsSwExtUtilityEntry": cucsSwExtUtilityEntry,
       "cucsSwExtUtilityInstanceId": cucsSwExtUtilityInstanceId,
       "cucsSwExtUtilityDn": cucsSwExtUtilityDn,
       "cucsSwExtUtilityRn": cucsSwExtUtilityRn,
       "cucsSwExtUtilityConfMode": cucsSwExtUtilityConfMode,
       "cucsSwExtUtilityFsmDescr": cucsSwExtUtilityFsmDescr,
       "cucsSwExtUtilityFsmPrev": cucsSwExtUtilityFsmPrev,
       "cucsSwExtUtilityFsmProgr": cucsSwExtUtilityFsmProgr,
       "cucsSwExtUtilityFsmRmtInvErrCode": cucsSwExtUtilityFsmRmtInvErrCode,
       "cucsSwExtUtilityFsmRmtInvErrDescr": cucsSwExtUtilityFsmRmtInvErrDescr,
       "cucsSwExtUtilityFsmRmtInvRslt": cucsSwExtUtilityFsmRmtInvRslt,
       "cucsSwExtUtilityFsmStageDescr": cucsSwExtUtilityFsmStageDescr,
       "cucsSwExtUtilityFsmStamp": cucsSwExtUtilityFsmStamp,
       "cucsSwExtUtilityFsmStatus": cucsSwExtUtilityFsmStatus,
       "cucsSwExtUtilityFsmTry": cucsSwExtUtilityFsmTry,
       "cucsSwExtUtilitySwitchId": cucsSwExtUtilitySwitchId,
       "cucsSwExtUtilityFsmTable": cucsSwExtUtilityFsmTable,
       "cucsSwExtUtilityFsmEntry": cucsSwExtUtilityFsmEntry,
       "cucsSwExtUtilityFsmInstanceId": cucsSwExtUtilityFsmInstanceId,
       "cucsSwExtUtilityFsmDn": cucsSwExtUtilityFsmDn,
       "cucsSwExtUtilityFsmRn": cucsSwExtUtilityFsmRn,
       "cucsSwExtUtilityFsmCompletionTime": cucsSwExtUtilityFsmCompletionTime,
       "cucsSwExtUtilityFsmCurrentFsm": cucsSwExtUtilityFsmCurrentFsm,
       "cucsSwExtUtilityFsmDescrData": cucsSwExtUtilityFsmDescrData,
       "cucsSwExtUtilityFsmFsmStatus": cucsSwExtUtilityFsmFsmStatus,
       "cucsSwExtUtilityFsmProgress": cucsSwExtUtilityFsmProgress,
       "cucsSwExtUtilityFsmRmtErrCode": cucsSwExtUtilityFsmRmtErrCode,
       "cucsSwExtUtilityFsmRmtErrDescr": cucsSwExtUtilityFsmRmtErrDescr,
       "cucsSwExtUtilityFsmRmtRslt": cucsSwExtUtilityFsmRmtRslt,
       "cucsSwExtUtilityFsmStageTable": cucsSwExtUtilityFsmStageTable,
       "cucsSwExtUtilityFsmStageEntry": cucsSwExtUtilityFsmStageEntry,
       "cucsSwExtUtilityFsmStageInstanceId": cucsSwExtUtilityFsmStageInstanceId,
       "cucsSwExtUtilityFsmStageDn": cucsSwExtUtilityFsmStageDn,
       "cucsSwExtUtilityFsmStageRn": cucsSwExtUtilityFsmStageRn,
       "cucsSwExtUtilityFsmStageDescrData": cucsSwExtUtilityFsmStageDescrData,
       "cucsSwExtUtilityFsmStageLastUpdateTime": cucsSwExtUtilityFsmStageLastUpdateTime,
       "cucsSwExtUtilityFsmStageName": cucsSwExtUtilityFsmStageName,
       "cucsSwExtUtilityFsmStageOrder": cucsSwExtUtilityFsmStageOrder,
       "cucsSwExtUtilityFsmStageRetry": cucsSwExtUtilityFsmStageRetry,
       "cucsSwExtUtilityFsmStageStageStatus": cucsSwExtUtilityFsmStageStageStatus,
       "cucsSwExtUtilityFsmTaskTable": cucsSwExtUtilityFsmTaskTable,
       "cucsSwExtUtilityFsmTaskEntry": cucsSwExtUtilityFsmTaskEntry,
       "cucsSwExtUtilityFsmTaskInstanceId": cucsSwExtUtilityFsmTaskInstanceId,
       "cucsSwExtUtilityFsmTaskDn": cucsSwExtUtilityFsmTaskDn,
       "cucsSwExtUtilityFsmTaskRn": cucsSwExtUtilityFsmTaskRn,
       "cucsSwExtUtilityFsmTaskCompletion": cucsSwExtUtilityFsmTaskCompletion,
       "cucsSwExtUtilityFsmTaskFlags": cucsSwExtUtilityFsmTaskFlags,
       "cucsSwExtUtilityFsmTaskItem": cucsSwExtUtilityFsmTaskItem,
       "cucsSwExtUtilityFsmTaskSeqId": cucsSwExtUtilityFsmTaskSeqId,
       "cucsSwPortBreakoutTable": cucsSwPortBreakoutTable,
       "cucsSwPortBreakoutEntry": cucsSwPortBreakoutEntry,
       "cucsSwPortBreakoutInstanceId": cucsSwPortBreakoutInstanceId,
       "cucsSwPortBreakoutDn": cucsSwPortBreakoutDn,
       "cucsSwPortBreakoutRn": cucsSwPortBreakoutRn,
       "cucsSwPortBreakoutBreakoutType": cucsSwPortBreakoutBreakoutType,
       "cucsSwPortBreakoutPortId": cucsSwPortBreakoutPortId,
       "cucsSwPortBreakoutSlotId": cucsSwPortBreakoutSlotId,
       "cucsSwVIFRefTable": cucsSwVIFRefTable,
       "cucsSwVIFRefEntry": cucsSwVIFRefEntry,
       "cucsSwVIFRefInstanceId": cucsSwVIFRefInstanceId,
       "cucsSwVIFRefDn": cucsSwVIFRefDn,
       "cucsSwVIFRefRn": cucsSwVIFRefRn,
       "cucsSwVIFRefId": cucsSwVIFRefId,
       "cucsSwVIFRefPeerDn": cucsSwVIFRefPeerDn}
)
