# SNMP MIB module (CISCO-FIREPOWER-COMPUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-COMPUTE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:10 2025
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

(CfprComputeABoardPower,
 CfprComputeAdminLinkAggregation,
 CfprComputeAdminMemoryState,
 CfprComputeAdminPowerState,
 CfprComputeAdminState,
 CfprComputeAdminTrigger,
 CfprComputeAlarmSeverity,
 CfprComputeAssociation,
 CfprComputeAvailability,
 CfprComputeBlackListing,
 CfprComputeBladeFsmCurrentFsm,
 CfprComputeBladeFsmStageName,
 CfprComputeBladeFsmTaskFlags,
 CfprComputeBladeFsmTaskItem,
 CfprComputeBladeSlotId,
 CfprComputeChassisConnPolicyChassisId,
 CfprComputeChassisDiscAction,
 CfprComputeChassisQualMaxId,
 CfprComputeChassisQualMinId,
 CfprComputeCheckPoint,
 CfprComputeConnectivityRebalancing,
 CfprComputeDiscovery,
 CfprComputeIOHubEnvStatsHistThresholded,
 CfprComputeIOHubEnvStatsThresholded,
 CfprComputeIssues,
 CfprComputeKvmMgmtPolicyVmediaEncryption,
 CfprComputeLinkAggregation,
 CfprComputeMbPowerStatsHistThresholded,
 CfprComputeMbPowerStatsThresholded,
 CfprComputeMbTempStatsHistThresholded,
 CfprComputeMbTempStatsThresholded,
 CfprComputeMemoryUnitConstraintType,
 CfprComputeMode,
 CfprComputeOwner,
 CfprComputePCIeFatalCompletionStatsThresholded,
 CfprComputePCIeFatalProtocolStatsThresholded,
 CfprComputePCIeFatalReceiveStatsThresholded,
 CfprComputePCIeFatalStatsThresholded,
 CfprComputePciCapOrder,
 CfprComputePhysicalFsmCurrentFsm,
 CfprComputePhysicalFsmStageName,
 CfprComputePhysicalFsmTaskFlags,
 CfprComputePhysicalFsmTaskItem,
 CfprComputePhysicalLowVoltageMemory,
 CfprComputePooledRackUnitId,
 CfprComputePooledSlotSlotId,
 CfprComputePsuClusterState,
 CfprComputePsuControlRedundancy,
 CfprComputePsuRedundancy,
 CfprComputePsuRedundancyOperQualifier,
 CfprComputePsuRedundancyOperState,
 CfprComputeRackQualMaxId,
 CfprComputeRackQualMinId,
 CfprComputeRackUnitFsmCurrentFsm,
 CfprComputeRackUnitFsmStageName,
 CfprComputeRackUnitFsmTaskFlags,
 CfprComputeRackUnitFsmTaskItem,
 CfprComputeRackUnitId,
 CfprComputeRackUnitMbTempStatsHistThresholded,
 CfprComputeRackUnitMbTempStatsThresholded,
 CfprComputeScrubAction,
 CfprComputeServerDiscPolicyFsmCurrentFsm,
 CfprComputeServerDiscPolicyFsmStageName,
 CfprComputeServerDiscPolicyFsmTaskItem,
 CfprComputeServerMgmtDiscAction,
 CfprComputeSlotQualMaxId,
 CfprComputeSlotQualMinId,
 CfprComputeUpgradeStatus,
 CfprConditionRemoteInvRslt,
 CfprEquipmentBiosPostState,
 CfprEquipmentBoardAggregationRole,
 CfprEquipmentBoardConnectorType,
 CfprEquipmentConnectionStatus,
 CfprEquipmentCpuType,
 CfprEquipmentOperability,
 CfprEquipmentPowerState,
 CfprEquipmentPresence,
 CfprEquipmentSensorThresholdStatus,
 CfprEquipmentSlotStatus,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprLsOperState,
 CfprNetworkSwitchId,
 CfprPolicyPolicyOwner,
 CfprPoolPoolAssignmentOrder,
 CfprTrigAckChangeDetails,
 CfprTrigAckChanges,
 CfprTrigAckDisr,
 CfprTrigAckOperState,
 CfprTrigAckPrevOperState,
 CfprTrigAdminState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprComputeABoardPower",
    "CfprComputeAdminLinkAggregation",
    "CfprComputeAdminMemoryState",
    "CfprComputeAdminPowerState",
    "CfprComputeAdminState",
    "CfprComputeAdminTrigger",
    "CfprComputeAlarmSeverity",
    "CfprComputeAssociation",
    "CfprComputeAvailability",
    "CfprComputeBlackListing",
    "CfprComputeBladeFsmCurrentFsm",
    "CfprComputeBladeFsmStageName",
    "CfprComputeBladeFsmTaskFlags",
    "CfprComputeBladeFsmTaskItem",
    "CfprComputeBladeSlotId",
    "CfprComputeChassisConnPolicyChassisId",
    "CfprComputeChassisDiscAction",
    "CfprComputeChassisQualMaxId",
    "CfprComputeChassisQualMinId",
    "CfprComputeCheckPoint",
    "CfprComputeConnectivityRebalancing",
    "CfprComputeDiscovery",
    "CfprComputeIOHubEnvStatsHistThresholded",
    "CfprComputeIOHubEnvStatsThresholded",
    "CfprComputeIssues",
    "CfprComputeKvmMgmtPolicyVmediaEncryption",
    "CfprComputeLinkAggregation",
    "CfprComputeMbPowerStatsHistThresholded",
    "CfprComputeMbPowerStatsThresholded",
    "CfprComputeMbTempStatsHistThresholded",
    "CfprComputeMbTempStatsThresholded",
    "CfprComputeMemoryUnitConstraintType",
    "CfprComputeMode",
    "CfprComputeOwner",
    "CfprComputePCIeFatalCompletionStatsThresholded",
    "CfprComputePCIeFatalProtocolStatsThresholded",
    "CfprComputePCIeFatalReceiveStatsThresholded",
    "CfprComputePCIeFatalStatsThresholded",
    "CfprComputePciCapOrder",
    "CfprComputePhysicalFsmCurrentFsm",
    "CfprComputePhysicalFsmStageName",
    "CfprComputePhysicalFsmTaskFlags",
    "CfprComputePhysicalFsmTaskItem",
    "CfprComputePhysicalLowVoltageMemory",
    "CfprComputePooledRackUnitId",
    "CfprComputePooledSlotSlotId",
    "CfprComputePsuClusterState",
    "CfprComputePsuControlRedundancy",
    "CfprComputePsuRedundancy",
    "CfprComputePsuRedundancyOperQualifier",
    "CfprComputePsuRedundancyOperState",
    "CfprComputeRackQualMaxId",
    "CfprComputeRackQualMinId",
    "CfprComputeRackUnitFsmCurrentFsm",
    "CfprComputeRackUnitFsmStageName",
    "CfprComputeRackUnitFsmTaskFlags",
    "CfprComputeRackUnitFsmTaskItem",
    "CfprComputeRackUnitId",
    "CfprComputeRackUnitMbTempStatsHistThresholded",
    "CfprComputeRackUnitMbTempStatsThresholded",
    "CfprComputeScrubAction",
    "CfprComputeServerDiscPolicyFsmCurrentFsm",
    "CfprComputeServerDiscPolicyFsmStageName",
    "CfprComputeServerDiscPolicyFsmTaskItem",
    "CfprComputeServerMgmtDiscAction",
    "CfprComputeSlotQualMaxId",
    "CfprComputeSlotQualMinId",
    "CfprComputeUpgradeStatus",
    "CfprConditionRemoteInvRslt",
    "CfprEquipmentBiosPostState",
    "CfprEquipmentBoardAggregationRole",
    "CfprEquipmentBoardConnectorType",
    "CfprEquipmentConnectionStatus",
    "CfprEquipmentCpuType",
    "CfprEquipmentOperability",
    "CfprEquipmentPowerState",
    "CfprEquipmentPresence",
    "CfprEquipmentSensorThresholdStatus",
    "CfprEquipmentSlotStatus",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprLsOperState",
    "CfprNetworkSwitchId",
    "CfprPolicyPolicyOwner",
    "CfprPoolPoolAssignmentOrder",
    "CfprTrigAckChangeDetails",
    "CfprTrigAckChanges",
    "CfprTrigAckDisr",
    "CfprTrigAckOperState",
    "CfprTrigAckPrevOperState",
    "CfprTrigAdminState")

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

cfprComputeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprComputeAutoconfigPolicyTable_Object = MibTable
cfprComputeAutoconfigPolicyTable = _CfprComputeAutoconfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyTable.setStatus("current")
_CfprComputeAutoconfigPolicyEntry_Object = MibTableRow
cfprComputeAutoconfigPolicyEntry = _CfprComputeAutoconfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1)
)
cfprComputeAutoconfigPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeAutoconfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyEntry.setStatus("current")
_CfprComputeAutoconfigPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeAutoconfigPolicyInstanceId_Object = MibTableColumn
cfprComputeAutoconfigPolicyInstanceId = _CfprComputeAutoconfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 1),
    _CfprComputeAutoconfigPolicyInstanceId_Type()
)
cfprComputeAutoconfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyInstanceId.setStatus("current")
_CfprComputeAutoconfigPolicyDn_Type = CfprManagedObjectDn
_CfprComputeAutoconfigPolicyDn_Object = MibTableColumn
cfprComputeAutoconfigPolicyDn = _CfprComputeAutoconfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 2),
    _CfprComputeAutoconfigPolicyDn_Type()
)
cfprComputeAutoconfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyDn.setStatus("current")
_CfprComputeAutoconfigPolicyRn_Type = SnmpAdminString
_CfprComputeAutoconfigPolicyRn_Object = MibTableColumn
cfprComputeAutoconfigPolicyRn = _CfprComputeAutoconfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 3),
    _CfprComputeAutoconfigPolicyRn_Type()
)
cfprComputeAutoconfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyRn.setStatus("current")
_CfprComputeAutoconfigPolicyDescr_Type = SnmpAdminString
_CfprComputeAutoconfigPolicyDescr_Object = MibTableColumn
cfprComputeAutoconfigPolicyDescr = _CfprComputeAutoconfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 4),
    _CfprComputeAutoconfigPolicyDescr_Type()
)
cfprComputeAutoconfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyDescr.setStatus("current")
_CfprComputeAutoconfigPolicyDstDn_Type = SnmpAdminString
_CfprComputeAutoconfigPolicyDstDn_Object = MibTableColumn
cfprComputeAutoconfigPolicyDstDn = _CfprComputeAutoconfigPolicyDstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 5),
    _CfprComputeAutoconfigPolicyDstDn_Type()
)
cfprComputeAutoconfigPolicyDstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyDstDn.setStatus("current")
_CfprComputeAutoconfigPolicyIntId_Type = SnmpAdminString
_CfprComputeAutoconfigPolicyIntId_Object = MibTableColumn
cfprComputeAutoconfigPolicyIntId = _CfprComputeAutoconfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 6),
    _CfprComputeAutoconfigPolicyIntId_Type()
)
cfprComputeAutoconfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyIntId.setStatus("current")
_CfprComputeAutoconfigPolicyName_Type = SnmpAdminString
_CfprComputeAutoconfigPolicyName_Object = MibTableColumn
cfprComputeAutoconfigPolicyName = _CfprComputeAutoconfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 7),
    _CfprComputeAutoconfigPolicyName_Type()
)
cfprComputeAutoconfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyName.setStatus("current")
_CfprComputeAutoconfigPolicyPolicyLevel_Type = Gauge32
_CfprComputeAutoconfigPolicyPolicyLevel_Object = MibTableColumn
cfprComputeAutoconfigPolicyPolicyLevel = _CfprComputeAutoconfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 8),
    _CfprComputeAutoconfigPolicyPolicyLevel_Type()
)
cfprComputeAutoconfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyPolicyLevel.setStatus("current")
_CfprComputeAutoconfigPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeAutoconfigPolicyPolicyOwner_Object = MibTableColumn
cfprComputeAutoconfigPolicyPolicyOwner = _CfprComputeAutoconfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 9),
    _CfprComputeAutoconfigPolicyPolicyOwner_Type()
)
cfprComputeAutoconfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyPolicyOwner.setStatus("current")
_CfprComputeAutoconfigPolicyQualifier_Type = SnmpAdminString
_CfprComputeAutoconfigPolicyQualifier_Object = MibTableColumn
cfprComputeAutoconfigPolicyQualifier = _CfprComputeAutoconfigPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 10),
    _CfprComputeAutoconfigPolicyQualifier_Type()
)
cfprComputeAutoconfigPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicyQualifier.setStatus("current")
_CfprComputeAutoconfigPolicySrcTemplName_Type = SnmpAdminString
_CfprComputeAutoconfigPolicySrcTemplName_Object = MibTableColumn
cfprComputeAutoconfigPolicySrcTemplName = _CfprComputeAutoconfigPolicySrcTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 1, 1, 11),
    _CfprComputeAutoconfigPolicySrcTemplName_Type()
)
cfprComputeAutoconfigPolicySrcTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeAutoconfigPolicySrcTemplName.setStatus("current")
_CfprComputeBladeTable_Object = MibTable
cfprComputeBladeTable = _CfprComputeBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2)
)
if mibBuilder.loadTexts:
    cfprComputeBladeTable.setStatus("current")
_CfprComputeBladeEntry_Object = MibTableRow
cfprComputeBladeEntry = _CfprComputeBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1)
)
cfprComputeBladeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBladeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBladeEntry.setStatus("current")
_CfprComputeBladeInstanceId_Type = CfprManagedObjectId
_CfprComputeBladeInstanceId_Object = MibTableColumn
cfprComputeBladeInstanceId = _CfprComputeBladeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 1),
    _CfprComputeBladeInstanceId_Type()
)
cfprComputeBladeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBladeInstanceId.setStatus("current")
_CfprComputeBladeDn_Type = CfprManagedObjectDn
_CfprComputeBladeDn_Object = MibTableColumn
cfprComputeBladeDn = _CfprComputeBladeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 2),
    _CfprComputeBladeDn_Type()
)
cfprComputeBladeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDn.setStatus("current")
_CfprComputeBladeRn_Type = SnmpAdminString
_CfprComputeBladeRn_Object = MibTableColumn
cfprComputeBladeRn = _CfprComputeBladeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 3),
    _CfprComputeBladeRn_Type()
)
cfprComputeBladeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeRn.setStatus("current")
_CfprComputeBladeAdminPower_Type = CfprComputeAdminPowerState
_CfprComputeBladeAdminPower_Object = MibTableColumn
cfprComputeBladeAdminPower = _CfprComputeBladeAdminPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 4),
    _CfprComputeBladeAdminPower_Type()
)
cfprComputeBladeAdminPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeAdminPower.setStatus("current")
_CfprComputeBladeAdminState_Type = CfprComputeAdminState
_CfprComputeBladeAdminState_Object = MibTableColumn
cfprComputeBladeAdminState = _CfprComputeBladeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 5),
    _CfprComputeBladeAdminState_Type()
)
cfprComputeBladeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeAdminState.setStatus("current")
_CfprComputeBladeAssignedToDn_Type = SnmpAdminString
_CfprComputeBladeAssignedToDn_Object = MibTableColumn
cfprComputeBladeAssignedToDn = _CfprComputeBladeAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 6),
    _CfprComputeBladeAssignedToDn_Type()
)
cfprComputeBladeAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeAssignedToDn.setStatus("current")
_CfprComputeBladeAssociation_Type = CfprComputeAssociation
_CfprComputeBladeAssociation_Object = MibTableColumn
cfprComputeBladeAssociation = _CfprComputeBladeAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 7),
    _CfprComputeBladeAssociation_Type()
)
cfprComputeBladeAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeAssociation.setStatus("current")
_CfprComputeBladeAvailability_Type = CfprComputeAvailability
_CfprComputeBladeAvailability_Object = MibTableColumn
cfprComputeBladeAvailability = _CfprComputeBladeAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 8),
    _CfprComputeBladeAvailability_Type()
)
cfprComputeBladeAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeAvailability.setStatus("current")
_CfprComputeBladeAvailableMemory_Type = Gauge32
_CfprComputeBladeAvailableMemory_Object = MibTableColumn
cfprComputeBladeAvailableMemory = _CfprComputeBladeAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 9),
    _CfprComputeBladeAvailableMemory_Type()
)
cfprComputeBladeAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeAvailableMemory.setStatus("current")
_CfprComputeBladeChassisId_Type = Gauge32
_CfprComputeBladeChassisId_Object = MibTableColumn
cfprComputeBladeChassisId = _CfprComputeBladeChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 10),
    _CfprComputeBladeChassisId_Type()
)
cfprComputeBladeChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeChassisId.setStatus("current")
_CfprComputeBladeCheckPoint_Type = CfprComputeCheckPoint
_CfprComputeBladeCheckPoint_Object = MibTableColumn
cfprComputeBladeCheckPoint = _CfprComputeBladeCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 11),
    _CfprComputeBladeCheckPoint_Type()
)
cfprComputeBladeCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeCheckPoint.setStatus("current")
_CfprComputeBladeConnPath_Type = CfprEquipmentConnectionStatus
_CfprComputeBladeConnPath_Object = MibTableColumn
cfprComputeBladeConnPath = _CfprComputeBladeConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 12),
    _CfprComputeBladeConnPath_Type()
)
cfprComputeBladeConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeConnPath.setStatus("current")
_CfprComputeBladeConnStatus_Type = CfprEquipmentConnectionStatus
_CfprComputeBladeConnStatus_Object = MibTableColumn
cfprComputeBladeConnStatus = _CfprComputeBladeConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 13),
    _CfprComputeBladeConnStatus_Type()
)
cfprComputeBladeConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeConnStatus.setStatus("current")
_CfprComputeBladeDescr_Type = SnmpAdminString
_CfprComputeBladeDescr_Object = MibTableColumn
cfprComputeBladeDescr = _CfprComputeBladeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 14),
    _CfprComputeBladeDescr_Type()
)
cfprComputeBladeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDescr.setStatus("current")
_CfprComputeBladeDiscovery_Type = CfprComputeDiscovery
_CfprComputeBladeDiscovery_Object = MibTableColumn
cfprComputeBladeDiscovery = _CfprComputeBladeDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 15),
    _CfprComputeBladeDiscovery_Type()
)
cfprComputeBladeDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscovery.setStatus("current")
_CfprComputeBladeFltAggr_Type = Unsigned64
_CfprComputeBladeFltAggr_Object = MibTableColumn
cfprComputeBladeFltAggr = _CfprComputeBladeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 16),
    _CfprComputeBladeFltAggr_Type()
)
cfprComputeBladeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFltAggr.setStatus("current")
_CfprComputeBladeFsmDescr_Type = SnmpAdminString
_CfprComputeBladeFsmDescr_Object = MibTableColumn
cfprComputeBladeFsmDescr = _CfprComputeBladeFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 17),
    _CfprComputeBladeFsmDescr_Type()
)
cfprComputeBladeFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmDescr.setStatus("current")
_CfprComputeBladeFsmFlags_Type = SnmpAdminString
_CfprComputeBladeFsmFlags_Object = MibTableColumn
cfprComputeBladeFsmFlags = _CfprComputeBladeFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 18),
    _CfprComputeBladeFsmFlags_Type()
)
cfprComputeBladeFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmFlags.setStatus("current")
_CfprComputeBladeFsmPrev_Type = SnmpAdminString
_CfprComputeBladeFsmPrev_Object = MibTableColumn
cfprComputeBladeFsmPrev = _CfprComputeBladeFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 19),
    _CfprComputeBladeFsmPrev_Type()
)
cfprComputeBladeFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmPrev.setStatus("current")
_CfprComputeBladeFsmProgr_Type = Gauge32
_CfprComputeBladeFsmProgr_Object = MibTableColumn
cfprComputeBladeFsmProgr = _CfprComputeBladeFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 20),
    _CfprComputeBladeFsmProgr_Type()
)
cfprComputeBladeFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmProgr.setStatus("current")
_CfprComputeBladeFsmRmtInvErrCode_Type = Gauge32
_CfprComputeBladeFsmRmtInvErrCode_Object = MibTableColumn
cfprComputeBladeFsmRmtInvErrCode = _CfprComputeBladeFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 21),
    _CfprComputeBladeFsmRmtInvErrCode_Type()
)
cfprComputeBladeFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmRmtInvErrCode.setStatus("current")
_CfprComputeBladeFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprComputeBladeFsmRmtInvErrDescr_Object = MibTableColumn
cfprComputeBladeFsmRmtInvErrDescr = _CfprComputeBladeFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 22),
    _CfprComputeBladeFsmRmtInvErrDescr_Type()
)
cfprComputeBladeFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmRmtInvErrDescr.setStatus("current")
_CfprComputeBladeFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprComputeBladeFsmRmtInvRslt_Object = MibTableColumn
cfprComputeBladeFsmRmtInvRslt = _CfprComputeBladeFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 23),
    _CfprComputeBladeFsmRmtInvRslt_Type()
)
cfprComputeBladeFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmRmtInvRslt.setStatus("current")
_CfprComputeBladeFsmStageDescr_Type = SnmpAdminString
_CfprComputeBladeFsmStageDescr_Object = MibTableColumn
cfprComputeBladeFsmStageDescr = _CfprComputeBladeFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 24),
    _CfprComputeBladeFsmStageDescr_Type()
)
cfprComputeBladeFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageDescr.setStatus("current")
_CfprComputeBladeFsmStamp_Type = DateAndTime
_CfprComputeBladeFsmStamp_Object = MibTableColumn
cfprComputeBladeFsmStamp = _CfprComputeBladeFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 25),
    _CfprComputeBladeFsmStamp_Type()
)
cfprComputeBladeFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStamp.setStatus("current")
_CfprComputeBladeFsmStatus_Type = SnmpAdminString
_CfprComputeBladeFsmStatus_Object = MibTableColumn
cfprComputeBladeFsmStatus = _CfprComputeBladeFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 26),
    _CfprComputeBladeFsmStatus_Type()
)
cfprComputeBladeFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStatus.setStatus("current")
_CfprComputeBladeFsmTry_Type = Gauge32
_CfprComputeBladeFsmTry_Object = MibTableColumn
cfprComputeBladeFsmTry = _CfprComputeBladeFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 27),
    _CfprComputeBladeFsmTry_Type()
)
cfprComputeBladeFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTry.setStatus("current")
_CfprComputeBladeIntId_Type = SnmpAdminString
_CfprComputeBladeIntId_Object = MibTableColumn
cfprComputeBladeIntId = _CfprComputeBladeIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 28),
    _CfprComputeBladeIntId_Type()
)
cfprComputeBladeIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeIntId.setStatus("current")
_CfprComputeBladeLc_Type = CfprComputeAdminTrigger
_CfprComputeBladeLc_Object = MibTableColumn
cfprComputeBladeLc = _CfprComputeBladeLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 29),
    _CfprComputeBladeLc_Type()
)
cfprComputeBladeLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeLc.setStatus("current")
_CfprComputeBladeLcTs_Type = DateAndTime
_CfprComputeBladeLcTs_Object = MibTableColumn
cfprComputeBladeLcTs = _CfprComputeBladeLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 30),
    _CfprComputeBladeLcTs_Type()
)
cfprComputeBladeLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeLcTs.setStatus("current")
_CfprComputeBladeLocalId_Type = SnmpAdminString
_CfprComputeBladeLocalId_Object = MibTableColumn
cfprComputeBladeLocalId = _CfprComputeBladeLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 31),
    _CfprComputeBladeLocalId_Type()
)
cfprComputeBladeLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeLocalId.setStatus("current")
_CfprComputeBladeLowVoltageMemory_Type = CfprComputePhysicalLowVoltageMemory
_CfprComputeBladeLowVoltageMemory_Object = MibTableColumn
cfprComputeBladeLowVoltageMemory = _CfprComputeBladeLowVoltageMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 32),
    _CfprComputeBladeLowVoltageMemory_Type()
)
cfprComputeBladeLowVoltageMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeLowVoltageMemory.setStatus("current")
_CfprComputeBladeManagingInst_Type = CfprNetworkSwitchId
_CfprComputeBladeManagingInst_Object = MibTableColumn
cfprComputeBladeManagingInst = _CfprComputeBladeManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 33),
    _CfprComputeBladeManagingInst_Type()
)
cfprComputeBladeManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeManagingInst.setStatus("current")
_CfprComputeBladeMemorySpeed_Type = Gauge32
_CfprComputeBladeMemorySpeed_Object = MibTableColumn
cfprComputeBladeMemorySpeed = _CfprComputeBladeMemorySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 34),
    _CfprComputeBladeMemorySpeed_Type()
)
cfprComputeBladeMemorySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeMemorySpeed.setStatus("current")
_CfprComputeBladeMfgTime_Type = DateAndTime
_CfprComputeBladeMfgTime_Object = MibTableColumn
cfprComputeBladeMfgTime = _CfprComputeBladeMfgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 35),
    _CfprComputeBladeMfgTime_Type()
)
cfprComputeBladeMfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeMfgTime.setStatus("current")
_CfprComputeBladeModel_Type = SnmpAdminString
_CfprComputeBladeModel_Object = MibTableColumn
cfprComputeBladeModel = _CfprComputeBladeModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 36),
    _CfprComputeBladeModel_Type()
)
cfprComputeBladeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeModel.setStatus("current")
_CfprComputeBladeName_Type = SnmpAdminString
_CfprComputeBladeName_Object = MibTableColumn
cfprComputeBladeName = _CfprComputeBladeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 37),
    _CfprComputeBladeName_Type()
)
cfprComputeBladeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeName.setStatus("current")
_CfprComputeBladeNumOfAdaptors_Type = Gauge32
_CfprComputeBladeNumOfAdaptors_Object = MibTableColumn
cfprComputeBladeNumOfAdaptors = _CfprComputeBladeNumOfAdaptors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 38),
    _CfprComputeBladeNumOfAdaptors_Type()
)
cfprComputeBladeNumOfAdaptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeNumOfAdaptors.setStatus("current")
_CfprComputeBladeNumOfCores_Type = Gauge32
_CfprComputeBladeNumOfCores_Object = MibTableColumn
cfprComputeBladeNumOfCores = _CfprComputeBladeNumOfCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 39),
    _CfprComputeBladeNumOfCores_Type()
)
cfprComputeBladeNumOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeNumOfCores.setStatus("current")
_CfprComputeBladeNumOfCoresEnabled_Type = Gauge32
_CfprComputeBladeNumOfCoresEnabled_Object = MibTableColumn
cfprComputeBladeNumOfCoresEnabled = _CfprComputeBladeNumOfCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 40),
    _CfprComputeBladeNumOfCoresEnabled_Type()
)
cfprComputeBladeNumOfCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeNumOfCoresEnabled.setStatus("current")
_CfprComputeBladeNumOfCpus_Type = Gauge32
_CfprComputeBladeNumOfCpus_Object = MibTableColumn
cfprComputeBladeNumOfCpus = _CfprComputeBladeNumOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 41),
    _CfprComputeBladeNumOfCpus_Type()
)
cfprComputeBladeNumOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeNumOfCpus.setStatus("current")
_CfprComputeBladeNumOfEthHostIfs_Type = Gauge32
_CfprComputeBladeNumOfEthHostIfs_Object = MibTableColumn
cfprComputeBladeNumOfEthHostIfs = _CfprComputeBladeNumOfEthHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 42),
    _CfprComputeBladeNumOfEthHostIfs_Type()
)
cfprComputeBladeNumOfEthHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeNumOfEthHostIfs.setStatus("current")
_CfprComputeBladeNumOfFcHostIfs_Type = Gauge32
_CfprComputeBladeNumOfFcHostIfs_Object = MibTableColumn
cfprComputeBladeNumOfFcHostIfs = _CfprComputeBladeNumOfFcHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 43),
    _CfprComputeBladeNumOfFcHostIfs_Type()
)
cfprComputeBladeNumOfFcHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeNumOfFcHostIfs.setStatus("current")
_CfprComputeBladeNumOfThreads_Type = Gauge32
_CfprComputeBladeNumOfThreads_Object = MibTableColumn
cfprComputeBladeNumOfThreads = _CfprComputeBladeNumOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 44),
    _CfprComputeBladeNumOfThreads_Type()
)
cfprComputeBladeNumOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeNumOfThreads.setStatus("current")
_CfprComputeBladeOperPower_Type = CfprEquipmentPowerState
_CfprComputeBladeOperPower_Object = MibTableColumn
cfprComputeBladeOperPower = _CfprComputeBladeOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 45),
    _CfprComputeBladeOperPower_Type()
)
cfprComputeBladeOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeOperPower.setStatus("current")
_CfprComputeBladeOperQualifier_Type = CfprComputeIssues
_CfprComputeBladeOperQualifier_Object = MibTableColumn
cfprComputeBladeOperQualifier = _CfprComputeBladeOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 46),
    _CfprComputeBladeOperQualifier_Type()
)
cfprComputeBladeOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeOperQualifier.setStatus("current")
_CfprComputeBladeOperState_Type = CfprLsOperState
_CfprComputeBladeOperState_Object = MibTableColumn
cfprComputeBladeOperState = _CfprComputeBladeOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 47),
    _CfprComputeBladeOperState_Type()
)
cfprComputeBladeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeOperState.setStatus("current")
_CfprComputeBladeOperability_Type = CfprEquipmentOperability
_CfprComputeBladeOperability_Object = MibTableColumn
cfprComputeBladeOperability = _CfprComputeBladeOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 48),
    _CfprComputeBladeOperability_Type()
)
cfprComputeBladeOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeOperability.setStatus("current")
_CfprComputeBladeOriginalUuid_Type = SnmpAdminString
_CfprComputeBladeOriginalUuid_Object = MibTableColumn
cfprComputeBladeOriginalUuid = _CfprComputeBladeOriginalUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 49),
    _CfprComputeBladeOriginalUuid_Type()
)
cfprComputeBladeOriginalUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeOriginalUuid.setStatus("current")
_CfprComputeBladePartNumber_Type = SnmpAdminString
_CfprComputeBladePartNumber_Object = MibTableColumn
cfprComputeBladePartNumber = _CfprComputeBladePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 50),
    _CfprComputeBladePartNumber_Type()
)
cfprComputeBladePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladePartNumber.setStatus("current")
_CfprComputeBladePolicyLevel_Type = Gauge32
_CfprComputeBladePolicyLevel_Object = MibTableColumn
cfprComputeBladePolicyLevel = _CfprComputeBladePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 51),
    _CfprComputeBladePolicyLevel_Type()
)
cfprComputeBladePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladePolicyLevel.setStatus("current")
_CfprComputeBladePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeBladePolicyOwner_Object = MibTableColumn
cfprComputeBladePolicyOwner = _CfprComputeBladePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 52),
    _CfprComputeBladePolicyOwner_Type()
)
cfprComputeBladePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladePolicyOwner.setStatus("current")
_CfprComputeBladePresence_Type = CfprEquipmentSlotStatus
_CfprComputeBladePresence_Object = MibTableColumn
cfprComputeBladePresence = _CfprComputeBladePresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 53),
    _CfprComputeBladePresence_Type()
)
cfprComputeBladePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladePresence.setStatus("current")
_CfprComputeBladeRevision_Type = SnmpAdminString
_CfprComputeBladeRevision_Object = MibTableColumn
cfprComputeBladeRevision = _CfprComputeBladeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 54),
    _CfprComputeBladeRevision_Type()
)
cfprComputeBladeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeRevision.setStatus("current")
_CfprComputeBladeScaledMode_Type = CfprComputeMode
_CfprComputeBladeScaledMode_Object = MibTableColumn
cfprComputeBladeScaledMode = _CfprComputeBladeScaledMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 55),
    _CfprComputeBladeScaledMode_Type()
)
cfprComputeBladeScaledMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeScaledMode.setStatus("current")
_CfprComputeBladeSerial_Type = SnmpAdminString
_CfprComputeBladeSerial_Object = MibTableColumn
cfprComputeBladeSerial = _CfprComputeBladeSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 56),
    _CfprComputeBladeSerial_Type()
)
cfprComputeBladeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeSerial.setStatus("current")
_CfprComputeBladeServerId_Type = SnmpAdminString
_CfprComputeBladeServerId_Object = MibTableColumn
cfprComputeBladeServerId = _CfprComputeBladeServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 57),
    _CfprComputeBladeServerId_Type()
)
cfprComputeBladeServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeServerId.setStatus("current")
_CfprComputeBladeSlotId_Type = CfprComputeBladeSlotId
_CfprComputeBladeSlotId_Object = MibTableColumn
cfprComputeBladeSlotId = _CfprComputeBladeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 58),
    _CfprComputeBladeSlotId_Type()
)
cfprComputeBladeSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeSlotId.setStatus("current")
_CfprComputeBladeTotalMemory_Type = Gauge32
_CfprComputeBladeTotalMemory_Object = MibTableColumn
cfprComputeBladeTotalMemory = _CfprComputeBladeTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 59),
    _CfprComputeBladeTotalMemory_Type()
)
cfprComputeBladeTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeTotalMemory.setStatus("current")
_CfprComputeBladeUpgradeScenario_Type = CfprComputeUpgradeStatus
_CfprComputeBladeUpgradeScenario_Object = MibTableColumn
cfprComputeBladeUpgradeScenario = _CfprComputeBladeUpgradeScenario_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 60),
    _CfprComputeBladeUpgradeScenario_Type()
)
cfprComputeBladeUpgradeScenario.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeUpgradeScenario.setStatus("current")
_CfprComputeBladeUsrLbl_Type = SnmpAdminString
_CfprComputeBladeUsrLbl_Object = MibTableColumn
cfprComputeBladeUsrLbl = _CfprComputeBladeUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 61),
    _CfprComputeBladeUsrLbl_Type()
)
cfprComputeBladeUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeUsrLbl.setStatus("current")
_CfprComputeBladeUuid_Type = SnmpAdminString
_CfprComputeBladeUuid_Object = MibTableColumn
cfprComputeBladeUuid = _CfprComputeBladeUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 62),
    _CfprComputeBladeUuid_Type()
)
cfprComputeBladeUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeUuid.setStatus("current")
_CfprComputeBladeVendor_Type = SnmpAdminString
_CfprComputeBladeVendor_Object = MibTableColumn
cfprComputeBladeVendor = _CfprComputeBladeVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 63),
    _CfprComputeBladeVendor_Type()
)
cfprComputeBladeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeVendor.setStatus("current")
_CfprComputeBladeVid_Type = SnmpAdminString
_CfprComputeBladeVid_Object = MibTableColumn
cfprComputeBladeVid = _CfprComputeBladeVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 64),
    _CfprComputeBladeVid_Type()
)
cfprComputeBladeVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeVid.setStatus("current")
_CfprComputeBladeLastAdaptorCrashReset_Type = SnmpAdminString
_CfprComputeBladeLastAdaptorCrashReset_Object = MibTableColumn
cfprComputeBladeLastAdaptorCrashReset = _CfprComputeBladeLastAdaptorCrashReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 65),
    _CfprComputeBladeLastAdaptorCrashReset_Type()
)
cfprComputeBladeLastAdaptorCrashReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeLastAdaptorCrashReset.setStatus("current")
_CfprComputeBladeLastBiosHangReset_Type = DateAndTime
_CfprComputeBladeLastBiosHangReset_Object = MibTableColumn
cfprComputeBladeLastBiosHangReset = _CfprComputeBladeLastBiosHangReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 66),
    _CfprComputeBladeLastBiosHangReset_Type()
)
cfprComputeBladeLastBiosHangReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeLastBiosHangReset.setStatus("current")
_CfprComputeBladeLastCatErrReset_Type = DateAndTime
_CfprComputeBladeLastCatErrReset_Object = MibTableColumn
cfprComputeBladeLastCatErrReset = _CfprComputeBladeLastCatErrReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 67),
    _CfprComputeBladeLastCatErrReset_Type()
)
cfprComputeBladeLastCatErrReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeLastCatErrReset.setStatus("current")
_CfprComputeBladePostState_Type = CfprEquipmentBiosPostState
_CfprComputeBladePostState_Object = MibTableColumn
cfprComputeBladePostState = _CfprComputeBladePostState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 68),
    _CfprComputeBladePostState_Type()
)
cfprComputeBladePostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladePostState.setStatus("current")
_CfprComputeBladePostWaitCount_Type = Gauge32
_CfprComputeBladePostWaitCount_Object = MibTableColumn
cfprComputeBladePostWaitCount = _CfprComputeBladePostWaitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 69),
    _CfprComputeBladePostWaitCount_Type()
)
cfprComputeBladePostWaitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladePostWaitCount.setStatus("current")
_CfprComputeBladeResetCatErrCount_Type = Gauge32
_CfprComputeBladeResetCatErrCount_Object = MibTableColumn
cfprComputeBladeResetCatErrCount = _CfprComputeBladeResetCatErrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 70),
    _CfprComputeBladeResetCatErrCount_Type()
)
cfprComputeBladeResetCatErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeResetCatErrCount.setStatus("current")
_CfprComputeBladeResetCount_Type = Gauge32
_CfprComputeBladeResetCount_Object = MibTableColumn
cfprComputeBladeResetCount = _CfprComputeBladeResetCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 2, 1, 71),
    _CfprComputeBladeResetCount_Type()
)
cfprComputeBladeResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeResetCount.setStatus("current")
_CfprComputeBladeDiscPolicyTable_Object = MibTable
cfprComputeBladeDiscPolicyTable = _CfprComputeBladeDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3)
)
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyTable.setStatus("current")
_CfprComputeBladeDiscPolicyEntry_Object = MibTableRow
cfprComputeBladeDiscPolicyEntry = _CfprComputeBladeDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1)
)
cfprComputeBladeDiscPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBladeDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyEntry.setStatus("current")
_CfprComputeBladeDiscPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeBladeDiscPolicyInstanceId_Object = MibTableColumn
cfprComputeBladeDiscPolicyInstanceId = _CfprComputeBladeDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 1),
    _CfprComputeBladeDiscPolicyInstanceId_Type()
)
cfprComputeBladeDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyInstanceId.setStatus("current")
_CfprComputeBladeDiscPolicyDn_Type = CfprManagedObjectDn
_CfprComputeBladeDiscPolicyDn_Object = MibTableColumn
cfprComputeBladeDiscPolicyDn = _CfprComputeBladeDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 2),
    _CfprComputeBladeDiscPolicyDn_Type()
)
cfprComputeBladeDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyDn.setStatus("current")
_CfprComputeBladeDiscPolicyRn_Type = SnmpAdminString
_CfprComputeBladeDiscPolicyRn_Object = MibTableColumn
cfprComputeBladeDiscPolicyRn = _CfprComputeBladeDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 3),
    _CfprComputeBladeDiscPolicyRn_Type()
)
cfprComputeBladeDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyRn.setStatus("current")
_CfprComputeBladeDiscPolicyAction_Type = SnmpAdminString
_CfprComputeBladeDiscPolicyAction_Object = MibTableColumn
cfprComputeBladeDiscPolicyAction = _CfprComputeBladeDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 4),
    _CfprComputeBladeDiscPolicyAction_Type()
)
cfprComputeBladeDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyAction.setStatus("current")
_CfprComputeBladeDiscPolicyDescr_Type = SnmpAdminString
_CfprComputeBladeDiscPolicyDescr_Object = MibTableColumn
cfprComputeBladeDiscPolicyDescr = _CfprComputeBladeDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 5),
    _CfprComputeBladeDiscPolicyDescr_Type()
)
cfprComputeBladeDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyDescr.setStatus("current")
_CfprComputeBladeDiscPolicyIntId_Type = SnmpAdminString
_CfprComputeBladeDiscPolicyIntId_Object = MibTableColumn
cfprComputeBladeDiscPolicyIntId = _CfprComputeBladeDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 6),
    _CfprComputeBladeDiscPolicyIntId_Type()
)
cfprComputeBladeDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyIntId.setStatus("current")
_CfprComputeBladeDiscPolicyName_Type = SnmpAdminString
_CfprComputeBladeDiscPolicyName_Object = MibTableColumn
cfprComputeBladeDiscPolicyName = _CfprComputeBladeDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 7),
    _CfprComputeBladeDiscPolicyName_Type()
)
cfprComputeBladeDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyName.setStatus("current")
_CfprComputeBladeDiscPolicyPolicyLevel_Type = Gauge32
_CfprComputeBladeDiscPolicyPolicyLevel_Object = MibTableColumn
cfprComputeBladeDiscPolicyPolicyLevel = _CfprComputeBladeDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 8),
    _CfprComputeBladeDiscPolicyPolicyLevel_Type()
)
cfprComputeBladeDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyPolicyLevel.setStatus("current")
_CfprComputeBladeDiscPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeBladeDiscPolicyPolicyOwner_Object = MibTableColumn
cfprComputeBladeDiscPolicyPolicyOwner = _CfprComputeBladeDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 9),
    _CfprComputeBladeDiscPolicyPolicyOwner_Type()
)
cfprComputeBladeDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyPolicyOwner.setStatus("current")
_CfprComputeBladeDiscPolicyQualifier_Type = SnmpAdminString
_CfprComputeBladeDiscPolicyQualifier_Object = MibTableColumn
cfprComputeBladeDiscPolicyQualifier = _CfprComputeBladeDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 10),
    _CfprComputeBladeDiscPolicyQualifier_Type()
)
cfprComputeBladeDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyQualifier.setStatus("current")
_CfprComputeBladeDiscPolicyScrubPolicyName_Type = SnmpAdminString
_CfprComputeBladeDiscPolicyScrubPolicyName_Object = MibTableColumn
cfprComputeBladeDiscPolicyScrubPolicyName = _CfprComputeBladeDiscPolicyScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 3, 1, 11),
    _CfprComputeBladeDiscPolicyScrubPolicyName_Type()
)
cfprComputeBladeDiscPolicyScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeDiscPolicyScrubPolicyName.setStatus("current")
_CfprComputeBladeFsmTable_Object = MibTable
cfprComputeBladeFsmTable = _CfprComputeBladeFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4)
)
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTable.setStatus("current")
_CfprComputeBladeFsmEntry_Object = MibTableRow
cfprComputeBladeFsmEntry = _CfprComputeBladeFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1)
)
cfprComputeBladeFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBladeFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBladeFsmEntry.setStatus("current")
_CfprComputeBladeFsmInstanceId_Type = CfprManagedObjectId
_CfprComputeBladeFsmInstanceId_Object = MibTableColumn
cfprComputeBladeFsmInstanceId = _CfprComputeBladeFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 1),
    _CfprComputeBladeFsmInstanceId_Type()
)
cfprComputeBladeFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmInstanceId.setStatus("current")
_CfprComputeBladeFsmDn_Type = CfprManagedObjectDn
_CfprComputeBladeFsmDn_Object = MibTableColumn
cfprComputeBladeFsmDn = _CfprComputeBladeFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 2),
    _CfprComputeBladeFsmDn_Type()
)
cfprComputeBladeFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmDn.setStatus("current")
_CfprComputeBladeFsmRn_Type = SnmpAdminString
_CfprComputeBladeFsmRn_Object = MibTableColumn
cfprComputeBladeFsmRn = _CfprComputeBladeFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 3),
    _CfprComputeBladeFsmRn_Type()
)
cfprComputeBladeFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmRn.setStatus("current")
_CfprComputeBladeFsmCompletionTime_Type = DateAndTime
_CfprComputeBladeFsmCompletionTime_Object = MibTableColumn
cfprComputeBladeFsmCompletionTime = _CfprComputeBladeFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 4),
    _CfprComputeBladeFsmCompletionTime_Type()
)
cfprComputeBladeFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmCompletionTime.setStatus("current")
_CfprComputeBladeFsmCurrentFsm_Type = CfprComputeBladeFsmCurrentFsm
_CfprComputeBladeFsmCurrentFsm_Object = MibTableColumn
cfprComputeBladeFsmCurrentFsm = _CfprComputeBladeFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 5),
    _CfprComputeBladeFsmCurrentFsm_Type()
)
cfprComputeBladeFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmCurrentFsm.setStatus("current")
_CfprComputeBladeFsmDescrData_Type = SnmpAdminString
_CfprComputeBladeFsmDescrData_Object = MibTableColumn
cfprComputeBladeFsmDescrData = _CfprComputeBladeFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 6),
    _CfprComputeBladeFsmDescrData_Type()
)
cfprComputeBladeFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmDescrData.setStatus("current")
_CfprComputeBladeFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprComputeBladeFsmFsmStatus_Object = MibTableColumn
cfprComputeBladeFsmFsmStatus = _CfprComputeBladeFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 7),
    _CfprComputeBladeFsmFsmStatus_Type()
)
cfprComputeBladeFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmFsmStatus.setStatus("current")
_CfprComputeBladeFsmProgress_Type = Gauge32
_CfprComputeBladeFsmProgress_Object = MibTableColumn
cfprComputeBladeFsmProgress = _CfprComputeBladeFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 8),
    _CfprComputeBladeFsmProgress_Type()
)
cfprComputeBladeFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmProgress.setStatus("current")
_CfprComputeBladeFsmRmtErrCode_Type = Gauge32
_CfprComputeBladeFsmRmtErrCode_Object = MibTableColumn
cfprComputeBladeFsmRmtErrCode = _CfprComputeBladeFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 9),
    _CfprComputeBladeFsmRmtErrCode_Type()
)
cfprComputeBladeFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmRmtErrCode.setStatus("current")
_CfprComputeBladeFsmRmtErrDescr_Type = SnmpAdminString
_CfprComputeBladeFsmRmtErrDescr_Object = MibTableColumn
cfprComputeBladeFsmRmtErrDescr = _CfprComputeBladeFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 10),
    _CfprComputeBladeFsmRmtErrDescr_Type()
)
cfprComputeBladeFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmRmtErrDescr.setStatus("current")
_CfprComputeBladeFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprComputeBladeFsmRmtRslt_Object = MibTableColumn
cfprComputeBladeFsmRmtRslt = _CfprComputeBladeFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 4, 1, 11),
    _CfprComputeBladeFsmRmtRslt_Type()
)
cfprComputeBladeFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmRmtRslt.setStatus("current")
_CfprComputeBladeFsmStageTable_Object = MibTable
cfprComputeBladeFsmStageTable = _CfprComputeBladeFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5)
)
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageTable.setStatus("current")
_CfprComputeBladeFsmStageEntry_Object = MibTableRow
cfprComputeBladeFsmStageEntry = _CfprComputeBladeFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1)
)
cfprComputeBladeFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBladeFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageEntry.setStatus("current")
_CfprComputeBladeFsmStageInstanceId_Type = CfprManagedObjectId
_CfprComputeBladeFsmStageInstanceId_Object = MibTableColumn
cfprComputeBladeFsmStageInstanceId = _CfprComputeBladeFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 1),
    _CfprComputeBladeFsmStageInstanceId_Type()
)
cfprComputeBladeFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageInstanceId.setStatus("current")
_CfprComputeBladeFsmStageDn_Type = CfprManagedObjectDn
_CfprComputeBladeFsmStageDn_Object = MibTableColumn
cfprComputeBladeFsmStageDn = _CfprComputeBladeFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 2),
    _CfprComputeBladeFsmStageDn_Type()
)
cfprComputeBladeFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageDn.setStatus("current")
_CfprComputeBladeFsmStageRn_Type = SnmpAdminString
_CfprComputeBladeFsmStageRn_Object = MibTableColumn
cfprComputeBladeFsmStageRn = _CfprComputeBladeFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 3),
    _CfprComputeBladeFsmStageRn_Type()
)
cfprComputeBladeFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageRn.setStatus("current")
_CfprComputeBladeFsmStageDescrData_Type = SnmpAdminString
_CfprComputeBladeFsmStageDescrData_Object = MibTableColumn
cfprComputeBladeFsmStageDescrData = _CfprComputeBladeFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 4),
    _CfprComputeBladeFsmStageDescrData_Type()
)
cfprComputeBladeFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageDescrData.setStatus("current")
_CfprComputeBladeFsmStageLastUpdateTime_Type = DateAndTime
_CfprComputeBladeFsmStageLastUpdateTime_Object = MibTableColumn
cfprComputeBladeFsmStageLastUpdateTime = _CfprComputeBladeFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 5),
    _CfprComputeBladeFsmStageLastUpdateTime_Type()
)
cfprComputeBladeFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageLastUpdateTime.setStatus("current")
_CfprComputeBladeFsmStageName_Type = CfprComputeBladeFsmStageName
_CfprComputeBladeFsmStageName_Object = MibTableColumn
cfprComputeBladeFsmStageName = _CfprComputeBladeFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 6),
    _CfprComputeBladeFsmStageName_Type()
)
cfprComputeBladeFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageName.setStatus("current")
_CfprComputeBladeFsmStageOrder_Type = Gauge32
_CfprComputeBladeFsmStageOrder_Object = MibTableColumn
cfprComputeBladeFsmStageOrder = _CfprComputeBladeFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 7),
    _CfprComputeBladeFsmStageOrder_Type()
)
cfprComputeBladeFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageOrder.setStatus("current")
_CfprComputeBladeFsmStageRetry_Type = Gauge32
_CfprComputeBladeFsmStageRetry_Object = MibTableColumn
cfprComputeBladeFsmStageRetry = _CfprComputeBladeFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 8),
    _CfprComputeBladeFsmStageRetry_Type()
)
cfprComputeBladeFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageRetry.setStatus("current")
_CfprComputeBladeFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprComputeBladeFsmStageStageStatus_Object = MibTableColumn
cfprComputeBladeFsmStageStageStatus = _CfprComputeBladeFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 5, 1, 9),
    _CfprComputeBladeFsmStageStageStatus_Type()
)
cfprComputeBladeFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmStageStageStatus.setStatus("current")
_CfprComputeBladeFsmTaskTable_Object = MibTable
cfprComputeBladeFsmTaskTable = _CfprComputeBladeFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6)
)
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskTable.setStatus("current")
_CfprComputeBladeFsmTaskEntry_Object = MibTableRow
cfprComputeBladeFsmTaskEntry = _CfprComputeBladeFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6, 1)
)
cfprComputeBladeFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBladeFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskEntry.setStatus("current")
_CfprComputeBladeFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprComputeBladeFsmTaskInstanceId_Object = MibTableColumn
cfprComputeBladeFsmTaskInstanceId = _CfprComputeBladeFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6, 1, 1),
    _CfprComputeBladeFsmTaskInstanceId_Type()
)
cfprComputeBladeFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskInstanceId.setStatus("current")
_CfprComputeBladeFsmTaskDn_Type = CfprManagedObjectDn
_CfprComputeBladeFsmTaskDn_Object = MibTableColumn
cfprComputeBladeFsmTaskDn = _CfprComputeBladeFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6, 1, 2),
    _CfprComputeBladeFsmTaskDn_Type()
)
cfprComputeBladeFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskDn.setStatus("current")
_CfprComputeBladeFsmTaskRn_Type = SnmpAdminString
_CfprComputeBladeFsmTaskRn_Object = MibTableColumn
cfprComputeBladeFsmTaskRn = _CfprComputeBladeFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6, 1, 3),
    _CfprComputeBladeFsmTaskRn_Type()
)
cfprComputeBladeFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskRn.setStatus("current")
_CfprComputeBladeFsmTaskCompletion_Type = CfprFsmCompletion
_CfprComputeBladeFsmTaskCompletion_Object = MibTableColumn
cfprComputeBladeFsmTaskCompletion = _CfprComputeBladeFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6, 1, 4),
    _CfprComputeBladeFsmTaskCompletion_Type()
)
cfprComputeBladeFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskCompletion.setStatus("current")
_CfprComputeBladeFsmTaskFlags_Type = CfprComputeBladeFsmTaskFlags
_CfprComputeBladeFsmTaskFlags_Object = MibTableColumn
cfprComputeBladeFsmTaskFlags = _CfprComputeBladeFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6, 1, 5),
    _CfprComputeBladeFsmTaskFlags_Type()
)
cfprComputeBladeFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskFlags.setStatus("current")
_CfprComputeBladeFsmTaskItem_Type = CfprComputeBladeFsmTaskItem
_CfprComputeBladeFsmTaskItem_Object = MibTableColumn
cfprComputeBladeFsmTaskItem = _CfprComputeBladeFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6, 1, 6),
    _CfprComputeBladeFsmTaskItem_Type()
)
cfprComputeBladeFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskItem.setStatus("current")
_CfprComputeBladeFsmTaskSeqId_Type = Gauge32
_CfprComputeBladeFsmTaskSeqId_Object = MibTableColumn
cfprComputeBladeFsmTaskSeqId = _CfprComputeBladeFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 6, 1, 7),
    _CfprComputeBladeFsmTaskSeqId_Type()
)
cfprComputeBladeFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeFsmTaskSeqId.setStatus("current")
_CfprComputeBladeInheritPolicyTable_Object = MibTable
cfprComputeBladeInheritPolicyTable = _CfprComputeBladeInheritPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7)
)
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyTable.setStatus("current")
_CfprComputeBladeInheritPolicyEntry_Object = MibTableRow
cfprComputeBladeInheritPolicyEntry = _CfprComputeBladeInheritPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1)
)
cfprComputeBladeInheritPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBladeInheritPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyEntry.setStatus("current")
_CfprComputeBladeInheritPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeBladeInheritPolicyInstanceId_Object = MibTableColumn
cfprComputeBladeInheritPolicyInstanceId = _CfprComputeBladeInheritPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 1),
    _CfprComputeBladeInheritPolicyInstanceId_Type()
)
cfprComputeBladeInheritPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyInstanceId.setStatus("current")
_CfprComputeBladeInheritPolicyDn_Type = CfprManagedObjectDn
_CfprComputeBladeInheritPolicyDn_Object = MibTableColumn
cfprComputeBladeInheritPolicyDn = _CfprComputeBladeInheritPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 2),
    _CfprComputeBladeInheritPolicyDn_Type()
)
cfprComputeBladeInheritPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyDn.setStatus("current")
_CfprComputeBladeInheritPolicyRn_Type = SnmpAdminString
_CfprComputeBladeInheritPolicyRn_Object = MibTableColumn
cfprComputeBladeInheritPolicyRn = _CfprComputeBladeInheritPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 3),
    _CfprComputeBladeInheritPolicyRn_Type()
)
cfprComputeBladeInheritPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyRn.setStatus("current")
_CfprComputeBladeInheritPolicyDescr_Type = SnmpAdminString
_CfprComputeBladeInheritPolicyDescr_Object = MibTableColumn
cfprComputeBladeInheritPolicyDescr = _CfprComputeBladeInheritPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 4),
    _CfprComputeBladeInheritPolicyDescr_Type()
)
cfprComputeBladeInheritPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyDescr.setStatus("current")
_CfprComputeBladeInheritPolicyDstDn_Type = SnmpAdminString
_CfprComputeBladeInheritPolicyDstDn_Object = MibTableColumn
cfprComputeBladeInheritPolicyDstDn = _CfprComputeBladeInheritPolicyDstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 5),
    _CfprComputeBladeInheritPolicyDstDn_Type()
)
cfprComputeBladeInheritPolicyDstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyDstDn.setStatus("current")
_CfprComputeBladeInheritPolicyIntId_Type = SnmpAdminString
_CfprComputeBladeInheritPolicyIntId_Object = MibTableColumn
cfprComputeBladeInheritPolicyIntId = _CfprComputeBladeInheritPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 6),
    _CfprComputeBladeInheritPolicyIntId_Type()
)
cfprComputeBladeInheritPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyIntId.setStatus("current")
_CfprComputeBladeInheritPolicyName_Type = SnmpAdminString
_CfprComputeBladeInheritPolicyName_Object = MibTableColumn
cfprComputeBladeInheritPolicyName = _CfprComputeBladeInheritPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 7),
    _CfprComputeBladeInheritPolicyName_Type()
)
cfprComputeBladeInheritPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyName.setStatus("current")
_CfprComputeBladeInheritPolicyPolicyLevel_Type = Gauge32
_CfprComputeBladeInheritPolicyPolicyLevel_Object = MibTableColumn
cfprComputeBladeInheritPolicyPolicyLevel = _CfprComputeBladeInheritPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 8),
    _CfprComputeBladeInheritPolicyPolicyLevel_Type()
)
cfprComputeBladeInheritPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyPolicyLevel.setStatus("current")
_CfprComputeBladeInheritPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeBladeInheritPolicyPolicyOwner_Object = MibTableColumn
cfprComputeBladeInheritPolicyPolicyOwner = _CfprComputeBladeInheritPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 9),
    _CfprComputeBladeInheritPolicyPolicyOwner_Type()
)
cfprComputeBladeInheritPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyPolicyOwner.setStatus("current")
_CfprComputeBladeInheritPolicyQualifier_Type = SnmpAdminString
_CfprComputeBladeInheritPolicyQualifier_Object = MibTableColumn
cfprComputeBladeInheritPolicyQualifier = _CfprComputeBladeInheritPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 7, 1, 10),
    _CfprComputeBladeInheritPolicyQualifier_Type()
)
cfprComputeBladeInheritPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBladeInheritPolicyQualifier.setStatus("current")
_CfprComputeBoardTable_Object = MibTable
cfprComputeBoardTable = _CfprComputeBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8)
)
if mibBuilder.loadTexts:
    cfprComputeBoardTable.setStatus("current")
_CfprComputeBoardEntry_Object = MibTableRow
cfprComputeBoardEntry = _CfprComputeBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1)
)
cfprComputeBoardEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBoardInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBoardEntry.setStatus("current")
_CfprComputeBoardInstanceId_Type = CfprManagedObjectId
_CfprComputeBoardInstanceId_Object = MibTableColumn
cfprComputeBoardInstanceId = _CfprComputeBoardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 1),
    _CfprComputeBoardInstanceId_Type()
)
cfprComputeBoardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBoardInstanceId.setStatus("current")
_CfprComputeBoardDn_Type = CfprManagedObjectDn
_CfprComputeBoardDn_Object = MibTableColumn
cfprComputeBoardDn = _CfprComputeBoardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 2),
    _CfprComputeBoardDn_Type()
)
cfprComputeBoardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardDn.setStatus("current")
_CfprComputeBoardRn_Type = SnmpAdminString
_CfprComputeBoardRn_Object = MibTableColumn
cfprComputeBoardRn = _CfprComputeBoardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 3),
    _CfprComputeBoardRn_Type()
)
cfprComputeBoardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardRn.setStatus("current")
_CfprComputeBoardCmosVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeBoardCmosVoltage_Object = MibTableColumn
cfprComputeBoardCmosVoltage = _CfprComputeBoardCmosVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 4),
    _CfprComputeBoardCmosVoltage_Type()
)
cfprComputeBoardCmosVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardCmosVoltage.setStatus("current")
_CfprComputeBoardCpuType_Type = CfprEquipmentCpuType
_CfprComputeBoardCpuType_Object = MibTableColumn
cfprComputeBoardCpuType = _CfprComputeBoardCpuType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 5),
    _CfprComputeBoardCpuType_Type()
)
cfprComputeBoardCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardCpuType.setStatus("current")
_CfprComputeBoardFaultQualifier_Type = SnmpAdminString
_CfprComputeBoardFaultQualifier_Object = MibTableColumn
cfprComputeBoardFaultQualifier = _CfprComputeBoardFaultQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 6),
    _CfprComputeBoardFaultQualifier_Type()
)
cfprComputeBoardFaultQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardFaultQualifier.setStatus("current")
_CfprComputeBoardId_Type = Gauge32
_CfprComputeBoardId_Object = MibTableColumn
cfprComputeBoardId = _CfprComputeBoardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 7),
    _CfprComputeBoardId_Type()
)
cfprComputeBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardId.setStatus("current")
_CfprComputeBoardLocationDn_Type = SnmpAdminString
_CfprComputeBoardLocationDn_Object = MibTableColumn
cfprComputeBoardLocationDn = _CfprComputeBoardLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 8),
    _CfprComputeBoardLocationDn_Type()
)
cfprComputeBoardLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardLocationDn.setStatus("current")
_CfprComputeBoardModel_Type = SnmpAdminString
_CfprComputeBoardModel_Object = MibTableColumn
cfprComputeBoardModel = _CfprComputeBoardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 9),
    _CfprComputeBoardModel_Type()
)
cfprComputeBoardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardModel.setStatus("current")
_CfprComputeBoardOperPower_Type = CfprEquipmentPowerState
_CfprComputeBoardOperPower_Object = MibTableColumn
cfprComputeBoardOperPower = _CfprComputeBoardOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 10),
    _CfprComputeBoardOperPower_Type()
)
cfprComputeBoardOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardOperPower.setStatus("current")
_CfprComputeBoardOperQualifierReason_Type = SnmpAdminString
_CfprComputeBoardOperQualifierReason_Object = MibTableColumn
cfprComputeBoardOperQualifierReason = _CfprComputeBoardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 11),
    _CfprComputeBoardOperQualifierReason_Type()
)
cfprComputeBoardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardOperQualifierReason.setStatus("current")
_CfprComputeBoardOperState_Type = CfprEquipmentOperability
_CfprComputeBoardOperState_Object = MibTableColumn
cfprComputeBoardOperState = _CfprComputeBoardOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 12),
    _CfprComputeBoardOperState_Type()
)
cfprComputeBoardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardOperState.setStatus("current")
_CfprComputeBoardOperability_Type = CfprEquipmentOperability
_CfprComputeBoardOperability_Object = MibTableColumn
cfprComputeBoardOperability = _CfprComputeBoardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 13),
    _CfprComputeBoardOperability_Type()
)
cfprComputeBoardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardOperability.setStatus("current")
_CfprComputeBoardPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeBoardPerf_Object = MibTableColumn
cfprComputeBoardPerf = _CfprComputeBoardPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 14),
    _CfprComputeBoardPerf_Type()
)
cfprComputeBoardPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardPerf.setStatus("current")
_CfprComputeBoardPower_Type = CfprComputeABoardPower
_CfprComputeBoardPower_Object = MibTableColumn
cfprComputeBoardPower = _CfprComputeBoardPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 15),
    _CfprComputeBoardPower_Type()
)
cfprComputeBoardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardPower.setStatus("current")
_CfprComputeBoardPowerUsage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeBoardPowerUsage_Object = MibTableColumn
cfprComputeBoardPowerUsage = _CfprComputeBoardPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 16),
    _CfprComputeBoardPowerUsage_Type()
)
cfprComputeBoardPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardPowerUsage.setStatus("current")
_CfprComputeBoardPresence_Type = CfprEquipmentPresence
_CfprComputeBoardPresence_Object = MibTableColumn
cfprComputeBoardPresence = _CfprComputeBoardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 17),
    _CfprComputeBoardPresence_Type()
)
cfprComputeBoardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardPresence.setStatus("current")
_CfprComputeBoardRevision_Type = SnmpAdminString
_CfprComputeBoardRevision_Object = MibTableColumn
cfprComputeBoardRevision = _CfprComputeBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 18),
    _CfprComputeBoardRevision_Type()
)
cfprComputeBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardRevision.setStatus("current")
_CfprComputeBoardSerial_Type = SnmpAdminString
_CfprComputeBoardSerial_Object = MibTableColumn
cfprComputeBoardSerial = _CfprComputeBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 19),
    _CfprComputeBoardSerial_Type()
)
cfprComputeBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardSerial.setStatus("current")
_CfprComputeBoardThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeBoardThermal_Object = MibTableColumn
cfprComputeBoardThermal = _CfprComputeBoardThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 20),
    _CfprComputeBoardThermal_Type()
)
cfprComputeBoardThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardThermal.setStatus("current")
_CfprComputeBoardVendor_Type = SnmpAdminString
_CfprComputeBoardVendor_Object = MibTableColumn
cfprComputeBoardVendor = _CfprComputeBoardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 21),
    _CfprComputeBoardVendor_Type()
)
cfprComputeBoardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardVendor.setStatus("current")
_CfprComputeBoardVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeBoardVoltage_Object = MibTableColumn
cfprComputeBoardVoltage = _CfprComputeBoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 8, 1, 22),
    _CfprComputeBoardVoltage_Type()
)
cfprComputeBoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardVoltage.setStatus("current")
_CfprComputeBoardConnectorTable_Object = MibTable
cfprComputeBoardConnectorTable = _CfprComputeBoardConnectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 9)
)
if mibBuilder.loadTexts:
    cfprComputeBoardConnectorTable.setStatus("current")
_CfprComputeBoardConnectorEntry_Object = MibTableRow
cfprComputeBoardConnectorEntry = _CfprComputeBoardConnectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 9, 1)
)
cfprComputeBoardConnectorEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBoardConnectorInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBoardConnectorEntry.setStatus("current")
_CfprComputeBoardConnectorInstanceId_Type = CfprManagedObjectId
_CfprComputeBoardConnectorInstanceId_Object = MibTableColumn
cfprComputeBoardConnectorInstanceId = _CfprComputeBoardConnectorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 9, 1, 1),
    _CfprComputeBoardConnectorInstanceId_Type()
)
cfprComputeBoardConnectorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBoardConnectorInstanceId.setStatus("current")
_CfprComputeBoardConnectorDn_Type = CfprManagedObjectDn
_CfprComputeBoardConnectorDn_Object = MibTableColumn
cfprComputeBoardConnectorDn = _CfprComputeBoardConnectorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 9, 1, 2),
    _CfprComputeBoardConnectorDn_Type()
)
cfprComputeBoardConnectorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardConnectorDn.setStatus("current")
_CfprComputeBoardConnectorRn_Type = SnmpAdminString
_CfprComputeBoardConnectorRn_Object = MibTableColumn
cfprComputeBoardConnectorRn = _CfprComputeBoardConnectorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 9, 1, 3),
    _CfprComputeBoardConnectorRn_Type()
)
cfprComputeBoardConnectorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardConnectorRn.setStatus("current")
_CfprComputeBoardConnectorBoardConnectorType_Type = CfprEquipmentBoardConnectorType
_CfprComputeBoardConnectorBoardConnectorType_Object = MibTableColumn
cfprComputeBoardConnectorBoardConnectorType = _CfprComputeBoardConnectorBoardConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 9, 1, 4),
    _CfprComputeBoardConnectorBoardConnectorType_Type()
)
cfprComputeBoardConnectorBoardConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardConnectorBoardConnectorType.setStatus("current")
_CfprComputeBoardConnectorMasterSlotId_Type = Gauge32
_CfprComputeBoardConnectorMasterSlotId_Object = MibTableColumn
cfprComputeBoardConnectorMasterSlotId = _CfprComputeBoardConnectorMasterSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 9, 1, 5),
    _CfprComputeBoardConnectorMasterSlotId_Type()
)
cfprComputeBoardConnectorMasterSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardConnectorMasterSlotId.setStatus("current")
_CfprComputeBoardConnectorSlaveSlotId_Type = Gauge32
_CfprComputeBoardConnectorSlaveSlotId_Object = MibTableColumn
cfprComputeBoardConnectorSlaveSlotId = _CfprComputeBoardConnectorSlaveSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 9, 1, 6),
    _CfprComputeBoardConnectorSlaveSlotId_Type()
)
cfprComputeBoardConnectorSlaveSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardConnectorSlaveSlotId.setStatus("current")
_CfprComputeBoardControllerTable_Object = MibTable
cfprComputeBoardControllerTable = _CfprComputeBoardControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10)
)
if mibBuilder.loadTexts:
    cfprComputeBoardControllerTable.setStatus("current")
_CfprComputeBoardControllerEntry_Object = MibTableRow
cfprComputeBoardControllerEntry = _CfprComputeBoardControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1)
)
cfprComputeBoardControllerEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeBoardControllerInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeBoardControllerEntry.setStatus("current")
_CfprComputeBoardControllerInstanceId_Type = CfprManagedObjectId
_CfprComputeBoardControllerInstanceId_Object = MibTableColumn
cfprComputeBoardControllerInstanceId = _CfprComputeBoardControllerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 1),
    _CfprComputeBoardControllerInstanceId_Type()
)
cfprComputeBoardControllerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerInstanceId.setStatus("current")
_CfprComputeBoardControllerDn_Type = CfprManagedObjectDn
_CfprComputeBoardControllerDn_Object = MibTableColumn
cfprComputeBoardControllerDn = _CfprComputeBoardControllerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 2),
    _CfprComputeBoardControllerDn_Type()
)
cfprComputeBoardControllerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerDn.setStatus("current")
_CfprComputeBoardControllerRn_Type = SnmpAdminString
_CfprComputeBoardControllerRn_Object = MibTableColumn
cfprComputeBoardControllerRn = _CfprComputeBoardControllerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 3),
    _CfprComputeBoardControllerRn_Type()
)
cfprComputeBoardControllerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerRn.setStatus("current")
_CfprComputeBoardControllerId_Type = Gauge32
_CfprComputeBoardControllerId_Object = MibTableColumn
cfprComputeBoardControllerId = _CfprComputeBoardControllerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 4),
    _CfprComputeBoardControllerId_Type()
)
cfprComputeBoardControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerId.setStatus("current")
_CfprComputeBoardControllerLocationDn_Type = SnmpAdminString
_CfprComputeBoardControllerLocationDn_Object = MibTableColumn
cfprComputeBoardControllerLocationDn = _CfprComputeBoardControllerLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 5),
    _CfprComputeBoardControllerLocationDn_Type()
)
cfprComputeBoardControllerLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerLocationDn.setStatus("current")
_CfprComputeBoardControllerModel_Type = SnmpAdminString
_CfprComputeBoardControllerModel_Object = MibTableColumn
cfprComputeBoardControllerModel = _CfprComputeBoardControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 6),
    _CfprComputeBoardControllerModel_Type()
)
cfprComputeBoardControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerModel.setStatus("current")
_CfprComputeBoardControllerOperQualifierReason_Type = SnmpAdminString
_CfprComputeBoardControllerOperQualifierReason_Object = MibTableColumn
cfprComputeBoardControllerOperQualifierReason = _CfprComputeBoardControllerOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 7),
    _CfprComputeBoardControllerOperQualifierReason_Type()
)
cfprComputeBoardControllerOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerOperQualifierReason.setStatus("current")
_CfprComputeBoardControllerOperState_Type = CfprEquipmentOperability
_CfprComputeBoardControllerOperState_Object = MibTableColumn
cfprComputeBoardControllerOperState = _CfprComputeBoardControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 8),
    _CfprComputeBoardControllerOperState_Type()
)
cfprComputeBoardControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerOperState.setStatus("current")
_CfprComputeBoardControllerOperability_Type = CfprEquipmentOperability
_CfprComputeBoardControllerOperability_Object = MibTableColumn
cfprComputeBoardControllerOperability = _CfprComputeBoardControllerOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 9),
    _CfprComputeBoardControllerOperability_Type()
)
cfprComputeBoardControllerOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerOperability.setStatus("current")
_CfprComputeBoardControllerPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeBoardControllerPerf_Object = MibTableColumn
cfprComputeBoardControllerPerf = _CfprComputeBoardControllerPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 10),
    _CfprComputeBoardControllerPerf_Type()
)
cfprComputeBoardControllerPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerPerf.setStatus("current")
_CfprComputeBoardControllerPower_Type = CfprEquipmentPowerState
_CfprComputeBoardControllerPower_Object = MibTableColumn
cfprComputeBoardControllerPower = _CfprComputeBoardControllerPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 11),
    _CfprComputeBoardControllerPower_Type()
)
cfprComputeBoardControllerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerPower.setStatus("current")
_CfprComputeBoardControllerPresence_Type = CfprEquipmentPresence
_CfprComputeBoardControllerPresence_Object = MibTableColumn
cfprComputeBoardControllerPresence = _CfprComputeBoardControllerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 12),
    _CfprComputeBoardControllerPresence_Type()
)
cfprComputeBoardControllerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerPresence.setStatus("current")
_CfprComputeBoardControllerRevision_Type = SnmpAdminString
_CfprComputeBoardControllerRevision_Object = MibTableColumn
cfprComputeBoardControllerRevision = _CfprComputeBoardControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 13),
    _CfprComputeBoardControllerRevision_Type()
)
cfprComputeBoardControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerRevision.setStatus("current")
_CfprComputeBoardControllerSerial_Type = SnmpAdminString
_CfprComputeBoardControllerSerial_Object = MibTableColumn
cfprComputeBoardControllerSerial = _CfprComputeBoardControllerSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 14),
    _CfprComputeBoardControllerSerial_Type()
)
cfprComputeBoardControllerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerSerial.setStatus("current")
_CfprComputeBoardControllerThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeBoardControllerThermal_Object = MibTableColumn
cfprComputeBoardControllerThermal = _CfprComputeBoardControllerThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 15),
    _CfprComputeBoardControllerThermal_Type()
)
cfprComputeBoardControllerThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerThermal.setStatus("current")
_CfprComputeBoardControllerVendor_Type = SnmpAdminString
_CfprComputeBoardControllerVendor_Object = MibTableColumn
cfprComputeBoardControllerVendor = _CfprComputeBoardControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 16),
    _CfprComputeBoardControllerVendor_Type()
)
cfprComputeBoardControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerVendor.setStatus("current")
_CfprComputeBoardControllerVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeBoardControllerVoltage_Object = MibTableColumn
cfprComputeBoardControllerVoltage = _CfprComputeBoardControllerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 10, 1, 17),
    _CfprComputeBoardControllerVoltage_Type()
)
cfprComputeBoardControllerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeBoardControllerVoltage.setStatus("current")
_CfprComputeChassisConnPolicyTable_Object = MibTable
cfprComputeChassisConnPolicyTable = _CfprComputeChassisConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11)
)
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyTable.setStatus("current")
_CfprComputeChassisConnPolicyEntry_Object = MibTableRow
cfprComputeChassisConnPolicyEntry = _CfprComputeChassisConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1)
)
cfprComputeChassisConnPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeChassisConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyEntry.setStatus("current")
_CfprComputeChassisConnPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeChassisConnPolicyInstanceId_Object = MibTableColumn
cfprComputeChassisConnPolicyInstanceId = _CfprComputeChassisConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 1),
    _CfprComputeChassisConnPolicyInstanceId_Type()
)
cfprComputeChassisConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyInstanceId.setStatus("current")
_CfprComputeChassisConnPolicyDn_Type = CfprManagedObjectDn
_CfprComputeChassisConnPolicyDn_Object = MibTableColumn
cfprComputeChassisConnPolicyDn = _CfprComputeChassisConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 2),
    _CfprComputeChassisConnPolicyDn_Type()
)
cfprComputeChassisConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyDn.setStatus("current")
_CfprComputeChassisConnPolicyRn_Type = SnmpAdminString
_CfprComputeChassisConnPolicyRn_Object = MibTableColumn
cfprComputeChassisConnPolicyRn = _CfprComputeChassisConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 3),
    _CfprComputeChassisConnPolicyRn_Type()
)
cfprComputeChassisConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyRn.setStatus("current")
_CfprComputeChassisConnPolicyAdminState_Type = CfprComputeAdminLinkAggregation
_CfprComputeChassisConnPolicyAdminState_Object = MibTableColumn
cfprComputeChassisConnPolicyAdminState = _CfprComputeChassisConnPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 4),
    _CfprComputeChassisConnPolicyAdminState_Type()
)
cfprComputeChassisConnPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyAdminState.setStatus("current")
_CfprComputeChassisConnPolicyChassisId_Type = CfprComputeChassisConnPolicyChassisId
_CfprComputeChassisConnPolicyChassisId_Object = MibTableColumn
cfprComputeChassisConnPolicyChassisId = _CfprComputeChassisConnPolicyChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 5),
    _CfprComputeChassisConnPolicyChassisId_Type()
)
cfprComputeChassisConnPolicyChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyChassisId.setStatus("current")
_CfprComputeChassisConnPolicyDescr_Type = SnmpAdminString
_CfprComputeChassisConnPolicyDescr_Object = MibTableColumn
cfprComputeChassisConnPolicyDescr = _CfprComputeChassisConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 6),
    _CfprComputeChassisConnPolicyDescr_Type()
)
cfprComputeChassisConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyDescr.setStatus("current")
_CfprComputeChassisConnPolicyIntId_Type = SnmpAdminString
_CfprComputeChassisConnPolicyIntId_Object = MibTableColumn
cfprComputeChassisConnPolicyIntId = _CfprComputeChassisConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 7),
    _CfprComputeChassisConnPolicyIntId_Type()
)
cfprComputeChassisConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyIntId.setStatus("current")
_CfprComputeChassisConnPolicyName_Type = SnmpAdminString
_CfprComputeChassisConnPolicyName_Object = MibTableColumn
cfprComputeChassisConnPolicyName = _CfprComputeChassisConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 8),
    _CfprComputeChassisConnPolicyName_Type()
)
cfprComputeChassisConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyName.setStatus("current")
_CfprComputeChassisConnPolicyPolicyLevel_Type = Gauge32
_CfprComputeChassisConnPolicyPolicyLevel_Object = MibTableColumn
cfprComputeChassisConnPolicyPolicyLevel = _CfprComputeChassisConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 9),
    _CfprComputeChassisConnPolicyPolicyLevel_Type()
)
cfprComputeChassisConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyPolicyLevel.setStatus("current")
_CfprComputeChassisConnPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeChassisConnPolicyPolicyOwner_Object = MibTableColumn
cfprComputeChassisConnPolicyPolicyOwner = _CfprComputeChassisConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 10),
    _CfprComputeChassisConnPolicyPolicyOwner_Type()
)
cfprComputeChassisConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyPolicyOwner.setStatus("current")
_CfprComputeChassisConnPolicyQualifier_Type = SnmpAdminString
_CfprComputeChassisConnPolicyQualifier_Object = MibTableColumn
cfprComputeChassisConnPolicyQualifier = _CfprComputeChassisConnPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 11),
    _CfprComputeChassisConnPolicyQualifier_Type()
)
cfprComputeChassisConnPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicyQualifier.setStatus("current")
_CfprComputeChassisConnPolicySwitchId_Type = CfprNetworkSwitchId
_CfprComputeChassisConnPolicySwitchId_Object = MibTableColumn
cfprComputeChassisConnPolicySwitchId = _CfprComputeChassisConnPolicySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 11, 1, 12),
    _CfprComputeChassisConnPolicySwitchId_Type()
)
cfprComputeChassisConnPolicySwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisConnPolicySwitchId.setStatus("current")
_CfprComputeChassisDiscPolicyTable_Object = MibTable
cfprComputeChassisDiscPolicyTable = _CfprComputeChassisDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12)
)
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyTable.setStatus("current")
_CfprComputeChassisDiscPolicyEntry_Object = MibTableRow
cfprComputeChassisDiscPolicyEntry = _CfprComputeChassisDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1)
)
cfprComputeChassisDiscPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeChassisDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyEntry.setStatus("current")
_CfprComputeChassisDiscPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeChassisDiscPolicyInstanceId_Object = MibTableColumn
cfprComputeChassisDiscPolicyInstanceId = _CfprComputeChassisDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 1),
    _CfprComputeChassisDiscPolicyInstanceId_Type()
)
cfprComputeChassisDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyInstanceId.setStatus("current")
_CfprComputeChassisDiscPolicyDn_Type = CfprManagedObjectDn
_CfprComputeChassisDiscPolicyDn_Object = MibTableColumn
cfprComputeChassisDiscPolicyDn = _CfprComputeChassisDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 2),
    _CfprComputeChassisDiscPolicyDn_Type()
)
cfprComputeChassisDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyDn.setStatus("current")
_CfprComputeChassisDiscPolicyRn_Type = SnmpAdminString
_CfprComputeChassisDiscPolicyRn_Object = MibTableColumn
cfprComputeChassisDiscPolicyRn = _CfprComputeChassisDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 3),
    _CfprComputeChassisDiscPolicyRn_Type()
)
cfprComputeChassisDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyRn.setStatus("current")
_CfprComputeChassisDiscPolicyAction_Type = CfprComputeChassisDiscAction
_CfprComputeChassisDiscPolicyAction_Object = MibTableColumn
cfprComputeChassisDiscPolicyAction = _CfprComputeChassisDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 4),
    _CfprComputeChassisDiscPolicyAction_Type()
)
cfprComputeChassisDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyAction.setStatus("current")
_CfprComputeChassisDiscPolicyDescr_Type = SnmpAdminString
_CfprComputeChassisDiscPolicyDescr_Object = MibTableColumn
cfprComputeChassisDiscPolicyDescr = _CfprComputeChassisDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 5),
    _CfprComputeChassisDiscPolicyDescr_Type()
)
cfprComputeChassisDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyDescr.setStatus("current")
_CfprComputeChassisDiscPolicyIntId_Type = SnmpAdminString
_CfprComputeChassisDiscPolicyIntId_Object = MibTableColumn
cfprComputeChassisDiscPolicyIntId = _CfprComputeChassisDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 6),
    _CfprComputeChassisDiscPolicyIntId_Type()
)
cfprComputeChassisDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyIntId.setStatus("current")
_CfprComputeChassisDiscPolicyLinkAggregationPref_Type = CfprComputeLinkAggregation
_CfprComputeChassisDiscPolicyLinkAggregationPref_Object = MibTableColumn
cfprComputeChassisDiscPolicyLinkAggregationPref = _CfprComputeChassisDiscPolicyLinkAggregationPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 7),
    _CfprComputeChassisDiscPolicyLinkAggregationPref_Type()
)
cfprComputeChassisDiscPolicyLinkAggregationPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyLinkAggregationPref.setStatus("current")
_CfprComputeChassisDiscPolicyName_Type = SnmpAdminString
_CfprComputeChassisDiscPolicyName_Object = MibTableColumn
cfprComputeChassisDiscPolicyName = _CfprComputeChassisDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 8),
    _CfprComputeChassisDiscPolicyName_Type()
)
cfprComputeChassisDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyName.setStatus("current")
_CfprComputeChassisDiscPolicyPolicyLevel_Type = Gauge32
_CfprComputeChassisDiscPolicyPolicyLevel_Object = MibTableColumn
cfprComputeChassisDiscPolicyPolicyLevel = _CfprComputeChassisDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 9),
    _CfprComputeChassisDiscPolicyPolicyLevel_Type()
)
cfprComputeChassisDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyPolicyLevel.setStatus("current")
_CfprComputeChassisDiscPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeChassisDiscPolicyPolicyOwner_Object = MibTableColumn
cfprComputeChassisDiscPolicyPolicyOwner = _CfprComputeChassisDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 10),
    _CfprComputeChassisDiscPolicyPolicyOwner_Type()
)
cfprComputeChassisDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyPolicyOwner.setStatus("current")
_CfprComputeChassisDiscPolicyQualifier_Type = SnmpAdminString
_CfprComputeChassisDiscPolicyQualifier_Object = MibTableColumn
cfprComputeChassisDiscPolicyQualifier = _CfprComputeChassisDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 11),
    _CfprComputeChassisDiscPolicyQualifier_Type()
)
cfprComputeChassisDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyQualifier.setStatus("current")
_CfprComputeChassisDiscPolicyRebalance_Type = CfprComputeConnectivityRebalancing
_CfprComputeChassisDiscPolicyRebalance_Object = MibTableColumn
cfprComputeChassisDiscPolicyRebalance = _CfprComputeChassisDiscPolicyRebalance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 12, 1, 12),
    _CfprComputeChassisDiscPolicyRebalance_Type()
)
cfprComputeChassisDiscPolicyRebalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisDiscPolicyRebalance.setStatus("current")
_CfprComputeChassisQualTable_Object = MibTable
cfprComputeChassisQualTable = _CfprComputeChassisQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 13)
)
if mibBuilder.loadTexts:
    cfprComputeChassisQualTable.setStatus("current")
_CfprComputeChassisQualEntry_Object = MibTableRow
cfprComputeChassisQualEntry = _CfprComputeChassisQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 13, 1)
)
cfprComputeChassisQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeChassisQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeChassisQualEntry.setStatus("current")
_CfprComputeChassisQualInstanceId_Type = CfprManagedObjectId
_CfprComputeChassisQualInstanceId_Object = MibTableColumn
cfprComputeChassisQualInstanceId = _CfprComputeChassisQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 13, 1, 1),
    _CfprComputeChassisQualInstanceId_Type()
)
cfprComputeChassisQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeChassisQualInstanceId.setStatus("current")
_CfprComputeChassisQualDn_Type = CfprManagedObjectDn
_CfprComputeChassisQualDn_Object = MibTableColumn
cfprComputeChassisQualDn = _CfprComputeChassisQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 13, 1, 2),
    _CfprComputeChassisQualDn_Type()
)
cfprComputeChassisQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisQualDn.setStatus("current")
_CfprComputeChassisQualRn_Type = SnmpAdminString
_CfprComputeChassisQualRn_Object = MibTableColumn
cfprComputeChassisQualRn = _CfprComputeChassisQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 13, 1, 3),
    _CfprComputeChassisQualRn_Type()
)
cfprComputeChassisQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisQualRn.setStatus("current")
_CfprComputeChassisQualMaxId_Type = CfprComputeChassisQualMaxId
_CfprComputeChassisQualMaxId_Object = MibTableColumn
cfprComputeChassisQualMaxId = _CfprComputeChassisQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 13, 1, 4),
    _CfprComputeChassisQualMaxId_Type()
)
cfprComputeChassisQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisQualMaxId.setStatus("current")
_CfprComputeChassisQualMinId_Type = CfprComputeChassisQualMinId
_CfprComputeChassisQualMinId_Object = MibTableColumn
cfprComputeChassisQualMinId = _CfprComputeChassisQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 13, 1, 5),
    _CfprComputeChassisQualMinId_Type()
)
cfprComputeChassisQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeChassisQualMinId.setStatus("current")
_CfprComputeDefaultsTable_Object = MibTable
cfprComputeDefaultsTable = _CfprComputeDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 14)
)
if mibBuilder.loadTexts:
    cfprComputeDefaultsTable.setStatus("current")
_CfprComputeDefaultsEntry_Object = MibTableRow
cfprComputeDefaultsEntry = _CfprComputeDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 14, 1)
)
cfprComputeDefaultsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeDefaultsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeDefaultsEntry.setStatus("current")
_CfprComputeDefaultsInstanceId_Type = CfprManagedObjectId
_CfprComputeDefaultsInstanceId_Object = MibTableColumn
cfprComputeDefaultsInstanceId = _CfprComputeDefaultsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 14, 1, 1),
    _CfprComputeDefaultsInstanceId_Type()
)
cfprComputeDefaultsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeDefaultsInstanceId.setStatus("current")
_CfprComputeDefaultsDn_Type = CfprManagedObjectDn
_CfprComputeDefaultsDn_Object = MibTableColumn
cfprComputeDefaultsDn = _CfprComputeDefaultsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 14, 1, 2),
    _CfprComputeDefaultsDn_Type()
)
cfprComputeDefaultsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeDefaultsDn.setStatus("current")
_CfprComputeDefaultsRn_Type = SnmpAdminString
_CfprComputeDefaultsRn_Object = MibTableColumn
cfprComputeDefaultsRn = _CfprComputeDefaultsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 14, 1, 3),
    _CfprComputeDefaultsRn_Type()
)
cfprComputeDefaultsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeDefaultsRn.setStatus("current")
_CfprComputeExtBoardTable_Object = MibTable
cfprComputeExtBoardTable = _CfprComputeExtBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15)
)
if mibBuilder.loadTexts:
    cfprComputeExtBoardTable.setStatus("current")
_CfprComputeExtBoardEntry_Object = MibTableRow
cfprComputeExtBoardEntry = _CfprComputeExtBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1)
)
cfprComputeExtBoardEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeExtBoardInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeExtBoardEntry.setStatus("current")
_CfprComputeExtBoardInstanceId_Type = CfprManagedObjectId
_CfprComputeExtBoardInstanceId_Object = MibTableColumn
cfprComputeExtBoardInstanceId = _CfprComputeExtBoardInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 1),
    _CfprComputeExtBoardInstanceId_Type()
)
cfprComputeExtBoardInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeExtBoardInstanceId.setStatus("current")
_CfprComputeExtBoardDn_Type = CfprManagedObjectDn
_CfprComputeExtBoardDn_Object = MibTableColumn
cfprComputeExtBoardDn = _CfprComputeExtBoardDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 2),
    _CfprComputeExtBoardDn_Type()
)
cfprComputeExtBoardDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardDn.setStatus("current")
_CfprComputeExtBoardRn_Type = SnmpAdminString
_CfprComputeExtBoardRn_Object = MibTableColumn
cfprComputeExtBoardRn = _CfprComputeExtBoardRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 3),
    _CfprComputeExtBoardRn_Type()
)
cfprComputeExtBoardRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardRn.setStatus("current")
_CfprComputeExtBoardBoardAggregationRole_Type = CfprEquipmentBoardAggregationRole
_CfprComputeExtBoardBoardAggregationRole_Object = MibTableColumn
cfprComputeExtBoardBoardAggregationRole = _CfprComputeExtBoardBoardAggregationRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 4),
    _CfprComputeExtBoardBoardAggregationRole_Type()
)
cfprComputeExtBoardBoardAggregationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardBoardAggregationRole.setStatus("current")
_CfprComputeExtBoardChassisId_Type = Gauge32
_CfprComputeExtBoardChassisId_Object = MibTableColumn
cfprComputeExtBoardChassisId = _CfprComputeExtBoardChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 5),
    _CfprComputeExtBoardChassisId_Type()
)
cfprComputeExtBoardChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardChassisId.setStatus("current")
_CfprComputeExtBoardCmosVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeExtBoardCmosVoltage_Object = MibTableColumn
cfprComputeExtBoardCmosVoltage = _CfprComputeExtBoardCmosVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 6),
    _CfprComputeExtBoardCmosVoltage_Type()
)
cfprComputeExtBoardCmosVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardCmosVoltage.setStatus("current")
_CfprComputeExtBoardConnPath_Type = CfprEquipmentConnectionStatus
_CfprComputeExtBoardConnPath_Object = MibTableColumn
cfprComputeExtBoardConnPath = _CfprComputeExtBoardConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 7),
    _CfprComputeExtBoardConnPath_Type()
)
cfprComputeExtBoardConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardConnPath.setStatus("current")
_CfprComputeExtBoardConnStatus_Type = CfprEquipmentConnectionStatus
_CfprComputeExtBoardConnStatus_Object = MibTableColumn
cfprComputeExtBoardConnStatus = _CfprComputeExtBoardConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 8),
    _CfprComputeExtBoardConnStatus_Type()
)
cfprComputeExtBoardConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardConnStatus.setStatus("current")
_CfprComputeExtBoardFaultQualifier_Type = SnmpAdminString
_CfprComputeExtBoardFaultQualifier_Object = MibTableColumn
cfprComputeExtBoardFaultQualifier = _CfprComputeExtBoardFaultQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 9),
    _CfprComputeExtBoardFaultQualifier_Type()
)
cfprComputeExtBoardFaultQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardFaultQualifier.setStatus("current")
_CfprComputeExtBoardId_Type = Gauge32
_CfprComputeExtBoardId_Object = MibTableColumn
cfprComputeExtBoardId = _CfprComputeExtBoardId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 10),
    _CfprComputeExtBoardId_Type()
)
cfprComputeExtBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardId.setStatus("current")
_CfprComputeExtBoardLocationDn_Type = SnmpAdminString
_CfprComputeExtBoardLocationDn_Object = MibTableColumn
cfprComputeExtBoardLocationDn = _CfprComputeExtBoardLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 11),
    _CfprComputeExtBoardLocationDn_Type()
)
cfprComputeExtBoardLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardLocationDn.setStatus("current")
_CfprComputeExtBoardManagingInst_Type = CfprNetworkSwitchId
_CfprComputeExtBoardManagingInst_Object = MibTableColumn
cfprComputeExtBoardManagingInst = _CfprComputeExtBoardManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 12),
    _CfprComputeExtBoardManagingInst_Type()
)
cfprComputeExtBoardManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardManagingInst.setStatus("current")
_CfprComputeExtBoardModel_Type = SnmpAdminString
_CfprComputeExtBoardModel_Object = MibTableColumn
cfprComputeExtBoardModel = _CfprComputeExtBoardModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 13),
    _CfprComputeExtBoardModel_Type()
)
cfprComputeExtBoardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardModel.setStatus("current")
_CfprComputeExtBoardOperPower_Type = CfprEquipmentPowerState
_CfprComputeExtBoardOperPower_Object = MibTableColumn
cfprComputeExtBoardOperPower = _CfprComputeExtBoardOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 14),
    _CfprComputeExtBoardOperPower_Type()
)
cfprComputeExtBoardOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardOperPower.setStatus("current")
_CfprComputeExtBoardOperQualifierReason_Type = SnmpAdminString
_CfprComputeExtBoardOperQualifierReason_Object = MibTableColumn
cfprComputeExtBoardOperQualifierReason = _CfprComputeExtBoardOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 15),
    _CfprComputeExtBoardOperQualifierReason_Type()
)
cfprComputeExtBoardOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardOperQualifierReason.setStatus("current")
_CfprComputeExtBoardOperState_Type = CfprEquipmentOperability
_CfprComputeExtBoardOperState_Object = MibTableColumn
cfprComputeExtBoardOperState = _CfprComputeExtBoardOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 16),
    _CfprComputeExtBoardOperState_Type()
)
cfprComputeExtBoardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardOperState.setStatus("current")
_CfprComputeExtBoardOperability_Type = CfprEquipmentOperability
_CfprComputeExtBoardOperability_Object = MibTableColumn
cfprComputeExtBoardOperability = _CfprComputeExtBoardOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 17),
    _CfprComputeExtBoardOperability_Type()
)
cfprComputeExtBoardOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardOperability.setStatus("current")
_CfprComputeExtBoardPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeExtBoardPerf_Object = MibTableColumn
cfprComputeExtBoardPerf = _CfprComputeExtBoardPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 18),
    _CfprComputeExtBoardPerf_Type()
)
cfprComputeExtBoardPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardPerf.setStatus("current")
_CfprComputeExtBoardPower_Type = CfprComputeABoardPower
_CfprComputeExtBoardPower_Object = MibTableColumn
cfprComputeExtBoardPower = _CfprComputeExtBoardPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 19),
    _CfprComputeExtBoardPower_Type()
)
cfprComputeExtBoardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardPower.setStatus("current")
_CfprComputeExtBoardPowerUsage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeExtBoardPowerUsage_Object = MibTableColumn
cfprComputeExtBoardPowerUsage = _CfprComputeExtBoardPowerUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 20),
    _CfprComputeExtBoardPowerUsage_Type()
)
cfprComputeExtBoardPowerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardPowerUsage.setStatus("current")
_CfprComputeExtBoardPresence_Type = CfprEquipmentPresence
_CfprComputeExtBoardPresence_Object = MibTableColumn
cfprComputeExtBoardPresence = _CfprComputeExtBoardPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 21),
    _CfprComputeExtBoardPresence_Type()
)
cfprComputeExtBoardPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardPresence.setStatus("current")
_CfprComputeExtBoardRevision_Type = SnmpAdminString
_CfprComputeExtBoardRevision_Object = MibTableColumn
cfprComputeExtBoardRevision = _CfprComputeExtBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 22),
    _CfprComputeExtBoardRevision_Type()
)
cfprComputeExtBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardRevision.setStatus("current")
_CfprComputeExtBoardSerial_Type = SnmpAdminString
_CfprComputeExtBoardSerial_Object = MibTableColumn
cfprComputeExtBoardSerial = _CfprComputeExtBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 23),
    _CfprComputeExtBoardSerial_Type()
)
cfprComputeExtBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardSerial.setStatus("current")
_CfprComputeExtBoardSlotId_Type = Gauge32
_CfprComputeExtBoardSlotId_Object = MibTableColumn
cfprComputeExtBoardSlotId = _CfprComputeExtBoardSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 24),
    _CfprComputeExtBoardSlotId_Type()
)
cfprComputeExtBoardSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardSlotId.setStatus("current")
_CfprComputeExtBoardThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeExtBoardThermal_Object = MibTableColumn
cfprComputeExtBoardThermal = _CfprComputeExtBoardThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 25),
    _CfprComputeExtBoardThermal_Type()
)
cfprComputeExtBoardThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardThermal.setStatus("current")
_CfprComputeExtBoardVendor_Type = SnmpAdminString
_CfprComputeExtBoardVendor_Object = MibTableColumn
cfprComputeExtBoardVendor = _CfprComputeExtBoardVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 26),
    _CfprComputeExtBoardVendor_Type()
)
cfprComputeExtBoardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardVendor.setStatus("current")
_CfprComputeExtBoardVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeExtBoardVoltage_Object = MibTableColumn
cfprComputeExtBoardVoltage = _CfprComputeExtBoardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 15, 1, 27),
    _CfprComputeExtBoardVoltage_Type()
)
cfprComputeExtBoardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeExtBoardVoltage.setStatus("current")
_CfprComputeFwSyncAckTable_Object = MibTable
cfprComputeFwSyncAckTable = _CfprComputeFwSyncAckTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16)
)
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckTable.setStatus("current")
_CfprComputeFwSyncAckEntry_Object = MibTableRow
cfprComputeFwSyncAckEntry = _CfprComputeFwSyncAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1)
)
cfprComputeFwSyncAckEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeFwSyncAckInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckEntry.setStatus("current")
_CfprComputeFwSyncAckInstanceId_Type = CfprManagedObjectId
_CfprComputeFwSyncAckInstanceId_Object = MibTableColumn
cfprComputeFwSyncAckInstanceId = _CfprComputeFwSyncAckInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 1),
    _CfprComputeFwSyncAckInstanceId_Type()
)
cfprComputeFwSyncAckInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckInstanceId.setStatus("current")
_CfprComputeFwSyncAckDn_Type = CfprManagedObjectDn
_CfprComputeFwSyncAckDn_Object = MibTableColumn
cfprComputeFwSyncAckDn = _CfprComputeFwSyncAckDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 2),
    _CfprComputeFwSyncAckDn_Type()
)
cfprComputeFwSyncAckDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckDn.setStatus("current")
_CfprComputeFwSyncAckRn_Type = SnmpAdminString
_CfprComputeFwSyncAckRn_Object = MibTableColumn
cfprComputeFwSyncAckRn = _CfprComputeFwSyncAckRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 3),
    _CfprComputeFwSyncAckRn_Type()
)
cfprComputeFwSyncAckRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckRn.setStatus("current")
_CfprComputeFwSyncAckAcked_Type = DateAndTime
_CfprComputeFwSyncAckAcked_Object = MibTableColumn
cfprComputeFwSyncAckAcked = _CfprComputeFwSyncAckAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 4),
    _CfprComputeFwSyncAckAcked_Type()
)
cfprComputeFwSyncAckAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckAcked.setStatus("current")
_CfprComputeFwSyncAckAckedBy_Type = SnmpAdminString
_CfprComputeFwSyncAckAckedBy_Object = MibTableColumn
cfprComputeFwSyncAckAckedBy = _CfprComputeFwSyncAckAckedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 5),
    _CfprComputeFwSyncAckAckedBy_Type()
)
cfprComputeFwSyncAckAckedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckAckedBy.setStatus("current")
_CfprComputeFwSyncAckAdminState_Type = CfprTrigAdminState
_CfprComputeFwSyncAckAdminState_Object = MibTableColumn
cfprComputeFwSyncAckAdminState = _CfprComputeFwSyncAckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 6),
    _CfprComputeFwSyncAckAdminState_Type()
)
cfprComputeFwSyncAckAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckAdminState.setStatus("current")
_CfprComputeFwSyncAckAutoDelete_Type = TruthValue
_CfprComputeFwSyncAckAutoDelete_Object = MibTableColumn
cfprComputeFwSyncAckAutoDelete = _CfprComputeFwSyncAckAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 7),
    _CfprComputeFwSyncAckAutoDelete_Type()
)
cfprComputeFwSyncAckAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckAutoDelete.setStatus("current")
_CfprComputeFwSyncAckChangeBy_Type = SnmpAdminString
_CfprComputeFwSyncAckChangeBy_Object = MibTableColumn
cfprComputeFwSyncAckChangeBy = _CfprComputeFwSyncAckChangeBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 8),
    _CfprComputeFwSyncAckChangeBy_Type()
)
cfprComputeFwSyncAckChangeBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckChangeBy.setStatus("current")
_CfprComputeFwSyncAckChangeDetails_Type = CfprTrigAckChangeDetails
_CfprComputeFwSyncAckChangeDetails_Object = MibTableColumn
cfprComputeFwSyncAckChangeDetails = _CfprComputeFwSyncAckChangeDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 9),
    _CfprComputeFwSyncAckChangeDetails_Type()
)
cfprComputeFwSyncAckChangeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckChangeDetails.setStatus("current")
_CfprComputeFwSyncAckChanges_Type = CfprTrigAckChanges
_CfprComputeFwSyncAckChanges_Object = MibTableColumn
cfprComputeFwSyncAckChanges = _CfprComputeFwSyncAckChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 10),
    _CfprComputeFwSyncAckChanges_Type()
)
cfprComputeFwSyncAckChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckChanges.setStatus("current")
_CfprComputeFwSyncAckDescr_Type = SnmpAdminString
_CfprComputeFwSyncAckDescr_Object = MibTableColumn
cfprComputeFwSyncAckDescr = _CfprComputeFwSyncAckDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 11),
    _CfprComputeFwSyncAckDescr_Type()
)
cfprComputeFwSyncAckDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckDescr.setStatus("current")
_CfprComputeFwSyncAckDisr_Type = CfprTrigAckDisr
_CfprComputeFwSyncAckDisr_Object = MibTableColumn
cfprComputeFwSyncAckDisr = _CfprComputeFwSyncAckDisr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 12),
    _CfprComputeFwSyncAckDisr_Type()
)
cfprComputeFwSyncAckDisr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckDisr.setStatus("current")
_CfprComputeFwSyncAckIgnoreCap_Type = TruthValue
_CfprComputeFwSyncAckIgnoreCap_Object = MibTableColumn
cfprComputeFwSyncAckIgnoreCap = _CfprComputeFwSyncAckIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 13),
    _CfprComputeFwSyncAckIgnoreCap_Type()
)
cfprComputeFwSyncAckIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckIgnoreCap.setStatus("current")
_CfprComputeFwSyncAckIntId_Type = SnmpAdminString
_CfprComputeFwSyncAckIntId_Object = MibTableColumn
cfprComputeFwSyncAckIntId = _CfprComputeFwSyncAckIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 14),
    _CfprComputeFwSyncAckIntId_Type()
)
cfprComputeFwSyncAckIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckIntId.setStatus("current")
_CfprComputeFwSyncAckModified_Type = DateAndTime
_CfprComputeFwSyncAckModified_Object = MibTableColumn
cfprComputeFwSyncAckModified = _CfprComputeFwSyncAckModified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 15),
    _CfprComputeFwSyncAckModified_Type()
)
cfprComputeFwSyncAckModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckModified.setStatus("current")
_CfprComputeFwSyncAckName_Type = SnmpAdminString
_CfprComputeFwSyncAckName_Object = MibTableColumn
cfprComputeFwSyncAckName = _CfprComputeFwSyncAckName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 16),
    _CfprComputeFwSyncAckName_Type()
)
cfprComputeFwSyncAckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckName.setStatus("current")
_CfprComputeFwSyncAckOperScheduler_Type = SnmpAdminString
_CfprComputeFwSyncAckOperScheduler_Object = MibTableColumn
cfprComputeFwSyncAckOperScheduler = _CfprComputeFwSyncAckOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 17),
    _CfprComputeFwSyncAckOperScheduler_Type()
)
cfprComputeFwSyncAckOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckOperScheduler.setStatus("current")
_CfprComputeFwSyncAckOperState_Type = CfprTrigAckOperState
_CfprComputeFwSyncAckOperState_Object = MibTableColumn
cfprComputeFwSyncAckOperState = _CfprComputeFwSyncAckOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 18),
    _CfprComputeFwSyncAckOperState_Type()
)
cfprComputeFwSyncAckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckOperState.setStatus("current")
_CfprComputeFwSyncAckPolicyLevel_Type = Gauge32
_CfprComputeFwSyncAckPolicyLevel_Object = MibTableColumn
cfprComputeFwSyncAckPolicyLevel = _CfprComputeFwSyncAckPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 19),
    _CfprComputeFwSyncAckPolicyLevel_Type()
)
cfprComputeFwSyncAckPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckPolicyLevel.setStatus("current")
_CfprComputeFwSyncAckPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeFwSyncAckPolicyOwner_Object = MibTableColumn
cfprComputeFwSyncAckPolicyOwner = _CfprComputeFwSyncAckPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 20),
    _CfprComputeFwSyncAckPolicyOwner_Type()
)
cfprComputeFwSyncAckPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckPolicyOwner.setStatus("current")
_CfprComputeFwSyncAckPrevOperState_Type = CfprTrigAckPrevOperState
_CfprComputeFwSyncAckPrevOperState_Object = MibTableColumn
cfprComputeFwSyncAckPrevOperState = _CfprComputeFwSyncAckPrevOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 21),
    _CfprComputeFwSyncAckPrevOperState_Type()
)
cfprComputeFwSyncAckPrevOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckPrevOperState.setStatus("current")
_CfprComputeFwSyncAckScheduler_Type = SnmpAdminString
_CfprComputeFwSyncAckScheduler_Object = MibTableColumn
cfprComputeFwSyncAckScheduler = _CfprComputeFwSyncAckScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 16, 1, 22),
    _CfprComputeFwSyncAckScheduler_Type()
)
cfprComputeFwSyncAckScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeFwSyncAckScheduler.setStatus("current")
_CfprComputeHealthLedSensorAlarmTable_Object = MibTable
cfprComputeHealthLedSensorAlarmTable = _CfprComputeHealthLedSensorAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17)
)
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmTable.setStatus("current")
_CfprComputeHealthLedSensorAlarmEntry_Object = MibTableRow
cfprComputeHealthLedSensorAlarmEntry = _CfprComputeHealthLedSensorAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17, 1)
)
cfprComputeHealthLedSensorAlarmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeHealthLedSensorAlarmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmEntry.setStatus("current")
_CfprComputeHealthLedSensorAlarmInstanceId_Type = CfprManagedObjectId
_CfprComputeHealthLedSensorAlarmInstanceId_Object = MibTableColumn
cfprComputeHealthLedSensorAlarmInstanceId = _CfprComputeHealthLedSensorAlarmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17, 1, 1),
    _CfprComputeHealthLedSensorAlarmInstanceId_Type()
)
cfprComputeHealthLedSensorAlarmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmInstanceId.setStatus("current")
_CfprComputeHealthLedSensorAlarmDn_Type = CfprManagedObjectDn
_CfprComputeHealthLedSensorAlarmDn_Object = MibTableColumn
cfprComputeHealthLedSensorAlarmDn = _CfprComputeHealthLedSensorAlarmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17, 1, 2),
    _CfprComputeHealthLedSensorAlarmDn_Type()
)
cfprComputeHealthLedSensorAlarmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmDn.setStatus("current")
_CfprComputeHealthLedSensorAlarmRn_Type = SnmpAdminString
_CfprComputeHealthLedSensorAlarmRn_Object = MibTableColumn
cfprComputeHealthLedSensorAlarmRn = _CfprComputeHealthLedSensorAlarmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17, 1, 3),
    _CfprComputeHealthLedSensorAlarmRn_Type()
)
cfprComputeHealthLedSensorAlarmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmRn.setStatus("current")
_CfprComputeHealthLedSensorAlarmAlarmDesc_Type = SnmpAdminString
_CfprComputeHealthLedSensorAlarmAlarmDesc_Object = MibTableColumn
cfprComputeHealthLedSensorAlarmAlarmDesc = _CfprComputeHealthLedSensorAlarmAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17, 1, 4),
    _CfprComputeHealthLedSensorAlarmAlarmDesc_Type()
)
cfprComputeHealthLedSensorAlarmAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmAlarmDesc.setStatus("current")
_CfprComputeHealthLedSensorAlarmAlarmSeverity_Type = CfprComputeAlarmSeverity
_CfprComputeHealthLedSensorAlarmAlarmSeverity_Object = MibTableColumn
cfprComputeHealthLedSensorAlarmAlarmSeverity = _CfprComputeHealthLedSensorAlarmAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17, 1, 5),
    _CfprComputeHealthLedSensorAlarmAlarmSeverity_Type()
)
cfprComputeHealthLedSensorAlarmAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmAlarmSeverity.setStatus("current")
_CfprComputeHealthLedSensorAlarmSensorId_Type = Gauge32
_CfprComputeHealthLedSensorAlarmSensorId_Object = MibTableColumn
cfprComputeHealthLedSensorAlarmSensorId = _CfprComputeHealthLedSensorAlarmSensorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17, 1, 6),
    _CfprComputeHealthLedSensorAlarmSensorId_Type()
)
cfprComputeHealthLedSensorAlarmSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmSensorId.setStatus("current")
_CfprComputeHealthLedSensorAlarmSensorName_Type = SnmpAdminString
_CfprComputeHealthLedSensorAlarmSensorName_Object = MibTableColumn
cfprComputeHealthLedSensorAlarmSensorName = _CfprComputeHealthLedSensorAlarmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 17, 1, 7),
    _CfprComputeHealthLedSensorAlarmSensorName_Type()
)
cfprComputeHealthLedSensorAlarmSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeHealthLedSensorAlarmSensorName.setStatus("current")
_CfprComputeIOHubTable_Object = MibTable
cfprComputeIOHubTable = _CfprComputeIOHubTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18)
)
if mibBuilder.loadTexts:
    cfprComputeIOHubTable.setStatus("current")
_CfprComputeIOHubEntry_Object = MibTableRow
cfprComputeIOHubEntry = _CfprComputeIOHubEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1)
)
cfprComputeIOHubEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeIOHubInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeIOHubEntry.setStatus("current")
_CfprComputeIOHubInstanceId_Type = CfprManagedObjectId
_CfprComputeIOHubInstanceId_Object = MibTableColumn
cfprComputeIOHubInstanceId = _CfprComputeIOHubInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 1),
    _CfprComputeIOHubInstanceId_Type()
)
cfprComputeIOHubInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeIOHubInstanceId.setStatus("current")
_CfprComputeIOHubDn_Type = CfprManagedObjectDn
_CfprComputeIOHubDn_Object = MibTableColumn
cfprComputeIOHubDn = _CfprComputeIOHubDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 2),
    _CfprComputeIOHubDn_Type()
)
cfprComputeIOHubDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubDn.setStatus("current")
_CfprComputeIOHubRn_Type = SnmpAdminString
_CfprComputeIOHubRn_Object = MibTableColumn
cfprComputeIOHubRn = _CfprComputeIOHubRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 3),
    _CfprComputeIOHubRn_Type()
)
cfprComputeIOHubRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubRn.setStatus("current")
_CfprComputeIOHubId_Type = Gauge32
_CfprComputeIOHubId_Object = MibTableColumn
cfprComputeIOHubId = _CfprComputeIOHubId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 4),
    _CfprComputeIOHubId_Type()
)
cfprComputeIOHubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubId.setStatus("current")
_CfprComputeIOHubLocationDn_Type = SnmpAdminString
_CfprComputeIOHubLocationDn_Object = MibTableColumn
cfprComputeIOHubLocationDn = _CfprComputeIOHubLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 5),
    _CfprComputeIOHubLocationDn_Type()
)
cfprComputeIOHubLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubLocationDn.setStatus("current")
_CfprComputeIOHubModel_Type = SnmpAdminString
_CfprComputeIOHubModel_Object = MibTableColumn
cfprComputeIOHubModel = _CfprComputeIOHubModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 6),
    _CfprComputeIOHubModel_Type()
)
cfprComputeIOHubModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubModel.setStatus("current")
_CfprComputeIOHubOperQualifierReason_Type = SnmpAdminString
_CfprComputeIOHubOperQualifierReason_Object = MibTableColumn
cfprComputeIOHubOperQualifierReason = _CfprComputeIOHubOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 7),
    _CfprComputeIOHubOperQualifierReason_Type()
)
cfprComputeIOHubOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubOperQualifierReason.setStatus("current")
_CfprComputeIOHubOperState_Type = CfprEquipmentOperability
_CfprComputeIOHubOperState_Object = MibTableColumn
cfprComputeIOHubOperState = _CfprComputeIOHubOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 8),
    _CfprComputeIOHubOperState_Type()
)
cfprComputeIOHubOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubOperState.setStatus("current")
_CfprComputeIOHubOperability_Type = CfprEquipmentOperability
_CfprComputeIOHubOperability_Object = MibTableColumn
cfprComputeIOHubOperability = _CfprComputeIOHubOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 9),
    _CfprComputeIOHubOperability_Type()
)
cfprComputeIOHubOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubOperability.setStatus("current")
_CfprComputeIOHubPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeIOHubPerf_Object = MibTableColumn
cfprComputeIOHubPerf = _CfprComputeIOHubPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 10),
    _CfprComputeIOHubPerf_Type()
)
cfprComputeIOHubPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubPerf.setStatus("current")
_CfprComputeIOHubPower_Type = CfprEquipmentPowerState
_CfprComputeIOHubPower_Object = MibTableColumn
cfprComputeIOHubPower = _CfprComputeIOHubPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 11),
    _CfprComputeIOHubPower_Type()
)
cfprComputeIOHubPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubPower.setStatus("current")
_CfprComputeIOHubPresence_Type = CfprEquipmentPresence
_CfprComputeIOHubPresence_Object = MibTableColumn
cfprComputeIOHubPresence = _CfprComputeIOHubPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 12),
    _CfprComputeIOHubPresence_Type()
)
cfprComputeIOHubPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubPresence.setStatus("current")
_CfprComputeIOHubRevision_Type = SnmpAdminString
_CfprComputeIOHubRevision_Object = MibTableColumn
cfprComputeIOHubRevision = _CfprComputeIOHubRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 13),
    _CfprComputeIOHubRevision_Type()
)
cfprComputeIOHubRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubRevision.setStatus("current")
_CfprComputeIOHubSerial_Type = SnmpAdminString
_CfprComputeIOHubSerial_Object = MibTableColumn
cfprComputeIOHubSerial = _CfprComputeIOHubSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 14),
    _CfprComputeIOHubSerial_Type()
)
cfprComputeIOHubSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubSerial.setStatus("current")
_CfprComputeIOHubThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeIOHubThermal_Object = MibTableColumn
cfprComputeIOHubThermal = _CfprComputeIOHubThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 15),
    _CfprComputeIOHubThermal_Type()
)
cfprComputeIOHubThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubThermal.setStatus("current")
_CfprComputeIOHubVendor_Type = SnmpAdminString
_CfprComputeIOHubVendor_Object = MibTableColumn
cfprComputeIOHubVendor = _CfprComputeIOHubVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 16),
    _CfprComputeIOHubVendor_Type()
)
cfprComputeIOHubVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubVendor.setStatus("current")
_CfprComputeIOHubVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeIOHubVoltage_Object = MibTableColumn
cfprComputeIOHubVoltage = _CfprComputeIOHubVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 18, 1, 17),
    _CfprComputeIOHubVoltage_Type()
)
cfprComputeIOHubVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubVoltage.setStatus("current")
_CfprComputeIOHubEnvStatsTable_Object = MibTable
cfprComputeIOHubEnvStatsTable = _CfprComputeIOHubEnvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19)
)
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsTable.setStatus("current")
_CfprComputeIOHubEnvStatsEntry_Object = MibTableRow
cfprComputeIOHubEnvStatsEntry = _CfprComputeIOHubEnvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1)
)
cfprComputeIOHubEnvStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeIOHubEnvStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsEntry.setStatus("current")
_CfprComputeIOHubEnvStatsInstanceId_Type = CfprManagedObjectId
_CfprComputeIOHubEnvStatsInstanceId_Object = MibTableColumn
cfprComputeIOHubEnvStatsInstanceId = _CfprComputeIOHubEnvStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 1),
    _CfprComputeIOHubEnvStatsInstanceId_Type()
)
cfprComputeIOHubEnvStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsInstanceId.setStatus("current")
_CfprComputeIOHubEnvStatsDn_Type = CfprManagedObjectDn
_CfprComputeIOHubEnvStatsDn_Object = MibTableColumn
cfprComputeIOHubEnvStatsDn = _CfprComputeIOHubEnvStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 2),
    _CfprComputeIOHubEnvStatsDn_Type()
)
cfprComputeIOHubEnvStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsDn.setStatus("current")
_CfprComputeIOHubEnvStatsRn_Type = SnmpAdminString
_CfprComputeIOHubEnvStatsRn_Object = MibTableColumn
cfprComputeIOHubEnvStatsRn = _CfprComputeIOHubEnvStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 3),
    _CfprComputeIOHubEnvStatsRn_Type()
)
cfprComputeIOHubEnvStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsRn.setStatus("current")
_CfprComputeIOHubEnvStatsIntervals_Type = Gauge32
_CfprComputeIOHubEnvStatsIntervals_Object = MibTableColumn
cfprComputeIOHubEnvStatsIntervals = _CfprComputeIOHubEnvStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 4),
    _CfprComputeIOHubEnvStatsIntervals_Type()
)
cfprComputeIOHubEnvStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsIntervals.setStatus("current")
_CfprComputeIOHubEnvStatsSuspect_Type = TruthValue
_CfprComputeIOHubEnvStatsSuspect_Object = MibTableColumn
cfprComputeIOHubEnvStatsSuspect = _CfprComputeIOHubEnvStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 5),
    _CfprComputeIOHubEnvStatsSuspect_Type()
)
cfprComputeIOHubEnvStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsSuspect.setStatus("current")
_CfprComputeIOHubEnvStatsTemperature_Type = Integer32
_CfprComputeIOHubEnvStatsTemperature_Object = MibTableColumn
cfprComputeIOHubEnvStatsTemperature = _CfprComputeIOHubEnvStatsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 6),
    _CfprComputeIOHubEnvStatsTemperature_Type()
)
cfprComputeIOHubEnvStatsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsTemperature.setStatus("current")
_CfprComputeIOHubEnvStatsTemperatureAvg_Type = Integer32
_CfprComputeIOHubEnvStatsTemperatureAvg_Object = MibTableColumn
cfprComputeIOHubEnvStatsTemperatureAvg = _CfprComputeIOHubEnvStatsTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 7),
    _CfprComputeIOHubEnvStatsTemperatureAvg_Type()
)
cfprComputeIOHubEnvStatsTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsTemperatureAvg.setStatus("current")
_CfprComputeIOHubEnvStatsTemperatureMax_Type = Integer32
_CfprComputeIOHubEnvStatsTemperatureMax_Object = MibTableColumn
cfprComputeIOHubEnvStatsTemperatureMax = _CfprComputeIOHubEnvStatsTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 8),
    _CfprComputeIOHubEnvStatsTemperatureMax_Type()
)
cfprComputeIOHubEnvStatsTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsTemperatureMax.setStatus("current")
_CfprComputeIOHubEnvStatsTemperatureMin_Type = Integer32
_CfprComputeIOHubEnvStatsTemperatureMin_Object = MibTableColumn
cfprComputeIOHubEnvStatsTemperatureMin = _CfprComputeIOHubEnvStatsTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 9),
    _CfprComputeIOHubEnvStatsTemperatureMin_Type()
)
cfprComputeIOHubEnvStatsTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsTemperatureMin.setStatus("current")
_CfprComputeIOHubEnvStatsThresholded_Type = CfprComputeIOHubEnvStatsThresholded
_CfprComputeIOHubEnvStatsThresholded_Object = MibTableColumn
cfprComputeIOHubEnvStatsThresholded = _CfprComputeIOHubEnvStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 10),
    _CfprComputeIOHubEnvStatsThresholded_Type()
)
cfprComputeIOHubEnvStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsThresholded.setStatus("current")
_CfprComputeIOHubEnvStatsTimeCollected_Type = DateAndTime
_CfprComputeIOHubEnvStatsTimeCollected_Object = MibTableColumn
cfprComputeIOHubEnvStatsTimeCollected = _CfprComputeIOHubEnvStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 11),
    _CfprComputeIOHubEnvStatsTimeCollected_Type()
)
cfprComputeIOHubEnvStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsTimeCollected.setStatus("current")
_CfprComputeIOHubEnvStatsUpdate_Type = Gauge32
_CfprComputeIOHubEnvStatsUpdate_Object = MibTableColumn
cfprComputeIOHubEnvStatsUpdate = _CfprComputeIOHubEnvStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 19, 1, 12),
    _CfprComputeIOHubEnvStatsUpdate_Type()
)
cfprComputeIOHubEnvStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsUpdate.setStatus("current")
_CfprComputeIOHubEnvStatsHistTable_Object = MibTable
cfprComputeIOHubEnvStatsHistTable = _CfprComputeIOHubEnvStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20)
)
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistTable.setStatus("current")
_CfprComputeIOHubEnvStatsHistEntry_Object = MibTableRow
cfprComputeIOHubEnvStatsHistEntry = _CfprComputeIOHubEnvStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1)
)
cfprComputeIOHubEnvStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeIOHubEnvStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistEntry.setStatus("current")
_CfprComputeIOHubEnvStatsHistInstanceId_Type = CfprManagedObjectId
_CfprComputeIOHubEnvStatsHistInstanceId_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistInstanceId = _CfprComputeIOHubEnvStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 1),
    _CfprComputeIOHubEnvStatsHistInstanceId_Type()
)
cfprComputeIOHubEnvStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistInstanceId.setStatus("current")
_CfprComputeIOHubEnvStatsHistDn_Type = CfprManagedObjectDn
_CfprComputeIOHubEnvStatsHistDn_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistDn = _CfprComputeIOHubEnvStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 2),
    _CfprComputeIOHubEnvStatsHistDn_Type()
)
cfprComputeIOHubEnvStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistDn.setStatus("current")
_CfprComputeIOHubEnvStatsHistRn_Type = SnmpAdminString
_CfprComputeIOHubEnvStatsHistRn_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistRn = _CfprComputeIOHubEnvStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 3),
    _CfprComputeIOHubEnvStatsHistRn_Type()
)
cfprComputeIOHubEnvStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistRn.setStatus("current")
_CfprComputeIOHubEnvStatsHistId_Type = Unsigned64
_CfprComputeIOHubEnvStatsHistId_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistId = _CfprComputeIOHubEnvStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 4),
    _CfprComputeIOHubEnvStatsHistId_Type()
)
cfprComputeIOHubEnvStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistId.setStatus("current")
_CfprComputeIOHubEnvStatsHistMostRecent_Type = TruthValue
_CfprComputeIOHubEnvStatsHistMostRecent_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistMostRecent = _CfprComputeIOHubEnvStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 5),
    _CfprComputeIOHubEnvStatsHistMostRecent_Type()
)
cfprComputeIOHubEnvStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistMostRecent.setStatus("current")
_CfprComputeIOHubEnvStatsHistSuspect_Type = TruthValue
_CfprComputeIOHubEnvStatsHistSuspect_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistSuspect = _CfprComputeIOHubEnvStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 6),
    _CfprComputeIOHubEnvStatsHistSuspect_Type()
)
cfprComputeIOHubEnvStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistSuspect.setStatus("current")
_CfprComputeIOHubEnvStatsHistTemperature_Type = Integer32
_CfprComputeIOHubEnvStatsHistTemperature_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistTemperature = _CfprComputeIOHubEnvStatsHistTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 7),
    _CfprComputeIOHubEnvStatsHistTemperature_Type()
)
cfprComputeIOHubEnvStatsHistTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistTemperature.setStatus("current")
_CfprComputeIOHubEnvStatsHistTemperatureAvg_Type = Integer32
_CfprComputeIOHubEnvStatsHistTemperatureAvg_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistTemperatureAvg = _CfprComputeIOHubEnvStatsHistTemperatureAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 8),
    _CfprComputeIOHubEnvStatsHistTemperatureAvg_Type()
)
cfprComputeIOHubEnvStatsHistTemperatureAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistTemperatureAvg.setStatus("current")
_CfprComputeIOHubEnvStatsHistTemperatureMax_Type = Integer32
_CfprComputeIOHubEnvStatsHistTemperatureMax_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistTemperatureMax = _CfprComputeIOHubEnvStatsHistTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 9),
    _CfprComputeIOHubEnvStatsHistTemperatureMax_Type()
)
cfprComputeIOHubEnvStatsHistTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistTemperatureMax.setStatus("current")
_CfprComputeIOHubEnvStatsHistTemperatureMin_Type = Integer32
_CfprComputeIOHubEnvStatsHistTemperatureMin_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistTemperatureMin = _CfprComputeIOHubEnvStatsHistTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 10),
    _CfprComputeIOHubEnvStatsHistTemperatureMin_Type()
)
cfprComputeIOHubEnvStatsHistTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistTemperatureMin.setStatus("current")
_CfprComputeIOHubEnvStatsHistThresholded_Type = CfprComputeIOHubEnvStatsHistThresholded
_CfprComputeIOHubEnvStatsHistThresholded_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistThresholded = _CfprComputeIOHubEnvStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 11),
    _CfprComputeIOHubEnvStatsHistThresholded_Type()
)
cfprComputeIOHubEnvStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistThresholded.setStatus("current")
_CfprComputeIOHubEnvStatsHistTimeCollected_Type = DateAndTime
_CfprComputeIOHubEnvStatsHistTimeCollected_Object = MibTableColumn
cfprComputeIOHubEnvStatsHistTimeCollected = _CfprComputeIOHubEnvStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 20, 1, 12),
    _CfprComputeIOHubEnvStatsHistTimeCollected_Type()
)
cfprComputeIOHubEnvStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeIOHubEnvStatsHistTimeCollected.setStatus("current")
_CfprComputeKvmMgmtPolicyTable_Object = MibTable
cfprComputeKvmMgmtPolicyTable = _CfprComputeKvmMgmtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21)
)
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyTable.setStatus("current")
_CfprComputeKvmMgmtPolicyEntry_Object = MibTableRow
cfprComputeKvmMgmtPolicyEntry = _CfprComputeKvmMgmtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1)
)
cfprComputeKvmMgmtPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeKvmMgmtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyEntry.setStatus("current")
_CfprComputeKvmMgmtPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeKvmMgmtPolicyInstanceId_Object = MibTableColumn
cfprComputeKvmMgmtPolicyInstanceId = _CfprComputeKvmMgmtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 1),
    _CfprComputeKvmMgmtPolicyInstanceId_Type()
)
cfprComputeKvmMgmtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyInstanceId.setStatus("current")
_CfprComputeKvmMgmtPolicyDn_Type = CfprManagedObjectDn
_CfprComputeKvmMgmtPolicyDn_Object = MibTableColumn
cfprComputeKvmMgmtPolicyDn = _CfprComputeKvmMgmtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 2),
    _CfprComputeKvmMgmtPolicyDn_Type()
)
cfprComputeKvmMgmtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyDn.setStatus("current")
_CfprComputeKvmMgmtPolicyRn_Type = SnmpAdminString
_CfprComputeKvmMgmtPolicyRn_Object = MibTableColumn
cfprComputeKvmMgmtPolicyRn = _CfprComputeKvmMgmtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 3),
    _CfprComputeKvmMgmtPolicyRn_Type()
)
cfprComputeKvmMgmtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyRn.setStatus("current")
_CfprComputeKvmMgmtPolicyDescr_Type = SnmpAdminString
_CfprComputeKvmMgmtPolicyDescr_Object = MibTableColumn
cfprComputeKvmMgmtPolicyDescr = _CfprComputeKvmMgmtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 4),
    _CfprComputeKvmMgmtPolicyDescr_Type()
)
cfprComputeKvmMgmtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyDescr.setStatus("current")
_CfprComputeKvmMgmtPolicyIntId_Type = SnmpAdminString
_CfprComputeKvmMgmtPolicyIntId_Object = MibTableColumn
cfprComputeKvmMgmtPolicyIntId = _CfprComputeKvmMgmtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 5),
    _CfprComputeKvmMgmtPolicyIntId_Type()
)
cfprComputeKvmMgmtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyIntId.setStatus("current")
_CfprComputeKvmMgmtPolicyName_Type = SnmpAdminString
_CfprComputeKvmMgmtPolicyName_Object = MibTableColumn
cfprComputeKvmMgmtPolicyName = _CfprComputeKvmMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 6),
    _CfprComputeKvmMgmtPolicyName_Type()
)
cfprComputeKvmMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyName.setStatus("current")
_CfprComputeKvmMgmtPolicyPolicyLevel_Type = Gauge32
_CfprComputeKvmMgmtPolicyPolicyLevel_Object = MibTableColumn
cfprComputeKvmMgmtPolicyPolicyLevel = _CfprComputeKvmMgmtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 7),
    _CfprComputeKvmMgmtPolicyPolicyLevel_Type()
)
cfprComputeKvmMgmtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyPolicyLevel.setStatus("current")
_CfprComputeKvmMgmtPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeKvmMgmtPolicyPolicyOwner_Object = MibTableColumn
cfprComputeKvmMgmtPolicyPolicyOwner = _CfprComputeKvmMgmtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 8),
    _CfprComputeKvmMgmtPolicyPolicyOwner_Type()
)
cfprComputeKvmMgmtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyPolicyOwner.setStatus("current")
_CfprComputeKvmMgmtPolicyVmediaEncryption_Type = CfprComputeKvmMgmtPolicyVmediaEncryption
_CfprComputeKvmMgmtPolicyVmediaEncryption_Object = MibTableColumn
cfprComputeKvmMgmtPolicyVmediaEncryption = _CfprComputeKvmMgmtPolicyVmediaEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 21, 1, 9),
    _CfprComputeKvmMgmtPolicyVmediaEncryption_Type()
)
cfprComputeKvmMgmtPolicyVmediaEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeKvmMgmtPolicyVmediaEncryption.setStatus("current")
_CfprComputeMbPowerStatsTable_Object = MibTable
cfprComputeMbPowerStatsTable = _CfprComputeMbPowerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22)
)
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsTable.setStatus("current")
_CfprComputeMbPowerStatsEntry_Object = MibTableRow
cfprComputeMbPowerStatsEntry = _CfprComputeMbPowerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1)
)
cfprComputeMbPowerStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeMbPowerStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsEntry.setStatus("current")
_CfprComputeMbPowerStatsInstanceId_Type = CfprManagedObjectId
_CfprComputeMbPowerStatsInstanceId_Object = MibTableColumn
cfprComputeMbPowerStatsInstanceId = _CfprComputeMbPowerStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 1),
    _CfprComputeMbPowerStatsInstanceId_Type()
)
cfprComputeMbPowerStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInstanceId.setStatus("current")
_CfprComputeMbPowerStatsDn_Type = CfprManagedObjectDn
_CfprComputeMbPowerStatsDn_Object = MibTableColumn
cfprComputeMbPowerStatsDn = _CfprComputeMbPowerStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 2),
    _CfprComputeMbPowerStatsDn_Type()
)
cfprComputeMbPowerStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsDn.setStatus("current")
_CfprComputeMbPowerStatsRn_Type = SnmpAdminString
_CfprComputeMbPowerStatsRn_Object = MibTableColumn
cfprComputeMbPowerStatsRn = _CfprComputeMbPowerStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 3),
    _CfprComputeMbPowerStatsRn_Type()
)
cfprComputeMbPowerStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsRn.setStatus("current")
_CfprComputeMbPowerStatsConsumedPower_Type = Integer32
_CfprComputeMbPowerStatsConsumedPower_Object = MibTableColumn
cfprComputeMbPowerStatsConsumedPower = _CfprComputeMbPowerStatsConsumedPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 4),
    _CfprComputeMbPowerStatsConsumedPower_Type()
)
cfprComputeMbPowerStatsConsumedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsConsumedPower.setStatus("current")
_CfprComputeMbPowerStatsConsumedPowerAvg_Type = Integer32
_CfprComputeMbPowerStatsConsumedPowerAvg_Object = MibTableColumn
cfprComputeMbPowerStatsConsumedPowerAvg = _CfprComputeMbPowerStatsConsumedPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 5),
    _CfprComputeMbPowerStatsConsumedPowerAvg_Type()
)
cfprComputeMbPowerStatsConsumedPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsConsumedPowerAvg.setStatus("current")
_CfprComputeMbPowerStatsConsumedPowerMax_Type = Integer32
_CfprComputeMbPowerStatsConsumedPowerMax_Object = MibTableColumn
cfprComputeMbPowerStatsConsumedPowerMax = _CfprComputeMbPowerStatsConsumedPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 6),
    _CfprComputeMbPowerStatsConsumedPowerMax_Type()
)
cfprComputeMbPowerStatsConsumedPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsConsumedPowerMax.setStatus("current")
_CfprComputeMbPowerStatsConsumedPowerMin_Type = Integer32
_CfprComputeMbPowerStatsConsumedPowerMin_Object = MibTableColumn
cfprComputeMbPowerStatsConsumedPowerMin = _CfprComputeMbPowerStatsConsumedPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 7),
    _CfprComputeMbPowerStatsConsumedPowerMin_Type()
)
cfprComputeMbPowerStatsConsumedPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsConsumedPowerMin.setStatus("current")
_CfprComputeMbPowerStatsInputCurrent_Type = Integer32
_CfprComputeMbPowerStatsInputCurrent_Object = MibTableColumn
cfprComputeMbPowerStatsInputCurrent = _CfprComputeMbPowerStatsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 8),
    _CfprComputeMbPowerStatsInputCurrent_Type()
)
cfprComputeMbPowerStatsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInputCurrent.setStatus("current")
_CfprComputeMbPowerStatsInputCurrentAvg_Type = Integer32
_CfprComputeMbPowerStatsInputCurrentAvg_Object = MibTableColumn
cfprComputeMbPowerStatsInputCurrentAvg = _CfprComputeMbPowerStatsInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 9),
    _CfprComputeMbPowerStatsInputCurrentAvg_Type()
)
cfprComputeMbPowerStatsInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInputCurrentAvg.setStatus("current")
_CfprComputeMbPowerStatsInputCurrentMax_Type = Integer32
_CfprComputeMbPowerStatsInputCurrentMax_Object = MibTableColumn
cfprComputeMbPowerStatsInputCurrentMax = _CfprComputeMbPowerStatsInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 10),
    _CfprComputeMbPowerStatsInputCurrentMax_Type()
)
cfprComputeMbPowerStatsInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInputCurrentMax.setStatus("current")
_CfprComputeMbPowerStatsInputCurrentMin_Type = Integer32
_CfprComputeMbPowerStatsInputCurrentMin_Object = MibTableColumn
cfprComputeMbPowerStatsInputCurrentMin = _CfprComputeMbPowerStatsInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 11),
    _CfprComputeMbPowerStatsInputCurrentMin_Type()
)
cfprComputeMbPowerStatsInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInputCurrentMin.setStatus("current")
_CfprComputeMbPowerStatsInputVoltage_Type = Integer32
_CfprComputeMbPowerStatsInputVoltage_Object = MibTableColumn
cfprComputeMbPowerStatsInputVoltage = _CfprComputeMbPowerStatsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 12),
    _CfprComputeMbPowerStatsInputVoltage_Type()
)
cfprComputeMbPowerStatsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInputVoltage.setStatus("current")
_CfprComputeMbPowerStatsInputVoltageAvg_Type = Integer32
_CfprComputeMbPowerStatsInputVoltageAvg_Object = MibTableColumn
cfprComputeMbPowerStatsInputVoltageAvg = _CfprComputeMbPowerStatsInputVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 13),
    _CfprComputeMbPowerStatsInputVoltageAvg_Type()
)
cfprComputeMbPowerStatsInputVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInputVoltageAvg.setStatus("current")
_CfprComputeMbPowerStatsInputVoltageMax_Type = Integer32
_CfprComputeMbPowerStatsInputVoltageMax_Object = MibTableColumn
cfprComputeMbPowerStatsInputVoltageMax = _CfprComputeMbPowerStatsInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 14),
    _CfprComputeMbPowerStatsInputVoltageMax_Type()
)
cfprComputeMbPowerStatsInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInputVoltageMax.setStatus("current")
_CfprComputeMbPowerStatsInputVoltageMin_Type = Integer32
_CfprComputeMbPowerStatsInputVoltageMin_Object = MibTableColumn
cfprComputeMbPowerStatsInputVoltageMin = _CfprComputeMbPowerStatsInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 15),
    _CfprComputeMbPowerStatsInputVoltageMin_Type()
)
cfprComputeMbPowerStatsInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsInputVoltageMin.setStatus("current")
_CfprComputeMbPowerStatsIntervals_Type = Gauge32
_CfprComputeMbPowerStatsIntervals_Object = MibTableColumn
cfprComputeMbPowerStatsIntervals = _CfprComputeMbPowerStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 16),
    _CfprComputeMbPowerStatsIntervals_Type()
)
cfprComputeMbPowerStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsIntervals.setStatus("current")
_CfprComputeMbPowerStatsSuspect_Type = TruthValue
_CfprComputeMbPowerStatsSuspect_Object = MibTableColumn
cfprComputeMbPowerStatsSuspect = _CfprComputeMbPowerStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 17),
    _CfprComputeMbPowerStatsSuspect_Type()
)
cfprComputeMbPowerStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsSuspect.setStatus("current")
_CfprComputeMbPowerStatsThresholded_Type = CfprComputeMbPowerStatsThresholded
_CfprComputeMbPowerStatsThresholded_Object = MibTableColumn
cfprComputeMbPowerStatsThresholded = _CfprComputeMbPowerStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 18),
    _CfprComputeMbPowerStatsThresholded_Type()
)
cfprComputeMbPowerStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsThresholded.setStatus("current")
_CfprComputeMbPowerStatsTimeCollected_Type = DateAndTime
_CfprComputeMbPowerStatsTimeCollected_Object = MibTableColumn
cfprComputeMbPowerStatsTimeCollected = _CfprComputeMbPowerStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 19),
    _CfprComputeMbPowerStatsTimeCollected_Type()
)
cfprComputeMbPowerStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsTimeCollected.setStatus("current")
_CfprComputeMbPowerStatsUpdate_Type = Gauge32
_CfprComputeMbPowerStatsUpdate_Object = MibTableColumn
cfprComputeMbPowerStatsUpdate = _CfprComputeMbPowerStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 22, 1, 20),
    _CfprComputeMbPowerStatsUpdate_Type()
)
cfprComputeMbPowerStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsUpdate.setStatus("current")
_CfprComputeMbPowerStatsHistTable_Object = MibTable
cfprComputeMbPowerStatsHistTable = _CfprComputeMbPowerStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23)
)
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistTable.setStatus("current")
_CfprComputeMbPowerStatsHistEntry_Object = MibTableRow
cfprComputeMbPowerStatsHistEntry = _CfprComputeMbPowerStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1)
)
cfprComputeMbPowerStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeMbPowerStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistEntry.setStatus("current")
_CfprComputeMbPowerStatsHistInstanceId_Type = CfprManagedObjectId
_CfprComputeMbPowerStatsHistInstanceId_Object = MibTableColumn
cfprComputeMbPowerStatsHistInstanceId = _CfprComputeMbPowerStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 1),
    _CfprComputeMbPowerStatsHistInstanceId_Type()
)
cfprComputeMbPowerStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInstanceId.setStatus("current")
_CfprComputeMbPowerStatsHistDn_Type = CfprManagedObjectDn
_CfprComputeMbPowerStatsHistDn_Object = MibTableColumn
cfprComputeMbPowerStatsHistDn = _CfprComputeMbPowerStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 2),
    _CfprComputeMbPowerStatsHistDn_Type()
)
cfprComputeMbPowerStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistDn.setStatus("current")
_CfprComputeMbPowerStatsHistRn_Type = SnmpAdminString
_CfprComputeMbPowerStatsHistRn_Object = MibTableColumn
cfprComputeMbPowerStatsHistRn = _CfprComputeMbPowerStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 3),
    _CfprComputeMbPowerStatsHistRn_Type()
)
cfprComputeMbPowerStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistRn.setStatus("current")
_CfprComputeMbPowerStatsHistConsumedPower_Type = Integer32
_CfprComputeMbPowerStatsHistConsumedPower_Object = MibTableColumn
cfprComputeMbPowerStatsHistConsumedPower = _CfprComputeMbPowerStatsHistConsumedPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 4),
    _CfprComputeMbPowerStatsHistConsumedPower_Type()
)
cfprComputeMbPowerStatsHistConsumedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistConsumedPower.setStatus("current")
_CfprComputeMbPowerStatsHistConsumedPowerAvg_Type = Integer32
_CfprComputeMbPowerStatsHistConsumedPowerAvg_Object = MibTableColumn
cfprComputeMbPowerStatsHistConsumedPowerAvg = _CfprComputeMbPowerStatsHistConsumedPowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 5),
    _CfprComputeMbPowerStatsHistConsumedPowerAvg_Type()
)
cfprComputeMbPowerStatsHistConsumedPowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistConsumedPowerAvg.setStatus("current")
_CfprComputeMbPowerStatsHistConsumedPowerMax_Type = Integer32
_CfprComputeMbPowerStatsHistConsumedPowerMax_Object = MibTableColumn
cfprComputeMbPowerStatsHistConsumedPowerMax = _CfprComputeMbPowerStatsHistConsumedPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 6),
    _CfprComputeMbPowerStatsHistConsumedPowerMax_Type()
)
cfprComputeMbPowerStatsHistConsumedPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistConsumedPowerMax.setStatus("current")
_CfprComputeMbPowerStatsHistConsumedPowerMin_Type = Integer32
_CfprComputeMbPowerStatsHistConsumedPowerMin_Object = MibTableColumn
cfprComputeMbPowerStatsHistConsumedPowerMin = _CfprComputeMbPowerStatsHistConsumedPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 7),
    _CfprComputeMbPowerStatsHistConsumedPowerMin_Type()
)
cfprComputeMbPowerStatsHistConsumedPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistConsumedPowerMin.setStatus("current")
_CfprComputeMbPowerStatsHistId_Type = Unsigned64
_CfprComputeMbPowerStatsHistId_Object = MibTableColumn
cfprComputeMbPowerStatsHistId = _CfprComputeMbPowerStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 8),
    _CfprComputeMbPowerStatsHistId_Type()
)
cfprComputeMbPowerStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistId.setStatus("current")
_CfprComputeMbPowerStatsHistInputCurrent_Type = Integer32
_CfprComputeMbPowerStatsHistInputCurrent_Object = MibTableColumn
cfprComputeMbPowerStatsHistInputCurrent = _CfprComputeMbPowerStatsHistInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 9),
    _CfprComputeMbPowerStatsHistInputCurrent_Type()
)
cfprComputeMbPowerStatsHistInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInputCurrent.setStatus("current")
_CfprComputeMbPowerStatsHistInputCurrentAvg_Type = Integer32
_CfprComputeMbPowerStatsHistInputCurrentAvg_Object = MibTableColumn
cfprComputeMbPowerStatsHistInputCurrentAvg = _CfprComputeMbPowerStatsHistInputCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 10),
    _CfprComputeMbPowerStatsHistInputCurrentAvg_Type()
)
cfprComputeMbPowerStatsHistInputCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInputCurrentAvg.setStatus("current")
_CfprComputeMbPowerStatsHistInputCurrentMax_Type = Integer32
_CfprComputeMbPowerStatsHistInputCurrentMax_Object = MibTableColumn
cfprComputeMbPowerStatsHistInputCurrentMax = _CfprComputeMbPowerStatsHistInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 11),
    _CfprComputeMbPowerStatsHistInputCurrentMax_Type()
)
cfprComputeMbPowerStatsHistInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInputCurrentMax.setStatus("current")
_CfprComputeMbPowerStatsHistInputCurrentMin_Type = Integer32
_CfprComputeMbPowerStatsHistInputCurrentMin_Object = MibTableColumn
cfprComputeMbPowerStatsHistInputCurrentMin = _CfprComputeMbPowerStatsHistInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 12),
    _CfprComputeMbPowerStatsHistInputCurrentMin_Type()
)
cfprComputeMbPowerStatsHistInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInputCurrentMin.setStatus("current")
_CfprComputeMbPowerStatsHistInputVoltage_Type = Integer32
_CfprComputeMbPowerStatsHistInputVoltage_Object = MibTableColumn
cfprComputeMbPowerStatsHistInputVoltage = _CfprComputeMbPowerStatsHistInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 13),
    _CfprComputeMbPowerStatsHistInputVoltage_Type()
)
cfprComputeMbPowerStatsHistInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInputVoltage.setStatus("current")
_CfprComputeMbPowerStatsHistInputVoltageAvg_Type = Integer32
_CfprComputeMbPowerStatsHistInputVoltageAvg_Object = MibTableColumn
cfprComputeMbPowerStatsHistInputVoltageAvg = _CfprComputeMbPowerStatsHistInputVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 14),
    _CfprComputeMbPowerStatsHistInputVoltageAvg_Type()
)
cfprComputeMbPowerStatsHistInputVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInputVoltageAvg.setStatus("current")
_CfprComputeMbPowerStatsHistInputVoltageMax_Type = Integer32
_CfprComputeMbPowerStatsHistInputVoltageMax_Object = MibTableColumn
cfprComputeMbPowerStatsHistInputVoltageMax = _CfprComputeMbPowerStatsHistInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 15),
    _CfprComputeMbPowerStatsHistInputVoltageMax_Type()
)
cfprComputeMbPowerStatsHistInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInputVoltageMax.setStatus("current")
_CfprComputeMbPowerStatsHistInputVoltageMin_Type = Integer32
_CfprComputeMbPowerStatsHistInputVoltageMin_Object = MibTableColumn
cfprComputeMbPowerStatsHistInputVoltageMin = _CfprComputeMbPowerStatsHistInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 16),
    _CfprComputeMbPowerStatsHistInputVoltageMin_Type()
)
cfprComputeMbPowerStatsHistInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistInputVoltageMin.setStatus("current")
_CfprComputeMbPowerStatsHistMostRecent_Type = TruthValue
_CfprComputeMbPowerStatsHistMostRecent_Object = MibTableColumn
cfprComputeMbPowerStatsHistMostRecent = _CfprComputeMbPowerStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 17),
    _CfprComputeMbPowerStatsHistMostRecent_Type()
)
cfprComputeMbPowerStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistMostRecent.setStatus("current")
_CfprComputeMbPowerStatsHistSuspect_Type = TruthValue
_CfprComputeMbPowerStatsHistSuspect_Object = MibTableColumn
cfprComputeMbPowerStatsHistSuspect = _CfprComputeMbPowerStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 18),
    _CfprComputeMbPowerStatsHistSuspect_Type()
)
cfprComputeMbPowerStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistSuspect.setStatus("current")
_CfprComputeMbPowerStatsHistThresholded_Type = CfprComputeMbPowerStatsHistThresholded
_CfprComputeMbPowerStatsHistThresholded_Object = MibTableColumn
cfprComputeMbPowerStatsHistThresholded = _CfprComputeMbPowerStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 19),
    _CfprComputeMbPowerStatsHistThresholded_Type()
)
cfprComputeMbPowerStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistThresholded.setStatus("current")
_CfprComputeMbPowerStatsHistTimeCollected_Type = DateAndTime
_CfprComputeMbPowerStatsHistTimeCollected_Object = MibTableColumn
cfprComputeMbPowerStatsHistTimeCollected = _CfprComputeMbPowerStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 23, 1, 20),
    _CfprComputeMbPowerStatsHistTimeCollected_Type()
)
cfprComputeMbPowerStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbPowerStatsHistTimeCollected.setStatus("current")
_CfprComputeMbTempStatsTable_Object = MibTable
cfprComputeMbTempStatsTable = _CfprComputeMbTempStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24)
)
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsTable.setStatus("current")
_CfprComputeMbTempStatsEntry_Object = MibTableRow
cfprComputeMbTempStatsEntry = _CfprComputeMbTempStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1)
)
cfprComputeMbTempStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeMbTempStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsEntry.setStatus("current")
_CfprComputeMbTempStatsInstanceId_Type = CfprManagedObjectId
_CfprComputeMbTempStatsInstanceId_Object = MibTableColumn
cfprComputeMbTempStatsInstanceId = _CfprComputeMbTempStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 1),
    _CfprComputeMbTempStatsInstanceId_Type()
)
cfprComputeMbTempStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsInstanceId.setStatus("current")
_CfprComputeMbTempStatsDn_Type = CfprManagedObjectDn
_CfprComputeMbTempStatsDn_Object = MibTableColumn
cfprComputeMbTempStatsDn = _CfprComputeMbTempStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 2),
    _CfprComputeMbTempStatsDn_Type()
)
cfprComputeMbTempStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsDn.setStatus("current")
_CfprComputeMbTempStatsRn_Type = SnmpAdminString
_CfprComputeMbTempStatsRn_Object = MibTableColumn
cfprComputeMbTempStatsRn = _CfprComputeMbTempStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 3),
    _CfprComputeMbTempStatsRn_Type()
)
cfprComputeMbTempStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsRn.setStatus("current")
_CfprComputeMbTempStatsFmTempSenIo_Type = Integer32
_CfprComputeMbTempStatsFmTempSenIo_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenIo = _CfprComputeMbTempStatsFmTempSenIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 4),
    _CfprComputeMbTempStatsFmTempSenIo_Type()
)
cfprComputeMbTempStatsFmTempSenIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenIo.setStatus("current")
_CfprComputeMbTempStatsFmTempSenIoAvg_Type = Integer32
_CfprComputeMbTempStatsFmTempSenIoAvg_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenIoAvg = _CfprComputeMbTempStatsFmTempSenIoAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 5),
    _CfprComputeMbTempStatsFmTempSenIoAvg_Type()
)
cfprComputeMbTempStatsFmTempSenIoAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenIoAvg.setStatus("current")
_CfprComputeMbTempStatsFmTempSenIoMax_Type = Integer32
_CfprComputeMbTempStatsFmTempSenIoMax_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenIoMax = _CfprComputeMbTempStatsFmTempSenIoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 6),
    _CfprComputeMbTempStatsFmTempSenIoMax_Type()
)
cfprComputeMbTempStatsFmTempSenIoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenIoMax.setStatus("current")
_CfprComputeMbTempStatsFmTempSenIoMin_Type = Integer32
_CfprComputeMbTempStatsFmTempSenIoMin_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenIoMin = _CfprComputeMbTempStatsFmTempSenIoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 7),
    _CfprComputeMbTempStatsFmTempSenIoMin_Type()
)
cfprComputeMbTempStatsFmTempSenIoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenIoMin.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRear_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRear_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRear = _CfprComputeMbTempStatsFmTempSenRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 8),
    _CfprComputeMbTempStatsFmTempSenRear_Type()
)
cfprComputeMbTempStatsFmTempSenRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRear.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearAvg_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearAvg_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearAvg = _CfprComputeMbTempStatsFmTempSenRearAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 9),
    _CfprComputeMbTempStatsFmTempSenRearAvg_Type()
)
cfprComputeMbTempStatsFmTempSenRearAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearAvg.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearL_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearL_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearL = _CfprComputeMbTempStatsFmTempSenRearL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 10),
    _CfprComputeMbTempStatsFmTempSenRearL_Type()
)
cfprComputeMbTempStatsFmTempSenRearL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearL.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearLAvg_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearLAvg_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearLAvg = _CfprComputeMbTempStatsFmTempSenRearLAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 11),
    _CfprComputeMbTempStatsFmTempSenRearLAvg_Type()
)
cfprComputeMbTempStatsFmTempSenRearLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearLAvg.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearLMax_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearLMax_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearLMax = _CfprComputeMbTempStatsFmTempSenRearLMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 12),
    _CfprComputeMbTempStatsFmTempSenRearLMax_Type()
)
cfprComputeMbTempStatsFmTempSenRearLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearLMax.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearLMin_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearLMin_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearLMin = _CfprComputeMbTempStatsFmTempSenRearLMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 13),
    _CfprComputeMbTempStatsFmTempSenRearLMin_Type()
)
cfprComputeMbTempStatsFmTempSenRearLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearLMin.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearMax_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearMax_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearMax = _CfprComputeMbTempStatsFmTempSenRearMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 14),
    _CfprComputeMbTempStatsFmTempSenRearMax_Type()
)
cfprComputeMbTempStatsFmTempSenRearMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearMax.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearMin_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearMin_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearMin = _CfprComputeMbTempStatsFmTempSenRearMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 15),
    _CfprComputeMbTempStatsFmTempSenRearMin_Type()
)
cfprComputeMbTempStatsFmTempSenRearMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearMin.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearR_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearR_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearR = _CfprComputeMbTempStatsFmTempSenRearR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 16),
    _CfprComputeMbTempStatsFmTempSenRearR_Type()
)
cfprComputeMbTempStatsFmTempSenRearR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearR.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearRAvg_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearRAvg_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearRAvg = _CfprComputeMbTempStatsFmTempSenRearRAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 17),
    _CfprComputeMbTempStatsFmTempSenRearRAvg_Type()
)
cfprComputeMbTempStatsFmTempSenRearRAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearRAvg.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearRMax_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearRMax_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearRMax = _CfprComputeMbTempStatsFmTempSenRearRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 18),
    _CfprComputeMbTempStatsFmTempSenRearRMax_Type()
)
cfprComputeMbTempStatsFmTempSenRearRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearRMax.setStatus("current")
_CfprComputeMbTempStatsFmTempSenRearRMin_Type = Integer32
_CfprComputeMbTempStatsFmTempSenRearRMin_Object = MibTableColumn
cfprComputeMbTempStatsFmTempSenRearRMin = _CfprComputeMbTempStatsFmTempSenRearRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 19),
    _CfprComputeMbTempStatsFmTempSenRearRMin_Type()
)
cfprComputeMbTempStatsFmTempSenRearRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsFmTempSenRearRMin.setStatus("current")
_CfprComputeMbTempStatsIntervals_Type = Gauge32
_CfprComputeMbTempStatsIntervals_Object = MibTableColumn
cfprComputeMbTempStatsIntervals = _CfprComputeMbTempStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 20),
    _CfprComputeMbTempStatsIntervals_Type()
)
cfprComputeMbTempStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsIntervals.setStatus("current")
_CfprComputeMbTempStatsSuspect_Type = TruthValue
_CfprComputeMbTempStatsSuspect_Object = MibTableColumn
cfprComputeMbTempStatsSuspect = _CfprComputeMbTempStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 21),
    _CfprComputeMbTempStatsSuspect_Type()
)
cfprComputeMbTempStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsSuspect.setStatus("current")
_CfprComputeMbTempStatsThresholded_Type = CfprComputeMbTempStatsThresholded
_CfprComputeMbTempStatsThresholded_Object = MibTableColumn
cfprComputeMbTempStatsThresholded = _CfprComputeMbTempStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 22),
    _CfprComputeMbTempStatsThresholded_Type()
)
cfprComputeMbTempStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsThresholded.setStatus("current")
_CfprComputeMbTempStatsTimeCollected_Type = DateAndTime
_CfprComputeMbTempStatsTimeCollected_Object = MibTableColumn
cfprComputeMbTempStatsTimeCollected = _CfprComputeMbTempStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 23),
    _CfprComputeMbTempStatsTimeCollected_Type()
)
cfprComputeMbTempStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsTimeCollected.setStatus("current")
_CfprComputeMbTempStatsUpdate_Type = Gauge32
_CfprComputeMbTempStatsUpdate_Object = MibTableColumn
cfprComputeMbTempStatsUpdate = _CfprComputeMbTempStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 24, 1, 24),
    _CfprComputeMbTempStatsUpdate_Type()
)
cfprComputeMbTempStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsUpdate.setStatus("current")
_CfprComputeMbTempStatsHistTable_Object = MibTable
cfprComputeMbTempStatsHistTable = _CfprComputeMbTempStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25)
)
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistTable.setStatus("current")
_CfprComputeMbTempStatsHistEntry_Object = MibTableRow
cfprComputeMbTempStatsHistEntry = _CfprComputeMbTempStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1)
)
cfprComputeMbTempStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeMbTempStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistEntry.setStatus("current")
_CfprComputeMbTempStatsHistInstanceId_Type = CfprManagedObjectId
_CfprComputeMbTempStatsHistInstanceId_Object = MibTableColumn
cfprComputeMbTempStatsHistInstanceId = _CfprComputeMbTempStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 1),
    _CfprComputeMbTempStatsHistInstanceId_Type()
)
cfprComputeMbTempStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistInstanceId.setStatus("current")
_CfprComputeMbTempStatsHistDn_Type = CfprManagedObjectDn
_CfprComputeMbTempStatsHistDn_Object = MibTableColumn
cfprComputeMbTempStatsHistDn = _CfprComputeMbTempStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 2),
    _CfprComputeMbTempStatsHistDn_Type()
)
cfprComputeMbTempStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistDn.setStatus("current")
_CfprComputeMbTempStatsHistRn_Type = SnmpAdminString
_CfprComputeMbTempStatsHistRn_Object = MibTableColumn
cfprComputeMbTempStatsHistRn = _CfprComputeMbTempStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 3),
    _CfprComputeMbTempStatsHistRn_Type()
)
cfprComputeMbTempStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistRn.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenIo_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenIo_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenIo = _CfprComputeMbTempStatsHistFmTempSenIo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 4),
    _CfprComputeMbTempStatsHistFmTempSenIo_Type()
)
cfprComputeMbTempStatsHistFmTempSenIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenIo.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenIoAvg_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenIoAvg_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenIoAvg = _CfprComputeMbTempStatsHistFmTempSenIoAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 5),
    _CfprComputeMbTempStatsHistFmTempSenIoAvg_Type()
)
cfprComputeMbTempStatsHistFmTempSenIoAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenIoAvg.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenIoMax_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenIoMax_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenIoMax = _CfprComputeMbTempStatsHistFmTempSenIoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 6),
    _CfprComputeMbTempStatsHistFmTempSenIoMax_Type()
)
cfprComputeMbTempStatsHistFmTempSenIoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenIoMax.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenIoMin_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenIoMin_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenIoMin = _CfprComputeMbTempStatsHistFmTempSenIoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 7),
    _CfprComputeMbTempStatsHistFmTempSenIoMin_Type()
)
cfprComputeMbTempStatsHistFmTempSenIoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenIoMin.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRear_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRear_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRear = _CfprComputeMbTempStatsHistFmTempSenRear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 8),
    _CfprComputeMbTempStatsHistFmTempSenRear_Type()
)
cfprComputeMbTempStatsHistFmTempSenRear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRear.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearAvg_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearAvg_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearAvg = _CfprComputeMbTempStatsHistFmTempSenRearAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 9),
    _CfprComputeMbTempStatsHistFmTempSenRearAvg_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearAvg.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearL_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearL_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearL = _CfprComputeMbTempStatsHistFmTempSenRearL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 10),
    _CfprComputeMbTempStatsHistFmTempSenRearL_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearL.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearLAvg_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearLAvg_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearLAvg = _CfprComputeMbTempStatsHistFmTempSenRearLAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 11),
    _CfprComputeMbTempStatsHistFmTempSenRearLAvg_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearLAvg.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearLMax_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearLMax_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearLMax = _CfprComputeMbTempStatsHistFmTempSenRearLMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 12),
    _CfprComputeMbTempStatsHistFmTempSenRearLMax_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearLMax.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearLMin_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearLMin_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearLMin = _CfprComputeMbTempStatsHistFmTempSenRearLMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 13),
    _CfprComputeMbTempStatsHistFmTempSenRearLMin_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearLMin.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearMax_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearMax_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearMax = _CfprComputeMbTempStatsHistFmTempSenRearMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 14),
    _CfprComputeMbTempStatsHistFmTempSenRearMax_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearMax.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearMin_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearMin_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearMin = _CfprComputeMbTempStatsHistFmTempSenRearMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 15),
    _CfprComputeMbTempStatsHistFmTempSenRearMin_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearMin.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearR_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearR_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearR = _CfprComputeMbTempStatsHistFmTempSenRearR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 16),
    _CfprComputeMbTempStatsHistFmTempSenRearR_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearR.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearRAvg_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearRAvg_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearRAvg = _CfprComputeMbTempStatsHistFmTempSenRearRAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 17),
    _CfprComputeMbTempStatsHistFmTempSenRearRAvg_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearRAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearRAvg.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearRMax_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearRMax_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearRMax = _CfprComputeMbTempStatsHistFmTempSenRearRMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 18),
    _CfprComputeMbTempStatsHistFmTempSenRearRMax_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearRMax.setStatus("current")
_CfprComputeMbTempStatsHistFmTempSenRearRMin_Type = Integer32
_CfprComputeMbTempStatsHistFmTempSenRearRMin_Object = MibTableColumn
cfprComputeMbTempStatsHistFmTempSenRearRMin = _CfprComputeMbTempStatsHistFmTempSenRearRMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 19),
    _CfprComputeMbTempStatsHistFmTempSenRearRMin_Type()
)
cfprComputeMbTempStatsHistFmTempSenRearRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistFmTempSenRearRMin.setStatus("current")
_CfprComputeMbTempStatsHistId_Type = Unsigned64
_CfprComputeMbTempStatsHistId_Object = MibTableColumn
cfprComputeMbTempStatsHistId = _CfprComputeMbTempStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 20),
    _CfprComputeMbTempStatsHistId_Type()
)
cfprComputeMbTempStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistId.setStatus("current")
_CfprComputeMbTempStatsHistMostRecent_Type = TruthValue
_CfprComputeMbTempStatsHistMostRecent_Object = MibTableColumn
cfprComputeMbTempStatsHistMostRecent = _CfprComputeMbTempStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 21),
    _CfprComputeMbTempStatsHistMostRecent_Type()
)
cfprComputeMbTempStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistMostRecent.setStatus("current")
_CfprComputeMbTempStatsHistSuspect_Type = TruthValue
_CfprComputeMbTempStatsHistSuspect_Object = MibTableColumn
cfprComputeMbTempStatsHistSuspect = _CfprComputeMbTempStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 22),
    _CfprComputeMbTempStatsHistSuspect_Type()
)
cfprComputeMbTempStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistSuspect.setStatus("current")
_CfprComputeMbTempStatsHistThresholded_Type = CfprComputeMbTempStatsHistThresholded
_CfprComputeMbTempStatsHistThresholded_Object = MibTableColumn
cfprComputeMbTempStatsHistThresholded = _CfprComputeMbTempStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 23),
    _CfprComputeMbTempStatsHistThresholded_Type()
)
cfprComputeMbTempStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistThresholded.setStatus("current")
_CfprComputeMbTempStatsHistTimeCollected_Type = DateAndTime
_CfprComputeMbTempStatsHistTimeCollected_Object = MibTableColumn
cfprComputeMbTempStatsHistTimeCollected = _CfprComputeMbTempStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 25, 1, 24),
    _CfprComputeMbTempStatsHistTimeCollected_Type()
)
cfprComputeMbTempStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMbTempStatsHistTimeCollected.setStatus("current")
_CfprComputeMemoryConfigPolicyTable_Object = MibTable
cfprComputeMemoryConfigPolicyTable = _CfprComputeMemoryConfigPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26)
)
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyTable.setStatus("current")
_CfprComputeMemoryConfigPolicyEntry_Object = MibTableRow
cfprComputeMemoryConfigPolicyEntry = _CfprComputeMemoryConfigPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1)
)
cfprComputeMemoryConfigPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeMemoryConfigPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyEntry.setStatus("current")
_CfprComputeMemoryConfigPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeMemoryConfigPolicyInstanceId_Object = MibTableColumn
cfprComputeMemoryConfigPolicyInstanceId = _CfprComputeMemoryConfigPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 1),
    _CfprComputeMemoryConfigPolicyInstanceId_Type()
)
cfprComputeMemoryConfigPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyInstanceId.setStatus("current")
_CfprComputeMemoryConfigPolicyDn_Type = CfprManagedObjectDn
_CfprComputeMemoryConfigPolicyDn_Object = MibTableColumn
cfprComputeMemoryConfigPolicyDn = _CfprComputeMemoryConfigPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 2),
    _CfprComputeMemoryConfigPolicyDn_Type()
)
cfprComputeMemoryConfigPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyDn.setStatus("current")
_CfprComputeMemoryConfigPolicyRn_Type = SnmpAdminString
_CfprComputeMemoryConfigPolicyRn_Object = MibTableColumn
cfprComputeMemoryConfigPolicyRn = _CfprComputeMemoryConfigPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 3),
    _CfprComputeMemoryConfigPolicyRn_Type()
)
cfprComputeMemoryConfigPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyRn.setStatus("current")
_CfprComputeMemoryConfigPolicyBlackListing_Type = CfprComputeBlackListing
_CfprComputeMemoryConfigPolicyBlackListing_Object = MibTableColumn
cfprComputeMemoryConfigPolicyBlackListing = _CfprComputeMemoryConfigPolicyBlackListing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 4),
    _CfprComputeMemoryConfigPolicyBlackListing_Type()
)
cfprComputeMemoryConfigPolicyBlackListing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyBlackListing.setStatus("current")
_CfprComputeMemoryConfigPolicyDescr_Type = SnmpAdminString
_CfprComputeMemoryConfigPolicyDescr_Object = MibTableColumn
cfprComputeMemoryConfigPolicyDescr = _CfprComputeMemoryConfigPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 5),
    _CfprComputeMemoryConfigPolicyDescr_Type()
)
cfprComputeMemoryConfigPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyDescr.setStatus("current")
_CfprComputeMemoryConfigPolicyIntId_Type = SnmpAdminString
_CfprComputeMemoryConfigPolicyIntId_Object = MibTableColumn
cfprComputeMemoryConfigPolicyIntId = _CfprComputeMemoryConfigPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 6),
    _CfprComputeMemoryConfigPolicyIntId_Type()
)
cfprComputeMemoryConfigPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyIntId.setStatus("current")
_CfprComputeMemoryConfigPolicyName_Type = SnmpAdminString
_CfprComputeMemoryConfigPolicyName_Object = MibTableColumn
cfprComputeMemoryConfigPolicyName = _CfprComputeMemoryConfigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 7),
    _CfprComputeMemoryConfigPolicyName_Type()
)
cfprComputeMemoryConfigPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyName.setStatus("current")
_CfprComputeMemoryConfigPolicyPolicyLevel_Type = Gauge32
_CfprComputeMemoryConfigPolicyPolicyLevel_Object = MibTableColumn
cfprComputeMemoryConfigPolicyPolicyLevel = _CfprComputeMemoryConfigPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 8),
    _CfprComputeMemoryConfigPolicyPolicyLevel_Type()
)
cfprComputeMemoryConfigPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyPolicyLevel.setStatus("current")
_CfprComputeMemoryConfigPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeMemoryConfigPolicyPolicyOwner_Object = MibTableColumn
cfprComputeMemoryConfigPolicyPolicyOwner = _CfprComputeMemoryConfigPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 26, 1, 9),
    _CfprComputeMemoryConfigPolicyPolicyOwner_Type()
)
cfprComputeMemoryConfigPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigPolicyPolicyOwner.setStatus("current")
_CfprComputeMemoryConfigurationTable_Object = MibTable
cfprComputeMemoryConfigurationTable = _CfprComputeMemoryConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 27)
)
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigurationTable.setStatus("current")
_CfprComputeMemoryConfigurationEntry_Object = MibTableRow
cfprComputeMemoryConfigurationEntry = _CfprComputeMemoryConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 27, 1)
)
cfprComputeMemoryConfigurationEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeMemoryConfigurationInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigurationEntry.setStatus("current")
_CfprComputeMemoryConfigurationInstanceId_Type = CfprManagedObjectId
_CfprComputeMemoryConfigurationInstanceId_Object = MibTableColumn
cfprComputeMemoryConfigurationInstanceId = _CfprComputeMemoryConfigurationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 27, 1, 1),
    _CfprComputeMemoryConfigurationInstanceId_Type()
)
cfprComputeMemoryConfigurationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigurationInstanceId.setStatus("current")
_CfprComputeMemoryConfigurationDn_Type = CfprManagedObjectDn
_CfprComputeMemoryConfigurationDn_Object = MibTableColumn
cfprComputeMemoryConfigurationDn = _CfprComputeMemoryConfigurationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 27, 1, 2),
    _CfprComputeMemoryConfigurationDn_Type()
)
cfprComputeMemoryConfigurationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigurationDn.setStatus("current")
_CfprComputeMemoryConfigurationRn_Type = SnmpAdminString
_CfprComputeMemoryConfigurationRn_Object = MibTableColumn
cfprComputeMemoryConfigurationRn = _CfprComputeMemoryConfigurationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 27, 1, 3),
    _CfprComputeMemoryConfigurationRn_Type()
)
cfprComputeMemoryConfigurationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigurationRn.setStatus("current")
_CfprComputeMemoryConfigurationAdminMemoryState_Type = CfprComputeAdminMemoryState
_CfprComputeMemoryConfigurationAdminMemoryState_Object = MibTableColumn
cfprComputeMemoryConfigurationAdminMemoryState = _CfprComputeMemoryConfigurationAdminMemoryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 27, 1, 4),
    _CfprComputeMemoryConfigurationAdminMemoryState_Type()
)
cfprComputeMemoryConfigurationAdminMemoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigurationAdminMemoryState.setStatus("current")
_CfprComputeMemoryConfigurationBlackListing_Type = CfprComputeBlackListing
_CfprComputeMemoryConfigurationBlackListing_Object = MibTableColumn
cfprComputeMemoryConfigurationBlackListing = _CfprComputeMemoryConfigurationBlackListing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 27, 1, 5),
    _CfprComputeMemoryConfigurationBlackListing_Type()
)
cfprComputeMemoryConfigurationBlackListing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryConfigurationBlackListing.setStatus("current")
_CfprComputeMemoryUnitConstraintDefTable_Object = MibTable
cfprComputeMemoryUnitConstraintDefTable = _CfprComputeMemoryUnitConstraintDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28)
)
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefTable.setStatus("current")
_CfprComputeMemoryUnitConstraintDefEntry_Object = MibTableRow
cfprComputeMemoryUnitConstraintDefEntry = _CfprComputeMemoryUnitConstraintDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1)
)
cfprComputeMemoryUnitConstraintDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeMemoryUnitConstraintDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefEntry.setStatus("current")
_CfprComputeMemoryUnitConstraintDefInstanceId_Type = CfprManagedObjectId
_CfprComputeMemoryUnitConstraintDefInstanceId_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefInstanceId = _CfprComputeMemoryUnitConstraintDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 1),
    _CfprComputeMemoryUnitConstraintDefInstanceId_Type()
)
cfprComputeMemoryUnitConstraintDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefInstanceId.setStatus("current")
_CfprComputeMemoryUnitConstraintDefDn_Type = CfprManagedObjectDn
_CfprComputeMemoryUnitConstraintDefDn_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefDn = _CfprComputeMemoryUnitConstraintDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 2),
    _CfprComputeMemoryUnitConstraintDefDn_Type()
)
cfprComputeMemoryUnitConstraintDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefDn.setStatus("current")
_CfprComputeMemoryUnitConstraintDefRn_Type = SnmpAdminString
_CfprComputeMemoryUnitConstraintDefRn_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefRn = _CfprComputeMemoryUnitConstraintDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 3),
    _CfprComputeMemoryUnitConstraintDefRn_Type()
)
cfprComputeMemoryUnitConstraintDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefRn.setStatus("current")
_CfprComputeMemoryUnitConstraintDefDescr_Type = SnmpAdminString
_CfprComputeMemoryUnitConstraintDefDescr_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefDescr = _CfprComputeMemoryUnitConstraintDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 4),
    _CfprComputeMemoryUnitConstraintDefDescr_Type()
)
cfprComputeMemoryUnitConstraintDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefDescr.setStatus("current")
_CfprComputeMemoryUnitConstraintDefIntId_Type = SnmpAdminString
_CfprComputeMemoryUnitConstraintDefIntId_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefIntId = _CfprComputeMemoryUnitConstraintDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 5),
    _CfprComputeMemoryUnitConstraintDefIntId_Type()
)
cfprComputeMemoryUnitConstraintDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefIntId.setStatus("current")
_CfprComputeMemoryUnitConstraintDefName_Type = SnmpAdminString
_CfprComputeMemoryUnitConstraintDefName_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefName = _CfprComputeMemoryUnitConstraintDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 6),
    _CfprComputeMemoryUnitConstraintDefName_Type()
)
cfprComputeMemoryUnitConstraintDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefName.setStatus("current")
_CfprComputeMemoryUnitConstraintDefPolicyLevel_Type = Gauge32
_CfprComputeMemoryUnitConstraintDefPolicyLevel_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefPolicyLevel = _CfprComputeMemoryUnitConstraintDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 7),
    _CfprComputeMemoryUnitConstraintDefPolicyLevel_Type()
)
cfprComputeMemoryUnitConstraintDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefPolicyLevel.setStatus("current")
_CfprComputeMemoryUnitConstraintDefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeMemoryUnitConstraintDefPolicyOwner_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefPolicyOwner = _CfprComputeMemoryUnitConstraintDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 8),
    _CfprComputeMemoryUnitConstraintDefPolicyOwner_Type()
)
cfprComputeMemoryUnitConstraintDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefPolicyOwner.setStatus("current")
_CfprComputeMemoryUnitConstraintDefRevisionModifier_Type = SnmpAdminString
_CfprComputeMemoryUnitConstraintDefRevisionModifier_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefRevisionModifier = _CfprComputeMemoryUnitConstraintDefRevisionModifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 9),
    _CfprComputeMemoryUnitConstraintDefRevisionModifier_Type()
)
cfprComputeMemoryUnitConstraintDefRevisionModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefRevisionModifier.setStatus("current")
_CfprComputeMemoryUnitConstraintDefType_Type = CfprComputeMemoryUnitConstraintType
_CfprComputeMemoryUnitConstraintDefType_Object = MibTableColumn
cfprComputeMemoryUnitConstraintDefType = _CfprComputeMemoryUnitConstraintDefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 28, 1, 10),
    _CfprComputeMemoryUnitConstraintDefType_Type()
)
cfprComputeMemoryUnitConstraintDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeMemoryUnitConstraintDefType.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTable_Object = MibTable
cfprComputePCIeFatalCompletionStatsTable = _CfprComputePCIeFatalCompletionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29)
)
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTable.setStatus("current")
_CfprComputePCIeFatalCompletionStatsEntry_Object = MibTableRow
cfprComputePCIeFatalCompletionStatsEntry = _CfprComputePCIeFatalCompletionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1)
)
cfprComputePCIeFatalCompletionStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePCIeFatalCompletionStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsEntry.setStatus("current")
_CfprComputePCIeFatalCompletionStatsInstanceId_Type = CfprManagedObjectId
_CfprComputePCIeFatalCompletionStatsInstanceId_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsInstanceId = _CfprComputePCIeFatalCompletionStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 1),
    _CfprComputePCIeFatalCompletionStatsInstanceId_Type()
)
cfprComputePCIeFatalCompletionStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsInstanceId.setStatus("current")
_CfprComputePCIeFatalCompletionStatsDn_Type = CfprManagedObjectDn
_CfprComputePCIeFatalCompletionStatsDn_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsDn = _CfprComputePCIeFatalCompletionStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 2),
    _CfprComputePCIeFatalCompletionStatsDn_Type()
)
cfprComputePCIeFatalCompletionStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsDn.setStatus("current")
_CfprComputePCIeFatalCompletionStatsRn_Type = SnmpAdminString
_CfprComputePCIeFatalCompletionStatsRn_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsRn = _CfprComputePCIeFatalCompletionStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 3),
    _CfprComputePCIeFatalCompletionStatsRn_Type()
)
cfprComputePCIeFatalCompletionStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsRn.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors_Type = Counter32
_CfprComputePCIeFatalCompletionStatsAbortErrors_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors = _CfprComputePCIeFatalCompletionStatsAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 4),
    _CfprComputePCIeFatalCompletionStatsAbortErrors_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors15Min_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors15Min = _CfprComputePCIeFatalCompletionStatsAbortErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 5),
    _CfprComputePCIeFatalCompletionStatsAbortErrors15Min_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors15Min.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors15MinH = _CfprComputePCIeFatalCompletionStatsAbortErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 6),
    _CfprComputePCIeFatalCompletionStatsAbortErrors15MinH_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors15MinH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors1Day_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors1Day = _CfprComputePCIeFatalCompletionStatsAbortErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 7),
    _CfprComputePCIeFatalCompletionStatsAbortErrors1Day_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors1Day.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors1DayH = _CfprComputePCIeFatalCompletionStatsAbortErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 8),
    _CfprComputePCIeFatalCompletionStatsAbortErrors1DayH_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors1DayH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors1Hour = _CfprComputePCIeFatalCompletionStatsAbortErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 9),
    _CfprComputePCIeFatalCompletionStatsAbortErrors1Hour_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors1Hour.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors1HourH = _CfprComputePCIeFatalCompletionStatsAbortErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 10),
    _CfprComputePCIeFatalCompletionStatsAbortErrors1HourH_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors1HourH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors1Week_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors1Week = _CfprComputePCIeFatalCompletionStatsAbortErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 11),
    _CfprComputePCIeFatalCompletionStatsAbortErrors1Week_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors1Week.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors1WeekH = _CfprComputePCIeFatalCompletionStatsAbortErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 12),
    _CfprComputePCIeFatalCompletionStatsAbortErrors1WeekH_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors2Weeks = _CfprComputePCIeFatalCompletionStatsAbortErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 13),
    _CfprComputePCIeFatalCompletionStatsAbortErrors2Weeks_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH = _CfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 14),
    _CfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH_Type()
)
cfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors_Type = Counter32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors = _CfprComputePCIeFatalCompletionStatsTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 15),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors15Min_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors15Min = _CfprComputePCIeFatalCompletionStatsTimeoutErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 16),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors15Min_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors15Min.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH = _CfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 17),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1Day_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors1Day = _CfprComputePCIeFatalCompletionStatsTimeoutErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 18),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors1Day_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors1Day.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH = _CfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 19),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour = _CfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 20),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH = _CfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 21),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1Week_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors1Week = _CfprComputePCIeFatalCompletionStatsTimeoutErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 22),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors1Week_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors1Week.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH = _CfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 23),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks = _CfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 24),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH = _CfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 25),
    _CfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH_Type()
)
cfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsIntervals_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsIntervals_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsIntervals = _CfprComputePCIeFatalCompletionStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 26),
    _CfprComputePCIeFatalCompletionStatsIntervals_Type()
)
cfprComputePCIeFatalCompletionStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsIntervals.setStatus("current")
_CfprComputePCIeFatalCompletionStatsSuspect_Type = TruthValue
_CfprComputePCIeFatalCompletionStatsSuspect_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsSuspect = _CfprComputePCIeFatalCompletionStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 27),
    _CfprComputePCIeFatalCompletionStatsSuspect_Type()
)
cfprComputePCIeFatalCompletionStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsSuspect.setStatus("current")
_CfprComputePCIeFatalCompletionStatsThresholded_Type = CfprComputePCIeFatalCompletionStatsThresholded
_CfprComputePCIeFatalCompletionStatsThresholded_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsThresholded = _CfprComputePCIeFatalCompletionStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 28),
    _CfprComputePCIeFatalCompletionStatsThresholded_Type()
)
cfprComputePCIeFatalCompletionStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsThresholded.setStatus("current")
_CfprComputePCIeFatalCompletionStatsTimeCollected_Type = DateAndTime
_CfprComputePCIeFatalCompletionStatsTimeCollected_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsTimeCollected = _CfprComputePCIeFatalCompletionStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 29),
    _CfprComputePCIeFatalCompletionStatsTimeCollected_Type()
)
cfprComputePCIeFatalCompletionStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsTimeCollected.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors_Type = Counter32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 30),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 31),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 32),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 33),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 34),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 35),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 36),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 37),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 38),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 39),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH = _CfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 40),
    _CfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH_Type()
)
cfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalCompletionStatsUpdate_Type = Gauge32
_CfprComputePCIeFatalCompletionStatsUpdate_Object = MibTableColumn
cfprComputePCIeFatalCompletionStatsUpdate = _CfprComputePCIeFatalCompletionStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 29, 1, 41),
    _CfprComputePCIeFatalCompletionStatsUpdate_Type()
)
cfprComputePCIeFatalCompletionStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalCompletionStatsUpdate.setStatus("current")
_CfprComputePCIeFatalProtocolStatsTable_Object = MibTable
cfprComputePCIeFatalProtocolStatsTable = _CfprComputePCIeFatalProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30)
)
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsTable.setStatus("current")
_CfprComputePCIeFatalProtocolStatsEntry_Object = MibTableRow
cfprComputePCIeFatalProtocolStatsEntry = _CfprComputePCIeFatalProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1)
)
cfprComputePCIeFatalProtocolStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePCIeFatalProtocolStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsEntry.setStatus("current")
_CfprComputePCIeFatalProtocolStatsInstanceId_Type = CfprManagedObjectId
_CfprComputePCIeFatalProtocolStatsInstanceId_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsInstanceId = _CfprComputePCIeFatalProtocolStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 1),
    _CfprComputePCIeFatalProtocolStatsInstanceId_Type()
)
cfprComputePCIeFatalProtocolStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsInstanceId.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDn_Type = CfprManagedObjectDn
_CfprComputePCIeFatalProtocolStatsDn_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDn = _CfprComputePCIeFatalProtocolStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 2),
    _CfprComputePCIeFatalProtocolStatsDn_Type()
)
cfprComputePCIeFatalProtocolStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDn.setStatus("current")
_CfprComputePCIeFatalProtocolStatsRn_Type = SnmpAdminString
_CfprComputePCIeFatalProtocolStatsRn_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsRn = _CfprComputePCIeFatalProtocolStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 3),
    _CfprComputePCIeFatalProtocolStatsRn_Type()
)
cfprComputePCIeFatalProtocolStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsRn.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors_Type = Counter32
_CfprComputePCIeFatalProtocolStatsDllpErrors_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors = _CfprComputePCIeFatalProtocolStatsDllpErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 4),
    _CfprComputePCIeFatalProtocolStatsDllpErrors_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors15Min_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors15Min = _CfprComputePCIeFatalProtocolStatsDllpErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 5),
    _CfprComputePCIeFatalProtocolStatsDllpErrors15Min_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors15Min.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors15MinH = _CfprComputePCIeFatalProtocolStatsDllpErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 6),
    _CfprComputePCIeFatalProtocolStatsDllpErrors15MinH_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors15MinH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors1Day_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors1Day = _CfprComputePCIeFatalProtocolStatsDllpErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 7),
    _CfprComputePCIeFatalProtocolStatsDllpErrors1Day_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors1Day.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors1DayH = _CfprComputePCIeFatalProtocolStatsDllpErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 8),
    _CfprComputePCIeFatalProtocolStatsDllpErrors1DayH_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors1DayH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors1Hour = _CfprComputePCIeFatalProtocolStatsDllpErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 9),
    _CfprComputePCIeFatalProtocolStatsDllpErrors1Hour_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors1Hour.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors1HourH = _CfprComputePCIeFatalProtocolStatsDllpErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 10),
    _CfprComputePCIeFatalProtocolStatsDllpErrors1HourH_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors1HourH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors1Week_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors1Week = _CfprComputePCIeFatalProtocolStatsDllpErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 11),
    _CfprComputePCIeFatalProtocolStatsDllpErrors1Week_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors1Week.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors1WeekH = _CfprComputePCIeFatalProtocolStatsDllpErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 12),
    _CfprComputePCIeFatalProtocolStatsDllpErrors1WeekH_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors2Weeks = _CfprComputePCIeFatalProtocolStatsDllpErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 13),
    _CfprComputePCIeFatalProtocolStatsDllpErrors2Weeks_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH = _CfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 14),
    _CfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH_Type()
)
cfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors_Type = Counter32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors = _CfprComputePCIeFatalProtocolStatsFlowControlErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 15),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors15Min_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors15Min = _CfprComputePCIeFatalProtocolStatsFlowControlErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 16),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors15Min_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors15Min.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH = _CfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 17),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1Day_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors1Day = _CfprComputePCIeFatalProtocolStatsFlowControlErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 18),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors1Day_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors1Day.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH = _CfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 19),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour = _CfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 20),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH = _CfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 21),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1Week_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors1Week = _CfprComputePCIeFatalProtocolStatsFlowControlErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 22),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors1Week_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors1Week.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH = _CfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 23),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks = _CfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 24),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH = _CfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 25),
    _CfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH_Type()
)
cfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalProtocolStatsIntervals_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsIntervals_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsIntervals = _CfprComputePCIeFatalProtocolStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 26),
    _CfprComputePCIeFatalProtocolStatsIntervals_Type()
)
cfprComputePCIeFatalProtocolStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsIntervals.setStatus("current")
_CfprComputePCIeFatalProtocolStatsSuspect_Type = TruthValue
_CfprComputePCIeFatalProtocolStatsSuspect_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsSuspect = _CfprComputePCIeFatalProtocolStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 27),
    _CfprComputePCIeFatalProtocolStatsSuspect_Type()
)
cfprComputePCIeFatalProtocolStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsSuspect.setStatus("current")
_CfprComputePCIeFatalProtocolStatsThresholded_Type = CfprComputePCIeFatalProtocolStatsThresholded
_CfprComputePCIeFatalProtocolStatsThresholded_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsThresholded = _CfprComputePCIeFatalProtocolStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 28),
    _CfprComputePCIeFatalProtocolStatsThresholded_Type()
)
cfprComputePCIeFatalProtocolStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsThresholded.setStatus("current")
_CfprComputePCIeFatalProtocolStatsTimeCollected_Type = DateAndTime
_CfprComputePCIeFatalProtocolStatsTimeCollected_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsTimeCollected = _CfprComputePCIeFatalProtocolStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 29),
    _CfprComputePCIeFatalProtocolStatsTimeCollected_Type()
)
cfprComputePCIeFatalProtocolStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsTimeCollected.setStatus("current")
_CfprComputePCIeFatalProtocolStatsUpdate_Type = Gauge32
_CfprComputePCIeFatalProtocolStatsUpdate_Object = MibTableColumn
cfprComputePCIeFatalProtocolStatsUpdate = _CfprComputePCIeFatalProtocolStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 30, 1, 30),
    _CfprComputePCIeFatalProtocolStatsUpdate_Type()
)
cfprComputePCIeFatalProtocolStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalProtocolStatsUpdate.setStatus("current")
_CfprComputePCIeFatalReceiveStatsTable_Object = MibTable
cfprComputePCIeFatalReceiveStatsTable = _CfprComputePCIeFatalReceiveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31)
)
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsTable.setStatus("current")
_CfprComputePCIeFatalReceiveStatsEntry_Object = MibTableRow
cfprComputePCIeFatalReceiveStatsEntry = _CfprComputePCIeFatalReceiveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1)
)
cfprComputePCIeFatalReceiveStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePCIeFatalReceiveStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsEntry.setStatus("current")
_CfprComputePCIeFatalReceiveStatsInstanceId_Type = CfprManagedObjectId
_CfprComputePCIeFatalReceiveStatsInstanceId_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsInstanceId = _CfprComputePCIeFatalReceiveStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 1),
    _CfprComputePCIeFatalReceiveStatsInstanceId_Type()
)
cfprComputePCIeFatalReceiveStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsInstanceId.setStatus("current")
_CfprComputePCIeFatalReceiveStatsDn_Type = CfprManagedObjectDn
_CfprComputePCIeFatalReceiveStatsDn_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsDn = _CfprComputePCIeFatalReceiveStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 2),
    _CfprComputePCIeFatalReceiveStatsDn_Type()
)
cfprComputePCIeFatalReceiveStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsDn.setStatus("current")
_CfprComputePCIeFatalReceiveStatsRn_Type = SnmpAdminString
_CfprComputePCIeFatalReceiveStatsRn_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsRn = _CfprComputePCIeFatalReceiveStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 3),
    _CfprComputePCIeFatalReceiveStatsRn_Type()
)
cfprComputePCIeFatalReceiveStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsRn.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors_Type = Counter32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 4),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 5),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 6),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 7),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 8),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 9),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 10),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 11),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 12),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 13),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH = _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 14),
    _CfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH_Type()
)
cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors_Type = Counter32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors = _CfprComputePCIeFatalReceiveStatsErrFatalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 15),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors15Min_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors15Min = _CfprComputePCIeFatalReceiveStatsErrFatalErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 16),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors15Min_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors15Min.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH = _CfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 17),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1Day_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors1Day = _CfprComputePCIeFatalReceiveStatsErrFatalErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 18),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors1Day_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors1Day.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH = _CfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 19),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour = _CfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 20),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH = _CfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 21),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1Week_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors1Week = _CfprComputePCIeFatalReceiveStatsErrFatalErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 22),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors1Week_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors1Week.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH = _CfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 23),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks = _CfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 24),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH = _CfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 25),
    _CfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH_Type()
)
cfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors_Type = Counter32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 26),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 27),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 28),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 29),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 30),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 31),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 32),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 33),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 34),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 35),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH = _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 36),
    _CfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH_Type()
)
cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsIntervals_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsIntervals_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsIntervals = _CfprComputePCIeFatalReceiveStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 37),
    _CfprComputePCIeFatalReceiveStatsIntervals_Type()
)
cfprComputePCIeFatalReceiveStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsIntervals.setStatus("current")
_CfprComputePCIeFatalReceiveStatsSuspect_Type = TruthValue
_CfprComputePCIeFatalReceiveStatsSuspect_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsSuspect = _CfprComputePCIeFatalReceiveStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 38),
    _CfprComputePCIeFatalReceiveStatsSuspect_Type()
)
cfprComputePCIeFatalReceiveStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsSuspect.setStatus("current")
_CfprComputePCIeFatalReceiveStatsThresholded_Type = CfprComputePCIeFatalReceiveStatsThresholded
_CfprComputePCIeFatalReceiveStatsThresholded_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsThresholded = _CfprComputePCIeFatalReceiveStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 39),
    _CfprComputePCIeFatalReceiveStatsThresholded_Type()
)
cfprComputePCIeFatalReceiveStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsThresholded.setStatus("current")
_CfprComputePCIeFatalReceiveStatsTimeCollected_Type = DateAndTime
_CfprComputePCIeFatalReceiveStatsTimeCollected_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsTimeCollected = _CfprComputePCIeFatalReceiveStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 40),
    _CfprComputePCIeFatalReceiveStatsTimeCollected_Type()
)
cfprComputePCIeFatalReceiveStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsTimeCollected.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Type = Counter32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 41),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 42),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 43),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 44),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 45),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 46),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 47),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 48),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 49),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 50),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH = _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 51),
    _CfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH_Type()
)
cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalReceiveStatsUpdate_Type = Gauge32
_CfprComputePCIeFatalReceiveStatsUpdate_Object = MibTableColumn
cfprComputePCIeFatalReceiveStatsUpdate = _CfprComputePCIeFatalReceiveStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 31, 1, 52),
    _CfprComputePCIeFatalReceiveStatsUpdate_Type()
)
cfprComputePCIeFatalReceiveStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalReceiveStatsUpdate.setStatus("current")
_CfprComputePCIeFatalStatsTable_Object = MibTable
cfprComputePCIeFatalStatsTable = _CfprComputePCIeFatalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32)
)
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsTable.setStatus("current")
_CfprComputePCIeFatalStatsEntry_Object = MibTableRow
cfprComputePCIeFatalStatsEntry = _CfprComputePCIeFatalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1)
)
cfprComputePCIeFatalStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePCIeFatalStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsEntry.setStatus("current")
_CfprComputePCIeFatalStatsInstanceId_Type = CfprManagedObjectId
_CfprComputePCIeFatalStatsInstanceId_Object = MibTableColumn
cfprComputePCIeFatalStatsInstanceId = _CfprComputePCIeFatalStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 1),
    _CfprComputePCIeFatalStatsInstanceId_Type()
)
cfprComputePCIeFatalStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsInstanceId.setStatus("current")
_CfprComputePCIeFatalStatsDn_Type = CfprManagedObjectDn
_CfprComputePCIeFatalStatsDn_Object = MibTableColumn
cfprComputePCIeFatalStatsDn = _CfprComputePCIeFatalStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 2),
    _CfprComputePCIeFatalStatsDn_Type()
)
cfprComputePCIeFatalStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsDn.setStatus("current")
_CfprComputePCIeFatalStatsRn_Type = SnmpAdminString
_CfprComputePCIeFatalStatsRn_Object = MibTableColumn
cfprComputePCIeFatalStatsRn = _CfprComputePCIeFatalStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 3),
    _CfprComputePCIeFatalStatsRn_Type()
)
cfprComputePCIeFatalStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsRn.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors_Type = Counter32
_CfprComputePCIeFatalStatsAcsViolationErrors_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors = _CfprComputePCIeFatalStatsAcsViolationErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 4),
    _CfprComputePCIeFatalStatsAcsViolationErrors_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors15Min_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors15Min = _CfprComputePCIeFatalStatsAcsViolationErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 5),
    _CfprComputePCIeFatalStatsAcsViolationErrors15Min_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors15Min.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors15MinH = _CfprComputePCIeFatalStatsAcsViolationErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 6),
    _CfprComputePCIeFatalStatsAcsViolationErrors15MinH_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors15MinH.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors1Day_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors1Day = _CfprComputePCIeFatalStatsAcsViolationErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 7),
    _CfprComputePCIeFatalStatsAcsViolationErrors1Day_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors1Day.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors1DayH = _CfprComputePCIeFatalStatsAcsViolationErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 8),
    _CfprComputePCIeFatalStatsAcsViolationErrors1DayH_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors1DayH.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors1Hour = _CfprComputePCIeFatalStatsAcsViolationErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 9),
    _CfprComputePCIeFatalStatsAcsViolationErrors1Hour_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors1Hour.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors1HourH = _CfprComputePCIeFatalStatsAcsViolationErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 10),
    _CfprComputePCIeFatalStatsAcsViolationErrors1HourH_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors1HourH.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors1Week_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors1Week = _CfprComputePCIeFatalStatsAcsViolationErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 11),
    _CfprComputePCIeFatalStatsAcsViolationErrors1Week_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors1Week.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors1WeekH = _CfprComputePCIeFatalStatsAcsViolationErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 12),
    _CfprComputePCIeFatalStatsAcsViolationErrors1WeekH_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors2Weeks = _CfprComputePCIeFatalStatsAcsViolationErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 13),
    _CfprComputePCIeFatalStatsAcsViolationErrors2Weeks_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalStatsAcsViolationErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalStatsAcsViolationErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalStatsAcsViolationErrors2WeeksH = _CfprComputePCIeFatalStatsAcsViolationErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 14),
    _CfprComputePCIeFatalStatsAcsViolationErrors2WeeksH_Type()
)
cfprComputePCIeFatalStatsAcsViolationErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsAcsViolationErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalStatsIntervals_Type = Gauge32
_CfprComputePCIeFatalStatsIntervals_Object = MibTableColumn
cfprComputePCIeFatalStatsIntervals = _CfprComputePCIeFatalStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 15),
    _CfprComputePCIeFatalStatsIntervals_Type()
)
cfprComputePCIeFatalStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsIntervals.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors_Type = Counter32
_CfprComputePCIeFatalStatsMalformedTLPErrors_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors = _CfprComputePCIeFatalStatsMalformedTLPErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 16),
    _CfprComputePCIeFatalStatsMalformedTLPErrors_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors15Min_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors15Min = _CfprComputePCIeFatalStatsMalformedTLPErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 17),
    _CfprComputePCIeFatalStatsMalformedTLPErrors15Min_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors15Min.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors15MinH = _CfprComputePCIeFatalStatsMalformedTLPErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 18),
    _CfprComputePCIeFatalStatsMalformedTLPErrors15MinH_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors15MinH.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors1Day_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors1Day = _CfprComputePCIeFatalStatsMalformedTLPErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 19),
    _CfprComputePCIeFatalStatsMalformedTLPErrors1Day_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors1Day.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors1DayH = _CfprComputePCIeFatalStatsMalformedTLPErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 20),
    _CfprComputePCIeFatalStatsMalformedTLPErrors1DayH_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors1DayH.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors1Hour = _CfprComputePCIeFatalStatsMalformedTLPErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 21),
    _CfprComputePCIeFatalStatsMalformedTLPErrors1Hour_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors1Hour.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors1HourH = _CfprComputePCIeFatalStatsMalformedTLPErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 22),
    _CfprComputePCIeFatalStatsMalformedTLPErrors1HourH_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors1HourH.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors1Week_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors1Week = _CfprComputePCIeFatalStatsMalformedTLPErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 23),
    _CfprComputePCIeFatalStatsMalformedTLPErrors1Week_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors1Week.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors1WeekH = _CfprComputePCIeFatalStatsMalformedTLPErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 24),
    _CfprComputePCIeFatalStatsMalformedTLPErrors1WeekH_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors2Weeks = _CfprComputePCIeFatalStatsMalformedTLPErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 25),
    _CfprComputePCIeFatalStatsMalformedTLPErrors2Weeks_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH = _CfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 26),
    _CfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH_Type()
)
cfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors_Type = Counter32
_CfprComputePCIeFatalStatsPoisonedTLPErrors_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors = _CfprComputePCIeFatalStatsPoisonedTLPErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 27),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors15Min_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors15Min = _CfprComputePCIeFatalStatsPoisonedTLPErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 28),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors15Min_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors15Min.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors15MinH = _CfprComputePCIeFatalStatsPoisonedTLPErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 29),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors15MinH_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors15MinH.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors1Day_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors1Day = _CfprComputePCIeFatalStatsPoisonedTLPErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 30),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors1Day_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors1Day.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors1DayH = _CfprComputePCIeFatalStatsPoisonedTLPErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 31),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors1DayH_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors1DayH.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors1Hour = _CfprComputePCIeFatalStatsPoisonedTLPErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 32),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors1Hour_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors1Hour.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors1HourH = _CfprComputePCIeFatalStatsPoisonedTLPErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 33),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors1HourH_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors1HourH.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors1Week_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors1Week = _CfprComputePCIeFatalStatsPoisonedTLPErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 34),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors1Week_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors1Week.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH = _CfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 35),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks = _CfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 36),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH = _CfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 37),
    _CfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH_Type()
)
cfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors_Type = Counter32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 38),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 39),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 40),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 41),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 42),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 43),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 44),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 45),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 46),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 47),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks.setStatus("current")
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Type = Gauge32
_CfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Object = MibTableColumn
cfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH = _CfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 48),
    _CfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH_Type()
)
cfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH.setStatus("current")
_CfprComputePCIeFatalStatsSuspect_Type = TruthValue
_CfprComputePCIeFatalStatsSuspect_Object = MibTableColumn
cfprComputePCIeFatalStatsSuspect = _CfprComputePCIeFatalStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 49),
    _CfprComputePCIeFatalStatsSuspect_Type()
)
cfprComputePCIeFatalStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsSuspect.setStatus("current")
_CfprComputePCIeFatalStatsThresholded_Type = CfprComputePCIeFatalStatsThresholded
_CfprComputePCIeFatalStatsThresholded_Object = MibTableColumn
cfprComputePCIeFatalStatsThresholded = _CfprComputePCIeFatalStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 50),
    _CfprComputePCIeFatalStatsThresholded_Type()
)
cfprComputePCIeFatalStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsThresholded.setStatus("current")
_CfprComputePCIeFatalStatsTimeCollected_Type = DateAndTime
_CfprComputePCIeFatalStatsTimeCollected_Object = MibTableColumn
cfprComputePCIeFatalStatsTimeCollected = _CfprComputePCIeFatalStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 51),
    _CfprComputePCIeFatalStatsTimeCollected_Type()
)
cfprComputePCIeFatalStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsTimeCollected.setStatus("current")
_CfprComputePCIeFatalStatsUpdate_Type = Gauge32
_CfprComputePCIeFatalStatsUpdate_Object = MibTableColumn
cfprComputePCIeFatalStatsUpdate = _CfprComputePCIeFatalStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 32, 1, 52),
    _CfprComputePCIeFatalStatsUpdate_Type()
)
cfprComputePCIeFatalStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePCIeFatalStatsUpdate.setStatus("current")
_CfprComputePciCapTable_Object = MibTable
cfprComputePciCapTable = _CfprComputePciCapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33)
)
if mibBuilder.loadTexts:
    cfprComputePciCapTable.setStatus("current")
_CfprComputePciCapEntry_Object = MibTableRow
cfprComputePciCapEntry = _CfprComputePciCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33, 1)
)
cfprComputePciCapEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePciCapInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePciCapEntry.setStatus("current")
_CfprComputePciCapInstanceId_Type = CfprManagedObjectId
_CfprComputePciCapInstanceId_Object = MibTableColumn
cfprComputePciCapInstanceId = _CfprComputePciCapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33, 1, 1),
    _CfprComputePciCapInstanceId_Type()
)
cfprComputePciCapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePciCapInstanceId.setStatus("current")
_CfprComputePciCapDn_Type = CfprManagedObjectDn
_CfprComputePciCapDn_Object = MibTableColumn
cfprComputePciCapDn = _CfprComputePciCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33, 1, 2),
    _CfprComputePciCapDn_Type()
)
cfprComputePciCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciCapDn.setStatus("current")
_CfprComputePciCapRn_Type = SnmpAdminString
_CfprComputePciCapRn_Object = MibTableColumn
cfprComputePciCapRn = _CfprComputePciCapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33, 1, 3),
    _CfprComputePciCapRn_Type()
)
cfprComputePciCapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciCapRn.setStatus("current")
_CfprComputePciCapMaxBusIdPerSlot_Type = Gauge32
_CfprComputePciCapMaxBusIdPerSlot_Object = MibTableColumn
cfprComputePciCapMaxBusIdPerSlot = _CfprComputePciCapMaxBusIdPerSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33, 1, 4),
    _CfprComputePciCapMaxBusIdPerSlot_Type()
)
cfprComputePciCapMaxBusIdPerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciCapMaxBusIdPerSlot.setStatus("current")
_CfprComputePciCapNumOfPhysSlots_Type = Gauge32
_CfprComputePciCapNumOfPhysSlots_Object = MibTableColumn
cfprComputePciCapNumOfPhysSlots = _CfprComputePciCapNumOfPhysSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33, 1, 5),
    _CfprComputePciCapNumOfPhysSlots_Type()
)
cfprComputePciCapNumOfPhysSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciCapNumOfPhysSlots.setStatus("current")
_CfprComputePciCapOrder_Type = CfprComputePciCapOrder
_CfprComputePciCapOrder_Object = MibTableColumn
cfprComputePciCapOrder = _CfprComputePciCapOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33, 1, 6),
    _CfprComputePciCapOrder_Type()
)
cfprComputePciCapOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciCapOrder.setStatus("current")
_CfprComputePciCapStartsWith_Type = Gauge32
_CfprComputePciCapStartsWith_Object = MibTableColumn
cfprComputePciCapStartsWith = _CfprComputePciCapStartsWith_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 33, 1, 7),
    _CfprComputePciCapStartsWith_Type()
)
cfprComputePciCapStartsWith.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciCapStartsWith.setStatus("current")
_CfprComputePciSlotScanDefTable_Object = MibTable
cfprComputePciSlotScanDefTable = _CfprComputePciSlotScanDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34)
)
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefTable.setStatus("current")
_CfprComputePciSlotScanDefEntry_Object = MibTableRow
cfprComputePciSlotScanDefEntry = _CfprComputePciSlotScanDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1)
)
cfprComputePciSlotScanDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePciSlotScanDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefEntry.setStatus("current")
_CfprComputePciSlotScanDefInstanceId_Type = CfprManagedObjectId
_CfprComputePciSlotScanDefInstanceId_Object = MibTableColumn
cfprComputePciSlotScanDefInstanceId = _CfprComputePciSlotScanDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 1),
    _CfprComputePciSlotScanDefInstanceId_Type()
)
cfprComputePciSlotScanDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefInstanceId.setStatus("current")
_CfprComputePciSlotScanDefDn_Type = CfprManagedObjectDn
_CfprComputePciSlotScanDefDn_Object = MibTableColumn
cfprComputePciSlotScanDefDn = _CfprComputePciSlotScanDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 2),
    _CfprComputePciSlotScanDefDn_Type()
)
cfprComputePciSlotScanDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefDn.setStatus("current")
_CfprComputePciSlotScanDefRn_Type = SnmpAdminString
_CfprComputePciSlotScanDefRn_Object = MibTableColumn
cfprComputePciSlotScanDefRn = _CfprComputePciSlotScanDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 3),
    _CfprComputePciSlotScanDefRn_Type()
)
cfprComputePciSlotScanDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefRn.setStatus("current")
_CfprComputePciSlotScanDefDescr_Type = SnmpAdminString
_CfprComputePciSlotScanDefDescr_Object = MibTableColumn
cfprComputePciSlotScanDefDescr = _CfprComputePciSlotScanDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 4),
    _CfprComputePciSlotScanDefDescr_Type()
)
cfprComputePciSlotScanDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefDescr.setStatus("current")
_CfprComputePciSlotScanDefIntId_Type = SnmpAdminString
_CfprComputePciSlotScanDefIntId_Object = MibTableColumn
cfprComputePciSlotScanDefIntId = _CfprComputePciSlotScanDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 5),
    _CfprComputePciSlotScanDefIntId_Type()
)
cfprComputePciSlotScanDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefIntId.setStatus("current")
_CfprComputePciSlotScanDefName_Type = SnmpAdminString
_CfprComputePciSlotScanDefName_Object = MibTableColumn
cfprComputePciSlotScanDefName = _CfprComputePciSlotScanDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 6),
    _CfprComputePciSlotScanDefName_Type()
)
cfprComputePciSlotScanDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefName.setStatus("current")
_CfprComputePciSlotScanDefPolicyLevel_Type = Gauge32
_CfprComputePciSlotScanDefPolicyLevel_Object = MibTableColumn
cfprComputePciSlotScanDefPolicyLevel = _CfprComputePciSlotScanDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 7),
    _CfprComputePciSlotScanDefPolicyLevel_Type()
)
cfprComputePciSlotScanDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefPolicyLevel.setStatus("current")
_CfprComputePciSlotScanDefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputePciSlotScanDefPolicyOwner_Object = MibTableColumn
cfprComputePciSlotScanDefPolicyOwner = _CfprComputePciSlotScanDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 8),
    _CfprComputePciSlotScanDefPolicyOwner_Type()
)
cfprComputePciSlotScanDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefPolicyOwner.setStatus("current")
_CfprComputePciSlotScanDefScanOrder_Type = Gauge32
_CfprComputePciSlotScanDefScanOrder_Object = MibTableColumn
cfprComputePciSlotScanDefScanOrder = _CfprComputePciSlotScanDefScanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 9),
    _CfprComputePciSlotScanDefScanOrder_Type()
)
cfprComputePciSlotScanDefScanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefScanOrder.setStatus("current")
_CfprComputePciSlotScanDefSlotId_Type = Gauge32
_CfprComputePciSlotScanDefSlotId_Object = MibTableColumn
cfprComputePciSlotScanDefSlotId = _CfprComputePciSlotScanDefSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 34, 1, 10),
    _CfprComputePciSlotScanDefSlotId_Type()
)
cfprComputePciSlotScanDefSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePciSlotScanDefSlotId.setStatus("current")
_CfprComputePhysicalAssocCtxTable_Object = MibTable
cfprComputePhysicalAssocCtxTable = _CfprComputePhysicalAssocCtxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 35)
)
if mibBuilder.loadTexts:
    cfprComputePhysicalAssocCtxTable.setStatus("current")
_CfprComputePhysicalAssocCtxEntry_Object = MibTableRow
cfprComputePhysicalAssocCtxEntry = _CfprComputePhysicalAssocCtxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 35, 1)
)
cfprComputePhysicalAssocCtxEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePhysicalAssocCtxInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePhysicalAssocCtxEntry.setStatus("current")
_CfprComputePhysicalAssocCtxInstanceId_Type = CfprManagedObjectId
_CfprComputePhysicalAssocCtxInstanceId_Object = MibTableColumn
cfprComputePhysicalAssocCtxInstanceId = _CfprComputePhysicalAssocCtxInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 35, 1, 1),
    _CfprComputePhysicalAssocCtxInstanceId_Type()
)
cfprComputePhysicalAssocCtxInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePhysicalAssocCtxInstanceId.setStatus("current")
_CfprComputePhysicalAssocCtxDn_Type = CfprManagedObjectDn
_CfprComputePhysicalAssocCtxDn_Object = MibTableColumn
cfprComputePhysicalAssocCtxDn = _CfprComputePhysicalAssocCtxDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 35, 1, 2),
    _CfprComputePhysicalAssocCtxDn_Type()
)
cfprComputePhysicalAssocCtxDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalAssocCtxDn.setStatus("current")
_CfprComputePhysicalAssocCtxRn_Type = SnmpAdminString
_CfprComputePhysicalAssocCtxRn_Object = MibTableColumn
cfprComputePhysicalAssocCtxRn = _CfprComputePhysicalAssocCtxRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 35, 1, 3),
    _CfprComputePhysicalAssocCtxRn_Type()
)
cfprComputePhysicalAssocCtxRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalAssocCtxRn.setStatus("current")
_CfprComputePhysicalAssocCtxFruCapDn_Type = SnmpAdminString
_CfprComputePhysicalAssocCtxFruCapDn_Object = MibTableColumn
cfprComputePhysicalAssocCtxFruCapDn = _CfprComputePhysicalAssocCtxFruCapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 35, 1, 4),
    _CfprComputePhysicalAssocCtxFruCapDn_Type()
)
cfprComputePhysicalAssocCtxFruCapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalAssocCtxFruCapDn.setStatus("current")
_CfprComputePhysicalFsmTable_Object = MibTable
cfprComputePhysicalFsmTable = _CfprComputePhysicalFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36)
)
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTable.setStatus("current")
_CfprComputePhysicalFsmEntry_Object = MibTableRow
cfprComputePhysicalFsmEntry = _CfprComputePhysicalFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1)
)
cfprComputePhysicalFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePhysicalFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmEntry.setStatus("current")
_CfprComputePhysicalFsmInstanceId_Type = CfprManagedObjectId
_CfprComputePhysicalFsmInstanceId_Object = MibTableColumn
cfprComputePhysicalFsmInstanceId = _CfprComputePhysicalFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 1),
    _CfprComputePhysicalFsmInstanceId_Type()
)
cfprComputePhysicalFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmInstanceId.setStatus("current")
_CfprComputePhysicalFsmDn_Type = CfprManagedObjectDn
_CfprComputePhysicalFsmDn_Object = MibTableColumn
cfprComputePhysicalFsmDn = _CfprComputePhysicalFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 2),
    _CfprComputePhysicalFsmDn_Type()
)
cfprComputePhysicalFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmDn.setStatus("current")
_CfprComputePhysicalFsmRn_Type = SnmpAdminString
_CfprComputePhysicalFsmRn_Object = MibTableColumn
cfprComputePhysicalFsmRn = _CfprComputePhysicalFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 3),
    _CfprComputePhysicalFsmRn_Type()
)
cfprComputePhysicalFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmRn.setStatus("current")
_CfprComputePhysicalFsmCompletionTime_Type = DateAndTime
_CfprComputePhysicalFsmCompletionTime_Object = MibTableColumn
cfprComputePhysicalFsmCompletionTime = _CfprComputePhysicalFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 4),
    _CfprComputePhysicalFsmCompletionTime_Type()
)
cfprComputePhysicalFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmCompletionTime.setStatus("current")
_CfprComputePhysicalFsmCurrentFsm_Type = CfprComputePhysicalFsmCurrentFsm
_CfprComputePhysicalFsmCurrentFsm_Object = MibTableColumn
cfprComputePhysicalFsmCurrentFsm = _CfprComputePhysicalFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 5),
    _CfprComputePhysicalFsmCurrentFsm_Type()
)
cfprComputePhysicalFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmCurrentFsm.setStatus("current")
_CfprComputePhysicalFsmDescr_Type = SnmpAdminString
_CfprComputePhysicalFsmDescr_Object = MibTableColumn
cfprComputePhysicalFsmDescr = _CfprComputePhysicalFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 6),
    _CfprComputePhysicalFsmDescr_Type()
)
cfprComputePhysicalFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmDescr.setStatus("current")
_CfprComputePhysicalFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprComputePhysicalFsmFsmStatus_Object = MibTableColumn
cfprComputePhysicalFsmFsmStatus = _CfprComputePhysicalFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 7),
    _CfprComputePhysicalFsmFsmStatus_Type()
)
cfprComputePhysicalFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmFsmStatus.setStatus("current")
_CfprComputePhysicalFsmProgress_Type = Gauge32
_CfprComputePhysicalFsmProgress_Object = MibTableColumn
cfprComputePhysicalFsmProgress = _CfprComputePhysicalFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 8),
    _CfprComputePhysicalFsmProgress_Type()
)
cfprComputePhysicalFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmProgress.setStatus("current")
_CfprComputePhysicalFsmRmtErrCode_Type = Gauge32
_CfprComputePhysicalFsmRmtErrCode_Object = MibTableColumn
cfprComputePhysicalFsmRmtErrCode = _CfprComputePhysicalFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 9),
    _CfprComputePhysicalFsmRmtErrCode_Type()
)
cfprComputePhysicalFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmRmtErrCode.setStatus("current")
_CfprComputePhysicalFsmRmtErrDescr_Type = SnmpAdminString
_CfprComputePhysicalFsmRmtErrDescr_Object = MibTableColumn
cfprComputePhysicalFsmRmtErrDescr = _CfprComputePhysicalFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 10),
    _CfprComputePhysicalFsmRmtErrDescr_Type()
)
cfprComputePhysicalFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmRmtErrDescr.setStatus("current")
_CfprComputePhysicalFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprComputePhysicalFsmRmtRslt_Object = MibTableColumn
cfprComputePhysicalFsmRmtRslt = _CfprComputePhysicalFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 36, 1, 11),
    _CfprComputePhysicalFsmRmtRslt_Type()
)
cfprComputePhysicalFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmRmtRslt.setStatus("current")
_CfprComputePhysicalFsmStageTable_Object = MibTable
cfprComputePhysicalFsmStageTable = _CfprComputePhysicalFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37)
)
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageTable.setStatus("current")
_CfprComputePhysicalFsmStageEntry_Object = MibTableRow
cfprComputePhysicalFsmStageEntry = _CfprComputePhysicalFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1)
)
cfprComputePhysicalFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePhysicalFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageEntry.setStatus("current")
_CfprComputePhysicalFsmStageInstanceId_Type = CfprManagedObjectId
_CfprComputePhysicalFsmStageInstanceId_Object = MibTableColumn
cfprComputePhysicalFsmStageInstanceId = _CfprComputePhysicalFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 1),
    _CfprComputePhysicalFsmStageInstanceId_Type()
)
cfprComputePhysicalFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageInstanceId.setStatus("current")
_CfprComputePhysicalFsmStageDn_Type = CfprManagedObjectDn
_CfprComputePhysicalFsmStageDn_Object = MibTableColumn
cfprComputePhysicalFsmStageDn = _CfprComputePhysicalFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 2),
    _CfprComputePhysicalFsmStageDn_Type()
)
cfprComputePhysicalFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageDn.setStatus("current")
_CfprComputePhysicalFsmStageRn_Type = SnmpAdminString
_CfprComputePhysicalFsmStageRn_Object = MibTableColumn
cfprComputePhysicalFsmStageRn = _CfprComputePhysicalFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 3),
    _CfprComputePhysicalFsmStageRn_Type()
)
cfprComputePhysicalFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageRn.setStatus("current")
_CfprComputePhysicalFsmStageDescr_Type = SnmpAdminString
_CfprComputePhysicalFsmStageDescr_Object = MibTableColumn
cfprComputePhysicalFsmStageDescr = _CfprComputePhysicalFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 4),
    _CfprComputePhysicalFsmStageDescr_Type()
)
cfprComputePhysicalFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageDescr.setStatus("current")
_CfprComputePhysicalFsmStageLastUpdateTime_Type = DateAndTime
_CfprComputePhysicalFsmStageLastUpdateTime_Object = MibTableColumn
cfprComputePhysicalFsmStageLastUpdateTime = _CfprComputePhysicalFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 5),
    _CfprComputePhysicalFsmStageLastUpdateTime_Type()
)
cfprComputePhysicalFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageLastUpdateTime.setStatus("current")
_CfprComputePhysicalFsmStageName_Type = CfprComputePhysicalFsmStageName
_CfprComputePhysicalFsmStageName_Object = MibTableColumn
cfprComputePhysicalFsmStageName = _CfprComputePhysicalFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 6),
    _CfprComputePhysicalFsmStageName_Type()
)
cfprComputePhysicalFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageName.setStatus("current")
_CfprComputePhysicalFsmStageOrder_Type = Gauge32
_CfprComputePhysicalFsmStageOrder_Object = MibTableColumn
cfprComputePhysicalFsmStageOrder = _CfprComputePhysicalFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 7),
    _CfprComputePhysicalFsmStageOrder_Type()
)
cfprComputePhysicalFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageOrder.setStatus("current")
_CfprComputePhysicalFsmStageRetry_Type = Gauge32
_CfprComputePhysicalFsmStageRetry_Object = MibTableColumn
cfprComputePhysicalFsmStageRetry = _CfprComputePhysicalFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 8),
    _CfprComputePhysicalFsmStageRetry_Type()
)
cfprComputePhysicalFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageRetry.setStatus("current")
_CfprComputePhysicalFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprComputePhysicalFsmStageStageStatus_Object = MibTableColumn
cfprComputePhysicalFsmStageStageStatus = _CfprComputePhysicalFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 37, 1, 9),
    _CfprComputePhysicalFsmStageStageStatus_Type()
)
cfprComputePhysicalFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmStageStageStatus.setStatus("current")
_CfprComputePhysicalFsmTaskTable_Object = MibTable
cfprComputePhysicalFsmTaskTable = _CfprComputePhysicalFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38)
)
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskTable.setStatus("current")
_CfprComputePhysicalFsmTaskEntry_Object = MibTableRow
cfprComputePhysicalFsmTaskEntry = _CfprComputePhysicalFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38, 1)
)
cfprComputePhysicalFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePhysicalFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskEntry.setStatus("current")
_CfprComputePhysicalFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprComputePhysicalFsmTaskInstanceId_Object = MibTableColumn
cfprComputePhysicalFsmTaskInstanceId = _CfprComputePhysicalFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38, 1, 1),
    _CfprComputePhysicalFsmTaskInstanceId_Type()
)
cfprComputePhysicalFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskInstanceId.setStatus("current")
_CfprComputePhysicalFsmTaskDn_Type = CfprManagedObjectDn
_CfprComputePhysicalFsmTaskDn_Object = MibTableColumn
cfprComputePhysicalFsmTaskDn = _CfprComputePhysicalFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38, 1, 2),
    _CfprComputePhysicalFsmTaskDn_Type()
)
cfprComputePhysicalFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskDn.setStatus("current")
_CfprComputePhysicalFsmTaskRn_Type = SnmpAdminString
_CfprComputePhysicalFsmTaskRn_Object = MibTableColumn
cfprComputePhysicalFsmTaskRn = _CfprComputePhysicalFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38, 1, 3),
    _CfprComputePhysicalFsmTaskRn_Type()
)
cfprComputePhysicalFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskRn.setStatus("current")
_CfprComputePhysicalFsmTaskCompletion_Type = CfprFsmCompletion
_CfprComputePhysicalFsmTaskCompletion_Object = MibTableColumn
cfprComputePhysicalFsmTaskCompletion = _CfprComputePhysicalFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38, 1, 4),
    _CfprComputePhysicalFsmTaskCompletion_Type()
)
cfprComputePhysicalFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskCompletion.setStatus("current")
_CfprComputePhysicalFsmTaskFlags_Type = CfprComputePhysicalFsmTaskFlags
_CfprComputePhysicalFsmTaskFlags_Object = MibTableColumn
cfprComputePhysicalFsmTaskFlags = _CfprComputePhysicalFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38, 1, 5),
    _CfprComputePhysicalFsmTaskFlags_Type()
)
cfprComputePhysicalFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskFlags.setStatus("current")
_CfprComputePhysicalFsmTaskItem_Type = CfprComputePhysicalFsmTaskItem
_CfprComputePhysicalFsmTaskItem_Object = MibTableColumn
cfprComputePhysicalFsmTaskItem = _CfprComputePhysicalFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38, 1, 6),
    _CfprComputePhysicalFsmTaskItem_Type()
)
cfprComputePhysicalFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskItem.setStatus("current")
_CfprComputePhysicalFsmTaskSeqId_Type = Gauge32
_CfprComputePhysicalFsmTaskSeqId_Object = MibTableColumn
cfprComputePhysicalFsmTaskSeqId = _CfprComputePhysicalFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 38, 1, 7),
    _CfprComputePhysicalFsmTaskSeqId_Type()
)
cfprComputePhysicalFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalFsmTaskSeqId.setStatus("current")
_CfprComputePhysicalQualTable_Object = MibTable
cfprComputePhysicalQualTable = _CfprComputePhysicalQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 39)
)
if mibBuilder.loadTexts:
    cfprComputePhysicalQualTable.setStatus("current")
_CfprComputePhysicalQualEntry_Object = MibTableRow
cfprComputePhysicalQualEntry = _CfprComputePhysicalQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 39, 1)
)
cfprComputePhysicalQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePhysicalQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePhysicalQualEntry.setStatus("current")
_CfprComputePhysicalQualInstanceId_Type = CfprManagedObjectId
_CfprComputePhysicalQualInstanceId_Object = MibTableColumn
cfprComputePhysicalQualInstanceId = _CfprComputePhysicalQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 39, 1, 1),
    _CfprComputePhysicalQualInstanceId_Type()
)
cfprComputePhysicalQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePhysicalQualInstanceId.setStatus("current")
_CfprComputePhysicalQualDn_Type = CfprManagedObjectDn
_CfprComputePhysicalQualDn_Object = MibTableColumn
cfprComputePhysicalQualDn = _CfprComputePhysicalQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 39, 1, 2),
    _CfprComputePhysicalQualDn_Type()
)
cfprComputePhysicalQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalQualDn.setStatus("current")
_CfprComputePhysicalQualRn_Type = SnmpAdminString
_CfprComputePhysicalQualRn_Object = MibTableColumn
cfprComputePhysicalQualRn = _CfprComputePhysicalQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 39, 1, 3),
    _CfprComputePhysicalQualRn_Type()
)
cfprComputePhysicalQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalQualRn.setStatus("current")
_CfprComputePhysicalQualModel_Type = SnmpAdminString
_CfprComputePhysicalQualModel_Object = MibTableColumn
cfprComputePhysicalQualModel = _CfprComputePhysicalQualModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 39, 1, 4),
    _CfprComputePhysicalQualModel_Type()
)
cfprComputePhysicalQualModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePhysicalQualModel.setStatus("current")
_CfprComputePlatformTable_Object = MibTable
cfprComputePlatformTable = _CfprComputePlatformTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40)
)
if mibBuilder.loadTexts:
    cfprComputePlatformTable.setStatus("current")
_CfprComputePlatformEntry_Object = MibTableRow
cfprComputePlatformEntry = _CfprComputePlatformEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40, 1)
)
cfprComputePlatformEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePlatformInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePlatformEntry.setStatus("current")
_CfprComputePlatformInstanceId_Type = CfprManagedObjectId
_CfprComputePlatformInstanceId_Object = MibTableColumn
cfprComputePlatformInstanceId = _CfprComputePlatformInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40, 1, 1),
    _CfprComputePlatformInstanceId_Type()
)
cfprComputePlatformInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePlatformInstanceId.setStatus("current")
_CfprComputePlatformDn_Type = CfprManagedObjectDn
_CfprComputePlatformDn_Object = MibTableColumn
cfprComputePlatformDn = _CfprComputePlatformDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40, 1, 2),
    _CfprComputePlatformDn_Type()
)
cfprComputePlatformDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePlatformDn.setStatus("current")
_CfprComputePlatformRn_Type = SnmpAdminString
_CfprComputePlatformRn_Object = MibTableColumn
cfprComputePlatformRn = _CfprComputePlatformRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40, 1, 3),
    _CfprComputePlatformRn_Type()
)
cfprComputePlatformRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePlatformRn.setStatus("current")
_CfprComputePlatformModel_Type = SnmpAdminString
_CfprComputePlatformModel_Object = MibTableColumn
cfprComputePlatformModel = _CfprComputePlatformModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40, 1, 4),
    _CfprComputePlatformModel_Type()
)
cfprComputePlatformModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePlatformModel.setStatus("current")
_CfprComputePlatformProductName_Type = SnmpAdminString
_CfprComputePlatformProductName_Object = MibTableColumn
cfprComputePlatformProductName = _CfprComputePlatformProductName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40, 1, 5),
    _CfprComputePlatformProductName_Type()
)
cfprComputePlatformProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePlatformProductName.setStatus("current")
_CfprComputePlatformRevision_Type = SnmpAdminString
_CfprComputePlatformRevision_Object = MibTableColumn
cfprComputePlatformRevision = _CfprComputePlatformRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40, 1, 6),
    _CfprComputePlatformRevision_Type()
)
cfprComputePlatformRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePlatformRevision.setStatus("current")
_CfprComputePlatformVendor_Type = SnmpAdminString
_CfprComputePlatformVendor_Object = MibTableColumn
cfprComputePlatformVendor = _CfprComputePlatformVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 40, 1, 7),
    _CfprComputePlatformVendor_Type()
)
cfprComputePlatformVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePlatformVendor.setStatus("current")
_CfprComputePnuOSImageTable_Object = MibTable
cfprComputePnuOSImageTable = _CfprComputePnuOSImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 41)
)
if mibBuilder.loadTexts:
    cfprComputePnuOSImageTable.setStatus("current")
_CfprComputePnuOSImageEntry_Object = MibTableRow
cfprComputePnuOSImageEntry = _CfprComputePnuOSImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 41, 1)
)
cfprComputePnuOSImageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePnuOSImageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePnuOSImageEntry.setStatus("current")
_CfprComputePnuOSImageInstanceId_Type = CfprManagedObjectId
_CfprComputePnuOSImageInstanceId_Object = MibTableColumn
cfprComputePnuOSImageInstanceId = _CfprComputePnuOSImageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 41, 1, 1),
    _CfprComputePnuOSImageInstanceId_Type()
)
cfprComputePnuOSImageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePnuOSImageInstanceId.setStatus("current")
_CfprComputePnuOSImageDn_Type = CfprManagedObjectDn
_CfprComputePnuOSImageDn_Object = MibTableColumn
cfprComputePnuOSImageDn = _CfprComputePnuOSImageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 41, 1, 2),
    _CfprComputePnuOSImageDn_Type()
)
cfprComputePnuOSImageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePnuOSImageDn.setStatus("current")
_CfprComputePnuOSImageRn_Type = SnmpAdminString
_CfprComputePnuOSImageRn_Object = MibTableColumn
cfprComputePnuOSImageRn = _CfprComputePnuOSImageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 41, 1, 3),
    _CfprComputePnuOSImageRn_Type()
)
cfprComputePnuOSImageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePnuOSImageRn.setStatus("current")
_CfprComputePnuOSImageImgLFBFFName_Type = SnmpAdminString
_CfprComputePnuOSImageImgLFBFFName_Object = MibTableColumn
cfprComputePnuOSImageImgLFBFFName = _CfprComputePnuOSImageImgLFBFFName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 41, 1, 4),
    _CfprComputePnuOSImageImgLFBFFName_Type()
)
cfprComputePnuOSImageImgLFBFFName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePnuOSImageImgLFBFFName.setStatus("current")
_CfprComputePnuOSImageImgLoc_Type = SnmpAdminString
_CfprComputePnuOSImageImgLoc_Object = MibTableColumn
cfprComputePnuOSImageImgLoc = _CfprComputePnuOSImageImgLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 41, 1, 5),
    _CfprComputePnuOSImageImgLoc_Type()
)
cfprComputePnuOSImageImgLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePnuOSImageImgLoc.setStatus("current")
_CfprComputePnuOSImageImgName_Type = SnmpAdminString
_CfprComputePnuOSImageImgName_Object = MibTableColumn
cfprComputePnuOSImageImgName = _CfprComputePnuOSImageImgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 41, 1, 6),
    _CfprComputePnuOSImageImgName_Type()
)
cfprComputePnuOSImageImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePnuOSImageImgName.setStatus("current")
_CfprComputePoolTable_Object = MibTable
cfprComputePoolTable = _CfprComputePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42)
)
if mibBuilder.loadTexts:
    cfprComputePoolTable.setStatus("current")
_CfprComputePoolEntry_Object = MibTableRow
cfprComputePoolEntry = _CfprComputePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1)
)
cfprComputePoolEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePoolInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePoolEntry.setStatus("current")
_CfprComputePoolInstanceId_Type = CfprManagedObjectId
_CfprComputePoolInstanceId_Object = MibTableColumn
cfprComputePoolInstanceId = _CfprComputePoolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 1),
    _CfprComputePoolInstanceId_Type()
)
cfprComputePoolInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePoolInstanceId.setStatus("current")
_CfprComputePoolDn_Type = CfprManagedObjectDn
_CfprComputePoolDn_Object = MibTableColumn
cfprComputePoolDn = _CfprComputePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 2),
    _CfprComputePoolDn_Type()
)
cfprComputePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolDn.setStatus("current")
_CfprComputePoolRn_Type = SnmpAdminString
_CfprComputePoolRn_Object = MibTableColumn
cfprComputePoolRn = _CfprComputePoolRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 3),
    _CfprComputePoolRn_Type()
)
cfprComputePoolRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolRn.setStatus("current")
_CfprComputePoolAssigned_Type = Gauge32
_CfprComputePoolAssigned_Object = MibTableColumn
cfprComputePoolAssigned = _CfprComputePoolAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 4),
    _CfprComputePoolAssigned_Type()
)
cfprComputePoolAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolAssigned.setStatus("current")
_CfprComputePoolAssignmentOrder_Type = CfprPoolPoolAssignmentOrder
_CfprComputePoolAssignmentOrder_Object = MibTableColumn
cfprComputePoolAssignmentOrder = _CfprComputePoolAssignmentOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 5),
    _CfprComputePoolAssignmentOrder_Type()
)
cfprComputePoolAssignmentOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolAssignmentOrder.setStatus("current")
_CfprComputePoolDescr_Type = SnmpAdminString
_CfprComputePoolDescr_Object = MibTableColumn
cfprComputePoolDescr = _CfprComputePoolDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 6),
    _CfprComputePoolDescr_Type()
)
cfprComputePoolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolDescr.setStatus("current")
_CfprComputePoolIntId_Type = SnmpAdminString
_CfprComputePoolIntId_Object = MibTableColumn
cfprComputePoolIntId = _CfprComputePoolIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 7),
    _CfprComputePoolIntId_Type()
)
cfprComputePoolIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolIntId.setStatus("current")
_CfprComputePoolName_Type = SnmpAdminString
_CfprComputePoolName_Object = MibTableColumn
cfprComputePoolName = _CfprComputePoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 8),
    _CfprComputePoolName_Type()
)
cfprComputePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolName.setStatus("current")
_CfprComputePoolPolicyLevel_Type = Gauge32
_CfprComputePoolPolicyLevel_Object = MibTableColumn
cfprComputePoolPolicyLevel = _CfprComputePoolPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 9),
    _CfprComputePoolPolicyLevel_Type()
)
cfprComputePoolPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolPolicyLevel.setStatus("current")
_CfprComputePoolPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputePoolPolicyOwner_Object = MibTableColumn
cfprComputePoolPolicyOwner = _CfprComputePoolPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 10),
    _CfprComputePoolPolicyOwner_Type()
)
cfprComputePoolPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolPolicyOwner.setStatus("current")
_CfprComputePoolSize_Type = Gauge32
_CfprComputePoolSize_Object = MibTableColumn
cfprComputePoolSize = _CfprComputePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 42, 1, 11),
    _CfprComputePoolSize_Type()
)
cfprComputePoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolSize.setStatus("current")
_CfprComputePoolPolicyRefTable_Object = MibTable
cfprComputePoolPolicyRefTable = _CfprComputePoolPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 43)
)
if mibBuilder.loadTexts:
    cfprComputePoolPolicyRefTable.setStatus("current")
_CfprComputePoolPolicyRefEntry_Object = MibTableRow
cfprComputePoolPolicyRefEntry = _CfprComputePoolPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 43, 1)
)
cfprComputePoolPolicyRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePoolPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePoolPolicyRefEntry.setStatus("current")
_CfprComputePoolPolicyRefInstanceId_Type = CfprManagedObjectId
_CfprComputePoolPolicyRefInstanceId_Object = MibTableColumn
cfprComputePoolPolicyRefInstanceId = _CfprComputePoolPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 43, 1, 1),
    _CfprComputePoolPolicyRefInstanceId_Type()
)
cfprComputePoolPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePoolPolicyRefInstanceId.setStatus("current")
_CfprComputePoolPolicyRefDn_Type = CfprManagedObjectDn
_CfprComputePoolPolicyRefDn_Object = MibTableColumn
cfprComputePoolPolicyRefDn = _CfprComputePoolPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 43, 1, 2),
    _CfprComputePoolPolicyRefDn_Type()
)
cfprComputePoolPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolPolicyRefDn.setStatus("current")
_CfprComputePoolPolicyRefRn_Type = SnmpAdminString
_CfprComputePoolPolicyRefRn_Object = MibTableColumn
cfprComputePoolPolicyRefRn = _CfprComputePoolPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 43, 1, 3),
    _CfprComputePoolPolicyRefRn_Type()
)
cfprComputePoolPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolPolicyRefRn.setStatus("current")
_CfprComputePoolPolicyRefId_Type = Unsigned64
_CfprComputePoolPolicyRefId_Object = MibTableColumn
cfprComputePoolPolicyRefId = _CfprComputePoolPolicyRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 43, 1, 4),
    _CfprComputePoolPolicyRefId_Type()
)
cfprComputePoolPolicyRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolPolicyRefId.setStatus("current")
_CfprComputePoolPolicyRefPolicyDn_Type = SnmpAdminString
_CfprComputePoolPolicyRefPolicyDn_Object = MibTableColumn
cfprComputePoolPolicyRefPolicyDn = _CfprComputePoolPolicyRefPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 43, 1, 5),
    _CfprComputePoolPolicyRefPolicyDn_Type()
)
cfprComputePoolPolicyRefPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolPolicyRefPolicyDn.setStatus("current")
_CfprComputePoolableTable_Object = MibTable
cfprComputePoolableTable = _CfprComputePoolableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 44)
)
if mibBuilder.loadTexts:
    cfprComputePoolableTable.setStatus("current")
_CfprComputePoolableEntry_Object = MibTableRow
cfprComputePoolableEntry = _CfprComputePoolableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 44, 1)
)
cfprComputePoolableEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePoolableInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePoolableEntry.setStatus("current")
_CfprComputePoolableInstanceId_Type = CfprManagedObjectId
_CfprComputePoolableInstanceId_Object = MibTableColumn
cfprComputePoolableInstanceId = _CfprComputePoolableInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 44, 1, 1),
    _CfprComputePoolableInstanceId_Type()
)
cfprComputePoolableInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePoolableInstanceId.setStatus("current")
_CfprComputePoolableDn_Type = CfprManagedObjectDn
_CfprComputePoolableDn_Object = MibTableColumn
cfprComputePoolableDn = _CfprComputePoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 44, 1, 2),
    _CfprComputePoolableDn_Type()
)
cfprComputePoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolableDn.setStatus("current")
_CfprComputePoolableRn_Type = SnmpAdminString
_CfprComputePoolableRn_Object = MibTableColumn
cfprComputePoolableRn = _CfprComputePoolableRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 44, 1, 3),
    _CfprComputePoolableRn_Type()
)
cfprComputePoolableRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolableRn.setStatus("current")
_CfprComputePoolableId_Type = Unsigned64
_CfprComputePoolableId_Object = MibTableColumn
cfprComputePoolableId = _CfprComputePoolableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 44, 1, 4),
    _CfprComputePoolableId_Type()
)
cfprComputePoolableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolableId.setStatus("current")
_CfprComputePoolablePoolDn_Type = SnmpAdminString
_CfprComputePoolablePoolDn_Object = MibTableColumn
cfprComputePoolablePoolDn = _CfprComputePoolablePoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 44, 1, 5),
    _CfprComputePoolablePoolDn_Type()
)
cfprComputePoolablePoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolablePoolDn.setStatus("current")
_CfprComputePooledRackUnitTable_Object = MibTable
cfprComputePooledRackUnitTable = _CfprComputePooledRackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45)
)
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitTable.setStatus("current")
_CfprComputePooledRackUnitEntry_Object = MibTableRow
cfprComputePooledRackUnitEntry = _CfprComputePooledRackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1)
)
cfprComputePooledRackUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePooledRackUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitEntry.setStatus("current")
_CfprComputePooledRackUnitInstanceId_Type = CfprManagedObjectId
_CfprComputePooledRackUnitInstanceId_Object = MibTableColumn
cfprComputePooledRackUnitInstanceId = _CfprComputePooledRackUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 1),
    _CfprComputePooledRackUnitInstanceId_Type()
)
cfprComputePooledRackUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitInstanceId.setStatus("current")
_CfprComputePooledRackUnitDn_Type = CfprManagedObjectDn
_CfprComputePooledRackUnitDn_Object = MibTableColumn
cfprComputePooledRackUnitDn = _CfprComputePooledRackUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 2),
    _CfprComputePooledRackUnitDn_Type()
)
cfprComputePooledRackUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitDn.setStatus("current")
_CfprComputePooledRackUnitRn_Type = SnmpAdminString
_CfprComputePooledRackUnitRn_Object = MibTableColumn
cfprComputePooledRackUnitRn = _CfprComputePooledRackUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 3),
    _CfprComputePooledRackUnitRn_Type()
)
cfprComputePooledRackUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitRn.setStatus("current")
_CfprComputePooledRackUnitAssigned_Type = TruthValue
_CfprComputePooledRackUnitAssigned_Object = MibTableColumn
cfprComputePooledRackUnitAssigned = _CfprComputePooledRackUnitAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 4),
    _CfprComputePooledRackUnitAssigned_Type()
)
cfprComputePooledRackUnitAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitAssigned.setStatus("current")
_CfprComputePooledRackUnitAssignedToDn_Type = SnmpAdminString
_CfprComputePooledRackUnitAssignedToDn_Object = MibTableColumn
cfprComputePooledRackUnitAssignedToDn = _CfprComputePooledRackUnitAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 5),
    _CfprComputePooledRackUnitAssignedToDn_Type()
)
cfprComputePooledRackUnitAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitAssignedToDn.setStatus("current")
_CfprComputePooledRackUnitId_Type = CfprComputePooledRackUnitId
_CfprComputePooledRackUnitId_Object = MibTableColumn
cfprComputePooledRackUnitId = _CfprComputePooledRackUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 6),
    _CfprComputePooledRackUnitId_Type()
)
cfprComputePooledRackUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitId.setStatus("current")
_CfprComputePooledRackUnitOwner_Type = CfprComputeOwner
_CfprComputePooledRackUnitOwner_Object = MibTableColumn
cfprComputePooledRackUnitOwner = _CfprComputePooledRackUnitOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 7),
    _CfprComputePooledRackUnitOwner_Type()
)
cfprComputePooledRackUnitOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitOwner.setStatus("current")
_CfprComputePooledRackUnitPoolableDn_Type = SnmpAdminString
_CfprComputePooledRackUnitPoolableDn_Object = MibTableColumn
cfprComputePooledRackUnitPoolableDn = _CfprComputePooledRackUnitPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 8),
    _CfprComputePooledRackUnitPoolableDn_Type()
)
cfprComputePooledRackUnitPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitPoolableDn.setStatus("current")
_CfprComputePooledRackUnitPrevAssignedToDn_Type = SnmpAdminString
_CfprComputePooledRackUnitPrevAssignedToDn_Object = MibTableColumn
cfprComputePooledRackUnitPrevAssignedToDn = _CfprComputePooledRackUnitPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 45, 1, 9),
    _CfprComputePooledRackUnitPrevAssignedToDn_Type()
)
cfprComputePooledRackUnitPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledRackUnitPrevAssignedToDn.setStatus("current")
_CfprComputePooledSlotTable_Object = MibTable
cfprComputePooledSlotTable = _CfprComputePooledSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46)
)
if mibBuilder.loadTexts:
    cfprComputePooledSlotTable.setStatus("current")
_CfprComputePooledSlotEntry_Object = MibTableRow
cfprComputePooledSlotEntry = _CfprComputePooledSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1)
)
cfprComputePooledSlotEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePooledSlotInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePooledSlotEntry.setStatus("current")
_CfprComputePooledSlotInstanceId_Type = CfprManagedObjectId
_CfprComputePooledSlotInstanceId_Object = MibTableColumn
cfprComputePooledSlotInstanceId = _CfprComputePooledSlotInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 1),
    _CfprComputePooledSlotInstanceId_Type()
)
cfprComputePooledSlotInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePooledSlotInstanceId.setStatus("current")
_CfprComputePooledSlotDn_Type = CfprManagedObjectDn
_CfprComputePooledSlotDn_Object = MibTableColumn
cfprComputePooledSlotDn = _CfprComputePooledSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 2),
    _CfprComputePooledSlotDn_Type()
)
cfprComputePooledSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotDn.setStatus("current")
_CfprComputePooledSlotRn_Type = SnmpAdminString
_CfprComputePooledSlotRn_Object = MibTableColumn
cfprComputePooledSlotRn = _CfprComputePooledSlotRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 3),
    _CfprComputePooledSlotRn_Type()
)
cfprComputePooledSlotRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotRn.setStatus("current")
_CfprComputePooledSlotAssigned_Type = TruthValue
_CfprComputePooledSlotAssigned_Object = MibTableColumn
cfprComputePooledSlotAssigned = _CfprComputePooledSlotAssigned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 4),
    _CfprComputePooledSlotAssigned_Type()
)
cfprComputePooledSlotAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotAssigned.setStatus("current")
_CfprComputePooledSlotAssignedToDn_Type = SnmpAdminString
_CfprComputePooledSlotAssignedToDn_Object = MibTableColumn
cfprComputePooledSlotAssignedToDn = _CfprComputePooledSlotAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 5),
    _CfprComputePooledSlotAssignedToDn_Type()
)
cfprComputePooledSlotAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotAssignedToDn.setStatus("current")
_CfprComputePooledSlotChassisId_Type = Gauge32
_CfprComputePooledSlotChassisId_Object = MibTableColumn
cfprComputePooledSlotChassisId = _CfprComputePooledSlotChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 6),
    _CfprComputePooledSlotChassisId_Type()
)
cfprComputePooledSlotChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotChassisId.setStatus("current")
_CfprComputePooledSlotOwner_Type = CfprComputeOwner
_CfprComputePooledSlotOwner_Object = MibTableColumn
cfprComputePooledSlotOwner = _CfprComputePooledSlotOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 7),
    _CfprComputePooledSlotOwner_Type()
)
cfprComputePooledSlotOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotOwner.setStatus("current")
_CfprComputePooledSlotPoolableDn_Type = SnmpAdminString
_CfprComputePooledSlotPoolableDn_Object = MibTableColumn
cfprComputePooledSlotPoolableDn = _CfprComputePooledSlotPoolableDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 8),
    _CfprComputePooledSlotPoolableDn_Type()
)
cfprComputePooledSlotPoolableDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotPoolableDn.setStatus("current")
_CfprComputePooledSlotPrevAssignedToDn_Type = SnmpAdminString
_CfprComputePooledSlotPrevAssignedToDn_Object = MibTableColumn
cfprComputePooledSlotPrevAssignedToDn = _CfprComputePooledSlotPrevAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 9),
    _CfprComputePooledSlotPrevAssignedToDn_Type()
)
cfprComputePooledSlotPrevAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotPrevAssignedToDn.setStatus("current")
_CfprComputePooledSlotSlotId_Type = CfprComputePooledSlotSlotId
_CfprComputePooledSlotSlotId_Object = MibTableColumn
cfprComputePooledSlotSlotId = _CfprComputePooledSlotSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 46, 1, 10),
    _CfprComputePooledSlotSlotId_Type()
)
cfprComputePooledSlotSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePooledSlotSlotId.setStatus("current")
_CfprComputePoolingPolicyTable_Object = MibTable
cfprComputePoolingPolicyTable = _CfprComputePoolingPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47)
)
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyTable.setStatus("current")
_CfprComputePoolingPolicyEntry_Object = MibTableRow
cfprComputePoolingPolicyEntry = _CfprComputePoolingPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1)
)
cfprComputePoolingPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePoolingPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyEntry.setStatus("current")
_CfprComputePoolingPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputePoolingPolicyInstanceId_Object = MibTableColumn
cfprComputePoolingPolicyInstanceId = _CfprComputePoolingPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 1),
    _CfprComputePoolingPolicyInstanceId_Type()
)
cfprComputePoolingPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyInstanceId.setStatus("current")
_CfprComputePoolingPolicyDn_Type = CfprManagedObjectDn
_CfprComputePoolingPolicyDn_Object = MibTableColumn
cfprComputePoolingPolicyDn = _CfprComputePoolingPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 2),
    _CfprComputePoolingPolicyDn_Type()
)
cfprComputePoolingPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyDn.setStatus("current")
_CfprComputePoolingPolicyRn_Type = SnmpAdminString
_CfprComputePoolingPolicyRn_Object = MibTableColumn
cfprComputePoolingPolicyRn = _CfprComputePoolingPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 3),
    _CfprComputePoolingPolicyRn_Type()
)
cfprComputePoolingPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyRn.setStatus("current")
_CfprComputePoolingPolicyDescr_Type = SnmpAdminString
_CfprComputePoolingPolicyDescr_Object = MibTableColumn
cfprComputePoolingPolicyDescr = _CfprComputePoolingPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 4),
    _CfprComputePoolingPolicyDescr_Type()
)
cfprComputePoolingPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyDescr.setStatus("current")
_CfprComputePoolingPolicyIntId_Type = SnmpAdminString
_CfprComputePoolingPolicyIntId_Object = MibTableColumn
cfprComputePoolingPolicyIntId = _CfprComputePoolingPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 5),
    _CfprComputePoolingPolicyIntId_Type()
)
cfprComputePoolingPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyIntId.setStatus("current")
_CfprComputePoolingPolicyName_Type = SnmpAdminString
_CfprComputePoolingPolicyName_Object = MibTableColumn
cfprComputePoolingPolicyName = _CfprComputePoolingPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 6),
    _CfprComputePoolingPolicyName_Type()
)
cfprComputePoolingPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyName.setStatus("current")
_CfprComputePoolingPolicyPolicyLevel_Type = Gauge32
_CfprComputePoolingPolicyPolicyLevel_Object = MibTableColumn
cfprComputePoolingPolicyPolicyLevel = _CfprComputePoolingPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 7),
    _CfprComputePoolingPolicyPolicyLevel_Type()
)
cfprComputePoolingPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyPolicyLevel.setStatus("current")
_CfprComputePoolingPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputePoolingPolicyPolicyOwner_Object = MibTableColumn
cfprComputePoolingPolicyPolicyOwner = _CfprComputePoolingPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 8),
    _CfprComputePoolingPolicyPolicyOwner_Type()
)
cfprComputePoolingPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyPolicyOwner.setStatus("current")
_CfprComputePoolingPolicyPoolDn_Type = SnmpAdminString
_CfprComputePoolingPolicyPoolDn_Object = MibTableColumn
cfprComputePoolingPolicyPoolDn = _CfprComputePoolingPolicyPoolDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 9),
    _CfprComputePoolingPolicyPoolDn_Type()
)
cfprComputePoolingPolicyPoolDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyPoolDn.setStatus("current")
_CfprComputePoolingPolicyQualifier_Type = SnmpAdminString
_CfprComputePoolingPolicyQualifier_Object = MibTableColumn
cfprComputePoolingPolicyQualifier = _CfprComputePoolingPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 47, 1, 10),
    _CfprComputePoolingPolicyQualifier_Type()
)
cfprComputePoolingPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePoolingPolicyQualifier.setStatus("current")
_CfprComputePsuControlTable_Object = MibTable
cfprComputePsuControlTable = _CfprComputePsuControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48)
)
if mibBuilder.loadTexts:
    cfprComputePsuControlTable.setStatus("current")
_CfprComputePsuControlEntry_Object = MibTableRow
cfprComputePsuControlEntry = _CfprComputePsuControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1)
)
cfprComputePsuControlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePsuControlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePsuControlEntry.setStatus("current")
_CfprComputePsuControlInstanceId_Type = CfprManagedObjectId
_CfprComputePsuControlInstanceId_Object = MibTableColumn
cfprComputePsuControlInstanceId = _CfprComputePsuControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 1),
    _CfprComputePsuControlInstanceId_Type()
)
cfprComputePsuControlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePsuControlInstanceId.setStatus("current")
_CfprComputePsuControlDn_Type = CfprManagedObjectDn
_CfprComputePsuControlDn_Object = MibTableColumn
cfprComputePsuControlDn = _CfprComputePsuControlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 2),
    _CfprComputePsuControlDn_Type()
)
cfprComputePsuControlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlDn.setStatus("current")
_CfprComputePsuControlRn_Type = SnmpAdminString
_CfprComputePsuControlRn_Object = MibTableColumn
cfprComputePsuControlRn = _CfprComputePsuControlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 3),
    _CfprComputePsuControlRn_Type()
)
cfprComputePsuControlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlRn.setStatus("current")
_CfprComputePsuControlClusterState_Type = CfprComputePsuClusterState
_CfprComputePsuControlClusterState_Object = MibTableColumn
cfprComputePsuControlClusterState = _CfprComputePsuControlClusterState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 4),
    _CfprComputePsuControlClusterState_Type()
)
cfprComputePsuControlClusterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlClusterState.setStatus("current")
_CfprComputePsuControlDescr_Type = SnmpAdminString
_CfprComputePsuControlDescr_Object = MibTableColumn
cfprComputePsuControlDescr = _CfprComputePsuControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 5),
    _CfprComputePsuControlDescr_Type()
)
cfprComputePsuControlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlDescr.setStatus("current")
_CfprComputePsuControlInputPowerState_Type = CfprEquipmentSensorThresholdStatus
_CfprComputePsuControlInputPowerState_Object = MibTableColumn
cfprComputePsuControlInputPowerState = _CfprComputePsuControlInputPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 6),
    _CfprComputePsuControlInputPowerState_Type()
)
cfprComputePsuControlInputPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlInputPowerState.setStatus("current")
_CfprComputePsuControlIntId_Type = SnmpAdminString
_CfprComputePsuControlIntId_Object = MibTableColumn
cfprComputePsuControlIntId = _CfprComputePsuControlIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 7),
    _CfprComputePsuControlIntId_Type()
)
cfprComputePsuControlIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlIntId.setStatus("current")
_CfprComputePsuControlName_Type = SnmpAdminString
_CfprComputePsuControlName_Object = MibTableColumn
cfprComputePsuControlName = _CfprComputePsuControlName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 8),
    _CfprComputePsuControlName_Type()
)
cfprComputePsuControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlName.setStatus("current")
_CfprComputePsuControlOperQualifier_Type = CfprComputePsuRedundancyOperQualifier
_CfprComputePsuControlOperQualifier_Object = MibTableColumn
cfprComputePsuControlOperQualifier = _CfprComputePsuControlOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 9),
    _CfprComputePsuControlOperQualifier_Type()
)
cfprComputePsuControlOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlOperQualifier.setStatus("current")
_CfprComputePsuControlOperState_Type = CfprComputePsuRedundancyOperState
_CfprComputePsuControlOperState_Object = MibTableColumn
cfprComputePsuControlOperState = _CfprComputePsuControlOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 10),
    _CfprComputePsuControlOperState_Type()
)
cfprComputePsuControlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlOperState.setStatus("current")
_CfprComputePsuControlOutputPowerState_Type = CfprEquipmentSensorThresholdStatus
_CfprComputePsuControlOutputPowerState_Object = MibTableColumn
cfprComputePsuControlOutputPowerState = _CfprComputePsuControlOutputPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 11),
    _CfprComputePsuControlOutputPowerState_Type()
)
cfprComputePsuControlOutputPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlOutputPowerState.setStatus("current")
_CfprComputePsuControlPolicyLevel_Type = Gauge32
_CfprComputePsuControlPolicyLevel_Object = MibTableColumn
cfprComputePsuControlPolicyLevel = _CfprComputePsuControlPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 12),
    _CfprComputePsuControlPolicyLevel_Type()
)
cfprComputePsuControlPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlPolicyLevel.setStatus("current")
_CfprComputePsuControlPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputePsuControlPolicyOwner_Object = MibTableColumn
cfprComputePsuControlPolicyOwner = _CfprComputePsuControlPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 13),
    _CfprComputePsuControlPolicyOwner_Type()
)
cfprComputePsuControlPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlPolicyOwner.setStatus("current")
_CfprComputePsuControlRedundancy_Type = CfprComputePsuControlRedundancy
_CfprComputePsuControlRedundancy_Object = MibTableColumn
cfprComputePsuControlRedundancy = _CfprComputePsuControlRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 48, 1, 14),
    _CfprComputePsuControlRedundancy_Type()
)
cfprComputePsuControlRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuControlRedundancy.setStatus("current")
_CfprComputePsuPolicyTable_Object = MibTable
cfprComputePsuPolicyTable = _CfprComputePsuPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49)
)
if mibBuilder.loadTexts:
    cfprComputePsuPolicyTable.setStatus("current")
_CfprComputePsuPolicyEntry_Object = MibTableRow
cfprComputePsuPolicyEntry = _CfprComputePsuPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1)
)
cfprComputePsuPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputePsuPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputePsuPolicyEntry.setStatus("current")
_CfprComputePsuPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputePsuPolicyInstanceId_Object = MibTableColumn
cfprComputePsuPolicyInstanceId = _CfprComputePsuPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 1),
    _CfprComputePsuPolicyInstanceId_Type()
)
cfprComputePsuPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyInstanceId.setStatus("current")
_CfprComputePsuPolicyDn_Type = CfprManagedObjectDn
_CfprComputePsuPolicyDn_Object = MibTableColumn
cfprComputePsuPolicyDn = _CfprComputePsuPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 2),
    _CfprComputePsuPolicyDn_Type()
)
cfprComputePsuPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyDn.setStatus("current")
_CfprComputePsuPolicyRn_Type = SnmpAdminString
_CfprComputePsuPolicyRn_Object = MibTableColumn
cfprComputePsuPolicyRn = _CfprComputePsuPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 3),
    _CfprComputePsuPolicyRn_Type()
)
cfprComputePsuPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyRn.setStatus("current")
_CfprComputePsuPolicyDescr_Type = SnmpAdminString
_CfprComputePsuPolicyDescr_Object = MibTableColumn
cfprComputePsuPolicyDescr = _CfprComputePsuPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 4),
    _CfprComputePsuPolicyDescr_Type()
)
cfprComputePsuPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyDescr.setStatus("current")
_CfprComputePsuPolicyIntId_Type = SnmpAdminString
_CfprComputePsuPolicyIntId_Object = MibTableColumn
cfprComputePsuPolicyIntId = _CfprComputePsuPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 5),
    _CfprComputePsuPolicyIntId_Type()
)
cfprComputePsuPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyIntId.setStatus("current")
_CfprComputePsuPolicyName_Type = SnmpAdminString
_CfprComputePsuPolicyName_Object = MibTableColumn
cfprComputePsuPolicyName = _CfprComputePsuPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 6),
    _CfprComputePsuPolicyName_Type()
)
cfprComputePsuPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyName.setStatus("current")
_CfprComputePsuPolicyPolicyLevel_Type = Gauge32
_CfprComputePsuPolicyPolicyLevel_Object = MibTableColumn
cfprComputePsuPolicyPolicyLevel = _CfprComputePsuPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 7),
    _CfprComputePsuPolicyPolicyLevel_Type()
)
cfprComputePsuPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyPolicyLevel.setStatus("current")
_CfprComputePsuPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputePsuPolicyPolicyOwner_Object = MibTableColumn
cfprComputePsuPolicyPolicyOwner = _CfprComputePsuPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 8),
    _CfprComputePsuPolicyPolicyOwner_Type()
)
cfprComputePsuPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyPolicyOwner.setStatus("current")
_CfprComputePsuPolicyRedundancy_Type = CfprComputePsuRedundancy
_CfprComputePsuPolicyRedundancy_Object = MibTableColumn
cfprComputePsuPolicyRedundancy = _CfprComputePsuPolicyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 49, 1, 9),
    _CfprComputePsuPolicyRedundancy_Type()
)
cfprComputePsuPolicyRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputePsuPolicyRedundancy.setStatus("current")
_CfprComputeQualTable_Object = MibTable
cfprComputeQualTable = _CfprComputeQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50)
)
if mibBuilder.loadTexts:
    cfprComputeQualTable.setStatus("current")
_CfprComputeQualEntry_Object = MibTableRow
cfprComputeQualEntry = _CfprComputeQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1)
)
cfprComputeQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeQualEntry.setStatus("current")
_CfprComputeQualInstanceId_Type = CfprManagedObjectId
_CfprComputeQualInstanceId_Object = MibTableColumn
cfprComputeQualInstanceId = _CfprComputeQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1, 1),
    _CfprComputeQualInstanceId_Type()
)
cfprComputeQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeQualInstanceId.setStatus("current")
_CfprComputeQualDn_Type = CfprManagedObjectDn
_CfprComputeQualDn_Object = MibTableColumn
cfprComputeQualDn = _CfprComputeQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1, 2),
    _CfprComputeQualDn_Type()
)
cfprComputeQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeQualDn.setStatus("current")
_CfprComputeQualRn_Type = SnmpAdminString
_CfprComputeQualRn_Object = MibTableColumn
cfprComputeQualRn = _CfprComputeQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1, 3),
    _CfprComputeQualRn_Type()
)
cfprComputeQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeQualRn.setStatus("current")
_CfprComputeQualDescr_Type = SnmpAdminString
_CfprComputeQualDescr_Object = MibTableColumn
cfprComputeQualDescr = _CfprComputeQualDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1, 4),
    _CfprComputeQualDescr_Type()
)
cfprComputeQualDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeQualDescr.setStatus("current")
_CfprComputeQualIntId_Type = SnmpAdminString
_CfprComputeQualIntId_Object = MibTableColumn
cfprComputeQualIntId = _CfprComputeQualIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1, 5),
    _CfprComputeQualIntId_Type()
)
cfprComputeQualIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeQualIntId.setStatus("current")
_CfprComputeQualName_Type = SnmpAdminString
_CfprComputeQualName_Object = MibTableColumn
cfprComputeQualName = _CfprComputeQualName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1, 6),
    _CfprComputeQualName_Type()
)
cfprComputeQualName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeQualName.setStatus("current")
_CfprComputeQualPolicyLevel_Type = Gauge32
_CfprComputeQualPolicyLevel_Object = MibTableColumn
cfprComputeQualPolicyLevel = _CfprComputeQualPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1, 7),
    _CfprComputeQualPolicyLevel_Type()
)
cfprComputeQualPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeQualPolicyLevel.setStatus("current")
_CfprComputeQualPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeQualPolicyOwner_Object = MibTableColumn
cfprComputeQualPolicyOwner = _CfprComputeQualPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 50, 1, 8),
    _CfprComputeQualPolicyOwner_Type()
)
cfprComputeQualPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeQualPolicyOwner.setStatus("current")
_CfprComputeRackQualTable_Object = MibTable
cfprComputeRackQualTable = _CfprComputeRackQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 51)
)
if mibBuilder.loadTexts:
    cfprComputeRackQualTable.setStatus("current")
_CfprComputeRackQualEntry_Object = MibTableRow
cfprComputeRackQualEntry = _CfprComputeRackQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 51, 1)
)
cfprComputeRackQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeRackQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeRackQualEntry.setStatus("current")
_CfprComputeRackQualInstanceId_Type = CfprManagedObjectId
_CfprComputeRackQualInstanceId_Object = MibTableColumn
cfprComputeRackQualInstanceId = _CfprComputeRackQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 51, 1, 1),
    _CfprComputeRackQualInstanceId_Type()
)
cfprComputeRackQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeRackQualInstanceId.setStatus("current")
_CfprComputeRackQualDn_Type = CfprManagedObjectDn
_CfprComputeRackQualDn_Object = MibTableColumn
cfprComputeRackQualDn = _CfprComputeRackQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 51, 1, 2),
    _CfprComputeRackQualDn_Type()
)
cfprComputeRackQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackQualDn.setStatus("current")
_CfprComputeRackQualRn_Type = SnmpAdminString
_CfprComputeRackQualRn_Object = MibTableColumn
cfprComputeRackQualRn = _CfprComputeRackQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 51, 1, 3),
    _CfprComputeRackQualRn_Type()
)
cfprComputeRackQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackQualRn.setStatus("current")
_CfprComputeRackQualMaxId_Type = CfprComputeRackQualMaxId
_CfprComputeRackQualMaxId_Object = MibTableColumn
cfprComputeRackQualMaxId = _CfprComputeRackQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 51, 1, 4),
    _CfprComputeRackQualMaxId_Type()
)
cfprComputeRackQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackQualMaxId.setStatus("current")
_CfprComputeRackQualMinId_Type = CfprComputeRackQualMinId
_CfprComputeRackQualMinId_Object = MibTableColumn
cfprComputeRackQualMinId = _CfprComputeRackQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 51, 1, 5),
    _CfprComputeRackQualMinId_Type()
)
cfprComputeRackQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackQualMinId.setStatus("current")
_CfprComputeRackUnitTable_Object = MibTable
cfprComputeRackUnitTable = _CfprComputeRackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52)
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitTable.setStatus("current")
_CfprComputeRackUnitEntry_Object = MibTableRow
cfprComputeRackUnitEntry = _CfprComputeRackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1)
)
cfprComputeRackUnitEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeRackUnitInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitEntry.setStatus("current")
_CfprComputeRackUnitInstanceId_Type = CfprManagedObjectId
_CfprComputeRackUnitInstanceId_Object = MibTableColumn
cfprComputeRackUnitInstanceId = _CfprComputeRackUnitInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 1),
    _CfprComputeRackUnitInstanceId_Type()
)
cfprComputeRackUnitInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeRackUnitInstanceId.setStatus("current")
_CfprComputeRackUnitDn_Type = CfprManagedObjectDn
_CfprComputeRackUnitDn_Object = MibTableColumn
cfprComputeRackUnitDn = _CfprComputeRackUnitDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 2),
    _CfprComputeRackUnitDn_Type()
)
cfprComputeRackUnitDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitDn.setStatus("current")
_CfprComputeRackUnitRn_Type = SnmpAdminString
_CfprComputeRackUnitRn_Object = MibTableColumn
cfprComputeRackUnitRn = _CfprComputeRackUnitRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 3),
    _CfprComputeRackUnitRn_Type()
)
cfprComputeRackUnitRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitRn.setStatus("current")
_CfprComputeRackUnitAdminPower_Type = CfprComputeAdminPowerState
_CfprComputeRackUnitAdminPower_Object = MibTableColumn
cfprComputeRackUnitAdminPower = _CfprComputeRackUnitAdminPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 4),
    _CfprComputeRackUnitAdminPower_Type()
)
cfprComputeRackUnitAdminPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitAdminPower.setStatus("current")
_CfprComputeRackUnitAdminState_Type = CfprComputeAdminState
_CfprComputeRackUnitAdminState_Object = MibTableColumn
cfprComputeRackUnitAdminState = _CfprComputeRackUnitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 5),
    _CfprComputeRackUnitAdminState_Type()
)
cfprComputeRackUnitAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitAdminState.setStatus("current")
_CfprComputeRackUnitAssignedToDn_Type = SnmpAdminString
_CfprComputeRackUnitAssignedToDn_Object = MibTableColumn
cfprComputeRackUnitAssignedToDn = _CfprComputeRackUnitAssignedToDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 6),
    _CfprComputeRackUnitAssignedToDn_Type()
)
cfprComputeRackUnitAssignedToDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitAssignedToDn.setStatus("current")
_CfprComputeRackUnitAssociation_Type = CfprComputeAssociation
_CfprComputeRackUnitAssociation_Object = MibTableColumn
cfprComputeRackUnitAssociation = _CfprComputeRackUnitAssociation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 7),
    _CfprComputeRackUnitAssociation_Type()
)
cfprComputeRackUnitAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitAssociation.setStatus("current")
_CfprComputeRackUnitAvailability_Type = CfprComputeAvailability
_CfprComputeRackUnitAvailability_Object = MibTableColumn
cfprComputeRackUnitAvailability = _CfprComputeRackUnitAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 8),
    _CfprComputeRackUnitAvailability_Type()
)
cfprComputeRackUnitAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitAvailability.setStatus("current")
_CfprComputeRackUnitAvailableMemory_Type = Gauge32
_CfprComputeRackUnitAvailableMemory_Object = MibTableColumn
cfprComputeRackUnitAvailableMemory = _CfprComputeRackUnitAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 9),
    _CfprComputeRackUnitAvailableMemory_Type()
)
cfprComputeRackUnitAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitAvailableMemory.setStatus("current")
_CfprComputeRackUnitCheckPoint_Type = CfprComputeCheckPoint
_CfprComputeRackUnitCheckPoint_Object = MibTableColumn
cfprComputeRackUnitCheckPoint = _CfprComputeRackUnitCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 10),
    _CfprComputeRackUnitCheckPoint_Type()
)
cfprComputeRackUnitCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitCheckPoint.setStatus("current")
_CfprComputeRackUnitConnPath_Type = CfprEquipmentConnectionStatus
_CfprComputeRackUnitConnPath_Object = MibTableColumn
cfprComputeRackUnitConnPath = _CfprComputeRackUnitConnPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 11),
    _CfprComputeRackUnitConnPath_Type()
)
cfprComputeRackUnitConnPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitConnPath.setStatus("current")
_CfprComputeRackUnitConnStatus_Type = CfprEquipmentConnectionStatus
_CfprComputeRackUnitConnStatus_Object = MibTableColumn
cfprComputeRackUnitConnStatus = _CfprComputeRackUnitConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 12),
    _CfprComputeRackUnitConnStatus_Type()
)
cfprComputeRackUnitConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitConnStatus.setStatus("current")
_CfprComputeRackUnitDescr_Type = SnmpAdminString
_CfprComputeRackUnitDescr_Object = MibTableColumn
cfprComputeRackUnitDescr = _CfprComputeRackUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 13),
    _CfprComputeRackUnitDescr_Type()
)
cfprComputeRackUnitDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitDescr.setStatus("current")
_CfprComputeRackUnitDiscovery_Type = CfprComputeDiscovery
_CfprComputeRackUnitDiscovery_Object = MibTableColumn
cfprComputeRackUnitDiscovery = _CfprComputeRackUnitDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 14),
    _CfprComputeRackUnitDiscovery_Type()
)
cfprComputeRackUnitDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitDiscovery.setStatus("current")
_CfprComputeRackUnitFltAggr_Type = Unsigned64
_CfprComputeRackUnitFltAggr_Object = MibTableColumn
cfprComputeRackUnitFltAggr = _CfprComputeRackUnitFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 15),
    _CfprComputeRackUnitFltAggr_Type()
)
cfprComputeRackUnitFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFltAggr.setStatus("current")
_CfprComputeRackUnitFsmDescr_Type = SnmpAdminString
_CfprComputeRackUnitFsmDescr_Object = MibTableColumn
cfprComputeRackUnitFsmDescr = _CfprComputeRackUnitFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 16),
    _CfprComputeRackUnitFsmDescr_Type()
)
cfprComputeRackUnitFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmDescr.setStatus("current")
_CfprComputeRackUnitFsmFlags_Type = SnmpAdminString
_CfprComputeRackUnitFsmFlags_Object = MibTableColumn
cfprComputeRackUnitFsmFlags = _CfprComputeRackUnitFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 17),
    _CfprComputeRackUnitFsmFlags_Type()
)
cfprComputeRackUnitFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmFlags.setStatus("current")
_CfprComputeRackUnitFsmPrev_Type = SnmpAdminString
_CfprComputeRackUnitFsmPrev_Object = MibTableColumn
cfprComputeRackUnitFsmPrev = _CfprComputeRackUnitFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 18),
    _CfprComputeRackUnitFsmPrev_Type()
)
cfprComputeRackUnitFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmPrev.setStatus("current")
_CfprComputeRackUnitFsmProgr_Type = Gauge32
_CfprComputeRackUnitFsmProgr_Object = MibTableColumn
cfprComputeRackUnitFsmProgr = _CfprComputeRackUnitFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 19),
    _CfprComputeRackUnitFsmProgr_Type()
)
cfprComputeRackUnitFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmProgr.setStatus("current")
_CfprComputeRackUnitFsmRmtInvErrCode_Type = Gauge32
_CfprComputeRackUnitFsmRmtInvErrCode_Object = MibTableColumn
cfprComputeRackUnitFsmRmtInvErrCode = _CfprComputeRackUnitFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 20),
    _CfprComputeRackUnitFsmRmtInvErrCode_Type()
)
cfprComputeRackUnitFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmRmtInvErrCode.setStatus("current")
_CfprComputeRackUnitFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprComputeRackUnitFsmRmtInvErrDescr_Object = MibTableColumn
cfprComputeRackUnitFsmRmtInvErrDescr = _CfprComputeRackUnitFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 21),
    _CfprComputeRackUnitFsmRmtInvErrDescr_Type()
)
cfprComputeRackUnitFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmRmtInvErrDescr.setStatus("current")
_CfprComputeRackUnitFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprComputeRackUnitFsmRmtInvRslt_Object = MibTableColumn
cfprComputeRackUnitFsmRmtInvRslt = _CfprComputeRackUnitFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 22),
    _CfprComputeRackUnitFsmRmtInvRslt_Type()
)
cfprComputeRackUnitFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmRmtInvRslt.setStatus("current")
_CfprComputeRackUnitFsmStageDescr_Type = SnmpAdminString
_CfprComputeRackUnitFsmStageDescr_Object = MibTableColumn
cfprComputeRackUnitFsmStageDescr = _CfprComputeRackUnitFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 23),
    _CfprComputeRackUnitFsmStageDescr_Type()
)
cfprComputeRackUnitFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageDescr.setStatus("current")
_CfprComputeRackUnitFsmStamp_Type = DateAndTime
_CfprComputeRackUnitFsmStamp_Object = MibTableColumn
cfprComputeRackUnitFsmStamp = _CfprComputeRackUnitFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 24),
    _CfprComputeRackUnitFsmStamp_Type()
)
cfprComputeRackUnitFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStamp.setStatus("current")
_CfprComputeRackUnitFsmStatus_Type = SnmpAdminString
_CfprComputeRackUnitFsmStatus_Object = MibTableColumn
cfprComputeRackUnitFsmStatus = _CfprComputeRackUnitFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 25),
    _CfprComputeRackUnitFsmStatus_Type()
)
cfprComputeRackUnitFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStatus.setStatus("current")
_CfprComputeRackUnitFsmTry_Type = Gauge32
_CfprComputeRackUnitFsmTry_Object = MibTableColumn
cfprComputeRackUnitFsmTry = _CfprComputeRackUnitFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 26),
    _CfprComputeRackUnitFsmTry_Type()
)
cfprComputeRackUnitFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTry.setStatus("current")
_CfprComputeRackUnitId_Type = CfprComputeRackUnitId
_CfprComputeRackUnitId_Object = MibTableColumn
cfprComputeRackUnitId = _CfprComputeRackUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 27),
    _CfprComputeRackUnitId_Type()
)
cfprComputeRackUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitId.setStatus("current")
_CfprComputeRackUnitIntId_Type = SnmpAdminString
_CfprComputeRackUnitIntId_Object = MibTableColumn
cfprComputeRackUnitIntId = _CfprComputeRackUnitIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 28),
    _CfprComputeRackUnitIntId_Type()
)
cfprComputeRackUnitIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitIntId.setStatus("current")
_CfprComputeRackUnitLc_Type = CfprComputeAdminTrigger
_CfprComputeRackUnitLc_Object = MibTableColumn
cfprComputeRackUnitLc = _CfprComputeRackUnitLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 29),
    _CfprComputeRackUnitLc_Type()
)
cfprComputeRackUnitLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitLc.setStatus("current")
_CfprComputeRackUnitLcTs_Type = DateAndTime
_CfprComputeRackUnitLcTs_Object = MibTableColumn
cfprComputeRackUnitLcTs = _CfprComputeRackUnitLcTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 30),
    _CfprComputeRackUnitLcTs_Type()
)
cfprComputeRackUnitLcTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitLcTs.setStatus("current")
_CfprComputeRackUnitLocalId_Type = SnmpAdminString
_CfprComputeRackUnitLocalId_Object = MibTableColumn
cfprComputeRackUnitLocalId = _CfprComputeRackUnitLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 31),
    _CfprComputeRackUnitLocalId_Type()
)
cfprComputeRackUnitLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitLocalId.setStatus("current")
_CfprComputeRackUnitLowVoltageMemory_Type = CfprComputePhysicalLowVoltageMemory
_CfprComputeRackUnitLowVoltageMemory_Object = MibTableColumn
cfprComputeRackUnitLowVoltageMemory = _CfprComputeRackUnitLowVoltageMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 32),
    _CfprComputeRackUnitLowVoltageMemory_Type()
)
cfprComputeRackUnitLowVoltageMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitLowVoltageMemory.setStatus("current")
_CfprComputeRackUnitManagingInst_Type = CfprNetworkSwitchId
_CfprComputeRackUnitManagingInst_Object = MibTableColumn
cfprComputeRackUnitManagingInst = _CfprComputeRackUnitManagingInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 33),
    _CfprComputeRackUnitManagingInst_Type()
)
cfprComputeRackUnitManagingInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitManagingInst.setStatus("current")
_CfprComputeRackUnitMemorySpeed_Type = Gauge32
_CfprComputeRackUnitMemorySpeed_Object = MibTableColumn
cfprComputeRackUnitMemorySpeed = _CfprComputeRackUnitMemorySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 34),
    _CfprComputeRackUnitMemorySpeed_Type()
)
cfprComputeRackUnitMemorySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMemorySpeed.setStatus("current")
_CfprComputeRackUnitMfgTime_Type = DateAndTime
_CfprComputeRackUnitMfgTime_Object = MibTableColumn
cfprComputeRackUnitMfgTime = _CfprComputeRackUnitMfgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 35),
    _CfprComputeRackUnitMfgTime_Type()
)
cfprComputeRackUnitMfgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMfgTime.setStatus("current")
_CfprComputeRackUnitModel_Type = SnmpAdminString
_CfprComputeRackUnitModel_Object = MibTableColumn
cfprComputeRackUnitModel = _CfprComputeRackUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 36),
    _CfprComputeRackUnitModel_Type()
)
cfprComputeRackUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitModel.setStatus("current")
_CfprComputeRackUnitName_Type = SnmpAdminString
_CfprComputeRackUnitName_Object = MibTableColumn
cfprComputeRackUnitName = _CfprComputeRackUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 37),
    _CfprComputeRackUnitName_Type()
)
cfprComputeRackUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitName.setStatus("current")
_CfprComputeRackUnitNumOfAdaptors_Type = Gauge32
_CfprComputeRackUnitNumOfAdaptors_Object = MibTableColumn
cfprComputeRackUnitNumOfAdaptors = _CfprComputeRackUnitNumOfAdaptors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 38),
    _CfprComputeRackUnitNumOfAdaptors_Type()
)
cfprComputeRackUnitNumOfAdaptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitNumOfAdaptors.setStatus("current")
_CfprComputeRackUnitNumOfCores_Type = Gauge32
_CfprComputeRackUnitNumOfCores_Object = MibTableColumn
cfprComputeRackUnitNumOfCores = _CfprComputeRackUnitNumOfCores_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 39),
    _CfprComputeRackUnitNumOfCores_Type()
)
cfprComputeRackUnitNumOfCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitNumOfCores.setStatus("current")
_CfprComputeRackUnitNumOfCoresEnabled_Type = Gauge32
_CfprComputeRackUnitNumOfCoresEnabled_Object = MibTableColumn
cfprComputeRackUnitNumOfCoresEnabled = _CfprComputeRackUnitNumOfCoresEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 40),
    _CfprComputeRackUnitNumOfCoresEnabled_Type()
)
cfprComputeRackUnitNumOfCoresEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitNumOfCoresEnabled.setStatus("current")
_CfprComputeRackUnitNumOfCpus_Type = Gauge32
_CfprComputeRackUnitNumOfCpus_Object = MibTableColumn
cfprComputeRackUnitNumOfCpus = _CfprComputeRackUnitNumOfCpus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 41),
    _CfprComputeRackUnitNumOfCpus_Type()
)
cfprComputeRackUnitNumOfCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitNumOfCpus.setStatus("current")
_CfprComputeRackUnitNumOfEthHostIfs_Type = Gauge32
_CfprComputeRackUnitNumOfEthHostIfs_Object = MibTableColumn
cfprComputeRackUnitNumOfEthHostIfs = _CfprComputeRackUnitNumOfEthHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 42),
    _CfprComputeRackUnitNumOfEthHostIfs_Type()
)
cfprComputeRackUnitNumOfEthHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitNumOfEthHostIfs.setStatus("current")
_CfprComputeRackUnitNumOfFcHostIfs_Type = Gauge32
_CfprComputeRackUnitNumOfFcHostIfs_Object = MibTableColumn
cfprComputeRackUnitNumOfFcHostIfs = _CfprComputeRackUnitNumOfFcHostIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 43),
    _CfprComputeRackUnitNumOfFcHostIfs_Type()
)
cfprComputeRackUnitNumOfFcHostIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitNumOfFcHostIfs.setStatus("current")
_CfprComputeRackUnitNumOfThreads_Type = Gauge32
_CfprComputeRackUnitNumOfThreads_Object = MibTableColumn
cfprComputeRackUnitNumOfThreads = _CfprComputeRackUnitNumOfThreads_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 44),
    _CfprComputeRackUnitNumOfThreads_Type()
)
cfprComputeRackUnitNumOfThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitNumOfThreads.setStatus("current")
_CfprComputeRackUnitOperPower_Type = CfprEquipmentPowerState
_CfprComputeRackUnitOperPower_Object = MibTableColumn
cfprComputeRackUnitOperPower = _CfprComputeRackUnitOperPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 45),
    _CfprComputeRackUnitOperPower_Type()
)
cfprComputeRackUnitOperPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitOperPower.setStatus("current")
_CfprComputeRackUnitOperQualifier_Type = CfprComputeIssues
_CfprComputeRackUnitOperQualifier_Object = MibTableColumn
cfprComputeRackUnitOperQualifier = _CfprComputeRackUnitOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 46),
    _CfprComputeRackUnitOperQualifier_Type()
)
cfprComputeRackUnitOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitOperQualifier.setStatus("current")
_CfprComputeRackUnitOperState_Type = CfprLsOperState
_CfprComputeRackUnitOperState_Object = MibTableColumn
cfprComputeRackUnitOperState = _CfprComputeRackUnitOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 47),
    _CfprComputeRackUnitOperState_Type()
)
cfprComputeRackUnitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitOperState.setStatus("current")
_CfprComputeRackUnitOperability_Type = CfprEquipmentOperability
_CfprComputeRackUnitOperability_Object = MibTableColumn
cfprComputeRackUnitOperability = _CfprComputeRackUnitOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 48),
    _CfprComputeRackUnitOperability_Type()
)
cfprComputeRackUnitOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitOperability.setStatus("current")
_CfprComputeRackUnitOriginalUuid_Type = SnmpAdminString
_CfprComputeRackUnitOriginalUuid_Object = MibTableColumn
cfprComputeRackUnitOriginalUuid = _CfprComputeRackUnitOriginalUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 49),
    _CfprComputeRackUnitOriginalUuid_Type()
)
cfprComputeRackUnitOriginalUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitOriginalUuid.setStatus("current")
_CfprComputeRackUnitPartNumber_Type = SnmpAdminString
_CfprComputeRackUnitPartNumber_Object = MibTableColumn
cfprComputeRackUnitPartNumber = _CfprComputeRackUnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 50),
    _CfprComputeRackUnitPartNumber_Type()
)
cfprComputeRackUnitPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitPartNumber.setStatus("current")
_CfprComputeRackUnitPolicyLevel_Type = Gauge32
_CfprComputeRackUnitPolicyLevel_Object = MibTableColumn
cfprComputeRackUnitPolicyLevel = _CfprComputeRackUnitPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 51),
    _CfprComputeRackUnitPolicyLevel_Type()
)
cfprComputeRackUnitPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitPolicyLevel.setStatus("current")
_CfprComputeRackUnitPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeRackUnitPolicyOwner_Object = MibTableColumn
cfprComputeRackUnitPolicyOwner = _CfprComputeRackUnitPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 52),
    _CfprComputeRackUnitPolicyOwner_Type()
)
cfprComputeRackUnitPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitPolicyOwner.setStatus("current")
_CfprComputeRackUnitPresence_Type = CfprEquipmentSlotStatus
_CfprComputeRackUnitPresence_Object = MibTableColumn
cfprComputeRackUnitPresence = _CfprComputeRackUnitPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 53),
    _CfprComputeRackUnitPresence_Type()
)
cfprComputeRackUnitPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitPresence.setStatus("current")
_CfprComputeRackUnitRevision_Type = SnmpAdminString
_CfprComputeRackUnitRevision_Object = MibTableColumn
cfprComputeRackUnitRevision = _CfprComputeRackUnitRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 54),
    _CfprComputeRackUnitRevision_Type()
)
cfprComputeRackUnitRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitRevision.setStatus("current")
_CfprComputeRackUnitSerial_Type = SnmpAdminString
_CfprComputeRackUnitSerial_Object = MibTableColumn
cfprComputeRackUnitSerial = _CfprComputeRackUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 55),
    _CfprComputeRackUnitSerial_Type()
)
cfprComputeRackUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitSerial.setStatus("current")
_CfprComputeRackUnitServerId_Type = SnmpAdminString
_CfprComputeRackUnitServerId_Object = MibTableColumn
cfprComputeRackUnitServerId = _CfprComputeRackUnitServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 56),
    _CfprComputeRackUnitServerId_Type()
)
cfprComputeRackUnitServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitServerId.setStatus("current")
_CfprComputeRackUnitTotalMemory_Type = Gauge32
_CfprComputeRackUnitTotalMemory_Object = MibTableColumn
cfprComputeRackUnitTotalMemory = _CfprComputeRackUnitTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 57),
    _CfprComputeRackUnitTotalMemory_Type()
)
cfprComputeRackUnitTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitTotalMemory.setStatus("current")
_CfprComputeRackUnitUsrLbl_Type = SnmpAdminString
_CfprComputeRackUnitUsrLbl_Object = MibTableColumn
cfprComputeRackUnitUsrLbl = _CfprComputeRackUnitUsrLbl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 58),
    _CfprComputeRackUnitUsrLbl_Type()
)
cfprComputeRackUnitUsrLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitUsrLbl.setStatus("current")
_CfprComputeRackUnitUuid_Type = SnmpAdminString
_CfprComputeRackUnitUuid_Object = MibTableColumn
cfprComputeRackUnitUuid = _CfprComputeRackUnitUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 59),
    _CfprComputeRackUnitUuid_Type()
)
cfprComputeRackUnitUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitUuid.setStatus("current")
_CfprComputeRackUnitVendor_Type = SnmpAdminString
_CfprComputeRackUnitVendor_Object = MibTableColumn
cfprComputeRackUnitVendor = _CfprComputeRackUnitVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 60),
    _CfprComputeRackUnitVendor_Type()
)
cfprComputeRackUnitVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitVendor.setStatus("current")
_CfprComputeRackUnitVersionHolder_Type = TruthValue
_CfprComputeRackUnitVersionHolder_Object = MibTableColumn
cfprComputeRackUnitVersionHolder = _CfprComputeRackUnitVersionHolder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 61),
    _CfprComputeRackUnitVersionHolder_Type()
)
cfprComputeRackUnitVersionHolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitVersionHolder.setStatus("current")
_CfprComputeRackUnitVid_Type = SnmpAdminString
_CfprComputeRackUnitVid_Object = MibTableColumn
cfprComputeRackUnitVid = _CfprComputeRackUnitVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 62),
    _CfprComputeRackUnitVid_Type()
)
cfprComputeRackUnitVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitVid.setStatus("current")
_CfprComputeRackUnitPostState_Type = CfprEquipmentBiosPostState
_CfprComputeRackUnitPostState_Object = MibTableColumn
cfprComputeRackUnitPostState = _CfprComputeRackUnitPostState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 52, 1, 63),
    _CfprComputeRackUnitPostState_Type()
)
cfprComputeRackUnitPostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitPostState.setStatus("current")
_CfprComputeRackUnitFsmTable_Object = MibTable
cfprComputeRackUnitFsmTable = _CfprComputeRackUnitFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53)
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTable.setStatus("current")
_CfprComputeRackUnitFsmEntry_Object = MibTableRow
cfprComputeRackUnitFsmEntry = _CfprComputeRackUnitFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1)
)
cfprComputeRackUnitFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeRackUnitFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmEntry.setStatus("current")
_CfprComputeRackUnitFsmInstanceId_Type = CfprManagedObjectId
_CfprComputeRackUnitFsmInstanceId_Object = MibTableColumn
cfprComputeRackUnitFsmInstanceId = _CfprComputeRackUnitFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 1),
    _CfprComputeRackUnitFsmInstanceId_Type()
)
cfprComputeRackUnitFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmInstanceId.setStatus("current")
_CfprComputeRackUnitFsmDn_Type = CfprManagedObjectDn
_CfprComputeRackUnitFsmDn_Object = MibTableColumn
cfprComputeRackUnitFsmDn = _CfprComputeRackUnitFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 2),
    _CfprComputeRackUnitFsmDn_Type()
)
cfprComputeRackUnitFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmDn.setStatus("current")
_CfprComputeRackUnitFsmRn_Type = SnmpAdminString
_CfprComputeRackUnitFsmRn_Object = MibTableColumn
cfprComputeRackUnitFsmRn = _CfprComputeRackUnitFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 3),
    _CfprComputeRackUnitFsmRn_Type()
)
cfprComputeRackUnitFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmRn.setStatus("current")
_CfprComputeRackUnitFsmCompletionTime_Type = DateAndTime
_CfprComputeRackUnitFsmCompletionTime_Object = MibTableColumn
cfprComputeRackUnitFsmCompletionTime = _CfprComputeRackUnitFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 4),
    _CfprComputeRackUnitFsmCompletionTime_Type()
)
cfprComputeRackUnitFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmCompletionTime.setStatus("current")
_CfprComputeRackUnitFsmCurrentFsm_Type = CfprComputeRackUnitFsmCurrentFsm
_CfprComputeRackUnitFsmCurrentFsm_Object = MibTableColumn
cfprComputeRackUnitFsmCurrentFsm = _CfprComputeRackUnitFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 5),
    _CfprComputeRackUnitFsmCurrentFsm_Type()
)
cfprComputeRackUnitFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmCurrentFsm.setStatus("current")
_CfprComputeRackUnitFsmDescrData_Type = SnmpAdminString
_CfprComputeRackUnitFsmDescrData_Object = MibTableColumn
cfprComputeRackUnitFsmDescrData = _CfprComputeRackUnitFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 6),
    _CfprComputeRackUnitFsmDescrData_Type()
)
cfprComputeRackUnitFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmDescrData.setStatus("current")
_CfprComputeRackUnitFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprComputeRackUnitFsmFsmStatus_Object = MibTableColumn
cfprComputeRackUnitFsmFsmStatus = _CfprComputeRackUnitFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 7),
    _CfprComputeRackUnitFsmFsmStatus_Type()
)
cfprComputeRackUnitFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmFsmStatus.setStatus("current")
_CfprComputeRackUnitFsmProgress_Type = Gauge32
_CfprComputeRackUnitFsmProgress_Object = MibTableColumn
cfprComputeRackUnitFsmProgress = _CfprComputeRackUnitFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 8),
    _CfprComputeRackUnitFsmProgress_Type()
)
cfprComputeRackUnitFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmProgress.setStatus("current")
_CfprComputeRackUnitFsmRmtErrCode_Type = Gauge32
_CfprComputeRackUnitFsmRmtErrCode_Object = MibTableColumn
cfprComputeRackUnitFsmRmtErrCode = _CfprComputeRackUnitFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 9),
    _CfprComputeRackUnitFsmRmtErrCode_Type()
)
cfprComputeRackUnitFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmRmtErrCode.setStatus("current")
_CfprComputeRackUnitFsmRmtErrDescr_Type = SnmpAdminString
_CfprComputeRackUnitFsmRmtErrDescr_Object = MibTableColumn
cfprComputeRackUnitFsmRmtErrDescr = _CfprComputeRackUnitFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 10),
    _CfprComputeRackUnitFsmRmtErrDescr_Type()
)
cfprComputeRackUnitFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmRmtErrDescr.setStatus("current")
_CfprComputeRackUnitFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprComputeRackUnitFsmRmtRslt_Object = MibTableColumn
cfprComputeRackUnitFsmRmtRslt = _CfprComputeRackUnitFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 53, 1, 11),
    _CfprComputeRackUnitFsmRmtRslt_Type()
)
cfprComputeRackUnitFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmRmtRslt.setStatus("current")
_CfprComputeRackUnitFsmStageTable_Object = MibTable
cfprComputeRackUnitFsmStageTable = _CfprComputeRackUnitFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54)
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageTable.setStatus("current")
_CfprComputeRackUnitFsmStageEntry_Object = MibTableRow
cfprComputeRackUnitFsmStageEntry = _CfprComputeRackUnitFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1)
)
cfprComputeRackUnitFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeRackUnitFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageEntry.setStatus("current")
_CfprComputeRackUnitFsmStageInstanceId_Type = CfprManagedObjectId
_CfprComputeRackUnitFsmStageInstanceId_Object = MibTableColumn
cfprComputeRackUnitFsmStageInstanceId = _CfprComputeRackUnitFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 1),
    _CfprComputeRackUnitFsmStageInstanceId_Type()
)
cfprComputeRackUnitFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageInstanceId.setStatus("current")
_CfprComputeRackUnitFsmStageDn_Type = CfprManagedObjectDn
_CfprComputeRackUnitFsmStageDn_Object = MibTableColumn
cfprComputeRackUnitFsmStageDn = _CfprComputeRackUnitFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 2),
    _CfprComputeRackUnitFsmStageDn_Type()
)
cfprComputeRackUnitFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageDn.setStatus("current")
_CfprComputeRackUnitFsmStageRn_Type = SnmpAdminString
_CfprComputeRackUnitFsmStageRn_Object = MibTableColumn
cfprComputeRackUnitFsmStageRn = _CfprComputeRackUnitFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 3),
    _CfprComputeRackUnitFsmStageRn_Type()
)
cfprComputeRackUnitFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageRn.setStatus("current")
_CfprComputeRackUnitFsmStageDescrData_Type = SnmpAdminString
_CfprComputeRackUnitFsmStageDescrData_Object = MibTableColumn
cfprComputeRackUnitFsmStageDescrData = _CfprComputeRackUnitFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 4),
    _CfprComputeRackUnitFsmStageDescrData_Type()
)
cfprComputeRackUnitFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageDescrData.setStatus("current")
_CfprComputeRackUnitFsmStageLastUpdateTime_Type = DateAndTime
_CfprComputeRackUnitFsmStageLastUpdateTime_Object = MibTableColumn
cfprComputeRackUnitFsmStageLastUpdateTime = _CfprComputeRackUnitFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 5),
    _CfprComputeRackUnitFsmStageLastUpdateTime_Type()
)
cfprComputeRackUnitFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageLastUpdateTime.setStatus("current")
_CfprComputeRackUnitFsmStageName_Type = CfprComputeRackUnitFsmStageName
_CfprComputeRackUnitFsmStageName_Object = MibTableColumn
cfprComputeRackUnitFsmStageName = _CfprComputeRackUnitFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 6),
    _CfprComputeRackUnitFsmStageName_Type()
)
cfprComputeRackUnitFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageName.setStatus("current")
_CfprComputeRackUnitFsmStageOrder_Type = Gauge32
_CfprComputeRackUnitFsmStageOrder_Object = MibTableColumn
cfprComputeRackUnitFsmStageOrder = _CfprComputeRackUnitFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 7),
    _CfprComputeRackUnitFsmStageOrder_Type()
)
cfprComputeRackUnitFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageOrder.setStatus("current")
_CfprComputeRackUnitFsmStageRetry_Type = Gauge32
_CfprComputeRackUnitFsmStageRetry_Object = MibTableColumn
cfprComputeRackUnitFsmStageRetry = _CfprComputeRackUnitFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 8),
    _CfprComputeRackUnitFsmStageRetry_Type()
)
cfprComputeRackUnitFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageRetry.setStatus("current")
_CfprComputeRackUnitFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprComputeRackUnitFsmStageStageStatus_Object = MibTableColumn
cfprComputeRackUnitFsmStageStageStatus = _CfprComputeRackUnitFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 54, 1, 9),
    _CfprComputeRackUnitFsmStageStageStatus_Type()
)
cfprComputeRackUnitFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmStageStageStatus.setStatus("current")
_CfprComputeRackUnitFsmTaskTable_Object = MibTable
cfprComputeRackUnitFsmTaskTable = _CfprComputeRackUnitFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55)
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskTable.setStatus("current")
_CfprComputeRackUnitFsmTaskEntry_Object = MibTableRow
cfprComputeRackUnitFsmTaskEntry = _CfprComputeRackUnitFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55, 1)
)
cfprComputeRackUnitFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeRackUnitFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskEntry.setStatus("current")
_CfprComputeRackUnitFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprComputeRackUnitFsmTaskInstanceId_Object = MibTableColumn
cfprComputeRackUnitFsmTaskInstanceId = _CfprComputeRackUnitFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55, 1, 1),
    _CfprComputeRackUnitFsmTaskInstanceId_Type()
)
cfprComputeRackUnitFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskInstanceId.setStatus("current")
_CfprComputeRackUnitFsmTaskDn_Type = CfprManagedObjectDn
_CfprComputeRackUnitFsmTaskDn_Object = MibTableColumn
cfprComputeRackUnitFsmTaskDn = _CfprComputeRackUnitFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55, 1, 2),
    _CfprComputeRackUnitFsmTaskDn_Type()
)
cfprComputeRackUnitFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskDn.setStatus("current")
_CfprComputeRackUnitFsmTaskRn_Type = SnmpAdminString
_CfprComputeRackUnitFsmTaskRn_Object = MibTableColumn
cfprComputeRackUnitFsmTaskRn = _CfprComputeRackUnitFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55, 1, 3),
    _CfprComputeRackUnitFsmTaskRn_Type()
)
cfprComputeRackUnitFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskRn.setStatus("current")
_CfprComputeRackUnitFsmTaskCompletion_Type = CfprFsmCompletion
_CfprComputeRackUnitFsmTaskCompletion_Object = MibTableColumn
cfprComputeRackUnitFsmTaskCompletion = _CfprComputeRackUnitFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55, 1, 4),
    _CfprComputeRackUnitFsmTaskCompletion_Type()
)
cfprComputeRackUnitFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskCompletion.setStatus("current")
_CfprComputeRackUnitFsmTaskFlags_Type = CfprComputeRackUnitFsmTaskFlags
_CfprComputeRackUnitFsmTaskFlags_Object = MibTableColumn
cfprComputeRackUnitFsmTaskFlags = _CfprComputeRackUnitFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55, 1, 5),
    _CfprComputeRackUnitFsmTaskFlags_Type()
)
cfprComputeRackUnitFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskFlags.setStatus("current")
_CfprComputeRackUnitFsmTaskItem_Type = CfprComputeRackUnitFsmTaskItem
_CfprComputeRackUnitFsmTaskItem_Object = MibTableColumn
cfprComputeRackUnitFsmTaskItem = _CfprComputeRackUnitFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55, 1, 6),
    _CfprComputeRackUnitFsmTaskItem_Type()
)
cfprComputeRackUnitFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskItem.setStatus("current")
_CfprComputeRackUnitFsmTaskSeqId_Type = Gauge32
_CfprComputeRackUnitFsmTaskSeqId_Object = MibTableColumn
cfprComputeRackUnitFsmTaskSeqId = _CfprComputeRackUnitFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 55, 1, 7),
    _CfprComputeRackUnitFsmTaskSeqId_Type()
)
cfprComputeRackUnitFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitFsmTaskSeqId.setStatus("current")
_CfprComputeRackUnitMbTempStatsTable_Object = MibTable
cfprComputeRackUnitMbTempStatsTable = _CfprComputeRackUnitMbTempStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56)
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsTable.setStatus("current")
_CfprComputeRackUnitMbTempStatsEntry_Object = MibTableRow
cfprComputeRackUnitMbTempStatsEntry = _CfprComputeRackUnitMbTempStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1)
)
cfprComputeRackUnitMbTempStatsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeRackUnitMbTempStatsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsEntry.setStatus("current")
_CfprComputeRackUnitMbTempStatsInstanceId_Type = CfprManagedObjectId
_CfprComputeRackUnitMbTempStatsInstanceId_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsInstanceId = _CfprComputeRackUnitMbTempStatsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 1),
    _CfprComputeRackUnitMbTempStatsInstanceId_Type()
)
cfprComputeRackUnitMbTempStatsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsInstanceId.setStatus("current")
_CfprComputeRackUnitMbTempStatsDn_Type = CfprManagedObjectDn
_CfprComputeRackUnitMbTempStatsDn_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsDn = _CfprComputeRackUnitMbTempStatsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 2),
    _CfprComputeRackUnitMbTempStatsDn_Type()
)
cfprComputeRackUnitMbTempStatsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsDn.setStatus("current")
_CfprComputeRackUnitMbTempStatsRn_Type = SnmpAdminString
_CfprComputeRackUnitMbTempStatsRn_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsRn = _CfprComputeRackUnitMbTempStatsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 3),
    _CfprComputeRackUnitMbTempStatsRn_Type()
)
cfprComputeRackUnitMbTempStatsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsRn.setStatus("current")
_CfprComputeRackUnitMbTempStatsAmbientTemp_Type = Integer32
_CfprComputeRackUnitMbTempStatsAmbientTemp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsAmbientTemp = _CfprComputeRackUnitMbTempStatsAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 4),
    _CfprComputeRackUnitMbTempStatsAmbientTemp_Type()
)
cfprComputeRackUnitMbTempStatsAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsAmbientTemp.setStatus("current")
_CfprComputeRackUnitMbTempStatsAmbientTempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsAmbientTempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsAmbientTempAvg = _CfprComputeRackUnitMbTempStatsAmbientTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 5),
    _CfprComputeRackUnitMbTempStatsAmbientTempAvg_Type()
)
cfprComputeRackUnitMbTempStatsAmbientTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsAmbientTempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsAmbientTempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsAmbientTempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsAmbientTempMax = _CfprComputeRackUnitMbTempStatsAmbientTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 6),
    _CfprComputeRackUnitMbTempStatsAmbientTempMax_Type()
)
cfprComputeRackUnitMbTempStatsAmbientTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsAmbientTempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsAmbientTempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsAmbientTempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsAmbientTempMin = _CfprComputeRackUnitMbTempStatsAmbientTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 7),
    _CfprComputeRackUnitMbTempStatsAmbientTempMin_Type()
)
cfprComputeRackUnitMbTempStatsAmbientTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsAmbientTempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsFrontTemp_Type = Integer32
_CfprComputeRackUnitMbTempStatsFrontTemp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsFrontTemp = _CfprComputeRackUnitMbTempStatsFrontTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 8),
    _CfprComputeRackUnitMbTempStatsFrontTemp_Type()
)
cfprComputeRackUnitMbTempStatsFrontTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsFrontTemp.setStatus("current")
_CfprComputeRackUnitMbTempStatsFrontTempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsFrontTempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsFrontTempAvg = _CfprComputeRackUnitMbTempStatsFrontTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 9),
    _CfprComputeRackUnitMbTempStatsFrontTempAvg_Type()
)
cfprComputeRackUnitMbTempStatsFrontTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsFrontTempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsFrontTempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsFrontTempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsFrontTempMax = _CfprComputeRackUnitMbTempStatsFrontTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 10),
    _CfprComputeRackUnitMbTempStatsFrontTempMax_Type()
)
cfprComputeRackUnitMbTempStatsFrontTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsFrontTempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsFrontTempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsFrontTempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsFrontTempMin = _CfprComputeRackUnitMbTempStatsFrontTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 11),
    _CfprComputeRackUnitMbTempStatsFrontTempMin_Type()
)
cfprComputeRackUnitMbTempStatsFrontTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsFrontTempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsIntervals_Type = Gauge32
_CfprComputeRackUnitMbTempStatsIntervals_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIntervals = _CfprComputeRackUnitMbTempStatsIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 12),
    _CfprComputeRackUnitMbTempStatsIntervals_Type()
)
cfprComputeRackUnitMbTempStatsIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIntervals.setStatus("current")
_CfprComputeRackUnitMbTempStatsIoh1Temp_Type = Integer32
_CfprComputeRackUnitMbTempStatsIoh1Temp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIoh1Temp = _CfprComputeRackUnitMbTempStatsIoh1Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 13),
    _CfprComputeRackUnitMbTempStatsIoh1Temp_Type()
)
cfprComputeRackUnitMbTempStatsIoh1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIoh1Temp.setStatus("current")
_CfprComputeRackUnitMbTempStatsIoh1TempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsIoh1TempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIoh1TempAvg = _CfprComputeRackUnitMbTempStatsIoh1TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 14),
    _CfprComputeRackUnitMbTempStatsIoh1TempAvg_Type()
)
cfprComputeRackUnitMbTempStatsIoh1TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIoh1TempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsIoh1TempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsIoh1TempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIoh1TempMax = _CfprComputeRackUnitMbTempStatsIoh1TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 15),
    _CfprComputeRackUnitMbTempStatsIoh1TempMax_Type()
)
cfprComputeRackUnitMbTempStatsIoh1TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIoh1TempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsIoh1TempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsIoh1TempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIoh1TempMin = _CfprComputeRackUnitMbTempStatsIoh1TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 16),
    _CfprComputeRackUnitMbTempStatsIoh1TempMin_Type()
)
cfprComputeRackUnitMbTempStatsIoh1TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIoh1TempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsIoh2Temp_Type = Integer32
_CfprComputeRackUnitMbTempStatsIoh2Temp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIoh2Temp = _CfprComputeRackUnitMbTempStatsIoh2Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 17),
    _CfprComputeRackUnitMbTempStatsIoh2Temp_Type()
)
cfprComputeRackUnitMbTempStatsIoh2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIoh2Temp.setStatus("current")
_CfprComputeRackUnitMbTempStatsIoh2TempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsIoh2TempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIoh2TempAvg = _CfprComputeRackUnitMbTempStatsIoh2TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 18),
    _CfprComputeRackUnitMbTempStatsIoh2TempAvg_Type()
)
cfprComputeRackUnitMbTempStatsIoh2TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIoh2TempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsIoh2TempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsIoh2TempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIoh2TempMax = _CfprComputeRackUnitMbTempStatsIoh2TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 19),
    _CfprComputeRackUnitMbTempStatsIoh2TempMax_Type()
)
cfprComputeRackUnitMbTempStatsIoh2TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIoh2TempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsIoh2TempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsIoh2TempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsIoh2TempMin = _CfprComputeRackUnitMbTempStatsIoh2TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 20),
    _CfprComputeRackUnitMbTempStatsIoh2TempMin_Type()
)
cfprComputeRackUnitMbTempStatsIoh2TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsIoh2TempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsRearTemp_Type = Integer32
_CfprComputeRackUnitMbTempStatsRearTemp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsRearTemp = _CfprComputeRackUnitMbTempStatsRearTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 21),
    _CfprComputeRackUnitMbTempStatsRearTemp_Type()
)
cfprComputeRackUnitMbTempStatsRearTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsRearTemp.setStatus("current")
_CfprComputeRackUnitMbTempStatsRearTempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsRearTempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsRearTempAvg = _CfprComputeRackUnitMbTempStatsRearTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 22),
    _CfprComputeRackUnitMbTempStatsRearTempAvg_Type()
)
cfprComputeRackUnitMbTempStatsRearTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsRearTempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsRearTempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsRearTempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsRearTempMax = _CfprComputeRackUnitMbTempStatsRearTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 23),
    _CfprComputeRackUnitMbTempStatsRearTempMax_Type()
)
cfprComputeRackUnitMbTempStatsRearTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsRearTempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsRearTempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsRearTempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsRearTempMin = _CfprComputeRackUnitMbTempStatsRearTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 24),
    _CfprComputeRackUnitMbTempStatsRearTempMin_Type()
)
cfprComputeRackUnitMbTempStatsRearTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsRearTempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsSuspect_Type = TruthValue
_CfprComputeRackUnitMbTempStatsSuspect_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsSuspect = _CfprComputeRackUnitMbTempStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 25),
    _CfprComputeRackUnitMbTempStatsSuspect_Type()
)
cfprComputeRackUnitMbTempStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsSuspect.setStatus("current")
_CfprComputeRackUnitMbTempStatsThresholded_Type = CfprComputeRackUnitMbTempStatsThresholded
_CfprComputeRackUnitMbTempStatsThresholded_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsThresholded = _CfprComputeRackUnitMbTempStatsThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 26),
    _CfprComputeRackUnitMbTempStatsThresholded_Type()
)
cfprComputeRackUnitMbTempStatsThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsThresholded.setStatus("current")
_CfprComputeRackUnitMbTempStatsTimeCollected_Type = DateAndTime
_CfprComputeRackUnitMbTempStatsTimeCollected_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsTimeCollected = _CfprComputeRackUnitMbTempStatsTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 27),
    _CfprComputeRackUnitMbTempStatsTimeCollected_Type()
)
cfprComputeRackUnitMbTempStatsTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsTimeCollected.setStatus("current")
_CfprComputeRackUnitMbTempStatsUpdate_Type = Gauge32
_CfprComputeRackUnitMbTempStatsUpdate_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsUpdate = _CfprComputeRackUnitMbTempStatsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 56, 1, 28),
    _CfprComputeRackUnitMbTempStatsUpdate_Type()
)
cfprComputeRackUnitMbTempStatsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsUpdate.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistTable_Object = MibTable
cfprComputeRackUnitMbTempStatsHistTable = _CfprComputeRackUnitMbTempStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57)
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistTable.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistEntry_Object = MibTableRow
cfprComputeRackUnitMbTempStatsHistEntry = _CfprComputeRackUnitMbTempStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1)
)
cfprComputeRackUnitMbTempStatsHistEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeRackUnitMbTempStatsHistInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistEntry.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistInstanceId_Type = CfprManagedObjectId
_CfprComputeRackUnitMbTempStatsHistInstanceId_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistInstanceId = _CfprComputeRackUnitMbTempStatsHistInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 1),
    _CfprComputeRackUnitMbTempStatsHistInstanceId_Type()
)
cfprComputeRackUnitMbTempStatsHistInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistInstanceId.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistDn_Type = CfprManagedObjectDn
_CfprComputeRackUnitMbTempStatsHistDn_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistDn = _CfprComputeRackUnitMbTempStatsHistDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 2),
    _CfprComputeRackUnitMbTempStatsHistDn_Type()
)
cfprComputeRackUnitMbTempStatsHistDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistDn.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistRn_Type = SnmpAdminString
_CfprComputeRackUnitMbTempStatsHistRn_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistRn = _CfprComputeRackUnitMbTempStatsHistRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 3),
    _CfprComputeRackUnitMbTempStatsHistRn_Type()
)
cfprComputeRackUnitMbTempStatsHistRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistRn.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistAmbientTemp_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistAmbientTemp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistAmbientTemp = _CfprComputeRackUnitMbTempStatsHistAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 4),
    _CfprComputeRackUnitMbTempStatsHistAmbientTemp_Type()
)
cfprComputeRackUnitMbTempStatsHistAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistAmbientTemp.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistAmbientTempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistAmbientTempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistAmbientTempAvg = _CfprComputeRackUnitMbTempStatsHistAmbientTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 5),
    _CfprComputeRackUnitMbTempStatsHistAmbientTempAvg_Type()
)
cfprComputeRackUnitMbTempStatsHistAmbientTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistAmbientTempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistAmbientTempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistAmbientTempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistAmbientTempMax = _CfprComputeRackUnitMbTempStatsHistAmbientTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 6),
    _CfprComputeRackUnitMbTempStatsHistAmbientTempMax_Type()
)
cfprComputeRackUnitMbTempStatsHistAmbientTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistAmbientTempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistAmbientTempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistAmbientTempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistAmbientTempMin = _CfprComputeRackUnitMbTempStatsHistAmbientTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 7),
    _CfprComputeRackUnitMbTempStatsHistAmbientTempMin_Type()
)
cfprComputeRackUnitMbTempStatsHistAmbientTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistAmbientTempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistFrontTemp_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistFrontTemp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistFrontTemp = _CfprComputeRackUnitMbTempStatsHistFrontTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 8),
    _CfprComputeRackUnitMbTempStatsHistFrontTemp_Type()
)
cfprComputeRackUnitMbTempStatsHistFrontTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistFrontTemp.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistFrontTempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistFrontTempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistFrontTempAvg = _CfprComputeRackUnitMbTempStatsHistFrontTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 9),
    _CfprComputeRackUnitMbTempStatsHistFrontTempAvg_Type()
)
cfprComputeRackUnitMbTempStatsHistFrontTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistFrontTempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistFrontTempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistFrontTempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistFrontTempMax = _CfprComputeRackUnitMbTempStatsHistFrontTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 10),
    _CfprComputeRackUnitMbTempStatsHistFrontTempMax_Type()
)
cfprComputeRackUnitMbTempStatsHistFrontTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistFrontTempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistFrontTempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistFrontTempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistFrontTempMin = _CfprComputeRackUnitMbTempStatsHistFrontTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 11),
    _CfprComputeRackUnitMbTempStatsHistFrontTempMin_Type()
)
cfprComputeRackUnitMbTempStatsHistFrontTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistFrontTempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistId_Type = Unsigned64
_CfprComputeRackUnitMbTempStatsHistId_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistId = _CfprComputeRackUnitMbTempStatsHistId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 12),
    _CfprComputeRackUnitMbTempStatsHistId_Type()
)
cfprComputeRackUnitMbTempStatsHistId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistId.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistIoh1Temp_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistIoh1Temp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistIoh1Temp = _CfprComputeRackUnitMbTempStatsHistIoh1Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 13),
    _CfprComputeRackUnitMbTempStatsHistIoh1Temp_Type()
)
cfprComputeRackUnitMbTempStatsHistIoh1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistIoh1Temp.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistIoh1TempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistIoh1TempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistIoh1TempAvg = _CfprComputeRackUnitMbTempStatsHistIoh1TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 14),
    _CfprComputeRackUnitMbTempStatsHistIoh1TempAvg_Type()
)
cfprComputeRackUnitMbTempStatsHistIoh1TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistIoh1TempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistIoh1TempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistIoh1TempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistIoh1TempMax = _CfprComputeRackUnitMbTempStatsHistIoh1TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 15),
    _CfprComputeRackUnitMbTempStatsHistIoh1TempMax_Type()
)
cfprComputeRackUnitMbTempStatsHistIoh1TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistIoh1TempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistIoh1TempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistIoh1TempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistIoh1TempMin = _CfprComputeRackUnitMbTempStatsHistIoh1TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 16),
    _CfprComputeRackUnitMbTempStatsHistIoh1TempMin_Type()
)
cfprComputeRackUnitMbTempStatsHistIoh1TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistIoh1TempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistIoh2Temp_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistIoh2Temp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistIoh2Temp = _CfprComputeRackUnitMbTempStatsHistIoh2Temp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 17),
    _CfprComputeRackUnitMbTempStatsHistIoh2Temp_Type()
)
cfprComputeRackUnitMbTempStatsHistIoh2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistIoh2Temp.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistIoh2TempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistIoh2TempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistIoh2TempAvg = _CfprComputeRackUnitMbTempStatsHistIoh2TempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 18),
    _CfprComputeRackUnitMbTempStatsHistIoh2TempAvg_Type()
)
cfprComputeRackUnitMbTempStatsHistIoh2TempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistIoh2TempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistIoh2TempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistIoh2TempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistIoh2TempMax = _CfprComputeRackUnitMbTempStatsHistIoh2TempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 19),
    _CfprComputeRackUnitMbTempStatsHistIoh2TempMax_Type()
)
cfprComputeRackUnitMbTempStatsHistIoh2TempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistIoh2TempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistIoh2TempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistIoh2TempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistIoh2TempMin = _CfprComputeRackUnitMbTempStatsHistIoh2TempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 20),
    _CfprComputeRackUnitMbTempStatsHistIoh2TempMin_Type()
)
cfprComputeRackUnitMbTempStatsHistIoh2TempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistIoh2TempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistMostRecent_Type = TruthValue
_CfprComputeRackUnitMbTempStatsHistMostRecent_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistMostRecent = _CfprComputeRackUnitMbTempStatsHistMostRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 21),
    _CfprComputeRackUnitMbTempStatsHistMostRecent_Type()
)
cfprComputeRackUnitMbTempStatsHistMostRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistMostRecent.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistRearTemp_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistRearTemp_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistRearTemp = _CfprComputeRackUnitMbTempStatsHistRearTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 22),
    _CfprComputeRackUnitMbTempStatsHistRearTemp_Type()
)
cfprComputeRackUnitMbTempStatsHistRearTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistRearTemp.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistRearTempAvg_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistRearTempAvg_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistRearTempAvg = _CfprComputeRackUnitMbTempStatsHistRearTempAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 23),
    _CfprComputeRackUnitMbTempStatsHistRearTempAvg_Type()
)
cfprComputeRackUnitMbTempStatsHistRearTempAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistRearTempAvg.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistRearTempMax_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistRearTempMax_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistRearTempMax = _CfprComputeRackUnitMbTempStatsHistRearTempMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 24),
    _CfprComputeRackUnitMbTempStatsHistRearTempMax_Type()
)
cfprComputeRackUnitMbTempStatsHistRearTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistRearTempMax.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistRearTempMin_Type = Integer32
_CfprComputeRackUnitMbTempStatsHistRearTempMin_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistRearTempMin = _CfprComputeRackUnitMbTempStatsHistRearTempMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 25),
    _CfprComputeRackUnitMbTempStatsHistRearTempMin_Type()
)
cfprComputeRackUnitMbTempStatsHistRearTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistRearTempMin.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistSuspect_Type = TruthValue
_CfprComputeRackUnitMbTempStatsHistSuspect_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistSuspect = _CfprComputeRackUnitMbTempStatsHistSuspect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 26),
    _CfprComputeRackUnitMbTempStatsHistSuspect_Type()
)
cfprComputeRackUnitMbTempStatsHistSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistSuspect.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistThresholded_Type = CfprComputeRackUnitMbTempStatsHistThresholded
_CfprComputeRackUnitMbTempStatsHistThresholded_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistThresholded = _CfprComputeRackUnitMbTempStatsHistThresholded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 27),
    _CfprComputeRackUnitMbTempStatsHistThresholded_Type()
)
cfprComputeRackUnitMbTempStatsHistThresholded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistThresholded.setStatus("current")
_CfprComputeRackUnitMbTempStatsHistTimeCollected_Type = DateAndTime
_CfprComputeRackUnitMbTempStatsHistTimeCollected_Object = MibTableColumn
cfprComputeRackUnitMbTempStatsHistTimeCollected = _CfprComputeRackUnitMbTempStatsHistTimeCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 57, 1, 28),
    _CfprComputeRackUnitMbTempStatsHistTimeCollected_Type()
)
cfprComputeRackUnitMbTempStatsHistTimeCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRackUnitMbTempStatsHistTimeCollected.setStatus("current")
_CfprComputeRtcBatteryTable_Object = MibTable
cfprComputeRtcBatteryTable = _CfprComputeRtcBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58)
)
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryTable.setStatus("current")
_CfprComputeRtcBatteryEntry_Object = MibTableRow
cfprComputeRtcBatteryEntry = _CfprComputeRtcBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1)
)
cfprComputeRtcBatteryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeRtcBatteryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryEntry.setStatus("current")
_CfprComputeRtcBatteryInstanceId_Type = CfprManagedObjectId
_CfprComputeRtcBatteryInstanceId_Object = MibTableColumn
cfprComputeRtcBatteryInstanceId = _CfprComputeRtcBatteryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 1),
    _CfprComputeRtcBatteryInstanceId_Type()
)
cfprComputeRtcBatteryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryInstanceId.setStatus("current")
_CfprComputeRtcBatteryDn_Type = CfprManagedObjectDn
_CfprComputeRtcBatteryDn_Object = MibTableColumn
cfprComputeRtcBatteryDn = _CfprComputeRtcBatteryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 2),
    _CfprComputeRtcBatteryDn_Type()
)
cfprComputeRtcBatteryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryDn.setStatus("current")
_CfprComputeRtcBatteryRn_Type = SnmpAdminString
_CfprComputeRtcBatteryRn_Object = MibTableColumn
cfprComputeRtcBatteryRn = _CfprComputeRtcBatteryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 3),
    _CfprComputeRtcBatteryRn_Type()
)
cfprComputeRtcBatteryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryRn.setStatus("current")
_CfprComputeRtcBatteryId_Type = Gauge32
_CfprComputeRtcBatteryId_Object = MibTableColumn
cfprComputeRtcBatteryId = _CfprComputeRtcBatteryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 4),
    _CfprComputeRtcBatteryId_Type()
)
cfprComputeRtcBatteryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryId.setStatus("current")
_CfprComputeRtcBatteryLocationDn_Type = SnmpAdminString
_CfprComputeRtcBatteryLocationDn_Object = MibTableColumn
cfprComputeRtcBatteryLocationDn = _CfprComputeRtcBatteryLocationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 5),
    _CfprComputeRtcBatteryLocationDn_Type()
)
cfprComputeRtcBatteryLocationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryLocationDn.setStatus("current")
_CfprComputeRtcBatteryModel_Type = SnmpAdminString
_CfprComputeRtcBatteryModel_Object = MibTableColumn
cfprComputeRtcBatteryModel = _CfprComputeRtcBatteryModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 6),
    _CfprComputeRtcBatteryModel_Type()
)
cfprComputeRtcBatteryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryModel.setStatus("current")
_CfprComputeRtcBatteryOperQualifierReason_Type = SnmpAdminString
_CfprComputeRtcBatteryOperQualifierReason_Object = MibTableColumn
cfprComputeRtcBatteryOperQualifierReason = _CfprComputeRtcBatteryOperQualifierReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 7),
    _CfprComputeRtcBatteryOperQualifierReason_Type()
)
cfprComputeRtcBatteryOperQualifierReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryOperQualifierReason.setStatus("current")
_CfprComputeRtcBatteryOperState_Type = CfprEquipmentOperability
_CfprComputeRtcBatteryOperState_Object = MibTableColumn
cfprComputeRtcBatteryOperState = _CfprComputeRtcBatteryOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 8),
    _CfprComputeRtcBatteryOperState_Type()
)
cfprComputeRtcBatteryOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryOperState.setStatus("current")
_CfprComputeRtcBatteryOperability_Type = CfprEquipmentOperability
_CfprComputeRtcBatteryOperability_Object = MibTableColumn
cfprComputeRtcBatteryOperability = _CfprComputeRtcBatteryOperability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 9),
    _CfprComputeRtcBatteryOperability_Type()
)
cfprComputeRtcBatteryOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryOperability.setStatus("current")
_CfprComputeRtcBatteryPerf_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeRtcBatteryPerf_Object = MibTableColumn
cfprComputeRtcBatteryPerf = _CfprComputeRtcBatteryPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 10),
    _CfprComputeRtcBatteryPerf_Type()
)
cfprComputeRtcBatteryPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryPerf.setStatus("current")
_CfprComputeRtcBatteryPower_Type = CfprEquipmentPowerState
_CfprComputeRtcBatteryPower_Object = MibTableColumn
cfprComputeRtcBatteryPower = _CfprComputeRtcBatteryPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 11),
    _CfprComputeRtcBatteryPower_Type()
)
cfprComputeRtcBatteryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryPower.setStatus("current")
_CfprComputeRtcBatteryPresence_Type = CfprEquipmentPresence
_CfprComputeRtcBatteryPresence_Object = MibTableColumn
cfprComputeRtcBatteryPresence = _CfprComputeRtcBatteryPresence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 12),
    _CfprComputeRtcBatteryPresence_Type()
)
cfprComputeRtcBatteryPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryPresence.setStatus("current")
_CfprComputeRtcBatteryRevision_Type = SnmpAdminString
_CfprComputeRtcBatteryRevision_Object = MibTableColumn
cfprComputeRtcBatteryRevision = _CfprComputeRtcBatteryRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 13),
    _CfprComputeRtcBatteryRevision_Type()
)
cfprComputeRtcBatteryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryRevision.setStatus("current")
_CfprComputeRtcBatterySerial_Type = SnmpAdminString
_CfprComputeRtcBatterySerial_Object = MibTableColumn
cfprComputeRtcBatterySerial = _CfprComputeRtcBatterySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 14),
    _CfprComputeRtcBatterySerial_Type()
)
cfprComputeRtcBatterySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatterySerial.setStatus("current")
_CfprComputeRtcBatteryThermal_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeRtcBatteryThermal_Object = MibTableColumn
cfprComputeRtcBatteryThermal = _CfprComputeRtcBatteryThermal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 15),
    _CfprComputeRtcBatteryThermal_Type()
)
cfprComputeRtcBatteryThermal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryThermal.setStatus("current")
_CfprComputeRtcBatteryVendor_Type = SnmpAdminString
_CfprComputeRtcBatteryVendor_Object = MibTableColumn
cfprComputeRtcBatteryVendor = _CfprComputeRtcBatteryVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 16),
    _CfprComputeRtcBatteryVendor_Type()
)
cfprComputeRtcBatteryVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryVendor.setStatus("current")
_CfprComputeRtcBatteryVoltage_Type = CfprEquipmentSensorThresholdStatus
_CfprComputeRtcBatteryVoltage_Object = MibTableColumn
cfprComputeRtcBatteryVoltage = _CfprComputeRtcBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 58, 1, 17),
    _CfprComputeRtcBatteryVoltage_Type()
)
cfprComputeRtcBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeRtcBatteryVoltage.setStatus("current")
_CfprComputeScrubPolicyTable_Object = MibTable
cfprComputeScrubPolicyTable = _CfprComputeScrubPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59)
)
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyTable.setStatus("current")
_CfprComputeScrubPolicyEntry_Object = MibTableRow
cfprComputeScrubPolicyEntry = _CfprComputeScrubPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1)
)
cfprComputeScrubPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeScrubPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyEntry.setStatus("current")
_CfprComputeScrubPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeScrubPolicyInstanceId_Object = MibTableColumn
cfprComputeScrubPolicyInstanceId = _CfprComputeScrubPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 1),
    _CfprComputeScrubPolicyInstanceId_Type()
)
cfprComputeScrubPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyInstanceId.setStatus("current")
_CfprComputeScrubPolicyDn_Type = CfprManagedObjectDn
_CfprComputeScrubPolicyDn_Object = MibTableColumn
cfprComputeScrubPolicyDn = _CfprComputeScrubPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 2),
    _CfprComputeScrubPolicyDn_Type()
)
cfprComputeScrubPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyDn.setStatus("current")
_CfprComputeScrubPolicyRn_Type = SnmpAdminString
_CfprComputeScrubPolicyRn_Object = MibTableColumn
cfprComputeScrubPolicyRn = _CfprComputeScrubPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 3),
    _CfprComputeScrubPolicyRn_Type()
)
cfprComputeScrubPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyRn.setStatus("current")
_CfprComputeScrubPolicyBiosSettingsScrub_Type = CfprComputeScrubAction
_CfprComputeScrubPolicyBiosSettingsScrub_Object = MibTableColumn
cfprComputeScrubPolicyBiosSettingsScrub = _CfprComputeScrubPolicyBiosSettingsScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 4),
    _CfprComputeScrubPolicyBiosSettingsScrub_Type()
)
cfprComputeScrubPolicyBiosSettingsScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyBiosSettingsScrub.setStatus("current")
_CfprComputeScrubPolicyDescr_Type = SnmpAdminString
_CfprComputeScrubPolicyDescr_Object = MibTableColumn
cfprComputeScrubPolicyDescr = _CfprComputeScrubPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 5),
    _CfprComputeScrubPolicyDescr_Type()
)
cfprComputeScrubPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyDescr.setStatus("current")
_CfprComputeScrubPolicyDiskScrub_Type = CfprComputeScrubAction
_CfprComputeScrubPolicyDiskScrub_Object = MibTableColumn
cfprComputeScrubPolicyDiskScrub = _CfprComputeScrubPolicyDiskScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 6),
    _CfprComputeScrubPolicyDiskScrub_Type()
)
cfprComputeScrubPolicyDiskScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyDiskScrub.setStatus("current")
_CfprComputeScrubPolicyFlexFlashScrub_Type = CfprComputeScrubAction
_CfprComputeScrubPolicyFlexFlashScrub_Object = MibTableColumn
cfprComputeScrubPolicyFlexFlashScrub = _CfprComputeScrubPolicyFlexFlashScrub_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 7),
    _CfprComputeScrubPolicyFlexFlashScrub_Type()
)
cfprComputeScrubPolicyFlexFlashScrub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyFlexFlashScrub.setStatus("current")
_CfprComputeScrubPolicyIntId_Type = SnmpAdminString
_CfprComputeScrubPolicyIntId_Object = MibTableColumn
cfprComputeScrubPolicyIntId = _CfprComputeScrubPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 8),
    _CfprComputeScrubPolicyIntId_Type()
)
cfprComputeScrubPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyIntId.setStatus("current")
_CfprComputeScrubPolicyName_Type = SnmpAdminString
_CfprComputeScrubPolicyName_Object = MibTableColumn
cfprComputeScrubPolicyName = _CfprComputeScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 9),
    _CfprComputeScrubPolicyName_Type()
)
cfprComputeScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyName.setStatus("current")
_CfprComputeScrubPolicyPolicyLevel_Type = Gauge32
_CfprComputeScrubPolicyPolicyLevel_Object = MibTableColumn
cfprComputeScrubPolicyPolicyLevel = _CfprComputeScrubPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 10),
    _CfprComputeScrubPolicyPolicyLevel_Type()
)
cfprComputeScrubPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyPolicyLevel.setStatus("current")
_CfprComputeScrubPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeScrubPolicyPolicyOwner_Object = MibTableColumn
cfprComputeScrubPolicyPolicyOwner = _CfprComputeScrubPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 59, 1, 11),
    _CfprComputeScrubPolicyPolicyOwner_Type()
)
cfprComputeScrubPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeScrubPolicyPolicyOwner.setStatus("current")
_CfprComputeServerDiscPolicyTable_Object = MibTable
cfprComputeServerDiscPolicyTable = _CfprComputeServerDiscPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60)
)
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyTable.setStatus("current")
_CfprComputeServerDiscPolicyEntry_Object = MibTableRow
cfprComputeServerDiscPolicyEntry = _CfprComputeServerDiscPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1)
)
cfprComputeServerDiscPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeServerDiscPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyEntry.setStatus("current")
_CfprComputeServerDiscPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeServerDiscPolicyInstanceId_Object = MibTableColumn
cfprComputeServerDiscPolicyInstanceId = _CfprComputeServerDiscPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 1),
    _CfprComputeServerDiscPolicyInstanceId_Type()
)
cfprComputeServerDiscPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyInstanceId.setStatus("current")
_CfprComputeServerDiscPolicyDn_Type = CfprManagedObjectDn
_CfprComputeServerDiscPolicyDn_Object = MibTableColumn
cfprComputeServerDiscPolicyDn = _CfprComputeServerDiscPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 2),
    _CfprComputeServerDiscPolicyDn_Type()
)
cfprComputeServerDiscPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyDn.setStatus("current")
_CfprComputeServerDiscPolicyRn_Type = SnmpAdminString
_CfprComputeServerDiscPolicyRn_Object = MibTableColumn
cfprComputeServerDiscPolicyRn = _CfprComputeServerDiscPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 3),
    _CfprComputeServerDiscPolicyRn_Type()
)
cfprComputeServerDiscPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyRn.setStatus("current")
_CfprComputeServerDiscPolicyAction_Type = SnmpAdminString
_CfprComputeServerDiscPolicyAction_Object = MibTableColumn
cfprComputeServerDiscPolicyAction = _CfprComputeServerDiscPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 4),
    _CfprComputeServerDiscPolicyAction_Type()
)
cfprComputeServerDiscPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyAction.setStatus("current")
_CfprComputeServerDiscPolicyDescr_Type = SnmpAdminString
_CfprComputeServerDiscPolicyDescr_Object = MibTableColumn
cfprComputeServerDiscPolicyDescr = _CfprComputeServerDiscPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 5),
    _CfprComputeServerDiscPolicyDescr_Type()
)
cfprComputeServerDiscPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyDescr.setStatus("current")
_CfprComputeServerDiscPolicyFsmDescr_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmDescr_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmDescr = _CfprComputeServerDiscPolicyFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 6),
    _CfprComputeServerDiscPolicyFsmDescr_Type()
)
cfprComputeServerDiscPolicyFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmDescr.setStatus("current")
_CfprComputeServerDiscPolicyFsmPrev_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmPrev_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmPrev = _CfprComputeServerDiscPolicyFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 7),
    _CfprComputeServerDiscPolicyFsmPrev_Type()
)
cfprComputeServerDiscPolicyFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmPrev.setStatus("current")
_CfprComputeServerDiscPolicyFsmProgr_Type = Gauge32
_CfprComputeServerDiscPolicyFsmProgr_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmProgr = _CfprComputeServerDiscPolicyFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 8),
    _CfprComputeServerDiscPolicyFsmProgr_Type()
)
cfprComputeServerDiscPolicyFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmProgr.setStatus("current")
_CfprComputeServerDiscPolicyFsmRmtInvErrCode_Type = Gauge32
_CfprComputeServerDiscPolicyFsmRmtInvErrCode_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmRmtInvErrCode = _CfprComputeServerDiscPolicyFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 9),
    _CfprComputeServerDiscPolicyFsmRmtInvErrCode_Type()
)
cfprComputeServerDiscPolicyFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmRmtInvErrCode.setStatus("current")
_CfprComputeServerDiscPolicyFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmRmtInvErrDescr_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmRmtInvErrDescr = _CfprComputeServerDiscPolicyFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 10),
    _CfprComputeServerDiscPolicyFsmRmtInvErrDescr_Type()
)
cfprComputeServerDiscPolicyFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmRmtInvErrDescr.setStatus("current")
_CfprComputeServerDiscPolicyFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprComputeServerDiscPolicyFsmRmtInvRslt_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmRmtInvRslt = _CfprComputeServerDiscPolicyFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 11),
    _CfprComputeServerDiscPolicyFsmRmtInvRslt_Type()
)
cfprComputeServerDiscPolicyFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmRmtInvRslt.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageDescr_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmStageDescr_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageDescr = _CfprComputeServerDiscPolicyFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 12),
    _CfprComputeServerDiscPolicyFsmStageDescr_Type()
)
cfprComputeServerDiscPolicyFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageDescr.setStatus("current")
_CfprComputeServerDiscPolicyFsmStamp_Type = DateAndTime
_CfprComputeServerDiscPolicyFsmStamp_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStamp = _CfprComputeServerDiscPolicyFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 13),
    _CfprComputeServerDiscPolicyFsmStamp_Type()
)
cfprComputeServerDiscPolicyFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStamp.setStatus("current")
_CfprComputeServerDiscPolicyFsmStatus_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmStatus_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStatus = _CfprComputeServerDiscPolicyFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 14),
    _CfprComputeServerDiscPolicyFsmStatus_Type()
)
cfprComputeServerDiscPolicyFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStatus.setStatus("current")
_CfprComputeServerDiscPolicyFsmTry_Type = Gauge32
_CfprComputeServerDiscPolicyFsmTry_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmTry = _CfprComputeServerDiscPolicyFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 15),
    _CfprComputeServerDiscPolicyFsmTry_Type()
)
cfprComputeServerDiscPolicyFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTry.setStatus("current")
_CfprComputeServerDiscPolicyIntId_Type = SnmpAdminString
_CfprComputeServerDiscPolicyIntId_Object = MibTableColumn
cfprComputeServerDiscPolicyIntId = _CfprComputeServerDiscPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 16),
    _CfprComputeServerDiscPolicyIntId_Type()
)
cfprComputeServerDiscPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyIntId.setStatus("current")
_CfprComputeServerDiscPolicyName_Type = SnmpAdminString
_CfprComputeServerDiscPolicyName_Object = MibTableColumn
cfprComputeServerDiscPolicyName = _CfprComputeServerDiscPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 17),
    _CfprComputeServerDiscPolicyName_Type()
)
cfprComputeServerDiscPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyName.setStatus("current")
_CfprComputeServerDiscPolicyPolicyLevel_Type = Gauge32
_CfprComputeServerDiscPolicyPolicyLevel_Object = MibTableColumn
cfprComputeServerDiscPolicyPolicyLevel = _CfprComputeServerDiscPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 18),
    _CfprComputeServerDiscPolicyPolicyLevel_Type()
)
cfprComputeServerDiscPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyPolicyLevel.setStatus("current")
_CfprComputeServerDiscPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeServerDiscPolicyPolicyOwner_Object = MibTableColumn
cfprComputeServerDiscPolicyPolicyOwner = _CfprComputeServerDiscPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 19),
    _CfprComputeServerDiscPolicyPolicyOwner_Type()
)
cfprComputeServerDiscPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyPolicyOwner.setStatus("current")
_CfprComputeServerDiscPolicyQualifier_Type = SnmpAdminString
_CfprComputeServerDiscPolicyQualifier_Object = MibTableColumn
cfprComputeServerDiscPolicyQualifier = _CfprComputeServerDiscPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 20),
    _CfprComputeServerDiscPolicyQualifier_Type()
)
cfprComputeServerDiscPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyQualifier.setStatus("current")
_CfprComputeServerDiscPolicyScrubPolicyName_Type = SnmpAdminString
_CfprComputeServerDiscPolicyScrubPolicyName_Object = MibTableColumn
cfprComputeServerDiscPolicyScrubPolicyName = _CfprComputeServerDiscPolicyScrubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 60, 1, 21),
    _CfprComputeServerDiscPolicyScrubPolicyName_Type()
)
cfprComputeServerDiscPolicyScrubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyScrubPolicyName.setStatus("current")
_CfprComputeServerDiscPolicyFsmTable_Object = MibTable
cfprComputeServerDiscPolicyFsmTable = _CfprComputeServerDiscPolicyFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61)
)
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTable.setStatus("current")
_CfprComputeServerDiscPolicyFsmEntry_Object = MibTableRow
cfprComputeServerDiscPolicyFsmEntry = _CfprComputeServerDiscPolicyFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1)
)
cfprComputeServerDiscPolicyFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeServerDiscPolicyFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmEntry.setStatus("current")
_CfprComputeServerDiscPolicyFsmInstanceId_Type = CfprManagedObjectId
_CfprComputeServerDiscPolicyFsmInstanceId_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmInstanceId = _CfprComputeServerDiscPolicyFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 1),
    _CfprComputeServerDiscPolicyFsmInstanceId_Type()
)
cfprComputeServerDiscPolicyFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmInstanceId.setStatus("current")
_CfprComputeServerDiscPolicyFsmDn_Type = CfprManagedObjectDn
_CfprComputeServerDiscPolicyFsmDn_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmDn = _CfprComputeServerDiscPolicyFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 2),
    _CfprComputeServerDiscPolicyFsmDn_Type()
)
cfprComputeServerDiscPolicyFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmDn.setStatus("current")
_CfprComputeServerDiscPolicyFsmRn_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmRn_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmRn = _CfprComputeServerDiscPolicyFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 3),
    _CfprComputeServerDiscPolicyFsmRn_Type()
)
cfprComputeServerDiscPolicyFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmRn.setStatus("current")
_CfprComputeServerDiscPolicyFsmCompletionTime_Type = DateAndTime
_CfprComputeServerDiscPolicyFsmCompletionTime_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmCompletionTime = _CfprComputeServerDiscPolicyFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 4),
    _CfprComputeServerDiscPolicyFsmCompletionTime_Type()
)
cfprComputeServerDiscPolicyFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmCompletionTime.setStatus("current")
_CfprComputeServerDiscPolicyFsmCurrentFsm_Type = CfprComputeServerDiscPolicyFsmCurrentFsm
_CfprComputeServerDiscPolicyFsmCurrentFsm_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmCurrentFsm = _CfprComputeServerDiscPolicyFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 5),
    _CfprComputeServerDiscPolicyFsmCurrentFsm_Type()
)
cfprComputeServerDiscPolicyFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmCurrentFsm.setStatus("current")
_CfprComputeServerDiscPolicyFsmDescrData_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmDescrData_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmDescrData = _CfprComputeServerDiscPolicyFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 6),
    _CfprComputeServerDiscPolicyFsmDescrData_Type()
)
cfprComputeServerDiscPolicyFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmDescrData.setStatus("current")
_CfprComputeServerDiscPolicyFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprComputeServerDiscPolicyFsmFsmStatus_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmFsmStatus = _CfprComputeServerDiscPolicyFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 7),
    _CfprComputeServerDiscPolicyFsmFsmStatus_Type()
)
cfprComputeServerDiscPolicyFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmFsmStatus.setStatus("current")
_CfprComputeServerDiscPolicyFsmProgress_Type = Gauge32
_CfprComputeServerDiscPolicyFsmProgress_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmProgress = _CfprComputeServerDiscPolicyFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 8),
    _CfprComputeServerDiscPolicyFsmProgress_Type()
)
cfprComputeServerDiscPolicyFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmProgress.setStatus("current")
_CfprComputeServerDiscPolicyFsmRmtErrCode_Type = Gauge32
_CfprComputeServerDiscPolicyFsmRmtErrCode_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmRmtErrCode = _CfprComputeServerDiscPolicyFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 9),
    _CfprComputeServerDiscPolicyFsmRmtErrCode_Type()
)
cfprComputeServerDiscPolicyFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmRmtErrCode.setStatus("current")
_CfprComputeServerDiscPolicyFsmRmtErrDescr_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmRmtErrDescr_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmRmtErrDescr = _CfprComputeServerDiscPolicyFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 10),
    _CfprComputeServerDiscPolicyFsmRmtErrDescr_Type()
)
cfprComputeServerDiscPolicyFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmRmtErrDescr.setStatus("current")
_CfprComputeServerDiscPolicyFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprComputeServerDiscPolicyFsmRmtRslt_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmRmtRslt = _CfprComputeServerDiscPolicyFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 61, 1, 11),
    _CfprComputeServerDiscPolicyFsmRmtRslt_Type()
)
cfprComputeServerDiscPolicyFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmRmtRslt.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageTable_Object = MibTable
cfprComputeServerDiscPolicyFsmStageTable = _CfprComputeServerDiscPolicyFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62)
)
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageTable.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageEntry_Object = MibTableRow
cfprComputeServerDiscPolicyFsmStageEntry = _CfprComputeServerDiscPolicyFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1)
)
cfprComputeServerDiscPolicyFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeServerDiscPolicyFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageEntry.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageInstanceId_Type = CfprManagedObjectId
_CfprComputeServerDiscPolicyFsmStageInstanceId_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageInstanceId = _CfprComputeServerDiscPolicyFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 1),
    _CfprComputeServerDiscPolicyFsmStageInstanceId_Type()
)
cfprComputeServerDiscPolicyFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageInstanceId.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageDn_Type = CfprManagedObjectDn
_CfprComputeServerDiscPolicyFsmStageDn_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageDn = _CfprComputeServerDiscPolicyFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 2),
    _CfprComputeServerDiscPolicyFsmStageDn_Type()
)
cfprComputeServerDiscPolicyFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageDn.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageRn_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmStageRn_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageRn = _CfprComputeServerDiscPolicyFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 3),
    _CfprComputeServerDiscPolicyFsmStageRn_Type()
)
cfprComputeServerDiscPolicyFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageRn.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageDescrData_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmStageDescrData_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageDescrData = _CfprComputeServerDiscPolicyFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 4),
    _CfprComputeServerDiscPolicyFsmStageDescrData_Type()
)
cfprComputeServerDiscPolicyFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageDescrData.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageLastUpdateTime_Type = DateAndTime
_CfprComputeServerDiscPolicyFsmStageLastUpdateTime_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageLastUpdateTime = _CfprComputeServerDiscPolicyFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 5),
    _CfprComputeServerDiscPolicyFsmStageLastUpdateTime_Type()
)
cfprComputeServerDiscPolicyFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageLastUpdateTime.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageName_Type = CfprComputeServerDiscPolicyFsmStageName
_CfprComputeServerDiscPolicyFsmStageName_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageName = _CfprComputeServerDiscPolicyFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 6),
    _CfprComputeServerDiscPolicyFsmStageName_Type()
)
cfprComputeServerDiscPolicyFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageName.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageOrder_Type = Gauge32
_CfprComputeServerDiscPolicyFsmStageOrder_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageOrder = _CfprComputeServerDiscPolicyFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 7),
    _CfprComputeServerDiscPolicyFsmStageOrder_Type()
)
cfprComputeServerDiscPolicyFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageOrder.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageRetry_Type = Gauge32
_CfprComputeServerDiscPolicyFsmStageRetry_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageRetry = _CfprComputeServerDiscPolicyFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 8),
    _CfprComputeServerDiscPolicyFsmStageRetry_Type()
)
cfprComputeServerDiscPolicyFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageRetry.setStatus("current")
_CfprComputeServerDiscPolicyFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprComputeServerDiscPolicyFsmStageStageStatus_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmStageStageStatus = _CfprComputeServerDiscPolicyFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 62, 1, 9),
    _CfprComputeServerDiscPolicyFsmStageStageStatus_Type()
)
cfprComputeServerDiscPolicyFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmStageStageStatus.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskTable_Object = MibTable
cfprComputeServerDiscPolicyFsmTaskTable = _CfprComputeServerDiscPolicyFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63)
)
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskTable.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskEntry_Object = MibTableRow
cfprComputeServerDiscPolicyFsmTaskEntry = _CfprComputeServerDiscPolicyFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63, 1)
)
cfprComputeServerDiscPolicyFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeServerDiscPolicyFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskEntry.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprComputeServerDiscPolicyFsmTaskInstanceId_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmTaskInstanceId = _CfprComputeServerDiscPolicyFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63, 1, 1),
    _CfprComputeServerDiscPolicyFsmTaskInstanceId_Type()
)
cfprComputeServerDiscPolicyFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskInstanceId.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskDn_Type = CfprManagedObjectDn
_CfprComputeServerDiscPolicyFsmTaskDn_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmTaskDn = _CfprComputeServerDiscPolicyFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63, 1, 2),
    _CfprComputeServerDiscPolicyFsmTaskDn_Type()
)
cfprComputeServerDiscPolicyFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskDn.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskRn_Type = SnmpAdminString
_CfprComputeServerDiscPolicyFsmTaskRn_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmTaskRn = _CfprComputeServerDiscPolicyFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63, 1, 3),
    _CfprComputeServerDiscPolicyFsmTaskRn_Type()
)
cfprComputeServerDiscPolicyFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskRn.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskCompletion_Type = CfprFsmCompletion
_CfprComputeServerDiscPolicyFsmTaskCompletion_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmTaskCompletion = _CfprComputeServerDiscPolicyFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63, 1, 4),
    _CfprComputeServerDiscPolicyFsmTaskCompletion_Type()
)
cfprComputeServerDiscPolicyFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskCompletion.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskFlags_Type = CfprFsmFlags
_CfprComputeServerDiscPolicyFsmTaskFlags_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmTaskFlags = _CfprComputeServerDiscPolicyFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63, 1, 5),
    _CfprComputeServerDiscPolicyFsmTaskFlags_Type()
)
cfprComputeServerDiscPolicyFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskFlags.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskItem_Type = CfprComputeServerDiscPolicyFsmTaskItem
_CfprComputeServerDiscPolicyFsmTaskItem_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmTaskItem = _CfprComputeServerDiscPolicyFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63, 1, 6),
    _CfprComputeServerDiscPolicyFsmTaskItem_Type()
)
cfprComputeServerDiscPolicyFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskItem.setStatus("current")
_CfprComputeServerDiscPolicyFsmTaskSeqId_Type = Gauge32
_CfprComputeServerDiscPolicyFsmTaskSeqId_Object = MibTableColumn
cfprComputeServerDiscPolicyFsmTaskSeqId = _CfprComputeServerDiscPolicyFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 63, 1, 7),
    _CfprComputeServerDiscPolicyFsmTaskSeqId_Type()
)
cfprComputeServerDiscPolicyFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerDiscPolicyFsmTaskSeqId.setStatus("current")
_CfprComputeServerMgmtPolicyTable_Object = MibTable
cfprComputeServerMgmtPolicyTable = _CfprComputeServerMgmtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64)
)
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyTable.setStatus("current")
_CfprComputeServerMgmtPolicyEntry_Object = MibTableRow
cfprComputeServerMgmtPolicyEntry = _CfprComputeServerMgmtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1)
)
cfprComputeServerMgmtPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeServerMgmtPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyEntry.setStatus("current")
_CfprComputeServerMgmtPolicyInstanceId_Type = CfprManagedObjectId
_CfprComputeServerMgmtPolicyInstanceId_Object = MibTableColumn
cfprComputeServerMgmtPolicyInstanceId = _CfprComputeServerMgmtPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 1),
    _CfprComputeServerMgmtPolicyInstanceId_Type()
)
cfprComputeServerMgmtPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyInstanceId.setStatus("current")
_CfprComputeServerMgmtPolicyDn_Type = CfprManagedObjectDn
_CfprComputeServerMgmtPolicyDn_Object = MibTableColumn
cfprComputeServerMgmtPolicyDn = _CfprComputeServerMgmtPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 2),
    _CfprComputeServerMgmtPolicyDn_Type()
)
cfprComputeServerMgmtPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyDn.setStatus("current")
_CfprComputeServerMgmtPolicyRn_Type = SnmpAdminString
_CfprComputeServerMgmtPolicyRn_Object = MibTableColumn
cfprComputeServerMgmtPolicyRn = _CfprComputeServerMgmtPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 3),
    _CfprComputeServerMgmtPolicyRn_Type()
)
cfprComputeServerMgmtPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyRn.setStatus("current")
_CfprComputeServerMgmtPolicyAction_Type = CfprComputeServerMgmtDiscAction
_CfprComputeServerMgmtPolicyAction_Object = MibTableColumn
cfprComputeServerMgmtPolicyAction = _CfprComputeServerMgmtPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 4),
    _CfprComputeServerMgmtPolicyAction_Type()
)
cfprComputeServerMgmtPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyAction.setStatus("current")
_CfprComputeServerMgmtPolicyDescr_Type = SnmpAdminString
_CfprComputeServerMgmtPolicyDescr_Object = MibTableColumn
cfprComputeServerMgmtPolicyDescr = _CfprComputeServerMgmtPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 5),
    _CfprComputeServerMgmtPolicyDescr_Type()
)
cfprComputeServerMgmtPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyDescr.setStatus("current")
_CfprComputeServerMgmtPolicyIntId_Type = SnmpAdminString
_CfprComputeServerMgmtPolicyIntId_Object = MibTableColumn
cfprComputeServerMgmtPolicyIntId = _CfprComputeServerMgmtPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 6),
    _CfprComputeServerMgmtPolicyIntId_Type()
)
cfprComputeServerMgmtPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyIntId.setStatus("current")
_CfprComputeServerMgmtPolicyName_Type = SnmpAdminString
_CfprComputeServerMgmtPolicyName_Object = MibTableColumn
cfprComputeServerMgmtPolicyName = _CfprComputeServerMgmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 7),
    _CfprComputeServerMgmtPolicyName_Type()
)
cfprComputeServerMgmtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyName.setStatus("current")
_CfprComputeServerMgmtPolicyPolicyLevel_Type = Gauge32
_CfprComputeServerMgmtPolicyPolicyLevel_Object = MibTableColumn
cfprComputeServerMgmtPolicyPolicyLevel = _CfprComputeServerMgmtPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 8),
    _CfprComputeServerMgmtPolicyPolicyLevel_Type()
)
cfprComputeServerMgmtPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyPolicyLevel.setStatus("current")
_CfprComputeServerMgmtPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprComputeServerMgmtPolicyPolicyOwner_Object = MibTableColumn
cfprComputeServerMgmtPolicyPolicyOwner = _CfprComputeServerMgmtPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 9),
    _CfprComputeServerMgmtPolicyPolicyOwner_Type()
)
cfprComputeServerMgmtPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyPolicyOwner.setStatus("current")
_CfprComputeServerMgmtPolicyQualifier_Type = SnmpAdminString
_CfprComputeServerMgmtPolicyQualifier_Object = MibTableColumn
cfprComputeServerMgmtPolicyQualifier = _CfprComputeServerMgmtPolicyQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 64, 1, 10),
    _CfprComputeServerMgmtPolicyQualifier_Type()
)
cfprComputeServerMgmtPolicyQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeServerMgmtPolicyQualifier.setStatus("current")
_CfprComputeSlotQualTable_Object = MibTable
cfprComputeSlotQualTable = _CfprComputeSlotQualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 65)
)
if mibBuilder.loadTexts:
    cfprComputeSlotQualTable.setStatus("current")
_CfprComputeSlotQualEntry_Object = MibTableRow
cfprComputeSlotQualEntry = _CfprComputeSlotQualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 65, 1)
)
cfprComputeSlotQualEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-COMPUTE-MIB", "cfprComputeSlotQualInstanceId"),
)
if mibBuilder.loadTexts:
    cfprComputeSlotQualEntry.setStatus("current")
_CfprComputeSlotQualInstanceId_Type = CfprManagedObjectId
_CfprComputeSlotQualInstanceId_Object = MibTableColumn
cfprComputeSlotQualInstanceId = _CfprComputeSlotQualInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 65, 1, 1),
    _CfprComputeSlotQualInstanceId_Type()
)
cfprComputeSlotQualInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprComputeSlotQualInstanceId.setStatus("current")
_CfprComputeSlotQualDn_Type = CfprManagedObjectDn
_CfprComputeSlotQualDn_Object = MibTableColumn
cfprComputeSlotQualDn = _CfprComputeSlotQualDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 65, 1, 2),
    _CfprComputeSlotQualDn_Type()
)
cfprComputeSlotQualDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeSlotQualDn.setStatus("current")
_CfprComputeSlotQualRn_Type = SnmpAdminString
_CfprComputeSlotQualRn_Object = MibTableColumn
cfprComputeSlotQualRn = _CfprComputeSlotQualRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 65, 1, 3),
    _CfprComputeSlotQualRn_Type()
)
cfprComputeSlotQualRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeSlotQualRn.setStatus("current")
_CfprComputeSlotQualMaxId_Type = CfprComputeSlotQualMaxId
_CfprComputeSlotQualMaxId_Object = MibTableColumn
cfprComputeSlotQualMaxId = _CfprComputeSlotQualMaxId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 65, 1, 4),
    _CfprComputeSlotQualMaxId_Type()
)
cfprComputeSlotQualMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeSlotQualMaxId.setStatus("current")
_CfprComputeSlotQualMinId_Type = CfprComputeSlotQualMinId
_CfprComputeSlotQualMinId_Object = MibTableColumn
cfprComputeSlotQualMinId = _CfprComputeSlotQualMinId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 12, 65, 1, 5),
    _CfprComputeSlotQualMinId_Type()
)
cfprComputeSlotQualMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprComputeSlotQualMinId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-COMPUTE-MIB",
    **{"cfprComputeObjects": cfprComputeObjects,
       "cfprComputeAutoconfigPolicyTable": cfprComputeAutoconfigPolicyTable,
       "cfprComputeAutoconfigPolicyEntry": cfprComputeAutoconfigPolicyEntry,
       "cfprComputeAutoconfigPolicyInstanceId": cfprComputeAutoconfigPolicyInstanceId,
       "cfprComputeAutoconfigPolicyDn": cfprComputeAutoconfigPolicyDn,
       "cfprComputeAutoconfigPolicyRn": cfprComputeAutoconfigPolicyRn,
       "cfprComputeAutoconfigPolicyDescr": cfprComputeAutoconfigPolicyDescr,
       "cfprComputeAutoconfigPolicyDstDn": cfprComputeAutoconfigPolicyDstDn,
       "cfprComputeAutoconfigPolicyIntId": cfprComputeAutoconfigPolicyIntId,
       "cfprComputeAutoconfigPolicyName": cfprComputeAutoconfigPolicyName,
       "cfprComputeAutoconfigPolicyPolicyLevel": cfprComputeAutoconfigPolicyPolicyLevel,
       "cfprComputeAutoconfigPolicyPolicyOwner": cfprComputeAutoconfigPolicyPolicyOwner,
       "cfprComputeAutoconfigPolicyQualifier": cfprComputeAutoconfigPolicyQualifier,
       "cfprComputeAutoconfigPolicySrcTemplName": cfprComputeAutoconfigPolicySrcTemplName,
       "cfprComputeBladeTable": cfprComputeBladeTable,
       "cfprComputeBladeEntry": cfprComputeBladeEntry,
       "cfprComputeBladeInstanceId": cfprComputeBladeInstanceId,
       "cfprComputeBladeDn": cfprComputeBladeDn,
       "cfprComputeBladeRn": cfprComputeBladeRn,
       "cfprComputeBladeAdminPower": cfprComputeBladeAdminPower,
       "cfprComputeBladeAdminState": cfprComputeBladeAdminState,
       "cfprComputeBladeAssignedToDn": cfprComputeBladeAssignedToDn,
       "cfprComputeBladeAssociation": cfprComputeBladeAssociation,
       "cfprComputeBladeAvailability": cfprComputeBladeAvailability,
       "cfprComputeBladeAvailableMemory": cfprComputeBladeAvailableMemory,
       "cfprComputeBladeChassisId": cfprComputeBladeChassisId,
       "cfprComputeBladeCheckPoint": cfprComputeBladeCheckPoint,
       "cfprComputeBladeConnPath": cfprComputeBladeConnPath,
       "cfprComputeBladeConnStatus": cfprComputeBladeConnStatus,
       "cfprComputeBladeDescr": cfprComputeBladeDescr,
       "cfprComputeBladeDiscovery": cfprComputeBladeDiscovery,
       "cfprComputeBladeFltAggr": cfprComputeBladeFltAggr,
       "cfprComputeBladeFsmDescr": cfprComputeBladeFsmDescr,
       "cfprComputeBladeFsmFlags": cfprComputeBladeFsmFlags,
       "cfprComputeBladeFsmPrev": cfprComputeBladeFsmPrev,
       "cfprComputeBladeFsmProgr": cfprComputeBladeFsmProgr,
       "cfprComputeBladeFsmRmtInvErrCode": cfprComputeBladeFsmRmtInvErrCode,
       "cfprComputeBladeFsmRmtInvErrDescr": cfprComputeBladeFsmRmtInvErrDescr,
       "cfprComputeBladeFsmRmtInvRslt": cfprComputeBladeFsmRmtInvRslt,
       "cfprComputeBladeFsmStageDescr": cfprComputeBladeFsmStageDescr,
       "cfprComputeBladeFsmStamp": cfprComputeBladeFsmStamp,
       "cfprComputeBladeFsmStatus": cfprComputeBladeFsmStatus,
       "cfprComputeBladeFsmTry": cfprComputeBladeFsmTry,
       "cfprComputeBladeIntId": cfprComputeBladeIntId,
       "cfprComputeBladeLc": cfprComputeBladeLc,
       "cfprComputeBladeLcTs": cfprComputeBladeLcTs,
       "cfprComputeBladeLocalId": cfprComputeBladeLocalId,
       "cfprComputeBladeLowVoltageMemory": cfprComputeBladeLowVoltageMemory,
       "cfprComputeBladeManagingInst": cfprComputeBladeManagingInst,
       "cfprComputeBladeMemorySpeed": cfprComputeBladeMemorySpeed,
       "cfprComputeBladeMfgTime": cfprComputeBladeMfgTime,
       "cfprComputeBladeModel": cfprComputeBladeModel,
       "cfprComputeBladeName": cfprComputeBladeName,
       "cfprComputeBladeNumOfAdaptors": cfprComputeBladeNumOfAdaptors,
       "cfprComputeBladeNumOfCores": cfprComputeBladeNumOfCores,
       "cfprComputeBladeNumOfCoresEnabled": cfprComputeBladeNumOfCoresEnabled,
       "cfprComputeBladeNumOfCpus": cfprComputeBladeNumOfCpus,
       "cfprComputeBladeNumOfEthHostIfs": cfprComputeBladeNumOfEthHostIfs,
       "cfprComputeBladeNumOfFcHostIfs": cfprComputeBladeNumOfFcHostIfs,
       "cfprComputeBladeNumOfThreads": cfprComputeBladeNumOfThreads,
       "cfprComputeBladeOperPower": cfprComputeBladeOperPower,
       "cfprComputeBladeOperQualifier": cfprComputeBladeOperQualifier,
       "cfprComputeBladeOperState": cfprComputeBladeOperState,
       "cfprComputeBladeOperability": cfprComputeBladeOperability,
       "cfprComputeBladeOriginalUuid": cfprComputeBladeOriginalUuid,
       "cfprComputeBladePartNumber": cfprComputeBladePartNumber,
       "cfprComputeBladePolicyLevel": cfprComputeBladePolicyLevel,
       "cfprComputeBladePolicyOwner": cfprComputeBladePolicyOwner,
       "cfprComputeBladePresence": cfprComputeBladePresence,
       "cfprComputeBladeRevision": cfprComputeBladeRevision,
       "cfprComputeBladeScaledMode": cfprComputeBladeScaledMode,
       "cfprComputeBladeSerial": cfprComputeBladeSerial,
       "cfprComputeBladeServerId": cfprComputeBladeServerId,
       "cfprComputeBladeSlotId": cfprComputeBladeSlotId,
       "cfprComputeBladeTotalMemory": cfprComputeBladeTotalMemory,
       "cfprComputeBladeUpgradeScenario": cfprComputeBladeUpgradeScenario,
       "cfprComputeBladeUsrLbl": cfprComputeBladeUsrLbl,
       "cfprComputeBladeUuid": cfprComputeBladeUuid,
       "cfprComputeBladeVendor": cfprComputeBladeVendor,
       "cfprComputeBladeVid": cfprComputeBladeVid,
       "cfprComputeBladeLastAdaptorCrashReset": cfprComputeBladeLastAdaptorCrashReset,
       "cfprComputeBladeLastBiosHangReset": cfprComputeBladeLastBiosHangReset,
       "cfprComputeBladeLastCatErrReset": cfprComputeBladeLastCatErrReset,
       "cfprComputeBladePostState": cfprComputeBladePostState,
       "cfprComputeBladePostWaitCount": cfprComputeBladePostWaitCount,
       "cfprComputeBladeResetCatErrCount": cfprComputeBladeResetCatErrCount,
       "cfprComputeBladeResetCount": cfprComputeBladeResetCount,
       "cfprComputeBladeDiscPolicyTable": cfprComputeBladeDiscPolicyTable,
       "cfprComputeBladeDiscPolicyEntry": cfprComputeBladeDiscPolicyEntry,
       "cfprComputeBladeDiscPolicyInstanceId": cfprComputeBladeDiscPolicyInstanceId,
       "cfprComputeBladeDiscPolicyDn": cfprComputeBladeDiscPolicyDn,
       "cfprComputeBladeDiscPolicyRn": cfprComputeBladeDiscPolicyRn,
       "cfprComputeBladeDiscPolicyAction": cfprComputeBladeDiscPolicyAction,
       "cfprComputeBladeDiscPolicyDescr": cfprComputeBladeDiscPolicyDescr,
       "cfprComputeBladeDiscPolicyIntId": cfprComputeBladeDiscPolicyIntId,
       "cfprComputeBladeDiscPolicyName": cfprComputeBladeDiscPolicyName,
       "cfprComputeBladeDiscPolicyPolicyLevel": cfprComputeBladeDiscPolicyPolicyLevel,
       "cfprComputeBladeDiscPolicyPolicyOwner": cfprComputeBladeDiscPolicyPolicyOwner,
       "cfprComputeBladeDiscPolicyQualifier": cfprComputeBladeDiscPolicyQualifier,
       "cfprComputeBladeDiscPolicyScrubPolicyName": cfprComputeBladeDiscPolicyScrubPolicyName,
       "cfprComputeBladeFsmTable": cfprComputeBladeFsmTable,
       "cfprComputeBladeFsmEntry": cfprComputeBladeFsmEntry,
       "cfprComputeBladeFsmInstanceId": cfprComputeBladeFsmInstanceId,
       "cfprComputeBladeFsmDn": cfprComputeBladeFsmDn,
       "cfprComputeBladeFsmRn": cfprComputeBladeFsmRn,
       "cfprComputeBladeFsmCompletionTime": cfprComputeBladeFsmCompletionTime,
       "cfprComputeBladeFsmCurrentFsm": cfprComputeBladeFsmCurrentFsm,
       "cfprComputeBladeFsmDescrData": cfprComputeBladeFsmDescrData,
       "cfprComputeBladeFsmFsmStatus": cfprComputeBladeFsmFsmStatus,
       "cfprComputeBladeFsmProgress": cfprComputeBladeFsmProgress,
       "cfprComputeBladeFsmRmtErrCode": cfprComputeBladeFsmRmtErrCode,
       "cfprComputeBladeFsmRmtErrDescr": cfprComputeBladeFsmRmtErrDescr,
       "cfprComputeBladeFsmRmtRslt": cfprComputeBladeFsmRmtRslt,
       "cfprComputeBladeFsmStageTable": cfprComputeBladeFsmStageTable,
       "cfprComputeBladeFsmStageEntry": cfprComputeBladeFsmStageEntry,
       "cfprComputeBladeFsmStageInstanceId": cfprComputeBladeFsmStageInstanceId,
       "cfprComputeBladeFsmStageDn": cfprComputeBladeFsmStageDn,
       "cfprComputeBladeFsmStageRn": cfprComputeBladeFsmStageRn,
       "cfprComputeBladeFsmStageDescrData": cfprComputeBladeFsmStageDescrData,
       "cfprComputeBladeFsmStageLastUpdateTime": cfprComputeBladeFsmStageLastUpdateTime,
       "cfprComputeBladeFsmStageName": cfprComputeBladeFsmStageName,
       "cfprComputeBladeFsmStageOrder": cfprComputeBladeFsmStageOrder,
       "cfprComputeBladeFsmStageRetry": cfprComputeBladeFsmStageRetry,
       "cfprComputeBladeFsmStageStageStatus": cfprComputeBladeFsmStageStageStatus,
       "cfprComputeBladeFsmTaskTable": cfprComputeBladeFsmTaskTable,
       "cfprComputeBladeFsmTaskEntry": cfprComputeBladeFsmTaskEntry,
       "cfprComputeBladeFsmTaskInstanceId": cfprComputeBladeFsmTaskInstanceId,
       "cfprComputeBladeFsmTaskDn": cfprComputeBladeFsmTaskDn,
       "cfprComputeBladeFsmTaskRn": cfprComputeBladeFsmTaskRn,
       "cfprComputeBladeFsmTaskCompletion": cfprComputeBladeFsmTaskCompletion,
       "cfprComputeBladeFsmTaskFlags": cfprComputeBladeFsmTaskFlags,
       "cfprComputeBladeFsmTaskItem": cfprComputeBladeFsmTaskItem,
       "cfprComputeBladeFsmTaskSeqId": cfprComputeBladeFsmTaskSeqId,
       "cfprComputeBladeInheritPolicyTable": cfprComputeBladeInheritPolicyTable,
       "cfprComputeBladeInheritPolicyEntry": cfprComputeBladeInheritPolicyEntry,
       "cfprComputeBladeInheritPolicyInstanceId": cfprComputeBladeInheritPolicyInstanceId,
       "cfprComputeBladeInheritPolicyDn": cfprComputeBladeInheritPolicyDn,
       "cfprComputeBladeInheritPolicyRn": cfprComputeBladeInheritPolicyRn,
       "cfprComputeBladeInheritPolicyDescr": cfprComputeBladeInheritPolicyDescr,
       "cfprComputeBladeInheritPolicyDstDn": cfprComputeBladeInheritPolicyDstDn,
       "cfprComputeBladeInheritPolicyIntId": cfprComputeBladeInheritPolicyIntId,
       "cfprComputeBladeInheritPolicyName": cfprComputeBladeInheritPolicyName,
       "cfprComputeBladeInheritPolicyPolicyLevel": cfprComputeBladeInheritPolicyPolicyLevel,
       "cfprComputeBladeInheritPolicyPolicyOwner": cfprComputeBladeInheritPolicyPolicyOwner,
       "cfprComputeBladeInheritPolicyQualifier": cfprComputeBladeInheritPolicyQualifier,
       "cfprComputeBoardTable": cfprComputeBoardTable,
       "cfprComputeBoardEntry": cfprComputeBoardEntry,
       "cfprComputeBoardInstanceId": cfprComputeBoardInstanceId,
       "cfprComputeBoardDn": cfprComputeBoardDn,
       "cfprComputeBoardRn": cfprComputeBoardRn,
       "cfprComputeBoardCmosVoltage": cfprComputeBoardCmosVoltage,
       "cfprComputeBoardCpuType": cfprComputeBoardCpuType,
       "cfprComputeBoardFaultQualifier": cfprComputeBoardFaultQualifier,
       "cfprComputeBoardId": cfprComputeBoardId,
       "cfprComputeBoardLocationDn": cfprComputeBoardLocationDn,
       "cfprComputeBoardModel": cfprComputeBoardModel,
       "cfprComputeBoardOperPower": cfprComputeBoardOperPower,
       "cfprComputeBoardOperQualifierReason": cfprComputeBoardOperQualifierReason,
       "cfprComputeBoardOperState": cfprComputeBoardOperState,
       "cfprComputeBoardOperability": cfprComputeBoardOperability,
       "cfprComputeBoardPerf": cfprComputeBoardPerf,
       "cfprComputeBoardPower": cfprComputeBoardPower,
       "cfprComputeBoardPowerUsage": cfprComputeBoardPowerUsage,
       "cfprComputeBoardPresence": cfprComputeBoardPresence,
       "cfprComputeBoardRevision": cfprComputeBoardRevision,
       "cfprComputeBoardSerial": cfprComputeBoardSerial,
       "cfprComputeBoardThermal": cfprComputeBoardThermal,
       "cfprComputeBoardVendor": cfprComputeBoardVendor,
       "cfprComputeBoardVoltage": cfprComputeBoardVoltage,
       "cfprComputeBoardConnectorTable": cfprComputeBoardConnectorTable,
       "cfprComputeBoardConnectorEntry": cfprComputeBoardConnectorEntry,
       "cfprComputeBoardConnectorInstanceId": cfprComputeBoardConnectorInstanceId,
       "cfprComputeBoardConnectorDn": cfprComputeBoardConnectorDn,
       "cfprComputeBoardConnectorRn": cfprComputeBoardConnectorRn,
       "cfprComputeBoardConnectorBoardConnectorType": cfprComputeBoardConnectorBoardConnectorType,
       "cfprComputeBoardConnectorMasterSlotId": cfprComputeBoardConnectorMasterSlotId,
       "cfprComputeBoardConnectorSlaveSlotId": cfprComputeBoardConnectorSlaveSlotId,
       "cfprComputeBoardControllerTable": cfprComputeBoardControllerTable,
       "cfprComputeBoardControllerEntry": cfprComputeBoardControllerEntry,
       "cfprComputeBoardControllerInstanceId": cfprComputeBoardControllerInstanceId,
       "cfprComputeBoardControllerDn": cfprComputeBoardControllerDn,
       "cfprComputeBoardControllerRn": cfprComputeBoardControllerRn,
       "cfprComputeBoardControllerId": cfprComputeBoardControllerId,
       "cfprComputeBoardControllerLocationDn": cfprComputeBoardControllerLocationDn,
       "cfprComputeBoardControllerModel": cfprComputeBoardControllerModel,
       "cfprComputeBoardControllerOperQualifierReason": cfprComputeBoardControllerOperQualifierReason,
       "cfprComputeBoardControllerOperState": cfprComputeBoardControllerOperState,
       "cfprComputeBoardControllerOperability": cfprComputeBoardControllerOperability,
       "cfprComputeBoardControllerPerf": cfprComputeBoardControllerPerf,
       "cfprComputeBoardControllerPower": cfprComputeBoardControllerPower,
       "cfprComputeBoardControllerPresence": cfprComputeBoardControllerPresence,
       "cfprComputeBoardControllerRevision": cfprComputeBoardControllerRevision,
       "cfprComputeBoardControllerSerial": cfprComputeBoardControllerSerial,
       "cfprComputeBoardControllerThermal": cfprComputeBoardControllerThermal,
       "cfprComputeBoardControllerVendor": cfprComputeBoardControllerVendor,
       "cfprComputeBoardControllerVoltage": cfprComputeBoardControllerVoltage,
       "cfprComputeChassisConnPolicyTable": cfprComputeChassisConnPolicyTable,
       "cfprComputeChassisConnPolicyEntry": cfprComputeChassisConnPolicyEntry,
       "cfprComputeChassisConnPolicyInstanceId": cfprComputeChassisConnPolicyInstanceId,
       "cfprComputeChassisConnPolicyDn": cfprComputeChassisConnPolicyDn,
       "cfprComputeChassisConnPolicyRn": cfprComputeChassisConnPolicyRn,
       "cfprComputeChassisConnPolicyAdminState": cfprComputeChassisConnPolicyAdminState,
       "cfprComputeChassisConnPolicyChassisId": cfprComputeChassisConnPolicyChassisId,
       "cfprComputeChassisConnPolicyDescr": cfprComputeChassisConnPolicyDescr,
       "cfprComputeChassisConnPolicyIntId": cfprComputeChassisConnPolicyIntId,
       "cfprComputeChassisConnPolicyName": cfprComputeChassisConnPolicyName,
       "cfprComputeChassisConnPolicyPolicyLevel": cfprComputeChassisConnPolicyPolicyLevel,
       "cfprComputeChassisConnPolicyPolicyOwner": cfprComputeChassisConnPolicyPolicyOwner,
       "cfprComputeChassisConnPolicyQualifier": cfprComputeChassisConnPolicyQualifier,
       "cfprComputeChassisConnPolicySwitchId": cfprComputeChassisConnPolicySwitchId,
       "cfprComputeChassisDiscPolicyTable": cfprComputeChassisDiscPolicyTable,
       "cfprComputeChassisDiscPolicyEntry": cfprComputeChassisDiscPolicyEntry,
       "cfprComputeChassisDiscPolicyInstanceId": cfprComputeChassisDiscPolicyInstanceId,
       "cfprComputeChassisDiscPolicyDn": cfprComputeChassisDiscPolicyDn,
       "cfprComputeChassisDiscPolicyRn": cfprComputeChassisDiscPolicyRn,
       "cfprComputeChassisDiscPolicyAction": cfprComputeChassisDiscPolicyAction,
       "cfprComputeChassisDiscPolicyDescr": cfprComputeChassisDiscPolicyDescr,
       "cfprComputeChassisDiscPolicyIntId": cfprComputeChassisDiscPolicyIntId,
       "cfprComputeChassisDiscPolicyLinkAggregationPref": cfprComputeChassisDiscPolicyLinkAggregationPref,
       "cfprComputeChassisDiscPolicyName": cfprComputeChassisDiscPolicyName,
       "cfprComputeChassisDiscPolicyPolicyLevel": cfprComputeChassisDiscPolicyPolicyLevel,
       "cfprComputeChassisDiscPolicyPolicyOwner": cfprComputeChassisDiscPolicyPolicyOwner,
       "cfprComputeChassisDiscPolicyQualifier": cfprComputeChassisDiscPolicyQualifier,
       "cfprComputeChassisDiscPolicyRebalance": cfprComputeChassisDiscPolicyRebalance,
       "cfprComputeChassisQualTable": cfprComputeChassisQualTable,
       "cfprComputeChassisQualEntry": cfprComputeChassisQualEntry,
       "cfprComputeChassisQualInstanceId": cfprComputeChassisQualInstanceId,
       "cfprComputeChassisQualDn": cfprComputeChassisQualDn,
       "cfprComputeChassisQualRn": cfprComputeChassisQualRn,
       "cfprComputeChassisQualMaxId": cfprComputeChassisQualMaxId,
       "cfprComputeChassisQualMinId": cfprComputeChassisQualMinId,
       "cfprComputeDefaultsTable": cfprComputeDefaultsTable,
       "cfprComputeDefaultsEntry": cfprComputeDefaultsEntry,
       "cfprComputeDefaultsInstanceId": cfprComputeDefaultsInstanceId,
       "cfprComputeDefaultsDn": cfprComputeDefaultsDn,
       "cfprComputeDefaultsRn": cfprComputeDefaultsRn,
       "cfprComputeExtBoardTable": cfprComputeExtBoardTable,
       "cfprComputeExtBoardEntry": cfprComputeExtBoardEntry,
       "cfprComputeExtBoardInstanceId": cfprComputeExtBoardInstanceId,
       "cfprComputeExtBoardDn": cfprComputeExtBoardDn,
       "cfprComputeExtBoardRn": cfprComputeExtBoardRn,
       "cfprComputeExtBoardBoardAggregationRole": cfprComputeExtBoardBoardAggregationRole,
       "cfprComputeExtBoardChassisId": cfprComputeExtBoardChassisId,
       "cfprComputeExtBoardCmosVoltage": cfprComputeExtBoardCmosVoltage,
       "cfprComputeExtBoardConnPath": cfprComputeExtBoardConnPath,
       "cfprComputeExtBoardConnStatus": cfprComputeExtBoardConnStatus,
       "cfprComputeExtBoardFaultQualifier": cfprComputeExtBoardFaultQualifier,
       "cfprComputeExtBoardId": cfprComputeExtBoardId,
       "cfprComputeExtBoardLocationDn": cfprComputeExtBoardLocationDn,
       "cfprComputeExtBoardManagingInst": cfprComputeExtBoardManagingInst,
       "cfprComputeExtBoardModel": cfprComputeExtBoardModel,
       "cfprComputeExtBoardOperPower": cfprComputeExtBoardOperPower,
       "cfprComputeExtBoardOperQualifierReason": cfprComputeExtBoardOperQualifierReason,
       "cfprComputeExtBoardOperState": cfprComputeExtBoardOperState,
       "cfprComputeExtBoardOperability": cfprComputeExtBoardOperability,
       "cfprComputeExtBoardPerf": cfprComputeExtBoardPerf,
       "cfprComputeExtBoardPower": cfprComputeExtBoardPower,
       "cfprComputeExtBoardPowerUsage": cfprComputeExtBoardPowerUsage,
       "cfprComputeExtBoardPresence": cfprComputeExtBoardPresence,
       "cfprComputeExtBoardRevision": cfprComputeExtBoardRevision,
       "cfprComputeExtBoardSerial": cfprComputeExtBoardSerial,
       "cfprComputeExtBoardSlotId": cfprComputeExtBoardSlotId,
       "cfprComputeExtBoardThermal": cfprComputeExtBoardThermal,
       "cfprComputeExtBoardVendor": cfprComputeExtBoardVendor,
       "cfprComputeExtBoardVoltage": cfprComputeExtBoardVoltage,
       "cfprComputeFwSyncAckTable": cfprComputeFwSyncAckTable,
       "cfprComputeFwSyncAckEntry": cfprComputeFwSyncAckEntry,
       "cfprComputeFwSyncAckInstanceId": cfprComputeFwSyncAckInstanceId,
       "cfprComputeFwSyncAckDn": cfprComputeFwSyncAckDn,
       "cfprComputeFwSyncAckRn": cfprComputeFwSyncAckRn,
       "cfprComputeFwSyncAckAcked": cfprComputeFwSyncAckAcked,
       "cfprComputeFwSyncAckAckedBy": cfprComputeFwSyncAckAckedBy,
       "cfprComputeFwSyncAckAdminState": cfprComputeFwSyncAckAdminState,
       "cfprComputeFwSyncAckAutoDelete": cfprComputeFwSyncAckAutoDelete,
       "cfprComputeFwSyncAckChangeBy": cfprComputeFwSyncAckChangeBy,
       "cfprComputeFwSyncAckChangeDetails": cfprComputeFwSyncAckChangeDetails,
       "cfprComputeFwSyncAckChanges": cfprComputeFwSyncAckChanges,
       "cfprComputeFwSyncAckDescr": cfprComputeFwSyncAckDescr,
       "cfprComputeFwSyncAckDisr": cfprComputeFwSyncAckDisr,
       "cfprComputeFwSyncAckIgnoreCap": cfprComputeFwSyncAckIgnoreCap,
       "cfprComputeFwSyncAckIntId": cfprComputeFwSyncAckIntId,
       "cfprComputeFwSyncAckModified": cfprComputeFwSyncAckModified,
       "cfprComputeFwSyncAckName": cfprComputeFwSyncAckName,
       "cfprComputeFwSyncAckOperScheduler": cfprComputeFwSyncAckOperScheduler,
       "cfprComputeFwSyncAckOperState": cfprComputeFwSyncAckOperState,
       "cfprComputeFwSyncAckPolicyLevel": cfprComputeFwSyncAckPolicyLevel,
       "cfprComputeFwSyncAckPolicyOwner": cfprComputeFwSyncAckPolicyOwner,
       "cfprComputeFwSyncAckPrevOperState": cfprComputeFwSyncAckPrevOperState,
       "cfprComputeFwSyncAckScheduler": cfprComputeFwSyncAckScheduler,
       "cfprComputeHealthLedSensorAlarmTable": cfprComputeHealthLedSensorAlarmTable,
       "cfprComputeHealthLedSensorAlarmEntry": cfprComputeHealthLedSensorAlarmEntry,
       "cfprComputeHealthLedSensorAlarmInstanceId": cfprComputeHealthLedSensorAlarmInstanceId,
       "cfprComputeHealthLedSensorAlarmDn": cfprComputeHealthLedSensorAlarmDn,
       "cfprComputeHealthLedSensorAlarmRn": cfprComputeHealthLedSensorAlarmRn,
       "cfprComputeHealthLedSensorAlarmAlarmDesc": cfprComputeHealthLedSensorAlarmAlarmDesc,
       "cfprComputeHealthLedSensorAlarmAlarmSeverity": cfprComputeHealthLedSensorAlarmAlarmSeverity,
       "cfprComputeHealthLedSensorAlarmSensorId": cfprComputeHealthLedSensorAlarmSensorId,
       "cfprComputeHealthLedSensorAlarmSensorName": cfprComputeHealthLedSensorAlarmSensorName,
       "cfprComputeIOHubTable": cfprComputeIOHubTable,
       "cfprComputeIOHubEntry": cfprComputeIOHubEntry,
       "cfprComputeIOHubInstanceId": cfprComputeIOHubInstanceId,
       "cfprComputeIOHubDn": cfprComputeIOHubDn,
       "cfprComputeIOHubRn": cfprComputeIOHubRn,
       "cfprComputeIOHubId": cfprComputeIOHubId,
       "cfprComputeIOHubLocationDn": cfprComputeIOHubLocationDn,
       "cfprComputeIOHubModel": cfprComputeIOHubModel,
       "cfprComputeIOHubOperQualifierReason": cfprComputeIOHubOperQualifierReason,
       "cfprComputeIOHubOperState": cfprComputeIOHubOperState,
       "cfprComputeIOHubOperability": cfprComputeIOHubOperability,
       "cfprComputeIOHubPerf": cfprComputeIOHubPerf,
       "cfprComputeIOHubPower": cfprComputeIOHubPower,
       "cfprComputeIOHubPresence": cfprComputeIOHubPresence,
       "cfprComputeIOHubRevision": cfprComputeIOHubRevision,
       "cfprComputeIOHubSerial": cfprComputeIOHubSerial,
       "cfprComputeIOHubThermal": cfprComputeIOHubThermal,
       "cfprComputeIOHubVendor": cfprComputeIOHubVendor,
       "cfprComputeIOHubVoltage": cfprComputeIOHubVoltage,
       "cfprComputeIOHubEnvStatsTable": cfprComputeIOHubEnvStatsTable,
       "cfprComputeIOHubEnvStatsEntry": cfprComputeIOHubEnvStatsEntry,
       "cfprComputeIOHubEnvStatsInstanceId": cfprComputeIOHubEnvStatsInstanceId,
       "cfprComputeIOHubEnvStatsDn": cfprComputeIOHubEnvStatsDn,
       "cfprComputeIOHubEnvStatsRn": cfprComputeIOHubEnvStatsRn,
       "cfprComputeIOHubEnvStatsIntervals": cfprComputeIOHubEnvStatsIntervals,
       "cfprComputeIOHubEnvStatsSuspect": cfprComputeIOHubEnvStatsSuspect,
       "cfprComputeIOHubEnvStatsTemperature": cfprComputeIOHubEnvStatsTemperature,
       "cfprComputeIOHubEnvStatsTemperatureAvg": cfprComputeIOHubEnvStatsTemperatureAvg,
       "cfprComputeIOHubEnvStatsTemperatureMax": cfprComputeIOHubEnvStatsTemperatureMax,
       "cfprComputeIOHubEnvStatsTemperatureMin": cfprComputeIOHubEnvStatsTemperatureMin,
       "cfprComputeIOHubEnvStatsThresholded": cfprComputeIOHubEnvStatsThresholded,
       "cfprComputeIOHubEnvStatsTimeCollected": cfprComputeIOHubEnvStatsTimeCollected,
       "cfprComputeIOHubEnvStatsUpdate": cfprComputeIOHubEnvStatsUpdate,
       "cfprComputeIOHubEnvStatsHistTable": cfprComputeIOHubEnvStatsHistTable,
       "cfprComputeIOHubEnvStatsHistEntry": cfprComputeIOHubEnvStatsHistEntry,
       "cfprComputeIOHubEnvStatsHistInstanceId": cfprComputeIOHubEnvStatsHistInstanceId,
       "cfprComputeIOHubEnvStatsHistDn": cfprComputeIOHubEnvStatsHistDn,
       "cfprComputeIOHubEnvStatsHistRn": cfprComputeIOHubEnvStatsHistRn,
       "cfprComputeIOHubEnvStatsHistId": cfprComputeIOHubEnvStatsHistId,
       "cfprComputeIOHubEnvStatsHistMostRecent": cfprComputeIOHubEnvStatsHistMostRecent,
       "cfprComputeIOHubEnvStatsHistSuspect": cfprComputeIOHubEnvStatsHistSuspect,
       "cfprComputeIOHubEnvStatsHistTemperature": cfprComputeIOHubEnvStatsHistTemperature,
       "cfprComputeIOHubEnvStatsHistTemperatureAvg": cfprComputeIOHubEnvStatsHistTemperatureAvg,
       "cfprComputeIOHubEnvStatsHistTemperatureMax": cfprComputeIOHubEnvStatsHistTemperatureMax,
       "cfprComputeIOHubEnvStatsHistTemperatureMin": cfprComputeIOHubEnvStatsHistTemperatureMin,
       "cfprComputeIOHubEnvStatsHistThresholded": cfprComputeIOHubEnvStatsHistThresholded,
       "cfprComputeIOHubEnvStatsHistTimeCollected": cfprComputeIOHubEnvStatsHistTimeCollected,
       "cfprComputeKvmMgmtPolicyTable": cfprComputeKvmMgmtPolicyTable,
       "cfprComputeKvmMgmtPolicyEntry": cfprComputeKvmMgmtPolicyEntry,
       "cfprComputeKvmMgmtPolicyInstanceId": cfprComputeKvmMgmtPolicyInstanceId,
       "cfprComputeKvmMgmtPolicyDn": cfprComputeKvmMgmtPolicyDn,
       "cfprComputeKvmMgmtPolicyRn": cfprComputeKvmMgmtPolicyRn,
       "cfprComputeKvmMgmtPolicyDescr": cfprComputeKvmMgmtPolicyDescr,
       "cfprComputeKvmMgmtPolicyIntId": cfprComputeKvmMgmtPolicyIntId,
       "cfprComputeKvmMgmtPolicyName": cfprComputeKvmMgmtPolicyName,
       "cfprComputeKvmMgmtPolicyPolicyLevel": cfprComputeKvmMgmtPolicyPolicyLevel,
       "cfprComputeKvmMgmtPolicyPolicyOwner": cfprComputeKvmMgmtPolicyPolicyOwner,
       "cfprComputeKvmMgmtPolicyVmediaEncryption": cfprComputeKvmMgmtPolicyVmediaEncryption,
       "cfprComputeMbPowerStatsTable": cfprComputeMbPowerStatsTable,
       "cfprComputeMbPowerStatsEntry": cfprComputeMbPowerStatsEntry,
       "cfprComputeMbPowerStatsInstanceId": cfprComputeMbPowerStatsInstanceId,
       "cfprComputeMbPowerStatsDn": cfprComputeMbPowerStatsDn,
       "cfprComputeMbPowerStatsRn": cfprComputeMbPowerStatsRn,
       "cfprComputeMbPowerStatsConsumedPower": cfprComputeMbPowerStatsConsumedPower,
       "cfprComputeMbPowerStatsConsumedPowerAvg": cfprComputeMbPowerStatsConsumedPowerAvg,
       "cfprComputeMbPowerStatsConsumedPowerMax": cfprComputeMbPowerStatsConsumedPowerMax,
       "cfprComputeMbPowerStatsConsumedPowerMin": cfprComputeMbPowerStatsConsumedPowerMin,
       "cfprComputeMbPowerStatsInputCurrent": cfprComputeMbPowerStatsInputCurrent,
       "cfprComputeMbPowerStatsInputCurrentAvg": cfprComputeMbPowerStatsInputCurrentAvg,
       "cfprComputeMbPowerStatsInputCurrentMax": cfprComputeMbPowerStatsInputCurrentMax,
       "cfprComputeMbPowerStatsInputCurrentMin": cfprComputeMbPowerStatsInputCurrentMin,
       "cfprComputeMbPowerStatsInputVoltage": cfprComputeMbPowerStatsInputVoltage,
       "cfprComputeMbPowerStatsInputVoltageAvg": cfprComputeMbPowerStatsInputVoltageAvg,
       "cfprComputeMbPowerStatsInputVoltageMax": cfprComputeMbPowerStatsInputVoltageMax,
       "cfprComputeMbPowerStatsInputVoltageMin": cfprComputeMbPowerStatsInputVoltageMin,
       "cfprComputeMbPowerStatsIntervals": cfprComputeMbPowerStatsIntervals,
       "cfprComputeMbPowerStatsSuspect": cfprComputeMbPowerStatsSuspect,
       "cfprComputeMbPowerStatsThresholded": cfprComputeMbPowerStatsThresholded,
       "cfprComputeMbPowerStatsTimeCollected": cfprComputeMbPowerStatsTimeCollected,
       "cfprComputeMbPowerStatsUpdate": cfprComputeMbPowerStatsUpdate,
       "cfprComputeMbPowerStatsHistTable": cfprComputeMbPowerStatsHistTable,
       "cfprComputeMbPowerStatsHistEntry": cfprComputeMbPowerStatsHistEntry,
       "cfprComputeMbPowerStatsHistInstanceId": cfprComputeMbPowerStatsHistInstanceId,
       "cfprComputeMbPowerStatsHistDn": cfprComputeMbPowerStatsHistDn,
       "cfprComputeMbPowerStatsHistRn": cfprComputeMbPowerStatsHistRn,
       "cfprComputeMbPowerStatsHistConsumedPower": cfprComputeMbPowerStatsHistConsumedPower,
       "cfprComputeMbPowerStatsHistConsumedPowerAvg": cfprComputeMbPowerStatsHistConsumedPowerAvg,
       "cfprComputeMbPowerStatsHistConsumedPowerMax": cfprComputeMbPowerStatsHistConsumedPowerMax,
       "cfprComputeMbPowerStatsHistConsumedPowerMin": cfprComputeMbPowerStatsHistConsumedPowerMin,
       "cfprComputeMbPowerStatsHistId": cfprComputeMbPowerStatsHistId,
       "cfprComputeMbPowerStatsHistInputCurrent": cfprComputeMbPowerStatsHistInputCurrent,
       "cfprComputeMbPowerStatsHistInputCurrentAvg": cfprComputeMbPowerStatsHistInputCurrentAvg,
       "cfprComputeMbPowerStatsHistInputCurrentMax": cfprComputeMbPowerStatsHistInputCurrentMax,
       "cfprComputeMbPowerStatsHistInputCurrentMin": cfprComputeMbPowerStatsHistInputCurrentMin,
       "cfprComputeMbPowerStatsHistInputVoltage": cfprComputeMbPowerStatsHistInputVoltage,
       "cfprComputeMbPowerStatsHistInputVoltageAvg": cfprComputeMbPowerStatsHistInputVoltageAvg,
       "cfprComputeMbPowerStatsHistInputVoltageMax": cfprComputeMbPowerStatsHistInputVoltageMax,
       "cfprComputeMbPowerStatsHistInputVoltageMin": cfprComputeMbPowerStatsHistInputVoltageMin,
       "cfprComputeMbPowerStatsHistMostRecent": cfprComputeMbPowerStatsHistMostRecent,
       "cfprComputeMbPowerStatsHistSuspect": cfprComputeMbPowerStatsHistSuspect,
       "cfprComputeMbPowerStatsHistThresholded": cfprComputeMbPowerStatsHistThresholded,
       "cfprComputeMbPowerStatsHistTimeCollected": cfprComputeMbPowerStatsHistTimeCollected,
       "cfprComputeMbTempStatsTable": cfprComputeMbTempStatsTable,
       "cfprComputeMbTempStatsEntry": cfprComputeMbTempStatsEntry,
       "cfprComputeMbTempStatsInstanceId": cfprComputeMbTempStatsInstanceId,
       "cfprComputeMbTempStatsDn": cfprComputeMbTempStatsDn,
       "cfprComputeMbTempStatsRn": cfprComputeMbTempStatsRn,
       "cfprComputeMbTempStatsFmTempSenIo": cfprComputeMbTempStatsFmTempSenIo,
       "cfprComputeMbTempStatsFmTempSenIoAvg": cfprComputeMbTempStatsFmTempSenIoAvg,
       "cfprComputeMbTempStatsFmTempSenIoMax": cfprComputeMbTempStatsFmTempSenIoMax,
       "cfprComputeMbTempStatsFmTempSenIoMin": cfprComputeMbTempStatsFmTempSenIoMin,
       "cfprComputeMbTempStatsFmTempSenRear": cfprComputeMbTempStatsFmTempSenRear,
       "cfprComputeMbTempStatsFmTempSenRearAvg": cfprComputeMbTempStatsFmTempSenRearAvg,
       "cfprComputeMbTempStatsFmTempSenRearL": cfprComputeMbTempStatsFmTempSenRearL,
       "cfprComputeMbTempStatsFmTempSenRearLAvg": cfprComputeMbTempStatsFmTempSenRearLAvg,
       "cfprComputeMbTempStatsFmTempSenRearLMax": cfprComputeMbTempStatsFmTempSenRearLMax,
       "cfprComputeMbTempStatsFmTempSenRearLMin": cfprComputeMbTempStatsFmTempSenRearLMin,
       "cfprComputeMbTempStatsFmTempSenRearMax": cfprComputeMbTempStatsFmTempSenRearMax,
       "cfprComputeMbTempStatsFmTempSenRearMin": cfprComputeMbTempStatsFmTempSenRearMin,
       "cfprComputeMbTempStatsFmTempSenRearR": cfprComputeMbTempStatsFmTempSenRearR,
       "cfprComputeMbTempStatsFmTempSenRearRAvg": cfprComputeMbTempStatsFmTempSenRearRAvg,
       "cfprComputeMbTempStatsFmTempSenRearRMax": cfprComputeMbTempStatsFmTempSenRearRMax,
       "cfprComputeMbTempStatsFmTempSenRearRMin": cfprComputeMbTempStatsFmTempSenRearRMin,
       "cfprComputeMbTempStatsIntervals": cfprComputeMbTempStatsIntervals,
       "cfprComputeMbTempStatsSuspect": cfprComputeMbTempStatsSuspect,
       "cfprComputeMbTempStatsThresholded": cfprComputeMbTempStatsThresholded,
       "cfprComputeMbTempStatsTimeCollected": cfprComputeMbTempStatsTimeCollected,
       "cfprComputeMbTempStatsUpdate": cfprComputeMbTempStatsUpdate,
       "cfprComputeMbTempStatsHistTable": cfprComputeMbTempStatsHistTable,
       "cfprComputeMbTempStatsHistEntry": cfprComputeMbTempStatsHistEntry,
       "cfprComputeMbTempStatsHistInstanceId": cfprComputeMbTempStatsHistInstanceId,
       "cfprComputeMbTempStatsHistDn": cfprComputeMbTempStatsHistDn,
       "cfprComputeMbTempStatsHistRn": cfprComputeMbTempStatsHistRn,
       "cfprComputeMbTempStatsHistFmTempSenIo": cfprComputeMbTempStatsHistFmTempSenIo,
       "cfprComputeMbTempStatsHistFmTempSenIoAvg": cfprComputeMbTempStatsHistFmTempSenIoAvg,
       "cfprComputeMbTempStatsHistFmTempSenIoMax": cfprComputeMbTempStatsHistFmTempSenIoMax,
       "cfprComputeMbTempStatsHistFmTempSenIoMin": cfprComputeMbTempStatsHistFmTempSenIoMin,
       "cfprComputeMbTempStatsHistFmTempSenRear": cfprComputeMbTempStatsHistFmTempSenRear,
       "cfprComputeMbTempStatsHistFmTempSenRearAvg": cfprComputeMbTempStatsHistFmTempSenRearAvg,
       "cfprComputeMbTempStatsHistFmTempSenRearL": cfprComputeMbTempStatsHistFmTempSenRearL,
       "cfprComputeMbTempStatsHistFmTempSenRearLAvg": cfprComputeMbTempStatsHistFmTempSenRearLAvg,
       "cfprComputeMbTempStatsHistFmTempSenRearLMax": cfprComputeMbTempStatsHistFmTempSenRearLMax,
       "cfprComputeMbTempStatsHistFmTempSenRearLMin": cfprComputeMbTempStatsHistFmTempSenRearLMin,
       "cfprComputeMbTempStatsHistFmTempSenRearMax": cfprComputeMbTempStatsHistFmTempSenRearMax,
       "cfprComputeMbTempStatsHistFmTempSenRearMin": cfprComputeMbTempStatsHistFmTempSenRearMin,
       "cfprComputeMbTempStatsHistFmTempSenRearR": cfprComputeMbTempStatsHistFmTempSenRearR,
       "cfprComputeMbTempStatsHistFmTempSenRearRAvg": cfprComputeMbTempStatsHistFmTempSenRearRAvg,
       "cfprComputeMbTempStatsHistFmTempSenRearRMax": cfprComputeMbTempStatsHistFmTempSenRearRMax,
       "cfprComputeMbTempStatsHistFmTempSenRearRMin": cfprComputeMbTempStatsHistFmTempSenRearRMin,
       "cfprComputeMbTempStatsHistId": cfprComputeMbTempStatsHistId,
       "cfprComputeMbTempStatsHistMostRecent": cfprComputeMbTempStatsHistMostRecent,
       "cfprComputeMbTempStatsHistSuspect": cfprComputeMbTempStatsHistSuspect,
       "cfprComputeMbTempStatsHistThresholded": cfprComputeMbTempStatsHistThresholded,
       "cfprComputeMbTempStatsHistTimeCollected": cfprComputeMbTempStatsHistTimeCollected,
       "cfprComputeMemoryConfigPolicyTable": cfprComputeMemoryConfigPolicyTable,
       "cfprComputeMemoryConfigPolicyEntry": cfprComputeMemoryConfigPolicyEntry,
       "cfprComputeMemoryConfigPolicyInstanceId": cfprComputeMemoryConfigPolicyInstanceId,
       "cfprComputeMemoryConfigPolicyDn": cfprComputeMemoryConfigPolicyDn,
       "cfprComputeMemoryConfigPolicyRn": cfprComputeMemoryConfigPolicyRn,
       "cfprComputeMemoryConfigPolicyBlackListing": cfprComputeMemoryConfigPolicyBlackListing,
       "cfprComputeMemoryConfigPolicyDescr": cfprComputeMemoryConfigPolicyDescr,
       "cfprComputeMemoryConfigPolicyIntId": cfprComputeMemoryConfigPolicyIntId,
       "cfprComputeMemoryConfigPolicyName": cfprComputeMemoryConfigPolicyName,
       "cfprComputeMemoryConfigPolicyPolicyLevel": cfprComputeMemoryConfigPolicyPolicyLevel,
       "cfprComputeMemoryConfigPolicyPolicyOwner": cfprComputeMemoryConfigPolicyPolicyOwner,
       "cfprComputeMemoryConfigurationTable": cfprComputeMemoryConfigurationTable,
       "cfprComputeMemoryConfigurationEntry": cfprComputeMemoryConfigurationEntry,
       "cfprComputeMemoryConfigurationInstanceId": cfprComputeMemoryConfigurationInstanceId,
       "cfprComputeMemoryConfigurationDn": cfprComputeMemoryConfigurationDn,
       "cfprComputeMemoryConfigurationRn": cfprComputeMemoryConfigurationRn,
       "cfprComputeMemoryConfigurationAdminMemoryState": cfprComputeMemoryConfigurationAdminMemoryState,
       "cfprComputeMemoryConfigurationBlackListing": cfprComputeMemoryConfigurationBlackListing,
       "cfprComputeMemoryUnitConstraintDefTable": cfprComputeMemoryUnitConstraintDefTable,
       "cfprComputeMemoryUnitConstraintDefEntry": cfprComputeMemoryUnitConstraintDefEntry,
       "cfprComputeMemoryUnitConstraintDefInstanceId": cfprComputeMemoryUnitConstraintDefInstanceId,
       "cfprComputeMemoryUnitConstraintDefDn": cfprComputeMemoryUnitConstraintDefDn,
       "cfprComputeMemoryUnitConstraintDefRn": cfprComputeMemoryUnitConstraintDefRn,
       "cfprComputeMemoryUnitConstraintDefDescr": cfprComputeMemoryUnitConstraintDefDescr,
       "cfprComputeMemoryUnitConstraintDefIntId": cfprComputeMemoryUnitConstraintDefIntId,
       "cfprComputeMemoryUnitConstraintDefName": cfprComputeMemoryUnitConstraintDefName,
       "cfprComputeMemoryUnitConstraintDefPolicyLevel": cfprComputeMemoryUnitConstraintDefPolicyLevel,
       "cfprComputeMemoryUnitConstraintDefPolicyOwner": cfprComputeMemoryUnitConstraintDefPolicyOwner,
       "cfprComputeMemoryUnitConstraintDefRevisionModifier": cfprComputeMemoryUnitConstraintDefRevisionModifier,
       "cfprComputeMemoryUnitConstraintDefType": cfprComputeMemoryUnitConstraintDefType,
       "cfprComputePCIeFatalCompletionStatsTable": cfprComputePCIeFatalCompletionStatsTable,
       "cfprComputePCIeFatalCompletionStatsEntry": cfprComputePCIeFatalCompletionStatsEntry,
       "cfprComputePCIeFatalCompletionStatsInstanceId": cfprComputePCIeFatalCompletionStatsInstanceId,
       "cfprComputePCIeFatalCompletionStatsDn": cfprComputePCIeFatalCompletionStatsDn,
       "cfprComputePCIeFatalCompletionStatsRn": cfprComputePCIeFatalCompletionStatsRn,
       "cfprComputePCIeFatalCompletionStatsAbortErrors": cfprComputePCIeFatalCompletionStatsAbortErrors,
       "cfprComputePCIeFatalCompletionStatsAbortErrors15Min": cfprComputePCIeFatalCompletionStatsAbortErrors15Min,
       "cfprComputePCIeFatalCompletionStatsAbortErrors15MinH": cfprComputePCIeFatalCompletionStatsAbortErrors15MinH,
       "cfprComputePCIeFatalCompletionStatsAbortErrors1Day": cfprComputePCIeFatalCompletionStatsAbortErrors1Day,
       "cfprComputePCIeFatalCompletionStatsAbortErrors1DayH": cfprComputePCIeFatalCompletionStatsAbortErrors1DayH,
       "cfprComputePCIeFatalCompletionStatsAbortErrors1Hour": cfprComputePCIeFatalCompletionStatsAbortErrors1Hour,
       "cfprComputePCIeFatalCompletionStatsAbortErrors1HourH": cfprComputePCIeFatalCompletionStatsAbortErrors1HourH,
       "cfprComputePCIeFatalCompletionStatsAbortErrors1Week": cfprComputePCIeFatalCompletionStatsAbortErrors1Week,
       "cfprComputePCIeFatalCompletionStatsAbortErrors1WeekH": cfprComputePCIeFatalCompletionStatsAbortErrors1WeekH,
       "cfprComputePCIeFatalCompletionStatsAbortErrors2Weeks": cfprComputePCIeFatalCompletionStatsAbortErrors2Weeks,
       "cfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH": cfprComputePCIeFatalCompletionStatsAbortErrors2WeeksH,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors": cfprComputePCIeFatalCompletionStatsTimeoutErrors,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors15Min": cfprComputePCIeFatalCompletionStatsTimeoutErrors15Min,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH": cfprComputePCIeFatalCompletionStatsTimeoutErrors15MinH,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors1Day": cfprComputePCIeFatalCompletionStatsTimeoutErrors1Day,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH": cfprComputePCIeFatalCompletionStatsTimeoutErrors1DayH,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour": cfprComputePCIeFatalCompletionStatsTimeoutErrors1Hour,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH": cfprComputePCIeFatalCompletionStatsTimeoutErrors1HourH,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors1Week": cfprComputePCIeFatalCompletionStatsTimeoutErrors1Week,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH": cfprComputePCIeFatalCompletionStatsTimeoutErrors1WeekH,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks": cfprComputePCIeFatalCompletionStatsTimeoutErrors2Weeks,
       "cfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH": cfprComputePCIeFatalCompletionStatsTimeoutErrors2WeeksH,
       "cfprComputePCIeFatalCompletionStatsIntervals": cfprComputePCIeFatalCompletionStatsIntervals,
       "cfprComputePCIeFatalCompletionStatsSuspect": cfprComputePCIeFatalCompletionStatsSuspect,
       "cfprComputePCIeFatalCompletionStatsThresholded": cfprComputePCIeFatalCompletionStatsThresholded,
       "cfprComputePCIeFatalCompletionStatsTimeCollected": cfprComputePCIeFatalCompletionStatsTimeCollected,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors": cfprComputePCIeFatalCompletionStatsUnexpectedErrors,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min": cfprComputePCIeFatalCompletionStatsUnexpectedErrors15Min,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH": cfprComputePCIeFatalCompletionStatsUnexpectedErrors15MinH,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day": cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Day,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH": cfprComputePCIeFatalCompletionStatsUnexpectedErrors1DayH,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour": cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Hour,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH": cfprComputePCIeFatalCompletionStatsUnexpectedErrors1HourH,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week": cfprComputePCIeFatalCompletionStatsUnexpectedErrors1Week,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH": cfprComputePCIeFatalCompletionStatsUnexpectedErrors1WeekH,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks": cfprComputePCIeFatalCompletionStatsUnexpectedErrors2Weeks,
       "cfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH": cfprComputePCIeFatalCompletionStatsUnexpectedErrors2WeeksH,
       "cfprComputePCIeFatalCompletionStatsUpdate": cfprComputePCIeFatalCompletionStatsUpdate,
       "cfprComputePCIeFatalProtocolStatsTable": cfprComputePCIeFatalProtocolStatsTable,
       "cfprComputePCIeFatalProtocolStatsEntry": cfprComputePCIeFatalProtocolStatsEntry,
       "cfprComputePCIeFatalProtocolStatsInstanceId": cfprComputePCIeFatalProtocolStatsInstanceId,
       "cfprComputePCIeFatalProtocolStatsDn": cfprComputePCIeFatalProtocolStatsDn,
       "cfprComputePCIeFatalProtocolStatsRn": cfprComputePCIeFatalProtocolStatsRn,
       "cfprComputePCIeFatalProtocolStatsDllpErrors": cfprComputePCIeFatalProtocolStatsDllpErrors,
       "cfprComputePCIeFatalProtocolStatsDllpErrors15Min": cfprComputePCIeFatalProtocolStatsDllpErrors15Min,
       "cfprComputePCIeFatalProtocolStatsDllpErrors15MinH": cfprComputePCIeFatalProtocolStatsDllpErrors15MinH,
       "cfprComputePCIeFatalProtocolStatsDllpErrors1Day": cfprComputePCIeFatalProtocolStatsDllpErrors1Day,
       "cfprComputePCIeFatalProtocolStatsDllpErrors1DayH": cfprComputePCIeFatalProtocolStatsDllpErrors1DayH,
       "cfprComputePCIeFatalProtocolStatsDllpErrors1Hour": cfprComputePCIeFatalProtocolStatsDllpErrors1Hour,
       "cfprComputePCIeFatalProtocolStatsDllpErrors1HourH": cfprComputePCIeFatalProtocolStatsDllpErrors1HourH,
       "cfprComputePCIeFatalProtocolStatsDllpErrors1Week": cfprComputePCIeFatalProtocolStatsDllpErrors1Week,
       "cfprComputePCIeFatalProtocolStatsDllpErrors1WeekH": cfprComputePCIeFatalProtocolStatsDllpErrors1WeekH,
       "cfprComputePCIeFatalProtocolStatsDllpErrors2Weeks": cfprComputePCIeFatalProtocolStatsDllpErrors2Weeks,
       "cfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH": cfprComputePCIeFatalProtocolStatsDllpErrors2WeeksH,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors": cfprComputePCIeFatalProtocolStatsFlowControlErrors,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors15Min": cfprComputePCIeFatalProtocolStatsFlowControlErrors15Min,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH": cfprComputePCIeFatalProtocolStatsFlowControlErrors15MinH,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors1Day": cfprComputePCIeFatalProtocolStatsFlowControlErrors1Day,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH": cfprComputePCIeFatalProtocolStatsFlowControlErrors1DayH,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour": cfprComputePCIeFatalProtocolStatsFlowControlErrors1Hour,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH": cfprComputePCIeFatalProtocolStatsFlowControlErrors1HourH,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors1Week": cfprComputePCIeFatalProtocolStatsFlowControlErrors1Week,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH": cfprComputePCIeFatalProtocolStatsFlowControlErrors1WeekH,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks": cfprComputePCIeFatalProtocolStatsFlowControlErrors2Weeks,
       "cfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH": cfprComputePCIeFatalProtocolStatsFlowControlErrors2WeeksH,
       "cfprComputePCIeFatalProtocolStatsIntervals": cfprComputePCIeFatalProtocolStatsIntervals,
       "cfprComputePCIeFatalProtocolStatsSuspect": cfprComputePCIeFatalProtocolStatsSuspect,
       "cfprComputePCIeFatalProtocolStatsThresholded": cfprComputePCIeFatalProtocolStatsThresholded,
       "cfprComputePCIeFatalProtocolStatsTimeCollected": cfprComputePCIeFatalProtocolStatsTimeCollected,
       "cfprComputePCIeFatalProtocolStatsUpdate": cfprComputePCIeFatalProtocolStatsUpdate,
       "cfprComputePCIeFatalReceiveStatsTable": cfprComputePCIeFatalReceiveStatsTable,
       "cfprComputePCIeFatalReceiveStatsEntry": cfprComputePCIeFatalReceiveStatsEntry,
       "cfprComputePCIeFatalReceiveStatsInstanceId": cfprComputePCIeFatalReceiveStatsInstanceId,
       "cfprComputePCIeFatalReceiveStatsDn": cfprComputePCIeFatalReceiveStatsDn,
       "cfprComputePCIeFatalReceiveStatsRn": cfprComputePCIeFatalReceiveStatsRn,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15Min,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors15MinH,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Day,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1DayH,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Hour,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1HourH,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1Week,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors1WeekH,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2Weeks,
       "cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH": cfprComputePCIeFatalReceiveStatsBufferOverflowErrors2WeeksH,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors": cfprComputePCIeFatalReceiveStatsErrFatalErrors,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors15Min": cfprComputePCIeFatalReceiveStatsErrFatalErrors15Min,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH": cfprComputePCIeFatalReceiveStatsErrFatalErrors15MinH,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors1Day": cfprComputePCIeFatalReceiveStatsErrFatalErrors1Day,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH": cfprComputePCIeFatalReceiveStatsErrFatalErrors1DayH,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour": cfprComputePCIeFatalReceiveStatsErrFatalErrors1Hour,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH": cfprComputePCIeFatalReceiveStatsErrFatalErrors1HourH,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors1Week": cfprComputePCIeFatalReceiveStatsErrFatalErrors1Week,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH": cfprComputePCIeFatalReceiveStatsErrFatalErrors1WeekH,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks": cfprComputePCIeFatalReceiveStatsErrFatalErrors2Weeks,
       "cfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH": cfprComputePCIeFatalReceiveStatsErrFatalErrors2WeeksH,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15Min,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors15MinH,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Day,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1DayH,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Hour,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1HourH,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1Week,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors1WeekH,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2Weeks,
       "cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH": cfprComputePCIeFatalReceiveStatsErrNonFatalErrors2WeeksH,
       "cfprComputePCIeFatalReceiveStatsIntervals": cfprComputePCIeFatalReceiveStatsIntervals,
       "cfprComputePCIeFatalReceiveStatsSuspect": cfprComputePCIeFatalReceiveStatsSuspect,
       "cfprComputePCIeFatalReceiveStatsThresholded": cfprComputePCIeFatalReceiveStatsThresholded,
       "cfprComputePCIeFatalReceiveStatsTimeCollected": cfprComputePCIeFatalReceiveStatsTimeCollected,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15Min,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors15MinH,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Day,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1DayH,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Hour,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1HourH,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1Week,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors1WeekH,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2Weeks,
       "cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH": cfprComputePCIeFatalReceiveStatsUnsupportedRequestErrors2WeeksH,
       "cfprComputePCIeFatalReceiveStatsUpdate": cfprComputePCIeFatalReceiveStatsUpdate,
       "cfprComputePCIeFatalStatsTable": cfprComputePCIeFatalStatsTable,
       "cfprComputePCIeFatalStatsEntry": cfprComputePCIeFatalStatsEntry,
       "cfprComputePCIeFatalStatsInstanceId": cfprComputePCIeFatalStatsInstanceId,
       "cfprComputePCIeFatalStatsDn": cfprComputePCIeFatalStatsDn,
       "cfprComputePCIeFatalStatsRn": cfprComputePCIeFatalStatsRn,
       "cfprComputePCIeFatalStatsAcsViolationErrors": cfprComputePCIeFatalStatsAcsViolationErrors,
       "cfprComputePCIeFatalStatsAcsViolationErrors15Min": cfprComputePCIeFatalStatsAcsViolationErrors15Min,
       "cfprComputePCIeFatalStatsAcsViolationErrors15MinH": cfprComputePCIeFatalStatsAcsViolationErrors15MinH,
       "cfprComputePCIeFatalStatsAcsViolationErrors1Day": cfprComputePCIeFatalStatsAcsViolationErrors1Day,
       "cfprComputePCIeFatalStatsAcsViolationErrors1DayH": cfprComputePCIeFatalStatsAcsViolationErrors1DayH,
       "cfprComputePCIeFatalStatsAcsViolationErrors1Hour": cfprComputePCIeFatalStatsAcsViolationErrors1Hour,
       "cfprComputePCIeFatalStatsAcsViolationErrors1HourH": cfprComputePCIeFatalStatsAcsViolationErrors1HourH,
       "cfprComputePCIeFatalStatsAcsViolationErrors1Week": cfprComputePCIeFatalStatsAcsViolationErrors1Week,
       "cfprComputePCIeFatalStatsAcsViolationErrors1WeekH": cfprComputePCIeFatalStatsAcsViolationErrors1WeekH,
       "cfprComputePCIeFatalStatsAcsViolationErrors2Weeks": cfprComputePCIeFatalStatsAcsViolationErrors2Weeks,
       "cfprComputePCIeFatalStatsAcsViolationErrors2WeeksH": cfprComputePCIeFatalStatsAcsViolationErrors2WeeksH,
       "cfprComputePCIeFatalStatsIntervals": cfprComputePCIeFatalStatsIntervals,
       "cfprComputePCIeFatalStatsMalformedTLPErrors": cfprComputePCIeFatalStatsMalformedTLPErrors,
       "cfprComputePCIeFatalStatsMalformedTLPErrors15Min": cfprComputePCIeFatalStatsMalformedTLPErrors15Min,
       "cfprComputePCIeFatalStatsMalformedTLPErrors15MinH": cfprComputePCIeFatalStatsMalformedTLPErrors15MinH,
       "cfprComputePCIeFatalStatsMalformedTLPErrors1Day": cfprComputePCIeFatalStatsMalformedTLPErrors1Day,
       "cfprComputePCIeFatalStatsMalformedTLPErrors1DayH": cfprComputePCIeFatalStatsMalformedTLPErrors1DayH,
       "cfprComputePCIeFatalStatsMalformedTLPErrors1Hour": cfprComputePCIeFatalStatsMalformedTLPErrors1Hour,
       "cfprComputePCIeFatalStatsMalformedTLPErrors1HourH": cfprComputePCIeFatalStatsMalformedTLPErrors1HourH,
       "cfprComputePCIeFatalStatsMalformedTLPErrors1Week": cfprComputePCIeFatalStatsMalformedTLPErrors1Week,
       "cfprComputePCIeFatalStatsMalformedTLPErrors1WeekH": cfprComputePCIeFatalStatsMalformedTLPErrors1WeekH,
       "cfprComputePCIeFatalStatsMalformedTLPErrors2Weeks": cfprComputePCIeFatalStatsMalformedTLPErrors2Weeks,
       "cfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH": cfprComputePCIeFatalStatsMalformedTLPErrors2WeeksH,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors": cfprComputePCIeFatalStatsPoisonedTLPErrors,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors15Min": cfprComputePCIeFatalStatsPoisonedTLPErrors15Min,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors15MinH": cfprComputePCIeFatalStatsPoisonedTLPErrors15MinH,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors1Day": cfprComputePCIeFatalStatsPoisonedTLPErrors1Day,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors1DayH": cfprComputePCIeFatalStatsPoisonedTLPErrors1DayH,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors1Hour": cfprComputePCIeFatalStatsPoisonedTLPErrors1Hour,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors1HourH": cfprComputePCIeFatalStatsPoisonedTLPErrors1HourH,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors1Week": cfprComputePCIeFatalStatsPoisonedTLPErrors1Week,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH": cfprComputePCIeFatalStatsPoisonedTLPErrors1WeekH,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks": cfprComputePCIeFatalStatsPoisonedTLPErrors2Weeks,
       "cfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH": cfprComputePCIeFatalStatsPoisonedTLPErrors2WeeksH,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors": cfprComputePCIeFatalStatsSurpriseLinkDownErrors,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min": cfprComputePCIeFatalStatsSurpriseLinkDownErrors15Min,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH": cfprComputePCIeFatalStatsSurpriseLinkDownErrors15MinH,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day": cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Day,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH": cfprComputePCIeFatalStatsSurpriseLinkDownErrors1DayH,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour": cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Hour,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH": cfprComputePCIeFatalStatsSurpriseLinkDownErrors1HourH,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week": cfprComputePCIeFatalStatsSurpriseLinkDownErrors1Week,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH": cfprComputePCIeFatalStatsSurpriseLinkDownErrors1WeekH,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks": cfprComputePCIeFatalStatsSurpriseLinkDownErrors2Weeks,
       "cfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH": cfprComputePCIeFatalStatsSurpriseLinkDownErrors2WeeksH,
       "cfprComputePCIeFatalStatsSuspect": cfprComputePCIeFatalStatsSuspect,
       "cfprComputePCIeFatalStatsThresholded": cfprComputePCIeFatalStatsThresholded,
       "cfprComputePCIeFatalStatsTimeCollected": cfprComputePCIeFatalStatsTimeCollected,
       "cfprComputePCIeFatalStatsUpdate": cfprComputePCIeFatalStatsUpdate,
       "cfprComputePciCapTable": cfprComputePciCapTable,
       "cfprComputePciCapEntry": cfprComputePciCapEntry,
       "cfprComputePciCapInstanceId": cfprComputePciCapInstanceId,
       "cfprComputePciCapDn": cfprComputePciCapDn,
       "cfprComputePciCapRn": cfprComputePciCapRn,
       "cfprComputePciCapMaxBusIdPerSlot": cfprComputePciCapMaxBusIdPerSlot,
       "cfprComputePciCapNumOfPhysSlots": cfprComputePciCapNumOfPhysSlots,
       "cfprComputePciCapOrder": cfprComputePciCapOrder,
       "cfprComputePciCapStartsWith": cfprComputePciCapStartsWith,
       "cfprComputePciSlotScanDefTable": cfprComputePciSlotScanDefTable,
       "cfprComputePciSlotScanDefEntry": cfprComputePciSlotScanDefEntry,
       "cfprComputePciSlotScanDefInstanceId": cfprComputePciSlotScanDefInstanceId,
       "cfprComputePciSlotScanDefDn": cfprComputePciSlotScanDefDn,
       "cfprComputePciSlotScanDefRn": cfprComputePciSlotScanDefRn,
       "cfprComputePciSlotScanDefDescr": cfprComputePciSlotScanDefDescr,
       "cfprComputePciSlotScanDefIntId": cfprComputePciSlotScanDefIntId,
       "cfprComputePciSlotScanDefName": cfprComputePciSlotScanDefName,
       "cfprComputePciSlotScanDefPolicyLevel": cfprComputePciSlotScanDefPolicyLevel,
       "cfprComputePciSlotScanDefPolicyOwner": cfprComputePciSlotScanDefPolicyOwner,
       "cfprComputePciSlotScanDefScanOrder": cfprComputePciSlotScanDefScanOrder,
       "cfprComputePciSlotScanDefSlotId": cfprComputePciSlotScanDefSlotId,
       "cfprComputePhysicalAssocCtxTable": cfprComputePhysicalAssocCtxTable,
       "cfprComputePhysicalAssocCtxEntry": cfprComputePhysicalAssocCtxEntry,
       "cfprComputePhysicalAssocCtxInstanceId": cfprComputePhysicalAssocCtxInstanceId,
       "cfprComputePhysicalAssocCtxDn": cfprComputePhysicalAssocCtxDn,
       "cfprComputePhysicalAssocCtxRn": cfprComputePhysicalAssocCtxRn,
       "cfprComputePhysicalAssocCtxFruCapDn": cfprComputePhysicalAssocCtxFruCapDn,
       "cfprComputePhysicalFsmTable": cfprComputePhysicalFsmTable,
       "cfprComputePhysicalFsmEntry": cfprComputePhysicalFsmEntry,
       "cfprComputePhysicalFsmInstanceId": cfprComputePhysicalFsmInstanceId,
       "cfprComputePhysicalFsmDn": cfprComputePhysicalFsmDn,
       "cfprComputePhysicalFsmRn": cfprComputePhysicalFsmRn,
       "cfprComputePhysicalFsmCompletionTime": cfprComputePhysicalFsmCompletionTime,
       "cfprComputePhysicalFsmCurrentFsm": cfprComputePhysicalFsmCurrentFsm,
       "cfprComputePhysicalFsmDescr": cfprComputePhysicalFsmDescr,
       "cfprComputePhysicalFsmFsmStatus": cfprComputePhysicalFsmFsmStatus,
       "cfprComputePhysicalFsmProgress": cfprComputePhysicalFsmProgress,
       "cfprComputePhysicalFsmRmtErrCode": cfprComputePhysicalFsmRmtErrCode,
       "cfprComputePhysicalFsmRmtErrDescr": cfprComputePhysicalFsmRmtErrDescr,
       "cfprComputePhysicalFsmRmtRslt": cfprComputePhysicalFsmRmtRslt,
       "cfprComputePhysicalFsmStageTable": cfprComputePhysicalFsmStageTable,
       "cfprComputePhysicalFsmStageEntry": cfprComputePhysicalFsmStageEntry,
       "cfprComputePhysicalFsmStageInstanceId": cfprComputePhysicalFsmStageInstanceId,
       "cfprComputePhysicalFsmStageDn": cfprComputePhysicalFsmStageDn,
       "cfprComputePhysicalFsmStageRn": cfprComputePhysicalFsmStageRn,
       "cfprComputePhysicalFsmStageDescr": cfprComputePhysicalFsmStageDescr,
       "cfprComputePhysicalFsmStageLastUpdateTime": cfprComputePhysicalFsmStageLastUpdateTime,
       "cfprComputePhysicalFsmStageName": cfprComputePhysicalFsmStageName,
       "cfprComputePhysicalFsmStageOrder": cfprComputePhysicalFsmStageOrder,
       "cfprComputePhysicalFsmStageRetry": cfprComputePhysicalFsmStageRetry,
       "cfprComputePhysicalFsmStageStageStatus": cfprComputePhysicalFsmStageStageStatus,
       "cfprComputePhysicalFsmTaskTable": cfprComputePhysicalFsmTaskTable,
       "cfprComputePhysicalFsmTaskEntry": cfprComputePhysicalFsmTaskEntry,
       "cfprComputePhysicalFsmTaskInstanceId": cfprComputePhysicalFsmTaskInstanceId,
       "cfprComputePhysicalFsmTaskDn": cfprComputePhysicalFsmTaskDn,
       "cfprComputePhysicalFsmTaskRn": cfprComputePhysicalFsmTaskRn,
       "cfprComputePhysicalFsmTaskCompletion": cfprComputePhysicalFsmTaskCompletion,
       "cfprComputePhysicalFsmTaskFlags": cfprComputePhysicalFsmTaskFlags,
       "cfprComputePhysicalFsmTaskItem": cfprComputePhysicalFsmTaskItem,
       "cfprComputePhysicalFsmTaskSeqId": cfprComputePhysicalFsmTaskSeqId,
       "cfprComputePhysicalQualTable": cfprComputePhysicalQualTable,
       "cfprComputePhysicalQualEntry": cfprComputePhysicalQualEntry,
       "cfprComputePhysicalQualInstanceId": cfprComputePhysicalQualInstanceId,
       "cfprComputePhysicalQualDn": cfprComputePhysicalQualDn,
       "cfprComputePhysicalQualRn": cfprComputePhysicalQualRn,
       "cfprComputePhysicalQualModel": cfprComputePhysicalQualModel,
       "cfprComputePlatformTable": cfprComputePlatformTable,
       "cfprComputePlatformEntry": cfprComputePlatformEntry,
       "cfprComputePlatformInstanceId": cfprComputePlatformInstanceId,
       "cfprComputePlatformDn": cfprComputePlatformDn,
       "cfprComputePlatformRn": cfprComputePlatformRn,
       "cfprComputePlatformModel": cfprComputePlatformModel,
       "cfprComputePlatformProductName": cfprComputePlatformProductName,
       "cfprComputePlatformRevision": cfprComputePlatformRevision,
       "cfprComputePlatformVendor": cfprComputePlatformVendor,
       "cfprComputePnuOSImageTable": cfprComputePnuOSImageTable,
       "cfprComputePnuOSImageEntry": cfprComputePnuOSImageEntry,
       "cfprComputePnuOSImageInstanceId": cfprComputePnuOSImageInstanceId,
       "cfprComputePnuOSImageDn": cfprComputePnuOSImageDn,
       "cfprComputePnuOSImageRn": cfprComputePnuOSImageRn,
       "cfprComputePnuOSImageImgLFBFFName": cfprComputePnuOSImageImgLFBFFName,
       "cfprComputePnuOSImageImgLoc": cfprComputePnuOSImageImgLoc,
       "cfprComputePnuOSImageImgName": cfprComputePnuOSImageImgName,
       "cfprComputePoolTable": cfprComputePoolTable,
       "cfprComputePoolEntry": cfprComputePoolEntry,
       "cfprComputePoolInstanceId": cfprComputePoolInstanceId,
       "cfprComputePoolDn": cfprComputePoolDn,
       "cfprComputePoolRn": cfprComputePoolRn,
       "cfprComputePoolAssigned": cfprComputePoolAssigned,
       "cfprComputePoolAssignmentOrder": cfprComputePoolAssignmentOrder,
       "cfprComputePoolDescr": cfprComputePoolDescr,
       "cfprComputePoolIntId": cfprComputePoolIntId,
       "cfprComputePoolName": cfprComputePoolName,
       "cfprComputePoolPolicyLevel": cfprComputePoolPolicyLevel,
       "cfprComputePoolPolicyOwner": cfprComputePoolPolicyOwner,
       "cfprComputePoolSize": cfprComputePoolSize,
       "cfprComputePoolPolicyRefTable": cfprComputePoolPolicyRefTable,
       "cfprComputePoolPolicyRefEntry": cfprComputePoolPolicyRefEntry,
       "cfprComputePoolPolicyRefInstanceId": cfprComputePoolPolicyRefInstanceId,
       "cfprComputePoolPolicyRefDn": cfprComputePoolPolicyRefDn,
       "cfprComputePoolPolicyRefRn": cfprComputePoolPolicyRefRn,
       "cfprComputePoolPolicyRefId": cfprComputePoolPolicyRefId,
       "cfprComputePoolPolicyRefPolicyDn": cfprComputePoolPolicyRefPolicyDn,
       "cfprComputePoolableTable": cfprComputePoolableTable,
       "cfprComputePoolableEntry": cfprComputePoolableEntry,
       "cfprComputePoolableInstanceId": cfprComputePoolableInstanceId,
       "cfprComputePoolableDn": cfprComputePoolableDn,
       "cfprComputePoolableRn": cfprComputePoolableRn,
       "cfprComputePoolableId": cfprComputePoolableId,
       "cfprComputePoolablePoolDn": cfprComputePoolablePoolDn,
       "cfprComputePooledRackUnitTable": cfprComputePooledRackUnitTable,
       "cfprComputePooledRackUnitEntry": cfprComputePooledRackUnitEntry,
       "cfprComputePooledRackUnitInstanceId": cfprComputePooledRackUnitInstanceId,
       "cfprComputePooledRackUnitDn": cfprComputePooledRackUnitDn,
       "cfprComputePooledRackUnitRn": cfprComputePooledRackUnitRn,
       "cfprComputePooledRackUnitAssigned": cfprComputePooledRackUnitAssigned,
       "cfprComputePooledRackUnitAssignedToDn": cfprComputePooledRackUnitAssignedToDn,
       "cfprComputePooledRackUnitId": cfprComputePooledRackUnitId,
       "cfprComputePooledRackUnitOwner": cfprComputePooledRackUnitOwner,
       "cfprComputePooledRackUnitPoolableDn": cfprComputePooledRackUnitPoolableDn,
       "cfprComputePooledRackUnitPrevAssignedToDn": cfprComputePooledRackUnitPrevAssignedToDn,
       "cfprComputePooledSlotTable": cfprComputePooledSlotTable,
       "cfprComputePooledSlotEntry": cfprComputePooledSlotEntry,
       "cfprComputePooledSlotInstanceId": cfprComputePooledSlotInstanceId,
       "cfprComputePooledSlotDn": cfprComputePooledSlotDn,
       "cfprComputePooledSlotRn": cfprComputePooledSlotRn,
       "cfprComputePooledSlotAssigned": cfprComputePooledSlotAssigned,
       "cfprComputePooledSlotAssignedToDn": cfprComputePooledSlotAssignedToDn,
       "cfprComputePooledSlotChassisId": cfprComputePooledSlotChassisId,
       "cfprComputePooledSlotOwner": cfprComputePooledSlotOwner,
       "cfprComputePooledSlotPoolableDn": cfprComputePooledSlotPoolableDn,
       "cfprComputePooledSlotPrevAssignedToDn": cfprComputePooledSlotPrevAssignedToDn,
       "cfprComputePooledSlotSlotId": cfprComputePooledSlotSlotId,
       "cfprComputePoolingPolicyTable": cfprComputePoolingPolicyTable,
       "cfprComputePoolingPolicyEntry": cfprComputePoolingPolicyEntry,
       "cfprComputePoolingPolicyInstanceId": cfprComputePoolingPolicyInstanceId,
       "cfprComputePoolingPolicyDn": cfprComputePoolingPolicyDn,
       "cfprComputePoolingPolicyRn": cfprComputePoolingPolicyRn,
       "cfprComputePoolingPolicyDescr": cfprComputePoolingPolicyDescr,
       "cfprComputePoolingPolicyIntId": cfprComputePoolingPolicyIntId,
       "cfprComputePoolingPolicyName": cfprComputePoolingPolicyName,
       "cfprComputePoolingPolicyPolicyLevel": cfprComputePoolingPolicyPolicyLevel,
       "cfprComputePoolingPolicyPolicyOwner": cfprComputePoolingPolicyPolicyOwner,
       "cfprComputePoolingPolicyPoolDn": cfprComputePoolingPolicyPoolDn,
       "cfprComputePoolingPolicyQualifier": cfprComputePoolingPolicyQualifier,
       "cfprComputePsuControlTable": cfprComputePsuControlTable,
       "cfprComputePsuControlEntry": cfprComputePsuControlEntry,
       "cfprComputePsuControlInstanceId": cfprComputePsuControlInstanceId,
       "cfprComputePsuControlDn": cfprComputePsuControlDn,
       "cfprComputePsuControlRn": cfprComputePsuControlRn,
       "cfprComputePsuControlClusterState": cfprComputePsuControlClusterState,
       "cfprComputePsuControlDescr": cfprComputePsuControlDescr,
       "cfprComputePsuControlInputPowerState": cfprComputePsuControlInputPowerState,
       "cfprComputePsuControlIntId": cfprComputePsuControlIntId,
       "cfprComputePsuControlName": cfprComputePsuControlName,
       "cfprComputePsuControlOperQualifier": cfprComputePsuControlOperQualifier,
       "cfprComputePsuControlOperState": cfprComputePsuControlOperState,
       "cfprComputePsuControlOutputPowerState": cfprComputePsuControlOutputPowerState,
       "cfprComputePsuControlPolicyLevel": cfprComputePsuControlPolicyLevel,
       "cfprComputePsuControlPolicyOwner": cfprComputePsuControlPolicyOwner,
       "cfprComputePsuControlRedundancy": cfprComputePsuControlRedundancy,
       "cfprComputePsuPolicyTable": cfprComputePsuPolicyTable,
       "cfprComputePsuPolicyEntry": cfprComputePsuPolicyEntry,
       "cfprComputePsuPolicyInstanceId": cfprComputePsuPolicyInstanceId,
       "cfprComputePsuPolicyDn": cfprComputePsuPolicyDn,
       "cfprComputePsuPolicyRn": cfprComputePsuPolicyRn,
       "cfprComputePsuPolicyDescr": cfprComputePsuPolicyDescr,
       "cfprComputePsuPolicyIntId": cfprComputePsuPolicyIntId,
       "cfprComputePsuPolicyName": cfprComputePsuPolicyName,
       "cfprComputePsuPolicyPolicyLevel": cfprComputePsuPolicyPolicyLevel,
       "cfprComputePsuPolicyPolicyOwner": cfprComputePsuPolicyPolicyOwner,
       "cfprComputePsuPolicyRedundancy": cfprComputePsuPolicyRedundancy,
       "cfprComputeQualTable": cfprComputeQualTable,
       "cfprComputeQualEntry": cfprComputeQualEntry,
       "cfprComputeQualInstanceId": cfprComputeQualInstanceId,
       "cfprComputeQualDn": cfprComputeQualDn,
       "cfprComputeQualRn": cfprComputeQualRn,
       "cfprComputeQualDescr": cfprComputeQualDescr,
       "cfprComputeQualIntId": cfprComputeQualIntId,
       "cfprComputeQualName": cfprComputeQualName,
       "cfprComputeQualPolicyLevel": cfprComputeQualPolicyLevel,
       "cfprComputeQualPolicyOwner": cfprComputeQualPolicyOwner,
       "cfprComputeRackQualTable": cfprComputeRackQualTable,
       "cfprComputeRackQualEntry": cfprComputeRackQualEntry,
       "cfprComputeRackQualInstanceId": cfprComputeRackQualInstanceId,
       "cfprComputeRackQualDn": cfprComputeRackQualDn,
       "cfprComputeRackQualRn": cfprComputeRackQualRn,
       "cfprComputeRackQualMaxId": cfprComputeRackQualMaxId,
       "cfprComputeRackQualMinId": cfprComputeRackQualMinId,
       "cfprComputeRackUnitTable": cfprComputeRackUnitTable,
       "cfprComputeRackUnitEntry": cfprComputeRackUnitEntry,
       "cfprComputeRackUnitInstanceId": cfprComputeRackUnitInstanceId,
       "cfprComputeRackUnitDn": cfprComputeRackUnitDn,
       "cfprComputeRackUnitRn": cfprComputeRackUnitRn,
       "cfprComputeRackUnitAdminPower": cfprComputeRackUnitAdminPower,
       "cfprComputeRackUnitAdminState": cfprComputeRackUnitAdminState,
       "cfprComputeRackUnitAssignedToDn": cfprComputeRackUnitAssignedToDn,
       "cfprComputeRackUnitAssociation": cfprComputeRackUnitAssociation,
       "cfprComputeRackUnitAvailability": cfprComputeRackUnitAvailability,
       "cfprComputeRackUnitAvailableMemory": cfprComputeRackUnitAvailableMemory,
       "cfprComputeRackUnitCheckPoint": cfprComputeRackUnitCheckPoint,
       "cfprComputeRackUnitConnPath": cfprComputeRackUnitConnPath,
       "cfprComputeRackUnitConnStatus": cfprComputeRackUnitConnStatus,
       "cfprComputeRackUnitDescr": cfprComputeRackUnitDescr,
       "cfprComputeRackUnitDiscovery": cfprComputeRackUnitDiscovery,
       "cfprComputeRackUnitFltAggr": cfprComputeRackUnitFltAggr,
       "cfprComputeRackUnitFsmDescr": cfprComputeRackUnitFsmDescr,
       "cfprComputeRackUnitFsmFlags": cfprComputeRackUnitFsmFlags,
       "cfprComputeRackUnitFsmPrev": cfprComputeRackUnitFsmPrev,
       "cfprComputeRackUnitFsmProgr": cfprComputeRackUnitFsmProgr,
       "cfprComputeRackUnitFsmRmtInvErrCode": cfprComputeRackUnitFsmRmtInvErrCode,
       "cfprComputeRackUnitFsmRmtInvErrDescr": cfprComputeRackUnitFsmRmtInvErrDescr,
       "cfprComputeRackUnitFsmRmtInvRslt": cfprComputeRackUnitFsmRmtInvRslt,
       "cfprComputeRackUnitFsmStageDescr": cfprComputeRackUnitFsmStageDescr,
       "cfprComputeRackUnitFsmStamp": cfprComputeRackUnitFsmStamp,
       "cfprComputeRackUnitFsmStatus": cfprComputeRackUnitFsmStatus,
       "cfprComputeRackUnitFsmTry": cfprComputeRackUnitFsmTry,
       "cfprComputeRackUnitId": cfprComputeRackUnitId,
       "cfprComputeRackUnitIntId": cfprComputeRackUnitIntId,
       "cfprComputeRackUnitLc": cfprComputeRackUnitLc,
       "cfprComputeRackUnitLcTs": cfprComputeRackUnitLcTs,
       "cfprComputeRackUnitLocalId": cfprComputeRackUnitLocalId,
       "cfprComputeRackUnitLowVoltageMemory": cfprComputeRackUnitLowVoltageMemory,
       "cfprComputeRackUnitManagingInst": cfprComputeRackUnitManagingInst,
       "cfprComputeRackUnitMemorySpeed": cfprComputeRackUnitMemorySpeed,
       "cfprComputeRackUnitMfgTime": cfprComputeRackUnitMfgTime,
       "cfprComputeRackUnitModel": cfprComputeRackUnitModel,
       "cfprComputeRackUnitName": cfprComputeRackUnitName,
       "cfprComputeRackUnitNumOfAdaptors": cfprComputeRackUnitNumOfAdaptors,
       "cfprComputeRackUnitNumOfCores": cfprComputeRackUnitNumOfCores,
       "cfprComputeRackUnitNumOfCoresEnabled": cfprComputeRackUnitNumOfCoresEnabled,
       "cfprComputeRackUnitNumOfCpus": cfprComputeRackUnitNumOfCpus,
       "cfprComputeRackUnitNumOfEthHostIfs": cfprComputeRackUnitNumOfEthHostIfs,
       "cfprComputeRackUnitNumOfFcHostIfs": cfprComputeRackUnitNumOfFcHostIfs,
       "cfprComputeRackUnitNumOfThreads": cfprComputeRackUnitNumOfThreads,
       "cfprComputeRackUnitOperPower": cfprComputeRackUnitOperPower,
       "cfprComputeRackUnitOperQualifier": cfprComputeRackUnitOperQualifier,
       "cfprComputeRackUnitOperState": cfprComputeRackUnitOperState,
       "cfprComputeRackUnitOperability": cfprComputeRackUnitOperability,
       "cfprComputeRackUnitOriginalUuid": cfprComputeRackUnitOriginalUuid,
       "cfprComputeRackUnitPartNumber": cfprComputeRackUnitPartNumber,
       "cfprComputeRackUnitPolicyLevel": cfprComputeRackUnitPolicyLevel,
       "cfprComputeRackUnitPolicyOwner": cfprComputeRackUnitPolicyOwner,
       "cfprComputeRackUnitPresence": cfprComputeRackUnitPresence,
       "cfprComputeRackUnitRevision": cfprComputeRackUnitRevision,
       "cfprComputeRackUnitSerial": cfprComputeRackUnitSerial,
       "cfprComputeRackUnitServerId": cfprComputeRackUnitServerId,
       "cfprComputeRackUnitTotalMemory": cfprComputeRackUnitTotalMemory,
       "cfprComputeRackUnitUsrLbl": cfprComputeRackUnitUsrLbl,
       "cfprComputeRackUnitUuid": cfprComputeRackUnitUuid,
       "cfprComputeRackUnitVendor": cfprComputeRackUnitVendor,
       "cfprComputeRackUnitVersionHolder": cfprComputeRackUnitVersionHolder,
       "cfprComputeRackUnitVid": cfprComputeRackUnitVid,
       "cfprComputeRackUnitPostState": cfprComputeRackUnitPostState,
       "cfprComputeRackUnitFsmTable": cfprComputeRackUnitFsmTable,
       "cfprComputeRackUnitFsmEntry": cfprComputeRackUnitFsmEntry,
       "cfprComputeRackUnitFsmInstanceId": cfprComputeRackUnitFsmInstanceId,
       "cfprComputeRackUnitFsmDn": cfprComputeRackUnitFsmDn,
       "cfprComputeRackUnitFsmRn": cfprComputeRackUnitFsmRn,
       "cfprComputeRackUnitFsmCompletionTime": cfprComputeRackUnitFsmCompletionTime,
       "cfprComputeRackUnitFsmCurrentFsm": cfprComputeRackUnitFsmCurrentFsm,
       "cfprComputeRackUnitFsmDescrData": cfprComputeRackUnitFsmDescrData,
       "cfprComputeRackUnitFsmFsmStatus": cfprComputeRackUnitFsmFsmStatus,
       "cfprComputeRackUnitFsmProgress": cfprComputeRackUnitFsmProgress,
       "cfprComputeRackUnitFsmRmtErrCode": cfprComputeRackUnitFsmRmtErrCode,
       "cfprComputeRackUnitFsmRmtErrDescr": cfprComputeRackUnitFsmRmtErrDescr,
       "cfprComputeRackUnitFsmRmtRslt": cfprComputeRackUnitFsmRmtRslt,
       "cfprComputeRackUnitFsmStageTable": cfprComputeRackUnitFsmStageTable,
       "cfprComputeRackUnitFsmStageEntry": cfprComputeRackUnitFsmStageEntry,
       "cfprComputeRackUnitFsmStageInstanceId": cfprComputeRackUnitFsmStageInstanceId,
       "cfprComputeRackUnitFsmStageDn": cfprComputeRackUnitFsmStageDn,
       "cfprComputeRackUnitFsmStageRn": cfprComputeRackUnitFsmStageRn,
       "cfprComputeRackUnitFsmStageDescrData": cfprComputeRackUnitFsmStageDescrData,
       "cfprComputeRackUnitFsmStageLastUpdateTime": cfprComputeRackUnitFsmStageLastUpdateTime,
       "cfprComputeRackUnitFsmStageName": cfprComputeRackUnitFsmStageName,
       "cfprComputeRackUnitFsmStageOrder": cfprComputeRackUnitFsmStageOrder,
       "cfprComputeRackUnitFsmStageRetry": cfprComputeRackUnitFsmStageRetry,
       "cfprComputeRackUnitFsmStageStageStatus": cfprComputeRackUnitFsmStageStageStatus,
       "cfprComputeRackUnitFsmTaskTable": cfprComputeRackUnitFsmTaskTable,
       "cfprComputeRackUnitFsmTaskEntry": cfprComputeRackUnitFsmTaskEntry,
       "cfprComputeRackUnitFsmTaskInstanceId": cfprComputeRackUnitFsmTaskInstanceId,
       "cfprComputeRackUnitFsmTaskDn": cfprComputeRackUnitFsmTaskDn,
       "cfprComputeRackUnitFsmTaskRn": cfprComputeRackUnitFsmTaskRn,
       "cfprComputeRackUnitFsmTaskCompletion": cfprComputeRackUnitFsmTaskCompletion,
       "cfprComputeRackUnitFsmTaskFlags": cfprComputeRackUnitFsmTaskFlags,
       "cfprComputeRackUnitFsmTaskItem": cfprComputeRackUnitFsmTaskItem,
       "cfprComputeRackUnitFsmTaskSeqId": cfprComputeRackUnitFsmTaskSeqId,
       "cfprComputeRackUnitMbTempStatsTable": cfprComputeRackUnitMbTempStatsTable,
       "cfprComputeRackUnitMbTempStatsEntry": cfprComputeRackUnitMbTempStatsEntry,
       "cfprComputeRackUnitMbTempStatsInstanceId": cfprComputeRackUnitMbTempStatsInstanceId,
       "cfprComputeRackUnitMbTempStatsDn": cfprComputeRackUnitMbTempStatsDn,
       "cfprComputeRackUnitMbTempStatsRn": cfprComputeRackUnitMbTempStatsRn,
       "cfprComputeRackUnitMbTempStatsAmbientTemp": cfprComputeRackUnitMbTempStatsAmbientTemp,
       "cfprComputeRackUnitMbTempStatsAmbientTempAvg": cfprComputeRackUnitMbTempStatsAmbientTempAvg,
       "cfprComputeRackUnitMbTempStatsAmbientTempMax": cfprComputeRackUnitMbTempStatsAmbientTempMax,
       "cfprComputeRackUnitMbTempStatsAmbientTempMin": cfprComputeRackUnitMbTempStatsAmbientTempMin,
       "cfprComputeRackUnitMbTempStatsFrontTemp": cfprComputeRackUnitMbTempStatsFrontTemp,
       "cfprComputeRackUnitMbTempStatsFrontTempAvg": cfprComputeRackUnitMbTempStatsFrontTempAvg,
       "cfprComputeRackUnitMbTempStatsFrontTempMax": cfprComputeRackUnitMbTempStatsFrontTempMax,
       "cfprComputeRackUnitMbTempStatsFrontTempMin": cfprComputeRackUnitMbTempStatsFrontTempMin,
       "cfprComputeRackUnitMbTempStatsIntervals": cfprComputeRackUnitMbTempStatsIntervals,
       "cfprComputeRackUnitMbTempStatsIoh1Temp": cfprComputeRackUnitMbTempStatsIoh1Temp,
       "cfprComputeRackUnitMbTempStatsIoh1TempAvg": cfprComputeRackUnitMbTempStatsIoh1TempAvg,
       "cfprComputeRackUnitMbTempStatsIoh1TempMax": cfprComputeRackUnitMbTempStatsIoh1TempMax,
       "cfprComputeRackUnitMbTempStatsIoh1TempMin": cfprComputeRackUnitMbTempStatsIoh1TempMin,
       "cfprComputeRackUnitMbTempStatsIoh2Temp": cfprComputeRackUnitMbTempStatsIoh2Temp,
       "cfprComputeRackUnitMbTempStatsIoh2TempAvg": cfprComputeRackUnitMbTempStatsIoh2TempAvg,
       "cfprComputeRackUnitMbTempStatsIoh2TempMax": cfprComputeRackUnitMbTempStatsIoh2TempMax,
       "cfprComputeRackUnitMbTempStatsIoh2TempMin": cfprComputeRackUnitMbTempStatsIoh2TempMin,
       "cfprComputeRackUnitMbTempStatsRearTemp": cfprComputeRackUnitMbTempStatsRearTemp,
       "cfprComputeRackUnitMbTempStatsRearTempAvg": cfprComputeRackUnitMbTempStatsRearTempAvg,
       "cfprComputeRackUnitMbTempStatsRearTempMax": cfprComputeRackUnitMbTempStatsRearTempMax,
       "cfprComputeRackUnitMbTempStatsRearTempMin": cfprComputeRackUnitMbTempStatsRearTempMin,
       "cfprComputeRackUnitMbTempStatsSuspect": cfprComputeRackUnitMbTempStatsSuspect,
       "cfprComputeRackUnitMbTempStatsThresholded": cfprComputeRackUnitMbTempStatsThresholded,
       "cfprComputeRackUnitMbTempStatsTimeCollected": cfprComputeRackUnitMbTempStatsTimeCollected,
       "cfprComputeRackUnitMbTempStatsUpdate": cfprComputeRackUnitMbTempStatsUpdate,
       "cfprComputeRackUnitMbTempStatsHistTable": cfprComputeRackUnitMbTempStatsHistTable,
       "cfprComputeRackUnitMbTempStatsHistEntry": cfprComputeRackUnitMbTempStatsHistEntry,
       "cfprComputeRackUnitMbTempStatsHistInstanceId": cfprComputeRackUnitMbTempStatsHistInstanceId,
       "cfprComputeRackUnitMbTempStatsHistDn": cfprComputeRackUnitMbTempStatsHistDn,
       "cfprComputeRackUnitMbTempStatsHistRn": cfprComputeRackUnitMbTempStatsHistRn,
       "cfprComputeRackUnitMbTempStatsHistAmbientTemp": cfprComputeRackUnitMbTempStatsHistAmbientTemp,
       "cfprComputeRackUnitMbTempStatsHistAmbientTempAvg": cfprComputeRackUnitMbTempStatsHistAmbientTempAvg,
       "cfprComputeRackUnitMbTempStatsHistAmbientTempMax": cfprComputeRackUnitMbTempStatsHistAmbientTempMax,
       "cfprComputeRackUnitMbTempStatsHistAmbientTempMin": cfprComputeRackUnitMbTempStatsHistAmbientTempMin,
       "cfprComputeRackUnitMbTempStatsHistFrontTemp": cfprComputeRackUnitMbTempStatsHistFrontTemp,
       "cfprComputeRackUnitMbTempStatsHistFrontTempAvg": cfprComputeRackUnitMbTempStatsHistFrontTempAvg,
       "cfprComputeRackUnitMbTempStatsHistFrontTempMax": cfprComputeRackUnitMbTempStatsHistFrontTempMax,
       "cfprComputeRackUnitMbTempStatsHistFrontTempMin": cfprComputeRackUnitMbTempStatsHistFrontTempMin,
       "cfprComputeRackUnitMbTempStatsHistId": cfprComputeRackUnitMbTempStatsHistId,
       "cfprComputeRackUnitMbTempStatsHistIoh1Temp": cfprComputeRackUnitMbTempStatsHistIoh1Temp,
       "cfprComputeRackUnitMbTempStatsHistIoh1TempAvg": cfprComputeRackUnitMbTempStatsHistIoh1TempAvg,
       "cfprComputeRackUnitMbTempStatsHistIoh1TempMax": cfprComputeRackUnitMbTempStatsHistIoh1TempMax,
       "cfprComputeRackUnitMbTempStatsHistIoh1TempMin": cfprComputeRackUnitMbTempStatsHistIoh1TempMin,
       "cfprComputeRackUnitMbTempStatsHistIoh2Temp": cfprComputeRackUnitMbTempStatsHistIoh2Temp,
       "cfprComputeRackUnitMbTempStatsHistIoh2TempAvg": cfprComputeRackUnitMbTempStatsHistIoh2TempAvg,
       "cfprComputeRackUnitMbTempStatsHistIoh2TempMax": cfprComputeRackUnitMbTempStatsHistIoh2TempMax,
       "cfprComputeRackUnitMbTempStatsHistIoh2TempMin": cfprComputeRackUnitMbTempStatsHistIoh2TempMin,
       "cfprComputeRackUnitMbTempStatsHistMostRecent": cfprComputeRackUnitMbTempStatsHistMostRecent,
       "cfprComputeRackUnitMbTempStatsHistRearTemp": cfprComputeRackUnitMbTempStatsHistRearTemp,
       "cfprComputeRackUnitMbTempStatsHistRearTempAvg": cfprComputeRackUnitMbTempStatsHistRearTempAvg,
       "cfprComputeRackUnitMbTempStatsHistRearTempMax": cfprComputeRackUnitMbTempStatsHistRearTempMax,
       "cfprComputeRackUnitMbTempStatsHistRearTempMin": cfprComputeRackUnitMbTempStatsHistRearTempMin,
       "cfprComputeRackUnitMbTempStatsHistSuspect": cfprComputeRackUnitMbTempStatsHistSuspect,
       "cfprComputeRackUnitMbTempStatsHistThresholded": cfprComputeRackUnitMbTempStatsHistThresholded,
       "cfprComputeRackUnitMbTempStatsHistTimeCollected": cfprComputeRackUnitMbTempStatsHistTimeCollected,
       "cfprComputeRtcBatteryTable": cfprComputeRtcBatteryTable,
       "cfprComputeRtcBatteryEntry": cfprComputeRtcBatteryEntry,
       "cfprComputeRtcBatteryInstanceId": cfprComputeRtcBatteryInstanceId,
       "cfprComputeRtcBatteryDn": cfprComputeRtcBatteryDn,
       "cfprComputeRtcBatteryRn": cfprComputeRtcBatteryRn,
       "cfprComputeRtcBatteryId": cfprComputeRtcBatteryId,
       "cfprComputeRtcBatteryLocationDn": cfprComputeRtcBatteryLocationDn,
       "cfprComputeRtcBatteryModel": cfprComputeRtcBatteryModel,
       "cfprComputeRtcBatteryOperQualifierReason": cfprComputeRtcBatteryOperQualifierReason,
       "cfprComputeRtcBatteryOperState": cfprComputeRtcBatteryOperState,
       "cfprComputeRtcBatteryOperability": cfprComputeRtcBatteryOperability,
       "cfprComputeRtcBatteryPerf": cfprComputeRtcBatteryPerf,
       "cfprComputeRtcBatteryPower": cfprComputeRtcBatteryPower,
       "cfprComputeRtcBatteryPresence": cfprComputeRtcBatteryPresence,
       "cfprComputeRtcBatteryRevision": cfprComputeRtcBatteryRevision,
       "cfprComputeRtcBatterySerial": cfprComputeRtcBatterySerial,
       "cfprComputeRtcBatteryThermal": cfprComputeRtcBatteryThermal,
       "cfprComputeRtcBatteryVendor": cfprComputeRtcBatteryVendor,
       "cfprComputeRtcBatteryVoltage": cfprComputeRtcBatteryVoltage,
       "cfprComputeScrubPolicyTable": cfprComputeScrubPolicyTable,
       "cfprComputeScrubPolicyEntry": cfprComputeScrubPolicyEntry,
       "cfprComputeScrubPolicyInstanceId": cfprComputeScrubPolicyInstanceId,
       "cfprComputeScrubPolicyDn": cfprComputeScrubPolicyDn,
       "cfprComputeScrubPolicyRn": cfprComputeScrubPolicyRn,
       "cfprComputeScrubPolicyBiosSettingsScrub": cfprComputeScrubPolicyBiosSettingsScrub,
       "cfprComputeScrubPolicyDescr": cfprComputeScrubPolicyDescr,
       "cfprComputeScrubPolicyDiskScrub": cfprComputeScrubPolicyDiskScrub,
       "cfprComputeScrubPolicyFlexFlashScrub": cfprComputeScrubPolicyFlexFlashScrub,
       "cfprComputeScrubPolicyIntId": cfprComputeScrubPolicyIntId,
       "cfprComputeScrubPolicyName": cfprComputeScrubPolicyName,
       "cfprComputeScrubPolicyPolicyLevel": cfprComputeScrubPolicyPolicyLevel,
       "cfprComputeScrubPolicyPolicyOwner": cfprComputeScrubPolicyPolicyOwner,
       "cfprComputeServerDiscPolicyTable": cfprComputeServerDiscPolicyTable,
       "cfprComputeServerDiscPolicyEntry": cfprComputeServerDiscPolicyEntry,
       "cfprComputeServerDiscPolicyInstanceId": cfprComputeServerDiscPolicyInstanceId,
       "cfprComputeServerDiscPolicyDn": cfprComputeServerDiscPolicyDn,
       "cfprComputeServerDiscPolicyRn": cfprComputeServerDiscPolicyRn,
       "cfprComputeServerDiscPolicyAction": cfprComputeServerDiscPolicyAction,
       "cfprComputeServerDiscPolicyDescr": cfprComputeServerDiscPolicyDescr,
       "cfprComputeServerDiscPolicyFsmDescr": cfprComputeServerDiscPolicyFsmDescr,
       "cfprComputeServerDiscPolicyFsmPrev": cfprComputeServerDiscPolicyFsmPrev,
       "cfprComputeServerDiscPolicyFsmProgr": cfprComputeServerDiscPolicyFsmProgr,
       "cfprComputeServerDiscPolicyFsmRmtInvErrCode": cfprComputeServerDiscPolicyFsmRmtInvErrCode,
       "cfprComputeServerDiscPolicyFsmRmtInvErrDescr": cfprComputeServerDiscPolicyFsmRmtInvErrDescr,
       "cfprComputeServerDiscPolicyFsmRmtInvRslt": cfprComputeServerDiscPolicyFsmRmtInvRslt,
       "cfprComputeServerDiscPolicyFsmStageDescr": cfprComputeServerDiscPolicyFsmStageDescr,
       "cfprComputeServerDiscPolicyFsmStamp": cfprComputeServerDiscPolicyFsmStamp,
       "cfprComputeServerDiscPolicyFsmStatus": cfprComputeServerDiscPolicyFsmStatus,
       "cfprComputeServerDiscPolicyFsmTry": cfprComputeServerDiscPolicyFsmTry,
       "cfprComputeServerDiscPolicyIntId": cfprComputeServerDiscPolicyIntId,
       "cfprComputeServerDiscPolicyName": cfprComputeServerDiscPolicyName,
       "cfprComputeServerDiscPolicyPolicyLevel": cfprComputeServerDiscPolicyPolicyLevel,
       "cfprComputeServerDiscPolicyPolicyOwner": cfprComputeServerDiscPolicyPolicyOwner,
       "cfprComputeServerDiscPolicyQualifier": cfprComputeServerDiscPolicyQualifier,
       "cfprComputeServerDiscPolicyScrubPolicyName": cfprComputeServerDiscPolicyScrubPolicyName,
       "cfprComputeServerDiscPolicyFsmTable": cfprComputeServerDiscPolicyFsmTable,
       "cfprComputeServerDiscPolicyFsmEntry": cfprComputeServerDiscPolicyFsmEntry,
       "cfprComputeServerDiscPolicyFsmInstanceId": cfprComputeServerDiscPolicyFsmInstanceId,
       "cfprComputeServerDiscPolicyFsmDn": cfprComputeServerDiscPolicyFsmDn,
       "cfprComputeServerDiscPolicyFsmRn": cfprComputeServerDiscPolicyFsmRn,
       "cfprComputeServerDiscPolicyFsmCompletionTime": cfprComputeServerDiscPolicyFsmCompletionTime,
       "cfprComputeServerDiscPolicyFsmCurrentFsm": cfprComputeServerDiscPolicyFsmCurrentFsm,
       "cfprComputeServerDiscPolicyFsmDescrData": cfprComputeServerDiscPolicyFsmDescrData,
       "cfprComputeServerDiscPolicyFsmFsmStatus": cfprComputeServerDiscPolicyFsmFsmStatus,
       "cfprComputeServerDiscPolicyFsmProgress": cfprComputeServerDiscPolicyFsmProgress,
       "cfprComputeServerDiscPolicyFsmRmtErrCode": cfprComputeServerDiscPolicyFsmRmtErrCode,
       "cfprComputeServerDiscPolicyFsmRmtErrDescr": cfprComputeServerDiscPolicyFsmRmtErrDescr,
       "cfprComputeServerDiscPolicyFsmRmtRslt": cfprComputeServerDiscPolicyFsmRmtRslt,
       "cfprComputeServerDiscPolicyFsmStageTable": cfprComputeServerDiscPolicyFsmStageTable,
       "cfprComputeServerDiscPolicyFsmStageEntry": cfprComputeServerDiscPolicyFsmStageEntry,
       "cfprComputeServerDiscPolicyFsmStageInstanceId": cfprComputeServerDiscPolicyFsmStageInstanceId,
       "cfprComputeServerDiscPolicyFsmStageDn": cfprComputeServerDiscPolicyFsmStageDn,
       "cfprComputeServerDiscPolicyFsmStageRn": cfprComputeServerDiscPolicyFsmStageRn,
       "cfprComputeServerDiscPolicyFsmStageDescrData": cfprComputeServerDiscPolicyFsmStageDescrData,
       "cfprComputeServerDiscPolicyFsmStageLastUpdateTime": cfprComputeServerDiscPolicyFsmStageLastUpdateTime,
       "cfprComputeServerDiscPolicyFsmStageName": cfprComputeServerDiscPolicyFsmStageName,
       "cfprComputeServerDiscPolicyFsmStageOrder": cfprComputeServerDiscPolicyFsmStageOrder,
       "cfprComputeServerDiscPolicyFsmStageRetry": cfprComputeServerDiscPolicyFsmStageRetry,
       "cfprComputeServerDiscPolicyFsmStageStageStatus": cfprComputeServerDiscPolicyFsmStageStageStatus,
       "cfprComputeServerDiscPolicyFsmTaskTable": cfprComputeServerDiscPolicyFsmTaskTable,
       "cfprComputeServerDiscPolicyFsmTaskEntry": cfprComputeServerDiscPolicyFsmTaskEntry,
       "cfprComputeServerDiscPolicyFsmTaskInstanceId": cfprComputeServerDiscPolicyFsmTaskInstanceId,
       "cfprComputeServerDiscPolicyFsmTaskDn": cfprComputeServerDiscPolicyFsmTaskDn,
       "cfprComputeServerDiscPolicyFsmTaskRn": cfprComputeServerDiscPolicyFsmTaskRn,
       "cfprComputeServerDiscPolicyFsmTaskCompletion": cfprComputeServerDiscPolicyFsmTaskCompletion,
       "cfprComputeServerDiscPolicyFsmTaskFlags": cfprComputeServerDiscPolicyFsmTaskFlags,
       "cfprComputeServerDiscPolicyFsmTaskItem": cfprComputeServerDiscPolicyFsmTaskItem,
       "cfprComputeServerDiscPolicyFsmTaskSeqId": cfprComputeServerDiscPolicyFsmTaskSeqId,
       "cfprComputeServerMgmtPolicyTable": cfprComputeServerMgmtPolicyTable,
       "cfprComputeServerMgmtPolicyEntry": cfprComputeServerMgmtPolicyEntry,
       "cfprComputeServerMgmtPolicyInstanceId": cfprComputeServerMgmtPolicyInstanceId,
       "cfprComputeServerMgmtPolicyDn": cfprComputeServerMgmtPolicyDn,
       "cfprComputeServerMgmtPolicyRn": cfprComputeServerMgmtPolicyRn,
       "cfprComputeServerMgmtPolicyAction": cfprComputeServerMgmtPolicyAction,
       "cfprComputeServerMgmtPolicyDescr": cfprComputeServerMgmtPolicyDescr,
       "cfprComputeServerMgmtPolicyIntId": cfprComputeServerMgmtPolicyIntId,
       "cfprComputeServerMgmtPolicyName": cfprComputeServerMgmtPolicyName,
       "cfprComputeServerMgmtPolicyPolicyLevel": cfprComputeServerMgmtPolicyPolicyLevel,
       "cfprComputeServerMgmtPolicyPolicyOwner": cfprComputeServerMgmtPolicyPolicyOwner,
       "cfprComputeServerMgmtPolicyQualifier": cfprComputeServerMgmtPolicyQualifier,
       "cfprComputeSlotQualTable": cfprComputeSlotQualTable,
       "cfprComputeSlotQualEntry": cfprComputeSlotQualEntry,
       "cfprComputeSlotQualInstanceId": cfprComputeSlotQualInstanceId,
       "cfprComputeSlotQualDn": cfprComputeSlotQualDn,
       "cfprComputeSlotQualRn": cfprComputeSlotQualRn,
       "cfprComputeSlotQualMaxId": cfprComputeSlotQualMaxId,
       "cfprComputeSlotQualMinId": cfprComputeSlotQualMinId}
)
